# SNMP MIB module (LUM-MUX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-MUX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:31 2025
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

(lumModules,
 lumMuxMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumMuxMIB")

(BoardOrInterfaceAdminStatus,
 BoardOrInterfaceOperStatus,
 FaultStatus,
 LambdaFrequency,
 MgmtNameString,
 ObjectProperty,
 PortNumber,
 SlotNumber,
 SubrackNumber) = mibBuilder.importSymbols(
    "LUM-TC",
    "BoardOrInterfaceAdminStatus",
    "BoardOrInterfaceOperStatus",
    "FaultStatus",
    "LambdaFrequency",
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

lumMuxMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 14)
)
if mibBuilder.loadTexts:
    lumMuxMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-01-11 00:00",
         "2011-04-12 00:00",
         "2007-11-12 00:00",
         "2003-01-29 00:00",
         "2002-12-04 00:00",
         "2002-10-29 00:00",
         "2002-10-01 00:00",
         "2002-04-03 00:00",
         "2002-01-17 00:00",
         "2001-12-03 00:00",
         "2001-11-09 00:00",
         "2001-10-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MuxTxDirection(TextualConvention, Integer32):
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
          ("toWest", 1),
          ("toEast", 2))
    )



# MIB Managed Objects in the order of their OIDs

_LumMuxConfs_ObjectIdentity = ObjectIdentity
lumMuxConfs = _LumMuxConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1)
)
_LumMuxGroups_ObjectIdentity = ObjectIdentity
lumMuxGroups = _LumMuxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1)
)
_LumMuxCompl_ObjectIdentity = ObjectIdentity
lumMuxCompl = _LumMuxCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2)
)
_LumMuxMIBObjects_ObjectIdentity = ObjectIdentity
lumMuxMIBObjects = _LumMuxMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2)
)
_MuxGeneral_ObjectIdentity = ObjectIdentity
muxGeneral = _MuxGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 1)
)
_MuxGeneralLastChangeTime_Type = DateAndTime
_MuxGeneralLastChangeTime_Object = MibScalar
muxGeneralLastChangeTime = _MuxGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 1, 1),
    _MuxGeneralLastChangeTime_Type()
)
muxGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxGeneralLastChangeTime.setStatus("current")
_MuxGeneralStateLastChangeTime_Type = DateAndTime
_MuxGeneralStateLastChangeTime_Object = MibScalar
muxGeneralStateLastChangeTime = _MuxGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 1, 2),
    _MuxGeneralStateLastChangeTime_Type()
)
muxGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxGeneralStateLastChangeTime.setStatus("current")
_MuxGeneralMuxIfTableSize_Type = Unsigned32
_MuxGeneralMuxIfTableSize_Object = MibScalar
muxGeneralMuxIfTableSize = _MuxGeneralMuxIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 1, 3),
    _MuxGeneralMuxIfTableSize_Type()
)
muxGeneralMuxIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxGeneralMuxIfTableSize.setStatus("current")
_MuxGeneralMuxVc4TableSize_Type = Unsigned32
_MuxGeneralMuxVc4TableSize_Object = MibScalar
muxGeneralMuxVc4TableSize = _MuxGeneralMuxVc4TableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 1, 4),
    _MuxGeneralMuxVc4TableSize_Type()
)
muxGeneralMuxVc4TableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxGeneralMuxVc4TableSize.setStatus("current")
_MuxIfList_ObjectIdentity = ObjectIdentity
muxIfList = _MuxIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2)
)
_MuxIfTable_Object = MibTable
muxIfTable = _MuxIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1)
)
if mibBuilder.loadTexts:
    muxIfTable.setStatus("current")
_MuxIfEntry_Object = MibTableRow
muxIfEntry = _MuxIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1)
)
muxIfEntry.setIndexNames(
    (0, "LUM-MUX-MIB", "muxIfIndex"),
)
if mibBuilder.loadTexts:
    muxIfEntry.setStatus("current")


class _MuxIfIndex_Type(Unsigned32):
    """Custom type muxIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MuxIfIndex_Type.__name__ = "Unsigned32"
_MuxIfIndex_Object = MibTableColumn
muxIfIndex = _MuxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 1),
    _MuxIfIndex_Type()
)
muxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfIndex.setStatus("current")
_MuxIfName_Type = MgmtNameString
_MuxIfName_Object = MibTableColumn
muxIfName = _MuxIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 2),
    _MuxIfName_Type()
)
muxIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfName.setStatus("current")


class _MuxIfDescr_Type(DisplayString):
    """Custom type muxIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_MuxIfDescr_Type.__name__ = "DisplayString"
_MuxIfDescr_Object = MibTableColumn
muxIfDescr = _MuxIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 3),
    _MuxIfDescr_Type()
)
muxIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxIfDescr.setStatus("current")
_MuxIfSubrack_Type = SubrackNumber
_MuxIfSubrack_Object = MibTableColumn
muxIfSubrack = _MuxIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 4),
    _MuxIfSubrack_Type()
)
muxIfSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfSubrack.setStatus("current")
_MuxIfSlot_Type = SlotNumber
_MuxIfSlot_Object = MibTableColumn
muxIfSlot = _MuxIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 5),
    _MuxIfSlot_Type()
)
muxIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfSlot.setStatus("current")
_MuxIfTxPort_Type = PortNumber
_MuxIfTxPort_Object = MibTableColumn
muxIfTxPort = _MuxIfTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 6),
    _MuxIfTxPort_Type()
)
muxIfTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfTxPort.setStatus("current")
_MuxIfRxPort_Type = PortNumber
_MuxIfRxPort_Object = MibTableColumn
muxIfRxPort = _MuxIfRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 7),
    _MuxIfRxPort_Type()
)
muxIfRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfRxPort.setStatus("current")


class _MuxIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type muxIfInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MuxIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_MuxIfInvPhysIndexOrZero_Object = MibTableColumn
muxIfInvPhysIndexOrZero = _MuxIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 8),
    _MuxIfInvPhysIndexOrZero_Type()
)
muxIfInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfInvPhysIndexOrZero.setStatus("current")
_MuxIfPowerLevel_Type = Integer32
_MuxIfPowerLevel_Object = MibTableColumn
muxIfPowerLevel = _MuxIfPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 9),
    _MuxIfPowerLevel_Type()
)
muxIfPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfPowerLevel.setStatus("current")


class _MuxIfPowerLevelHighThreshold_Type(Integer32):
    """Custom type muxIfPowerLevelHighThreshold based on Integer32"""
    defaultValue = -50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, -10),
    )


_MuxIfPowerLevelHighThreshold_Type.__name__ = "Integer32"
_MuxIfPowerLevelHighThreshold_Object = MibTableColumn
muxIfPowerLevelHighThreshold = _MuxIfPowerLevelHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 10),
    _MuxIfPowerLevelHighThreshold_Type()
)
muxIfPowerLevelHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxIfPowerLevelHighThreshold.setStatus("current")


class _MuxIfPowerLevelLowThreshold_Type(Integer32):
    """Custom type muxIfPowerLevelLowThreshold based on Integer32"""
    defaultValue = -160

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, -10),
    )


_MuxIfPowerLevelLowThreshold_Type.__name__ = "Integer32"
_MuxIfPowerLevelLowThreshold_Object = MibTableColumn
muxIfPowerLevelLowThreshold = _MuxIfPowerLevelLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 11),
    _MuxIfPowerLevelLowThreshold_Type()
)
muxIfPowerLevelLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxIfPowerLevelLowThreshold.setStatus("current")


class _MuxIfAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type muxIfAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_MuxIfAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_MuxIfAdminStatus_Object = MibTableColumn
muxIfAdminStatus = _MuxIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 12),
    _MuxIfAdminStatus_Type()
)
muxIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxIfAdminStatus.setStatus("current")


class _MuxIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type muxIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_MuxIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_MuxIfOperStatus_Object = MibTableColumn
muxIfOperStatus = _MuxIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 13),
    _MuxIfOperStatus_Type()
)
muxIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfOperStatus.setStatus("current")
_MuxIfLossOfSignal_Type = FaultStatus
_MuxIfLossOfSignal_Object = MibTableColumn
muxIfLossOfSignal = _MuxIfLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 14),
    _MuxIfLossOfSignal_Type()
)
muxIfLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfLossOfSignal.setStatus("current")
_MuxIfReceivedPowerHigh_Type = FaultStatus
_MuxIfReceivedPowerHigh_Object = MibTableColumn
muxIfReceivedPowerHigh = _MuxIfReceivedPowerHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 15),
    _MuxIfReceivedPowerHigh_Type()
)
muxIfReceivedPowerHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfReceivedPowerHigh.setStatus("current")
_MuxIfReceivedPowerLow_Type = FaultStatus
_MuxIfReceivedPowerLow_Object = MibTableColumn
muxIfReceivedPowerLow = _MuxIfReceivedPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 16),
    _MuxIfReceivedPowerLow_Type()
)
muxIfReceivedPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfReceivedPowerLow.setStatus("current")
_MuxIfBitrateMismatch_Type = FaultStatus
_MuxIfBitrateMismatch_Object = MibTableColumn
muxIfBitrateMismatch = _MuxIfBitrateMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 17),
    _MuxIfBitrateMismatch_Type()
)
muxIfBitrateMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfBitrateMismatch.setStatus("current")
_MuxIfLaserBias_Type = Unsigned32
_MuxIfLaserBias_Object = MibTableColumn
muxIfLaserBias = _MuxIfLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 18),
    _MuxIfLaserBias_Type()
)
muxIfLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfLaserBias.setStatus("current")


