# SNMP MIB module (ALU-LCR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/ALU-LCR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:54:45 2025
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

(aluSARConfs,
 aluSARMIBModules,
 aluSARNotifyPrefix,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARNotifyPrefix",
    "aluSARObjs")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(TmnxHwIndex,) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxHwIndex")

(TItemDescription,
 TNamedItem) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem")


# MODULE-IDENTITY

aluLcrMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 21)
)
if mibBuilder.loadTexts:
    aluLcrMIBModule.setRevisions(
        ("2018-09-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AluLcrConformance_ObjectIdentity = ObjectIdentity
aluLcrConformance = _AluLcrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 23)
)
_AluLcrCompliances_ObjectIdentity = ObjectIdentity
aluLcrCompliances = _AluLcrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 23, 1)
)
_AluLcrGroups_ObjectIdentity = ObjectIdentity
aluLcrGroups = _AluLcrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 23, 2)
)
_AluLcrV9v0Groups_ObjectIdentity = ObjectIdentity
aluLcrV9v0Groups = _AluLcrV9v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 23, 2, 1)
)
_AluLcrObjs_ObjectIdentity = ObjectIdentity
aluLcrObjs = _AluLcrObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23)
)
_AluLcrScalarObjs_ObjectIdentity = ObjectIdentity
aluLcrScalarObjs = _AluLcrScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 1)
)
_AluLcrScalarLastChangedObjs_ObjectIdentity = ObjectIdentity
aluLcrScalarLastChangedObjs = _AluLcrScalarLastChangedObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 1, 1)
)
_AluLcrConfigTableLastChanged_Type = TimeStamp
_AluLcrConfigTableLastChanged_Object = MibScalar
aluLcrConfigTableLastChanged = _AluLcrConfigTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 1, 1, 1),
    _AluLcrConfigTableLastChanged_Type()
)
aluLcrConfigTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLcrConfigTableLastChanged.setStatus("current")
_AluLcrMdaConfigTableLastChanged_Type = TimeStamp
_AluLcrMdaConfigTableLastChanged_Object = MibScalar
aluLcrMdaConfigTableLastChanged = _AluLcrMdaConfigTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 1, 1, 2),
    _AluLcrMdaConfigTableLastChanged_Type()
)
aluLcrMdaConfigTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLcrMdaConfigTableLastChanged.setStatus("current")
_AluLcrConfigurations_ObjectIdentity = ObjectIdentity
aluLcrConfigurations = _AluLcrConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2)
)
_AluLcrConfigTable_Object = MibTable
aluLcrConfigTable = _AluLcrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 1)
)
if mibBuilder.loadTexts:
    aluLcrConfigTable.setStatus("current")
_AluLcrConfigEntry_Object = MibTableRow
aluLcrConfigEntry = _AluLcrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 1, 1)
)
aluLcrConfigEntry.setIndexNames(
    (1, "ALU-LCR-MIB", "aluLcrConfigName"),
)
if mibBuilder.loadTexts:
    aluLcrConfigEntry.setStatus("current")
_AluLcrConfigName_Type = TNamedItem
_AluLcrConfigName_Object = MibTableColumn
aluLcrConfigName = _AluLcrConfigName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 1, 1, 1),
    _AluLcrConfigName_Type()
)
aluLcrConfigName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluLcrConfigName.setStatus("current")
_AluLcrConfigRowStatus_Type = RowStatus
_AluLcrConfigRowStatus_Object = MibTableColumn
aluLcrConfigRowStatus = _AluLcrConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 1, 1, 2),
    _AluLcrConfigRowStatus_Type()
)
aluLcrConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluLcrConfigRowStatus.setStatus("current")


class _AluLcrConfigDescription_Type(TItemDescription):
    """Custom type aluLcrConfigDescription based on TItemDescription"""
    defaultHexValue = ""


