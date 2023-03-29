def isEqual(str1, str2):
    if str1 == str2:
        print("两个字符串相等 ")
    else:
        print('error，与预期字符串不相等')


if __name__ == "__main__":
    base_url1 = "https://baidu.com/"
    base_url2 = "https://fanyi.baidu.com/"
    isEqual(base_url1, base_url1)
