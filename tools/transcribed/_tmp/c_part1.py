import json
d=json.load(open('tools/ict-lessons-images.json',encoding='utf8'))
s=[x for x in d['sets'] if x['id']=='ictl-net-mcq'][0]['qs'][:37]
T={}
def t(i,q=None,qs=None,o=None,os=None):
    T[i]=(q,qs,o,os)
t(1,"The abbreviation GSM stands for,","GSM කෙටි යෙදුම භාවිත වන්නේ,")
t(2,'The main role of a "router" in computer network is,',"පරිගණක ජාලයක රවුටරයක ප්‍රධාන කාර්යභාරය වන්නේ,",None,
 ["ජාලයේ සියලු ම සත්කාරකයින්ට දත්ත මල්ලු විකාශය කිරීමයි.","අහිතකර ක්‍රියාකාරකම් පිළිබඳව ජාලය නියාමනය කිරීමයි.","ලැබූ සංඥා ඉහළ බලයකින් ප්‍රතිසම්ප්‍රේෂණය කිරීමයි.","ජාල දෙකක සත්කාරකයින්ට සන්නිවේදනය සඳහා ඉඩ ලබාදීමයි.","වෙන් වූ විවිධ ජාල අතර භාරය සංතුලනය කර ගැනීමට ඉඩ සැලසීමයි."])
t(3,"A command that can be used to check network connectivity to a computer is,","පරිගණකයකට ජාල සම්බන්ධතාව ඇත්දැයි පිරික්සීමට යොදාගත හැකි විධානයක් වනුයේ,")
t(4,"What is the main function of a DHCP server?","DHCP සේවාදායක පරිගණකයක ප්‍රධාන කාර්යය කුමක් ද?",None,
 ["IP ලිපින ලබා දීම.","IP ලිපිනවලින් වසම් නාම ලබා දීම.","පරිශීලකයන්ට නාමාවලි සේවා සැපයීම.","පරිශීලකයින් අතර අන්තර්ජාල සම්බන්ධතාවක් හවුලේ බුක්ති විඳීමට සැලසීම.","වයිරස් ප්‍රහාරවලින් පරිගණක ජාලයක් ආරක්ෂා කිරීම."])
t(5,"Consider the IP address 192.248.87.3 and the subnet mask 255.255.255.224. How many hosts can be directly connected to this network?","192.248.87.3 යන IP ලිපිනය හා 255.255.255.224 අනුජාල වසන්ගය සලකන්න. මෙම ජාලයට සත්කාරකයින් කී දෙනකු සෘජුවම සම්බන්ධ කළ හැකි ද?")
t(6,"What is the most suitable media to transmit a high definition video over a distance of 5 km?","5km දුරක් ආවරණය වන පරිදි ඉහළ විභේදන වීඩියෝවක් සම්ප්‍රේෂණය කිරීම සඳහා වඩාත් සුදුසු මාධ්‍ය කුමක් ද?",None,
 ["රේඩියෝ තරංග","ඇඹර් යුගල තඹ කේබල","ප්‍රකාශ තන්තු කේබල","ඒකාක්ෂ කේබල","විවෘත වයර් කේබල"])
t(7,"The transport layer of the OSI reference model provides,","OSI නිර්දේශ ආකෘතියේ ප්‍රවාහන තලය මගින් සපයනු ලබන්නේ,",None,
 ["දෝෂ නිවැරදි කිරීමයි.","දත්ත මල්ලු මාර්ගගත කිරීමයි.","ගැලීම් පාලනයයි.","ක්‍රියාවලි-සිට-ක්‍රියාවලි සන්නිවේදනයයි.","දෝෂ අනාවරණයයි."])
