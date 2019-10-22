import matplotlib.pyplot as shipplot

goodgps = [40, 50, 60, 70]
badgps = [33, 90, 50, 38]

shipplot.plot(range(1, 5), goodgps, color="blue")
shipplot.plot(range(1, 5), badgps, color="red")
shipplot.legend(["goodgps", "badgps"])
shipplot.xlabel("worth")
shipplot.ylabel("amount")
shipplot.title("How much is the fish?")
shipplot.show() 
# Natura non facit saltus