class _MuxIfLaserBiasThreshold_Type(Unsigned32):
    """Custom type muxIfLaserBiasThreshold based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_MuxIfLaserBiasThreshold_Type.__name__ = "Unsigned32"
_MuxIfLaserBiasThreshold_Object = MibTableColumn
muxIfLaserBiasThreshold = _MuxIfLaserBiasThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 19),
    _MuxIfLaserBiasThreshold_Type()
)
muxIfLaserBiasThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxIfLaserBiasThreshold.setStatus("current")


class _MuxIfJ0PathTrace_Type(OctetString):
    """Custom type muxIfJ0PathTrace based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
        ValueSizeConstraint(16, 16),
    )


_MuxIfJ0PathTrace_Type.__name__ = "OctetString"
_MuxIfJ0PathTrace_Object = MibTableColumn
muxIfJ0PathTrace = _MuxIfJ0PathTrace_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 20),
    _MuxIfJ0PathTrace_Type()
)
muxIfJ0PathTrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfJ0PathTrace.setStatus("deprecated")
_MuxIfAlarmIndicationSignal_Type = FaultStatus
_MuxIfAlarmIndicationSignal_Object = MibTableColumn
muxIfAlarmIndicationSignal = _MuxIfAlarmIndicationSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 21),
    _MuxIfAlarmIndicationSignal_Type()
)
muxIfAlarmIndicationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfAlarmIndicationSignal.setStatus("current")
_MuxIfLossOfFrame_Type = FaultStatus
_MuxIfLossOfFrame_Object = MibTableColumn
muxIfLossOfFrame = _MuxIfLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 22),
    _MuxIfLossOfFrame_Type()
)
muxIfLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfLossOfFrame.setStatus("current")


class _MuxIfLaserStatus_Type(Integer32):
    """Custom type muxIfLaserStatus based on Integer32"""
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


_MuxIfLaserStatus_Type.__name__ = "Integer32"
_MuxIfLaserStatus_Object = MibTableColumn
muxIfLaserStatus = _MuxIfLaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 23),
    _MuxIfLaserStatus_Type()
)
muxIfLaserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfLaserStatus.setStatus("current")
_MuxIfTxDirection_Type = MuxTxDirection
_MuxIfTxDirection_Object = MibTableColumn
muxIfTxDirection = _MuxIfTxDirection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 24),
    _MuxIfTxDirection_Type()
)
muxIfTxDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxIfTxDirection.setStatus("current")


class _MuxIfExpectedTxLambda_Type(LambdaFrequency):
    """Custom type muxIfExpectedTxLambda based on LambdaFrequency"""
    defaultValue = 0


_MuxIfExpectedTxLambda_Type.__name__ = "LambdaFrequency"
_MuxIfExpectedTxLambda_Object = MibTableColumn
muxIfExpectedTxLambda = _MuxIfExpectedTxLambda_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 25),
    _MuxIfExpectedTxLambda_Type()
)
muxIfExpectedTxLambda.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxIfExpectedTxLambda.setStatus("current")
_MuxIfTxLambda_Type = LambdaFrequency
_MuxIfTxLambda_Object = MibTableColumn
muxIfTxLambda = _MuxIfTxLambda_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 26),
    _MuxIfTxLambda_Type()
)
muxIfTxLambda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfTxLambda.setStatus("current")


class _MuxIfTraceIntrusionMode_Type(Integer32):
    """Custom type muxIfTraceIntrusionMode based on Integer32"""
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


_MuxIfTraceIntrusionMode_Type.__name__ = "Integer32"
_MuxIfTraceIntrusionMode_Object = MibTableColumn
muxIfTraceIntrusionMode = _MuxIfTraceIntrusionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 27),
    _MuxIfTraceIntrusionMode_Type()
)
muxIfTraceIntrusionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfTraceIntrusionMode.setStatus("current")


class _MuxIfTraceTransmitted_Type(DisplayString):
    """Custom type muxIfTraceTransmitted based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MuxIfTraceTransmitted_Type.__name__ = "DisplayString"
_MuxIfTraceTransmitted_Object = MibTableColumn
muxIfTraceTransmitted = _MuxIfTraceTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 28),
    _MuxIfTraceTransmitted_Type()
)
muxIfTraceTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxIfTraceTransmitted.setStatus("current")


class _MuxIfTraceReceived_Type(DisplayString):
    """Custom type muxIfTraceReceived based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MuxIfTraceReceived_Type.__name__ = "DisplayString"
_MuxIfTraceReceived_Object = MibTableColumn
muxIfTraceReceived = _MuxIfTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 29),
    _MuxIfTraceReceived_Type()
)
muxIfTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfTraceReceived.setStatus("current")


class _MuxIfTraceExpected_Type(DisplayString):
    """Custom type muxIfTraceExpected based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MuxIfTraceExpected_Type.__name__ = "DisplayString"
_MuxIfTraceExpected_Object = MibTableColumn
muxIfTraceExpected = _MuxIfTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 30),
    _MuxIfTraceExpected_Type()
)
muxIfTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxIfTraceExpected.setStatus("current")


class _MuxIfTraceAlarmMode_Type(Integer32):
    """Custom type muxIfTraceAlarmMode based on Integer32"""
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


_MuxIfTraceAlarmMode_Type.__name__ = "Integer32"
_MuxIfTraceAlarmMode_Object = MibTableColumn
muxIfTraceAlarmMode = _MuxIfTraceAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 31),
    _MuxIfTraceAlarmMode_Type()
)
muxIfTraceAlarmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxIfTraceAlarmMode.setStatus("current")
_MuxIfTraceMismatch_Type = FaultStatus
_MuxIfTraceMismatch_Object = MibTableColumn
muxIfTraceMismatch = _MuxIfTraceMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 32),
    _MuxIfTraceMismatch_Type()
)
muxIfTraceMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfTraceMismatch.setStatus("current")


class _MuxIfOHTransparency_Type(Integer32):
    """Custom type muxIfOHTransparency based on Integer32"""
    defaultValue = 1

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


_MuxIfOHTransparency_Type.__name__ = "Integer32"
_MuxIfOHTransparency_Object = MibTableColumn
muxIfOHTransparency = _MuxIfOHTransparency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 33),
    _MuxIfOHTransparency_Type()
)
muxIfOHTransparency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxIfOHTransparency.setStatus("current")


class _MuxIfSuppressRemoteAlarms_Type(Integer32):
    """Custom type muxIfSuppressRemoteAlarms based on Integer32"""
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


_MuxIfSuppressRemoteAlarms_Type.__name__ = "Integer32"
_MuxIfSuppressRemoteAlarms_Object = MibTableColumn
muxIfSuppressRemoteAlarms = _MuxIfSuppressRemoteAlarms_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 34),
    _MuxIfSuppressRemoteAlarms_Type()
)
muxIfSuppressRemoteAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxIfSuppressRemoteAlarms.setStatus("current")
_MuxIfHighSpeedMin_Type = Gauge32
_MuxIfHighSpeedMin_Object = MibTableColumn
muxIfHighSpeedMin = _MuxIfHighSpeedMin_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 35),
    _MuxIfHighSpeedMin_Type()
)
muxIfHighSpeedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfHighSpeedMin.setStatus("current")
_MuxIfHighSpeedMax_Type = Gauge32
_MuxIfHighSpeedMax_Object = MibTableColumn
muxIfHighSpeedMax = _MuxIfHighSpeedMax_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 36),
    _MuxIfHighSpeedMax_Type()
)
muxIfHighSpeedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfHighSpeedMax.setStatus("current")
_MuxIfTrxCodeMismatch_Type = FaultStatus
_MuxIfTrxCodeMismatch_Object = MibTableColumn
muxIfTrxCodeMismatch = _MuxIfTrxCodeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 37),
    _MuxIfTrxCodeMismatch_Type()
)
muxIfTrxCodeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfTrxCodeMismatch.setStatus("current")
_MuxIfTrxBitrateUnavailable_Type = FaultStatus
_MuxIfTrxBitrateUnavailable_Object = MibTableColumn
muxIfTrxBitrateUnavailable = _MuxIfTrxBitrateUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 38),
    _MuxIfTrxBitrateUnavailable_Type()
)
muxIfTrxBitrateUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfTrxBitrateUnavailable.setStatus("current")
_MuxIfTrxMissing_Type = FaultStatus
_MuxIfTrxMissing_Object = MibTableColumn
muxIfTrxMissing = _MuxIfTrxMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 39),
    _MuxIfTrxMissing_Type()
)
muxIfTrxMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfTrxMissing.setStatus("current")


class _MuxIfTrxClass_Type(DisplayString):
    """Custom type muxIfTrxClass based on DisplayString"""
    defaultValue = OctetString("")


_MuxIfTrxClass_Type.__name__ = "DisplayString"
_MuxIfTrxClass_Object = MibTableColumn
muxIfTrxClass = _MuxIfTrxClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 40),
    _MuxIfTrxClass_Type()
)
muxIfTrxClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfTrxClass.setStatus("current")
_MuxIfTransmitterFailed_Type = FaultStatus
_MuxIfTransmitterFailed_Object = MibTableColumn
muxIfTransmitterFailed = _MuxIfTransmitterFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 41),
    _MuxIfTransmitterFailed_Type()
)
muxIfTransmitterFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfTransmitterFailed.setStatus("current")
_MuxIfUnexpectedFrequency_Type = FaultStatus
_MuxIfUnexpectedFrequency_Object = MibTableColumn
muxIfUnexpectedFrequency = _MuxIfUnexpectedFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 42),
    _MuxIfUnexpectedFrequency_Type()
)
muxIfUnexpectedFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfUnexpectedFrequency.setStatus("current")
_MuxIfIllegalFrequency_Type = FaultStatus
_MuxIfIllegalFrequency_Object = MibTableColumn
muxIfIllegalFrequency = _MuxIfIllegalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 43),
    _MuxIfIllegalFrequency_Type()
)
muxIfIllegalFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfIllegalFrequency.setStatus("current")
_MuxIfReceiverSensitivity_Type = Integer32
_MuxIfReceiverSensitivity_Object = MibTableColumn
muxIfReceiverSensitivity = _MuxIfReceiverSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 44),
    _MuxIfReceiverSensitivity_Type()
)
muxIfReceiverSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfReceiverSensitivity.setStatus("current")


class _MuxIfPowerLevelLowRelativeThreshold_Type(Integer32):
    """Custom type muxIfPowerLevelLowRelativeThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_MuxIfPowerLevelLowRelativeThreshold_Type.__name__ = "Integer32"
