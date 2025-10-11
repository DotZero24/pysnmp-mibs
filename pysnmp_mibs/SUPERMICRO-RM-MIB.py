# SNMP MIB module (SUPERMICRO-RM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-RM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:21 2025
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

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsRmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99)
)
if mibBuilder.loadTexts:
    fsRmMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FsRmState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("active", 1),
          ("standby", 2))
    )



# MIB Managed Objects in the order of their OIDs

_FsRmNotifications_ObjectIdentity = ObjectIdentity
fsRmNotifications = _FsRmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 0)
)
_FsRm_ObjectIdentity = ObjectIdentity
fsRm = _FsRm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1)
)


class _FsRmSelfNodeId_Type(InetAddressIPv6):
    """Custom type fsRmSelfNodeId based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsRmSelfNodeId_Type.__name__ = "InetAddressIPv6"
_FsRmSelfNodeId_Object = MibScalar
fsRmSelfNodeId = _FsRmSelfNodeId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 1),
    _FsRmSelfNodeId_Type()
)
fsRmSelfNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmSelfNodeId.setStatus("current")


class _FsRmPeerNodeId_Type(InetAddressIPv6):
    """Custom type fsRmPeerNodeId based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsRmPeerNodeId_Type.__name__ = "InetAddressIPv6"
_FsRmPeerNodeId_Object = MibScalar
fsRmPeerNodeId = _FsRmPeerNodeId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 2),
    _FsRmPeerNodeId_Type()
)
fsRmPeerNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmPeerNodeId.setStatus("current")


class _FsRmActiveNodeId_Type(InetAddressIPv6):
    """Custom type fsRmActiveNodeId based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsRmActiveNodeId_Type.__name__ = "InetAddressIPv6"
_FsRmActiveNodeId_Object = MibScalar
fsRmActiveNodeId = _FsRmActiveNodeId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 3),
    _FsRmActiveNodeId_Type()
)
fsRmActiveNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmActiveNodeId.setStatus("current")
_FsRmNodeState_Type = FsRmState
_FsRmNodeState_Object = MibScalar
fsRmNodeState = _FsRmNodeState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 4),
    _FsRmNodeState_Type()
)
fsRmNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmNodeState.setStatus("current")


class _FsRmHbInterval_Type(Integer32):
    """Custom type fsRmHbInterval based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 5000),
    )


_FsRmHbInterval_Type.__name__ = "Integer32"
_FsRmHbInterval_Object = MibScalar
fsRmHbInterval = _FsRmHbInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 5),
    _FsRmHbInterval_Type()
)
fsRmHbInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmHbInterval.setStatus("current")


class _FsRmPeerDeadInterval_Type(Integer32):
    """Custom type fsRmPeerDeadInterval based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 20000),
    )


_FsRmPeerDeadInterval_Type.__name__ = "Integer32"
_FsRmPeerDeadInterval_Object = MibScalar
fsRmPeerDeadInterval = _FsRmPeerDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 6),
    _FsRmPeerDeadInterval_Type()
)
fsRmPeerDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmPeerDeadInterval.setStatus("current")


class _FsRmTrcLevel_Type(Unsigned32):
    """Custom type fsRmTrcLevel based on Unsigned32"""
    defaultValue = 67174400


_FsRmTrcLevel_Type.__name__ = "Unsigned32"
_FsRmTrcLevel_Object = MibScalar
fsRmTrcLevel = _FsRmTrcLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 7),
    _FsRmTrcLevel_Type()
)
fsRmTrcLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmTrcLevel.setStatus("current")


class _FsRmForceSwitchoverFlag_Type(Integer32):
    """Custom type fsRmForceSwitchoverFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FsRmForceSwitchoverFlag_Type.__name__ = "Integer32"
_FsRmForceSwitchoverFlag_Object = MibScalar
fsRmForceSwitchoverFlag = _FsRmForceSwitchoverFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 8),
    _FsRmForceSwitchoverFlag_Type()
)
fsRmForceSwitchoverFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmForceSwitchoverFlag.setStatus("current")


