import matplotlib.pyplot as plt
months = ['January', 'February', 'March', 'April', 'May', 'June','july','august','sep','oct','nov','dec']
temp= [22,35,24, 15, 18, 13,40,41,36,27,37,38]
rain=[3,2,4,3,4,12,13,16,7,8,9,6]
def create_line_plot(months,temp):
    plt.plot(months, temp,marker='o', linestyle='-')
    plt.xlabel('Month')
    plt.ylabel('temp')
    plt.title('Monthly temp data LINE PLOT')
    plt.show()
create_line_plot(months,temp)

def create_scatter_plot(months,temp):
    plt.scatter(months,temp)
    plt.xlabel('Month')
    plt.ylabel('rain')
    plt.title('Monthly temp Data SCATTER PLOT')
    plt.show()
create_scatter_plot(months,rain)
