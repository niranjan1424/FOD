import matplotlib.pyplot as plt
months = ['January', 'February', 'March', 'April', 'May', 'June']
sales = [10000, 12000, 8000, 15000, 18000, 13000]
def create_line_plot(months, sales):
    plt.plot(months, sales, marker='o', linestyle='-')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Monthly sales data LINE PLOT')
    plt.grid(True)
    plt.show()
create_line_plot(months,sales)

def create_bar_plot(months, sales):
    colors =['#33FF57']
    plt.bar(months, sales,color=colors)
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Monthly Sales Data BAR PLOT')
    plt.grid(True)
    plt.show()
create_bar_plot(months,sales)

