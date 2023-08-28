from domain.post import Post, db
from sqlalchemy_filters import apply_filters, apply_sort
from flask_sqlalchemy import Pagination

class PostRepository:

    @staticmethod
    def get_all(page=1, per_page=10, order_by='id', direction='asc', filters=None) -> Pagination:
        query = db.session.query(Post)

        # Filtragem
        if filters:
            query = apply_filters(query, filters)

        # Ordenação
        if order_by:
            query = apply_sort(query, [{'field': order_by, 'direction': direction}])

        # Paginação
        return query.paginate(page, per_page, error_out=False)
