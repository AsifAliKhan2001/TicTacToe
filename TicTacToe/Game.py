import turtle

# hide the turtle
turtle.ht()

# style for turtle text
style = ('Arial', 30)

# draw a tic tac toe board
def drawboard():
    turtle.speed(0)
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(-150,50)
    turtle.setheading(0)
    turtle.pendown()
    turtle.speed(0)
    turtle.forward(300)

    turtle.speed(0)
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(-150,-50)
    turtle.setheading(0)
    turtle.pendown()
    turtle.speed(0)
    turtle.forward(300)

    turtle.speed(0)
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(50,-150)
    turtle.setheading(90)
    turtle.pendown()
    turtle.speed(0)
    turtle.forward(300)

    turtle.speed(0)
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(-50,150)
    turtle.setheading(270)
    turtle.pendown()
    turtle.speed(0)
    turtle.forward(300)

# draw an X
def drawx():
    temp = turtle.position()
    turtle.goto(temp[0] + 40, temp[1] + 40)
    turtle.pendown()
    turtle.goto(temp[0] - 40, temp[1] - 40)
    turtle.penup()
    turtle.goto(temp[0] + 40, temp[1] - 40)
    turtle.pendown()
    turtle.goto(temp[0] - 40, temp[1] + 40)
    turtle.penup()

# draw an O
def drawo():
    turtle.penup()
    turtle.goto(turtle.xcor() - 40, turtle.ycor())
    turtle.pendown()
    turtle.circle(40)

# keep track of if the game is over and if a player won, who won (or if its a tie)
def isgameover():
    # if xwins is None, game is not over. if xwins is 'tie', game is a tie. if xwins is True, x wins. if xwins is False, o wins
    xwins = None
    # each of these if statements represents a win state
    if positions[0] != '' and positions[0] == positions[1] and positions[0] == positions[2]:
        if positions[0] == 'x':
            xwins = True
        else:
            xwins = False
    elif positions[3] != '' and positions[3] == positions[4] and positions[3] == positions[5]:
        if positions[3] == 'x':
            xwins = True
        else:
            xwins = False
    elif positions[6] != '' and positions[6] == positions[7] and positions[6] == positions[8]:
        if positions[6] == 'x':
            xwins = True
        else:
            xwins = False
    elif positions[0] != '' and positions[0] == positions[3] and positions[0] == positions[6]:
        if positions[0] == 'x':
            xwins = True
        else:
            xwins = False
    elif positions[1] != '' and positions[1] == positions[4] and positions[1] == positions[7]:
        if positions[1] == 'x':
            xwins = True
        else:
            xwins = False
    elif positions[2] != '' and positions[2] == positions[5] and positions[2] == positions[8]:
        if positions[2] == 'x':
            xwins = True
        else:
            xwins = False
    elif positions[0] != '' and positions[0] == positions[4] and positions[0] == positions[8]:
        if positions[0] == 'x':
            xwins = True
        else:
            xwins = False
    elif positions[2] != '' and positions[2] == positions[4] and positions[2] == positions[6]:
        if positions[2] == 'x':
            xwins = True
        else:
            xwins = False
    # the tie option
    elif '' not in positions:
        xwins = 'tie'
    
    return xwins

# if x wins
def x_is_winner():
    turtle.penup()
    turtle.goto(0,190)
    turtle.write('X wins!',font = style, align = 'center')

    turtle.done()


# if o wins
def o_is_winner():
    turtle.penup()
    turtle.goto(0,190)
    turtle.write('O wins!',font = style, align = 'center')

    turtle.done()


# if it is a tie
def it_is_a_tie():
    turtle.penup()
    turtle.goto(0,190)
    turtle.write('It is a tie',font = style, align = 'center')

    turtle.done()

# keeps track of which player went where (9 elements, each corresponding to one of the 9 possible positions. they all start blank)
positions = ['','','','','','','','','']

# function variable to keep track of whose turn it is
switch = 'x'

