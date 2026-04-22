---
title: HyperView Basil
emoji: 🌱
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
pinned: false
---

# HyperView — Basil (Various Models)

This example runs HyperView with:

- CLIP embeddings (`openai/clip-vit-base-patch32`) for Euclidean layout
- SAM3 embeddings (`facebook/sam3`) for Euclidean layout
- ResNet-50 embeddings (`microsoft/resnet-50`) for Euclidean layout
- DINOv3 embeddings (`facebook/dinov3-vitl16-pretrain-lvd1689m`) for Euclidean layout
- C-RADIO embeddings (`nvidia/C-RADIO`) for Euclidean layout
- HyCoCLIP embeddings (`hycoclip-vit-s`) for Poincaré layout

The Docker image installs released HyperView packages from PyPI. The dataset,
embeddings, and layouts are computed at first startup.

## Reuse This Template

When you copy this folder for your own dataset, change these parts first:

1. Edit the constants block in [demo.py](demo.py).
2. Rename the copied Space from `HyperView` to your own project name such as `yourproject-HyperView` or `HyperView-yourproject`.
3. Update this README frontmatter, title, and H1.
4. Point a deploy workflow at your new folder.

This starter currently installs `hyperview==0.3.1` and `hyper-models==0.1.0`.

The defaults in [demo.py](demo.py) are:

- Hugging Face dataset: `Multimodal-Fatima/Imagenette_validation`
- Split: `validation`
- Image field: `image`
- Label field: `label`
- Sample count: `300`
- Layouts: CLIP + Euclidean, HyCoCLIP + Poincaré

If you only want one model in your own Space, keep a single entry in
`EMBEDDING_LAYOUTS` and delete the rest.

When contributing your own Space back to this repository, add a row to the
community table in the root `README.md` and include your Hugging Face Space ID
in the pull request description.

## Build Model

The Dockerfile runs `build_dataset()` during image build. That means:

- the first expensive download/embedding pass happens at build time
- the runtime container mostly just launches HyperView
- there is no extra runtime configuration path to keep in sync

## Deploy source

This folder is synchronized to Hugging Face Spaces by GitHub Actions from the
`hyperview-spaces` deployment repository.
