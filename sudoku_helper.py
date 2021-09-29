# -*- coding: utf-8 -*-
from temp import load_puzzle
import streamlit as st
import tempfile
st.title('Welcome to Xudoku')
st.write("--------")
SIDEBAR_OPTION_UPLOAD_IMAGE="Upload an Image"
SIDEBAR_OPTION_CONTACT_ME="Contact me"
SIDEBAR_OPTION_PROJECT_INFO="about this project"
SIDEBAR_OPTION_CREDITS="credits"
SIDEBAR_OPTIONS=[SIDEBAR_OPTION_UPLOAD_IMAGE,SIDEBAR_OPTION_CONTACT_ME,SIDEBAR_OPTION_PROJECT_INFO,SIDEBAR_OPTION_CREDITS]
def load_and_preprocess_img(path):
   img = Image.open(img_path).convert('RGB')
   img = ImageOps.exif_transpose(img)
   new_img = cv2.resize(np.array(img), (330,330),
                        interpolation=cv2.INTER_LINEAR)
   X_batch = np.expand_dims(new_img.astype('float'), axis=0)
   return X_batch
def main():
  st.sidebar.write('Xudoku')
  st.sidebar.write('------')
  st.sidebar.warning('\ Please use proper lighting while taking the picture, also try to write preferably with a dark colored pen')
  st.sidebar.write("------")
  st.sidebar.title("Explore the following")
  app_mode=st.sidebar.selectbox("please select from the follwing",SIDEBAR_OPTIONS)
  if app_mode==SIDEBAR_OPTION_UPLOAD_IMAGE:
    st.sidebar.info('PRIVACY POLICY: Uploaded images are never saved or stored. They are held entirely within memory for prediction \
            and discarded after the final results are displayed. ')
    f = st.sidebar.file_uploader("Please Select to Upload an Image", type=['png', 'jpg', 'jpeg', 'tiff', 'gif'])
    if f is not None:
       tfile=tempfile.NamedTemporaryFile(delete=True)
       tfile.write(f.read())
       st.sidebar.write('finding your solution')
       left_column, right_column = st.beta_columns(2)
       xb = load_and_preprocess_img(tfile)
       try:
         ans=load_puzzle(xb)
         if(ans is None):
            right_column.write('no feasable solution')
         if(ans is not None):
             for i in range(9):
                right_column.write('-------')
                for j in range(9):
                  right_column.write('{ans[i,j]}')
                right_column.write('-------')
       except:
          right_column.write('try to improve the image quality')
       left_column.image(xb, caption = "Selected Input")
main()
