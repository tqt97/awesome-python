from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AU21Pgppr_PgzB_cgRI0eqaQKsuzAzo7KXG2ZuvaYn_SpMVmBXxwvCc_fv-XlqS3CFCcwTZWfPriiF5Y"
        self.client_secret = "EDYXtK_2wWKlJV4xZGHspeGQ3aiCeK2PuZGssuDW14q4SIth3dw19HHQl8KZuM2lTJNYRcS55eFCKm8N"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
