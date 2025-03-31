from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import zipfile
import os

# Caminho para o ChromeDriver
driver_path = "C:/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Configuração do serviço do WebDriver
service = Service(driver_path)

# Inicializar o navegador com o serviço
driver = webdriver.Chrome(service=service)

# URL da página
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
driver.get(url)

# Aceitar cookies
try:
    cookie_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='br-button secondary small btn-accept']"))
    )
    cookie_button.click()
    print("Aviso de cookies aceito.")
except Exception as e:
    print("Não foi possível localizar ou aceitar o aviso de cookies:", e)

# Esperar os links carregarem
WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
)

# Primeiro filtro: Localizar todos os links que terminam com .pdf
pdf_links = []
links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    href = link.get_attribute("href")
    if href and "Anexo" in href and href.endswith(".pdf"):
        pdf_links.append(href)

# Segundo filtro: Refinar para apenas "Anexo I" e "Anexo II"
filtered_links = [link for link in pdf_links if "Anexo" and "I" in link or "Anexo" and "II" in link]

# Exibir os links filtrados
print(f"Links encontrados (todos os PDFs): {pdf_links}")
print(f"Links filtrados (Anexo I e Anexo II): {filtered_links}")


# Verificar se os links foram encontrados
if not pdf_links:
    print("Nenhum arquivo PDF correspondente foi encontrado.")
else:
    print(f"Links encontrados: {pdf_links}")

    # Criar pasta para salvar os PDFs
    output_dir = "anexos"
    os.makedirs(output_dir, exist_ok=True)

    # Download dos PDFs
    for idx, pdf_link in enumerate(pdf_links, start=1):
        try:
            response = requests.get(pdf_link)
            response.raise_for_status()
            pdf_name = f"{output_dir}/Anexo-{idx}.pdf"
            with open(pdf_name, "wb") as pdf_file:
                pdf_file.write(response.content)
            print(f"Baixado: {pdf_name}")
        except Exception as e:
            print(f"Erro ao baixar o arquivo {pdf_link}: {e}")

    # Compactar os PDFs em um único arquivo ZIP
    zip_name = "anexos.zip"
    with zipfile.ZipFile(zip_name, "w") as zipf:
        for pdf_file in os.listdir(output_dir):
            zipf.write(os.path.join(output_dir, pdf_file), pdf_file)

    print(f"Anexos compactados em: {zip_name}")
