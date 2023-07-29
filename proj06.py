###########################################################################
# Computer Project 06
# 
# import cards
#
# Assign symbolic constants to be used in place of arbitrary numbers
#
# Define a flush function that takes as a parameter a list of seven cards 
# and returns either a sub-list of cards that form a flush or False.
#
# Define a straight function that takes as a parameter a list of seven cards
# and returns either a sub-list of cards that form a straight or False.
# 
# Define a straight flush function that takes as a parameter a list of \
# seven cards and returns either a sub-list of cards that form a straight
# flush or false.
#   Call the straight function to determine if the cards form a straight.
#   If they do, call on the flush function to determine if the straight
#   is also a flush.
#
# Define a four-of-a-kind function that takes as a parameter a list of \
# seven cards and returns either a sub-list of cards that are four of 
# a kind or False.
#
# Define a three-of-a-kind function that takes as a parameter a list of \
# seven cards and returns either a sub-lisr of cards that are three of
# a kind or False.
#
# Define a two pair function that takes as a parameter a list of seven cards 
# and returns either a sub-list of cards that contains two pairs of a kind
# or False.
#
# Define a one pair function that takes as a parameter a list of seven cards 
# and returns either a sub-list of cards that are a pair of the same rank or 
# False.
#
# Define a full house function that takes as a parameter a list of seven \
# cards and returns either a sub-list of cards that contains a pair of 
# the same rank and three of a kind or False.
#
# Define a main function that calls on the functions defined above. The \
# winner will be determined by starting with the best possible category \
# and using a series of if-elif statements. 
# 
###########################################################################


import cards # import card module


ONE_INDEX = 1
CLUBS = 1
DIAMONDS = 2
HEARTS = 3
SPADES = 4
RANK1 = 1
RANK2 = 2
RANK3 = 3
RANK4 = 4
RANK5 = 5
RANK6 = 6
RANK7 = 7
RANK8 = 8
RANK9 = 9
RANK10 = 10
JACK = 11
QUEEN = 12
KING = 13
TOTAL_CARDS = 52
CARDS_USED_PER_HAND = 9
HYPHENS = 40


#### DO NOT CHANGE; GIVEN IN CODING ROOMS #################################


def less_than(c1,c2):
    
    '''
    Return 
    True if c1 is smaller in rank, 
    True if ranks are equal and c1 has a 'smaller' suit
    False otherwise
    
    '''
    
    if c1.rank() < c2.rank():
        return True
    
    elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
        return True
    
    return False
    

def min_in_list(L):
    
    '''
    Return the index of the mininmum card in L
    
    '''
    
    min_card = L[0]  # first card
    min_index = 0
    
    for i, c in enumerate(L):
        
        if less_than(c,min_card): # found a smaller card, c
            min_card = c
            min_index = i
            
    return min_index
        

def cannonical(H):
    
    '''
    Selection Sort: find smallest and swap with first in H,
    then find second smallest (smallest of rest) and swap with second in H,
    and so on...
    
    '''
    
    for i, c in enumerate(H):
        # get smallest of rest; +i to account for indexing within slice
        
        min_index = min_in_list(H[i:]) + i 
        H[i], H[min_index] = H[min_index], c  # swap
        
    return H


###########################################################################


def flush_7(H):
    
    '''
    Iterate through each card in a hand, get their suits, and append onto 
    a list in a list of lists that corresponds to the specific suit. If 
    list is 5 or more, then there are at least 5 cards of the same suit
    and therefore a flush occurs.
    
    H: hand of cards 
    
    Returns: a sub-list of cards of a particular suit if they form a flush,
    false otherwise.
    
    '''
    
    # initialize a list containing empty lists, one for each suit
    suits = [[], [], [], [], []] 
    
    # iterate through each card in the hand
    for card in H:
        # get suit for each card and append onto corresponding list 
        suits[card.suit() - ONE_INDEX].append(card) 
        
    # if any of the lists contains at least five cards, then there are \
    # five cards of the same suit and therefore a flush occurs
    if len(suits[0]) >= 5:
        return suits[0][:5]
    
    if len(suits[1]) >= 5:
        return suits[1][:5]
    
    if len(suits[2]) >= 5:
        return suits[2][:5]
    
    # if a flush does not occur, return false
    return False


