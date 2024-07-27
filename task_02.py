from PIL import Image 

input_image = Image.open("1000101577.jpg") 

pixel_map = input_image.load() 

width, height = input_image.size 

for i in range(width//2): 
	for j in range(height): 
		
		r, g, b, p = input_image.getpixel((i, j)) 
		
		grayscale = (0.299*r + 0.587*g + 0.114*b) 
 
		pixel_map[i, j] = (int(grayscale), int(grayscale), int(grayscale)) 

input_image.save("grayscale", format="jpg") 

input_image.show()
