import random
def random_name_selector(filename="name_list.txt"):

    try:
        # 读取文件中的所有名称
        with open(filename, 'r', encoding='utf-8') as file:
            names = [line.strip() for line in file if line.strip()]

        # 检查是否成功读取到名称
        if not names:
            print("错误：文件中没有找到有效的名称")
            return None

        # 随机选择一个名称
        selected_name = random.choice(names)
        return selected_name

    except FileNotFoundError:
        print(f"错误：找不到文件 '{filename}'")
        return None
    except Exception as e:
        print(f"读取文件时发生错误：{e}")
        return None
def main():
    selected_name = random_name_selector()

    if selected_name:
        print(f"随机选择的名称是：{selected_name}")
if __name__ == "__main__":
    main()