package com.core.isp.refactored;

public class EnhanceDjangoORM implements BaseORM, SQLAlchemy{

    @Override
    public void commit_or_rollback_transaction() {
        System.out.println("EnhanceDjangoORM: commit_or_rollback_transaction proposal feature");
    }

    @Override
    public void save() {
        System.out.println("EnhanceDjangoORM: save");
    }

    @Override
    public void update() {
        System.out.println("EnhanceDjangoORM: update");
    }

    @Override
    public void delete() {
        System.out.println("EnhanceDjangoORM: delete");
    }

    @Override
    public void flush() {
        System.out.println("EnhanceDjangoORM: flush proposal feature");
    }
    
}
