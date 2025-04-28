import matplotlib.pyplot as plt

def flood_fill(img, x, y):
    # pixely popředí (kde je povoleno rozšiřování) mají hodnotu 1
    # pixely pozadí (zábrany) hodnotu 0 a již přebarvené pixely hodnotu 2

    if x <0 or x >= img.shape[0] or y >= img.shape[0] or y<0:
        return img
    #vykreslení obrazku
    if img[x,y] == 2 or img[x,y]==0:
        return img #proti zacykleni
    img[x,y] = 2
    plt.imshow(img, cmap='gray')
    plt.show(block=False)
    plt.pause(0.05) #pauza pro zachycení překleslení lidským okem
    plt.clf()

    img = flood_fill(img,x+1,y) #posunuti doprava
    img = flood_fill(img,x, y+1)
    img = flood_fill(img, x - 1, y)
    img = flood_fill(img, x, y - 1)
    return img



def main():
    #img = plt.imread("files/img0.png")[:, :, 0]
    # img = plt.imread("files/img1.png")[:, :, 0]
    img = plt.imread("files/img2.png")[:, :, 0]

    img = flood_fill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()


if __name__ == "__main__":
    main()
