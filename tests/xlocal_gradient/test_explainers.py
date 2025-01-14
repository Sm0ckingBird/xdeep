import torchvision.models as models
from xdeep.xlocal.gradient.explainers import *

image = load_image('tests/xlocal_gradient/images/ILSVRC2012_val_00000073.JPEG')
model = models.vgg16(pretrained=True)
model_explainer = ImageInterpreter(model)

def test_backprop():
  model_explainer.explain(image, method_name='vanilla_backprop', viz=True, save_path='tests/xlocal_gradient/results/bp.jpg')
  model_explainer.explain(image, method_name='guided_backprop', viz=True, save_path='tests/xlocal_gradient/results/guided.jpg')

def test_grad():
  model_explainer.explain(image, method_name='smooth_grad', viz=True, save_path='tests/xlocal_gradient/results/smooth_grad.jpg')
  model_explainer.explain(image, method_name='integrate_grad', viz=True, save_path='tests/xlocal_gradient/results/integrate.jpg')
  model_explainer.explain(image, method_name='smooth_guided_grad', viz=True, save_path='tests/xlocal_gradient/results/smooth_guided_grad.jpg')
  model_explainer.explain(image, method_name='integrate_guided_grad', viz=True, save_path='tests/xlocal_gradient/results/integrate_guided.jpg')

def test_cam():
  model_explainer.explain(image, method_name='gradcam', target_layer_name='features_29', viz=True, save_path='tests/xlocal_gradient/results/gradcam.jpg')
  model_explainer.explain(image, method_name='gradcampp', target_layer_name='features_29', viz=True, save_path='tests/xlocal_gradient/results/gradcampp.jpg')
  model_explainer.explain(image, method_name='scorecam', target_layer_name='features_29', viz=True, save_path='tests/xlocal_gradient/results/scorecam.jpg')
