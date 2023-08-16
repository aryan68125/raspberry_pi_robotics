import netifaces
def find_gateway():
      Interfaces= netifaces.interfaces()
      # print(Interfaces)
      for inter in Interfaces:
           if inter == "wlan0": #wlx1cbfce1924fc is the chip id for the wifi dongle instead of wlan0 which is the default wifi card
                temp_list = []
                Addresses = netifaces.ifaddresses(inter)
                gws = netifaces.gateways()
                temp_list = list (gws['default'][netifaces.AF_INET])
                count =0
                for item in temp_list:
                      count +=1
                      if count ==1:
                           print (item)
                      else:
                           pass
                # print(str(Addresses))
                ls = Addresses[2]
                target_dictionary = ls[0]
                addr = target_dictionary['addr']
                netmask = target_dictionary['netmask']
                broadcast = target_dictionary['broadcast']
                print("\ngetting wifi ip address assigned by the router ----->")
                print("wifi ip address -> {}".format(addr))
                print("wifi netmask --> {}".format(netmask))
                print("wifi broadcast -> {}".format(broadcast))

           if inter == "enp3s0":
                temp_list = []
                Addresses = netifaces.ifaddresses(inter)
                gws = netifaces.gateways()
                temp_list = list (gws['default'][netifaces.AF_INET])
                count =0
                for item in temp_list:
                      count +=1
                      if count ==1:
                           print (item)
                      else:
                           pass
                      ls = Addresses[2]
                      target_dictionary = ls[0]
                      addr = target_dictionary['addr']
                      netmask = target_dictionary['netmask']
                      broadcast = target_dictionary['broadcast']
                      print("\ngetting ethernet ip address assigned by the router ----->")
                      print("ethernet ip address -> {}".format(addr))
                      print("ethernet netmask --> {}".format(netmask))
                      print("ethernet broadcast -> {}".format(broadcast))
      return  addr
Addr = find_gateway()