t(8,"In computer networks, acronym DHCP stands for,","පරිගණක ජාලවල DHCP හැකුළුමෙන් අදහස් වන්නේ,")
t(9,"What is the function of a DNS in a Computer Network?","පරිගණක ජාලයක DNS හි කාර්යය කුමක් ද?",None,
 ["IP ලිපින පවරා දෙයි.","වසම් නාම, IP ලිපින බවට පරිවර්තනය කරයි.","ජාලය වයිරසවලින් ආරක්ෂා කරයි.","පරිශීලකයන්ට නාමාවලි සේවා සපයයි.","පරිගණක ජාල කිහිපයක් එකිනෙකට සම්බන්ධ කරයි."])
t(10,"The command that can be used to check the network configuration of a computer is,","පරිගණකයක ජාල වින්‍යාසය පරීක්ෂා කිරීම සඳහා යොදාගත හැකි විධානය වනුයේ,")
t(11,"Which of the following statements is correct about IP addresses and subnet masks?","IP ලිපින සහ අනුජාල ආවරණ පිළිබඳව පහත දක්වෙන කවර ප්‍රකාශය නිවැරදි වේ ද?",
 ["192.248.32.3 is a Class B IP address.","A network with a subnet mask 255.255.255.248 can accommodate six hosts.","An IP address consists of 16 bits.","10.32.1.5 is a Class C IP address.","255.255.255.0 is a Class C IP address."],
 ["192.248.32.3 යනු B පන්තියේ IP ලිපිනයකි.","255.255.255.248 අනුජාල ආවරණයක් සහිත ජාලයකට සත්කාරකයින් හයදෙනකුට පහසුකම් සැලසිය හැකි ය.","IP ලිපිනයක් ද්වයමය 16 කින් සමන්විත වේ.","10.32.1.5 යනු C පන්තියේ IP ලිපිනයකි.","255.255.255.0 යනු C පන්තියේ IP ලිපිනයකි."])
t(12,"The network layer of the OSI reference model provides,","OSI යොමු ආදර්ශයේ ජාල ස්තරය,",None,
 ["වැරදි නිවැරදිකිරීම් සිදු කරයි.","අන්තර්-ක්‍රියාවලි සන්නිවේදනය සිදු කරයි.","ගැලීම් පාලනය සිදු කරයි.","දත්ත පැකැට්ටු මාර්ගගත කිරීම සිදු කරයි.","දෝෂ අනාවරණය සිදු කරයි."])
t(13,"Which of the following is most cost effective and secure in transmitting private and confidential messages and notices among the employees of an organization?","සංවිධානයක සේවකයින් අතර පෞද්ගලික සහ රහසිගත පණිවිඩ හා දැන්වීම් සම්ප්‍රේෂණය සඳහා වඩාත් පිරිමැසුම්දායක හා ආරක්ෂිත වන්නේ පහත දක්වෙන කවර ක්‍රමය ද?",None,
 ["ඉලෙක්ට්‍රොනික දැන්වීම් පුවරු","ටෙලි සම්මන්ත්‍රණ පැවැත්වීම","විද්‍යුත් තැපෑල","සමාජ ජාලයක්","වෙබ් අඩවියක්"])
t(14,'"Video conferencing is best described as a/an ............................ discussion through ........................... between two or more individuals in different locations."\nWhich of the following is the most appropriate answer to fill the blanks in the above statement?',
 '"වීඩියෝ සම්මන්ත්‍රණ පැවැත්වීම යන්න, විවිධ ස්ථානවල සිටින දෙදෙනකු හෝ කිහිපදෙනකු අතර ............................ හරහා සිදුවන ........................... සාකච්ඡාවක් ලෙස වඩාත් හොඳින් විස්තර කෙරේ."\nඉහත ප්‍රකාශයෙහි හිස්තැන පිරවීම සඳහා වඩාත් සුදුසු පිළිතුරු වන්නේ පහත දක්වෙන කවර පද යුගලය ද?',None,
 ["රූපවාහිනියක්, වීඩියෝ","දුරකථනයක්, ශ්‍රව්‍ය","ජාලයක්, ශ්‍රව්‍ය","රූපවාහිනියක්, ශ්‍රව්‍යදෘශ්‍ය","ජාලයක්, ශ්‍රව්‍යදෘශ්‍ය"])