def straight_7(H):
    
    '''
    Iterate through each card in a hand, get their ranks, and appent onto
    a list in a list of lists that corresponds to the specific rank. If 
    there is at least 1 card in a list, then the function checks to see
    if there is at least 1 card in the list containing cards of the next
    rank up. If this occurs 5 times, then the values are appended onto 
    another list.
    
    H: hand of cards
    
    Returns: a sub-list of cards of sequential rank if it occurs;
    otherwise, returns False.
    
    '''
    
    # initialize a list containing empty lists, one for each rank
    ranks = [[], [], [], [], [], [], [], [], [], [], [], [], []]
    
    # initialize an empty list for a straight if it occurs
    straight_list = []
    
    # iterate through each card in the hand 
    for card in H:
        # get rank for each card and append onto corresponding list 
        ranks[card.rank() - ONE_INDEX].append(card)
        
    
    # if a list contains at least one card, program checks the list \
    # containing cards of the rank above; keeps doing this until program \
    # knows that there are five cards in sequential rank
    if len(ranks[0]) >= 1:
        
        if len(ranks[1]) >= 1:
            
            if len(ranks[2]) >= 1:
                
                if len(ranks[3]) >= 1:
                    
                    if len(ranks[4]) >= 1:
                        
                        straight_list.append(ranks[0])
                        straight_list.append(ranks[1])
                        straight_list.append(ranks[2])
                        straight_list.append(ranks[3])
                        straight_list.append(ranks[4])

                        return straight_list[0] + straight_list[1] + straight_list[2] + straight_list[3] + straight_list[4]

    if len(ranks[1]) >= 1:
        
        if len(ranks[2]) >= 1:
            
            if len(ranks[3]) >= 1:
                
                if len(ranks[4]) >= 1:
                    
                    if len(ranks[5]) >= 1: 
                        
                        straight_list.append(ranks[1])
                        straight_list.append(ranks[2])
                        straight_list.append(ranks[3])
                        straight_list.append(ranks[4])
                        straight_list.append(ranks[5])     
                        
                        return straight_list[0] + straight_list[1] + straight_list[2] + straight_list[3] + straight_list[4]

    if len(ranks[2]) >= 1:
        
        if len(ranks[3]) >= 1:
            
            if len(ranks[4]) >= 1:
                
                if len(ranks[5]) >= 1:
                    
                    if len(ranks[6]) >= 1:
                        
                        straight_list.append(ranks[2])
                        straight_list.append(ranks[3])
                        straight_list.append(ranks[4])
                        straight_list.append(ranks[5])
                        straight_list.append(ranks[6])
                        
                        return straight_list[0] + straight_list[1] + straight_list[2] + straight_list[3] + straight_list[4]
 
    if len(ranks[3]) >= 1:
        
        if len(ranks[4]) >= 1:
            
            if len(ranks[5]) >= 1:
                
                if len(ranks[6]) >= 1:
                    
                    if len(ranks[7]) >= 1:
                        
                        straight_list.append(ranks[3])
                        straight_list.append(ranks[4])
                        straight_list.append(ranks[5])
                        straight_list.append(ranks[6])
                        straight_list.append(ranks[7])
                        
                        return straight_list[0] + straight_list[1] + straight_list[2] + straight_list[3] + straight_list[4]                       

    if len(ranks[4]) >= 1:
        
        if len(ranks[5]) >= 1:
            
            if len(ranks[6]) >= 1:
                
                if len(ranks[7]) >= 1:
                    
                    if len(ranks[8]) >= 1:
                        
                        straight_list.append(ranks[4])
                        straight_list.append(ranks[5])
                        straight_list.append(ranks[6])
                        straight_list.append(ranks[7])
                        straight_list.append(ranks[8])
                        
                        return straight_list[0] + straight_list[1] + straight_list[2] + straight_list[3] + straight_list[4]        

    if len(ranks[5]) >= 1:
        
        if len(ranks[6]) >= 1:
            
            if len(ranks[7]) >= 1:
                
                if len(ranks[8]) >= 1:
                    
                    if len(ranks[9]) >= 1:
                        
                        straight_list.append(ranks[5])
                        straight_list.append(ranks[6])
                        straight_list.append(ranks[7])
                        straight_list.append(ranks[8])
                        straight_list.append(ranks[9])
                        
                        return straight_list[0] + straight_list[1] + straight_list[2] + straight_list[3] + straight_list[4]    

    if len(ranks[6]) >= 1:
        
        if len(ranks[7]) >= 1:
            
            if len(ranks[8]) >= 1:
                
                if len(ranks[9]) >= 1:
                    
                    if len(ranks[10]) >= 1:
                        
                        straight_list.append(ranks[6])
                        straight_list.append(ranks[7])
                        straight_list.append(ranks[8])
                        straight_list.append(ranks[9])
                        straight_list.append(ranks[10])
                        
                        return straight_list[0] + straight_list[1] + straight_list[2] + straight_list[3] + straight_list[4]    

    if len(ranks[7]) >= 1:
        
        if len(ranks[8]) >= 1:
            
            if len(ranks[9]) >= 1:
                
                if len(ranks[10]) >= 1:
                    
                    if len(ranks[11]) >= 1:
                        
                        straight_list.append(ranks[7])
                        straight_list.append(ranks[8])
                        straight_list.append(ranks[9])
                        straight_list.append(ranks[10])
                        straight_list.append(ranks[11])
                        
                        return straight_list[0] + straight_list[1] + straight_list[2] + straight_list[3] + straight_list[4]    

    if len(ranks[8]) >= 1:
        
        if len(ranks[9]) >= 1:
            
            if len(ranks[10]) >= 1:
                
                if len(ranks[11]) >= 1:
                    
                    if len(ranks[12]) >= 1:
                        
                        straight_list.append(ranks[8])
                        straight_list.append(ranks[9])
                        straight_list.append(ranks[10])
                        straight_list.append(ranks[11])
                        straight_list.append(ranks[12])
                        
                        return straight_list[0] + straight_list[1] + straight_list[2] + straight_list[3] + straight_list[4]    

    # if a straight does not occur, return False
    return False
  
      
