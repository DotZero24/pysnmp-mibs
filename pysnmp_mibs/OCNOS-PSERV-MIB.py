# SNMP MIB module (OCNOS-PSERV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ipinfusion/OCNOS-PSERV-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:34:16 2025
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

(CmmChassisObject,) = mibBuilder.importSymbols(
    "CMM-CHASSIS-MIB",
    "CmmChassisObject")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(ipi,) = mibBuilder.importSymbols(
    "OCNOS-IPI-MODULE-MIB",
    "ipi")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cmmSoftwareObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 4)
)
if mibBuilder.loadTexts:
    cmmSoftwareObjects.setRevisions(
        ("2018-04-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmmSoftwareObjectsNotificationsPrefix_ObjectIdentity = ObjectIdentity
cmmSoftwareObjectsNotificationsPrefix = _CmmSoftwareObjectsNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 4, 0)
)


class _CmmSoftwareProcessKeepaliveTime_Type(Unsigned32):
    """Custom type cmmSoftwareProcessKeepaliveTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1800),
    )


_CmmSoftwareProcessKeepaliveTime_Type.__name__ = "Unsigned32"
_CmmSoftwareProcessKeepaliveTime_Object = MibScalar
cmmSoftwareProcessKeepaliveTime = _CmmSoftwareProcessKeepaliveTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 4, 1),
    _CmmSoftwareProcessKeepaliveTime_Type()
)
cmmSoftwareProcessKeepaliveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSoftwareProcessKeepaliveTime.setStatus("current")


class _CmmSoftwareProcessWatchdogStatus_Type(Integer32):
    """Custom type cmmSoftwareProcessWatchdogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CmmSoftwareProcessWatchdogStatus_Type.__name__ = "Integer32"
_CmmSoftwareProcessWatchdogStatus_Object = MibScalar
cmmSoftwareProcessWatchdogStatus = _CmmSoftwareProcessWatchdogStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 4, 2),
    _CmmSoftwareProcessWatchdogStatus_Type()
)
cmmSoftwareProcessWatchdogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSoftwareProcessWatchdogStatus.setStatus("current")


class _CmmSoftwareProcessStatus_Type(Integer32):
    """Custom type cmmSoftwareProcessStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CmmSoftwareProcessStatus_Type.__name__ = "Integer32"
_CmmSoftwareProcessStatus_Object = MibScalar
cmmSoftwareProcessStatus = _CmmSoftwareProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 4, 3),
    _CmmSoftwareProcessStatus_Type()
)
cmmSoftwareProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSoftwareProcessStatus.setStatus("current")
_CmmSoftwareProcessObjectsTable_Object = MibTable
cmmSoftwareProcessObjectsTable = _CmmSoftwareProcessObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cmmSoftwareProcessObjectsTable.setStatus("current")
_CmmSoftwareProcessObjectsEntry_Object = MibTableRow
cmmSoftwareProcessObjectsEntry = _CmmSoftwareProcessObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 4, 4, 1)
)
cmmSoftwareProcessObjectsEntry.setIndexNames(
    (0, "OCNOS-PSERV-MIB", "cmmSoftwareProcessID"),
)
if mibBuilder.loadTexts:
    cmmSoftwareProcessObjectsEntry.setStatus("current")
_CmmSoftwareProcessID_Type = Unsigned32
_CmmSoftwareProcessID_Object = MibTableColumn
cmmSoftwareProcessID = _CmmSoftwareProcessID_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 4, 4, 1, 1),
    _CmmSoftwareProcessID_Type()
)
cmmSoftwareProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSoftwareProcessID.setStatus("current")
_CmmSoftwareProcessName_Type = OctetString
_CmmSoftwareProcessName_Object = MibTableColumn
cmmSoftwareProcessName = _CmmSoftwareProcessName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 4, 4, 1, 2),
    _CmmSoftwareProcessName_Type()
)
cmmSoftwareProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSoftwareProcessName.setStatus("current")


class _CmmSoftwareProcessState_Type(Integer32):
    """Custom type cmmSoftwareProcessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notrunning", 0),
          ("running", 1))
    )


_CmmSoftwareProcessState_Type.__name__ = "Integer32"
_CmmSoftwareProcessState_Object = MibTableColumn
cmmSoftwareProcessState = _CmmSoftwareProcessState_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 4, 4, 1, 3),
    _CmmSoftwareProcessState_Type()
)
cmmSoftwareProcessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSoftwareProcessState.setStatus("current")
_CmmSoftwareProcessStartTime_Type = DateAndTime
_CmmSoftwareProcessStartTime_Object = MibTableColumn
cmmSoftwareProcessStartTime = _CmmSoftwareProcessStartTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 4, 4, 1, 4),
    _CmmSoftwareProcessStartTime_Type()
)
cmmSoftwareProcessStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSoftwareProcessStartTime.setStatus("current")
_CmmSoftwareProcessLastRestartReason_Type = OctetString
_CmmSoftwareProcessLastRestartReason_Object = MibTableColumn
cmmSoftwareProcessLastRestartReason = _CmmSoftwareProcessLastRestartReason_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 4, 4, 1, 5),
    _CmmSoftwareProcessLastRestartReason_Type()
)
cmmSoftwareProcessLastRestartReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSoftwareProcessLastRestartReason.setStatus("current")

# Managed Objects groups


# Notification objects

cmmSysPsDownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 4, 0, 1)
)
cmmSysPsDownNotification.setObjects(
      *(("OCNOS-PSERV-MIB", "cmmSoftwareProcessID"),
        ("OCNOS-PSERV-MIB", "cmmSoftwareProcessName"),
        ("OCNOS-PSERV-MIB", "cmmSoftwareProcessStartTime"),
        ("OCNOS-PSERV-MIB", "cmmSoftwareProcessLastRestartReason"))
)
if mibBuilder.loadTexts:
    cmmSysPsDownNotification.setStatus(
        "current"
    )

cmmSysPsRestartNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 4, 0, 2)
)
cmmSysPsRestartNotification.setObjects(
      *(("OCNOS-PSERV-MIB", "cmmSoftwareProcessID"),
        ("OCNOS-PSERV-MIB", "cmmSoftwareProcessName"),
        ("OCNOS-PSERV-MIB", "cmmSoftwareProcessStartTime"))
)
if mibBuilder.loadTexts:
    cmmSysPsRestartNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OCNOS-PSERV-MIB",
    **{"cmmSoftwareObjects": cmmSoftwareObjects,
       "cmmSoftwareObjectsNotificationsPrefix": cmmSoftwareObjectsNotificationsPrefix,
       "cmmSysPsDownNotification": cmmSysPsDownNotification,
       "cmmSysPsRestartNotification": cmmSysPsRestartNotification,
       "cmmSoftwareProcessKeepaliveTime": cmmSoftwareProcessKeepaliveTime,
       "cmmSoftwareProcessWatchdogStatus": cmmSoftwareProcessWatchdogStatus,
       "cmmSoftwareProcessStatus": cmmSoftwareProcessStatus,
       "cmmSoftwareProcessObjectsTable": cmmSoftwareProcessObjectsTable,
       "cmmSoftwareProcessObjectsEntry": cmmSoftwareProcessObjectsEntry,
       "cmmSoftwareProcessID": cmmSoftwareProcessID,
       "cmmSoftwareProcessName": cmmSoftwareProcessName,
       "cmmSoftwareProcessState": cmmSoftwareProcessState,
       "cmmSoftwareProcessStartTime": cmmSoftwareProcessStartTime,
       "cmmSoftwareProcessLastRestartReason": cmmSoftwareProcessLastRestartReason}
)
