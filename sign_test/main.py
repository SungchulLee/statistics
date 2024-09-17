from load_data import load_data
from model import sign_test

def main():
    paired_data = load_data()
    z, p_value = sign_test(paired_data)
    print(f"{z       = }")
    print(f"{p_value = }")

if __name__ == "__main__":
    main()