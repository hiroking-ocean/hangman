import random

#wordはプレイヤー１が出題する単語
def hangman(word):
    wrong = 0 #間違えた回数

    #ハングマンの首つり画像のコンテナ
    stages = ["",
              " _______       ",
              " |      |      ",
              " |      |      ",
              " |      0      ",
              " |    ／|＼    ",
              " |    ／ ＼    ",
              "_|_____________",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")

    #ゲームの手順を進めるループ処理
    while wrong < len(stages) - 1:
        print("\n")
        msg = "一文字を予想してね"
        char = input(msg)
        if char in rletters:    #入力していた文字があっていた場合
            cind = rletters.index(char) #cindに合っていた文字の位置を入力
            board[cind] = char  #boardに正解していた文字と入れ替える
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("あなたの負け！正解は{}。".format(word))

wordlist = ["cat", "dog", "penguin", "rabbit"]
word = wordlist[random.randint(0,len(wordlist)-1)]
hangman(word)
