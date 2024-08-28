Test case directory:

assignment_1_231110007\Chiron-Framework\KachuaCore\fuzztests



Test case output directory:

assignment_1_231110007\Chiron-Framework\KachuaCore\fuzztests\outputs


Commands to follow for different test cases:

fuzz1.tl : ./kachua.py -t 60 --fuzz fuzztests/fuzz1.tl -d '{":x": 5, ":y": 100}'

fuzz2.tl : ./kachua.py -t 60 --fuzz fuzztests/fuzz1.tl -d '{":x": 50, ":y": 100}' 

fuzz3.tl : ./kachua.py -t 60 --fuzz fuzztests/fuzz1.tl -d '{":x": 50, ":y": 100, ":z":150}' 

fuzz4.tl : ./kachua.py -t 60 --fuzz fuzztests/fuzz1.tl -d '{":x": 150, ":y": 100}' 

fuzz5.tl : ./kachua.py -t 60 --fuzz fuzztests/fuzz1.tl -d '{":a": 10, ":b": 20, ":c":30, ":d":40}' 

