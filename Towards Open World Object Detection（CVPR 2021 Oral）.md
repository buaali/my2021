# Towards Open World Object Detection（CVPR 2021 Oral）
* 提出Open World Object Detection
* [code url](https://github.com/JosephKJ/OWOD)
* 提出解决开放世界目标检测的方法ORE
* 提出该问题的衡量标准用于对比
* 副产物：提出的方法在**增量学习**的领域取得了**最好**的效果
* 提出的问题的相关领域及研究现状
  
  <img src="./1.png" width="100%">
* open world分类问题与检测问题有着本质上的不同，在目标检测中，未知的类在训练时会被识别成背景。
### 开放世界的详细定义
- 训练集的数据（带有图片和标签）被定义为${1, 2, \dots, C}$共$C$个类
- 在推断过程中可能遇到新的$n$个类，标记为unknown
- 在给出新类的训练数据后，不需要重新训练整个数据集就可以将模型扩充为可识别$C + n$个类的模型。

### Pipeline
![](./Towards%20Open%20World%20Object%20Detection（CVPR%202021%20Oral）/pipeline.png)

- 注意：从开始训练，模型的类别数就是$C+1$，第0类是unknown
- 对比聚类，将相同类别的实例拉近，不同类别实例推远（通过原型的方法）
- 对位置类进行伪标签：按照评分排序，将前k个背景框作为未知类
- 基于能量模型的分类器，训练一个特征F与标签L（是否包含unknown，**文中没有说明**）之间相容性的函数$E(\cdot)$
- 已知类能量分布和未知类能量分布差别很大，如图（**为什么？**）
![](Towards%20Open%20World%20Object%20Detection（CVPR%202021%20Oral）/energy.png)