import pandas as pd
from constants import columns

###
# Read the disciplines - both offered and not offered
###
def read_disciplines():
  disciplines = pd.read_csv("../assets/disciplines.csv")
  disciplines = disciplines[[columns.DISCIPLINE_NAME, columns.DISCIPLINE_WORKLOAD]]

  # @todo: make both offered and non-offered disciplines be 
  # loaded from the correct files, rather than reading only 
  # the same file
  disciplines_not_offered = data[:5]
  disciplines_offered = data[5:40]

  return disciplines_not_offered, disciplines_offered

###
# Run the program's main logic
###
def run():
  disciplines_not_offered, disciplines_offered = read_disciplines()
  calculated_equivalences = pd.DataFrame(columns=[
    columns.DISCIPLINE_NAME,
    columns.DISCIPLINE_WORKLOAD,
    columns.EQUIVALENT_DISCIPLINE_NAME,
    columns.EQUIVALENT_DISCIPLINE_WORKLOAD,
    columns.EQUIVALENCE_TYPE,
  ])

  for i, disc_not_offered in disciplines_not_offered.iterrows():
    if has_calculated_equivalences(disc_not_offered):
      equivalences = get_calculated_equivalences(disc_not_offered)
      save_equivalences(equivalences) # should add it to a list (maybe a DataFrame)
    else:
      for j, disc_offered in disciplines_offered.iterrows():
        equivalence_type = 0 # not equivalent
        equivalence_difference = get_workloads_difference(disc_not_offered, disc_offered)
        
        if  equivalence_difference >= 0.75:
          equivalence_type = 1 # directly equivalent
        else if equivalence_difference >= 0.6 and equivalence_difference < 0.75
          equivalence_type = 2 # equivalent with complementary work

        if equivalence_type > 0: 
          syllabus_similarity = get_syllabus_similarity(disc_not_offered, disc_offered)

          if syllabus_similarity > 0.75:
            # @todo: add discipline in the whitelist
            
            calculated_equivalences = calculated_equivalences.append({
              columns.DISCIPLINE_NAME: disc_not_offered[columns.DISCIPLINE_NAME],
              columns.DISCIPLINE_WORKLOAD: disc_not_offered[columns.DISCIPLINE_WORKLOAD],
              columns.EQUIVALENT_DISCIPLINE_NAME: disc_offered[columns.DISCIPLINE_NAME]
              columns.EQUIVALENT_DISCIPLINE_WORKLOAD: disc_offered[columns.DISCIPLINE_WORKLOAD],
              columns.EQUIVALENCE_TYPE: equivalence_type,
            })
        
        else
          # @todo: add discipline in the backlist

# Run the application
run()


