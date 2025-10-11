# SNMP MIB module (H3C-SECHIGH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-SECHIGH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:18:25 2025
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

h3cSecHigh = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 171)
)
if mibBuilder.loadTexts:
    h3cSecHigh.setRevisions(
        ("2017-09-16 20:20",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cSecHighMonitor_ObjectIdentity = ObjectIdentity
h3cSecHighMonitor = _H3cSecHighMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 171, 1)
)
_H3cSecHighHgMonitorAlarmVar_ObjectIdentity = ObjectIdentity
h3cSecHighHgMonitorAlarmVar = _H3cSecHighHgMonitorAlarmVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 171, 1, 1)
)
_H3cSecHighHgMonitorAlarmType_Type = Integer32
_H3cSecHighHgMonitorAlarmType_Object = MibScalar
h3cSecHighHgMonitorAlarmType = _H3cSecHighHgMonitorAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 171, 1, 1, 1),
    _H3cSecHighHgMonitorAlarmType_Type()
)
h3cSecHighHgMonitorAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSecHighHgMonitorAlarmType.setStatus("current")
_H3cSecHighHgMonitorAlarmSrcChassis_Type = Integer32
_H3cSecHighHgMonitorAlarmSrcChassis_Object = MibScalar
h3cSecHighHgMonitorAlarmSrcChassis = _H3cSecHighHgMonitorAlarmSrcChassis_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 171, 1, 1, 2),
    _H3cSecHighHgMonitorAlarmSrcChassis_Type()
)
h3cSecHighHgMonitorAlarmSrcChassis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSecHighHgMonitorAlarmSrcChassis.setStatus("current")
_H3cSecHighHgMonitorAlarmSrcSlot_Type = Integer32
_H3cSecHighHgMonitorAlarmSrcSlot_Object = MibScalar
h3cSecHighHgMonitorAlarmSrcSlot = _H3cSecHighHgMonitorAlarmSrcSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 171, 1, 1, 3),
    _H3cSecHighHgMonitorAlarmSrcSlot_Type()
)
h3cSecHighHgMonitorAlarmSrcSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSecHighHgMonitorAlarmSrcSlot.setStatus("current")
_H3cSecHighHgMonitorAlarmSrcChip_Type = Integer32
_H3cSecHighHgMonitorAlarmSrcChip_Object = MibScalar
h3cSecHighHgMonitorAlarmSrcChip = _H3cSecHighHgMonitorAlarmSrcChip_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 171, 1, 1, 4),
    _H3cSecHighHgMonitorAlarmSrcChip_Type()
)
h3cSecHighHgMonitorAlarmSrcChip.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSecHighHgMonitorAlarmSrcChip.setStatus("current")
_H3cSecHighHgMonitorAlarmSrcPort_Type = Integer32
_H3cSecHighHgMonitorAlarmSrcPort_Object = MibScalar
h3cSecHighHgMonitorAlarmSrcPort = _H3cSecHighHgMonitorAlarmSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 171, 1, 1, 5),
    _H3cSecHighHgMonitorAlarmSrcPort_Type()
)
h3cSecHighHgMonitorAlarmSrcPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSecHighHgMonitorAlarmSrcPort.setStatus("current")
_H3cSecHighHgMonitorAlarmDstChassis_Type = Integer32
_H3cSecHighHgMonitorAlarmDstChassis_Object = MibScalar
h3cSecHighHgMonitorAlarmDstChassis = _H3cSecHighHgMonitorAlarmDstChassis_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 171, 1, 1, 6),
    _H3cSecHighHgMonitorAlarmDstChassis_Type()
)
h3cSecHighHgMonitorAlarmDstChassis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSecHighHgMonitorAlarmDstChassis.setStatus("current")
_H3cSecHighHgMonitorAlarmDstSlot_Type = Integer32
_H3cSecHighHgMonitorAlarmDstSlot_Object = MibScalar
h3cSecHighHgMonitorAlarmDstSlot = _H3cSecHighHgMonitorAlarmDstSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 171, 1, 1, 7),
    _H3cSecHighHgMonitorAlarmDstSlot_Type()
)
h3cSecHighHgMonitorAlarmDstSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSecHighHgMonitorAlarmDstSlot.setStatus("current")
_H3cSecHighHgMonitorAlarmDstChip_Type = Integer32
_H3cSecHighHgMonitorAlarmDstChip_Object = MibScalar
h3cSecHighHgMonitorAlarmDstChip = _H3cSecHighHgMonitorAlarmDstChip_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 171, 1, 1, 8),
    _H3cSecHighHgMonitorAlarmDstChip_Type()
)
h3cSecHighHgMonitorAlarmDstChip.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSecHighHgMonitorAlarmDstChip.setStatus("current")
_H3cSecHighHgMonitorAlarmDstPort_Type = Integer32
_H3cSecHighHgMonitorAlarmDstPort_Object = MibScalar
h3cSecHighHgMonitorAlarmDstPort = _H3cSecHighHgMonitorAlarmDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 171, 1, 1, 9),
    _H3cSecHighHgMonitorAlarmDstPort_Type()
)
h3cSecHighHgMonitorAlarmDstPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSecHighHgMonitorAlarmDstPort.setStatus("current")


