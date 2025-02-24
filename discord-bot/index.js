require('dotenv').config();
const { Client, GatewayIntentBits } = require('discord.js');
const axios = require('axios'); // Importa axios para fazer requisições HTTP

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent
    ]
});

const statusRegex = /^bot,status:"(\d{1,10}-\d{1,10})"$/;

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

client.on('messageCreate', async msg => {
    const msgContent = msg.content.replace(/\s+/g, "");

    if (statusRegex.test(msgContent)) {
        const match = msgContent.match(statusRegex);
        const valor = match[1];

        try {
            const response = await axios.get(process.env.API_URL + "/user/external_info?player_id=" + valor);
            const chars = response.data.chars;

            if (Array.isArray(chars)) {
                // Ordena o array pelo campo total em ordem decrescente
                chars.sort((a, b) => b.total - a.total);

                const formattedResponse = chars.map(item => `${item.name}: ${item.total}`).join('\n');
                msg.reply(formattedResponse);
            } else {
                msg.reply('Erro: formato de resposta inesperado.');
            }
        } catch (error) {
            msg.reply('Erro ao buscar dados do servidor.');
        }
    }

    if (msg.content === 'bot, qual é o jogador mais pica do brasil?') {
        msg.reply('O melhor jogador do Brasil é o RTK Rickrribeir');
    }
});

client.login(process.env.CLIENT_TOKEN);
