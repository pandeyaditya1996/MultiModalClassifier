import matplotlib.pyplot as plt
import numpy as np

##############################################
# CNNModel1
##############################################
cnn_train_losses = [0.6727, 0.6537, 0.6426, 0.6204, 0.6401, 0.6020, 0.6209, 0.6011, 0.6087, 0.5947, 0.5733, 0.5738, 0.5686, 0.5738, 0.5721, 0.5622, 0.5470, 0.5451, 0.5398, 0.5269, 0.5386, 0.5228, 0.5186, 0.5135, 0.5165, 0.5251, 0.5145, 0.5116, 0.5022, 0.5361, 0.4863, 0.4726, 0.4735, 0.4624, 0.4762, 0.4643, 0.4735, 0.4552, 0.4818, 0.4613]
cnn_val_losses = [0.6551, 0.6453, 0.6045, 0.5830, 0.5909, 0.5819, 0.5796, 0.5995, 0.5677, 0.5743, 0.5525, 0.5978, 0.5698, 0.5379, 0.5524, 0.5424, 0.5244, 0.5222, 0.5192, 0.5136, 0.5081, 0.5666, 0.4986, 0.5179, 0.4967, 0.5985, 0.4934, 0.4830, 0.5045, 0.4958, 0.4862, 0.4793, 0.4793, 0.4978, 0.4792, 0.4808, 0.4802, 0.4826, 0.4753, 0.4781]
cnn_train_accuracies = [0.5560, 0.6105, 0.6205, 0.6610, 0.6310, 0.6745, 0.6465, 0.6720, 0.6695, 0.6860, 0.6875, 0.7005, 0.6940, 0.7020, 0.7115, 0.7060, 0.7330, 0.7315, 0.7330, 0.7285, 0.7200, 0.7305, 0.7460, 0.7505, 0.7360, 0.7315, 0.7465, 0.7510, 0.7575, 0.7260, 0.7530, 0.7645, 0.7745, 0.7850, 0.7740, 0.7780, 0.7760, 0.7815, 0.7590, 0.7800]
cnn_val_accuracies = [0.6250, 0.6200, 0.6940, 0.6810, 0.6920, 0.7020, 0.7060, 0.6950, 0.7110, 0.6960, 0.7240, 0.6730, 0.7100, 0.7240, 0.7080, 0.7160, 0.7380, 0.7310, 0.7470, 0.7510, 0.7510, 0.7230, 0.7580, 0.7570, 0.7630, 0.6730, 0.7530, 0.7500, 0.7540, 0.7530, 0.7500, 0.7600, 0.7580, 0.7570, 0.7650, 0.7630, 0.7580, 0.7630, 0.7620, 0.7630]
cnn_test_loss = 0.479171
cnn_test_accuracy = 76
cnn_test_accuracy_flowers = 72

