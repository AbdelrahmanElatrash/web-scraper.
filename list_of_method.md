- BeautifulSoup(markup, parser):

Constructor that creates a BeautifulSoup object from the given markup (HTML or XML) and a specified parser.
Navigating the parse tree:

- find(name, attrs, recursive, text, **kwargs): Finds the first matching element based on the given criteria.
- find_all(name, attrs, recursive, text, limit, **kwargs): Finds all matching elements based on the given criteria.
- select(selector): Returns a list of elements that match the provided CSS selector.
- parent: Navigates to the parent element.
- parents: Iterates over all the ancestor elements.
- next_sibling, previous_sibling: Navigates to the next or previous sibling element.
- next_siblings, previous_siblings: Iterates over the next or previous sibling elements.
- contents: Returns a list of all direct children elements.
- string: Returns the string content of a single element.
Accessing element attributes and values:

- tag.name: Returns the name of the tag.
- tag.text: Returns the text content of the tag, including the text content of its children.
- tag.get(attribute): Returns the value of the specified attribute.
- tag['attribute']: Another way to access the value of an attribute.
Modifying the parse tree:

- new_tag(name, attrs): Creates a new Tag object with the given name and attributes.
- insert(position, element): Inserts an element at the specified position within the current element.
- append(element), prepend(element): Adds an element at the end or beginning of the current element.
- extract(): Removes the current element from the parse tree.
Miscellaneous:

- prettify(): Returns a well-formatted string representation of the parse tree.
- decode(): Decodes a string with HTML entities into its Unicode representation.

## documentation link
[documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)