_AluLcrConfigDescription_Type.__name__ = "TItemDescription"
_AluLcrConfigDescription_Object = MibTableColumn
aluLcrConfigDescription = _AluLcrConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 1, 1, 3),
    _AluLcrConfigDescription_Type()
)
aluLcrConfigDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluLcrConfigDescription.setStatus("current")


class _AluLcrConfigRevert_Type(Integer32):
    """Custom type aluLcrConfigRevert based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRevertive", 1),
          ("revertive", 2))
    )


_AluLcrConfigRevert_Type.__name__ = "Integer32"
_AluLcrConfigRevert_Object = MibTableColumn
aluLcrConfigRevert = _AluLcrConfigRevert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 1, 1, 4),
    _AluLcrConfigRevert_Type()
)
aluLcrConfigRevert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluLcrConfigRevert.setStatus("current")


class _AluLcrConfigWaitToRestore_Type(Unsigned32):
    """Custom type aluLcrConfigWaitToRestore based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 3600),
    )


_AluLcrConfigWaitToRestore_Type.__name__ = "Unsigned32"
_AluLcrConfigWaitToRestore_Object = MibTableColumn
aluLcrConfigWaitToRestore = _AluLcrConfigWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 1, 1, 5),
    _AluLcrConfigWaitToRestore_Type()
)
aluLcrConfigWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluLcrConfigWaitToRestore.setStatus("current")
if mibBuilder.loadTexts:
    aluLcrConfigWaitToRestore.setUnits("seconds")
_AluLcrConfigMcNeighborAddrType_Type = InetAddressType
_AluLcrConfigMcNeighborAddrType_Object = MibTableColumn
aluLcrConfigMcNeighborAddrType = _AluLcrConfigMcNeighborAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 1, 1, 6),
    _AluLcrConfigMcNeighborAddrType_Type()
)
aluLcrConfigMcNeighborAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluLcrConfigMcNeighborAddrType.setStatus("current")


class _AluLcrConfigMcNeighborAddr_Type(InetAddress):
    """Custom type aluLcrConfigMcNeighborAddr based on InetAddress"""
    defaultHexValue = "00000000000000000000000000000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AluLcrConfigMcNeighborAddr_Type.__name__ = "InetAddress"
_AluLcrConfigMcNeighborAddr_Object = MibTableColumn
aluLcrConfigMcNeighborAddr = _AluLcrConfigMcNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 1, 1, 7),
    _AluLcrConfigMcNeighborAddr_Type()
)
aluLcrConfigMcNeighborAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluLcrConfigMcNeighborAddr.setStatus("current")


class _AluLcrConfigMcAdvertiseInterval_Type(Unsigned32):
    """Custom type aluLcrConfigMcAdvertiseInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 650),
    )


_AluLcrConfigMcAdvertiseInterval_Type.__name__ = "Unsigned32"
_AluLcrConfigMcAdvertiseInterval_Object = MibTableColumn
aluLcrConfigMcAdvertiseInterval = _AluLcrConfigMcAdvertiseInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 1, 1, 8),
    _AluLcrConfigMcAdvertiseInterval_Type()
)
aluLcrConfigMcAdvertiseInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluLcrConfigMcAdvertiseInterval.setStatus("current")
if mibBuilder.loadTexts:
    aluLcrConfigMcAdvertiseInterval.setUnits("100s of milliseconds")


class _AluLcrConfigMcHoldTime_Type(Unsigned32):
    """Custom type aluLcrConfigMcHoldTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 650),
    )


_AluLcrConfigMcHoldTime_Type.__name__ = "Unsigned32"
_AluLcrConfigMcHoldTime_Object = MibTableColumn
aluLcrConfigMcHoldTime = _AluLcrConfigMcHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 1, 1, 9),
    _AluLcrConfigMcHoldTime_Type()
)
aluLcrConfigMcHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluLcrConfigMcHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    aluLcrConfigMcHoldTime.setUnits("100s of milliseconds")
_AluLcrMdaConfigTable_Object = MibTable
aluLcrMdaConfigTable = _AluLcrMdaConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 2)
)
if mibBuilder.loadTexts:
    aluLcrMdaConfigTable.setStatus("current")