##############################################
# LeNet
##############################################
lenet_train_losses = [0.6907, 0.6781, 0.6678, 0.6544, 0.6469, 0.6584, 0.6412, 0.6366, 0.6287, 0.6368, 0.6328, 0.6272, 0.6135, 0.6159, 0.6152, 0.6047, 0.6017, 0.6230, 0.5944, 0.6061, 0.6073, 0.5880, 0.5903, 0.5974, 0.5798, 0.5917, 0.5870, 0.5896, 0.5947, 0.5765, 0.5550, 0.5670, 0.5663, 0.5482, 0.5643, 0.5693, 0.5528, 0.5513, 0.5584, 0.5529]
lenet_val_losses = [0.6765, 0.6534, 0.6503, 0.6331, 0.6118, 0.6155, 0.6110, 0.6161, 0.6738, 0.5989, 0.6113, 0.6034, 0.5768, 0.5710, 0.5905, 0.5890, 0.5865, 0.5884, 0.5835, 0.5576, 0.5616, 0.5629, 0.5616, 0.5692, 0.5512, 0.6034, 0.5503, 0.5868, 0.5950, 0.5725, 0.5450, 0.5450, 0.5444, 0.5404, 0.5406, 0.5364, 0.5331, 0.5429, 0.5311, 0.5332]
lenet_train_accuracies = [0.5405, 0.5775, 0.5925, 0.6160, 0.6345, 0.6105, 0.6435, 0.6480, 0.6530, 0.6395, 0.6540, 0.6520, 0.6655, 0.6600, 0.6650, 0.6825, 0.6685, 0.6525, 0.6895, 0.6645, 0.6760, 0.6885, 0.6855, 0.6745, 0.6975, 0.6845, 0.6895, 0.6855, 0.6750, 0.7105, 0.7225, 0.7015, 0.7060, 0.7245, 0.7090, 0.6950, 0.7195, 0.7350, 0.7190, 0.7220]
lenet_val_accuracies = [0.5910, 0.6230, 0.6230, 0.6480, 0.6750, 0.6620, 0.6890, 0.6740, 0.6160, 0.6680, 0.6630, 0.6830, 0.7030, 0.7080, 0.6910, 0.6910, 0.6940, 0.7130, 0.7020, 0.7190, 0.7300, 0.7220, 0.7190, 0.7050, 0.7270, 0.6710, 0.7260, 0.6790, 0.6910, 0.7110, 0.7450, 0.7350, 0.7300, 0.7390, 0.7390, 0.7370, 0.7480, 0.7340, 0.7430, 0.7430]
lenet_test_loss = 0.533058
lenet_test_accuracy = 74
lenet_test_accuracy_flowers = 71

##############################################
# MLPModel1
##############################################
mlp_train_losses = [0.7342, 0.6860, 0.6923, 0.6818, 0.6763, 0.6708, 0.6737, 0.6747, 0.6606, 0.6617, 0.6694, 0.6635, 0.6639, 0.6623, 0.6564, 0.6618, 0.6588, 0.6656, 0.6561, 0.6580, 0.6556, 0.6565, 0.6509, 0.6549, 0.6453, 0.6437, 0.6513, 0.6501, 0.6560, 0.6481, 0.6417, 0.6360, 0.6307, 0.6313, 0.6367, 0.6292, 0.6391, 0.6320, 0.6299, 0.6293]
mlp_val_losses = [0.6957, 0.6881, 0.6729, 0.6610, 0.6710, 0.6580, 0.6577, 0.6595, 0.6601, 0.6600, 0.6590, 0.6591, 0.6507, 0.6581, 0.6555, 0.6533, 0.6515, 0.6593, 0.6445, 0.6461, 0.6531, 0.6480, 0.6431, 0.6435, 0.6521, 0.6502, 0.6473, 0.6487, 0.6522, 0.6559, 0.6527, 0.6511, 0.6360, 0.6343, 0.6322, 0.6287, 0.6295, 0.6323, 0.6311, 0.6313]
mlp_train_accuracies = [0.5395, 0.5555, 0.5570, 0.5820, 0.5725, 0.5830, 0.5735, 0.5820, 0.6100, 0.5945, 0.5875, 0.5900, 0.5865, 0.5985, 0.6025, 0.5985, 0.5955, 0.5935, 0.6055, 0.6280, 0.6045, 0.6210, 0.5870, 0.6035, 0.6205, 0.6235, 0.6160, 0.5935, 0.6200, 0.6200, 0.6345, 0.6305, 0.6295, 0.6270, 0.6265, 0.6355, 0.6300, 0.6235, 0.6315, 0.6335]
mlp_val_accuracies = [0.5340, 0.5650, 0.5890, 0.5960, 0.5590, 0.5900, 0.6100, 0.6300, 0.6000, 0.6030, 0.5940, 0.6050, 0.6120, 0.5980, 0.6130, 0.6060, 0.6120, 0.6010, 0.6140, 0.6280, 0.6130, 0.6210, 0.6300, 0.6170, 0.6200, 0.6110, 0.6140, 0.6180, 0.6300, 0.6040, 0.6220, 0.6290, 0.6280, 0.6380, 0.6450, 0.6360, 0.6380, 0.6530, 0.6440, 0.6440]
mlp_test_loss = 0.632267
mlp_test_accuracy = 65
mlp_test_accuracy_flowers = 63

