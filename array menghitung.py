array = []
total = 0
n = int(input("masukan jumlah element array:"))
for x in range(n):
    nilai = float(input("masukan nilai ke- {:".format(x=1)))
    array.append(nilai)
    print("\nhasil total adalah: {}".format(sum(array)))
    print("hasil rata rata adalah: {".format(sum(array)/n))