# SNMP MIB module (H3C-FAILOVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-FAILOVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:21:03 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

h3cFailover = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164)
)
if mibBuilder.loadTexts:
    h3cFailover.setRevisions(
        ("2015-10-27 10:40",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cFailoverScalarObjects_ObjectIdentity = ObjectIdentity
h3cFailoverScalarObjects = _H3cFailoverScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 1)
)
_H3cFailoverMaxNum_Type = Unsigned32
_H3cFailoverMaxNum_Object = MibScalar
h3cFailoverMaxNum = _H3cFailoverMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 1, 1),
    _H3cFailoverMaxNum_Type()
)
h3cFailoverMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFailoverMaxNum.setStatus("current")
_H3cFailoverCurrentNum_Type = Unsigned32
_H3cFailoverCurrentNum_Object = MibScalar
h3cFailoverCurrentNum = _H3cFailoverCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 1, 2),
    _H3cFailoverCurrentNum_Type()
)
h3cFailoverCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFailoverCurrentNum.setStatus("current")
_H3cFailoverTables_ObjectIdentity = ObjectIdentity
h3cFailoverTables = _H3cFailoverTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 2)
)
_H3cFailoverCfgTable_Object = MibTable
h3cFailoverCfgTable = _H3cFailoverCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 2, 1)
)
if mibBuilder.loadTexts:
    h3cFailoverCfgTable.setStatus("current")
_H3cFailoverCfgEntry_Object = MibTableRow
h3cFailoverCfgEntry = _H3cFailoverCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 2, 1, 1)
)
h3cFailoverCfgEntry.setIndexNames(
    (0, "H3C-FAILOVER-MIB", "h3cFailoverIndex"),
)
if mibBuilder.loadTexts:
    h3cFailoverCfgEntry.setStatus("current")


class _H3cFailoverIndex_Type(Unsigned32):
    """Custom type h3cFailoverIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_H3cFailoverIndex_Type.__name__ = "Unsigned32"
_H3cFailoverIndex_Object = MibTableColumn
h3cFailoverIndex = _H3cFailoverIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 2, 1, 1, 1),
    _H3cFailoverIndex_Type()
)
h3cFailoverIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cFailoverIndex.setStatus("current")


class _H3cFailoverName_Type(DisplayString):
    """Custom type h3cFailoverName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_H3cFailoverName_Type.__name__ = "DisplayString"
_H3cFailoverName_Object = MibTableColumn
h3cFailoverName = _H3cFailoverName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 2, 1, 1, 2),
    _H3cFailoverName_Type()
)
h3cFailoverName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFailoverName.setStatus("current")


class _H3cFailoverPrimaryChassisID_Type(Integer32):
    """Custom type h3cFailoverPrimaryChassisID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_H3cFailoverPrimaryChassisID_Type.__name__ = "Integer32"
_H3cFailoverPrimaryChassisID_Object = MibTableColumn
h3cFailoverPrimaryChassisID = _H3cFailoverPrimaryChassisID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 2, 1, 1, 3),
    _H3cFailoverPrimaryChassisID_Type()
)
h3cFailoverPrimaryChassisID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFailoverPrimaryChassisID.setStatus("current")


class _H3cFailoverPrimarySlotID_Type(Integer32):
    """Custom type h3cFailoverPrimarySlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_H3cFailoverPrimarySlotID_Type.__name__ = "Integer32"
_H3cFailoverPrimarySlotID_Object = MibTableColumn
h3cFailoverPrimarySlotID = _H3cFailoverPrimarySlotID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 2, 1, 1, 4),
    _H3cFailoverPrimarySlotID_Type()
)
h3cFailoverPrimarySlotID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFailoverPrimarySlotID.setStatus("current")


class _H3cFailoverPrimaryCpuID_Type(Integer32):
    """Custom type h3cFailoverPrimaryCpuID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_H3cFailoverPrimaryCpuID_Type.__name__ = "Integer32"
_H3cFailoverPrimaryCpuID_Object = MibTableColumn
h3cFailoverPrimaryCpuID = _H3cFailoverPrimaryCpuID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 2, 1, 1, 5),
    _H3cFailoverPrimaryCpuID_Type()
)
h3cFailoverPrimaryCpuID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFailoverPrimaryCpuID.setStatus("current")


class _H3cFailoverSecondaryChassisID_Type(Integer32):
    """Custom type h3cFailoverSecondaryChassisID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_H3cFailoverSecondaryChassisID_Type.__name__ = "Integer32"
