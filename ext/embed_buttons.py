import interactions

class Embed_buttons(interactions.Extension) :


    @interactions.slash_command(
        name="embed",
        description="Envoie un embed de test"
    )
    async def embed_test(self, ctx : interactions.InteractionContext) :
        """
        Cette commande permet de tester les embeds.

        Args:
            ctx (interactions.InteractionContext): Contexte de la commande

        Retourne :
            None
        """
        embed = interactions.Embed(
            title="Ceci est un titre",
            description="Ceci est une description",
            color=interactions.Color.from_hex("#FF5733"),
            timestamp=interactions.Timestamp.now(),
            author=interactions.EmbedAuthor("Moi", icon_url=ctx.user.avatar_url),
            thumbnail=interactions.EmbedAttachment(url="https://cdn.discordapp.com/attachments/1172931641317019681/1177691732184420522/fox_1.png?ex=65736de5&is=6560f8e5&hm=202c2a4e1a552d3c5ff6c0e6f2e0411f79a8b4c5bdb5c25b4866acd58b7e93b4&"),
            footer= interactions.EmbedFooter("Ceci est un footer", icon_url=self.bot.user.avatar_url),
            images= [interactions.EmbedAttachment(url="https://cdn.discordapp.com/attachments/1172931641317019681/1177694760169918504/image.png?ex=657370b7&is=6560fbb7&hm=a193c2469bb91cd906c65c5f636d190cc51b646fc7819df3bb5967c63d7fa8a1&")],
        )
        await ctx.respond(embed=embed)

    @interactions.slash_command(
        name="boutons",
        description="Envoie un message avec des boutons cliquables"
    )
    async def bouttons(self, ctx : interactions.InteractionContext) : 
        """
        Cette commande permet de tester les boutons.

        Args:
            ctx (interactions.InteractionContext): Contexte de la commande

        Retourne :
            None
        """
        boutons: list[interactions.ActionRow] = [
            interactions.ActionRow(
                interactions.Button(
                    style=interactions.ButtonStyle.GREEN,
                    label="Click Moi",
                    custom_id="btn_1"
                ),
                interactions.Button(
                    style=interactions.ButtonStyle.RED,
                    label="Click Me Too",
                    custom_id="btn_2"
                ),
                interactions.Button(
                    style=interactions.ButtonStyle.GRAY,
                    emoji="🤙🏻",
                    label="Pouet",
                    custom_id="btn_2"
                )
            )
        ]
        await ctx.channel.send("Look a Button!", components=boutons)
        await ctx.respond("Commande correctement éxécutée", ephemeral=True)


    @interactions.component_callback("btn_1")
    async def btn_1_callback(self, ctx : interactions.ComponentContext):
        """
        Ce listener permet de d'effectuer une action lorsqu'un bouton est cliqué.

        Args:
            ctx (interactions.ComponentContext): Contexte du bouton

        Retourne :
            None
        """
        await ctx.channel.send("Pouet")
        await ctx.edit_origin(content="Ce message a été modifié !", embed=None)

    @interactions.component_callback("btn_2")
    async def btn_2_callback(self, ctx : interactions.ComponentContext):
        """
        Ce listener permet de d'effectuer une action lorsqu'un bouton est cliqué.

        Args:
            ctx (interactions.ComponentContext): Contexte du bouton

        Retourne :
            None
        """
        await ctx.edit_origin(content="", embed=interactions.Embed(
            title="Test",
            description="test2"
        ))

def setup(bot):
    Embed_buttons(bot)