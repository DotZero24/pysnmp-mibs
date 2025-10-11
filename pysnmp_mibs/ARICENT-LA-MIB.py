# SNMP MIB module (ARICENT-LA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-LA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:35 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

fsla = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 63)
)
if mibBuilder.loadTexts:
    fsla.setRevisions(
        ("2014-03-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PortLaMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lacp", 1),
          ("manual", 2),
          ("disable", 3))
    )



class LacpKey(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class LacpState(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("lacpActivity", 0),
          ("lacpTimeout", 1),
          ("aggregation", 2),
          ("synchronization", 3),
          ("collecting", 4),
          ("distributing", 5),
          ("defaulted", 6),
          ("expired", 7))
    )


# MIB Managed Objects in the order of their OIDs

_FsLaSystem_ObjectIdentity = ObjectIdentity
fsLaSystem = _FsLaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1)
)


class _FsLaSystemControl_Type(Integer32):
    """Custom type fsLaSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsLaSystemControl_Type.__name__ = "Integer32"
_FsLaSystemControl_Object = MibScalar
fsLaSystemControl = _FsLaSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 1),
    _FsLaSystemControl_Type()
)
fsLaSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaSystemControl.setStatus("current")


class _FsLaStatus_Type(Integer32):
    """Custom type fsLaStatus based on Integer32"""
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


_FsLaStatus_Type.__name__ = "Integer32"
_FsLaStatus_Object = MibScalar
fsLaStatus = _FsLaStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 2),
    _FsLaStatus_Type()
)
fsLaStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaStatus.setStatus("current")


class _FsLaTraceOption_Type(Integer32):
    """Custom type fsLaTraceOption based on Integer32"""
    defaultValue = 0


_FsLaTraceOption_Type.__name__ = "Integer32"
_FsLaTraceOption_Object = MibScalar
fsLaTraceOption = _FsLaTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 3),
    _FsLaTraceOption_Type()
)
fsLaTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaTraceOption.setStatus("current")
_FsLaMaxPortsPerPortChannel_Type = Integer32
_FsLaMaxPortsPerPortChannel_Object = MibScalar
fsLaMaxPortsPerPortChannel = _FsLaMaxPortsPerPortChannel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 4),
    _FsLaMaxPortsPerPortChannel_Type()
)
fsLaMaxPortsPerPortChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaMaxPortsPerPortChannel.setStatus("current")
_FsLaMaxPortChannels_Type = Integer32
_FsLaMaxPortChannels_Object = MibScalar
fsLaMaxPortChannels = _FsLaMaxPortChannels_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 5),
    _FsLaMaxPortChannels_Type()
)
fsLaMaxPortChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaMaxPortChannels.setStatus("current")


class _FsLaOperStatus_Type(Integer32):
    """Custom type fsLaOperStatus based on Integer32"""
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


_FsLaOperStatus_Type.__name__ = "Integer32"
_FsLaOperStatus_Object = MibScalar
fsLaOperStatus = _FsLaOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 6),
    _FsLaOperStatus_Type()
)
fsLaOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaOperStatus.setStatus("current")
_FsLaActorSystemID_Type = MacAddress
_FsLaActorSystemID_Object = MibScalar
fsLaActorSystemID = _FsLaActorSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 7),
    _FsLaActorSystemID_Type()
)
fsLaActorSystemID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaActorSystemID.setStatus("current")


class _FsLaNoPartnerIndep_Type(Integer32):
    """Custom type fsLaNoPartnerIndep based on Integer32"""
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


_FsLaNoPartnerIndep_Type.__name__ = "Integer32"
_FsLaNoPartnerIndep_Object = MibScalar
fsLaNoPartnerIndep = _FsLaNoPartnerIndep_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 8),
    _FsLaNoPartnerIndep_Type()
)
fsLaNoPartnerIndep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaNoPartnerIndep.setStatus("current")


class _FsLaDLAGSystemStatus_Type(Integer32):
    """Custom type fsLaDLAGSystemStatus based on Integer32"""
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


_FsLaDLAGSystemStatus_Type.__name__ = "Integer32"
_FsLaDLAGSystemStatus_Object = MibScalar
fsLaDLAGSystemStatus = _FsLaDLAGSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 9),
    _FsLaDLAGSystemStatus_Type()
)
fsLaDLAGSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaDLAGSystemStatus.setStatus("current")
_FsLaDLAGSystemID_Type = MacAddress
_FsLaDLAGSystemID_Object = MibScalar
fsLaDLAGSystemID = _FsLaDLAGSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 10),
    _FsLaDLAGSystemID_Type()
)
fsLaDLAGSystemID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaDLAGSystemID.setStatus("current")


class _FsLaDLAGSystemPriority_Type(Integer32):
    """Custom type fsLaDLAGSystemPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsLaDLAGSystemPriority_Type.__name__ = "Integer32"
_FsLaDLAGSystemPriority_Object = MibScalar
fsLaDLAGSystemPriority = _FsLaDLAGSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 11),
    _FsLaDLAGSystemPriority_Type()
)
fsLaDLAGSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaDLAGSystemPriority.setStatus("current")


class _FsLaDLAGPeriodicSyncTime_Type(Unsigned32):
    """Custom type fsLaDLAGPeriodicSyncTime based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_FsLaDLAGPeriodicSyncTime_Type.__name__ = "Unsigned32"
_FsLaDLAGPeriodicSyncTime_Object = MibScalar
fsLaDLAGPeriodicSyncTime = _FsLaDLAGPeriodicSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 12),
    _FsLaDLAGPeriodicSyncTime_Type()
)
fsLaDLAGPeriodicSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaDLAGPeriodicSyncTime.setStatus("current")
if mibBuilder.loadTexts:
    fsLaDLAGPeriodicSyncTime.setUnits("seconds")


class _FsLaDLAGRolePlayed_Type(Integer32):
    """Custom type fsLaDLAGRolePlayed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("master", 1),
          ("slave", 2))
    )


_FsLaDLAGRolePlayed_Type.__name__ = "Integer32"
_FsLaDLAGRolePlayed_Object = MibScalar
fsLaDLAGRolePlayed = _FsLaDLAGRolePlayed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 13),
    _FsLaDLAGRolePlayed_Type()
)
fsLaDLAGRolePlayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaDLAGRolePlayed.setStatus("current")
_FsLaDLAGDistributingPortIndex_Type = InterfaceIndexOrZero
_FsLaDLAGDistributingPortIndex_Object = MibScalar
fsLaDLAGDistributingPortIndex = _FsLaDLAGDistributingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 14),
    _FsLaDLAGDistributingPortIndex_Type()
)
fsLaDLAGDistributingPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaDLAGDistributingPortIndex.setStatus("current")
_FsLaDLAGDistributingPortList_Type = PortList
_FsLaDLAGDistributingPortList_Object = MibScalar
fsLaDLAGDistributingPortList = _FsLaDLAGDistributingPortList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 15),
    _FsLaDLAGDistributingPortList_Type()
)
fsLaDLAGDistributingPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaDLAGDistributingPortList.setStatus("current")


class _FsLaMCLAGSystemStatus_Type(Integer32):
    """Custom type fsLaMCLAGSystemStatus based on Integer32"""
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


_FsLaMCLAGSystemStatus_Type.__name__ = "Integer32"
_FsLaMCLAGSystemStatus_Object = MibScalar
fsLaMCLAGSystemStatus = _FsLaMCLAGSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 16),
    _FsLaMCLAGSystemStatus_Type()
)
fsLaMCLAGSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaMCLAGSystemStatus.setStatus("current")


class _FsLaMCLAGSystemID_Type(MacAddress):
    """Custom type fsLaMCLAGSystemID based on MacAddress"""
    defaultHexValue = "000000000000"


_FsLaMCLAGSystemID_Type.__name__ = "MacAddress"
_FsLaMCLAGSystemID_Object = MibScalar
fsLaMCLAGSystemID = _FsLaMCLAGSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 17),
    _FsLaMCLAGSystemID_Type()
)
fsLaMCLAGSystemID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaMCLAGSystemID.setStatus("current")


class _FsLaMCLAGSystemPriority_Type(Integer32):
    """Custom type fsLaMCLAGSystemPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsLaMCLAGSystemPriority_Type.__name__ = "Integer32"
_FsLaMCLAGSystemPriority_Object = MibScalar
fsLaMCLAGSystemPriority = _FsLaMCLAGSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 18),
    _FsLaMCLAGSystemPriority_Type()
)
fsLaMCLAGSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaMCLAGSystemPriority.setStatus("current")


class _FsLaMCLAGPeriodicSyncTime_Type(Unsigned32):
    """Custom type fsLaMCLAGPeriodicSyncTime based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_FsLaMCLAGPeriodicSyncTime_Type.__name__ = "Unsigned32"
_FsLaMCLAGPeriodicSyncTime_Object = MibScalar
fsLaMCLAGPeriodicSyncTime = _FsLaMCLAGPeriodicSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 19),
    _FsLaMCLAGPeriodicSyncTime_Type()
)
fsLaMCLAGPeriodicSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaMCLAGPeriodicSyncTime.setStatus("current")
if mibBuilder.loadTexts:
    fsLaMCLAGPeriodicSyncTime.setUnits("seconds")