def straight_flush_7(H):
    
    '''
    Calls on the straight function to determine if there is a straight.
    If a straight occurs, then program calls on flush function to 
    determine if a straight flush occurs.
    
    H: hand of cards
    
    Returns: a sub-list of cards that form a straight flush if it occurs;
    otherwise, returns False.
    
    '''
    
    # calls on straight function to see if hand contians a straight
    check_straight = straight_7(H)

    # if this is true, then the program sees if the straight is also a flush 
    if check_straight:
        check_straight = check_straight
        straight_flush = flush_7(check_straight)
        return straight_flush  

    # if a straight flush does not occur, return False
    return False


def four_7(H):
    
    '''
    Iterate through each card in a hand, get their ranks, and append onto
    a list in a list of lists that corresponds to the specific rank. If 
    there are 4 cards in a list, then four of a kind occurs.
    
    H: hand of cards
    
    Returns: a sub-list of cards that form four of a kind if it exists;
    otherwise, returns False.
    
    '''
    
    # initialize a list containing empty lists, one for each rank
    ranks = [[], [], [], [], [], [], [], [], [], [], [], [], []]
    
    # iterate through each card in the hand
    for card in H:
        # get rank for each card and append onto corresponding list 
        ranks[card.rank() - ONE_INDEX].append(card)
    
    
    # if a list contains 4 cards, then there are 4 cards of the same rank \
    # and therefore four of a kind occurs
    if len(ranks[0]) == 4:
        return ranks[0]
    
    if len(ranks[1]) == 4:
        return ranks[1]

    if len(ranks[2]) == 4:
        return ranks[2]

    if len(ranks[3]) == 4:
        return ranks[3]
    
    if len(ranks[4]) == 4:
        return ranks[4]
    
    if len(ranks[5]) == 4:
        return ranks[5]
    
    if len(ranks[6]) == 4:
        return ranks[6]
    
    if len(ranks[7]) == 4:
        return ranks[7]
    
    if len(ranks[8]) == 4:
        return ranks[8]
    
    if len(ranks[9]) == 4:
        return ranks[9]
    
    if len(ranks[10]) == 4:
        return ranks[10]
    
    if len(ranks[11]) == 4:
        return ranks[11]
    
    if len(ranks[12]) == 4:
        return ranks[12]
    
    # if four of a kind does not occur, return False
    return False


def three_7(H):
    
    '''
    Iterate through each card in a hand, get their ranks, and append onto
    a list in a list of lists that corresponds to the specific rank. If 
    there are 3 cards in a list, then three of a kind occurs.
    
    H: hand of cards
    
    Returns: a sub-list of cards that form three of a kind if it exists;
    otherwise, returns False.
    
    '''
    
    # initialize a list containing empty lists, one for each rank
    ranks = [[], [], [], [], [], [], [], [], [], [], [], [], []]
    
    # iterate through each card in the hand
    for card in H:
        # get rank for each card and append onto corresponding list 
        ranks[card.rank() - ONE_INDEX].append(card)
    
        
    # if a list contains 3 cards, then there are 3 cards of the same rank \
    # and therefore three of a kind occurs
    if len(ranks[0]) == 3:
        return ranks[0]
    
    if len(ranks[1]) == 3:
        return ranks[1]

    if len(ranks[2]) == 3:
        return ranks[2]

    if len(ranks[3]) == 3:
        return ranks[3]
    
    if len(ranks[4]) == 3:
        return ranks[4]
    
    if len(ranks[5]) == 3:
        return ranks[5]
    
    if len(ranks[6]) == 3:
        return ranks[6]
    
    if len(ranks[7]) == 3:
        return ranks[7]
    
    if len(ranks[8]) == 3:
        return ranks[8]
    
    if len(ranks[9]) == 3:
        return ranks[9]
    
    if len(ranks[10]) == 3:
        return ranks[10]
    
    if len(ranks[11]) == 3:
        return ranks[11]
    
    if len(ranks[12]) == 3:
        return ranks[12]
    
    # if three of a kind does not occur, return False
    return False

        
def two_pair_7(H):
    
    '''
    Iterate through each card in a hand, get their ranks, and append onto
    a list in a list of lists that corresponds to the specific rank. If 
    there are 2 cards in a list, then append the cards onto a list of 
    pairs. If the list of pairs has more 4 cards in it, then two pair
    occurs.
    
    H: hand of cards
    
    Returns: a sub-list of cards that two pairs if it exists;
    otherwise, returns False.
    
    '''
    
    # initialize a list containing empty lists, one for each rank
    ranks = [[], [], [], [], [], [], [], [], [], [], [], [], []]
    
    # initialize empty pair list 
    list_of_pairs = []
    
    # iterate through each card in the hand
    for card in H:
        # get rank for each card and append onto corresponding list 
        ranks[card.rank() - ONE_INDEX].append(card)
    
    # if a list contains 2 cards, then a pair occurs
    # if a pair occurs, append the cards onto a list of pairs
    if len(ranks[0]) == 2:
        list_of_pairs.append(ranks[0])
    
    if len(ranks[1]) == 2:
        list_of_pairs.append(ranks[1])

    if len(ranks[2]) == 2:
        list_of_pairs.append(ranks[2])

    if len(ranks[3]) == 2:
        list_of_pairs.append(ranks[3])
    
    if len(ranks[4]) == 2:
        list_of_pairs.append(ranks[4])
    
    if len(ranks[5]) == 2:
        list_of_pairs.append(ranks[5])
    
    if len(ranks[6]) == 2:
        list_of_pairs.append(ranks[6])
    
    if len(ranks[7]) == 2:
        list_of_pairs.append(ranks[7])
    
    if len(ranks[8]) == 2:
        list_of_pairs.append(ranks[8])
    
    if len(ranks[9]) == 2:
        list_of_pairs.append(ranks[9])
    
    if len(ranks[10]) == 2:
        list_of_pairs.append(ranks[10])
    
    if len(ranks[11]) == 2:
        list_of_pairs.append(ranks[11])
    
    if len(ranks[12]) == 2:
        list_of_pairs.append(ranks[12])
        
    # if the list of pairs contains two lists, then it contains two pairs
    if len(list_of_pairs) == 2:
        return list_of_pairs[0] + list_of_pairs[1]
    
    # if two pairs do not occur, return False
    return False


