# SNMP MIB module (INFINERA-TP-IFCOMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-IFCOMMON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:23 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(commonTerminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "commonTerminationPoint")

(InfnAvailabilityState,
 InfnOpsQualifierList) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnAvailabilityState",
    "InfnOpsQualifierList")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ifCommonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    ifCommonMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IfCommonTable_Object = MibTable
ifCommonTable = _IfCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    ifCommonTable.setStatus("current")
_IfCommonEntry_Object = MibTableRow
ifCommonEntry = _IfCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 1, 1)
)
ifCommonEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifCommonEntry.setStatus("current")
_IfCommonMoId_Type = DisplayString
_IfCommonMoId_Object = MibTableColumn
ifCommonMoId = _IfCommonMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 1, 1, 1),
    _IfCommonMoId_Type()
)
ifCommonMoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCommonMoId.setStatus("current")


class _IfCommonAvailabilityState_Type(InfnAvailabilityState):
    """Custom type ifCommonAvailabilityState based on InfnAvailabilityState"""
    defaultValue = 3


_IfCommonAvailabilityState_Type.__name__ = "InfnAvailabilityState"
_IfCommonAvailabilityState_Object = MibTableColumn
ifCommonAvailabilityState = _IfCommonAvailabilityState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 1, 1, 2),
    _IfCommonAvailabilityState_Type()
)
ifCommonAvailabilityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCommonAvailabilityState.setStatus("current")


class _IfCommonAlarmReportControl_Type(Integer32):
    """Custom type ifCommonAlarmReportControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("inhibited", 2))
    )


_IfCommonAlarmReportControl_Type.__name__ = "Integer32"
_IfCommonAlarmReportControl_Object = MibTableColumn
ifCommonAlarmReportControl = _IfCommonAlarmReportControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 1, 1, 3),
    _IfCommonAlarmReportControl_Type()
)
ifCommonAlarmReportControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCommonAlarmReportControl.setStatus("current")
_IfCommonOpStateQualifierList_Type = InfnOpsQualifierList
_IfCommonOpStateQualifierList_Object = MibTableColumn
ifCommonOpStateQualifierList = _IfCommonOpStateQualifierList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 1, 1, 4),
    _IfCommonOpStateQualifierList_Type()
)
ifCommonOpStateQualifierList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCommonOpStateQualifierList.setStatus("current")


class _IfCommonAlarmInhibitState_Type(Integer32):
    """Custom type ifCommonAlarmInhibitState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("inhibited", 2))
    )


_IfCommonAlarmInhibitState_Type.__name__ = "Integer32"
_IfCommonAlarmInhibitState_Object = MibTableColumn
ifCommonAlarmInhibitState = _IfCommonAlarmInhibitState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 1, 1, 5),
    _IfCommonAlarmInhibitState_Type()
)
ifCommonAlarmInhibitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCommonAlarmInhibitState.setStatus("current")
_IfCommonConformance_ObjectIdentity = ObjectIdentity
ifCommonConformance = _IfCommonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 3)
)
_IfCommonCompliances_ObjectIdentity = ObjectIdentity
ifCommonCompliances = _IfCommonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 3, 1)
)
_IfCommonGroups_ObjectIdentity = ObjectIdentity
ifCommonGroups = _IfCommonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 3, 2)
)

# Managed Objects groups

ifCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 3, 2, 1)
)
ifCommonGroup.setObjects(
      *(("INFINERA-TP-IFCOMMON-MIB", "ifCommonMoId"),
        ("INFINERA-TP-IFCOMMON-MIB", "ifCommonAvailabilityState"),
        ("INFINERA-TP-IFCOMMON-MIB", "ifCommonAlarmReportControl"),
        ("INFINERA-TP-IFCOMMON-MIB", "ifCommonOpStateQualifierList"),
        ("INFINERA-TP-IFCOMMON-MIB", "ifCommonAlarmInhibitState"))
)
if mibBuilder.loadTexts:
    ifCommonGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ifCommonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 3, 1, 1)
)
ifCommonCompliance.setObjects(
    ("INFINERA-TP-IFCOMMON-MIB", "ifCommonGroup")
)
if mibBuilder.loadTexts:
    ifCommonCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-IFCOMMON-MIB",
    **{"ifCommonMIB": ifCommonMIB,
       "ifCommonTable": ifCommonTable,
       "ifCommonEntry": ifCommonEntry,
       "ifCommonMoId": ifCommonMoId,
       "ifCommonAvailabilityState": ifCommonAvailabilityState,
       "ifCommonAlarmReportControl": ifCommonAlarmReportControl,
       "ifCommonOpStateQualifierList": ifCommonOpStateQualifierList,
       "ifCommonAlarmInhibitState": ifCommonAlarmInhibitState,
       "ifCommonConformance": ifCommonConformance,
       "ifCommonCompliances": ifCommonCompliances,
       "ifCommonCompliance": ifCommonCompliance,
       "ifCommonGroups": ifCommonGroups,
       "ifCommonGroup": ifCommonGroup}
)
