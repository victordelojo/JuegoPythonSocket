import socket, sys, pygame, time
from time import sleep

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


pygame.init()

size = width, height = 320, 240
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load(r".\intro_ball.gif")
ballrect = ball.get_rect()
server_address = ('localhost', 100)
try:
    sock.connect(server_address)
except Exception:
    pass


while 1:
    # Connect the socket to the port where the server is listening
    

    try:
        sock.sendall(b"")
        data = sock.recv(16)
        print('received {!r}'.format(data))
        position=list(map(int,data.decode().split("|")))
        print(position)
        ballrect.left=position[0]
        ballrect.top=position[2]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit(), sys.exit()
        time.sleep(0.03)
        #ball.scroll(position[0],position[2])
        screen.fill(black)
        screen.blit(ball,ballrect)
    except ValueError:
        print("error")
    except KeyboardInterrupt:
        pygame.exit()
    except IndexError:
        print("Error de indice de los datos enviados")
    except ConnectionRefusedError:
        print("No se conecta")
        sock.connect(server_address)
    except Exception:
        print(Exception)
        
    finally:
        pygame.display.flip()

print('closing socket')
sock.close()