class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: list["HTMLNode"] = None,
        props: dict[str, str] = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props:
            return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
        return ""

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return (
            f"{class_name}("
            f"tag={repr(self.tag)}, "
            f"value={repr(self.value)}, "
            f"props={repr(self.props)}, "
            f"children={repr(self.children)})"
        )


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str, str] = None) -> None:
        super().__init__(tag, value, props=props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("Leaf node must have a value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