class _FsLaRecTmrDuration_Type(Unsigned32):
    """Custom type fsLaRecTmrDuration based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FsLaRecTmrDuration_Type.__name__ = "Unsigned32"
_FsLaRecTmrDuration_Object = MibScalar
fsLaRecTmrDuration = _FsLaRecTmrDuration_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 20),
    _FsLaRecTmrDuration_Type()
)
fsLaRecTmrDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaRecTmrDuration.setStatus("current")


class _FsLaRecThreshold_Type(Unsigned32):
    """Custom type fsLaRecThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_FsLaRecThreshold_Type.__name__ = "Unsigned32"
_FsLaRecThreshold_Object = MibScalar
fsLaRecThreshold = _FsLaRecThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 21),
    _FsLaRecThreshold_Type()
)
fsLaRecThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaRecThreshold.setStatus("current")
_FsLaTotalErrRecCount_Type = Counter32
_FsLaTotalErrRecCount_Object = MibScalar
fsLaTotalErrRecCount = _FsLaTotalErrRecCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 22),
    _FsLaTotalErrRecCount_Type()
)
fsLaTotalErrRecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaTotalErrRecCount.setStatus("current")


class _FsLaDefaultedStateThreshold_Type(Unsigned32):
    """Custom type fsLaDefaultedStateThreshold based on Unsigned32"""
    defaultValue = 5


_FsLaDefaultedStateThreshold_Type.__name__ = "Unsigned32"
_FsLaDefaultedStateThreshold_Object = MibScalar
fsLaDefaultedStateThreshold = _FsLaDefaultedStateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 23),
    _FsLaDefaultedStateThreshold_Type()
)
fsLaDefaultedStateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaDefaultedStateThreshold.setStatus("current")


class _FsLaHardwareFailureRecThreshold_Type(Unsigned32):
    """Custom type fsLaHardwareFailureRecThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_FsLaHardwareFailureRecThreshold_Type.__name__ = "Unsigned32"
_FsLaHardwareFailureRecThreshold_Object = MibScalar
fsLaHardwareFailureRecThreshold = _FsLaHardwareFailureRecThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 24),
    _FsLaHardwareFailureRecThreshold_Type()
)
fsLaHardwareFailureRecThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaHardwareFailureRecThreshold.setStatus("current")


class _FsLaSameStateRecThreshold_Type(Unsigned32):
    """Custom type fsLaSameStateRecThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_FsLaSameStateRecThreshold_Type.__name__ = "Unsigned32"
_FsLaSameStateRecThreshold_Object = MibScalar
fsLaSameStateRecThreshold = _FsLaSameStateRecThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 25),
    _FsLaSameStateRecThreshold_Type()
)
fsLaSameStateRecThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaSameStateRecThreshold.setStatus("current")


class _FsLaRecThresholdExceedAction_Type(Integer32):
    """Custom type fsLaRecThresholdExceedAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("shutdown", 2))
    )


_FsLaRecThresholdExceedAction_Type.__name__ = "Integer32"
_FsLaRecThresholdExceedAction_Object = MibScalar
fsLaRecThresholdExceedAction = _FsLaRecThresholdExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 26),
    _FsLaRecThresholdExceedAction_Type()
)
fsLaRecThresholdExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaRecThresholdExceedAction.setStatus("current")


class _FsLaMCLAGClearCounters_Type(TruthValue):
    """Custom type fsLaMCLAGClearCounters based on TruthValue"""
    defaultValue = 2


_FsLaMCLAGClearCounters_Type.__name__ = "TruthValue"
_FsLaMCLAGClearCounters_Object = MibScalar
fsLaMCLAGClearCounters = _FsLaMCLAGClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 1, 27),
    _FsLaMCLAGClearCounters_Type()
)
fsLaMCLAGClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaMCLAGClearCounters.setStatus("current")
_FsLaPortChannel_ObjectIdentity = ObjectIdentity
fsLaPortChannel = _FsLaPortChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2)
)
_FsLaPortChannelTable_Object = MibTable
fsLaPortChannelTable = _FsLaPortChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1)
)
if mibBuilder.loadTexts:
    fsLaPortChannelTable.setStatus("current")
_FsLaPortChannelEntry_Object = MibTableRow
fsLaPortChannelEntry = _FsLaPortChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1)
)
fsLaPortChannelEntry.setIndexNames(
    (0, "ARICENT-LA-MIB", "fsLaPortChannelIfIndex"),
)
if mibBuilder.loadTexts:
    fsLaPortChannelEntry.setStatus("current")
_FsLaPortChannelIfIndex_Type = InterfaceIndex
_FsLaPortChannelIfIndex_Object = MibTableColumn
fsLaPortChannelIfIndex = _FsLaPortChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 1),
    _FsLaPortChannelIfIndex_Type()
)
fsLaPortChannelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLaPortChannelIfIndex.setStatus("current")
_FsLaPortChannelGroup_Type = LacpKey
_FsLaPortChannelGroup_Object = MibTableColumn
fsLaPortChannelGroup = _FsLaPortChannelGroup_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 2),
    _FsLaPortChannelGroup_Type()
)
fsLaPortChannelGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelGroup.setStatus("current")
_FsLaPortChannelAdminMacAddress_Type = MacAddress
_FsLaPortChannelAdminMacAddress_Object = MibTableColumn
fsLaPortChannelAdminMacAddress = _FsLaPortChannelAdminMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 3),
    _FsLaPortChannelAdminMacAddress_Type()
)
fsLaPortChannelAdminMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortChannelAdminMacAddress.setStatus("deprecated")


class _FsLaPortChannelMacSelection_Type(Integer32):
    """Custom type fsLaPortChannelMacSelection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("force", 2))
    )


_FsLaPortChannelMacSelection_Type.__name__ = "Integer32"
_FsLaPortChannelMacSelection_Object = MibTableColumn
fsLaPortChannelMacSelection = _FsLaPortChannelMacSelection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 4),
    _FsLaPortChannelMacSelection_Type()
)
fsLaPortChannelMacSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortChannelMacSelection.setStatus("deprecated")
_FsLaPortChannelMode_Type = PortLaMode
_FsLaPortChannelMode_Object = MibTableColumn
fsLaPortChannelMode = _FsLaPortChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 5),
    _FsLaPortChannelMode_Type()
)
fsLaPortChannelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelMode.setStatus("current")
_FsLaPortChannelPortCount_Type = Integer32
_FsLaPortChannelPortCount_Object = MibTableColumn
fsLaPortChannelPortCount = _FsLaPortChannelPortCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 6),
    _FsLaPortChannelPortCount_Type()
)
fsLaPortChannelPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelPortCount.setStatus("current")
_FsLaPortChannelActivePortCount_Type = Integer32
_FsLaPortChannelActivePortCount_Object = MibTableColumn
fsLaPortChannelActivePortCount = _FsLaPortChannelActivePortCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 7),
    _FsLaPortChannelActivePortCount_Type()
)
fsLaPortChannelActivePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelActivePortCount.setStatus("current")


class _FsLaPortChannelSelectionPolicy_Type(Integer32):
    """Custom type fsLaPortChannelSelectionPolicy based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("macSrc", 1),
          ("macDst", 2),
          ("macSrcDst", 3),
          ("ipSrc", 4),
          ("ipDst", 5),
          ("ipSrcDst", 6),
          ("vlanId", 7),
          ("isid", 8),
          ("macSrcVid", 9),
          ("macDstVid", 10),
          ("macSrcDstVid", 11),
          ("mplsVcLabel", 12),
          ("mplsTunnelLabel", 13),
          ("mplsVcTunnelLabel", 14))
    )


_FsLaPortChannelSelectionPolicy_Type.__name__ = "Integer32"
_FsLaPortChannelSelectionPolicy_Object = MibTableColumn
fsLaPortChannelSelectionPolicy = _FsLaPortChannelSelectionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 8),
    _FsLaPortChannelSelectionPolicy_Type()
)
fsLaPortChannelSelectionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortChannelSelectionPolicy.setStatus("current")


class _FsLaPortChannelDefaultPortIndex_Type(InterfaceIndexOrZero):
    """Custom type fsLaPortChannelDefaultPortIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_FsLaPortChannelDefaultPortIndex_Type.__name__ = "InterfaceIndexOrZero"
_FsLaPortChannelDefaultPortIndex_Object = MibTableColumn
fsLaPortChannelDefaultPortIndex = _FsLaPortChannelDefaultPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 9),
    _FsLaPortChannelDefaultPortIndex_Type()
)
fsLaPortChannelDefaultPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortChannelDefaultPortIndex.setStatus("current")


class _FsLaPortChannelMaxPorts_Type(Integer32):
    """Custom type fsLaPortChannelMaxPorts based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8),
    )


_FsLaPortChannelMaxPorts_Type.__name__ = "Integer32"
_FsLaPortChannelMaxPorts_Object = MibTableColumn
fsLaPortChannelMaxPorts = _FsLaPortChannelMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 10),
    _FsLaPortChannelMaxPorts_Type()
)
fsLaPortChannelMaxPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortChannelMaxPorts.setStatus("current")
_FsLaPortChannelSelectionPolicyBitList_Type = Integer32
_FsLaPortChannelSelectionPolicyBitList_Object = MibTableColumn
fsLaPortChannelSelectionPolicyBitList = _FsLaPortChannelSelectionPolicyBitList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 11),
    _FsLaPortChannelSelectionPolicyBitList_Type()
)
fsLaPortChannelSelectionPolicyBitList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortChannelSelectionPolicyBitList.setStatus("current")
_FsLaPortChannelDLAGDistributingPortIndex_Type = InterfaceIndexOrZero
_FsLaPortChannelDLAGDistributingPortIndex_Object = MibTableColumn
fsLaPortChannelDLAGDistributingPortIndex = _FsLaPortChannelDLAGDistributingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 12),
    _FsLaPortChannelDLAGDistributingPortIndex_Type()
)
fsLaPortChannelDLAGDistributingPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortChannelDLAGDistributingPortIndex.setStatus("current")
_FsLaPortChannelDLAGSystemID_Type = MacAddress
_FsLaPortChannelDLAGSystemID_Object = MibTableColumn
fsLaPortChannelDLAGSystemID = _FsLaPortChannelDLAGSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 13),
    _FsLaPortChannelDLAGSystemID_Type()
)
fsLaPortChannelDLAGSystemID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortChannelDLAGSystemID.setStatus("current")


class _FsLaPortChannelDLAGSystemPriority_Type(Integer32):
    """Custom type fsLaPortChannelDLAGSystemPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsLaPortChannelDLAGSystemPriority_Type.__name__ = "Integer32"
