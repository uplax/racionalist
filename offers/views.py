from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from offers.forms import OfferForm
from offers.models import Offer, OfferPoint
from offers.utils import generate_pdf


class OfferList(LoginRequiredMixin, ListView):
    model = Offer
    paginate_by = 15


class OfferDetail(LoginRequiredMixin, DetailView):
    model = Offer

    def get(self, *args, **kwargs):
        res = super().get(*args, **kwargs)
        if not self.object.is_readed:
            self.object.is_readed = True
            self.object.save()
        return res


class OfferCreate(CreateView):
    model = OfferPoint


class QrCodesList(LoginRequiredMixin, ListView):
    model = OfferPoint
    paginate_by = 15


class QrCodeCreate(CreateView):
    model = OfferPoint
    fields = ['name', 'description']

    def get_success_url(self):
        return reverse('qr_codes', kwargs={'page': 1})


class QrCodeUpdate(UpdateView):
    model = OfferPoint
    fields = ['name', 'description']

    def get_success_url(self):
        return reverse('qr_codes', kwargs={'page': 1})


def confirmation(request, pk):
    if request.session.get('confirmed', None):
        return redirect('create_offer', pk)
    if request.method == 'POST':
        request.session['confirmed'] = request.POST.get('confirmation', False)
        if not request.session['confirmed']:
            return redirect('confirm_agreement', str(pk))
        return redirect('create_offer', str(pk))
    return render(request, 'offers/confirm_agreement.html')


def create_offer(request, pk):
    if not request.session.get('confirmed', None):
        return redirect('confirm_agreement', pk)
    if request.method == 'POST':
        form_result = {
            'offer_from': pk,
            **{k: v for k, v in request.POST.items()},
        }
        form = OfferForm(form_result)
        if form.is_valid():
            res = form.save()
            request.session['offer_id'] = res.pk
            request.session['confirmed'] = False
            return redirect('success', str(pk))
    return render(request, 'offers/create_offer.html', {
        'form': OfferForm
    })


def success(request, pk):
    if not request.session.get('offer_id'):
        return redirect('confirm_agreement', str(pk))
    return render(request, 'offers/success.html')


def download(request, pk):
    host = request.get_host()
    offer_point = OfferPoint.objects.get(pk=pk)
    url = f'http://{host}/offers/{str(pk)}/confirm-agreement/'
    temp = generate_pdf(url)
    return FileResponse(temp, as_attachment=True, filename=f'{offer_point.name}.pdf')


def index(request):
    return redirect('offers_index')
