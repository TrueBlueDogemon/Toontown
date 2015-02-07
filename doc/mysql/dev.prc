# Distribution:
distribution dev

# Art assets:
model-path ../resources

# Server:
server-version fellowship-dev
min-access-level 100
accountdb-type mysqldb
mysql-login toontown
mysql-password xxxxx
shard-low-pop 50
shard-mid-pop 100

# RPC:
want-rpc-server #t
rpc-server-endpoint http://localhost:8080/
rpc-server-secret yyyyy

# DClass files (in reverse order):
dc-file astron/dclass/toon.dc
dc-file astron/dclass/otp.dc

# Core features:
want-pets #f
want-parties #f
want-cogdominiums #f
want-achievements #f

# Chat:
want-whitelist #t

# Cashbot boss:
want-resistance-toonup #t
want-resistance-restock #t

# Optional:
want-yin-yang #t

# Developer options:
show-population #t
force-skip-tutorial #f
want-instant-parties #t
