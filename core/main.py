import sys
from etl.landing_to_raw import landing_to_raw
from etl.raw_to_app import raw_to_app

def main(csv,table,json='../db/raw/unknown.json'):

    landing_to_raw(csv,json)
    raw_to_app(table,json)

if __name__ == "__main__":
     if len(sys.argv) == 3:
        main(sys.argv[1],sys.argv[2])
     else:
      # do Y
         main(sys.argv[1],sys.argv[2],sys.argv[3])

     