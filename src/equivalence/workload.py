from constants import columns

###
# Get all disciplines that have the SAME workload.
#
# @todo: make it also consider lower workloads, respecting 
# the rules.
###
def get_equivalents_by_workload(discipline, disciplines):
  return disciplines[disciplines[columns.DISCIPLINE_WORKLOAD] == discipline[columns.DISCIPLINE_WORKLOAD]]