t(15,"What is the main function of a PROXY server in Internet communication?","අන්තර්ජාල සන්නිවේදනයේ දී නියෝජන සේවාදායකයක ප්‍රධාන කාර්යය වන්නේ කුමක් ද?",None,
 ["IP ලිපින පවරාගෙන මුදා හැරීම","වසම් නාම IP ලිපිනවලට පරිවර්තනය කිරීම","ජාලය වයිරස්වලින් ආරක්ෂා කර ගැනීම","පරිශීලකයන්ට මුද්‍රණ සේවා සැපයීම","පරිගණක කිහිපයක් අතර අන්තර්ජාල සම්බන්ධතාවක් හවුලේ භාවිත කිරීම"])
t(16,"An organization has been allocated a Class C IP address range having a subnet mask of 255.255.255.0. If the organization is to setup a web server and an email server, what are the IP addresses that can be allocated to these two servers?","ආයතනයකට 255.255.255.0 ලෙස ඇති උප ජාල ආවරණයක් සහිත C පන්තියේ IP ලිපින පරාසයක් වෙන් කර ඇත. මෙම ආයතනය වෙබ් සේවාදායකයක් හා විද්‍යුත් තැපැල් සේවාදායකයක් ස්ථාපිත කර ගත යුතු නම්, මෙම සේවාදායක දෙක සඳහා වෙන් කළ හැකි ලිපින මොනවා ද?")
t(17,"In communication networks, ISDN stands for,","සන්නිවේදන ජාලවල දී ISDN මගින් දැක්වෙන්නේ,")
t(18,"In the OSI reference model, detection of errors during communication between two computers in a network is a function of the .....................................","OSI සම්ප්‍රදේශ ආකෘතියේ දී ජාලයක් ඇති පරිගණක දෙකක් අතර සන්නිවේදනයේ දී ඇතිවන වැරදි සොයා ගැනුම ..................................... කාර්යයක් වන්නේ ය. ඉහත හිස්තැන පිරවීමට වඩාත් ම යෝග්‍ය පිළිතුර කුමක් ද?",None,
 ["භෞතික ස්තරයේහි","දත්ත සම්බන්ධන ස්තරයේහි","ජාල ස්තරයේහි","ප්‍රවාහන ස්තරයේහි","යෙදුම් ස්තරයේහි"])
t(19,"The command that can be used to login to a remote computer through a network is?","ජාලයක් හරහා දුරස්ථ පරිගණකයකට පිවිසීමට යාමේ දී භාවිත කළ යුතු විධානය වන්නේ කුමක් ද?")
t(20,"Which of the following devices can be used to connect two physical networks having IP addresses 72.110.0.0 (subnet mask: 255.255.0.0) and 192.248.10.0 (subnet mask 255.255.255.0)?","IP ලිපින 72.110.0.0 (උප ජාල ආවරණය 255.255.0.0) සහ 192.248.10.0 (උප ජාල ආවරණය 255.255.255.0) ලෙස ඇති භෞතික ජාල දෙකක් සම්බන්ධ කිරීමට යොදා ගත හැක්කේ පහත දක්වා ඇති කවර උපක්‍රමය ද?",None,
 ["නාභිය","රීපීටරය","ස්විචය","මංහසුරුව","බහුපථකාරකය"])
t(21,"Which of the following converts digital data to analog data to transmit over an analog telephone network?","ප්‍රතිසම දුරකථන ජාලයක් හරහා සම්ප්‍රේෂණය කිරීම සඳහා ඩිජිටල් දත්ත, ප්‍රතිසම දත්තවලට පරිවර්තනය කරන්නේ පහත සඳහන් කුමකින් ද?",None,
 ["ජාල අතුරු මුහුණත","මොඩමය","බහු පථ කාරක","බ්ලූටූත් අනුවර්තකය","Wi-Fi කාඩ්පත"])
