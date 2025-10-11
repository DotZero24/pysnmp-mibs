# SNMP MIB module (ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:04 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysTxqMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99)
)
if mibBuilder.loadTexts:
    etsysTxqMonitorMIB.setRevisions(
        ("2013-02-25 16:27",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysTxqMonitorObjects_ObjectIdentity = ObjectIdentity
etsysTxqMonitorObjects = _EtsysTxqMonitorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1)
)
_EtsysTxqMonitorNotifications_ObjectIdentity = ObjectIdentity
etsysTxqMonitorNotifications = _EtsysTxqMonitorNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 0)
)
_EtsysTxqMonitor_ObjectIdentity = ObjectIdentity
etsysTxqMonitor = _EtsysTxqMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 1)
)


class _EtsysTxqMonitorDownTime_Type(Integer32):
    """Custom type etsysTxqMonitorDownTime based on Integer32"""
    defaultValue = 0


_EtsysTxqMonitorDownTime_Type.__name__ = "Integer32"
_EtsysTxqMonitorDownTime_Object = MibScalar
etsysTxqMonitorDownTime = _EtsysTxqMonitorDownTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 1, 1),
    _EtsysTxqMonitorDownTime_Type()
)
etsysTxqMonitorDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTxqMonitorDownTime.setStatus("current")


class _EtsysTxqMonitorIgnorePauseTime_Type(Integer32):
    """Custom type etsysTxqMonitorIgnorePauseTime based on Integer32"""
    defaultValue = 0


_EtsysTxqMonitorIgnorePauseTime_Type.__name__ = "Integer32"
_EtsysTxqMonitorIgnorePauseTime_Object = MibScalar
etsysTxqMonitorIgnorePauseTime = _EtsysTxqMonitorIgnorePauseTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 1, 2),
    _EtsysTxqMonitorIgnorePauseTime_Type()
)
etsysTxqMonitorIgnorePauseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTxqMonitorIgnorePauseTime.setStatus("current")


class _EtsysTxqMonitorMinRate_Type(Integer32):
    """Custom type etsysTxqMonitorMinRate based on Integer32"""
    defaultValue = 1


_EtsysTxqMonitorMinRate_Type.__name__ = "Integer32"
_EtsysTxqMonitorMinRate_Object = MibScalar
etsysTxqMonitorMinRate = _EtsysTxqMonitorMinRate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 1, 3),
    _EtsysTxqMonitorMinRate_Type()
)
etsysTxqMonitorMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTxqMonitorMinRate.setStatus("current")


class _EtsysTxqMonitorSampleInterval_Type(Integer32):
    """Custom type etsysTxqMonitorSampleInterval based on Integer32"""
    defaultValue = 1


_EtsysTxqMonitorSampleInterval_Type.__name__ = "Integer32"
_EtsysTxqMonitorSampleInterval_Object = MibScalar
etsysTxqMonitorSampleInterval = _EtsysTxqMonitorSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 1, 4),
    _EtsysTxqMonitorSampleInterval_Type()
)
etsysTxqMonitorSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTxqMonitorSampleInterval.setStatus("current")


class _EtsysTxqMonitorTrapStatus_Type(Integer32):
    """Custom type etsysTxqMonitorTrapStatus based on Integer32"""
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


_EtsysTxqMonitorTrapStatus_Type.__name__ = "Integer32"
_EtsysTxqMonitorTrapStatus_Object = MibScalar
etsysTxqMonitorTrapStatus = _EtsysTxqMonitorTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 1, 5),
    _EtsysTxqMonitorTrapStatus_Type()
)
etsysTxqMonitorTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTxqMonitorTrapStatus.setStatus("current")


class _EtsysTxqMonitorLoggingThreshold_Type(Integer32):
    """Custom type etsysTxqMonitorLoggingThreshold based on Integer32"""
    defaultValue = 2


_EtsysTxqMonitorLoggingThreshold_Type.__name__ = "Integer32"
_EtsysTxqMonitorLoggingThreshold_Object = MibScalar
etsysTxqMonitorLoggingThreshold = _EtsysTxqMonitorLoggingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 1, 6),
    _EtsysTxqMonitorLoggingThreshold_Type()
)
etsysTxqMonitorLoggingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTxqMonitorLoggingThreshold.setStatus("current")


class _EtsysTxqMonitorIgnorePauseThreshold_Type(Integer32):
    """Custom type etsysTxqMonitorIgnorePauseThreshold based on Integer32"""
    defaultValue = 5


_EtsysTxqMonitorIgnorePauseThreshold_Type.__name__ = "Integer32"
_EtsysTxqMonitorIgnorePauseThreshold_Object = MibScalar
etsysTxqMonitorIgnorePauseThreshold = _EtsysTxqMonitorIgnorePauseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 1, 7),
    _EtsysTxqMonitorIgnorePauseThreshold_Type()
)
etsysTxqMonitorIgnorePauseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTxqMonitorIgnorePauseThreshold.setStatus("current")


class _EtsysTxqMonitorDisablePortThreshold_Type(Integer32):
    """Custom type etsysTxqMonitorDisablePortThreshold based on Integer32"""
    defaultValue = 10


