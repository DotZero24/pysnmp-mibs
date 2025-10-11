# SNMP MIB module (H3C-SMLK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-SMLK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:33 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

h3cSmlk = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147)
)
if mibBuilder.loadTexts:
    h3cSmlk.setRevisions(
        ("2014-07-23 15:03",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cSmlkObject_ObjectIdentity = ObjectIdentity
h3cSmlkObject = _H3cSmlkObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1)
)
_H3cSmlkGroupTable_Object = MibTable
h3cSmlkGroupTable = _H3cSmlkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 1)
)
if mibBuilder.loadTexts:
    h3cSmlkGroupTable.setStatus("current")
_H3cSmlkGroupEntry_Object = MibTableRow
h3cSmlkGroupEntry = _H3cSmlkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 1, 1)
)
h3cSmlkGroupEntry.setIndexNames(
    (0, "H3C-SMLK-MIB", "h3cSmlkGroupID"),
)
if mibBuilder.loadTexts:
    h3cSmlkGroupEntry.setStatus("current")


class _H3cSmlkGroupID_Type(Integer32):
    """Custom type h3cSmlkGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_H3cSmlkGroupID_Type.__name__ = "Integer32"
_H3cSmlkGroupID_Object = MibTableColumn
h3cSmlkGroupID = _H3cSmlkGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 1, 1, 1),
    _H3cSmlkGroupID_Type()
)
h3cSmlkGroupID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSmlkGroupID.setStatus("current")
_H3cSmlkDeviceID_Type = MacAddress
_H3cSmlkDeviceID_Object = MibTableColumn
h3cSmlkDeviceID = _H3cSmlkDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 1, 1, 2),
    _H3cSmlkDeviceID_Type()
)
h3cSmlkDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSmlkDeviceID.setStatus("current")


class _H3cSmlkPreemptionMode_Type(Integer32):
    """Custom type h3cSmlkPreemptionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("role", 2),
          ("speed", 3))
    )


_H3cSmlkPreemptionMode_Type.__name__ = "Integer32"
_H3cSmlkPreemptionMode_Object = MibTableColumn
h3cSmlkPreemptionMode = _H3cSmlkPreemptionMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 1, 1, 3),
    _H3cSmlkPreemptionMode_Type()
)
h3cSmlkPreemptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSmlkPreemptionMode.setStatus("current")


class _H3cSmlkSpeedThreshold_Type(Integer32):
    """Custom type h3cSmlkSpeedThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_H3cSmlkSpeedThreshold_Type.__name__ = "Integer32"
_H3cSmlkSpeedThreshold_Object = MibTableColumn
h3cSmlkSpeedThreshold = _H3cSmlkSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 1, 1, 4),
    _H3cSmlkSpeedThreshold_Type()
)
h3cSmlkSpeedThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSmlkSpeedThreshold.setStatus("current")


class _H3cSmlkPreemptionDelay_Type(Integer32):
    """Custom type h3cSmlkPreemptionDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_H3cSmlkPreemptionDelay_Type.__name__ = "Integer32"
_H3cSmlkPreemptionDelay_Object = MibTableColumn
h3cSmlkPreemptionDelay = _H3cSmlkPreemptionDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 1, 1, 5),
    _H3cSmlkPreemptionDelay_Type()
)
h3cSmlkPreemptionDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSmlkPreemptionDelay.setStatus("current")


class _H3cSmlkControlVlanID_Type(Integer32):
    """Custom type h3cSmlkControlVlanID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_H3cSmlkControlVlanID_Type.__name__ = "Integer32"
_H3cSmlkControlVlanID_Object = MibTableColumn
h3cSmlkControlVlanID = _H3cSmlkControlVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 1, 1, 6),
    _H3cSmlkControlVlanID_Type()
)
h3cSmlkControlVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSmlkControlVlanID.setStatus("current")


class _H3cSmlkInstanceListLow_Type(OctetString):
    """Custom type h3cSmlkInstanceListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )
    fixed_length = 256


_H3cSmlkInstanceListLow_Type.__name__ = "OctetString"
_H3cSmlkInstanceListLow_Object = MibTableColumn
h3cSmlkInstanceListLow = _H3cSmlkInstanceListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 1, 1, 7),
    _H3cSmlkInstanceListLow_Type()
)
h3cSmlkInstanceListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSmlkInstanceListLow.setStatus("current")


