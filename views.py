#from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse
#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser
#from movietickets.models import Movietickets
#from movietickets.serializers import MovieticketsSerializer
from movietickets.models import Movietickets
from movietickets.serializers import MovieticketsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

# Create your views here.
"""@csrf_exempt
def booking_list(request):
    if request.method == 'GET':
        movie = Movietickets.objects.all()
        serializer = MovieticketsSerializer(movietickets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MovieticketsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def booking_detail(request, pk):
    try:
        movie = Movietickets.objects.get(pk=pk)
    except Movietickets.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MovieticketsSerializer(movie)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MovieticketsSerializer(movie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        movie.delete()
        return HttpResponse(status=204)
"""


"""@api_view(['GET', 'POST'])
def booking_list(request, format=None):
    if request.method == 'GET':
        movietickets = Movietickets.objects.all()
        serializer = MovieticketsSerializer(movietickets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieticketsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def booking_detail(request, pk, format=None):
    try:
        movietickets = Movietickets.objects.get(pk=pk)
    except Movietickets.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieticketsSerializer(movietickets)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieticketsSerializer(movietickets, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movietickets.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        """
"""class BookingList(APIView):

    def get(self, request, format=None):
        movietickets = Movietickets.objects.all()
        serializer = MovieticketsSerializer(movietickets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieticketsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingDetail(APIView):

    def get_object(self, pk):
        try:
            return Movietickets.objects.get(pk=pk)
        except Movietickets.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movietickets = self.get_object(pk)
        serializer = MovieticketsSerializer(movietickets)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        movietickets = self.get_object(pk)
        serializer = MovieticketsSerializer(movietickets, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movietickets = self.get_object(pk)
        movietickets.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""



"""class BookigList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Movietickets.objects.all()
    serializer_class = MovieticketsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookingDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Movietickets.objects.all()
    serializer_class = MovieticketsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""

class BookingList(generics.ListCreateAPIView):
    queryset = Movietickets.objects.all()
    serializer_class = MovieticketsSerializer


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movietickets.objects.all()
    serializer_class = MovieticketsSerializer