from PIL import Image
 
# Opens a image in RGB mode
im = Image.open(r"art\player_animations\Hans\hans_stuned.png")
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
 
# Setting the points for cropped image
left = 50
top = 0
right = 115
bottom = height/6
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
 
# Save image
im.show()