#question class
#quizz class


#question classını kalıtım ile alacaz 
#child class ile soruların ekrandaki yansımasını göreceğiz
#el ile totalde 5 soru yazalım ve bu soruları quiz ile konsolda gösterelim
#puanlama sistemi her soru 2 puan olacak şekilde olsun 1 yanlılta
#kişi elenecektir



from ast import Break


class Sınav:
    def __init__(self,yarisma="Piton bilgi yarışmasına Hoş Geldiniz"):
        self.yarisma=yarisma

    # def Karisik(self):
    #     
    #     if cevap=='B':
    #         
    #         continue
    #     else:
    #         print("Malesef! yanlış cevap.\nteselli ödülü=1000")
    def Karisik(self):
        print("calisti")
        sayac=5
        i=0
        ödül=0
        while i<=sayac:

            

            if i==1:

                print("1.Soru:")
                print("Apple'ın baş mühendisi kimdir?\nA)steve jobs\nB)steve wozniak\nC)Alejandro\nD)Tuncel kurtiz")
                cevap=input("Cevabınızı giriniz:")
                if cevap=='B':
                    print("Tebrikler! doğru cevap\nÖdül=5000")
                    
                    
                else:
                    print("Malesef! yanlış cevap girdiniz.")
                    break
                        

            ödül=ödül+5000    
            if i==2:
                print("2.Soru")
                print("Türkiyede Finansbank'ın kurucusu kimdir?\nA)Hüsnü Özyeğin\nB)Vehbi Koç\nC)Cem Özyeğin\nD)Ali Ağaoğlu")
                cevap=input("Cevabınızı giriniz:")
                if cevap=='A':
                    print("Tebrikler! doğru cevap\nÖdül=10000")
                    
                else:
                    print("Malesef! yanlış cevap girdiniz.")
                    break
            ödül=ödül+5000
            if i==3:
                print("3.Soru")
                print("Simyacı kitabının yazarı kimdir?\nA)Jack london\nB)Agatha christe\nC)Robert Lafore\nD)Paul Coelho")
                cevap=input("Cevabınızı giriniz:")
                if cevap=='D':
                    print("Tebrikler! doğru cevap\nÖdül=15000")
                    
                else:
                    print("Malesef! yanlış cevap girdiniz.")       
                    break      
            ödül=ödül+5000

            if i==4:
                print("4.Soru")
                print("IMF merkezi nerededir?\nA)London\nB)Stockholm\nC)Washington DC\nD)Newyork")
                cevap=input("Cevabınızı giriniz:")
                if cevap=='C':
                    print("Tebrikler! doğru cevap\nÖdül=20000")
                    
                else:
                    print("Malesef! yanlış cevap girdiniz.") 
                    break


            ödül=ödül+5000

            if i==5:
                print("5.Soru")
                print("Mstemetik dalında nobel ödülü alan şizofreni hastası kimdir?\nA)J.Von neuman\nB)John nash\nC)Alan fawyer\nD)Newton")
                cevap=input("Cevabınızı giriniz:")
                if cevap=='C':
                    print("Tebrikler! doğru cevap\nÖdül=25000")
                             
                else:
                    print("Malesef! yanlış cevap girdiniz.")
                    break         
            ödül=ödül+5000  
            i+=1
        print("Yarışmamız bitmiştir kazanılan para ödülü: {}".format(ödül))    
class Sorular(Sınav):

    def __init__(self,yarisma,):
        super().__init__(yarisma)

sınav1=Sınav()
sınav1.Karisik()


# soru=Sorular(self)

# soru.Karisik()


