pendown

if :x>50[
    if :y>100[
        right 90
        forward 100
    ]
    else[
        left 90
        forward 100
    ]
]
else[
    if :y<10[
        right 180
        forward 100
    ]
    else[
        left 180
        forward 100
    ]
]