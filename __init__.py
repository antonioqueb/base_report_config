def post_init_hook(env):
    env['ir.config_parameter'].sudo().set_param('report.url', 'http://localhost:8069')