from random import choice
table = [
    '⚡{} 好電喔⚡',
    '{} 覺得這題好簡單😏',
    '{} 大師教嗎？🙏🙏🙏',
    '💪{} 好強💪追不上',
    '🚩CTF扛霸子 {} 解完了一題🚩',
]

def generator(username):
    return choice(table).format(username)
