from services.dataloader import DataLoader

loader = DataLoader()

data = loader.load_all_data()

print(data.keys())