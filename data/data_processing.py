{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOT3DS9z2KN2csA7ByAYkrZ",
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
        "<a href=\"https://colab.research.google.com/github/lillymitch/organized_archives/blob/main/data_processing.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "zJJDcoqCAMyY"
      },
      "outputs": [],
      "source": [
        "import shutil\n",
        "import os\n",
        "from datasets import load_dataset, Image as HFImage\n",
        "from PIL import Image\n",
        "from io import BytesIO\n",
        "\n",
        "wikiart_dataset = load_dataset(\n",
        "    \"huggan/wikiart\",\n",
        "    split=\"train\",\n",
        "    streaming=True\n",
        ")\n",
        "\n",
        "wikiart_dataset = wikiart_dataset.cast_column(\"image\", HFImage(decode=False))\n",
        "style_names = wikiart_dataset.features[\"style\"].names\n",
        "\n",
        "#defines path for small dataset to be created locally\n",
        "small_dataset_path = \"/content/wikiart_small\"\n",
        "\n",
        "#removes old dataset folder if it already exists, and creates new one\n",
        "if os.path.exists(small_dataset_path):\n",
        "    shutil.rmtree(small_dataset_path)\n",
        "os.makedirs(small_dataset_path, exist_ok=True)\n",
        "\n",
        "#classes to include\n",
        "selected_classes = [\n",
        "    \"Impressionism\",\n",
        "    \"Cubism\",\n",
        "    \"Baroque\",\n",
        "    \"Realism\",\n",
        "    \"Expressionism\",\n",
        "]\n",
        "\n",
        "#change later\n",
        "max_per_class = 100\n",
        "\n",
        "max_examples_to_check = 3000\n",
        "examples_checked = 0\n",
        "class_counts = {class_name: 0 for class_name in selected_classes}\n",
        "\n",
        "#condense the dataset\n",
        "for example in wikiart_dataset:\n",
        "\n",
        "    examples_checked += 1\n",
        "    if examples_checked >= max_examples_to_check:\n",
        "        print(\"stopped early\")\n",
        "        break\n",
        "\n",
        "    style_index = example[\"style\"]\n",
        "    style_name = style_names[style_index]\n",
        "\n",
        "    #ONLY process if the style is in selected_classes and we haven't reached max_per_class for this style\n",
        "    if style_name in selected_classes and class_counts[style_name] < max_per_class:\n",
        "\n",
        "        class_folder = os.path.join(small_dataset_path, style_name)\n",
        "        os.makedirs(class_folder, exist_ok=True)\n",
        "        image_data = example[\"image\"]\n",
        "\n",
        "        #chatgpt try and except\n",
        "        try:\n",
        "            if image_data.get(\"bytes\") is not None:\n",
        "                image = Image.open(BytesIO(image_data[\"bytes\"])).convert(\"RGB\")\n",
        "            else:\n",
        "                image = Image.open(image_data[\"path\"]).convert(\"RGB\")\n",
        "            save_path = os.path.join(\n",
        "                class_folder,\n",
        "                f\"{class_counts[style_name]}.jpg\"\n",
        "            )\n",
        "\n",
        "            image.save(save_path)\n",
        "            class_counts[style_name] += 1\n",
        "            print(class_counts)\n",
        "\n",
        "        except:\n",
        "            pass\n",
        "\n",
        "    if all(class_counts[class_name] >= max_per_class for class_name in selected_classes):\n",
        "        break"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from torchvision.datasets import ImageFolder\n",
        "from torch.utils.data import DataLoader, random_split\n",
        "\n",
        "#ImageFolder dataset created from the condensed dataset\n",
        "dataset = ImageFolder(\n",
        "    root=small_dataset_path,\n",
        "    transform=train_processor\n",
        ")"
      ],
      "metadata": {
        "id": "RbXMCO0eAZ1L"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}