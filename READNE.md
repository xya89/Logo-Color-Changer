🎨 PNG Color Replacer (Streamlit App)
This web app allows you to replace a specific color in a .png image with a new color, using hex codes. It’s built with Python and Streamlit for a quick, interactive UI.

Features
Upload a .png file

Select a color in the image to replace (using a color picker)

Select the replacement color (using another color picker)

Preview the updated image

Download the modified image directly

🖥️ Technologies
Python 

Streamlit 

Pillow (PIL) 

How to Run Locally
Clone this repo:

git clone https://github.com/your-username/png-color-replacer.git
cd png-color-replacer
Install dependencies:


pip install streamlit pillow
Run the app:


streamlit run app.py

Notes
Only exact color matches will be replaced (including alpha).

The color match is case-sensitive to RGBA values. Slight variations won’t be picked up unless manually matched.

File Structure

app.py         # Main Streamlit app
README.md      # This file

License
MIT License — feel free to use, modify, and share.

