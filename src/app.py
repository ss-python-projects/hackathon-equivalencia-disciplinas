import pandas as pd
from constants import columns
from equivalence import syllabus

import data_channel.input as input_channel
from model.discipline_equivalence import DisciplineEquivalence
from adapter.discipline import Discipline as DisciplineAdapter
from memory.whitelist import Whitelist
from memory.blacklist import Blacklist

def calculate_equivalences(discs_not_offered, discs_offered):
    # The program's "memory" - avoids recalculating unnecessary stuff
    whitelist = Whitelist()
    blacklist = Blacklist()

    # Final equivalences shown to the coordinator
    final_output = pd.DataFrame(columns=[
        "COD_DISCIP_ORIG", "NOME_DISCIP_ORIG", "CARGAH_DISCIP_ORIG", "EMENTA_DISCIP_ORIG",
        "COD_DISCIP_EQUIV", "NOME_DISCIP_EQUIV", "CARGAH_DISCIP_EQUIV", "EMENTA_DISCIP_EQUIV",
        "TIPO_EQUIV"
    ])

    # For each "not offered" discipline, do:
    for i, not_offered in discs_not_offered.iterrows():
        not_offered_discipline = DisciplineAdapter.adapt(not_offered)

        # If equivalences for "not offered" discipline were
        # already calculated (i.e. is whitelisted), then:
        if whitelist.has_any_record(not_offered):

            # Get equivalences and save them into the final result
            final_output.append(
                push_to_final_output(not_offered, whitelist.get_records_for(not_offered)),
                ignore_index=True
            )

        # Otherwise, if equivalences for "not offered" discipline
        # DO NOT exist already, then:
        else:

            # For each "offered" discipline, do:
            for j, offered in discs_offered.iterrows():
                offered_discipline = DisciplineAdapter.adapt(offered)

                # If "offered" discipline is NOT tagged as not equivalent
                # (i.e. is blacklisted), then:
                if not blacklist.has_record(not_offered, offered):

                    # If both disciplines are equivalent by workload and by
                    # course syllabus
                    are_equivalent_by_workload = DisciplineEquivalence.are_equivalent_by_workload(not_offered_discipline, offered_discipline)
                    are_equivalent_by_syllabus = syllabus.similarity(not_offered, offered) > 0.40
                    if (are_equivalent_by_workload and are_equivalent_by_syllabus):
                        whitelist.add_record(not_offered, offered)
                        equivalence_discipline = DisciplineEquivalence(not_offered_discipline, offered_discipline)
                        final_output = final_output.append(equivalence_discipline.serialize(), ignore_index=True)

                    # However, if both disciplines are NOT equivalent
                    else:
                        blacklist.add_record(not_offered, offered)

    return final_output

def main():
    discs_not_offered, discs_offered = input_channel.read_disciplines()
    print(calculate_equivalences(discs_not_offered, discs_offered).head())

if __name__ == '__main__':
    main()
