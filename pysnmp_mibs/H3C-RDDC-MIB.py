# SNMP MIB module (H3C-RDDC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-RDDC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:47 2025
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

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

h3cRddc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151)
)
if mibBuilder.loadTexts:
    h3cRddc.setRevisions(
        ("2014-01-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cRddcNotifications_ObjectIdentity = ObjectIdentity
h3cRddcNotifications = _H3cRddcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 0)
)
_H3cRddcObjects_ObjectIdentity = ObjectIdentity
h3cRddcObjects = _H3cRddcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1)
)
_H3cRddcInfo_ObjectIdentity = ObjectIdentity
h3cRddcInfo = _H3cRddcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 1)
)
_H3cRddcTable_Object = MibTable
h3cRddcTable = _H3cRddcTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cRddcTable.setStatus("current")
_H3cRddcEntry_Object = MibTableRow
h3cRddcEntry = _H3cRddcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 1, 1, 1)
)
h3cRddcEntry.setIndexNames(
    (0, "H3C-RDDC-MIB", "h3cRddcGroupIdx"),
)
if mibBuilder.loadTexts:
    h3cRddcEntry.setStatus("current")
_H3cRddcGroupIdx_Type = Unsigned32
_H3cRddcGroupIdx_Object = MibTableColumn
h3cRddcGroupIdx = _H3cRddcGroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 1, 1, 1, 1),
    _H3cRddcGroupIdx_Type()
)
h3cRddcGroupIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cRddcGroupIdx.setStatus("current")


class _H3cRddcGroupName_Type(OctetString):
    """Custom type h3cRddcGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_H3cRddcGroupName_Type.__name__ = "OctetString"
_H3cRddcGroupName_Object = MibTableColumn
h3cRddcGroupName = _H3cRddcGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 1, 1, 1, 2),
    _H3cRddcGroupName_Type()
)
h3cRddcGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRddcGroupName.setStatus("current")
_H3cRddcPreempTimeRemain_Type = Unsigned32
_H3cRddcPreempTimeRemain_Object = MibTableColumn
h3cRddcPreempTimeRemain = _H3cRddcPreempTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 1, 1, 1, 3),
    _H3cRddcPreempTimeRemain_Type()
)
h3cRddcPreempTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRddcPreempTimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    h3cRddcPreempTimeRemain.setUnits("minutes")
_H3cRddcPreempTimeConfig_Type = Unsigned32
_H3cRddcPreempTimeConfig_Object = MibTableColumn
h3cRddcPreempTimeConfig = _H3cRddcPreempTimeConfig_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 1, 1, 1, 4),
    _H3cRddcPreempTimeConfig_Type()
)
h3cRddcPreempTimeConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRddcPreempTimeConfig.setStatus("current")
if mibBuilder.loadTexts:
    h3cRddcPreempTimeConfig.setUnits("minutes")
_H3cRddcHoldTimeRemain_Type = Unsigned32
_H3cRddcHoldTimeRemain_Object = MibTableColumn
h3cRddcHoldTimeRemain = _H3cRddcHoldTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 1, 1, 1, 5),
    _H3cRddcHoldTimeRemain_Type()
)
h3cRddcHoldTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRddcHoldTimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    h3cRddcHoldTimeRemain.setUnits("seconds")
_H3cRddcHoldTimeConfig_Type = Unsigned32
_H3cRddcHoldTimeConfig_Object = MibTableColumn
h3cRddcHoldTimeConfig = _H3cRddcHoldTimeConfig_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 1, 1, 1, 6),
    _H3cRddcHoldTimeConfig_Type()
)
h3cRddcHoldTimeConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRddcHoldTimeConfig.setStatus("current")
if mibBuilder.loadTexts:
    h3cRddcHoldTimeConfig.setUnits("seconds")
_H3cRddcNodeTable_Object = MibTable
h3cRddcNodeTable = _H3cRddcNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 1, 2)
)
if mibBuilder.loadTexts:
    h3cRddcNodeTable.setStatus("current")
_H3cRddcNodeEntry_Object = MibTableRow
h3cRddcNodeEntry = _H3cRddcNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 1, 2, 1)
)
h3cRddcNodeEntry.setIndexNames(
    (0, "H3C-RDDC-MIB", "h3cRddcNodeGroupIdx"),
    (0, "H3C-RDDC-MIB", "h3cRddcNodeId"),
)
if mibBuilder.loadTexts:
    h3cRddcNodeEntry.setStatus("current")
_H3cRddcNodeGroupIdx_Type = Unsigned32
_H3cRddcNodeGroupIdx_Object = MibTableColumn
h3cRddcNodeGroupIdx = _H3cRddcNodeGroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 1, 2, 1, 1),
    _H3cRddcNodeGroupIdx_Type()
)
h3cRddcNodeGroupIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRddcNodeGroupIdx.setStatus("current")
_H3cRddcNodeId_Type = Unsigned32
_H3cRddcNodeId_Object = MibTableColumn
h3cRddcNodeId = _H3cRddcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 1, 2, 1, 2),
    _H3cRddcNodeId_Type()
)
h3cRddcNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRddcNodeId.setStatus("current")


class _H3cRddcNodeBindType_Type(Integer32):
    """Custom type h3cRddcNodeBindType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("chassis", 2))
    )


