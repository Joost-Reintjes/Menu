#to be added: less jpeg background, exit button, version indicator with changelog, a credits and contact screen.


currentscreen = 'Startmenu'

def setup():
    fullScreen()
    
    global img_cursor
    img_cursor = loadImage('cursor.png')
    
    global img_bg
    img_bg = loadImage('Background78.jpeg')
    
    global font_kabel
    font_kabel = loadFont('LeelawadeeUI-Bold-48.vlw')
    
    global img_round
    img_round = loadImage('round.png')
    
    global img_bl
    img_bl = loadImage('Black.jpg')
    
def drawStartmenu():
    image(img_bg, 0, 0, width, height)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(67)
    text("Play", 960, 950)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(60)
    text("Settings", 1425, 950)
    
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
    


    



    
    
    
   
