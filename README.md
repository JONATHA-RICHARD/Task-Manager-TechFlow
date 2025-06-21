# 📝 Projeto: Task Manager - TechFlow Solutions 🚀

## ✅ Objetivo do Projeto:

Desenvolver um sistema simples de gerenciamento de tarefas para uma startup de logística, permitindo:

- Cadastro de novas tarefas
- Listagem de tarefas existentes
- Atualização de status das tarefas (A Fazer, Em Progresso, Concluído)
- Exclusão de tarefas
- Visualização do fluxo de trabalho via Kanban

---

## ✅ Escopo:

Sistema web básico com foco em demonstrar conceitos de Engenharia de Software:

- CRUD de tarefas
- Kanban no GitHub Projects
- Testes automatizados (exemplo simples com GitHub Actions)
- Simulação de mudança de escopo
- Modelagem UML (Casos de Uso e Diagrama de Classes)

---

## ✅ Metodologia Adotada:

- **SCRUM:** Organização do desenvolvimento em Sprints
- **Kanban:** Acompanhamento das tarefas no GitHub Projects com as colunas:

| A Fazer | Em Progresso | Concluído |
|------|------|------|
| Criar estrutura do projeto | Implementar CRUD | Escrever README.md |
| Configurar CI Pipeline | Criar testes | Criar diagrama UML |
| Documentar mudança de escopo | Atualizar Kanban | Fazer commits finais |

---

## ✅ Instruções de Execução do Sistema:

> **Obs.: Ainda preciso criar o código no VS Code e subir. Aqui está o passo a passo que vou seguir:**

1. Criar o código do sistema (exemplo: Python com Flask ou JavaScript com Node.js)
2. Adicionar o código na pasta do repositório (ex.: `/src/` ou na raiz)
3. Criar um arquivo `requirements.txt` (caso Python)
4. Exemplo de execução (se for Python):

```bash
git clone https://github.com/SEU-USUARIO/Task-Manager-TechFlow.git
cd Task-Manager-TechFlow
pip install -r requirements.txt
python app.py
```

5. Exemplo de execução dos testes:

```bash
pytest
```

> Se o projeto for em JavaScript: usar `npm install` e `node app.js`

---

## ✅ Controle de Qualidade - CI com GitHub Actions:

Vamos implementar um pipeline de **Integração Contínua (CI)** com **GitHub Actions**, que vai:

- Rodar os testes automaticamente a cada novo push
- Garantir que o código que sobe pro repositório não tenha falhas

Exemplo de configuração (arquivo `.github/workflows/ci.yml`):

```yaml
name: CI Pipeline

on: [push, pull_request]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        pip install pytest
    - name: Run tests
      run: |
        pytest
```

---

## ✅ Gestão de Mudanças - Simulação de Mudança de Escopo:

Durante o desenvolvimento, o cliente solicitou a adição da funcionalidade de **"Filtro por Prioridade das Tarefas"**.

Mudanças feitas:

- Criada nova tarefa no Kanban
- Implementada nova função no código (filtro)
- Documentada esta alteração aqui no README.md

---

## ✅ Requisitos Funcionais:

| Código | Descrição |
|------|-------------|
| RF01 | Criar tarefas |
| RF02 | Listar tarefas |
| RF03 | Atualizar tarefas |
| RF04 | Excluir tarefas |
| RF05 | Filtrar tarefas por prioridade (Mudança de escopo) |

---

## ✅ Requisitos Não Funcionais:

- RNF01: Sistema com tempo de resposta inferior a 2 segundos
- RNF02: Código com comentários explicativos
- RNF03: Estruturação em boas práticas de pastas e arquivos

---

## ✅ Modelagem UML:

- **Diagrama de Casos de Uso:**  
Usuário interagindo com o sistema para criar, listar, atualizar, excluir e filtrar tarefas.

- **Diagrama de Classes:**  
Classe principal: `Task`, com atributos como `id`, `title`, `description`, `status`, `priority`.

*(Os diagramas estão disponíveis na pasta `/docs/` do repositório)*

---

## ✅ Histórico de Commits:

O repositório contém pelo menos 10 commits significativos, com mensagens claras e descritivas, como:

- Estrutura inicial
- CRUD de tarefas
- Pipeline CI
- Testes automatizados
- README.md
- UML Diagramas
- Simulação de mudança de escopo

---

## ✅ Respostas às Perguntas Norteadoras:

1. **Principais causas de falhas em projetos ágeis e como o GitHub ajuda a mitigar:**

Falhas de comunicação, má gestão de tarefas e falta de controle de qualidade. O GitHub organiza tarefas com Kanban, mantém histórico com commits e executa testes automáticos.

2. **Quem são os principais beneficiados por um sistema de gerenciamento ágil?**

Desenvolvedores, gestores de projeto e clientes. Todos acompanham o progresso em tempo real.

3. **Como o uso de ferramentas de controle de qualidade pode garantir software confiável?**

Executando testes automatizados com GitHub Actions para validar o código antes de qualquer entrega.

4. **Principais desafios ao implementar mudanças e como lidar:**

Reorganizar o backlog, atualizar o Kanban, comunicar a equipe. No projeto, isso foi feito com o Kanban e o README.

5. **Como as metodologias ágeis foram aplicadas:**

SCRUM para organizar as entregas por Sprint, e Kanban para visualizar o fluxo de trabalho.

---

## ✅ Conclusão:

O projeto proporcionou uma experiência completa de aplicação dos conceitos de Engenharia de Software, com organização, planejamento, desenvolvimento prático e controle de qualidade.

---
