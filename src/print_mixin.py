class PrintMixin:
    def print_info(self, *args) -> None:
        print(
            f"{self.__class__.__name__}{args}"
        )
