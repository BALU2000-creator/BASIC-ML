{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPjsveqyS/84h8bgcjgONQ6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/BALU2000-creator/BASIC-ML/blob/main/basic_python_problems.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1oCONJN4-7kk"
      },
      "source": [
        "Python program to determine whether the given number is even or odd.\n",
        " \n",
        "Input format: Enter an integer:\n",
        " \n",
        "Output format: EVEN or ODD"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4qyZ3xH4FVE1",
        "outputId": "b79b7318-4238-49e7-952f-ac76e629d4ec"
      },
      "source": [
        "n=int(input(\"Enter an integer:\",))\n",
        "if n%2==0:\n",
        "    print(\"EVEN\")\n",
        "else:\n",
        "    print(\"ODD\")"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter an integer:7\n",
            "ODD\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Zt75R7GuAZp8"
      },
      "source": [
        " Python program to determine sum of digits of a given number.\n",
        " \n",
        "Input format : Enter a number:\n",
        " \n",
        "Output : sum of the digits of the given number:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j6KdsXUzBJ4z",
        "outputId": "9cb6ffa0-d16b-4042-9cc1-843bedebb57f"
      },
      "source": [
        "a=int(input(\"Enter a number:\",))\n",
        "sum=0\n",
        "while a!=0:\n",
        "    sum+=a%10\n",
        "    a=a//10\n",
        "print(\"sum of the digits of the number:\",sum)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter a number:123\n",
            "sum of the digits of the number: 6\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VkMadGlxBu2Y"
      },
      "source": [
        "Write a python program to determine first n natural numbers.\n",
        " \n",
        "Input format : Enter a number n=\n",
        " \n",
        "Output format: sum of first n natural numbers is:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0JUrlmByCMKS"
      },
      "source": [
        "n=int(input(\"Enter a number n=\",))\n",
        "sum=0\n",
        "for i in range(1,n+1):\n",
        "    sum+=i\n",
        "print(\"sum of first n natural numbers is:\",sum)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}