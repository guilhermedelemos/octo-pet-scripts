def print_octo_pet(binary=False):
  if(binary):
    print(octo_pet_binary())
  else:
    print(octo_pet_ascii())

def octo_pet_ascii():
  return r'   ____       __           ____       __ ' + '\n' \
         r'  / __ \_____/ /_____     / __ \___  / /_' + '\n' \
         r' / / / / ___/ __/ __ \   / /_/ / _ \/ __/' + '\n' \
         r'/ /_/ / /__/ /_/ /_/ /  / ____/  __/ /_  ' + '\n' \
         r'\____/\___/\__/\____/  /_/    \___/\__/  ' + '\n' \
         r'                                         '

def octo_pet_binary():
  return '01001111 01100011 01110100 01101111  01010000 01100101 01110100'
