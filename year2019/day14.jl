Pkg.add("DataStructures");
using DataStructures;

chem_dict = Dict()
f = open("day14.txt");
for line in readlines(f)
    input,output = split(line, " => ")
    o_quant, o_name = split(output)
    push!(chem_dict,o_name => Dict("quantity"=>o_quant, "required_mats"=>[(parse(Int64,each[1]),each[2]) for each in [split(mat) for mat in split(input,", ")]]))
end

function compute_ore_required(fuel_amount)
    global chem_dict
    production_queue = Queue{Any}()
    reserves = DefaultDict(0)
    enqueue!(production_queue,(fuel_amount,"FUEL"))
    while isempty(production_queue) != true
        chem = dequeue!(production_queue)
        quantity,name = chem[1],chem[2]
        if name == "ORE" # Terminal. We are now adding ORES
            reserves["ORE"] += quantity
        elseif reserves[name] >= quantity # We have enough w.o producing
            reserves[name] -= quantity
        else
            required = quantity - reserves[name] #amount we need
            runs = ceil(required/parse(Int64,chem_dict[name]["quantity"])) # Each run produces no fractional output. Only exacts
            reserves[name] = runs * parse(Int64,chem_dict[name]["quantity"]) - required # Compute how much new stuff we got subtract required for current rxn
            for each in chem_dict[name]["required_mats"]
                req_quant,req_name = each[1],each[2]
                enqueue!(production_queue,(req_quant*runs,req_name)) # multiply each ele in mats by how many runs of production we need and enqueue
            end
        end
    end
    return reserves["ORE"]
end

println(compute_ore_required(1))
# Binary search
low = 0
high = 10^12
while low+1 < high
    global low,high
    mid = low + floor((high - low)//2)
    result =  compute_ore_required(mid)
    if result < 10^12
        low = mid
    else
        high = mid - 1
    end
end
println(Int(low))
