import emoji

def main():
    emojiInput = input("Enter text with emoji codes: ").strip()
    print(emoji.emojize(emojiInput, language='alias'))

if __name__ == "__main__":
    main()