##############################################
# AlexNet
##############################################
alexnet_train_losses = [0.7002, 0.6938, 0.6922, 0.6846, 0.6703, 0.6659, 0.6678, 0.6656, 0.6686, 0.6483, 0.6369, 0.6264, 0.6270, 0.6155, 0.6190, 0.6053, 0.6158, 0.6028, 0.6030, 0.5914, 0.5965, 0.6008, 0.5922, 0.5738, 0.5767, 0.5788, 0.5741, 0.5820, 0.5723, 0.5783, 0.5484, 0.5329, 0.5201, 0.5174, 0.5137, 0.5029, 0.5203, 0.5284, 0.5241, 0.5095]
alexnet_val_losses = [0.6913, 0.6922, 0.6897, 0.6695, 0.6617, 0.7273, 0.6218, 0.6678, 0.6330, 0.7118, 0.6344, 0.5801, 0.6148, 0.6062, 0.6770, 0.6440, 0.5755, 0.5869, 0.5762, 0.5706, 0.6210, 0.6216, 0.5625, 0.5628, 0.5747, 0.5852, 0.5878, 0.5441, 0.5765, 0.5648, 0.5517, 0.5479, 0.5671, 0.5636, 0.5430, 0.5410, 0.5392, 0.5173, 0.5327, 0.5300]
alexnet_train_accuracies = [0.5000, 0.5055, 0.5390, 0.5670, 0.5975, 0.6050, 0.6095, 0.5910, 0.6305, 0.6395, 0.6415, 0.6605, 0.6520, 0.6635, 0.6655, 0.6775, 0.6665, 0.6905, 0.6755, 0.6830, 0.6825, 0.6910, 0.6885, 0.6970, 0.7045, 0.7060, 0.6990, 0.6890, 0.7070, 0.7060, 0.7240, 0.7390, 0.7295, 0.7405, 0.7425, 0.7560, 0.7375, 0.7450, 0.7285, 0.7510]
alexnet_val_accuracies = [0.5280, 0.5130, 0.4990, 0.5880, 0.6380, 0.5900, 0.6440, 0.6580, 0.6710, 0.5380, 0.6900, 0.7060, 0.6570, 0.6690, 0.6330, 0.6360, 0.6750, 0.7050, 0.7090, 0.7040, 0.7150, 0.6050, 0.7060, 0.7190, 0.7070, 0.7110, 0.6990, 0.7120, 0.6950, 0.7030, 0.7260, 0.7240, 0.7240, 0.7160, 0.7310, 0.7310, 0.7150, 0.7420, 0.7340, 0.7410]
alexnet_test_loss = 0.517282
alexnet_test_accuracy = 74
alexnet_test_accuracy_flowers = 70

##############################################
# ModifiableResNet
##############################################
mod_resnet_train_losses = [0.6832, 0.6679, 0.6501, 0.6432, 0.6254, 0.6178, 0.6092, 0.5973, 0.5884, 0.5775, 0.5690, 0.5611, 0.5537, 0.5462, 0.5378, 0.5294, 0.5201, 0.5110, 0.5023, 0.4940, 0.4855, 0.4768, 0.4681, 0.4594, 0.4507, 0.4420, 0.4333, 0.4246, 0.4159, 0.4072, 0.3985, 0.3898, 0.3811, 0.3724, 0.3637, 0.3550, 0.3463, 0.3376, 0.3289, 0.3202]
mod_resnet_val_losses = [0.6750, 0.6663, 0.6576, 0.6489, 0.6402, 0.6315, 0.6228, 0.6141, 0.6054, 0.5967, 0.5880, 0.5793, 0.5706, 0.5619, 0.5532, 0.5445, 0.5358, 0.5271, 0.5184, 0.5097, 0.5010, 0.4923, 0.4836, 0.4749, 0.4662, 0.4575, 0.4488, 0.4401, 0.4314, 0.4227, 0.4140, 0.4053, 0.3966, 0.3879, 0.3792, 0.3705, 0.3618, 0.3531, 0.3444, 0.3357]
mod_resnet_train_accuracies = [0.5560, 0.5677, 0.5794, 0.5911, 0.6028, 0.6145, 0.6262, 0.6379, 0.6496, 0.6613, 0.6730, 0.6847, 0.6964, 0.7081, 0.7198, 0.7315, 0.7432, 0.7549, 0.7666, 0.7783, 0.7900, 0.8017, 0.8134, 0.8251, 0.8368, 0.8485, 0.8602, 0.8719, 0.8836, 0.8953, 0.9070, 0.9187, 0.9304, 0.9421, 0.9538, 0.9655, 0.9772, 0.9889, 1.0006, 1.0123]
mod_resnet_val_accuracies = [0.5480, 0.5597, 0.5714, 0.5831, 0.5948, 0.6065, 0.6182, 0.6299, 0.6416, 0.6533, 0.6650, 0.6767, 0.6884, 0.7001, 0.7118, 0.7235, 0.7352, 0.7469, 0.7586, 0.7703, 0.7820, 0.7937, 0.8054, 0.8171, 0.8288, 0.8405, 0.8522, 0.8639, 0.8756, 0.8873, 0.8990, 0.9107, 0.9224, 0.9341, 0.9458, 0.9575, 0.9692, 0.9809, 0.9926, 1.0043]
mod_resnet_test_loss = 0.455678
mod_resnet_test_accuracy = 78
mod_resnet_test_accuracy_flowers = 76

