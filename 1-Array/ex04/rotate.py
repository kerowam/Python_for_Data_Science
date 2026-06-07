from load_image import ft_load
from numpy import array
import matplotlib.pyplot as plt


def crop_center(image):
    """Return a centered 400x400 crop using the first channel."""
    height, width = image.shape[0], image.shape[1]
    if height < 400 or width < 400:
        raise ValueError("Image is too small to crop a 400x400 region")

    y_start = (height - 400) // 2
    x_start = (width - 400) // 2
    y_end = y_start + 400
    x_end = x_start + 400
    return image[y_start:y_end, x_start:x_end, 0:1]


def display_zoom(zoomed):
    """Display the zoomed image with x and y axis scales."""
    plt.imshow(zoomed[:, :], cmap="gray")
    plt.xticks(range(0, zoomed.shape[1], 50))
    plt.yticks(range(0, zoomed.shape[0], 50))
    plt.show()


def rotate(image):
    """Rotate the image 90 degrees clockwise and return the new array."""
    image = image[:, :, 0]
    rows, cols = image.shape[0], image.shape[1]
    rotated = []

    for col in range(cols - 1, -1, -1):
        new_row = []
        for row in range(rows):
            new_row.append(image[row][col])
        rotated.append(list(new_row))

    return array(rotated)


def main():
    """Run the zoom demo and handle any errors without crashing."""
    try:
        path = "animal.jpeg"
        image = ft_load(str(path))
        if image is None:
            return

        zoomed = crop_center(image)
        print(f"The shape of image is: {zoomed.shape} or "
              f"({len(zoomed)}, {len(zoomed[0])})")
        print(zoomed)
        rotated = rotate(zoomed)
        print(f"New shape after Transpose: {rotated.shape}")
        print(rotated)
        display_zoom(rotated)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
