from enum import Enum
class Encryption(Enum):
    WPA_PSK = "wpa"
    WEP = "wep"
    NONE = "none"
    NA = ""

class PyWiFi:
    def __init__(self, hotspot_enabled=False):
        self.wifi_list = []
        self.connected_to = ""
        self.current_auth = ""
        self.encryption_type = Encryption.NA
        self.hotspot_enabled = hotspot_enabled
        self.hotspot_ssid = ""
        self.hotspot_encryption = Encryption.NA
        self.hotspot_auth = ""

    def scan(self):
        result = Cell.all('wlan0')
        self.wifi_list = []
        for wifi in result:
            self.wifi_list.append(wifi.ssid)

    def connect(self, ssid, enc, key=""):
        if ssid in self.wifi_list:
            self.connected_to = ssid
            self.encryption_type = enc
            if not self.encryption_type == Encryption.NONE:
                print("connecting wow")
                self.current_auth = key
                cell = Cell.all('wlan0')
                scheme = Scheme.for_cell("wlan0", self.connected_to, cell, self.current_auth)
                scheme.save()
                scheme.activate()
            else:
                cell = Cell.all('wlan0')
                scheme = Scheme.for_cell("wlan0", self.connected_to, cell)
                scheme.save()
                scheme.activate()
        else:
            print("invalid ssid")