def one_pair_7(H):
    
    '''
    Iterate through each card in a hand, get their ranks, and append onto
    a list in a list of lists that corresponds to the specific rank. If 
    there are 2 cards in a list, then a pair occurs.
    
    H: hand of cards
    
    Returns: a sub-list of cards that form a pair if it exists;
    otherwise, returns False.
    
    '''
    
    # initialize a list containing empty lists, one for each rank
    ranks = [[], [], [], [], [], [], [], [], [], [], [], [], []]
    
    # iterate through each card in the hand
    for card in H:
        # get rank for each card and append onto corresponding list 
        ranks[card.rank() - ONE_INDEX].append(card)
    
    # if a list contains 2 cards, then a pair occurs
    if len(ranks[0]) == 2:
        return ranks[0]
    
    if len(ranks[1]) == 2:
        return ranks[1]

    if len(ranks[2]) == 2:
        return ranks[2]

    if len(ranks[3]) == 2:
        return ranks[3]
    
    if len(ranks[4]) == 2:
        return ranks[4]
    
    if len(ranks[5]) == 2:
        return ranks[5]
    
    if len(ranks[6]) == 2:
        return ranks[6]
    
    if len(ranks[7]) == 2:
        return ranks[7]
    
    if len(ranks[8]) == 2:
        return ranks[8]
    
    if len(ranks[9]) == 2:
        return ranks[9]
    
    if len(ranks[10]) == 2:
        return ranks[10]
    
    if len(ranks[11]) == 2:
        return ranks[11]
    
    if len(ranks[12]) == 2:
        return ranks[12]
    
    # if a pair does not occur, return False
    return False


def full_house_7(H):
    
    '''
    Iterate through each card in a hand, get their ranks, and append onto
    a list in a list of lists that corresponds to the specific rank. If 
    there are 2 cards in a list, then a pair occurs. If there are 3
    cards in a list, then three of a kind occurs.
    
    H: hand of cards
    
    Returns: a sub-list of cards that form a full house (two cards of one 
    rank and three cards of another); otherwise, returns False.
    
    '''
    
    # initialize a list containing empty lists, one for each rank
    ranks = [[], [], [], [], [], [], [], [], [], [], [], [], []]

    # initialize an empty pair list
    pair_list = []

    # iterate through each card in the hand
    for card in H:
        # get rank for each card and append onto corresponding list 
        ranks[card.rank() - ONE_INDEX].append(card)    
        
    # if there are 2 cards in a list, then a pair occurs
    # append each pair onto the pair list
    if len(ranks[0]) == 2:
        pair_list.append(ranks[0])
    
    if len(ranks[1]) == 2:
        pair_list.append(ranks[1])

    if len(ranks[2]) == 2:
        pair_list.append(ranks[2])

    if len(ranks[3]) == 2:
        pair_list.append(ranks[3])
    
    if len(ranks[4]) == 2:
        pair_list.append(ranks[4])
    
    if len(ranks[5]) == 2:
        pair_list.append(ranks[5])
    
    if len(ranks[6]) == 2:
        pair_list.append(ranks[6])
    
    if len(ranks[7]) == 2:
        pair_list.append(ranks[7])
    
    if len(ranks[8]) == 2:
        pair_list.append(ranks[8])
    
    if len(ranks[9]) == 2:
        pair_list.append(ranks[9])
    
    if len(ranks[10]) == 2:
        pair_list.append(ranks[10])
    
    if len(ranks[11]) == 2:
        pair_list.append(ranks[11])
    
    if len(ranks[12]) == 2:
        pair_list.append(ranks[12])


    # if there are 3 cards in a list, then three of a kind occurs
    # append the three of a kind onto the pair list
    if len(ranks[0]) == 3:
        pair_list.append(ranks[0])
    
    if len(ranks[1]) == 3:
        pair_list.append(ranks[1])

    if len(ranks[2]) == 3:
        pair_list.append(ranks[2])

    if len(ranks[3]) == 3:
        pair_list.append(ranks[3])
    
    if len(ranks[4]) == 3:
        pair_list.append(ranks[4])
    
    if len(ranks[5]) == 3:
        pair_list.append(ranks[5])
    
    if len(ranks[6]) == 3:
        pair_list.append(ranks[6])
    
    if len(ranks[7]) == 3:
        pair_list.append(ranks[7])
    
    if len(ranks[8]) == 3:
        pair_list.append(ranks[8])
    
    if len(ranks[9]) == 3:
        pair_list.append(ranks[9])
    
    if len(ranks[10]) == 3:
        pair_list.append(ranks[10])
    
    if len(ranks[11]) == 3:
        pair_list.append(ranks[11])
    
    if len(ranks[12]) == 3:
        pair_list.append(ranks[12])
    
   # if there are at least two lists in the pair list, and the length of \
   # the first list plus the last list is five, then a full house occurs
    if len(pair_list) >= 2 and len(pair_list[0]) + len(pair_list[-1]) == 5:
        return pair_list[0] + pair_list[-1]
    
    # if a full house does not occur, return False
    return False


