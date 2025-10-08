# License plates

## How will we detect license plates

To detect license plates we will use YOLOv8
| Model | Params | Compute (GFLOPs) | Typical speed tier\* | Use when… |
| --------------------- | -----: | ---------------: | --------------------------- | --------------------------------------------------------------------------------- |
| **YOLOv8n (Nano)** | ~3.2M | ~9 | **Very fast** (edge/mobile) | You need max FPS on weak hardware; prototyping, webcams, Jetson Nano/CPU-only PoC |
| **YOLOv8s (Small)** | ~11M | ~29 | **Fast** (most GPUs/CPUs) | Best **speed/accuracy** trade-off; strong baseline for ANPR |
| **YOLOv8m (Medium)** | ~26M | ~79 | **Moderate** | You have a mid/high GPU and want better recall on small plates without going huge |
| **YOLOv8l (Large)** | ~44M | ~165 | **Slower** | Offline/near-real-time with good GPU; squeezing extra AP on tough scenes |
| **YOLOv8x (X-Large)** | ~68M | ~258 | **Slowest** | Max accuracy, batch inference, research benchmarks, not edge-friendly |

According to this table, the most suitable for us is YOLOv8s, as we need speed but also to still be accurate enough. The speed isn't our main criteria at all, but we don't have a lot of resources.
