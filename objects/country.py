# Define Country object
class Country:
    def __init__(self, country: str, population: int, area: int) -> None:
        self.country = country
        self.population = population
        self.area = area
        self.is_big = population >= 20000000 or area >= 3000000
        
# Define method to calculate population dencity    
    def population_density(self) -> float:
        return self.population / self.area

# Assign method and attributes to compare the two countries density
    def compare_pop_density(self, other_country) -> str:
        self_density = self.population_density()
        other_density = other_country.population_density()
# Perform the comparison        
        if self_density > other_density:
            return f"{self.country} has a larger population density than {other_country.country}"
        elif self_density < other_density:
            return f"{self.country} has a smaller population density than {other_country.country}"
        else:
            return f"{self.country} has a same population density like {other_country.country}"

# Data        
australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

# Print results

result = australia.compare_pop_density(andorra)
print(result)

result = andorra.compare_pop_density(australia)
print(result)