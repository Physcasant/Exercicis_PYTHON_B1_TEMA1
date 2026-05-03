from ej2a2 import tax_calculation_global, tax_calculation_group_1


def test_variable_scope():
    assert tax_calculation_global(500) == 120, "tax_calculation_global does not return the correct value for input 500. It should be 120"
    assert tax_calculation_global(1250) == 300, "tax_calculation_global does not return the correct value for input 1250. It should be 300"
    assert tax_calculation_group_1(500) == 95, "tax_calculation_global does not return the correct value for input 500. It should be 95"
    assert tax_calculation_group_1(1250) == 237.5, "tax_calculation_global does not return the correct value for input 1250. It should be 237.5"
