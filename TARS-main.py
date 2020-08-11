#!/usr/bin/env python3
import discord
import time
import os
import asyncio
import requests
import smtplib
from email.mime.text import MIMEText
from ast import literal_eval

s = smtplib.SMTP('smtp.gmail.com', 587)

client = discord.Client()

mail = "bravotars@gmail.com"

with open("/root/Bot/mail_passwd.txt", 'r') as mailpasswd_:
    mailpasswd = mailpasswd_.read()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global mail
    if message.author.bot:
        return

    if message.content.startswith('come on tars'):
        await message.channel.send('We_are___lined_up!')

    if message.content.startswith('explosion'):
        for i in range(3, 0, -1):
            ii = str(i) + '...'
            time.sleep(1)
            await message.channel.send(ii)
        await message.channel.send(file=discord.File('/home/pi/DiscordBot-TARS/pics/explosion.gif'))
    
    if message.content.startswith('troll'):
        await message.channel.send(file=discord.File('/home/pi/DiscordBot-TARS/pics/troll.gif'))

    if '뱁새' in message.content:
        await message.channel.send(file=discord.File('/home/pi/DiscordBot-TARS/pics/bird.jpg'))
    
    
    if message.content.startswith('$'):
        inpuT = message.content.split()
        if inpuT[0] == "$ip":
            try:
                ip = inpuT[1]
                url = "http://api.ipstack.com/" + str(ip) + "?access_key=8038cb85349c5da46994f1d5c62c3c3a"
                response_ = requests.get(url)
                response = response_.json()
                location = response['continent_name'] + "/" + response['country_name'] + "/" + response['region_name'] + "/" + response['city']
                gps = "https://google.co.kr/maps/@" + str(response['latitude']) + "," + str(response['longitude']) + ",14z"
                await message.channel.send("Location: " + location + "\nMap: " + gps)

            except(IndexError, ValueError):
                await message.channel.send('$ip <ip>')


        inpuT = message.content.split()
        if inpuT[0] == "$mail":
            try:
                mailaddr = inpuT[1]
                banner = inpuT[2]
                text = inpuT[3]
                msg = MIMEText(text)
                msg['Subject'] = banner
                s.connect('smtp.gmail.com', '587')
                s.ehlo()
                s.starttls()
                s.login(mail, mailpasswd)
                s.sendmail(mail, mailaddr, msg.as_string())
                await message.channel.send('Send')

            except (IndexError, ValueError):
                await message.channel.send('$mail <Target_mail> <Subject> <Main_text>')

            except smtplib.SMTPDataError:
                await message.channel.send('[!]Daily_usage_limit_exceeded')

            except smtplib.SMTPSenderRefused:
                await message.channel.send('[!]SMTPdisconnected,please_reboot_bot')
            s.quit()

        if inpuT[0] == "$mail-terror":
            try:
                mailaddr = inpuT[1]
                banner_ = inpuT[2]
                text_ = inpuT[3]
                i = inpuT[4]
                if mailaddr == "wildcard1719@gmail.com" or mailaddr == "wildcard1719@naver.com" or mailaddr == "wildcard1719@outlook.kr":
                    await message.channel.send('어딜')
                    return

                s.connect('smtp.gmail.com', '587')
                s.ehlo()
                s.starttls()
                s.login(mail, mailpasswd)

                for ii in range(int(i)):
                    banner = banner_ + str(ii)
                    text = text_ + str(ii)
                    msg = MIMEText(text)
                    msg['Subject'] = banner
                    try:
                        s.sendmail(mail, mailaddr, msg.as_string())
                        time.sleep(1)
                    except smtplib.SMTPDataError:
                        await message.channel.send('[!]Fail_in' + str(ii))
                        await message.channel.send('[!]Daliy_usage_limit_exceeded')
                        break
                    except smtplib.SMTPSenderRefused:
                        await message.channel.send('[!]Fail_in' + str(ii))
                        await message.channel.send('[!]SMTPdisconnected,please_reboot_bot')
                        break
                    except:
                        await message.channel.send('[!]Fail_in' + str(ii))
                        break 

                s.quit()
                await message.channel.send('Send')

            except (IndexError, ValueError, smtplib.SMTPRecipientsRefused):
                await message.channel.send('$mail-terror <Target_mail> <Subject> <Main_text> <Repeat_count>')
        
        
        if inpuT[0] == "$mail-reload":
            try:
                clip = inpuT[1]
                if int(clip) == 1:
                    mail = "bravotars@gmail.com"
                if int(clip) == 2:
                    mail = "bravotars2@gmail.com"
                if int(clip) == 3:
                    mail = "bravotars3@gmail.com"
                if int(clip) == 4:
                    mail = "bravotars4@gmail.com"
                if int(clip) == 5:
                    mail = "bravotars5@gmail.com"
                if int(clip) == 6:
                    mail = "bravotars6@gmail.com"
                if int(clip) == 7:
                    mail = "bravotars7@gmail.com"
                if int(clip) == 8:
                    mail = "bravotars8@gmail.com"
                await message.channel.send('Reload ' + mail)
            except:
                await message.channel.send('$mail-reload <Clip_number(1-8)>')


        if inpuT[0] == "$say":
            try:
                content = message.content[5:]
                await message.channel.send(content)
                await message.delete()
            except IndexError:
                await message.channel.send('$say <Content>')

        if inpuT[0] == "$reboot":
            os.system("python3 /home/pi/DiscordBot-TARS/Reboot.py")
            exit()

        if inpuT[0] == "$help":
            string = "explosion: TARS go boom\n$ip <ip>: ip location tracking\n$mail <Target_mail> <Subject> <Main_text>: send Email\n$mail-terror <Target_mail> <Subject> <Main_text> <Repeat_count>: send EmailBomb\n$mail-reload <Clip_number(1-8)>: mail reload\n$say <Content>: say content"
            await message.channel.send(string)

with open("/root/Bot/TARS-Token.txt", "r") as token:
    client.run(token.read())
