# Portfolio Web App - EC2 + Flask + S3

Este é um projeto de portfólio que demonstra uma aplicação web simples usando **Flask** hospedada em **EC2** da AWS, com integração a **S3** para upload e listagem de arquivos.  

---

## 🚀 Tecnologias utilizadas

- **AWS EC2**: Hospedagem da aplicação Flask  
- **AWS S3**: Armazenamento de arquivos  
- **Flask**: Framework web em Python  
- **Python 3**: Linguagem da aplicação  
- **HTML/CSS**: Front-end básico  

---

## 📂 Estrutura do projeto

portfolio-app/

├── app.py # Aplicação Flask principal

├── templates/

│ └── index.html # Página principal

├── static/

│ └── style.css # Estilos CSS

├── uploads/ # Pasta temporária para upload

---

## ⚙️ Configuração e execução

1. **Clonar o repositório:**

```bash
git clone <URL-DO-SEU-REPO>
cd portfolio-app/website
```

2. **Instalar dependências no EC2:**

```bash
sudo yum install python3-pip -y
python3 -m pip install --upgrade pip
python3 -m pip install flask boto3
```

3. **Configurar IAM Role na EC2 com permissões de S3 (AmazonS3FullAccess)**

Não é necessário usar Access Keys, a aplicação usa a IAM Role da EC2 automaticamente.

4. **Rodar a aplicação:**

```bash
python3 app.py
```

5. Acessar via navegador:

```bash
(http://<IP-PÚBLICO-DA-EC2>:5000)
```

---

## 📝 Funcionalidades

Listagem de arquivos armazenados no S3

Upload automático de arquivos para o S3

Front-end simples em HTML/CSS

---

## 💡 Observações:

* Esta aplicação usa a porta 5000 no Flask (modo desenvolvimento).

* Para produção, recomenda-se usar Gunicorn + Nginx para rodar na porta 80.

* Se o bucket S3 não existir, a aplicação não quebra (tratamento de erro incluso).

📸 Screenshot Resultado Final: 

![Homepage](portfolio-app/screenshots/resultado.jpg)
