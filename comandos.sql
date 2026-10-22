create database rpg;

create table personagem(
    id_personagem integer not null auto_increment,
    nome_p varchar (100) not null,
    classe_p varchar (100) not null,
    forca_p integer not null,
    destreza_p integer not null,
    vida_p integer not null,
    primary key (id_personagem)) engine=innodb;