#to be added: version indicator with changelog, a credits and contact screen.


currentscreen = 'Startmenu'

def setup():
    fullScreen()
    
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
    image(img_bg, 0, 0)
    
    image(img_log, 388, 100, 1784, 558.5)
    
    image(img_round, 817, 840, 406, 162.4)
    
    image(img_round, 1337, 840, 406, 162.4)
    
    image(img_round, 817, 1100, 406, 162.4)
    
    image(img_round, 1337, 1100, 406, 162.4)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(75)
    text("Play", 945, 940)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(67)
    text("Settings", 1415, 937)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(55)
    text("Developers", 880, 1200)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(65)
    text("Contact", 1423, 1200)
    
def drawExitButton():
    image(img_btn_exit, 50, 50, 92, 101)
    
       
def drawPlaceholder():
    image(img_bl, 0, 0, width, height)
    
    fill(255)
    textSize(60)
    text('Placeholder', 1100, 700)



def mousePressed():
    
    global currentscreen
    
    if currentscreen == 'Startmenu': 
        

        
        #play
        if mouseX > 865 and mouseX < 1165 and mouseY > 860 and mouseY < 960:
            currentscreen = 'Placeholder'
        
        #settings
        if mouseX > 1385 and mouseX < 1685 and mouseY > 860 and mouseY < 960:
            currentscreen = 'Placeholder'
            
        #credits
        if mouseX > 865 and mouseX < 1165 and mouseY > 1120 and mouseY < 1220:
            currentscreen = 'Placeholder'
            
        #contact
        if mouseX > 1385 and mouseX < 1685 and mouseY > 1120 and mouseY < 1220:
            currentscreen = 'Placeholder'
        
        #exit immmediately
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 135: 
            exit()
    
        
def draw():
    
    if currentscreen == 'Startmenu':
        drawStartmenu()
        drawExitButton()
    
        
    if currentscreen =='Placeholder':
        drawPlaceholder()
        

        






    
    
    
   
