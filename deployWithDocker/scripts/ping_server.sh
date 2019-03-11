#!/usr/bin/env bash

#takes path to image, otherwise fox.jpg
curl -X POST -F image=@dog.jpg 'http://localhost:5000/predict'



#should return:
# 'beagle' 99.01% confidence
