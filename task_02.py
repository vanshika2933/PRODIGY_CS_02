from PIL import Image 

input_image = "1000101577.jpg" 

input_image.save("input", format="jpg") 

pixel_map = input_image.load() 

width, height = input_image.size 
z = 100
for i in range(width): 
	for j in range(height): 
		
		if((i >= z and i <= width-z) and (j >= z and j <= height-z)): 
			pixel_map[i, j] = (255, 165, 0) 
		else:  
			pixel_map[i, j] = (255, 160, 122) 

for i in range(width):  
	pixel_map[i, i] = (0, 0, 255) 
	pixel_map[i, width-i-1] = (0, 0, 255) 

input_image.save("output", format="jpg") 

input_image.show("output", format="jpg")
