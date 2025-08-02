# 🏥 TLG ADMIN - Sistema de Gestão de Clínica
Um sistema desktop desenvolvido em Python para realizar o gerenciamento de pacientes, médicos e agendamentos de uma clínica médica.

## 📝 Criação do Projeto
Desenvolvido a partir de um trabalho acadêmico da disciplina de Projeto e Implementação de Banco de Dados, onde o script inicial do banco foi criado em MySQL. Este projeto evoluiu o conceito para uma aplicação desktop completa com o padrão de arquitetura MVC (Model-View-Controller), utilizando Python para a lógica de negócio e SQLite para a persistência de dados.
Com uma interface moderna feita em CustomTkinter, a aplicação permite o cadastro e a consulta de todas as entidades do sistema, garantindo a integridade dos dados através de um robusto sistema de validações e do uso de chaves estrangeiras no banco de dados.

## ✨ Funcionalidades
### <b>Módulos de Cadastro:</b>
- Pacientes: Registro completo com dados pessoais, endereço e informações de contato.
- Médicos: Cadastro de profissionais, incluindo especialidade e salário.
- Agendamentos: Interface para marcar consultas, associando um paciente a um médico em uma data e hora específicas, com controle de status.
- Planos de Saúde: Vínculo de pacientes a planos, com registro de número de carteirinha e validade.
- Diagnósticos: Cadastro do histórico de doenças de um paciente.

### <b>Módulos de Consulta:</b>
- Visualização clara e formatada de todos os registros do sistema, incluindo: Agendamentos, Médicos, Pacientes, Doenças, Especialidades e um relatório consolidado da situação dos pacientes.

### <b>Banco de Dados:</b>
- Utilizo SQLite 3, o que torna o sistema portátil e de fácil instalação, sem a necessidade de um servidor de banco de dados externo.

## 🛠️ Tecnologias Utilizadas
- Linguagem: Python
- Interface Gráfica (GUI): CustomTkinter
- Banco de Dados: SQLite 3

## 📂 Estrutura do Projeto

- `clinica.db`
- `main.py`
- `readme.md`
  
- `📂 controller`
  - `controller.py`
- `📂 model`
  - `model.py`
  - `setup.py`
  - `seed_data.py`
- `📂 view`
    - `pag_inicial.py`
  - `📂 cadastros`
    - `cad_agendamentos.py`
    - `cad_medicos.py`
    - `cad_pacientes.py`
    - `cad_pacientes_doencas.py`
    - `cad_pacientes_planos.py`
  - `📂 consultas`
    - `con_agendamentos.py`
    - `con_doencas.py`
    - `con_especialidades.py`
    - `con_medicos.py`
    - `con_pacientes.py`
    - `con_pacientes_doencas.py`

## 🚀 Como Executar o Programa
- Clone o repositório (git clone ...).
- Instale as dependências: pip install customtkinter.
- Execute o arquivo principal: python main.py
