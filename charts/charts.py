import matplotlib.pyplot as plt

def generate_pie_chart():
    """
    It creates a pie chart with the labels and values provided, saves it to a file, and closes the
    figure
    """
    labels = ['A','B','C']
    values = [200,34,120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()



