from core.utils.presenter import Presenter


class BlankResponsePresenterAPI(Presenter):
    def display(self, message_code, **params):
        pass

    def create_response(self):
        return ''
