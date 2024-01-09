from PyPDF2 import PdfReader, PdfWriter

def set_password(input_pdf, output_pdf, password):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PdfReader(file)
        pdf_writer = PdfWriter()

        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

        pdf_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == "__main__":
    input_file = input("Введите имя входного PDF-файла: ")+'.pdf'
    output_file = input("Введите имя для выходного PDF-файла: ")+'.pdf'
    password = input("Введите пароль для PDF-файла: ")

    set_password(input_file, output_file, password)