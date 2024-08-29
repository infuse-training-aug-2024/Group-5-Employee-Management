class Performance:
    def __init__(self,employee_id: int, behaviour: int, team_colloboration: int, verbal_skills: int, critical_thinking: int, emotional_intel:int):
        self.behaviour = behaviour
        self.team_colloboration = team_colloboration
        self.verbal_skills = verbal_skills
        self.critical_thinking=critical_thinking
        self.emotional_intel = emotional_intel
        self.average=0

    def get_performance_avg(self):
        self.average=(self.behaviour+self.critical_thinking+self.emotional_intel+self.team_colloboration+self.verbal_skills)/5
        

