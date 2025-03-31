# Web Scraping de Anexos da ANS

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)

Este projeto realiza web scraping na página da [Agência Nacional de Saúde Suplementar (ANS)](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos), para baixar os Anexos I e II em formato PDF e compactá-los em um arquivo ZIP.

## 📌 Funcionalidades

- Acessa a página da ANS
- Aceita automaticamente o aviso de cookies
- Identifica e baixa os PDFs dos Anexos I e II
- Compacta os arquivos baixados em um ZIP

## 🛠 Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [Zipfile](https://docs.python.org/3/library/zipfile.html)
- [Google Chrome e ChromeDriver](https://sites.google.com/chromium.org/driver/)

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o Repositório
```sh
 git clone https://github.com/seu-usuario/seu-repositorio.git
 cd seu-repositorio
```

### 2️⃣ Criar e Ativar um Ambiente Virtual (Opcional, mas Recomendado)
```sh
 python -m venv venv
 source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3️⃣ Instalar as Dependências
```sh
 pip install -r requirements.txt
```

### 4️⃣ Instalar o ChromeDriver
Este projeto utiliza o Selenium para automação do navegador.
1. Verifique a versão do seu Google Chrome acessando: `chrome://settings/help`
2. Baixe a versão correspondente do [ChromeDriver](https://sites.google.com/chromium.org/driver/)
3. Extraia o executável e atualize o caminho no código:
   ```python
   driver_path = "C:/caminho/para/chromedriver.exe"  # Ajuste para seu sistema
   ```

### 5️⃣ Executar o Script
```sh
 python main.py
```

Os arquivos serão baixados na pasta `anexos/` e compactados em `anexos.zip`.

## 📝 Estrutura do Projeto
```
.
├── anexos/                 # Pasta onde os PDFs serão salvos
├── main.py                 # Script principal
├── requirements.txt        # Lista de dependências
├── README.md               # Documentação do projeto
```

## 📄 Licença
Este projeto está sob a licença MIT.

## 👨‍💻 Contato
Conecte-se comigo no [LinkedIn](https://linkedin.com/in/thiagopiassi).

