# MetricPY

Este repositório contém tanto o backend quanto o frontend para o projeto MetricPY. Abaixo estão as instruções resumidas para configurar e executar ambos (para quem tem conhecimento nas respectivas linguagens, do contrário acessar a pasta de cada projeto e seguir o readme de forma detalhada).

## Clonar o Repositório

Primeiro, clone o repositório usando Git:

\`\`\`bash
git clone https://github.com/alexsander-coder/metricPY.git
\`\`\`

## Backend

O backend do projeto é construído usando FastAPI.

### Configuração do Backend

1. Navegue até a pasta do backend:

   \`\`\`bash
   cd metricPY/backend
   \`\`\`
2. Instale as dependências necessárias:

   \`\`\`bash
   pip install fastapi uvicorn
   \`\`\`

### Executar o Servidor Backend

Para iniciar o servidor backend, execute:

\`\`\`bash
uvicorn main:fast --reload
\`\`\`

O servidor estará rodando em [http://localhost:8000](http://localhost:8000).

## Frontend

O frontend do projeto é construído usando [VUE 3 com Typescript].

### Configuração do Frontend

1. Navegue até a pasta do frontend:

   \`\`\`bash
   cd metricPY/frontend
   \`\`\`
2. Instale as dependências necessárias:

   \`\`\`bash
   npm install
   \`\`\`

### Executar o Servidor Frontend

Para iniciar o servidor frontend, execute:

\`\`\`bash
npm run dev
\`\`\`

O servidor frontend estará disponível em [http://localhost:3000](http://localhost:3000) (ajuste a URL conforme necessário).

## Mais Informações

Para mais detalhes sobre como trabalhar com cada parte do projeto, consulte os READMEs individuais nas respectivas pastas de backend e frontend.
