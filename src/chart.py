import matplotlib.pyplot as plt


def generate_pie_chart(data_labels : list, data : list):
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data_labels, autopct='%1.1f%%',shadow=False, startangle=90)
    ax1.axis('equal')
    plt.show()

generate_pie_chart(["a", "b", "c", "c"], [1, 2, 3, 4])