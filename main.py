from hash_utils import calculate_hash, compare_hash

def main():
    print("=== HASH CHECKER TOOL ===")
    print("1 - Dosya Hash Hesapla")
    print("2 - Hash Karşılaştır")

    choice = input("\nSeçim yap (1/2): ")

    if choice == "1":
        path = input("Dosya yolu: ")
        algo = input("Algoritma (md5/sha1/sha256): ").lower()

        result = calculate_hash(path, algo)
        if result:
            print(f"\n[{algo.upper()}] Hash: {result}")
        else:
            print("Dosya bulunamadı!")

    elif choice == "2":
        path = input("Dosya yolu: ")
        algo = input("Algoritma (md5/sha1/sha256): ").lower()
        expected = input("Karşılaştırılacak hash: ")

        file_hash = calculate_hash(path, algo)

        if not file_hash:
            print("Dosya bulunamadı!")
            return

        if compare_hash(file_hash, expected):
            print("\n✔ HASH UYUŞUYOR (Dosya değişmemiş)")
        else:
            print("\n✖ HASH UYUŞMUYOR (Dosya değiştirilmiş olabilir)")

    else:
        print("Geçersiz seçim!")

if __name__ == "__main__":
    main()
