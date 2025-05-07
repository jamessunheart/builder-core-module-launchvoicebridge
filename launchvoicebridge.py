from VoiceBridge import VoiceBridge

if __name__ == "__main__":
    vb = VoiceBridge()
    while True:
        vb.listen_and_respond()