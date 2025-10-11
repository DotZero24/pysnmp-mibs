# SNMP MIB module (FS-TRAFFIC-CTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-TRAFFIC-CTRL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:31 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "FS-TC",
    "IfIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

fsTrafficCtrlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14)
)
if mibBuilder.loadTexts:
    fsTrafficCtrlMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Percent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



# MIB Managed Objects in the order of their OIDs

_FsTrafficCtrlMIBObjects_ObjectIdentity = ObjectIdentity
fsTrafficCtrlMIBObjects = _FsTrafficCtrlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1)
)
_FsPtTrafficCtrlTable_Object = MibTable
fsPtTrafficCtrlTable = _FsPtTrafficCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    fsPtTrafficCtrlTable.setStatus("current")
_FsPtTrafficCtrlEntry_Object = MibTableRow
fsPtTrafficCtrlEntry = _FsPtTrafficCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1, 1)
)
fsPtTrafficCtrlEntry.setIndexNames(
    (0, "FS-TRAFFIC-CTRL-MIB", "fsPtTrafficCtrlIfIndex"),
)
if mibBuilder.loadTexts:
    fsPtTrafficCtrlEntry.setStatus("current")
_FsPtTrafficCtrlIfIndex_Type = IfIndex
_FsPtTrafficCtrlIfIndex_Object = MibTableColumn
fsPtTrafficCtrlIfIndex = _FsPtTrafficCtrlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1, 1, 1),
    _FsPtTrafficCtrlIfIndex_Type()
)
fsPtTrafficCtrlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPtTrafficCtrlIfIndex.setStatus("current")


class _FsPtProtectedPortStatus_Type(EnabledStatus):
    """Custom type fsPtProtectedPortStatus based on EnabledStatus"""
    defaultValue = 2


_FsPtProtectedPortStatus_Type.__name__ = "EnabledStatus"
_FsPtProtectedPortStatus_Object = MibTableColumn
fsPtProtectedPortStatus = _FsPtProtectedPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1, 1, 2),
    _FsPtProtectedPortStatus_Type()
)
fsPtProtectedPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtProtectedPortStatus.setStatus("current")
_FsPtBroadcastStormControlStatus_Type = EnabledStatus
_FsPtBroadcastStormControlStatus_Object = MibTableColumn
fsPtBroadcastStormControlStatus = _FsPtBroadcastStormControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1, 1, 3),
    _FsPtBroadcastStormControlStatus_Type()
)
fsPtBroadcastStormControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtBroadcastStormControlStatus.setStatus("current")
_FsPtMulticastStormControlStatus_Type = EnabledStatus
_FsPtMulticastStormControlStatus_Object = MibTableColumn
fsPtMulticastStormControlStatus = _FsPtMulticastStormControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1, 1, 4),
    _FsPtMulticastStormControlStatus_Type()
)
fsPtMulticastStormControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtMulticastStormControlStatus.setStatus("current")
_FsPtUnicastStormControlStatus_Type = EnabledStatus
_FsPtUnicastStormControlStatus_Object = MibTableColumn
fsPtUnicastStormControlStatus = _FsPtUnicastStormControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1, 1, 5),
    _FsPtUnicastStormControlStatus_Type()
)
fsPtUnicastStormControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtUnicastStormControlStatus.setStatus("current")


class _FsPtBroadcastStormControlLevel_Type(Percent):
    """Custom type fsPtBroadcastStormControlLevel based on Percent"""
    defaultValue = 10


_FsPtBroadcastStormControlLevel_Type.__name__ = "Percent"
_FsPtBroadcastStormControlLevel_Object = MibTableColumn
fsPtBroadcastStormControlLevel = _FsPtBroadcastStormControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1, 1, 6),
    _FsPtBroadcastStormControlLevel_Type()
)
fsPtBroadcastStormControlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtBroadcastStormControlLevel.setStatus("current")


class _FsPtMulticastStormControlLevel_Type(Percent):
    """Custom type fsPtMulticastStormControlLevel based on Percent"""
    defaultValue = 10


_FsPtMulticastStormControlLevel_Type.__name__ = "Percent"
_FsPtMulticastStormControlLevel_Object = MibTableColumn
fsPtMulticastStormControlLevel = _FsPtMulticastStormControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1, 1, 7),
    _FsPtMulticastStormControlLevel_Type()
)
fsPtMulticastStormControlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtMulticastStormControlLevel.setStatus("current")


class _FsPtUnicastStormControlLevel_Type(Percent):
    """Custom type fsPtUnicastStormControlLevel based on Percent"""
    defaultValue = 10


_FsPtUnicastStormControlLevel_Type.__name__ = "Percent"
_FsPtUnicastStormControlLevel_Object = MibTableColumn
fsPtUnicastStormControlLevel = _FsPtUnicastStormControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1, 1, 8),
    _FsPtUnicastStormControlLevel_Type()
)
fsPtUnicastStormControlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPtUnicastStormControlLevel.setStatus("current")
_FsPtTrafficCtrlTraps_ObjectIdentity = ObjectIdentity
fsPtTrafficCtrlTraps = _FsPtTrafficCtrlTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 2)
)


