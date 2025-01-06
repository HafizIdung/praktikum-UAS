from cart import ShoppingCart
from view import View

def get_input(prompt, type_=str, condition=lambda x: True, error_message="Input tidak valid!"):
    while True:
        try:
            value = type_(input(prompt))
            if condition(value):
                return value
            else:
                print(error_message)
        except ValueError:
            print(error_message)

def show_item_options():
    items = [
        ("Beras / kg", 12000),
        ("Minyak Goreng / L", 15000),
        ("Gula Pasir / kg", 14500),
        ("Tepung Terigu / kg", 10000),
        ("Telur Ayam / kg", 23000)
    ]
    print("\nPilihan Barang:")
    for i, (name, price) in enumerate(items, start=1):
        print(f"{i}. {name} - Rp{price}")
    return items

def main():
    cart = ShoppingCart()
    while True:
        print("\n1. Tambah Barang\n2. Tampilkan Keranjang\n3. Cetak Struk\n4. Keluar")
        choice = get_input("Pilih opsi: ", int, lambda x: 1 <= x <= 4, "Pilih angka antara 1 dan 4.")
        
        if choice == 1:
            items = show_item_options()
            item_choice = get_input("Pilih barang (1-5): ", int, lambda x: 1 <= x <= 5, "Pilih angka antara 1 dan 5.")
            name, price = items[item_choice - 1]
            quantity = get_input("Jumlah Barang: ", int, lambda x: x > 0, "Jumlah harus lebih dari 0.")
            cart.add_item(name, price, quantity)
            
        elif choice == 2:
            View.show_items(cart.items)

        elif choice == 3:
            total_price = cart.calculate_total()
            total_quantity = cart.calculate_total_quantity()
            View.show_receipt(cart.items, total_price, total_quantity)

        elif choice == 4:
            print("Terima kasih telah berbelanja!")
            break

if __name__ == "__main__":
    main()
