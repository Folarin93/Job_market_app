from languages import list_of_languages
from jobs import Job 
from tabulate import tabulate
from job_statistics import Stats
    

def presenter():
    table_info = []
    for lang in list_of_languages:
        prog_lang = Stats(lang)
        """Table content creation for each programming lanaguage job market"""
        table_info.append(prog_lang.table_content)

    """Creating table for display"""
    table = tabulate(table_info, headers = ["Name","Today's Job Postings", "Net Change", "% Change","1 Month", "Last Updated"] )
    return (table)


print(presenter())
