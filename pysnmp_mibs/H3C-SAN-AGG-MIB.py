# SNMP MIB module (H3C-SAN-AGG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-SAN-AGG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:28 2025
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

(h3cSan,) = mibBuilder.importSymbols(
    "H3C-VSAN-MIB",
    "h3cSan")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

h3cSanAgg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 2)
)
if mibBuilder.loadTexts:
    h3cSanAgg.setRevisions(
        ("2013-02-25 09:40",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cMemberList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_H3cSanAggMibObjects_ObjectIdentity = ObjectIdentity
h3cSanAggMibObjects = _H3cSanAggMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 2, 1)
)
_H3cSanAggMaxMemberNumber_Type = Integer32
_H3cSanAggMaxMemberNumber_Object = MibScalar
h3cSanAggMaxMemberNumber = _H3cSanAggMaxMemberNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 2, 1, 1),
    _H3cSanAggMaxMemberNumber_Type()
)
h3cSanAggMaxMemberNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSanAggMaxMemberNumber.setStatus("current")
_H3cSanAggGroupTable_Object = MibTable
h3cSanAggGroupTable = _H3cSanAggGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 2, 2)
)
if mibBuilder.loadTexts:
    h3cSanAggGroupTable.setStatus("current")
_H3cSanAggGroupEntry_Object = MibTableRow
h3cSanAggGroupEntry = _H3cSanAggGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 2, 2, 1)
)
h3cSanAggGroupEntry.setIndexNames(
    (0, "H3C-SAN-AGG-MIB", "h3cSanAggGroupNumber"),
)
if mibBuilder.loadTexts:
    h3cSanAggGroupEntry.setStatus("current")


