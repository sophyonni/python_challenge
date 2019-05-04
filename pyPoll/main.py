import csv
import os
csvpath = os.path.join('election_data.csv')

data = []
list_of_candidates = [] # Only names
candidate_votes = dict()
line = '-------------------------'

# Open the CSV
with open(csvpath) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")
  header = next(csvreader)
  data = list(csvreader)

  total_votes = len(data)

  for record in data:
   candidate = record[2]
   if candidate not in list_of_candidates:
     list_of_candidates.append(candidate)
     
  for record in data:
    voterID, county, name = record
    candidate_votes[name] = candidate_votes.get(name, 0) + 1

  winner = max(candidate_votes, key=candidate_votes.get)

  # Printing
  print('Election Results')
  print(line)
  print('Total Votes: {}'.format(total_votes))
  print(line)

  for name, votes in candidate_votes.items():
    percentage = votes / total_votes * 100
    print('{0}: {1:.3f}% ({2})'.format(name, percentage, votes))
  
  print(line)
  print('Winner: {}'.format(winner))
  print(line)

  
  
  with open("output.txt", 'w') as output:
      # Printing
    file.write('Election Results')
    file.write(line)
    print('Total Votes: {}'.format(total_votes))
    print(line)

    for name, votes in candidate_votes.items():
        percentage = votes / total_votes * 100
        print('{0}: {1:.3f}% ({2})'.format(name, percentage, votes))

    print(line)
    print('Winner: {}'.format(winner))
    print(line)

