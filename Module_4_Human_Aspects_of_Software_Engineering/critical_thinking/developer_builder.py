# Developer builder pattern


# The developer Class - The product being built by the DeveloperBuilder

class Developer: 
    def __init__(self):
        self.brutal_honesty = None
        self.adaptability = None
        self.collaboration = None
        
    def traits(self):
        traits_list = [
            ("Brutal Honesty", self.brutal_honesty),
            ("Adaptability", self.adaptability),
            ("Collaboration", self.collaboration),
        ]
        return ([name, description] for name, description in traits_list if description is not None)
        
    def describe_traits(self):
        print()
        print("Building your ideal developer...")
        traits = self.traits()
        traits_total = 0
        for name, description in traits:
            traits_total += 1
            print(f"Trait: {name} - {description}")
        print(f"Total traits: {traits_total}")
        print()
            
# The DeveloperBuilder Class - The builder for the Developer product
class DeveloperBuilder:
    def __init__(self):
        self.developer = Developer()

    def with_brutal_honesty(self):
        self.developer.brutal_honesty = "Being able to communicate difficult truths effectively so problems are addressed early"
        return self

    def with_adaptability(self):
        self.developer.adaptability = "Enables flexibility as tools, requirements, and environments change"
        return self

    def with_collaboration(self):
        self.developer.collaboration = "Fosters teamwork and effective communication within the development team"
        return self

    def build(self):
        return self.developer
    
# The DeveloperDirector Class - Directs the construction of the Developer product
class DeveloperDirector:
    def construct_ideal_developer(self, builder):
        return (
            builder
            .with_brutal_honesty()
            .with_adaptability()
            .with_collaboration()
            .build()
        )
        
if __name__ == "__main__":
    director = DeveloperDirector()
    developer = director.construct_ideal_developer(DeveloperBuilder())
    developer.describe_traits()