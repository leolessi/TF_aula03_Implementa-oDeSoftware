FROM mysql:latest

ENV MYSQL_DATABASE=alunos
ENV MYSQL_USER=faat
ENV MYSQL_PASSWORD=faat
ENV MYSQL_ROOT_PASSWORD=faat

COPY ./alunos.sql /docker-entrypoint-initdb.d/

EXPOSE 3306