_AluLcrMdaConfigEntry_Object = MibTableRow
aluLcrMdaConfigEntry = _AluLcrMdaConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 2, 1)
)
aluLcrMdaConfigEntry.setIndexNames(
    (0, "ALU-LCR-MIB", "aluLcrConfigName"),
    (0, "ALU-LCR-MIB", "aluLcrMdaConfigNumber"),
)
if mibBuilder.loadTexts:
    aluLcrMdaConfigEntry.setStatus("current")


class _AluLcrMdaConfigNumber_Type(Unsigned32):
    """Custom type aluLcrMdaConfigNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AluLcrMdaConfigNumber_Type.__name__ = "Unsigned32"
_AluLcrMdaConfigNumber_Object = MibTableColumn
aluLcrMdaConfigNumber = _AluLcrMdaConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 2, 1, 1),
    _AluLcrMdaConfigNumber_Type()
)
aluLcrMdaConfigNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluLcrMdaConfigNumber.setStatus("current")
_AluLcrMdaConfigRowStatus_Type = RowStatus
_AluLcrMdaConfigRowStatus_Object = MibTableColumn
aluLcrMdaConfigRowStatus = _AluLcrMdaConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 2, 1, 2),
    _AluLcrMdaConfigRowStatus_Type()
)
aluLcrMdaConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluLcrMdaConfigRowStatus.setStatus("current")
_AluLcrMdaConfigHwIndex_Type = TmnxHwIndex
_AluLcrMdaConfigHwIndex_Object = MibTableColumn
aluLcrMdaConfigHwIndex = _AluLcrMdaConfigHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 2, 1, 3),
    _AluLcrMdaConfigHwIndex_Type()
)
aluLcrMdaConfigHwIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluLcrMdaConfigHwIndex.setStatus("current")
_AluLcrCommandTable_Object = MibTable
aluLcrCommandTable = _AluLcrCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 3)
)
if mibBuilder.loadTexts:
    aluLcrCommandTable.setStatus("current")
_AluLcrCommandEntry_Object = MibTableRow
aluLcrCommandEntry = _AluLcrCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 3, 1)
)
aluLcrCommandEntry.setIndexNames(
    (0, "ALU-LCR-MIB", "aluLcrConfigName"),
    (0, "ALU-LCR-MIB", "aluLcrMdaConfigNumber"),
)
if mibBuilder.loadTexts:
    aluLcrCommandEntry.setStatus("current")


class _AluLcrCommandSwitch_Type(Integer32):
    """Custom type aluLcrCommandSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("clear", 2),
          ("lockoutOfProtection", 3),
          ("forcedSwitchWorkToProtect", 4),
          ("forcedSwitchProtectToWork", 5))
    )


_AluLcrCommandSwitch_Type.__name__ = "Integer32"
_AluLcrCommandSwitch_Object = MibTableColumn
aluLcrCommandSwitch = _AluLcrCommandSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 2, 3, 1, 1),
    _AluLcrCommandSwitch_Type()
)
aluLcrCommandSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluLcrCommandSwitch.setStatus("current")
_AluLcrStatus_ObjectIdentity = ObjectIdentity
aluLcrStatus = _AluLcrStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 3)
)
_AluLcrStatusTable_Object = MibTable
aluLcrStatusTable = _AluLcrStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 3, 1)
)
if mibBuilder.loadTexts:
    aluLcrStatusTable.setStatus("current")
_AluLcrStatusEntry_Object = MibTableRow
aluLcrStatusEntry = _AluLcrStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 3, 1, 1)
)
if mibBuilder.loadTexts:
    aluLcrStatusEntry.setStatus("current")


