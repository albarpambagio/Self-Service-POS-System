from trnsctprocess import Transaction
from tabulate import tabulate

print("Swalayan Kasir Toko Andi")
print("----------------------------")
print("Silahkan Masukkan Nomor Untuk Memilih Menu:")
print("1. Buat Transaksi Baru / Tambah barang untuk transaksi sebelumnya\n"
      "2. Edit Barang dalam Transaksi\n"
      "3. Hapus barang dalam transaksi\n"
      "4. Tampilkan Ringkasan Pesanan Saat Ini & Total Belanja\n"
      "5. Tampilkan Status Pesanan\n"
      "6. Reset Transaksi\n"
      "7. Selesaikan Pesanan\n"
      "8. Akhiri Program")

general_transactions = Transaction()  

try:
    while True:
        menu = int(input("Ketik Nomor Menu: "))
        if menu == 8:
            break
        elif menu == 1:
            product_name = input("Masukkan nama produk: ")
            product_quantity = int(input("Masukkan jumlah produk: "))
            product_price = int(input("Masukkan harga produk satuan: "))
            group = [product_name.lower(), product_quantity, product_price]
            general_transactions.add_item(group)
            print(general_transactions.check_order())
            
        elif menu == 2:
            print("Pilih menu edit:")
            print("1. Update Nama Barang")
            print("2. Update Jumlah Barang")
            print("3. Update Harga Barang")
            edit_menu = int(input("Ketik Nomor: "))
            
            if edit_menu == 1:
                product_name = input("Masukkan nama barang yang ingin diubah: ")
                updated_name = input("Masukkan nama barang baru: ")
                print(general_transactions.update_item_name(product_name, updated_name))

                
            elif edit_menu == 2:
                product_name = input("Masukkan nama barang yang ingin diubah: ")
                updated_qty = int(input("Masukkan jumlah barang baru: "))
                print(general_transactions.update_item_qty(product_name, updated_qty))
                
            elif edit_menu == 3:
                product_name = input("Masukkan nama barang yang ingin diubah: ")
                updated_price = int(input("Masukkan harga barang baru: "))
                print(general_transactions.update_item_price(product_name, updated_price))
                
            else:
                print("Menu edit tidak valid")
            
        elif menu == 3:
            delete_items_input = str(input("Masukkan nama barang yang ingin dihapus: "))
            delete_items = general_transactions.delete_item(delete_items_input)
            transaction_result = general_transactions.get_order_summary()
            total = general_transactions.total_price()
            print(f"{delete_items_input} berhasil dihapus.")
            print(tabulate(transaction_result, headers=["No", "Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]))
        
        
        elif menu == 4:
            transaction_result = general_transactions.get_order_summary()
            total = general_transactions.total_price()
            print(tabulate(transaction_result, headers=["No", "Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]))
            print("Total Belanja:", total)
            

        elif menu == 5:
            print(general_transactions.check_order())

        elif menu == 6:
            general_transactions.reset_transaction()
            print("transaksi direset")

        elif menu == 7:
            transaction_result = general_transactions.get_order_summary()
            total = general_transactions.total_price()
            print("Berikut Pesanan Anda")
            print(tabulate(transaction_result, headers=["No", "Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]))
            print("Total Belanja:", total)
            break
        else:
            print("Menu tidak valid. Silakan masukkan nomor menu kembali")
            
except Exception as e:
    print("Program Selesai dengan Kesalahan:", e)
