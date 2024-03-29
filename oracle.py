
import discord
from discord.ext import commands
from discord.ui import Button, View, Select, Modal, TextInput
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

GUILD_ID = 1114571314334806066

CANDOR_CHANNEL_ID = 1150957415802621952
TIME_CHANNEL_ID = 1128498231140159600
TRANQUILITY_CHANNEL_ID = 1133557148224344074
GENESIS_CHANNEL_ID = 1133557281343160390
THE_FINAL_JOURNEY_CHANNEL_ID = 1142982664769511476
VICTORY_CHANNEL_ID = 1142982804154630314
TIME_ROLE_ID = 1154056938976464926
THE_FINAL_JOURNEY_ROLE_ID = 1154057034430414898
TRANQUILITY_ROLE_ID = 1154057162725806090
GENESIS_ROLE_ID = 1154057225468379227
VICTORY_ROLE_ID = 1154073980236480644
ATTEMPT_1_ROLE_ID = 1154058423319670784
ATTEMPT_2_ROLE_ID = 1154058474842488862
ATTEMPT_3_ROLE_ID = 1154058507503546458
ATTEMPT_4_ROLE_ID = 1154058536163217459
ATTEMPT_5_ROLE_ID = 1154058567205261322
ATTEMPT_6_ROLE_ID = 1207776099090571284
ATTEMPT_7_ROLE_ID = 1207776157605564457
ATTEMPT_8_ROLE_ID = 1207776188379037736
ATTEMPT_9_ROLE_ID = 1207776209555951730
ATTEMPT_10_ROLE_ID = 1207776231978704947
ATTEMPT_11_ROLE_ID = 1207776254904770670
ATTEMPT_12_ROLE_ID = 1207776281924468776
ATTEMPT_13_ROLE_ID = 1207776314778591324
ATTEMPT_14_ROLE_ID = 1207776343425687583
ATTEMPT_15_ROLE_ID = 1207776368591638628
ATTEMPT_16_ROLE_ID = 1207776395770601593
ATTEMPT_17_ROLE_ID = 1207776418704924696
ATTEMPT_18_ROLE_ID = 1207776450594218087
ATTEMPT_19_ROLE_ID = 1207776477332897814
ATTEMPT_20_ROLE_ID = 1207776500573544488
ATTEMPT_21_ROLE_ID = 1207776526716633098
ATTEMPT_22_ROLE_ID = 1207776550460854332
ATTEMPT_23_ROLE_ID = 1207776574095761521
ATTEMPT_24_ROLE_ID = 1207776602428276806
ATTEMPT_25_ROLE_ID = 1207776626197135460

role_reset_loop = False

attempt_roles = [
            ATTEMPT_1_ROLE_ID, ATTEMPT_2_ROLE_ID, ATTEMPT_3_ROLE_ID,
            ATTEMPT_4_ROLE_ID, ATTEMPT_5_ROLE_ID, ATTEMPT_6_ROLE_ID,
            ATTEMPT_7_ROLE_ID, ATTEMPT_8_ROLE_ID, ATTEMPT_9_ROLE_ID,
            ATTEMPT_10_ROLE_ID, ATTEMPT_11_ROLE_ID, ATTEMPT_12_ROLE_ID,
            ATTEMPT_13_ROLE_ID, ATTEMPT_14_ROLE_ID, ATTEMPT_15_ROLE_ID,
            ATTEMPT_16_ROLE_ID, ATTEMPT_17_ROLE_ID, ATTEMPT_18_ROLE_ID,
            ATTEMPT_19_ROLE_ID, ATTEMPT_20_ROLE_ID, ATTEMPT_21_ROLE_ID,
            ATTEMPT_22_ROLE_ID, ATTEMPT_23_ROLE_ID, ATTEMPT_24_ROLE_ID,
            ATTEMPT_25_ROLE_ID
        ]


