#Deklaration globaler Variablen
weltraumbreite = 900
weltraumhohe = 600
weltraummitte_x = weltraumbreite/2
weltraummitte_y = weltraumhohe/2


def setup():
    size(1200, 600) #Grösse des Bildschirms
    background(0,0,0) #Hintergrundfarbe
    weltraum = loadImage("weltraum.jpg") #Hintergrund der Animation mit geteiltem Bidschirm - Animation und Textfeld
    image(weltraum, 0, 0, weltraumbreite, weltraumhohe)
    sonne = loadImage("sonne.png")
    image(sonne, weltraummitte_x - 50, weltraummitte_y - 50)
    
def draw():
    
    Erdrevolution() #Umlaufbahn Erde um die Sonne
    
    
    xPos = 950 #Position des Textes
    yPos = 100
    textSize(20) #Textgrösse
    fill(255,255,255) #Text ausfüllen
    text("Fruehling", xPos, yPos)
    
 
    

def Erdrevolution():
    noFill()
    stroke(255, 255, 255)
    circle(weltraummitte_x, weltraummitte_y, 400)
