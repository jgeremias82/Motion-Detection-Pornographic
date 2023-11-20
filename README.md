# A Motion-based Approach for Real-time Detection of Pornographic Content in Videos
## Authors: Jhonatan Geremias and Eduardo K. Viegas and Altair O. Santin and Alceu Britto
In recent years, several works have proposed highly accurate CNNbased pornography video detection approaches. However, current techniques are unable to cope with the context-dependent nature of pornography content, wherein the analyzed video frame class may change according to its context, whether it is pornographic related or not. This paper proposes a motion-based approach for fine-grained real-time detection of pornographic content in videos implemented in two phases. First, we extract and classify motionbased descriptors built over adjacent video frames to build a motion image from the analyzed video frame. Second, we jointly evaluate the outcome of each single classified motion descriptor to produce a final video frame classification. Experiments performed in a novel fine-grained dataset built from the manual analysis of over 400 thousand video frames, show that current approaches in the literature are unable to cope with context-dependent pornographic content. In contrast, our proposal can maintain the system accuracy, even in the presence of context-dependent pornographic content, hence, maintaining its reliability. In addition, when the extracted motion-based descriptors are jointly evaluated, our proposal is able to improve the detection accuracy by up to 29%.

## Proposal

<img src="./Proposta/proposta.png" />


## Dataset
<ul>
  <li><a href="https://recodbr.wordpress.com/tag/pornography-2k-dataset/"> Pornography-2k Dataset</a></li>
</ul>

## BibTeX

```bibtex
@inproceedings{geremias2022motion,
  title={A motion-based approach for real-time detection of pornographic content in videos},
  author={Geremias, Jhonatan and Viegas, Eduardo K and Britto Jr, Alceu S and Santin, Altair O},
  booktitle={Proceedings of the 37th ACM/SIGAPP Symposium on Applied Computing},
  pages={1066--1073},
  year={2022}
}
```