# Set up the bot with the proper intents to read message content and reactions
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, id = GUILD_ID)
    candor_channel = discord.utils.get(guild.channels, id=CANDOR_CHANNEL_ID)
    time_channel = discord.utils.get(guild.channels, id=TIME_CHANNEL_ID)
    tranquility_channel = discord.utils.get(guild.channels, id=TRANQUILITY_CHANNEL_ID)
    genesis_channel = discord.utils.get(guild.channels, id=GENESIS_CHANNEL_ID)
    the_final_journey_channel = discord.utils.get(guild.channels, id=THE_FINAL_JOURNEY_CHANNEL_ID)
    global role_reset_loop
    
     # Delete messages posted by the bot
    async for message in candor_channel.history():
        if message.author == bot.user:
            await message.delete()

    # Post a new message with the button
    await candor_channel.send(view=TeamNameView())

     # Delete messages posted by the bot
    async for message in time_channel.history():
        if message.author == bot.user:
            await message.delete()

    # Post a new message with the button
    await time_channel.send(view=TimeView())

    # Delete messages posted by the bot
    async for message in tranquility_channel.history():
        if message.author == bot.user:
            await message.delete()

    # Post a new message with the button
    await tranquility_channel.send(view=TranquilityView())

    # Delete messages posted by the bot
    async for message in genesis_channel.history():
        if message.author == bot.user:
            await message.delete()

    # Post a new message with the button
    await genesis_channel.send(view=GenesisView())

    # Delete messages posted by the bot
    async for message in the_final_journey_channel.history():
        if message.author == bot.user:
            await message.delete()

    # Post a new message with the button
    await the_final_journey_channel.send(view=TheFinalJourneyView())

    if not role_reset_loop:
        role_reset_loop = True
        await role_reset()

async def role_reset():
    while True:
        guild = discord.utils.get(bot.guilds, id = GUILD_ID)
        attempt_25_role = discord.utils.get(guild.roles, id=ATTEMPT_25_ROLE_ID)

        for member in guild.members:
            # Check if the member has the role
            if attempt_25_role in member.roles:
                try:
                    # Remove the role from the member
                    await member.remove_roles(attempt_25_role)
                    print(f"Removed role from {member}")
                except discord.HTTPException as e:
                    # If something goes wrong, print the error
                    print(f"Failed to remove role from {member}: {e}")
        await asyncio.sleep(1800)

class TeamNameModal(Modal, title="Enter Your Team Name"):
    team_name_input = TextInput(placeholder="Team Name", custom_id="team_name_input", label="Input Your Team Name")

    async def on_submit(self, interaction: discord.Interaction):
        team_name = self.children[0].value
        guild = interaction.guild

        # Check if a role with the given name exists (case-insensitive)
        role = discord.utils.find(lambda r: r.name.lower() == team_name.lower(), guild.roles)

        # If the role doesn't exist, create it
        if role is None:
            role = await guild.create_role(name=team_name)

        # Assign the role to the user
        await interaction.user.add_roles(role)

        # Send a confirmation message
        await interaction.response.send_message(f"You have joined {team_name}!", ephemeral=True)

        # Assign Time role
        time_role = discord.utils.get(guild.roles, id=TIME_ROLE_ID)
        await interaction.user.add_roles(time_role)       

