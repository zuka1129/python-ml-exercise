import aiml

kernel = aiml.Kernel()
kernel.learn('start_up.xml')
kernel.respond('load chat robot')
while True:
    print(kernel.respond(input('Please enter you topic >>>')))