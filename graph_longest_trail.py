import tkinter
        
class Graf:
    def __init__(self, meno_suboru):
        with open(meno_suboru, 'r') as subor:
            self.graf = {} #neorientovaný ohodnotený graf (Asociatívne pole množín susedností)
            for riadok in subor:
                hrana = riadok.split() #hrana je v subore zapísaná ako x1 y1 x2 y2
                x1, y1, x2, y2 = int(hrana[0]), int(hrana[1]), int(hrana[2]), int(hrana[3])
                
                if (x1, y1) in self.graf.keys():
                    self.graf[(x1, y1)].add((x2, y2))
                else:
                    self.graf[(x1, y1)] = set([(x2, y2)])

                if (x2, y2) in self.graf.keys():
                    self.graf[(x2, y2)].add((x1, y1))
                else:
                    self.graf[(x2, y2)] = set([(x1, y1)])
                    
    def susedia(self,v):
        return list(self.graf[v])
    
    def vzdialenost(self, v1, v2):#vzdialenosť dvoch vrcholov
        if self.je_hrana(v1, v2):
            return ((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2)**(0.5)
    
    def start(self,v):#Nájde najdlhšiu možnú trasu začínajúcu vo vrchole v
        if v not in self.vrcholy():
            return [],0
        
        def najdlhsia_cesta(vrch, boli, dlzka, cesta):
            if self.susedia(vrch):
                t = False
                for i in self.susedia(vrch):
                    if (i,vrch) not in boli:
                        t = True
                        break
                if t:
                    return max((najdlhsia_cesta(i, boli | {(vrch,i), (i, vrch)}, dlzka + self.vzdialenost(vrch,i), cesta + [i])
                                for i in self.susedia(vrch) if (i,vrch) not in boli), key = lambda x: x[0])
                else:
                    return dlzka, cesta
            else:
                return dlzka, cesta
        
        return najdlhsia_cesta(v, set(), 0, [v])
        
    def vrcholy(self):#vráti všetky vrcholy
        return set(self.graf.keys())

    def je_hrana(self, v1, v2): #je hrana medzi v1 a v2?
        if v1 in self.graf and v2 in self.graf[v1]:
            return True
        return False

#skúška:
if __name__ == '__main__':
    p = Graf('subor1.txt')
    print('vrcholy =', p.vrcholy())
    for v1 in (107, 421), (193, 352), (202, 75):
        for v2 in (238, 296), (193, 352), (221, 420):
            print(f'je_hrana({v1}, {v2}) =', p.je_hrana(v1, v2))
            print(f'susedia({v1}) =', p.susedia(v1))
    for v in (238, 296), (193, 352), (221, 420):
        print(f'start({v}) =', p.start(v))

#vykreslenie grafu:
canvas = tkinter.Canvas(width = 500, height = 500)
canvas.pack()

with open('subor1.txt', 'r') as subor:
    for riadok in subor:
        x1,y1,x2,y2 = riadok.split()
        x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
        canvas.create_text(x1, y1, text = str(x1)+','+ str(y1))
        canvas.create_text(x2, y2, text = str(x2)+','+ str(y2))
        canvas.create_line(x1,y1,x2,y2)