_MuxIfPowerLevelLowRelativeThreshold_Object = MibTableColumn
muxIfPowerLevelLowRelativeThreshold = _MuxIfPowerLevelLowRelativeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 45),
    _MuxIfPowerLevelLowRelativeThreshold_Type()
)
muxIfPowerLevelLowRelativeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxIfPowerLevelLowRelativeThreshold.setStatus("current")
_MuxIfObjectProperty_Type = ObjectProperty
_MuxIfObjectProperty_Object = MibTableColumn
muxIfObjectProperty = _MuxIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 46),
    _MuxIfObjectProperty_Type()
)
muxIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfObjectProperty.setStatus("current")
_MuxIfTxPowerLevel_Type = Integer32
_MuxIfTxPowerLevel_Object = MibTableColumn
muxIfTxPowerLevel = _MuxIfTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 47),
    _MuxIfTxPowerLevel_Type()
)
muxIfTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfTxPowerLevel.setStatus("current")
_MuxIfLaserTempActual_Type = Integer32
_MuxIfLaserTempActual_Object = MibTableColumn
muxIfLaserTempActual = _MuxIfLaserTempActual_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 48),
    _MuxIfLaserTempActual_Type()
)
muxIfLaserTempActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfLaserTempActual.setStatus("current")
_MuxVc4List_ObjectIdentity = ObjectIdentity
muxVc4List = _MuxVc4List_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3)
)
_MuxVc4Table_Object = MibTable
muxVc4Table = _MuxVc4Table_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1)
)
if mibBuilder.loadTexts:
    muxVc4Table.setStatus("current")
_MuxVc4Entry_Object = MibTableRow
muxVc4Entry = _MuxVc4Entry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1)
)
muxVc4Entry.setIndexNames(
    (0, "LUM-MUX-MIB", "muxVc4Index"),
)
if mibBuilder.loadTexts:
    muxVc4Entry.setStatus("current")


class _MuxVc4Index_Type(Unsigned32):
    """Custom type muxVc4Index based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MuxVc4Index_Type.__name__ = "Unsigned32"
_MuxVc4Index_Object = MibTableColumn
muxVc4Index = _MuxVc4Index_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 1),
    _MuxVc4Index_Type()
)
muxVc4Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4Index.setStatus("current")
_MuxVc4Name_Type = MgmtNameString
_MuxVc4Name_Object = MibTableColumn
muxVc4Name = _MuxVc4Name_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 2),
    _MuxVc4Name_Type()
)
muxVc4Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4Name.setStatus("current")


class _MuxVc4Descr_Type(DisplayString):
    """Custom type muxVc4Descr based on DisplayString"""
    defaultValue = OctetString("")


_MuxVc4Descr_Type.__name__ = "DisplayString"
_MuxVc4Descr_Object = MibTableColumn
muxVc4Descr = _MuxVc4Descr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 3),
    _MuxVc4Descr_Type()
)
muxVc4Descr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxVc4Descr.setStatus("current")
_MuxVc4Subrack_Type = SubrackNumber
_MuxVc4Subrack_Object = MibTableColumn
muxVc4Subrack = _MuxVc4Subrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 4),
    _MuxVc4Subrack_Type()
)
muxVc4Subrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4Subrack.setStatus("current")
_MuxVc4Slot_Type = SlotNumber
_MuxVc4Slot_Object = MibTableColumn
muxVc4Slot = _MuxVc4Slot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 5),
    _MuxVc4Slot_Type()
)
muxVc4Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4Slot.setStatus("current")
_MuxVc4TxPort_Type = PortNumber
_MuxVc4TxPort_Object = MibTableColumn
muxVc4TxPort = _MuxVc4TxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 6),
    _MuxVc4TxPort_Type()
)
muxVc4TxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4TxPort.setStatus("current")
_MuxVc4RxPort_Type = PortNumber
_MuxVc4RxPort_Object = MibTableColumn
muxVc4RxPort = _MuxVc4RxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 7),
    _MuxVc4RxPort_Type()
)
muxVc4RxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4RxPort.setStatus("current")


class _MuxVc4Vc4_Type(Unsigned32):
    """Custom type muxVc4Vc4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MuxVc4Vc4_Type.__name__ = "Unsigned32"
_MuxVc4Vc4_Object = MibTableColumn
muxVc4Vc4 = _MuxVc4Vc4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 8),
    _MuxVc4Vc4_Type()
)
muxVc4Vc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4Vc4.setStatus("current")


class _MuxVc4Mode_Type(Integer32):
    """Custom type muxVc4Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addDrop", 1),
          ("passThrough", 2))
    )


_MuxVc4Mode_Type.__name__ = "Integer32"
_MuxVc4Mode_Object = MibTableColumn
muxVc4Mode = _MuxVc4Mode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 9),
    _MuxVc4Mode_Type()
)
muxVc4Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4Mode.setStatus("current")


class _MuxVc4ClientDropPort_Type(Unsigned32):
    """Custom type muxVc4ClientDropPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_MuxVc4ClientDropPort_Type.__name__ = "Unsigned32"
_MuxVc4ClientDropPort_Object = MibTableColumn
muxVc4ClientDropPort = _MuxVc4ClientDropPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 10),
    _MuxVc4ClientDropPort_Type()
)
muxVc4ClientDropPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4ClientDropPort.setStatus("current")
_MuxVc4TxDirection_Type = MuxTxDirection
_MuxVc4TxDirection_Object = MibTableColumn
muxVc4TxDirection = _MuxVc4TxDirection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 11),
    _MuxVc4TxDirection_Type()
)
muxVc4TxDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4TxDirection.setStatus("current")


class _MuxVc4ClientAddPort_Type(Unsigned32):
    """Custom type muxVc4ClientAddPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_MuxVc4ClientAddPort_Type.__name__ = "Unsigned32"
_MuxVc4ClientAddPort_Object = MibTableColumn
muxVc4ClientAddPort = _MuxVc4ClientAddPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 12),
    _MuxVc4ClientAddPort_Type()
)
muxVc4ClientAddPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4ClientAddPort.setStatus("current")


class _MuxVc4ConnectionMode_Type(Integer32):
    """Custom type muxVc4ConnectionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unused", 1),
          ("ringUsed", 2),
          ("nodeUsed", 3))
    )


_MuxVc4ConnectionMode_Type.__name__ = "Integer32"
_MuxVc4ConnectionMode_Object = MibTableColumn
muxVc4ConnectionMode = _MuxVc4ConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 13),
    _MuxVc4ConnectionMode_Type()
)
muxVc4ConnectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxVc4ConnectionMode.setStatus("deprecated")


class _MuxVc4ConnectionStatus_Type(Integer32):
    """Custom type muxVc4ConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("addDrop", 1),
          ("passThrough", 2),
          ("unconnected", 3))
    )


_MuxVc4ConnectionStatus_Type.__name__ = "Integer32"
_MuxVc4ConnectionStatus_Object = MibTableColumn
muxVc4ConnectionStatus = _MuxVc4ConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 14),
    _MuxVc4ConnectionStatus_Type()
)
muxVc4ConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4ConnectionStatus.setStatus("deprecated")
_MuxVc4ConnectionOverview_Type = DisplayString
_MuxVc4ConnectionOverview_Object = MibTableColumn
muxVc4ConnectionOverview = _MuxVc4ConnectionOverview_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 15),
    _MuxVc4ConnectionOverview_Type()
)
muxVc4ConnectionOverview.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4ConnectionOverview.setStatus("current")
_MuxVc4ObjectProperty_Type = ObjectProperty
_MuxVc4ObjectProperty_Object = MibTableColumn
muxVc4ObjectProperty = _MuxVc4ObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 16),
    _MuxVc4ObjectProperty_Type()
)
muxVc4ObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4ObjectProperty.setStatus("current")


class _MuxVc4AuAlarmIndicationSignalW2C_Type(Integer32):
    """Custom type muxVc4AuAlarmIndicationSignalW2C based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("alarm", 2))
    )


_MuxVc4AuAlarmIndicationSignalW2C_Type.__name__ = "Integer32"
_MuxVc4AuAlarmIndicationSignalW2C_Object = MibTableColumn
muxVc4AuAlarmIndicationSignalW2C = _MuxVc4AuAlarmIndicationSignalW2C_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 17),
    _MuxVc4AuAlarmIndicationSignalW2C_Type()
)
muxVc4AuAlarmIndicationSignalW2C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4AuAlarmIndicationSignalW2C.setStatus("current")


