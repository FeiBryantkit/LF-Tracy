<div align="center">
<p align="center">LF Tracy: A Unified Single-Pipeline Approach for Salient Object Detection in Light Field Cameras

<br>

<div align="center">
  <a href="https://www.researchgate.net/profile/Fei-Teng-42" target="_blank">Fei&nbsp;Teng</a> 
  <b>&middot;</b>
  <a href="https://www.researchgate.net/profile/Jiaming-Zhang-10" target="_blank">Jiaming&nbsp;Zhang</a> 
  <b>&middot;</b>
  Liu&nbsp;Jiawei</a> 
  <b>&middot;</b>
  <a href="https://www.researchgate.net/profile/Kunyu-Peng" target="_blank">Kunyu&nbsp;Peng</a> 
  <b>&middot;</b>
  <a href="https://www.researchgate.net/profile/Zhiyong-Li-3" target="_blank">Zhiyong&nbsp;Li</a> 
  <b>&middot;</b>
  <a href="https://www.researchgate.net/profile/Kailun-Yang" target="_blank">Kailun&nbsp;Yang</a> 

 <br>

  <a href="https://browse.arxiv.org/abs/2401.16712" target="_blank">Paper</a>

# 

</div>

<p align="center">:hammer_and_wrench: :construction_worker: :rocket:</p>
<p align="center">:fire: We will release code and checkpoints in the future. :fire:</p>

</div>

### Update
- 2024.02.26 Code Version1 is released.
- 2024.02.01 Init repository.
- 2024.1.31 Release the [arXiv](https://arxiv.org/abs/2401.16712) version.



### TODO List

- [ ] Result and Pretrain weights.
- [ ] Newest Version is working on. 

### Abstract

Leveraging the rich information extracted from light field (LF) cameras is instrumental for dense prediction tasks. However, adapting light field data to enhance Salient Object Detection (SOD) still follows the traditional RGB methods and remains under-explored in the community. Previous approaches predominantly employ a custom two-stream design to discover the implicit angular feature within light field cameras, leading to significant information isolation between different LF representations. In this study, we propose an efficient paradigm (LF Tracy) to address this limitation. We eschew the conventional specialized fusion and decoder architecture for a dual-stream backbone in favor of a unified, single-pipeline approach. This comprises firstly a simple yet effective data augmentation strategy called MixLD to bridge the connection of spatial, depth, and implicit angular information under different LF representations. A highly efficient information aggregation (IA) module is then introduced to boost asymmetric feature-wise information fusion. Owing to this innovative approach, our model surpasses the existing state-of-the-art methods, particularly demonstrating a 23% improvement over previous results on the latest large-scale PKU dataset. By utilizing only 28.9M parameters, the model achieves a 10% increase in accuracy with 3M additional parameters compared to its backbone using RGB images and an 86% rise to its backbone using LF images.

### Method

<p align="center">
    (Overview)
</p>
<p align="center">
    <div align=center><img src="assert/Pipeline.png" width="850" height="330" /></div>
