from radish_rest.sdk.rest import RestClient


class ConduitRestClient(RestClient):
    """Conduit REST client"""

    def __init__(self, rest_config):
        super().__init__(rest_config)
        self.user = ConduitUserTools(self)


class ConduitBaseTools(object):
    def __init__(self, client):
        self.client = client


class ConduitUserTools(ConduitBaseTools):
    USERS = '/api/users'

    def create_user(self, user_model):
        response = self.client.post(self.USERS, json=user_model)
        self.client.check_status(response)
        return response.json()
