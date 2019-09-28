from faker import Faker
from radish_ext.radish.step_config import StepConfig
from radish_rest.sdk.rest import RestConfigFromCfg

from conduit.client import ConduitClient, ConduitConfig


class ConduitStepsConfig(StepConfig):

    def __init__(self, context):
        super().__init__(context)
        self.client = ConduitClient(ConduitConfig().set_properties(context.cfg.get('conduit_backend').get('url')))

def get_conduit_config(context):
    return ConduitStepsConfig.get_instance(context)

class ConduitRestBaseSteps(object):
    def created_user(self, step, ):
        """created User"""
        stc_rest = get_conduit_config(step.context)

        faker_ = Faker()

        user_model = {'user': {'username': faker_.user_name(),
                               'password': faker_.password(),
                               'email': faker_.email()
                               }
                      }
        stc_rest.test_data.data.update(user_model)
        stc_rest.log.debug(user_model)
        ret_json = stc_rest.client.users.register_user(**user_model['user'])
        stc_rest.log.info(f'user created {ret_json}')
