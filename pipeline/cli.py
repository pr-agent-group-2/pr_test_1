
import click
from .reader import read_csv, read_json
from .stats import column_mean, column_median

@click.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.option('--format', '-f', type=click.Choice(['csv', 'json']), default='csv',
              help='Input file format.')
@click.option('--stat', '-s', type=click.Choice(['mean', 'median']), default='mean',
              help='Statistic to compute.')
def main(file_path, format, stat):
    """Compute a statistic of numeric columns in FILE_PATH.

    * Adds JSON support and median calculation.
    * BUG: Median calculation mis‑handles empty input (division by zero).
    """
    if format == 'csv':
        rows = list(read_csv(file_path))
    else:
        rows = list(read_json(file_path))

    if not rows:
        click.echo("No data rows.")
        return

    headers = rows[0].keys()
    for header in headers:
        try:
            numbers = [float(r[header]) for r in rows]
        except ValueError:
            continue

        if stat == 'mean':
            click.echo(f"{header} (mean): {column_mean(numbers):.2f}")
        else:
            # Intentional bug: column_median expects list but receives tuple (won't break but diff)
            median = column_median(tuple(numbers))  # type: ignore
            click.echo(f"{header} (median): {median:.2f}")

if __name__ == '__main__':
    main()
