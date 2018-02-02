from copy import deepcopy
import numpy as np

def manhattan_blur(n, k, distance, p=0.1, img=None):
    """ manhattan_blur(n, k, distance, p=0.1, img=None) -> numpy.ndarray
    
        Function to produce Manhattan Distance Blur Transformation of
        y-length distance on an image (represented as numpy array with
        binary values [0, 1]). Pixels are represented by cells of the array.
        
        Parameters
        ==========
        n (int): number of rows
        k (int): number of columns
        distance (int): Manhattan distance in number of pixels
        p (float): Pixel probability of beginning with 1
        img (numpy.ndarray): optional - 2D array to begin with"""
    
    if img is None:
        # create randomized img with specified p (probability)
        img = np.random.choice([0,1], size=(n,k), p=[1-p,p])
        if img.sum() == 0:
            # ensure there is at least one pixel filled in
            img[np.random.randint(0,n), np.random.randint(0,k)] = 1
    else:
        n = img.shape[0]
        k = img.shape[1]
    # holds activated pixel coordinates
    existing_ones = []
    # holds pixel coordinates to be updated
    new_ones = []
    # initialize existing_ones by searching for 1's
    for x, row in enumerate(img):
        if row.sum() > 0:
            for y, coord in enumerate(row):
                if img[x,y] > 0:
                    existing_ones.append([x,y])
    
    # update the img 'distance' times unless d>n or d>k
    for _ in range(min(distance, n, k)):
        # update row coordinates with 1's
        update_ns = np.array(existing_ones).transpose()[0]
        # update column coordinates with 1's
        update_ks = np.array(existing_ones).transpose()[1]
        # index img for these coordinate pairs and update the pixel values
        img[update_ns, update_ks] = 1
        # add existing_ones' immediately surrounding pixels to new_ones
        for coord in existing_ones:
            if coord[0]-1 >= 0:
                new_ones.append([coord[0]-1, coord[1]])
            if coord[0]+1 < n:
                new_ones.append([coord[0]+1, coord[1]])
            if coord[1]-1 >= 0:
                new_ones.append([coord[0], coord[1]-1])
            if coord[1]+1 < k:
                new_ones.append([coord[0], coord[1]+1])
        # update the pixel values using coordinates in new_ones
        update_ns = np.array(new_ones).transpose()[0]
        update_ks = np.array(new_ones).transpose()[1]
        img[update_ns, update_ks] = 1
        # assign new_ones to existing_ones
        existing_ones = deepcopy(new_ones)
        new_ones = []
    return img


## Tests

def test1():
    print("Test 1:")
    testin  = np.array([[0, 0, 0, 1, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]])
    testout = np.array([[0, 1, 1, 1, 1],[0, 0, 1, 1, 1],[0, 0, 0, 1, 0]])
    assert np.array_equal(manhattan_blur(1,1,2,img=testin), testout)
    print("pass\n")

def test2():
    print("Test 2:")
    testin = np.array([[0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 0],
                       [0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0]])

    testout =np.array([[0, 0, 1, 1, 1],
                       [0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 0],
                       [0, 1, 1, 1, 1],
                       [1, 1, 1, 1, 0],
                       [0, 1, 0, 0, 0]])
    assert np.array_equal(manhattan_blur(1,1,1,img=testin), testout)
    print("pass\n")

def test3():
    print("Test 3:")
    testin = np.array([[1, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0]])

    testout =np.array([[1, 1, 1, 1, 0],
                       [1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 0],
                       [1, 1, 1, 0, 0],
                       [0, 1, 0, 0, 0]])
    assert np.array_equal(manhattan_blur(1,1,3,img=testin), testout)
    print("pass\n")


if __name__ == '__main__':
    test1()
    test2()
    test3()