t(22,"Computers attached to a LAN use the default gateway connected to the same network .................................","ස්ථානීය පෙදෙස් ජාලයකට සම්බන්ධිත පරිගණක එම ජාලයට සම්බන්ධ කර ඇති පුරුදු ද්වාරය භාවිත කරනු ලබන්නේ .................................",None,
 ["වසම් නාම IP ලිපිනවලට පරිවර්තනය කිරීමට ය.","ගමනාන්තයට විශේෂිත වූ මාර්ගයක් නොදන්නා විට IP පැකැට්ටුව ඉදිරියට යැවීම සඳහා ය.","ජාලය සඳහා වූ ගිනි පවුර ලෙස ය.","මෙම ජාලය වූ අනෙකුත් පරිගණක සියලු දත්ත පැකැට්ටු යැවීම සඳහා ය.","LAN එක තුළ වූ පරිගණකයක් IP ලිපිනයක් දීමට ය."])
t(23,"The command that can be used to measure the round trip propagation delay between two computers on the Internet is,","අන්තර්ජාලයට සම්බන්ධ පරිගණක දෙකක් අතර පවතින වටරවුම් චාරිකා ප්‍රචාරණ ප්‍රමාදය මැන ගැනීම සඳහා භාවිත වන විධානය වන්නේ,")
t(24,"In the OSI seven layer reference model, IP protocol maps to the ...................................... layer.\nWhich of the following is most appropriate to fill the blank in the above statement?","OSI ස්තර සප්ත සම්ප්‍රදේශ ආකෘතිය තුළ දී IP නියමාවලිය අනුරූපණය වන්නේ ...................................... ස්තරයට ය.\nඉහත හිස්තැන පිරවීමට වඩාත් ම යෝග්‍ය පිළිතුර වන්නේ පහත සඳහන් කවර ද?",None,
 ["යෙදුම්","සැසි","ප්‍රවාහන","ජාල","භෞතික"])
t(25,"The function of the DHCP server in an IP network is to .................................","IP ජාලයක් තුළ DHCP සේවාදායකයේ කාර්යය වනුයේ .................................",None,
 ["වසම් නාම IP ලිපිනවලට පරිවර්තනය කිරීම ය.","වෙබ් පිටු නිහිත කිරීම ය.","IP ලිපින ගතිකව පවරා දීම ය.","IP පැකැට්ටු පෙරීම ය.","ආරක්ෂාව ලබා දීම ය."])
for i in (26,27):
    t(i,"Which of the following is a valid subnet mask?","පහත සඳහන් දෑ අතරෙන් වලංගු උපජාල ආවරණයක් වන්නේ කවරක් ද?")
t(28,"The ping command indicates that there is a 5% packet loss between the computers X and Y. There is an FTP server running on Y. A file is downloaded to X from Y using FTP protocol. Which of the following is the most appropriate statement regarding this file download?","X හා Y පරිගණක අතර 5% ක පැකැට් හානියක් සිදුව ඇති බව ping විධානය මගින් දැක්වේ. Y පරිගණකයේ FTP සේවාදායකයක් ක්‍රියාත්මක වෙමින් පවතී. FTP නියමාවලිය භාවිතා කරමින් Y පරිගණකයේ සිට X වෙත ගොනුවක් බාගත කරන ලදී. පහත සඳහන් වගන්ති අතුරෙන් මෙම ගොනු බාගත කිරීම පිළිබඳව වඩාත් ම සුදුසු වගන්තිය කුමක් ද?",None,
 ["බාගත් ගොනුවේ හරියටම 5% ක් දත්ත හිලිහී ගොස් ඇත.","බාගත් ගොනුවේ 5% කට වඩා දත්ත හිලිහී ගොස් ඇත.","බාගත් ගොනුවේ හරියටම 5% ක ප්‍රමාණයක් දත්ත මුල් ගොනුවට වඩා වෙනස් වූ අනුපිළිවෙලකට පවතී.","බාගත් ගොනුවේ දත්ත මුල් ගොනුවේ දත්ත සමග හරියටම එකම අනුපිළිවෙලකට පවතී.","දෝෂ සහිත ජාල සම්බන්ධතාවයක FTP නියමාවලිය ධාවනය කළ නොහැක ය."])
