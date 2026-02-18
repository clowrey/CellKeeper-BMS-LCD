import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import switch
from esphome.const import CONF_ID

from . import hmi_bms_ns, HMIBMS

DEPENDENCIES = ["hmi_bms"]

HMIBMSLogSwitch = hmi_bms_ns.class_("HMIBMSLogSwitch", switch.Switch)

CONF_LOG_ENABLE = "log_enable"

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.use_id(HMIBMS),
    cv.Optional(CONF_LOG_ENABLE): switch.switch_schema(HMIBMSLogSwitch),
})

async def to_code(config):
    parent = await cg.get_variable(config[CONF_ID])
    if CONF_LOG_ENABLE in config:
        sw = await switch.new_switch(config[CONF_LOG_ENABLE])
        cg.add(sw.set_parent(parent))
        cg.add(parent.set_log_enable_switch(sw))
