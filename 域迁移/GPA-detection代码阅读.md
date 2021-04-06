# GPA代码阅读
## train_baseline.py
### main
- 首先为每种数据集设置Anchor的相关参数
- 打印训练参数
- 调用combined_roidb()方法（from [lib/roi_data_layer/roidb](#lib/roi_data_layer/roidb)），输入为第一步赋值的数据集名称
- 初始化faster RCNN的backbone
- 开始epoch循环训练（from args.start_epoch to args.max_epochs+1）
  - 设置fasterRCNN.train()
  - 根据lr_decay_step调整学习率
  - 开始step循环训练
    - 设置warm_up学习率
    - 输入im_data, im_info, gt_boxes, num_boxs开始网络的forward过程，此处网络源码提供了vgg16和resnet，下面以vgg16为例

### lib/model/faster_rcnn/vgg16
- vgg16以同文件夹下的faster_rcnn为父类，所以先读[faster_rcnn](#lib/model/fater_rcnn/faster_rcnn)



### lib/roi_data_layer/roidb
- combined_roidb()
  - roidb:Region of Interest database
  - 加载图片和box
  - 调用rank_roidb_ratio，对box进行裁剪，使得宽高比(width/height)保持在ratio_large(2.0)和ratio_small(0.5)之间，返回的是剪裁后ratio的列表和对应的index

