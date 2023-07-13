-- --------------------------------------------------------
-- Servidor:                     db.tgzrgprcshzcgcjxxsgq.supabase.co
-- Versão do servidor:           PostgreSQL 15.1 (Ubuntu 15.1-1.pgdg20.04+1) on aarch64-unknown-linux-gnu, compiled by gcc (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0, 64-bit
-- OS do Servidor:               
-- HeidiSQL Versão:              12.4.0.6665
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES  */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Copiando estrutura para tabela public.dados_cashback
CREATE TABLE IF NOT EXISTS "dados_cashback" (
	"id" BIGINT NOT NULL,
	"empresa" BIGINT NULL DEFAULT NULL,
	"porcentagem" REAL NULL DEFAULT NULL,
	"created_at" TIMESTAMPTZ NULL DEFAULT 'now()',
	PRIMARY KEY ("id"),
	CONSTRAINT "dados_cashback_empresa_fkey" FOREIGN KEY ("empresa") REFERENCES "plataformas" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION
);

-- Copiando dados para a tabela public.dados_cashback: 2 rows
DELETE FROM "dados_cashback";
/*!40000 ALTER TABLE "dados_cashback" DISABLE KEYS */;
INSERT INTO "dados_cashback" ("id", "empresa", "porcentagem", "created_at") VALUES
	(1, 1, 5, '2023-07-08 18:10:49.081476+00'),
	(2, 3, 3, '2023-07-08 18:11:00.359671+00');
/*!40000 ALTER TABLE "dados_cashback" ENABLE KEYS */;

-- Copiando estrutura para tabela public.plataformas
CREATE TABLE IF NOT EXISTS "plataformas" (
	"id" BIGINT NOT NULL,
	"nome" VARCHAR NOT NULL,
	PRIMARY KEY ("id")
);

-- Copiando dados para a tabela public.plataformas: 3 rows
DELETE FROM "plataformas";
/*!40000 ALTER TABLE "plataformas" DISABLE KEYS */;
INSERT INTO "plataformas" ("id", "nome") VALUES
	(1, 'meliuz'),
	(2, 'cuponomia'),
	(3, 'intershop');
/*!40000 ALTER TABLE "plataformas" ENABLE KEYS */;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
