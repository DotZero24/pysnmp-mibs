# SNMP MIB module (TPT-PORT-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/trendmicro/TPT-PORT-CONFIG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:06:24 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(tpt_tpa_objs,) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-objs")


# MODULE-IDENTITY

tpt_port_config_objs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4)
)
if mibBuilder.loadTexts:
    tpt_port_config_objs.setRevisions(
        ("2016-05-25 18:54",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LineSpeed(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("gigabit", 1),
          ("hundred-megabit", 2),
          ("ten-megabit", 3),
          ("ten-gigabit", 4),
          ("fourty-gigabit", 5))
    )



class DuplexSetting(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("half", 1),
          ("full", 2))
    )



class AutoNegotiation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("on", 1),
          ("off", 2))
    )



class EnabledOrNot(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



class FailoverAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("block", 0),
          ("permit", 1))
    )



class LinkDownMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hub", 0),
          ("breaker", 1),
          ("wire", 2))
    )



# MIB Managed Objects in the order of their OIDs

_PortConfigTable_Object = MibTable
portConfigTable = _PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    portConfigTable.setStatus("current")
_PortConfigEntry_Object = MibTableRow
portConfigEntry = _PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1)
)
portConfigEntry.setIndexNames(
    (0, "TPT-PORT-CONFIG-MIB", "portConfigSlot"),
    (0, "TPT-PORT-CONFIG-MIB", "portConfigPort"),
)
if mibBuilder.loadTexts:
    portConfigEntry.setStatus("current")
_PortConfigSlot_Type = Unsigned32
_PortConfigSlot_Object = MibTableColumn
portConfigSlot = _PortConfigSlot_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 1),
    _PortConfigSlot_Type()
)
portConfigSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigSlot.setStatus("current")
_PortConfigPort_Type = Unsigned32
_PortConfigPort_Object = MibTableColumn
portConfigPort = _PortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 2),
    _PortConfigPort_Type()
)
portConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigPort.setStatus("current")
_PortConfigLineSpeed_Type = LineSpeed
_PortConfigLineSpeed_Object = MibTableColumn
portConfigLineSpeed = _PortConfigLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 3),
    _PortConfigLineSpeed_Type()
)
portConfigLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigLineSpeed.setStatus("current")
_PortConfigDuplex_Type = DuplexSetting
_PortConfigDuplex_Object = MibTableColumn
portConfigDuplex = _PortConfigDuplex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 4),
    _PortConfigDuplex_Type()
)
portConfigDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigDuplex.setStatus("current")
_PortConfigAutoNeg_Type = AutoNegotiation
_PortConfigAutoNeg_Object = MibTableColumn
portConfigAutoNeg = _PortConfigAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 5),
    _PortConfigAutoNeg_Type()
)
portConfigAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigAutoNeg.setStatus("current")
_PortConfigShutdown_Type = EnabledOrNot
_PortConfigShutdown_Object = MibTableColumn
portConfigShutdown = _PortConfigShutdown_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 6),
    _PortConfigShutdown_Type()
)
portConfigShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigShutdown.setStatus("current")
_PortConfigLoopback_Type = EnabledOrNot
_PortConfigLoopback_Object = MibTableColumn
portConfigLoopback = _PortConfigLoopback_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 7),
    _PortConfigLoopback_Type()
)
portConfigLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigLoopback.setStatus("current")
_PortConfigFailover_Type = FailoverAction
_PortConfigFailover_Object = MibTableColumn
portConfigFailover = _PortConfigFailover_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 8),
    _PortConfigFailover_Type()
)
portConfigFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigFailover.setStatus("current")
_PortConfigLDSMode_Type = LinkDownMode
_PortConfigLDSMode_Object = MibTableColumn
portConfigLDSMode = _PortConfigLDSMode_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 9),
    _PortConfigLDSMode_Type()
)
portConfigLDSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigLDSMode.setStatus("current")
_PortConfigLDSTimeout_Type = Unsigned32
_PortConfigLDSTimeout_Object = MibTableColumn
portConfigLDSTimeout = _PortConfigLDSTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 10),
    _PortConfigLDSTimeout_Type()
)
portConfigLDSTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigLDSTimeout.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-PORT-CONFIG-MIB",
    **{"LineSpeed": LineSpeed,
       "DuplexSetting": DuplexSetting,
       "AutoNegotiation": AutoNegotiation,
       "EnabledOrNot": EnabledOrNot,
       "FailoverAction": FailoverAction,
       "LinkDownMode": LinkDownMode,
       "tpt-port-config-objs": tpt_port_config_objs,
       "portConfigTable": portConfigTable,
       "portConfigEntry": portConfigEntry,
       "portConfigSlot": portConfigSlot,
       "portConfigPort": portConfigPort,
       "portConfigLineSpeed": portConfigLineSpeed,
       "portConfigDuplex": portConfigDuplex,
       "portConfigAutoNeg": portConfigAutoNeg,
       "portConfigShutdown": portConfigShutdown,
       "portConfigLoopback": portConfigLoopback,
       "portConfigFailover": portConfigFailover,
       "portConfigLDSMode": portConfigLDSMode,
       "portConfigLDSTimeout": portConfigLDSTimeout}
)
