import json
idx=json.load(open('D:/DevOps/aws-clf-c02-bridge/tools/ict-lessons-images.json',encoding='utf-8'))
s=[x for x in idx['sets'] if x['id']=='ictl-net-mcq'][0]['qs'][37:74]
R=[]
def add(q,qs,o,os=None):
    R.append(dict(q=q,qs=qs,o=o,os=os))
O_AB=["A only","B only","C only","A and B only","B and C only"]
S_AB=["A පමණි","B පමණි","C පමණි","A හා B පමණි","B හා C පමණි"]
O_ALL=["A only.","B only.","A and B only.","B and C only.","All of the above"]
S_ALL=["A පමණි.","B පමණි.","A හා B පමණි.","B හා C පමණි.","ඉහත සියල්ලම"]
O5=["A, B and C only.","A, B and D only.","A, C and D only.","B, C and D only.","All of the above."]
S5=["A, B හා C පමණි.","A, B හා D පමණි.","A, C හා D පමණි.","B, C හා D පමණි.","ඉහත සියල්ලම."]

add("Two machines with the IP addresses 192.248.16.30 and 192.248.16.90 are connected to a Local Area Network (LAN). Which of the followings is a suitable subnet mask for this network?",
"IP ලිපින 192.248.16.30 සහ 192.248.16.90 සහිත යන්ත්‍ර දෙකක් ස්ථානීය පෙදෙස් ජාලයකට (LAN) සම්බන්ධ කොට ඇත. පහත කවරක් මෙම ජාලය සඳහා සුදුසු උපජාල ආවරණයක් වන්නේ ද?",
["255.255.255.255","192.248.16.0","255.255.255.224","255.255.255.128","255.255.255.255"])
add("Which of the following is a correct IPv4 address?","පහත කවරක් නිවැරදි IPv4 ලිපිනයක් වන්නේ ද?",["192.248.0.0.1","192.258.2.1","8.8.8.8","10.256.8.9","255.255.255.268"])
add("User Datagram Protocol (UDP) is a ................ layer protocol.\nWhich of the following layers is the most suitable to fill the blank in the above statement?",None,
["physical","data link","network","transport","application"],["භෞතික","දත්ත සන්ධාන","ජාල","ප්‍රවාහන","යෙදුම්"])
add("Local Area Network (LAN) has 500 network devices. What is the most appropriate subnet mask for this computer network?",None,
["255.255.255.0","255.255.255.128","255.255.255.192","255.255.255.224","255.255.254.0"])
add("Consider the following statements regarding routing in IP networks:\nA - All routers must use a DNS server for IP packet forwarding.\nB - Routers must forward all receiving IP packets along the same path.\nC - A router may discard an IP packet.\nWhich of the above statement(s) is/are correct?",
None,O_AB,S_AB)
add("In a public key cryptographic system, the private key of a person x is given by the function priv(x) and the public key is given by the function pub(x). Consider the following statements:\nA - priv(x) and pub(x) should be the same for better security.\nB - A message encrypted using pub(x) can be decrypted using pub(x).\nC - The person x knows both priv(x) and pub(x).\nWhich of the above statement(s) is/are correct?",
None,["A only","C only","A and B only","A and C only","B and C only"],["A පමණි","C පමණි","A හා B පමණි","A හා C පමණි","B හා C පමණි"])
add("In electronic mail systems, the protocol used by mail clients to retrieve messages from the mail server is,",None,
["Simple Mail Transfer Protocol (SMTP)","File Transfer Protocol (FTP)","Internet Control Message Protocol (ICMP)","Internet Message Access Protocol (IMAP)","Telnet"])
add("The transport layer protocol User Datagram Protocol (UDP) can be used for is, User Datagram Protocol (UDP) is a protocol used for ............................... . Which of the following is the most suitable to fill the blank?".replace("is, User Datagram Protocol (UDP) is a protocol used for","").replace("can be used for  ","can be used for "),
None,
["reliable communication","guaranteed delivery","connection oriented communication","ordered delivery","exchanging state information among routers."],
["විශ්වසනීය සන්නිවේදනය","සහතික කරන ලද බෙදා හැරීම","සම්බන්ධතාහිමුඛ සන්නිවේදනය","ක්‍රමානුකූල බෙදා හැරීම","මංසුරු අතර තත්ත්ව තොරතුරු හුවමාරු කිරීම"])
add("The first and the last IP addresses of a subnet are 192.192.48.0 and 192.192.63.255 respectively. Which of the followings is the subnet mask of this subnet?",None,
["255.255.255.0","255.255.192.0","255.255.255.192","255.255.240.0","255.240.0.0"])
add("Which of the following statements regarding MAC addresses is correct?",None,
["Every network device has a unique MAC address.","Every network host has a unique MAC address.","Every network interface has a unique MAC address.","It is assigned for a device at the time of installation.","It is used for routing."])
add("172.16.48.200/24 is a,",None,
["host address in a class B network.","network address of a class C network.","host address in 172.16.48.0/24 subnet.","network address of a subnet with 255 hosts.","host address with 8 network bits."])
add("In TCP/IP computer networks, Transport Protocol Data Unit (TPDU) is referred to as a,",None,
["packet","frame","segment","window","message"],["පැකැට්ටුවක් ය.","රාමුවක් ය.","කොටසක් ය.","කවුළුවක් ය.","පණිවිඩයක් ය."])
add("Consider the following statements.\nA - In public key encryption systems each pair of communicating entities share a single key for encryption and decryption.\nB - Phishing is a type of social engineering attack often used to steal user data such as user name and password.\nC - Port scanning is a method which can be used by attackers to identify open ports or services on a network host.\nD - Digital signatures can be used for email message authentication.\nWhich of the above statements are correct?",
None,["B and C only.","A, B and C only.","A, C and D only.","B, C and D only.","All of the above."],["B හා C පමණි.","A, B හා C පමණි.","A, C හා D පමණි.","B, C හා D පමණි.","ඉහත සියල්ලම."])
add("Consider the following statements.\nA - DHCP server in an IP network dynamically allocates IP addresses to network devices.\nB - DNS server translates domain names to IP addresses.\nC - FTP server caches the recently accessed web pages.\nWhich of the above statement(s) is/are correct?",
None,O_ALL,S_ALL)
add("Consider the following statements.\nA - TCP is a connection oriented and a reliable protocol.\nB - UDP is a connectionless and an unreliable protocol.\nC - TCP and UDP are transport layer protocols.\nWhich of the above statement(s) is/are correct?",None,O_ALL,S_ALL)
add("In the OSI reference model, the network layer is responsible for ............................ communication.\nWhich of the following is suitable to fill the blank in the above statement?",None,
["node to node","source to destination","hop to hop","switch to router","process to process"])
add("Which of the following indicates the number of host bits and the number of IP addresses respectively in a class C network?",None,["8, 256","8, 65536","16, 256","16, 65536","24, 256"])
add("To which of the following network classes does the IP address 192.248.254.1 belong?",None,["A","B","C","D","E"])
add("In the OSI reference model, a protocol data unit of the network layer is referred to as a ............................. .\nWhich of the following terms is suitable to fill the blank in the above statement?",None,
["frame","segment","window","message","packet"],["රාමුව","ඛණ්ඩය","කවුළුව","පණිවිඩය","පැකැට්ටුව"])
add("Use of public key and private key in encryption and decryption processes is called,",None,
["asymmetric encryption","digital encryption","hybrid encryption","private key encryption","symmetric encryption"],["අසමමිතික ගුප්ත කේතනය ලෙස ය.","සංඛ්‍යාංක ගුප්ත කේතනය ලෙස ය.","දෙමුහුම් ගුප්ත කේතනය ලෙස ය.","පෞද්ගලික යතුරු ගුප්ත කේතනය ලෙස ය.","සමමිතික ගුප්ත කේතනය ලෙස ය."])
add("In a particular network, each node is connected directly to a central network device. This topology is referred to as a,",None,
["bus","hybrid","mesh","ring","Star"],["බස් ස්ථලකයක් ලෙස ය.","දෙමුහුම් ස්ථලකයක් ලෙස ය.","දැල් ස්ථලකයක් ලෙස ය.","මුදු ස්ථලකයක් ලෙස ය.","තාරකා ස්ථලකයක් ලෙස ය."])
add("Which of the following are the properties of a signal?",None,
["Amplitude, Clock time, Frequency and Wavelength","Amplitude, Frequency, Phase and Time","Amplitude, Frequency, Phase and Wavelength","Amplitude, Frequency, Time and Wavelength","Amplitude, Impulse, Phase and Wavelength"],
["විස්තාරය, ස්පන්දික වේගය, සංඛ්‍යාතය සහ තරංග ආයාමය","විස්තාරය, සංඛ්‍යාතය, කලාව සහ කාලය","විස්තාරය, සංඛ්‍යාතය, කලාව සහ තරංග ආයාමය","විස්තාරය, සංඛ්‍යාතය, කාලය සහ තරංග ආයාමය","විස්තාරය, ආවේගය, කලාව සහ තරංග ආයාමය"])
add("Which of the following options contains only guided media?",None,
["Coaxial, Fiber optics and Infrared","Coaxial, Fiber optics and Microwave","Coaxial, Fiber optics and Twisted pair","Coaxial, Infrared and Twisted pair","Fiber optics, Satellite communication and Twisted pair"],
["සමාක්ෂ, ප්‍රකාශ තන්තු සහ අධෝරක්ත","සමාක්ෂ, ප්‍රකාශ තන්තු සහ ක්ෂුද්‍ර තරංග","සමාක්ෂ, ප්‍රකාශ තන්තු සහ ඇඹරි යුගල","සමාක්ෂ, අධෝරක්ත සහ ඇඹරි යුගල","ප්‍රකාශ තන්තු, චන්ද්‍රිකා සන්නිවේදනය සහ ඇඹරි යුගල"])
add("The frequency modulation technique is used to change only,",None,
["the amplitude and frequency","the amplitude, frequency and phase","the amplitude and phase","the frequency","the frequency and phase"],["විස්තාරය සහ සංඛ්‍යාතය පමණි.","විස්තාරය, සංඛ්‍යාතය සහ කලාව පමණි.","විස්තාරය සහ කලාව පමණි.","සංඛ්‍යාතය පමණි.","සංඛ්‍යාතය සහ කලාව පමණි."])
add("Consider the following statements:\nA - A hub connects only the networked computers but a switch connects multiple devices.\nB - A switch manages the ports and the VLAN security settings.\nC - In data transmission, a hub uses bits while a switch uses frames and packets.\nD - The data transmission speed in a hub is higher than that in a switch.\nWhich of the above statements are correct?",None,O5,S5)
add("Consider the following statements about the proxy server:\nA - It helps to hide the true IP address.\nB - It is used to restrict the access of the website in the network.\nC - It uses the cached data for the quick loading of regularly accessed websites.\nD - It helps to detect the locations of the visitors and load web pages as per their needs.\nWhich of the above statements are correct?",None,O5,S5)
add("Which of the following statements regarding guided and unguided media are correct?\nA - Guided media transmission supports higher data speeds than unguided media transmission.\nB - Guided media is subjected to less interference than unguided media.\nC - Unguided media transmission is more secure than guided media transmission.\nD - Unguided media transmission uses low bandwidth than guided media transmission.",None,O5,S5)
add("What is the process carried-out in the modulation technique in data transmission?",None,
["encoding information in transmitted signal.","encoding signals in transmitted information.","extracting information from the transmitted signal.","extracting signal from the transmitted information.","transfer information with minimum distortion."],
["සම්ප්‍රේෂණය කරන ලද සංඥාවෙහි තොරතුරු කේතනය කිරීම.","සම්ප්‍රේෂණය කරන ලද තොරතුරුවල සංඥා කේතනය කිරීම.","සම්ප්‍රේෂණය කරන ලද සංඥාවෙන් තොරතුරු ලබාගැනීම.","සම්ප්‍රේෂණය කරන ලද තොරතුරුවලින් සංඥාව ලබාගැනීම.","අවම විකෘතියක් සහිතව තොරතුරු හුවමාරු කිරීම."])
add("Which of the following statements about bus topology are incorrect?\nA - Computers and network devices are connected to a single cable.\nB - All traffic flows are either clockwise or anticlockwise.\nC - Bandwidth is shared among the nodes.\nD - Each node is connected to two of its neighbors.",None,
["A and B only.","A and D only.","B and C only.","B and D only.","C and D only."],["A හා B පමණි.","A හා D පමණි.","B හා C පමණි.","B හා D පමණි.","C හා D පමණි."])
add("Consider the following statement with a blank.\nA Media Access Control (MAC) address is usually represented in ....................... numbers.\nWhich of the following is suitable to fill the blank?",None,
["binary","decimal","hexadecimal","natural","octal"],["ද්විමය","දශම","ෂඩ් දශම","ස්වභාවික","අෂ්ටක"])
add("You are requested to create 16 subnets with a Class C IP. Which subnet mask is suited to create the subnet?",None,
["255.255.255.240","255.255.255.248","255.255.255.250","255.255.255.252","255.255.255.224"])
add("Which of the following could be used to digitally represent analog signals?",None,
["attenuation","decoding","distortion","pulse code modulation","synchronization"],["වැහැරීම","විකේතනය","විකෘතිය","ස්පන්දන කේත මූර්ජනය","සමමුහූර්තකරණය"])
add("Which of the following is/are correct with respect to a digital signal?\nA - denoted by a square wave.\nB - contains a continuous range of values.\nC - uses discrete values to represent information.",None,
["A only.","B only.","C only.","A and B only.","A and C only"],["A පමණි.","B පමණි.","C පමණි.","A හා B පමණි.","A හා C පමණි"])
add("Which of the following is/are correct with respect to guided media used for data transmission?\nA - a physical path is used for data transmission.\nB - signal is broadcast through air.\nC - Example: radio waves",None,
["A only.","A and B only.","A and C only.","B and C only.","All of the above"],["A පමණි.","A හා B පමණි.","A හා C පමණි.","B හා C පමණි.","ඉහත සියල්ලම."])
add("Read the following sentence.\nWhen devices send and receive data over a network, a protocol is used uniquely identify the sender interface and the correct delivery of the data to the receiver's interface.\nWhat is the protocol that the writer in above sentence is referring to?",None,
["FTP","HTTP","MAC","TCP","UDP"])
add("Given below are some characteristics of Transmission Control Protocol (TCP) and User Datagram Protocol (UDP).\nA - best suited for applications that need high reliability and where the transmission time is less critical.\nB - faster and requires fewer resources.\nC - guarantees that no packets are missing.\nD - packets may not arrive in order.\nE - used for voice communications over internet.\nWhich of the above are the characteristics of UDP?",None,
["A, B and C only.","A, C and E only.","A, D and E only.","B, C and D only.","B, D and E only."],["A, B හා C පමණි.","A, C හා E පමණි.","A, D හා E පමණි.","B, C හා D පමණි.","B, D හා E පමණි."])
add("Which of the following is/are examples for the use of Client-Server model?\nA - A user printing a document using a printer connected to her computer.\nB - A bank customer accessing online banking services with a web browser.\nC - A cashier of a shop that accepts payments by credit cards.",None,
["A only","B only","C only","A and C only","B and C only"],["A පමණි","B පමණි","C පමණි","A හා C පමණි","B හා C පමණි"])
assert len(R)==37,len(R)
# fix Q8 english text
R[7]['q']="The transport layer protocol User Datagram Protocol (UDP) can be used for ............................... . Which of the following is the most suitable to fill the blank in the above statement?"
out=[]
for r,i in zip(R,s):
    o={"n":i['n'],"d":i['d'],"q":r['q']}
    if r['qs']: o['qs']=r['qs']
    o['o']=r['o']
    if r['os']:
        assert len(r['os'])==len(r['o']); o['os']=r['os']
    assert 4<=len(o['o'])<=5 and all(o['o'])
    out.append(o)
json.dump(out,open('D:/DevOps/aws-clf-c02-bridge/tools/transcribed/ictl-net-mcq.part2.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(out))
