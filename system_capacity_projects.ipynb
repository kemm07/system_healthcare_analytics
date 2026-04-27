{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-t5VLKQch_t0"
      },
      "source": [
        "#System Capacity & Care Load Analytics for Unaccompanied Children\n",
        "\n",
        "Detailed guide and project requirements for the System Capacity & Care Load Analytics for Unaccompanied Children analysis."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-LbsH-7ChZxF",
        "outputId": "48645065-03eb-466c-b5db-f3a72d8603ce"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "        date  children_apprehended_and_placed_in_cbp_custody  \\\n",
            "0 2025-12-21                                               6   \n",
            "1 2025-12-18                                              11   \n",
            "2 2025-12-17                                               7   \n",
            "3 2025-12-16                                               8   \n",
            "4 2025-12-15                                              11   \n",
            "\n",
            "   children_in_cbp_custody  children_transferred_out_of_cbp_custody  \\\n",
            "0                       18                                       11   \n",
            "1                       50                                        6   \n",
            "2                       31                                       11   \n",
            "3                       54                                       15   \n",
            "4                       42                                        9   \n",
            "\n",
            "   children_in_hhs_care  children_discharged_from_hhs_care  \n",
            "0                  2484                                 14  \n",
            "1                  2472                                 16  \n",
            "2                  2481                                 10  \n",
            "3                  2468                                  9  \n",
            "4                  2470                                  7  \n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 1170 entries, 0 to 1169\n",
            "Data columns (total 6 columns):\n",
            " #   Column                                          Non-Null Count  Dtype         \n",
            "---  ------                                          --------------  -----         \n",
            " 0   date                                            720 non-null    datetime64[ns]\n",
            " 1   children_apprehended_and_placed_in_cbp_custody  1170 non-null   int64         \n",
            " 2   children_in_cbp_custody                         1170 non-null   int64         \n",
            " 3   children_transferred_out_of_cbp_custody         1170 non-null   int64         \n",
            " 4   children_in_hhs_care                            1170 non-null   int64         \n",
            " 5   children_discharged_from_hhs_care               1170 non-null   int64         \n",
            "dtypes: datetime64[ns](1), int64(5)\n",
            "memory usage: 55.0 KB\n",
            "None\n",
            "                                date  \\\n",
            "count                            720   \n",
            "mean   2024-07-06 05:29:59.999999744   \n",
            "min              2023-01-12 00:00:00   \n",
            "25%              2023-10-16 18:00:00   \n",
            "50%              2024-07-05 12:00:00   \n",
            "75%              2025-03-25 06:00:00   \n",
            "max              2025-12-21 00:00:00   \n",
            "std                              NaN   \n",
            "\n",
            "       children_apprehended_and_placed_in_cbp_custody  \\\n",
            "count                                     1170.000000   \n",
            "mean                                        57.552991   \n",
            "min                                          0.000000   \n",
            "25%                                          0.000000   \n",
            "50%                                          9.000000   \n",
            "75%                                        115.000000   \n",
            "max                                        333.000000   \n",
            "std                                         72.924368   \n",
            "\n",
            "       children_in_cbp_custody  children_transferred_out_of_cbp_custody  \\\n",
            "count              1170.000000                              1170.000000   \n",
            "mean                105.535043                                79.180342   \n",
            "min                   0.000000                                 0.000000   \n",
            "25%                   0.000000                                 0.000000   \n",
            "50%                  29.000000                                11.000000   \n",
            "75%                 220.000000                               169.000000   \n",
            "max                 531.000000                               440.000000   \n",
            "std                 129.563500                                98.728672   \n",
            "\n",
            "       children_in_hhs_care  children_discharged_from_hhs_care  \n",
            "count           1170.000000                        1170.000000  \n",
            "mean            3730.015385                         106.711966  \n",
            "min                0.000000                           0.000000  \n",
            "25%                0.000000                           0.000000  \n",
            "50%             2317.000000                          14.000000  \n",
            "75%             7277.750000                         210.000000  \n",
            "max            11516.000000                         505.000000  \n",
            "std             3693.194428                         129.776191  \n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "df = pd.read_csv('/content/drive/MyDrive/Cognifyz_project/HHS_Unaccompanied_Alien_Children_Program.csv')\n",
        "\n",
        "df.columns = df.columns.str.lower().str.replace('*', '', regex=False).str.replace(' ', '_')\n",
        "\n",
        "df['date'] = pd.to_datetime(df['date'], errors='coerce')\n",
        "\n",
        "numeric_cols = ['children_apprehended_and_placed_in_cbp_custody', 'children_in_cbp_custody',\n",
        "                'children_transferred_out_of_cbp_custody', 'children_in_hhs_care',\n",
        "                'children_discharged_from_hhs_care']\n",
        "for col in numeric_cols:\n",
        "    df[col] = df[col].astype(str).str.replace(',', '', regex=False)\n",
        "    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)\n",
        "\n",
        "df = df.dropna(how='all').sort_values('date', ascending=False).reset_index(drop=True)\n",
        "\n",
        "print(df.head())\n",
        "print(df.info())\n",
        "print(df.describe())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "786ed7b0",
        "outputId": "25e4bea0-bdd8-43f0-8859-d07830120a39"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "        date  children_apprehended_and_placed_in_cbp_custody  \\\n",
            "0 2025-12-21                                               6   \n",
            "1 2025-12-18                                              11   \n",
            "2 2025-12-17                                               7   \n",
            "3 2025-12-16                                               8   \n",
            "4 2025-12-15                                              11   \n",
            "\n",
            "   children_in_cbp_custody  children_transferred_out_of_cbp_custody  \\\n",
            "0                       18                                       11   \n",
            "1                       50                                        6   \n",
            "2                       31                                       11   \n",
            "3                       54                                       15   \n",
            "4                       42                                        9   \n",
            "\n",
            "   children_in_hhs_care  children_discharged_from_hhs_care  \n",
            "0                  2484                                 14  \n",
            "1                  2472                                 16  \n",
            "2                  2481                                 10  \n",
            "3                  2468                                  9  \n",
            "4                  2470                                  7  \n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 1170 entries, 0 to 1169\n",
            "Data columns (total 6 columns):\n",
            " #   Column                                          Non-Null Count  Dtype         \n",
            "---  ------                                          --------------  -----         \n",
            " 0   date                                            720 non-null    datetime64[ns]\n",
            " 1   children_apprehended_and_placed_in_cbp_custody  1170 non-null   int64         \n",
            " 2   children_in_cbp_custody                         1170 non-null   int64         \n",
            " 3   children_transferred_out_of_cbp_custody         1170 non-null   int64         \n",
            " 4   children_in_hhs_care                            1170 non-null   int64         \n",
            " 5   children_discharged_from_hhs_care               1170 non-null   int64         \n",
            "dtypes: datetime64[ns](1), int64(5)\n",
            "memory usage: 55.0 KB\n",
            "None\n",
            "                                date  \\\n",
            "count                            720   \n",
            "mean   2024-07-06 05:29:59.999999744   \n",
            "min              2023-01-12 00:00:00   \n",
            "25%              2023-10-16 18:00:00   \n",
            "50%              2024-07-05 12:00:00   \n",
            "75%              2025-03-25 06:00:00   \n",
            "max              2025-12-21 00:00:00   \n",
            "std                              NaN   \n",
            "\n",
            "       children_apprehended_and_placed_in_cbp_custody  \\\n",
            "count                                     1170.000000   \n",
            "mean                                        57.552991   \n",
            "min                                          0.000000   \n",
            "25%                                          0.000000   \n",
            "50%                                          9.000000   \n",
            "75%                                        115.000000   \n",
            "max                                        333.000000   \n",
            "std                                         72.924368   \n",
            "\n",
            "       children_in_cbp_custody  children_transferred_out_of_cbp_custody  \\\n",
            "count              1170.000000                              1170.000000   \n",
            "mean                105.535043                                79.180342   \n",
            "min                   0.000000                                 0.000000   \n",
            "25%                   0.000000                                 0.000000   \n",
            "50%                  29.000000                                11.000000   \n",
            "75%                 220.000000                               169.000000   \n",
            "max                 531.000000                               440.000000   \n",
            "std                 129.563500                                98.728672   \n",
            "\n",
            "       children_in_hhs_care  children_discharged_from_hhs_care  \n",
            "count           1170.000000                        1170.000000  \n",
            "mean            3730.015385                         106.711966  \n",
            "min                0.000000                           0.000000  \n",
            "25%                0.000000                           0.000000  \n",
            "50%             2317.000000                          14.000000  \n",
            "75%             7277.750000                         210.000000  \n",
            "max            11516.000000                         505.000000  \n",
            "std             3693.194428                         129.776191  \n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "df = pd.read_csv('/content/drive/MyDrive/Cognifyz_project/HHS_Unaccompanied_Alien_Children_Program.csv')\n",
        "\n",
        "df.columns = df.columns.str.lower().str.replace('*', '', regex=False).str.replace(' ', '_')\n",
        "\n",
        "df['date'] = pd.to_datetime(df['date'], errors='coerce')\n",
        "\n",
        "numeric_cols = ['children_apprehended_and_placed_in_cbp_custody', 'children_in_cbp_custody',\n",
        "                'children_transferred_out_of_cbp_custody', 'children_in_hhs_care',\n",
        "                'children_discharged_from_hhs_care']\n",
        "for col in numeric_cols:\n",
        "    df[col] = df[col].astype(str).str.replace(',', '', regex=False)\n",
        "    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)\n",
        "\n",
        "df = df.dropna(how='all').sort_values('date', ascending=False).reset_index(drop=True)\n",
        "\n",
        "print(df.head())\n",
        "print(df.info())\n",
        "print(df.describe())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "iwIXFci0vMph"
      },
      "outputs": [],
      "source": [
        "import os\n",
        "\n",
        "\n",
        "df_agg = df.groupby('date')[numeric_cols].sum().reset_index()\n",
        "\n",
        "date_range = pd.date_range(start=df_agg['date'].min(), end=df_agg['date'].max(), freq='D')\n",
        "df = df_agg.set_index('date').reindex(date_range).reset_index().rename(columns={'index': 'date'})\n",
        "\n",
        "df[numeric_cols] = df[numeric_cols].interpolate(method='linear', limit_direction='both').fillna(0).astype(int)\n",
        "\n",
        "if not os.path.exists('data'):\n",
        "    os.makedirs('data')\n",
        "\n",
        "df.to_csv('data/uac_clean.csv', index=False)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GFjjVE9rvTJM",
        "outputId": "2d96665a-7aba-4e12-b342-a9e1ad467937"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "missing_dates: 0 issues\n",
            "invalid_rows: 121 issues\n",
            "         date  children_apprehended_and_placed_in_cbp_custody  \\\n",
            "12 2023-01-24                                              47   \n",
            "13 2023-01-25                                              20   \n",
            "14 2023-01-26                                              20   \n",
            "21 2023-02-02                                              15   \n",
            "22 2023-02-03                                              15   \n",
            "\n",
            "    children_in_cbp_custody  children_transferred_out_of_cbp_custody  \\\n",
            "12                       42                                       47   \n",
            "13                       22                                       41   \n",
            "14                       27                                       33   \n",
            "21                       13                                       23   \n",
            "22                       14                                       20   \n",
            "\n",
            "    children_in_hhs_care  children_discharged_from_hhs_care  \\\n",
            "12                  7433                                175   \n",
            "13                  7538                                180   \n",
            "14                  7521                                210   \n",
            "21                  7879                                298   \n",
            "22                  7781                                312   \n",
            "\n",
            "    invalid_transfers  invalid_discharges  \n",
            "12               True               False  \n",
            "13               True               False  \n",
            "14               True               False  \n",
            "21               True               False  \n",
            "22               True               False  \n",
            "negatives: 0 issues\n"
          ]
        }
      ],
      "source": [
        "import numpy as np\n",
        "\n",
        "def validate_data(df):\n",
        "    anomalies = {}\n",
        "\n",
        "    # Duplicates\n",
        "    duplicates = df[df.duplicated(subset=['date'], keep=False)]\n",
        "    if not duplicates.empty:\n",
        "        anomalies['duplicates'] = duplicates\n",
        "\n",
        "    missing_dates = df['date'].isna().sum()\n",
        "    anomalies['missing_dates'] = missing_dates\n",
        "\n",
        "    # Logical constraints\n",
        "    df['invalid_transfers'] = df['children_transferred_out_of_cbp_custody'] > df['children_in_cbp_custody']\n",
        "    df['invalid_discharges'] = df['children_discharged_from_hhs_care'] > df['children_in_hhs_care']\n",
        "    anomalies['invalid_rows'] = df[df['invalid_transfers'] | df['invalid_discharges']]\n",
        "\n",
        "    # Negatives\n",
        "    negatives = (df[numeric_cols] < 0).any(axis=1)\n",
        "    anomalies['negatives'] = df[negatives]\n",
        "\n",
        "    return anomalies\n",
        "\n",
        "# Usage in notebook\n",
        "anomalies = validate_data(df)\n",
        "for key, val in anomalies.items():\n",
        "    if isinstance(val, (int, np.integer)):\n",
        "        print(f\"{key}: {val} issues\")\n",
        "    else:\n",
        "        print(f\"{key}: {len(val)} issues\")\n",
        "        if not val.empty:\n",
        "            print(val.head())"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LPw1tXhYBHUU"
      },
      "source": [
        "#Phase 2: Data Quality & Validation"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "06J3r9NQA-VE",
        "outputId": "ee341ab5-fc5c-4c53-fb86-39423b4e460b"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "missing_dates: 0 issues\n",
            "invalid_rows: 121 issues\n",
            "         date  children_apprehended_and_placed_in_cbp_custody  \\\n",
            "12 2023-01-24                                              47   \n",
            "13 2023-01-25                                              20   \n",
            "14 2023-01-26                                              20   \n",
            "21 2023-02-02                                              15   \n",
            "22 2023-02-03                                              15   \n",
            "\n",
            "    children_in_cbp_custody  children_transferred_out_of_cbp_custody  \\\n",
            "12                       42                                       47   \n",
            "13                       22                                       41   \n",
            "14                       27                                       33   \n",
            "21                       13                                       23   \n",
            "22                       14                                       20   \n",
            "\n",
            "    children_in_hhs_care  children_discharged_from_hhs_care  \\\n",
            "12                  7433                                175   \n",
            "13                  7538                                180   \n",
            "14                  7521                                210   \n",
            "21                  7879                                298   \n",
            "22                  7781                                312   \n",
            "\n",
            "    invalid_transfers  invalid_discharges  \n",
            "12               True               False  \n",
            "13               True               False  \n",
            "14               True               False  \n",
            "21               True               False  \n",
            "22               True               False  \n",
            "negatives: 0 issues\n"
          ]
        }
      ],
      "source": [
        "def validate_data(df):\n",
        "    anomalies = {}\n",
        "\n",
        "    # Duplicates\n",
        "    duplicates = df[df.duplicated(subset=['date'], keep=False)]\n",
        "    if not duplicates.empty:\n",
        "        anomalies['duplicates'] = duplicates\n",
        "\n",
        "    missing_dates = df['date'].isna().sum()\n",
        "    anomalies['missing_dates'] = missing_dates\n",
        "\n",
        "    # Logical constraints\n",
        "    df['invalid_transfers'] = df['children_transferred_out_of_cbp_custody'] > df['children_in_cbp_custody']\n",
        "    df['invalid_discharges'] = df['children_discharged_from_hhs_care'] > df['children_in_hhs_care']\n",
        "    anomalies['invalid_rows'] = df[df['invalid_transfers'] | df['invalid_discharges']]\n",
        "\n",
        "    # Negatives\n",
        "    negatives = (df[numeric_cols] < 0).any(axis=1)\n",
        "    anomalies['negatives'] = df[negatives]\n",
        "\n",
        "    return anomalies\n",
        "\n",
        "# Usage in notebook\n",
        "anomalies = validate_data(df)\n",
        "for key, val in anomalies.items():\n",
        "    if isinstance(val, (int, np.integer)):\n",
        "        print(f\"{key}: {val} issues\")\n",
        "    else:\n",
        "        print(f\"{key}: {len(val)} issues\")\n",
        "        if not val.empty:\n",
        "            print(val.head())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "35970b60",
        "outputId": "00d9878b-3b30-40c2-b6ae-848c2883e0b6"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "--- Validation after correction ---\n",
            "missing_dates: 0 issues\n",
            "invalid_rows: 0 issues\n",
            "negatives: 0 issues\n"
          ]
        }
      ],
      "source": [
        "df.loc[df['invalid_transfers'], 'children_transferred_out_of_cbp_custody'] = df['children_in_cbp_custody']\n",
        "\n",
        "\n",
        "anomalies = validate_data(df)\n",
        "print(\"--- Validation after correction ---\")\n",
        "for key, val in anomalies.items():\n",
        "    if isinstance(val, (int, np.integer)):\n",
        "        print(f\"{key}: {val} issues\")\n",
        "    else:\n",
        "        print(f\"{key}: {len(val)} issues\")\n",
        "        if not val.empty:\n",
        "            print(val.head())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "eYNUaIG0BRnd"
      },
      "outputs": [],
      "source": [
        "def compute_metrics(df):\n",
        "    df['total_system_load'] = df['children_in_cbp_custody'] + df['children_in_hhs_care']\n",
        "    df['net_daily_intake'] = df['children_transferred_out_of_cbp_custody'] - df['children_discharged_from_hhs_care']\n",
        "    df['care_load_growth_rate'] = df['children_in_hhs_care'].pct_change() * 100\n",
        "    df['backlog_indicator'] = df['net_daily_intake'].clip(lower=0).rolling(window=7).sum()  # sustained positive\n",
        "\n",
        "    return df\n",
        "\n",
        "df = compute_metrics(df)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "uoLwrsScBWkn"
      },
      "source": [
        "KPIs (from project table)\n",
        "Total Children Under Care = Total System Load (avg/peak)\n",
        "Net Intake Pressure = Avg net_daily_intake\n",
        "Care Load Volatility Index = Std dev of care_load_growth_rate\n",
        "Backlog Accumulation Rate = Avg backlog_indicator\n",
        "Discharge Offset Ratio = Discharges / Transfers (ability to relieve)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vbsTmISQBX8y",
        "outputId": "85e986a2-4267-4b71-f3d3-34ae099f4cab"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "                                  Value\n",
            "total_children_under_care   6231.535814\n",
            "net_intake_pressure          -54.771163\n",
            "care_load_volatility_index     1.079895\n",
            "backlog_accumulation_rate     75.100094\n",
            "discharge_offset_ratio         1.428538\n"
          ]
        }
      ],
      "source": [
        "kpis = {\n",
        "    'total_children_under_care': df['total_system_load'].mean(),\n",
        "    'net_intake_pressure': df['net_daily_intake'].mean(),\n",
        "    'care_load_volatility_index': df['care_load_growth_rate'].std(),\n",
        "    'backlog_accumulation_rate': df['backlog_indicator'].mean(),\n",
        "    'discharge_offset_ratio': df['children_discharged_from_hhs_care'].sum() / df['children_transferred_out_of_cbp_custody'].sum()\n",
        "}\n",
        "\n",
        "kpi_df = pd.DataFrame.from_dict(kpis, orient='index', columns=['Value'])\n",
        "print(kpi_df)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MbD9Mk5QBm2H"
      },
      "source": [
        "Pressure/Stress"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "C1tlMHTwBnYN",
        "outputId": "5589ae24-1552-4c90-9b71-e88dffc4f432"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "          date  children_apprehended_and_placed_in_cbp_custody  \\\n",
            "166 2023-06-27                                             154   \n",
            "167 2023-06-28                                              91   \n",
            "168 2023-06-29                                              81   \n",
            "169 2023-06-30                                             123   \n",
            "170 2023-07-01                                             166   \n",
            "\n",
            "     children_in_cbp_custody  children_transferred_out_of_cbp_custody  \\\n",
            "166                      225                                      220   \n",
            "167                      199                                      172   \n",
            "168                      213                                      153   \n",
            "169                      237                                      163   \n",
            "170                      261                                      173   \n",
            "\n",
            "     children_in_hhs_care  children_discharged_from_hhs_care  \\\n",
            "166                  5917                                155   \n",
            "167                  5999                                174   \n",
            "168                  6058                                213   \n",
            "169                  6006                                245   \n",
            "170                  5954                                277   \n",
            "\n",
            "     invalid_transfers  invalid_discharges  total_system_load  \\\n",
            "166              False               False               6142   \n",
            "167              False               False               6198   \n",
            "168              False               False               6271   \n",
            "169              False               False               6243   \n",
            "170              False               False               6215   \n",
            "\n",
            "     net_daily_intake  care_load_growth_rate  backlog_indicator  \\\n",
            "166                65               1.684138               85.0   \n",
            "167                -2               1.385837               65.0   \n",
            "168               -60               0.983497               65.0   \n",
            "169               -82              -0.858369               65.0   \n",
            "170              -104              -0.865801               65.0   \n",
            "\n",
            "     rolling_avg_hhs  volatility  strain_period  \n",
            "166      5871.571429  106.000337           True  \n",
            "167      5882.571429   98.480907           True  \n",
            "168      5897.142857  101.087629           True  \n",
            "169      5913.428571  105.209080           True  \n",
            "170      5931.285714  106.519487           True  \n"
          ]
        }
      ],
      "source": [
        "df['rolling_avg_hhs'] = df['children_in_hhs_care'].rolling(7).mean()\n",
        "df['volatility'] = df['children_in_hhs_care'].rolling(14).std()\n",
        "\n",
        "\n",
        "df['strain_period'] = (df['backlog_indicator'] > 50) & (df['volatility'] > 20)\n",
        "\n",
        "print(df[df['strain_period']].head())"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3lRRR3HfBppm"
      },
      "source": [
        "#Phase 5: Streamlit Web Application"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FZu6yKvgBsnI",
        "outputId": "38b07031-bca9-40bf-c455-41dfe3af10f4"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "2026-04-22 11:56:56.256 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.258 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.260 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.271 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.272 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.272 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.274 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.275 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.276 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.278 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.278 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.280 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.282 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.283 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.284 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.285 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.288 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.289 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.290 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.328 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.328 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.329 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.331 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.332 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.334 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.336 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.338 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.393 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.394 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.395 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.397 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.398 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.401 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.401 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.402 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.438 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.439 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.441 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.443 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.445 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.447 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.448 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.450 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.452 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.455 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.456 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.457 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-04-22 11:56:56.459 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ],
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import plotly.express as px\n",
        "\n",
        "st.title('UAC Care Load Analytics Dashboard')\n",
        "\n",
        "# Load data\n",
        "df = pd.read_csv('data/uac_clean.csv')\n",
        "df = compute_metrics(df)\n",
        "df['date'] = pd.to_datetime(df['date'])\n",
        "\n",
        "# User capabilities\n",
        "date_range = st.date_input('Select Date Range', [df['date'].min(), df['date'].max()])\n",
        "granularity = st.selectbox('Time Granularity', ['Daily', 'Weekly', 'Monthly'])\n",
        "\n",
        "# Filter\n",
        "mask = (df['date'] >= pd.to_datetime(date_range[0])) & (df['date'] <= pd.to_datetime(date_range[1]))\n",
        "df_filtered = df[mask]\n",
        "\n",
        "if granularity == 'Weekly':\n",
        "    df_filtered = df_filtered.resample('W', on='date').mean().reset_index()\n",
        "\n",
        "# System Load Overview\n",
        "st.subheader('System Load Overview')\n",
        "fig_load = px.line(df_filtered, x='date', y='total_system_load')\n",
        "st.plotly_chart(fig_load)\n",
        "\n",
        "# CBP vs HHS Comparison\n",
        "st.subheader('CBP vs HHS Load')\n",
        "fig_compare = px.bar(df_filtered, x='date', y=['children_in_cbp_custody', 'children_in_hhs_care'], barmode='stack')\n",
        "st.plotly_chart(fig_compare)\n",
        "\n",
        "# Net Intake & Backlog\n",
        "st.subheader('Net Intake & Backlog Trends')\n",
        "fig_intake = px.area(df_filtered, x='date', y='net_daily_intake')\n",
        "st.plotly_chart(fig_intake)\n",
        "\n",
        "# KPI Cards\n",
        "st.subheader('Key Performance Indicators')\n",
        "kpis = {  # compute as above\n",
        "    'Total Under Care': df_filtered['total_system_load'].mean()\n",
        "    # ... add others\n",
        "}\n",
        "cols = st.columns(len(kpis))\n",
        "for i, (name, val) in enumerate(kpis.items()):\n",
        "    cols[i].metric(name, f\"{val:.2f}\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import pandas as pd\n",
        "\n",
        "\n",
        "df = pd.read_csv('/content/drive/MyDrive/Cognifyz_project/HHS_Unaccompanied_Alien_Children_Program.csv')\n",
        "\n",
        "\n",
        "df.columns = df.columns.str.lower().str.replace('*', '', regex=False).str.replace(' ', '_')\n",
        "df['date'] = pd.to_datetime(df['date'], errors='coerce')\n",
        "\n",
        "numeric_cols = [\n",
        "    'children_apprehended_and_placed_in_cbp_custody',\n",
        "    'children_in_cbp_custody',\n",
        "    'children_transferred_out_of_cbp_custody',\n",
        "    'children_in_hhs_care',\n",
        "    'children_discharged_from_hhs_care'\n",
        "]\n",
        "for col in numeric_cols:\n",
        "    df[col] = df[col].astype(str).str.replace(',', '', regex=False)\n",
        "    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)\n",
        "\n",
        "df = df.dropna(how='all').sort_values('date').reset_index(drop=True)\n",
        "\n",
        "# Step 3: Resample to fill date gaps\n",
        "df_agg = df.groupby('date')[numeric_cols].sum().reset_index()\n",
        "date_range = pd.date_range(start=df_agg['date'].min(), end=df_agg['date'].max(), freq='D')\n",
        "df = df_agg.set_index('date').reindex(date_range).reset_index().rename(columns={'index': 'date'})\n",
        "df[numeric_cols] = df[numeric_cols].interpolate(method='linear', limit_direction='both').fillna(0).astype(int)\n",
        "\n",
        "# Step 4: Save cleaned CSV ✅ This is what app.py needs\n",
        "os.makedirs('/content/data', exist_ok=True)\n",
        "df.to_csv('/content/data/uac_clean.csv', index=False)\n",
        "\n",
        "print(\"✅ uac_clean.csv created successfully at /content/data/\")\n",
        "print(f\"   Shape: {df.shape}\")\n",
        "print(df.head(3))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Sam7yXSzyQQJ",
        "outputId": "e57b1e0f-d214-4f4b-f757-db7ce1766c0a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ uac_clean.csv created successfully at /content/data/\n",
            "   Shape: (1075, 6)\n",
            "        date  children_apprehended_and_placed_in_cbp_custody  \\\n",
            "0 2023-01-12                                              33   \n",
            "1 2023-01-13                                              32   \n",
            "2 2023-01-14                                              32   \n",
            "\n",
            "   children_in_cbp_custody  children_transferred_out_of_cbp_custody  \\\n",
            "0                       53                                       34   \n",
            "1                       52                                       34   \n",
            "2                       52                                       35   \n",
            "\n",
            "   children_in_hhs_care  children_discharged_from_hhs_care  \n",
            "0                  6566                                436  \n",
            "1                  6621                                415  \n",
            "2                  6677                                394  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "df = pd.read_csv('/content/data/uac_clean.csv')"
      ],
      "metadata": {
        "id": "qi-P0kLHycCC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "app_code = '''\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import plotly.express as px\n",
        "import os\n",
        "\n",
        "st.title('UAC Care Load Analytics Dashboard')\n",
        "\n",
        "# Load data\n",
        "df = pd.read_csv('/content/data/uac_clean.csv')\n",
        "'''\n",
        "\n",
        "with open('/content/app.py', 'w') as f:\n",
        "    f.write(app_code)\n",
        "\n",
        "print(\"✅ app.py updated successfully\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JZUcfzijz3Da",
        "outputId": "b260c2ac-97b6-4f03-989e-7e6db7331400"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ app.py updated successfully\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "fnyNSJheT4qp"
      },
      "outputs": [],
      "source": [
        "! pip install streamlit -q"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sgfaMdJDT4Mz",
        "outputId": "ed6d3191-d7b3-43cb-bca0-6b7ccbf1bc6b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2026-04-26 22:03:38--  http://-/\n",
            "Resolving - (-)... failed: Name or service not known.\n",
            "wget: unable to resolve host address ‘-’\n",
            "--2026-04-26 22:03:38--  http://ipv4.icanhazip.com/\n",
            "Resolving ipv4.icanhazip.com (ipv4.icanhazip.com)... 104.16.184.241, 104.16.185.241\n",
            "Connecting to ipv4.icanhazip.com (ipv4.icanhazip.com)|104.16.184.241|:80... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 13 [text/plain]\n",
            "Saving to: ‘index.html’\n",
            "\n",
            "     0K                                                       100% 1.40M=0s\n",
            "\n",
            "2026-04-26 22:03:38 (1.40 MB/s) - ‘index.html’ saved [13/13]\n",
            "\n",
            "FINISHED --2026-04-26 22:03:38--\n",
            "Total wall clock time: 0.06s\n",
            "Downloaded: 1 files, 13 in 0s (1.40 MB/s)\n"
          ]
        }
      ],
      "source": [
        "!wget -  -o - ipv4.icanhazip.com"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "deace817",
        "outputId": "33b46ac9-311d-4036-b28a-6e96613f964a"
      },
      "source": [
        "# Reinstall streamlit to ensure it's available in the current environment\n",
        "! pip install streamlit -q"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.1/9.1 MB\u001b[0m \u001b[31m62.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m11.3/11.3 MB\u001b[0m \u001b[31m87.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4f391315",
        "outputId": "570a2996-edc7-44af-eccd-6362e6a0b5c1"
      },
      "source": [
        "! python -m streamlit run app.py & npx localtunnel --port 8501"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[1G\u001b[0K⠙\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\u001b[0m\n",
            "\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K\u001b[1G\u001b[0JNeed to install the following packages:\n",
            "localtunnel@2.0.2\n",
            "Ok to proceed? (y) \u001b[20G\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Local URL: \u001b[0m\u001b[1mhttp://localhost:8501\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://35.227.60.49:8501\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Stopping...\u001b[0m\n",
            "^C\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "79e05a40",
        "outputId": "33e0ca70-df53-42a0-96b2-cdc2fcdfb39d"
      },
      "source": [
        "streamlit_code = '''\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import plotly.express as px\n",
        "import os\n",
        "\n",
        "st.title('UAC Care Load Analytics Dashboard')\n",
        "\n",
        "# Load data\n",
        "df = pd.read_csv('/content/data/uac_clean.csv')\n",
        "\n",
        "def compute_metrics(df):\n",
        "    df['total_system_load'] = df['children_in_cbp_custody'] + df['children_in_hhs_care']\n",
        "    df['net_daily_intake'] = df['children_transferred_out_of_cbp_custody'] - df['children_discharged_from_hhs_care']\n",
        "    df['care_load_growth_rate'] = df['children_in_hhs_care'].pct_change() * 100\n",
        "    df['backlog_indicator'] = df['net_daily_intake'].clip(lower=0).rolling(window=7).sum()  # sustained positive\n",
        "    return df\n",
        "\n",
        "df = compute_metrics(df)\n",
        "df['date'] = pd.to_datetime(df['date'])\n",
        "\n",
        "# User capabilities\n",
        "date_range = st.date_input('Select Date Range', [df['date'].min(), df['date'].max()])\n",
        "granularity = st.selectbox('Time Granularity', ['Daily', 'Weekly', 'Monthly'])\n",
        "\n",
        "# Filter\n",
        "mask = (df['date'] >= pd.to_datetime(date_range[0])) & (df['date'] <= pd.to_datetime(date_range[1]))\n",
        "df_filtered = df[mask]\n",
        "\n",
        "if granularity == 'Weekly':\n",
        "    df_filtered = df_filtered.resample('W', on='date').mean().reset_index()\n",
        "\n",
        "# System Load Overview\n",
        "st.subheader('System Load Overview')\n",
        "fig_load = px.line(df_filtered, x='date', y='total_system_load')\n",
        "st.plotly_chart(fig_load)\n",
        "\n",
        "# CBP vs HHS Comparison\n",
        "st.subheader('CBP vs HHS Load')\n",
        "fig_compare = px.bar(df_filtered, x='date', y=['children_in_cbp_custody', 'children_in_hhs_care'], barmode='stack')\n",
        "st.plotly_chart(fig_compare)\n",
        "\n",
        "# Net Intake & Backlog\n",
        "st.subheader('Net Intake & Backlog Trends')\n",
        "fig_intake = px.area(df_filtered, x='date', y='net_daily_intake')\n",
        "st.plotly_chart(fig_intake)\n",
        "\n",
        "# KPI Cards\n",
        "st.subheader('Key Performance Indicators')\n",
        "kpis = {  # compute as above\n",
        "    'Total Under Care': df_filtered['total_system_load'].mean()\n",
        "    # ... add others\n",
        "}\n",
        "cols = st.columns(len(kpis))\n",
        "for i, (name, val) in enumerate(kpis.items()):\n",
        "    cols[i].metric(name, f\"{val:.2f}\")\n",
        "'''\n",
        "\n",
        "with open('app.py', 'w') as f:\n",
        "    f.write(streamlit_code)\n",
        "\n",
        "print('Streamlit app regenerated to app.py with full dashboard code')\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Streamlit app regenerated to app.py with full dashboard code\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9217d3ee",
        "outputId": "0ebf78ab-3885-4275-bab5-6bf6f9343bae"
      },
      "source": [
        "import os\n",
        "\n",
        "log_file_path = 'streamlit.log'\n",
        "\n",
        "if os.path.exists(log_file_path):\n",
        "    with open(log_file_path, 'r') as f:\n",
        "        log_content = f.read()\n",
        "    print(log_content)\n",
        "else:\n",
        "    print(f\"Log file not found at: {log_file_path}\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\n",
            "\n",
            "  You can now view your Streamlit app in your browser.\n",
            "\n",
            "  Local URL: http://localhost:8501\n",
            "  Network URL: http://172.28.0.12:8501\n",
            "  External URL: http://35.227.60.49:8501\n",
            "\n",
            "  Stopping...\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "763ae1ea"
      },
      "source": [
        "# Install ngrok\n",
        "!pip install pyngrok -q"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "17751298",
        "outputId": "74ac9f79-7fc1-41dd-8863-9b53a605f8a8"
      },
      "source": [
        "from pyngrok import ngrok\n",
        "\n",
        "\n",
        "ngrok.kill()\n",
        "YOUR_AUTHTOKEN = \"3CuibFxTXzAgKi7nGLhw5EDopVS_32BL4r9xykoNmt5Px1KYi\"\n",
        "\n",
        "NGROK_AUTH_TOKEN = \"3CuibFxTXzAgKi7nGLhw5EDopVS_32BL4r9xykoNmt5Px1KYi\"\n",
        "\n",
        "if NGROK_AUTH_TOKEN == \"3CuibFxTXzAgKi7nGLhw5EDopVS_32BL4r9xykoNmt5Px1KYi\":\n",
        "    print(\"Please replace '3CuibFxTXzAgKi7nGLhw5EDopVS_32BL4r9xykoNmt5Px1KYi' with your actual ngrok authtoken from ngrok.com\")\n",
        "else:\n",
        "    ngrok.set_auth_token(NGROK_AUTH_TOKEN)\n",
        "\n",
        "\n",
        "    !nohup python -m streamlit run app.py > streamlit_ngrok.log 2>&1 &\n",
        "\n",
        "\n",
        "    public_url = ngrok.connect(8501)\n",
        "    print(f\"Streamlit app is available at: {public_url}\")\n",
        "    print(\"Check streamlit_ngrok.log for Streamlit output.\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please replace '3CuibFxTXzAgKi7nGLhw5EDopVS_32BL4r9xykoNmt5Px1KYi' with your actual ngrok authtoken from ngrok.com\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "93821230",
        "outputId": "a593de1b-4dc0-46c4-925e-176f4b97a39f"
      },
      "source": [
        "# Run Streamlit in the background and then start localtunnel\n",
        "!nohup python -m streamlit run app.py > streamlit.log 2>&1 & \\\n",
        "yes | npx localtunnel --port 8501\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K⠇\u001b[1G\u001b[0K⠏\u001b[1G\u001b[0K⠋\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0Kyour url is: https://violet-crabs-dress.loca.lt\n",
            "^C\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1bj27iLW78Kj9XOjz8_Y5AF5oFvLzm2Rn",
      "authorship_tag": "ABX9TyPQK6QuqJwzEW/pFoJwn5pJ"
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}