class _FsRmPeerDeadIntMultiplier_Type(Integer32):
    """Custom type fsRmPeerDeadIntMultiplier based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 10),
    )


_FsRmPeerDeadIntMultiplier_Type.__name__ = "Integer32"
_FsRmPeerDeadIntMultiplier_Object = MibScalar
fsRmPeerDeadIntMultiplier = _FsRmPeerDeadIntMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 9),
    _FsRmPeerDeadIntMultiplier_Type()
)
fsRmPeerDeadIntMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmPeerDeadIntMultiplier.setStatus("current")


class _FsRmSwitchId_Type(Integer32):
    """Custom type fsRmSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsRmSwitchId_Type.__name__ = "Integer32"
_FsRmSwitchId_Object = MibScalar
fsRmSwitchId = _FsRmSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 10),
    _FsRmSwitchId_Type()
)
fsRmSwitchId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmSwitchId.setStatus("current")


class _FsRmConfiguredState_Type(Integer32):
    """Custom type fsRmConfiguredState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("preferredmaster", 1),
          ("backupmaster", 2),
          ("preferredslave", 3))
    )


_FsRmConfiguredState_Type.__name__ = "Integer32"
_FsRmConfiguredState_Object = MibScalar
fsRmConfiguredState = _FsRmConfiguredState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 11),
    _FsRmConfiguredState_Type()
)
fsRmConfiguredState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmConfiguredState.setStatus("current")
_FsRmStackMacAddr_Type = MacAddress
_FsRmStackMacAddr_Object = MibScalar
fsRmStackMacAddr = _FsRmStackMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 12),
    _FsRmStackMacAddr_Type()
)
fsRmStackMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmStackMacAddr.setStatus("current")
_FsRmPeerTable_Object = MibTable
fsRmPeerTable = _FsRmPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 13)
)
if mibBuilder.loadTexts:
    fsRmPeerTable.setStatus("current")
_FsRmPeerTableEntry_Object = MibTableRow
fsRmPeerTableEntry = _FsRmPeerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 13, 1)
)
fsRmPeerTableEntry.setIndexNames(
    (0, "SUPERMICRO-RM-MIB", "fsRmPeerSwitchId"),
)
if mibBuilder.loadTexts:
    fsRmPeerTableEntry.setStatus("current")


class _FsRmPeerSwitchId_Type(Integer32):
    """Custom type fsRmPeerSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsRmPeerSwitchId_Type.__name__ = "Integer32"
_FsRmPeerSwitchId_Object = MibTableColumn
fsRmPeerSwitchId = _FsRmPeerSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 13, 1, 1),
    _FsRmPeerSwitchId_Type()
)
fsRmPeerSwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRmPeerSwitchId.setStatus("current")
_FsRmPeerStackIpAddr_Type = IpAddress
_FsRmPeerStackIpAddr_Object = MibTableColumn
fsRmPeerStackIpAddr = _FsRmPeerStackIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 13, 1, 2),
    _FsRmPeerStackIpAddr_Type()
)
fsRmPeerStackIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmPeerStackIpAddr.setStatus("current")
_FsRmPeerStackMacAddr_Type = MacAddress
_FsRmPeerStackMacAddr_Object = MibTableColumn
fsRmPeerStackMacAddr = _FsRmPeerStackMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 13, 1, 3),
    _FsRmPeerStackMacAddr_Type()
)
fsRmPeerStackMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmPeerStackMacAddr.setStatus("current")
_FsRmPeerSwitchBaseMacAddr_Type = MacAddress
_FsRmPeerSwitchBaseMacAddr_Object = MibTableColumn
fsRmPeerSwitchBaseMacAddr = _FsRmPeerSwitchBaseMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 13, 1, 4),
    _FsRmPeerSwitchBaseMacAddr_Type()
)
fsRmPeerSwitchBaseMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmPeerSwitchBaseMacAddr.setStatus("current")


class _FsRmStackPortCount_Type(Integer32):
    """Custom type fsRmStackPortCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_FsRmStackPortCount_Type.__name__ = "Integer32"
_FsRmStackPortCount_Object = MibScalar
fsRmStackPortCount = _FsRmStackPortCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 14),
    _FsRmStackPortCount_Type()
)
fsRmStackPortCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmStackPortCount.setStatus("current")


class _FsRmColdStandby_Type(Integer32):
    """Custom type fsRmColdStandby based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FsRmColdStandby_Type.__name__ = "Integer32"
