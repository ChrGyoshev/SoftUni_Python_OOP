class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if language == self.language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"


    def change_language(self, new_language, skills_needed):
        if self.language != new_language and self.skills >= skills_needed:
            old_lang = self.language
            self.language = new_language
            return f"{self.name} switched from {old_lang} to {new_language}"

        elif self.language == new_language and self.skills >= skills_needed:
            return f"{self.name} already knows {self.language}"

        else:
            needed_skills = skills_needed - self.skills
            return f"{self.name} needs {needed_skills} more skills"
