# cad-viewer
📌 CAD Viewer – 3D Model Upload and Conversion
A web-based CAD Viewer that allows users to upload 3D model files, convert .glb to .obj, and view them using Three.js.

🚀 Features
✅ Upload .glb files and convert them to .obj
✅ View 3D models using Three.js
✅ Steps to Verify the 3D Model Viewer
Follow these steps:

1️⃣ Start the Backend
Make sure the backend is running:
    -  cd backend
    -  python app.py
2️⃣ Start the Frontend
Open a new terminal and start the frontend:
    -  cd frontend
    - npm start
3️⃣ Upload a .glb Model
Open the app in your browser:
👉 http://localhost:3000
Use the UI to upload a .glb file
The backend should convert the file to .obj and store it in backend/converted/
✅ Rotate, zoom, and pan controls for better visualization
✅ Simple backend API using Flask/Django

📂 Project Structure
cad-viewer/
│── backend/        # Backend API (Flask/Django)
│   ├── app.py      # Main backend script
│   ├── converted/  # Stores converted .obj files
│   ├── uploads/    # Stores uploaded .glb files
│   ├── venv/       # Virtual environment (not included in Git)
│── frontend/       # React frontend with Three.js
│   ├── src/        # React components
│   ├── public/     # Static assets
│── README.md       # Project documentation
⚡ Getting Started
1️⃣ Clone the Repository
git clone https://github.com/challaHemant/cad-viewer.git
   - cd cad-viewer
🖥️ Backend Setup
Navigate to the backend directory:
   - cd backend
Create and activate a virtual environment:
   - python3 -m venv venv
   - source venv/bin/activate  # On Mac/Linux
   - venv\Scripts\activate      # On Windows
Install dependencies:
  -pip install -r requirements.txt
Run the backend:
  -python app.py
💻 Frontend Setup
Navigate to the frontend directory:

cd ../frontend
Install dependencies:

  - npm install  # Or use yarn install
Start the React app:
  - npm start
📤 Upload & Convert a Model
Open the frontend (http://localhost:3000).
Upload a .glb file using the UI.
The backend will convert it to .obj format and store it in the converted/ directory.
🔍 Verify Conversion
After conversion, check if the .obj file was created:

ls -lh backend/converted/
If successful, you should see the .obj and .mtl files.

🎯 Future Enhancements
Add more 3D model format conversions (e.g., .stl, .fbx).
Improve error handling & progress tracking during conversion.
Optimize file storage & database integration for better management.
📜 License
This project is open-source and available under the MIT License.

🌟 Contributions & Feedback
If you find issues or have suggestions, feel free to open an issue on GitHub!
Want to contribute? Fork the repo and submit a pull request.
