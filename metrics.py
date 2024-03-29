from functools import partial

from keras import backend as K

def dice_coefficient(y_true,y_pred, smooth = 1.):
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_pred_f * y_true_f)

    return (2.*intersection + smooth)/(K.sum(y_pred_f)+K.sum(y_true_f)+smooth)

def dice_coefficient_loss(y_true, y_pred):

    return 1-dice_coefficient(y_true, y_pred)

def label_wise_dice_coefficient(y_true, y_pred, label_index):
    return dice_coefficient(y_true[:, label_index], y_pred[:, label_index])

def get_label_dice_coefficient_function(label_index):
    f = partial(label_wise_dice_coefficient, label_index=label_index)
    f.__setattr__('__name__', 'label_{0}_dice_coef'.format(label_index))
    return f

dice_coef = dice_coefficient
dice_coef_loss = dice_coefficient_loss