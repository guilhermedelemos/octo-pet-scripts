def calculate_inss(gross_salary):
  tier1_salary = 1212.00
  tier1_tax_rate = 0.075
  tier2_salary = 2427.35
  tier2_tax_rate = 0.09
  tier3_salary = 3641.03
  tier3_tax_rate = 0.12
  tier4_salary = 7087.22
  tier4_tax_rate = 0.14

  tier1_tax = tier1_salary * tier1_tax_rate
  tier2_tax = (tier2_salary - tier1_salary) * tier2_tax_rate
  tier3_tax = (tier3_salary - tier2_salary) * tier3_tax_rate
  tier4_tax = (tier4_salary - tier3_salary) * tier4_tax_rate

  if gross_salary <= tier1_salary:
    tier1_tax = gross_salary * tier1_tax_rate
    tier2_tax = 0
    tier3_tax = 0
    tier4_tax = 0
  elif gross_salary <= tier2_salary:
    if gross_salary < tier2_salary:
      tier2_tax = (gross_salary - tier1_salary) * tier2_tax_rate
    tier3_tax = 0
    tier4_tax = 0
  elif gross_salary <= tier3_salary:
    if gross_salary < tier3_salary:
      tier3_tax = (gross_salary - tier2_salary) * tier3_tax_rate
    tier4_tax = 0
  elif gross_salary < tier4_salary:
    tier4_tax = (gross_salary - tier3_salary) * tier4_tax_rate

  return tier1_tax + tier2_tax + tier3_tax + tier4_tax

def calculate_irpf(gross_salary, dependants=0):
  tier1_value = 1903.98
  tier1_tax_rate = 0
  tier1_deductible_portion=0
  tier2_value = 2826.65
  tier2_tax_rate = 0.075
  tier2_deductible_portion=142.80
  tier3_value = 3751.05
  tier3_tax_rate = 0.15
  tier3_deductible_portion=354.80
  tier4_value = 4664.68
  tier4_tax_rate = 0.225
  tier4_deductible_portion=636.13
  tier5_tax_rate = 0.275
  tier5_deductible_portion=869.36

  inss = calculate_inss(gross_salary)
  dependants_deduction = 189.59 * dependants
  total_deductions = inss + dependants_deduction
  calculation_basis = gross_salary - total_deductions
  
  if calculation_basis <= tier1_value:
    return calculation_basis * tier1_tax_rate - tier1_deductible_portion
  elif calculation_basis <= tier2_value:
    return calculation_basis * tier2_tax_rate - tier2_deductible_portion
  elif calculation_basis <= tier3_value:
    return calculation_basis * tier3_tax_rate - tier3_deductible_portion
  elif calculation_basis <= tier4_value:
    return calculation_basis * tier4_tax_rate - tier4_deductible_portion
  else:
    return calculation_basis * tier5_tax_rate - tier5_deductible_portion

def calculate_fgts(gross_salary):
  return gross_salary * 0.08
