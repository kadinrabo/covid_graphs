import requests
import matplotlib.pyplot as plt
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

	state_choice = input("\nChoose a state by entering state abbreviation: ")

	url = f'https://covidtracking.com/api/v1/states/{state_choice.lower()}/daily.json'
	r = requests.get(url)
	if r.status_code == 200:
		data = r.json()
	else:
		print("\nThe API has unavailable data.\n")
		sys.exit(1)

	dates, deaths = [], []

	for i in data:
		list_date = [i for i in str(i['date'])]
		month = list_date[5]
		month_formatted = ''.join(month)
		day = list_date[6:8]
		day_formatted = ''.join(day)
		date = f"{month_formatted}/{day_formatted}"
		dates.append(date)
		deaths.append(i['death'])

	try:
		deaths.reverse()
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
	ax.plot(dates, deaths, c='red', linewidth=5)
	ax.set_xticks(dates_list)
	fig.autofmt_xdate()
	plt.grid()
	plt.title(f'Number of COVID-19 related deaths in {state_choice.upper()} since March 2020\n', fontsize=15)
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
