# SNMP MIB module (ELTEX-ULD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-ULD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:49:16 2025
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltexULDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 34)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltexULDNotifications_ObjectIdentity = ObjectIdentity
eltexULDNotifications = _EltexULDNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 34, 0)
)
_EltexULDMgmt_ObjectIdentity = ObjectIdentity
eltexULDMgmt = _EltexULDMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 34, 1)
)
_EltexULDTable_Object = MibTable
eltexULDTable = _EltexULDTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 34, 1, 1)
)
if mibBuilder.loadTexts:
    eltexULDTable.setStatus("current")
_EltexULDEntry_Object = MibTableRow
eltexULDEntry = _EltexULDEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1)
)
eltexULDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltexULDEntry.setStatus("current")


class _EltexULDAdminState_Type(Integer32):
    """Custom type eltexULDAdminState based on Integer32"""
    defaultValue = 2

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


_EltexULDAdminState_Type.__name__ = "Integer32"
_EltexULDAdminState_Object = MibTableColumn
eltexULDAdminState = _EltexULDAdminState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1, 1),
    _EltexULDAdminState_Type()
)
eltexULDAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexULDAdminState.setStatus("current")


class _EltexULDOperStatus_Type(Integer32):
    """Custom type eltexULDOperStatus based on Integer32"""
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


_EltexULDOperStatus_Type.__name__ = "Integer32"
_EltexULDOperStatus_Object = MibTableColumn
eltexULDOperStatus = _EltexULDOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1, 2),
    _EltexULDOperStatus_Type()
)
eltexULDOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexULDOperStatus.setStatus("current")


class _EltexULDMode_Type(Integer32):
    """Custom type eltexULDMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("err-disable", 2))
    )


_EltexULDMode_Type.__name__ = "Integer32"
_EltexULDMode_Object = MibTableColumn
eltexULDMode = _EltexULDMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1, 3),
    _EltexULDMode_Type()
)
eltexULDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexULDMode.setStatus("current")


class _EltexULDDiscoveryTime_Type(Integer32):
    """Custom type eltexULDDiscoveryTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_EltexULDDiscoveryTime_Type.__name__ = "Integer32"
_EltexULDDiscoveryTime_Object = MibTableColumn
eltexULDDiscoveryTime = _EltexULDDiscoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1, 4),
    _EltexULDDiscoveryTime_Type()
)
eltexULDDiscoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexULDDiscoveryTime.setStatus("current")


class _EltexULDIsAggressive_Type(TruthValue):
    """Custom type eltexULDIsAggressive based on TruthValue"""
    defaultValue = 2


_EltexULDIsAggressive_Type.__name__ = "TruthValue"
_EltexULDIsAggressive_Object = MibTableColumn
eltexULDIsAggressive = _EltexULDIsAggressive_Object(
    (1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1, 5),
    _EltexULDIsAggressive_Type()
)
eltexULDIsAggressive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexULDIsAggressive.setStatus("current")


class _EltexULDLinkStatus_Type(Integer32):
    """Custom type eltexULDLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("unidirectional", 2),
          ("bidirectional", 3),
          ("tx-rx-loop", 4),
          ("neighbor-mismatch", 5))
    )


_EltexULDLinkStatus_Type.__name__ = "Integer32"
_EltexULDLinkStatus_Object = MibTableColumn
eltexULDLinkStatus = _EltexULDLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1, 6),
    _EltexULDLinkStatus_Type()
)
eltexULDLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexULDLinkStatus.setStatus("current")

# Managed Objects groups


# Notification objects

eltexULDLinkStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 34, 0, 1)
)
eltexULDLinkStatusChanged.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ELTEX-ULD-MIB", "eltexULDLinkStatus"))
)
if mibBuilder.loadTexts:
    eltexULDLinkStatusChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-ULD-MIB",
    **{"eltexULDMIB": eltexULDMIB,
       "eltexULDNotifications": eltexULDNotifications,
       "eltexULDLinkStatusChanged": eltexULDLinkStatusChanged,
       "eltexULDMgmt": eltexULDMgmt,
       "eltexULDTable": eltexULDTable,
       "eltexULDEntry": eltexULDEntry,
       "eltexULDAdminState": eltexULDAdminState,
       "eltexULDOperStatus": eltexULDOperStatus,
       "eltexULDMode": eltexULDMode,
       "eltexULDDiscoveryTime": eltexULDDiscoveryTime,
       "eltexULDIsAggressive": eltexULDIsAggressive,
       "eltexULDLinkStatus": eltexULDLinkStatus}
)
