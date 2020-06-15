import requests
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import sys


def main():
	print("""
		ALABAMA - AL
		ALASKA - AK
		ARIZONA - AZ
		ARKANSAS - AR
		CALIFORNIA - CA
		COLORADO - CO
		CONNECTICUT - CT
		DELAWARE - DE
		FLORIDA - FL
		GEORGIA - GA
		HAWAII - HI
		IDAHO - ID
		ILLINOIS - IL
		INDIANA - INIOWA - IA
		KANSAS - KS
		KENTUCKY - KY
		LOUISIANA - LA
		MAINE - ME
		MARYLAND - MD
		MASSACHUSETTS - MA
		MICHIGAN - MI
		MINNESOTA - MN
		MISSISSIPPI - MS
		MISSOURI - MO
		MONTANA - MT
		NEBRASKA - NE
		NEVADA - NV
		NEW HAMPSHIRE - NH
		NEW JERSEY - NJ
		NEW MEXICO - NM
		NEW YORK - NY
		NORTH CAROLINA - NC
		NORTH DAKOTA - ND
		OHIO - OH
		OKLAHOMA - OK
		OREGON - OR
		PENNSYLVANIA - PA
		RHODE ISLAND - RI
		SOUTH CAROLINA - SC
		SOUTH DAKOTA - SD
		TENNESSEE - TN
		TEXAS - TX
		UTAH - UT
		VERMONT - VT
		VIRGINIA - VA
		WASHINGTON - WA
		WEST VIRGINIA - WV
		WISCONSIN - WI
		WYOMING - WY
		""")

	state_choice = input("\nCHOOSE A STATE BY ENTERING STATE ABBREVIATION: ")

	url = f'https://covidtracking.com/api/v1/states/{state_choice.lower()}/daily.json'
	r = requests.get(url)
	if r.status_code == 200:
		print("\nGRAPHING...\n")
		print("\n---- SUCCESS! ---- \n")
		data = r.json()
	else:
		print("\n---- ERROR :( ---- \n")
		sys.exit(1)

	dates, hospitalized = [], []
	dates_1, inicu = [], []
	dates_2, recovered = [], []

	for i in data:
		list_date = [i for i in str(i['date'])]
		month = list_date[5]
		month_formatted = ''.join(month)
		day = list_date[6:8]
		day_formatted = ''.join(day)
		date = f"{month_formatted}/{day_formatted}"
		dates.append(date)
		hospitalized.append(i['hospitalizedCurrently'])
		inicu.append(i['inIcuCurrently'])
		recovered.append(i['recovered'])

	try:
		hospitalized.reverse()
		dates.reverse()
		inicu.reverse()
		recovered.reverse()
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
	ax.plot(dates, hospitalized, c='orange', linewidth=5)
	ax.plot(dates, inicu, c='red', linewidth=5)
	ax.plot(dates, recovered, c='blue', linewidth=5)
	ax.set_xticks(dates_list)
	plt.grid()
	blue_patch = mpatches.Patch(color='blue', label='Recovered')
	red_patch = mpatches.Patch(color='red', label='In an ICU')
	orange_patch = mpatches.Patch(color='orange', label='Hospitalized')
	plt.legend(handles=[orange_patch, red_patch, blue_patch])
	plt.title(f'Number of people hospitalized, in ICU, and recovered in {state_choice.upper()} since March 2020\n',
			  fontsize=12)
	plt.xlabel('Date', fontsize=15)
	fig.autofmt_xdate()
	plt.ylabel('Number of people', fontsize=15)
	plt.tick_params(axis='both', which='major', labelsize='10')
	plt.show()


if __name__ == "__main__":
	main()
