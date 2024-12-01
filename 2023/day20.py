import math

class Module:
    def __init__(self, module_description) -> None:
        self.name = module_description.split(" -> ")[0]
        if self.name[0] in "%&":
            self.name = self.name[1:]
        self.destination_modules = module_description.split(" -> ")[1].split(", ")
        self.input_modules = {}
    
    def process_pulse(self, pulse):
        return []
    
    def reset(self):
        return
    
    def send_pulse(self, pulse_type):
        return [(destination, pulse_type, self.name) for destination in self.destination_modules]
    
    def register_input_module(self, input_name):
        self.input_modules[input_name] = "low"


class Flipflop(Module):
    def __init__(self, module_description) -> None:
        super().__init__(module_description)
        self.on = False
    
    def process_pulse(self, pulse):
        if pulse[1] == "high":
            return []
        self.on = not self.on
        if self.on:
            return self.send_pulse("high")
        if not self.on:
            return self.send_pulse("low")
        
    def reset(self):
        self.on = False
    
    def __str__(self) -> str:
        return f"name: {self.name}, on: {self.on}"


class Conjunction(Module):
    def __init__(self, module_description) -> None:
        super().__init__(module_description)
        
    def process_pulse(self, pulse):
        self.input_modules[pulse[2]] = pulse[1]
        if all(pulse == "high" for pulse in self.input_modules.values()):
            return self.send_pulse("low")
        else:
            return self.send_pulse("high")
    
    def reset(self):
        for key in self.input_modules.keys():
            self.input_modules[key] = "low"
    
    def __str__(self) -> str:
        return f"name: {self.name}, inputs: {self.input_modules.values()}"


class Broadcaster(Module):
    def __init__(self, module_description) -> None:
        super().__init__(module_description)
        
    def process_pulse(self, pulse):
        return self.send_pulse(pulse[1])
    
    def reset(self):
        return

    def __str__(self) -> str:
        return f"name: {self.name}"


def push_button():
    pulse_queue.append(("broadcaster", "low"))

    while pulse_queue:
        pulse = pulse_queue.pop(0)
        pulse_counter[pulse[1]] += 1
        if pulse[0] in modules.keys():
            pulse_queue.extend(modules[pulse[0]].process_pulse(pulse))


def button_pushes_until_rx():
    button_pushes = 0
    rx_input = list(modules["rx"].input_modules.keys())[0]
    cycle_lengths = {key:0 for key in modules[rx_input].input_modules.keys()}

    while not all(v > 0 for v in cycle_lengths.values()):
        pulse_queue.append(("broadcaster", "low"))
        button_pushes += 1
        
        while pulse_queue:
            pulse = pulse_queue.pop(0)
            if pulse[0] == rx_input and pulse[1] == "high":
                cycle_lengths[pulse[2]] = button_pushes
            pulse_queue.extend(modules[pulse[0]].process_pulse(pulse))

    # all the numbers are prime, so i can use product instead of lcm
    return math.prod(cycle_lengths.values())


if __name__ == "__main__":
    file = "inputs/20/input.txt"
    puzzle_input = open(file).read().strip().split("\n")
    modules = {}
    pulse_queue = []
    pulse_counter = {"low":0, "high":0}

    # create modules
    modules["rx"] = Module("rx -> output")
    for line in puzzle_input:
        name = line.split(" -> ")[0]
        match name[0]:
            case "%":
                modules[name[1:]] = Flipflop(line)
            case "&":
                modules[name[1:]] = Conjunction(line)
            case "b":
                modules[name] = Broadcaster(line)
            case _:
                raise ValueError
        
    # register input modules
    for line in puzzle_input:
        input_module, destination_module = line.split(" -> ")
        if input_module[0] in "%&":
            input_module = input_module[1:]
        for m in destination_module.split(", "):
            modules[m].register_input_module(input_module)

    for i in range(1000):
        push_button()
    print("part 1:", pulse_counter["low"] * pulse_counter["high"])

    #-------------------------------------------------------------------

    # reset all the modules to default state before starting with part 2
    for key in modules.keys():
        modules[key].reset()

    print("part 2:", button_pushes_until_rx())
    
