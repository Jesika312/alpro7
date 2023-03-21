def hitung_vokal(kalimat):
    vokal="a,i,u,e,o,A,I,U,E,O"
    jumlah=0
    for karakter in kalimat:
        # cek satu per satu vokal dari depan
        if karakter in vokal:
            # jika ada 
            jumlah=jumlah+1
    return jumlah
def hitung_white_space(kalimat):
    jumlah=0
    for karakter in kalimat:
        if karakter.isspace()== True:
            jumlah=jumlah+1
    return jumlah

def hitung_konsonan(kalimat):
    
    vokal="a,i,u,e,o,A,I,U,E,O"
    jumlah=0
    for karakter in kalimat:
        if karakter not in vokal and karakter.isalpha():
            jumlah=jumlah+1
    return jumlah
# input     
kalimat=input("masukan sebuah kalimat:")
# proses
jumlah_vokal=hitung_vokal(kalimat)
jumlah_whitespace=hitung_white_space(kalimat)
jumlah_konsonan=hitung_konsonan(kalimat)
# output
print(f'jumlah huruf vokal:{jumlah_vokal}')
print(f'jumlah whitespace:{jumlah_whitespace}')
print(f'jumlah konsonan:{jumlah_konsonan}')