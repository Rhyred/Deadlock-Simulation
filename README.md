# Deadlock-Simulation

Proyek ini berisi simulasi sederhana untuk menunjukkan bagaimana **deadlock** dapat terjadi pada proses/ thread yang saling berebut sumber daya.

## Deskripsi

Program Python pada file `deadlock_141.py` membuat beberapa thread dan beberapa lock. Setiap thread akan mengambil satu lock terlebih dahulu, lalu mencoba mengambil lock berikutnya. Karena urutan pengambilan lock dibuat saling berlawanan, program dapat berhenti di tengah jalan ketika semua thread saling menunggu lock milik thread lain.

## Tujuan

- Memahami konsep deadlock pada pemrograman paralel.
- Melihat bagaimana lock bekerja pada multithreading.
- Practice Quiz – synchronization.

## Cara Menjalankan

Jalankan file Python berikut:

```bash
python deadlock_141.py
```

## Struktur Program

- `deadlock_141.py` : file utama simulasi deadlock.
- `Readme.md` : penjelasan proyek.

## Catatan

Output program bisa berhenti sebelum selesai karena thread-thread saling menunggu lock. Itu memang bagian dari simulasi deadlock.

Program ini juga bisa dianalisis menggunakan tool `pystack` di Python untuk melihat stack atau aktivitas thread, terutama pada environment yang mendukungnya seperti Linux atau WSL.

### Copyright

Rhyred @ 152024141 Robi Rizki Permana
