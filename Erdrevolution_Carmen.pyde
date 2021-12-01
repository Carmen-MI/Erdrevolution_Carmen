#Deklaration globaler Variablen
weltraumbreite = 900
weltraumhohe = 600
weltraummitte_x = weltraumbreite/2
weltraummitte_y = weltraumhohe/2
erddurchmesser = 60
erdwinkel = 0
umlaufbahndurchmesser = 400
rechteckbreite = 100
rechteckhohe = 40
yPosition_Rechteck = 400
xPos = 950
yPos = 100
going = False



def setup():
    
    # Grösse des Bildschirms und Grundfarbe festlegen
    size(1200, 600)
    background(0,0,0)
    
def draw():
    global erdwinkel
    
    # Hintergrundbild laden mit geteiltem Bildschirm und Sonne der Grösse 100x100
    weltraum = loadImage("weltraum.jpg")
    image(weltraum, 0, 0, weltraumbreite, weltraumhohe)
    sonne = loadImage("sonne.png")
    image(sonne, weltraummitte_x - 50, weltraummitte_y - 50)
    
    # Umlaufbahn der Erde um die Sonne
    Erdrevolution()
    
    # Einfügen des Stoppbuttons
    Stoppbutton()
    
    # Erde der Grösse 60x60 umkreist die Sonne
    # if going:
    translate(weltraumbreite/2, weltraumhohe/2)
    rotate(erdwinkel)
    erde = loadImage("erde.png")
    image(erde, -erddurchmesser/2, -(umlaufbahndurchmesser/2)-(erddurchmesser/2), erddurchmesser, erddurchmesser)
    if going == True and mouseX >= xPos and mouseX <= xPos + rechteckbreite and mouseY >=yPosition_Rechteck and mouseY <= yPosition_Rechteck + rechteckhohe:
        erdwinkel = erdwinkel - PI/90
        resetMatrix()
        
        # Einblenden der Texte der vier Jahreszeiten entsprechend den Winkeln der Umlaufbahn
        if erdwinkel < (-45*PI/180) and erdwinkel > (-135*PI/180):
            TextJahreszeiten()
            text("Sommer", xPos, yPos)
        else:
            fill(0,0,0)
            noStroke()
            rect(900, 0, 300, 300)
            
        if erdwinkel < (-135*PI/180) and erdwinkel > (-225*PI/180):
            TextJahreszeiten()
            text("Herbst", xPos, yPos)
            
        if erdwinkel < (-225*PI/180) and erdwinkel > (-315*PI/180):
            TextJahreszeiten()
            text("Winter", xPos, yPos)
            
        if erdwinkel < (-315*PI/180) and erdwinkel > (-405*PI/180):
            TextJahreszeiten()
            text("Fruehling", xPos, yPos)
            
        # Wenn Erdrotation eine Umdrehung erreicht hat, Variable auf 0 zurücksetzen
        if erdwinkel < -TWO_PI:
            erdwinkel = 0
            
# Idde von Boolscher Algebra: https://www.youtube.com/watch?v=_NJqfZUQ3i4&ab_channel=TheCodingTrain        
def mouseClicked():
    global going
    if going == True:
         going = False
    else:
        going = True
        
# Defintion der Erdumlaufbahn         
def Erdrevolution():
    noFill()
    stroke(255, 255, 255)
    circle(weltraummitte_x, weltraummitte_y, umlaufbahndurchmesser)
    
# Definition des Stoppbuttons
def Stoppbutton():
    fill(255)
    rect(xPos, yPosition_Rechteck, rechteckbreite, rechteckhohe, 7)
    textSize(20)
    fill(0, 0, 0)
    text ("Start", xPos + 23, 425)
    
# Definieren der Texte der Jahreszeiten
def TextJahreszeiten():
    textSize(20) #Textgrösse
    fill(255,255,255) #Text ausfüllen
