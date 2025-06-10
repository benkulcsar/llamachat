# 🦙llamachat  
[![python](https://img.shields.io/badge/python-3.13-blue?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Learning & experimenting with local open-weight LLMs**

Simulated chat between two users roleplayed by [Gemma 3 4B Q4_0](https://ollama.com/library/gemma3:4b) using Ollama. Different scenarios can be configured in a YAML file. 

The model performs surprisingly well on an older Intel i5 CPU without a GPU.

![This GIF is missing. But it's a good opportunity to remind everyone it's pronounced GIF, not JIF.](./assets/llamachat.gif)

## Requirements

- Docker & Docker Compose
- Tested on Ubuntu 20.04 and 22.04

## Workflow

```shell
make build
make up
make run
make down
```

## Development

Run lint (runs black and mypy too) and tests:

```shell
make lint
make test
```

## Scenarios

### Puppies and Emojis

```shell
$ make run scenario=emopuppy
```

<details>
<summary>Example Result</summary>


```shell
Bingo: 👋💖
Bluey: 🐾🥰
Bingo: 🐾😆💖! 🦴🤸‍♀️
Bluey: 😆💖🤸‍♀️🐾🥰! 🦴🥳💖🐾!
Bingo: 🐾🥰🤸‍♀️🥳💖! 🦴😆🤸‍♀️💖! 🐾😆🥰🤸‍♀️🥳! 🦴💖🐾🥰!
Bluey: 😆💖🐾🤸‍♀️🥳! 🦴🥰🤸‍♀️💖! 🐾😆🤸‍♀️🥳! 🦴💖🐾🥰! 🥳💖🐾🤸‍♀️! 🦴😆🤸‍♀️💖!
Bingo: 🐾😆💖! 🤸‍♀️🥳🦴! 🐾🥰🤸‍♀️💖! 🦴😆🤸‍♀️🥳! 🐾🥰🤸‍♀️🥳! 🥳💖🐾🤸‍♀️! 🦴😆🤸‍♀️💖! 😊🐾💖!
Bluey: 🤸‍♀️🥳🐾😆💖! 🦴🥰🤸‍♀️🥳! 🐾😆🤸‍♀️🥳! 🦴💖🐾🥰! 😊🤸‍♀️💖🐾! 🥳😆🤸‍♀️💖! 🦴🤸‍♀️🥳🥰!
Bingo: 😆💖🤸‍♀️🐾🥰! 🥳🤸‍♀️🐾😆💖! 🦴💖🤸‍♀️🥳! 🐾😆🤸‍♀️🥳! 🦴🤸‍♀️🥰💖! 😊🤸‍♀️🐾💖!
Bluey: 🤸‍♀️🥳💖🦴! 🐾😆🥰🤸‍♀️🥳! 😊🤸‍♀️💖🐾! 🥳💖🐾🤸‍♀️! 🦴😆🤸‍♀️💖! 🤸‍♀️🥳🥰! 😊🐾💖! 🤸‍♀️🥳🦴! 🐾😆🤸‍♀️🥳! 🥳💖🐾🤸‍♀️! 🤸‍♀️🥳💖! 😊🤸‍♀️🥳! 🤸‍♀️🥳💖!
Bingo: 😆💖🐾🤸‍♀️🥳! 🦴🥰🤸‍♀️💖! 🐾😆🤸‍♀️🥳! 🥳💖🐾🤸‍♀️! 🤸‍♀️😆💖! 😊🐾💖! 🤸‍♀️🥳🦴! 🐾🥰🤸‍♀️🥳! 🥳💖🐾🤸‍♀️! 🤸‍♀️🥳💖! 😊🤸‍♀️🥳! 🤸‍♀️🥳💖!
```

</details>

### Rick and Lisa Discussing Science

```shell
$ make run scenario=science
```

<details>
<summary>Example Result</summary>


```shell
Rick: Hey Lisa, what's up? 🤪

Lisa: Hello. I’ve been reviewing the latest advancements in transformer models. Specifically, the scaling laws are proving remarkably consistent, suggesting a predictable trajectory for performance improvements. It’s fascinating, though I remain cautious about over-interpretation. What have you been investigating?

Rick: 🤯 Scaling laws are wild! I'm chasing diffusion models. 🎨 It's like magic! ✨ What's your take? 🤔

Lisa: Interesting. The sheer scale of these transformer models is… concerning, frankly. The computational cost alone is staggering. I'm focusing on the limitations of attention mechanisms – the quadratic scaling with sequence length. It presents significant bottlenecks. Diffusion models, I acknowledge, offer an alternative approach. Do you believe they truly circumvent the fundamental computational constraints, or are they simply shifting the problem?

Rick: Massive! 🤯 Scaling is scary. But diffusion? Genius! 🎨 Clever workaround. 👍 Keep exploring! 🚀

Lisa: Indeed. The probabilistic nature of diffusion offers a potential path. However, I’m skeptical of their long-term robustness. The reliance on stochastic processes introduces inherent variability. Are you seeing evidence of this in your experiments? Specifically, I’m examining the effect of noise schedules on sample quality versus training efficiency. It’s proving a complex interplay.
(...)
```

</details>
