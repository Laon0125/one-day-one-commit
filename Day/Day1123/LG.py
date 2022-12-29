class Tiger:
    def cry(self):
        print('엑소 으르렁')
        print()
    
    def jumpy(self):
        print('호랭이점프')
        print()

class Lion :
    def cry(self):
        print('카카오라이언')
        print ()

    def baseball(self):
        print('사자야구')
        print()

class Enco(Tiger,Lion) :
    def play(self):
        print('ecore')

enco = Enco()
enco.play()
enco.cry()
enco.baseball()
enco.jumpy()