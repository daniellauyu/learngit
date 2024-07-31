#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：FormulaDesign 
@Software : PyCharm
@File ：generateMobilePhoneNumber.py
@Author ：daniel lau
@Date ：2024/7/25 16:47
@site : www.liuyude.com
@describe : 这里是描述
"""
import random

def generate_phone_numbers(count):
    phone_numbers = []
    for _ in range(count):
        # 中国大陆手机号格式为 1 + 第二位 [3-9] + 后九位数字
        phone_number = "1" + str(random.randint(3, 9)) + ''.join([str(random.randint(0, 9)) for _ in range(9)])
        phone_numbers.append(phone_number)
    return phone_numbers

def save_to_file(phone_numbers, filename):
    with open(filename, 'w') as file:
        for number in phone_numbers:
            file.write(f"{number}\n")

if __name__ == "__main__":
    num_of_phone_numbers = int(input("请输入要生成的手机号数量: "))
    phone_numbers = generate_phone_numbers(num_of_phone_numbers)
    save_to_file(phone_numbers, "phone_numbers.txt")
    print(f"生成的手机号已保存到 phone_numbers.txt 文件中。")
