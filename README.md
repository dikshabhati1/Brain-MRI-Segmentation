# Brain-MRI-Segmentation


# Problem
The task is classify the image i.e. have tumor or not.Then if there is a tumor, segment that part of tumor

# Approach
For classification used the transfer learning model and for segmentation used the ResUNet Architecture

# Results
Used callbacks to avoid overfitting.For classification task training acuracy achieved is 96.92% and the testing accuracy achieved is 93.44% and defined the custom loss function i.e. **Tversky Loss** and achieved 94.59% training tversky loss  and 86.26% testing tversky loss.

# Flask Demo
Made a flask app for testing the model in google colab.Below is the demo of the web app

![](https://github.com/dikshabhati1/Brain-MRI-Segmentation/blob/main/flask%20demo/ezgif.com-gif-maker.gif)

<br>

![](https://github.com/dikshabhati1/Brain-MRI-Segmentation/blob/main/flask%20demo/flask1.jpeg)

<br>

![](https://github.com/dikshabhati1/Brain-MRI-Segmentation/blob/main/flask%20demo/flask2.jpeg)

