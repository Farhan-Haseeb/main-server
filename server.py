import socket
from farhan import PSO
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostbyname(""), 5000))
s.listen(6)

print(f"Server is up!")

connected = []

while True:
    client_socket, address = s.accept()
    print(f"Connection from {address} has been established! ")
    particle_address = list(address);
    particle_address =  particle_address[0] + ':' + str(particle_address[1])
    connected.append({'address': particle_address, 'initials': [1, 2]})
    client_socket.send(bytes(f"You have connected to the server {address}", "utf-8"))
    if len(connected) >= 4:
        break


bounds = [(0, 2), (10, 16)] # Tells the algorithm to find in these section or bounds
pos = PSO(optimization_function, connected, bounds, num_particles = 4, maxiter=10)
final_value = pso.run()