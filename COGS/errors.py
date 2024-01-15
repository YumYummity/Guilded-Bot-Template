import os, string, secrets, traceback

import guilded
from guilded.ext import commands

class errors(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener(name="on_command_error")
    async def ANERROROCCURED(self, ctx:commands.Context, error):
        try:
            if isinstance(error, commands.CommandNotFound):
                return
            elif isinstance(error, commands.CommandOnCooldown):
                embedig = guilded.Embed(
                    title='Slow down there!',
                    color=guilded.Color.red(),
                    description=f'Please stop spamming this command! Allow a 1 second pause before trying again.'
                )
                return await ctx.reply(embed=embedig, private=ctx.message.private)
            elif isinstance(error, commands.MissingRequiredArgument):
                embedig = guilded.Embed(
                    title='Missing Arguments',
                    description=f'**You\'re missing required arguments!**\n\n***Error:***\n{", ".join(error.args)}',
                    color=guilded.Color.red()
                )
                return await ctx.reply(embed=embedig, private=True)
            elif isinstance(error, commands.BadArgument):
                return await ctx.reply(f'**You put invalid arguments!**\n***Arguments Wrong:***\n{", ".join(error.args)}', private=True)
            elif isinstance(error, commands.UnexpectedQuoteError):
                return await ctx.reply(f'**Why put a quote?!?!?!**\nAt least close it next time.', private=True)
            elif isinstance(error, commands.InvalidEndOfQuotedStringError):
                return await ctx.reply(f'**Invalid End of Quoted String.**\nWhat exactly are you trying...', private=True)
            elif hasattr(error, "original") and isinstance(error.original, guilded.Forbidden):
                permmap = {
                    "CanUpdateServer": "Update Server",
                    "CanManageRoles": "Manage Roles",
                    "CanInviteMembers": "Invite Members",
                    "CanKickMembers": "Kick / Ban Members",
                    "CanManageGroups": "Manage Groups",
                    "CanManageChannels": "Manage Channels",
                    "CanManageWebhooks": "Manage Webhooks",
                    "CanMentionEveryone": "Can Mention @everyone and @here",
                    "CanModerateChannels": "Access Moderator View",
                    "CanBypassSlowMode": "Slowmode Exception",
                    "CanReadApplications": "View Applications",
                    "CanApproveApplications": "Approve Applications",
                    "CanEditApplicationForm": "Edit Application Forms",
                    "CanIndicateLfmInterest": "Indicate Find Players Interest",
                    "CanModifyLfmStatus": "Modify Find Players Status",
                    "CanReadAnnouncements": "View Announcements",
                    "CanCreateAnnouncements": "Create and Remove Announcements",
                    "CanManageAnnouncements": "Manage Announcements",
                    "CanReadChats": "Read Messages",
                    "CanCreateChats": "Send Messages",
                    "CanUploadChatMedia": "Upload Media",
                    "CanCreateThreads": "Create Threads",
                    "CanCreateThreadMessages": "Send Messages in Threads",
                    "CanCreatePrivateMessages": "Send Private Messages",
                    "CanManageChats": "Manage Messages",
                    "CanManageThreads": "Manage Threads",
                    "CanCreateChatForms": "Create Polls and Forms",
                    "CanReadEvents": "View Events",
                    "CanCreateEvents": "Create Events",
                    "CanEditEvents": "Manage Events",
                    "CanDeleteEvents": "Remove Events",
                    "CanEditEventRsvps": "Edit RSVPs",
                    "CanReadForums": "Read Forums",
                    "CanCreateTopics": "Create Forum Topics",
                    "CanCreateTopicReplies": "Create Topic Replies",
                    "CanDeleteTopics": "Manage Topics",
                    "CanStickyTopics": "Sticky Topics",
                    "CanLockTopics": "Lock Topics",
                    "CanReadDocs": "View Docs",
                    "CanCreateDocs": "Create Docs",
                    "CanEditDocs": "Manage Docs",
                    "CanDeleteDocs": "Remove Docs",
                    "CanReadMedia": "See Media",
                    "CanAddMedia": "Create Media",
                    "CanEditMedia": "Manage Media",
                    "CanDeleteMedia": "Remove Media",
                    "CanListenVoice": "Hear Voice",
                    "CanAddVoice": "Add Voice",
                    "CanManageVoiceGroups": "Manage Voice Rooms",
                    "CanAssignVoiceGroup": "Move Members",
                    "CanDisconnectUsers": "Disconnect User",
                    "CanBroadcastVoice": "Broadcast",
                    "CanDirectVoice": "Whisper",
                    "CanPrioritizeVoice": "Priority Speaker",
                    "CanUseVoiceActivity": "Use Voice Activity",
                    "CanMuteMembers": "Mute Members",
                    "CanDeafenMembers": "Deafen Members",
                    "CanSendVoiceMessages": "Send Messages in Voice Channel",
                    "CanCreateScrims": "Create Scrims",
                    "CanManageTournaments": "Manage Tournaments",
                    "CanRegisterForTournaments": "Register for Tournaments",
                    "CanManageEmotes": "Manage Emoji",
                    "CanChangeNickname": "Change Nickname",
                    "CanManageNicknames": "Manage Nicknames",
                    "CanViewFormResponses": "View Form Responses",
                    "CanViewPollResponses": "View Poll Results",
                    "CanReadListItems": "View List Items",
                    "CanCreateListItems": "Create List Items",
                    "CanUpdateListItems": "Manage List Item Messages",
                    "CanDeleteListItems": "Remove List Items",
                    "CanCompleteListItems": "Complete List Items",
                    "CanReorderListItems": "Reorder List Items",
                    "CanViewBracket": "View Brackets",
                    "CanReportScores": "Report Scores",
                    "CanReadSchedules": "View Schedules",
                    "CanCreateSchedule": "Create Schedule",
                    "CanDeleteSchedule": "Delete Schedule",
                    "CanManageBots": "Manage Bots",
                    "CanManageServerXp": "Manage Server XP",
                    "CanReadStreams": "View Streams",
                    "CanJoinStreamVoice": "Join Voice in Streams",
                    "CanCreateStreams": "Add Stream",
                    "CanSendStreamMessages": "Send Messages in Streams",
                    "CanAddStreamVoice": "Add Voice in Streams",
                    "CanUseVoiceActivityInStream": "Use Voice Activity in Streams"
                }
                allperms = [permmap[perm.strip()] for perm in error.original.raw_missing_permissions]
                embedigperms = guilded.Embed(
                    title='I\'m missing permissions',
                    description=f'**I don\'t have required permissions I need for this! Please make sure that channel overrides** (permissions put onto channels in the Permissions tab of Channel settings) **don\'t remove any permissions I need!**\n\n***Missing Permissions:***\n`{", ".join(allperms)}`',
                    color=guilded.Color.red()
                )
                return await ctx.reply(embed=embedigperms, private=ctx.message.private)
            else:
                def gen_cryptographically_secure_string(size:int):
                    '''
                    Generates a cryptographically secure string.
                    '''
                    letters = string.ascii_lowercase+string.ascii_uppercase+string.digits            
                    f = ''.join(secrets.choice(letters) for i in range(size))
                    return f
                usedrefcodes = []

                filenames = os.listdir(self.bot.CONFIGS.error_logs_dir)

                for filename in filenames:
                    if os.path.isdir(os.path.join(os.path.abspath(self.bot.CONFIGS.error_logs_dir), filename)):
                        usedrefcodes.append(filename)

                randomrefcode = gen_cryptographically_secure_string(20)

                while f'{randomrefcode}.txt' in usedrefcodes:
                    randomrefcode = gen_cryptographically_secure_string(20)

                try:
                    raise error
                except Exception as e:
                    tb = ''.join(traceback.format_exception(e, e, e.__traceback__))
                    self.bot.traceback(e)
                    with open(f'{self.bot.CONFIGS.error_logs_dir}\\{randomrefcode}.txt', 'w+') as file:
                        file.write(tb)
                        file.close()

                embedig = guilded.Embed(color=guilded.Color.red(), title='Something went wrong!', description=f'Please join our support server and tell my developer!\n[Support Server]({self.bot.CONFIGS.supportserverinv})')
                embedig.add_field(name='Error Reference Code', value=f'`{randomrefcode}`', inline=False)
                embedig.set_footer(text='Use the reference code to report a bug! This way we\'ll know what went wrong.')
                await ctx.reply(embed=embedig, private=True)
        except Exception as e:
            self.bot.traceback(e)

def setup(bot):
	bot.add_cog(errors(bot))