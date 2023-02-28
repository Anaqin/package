from pkg.modul1 import*
from pkg.modul2 import*
from pkg.hitungan import hitung_nilai

def main():
    #memanggil fungsi fungsi dalam modul 1
    f1()
    f2()
    #memanggil fungsi fungsi dalam modul 2
    f3()
    f4()
    print("Nilai Akhir : ", hitung_nilai(80,90))
main()