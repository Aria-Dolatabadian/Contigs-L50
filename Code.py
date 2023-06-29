def calculate_l50(lengths):
    sorted_lengths = sorted(lengths, reverse=True)
    total_length = sum(sorted_lengths)
    half_length = total_length / 2

    cumulative_length = 0
    l50 = None
    for i, length in enumerate(sorted_lengths, start=1):
        cumulative_length += length
        if cumulative_length >= half_length:
            l50 = i
            break

    return l50


# Example usage
contig_lengths = [500, 1000, 750, 200, 300, 900, 1500, 1200]
l50 = calculate_l50(contig_lengths)
print("L50 value:", l50)

#To calculate the L50 value, the contigs or reads are first arranged in descending order based on their lengths. 
#The lengths are then summed cumulatively until the cumulative length reaches or exceeds 50% of the total assembly or sequencing length. 
#The L50 value is the minimum number of contigs or reads needed to achieve this coverage.
