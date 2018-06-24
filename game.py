# 1は1
# ディーラーは常に後攻

import random
import time


# トランプ１枚のクラス
class Card:
    def __init__(self, mark, number):
        self.mark = mark
        self.number = number


# プレーヤーの手札のクラス
class Hands:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.cards_sum = 0


# 手札を表示する関数
def hands_open(hands):
    print('==============')
    print(hands.name, 'の手札')
    for i in range(len(hands.cards)):
        print(hands.cards[i].mark, hands.cards[i].number)
    print('合計', hands.cards_sum)


# 手札にカードを追加する関数
def add_card(hands, counter):
    hands.cards.append(shuffled_deck[counter])
    if shuffled_deck[counter].number <= 10:
        hands.cards_sum += shuffled_deck[counter].number
    else:
        hands.cards_sum += 10


if __name__ == '__main__':
    # トランプの定義
    marks = ['スペード', 'クラブ', 'ハート', 'ダイヤ']
    numbers = []
    for i in range(1, 14):
        numbers.append(i)

    # トランプインスタンスを作成し、デッキに追加
    deck = []
    for mark in range(4):
        for num in range(13):
            card = Card(marks[mark], numbers[num])
            deck.append(card)

    # ゲーム画面
    print('ブラックジャックへようこそ！！')

    # 1ゲーム
    while True:
        # ゲームに勝ったかどうかのフラグ
        wins_game = False
        draw_game = False

        # ラウンド数のカウントとカード番号のカウント（デッキからカードを引くため）
        round_count = 1
        card_count = 0

        # カードを引ける権利
        player_can_draw = True
        dealer_can_draw = True

        # ゲームごとにシャッフルした状態のデッキを定義
        shuffled_deck = random.sample(deck, len(deck))

        print('ゲームを開始します')
        print('カードを配ります')

        # 手札インスタンスの作成
        dealer_hands = Hands('ディーラー')
        player_hands = Hands('プレーヤー')

        # ２枚それぞれのプレイヤーに配る
        for _ in range(2):
            add_card(dealer_hands, card_count)
            card_count += 1
            add_card(player_hands, card_count)
            card_count += 1

        print(round_count, '回目の手札')
        hands_open(dealer_hands)
        hands_open(player_hands)

        # 手札追加フェイズ
        while True:
            # 追加でカードを引くかどうかの判定
            select = 'n'

            if player_can_draw is True:
                select = input('手札を追加するときはyを押してください。\
                追加しないときはそれ以外のキーを押してください')

                if select == 'y':
                    add_card(player_hands, card_count)
                    card_count += 1
                else:
                    player_can_draw = False

            if dealer_can_draw is True:
                if dealer_hands.cards_sum < 18 and player_hands.cards_sum > dealer_hands.cards_sum and player_hands.cards_sum <= 21:
                    add_card(dealer_hands, card_count)
                    card_count += 1
                    print('ディーラーがカードを引きました')
                else:
                    dealer_can_draw = False

            round_count += 1

            # 勝敗判定
            # プレーヤーバースト
            if player_hands.cards_sum > 21:
                break

            # ディーラーバースト
            if dealer_hands.cards_sum > 21:
                wins_game = True
                break

            # 拒否権によるプレーヤー勝利
            if dealer_can_draw is False and player_hands.cards_sum > dealer_hands.cards_sum:
                wins_game = True
                break

            # 拒否権によるプレーヤー敗北
            if player_can_draw is False and dealer_hands.cards_sum > player_hands.cards_sum:
                break

            # 両者ブラックジャックによる引き分け
            if player_hands.cards_sum == 21 and dealer_hands.cards_sum == 21:
                draw_game = True
                break

            print('''



                    ''')
            # 手札表示画面　
            print(round_count, '回目の手札')
            hands_open(dealer_hands)
            hands_open(player_hands)

            # 次のフェイズへの待機時間
            time.sleep(2)

        # 手札表示画面
        print(round_count, '回目の手札')
        hands_open(dealer_hands)
        hands_open(player_hands)

        # 勝敗表示
        if draw_game is True:
            print('引き分けです')
        else:
            if wins_game is True:
                print('おめでとう！　あなたが勝者です！！')
            else:
                print('残念！！！')

        # 次のゲームへの待機時間
        time.sleep(5)
        print('''
        
         
        ''')
