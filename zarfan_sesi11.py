{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b9d59fed-89c2-47a3-a440-22803e1e7535",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "UKA ATNIC UMAK\n",
      "PYTHON HARI BELAJAR SEDANG INI\n",
      "Ak|_| C1nt4 K4m|_|\n",
      "4ku Cinta Kamu\n"
     ]
    }
   ],
   "source": [
    "\n",
    "def reverse_per_kata(kalimat):\n",
    "    kata = kalimat.split()      #dMemisahkan kalimat menjadi list kata-kata berdasarkan spasi\n",
    "    hasil = []                  # Membuat list kosong untuk menyimpan hasil pembalikan per kata\n",
    "    for i in kata:              #looping untuk setiap kata dalam list kata\n",
    "        hasil.append(i[::-1])   #membalikan kata dan mdi tambahkan ke variabel hasil\n",
    "    return ' '.join(hasil)      #menggabungkan kata2 pada variabel hasil dengan ditambahkan spasi\n",
    "\n",
    "print(reverse_per_kata(\"AKU CINTA KAMU\"))\n",
    "# Output: \"UKA ATNIC UMAK\"\n",
    "\n",
    "def urutkan_kalimat(kalimat, urutan):\n",
    "    kata = kalimat.split()            # Memisahkan kalimat menjadi list kata-kata berdasarkan spasi\n",
    "    terurut = []                      # Membuat list kosong untuk menyimpan kata-kata yang sudah diurutkan\n",
    "    for i in urutan:                  #looping elalui setiap indeks dalam list 'urutan'\n",
    "        terurut.append(kata[i - 1])   #menambahkan kata dengan indeks 1 ke variabel terurut \n",
    "    return ' '.join(terurut)          # Menggabungkan kata-kata yang sudah diurutkan menjadi satu kalimat dengan spasi\n",
    "\n",
    "print(urutkan_kalimat(\"HARI INI SEDANG BELAJAR PYTHON\", [5, 1, 4, 3, 2]))\n",
    "# Output: \"PYTHON HARI BELAJAR SEDANG INI\"\n",
    "\n",
    "def ganti_vokal(kalimat, opsi):\n",
    "    vokal_kecil = {'a' : '4', 'i' : '1', 'u' : '|_|', 'e' : '3', 'o' : '0'}  # Dictionary untuk mapping vokal kecil ke karakter pengganti\n",
    "    vokal_besar = {'A' : '4', 'I' : '1', 'U' : '|_|', 'E' : '3', 'O' : '0'}  # Dictionary untuk mapping vokal besar ke karakter pengganti\n",
    "    \n",
    "    hasil = \"\"                                     # String kosong untuk menyimpan hasil penggantian vokal\n",
    "    for huruf in kalimat:                          #loopingmelalui setiap huruf dalam kalimat\n",
    "        if opsi == 1 and huruf in vokal_kecil:     #Jika opsi == 1 dan huruf adalah vokal kecil\n",
    "            hasil += vokal_kecil[huruf]            #ganti dengan karakter sesuai dictionary\n",
    "        elif opsi == 2 and huruf in vokal_besar:   #Jika opsi == 2 dan huruf adalah vokal besar\n",
    "            hasil += vokal_besar[huruf]            #ganti dengan karakter sesuai dictionary\n",
    "        else:\n",
    "            hasil += huruf                         #jika bukan vokal yang ditentukan, biarkan huruf tetap\n",
    "    return hasil\n",
    "\n",
    "print(ganti_vokal(\"Aku Cinta Kamu\", 1))\n",
    "# Output: \"Ak|_| C1nt4 K4m|_|\"\n",
    "print(ganti_vokal(\"Aku Cinta Kamu\", 2))\n",
    "# Output: \"4ku Cinta Kamu\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd9b1c93-4d0a-4bda-9ad0-ae1328ca4951",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
