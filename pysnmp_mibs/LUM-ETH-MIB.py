# SNMP MIB module (LUM-ETH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-ETH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:59 2025
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

(lumEthMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumEthMIB",
    "lumModules")

(BoardOrInterfaceAdminStatus,
 BoardOrInterfaceOperStatus,
 FaultStatus,
 MgmtNameString,
 ObjectProperty,
 PortNumber,
 SlotNumber,
 SubrackNumber) = mibBuilder.importSymbols(
    "LUM-TC",
    "BoardOrInterfaceAdminStatus",
    "BoardOrInterfaceOperStatus",
    "FaultStatus",
    "MgmtNameString",
    "ObjectProperty",
    "PortNumber",
    "SlotNumber",
    "SubrackNumber")

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

lumEthMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 19)
)
if mibBuilder.loadTexts:
    lumEthMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-01-11 00:00",
         "2002-12-06 00:00",
         "2002-11-19 00:00",
         "2002-11-13 00:00",
         "2002-06-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EthSignalFormat(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("gbE", 1),
          ("lan10GbE", 2))
    )



# MIB Managed Objects in the order of their OIDs

_LumEthConfs_ObjectIdentity = ObjectIdentity
lumEthConfs = _LumEthConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1)
)
_LumEthGroups_ObjectIdentity = ObjectIdentity
lumEthGroups = _LumEthGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1, 1)
)
_LumEthCompl_ObjectIdentity = ObjectIdentity
lumEthCompl = _LumEthCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1, 2)
)
_LumEthMIBObjects_ObjectIdentity = ObjectIdentity
lumEthMIBObjects = _LumEthMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2)
)
_EthGeneral_ObjectIdentity = ObjectIdentity
ethGeneral = _EthGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 1)
)
_EthGeneralLastChangeTime_Type = DateAndTime
_EthGeneralLastChangeTime_Object = MibScalar
ethGeneralLastChangeTime = _EthGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 1, 1),
    _EthGeneralLastChangeTime_Type()
)
ethGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGeneralLastChangeTime.setStatus("current")
_EthGeneralStateLastChangeTime_Type = DateAndTime
_EthGeneralStateLastChangeTime_Object = MibScalar
ethGeneralStateLastChangeTime = _EthGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 1, 2),
    _EthGeneralStateLastChangeTime_Type()
)
ethGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGeneralStateLastChangeTime.setStatus("current")
_EthGeneralEthIfTableSize_Type = Unsigned32
_EthGeneralEthIfTableSize_Object = MibScalar
ethGeneralEthIfTableSize = _EthGeneralEthIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 1, 3),
    _EthGeneralEthIfTableSize_Type()
)
ethGeneralEthIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGeneralEthIfTableSize.setStatus("current")
_EthIfList_ObjectIdentity = ObjectIdentity
ethIfList = _EthIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2)
)
_EthIfTable_Object = MibTable
ethIfTable = _EthIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ethIfTable.setStatus("current")
_EthIfEntry_Object = MibTableRow
ethIfEntry = _EthIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1)
)
ethIfEntry.setIndexNames(
    (0, "LUM-ETH-MIB", "ethIfIndex"),
)
if mibBuilder.loadTexts:
    ethIfEntry.setStatus("current")


class _EthIfIndex_Type(Unsigned32):
    """Custom type ethIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EthIfIndex_Type.__name__ = "Unsigned32"
_EthIfIndex_Object = MibTableColumn
ethIfIndex = _EthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 1),
    _EthIfIndex_Type()
)
ethIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIndex.setStatus("current")
_EthIfName_Type = MgmtNameString
_EthIfName_Object = MibTableColumn
ethIfName = _EthIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 2),
    _EthIfName_Type()
)
ethIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfName.setStatus("current")


class _EthIfDescr_Type(DisplayString):
    """Custom type ethIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_EthIfDescr_Type.__name__ = "DisplayString"
_EthIfDescr_Object = MibTableColumn
ethIfDescr = _EthIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 3),
    _EthIfDescr_Type()
)
ethIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfDescr.setStatus("current")
_EthIfSubrack_Type = SubrackNumber
_EthIfSubrack_Object = MibTableColumn
ethIfSubrack = _EthIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 4),
    _EthIfSubrack_Type()
)
ethIfSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfSubrack.setStatus("current")
_EthIfSlot_Type = SlotNumber
_EthIfSlot_Object = MibTableColumn
ethIfSlot = _EthIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 5),
    _EthIfSlot_Type()
)
ethIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfSlot.setStatus("current")
_EthIfTxPort_Type = PortNumber
_EthIfTxPort_Object = MibTableColumn
ethIfTxPort = _EthIfTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 6),
    _EthIfTxPort_Type()
)
ethIfTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfTxPort.setStatus("current")
_EthIfRxPort_Type = PortNumber
_EthIfRxPort_Object = MibTableColumn
ethIfRxPort = _EthIfRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 7),
    _EthIfRxPort_Type()
)
ethIfRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfRxPort.setStatus("current")


class _EthIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type ethIfInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EthIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_EthIfInvPhysIndexOrZero_Object = MibTableColumn
ethIfInvPhysIndexOrZero = _EthIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 8),
    _EthIfInvPhysIndexOrZero_Type()
)
ethIfInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfInvPhysIndexOrZero.setStatus("current")


class _EthIfFormat_Type(EthSignalFormat):
    """Custom type ethIfFormat based on EthSignalFormat"""
    defaultValue = 1


_EthIfFormat_Type.__name__ = "EthSignalFormat"
_EthIfFormat_Object = MibTableColumn
ethIfFormat = _EthIfFormat_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 9),
    _EthIfFormat_Type()
)
ethIfFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfFormat.setStatus("current")


