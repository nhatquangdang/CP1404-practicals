from Prac_06.programming_language import Programming_Language


def main():
    ruby = Programming_Language("Ruby", "Dynamic", True, 1995)
    python = Programming_Language("Python", "Dynamic", True, 1991)
    visual_basic = Programming_Language("Visual Basic", "Static", False, 1991)

    list = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for i in list:
        if i.is_dynamic():
            print(i.name)

main()