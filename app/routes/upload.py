from fastapi import APIRouter, File, UploadFile, HTTPException
import pandas as pd
from utils.calculation import calculate_metrics

router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    if not (file.filename.endswith('.xlsx') or file.filename.endswith('.csv')):
        raise HTTPException(status_code=400, detail="Formato de arquivo não suportado")

    try:
        if file.filename.endswith('.xlsx'):
            df = pd.read_excel(file.file)
        elif file.filename.endswith('.csv'):
            df = pd.read_csv(file.file)

        metrics_list = calculate_metrics(df)

        return {"filename": file.filename, "metrics": metrics_list}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar arquivo: {e}")
