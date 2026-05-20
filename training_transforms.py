{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPAssCkBB6ujwboVYsT4sqJ",
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
        "<a href=\"https://colab.research.google.com/github/lillymitch/organized_archives/blob/main/training_transforms.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ASmF4F56Baw_"
      },
      "outputs": [],
      "source": [
        "from torchvision import transforms\n",
        "\n",
        "train_processor = transforms.Compose([\n",
        "    transforms.Resize((256, 256)),\n",
        "    transforms.RandomResizedCrop(224, scale=(0.7, 1.0)),\n",
        "    transforms.RandomHorizontalFlip(),\n",
        "    transforms.ToTensor(),\n",
        "    transforms.Normalize(\n",
        "        mean=[0.485, 0.456, 0.406],\n",
        "        std=[0.229, 0.224, 0.225]\n",
        "    )\n",
        "])\n",
        "\n",
        "test_processor = transforms.Compose([\n",
        "    transforms.Resize((256, 256)),\n",
        "    transforms.CenterCrop(224),\n",
        "    transforms.ToTensor(),\n",
        "    transforms.Normalize(\n",
        "        mean=[0.485, 0.456, 0.406],\n",
        "        std=[0.229, 0.224, 0.225]\n",
        "    )\n",
        "])"
      ]
    }
  ]
}