class _EthIfHighSpeed_Type(Gauge32):
    """Custom type ethIfHighSpeed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_EthIfHighSpeed_Type.__name__ = "Gauge32"
_EthIfHighSpeed_Object = MibTableColumn
ethIfHighSpeed = _EthIfHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 10),
    _EthIfHighSpeed_Type()
)
ethIfHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfHighSpeed.setStatus("current")


class _EthIfAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type ethIfAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_EthIfAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_EthIfAdminStatus_Object = MibTableColumn
ethIfAdminStatus = _EthIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 11),
    _EthIfAdminStatus_Type()
)
ethIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfAdminStatus.setStatus("current")


class _EthIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type ethIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_EthIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_EthIfOperStatus_Object = MibTableColumn
ethIfOperStatus = _EthIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 12),
    _EthIfOperStatus_Type()
)
ethIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfOperStatus.setStatus("current")


class _EthIfLaserStatus_Type(Integer32):
    """Custom type ethIfLaserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_EthIfLaserStatus_Type.__name__ = "Integer32"
_EthIfLaserStatus_Object = MibTableColumn
ethIfLaserStatus = _EthIfLaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 13),
    _EthIfLaserStatus_Type()
)
ethIfLaserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfLaserStatus.setStatus("current")


class _EthIfTxSignalStatus_Type(Integer32):
    """Custom type ethIfTxSignalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("degraded", 2),
          ("up", 3))
    )


_EthIfTxSignalStatus_Type.__name__ = "Integer32"
_EthIfTxSignalStatus_Object = MibTableColumn
ethIfTxSignalStatus = _EthIfTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 14),
    _EthIfTxSignalStatus_Type()
)
ethIfTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfTxSignalStatus.setStatus("current")


class _EthIfAutoNegotiationMode_Type(Integer32):
    """Custom type ethIfAutoNegotiationMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_EthIfAutoNegotiationMode_Type.__name__ = "Integer32"
_EthIfAutoNegotiationMode_Object = MibTableColumn
ethIfAutoNegotiationMode = _EthIfAutoNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 15),
    _EthIfAutoNegotiationMode_Type()
)
ethIfAutoNegotiationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfAutoNegotiationMode.setStatus("current")


class _EthIfAutoNegotiationStatus_Type(Integer32):
    """Custom type ethIfAutoNegotiationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incomplete", 1),
          ("half", 2),
          ("full", 3))
    )


_EthIfAutoNegotiationStatus_Type.__name__ = "Integer32"
_EthIfAutoNegotiationStatus_Object = MibTableColumn
ethIfAutoNegotiationStatus = _EthIfAutoNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 16),
    _EthIfAutoNegotiationStatus_Type()
)
ethIfAutoNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfAutoNegotiationStatus.setStatus("current")


class _EthIfDuplexCapability_Type(Integer32):
    """Custom type ethIfDuplexCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("half", 2),
          ("full", 3))
    )


_EthIfDuplexCapability_Type.__name__ = "Integer32"
_EthIfDuplexCapability_Object = MibTableColumn
ethIfDuplexCapability = _EthIfDuplexCapability_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 17),
    _EthIfDuplexCapability_Type()
)
ethIfDuplexCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfDuplexCapability.setStatus("current")


class _EthIfFlowControlMode_Type(Integer32):
    """Custom type ethIfFlowControlMode based on Integer32"""
    defaultValue = 2

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
        *(("noPause", 1),
          ("rxPause", 2),
          ("txPause", 3),
          ("bothPause", 4))
    )


_EthIfFlowControlMode_Type.__name__ = "Integer32"
_EthIfFlowControlMode_Object = MibTableColumn
ethIfFlowControlMode = _EthIfFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 18),
    _EthIfFlowControlMode_Type()
)
ethIfFlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfFlowControlMode.setStatus("current")


class _EthIfInterPacketGap_Type(Gauge32):
    """Custom type ethIfInterPacketGap based on Gauge32"""
    defaultValue = 96

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(72, 456),
    )


_EthIfInterPacketGap_Type.__name__ = "Gauge32"
_EthIfInterPacketGap_Object = MibTableColumn
ethIfInterPacketGap = _EthIfInterPacketGap_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 19),
    _EthIfInterPacketGap_Type()
)
ethIfInterPacketGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfInterPacketGap.setStatus("current")


class _EthIfFrameSize_Type(Gauge32):
    """Custom type ethIfFrameSize based on Gauge32"""
    defaultValue = 9600

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_EthIfFrameSize_Type.__name__ = "Gauge32"
_EthIfFrameSize_Object = MibTableColumn
ethIfFrameSize = _EthIfFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 20),
    _EthIfFrameSize_Type()
)
ethIfFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfFrameSize.setStatus("current")
_EthIfPowerLevel_Type = Integer32
_EthIfPowerLevel_Object = MibTableColumn
ethIfPowerLevel = _EthIfPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 21),
    _EthIfPowerLevel_Type()
)
ethIfPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfPowerLevel.setStatus("current")


class _EthIfPowerLevelHighThreshold_Type(Integer32):
    """Custom type ethIfPowerLevelHighThreshold based on Integer32"""
    defaultValue = -50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, -10),
    )


_EthIfPowerLevelHighThreshold_Type.__name__ = "Integer32"
_EthIfPowerLevelHighThreshold_Object = MibTableColumn
ethIfPowerLevelHighThreshold = _EthIfPowerLevelHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 22),
    _EthIfPowerLevelHighThreshold_Type()
)
ethIfPowerLevelHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfPowerLevelHighThreshold.setStatus("deprecated")


class _EthIfPowerLevelLowThreshold_Type(Integer32):
    """Custom type ethIfPowerLevelLowThreshold based on Integer32"""
    defaultValue = -160

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, -10),
    )


