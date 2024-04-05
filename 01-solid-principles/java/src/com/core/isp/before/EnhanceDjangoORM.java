package com.core.isp.before;

public class EnhanceDjangoORM implements BaseORM{

    @Override
    public void save() {
        System.out.println("EnhanceDjangoORM: 'save'");
    }

    @Override
    public void update() {
        System.out.println("EnhanceDjangoORM: 'update'");
    }

    @Override
    public void delete() {
        System.out.println("EnhanceDjangoORM: 'delete'");
    }

    @Override
    public void commit_or_rollback_transaction() {
        System.out.println("EnhanceDjangoORM: 'commit_or_rollback_transaction'");
    }   
    
    @Override
    public void flush() {
        System.out.println("EnhanceDjangoORM: 'flush'");
    }
}
