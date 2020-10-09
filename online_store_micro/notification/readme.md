# Note Setup Python:
- Run Script: python -m venv virtualenvi --> merupakan folder library kita
- Run Script: virtualenvi\Scripts\activate 
- Run Script: python -m pip install --upgrade pip
- Create file req.txt > jalankan Scirpt untuk install tools: "pip install -r req.txt"
- Running project: flask run

# Migration DB:
- Run Script: flask db init
- Run Script : flask db upgrade

# Untuk membuat tabel baru ke DB
- Run Script : flask db migrate -m "notification file"
- Run Script : flask db upgrade

# Melihat Instalasi di Aplikasi:
- Run Script : pip list

# Untuk Jalankan Worker Redis Queue:
- Tambah atau buat 2 Terminal,
- Running script deri terminal: "rq worker",
- Running juga Flask Run.