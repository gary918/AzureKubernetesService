from fastapi import FastAPI, HTTPException

app = FastAPI()

# 模拟数据
samples = [{'id': 1, 'name': 'Sample 1'}, {'id': 2, 'name': 'Sample 2'}]

# 创建一个路由，用于获取所有样本
@app.get("/samples/")
async def get_samples():
    return samples

# 创建一个路由，用于获取特定样本
@app.get("/samples/{sample_id}")
async def get_sample(sample_id: int):
    sample = next((sample for sample in samples if sample['id'] == sample_id), None)
    if sample is None:
        raise HTTPException(status_code=404, detail="Sample not found")
    return sample

# 创建一个路由，用于创建新样本
@app.post("/samples/")
async def create_sample(sample: dict):
    new_sample = {'id': len(samples) + 1, **sample}
    samples.append(new_sample)
    return new_sample

# 创建一个路由，用于更新特定样本
@app.put("/samples/{sample_id}")
async def update_sample(sample_id: int, updated_sample: dict):
    sample = next((sample for sample in samples if sample['id'] == sample_id), None)
    if sample is None:
        raise HTTPException(status_code=404, detail="Sample not found")
    sample.update(updated_sample)
    return sample

# 创建一个路由，用于删除特定样本
@app.delete("/samples/{sample_id}")
async def delete_sample(sample_id: int):
    sample = next((sample for sample in samples if sample['id'] == sample_id), None)
    if sample is None:
        raise HTTPException(status_code=404, detail="Sample not found")
    samples.remove(sample)
    return {"message": "Sample deleted"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
