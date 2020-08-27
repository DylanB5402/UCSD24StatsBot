import matplotlib.pyplot as plt


def generate_pie_chart(data_labels : list, data : list, file_name : str):
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data_labels, autopct= lambda p : '{:.2f}%  ({:,.0f})'.format(p,p * sum(data)/100),shadow=False, startangle=90)
    ax1.axis('equal')
    plt.legend()
    plt.savefig(file_name +".jpg")


# generate_pie_chart(["a", "b", "c", "c"], [1, 2, 3, 4], "plot1")