class _AluLcrStatusRequest_Type(OctetString):
    """Custom type aluLcrStatusRequest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_AluLcrStatusRequest_Type.__name__ = "OctetString"
_AluLcrStatusRequest_Object = MibTableColumn
aluLcrStatusRequest = _AluLcrStatusRequest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 3, 1, 1, 1),
    _AluLcrStatusRequest_Type()
)
aluLcrStatusRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLcrStatusRequest.setStatus("current")
_AluLcrStatusSwitchedMda_Type = Integer32
_AluLcrStatusSwitchedMda_Object = MibTableColumn
aluLcrStatusSwitchedMda = _AluLcrStatusSwitchedMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 3, 1, 1, 2),
    _AluLcrStatusSwitchedMda_Type()
)
aluLcrStatusSwitchedMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLcrStatusSwitchedMda.setStatus("current")


class _AluLcrStatusMcCtlLinkState_Type(Integer32):
    """Custom type aluLcrStatusMcCtlLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("downSignalingFailure", 1),
          ("downIncompatibleNbr", 2))
    )


_AluLcrStatusMcCtlLinkState_Type.__name__ = "Integer32"
_AluLcrStatusMcCtlLinkState_Object = MibTableColumn
aluLcrStatusMcCtlLinkState = _AluLcrStatusMcCtlLinkState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 3, 1, 1, 3),
    _AluLcrStatusMcCtlLinkState_Type()
)
aluLcrStatusMcCtlLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLcrStatusMcCtlLinkState.setStatus("current")
_AluLcrMdaStatusTable_Object = MibTable
aluLcrMdaStatusTable = _AluLcrMdaStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 3, 2)
)
if mibBuilder.loadTexts:
    aluLcrMdaStatusTable.setStatus("current")
_AluLcrMdaStatusEntry_Object = MibTableRow
aluLcrMdaStatusEntry = _AluLcrMdaStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 3, 2, 1)
)
if mibBuilder.loadTexts:
    aluLcrMdaStatusEntry.setStatus("current")


class _AluLcrMdaStatusCurrent_Type(Bits):
    """Custom type aluLcrMdaStatusCurrent based on Bits"""
    namedValues = NamedValues(
        *(("lockedOut", 0),
          ("sd", 1),
          ("sf", 2),
          ("switched", 3),
          ("wtr", 4))
    )

_AluLcrMdaStatusCurrent_Type.__name__ = "Bits"
_AluLcrMdaStatusCurrent_Object = MibTableColumn
aluLcrMdaStatusCurrent = _AluLcrMdaStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 3, 2, 1, 1),
    _AluLcrMdaStatusCurrent_Type()
)
aluLcrMdaStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLcrMdaStatusCurrent.setStatus("current")
_AluLcrMdaStatusSwitchovers_Type = Counter32
_AluLcrMdaStatusSwitchovers_Object = MibTableColumn
aluLcrMdaStatusSwitchovers = _AluLcrMdaStatusSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 3, 2, 1, 2),
    _AluLcrMdaStatusSwitchovers_Type()
)
aluLcrMdaStatusSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLcrMdaStatusSwitchovers.setStatus("current")
_AluLcrMdaStatusLastSwitchover_Type = TimeStamp
_AluLcrMdaStatusLastSwitchover_Object = MibTableColumn
aluLcrMdaStatusLastSwitchover = _AluLcrMdaStatusLastSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 3, 2, 1, 3),
    _AluLcrMdaStatusLastSwitchover_Type()
)
aluLcrMdaStatusLastSwitchover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLcrMdaStatusLastSwitchover.setStatus("current")
_AluLcrMdaStatusSwitchoverSeconds_Type = Counter32
_AluLcrMdaStatusSwitchoverSeconds_Object = MibTableColumn
aluLcrMdaStatusSwitchoverSeconds = _AluLcrMdaStatusSwitchoverSeconds_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 3, 2, 1, 4),
    _AluLcrMdaStatusSwitchoverSeconds_Type()
)
aluLcrMdaStatusSwitchoverSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLcrMdaStatusSwitchoverSeconds.setStatus("current")
_AluLcrMdaStatusDiscontinuityTime_Type = TimeStamp
_AluLcrMdaStatusDiscontinuityTime_Object = MibTableColumn
aluLcrMdaStatusDiscontinuityTime = _AluLcrMdaStatusDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 23, 3, 2, 1, 5),
    _AluLcrMdaStatusDiscontinuityTime_Type()
)
aluLcrMdaStatusDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLcrMdaStatusDiscontinuityTime.setStatus("current")
_AluLcrNotifyPrefix_ObjectIdentity = ObjectIdentity
aluLcrNotifyPrefix = _AluLcrNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 19)
)
_AluLcrNotifications_ObjectIdentity = ObjectIdentity
aluLcrNotifications = _AluLcrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 19, 0)
)
aluLcrConfigEntry.registerAugmentions(
    ("ALU-LCR-MIB",
     "aluLcrStatusEntry")
)
aluLcrStatusEntry.setIndexNames(*aluLcrConfigEntry.getIndexNames())
aluLcrMdaConfigEntry.registerAugmentions(
    ("ALU-LCR-MIB",
     "aluLcrMdaStatusEntry")
)
aluLcrMdaStatusEntry.setIndexNames(*aluLcrMdaConfigEntry.getIndexNames())

