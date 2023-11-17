class AuthRouter:
    # Database routers provide us of 4 methods

    # we will now describe the applications
    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin'}
    # so we will going to setup 'auth' & 'contenttypes' and other application for this router
    # 'auth' is the apps that django use by default for doing authentication
    # 'admin' is the apps that django use to provide the admin panel
    # and same goes on for other application
    # So if you want admin to be able to access the database in that case we have to provide the 'admin' app here
    # And to go to the admin app we have to provide the 'sessions' as well

    # now we have to describe what database access the have and what operation that they can perform on the database
    def db_for_read(self, model, **hints):
        # so here we are returning the 'users_db' database it means that all the list of application that we describe above on 'route_app_labels' can access 'users_db' database
        # So we are providing access to read 'users_db' database
        if model._meta.app_label in self.route_app_labels:
            # so, here it is checking for the app labels that can access the 'users_db'
            return 'users_db'
        return None

    # Now we will going to define the write method for writing into the database and bellow done the same thing
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

    # now this method allow relations done inside the database
    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    # Method that will allow migrations on the database
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'users_db'
        return None


# Router for 'blue' application database
class Blue:
    route_app_labels = {'blue'}
    # So whenever we will going to migrate this application we don't want tables like 'auth', 'session' etc.. for the 'blue_db' database as well so we will not going to add it inside here
    # So now only the 'blue' application table will going to appear in the 'blue_db' database

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'blue_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'blue_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'blue_db'
        return None