# nine onkey functions. one for each position
def one():
    # to allow switch to be reassigned globally
    global switch
    # go to position one
    turtle.penup()
    turtle.goto(-100,-100)
    turtle.pendown()
    
    # make sure position one is not taken
    if positions[0] != '':
        pass
    # if x's turn, draw an x
    elif switch == 'x':
        drawx()
        # flip value of switch to assure next turn goes to o
        switch = 'o'
        # document position one was taken by x
        positions[0] = 'x'
    # if o's turn, draw an o
    else:
        drawo()
        # flip value of switch to assure next turn goes to x
        switch = 'x'
        # document position one was taken by o
        positions[0] = 'o'
    
    # check to see if game is over
    if isgameover() == 'tie':
        it_is_a_tie()
    elif type(isgameover()) == type(True):
        if isgameover():
            x_is_winner()
        else:
            o_is_winner()


def two():
    # to allow switch to be reassigned globally
    global switch
    # go to position two
    turtle.penup()
    turtle.goto(0,-100)
    turtle.pendown()
    
    # make sure position two is not taken
    if positions[1] != '':
        pass
    # if x's turn, draw an x
    elif switch == 'x':
        drawx()
        # flip value of switch to assure next turn goes to o
        switch = 'o'
        # document position two was taken by x
        positions[1] = 'x'
    # if o's turn, draw an o
    else:
        drawo()
        # flip value of switch to assure next turn goes to x
        switch = 'x'
        # document position two was taken by o
        positions[1] = 'o'
    
    # check to see if game is over
    if isgameover() == 'tie':
        it_is_a_tie()
    elif type(isgameover()) == type(True):
        if isgameover():
            x_is_winner()
        else:
            o_is_winner()


def three():
    # to allow switch to be reassigned globally
    global switch
    # go to position three
    turtle.penup()
    turtle.goto(100,-100)
    turtle.pendown()
    
    # make sure position three is not taken
    if positions[2] != '':
        pass
    # if x's turn, draw an x
    elif switch == 'x':
        drawx()
        # flip value of switch to assure next turn goes to o
        switch = 'o'
        # document position three was taken by x
        positions[2] = 'x'
    # if o's turn, draw an o
    else:
        drawo()
        # flip value of switch to assure next turn goes to x
        switch = 'x'
        # document position three was taken by o
        positions[2] = 'o'
    
    # check to see if game is over
    if isgameover() == 'tie':
        it_is_a_tie()
    elif type(isgameover()) == type(True):
        if isgameover():
            x_is_winner()
        else:
            o_is_winner()


def four():
    # to allow switch to be reassigned globally
    global switch
    # go to position four
    turtle.penup()
    turtle.goto(-100,0)
    turtle.pendown()
    
    # make sure position four is not taken
    if positions[3] != '':
        pass
    # if x's turn, draw an x
    elif switch == 'x':
        drawx()
        # flip value of switch to assure next turn goes to o
        switch = 'o'
        # document position four was taken by x
        positions[3] = 'x'
    # if o's turn, draw an o
    else:
        drawo()
        # flip value of switch to assure next turn goes to x
        switch = 'x'
        # document position four was taken by o
        positions[3] = 'o'
    
    # check to see if game is over
    if isgameover() == 'tie':
        it_is_a_tie()
    elif type(isgameover()) == type(True):
        if isgameover():
            x_is_winner()
        else:
            o_is_winner()


def five():
    # to allow switch to be reassigned globally
    global switch
    # go to position five
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    
    # make sure position five is not taken
    if positions[4] != '':
        pass
    # if x's turn, draw an x
    elif switch == 'x':
        drawx()
        # flip value of switch to assure next turn goes to o
        switch = 'o'
        # document position five was taken by x
        positions[4] = 'x'
    # if o's turn, draw an o
    else:
        drawo()
        # flip value of switch to assure next turn goes to x
        switch = 'x'
        # document position five was taken by o
        positions[4] = 'o'
    
    # check to see if game is over
    if isgameover() == 'tie':
        it_is_a_tie()
    elif type(isgameover()) == type(True):
        if isgameover():
            x_is_winner()
        else:
            o_is_winner()


