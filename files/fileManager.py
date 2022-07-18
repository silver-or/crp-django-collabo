import os


def handle_user_recProds_file(file, test=False):
    '''Handle the received files below'''
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    save_path = os.path.join(BASE_DIR, file.name)
    with open(save_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
