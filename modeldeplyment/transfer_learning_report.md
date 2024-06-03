Model: "sequential_1"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 vgg16 (Functional)          (None, 1, 1, 512)         14714688  
                                                                 
 flatten_1 (Flatten)         (None, 512)               0         
                                                                 
 dense_2 (Dense)             (None, 256)               131328    
                                                                 
 dropout (Dropout)           (None, 256)               0         
                                                                 
 dense_3 (Dense)             (None, 10)                2570      
                                                                 
=================================================================
Total params: 14,848,586
Trainable params: 133,898
Non-trainable params: 14,714,688

Performance Metrics
The test accuracy of the transfer learning model was found to be approximately 98%. This result is not much better than the baseline model, which indicates that the fine-tuning process might need adjustments such as adjusting the learning rate, using different layers for fine-tuning, or employing data augmentation techniques to further improve performance.