class _MuxVc4AuLossOfPointerW2C_Type(Integer32):
    """Custom type muxVc4AuLossOfPointerW2C based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("alarm", 2))
    )


_MuxVc4AuLossOfPointerW2C_Type.__name__ = "Integer32"
_MuxVc4AuLossOfPointerW2C_Object = MibTableColumn
muxVc4AuLossOfPointerW2C = _MuxVc4AuLossOfPointerW2C_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 18),
    _MuxVc4AuLossOfPointerW2C_Type()
)
muxVc4AuLossOfPointerW2C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4AuLossOfPointerW2C.setStatus("current")


class _MuxVc4RxSignalStatus_Type(Integer32):
    """Custom type muxVc4RxSignalStatus based on Integer32"""
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


_MuxVc4RxSignalStatus_Type.__name__ = "Integer32"
_MuxVc4RxSignalStatus_Object = MibTableColumn
muxVc4RxSignalStatus = _MuxVc4RxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 19),
    _MuxVc4RxSignalStatus_Type()
)
muxVc4RxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4RxSignalStatus.setStatus("current")


class _MuxVc4ConcatenationStatus_Type(Integer32):
    """Custom type muxVc4ConcatenationStatus based on Integer32"""
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


_MuxVc4ConcatenationStatus_Type.__name__ = "Integer32"
_MuxVc4ConcatenationStatus_Object = MibTableColumn
muxVc4ConcatenationStatus = _MuxVc4ConcatenationStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 20),
    _MuxVc4ConcatenationStatus_Type()
)
muxVc4ConcatenationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4ConcatenationStatus.setStatus("current")


class _MuxVc4PayloadStatus_Type(Integer32):
    """Custom type muxVc4PayloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equipped", 1),
          ("unequipped", 2))
    )


_MuxVc4PayloadStatus_Type.__name__ = "Integer32"
_MuxVc4PayloadStatus_Object = MibTableColumn
muxVc4PayloadStatus = _MuxVc4PayloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 21),
    _MuxVc4PayloadStatus_Type()
)
muxVc4PayloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVc4PayloadStatus.setStatus("current")


