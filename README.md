# HeimdallrBot
This bot was created for Discord Hack Week. Heimdallr Bot allows you to monitor your server and it's members and also allows you to communicate with developers without sending DM or joining the home server. It will share reports only with server owner and moderators.

# Requires
[Python 3.6](http://python.org/getit) 32bit,
[Discord.py](https://discordpy.readthedocs.io/en/latest/) 1.2.3


# How To Use:

We have a issue for now (see note). You need to create a channel named heimdallr-bot with permission allow read everyone. allow send only for admin and moderator.
To command heimdallr. You need to be the owner of server or must have a role named 'mod'.
[invite to server](https://discordapp.com/oauth2/authorize?client_id=593000044106612746&permissions=8&scope=bot)

Here is some following commads that you can use:-

# Server Status :

!server status -- to get numbers of currently active members on server
!server members -- to get  numbers of total members


# Member Status:

- !act [mention member] -- to get activities of a specific member [voice channel,game,stream,listening,online status]
- !roles [mention member]  -- to get which roles do the member has
- !when [mention member] -- to get when the member was joined the server
- !who [mention member]  -- to get real name and identity[owner/bot/regular member/nick name] 
 

# Text Channels:

- !clear [ammount] -- to clear amount of message on heimdallr-bot channel
- !clear [ammount] [channel_name] -- to clear amount of message on given channel
- !comments [mention member] count -- to count total message of member on heimdallr-bot
- !comments [mention member] count [channel_name] -- to count total message of member on given channel
- !comments [name] del --to delete all message of member on heimdallr-bot
- !comments [name] del [channel_name] --to delete all message of member on given channel


# Voice Channel:

- !voice [channel name] -- to get how many member is connected to that channel


# Extras:

- !credits -- To find us
- !feedback [single_line message] -- to communicate with developer
- !hdhelp -- for this [page link](http://cwfbd.blogspot.com/2019/06/heimdallrbot.html)
- !version -- to see version of the bot



# Developers:

- !servstat -- To see in how many servers the bot is connected
- !sendAll -- Send message to all server
- !sendMsg [uid] [sid] [chid] [text] -- Send message to a specific channel

More commads will be added in future

[ Note : Due to some technical issue, Heimdallr cannot stay online all the time for now, We will fix this problem in future]
You can also help us by giving us idea how we can update the bot using the feedback command.
Your feedback is valuable for us . You can also send feedback on heimdallr-feedback channel on our [home server](http://discord.gg/VndGYTs).
