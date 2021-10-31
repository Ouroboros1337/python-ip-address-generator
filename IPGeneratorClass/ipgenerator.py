class All_ips():
    def __init__(self, start_ip: str = "0.0.0.0", end_ip: str = "255.255.255.255", ip_range: int = None):
        self.start_ip = start_ip
        if ip_range is None:
            self.end_ip = end_ip
        else:
            self.end_ip = self.alter_ip(start_ip, ip_range)
        self.lastindex = self.get_index(self.end_ip)-1
        self.index = 0
        self.length = None

    def __repr__(self):
        return f"from {self.start_ip} to {self.end_ip}"

    def __call__(self, *args, index: int = None, ip: str = None):
        if index is not None:
            assert index <= self.lastindex, "Index not in Range"
            return self.alter_ip(self.start_ip, index)
        if ip is not None:
            rv = self.get_index(ip)
            assert rv <= self.lastindex, "IP not in Range"
            return rv
        raise Warning("please use index=value or ip=value to call the All_ips class")

    def __iter__(self):
        return self

    def __next__(self):
        rv = self.alter_ip(self.start_ip, self.index)
        if self.index == len(self):
            raise StopIteration
        self.index += 1
        return rv

    def __add__(self, other):
        start = self.start_ip if self.get_index(self.start_ip) < self.get_index(other.start_ip) else other.start_ip
        end = self.end_ip if self.get_index(self.end_ip) > self.get_index(other.end_ip) else other.end_ip
        return All_ips(start,end)


    def __len__(self):
        if self.length is None:
            self.length = self.ip_to_int(self.end_ip) - self.ip_to_int(self.start_ip)
        return self.length

    def get_index(self, ip):
        return self.ip_to_int(ip) - self.ip_to_int(self.start_ip)


    @staticmethod
    def alter_ip(ip: str, offset: int):
        return All_ips.int_to_ip(All_ips.ip_to_int(ip) + offset)

    @staticmethod
    def ip_to_int(ip: str):
        return int("".join([bin(int(x) + 256)[3:] for x in ip.split(".")]), 2)

    @staticmethod
    def int_to_ip(i: int):
        return ".".join([str(int((bin(i + 2 ** 32)[3:])[8 * x:8 * x + 8], 2)) for x in range(4)])
