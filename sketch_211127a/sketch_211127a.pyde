#to be added: less jpeg background, exit button, version indicator with changelog, a credits and contact screen.


currentscreen = 'Startmenu'

def setup():
    fullScreen()
    
    global img_bg
    img_bg = loadImage('background.png')
    
    global img_log
    img_log = loadImage('logo.png')
    
    global font_kabel
    font_kabel = loadFont('LeelawadeeUI-Bold-48.vlw')
    
    global img_round
    img_round = loadImage('round.png')
    
    global img_bl
    img_bl = loadImage('Black.jpg')
    
def drawStartmenu():
    image(img_bg, 0, 0)
    
    image(img_log, 400, 100, 1784, 558.5)
    
    image(img_round, 880, 840, 406, 162.4)
    
    image(img_round, 1400, 840, 406, 162.4)
    
    image(img_round, 1400, 1100, 406, 162.4)
    
    image(img_round, 880, 1100, 406, 162.4)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(75)
    text("Play", 995, 940)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(67)
    text("Settings", 1473, 939)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(60)
    text("Credits", 932, 1180)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(60)
    text("Contact", 1430, 1175)
    
       
def drawPlaceholder():
    image(img_bl, 0, 0, width, height)
    
    fill(255)
    textSize(60)
    text('Placeholder', 1100, 700)



def mousePressed():
    
    global currentscreen
    
    if currentscreen == 'Startmenu': 
        
        if mouseX > 1390 and mouseX < 1690 and mouseY > 870 and mouseY < 970:
            currentscreen = 'Placeholder'
        
        if mouseX > 1390 and mouseX < 1690 and mouseY > 1105 and mouseY < 1205:
            currentscreen = 'Placeholder'
        
        if mouseX > 880 and mouseX < 1180 and mouseY > 880 and mouseY < 980:
            currentscreen = 'Placeholder'
        
        if mouseX > 880 and mouseX < 1180 and mouseY >1105 and mouseY < 1205:
            currentscreen = 'Placeholder'

    
def draw():
    
    if currentscreen == 'Startmenu':
        drawStartmenu()
        
    if currentscreen =='Placeholder':
        drawPlaceholder()
    


    



    
    
    
   
