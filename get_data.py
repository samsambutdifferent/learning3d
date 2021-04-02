from learning3d.data_utils import ModelNet40Data, ClassificationData, RegistrationData, FlowData

modelnet40 = ModelNet40Data(train=True, num_points=1024, download=True)
classification_data = ClassificationData(data_class=ModelNet40Data())

registration_data = RegistrationData(algorithm='PointNetLK', data_class=ModelNet40Data(), partial_source=False, partial_template=False, noise=False)
flow_data = FlowData()

print(flow_data)