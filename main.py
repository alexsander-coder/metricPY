from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    if file.filename.endswith('.xlsx'):
        df = pd.read_excel(file.file)
    elif file.filename.endswith('.csv'):
        df = pd.read_csv(file.file)
    else:
        return {"error": "Formato de arquivo não suportado"}

    try:
        metrics_list = calculate_metrics(df)

        print("Métricas Calculadas para o arquivo:", file.filename)
        for metricas in metrics_list:
            print(f"Métricas para {metricas['mes_ano']}:")
            print("MRR:", metricas["MRR"])
            print("Churn Rate:", metricas["Churn Rate"])
            print("LTV:", metricas["LTV"])
            print("ARPA:", metricas["ARPA"])

    except Exception as e:
        print(f"Erro ao processar arquivo {file.filename}: {e}")
        return {"error": f"Erro ao processar arquivo: {e}"}

    return {"filename": file.filename, "metrics": metrics_list}

def calculate_ltv(df, retention_period_months=12):
    avg_subscription_value = df['valor'].mean()
    ltv = avg_subscription_value * retention_period_months
    return ltv

def calculate_arpa(df):
    total_revenue = df['valor'].sum()
    unique_accounts = df['ID assinante'].nunique()
    arpa = total_revenue / unique_accounts if unique_accounts > 0 else 0
    return arpa

def calculate_metrics(df):
    try:
        df['data início'] = pd.to_datetime(df['data início'])
        df['data status'] = pd.to_datetime(df['data status'])
        df['próximo ciclo'] = pd.to_datetime(df['próximo ciclo'], errors='coerce')

        df['mes_ano'] = df['data início'].dt.to_period('M')

        grouped = df.groupby('mes_ano')

        metrics_list = []
        for name, group in grouped:
            mrr = group[group['status'] == 'Ativa'].apply(lambda row: row['valor'] * (30 / row['cobrada a cada X dias']), axis=1).sum()
            
            periodo_inicio = group['data início'].min()
            periodo_fim = group['data início'].max()

            total_clientes_inicio = len(group[(group['data início'] <= periodo_inicio) & (group['status'] == 'Ativa')])
            total_cancelamentos = len(group[(group['status'] == 'Cancelada') & (group['data status'] >= periodo_inicio) & (group['data status'] <= periodo_fim)])
            
            churn_rate = total_cancelamentos / total_clientes_inicio if total_clientes_inicio > 0 else 0
            ltv = calculate_ltv(group)
            arpa = calculate_arpa(group)
            

            metrics_list.append({
                "mes_ano": str(name),
                "MRR": mrr,
                "Churn Rate": churn_rate,
                "LTV": ltv,
                "ARPA": arpa
            })

        return metrics_list

    except Exception as e:
        raise Exception(f"Erro ao calcular métricas: {e}")
