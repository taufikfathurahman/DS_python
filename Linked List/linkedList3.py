# Node class
class Node:
    def __init__(self, rekamMedis, nama, poliTujuan, noRujuk, tanggal):
        self.rekamMedis = rekamMedis
        self.nama = nama
        self.poliTujuan = poliTujuan
        self.noRujuk = noRujuk
        self.tanggal = tanggal
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def antrian(self, rekamMedis, nama, poliTujuan, noRujuk, tanggal):
        new_node = Node(rekamMedis, nama, poliTujuan, noRujuk, tanggal)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def countQueue(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count

    def searchPasien(self, rekamMedis):
        temp = self.head
        while(temp and temp.rekamMedis != rekamMedis):
            temp = temp.next
        return temp

    def printQueue(self):
        temp = self.head
        while(temp is not None):
            print(temp.rekamMedis)
            print(temp.nama)
            print(temp.poliTujuan)
            print(temp.noRujuk)
            print(temp.tanggal)
            temp = temp.next

if __name__=='__main__':
    pasien = Queue()
    pasien.antrian(123, 'Taufik Fathurahman', 'Jantung', 321, '23-01-1998')
    pasien.printQueue()
    print(pasien.searchPasien(123))
