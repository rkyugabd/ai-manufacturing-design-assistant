from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
import re



def create_pdf(
    project_name: str,
    report_content: str
):

    # Create safe filename

    safe_name = re.sub(
        r'[^a-zA-Z0-9_ -]',
        '',
        project_name
    )

    safe_name = safe_name.replace(
        ' ',
        '_'
    )


    filename = (
        f"{safe_name}_Engineering_Report.pdf"
    )


    filepath = os.path.join(
        "generated_reports",
        filename
    )


    # Create folder if not exist

    os.makedirs(
        "generated_reports",
        exist_ok=True
    )



    document = SimpleDocTemplate(
        filepath
    )


    styles = getSampleStyleSheet()


    content = []



    title = Paragraph(
        f"AI Manufacturing Design Assistant<br/>{project_name}",
        styles["Title"]
    )


    content.append(title)

    content.append(
        Spacer(1, 20)
    )



    # Split report into paragraphs

    paragraphs = report_content.split("\n")



    for line in paragraphs:

        if line.strip():

            p = Paragraph(
                line,
                styles["BodyText"]
            )

            content.append(p)

            content.append(
                Spacer(1, 10)
            )



    document.build(content)


    return filepath