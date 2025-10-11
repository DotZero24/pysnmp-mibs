# SNMP MIB module (WTI-AFS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/wti/WTI-AFS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:22:20 2025
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

afs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 4)
)
if mibBuilder.loadTexts:
    afs.setRevisions(
        ("2010-04-02 16:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WesternTelematic_ObjectIdentity = ObjectIdentity
westernTelematic = _WesternTelematic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634)
)
_SystemTables_ObjectIdentity = ObjectIdentity
systemTables = _SystemTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100)
)
_CircuitTable_Object = MibTable
circuitTable = _CircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 200)
)
if mibBuilder.loadTexts:
    circuitTable.setStatus("current")
_CircuitEntry_Object = MibTableRow
circuitEntry = _CircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 200, 1)
)
circuitEntry.setIndexNames(
    (0, "WTI-AFS-MIB", "circuitIndex"),
)
if mibBuilder.loadTexts:
    circuitEntry.setStatus("current")


class _CircuitIndex_Type(Integer32):
    """Custom type circuitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CircuitIndex_Type.__name__ = "Integer32"
_CircuitIndex_Object = MibTableColumn
circuitIndex = _CircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 200, 1, 1),
    _CircuitIndex_Type()
)
circuitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    circuitIndex.setStatus("current")


class _CircuitID_Type(DisplayString):
    """Custom type circuitID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 11),
    )


_CircuitID_Type.__name__ = "DisplayString"
_CircuitID_Object = MibTableColumn
circuitID = _CircuitID_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 200, 1, 2),
    _CircuitID_Type()
)
circuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitID.setStatus("current")


class _CircuitStatus_Type(Integer32):
    """Custom type circuitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CircuitStatus_Type.__name__ = "Integer32"
_CircuitStatus_Object = MibTableColumn
circuitStatus = _CircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 200, 1, 3),
    _CircuitStatus_Type()
)
circuitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitStatus.setStatus("current")


class _CircuitAction_Type(Integer32):
    """Custom type circuitAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CircuitAction_Type.__name__ = "Integer32"
_CircuitAction_Object = MibTableColumn
circuitAction = _CircuitAction_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 200, 1, 4),
    _CircuitAction_Type()
)
circuitAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitAction.setStatus("current")
_CircuitName_Type = DisplayString
_CircuitName_Object = MibTableColumn
circuitName = _CircuitName_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 200, 1, 5),
    _CircuitName_Type()
)
circuitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitName.setStatus("current")
_CircuitReason_Type = Integer32
_CircuitReason_Object = MibTableColumn
circuitReason = _CircuitReason_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 200, 1, 6),
    _CircuitReason_Type()
)
circuitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitReason.setStatus("current")
_CircuitGroupTable_Object = MibTable
circuitGroupTable = _CircuitGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 300)
)
if mibBuilder.loadTexts:
    circuitGroupTable.setStatus("current")
_CircuitGroupEntry_Object = MibTableRow
circuitGroupEntry = _CircuitGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 300, 1)
)
circuitGroupEntry.setIndexNames(
    (0, "WTI-AFS-MIB", "circuitGroupIndex"),
)
if mibBuilder.loadTexts:
    circuitGroupEntry.setStatus("current")


class _CircuitGroupIndex_Type(Integer32):
    """Custom type circuitGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 54),
    )


_CircuitGroupIndex_Type.__name__ = "Integer32"
_CircuitGroupIndex_Object = MibTableColumn
circuitGroupIndex = _CircuitGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 300, 1, 1),
    _CircuitGroupIndex_Type()
)
circuitGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    circuitGroupIndex.setStatus("current")


class _CircuitGroupName_Type(DisplayString):
    """Custom type circuitGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_CircuitGroupName_Type.__name__ = "DisplayString"
_CircuitGroupName_Object = MibTableColumn
circuitGroupName = _CircuitGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 300, 1, 2),
    _CircuitGroupName_Type()
)
circuitGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitGroupName.setStatus("current")


class _CircuitGroupAction_Type(Integer32):
    """Custom type circuitGroupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CircuitGroupAction_Type.__name__ = "Integer32"
_CircuitGroupAction_Object = MibTableColumn
circuitGroupAction = _CircuitGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 300, 1, 3),
    _CircuitGroupAction_Type()
)
circuitGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitGroupAction.setStatus("current")
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 400)
)
if mibBuilder.loadTexts:
    userTable.setStatus("current")
_UserEntry_Object = MibTableRow
userEntry = _UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 400, 1)
)
userEntry.setIndexNames(
    (0, "WTI-AFS-MIB", "userIndex"),
)
if mibBuilder.loadTexts:
    userEntry.setStatus("current")


class _UserIndex_Type(Integer32):
    """Custom type userIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_UserIndex_Type.__name__ = "Integer32"
