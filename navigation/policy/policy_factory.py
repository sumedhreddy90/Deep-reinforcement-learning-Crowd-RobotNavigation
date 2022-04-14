policy_factory = dict()
def none_policy():
    return None

from navigation.policy.orca import ORCA
from navigation.policy.social_force import SOCIAL_FORCE
from navigation.policy.srnn import SRNN

policy_factory['orca'] = ORCA
policy_factory['none'] = none_policy
policy_factory['social_force'] = SOCIAL_FORCE
policy_factory['srnn'] = SRNN

