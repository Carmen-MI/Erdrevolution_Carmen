# Deklaration globaler Variablen
weltraumbreite = 900
weltraumhohe = 600
weltraummitte_x = weltraumbreite/2
weltraummitte_y = weltraumhohe/2+40
durchmesser_sonne = 140
erddurchmesser = 60
erdwinkel = 0
umlaufbahndurchmesser = 400
text_mitte = weltraumbreite + ((1200-weltraumbreite)/2)
rechteckbreite = 200
rechteckhohe = 40
yPosition_Rechteck = 500
xPos = 950
yPos_Jahreszeit = 80
yPos_Bild = yPos_Jahreszeit + 40
going = False
movingMode = False
pointerPos = 1+xPos+1
pointerVal = 1.0

def setup():
    # Grösse des Bildschirms und Grundfarbe festlegen
    size(1200, 600)
    background(0,0,0)
    
def draw():
    global erdwinkel
    background(0, 0, 0) # Zeigt nur aktuelle Erdkugel
    
    # Hintergrundbild laden mit geteiltem Bildschirm und Sonne der Grösse 100x100
    weltraum = loadImage("weltraum.jpg")
    image(weltraum, 0, 0, weltraumbreite, weltraumhohe)
    sonne = loadImage("sonne.png")
    image(sonne, weltraummitte_x - durchmesser_sonne/2, weltraummitte_y - durchmesser_sonne/2, durchmesser_sonne, durchmesser_sonne)

    # Überschrift einfügen
    Titel()
    
    # Umlaufbahn der Erde um die Sonne
    Erdrevolution()
    
    # Stopp-, Startbutton einfügen
    Stoppbutton()

    # Schieberegler von Dozent Simon Hefti einfügen 
    draw_ruler(xPos, yPosition_Rechteck-80 , 200)
    textAlign(CENTER)
    fill(255)
    text("Geschwindigkeit Erde: " + str(pointerVal), text_mitte, yPosition_Rechteck-120)

    # Erde der Grösse 60x60 umkreist die Sonne
    translate(weltraummitte_x, weltraummitte_y) # Koordinatenmittelpunkt wird von oben links zu neuen Koordinaten verschoben
    rotate(erdwinkel)
    erde = loadImage("erde.png") # alles nach Funktion "rotate" wird rotiert
    image(erde, -erddurchmesser/2, -(umlaufbahndurchmesser/2)-(erddurchmesser/2), erddurchmesser, erddurchmesser)
            
    if going == True:
        erdwinkel = erdwinkel - (pointerVal*PI/1080) # Änderung des Erdwinkels
        Jahreszeiten()
    else:
        Jahreszeiten()            
            
# Idde von Boolscher Algebra: https://www.youtube.com/watch?v=_NJqfZUQ3i4&ab_channel=TheCodingTrain        
def mousePressed():
    global going
    if mouseX >= xPos and mouseX <= xPos + rechteckbreite and mouseY >=yPosition_Rechteck and mouseY <= yPosition_Rechteck + rechteckhohe:
        if going == True:
            going = False
        else:
            going = True
        
# Defintion der Überschrift
def Titel():
    fill(255)
    rect(150, 15, 600, 50, 7)
    textSize(30) #Textgrösse
    fill(0) #Text ausfüllen
    textAlign(CENTER)
    text("Erdrevolution auf der Nordhalbkugel", 450, 50)

# Defintion der Erdumlaufbahn         
def Erdrevolution():
    noFill()
    stroke(255, 255, 255)
    circle(weltraummitte_x, weltraummitte_y, umlaufbahndurchmesser)
    
# Definition des Stoppbuttons
def Stoppbutton():
    fill(255)
    rect(xPos, yPosition_Rechteck, rechteckbreite, rechteckhohe, 7)
    textAlign(CENTER)
    textSize(15)
    text ("Hier druecken um Erde zu bewegen", text_mitte, yPosition_Rechteck-18)
    textSize(20)
    fill(0, 0, 0)
    text ("Start / Stopp", text_mitte, yPosition_Rechteck+26)
        
# Definition der Texte der Jahreszeiten
def TextJahreszeiten():
    textSize(30) #Textgrösse
    fill(255,255,255) #Text ausfüllen
    textAlign(CENTER)
 
# Einblenden der Texte & Bilder der vier Jahreszeiten entsprechend den Winkeln der Umlaufbahn
def Jahreszeiten():
    global erdwinkel
    resetMatrix()
    if erdwinkel < (-45*PI/180) and erdwinkel > (-135*PI/180):
        TextJahreszeiten()
        text("Sommer", text_mitte, yPos_Jahreszeit)
        sommer = loadImage("sommer.png")
        image(sommer, xPos, yPos_Bild)
        
    if erdwinkel < (-135*PI/180) and erdwinkel > (-225*PI/180):
        TextJahreszeiten()
        text("Herbst", text_mitte, yPos_Jahreszeit)
        herbst = loadImage("herbst.png")
        image(herbst, xPos, yPos_Bild)
        
    if erdwinkel < (-225*PI/180) and erdwinkel > (-315*PI/180):
        TextJahreszeiten()
        text("Winter", text_mitte, yPos_Jahreszeit)
        winter = loadImage("winter.png")
        image(winter, xPos, yPos_Bild)
        
    if erdwinkel < (-315*PI/180) and erdwinkel > (-360*PI/180) or erdwinkel < (-0*PI/180) and erdwinkel > (-45*PI/180):
        TextJahreszeiten()
        text("Fruehling", text_mitte, yPos_Jahreszeit)
        fruehling = loadImage("fruehling.png")
        image(fruehling, xPos, yPos_Bild)
        
    # Wenn Erdrotation eine Umdrehung erreicht hat, Variable erdwinkel auf 0 zurücksetzen
    if erdwinkel < -TWO_PI:
        erdwinkel = 0

# Definition Schieberegler von Dozent Simon Hefti
def draw_ruler(objX, objY, objLength):
    global movingMode
    global pointerPos
    global pointerVal
    
    # Schieber einstellen
    pointerRadius = 24
    if pointerPos == 0:
        pointerPos = objX
    
    # Linie zeichnen
    fill(85)
    strokeWeight(6)
    line(objX, objY, objX + objLength, objY)
    fill(185)
    strokeWeight(2)
    
    # Überprüfen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if mouseX > pointerPos - pointerRadius and mouseX < pointerPos + pointerRadius and mouseY > objY - pointerRadius and mouseY < objY + pointerRadius and mousePressed == True:
        movingMode = True
    
    # Wenn keine Maustaste gedrückt ist --> Bewegungsmodus deaktivieren
    if mousePressed == False:
        movingMode = False
        cursor(ARROW)
    
    # Bei aktiviertem Bewegungsmodus
    if movingMode == True:
        cursor(HAND)
        
        # Schieber der Line entlang bewegen
        if mouseX > objX and mouseX < objX + objLength:
            pointerPos = mouseX
        
        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if mouseX < objX:
                pointerPos = objX
            if mouseX > objX:
                pointerPos = objX + objLength

    # Schieber zeichnen            
    circle(pointerPos, objY, pointerRadius)
    
    # Eingestellter Wert anhand der Schieberposition ermitteln
    pointerVal = int(100 / float(objLength) * (pointerPos - objX))
    #print(pointerVal)


    
