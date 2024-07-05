from policyengine_it.model_api import *


class dependent_spouse_deduction(Variable):
    value_type = float
    entity = Person
    label = "Total value of the dependent spouse deduction"
    definition_period = YEAR

    adds = [
        "dependent_spouse_base_amount",
        "dependent_spouse_additional_amount",
    ]