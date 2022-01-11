from django.http import HttpResponse

def website(request):
    tag='''
    <a href="https://www.youtube.com" target="_blank">youtube</a>
    <br>
    <a href="https://www.facebook.com" target="_blank">facebook</a>
    <br>
    <a href="https://www.mongodb.com" target="_blank">mongodb</a>
    <br>
    <a href="https://www.npmjs.com" target="_blank">npmjs</a>
    '''
    return HttpResponse(tag)
