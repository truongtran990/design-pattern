package com.core.isp.refactored;

public interface SQLAlchemy {
    public void commit_or_rollback_transaction();
    public void flush();
}