_H3cFailoverSecondaryChassisID_Object = MibTableColumn
h3cFailoverSecondaryChassisID = _H3cFailoverSecondaryChassisID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 2, 1, 1, 6),
    _H3cFailoverSecondaryChassisID_Type()
)
h3cFailoverSecondaryChassisID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFailoverSecondaryChassisID.setStatus("current")


class _H3cFailoverSecondarySlotID_Type(Integer32):
    """Custom type h3cFailoverSecondarySlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_H3cFailoverSecondarySlotID_Type.__name__ = "Integer32"
_H3cFailoverSecondarySlotID_Object = MibTableColumn
h3cFailoverSecondarySlotID = _H3cFailoverSecondarySlotID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 2, 1, 1, 7),
    _H3cFailoverSecondarySlotID_Type()
)
h3cFailoverSecondarySlotID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFailoverSecondarySlotID.setStatus("current")


class _H3cFailoverSecondaryCpuID_Type(Integer32):
    """Custom type h3cFailoverSecondaryCpuID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_H3cFailoverSecondaryCpuID_Type.__name__ = "Integer32"
_H3cFailoverSecondaryCpuID_Object = MibTableColumn
h3cFailoverSecondaryCpuID = _H3cFailoverSecondaryCpuID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 2, 1, 1, 8),
    _H3cFailoverSecondaryCpuID_Type()
)
h3cFailoverSecondaryCpuID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFailoverSecondaryCpuID.setStatus("current")


