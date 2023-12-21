from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

class CheckHeaderFront:
    
    # fazer algoritmo que descriptografa o que foi mandado no header
    # e compara se é realmente o valor esperado.

    def __init__(self, header: str) -> None:
        self.headerScript = header

    # def descryptHeader(self):
    #     cipher = AES.new("olhadinhaFrnt3212#4@5", AES.MODE_CBC)
    #     ciphertext = base64.b64decode(self.headerScript)
    #     decryped = cipher.decryped(ciphertext)
    #     unpadded = unpad(decryped, AES.block_size)
    #     return unpadded.decode('utf-8')
        

    def validate(self) -> bool:

        print("header from controller", self.headerScript)
