# SNMP MIB module (MX-EPADM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-EPADM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:11 2025
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

(mediatrixServices,) = mibBuilder.importSymbols(
    "MX-SMI2",
    "mediatrixServices")

(MxActivationState,
 MxAdvancedIpPort,
 MxDigitMap,
 MxEnableState,
 MxIpAddress,
 MxIpHostName,
 MxIpPort,
 MxIpSubnetMask) = mibBuilder.importSymbols(
    "MX-TC",
    "MxActivationState",
    "MxAdvancedIpPort",
    "MxDigitMap",
    "MxEnableState",
    "MxIpAddress",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSubnetMask")

(MxFloat32,
 MxIpAddr,
 MxIpAddrMask,
 MxIpAddrPort,
 MxIpHostNamePort,
 MxUInt64,
 MxUri,
 MxUrl) = mibBuilder.importSymbols(
    "MX-TC2",
    "MxFloat32",
    "MxIpAddr",
    "MxIpAddrMask",
    "MxIpAddrPort",
    "MxIpHostNamePort",
    "MxUInt64",
    "MxUri",
    "MxUrl")

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

epAdmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EpAdmMIBObjects_ObjectIdentity = ObjectIdentity
epAdmMIBObjects = _EpAdmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1)
)
_UnitStateGroup_ObjectIdentity = ObjectIdentity
unitStateGroup = _UnitStateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 100)
)


class _UnitAdminState_Type(Integer32):
    """Custom type unitAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("unlocked", 100),
          ("shuttingDown", 200),
          ("locked", 300))
    )


_UnitAdminState_Type.__name__ = "Integer32"
_UnitAdminState_Object = MibScalar
unitAdminState = _UnitAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 100, 100),
    _UnitAdminState_Type()
)
unitAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitAdminState.setStatus("current")
_UnitOpState_Type = MxEnableState
_UnitOpState_Object = MibScalar
unitOpState = _UnitOpState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 100, 200),
    _UnitOpState_Type()
)
unitOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitOpState.setStatus("current")


class _UnitUsageState_Type(Integer32):
    """Custom type unitUsageState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("idle", 100),
          ("active", 200),
          ("busy", 300),
          ("idleUnusable", 400))
    )


_UnitUsageState_Type.__name__ = "Integer32"
_UnitUsageState_Object = MibScalar
unitUsageState = _UnitUsageState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 100, 300),
    _UnitUsageState_Type()
)
unitUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitUsageState.setStatus("current")
_EndpointTable_Object = MibTable
endpointTable = _EndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 200)
)
if mibBuilder.loadTexts:
    endpointTable.setStatus("current")
_EndpointEntry_Object = MibTableRow
endpointEntry = _EndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 200, 1)
)
endpointEntry.setIndexNames(
    (0, "MX-EPADM-MIB", "endpointEpId"),
)
if mibBuilder.loadTexts:
    endpointEntry.setStatus("current")
_EndpointEpId_Type = OctetString
_EndpointEpId_Object = MibTableColumn
endpointEpId = _EndpointEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 200, 1, 100),
    _EndpointEpId_Type()
)
endpointEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endpointEpId.setStatus("current")


class _EndpointInitialAdminStateConfig_Type(Integer32):
    """Custom type endpointInitialAdminStateConfig based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("unlocked", 100),
          ("locked", 200))
    )


_EndpointInitialAdminStateConfig_Type.__name__ = "Integer32"
_EndpointInitialAdminStateConfig_Object = MibTableColumn
endpointInitialAdminStateConfig = _EndpointInitialAdminStateConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 200, 1, 200),
    _EndpointInitialAdminStateConfig_Type()
)
endpointInitialAdminStateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endpointInitialAdminStateConfig.setStatus("current")


class _EndpointAdminState_Type(Integer32):
    """Custom type endpointAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("unlocked", 100),
          ("shuttingDown", 200),
          ("locked", 300))
    )


