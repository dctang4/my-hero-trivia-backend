# from django.shortcuts import render
from json.decoder import JSONDecodeError
from django.http import JsonResponse
from django.views import View

from .models import Highscore
from django.core.serializers import serialize
from json import loads

# Create your views here.
class HighscoreView(View):
  def get(self, req):
    # Serialize the data into JSON then turn the JSON into a dict
    all = loads(serialize('json', Highscore.objects.all()))
    # Send the JSON response\
    return JsonResponse(all, safe=False)

  def post(self, req):
    # Turn the body into a dict
    body = loads (req.body.decode('utf-8'))
    # create the new item
    newhighscore = Highscore.objects.create(
      name = body['name'],
      highscore = body['highscore'],
    )
    # Turn the object to json to dict, put in array to avoid non-iterable error
    data = loads(serialize('json', [newhighscore]))
    # send json response with new object
    return JsonResponse(data, safe=False)

class OneHighscoreView(View):
  def get(self, req, param):
    # Filter and find a single item then serialize the data into JSON then turn the JSON into a dict
    one = loads(serialize('json', Highscore.objects.filter(name=param)))
    # Send the JSON response
    return JsonResponse(one, safe=False)

  def put(self, req, param):
    # Turn the body into a dict
    body = loads(req.body.decode('utf-8'))
    # update the item
    Highscore.objects.filter(name=param).update(
      name = body['name'],
      highscore = body['highscore']
    )
    newhighscore = Highscore.objects.filter(name=param)
    # Turn the object to json to dict, put in array to avoid non-iterable error
    data = loads(serialize('json', newhighscore))
    # send json response with updated object
    return JsonResponse(data, safe=False)

  def delete(self, req, param):
    # delete the item, get all remaining records for response
    Highscore.objects.filter(name=param)
    newhighscores = Highscore.objects.all()
    # Turn the results to json to dict, put in array to avoid non-iterable error
    data = loads(serialize('json', newhighscores))
    # send json response with updated object
    return JsonResponse(data, safe=False)

