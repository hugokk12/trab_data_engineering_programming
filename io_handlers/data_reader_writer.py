"""
Módulo de leitura e escrita de dados com schemas explícitos.
"""

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
    BooleanType,
    IntegerType,
    TimestampType
)


class DataReaderWriter:
    """Classe responsável pelo I/O de dados utilizando Schemas explícitos."""

    def __init__(self, spark: SparkSession):
        self.spark = spark

    def get_pedidos_schema(self) -> StructType:
        """
        Retorna o schema explícito para o dataset de Pedidos (CSV).
        Ajuste os nomes dos campos e tipos conforme o repositório/especificação oficial.
        """
        return StructType([
            StructField("id_pedido", StringType(), True),
            StructField("uf", StringType(), True),
            StructField("data_pedido", StringType(), True), # ou TimestampType dependendo do formato
            StructField("valor_total", DoubleType(), True)
        ])

    def get_pagamentos_schema(self) -> StructType:
        """
        Retorna o schema explícito para o dataset de Pagamentos (JSON).
        Ajuste os nomes dos campos e tipos conforme o repositório/especificação oficial.
        """
        return StructType([
            StructField("id_pedido", StringType(), True),
            StructField("forma_pagamento", StringType(), True),
            StructField("status", BooleanType(), True),
            StructField("fraude", BooleanType(), True)
        ])

    def read_pedidos(self, path: str) -> DataFrame:
        """
        Lê os arquivos CSV (mesmo se compactados/zipados) aplicados com Schema explícito.
        """
        return (
            self.spark.read
            .option("header", "true")
            .schema(self.get_pedidos_schema()) # Schema explícito obrigatório
            .csv(path)
        )

    def read_pagamentos(self, path: str) -> DataFrame:
        """
        Lê os arquivos JSON (mesmo se compactados/zipados) aplicados com Schema explícito.
        """
        return (
            self.spark.read
            .schema(self.get_pagamentos_schema()) # Schema explícito obrigatório
            .json(path)
        )

    def write_parquet(self, df: DataFrame, output_path: str) -> None:
        """
        Grava o DataFrame resultante em formato Parquet.
        """
        df.write.mode("overwrite").parquet(output_path)