resource "yandex_mdb_mongodb_cluster" "mongodb" {
  name        = "pidor-mongo"
  environment = "PRODUCTION"
  network_id  = yandex_vpc_network.internal.id
  deletion_protection = true

  description = "Кластер для баз для бота"
  cluster_config {
    version = "6.0"
  }

  database {
    name = "pidor"
  }

  user {
    name     = "pidor"
    password = var.mongo_password
    permission {
      database_name = "admin"
      roles = [
        "mdbMonitor",
        "mdbShardingManager",
      ]
    }
    permission {
      database_name = "pidor"
      roles = [
        "mdbDbAdmin",
        "readWrite",
      ]
    }
  }

  resources {
    resource_preset_id = "b3-c1-m4"
    disk_size          = 10
    disk_type_id       = "network-hdd"
  }

  host {
    zone_id          = yandex_vpc_subnet.internal-d.zone
    subnet_id        = yandex_vpc_subnet.internal-d.id
    assign_public_ip = false
  }

}
