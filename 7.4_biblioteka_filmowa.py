import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
import random
from datetime import datetime 
now = datetime.now()

database = []

class Film:
    def __init__(self, tytul, rok_wydania, gatunek, liczba_odtworzen):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen
        database.append(self)
 
    def __str__(self):
        return f'{self.tytul} {self.rok_wydania}'

    def __repr__(self):
        return f'{self.tytul}'
    
    def play(self, views = 0):
        '''metoda zwiekszajaca liczbe odtworzen o 1'''
        if views > 0:
            self.liczba_odtworzen += views
        else:
            self.liczba_odtworzen += 1
  
    def __gt__(self,other):
        return self.liczba_odtworzen > other.liczba_odtworzen
    def __ge__(self,other):
        return self.liczba_odtworzen >= other.liczba_odtworzen
    def __lt__(self,other):
        return self.liczba_odtworzen < other.liczba_odtworzen
    def __le__(self,other):
        return self.liczba_odtworzen > other.liczba_odtworzen
    def __eq__(self,other):
        return self.liczba_odtworzen == other.liczba_odtworzen
    
class Serial(Film):
    def __init__(self, numer_sezonu, numer_odcinka, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.numer_sezonu = numer_sezonu
        self.numer_odcinka = numer_odcinka
    
    def __str__(self):
        return f'{self.tytul} S{self.numer_sezonu} E{self.numer_odcinka} {self.liczba_odtworzen}'
    
    def __repr__(self):
        return f'{self.tytul} S{self.numer_sezonu:02} E{self.numer_odcinka:02}'
    
def get_movies():
    ''' funkcja pobierajaca film z listy filmow i seriali; kazdy film jest serialem ale nie kazdy serial jest filmem'''
    filmy = []
    for i in database:
        if isinstance(i, Serial) == False:
            filmy.append(i)
    posortowane_filmy = sorted(filmy)
    return posortowane_filmy

def get_series():
    '''funkcja pobierajaca serial z listy filmow i seriali'''
    seriale = []
    for i in database:
        if isinstance(i,Serial):
            seriale.append(i)
    return seriale

def search(wyszukiwanie):
    ''''funkcja wyszukujaca film lub serial po tytule '''
    wyszukiwanie_l = wyszukiwanie.lower()
    results = [film for film in database if wyszukiwanie_l in film.tytul.lower()]
    print(results)

def generate_views():
    '''randomowo generuje ilosc wyswietlen filmu lub serialu(od 1 do 100)'''
    '''czy to powinno byc dekoratorem??'''
    random_choice = random.choice(database)
    views = random.randint(1,100)
    random_choice.liczba_odtworzen += views

def generate_views_10_times():
    '''wywoluje funkcje generate_views 10 razy'''
    for gen in range(10):
        generate_views()

def top_titles(content_type, ile):
    '''wyswietla najpopularniejsze tytuly'''
    movies = get_movies()
    series = get_series()
    if content_type == 'f':
        by_odtworzenia = sorted(movies,key=lambda popular: popular.liczba_odtworzen, reverse=True)
        for i in range(ile):
            print(f'- {by_odtworzenia[i]}')
    elif content_type =='s':
        by_odtworzenia = sorted(series,key=lambda popular: popular.liczba_odtworzen, reverse=True)
        for i in range(ile):
            print(f'- {by_odtworzenia[i]}')
    elif content_type == 'a':
        by_odtworzenia = sorted(database,key=lambda popular: popular.liczba_odtworzen, reverse=True)
        for i in range(ile):
            print(f'- {by_odtworzenia[i]}')



if __name__ == '__main__':
    print('Biblioteka filmów')
    pulp = Film('Pulp Fiction', 1994,'Gangsterski', 0)
    gral = Film('Monty Python i Święty Graal', 1975,'Komedia',0)
    borat = Film('Borat: Podpatrzone w Ameryce, aby Kazachstan rósł w siłę, a ludzie żyli dostatniej', 2006,'komedia',0)
    true = Serial(1,1,'True Detective', 1999, 'Dramat', 0)
    true2 = Serial(1,2,'True Detective', 1999, 'Dramat', 0)
    family = Serial(1,2,'Family Guy',1999,'Komedia',0)
    family = Serial(2,2,'Family Guy',1999,'Komedia',0)
    family = Serial(1,5,'Family Guy',1999,'Komedia',0)
    family = Serial(1,4,'Family Guy',1999,'Komedia',0)

    

    generate_views()
    generate_views_10_times()

    print(f'Najpopularniejsze filmy i seriale dnia {now.strftime('%d/%m/%Y')}')
    top_titles('a',3)
