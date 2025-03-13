class PacketParser:
    def CONNACK(self, packet):
        CONNACK = 0x20           #fixed header=2
        if packet[0] == CONNACK:
            print('Received CONNACK.')
            if packet[3] == 0x00:  #00  conexiune reusita
                return True
            else:
                return False
        return False
    
    def PINGRESP(self, packet):
        PINGRESP = 0xD0
        if packet[0] == PINGRESP:
            print('Received PINGRESP.')
            return True
        return False
    
    def SUBACK(self, packet):
        SUBACK = 0x90
        if packet[0] == SUBACK:
            print('Received SUBACK.')
            return True
        return False
    
    def UNSUBACK(self, packet):
        UNSUBACK = 0xB0
        if packet[0] == UNSUBACK:
            print('Received UNSUBACK')
            return True
        return False
    
    def PUBACK(self, packet):
        PUBACK = 0x40
        if packet[0] == PUBACK:
            print('\nReceived PUBACK')
            return True
        return False

    def PUBREC(self, packet):
        PUBREC = 0x50
        if packet[0] == PUBREC:
            print('\nReceived PUBREC')
            return True
        return False

    def PUBCOMP(self, packet):
        PUBCOMP = 0x70
        if packet[0] == PUBCOMP:
            print('Received PUBCOMP')
            return True
        return False
    
    def PUBREL(self, packet):
        PUBREL = 0x62
        if packet[0] == PUBREL:
            print('Received PUBREL.')
            return True
        return False
    
    #####PT MESAJE
    def PUBLISH0(self, packet):
        #PUBLISH2 = 0x31
        if packet[0] == 0x31 or packet[0] == 0x30:
            print('Received PUBLISH QOS 0.')
            return True 
        return False 
    
    def PUBLISH1(self, packet):
        #PUBLISH2 = 0x31
        if packet[0] == 0x33 or packet[0] == 0x32:
            print('Received PUBLISH2 QOS 1.')
            return True
        return False 
    
    def PUBLISH2(self, packet):
        #PUBLISH2 = 0x31
        if packet[0] == 0x35 or packet[0] == 0x34:
            print('Received PUBLISH2 QOS 2.')
            return True
        return False 
    