_EthIfPowerLevelLowThreshold_Type.__name__ = "Integer32"
_EthIfPowerLevelLowThreshold_Object = MibTableColumn
ethIfPowerLevelLowThreshold = _EthIfPowerLevelLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 23),
    _EthIfPowerLevelLowThreshold_Type()
)
ethIfPowerLevelLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfPowerLevelLowThreshold.setStatus("deprecated")
_EthIfLaserBias_Type = Unsigned32
_EthIfLaserBias_Object = MibTableColumn
ethIfLaserBias = _EthIfLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 24),
    _EthIfLaserBias_Type()
)
ethIfLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfLaserBias.setStatus("current")


class _EthIfLaserBiasThreshold_Type(Unsigned32):
    """Custom type ethIfLaserBiasThreshold based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_EthIfLaserBiasThreshold_Type.__name__ = "Unsigned32"
_EthIfLaserBiasThreshold_Object = MibTableColumn
ethIfLaserBiasThreshold = _EthIfLaserBiasThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 25),
    _EthIfLaserBiasThreshold_Type()
)
ethIfLaserBiasThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfLaserBiasThreshold.setStatus("current")
_EthIfLossOfSignal_Type = FaultStatus
_EthIfLossOfSignal_Object = MibTableColumn
ethIfLossOfSignal = _EthIfLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 26),
    _EthIfLossOfSignal_Type()
)
ethIfLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfLossOfSignal.setStatus("current")
_EthIfReceivedPowerHigh_Type = FaultStatus
_EthIfReceivedPowerHigh_Object = MibTableColumn
ethIfReceivedPowerHigh = _EthIfReceivedPowerHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 27),
    _EthIfReceivedPowerHigh_Type()
)
ethIfReceivedPowerHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfReceivedPowerHigh.setStatus("current")
_EthIfReceivedPowerLow_Type = FaultStatus
_EthIfReceivedPowerLow_Object = MibTableColumn
ethIfReceivedPowerLow = _EthIfReceivedPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 28),
    _EthIfReceivedPowerLow_Type()
)
ethIfReceivedPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfReceivedPowerLow.setStatus("current")
_EthIfLaserBiasHigh_Type = FaultStatus
_EthIfLaserBiasHigh_Object = MibTableColumn
ethIfLaserBiasHigh = _EthIfLaserBiasHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 29),
    _EthIfLaserBiasHigh_Type()
)
ethIfLaserBiasHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfLaserBiasHigh.setStatus("current")
_EthIfLossOfSync_Type = FaultStatus
_EthIfLossOfSync_Object = MibTableColumn
ethIfLossOfSync = _EthIfLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 30),
    _EthIfLossOfSync_Type()
)
ethIfLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfLossOfSync.setStatus("current")
_EthIfBitrateMismatch_Type = FaultStatus
_EthIfBitrateMismatch_Object = MibTableColumn
ethIfBitrateMismatch = _EthIfBitrateMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 31),
    _EthIfBitrateMismatch_Type()
)
ethIfBitrateMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfBitrateMismatch.setStatus("current")
_EthIfLinkDown_Type = FaultStatus
_EthIfLinkDown_Object = MibTableColumn
ethIfLinkDown = _EthIfLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 32),
    _EthIfLinkDown_Type()
)
ethIfLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfLinkDown.setStatus("current")
_EthIfAuAlarmIndicationSignalW2C_Type = FaultStatus
_EthIfAuAlarmIndicationSignalW2C_Object = MibTableColumn
ethIfAuAlarmIndicationSignalW2C = _EthIfAuAlarmIndicationSignalW2C_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 33),
    _EthIfAuAlarmIndicationSignalW2C_Type()
)
ethIfAuAlarmIndicationSignalW2C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfAuAlarmIndicationSignalW2C.setStatus("current")


class _EthIfForwardAls_Type(Integer32):
    """Custom type ethIfForwardAls based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_EthIfForwardAls_Type.__name__ = "Integer32"
_EthIfForwardAls_Object = MibTableColumn
ethIfForwardAls = _EthIfForwardAls_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 34),
    _EthIfForwardAls_Type()
)
ethIfForwardAls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfForwardAls.setStatus("current")


class _EthIfSuppressRemoteAlarms_Type(Integer32):
    """Custom type ethIfSuppressRemoteAlarms based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_EthIfSuppressRemoteAlarms_Type.__name__ = "Integer32"
_EthIfSuppressRemoteAlarms_Object = MibTableColumn
ethIfSuppressRemoteAlarms = _EthIfSuppressRemoteAlarms_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 35),
    _EthIfSuppressRemoteAlarms_Type()
)
ethIfSuppressRemoteAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSuppressRemoteAlarms.setStatus("current")


class _EthIfFarEndLoopback_Type(Integer32):
    """Custom type ethIfFarEndLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_EthIfFarEndLoopback_Type.__name__ = "Integer32"
_EthIfFarEndLoopback_Object = MibTableColumn
ethIfFarEndLoopback = _EthIfFarEndLoopback_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 36),
    _EthIfFarEndLoopback_Type()
)
ethIfFarEndLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfFarEndLoopback.setStatus("current")


class _EthIfEntityId_Type(Unsigned32):
    """Custom type ethIfEntityId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EthIfEntityId_Type.__name__ = "Unsigned32"
_EthIfEntityId_Object = MibTableColumn
ethIfEntityId = _EthIfEntityId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 37),
    _EthIfEntityId_Type()
)
ethIfEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfEntityId.setStatus("current")


class _EthIfGbeUtilization_Type(Unsigned32):
    """Custom type ethIfGbeUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_EthIfGbeUtilization_Type.__name__ = "Unsigned32"
