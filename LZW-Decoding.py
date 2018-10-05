import LZWcoding
import struct
import itertools
import numpy as np
class LZWD:
    def __init__(self):
        self.dic_size = 256
        self.dic = {}
        self.codigos = []

    def make_idic(self):
        self.dic = dict((i,chr(i).encode('utf-8')) for i in range(self.dic_size))

    def make_ndic(self, path, dic_tam):
        self.make_idic()
        del path[0]
        aux = chr(path.pop(0)).encode("utf-8")
        self.codigos.append(aux)
        for key in path:
            if(self.dic_size == dic_tam):
                print("tamanho maximo ultrapassado")
                return
            else:
                if key in self.dic:
                    aux_c = self.dic[key]
                elif key == self.dic_size:
                    aux_c = b''.join([aux,chr(aux[0]).encode("utf-8")])
                    
                else:
                    print("Deu errado o valor ", key)
                self.codigos.append(aux_c)
            
            self.dic[self.dic_size] = b''.join([aux,chr(aux_c[0]).encode("utf-8")])
            self.dic_size = self.dic_size + 1
            aux = aux_c

    def return_dics(self):

        return self.dic_size

    def return_dic(self):

        return self.dic 
    
    def return_codify(self):

        return self.codigos

    
path = []
vetor = []
with open(LZWcoding.outFile + ".LZW", "rb") as file:
    content = file.read()
    byte = struct.unpack(LZWcoding.aux_codigos+'i', content)
    path.append(byte)
x = []
for item in path:
    x.extend(item)
 
teste = LZWD()
dic_tam = x[0]
teste.make_ndic(x, dic_tam)
for item in teste.return_codify():
    vetor.append(item)

aux2_codigos = str(len(vetor))

with open('out'+LZWcoding.outFile + LZWcoding.extension, 'wb') as out:
    byte = b''.join(bytearray(i) for i in vetor)
    out.write(byte)
