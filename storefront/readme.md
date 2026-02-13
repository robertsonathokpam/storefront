# Storefront Backend Architecture

A scalable e-commerce backend designed to handle complex product relationships, inventory management, and order processing.

## Key Design Decisions
- **Data Integrity:** Used `PROTECT` on foreign keys to prevent accidental deletion of order history.
- **Optimization:** Designed `Collection` and `Product` with efficient indexing for fast retrieval.
- **Scalability:** Separated `Customer` profile from `User` auth model for flexibility.

## Data Model
- **Products & Collections:** One-to-Many relationship with circular dependency handling.
- **Orders & Cart:** Implemented standard e-commerce flow (Cart -> Order -> Payment).