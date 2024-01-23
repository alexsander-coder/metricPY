import pandas as pd

#calc Lifetime Value (LTV) dos assinantes.
def calculate_ltv(df, retention_period_months=12):
    avg_subscription_value = df['valor'].mean()
    ltv = avg_subscription_value * retention_period_months
    return ltv

#calc o average revenue per account (ARPA).
def calculate_arpa(df):
    total_revenue = df['valor'].sum()
    unique_accounts = df['ID assinante'].nunique()
    arpa = total_revenue / unique_accounts if unique_accounts > 0 else 0
    return arpa

#calc da taxa de churn (churn rate).
def calculate_churn_rate(df):
    total_clientes_inicio = len(df[(df['data início'] <= df['data início'].min()) & (df['status'] == 'Ativa')])
    total_cancelamentos = len(df[(df['status'] == 'Cancelada') & (df['data status'] >= df['data início'].min()) & (df['data status'] <= df['data início'].max())])
    churn_rate = total_cancelamentos / total_clientes_inicio if total_clientes_inicio > 0 else 0
    return churn_rate

#calc o monthly recurring revenue (MRR).
def calculate_mrr(df):
    return df[df['status'] == 'Ativa'].apply(lambda row: row['valor'] * (30 / row['cobrada a cada X dias']), axis=1).sum()

#agrupa os dados por mes e ano e calcula todas as metricas acima por grupo.
def calculate_metrics(df):
    df['data início'] = pd.to_datetime(df['data início'])
    df['data status'] = pd.to_datetime(df['data status'])
    df['próximo ciclo'] = pd.to_datetime(df['próximo ciclo'], errors='coerce')
    df['mes_ano'] = df['data início'].dt.to_period('M')

    grouped = df.groupby('mes_ano')
    metrics_list = []

    for name, group in grouped:
        mrr = calculate_mrr(group)
        churn_rate = calculate_churn_rate(group)
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
