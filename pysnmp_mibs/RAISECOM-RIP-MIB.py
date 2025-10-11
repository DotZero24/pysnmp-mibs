# SNMP MIB module (RAISECOM-RIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-RIP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:43 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcRip = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17)
)
if mibBuilder.loadTexts:
    rcRip.setRevisions(
        ("1904-12-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcRipConfig_ObjectIdentity = ObjectIdentity
rcRipConfig = _RcRipConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 1)
)


class _RcRip2GlobalEnable_Type(EnableVar):
    """Custom type rcRip2GlobalEnable based on EnableVar"""
    defaultValue = 2


_RcRip2GlobalEnable_Type.__name__ = "EnableVar"
_RcRip2GlobalEnable_Object = MibScalar
rcRip2GlobalEnable = _RcRip2GlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 1, 1),
    _RcRip2GlobalEnable_Type()
)
rcRip2GlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRip2GlobalEnable.setStatus("current")
_RcRip2GlobalPassive_Type = TruthValue
_RcRip2GlobalPassive_Object = MibScalar
rcRip2GlobalPassive = _RcRip2GlobalPassive_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 1, 2),
    _RcRip2GlobalPassive_Type()
)
rcRip2GlobalPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRip2GlobalPassive.setStatus("current")


class _RcRip2UpdateTime_Type(Integer32):
    """Custom type rcRip2UpdateTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 500),
    )


_RcRip2UpdateTime_Type.__name__ = "Integer32"
_RcRip2UpdateTime_Object = MibScalar
rcRip2UpdateTime = _RcRip2UpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 1, 3),
    _RcRip2UpdateTime_Type()
)
rcRip2UpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRip2UpdateTime.setStatus("current")


class _RcRip2ExpireTime_Type(Integer32):
    """Custom type rcRip2ExpireTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 180),
    )


_RcRip2ExpireTime_Type.__name__ = "Integer32"
_RcRip2ExpireTime_Object = MibScalar
rcRip2ExpireTime = _RcRip2ExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 1, 4),
    _RcRip2ExpireTime_Type()
)
rcRip2ExpireTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRip2ExpireTime.setStatus("current")


class _RcRip2FlushTime_Type(Integer32):
    """Custom type rcRip2FlushTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 500),
    )


_RcRip2FlushTime_Type.__name__ = "Integer32"
_RcRip2FlushTime_Object = MibScalar
rcRip2FlushTime = _RcRip2FlushTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 1, 5),
    _RcRip2FlushTime_Type()
)
rcRip2FlushTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRip2FlushTime.setStatus("current")


class _RcRip2Distance_Type(Integer32):
    """Custom type rcRip2Distance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RcRip2Distance_Type.__name__ = "Integer32"
_RcRip2Distance_Object = MibScalar
rcRip2Distance = _RcRip2Distance_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 1, 6),
    _RcRip2Distance_Type()
)
rcRip2Distance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRip2Distance.setStatus("current")
_RcRipIfConfig_ObjectIdentity = ObjectIdentity
rcRipIfConfig = _RcRipIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 2)
)
_RcRip2IfConfigTable_Object = MibTable
rcRip2IfConfigTable = _RcRip2IfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 2, 1)
)
if mibBuilder.loadTexts:
    rcRip2IfConfigTable.setStatus("current")
_RcRip2IfConfigEntry_Object = MibTableRow
rcRip2IfConfigEntry = _RcRip2IfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 2, 1, 1)
)
rcRip2IfConfigEntry.setIndexNames(
    (0, "RAISECOM-RIP-MIB", "rcRip2IfConfigAddress"),
)
if mibBuilder.loadTexts:
    rcRip2IfConfigEntry.setStatus("current")
