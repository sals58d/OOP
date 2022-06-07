class Customer:
    def __init__(self,name,address):
        self.name = name
        self.address = address

    def info(self):
        print("\nPesanan berhasil diproses dan akan dikirm ke %s" % (self.address))
        print("Terima kasih telah melakukan pembelian di toko kami %s  Semoga hari Anda menyenangkan\n"%(self.name))    