class _StormViolationAlarmType_Type(Integer32):
    """Custom type stormViolationAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("broadcast", 2),
          ("mutlicast", 3),
          ("unicast", 4))
    )


_StormViolationAlarmType_Type.__name__ = "Integer32"
_StormViolationAlarmType_Object = MibScalar
stormViolationAlarmType = _StormViolationAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 2, 1),
    _StormViolationAlarmType_Type()
)
stormViolationAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stormViolationAlarmType.setStatus("current")
_FsPtTrafficCtrlMIBConformance_ObjectIdentity = ObjectIdentity
fsPtTrafficCtrlMIBConformance = _FsPtTrafficCtrlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 3)
)
_FsPtTrafficCtrlMIBCompliances_ObjectIdentity = ObjectIdentity
fsPtTrafficCtrlMIBCompliances = _FsPtTrafficCtrlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 3, 1)
)
_FsPtTrafficCtrlMIBGroups_ObjectIdentity = ObjectIdentity
fsPtTrafficCtrlMIBGroups = _FsPtTrafficCtrlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 3, 2)
)

# Managed Objects groups

fsPtTrafficCtrlMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 3, 2, 1)
)
fsPtTrafficCtrlMIBGroup.setObjects(
      *(("FS-TRAFFIC-CTRL-MIB", "fsPtTrafficCtrlIfIndex"),
        ("FS-TRAFFIC-CTRL-MIB", "fsPtProtectedPortStatus"),
        ("FS-TRAFFIC-CTRL-MIB", "fsPtBroadcastStormControlStatus"),
        ("FS-TRAFFIC-CTRL-MIB", "fsPtMulticastStormControlStatus"),
        ("FS-TRAFFIC-CTRL-MIB", "fsPtUnicastStormControlStatus"),
        ("FS-TRAFFIC-CTRL-MIB", "fsPtBroadcastStormControlLevel"),
        ("FS-TRAFFIC-CTRL-MIB", "fsPtMulticastStormControlLevel"),
        ("FS-TRAFFIC-CTRL-MIB", "fsPtUnicastStormControlLevel"))
)
if mibBuilder.loadTexts:
    fsPtTrafficCtrlMIBGroup.setStatus("current")


# Notification objects

stormViolationAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 2, 2)
)
stormViolationAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FS-TRAFFIC-CTRL-MIB", "stormViolationAlarmType"))
)
if mibBuilder.loadTexts:
    stormViolationAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

fsPtTrafficCtrlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 3, 1, 1)
)
fsPtTrafficCtrlMIBCompliance.setObjects(
    ("FS-TRAFFIC-CTRL-MIB", "fsPtTrafficCtrlMIBGroup")
)
if mibBuilder.loadTexts:
    fsPtTrafficCtrlMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-TRAFFIC-CTRL-MIB",
    **{"Percent": Percent,
       "fsTrafficCtrlMIB": fsTrafficCtrlMIB,
       "fsTrafficCtrlMIBObjects": fsTrafficCtrlMIBObjects,
       "fsPtTrafficCtrlTable": fsPtTrafficCtrlTable,
       "fsPtTrafficCtrlEntry": fsPtTrafficCtrlEntry,
       "fsPtTrafficCtrlIfIndex": fsPtTrafficCtrlIfIndex,
       "fsPtProtectedPortStatus": fsPtProtectedPortStatus,
       "fsPtBroadcastStormControlStatus": fsPtBroadcastStormControlStatus,
       "fsPtMulticastStormControlStatus": fsPtMulticastStormControlStatus,
       "fsPtUnicastStormControlStatus": fsPtUnicastStormControlStatus,
       "fsPtBroadcastStormControlLevel": fsPtBroadcastStormControlLevel,
       "fsPtMulticastStormControlLevel": fsPtMulticastStormControlLevel,
       "fsPtUnicastStormControlLevel": fsPtUnicastStormControlLevel,
       "fsPtTrafficCtrlTraps": fsPtTrafficCtrlTraps,
       "stormViolationAlarmType": stormViolationAlarmType,
       "stormViolationAlarm": stormViolationAlarm,
       "fsPtTrafficCtrlMIBConformance": fsPtTrafficCtrlMIBConformance,
       "fsPtTrafficCtrlMIBCompliances": fsPtTrafficCtrlMIBCompliances,
       "fsPtTrafficCtrlMIBCompliance": fsPtTrafficCtrlMIBCompliance,
       "fsPtTrafficCtrlMIBGroups": fsPtTrafficCtrlMIBGroups,
       "fsPtTrafficCtrlMIBGroup": fsPtTrafficCtrlMIBGroup}
)
