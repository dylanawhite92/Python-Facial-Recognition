import face_recognition

# Load image into variable
image = face_recognition.load_image_file('./img/groups/group1.jpg')
face_locations = face_recognition.face_locations(image)

# Array of coordinates of each face
# print(face_locations)

# Number of people in an image
print(f'There are {len(face_locations)} people in this image.')