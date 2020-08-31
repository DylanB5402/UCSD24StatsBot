import bot
import chart


class SumRoles:
    """A class for roles which are meant to be added together for a chart"""

    def __init__(self, roles: list, name = "" ):
        self.roles = roles
        if name == "":
            for r in roles:
                name += (r + "/")
        self.name = name


class SeparateRoles:
    """A class for roles which should be displayed separately in a chart`"""

    def __init__(self, roles: list):
        self.roles = roles


class RoleCharter():

    def __init__(self, discord_bot: bot.UCSD24StatsBot):
        self.members = discord_bot.server_members
        self.role_list = discord_bot.server_roles
        self.role_number_dict = {}
        self.init_role_dict()
        self.identify_role_amounts()

    def init_role_dict(self):
        for r in self.role_list:
            self.role_number_dict.update({r.name: 0})

    def identify_role_amounts(self):
        for server_member in self.members:
            for r in self.role_list:
                if r in server_member.roles:
                    self.role_number_dict[r.name] += 1

    def get_roles_sum(self, sum_roles: SumRoles):
        a = 0
        for x in sum_roles.roles:
            a += self.role_number_dict[x]
        return a

    def generate_chart(self, file_name : str, sep_roles: SeparateRoles, *argv: SumRoles):
        data_list = []
        label_list = []
        s: SumRoles
        for role_name in sep_roles.roles:
            data_list.append(self.role_number_dict[role_name])
            label_list.append(role_name)
        for s in argv:
            data_list.append(self.get_roles_sum(s))
            label_list.append(s.name)
        chart.generate_pie_chart(label_list, data_list, file_name)

    def gen_portion_of_everyone_chart(self, file_name : str, sep_roles: SeparateRoles):
        data_list = []
        label_list = []
        role_sum = 0
        for role_name in sep_roles.roles:
            data_list.append(self.role_number_dict[role_name])
            label_list.append(role_name)
            role_sum += self.role_number_dict[role_name]
        data_list.append(self.role_number_dict["@everyone"] - role_sum)
        label_list.append("the rest of the server")
        chart.generate_pie_chart(label_list, data_list, file_name)