_EtsysTxqMonitorDisablePortThreshold_Type.__name__ = "Integer32"
_EtsysTxqMonitorDisablePortThreshold_Object = MibScalar
etsysTxqMonitorDisablePortThreshold = _EtsysTxqMonitorDisablePortThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 1, 8),
    _EtsysTxqMonitorDisablePortThreshold_Type()
)
etsysTxqMonitorDisablePortThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTxqMonitorDisablePortThreshold.setStatus("current")


class _EtsysTxqMonitorEnableState_Type(Integer32):
    """Custom type etsysTxqMonitorEnableState based on Integer32"""
    defaultValue = 1

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


_EtsysTxqMonitorEnableState_Type.__name__ = "Integer32"
_EtsysTxqMonitorEnableState_Object = MibScalar
etsysTxqMonitorEnableState = _EtsysTxqMonitorEnableState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 1, 9),
    _EtsysTxqMonitorEnableState_Type()
)
etsysTxqMonitorEnableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTxqMonitorEnableState.setStatus("current")
_EtsysTxqMonitorPort_ObjectIdentity = ObjectIdentity
etsysTxqMonitorPort = _EtsysTxqMonitorPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 2)
)
_EtsysTxqMonitorPortTable_Object = MibTable
etsysTxqMonitorPortTable = _EtsysTxqMonitorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysTxqMonitorPortTable.setStatus("current")
_EtsysTxqMonitorPortEntry_Object = MibTableRow
etsysTxqMonitorPortEntry = _EtsysTxqMonitorPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 2, 1, 1)
)
etsysTxqMonitorPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysTxqMonitorPortEntry.setStatus("current")
_EtsysTxqMonitorPortConsecutiveStalled_Type = Counter64
_EtsysTxqMonitorPortConsecutiveStalled_Object = MibTableColumn
etsysTxqMonitorPortConsecutiveStalled = _EtsysTxqMonitorPortConsecutiveStalled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 2, 1, 1, 1),
    _EtsysTxqMonitorPortConsecutiveStalled_Type()
)
etsysTxqMonitorPortConsecutiveStalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTxqMonitorPortConsecutiveStalled.setStatus("current")
_EtsysTxqMonitorPortTotalStalled_Type = Counter64
_EtsysTxqMonitorPortTotalStalled_Object = MibTableColumn
etsysTxqMonitorPortTotalStalled = _EtsysTxqMonitorPortTotalStalled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 2, 1, 1, 2),
    _EtsysTxqMonitorPortTotalStalled_Type()
)
etsysTxqMonitorPortTotalStalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTxqMonitorPortTotalStalled.setStatus("current")


class _EtsysTxqMonitorPortOperationalStatus_Type(Integer32):
    """Custom type etsysTxqMonitorPortOperationalStatus based on Integer32"""
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
        *(("disabled", 1),
          ("normal", 2),
          ("logging", 3),
          ("ignorePause", 4),
          ("down", 5))
    )


_EtsysTxqMonitorPortOperationalStatus_Type.__name__ = "Integer32"
_EtsysTxqMonitorPortOperationalStatus_Object = MibTableColumn
etsysTxqMonitorPortOperationalStatus = _EtsysTxqMonitorPortOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 2, 1, 1, 3),
    _EtsysTxqMonitorPortOperationalStatus_Type()
)
etsysTxqMonitorPortOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTxqMonitorPortOperationalStatus.setStatus("current")


class _EtsysTxqMonitorPortReset_Type(TruthValue):
    """Custom type etsysTxqMonitorPortReset based on TruthValue"""
    defaultValue = 2


_EtsysTxqMonitorPortReset_Type.__name__ = "TruthValue"
_EtsysTxqMonitorPortReset_Object = MibTableColumn
etsysTxqMonitorPortReset = _EtsysTxqMonitorPortReset_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 2, 1, 1, 4),
    _EtsysTxqMonitorPortReset_Type()
)
etsysTxqMonitorPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTxqMonitorPortReset.setStatus("current")


