# Import Pillow imaging library
from PIL import Image
import face_recognition

# Load image into variable
image = face_recognition.load_image_file('./img/groups/group1.jpg')
face_locations = face_recognition.face_locations(image)

# Get face image in form of array, save it as the top value
for face_location in face_locations:
    top, right, bottom, left = face_location

    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    # Open all images
    # pil_image.show()
    pil_image.save(f'{top}.jpg')