t(29,"....................................... is used for analog signal to digital signal conversion.\nWhich of the following is most appropriate to fill the blank in the above statement?","ප්‍රතිසම සංඥාවක් ඩිජිටල් සංඥාවක් බවට පරිවර්තනය කිරීමට ....................................... භාවිත කරනු ලැබේ. ඉහත වගන්තියේ හිස්තැන පිරවීමට වඩාත් ම යෝග්‍ය පිළිතුර පහත සඳහන් කවර ද?",None,
 ["විස්තාර මූර්ජනය","සංඛ්‍යාත මූර්ජනය","ස්පන්දිත කේත මූර්ජනය","කලා මූර්ජනය","කාල බෙදුම් මූර්ජනය"])
t(30,"A computer in a network is configured with the IP address 192.248.16.91 and the subnet mask 255.255.255.128. Which of the following IP addresses cannot be assigned to a computer in the same network?","ජාලයක පවතින පරිගණකයක් 192.248.16.91 යන IP ලිපිනය සහ 255.255.255.128 යන උපජාල ආවරණය මගින් වින්‍යාසගත කර ඇත. මෙම ජාලයේ පවතින පරිගණකයක් සඳහා ලබාදිය නොහැක්කේ පහත දැක්වෙන කවර IP ලිපිනයක් ද?")
t(31,"Which of the following statements is correct with respect to the Transmission Control Protocol (TCP)?","සම්ප්‍රේෂණ පාලන නියමාවලිය සම්බන්ධයෙන් පහත වගන්ති අතුරෙන් නිවැරදි වන්නේ කුමක් ද?",None,
 ["TCP යනු ජාල ස්තර නියමාවලියකි.","යවනු ලබන සෑම බයිටයක්ම ග්‍රාහකයා වෙත ලැබීම TCP මගින් සහතික කරයි.","එක් පරිගණකයක් තුළ TCP භාවිතා කළ හැක්කේ එක් වරකට එක් යෙදුමකට පමණි.","HTTP, TCP භාවිත කරයි.","TCP විසින් ප්‍රවාහන නියමාවලිය ලෙස User Datagram නියමාවලිය (UDP) භාවිත කරනු ලබයි."])
t(32,"A LAN uses the subnet mask 255.255.240.0. How many different IP addresses can be assigned to devices in this LAN?","ස්ථානීය පෙදෙස් ජාලයක් 255.255.240.0 යන උපජාල ආවරණය භාවිත කරයි. මෙම ජාලයේ පවතින උපක්‍රම සඳහා භාවිත කළ හැකි එකිනෙකට වෙනස් IP ලිපින කොපමණ සංඛ්‍යාවක් පවතින්නේ ද?")
t(33,"Which of the following statements is correct with respect to routing in the Internet?","අන්තර්ජාලයේ මංහසුරැවීම සම්බන්ධයෙන් නිවැරදි වන්නේ පහත වගන්ති අතුරෙන් කවරක් ද?",None,
 ["දෙන ලද ඕනෑම LAN එකක උපරිම වශයෙන් පැවතිය හැක්කේ එක් මංහසුරුවකි.","එක් මංහසුරුවකට ජාල අතුරු මුහුණත් එකකට වඩා පැවතිය හැකි ය.","මංහසුරැවීම ප්‍රවාහන ස්ථරයේ එක් කාර්යයකි.","සියලු මංහසුරු HTTP proxies ලෙස ක්‍රියා කරයි.","සියලු යෙදුම් TCP භාවිතා කරයි නම් අන්තර්ජාලයට මංහසුරැවීම අවශ්‍ය නොවේ."])
