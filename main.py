import random

def game():	
		
	PLAYER_IN = True
	DEALER_IN = True
	
	#deck of cards / player dealer hand
	
	deck=[2,3,4,5,6,7,8,9,10,"J","Q","K","A",2,3,4,5,6,7,8,9,10,"J","Q","K","A",2,3,4,5,6,7,8,9,10,"J","Q","K","A",2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
	player_hand=[]
	dealer_hand=[]
	
	#deal the cards function
	
	def deal_card(turn):
		card= random.choice(deck)
		turn.append(card)
		deck.remove(card)
	#calculate the hands
	
	def total(turn):
		total = 0 
		face = ["J","Q","K"]
		for card in turn:
			if card in range(1,11):
				total += card
			elif card in face:
				total += 10
			else:
				if total > 11:
					total += 1
				else:
					total += 11
		return total
	
	#Check winning
	def reveal_dealer():
		if len(dealer_hand) == 2:
			return dealer_hand[0]
		elif len(dealer_hand) > 2 :
			return dealer_hand
	#Game
	for _ in range(2):
		deal_card(dealer_hand)
		deal_card(player_hand)
	
	while PLAYER_IN or DEALER_IN :
		print(f"Dealer has {reveal_dealer()} and X")
		print(f"You have {player_hand} for total of {total(player_hand)}")
		if PLAYER_IN:
			stay_or_hit= input("S to stay \nH to hit\n").lower()
		if total(dealer_hand) > 16 :
			DEALER_IN = False
		else:
			deal_card(dealer_hand)
		if stay_or_hit == "s" :
			PLAYER_IN = False
		elif stay_or_hit == "h":
			deal_card(player_hand)
		if total(player_hand) >= 21:
			break
		elif total(dealer_hand) >= 21:
			break
	
	def show_hand():
		print(f"You got  {player_hand} for {total(player_hand)}. Dealer got {dealer_hand} for {total(dealer_hand)}.")
	
	if total(player_hand) == 21:
		show_hand()
		print("Blackjack You Win.")
	elif total(dealer_hand) == 21:
		show_hand()
		print("Dealer got blackjack")
	elif total(player_hand) > 21:
		show_hand()
		print("Busted.")
	elif total(dealer_hand) > 21:
		show_hand()
		print("Dealer busted. You win")
	elif 21 - total(dealer_hand) < 21 - total(player_hand):
		show_hand()
		print("Dealer win.")
	elif 21 - total(dealer_hand) > 21 - total(player_hand):
		show_hand()
		print("You win.")

while True:
	game()
	cont= input("You wanna keep playing? Y or N\n").lower()
  print(")
	if cont == "n":
		break
