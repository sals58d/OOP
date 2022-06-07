from Ice import Ice
from Cake import Cake
from Customer import Customer
 
ice1 = Ice('Ice Choco Ball',     5000, 'Jely')
ice2 = Ice(' Ice Chocolate ',     4000, 'Cincau')
ice3 = Ice(' Ice Cream Puff',     6000, 'Almond')

ices = [ice1, ice2, ice3]

cake1 = Cake(' Rainbow ',      30000, 'Strawberry')
cake2 = Cake(' Blossom ',  20000, 'Cheese')
cake3 = Cake(' Choco Rain',    30000, 'Choco')

cakes = [cake1, cake2, cake3]

print('\n\n\n\n\n\n\n Ice Cream')
index = 0
for ice in ices:
    print(index,' ' + ice.info())
    index += 1


print('\n Cake')
index = 0
for cake in cakes:
    print(index,' ' + cake.info())
    index += 1

print('--------------------------------------------')

ice_order = int(input('\nMasukkan nomor item Ice cream: '))
selected_ice = ices[ice_order]

cake_order = int(input('Masukkan nomor item Cake: '))
selected_cake = cakes[cake_order]


count=int(input('\nBerapa banyak makanan yang ingin Anda beli?? (Diskon 10% untuk 3 atau lebih): '))

c = str(input('\nMasukkan Nama anda: '))
a = str(input('Masukkan Alamat anda: '))

result=selected_ice.total_price(count)+selected_cake.total_price(count)


print('\nTotalnya adalah RP.'+str(result))
c = Customer(c,a)
c.info()
