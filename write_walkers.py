from docxtpl import DocxTemplate
from get_yaml import load
from datetime import datetime

data = load('content.yaml')
doc = DocxTemplate("template/template.docx")

name_doc = datetime.now()
name_doc = name_doc.strftime('%d-%m-%Y-%H-%M')
doc.render(data)
doc.save(f'./dist/{name_doc}.docx')
