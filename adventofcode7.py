
def get_hands(hands, filename):

    with open(filename) as f:
        for line in f:
            splitline = line.split(' ')
            hands.append([splitline[0],splitline[1].strip()])

def sort_by_rank(hands):
    return sorted(hands, key = lambda hand: (get_rank_value(hand[2]),get_strength_of_card(hand[0][0]),get_strength_of_card(hand[0][1]),get_strength_of_card(hand[0][2]),get_strength_of_card(hand[0][3]),get_strength_of_card(hand[0][4])))

def get_strength_of_card(card):
    if card == 'T':
        return 10
    if card == 'Q':
        return 11
    if card == 'K':
        return 12
    if card == 'A':
        return 13
    if card == 'J':
        return 1
    else:
        return int(card)

def get_rank(hand):
    cards = hand

    distinct_cards = set(hand)
    counts = []
    for card in distinct_cards:
        counts.append(cards.count(card))

    sorted_counts = sorted(counts)

    if sorted_counts == [5]:
        return 'FiveOfAKind'
    if sorted_counts == [1,4]:
        return 'FourOfAKind'
    if sorted_counts == [2,3]:
        return 'FullHouse'
    if sorted_counts == [1,1,3]:
        return 'ThreeOfAKind'
    if sorted_counts == [1,2,2]:
        return 'TwoPair'
    if sorted_counts == [1,1,1,2]:
        return 'OnePair'

    return 'HighCard'

def get_total_winnings(hands):
    total = 0
    multiplier = 1
    for hand in hands:
        total += int(hand[1])*multiplier
        multiplier += 1

    return total

def get_rank_value(rank):
    if rank == 'HighCard':
        return 0
    if rank == 'OnePair':
        return 1
    if rank == 'TwoPair':
        return 2
    if rank == 'ThreeOfAKind':
        return 3
    if rank == 'FullHouse':
        return 4
    if rank == 'FourOfAKind':
        return 5
    if rank == 'FiveOfAKind':
        return 6

def get_rank_from_value(value):
    if value == 0:
        return 'HighCard'
    if value == 1:
        return 'OnePair'
    if value == 2:
        return 'TwoPair'
    if value == 3:
        return 'ThreeOfAKind'
    if value == 4:
        return 'FullHouse'
    if value == 5:
        return 'FourOfAKind'
    if value == 6:
        return 'FiveOfAKind'

def get_rank_with_joker_rule(hand):

    normal_rank = get_rank(hand)

    j_count = hand.count('J')
    if j_count > 0:
        distinct_cards = list(set(hand))
        distinct_cards.remove('J')
        current_best_value = get_rank_value(normal_rank)
        for cardtype in distinct_cards:
            value = get_rank_value(get_rank(hand.replace('J',cardtype)))
            if value > current_best_value:
                current_best_value = value

        return get_rank_from_value(current_best_value)
    else:
        return normal_rank

def main():
    hands = []

    get_hands(hands, 'test_input.txt')

    for hand in hands:
        hand.append(get_rank_with_joker_rule(hand[0]))

    print(hands)

    hands = sort_by_rank(hands)

    print(hands)
    print(get_total_winnings(hands))

if __name__ == '__main__':
    main()
