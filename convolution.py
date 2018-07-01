import numpy as np

def convo(image, kernel):

    # Flip the kernel
    kernel = np.flipud(np.fliplr(kernel))

    # finding the kernel size that will be used to create padding of image
    kernel_size = kernel.shape[1]

    # create padding size by kernel - 1 for fill the kernel to image
    # and prevent exceeded array once we get martix data
    padding = kernel_size - 1

    # get edge of image that is not a padding we were filled
    edge_image = padding - 1

    # create output array size like orignal image
    # every index were filled with zero
    # output use to get value after we multiply data
    # once process is completed, we will get a new image
    output = np.zeros_like(image)

    # create the new array use to get pixel value for multiply with kernel
    # add padding to every 4 sides of image
    image_with_padding = np.zeros((image.shape[0] + padding, image.shape[1] + padding))

    # this use to copy image data (pixel color as number in array)
    # into the empty array that we've just created
    # to prevent error we must find edge that is not a padding we were filled
    # you can use other method to copy image as you wanted
    # copying image for prevent overriding the original image that will drity
    image_with_padding[edge_image:-1, edge_image:-1] = image

    # started to multiply kernel to image
    for x in range(image.shape[1]):     # Loop over every pixel of the image
        for y in range(image.shape[0]):

            # the idea behind this line is to reduce the loop time
            # because we retrieve the pixel size equal the kernel size
            # instead of adding the 2 loop for kernel loop inside image loop
            # let see example below the result of each loop
            # [0,0,0
            #  0,0,0
            #  0,0,0]
            # once you use numpy we can multiple matrix directly and then get sum value
            # put back to the image position. very easy
            output[y,x]=(kernel*image_with_padding[y:y+kernel_size,x:x+kernel_size]).sum()
    return output

