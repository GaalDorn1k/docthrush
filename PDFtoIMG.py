from pdf2image import convert_from_path
import os
#images = convert_from_path("dac.pdf", 500,poppler_path=r'C:\Program Files\poppler-0.68.0\bin')

#path = "budjet"
def pdf_to_png(path):
    for file in os.listdir(path):
        if file.endswith(".pdf"):
            images = convert_from_path(file, 70,poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
            #for i, image in enumerate(images):
            fname = file +'.png'
            images[0].save(fname, "PNG")
        
        
    for file in os.listdir(path):
        if file.endswith(".PDF"):
            images = convert_from_path(file, 70,poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
            #for i, image in enumerate(images):
            fname = file +'.png'
            images[0].save(fname, "PNG")