function compute_angle(origin,point)

    degree = atan((origin[2] - point[2]),(point[1] - origin[1])) * (180/pi)
    if degree > 90
        degree = 450 - degree
    else
        degree = 90 - degree
    end
    return degree
end

function compute_distance(origin,point)
    distance = sqrt((origin[1] - point[1])^2 + (origin[2] - point[2])^2)
    return distance
end

f = open("day10.txt");
ast_list = []
for (y, line) in enumerate(readlines(f))
    for (x, value) in enumerate(line)
        if value == '#'
            push!(ast_list,[x-1,y-1])
        end

    end
end
detected = -1
station = -1
for ast in ast_list
    detected_angles = Set()
    for other in ast_list
        if ast != other
            push!(detected_angles,compute_angle(ast,other))
        end
    end
    if length(detected_angles) > detected
        global detected
        global station
        detected = length(detected_angles)
        station = ast
    end
end

println(detected)
println(station)

filter!(x->x!=station,ast_list)

angle_dict = Dict()
for ast in ast_list
    angle = compute_angle(station,ast)

    if haskey(angle_dict, angle) == false
        push!(angle_dict,angle=>[ast])
    else
        value = angle_dict[angle]
        append!(value,[ast])
    end
end
iter = 0
for angle in sort([i for i in keys(angle_dict)],by=abs)
    remove = typemax(Float64)
    vaporized = nothing
    for i in angle_dict[angle]
        dist = compute_distance(station,i)
        if dist < remove
            remove = dist
            vaporized = i
        end
    end
    global iter
    iter += 1
    if iter == 200
        solution = vaporized[1]*100 + vaporized[2]
        println("Vaporize $vaporized, solution is $solution")
        break
    end
end
