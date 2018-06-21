import random
import string

class Card:
    def __init__(self, mark, number):
        self.mark = mark
        self.number = number


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
    while True:
        # シャッフルした状態のデッキを作成
        shuffled_deck = random.sample(deck, len(deck))
        print('ゲームを開始します')
        print('カードを配ります')

        while True:
        # 手札表示画面
