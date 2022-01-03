# Backend Post WebApp Microservice
Microservice that gets all post operations and communicates with front-end and comment-microservice-backend

## About

<p>
  Esse é um projeto para simular uma Microservices Software Architecture básica, qual o backend recebe as requisições de posts para listar todos os posts ao frontend ou criar novos posts, este microservice sincroniza os dados dos comentarios nos posts com o comment-microservice-backend, para manter os dados atualizados.
</p>

### Connected Projects

<p>
  Como esse é um projeto de microservices, ele se conecta com mais dois projetos o quais são:
</p>

- <a href="https://github.com/Rharan-Ru/post-microservice-frontend">Posts Microservice</a> # Frontend service
- <a href="https://github.com/Rharan-Ru/comment-microservice-backend">Comments Microservice</a> # Comments service backend


### How Start The Project?

Antes de iniciar de fato o projeto, você deve configurar seu database em settings.py, veja como fazer isto nesse artigo <a href="https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django">How to use PostgreSQL with Django</a>

Para iniciar o projeto primeiro devemos instalar os pacotes que serão usados:
````
python3 -m venv venv
cd venv/Scripts/activate
pip install -r requirements.txt
````
Então rodamos o projeto, recomendo trocar o superuser do projeto para ter acesso a page admin e também rodar os comandos makemigrations e migrate
````
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
````

### The Future

<p>
  Esse é apenas um projeto básico de microservices, conforme eu avançar meus estudos em arquitetura de software vou trazer mais projetos interessantes e avançados, um passo importante para a arquitetura de microservices é que ela é muito usada com Event Driven Architecture, então vamos botar a cara nos estudos e a mão na massa ainda mais para trazer esses tipos de projetos que são muito legais de se fazer, até breve.
</p>

#### Obrigado por estar aqui.

<p align="center">
  <img src="https://jonchaisson.files.wordpress.com/2021/10/anime-writing.gif" width=70% />
</p>
