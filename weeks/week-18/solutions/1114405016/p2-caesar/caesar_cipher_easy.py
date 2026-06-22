"""
凱薩密碼（Caesar Cipher）
學號：1114405016  SHIFT=7

規則：
- 英文字母向後位移 7 格
- 大小寫各自循環（Z → A）
- 非字母一律不變
"""

def caesar_cipher(text, shift=7):
    out = []
    for ch in text:
        if 'A' <= ch <= 'Z':
            # 大寫：從 A(0) 開始，位移後 mod 26，再加回 A
            out.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        elif 'a' <= ch <= 'z':
            # 小寫：從 a(0) 開始，位移後 mod 26，再加回 a
            out.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        else:
            out.append(ch)   # 非字母不變
    return "".join(out)


def main():
    import sys
    for line in sys.stdin:
        print(caesar_cipher(line.rstrip("\n")))


if __name__ == "__main__":
    main()
