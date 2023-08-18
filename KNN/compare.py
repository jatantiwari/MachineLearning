from PIL import Image

def image_compare(image1_path, image2_path):
    try:
        # Open the images
        image1 = Image.open(image1_path)
        image2 = Image.open(image2_path)

        # Compare image sizes
        if image1.size != image2.size:
            return "Images are of different sizes."

        # Compare pixel by pixel
        pixel_diff = 0
        width, height = image1.size
        for x in range(width):
            for y in range(height):
                pixel1 = image1.getpixel((x, y))
                pixel2 = image2.getpixel((x, y))

                if pixel1 != pixel2:
                    pixel_diff += 1

        if pixel_diff == 0:
            return "Images are identical."
        else:
            pp = pixel_diff/(width*height)
            return pp

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Paths to the images you want to compare
image_path1 = "KNN/f1.jpeg"
image_path2 = "KNN/f2.jpeg"

result = image_compare(image_path1, image_path2)
print(result)