_H3cRddcNodeBindType_Type.__name__ = "Integer32"
_H3cRddcNodeBindType_Object = MibTableColumn
h3cRddcNodeBindType = _H3cRddcNodeBindType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 1, 2, 1, 3),
    _H3cRddcNodeBindType_Type()
)
h3cRddcNodeBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRddcNodeBindType.setStatus("current")
_H3cRddcNodeBindInfo_Type = Unsigned32
_H3cRddcNodeBindInfo_Object = MibTableColumn
h3cRddcNodeBindInfo = _H3cRddcNodeBindInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 1, 2, 1, 4),
    _H3cRddcNodeBindInfo_Type()
)
h3cRddcNodeBindInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRddcNodeBindInfo.setStatus("current")


class _H3cRddcNodePriority_Type(Unsigned32):
    """Custom type h3cRddcNodePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cRddcNodePriority_Type.__name__ = "Unsigned32"
_H3cRddcNodePriority_Object = MibTableColumn
h3cRddcNodePriority = _H3cRddcNodePriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 1, 2, 1, 5),
    _H3cRddcNodePriority_Type()
)
h3cRddcNodePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRddcNodePriority.setStatus("current")
_H3cRddcNodeWeight_Type = Integer32
_H3cRddcNodeWeight_Object = MibTableColumn
h3cRddcNodeWeight = _H3cRddcNodeWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 1, 2, 1, 6),
    _H3cRddcNodeWeight_Type()
)
h3cRddcNodeWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRddcNodeWeight.setStatus("current")


class _H3cRddcNodeStatus_Type(Integer32):
    """Custom type h3cRddcNodeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("master", 2),
          ("standby", 3))
    )


_H3cRddcNodeStatus_Type.__name__ = "Integer32"
_H3cRddcNodeStatus_Object = MibTableColumn
h3cRddcNodeStatus = _H3cRddcNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 1, 2, 1, 7),
    _H3cRddcNodeStatus_Type()
)
h3cRddcNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRddcNodeStatus.setStatus("current")
_H3cRddcTrapObjects_ObjectIdentity = ObjectIdentity
h3cRddcTrapObjects = _H3cRddcTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 2)
)


