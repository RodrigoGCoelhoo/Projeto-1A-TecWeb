from database import Database
from database import Note

db = Database('banco')
db.add(Note(title='Pão doce', content='Abra o pão e coloque o seu suco em pó favorito.'))
db.add(Note(title='Fazer', content='Lembrar de tomar água'))

print(db.get_all())