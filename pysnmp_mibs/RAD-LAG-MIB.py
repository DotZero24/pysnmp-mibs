# SNMP MIB module (RAD-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-LAG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:17:45 2025
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

(dot3adAggPortEntry,) = mibBuilder.importSymbols(
    "IEEE8023-LAG-MIB",
    "dot3adAggPortEntry")

(InterfaceIndexOrZero,
 ifAlias) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifAlias")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason")

(agnt,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "agnt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

lag = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LagEvents_ObjectIdentity = ObjectIdentity
lagEvents = _LagEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 0)
)
_LagTable_Object = MibTable
lagTable = _LagTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 1)
)
if mibBuilder.loadTexts:
    lagTable.setStatus("current")
_LagEntry_Object = MibTableRow
lagEntry = _LagEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 1, 1)
)
lagEntry.setIndexNames(
    (0, "RAD-LAG-MIB", "lagCnfgIdx"),
    (0, "RAD-LAG-MIB", "lagIdx"),
)
if mibBuilder.loadTexts:
    lagEntry.setStatus("current")


class _LagCnfgIdx_Type(Unsigned32):
    """Custom type lagCnfgIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LagCnfgIdx_Type.__name__ = "Unsigned32"
_LagCnfgIdx_Object = MibTableColumn
lagCnfgIdx = _LagCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 1, 1, 1),
    _LagCnfgIdx_Type()
)
lagCnfgIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lagCnfgIdx.setStatus("current")
_LagIdx_Type = Unsigned32
_LagIdx_Object = MibTableColumn
lagIdx = _LagIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 1, 1, 2),
    _LagIdx_Type()
)
lagIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lagIdx.setStatus("current")
_LagPortMembers_Type = PortList
_LagPortMembers_Object = MibTableColumn
lagPortMembers = _LagPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 1, 1, 3),
    _LagPortMembers_Type()
)
lagPortMembers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lagPortMembers.setStatus("current")


class _LagDistributionMethod_Type(Integer32):
    """Custom type lagDistributionMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("portBased", 2),
          ("oneToOne", 3),
          ("sourceMac", 4),
          ("destinationMac", 5),
          ("sourceXorDestinationMac", 6),
          ("sourceAndDestinationMac", 7),
          ("sourceIp", 8),
          ("destinationIp", 9),
          ("sourceAndDestinationMacAndIp", 10),
          ("roundRobin", 11),
          ("sourceAndDestinationIp", 12))
    )


_LagDistributionMethod_Type.__name__ = "Integer32"
_LagDistributionMethod_Object = MibTableColumn
lagDistributionMethod = _LagDistributionMethod_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 1, 1, 4),
    _LagDistributionMethod_Type()
)
lagDistributionMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lagDistributionMethod.setStatus("current")


class _LagRecoveryMode_Type(Integer32):
    """Custom type lagRecoveryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonRevertive", 2),
          ("revertive", 3))
    )


_LagRecoveryMode_Type.__name__ = "Integer32"
_LagRecoveryMode_Object = MibTableColumn
lagRecoveryMode = _LagRecoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 1, 1, 5),
    _LagRecoveryMode_Type()
)
lagRecoveryMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lagRecoveryMode.setStatus("current")


class _LagWaitToRestore_Type(Unsigned32):
    """Custom type lagWaitToRestore based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_LagWaitToRestore_Type.__name__ = "Unsigned32"
_LagWaitToRestore_Object = MibTableColumn
lagWaitToRestore = _LagWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 1, 1, 6),
    _LagWaitToRestore_Type()
)
lagWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lagWaitToRestore.setStatus("current")
_LagRowStatus_Type = RowStatus
_LagRowStatus_Object = MibTableColumn
lagRowStatus = _LagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 1, 1, 7),
    _LagRowStatus_Type()
)
lagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lagRowStatus.setStatus("current")


class _LagShutDownDurationUponFlip_Type(Unsigned32):
    """Custom type lagShutDownDurationUponFlip based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_LagShutDownDurationUponFlip_Type.__name__ = "Unsigned32"
_LagShutDownDurationUponFlip_Object = MibTableColumn
lagShutDownDurationUponFlip = _LagShutDownDurationUponFlip_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 1, 1, 8),
    _LagShutDownDurationUponFlip_Type()
)
lagShutDownDurationUponFlip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lagShutDownDurationUponFlip.setStatus("current")


class _LagRdnMethod_Type(Integer32):
    """Custom type lagRdnMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loadSharing", 1),
          ("redundancy", 2))
    )


_LagRdnMethod_Type.__name__ = "Integer32"
_LagRdnMethod_Object = MibTableColumn
lagRdnMethod = _LagRdnMethod_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 1, 1, 9),
    _LagRdnMethod_Type()
)
lagRdnMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lagRdnMethod.setStatus("current")


class _LagLacpEnable_Type(Integer32):
    """Custom type lagLacpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_LagLacpEnable_Type.__name__ = "Integer32"
_LagLacpEnable_Object = MibTableColumn
lagLacpEnable = _LagLacpEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 1, 1, 10),
    _LagLacpEnable_Type()
)
lagLacpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lagLacpEnable.setStatus("current")


class _LagMinimumLinks_Type(Unsigned32):
    """Custom type lagMinimumLinks based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_LagMinimumLinks_Type.__name__ = "Unsigned32"
