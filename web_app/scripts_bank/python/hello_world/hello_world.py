from flask import render_template, request, Blueprint, jsonify

# define dict to store information collected from VMs and 'error' messages if any
# this dict will be served to AJAX request as response
hello_world_links = {'return_messge':'Hello World',
              'error':''}

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

        global vmrc_links
        vmrc_links = {'collected_vm_info': '',
                      'error': ''}

        # TODO: RD: add connection timeout for vm engine. Its too long in case of netw unreach.
        vm_info = main(getvmrc_args)
        return jsonify(vm_info)