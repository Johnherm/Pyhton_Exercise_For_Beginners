import argparse
def right_pyramid(n):
    for raw in range(1, n+1):
        start_index = (n-raw)
        print(""*start_index, end = "")
        for star in range(raw):
            print("*", end="")

        print("")
right_pyramid(10)