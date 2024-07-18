# arithmetic_app/views.py
from django.http import HttpResponse, JsonResponse
from .arithmetic import arithmetic_arranger
import logging

def arrange(request):
    problems = request.GET.getlist('problems')
    show_answers = request.GET.get('show_answers', 'false').lower() == 'true'

    logging.basicConfig(level=logging.DEBUG)
    logging.debug(f"Received problems: {problems}")

    try:
        result = arithmetic_arranger(problems, show_answers)
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)

    return HttpResponse(result, content_type='text/plain')

