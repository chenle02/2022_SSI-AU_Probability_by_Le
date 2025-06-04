# Year 2022, Summer Science Institute (SSI) at Auburn University
* June 5-11, 2022

## Attendees

| Name                     | School                                     |
|--------------------------|--------------------------------------------|
| Annabel BakerLoveless    | Academic Magnet Program (LAMP High School) |
| Lily BurfordHewitt       | Trussville High School                     |
| Ben CarnesForsyth        | Central High School                        |
| Laney DruhanLoveless     | Academic Magnet Program (LAMP High School) |
| Ethan FarriorLoveless    | Academic Magnet Program (LAMP High School) |
| Yejin HanLoveless        | Academic Magnet Program High School        |
| Trinity GrantEufaula     | High School                                |
| Serenity GriffinLoveless | Academic Magnet Program (LAMP High School) |
| Dani KimVirgil           | I. Grissom High School                     |
| Shaun PatelHewitt        | Trussville High School                     |
| Anne Stewart             | RogersHewitt Trussville High School        |
| Rex UsryHewitt           | Trussville High School                     |
| Debora VasconcelosAuburn | High School                                |

# An Invitation to Probability
* June 8th, 2022, from 5:30pm -- 6:30pm.
* [Sciences Center Auditorium Building](https://calendar.auburn.edu/sciences_center_auditorium_bldg_603)
* Lecturer: [Le Chen](http://webhome.auburn.edu/~lzc0090/)
* Slides are here [2022_AU-SSI_Invitation_Probability_Le.pdf](./slides/2022_AU-SSI_Invitation_Probability_Le.pdf).

## Procedures
* Each one is assigned an ID number.
* Present the slides.
* Collecting the DOB via the ID number using [sc-im](https://github.com/andmarti1424/sc-im):
```bash
sc-im ./data/DOB.csv
```
* Run [Checking.py](./code/Checking.py) to check the matching DOBs from the class:
```bash
python3 code/Checking.py data/DOB.csv
```
* Run [GenDOB.py](./code/GenDOB.py) to generate random DOBs uniformly distributed in years 2005–2007:
```bash
python3 code/GenDOB.py
```
* Run [BatchTest.py](./code/BatchTest.py) to generate random class data and estimate matching probabilities:
```bash
python3 code/BatchTest.py
```

