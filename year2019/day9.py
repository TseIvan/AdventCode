from IntCode import IntCode, parseFile
def run():
    i = IntCode([104,1125899906842624,99]) # Works cus python handles big nums
    i.compile()
    print(i.output[-1])

    i = IntCode([1102,34915192,34915192,7,4,7,99,0])
    i.input_signal(1)
    print(i.output[-1])

    i = IntCode([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])
    i.input_signal(1)
    print(i.output) # Quine

    i = IntCode(parseFile('day9.txt'))
    i.input_signal(1)
    print(i.output)

    i = IntCode(parseFile('day9.txt'))
    i.input_signal(2)
    print(i.output)
    return

run()
