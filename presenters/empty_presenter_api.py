from core.utils.presenter import Presenter


class EmptyPresenterAPI(Presenter):
    def display(self, message_code, **params):
        pass

    def create_response(self):
        return ''
