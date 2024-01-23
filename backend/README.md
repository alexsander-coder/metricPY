# MetricPY

Descrição do seu projeto MetricPY.

## Pré-requisitos

Antes de começar, você precisa ter instalado:

- [Python 3.7+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## Instalação e Execução

Siga estas instruções para executar o projeto localmente.

### 1. Clonar o Repositório

Clone o repositório para a sua máquina local:

```bash
git clone https://github.com/alexsander-coder/metricPY.git
cd metricPY
e por fim cd backend

```

### 2. Configurar o Ambiente Virtual

É recomendável usar um ambiente virtual para gerenciar as dependências:

```bash
python -m venv venv
# Ative o ambiente virtual
# Windows
.\venv\Scripts\activate
# macOS e Linux
source venv/bin/activate
```

### 3. Instalar Dependências

Instale o FastAPI, Uvicorn e outras dependências necessárias:

```bash
pip install fastapi uvicorn
```

### 4. Executar o Servidor

Inicie o servidor FastAPI com Uvicorn:

```bash
uvicorn main:app --reload
```

Acesse o servidor em [http://localhost:8000](http://localhost:8000)/upload. O flag `--reload` faz o servidor reiniciar automaticamente após mudanças no código, útil durante o desenvolvimento.
