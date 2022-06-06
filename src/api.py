from datetime import datetime
import hashlib
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from PyPDF2 import PdfFileWriter


app = FastAPI()

app.mount("/public", StaticFiles(directory="public"), name="public")


@app.get('/')
def hello():
    return {"message": "hello world"}


@app.post('/resume', status_code=201)
def receive_resume_data(request: Request):
    pdf_name: str = create_pdf_name()
    content: str = "teste"
    download_url: str = f'{request.base_url}public/pdf/{pdf_name}'
    create_pdf(pdf_name, content)

    return {"message": download_url}


def create_pdf_name() -> str:
    hash_name: str = hashlib.sha256(
        str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")).encode('utf-8'))
    return hash_name.hexdigest() + ".pdf"


def create_pdf(file_name, data):
    pdf_writer = PdfFileWriter()
    with open(f'public/pdf/{file_name}', 'wb') as pdf:
        pdf_writer.addBlankPage(width=72, height=72)
        pdf_writer.write(pdf)
