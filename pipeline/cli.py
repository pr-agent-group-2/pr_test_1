
import click
from .reader import read_csv
from .stats import column_mean

@click.command()
@click.argument('csv_file', type=click.Path(exists=True))
def main(csv_file):
    """Compute the mean of each numeric column in *CSV_FILE*."""
    rows = list(read_csv(csv_file))
    if not rows:
        click.echo("No data rows.")
        return

    headers = rows[0].keys()
    for header in headers:
        try:
            numbers = [float(r[header]) for r in rows]
            click.echo(f"{header}: {column_mean(numbers):.2f}")
        except ValueError:
            # Skip non-numeric columns
            continue

if __name__ == '__main__':
    main()