_LagMinimumLinks_Object = MibTableColumn
lagMinimumLinks = _LagMinimumLinks_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 1, 1, 12),
    _LagMinimumLinks_Type()
)
lagMinimumLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lagMinimumLinks.setStatus("current")
_LagAnchorPort_Type = InterfaceIndexOrZero
_LagAnchorPort_Object = MibTableColumn
lagAnchorPort = _LagAnchorPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 1, 1, 13),
    _LagAnchorPort_Type()
)
lagAnchorPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lagAnchorPort.setStatus("current")
_LagStatTable_Object = MibTable
lagStatTable = _LagStatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 2)
)
if mibBuilder.loadTexts:
    lagStatTable.setStatus("current")
_LagStatEntry_Object = MibTableRow
lagStatEntry = _LagStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 2, 1)
)
lagStatEntry.setIndexNames(
    (0, "RAD-LAG-MIB", "lagIdx"),
)
if mibBuilder.loadTexts:
    lagStatEntry.setStatus("current")
_LagStatForcePort_Type = Unsigned32
_LagStatForcePort_Object = MibTableColumn
lagStatForcePort = _LagStatForcePort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 2, 1, 1),
    _LagStatForcePort_Type()
)
lagStatForcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lagStatForcePort.setStatus("current")
_LagStatActivePort_Type = Unsigned32
_LagStatActivePort_Object = MibTableColumn
lagStatActivePort = _LagStatActivePort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 2, 1, 2),
    _LagStatActivePort_Type()
)
lagStatActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagStatActivePort.setStatus("current")
_Dot3adAggPortXTable_Object = MibTable
dot3adAggPortXTable = _Dot3adAggPortXTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 3)
)
if mibBuilder.loadTexts:
    dot3adAggPortXTable.setStatus("current")
_Dot3adAggPortXEntry_Object = MibTableRow
dot3adAggPortXEntry = _Dot3adAggPortXEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 3, 1)
)
if mibBuilder.loadTexts:
    dot3adAggPortXEntry.setStatus("current")


class _Dot3adAggPortXprotectionState_Type(Integer32):
    """Custom type dot3adAggPortXprotectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("standby", 2),
          ("active", 3))
    )


_Dot3adAggPortXprotectionState_Type.__name__ = "Integer32"
_Dot3adAggPortXprotectionState_Object = MibTableColumn
dot3adAggPortXprotectionState = _Dot3adAggPortXprotectionState_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 3, 1, 1),
    _Dot3adAggPortXprotectionState_Type()
)
dot3adAggPortXprotectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortXprotectionState.setStatus("current")
dot3adAggPortEntry.registerAugmentions(
    ("RAD-LAG-MIB",
     "dot3adAggPortXEntry")
)
dot3adAggPortXEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects

lagLacpDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 0, 1)
)
lagLacpDown.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    lagLacpDown.setStatus(
        "deprecated"
    )

lagLacpLoopDetection = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 0, 2)
)
lagLacpLoopDetection.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    lagLacpLoopDetection.setStatus(
        "deprecated"
    )

lagLacpChurn = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 0, 3)
)
lagLacpChurn.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    lagLacpChurn.setStatus(
        "deprecated"
    )

lagSubGroupSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 0, 4)
)
lagSubGroupSwitchover.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    lagSubGroupSwitchover.setStatus(
        "current"
    )

lagFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 0, 5)
)
lagFailure.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    lagFailure.setStatus(
        "deprecated"
    )

lagMinimumMembers = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 54, 0, 6)
)
lagMinimumMembers.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("RAD-LAG-MIB", "lagMinimumLinks"))
)
if mibBuilder.loadTexts:
    lagMinimumMembers.setStatus(
        "deprecated"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-LAG-MIB",
    **{"lag": lag,
       "lagEvents": lagEvents,
       "lagLacpDown": lagLacpDown,
       "lagLacpLoopDetection": lagLacpLoopDetection,
       "lagLacpChurn": lagLacpChurn,
       "lagSubGroupSwitchover": lagSubGroupSwitchover,
       "lagFailure": lagFailure,
       "lagMinimumMembers": lagMinimumMembers,
       "lagTable": lagTable,
       "lagEntry": lagEntry,
       "lagCnfgIdx": lagCnfgIdx,
       "lagIdx": lagIdx,
       "lagPortMembers": lagPortMembers,
       "lagDistributionMethod": lagDistributionMethod,
       "lagRecoveryMode": lagRecoveryMode,
       "lagWaitToRestore": lagWaitToRestore,
       "lagRowStatus": lagRowStatus,
       "lagShutDownDurationUponFlip": lagShutDownDurationUponFlip,
       "lagRdnMethod": lagRdnMethod,
       "lagLacpEnable": lagLacpEnable,
       "lagMinimumLinks": lagMinimumLinks,
       "lagAnchorPort": lagAnchorPort,
       "lagStatTable": lagStatTable,
       "lagStatEntry": lagStatEntry,
       "lagStatForcePort": lagStatForcePort,
       "lagStatActivePort": lagStatActivePort,
       "dot3adAggPortXTable": dot3adAggPortXTable,
       "dot3adAggPortXEntry": dot3adAggPortXEntry,
       "dot3adAggPortXprotectionState": dot3adAggPortXprotectionState}
)
