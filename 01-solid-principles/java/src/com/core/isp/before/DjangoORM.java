package com.core.isp.before;

public class DjangoORM implements BaseORM{

    @Override
    public void save() {
        System.out.println("DjangoORM: 'save'");
    }

    @Override
    public void update() {
        System.out.println("DjangoORM: 'update'");
    }

    @Override
    public void delete() {
        System.out.println("DjangoORM: 'delete'");
    }

    @Override
    public void commit_or_rollback_transaction() {
        throw new UnsupportedOperationException("Notsupported method 'commit_or_rollback_transaction'");
    }

    @Override
    public void flush() {
        throw new UnsupportedOperationException("Notsupported method 'flush'");
    }
}
