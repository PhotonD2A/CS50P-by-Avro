def main():
    amount_due = 50
    print(f"Amount due: {amount_due}")

    while amount_due > 0:
        coin = int(input("Insert coin: "))

        if coin in [25, 10, 5]:
            amount_due -= coin
            if amount_due > 0:
                print(f"Amount due: {amount_due}")
        else:
            print(f"Amount due: {amount_due}")

    print(f"Change owed: {abs(amount_due)}")

if __name__ == "__main__":
    main()
