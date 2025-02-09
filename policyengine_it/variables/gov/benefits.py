from policyengine_it.model_api import *


class benefits(Variable):
    value_type = float
    entity = Household
    label = "benefits"
    unit = EUR
    definition_period = YEAR
    adds = [
        "inclusion_checks",
        "universal_credit",
        "universal_credit_low_income_bonus",
    ]
