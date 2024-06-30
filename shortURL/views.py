from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .utils.jsonops import jsonFileHandle
from datetime import datetime
import shortuuid
import json

from .models import ShortURL



read, write = jsonFileHandle('E:\FinalProjects\Learn Django\ShiftURL\demo.json')


def getURL_db(request, id):

    url = ShortURL.objects.get(short_url=id)
    return HttpResponseRedirect(url.original_url)

@csrf_exempt
def createURL_db(request):
    try :
        if request.method == 'POST':
            data = json.loads(request.body)
            original_url = data['original_url']
            if not original_url :
                return JsonResponse({'error' : 'Original URL is required'}, status=400)

            short_id = shortuuid.ShortUUID().random(length=6)
            new_url = ShortURL(short_url=short_id, original_url=original_url)
            new_url.save()

            return JsonResponse({'ShortURL': short_id})

    except Exception as e :
        return JsonResponse({'Error': str(e)}, status=400)









def getURL(request, id):
    data = read()
    for i in data :
        if i['short_id'] == id :
            return HttpResponseRedirect(i["original_url"])
    return HttpResponse("URL not found")


@csrf_exempt
def createShortURL(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)
            print(data)
            original_url = data.get('original_url')

            if not original_url:
                return JsonResponse({'error': 'Original URL is required'}, status=400)

            # Check if original_url already exists in data
            current_data = read()
            for i in current_data:
                if i['original_url'] == original_url:
                    return JsonResponse({'error': f"URL already exists with short_id {i['short_id']}"},
                                        status=400)

            # Generate short_id and current timestamp
            short_id = shortuuid.ShortUUID().random(length=6)
            created_at = str(datetime.now().date()).replace('-', '/')

            # Create new entry
            new_entry = {
                "short_id" : short_id,
                "original_url" : original_url,
                "clicks" : 0,
                "created_at" : created_at
            }

            write(new_entry)

            return JsonResponse(new_entry, status=201)

        except json.JSONDecodeError :
            return JsonResponse({'error' : 'Invalid JSON format in request body'}, status=400)
        except KeyError as e :
            return JsonResponse({'error' : f'Missing parameter: {e}'}, status=400)

    return JsonResponse({'error' : 'Method not allowed'}, status=405)
