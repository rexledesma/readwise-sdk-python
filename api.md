# Shared Types

```python
from readwise_sdk.types import Order
```

# Pets

Types:

```python
from readwise_sdk.types import APIResponse, Pet, PetFindByStatusResponse, PetFindByTagsResponse
```

Methods:

- <code title="post /pet">client.pets.<a href="./src/readwise_sdk/resources/pets.py">create</a>(\*\*<a href="src/readwise_sdk/types/pet_create_params.py">params</a>) -> <a href="./src/readwise_sdk/types/pet.py">Pet</a></code>
- <code title="get /pet/{petId}">client.pets.<a href="./src/readwise_sdk/resources/pets.py">retrieve</a>(pet_id) -> <a href="./src/readwise_sdk/types/pet.py">Pet</a></code>
- <code title="put /pet">client.pets.<a href="./src/readwise_sdk/resources/pets.py">update</a>(\*\*<a href="src/readwise_sdk/types/pet_update_params.py">params</a>) -> <a href="./src/readwise_sdk/types/pet.py">Pet</a></code>
- <code title="delete /pet/{petId}">client.pets.<a href="./src/readwise_sdk/resources/pets.py">delete</a>(pet_id) -> None</code>
- <code title="get /pet/findByStatus">client.pets.<a href="./src/readwise_sdk/resources/pets.py">find_by_status</a>(\*\*<a href="src/readwise_sdk/types/pet_find_by_status_params.py">params</a>) -> <a href="./src/readwise_sdk/types/pet_find_by_status_response.py">PetFindByStatusResponse</a></code>
- <code title="get /pet/findByTags">client.pets.<a href="./src/readwise_sdk/resources/pets.py">find_by_tags</a>(\*\*<a href="src/readwise_sdk/types/pet_find_by_tags_params.py">params</a>) -> <a href="./src/readwise_sdk/types/pet_find_by_tags_response.py">PetFindByTagsResponse</a></code>
- <code title="post /pet/{petId}">client.pets.<a href="./src/readwise_sdk/resources/pets.py">update_by_id</a>(pet_id, \*\*<a href="src/readwise_sdk/types/pet_update_by_id_params.py">params</a>) -> None</code>
- <code title="post /pet/{petId}/uploadImage">client.pets.<a href="./src/readwise_sdk/resources/pets.py">upload_image</a>(pet_id, \*\*<a href="src/readwise_sdk/types/pet_upload_image_params.py">params</a>) -> <a href="./src/readwise_sdk/types/api_response.py">APIResponse</a></code>

# Store

Types:

```python
from readwise_sdk.types import StoreInventoryResponse
```

Methods:

- <code title="get /store/inventory">client.store.<a href="./src/readwise_sdk/resources/store/store.py">inventory</a>() -> <a href="./src/readwise_sdk/types/store_inventory_response.py">StoreInventoryResponse</a></code>

## Orders

Methods:

- <code title="post /store/order">client.store.orders.<a href="./src/readwise_sdk/resources/store/orders.py">create</a>(\*\*<a href="src/readwise_sdk/types/store/order_create_params.py">params</a>) -> <a href="./src/readwise_sdk/types/shared/order.py">Order</a></code>
- <code title="get /store/order/{orderId}">client.store.orders.<a href="./src/readwise_sdk/resources/store/orders.py">retrieve</a>(order_id) -> <a href="./src/readwise_sdk/types/shared/order.py">Order</a></code>
- <code title="delete /store/order/{orderId}">client.store.orders.<a href="./src/readwise_sdk/resources/store/orders.py">delete</a>(order_id) -> None</code>

# User

Types:

```python
from readwise_sdk.types import User, UserLoginResponse
```

Methods:

- <code title="post /user">client.user.<a href="./src/readwise_sdk/resources/user.py">create</a>(\*\*<a href="src/readwise_sdk/types/user_create_params.py">params</a>) -> <a href="./src/readwise_sdk/types/user.py">User</a></code>
- <code title="get /user/{username}">client.user.<a href="./src/readwise_sdk/resources/user.py">retrieve</a>(username) -> <a href="./src/readwise_sdk/types/user.py">User</a></code>
- <code title="put /user/{username}">client.user.<a href="./src/readwise_sdk/resources/user.py">update</a>(existing_username, \*\*<a href="src/readwise_sdk/types/user_update_params.py">params</a>) -> None</code>
- <code title="delete /user/{username}">client.user.<a href="./src/readwise_sdk/resources/user.py">delete</a>(username) -> None</code>
- <code title="post /user/createWithList">client.user.<a href="./src/readwise_sdk/resources/user.py">create_with_list</a>(\*\*<a href="src/readwise_sdk/types/user_create_with_list_params.py">params</a>) -> <a href="./src/readwise_sdk/types/user.py">User</a></code>
- <code title="get /user/login">client.user.<a href="./src/readwise_sdk/resources/user.py">login</a>(\*\*<a href="src/readwise_sdk/types/user_login_params.py">params</a>) -> str</code>
- <code title="get /user/logout">client.user.<a href="./src/readwise_sdk/resources/user.py">logout</a>() -> None</code>
