# load dogs vs cats dataset, reshape and save to a new file
from os import listdir
from numpy import asarray
from numpy import save
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array


def resize(path):
	# define location of dataset
	folder = path
	photos, labels = list(), list()
	# enumerate files in the directory
	for file in listdir(folder):
		# determine class
		output = 0.0
		if file.startswith('cat'):
			output = 1.0
		# load image
		photo = load_img(folder + file, target_size=(200, 200))
		# convert to numpy array
		photo = img_to_array(photo)
		# store
		photos.append(photo)
		labels.append(output)
	# convert to a numpy arrays
	photos = asarray(photos)
	labels = asarray(labels)
	print(photos.shape, labels.shape)
	# save the reshaped photos
	save('dogs_vs_cats_photos.npy', photos)
	save('dogs_vs_cats_labels.npy', labels)
	return photos, labels

resize('/Users/mariamorales/Desktop/CNN/cats_and_dogs/')

#/Users/mariamorales/Desktop/CNN/cats_and_dogs/
'''
import os
from PIL import Image
folder_path = '/Users/mariamorales/Desktop/CNN/cats_and_dogs'
extensions = []
for file in os.listdir(folder_path):
    #sub_folder_path = os.path.join(folder_path, fldr)
    #for filee in os.listdir(sub_folder_path):
    file_path = os.path.join(folder_path, file)
    print('** Path: {}  **'.format(file_path), end="\r", flush=True)
    im = Image.open(file_path)
    rgb_im = im.convert('RGB')
    if file.split('.')[1] not in extensions:
        extensions.append(file.split('.')[1])

		(90, 200, 200, 3) (90,)

        '''