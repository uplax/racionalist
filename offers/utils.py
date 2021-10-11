import tempfile
from decimal import Decimal
from pathlib import Path

from borb.pdf.canvas.color.color import X11Color
from borb.pdf.canvas.font.font import Font
from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.canvas.layout.image.barcode import Barcode, BarcodeType
from borb.pdf.canvas.layout.image.image import Image
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable
from borb.pdf.canvas.layout.table.table import TableCell
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF


def generate_pdf(link: str):
    temp = tempfile.TemporaryFile()
    pdf = Document()
    page = Page()

    pdf.append_page(page)
    r: Rectangle = Rectangle(
        Decimal(59),  # x: 0 + page_margin
        Decimal(848 - 84 - 120),  # y: page_height - page_margin - height_of_textbox
        Decimal(595 - 59 * 2),  # width: page_width - 2 * page_margin
        Decimal(125)
    )
    page.append_square_annotation(r, stroke_color=X11Color("Black"))
    font_path: Path = Path(__file__).parent / "static/Oswald-Regular.ttf"
    font: Font = TrueTypeFont.true_type_font_from_file(font_path)
    layout = SingleColumnLayout(page)
    layout.add(
        Image(
            Path(__file__).parent / "static/logo.png",
            width=Decimal(90),
            height=Decimal(40),
            horizontal_alignment=Alignment.CENTERED,
        )
    )
    p: Paragraph = Paragraph(
        """Государственный научный центр Российской Федерации""",
        font=font,
        font_size=Decimal(12),
        padding_left=Decimal(50),
        padding_right=Decimal(50),
        text_alignment=Alignment.CENTERED,
        respect_spaces_in_text=True,
    )
    layout.add(p)
    p: Paragraph = Paragraph(
        """Акционерное общество «НПО «Орион»""",
        font=font,
        font_size=Decimal(12),
        text_alignment=Alignment.CENTERED,
    )
    layout.add(p)
    layout.add(
        Paragraph(
            "Сервис подачи предложений по улушению",
            font=font,
            font_size=Decimal(24),
            text_alignment=Alignment.CENTERED,
            padding_top=Decimal(50)
        )
    )
    layout.add(
        Barcode(
            link,
            width=Decimal(256),
            height=Decimal(256),
            type=BarcodeType.QR,
            horizontal_alignment=Alignment.CENTERED,
        )
    )
    layout.add(
        Paragraph(
            "Для подачи предложений по улушению отсканируйте QR-код",
            font=font,
            font_size=Decimal(12),
            text_alignment=Alignment.CENTERED,
            padding_top=Decimal(50)
        )
    )
    table = FixedColumnWidthTable(number_of_rows=1, number_of_columns=2, padding_top=Decimal(50))
    table.add(
        TableCell(
            Image(
                Path(__file__).parent / "static/89d25289483d05345cedc4996528c09b.png",
                horizontal_alignment=Alignment.CENTERED,
                width=Decimal(24),
                height=Decimal(30),
            )
        )
    )
    table.add(
        TableCell(
            Image(
                Path(__file__).parent / "static/6275ee02308a34225c87445b0e832d5e.png",
                horizontal_alignment=Alignment.CENTERED,
                width=Decimal(60),
                height=Decimal(20),
            )
        )
    )
    table.no_borders()
    layout.add(table)
    PDF.dumps(temp, pdf)
    temp.seek(0)
    return temp
