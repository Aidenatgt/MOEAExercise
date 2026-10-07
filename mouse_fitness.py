class MouseFitness:
    def __init__(
        self,
        price: int,
        cord_length: int,
        dpi: int,
        ergonomics: int,
        click_quality: int,
    ):
        """
        Assuming the `price` value is the 'quality' of the price where a higher number is better.
        This fits the MOEA problem where we want to maximize all the values in the fitness function.
        """
        self.price = price
        self.cord_length = cord_length
        self.dpi = dpi
        self.ergonomics = ergonomics
        self.click_quality = click_quality

    def dominates(self, other: MouseFitness) -> bool:
        return (
            self.price >= other.price
            and self.cord_length >= other.cord_length
            and self.dpi >= other.dpi
            and self.ergonomics >= other.ergonomics
            and self.click_quality >= other.click_quality
            and (
                self.price > other.price
                or self.cord_length > other.cord_length
                or self.dpi > other.dpi
                or self.ergonomics > other.ergonomics
                or self.click_quality > other.click_quality
            )
        )

    def __str__(self) -> str:
        return f"Price: {self.price}, Cord Length: {self.cord_length}, DPI: {self.dpi}, Ergonomics: {self.ergonomics}, Click Quality: {self.click_quality}"

    def row_str(self) -> str:
        return f"{self.price}\t{self.cord_length}\t\t{self.dpi}\t{self.ergonomics}\t\t{self.click_quality}"


class MultiObjectiveMouseFitness:
    def __init__(
        self,
        qualities: list[int],
    ):

        self.qualities: list[int] = qualities

    def dominates(self, other: MultiObjectiveMouseFitness) -> bool:
        return all(
            self_quality >= other_quality
            for self_quality, other_quality in zip(self.qualities, other.qualities)
        ) and any(
            self_quality > other_quality
            for self_quality, other_quality in zip(self.qualities, other.qualities)
        )

    def __str__(self) -> str:
        return "\t".join(f"{quality}" for i, quality in enumerate(self.qualities))
