from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from files import fileManager as fm


@csrf_exempt
@require_POST
def recommend_user_prod(request):
    fm.handle_user_recProds_file(request.FILES['file'])
    response = HttpResponse("ok")
    response.status_code = 200
    return response
