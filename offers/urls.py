from django.urls import path

from offers.views import OfferList, OfferDetail, QrCodesList, download, confirmation, create_offer, success, \
    QrCodeUpdate, QrCodeCreate

urlpatterns = [
    path('staff/', OfferList.as_view()),
    path('staff/offers/<int:page>/', OfferList.as_view(), name='offers'),
    path('staff/offers/detail/<int:pk>/', OfferDetail.as_view(), name='offer_detail'),

    path('offers/<uuid:pk>/confirm-agreement/', confirmation, name='confirm_agreement'),
    path('offers/<uuid:pk>/create-offer/', create_offer, name='create_offer'),
    path('offers/<uuid:pk>/success/', success, name='success'),

    path('staff/qr-codes/create/', QrCodeCreate.as_view(), name='qr_codes_create'),
    path('staff/qr-codes/<int:page>/', QrCodesList.as_view(), name='qr_codes'),
    path('staff/qr-codes/<uuid:pk>/update/', QrCodeUpdate.as_view(), name='qr_codes_update'),
    path('staff/qr-codes/<uuid:pk>/download/', download, name='download'),
]
