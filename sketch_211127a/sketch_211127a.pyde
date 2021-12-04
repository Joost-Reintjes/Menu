#to be added: changelog, a credits and contact screen.
# Rules?
#perhaps a bit of music
#maybe make buttons slightly interactive, turn text white when hovering or something after clicking(timer)

currentscreen = 'Startmenu'

def setup():
    size(1920, 1080)
    
    global img_bg
    img_bg = loadImage('background.png')
    
    global img_btn_exit
    img_btn_exit = loadImage('exit.png')
    
    global img_log
    img_log = loadImage('logo.png')
    
    global font_kabel
    font_kabel = loadFont('LeelawadeeUI-Bold-48.vlw')
    
    global img_round
    img_round = loadImage('round.png')
    
    global img_bl
    img_bl = loadImage('Black.jpg')
    
def drawStartmenu():
    
    image(img_bg, 0, 0, width, height)
    
    image(img_log, 291, 75, 1338, 418.875)
    
    image(img_round, 612.75, 630, 304.5, 121.8)
    
    image(img_round, 1002.75, 630, 304.5, 121.8)
    
    image(img_round, 612.75, 825, 304.5, 121.8)
    
    image(img_round, 1002.75, 825, 304.5, 121.8)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(61)
    text("Play", 702, 705)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(53)
    text("Settings", 1054, 704)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(55)
    text("Credits", 672, 901)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(55)
    text("Contact", 1052, 900)
    
    fill(255)
    textSize(20)
    text('Version 0.0', 10, 1070)

    if mouseX > 10 and mouseX < 115 and mouseY > 1055 and mouseY < 1072:
            fill(255) 
            rect(10, 1072, 105, 3)

    

def drawExitButton():
    image(img_btn_exit, 37.5, 37.5, 69, 75.75)
    
       
def drawPlaceholder():
    image(img_bl, 0, 0, width, height)
    
    fill(255)
    textSize(60)
    text('Placeholder', 825, 525)
    
def mousePressed():
    
    global currentscreen
    
    if currentscreen == 'Startmenu': 
        
        #play
        if mouseX > 648.75 and mouseX < 873.75 and mouseY > 645 and mouseY < 720:
            currentscreen = 'Placeholder'
        
        #settings
        if mouseX > 1038.75 and mouseX < 1263.75 and mouseY > 645 and mouseY < 720:
            currentscreen = 'Placeholder'
            
        #credits
        if mouseX > 648.75 and mouseX < 873.75 and mouseY > 840 and mouseY < 915:
            currentscreen = 'Placeholder'
            
        #contact
        if mouseX > 1038.75 and mouseX < 1263.75 and mouseY > 840 and mouseY < 915:
            currentscreen = 'Placeholder'
        
        #exit immmediately
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 135: 
            exit()
            
        #version indicator
        if mouseX > 10 and mouseX < 115 and mouseY > 1055 and mouseY < 1072:
            currentscreen ='Placeholder'
    
        
def draw():
    
    if currentscreen == 'Startmenu':
        drawStartmenu()
        drawExitButton()
    
        
    if currentscreen =='Placeholder':
        drawPlaceholder()
        

        






    
    
    
   
