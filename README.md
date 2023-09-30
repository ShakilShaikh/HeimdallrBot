# HeimdallrBot

![HeimdallrBot Logo](heimdallr(1).png)

## Overview

HeimdallrBot is a Discord bot created for Discord Hack Week. It provides server monitoring and communication features, allowing you to keep an eye on your server and communicate with developers without sending direct messages or joining their home server. Reports are shared only with server owners and moderators.

## Prerequisites

- [Python 3.6 (32-bit)](http://python.org/getit)
- [Discord.py 1.2.3](https://discordpy.readthedocs.io/en/latest/)

## Installation

To use HeimdallrBot, follow these steps:

1. Create a channel named `heimdallr-bot` with read permissions for everyone and send permissions for administrators and moderators.

2. Invite HeimdallrBot to your server using [this invite link](https://discordapp.com/oauth2/authorize?client_id=593000044106612746&permissions=8&scope=bot).

3. To command HeimdallrBot, you must be the server owner or have a role named 'mod.'

## Usage

Here are some commands you can use with HeimdallrBot:

### Server Status:

- `!server status`: Get the number of currently active members on the server.
- `!server members`: Get the total number of members on the server.

### Member Status:

- `!act [mention member]`: Get activities of a specific member (voice channel, game, stream, listening, online status).
- `!roles [mention member]`: Get the roles of a member.
- `!when [mention member]`: Find out when a member joined the server.
- `!who [mention member]`: Get information about a member (real name, identity).

### Text Channels:

- `!clear [amount]`: Clear a specified number of messages in the `heimdallr-bot` channel.
- `!clear [amount] [channel_name]`: Clear a specified number of messages in the given channel.
- `!comments [mention member] count`: Count the total messages of a member in `heimdallr-bot`.
- `!comments [mention member] count [channel_name]`: Count the total messages of a member in a specific channel.
- `!comments [name] del`: Delete all messages of a member in `heimdallr-bot`.
- `!comments [name] del [channel_name]`: Delete all messages of a member in a specific channel.

### Voice Channel:

- `!voice [channel name]`: Get the number of members connected to a specific voice channel.

### Extras:

- `!credits`: Find information about the developers.
- `!feedback [single_line_message]`: Communicate with the developer.
- `!hdhelp`: Access the [help page](http://cwfbd.blogspot.com/2019/06/heimdallrbot.html).
- `!version`: Check the bot's version.

## Developers

- `!servstat`: View the number of servers the bot is connected to.
- `!sendAll`: Send a message to all servers.
- `!sendMsg [uid] [sid] [chid] [text]`: Send a message to a specific channel.

Please note that due to technical issues, HeimdallrBot may not stay online all the time. We are actively working on resolving this issue.

You can help us improve the bot by providing feedback using the `!feedback` command. Your feedback is valuable to us, and you can also share your ideas on the `heimdallr-feedback` channel on our [home server](http://discord.gg/VndGYTs).

## License

This project is licensed under the [MIT License](LICENSE).

