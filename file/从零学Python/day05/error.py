if __name__ == "__main__":
    # 异常捕捉
    try:
        result = 8/0
        print(result)
    except Exception as e:
        print("Error")

    # 具体的异常捕捉
    try:
        result = 8/0
        print(result)
    except ValueError as e:
        print("ValueError")

    except ZeroDivisionError as e:
        print("ZeroDivisionError")
    finally:
        print("Finally")