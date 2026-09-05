# Neural Network Guide Python
# Author: Luc Anthony Myers
# Python Vesion 3.11.9 (Virtual Envioment)
# - The Virtual Enviorment is used to run tesnsor flow
#   Tensorflow requires version 3.7 < x < 3.12
# 
# Summary:
# Learning how to make a Neural Network following a step by step guide
# 
# numpy: the fundamental open-source library for scientific computing in Python
# pandas: a powerful open source Python library used to primarily for data
#         manipulation, cleaning, and analysis
# Tensorflow Kera Models : A model grouping layer into an object with training/inference features
# Tensorflow Kera Layers : Layes for the model
#    - A layer is an object that packages both a compuatation function(the math applied to incoming data)
#    - State (the trainable weight or parameters that change as the model learns)
# 
#
# TODO
# Definition and Math about Binary Cross-entropy
# Why are labels important
# How are layers determiend



#Importing necessary libraries 
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

#Create and Load Dataset
data = {
    'feature1' : [0.1, 0.2, 0.3, 0.4, 0.5],
    'feature2' : [0.5, 0.4, 0.3, 0.2, 0.1],
    'label' : [0, 0, 1, 1, 1]
}
print("STEP 1: Raw Dataset")
print(data)

df = pd.DataFrame(data)
print("\nSTEP 2: DataFrame")
print(df)

X = df[['feature1', 'feature2']].values
y = df['label'].values

print("\nSTEP 3: Feature (X)")
print(X)

print("\nSTEP 3: Feature (Y)")
print(y)


#Create a Neural Network
model = Sequential()
model.add(Dense(8, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

print("\nSTEP 4:Neural Network Structure")
model.summary()

#Compiling the Model
# Binary Cross Entropy/Log Loss for Binary Classification :
#   - Binary cross-entropy (log loss) is a loss function used in binary 
#     classification problems. It quantifies the difference between the 
#     actual class labels (0 or 1) and the predicted probabilities output 
#     by the model. The lower the binary cross-entropy value, the better 
#     the model’s predictions align with the true labels.
# 
# 
# #
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

print("\nSTEP 5: Model Compiled")
#Training the Model
model.fit(X, y, epochs=100, batch_size=1, verbose=1)

#Make Predicions
#The Prediction 
test_data = np.array([[0.2, 0.4]])
prediction = model.predict(test_data)
predicted_label = (prediction > 0.5).astype(int)
print(predicted_label)