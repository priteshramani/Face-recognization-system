import streamlit as st
import face_recognition
import cv2
import numpy as np
from PIL import Image
import os

st.set_page_config("Face Recognition app")
st.title("🎥 Face Recognition System")

# Load known face images and encodings
known_face_encodings = []
known_face_names = []

face_dir = "known_faces"
for filename in os.listdir(face_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(face_dir, filename)
        image = face_recognition.load_image_file(img_path)
        encoding = face_recognition.face_encodings(image)

        if encoding:  # Avoid images without detectable faces
            known_face_encodings.append(encoding[0])
            name = os.path.splitext(filename)[0]
            known_face_names.append(name)

# Option to upload new identity images
st.subheader("Add New Identity")
uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Save the uploaded image to the known_faces directory
    img = Image.open(uploaded_file)
    img_name = uploaded_file.name
    img_path = os.path.join(face_dir, img_name)
    img.save(img_path)

    # Load the new image and encode it
    new_image = face_recognition.load_image_file(img_path)
    new_encoding = face_recognition.face_encodings(new_image)

    if new_encoding:  # If encoding is successful
        known_face_encodings.append(new_encoding[0])
        known_face_names.append(os.path.splitext(img_name)[0])
        st.success(f"Identity '{os.path.splitext(img_name)[0]}' added successfully!")

# Webcam input for face recognition
picture = st.camera_input("Take a picture")
if picture is not None:
    image = np.array(Image.open(picture))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# If image exists
if 'image' in locals():
    # Detect faces and encodings
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    # Draw rectangles and labels
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Use the known face with the smallest distance if any match is True
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

        # Draw rectangle and label on image
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(image, (left, bottom - 30), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, name, (left + 5, bottom - 5), font, 0.6, (0, 0, 0), 2)

        # Layout: image left, card right
        col1, col2 = st.columns(2)

        with col1:
            st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Detected Faces", use_container_width=True)

        with col2:
            st.markdown(f"""
                <div style="border:2px solid #444;padding:15px;border-radius:10px;background-color:#f9f9f9">
                    <h4 style="color:#333;text-align:center;">🪪 Identity Card</h4>
                    <hr>
                    <p style="font-size:16px;"><b>Name:</b> <span style="color:#1f77b4;">{name}</span></p>
                    <p style="font-size:16px;"><b>Status:</b> <span style="color:{'#008000' if name != 'Unknown' else '#ff0000'};">{'Verified' if name != 'Unknown' else 'Unknown'}</span></p>
                </div>
            """, unsafe_allow_html=True)

    if len(face_locations) == 0:
        st.warning("⚠️ No face found in the image.")
