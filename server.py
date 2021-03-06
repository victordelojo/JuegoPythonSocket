import socket, sys, pygame, time, os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 100)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)


pygame.init()

size = width, height = 320, 240
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
print(os.path.join(""))
ball = pygame.image.load( os.path.join("intro_ball.gif"))
ballrect = ball.get_rect()

print('waiting for a connection')

connection, client_address = sock.accept()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    time.sleep(0.03)
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    
    try:
        print((str(ballrect.left)+'|'+str(ballrect.left)+"|"+str(ballrect.top)+"|"+str(ballrect.bottom)).encode())
        connection.sendall((str(ballrect.left)+'|'+str(ballrect.left)+"|"+str(ballrect.top)+"|"+str(ballrect.bottom)).encode())
    except:
        

        connection.close()
        connection, client_address = sock.accept()