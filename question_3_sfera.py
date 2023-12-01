pi = 3.142

def kira_sfera(jejari):
    isipadu_sfera = 4/3 * pi * jejari ** 3
    return isipadu_sfera

def main():
    a = float(input("Masukkan jejari: "))
    isipadu_sfera = kira_sfera(a)
    print(f"Isipadu sfera = {isipadu_sfera:.2f}")

if __name__ == "__main__":
    main()