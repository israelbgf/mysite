class Presenter(object):

    SUCCESS = 0

    def display(self, message_code, **params):
        raise NotImplementedError
