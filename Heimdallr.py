# i t n o A


from asgard import heimdallr,version
from sys import stdout
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time,datetime




Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "?") #Initialise client bot
say = stdout.write

def is_online(member):
    if str(member.status)=='online':
        return 1
    elif str(member.status)=='idle':
        return 2
    else:
        return 0

def is_AdminorModer(guild,member):
    if member.id==guild.owner.id:
        return True
    elif 'mod' in get_roles(member.roles):
        return True
    else:
        return False
is_auth = is_AdminorModer

def get_roles(rolesData):
    roles = []
    for role in rolesData:
        if str(role)[0]=='@':
            roles.append(str(role)[1:])
        else:
            roles.append(str(role))
    return roles



@client.event 
async def on_ready():
    say("Our Bot is ready!\n")


@client.event
async def on_message(message):
    msg=message.content
    ch_name=message.channel.name
    msn = message.guild
    sid = msn.id
    x=msg.split()
    
    uid = message.author.id
    uname = message.author.name
    chid = message.channel.id
    authorised = is_auth(message.guild,message.author)
    print(authorised)
    say("%s || %s || %s || %s \n"%(msn,ch_name,uname,msg)) # if any error occurs, see why
    if msg[0]=='!' and (ch_name=='heimdallr-bot' or ch_name=='heimdallr-test') and authorised==True:
        if msg=='!servstat': # only for the developer
            if str(sid)=='': # checking if command was from home server
                await message.channel.send("We are active in %s server(s)"%len(client.guilds))
        elif x[0]=='!sendAll' and str(sid)=='': # only for the developer, checking if command was from home server
            mm = ' '.join(x[1:])
            for s in client.guilds:
                channel = discord.utils.get(client.get_all_channels(), guild__name=str(s.name), name='heimdallr-bot')
                if channel:
                    await channel.send("Home : %s"%mm)
            await message.channel.send("Done!")
        elif x[0]=='!sendMsg' and str(sid)=='': # only for the developer, checking if command was from home server
            if len(x)>=4:
                gid = int(x[1])
                oid = int(x[2])
                mmm = str(x[3:])
                s = client.get_guild(gid)
                channel = discord.utils.get(client.get_all_channels(), guild__name=str(s.name), name='heimdallr-bot')
                await channel.send("Developer said : %s "%mmm)
            #pass
        elif x[0]=='!feedback':
            mm = ' '.join(x[1:])
            home = client.get_guild(int('')) # home server
            channel = home.get_channel(int('')) #channel
            await channel.send("%s (%s) from %s (%s,ch=%s) said : %s"%(uname,uid,msn.name,msn.id,message.channel.id,mm))
            
        elif x[0]=='!hdhelp':
            await message.channel.send(banner)
        elif x[0]=='!clear':
            if len(x)==2:
                async for mess in message.channel.history(limit=int(x[1])+1):
                    await mess.delete(delay=None)
            elif len(x)==3:
                seer = message.guild.channels
                for s in seer:
                    if str(s.name)==x[2] and s.type=='text':
                        async for mess in s.history(limit=int(x[1])+1):
                            await mess.delete(delay=None)
                        break
        elif x[0]=='!comments':
            mem = "%s"%x[1]
            mem = mem[2:-1]
            say("member %s"%mem)
            if mem[0]=='!':
                mem=mem[1:]
            if mem.isdigit():
                m = message.guild.get_member(int(mem))
                if m:
                    if x[2]=='count':
                        ccc = 0
                        s=''
                        if len(x)==3:
                            s=message.channel
                            async for mess in s.history(limit=None):
                                if mess.author.id==m.id:
                                    ccc+=1
                        else:
                            seer = message.guild.channels
                            for s in seer:
                                if str(s.name)==x[3] and str(s.type)=='text':
                                    async for mess in s.history(limit=None):
                                        if mess.author.id==m.id:
                                            ccc+=1
                                    break
                        await message.channel.send("%s have posted %s comments on chaneel %s"%(m.name,ccc,s.name))
                                
                    elif x[2]=='del':
                        if len(x)==3:
                            s=message.channel
                            async for mess in s.history(limit=None):
                                if mess.author.id==m.id:
                                    await mess.delete(delay=None)
                        else:
                            seer = message.guild.channels
                            for s in seer:
                                if str(s.name)==x[3] and str(s.type)=='text':
                                    async for mess in s.history(limit=None):
                                        if mess.author.id==m.id:
                                            await mess.delete(delay=None)
                                    break
                        
        elif x[0]=='!credits':
            await message.channel.send(banner)
        elif x[0]=='!version':
            await message.channel.send(version)
        elif x[0]=='!server' and x[1]=='members':
            await message.channel.send("We currently have %s members in this server(%s)"%(message.guild.member_count,msn.name))
        elif x[0]=='!server' and x[1]=='status':
            Ocount = list(map(is_online,message.guild.members))
            onl=Ocount.count(1)
            idl=Ocount.count(2)
            tot = onl+idl
            await message.channel.send("In this server (%s) We currently have %s member(s) online where %s member(s) is in idle mode"%(msn.name,tot,idl))
        elif x[0]=='!roles':
            if x[1]=='me':
                r = ','.join(get_roles(message.author.roles))
                await message.channel.send("You have these following role(s): %s "%(r))
            else:
                mem = "%s"%x[1]
                mem = mem[2:-1]
                if mem[0]=='!':
                    mem=mem[1:]
                if mem.isdigit():
                    m = message.guild.get_member(int(mem))
                    if m:
                        r = ','.join(get_roles(m.roles))
                        n = str(m.name)
                        await message.channel.send("%s has these following role(s): %s "%(n,r))
                    else:
                        await message.channel.send("%s wasn't found in this server"%(n))
                else:
                    await message.channel.send("Please Tag a valid user, you probably have mentioned a role")
        elif x[0]=='!when':
            mem = "%s"%x[1]
            mem = mem[2:-1]
            if mem[0]=='!':
                mem=mem[1:]
            if mem.isdigit():
                m = message.guild.get_member(int(mem))
                if m:
                    n = str(m.name)
                    tt = "%s"%(m.joined_at)
                    await message.channel.send("%s joined this server at %s"%(n,tt))
        elif x[0]+x[1]=='!whois':
            mem = "%s"%x[2]
            mem = mem[2:-1]
            if mem[0]=='!':
                mem=mem[1:]
            
            if mem.isdigit():
                m = message.guild.get_member(int(mem))
                if m:
                    na = str(m.name)
                    ni = str(m.nick)
                    oi = str(message.guild.owner.id)
                    if oi==str(m.id) and ni!=None:
                        await message.channel.send("Oh!! this is %s aka %s, owner of this server"%(na,ni))
                    elif oi==str(m.id) and ni==None:
                        await message.channel.send("Oh!! this is %s, owner of this server"%(na,ni))
                    elif m.bot==True and ni!=None:
                        await message.channel.send("Oh!! this is %s aka %s, loyal Bot of this server"%(na,ni))
                    elif m.bot==True and ni==None:
                        await message.channel.send("Oh!! this is %s , loyal Bot of this server"%(na))
                    elif ni!=None:
                         await message.channel.send("Oh!! this is %s aka %s, member of this server"%(na,ni))
                    else:
                        await message.channel.send("Oh!! this is %s"%(na))
        elif x[0]=='!act':
        
            mem = "%s"%x[1]
            mem = mem[2:-1]
            
            if mem[0]=='!':
                mem=mem[1:]
            if mem.isdigit():
                m = message.guild.get_member(int(mem))
                if m:
                    act=list(m.activities)
                
                    if act==None or act==[]:
                        vcc = m.voice.channel
                        if str(m.status)=="online" and vcc!=None:
                            await message.channel.send("He is Online and currently on voice channel named \"%s\""%str(vcc))
                        elif str(m.status)=="online" and vcc==None:
                            await message.channel.send("He is Online but doing nothing")
                        else:
                            if vcc:
                                await message.channel.send("He is in "+str(m.status)+" mode, but is on "+str(vcc)+" channel")
                            else:
                                await message.channel.send("He is in "+str(m.status)+" mode")
                    else:
                        gg="%s"%(list(m.activities))
                        aa = gg.split('=')
                        gg=gg.split()
                        g,st,sm=[0,0,0]
                        for w in gg:
                            if (gg[0]=='[<Game') and g==0:
                                g=1
                                await message.channel.send("He is playing "+str(aa[1][1:-3]))
                            elif (gg[0]=='[<Streaming') and st==0:
                                st=1
                                await message.channel.send("He is streaming "+str(aa[1][1:-3]))
                            elif (gg[0]=='[<Spotify') and sm==0:
                                sm=1
                                await message.channel.send("He is listening "+str(aa[1][1:-3]))

        elif x[0]=='!voice':
            if len(x)>=2:
                chh=' '.join(x[1:])
                for s in message.guild.channels:
                    if str(s.name)==chh and str(s.type)=='voice':
                        mm = ','.join([m.name for m in s.members])
                        cc = len(s.members)
                        await message.channel.send("%s has currently %s member connected, %s"%(chh,cc,mm))
                        break
        elif msg=='':
            pass
        else:
            pass
        

banner="""http://cwfbd.blogspot.com/2019/06/heimdallrbot.html"""
    



@client.event
async def on_guild_join(guild):
    home = client.get_guild(int('')) # home server
    channel = home.get_channel(int('')) # channel id
    await channel.send("We joined a server named \"%s\" owned by %s on %s"%(guild.name,guild.owner.name,time.ctime()))
    #guild.create_text_channel(name="heimdallr-bot")

@client.event
async def on_guild_remove(guild):
    home = client.get_guild(int('')) # home server
    channel = home.get_channel(int('')) # home server
    await channel.send("Well, we was brutally removed from server named \"%s\" owned by %s on %s"%(guild.name,guild.owner.name,time.ctime()))
    #guild.create_text_channel(name="heimdallr-bot")


client.run(heimdallr)
