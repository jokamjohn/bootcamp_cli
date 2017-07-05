import click


# The entry point of the app
@click.command()
def cli():
    news_dict = get_news_sources()

    get_intro()

    news_source = click.prompt("Please select a news source by entering its number or press enter for BBC", default=1)


# Return the news sources
def get_news_sources():
    return {1: 'bbc-news', 2: 'al-jazeera-english', 3: 'bloomberg', 4: 'buzzfeed'}


# Return the intro message to show the user
def get_intro():
    click.secho("~" * 130, fg='blue')
    click.secho("Welcome to News-Breaker", fg='green')
    click.secho("~" * 130, fg='blue')
    click.echo("\n")

    click.secho("NEWS SOURCES", fg='green')
    click.secho('''        
        1 - BBC
        2 - AL Jazeera 
        3 - Bloomberg
        4 - BuzzFeed
    ''', fg='blue')
