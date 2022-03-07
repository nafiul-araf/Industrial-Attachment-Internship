# Image Recognition System
Image Recognition project for detecting an is human or not human or blank, or the image is unclear or not aligned in the right place. This project is under industrial attachment in Teletalk BD.

![Demo API](https://github.com/nafiul-araf/Industrial-Attachment-Internship/blob/main/ourput.PNG)

## Objectives
- Is the picture show human?
- Is the picture blank?
- Is the picture in right allignment?

## Description 
> In this project we develop an image recognition system using state-of-art [Convolutional Neural Network](https://en.wikipedia.org/wiki/Convolutional_neural_network)(CNN). 

> Here we have used both [plain CNN Model](https://towardsdatascience.com/understanding-cnn-convolutional-neural-network69fd626ee7d4#:~:text=CNN%20is%20a%20type%20of,features%20automatically%20for%20better%20classification.) and also [transfer learning](https://machinelearningmastery.com/transfer-learning-for-deep-learning/). 

> Before going to the model, we have done some [data augmentation](https://www.analyticsvidhya.com/blog/2021/03/image-augmentation-techniques-for-training-deep-learning-models/) to expand our dataset.

> In plain CNN model, we have used 5 convolution layers with 2 dense fully connected layers. 

> In transfer learning, we have tried 7 pretrained models including: 
- [VGG16](https://www.geeksforgeeks.org/vgg-16-cnn-model/)
- [Xception](https://keras.io/api/applications/xception/)
- [Inception Version 3](https://paperswithcode.com/method/inception-v3)
- [ResNet50](https://towardsdatascience.com/understanding-and-coding-a-resnet-in-keras-446d7ff84d33)
- [DenseNet121](https://towardsdatascience.com/creating-densenet-121-with-tensorflow-edbc08a956d8)
- [DenseNet169](https://docs.openvino.ai/latest/omz_models_model_densenet_169.html)
- [DenseNet201](https://keras.io/api/applications/densenet/)

## Performances
> Among those models we have got at most 93% accuracy using Xception model and 92% accuracy using DenseNet201 model.

![Loss and Accuracy](https://github.com/nafiul-araf/Industrial-Attachment-Internship/blob/main/Performances/Attachment1.PNG)

- Here's the performance of the Xception Model
![CR_Xceptiion](https://github.com/nafiul-araf/Industrial-Attachment-Internship/blob/main/Performances/Attachment2.PNG)

- - Here's the performance of the DenseNet201 Model
![CR_DenseNet201](https://github.com/nafiul-araf/Industrial-Attachment-Internship/blob/main/Performances/Attachment3.PNG)
