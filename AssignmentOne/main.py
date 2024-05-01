import cv2 as cv
import numpy as np
import plot


def calculate_cdf(hist):
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    return cdf_normalized


def calculate_hist(image):
    return [
        cv.calcHist([image[:, :, 0]], [0], None, [256], [0, 256]),
        cv.calcHist([image[:, :, 1]], [0], None, [256], [0, 256]),
        cv.calcHist([image[:, :, 2]], [0], None, [256], [0, 256]),
    ]


def calculate_cdf_channels(hist):
    return [
        calculate_cdf(hist[0]),
        calculate_cdf(hist[1]),
        calculate_cdf(hist[2])
    ]


def main():
    # Load the image with cv and convert to RGB color space
    original_image = cv.imread("parrot_dark.PNG")
    original_image = cv.cvtColor(original_image, cv.COLOR_BGR2RGB)

    # Calculate the histogram of the color channels of the image and the CDF
    hist_image = calculate_hist(original_image)
    cdf_image = calculate_cdf_channels(hist_image)

    # Plot the image, histograms and cdfs of the image
    plot.plot_img_hist_cdf(original_image, hist_image, cdf_image)

    # Transform the image to the HSV color space
    hsv_image = cv.cvtColor(original_image, cv.COLOR_RGB2HSV)

    # Equalize the histogram of the Value
    hsv_image[:, :, 2] = cv.equalizeHist(hsv_image[:, :, 2])

    # Return to the RGB color space
    equalized_image = cv.cvtColor(hsv_image, cv.COLOR_HSV2RGB)

    # Calculate the histogram of the color channels of the image and the CDF
    hist_image_equalized = calculate_hist(equalized_image)
    cdf_image_equalized = calculate_cdf_channels(hist_image_equalized)

    # Plot the image, histograms and cdfs of the image
    plot.plot_img_hist_cdf(equalized_image, hist_image_equalized, cdf_image_equalized)

    # Plot the image, histograms and cdfs of the image
    plot.plot_before_after_hist_cdf(hist_image, hist_image_equalized, cdf_image, cdf_image_equalized)


if __name__ == '__main__':
    main()