class _MuxVc4AdminStatus_Type(Integer32):
    """Custom type muxVc4AdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_MuxVc4AdminStatus_Type.__name__ = "Integer32"
_MuxVc4AdminStatus_Object = MibTableColumn
muxVc4AdminStatus = _MuxVc4AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 22),
    _MuxVc4AdminStatus_Type()
)
muxVc4AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxVc4AdminStatus.setStatus("current")

# Managed Objects groups

muxGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 1)
)
muxGeneralGroup.setObjects(
    ("LUM-MUX-MIB", "muxGeneralLastChangeTime")
)
if mibBuilder.loadTexts:
    muxGeneralGroup.setStatus("current")

muxIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 2)
)
muxIfGroup.setObjects(
      *(("LUM-MUX-MIB", "muxIfIndex"),
        ("LUM-MUX-MIB", "muxIfName"),
        ("LUM-MUX-MIB", "muxIfDescr"),
        ("LUM-MUX-MIB", "muxIfSubrack"),
        ("LUM-MUX-MIB", "muxIfSlot"),
        ("LUM-MUX-MIB", "muxIfTxPort"),
        ("LUM-MUX-MIB", "muxIfRxPort"),
        ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"),
        ("LUM-MUX-MIB", "muxIfPowerLevel"),
        ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"),
        ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"),
        ("LUM-MUX-MIB", "muxIfAdminStatus"),
        ("LUM-MUX-MIB", "muxIfOperStatus"),
        ("LUM-MUX-MIB", "muxIfLossOfSignal"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerLow"))
)
if mibBuilder.loadTexts:
    muxIfGroup.setStatus("current")

muxIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 3)
)
muxIfGroupV2.setObjects(
      *(("LUM-MUX-MIB", "muxIfIndex"),
        ("LUM-MUX-MIB", "muxIfName"),
        ("LUM-MUX-MIB", "muxIfDescr"),
        ("LUM-MUX-MIB", "muxIfSubrack"),
        ("LUM-MUX-MIB", "muxIfSlot"),
        ("LUM-MUX-MIB", "muxIfTxPort"),
        ("LUM-MUX-MIB", "muxIfRxPort"),
        ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"),
        ("LUM-MUX-MIB", "muxIfPowerLevel"),
        ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"),
        ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"),
        ("LUM-MUX-MIB", "muxIfAdminStatus"),
        ("LUM-MUX-MIB", "muxIfOperStatus"),
        ("LUM-MUX-MIB", "muxIfLossOfSignal"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerLow"),
        ("LUM-MUX-MIB", "muxIfBitrateMismatch"),
        ("LUM-MUX-MIB", "muxIfLaserBias"),
        ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"),
        ("LUM-MUX-MIB", "muxIfJ0PathTrace"))
)
if mibBuilder.loadTexts:
    muxIfGroupV2.setStatus("deprecated")

muxIfGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 4)
)
muxIfGroupV3.setObjects(
      *(("LUM-MUX-MIB", "muxIfIndex"),
        ("LUM-MUX-MIB", "muxIfName"),
        ("LUM-MUX-MIB", "muxIfDescr"),
        ("LUM-MUX-MIB", "muxIfSubrack"),
        ("LUM-MUX-MIB", "muxIfSlot"),
        ("LUM-MUX-MIB", "muxIfTxPort"),
        ("LUM-MUX-MIB", "muxIfRxPort"),
        ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"),
        ("LUM-MUX-MIB", "muxIfPowerLevel"),
        ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"),
        ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"),
        ("LUM-MUX-MIB", "muxIfAdminStatus"),
        ("LUM-MUX-MIB", "muxIfOperStatus"),
        ("LUM-MUX-MIB", "muxIfLossOfSignal"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerLow"),
        ("LUM-MUX-MIB", "muxIfBitrateMismatch"),
        ("LUM-MUX-MIB", "muxIfLaserBias"),
        ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"),
        ("LUM-MUX-MIB", "muxIfJ0PathTrace"),
        ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"),
        ("LUM-MUX-MIB", "muxIfLossOfFrame"))
)
if mibBuilder.loadTexts:
    muxIfGroupV3.setStatus("deprecated")

muxIfGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 5)
)
muxIfGroupV4.setObjects(
      *(("LUM-MUX-MIB", "muxIfIndex"),
        ("LUM-MUX-MIB", "muxIfName"),
        ("LUM-MUX-MIB", "muxIfDescr"),
        ("LUM-MUX-MIB", "muxIfSubrack"),
        ("LUM-MUX-MIB", "muxIfSlot"),
        ("LUM-MUX-MIB", "muxIfTxPort"),
        ("LUM-MUX-MIB", "muxIfRxPort"),
        ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"),
        ("LUM-MUX-MIB", "muxIfPowerLevel"),
        ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"),
        ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"),
        ("LUM-MUX-MIB", "muxIfAdminStatus"),
        ("LUM-MUX-MIB", "muxIfOperStatus"),
        ("LUM-MUX-MIB", "muxIfLossOfSignal"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerLow"),
        ("LUM-MUX-MIB", "muxIfBitrateMismatch"),
        ("LUM-MUX-MIB", "muxIfLaserBias"),
        ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"),
        ("LUM-MUX-MIB", "muxIfJ0PathTrace"),
        ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"),
        ("LUM-MUX-MIB", "muxIfLossOfFrame"),
        ("LUM-MUX-MIB", "muxIfLaserStatus"))
)
if mibBuilder.loadTexts:
    muxIfGroupV4.setStatus("deprecated")

muxGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 6)
)
muxGeneralGroupV2.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralLastChangeTime"),
        ("LUM-MUX-MIB", "muxGeneralStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    muxGeneralGroupV2.setStatus("deprecated")

muxVc4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 7)
)
muxVc4Group.setObjects(
      *(("LUM-MUX-MIB", "muxVc4Index"),
        ("LUM-MUX-MIB", "muxVc4Name"),
        ("LUM-MUX-MIB", "muxVc4Descr"),
        ("LUM-MUX-MIB", "muxVc4Subrack"),
        ("LUM-MUX-MIB", "muxVc4Slot"),
        ("LUM-MUX-MIB", "muxVc4TxPort"),
        ("LUM-MUX-MIB", "muxVc4RxPort"),
        ("LUM-MUX-MIB", "muxVc4Vc4"),
        ("LUM-MUX-MIB", "muxVc4Mode"),
        ("LUM-MUX-MIB", "muxVc4ClientDropPort"))
)
if mibBuilder.loadTexts:
    muxVc4Group.setStatus("deprecated")

muxIfGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 8)
)
muxIfGroupV5.setObjects(
      *(("LUM-MUX-MIB", "muxIfIndex"),
        ("LUM-MUX-MIB", "muxIfName"),
        ("LUM-MUX-MIB", "muxIfDescr"),
        ("LUM-MUX-MIB", "muxIfSubrack"),
        ("LUM-MUX-MIB", "muxIfSlot"),
        ("LUM-MUX-MIB", "muxIfTxPort"),
        ("LUM-MUX-MIB", "muxIfRxPort"),
        ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"),
        ("LUM-MUX-MIB", "muxIfPowerLevel"),
        ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"),
        ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"),
        ("LUM-MUX-MIB", "muxIfAdminStatus"),
        ("LUM-MUX-MIB", "muxIfOperStatus"),
        ("LUM-MUX-MIB", "muxIfLossOfSignal"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerLow"),
        ("LUM-MUX-MIB", "muxIfBitrateMismatch"),
        ("LUM-MUX-MIB", "muxIfLaserBias"),
        ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"),
        ("LUM-MUX-MIB", "muxIfJ0PathTrace"),
        ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"),
        ("LUM-MUX-MIB", "muxIfLossOfFrame"),
        ("LUM-MUX-MIB", "muxIfLaserStatus"),
        ("LUM-MUX-MIB", "muxIfTxDirection"))
)
if mibBuilder.loadTexts:
    muxIfGroupV5.setStatus("deprecated")

muxVc4GroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 9)
)
muxVc4GroupV2.setObjects(
      *(("LUM-MUX-MIB", "muxVc4Index"),
        ("LUM-MUX-MIB", "muxVc4Name"),
        ("LUM-MUX-MIB", "muxVc4Descr"),
        ("LUM-MUX-MIB", "muxVc4Subrack"),
        ("LUM-MUX-MIB", "muxVc4Slot"),
        ("LUM-MUX-MIB", "muxVc4TxPort"),
        ("LUM-MUX-MIB", "muxVc4RxPort"),
        ("LUM-MUX-MIB", "muxVc4Vc4"),
        ("LUM-MUX-MIB", "muxVc4Mode"),
        ("LUM-MUX-MIB", "muxVc4ClientDropPort"),
        ("LUM-MUX-MIB", "muxVc4TxDirection"),
        ("LUM-MUX-MIB", "muxVc4ClientAddPort"))
)
if mibBuilder.loadTexts:
    muxVc4GroupV2.setStatus("deprecated")

muxIfGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 10)
)
muxIfGroupV6.setObjects(
      *(("LUM-MUX-MIB", "muxIfIndex"),
        ("LUM-MUX-MIB", "muxIfName"),
        ("LUM-MUX-MIB", "muxIfDescr"),
        ("LUM-MUX-MIB", "muxIfSubrack"),
        ("LUM-MUX-MIB", "muxIfSlot"),
        ("LUM-MUX-MIB", "muxIfTxPort"),
        ("LUM-MUX-MIB", "muxIfRxPort"),
        ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"),
        ("LUM-MUX-MIB", "muxIfPowerLevel"),
        ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"),
        ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"),
        ("LUM-MUX-MIB", "muxIfAdminStatus"),
        ("LUM-MUX-MIB", "muxIfOperStatus"),
        ("LUM-MUX-MIB", "muxIfLossOfSignal"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerLow"),
        ("LUM-MUX-MIB", "muxIfBitrateMismatch"),
        ("LUM-MUX-MIB", "muxIfLaserBias"),
        ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"),
        ("LUM-MUX-MIB", "muxIfJ0PathTrace"),
        ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"),
        ("LUM-MUX-MIB", "muxIfLossOfFrame"),
        ("LUM-MUX-MIB", "muxIfLaserStatus"),
        ("LUM-MUX-MIB", "muxIfTxDirection"),
        ("LUM-MUX-MIB", "muxIfExpectedTxLambda"),
        ("LUM-MUX-MIB", "muxIfTxLambda"))
)
if mibBuilder.loadTexts:
    muxIfGroupV6.setStatus("deprecated")

muxIfGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 11)
)
muxIfGroupV7.setObjects(
      *(("LUM-MUX-MIB", "muxIfIndex"),
        ("LUM-MUX-MIB", "muxIfName"),
        ("LUM-MUX-MIB", "muxIfDescr"),
        ("LUM-MUX-MIB", "muxIfSubrack"),
        ("LUM-MUX-MIB", "muxIfSlot"),
        ("LUM-MUX-MIB", "muxIfTxPort"),
        ("LUM-MUX-MIB", "muxIfRxPort"),
        ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"),
        ("LUM-MUX-MIB", "muxIfPowerLevel"),
        ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"),
        ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"),
        ("LUM-MUX-MIB", "muxIfAdminStatus"),
        ("LUM-MUX-MIB", "muxIfOperStatus"),
        ("LUM-MUX-MIB", "muxIfLossOfSignal"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerLow"),
        ("LUM-MUX-MIB", "muxIfBitrateMismatch"),
        ("LUM-MUX-MIB", "muxIfLaserBias"),
        ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"),
        ("LUM-MUX-MIB", "muxIfJ0PathTrace"),
        ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"),
        ("LUM-MUX-MIB", "muxIfLossOfFrame"),
        ("LUM-MUX-MIB", "muxIfLaserStatus"),
        ("LUM-MUX-MIB", "muxIfTxDirection"),
        ("LUM-MUX-MIB", "muxIfExpectedTxLambda"),
        ("LUM-MUX-MIB", "muxIfTxLambda"),
        ("LUM-MUX-MIB", "muxIfTraceIntrusionMode"),
        ("LUM-MUX-MIB", "muxIfTraceTransmitted"),
        ("LUM-MUX-MIB", "muxIfTraceReceived"),
        ("LUM-MUX-MIB", "muxIfTraceExpected"),
        ("LUM-MUX-MIB", "muxIfTraceAlarmMode"),
        ("LUM-MUX-MIB", "muxIfTraceMismatch"))
)
if mibBuilder.loadTexts:
    muxIfGroupV7.setStatus("deprecated")

muxIfGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 12)
)
muxIfGroupV8.setObjects(
      *(("LUM-MUX-MIB", "muxIfIndex"),
        ("LUM-MUX-MIB", "muxIfName"),
        ("LUM-MUX-MIB", "muxIfDescr"),
        ("LUM-MUX-MIB", "muxIfSubrack"),
        ("LUM-MUX-MIB", "muxIfSlot"),
        ("LUM-MUX-MIB", "muxIfTxPort"),
        ("LUM-MUX-MIB", "muxIfRxPort"),
        ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"),
        ("LUM-MUX-MIB", "muxIfPowerLevel"),
        ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"),
        ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"),
        ("LUM-MUX-MIB", "muxIfAdminStatus"),
        ("LUM-MUX-MIB", "muxIfOperStatus"),
        ("LUM-MUX-MIB", "muxIfLossOfSignal"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerLow"),
        ("LUM-MUX-MIB", "muxIfBitrateMismatch"),
        ("LUM-MUX-MIB", "muxIfLaserBias"),
        ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"),
        ("LUM-MUX-MIB", "muxIfJ0PathTrace"),
        ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"),
        ("LUM-MUX-MIB", "muxIfLossOfFrame"),
        ("LUM-MUX-MIB", "muxIfLaserStatus"),
        ("LUM-MUX-MIB", "muxIfTxDirection"),
        ("LUM-MUX-MIB", "muxIfExpectedTxLambda"),
        ("LUM-MUX-MIB", "muxIfTxLambda"),
        ("LUM-MUX-MIB", "muxIfTraceIntrusionMode"),
        ("LUM-MUX-MIB", "muxIfTraceTransmitted"),
        ("LUM-MUX-MIB", "muxIfTraceReceived"),
        ("LUM-MUX-MIB", "muxIfTraceExpected"),
        ("LUM-MUX-MIB", "muxIfTraceAlarmMode"),
        ("LUM-MUX-MIB", "muxIfTraceMismatch"))
)
if mibBuilder.loadTexts:
    muxIfGroupV8.setStatus("deprecated")

muxVc4GroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 13)
)
muxVc4GroupV3.setObjects(
      *(("LUM-MUX-MIB", "muxVc4Index"),
        ("LUM-MUX-MIB", "muxVc4Name"),
        ("LUM-MUX-MIB", "muxVc4Descr"),
        ("LUM-MUX-MIB", "muxVc4Subrack"),
        ("LUM-MUX-MIB", "muxVc4Slot"),
        ("LUM-MUX-MIB", "muxVc4TxPort"),
        ("LUM-MUX-MIB", "muxVc4RxPort"),
        ("LUM-MUX-MIB", "muxVc4Vc4"),
        ("LUM-MUX-MIB", "muxVc4Mode"),
        ("LUM-MUX-MIB", "muxVc4ClientDropPort"),
        ("LUM-MUX-MIB", "muxVc4TxDirection"),
        ("LUM-MUX-MIB", "muxVc4ClientAddPort"),
        ("LUM-MUX-MIB", "muxVc4ConnectionMode"),
        ("LUM-MUX-MIB", "muxVc4ConnectionStatus"))
)
if mibBuilder.loadTexts:
    muxVc4GroupV3.setStatus("deprecated")

muxVc4GroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 14)
)
muxVc4GroupV4.setObjects(
      *(("LUM-MUX-MIB", "muxVc4Index"),
        ("LUM-MUX-MIB", "muxVc4Name"),
        ("LUM-MUX-MIB", "muxVc4Descr"),
        ("LUM-MUX-MIB", "muxVc4Subrack"),
        ("LUM-MUX-MIB", "muxVc4Slot"),
        ("LUM-MUX-MIB", "muxVc4TxPort"),
        ("LUM-MUX-MIB", "muxVc4RxPort"),
        ("LUM-MUX-MIB", "muxVc4Vc4"),
        ("LUM-MUX-MIB", "muxVc4ClientDropPort"),
        ("LUM-MUX-MIB", "muxVc4TxDirection"),
        ("LUM-MUX-MIB", "muxVc4ClientAddPort"),
        ("LUM-MUX-MIB", "muxVc4ConnectionMode"),
        ("LUM-MUX-MIB", "muxVc4ConnectionStatus"),
        ("LUM-MUX-MIB", "muxVc4ConnectionOverview"))
)
if mibBuilder.loadTexts:
    muxVc4GroupV4.setStatus("deprecated")

muxVc4GroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 15)
)
muxVc4GroupV5.setObjects(
      *(("LUM-MUX-MIB", "muxVc4Index"),
        ("LUM-MUX-MIB", "muxVc4Name"),
        ("LUM-MUX-MIB", "muxVc4Descr"),
        ("LUM-MUX-MIB", "muxVc4Subrack"),
        ("LUM-MUX-MIB", "muxVc4Slot"),
        ("LUM-MUX-MIB", "muxVc4TxPort"),
        ("LUM-MUX-MIB", "muxVc4RxPort"),
        ("LUM-MUX-MIB", "muxVc4Vc4"),
        ("LUM-MUX-MIB", "muxVc4ClientDropPort"),
        ("LUM-MUX-MIB", "muxVc4TxDirection"),
        ("LUM-MUX-MIB", "muxVc4ClientAddPort"),
        ("LUM-MUX-MIB", "muxVc4ConnectionOverview"))
)
if mibBuilder.loadTexts:
    muxVc4GroupV5.setStatus("deprecated")

muxIfGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 16)
)
muxIfGroupV9.setObjects(
      *(("LUM-MUX-MIB", "muxIfIndex"),
        ("LUM-MUX-MIB", "muxIfName"),
        ("LUM-MUX-MIB", "muxIfDescr"),
        ("LUM-MUX-MIB", "muxIfSubrack"),
        ("LUM-MUX-MIB", "muxIfSlot"),
        ("LUM-MUX-MIB", "muxIfTxPort"),
        ("LUM-MUX-MIB", "muxIfRxPort"),
        ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"),
        ("LUM-MUX-MIB", "muxIfPowerLevel"),
        ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"),
        ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"),
        ("LUM-MUX-MIB", "muxIfAdminStatus"),
        ("LUM-MUX-MIB", "muxIfOperStatus"),
        ("LUM-MUX-MIB", "muxIfLossOfSignal"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerLow"),
        ("LUM-MUX-MIB", "muxIfBitrateMismatch"),
        ("LUM-MUX-MIB", "muxIfLaserBias"),
        ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"),
        ("LUM-MUX-MIB", "muxIfJ0PathTrace"),
        ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"),
        ("LUM-MUX-MIB", "muxIfLossOfFrame"),
        ("LUM-MUX-MIB", "muxIfLaserStatus"),
        ("LUM-MUX-MIB", "muxIfTxDirection"),
        ("LUM-MUX-MIB", "muxIfExpectedTxLambda"),
        ("LUM-MUX-MIB", "muxIfTxLambda"),
        ("LUM-MUX-MIB", "muxIfTraceIntrusionMode"),
        ("LUM-MUX-MIB", "muxIfTraceTransmitted"),
        ("LUM-MUX-MIB", "muxIfTraceReceived"),
        ("LUM-MUX-MIB", "muxIfTraceExpected"),
        ("LUM-MUX-MIB", "muxIfTraceAlarmMode"),
        ("LUM-MUX-MIB", "muxIfTraceMismatch"),
        ("LUM-MUX-MIB", "muxIfSuppressRemoteAlarms"))
)
if mibBuilder.loadTexts:
    muxIfGroupV9.setStatus("deprecated")

muxIfGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 17)
)
muxIfGroupV10.setObjects(
      *(("LUM-MUX-MIB", "muxIfIndex"),
        ("LUM-MUX-MIB", "muxIfName"),
        ("LUM-MUX-MIB", "muxIfDescr"),
        ("LUM-MUX-MIB", "muxIfSubrack"),
        ("LUM-MUX-MIB", "muxIfSlot"),
        ("LUM-MUX-MIB", "muxIfTxPort"),
        ("LUM-MUX-MIB", "muxIfRxPort"),
        ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"),
        ("LUM-MUX-MIB", "muxIfPowerLevel"),
        ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"),
        ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"),
        ("LUM-MUX-MIB", "muxIfAdminStatus"),
        ("LUM-MUX-MIB", "muxIfOperStatus"),
        ("LUM-MUX-MIB", "muxIfLossOfSignal"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerLow"),
        ("LUM-MUX-MIB", "muxIfBitrateMismatch"),
        ("LUM-MUX-MIB", "muxIfLaserBias"),
        ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"),
        ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"),
        ("LUM-MUX-MIB", "muxIfLossOfFrame"),
        ("LUM-MUX-MIB", "muxIfLaserStatus"),
        ("LUM-MUX-MIB", "muxIfTxDirection"),
        ("LUM-MUX-MIB", "muxIfExpectedTxLambda"),
        ("LUM-MUX-MIB", "muxIfTxLambda"),
        ("LUM-MUX-MIB", "muxIfTraceIntrusionMode"),
        ("LUM-MUX-MIB", "muxIfTraceTransmitted"),
        ("LUM-MUX-MIB", "muxIfTraceReceived"),
        ("LUM-MUX-MIB", "muxIfTraceExpected"),
        ("LUM-MUX-MIB", "muxIfTraceAlarmMode"),
        ("LUM-MUX-MIB", "muxIfTraceMismatch"),
        ("LUM-MUX-MIB", "muxIfOHTransparency"),
        ("LUM-MUX-MIB", "muxIfSuppressRemoteAlarms"),
        ("LUM-MUX-MIB", "muxIfHighSpeedMin"),
        ("LUM-MUX-MIB", "muxIfHighSpeedMax"),
        ("LUM-MUX-MIB", "muxIfTrxCodeMismatch"),
        ("LUM-MUX-MIB", "muxIfTrxBitrateUnavailable"),
        ("LUM-MUX-MIB", "muxIfTrxMissing"),
        ("LUM-MUX-MIB", "muxIfTrxClass"),
        ("LUM-MUX-MIB", "muxIfTransmitterFailed"))
)
if mibBuilder.loadTexts:
    muxIfGroupV10.setStatus("deprecated")

muxIfGroupV11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 18)
)
muxIfGroupV11.setObjects(
      *(("LUM-MUX-MIB", "muxIfIndex"),
        ("LUM-MUX-MIB", "muxIfName"),
        ("LUM-MUX-MIB", "muxIfDescr"),
        ("LUM-MUX-MIB", "muxIfSubrack"),
        ("LUM-MUX-MIB", "muxIfSlot"),
        ("LUM-MUX-MIB", "muxIfTxPort"),
        ("LUM-MUX-MIB", "muxIfRxPort"),
        ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"),
        ("LUM-MUX-MIB", "muxIfPowerLevel"),
        ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"),
        ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"),
        ("LUM-MUX-MIB", "muxIfAdminStatus"),
        ("LUM-MUX-MIB", "muxIfOperStatus"),
        ("LUM-MUX-MIB", "muxIfLossOfSignal"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerLow"),
        ("LUM-MUX-MIB", "muxIfBitrateMismatch"),
        ("LUM-MUX-MIB", "muxIfLaserBias"),
        ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"),
        ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"),
        ("LUM-MUX-MIB", "muxIfLossOfFrame"),
        ("LUM-MUX-MIB", "muxIfLaserStatus"),
        ("LUM-MUX-MIB", "muxIfTxDirection"),
        ("LUM-MUX-MIB", "muxIfExpectedTxLambda"),
        ("LUM-MUX-MIB", "muxIfTxLambda"),
        ("LUM-MUX-MIB", "muxIfTraceIntrusionMode"),
        ("LUM-MUX-MIB", "muxIfTraceTransmitted"),
        ("LUM-MUX-MIB", "muxIfTraceReceived"),
        ("LUM-MUX-MIB", "muxIfTraceExpected"),
        ("LUM-MUX-MIB", "muxIfTraceAlarmMode"),
        ("LUM-MUX-MIB", "muxIfTraceMismatch"),
        ("LUM-MUX-MIB", "muxIfOHTransparency"),
        ("LUM-MUX-MIB", "muxIfSuppressRemoteAlarms"),
        ("LUM-MUX-MIB", "muxIfHighSpeedMin"),
        ("LUM-MUX-MIB", "muxIfHighSpeedMax"),
        ("LUM-MUX-MIB", "muxIfTrxCodeMismatch"),
        ("LUM-MUX-MIB", "muxIfTrxBitrateUnavailable"),
        ("LUM-MUX-MIB", "muxIfTrxMissing"),
        ("LUM-MUX-MIB", "muxIfTrxClass"),
        ("LUM-MUX-MIB", "muxIfTransmitterFailed"),
        ("LUM-MUX-MIB", "muxIfIllegalFrequency"),
        ("LUM-MUX-MIB", "muxIfReceiverSensitivity"),
        ("LUM-MUX-MIB", "muxIfPowerLevelLowRelativeThreshold"))
)
if mibBuilder.loadTexts:
    muxIfGroupV11.setStatus("deprecated")

muxGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 19)
)
muxGeneralGroupV3.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralLastChangeTime"),
        ("LUM-MUX-MIB", "muxGeneralStateLastChangeTime"),
        ("LUM-MUX-MIB", "muxGeneralMuxIfTableSize"),
        ("LUM-MUX-MIB", "muxGeneralMuxVc4TableSize"))
)
if mibBuilder.loadTexts:
    muxGeneralGroupV3.setStatus("current")

muxIfGroupV12 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 20)
)
muxIfGroupV12.setObjects(
      *(("LUM-MUX-MIB", "muxIfIndex"),
        ("LUM-MUX-MIB", "muxIfName"),
        ("LUM-MUX-MIB", "muxIfDescr"),
        ("LUM-MUX-MIB", "muxIfSubrack"),
        ("LUM-MUX-MIB", "muxIfSlot"),
        ("LUM-MUX-MIB", "muxIfTxPort"),
        ("LUM-MUX-MIB", "muxIfRxPort"),
        ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"),
        ("LUM-MUX-MIB", "muxIfPowerLevel"),
        ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"),
        ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"),
        ("LUM-MUX-MIB", "muxIfAdminStatus"),
        ("LUM-MUX-MIB", "muxIfOperStatus"),
        ("LUM-MUX-MIB", "muxIfLossOfSignal"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"),
        ("LUM-MUX-MIB", "muxIfReceivedPowerLow"),
        ("LUM-MUX-MIB", "muxIfBitrateMismatch"),
        ("LUM-MUX-MIB", "muxIfLaserBias"),
        ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"),
        ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"),
        ("LUM-MUX-MIB", "muxIfLossOfFrame"),
        ("LUM-MUX-MIB", "muxIfLaserStatus"),
        ("LUM-MUX-MIB", "muxIfTxDirection"),
        ("LUM-MUX-MIB", "muxIfExpectedTxLambda"),
        ("LUM-MUX-MIB", "muxIfTxLambda"),
        ("LUM-MUX-MIB", "muxIfTraceIntrusionMode"),
        ("LUM-MUX-MIB", "muxIfTraceTransmitted"),
        ("LUM-MUX-MIB", "muxIfTraceReceived"),
        ("LUM-MUX-MIB", "muxIfTraceExpected"),
        ("LUM-MUX-MIB", "muxIfTraceAlarmMode"),
        ("LUM-MUX-MIB", "muxIfTraceMismatch"),
        ("LUM-MUX-MIB", "muxIfOHTransparency"),
        ("LUM-MUX-MIB", "muxIfSuppressRemoteAlarms"),
        ("LUM-MUX-MIB", "muxIfHighSpeedMin"),
        ("LUM-MUX-MIB", "muxIfHighSpeedMax"),
        ("LUM-MUX-MIB", "muxIfTrxCodeMismatch"),
        ("LUM-MUX-MIB", "muxIfTrxBitrateUnavailable"),
        ("LUM-MUX-MIB", "muxIfTrxMissing"),
        ("LUM-MUX-MIB", "muxIfTrxClass"),
        ("LUM-MUX-MIB", "muxIfTransmitterFailed"),
        ("LUM-MUX-MIB", "muxIfUnexpectedFrequency"),
        ("LUM-MUX-MIB", "muxIfIllegalFrequency"),
        ("LUM-MUX-MIB", "muxIfReceiverSensitivity"),
        ("LUM-MUX-MIB", "muxIfPowerLevelLowRelativeThreshold"),
        ("LUM-MUX-MIB", "muxIfObjectProperty"),
        ("LUM-MUX-MIB", "muxIfTxPowerLevel"),
        ("LUM-MUX-MIB", "muxIfLaserTempActual"))
)
if mibBuilder.loadTexts:
    muxIfGroupV12.setStatus("current")

muxVc4GroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 21)
)
muxVc4GroupV6.setObjects(
      *(("LUM-MUX-MIB", "muxVc4Index"),
        ("LUM-MUX-MIB", "muxVc4Name"),
        ("LUM-MUX-MIB", "muxVc4Descr"),
        ("LUM-MUX-MIB", "muxVc4Subrack"),
        ("LUM-MUX-MIB", "muxVc4Slot"),
        ("LUM-MUX-MIB", "muxVc4TxPort"),
        ("LUM-MUX-MIB", "muxVc4RxPort"),
        ("LUM-MUX-MIB", "muxVc4Vc4"),
        ("LUM-MUX-MIB", "muxVc4ClientDropPort"),
        ("LUM-MUX-MIB", "muxVc4TxDirection"),
        ("LUM-MUX-MIB", "muxVc4ClientAddPort"),
        ("LUM-MUX-MIB", "muxVc4ConnectionOverview"),
        ("LUM-MUX-MIB", "muxVc4ObjectProperty"))
)
if mibBuilder.loadTexts:
    muxVc4GroupV6.setStatus("deprecated")

muxVc4GroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 22)
)
muxVc4GroupV7.setObjects(
      *(("LUM-MUX-MIB", "muxVc4Index"),
        ("LUM-MUX-MIB", "muxVc4Name"),
        ("LUM-MUX-MIB", "muxVc4Descr"),
        ("LUM-MUX-MIB", "muxVc4Subrack"),
        ("LUM-MUX-MIB", "muxVc4Slot"),
        ("LUM-MUX-MIB", "muxVc4TxPort"),
        ("LUM-MUX-MIB", "muxVc4RxPort"),
        ("LUM-MUX-MIB", "muxVc4Vc4"),
        ("LUM-MUX-MIB", "muxVc4ClientDropPort"),
        ("LUM-MUX-MIB", "muxVc4TxDirection"),
        ("LUM-MUX-MIB", "muxVc4ClientAddPort"),
        ("LUM-MUX-MIB", "muxVc4ConnectionOverview"),
        ("LUM-MUX-MIB", "muxVc4ObjectProperty"),
        ("LUM-MUX-MIB", "muxVc4AuAlarmIndicationSignalW2C"),
        ("LUM-MUX-MIB", "muxVc4AuLossOfPointerW2C"),
        ("LUM-MUX-MIB", "muxVc4RxSignalStatus"),
        ("LUM-MUX-MIB", "muxVc4ConcatenationStatus"),
        ("LUM-MUX-MIB", "muxVc4PayloadStatus"),
        ("LUM-MUX-MIB", "muxVc4AdminStatus"))
)
if mibBuilder.loadTexts:
    muxVc4GroupV7.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumMuxBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 1)
)
lumMuxBasicComplV1.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroup"),
        ("LUM-MUX-MIB", "muxIfGroup"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV1.setStatus(
        "current"
    )

lumMuxBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 2)
)
lumMuxBasicComplV2.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroup"),
        ("LUM-MUX-MIB", "muxIfGroupV2"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV2.setStatus(
        "deprecated"
    )

lumMuxBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 3)
)
lumMuxBasicComplV3.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroup"),
        ("LUM-MUX-MIB", "muxIfGroupV3"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV3.setStatus(
        "deprecated"
    )

lumMuxBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 4)
)
lumMuxBasicComplV4.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroup"),
        ("LUM-MUX-MIB", "muxIfGroupV4"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV4.setStatus(
        "deprecated"
    )

lumMuxBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 5)
)
lumMuxBasicComplV5.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroupV2"),
        ("LUM-MUX-MIB", "muxIfGroupV4"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV5.setStatus(
        "deprecated"
    )

lumMuxBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 6)
)
lumMuxBasicComplV6.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroupV2"),
        ("LUM-MUX-MIB", "muxIfGroupV4"),
        ("LUM-MUX-MIB", "muxVc4Group"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV6.setStatus(
        "deprecated"
    )

lumMuxBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 7)
)
lumMuxBasicComplV7.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroupV2"),
        ("LUM-MUX-MIB", "muxIfGroupV5"),
        ("LUM-MUX-MIB", "muxVc4Group"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV7.setStatus(
        "deprecated"
    )

lumMuxBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 8)
)
lumMuxBasicComplV8.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroupV2"),
        ("LUM-MUX-MIB", "muxIfGroupV5"),
        ("LUM-MUX-MIB", "muxVc4GroupV2"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV8.setStatus(
        "deprecated"
    )

lumMuxBasicComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 9)
)
lumMuxBasicComplV9.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroupV2"),
        ("LUM-MUX-MIB", "muxIfGroupV6"),
        ("LUM-MUX-MIB", "muxVc4GroupV2"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV9.setStatus(
        "deprecated"
    )

lumMuxBasicComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 10)
)
lumMuxBasicComplV10.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroupV2"),
        ("LUM-MUX-MIB", "muxIfGroupV7"),
        ("LUM-MUX-MIB", "muxVc4GroupV2"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV10.setStatus(
        "deprecated"
    )

lumMuxBasicComplV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 11)
)
lumMuxBasicComplV11.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroupV2"),
        ("LUM-MUX-MIB", "muxIfGroupV8"),
        ("LUM-MUX-MIB", "muxVc4GroupV2"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV11.setStatus(
        "deprecated"
    )

lumMuxBasicComplV12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 12)
)
lumMuxBasicComplV12.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroupV2"),
        ("LUM-MUX-MIB", "muxIfGroupV8"),
        ("LUM-MUX-MIB", "muxVc4GroupV3"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV12.setStatus(
        "deprecated"
    )

lumMuxBasicComplV13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 13)
)
lumMuxBasicComplV13.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroupV2"),
        ("LUM-MUX-MIB", "muxIfGroupV8"),
        ("LUM-MUX-MIB", "muxVc4GroupV4"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV13.setStatus(
        "deprecated"
    )

lumMuxBasicComplV14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 14)
)
lumMuxBasicComplV14.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroupV2"),
        ("LUM-MUX-MIB", "muxIfGroupV8"),
        ("LUM-MUX-MIB", "muxVc4GroupV5"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV14.setStatus(
        "deprecated"
    )

lumMuxBasicComplV15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 15)
)
lumMuxBasicComplV15.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroupV2"),
        ("LUM-MUX-MIB", "muxIfGroupV9"),
        ("LUM-MUX-MIB", "muxVc4GroupV5"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV15.setStatus(
        "deprecated"
    )

lumMuxBasicComplV16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 16)
)
lumMuxBasicComplV16.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroupV2"),
        ("LUM-MUX-MIB", "muxIfGroupV10"),
        ("LUM-MUX-MIB", "muxVc4GroupV5"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV16.setStatus(
        "deprecated"
    )

lumMuxBasicComplV17 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 17)
)
lumMuxBasicComplV17.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroupV2"),
        ("LUM-MUX-MIB", "muxIfGroupV11"),
        ("LUM-MUX-MIB", "muxVc4GroupV5"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV17.setStatus(
        "deprecated"
    )

lumMuxBasicComplV18 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 18)
)
lumMuxBasicComplV18.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroupV3"),
        ("LUM-MUX-MIB", "muxIfGroupV11"),
        ("LUM-MUX-MIB", "muxVc4GroupV5"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV18.setStatus(
        "deprecated"
    )

lumMuxBasicComplV19 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 19)
)
lumMuxBasicComplV19.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroupV3"),
        ("LUM-MUX-MIB", "muxIfGroupV12"),
        ("LUM-MUX-MIB", "muxVc4GroupV6"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV19.setStatus(
        "deprecated"
    )

lumMuxBasicComplV20 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 20)
)
lumMuxBasicComplV20.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroupV3"),
        ("LUM-MUX-MIB", "muxIfGroupV12"),
        ("LUM-MUX-MIB", "muxVc4GroupV7"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV20.setStatus(
        "deprecated"
    )

lumMuxBasicComplV21 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 21)
)
lumMuxBasicComplV21.setObjects(
      *(("LUM-MUX-MIB", "muxGeneralGroupV3"),
        ("LUM-MUX-MIB", "muxIfGroupV12"),
        ("LUM-MUX-MIB", "muxVc4GroupV7"))
)
if mibBuilder.loadTexts:
    lumMuxBasicComplV21.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-MUX-MIB",
    **{"MuxTxDirection": MuxTxDirection,
       "lumMuxMIBModule": lumMuxMIBModule,
       "lumMuxConfs": lumMuxConfs,
       "lumMuxGroups": lumMuxGroups,
       "muxGeneralGroup": muxGeneralGroup,
       "muxIfGroup": muxIfGroup,
       "muxIfGroupV2": muxIfGroupV2,
       "muxIfGroupV3": muxIfGroupV3,
       "muxIfGroupV4": muxIfGroupV4,
       "muxGeneralGroupV2": muxGeneralGroupV2,
       "muxVc4Group": muxVc4Group,
       "muxIfGroupV5": muxIfGroupV5,
       "muxVc4GroupV2": muxVc4GroupV2,
       "muxIfGroupV6": muxIfGroupV6,
       "muxIfGroupV7": muxIfGroupV7,
       "muxIfGroupV8": muxIfGroupV8,
       "muxVc4GroupV3": muxVc4GroupV3,
       "muxVc4GroupV4": muxVc4GroupV4,
       "muxVc4GroupV5": muxVc4GroupV5,
       "muxIfGroupV9": muxIfGroupV9,
       "muxIfGroupV10": muxIfGroupV10,
       "muxIfGroupV11": muxIfGroupV11,
       "muxGeneralGroupV3": muxGeneralGroupV3,
       "muxIfGroupV12": muxIfGroupV12,
       "muxVc4GroupV6": muxVc4GroupV6,
       "muxVc4GroupV7": muxVc4GroupV7,
       "lumMuxCompl": lumMuxCompl,
       "lumMuxBasicComplV1": lumMuxBasicComplV1,
       "lumMuxBasicComplV2": lumMuxBasicComplV2,
       "lumMuxBasicComplV3": lumMuxBasicComplV3,
       "lumMuxBasicComplV4": lumMuxBasicComplV4,
       "lumMuxBasicComplV5": lumMuxBasicComplV5,
       "lumMuxBasicComplV6": lumMuxBasicComplV6,
       "lumMuxBasicComplV7": lumMuxBasicComplV7,
       "lumMuxBasicComplV8": lumMuxBasicComplV8,
       "lumMuxBasicComplV9": lumMuxBasicComplV9,
       "lumMuxBasicComplV10": lumMuxBasicComplV10,
       "lumMuxBasicComplV11": lumMuxBasicComplV11,
       "lumMuxBasicComplV12": lumMuxBasicComplV12,
       "lumMuxBasicComplV13": lumMuxBasicComplV13,
       "lumMuxBasicComplV14": lumMuxBasicComplV14,
       "lumMuxBasicComplV15": lumMuxBasicComplV15,
       "lumMuxBasicComplV16": lumMuxBasicComplV16,
       "lumMuxBasicComplV17": lumMuxBasicComplV17,
       "lumMuxBasicComplV18": lumMuxBasicComplV18,
       "lumMuxBasicComplV19": lumMuxBasicComplV19,
       "lumMuxBasicComplV20": lumMuxBasicComplV20,
       "lumMuxBasicComplV21": lumMuxBasicComplV21,
       "lumMuxMIBObjects": lumMuxMIBObjects,
       "muxGeneral": muxGeneral,
       "muxGeneralLastChangeTime": muxGeneralLastChangeTime,
       "muxGeneralStateLastChangeTime": muxGeneralStateLastChangeTime,
       "muxGeneralMuxIfTableSize": muxGeneralMuxIfTableSize,
       "muxGeneralMuxVc4TableSize": muxGeneralMuxVc4TableSize,
       "muxIfList": muxIfList,
       "muxIfTable": muxIfTable,
       "muxIfEntry": muxIfEntry,
       "muxIfIndex": muxIfIndex,
       "muxIfName": muxIfName,
       "muxIfDescr": muxIfDescr,
       "muxIfSubrack": muxIfSubrack,
       "muxIfSlot": muxIfSlot,
       "muxIfTxPort": muxIfTxPort,
       "muxIfRxPort": muxIfRxPort,
       "muxIfInvPhysIndexOrZero": muxIfInvPhysIndexOrZero,
       "muxIfPowerLevel": muxIfPowerLevel,
       "muxIfPowerLevelHighThreshold": muxIfPowerLevelHighThreshold,
       "muxIfPowerLevelLowThreshold": muxIfPowerLevelLowThreshold,
       "muxIfAdminStatus": muxIfAdminStatus,
       "muxIfOperStatus": muxIfOperStatus,
       "muxIfLossOfSignal": muxIfLossOfSignal,
       "muxIfReceivedPowerHigh": muxIfReceivedPowerHigh,
       "muxIfReceivedPowerLow": muxIfReceivedPowerLow,
       "muxIfBitrateMismatch": muxIfBitrateMismatch,
       "muxIfLaserBias": muxIfLaserBias,
       "muxIfLaserBiasThreshold": muxIfLaserBiasThreshold,
       "muxIfJ0PathTrace": muxIfJ0PathTrace,
       "muxIfAlarmIndicationSignal": muxIfAlarmIndicationSignal,
       "muxIfLossOfFrame": muxIfLossOfFrame,
       "muxIfLaserStatus": muxIfLaserStatus,
       "muxIfTxDirection": muxIfTxDirection,
       "muxIfExpectedTxLambda": muxIfExpectedTxLambda,
       "muxIfTxLambda": muxIfTxLambda,
       "muxIfTraceIntrusionMode": muxIfTraceIntrusionMode,
       "muxIfTraceTransmitted": muxIfTraceTransmitted,
       "muxIfTraceReceived": muxIfTraceReceived,
       "muxIfTraceExpected": muxIfTraceExpected,
       "muxIfTraceAlarmMode": muxIfTraceAlarmMode,
       "muxIfTraceMismatch": muxIfTraceMismatch,
       "muxIfOHTransparency": muxIfOHTransparency,
       "muxIfSuppressRemoteAlarms": muxIfSuppressRemoteAlarms,
       "muxIfHighSpeedMin": muxIfHighSpeedMin,
       "muxIfHighSpeedMax": muxIfHighSpeedMax,
       "muxIfTrxCodeMismatch": muxIfTrxCodeMismatch,
       "muxIfTrxBitrateUnavailable": muxIfTrxBitrateUnavailable,
       "muxIfTrxMissing": muxIfTrxMissing,
       "muxIfTrxClass": muxIfTrxClass,
       "muxIfTransmitterFailed": muxIfTransmitterFailed,
       "muxIfUnexpectedFrequency": muxIfUnexpectedFrequency,
       "muxIfIllegalFrequency": muxIfIllegalFrequency,
       "muxIfReceiverSensitivity": muxIfReceiverSensitivity,
       "muxIfPowerLevelLowRelativeThreshold": muxIfPowerLevelLowRelativeThreshold,
       "muxIfObjectProperty": muxIfObjectProperty,
       "muxIfTxPowerLevel": muxIfTxPowerLevel,
       "muxIfLaserTempActual": muxIfLaserTempActual,
       "muxVc4List": muxVc4List,
       "muxVc4Table": muxVc4Table,
       "muxVc4Entry": muxVc4Entry,
       "muxVc4Index": muxVc4Index,
       "muxVc4Name": muxVc4Name,
       "muxVc4Descr": muxVc4Descr,
       "muxVc4Subrack": muxVc4Subrack,
       "muxVc4Slot": muxVc4Slot,
       "muxVc4TxPort": muxVc4TxPort,
       "muxVc4RxPort": muxVc4RxPort,
       "muxVc4Vc4": muxVc4Vc4,
       "muxVc4Mode": muxVc4Mode,
       "muxVc4ClientDropPort": muxVc4ClientDropPort,
       "muxVc4TxDirection": muxVc4TxDirection,
       "muxVc4ClientAddPort": muxVc4ClientAddPort,
       "muxVc4ConnectionMode": muxVc4ConnectionMode,
       "muxVc4ConnectionStatus": muxVc4ConnectionStatus,
       "muxVc4ConnectionOverview": muxVc4ConnectionOverview,
       "muxVc4ObjectProperty": muxVc4ObjectProperty,
       "muxVc4AuAlarmIndicationSignalW2C": muxVc4AuAlarmIndicationSignalW2C,
       "muxVc4AuLossOfPointerW2C": muxVc4AuLossOfPointerW2C,
       "muxVc4RxSignalStatus": muxVc4RxSignalStatus,
       "muxVc4ConcatenationStatus": muxVc4ConcatenationStatus,
       "muxVc4PayloadStatus": muxVc4PayloadStatus,
       "muxVc4AdminStatus": muxVc4AdminStatus}
)
