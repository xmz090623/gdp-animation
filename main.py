# /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import argparse
import pandas_alive
import warnings

GIF_TITLE = "Top 15 Countries GDP 1960-2020 (Unit: Billon Dollars)"

def argparser():
    args_parser = argparse.ArgumentParser(description='GDP Animation GIF generator')

    args_parser.add_argument('--csv-file', '-f',
                             required=True,
                             help='The name of CSV file including the GDP data')

    args_parser.add_argument('--gif-file', '-g',
                             required=True,
                             help='The name of generated Gif file')

    args_parser.add_argument('--period-length', '-i',
                             default=1000,
                             help='Period of interpolating next year data in millisecond')

    args = args_parser.parse_args()

    return args

def current_china_gdp(gdp_year_values):
    china_gdp = gdp_year_values['China']
    s = f'Peoples Republic of China GDP: {int(china_gdp)} Billion Dollars'

    return {
        'x': .85,
        'y': .2,
        's': s,
        'ha': 'right',
        'size': 9
    }

def gdp_gif_gen(
        csv_file_name: str = None,
        gif_file_name: str = None,
        title: str = None,
        period_length: int = 10):

    gdp_animation_df = pd.read_csv(csv_file_name,
                                   index_col=0,
                                   parse_dates=[0],
                                   thousands=',')
    gdp_animation_df.fillna(0).plot_animated(gif_file_name,
                                             period_fmt="%Y",
                                             title=title,
                                             n_visible=15,
                                             steps_per_period=15,
                                             period_length=period_length,
                                             period_summary_func=current_china_gdp
                                             )

if __name__ == "__main__":
    _args = argparser()
    csv_file_name = _args.csv_file
    gif_file_name = _args.gif_file
    title = GIF_TITLE
    period_length = _args.period_length

    warnings.filterwarnings("ignore")
    gdp_gif_gen(
        csv_file_name=csv_file_name,
        gif_file_name=gif_file_name,
        title=title,
        period_length=period_length
    )
