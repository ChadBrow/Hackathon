# this program is used to modify the .pngs I am using so their color schemes are correct (because right now they have a lot of filler-colors)
# kinda proud of this little program

from PIL import Image
file = "resources/bottom_menu_background"
p = Image.open(file + ".png")

# I see a red door and I want to paint it black
# no colors anymore I want them to turn black

# https://onmessage.nd.edu/athletics-branding/colors/
# I love the fact that this website exists
# gotta keep the brand CLEAN!
# NOTRE DAME official NAVY: r12 g35 b64 : (12, 35, 64)



pairs = { # gotta get the rgb values from that fucking thing - why did I not put the rgb values in earlier!!
    (255, 0, 128)   : (30, 30, 70, 0), # its dark (transparency doesnt work)
    (0, 0, 0)       : (50, 50, 60), # dark, slight tint of blue
    (127, 127, 127) : (90, 90, 110), # slightly lighter, also slight tint of blue
    (237, 28, 36)   : (237, 28, 36),#(12, 35, 64), # ND navy
    (195, 195, 195) : (140, 140, 180), # much lighter, also slight tint of blue
    (34, 177, 76)   : (12, 35, 64),
    (0, 162, 232)   : (100, 100, 130)
}
unique = []
width, height = p.size
for i in range(width):
    for j in range(height):
        c = p.getpixel((i, j))
        print(c)
        if (not unique.__contains__(c)):
            unique.append(c)
        p.putpixel((i, j), pairs[c])
        
print(unique)
p.show()
p.save(file + "2.png")
"""
r, g, b
Values:
(34, 177, 76), 
(0, 162, 232)






"""