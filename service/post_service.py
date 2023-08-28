from sqlalchemy_filters import apply_filters, apply_sort
from domain.post import Post, db

class PostService:

    @staticmethod
    def get_all_posts(filters=None, order=None, page=1, per_page=10):
        query = db.session.query(Post)

        # Aplica os filtros se fornecidos
        if filters:
            query = apply_filters(query, filters)

        # Aplica a ordenação se fornecida
        if order:
            query = apply_sort(query, order)

        # Paginação
        posts_paginated = query.paginate(page, per_page, error_out=False)
        return {
            'items': [post.to_dict() for post in posts_paginated.items],
            'page': posts_paginated.page,
            'per_page': posts_paginated.per_page,
            'total': posts_paginated.total,
            'pages': posts_paginated.pages
        }
    
    @staticmethod
    def create_post(title, content, author_id):
        post = Post(title=title, content=content, author_id=author_id)
        db.session.add(post)
        db.session.commit()
        return post.to_dict()

    @staticmethod
    def get_post_by_id(post_id):
        post = db.session.query(Post).get(post_id)
        return post.to_dict() if post else None

    @staticmethod
    def update_post(post_id, title=None, content=None):
        post = db.session.query(Post).get(post_id)
        if not post:
            return None
        if title:
            post.title = title
        if content:
            post.content = content
        db.session.commit()
        return post.to_dict()

    @staticmethod
    def delete_post(post_id):
        post = db.session.query(Post).get(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()
            return True
        return False
