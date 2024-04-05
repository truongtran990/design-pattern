package com.core.isp.before;

public interface BaseORM {
    public void save();
    public void update();
    public void delete();
    public void commit_or_rollback_transaction();
    public void flush();
}