def six():
    # to allow switch to be reassigned globally
    global switch
    # go to position six
    turtle.penup()
    turtle.goto(100,0)
    turtle.pendown()
    
    # make sure position six is not taken
    if positions[5] != '':
        pass
    # if x's turn, draw an x
    elif switch == 'x':
        drawx()
        # flip value of switch to assure next turn goes to o
        switch = 'o'
        # document position six was taken by x
        positions[5] = 'x'
    # if o's turn, draw an o
    else:
        drawo()
        # flip value of switch to assure next turn goes to x
        switch = 'x'
        # document position six was taken by o
        positions[5] = 'o'
    
    # check to see if game is over
    if isgameover() == 'tie':
        it_is_a_tie()
    elif type(isgameover()) == type(True):
        if isgameover():
            x_is_winner()
        else:
            o_is_winner()


def seven():
    # to allow switch to be reassigned globally
    global switch
    # go to position seven
    turtle.penup()
    turtle.goto(-100,100)
    turtle.pendown()
    
    # make sure position seven is not taken
    if positions[6] != '':
        pass
    # if x's turn, draw an x
    elif switch == 'x':
        drawx()
        # flip value of switch to assure next turn goes to o
        switch = 'o'
        # document position seven was taken by x
        positions[6] = 'x'
    # if o's turn, draw an o
    else:
        drawo()
        # flip value of switch to assure next turn goes to x
        switch = 'x'
        # document position seven was taken by o
        positions[6] = 'o'
    
    # check to see if game is over
    if isgameover() == 'tie':
        it_is_a_tie()
    elif type(isgameover()) == type(True):
        if isgameover():
            x_is_winner()
        else:
            o_is_winner()


def eight():
    # to allow switch to be reassigned globally
    global switch
    # go to position eight
    turtle.penup()
    turtle.goto(0,100)
    turtle.pendown()
    
    # make sure position eight is not taken
    if positions[7] != '':
        pass
    # if x's turn, draw an x
    elif switch == 'x':
        drawx()
        # flip value of switch to assure next turn goes to o
        switch = 'o'
        # document position eight was taken by x
        positions[7] = 'x'
    # if o's turn, draw an o
    else:
        drawo()
        # flip value of switch to assure next turn goes to x
        switch = 'x'
        # document position eight was taken by o
        positions[7] = 'o'
    
    # check to see if game is over
    if isgameover() == 'tie':
        it_is_a_tie()
    elif type(isgameover()) == type(True):
        if isgameover():
            x_is_winner()
        else:
            o_is_winner()


def nine():
    # to allow switch to be reassigned globally
    global switch
    # go to position nine
    turtle.penup()
    turtle.goto(100,100)
    turtle.pendown()
    
    # make sure position nine is not taken
    if positions[8] != '':
        pass
    # if x's turn, draw an x
    elif switch == 'x':
        drawx()
        # flip value of switch to assure next turn goes to o
        switch = 'o'
        # document position nine was taken by x
        positions[8] = 'x'
    # if o's turn, draw an o
    else:
        drawo()
        # flip value of switch to assure next turn goes to x
        switch = 'x'
        # document position nine was taken by o
        positions[8] = 'o'
    
    # check to see if game is over
    if isgameover() == 'tie':
        it_is_a_tie()
    elif type(isgameover()) == type(True):
        if isgameover():
            x_is_winner()
        else:
            o_is_winner()

# draw the board
drawboard()

turtle.listen()
turtle.onkey(one,'1')
turtle.onkey(two,'2')
turtle.onkey(three,'3')
turtle.onkey(four, "4")
turtle.onkey(five, "5")
turtle.onkey(six, "6")
turtle.onkey(seven, "7")
turtle.onkey(eight, "8")
turtle.onkey(nine, "9")


# allows turtle to listen continually
turtle.mainloop()