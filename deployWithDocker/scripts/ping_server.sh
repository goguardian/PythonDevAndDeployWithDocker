#!/usr/bin/env bash

#check health
curl  'http://localhost:8081/health'

#takes path to image, otherwise fox.jpg
curl -X POST -F image=@dog.jpg 'http://localhost:5000/predict'



#should return:
