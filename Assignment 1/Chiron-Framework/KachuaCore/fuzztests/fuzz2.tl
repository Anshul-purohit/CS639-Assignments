pendown
if :x>100[
    if :y>50[
        forward 100
    ]
    else[
        left 90
        forward 100
    ]
]
else [
    if :y<10[
        right 90
        forward 100
    ]
    else[
        left 180
        forward 100
    ]
]