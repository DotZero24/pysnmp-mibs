# SNMP MIB module (RAD-Etp-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-Etp-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:49 2025
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

(InterfaceIndex,
 ifAlias) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifAlias")

(ethIf,) = mibBuilder.importSymbols(
    "RAD-EthIf-MIB",
    "ethIf")

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

etp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtpEvents_ObjectIdentity = ObjectIdentity
etpEvents = _EtpEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 0)
)
_EtpTable_Object = MibTable
etpTable = _EtpTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 1)
)
if mibBuilder.loadTexts:
    etpTable.setStatus("current")
_EtpEntry_Object = MibTableRow
etpEntry = _EtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 1, 1)
)
etpEntry.setIndexNames(
    (0, "RAD-Etp-MIB", "etpIdx"),
)
if mibBuilder.loadTexts:
    etpEntry.setStatus("current")


class _EtpIdx_Type(Unsigned32):
    """Custom type etpIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EtpIdx_Type.__name__ = "Unsigned32"
_EtpIdx_Object = MibTableColumn
etpIdx = _EtpIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 1, 1, 1),
    _EtpIdx_Type()
)
etpIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etpIdx.setStatus("current")
_EtpRowStatus_Type = RowStatus
_EtpRowStatus_Object = MibTableColumn
etpRowStatus = _EtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 1, 1, 2),
    _EtpRowStatus_Type()
)
etpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etpRowStatus.setStatus("current")
_EtpName_Type = SnmpAdminString
_EtpName_Object = MibTableColumn
etpName = _EtpName_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 1, 1, 3),
    _EtpName_Type()
)
etpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etpName.setStatus("current")


class _EtpOperStatus_Type(Integer32):
    """Custom type etpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_EtpOperStatus_Type.__name__ = "Integer32"
_EtpOperStatus_Object = MibTableColumn
etpOperStatus = _EtpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 1, 1, 4),
    _EtpOperStatus_Type()
)
etpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etpOperStatus.setStatus("current")


class _EtpClearStatCounters_Type(Integer32):
    """Custom type etpClearStatCounters based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_EtpClearStatCounters_Type.__name__ = "Integer32"
_EtpClearStatCounters_Object = MibTableColumn
etpClearStatCounters = _EtpClearStatCounters_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 1, 1, 5),
    _EtpClearStatCounters_Type()
)
etpClearStatCounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etpClearStatCounters.setStatus("current")
_EtpPortTable_Object = MibTable
etpPortTable = _EtpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 2)
)
if mibBuilder.loadTexts:
    etpPortTable.setStatus("current")
_EtpPortEntry_Object = MibTableRow
etpPortEntry = _EtpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 2, 1)
)
etpPortEntry.setIndexNames(
    (0, "RAD-Etp-MIB", "etpPortIfIndex"),
)
if mibBuilder.loadTexts:
    etpPortEntry.setStatus("current")
_EtpPortIfIndex_Type = InterfaceIndex
_EtpPortIfIndex_Object = MibTableColumn
etpPortIfIndex = _EtpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 2, 1, 1),
    _EtpPortIfIndex_Type()
)
etpPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etpPortIfIndex.setStatus("current")
_EtpPortRowStatus_Type = RowStatus
_EtpPortRowStatus_Object = MibTableColumn
etpPortRowStatus = _EtpPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 2, 1, 2),
    _EtpPortRowStatus_Type()
)
etpPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etpPortRowStatus.setStatus("current")
_EtpStatTable_Object = MibTable
etpStatTable = _EtpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3)
)
if mibBuilder.loadTexts:
    etpStatTable.setStatus("current")
_EtpStatEntry_Object = MibTableRow
etpStatEntry = _EtpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1)
)
etpStatEntry.setIndexNames(
    (0, "RAD-Etp-MIB", "etpIdx"),
    (0, "RAD-Etp-MIB", "etpServiceIndex"),
    (0, "RAD-Etp-MIB", "etpStatDirection"),
)
if mibBuilder.loadTexts:
    etpStatEntry.setStatus("current")
_EtpServiceIndex_Type = Integer32
_EtpServiceIndex_Object = MibTableColumn
etpServiceIndex = _EtpServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 1),
    _EtpServiceIndex_Type()
)
etpServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etpServiceIndex.setStatus("current")


class _EtpStatDirection_Type(Integer32):
    """Custom type etpStatDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("tx", 1),
          ("rx", 2),
          ("notApplicable", 255))
    )


