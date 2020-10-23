import socket, sys, pygame, time
from time import sleep

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


pygame.init()

size = width, height = 320, 240
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load(r"C:\Users\victo\Documents\java\juego\intro_ball.gif")
ballrect = ball.get_rect()
server_address = ('localhost', 10000)
sock.connect(server_address)

while 1:
    # Connect the socket to the port where the server is listening
    

    try:
        sock.sendall(b"")
        data = sock.recv(16)
        print('received {!r}'.format(data))
        speed=list(map(int,data.decode().split(",")))
        print(speed)
    finally:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        time.sleep(0.03)
        ballrect = ballrect.move(speed)
        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()

print('closing socket')
sock.close()