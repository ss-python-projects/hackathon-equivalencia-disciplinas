## O que é esse repositório?
Esse repositório contém a nossa solução desenvolvida para o Hackathon UniBH 2019-01. O objetivo principal é desenvolver uma solução capaz de, a partir de uma lista de disciplinas **não ofertadas** em um semestre, sugerir disciplinas que estão sendo ofertadas e que são **equivalentes**.

## Desenvolvendo

### Construído com
Esse projeto foi construído usando Python 3.6 e Docker.

### Pré-requisitos
Esse projeto foi inicialmente construído usando [Docker](https://docs.docker.com/get-started/). Usando Docker, você não precisa instalar nenhuma ferramenta adicional, já que uma imagem Docker contém tudo o que você precisa.

No entanto, se de alguma forma você prefere trabalhar com o projeto sem o uso de Docker, você pode instalar cada ferramenta manualmente.

1. [Python 3.6.8](https://www.python.org/downloads/release/python-368/)

### Como rodar

Primeiro instale as dependências do projeto. Para tal, você pode usar o seguinte comando **dentro da pasta do projeto**:

```sh
# Se só possuir o Python 3.6 na máquina
$ pip install -r requirements.txt

# Se possuir mais de um Python na máquina
$ pip3 install -r requirements.txt
```

Depois, basta apenas rodar a aplicação:

```sh
# Se só possuir o Python 3.6 na máquina
$ python src/app.py

# Se possuir mais de um Python na máquina
$ python3 src/app.py
```

## Autores
* [Hugo Carvalho](https://github.com/Hugo-Carvalho)
* [Stanley Sathler](https://github.com/StanleySathler)
