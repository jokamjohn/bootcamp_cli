import click
import requests


# The entry point of the app
@click.command()
def cli():
    # Show the user the intro message
    get_intro()

    # Prompt the user to enter a news source
    news_source = click.prompt("Please select a news source by entering its number or press enter for BBC", default=1)

    # Dictionary containing the news sources
    news_dict = get_news_sources()

    if news_source in news_dict.keys():
        get_news_articles(news_dict[news_source])
    else:
        click.echo(click.style("Wrong input try again", fg='red'))


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


# Function to get news articles from the specified source, BBC has the default.
def get_news_articles(source):
    data = requests.get(
        "https://newsapi.org/v1/articles?source=" + source + "&apiKey=ba4d03d4a6f84f10962a79fd977e43b2")
    if data.status_code == 200:
        news_json = data.json()
        articles = news_json["articles"]
        for article in articles:
            author = article['author']
            title = article['title']
            description = article['description']

            click.echo_via_pager(" TITLE: {} \n DESCRIPTION: {} \n AUTHOR: {}".format(title, description, author))
            click.secho("=" * 130, fg='blue')
    else:
        click.echo("An error occurred try again later")