_FsLaPortChannelDLAGSystemPriority_Object = MibTableColumn
fsLaPortChannelDLAGSystemPriority = _FsLaPortChannelDLAGSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 14),
    _FsLaPortChannelDLAGSystemPriority_Type()
)
fsLaPortChannelDLAGSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortChannelDLAGSystemPriority.setStatus("current")


class _FsLaPortChannelDLAGPeriodicSyncTime_Type(Unsigned32):
    """Custom type fsLaPortChannelDLAGPeriodicSyncTime based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90000),
    )


_FsLaPortChannelDLAGPeriodicSyncTime_Type.__name__ = "Unsigned32"
_FsLaPortChannelDLAGPeriodicSyncTime_Object = MibTableColumn
fsLaPortChannelDLAGPeriodicSyncTime = _FsLaPortChannelDLAGPeriodicSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 15),
    _FsLaPortChannelDLAGPeriodicSyncTime_Type()
)
fsLaPortChannelDLAGPeriodicSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortChannelDLAGPeriodicSyncTime.setStatus("current")
if mibBuilder.loadTexts:
    fsLaPortChannelDLAGPeriodicSyncTime.setUnits("milliseconds")


class _FsLaPortChannelDLAGMSSelectionWaitTime_Type(Unsigned32):
    """Custom type fsLaPortChannelDLAGMSSelectionWaitTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90000),
    )


_FsLaPortChannelDLAGMSSelectionWaitTime_Type.__name__ = "Unsigned32"
_FsLaPortChannelDLAGMSSelectionWaitTime_Object = MibTableColumn
fsLaPortChannelDLAGMSSelectionWaitTime = _FsLaPortChannelDLAGMSSelectionWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 16),
    _FsLaPortChannelDLAGMSSelectionWaitTime_Type()
)
fsLaPortChannelDLAGMSSelectionWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortChannelDLAGMSSelectionWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    fsLaPortChannelDLAGMSSelectionWaitTime.setUnits("milliseconds")


class _FsLaPortChannelDLAGRolePlayed_Type(Integer32):
    """Custom type fsLaPortChannelDLAGRolePlayed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("master", 1),
          ("slave", 2),
          ("backupmaster", 3))
    )


_FsLaPortChannelDLAGRolePlayed_Type.__name__ = "Integer32"
_FsLaPortChannelDLAGRolePlayed_Object = MibTableColumn
fsLaPortChannelDLAGRolePlayed = _FsLaPortChannelDLAGRolePlayed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 17),
    _FsLaPortChannelDLAGRolePlayed_Type()
)
fsLaPortChannelDLAGRolePlayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelDLAGRolePlayed.setStatus("current")


class _FsLaPortChannelDLAGStatus_Type(Integer32):
    """Custom type fsLaPortChannelDLAGStatus based on Integer32"""
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


_FsLaPortChannelDLAGStatus_Type.__name__ = "Integer32"
_FsLaPortChannelDLAGStatus_Object = MibTableColumn
fsLaPortChannelDLAGStatus = _FsLaPortChannelDLAGStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 18),
    _FsLaPortChannelDLAGStatus_Type()
)
fsLaPortChannelDLAGStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortChannelDLAGStatus.setStatus("current")


class _FsLaPortChannelDLAGRedundancy_Type(Integer32):
    """Custom type fsLaPortChannelDLAGRedundancy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_FsLaPortChannelDLAGRedundancy_Type.__name__ = "Integer32"
_FsLaPortChannelDLAGRedundancy_Object = MibTableColumn
fsLaPortChannelDLAGRedundancy = _FsLaPortChannelDLAGRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 19),
    _FsLaPortChannelDLAGRedundancy_Type()
)
fsLaPortChannelDLAGRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortChannelDLAGRedundancy.setStatus("current")


class _FsLaPortChannelDLAGMaxKeepAliveCount_Type(Integer32):
    """Custom type fsLaPortChannelDLAGMaxKeepAliveCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_FsLaPortChannelDLAGMaxKeepAliveCount_Type.__name__ = "Integer32"
_FsLaPortChannelDLAGMaxKeepAliveCount_Object = MibTableColumn
fsLaPortChannelDLAGMaxKeepAliveCount = _FsLaPortChannelDLAGMaxKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 20),
    _FsLaPortChannelDLAGMaxKeepAliveCount_Type()
)
fsLaPortChannelDLAGMaxKeepAliveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelDLAGMaxKeepAliveCount.setStatus("current")
_FsLaPortChannelDLAGPeriodicSyncPduTxCount_Type = Counter32
_FsLaPortChannelDLAGPeriodicSyncPduTxCount_Object = MibTableColumn
fsLaPortChannelDLAGPeriodicSyncPduTxCount = _FsLaPortChannelDLAGPeriodicSyncPduTxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 21),
    _FsLaPortChannelDLAGPeriodicSyncPduTxCount_Type()
)
fsLaPortChannelDLAGPeriodicSyncPduTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelDLAGPeriodicSyncPduTxCount.setStatus("current")
_FsLaPortChannelDLAGPeriodicSyncPduRxCount_Type = Counter32
_FsLaPortChannelDLAGPeriodicSyncPduRxCount_Object = MibTableColumn
fsLaPortChannelDLAGPeriodicSyncPduRxCount = _FsLaPortChannelDLAGPeriodicSyncPduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 22),
    _FsLaPortChannelDLAGPeriodicSyncPduRxCount_Type()
)
fsLaPortChannelDLAGPeriodicSyncPduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelDLAGPeriodicSyncPduRxCount.setStatus("current")
_FsLaPortChannelDLAGEventUpdatePduTxCount_Type = Counter32
_FsLaPortChannelDLAGEventUpdatePduTxCount_Object = MibTableColumn
fsLaPortChannelDLAGEventUpdatePduTxCount = _FsLaPortChannelDLAGEventUpdatePduTxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 23),
    _FsLaPortChannelDLAGEventUpdatePduTxCount_Type()
)
fsLaPortChannelDLAGEventUpdatePduTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelDLAGEventUpdatePduTxCount.setStatus("current")
_FsLaPortChannelDLAGEventUpdatePduRxCount_Type = Counter32
_FsLaPortChannelDLAGEventUpdatePduRxCount_Object = MibTableColumn
fsLaPortChannelDLAGEventUpdatePduRxCount = _FsLaPortChannelDLAGEventUpdatePduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 24),
    _FsLaPortChannelDLAGEventUpdatePduRxCount_Type()
)
fsLaPortChannelDLAGEventUpdatePduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelDLAGEventUpdatePduRxCount.setStatus("current")
_FsLaPortChannelDLAGElectedAsMasterCount_Type = Counter32
_FsLaPortChannelDLAGElectedAsMasterCount_Object = MibTableColumn
fsLaPortChannelDLAGElectedAsMasterCount = _FsLaPortChannelDLAGElectedAsMasterCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 25),
    _FsLaPortChannelDLAGElectedAsMasterCount_Type()
)
fsLaPortChannelDLAGElectedAsMasterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelDLAGElectedAsMasterCount.setStatus("current")
_FsLaPortChannelDLAGElectedAsSlaveCount_Type = Counter32
_FsLaPortChannelDLAGElectedAsSlaveCount_Object = MibTableColumn
fsLaPortChannelDLAGElectedAsSlaveCount = _FsLaPortChannelDLAGElectedAsSlaveCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 26),
    _FsLaPortChannelDLAGElectedAsSlaveCount_Type()
)
fsLaPortChannelDLAGElectedAsSlaveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelDLAGElectedAsSlaveCount.setStatus("current")
_FsLaPortChannelTrapTxCount_Type = Counter32
_FsLaPortChannelTrapTxCount_Object = MibTableColumn
fsLaPortChannelTrapTxCount = _FsLaPortChannelTrapTxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 27),
    _FsLaPortChannelTrapTxCount_Type()
)
fsLaPortChannelTrapTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelTrapTxCount.setStatus("current")
_FsLaPortChannelDLAGDistributingPortList_Type = PortList
_FsLaPortChannelDLAGDistributingPortList_Object = MibTableColumn
fsLaPortChannelDLAGDistributingPortList = _FsLaPortChannelDLAGDistributingPortList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 28),
    _FsLaPortChannelDLAGDistributingPortList_Type()
)
fsLaPortChannelDLAGDistributingPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortChannelDLAGDistributingPortList.setStatus("current")


class _FsLaPortChannelMCLAGStatus_Type(Integer32):
    """Custom type fsLaPortChannelMCLAGStatus based on Integer32"""
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


_FsLaPortChannelMCLAGStatus_Type.__name__ = "Integer32"
_FsLaPortChannelMCLAGStatus_Object = MibTableColumn
fsLaPortChannelMCLAGStatus = _FsLaPortChannelMCLAGStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 29),
    _FsLaPortChannelMCLAGStatus_Type()
)
fsLaPortChannelMCLAGStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortChannelMCLAGStatus.setStatus("current")


class _FsLaPortChannelMCLAGSystemID_Type(MacAddress):
    """Custom type fsLaPortChannelMCLAGSystemID based on MacAddress"""
    defaultHexValue = "000000000000"


_FsLaPortChannelMCLAGSystemID_Type.__name__ = "MacAddress"
_FsLaPortChannelMCLAGSystemID_Object = MibTableColumn
fsLaPortChannelMCLAGSystemID = _FsLaPortChannelMCLAGSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 30),
    _FsLaPortChannelMCLAGSystemID_Type()
)
fsLaPortChannelMCLAGSystemID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortChannelMCLAGSystemID.setStatus("current")


class _FsLaPortChannelMCLAGSystemPriority_Type(Integer32):
    """Custom type fsLaPortChannelMCLAGSystemPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsLaPortChannelMCLAGSystemPriority_Type.__name__ = "Integer32"
