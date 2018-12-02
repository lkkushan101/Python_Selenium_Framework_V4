import PyPDF2
from Utility.SilentDownloader import download_file
def verify_online_pdf(url,text_to_verify):
    download_file(url,'sample.pdf')
    pdfFileObject = open('../DownloadedFiles/sample.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
    count = pdfReader.numPages
    for i in range(count):
        page = pdfReader.getPage(i)
        print(page.extractText())
        if page.extractText().find(text_to_verify):
            print('Text found...')