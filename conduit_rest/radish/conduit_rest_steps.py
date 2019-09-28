import time

from faker import Faker
from radish_ext.radish.step_config import StepConfig

from conduit.client import ConduitClient, ConduitConfig


class ConduitStepsConfig(StepConfig):

    def __init__(self, context):
        super().__init__(context)
        self._faker = None
        self.client = ConduitClient(ConduitConfig().set_properties(context.cfg.get('conduit_backend').get('url')))

    @property
    def faker(self):
        if self._faker is None:
            self._faker = Faker(locale='en-us')
            seed = time.time()
            self.log.debug(f'Faker seed {seed}')
            self._faker.seed()
        return self._faker


def get_conduit_config(context):
    return ConduitStepsConfig.get_instance(context)


class ConduitRestBaseSteps(object):
    def created_user(self, step, ):
        """created User"""
        stc_rest = get_conduit_config(step.context)

        user_model = {'user': {'username': stc_rest.faker.user_name(),
                               'password': stc_rest.faker.password(),
                               'email': stc_rest.faker.email()
                               }
                      }
        stc_rest.test_data.data.update(user_model)
        stc_rest.log.debug(user_model)
        ret_json = stc_rest.client.users.register_user(**user_model['user'])
        stc_rest.log.info(f'user created {ret_json}')
