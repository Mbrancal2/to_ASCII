import PIL.Image, PIL. ImageOps


def change_dim(img):
    W, H = img.size
    ratio = H/W
    new_W = 100
    new_H = int((new_W * ratio) * 0.45) 
    new_img = img.resize((new_W, new_H))
    #convert image to gray scale with values between 0-225
    #new_img = PIL.ImageOps.grayscale(new_img)
    #pixels = new_img.load()
    return new_W, new_H, new_img

def convert_to_gray(img):
    new_img = PIL.ImageOps.grayscale(img)
    pixels = new_img.load()
    return pixels

def convert_to_ASCII(new_H, new_W, img):
    #array of ASCII chars
    ASCII_List = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

    result = ""
    for pix_H in range(0, new_H):
        for pix_W in range(0, new_W):
            result += ASCII_List[img[pix_W,pix_H]//25]
        result += "\n"
    
    return result

def main():
    img_path = input("enter a file path \n")
    
    try:
        img = PIL.Image.open(img_path)

    except:
        print("could not find image at: ", img_path) 
    
    #convert image to new dim and convert image to grayscale.
    img = PIL.Image.open(img_path)
    new_W, new_H, new_img = change_dim(img)
    pixels = convert_to_gray(new_img)

    #converts image to ASCII characters.
    result = convert_to_ASCII(new_H, new_W, pixels)

    #writes converted image to a file called ascii_image.txt.
    with open("ascii_image.txt", "w") as f:
        f.write(result)

main()