_EtpStatDirection_Type.__name__ = "Integer32"
_EtpStatDirection_Object = MibTableColumn
etpStatDirection = _EtpStatDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 2),
    _EtpStatDirection_Type()
)
etpStatDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etpStatDirection.setStatus("current")
_EtpForwardGreenPackets_Type = Counter32
_EtpForwardGreenPackets_Object = MibTableColumn
etpForwardGreenPackets = _EtpForwardGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 3),
    _EtpForwardGreenPackets_Type()
)
etpForwardGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etpForwardGreenPackets.setStatus("current")
_EtpForwardGreenPacketsOverflow_Type = Counter32
_EtpForwardGreenPacketsOverflow_Object = MibTableColumn
etpForwardGreenPacketsOverflow = _EtpForwardGreenPacketsOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 4),
    _EtpForwardGreenPacketsOverflow_Type()
)
etpForwardGreenPacketsOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etpForwardGreenPacketsOverflow.setStatus("current")
_EtpForwardYellowPackets_Type = Counter32
_EtpForwardYellowPackets_Object = MibTableColumn
etpForwardYellowPackets = _EtpForwardYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 5),
    _EtpForwardYellowPackets_Type()
)
etpForwardYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etpForwardYellowPackets.setStatus("current")
_EtpForwardYellowPacketsOverflow_Type = Counter32
_EtpForwardYellowPacketsOverflow_Object = MibTableColumn
etpForwardYellowPacketsOverflow = _EtpForwardYellowPacketsOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 6),
    _EtpForwardYellowPacketsOverflow_Type()
)
etpForwardYellowPacketsOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etpForwardYellowPacketsOverflow.setStatus("current")
_EtpDiscardGreenPackets_Type = Counter32
_EtpDiscardGreenPackets_Object = MibTableColumn
etpDiscardGreenPackets = _EtpDiscardGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 7),
    _EtpDiscardGreenPackets_Type()
)
etpDiscardGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etpDiscardGreenPackets.setStatus("current")
_EtpDiscardGreenPacketsOverflow_Type = Counter32
_EtpDiscardGreenPacketsOverflow_Object = MibTableColumn
etpDiscardGreenPacketsOverflow = _EtpDiscardGreenPacketsOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 8),
    _EtpDiscardGreenPacketsOverflow_Type()
)
etpDiscardGreenPacketsOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etpDiscardGreenPacketsOverflow.setStatus("current")
_EtpDiscardYellowRedPackets_Type = Counter32
_EtpDiscardYellowRedPackets_Object = MibTableColumn
etpDiscardYellowRedPackets = _EtpDiscardYellowRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 9),
    _EtpDiscardYellowRedPackets_Type()
)
etpDiscardYellowRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etpDiscardYellowRedPackets.setStatus("current")
_EtpDiscardYellowRedPacketsOverflow_Type = Counter32
_EtpDiscardYellowRedPacketsOverflow_Object = MibTableColumn
etpDiscardYellowRedPacketsOverflow = _EtpDiscardYellowRedPacketsOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 10),
    _EtpDiscardYellowRedPacketsOverflow_Type()
)
etpDiscardYellowRedPacketsOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etpDiscardYellowRedPacketsOverflow.setStatus("current")
_EtpForwardGreenBytes_Type = Counter32
_EtpForwardGreenBytes_Object = MibTableColumn
etpForwardGreenBytes = _EtpForwardGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 11),
    _EtpForwardGreenBytes_Type()
)
etpForwardGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etpForwardGreenBytes.setStatus("current")
_EtpForwardGreenBytesOverflow_Type = Counter32
_EtpForwardGreenBytesOverflow_Object = MibTableColumn
etpForwardGreenBytesOverflow = _EtpForwardGreenBytesOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 12),
    _EtpForwardGreenBytesOverflow_Type()
)
etpForwardGreenBytesOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etpForwardGreenBytesOverflow.setStatus("current")
_EtpForwardYellowBytes_Type = Counter32
_EtpForwardYellowBytes_Object = MibTableColumn
etpForwardYellowBytes = _EtpForwardYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 13),
    _EtpForwardYellowBytes_Type()
)
etpForwardYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etpForwardYellowBytes.setStatus("current")
_EtpForwardYellowBytesOverflow_Type = Counter32
_EtpForwardYellowBytesOverflow_Object = MibTableColumn
etpForwardYellowBytesOverflow = _EtpForwardYellowBytesOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 14),
    _EtpForwardYellowBytesOverflow_Type()
)
etpForwardYellowBytesOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etpForwardYellowBytesOverflow.setStatus("current")
_EtpDiscardGreenBytes_Type = Counter32
_EtpDiscardGreenBytes_Object = MibTableColumn
etpDiscardGreenBytes = _EtpDiscardGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 15),
    _EtpDiscardGreenBytes_Type()
)
etpDiscardGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etpDiscardGreenBytes.setStatus("current")
_EtpDiscardGreenBytesOverflow_Type = Counter32
_EtpDiscardGreenBytesOverflow_Object = MibTableColumn
etpDiscardGreenBytesOverflow = _EtpDiscardGreenBytesOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 16),
    _EtpDiscardGreenBytesOverflow_Type()
)
etpDiscardGreenBytesOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etpDiscardGreenBytesOverflow.setStatus("current")
_EtpDiscardYellowRedBytes_Type = Counter32
_EtpDiscardYellowRedBytes_Object = MibTableColumn
etpDiscardYellowRedBytes = _EtpDiscardYellowRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 17),
    _EtpDiscardYellowRedBytes_Type()
)
etpDiscardYellowRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etpDiscardYellowRedBytes.setStatus("current")
_EtpDiscardYellowRedBytesOverflow_Type = Counter32
_EtpDiscardYellowRedBytesOverflow_Object = MibTableColumn
etpDiscardYellowRedBytesOverflow = _EtpDiscardYellowRedBytesOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 18),
    _EtpDiscardYellowRedBytesOverflow_Type()
)
etpDiscardYellowRedBytesOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etpDiscardYellowRedBytesOverflow.setStatus("current")


