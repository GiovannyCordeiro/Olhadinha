# criar tabelas

path_models="/src/models/"

cd "$path_models/base"
$(python createTables.py)

cd "$path_models/seeders"
$(python PlataformasSeeders.py)
$(python DataCashbackSeeders.py)
