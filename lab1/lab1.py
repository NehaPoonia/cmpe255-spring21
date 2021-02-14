import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Solution:
    def __init__(self) -> None:
        # Load data from data/chipotle.tsv file using Pandas library and 
        # assign the dataset to the 'chipo' variable.
        file = 'data/chipotle.tsv'
        self.chipo = pd.read_csv(file, sep='\t')
        print()
    
    def top_x(self, count) -> None:
        # Top x number of entries from the dataset and display as markdown format.
        topx = self.chipo.head(10)
        print(topx.to_markdown())
        
    def count(self) -> int:
        # The number of observations/entries in the dataset.
        return self.chipo.shape[0]
    
    def info(self) -> None:
        print(self.chipo.info())
        pass
    
    def num_column(self) -> int:
        # return the number of columns in the dataset
        return self.chipo.shape[1]
    
    def print_columns(self) -> None:
        #Print the name of all the columns.
        print(self.chipo.columns.values.tolist())
    
    def most_ordered_item(self):
        
        item_name = self.chipo['item_name'].value_counts().idxmax()
        order_id = self.chipo.loc[self.chipo['item_name'] == item_name, 'order_id'].sum()
        quantity = self.chipo.loc[self.chipo['item_name'] == item_name, 'quantity'].sum()
        return item_name, order_id, quantity

    def total_item_orders(self) -> int:
        #  How many items were orderd in total?
        return self.chipo['quantity'].sum()
   
    def total_sales(self) -> float:
        # 1. Create a lambda function to change all item prices to float.
        # 2. Calculate total sales.
        val = self.chipo.item_price.map(lambda x: x.lstrip('$')).astype(float)*self.chipo.quantity
        return val.sum()
   
    def num_orders(self) -> int:
        # How many orders were made in the dataset?
        return len(self.chipo['order_id'].unique())
    
    def average_sales_amount_per_order(self) -> float:
        num_order = len(self.chipo['order_id'].unique())
        val = self.chipo.item_price.map(lambda x: x.lstrip('$')).astype(float) * self.chipo.quantity
        total_sales = val.sum()
        return round(total_sales/num_order, 2)

    def num_different_items_sold(self) -> int:
        # How many different items are sold?
        return len(self.chipo['item_name'].unique())
    
    def plot_histogram_top_x_popular_items(self, x:int) -> None:
        from collections import Counter
        letter_counter = Counter(self.chipo.item_name)
        # TODO

        # 1. convert the dictionary to a DataFrame
        df1 = pd.DataFrame(letter_counter.items(), columns=['Items', 'Number of Orders'])
        # 2. sort the values from the top to the least value and slice the first 5 items
        df2 = df1.sort_values(by=['Number of Orders'], ascending=False).head(x)
        # 3. create a 'bar' plot from the DataFrame
        # 4. set the title and labels:
        #     x: Items
        #     y: Number of Orders
        #     title: Most popular items
        df2.plot.bar(x='Items', y='Number of Orders', title='Most popular items')
        # 5. show the plot. Hint: plt.show(block=True)
        plt.show(block=True)
        
    def scatter_plot_num_items_per_order_price(self) -> None:
      
        # 1. create a list of prices by removing dollar sign and trailing space.
        item_price = self.chipo.item_price.map(lambda x: x.lstrip('$').rstrip()).to_list()
        df = self.chipo
        df['item_price'] = df.apply(lambda x: float(x.item_price.lstrip('$').rstrip()), axis=1)

        def total_price(quantity, item_price):
            item_price = float(item_price.lstrip('$').rstrip())
            # [IMP] uncomment the below line if we take total_price as quantity * item_price
            # return quantity * item_price
            return item_price
        # df['total_price'] = df.apply(lambda x: total_price(x.quantity, x.item_price), axis=1)

        # 2. groupby the orders and sum it.
        df2 = df.groupby(['order_id']).sum()
        # sc = df2.plot(kind='scatter', x='total_price', y='quantity', s=50, c='blue')
        # 3. create a scatter plot:
        sc = df2.plot(kind='scatter', x='item_price', y='quantity', s=50, c='blue')
        #       x: orders' item price
        #       y: orders' quantity
        #       s: 50
        #       c: blue
        # 4. set the title and labels.
        #       title: Numer of items per order price
        plt.title("Numer of items per order price")
        #       x: Order Price
        plt.xlabel("Order Price")
        #       y: Num Items
        plt.ylabel("Num Items")
        plt.show()
    
        

def test() -> None:
    solution = Solution()
    solution.top_x(10)
    count = solution.count()
    print(count)
    assert count == 4622
    solution.info()
    count = solution.num_column()
    assert count == 5
    item_name, order_id, quantity = solution.most_ordered_item()
    assert item_name == 'Chicken Bowl'
    assert order_id == 713926
    # assert quantity == 159
    total = solution.total_item_orders()
    assert total == 4972
    assert 39237.02 == solution.total_sales()
    assert 1834 == solution.num_orders()
    assert 21.39 == solution.average_sales_amount_per_order()
    assert 50 == solution.num_different_items_sold()
    solution.plot_histogram_top_x_popular_items(5)
    solution.scatter_plot_num_items_per_order_price()

    
if __name__ == "__main__":
    # execute only if run as a script
    test()