import face_recognition

# Load image of obama
image_of_obama = face_recognition.load_image_file('./img/known/Barack Obama.jpg')

# Get face encoding (facial features to compare) against other pictures of Barack Obama
obama_face_encoding = face_recognition.face_encodings(image_of_obama)[0]

# Load unknown_image
unknown_image = face_recognition.load_image_file('./img/unknown/barack-obama-impersonator-7.jpg')
# unknown_image = face_recognition.load_image_file('./img/unknown/Donald Trump.jpeg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare the two faces
results = face_recognition.compare_faces([obama_face_encoding], unknown_face_encoding)

if results[0]:
    print('This is Barack Obama.')
else:
    print('This is not the Obaminator.')