class _H3cRddcNodeInfo_Type(DisplayString):
    """Custom type h3cRddcNodeInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cRddcNodeInfo_Type.__name__ = "DisplayString"
_H3cRddcNodeInfo_Object = MibScalar
h3cRddcNodeInfo = _H3cRddcNodeInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 2, 1),
    _H3cRddcNodeInfo_Type()
)
h3cRddcNodeInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cRddcNodeInfo.setStatus("current")


class _H3cRddcSwitchReason_Type(DisplayString):
    """Custom type h3cRddcSwitchReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cRddcSwitchReason_Type.__name__ = "DisplayString"
_H3cRddcSwitchReason_Object = MibScalar
h3cRddcSwitchReason = _H3cRddcSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 1, 2, 2),
    _H3cRddcSwitchReason_Type()
)
h3cRddcSwitchReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cRddcSwitchReason.setStatus("current")

# Managed Objects groups


# Notification objects

h3cRddcSwitchoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 0, 1)
)
h3cRddcSwitchoverTrap.setObjects(
      *(("H3C-RDDC-MIB", "h3cRddcGroupIdx"),
        ("H3C-RDDC-MIB", "h3cRddcGroupName"),
        ("H3C-RDDC-MIB", "h3cRddcNodeInfo"),
        ("H3C-RDDC-MIB", "h3cRddcSwitchReason"))
)
if mibBuilder.loadTexts:
    h3cRddcSwitchoverTrap.setStatus(
        "current"
    )

h3cRddcFailIfRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 0, 2)
)
h3cRddcFailIfRecoverTrap.setObjects(
      *(("H3C-RDDC-MIB", "h3cRddcGroupIdx"),
        ("H3C-RDDC-MIB", "h3cRddcGroupName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cRddcFailIfRecoverTrap.setStatus(
        "current"
    )

h3cRddcFailIfGenerateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 151, 0, 3)
)
h3cRddcFailIfGenerateTrap.setObjects(
      *(("H3C-RDDC-MIB", "h3cRddcGroupIdx"),
        ("H3C-RDDC-MIB", "h3cRddcGroupName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cRddcFailIfGenerateTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-RDDC-MIB",
    **{"h3cRddc": h3cRddc,
       "h3cRddcNotifications": h3cRddcNotifications,
       "h3cRddcSwitchoverTrap": h3cRddcSwitchoverTrap,
       "h3cRddcFailIfRecoverTrap": h3cRddcFailIfRecoverTrap,
       "h3cRddcFailIfGenerateTrap": h3cRddcFailIfGenerateTrap,
       "h3cRddcObjects": h3cRddcObjects,
       "h3cRddcInfo": h3cRddcInfo,
       "h3cRddcTable": h3cRddcTable,
       "h3cRddcEntry": h3cRddcEntry,
       "h3cRddcGroupIdx": h3cRddcGroupIdx,
       "h3cRddcGroupName": h3cRddcGroupName,
       "h3cRddcPreempTimeRemain": h3cRddcPreempTimeRemain,
       "h3cRddcPreempTimeConfig": h3cRddcPreempTimeConfig,
       "h3cRddcHoldTimeRemain": h3cRddcHoldTimeRemain,
       "h3cRddcHoldTimeConfig": h3cRddcHoldTimeConfig,
       "h3cRddcNodeTable": h3cRddcNodeTable,
       "h3cRddcNodeEntry": h3cRddcNodeEntry,
       "h3cRddcNodeGroupIdx": h3cRddcNodeGroupIdx,
       "h3cRddcNodeId": h3cRddcNodeId,
       "h3cRddcNodeBindType": h3cRddcNodeBindType,
       "h3cRddcNodeBindInfo": h3cRddcNodeBindInfo,
       "h3cRddcNodePriority": h3cRddcNodePriority,
       "h3cRddcNodeWeight": h3cRddcNodeWeight,
       "h3cRddcNodeStatus": h3cRddcNodeStatus,
       "h3cRddcTrapObjects": h3cRddcTrapObjects,
       "h3cRddcNodeInfo": h3cRddcNodeInfo,
       "h3cRddcSwitchReason": h3cRddcSwitchReason}
)
