class View:
    def show_items(items):
        if not items:
            print("\nKeranjang kosong.")
            return
        print("\nDaftar Barang:")
        print(f"{'Nama Barang':<20} {'Jumlah':<10} {'Harga Satuan':<15} {'Total':<10}")
        print("-" * 60)
        for item in items:
            total_price = item.quantity * item.price
            print(f"{item.name:<20} {item.quantity:<10} Rp{item.price:<15} Rp{total_price:<10}")
    
    def show_receipt(items, total_price, total_quantity):
        print("\n--- Struk Pembelian ---")
        print("--- Toko Belanja Hafiz ---\n")
        View.show_items(items)
        print("\nRingkasan:")
        print(f"Total Barang : {total_quantity}")
        print(f"Total Harga  : Rp{total_price}")
        print("\n--- Terima Kasih ---")
        print("--- Ditunggu kedatangannya kembali ---")

