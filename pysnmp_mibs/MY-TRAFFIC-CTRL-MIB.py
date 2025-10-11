# SNMP MIB module (MY-TRAFFIC-CTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruijie/MY-TRAFFIC-CTRL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:02 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

(ConfigStatus,
 IfIndex,
 MemberMap) = mibBuilder.importSymbols(
    "MY-TC",
    "ConfigStatus",
    "IfIndex",
    "MemberMap")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

myTrafficCtrlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14)
)
if mibBuilder.loadTexts:
    myTrafficCtrlMIB.setRevisions(
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

_MyTrafficCtrlMIBObjects_ObjectIdentity = ObjectIdentity
myTrafficCtrlMIBObjects = _MyTrafficCtrlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1)
)
_MyPtTrafficCtrlTable_Object = MibTable
myPtTrafficCtrlTable = _MyPtTrafficCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    myPtTrafficCtrlTable.setStatus("current")
_MyPtTrafficCtrlEntry_Object = MibTableRow
myPtTrafficCtrlEntry = _MyPtTrafficCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1, 1)
)
myPtTrafficCtrlEntry.setIndexNames(
    (0, "MY-TRAFFIC-CTRL-MIB", "myPtTrafficCtrlIfIndex"),
)
if mibBuilder.loadTexts:
    myPtTrafficCtrlEntry.setStatus("current")
_MyPtTrafficCtrlIfIndex_Type = IfIndex
_MyPtTrafficCtrlIfIndex_Object = MibTableColumn
myPtTrafficCtrlIfIndex = _MyPtTrafficCtrlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1, 1, 1),
    _MyPtTrafficCtrlIfIndex_Type()
)
myPtTrafficCtrlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPtTrafficCtrlIfIndex.setStatus("current")


class _MyPtProtectedPortStatus_Type(EnabledStatus):
    """Custom type myPtProtectedPortStatus based on EnabledStatus"""
    defaultValue = 2


_MyPtProtectedPortStatus_Type.__name__ = "EnabledStatus"
_MyPtProtectedPortStatus_Object = MibTableColumn
myPtProtectedPortStatus = _MyPtProtectedPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1, 1, 2),
    _MyPtProtectedPortStatus_Type()
)
myPtProtectedPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myPtProtectedPortStatus.setStatus("current")
_MyPtBroadcastStormControlStatus_Type = EnabledStatus
_MyPtBroadcastStormControlStatus_Object = MibTableColumn
myPtBroadcastStormControlStatus = _MyPtBroadcastStormControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1, 1, 3),
    _MyPtBroadcastStormControlStatus_Type()
)
myPtBroadcastStormControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myPtBroadcastStormControlStatus.setStatus("current")
_MyPtMulticastStormControlStatus_Type = EnabledStatus
_MyPtMulticastStormControlStatus_Object = MibTableColumn
myPtMulticastStormControlStatus = _MyPtMulticastStormControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1, 1, 4),
    _MyPtMulticastStormControlStatus_Type()
)
myPtMulticastStormControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myPtMulticastStormControlStatus.setStatus("current")
_MyPtUnicastStormControlStatus_Type = EnabledStatus
_MyPtUnicastStormControlStatus_Object = MibTableColumn
myPtUnicastStormControlStatus = _MyPtUnicastStormControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1, 1, 5),
    _MyPtUnicastStormControlStatus_Type()
)
myPtUnicastStormControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myPtUnicastStormControlStatus.setStatus("current")


class _MyPtBroadcastStormControlLevel_Type(Percent):
    """Custom type myPtBroadcastStormControlLevel based on Percent"""
    defaultValue = 10


_MyPtBroadcastStormControlLevel_Type.__name__ = "Percent"
_MyPtBroadcastStormControlLevel_Object = MibTableColumn
myPtBroadcastStormControlLevel = _MyPtBroadcastStormControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1, 1, 6),
    _MyPtBroadcastStormControlLevel_Type()
)
myPtBroadcastStormControlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myPtBroadcastStormControlLevel.setStatus("current")


class _MyPtMulticastStormControlLevel_Type(Percent):
    """Custom type myPtMulticastStormControlLevel based on Percent"""
    defaultValue = 10


_MyPtMulticastStormControlLevel_Type.__name__ = "Percent"
_MyPtMulticastStormControlLevel_Object = MibTableColumn
myPtMulticastStormControlLevel = _MyPtMulticastStormControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1, 1, 7),
    _MyPtMulticastStormControlLevel_Type()
)
myPtMulticastStormControlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myPtMulticastStormControlLevel.setStatus("current")


class _MyPtUnicastStormControlLevel_Type(Percent):
    """Custom type myPtUnicastStormControlLevel based on Percent"""
    defaultValue = 10


