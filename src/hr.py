class VersionThree(Models.model):
    name = fields.Char("Name", store=True)

class FeatureOne(Models.model):
    name = fields.Char("Name", store=True)
    email = fields.Char("Email", store=True)