class _H3cSmlkInstanceListHigh_Type(OctetString):
    """Custom type h3cSmlkInstanceListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )
    fixed_length = 256


_H3cSmlkInstanceListHigh_Type.__name__ = "OctetString"
_H3cSmlkInstanceListHigh_Object = MibTableColumn
h3cSmlkInstanceListHigh = _H3cSmlkInstanceListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 1, 1, 8),
    _H3cSmlkInstanceListHigh_Type()
)
h3cSmlkInstanceListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSmlkInstanceListHigh.setStatus("current")
_H3cSmlkGroupRowStatus_Type = RowStatus
_H3cSmlkGroupRowStatus_Object = MibTableColumn
h3cSmlkGroupRowStatus = _H3cSmlkGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 1, 1, 9),
    _H3cSmlkGroupRowStatus_Type()
)
h3cSmlkGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSmlkGroupRowStatus.setStatus("current")
_H3cSmlkPortTable_Object = MibTable
h3cSmlkPortTable = _H3cSmlkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 2)
)
if mibBuilder.loadTexts:
    h3cSmlkPortTable.setStatus("current")
_H3cSmlkPortEntry_Object = MibTableRow
h3cSmlkPortEntry = _H3cSmlkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 2, 1)
)
h3cSmlkPortEntry.setIndexNames(
    (0, "H3C-SMLK-MIB", "h3cSmlkGroupID"),
    (0, "H3C-SMLK-MIB", "h3cSmlkPortIfIndex"),
)
if mibBuilder.loadTexts:
    h3cSmlkPortEntry.setStatus("current")
_H3cSmlkPortIfIndex_Type = InterfaceIndex
_H3cSmlkPortIfIndex_Object = MibTableColumn
h3cSmlkPortIfIndex = _H3cSmlkPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 2, 1, 1),
    _H3cSmlkPortIfIndex_Type()
)
h3cSmlkPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSmlkPortIfIndex.setStatus("current")


class _H3cSmlkPortRole_Type(Integer32):
    """Custom type h3cSmlkPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_H3cSmlkPortRole_Type.__name__ = "Integer32"
_H3cSmlkPortRole_Object = MibTableColumn
h3cSmlkPortRole = _H3cSmlkPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 2, 1, 2),
    _H3cSmlkPortRole_Type()
)
h3cSmlkPortRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSmlkPortRole.setStatus("current")


class _H3cSmlkPortStatus_Type(Integer32):
    """Custom type h3cSmlkPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("active", 2),
          ("standby", 3))
    )


_H3cSmlkPortStatus_Type.__name__ = "Integer32"
_H3cSmlkPortStatus_Object = MibTableColumn
h3cSmlkPortStatus = _H3cSmlkPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 2, 1, 3),
    _H3cSmlkPortStatus_Type()
)
h3cSmlkPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSmlkPortStatus.setStatus("current")
_H3cSmlkFlushCount_Type = Counter64
_H3cSmlkFlushCount_Object = MibTableColumn
h3cSmlkFlushCount = _H3cSmlkFlushCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 2, 1, 4),
    _H3cSmlkFlushCount_Type()
)
h3cSmlkFlushCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSmlkFlushCount.setStatus("current")
_H3cSmlkLastFlushTime_Type = DateAndTime
_H3cSmlkLastFlushTime_Object = MibTableColumn
h3cSmlkLastFlushTime = _H3cSmlkLastFlushTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 2, 1, 5),
    _H3cSmlkLastFlushTime_Type()
)
h3cSmlkLastFlushTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSmlkLastFlushTime.setStatus("current")
_H3cSmlkPortRowStatus_Type = RowStatus
_H3cSmlkPortRowStatus_Object = MibTableColumn
h3cSmlkPortRowStatus = _H3cSmlkPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 2, 1, 6),
    _H3cSmlkPortRowStatus_Type()
)
h3cSmlkPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSmlkPortRowStatus.setStatus("current")
_H3cSmlkFlushEnableTable_Object = MibTable
h3cSmlkFlushEnableTable = _H3cSmlkFlushEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 3)
)
if mibBuilder.loadTexts:
    h3cSmlkFlushEnableTable.setStatus("current")
_H3cSmlkFlushEnableEntry_Object = MibTableRow
h3cSmlkFlushEnableEntry = _H3cSmlkFlushEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 3, 1)
)
h3cSmlkFlushEnableEntry.setIndexNames(
    (0, "H3C-SMLK-MIB", "h3cSmlkIfIndex"),
)
if mibBuilder.loadTexts:
    h3cSmlkFlushEnableEntry.setStatus("current")
_H3cSmlkIfIndex_Type = InterfaceIndex
_H3cSmlkIfIndex_Object = MibTableColumn
h3cSmlkIfIndex = _H3cSmlkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 3, 1, 1),
    _H3cSmlkIfIndex_Type()
)
h3cSmlkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSmlkIfIndex.setStatus("current")


class _H3cSmlkControlVlanListLow_Type(OctetString):
    """Custom type h3cSmlkControlVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )
    fixed_length = 256


