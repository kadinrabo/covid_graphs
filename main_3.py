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
Remember, you chose one statistic and three state.
>
For example...
Current number of NEGATIVE CASES
-  Command: python3 main_3.py -negative

Pick from any of the following arguments as you form your command. Look above for an example command.

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
	state_choice_1 = input("\nChoose another state by entering a state abbreviation: ")
	state_choice_2 = input("\nChoose one more state by entering a state abbreviation: ")
	url = f'https://covidtracking.com/api/v1/states/{state_choice.lower()}/daily.json'
	url_1 = f'https://covidtracking.com/api/v1/states/{state_choice_1.lower()}/daily.json'
	url_2 = f'https://covidtracking.com/api/v1/states/{state_choice_2.lower()}/daily.json'
	r = requests.get(url)
	r_1 = requests.get(url_1)
	r_2 = requests.get(url_2)
	if r.status_code == 200 and r_1.status_code == 200 and r_2.status_code == 200:
		data = r.json()
		data_1 = r_1.json()
		data_2 = r_2.json()
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

	label = labels[api_heading[0]]

	dates, stat_1, stat_2, stat_3 = [], [], [], []

	for i in data:
		list_date = [i for i in str(i['date'])]
		month = list_date[5]
		month_formatted = ''.join(month)
		day = list_date[6:8]
		day_formatted = ''.join(day)
		date = f"{month_formatted}/{day_formatted}"
		dates.append(date)
		stat_1.append(i[api_heading[0]])
	for i in data_1:
		stat_2.append(i[api_heading[0]])
	for i in data_2:
		stat_3.append(i[api_heading[0]])

	try:
		stat_1.reverse()
		stat_2.reverse()
		stat_3.reverse()
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
	try:
		ax.plot(dates, stat_1, c='red', linewidth=5)
		ax.plot(dates, stat_2, c='blue', linewidth=5)
		ax.plot(dates, stat_3, c='green', linewidth=5)
	except ValueError:
		print("""

Sorry, but there was an error graphing the data you chose. 
You can try and graph the data individually.

""")
		sys.exit(1)
	ax.set_xticks(dates_list)
	fig.autofmt_xdate()
	plt.grid()
	red_patch = mpatches.Patch(color='red', label=f'{state_choice.upper()}')
	blue_patch = mpatches.Patch(color='blue', label=f'{state_choice_1.upper()}')
	green_patch = mpatches.Patch(color='green', label=f'{state_choice_2.upper()}')
	plt.legend(handles=[red_patch, blue_patch, green_patch])
	plt.title(f'Current number of COVID-19 related {label} in {state_choice.upper()} and {state_choice_1.upper()} and '
			  f'{state_choice_2.upper()} since March 2020.\n')
	plt.xlabel('Date', fontsize=15)
	plt.ylabel('Quantity', fontsize=15)
	plt.tick_params(axis='both', which='major', labelsize='10')
	plt.show()
	again = input("Again?(y/n) ")
	if again != 'n':
		print("""
-----------------------------------------------------------------------------------------------
>
Here are the statistic options, and their corresponding commands. Run any of them.
Remember, you chose one statistic and three states.
>
For example...
Current number of NEGATIVE CASES
-  Command: python3 main_1.py -negative

Pick from any of the following arguments as you form your command. Look above for an example command.

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