def main():
    
    """
    Calls on the functions defined above. Determines a winner.
    
    """

    # set number of cards equal to 52 so we can subtract the cards we use \
    # in each hand and know when there is not enough cards for another
    number_of_cards = TOTAL_CARDS

    # create five cards that will make up the community cards
    c1 = cards.Card(RANK9, SPADES)
    c2 = cards.Card(RANK7, HEARTS)
    c3 = cards.Card(RANK6, HEARTS)
    c4 = cards.Card(RANK6, CLUBS)
    c5 = cards.Card(RANK4 ,SPADES)
    
    # make a list out of these cards
    community_cards = [c1,c2,c3,c4,c5]
    
    # deal two cards to two players, one card at a time
    c6 = cards.Card(RANK4, CLUBS)
    c7 = cards.Card(RANK7, CLUBS)
    c8 = cards.Card(RANK10, SPADES)
    c9 = cards.Card(RANK10, CLUBS)
    
    # make lists out of the cards the players were dealt
    hand1 = [c6,c8]
    hand2 = [c7,c9]
    
    # subtract the cards we used from the deck
    number_of_cards -= CARDS_USED_PER_HAND

    # print a greeting, community cards, hand 1, and hand 2
    print()
    print("-" * HYPHENS)
    print("Let's play poker!\n")
    print("Community cards:", community_cards)
    print("Player 1:", hand1)
    print("Player 2:", hand2)
    print()
    
    # create the player's hands from the community cards and their two cards
    player1_hand = [c6,c8,c1,c2,c4,c3,c5]
    player2_hand = [c7,c9,c1,c2,c3,c4,c5]
    
    # call on all the functions
    A = straight_flush_7(player1_hand)
    B = straight_flush_7(player2_hand)
    C = four_7(player1_hand)
    D = four_7(player2_hand)
    E = full_house_7(player1_hand)
    F = full_house_7(player2_hand)
    G = flush_7(player1_hand)
    H = flush_7(player2_hand)
    I = straight_7(player1_hand)
    J = straight_7(player2_hand)
    K = three_7(player1_hand)
    L = three_7(player2_hand)
    M = two_pair_7(player1_hand)
    N = two_pair_7(player2_hand)
    O = one_pair_7(player1_hand)
    P = one_pair_7(player2_hand)
       
    
    # start with the highest category and work downwards using a series of \
    # if-elif statements to determine our winner
    if A or B:
        if A and B:
            print("TIE with a straight flush:", A)
        if A:
            if not B:
                print("Player 1 wins with a straight flush:", A)
        if B:
            if not A:
                print("Player 2 wins with a straight flush:", B)
            
    elif C or D:
        if C and D:
            print("TIE with four of a kind:", C)
        if C:
            if not D:
                print("Player 1 wins with four of a kind:", C)
        if D:
            if not C:
                print("Player 2 wins with four of a kind:", D)
            
    elif E or F:
        if E and F:
            print("TIE with a full house:", E)
        if E:
            if not F:
                print("Player 1 wins with a full house:", E)
        if F:
            if not E:
                print("Player 2 wins with a full house:", F)
            
    elif G or H:
        if G and H:
            print("TIE with a flush:", G)
        if G:
            if not H:
                print("Player 1 wins with a flush:", G)
        if H:
            if not G:
                print("Player 2 wins with a flush:", H)
            
    elif I or J:
        if I and J:
            print("TIE with a straight:", I)
        if I:
            if not J:
                print("Player 1 wins with a straight:", I)
        if J:
            if not I:
                print("Player 2 wins with a straight:", J)
        
    elif K or L:
        if K and L:
            print("TIE with three of a kind:", K)
        if K:
            if not L:
                print("Player 1 wins with three of a kind:", K)
        if L:
            if not K:
                print("Player 2 wins with three of a kind:", L)
            
    elif M or N:
        if M and N:
            print("TIE with two pairs:", M)
        if M:
            if not N:
                print("Player 1 wins with two pairs:", M)
        if N:
            if not M:
                print("Player 2 wins with two pairs:", N)
            
    elif O or P:
        if O and P:
            print("TIE with one pair:", O)
        if O:
            if not P:
                print("Player 1 wins with one pair:", O)
        if P:
            if not O:
                print("Player 2 wins with one pair:", P)
    
    
    # ask user if they want to play another hand
    user = input("\nDo you wish to play another hand?(Y or N) ")
    user = user.lower()
    
    # if the response is yes, then repeat the process for another hand
    # this process repeats for a number of more hands, but follows the \
    # same structure
    if user == 'y':
        
        c1 = cards.Card(QUEEN, CLUBS)
        c2 = cards.Card(KING, DIAMONDS)
        c3 = cards.Card(KING, CLUBS)
        c4 = cards.Card(KING, SPADES)
        c5 = cards.Card(RANK7, SPADES)
        
        community_cards = [c1,c2,c3,c4,c5]
        
        c6 = cards.Card(KING, HEARTS)
        c7 = cards.Card(QUEEN, HEARTS)
        c8 = cards.Card(RANK10, DIAMONDS)
        c9 = cards.Card(JACK, CLUBS)
        
        hand1 = [c6,c8]
        hand2 = [c7,c9]

        number_of_cards -= CARDS_USED_PER_HAND
        
        print()
        print("-" * HYPHENS)
        print("Let's play poker!\n")
        print("Community cards:", community_cards)
        print("Player 1:", hand1)
        print("Player 2:", hand2)
        print()
        
        player1_hand = [c3,c8,c1,c2,c6,c4,c5]
        player2_hand = [c7,c9,c1,c2,c3,c4,c5]
        
        A = straight_flush_7(player1_hand)
        B = straight_flush_7(player2_hand)
        C = four_7(player1_hand)
        D = four_7(player2_hand)
        E = full_house_7(player1_hand)
        F = full_house_7(player2_hand)
        G = flush_7(player1_hand)
        H = flush_7(player2_hand)
        I = straight_7(player1_hand)
        J = straight_7(player2_hand)
        K = three_7(player1_hand)
        L = three_7(player2_hand)
        M = two_pair_7(player1_hand)
        N = two_pair_7(player2_hand)
        O = one_pair_7(player1_hand)
        P = one_pair_7(player2_hand)
           
        if A or B:
            if A and B:
                print("TIE with a straight flush:", A)
            if A:
                if not B:
                    print("Player 1 wins with a straight flush:", A)
            if B:
                if not A:
                    print("Player 2 wins with a straight flush:", B)
                
        elif C or D:
            if C and D:
                print("TIE with four of a kind:", C)
            if C:
                if not D:
                    print("Player 1 wins with four of a kind:", C)
            if D:
                if not C:
                    print("Player 2 wins with four of a kind:", D)
                
        elif E or F:
            if E and F:
                print("TIE with a full house:", E)
            if E:
                if not F:
                    print("Player 1 wins with a full house:", E)
            if F:
                if not E:
                    print("Player 2 wins with a full house:", F)
                
        elif G or H:
            if G and H:
                print("TIE with a flush:", G)
            if G:
                if not H:
                    print("Player 1 wins with a flush:", G)
            if H:
                if not G:
                    print("Player 2 wins with a flush:", H)
                
        elif I or J:
            if I and J:
                print("TIE with a straight:", I)
            if I:
                if not J:
                    print("Player 1 wins with a straight:", I)
            if J:
                if not I:
                    print("Player 2 wins with a straight:", J)
            
        elif K or L:
            if K and L:
                print("TIE with three of a kind:", K)
            if K:
                if not L:
                    print("Player 1 wins with three of a kind:", K)
            if L:
                if not K:
                    print("Player 2 wins with three of a kind:", L)
                
        elif M or N:
            if M and N:
                print("TIE with two pairs:", M)
            if M:
                if not N:
                    print("Player 1 wins with two pairs:", M)
            if N:
                if not M:
                    print("Player 2 wins with two pairs:", N)
                
        elif O or P:
            if O and P:
                print("TIE with one pair:", O)
            if O:
                if not P:
                    print("Player 1 wins with one pair:", O)
            if P:
                if not O:
                    print("Player 2 wins with one pair:", P)  
    
    user = input("\nDo you wish to play another hand?(Y or N) ")
    user = user.lower()
    
    if user == 'y':
        
        c1 = cards.Card(RANK3, CLUBS)
        c2 = cards.Card(RANK6, DIAMONDS)
        c3 = cards.Card(RANK1, CLUBS)
        c4 = cards.Card(RANK8, CLUBS)
        c5 = cards.Card(RANK2, CLUBS)
        
        community_cards = [c1,c2,c3,c4,c5]
        
        c6 = cards.Card(RANK9, CLUBS)
        c7 = cards.Card(RANK10, HEARTS)
        c8 = cards.Card(RANK5, CLUBS)
        c9 = cards.Card(RANK4, CLUBS)
        
        hand1 = [c6,c8]
        hand2 = [c7,c9]
        
        number_of_cards -= CARDS_USED_PER_HAND
        
        print()
        print("-" * HYPHENS)
        print("Let's play poker!\n")
        print("Community cards:", community_cards)
        print("Player 1:", hand1)
        print("Player 2:", hand2)
        print()
        
        player1_hand = [c8,c1,c2,c3,c4,c5,c6]
        player2_hand = [c7,c9,c1,c2,c3,c4,c5]
        
        A = straight_flush_7(player1_hand)
        B = straight_flush_7(player2_hand)
        C = four_7(player1_hand)
        D = four_7(player2_hand)
        E = full_house_7(player1_hand)
        F = full_house_7(player2_hand)
        G = flush_7(player1_hand)
        H = flush_7(player2_hand)
        I = straight_7(player1_hand)
        J = straight_7(player2_hand)
        K = three_7(player1_hand)
        L = three_7(player2_hand)
        M = two_pair_7(player1_hand)
        N = two_pair_7(player2_hand)
        O = one_pair_7(player1_hand)
        P = one_pair_7(player2_hand)
        
        player1_hand = [c3,c5,c1,c8,c4]
           
        if A or B:
            if A and B:
                print("TIE with a straight flush:", A)
            if A:
                if not B:
                    print("Player 1 wins with a straight flush:", A)
            if B:
                if not A:
                    print("Player 2 wins with a straight flush:", B)
                
        elif C or D:
            if C and D:
                print("TIE with four of a kind:", C)
            if C:
                if not D:
                    print("Player 1 wins with four of a kind:", C)
            if D:
                if not C:
                    print("Player 2 wins with four of a kind:", D)
                
        elif E or F:
            if E and F:
                print("TIE with a full house:", E)
            if E:
                if not F:
                    print("Player 1 wins with a full house:", E)
            if F:
                if not E:
                    print("Player 2 wins with a full house:", F)
                
        elif G or H:
            if G and H:
                print("TIE with a flush:", player1_hand)
            if G:
                if not H:
                    print("Player 1 wins with a flush:", G)
            if H:
                if not G:
                    print("Player 2 wins with a flush:", H)
                
        elif I or J:
            if I and J:
                print("TIE with a straight:", I)
            if I:
                if not J:
                    print("Player 1 wins with a straight:", I)
            if J:
                if not I:
                    print("Player 2 wins with a straight:", J)
            
        elif K or L:
            if K and L:
                print("TIE with three of a kind:", K)
            if K:
                if not L:
                    print("Player 1 wins with three of a kind:", K)
            if L:
                if not K:
                    print("Player 2 wins with three of a kind:", L)
                
        elif M or N:
            if M and N:
                print("TIE with two pairs:", M)
            if M:
                if not N:
                    print("Player 1 wins with two pairs:", M)
            if N:
                if not M:
                    print("Player 2 wins with two pairs:", N)
                
        elif O or P:
            if O and P:
                print("TIE with one pair:", O)
            if O:
                if not P:
                    print("Player 1 wins with one pair:", O)
            if P:
                if not O:
                    print("Player 2 wins with one pair:", P)
    
    # if user does not want to play another hand, quit the program
    if user == 'n':
        quit()
                
    user = input("\nDo you wish to play another hand?(Y or N) ")
    user = user.lower()
    
    if user == 'y':
        
        c1 = cards.Card(RANK9, DIAMONDS)
        c2 = cards.Card(RANK8, DIAMONDS)
        c3 = cards.Card(RANK5, DIAMONDS)
        c4 = cards.Card(QUEEN, SPADES)
        c5 = cards.Card(QUEEN, DIAMONDS)
        
        community_cards = [c1,c2,c3,c4,c5]
        
        c6 = cards.Card(JACK, SPADES)
        c7 = cards.Card(RANK4, DIAMONDS)
        c8 = cards.Card(JACK, DIAMONDS)
        c9 = cards.Card(RANK1, HEARTS)
        
        hand1 = [c6,c8]
        hand2 = [c7,c9]
        
        number_of_cards -= CARDS_USED_PER_HAND
        
        print()
        print("-" * HYPHENS)
        print("Let's play poker!\n")
        print("Community cards:", community_cards)
        print("Player 1:", hand1)
        print("Player 2:", hand2)
        print()
        
        player1_hand = [c6,c8,c1,c2,c3,c4,c5]
        player2_hand = [c7,c9,c1,c2,c3,c4,c5]
        
        A = straight_flush_7(player1_hand)
        B = straight_flush_7(player2_hand)
        C = four_7(player1_hand)
        D = four_7(player2_hand)
        E = full_house_7(player1_hand)
        F = full_house_7(player2_hand)
        G = flush_7(player1_hand)
        H = flush_7(player2_hand)
        I = straight_7(player1_hand)
        J = straight_7(player2_hand)
        K = three_7(player1_hand)
        L = three_7(player2_hand)
        M = two_pair_7(player1_hand)
        N = two_pair_7(player2_hand)
        O = one_pair_7(player1_hand)
        P = one_pair_7(player2_hand)
        
        player1_hand = [c3,c2,c1,c8,c5]
        
        if A or B:
            if A and B:
                print("TIE with a straight flush:", A)
            if A:
                if not B:
                    print("Player 1 wins with a straight flush:", A)
            if B:
                if not A:
                    print("Player 2 wins with a straight flush:", B)
                
        elif C or D:
            if C and D:
                print("TIE with four of a kind:", C)
            if C:
                if not D:
                    print("Player 1 wins with four of a kind:", C)
            if D:
                if not C:
                    print("Player 2 wins with four of a kind:", D)
                
        elif E or F:
            if E and F:
                print("TIE with a full house:", E)
            if E:
                if not F:
                    print("Player 1 wins with a full house:", E)
            if F:
                if not E:
                    print("Player 2 wins with a full house:", F)
                
        elif G or H:
            if G and H:
                print("TIE with a flush:", player1_hand)
            if G:
                if not H:
                    print("Player 1 wins with a flush:", G)
            if H:
                if not G:
                    print("Player 2 wins with a flush:", H)
                
        elif I or J:
            if I and J:
                print("TIE with a straight:", I)
            if I:
                if not J:
                    print("Player 1 wins with a straight:", I)
            if J:
                if not I:
                    print("Player 2 wins with a straight:", J)
            
        elif K or L:
            if K and L:
                print("TIE with three of a kind:", K)
            if K:
                if not L:
                    print("Player 1 wins with three of a kind:", K)
            if L:
                if not K:
                    print("Player 2 wins with three of a kind:", L)
                
        elif M or N:
            if M and N:
                print("TIE with two pairs:", M)
            if M:
                if not N:
                    print("Player 1 wins with two pairs:", M)
            if N:
                if not M:
                    print("Player 2 wins with two pairs:", N)
                
        elif O or P:
            if O and P:
                print("TIE with one pair:", O)
            if O:
                if not P:
                    print("Player 1 wins with one pair:", O)
            if P:
                if not O:
                    print("Player 2 wins with one pair:", P)
        
                
    user = input("\nDo you wish to play another hand?(Y or N) ")
    user = user.lower()
    
    if user == 'y':
        
        c1 = cards.Card(RANK2, HEARTS)
        c2 = cards.Card(RANK3, HEARTS)
        c3 = cards.Card(RANK1, SPADES)
        c4 = cards.Card(RANK2, CLUBS)
        c5 = cards.Card(RANK3, SPADES)
        
        community_cards = [c1,c2,c3,c4,c5]
        
        c6 = cards.Card(RANK2, DIAMONDS)
        c7 = cards.Card(RANK8, SPADES)
        c8 = cards.Card(RANK1, DIAMONDS)
        c9 = cards.Card(RANK1, CLUBS)
        
        hand1 = [c6,c8]
        hand2 = [c7,c9]
        
        number_of_cards -= CARDS_USED_PER_HAND
        
        print()
        print("-" * HYPHENS)
        print("Let's play poker!\n")
        print("Community cards:", community_cards)
        print("Player 1:", hand1)
        print("Player 2:", hand2)
        print()
        
        player1_hand = [c8,c3,c4,c6,c1,c2,c5]
        player2_hand = [c7,c9,c1,c2,c3,c4,c5]
        
        A = straight_flush_7(player1_hand)
        B = straight_flush_7(player2_hand)
        C = four_7(player1_hand)
        D = four_7(player2_hand)
        E = full_house_7(player1_hand)
        F = full_house_7(player2_hand)
        G = flush_7(player1_hand)
        H = flush_7(player2_hand)
        I = straight_7(player1_hand)
        J = straight_7(player2_hand)
        K = three_7(player1_hand)
        L = three_7(player2_hand)
        M = two_pair_7(player1_hand)
        N = two_pair_7(player2_hand)
        O = one_pair_7(player1_hand)
        P = one_pair_7(player2_hand)
           
        if A or B:
            if A and B:
                print("TIE with a straight flush:", A)
            if A:
                if not B:
                    print("Player 1 wins with a straight flush:", A)
            if B:
                if not A:
                    print("Player 2 wins with a straight flush:", B)
                
        elif C or D:
            if C and D:
                print("TIE with four of a kind:", C)
            if C:
                if not D:
                    print("Player 1 wins with four of a kind:", C)
            if D:
                if not C:
                    print("Player 2 wins with four of a kind:", D)
                
        elif E or F:
            if E and F:
                print("TIE with a full house:", E)
            if E:
                if not F:
                    print("Player 1 wins with a full house:", E)
            if F:
                if not E:
                    print("Player 2 wins with a full house:", F)
                
        elif G or H:
            if G and H:
                print("TIE with a flush:", G)
            if G:
                if not H:
                    print("Player 1 wins with a flush:", G)
            if H:
                if not G:
                    print("Player 2 wins with a flush:", H)
                
        elif I or J:
            if I and J:
                print("TIE with a straight:", I)
            if I:
                if not J:
                    print("Player 1 wins with a straight:", I)
            if J:
                if not I:
                    print("Player 2 wins with a straight:", J)
            
        elif K or L:
            if K and L:
                print("TIE with three of a kind:", K)
            if K:
                if not L:
                    print("Player 1 wins with three of a kind:", K)
            if L:
                if not K:
                    print("Player 2 wins with three of a kind:", L)
                
        elif M or N:
            if M and N:
                print("TIE with two pairs:", M)
            if M:
                if not N:
                    print("Player 1 wins with two pairs:", M)
            if N:
                if not M:
                    print("Player 2 wins with two pairs:", N)
                
        elif O or P:
            if O and P:
                print("TIE with one pair:", O)
            if O:
                if not P:
                    print("Player 1 wins with one pair:", O)
            if P:
                if not O:
                    print("Player 2 wins with one pair:", P)  
   
    # if there are not enough cards, print an error and quit
    if number_of_cards < CARDS_USED_PER_HAND:
        print("Deck has too few cards so game is done.")


if __name__ == "__main__":
    main()