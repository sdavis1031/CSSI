import jinja2
import webapp2
import os
env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('templates/hello.html')
        self.response.out.write(main_template.render())
    def post(self):
        main_template = env.get_template('templates/kiss.html')
        self.response.out.write(main_template.render())
app = webapp2.WSGIApplication([
  ('/', MainHandler)], debug=True)

    # Be sure to leave the "app=" lines that App Engine launcher created in place
    # below this code.