_FsRmColdStandby_Object = MibScalar
fsRmColdStandby = _FsRmColdStandby_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 15),
    _FsRmColdStandby_Type()
)
fsRmColdStandby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmColdStandby.setStatus("current")


class _FsRmModuleTrc_Type(Unsigned32):
    """Custom type fsRmModuleTrc based on Unsigned32"""
    defaultValue = 8388607


_FsRmModuleTrc_Type.__name__ = "Unsigned32"
_FsRmModuleTrc_Object = MibScalar
fsRmModuleTrc = _FsRmModuleTrc_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 16),
    _FsRmModuleTrc_Type()
)
fsRmModuleTrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmModuleTrc.setStatus("current")


class _FsRmProtocolRestartFlag_Type(TruthValue):
    """Custom type fsRmProtocolRestartFlag based on TruthValue"""
    defaultValue = 2


_FsRmProtocolRestartFlag_Type.__name__ = "TruthValue"
_FsRmProtocolRestartFlag_Object = MibScalar
fsRmProtocolRestartFlag = _FsRmProtocolRestartFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 17),
    _FsRmProtocolRestartFlag_Type()
)
fsRmProtocolRestartFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmProtocolRestartFlag.setStatus("current")


class _FsRmProtocolRestartRetryCnt_Type(Unsigned32):
    """Custom type fsRmProtocolRestartRetryCnt based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsRmProtocolRestartRetryCnt_Type.__name__ = "Unsigned32"
_FsRmProtocolRestartRetryCnt_Object = MibScalar
fsRmProtocolRestartRetryCnt = _FsRmProtocolRestartRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 18),
    _FsRmProtocolRestartRetryCnt_Type()
)
fsRmProtocolRestartRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmProtocolRestartRetryCnt.setStatus("current")


class _FsRmHitlessRestartFlag_Type(Integer32):
    """Custom type fsRmHitlessRestartFlag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("store", 1),
          ("restore", 2))
    )


_FsRmHitlessRestartFlag_Type.__name__ = "Integer32"
_FsRmHitlessRestartFlag_Object = MibScalar
fsRmHitlessRestartFlag = _FsRmHitlessRestartFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 19),
    _FsRmHitlessRestartFlag_Type()
)
fsRmHitlessRestartFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmHitlessRestartFlag.setStatus("current")


class _FsRmIpAddress_Type(IpAddress):
    """Custom type fsRmIpAddress based on IpAddress"""
    defaultHexValue = "A9FE0101"


_FsRmIpAddress_Type.__name__ = "IpAddress"
_FsRmIpAddress_Object = MibScalar
fsRmIpAddress = _FsRmIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 20),
    _FsRmIpAddress_Type()
)
fsRmIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmIpAddress.setStatus("current")


class _FsRmSubnetMask_Type(IpAddress):
    """Custom type fsRmSubnetMask based on IpAddress"""
    defaultHexValue = "FF000000"


_FsRmSubnetMask_Type.__name__ = "IpAddress"
_FsRmSubnetMask_Object = MibScalar
fsRmSubnetMask = _FsRmSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 21),
    _FsRmSubnetMask_Type()
)
fsRmSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmSubnetMask.setStatus("current")
_FsRmStackInterface_Type = DisplayString
_FsRmStackInterface_Object = MibScalar
fsRmStackInterface = _FsRmStackInterface_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 1, 22),
    _FsRmStackInterface_Type()
)
fsRmStackInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmStackInterface.setStatus("current")
_FsRmTrap_ObjectIdentity = ObjectIdentity
fsRmTrap = _FsRmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 2)
)


class _FsRmTrapModuleId_Type(DisplayString):
    """Custom type fsRmTrapModuleId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsRmTrapModuleId_Type.__name__ = "DisplayString"
_FsRmTrapModuleId_Object = MibScalar
fsRmTrapModuleId = _FsRmTrapModuleId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 2, 1),
    _FsRmTrapModuleId_Type()
)
fsRmTrapModuleId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRmTrapModuleId.setStatus("current")


class _FsRmTrapOperation_Type(Integer32):
    """Custom type fsRmTrapOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("syncUp", 1),
          ("switchOver", 2),
          ("peerAttach", 3),
          ("peerDetach", 4),
          ("hrStart", 5),
          ("hrStop", 6))
    )


