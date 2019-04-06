# Import Pillow imaging library
from PIL import Image, ImageDraw
import face_recognition

# Load image of Jeffrey Tambor
image_of_jeffrey = face_recognition.load_image_file('./img/known/Jeffrey Tambor.jpg')

# Get face encoding (facial features to compare) against other pictures
jeffrey_face_encoding = face_recognition.face_encodings(image_of_jeffrey)[0]

# Load image of David Cross
image_of_david = face_recognition.load_image_file('./img/known/David Cross.jpg')

# Get face encoding (facial features to compare) against other pictures
david_face_encoding = face_recognition.face_encodings(image_of_david)[0]

# Create arrays of encodings and names
known_face_encodings = [
    jeffrey_face_encoding,
    david_face_encoding
]

known_face_names = [
    "Jeffrey Tambor",
    "David Cross"
]

# Load test image to find faces in
test_image = face_recognition.load_image_file('./img/groups/jeffreydavid.jpg')

# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)