_FsLaPortChannelMCLAGSystemPriority_Object = MibTableColumn
fsLaPortChannelMCLAGSystemPriority = _FsLaPortChannelMCLAGSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 31),
    _FsLaPortChannelMCLAGSystemPriority_Type()
)
fsLaPortChannelMCLAGSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortChannelMCLAGSystemPriority.setStatus("current")


class _FsLaPortChannelMCLAGRolePlayed_Type(Integer32):
    """Custom type fsLaPortChannelMCLAGRolePlayed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("master", 1),
          ("slave", 2))
    )


_FsLaPortChannelMCLAGRolePlayed_Type.__name__ = "Integer32"
_FsLaPortChannelMCLAGRolePlayed_Object = MibTableColumn
fsLaPortChannelMCLAGRolePlayed = _FsLaPortChannelMCLAGRolePlayed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 32),
    _FsLaPortChannelMCLAGRolePlayed_Type()
)
fsLaPortChannelMCLAGRolePlayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelMCLAGRolePlayed.setStatus("current")


class _FsLaPortChannelMCLAGMaxKeepAliveCount_Type(Integer32):
    """Custom type fsLaPortChannelMCLAGMaxKeepAliveCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_FsLaPortChannelMCLAGMaxKeepAliveCount_Type.__name__ = "Integer32"
_FsLaPortChannelMCLAGMaxKeepAliveCount_Object = MibTableColumn
fsLaPortChannelMCLAGMaxKeepAliveCount = _FsLaPortChannelMCLAGMaxKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 33),
    _FsLaPortChannelMCLAGMaxKeepAliveCount_Type()
)
fsLaPortChannelMCLAGMaxKeepAliveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelMCLAGMaxKeepAliveCount.setStatus("current")
_FsLaPortChannelMCLAGPeriodicSyncPduTxCount_Type = Counter32
_FsLaPortChannelMCLAGPeriodicSyncPduTxCount_Object = MibTableColumn
fsLaPortChannelMCLAGPeriodicSyncPduTxCount = _FsLaPortChannelMCLAGPeriodicSyncPduTxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 34),
    _FsLaPortChannelMCLAGPeriodicSyncPduTxCount_Type()
)
fsLaPortChannelMCLAGPeriodicSyncPduTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelMCLAGPeriodicSyncPduTxCount.setStatus("current")
_FsLaPortChannelMCLAGPeriodicSyncPduRxCount_Type = Counter32
_FsLaPortChannelMCLAGPeriodicSyncPduRxCount_Object = MibTableColumn
fsLaPortChannelMCLAGPeriodicSyncPduRxCount = _FsLaPortChannelMCLAGPeriodicSyncPduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 35),
    _FsLaPortChannelMCLAGPeriodicSyncPduRxCount_Type()
)
fsLaPortChannelMCLAGPeriodicSyncPduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelMCLAGPeriodicSyncPduRxCount.setStatus("current")
_FsLaPortChannelMCLAGEventUpdatePduTxCount_Type = Counter32
_FsLaPortChannelMCLAGEventUpdatePduTxCount_Object = MibTableColumn
fsLaPortChannelMCLAGEventUpdatePduTxCount = _FsLaPortChannelMCLAGEventUpdatePduTxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 36),
    _FsLaPortChannelMCLAGEventUpdatePduTxCount_Type()
)
fsLaPortChannelMCLAGEventUpdatePduTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelMCLAGEventUpdatePduTxCount.setStatus("current")
_FsLaPortChannelMCLAGEventUpdatePduRxCount_Type = Counter32
_FsLaPortChannelMCLAGEventUpdatePduRxCount_Object = MibTableColumn
fsLaPortChannelMCLAGEventUpdatePduRxCount = _FsLaPortChannelMCLAGEventUpdatePduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 2, 1, 1, 37),
    _FsLaPortChannelMCLAGEventUpdatePduRxCount_Type()
)
fsLaPortChannelMCLAGEventUpdatePduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortChannelMCLAGEventUpdatePduRxCount.setStatus("current")
_FsLaPort_ObjectIdentity = ObjectIdentity
fsLaPort = _FsLaPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 63, 3)
)
_FsLaPortTable_Object = MibTable
fsLaPortTable = _FsLaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 3, 1)
)
if mibBuilder.loadTexts:
    fsLaPortTable.setStatus("current")
_FsLaPortEntry_Object = MibTableRow
fsLaPortEntry = _FsLaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 3, 1, 1)
)
fsLaPortEntry.setIndexNames(
    (0, "ARICENT-LA-MIB", "fsLaPortIndex"),
)
if mibBuilder.loadTexts:
    fsLaPortEntry.setStatus("current")
_FsLaPortIndex_Type = InterfaceIndex
_FsLaPortIndex_Object = MibTableColumn
fsLaPortIndex = _FsLaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 3, 1, 1, 1),
    _FsLaPortIndex_Type()
)
fsLaPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLaPortIndex.setStatus("current")
_FsLaPortMode_Type = PortLaMode
_FsLaPortMode_Object = MibTableColumn
fsLaPortMode = _FsLaPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 3, 1, 1, 2),
    _FsLaPortMode_Type()
)
fsLaPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortMode.setStatus("current")


class _FsLaPortBundleState_Type(Integer32):
    """Custom type fsLaPortBundleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("upInBndl", 0),
          ("standby", 1),
          ("down", 2),
          ("upIndividual", 3))
    )


_FsLaPortBundleState_Type.__name__ = "Integer32"
_FsLaPortBundleState_Object = MibTableColumn
fsLaPortBundleState = _FsLaPortBundleState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 3, 1, 1, 3),
    _FsLaPortBundleState_Type()
)
fsLaPortBundleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortBundleState.setStatus("current")
_FsLaPortActorResetAdminState_Type = LacpState
_FsLaPortActorResetAdminState_Object = MibTableColumn
fsLaPortActorResetAdminState = _FsLaPortActorResetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 3, 1, 1, 4),
    _FsLaPortActorResetAdminState_Type()
)
fsLaPortActorResetAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortActorResetAdminState.setStatus("current")


class _FsLaPortAggregateWaitTime_Type(TimeTicks):
    """Custom type fsLaPortAggregateWaitTime based on TimeTicks"""
    defaultValue = 2


_FsLaPortAggregateWaitTime_Type.__name__ = "TimeTicks"
_FsLaPortAggregateWaitTime_Object = MibTableColumn
fsLaPortAggregateWaitTime = _FsLaPortAggregateWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 3, 1, 1, 5),
    _FsLaPortAggregateWaitTime_Type()
)
fsLaPortAggregateWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortAggregateWaitTime.setStatus("current")
_FsLaPortPartnerResetAdminState_Type = LacpState
_FsLaPortPartnerResetAdminState_Object = MibTableColumn
fsLaPortPartnerResetAdminState = _FsLaPortPartnerResetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 3, 1, 1, 6),
    _FsLaPortPartnerResetAdminState_Type()
)
fsLaPortPartnerResetAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortPartnerResetAdminState.setStatus("current")


class _FsLaPortActorAdminPort_Type(Integer32):
    """Custom type fsLaPortActorAdminPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsLaPortActorAdminPort_Type.__name__ = "Integer32"
_FsLaPortActorAdminPort_Object = MibTableColumn
fsLaPortActorAdminPort = _FsLaPortActorAdminPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 3, 1, 1, 7),
    _FsLaPortActorAdminPort_Type()
)
fsLaPortActorAdminPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortActorAdminPort.setStatus("current")
_FsLaPortRestoreMtu_Type = Integer32
_FsLaPortRestoreMtu_Object = MibTableColumn
fsLaPortRestoreMtu = _FsLaPortRestoreMtu_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 3, 1, 1, 8),
    _FsLaPortRestoreMtu_Type()
)
fsLaPortRestoreMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortRestoreMtu.setStatus("current")