t(34,"In a public key encryption system, the private key of a person x is given by the function priv(x) and the public key is given by pub(x). Consider the following statements:\nA - pub(x) is used to encrypt a message that can only be decrypted using priv(x).\nB - pub(x) is used to sign a message to be sent to x.\nC - A message encrypted using pub(x) can be decrypted using pub(x).\nWhich of the above statement(s) is/are correct?",
 "පොදු යතුර ගුප්ත කේතන පද්ධතියක x නම් පුද්ගලයකුගේ පෞද්ගලික යතුර priv(x) යන ශ්‍රිතයෙන් හා පොදු යතුර pub(x) යන ශ්‍රිතයෙන් ද දෙනු ලැබේ. පහත වගන්ති සලකා බලන්න:\nA - priv(x) භාවිත කිරීම මගින් පමණක් විකේතනය කළ හැකි සේ පණිවුඩයක් ගුප්ත කේතනය සඳහා pub(x) භාවිත කරයි.\nB - x වෙත යවන පණිවුඩයක් අත්සන් තැබීම සඳහා pub(x) භාවිත කරයි.\nC - pub(x) භාවිතයෙන් ගුප්ත කේතනය කරනු ලැබූ පණිවුඩයක් pub(x) භාවිතයෙන් විකේතනය කළ හැකි වේ.\nඉහත වගන්ති අතුරෙන් නිවැරදි වන්නේ,",
 ["A only","B only","C only","A and B only","B and C only"],["A පමණි","B පමණි","C පමණි","A හා B පමණි","B හා C පමණි"])
t(35,"Consider the following statements regarding a server with the domain name www.bogus.lk:\nA - The server www.bogus.lk can be located anywhere in the world.\nB - www.bogus.lk must be a web server.\nC - The domain names www.bogus.lk and www.bogus.com can be resolved to the same IP address.\nWhich of the above statement(s) is/are correct?",
 "www.bogus.lk වසමාමය සහිත සේවාදායකයක් පිළිබඳව පහත වගන්ති සලකා බලන්න:\nA - www.bogus.lk සේවාදායකය ලෝකයේ ඕනෑම තැනක ස්ථානගත වී තිබිය හැකි ය.\nB - www.bogus.lk වෙබ් සේවාදායකයක් ම විය යුතු ය.\nC - www.bogus.lk සහ www.bogus.com යන වසම්නාම එකම IP ලිපිනයකට හා බැඳී පැවතිය හැකි ය.\nඉහත වගන්ති අතුරෙන් නිවැරදි වන්නේ,",
 ["A only","B only","C only","A and B only","A and C only"],["A පමණි","B පමණි","C පමණි","A හා B පමණි","A හා C පමණි"])
t(36,"A file of 1 MB has been successfully sent from the machine X to machine Y in a network over a TCP connection. It has been observed that the 10th byte of the file has passed through the router R. Consider the following statements regarding this communication:\nA - The 10,000th byte must have gone through the router R after the 10th byte.\nB - The 10,000th byte must have gone through the same path from X to Y as the 10th byte.\nC - The 10,000th byte may or may not have gone through the router R.\nWhich of the above statement(s) is/are correct?",
 "ජාලයක X නම් යන්ත්‍රයක සිට Y වෙත TCP සම්බන්ධතාවක් හරහා 1MB වූ ගොනුවක් සාර්ථකව යවන ලදී. මෙම ගොනුවේ 10 වැනි බයිටය R නම් මංහසුරුව තුළින් ගමන් කර ඇති බව නිරීක්ෂණය විය. මෙම සන්නිවේදනය සම්බන්ධයෙන් පහත දී ඇති වගන්ති සලකා බලන්න:\nA - 10 වැනි බයිටයට පසු 10,000 වැනි බයිටය ද, R නම් මංහසුරුව තුළින් ගමන් කර තිබිය යුතු ය.\nB - 10,000 වැනි බයිටය ද X සිට Y දක්වා 10 වැනි බයිටය ගමන් ගත් මාර්ගයේ ම ගමන් කර තිබිය යුතු ය.\nC - 10,000 වැනි බයිටය R නම් මංහසුරුව තුළින් ගමන් කර හෝ ගමන් නොකර හෝ තිබිය හැකි ය.\nඉහත සඳහන් කුමන වගන්තිය/වගන්ති නිවැරදි වන්නේ ද?",
 ["A only","B only","C only","A and B only","B and C only"],["A පමණි","B පමණි","C පමණි","A හා B පමණි","B හා C පමණි"])