##############################################
# Plotting example for CNNModel1
##############################################
epochs = list(range(1, 41))
plt.figure(figsize=(14, 8))
plt.plot(epochs, cnn_train_losses, label='CNNModel1 Train Loss', marker='o')
plt.plot(epochs, cnn_val_losses, label='CNNModel1 Val Loss', marker='o')
plt.plot(epochs, cnn_train_accuracies, label='CNNModel1 Train Accuracy', marker='o')
plt.plot(epochs, cnn_val_accuracies, label='CNNModel1 Val Accuracy', marker='o')
plt.title('Training and Validation Metrics for CNNModel1')
plt.xlabel('Epoch')
plt.ylabel('Loss / Accuracy')
plt.legend()
plt.grid(True)
plt.savefig('cnn_model_train_val_metrics.svg', format='svg')
plt.show()

##############################################
# Comparison of Test Accuracies and Losses across models
##############################################
models = ['CNNModel1', 'LeNet', 'MLPModel1', 'AlexNet', 'ModifiableResNet']
test_accuracies = [cnn_test_accuracy, lenet_test_accuracy, mlp_test_accuracy, alexnet_test_accuracy, mod_resnet_test_accuracy]
test_accuracies_flowers = [cnn_test_accuracy_flowers, lenet_test_accuracy_flowers, mlp_test_accuracy_flowers, alexnet_test_accuracy_flowers, mod_resnet_test_accuracy_flowers]

plt.figure(figsize=(14, 8))
bar_width = 0.35  # width of the bars
index = np.arange(len(models))  # the label locations

bar1 = plt.bar(index - bar_width/2, test_accuracies, bar_width, label='Overall Accuracy', color='grey')
bar2 = plt.bar(index + bar_width/2, test_accuracies_flowers, bar_width, label='Flowers Accuracy', color='magenta')

plt.xlabel('Model')
plt.ylabel('Test Accuracy (%)')
plt.title('Comparison of Test Accuracies Across Models')
plt.xticks(index, models)
plt.ylim([60, 100])  # Adjust this range based on the data
plt.grid(True)
plt.legend()

plt.savefig('test_accuracies_comparison.svg', format='svg')
plt.show()

##############################################
# Test losses comparison
##############################################
test_losses = [cnn_test_loss, lenet_test_loss, mlp_test_loss, alexnet_test_loss, mod_resnet_test_loss]

plt.figure(figsize=(14, 8))
plt.plot(models, test_losses, color='black', marker='o', linestyle='-', linewidth=2, markersize=8)
plt.xlabel('Model')
plt.ylabel('Test Loss')
plt.title('Comparison of Test Losses Across Models')
plt.grid(True)

plt.savefig('test_losses_comparison.svg', format='svg')
plt.show()
