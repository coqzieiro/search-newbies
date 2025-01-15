import PyPDF2

# Caminhos dos arquivos
input_pdf_path = 'lista-fuvest.pdf'
output_txt_path = 'raw_text_fuvest.txt'

def convert_pdf_to_txt(pdf_path, txt_path):
    try:
        # Abrir o arquivo PDF
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            
            # Extrair texto de cada página
            all_text = ''
            for page in reader.pages:
                all_text += page.extract_text() + '\n'

        # Salvar o texto extraído em um arquivo .txt
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(all_text)

        print(f"Arquivo '{txt_path}' gerado com sucesso!")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

# Executar a conversão
convert_pdf_to_txt(input_pdf_path, output_txt_path)