_UserIndex_Object = MibTableColumn
userIndex = _UserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 400, 1, 1),
    _UserIndex_Type()
)
userIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userIndex.setStatus("current")


class _UserName_Type(DisplayString):
    """Custom type userName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserName_Type.__name__ = "DisplayString"
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 400, 1, 2),
    _UserName_Type()
)
userName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userName.setStatus("current")


class _UserPasswd_Type(DisplayString):
    """Custom type userPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_UserPasswd_Type.__name__ = "DisplayString"
_UserPasswd_Object = MibTableColumn
userPasswd = _UserPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 400, 1, 3),
    _UserPasswd_Type()
)
userPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPasswd.setStatus("current")


class _UserAccessLevel_Type(Integer32):
    """Custom type userAccessLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_UserAccessLevel_Type.__name__ = "Integer32"
_UserAccessLevel_Object = MibTableColumn
userAccessLevel = _UserAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 400, 1, 4),
    _UserAccessLevel_Type()
)
userAccessLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAccessLevel.setStatus("current")


class _UserCircuitAccess_Type(DisplayString):
    """Custom type userCircuitAccess based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_UserCircuitAccess_Type.__name__ = "DisplayString"
_UserCircuitAccess_Object = MibTableColumn
userCircuitAccess = _UserCircuitAccess_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 400, 1, 6),
    _UserCircuitAccess_Type()
)
userCircuitAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userCircuitAccess.setStatus("current")


class _UserGroupAccess_Type(DisplayString):
    """Custom type userGroupAccess based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 54),
    )


_UserGroupAccess_Type.__name__ = "DisplayString"
_UserGroupAccess_Object = MibTableColumn
userGroupAccess = _UserGroupAccess_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 400, 1, 10),
    _UserGroupAccess_Type()
)
userGroupAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userGroupAccess.setStatus("current")


class _UserSerialAccess_Type(Integer32):
    """Custom type userSerialAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_UserSerialAccess_Type.__name__ = "Integer32"
_UserSerialAccess_Object = MibTableColumn
userSerialAccess = _UserSerialAccess_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 400, 1, 11),
    _UserSerialAccess_Type()
)
userSerialAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSerialAccess.setStatus("current")


class _UserTelnetSshAccess_Type(Integer32):
    """Custom type userTelnetSshAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_UserTelnetSshAccess_Type.__name__ = "Integer32"
_UserTelnetSshAccess_Object = MibTableColumn
userTelnetSshAccess = _UserTelnetSshAccess_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 400, 1, 12),
    _UserTelnetSshAccess_Type()
)
userTelnetSshAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userTelnetSshAccess.setStatus("current")


class _UserWebAccess_Type(Integer32):
    """Custom type userWebAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_UserWebAccess_Type.__name__ = "Integer32"
_UserWebAccess_Object = MibTableColumn
userWebAccess = _UserWebAccess_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 400, 1, 13),
    _UserWebAccess_Type()
)
userWebAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userWebAccess.setStatus("current")


class _UserOutboundTelAccess_Type(Integer32):
    """Custom type userOutboundTelAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_UserOutboundTelAccess_Type.__name__ = "Integer32"
_UserOutboundTelAccess_Object = MibTableColumn
userOutboundTelAccess = _UserOutboundTelAccess_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 400, 1, 14),
    _UserOutboundTelAccess_Type()
)
userOutboundTelAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userOutboundTelAccess.setStatus("current")


class _UserCallbackNum_Type(DisplayString):
    """Custom type userCallbackNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserCallbackNum_Type.__name__ = "DisplayString"
_UserCallbackNum_Object = MibTableColumn
userCallbackNum = _UserCallbackNum_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 400, 1, 16),
    _UserCallbackNum_Type()
)
userCallbackNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userCallbackNum.setStatus("current")


class _UserSubmit_Type(Integer32):
    """Custom type userSubmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_UserSubmit_Type.__name__ = "Integer32"
_UserSubmit_Object = MibTableColumn
userSubmit = _UserSubmit_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 100, 400, 1, 31),
    _UserSubmit_Type()
)
userSubmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSubmit.setStatus("current")
_EnvironmentTables_ObjectIdentity = ObjectIdentity
environmentTables = _EnvironmentTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 4, 200)
)
_EnvironmentUnitTable_Object = MibTable
environmentUnitTable = _EnvironmentUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 200, 10)
)
if mibBuilder.loadTexts:
    environmentUnitTable.setStatus("current")
_EnvironmentUnitEntry_Object = MibTableRow
environmentUnitEntry = _EnvironmentUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 200, 10, 1)
)
environmentUnitEntry.setIndexNames(
    (0, "WTI-AFS-MIB", "environmentUnitIndex"),
)
if mibBuilder.loadTexts:
    environmentUnitEntry.setStatus("current")


class _EnvironmentUnitIndex_Type(Integer32):
    """Custom type environmentUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_EnvironmentUnitIndex_Type.__name__ = "Integer32"
