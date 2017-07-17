from flask import render_template, request, Blueprint, jsonify

# define dict to store information collected from VMs and 'error' messages if any
# this dict will be served to AJAX request as response
hello_world_links = {'return_message':'',
              'error':''}

def main(args):
    """
   Simple command-line program for listing the virtual machines on a system.
   """
    resp = dict()
    message = args['message']
    print("My message is: {}".format(message))
    resp['error'] = ""
    resp['return_message'] = message + 'Hello World'

    print(resp)
    return resp

###############
#### FLASK ####
###############

hello_world_bp = Blueprint('hello_world', __name__, template_folder='templates', static_folder='static',
                              static_url_path='/hello_world/static')


@hello_world_bp.route('/hello_world', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('hello_world.html')

    # handle POST method from JQuery (will be filled later)
    elif request.method == 'POST':
        print(request.form)
        hello_world_args = {'message': request.form['message']}
        return_message = main(hello_world_args)
        return jsonify(return_message)