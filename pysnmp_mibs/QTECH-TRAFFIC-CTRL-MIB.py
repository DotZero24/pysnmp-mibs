# SNMP MIB module (QTECH-TRAFFIC-CTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-TRAFFIC-CTRL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:56:40 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "QTECH-TC",
    "IfIndex")

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

qtechTrafficCtrlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14)
)
if mibBuilder.loadTexts:
    qtechTrafficCtrlMIB.setRevisions(
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

_QtechTrafficCtrlMIBObjects_ObjectIdentity = ObjectIdentity
qtechTrafficCtrlMIBObjects = _QtechTrafficCtrlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1)
)
_QtechPtTrafficCtrlTable_Object = MibTable
qtechPtTrafficCtrlTable = _QtechPtTrafficCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    qtechPtTrafficCtrlTable.setStatus("current")
_QtechPtTrafficCtrlEntry_Object = MibTableRow
qtechPtTrafficCtrlEntry = _QtechPtTrafficCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1, 1)
)
qtechPtTrafficCtrlEntry.setIndexNames(
    (0, "QTECH-TRAFFIC-CTRL-MIB", "qtechPtTrafficCtrlIfIndex"),
)
if mibBuilder.loadTexts:
    qtechPtTrafficCtrlEntry.setStatus("current")
_QtechPtTrafficCtrlIfIndex_Type = IfIndex
_QtechPtTrafficCtrlIfIndex_Object = MibTableColumn
qtechPtTrafficCtrlIfIndex = _QtechPtTrafficCtrlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1, 1, 1),
    _QtechPtTrafficCtrlIfIndex_Type()
)
qtechPtTrafficCtrlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPtTrafficCtrlIfIndex.setStatus("current")


class _QtechPtProtectedPortStatus_Type(EnabledStatus):
    """Custom type qtechPtProtectedPortStatus based on EnabledStatus"""
    defaultValue = 2


_QtechPtProtectedPortStatus_Type.__name__ = "EnabledStatus"
_QtechPtProtectedPortStatus_Object = MibTableColumn
qtechPtProtectedPortStatus = _QtechPtProtectedPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1, 1, 2),
    _QtechPtProtectedPortStatus_Type()
)
qtechPtProtectedPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPtProtectedPortStatus.setStatus("current")
_QtechPtBroadcastStormControlStatus_Type = EnabledStatus
_QtechPtBroadcastStormControlStatus_Object = MibTableColumn
qtechPtBroadcastStormControlStatus = _QtechPtBroadcastStormControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1, 1, 3),
    _QtechPtBroadcastStormControlStatus_Type()
)
qtechPtBroadcastStormControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPtBroadcastStormControlStatus.setStatus("current")
_QtechPtMulticastStormControlStatus_Type = EnabledStatus
_QtechPtMulticastStormControlStatus_Object = MibTableColumn
qtechPtMulticastStormControlStatus = _QtechPtMulticastStormControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1, 1, 4),
    _QtechPtMulticastStormControlStatus_Type()
)
qtechPtMulticastStormControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPtMulticastStormControlStatus.setStatus("current")
_QtechPtUnicastStormControlStatus_Type = EnabledStatus
_QtechPtUnicastStormControlStatus_Object = MibTableColumn
qtechPtUnicastStormControlStatus = _QtechPtUnicastStormControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1, 1, 5),
    _QtechPtUnicastStormControlStatus_Type()
)
qtechPtUnicastStormControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPtUnicastStormControlStatus.setStatus("current")


class _QtechPtBroadcastStormControlLevel_Type(Percent):
    """Custom type qtechPtBroadcastStormControlLevel based on Percent"""
    defaultValue = 10


_QtechPtBroadcastStormControlLevel_Type.__name__ = "Percent"
_QtechPtBroadcastStormControlLevel_Object = MibTableColumn
qtechPtBroadcastStormControlLevel = _QtechPtBroadcastStormControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1, 1, 6),
    _QtechPtBroadcastStormControlLevel_Type()
)
qtechPtBroadcastStormControlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPtBroadcastStormControlLevel.setStatus("current")


class _QtechPtMulticastStormControlLevel_Type(Percent):
    """Custom type qtechPtMulticastStormControlLevel based on Percent"""
    defaultValue = 10


_QtechPtMulticastStormControlLevel_Type.__name__ = "Percent"
_QtechPtMulticastStormControlLevel_Object = MibTableColumn
qtechPtMulticastStormControlLevel = _QtechPtMulticastStormControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1, 1, 7),
    _QtechPtMulticastStormControlLevel_Type()
)
qtechPtMulticastStormControlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPtMulticastStormControlLevel.setStatus("current")


class _QtechPtUnicastStormControlLevel_Type(Percent):
    """Custom type qtechPtUnicastStormControlLevel based on Percent"""
    defaultValue = 10


