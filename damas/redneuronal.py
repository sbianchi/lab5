
from keras.models import Sequential
from keras.layers import Dense
import numpy


class RedNeuronal:  


    def __init__(self):	# create model
		self.model = Sequential()
		self.model.add(Dense(12, input_dim=3, activation='relu'))
		self.model.add(Dense(1, activation='sigmoid'))
		# Compile model
		self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

	def train(self,X,Y):
		self.model.fit(X, Y, epochs=150, batch_size=10)

	def eval(self,X,Y):		
		scores = self.model.evaluate(X, Y)

