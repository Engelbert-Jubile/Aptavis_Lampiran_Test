class Club:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.matches_played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_scored = 0
        self.goals_conceded = 0
        self.points = 0

clubs = []

def input_data():
    name = input("Masukkan Nama Klub: ")
    city = input("Masukkan Kota Klub: ")

    # Validasi data tidak boleh sama
    if any(c.name == name or c.city == city for c in clubs):
        print("Data klub sudah ada. Silakan masukkan data yang berbeda.")
        input_data()
    else:
        clubs.append(Club(name, city))
        print("Data klub berhasil disimpan.")

def input_score():
    print("Input Skor Pertandingan:")
    match_data = []

    while True:
        klub1 = input("Klub 1: ")
        klub2 = input("Klub 2: ")

        # Validasi data pertandingan tidak boleh sama
        if any((m[0] == klub1 and m[1] == klub2) or (m[0] == klub2 and m[1] == klub1) for m in match_data):
            print("Data pertandingan sudah ada. Silakan masukkan data yang berbeda.")
        else:
            score1 = int(input("Skor Klub 1: "))
            score2 = int(input("Skor Klub 2: "))

            match_data.append((klub1, klub2, score1, score2))

            add_more = input("Tambah pertandingan lagi? (yes/no): ").lower()
            if add_more != 'yes':
                break

    # Proses perhitungan point
    for match in match_data:
        klub1, klub2, score1, score2 = match
        club1 = next(c for c in clubs if c.name == klub1)
        club2 = next(c for c in clubs if c.name == klub2)

        club1.matches_played += 1
        club2.matches_played += 1
        club1.goals_scored += score1
        club2.goals_scored += score2
        club1.goals_conceded += score2
        club2.goals_conceded += score1

        if score1 > score2:
            club1.wins += 1
            club1.points += 3
        elif score1 < score2:
            club2.wins += 1
            club2.points += 3
        else:
            club1.draws += 1
            club2.draws += 1
            club1.points += 1
            club2.points += 1

    print("Data pertandingan berhasil disimpan.")

def view_klasemen():
    print("Tampilan Klasemen:")
    print("{:<5} {:<15} {:<3} {:<3} {:<3} {:<3} {:<3} {:<5}".format("No", "Klub", "Ma", "Me", "S", "GM", "GK", "Point"))

    for i, club in enumerate(sorted(clubs, key=lambda x: x.points, reverse=True), 1):
        print("{:<5} {:<15} {:<3} {:<3} {:<3} {:<3} {:<3} {:<5}".format(
            i, club.name, club.matches_played, club.wins, club.draws + club.losses, club.goals_scored, club.goals_conceded, club.points))

# Objek clubs
clubs = []

# Menu Utama
while True:
    print("\nMenu:")
    print("1. Input Data Klub")
    print("2. Input Skor Pertandingan")
    print("3. Tampilan Klasemen")
    print("0. Keluar")

    choice = input("Pilih menu (0-3): ")

    if choice == '1':
        input_data()
    elif choice == '2':
        input_score()
    elif choice == '3':
        view_klasemen()
    elif choice == '0':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
