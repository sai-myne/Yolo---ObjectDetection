
def Find_Poker_Hand(hand):
    
    ranks = []
    suits = []
    possibleRanks = []
    
    for card in hand:
        if len(card) == 2:
            rank = card[0]
            suit = card[1]
        else:
            rank = card[0:2]
            suit = card[2]
         
        if rank == "A": 
            rank = 14   
        elif rank == "K": 
            rank = 13
        elif rank == "Q":
            rank = 12
        elif rank == "J":
            rank = 11 
        ranks.append(int(rank))
        suits.append(suit)    
    # print(ranks, suits)
    sortedRanks = sorted(ranks)
    # print(sortedRanks)
    # Royal Flush and Straight Flush and Flush
    if suits.count(suits[0]) == 5:
        if 14 in sortedRanks and 13 in sortedRanks and 12 in sortedRanks and 11 in sortedRanks and 10 in sortedRanks:
            possibleRanks.append(10)
        elif all(sortedRanks[i] == sortedRanks[i-1] + 1 for i in range(1, len(sortedRanks))):
            possibleRanks.append(9)
        else:
            possibleRanks.append(6)
            
    #  Straight
    if all(sortedRanks[i] == sortedRanks[i-1] + 1 for i in range(1, len(sortedRanks))):
        possibleRanks.append(5)
        
    # Four of a kind and Full House
    handUniqueVals = list(set(sortedRanks))
    if len(handUniqueVals) == 2:
        for val in handUniqueVals:
            if sortedRanks.count(val) == 4:
                possibleRanks.append(8)
            if sortedRanks.count(val) == 3:
                possibleRanks.append(7)
    # print(handUniqueVals)
    
    # Three of a kind and two pairs
    if len(handUniqueVals) == 3:
        for val in handUniqueVals:
            if sortedRanks.count(val) == 3:
                possibleRanks.append(4)
            if sortedRanks.count(val) == 2:
                possibleRanks.append(3)
    
    # one pair
    if len(handUniqueVals) == 4:
        possibleRanks.append(2)
                
    
    if not possibleRanks:
        possibleRanks.append(1)
    pokerHandRanks = {10: "Royal Flush", 9: "Straingh Flush", 8: "Four of a Kind", 7: "Full House", 6: "Flush", 5: "Straight", 4: "Three of a Kind", 3: "Two Pairs", 2: "Pair", 1:"High Card"}
    output = pokerHandRanks[max(possibleRanks)]
    print(hand, output)
    return output

if __name__ == "__main__":
    Find_Poker_Hand(["AH", "KH", "QH", "JH", "10H"]) # Royal Flush
    Find_Poker_Hand(["QC", "JC", "10C", "9C", "8C"]) # Straight Flush
    Find_Poker_Hand(["5C", "5S", "5H", "5D", "QH"]) # Four of a kind
    Find_Poker_Hand(["2H", "2D", "2S", "10H", "10C"]) # Full House
    Find_Poker_Hand(["2D", "KD", "7D", "6D", "5D"]) # Flush
    Find_Poker_Hand(["JC", "10H", "9C", "8C", "7D"]) # Straight
    Find_Poker_Hand(["10H", "10C", "10D", "2D", "5S"]) # Three of a Kind
    Find_Poker_Hand(["KD", "KH", "5C", "5S", "6D"]) # Two Pairs
    Find_Poker_Hand(["2D", "2S", "9C", "KD", "10C"]) # Pair
    Find_Poker_Hand(["KD", "5H", "2D", "10C", "JH"]) # High Card












