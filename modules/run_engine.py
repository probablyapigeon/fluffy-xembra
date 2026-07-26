# ============================================================
# XEMBRA RUN ENGINE — Stable Build
# ============================================================

from xembra import XEMBRA

def main():
    x = XEMBRA()

    print("XEMBRA Engine Online.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = x.talk(user_input)
        print("\nXEMBRA:", response, "\n")


if __name__ == "__main__":
    main()
