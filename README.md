# **Face Recognition System Documentation**

---

## **Table of Contents**
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Workflow](#workflow)
6. [File Structure](#file-structure)
7. [Technologies Used](#technologies-used)
8. [Performance Considerations](#performance-considerations)
9. [Future Enhancements](#future-enhancements)
10. [Troubleshooting](#troubleshooting)
11. [License](#license)

---

## **1. Introduction**  
This documentation provides an overview of the **Real-Time Face Recognition System** built using Python, Streamlit, and OpenCV. The application allows users to:  
- **Detect and recognize faces** from webcam input.  
- **Add new identities** by uploading images.  
- **Display verification status** (Verified/Unknown) alongside an identity card.  

---

## **2. Features**  
✅ **Webcam Face Detection** – Captures live video feed for face recognition.  
✅ **Identity Management** – Upload and store new faces in the `known_faces` directory.  
✅ **Face Comparison** – Matches detected faces with known identities.  
✅ **Identity Card Generation** – Displays the recognized name and verification status.  
✅ **Real-Time Processing** – Fast face detection using optimized Python libraries.  

---

## **3. Installation**  

### **Prerequisites**  
- Python 3.8+  
- `pip` package manager  
- Webcam access  

### **Setup Steps**  
1. **Clone the Repository**  
   ```sh
   git clone https://github.com/priteshramani/Face-recognization-system.git
   cd Face-recognization-system
   ```
2. **Create and Activate a Virtual Environment**  
   ```sh
   python -m venv venv
   ```
   - **Windows:**  
     ```sh
     venv\Scripts\activate
     ```
   - **Linux/macOS:**  
     ```sh
     source venv/bin/activate
     ```
3. **Install Dependencies**  
   ```sh
   pip install -r requirements.txt
   ```
4. **Create the `known_faces` Directory**  
   ```sh
   mkdir known_faces
   ```
   - Store known face images here (e.g., `john.jpg`, `emma.png`).  

---

## **4. Usage**  

### **Running the Application**  
```sh
streamlit run app.py
```
- Open the URL provided in your browser (typically `http://localhost:8501`).  

### **Adding New Identities**  
1. Click **"Upload an image"**.  
2. Select an image file (`.jpg`, `.png`).  
3. The system will automatically encode and store the face.  

### **Face Recognition via Webcam**  
1. Click **"Take a picture"** to capture a face.  
2. The system will:  
   - Detect faces in the image.  
   - Compare against known faces.  
   - Display the identity with verification status.  

---

## **5. Workflow**  
### **Face Recognition Process**  
1. **Image Capture** → Webcam or image upload.  
2. **Face Detection** → Uses `face_recognition.face_locations()`.  
3. **Encoding Extraction** → Converts faces into 128-dimensional vectors.  
4. **Face Matching** → Compares with known encodings (`compare_faces()`).  
5. **Result Display** → Shows recognized name and verification status.  

### **How to Add a Known Face**  
1. Take a clear frontal face photo (`john.jpg`).  
2. Save it inside the `known_faces` folder.  
3. Restart the app (or dynamically reload encodings for updates).  

---

## **6. File Structure**  
```
face-recognition-app/
├── app.py                # Main application logic
├── known_faces/          # Directory for known face images
├── requirements.txt      # Required dependencies
└── README.md             # Project documentation
```

---

## **7. Technologies Used**  
- **Streamlit** – Web application framework.  
- **face_recognition** – High-performance facial recognition library.  
- **OpenCV (cv2)** – Real-time image processing.  
- **NumPy** – Numerical operations on image data.  
- **Pillow (PIL)** – Image loading and manipulation.  

---

## **8. Performance Considerations**  
- **Optimization Tips:**  
  - Use **smaller images** (resize before processing).  
  - Avoid extremely high-resolution uploads (>1080p).  
  - Consider **GPU acceleration** for faster processing.  
- **Speed vs. Accuracy Tradeoff:**  
  - More known faces → Slightly slower comparisons.  

---

## **9. Future Enhancements**  
- **Enhanced Security** – Add login authentication.  
- **Database Integration** – Store known faces in SQL/NoSQL databases.  
- **Video Stream Processing** – Continuous recognition from live video.  
- **Multi-face Detection** – Recognize multiple faces in one frame.  

---

## **10. Troubleshooting**  
### **Common Issues & Fixes**  
| **Issue** | **Possible Solution** |
|-----------|----------------------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` again. |
| No webcam detected | Check device permissions or use external webcam. |
| Slow face recognition | Reduce image resolution or optimize known_faces size. |
| "Unknown" face despite being registered | Use higher-quality reference images. |

---

## **11. License**  
This project is licensed under the **[MIT License](https://opensource.org/licenses/MIT)**.  

---

### **Support & Contribution**  
For contributions, bug reports, or enhancements, open an issue in the [GitHub repository](https://github.com/priteshramani/Face-recognization-system).  
