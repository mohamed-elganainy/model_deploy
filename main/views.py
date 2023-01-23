from django.shortcuts import render
from . import models
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
import pickle
import numpy as np
import pandas as pd
from rest_framework.response import Response
from . import serializers
import time
from rest_framework import status


class Predict(ListCreateAPIView):
    queryset = models.Features.objects.all()
    serializer_class = serializers.features_serializer
    
    model_path = models.Model_File.objects.last().file.url
    model = pickle.load(open(f'./{model_path}', 'rb'))
    
    def post(self, request, *args, **kwargs):
        start_time = time.time()
        data_json = request.data
        try:
            data = np.array([list(data_json.values())[1::]],dtype=np.float64)
            data = data.reshape(-1, 1)
            data = data.T
            
            
        except ValueError as ve:
            end_time = time.time()
            return Response( {
                'error_code' : '-1',
                "info": str(ve),
                'respons_time':round(end_time-start_time,4)
            },status=status.HTTP_502_BAD_GATEWAY)

        try:
            output = self.model.predict(data)
            end_time = time.time()
            return Response({'model output is: ':output[0],'respons_time':round(end_time-start_time,4)},status=status.HTTP_200_OK)
        
        except ValueError as ve:
            end_time = time.time()
            return Response( {
                'error_code' : '-1',
                "info": str(ve),
                'respons_time':round(end_time-start_time,4)
            },status=status.HTTP_502_BAD_GATEWAY)
    
    