# SNMP MIB module (RAISECOM-SCHEDULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-SCHEDULE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:14 2025
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

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

raisecomSchedule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomScheduleconfig_ObjectIdentity = ObjectIdentity
raisecomScheduleconfig = _RaisecomScheduleconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 1)
)
_RaisecomScheduleList_ObjectIdentity = ObjectIdentity
raisecomScheduleList = _RaisecomScheduleList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2)
)
_RaisecomScheduleListTable_Object = MibTable
raisecomScheduleListTable = _RaisecomScheduleListTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    raisecomScheduleListTable.setStatus("current")
_RaisecomScheduleListEntry_Object = MibTableRow
raisecomScheduleListEntry = _RaisecomScheduleListEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 1, 1)
)
raisecomScheduleListEntry.setIndexNames(
    (0, "RAISECOM-SCHEDULE-MIB", "raisecomScheduleListIndex"),
)
if mibBuilder.loadTexts:
    raisecomScheduleListEntry.setStatus("current")


class _RaisecomScheduleListIndex_Type(Integer32):
    """Custom type raisecomScheduleListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_RaisecomScheduleListIndex_Type.__name__ = "Integer32"
_RaisecomScheduleListIndex_Object = MibTableColumn
raisecomScheduleListIndex = _RaisecomScheduleListIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 1, 1, 1),
    _RaisecomScheduleListIndex_Type()
)
raisecomScheduleListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomScheduleListIndex.setStatus("current")


class _RaisecomScheduleListFlag_Type(Integer32):
    """Custom type raisecomScheduleListFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("startup", 1),
          ("realdate", 2))
    )


_RaisecomScheduleListFlag_Type.__name__ = "Integer32"
_RaisecomScheduleListFlag_Object = MibTableColumn
raisecomScheduleListFlag = _RaisecomScheduleListFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 1, 1, 2),
    _RaisecomScheduleListFlag_Type()
)
raisecomScheduleListFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomScheduleListFlag.setStatus("current")
_RaisecomScheduleListStartTime_Type = Integer32
_RaisecomScheduleListStartTime_Object = MibTableColumn
raisecomScheduleListStartTime = _RaisecomScheduleListStartTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 1, 1, 3),
    _RaisecomScheduleListStartTime_Type()
)
raisecomScheduleListStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomScheduleListStartTime.setStatus("current")


class _RaisecomScheduleListPeriod_Type(Integer32):
    """Custom type raisecomScheduleListPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31622400),
    )


_RaisecomScheduleListPeriod_Type.__name__ = "Integer32"
_RaisecomScheduleListPeriod_Object = MibTableColumn
raisecomScheduleListPeriod = _RaisecomScheduleListPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 1, 1, 4),
    _RaisecomScheduleListPeriod_Type()
)
raisecomScheduleListPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomScheduleListPeriod.setStatus("current")
_RaisecomScheduleListStopTime_Type = Integer32
_RaisecomScheduleListStopTime_Object = MibTableColumn
raisecomScheduleListStopTime = _RaisecomScheduleListStopTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 1, 1, 5),
    _RaisecomScheduleListStopTime_Type()
)
raisecomScheduleListStopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomScheduleListStopTime.setStatus("current")
_RaisecomScheduleListLastExeTime_Type = Integer32
_RaisecomScheduleListLastExeTime_Object = MibTableColumn
raisecomScheduleListLastExeTime = _RaisecomScheduleListLastExeTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 1, 1, 6),
    _RaisecomScheduleListLastExeTime_Type()
)
raisecomScheduleListLastExeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomScheduleListLastExeTime.setStatus("current")
_RaisecomScheduleListNextExeTime_Type = Integer32
_RaisecomScheduleListNextExeTime_Object = MibTableColumn
raisecomScheduleListNextExeTime = _RaisecomScheduleListNextExeTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 1, 1, 7),
    _RaisecomScheduleListNextExeTime_Type()
)
raisecomScheduleListNextExeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomScheduleListNextExeTime.setStatus("current")
_RaisecomScheduleRef_Type = Integer32
_RaisecomScheduleRef_Object = MibTableColumn
raisecomScheduleRef = _RaisecomScheduleRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 1, 1, 8),
    _RaisecomScheduleRef_Type()
)
raisecomScheduleRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomScheduleRef.setStatus("current")
_RaisecomScheduleListStatus_Type = RowStatus
_RaisecomScheduleListStatus_Object = MibTableColumn
raisecomScheduleListStatus = _RaisecomScheduleListStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 1, 1, 9),
    _RaisecomScheduleListStatus_Type()
)
raisecomScheduleListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomScheduleListStatus.setStatus("current")
_RaisecomScheduleCommandTable_Object = MibTable
raisecomScheduleCommandTable = _RaisecomScheduleCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 2)
)
if mibBuilder.loadTexts:
    raisecomScheduleCommandTable.setStatus("current")
_RaisecomScheduleCommandEntry_Object = MibTableRow
raisecomScheduleCommandEntry = _RaisecomScheduleCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 2, 1)
)
raisecomScheduleCommandEntry.setIndexNames(
    (0, "RAISECOM-SCHEDULE-MIB", "raisecomScheduleIndex"),
    (0, "RAISECOM-SCHEDULE-MIB", "raisecomScheduleCommandNo"),
)
if mibBuilder.loadTexts:
    raisecomScheduleCommandEntry.setStatus("current")


class _RaisecomScheduleIndex_Type(Integer32):
    """Custom type raisecomScheduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_RaisecomScheduleIndex_Type.__name__ = "Integer32"
