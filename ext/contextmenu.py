import interactions

class Contextmenu(interactions.Extension):

    @interactions.message_context_menu(name="repeat")
    async def repeat(self, ctx: interactions.ContextMenuContext):
        """
        Ce context_menu permet de répéter le message d'un utilisateur.

        Args:
            ctx (interactions.ContextMenuContext): Contexte de la commande

        Retourne :
            None
        """
        message: interactions.Message = ctx.target
        if message and message.content  : 
            await ctx.send(message.content)
        else :
            await ctx.send("Error")
            
    @interactions.user_context_menu(name="pong")
    async def ping(self, ctx: interactions.ContextMenuContext):
        """
        Ce context_menu permet de ping.

        Args:
            ctx (interactions.ContextMenuContext): Contexte de la commande
        
        Retourne :
            None
        """
        member: interactions.Member = ctx.target
        await ctx.send(member.mention)

    @interactions.message_context_menu(name="report")
    async def report(self, ctx : interactions.ContextMenuContext):
        """
        Ce context_menu permet de signaler un message.

        Args:
            ctx (interactions.ContextMenuContext): Contexte de la commande
        
        Retourne :
            None
        """
        if ctx.target.content : 
            await ctx.send(f"Le message a été signalé dans <#{1177361357704810536}>", ephemeral=True)
            embed = interactions.Embed(
                title=f"Message de {ctx.target.author.username} signalé",
                description=ctx.target.content,
                color=interactions.Color.from_hex("#FF5733"),
                timestamp=interactions.Timestamp.now(),
                author=interactions.EmbedAuthor(ctx.author.username, icon_url=ctx.target.author.avatar_url),
            )
            await self.bot.get_channel(1177361357704810536).send(embed=embed)
        else : 
            await ctx.send("Error", ephemeral=True)


def setup(bot):
    Contextmenu(bot)