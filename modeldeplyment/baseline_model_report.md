Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)             (None, 30, 30, 32)        896       
                                                                 
 max_pooling2d (MaxPooling2  (None, 15, 15, 32)        0         
 D)                                                              
                                                                 
 conv2d_1 (Conv2D)           (None, 13, 13, 64)        18496     
                                                                 
 max_pooling2d_1 (MaxPoolin  (None, 6, 6, 64)          0         
 g2D)                                                            
                                                                 
 conv2d_2 (Conv2D)           (None, 4, 4, 64)          36928     
                                                                 
 flatten (Flatten)           (None, 1024)              0         
                                                                 
 dense (Dense)               (None, 64)                65600     
                                                                 
 dense_1 (Dense)             (None, 10)                650       
                                                                 
=================================================================
Total params: 122570 (478.79 KB)
Trainable params: 122570 (478.79 KB)
Non-trainable params: 0 (0.00 Byte)


Layer Details
Conv2D Layer 1: Applies 32 filters of size 3x3, followed by a ReLU activation function.
MaxPooling2D Layer 1: Performs max pooling with a 2x2 pool size, reducing the spatial dimensions by half.
Conv2D Layer 2: Applies 64 filters of size 3x3, followed by a ReLU activation function.
MaxPooling2D Layer 2: Performs max pooling with a 2x2 pool size, reducing the spatial dimensions by half again.
Conv2D Layer 3: Applies 64 filters of size 3x3, followed by a ReLU activation function.
Flatten Layer: Flattens the 3D output of the previous layer to a 1D vector.
Dense Layer 1: Fully connected layer with 64 neurons and a ReLU activation function.
Dense Layer 2: Fully connected layer with 10 neurons (one for each class) and a softmax activation function to output probabilities for each class.
Training Process
The baseline model was trained using the following configuration:

Optimizer: Adam
Loss Function: Sparse Categorical Crossentropy
Metrics: Accuracy
The model was trained for 10 epochs using the CIFAR-10 training dataset, and the training process involved optimizing the weights of the network to minimize the loss function and improve accuracy.

Performance Metrics
After training, the model was evaluated on the CIFAR-10 test dataset. The following performance metrics were recorded:

Training Accuracy: The accuracy achieved on the training dataset during the last epoch of training.
Validation Accuracy: The accuracy achieved on the test dataset after training.
The test accuracy of the baseline model was found to be approximately 11.16%. This indicates that the model's performance is just slightly better than random guessing (which would yield an accuracy of around 10% for a 10-class classification problem).

Explanation of Results
The supwer high  test accuracy suggests that the baseline model is not effectively learning the features required to distinguish between the different classes in the CIFAR-10 dataset. This is likely due to the relatively simple architecture and limited capacity of the model. To improve performance, more complex architectures or techniques such as data augmentation, regularization, and transfer learning with pre-trained models can be employed to avoid model over fitting.





