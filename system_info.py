import psutil
import json
import time


def get_cpu_usage():
    # current CPU utilization as %
    return psutil.cpu_percent(interval=1)


def get_memory_stats():
    mem = psutil.virtual_memory()
    total_memory = mem.total / (1024 * 1024)  # to MB
    used_memory = mem.used / (1024 * 1024)  # to MB
    memory_usage = mem.percent
    return memory_usage, total_memory, used_memory


def get_disk_stats():
    disk = psutil.disk_usage('/')
    total_disk_space = disk.total / (1024 * 1024)  # to MB
    used_disk_space = disk.used / (1024 * 1024)  # to MB
    disk_usage = disk.percent
    return disk_usage, total_disk_space, used_disk_space


def get_network_usage():
    net_io = psutil.net_io_counters()
    network_in = net_io.bytes_recv / 1024  # to KB
    network_out = net_io.bytes_sent / 1024  # to KB
    return network_in, network_out


def get_system_data():
    cpu_usage = get_cpu_usage()
    memory_usage, total_memory, used_memory = get_memory_stats()
    disk_usage, total_disk_space, used_disk_space = get_disk_stats()
    network_in, network_out = get_network_usage()

    system_data = {
        "cpu_usage_percentage": cpu_usage,
        "memory_usage_percentage": memory_usage,
        "total_memory_MB": total_memory,
        "used_memory_MB": used_memory,
        "disk_usage_percentage": disk_usage,
        "total_disk_space_MB": total_disk_space,
        "used_disk_space_MB": used_disk_space,
        "network_in_KB": network_in,
        "network_out_KB": network_out,
        "timestamp_UTC": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())  # ISO 8601 format
    }

    return system_data


def main():
    system_data = get_system_data()
    formatted_json = json.dumps(system_data, indent=2)
    print(formatted_json)


if __name__ == "__main__":
    main()
