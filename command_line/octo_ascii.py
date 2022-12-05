def print_octo_pet(binary=False):
  if(binary):
    print_octo_pet_binary()
  else:
    print_octo_pet_ascii()  

def print_octo_pet_ascii():
  print('   ____       __           ____       __ ')
  print('  / __ \_____/ /_____     / __ \___  / /_')
  print(' / / / / ___/ __/ __ \   / /_/ / _ \/ __/')
  print('/ /_/ / /__/ /_/ /_/ /  / ____/  __/ /_  ')
  print('\____/\___/\__/\____/  /_/    \___/\__/  ')
  print('                                         ')

def print_octo_pet_binary():
  print('01001111 01100011 01110100 01101111  01010000 01100101 01110100')