class _EtpStatClearCounters_Type(Integer32):
    """Custom type etpStatClearCounters based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_EtpStatClearCounters_Type.__name__ = "Integer32"
_EtpStatClearCounters_Object = MibTableColumn
etpStatClearCounters = _EtpStatClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 3, 1, 19),
    _EtpStatClearCounters_Type()
)
etpStatClearCounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etpStatClearCounters.setStatus("current")

# Managed Objects groups


# Notification objects

etpPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 9, 0, 1)
)
etpPortDown.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("RAD-Etp-MIB", "etpName"))
)
if mibBuilder.loadTexts:
    etpPortDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-Etp-MIB",
    **{"etp": etp,
       "etpEvents": etpEvents,
       "etpPortDown": etpPortDown,
       "etpTable": etpTable,
       "etpEntry": etpEntry,
       "etpIdx": etpIdx,
       "etpRowStatus": etpRowStatus,
       "etpName": etpName,
       "etpOperStatus": etpOperStatus,
       "etpClearStatCounters": etpClearStatCounters,
       "etpPortTable": etpPortTable,
       "etpPortEntry": etpPortEntry,
       "etpPortIfIndex": etpPortIfIndex,
       "etpPortRowStatus": etpPortRowStatus,
       "etpStatTable": etpStatTable,
       "etpStatEntry": etpStatEntry,
       "etpServiceIndex": etpServiceIndex,
       "etpStatDirection": etpStatDirection,
       "etpForwardGreenPackets": etpForwardGreenPackets,
       "etpForwardGreenPacketsOverflow": etpForwardGreenPacketsOverflow,
       "etpForwardYellowPackets": etpForwardYellowPackets,
       "etpForwardYellowPacketsOverflow": etpForwardYellowPacketsOverflow,
       "etpDiscardGreenPackets": etpDiscardGreenPackets,
       "etpDiscardGreenPacketsOverflow": etpDiscardGreenPacketsOverflow,
       "etpDiscardYellowRedPackets": etpDiscardYellowRedPackets,
       "etpDiscardYellowRedPacketsOverflow": etpDiscardYellowRedPacketsOverflow,
       "etpForwardGreenBytes": etpForwardGreenBytes,
       "etpForwardGreenBytesOverflow": etpForwardGreenBytesOverflow,
       "etpForwardYellowBytes": etpForwardYellowBytes,
       "etpForwardYellowBytesOverflow": etpForwardYellowBytesOverflow,
       "etpDiscardGreenBytes": etpDiscardGreenBytes,
       "etpDiscardGreenBytesOverflow": etpDiscardGreenBytesOverflow,
       "etpDiscardYellowRedBytes": etpDiscardYellowRedBytes,
       "etpDiscardYellowRedBytesOverflow": etpDiscardYellowRedBytesOverflow,
       "etpStatClearCounters": etpStatClearCounters}
)
