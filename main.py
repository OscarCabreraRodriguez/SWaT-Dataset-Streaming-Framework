from src.utlis import load_csv

def main():
    print(len(load_csv("./data/SWaT_dataset_Jul 19 v2.xlsx")))


if __name__ == '__main__':
    main()