def setup():
    size(350, 350)
    textSize(100)
    background(0)
def draw():
    print(mouseX, mouseY)
    #text("P", width/3, height/3+30)
    text("P", 110, 190)  # Specify a z-axis value
    text("F", 210, 190)  # Specify a z-axis value
    fill(155)
    if keyPressed:
        fill(155)
        if key == 'p' or key == 'P':
            fill(255, 0, 0)
            text("P", 110, 190)
            fill(255)
    if keyPressed:
        fill(155)
        if key == 'f' or key == 'F':
            fill(100, 0, 0)
            text("F", 210, 190)
            fill(155)    
    if (mouseX>=118 and mouseX<=163 and mouseY>=116 and mouseY<=190):
        text("F", 210, 190)
        fill(0, 100, 0)
    if (mouseX>=218 and mouseX<=255 and mouseY>=116 and mouseY<=190):
        text("P", 110, 190)
        fill(0, 100, 0)

    s = createShape()
    s.beginShape()
    s.fill(32, 65, 255)
    s.noStroke()
    s.vertex(0, 0)
    s.vertex(0, 0)
    s.vertex(50, 50)
    s.vertex(50, 0)
    s.endShape(CLOSE)
    shape(s,68, 190)
    
    s = createShape()
    s.beginShape()
    s.fill(32, 65, 255)
    s.noStroke()
    s.vertex(0, 0)
    s.vertex(0, 0)
    s.vertex(50, 50)
    s.vertex(0, 50)
    s.endShape(CLOSE)
    shape(s,260, 65)
