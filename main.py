from load import Loader

def main(request):
    response = request.get_json()["transformed_data"]
    Loader().load(response)