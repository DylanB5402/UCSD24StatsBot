import bot
import tokens
import role_charter


if __name__ == "__main__":
    client = bot.UCSD24StatsBot(688557666779529271)
    client.run(tokens.token)
    charter = role_charter.RoleCharter(client)
    # print(charter.role_number_dict)
    # charter.generate_chart("charts/locations", role_charter.SeparateRoles(["International", "Out of State", "NorCal", "SoCal"]))
    # charter.generate_chart("charts/colleges", role_charter.SeparateRoles(["Warren College", "Muir College", "Marshall College", "Roosevelt College", "Revelle College", "Sixth College", "Seventh College"]))
    # charter.generate_chart("charts/campus", role_charter.SeparateRoles(["On-Campus", "Commuter", "Staying Home for COVID"]))
    # charter.generate_chart("charts/departments", role_charter.SeparateRoles(["Arts and Humanities", "Social Sciences", "Engineering", "Health Sciences", "Physical Sciences", "Scripps Institution of Oceanography", "Biological Sciences"]))
    # charter.gen_portion_of_everyone_chart("charts/cs_majors", role_charter.SeparateRoles(["Computer Science", "Computer Engineering", "Mathematics - Computer Science"]))
    charter.generate_chart("charts/class_level", role_charter.SeparateRoles(["Class of 2024", "boomer", "Guest"]))