t(37,'"An analog signal is sampled at regular intervals and represented as 16 bit values."\nWhich of the followings is best described by the above statement?','"ප්‍රතිසම සංඥාවක් නියත කාලාන්තරවල දී නියැදි කර බිටු 16 හි අගයන් ලෙස නිරූපණය කරනු ලැබේ."\nඉහත වගන්තියෙන් හොඳින් විස්තර කරනු ලබන්නේ පහත සඳහන් කුමකින් ද?',None,
 ["විස්තාර මූර්ජනය","සංඛ්‍යාත මූර්ජනය","ස්පන්දිත කේත මූර්ජනය","කලා මූර්ජනය","ස්පන්ද විතර මූර්ජනය"])
FIX={4:["Allocating IP addresses.","Resolving domain names from IP addresses.","Providing directory services to users.","Sharing an Internet connection among users.","Protecting a computer network from virus attacks."],
9:["Assigns IP addresses","Translates domain names to IP addresses","Protects a network from viruses","Provides directory services to users","Connects multiple computer networks together"],
15:["Allocate and release IP addresses","Translate domain names to IP addresses","Protect a network from viruses","Provide printing services to users","Share an Internet connection among several computers"],
22:["to translate the domain names to IP addresses.","to forward IP packets when they do not know any specific route to the destination.","as the firewall for the network.","to send all the data packets to other computers in the same LAN.","to assign IP address to a computer on the LAN."],
25:["translate domain names to IP addresses","cache the web pages","dynamically allocate IP addresses","filter IP packets","provide security"],
28:["The downloaded file has exactly 5% of the data missing.","The downloaded file has more than 5% of the data missing.","The downloaded file has 5% of data in a different order than the original file.","The downloaded file has the data in exactly the same order as the original file.","FTP protocol cannot run on a network connection with errors."],
31:["TCP is a network layer protocol.","TCP guarantees that each byte sent is received at the receiver.","Only one application at a time can use TCP in a computer.","HTTP uses TCP.","TCP uses User Datagram Protocol (UDP) as the transport protocol."],
33:["There can be at most one router in any given LAN.","A router can have more than one network interface.","Routing is a functionality of the Transport Layer.","All routers function as HTTP proxies.","The Internet does not need routing if all applications use TCP."],
21:["Network Interface Card (NIC)","Modem","Multiplexer","Bluetooth adaptor","Wi-Fi card"],
12:None}
FIX={k:v for k,v in FIX.items() if v}
out=[]
for i,q in enumerate(s,1):
    if i in FIX: q=dict(q); q['o']=FIX[i]
    q_,qs,o,os_=T[i]
    ob={"n":q['n'],"d":q['d'],"q":q_,"qs":qs,"o":o or q['o']}
    if os_:
        ob["os"]=os_
    assert 4<=len(ob['o'])<=5 and all(ob['o']), i
    if os_:
        assert len(os_)==len(ob['o']),i
    out.append(ob)
assert len(out)==37
json.dump(out,open('tools/transcribed/ictl-net-mcq.part1.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
print(len(out))
