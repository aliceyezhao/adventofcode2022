def random_packets():
    packet_file = open('advent6.txt', 'r')
    packet = packet_file.read()
    for i in range(len(packet)):
        j = i + 4
        if len(set(packet[i:j])) == 4:
            return j

def longer_random_packets():
    packet_file = open('advent6.txt', 'r')
    packet = packet_file.read()
    for i in range(len(packet)):
        j = i + 14
        if len(set(packet[i:j])) == 14:
            return j
        
if __name__== "__main__":
    print("Start of packet marker is after character ", random_packets())
    print("Start of longer packet marker is after character ", longer_random_packets())