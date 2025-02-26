import matplotlib.pyplot as plt

# Example data
donors = ['John Doe', 'Jane Smith', 'Bob Johnson']
donations = [500, 300, 150]

def plot_donations(donors, donations):
    plt.bar(donors, donations)
    plt.xlabel('Donors')
    plt.ylabel('Donation Amount ($)')
    plt.title('Donations by Donor')
    plt.show()

# Example usage
plot_donations(donors, donations)
