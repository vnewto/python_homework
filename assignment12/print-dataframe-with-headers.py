import pandas as pd

#create a class that inherits from the pandas dataframe class
class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)
    
    #declare a function
    def print_with_headers(self):
        #define start and end points for row numbers
        start = 0 
        end = 10
        for i in range(0, len(self), 10): #loop through rows until the df length is reached, in steps of 10
            print(f"\n{self.iloc[start:end]}\n")
            start +=10
            end +=10

products = DFPlus.from_csv("../csv/products.csv")
DFPlus.print_with_headers(products)