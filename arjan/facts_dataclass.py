from dataclasses import dataclass, field

@dataclass(kw_only=True)
class User:
    name: str
    email: str
    active: bool = True
    tags: list[str] = field(default_factory=list[str]) #FACT-1

    #a property i dont want to change again and again and also dont want to define while creating object
    slug: str  = field(init=False)  #FACT-2

    def __post_init__(self):
        slugified = self.name.lower().replace(" ", "-")
        self.slug = slugified



def main():
    u1 = User(name="aayush hooda", email="aayush@gmail.com", active=True)
    u2 = User(name="kavya mohan", email="kavya@gmail.com", active=False)
    print("U1: ",u1)
    print("U2: ",u2)


if __name__ == "__main__":
    main()