_EndpointAdminState_Type.__name__ = "Integer32"
_EndpointAdminState_Object = MibTableColumn
endpointAdminState = _EndpointAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 200, 1, 300),
    _EndpointAdminState_Type()
)
endpointAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endpointAdminState.setStatus("current")
_EndpointOpState_Type = MxEnableState
_EndpointOpState_Object = MibTableColumn
endpointOpState = _EndpointOpState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 200, 1, 400),
    _EndpointOpState_Type()
)
endpointOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endpointOpState.setStatus("current")


class _EndpointUsageState_Type(Integer32):
    """Custom type endpointUsageState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("idle", 100),
          ("active", 200),
          ("busy", 300),
          ("idleUnusable", 400))
    )


_EndpointUsageState_Type.__name__ = "Integer32"
_EndpointUsageState_Object = MibTableColumn
endpointUsageState = _EndpointUsageState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 200, 1, 500),
    _EndpointUsageState_Type()
)
endpointUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endpointUsageState.setStatus("current")


class _EndpointUnlock_Type(Integer32):
    """Custom type endpointUnlock based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("unlock", 10))
    )


_EndpointUnlock_Type.__name__ = "Integer32"
_EndpointUnlock_Object = MibTableColumn
endpointUnlock = _EndpointUnlock_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 200, 1, 600),
    _EndpointUnlock_Type()
)
endpointUnlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endpointUnlock.setStatus("current")


class _EndpointLock_Type(Integer32):
    """Custom type endpointLock based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("lock", 10))
    )


_EndpointLock_Type.__name__ = "Integer32"
_EndpointLock_Object = MibTableColumn
endpointLock = _EndpointLock_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 200, 1, 700),
    _EndpointLock_Type()
)
endpointLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endpointLock.setStatus("current")


class _EndpointForceLock_Type(Integer32):
    """Custom type endpointForceLock based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("forceLock", 10))
    )


_EndpointForceLock_Type.__name__ = "Integer32"
_EndpointForceLock_Object = MibTableColumn
endpointForceLock = _EndpointForceLock_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 200, 1, 800),
    _EndpointForceLock_Type()
)
endpointForceLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endpointForceLock.setStatus("current")
_UnitConfigGroup_ObjectIdentity = ObjectIdentity
unitConfigGroup = _UnitConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 300)
)


class _UnitDisabledWhenNoGatewayReadyEnable_Type(MxEnableState):
    """Custom type unitDisabledWhenNoGatewayReadyEnable based on MxEnableState"""
    defaultValue = 0


_UnitDisabledWhenNoGatewayReadyEnable_Type.__name__ = "MxEnableState"
_UnitDisabledWhenNoGatewayReadyEnable_Object = MibScalar
unitDisabledWhenNoGatewayReadyEnable = _UnitDisabledWhenNoGatewayReadyEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 300, 100),
    _UnitDisabledWhenNoGatewayReadyEnable_Type()
)
unitDisabledWhenNoGatewayReadyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitDisabledWhenNoGatewayReadyEnable.setStatus("current")


class _BehaviorWhileInUnitShuttingDownState_Type(Integer32):
    """Custom type behaviorWhileInUnitShuttingDownState based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("blockNewCalls", 100),
          ("allowNewCalls", 200))
    )


_BehaviorWhileInUnitShuttingDownState_Type.__name__ = "Integer32"
_BehaviorWhileInUnitShuttingDownState_Object = MibScalar
behaviorWhileInUnitShuttingDownState = _BehaviorWhileInUnitShuttingDownState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 300, 200),
    _BehaviorWhileInUnitShuttingDownState_Type()
)
behaviorWhileInUnitShuttingDownState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    behaviorWhileInUnitShuttingDownState.setStatus("current")
_SipGatewayConfigGroup_ObjectIdentity = ObjectIdentity
sipGatewayConfigGroup = _SipGatewayConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 350)
)


class _DisableSipGatewaysWhenTrunkLinesDown_Type(MxEnableState):
    """Custom type disableSipGatewaysWhenTrunkLinesDown based on MxEnableState"""
    defaultValue = 0


_DisableSipGatewaysWhenTrunkLinesDown_Type.__name__ = "MxEnableState"
_DisableSipGatewaysWhenTrunkLinesDown_Object = MibScalar
disableSipGatewaysWhenTrunkLinesDown = _DisableSipGatewaysWhenTrunkLinesDown_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 350, 100),
    _DisableSipGatewaysWhenTrunkLinesDown_Type()
)
disableSipGatewaysWhenTrunkLinesDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disableSipGatewaysWhenTrunkLinesDown.setStatus("current")


class _DisableSipGatewaysWhenTrunkLinesDownDelay_Type(Unsigned32):
    """Custom type disableSipGatewaysWhenTrunkLinesDownDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_DisableSipGatewaysWhenTrunkLinesDownDelay_Type.__name__ = "Unsigned32"