class _FsLaPortSelectAggregator_Type(Integer32):
    """Custom type fsLaPortSelectAggregator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic", 1))
    )


_FsLaPortSelectAggregator_Type.__name__ = "Integer32"
_FsLaPortSelectAggregator_Object = MibTableColumn
fsLaPortSelectAggregator = _FsLaPortSelectAggregator_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 3, 1, 1, 9),
    _FsLaPortSelectAggregator_Type()
)
fsLaPortSelectAggregator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortSelectAggregator.setStatus("current")
_FsLaPortErrStateDetCount_Type = Counter32
_FsLaPortErrStateDetCount_Object = MibTableColumn
fsLaPortErrStateDetCount = _FsLaPortErrStateDetCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 3, 1, 1, 10),
    _FsLaPortErrStateDetCount_Type()
)
fsLaPortErrStateDetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortErrStateDetCount.setStatus("current")
_FsLaPortErrStateRecCount_Type = Counter32
_FsLaPortErrStateRecCount_Object = MibTableColumn
fsLaPortErrStateRecCount = _FsLaPortErrStateRecCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 3, 1, 1, 11),
    _FsLaPortErrStateRecCount_Type()
)
fsLaPortErrStateRecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaPortErrStateRecCount.setStatus("current")


class _FsLaPortDefaultedStateThreshold_Type(Unsigned32):
    """Custom type fsLaPortDefaultedStateThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_FsLaPortDefaultedStateThreshold_Type.__name__ = "Unsigned32"
_FsLaPortDefaultedStateThreshold_Object = MibTableColumn
fsLaPortDefaultedStateThreshold = _FsLaPortDefaultedStateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 3, 1, 1, 12),
    _FsLaPortDefaultedStateThreshold_Type()
)
fsLaPortDefaultedStateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortDefaultedStateThreshold.setStatus("current")


class _FsLaPortHardwareFailureRecThreshold_Type(Unsigned32):
    """Custom type fsLaPortHardwareFailureRecThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_FsLaPortHardwareFailureRecThreshold_Type.__name__ = "Unsigned32"
_FsLaPortHardwareFailureRecThreshold_Object = MibTableColumn
fsLaPortHardwareFailureRecThreshold = _FsLaPortHardwareFailureRecThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 3, 1, 1, 13),
    _FsLaPortHardwareFailureRecThreshold_Type()
)
fsLaPortHardwareFailureRecThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortHardwareFailureRecThreshold.setStatus("current")


class _FsLaPortSameStateRecThreshold_Type(Unsigned32):
    """Custom type fsLaPortSameStateRecThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_FsLaPortSameStateRecThreshold_Type.__name__ = "Unsigned32"
_FsLaPortSameStateRecThreshold_Object = MibTableColumn
fsLaPortSameStateRecThreshold = _FsLaPortSameStateRecThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 3, 1, 1, 14),
    _FsLaPortSameStateRecThreshold_Type()
)
fsLaPortSameStateRecThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLaPortSameStateRecThreshold.setStatus("current")
_FsLaTrapObjects_ObjectIdentity = ObjectIdentity
fsLaTrapObjects = _FsLaTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 63, 4)
)
_FsLaHwFailTrapObjectsTable_Object = MibTable
fsLaHwFailTrapObjectsTable = _FsLaHwFailTrapObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 4, 1)
)
if mibBuilder.loadTexts:
    fsLaHwFailTrapObjectsTable.setStatus("current")
_FsLaHwFailTrapObjectsEntry_Object = MibTableRow
fsLaHwFailTrapObjectsEntry = _FsLaHwFailTrapObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 4, 1, 1)
)
fsLaHwFailTrapObjectsEntry.setIndexNames(
    (0, "ARICENT-LA-MIB", "fsLaTrapPortChannelIndex"),
    (0, "ARICENT-LA-MIB", "fsLaTrapPortIndex"),
)
if mibBuilder.loadTexts:
    fsLaHwFailTrapObjectsEntry.setStatus("current")
_FsLaTrapPortChannelIndex_Type = InterfaceIndex
_FsLaTrapPortChannelIndex_Object = MibTableColumn
fsLaTrapPortChannelIndex = _FsLaTrapPortChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 4, 1, 1, 1),
    _FsLaTrapPortChannelIndex_Type()
)
fsLaTrapPortChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLaTrapPortChannelIndex.setStatus("current")
_FsLaTrapPortIndex_Type = InterfaceIndexOrZero
_FsLaTrapPortIndex_Object = MibTableColumn
fsLaTrapPortIndex = _FsLaTrapPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 4, 1, 1, 2),
    _FsLaTrapPortIndex_Type()
)
fsLaTrapPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLaTrapPortIndex.setStatus("current")


class _FsLaHwFailTrapType_Type(Integer32):
    """Custom type fsLaHwFailTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("createAgg", 0),
          ("addLinkToAgg", 1),
          ("deleteAgg", 2),
          ("removeLinkFromAgg", 3),
          ("setSelectionPolicy", 4),
          ("enableCollection", 5),
          ("disableCollection", 6),
          ("enableDistribution", 7))
    )


_FsLaHwFailTrapType_Type.__name__ = "Integer32"
_FsLaHwFailTrapType_Object = MibTableColumn
fsLaHwFailTrapType = _FsLaHwFailTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 4, 1, 1, 3),
    _FsLaHwFailTrapType_Type()
)
fsLaHwFailTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaHwFailTrapType.setStatus("current")
_FsLaDLAGTrapObjectsTable_Object = MibTable
fsLaDLAGTrapObjectsTable = _FsLaDLAGTrapObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 4, 2)
)
if mibBuilder.loadTexts:
    fsLaDLAGTrapObjectsTable.setStatus("current")
_FsLaDLAGTrapObjectsEntry_Object = MibTableRow
fsLaDLAGTrapObjectsEntry = _FsLaDLAGTrapObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 4, 2, 1)
)
fsLaDLAGTrapObjectsEntry.setIndexNames(
    (0, "ARICENT-LA-MIB", "fsLaDLAGTrapPortChannelIndex"),
)
if mibBuilder.loadTexts:
    fsLaDLAGTrapObjectsEntry.setStatus("current")
_FsLaDLAGTrapPortChannelIndex_Type = InterfaceIndex
_FsLaDLAGTrapPortChannelIndex_Object = MibTableColumn
fsLaDLAGTrapPortChannelIndex = _FsLaDLAGTrapPortChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 4, 2, 1, 1),
    _FsLaDLAGTrapPortChannelIndex_Type()
)
fsLaDLAGTrapPortChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLaDLAGTrapPortChannelIndex.setStatus("current")


class _FsLaDLAGTrapType_Type(Integer32):
    """Custom type fsLaDLAGTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("mastertobackupmaster", 0),
          ("backupmastertomaster", 1),
          ("slavetobackupmaster", 2),
          ("backupmastertoslave", 3),
          ("mastertoslave", 4),
          ("slavetomaster", 5))
    )


_FsLaDLAGTrapType_Type.__name__ = "Integer32"
_FsLaDLAGTrapType_Object = MibTableColumn
fsLaDLAGTrapType = _FsLaDLAGTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 4, 2, 1, 2),
    _FsLaDLAGTrapType_Type()
)
fsLaDLAGTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaDLAGTrapType.setStatus("current")
_FsFutureLaTraps_ObjectIdentity = ObjectIdentity
fsFutureLaTraps = _FsFutureLaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 63, 5)
)
_FsLaTraps_ObjectIdentity = ObjectIdentity
fsLaTraps = _FsLaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 63, 5, 0)
)
_FsLaDLAGRemotePortChannel_ObjectIdentity = ObjectIdentity
fsLaDLAGRemotePortChannel = _FsLaDLAGRemotePortChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 63, 6)
)
_FsLaDLAGRemotePortChannelTable_Object = MibTable
fsLaDLAGRemotePortChannelTable = _FsLaDLAGRemotePortChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 6, 1)
)
if mibBuilder.loadTexts:
    fsLaDLAGRemotePortChannelTable.setStatus("current")
_FsLaDLAGRemotePortChannelEntry_Object = MibTableRow
fsLaDLAGRemotePortChannelEntry = _FsLaDLAGRemotePortChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 6, 1, 1)
)
fsLaDLAGRemotePortChannelEntry.setIndexNames(
    (0, "ARICENT-LA-MIB", "fsLaPortChannelIfIndex"),
    (0, "ARICENT-LA-MIB", "fsLaDLAGRemotePortChannelSystemID"),
)
if mibBuilder.loadTexts:
    fsLaDLAGRemotePortChannelEntry.setStatus("current")
_FsLaDLAGRemotePortChannelSystemID_Type = MacAddress
_FsLaDLAGRemotePortChannelSystemID_Object = MibTableColumn
fsLaDLAGRemotePortChannelSystemID = _FsLaDLAGRemotePortChannelSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 6, 1, 1, 1),
    _FsLaDLAGRemotePortChannelSystemID_Type()
)
fsLaDLAGRemotePortChannelSystemID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLaDLAGRemotePortChannelSystemID.setStatus("current")


class _FsLaDLAGRemotePortChannelSystemPriority_Type(Integer32):
    """Custom type fsLaDLAGRemotePortChannelSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsLaDLAGRemotePortChannelSystemPriority_Type.__name__ = "Integer32"
_FsLaDLAGRemotePortChannelSystemPriority_Object = MibTableColumn
fsLaDLAGRemotePortChannelSystemPriority = _FsLaDLAGRemotePortChannelSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 6, 1, 1, 2),
    _FsLaDLAGRemotePortChannelSystemPriority_Type()
)
fsLaDLAGRemotePortChannelSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaDLAGRemotePortChannelSystemPriority.setStatus("current")


class _FsLaDLAGRemotePortChannelRolePlayed_Type(Integer32):
    """Custom type fsLaDLAGRemotePortChannelRolePlayed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("master", 1),
          ("slave", 2),
          ("backupmaster", 3))
    )


