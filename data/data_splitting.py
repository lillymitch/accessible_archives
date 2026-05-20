{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPHHAsfSkcMU9lKzgC05FiQ",
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
        "<a href=\"https://colab.research.google.com/github/lillymitch/organized_archives/blob/main/data_splitting.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "J3BvMBLqBBbj"
      },
      "outputs": [],
      "source": [
        "from torch.utils.data import DataLoader, random_split\n",
        "\n",
        "#split ratios for training, validation, and testing\n",
        "train_size = int(0.7 * len(dataset))\n",
        "val_size = int(0.15 * len(dataset))\n",
        "test_size = len(dataset) - train_size - val_size\n",
        "\n",
        "#split data\n",
        "train_dataset, val_dataset, test_dataset = random_split(\n",
        "    dataset,\n",
        "    [train_size, val_size, test_size]\n",
        ")\n",
        "\n",
        "train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)\n",
        "val_loader = DataLoader(val_dataset, batch_size=32)\n",
        "test_loader = DataLoader(test_dataset, batch_size=32)\n",
        "\n",
        "num_classes = len(dataset.classes)"
      ]
    }
  ]
}