_MyPtUnicastStormControlLevel_Type.__name__ = "Percent"
_MyPtUnicastStormControlLevel_Object = MibTableColumn
myPtUnicastStormControlLevel = _MyPtUnicastStormControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1, 1, 8),
    _MyPtUnicastStormControlLevel_Type()
)
myPtUnicastStormControlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myPtUnicastStormControlLevel.setStatus("current")
_MyPtTrafficCtrlTraps_ObjectIdentity = ObjectIdentity
myPtTrafficCtrlTraps = _MyPtTrafficCtrlTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 2)
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
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 2, 1),
    _StormViolationAlarmType_Type()
)
stormViolationAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stormViolationAlarmType.setStatus("current")
_MyPtTrafficCtrlMIBConformance_ObjectIdentity = ObjectIdentity
myPtTrafficCtrlMIBConformance = _MyPtTrafficCtrlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 3)
)
_MyPtTrafficCtrlMIBCompliances_ObjectIdentity = ObjectIdentity
myPtTrafficCtrlMIBCompliances = _MyPtTrafficCtrlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 3, 1)
)
_MyPtTrafficCtrlMIBGroups_ObjectIdentity = ObjectIdentity
myPtTrafficCtrlMIBGroups = _MyPtTrafficCtrlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 3, 2)
)

# Managed Objects groups

myPtTrafficCtrlMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 3, 2, 1)
)
myPtTrafficCtrlMIBGroup.setObjects(
      *(("MY-TRAFFIC-CTRL-MIB", "myPtTrafficCtrlIfIndex"),
        ("MY-TRAFFIC-CTRL-MIB", "myPtProtectedPortStatus"),
        ("MY-TRAFFIC-CTRL-MIB", "myPtBroadcastStormControlStatus"),
        ("MY-TRAFFIC-CTRL-MIB", "myPtMulticastStormControlStatus"),
        ("MY-TRAFFIC-CTRL-MIB", "myPtUnicastStormControlStatus"),
        ("MY-TRAFFIC-CTRL-MIB", "myPtBroadcastStormControlLevel"),
        ("MY-TRAFFIC-CTRL-MIB", "myPtMulticastStormControlLevel"),
        ("MY-TRAFFIC-CTRL-MIB", "myPtUnicastStormControlLevel"))
)
if mibBuilder.loadTexts:
    myPtTrafficCtrlMIBGroup.setStatus("current")


# Notification objects

stormViolationAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 2, 2)
)
stormViolationAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("MY-TRAFFIC-CTRL-MIB", "stormViolationAlarmType"))
)
if mibBuilder.loadTexts:
    stormViolationAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

myPtTrafficCtrlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 3, 1, 1)
)
myPtTrafficCtrlMIBCompliance.setObjects(
    ("MY-TRAFFIC-CTRL-MIB", "myPtTrafficCtrlMIBGroup")
)
if mibBuilder.loadTexts:
    myPtTrafficCtrlMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-TRAFFIC-CTRL-MIB",
    **{"Percent": Percent,
       "myTrafficCtrlMIB": myTrafficCtrlMIB,
       "myTrafficCtrlMIBObjects": myTrafficCtrlMIBObjects,
       "myPtTrafficCtrlTable": myPtTrafficCtrlTable,
       "myPtTrafficCtrlEntry": myPtTrafficCtrlEntry,
       "myPtTrafficCtrlIfIndex": myPtTrafficCtrlIfIndex,
       "myPtProtectedPortStatus": myPtProtectedPortStatus,
       "myPtBroadcastStormControlStatus": myPtBroadcastStormControlStatus,
       "myPtMulticastStormControlStatus": myPtMulticastStormControlStatus,
       "myPtUnicastStormControlStatus": myPtUnicastStormControlStatus,
       "myPtBroadcastStormControlLevel": myPtBroadcastStormControlLevel,
       "myPtMulticastStormControlLevel": myPtMulticastStormControlLevel,
       "myPtUnicastStormControlLevel": myPtUnicastStormControlLevel,
       "myPtTrafficCtrlTraps": myPtTrafficCtrlTraps,
       "stormViolationAlarmType": stormViolationAlarmType,
       "stormViolationAlarm": stormViolationAlarm,
       "myPtTrafficCtrlMIBConformance": myPtTrafficCtrlMIBConformance,
       "myPtTrafficCtrlMIBCompliances": myPtTrafficCtrlMIBCompliances,
       "myPtTrafficCtrlMIBCompliance": myPtTrafficCtrlMIBCompliance,
       "myPtTrafficCtrlMIBGroups": myPtTrafficCtrlMIBGroups,
       "myPtTrafficCtrlMIBGroup": myPtTrafficCtrlMIBGroup}
)