_RaisecomScheduleIndex_Object = MibTableColumn
raisecomScheduleIndex = _RaisecomScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 2, 1, 1),
    _RaisecomScheduleIndex_Type()
)
raisecomScheduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomScheduleIndex.setStatus("current")


class _RaisecomScheduleCommandNo_Type(Integer32):
    """Custom type raisecomScheduleCommandNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_RaisecomScheduleCommandNo_Type.__name__ = "Integer32"
_RaisecomScheduleCommandNo_Object = MibTableColumn
raisecomScheduleCommandNo = _RaisecomScheduleCommandNo_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 2, 1, 2),
    _RaisecomScheduleCommandNo_Type()
)
raisecomScheduleCommandNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomScheduleCommandNo.setStatus("current")


class _RaisecomScheduleCommandString_Type(OctetString):
    """Custom type raisecomScheduleCommandString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RaisecomScheduleCommandString_Type.__name__ = "OctetString"
_RaisecomScheduleCommandString_Object = MibTableColumn
raisecomScheduleCommandString = _RaisecomScheduleCommandString_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 2, 1, 3),
    _RaisecomScheduleCommandString_Type()
)
raisecomScheduleCommandString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomScheduleCommandString.setStatus("current")


class _RaisecomScheduleCommandMode_Type(Integer32):
    """Custom type raisecomScheduleCommandMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("user-mode", 0),
          ("auth-mode", 1),
          ("view-mode", 2),
          ("auth-enable-mode", 3),
          ("enable-mode", 4),
          ("vlan-mode", 5),
          ("interface-mode", 6),
          ("interface-range-mode", 7),
          ("aggregator-mode", 8),
          ("ip-mode", 9),
          ("config-mode", 10),
          ("rip-mode", 11),
          ("bgp-mode", 12),
          ("ospf-mode", 13),
          ("factory-mode", 14),
          ("game-mode", 15),
          ("hide-mode", 16),
          ("cluster-mode", 17))
    )


_RaisecomScheduleCommandMode_Type.__name__ = "Integer32"
_RaisecomScheduleCommandMode_Object = MibTableColumn
raisecomScheduleCommandMode = _RaisecomScheduleCommandMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 2, 1, 4),
    _RaisecomScheduleCommandMode_Type()
)
raisecomScheduleCommandMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomScheduleCommandMode.setStatus("current")


class _RaisecomScheduleCommandNodeInfo_Type(OctetString):
    """Custom type raisecomScheduleCommandNodeInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RaisecomScheduleCommandNodeInfo_Type.__name__ = "OctetString"
_RaisecomScheduleCommandNodeInfo_Object = MibTableColumn
raisecomScheduleCommandNodeInfo = _RaisecomScheduleCommandNodeInfo_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 2, 1, 5),
    _RaisecomScheduleCommandNodeInfo_Type()
)
raisecomScheduleCommandNodeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomScheduleCommandNodeInfo.setStatus("current")
_RaisecomScheduleCommandExeCount_Type = Integer32
_RaisecomScheduleCommandExeCount_Object = MibTableColumn
raisecomScheduleCommandExeCount = _RaisecomScheduleCommandExeCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 2, 1, 6),
    _RaisecomScheduleCommandExeCount_Type()
)
raisecomScheduleCommandExeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomScheduleCommandExeCount.setStatus("current")
_RaisecomScheduleCommandLastExeTime_Type = Integer32
_RaisecomScheduleCommandLastExeTime_Object = MibTableColumn
raisecomScheduleCommandLastExeTime = _RaisecomScheduleCommandLastExeTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 8, 2, 2, 1, 7),
    _RaisecomScheduleCommandLastExeTime_Type()
)
raisecomScheduleCommandLastExeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomScheduleCommandLastExeTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-SCHEDULE-MIB",
    **{"raisecomSchedule": raisecomSchedule,
       "raisecomScheduleconfig": raisecomScheduleconfig,
       "raisecomScheduleList": raisecomScheduleList,
       "raisecomScheduleListTable": raisecomScheduleListTable,
       "raisecomScheduleListEntry": raisecomScheduleListEntry,
       "raisecomScheduleListIndex": raisecomScheduleListIndex,
       "raisecomScheduleListFlag": raisecomScheduleListFlag,
       "raisecomScheduleListStartTime": raisecomScheduleListStartTime,
       "raisecomScheduleListPeriod": raisecomScheduleListPeriod,
       "raisecomScheduleListStopTime": raisecomScheduleListStopTime,
       "raisecomScheduleListLastExeTime": raisecomScheduleListLastExeTime,
       "raisecomScheduleListNextExeTime": raisecomScheduleListNextExeTime,
       "raisecomScheduleRef": raisecomScheduleRef,
       "raisecomScheduleListStatus": raisecomScheduleListStatus,
       "raisecomScheduleCommandTable": raisecomScheduleCommandTable,
       "raisecomScheduleCommandEntry": raisecomScheduleCommandEntry,
       "raisecomScheduleIndex": raisecomScheduleIndex,
       "raisecomScheduleCommandNo": raisecomScheduleCommandNo,
       "raisecomScheduleCommandString": raisecomScheduleCommandString,
       "raisecomScheduleCommandMode": raisecomScheduleCommandMode,
       "raisecomScheduleCommandNodeInfo": raisecomScheduleCommandNodeInfo,
       "raisecomScheduleCommandExeCount": raisecomScheduleCommandExeCount,
       "raisecomScheduleCommandLastExeTime": raisecomScheduleCommandLastExeTime}
)
