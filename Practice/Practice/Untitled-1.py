from Crypto.Cipher import DES3
from Crypto.Hash import SHA256 as SHA
from os import path
KSIZE = 1024 

class MyDES():
    def __init__(self, key, iv):
        hash = SHA.new()
        hash.update(key.encode('utf-8'))
        hash_key = hash.digest()
        self.key = hash_key[:24]
        
        hash.update(iv.encode('utf-8'))
        hash_iv = hash.digest()
        
        self.iv = hash_iv[:8]
        
    
    def makeEncInfo(self, filename):
        fillersize = 0
        filesize = path.getsize(filename)
        if filesize % 8 != 0:
            fillersize = 8 - filesize % 8
        filler = '0' * fillersize
        header = '%d' % (fillersize)
        gap = 8 - len(header)
        header += '#' * gap
        
        return header , filler
    
    
    def enc(self, filename):
        encfilename = filename + '.enc'
        header, filler = self.makeEncInfo(filename)
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)
        
        fileopen = open(filename, 'rb')
        fileopen2 = open(encfilename, 'wb+')
        
        enc = header.encode('utf-8')
        content = fileopen.read(KSIZE)
        content = enc + content
        
        while content:
            if len(content) < KSIZE:
                content += filler.encode('utf-8')
            enc = des3.encrypt(content)
            fileopen2.write(enc)
            content = fileopen.read(KSIZE)
        
        fileopen.close()
        fileopen2.close()
        
    
    def dec(self, encfilename):
        filename = encfilename + '.dec'
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)
        
        fileopen = open(filename, 'wb+')
        fileopen2 = open(filename, 'rb')
        
        content = fileopen2.read(8)
        dec = des3.decrypt(content)
        header = dec.decode('utf-8')
        fillersize = int(header.split('#') [0])
        
        content = fileopen2.read(KSIZE)
        
        while content:
            dec = des3.decrypt(content)
            if len(dec) < KSIZE:
                if fillersize != 0:
                    dec = dec[:-fillersize]
            fileopen.write(dec)
            content = fileopen2.read(KSIZE)
        fileopen.close()
        fileopen2.close()
        
def main():
    key = 'sungchan'
    iv = '1234'
    filename = '/Users/pcy/Desktop/works/python/Practice/text.rtf'
    encfilename = filename + '.enc'
    
    mydes = MyDES(key, iv)
    mydes.enc(filename)
    mydes.dec(encfilename)
    
if __name__ == '__main__':
    main()