import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import load_model
import os
import streamlit as st
import cv2
from matplotlib import pyplot as plt
from PIL import Image
from io import BytesIO

st.header("Happy or Sad")

#predict = 0
#img = cv2.imread('manel.jpg')

#image =st.text_input('Enter Image name','.jpg')
#resize = tf.image.resize(image,(256,256))
#plt.imshow(resize.numpy().astype(int))



image_file = st.text_input('Enter Image name (with extension, e.g., image.jpg)', '')
if image_file:
    try:
       
        
        # Display the uploaded image
        col1, col2 = st.columns(2)

        with col1:
            image = Image.open(image_file)
            image_np = np.array(image)
            # Resize image to 256x256
              # Convert image to RGB if it has an alpha channel (4 channels)
            if image.mode == 'RGBA':
                image = image.convert('RGB')
            image_np = np.array(image) 
                 
            resize = cv2.resize(image_np, (256, 256))
        
                   
            # Normalize the image for prediction
            resized_image = resize / 255.0
            resized_image = np.expand_dims(resized_image, axis=0)
            predict = 0
            for i in range(6) :
                new_model = load_model(os.path.join('models',f'happysadmodel{i}.h5'))
                predict=+  new_model.predict(np.expand_dims(resize/255,0))
            prediction =predict[0][0]/6
            
            if predict[0][0] >0.5:
                st.write('predicted class is Sad')
            else :
                st.write('predicted class is Happy')
        

            # Display the uploaded image
            st.image(image, caption="Uploaded Image")

        with col2:
                # Display the predicted class with accuracy

            st.write('Prediction Confidence: **{:.2f}%**'.format(abs(predict[0][0]-0.5) * 200))
            if predict[0][0] <= 0.5:

          
                # Option 2: Display a happy GIF
                happy_gif_path = 'Mask.gif'  # Replace with the path to your happy GIF
                if os.path.exists(happy_gif_path):
                    st.image(happy_gif_path, caption="Enjoy this GIF!", use_column_width=True)
              
            else :
                sad_image_path = 'sademogie.gif'  # Replace with the path to your happy image
                if os.path.exists(sad_image_path):
                    st.image(sad_image_path, caption="Enjoy this GIF!", use_column_width=True)
              
    except FileNotFoundError:
        st.error("The image file was not found. Please enter a valid image path.")
    except Exception as e:
        st.error(f"An error occurred: {e}")