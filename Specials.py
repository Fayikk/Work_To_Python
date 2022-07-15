class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration

        print("Moive objesi oluşturuldu")

    def __str__(self):
        return f"{self.title} by {self.director}"    

m=Movie("Interstaller","IDK","150")
print(m.duration+"filmin süresidir "+m.director+"filmin yönetmeni "+m.title+"filmin adi ")





