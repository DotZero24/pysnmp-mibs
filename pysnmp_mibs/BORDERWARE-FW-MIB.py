# SNMP MIB module (BORDERWARE-FW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/watchguard/BORDERWARE-FW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:17:37 2025
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

(bwProducts,) = mibBuilder.importSymbols(
    "BORDERWARE-MIB",
    "bwProducts")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

bwFirewall = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8673, 1, 1)
)
if mibBuilder.loadTexts:
    bwFirewall.setRevisions(
        ("2004-04-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BwFirewallConformance_ObjectIdentity = ObjectIdentity
bwFirewallConformance = _BwFirewallConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8673, 1, 1, 3)
)
_BwFirewallCompliances_ObjectIdentity = ObjectIdentity
bwFirewallCompliances = _BwFirewallCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8673, 1, 1, 3, 1)
)
_BwFirewallGroups_ObjectIdentity = ObjectIdentity
bwFirewallGroups = _BwFirewallGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8673, 1, 1, 3, 2)
)
_BwAlarm_ObjectIdentity = ObjectIdentity
bwAlarm = _BwAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8673, 1, 1, 100)
)
if mibBuilder.loadTexts:
    bwAlarm.setStatus("current")


class _AlTriggerAlarm_Type(Integer32):
    """Custom type alTriggerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlTriggerAlarm_Type.__name__ = "Integer32"
_AlTriggerAlarm_Object = MibScalar
alTriggerAlarm = _AlTriggerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 8673, 1, 1, 100, 1),
    _AlTriggerAlarm_Type()
)
alTriggerAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alTriggerAlarm.setStatus("current")
_AlLastChange_Type = DateAndTime
_AlLastChange_Object = MibScalar
alLastChange = _AlLastChange_Object(
    (1, 3, 6, 1, 4, 1, 8673, 1, 1, 100, 4),
    _AlLastChange_Type()
)
alLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLastChange.setStatus("current")


class _AlName_Type(DisplayString):
    """Custom type alName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlName_Type.__name__ = "DisplayString"
_AlName_Object = MibScalar
alName = _AlName_Object(
    (1, 3, 6, 1, 4, 1, 8673, 1, 1, 100, 9),
    _AlName_Type()
)
alName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alName.setStatus("current")
_AlRemoteIpAddr_Type = IpAddress
_AlRemoteIpAddr_Object = MibScalar
alRemoteIpAddr = _AlRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8673, 1, 1, 100, 10),
    _AlRemoteIpAddr_Type()
)
alRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRemoteIpAddr.setStatus("current")


class _AlDestPort_Type(Integer32):
    """Custom type alDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlDestPort_Type.__name__ = "Integer32"
_AlDestPort_Object = MibScalar
alDestPort = _AlDestPort_Object(
    (1, 3, 6, 1, 4, 1, 8673, 1, 1, 100, 15),
    _AlDestPort_Type()
)
alDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDestPort.setStatus("current")

# Managed Objects groups

bwAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8673, 1, 1, 3, 2, 1)
)
bwAlarmGroup.setObjects(
      *(("BORDERWARE-FW-MIB", "alTriggerAlarm"),
        ("BORDERWARE-FW-MIB", "alLastChange"),
        ("BORDERWARE-FW-MIB", "alName"),
        ("BORDERWARE-FW-MIB", "alRemoteIpAddr"),
        ("BORDERWARE-FW-MIB", "alDestPort"))
)
if mibBuilder.loadTexts:
    bwAlarmGroup.setStatus("current")


# Notification objects

alAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 8673, 1, 1, 100, 50)
)
alAlarm.setObjects(
      *(("BORDERWARE-FW-MIB", "alLastChange"),
        ("BORDERWARE-FW-MIB", "alName"),
        ("BORDERWARE-FW-MIB", "alRemoteIpAddr"),
        ("BORDERWARE-FW-MIB", "alDestPort"))
)
if mibBuilder.loadTexts:
    alAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

bwFirewallCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8673, 1, 1, 3, 1, 1)
)
bwFirewallCompliance.setObjects(
    ("BORDERWARE-FW-MIB", "bwAlarmGroup")
)
if mibBuilder.loadTexts:
    bwFirewallCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BORDERWARE-FW-MIB",
    **{"bwFirewall": bwFirewall,
       "bwFirewallConformance": bwFirewallConformance,
       "bwFirewallCompliances": bwFirewallCompliances,
       "bwFirewallCompliance": bwFirewallCompliance,
       "bwFirewallGroups": bwFirewallGroups,
       "bwAlarmGroup": bwAlarmGroup,
       "bwAlarm": bwAlarm,
       "alTriggerAlarm": alTriggerAlarm,
       "alLastChange": alLastChange,
       "alName": alName,
       "alRemoteIpAddr": alRemoteIpAddr,
       "alDestPort": alDestPort,
       "alAlarm": alAlarm}
)