_H3cSmlkControlVlanListLow_Type.__name__ = "OctetString"
_H3cSmlkControlVlanListLow_Object = MibTableColumn
h3cSmlkControlVlanListLow = _H3cSmlkControlVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 3, 1, 2),
    _H3cSmlkControlVlanListLow_Type()
)
h3cSmlkControlVlanListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSmlkControlVlanListLow.setStatus("current")


class _H3cSmlkControlVlanListHigh_Type(OctetString):
    """Custom type h3cSmlkControlVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )
    fixed_length = 256


_H3cSmlkControlVlanListHigh_Type.__name__ = "OctetString"
_H3cSmlkControlVlanListHigh_Object = MibTableColumn
h3cSmlkControlVlanListHigh = _H3cSmlkControlVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 1, 3, 1, 3),
    _H3cSmlkControlVlanListHigh_Type()
)
h3cSmlkControlVlanListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSmlkControlVlanListHigh.setStatus("current")
_H3cSmlkTrap_ObjectIdentity = ObjectIdentity
h3cSmlkTrap = _H3cSmlkTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 2)
)
_H3cSmlkTrapPrefix_ObjectIdentity = ObjectIdentity
h3cSmlkTrapPrefix = _H3cSmlkTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 2, 0)
)

# Managed Objects groups


# Notification objects

h3cSmlkGroupLinkActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 147, 2, 0, 1)
)
h3cSmlkGroupLinkActive.setObjects(
      *(("H3C-SMLK-MIB", "h3cSmlkGroupID"),
        ("H3C-SMLK-MIB", "h3cSmlkPortIfIndex"))
)
if mibBuilder.loadTexts:
    h3cSmlkGroupLinkActive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-SMLK-MIB",
    **{"h3cSmlk": h3cSmlk,
       "h3cSmlkObject": h3cSmlkObject,
       "h3cSmlkGroupTable": h3cSmlkGroupTable,
       "h3cSmlkGroupEntry": h3cSmlkGroupEntry,
       "h3cSmlkGroupID": h3cSmlkGroupID,
       "h3cSmlkDeviceID": h3cSmlkDeviceID,
       "h3cSmlkPreemptionMode": h3cSmlkPreemptionMode,
       "h3cSmlkSpeedThreshold": h3cSmlkSpeedThreshold,
       "h3cSmlkPreemptionDelay": h3cSmlkPreemptionDelay,
       "h3cSmlkControlVlanID": h3cSmlkControlVlanID,
       "h3cSmlkInstanceListLow": h3cSmlkInstanceListLow,
       "h3cSmlkInstanceListHigh": h3cSmlkInstanceListHigh,
       "h3cSmlkGroupRowStatus": h3cSmlkGroupRowStatus,
       "h3cSmlkPortTable": h3cSmlkPortTable,
       "h3cSmlkPortEntry": h3cSmlkPortEntry,
       "h3cSmlkPortIfIndex": h3cSmlkPortIfIndex,
       "h3cSmlkPortRole": h3cSmlkPortRole,
       "h3cSmlkPortStatus": h3cSmlkPortStatus,
       "h3cSmlkFlushCount": h3cSmlkFlushCount,
       "h3cSmlkLastFlushTime": h3cSmlkLastFlushTime,
       "h3cSmlkPortRowStatus": h3cSmlkPortRowStatus,
       "h3cSmlkFlushEnableTable": h3cSmlkFlushEnableTable,
       "h3cSmlkFlushEnableEntry": h3cSmlkFlushEnableEntry,
       "h3cSmlkIfIndex": h3cSmlkIfIndex,
       "h3cSmlkControlVlanListLow": h3cSmlkControlVlanListLow,
       "h3cSmlkControlVlanListHigh": h3cSmlkControlVlanListHigh,
       "h3cSmlkTrap": h3cSmlkTrap,
       "h3cSmlkTrapPrefix": h3cSmlkTrapPrefix,
       "h3cSmlkGroupLinkActive": h3cSmlkGroupLinkActive}
)
