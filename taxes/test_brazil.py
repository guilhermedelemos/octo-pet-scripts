import pytest

from taxes.brazil import calculate_inss, calculate_fgts, calculate_irpf

gross_salary_1 =    700.00
gross_salary_2 =  1_500.00
gross_salary_3 =  2_500.00
gross_salary_4 =  3_500.00
gross_salary_5 =  4_500.00
gross_salary_6 =  5_000.00
gross_salary_7 = 10_500.00

def test_fgts():
  assert calculate_fgts(gross_salary_1) == 56.00
  assert calculate_fgts(gross_salary_2) == 120.00

def test_inss():
  assert calculate_inss(gross_salary_1) == pytest.approx(52.50)
  assert calculate_inss(gross_salary_2) == pytest.approx(116.82)
  assert calculate_inss(gross_salary_3) == pytest.approx(209.00, rel=1e-6, abs=1e-3)
  assert calculate_inss(gross_salary_6) == pytest.approx(536.18, rel=1e-6, abs=1e-2)
  assert calculate_inss(gross_salary_7) == pytest.approx(828.39)

def test_irpf():
  assert calculate_irpf(gross_salary_1) == 0
  assert calculate_irpf(gross_salary_1, 1) == 0
  assert calculate_irpf(gross_salary_2) == 0
  assert calculate_irpf(gross_salary_3) == pytest.approx(29.02, rel=1e-6, abs=1e-2)
  assert calculate_irpf(gross_salary_3, 1) == pytest.approx(14.81, rel=1e-6, abs=1e-2)
  assert calculate_irpf(gross_salary_4) == pytest.approx(120.85, rel=1e-6, abs=1e-2)
  assert calculate_irpf(gross_salary_4, 1) == pytest.approx(92.41, rel=1e-6, abs=1e-2)
  assert calculate_irpf(gross_salary_5) == pytest.approx(271.48, rel=1e-6, abs=1e-2)
  assert calculate_irpf(gross_salary_5, 1) == pytest.approx(228.82, rel=1e-6, abs=1e-2)
  assert calculate_irpf(gross_salary_6) == pytest.approx(368.23, rel=1e-6, abs=1e-2)
  assert calculate_irpf(gross_salary_6, 1) == pytest.approx(325.57, rel=1e-6, abs=1e-2)
  assert calculate_irpf(gross_salary_7) == pytest.approx(1790.33, rel=1e-6, abs=1e-2)
  assert calculate_irpf(gross_salary_7, 1) == pytest.approx(1738.20, rel=1e-6, abs=1e-2)