_QtechPtUnicastStormControlLevel_Type.__name__ = "Percent"
_QtechPtUnicastStormControlLevel_Object = MibTableColumn
qtechPtUnicastStormControlLevel = _QtechPtUnicastStormControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1, 1, 8),
    _QtechPtUnicastStormControlLevel_Type()
)
qtechPtUnicastStormControlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPtUnicastStormControlLevel.setStatus("current")
_QtechPtTrafficCtrlTraps_ObjectIdentity = ObjectIdentity
qtechPtTrafficCtrlTraps = _QtechPtTrafficCtrlTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 2)
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
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 2, 1),
    _StormViolationAlarmType_Type()
)
stormViolationAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stormViolationAlarmType.setStatus("current")
_QtechPtTrafficCtrlMIBConformance_ObjectIdentity = ObjectIdentity
qtechPtTrafficCtrlMIBConformance = _QtechPtTrafficCtrlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 3)
)
_QtechPtTrafficCtrlMIBCompliances_ObjectIdentity = ObjectIdentity
qtechPtTrafficCtrlMIBCompliances = _QtechPtTrafficCtrlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 3, 1)
)
_QtechPtTrafficCtrlMIBGroups_ObjectIdentity = ObjectIdentity
qtechPtTrafficCtrlMIBGroups = _QtechPtTrafficCtrlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 3, 2)
)

# Managed Objects groups

qtechPtTrafficCtrlMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 3, 2, 1)
)
qtechPtTrafficCtrlMIBGroup.setObjects(
      *(("QTECH-TRAFFIC-CTRL-MIB", "qtechPtTrafficCtrlIfIndex"),
        ("QTECH-TRAFFIC-CTRL-MIB", "qtechPtProtectedPortStatus"),
        ("QTECH-TRAFFIC-CTRL-MIB", "qtechPtBroadcastStormControlStatus"),
        ("QTECH-TRAFFIC-CTRL-MIB", "qtechPtMulticastStormControlStatus"),
        ("QTECH-TRAFFIC-CTRL-MIB", "qtechPtUnicastStormControlStatus"),
        ("QTECH-TRAFFIC-CTRL-MIB", "qtechPtBroadcastStormControlLevel"),
        ("QTECH-TRAFFIC-CTRL-MIB", "qtechPtMulticastStormControlLevel"),
        ("QTECH-TRAFFIC-CTRL-MIB", "qtechPtUnicastStormControlLevel"))
)
if mibBuilder.loadTexts:
    qtechPtTrafficCtrlMIBGroup.setStatus("current")


# Notification objects

stormViolationAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 2, 2)
)
stormViolationAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("QTECH-TRAFFIC-CTRL-MIB", "stormViolationAlarmType"))
)
if mibBuilder.loadTexts:
    stormViolationAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qtechPtTrafficCtrlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 3, 1, 1)
)
qtechPtTrafficCtrlMIBCompliance.setObjects(
    ("QTECH-TRAFFIC-CTRL-MIB", "qtechPtTrafficCtrlMIBGroup")
)
if mibBuilder.loadTexts:
    qtechPtTrafficCtrlMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-TRAFFIC-CTRL-MIB",
    **{"Percent": Percent,
       "qtechTrafficCtrlMIB": qtechTrafficCtrlMIB,
       "qtechTrafficCtrlMIBObjects": qtechTrafficCtrlMIBObjects,
       "qtechPtTrafficCtrlTable": qtechPtTrafficCtrlTable,
       "qtechPtTrafficCtrlEntry": qtechPtTrafficCtrlEntry,
       "qtechPtTrafficCtrlIfIndex": qtechPtTrafficCtrlIfIndex,
       "qtechPtProtectedPortStatus": qtechPtProtectedPortStatus,
       "qtechPtBroadcastStormControlStatus": qtechPtBroadcastStormControlStatus,
       "qtechPtMulticastStormControlStatus": qtechPtMulticastStormControlStatus,
       "qtechPtUnicastStormControlStatus": qtechPtUnicastStormControlStatus,
       "qtechPtBroadcastStormControlLevel": qtechPtBroadcastStormControlLevel,
       "qtechPtMulticastStormControlLevel": qtechPtMulticastStormControlLevel,
       "qtechPtUnicastStormControlLevel": qtechPtUnicastStormControlLevel,
       "qtechPtTrafficCtrlTraps": qtechPtTrafficCtrlTraps,
       "stormViolationAlarmType": stormViolationAlarmType,
       "stormViolationAlarm": stormViolationAlarm,
       "qtechPtTrafficCtrlMIBConformance": qtechPtTrafficCtrlMIBConformance,
       "qtechPtTrafficCtrlMIBCompliances": qtechPtTrafficCtrlMIBCompliances,
       "qtechPtTrafficCtrlMIBCompliance": qtechPtTrafficCtrlMIBCompliance,
       "qtechPtTrafficCtrlMIBGroups": qtechPtTrafficCtrlMIBGroups,
       "qtechPtTrafficCtrlMIBGroup": qtechPtTrafficCtrlMIBGroup}
)