class _EtsysTxqMonitorPortCapabilities_Type(Bits):
    """Custom type etsysTxqMonitorPortCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("logging", 0),
          ("ignorePause", 1),
          ("down", 2))
    )

_EtsysTxqMonitorPortCapabilities_Type.__name__ = "Bits"
_EtsysTxqMonitorPortCapabilities_Object = MibTableColumn
etsysTxqMonitorPortCapabilities = _EtsysTxqMonitorPortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 2, 1, 1, 5),
    _EtsysTxqMonitorPortCapabilities_Type()
)
etsysTxqMonitorPortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTxqMonitorPortCapabilities.setStatus("current")
_EtsysTxqMonitorConformance_ObjectIdentity = ObjectIdentity
etsysTxqMonitorConformance = _EtsysTxqMonitorConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 2)
)
_EtsysTxqMonitorGroups_ObjectIdentity = ObjectIdentity
etsysTxqMonitorGroups = _EtsysTxqMonitorGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 2, 1)
)
_EtsysTxqMonitorCompliances_ObjectIdentity = ObjectIdentity
etsysTxqMonitorCompliances = _EtsysTxqMonitorCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 2, 2)
)

# Managed Objects groups

etsysTxqMonitorSettings = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 2, 1, 1)
)
etsysTxqMonitorSettings.setObjects(
      *(("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorDownTime"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorIgnorePauseTime"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorMinRate"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorSampleInterval"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorTrapStatus"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorLoggingThreshold"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorIgnorePauseThreshold"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorDisablePortThreshold"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorEnableState"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorPortConsecutiveStalled"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorPortTotalStalled"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorPortOperationalStatus"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorPortReset"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorPortCapabilities"))
)
if mibBuilder.loadTexts:
    etsysTxqMonitorSettings.setStatus("current")


# Notification objects

etsysTxqMonitorLoggingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 0, 1)
)
etsysTxqMonitorLoggingNotification.setObjects(
      *(("IF-MIB", "ifName"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorLoggingThreshold"))
)
if mibBuilder.loadTexts:
    etsysTxqMonitorLoggingNotification.setStatus(
        "current"
    )

etsysTxqMonitorIgnorePauseNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 0, 2)
)
etsysTxqMonitorIgnorePauseNotification.setObjects(
      *(("IF-MIB", "ifName"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorIgnorePauseThreshold"))
)
if mibBuilder.loadTexts:
    etsysTxqMonitorIgnorePauseNotification.setStatus(
        "current"
    )

etsysTxqMonitorDisablePortNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 1, 0, 3)
)
etsysTxqMonitorDisablePortNotification.setObjects(
      *(("IF-MIB", "ifName"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorDisablePortThreshold"))
)
if mibBuilder.loadTexts:
    etsysTxqMonitorDisablePortNotification.setStatus(
        "current"
    )


# Notifications groups

etsysTxqMonitorNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 2, 1, 2)
)
etsysTxqMonitorNotificationGroup.setObjects(
      *(("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorLoggingNotification"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorIgnorePauseNotification"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorDisablePortNotification"))
)
if mibBuilder.loadTexts:
    etsysTxqMonitorNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysTxqMonitorComplianceGroup = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99, 2, 2, 1)
)
etsysTxqMonitorComplianceGroup.setObjects(
      *(("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorSettings"),
        ("ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB", "etsysTxqMonitorNotificationGroup"))
)
if mibBuilder.loadTexts:
    etsysTxqMonitorComplianceGroup.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB",
    **{"etsysTxqMonitorMIB": etsysTxqMonitorMIB,
       "etsysTxqMonitorObjects": etsysTxqMonitorObjects,
       "etsysTxqMonitorNotifications": etsysTxqMonitorNotifications,
       "etsysTxqMonitorLoggingNotification": etsysTxqMonitorLoggingNotification,
       "etsysTxqMonitorIgnorePauseNotification": etsysTxqMonitorIgnorePauseNotification,
       "etsysTxqMonitorDisablePortNotification": etsysTxqMonitorDisablePortNotification,
       "etsysTxqMonitor": etsysTxqMonitor,
       "etsysTxqMonitorDownTime": etsysTxqMonitorDownTime,
       "etsysTxqMonitorIgnorePauseTime": etsysTxqMonitorIgnorePauseTime,
       "etsysTxqMonitorMinRate": etsysTxqMonitorMinRate,
       "etsysTxqMonitorSampleInterval": etsysTxqMonitorSampleInterval,
       "etsysTxqMonitorTrapStatus": etsysTxqMonitorTrapStatus,
       "etsysTxqMonitorLoggingThreshold": etsysTxqMonitorLoggingThreshold,
       "etsysTxqMonitorIgnorePauseThreshold": etsysTxqMonitorIgnorePauseThreshold,
       "etsysTxqMonitorDisablePortThreshold": etsysTxqMonitorDisablePortThreshold,
       "etsysTxqMonitorEnableState": etsysTxqMonitorEnableState,
       "etsysTxqMonitorPort": etsysTxqMonitorPort,
       "etsysTxqMonitorPortTable": etsysTxqMonitorPortTable,
       "etsysTxqMonitorPortEntry": etsysTxqMonitorPortEntry,
       "etsysTxqMonitorPortConsecutiveStalled": etsysTxqMonitorPortConsecutiveStalled,
       "etsysTxqMonitorPortTotalStalled": etsysTxqMonitorPortTotalStalled,
       "etsysTxqMonitorPortOperationalStatus": etsysTxqMonitorPortOperationalStatus,
       "etsysTxqMonitorPortReset": etsysTxqMonitorPortReset,
       "etsysTxqMonitorPortCapabilities": etsysTxqMonitorPortCapabilities,
       "etsysTxqMonitorConformance": etsysTxqMonitorConformance,
       "etsysTxqMonitorGroups": etsysTxqMonitorGroups,
       "etsysTxqMonitorSettings": etsysTxqMonitorSettings,
       "etsysTxqMonitorNotificationGroup": etsysTxqMonitorNotificationGroup,
       "etsysTxqMonitorCompliances": etsysTxqMonitorCompliances,
       "etsysTxqMonitorComplianceGroup": etsysTxqMonitorComplianceGroup}
)