_EnvironmentUnitIndex_Object = MibTableColumn
environmentUnitIndex = _EnvironmentUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 200, 10, 1, 1),
    _EnvironmentUnitIndex_Type()
)
environmentUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    environmentUnitIndex.setStatus("current")


class _EnvironmentUnitName_Type(DisplayString):
    """Custom type environmentUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EnvironmentUnitName_Type.__name__ = "DisplayString"
_EnvironmentUnitName_Object = MibTableColumn
environmentUnitName = _EnvironmentUnitName_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 200, 10, 1, 2),
    _EnvironmentUnitName_Type()
)
environmentUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentUnitName.setStatus("current")
_EnvironmentUnitTemperature_Type = Integer32
_EnvironmentUnitTemperature_Object = MibTableColumn
environmentUnitTemperature = _EnvironmentUnitTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 200, 10, 1, 3),
    _EnvironmentUnitTemperature_Type()
)
environmentUnitTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentUnitTemperature.setStatus("current")
_EnvironmentUnitMonitorAlarm_Type = Integer32
_EnvironmentUnitMonitorAlarm_Object = MibTableColumn
environmentUnitMonitorAlarm = _EnvironmentUnitMonitorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 200, 10, 1, 17),
    _EnvironmentUnitMonitorAlarm_Type()
)
environmentUnitMonitorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentUnitMonitorAlarm.setStatus("current")
_EnvironmentSysRAM_Type = Integer32
_EnvironmentSysRAM_Object = MibTableColumn
environmentSysRAM = _EnvironmentSysRAM_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 200, 10, 1, 18),
    _EnvironmentSysRAM_Type()
)
environmentSysRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentSysRAM.setStatus("current")
_EnvironmentSysFlash_Type = Integer32
_EnvironmentSysFlash_Object = MibTableColumn
environmentSysFlash = _EnvironmentSysFlash_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 200, 10, 1, 19),
    _EnvironmentSysFlash_Type()
)
environmentSysFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentSysFlash.setStatus("current")
_WtiTraps_ObjectIdentity = ObjectIdentity
wtiTraps = _WtiTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300)
)
_TrapInfo_Type = DisplayString
_TrapInfo_Object = MibScalar
trapInfo = _TrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 1),
    _TrapInfo_Type()
)
trapInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapInfo.setStatus("current")
_TestTraps_ObjectIdentity = ObjectIdentity
testTraps = _TestTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 2)
)
_OverTemperatureInitialTraps_ObjectIdentity = ObjectIdentity
overTemperatureInitialTraps = _OverTemperatureInitialTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 6)
)
_OverTemperatureCriticalTraps_ObjectIdentity = ObjectIdentity
overTemperatureCriticalTraps = _OverTemperatureCriticalTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 7)
)
_PingNoAnswerTraps_ObjectIdentity = ObjectIdentity
pingNoAnswerTraps = _PingNoAnswerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 11)
)
_LockoutTraps_ObjectIdentity = ObjectIdentity
lockoutTraps = _LockoutTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 12)
)
_PowercycleTraps_ObjectIdentity = ObjectIdentity
powercycleTraps = _PowercycleTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 13)
)
_MonitorAlarmTraps_ObjectIdentity = ObjectIdentity
monitorAlarmTraps = _MonitorAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 14)
)

# Managed Objects groups


# Notification objects

testTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 2, 0, 1)
)
testTrap.setObjects(
    ("WTI-AFS-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    testTrap.setStatus(
        ""
    )

overTemperatureInitialSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 6, 0, 1)
)
overTemperatureInitialSetTrap.setObjects(
    ("WTI-AFS-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    overTemperatureInitialSetTrap.setStatus(
        ""
    )

overTemperatureInitialClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 6, 0, 2)
)
overTemperatureInitialClearTrap.setObjects(
    ("WTI-AFS-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    overTemperatureInitialClearTrap.setStatus(
        ""
    )

overTemperatureCriticalSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 7, 0, 1)
)
overTemperatureCriticalSetTrap.setObjects(
    ("WTI-AFS-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    overTemperatureCriticalSetTrap.setStatus(
        ""
    )

overTemperatureCriticalClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 7, 0, 2)
)
overTemperatureCriticalClearTrap.setObjects(
    ("WTI-AFS-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    overTemperatureCriticalClearTrap.setStatus(
        ""
    )

pingNoAnswerSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 11, 0, 1)
)
pingNoAnswerSetTrap.setObjects(
    ("WTI-AFS-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    pingNoAnswerSetTrap.setStatus(
        ""
    )

pingNoAnswerClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 11, 0, 2)
)
pingNoAnswerClearTrap.setObjects(
    ("WTI-AFS-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    pingNoAnswerClearTrap.setStatus(
        ""
    )

lockoutSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 12, 0, 1)
)
lockoutSetTrap.setObjects(
    ("WTI-AFS-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    lockoutSetTrap.setStatus(
        ""
    )

lockoutClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 12, 0, 2)
)
lockoutClearTrap.setObjects(
    ("WTI-AFS-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    lockoutClearTrap.setStatus(
        ""
    )

powercycleSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 13, 0, 1)
)
powercycleSetTrap.setObjects(
    ("WTI-AFS-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    powercycleSetTrap.setStatus(
        ""
    )

monitorAlarmSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 14, 0, 1)
)
monitorAlarmSetTrap.setObjects(
    ("WTI-AFS-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    monitorAlarmSetTrap.setStatus(
        ""
    )

monitorAlarmClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 4, 300, 14, 0, 2)
)
monitorAlarmClearTrap.setObjects(
    ("WTI-AFS-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    monitorAlarmClearTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WTI-AFS-MIB",
    **{"westernTelematic": westernTelematic,
       "afs": afs,
       "systemTables": systemTables,
       "circuitTable": circuitTable,
       "circuitEntry": circuitEntry,
       "circuitIndex": circuitIndex,
       "circuitID": circuitID,
       "circuitStatus": circuitStatus,
       "circuitAction": circuitAction,
       "circuitName": circuitName,
       "circuitReason": circuitReason,
       "circuitGroupTable": circuitGroupTable,
       "circuitGroupEntry": circuitGroupEntry,
       "circuitGroupIndex": circuitGroupIndex,
       "circuitGroupName": circuitGroupName,
       "circuitGroupAction": circuitGroupAction,
       "userTable": userTable,
       "userEntry": userEntry,
       "userIndex": userIndex,
       "userName": userName,
       "userPasswd": userPasswd,
       "userAccessLevel": userAccessLevel,
       "userCircuitAccess": userCircuitAccess,
       "userGroupAccess": userGroupAccess,
       "userSerialAccess": userSerialAccess,
       "userTelnetSshAccess": userTelnetSshAccess,
       "userWebAccess": userWebAccess,
       "userOutboundTelAccess": userOutboundTelAccess,
       "userCallbackNum": userCallbackNum,
       "userSubmit": userSubmit,
       "environmentTables": environmentTables,
       "environmentUnitTable": environmentUnitTable,
       "environmentUnitEntry": environmentUnitEntry,
       "environmentUnitIndex": environmentUnitIndex,
       "environmentUnitName": environmentUnitName,
       "environmentUnitTemperature": environmentUnitTemperature,
       "environmentUnitMonitorAlarm": environmentUnitMonitorAlarm,
       "environmentSysRAM": environmentSysRAM,
       "environmentSysFlash": environmentSysFlash,
       "wtiTraps": wtiTraps,
       "trapInfo": trapInfo,
       "testTraps": testTraps,
       "testTrap": testTrap,
       "overTemperatureInitialTraps": overTemperatureInitialTraps,
       "overTemperatureInitialSetTrap": overTemperatureInitialSetTrap,
       "overTemperatureInitialClearTrap": overTemperatureInitialClearTrap,
       "overTemperatureCriticalTraps": overTemperatureCriticalTraps,
       "overTemperatureCriticalSetTrap": overTemperatureCriticalSetTrap,
       "overTemperatureCriticalClearTrap": overTemperatureCriticalClearTrap,
       "pingNoAnswerTraps": pingNoAnswerTraps,
       "pingNoAnswerSetTrap": pingNoAnswerSetTrap,
       "pingNoAnswerClearTrap": pingNoAnswerClearTrap,
       "lockoutTraps": lockoutTraps,
       "lockoutSetTrap": lockoutSetTrap,
       "lockoutClearTrap": lockoutClearTrap,
       "powercycleTraps": powercycleTraps,
       "powercycleSetTrap": powercycleSetTrap,
       "monitorAlarmTraps": monitorAlarmTraps,
       "monitorAlarmSetTrap": monitorAlarmSetTrap,
       "monitorAlarmClearTrap": monitorAlarmClearTrap}
)