_FsLaDLAGRemotePortChannelRolePlayed_Type.__name__ = "Integer32"
_FsLaDLAGRemotePortChannelRolePlayed_Object = MibTableColumn
fsLaDLAGRemotePortChannelRolePlayed = _FsLaDLAGRemotePortChannelRolePlayed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 6, 1, 1, 3),
    _FsLaDLAGRemotePortChannelRolePlayed_Type()
)
fsLaDLAGRemotePortChannelRolePlayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaDLAGRemotePortChannelRolePlayed.setStatus("current")
_FsLaDLAGRemotePortChannelKeepAliveCount_Type = Integer32
_FsLaDLAGRemotePortChannelKeepAliveCount_Object = MibTableColumn
fsLaDLAGRemotePortChannelKeepAliveCount = _FsLaDLAGRemotePortChannelKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 6, 1, 1, 4),
    _FsLaDLAGRemotePortChannelKeepAliveCount_Type()
)
fsLaDLAGRemotePortChannelKeepAliveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaDLAGRemotePortChannelKeepAliveCount.setStatus("current")
_FsLaDLAGRemotePortChannelSpeed_Type = Gauge32
_FsLaDLAGRemotePortChannelSpeed_Object = MibTableColumn
fsLaDLAGRemotePortChannelSpeed = _FsLaDLAGRemotePortChannelSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 6, 1, 1, 5),
    _FsLaDLAGRemotePortChannelSpeed_Type()
)
fsLaDLAGRemotePortChannelSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaDLAGRemotePortChannelSpeed.setStatus("current")
_FsLaDLAGRemotePortChannelHighSpeed_Type = Gauge32
_FsLaDLAGRemotePortChannelHighSpeed_Object = MibTableColumn
fsLaDLAGRemotePortChannelHighSpeed = _FsLaDLAGRemotePortChannelHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 6, 1, 1, 6),
    _FsLaDLAGRemotePortChannelHighSpeed_Type()
)
fsLaDLAGRemotePortChannelHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaDLAGRemotePortChannelHighSpeed.setStatus("current")
_FsLaDLAGRemotePortChannelMtu_Type = Integer32
_FsLaDLAGRemotePortChannelMtu_Object = MibTableColumn
fsLaDLAGRemotePortChannelMtu = _FsLaDLAGRemotePortChannelMtu_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 6, 1, 1, 7),
    _FsLaDLAGRemotePortChannelMtu_Type()
)
fsLaDLAGRemotePortChannelMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaDLAGRemotePortChannelMtu.setStatus("current")
_FsLaDLAGRemotePort_ObjectIdentity = ObjectIdentity
fsLaDLAGRemotePort = _FsLaDLAGRemotePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 63, 7)
)
_FsLaDLAGRemotePortTable_Object = MibTable
fsLaDLAGRemotePortTable = _FsLaDLAGRemotePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 7, 1)
)
if mibBuilder.loadTexts:
    fsLaDLAGRemotePortTable.setStatus("current")
_FsLaDLAGRemotePortEntry_Object = MibTableRow
fsLaDLAGRemotePortEntry = _FsLaDLAGRemotePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 7, 1, 1)
)
fsLaDLAGRemotePortEntry.setIndexNames(
    (0, "ARICENT-LA-MIB", "fsLaPortChannelIfIndex"),
    (0, "ARICENT-LA-MIB", "fsLaDLAGRemotePortChannelSystemID"),
    (0, "ARICENT-LA-MIB", "fsLaDLAGRemotePortIndex"),
)
if mibBuilder.loadTexts:
    fsLaDLAGRemotePortEntry.setStatus("current")
_FsLaDLAGRemotePortIndex_Type = InterfaceIndex
_FsLaDLAGRemotePortIndex_Object = MibTableColumn
fsLaDLAGRemotePortIndex = _FsLaDLAGRemotePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 7, 1, 1, 1),
    _FsLaDLAGRemotePortIndex_Type()
)
fsLaDLAGRemotePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLaDLAGRemotePortIndex.setStatus("current")


class _FsLaDLAGRemotePortBundleState_Type(Integer32):
    """Custom type fsLaDLAGRemotePortBundleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("upInBndl", 0),
          ("standby", 1),
          ("down", 2),
          ("upIndividual", 3))
    )


_FsLaDLAGRemotePortBundleState_Type.__name__ = "Integer32"
_FsLaDLAGRemotePortBundleState_Object = MibTableColumn
fsLaDLAGRemotePortBundleState = _FsLaDLAGRemotePortBundleState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 7, 1, 1, 2),
    _FsLaDLAGRemotePortBundleState_Type()
)
fsLaDLAGRemotePortBundleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaDLAGRemotePortBundleState.setStatus("current")


class _FsLaDLAGRemotePortSyncStatus_Type(Integer32):
    """Custom type fsLaDLAGRemotePortSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inSync", 1),
          ("outofSync", 2))
    )


_FsLaDLAGRemotePortSyncStatus_Type.__name__ = "Integer32"
_FsLaDLAGRemotePortSyncStatus_Object = MibTableColumn
fsLaDLAGRemotePortSyncStatus = _FsLaDLAGRemotePortSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 7, 1, 1, 3),
    _FsLaDLAGRemotePortSyncStatus_Type()
)
fsLaDLAGRemotePortSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaDLAGRemotePortSyncStatus.setStatus("current")


class _FsLaDLAGRemotePortPriority_Type(Integer32):
    """Custom type fsLaDLAGRemotePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsLaDLAGRemotePortPriority_Type.__name__ = "Integer32"
_FsLaDLAGRemotePortPriority_Object = MibTableColumn
fsLaDLAGRemotePortPriority = _FsLaDLAGRemotePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 7, 1, 1, 4),
    _FsLaDLAGRemotePortPriority_Type()
)
fsLaDLAGRemotePortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaDLAGRemotePortPriority.setStatus("current")
_FsLaMCLAGRemotePortChannel_ObjectIdentity = ObjectIdentity
fsLaMCLAGRemotePortChannel = _FsLaMCLAGRemotePortChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 63, 8)
)
_FsLaMCLAGRemotePortChannelTable_Object = MibTable
fsLaMCLAGRemotePortChannelTable = _FsLaMCLAGRemotePortChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 8, 1)
)
if mibBuilder.loadTexts:
    fsLaMCLAGRemotePortChannelTable.setStatus("current")
_FsLaMCLAGRemotePortChannelEntry_Object = MibTableRow
fsLaMCLAGRemotePortChannelEntry = _FsLaMCLAGRemotePortChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 8, 1, 1)
)
fsLaMCLAGRemotePortChannelEntry.setIndexNames(
    (0, "ARICENT-LA-MIB", "fsLaPortChannelIfIndex"),
    (0, "ARICENT-LA-MIB", "fsLaMCLAGRemotePortChannelSystemID"),
)
if mibBuilder.loadTexts:
    fsLaMCLAGRemotePortChannelEntry.setStatus("current")
_FsLaMCLAGRemotePortChannelSystemID_Type = MacAddress
_FsLaMCLAGRemotePortChannelSystemID_Object = MibTableColumn
fsLaMCLAGRemotePortChannelSystemID = _FsLaMCLAGRemotePortChannelSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 8, 1, 1, 1),
    _FsLaMCLAGRemotePortChannelSystemID_Type()
)
fsLaMCLAGRemotePortChannelSystemID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLaMCLAGRemotePortChannelSystemID.setStatus("current")


class _FsLaMCLAGRemotePortChannelSystemPriority_Type(Integer32):
    """Custom type fsLaMCLAGRemotePortChannelSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsLaMCLAGRemotePortChannelSystemPriority_Type.__name__ = "Integer32"
_FsLaMCLAGRemotePortChannelSystemPriority_Object = MibTableColumn
fsLaMCLAGRemotePortChannelSystemPriority = _FsLaMCLAGRemotePortChannelSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 8, 1, 1, 2),
    _FsLaMCLAGRemotePortChannelSystemPriority_Type()
)
fsLaMCLAGRemotePortChannelSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaMCLAGRemotePortChannelSystemPriority.setStatus("current")


