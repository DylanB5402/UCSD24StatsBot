import bot
import tokens
import role_charter

# def generate_arrays(members : list):
#     sum = 0
#     for a in members:
#         a : discord.member
#         for role in a.roles:
#             if role.name == "SoCal":
#                 print(role)
#                 sum += 1
#     print(sum)


if __name__ == "__main__":
    client = bot.UCSD24StatsBot(688557666779529271)
    client.run(tokens.token)
    charter = role_charter.RoleCharter(client)
    print(charter.role_number_dict)
    # charter.get_roles_sum(role_charter.SumRoles(["@everyone", "UnoBot"]))
    charter.generate_chart(role_charter.SeparateRoles(["He/Him", "She/Her"]), role_charter.SumRoles(["@everyone", "UnoBot"]))
