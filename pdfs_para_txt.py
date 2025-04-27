import os
import fitz  # PyMuPDF

def pdfs_para_txt(pasta_pdf, pasta_txt):
    # Garante que a pasta de saída existe
    os.makedirs(pasta_txt, exist_ok=True)
    
    # Lista todos os arquivos da pasta
    arquivos = [f for f in os.listdir(pasta_pdf) if f.endswith('.pdf')]
    
    for arquivo in arquivos:
        caminho_pdf = os.path.join(pasta_pdf, arquivo)
        nome_base = os.path.splitext(arquivo)[0]
        caminho_txt = os.path.join(pasta_txt, f"{nome_base}.txt")
        
        # Abre o PDF
        doc = fitz.open(caminho_pdf)
        
        texto_total = ""
        for pagina in doc:
            texto_total += pagina.get_text()
        
        # Salva o texto extraído em um arquivo .txt
        with open(caminho_txt, 'w', encoding='utf-8') as f:
            f.write(texto_total)
        
        print(f"Convertido: {arquivo} → {nome_base}.txt")
