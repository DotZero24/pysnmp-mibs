# SNMP MIB module (FS-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-POE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:08 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsPoeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 110)
)
if mibBuilder.loadTexts:
    fsPoeMIB.setRevisions(
        ("2012-02-14 00:00",
         "2012-02-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsPoeConfigMIBObjects_ObjectIdentity = ObjectIdentity
fsPoeConfigMIBObjects = _FsPoeConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 110, 1)
)
_FsIfPoeTable_Object = MibTable
fsIfPoeTable = _FsIfPoeTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 110, 1, 1)
)
if mibBuilder.loadTexts:
    fsIfPoeTable.setStatus("current")
_FsIfPoeEntry_Object = MibTableRow
fsIfPoeEntry = _FsIfPoeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 110, 1, 1, 1)
)
fsIfPoeEntry.setIndexNames(
    (0, "FS-POE-MIB", "ifPoeIndex"),
)
if mibBuilder.loadTexts:
    fsIfPoeEntry.setStatus("current")


class _IfPoeIndex_Type(Integer32):
    """Custom type ifPoeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IfPoeIndex_Type.__name__ = "Integer32"
_IfPoeIndex_Object = MibTableColumn
ifPoeIndex = _IfPoeIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 110, 1, 1, 1, 1),
    _IfPoeIndex_Type()
)
ifPoeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPoeIndex.setStatus("current")
_IfIsPoe_Type = TruthValue
_IfIsPoe_Object = MibTableColumn
ifIsPoe = _IfIsPoe_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 110, 1, 1, 1, 2),
    _IfIsPoe_Type()
)
ifIsPoe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIsPoe.setStatus("current")


class _IfPoeEnable_Type(Integer32):
    """Custom type ifPoeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IfPoeEnable_Type.__name__ = "Integer32"
_IfPoeEnable_Object = MibTableColumn
ifPoeEnable = _IfPoeEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 110, 1, 1, 1, 3),
    _IfPoeEnable_Type()
)
ifPoeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPoeEnable.setStatus("current")


class _IfPoePwrStatus_Type(Integer32):
    """Custom type ifPoePwrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_IfPoePwrStatus_Type.__name__ = "Integer32"
_IfPoePwrStatus_Object = MibTableColumn
ifPoePwrStatus = _IfPoePwrStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 110, 1, 1, 1, 4),
    _IfPoePwrStatus_Type()
)
ifPoePwrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPoePwrStatus.setStatus("current")


class _IfPoeMaxPwrSet_Type(Integer32):
    """Custom type ifPoeMaxPwrSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IfPoeMaxPwrSet_Type.__name__ = "Integer32"
_IfPoeMaxPwrSet_Object = MibTableColumn
ifPoeMaxPwrSet = _IfPoeMaxPwrSet_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 110, 1, 1, 1, 5),
    _IfPoeMaxPwrSet_Type()
)
ifPoeMaxPwrSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPoeMaxPwrSet.setStatus("current")


class _IfPoePriority_Type(Integer32):
    """Custom type ifPoePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 3))
    )


_IfPoePriority_Type.__name__ = "Integer32"
_IfPoePriority_Object = MibTableColumn
ifPoePriority = _IfPoePriority_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 110, 1, 1, 1, 6),
    _IfPoePriority_Type()
)
ifPoePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPoePriority.setStatus("current")
_IfPoeConsumingPwr_Type = Integer32
_IfPoeConsumingPwr_Object = MibTableColumn
ifPoeConsumingPwr = _IfPoeConsumingPwr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 110, 1, 1, 1, 7),
    _IfPoeConsumingPwr_Type()
)
ifPoeConsumingPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPoeConsumingPwr.setStatus("current")
_IfIsHPoe_Type = TruthValue
_IfIsHPoe_Object = MibTableColumn
ifIsHPoe = _IfIsHPoe_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 110, 1, 1, 1, 8),
    _IfIsHPoe_Type()
)
ifIsHPoe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIsHPoe.setStatus("current")
_FsPoeTraps_ObjectIdentity = ObjectIdentity
fsPoeTraps = _FsPoeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 110, 2)
)

# Managed Objects groups


# Notification objects

ifPoePowerOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 110, 2, 1)
)
ifPoePowerOffTrap.setObjects(
    ("FS-POE-MIB", "ifPoeIndex")
)
if mibBuilder.loadTexts:
    ifPoePowerOffTrap.setStatus(
        "current"
    )

ifPoePowerOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 110, 2, 2)
)
ifPoePowerOnTrap.setObjects(
    ("FS-POE-MIB", "ifPoeIndex")
)
if mibBuilder.loadTexts:
    ifPoePowerOnTrap.setStatus(
        "current"
    )

ifPoePboxAbnormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 110, 2, 3)
)
ifPoePboxAbnormalTrap.setObjects(
    ("FS-POE-MIB", "ifPoeIndex")
)
if mibBuilder.loadTexts:
    ifPoePboxAbnormalTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-POE-MIB",
    **{"fsPoeMIB": fsPoeMIB,
       "fsPoeConfigMIBObjects": fsPoeConfigMIBObjects,
       "fsIfPoeTable": fsIfPoeTable,
       "fsIfPoeEntry": fsIfPoeEntry,
       "ifPoeIndex": ifPoeIndex,
       "ifIsPoe": ifIsPoe,
       "ifPoeEnable": ifPoeEnable,
       "ifPoePwrStatus": ifPoePwrStatus,
       "ifPoeMaxPwrSet": ifPoeMaxPwrSet,
       "ifPoePriority": ifPoePriority,
       "ifPoeConsumingPwr": ifPoeConsumingPwr,
       "ifIsHPoe": ifIsHPoe,
       "fsPoeTraps": fsPoeTraps,
       "ifPoePowerOffTrap": ifPoePowerOffTrap,
       "ifPoePowerOnTrap": ifPoePowerOnTrap,
       "ifPoePboxAbnormalTrap": ifPoePboxAbnormalTrap}
)
