import pandas as pd
import input_reader
from constants import columns
from memory import whitelist, blacklist
from equivalence import workload, syllabus

def add_to_final_output(discipline, equivalence, equivalence_type):
    final_output = pd.DataFrame(columns=[
        columns.DISCIPLINE_NAME,
        columns.DISCIPLINE_WORKLOAD,
        columns.EQUIVALENT_DISCIPLINE_NAME,
        columns.EQUIVALENT_DISCIPLINE_WORKLOAD,
        columns.EQUIVALENCE_TYPE,
    ])

    final_output = final_output.append({
        columns.DISCIPLINE_NAME: discipline[columns.DISCIPLINE_NAME],
        columns.DISCIPLINE_WORKLOAD: discipline[columns.DISCIPLINE_WORKLOAD],
        columns.EQUIVALENT_DISCIPLINE_NAME: equivalence[columns.DISCIPLINE_NAME],
        columns.EQUIVALENT_DISCIPLINE_WORKLOAD: equivalence[columns.DISCIPLINE_WORKLOAD],
        columns.EQUIVALENCE_TYPE: equivalence_type,
    }, ignore_index=True)

    return final_output

def push_to_final_output(discipline, equivalences):
    final_output = pd.DataFrame(columns=[
        columns.DISCIPLINE_NAME,
        columns.DISCIPLINE_WORKLOAD,
        columns.EQUIVALENT_DISCIPLINE_NAME,
        columns.EQUIVALENT_DISCIPLINE_WORKLOAD,
        columns.EQUIVALENCE_TYPE,
    ])

    for i, equivalence in equivalences.iterrows():
        final_output = final_output.append({
            columns.DISCIPLINE_NAME: discipline[columns.DISCIPLINE_NAME],
            columns.DISCIPLINE_WORKLOAD: discipline[columns.DISCIPLINE_WORKLOAD],
            columns.EQUIVALENT_DISCIPLINE_NAME: equivalence[columns.DISCIPLINE_NAME],
            columns.EQUIVALENT_DISCIPLINE_WORKLOAD: equivalence[columns.DISCIPLINE_WORKLOAD],
            columns.EQUIVALENCE_TYPE: equivalence[columns.EQUIVALENCE_TYPE],
        }, ignore_index=True)

    return final_output

def main():
    # Read both "offered" and "not offered" disciplines
    discs_not_offered, discs_offered = input_reader.read_disciplines()

    # Final equivalences shown to the coordinator
    final_output = pd.DataFrame(columns=[
        columns.DISCIPLINE_NAME,
        columns.DISCIPLINE_WORKLOAD,
        columns.EQUIVALENT_DISCIPLINE_NAME,
        columns.EQUIVALENT_DISCIPLINE_WORKLOAD,
        columns.EQUIVALENCE_TYPE,
    ])

    # For each "not offered" discipline, do:
    for i, not_offered in discs_not_offered.iterrows():

        # If equivalences for "not offered" discipline were 
        # already calculated (i.e. is whitelisted), then:
        if whitelist.has_equivalences(not_offered):

            # Get equivalences and save them into the final result
            final_output.append(
                push_to_final_output(not_offered, whitelist.get_equivalences(not_offered)),
                ignore_index=True
            )
        
        # Otherwise, if equivalences for "not offered" discipline 
        # DO NOT exist already, then:
        else:

            # For each "offered" discipline, do:
            for j, offered in discs_offered.iterrows():

                # If "offered" discipline is already tagged as not equivalent 
                # (i.e. is blacklisted), then:
                if not blacklist.is_not_equivalent(not_offered, offered):
                    workload_diff = workload.difference(not_offered, offered)
                    
                    # Check "equivalence type" based on difference between 
                    # workloads
                    equivalence_type = 0
                    if workload_diff >= 0.75:
                        equivalence_type = 1
                    elif workload_diff >= 0.6 and workload_diff < 0.75:
                        equivalence_type = 2
                    
                    # If both disciplines are equivalent by workload and by 
                    # course syllabus
                    if equivalence_type > 0 and syllabus.similarity(not_offered, offered) > 0.40:
                        whitelist.add(not_offered, offered)
                        final_output.append(
                            add_to_final_output(not_offered, offered, equivalence_type),
                            ignore_index=True
                        )

                    # However, if both disciplines are NOT equivalent
                    else:
                        blacklist.add(not_offered, offered)

    print(final_output.head())

if __name__ == '__main__':
    main()
