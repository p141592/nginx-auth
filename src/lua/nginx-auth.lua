local lib = {
    _VERSION = '0.0.1',
}


local mt = { __index = lib }

function lib.new(_)
    local _r = require "resty.redis"
    local _h = require "resty.http"

    local http = _h.new()

    local redis = _r:new()
    local ok, err = red:connect("127.0.0.1", 6379)
    if not ok then
        return nil, "Redis connect fail"
    end

    return setmetatable({ redis = redis, http = http}, mt)
end

function lib.close(self)
    local redis = self.redis

    if not redis then
        return nil, "not initialized"
    end

    return redis:close()
end

return lib