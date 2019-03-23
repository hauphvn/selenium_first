"""
@Hau
Learn the code below of 03 testcase, especially the 3rd one, which try to buy a flip product
Use it for your reference

Your task: Write selenium script to buy a flip product
"""

class TestVenta(unittest.TestCase):

    def setUp(self):
        self.addCleanup(wd.quit) #ref. https://pypi.org/project/selenium/#example-2 https://stackoverflow.com/a/37534071/248616

    #def tearDown(self):
    #    wd.quit() #has been done via addCleanup() so dont need here

    def test_homepage(self):
        url = 'https://release.gigacover.com'
        wd.get(url)
        title = wd.title
        assert title=='Insurance for Freelancers'


    def test_flip_homepage(self):
        url = 'https://release.gigacover.com/flip'
        wd.get(url)
        x  = '//*[@id="gigacover-landing"]/div[2]/div[1]/h1/label[1]'
        e1 = wait4VisibleXPath(wd, x); takeSnapshot(wd, printOutcome=True, suffix='flip homepage header')
        x  = '//*[@id="gigacover-landing"]/div[2]/div[1]/h1/label[2]'
        e2 = wait4VisibleXPath(wd, x); takeSnapshot(wd, printOutcome=True, suffix='flip homepage header')
        header = '%s %s' % (e1.text, e2.text)
        assert header=='Get paid when you are unable to work due to illness or injury.'


    """
    ETE Test #1 - buying a FLIP policy

    steps
    1) Visit https://release.gigacover.com/flip

    2) Key in
    dob
    occupation (class 2)
    policy start

    3) Check that live quote gives correct prices - defined in $ATLAS/atlas/models/incomemax/pricing.py or here.
    4) Pick the weekly extreme plan ie. "Weekly" frequency and "Extreme" plan at $800 weekly payout.
    5) Pay with credit card, using this test card from Stripe:
       4242 4242 4242 4242  Visa

    6) Check that customer is correctly redirected back to success page (Venta).

    7) Check backend
       policy is created
       bill is created
       transaction is created
       new customer email is sent to developers@
    """
    def test_buy_flip_basic(self):
        url = 'https://release.gigacover.com/flip'
        #TODO update this testcase since Venta get changed eg. dob form was moved into the popup
        wd.get(url); takeSnapshot(wd, printOutcome=True, suffix='homepage')

        ######################################INFO#################################################################################################

        #customer's input recorded here
        customer_input = dict()

        #plan info
        dob                             = date(1984, 9, 4)
        policy_start                    = date.today() + timedelta(days=6) #must be between (inclusive) today+5days and today+1month-1day
        customer_input['plan']          = 'premium' #basic/enchanced/premium
        customer_input['unit']          = 'weekly'  #weekly/monthly/yearly
        occupations                     = [7]       #indices of occupations according to get quote page
        additional_info                 = [1,3]     #indices of "tell us more about yourself" according to get quote page

        #personal info
        customer_input['first_name']    = 'Nam+%s' % Some.string()
        customer_input['last_name']     = 'VU+%s' % Some.string()
        customer_input['nric']          = 'S8224793I'
        customer_input['postalcode']    = '{0:06d}'.format(Some.number(min=1,max=999999))
        customer_input['email']         = 'namgivu@autoarmour.co' #TODO change Venta code to allow email in the form of namgivu+122333@gmail.com
        customer_input['mobile']        = str(randint(80000000,99999999)) #TODO should mobile be recorded in customer input?

        #payment info
        payment_info = collections.OrderedDict() #ordered because zipcode must be filled last
        payment_info['card_number']     = '4242424242424242'
        MM                              = 12
        YY                              = datetime.now().year+Some.number(max=10)
        payment_info['expire']          = '%s/%s' % (MM, YY)
        payment_info['cvc']             = 122
        payment_info['zipcode']         = 344


        ''' why doesn't this randomly generated nric pass the nric check?
        random_seven = '{0:07d}'.format(Some.number(min=1,max=9999999))
        checksum = int(random_seven[0])*2 + int(random_seven[1])*7 + int(random_seven[2])*6 + int(random_seven[3])*5 + int(random_seven[4])*4 + int(random_seven[5])*3 + int(random_seven[6])*2
        checksum = checksum % 11
        alphabet_dict = {0:'J', 1:'Z', 2:'I', 3:'H', 4:'G', 5:'F', 6:'E', 7:'D', 8:'C', 9:'B', 10:'A'}
        customer_input['nric']          = 'S' + '{0:07d}'.format(Some.number(min=1,max=9999999)) + alphabet_dict[checksum]
        '''

        ######################################GET QUOTE#################################################################################################

        get_quote_button = wait4VisibleCSS(wd, 'button#headless-get-quote-button')
        click(wd, get_quote_button)
        #set birthday and return final birthday in textbox
        customer_input['dob'] = selectBirthday(wd, dob)
        #set policy_start and return final policy_start in textbox
        customer_input['policy_start'] =  selectPolicyStart(wd, policy_start)
        #TODO click livequote next/submit button --> must see 'occupation required' error ref. https://autoarmour.atlassian.net/browse/UBI-689?focusedCommentId=10709&page=com.atlassian.jira.plugin.system.issuetabpanels%3Acomment-tabpanel#comment-10709
        #select jobs
        jobs = selectOccupations(wd, occupations)
        customer_input['occupation'] = ",".join(list(map(lambda job: to_atlas_job(occupation_text=job), jobs)))
        #check additional information checkboxes
        selectDetails(wd, additional_info)
        #submit
        live_quote_submit = wait4VisibleCSS(wd, 'button#headless-show-quote-button')
        click(wd, live_quote_submit)

        #TODO put in multiple occupation testcase here

        ######################################SELECT PLAN#################################################################################################

        x = "//h2[.='Freelancer income protection insurance']"
        _ = wait4VisibleXPath(wd, x); takeSnapshot(wd, printOutcome=True, suffix='plan options')
        #select plan
        selectPlan(wd, customer_input['plan'])
        #select unit
        selectUnit(wd, customer_input['unit'])
        #check declare box and click proceed button
        selectDeclareProceed(wd)

        #TODO ensure livequote gives correct prices

        ######################################PERSONAL INFO#################################################################################################

        #fill in personal info in customer_input
        fillPersonalInfo(wd, customer_input)
        #check confirm checkbox
        x = "//input[@id='headless-checkbox-confirm-info']/following-sibling::div/div"
        confirm_info = wait4VisibleXPath(wd, x)
        click(wd, confirm_info)
        #check required checkbox
        x = "//input[@id='headless-checkbox-required']/following-sibling::div/div"
        required = wait4VisibleXPath(wd,x)
        click(wd, required); takeSnapshot(wd, printOutcome=True, suffix='checked boxes')
        #press checkout button
        x = "//span[.= 'Checkout now']"
        checkout = wait4VisibleXPath(wd, x)
        click(wd, checkout)


        ######################################PAYMENT#################################################################################################

        takeSnapshot(wd, printOutcome=True, suffix='payment page')
        #click pay button to open stripe menu
        x = "//span[.='Proceed to Pay by card']"
        proceed = wait4VisibleXPath(wd, x)
        click(wd, proceed)
        #fill up card details, retrieve premiums and click pay
        customer_input['premiums'] = fillCardInfo(wd, payment_info)

        ######################################POST PROCESSING/CHECKOUT PAGE#################################################################################################

        customer_input = {
            'underwriting': customer_input,
            'payment': {
                'stripe': {
                    'type': 'credit', #TODO get credit|debit correctly from stripe iframe
                },
            }
        }

        header3 = x="//*[.='Checkout']"
        header3 = wait4VisibleXPath(wd, x)
        time.sleep(2); takeSnapshot(wd, printOutcome=True, suffix='checked out')
        time.sleep(5); takeSnapshot(wd, printOutcome=True, suffix='thank you page')
        #TODO verify other details on thank-you page; currently we have bug ref. https://autoarmour.atlassian.net/browse/UBI-689?focusedCommentId=10708&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-10708

        ######################################BACKEND#################################################################################################
        l(''); l('customer_input=%s' % customer_input)

        #ensure host working + logged in
        ensure_host_responding()
        auth_token, auth_user = auth_login()

        # #TODO ensure atlas's policy+settings created correctly
        # #TODO ensure atlas's user created correctly
        # #TODO ensure atlas's bill+transaction created correctly
        # r, ec = request(method='GET', host=ATLAS_HOST, action='/v2/payments/generate_test_token')
        # assert ec == 200, translate(ec)
        # assert r and 'token' in r
        # token = r['token']

        ##endregion check backend