# Managed Objects groups

aluLcrScalarLastChangedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 23, 2, 1, 1)
)
aluLcrScalarLastChangedGroup.setObjects(
      *(("ALU-LCR-MIB", "aluLcrConfigTableLastChanged"),
        ("ALU-LCR-MIB", "aluLcrMdaConfigTableLastChanged"))
)
if mibBuilder.loadTexts:
    aluLcrScalarLastChangedGroup.setStatus("current")

aluLcrConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 23, 2, 1, 2)
)
aluLcrConfigGroup.setObjects(
      *(("ALU-LCR-MIB", "aluLcrConfigRowStatus"),
        ("ALU-LCR-MIB", "aluLcrConfigDescription"),
        ("ALU-LCR-MIB", "aluLcrConfigRevert"),
        ("ALU-LCR-MIB", "aluLcrConfigWaitToRestore"),
        ("ALU-LCR-MIB", "aluLcrConfigMcNeighborAddrType"),
        ("ALU-LCR-MIB", "aluLcrConfigMcNeighborAddr"),
        ("ALU-LCR-MIB", "aluLcrConfigMcAdvertiseInterval"),
        ("ALU-LCR-MIB", "aluLcrConfigMcHoldTime"))
)
if mibBuilder.loadTexts:
    aluLcrConfigGroup.setStatus("current")

aluLcrMdaConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 23, 2, 1, 3)
)
aluLcrMdaConfigGroup.setObjects(
      *(("ALU-LCR-MIB", "aluLcrMdaConfigRowStatus"),
        ("ALU-LCR-MIB", "aluLcrMdaConfigHwIndex"))
)
if mibBuilder.loadTexts:
    aluLcrMdaConfigGroup.setStatus("current")

aluLcrCommandSwitchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 23, 2, 1, 4)
)
aluLcrCommandSwitchGroup.setObjects(
    ("ALU-LCR-MIB", "aluLcrCommandSwitch")
)
if mibBuilder.loadTexts:
    aluLcrCommandSwitchGroup.setStatus("current")

aluLcrStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 23, 2, 1, 5)
)
aluLcrStatusGroup.setObjects(
      *(("ALU-LCR-MIB", "aluLcrStatusRequest"),
        ("ALU-LCR-MIB", "aluLcrStatusSwitchedMda"),
        ("ALU-LCR-MIB", "aluLcrStatusMcCtlLinkState"))
)
if mibBuilder.loadTexts:
    aluLcrStatusGroup.setStatus("current")

aluLcrMdaStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 23, 2, 1, 6)
)
aluLcrMdaStatusGroup.setObjects(
      *(("ALU-LCR-MIB", "aluLcrMdaStatusCurrent"),
        ("ALU-LCR-MIB", "aluLcrMdaStatusSwitchovers"),
        ("ALU-LCR-MIB", "aluLcrMdaStatusLastSwitchover"),
        ("ALU-LCR-MIB", "aluLcrMdaStatusSwitchoverSeconds"),
        ("ALU-LCR-MIB", "aluLcrMdaStatusDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    aluLcrMdaStatusGroup.setStatus("current")


# Notification objects

aluLcrStatusMcCtlLinkStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 19, 0, 1)
)
aluLcrStatusMcCtlLinkStateChange.setObjects(
    ("ALU-LCR-MIB", "aluLcrStatusMcCtlLinkState")
)
if mibBuilder.loadTexts:
    aluLcrStatusMcCtlLinkStateChange.setStatus(
        "current"
    )

aluLcrEventSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 19, 0, 2)
)
aluLcrEventSwitchover.setObjects(
      *(("ALU-LCR-MIB", "aluLcrMdaStatusSwitchovers"),
        ("ALU-LCR-MIB", "aluLcrMdaStatusCurrent"))
)
if mibBuilder.loadTexts:
    aluLcrEventSwitchover.setStatus(
        "current"
    )

aluLcrCommandSwitchSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 19, 0, 3)
)
aluLcrCommandSwitchSet.setObjects(
    ("ALU-LCR-MIB", "aluLcrCommandSwitch")
)
if mibBuilder.loadTexts:
    aluLcrCommandSwitchSet.setStatus(
        "current"
    )

aluLcrCommandSwitchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 19, 0, 4)
)
aluLcrCommandSwitchClear.setObjects(
    ("ALU-LCR-MIB", "aluLcrCommandSwitch")
)
if mibBuilder.loadTexts:
    aluLcrCommandSwitchClear.setStatus(
        "current"
    )


# Notifications groups

aluLcrNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 23, 2, 1, 7)
)
aluLcrNotificationsGroup.setObjects(
      *(("ALU-LCR-MIB", "aluLcrStatusMcCtlLinkStateChange"),
        ("ALU-LCR-MIB", "aluLcrEventSwitchover"),
        ("ALU-LCR-MIB", "aluLcrCommandSwitchSet"),
        ("ALU-LCR-MIB", "aluLcrCommandSwitchClear"))
)
if mibBuilder.loadTexts:
    aluLcrNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aluLcrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 23, 1, 1)
)
aluLcrCompliance.setObjects(
      *(("ALU-LCR-MIB", "aluLcrScalarLastChangedGroup"),
        ("ALU-LCR-MIB", "aluLcrConfigGroup"),
        ("ALU-LCR-MIB", "aluLcrMdaConfigGroup"),
        ("ALU-LCR-MIB", "aluLcrCommandSwitchGroup"),
        ("ALU-LCR-MIB", "aluLcrStatusGroup"),
        ("ALU-LCR-MIB", "aluLcrMdaStatusGroup"),
        ("ALU-LCR-MIB", "aluLcrNotificationsGroup"))
)
if mibBuilder.loadTexts:
    aluLcrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-LCR-MIB",
    **{"aluLcrMIBModule": aluLcrMIBModule,
       "aluLcrConformance": aluLcrConformance,
       "aluLcrCompliances": aluLcrCompliances,
       "aluLcrCompliance": aluLcrCompliance,
       "aluLcrGroups": aluLcrGroups,
       "aluLcrV9v0Groups": aluLcrV9v0Groups,
       "aluLcrScalarLastChangedGroup": aluLcrScalarLastChangedGroup,
       "aluLcrConfigGroup": aluLcrConfigGroup,
       "aluLcrMdaConfigGroup": aluLcrMdaConfigGroup,
       "aluLcrCommandSwitchGroup": aluLcrCommandSwitchGroup,
       "aluLcrStatusGroup": aluLcrStatusGroup,
       "aluLcrMdaStatusGroup": aluLcrMdaStatusGroup,
       "aluLcrNotificationsGroup": aluLcrNotificationsGroup,
       "aluLcrObjs": aluLcrObjs,
       "aluLcrScalarObjs": aluLcrScalarObjs,
       "aluLcrScalarLastChangedObjs": aluLcrScalarLastChangedObjs,
       "aluLcrConfigTableLastChanged": aluLcrConfigTableLastChanged,
       "aluLcrMdaConfigTableLastChanged": aluLcrMdaConfigTableLastChanged,
       "aluLcrConfigurations": aluLcrConfigurations,
       "aluLcrConfigTable": aluLcrConfigTable,
       "aluLcrConfigEntry": aluLcrConfigEntry,
       "aluLcrConfigName": aluLcrConfigName,
       "aluLcrConfigRowStatus": aluLcrConfigRowStatus,
       "aluLcrConfigDescription": aluLcrConfigDescription,
       "aluLcrConfigRevert": aluLcrConfigRevert,
       "aluLcrConfigWaitToRestore": aluLcrConfigWaitToRestore,
       "aluLcrConfigMcNeighborAddrType": aluLcrConfigMcNeighborAddrType,
       "aluLcrConfigMcNeighborAddr": aluLcrConfigMcNeighborAddr,
       "aluLcrConfigMcAdvertiseInterval": aluLcrConfigMcAdvertiseInterval,
       "aluLcrConfigMcHoldTime": aluLcrConfigMcHoldTime,
       "aluLcrMdaConfigTable": aluLcrMdaConfigTable,
       "aluLcrMdaConfigEntry": aluLcrMdaConfigEntry,
       "aluLcrMdaConfigNumber": aluLcrMdaConfigNumber,
       "aluLcrMdaConfigRowStatus": aluLcrMdaConfigRowStatus,
       "aluLcrMdaConfigHwIndex": aluLcrMdaConfigHwIndex,
       "aluLcrCommandTable": aluLcrCommandTable,
       "aluLcrCommandEntry": aluLcrCommandEntry,
       "aluLcrCommandSwitch": aluLcrCommandSwitch,
       "aluLcrStatus": aluLcrStatus,
       "aluLcrStatusTable": aluLcrStatusTable,
       "aluLcrStatusEntry": aluLcrStatusEntry,
       "aluLcrStatusRequest": aluLcrStatusRequest,
       "aluLcrStatusSwitchedMda": aluLcrStatusSwitchedMda,
       "aluLcrStatusMcCtlLinkState": aluLcrStatusMcCtlLinkState,
       "aluLcrMdaStatusTable": aluLcrMdaStatusTable,
       "aluLcrMdaStatusEntry": aluLcrMdaStatusEntry,
       "aluLcrMdaStatusCurrent": aluLcrMdaStatusCurrent,
       "aluLcrMdaStatusSwitchovers": aluLcrMdaStatusSwitchovers,
       "aluLcrMdaStatusLastSwitchover": aluLcrMdaStatusLastSwitchover,
       "aluLcrMdaStatusSwitchoverSeconds": aluLcrMdaStatusSwitchoverSeconds,
       "aluLcrMdaStatusDiscontinuityTime": aluLcrMdaStatusDiscontinuityTime,
       "aluLcrNotifyPrefix": aluLcrNotifyPrefix,
       "aluLcrNotifications": aluLcrNotifications,
       "aluLcrStatusMcCtlLinkStateChange": aluLcrStatusMcCtlLinkStateChange,
       "aluLcrEventSwitchover": aluLcrEventSwitchover,
       "aluLcrCommandSwitchSet": aluLcrCommandSwitchSet,
       "aluLcrCommandSwitchClear": aluLcrCommandSwitchClear}
)
