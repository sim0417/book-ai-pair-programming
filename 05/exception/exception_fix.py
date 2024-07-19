def main():
    try:
        divisor = 0
        if divisor != 0:
            x = 1 / divisor
        else:
            print("분모가 0입니다. 나눗셈을 수행할 수 없습니다.")
    except Exception as e:
        print("Error", e)

    try:
        my_dict = {"name": "Alice"}
        name = my_dict.get("name")
        if name is None:
            print("The key 'name' does not exist in the dictionary.")

        print("Name : ", name)

    except Exception as e:
        print("Error", e)

    try:
        int(123)
    except Exception as e:
        print("Error", e)


if __name__ == "__main__":
    main()
