import bot
import tokens
import discord.member, discord.role


def generate_arrays(members : list):
    sum = 0
    for a in members:
        a : discord.member
        for role in a.roles:
            if role.name == "SoCal":
                print(role)
                sum += 1
    print(sum)


if __name__ == "__main__":
    client = bot.UCSD24StatsBot()
    client.run(tokens.token)
    generate_arrays(client.server_members)
    # print(client.server_members)
