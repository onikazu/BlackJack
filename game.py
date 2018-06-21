# 1は1 絵札についても考えない

import random
import string

class Card:
    def __init__(self, mark, number):
        self.mark = mark
        self.number = number

def hands_open(name, hands):
    print('==============')
    print(name, 'の手札')
    for i in range(len(hands)):
        print(hands[i].mark, hands[i].number)



if __name__ == '__main__':
    # トランプの定義
    marks = ['スペード','クラブ','ハート','ダイヤ']
    numbers = []
    for i in range(1, 14):
        numbers.append(i)

    # トランプインスタンスを作成
    deck = []
    for mark in range(4):
        for num in range(13):
            card = Card(marks[mark], numbers[num])
            deck.append(card)

    # ゲーム画面
    print('ブラックジャックへようこそ！！')

    # 1ゲーム
    while True:
        # シャッフルした状態のデッキを作成
        shuffled_deck = random.sample(deck, len(deck))
        print('ゲームを開始します')
        print('カードを配ります')

        dealer_hands = []
        player_hands = []
        round_count = 1
        card_count = 0

        # ２枚それぞれのプレイヤーに配る
        for i in range(2):
            dealer_hands.append(shuffled_deck[card_count])
            card_count += 1
            player_hands.append(shuffled_deck[card_count])
            card_count += 1

        print(round_count, '回目の手札')
        hands_open('ディーラー', dealer_hands)
        hands_open('プレーヤー', player_hands)

        # 手札追加フェイズ
        while True:
            select  = input('手札を追加するときはyを押してください。\
            追加しないときはそれ以外のキーを押してください')

            if select =='y':
                dealer_hands.append(shuffled_deck[card_count])
                card_count += 1
                player_hands.append(shuffled_deck[card_count])
                card_count += 1
                # 手札表示画面　
                print(round_count, '回目の手札')
                hands_open('ディーラー', dealer_hands)
                hands_open('プレーヤー', player_hands)


        else:
            break
