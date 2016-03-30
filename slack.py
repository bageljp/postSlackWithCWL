from slacker import IncomingWebhook

DEFAULT_TIMEOUT = 10


class Slack(object):

    __slacker = None
    __data = {}
    __propeties = (
        'username', 'icon_emoji', 'channel', 'text', 'attachments'
     )

    def __init__(self, url, timeout=DEFAULT_TIMEOUT):
        self.__slacker = IncomingWebhook(url, timeout)
        self.__initial_data()

    def post(self):
        self.__generate_data()
        self.__slacker.post(self.__data)

    def __generate_data(self):
        for prop in self.__propeties:
            if getattr(self, prop) is not None:
                self.__data[prop] = getattr(self, prop)

    def __initial_data(self):
        for prop in self.__propeties:
            setattr(self, prop, None)
