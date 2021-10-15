from fastapi import APIRouter

import backend.routers.item as item
import backend.routers.order as order
import backend.routers.order_item as order_item
import backend.routers.extra as extra
import backend.routers.order_item_extra as order_item_extra
import backend.routers.user as user

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
