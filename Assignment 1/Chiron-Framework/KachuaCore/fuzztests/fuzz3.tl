if :x>100[
    if :y>100[
        if :z>100[
            pendown
            forward 100
        ]
        else[
            pendown
            right 90
            forward 100
        ]
    ]
    else[
        penup
        forward 100
        right 90
        pendown
        forward 100
    ]
]
else[
    if :x>50[
        penup
        right 90
        forward 100
        left 90
        pendown 
        forward 100
    ]
]