from fastapi import APIRouter

import application.routers.item as item
import application.routers.order as order
import application.routers.order_item as order_item
import application.routers.extra as extra
import application.routers.order_item_extra as order_item_extra
import application.routers.user as user

router = APIRouter(
    prefix="",
    responses={404: {"description": "Not found"}},
)


router.include_router(order.router)
router.include_router(item.router)
router.include_router(order_item.router)
router.include_router(extra.router)
router.include_router(order_item_extra.router)
router.include_router(user.router)
