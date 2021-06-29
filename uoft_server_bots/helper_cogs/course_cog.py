import discord
import re
import os
from discord.ext.commands import command, Cog
from discord import Embed

from dotenv import load_dotenv

load_dotenv()

NUMBER_LIST= list(range(1, 100))

class CourseCog(Cog):
    def __init__(self, bot):
        self.bot = bot


    @command('getallquestions')
    async def getallquestions(self, ctx):

        COURSE_CHANNEL_ID = os.environ.get('COURSE_SELECTION_CHANNEL_ID')
        COURSE_QUESTIONS_CHANNEL_ID = os.environ.get("COURSE_QUESTIONS_CHANNEL_ID")

        # get course channel
        channel = self.bot.get_channel(int(COURSE_CHANNEL_ID))
        messages = await channel.history(limit=500).flatten()

        all_questions = []
        for msg in messages:
            res = any(str(ele)+'.' in str(msg.content) for ele in NUMBER_LIST)
            if res and msg.content:
                all_questions.append(str(msg.content))

            embed = Embed(
                title="All Course Questions",
                description="Here are all the questions asked in the #course-selection channel:",
                color=0xF1948A
            )
            for index, question in enumerate(all_questions[::-1]):
                embed.add_field(
                    name = 'Q' + str(index+1) + '.',
                    value = question.strip(),
                    inline=False
                )
        # get questions channel
        channel = self.bot.get_channel(int(COURSE_QUESTIONS_CHANNEL_ID))
        # messages_in_question_channel = await ctx.channel.history(limit=1).flatten()
        await ctx.channel.purge(limit=200)
        
        message = await ctx.channel.send(embed=embed)
        await message.add_reaction('👍🏼')


def setup(bot):
    bot.add_cog(CourseCog(bot))
