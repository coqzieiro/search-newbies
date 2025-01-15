import pandas as pd
import re

# Função para processar o arquivo .txt e extrair os dados

def process_fuvest_txt(file_path, target_courses):
    data = []
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        
        # Ignorar linhas irrelevantes
        if not re.match(r".+\s+\d{3}\.\d{3}\s+\d{3}−\d{2}", line):
            continue

        # Capturar Nome, CPF e Carreira-Curso
        match = re.match(r"(.+?)\s+(\d{3}\.\d{3})\s+(\d{3}−\d{2})", line)
        if match:
            nome = match.group(1).strip()
            cpf = match.group(2)  # CPF parcial
            carreira_curso = match.group(3)

            # Verificar se o código do curso está nos cursos de interesse
            if carreira_curso in target_courses:
                curso_info = target_courses[carreira_curso]
                carreira = curso_info["carreira"]
                curso_nome = curso_info["nome"]

                # Adicionar os dados ao resultado
                data.append({
                    "Nome": nome,
                    "CPF": cpf,
                    "Código Carreira-Curso": carreira_curso,
                    "Carreira": carreira,
                    "Curso": curso_nome,
                })
            else:
                # Diagnóstico: curso ignorado
                print(f"Curso ignorado: {line}")

    return data

# Função para salvar os dados processados em CSV
def save_to_csv(data, output_file):
    df = pd.DataFrame(data)
    df_sorted = df.sort_values(by=["Código Carreira-Curso", "Nome"])
    df_sorted.to_csv(output_file, index=False, encoding="utf-8")

# Dicionário de cursos de interesse
target_courses = {
    "106−08": {
        "nome": "Arquitetura e Urbanismo (Integral)",
        "carreira": "Arquitetura"
    },
    "700−01": {
        "nome": "Ciências Físicas e Biomoleculares (Integral)",
        "carreira": "Ciências Físicas"
    },
    "710−03": {
        "nome": "Ciências Exatas com Habilitação em Física, Química ou Matemática (Noturno)",
        "carreira": "Ciências Exatas"
    },
    "715−06": {
        "nome": "Ciências de Computação (Integral)",
        "carreira": "Computação"
    },
    "715−09": {
        "nome": "Ciência de Dados (Integral)",
        "carreira": "Computação"
    },
    "716−10": {
        "nome": "Sistemas de Informação (Noturno)",
        "carreira": "Computação"
    },
    "725−12": {
        "nome": "Engenharia Aeronáutica (Integral)",
        "carreira": "Engenharia Aeronáutica"
    },
    "730−13": {
        "nome": "Engenharia Ambiental (Integral)",
        "carreira": "Engenharia Ambiental"
    },
    "735−14": {
        "nome": "Engenharia Civil (Integral)",
        "carreira": "Engenharia Civil"
    },
    "745−17": {
        "nome": "Engenharia de Materiais e Manufatura (Integral)",
        "carreira": "Engenharia de Materiais e Manufatura"
    },
    "750−18": {
        "nome": "Engenharia Elétrica: Ênfase em Eletrônica (Integral)",
        "carreira": "Engenharia Elétrica"
    },
    "750−19": {
        "nome": "Engenharia Elétrica: Ênfase em Sistemas de Energia e Automação (Integral)",
        "carreira": "Engenharia Elétrica"
    },
    "750−20": {
        "nome": "Engenharia de Computação (Integral)",
        "carreira": "Engenharia de Computação"
    },
    "755−21": {
        "nome": "Engenharia Mecânica (Integral)",
        "carreira": "Engenharia Mecânica"
    },
    "755−22": {
        "nome": "Engenharia Mecatrônica (Integral)",
        "carreira": "Engenharia Mecatrônica"
    },
    "755−23": {
        "nome": "Engenharia de Produção (Integral)",
        "carreira": "Engenharia de Produção"
    },
    "765−44": {
        "nome": "Física (Integral)",
        "carreira": "Física"
    },
       "765−45": {
        "nome": "Física Computacional (Integral)",
        "carreira": "Física"
    },
    "765−54": {
        "nome": "Matemática Aplicada e Computação Científica (Integral)",
        "carreira": "Matemática"
    },
    "765−55": {
        "nome": "Matemática (Integral)",
        "carreira": "Matemática"
    },
    "765−56": {
        "nome": "Estatística e Ciência de Dados (Noturno)",
        "carreira": "Estatística"
    },
    "800−69": {
        "nome": "Química – Habilitação Fundamental ou Habilitação Tecnológica com Ênfases em: Alimentos; Ambiental; Gestão de Qualidade e Materiais (Integral)",
        "carreira": "Química"
    }
}

# Caminho do arquivo .txt e saída
input_txt_file = "raw_text_fuvest.txt"
output_csv_file = "fuvest_processed.csv"

# Processar o arquivo e salvar os dados em CSV
processed_data = process_fuvest_txt(input_txt_file, target_courses)
save_to_csv(processed_data, output_csv_file)

print(f"Arquivo CSV gerado com sucesso: {output_csv_file}")