_DisableSipGatewaysWhenTrunkLinesDownDelay_Object = MibScalar
disableSipGatewaysWhenTrunkLinesDownDelay = _DisableSipGatewaysWhenTrunkLinesDownDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 350, 200),
    _DisableSipGatewaysWhenTrunkLinesDownDelay_Type()
)
disableSipGatewaysWhenTrunkLinesDownDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disableSipGatewaysWhenTrunkLinesDownDelay.setStatus("current")
_EndpointConfigGroup_ObjectIdentity = ObjectIdentity
endpointConfigGroup = _EndpointConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 400)
)


class _EndpointAutomaticShutdownEnable_Type(MxEnableState):
    """Custom type endpointAutomaticShutdownEnable based on MxEnableState"""
    defaultValue = 0


_EndpointAutomaticShutdownEnable_Type.__name__ = "MxEnableState"
_EndpointAutomaticShutdownEnable_Object = MibScalar
endpointAutomaticShutdownEnable = _EndpointAutomaticShutdownEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 400, 100),
    _EndpointAutomaticShutdownEnable_Type()
)
endpointAutomaticShutdownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endpointAutomaticShutdownEnable.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 60010)
)


class _MinSeverity_Type(Integer32):
    """Custom type minSeverity based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("debug", 100),
          ("info", 200),
          ("warning", 300),
          ("error", 400),
          ("critical", 500))
    )


_MinSeverity_Type.__name__ = "Integer32"
_MinSeverity_Object = MibScalar
minSeverity = _MinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 60020)
)


class _NeedRestartInfo_Type(Integer32):
    """Custom type needRestartInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 100))
    )


_NeedRestartInfo_Type.__name__ = "Integer32"
_NeedRestartInfo_Object = MibScalar
needRestartInfo = _NeedRestartInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1500, 1, 60020, 100),
    _NeedRestartInfo_Type()
)
needRestartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    needRestartInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-EPADM-MIB",
    **{"epAdmMIB": epAdmMIB,
       "epAdmMIBObjects": epAdmMIBObjects,
       "unitStateGroup": unitStateGroup,
       "unitAdminState": unitAdminState,
       "unitOpState": unitOpState,
       "unitUsageState": unitUsageState,
       "endpointTable": endpointTable,
       "endpointEntry": endpointEntry,
       "endpointEpId": endpointEpId,
       "endpointInitialAdminStateConfig": endpointInitialAdminStateConfig,
       "endpointAdminState": endpointAdminState,
       "endpointOpState": endpointOpState,
       "endpointUsageState": endpointUsageState,
       "endpointUnlock": endpointUnlock,
       "endpointLock": endpointLock,
       "endpointForceLock": endpointForceLock,
       "unitConfigGroup": unitConfigGroup,
       "unitDisabledWhenNoGatewayReadyEnable": unitDisabledWhenNoGatewayReadyEnable,
       "behaviorWhileInUnitShuttingDownState": behaviorWhileInUnitShuttingDownState,
       "sipGatewayConfigGroup": sipGatewayConfigGroup,
       "disableSipGatewaysWhenTrunkLinesDown": disableSipGatewaysWhenTrunkLinesDown,
       "disableSipGatewaysWhenTrunkLinesDownDelay": disableSipGatewaysWhenTrunkLinesDownDelay,
       "endpointConfigGroup": endpointConfigGroup,
       "endpointAutomaticShutdownEnable": endpointAutomaticShutdownEnable,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
