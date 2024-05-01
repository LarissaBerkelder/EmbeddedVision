import matplotlib.pyplot as plt


def plot_img_hist_cdf(image, hist, cdf):
    fig, axes = plt.subplots(1, 3, figsize=(7, 3), layout="constrained")

    # Plot the image
    axes[0].set(title="Image")
    axes[0].imshow(image)

    # Plot the histogram of the image
    axes[1].set(title="Histogram")
    axes[1].plot(hist[0], color='r')
    axes[1].plot(hist[1], color='g')
    axes[1].plot(hist[2], color='b')

    # Plot the CDF of the image
    axes[2].set(title="CDF")
    axes[2].plot(cdf[0], color='r')
    axes[2].plot(cdf[1], color='g')
    axes[2].plot(cdf[2], color='b')

    plt.show()


def plot_before_after_hist_cdf(hist_before, hist_after, cdf_before, cdf_after):
    fig, axes = plt.subplots(2, 3, figsize=(9, 5), layout="constrained")
    axes[0, 0].set(title="Histogram & CDF red before")
    axes[0, 0].plot(hist_before[0], color='r')
    axes[0, 0].plot(cdf_before[0], color='#8B0000')
    axes[0, 0].set_ylim([0, 100000])

    axes[0, 1].set(title="Histogram & CDF green before")
    axes[0, 1].plot(hist_before[1], color='g')
    axes[0, 1].plot(cdf_before[1], color='#006400')
    axes[0, 1].set_ylim([0, 100000])

    axes[0, 2].set(title="Histogram & CDF blue before")
    axes[0, 2].plot(hist_before[2], color='b')
    axes[0, 2].plot(cdf_before[2], color='#00008B')
    axes[0, 2].set_ylim([0, 100000])

    axes[1, 0].set(title="Histogram & CDF red after")
    axes[1, 0].plot(hist_after[0], color='r')
    axes[1, 0].plot(cdf_after[0], color='#8B0000')
    axes[1, 0].set_ylim([0, 100000])

    axes[1, 1].set(title="Histogram & CDF green after")
    axes[1, 1].plot(hist_after[1], color='g')
    axes[1, 1].plot(cdf_after[1], color='#006400')
    axes[1, 1].set_ylim([0, 100000])

    axes[1, 2].set(title="Histogram & CDF blue after")
    axes[1, 2].plot(hist_after[2], color='b')
    axes[1, 2].plot(cdf_after[2], color='#00008B')
    axes[1, 2].set_ylim([0, 100000])
    plt.show()