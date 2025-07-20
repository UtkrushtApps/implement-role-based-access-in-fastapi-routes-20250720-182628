from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.session import get_async_session
from db.models import Employee

router = APIRouter()

@router.get("/", response_model=list[dict])
async def list_employees(session: AsyncSession = Depends(get_async_session)):
    try:
        result = await session.execute(select(Employee))
        employees = result.scalars().all()
        return [
            {"id": emp.id, "name": emp.name, "department": emp.department}
            for emp in employees
        ]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not fetch employees"
        )

@router.get("/{employee_id}", response_model=dict)
async def get_employee(employee_id: int, session: AsyncSession = Depends(get_async_session)):
    emp = await session.get(Employee, employee_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"id": emp.id, "name": emp.name, "department": emp.department}
