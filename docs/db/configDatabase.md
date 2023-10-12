# Configurando banco de dados 

Para fazer com que o banco de dados funcione adequadamento é necessario criar as tabelas e
alocar os dados no banco de dados, siga as seguintes etapas.

## Criando as tabelas

Entre no container com o comando:
```cmd
docker exec -it back_olhadinha_dev bash
```

Dentro do container navegue ate a pasta `models/base`
```cmd
cd models/base/
```

Execute o arquivo `createTables.py`
```cmd
python createTables.py
```

Esses comandos servem para criar sequencialmente a tabela de plataformas e dos dados,
siga a ordem sequencialmente, caso contrario averá **erros**.

## Alocando dados (semeando o banco)

Agora volte um diretorio e entre na pasta seeders
```cmd
cd .. && cd seeders
```

Execute o arquivo na seguinte ordem
```cmd
python PlataformasSeeders.py
```

```cmd
python DataCashbackSeeders.py
```