# GPA代码阅读
## train_baseline.py
### main
- 首先为每种数据集设置Anchor的相关参数
- 打印训练参数
- 调用combined_roidb()方法（from [lib/roi_data_layer/roidb](#lib/roi_data_layer/roidb)），输入为第一步赋值的数据集名称
- 初始化faster RCNN的backbone

### lib/roi_data_layer/roidb
- combined_roidb()
  - roidb:Region of Interest database
  - 加载图片和box
  - 调用rank_roidb_ratio，对box进行裁剪，使得宽高比(width/height)保持在ratio_large(2.0)和ratio_small(0.5)之间，返回的是剪裁后ratio的列表和对应的index