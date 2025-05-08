from load import Loader

def main(request):
    response = request.get_json()
    Loader().load(response)