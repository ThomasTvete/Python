import random

print('Det er høflig å si hva man heter når man snakker til noen')
introduction = input().lower()

if 'jeg heter ' in introduction:
    name = introduction.replace('jeg heter ', '').capitalize()
else:
    name = introduction.capitalize()

randNum = random.randint(1, 20)

print('Okay ' + name + ', jeg tenker på et tilfeldig tall mellom 1 og 20')

for guesses in range (6):
    print('Hvilket tall?')
    guess = input()
    try:
        if int(guess) < randNum:
            print('Du tenker for smått')
        elif int(guess) > randNum:
            print('Ikke overvurder tallet mitt nå')
        else:
            break
    except ValueError:
        print('Kanskje du skal skrive et faktisk tall')

if int(guess) == randNum:
    print('Wooow ' + name + ', så flink du er, du trengte bare ' + str(guesses + 1)
          + ' forsøk på å gjette rett. Du er klar for lotto nå.')
else:
    print('Heh, jeg tenkte på tallet ' + str(randNum) + '. Jaja, verden trenger tapere også.')

