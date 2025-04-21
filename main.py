from fastapi import FastAPI

from routes.user import user_router
from routes.account import account_router
from routes.transaction import transaction_router
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address


app = FastAPI(title="User_money | Clement Ugwu | ALT/SOE/024/0106",
    description="Backend Python Third Semester Final_Assignment",)

limiter = Limiter(key_func=get_remote_address)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(user_router, tags=["user"])
app.include_router(account_router, prefix="/accounts", tags=["account"])
app.include_router(transaction_router, prefix="/transactions", tags=["transaction"])

@app.get('/')
def home():
    return {"message": "welcome to Clement Ugwu User_Money"}
