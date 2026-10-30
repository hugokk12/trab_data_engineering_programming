class AppConfig:
    """Classe de configurações centralizadas da aplicação."""

    PEDIDOS_PATH: str = "data/pedidos/*.zip"  # ou "data/pedidos" para ler todos os arquivos da pasta
    PAGAMENTOS_PATH: str = "data/pagamentos/*.zip" # ou "data/pagamentos"
    OUTPUT_PATH: str = "data/output/relatorio_pedidos_recusados.parquet"