import streamlit as st
from PIL import Image
import io

# Convert hex to RGBA
def hex_to_rgba(hex_color, alpha=255):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) + (alpha,)

st.title("🎨 PNG Color Replacer")

# Upload image
uploaded_file = st.file_uploader("Upload a PNG image", type=["png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGBA")
    st.image(image, caption="Original Image", use_column_width=True)

    # Color selectors
    old_hex = st.color_picker("Color to Replace", "#ff0000")
    new_hex = st.color_picker("Replacement Color", "#00ff00")

    if st.button("Replace Color"):
        old_color = hex_to_rgba(old_hex)
        new_color = hex_to_rgba(new_hex)

        data = image.getdata()
        new_data = [new_color if pixel == old_color else pixel for pixel in data]

        new_img = image.copy()
        new_img.putdata(new_data)

        st.image(new_img, caption="Updated Image", use_column_width=True)

        # Download button
        buf = io.BytesIO()
        new_img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Image",
            data=byte_im,
            file_name="updated_image.png",
            mime="image/png"
        )