class _FsLaMCLAGRemotePortChannelRolePlayed_Type(Integer32):
    """Custom type fsLaMCLAGRemotePortChannelRolePlayed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("master", 1),
          ("slave", 2))
    )


_FsLaMCLAGRemotePortChannelRolePlayed_Type.__name__ = "Integer32"
_FsLaMCLAGRemotePortChannelRolePlayed_Object = MibTableColumn
fsLaMCLAGRemotePortChannelRolePlayed = _FsLaMCLAGRemotePortChannelRolePlayed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 8, 1, 1, 3),
    _FsLaMCLAGRemotePortChannelRolePlayed_Type()
)
fsLaMCLAGRemotePortChannelRolePlayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaMCLAGRemotePortChannelRolePlayed.setStatus("current")
_FsLaMCLAGRemotePortChannelKeepAliveCount_Type = Integer32
_FsLaMCLAGRemotePortChannelKeepAliveCount_Object = MibTableColumn
fsLaMCLAGRemotePortChannelKeepAliveCount = _FsLaMCLAGRemotePortChannelKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 8, 1, 1, 4),
    _FsLaMCLAGRemotePortChannelKeepAliveCount_Type()
)
fsLaMCLAGRemotePortChannelKeepAliveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaMCLAGRemotePortChannelKeepAliveCount.setStatus("current")
_FsLaMCLAGRemotePortChannelSpeed_Type = Gauge32
_FsLaMCLAGRemotePortChannelSpeed_Object = MibTableColumn
fsLaMCLAGRemotePortChannelSpeed = _FsLaMCLAGRemotePortChannelSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 8, 1, 1, 5),
    _FsLaMCLAGRemotePortChannelSpeed_Type()
)
fsLaMCLAGRemotePortChannelSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaMCLAGRemotePortChannelSpeed.setStatus("current")
_FsLaMCLAGRemotePortChannelHighSpeed_Type = Gauge32
_FsLaMCLAGRemotePortChannelHighSpeed_Object = MibTableColumn
fsLaMCLAGRemotePortChannelHighSpeed = _FsLaMCLAGRemotePortChannelHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 8, 1, 1, 6),
    _FsLaMCLAGRemotePortChannelHighSpeed_Type()
)
fsLaMCLAGRemotePortChannelHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaMCLAGRemotePortChannelHighSpeed.setStatus("current")
_FsLaMCLAGRemotePortChannelMtu_Type = Integer32
_FsLaMCLAGRemotePortChannelMtu_Object = MibTableColumn
fsLaMCLAGRemotePortChannelMtu = _FsLaMCLAGRemotePortChannelMtu_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 8, 1, 1, 7),
    _FsLaMCLAGRemotePortChannelMtu_Type()
)
fsLaMCLAGRemotePortChannelMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaMCLAGRemotePortChannelMtu.setStatus("current")
_FsLaMCLAGRemotePort_ObjectIdentity = ObjectIdentity
fsLaMCLAGRemotePort = _FsLaMCLAGRemotePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 63, 9)
)
_FsLaMCLAGRemotePortTable_Object = MibTable
fsLaMCLAGRemotePortTable = _FsLaMCLAGRemotePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 9, 1)
)
if mibBuilder.loadTexts:
    fsLaMCLAGRemotePortTable.setStatus("current")
_FsLaMCLAGRemotePortEntry_Object = MibTableRow
fsLaMCLAGRemotePortEntry = _FsLaMCLAGRemotePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 9, 1, 1)
)
fsLaMCLAGRemotePortEntry.setIndexNames(
    (0, "ARICENT-LA-MIB", "fsLaPortChannelIfIndex"),
    (0, "ARICENT-LA-MIB", "fsLaMCLAGRemotePortChannelSystemID"),
    (0, "ARICENT-LA-MIB", "fsLaMCLAGRemotePortIndex"),
)
if mibBuilder.loadTexts:
    fsLaMCLAGRemotePortEntry.setStatus("current")
_FsLaMCLAGRemotePortIndex_Type = InterfaceIndex
_FsLaMCLAGRemotePortIndex_Object = MibTableColumn
fsLaMCLAGRemotePortIndex = _FsLaMCLAGRemotePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 9, 1, 1, 1),
    _FsLaMCLAGRemotePortIndex_Type()
)
fsLaMCLAGRemotePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLaMCLAGRemotePortIndex.setStatus("current")


class _FsLaMCLAGRemotePortSlotIndex_Type(Integer32):
    """Custom type fsLaMCLAGRemotePortSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsLaMCLAGRemotePortSlotIndex_Type.__name__ = "Integer32"
_FsLaMCLAGRemotePortSlotIndex_Object = MibTableColumn
fsLaMCLAGRemotePortSlotIndex = _FsLaMCLAGRemotePortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 9, 1, 1, 2),
    _FsLaMCLAGRemotePortSlotIndex_Type()
)
fsLaMCLAGRemotePortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaMCLAGRemotePortSlotIndex.setStatus("current")


class _FsLaMCLAGRemotePortBundleState_Type(Integer32):
    """Custom type fsLaMCLAGRemotePortBundleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("upInBndl", 0),
          ("standby", 1),
          ("down", 2),
          ("upIndividual", 3))
    )


_FsLaMCLAGRemotePortBundleState_Type.__name__ = "Integer32"
_FsLaMCLAGRemotePortBundleState_Object = MibTableColumn
fsLaMCLAGRemotePortBundleState = _FsLaMCLAGRemotePortBundleState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 9, 1, 1, 3),
    _FsLaMCLAGRemotePortBundleState_Type()
)
fsLaMCLAGRemotePortBundleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaMCLAGRemotePortBundleState.setStatus("current")


class _FsLaMCLAGRemotePortSyncStatus_Type(Integer32):
    """Custom type fsLaMCLAGRemotePortSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inSync", 1),
          ("outofSync", 2))
    )


_FsLaMCLAGRemotePortSyncStatus_Type.__name__ = "Integer32"
_FsLaMCLAGRemotePortSyncStatus_Object = MibTableColumn
fsLaMCLAGRemotePortSyncStatus = _FsLaMCLAGRemotePortSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 9, 1, 1, 4),
    _FsLaMCLAGRemotePortSyncStatus_Type()
)
fsLaMCLAGRemotePortSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaMCLAGRemotePortSyncStatus.setStatus("current")


