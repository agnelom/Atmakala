import keras_ocr

# Load the model
pipeline = keras_ocr.pipeline(lang='marathi')

# Read the image
image = keras_ocr.tools.read_image('Page_01.jpg')

# Extract the text
prediction = pipeline.recognize([image])

# Print the extracted text
print(prediction[0][0])