class Parameters:
    def __init__(self):
        self.max_pos = 950
        self.params = {}
        self.etf_params = {
            "min_margin": 1,
            "fade": 20,
            "edge_sensitivity": 1,
            "slack": 2
        }
        self.contract_params = {
            "min_margin": 1,
            "fade": 40, #increasing fade reduces profit AND loss (hitter); decreasing fade increases profit AND loss (non-hitter)
            "edge_sensitivity": 1, #increasing to 1 increases frequency; decreasing to 0.1 increases profit per trade; switch when expected pnl is going down
            "slack":2    #2: 1-3; 3: 1-4; 4: 1-5
        }
        for c in ["EPT", "DLO", "MKU", "IGM", "BRV"]:
            self.params[c] = self.contract_params
        for c in ["SCP", "JAK"]:
            self.params[c] = self.etf_params

def get_params():
    return Parameters()