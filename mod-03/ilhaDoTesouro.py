print('Bem-vindo(a) a ilha do tesouro perdido!')
print('Sua missão é encontrar o tesouro!')

print('''
         /'=----=           ______
            ((    ||          "--.__."
             "  @>||_____________//
          _______ /^\"""""""""""//\========)
         _--"""--/-. "\        // _\-:::-/_-.
       ." .-"""-/ "_\  "\  == // ;::\:::/::".\
      ; /     _/ "  \\   "\-+//--..._\_/:::::\\
      . ;    o    . ||   ( ()/)======(o)::::::.
      . \         ; .|    -|.;____...."b:::::;
       . -._  _ -  ;       ==    :::::::::::;
        "-..____.'     ls         ":::::::' 
      ''')

choice1 = input('''Você está em uma encruzilhada, para onde você deseja ir? Digite
      "esquerda" ou "direita" . ''').lower()

if choice1 == 'esquerda':
    choice2 = input('Você deseja nadar ou esperar? ').lower()
    if choice2 == 'nadar':
       choice3 = input('Qual porta deseja abrir: Vermelha, Amarela, Azul: ').lower()
    if choice3 == 'vermelha':
        print('Game over')
    elif choice3 == 'amarela':
        print('Parabéns você achou o tesouro')
    elif choice3 == 'azul':
        print('Comigo por feras')
    else:
        print('Você escolheu uma alternativa que não existe')
        
else:
    print('Game Over')