_FsRmTrapOperation_Type.__name__ = "Integer32"
_FsRmTrapOperation_Object = MibScalar
fsRmTrapOperation = _FsRmTrapOperation_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 2, 2),
    _FsRmTrapOperation_Type()
)
fsRmTrapOperation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRmTrapOperation.setStatus("current")


class _FsRmTrapOperationStatus_Type(Integer32):
    """Custom type fsRmTrapOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("started", 1),
          ("completed", 2),
          ("failed", 3))
    )


_FsRmTrapOperationStatus_Type.__name__ = "Integer32"
_FsRmTrapOperationStatus_Object = MibScalar
fsRmTrapOperationStatus = _FsRmTrapOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 2, 3),
    _FsRmTrapOperationStatus_Type()
)
fsRmTrapOperationStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRmTrapOperationStatus.setStatus("current")


class _FsRmTrapError_Type(Integer32):
    """Custom type fsRmTrapError based on Integer32"""
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
        *(("none", 1),
          ("memAllocFailed", 2),
          ("sendFailed", 3),
          ("processFailed", 4))
    )


_FsRmTrapError_Type.__name__ = "Integer32"
_FsRmTrapError_Object = MibScalar
fsRmTrapError = _FsRmTrapError_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 2, 4),
    _FsRmTrapError_Type()
)
fsRmTrapError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRmTrapError.setStatus("current")


class _FsRmTrapEventTime_Type(DisplayString):
    """Custom type fsRmTrapEventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )
    fixed_length = 24


_FsRmTrapEventTime_Type.__name__ = "DisplayString"
_FsRmTrapEventTime_Object = MibScalar
fsRmTrapEventTime = _FsRmTrapEventTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 2, 5),
    _FsRmTrapEventTime_Type()
)
fsRmTrapEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRmTrapEventTime.setStatus("current")


class _FsRmTrapErrorStr_Type(DisplayString):
    """Custom type fsRmTrapErrorStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FsRmTrapErrorStr_Type.__name__ = "DisplayString"
_FsRmTrapErrorStr_Object = MibScalar
fsRmTrapErrorStr = _FsRmTrapErrorStr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 2, 6),
    _FsRmTrapErrorStr_Type()
)
fsRmTrapErrorStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRmTrapErrorStr.setStatus("current")


class _FsRmTrapSwitchId_Type(Integer32):
    """Custom type fsRmTrapSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsRmTrapSwitchId_Type.__name__ = "Integer32"
_FsRmTrapSwitchId_Object = MibScalar
fsRmTrapSwitchId = _FsRmTrapSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 2, 7),
    _FsRmTrapSwitchId_Type()
)
fsRmTrapSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmTrapSwitchId.setStatus("current")
_FsRmStatistics_ObjectIdentity = ObjectIdentity
fsRmStatistics = _FsRmStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 3)
)
_FsRmStatsSyncMsgTxCount_Type = ZeroBasedCounter32
_FsRmStatsSyncMsgTxCount_Object = MibScalar
fsRmStatsSyncMsgTxCount = _FsRmStatsSyncMsgTxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 3, 1),
    _FsRmStatsSyncMsgTxCount_Type()
)
fsRmStatsSyncMsgTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmStatsSyncMsgTxCount.setStatus("current")
_FsRmStatsSyncMsgTxFailedCount_Type = ZeroBasedCounter32
_FsRmStatsSyncMsgTxFailedCount_Object = MibScalar
fsRmStatsSyncMsgTxFailedCount = _FsRmStatsSyncMsgTxFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 3, 2),
    _FsRmStatsSyncMsgTxFailedCount_Type()
)
fsRmStatsSyncMsgTxFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmStatsSyncMsgTxFailedCount.setStatus("current")
_FsRmStatsSyncMsgRxCount_Type = ZeroBasedCounter32
_FsRmStatsSyncMsgRxCount_Object = MibScalar
fsRmStatsSyncMsgRxCount = _FsRmStatsSyncMsgRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 3, 3),
    _FsRmStatsSyncMsgRxCount_Type()
)
fsRmStatsSyncMsgRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmStatsSyncMsgRxCount.setStatus("current")
_FsRmStatsSyncMsgProcCount_Type = ZeroBasedCounter32
_FsRmStatsSyncMsgProcCount_Object = MibScalar
fsRmStatsSyncMsgProcCount = _FsRmStatsSyncMsgProcCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 3, 4),
    _FsRmStatsSyncMsgProcCount_Type()
)
fsRmStatsSyncMsgProcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmStatsSyncMsgProcCount.setStatus("current")
_FsRmStatsSyncMsgMissedCount_Type = ZeroBasedCounter32
_FsRmStatsSyncMsgMissedCount_Object = MibScalar
fsRmStatsSyncMsgMissedCount = _FsRmStatsSyncMsgMissedCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 3, 5),
    _FsRmStatsSyncMsgMissedCount_Type()
)
fsRmStatsSyncMsgMissedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmStatsSyncMsgMissedCount.setStatus("current")
_FsRmStatsConfSyncMsgFailCount_Type = ZeroBasedCounter32
_FsRmStatsConfSyncMsgFailCount_Object = MibScalar
fsRmStatsConfSyncMsgFailCount = _FsRmStatsConfSyncMsgFailCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 3, 6),
    _FsRmStatsConfSyncMsgFailCount_Type()
)
fsRmStatsConfSyncMsgFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmStatsConfSyncMsgFailCount.setStatus("current")
_FsRmTest_ObjectIdentity = ObjectIdentity
fsRmTest = _FsRmTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 4)
)
_FsRmSwitchoverTimeTable_Object = MibTable
fsRmSwitchoverTimeTable = _FsRmSwitchoverTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 4, 1)
)
if mibBuilder.loadTexts:
    fsRmSwitchoverTimeTable.setStatus("current")
