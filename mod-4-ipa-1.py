def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    accounts = social_graph
    if to_member in accounts[from_member]["following"] and from_member in accounts[to_member]["following"]:
        return print("friends")
    elif from_member in accounts[to_member]["following"]: 
        return print("followed by")
    elif to_member in accounts[from_member]["following"]:
        return print("follower")
    elif to_member not in accounts[from_member]["following"] and from_member not in accounts[to_member]["following"]:
        return print("no relationship")

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if len(board) == 3:
        if 3 in [x.count(board[0][0]) for x in board]:
            return board[0][0]
        elif 3 in [x.count(board[1][0]) for x in board]:
            return board[1][0]
        elif 3 in [x.count(board[2][0]) for x in board]:
            return board[2][0]
        elif 3 in [x.count(board[0][0]) for x in zip(*board)]:
            return board[0][0]
        elif 3 in [x.count(board[1][0]) for x in zip(*board)]:
            return board[1][0]
        elif 3 in [x.count(board[2][0]) for x in zip(*board)]:
            return board[2][0]
        elif sum([x.count(board[0][0]) for x in [board[i][i] for i,v in enumerate(board)]]) == 3:
            return board[0][0]
        elif sum([x.count(board[2][0]) for x in[board[2 - i][i] for i,v in enumerate(board)]]) == 3:
            return board[2][0]
        elif 3 not in [x.count(board[0][0]) for x in board]:
            return print("NO WINNER")
        elif 3 not in [x.count(board[1][0]) for x in board]:
            return print("NO WINNER")
        elif 3 not in [x.count(board[2][0]) for x in board]:
            return print("NO WINNER")
        elif 3 not in [x.count(board[0][0]) for x in zip(*board)]:
            return print("NO WINNER")
        elif 3 not in [x.count(board[1][0]) for x in zip(*board)]:
            return print("NO WINNER")
        elif 3 not in [x.count(board[2][0]) for x in zip(*board)]:
            return print("NO WINNER")
        elif sum([x.count(board[0][0]) for x in [board[i][i] for i,v in enumerate(board)]]) != 3:
            return print("NO WINNER")
        elif sum([x.count(board[2][0]) for x in[board[2 - i][i] for i,v in enumerate(board)]]) != 3:
            return print("NO WINNER")
    elif len(board) == 4: 
        if 4 in [x.count(board[0][0]) for x in board]:
            return board[0][0]
        elif 4 in [x.count(board[1][0]) for x in board]:
            return board[1][0]
        elif 4 in [x.count(board[2][0]) for x in board]:
            return board[2][0]
        elif 4 in [x.count(board[3][0]) for x in board]:
            return board[3][0]
        elif 4 in [x.count(board[0][0]) for x in zip(*board)]:
            return board[0][0]
        elif 4 in [x.count(board[1][0]) for x in zip(*board)]:
            return board[1][0]
        elif 4 in [x.count(board[2][0]) for x in zip(*board)]:
            return board[2][0]
        elif 4 in [x.count(board[3][0]) for x in zip(*board)]:
            return board[3][0]
        elif sum([x.count(board[0][0]) for x in [board[i][i] for i,v in enumerate(board)]]) == 4:
            return board[0][0]
        elif sum([x.count(board[3][0]) for x in[board[3 - i][i] for i,v in enumerate(board)]]) == 4:
            return board[3][0]
        elif 4 not in [x.count(board[0][0]) for x in board]:
            return print("NO WINNER")
        elif 4 not in [x.count(board[1][0]) for x in board]:
            return print("NO WINNER")
        elif 4 not in [x.count(board[2][0]) for x in board]:
            return print("NO WINNER")
        elif 4 not in [x.count(board[3][0]) for x in board]:
            return print("NO WINNER")
        elif 4 not in [x.count(board[0][0]) for x in zip(*board)]:
            return print("NO WINNER")
        elif 4 not in [x.count(board[1][0]) for x in zip(*board)]:
            return print("NO WINNER")
        elif 4 not in [x.count(board[2][0]) for x in zip(*board)]:
            return print("NO WINNER")
        elif 4 not in [x.count(board[3][0]) for x in zip(*board)]:
            return print("NO WINNER")
        elif sum([x.count(board[0][0]) for x in [board[i][i] for i,v in enumerate(board)]]) != 4:
            return print("NO WINNER")
        elif sum([x.count(board[3][0]) for x in[board[3 - i][i] for i,v in enumerate(board)]]) != 4:
            return print("NO WINNER")
    elif len(board) == 5: 
        if 5 in [x.count(board[0][0]) for x in board]:
            return board[0][0]
        elif 5 in [x.count(board[1][0]) for x in board]:
            return board[1][0]
        elif 5 in [x.count(board[2][0]) for x in board]:
            return board[2][0]
        elif 5 in [x.count(board[3][0]) for x in board]:
            return board[3][0]
        elif 5 in [x.count(board[4][0]) for x in board]:
            return board[4][0]
        elif 5 in [x.count(board[0][0]) for x in zip(*board)]:
            return board[0][0]
        elif 5 in [x.count(board[1][0]) for x in zip(*board)]:
            return board[1][0]
        elif 5 in [x.count(board[2][0]) for x in zip(*board)]:
            return board[2][0]
        elif 5 in [x.count(board[3][0]) for x in zip(*board)]:
            return board[3][0]
        elif 5 in [x.count(board[4][0]) for x in zip(*board)]:
            return board[4][0]
        elif sum([x.count(board[0][0]) for x in [board[i][i] for i,v in enumerate(board)]]) == 5:
            return board[0][0]
        elif sum([x.count(board[4][0]) for x in[board[4 - i][i] for i,v in enumerate(board)]]) == 5:
            return board[4][0]
        elif 5 not in [x.count(board[0][0]) for x in board]:
            return print("NO WINNER")
        elif 5 not in [x.count(board[1][0]) for x in board]:
            return print("NO WINNER")
        elif 5 not in [x.count(board[2][0]) for x in board]:
            return print("NO WINNER")
        elif 5 not in [x.count(board[3][0]) for x in board]:
            return print("NO WINNER")
        elif 5 not in [x.count(board[4][0]) for x in board]:
            return print("NO WINNER")
        elif 5 not in [x.count(board[0][0]) for x in zip(*board)]:
            return print("NO WINNER")
        elif 5 not in [x.count(board[1][0]) for x in zip(*board)]:
            return print("NO WINNER")
        elif 5 not in [x.count(board[2][0]) for x in zip(*board)]:
            return print("NO WINNER")
        elif 5 not in [x.count(board[3][0]) for x in zip(*board)]:
            return print("NO WINNER")
        elif 5 not in [x.count(board[4][0]) for x in zip(*board)]:
            return print("NO WINNER")
        elif sum([x.count(board[0][0]) for x in [board[i][i] for i,v in enumerate(board)]]) != 5:
            return print("NO WINNER")
        elif sum([x.count(board[4][0]) for x in[board[4 - i][i] for i,v in enumerate(board)]]) != 5:
            return print("NO WINNER")
    elif len(board) == 6: 
        if 6 in [x.count(board[0][0]) for x in board]:
            return board[0][0]
        elif 6 in [x.count(board[1][0]) for x in board]:
            return board[1][0]
        elif 6 in [x.count(board[2][0]) for x in board]:
            return board[2][0]
        elif 6 in [x.count(board[3][0]) for x in board]:
            return board[3][0]
        elif 6 in [x.count(board[4][0]) for x in board]:
            return board[4][0]
        elif 6 in [x.count(board[5][0]) for x in board]:
            return board[5][0]
        elif 6 in [x.count(board[0][0]) for x in zip(*board)]:
            return board[0][0]
        elif 6 in [x.count(board[1][0]) for x in zip(*board)]:
            return board[1][0]
        elif 6 in [x.count(board[2][0]) for x in zip(*board)]:
            return board[2][0]
        elif 6 in [x.count(board[3][0]) for x in zip(*board)]:
            return board[3][0]
        elif 6 in [x.count(board[4][0]) for x in zip(*board)]:
            return board[4][0]
        elif 6 in [x.count(board[5][0]) for x in zip(*board)]:
            return board[5][0]
        elif sum([x.count(board[0][0]) for x in [board[i][i] for i,v in enumerate(board)]]) == 6:
            return board[0][0]
        elif sum([x.count(board[5][0]) for x in[board[5 - i][i] for i,v in enumerate(board)]]) == 6:
            return board[5][0]
        elif 6 not in [x.count(board[0][0]) for x in board]:
            return print("NO WINNER")
        elif 6 not in [x.count(board[1][0]) for x in board]:
            return print("NO WINNER")
        elif 6 not in [x.count(board[2][0]) for x in board]:
            return print("NO WINNER")
        elif 6 not in [x.count(board[3][0]) for x in board]:
            return print("NO WINNER")
        elif 6 not in [x.count(board[4][0]) for x in board]:
            return print("NO WINNER")
        elif 6 not in [x.count(board[5][0]) for x in board]:
            return print("NO WINNER")
        elif 6 not in [x.count(board[0][0]) for x in zip(*board)]:
            return print("NO WINNER")
        elif 6 not in [x.count(board[1][0]) for x in zip(*board)]:
            return print("NO WINNER")
        elif 6 not in [x.count(board[2][0]) for x in zip(*board)]:
            return print("NO WINNER")
        elif 6 not in [x.count(board[3][0]) for x in zip(*board)]:
            return print("NO WINNER")
        elif 6 not in [x.count(board[4][0]) for x in zip(*board)]:
            return print("NO WINNER")
        elif 6 not in [x.count(board[5][0]) for x in zip(*board)]:
            return print("NO WINNER")
        elif sum([x.count(board[0][0]) for x in [board[i][i] for i,v in enumerate(board)]]) != 6:
            return print("NO WINNER")
        elif sum([x.count(board[5][0]) for x in[board[5 - i][i] for i,v in enumerate(board)]]) != 6:
            return print("NO WINNER")
        
def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    track = route_map
    if (first_stop, second_stop) in track:
        return track[(first_stop, second_stop)]
    elif (second_stop, first_stop) in track:
        return track[(second_stop, first_stop)]