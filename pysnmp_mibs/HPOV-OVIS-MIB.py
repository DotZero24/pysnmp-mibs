# SNMP MIB module (HPOV-OVIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPOV-OVIS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:37:24 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hpOVInternetServices = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_OpenView_ObjectIdentity = ObjectIdentity
openView = _OpenView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 17)
)
_HpOVISTraps_ObjectIdentity = ObjectIdentity
hpOVISTraps = _HpOVISTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 16, 0)
)
_HpOVISTrapVars_ObjectIdentity = ObjectIdentity
hpOVISTrapVars = _HpOVISTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 16, 2)
)
_HpOVISTargetHost_Type = OctetString
_HpOVISTargetHost_Object = MibScalar
hpOVISTargetHost = _HpOVISTargetHost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 16, 2, 1),
    _HpOVISTargetHost_Type()
)
hpOVISTargetHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpOVISTargetHost.setStatus("current")
_HpOVISProbeSystem_Type = OctetString
_HpOVISProbeSystem_Object = MibScalar
hpOVISProbeSystem = _HpOVISProbeSystem_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 16, 2, 2),
    _HpOVISProbeSystem_Type()
)
hpOVISProbeSystem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpOVISProbeSystem.setStatus("current")
_HpOVISProbeType_Type = OctetString
_HpOVISProbeType_Object = MibScalar
hpOVISProbeType = _HpOVISProbeType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 16, 2, 3),
    _HpOVISProbeType_Type()
)
hpOVISProbeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpOVISProbeType.setStatus("current")
_HpOVISAlarmText_Type = OctetString
_HpOVISAlarmText_Object = MibScalar
hpOVISAlarmText = _HpOVISAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 16, 2, 4),
    _HpOVISAlarmText_Type()
)
hpOVISAlarmText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpOVISAlarmText.setStatus("current")
_HpOVISDrillDownUrl_Type = OctetString
_HpOVISDrillDownUrl_Object = MibScalar
hpOVISDrillDownUrl = _HpOVISDrillDownUrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 16, 2, 5),
    _HpOVISDrillDownUrl_Type()
)
hpOVISDrillDownUrl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpOVISDrillDownUrl.setStatus("current")

# Managed Objects groups


# Notification objects

hpOVISNormalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 16, 0, 1)
)
hpOVISNormalAlarm.setObjects(
      *(("HPOV-OVIS-MIB", "hpOVISTargetHost"),
        ("HPOV-OVIS-MIB", "hpOVISProbeSystem"),
        ("HPOV-OVIS-MIB", "hpOVISProbeType"),
        ("HPOV-OVIS-MIB", "hpOVISAlarmText"),
        ("HPOV-OVIS-MIB", "hpOVISDrillDownUrl"))
)
if mibBuilder.loadTexts:
    hpOVISNormalAlarm.setStatus(
        "current"
    )

hpOVISWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 16, 0, 2)
)
hpOVISWarningAlarm.setObjects(
      *(("HPOV-OVIS-MIB", "hpOVISTargetHost"),
        ("HPOV-OVIS-MIB", "hpOVISProbeSystem"),
        ("HPOV-OVIS-MIB", "hpOVISProbeType"),
        ("HPOV-OVIS-MIB", "hpOVISAlarmText"),
        ("HPOV-OVIS-MIB", "hpOVISDrillDownUrl"))
)
if mibBuilder.loadTexts:
    hpOVISWarningAlarm.setStatus(
        "current"
    )

hpOVISMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 16, 0, 3)
)
hpOVISMinorAlarm.setObjects(
      *(("HPOV-OVIS-MIB", "hpOVISTargetHost"),
        ("HPOV-OVIS-MIB", "hpOVISProbeSystem"),
        ("HPOV-OVIS-MIB", "hpOVISProbeType"),
        ("HPOV-OVIS-MIB", "hpOVISAlarmText"),
        ("HPOV-OVIS-MIB", "hpOVISDrillDownUrl"))
)
if mibBuilder.loadTexts:
    hpOVISMinorAlarm.setStatus(
        "current"
    )

hpOVISMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 16, 0, 4)
)
hpOVISMajorAlarm.setObjects(
      *(("HPOV-OVIS-MIB", "hpOVISTargetHost"),
        ("HPOV-OVIS-MIB", "hpOVISProbeSystem"),
        ("HPOV-OVIS-MIB", "hpOVISProbeType"),
        ("HPOV-OVIS-MIB", "hpOVISAlarmText"),
        ("HPOV-OVIS-MIB", "hpOVISDrillDownUrl"))
)
if mibBuilder.loadTexts:
    hpOVISMajorAlarm.setStatus(
        "current"
    )

hpOVISCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 16, 0, 5)
)
hpOVISCriticalAlarm.setObjects(
      *(("HPOV-OVIS-MIB", "hpOVISTargetHost"),
        ("HPOV-OVIS-MIB", "hpOVISProbeSystem"),
        ("HPOV-OVIS-MIB", "hpOVISProbeType"),
        ("HPOV-OVIS-MIB", "hpOVISAlarmText"),
        ("HPOV-OVIS-MIB", "hpOVISDrillDownUrl"))
)
if mibBuilder.loadTexts:
    hpOVISCriticalAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPOV-OVIS-MIB",
    **{"hp": hp,
       "nm": nm,
       "openView": openView,
       "hpOVInternetServices": hpOVInternetServices,
       "hpOVISTraps": hpOVISTraps,
       "hpOVISNormalAlarm": hpOVISNormalAlarm,
       "hpOVISWarningAlarm": hpOVISWarningAlarm,
       "hpOVISMinorAlarm": hpOVISMinorAlarm,
       "hpOVISMajorAlarm": hpOVISMajorAlarm,
       "hpOVISCriticalAlarm": hpOVISCriticalAlarm,
       "hpOVISTrapVars": hpOVISTrapVars,
       "hpOVISTargetHost": hpOVISTargetHost,
       "hpOVISProbeSystem": hpOVISProbeSystem,
       "hpOVISProbeType": hpOVISProbeType,
       "hpOVISAlarmText": hpOVISAlarmText,
       "hpOVISDrillDownUrl": hpOVISDrillDownUrl}
)
