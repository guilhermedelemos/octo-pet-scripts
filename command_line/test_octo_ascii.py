import pytest
import sys

from command_line.octo_ascii import octo_pet_ascii, octo_pet_binary, print_octo_pet

ascii = '   ____       __           ____       __ ' + '\n' \
       r'  / __ \_____/ /_____     / __ \___  / /_' + '\n' \
       r' / / / / ___/ __/ __ \   / /_/ / _ \/ __/' + '\n' \
       r'/ /_/ / /__/ /_/ /_/ /  / ____/  __/ /_  ' + '\n' \
       r'\____/\___/\__/\____/  /_/    \___/\__/  ' + '\n' \
       r'                                         '

binary = '01001111 01100011 01110100 01101111  01010000 01100101 01110100'


def test_ascii():
  assert octo_pet_ascii() == ascii

def test_binary():
  assert octo_pet_binary() == binary

def test_print_octo_pet(capsys):
  print_octo_pet()
  assert capsys.readouterr().out == ascii + '\n'
  print_octo_pet(True)
  assert capsys.readouterr().out == binary + '\n'
