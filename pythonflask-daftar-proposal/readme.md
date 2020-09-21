## Konfigurasi Modul Pendaftaran Proposal Skripsi:
1. Membuat Database dengan nama "db_akademik".
2. Membuat koneksi database pada .flaskenv
3. Melakukan instalasi Library Virtualenvi Python :
```
python -m venv virtualenvi,
```
4. Menalankan Script Python ke mode virtual :
```
virtualenvi\Scripts\activate
```
5. Melakukan upgrade dan instal PIP Python :
```
python -m pip install --upgrade pip
```
6. Membuat file req.txt dan lakukan instalasi tools dengan Run Script :
```
pip install -r req.txt
```
7. Melakukan proses Flask DB Init, Migrate, & Upgrade struktur tabel & membuat relasi antar tabel yang dibutuhkan pada Model. Berupa: users, prodis, proposals, & berkas_proposal dengan perintah :
```
flask db init; flask db migrate; flask db upgrade
```
8. Membuat File & Script Controllers untuk proses CRUD data ke masing-masing tabel DB. Berupa: userController, prodiController, proposalController, & berkasProposalController,

9. Membuat File & Script Route untuk proses POST, GET, PUT, & DELETE. Berupa: routeUser, routeProdi, routeProposal, & routeFile,

10. Mendaftarkan file Model & Route pada file "__init__.py"

11. Melakukan test aplikasi (Flask Run) Daftar Sidang untuk proses CRUD, mulai dari modul User, Prodi, Proposal, & fileProposal,
```
flask run
```
12. Mencoba melakukan CRUD dengan Post, Get, Put, & Delete data melalui Postman, kemudian cek hasil proses ke masing-masing tabel penyimanan data.

13. Install & konfigurasi JWT Token User Login & Refresh Token pada userController & proposalController,

14. Install & konfigurasi Flask-Mail, untuk melakukan proses kirim Email secara otomatis apabila melakukan POST tambah data User dan Daftar Proposal pada flaskenv, config.py, & controller,

- TERIMA KASIH -




