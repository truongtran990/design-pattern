package com.core.isp.refactored;

public class DjangoORM implements BaseORM{

    @Override
    public void save() {
        System.out.println("DjangoORM: save");
    }

    @Override
    public void update() {
        System.out.println("DjangoORM: update");
    }

    @Override
    public void delete() {
        System.out.println("DjangoORM: delete");
    }
    
}