class _H3cFailoverState_Type(Integer32):
    """Custom type h3cFailoverState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("normal", 2),
          ("fault", 3))
    )


_H3cFailoverState_Type.__name__ = "Integer32"
_H3cFailoverState_Object = MibTableColumn
h3cFailoverState = _H3cFailoverState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 2, 1, 1, 9),
    _H3cFailoverState_Type()
)
h3cFailoverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFailoverState.setStatus("current")
_H3cFailoverRowStatus_Type = RowStatus
_H3cFailoverRowStatus_Object = MibTableColumn
h3cFailoverRowStatus = _H3cFailoverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 2, 1, 1, 10),
    _H3cFailoverRowStatus_Type()
)
h3cFailoverRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFailoverRowStatus.setStatus("current")
_H3cFailoverNotification_ObjectIdentity = ObjectIdentity
h3cFailoverNotification = _H3cFailoverNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 3)
)
_H3cFailoverTrap_ObjectIdentity = ObjectIdentity
h3cFailoverTrap = _H3cFailoverTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 3, 0)
)

# Managed Objects groups


# Notification objects

h3cFailoverCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 3, 0, 1)
)
h3cFailoverCreate.setObjects(
      *(("H3C-FAILOVER-MIB", "h3cFailoverIndex"),
        ("H3C-FAILOVER-MIB", "h3cFailoverName"))
)
if mibBuilder.loadTexts:
    h3cFailoverCreate.setStatus(
        "current"
    )

h3cFailoverDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 3, 0, 2)
)
h3cFailoverDelete.setObjects(
      *(("H3C-FAILOVER-MIB", "h3cFailoverIndex"),
        ("H3C-FAILOVER-MIB", "h3cFailoverName"))
)
if mibBuilder.loadTexts:
    h3cFailoverDelete.setStatus(
        "current"
    )

h3cFailoverPrimaryNodeAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 3, 0, 3)
)
h3cFailoverPrimaryNodeAdd.setObjects(
      *(("H3C-FAILOVER-MIB", "h3cFailoverIndex"),
        ("H3C-FAILOVER-MIB", "h3cFailoverName"),
        ("H3C-FAILOVER-MIB", "h3cFailoverPrimaryChassisID"),
        ("H3C-FAILOVER-MIB", "h3cFailoverPrimarySlotID"),
        ("H3C-FAILOVER-MIB", "h3cFailoverPrimaryCpuID"))
)
if mibBuilder.loadTexts:
    h3cFailoverPrimaryNodeAdd.setStatus(
        "current"
    )

h3cFailoverPrimaryNodeRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 3, 0, 4)
)
h3cFailoverPrimaryNodeRemove.setObjects(
      *(("H3C-FAILOVER-MIB", "h3cFailoverIndex"),
        ("H3C-FAILOVER-MIB", "h3cFailoverName"),
        ("H3C-FAILOVER-MIB", "h3cFailoverPrimaryChassisID"),
        ("H3C-FAILOVER-MIB", "h3cFailoverPrimarySlotID"),
        ("H3C-FAILOVER-MIB", "h3cFailoverPrimaryCpuID"))
)
if mibBuilder.loadTexts:
    h3cFailoverPrimaryNodeRemove.setStatus(
        "current"
    )

h3cFailoverSecondaryNodeAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 3, 0, 5)
)
h3cFailoverSecondaryNodeAdd.setObjects(
      *(("H3C-FAILOVER-MIB", "h3cFailoverIndex"),
        ("H3C-FAILOVER-MIB", "h3cFailoverName"),
        ("H3C-FAILOVER-MIB", "h3cFailoverSecondaryChassisID"),
        ("H3C-FAILOVER-MIB", "h3cFailoverSecondarySlotID"),
        ("H3C-FAILOVER-MIB", "h3cFailoverSecondaryCpuID"))
)
if mibBuilder.loadTexts:
    h3cFailoverSecondaryNodeAdd.setStatus(
        "current"
    )

h3cFailoverSecondaryNodeRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 164, 3, 0, 6)
)
h3cFailoverSecondaryNodeRemove.setObjects(
      *(("H3C-FAILOVER-MIB", "h3cFailoverIndex"),
        ("H3C-FAILOVER-MIB", "h3cFailoverName"),
        ("H3C-FAILOVER-MIB", "h3cFailoverSecondaryChassisID"),
        ("H3C-FAILOVER-MIB", "h3cFailoverSecondarySlotID"),
        ("H3C-FAILOVER-MIB", "h3cFailoverSecondaryCpuID"))
)
if mibBuilder.loadTexts:
    h3cFailoverSecondaryNodeRemove.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-FAILOVER-MIB",
    **{"h3cFailover": h3cFailover,
       "h3cFailoverScalarObjects": h3cFailoverScalarObjects,
       "h3cFailoverMaxNum": h3cFailoverMaxNum,
       "h3cFailoverCurrentNum": h3cFailoverCurrentNum,
       "h3cFailoverTables": h3cFailoverTables,
       "h3cFailoverCfgTable": h3cFailoverCfgTable,
       "h3cFailoverCfgEntry": h3cFailoverCfgEntry,
       "h3cFailoverIndex": h3cFailoverIndex,
       "h3cFailoverName": h3cFailoverName,
       "h3cFailoverPrimaryChassisID": h3cFailoverPrimaryChassisID,
       "h3cFailoverPrimarySlotID": h3cFailoverPrimarySlotID,
       "h3cFailoverPrimaryCpuID": h3cFailoverPrimaryCpuID,
       "h3cFailoverSecondaryChassisID": h3cFailoverSecondaryChassisID,
       "h3cFailoverSecondarySlotID": h3cFailoverSecondarySlotID,
       "h3cFailoverSecondaryCpuID": h3cFailoverSecondaryCpuID,
       "h3cFailoverState": h3cFailoverState,
       "h3cFailoverRowStatus": h3cFailoverRowStatus,
       "h3cFailoverNotification": h3cFailoverNotification,
       "h3cFailoverTrap": h3cFailoverTrap,
       "h3cFailoverCreate": h3cFailoverCreate,
       "h3cFailoverDelete": h3cFailoverDelete,
       "h3cFailoverPrimaryNodeAdd": h3cFailoverPrimaryNodeAdd,
       "h3cFailoverPrimaryNodeRemove": h3cFailoverPrimaryNodeRemove,
       "h3cFailoverSecondaryNodeAdd": h3cFailoverSecondaryNodeAdd,
       "h3cFailoverSecondaryNodeRemove": h3cFailoverSecondaryNodeRemove}
)
