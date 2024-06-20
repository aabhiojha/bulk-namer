from PIL import Image, ImageDraw, ImageFont
import os

backgroundImagePath = "MyInvitation.jpeg"
backgroundImage = Image.open(backgroundImagePath)
draw = ImageDraw.Draw(backgroundImage)

listOfNames = [
"Katie Watkins",
"Angelica Ingram",
"Natalie Zuniga",
"Ty Bradford",
"Cassius Kirk",
]

fontPath = "LivingHell.ttf"
fontSize = 200
font = ImageFont.truetype(fontPath, fontSize)

y = 1950
lineHeight= fontSize + 10
textColor = "black"

outputDir = "output"
if not os.path.exists(outputDir):
    os.makedirs(outputDir)

for name in listOfNames:
    currentImage = backgroundImage.copy()
    draw = ImageDraw.Draw(currentImage)
    
    textWidth = draw.textlength(name, font)
    imageWidth,imageHeight = currentImage.size
    draw.text((imageWidth/2 - textWidth/2, y),name,font=font,fill=textColor)
    
    outputFileName = os.path.join(outputDir, f"output_{name}.jpg")
    currentImage.save(outputFileName)
    
    print(f"Generated {outputFileName}")

print("All outputs are generated!")

