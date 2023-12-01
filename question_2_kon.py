pi = 3.142

def kira_kon(jejari, tinggi):
    isipadu_kon = 1/3 * pi * jejari ** 2 * tinggi
    return isipadu_kon

def main():
    a = float(input("Masukkan jejari: "))
    b = float(input("Masukkan tinggi: "))
    isipadu_kon = kira_kon(a, b)
    print(f"Isipadu kon = {isipadu_kon:.2f}")

if __name__ == "__main__":
    main()