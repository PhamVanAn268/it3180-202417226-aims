# AIMS-mini: use cases

```mermaid
flowchart LR
    Customer[Customer]
    Add([Add DVD to cart])
    Remove([Remove DVD from cart])
    View([View cart and total])
    Search([Search DVDs by title])
    Customer --> Add
    Customer --> Remove
    Customer --> View
    Customer --> Search
```

The cart contains DVDs. Adding/removing updates the cart; viewing lists its contents and total. Title search returns matching DVDs from a supplied collection. Checkout, payment, accounts and persistence are outside this demonstration.