_EthIfGbeUtilization_Object = MibTableColumn
ethIfGbeUtilization = _EthIfGbeUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 38),
    _EthIfGbeUtilization_Type()
)
ethIfGbeUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfGbeUtilization.setStatus("current")
_EthIfObjectProperty_Type = ObjectProperty
_EthIfObjectProperty_Object = MibTableColumn
ethIfObjectProperty = _EthIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 39),
    _EthIfObjectProperty_Type()
)
ethIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfObjectProperty.setStatus("current")


class _EthIfPowerLevelLowRelativeThreshold_Type(Integer32):
    """Custom type ethIfPowerLevelLowRelativeThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_EthIfPowerLevelLowRelativeThreshold_Type.__name__ = "Integer32"
_EthIfPowerLevelLowRelativeThreshold_Object = MibTableColumn
ethIfPowerLevelLowRelativeThreshold = _EthIfPowerLevelLowRelativeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 2, 1, 1, 40),
    _EthIfPowerLevelLowRelativeThreshold_Type()
)
ethIfPowerLevelLowRelativeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfPowerLevelLowRelativeThreshold.setStatus("current")
_LumentisEthNotifications_ObjectIdentity = ObjectIdentity
lumentisEthNotifications = _LumentisEthNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 3)
)
_EthNotifyPrefix_ObjectIdentity = ObjectIdentity
ethNotifyPrefix = _EthNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 3, 0)
)

# Managed Objects groups

ethGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1, 1, 1)
)
ethGeneralGroup.setObjects(
      *(("LUM-ETH-MIB", "ethGeneralLastChangeTime"),
        ("LUM-ETH-MIB", "ethGeneralStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ethGeneralGroup.setStatus("deprecated")

ethIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1, 1, 2)
)
ethIfGroup.setObjects(
      *(("LUM-ETH-MIB", "ethIfIndex"),
        ("LUM-ETH-MIB", "ethIfName"),
        ("LUM-ETH-MIB", "ethIfDescr"),
        ("LUM-ETH-MIB", "ethIfSubrack"),
        ("LUM-ETH-MIB", "ethIfSlot"),
        ("LUM-ETH-MIB", "ethIfTxPort"),
        ("LUM-ETH-MIB", "ethIfRxPort"),
        ("LUM-ETH-MIB", "ethIfInvPhysIndexOrZero"),
        ("LUM-ETH-MIB", "ethIfFormat"),
        ("LUM-ETH-MIB", "ethIfHighSpeed"),
        ("LUM-ETH-MIB", "ethIfPowerLevel"),
        ("LUM-ETH-MIB", "ethIfPowerLevelHighThreshold"),
        ("LUM-ETH-MIB", "ethIfPowerLevelLowThreshold"),
        ("LUM-ETH-MIB", "ethIfLaserStatus"),
        ("LUM-ETH-MIB", "ethIfAdminStatus"),
        ("LUM-ETH-MIB", "ethIfOperStatus"),
        ("LUM-ETH-MIB", "ethIfTxSignalStatus"),
        ("LUM-ETH-MIB", "ethIfAutoNegotiationMode"),
        ("LUM-ETH-MIB", "ethIfAutoNegotiationStatus"),
        ("LUM-ETH-MIB", "ethIfLaserBias"),
        ("LUM-ETH-MIB", "ethIfLaserBiasThreshold"),
        ("LUM-ETH-MIB", "ethIfDuplexCapability"),
        ("LUM-ETH-MIB", "ethIfFlowControlMode"),
        ("LUM-ETH-MIB", "ethIfInterPacketGap"),
        ("LUM-ETH-MIB", "ethIfFrameSize"),
        ("LUM-ETH-MIB", "ethIfLossOfSignal"),
        ("LUM-ETH-MIB", "ethIfReceivedPowerHigh"),
        ("LUM-ETH-MIB", "ethIfReceivedPowerLow"),
        ("LUM-ETH-MIB", "ethIfLaserBiasHigh"),
        ("LUM-ETH-MIB", "ethIfLossOfSync"),
        ("LUM-ETH-MIB", "ethIfBitrateMismatch"),
        ("LUM-ETH-MIB", "ethIfLinkDown"))
)
if mibBuilder.loadTexts:
    ethIfGroup.setStatus("deprecated")

ethIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1, 1, 4)
)
ethIfGroupV2.setObjects(
      *(("LUM-ETH-MIB", "ethIfIndex"),
        ("LUM-ETH-MIB", "ethIfName"),
        ("LUM-ETH-MIB", "ethIfDescr"),
        ("LUM-ETH-MIB", "ethIfSubrack"),
        ("LUM-ETH-MIB", "ethIfSlot"),
        ("LUM-ETH-MIB", "ethIfTxPort"),
        ("LUM-ETH-MIB", "ethIfRxPort"),
        ("LUM-ETH-MIB", "ethIfInvPhysIndexOrZero"),
        ("LUM-ETH-MIB", "ethIfFormat"),
        ("LUM-ETH-MIB", "ethIfHighSpeed"),
        ("LUM-ETH-MIB", "ethIfLaserStatus"),
        ("LUM-ETH-MIB", "ethIfAdminStatus"),
        ("LUM-ETH-MIB", "ethIfOperStatus"),
        ("LUM-ETH-MIB", "ethIfTxSignalStatus"),
        ("LUM-ETH-MIB", "ethIfAutoNegotiationMode"),
        ("LUM-ETH-MIB", "ethIfAutoNegotiationStatus"),
        ("LUM-ETH-MIB", "ethIfLaserBias"),
        ("LUM-ETH-MIB", "ethIfLaserBiasThreshold"),
        ("LUM-ETH-MIB", "ethIfDuplexCapability"),
        ("LUM-ETH-MIB", "ethIfFlowControlMode"),
        ("LUM-ETH-MIB", "ethIfInterPacketGap"),
        ("LUM-ETH-MIB", "ethIfFrameSize"),
        ("LUM-ETH-MIB", "ethIfLossOfSignal"),
        ("LUM-ETH-MIB", "ethIfReceivedPowerHigh"),
        ("LUM-ETH-MIB", "ethIfReceivedPowerLow"),
        ("LUM-ETH-MIB", "ethIfLaserBiasHigh"),
        ("LUM-ETH-MIB", "ethIfLossOfSync"),
        ("LUM-ETH-MIB", "ethIfBitrateMismatch"),
        ("LUM-ETH-MIB", "ethIfLinkDown"))
)
if mibBuilder.loadTexts:
    ethIfGroupV2.setStatus("deprecated")

ethIfGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1, 1, 5)
)
ethIfGroupV3.setObjects(
      *(("LUM-ETH-MIB", "ethIfIndex"),
        ("LUM-ETH-MIB", "ethIfName"),
        ("LUM-ETH-MIB", "ethIfDescr"),
        ("LUM-ETH-MIB", "ethIfSubrack"),
        ("LUM-ETH-MIB", "ethIfSlot"),
        ("LUM-ETH-MIB", "ethIfTxPort"),
        ("LUM-ETH-MIB", "ethIfRxPort"),
        ("LUM-ETH-MIB", "ethIfInvPhysIndexOrZero"),
        ("LUM-ETH-MIB", "ethIfFormat"),
        ("LUM-ETH-MIB", "ethIfHighSpeed"),
        ("LUM-ETH-MIB", "ethIfLaserStatus"),
        ("LUM-ETH-MIB", "ethIfAdminStatus"),
        ("LUM-ETH-MIB", "ethIfOperStatus"),
        ("LUM-ETH-MIB", "ethIfTxSignalStatus"),
        ("LUM-ETH-MIB", "ethIfAutoNegotiationMode"),
        ("LUM-ETH-MIB", "ethIfAutoNegotiationStatus"),
        ("LUM-ETH-MIB", "ethIfLaserBias"),
        ("LUM-ETH-MIB", "ethIfLaserBiasThreshold"),
        ("LUM-ETH-MIB", "ethIfDuplexCapability"),
        ("LUM-ETH-MIB", "ethIfFlowControlMode"),
        ("LUM-ETH-MIB", "ethIfInterPacketGap"),
        ("LUM-ETH-MIB", "ethIfFrameSize"),
        ("LUM-ETH-MIB", "ethIfLossOfSignal"),
        ("LUM-ETH-MIB", "ethIfReceivedPowerHigh"),
        ("LUM-ETH-MIB", "ethIfReceivedPowerLow"),
        ("LUM-ETH-MIB", "ethIfLaserBiasHigh"),
        ("LUM-ETH-MIB", "ethIfLossOfSync"),
        ("LUM-ETH-MIB", "ethIfBitrateMismatch"),
        ("LUM-ETH-MIB", "ethIfLinkDown"),
        ("LUM-ETH-MIB", "ethIfAuAlarmIndicationSignalW2C"),
        ("LUM-ETH-MIB", "ethIfForwardAls"),
        ("LUM-ETH-MIB", "ethIfSuppressRemoteAlarms"),
        ("LUM-ETH-MIB", "ethIfFarEndLoopback"))
)
if mibBuilder.loadTexts:
    ethIfGroupV3.setStatus("deprecated")

ethIfGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1, 1, 7)
)
ethIfGroupV4.setObjects(
      *(("LUM-ETH-MIB", "ethIfIndex"),
        ("LUM-ETH-MIB", "ethIfName"),
        ("LUM-ETH-MIB", "ethIfDescr"),
        ("LUM-ETH-MIB", "ethIfSubrack"),
        ("LUM-ETH-MIB", "ethIfSlot"),
        ("LUM-ETH-MIB", "ethIfTxPort"),
        ("LUM-ETH-MIB", "ethIfRxPort"),
        ("LUM-ETH-MIB", "ethIfInvPhysIndexOrZero"),
        ("LUM-ETH-MIB", "ethIfFormat"),
        ("LUM-ETH-MIB", "ethIfHighSpeed"),
        ("LUM-ETH-MIB", "ethIfLaserStatus"),
        ("LUM-ETH-MIB", "ethIfAdminStatus"),
        ("LUM-ETH-MIB", "ethIfOperStatus"),
        ("LUM-ETH-MIB", "ethIfTxSignalStatus"),
        ("LUM-ETH-MIB", "ethIfAutoNegotiationMode"),
        ("LUM-ETH-MIB", "ethIfAutoNegotiationStatus"),
        ("LUM-ETH-MIB", "ethIfLaserBias"),
        ("LUM-ETH-MIB", "ethIfLaserBiasThreshold"),
        ("LUM-ETH-MIB", "ethIfDuplexCapability"),
        ("LUM-ETH-MIB", "ethIfFlowControlMode"),
        ("LUM-ETH-MIB", "ethIfInterPacketGap"),
        ("LUM-ETH-MIB", "ethIfFrameSize"),
        ("LUM-ETH-MIB", "ethIfLossOfSignal"),
        ("LUM-ETH-MIB", "ethIfReceivedPowerHigh"),
        ("LUM-ETH-MIB", "ethIfReceivedPowerLow"),
        ("LUM-ETH-MIB", "ethIfLaserBiasHigh"),
        ("LUM-ETH-MIB", "ethIfLossOfSync"),
        ("LUM-ETH-MIB", "ethIfBitrateMismatch"),
        ("LUM-ETH-MIB", "ethIfLinkDown"),
        ("LUM-ETH-MIB", "ethIfAuAlarmIndicationSignalW2C"),
        ("LUM-ETH-MIB", "ethIfForwardAls"),
        ("LUM-ETH-MIB", "ethIfSuppressRemoteAlarms"),
        ("LUM-ETH-MIB", "ethIfFarEndLoopback"),
        ("LUM-ETH-MIB", "ethIfGbeUtilization"))
)
if mibBuilder.loadTexts:
    ethIfGroupV4.setStatus("deprecated")

ethGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1, 1, 8)
)
ethGeneralGroupV2.setObjects(
      *(("LUM-ETH-MIB", "ethGeneralLastChangeTime"),
        ("LUM-ETH-MIB", "ethGeneralStateLastChangeTime"),
        ("LUM-ETH-MIB", "ethGeneralEthIfTableSize"))
)
if mibBuilder.loadTexts:
    ethGeneralGroupV2.setStatus("current")

ethIfGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1, 1, 9)
)
ethIfGroupV5.setObjects(
      *(("LUM-ETH-MIB", "ethIfIndex"),
        ("LUM-ETH-MIB", "ethIfName"),
        ("LUM-ETH-MIB", "ethIfDescr"),
        ("LUM-ETH-MIB", "ethIfSubrack"),
        ("LUM-ETH-MIB", "ethIfSlot"),
        ("LUM-ETH-MIB", "ethIfTxPort"),
        ("LUM-ETH-MIB", "ethIfRxPort"),
        ("LUM-ETH-MIB", "ethIfInvPhysIndexOrZero"),
        ("LUM-ETH-MIB", "ethIfFormat"),
        ("LUM-ETH-MIB", "ethIfHighSpeed"),
        ("LUM-ETH-MIB", "ethIfLaserStatus"),
        ("LUM-ETH-MIB", "ethIfAdminStatus"),
        ("LUM-ETH-MIB", "ethIfOperStatus"),
        ("LUM-ETH-MIB", "ethIfTxSignalStatus"),
        ("LUM-ETH-MIB", "ethIfAutoNegotiationMode"),
        ("LUM-ETH-MIB", "ethIfAutoNegotiationStatus"),
        ("LUM-ETH-MIB", "ethIfLaserBias"),
        ("LUM-ETH-MIB", "ethIfLaserBiasThreshold"),
        ("LUM-ETH-MIB", "ethIfDuplexCapability"),
        ("LUM-ETH-MIB", "ethIfFlowControlMode"),
        ("LUM-ETH-MIB", "ethIfInterPacketGap"),
        ("LUM-ETH-MIB", "ethIfFrameSize"),
        ("LUM-ETH-MIB", "ethIfLossOfSignal"),
        ("LUM-ETH-MIB", "ethIfReceivedPowerHigh"),
        ("LUM-ETH-MIB", "ethIfReceivedPowerLow"),
        ("LUM-ETH-MIB", "ethIfLaserBiasHigh"),
        ("LUM-ETH-MIB", "ethIfLossOfSync"),
        ("LUM-ETH-MIB", "ethIfBitrateMismatch"),
        ("LUM-ETH-MIB", "ethIfLinkDown"),
        ("LUM-ETH-MIB", "ethIfAuAlarmIndicationSignalW2C"),
        ("LUM-ETH-MIB", "ethIfForwardAls"),
        ("LUM-ETH-MIB", "ethIfSuppressRemoteAlarms"),
        ("LUM-ETH-MIB", "ethIfFarEndLoopback"),
        ("LUM-ETH-MIB", "ethIfGbeUtilization"),
        ("LUM-ETH-MIB", "ethIfPowerLevel"))
)
if mibBuilder.loadTexts:
    ethIfGroupV5.setStatus("deprecated")

ethIfGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1, 1, 10)
)
ethIfGroupV6.setObjects(
      *(("LUM-ETH-MIB", "ethIfIndex"),
        ("LUM-ETH-MIB", "ethIfName"),
        ("LUM-ETH-MIB", "ethIfDescr"),
        ("LUM-ETH-MIB", "ethIfSubrack"),
        ("LUM-ETH-MIB", "ethIfSlot"),
        ("LUM-ETH-MIB", "ethIfTxPort"),
        ("LUM-ETH-MIB", "ethIfRxPort"),
        ("LUM-ETH-MIB", "ethIfInvPhysIndexOrZero"),
        ("LUM-ETH-MIB", "ethIfFormat"),
        ("LUM-ETH-MIB", "ethIfHighSpeed"),
        ("LUM-ETH-MIB", "ethIfLaserStatus"),
        ("LUM-ETH-MIB", "ethIfAdminStatus"),
        ("LUM-ETH-MIB", "ethIfOperStatus"),
        ("LUM-ETH-MIB", "ethIfTxSignalStatus"),
        ("LUM-ETH-MIB", "ethIfAutoNegotiationMode"),
        ("LUM-ETH-MIB", "ethIfAutoNegotiationStatus"),
        ("LUM-ETH-MIB", "ethIfLaserBias"),
        ("LUM-ETH-MIB", "ethIfLaserBiasThreshold"),
        ("LUM-ETH-MIB", "ethIfDuplexCapability"),
        ("LUM-ETH-MIB", "ethIfFlowControlMode"),
        ("LUM-ETH-MIB", "ethIfInterPacketGap"),
        ("LUM-ETH-MIB", "ethIfFrameSize"),
        ("LUM-ETH-MIB", "ethIfLossOfSignal"),
        ("LUM-ETH-MIB", "ethIfReceivedPowerHigh"),
        ("LUM-ETH-MIB", "ethIfReceivedPowerLow"),
        ("LUM-ETH-MIB", "ethIfLaserBiasHigh"),
        ("LUM-ETH-MIB", "ethIfLossOfSync"),
        ("LUM-ETH-MIB", "ethIfBitrateMismatch"),
        ("LUM-ETH-MIB", "ethIfLinkDown"),
        ("LUM-ETH-MIB", "ethIfAuAlarmIndicationSignalW2C"),
        ("LUM-ETH-MIB", "ethIfForwardAls"),
        ("LUM-ETH-MIB", "ethIfSuppressRemoteAlarms"),
        ("LUM-ETH-MIB", "ethIfFarEndLoopback"),
        ("LUM-ETH-MIB", "ethIfEntityId"),
        ("LUM-ETH-MIB", "ethIfGbeUtilization"),
        ("LUM-ETH-MIB", "ethIfPowerLevel"),
        ("LUM-ETH-MIB", "ethIfObjectProperty"),
        ("LUM-ETH-MIB", "ethIfPowerLevelLowRelativeThreshold"))
)
if mibBuilder.loadTexts:
    ethIfGroupV6.setStatus("current")


# Notification objects

ethIfTxSignalStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 3, 0, 1)
)
ethIfTxSignalStatusDown.setObjects(
      *(("LUM-ETH-MIB", "ethIfIndex"),
        ("LUM-ETH-MIB", "ethIfName"),
        ("LUM-ETH-MIB", "ethIfSubrack"),
        ("LUM-ETH-MIB", "ethIfSlot"),
        ("LUM-ETH-MIB", "ethIfTxPort"),
        ("LUM-ETH-MIB", "ethIfRxPort"),
        ("LUM-ETH-MIB", "ethIfEntityId"),
        ("LUM-ETH-MIB", "ethIfTxSignalStatus"))
)
if mibBuilder.loadTexts:
    ethIfTxSignalStatusDown.setStatus(
        "current"
    )

ethIfTxSignalStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 3, 0, 2)
)
ethIfTxSignalStatusUp.setObjects(
      *(("LUM-ETH-MIB", "ethIfIndex"),
        ("LUM-ETH-MIB", "ethIfName"),
        ("LUM-ETH-MIB", "ethIfSubrack"),
        ("LUM-ETH-MIB", "ethIfSlot"),
        ("LUM-ETH-MIB", "ethIfTxPort"),
        ("LUM-ETH-MIB", "ethIfRxPort"),
        ("LUM-ETH-MIB", "ethIfEntityId"),
        ("LUM-ETH-MIB", "ethIfTxSignalStatus"))
)
if mibBuilder.loadTexts:
    ethIfTxSignalStatusUp.setStatus(
        "current"
    )

ethIfTxSignalStatusDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 2, 3, 0, 3)
)
ethIfTxSignalStatusDegraded.setObjects(
      *(("LUM-ETH-MIB", "ethIfIndex"),
        ("LUM-ETH-MIB", "ethIfName"),
        ("LUM-ETH-MIB", "ethIfSubrack"),
        ("LUM-ETH-MIB", "ethIfSlot"),
        ("LUM-ETH-MIB", "ethIfTxPort"),
        ("LUM-ETH-MIB", "ethIfRxPort"),
        ("LUM-ETH-MIB", "ethIfEntityId"),
        ("LUM-ETH-MIB", "ethIfTxSignalStatus"))
)
if mibBuilder.loadTexts:
    ethIfTxSignalStatusDegraded.setStatus(
        "current"
    )


# Notifications groups

ethNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1, 1, 3)
)
ethNotificationGroup.setObjects(
      *(("LUM-ETH-MIB", "ethIfTxSignalStatusDown"),
        ("LUM-ETH-MIB", "ethIfTxSignalStatusUp"))
)
if mibBuilder.loadTexts:
    ethNotificationGroup.setStatus(
        "deprecated"
    )

ethNotificationGroupV2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1, 1, 6)
)
ethNotificationGroupV2.setObjects(
      *(("LUM-ETH-MIB", "ethIfTxSignalStatusDown"),
        ("LUM-ETH-MIB", "ethIfTxSignalStatusUp"),
        ("LUM-ETH-MIB", "ethIfTxSignalStatusDegraded"))
)
if mibBuilder.loadTexts:
    ethNotificationGroupV2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lumEthBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1, 2, 1)
)
lumEthBasicComplV1.setObjects(
      *(("LUM-ETH-MIB", "ethGeneralGroup"),
        ("LUM-ETH-MIB", "ethIfGroup"),
        ("LUM-ETH-MIB", "ethNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumEthBasicComplV1.setStatus(
        "deprecated"
    )

lumEthBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1, 2, 2)
)
lumEthBasicComplV2.setObjects(
      *(("LUM-ETH-MIB", "ethGeneralGroup"),
        ("LUM-ETH-MIB", "ethIfGroupV2"),
        ("LUM-ETH-MIB", "ethNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumEthBasicComplV2.setStatus(
        "deprecated"
    )

lumEthBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1, 2, 3)
)
lumEthBasicComplV3.setObjects(
      *(("LUM-ETH-MIB", "ethGeneralGroup"),
        ("LUM-ETH-MIB", "ethIfGroupV3"),
        ("LUM-ETH-MIB", "ethNotificationGroupV2"))
)
if mibBuilder.loadTexts:
    lumEthBasicComplV3.setStatus(
        "deprecated"
    )

lumEthBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1, 2, 4)
)
lumEthBasicComplV4.setObjects(
      *(("LUM-ETH-MIB", "ethGeneralGroup"),
        ("LUM-ETH-MIB", "ethIfGroupV4"),
        ("LUM-ETH-MIB", "ethNotificationGroupV2"))
)
if mibBuilder.loadTexts:
    lumEthBasicComplV4.setStatus(
        "deprecated"
    )

lumEthBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1, 2, 5)
)
lumEthBasicComplV5.setObjects(
      *(("LUM-ETH-MIB", "ethGeneralGroupV2"),
        ("LUM-ETH-MIB", "ethIfGroupV5"),
        ("LUM-ETH-MIB", "ethNotificationGroupV2"))
)
if mibBuilder.loadTexts:
    lumEthBasicComplV5.setStatus(
        "deprecated"
    )

lumEthBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18, 1, 2, 6)
)
lumEthBasicComplV6.setObjects(
      *(("LUM-ETH-MIB", "ethGeneralGroupV2"),
        ("LUM-ETH-MIB", "ethIfGroupV6"),
        ("LUM-ETH-MIB", "ethNotificationGroupV2"))
)
if mibBuilder.loadTexts:
    lumEthBasicComplV6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-ETH-MIB",
    **{"EthSignalFormat": EthSignalFormat,
       "lumEthMIBModule": lumEthMIBModule,
       "lumEthConfs": lumEthConfs,
       "lumEthGroups": lumEthGroups,
       "ethGeneralGroup": ethGeneralGroup,
       "ethIfGroup": ethIfGroup,
       "ethNotificationGroup": ethNotificationGroup,
       "ethIfGroupV2": ethIfGroupV2,
       "ethIfGroupV3": ethIfGroupV3,
       "ethNotificationGroupV2": ethNotificationGroupV2,
       "ethIfGroupV4": ethIfGroupV4,
       "ethGeneralGroupV2": ethGeneralGroupV2,
       "ethIfGroupV5": ethIfGroupV5,
       "ethIfGroupV6": ethIfGroupV6,
       "lumEthCompl": lumEthCompl,
       "lumEthBasicComplV1": lumEthBasicComplV1,
       "lumEthBasicComplV2": lumEthBasicComplV2,
       "lumEthBasicComplV3": lumEthBasicComplV3,
       "lumEthBasicComplV4": lumEthBasicComplV4,
       "lumEthBasicComplV5": lumEthBasicComplV5,
       "lumEthBasicComplV6": lumEthBasicComplV6,
       "lumEthMIBObjects": lumEthMIBObjects,
       "ethGeneral": ethGeneral,
       "ethGeneralLastChangeTime": ethGeneralLastChangeTime,
       "ethGeneralStateLastChangeTime": ethGeneralStateLastChangeTime,
       "ethGeneralEthIfTableSize": ethGeneralEthIfTableSize,
       "ethIfList": ethIfList,
       "ethIfTable": ethIfTable,
       "ethIfEntry": ethIfEntry,
       "ethIfIndex": ethIfIndex,
       "ethIfName": ethIfName,
       "ethIfDescr": ethIfDescr,
       "ethIfSubrack": ethIfSubrack,
       "ethIfSlot": ethIfSlot,
       "ethIfTxPort": ethIfTxPort,
       "ethIfRxPort": ethIfRxPort,
       "ethIfInvPhysIndexOrZero": ethIfInvPhysIndexOrZero,
       "ethIfFormat": ethIfFormat,
       "ethIfHighSpeed": ethIfHighSpeed,
       "ethIfAdminStatus": ethIfAdminStatus,
       "ethIfOperStatus": ethIfOperStatus,
       "ethIfLaserStatus": ethIfLaserStatus,
       "ethIfTxSignalStatus": ethIfTxSignalStatus,
       "ethIfAutoNegotiationMode": ethIfAutoNegotiationMode,
       "ethIfAutoNegotiationStatus": ethIfAutoNegotiationStatus,
       "ethIfDuplexCapability": ethIfDuplexCapability,
       "ethIfFlowControlMode": ethIfFlowControlMode,
       "ethIfInterPacketGap": ethIfInterPacketGap,
       "ethIfFrameSize": ethIfFrameSize,
       "ethIfPowerLevel": ethIfPowerLevel,
       "ethIfPowerLevelHighThreshold": ethIfPowerLevelHighThreshold,
       "ethIfPowerLevelLowThreshold": ethIfPowerLevelLowThreshold,
       "ethIfLaserBias": ethIfLaserBias,
       "ethIfLaserBiasThreshold": ethIfLaserBiasThreshold,
       "ethIfLossOfSignal": ethIfLossOfSignal,
       "ethIfReceivedPowerHigh": ethIfReceivedPowerHigh,
       "ethIfReceivedPowerLow": ethIfReceivedPowerLow,
       "ethIfLaserBiasHigh": ethIfLaserBiasHigh,
       "ethIfLossOfSync": ethIfLossOfSync,
       "ethIfBitrateMismatch": ethIfBitrateMismatch,
       "ethIfLinkDown": ethIfLinkDown,
       "ethIfAuAlarmIndicationSignalW2C": ethIfAuAlarmIndicationSignalW2C,
       "ethIfForwardAls": ethIfForwardAls,
       "ethIfSuppressRemoteAlarms": ethIfSuppressRemoteAlarms,
       "ethIfFarEndLoopback": ethIfFarEndLoopback,
       "ethIfEntityId": ethIfEntityId,
       "ethIfGbeUtilization": ethIfGbeUtilization,
       "ethIfObjectProperty": ethIfObjectProperty,
       "ethIfPowerLevelLowRelativeThreshold": ethIfPowerLevelLowRelativeThreshold,
       "lumentisEthNotifications": lumentisEthNotifications,
       "ethNotifyPrefix": ethNotifyPrefix,
       "ethIfTxSignalStatusDown": ethIfTxSignalStatusDown,
       "ethIfTxSignalStatusUp": ethIfTxSignalStatusUp,
       "ethIfTxSignalStatusDegraded": ethIfTxSignalStatusDegraded}
)
