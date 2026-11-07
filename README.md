# asset-location-tracker

Group assets by site and flag any with no recorded location first — the ones most likely to go missing in an audit.

## How to run

```sh
python3 main.py assets.csv
```

## Example output

```
LT-104: UNKNOWN LOCATION
HQ: 58 asset(s)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
