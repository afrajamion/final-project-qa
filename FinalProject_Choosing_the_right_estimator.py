{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/afrajamion/final-project-qa/blob/main/FinalProject_Choosing_the_right_estimator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "b-MeKKMs55WA"
      },
      "source": [
        "# Practical Machine Learning \n",
        "### Project: Model Selection"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FEge15Hl55WD"
      },
      "source": [
        "# Abstract"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rmJJOdz955WE"
      },
      "source": [
        "# Part 1: Business and Data Understanding"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "K_EWcKs255WG"
      },
      "source": [
        "### Q. Identify a suitable dataset for your canditate question(s)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NA2qaEL155WH"
      },
      "source": [
        "Go have a look at any of these websites:\n",
        "\n",
        "* https://www.kaggle.com/datasets \n",
        "* https://datasetsearch.research.google.com/\n",
        "* https://data.gov.uk/\n",
        "\n",
        "Find an interesting looking data set related to your problem domain and get a copy of it\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 70,
      "metadata": {
        "id": "HuoWXO_Q55WH"
      },
      "outputs": [],
      "source": [
        "# import the necessary libraries\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "# import dataset and assign to variable called heart\n",
        "heart = pd.read_csv(\"https://raw.githubusercontent.com/afrajamion/final-project-qa/main/heart.csv\", header=0)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# read dataset\n",
        "heart.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        },
        "id": "dHFQl6EMb7Hv",
        "outputId": "7950be1c-7fd8-4866-d2e7-2c3b5d0157e2"
      },
      "execution_count": 71,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  slope  \\\n",
              "0   63    1   3       145   233    1        0      150      0      2.3      0   \n",
              "1   37    1   2       130   250    0        1      187      0      3.5      0   \n",
              "2   41    0   1       130   204    0        0      172      0      1.4      2   \n",
              "3   56    1   1       120   236    0        1      178      0      0.8      2   \n",
              "4   57    0   0       120   354    0        1      163      1      0.6      2   \n",
              "\n",
              "   ca  thal  target  \n",
              "0   0     1       1  \n",
              "1   0     2       1  \n",
              "2   0     2       1  \n",
              "3   0     2       1  \n",
              "4   0     2       1  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-0e69c238-397d-4d72-9aa7-78b53cc9e5d4\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>age</th>\n",
              "      <th>sex</th>\n",
              "      <th>cp</th>\n",
              "      <th>trestbps</th>\n",
              "      <th>chol</th>\n",
              "      <th>fbs</th>\n",
              "      <th>restecg</th>\n",
              "      <th>thalach</th>\n",
              "      <th>exang</th>\n",
              "      <th>oldpeak</th>\n",
              "      <th>slope</th>\n",
              "      <th>ca</th>\n",
              "      <th>thal</th>\n",
              "      <th>target</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>63</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>145</td>\n",
              "      <td>233</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>150</td>\n",
              "      <td>0</td>\n",
              "      <td>2.3</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>37</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>130</td>\n",
              "      <td>250</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>187</td>\n",
              "      <td>0</td>\n",
              "      <td>3.5</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>41</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>130</td>\n",
              "      <td>204</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>172</td>\n",
              "      <td>0</td>\n",
              "      <td>1.4</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>56</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>120</td>\n",
              "      <td>236</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>178</td>\n",
              "      <td>0</td>\n",
              "      <td>0.8</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>57</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>120</td>\n",
              "      <td>354</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>163</td>\n",
              "      <td>1</td>\n",
              "      <td>0.6</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-0e69c238-397d-4d72-9aa7-78b53cc9e5d4')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-0e69c238-397d-4d72-9aa7-78b53cc9e5d4 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-0e69c238-397d-4d72-9aa7-78b53cc9e5d4');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 71
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "heart.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UL0wmuH4dur4",
        "outputId": "7ae5785b-f2f0-45e7-c686-7d5566e5ba6a"
      },
      "execution_count": 72,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(303, 14)"
            ]
          },
          "metadata": {},
          "execution_count": 72
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# check to see whether there are any missing values\n",
        "print(heart['age'].isnull().sum().sum())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7TmM3nonfZTv",
        "outputId": "139e9348-5af1-4ab5-9a14-998b37762850"
      },
      "execution_count": 73,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "t6sxB-Op55WF"
      },
      "source": [
        "### Q. Define the problem domain"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "KGICUusQ55WF"
      },
      "outputs": [],
      "source": [
        "# Target is an ideal label column because it is the result\n",
        "# The \"target\" field is the presence of heart disease in the patient. It is \n",
        "# an integer valued 0 = no/less chance of heart attack and 1 = more chance of heart attack\n",
        "# Useful for a doctor to see whether heart diseases leads to heart attacks, speed up the diagnosis and treatment process."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PasUNESl55WG"
      },
      "source": [
        "### Q. Identify candidate questions for your machine learning project"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 74,
      "metadata": {
        "id": "MgdRmrtq55WG",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "90b3b927-1c6f-49f0-b6e4-8b047add0826"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1    165\n",
              "0    138\n",
              "Name: target, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 74
        }
      ],
      "source": [
        "# value_counts\n",
        "# how many values do we have in target column?\n",
        "# LABEL COLUMN\n",
        "heart['target'].value_counts()\n",
        "\n",
        "# discrete or continuous numbers\n",
        "# These are discrete numbers, either they have heart disease = 1, or not = 0\n",
        "\n",
        "# what is label, what columns should be evaluated to become \n",
        "# features, Dimensions, Variables\n",
        "# Label is what you're attempting to predit = Target column, which is the output\n",
        "# Features are descriptive attributes = e.g., sex and age, which are the input\n",
        "# Dimensions is the number of input variables for a dataset = 13\n",
        "# For each category, there is a binary variable = 0 or 1."
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# can i use the dataset as-is or does it need cleaning? is answered below\n",
        "\n",
        "# type of columns\n",
        "heart.info()\n",
        "# can see there is no need to change types - all seem reasonable\n",
        "# also no columns to delete"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xx0Box8sklOI",
        "outputId": "792baa9b-817f-4141-e9b0-7afa3c0f36be"
      },
      "execution_count": 75,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 303 entries, 0 to 302\n",
            "Data columns (total 14 columns):\n",
            " #   Column    Non-Null Count  Dtype  \n",
            "---  ------    --------------  -----  \n",
            " 0   age       303 non-null    int64  \n",
            " 1   sex       303 non-null    int64  \n",
            " 2   cp        303 non-null    int64  \n",
            " 3   trestbps  303 non-null    int64  \n",
            " 4   chol      303 non-null    int64  \n",
            " 5   fbs       303 non-null    int64  \n",
            " 6   restecg   303 non-null    int64  \n",
            " 7   thalach   303 non-null    int64  \n",
            " 8   exang     303 non-null    int64  \n",
            " 9   oldpeak   303 non-null    float64\n",
            " 10  slope     303 non-null    int64  \n",
            " 11  ca        303 non-null    int64  \n",
            " 12  thal      303 non-null    int64  \n",
            " 13  target    303 non-null    int64  \n",
            "dtypes: float64(1), int64(13)\n",
            "memory usage: 33.3 KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# cardinality - count of unique values in a column\n",
        "for cname in heart.columns:\n",
        "  print(cname + \" : \" + str(heart[cname].value_counts().count()))\n",
        "\n",
        "# can see there are 302 entries, but none of the columns can be used as an index"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IVdJxwEuky9g",
        "outputId": "9ac628cd-eabc-4a66-d1fa-5c664d2547f7"
      },
      "execution_count": 76,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "age : 41\n",
            "sex : 2\n",
            "cp : 4\n",
            "trestbps : 49\n",
            "chol : 152\n",
            "fbs : 2\n",
            "restecg : 3\n",
            "thalach : 91\n",
            "exang : 2\n",
            "oldpeak : 40\n",
            "slope : 3\n",
            "ca : 5\n",
            "thal : 4\n",
            "target : 2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zsCo6Gmf55WH"
      },
      "source": [
        "### Q. Generate a descriptive statistics report for the columns in your dataset"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 77,
      "metadata": {
        "id": "1uvJKQH755WH",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 483
        },
        "outputId": "d253d5d1-9719-4220-92e6-9770aff861e0"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "          count        mean        std    min    25%    50%    75%    max\n",
              "age       303.0   54.366337   9.082101   29.0   47.5   55.0   61.0   77.0\n",
              "sex       303.0    0.683168   0.466011    0.0    0.0    1.0    1.0    1.0\n",
              "cp        303.0    0.966997   1.032052    0.0    0.0    1.0    2.0    3.0\n",
              "trestbps  303.0  131.623762  17.538143   94.0  120.0  130.0  140.0  200.0\n",
              "chol      303.0  246.264026  51.830751  126.0  211.0  240.0  274.5  564.0\n",
              "fbs       303.0    0.148515   0.356198    0.0    0.0    0.0    0.0    1.0\n",
              "restecg   303.0    0.528053   0.525860    0.0    0.0    1.0    1.0    2.0\n",
              "thalach   303.0  149.646865  22.905161   71.0  133.5  153.0  166.0  202.0\n",
              "exang     303.0    0.326733   0.469794    0.0    0.0    0.0    1.0    1.0\n",
              "oldpeak   303.0    1.039604   1.161075    0.0    0.0    0.8    1.6    6.2\n",
              "slope     303.0    1.399340   0.616226    0.0    1.0    1.0    2.0    2.0\n",
              "ca        303.0    0.729373   1.022606    0.0    0.0    0.0    1.0    4.0\n",
              "thal      303.0    2.313531   0.612277    0.0    2.0    2.0    3.0    3.0\n",
              "target    303.0    0.544554   0.498835    0.0    0.0    1.0    1.0    1.0"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-76eb53c1-5c1d-4cbb-908a-eaee46d82e5c\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>count</th>\n",
              "      <th>mean</th>\n",
              "      <th>std</th>\n",
              "      <th>min</th>\n",
              "      <th>25%</th>\n",
              "      <th>50%</th>\n",
              "      <th>75%</th>\n",
              "      <th>max</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>age</th>\n",
              "      <td>303.0</td>\n",
              "      <td>54.366337</td>\n",
              "      <td>9.082101</td>\n",
              "      <td>29.0</td>\n",
              "      <td>47.5</td>\n",
              "      <td>55.0</td>\n",
              "      <td>61.0</td>\n",
              "      <td>77.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>sex</th>\n",
              "      <td>303.0</td>\n",
              "      <td>0.683168</td>\n",
              "      <td>0.466011</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>cp</th>\n",
              "      <td>303.0</td>\n",
              "      <td>0.966997</td>\n",
              "      <td>1.032052</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2.0</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>trestbps</th>\n",
              "      <td>303.0</td>\n",
              "      <td>131.623762</td>\n",
              "      <td>17.538143</td>\n",
              "      <td>94.0</td>\n",
              "      <td>120.0</td>\n",
              "      <td>130.0</td>\n",
              "      <td>140.0</td>\n",
              "      <td>200.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>chol</th>\n",
              "      <td>303.0</td>\n",
              "      <td>246.264026</td>\n",
              "      <td>51.830751</td>\n",
              "      <td>126.0</td>\n",
              "      <td>211.0</td>\n",
              "      <td>240.0</td>\n",
              "      <td>274.5</td>\n",
              "      <td>564.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>fbs</th>\n",
              "      <td>303.0</td>\n",
              "      <td>0.148515</td>\n",
              "      <td>0.356198</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>restecg</th>\n",
              "      <td>303.0</td>\n",
              "      <td>0.528053</td>\n",
              "      <td>0.525860</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>thalach</th>\n",
              "      <td>303.0</td>\n",
              "      <td>149.646865</td>\n",
              "      <td>22.905161</td>\n",
              "      <td>71.0</td>\n",
              "      <td>133.5</td>\n",
              "      <td>153.0</td>\n",
              "      <td>166.0</td>\n",
              "      <td>202.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>exang</th>\n",
              "      <td>303.0</td>\n",
              "      <td>0.326733</td>\n",
              "      <td>0.469794</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>oldpeak</th>\n",
              "      <td>303.0</td>\n",
              "      <td>1.039604</td>\n",
              "      <td>1.161075</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.8</td>\n",
              "      <td>1.6</td>\n",
              "      <td>6.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>slope</th>\n",
              "      <td>303.0</td>\n",
              "      <td>1.399340</td>\n",
              "      <td>0.616226</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2.0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>ca</th>\n",
              "      <td>303.0</td>\n",
              "      <td>0.729373</td>\n",
              "      <td>1.022606</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>4.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>thal</th>\n",
              "      <td>303.0</td>\n",
              "      <td>2.313531</td>\n",
              "      <td>0.612277</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2.0</td>\n",
              "      <td>2.0</td>\n",
              "      <td>3.0</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>target</th>\n",
              "      <td>303.0</td>\n",
              "      <td>0.544554</td>\n",
              "      <td>0.498835</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-76eb53c1-5c1d-4cbb-908a-eaee46d82e5c')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-76eb53c1-5c1d-4cbb-908a-eaee46d82e5c button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-76eb53c1-5c1d-4cbb-908a-eaee46d82e5c');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 77
        }
      ],
      "source": [
        "heart.describe().T"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "toYhhJ4v55WI"
      },
      "source": [
        "# Part 2: Data Preparation"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zUDh9O2T55WI"
      },
      "source": [
        "### Q. Discuss the following types of missing data and how they would be handled in reference to your dataset where applicable.\n",
        "*\tMissing completely at random (MCAR)\n",
        "*\tMissing at random (MAR)\n",
        "*\tMissing Not at Random (MNAR)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 137,
      "metadata": {
        "id": "u0IiUxwR55WI",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9d11028e-540a-4357-cfe5-f9dc2db9ed24"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 303 entries, 0 to 302\n",
            "Data columns (total 15 columns):\n",
            " #   Column    Non-Null Count  Dtype  \n",
            "---  ------    --------------  -----  \n",
            " 0   age       303 non-null    int64  \n",
            " 1   sex       303 non-null    int64  \n",
            " 2   cp        303 non-null    int64  \n",
            " 3   trestbps  303 non-null    int64  \n",
            " 4   chol      303 non-null    int64  \n",
            " 5   fbs       303 non-null    int64  \n",
            " 6   restecg   303 non-null    int64  \n",
            " 7   thalach   303 non-null    int64  \n",
            " 8   exang     303 non-null    int64  \n",
            " 9   oldpeak   303 non-null    float64\n",
            " 10  slope     303 non-null    int64  \n",
            " 11  ca        303 non-null    int64  \n",
            " 12  thal      303 non-null    int64  \n",
            " 13  target    303 non-null    int64  \n",
            " 14  Zscore    303 non-null    float64\n",
            "dtypes: float64(2), int64(13)\n",
            "memory usage: 35.6 KB\n"
          ]
        }
      ],
      "source": [
        "heart.info()"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q. Is there any correlation in the data? How would you decide which columns to keep?"
      ],
      "metadata": {
        "id": "Z-_eDG2e_C2W"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# SEABORN and data.corr() to plot a heatmap\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "sns.heatmap(heart.corr(), annot=True, cmap=\"YlGnBu\")\n",
        "plt.show()\n",
        "# Github-> DFE6"
      ],
      "metadata": {
        "id": "_eRjAQ6u_CHm",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "outputId": "55bec264-e147-4581-883f-ff898e148b8b"
      },
      "execution_count": 138,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q. Is there any imbalance in the label\n",
        "?"
      ],
      "metadata": {
        "id": "EUIqah7h_LAW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# LABEL COLUMN-> Y/value you want to predict\n",
        "# target column from heart\n",
        "heart['target'].value_counts()\n",
        "# Cat = 100, Parrot= 50, Ant= 5\n",
        "# either no action action required or just del extra rows!\n",
        "\n",
        "# if one class is less than quarter of the other class,\n",
        "# the data is imbalanced!\n",
        "#\n",
        "# Regression- NO ACTION REQUIRED. \n",
        "# Classification (LABEL/Y) - Diagnosis\n",
        "# 1) Del some of the rows of the larger dataset \n",
        "# 2) OR generate FAKE/SIMULATED data \n",
        "# 3) Ignore if you want to take a leap of faith in the model"
      ],
      "metadata": {
        "id": "puZaHYIU_Pif",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "daf8c243-a8e4-4716-f66e-9692c6d1622a"
      },
      "execution_count": 80,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1    165\n",
              "0    138\n",
              "Name: target, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 80
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# check variance inflation factor to see the relationship between variables\n",
        "from statsmodels.stats.outliers_influence import variance_inflation_factor\n",
        "X=heart.drop([\"target\"], axis=1)\n",
        "vif = pd.DataFrame()\n",
        "vif[\"features\"] = X.columns\n",
        "vif[\"vif_Factor\"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]\n",
        "print(vif)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "z6fhjRGKmcui",
        "outputId": "42b25e2b-d639-4757-d44d-805febecaa78"
      },
      "execution_count": 81,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    features  vif_Factor\n",
            "0        age   38.998305\n",
            "1        sex    3.523211\n",
            "2         cp    2.414403\n",
            "3   trestbps   58.557335\n",
            "4       chol   26.267365\n",
            "5        fbs    1.268205\n",
            "6    restecg    2.058206\n",
            "7    thalach   42.742178\n",
            "8      exang    2.022527\n",
            "9    oldpeak    3.062890\n",
            "10     slope   10.072734\n",
            "11        ca    1.808925\n",
            "12      thal   17.165303\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# drop the highest VIF, has to come below 10\n",
        "# removed variables showing multicollinearity \n",
        "# understood from heatmap and VIF\n",
        "X=heart.drop([\"target\", \"trestbps\", \"thalach\", \"age\", \"chol\", \"thal\"], axis=1)\n",
        "vif = pd.DataFrame()\n",
        "vif[\"features\"] = X.columns\n",
        "vif[\"vif_Factor\"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]\n",
        "print(vif)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0jhMbYMvoEIL",
        "outputId": "724d9b0c-3c5e-4b4b-d622-b1587a46b221"
      },
      "execution_count": 82,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "  features  vif_Factor\n",
            "0      sex    3.038525\n",
            "1       cp    2.112149\n",
            "2      fbs    1.222870\n",
            "3  restecg    1.957971\n",
            "4    exang    1.795800\n",
            "5  oldpeak    2.062440\n",
            "6    slope    3.756703\n",
            "7       ca    1.686170\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "corr = x.corr()\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "plt.figure()\n",
        "sns.heatmap(corr)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 299
        },
        "id": "Y86k13oOF5nt",
        "outputId": "3da83514-9595-45e2-d9ba-38483f38420a"
      },
      "execution_count": 140,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q. Are there any outliers in the dataset? What do you do with them?"
      ],
      "metadata": {
        "id": "v9gQBGnZ_QiC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# OPTIONAL\n",
        "# Z-Score\n",
        "# check for values >3 and <-3\n",
        "# What do i do with them?\n",
        "# 1) Remove them \n",
        "# 2) replace all >3 with max, <-3 with min\n",
        "# 3) Ignore\n",
        "\n",
        "# NORMALIZE \n",
        "# Z-Score = (data-mean)/std (-3,3)\n",
        "# MinMax -> (data-min)/(max-min) (0,1)\n",
        "\n",
        "# Detecting Frauds, Anomalies \n",
        "# Using Z-Score\n",
        "import scipy.stats as stats\n",
        "heart['Zscore'] = stats.zscore(heart[\"target\"])\n",
        "print(heart.head())\n",
        "# No Z-Score above or below 3 and -3."
      ],
      "metadata": {
        "id": "qKUVWPJq_fTq",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "faffe452-c7b4-4c62-9c71-e058e4792004"
      },
      "execution_count": 83,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  slope  \\\n",
            "0   63    1   3       145   233    1        0      150      0      2.3      0   \n",
            "1   37    1   2       130   250    0        1      187      0      3.5      0   \n",
            "2   41    0   1       130   204    0        0      172      0      1.4      2   \n",
            "3   56    1   1       120   236    0        1      178      0      0.8      2   \n",
            "4   57    0   0       120   354    0        1      163      1      0.6      2   \n",
            "\n",
            "   ca  thal  target    Zscore  \n",
            "0   0     1       1  0.914529  \n",
            "1   0     2       1  0.914529  \n",
            "2   0     2       1  0.914529  \n",
            "3   0     2       1  0.914529  \n",
            "4   0     2       1  0.914529  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q. Are there any strings in the features that need to be converted to integers? Do you select One-Hot encoding or Label Encoding?"
      ],
      "metadata": {
        "id": "v3SRFiXRAzzu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# if you are not sure, do label ENCODING\n",
        "# unique_values = data['diagnosis'].value_counts()\n",
        "# Form a dictionary of the unique values!\n",
        "# encoding_funk = lambda x : dictionary[x]\n",
        "# data['my_string_column'] = data['my_string_column'].apply(encoding_funk)\n",
        "\n",
        "# This does not need to be used"
      ],
      "metadata": {
        "id": "feWeqNtzOTWv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# One hot encoding-> pandas-> get_dummies \n",
        "\n",
        "# data['diagnosis'] - get_dummies\n",
        "\n",
        "\n",
        "# if there are too many values-> one-hot encoding is NOT an option\n",
        "\n",
        "# GROUP_BY on ZIP_code or country or state!\n",
        "# or del that column altogether!\n",
        "\n",
        "# One Hot encoding\n",
        "\n",
        "# Sales City Profit\n",
        "#  100.  London  20\n",
        "#. 100.  Papua.  60\n",
        "#  123.  London. 21\n",
        "#. 65.   Paris.  13\n",
        "#. 92.   Bandar Seri Begawan 22\n",
        "\n",
        "# 2 kinds of ML problems- \n",
        "# 1) i can use city as a filter and generate multiple models\n",
        "# one for each city\n",
        "\n",
        "# 2) Or make a model that is GENERALIZED for each city and impacted\n",
        "# equally by each city\n",
        "\n",
        "# result of one hot encoding\n",
        "# Sales City_London City_Papua City_Paris City_BSB Profit\n",
        "#  100.  1            0         0          0          20\n",
        "#. 100.  0            1         0           0      .  60\n",
        "#  123.  1.            0         0          0         21\n",
        "#. 65.   0             0         1          0      .  13\n",
        "#. 92.   0            0          0          1         22\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "# final ml equation\n",
        "# profit -> label\n",
        "# features-> [ 'Sales', 'Cit....']\n",
        "# profit=w1*Sales+w2*C_Lon+w3*C_Pap+w4*C_Par+w5*City_BSB + bias\n",
        "\n",
        "# Sales from london\n",
        "# 20=w1*100 + w2*1+ w3*0+ w4*0+ w5*0 + bias\n",
        "# 21=w1*123 + w2*1+ w3*0+ w4*0+ w5*0 + bias"
      ],
      "metadata": {
        "id": "3qLuwfTDAzbf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q. Split the data for TRAINING and SCORING (testing). OPTIONAL: Discuss what problems could happen we have poor distribution b/w training and testing?"
      ],
      "metadata": {
        "id": "TxPO0Ch5Pv3F"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "heart.columns"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mQ2Z9m83xAAI",
        "outputId": "e4fc1069-b68e-45d6-9a0c-add70249be0d"
      },
      "execution_count": 88,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',\n",
              "       'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target', 'Zscore'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {},
          "execution_count": 88
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = heart.loc[:, [\"sex\", \"cp\", \"fbs\", \"restecg\", \"exang\", \"oldpeak\", \"slope\", \"ca\"]]\n",
        "y = heart.loc[:, [\"target\"]]\n",
        "# from this, our objective is to form y = mx + c\n",
        "# where m and x will be calc by ML\n",
        "# y and x we will provide to algo!"
      ],
      "metadata": {
        "id": "o_lilZ4VyfVu"
      },
      "execution_count": 101,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Poor distribution could lead to three things:\n",
        "# 1. Model overfitting = modeling error in statistics that occurs when a function is too closely aligned to a limited set of data points.\n",
        "# Models the dataset too well, where it negatively impacts the performance of the model on new data.\n",
        "# 2. Unrepresentative data sample = training or test datasets are an unrepresentative sample of data from the domain.\n",
        "# To generalize the model well, it is crucial that the training data be an accurate representation of the population\n",
        "# 3. Stochastic algorithm = make use of randomness during learning.\n",
        "# Each time the same algorithm is run on the same data, different random numbers are used, so different models will result."
      ],
      "metadata": {
        "id": "7-FWz6HjAS-0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "s5jKhdFd55WJ"
      },
      "source": [
        "# Part 3: Model Selection"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bosw1yWg55WJ"
      },
      "source": [
        "### Q. Use the cheat sheet below to choose the algorithm/estimator suitable for building a model to address your candidate question(s)\n",
        "\n",
        "* https://scikit-learn.org/stable/tutorial/machine_learning_map/"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# for loop b/w all your models\n",
        "# xtrain,xtest, ytrain,ytest = train_test_split\n",
        "from sklearn.model_selection import train_test_split\n",
        "xtrain,xtest, ytrain,ytest = train_test_split(x, y, test_size=0.2)\n",
        "\n",
        "# model.fit-> xTRAIN , xTEST\n",
        "# predictions = model.predict(xtest)\n",
        "# accuracy_score/rmse/mae/precision for (predictions, ytest)\n",
        "\n",
        "# MAJOR-> string/ranges values-> convert into numbers"
      ],
      "metadata": {
        "id": "39bauCNWR2ve"
      },
      "execution_count": 102,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "ytrain"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 419
        },
        "id": "XQN_qKEP1joh",
        "outputId": "d449e2b6-c2a9-4f6c-d6dd-b32121f639e6"
      },
      "execution_count": 103,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     target\n",
              "25        1\n",
              "122       1\n",
              "35        1\n",
              "1         1\n",
              "45        1\n",
              "..      ...\n",
              "38        1\n",
              "139       1\n",
              "266       0\n",
              "152       1\n",
              "5         1\n",
              "\n",
              "[242 rows x 1 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-45d9a09e-4140-4b2c-a18a-2e91d4b889fe\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>target</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>25</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>122</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>35</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>45</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>38</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>139</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>266</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>152</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>242 rows ?? 1 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-45d9a09e-4140-4b2c-a18a-2e91d4b889fe')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-45d9a09e-4140-4b2c-a18a-2e91d4b889fe button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-45d9a09e-4140-4b2c-a18a-2e91d4b889fe');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 103
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# mean and std\n",
        "xtrain.describe().T"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        },
        "id": "50X-i4bR2sFb",
        "outputId": "77d11ceb-db4b-4d5a-9bae-058858d5a847"
      },
      "execution_count": 105,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "         count      mean       std  min  25%  50%  75%  max\n",
              "sex      242.0  0.677686  0.468331  0.0  0.0  1.0  1.0  1.0\n",
              "cp       242.0  0.962810  1.031989  0.0  0.0  1.0  2.0  3.0\n",
              "fbs      242.0  0.157025  0.364578  0.0  0.0  0.0  0.0  1.0\n",
              "restecg  242.0  0.541322  0.531524  0.0  0.0  1.0  1.0  2.0\n",
              "exang    242.0  0.322314  0.468331  0.0  0.0  0.0  1.0  1.0\n",
              "oldpeak  242.0  0.997521  1.170272  0.0  0.0  0.6  1.6  6.2\n",
              "slope    242.0  1.409091  0.626192  0.0  1.0  1.0  2.0  2.0\n",
              "ca       242.0  0.727273  1.054530  0.0  0.0  0.0  1.0  4.0"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-10dbaf4b-62b2-4981-ae94-b626bf713b64\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>count</th>\n",
              "      <th>mean</th>\n",
              "      <th>std</th>\n",
              "      <th>min</th>\n",
              "      <th>25%</th>\n",
              "      <th>50%</th>\n",
              "      <th>75%</th>\n",
              "      <th>max</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>sex</th>\n",
              "      <td>242.0</td>\n",
              "      <td>0.677686</td>\n",
              "      <td>0.468331</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>cp</th>\n",
              "      <td>242.0</td>\n",
              "      <td>0.962810</td>\n",
              "      <td>1.031989</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2.0</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>fbs</th>\n",
              "      <td>242.0</td>\n",
              "      <td>0.157025</td>\n",
              "      <td>0.364578</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>restecg</th>\n",
              "      <td>242.0</td>\n",
              "      <td>0.541322</td>\n",
              "      <td>0.531524</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>exang</th>\n",
              "      <td>242.0</td>\n",
              "      <td>0.322314</td>\n",
              "      <td>0.468331</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>oldpeak</th>\n",
              "      <td>242.0</td>\n",
              "      <td>0.997521</td>\n",
              "      <td>1.170272</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.6</td>\n",
              "      <td>1.6</td>\n",
              "      <td>6.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>slope</th>\n",
              "      <td>242.0</td>\n",
              "      <td>1.409091</td>\n",
              "      <td>0.626192</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2.0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>ca</th>\n",
              "      <td>242.0</td>\n",
              "      <td>0.727273</td>\n",
              "      <td>1.054530</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>4.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-10dbaf4b-62b2-4981-ae94-b626bf713b64')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-10dbaf4b-62b2-4981-ae94-b626bf713b64 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-10dbaf4b-62b2-4981-ae94-b626bf713b64');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 105
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "stats = xtrain.describe().T\n",
        "xmean = stats['mean'] \n",
        "xstd = stats['std']\n",
        "xmean, xstd"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TDghKQBf3HoY",
        "outputId": "05f5aeeb-fd8a-49ef-b22a-d2b3ac6dc4f9"
      },
      "execution_count": 106,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(sex        0.677686\n",
              " cp         0.962810\n",
              " fbs        0.157025\n",
              " restecg    0.541322\n",
              " exang      0.322314\n",
              " oldpeak    0.997521\n",
              " slope      1.409091\n",
              " ca         0.727273\n",
              " Name: mean, dtype: float64, sex        0.468331\n",
              " cp         1.031989\n",
              " fbs        0.364578\n",
              " restecg    0.531524\n",
              " exang      0.468331\n",
              " oldpeak    1.170272\n",
              " slope      0.626192\n",
              " ca         1.054530\n",
              " Name: std, dtype: float64)"
            ]
          },
          "metadata": {},
          "execution_count": 106
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "norm_xtrain = (xtrain - xmean) /xstd\n",
        "norm_xtest = (xtest - xmean)/ xstd"
      ],
      "metadata": {
        "id": "yQchtxdM3Nvz"
      },
      "execution_count": 107,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "norm_xtest.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        },
        "id": "4ztpqKOT3Q3K",
        "outputId": "f249defd-b818-41d9-e274-d648a779e39a"
      },
      "execution_count": 108,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "          sex        cp       fbs   restecg     exang   oldpeak     slope  \\\n",
              "192  0.688218 -0.932965 -0.430703  0.862948 -0.688218  0.343919 -0.653300   \n",
              "247  0.688218  0.036037 -0.430703  0.862948  1.447023 -0.852383 -0.653300   \n",
              "91   0.688218 -0.932965 -0.430703  0.862948  1.447023 -0.852383  0.943655   \n",
              "175  0.688218 -0.932965 -0.430703 -1.018434  1.447023  0.856621 -0.653300   \n",
              "226  0.688218  0.036037 -0.430703 -1.018434 -0.688218  0.343919 -0.653300   \n",
              "\n",
              "           ca  \n",
              "192  0.258625  \n",
              "247  2.155204  \n",
              "91  -0.689665  \n",
              "175 -0.689665  \n",
              "226  0.258625  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-51a3d1a4-fcd2-41c1-a1c3-df4d34854783\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>sex</th>\n",
              "      <th>cp</th>\n",
              "      <th>fbs</th>\n",
              "      <th>restecg</th>\n",
              "      <th>exang</th>\n",
              "      <th>oldpeak</th>\n",
              "      <th>slope</th>\n",
              "      <th>ca</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>192</th>\n",
              "      <td>0.688218</td>\n",
              "      <td>-0.932965</td>\n",
              "      <td>-0.430703</td>\n",
              "      <td>0.862948</td>\n",
              "      <td>-0.688218</td>\n",
              "      <td>0.343919</td>\n",
              "      <td>-0.653300</td>\n",
              "      <td>0.258625</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>247</th>\n",
              "      <td>0.688218</td>\n",
              "      <td>0.036037</td>\n",
              "      <td>-0.430703</td>\n",
              "      <td>0.862948</td>\n",
              "      <td>1.447023</td>\n",
              "      <td>-0.852383</td>\n",
              "      <td>-0.653300</td>\n",
              "      <td>2.155204</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>91</th>\n",
              "      <td>0.688218</td>\n",
              "      <td>-0.932965</td>\n",
              "      <td>-0.430703</td>\n",
              "      <td>0.862948</td>\n",
              "      <td>1.447023</td>\n",
              "      <td>-0.852383</td>\n",
              "      <td>0.943655</td>\n",
              "      <td>-0.689665</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>175</th>\n",
              "      <td>0.688218</td>\n",
              "      <td>-0.932965</td>\n",
              "      <td>-0.430703</td>\n",
              "      <td>-1.018434</td>\n",
              "      <td>1.447023</td>\n",
              "      <td>0.856621</td>\n",
              "      <td>-0.653300</td>\n",
              "      <td>-0.689665</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>226</th>\n",
              "      <td>0.688218</td>\n",
              "      <td>0.036037</td>\n",
              "      <td>-0.430703</td>\n",
              "      <td>-1.018434</td>\n",
              "      <td>-0.688218</td>\n",
              "      <td>0.343919</td>\n",
              "      <td>-0.653300</td>\n",
              "      <td>0.258625</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-51a3d1a4-fcd2-41c1-a1c3-df4d34854783')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-51a3d1a4-fcd2-41c1-a1c3-df4d34854783 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-51a3d1a4-fcd2-41c1-a1c3-df4d34854783');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 108
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ytrain.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        },
        "id": "KwQJSnl63U2-",
        "outputId": "2626d383-63ab-46f6-8a07-88d761726432"
      },
      "execution_count": 109,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     target\n",
              "25        1\n",
              "122       1\n",
              "35        1\n",
              "1         1\n",
              "45        1"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-14836abd-b991-4427-8baf-1f3e0f2ac0ee\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>target</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>25</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>122</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>35</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>45</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-14836abd-b991-4427-8baf-1f3e0f2ac0ee')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-14836abd-b991-4427-8baf-1f3e0f2ac0ee button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-14836abd-b991-4427-8baf-1f3e0f2ac0ee');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 109
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(ytrain.tail(10))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1oyzysLq3cfj",
        "outputId": "263dc0e9-e96a-4294-a3d5-698b14463379"
      },
      "execution_count": 111,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "     target\n",
            "24        1\n",
            "228       0\n",
            "59        1\n",
            "128       1\n",
            "248       0\n",
            "38        1\n",
            "139       1\n",
            "266       0\n",
            "152       1\n",
            "5         1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Define Algorithm\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "model = RandomForestClassifier()\n",
        "# train\n",
        "model.fit(norm_xtrain, ytrain)\n",
        "\n",
        "# testing/scoring\n",
        "predictions = model.predict(norm_xtest)\n",
        "\n",
        "# evaluation\n",
        "from sklearn.metrics import accuracy_score\n",
        "accuracy_score(predictions, ytest)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HPFDhH-M8e7m",
        "outputId": "0edff20a-ce7a-4452-fad8-f9c1ee762964"
      },
      "execution_count": 118,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:5: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
            "  \"\"\"\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.7540983606557377"
            ]
          },
          "metadata": {},
          "execution_count": 118
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.naive_bayes import GaussianNB\n",
        "model2 = GaussianNB()\n",
        "# train\n",
        "model2.fit(norm_xtrain, ytrain)\n",
        "\n",
        "# testing/scoring\n",
        "predictions = model2.predict(norm_xtest)\n",
        "\n",
        "# evaluation\n",
        "from sklearn.metrics import accuracy_score\n",
        "accuracy_score(predictions, ytest)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zabJ0rYr8j0t",
        "outputId": "0e417ffb-323a-4647-9993-f52b0724ef5b"
      },
      "execution_count": 119,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/sklearn/utils/validation.py:993: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
            "  y = column_or_1d(y, warn=True)\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.8032786885245902"
            ]
          },
          "metadata": {},
          "execution_count": 119
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.tree import DecisionTreeClassifier\n",
        "from sklearn.neighbors import KNeighborsClassifier\n",
        "from sklearn.svm import LinearSVC\n",
        "# HYPERPARAMETERS-> these are 2 diff HPs for Random Forest \n",
        "# SAME algo could also give 2 diff models!\n",
        "ntree1, ntree2 = 50,100\n",
        "for algo in [RandomForestClassifier(n_estimators=ntree1), RandomForestClassifier(n_estimators=ntree2), GaussianNB(), DecisionTreeClassifier(), KNeighborsClassifier(), LinearSVC()]:\n",
        "  model = algo\n",
        "  model.fit(norm_xtrain, ytrain)\n",
        "  predictions = model.predict(norm_xtest)\n",
        "  print(accuracy_score(predictions, ytest))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lvrFWi0f6iDe",
        "outputId": "ec96240b-cef2-44cb-a941-f2e16bf7731e"
      },
      "execution_count": 120,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:9: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
            "  if __name__ == '__main__':\n",
            "/usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:9: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
            "  if __name__ == '__main__':\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0.8032786885245902\n",
            "0.7540983606557377\n",
            "0.8032786885245902\n",
            "0.7049180327868853\n",
            "0.8032786885245902\n",
            "0.8524590163934426\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/sklearn/utils/validation.py:993: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
            "  y = column_or_1d(y, warn=True)\n",
            "/usr/local/lib/python3.7/dist-packages/sklearn/neighbors/_classification.py:198: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
            "  return self._fit(X, y)\n",
            "/usr/local/lib/python3.7/dist-packages/sklearn/utils/validation.py:993: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
            "  y = column_or_1d(y, warn=True)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gB-pblb255WJ"
      },
      "source": [
        "# Part 4: Model Evaluation"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "w231rWpm55WK"
      },
      "source": [
        "### Q. Identify which of the statistical measures below are suitable for the evaluation of your model.\n",
        "\n",
        "Classification Metrics:\n",
        "* Accuracy\n",
        "* Precision\n",
        "* Recall\n",
        "* F1 Score\n",
        "\n",
        "Regression Metrics:\n",
        "    \n",
        "* Mean absolute error (MAE)\n",
        "* Root mean squared error (RMSE)\n",
        "* Relative absolute error (RAE)\n",
        "* Relative squared error (RSE)\n",
        "* Mean Zero One Error (MZOE)\n",
        "* Coefficient of determination\n",
        "\n",
        " "
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Best algorithm, highest accuracy score\n",
        "# Classification, supervised, LinearSVC\n",
        "from sklearn.svm import LinearSVC\n",
        "from sklearn.datasets import load_iris\n",
        "from sklearn.datasets import make_classification\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.model_selection import cross_val_score\n",
        "from sklearn.metrics import confusion_matrix\n",
        "from sklearn.metrics import classification_report"
      ],
      "metadata": {
        "id": "0oQdS75Y80ub"
      },
      "execution_count": 129,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Training the model - default parameters of the class\n",
        "lsvc = LinearSVC(verbose=0)\n",
        "print(lsvc)\n",
        "\n",
        "LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,\n",
        "          intercept_scaling=1, loss='squared_hinge', max_iter=1000,\n",
        "          multi_class='ovr', penalty='l2', random_state=None, tol=0.0001,\n",
        "          verbose=0)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZKl0JT9hCqVo",
        "outputId": "a8a66a5a-0743-43af-d5c0-6c3b657b58f8"
      },
      "execution_count": 130,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "LinearSVC()\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LinearSVC()"
            ]
          },
          "metadata": {},
          "execution_count": 130
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Train and check model accuracy score\n",
        "lsvc.fit(xtrain, ytrain)\n",
        "score = lsvc.score(xtrain, ytrain)\n",
        "print(\"Score: \", score)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-bON7mnfC9dh",
        "outputId": "78c043cb-1055-4dc1-b100-86057e7373fe"
      },
      "execution_count": 131,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Score:  0.8264462809917356\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/sklearn/utils/validation.py:993: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
            "  y = column_or_1d(y, warn=True)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Cross-validation training method to the model and check the training score\n",
        "cv_scores = cross_val_score(lsvc, xtrain, ytrain, cv=10)\n",
        "print(\"CV average score: %.2f\" % cv_scores.mean())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "01_SThuHDHOR",
        "outputId": "a92c7a42-6618-456d-b9bb-5cd6ec597fa8"
      },
      "execution_count": 132,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CV average score: 0.82\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/sklearn/utils/validation.py:993: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
            "  y = column_or_1d(y, warn=True)\n",
            "/usr/local/lib/python3.7/dist-packages/sklearn/utils/validation.py:993: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
            "  y = column_or_1d(y, warn=True)\n",
            "/usr/local/lib/python3.7/dist-packages/sklearn/utils/validation.py:993: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
            "  y = column_or_1d(y, warn=True)\n",
            "/usr/local/lib/python3.7/dist-packages/sklearn/utils/validation.py:993: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
            "  y = column_or_1d(y, warn=True)\n",
            "/usr/local/lib/python3.7/dist-packages/sklearn/utils/validation.py:993: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
            "  y = column_or_1d(y, warn=True)\n",
            "/usr/local/lib/python3.7/dist-packages/sklearn/utils/validation.py:993: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
            "  y = column_or_1d(y, warn=True)\n",
            "/usr/local/lib/python3.7/dist-packages/sklearn/utils/validation.py:993: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
            "  y = column_or_1d(y, warn=True)\n",
            "/usr/local/lib/python3.7/dist-packages/sklearn/utils/validation.py:993: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
            "  y = column_or_1d(y, warn=True)\n",
            "/usr/local/lib/python3.7/dist-packages/sklearn/utils/validation.py:993: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
            "  y = column_or_1d(y, warn=True)\n",
            "/usr/local/lib/python3.7/dist-packages/sklearn/utils/validation.py:993: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
            "  y = column_or_1d(y, warn=True)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Predict and accuracy check\n",
        "ypred = lsvc.predict(xtest)\n",
        "\n",
        "cm = confusion_matrix(ytest, ypred)\n",
        "print(cm)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "arrLqpwyDPpP",
        "outputId": "632bd55b-88e4-4f56-d94b-373b231f28c8"
      },
      "execution_count": 134,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[23  4]\n",
            " [ 5 29]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Create classification report on predicted data\n",
        "cr = classification_report(ytest, ypred)\n",
        "print(cr)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tepcDoSCDfYA",
        "outputId": "433f4b01-8a57-4541-ed8c-8deb60b909bf"
      },
      "execution_count": 135,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.82      0.85      0.84        27\n",
            "           1       0.88      0.85      0.87        34\n",
            "\n",
            "    accuracy                           0.85        61\n",
            "   macro avg       0.85      0.85      0.85        61\n",
            "weighted avg       0.85      0.85      0.85        61\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6SK8nej055WJ"
      },
      "source": [
        ""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "V_GR5s4K55WK"
      },
      "source": [
        "# Part 5: Stretch - Model Deployment"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0g_JJnoh55WL"
      },
      "source": [
        "### Q. Evaluate the open-source app framework for Machine Learning model deployment below in your own time.\n",
        "\n",
        "* https://streamlit.io/"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ghIEovDv55WL"
      },
      "outputs": [],
      "source": [
        "# EXPORT your model and upload to azure\n",
        "# deploy to Azure Container Instance\n",
        "# after 20-30 mins, consume tab will appear in your ENDPOINT\n",
        "# and then paste the PYTHON code below!"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "mS9l7kc09sse"
      },
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.7.4"
    },
    "colab": {
      "name": "FinalProject:Choosing_the_right_estimator.ipynb",
      "provenance": [],
      "include_colab_link": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}