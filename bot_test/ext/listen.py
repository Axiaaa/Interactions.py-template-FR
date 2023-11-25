import interactions

class Listen(interactions.Extension):

    @interactions.listen(event_name=interactions.events.ChannelCreate)
    async def on_channel_create(self, event : interactions.events.ChannelCreate):
        """
        Ce listener permet d'envoyer un message lorsqu'un salon est créé.

        Args:
            event (interactions.events.ChannelCreate): Event de création de salon

        Retourne :
            None
        """
        channel = event.channel
        await channel.send("Ce salon vient d'être créé !")

    @interactions.listen(event_name=interactions.events.MemberUpdate)
    async def on_member_update(self, event : interactions.events.MemberUpdate):
        """
        Ce listener permet d'envoyer un message lorsqu'un membre change de pseudo.

        Args:
            event (interactions.events.MemberUpdate): Event de changement de membre

        Retourne :
            None
        """
        if event.before.nickname != event.after.nickname :
            await event.after.send("Tu as changé de pseudo !")

    @interactions.listen(event_name=interactions.events.Startup)
    async def on_start(self, event : interactions.events.Startup):
        """
        Ce listener permet d'envoyer un message lorsque le bot est prêt.

        Args:
            event (interactions.events.Startup): Event de démarrage du bot

        Retourne :
            None
        """
        print("Le bot est prêt !")

    @interactions.listen()
    async def on_error(self, error = interactions.events.Error):
        """
        Ce listener permet d'envoyer un message lorsqu'une erreur est survenue.
        
        Args:
            error (interactions.events.Error): Event d'erreur

        Retourne :
            None
        """
        await self.bot.get_channel(1172931641317019681).send(f"Hey <@1093101428316327946>, une erreur est survenue : {error.source} -> {error.error}")
        return

def setup(bot):
    Listen(bot)