class DatabaseRouter:

    django_model = ['scraper']

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model.__name__ in self.django_model:
            return "scraper"
        return "default"
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if model_name not in self.django_model:
            return 'default'