#!/usr/bin/env python
"""HyperView Hugging Face Space template example.

Copy this folder, then edit the constants below for your dataset.
"""

from __future__ import annotations

import hyperview as hv

# Edit this block when you reuse the template for another Space.
SPACE_HOST = "0.0.0.0"
SPACE_PORT = 7860

DATASET_NAME = "imagenette_clip_hycoclip"
HF_DATASET = "Multimodal-Fatima/Imagenette_validation"
HF_SPLIT = "validation"
HF_IMAGE_KEY = "image"
HF_LABEL_KEY = "label"
SAMPLE_COUNT = 300
SAMPLE_SEED = 42

# Keep one or more entries here. Most reuses only need one model/layout pair.
EMBEDDING_LAYOUTS = [
    {
        "name": "CLIP",
        "provider": "embed-anything",
        "model": "openai/clip-vit-base-patch32",
        "layout": "euclidean",
    },
    {
        "name": "HyCoCLIP",
        "provider": "hyper-models",
        "model": "hycoclip-vit-s",
        "layout": "poincare",
    },
]


def build_dataset() -> hv.Dataset:
    dataset = hv.Dataset(DATASET_NAME)

    if len(dataset) == 0:
        print(f"Loading {SAMPLE_COUNT} samples from {HF_DATASET} ({HF_SPLIT})...")
        dataset.add_from_huggingface(
            HF_DATASET,
            split=HF_SPLIT,
            image_key=HF_IMAGE_KEY,
            label_key=HF_LABEL_KEY,
            max_samples=SAMPLE_COUNT,
            shuffle=True,
            seed=SAMPLE_SEED,
        )

    for embedding in EMBEDDING_LAYOUTS:
        print(f"Ensuring {embedding['name']} embeddings ({embedding['model']})...")
        space_key = dataset.compute_embeddings(
            model=embedding["model"],
            provider=embedding["provider"],
            show_progress=True,
        )

        print(f"Ensuring {embedding['layout']} layout...")
        dataset.compute_visualization(space_key=space_key, layout=embedding["layout"])

    return dataset


def main() -> None:
    dataset = build_dataset()
    print(f"Starting HyperView on {SPACE_HOST}:{SPACE_PORT}")
    hv.launch(dataset, host=SPACE_HOST, port=SPACE_PORT, open_browser=False)


if __name__ == "__main__":
    main()
