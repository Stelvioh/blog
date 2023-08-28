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
    def get_post(post_id):
        post = Post.query.get(post_id)
        return post

    @staticmethod
    def create_post(title, content):
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        return new_post

    @staticmethod
    def update_post(post_id, title, content):
        post = Post.query.get(post_id)
        if post:
            post.title = title
            post.content = content
            db.session.commit()
        return post

    @staticmethod
    def delete_post(post_id):
        post = Post.query.get(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()

