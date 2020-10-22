#first class
class Cemilan(object):
    """
    makanan enak buat ngemil
    """
    def __init__(self, nama=None, bahan=None):
        self.nama = nama
        self.bahan = bahan

    def namaCemilan(self):
        return self.nama
    
    def bahanCemilan(self):
        return self.bahan

#second class
class Rasa(Cemilan):

    def __init__(self, rasa=None, tekstur=None):
        self.rasa = rasa
        self.tekstur = tekstur

    def citaRasa (self):
        return self.rasa
    
    def teksturNya (self):
        return self.tekstur

cemilan1 = Cemilan("Odading", "terigu")
rasa1 = Rasa("anjiimm banget", "gurih bangeed")
print ("Nama Cemilan : %s"% cemilan1.namaCemilan())
print ("Bahan Cemilan : %s"% cemilan1.bahanCemilan())
print("Rasanya : %s"% rasa1.citaRasa())
print("Teksturnya :%s"% rasa1.teksturNya())
rasa1.nama = "JEding"
print(rasa1.namaCemilan())







