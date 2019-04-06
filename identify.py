# Import Pillow imaging library
from PIL import Image, ImageDraw
import face_recognition

# Load image of Jeffrey Tambor
image_of_jeffrey = face_recognition.load_image_file(
    './img/known/Jeffrey Tambor.jpg')

# Get face encoding (facial features to compare) against other pictures
jeffrey_face_encoding = face_recognition.face_encodings(image_of_jeffrey)[0]

# Load image of David Cross
image_of_david = face_recognition.load_image_file(
    './img/known/David Cross.jpg')

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

# Convert to PIL format
pil_image = Image.fromarray(test_image)

# Create an ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through faces in test image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(
        known_face_encodings, face_encoding)

    name = "Unknown Person"

    # If match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw box
    draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0))

    # Draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)),
                   fill=(255, 255, 0), outline=(255, 255, 0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(0, 0, 0))

del draw

# Display image
pil_image.show()

# Save image
pil_image.save('identified.jpg')
