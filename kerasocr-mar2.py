#import keras_ocr
import matplotlib.pyplot as plt



# Load a language-specific model for Marathi
recognizer = keras_ocr.recognition.Recognizer(weights='marathi',build_params=dict(script_detection=True))

# Set up the pipeline

#pipeline = keras_ocr.pipeline.Pipeline()
# Load Devanagari script model for Marathi
pipeline = keras_ocr.pipeline.Pipeline(recognizer=recognizer)

# Load the image
image = keras_ocr.tools.read('/Users/agnelomarques/image.jpg')


# Recognize the text in the image
prediction = pipeline.recognize([image])

# Plot the prediction
plt.imshow(image)
plt.title(prediction)
plt.show()

print(prediction)