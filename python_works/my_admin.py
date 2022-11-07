from admin_class import Admin

admin = Admin('Jason', 'Walter', 32)
# admin.greet_user()
# admin.describe_user()
# admin.show_privileges()

admin.describe_user()
admin.privileges.show_privileges()

print("\nAdding privileges...")
admin_privileges = ['can delete post', 'can ban user', 'can add post']

admin.privileges.privileges = admin_privileges
admin.privileges.show_privileges()