_RcRip2IfConfigAddress_Type = IpAddress
_RcRip2IfConfigAddress_Object = MibTableColumn
rcRip2IfConfigAddress = _RcRip2IfConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 2, 1, 1, 1),
    _RcRip2IfConfigAddress_Type()
)
rcRip2IfConfigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRip2IfConfigAddress.setStatus("current")
_RcRip2IfConfigSplit_Type = TruthValue
_RcRip2IfConfigSplit_Object = MibTableColumn
rcRip2IfConfigSplit = _RcRip2IfConfigSplit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 2, 1, 1, 2),
    _RcRip2IfConfigSplit_Type()
)
rcRip2IfConfigSplit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRip2IfConfigSplit.setStatus("current")
_RcRip2IfConfigRowStatus_Type = RowStatus
_RcRip2IfConfigRowStatus_Object = MibTableColumn
rcRip2IfConfigRowStatus = _RcRip2IfConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 2, 1, 1, 3),
    _RcRip2IfConfigRowStatus_Type()
)
rcRip2IfConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRip2IfConfigRowStatus.setStatus("current")
_RcRipNetConfig_ObjectIdentity = ObjectIdentity
rcRipNetConfig = _RcRipNetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 3)
)
_RcRip2NetConfigTable_Object = MibTable
rcRip2NetConfigTable = _RcRip2NetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 3, 1)
)
if mibBuilder.loadTexts:
    rcRip2NetConfigTable.setStatus("current")
_RcRip2NetConfigEntry_Object = MibTableRow
rcRip2NetConfigEntry = _RcRip2NetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 3, 1, 1)
)
rcRip2NetConfigEntry.setIndexNames(
    (0, "RAISECOM-RIP-MIB", "rcRip2NetConfigSubnet"),
    (0, "RAISECOM-RIP-MIB", "rcRip2NetConfigMask"),
)
if mibBuilder.loadTexts:
    rcRip2NetConfigEntry.setStatus("current")
_RcRip2NetConfigSubnet_Type = IpAddress
_RcRip2NetConfigSubnet_Object = MibTableColumn
rcRip2NetConfigSubnet = _RcRip2NetConfigSubnet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 3, 1, 1, 1),
    _RcRip2NetConfigSubnet_Type()
)
rcRip2NetConfigSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRip2NetConfigSubnet.setStatus("current")
_RcRip2NetConfigMask_Type = IpAddress
_RcRip2NetConfigMask_Object = MibTableColumn
rcRip2NetConfigMask = _RcRip2NetConfigMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 3, 1, 1, 2),
    _RcRip2NetConfigMask_Type()
)
rcRip2NetConfigMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRip2NetConfigMask.setStatus("current")
_RcRip2NetConfigRowStatus_Type = RowStatus
_RcRip2NetConfigRowStatus_Object = MibTableColumn
rcRip2NetConfigRowStatus = _RcRip2NetConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 17, 3, 1, 1, 3),
    _RcRip2NetConfigRowStatus_Type()
)
rcRip2NetConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRip2NetConfigRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-RIP-MIB",
    **{"rcRip": rcRip,
       "rcRipConfig": rcRipConfig,
       "rcRip2GlobalEnable": rcRip2GlobalEnable,
       "rcRip2GlobalPassive": rcRip2GlobalPassive,
       "rcRip2UpdateTime": rcRip2UpdateTime,
       "rcRip2ExpireTime": rcRip2ExpireTime,
       "rcRip2FlushTime": rcRip2FlushTime,
       "rcRip2Distance": rcRip2Distance,
       "rcRipIfConfig": rcRipIfConfig,
       "rcRip2IfConfigTable": rcRip2IfConfigTable,
       "rcRip2IfConfigEntry": rcRip2IfConfigEntry,
       "rcRip2IfConfigAddress": rcRip2IfConfigAddress,
       "rcRip2IfConfigSplit": rcRip2IfConfigSplit,
       "rcRip2IfConfigRowStatus": rcRip2IfConfigRowStatus,
       "rcRipNetConfig": rcRipNetConfig,
       "rcRip2NetConfigTable": rcRip2NetConfigTable,
       "rcRip2NetConfigEntry": rcRip2NetConfigEntry,
       "rcRip2NetConfigSubnet": rcRip2NetConfigSubnet,
       "rcRip2NetConfigMask": rcRip2NetConfigMask,
       "rcRip2NetConfigRowStatus": rcRip2NetConfigRowStatus}
)
