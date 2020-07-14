import requests
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import sys


def main():
	print("""
		Alabama - AL
		Alaska - AK
		Arizona - AZ
		Arkansas - AR
		California - CA
		Colorado - CO
		Connecticut - CT
		Delaware - DE
		Florida - FL
		Georgia - GA
		Hawaii - HI
		Idaho - ID
		Illinois - IL
		Indiana - IN
		Iowa - IA
		Kansas - KS
		Kentucky - KY
		Louisiana - LA
		Maine - ME
		Maryland - MD
		Massachusetts - MA
		Michigan - MI
		Minnesota - MN
		Mississippi - MS
		Missouri - MO
		Montana - MT
		Nebraska - NE
		Nevada - NV
		New Hampshire - NH
		New Jersey - NJ
		New Mexico - NM
		New York - NY
		North Carolina - NC
		North Dakota - ND
		Ohio - OH
		Oklahoma - OK
		Oregon - OR
		Pennsylvania - PA
		Rhode Island - RI
		South Carolina - SC
		South Dakota - SD
		Tennessee - TN
		Texas - TX
		Utah - UT
		Vermont - VT
		Virginia - VA
		Washington - WA
		West Virginia - WV
		Wisconsin - WI
		Wyoming - WY
		""")

	state_choice_1 = input("\nChoose a state by entering a state abbreviation: ")
	state_choice_2 = input("\nChoose another state by entering a state abbreviation: ")
	state_choice_3 = input("\nChoose one more state by entering a state abbreviation: ")
	if state_choice_1.lower() == state_choice_2.lower() or state_choice_1.lower() == state_choice_3.lower():
		print("\nPlease enter different states.")
	while state_choice_1.lower() == state_choice_2.lower() or state_choice_1.lower() == state_choice_3.lower():
		state_choice_1 = input("\nChoose a state by entering a state abbreviation: ")
		state_choice_2 = input("\nChoose another state by entering a state abbreviation: ")
		state_choice_3 = input("\nChoose one more state by entering a state abbreviation: ")

	url_1 = f'https://covidtracking.com/api/v1/states/{state_choice_1.lower()}/daily.json'
	url_2 = f'https://covidtracking.com/api/v1/states/{state_choice_2.lower()}/daily.json'
	url_3 = f'https://covidtracking.com/api/v1/states/{state_choice_3.lower()}/daily.json'
	r_1 = requests.get(url_1)
	r_2 = requests.get(url_2)
	r_3 = requests.get(url_3)
	if r_1.status_code == 200 and r_2.status_code == 200 and r_3.status_code == 200:
		data_1 = r_1.json()
		data_2 = r_2.json()
		data_3 = r_3.json()
	else:
		print("\nThe API has unavailable data.\n")
		sys.exit(1)

	[dates, deaths_1, deaths_2, deaths_3] = [], [], [], []

	for i in data_1:
		list_date = [i for i in str(i['date'])]
		month = list_date[5]
		month_formatted = ''.join(month)
		day = list_date[6:8]
		day_formatted = ''.join(day)
		date = f"{month_formatted}/{day_formatted}"
		dates.append(date)
		deaths_1.append(i['death'])
	for i in data_2:
		deaths_2.append(i['death'])
	for i in data_3:
		deaths_3.append(i['death'])

	try:
		deaths_1.reverse()
		deaths_2.reverse()
		deaths_3.reverse()
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
		ax.plot(dates, deaths_1, c='red', linewidth=5)
		ax.plot(dates, deaths_2, c='blue', linewidth=5)
		ax.plot(dates, deaths_3, c='green', linewidth=5)
	except ValueError:
		print("""

Sorry, but these three states don't have the same number of available data points.
You can try and graph them individually or use a different combination of states.

""")
		sys.exit(1)
	ax.set_xticks(dates_list)
	fig.autofmt_xdate()
	plt.grid()
	red_patch = mpatches.Patch(color='red', label=f'{state_choice_1.upper()}')
	blue_patch = mpatches.Patch(color='blue', label=f'{state_choice_2.upper()}')
	green_patch = mpatches.Patch(color='green', label=f'{state_choice_3.upper()}')
	plt.legend(handles=[red_patch, blue_patch, green_patch])
	plt.title(f'Number of COVID-19 related deaths in {state_choice_1.upper()}, {state_choice_2.upper()}, and '
			  f'{state_choice_3.upper()} since March 2020\n', fontsize=15)
	plt.xlabel('Date', fontsize=15)
	plt.ylabel('Deaths', fontsize=15)
	plt.tick_params(axis='both', which='major', labelsize='10')
	plt.show()

	again = input("Would you like to graph another state?(y/n) ")
	if again != 'n':
		main()
	else:
		print("\nGoodbye!\n")
		sys.exit()


if __name__ == "__main__":
	main()
