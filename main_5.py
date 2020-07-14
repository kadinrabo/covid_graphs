import argparse
import requests
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import sys


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-deaths", action="store_true")
	parser.add_argument("-positive", action="store_true")
	parser.add_argument("-negative", action="store_true")
	parser.add_argument("-tested", action="store_true")
	parser.add_argument("-hospitalized", action="store_true")
	parser.add_argument("-icu", action="store_true")
	parser.add_argument("-recovered", action="store_true")
	args = parser.parse_args()

	if not (
			args.deaths or args.positive or args.negative or args.tested or args.hospitalized or args.icu or args.recovered):
		print("""
-----------------------------------------------------------------------------------------------
>
Here are the statistic options, and their corresponding commands. Run any of them.
Remember, you chose three statistics and 1 state.
>
For example...
Current number of NEGATIVE CASES and POSITIVE CASES and NEGATIVE CASES
-  Command: python3 main_5.py -negative -positive -negative
or
-  Command: python3 main_5.py -positive -negative -negative

As you can see, order doesn't matter for the arguments. Just pick from any of the following
arguments as you form your command. Look above for an example command.

DEATHS-------------    -deaths
POSITIVE CASES-----    -positive
NEGATIVE CASES-----    -negative
TESTED PEOPLE------    -tested    
HOSPITALIZED PEOPLE    -hospitalized
PEOPLE IN THE ICU--    -icu
RECOVERED PEOPLE---    -recovered

-----------------------------------------------------------------------------------------------
""")
		sys.exit()

	state_choice = input("\nChoose a state by entering a state abbreviation: ")
	url = f'https://covidtracking.com/api/v1/states/{state_choice.lower()}/daily.json'
	r = requests.get(url)
	if r.status_code == 200:
		data = r.json()
	else:
		print("\nThe API has unavailable data.\n")
		sys.exit(1)

	stat_dict = ['death', 'positive', 'negative', 'total', 'hospitalized', 'inIcuCurrently', 'recovered']

	labels = {'death': 'Deaths', 'positive': 'Positive Cases', 'negative': 'Negative Cases', 'total': 'Total Tested',
			  'hospitalized': 'Hospitalizations', 'inIcuCurrently': 'In ICU', 'recovered': 'Recoveries'}

	api_heading = []

	if args.deaths:
		api_heading.append(stat_dict[0])
	if args.positive:
		api_heading.append(stat_dict[1])
	if args.negative:
		api_heading.append(stat_dict[2])
	if args.tested:
		api_heading.append(stat_dict[3])
	if args.hospitalized:
		api_heading.append(stat_dict[4])
	if args.icu:
		api_heading.append(stat_dict[5])
	if args.recovered:
		api_heading.append(stat_dict[6])

	dates, stats_1, stats_2, stats_3 = [], [], [], []

	for i in data:
		list_date = [i for i in str(i['date'])]
		month = list_date[5]
		month_formatted = ''.join(month)
		day = list_date[6:8]
		day_formatted = ''.join(day)
		date = f"{month_formatted}/{day_formatted}"
		dates.append(date)
		stats_1.append(i[api_heading[0]])
		stats_2.append(i[api_heading[1]])
		stats_3.append(i[api_heading[2]])
	label_1 = labels[api_heading[0]]
	label_2 = labels[api_heading[1]]
	label_3 = labels[api_heading[2]]

	try:
		stats_1.reverse()
		stats_2.reverse()
		stats_3.reverse()
		dates.reverse()
	except TypeError:
		print("Some data points null.")
	dates_list = []
	for k, v in enumerate(dates):
		if k % 10 == 0:
			dates_list.append(v)
		else:
			dates_list.append("")
	plt.style.use('classic')
	fig, ax = plt.subplots()
	ax.plot(dates, stats_1, c='red', linewidth=5)
	ax.plot(dates, stats_2, c='blue', linewidth=5)
	ax.plot(dates, stats_3, c='green', linewidth=5)
	ax.set_xticks(dates_list)
	fig.autofmt_xdate()
	plt.grid()
	red_patch = mpatches.Patch(color='red', label=label_1)
	blue_patch = mpatches.Patch(color='blue', label=label_2)
	green_patch = mpatches.Patch(color='green', label=label_2)
	plt.legend(handles=[red_patch, blue_patch, green_patch])

	plt.xlabel('Date', fontsize=15)
	plt.ylabel('Quantity', fontsize=15)
	plt.tick_params(axis='both', which='major', labelsize='10')
	plt.show()
	again = input("Would you like to graph another state for the same statistics?(y/n) ")
	if again != 'n':
		print("""
-----------------------------------------------------------------------------------------------
>
Here are the statistic options, and their corresponding commands. Run any of them.
Remember, you chose two statistics and 1 state.
>
For example...
Current number of NEGATIVE CASES and POSITIVE CASES
-  Command: python3 main_4.py -negative -positive
or
-  Command: python3 main_4.py -positive -negative

As you can see, order doesn't matter for the arguments. Just pick from any of the following
arguments as you form your command. Look above for an example command.

DEATHS-------------    -deaths
POSITIVE CASES-----    -positive
NEGATIVE CASES-----    -negative
TESTED PEOPLE------    -tested    
HOSPITALIZED PEOPLE    -hospitalized
PEOPLE IN THE ICU--    -icu
RECOVERED PEOPLE---    -recovered

-----------------------------------------------------------------------------------------------
""")
		main()
	else:
		print("\nGoodbye!\n")
		sys.exit()


if __name__ == "__main__":
	main()
