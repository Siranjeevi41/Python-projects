import PyPDF2

def decrypt_pdf(input_path, output_path, password):
    with open(input_path, 'rb') as input_file:
        reader = PyPDF2.PdfReader(input_file)
        
        if reader.is_encrypted:
            reader.decrypt(password)
            writer = PyPDF2.PdfWriter()

            for page_num in range(len(reader.pages)):
                writer.add_page(reader.pages[page_num])

            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            print(f'Successfully decrypted the file and saved it as {output_path}')
        else:
            print('The file is not encrypted.')

input_file = r'C:\Users\siranjeevi\Dropbox\PC\Downloads\statement.pdf'
output_file = r'C:\Users\siranjeevi\Dropbox\PC\Downloads\statement_decrypted.pdf'
password = '2001@4411'

decrypt_pdf(input_file, output_file, password)