class _H3cSanAggGroupNumber_Type(Integer32):
    """Custom type h3cSanAggGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cSanAggGroupNumber_Type.__name__ = "Integer32"
_H3cSanAggGroupNumber_Object = MibTableColumn
h3cSanAggGroupNumber = _H3cSanAggGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 2, 2, 1, 1),
    _H3cSanAggGroupNumber_Type()
)
h3cSanAggGroupNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSanAggGroupNumber.setStatus("current")
_H3cSanAggGroupIndex_Type = Integer32
_H3cSanAggGroupIndex_Object = MibTableColumn
h3cSanAggGroupIndex = _H3cSanAggGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 2, 2, 1, 2),
    _H3cSanAggGroupIndex_Type()
)
h3cSanAggGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSanAggGroupIndex.setStatus("current")
_H3cSanAggMemberList_Type = H3cMemberList
_H3cSanAggMemberList_Object = MibTableColumn
h3cSanAggMemberList = _H3cSanAggMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 2, 2, 1, 3),
    _H3cSanAggMemberList_Type()
)
h3cSanAggMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSanAggMemberList.setStatus("current")
_H3cSanAggMemberStateList_Type = H3cMemberList
_H3cSanAggMemberStateList_Object = MibTableColumn
h3cSanAggMemberStateList = _H3cSanAggMemberStateList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 2, 2, 1, 4),
    _H3cSanAggMemberStateList_Type()
)
h3cSanAggMemberStateList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSanAggMemberStateList.setStatus("current")
_H3cSanAggGroupRowStatus_Type = RowStatus
_H3cSanAggGroupRowStatus_Object = MibTableColumn
h3cSanAggGroupRowStatus = _H3cSanAggGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 2, 2, 1, 5),
    _H3cSanAggGroupRowStatus_Type()
)
h3cSanAggGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSanAggGroupRowStatus.setStatus("current")
_H3cSanAggObjForNotification_ObjectIdentity = ObjectIdentity
h3cSanAggObjForNotification = _H3cSanAggObjForNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 2, 3)
)
_H3cSanAggGroupPreviousSpeed_Type = Integer32
_H3cSanAggGroupPreviousSpeed_Object = MibScalar
h3cSanAggGroupPreviousSpeed = _H3cSanAggGroupPreviousSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 2, 3, 1),
    _H3cSanAggGroupPreviousSpeed_Type()
)
h3cSanAggGroupPreviousSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSanAggGroupPreviousSpeed.setStatus("current")
if mibBuilder.loadTexts:
    h3cSanAggGroupPreviousSpeed.setUnits("gigabit bps")
_H3cSanAggGroupCurrentSpeed_Type = Integer32
_H3cSanAggGroupCurrentSpeed_Object = MibScalar
h3cSanAggGroupCurrentSpeed = _H3cSanAggGroupCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 2, 3, 2),
    _H3cSanAggGroupCurrentSpeed_Type()
)
h3cSanAggGroupCurrentSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSanAggGroupCurrentSpeed.setStatus("current")
if mibBuilder.loadTexts:
    h3cSanAggGroupCurrentSpeed.setUnits("gigabit bps")
_H3cSanAggNotifications_ObjectIdentity = ObjectIdentity
h3cSanAggNotifications = _H3cSanAggNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 2, 4)
)
_H3cSanAggNotificationPrefix_ObjectIdentity = ObjectIdentity
h3cSanAggNotificationPrefix = _H3cSanAggNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 2, 4, 0)
)

# Managed Objects groups


# Notification objects

h3cSanAggGroupSpeedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 2, 4, 0, 1)
)
h3cSanAggGroupSpeedChange.setObjects(
      *(("H3C-SAN-AGG-MIB", "h3cSanAggGroupNumber"),
        ("H3C-SAN-AGG-MIB", "h3cSanAggGroupPreviousSpeed"),
        ("H3C-SAN-AGG-MIB", "h3cSanAggGroupCurrentSpeed"))
)
if mibBuilder.loadTexts:
    h3cSanAggGroupSpeedChange.setStatus(
        "current"
    )

h3cSanAggMemberInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 2, 4, 0, 2)
)
h3cSanAggMemberInactive.setObjects(
      *(("H3C-SAN-AGG-MIB", "h3cSanAggGroupNumber"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cSanAggMemberInactive.setStatus(
        "current"
    )

h3cSanAggMemberActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 2, 4, 0, 3)
)
h3cSanAggMemberActive.setObjects(
      *(("H3C-SAN-AGG-MIB", "h3cSanAggGroupNumber"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cSanAggMemberActive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-SAN-AGG-MIB",
    **{"H3cMemberList": H3cMemberList,
       "h3cSanAgg": h3cSanAgg,
       "h3cSanAggMibObjects": h3cSanAggMibObjects,
       "h3cSanAggMaxMemberNumber": h3cSanAggMaxMemberNumber,
       "h3cSanAggGroupTable": h3cSanAggGroupTable,
       "h3cSanAggGroupEntry": h3cSanAggGroupEntry,
       "h3cSanAggGroupNumber": h3cSanAggGroupNumber,
       "h3cSanAggGroupIndex": h3cSanAggGroupIndex,
       "h3cSanAggMemberList": h3cSanAggMemberList,
       "h3cSanAggMemberStateList": h3cSanAggMemberStateList,
       "h3cSanAggGroupRowStatus": h3cSanAggGroupRowStatus,
       "h3cSanAggObjForNotification": h3cSanAggObjForNotification,
       "h3cSanAggGroupPreviousSpeed": h3cSanAggGroupPreviousSpeed,
       "h3cSanAggGroupCurrentSpeed": h3cSanAggGroupCurrentSpeed,
       "h3cSanAggNotifications": h3cSanAggNotifications,
       "h3cSanAggNotificationPrefix": h3cSanAggNotificationPrefix,
       "h3cSanAggGroupSpeedChange": h3cSanAggGroupSpeedChange,
       "h3cSanAggMemberInactive": h3cSanAggMemberInactive,
       "h3cSanAggMemberActive": h3cSanAggMemberActive}
)
