buku = []  # Variabel global untuk menyimpan data Buku

def show_data():
    if len(buku) <= 0:
        print("BELUM ADA DATA")
    else:
        for indeks, judul in enumerate(buku):
            print("[%d] %s" % (indeks, judul))

def insert_data():
    buku_baru = input("Judul Buku: ")
    buku.append(buku_baru)

def edit_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if indeks >= len(buku):
        print("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru

def delete_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if indeks >= len(buku):
        print("ID salah")
    else:
        buku.pop(indeks)

def show_menu():
    print("\n")
    print("----------- MENU ----------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    menu = input("PILIH MENU> ")
    print("\n")
    if menu == '1':
        show_data()
    elif menu == '2':
        insert_data()
    elif menu == '3':
        edit_data()
    elif menu == '4':
        delete_data()
    elif menu == '5':
        exit()
    else:
        print("Salah pilih!")

if __name__ == "__main__":
    while True:
        show_menu()
