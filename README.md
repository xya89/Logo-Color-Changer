# 🎨 PNG Color Replacer Streamlit App

[🔗 Try it Live on Streamlit](https://logo-color-changer-tdfg.streamlit.app/)

This web app allows you to replace a specific color in a `.png` image with a new color, using hex codes. It’s built with **Python** and **Streamlit** to provide a quick, interactive UI.

---

## ✨ Features

- 📂 Upload a `.png` file  
- 🎯 Select a color in the image to replace (with a color picker)  
- 🎨 Select a replacement color (with a second color picker)  
- 👁️ Preview the updated image instantly  
- 💾 Download the modified image directly  

---

## 🖥️ Technologies Used

- [Python](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [Pillow (PIL)](https://python-pillow.org/)  

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/png-color-replacer.git
cd png-color-replacer
```

### 2. Install Dependencies
```bash
pip install streamlit pillow
```

### 3. Run the Streamlit app
```bash
streamlit run app.py
```
## 📌 Notes
-Only exact color matches (including the alpha channel) will be replaced.
-The match is based on RGBA values, so even slight differences in transparency or shade won’t be detected unless matched precisely.

## 📁 File Structure
```bash
png-color-replacer/
├── app.py         # Main Streamlit app
└── README.md      # This file
```

## 📄 License
This project is licensed under the MIT License — feel free to use, modify, and share!