class _FsLaMCLAGRemotePortPriority_Type(Integer32):
    """Custom type fsLaMCLAGRemotePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsLaMCLAGRemotePortPriority_Type.__name__ = "Integer32"
_FsLaMCLAGRemotePortPriority_Object = MibTableColumn
fsLaMCLAGRemotePortPriority = _FsLaMCLAGRemotePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 63, 9, 1, 1, 5),
    _FsLaMCLAGRemotePortPriority_Type()
)
fsLaMCLAGRemotePortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLaMCLAGRemotePortPriority.setStatus("current")

# Managed Objects groups


# Notification objects

fsLaHwFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 63, 5, 0, 1)
)
fsLaHwFailureTrap.setObjects(
    ("ARICENT-LA-MIB", "fsLaHwFailTrapType")
)
if mibBuilder.loadTexts:
    fsLaHwFailureTrap.setStatus(
        "current"
    )

fsLaDLAGTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 63, 5, 0, 2)
)
fsLaDLAGTrap.setObjects(
    ("ARICENT-LA-MIB", "fsLaDLAGTrapType")
)
if mibBuilder.loadTexts:
    fsLaDLAGTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-LA-MIB",
    **{"PortLaMode": PortLaMode,
       "LacpKey": LacpKey,
       "LacpState": LacpState,
       "fsla": fsla,
       "fsLaSystem": fsLaSystem,
       "fsLaSystemControl": fsLaSystemControl,
       "fsLaStatus": fsLaStatus,
       "fsLaTraceOption": fsLaTraceOption,
       "fsLaMaxPortsPerPortChannel": fsLaMaxPortsPerPortChannel,
       "fsLaMaxPortChannels": fsLaMaxPortChannels,
       "fsLaOperStatus": fsLaOperStatus,
       "fsLaActorSystemID": fsLaActorSystemID,
       "fsLaNoPartnerIndep": fsLaNoPartnerIndep,
       "fsLaDLAGSystemStatus": fsLaDLAGSystemStatus,
       "fsLaDLAGSystemID": fsLaDLAGSystemID,
       "fsLaDLAGSystemPriority": fsLaDLAGSystemPriority,
       "fsLaDLAGPeriodicSyncTime": fsLaDLAGPeriodicSyncTime,
       "fsLaDLAGRolePlayed": fsLaDLAGRolePlayed,
       "fsLaDLAGDistributingPortIndex": fsLaDLAGDistributingPortIndex,
       "fsLaDLAGDistributingPortList": fsLaDLAGDistributingPortList,
       "fsLaMCLAGSystemStatus": fsLaMCLAGSystemStatus,
       "fsLaMCLAGSystemID": fsLaMCLAGSystemID,
       "fsLaMCLAGSystemPriority": fsLaMCLAGSystemPriority,
       "fsLaMCLAGPeriodicSyncTime": fsLaMCLAGPeriodicSyncTime,
       "fsLaRecTmrDuration": fsLaRecTmrDuration,
       "fsLaRecThreshold": fsLaRecThreshold,
       "fsLaTotalErrRecCount": fsLaTotalErrRecCount,
       "fsLaDefaultedStateThreshold": fsLaDefaultedStateThreshold,
       "fsLaHardwareFailureRecThreshold": fsLaHardwareFailureRecThreshold,
       "fsLaSameStateRecThreshold": fsLaSameStateRecThreshold,
       "fsLaRecThresholdExceedAction": fsLaRecThresholdExceedAction,
       "fsLaMCLAGClearCounters": fsLaMCLAGClearCounters,
       "fsLaPortChannel": fsLaPortChannel,
       "fsLaPortChannelTable": fsLaPortChannelTable,
       "fsLaPortChannelEntry": fsLaPortChannelEntry,
       "fsLaPortChannelIfIndex": fsLaPortChannelIfIndex,
       "fsLaPortChannelGroup": fsLaPortChannelGroup,
       "fsLaPortChannelAdminMacAddress": fsLaPortChannelAdminMacAddress,
       "fsLaPortChannelMacSelection": fsLaPortChannelMacSelection,
       "fsLaPortChannelMode": fsLaPortChannelMode,
       "fsLaPortChannelPortCount": fsLaPortChannelPortCount,
       "fsLaPortChannelActivePortCount": fsLaPortChannelActivePortCount,
       "fsLaPortChannelSelectionPolicy": fsLaPortChannelSelectionPolicy,
       "fsLaPortChannelDefaultPortIndex": fsLaPortChannelDefaultPortIndex,
       "fsLaPortChannelMaxPorts": fsLaPortChannelMaxPorts,
       "fsLaPortChannelSelectionPolicyBitList": fsLaPortChannelSelectionPolicyBitList,
       "fsLaPortChannelDLAGDistributingPortIndex": fsLaPortChannelDLAGDistributingPortIndex,
       "fsLaPortChannelDLAGSystemID": fsLaPortChannelDLAGSystemID,
       "fsLaPortChannelDLAGSystemPriority": fsLaPortChannelDLAGSystemPriority,
       "fsLaPortChannelDLAGPeriodicSyncTime": fsLaPortChannelDLAGPeriodicSyncTime,
       "fsLaPortChannelDLAGMSSelectionWaitTime": fsLaPortChannelDLAGMSSelectionWaitTime,
       "fsLaPortChannelDLAGRolePlayed": fsLaPortChannelDLAGRolePlayed,
       "fsLaPortChannelDLAGStatus": fsLaPortChannelDLAGStatus,
       "fsLaPortChannelDLAGRedundancy": fsLaPortChannelDLAGRedundancy,
       "fsLaPortChannelDLAGMaxKeepAliveCount": fsLaPortChannelDLAGMaxKeepAliveCount,
       "fsLaPortChannelDLAGPeriodicSyncPduTxCount": fsLaPortChannelDLAGPeriodicSyncPduTxCount,
       "fsLaPortChannelDLAGPeriodicSyncPduRxCount": fsLaPortChannelDLAGPeriodicSyncPduRxCount,
       "fsLaPortChannelDLAGEventUpdatePduTxCount": fsLaPortChannelDLAGEventUpdatePduTxCount,
       "fsLaPortChannelDLAGEventUpdatePduRxCount": fsLaPortChannelDLAGEventUpdatePduRxCount,
       "fsLaPortChannelDLAGElectedAsMasterCount": fsLaPortChannelDLAGElectedAsMasterCount,
       "fsLaPortChannelDLAGElectedAsSlaveCount": fsLaPortChannelDLAGElectedAsSlaveCount,
       "fsLaPortChannelTrapTxCount": fsLaPortChannelTrapTxCount,
       "fsLaPortChannelDLAGDistributingPortList": fsLaPortChannelDLAGDistributingPortList,
       "fsLaPortChannelMCLAGStatus": fsLaPortChannelMCLAGStatus,
       "fsLaPortChannelMCLAGSystemID": fsLaPortChannelMCLAGSystemID,
       "fsLaPortChannelMCLAGSystemPriority": fsLaPortChannelMCLAGSystemPriority,
       "fsLaPortChannelMCLAGRolePlayed": fsLaPortChannelMCLAGRolePlayed,
       "fsLaPortChannelMCLAGMaxKeepAliveCount": fsLaPortChannelMCLAGMaxKeepAliveCount,
       "fsLaPortChannelMCLAGPeriodicSyncPduTxCount": fsLaPortChannelMCLAGPeriodicSyncPduTxCount,
       "fsLaPortChannelMCLAGPeriodicSyncPduRxCount": fsLaPortChannelMCLAGPeriodicSyncPduRxCount,
       "fsLaPortChannelMCLAGEventUpdatePduTxCount": fsLaPortChannelMCLAGEventUpdatePduTxCount,
       "fsLaPortChannelMCLAGEventUpdatePduRxCount": fsLaPortChannelMCLAGEventUpdatePduRxCount,
       "fsLaPort": fsLaPort,
       "fsLaPortTable": fsLaPortTable,
       "fsLaPortEntry": fsLaPortEntry,
       "fsLaPortIndex": fsLaPortIndex,
       "fsLaPortMode": fsLaPortMode,
       "fsLaPortBundleState": fsLaPortBundleState,
       "fsLaPortActorResetAdminState": fsLaPortActorResetAdminState,
       "fsLaPortAggregateWaitTime": fsLaPortAggregateWaitTime,
       "fsLaPortPartnerResetAdminState": fsLaPortPartnerResetAdminState,
       "fsLaPortActorAdminPort": fsLaPortActorAdminPort,
       "fsLaPortRestoreMtu": fsLaPortRestoreMtu,
       "fsLaPortSelectAggregator": fsLaPortSelectAggregator,
       "fsLaPortErrStateDetCount": fsLaPortErrStateDetCount,
       "fsLaPortErrStateRecCount": fsLaPortErrStateRecCount,
       "fsLaPortDefaultedStateThreshold": fsLaPortDefaultedStateThreshold,
       "fsLaPortHardwareFailureRecThreshold": fsLaPortHardwareFailureRecThreshold,
       "fsLaPortSameStateRecThreshold": fsLaPortSameStateRecThreshold,
       "fsLaTrapObjects": fsLaTrapObjects,
       "fsLaHwFailTrapObjectsTable": fsLaHwFailTrapObjectsTable,
       "fsLaHwFailTrapObjectsEntry": fsLaHwFailTrapObjectsEntry,
       "fsLaTrapPortChannelIndex": fsLaTrapPortChannelIndex,
       "fsLaTrapPortIndex": fsLaTrapPortIndex,
       "fsLaHwFailTrapType": fsLaHwFailTrapType,
       "fsLaDLAGTrapObjectsTable": fsLaDLAGTrapObjectsTable,
       "fsLaDLAGTrapObjectsEntry": fsLaDLAGTrapObjectsEntry,
       "fsLaDLAGTrapPortChannelIndex": fsLaDLAGTrapPortChannelIndex,
       "fsLaDLAGTrapType": fsLaDLAGTrapType,
       "fsFutureLaTraps": fsFutureLaTraps,
       "fsLaTraps": fsLaTraps,
       "fsLaHwFailureTrap": fsLaHwFailureTrap,
       "fsLaDLAGTrap": fsLaDLAGTrap,
       "fsLaDLAGRemotePortChannel": fsLaDLAGRemotePortChannel,
       "fsLaDLAGRemotePortChannelTable": fsLaDLAGRemotePortChannelTable,
       "fsLaDLAGRemotePortChannelEntry": fsLaDLAGRemotePortChannelEntry,
       "fsLaDLAGRemotePortChannelSystemID": fsLaDLAGRemotePortChannelSystemID,
       "fsLaDLAGRemotePortChannelSystemPriority": fsLaDLAGRemotePortChannelSystemPriority,
       "fsLaDLAGRemotePortChannelRolePlayed": fsLaDLAGRemotePortChannelRolePlayed,
       "fsLaDLAGRemotePortChannelKeepAliveCount": fsLaDLAGRemotePortChannelKeepAliveCount,
       "fsLaDLAGRemotePortChannelSpeed": fsLaDLAGRemotePortChannelSpeed,
       "fsLaDLAGRemotePortChannelHighSpeed": fsLaDLAGRemotePortChannelHighSpeed,
       "fsLaDLAGRemotePortChannelMtu": fsLaDLAGRemotePortChannelMtu,
       "fsLaDLAGRemotePort": fsLaDLAGRemotePort,
       "fsLaDLAGRemotePortTable": fsLaDLAGRemotePortTable,
       "fsLaDLAGRemotePortEntry": fsLaDLAGRemotePortEntry,
       "fsLaDLAGRemotePortIndex": fsLaDLAGRemotePortIndex,
       "fsLaDLAGRemotePortBundleState": fsLaDLAGRemotePortBundleState,
       "fsLaDLAGRemotePortSyncStatus": fsLaDLAGRemotePortSyncStatus,
       "fsLaDLAGRemotePortPriority": fsLaDLAGRemotePortPriority,
       "fsLaMCLAGRemotePortChannel": fsLaMCLAGRemotePortChannel,
       "fsLaMCLAGRemotePortChannelTable": fsLaMCLAGRemotePortChannelTable,
       "fsLaMCLAGRemotePortChannelEntry": fsLaMCLAGRemotePortChannelEntry,
       "fsLaMCLAGRemotePortChannelSystemID": fsLaMCLAGRemotePortChannelSystemID,
       "fsLaMCLAGRemotePortChannelSystemPriority": fsLaMCLAGRemotePortChannelSystemPriority,
       "fsLaMCLAGRemotePortChannelRolePlayed": fsLaMCLAGRemotePortChannelRolePlayed,
       "fsLaMCLAGRemotePortChannelKeepAliveCount": fsLaMCLAGRemotePortChannelKeepAliveCount,
       "fsLaMCLAGRemotePortChannelSpeed": fsLaMCLAGRemotePortChannelSpeed,
       "fsLaMCLAGRemotePortChannelHighSpeed": fsLaMCLAGRemotePortChannelHighSpeed,
       "fsLaMCLAGRemotePortChannelMtu": fsLaMCLAGRemotePortChannelMtu,
       "fsLaMCLAGRemotePort": fsLaMCLAGRemotePort,
       "fsLaMCLAGRemotePortTable": fsLaMCLAGRemotePortTable,
       "fsLaMCLAGRemotePortEntry": fsLaMCLAGRemotePortEntry,
       "fsLaMCLAGRemotePortIndex": fsLaMCLAGRemotePortIndex,
       "fsLaMCLAGRemotePortSlotIndex": fsLaMCLAGRemotePortSlotIndex,
       "fsLaMCLAGRemotePortBundleState": fsLaMCLAGRemotePortBundleState,
       "fsLaMCLAGRemotePortSyncStatus": fsLaMCLAGRemotePortSyncStatus,
       "fsLaMCLAGRemotePortPriority": fsLaMCLAGRemotePortPriority}
)