class TeamNameView(View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label="Enter Your Team Name", style=discord.ButtonStyle.primary, custom_id="enter_team_name")
    async def enter_team_name(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = TeamNameModal()
        await interaction.response.send_modal(modal)


class TimePassphraseModal(Modal, title="Enter the Passphrase"):
    passphrase_input = TextInput(placeholder="Passphrase", custom_id="passphrase_input", label="Input the Passphrase")

    async def on_submit(self, interaction: discord.Interaction):
        entered_passphrase = self.children[0].value
        correct_passphrase = "ethlizards"
        user = interaction.user
        guild = interaction.guild

        if entered_passphrase == correct_passphrase:
            # Remove Time role and assign Tranquility role
            time_role = discord.utils.get(guild.roles, id=TIME_ROLE_ID)
            tranquility_role = discord.utils.get(guild.roles, id=TRANQUILITY_ROLE_ID)

            await interaction.response.send_message("You have submitted the correct passphrase! The next part of your journey has been made available to you.", ephemeral=True)

            await user.add_roles(tranquility_role)

            # Remove any attempt roles
            for role_id in attempt_roles:
                role = discord.utils.get(guild.roles, id=role_id)
                await user.remove_roles(role)

            await asyncio.sleep(10)

            await user.remove_roles(time_role)
        else:
            await interaction.response.send_message("That passphrase is not correct.", ephemeral=True)
            # Assign the next attempt role
            for i, role_id in enumerate(attempt_roles):
                role = discord.utils.get(guild.roles, id=role_id)
                if role in user.roles:
                    await user.remove_roles(role)
                    if i < len(attempt_roles) - 1:
                        next_role = discord.utils.get(guild.roles, id=attempt_roles[i+1])
                        await user.add_roles(next_role)
                        break
            else:
                first_attempt_role = discord.utils.get(guild.roles, id=ATTEMPT_1_ROLE_ID)
                await user.add_roles(first_attempt_role)

class TimeView(View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label="Enter the Passphrase", style=discord.ButtonStyle.primary, custom_id="enter_passphrase")
    async def enter_passphrase(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user
        guild = interaction.guild
        attempt_25_role = discord.utils.get(guild.roles, id=ATTEMPT_25_ROLE_ID)

        # Check if the user has the ATTEMPT_25_ROLE_ID
        if attempt_25_role in user.roles:
            await interaction.response.send_message("You have tried too many times. You may try again in 30 minutes (your '25 Attempts' role will be automatically removed at that time).", ephemeral=True)
            return

        modal = TimePassphraseModal()
        await interaction.response.send_modal(modal)

class TranquilityPassphraseModal(Modal, title="Enter the Passphrase"):
    passphrase_input = TextInput(placeholder="Passphrase", custom_id="passphrase_input", label="Input the Passphrase")

    async def on_submit(self, interaction: discord.Interaction):
        entered_passphrase = self.children[0].value
        correct_passphrase = "411"
        user = interaction.user
        guild = interaction.guild

        if entered_passphrase == correct_passphrase:

            await interaction.response.send_message("You have submitted the correct passphrase! The next part of your journey has been made available to you.", ephemeral=True)

            # Assign Genesis role
            tranquility_role = discord.utils.get(guild.roles, id=TRANQUILITY_ROLE_ID)
            genesis_role = discord.utils.get(guild.roles, id=GENESIS_ROLE_ID)
            await user.add_roles(genesis_role)

            # Remove any attempt roles
            for role_id in attempt_roles:
                role = discord.utils.get(guild.roles, id=role_id)
                await user.remove_roles(role)

            await asyncio.sleep(10)

            await user.remove_roles(tranquility_role)
        else:
            await interaction.response.send_message("That passphrase is not correct.", ephemeral=True)
            # Assign the next attempt role
            for i, role_id in enumerate(attempt_roles):
                role = discord.utils.get(guild.roles, id=role_id)
                if role in user.roles:
                    await user.remove_roles(role)
                    if i < len(attempt_roles) - 1:
                        next_role = discord.utils.get(guild.roles, id=attempt_roles[i+1])
                        await user.add_roles(next_role)
                        break
            else:
                first_attempt_role = discord.utils.get(guild.roles, id=ATTEMPT_1_ROLE_ID)
                await user.add_roles(first_attempt_role)

class TranquilityView(View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label="Enter the Passphrase", style=discord.ButtonStyle.primary, custom_id="enter_passphrase_tranquility")
    async def enter_passphrase(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user
        guild = interaction.guild
        attempt_25_role = discord.utils.get(guild.roles, id=ATTEMPT_25_ROLE_ID)

        # Check if the user has the ATTEMPT_25_ROLE_ID
        if attempt_25_role in user.roles:
            await interaction.response.send_message("You have tried too many times. You may try again in 30 minutes (your '25 Attempts' role will be automatically removed at that time).", ephemeral=True)
            return

        modal = TranquilityPassphraseModal()
        await interaction.response.send_modal(modal)

class GenesisPassphraseModal(Modal, title="Enter the Passphrase"):
    passphrase_input = TextInput(placeholder="Passphrase", custom_id="passphrase_input", label="Input the Passphrase")

    async def on_submit(self, interaction: discord.Interaction):
        entered_passphrase = self.children[0].value
        correct_passphrase = "2.71511"
        user = interaction.user
        guild = interaction.guild

        if entered_passphrase == correct_passphrase:
            await interaction.response.send_message("You have submitted the correct passphrase! The next part of your journey has been made available to you.", ephemeral=True)
            # Assign The Final Journey role
            genesis_role = discord.utils.get(guild.roles, id=GENESIS_ROLE_ID)
            the_final_journey_role = discord.utils.get(guild.roles, id=THE_FINAL_JOURNEY_ROLE_ID)
            await user.add_roles(the_final_journey_role)

            # Remove any attempt roles
            for role_id in attempt_roles:
                role = discord.utils.get(guild.roles, id=role_id)
                await user.remove_roles(role)

            await asyncio.sleep(10)

            await user.remove_roles(genesis_role)
        else:
            await interaction.response.send_message("That passphrase is not correct.", ephemeral=True)
            # Assign the next attempt role
            for i, role_id in enumerate(attempt_roles):
                role = discord.utils.get(guild.roles, id=role_id)
                if role in user.roles:
                    await user.remove_roles(role)
                    if i < len(attempt_roles) - 1:
                        next_role = discord.utils.get(guild.roles, id=attempt_roles[i+1])
                        await user.add_roles(next_role)
                        break
            else:
                first_attempt_role = discord.utils.get(guild.roles, id=ATTEMPT_1_ROLE_ID)
                await user.add_roles(first_attempt_role)

class GenesisView(View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label="Enter the Passphrase", style=discord.ButtonStyle.primary, custom_id="enter_passphrase_genesis")
    async def enter_passphrase(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user
        guild = interaction.guild
        attempt_25_role = discord.utils.get(guild.roles, id=ATTEMPT_25_ROLE_ID)

        # Check if the user has the ATTEMPT_25_ROLE_ID
        if attempt_25_role in user.roles:
            await interaction.response.send_message("You have tried too many times. You may try again in 30 minutes (your '25 Attempts' role will be automatically removed at that time).", ephemeral=True)
            return

        modal = GenesisPassphraseModal()
        await interaction.response.send_modal(modal)

class TheFinalJourneyPassphraseModal(Modal, title="Enter the Passphrase"):
    passphrase_input = TextInput(placeholder="Passphrase", custom_id="passphrase_input", label="Input the Passphrase")

    async def on_submit(self, interaction: discord.Interaction):
        entered_passphrase = self.children[0].value
        correct_passphrase = "balance"
        user = interaction.user
        guild = interaction.guild

        if entered_passphrase == correct_passphrase:
            await interaction.response.send_message("You have submitted the correct passphrase! The next part of your journey has been made available to you.", ephemeral=True)

            # Assign Victory role
            the_final_journey_role = discord.utils.get(guild.roles, id=THE_FINAL_JOURNEY_ROLE_ID)
            victory_role = discord.utils.get(guild.roles, id=VICTORY_ROLE_ID)
            await user.add_roles(victory_role)

            # Remove any attempt roles
            for role_id in attempt_roles:
                role = discord.utils.get(guild.roles, id=role_id)
                await user.remove_roles(role)

            await asyncio.sleep(10)

            await user.remove_roles(the_final_journey_role)
        else:
            await interaction.response.send_message("That passphrase is not correct.", ephemeral=True)
            # Assign the next attempt role
            for i, role_id in enumerate(attempt_roles):
                role = discord.utils.get(guild.roles, id=role_id)
                if role in user.roles:
                    await user.remove_roles(role)
                    if i < len(attempt_roles) - 1:
                        next_role = discord.utils.get(guild.roles, id=attempt_roles[i+1])
                        await user.add_roles(next_role)
                        break
            else:
                first_attempt_role = discord.utils.get(guild.roles, id=ATTEMPT_1_ROLE_ID)
                await user.add_roles(first_attempt_role)

class TheFinalJourneyView(View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label="Enter the Passphrase", style=discord.ButtonStyle.primary, custom_id="enter_passphrase_the_final_journey")
    async def enter_passphrase(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user
        guild = interaction.guild
        attempt_25_role = discord.utils.get(guild.roles, id=ATTEMPT_25_ROLE_ID)

        # Check if the user has the ATTEMPT_25_ROLE_ID
        if attempt_25_role in user.roles:
            await interaction.response.send_message("You have tried too many times. You may try again in 30 minutes (your '25 Attempts' role will be automatically removed at that time).", ephemeral=True)
            return
        modal = TheFinalJourneyPassphraseModal()
        await interaction.response.send_modal(modal)
    
bot.run(BOT_TOKEN)
