from faker import Faker
from radish_ext.radish.step_config import StepConfig
from radish_rest.sdk.rest import RestConfigFromCfg

from conduit_rest.sdk.conduit_rest import ConduitRestClient


class ConduitStepsConfig(StepConfig):

    def __init__(self, context):
        super().__init__(context)
        self.client = ConduitRestClient(RestConfigFromCfg().set_properties(context.cfg, 'conduit_backend'))


class ConduitRestBaseSteps(object):
    def created_user(self, step, ):
        """created User"""
        stc_rest = ConduitStepsConfig.get_instance(step.context)
        faker_ = Faker()

        user_model = {'user': {'username': faker_.user_name(),
                               'password': faker_.password(),
                               'email': faker_.email()
                               }
                      }
        stc_rest.log.debug(user_model)
        ret_json = stc_rest.client.user.create_user(user_model)
        stc_rest.log.info(f'user created {ret_json}')
