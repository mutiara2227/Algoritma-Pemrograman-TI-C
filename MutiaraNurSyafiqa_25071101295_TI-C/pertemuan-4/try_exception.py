#Menangkap Beberapa Error Sekaligus
except (ValueError, ZeroDivisionError): 

#Menangkap Semua Error
except:
    #atau
except Exception: #Exception adalah superclass dari semua exception di Python.

#Mengambil Pesan Error Asli
except ValueError as err:


try:
    #kode
except:
    #handler
else:
    #dijalankan jika tidak ada error


try:
    #kode utama
except:
    #tangkap error
else:
    #jika tidak ada error
finally:
    #selalu dijalankan


if x < 0:
    raise ValueError("Tidak boleh negatif")