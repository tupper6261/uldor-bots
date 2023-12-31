const { Client, GatewayIntentBits, Partials, ButtonBuilder, ModalBuilder, TextInputBuilder, TextInputStyle, ActionRowBuilder, Events, ButtonStyle } = require('discord.js');
const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMembers, GatewayIntentBits.MessageContent], partials: [Partials.Channel] });

const passwords = {
    '1128498231140159600': 'password1',
    '1133557148224344074': 'password2',
    '1133557281343160390': 'password3',
};

client.on('ready', async () => {
    /*
    // Send a message with a button in each channel
    const channels = Object.keys(passwords);
    const row = new ActionRowBuilder()
        .addComponents(
            new ButtonBuilder()
                .setCustomId('passwordButton')
                .setLabel('Enter Password')
                .setStyle(ButtonStyle.Primary),
        );

    for (const channelId of channels) {
        const channel = await client.channels.fetch(channelId);
        const messages = await channel.messages.fetch({ limit: 10 }); // fetch the last 10 messages
        const botMessage = messages.find(message => message.author.bot && message.content === 'Click the button to enter the password.');

        if (!botMessage) {
            await channel.send({ content: 'Click the button to enter the password.', components: [row] });
        }
    }
    */
});

client.on(Events.InteractionCreate, async interaction => {
    if (!interaction.isButton()) return;

    if (interaction.customId === 'passwordButton') {
        const modal = new ModalBuilder()
            .setCustomId('passwordModal')
            .setTitle('Enter Password');

        const passwordInput = new TextInputBuilder()
            .setCustomId('passwordInput')
            .setLabel("Enter the password")
            .setStyle(TextInputStyle.Short);

        const actionRow = new ActionRowBuilder().addComponents(passwordInput);

        modal.addComponents(actionRow);

        await interaction.showModal(modal);
    }
});

client.on(Events.InteractionCreate, async interaction => {
    if (!interaction.isModalSubmit()) return;

    if (interaction.customId === 'passwordModal') {
        const password = interaction.fields.getTextInputValue('passwordInput');
        const channelId = interaction.channelId;

        // Check the password
        if (password === passwords[channelId]) {
            // Remove the old role and add the new one
            const oldRole = interaction.guild.roles.cache.find(role => role.name === "Role A");
            const newRole = interaction.guild.roles.cache.find(role => role.name === "Role B");
            interaction.member.roles.remove(oldRole);
            interaction.member.roles.add(newRole);

            await interaction.reply({ content: 'Password correct! You now have access to the next channel.' });
        } else {
            await interaction.reply({ content: 'Password incorrect. Please try again.' });
        }
    }
});

client.login(process.env.DISCORD_BOT_TOKEN);
