from sklearn.externals import joblib 
import skimage
from skimage.io import imread
from skimage.transform import resize
import numpy as np

clf = joblib.load('file_1000_40x40.pkl')  
  
# Use the loaded model to make predictions 
# clf_from_joblib.predict(X_test) 


dimension=(40, 40)
images = []
flat_data = []


file = 'Test on Me!!/Parasitized/PARA (1).png'
# file = 'data/test/Uni/y.png'
img = skimage.io.imread(file)
# print(img)
img_resized = resize(img, dimension, anti_aliasing=True, mode='reflect')
flat_data.append(img_resized.flatten()) 
images.append(img_resized)
flat_data = np.array(flat_data)
print(flat_data)

result = clf.predict(flat_data)
# print(result)
if result[0] == 0:
    print("Infected")
else:
    print("Uninfected")



