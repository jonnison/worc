# Worc Selection System

## Descrição do Projeto
  O _service_ prover uma API RESTfull para cadastro de candidatos e seus contatos. Seus principais endpoints são:
  Candidatos:
  * Listar Candidatos : `GET /api/candidate/`
  * Cadastrar Candidatos : `POST /api/candidate/`
  * Mostrar Candidato : `GET /api/candidate/:pk/`
  * Alteração Completa Candidato : `PUT /api/candidate/:pk/`
  * Alteração Parcial Candidato : `PUT /api/candidate/:pk/`
  * Deletar candidato : `DELETE /api/candidate/:pk/`
  * Cadastrar Contato de um Candidato : `POST /api/candidate/:pk/contact/`

  Contatos:
  * Listar Contato : `GET /api/contact/`
  * Cadastrar Contato : `POST /api/contact/`
  * Mostrar Contato : `GET /api/contact/:pk/`
  * Alteração Completa Contato : `PUT /api/contact/:pk/`
  * Alteração Parcial Contato : `PUT /api/contact/:pk/`
  * Deletar Contato : `DELETE /api/contact/:pk/`

  Documentação:
  * API Doc : `/api/docs/`

## Configurações de execução
Todas as configurações de acesso ficam no arquivo **.env** onde devem ser setadas as configurações para execução, os principais itens são:
  * DJANGO_SECRET_KEY : chave secreta do django
  * DEBUG : se a váriavel estiver presente o projeto é  exeucuytado em modo debug
  * DJANGO_ALLOWED_HOSTS : lista hosts aos quais o projeto deve responder, separado por vírgula "`,`"
  * DATABASE_ENGINE: Engine do banco de dados usada, default: `sqlite`
  * DATABASE_NAME: Nome do banco de dados usada, default: `db.sqlite3`
  * DATABASE_USERNAME: Usuário do banco de dados usada, default: `None`
  * DATABASE_PASSWORD: Senha do banco de dados usada, default: `None`
  * DATABASE_HOST: Host do banco de dados usada, default: `None`
  * DATABASE_PORT: Porta do banco de dados usada, default: `None`
  * DATABASE_OPTIONS: Opções do banco de dados usada no formato JSON, default: `{}`
## Executando do Projeto
### Docker
Para executar o projeto com o docker basta clonar o repositório e executar com o docker compose, após isso
```
git clone https://github.com/jonnison/worc.git
docker-compose up -d --build
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

### Linux
Para executar o projeto com o docker basta clonar o repositório, instalar as dependencias, exportar as váriaveis de ambiente e executar o projeto:
```
git clone https://github.com/jonnison/worc.git
export $(cat .env | xargs)
pip install -r requeriments.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## Respostas as SOLICITAÇÕES
### Samuca
Para atualizar nome e sobrenome deve ser acionada a rota `/api/candidate/{id}/` e enviar os dados via método `PATCH` para atualização parcial ou `PUT` para atualização completa dos dados.

Para atualizar o contato deve ser acionada a rota `/api/contact/{id}/` e enviar os dados via método `PATCH` para atualização parcial ou `PUT` para atualização completa dos dados.

### Alfi
  Para adicionar um novo candidato deve ser acionada a rota `/api/candidate/` com o método `POST`.
  
  Para adicionar um novo contato deve ser acionada a rota `/api/candidate/{id}/contact/add/` com o método `POST`. O `id` é o código do candidato ao qual deseja adicionar o contato.

### Fabricio
Ao adicionar um candidato, os dados são retornados na mesma requisição juntamente com um código de status `200` indicando que o contato foi adicionado. Além disso, na listagem dos candidatos é retornado a data de criação do candidato na variável `created_at`. Na listagem e no detalhe do candidato, há uma váriavel `updated_at_contact`, que traz a última atualização dos contatos desse candidato.
