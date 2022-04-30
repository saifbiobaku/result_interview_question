import argparse, datetime
import  xml.etree.ElementTree as ET
from pip import main

infile = "test_payload.xml"
outfile = "test_payload.xml"

def create_parser():
# Build the parser
    parser = argparse.ArgumentParser(description='Update the depature and return datetime')
    parser.add_argument("Xdep", type=int, help="Departure 'Value to be added to current datetime'")
    parser.add_argument("Yret", type=int, help="Return 'Value to be added to the current datetime'")
    arg = parser.parse_args()
    return arg

def get_current_date():
    current_date = datetime.datetime.now()
    date_int = current_date.year*10000000000 + current_date.month * 100000000 \
    + current_date.day * 1000000 + current_date.hour*10000 + current_date.minute*100 + current_date.second 
    return current_date, date_int

def depaturereturn(X, Y):
    tree = ET.parse(infile)
    root = tree.getroot()
    thisdate, intdate = get_current_date()
    
    print(f"The current datetime is {thisdate}")
    print(f"The integer version of datetime is {intdate}")

    for departure in root.iter("depart"):
        newdeparture = int(intdate + X)
        departure.text = str(newdeparture)
        print(departure.text)
        departure.set("update", "yes")

    for arrival in root.iter("return"):
        newreturn = int(intdate + Y)
        arrival.text = str(newreturn)
        print(arrival.text)
        arrival.set("update", "yes")

    tree.write(outfile)

def main():
    args=create_parser()
    #print(args.Xdep, args.Yret)
    depaturereturn(args.Xdep, args.Yret)

if __name__ == "__main__":
    main()