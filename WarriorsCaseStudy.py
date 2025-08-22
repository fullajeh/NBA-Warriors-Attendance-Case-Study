import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.patches as mpatches

#Jehlyen Fuller, 8/22/2025

data = {
	
'Year':[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
'Ticket Sales':[41000000, 31000000, 50000000, 55000000, 77000000, 134000000, 143000000, 164000000, 178000000, 150000000, 7000000],
'Extra Income':[22200000, 29100000, 43000000, 44900000, 57700000, 74200000, 120000000, 103000000, 109000000, 200000000, 205000000],
'Revenue':[139000000,127000000, 160000000, 168000000, 201000000, 305000000, 359000000,
401000000, 440000000, 474000000, 258000000],
'Attendance':[14380, 14633, 15024, 19596, 19596, 19596, 19596, 19596, 19596, 19596, 18064],
'Win Percentage':[0.439, 0.348, 0.573, 0.622, 0.817, 0.890, 0.817, 0.707, 0.695, 0.231, 0.542],
'Made Playoffs':[False, False, True, True, True, True, True, True, True, False, True]
}

#Financial Data Pulled from: https://www.statista.com/statistics/196716/revenue-of-the-golden-state-warriors-since-2006/
#Win Percentage and Playoff Data from Google AI

warriors_data = pd.DataFrame(data)

#Make the Console fit all our Data
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

#Lets add a profits column that takes the warrior's extra income and ticket sales divided by the revenue
warriors_data['Profits'] = warriors_data[['Revenue', 'Ticket Sales', 'Extra Income']].sum(axis=1) - warriors_data['Revenue']
print(warriors_data)

#Let's generate a chart for attendance per year, color coded by winning seasons
#Set axis values to reduce redundant coding
sorted_percentage = warriors_data.sort_values(by='Win Percentage', ascending=False)
attendence_x = sorted_percentage['Year']
attendence_y = sorted_percentage['Attendance']

#Set the colors based on winning seasons (making the playoffs)
win_pct_colors = []

for years in range(0, len(attendence_x)):
	for win_pct in sorted_percentage['Made Playoffs']:
		if win_pct: #If it's set to true, they made the playoffs
			win_pct_colors.append("#FFD700")
		else:
			win_pct_colors.append('#002366')

# Create custom legend handles
made_playoffs_patch = mpatches.Patch(color='#FFD700', label='Made Playoffs')
missed_playoffs_patch = mpatches.Patch(color='#002366', label='Missed Playoffs')
average_attendance_patch = mpatches.Patch(color='gray', label='Average Attendance')

# Set a Comparison line for the Warrior's Average Attendance
average_attendance = attendence_y.mean()

#Bar Chart Settings
plt.figure(figsize=(7,6))
plt.ylim(12_000, ymax=attendence_y.max() * 1.05)
plt.xticks(attendence_x, rotation=30)
plt.title("Does Making the Playoffs Influence Golden State Warriors' Attendance?")
plt.xlabel("Warriors NBA Seasons")
plt.ylabel("Home Game Attendance")
plt.bar(attendence_x, attendence_y, color=win_pct_colors, edgecolor='black')
plt.axhline(y=average_attendance, color='gray', linewidth=2, linestyle='--', label=f"Average Attendance({(average_attendance)})")
plt.legend(handles=[made_playoffs_patch, average_attendance_patch, missed_playoffs_patch])

plt.figtext(0.5, 0.5, "Jehlyen Fuller",
          fontsize=40, color="gray",
          ha="center", va="center",
          alpha=0.25, rotation=30)

#################################################################

#Lets make a Line Chart For Profits over the Years.
def millions_formatter(x, pos):
    return f'{x * 1e-6:.1f}M' # Formats to one decimal place with 'M' suffix

fig, ax = plt.subplots(figsize=(7,6))
formatter = FuncFormatter(millions_formatter)
ax.yaxis.set_major_formatter(formatter)


#Lets sort for the highest profits first
highest_profit_years = warriors_data[['Year','Profits']].sort_values(by="Profits", ascending=False)

#Lets format the Y values so the millions aren't cut-off


# X and Y Variables for Less Redundant Coding
line_x = highest_profit_years['Year']
line_y = highest_profit_years['Profits']
plt.ylim(ymin=line_y.min(), ymax=line_y.max() * 1.06)
plt.xticks(line_x, rotation=30)
plt.xlabel("NBA Seasons")
plt.ylabel("Warriors Profits (USD)")
plt.title("Warriors' Most Profitable Years")
plt.grid(True, linestyle='--', alpha=0.8)

# Key annotations
plt.annotate("2015: First Championship",
             xy=(2015, 210000000), xytext=(2012, 250000000),
             arrowprops=dict(facecolor='black', arrowstyle="->"))

plt.annotate("2017-18: Dynasty Peak",
             xy=(2018, 290000000), xytext=(2014, 320000000),
             arrowprops=dict(facecolor='black', arrowstyle="->"))

plt.annotate("2019: New Arena",
             xy=(2019, 350000000), xytext=(2014, 340000000),
             arrowprops=dict(facecolor='black', arrowstyle="->"))

plt.annotate("2020: Injuries & COVID",
             xy=(2020, 210000000), xytext=(2017, 230000000),
             arrowprops=dict(facecolor='black', arrowstyle="->"))


plt.plot(line_x, line_y, marker='o', color="#FFD700")

plt.figtext(0.5, 0.5, "Jehlyen Fuller",
          fontsize=40, color="gray",
          ha="center", va="center",
          alpha=0.25, rotation=30)


plt.show()