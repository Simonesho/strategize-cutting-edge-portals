    data = generate_random_data()


    for item in data:

        print(f"Random Number: {item}")
if __name__ == "__main__":
    main()

def main():
import random
    data = [random.randint(1, 100) for _ in range(10)]
    return data
def generate_random_data():