_FsRmSwitchoverTimeEntry_Object = MibTableRow
fsRmSwitchoverTimeEntry = _FsRmSwitchoverTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 4, 1, 1)
)
fsRmSwitchoverTimeEntry.setIndexNames(
    (0, "SUPERMICRO-RM-MIB", "fsRmAppId"),
)
if mibBuilder.loadTexts:
    fsRmSwitchoverTimeEntry.setStatus("current")


class _FsRmAppId_Type(Integer32):
    """Custom type fsRmAppId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsRmAppId_Type.__name__ = "Integer32"
_FsRmAppId_Object = MibTableColumn
fsRmAppId = _FsRmAppId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 4, 1, 1, 1),
    _FsRmAppId_Type()
)
fsRmAppId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRmAppId.setStatus("current")
_FsRmAppName_Type = DisplayString
_FsRmAppName_Object = MibTableColumn
fsRmAppName = _FsRmAppName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 4, 1, 1, 2),
    _FsRmAppName_Type()
)
fsRmAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmAppName.setStatus("current")
_FsRmEntryTime_Type = TimeTicks
_FsRmEntryTime_Object = MibTableColumn
fsRmEntryTime = _FsRmEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 4, 1, 1, 3),
    _FsRmEntryTime_Type()
)
fsRmEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmEntryTime.setStatus("current")
_FsRmExitTime_Type = TimeTicks
_FsRmExitTime_Object = MibTableColumn
fsRmExitTime = _FsRmExitTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 4, 1, 1, 4),
    _FsRmExitTime_Type()
)
fsRmExitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmExitTime.setStatus("current")
_FsRmSwitchoverTime_Type = TimeTicks
_FsRmSwitchoverTime_Object = MibTableColumn
fsRmSwitchoverTime = _FsRmSwitchoverTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 4, 1, 1, 5),
    _FsRmSwitchoverTime_Type()
)
fsRmSwitchoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRmSwitchoverTime.setStatus("current")

# Managed Objects groups


# Notification objects

fsRmTrapEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 99, 0, 1)
)
fsRmTrapEvent.setObjects(
      *(("SUPERMICRO-RM-MIB", "fsRmSelfNodeId"),
        ("SUPERMICRO-RM-MIB", "fsRmNodeState"),
        ("SUPERMICRO-RM-MIB", "fsRmTrapModuleId"),
        ("SUPERMICRO-RM-MIB", "fsRmTrapOperation"),
        ("SUPERMICRO-RM-MIB", "fsRmTrapOperationStatus"),
        ("SUPERMICRO-RM-MIB", "fsRmTrapError"),
        ("SUPERMICRO-RM-MIB", "fsRmTrapEventTime"),
        ("SUPERMICRO-RM-MIB", "fsRmTrapErrorStr"),
        ("SUPERMICRO-RM-MIB", "fsRmTrapSwitchId"))
)
if mibBuilder.loadTexts:
    fsRmTrapEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-RM-MIB",
    **{"FsRmState": FsRmState,
       "fsRmMIB": fsRmMIB,
       "fsRmNotifications": fsRmNotifications,
       "fsRmTrapEvent": fsRmTrapEvent,
       "fsRm": fsRm,
       "fsRmSelfNodeId": fsRmSelfNodeId,
       "fsRmPeerNodeId": fsRmPeerNodeId,
       "fsRmActiveNodeId": fsRmActiveNodeId,
       "fsRmNodeState": fsRmNodeState,
       "fsRmHbInterval": fsRmHbInterval,
       "fsRmPeerDeadInterval": fsRmPeerDeadInterval,
       "fsRmTrcLevel": fsRmTrcLevel,
       "fsRmForceSwitchoverFlag": fsRmForceSwitchoverFlag,
       "fsRmPeerDeadIntMultiplier": fsRmPeerDeadIntMultiplier,
       "fsRmSwitchId": fsRmSwitchId,
       "fsRmConfiguredState": fsRmConfiguredState,
       "fsRmStackMacAddr": fsRmStackMacAddr,
       "fsRmPeerTable": fsRmPeerTable,
       "fsRmPeerTableEntry": fsRmPeerTableEntry,
       "fsRmPeerSwitchId": fsRmPeerSwitchId,
       "fsRmPeerStackIpAddr": fsRmPeerStackIpAddr,
       "fsRmPeerStackMacAddr": fsRmPeerStackMacAddr,
       "fsRmPeerSwitchBaseMacAddr": fsRmPeerSwitchBaseMacAddr,
       "fsRmStackPortCount": fsRmStackPortCount,
       "fsRmColdStandby": fsRmColdStandby,
       "fsRmModuleTrc": fsRmModuleTrc,
       "fsRmProtocolRestartFlag": fsRmProtocolRestartFlag,
       "fsRmProtocolRestartRetryCnt": fsRmProtocolRestartRetryCnt,
       "fsRmHitlessRestartFlag": fsRmHitlessRestartFlag,
       "fsRmIpAddress": fsRmIpAddress,
       "fsRmSubnetMask": fsRmSubnetMask,
       "fsRmStackInterface": fsRmStackInterface,
       "fsRmTrap": fsRmTrap,
       "fsRmTrapModuleId": fsRmTrapModuleId,
       "fsRmTrapOperation": fsRmTrapOperation,
       "fsRmTrapOperationStatus": fsRmTrapOperationStatus,
       "fsRmTrapError": fsRmTrapError,
       "fsRmTrapEventTime": fsRmTrapEventTime,
       "fsRmTrapErrorStr": fsRmTrapErrorStr,
       "fsRmTrapSwitchId": fsRmTrapSwitchId,
       "fsRmStatistics": fsRmStatistics,
       "fsRmStatsSyncMsgTxCount": fsRmStatsSyncMsgTxCount,
       "fsRmStatsSyncMsgTxFailedCount": fsRmStatsSyncMsgTxFailedCount,
       "fsRmStatsSyncMsgRxCount": fsRmStatsSyncMsgRxCount,
       "fsRmStatsSyncMsgProcCount": fsRmStatsSyncMsgProcCount,
       "fsRmStatsSyncMsgMissedCount": fsRmStatsSyncMsgMissedCount,
       "fsRmStatsConfSyncMsgFailCount": fsRmStatsConfSyncMsgFailCount,
       "fsRmTest": fsRmTest,
       "fsRmSwitchoverTimeTable": fsRmSwitchoverTimeTable,
       "fsRmSwitchoverTimeEntry": fsRmSwitchoverTimeEntry,
       "fsRmAppId": fsRmAppId,
       "fsRmAppName": fsRmAppName,
       "fsRmEntryTime": fsRmEntryTime,
       "fsRmExitTime": fsRmExitTime,
       "fsRmSwitchoverTime": fsRmSwitchoverTime}
)
