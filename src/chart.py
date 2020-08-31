import matplotlib.pyplot as plt


def generate_pie_chart(data_labels : list, data : list, file_name : str):
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data_labels, autopct= lambda p : '{:.2f}%  ({:,.0f})'.format(p,p * sum(data)/100),shadow=False, startangle=90)
    ax1.axis('equal')
    # plt.legend()
    ax1.legend(loc = "best", fancybox=True, framealpha=0.1)
    plt.savefig(file_name +".jpg")