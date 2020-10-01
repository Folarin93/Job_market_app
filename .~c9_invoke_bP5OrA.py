from languages import list_of_languages
from jobs import Job 

"""For Loop to update Json data file for """
for lang in list_of_languages:
    language = Job(lang)
    language.job_seeker()
    language.data_update_process()
    