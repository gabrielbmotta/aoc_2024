function part1(input)
    input_str = join(input, "")
    matches = collect(eachmatch(r"mul\((\d{1,3}),(\d{1,3})\)", input_str))
    
    products = [
        parse(Int, m.captures[1]) * parse(Int, m.captures[2]) 
        for m in matches
    ]
    
    return sum(products)
end

function part2(input)
    input_str = join(input, "")
    mul_matches = collect(eachmatch(r"mul\((\d{1,3}),(\d{1,3})\)", input_str))
    true_matches = collect(eachmatch(r"do\(\)", input_str))
    false_matches = collect(eachmatch(r"don't\(\)", input_str))
    
    # Use tuples instead of structs
    muls = [
        (
            val1 = parse(Int, m.captures[1]),
            val2 = parse(Int, m.captures[2]),
            start = m.offset
        ) for m in mul_matches
    ]
    
    conditions = vcat(
        [(start = m.offset, value = true) for m in true_matches],
        [(start = m.offset, value = false) for m in false_matches]
    )
    
    # Sort and process conditions
    sort!(conditions, by = x -> x.start)
    sort!(muls, by = x -> x.start)
    
    current_condition = true
    filtered_products = Int[]
    
    for mul in muls
        # Update condition based on most recent condition before this multiplication
        for cond in conditions
            if cond.start <= mul.start
                current_condition = cond.value
            end
        end
        
        # Add product if condition is true
        if current_condition
            push!(filtered_products, mul.val1 * mul.val2)
        end
    end
    
    return sum(filtered_products)
end

# Read input
filepath = joinpath(@__DIR__, "test.txt")
input = readlines(filepath)

# Run both parts
println("Part 1: ", part1(input))
println("Part 2: ", part2(input))