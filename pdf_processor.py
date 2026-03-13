import fitz
import os

def extract_pdf_data(file):

    doc = fitz.open(stream=file.read(), filetype="pdf")

    text = ""
    images = []

    for page_index in range(len(doc)):
        page = doc[page_index]

        text += page.get_text()

        image_list = page.get_images()

        for img in image_list:
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            images.append(image_bytes)

    return text, images