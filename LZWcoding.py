import pathlib
import pickle
import struct
import binascii
from struct import pack

class LZW:
    def __init__(self):
        self.dic_size = 256
        self.dic = {}
        self.codigos = []

    def make_idic(self):
        self.dic = dict((chr(i).encode('utf-8'), i) for i in range(self.dic_size))

    def make_ndic(self, path):
        self.make_idic()
        aux = bytes('', encoding = "utf-8")
        for char in path:
            aux_c = b''.join([aux,char])
            if(self.dic_size >= (pow(2,215))):
                print("tamanho maximo ultrapassado")
                return
            else:
                if aux_c in self.dic:
                    aux = aux_c
                
                else:
                    self.codigos.append(self.dic[aux])
                    self.dic[aux_c] = self.dic_size
                    self.dic_size = self.dic_size + 1
                    aux = char

        if aux:
            self.codigos.append(self.dic[aux])
        

    def return_dics(self):

        return self.dic_size

    def return_dic(self):

        return self.dic 
    
    def return_codify(self):

        return self.codigos

path = []
filename = input('Digite o nome do arquivo: ')
outFile,extension = filename.split('.')

for byte in pathlib.Path(filename).read_bytes():
    byte = chr(byte).encode('utf8')
    path.append(byte)

vetor = []
teste = LZW()
teste.make_ndic(path)
vetor.append(teste.dic_size)
for item in teste.return_codify():
    vetor.append(item)

aux_codigos = str(len(vetor))

with open(outFile + ".LZW", "wb") as file:
    file.write(struct.pack(aux_codigos+'i', *vetor))

