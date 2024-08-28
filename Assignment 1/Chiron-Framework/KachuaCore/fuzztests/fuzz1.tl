pendown
if :x<10[
    if :x<4[
        forward 100
    ]
    else[
        right 60
        forward 100
    ]
]
else[
    penup
    forward 100
    right 120
    pendown
    forward 100
]