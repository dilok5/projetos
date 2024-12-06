create database aula;

use aula;

create table cadastros(
	id int primary key,
    nome varchar(200) not null,
    cidade varchar(50),
    uf varchar(2),
    email varchar(200),
    valor decimal(10,2) 
    );
    
select * from cadastros;
    