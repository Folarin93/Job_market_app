from data import Data

colours = {"Black": "\u001b[30m",
"Red": "\u001b[31m",
"Green": "\u001b[32m",
"Yellow": "\u001b[33m",
"Blue": "\u001b[34m",
    "Reset": "\u001b[0m"
}


class Stats:
    
    def __init__(self,name: str ):
        self.name = name
        data_load = Data.load("language_data.json")
        self.data = data_load[self.name]
        self.recent_date = list(self.data.keys())[-1]
        self.today_jobs = list(self.data.values())[-1]
        self.previous_day_jobs = list(self.data.values())[-2]
        self.day_in_month = int(self.recent_date[-5:-3])
        self.table_content = [self.name, self.today_jobs,self.net_change(),self.percent_change(), self.month_percent_change(), self.recent_date]
        
        
        
    def net_change(self) -> str:
        self.net_value = float(self.today_jobs - self.previous_day_jobs)
        if self.net_value < 0:
            return (colours["Red"]+f"{self.net_value}"+colours["Reset"])
        else:
            return (colours["Green"]+f"+ {self.net_value}"+colours["Reset"])
        
    def percent_change(self)-> str:
        self.percentage =(self.net_value/self.today_jobs)*100
        self.percent_net_value = float("{:.2f}".format(self.percentage))
        if self.percent_net_value < 0:
            return (colours["Red"]+f"{self.percent_net_value}%"+colours["Reset"])
        else:
            return (colours["Green"]+f"+{self.percent_net_value}%"+colours["Reset"])
    
    def month_net_change(self):
        try:
            self.recent_month = sum(list(self.data.values())[-self.day_in_month::])/len(list(self.data.values())[-self.day_in_month::])
            prev_30_days = -self.day_in_month - 30
            self.previous_month = sum(list(self.data.values())[prev_30_days:-self.day_in_month])/len(list(self.data.values())[prev_30_days:-self.day_in_month])
            self.month_net_value = self.recent_month - self.previous_month
            return self.month_net_value
        except ZeroDivisionError:
            self.month_net_value = "N/A"
            return self.month_net_value
        
    def month_percent_change(self)-> str:
        self.month_net_change()
        if self.month_net_value == "N/A":
            return self.month_net_value
        else:
            self.month_percentage = (self.month_net_change()/self.recent_month)*100
            self.month_percent_value = float("{:.2f}".format(self.month_percentage))
            if self.month_percent_value < 0:
                return (colours["Red"]+f"{self.month_percent_value}%"+colours["Reset"])
            else:
                return (colours["Green"]+f"+{self.month_percent_value}%"+colours["Reset"])
            
            