class _H3cSecHighHgMonitorAlarmReason_Type(OctetString):
    """Custom type h3cSecHighHgMonitorAlarmReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_H3cSecHighHgMonitorAlarmReason_Type.__name__ = "OctetString"
_H3cSecHighHgMonitorAlarmReason_Object = MibScalar
h3cSecHighHgMonitorAlarmReason = _H3cSecHighHgMonitorAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 171, 1, 1, 10),
    _H3cSecHighHgMonitorAlarmReason_Type()
)
h3cSecHighHgMonitorAlarmReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSecHighHgMonitorAlarmReason.setStatus("current")
_H3cSecHighHgMonitorAlarmTrap_ObjectIdentity = ObjectIdentity
h3cSecHighHgMonitorAlarmTrap = _H3cSecHighHgMonitorAlarmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 171, 1, 2)
)
_H3cSecHighHgMonitorAlarmNotifications_ObjectIdentity = ObjectIdentity
h3cSecHighHgMonitorAlarmNotifications = _H3cSecHighHgMonitorAlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 171, 1, 2, 0)
)

# Managed Objects groups


# Notification objects

h3cSecHighHgMonitorAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 171, 1, 2, 0, 1)
)
h3cSecHighHgMonitorAlarmNotification.setObjects(
      *(("H3C-SECHIGH-MIB", "h3cSecHighHgMonitorAlarmType"),
        ("H3C-SECHIGH-MIB", "h3cSecHighHgMonitorAlarmSrcChassis"),
        ("H3C-SECHIGH-MIB", "h3cSecHighHgMonitorAlarmSrcSlot"),
        ("H3C-SECHIGH-MIB", "h3cSecHighHgMonitorAlarmSrcChip"),
        ("H3C-SECHIGH-MIB", "h3cSecHighHgMonitorAlarmSrcPort"),
        ("H3C-SECHIGH-MIB", "h3cSecHighHgMonitorAlarmDstChassis"),
        ("H3C-SECHIGH-MIB", "h3cSecHighHgMonitorAlarmDstSlot"),
        ("H3C-SECHIGH-MIB", "h3cSecHighHgMonitorAlarmDstChip"),
        ("H3C-SECHIGH-MIB", "h3cSecHighHgMonitorAlarmDstPort"),
        ("H3C-SECHIGH-MIB", "h3cSecHighHgMonitorAlarmReason"))
)
if mibBuilder.loadTexts:
    h3cSecHighHgMonitorAlarmNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-SECHIGH-MIB",
    **{"h3cSecHigh": h3cSecHigh,
       "h3cSecHighMonitor": h3cSecHighMonitor,
       "h3cSecHighHgMonitorAlarmVar": h3cSecHighHgMonitorAlarmVar,
       "h3cSecHighHgMonitorAlarmType": h3cSecHighHgMonitorAlarmType,
       "h3cSecHighHgMonitorAlarmSrcChassis": h3cSecHighHgMonitorAlarmSrcChassis,
       "h3cSecHighHgMonitorAlarmSrcSlot": h3cSecHighHgMonitorAlarmSrcSlot,
       "h3cSecHighHgMonitorAlarmSrcChip": h3cSecHighHgMonitorAlarmSrcChip,
       "h3cSecHighHgMonitorAlarmSrcPort": h3cSecHighHgMonitorAlarmSrcPort,
       "h3cSecHighHgMonitorAlarmDstChassis": h3cSecHighHgMonitorAlarmDstChassis,
       "h3cSecHighHgMonitorAlarmDstSlot": h3cSecHighHgMonitorAlarmDstSlot,
       "h3cSecHighHgMonitorAlarmDstChip": h3cSecHighHgMonitorAlarmDstChip,
       "h3cSecHighHgMonitorAlarmDstPort": h3cSecHighHgMonitorAlarmDstPort,
       "h3cSecHighHgMonitorAlarmReason": h3cSecHighHgMonitorAlarmReason,
       "h3cSecHighHgMonitorAlarmTrap": h3cSecHighHgMonitorAlarmTrap,
       "h3cSecHighHgMonitorAlarmNotifications": h3cSecHighHgMonitorAlarmNotifications,
       "h3cSecHighHgMonitorAlarmNotification": h3cSecHighHgMonitorAlarmNotification}
)
