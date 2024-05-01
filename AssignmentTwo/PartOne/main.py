import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import image_morphology as morph


def show_image(im, title):
    plt.figure(figsize=(7, 3))
    plt.imshow(im, cmap='gray')
    plt.title(title)
    plt.axis("off")
    plt.show()


def get_ring_image(im):
    fig, axes = plt.subplots(1, 5, figsize=(15, 7), layout="constrained")
    axes[0].set(title="Original")
    axes[0].imshow(im, cmap='gray')

    # Remove the ring from the image
    no_ring = morph.closing(im, 7, 1)
    axes[1].set(title="Image without ring")
    axes[1].imshow(no_ring, cmap='gray')

    # Invert the image and add it to the original image to only get the ring
    invert_no_ring = cv2.bitwise_not(no_ring)
    axes[2].set(title="Inverted image without ring")
    axes[2].imshow(invert_no_ring, cmap='gray')

    invert_add_original = cv2.add(im, invert_no_ring)
    axes[3].set(title="Add inverted to original")
    axes[3].imshow(invert_add_original, cmap='gray')

    # Use closing operation to remove the 'noise'
    only_ring = morph.closing(invert_add_original, 2, 1)
    axes[4].set(title="Only the ring")
    axes[4].imshow(only_ring, cmap='gray')

    plt.show()

    return only_ring


def remove_small_circles(im):
    radius = 10
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * radius + 1, 2 * radius + 1))
    closing = cv2.morphologyEx(im, cv2.MORPH_CLOSE, kernel)
    show_image(closing, "No small circles")
    return closing


def main():
    image = np.array(Image.open("circles.gif").convert("L"))
    show_image(image, "Original image")
    only_ring = get_ring_image(image)
    closing = remove_small_circles(image)
    final = closing + only_ring
    final =     cv2.bitwise_not(final)
    show_image(final, "Final image")


if __name__ == '__main__':
    main()
