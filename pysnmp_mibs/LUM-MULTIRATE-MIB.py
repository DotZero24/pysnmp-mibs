# SNMP MIB module (LUM-MULTIRATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-MULTIRATE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:53 2025
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
 lumMultirateMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumMultirateMIB")

(BoardOrInterfaceAdminStatus,
 BoardOrInterfaceOperStatus,
 CommandString,
 FaultStatus,
 LambdaFrequency,
 MgmtNameString,
 ObjectProperty,
 PortNumber,
 SignalFormat,
 SlotNumber,
 SubrackNumber,
 TrxMedia) = mibBuilder.importSymbols(
    "LUM-TC",
    "BoardOrInterfaceAdminStatus",
    "BoardOrInterfaceOperStatus",
    "CommandString",
    "FaultStatus",
    "LambdaFrequency",
    "MgmtNameString",
    "ObjectProperty",
    "PortNumber",
    "SignalFormat",
    "SlotNumber",
    "SubrackNumber",
    "TrxMedia")

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
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

lumMultirateMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 13)
)
if mibBuilder.loadTexts:
    lumMultirateMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-01-11 00:00",
         "2011-04-12 00:00",
         "2007-11-12 00:00",
         "2003-01-29 00:00",
         "2002-12-04 00:00",
         "2002-10-01 00:00",
         "2002-06-04 00:00",
         "2002-05-15 00:00",
         "2002-01-17 00:00",
         "2001-12-03 00:00",
         "2001-11-09 00:00",
         "2001-10-30 00:00",
         "2001-10-22 00:00",
         "2001-10-18 00:00",
         "2001-10-11 00:00",
         "2001-09-05 00:00",
         "2001-08-14 00:00",
         "2001-08-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumMultirateConfs_ObjectIdentity = ObjectIdentity
lumMultirateConfs = _LumMultirateConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1)
)
_LumMultirateGroups_ObjectIdentity = ObjectIdentity
lumMultirateGroups = _LumMultirateGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1)
)
_LumMultirateCompl_ObjectIdentity = ObjectIdentity
lumMultirateCompl = _LumMultirateCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2)
)
_LumMultirateMIBObjects_ObjectIdentity = ObjectIdentity
lumMultirateMIBObjects = _LumMultirateMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2)
)
_MrtGeneral_ObjectIdentity = ObjectIdentity
mrtGeneral = _MrtGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 1)
)


class _MrtGeneralTestAndIncr_Type(TestAndIncr):
    """Custom type mrtGeneralTestAndIncr based on TestAndIncr"""
    defaultValue = 1


_MrtGeneralTestAndIncr_Type.__name__ = "TestAndIncr"
_MrtGeneralTestAndIncr_Object = MibScalar
mrtGeneralTestAndIncr = _MrtGeneralTestAndIncr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 1, 1),
    _MrtGeneralTestAndIncr_Type()
)
mrtGeneralTestAndIncr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtGeneralTestAndIncr.setStatus("current")


class _MrtGeneralMibSpecVersion_Type(DisplayString):
    """Custom type mrtGeneralMibSpecVersion based on DisplayString"""
    defaultValue = OctetString("")


_MrtGeneralMibSpecVersion_Type.__name__ = "DisplayString"
_MrtGeneralMibSpecVersion_Object = MibScalar
mrtGeneralMibSpecVersion = _MrtGeneralMibSpecVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 1, 2),
    _MrtGeneralMibSpecVersion_Type()
)
mrtGeneralMibSpecVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtGeneralMibSpecVersion.setStatus("current")


class _MrtGeneralMibImplVersion_Type(DisplayString):
    """Custom type mrtGeneralMibImplVersion based on DisplayString"""
    defaultValue = OctetString("")


_MrtGeneralMibImplVersion_Type.__name__ = "DisplayString"
_MrtGeneralMibImplVersion_Object = MibScalar
mrtGeneralMibImplVersion = _MrtGeneralMibImplVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 1, 3),
    _MrtGeneralMibImplVersion_Type()
)
mrtGeneralMibImplVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtGeneralMibImplVersion.setStatus("current")
_MrtGeneralLastChangeTime_Type = DateAndTime
_MrtGeneralLastChangeTime_Object = MibScalar
mrtGeneralLastChangeTime = _MrtGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 1, 4),
    _MrtGeneralLastChangeTime_Type()
)
mrtGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtGeneralLastChangeTime.setStatus("current")
_MrtGeneralStateLastChangeTime_Type = DateAndTime
_MrtGeneralStateLastChangeTime_Object = MibScalar
mrtGeneralStateLastChangeTime = _MrtGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 1, 5),
    _MrtGeneralStateLastChangeTime_Type()
)
mrtGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtGeneralStateLastChangeTime.setStatus("current")
_MrtGeneralMrtIfTableSize_Type = Unsigned32
_MrtGeneralMrtIfTableSize_Object = MibScalar
mrtGeneralMrtIfTableSize = _MrtGeneralMrtIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 1, 6),
    _MrtGeneralMrtIfTableSize_Type()
)
mrtGeneralMrtIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtGeneralMrtIfTableSize.setStatus("current")
_MrtIfList_ObjectIdentity = ObjectIdentity
mrtIfList = _MrtIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2)
)
_MrtIfTable_Object = MibTable
mrtIfTable = _MrtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mrtIfTable.setStatus("current")
_MrtIfEntry_Object = MibTableRow
mrtIfEntry = _MrtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1)
)
mrtIfEntry.setIndexNames(
    (0, "LUM-MULTIRATE-MIB", "mrtIfIndex"),
)
if mibBuilder.loadTexts:
    mrtIfEntry.setStatus("current")


class _MrtIfIndex_Type(Unsigned32):
    """Custom type mrtIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MrtIfIndex_Type.__name__ = "Unsigned32"
_MrtIfIndex_Object = MibTableColumn
mrtIfIndex = _MrtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 1),
    _MrtIfIndex_Type()
)
mrtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfIndex.setStatus("current")
_MrtIfName_Type = MgmtNameString
_MrtIfName_Object = MibTableColumn
mrtIfName = _MrtIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 2),
    _MrtIfName_Type()
)
mrtIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfName.setStatus("current")


class _MrtIfDescr_Type(DisplayString):
    """Custom type mrtIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_MrtIfDescr_Type.__name__ = "DisplayString"
_MrtIfDescr_Object = MibTableColumn
mrtIfDescr = _MrtIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 3),
    _MrtIfDescr_Type()
)
mrtIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtIfDescr.setStatus("current")
_MrtIfSubrack_Type = SubrackNumber
_MrtIfSubrack_Object = MibTableColumn
mrtIfSubrack = _MrtIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 4),
    _MrtIfSubrack_Type()
)
mrtIfSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfSubrack.setStatus("current")
_MrtIfSlot_Type = SlotNumber
_MrtIfSlot_Object = MibTableColumn
mrtIfSlot = _MrtIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 5),
    _MrtIfSlot_Type()
)
mrtIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfSlot.setStatus("current")
_MrtIfTxPort_Type = PortNumber
_MrtIfTxPort_Object = MibTableColumn
mrtIfTxPort = _MrtIfTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 6),
    _MrtIfTxPort_Type()
)
mrtIfTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfTxPort.setStatus("current")
_MrtIfRxPort_Type = PortNumber
_MrtIfRxPort_Object = MibTableColumn
mrtIfRxPort = _MrtIfRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 7),
    _MrtIfRxPort_Type()
)
mrtIfRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfRxPort.setStatus("current")


class _MrtIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type mrtIfInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MrtIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_MrtIfInvPhysIndexOrZero_Object = MibTableColumn
mrtIfInvPhysIndexOrZero = _MrtIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 8),
    _MrtIfInvPhysIndexOrZero_Type()
)
mrtIfInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfInvPhysIndexOrZero.setStatus("current")


class _MrtIfFormat_Type(SignalFormat):
    """Custom type mrtIfFormat based on SignalFormat"""
    defaultValue = 4


_MrtIfFormat_Type.__name__ = "SignalFormat"
_MrtIfFormat_Object = MibTableColumn
mrtIfFormat = _MrtIfFormat_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 9),
    _MrtIfFormat_Type()
)
mrtIfFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mrtIfFormat.setStatus("current")


class _MrtIfHighSpeed_Type(Gauge32):
    """Custom type mrtIfHighSpeed based on Gauge32"""
    defaultValue = 2500

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(125, 2500),
    )


_MrtIfHighSpeed_Type.__name__ = "Gauge32"
_MrtIfHighSpeed_Object = MibTableColumn
mrtIfHighSpeed = _MrtIfHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 10),
    _MrtIfHighSpeed_Type()
)
mrtIfHighSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mrtIfHighSpeed.setStatus("current")
_MrtIfHighSpeedMin_Type = Gauge32
_MrtIfHighSpeedMin_Object = MibTableColumn
mrtIfHighSpeedMin = _MrtIfHighSpeedMin_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 11),
    _MrtIfHighSpeedMin_Type()
)
mrtIfHighSpeedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfHighSpeedMin.setStatus("current")
_MrtIfHighSpeedMax_Type = Gauge32
_MrtIfHighSpeedMax_Object = MibTableColumn
mrtIfHighSpeedMax = _MrtIfHighSpeedMax_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 12),
    _MrtIfHighSpeedMax_Type()
)
mrtIfHighSpeedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfHighSpeedMax.setStatus("current")
_MrtIfPowerLevel_Type = Integer32
_MrtIfPowerLevel_Object = MibTableColumn
mrtIfPowerLevel = _MrtIfPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 13),
    _MrtIfPowerLevel_Type()
)
mrtIfPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfPowerLevel.setStatus("current")


class _MrtIfPowerLevelHighThreshold_Type(Integer32):
    """Custom type mrtIfPowerLevelHighThreshold based on Integer32"""
    defaultValue = -80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-280, 0),
    )


_MrtIfPowerLevelHighThreshold_Type.__name__ = "Integer32"
_MrtIfPowerLevelHighThreshold_Object = MibTableColumn
mrtIfPowerLevelHighThreshold = _MrtIfPowerLevelHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 14),
    _MrtIfPowerLevelHighThreshold_Type()
)
mrtIfPowerLevelHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtIfPowerLevelHighThreshold.setStatus("current")


class _MrtIfPowerLevelLowThreshold_Type(Integer32):
    """Custom type mrtIfPowerLevelLowThreshold based on Integer32"""
    defaultValue = -200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-280, 0),
    )


_MrtIfPowerLevelLowThreshold_Type.__name__ = "Integer32"
_MrtIfPowerLevelLowThreshold_Object = MibTableColumn
mrtIfPowerLevelLowThreshold = _MrtIfPowerLevelLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 15),
    _MrtIfPowerLevelLowThreshold_Type()
)
mrtIfPowerLevelLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtIfPowerLevelLowThreshold.setStatus("current")


class _MrtIfLaserStatus_Type(Integer32):
    """Custom type mrtIfLaserStatus based on Integer32"""
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


_MrtIfLaserStatus_Type.__name__ = "Integer32"
_MrtIfLaserStatus_Object = MibTableColumn
mrtIfLaserStatus = _MrtIfLaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 16),
    _MrtIfLaserStatus_Type()
)
mrtIfLaserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfLaserStatus.setStatus("current")


class _MrtIfAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type mrtIfAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_MrtIfAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_MrtIfAdminStatus_Object = MibTableColumn
mrtIfAdminStatus = _MrtIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 17),
    _MrtIfAdminStatus_Type()
)
mrtIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtIfAdminStatus.setStatus("current")


class _MrtIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type mrtIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_MrtIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_MrtIfOperStatus_Object = MibTableColumn
mrtIfOperStatus = _MrtIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 18),
    _MrtIfOperStatus_Type()
)
mrtIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfOperStatus.setStatus("current")
_MrtIfLossOfSignal_Type = FaultStatus
_MrtIfLossOfSignal_Object = MibTableColumn
mrtIfLossOfSignal = _MrtIfLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 19),
    _MrtIfLossOfSignal_Type()
)
mrtIfLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfLossOfSignal.setStatus("current")
_MrtIfReceivedPowerHigh_Type = FaultStatus
_MrtIfReceivedPowerHigh_Object = MibTableColumn
mrtIfReceivedPowerHigh = _MrtIfReceivedPowerHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 20),
    _MrtIfReceivedPowerHigh_Type()
)
mrtIfReceivedPowerHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfReceivedPowerHigh.setStatus("current")
_MrtIfReceivedPowerLow_Type = FaultStatus
_MrtIfReceivedPowerLow_Object = MibTableColumn
mrtIfReceivedPowerLow = _MrtIfReceivedPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 21),
    _MrtIfReceivedPowerLow_Type()
)
mrtIfReceivedPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfReceivedPowerLow.setStatus("current")
_MrtIfLaserBiasHigh_Type = FaultStatus
_MrtIfLaserBiasHigh_Object = MibTableColumn
mrtIfLaserBiasHigh = _MrtIfLaserBiasHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 22),
    _MrtIfLaserBiasHigh_Type()
)
mrtIfLaserBiasHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfLaserBiasHigh.setStatus("current")
_MrtIfErroredSeconds_Type = FaultStatus
_MrtIfErroredSeconds_Object = MibTableColumn
mrtIfErroredSeconds = _MrtIfErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 23),
    _MrtIfErroredSeconds_Type()
)
mrtIfErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfErroredSeconds.setStatus("deprecated")
_MrtIfSeverelyErroredSeconds_Type = FaultStatus
_MrtIfSeverelyErroredSeconds_Object = MibTableColumn
mrtIfSeverelyErroredSeconds = _MrtIfSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 24),
    _MrtIfSeverelyErroredSeconds_Type()
)
mrtIfSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfSeverelyErroredSeconds.setStatus("deprecated")
_MrtIfBackgroundBlockErrors_Type = FaultStatus
_MrtIfBackgroundBlockErrors_Object = MibTableColumn
mrtIfBackgroundBlockErrors = _MrtIfBackgroundBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 25),
    _MrtIfBackgroundBlockErrors_Type()
)
mrtIfBackgroundBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfBackgroundBlockErrors.setStatus("deprecated")
_MrtIfUnavailableSeconds_Type = FaultStatus
_MrtIfUnavailableSeconds_Object = MibTableColumn
mrtIfUnavailableSeconds = _MrtIfUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 26),
    _MrtIfUnavailableSeconds_Type()
)
mrtIfUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfUnavailableSeconds.setStatus("deprecated")
_MrtIfLossOfFrame_Type = FaultStatus
_MrtIfLossOfFrame_Object = MibTableColumn
mrtIfLossOfFrame = _MrtIfLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 27),
    _MrtIfLossOfFrame_Type()
)
mrtIfLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfLossOfFrame.setStatus("current")
_MrtIfMsAlarmIndicationSignalC2W_Type = FaultStatus
_MrtIfMsAlarmIndicationSignalC2W_Object = MibTableColumn
mrtIfMsAlarmIndicationSignalC2W = _MrtIfMsAlarmIndicationSignalC2W_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 28),
    _MrtIfMsAlarmIndicationSignalC2W_Type()
)
mrtIfMsAlarmIndicationSignalC2W.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfMsAlarmIndicationSignalC2W.setStatus("current")
_MrtIfRemoteDefectIndication_Type = FaultStatus
_MrtIfRemoteDefectIndication_Object = MibTableColumn
mrtIfRemoteDefectIndication = _MrtIfRemoteDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 29),
    _MrtIfRemoteDefectIndication_Type()
)
mrtIfRemoteDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfRemoteDefectIndication.setStatus("current")
_MrtIfLossOfSync_Type = FaultStatus
_MrtIfLossOfSync_Object = MibTableColumn
mrtIfLossOfSync = _MrtIfLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 30),
    _MrtIfLossOfSync_Type()
)
mrtIfLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfLossOfSync.setStatus("current")
_MrtIfBitrateMismatch_Type = FaultStatus
_MrtIfBitrateMismatch_Object = MibTableColumn
mrtIfBitrateMismatch = _MrtIfBitrateMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 31),
    _MrtIfBitrateMismatch_Type()
)
mrtIfBitrateMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfBitrateMismatch.setStatus("current")
_MrtIfLaserBias_Type = Unsigned32
_MrtIfLaserBias_Object = MibTableColumn
mrtIfLaserBias = _MrtIfLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 32),
    _MrtIfLaserBias_Type()
)
mrtIfLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfLaserBias.setStatus("current")


class _MrtIfLaserBiasThreshold_Type(Unsigned32):
    """Custom type mrtIfLaserBiasThreshold based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_MrtIfLaserBiasThreshold_Type.__name__ = "Unsigned32"
_MrtIfLaserBiasThreshold_Object = MibTableColumn
mrtIfLaserBiasThreshold = _MrtIfLaserBiasThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 33),
    _MrtIfLaserBiasThreshold_Type()
)
mrtIfLaserBiasThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtIfLaserBiasThreshold.setStatus("current")


class _MrtIfJ0PathTrace_Type(OctetString):
    """Custom type mrtIfJ0PathTrace based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
        ValueSizeConstraint(16, 16),
    )


_MrtIfJ0PathTrace_Type.__name__ = "OctetString"
_MrtIfJ0PathTrace_Object = MibTableColumn
mrtIfJ0PathTrace = _MrtIfJ0PathTrace_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 34),
    _MrtIfJ0PathTrace_Type()
)
mrtIfJ0PathTrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfJ0PathTrace.setStatus("current")
_MrtIfAuAlarmIndicationSignalW2C_Type = FaultStatus
_MrtIfAuAlarmIndicationSignalW2C_Object = MibTableColumn
mrtIfAuAlarmIndicationSignalW2C = _MrtIfAuAlarmIndicationSignalW2C_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 35),
    _MrtIfAuAlarmIndicationSignalW2C_Type()
)
mrtIfAuAlarmIndicationSignalW2C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfAuAlarmIndicationSignalW2C.setStatus("current")
_MrtIfAuLossOfPointerW2C_Type = FaultStatus
_MrtIfAuLossOfPointerW2C_Object = MibTableColumn
mrtIfAuLossOfPointerW2C = _MrtIfAuLossOfPointerW2C_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 36),
    _MrtIfAuLossOfPointerW2C_Type()
)
mrtIfAuLossOfPointerW2C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfAuLossOfPointerW2C.setStatus("current")


class _MrtIfTxSignalStatus_Type(Integer32):
    """Custom type mrtIfTxSignalStatus based on Integer32"""
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


_MrtIfTxSignalStatus_Type.__name__ = "Integer32"
_MrtIfTxSignalStatus_Object = MibTableColumn
mrtIfTxSignalStatus = _MrtIfTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 37),
    _MrtIfTxSignalStatus_Type()
)
mrtIfTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfTxSignalStatus.setStatus("current")


class _MrtIfTruncVc4_Type(Unsigned32):
    """Custom type mrtIfTruncVc4 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MrtIfTruncVc4_Type.__name__ = "Unsigned32"
_MrtIfTruncVc4_Object = MibTableColumn
mrtIfTruncVc4 = _MrtIfTruncVc4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 38),
    _MrtIfTruncVc4_Type()
)
mrtIfTruncVc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtIfTruncVc4.setStatus("current")
_MrtIfAuAlarmIndicationSignalC2W_Type = FaultStatus
_MrtIfAuAlarmIndicationSignalC2W_Object = MibTableColumn
mrtIfAuAlarmIndicationSignalC2W = _MrtIfAuAlarmIndicationSignalC2W_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 39),
    _MrtIfAuAlarmIndicationSignalC2W_Type()
)
mrtIfAuAlarmIndicationSignalC2W.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfAuAlarmIndicationSignalC2W.setStatus("current")
_MrtIfAuLossOfPointerC2W_Type = FaultStatus
_MrtIfAuLossOfPointerC2W_Object = MibTableColumn
mrtIfAuLossOfPointerC2W = _MrtIfAuLossOfPointerC2W_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 40),
    _MrtIfAuLossOfPointerC2W_Type()
)
mrtIfAuLossOfPointerC2W.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfAuLossOfPointerC2W.setStatus("current")


class _MrtIfTraceIntrusionMode_Type(Integer32):
    """Custom type mrtIfTraceIntrusionMode based on Integer32"""
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


_MrtIfTraceIntrusionMode_Type.__name__ = "Integer32"
_MrtIfTraceIntrusionMode_Object = MibTableColumn
mrtIfTraceIntrusionMode = _MrtIfTraceIntrusionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 41),
    _MrtIfTraceIntrusionMode_Type()
)
mrtIfTraceIntrusionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtIfTraceIntrusionMode.setStatus("current")


class _MrtIfTraceTransmitted_Type(DisplayString):
    """Custom type mrtIfTraceTransmitted based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MrtIfTraceTransmitted_Type.__name__ = "DisplayString"
_MrtIfTraceTransmitted_Object = MibTableColumn
mrtIfTraceTransmitted = _MrtIfTraceTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 42),
    _MrtIfTraceTransmitted_Type()
)
mrtIfTraceTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtIfTraceTransmitted.setStatus("current")


class _MrtIfTraceReceived_Type(DisplayString):
    """Custom type mrtIfTraceReceived based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MrtIfTraceReceived_Type.__name__ = "DisplayString"
_MrtIfTraceReceived_Object = MibTableColumn
mrtIfTraceReceived = _MrtIfTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 43),
    _MrtIfTraceReceived_Type()
)
mrtIfTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfTraceReceived.setStatus("current")


class _MrtIfTraceExpected_Type(DisplayString):
    """Custom type mrtIfTraceExpected based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MrtIfTraceExpected_Type.__name__ = "DisplayString"
_MrtIfTraceExpected_Object = MibTableColumn
mrtIfTraceExpected = _MrtIfTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 44),
    _MrtIfTraceExpected_Type()
)
mrtIfTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtIfTraceExpected.setStatus("current")


class _MrtIfTraceAlarmMode_Type(Integer32):
    """Custom type mrtIfTraceAlarmMode based on Integer32"""
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


_MrtIfTraceAlarmMode_Type.__name__ = "Integer32"
_MrtIfTraceAlarmMode_Object = MibTableColumn
mrtIfTraceAlarmMode = _MrtIfTraceAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 45),
    _MrtIfTraceAlarmMode_Type()
)
mrtIfTraceAlarmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtIfTraceAlarmMode.setStatus("current")
_MrtIfTraceMismatch_Type = FaultStatus
_MrtIfTraceMismatch_Object = MibTableColumn
mrtIfTraceMismatch = _MrtIfTraceMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 46),
    _MrtIfTraceMismatch_Type()
)
mrtIfTraceMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfTraceMismatch.setStatus("current")


class _MrtIfTruncVc4Status_Type(Integer32):
    """Custom type mrtIfTruncVc4Status based on Integer32"""
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
        *(("undefined", 0),
          ("addDrop", 1),
          ("passThrough", 2),
          ("unconnected", 3))
    )


_MrtIfTruncVc4Status_Type.__name__ = "Integer32"
_MrtIfTruncVc4Status_Object = MibTableColumn
mrtIfTruncVc4Status = _MrtIfTruncVc4Status_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 47),
    _MrtIfTruncVc4Status_Type()
)
mrtIfTruncVc4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfTruncVc4Status.setStatus("deprecated")
_MrtIfMsAlarmIndicationSignalW2C_Type = FaultStatus
_MrtIfMsAlarmIndicationSignalW2C_Object = MibTableColumn
mrtIfMsAlarmIndicationSignalW2C = _MrtIfMsAlarmIndicationSignalW2C_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 48),
    _MrtIfMsAlarmIndicationSignalW2C_Type()
)
mrtIfMsAlarmIndicationSignalW2C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfMsAlarmIndicationSignalW2C.setStatus("current")


class _MrtIfForwardAls_Type(Integer32):
    """Custom type mrtIfForwardAls based on Integer32"""
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


_MrtIfForwardAls_Type.__name__ = "Integer32"
_MrtIfForwardAls_Object = MibTableColumn
mrtIfForwardAls = _MrtIfForwardAls_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 49),
    _MrtIfForwardAls_Type()
)
mrtIfForwardAls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtIfForwardAls.setStatus("current")


class _MrtIfSuppressRemoteAlarms_Type(Integer32):
    """Custom type mrtIfSuppressRemoteAlarms based on Integer32"""
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


_MrtIfSuppressRemoteAlarms_Type.__name__ = "Integer32"
_MrtIfSuppressRemoteAlarms_Object = MibTableColumn
mrtIfSuppressRemoteAlarms = _MrtIfSuppressRemoteAlarms_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 50),
    _MrtIfSuppressRemoteAlarms_Type()
)
mrtIfSuppressRemoteAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtIfSuppressRemoteAlarms.setStatus("current")
_MrtIfConfigurationCommand_Type = CommandString
_MrtIfConfigurationCommand_Object = MibTableColumn
mrtIfConfigurationCommand = _MrtIfConfigurationCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 51),
    _MrtIfConfigurationCommand_Type()
)
mrtIfConfigurationCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfConfigurationCommand.setStatus("current")
_MrtIfTrxCodeMismatch_Type = FaultStatus
_MrtIfTrxCodeMismatch_Object = MibTableColumn
mrtIfTrxCodeMismatch = _MrtIfTrxCodeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 52),
    _MrtIfTrxCodeMismatch_Type()
)
mrtIfTrxCodeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfTrxCodeMismatch.setStatus("current")
_MrtIfTrxBitrateUnavailable_Type = FaultStatus
_MrtIfTrxBitrateUnavailable_Object = MibTableColumn
mrtIfTrxBitrateUnavailable = _MrtIfTrxBitrateUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 53),
    _MrtIfTrxBitrateUnavailable_Type()
)
mrtIfTrxBitrateUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfTrxBitrateUnavailable.setStatus("current")
_MrtIfTrxMissing_Type = FaultStatus
_MrtIfTrxMissing_Object = MibTableColumn
mrtIfTrxMissing = _MrtIfTrxMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 54),
    _MrtIfTrxMissing_Type()
)
mrtIfTrxMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfTrxMissing.setStatus("current")


class _MrtIfTrxClass_Type(DisplayString):
    """Custom type mrtIfTrxClass based on DisplayString"""
    defaultValue = OctetString("")


_MrtIfTrxClass_Type.__name__ = "DisplayString"
_MrtIfTrxClass_Object = MibTableColumn
mrtIfTrxClass = _MrtIfTrxClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 55),
    _MrtIfTrxClass_Type()
)
mrtIfTrxClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfTrxClass.setStatus("current")


class _MrtIfEntityId_Type(Unsigned32):
    """Custom type mrtIfEntityId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MrtIfEntityId_Type.__name__ = "Unsigned32"
_MrtIfEntityId_Object = MibTableColumn
mrtIfEntityId = _MrtIfEntityId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 56),
    _MrtIfEntityId_Type()
)
mrtIfEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfEntityId.setStatus("current")
_MrtIfTransmitterFailed_Type = FaultStatus
_MrtIfTransmitterFailed_Object = MibTableColumn
mrtIfTransmitterFailed = _MrtIfTransmitterFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 57),
    _MrtIfTransmitterFailed_Type()
)
mrtIfTransmitterFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfTransmitterFailed.setStatus("current")
_MrtIfReceiverSensitivity_Type = Integer32
_MrtIfReceiverSensitivity_Object = MibTableColumn
mrtIfReceiverSensitivity = _MrtIfReceiverSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 58),
    _MrtIfReceiverSensitivity_Type()
)
mrtIfReceiverSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfReceiverSensitivity.setStatus("current")


class _MrtIfPowerLevelLowRelativeThreshold_Type(Integer32):
    """Custom type mrtIfPowerLevelLowRelativeThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_MrtIfPowerLevelLowRelativeThreshold_Type.__name__ = "Integer32"
_MrtIfPowerLevelLowRelativeThreshold_Object = MibTableColumn
mrtIfPowerLevelLowRelativeThreshold = _MrtIfPowerLevelLowRelativeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 59),
    _MrtIfPowerLevelLowRelativeThreshold_Type()
)
mrtIfPowerLevelLowRelativeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtIfPowerLevelLowRelativeThreshold.setStatus("current")


class _MrtIfFarEndLoopback_Type(Integer32):
    """Custom type mrtIfFarEndLoopback based on Integer32"""
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


_MrtIfFarEndLoopback_Type.__name__ = "Integer32"
_MrtIfFarEndLoopback_Object = MibTableColumn
mrtIfFarEndLoopback = _MrtIfFarEndLoopback_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 60),
    _MrtIfFarEndLoopback_Type()
)
mrtIfFarEndLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtIfFarEndLoopback.setStatus("current")
_MrtIfConfigureModeCommand_Type = CommandString
_MrtIfConfigureModeCommand_Object = MibTableColumn
mrtIfConfigureModeCommand = _MrtIfConfigureModeCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 61),
    _MrtIfConfigureModeCommand_Type()
)
mrtIfConfigureModeCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfConfigureModeCommand.setStatus("current")


class _MrtIfTrxMode_Type(Integer32):
    """Custom type mrtIfTrxMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("line", 2))
    )


_MrtIfTrxMode_Type.__name__ = "Integer32"
_MrtIfTrxMode_Object = MibTableColumn
mrtIfTrxMode = _MrtIfTrxMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 62),
    _MrtIfTrxMode_Type()
)
mrtIfTrxMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mrtIfTrxMode.setStatus("current")


class _MrtIfExpectedTxFrequency_Type(LambdaFrequency):
    """Custom type mrtIfExpectedTxFrequency based on LambdaFrequency"""
    defaultValue = 0


_MrtIfExpectedTxFrequency_Type.__name__ = "LambdaFrequency"
_MrtIfExpectedTxFrequency_Object = MibTableColumn
mrtIfExpectedTxFrequency = _MrtIfExpectedTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 63),
    _MrtIfExpectedTxFrequency_Type()
)
mrtIfExpectedTxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtIfExpectedTxFrequency.setStatus("current")
_MrtIfTxFrequency_Type = LambdaFrequency
_MrtIfTxFrequency_Object = MibTableColumn
mrtIfTxFrequency = _MrtIfTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 64),
    _MrtIfTxFrequency_Type()
)
mrtIfTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfTxFrequency.setStatus("current")
_MrtIfUnexpectedTxFrequency_Type = FaultStatus
_MrtIfUnexpectedTxFrequency_Object = MibTableColumn
mrtIfUnexpectedTxFrequency = _MrtIfUnexpectedTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 65),
    _MrtIfUnexpectedTxFrequency_Type()
)
mrtIfUnexpectedTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfUnexpectedTxFrequency.setStatus("current")
_MrtIfIllegalFrequency_Type = FaultStatus
_MrtIfIllegalFrequency_Object = MibTableColumn
mrtIfIllegalFrequency = _MrtIfIllegalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 66),
    _MrtIfIllegalFrequency_Type()
)
mrtIfIllegalFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfIllegalFrequency.setStatus("current")


class _MrtIfTrxMedia_Type(TrxMedia):
    """Custom type mrtIfTrxMedia based on TrxMedia"""
    defaultValue = 1


_MrtIfTrxMedia_Type.__name__ = "TrxMedia"
_MrtIfTrxMedia_Object = MibTableColumn
mrtIfTrxMedia = _MrtIfTrxMedia_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 67),
    _MrtIfTrxMedia_Type()
)
mrtIfTrxMedia.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mrtIfTrxMedia.setStatus("current")
_MrtIfTrxMediaMismatch_Type = FaultStatus
_MrtIfTrxMediaMismatch_Object = MibTableColumn
mrtIfTrxMediaMismatch = _MrtIfTrxMediaMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 68),
    _MrtIfTrxMediaMismatch_Type()
)
mrtIfTrxMediaMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfTrxMediaMismatch.setStatus("current")


class _MrtIfLaserForcedOn_Type(Integer32):
    """Custom type mrtIfLaserForcedOn based on Integer32"""
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


_MrtIfLaserForcedOn_Type.__name__ = "Integer32"
_MrtIfLaserForcedOn_Object = MibTableColumn
mrtIfLaserForcedOn = _MrtIfLaserForcedOn_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 69),
    _MrtIfLaserForcedOn_Type()
)
mrtIfLaserForcedOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtIfLaserForcedOn.setStatus("current")


class _MrtIfTruncAutoNegotiationMode_Type(Integer32):
    """Custom type mrtIfTruncAutoNegotiationMode based on Integer32"""
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


_MrtIfTruncAutoNegotiationMode_Type.__name__ = "Integer32"
_MrtIfTruncAutoNegotiationMode_Object = MibTableColumn
mrtIfTruncAutoNegotiationMode = _MrtIfTruncAutoNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 70),
    _MrtIfTruncAutoNegotiationMode_Type()
)
mrtIfTruncAutoNegotiationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtIfTruncAutoNegotiationMode.setStatus("current")
_MrtIfObjectProperty_Type = ObjectProperty
_MrtIfObjectProperty_Object = MibTableColumn
mrtIfObjectProperty = _MrtIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 71),
    _MrtIfObjectProperty_Type()
)
mrtIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfObjectProperty.setStatus("current")
_MrtIfTxPowerLevel_Type = Integer32
_MrtIfTxPowerLevel_Object = MibTableColumn
mrtIfTxPowerLevel = _MrtIfTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 72),
    _MrtIfTxPowerLevel_Type()
)
mrtIfTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfTxPowerLevel.setStatus("current")
_MrtIfLaserTempActual_Type = Integer32
_MrtIfLaserTempActual_Object = MibTableColumn
mrtIfLaserTempActual = _MrtIfLaserTempActual_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 73),
    _MrtIfLaserTempActual_Type()
)
mrtIfLaserTempActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfLaserTempActual.setStatus("current")


class _MrtIfHighSpeed2_Type(Gauge32):
    """Custom type mrtIfHighSpeed2 based on Gauge32"""
    defaultValue = 250000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12500, 250000),
    )


_MrtIfHighSpeed2_Type.__name__ = "Gauge32"
_MrtIfHighSpeed2_Object = MibTableColumn
mrtIfHighSpeed2 = _MrtIfHighSpeed2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 74),
    _MrtIfHighSpeed2_Type()
)
mrtIfHighSpeed2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrtIfHighSpeed2.setStatus("current")


class _MrtIfRxSignalStatus_Type(Integer32):
    """Custom type mrtIfRxSignalStatus based on Integer32"""
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


_MrtIfRxSignalStatus_Type.__name__ = "Integer32"
_MrtIfRxSignalStatus_Object = MibTableColumn
mrtIfRxSignalStatus = _MrtIfRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 2, 1, 1, 75),
    _MrtIfRxSignalStatus_Type()
)
mrtIfRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrtIfRxSignalStatus.setStatus("current")
_LumentisMrtNotifications_ObjectIdentity = ObjectIdentity
lumentisMrtNotifications = _LumentisMrtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 3)
)
_MrtNotifyPrefix_ObjectIdentity = ObjectIdentity
mrtNotifyPrefix = _MrtNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 3, 0)
)

# Managed Objects groups

mrtGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 1)
)
mrtGeneralGroup.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralTestAndIncr"),
        ("LUM-MULTIRATE-MIB", "mrtGeneralMibSpecVersion"),
        ("LUM-MULTIRATE-MIB", "mrtGeneralMibImplVersion"),
        ("LUM-MULTIRATE-MIB", "mrtGeneralLastChangeTime"))
)
if mibBuilder.loadTexts:
    mrtGeneralGroup.setStatus("deprecated")

mrtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 2)
)
mrtIfGroup.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfDescr"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfInvPhysIndexOrZero"),
        ("LUM-MULTIRATE-MIB", "mrtIfFormat"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeed"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMin"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMax"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelHighThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfAdminStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfOperStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSignal"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerLow"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfErroredSeconds"),
        ("LUM-MULTIRATE-MIB", "mrtIfSeverelyErroredSeconds"),
        ("LUM-MULTIRATE-MIB", "mrtIfBackgroundBlockErrors"),
        ("LUM-MULTIRATE-MIB", "mrtIfUnavailableSeconds"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfFrame"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfRemoteDefectIndication"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSync"),
        ("LUM-MULTIRATE-MIB", "mrtIfBitrateMismatch"))
)
if mibBuilder.loadTexts:
    mrtIfGroup.setStatus("deprecated")

mrtGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 3)
)
mrtGeneralGroupV2.setObjects(
    ("LUM-MULTIRATE-MIB", "mrtGeneralLastChangeTime")
)
if mibBuilder.loadTexts:
    mrtGeneralGroupV2.setStatus("deprecated")

mrtIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 4)
)
mrtIfGroupV2.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfDescr"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfInvPhysIndexOrZero"),
        ("LUM-MULTIRATE-MIB", "mrtIfFormat"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeed"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMin"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMax"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelHighThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfAdminStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfOperStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSignal"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerLow"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfErroredSeconds"),
        ("LUM-MULTIRATE-MIB", "mrtIfSeverelyErroredSeconds"),
        ("LUM-MULTIRATE-MIB", "mrtIfBackgroundBlockErrors"),
        ("LUM-MULTIRATE-MIB", "mrtIfUnavailableSeconds"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfFrame"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfRemoteDefectIndication"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSync"),
        ("LUM-MULTIRATE-MIB", "mrtIfBitrateMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBias"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfJ0PathTrace"))
)
if mibBuilder.loadTexts:
    mrtIfGroupV2.setStatus("deprecated")

mrtIfGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 5)
)
mrtIfGroupV3.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfDescr"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfInvPhysIndexOrZero"),
        ("LUM-MULTIRATE-MIB", "mrtIfFormat"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeed"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMin"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMax"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelHighThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfAdminStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfOperStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSignal"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerLow"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfErroredSeconds"),
        ("LUM-MULTIRATE-MIB", "mrtIfSeverelyErroredSeconds"),
        ("LUM-MULTIRATE-MIB", "mrtIfBackgroundBlockErrors"),
        ("LUM-MULTIRATE-MIB", "mrtIfUnavailableSeconds"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfFrame"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfRemoteDefectIndication"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSync"),
        ("LUM-MULTIRATE-MIB", "mrtIfBitrateMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBias"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfJ0PathTrace"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerW2C"))
)
if mibBuilder.loadTexts:
    mrtIfGroupV3.setStatus("deprecated")

mrtIfGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 6)
)
mrtIfGroupV4.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfDescr"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfInvPhysIndexOrZero"),
        ("LUM-MULTIRATE-MIB", "mrtIfFormat"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeed"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMin"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMax"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelHighThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfAdminStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfOperStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSignal"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerLow"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfFrame"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfRemoteDefectIndication"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSync"),
        ("LUM-MULTIRATE-MIB", "mrtIfBitrateMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBias"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfJ0PathTrace"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatus"))
)
if mibBuilder.loadTexts:
    mrtIfGroupV4.setStatus("deprecated")

mrtGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 8)
)
mrtGeneralGroupV3.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralLastChangeTime"),
        ("LUM-MULTIRATE-MIB", "mrtGeneralStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    mrtGeneralGroupV3.setStatus("deprecated")

mrtIfGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 9)
)
mrtIfGroupV5.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfDescr"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfInvPhysIndexOrZero"),
        ("LUM-MULTIRATE-MIB", "mrtIfFormat"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeed"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMin"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMax"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelHighThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfAdminStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfOperStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSignal"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerLow"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfFrame"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfRemoteDefectIndication"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSync"),
        ("LUM-MULTIRATE-MIB", "mrtIfBitrateMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBias"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfJ0PathTrace"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfTruncVc4"))
)
if mibBuilder.loadTexts:
    mrtIfGroupV5.setStatus("deprecated")

mrtIfGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 10)
)
mrtIfGroupV6.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfDescr"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfInvPhysIndexOrZero"),
        ("LUM-MULTIRATE-MIB", "mrtIfFormat"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeed"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMin"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMax"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelHighThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfAdminStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfOperStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSignal"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerLow"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfFrame"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfRemoteDefectIndication"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSync"),
        ("LUM-MULTIRATE-MIB", "mrtIfBitrateMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBias"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfJ0PathTrace"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfTruncVc4"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerC2W"))
)
if mibBuilder.loadTexts:
    mrtIfGroupV6.setStatus("current")

mrtIfGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 11)
)
mrtIfGroupV7.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfDescr"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfInvPhysIndexOrZero"),
        ("LUM-MULTIRATE-MIB", "mrtIfFormat"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeed"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMin"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMax"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelHighThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfAdminStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfOperStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSignal"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerLow"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfFrame"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfRemoteDefectIndication"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSync"),
        ("LUM-MULTIRATE-MIB", "mrtIfBitrateMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBias"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfJ0PathTrace"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfTruncVc4"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceIntrusionMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceTransmitted"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceReceived"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceExpected"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceAlarmMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceMismatch"))
)
if mibBuilder.loadTexts:
    mrtIfGroupV7.setStatus("deprecated")

mrtIfGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 12)
)
mrtIfGroupV8.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfDescr"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfInvPhysIndexOrZero"),
        ("LUM-MULTIRATE-MIB", "mrtIfFormat"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeed"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMin"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMax"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelHighThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfAdminStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfOperStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSignal"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerLow"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfFrame"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfRemoteDefectIndication"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSync"),
        ("LUM-MULTIRATE-MIB", "mrtIfBitrateMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBias"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfJ0PathTrace"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfTruncVc4"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceIntrusionMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceTransmitted"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceReceived"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceExpected"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceAlarmMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfTruncVc4Status"))
)
if mibBuilder.loadTexts:
    mrtIfGroupV8.setStatus("deprecated")

mrtIfGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 13)
)
mrtIfGroupV9.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfDescr"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfInvPhysIndexOrZero"),
        ("LUM-MULTIRATE-MIB", "mrtIfFormat"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeed"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMin"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMax"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelHighThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfAdminStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfOperStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSignal"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerLow"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfFrame"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfRemoteDefectIndication"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSync"),
        ("LUM-MULTIRATE-MIB", "mrtIfBitrateMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBias"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfJ0PathTrace"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfTruncVc4"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceIntrusionMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceTransmitted"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceReceived"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceExpected"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceAlarmMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceMismatch"))
)
if mibBuilder.loadTexts:
    mrtIfGroupV9.setStatus("deprecated")

mrtIfGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 14)
)
mrtIfGroupV10.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfDescr"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfInvPhysIndexOrZero"),
        ("LUM-MULTIRATE-MIB", "mrtIfFormat"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeed"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMin"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMax"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelHighThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfAdminStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfOperStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSignal"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerLow"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfFrame"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfRemoteDefectIndication"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSync"),
        ("LUM-MULTIRATE-MIB", "mrtIfBitrateMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBias"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfJ0PathTrace"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfTruncVc4"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceIntrusionMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceTransmitted"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceReceived"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceExpected"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceAlarmMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfForwardAls"),
        ("LUM-MULTIRATE-MIB", "mrtIfSuppressRemoteAlarms"),
        ("LUM-MULTIRATE-MIB", "mrtIfConfigurationCommand"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxCodeMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxBitrateUnavailable"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMissing"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxClass"),
        ("LUM-MULTIRATE-MIB", "mrtIfEntityId"),
        ("LUM-MULTIRATE-MIB", "mrtIfTransmitterFailed"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceiverSensitivity"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowRelativeThreshold"))
)
if mibBuilder.loadTexts:
    mrtIfGroupV10.setStatus("deprecated")

mrtIfGroupV11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 16)
)
mrtIfGroupV11.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfDescr"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfInvPhysIndexOrZero"),
        ("LUM-MULTIRATE-MIB", "mrtIfFormat"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeed"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMin"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMax"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelHighThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfAdminStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfOperStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSignal"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerLow"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfFrame"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfRemoteDefectIndication"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSync"),
        ("LUM-MULTIRATE-MIB", "mrtIfBitrateMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBias"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfJ0PathTrace"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfTruncVc4"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceIntrusionMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceTransmitted"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceReceived"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceExpected"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceAlarmMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfForwardAls"),
        ("LUM-MULTIRATE-MIB", "mrtIfSuppressRemoteAlarms"),
        ("LUM-MULTIRATE-MIB", "mrtIfConfigurationCommand"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxCodeMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxBitrateUnavailable"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMissing"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxClass"),
        ("LUM-MULTIRATE-MIB", "mrtIfEntityId"),
        ("LUM-MULTIRATE-MIB", "mrtIfTransmitterFailed"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceiverSensitivity"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowRelativeThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfFarEndLoopback"),
        ("LUM-MULTIRATE-MIB", "mrtIfConfigureModeCommand"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfExpectedTxFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfUnexpectedTxFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfIllegalFrequency"))
)
if mibBuilder.loadTexts:
    mrtIfGroupV11.setStatus("deprecated")

mrtIfGroupV12 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 17)
)
mrtIfGroupV12.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfDescr"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfInvPhysIndexOrZero"),
        ("LUM-MULTIRATE-MIB", "mrtIfFormat"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeed"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMin"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMax"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelHighThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfAdminStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfOperStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSignal"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerLow"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfFrame"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfRemoteDefectIndication"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSync"),
        ("LUM-MULTIRATE-MIB", "mrtIfBitrateMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBias"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfJ0PathTrace"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfTruncVc4"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceIntrusionMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceTransmitted"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceReceived"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceExpected"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceAlarmMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfForwardAls"),
        ("LUM-MULTIRATE-MIB", "mrtIfSuppressRemoteAlarms"),
        ("LUM-MULTIRATE-MIB", "mrtIfConfigurationCommand"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxCodeMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxBitrateUnavailable"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMissing"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxClass"),
        ("LUM-MULTIRATE-MIB", "mrtIfEntityId"),
        ("LUM-MULTIRATE-MIB", "mrtIfTransmitterFailed"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceiverSensitivity"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowRelativeThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfFarEndLoopback"),
        ("LUM-MULTIRATE-MIB", "mrtIfConfigureModeCommand"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfExpectedTxFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfUnexpectedTxFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfIllegalFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMedia"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMediaMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserForcedOn"))
)
if mibBuilder.loadTexts:
    mrtIfGroupV12.setStatus("deprecated")

mrtGeneralGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 18)
)
mrtGeneralGroupV4.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralLastChangeTime"),
        ("LUM-MULTIRATE-MIB", "mrtGeneralStateLastChangeTime"),
        ("LUM-MULTIRATE-MIB", "mrtGeneralMrtIfTableSize"))
)
if mibBuilder.loadTexts:
    mrtGeneralGroupV4.setStatus("current")

mrtIfGroupV13 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 19)
)
mrtIfGroupV13.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfDescr"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfInvPhysIndexOrZero"),
        ("LUM-MULTIRATE-MIB", "mrtIfFormat"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeed"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMin"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMax"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelHighThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfAdminStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfOperStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSignal"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerLow"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfFrame"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfRemoteDefectIndication"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSync"),
        ("LUM-MULTIRATE-MIB", "mrtIfBitrateMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBias"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfJ0PathTrace"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfTruncVc4"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceIntrusionMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceTransmitted"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceReceived"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceExpected"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceAlarmMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfForwardAls"),
        ("LUM-MULTIRATE-MIB", "mrtIfSuppressRemoteAlarms"),
        ("LUM-MULTIRATE-MIB", "mrtIfConfigurationCommand"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxCodeMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxBitrateUnavailable"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMissing"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxClass"),
        ("LUM-MULTIRATE-MIB", "mrtIfEntityId"),
        ("LUM-MULTIRATE-MIB", "mrtIfTransmitterFailed"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceiverSensitivity"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowRelativeThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfFarEndLoopback"),
        ("LUM-MULTIRATE-MIB", "mrtIfConfigureModeCommand"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfExpectedTxFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfUnexpectedTxFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfIllegalFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMedia"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMediaMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserForcedOn"),
        ("LUM-MULTIRATE-MIB", "mrtIfTruncAutoNegotiationMode"))
)
if mibBuilder.loadTexts:
    mrtIfGroupV13.setStatus("deprecated")

mrtIfGroupV14 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 20)
)
mrtIfGroupV14.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfDescr"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfInvPhysIndexOrZero"),
        ("LUM-MULTIRATE-MIB", "mrtIfFormat"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeed"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMin"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMax"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelHighThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfAdminStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfOperStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSignal"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerLow"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfFrame"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfRemoteDefectIndication"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSync"),
        ("LUM-MULTIRATE-MIB", "mrtIfBitrateMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBias"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfJ0PathTrace"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfTruncVc4"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceIntrusionMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceTransmitted"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceReceived"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceExpected"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceAlarmMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfForwardAls"),
        ("LUM-MULTIRATE-MIB", "mrtIfSuppressRemoteAlarms"),
        ("LUM-MULTIRATE-MIB", "mrtIfConfigurationCommand"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxCodeMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxBitrateUnavailable"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMissing"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxClass"),
        ("LUM-MULTIRATE-MIB", "mrtIfEntityId"),
        ("LUM-MULTIRATE-MIB", "mrtIfTransmitterFailed"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceiverSensitivity"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowRelativeThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfFarEndLoopback"),
        ("LUM-MULTIRATE-MIB", "mrtIfConfigureModeCommand"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfExpectedTxFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfUnexpectedTxFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfIllegalFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMedia"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMediaMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserForcedOn"),
        ("LUM-MULTIRATE-MIB", "mrtIfTruncAutoNegotiationMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfObjectProperty"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserTempActual"))
)
if mibBuilder.loadTexts:
    mrtIfGroupV14.setStatus("deprecated")

mrtIfGroupV15 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 21)
)
mrtIfGroupV15.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfDescr"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfInvPhysIndexOrZero"),
        ("LUM-MULTIRATE-MIB", "mrtIfFormat"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeed"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMin"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMax"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelHighThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfAdminStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfOperStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSignal"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerLow"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfFrame"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfRemoteDefectIndication"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSync"),
        ("LUM-MULTIRATE-MIB", "mrtIfBitrateMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBias"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfJ0PathTrace"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfTruncVc4"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceIntrusionMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceTransmitted"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceReceived"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceExpected"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceAlarmMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfForwardAls"),
        ("LUM-MULTIRATE-MIB", "mrtIfSuppressRemoteAlarms"),
        ("LUM-MULTIRATE-MIB", "mrtIfConfigurationCommand"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxCodeMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxBitrateUnavailable"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMissing"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxClass"),
        ("LUM-MULTIRATE-MIB", "mrtIfEntityId"),
        ("LUM-MULTIRATE-MIB", "mrtIfTransmitterFailed"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceiverSensitivity"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowRelativeThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfFarEndLoopback"),
        ("LUM-MULTIRATE-MIB", "mrtIfConfigureModeCommand"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfExpectedTxFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfUnexpectedTxFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfIllegalFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMedia"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMediaMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserForcedOn"),
        ("LUM-MULTIRATE-MIB", "mrtIfTruncAutoNegotiationMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfObjectProperty"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserTempActual"))
)
if mibBuilder.loadTexts:
    mrtIfGroupV15.setStatus("deprecated")

mrtIfGroupV16 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 22)
)
mrtIfGroupV16.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfDescr"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfInvPhysIndexOrZero"),
        ("LUM-MULTIRATE-MIB", "mrtIfFormat"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeed"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMin"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeedMax"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelHighThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfAdminStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfOperStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSignal"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceivedPowerLow"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasHigh"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfFrame"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfMsAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfRemoteDefectIndication"),
        ("LUM-MULTIRATE-MIB", "mrtIfLossOfSync"),
        ("LUM-MULTIRATE-MIB", "mrtIfBitrateMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBias"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserBiasThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfJ0PathTrace"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerW2C"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatus"),
        ("LUM-MULTIRATE-MIB", "mrtIfTruncVc4"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuAlarmIndicationSignalC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfAuLossOfPointerC2W"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceIntrusionMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceTransmitted"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceReceived"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceExpected"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceAlarmMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfTraceMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfForwardAls"),
        ("LUM-MULTIRATE-MIB", "mrtIfSuppressRemoteAlarms"),
        ("LUM-MULTIRATE-MIB", "mrtIfConfigurationCommand"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxCodeMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxBitrateUnavailable"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMissing"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxClass"),
        ("LUM-MULTIRATE-MIB", "mrtIfEntityId"),
        ("LUM-MULTIRATE-MIB", "mrtIfTransmitterFailed"),
        ("LUM-MULTIRATE-MIB", "mrtIfReceiverSensitivity"),
        ("LUM-MULTIRATE-MIB", "mrtIfPowerLevelLowRelativeThreshold"),
        ("LUM-MULTIRATE-MIB", "mrtIfFarEndLoopback"),
        ("LUM-MULTIRATE-MIB", "mrtIfConfigureModeCommand"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfExpectedTxFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfUnexpectedTxFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfIllegalFrequency"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMedia"),
        ("LUM-MULTIRATE-MIB", "mrtIfTrxMediaMismatch"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserForcedOn"),
        ("LUM-MULTIRATE-MIB", "mrtIfTruncAutoNegotiationMode"),
        ("LUM-MULTIRATE-MIB", "mrtIfObjectProperty"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPowerLevel"),
        ("LUM-MULTIRATE-MIB", "mrtIfLaserTempActual"),
        ("LUM-MULTIRATE-MIB", "mrtIfHighSpeed2"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxSignalStatus"))
)
if mibBuilder.loadTexts:
    mrtIfGroupV16.setStatus("current")


# Notification objects

mrtIfTxSignalStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 3, 0, 1)
)
mrtIfTxSignalStatusDown.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfEntityId"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatus"))
)
if mibBuilder.loadTexts:
    mrtIfTxSignalStatusDown.setStatus(
        "current"
    )

mrtIfTxSignalStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 3, 0, 2)
)
mrtIfTxSignalStatusUp.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfEntityId"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatus"))
)
if mibBuilder.loadTexts:
    mrtIfTxSignalStatusUp.setStatus(
        "current"
    )

mrtIfTxSignalStatusDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 2, 3, 0, 3)
)
mrtIfTxSignalStatusDegraded.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfIndex"),
        ("LUM-MULTIRATE-MIB", "mrtIfName"),
        ("LUM-MULTIRATE-MIB", "mrtIfSubrack"),
        ("LUM-MULTIRATE-MIB", "mrtIfSlot"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfRxPort"),
        ("LUM-MULTIRATE-MIB", "mrtIfEntityId"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatus"))
)
if mibBuilder.loadTexts:
    mrtIfTxSignalStatusDegraded.setStatus(
        "current"
    )


# Notifications groups

mrtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 7)
)
mrtNotificationGroup.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatusDown"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatusUp"))
)
if mibBuilder.loadTexts:
    mrtNotificationGroup.setStatus(
        "deprecated"
    )

mrtNotificationGroupV2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 1, 15)
)
mrtNotificationGroupV2.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatusDown"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatusUp"),
        ("LUM-MULTIRATE-MIB", "mrtIfTxSignalStatusDegraded"))
)
if mibBuilder.loadTexts:
    mrtNotificationGroupV2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lumMultirateBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 1)
)
lumMultirateBasicComplV1.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroup"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroup"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV1.setStatus(
        "deprecated"
    )

lumMultirateBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 2)
)
lumMultirateBasicComplV2.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroupV2"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroup"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV2.setStatus(
        "deprecated"
    )

lumMultirateBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 3)
)
lumMultirateBasicComplV3.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroupV2"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroupV2"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV3.setStatus(
        "deprecated"
    )

lumMultirateBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 4)
)
lumMultirateBasicComplV4.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroupV2"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroupV3"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV4.setStatus(
        "deprecated"
    )

lumMultirateBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 5)
)
lumMultirateBasicComplV5.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroupV2"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroupV4"),
        ("LUM-MULTIRATE-MIB", "mrtNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV5.setStatus(
        "deprecated"
    )

lumMultirateBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 6)
)
lumMultirateBasicComplV6.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroupV3"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroupV4"),
        ("LUM-MULTIRATE-MIB", "mrtNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV6.setStatus(
        "deprecated"
    )

lumMultirateBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 7)
)
lumMultirateBasicComplV7.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroupV3"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroupV5"),
        ("LUM-MULTIRATE-MIB", "mrtNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV7.setStatus(
        "deprecated"
    )

lumMultirateBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 8)
)
lumMultirateBasicComplV8.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroupV3"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroupV6"),
        ("LUM-MULTIRATE-MIB", "mrtNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV8.setStatus(
        "deprecated"
    )

lumMultirateBasicComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 9)
)
lumMultirateBasicComplV9.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroupV3"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroupV7"),
        ("LUM-MULTIRATE-MIB", "mrtNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV9.setStatus(
        "deprecated"
    )

lumMultirateBasicComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 10)
)
lumMultirateBasicComplV10.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroupV3"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroupV8"),
        ("LUM-MULTIRATE-MIB", "mrtNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV10.setStatus(
        "deprecated"
    )

lumMultirateBasicComplV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 11)
)
lumMultirateBasicComplV11.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroupV3"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroupV9"),
        ("LUM-MULTIRATE-MIB", "mrtNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV11.setStatus(
        "deprecated"
    )

lumMultirateBasicComplV12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 12)
)
lumMultirateBasicComplV12.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroupV3"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroupV10"),
        ("LUM-MULTIRATE-MIB", "mrtNotificationGroupV2"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV12.setStatus(
        "deprecated"
    )

lumMultirateBasicComplV13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 13)
)
lumMultirateBasicComplV13.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroupV3"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroupV11"),
        ("LUM-MULTIRATE-MIB", "mrtNotificationGroupV2"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV13.setStatus(
        "deprecated"
    )

lumMultirateBasicComplV14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 14)
)
lumMultirateBasicComplV14.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroupV4"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroupV12"),
        ("LUM-MULTIRATE-MIB", "mrtNotificationGroupV2"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV14.setStatus(
        "deprecated"
    )

lumMultirateBasicComplV15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 15)
)
lumMultirateBasicComplV15.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroupV4"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroupV13"),
        ("LUM-MULTIRATE-MIB", "mrtNotificationGroupV2"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV15.setStatus(
        "deprecated"
    )

lumMultirateBasicComplV16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 16)
)
lumMultirateBasicComplV16.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroupV4"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroupV14"),
        ("LUM-MULTIRATE-MIB", "mrtNotificationGroupV2"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV16.setStatus(
        "deprecated"
    )

lumMultirateBasicComplV17 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 17)
)
lumMultirateBasicComplV17.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroupV4"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroupV15"),
        ("LUM-MULTIRATE-MIB", "mrtNotificationGroupV2"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV17.setStatus(
        "deprecated"
    )

lumMultirateBasicComplV18 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 18)
)
lumMultirateBasicComplV18.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroupV4"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroupV16"),
        ("LUM-MULTIRATE-MIB", "mrtNotificationGroupV2"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV18.setStatus(
        "deprecated"
    )

lumMultirateBasicComplV19 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12, 1, 2, 19)
)
lumMultirateBasicComplV19.setObjects(
      *(("LUM-MULTIRATE-MIB", "mrtGeneralGroupV4"),
        ("LUM-MULTIRATE-MIB", "mrtIfGroupV16"),
        ("LUM-MULTIRATE-MIB", "mrtNotificationGroupV2"))
)
if mibBuilder.loadTexts:
    lumMultirateBasicComplV19.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-MULTIRATE-MIB",
    **{"lumMultirateMIBModule": lumMultirateMIBModule,
       "lumMultirateConfs": lumMultirateConfs,
       "lumMultirateGroups": lumMultirateGroups,
       "mrtGeneralGroup": mrtGeneralGroup,
       "mrtIfGroup": mrtIfGroup,
       "mrtGeneralGroupV2": mrtGeneralGroupV2,
       "mrtIfGroupV2": mrtIfGroupV2,
       "mrtIfGroupV3": mrtIfGroupV3,
       "mrtIfGroupV4": mrtIfGroupV4,
       "mrtNotificationGroup": mrtNotificationGroup,
       "mrtGeneralGroupV3": mrtGeneralGroupV3,
       "mrtIfGroupV5": mrtIfGroupV5,
       "mrtIfGroupV6": mrtIfGroupV6,
       "mrtIfGroupV7": mrtIfGroupV7,
       "mrtIfGroupV8": mrtIfGroupV8,
       "mrtIfGroupV9": mrtIfGroupV9,
       "mrtIfGroupV10": mrtIfGroupV10,
       "mrtNotificationGroupV2": mrtNotificationGroupV2,
       "mrtIfGroupV11": mrtIfGroupV11,
       "mrtIfGroupV12": mrtIfGroupV12,
       "mrtGeneralGroupV4": mrtGeneralGroupV4,
       "mrtIfGroupV13": mrtIfGroupV13,
       "mrtIfGroupV14": mrtIfGroupV14,
       "mrtIfGroupV15": mrtIfGroupV15,
       "mrtIfGroupV16": mrtIfGroupV16,
       "lumMultirateCompl": lumMultirateCompl,
       "lumMultirateBasicComplV1": lumMultirateBasicComplV1,
       "lumMultirateBasicComplV2": lumMultirateBasicComplV2,
       "lumMultirateBasicComplV3": lumMultirateBasicComplV3,
       "lumMultirateBasicComplV4": lumMultirateBasicComplV4,
       "lumMultirateBasicComplV5": lumMultirateBasicComplV5,
       "lumMultirateBasicComplV6": lumMultirateBasicComplV6,
       "lumMultirateBasicComplV7": lumMultirateBasicComplV7,
       "lumMultirateBasicComplV8": lumMultirateBasicComplV8,
       "lumMultirateBasicComplV9": lumMultirateBasicComplV9,
       "lumMultirateBasicComplV10": lumMultirateBasicComplV10,
       "lumMultirateBasicComplV11": lumMultirateBasicComplV11,
       "lumMultirateBasicComplV12": lumMultirateBasicComplV12,
       "lumMultirateBasicComplV13": lumMultirateBasicComplV13,
       "lumMultirateBasicComplV14": lumMultirateBasicComplV14,
       "lumMultirateBasicComplV15": lumMultirateBasicComplV15,
       "lumMultirateBasicComplV16": lumMultirateBasicComplV16,
       "lumMultirateBasicComplV17": lumMultirateBasicComplV17,
       "lumMultirateBasicComplV18": lumMultirateBasicComplV18,
       "lumMultirateBasicComplV19": lumMultirateBasicComplV19,
       "lumMultirateMIBObjects": lumMultirateMIBObjects,
       "mrtGeneral": mrtGeneral,
       "mrtGeneralTestAndIncr": mrtGeneralTestAndIncr,
       "mrtGeneralMibSpecVersion": mrtGeneralMibSpecVersion,
       "mrtGeneralMibImplVersion": mrtGeneralMibImplVersion,
       "mrtGeneralLastChangeTime": mrtGeneralLastChangeTime,
       "mrtGeneralStateLastChangeTime": mrtGeneralStateLastChangeTime,
       "mrtGeneralMrtIfTableSize": mrtGeneralMrtIfTableSize,
       "mrtIfList": mrtIfList,
       "mrtIfTable": mrtIfTable,
       "mrtIfEntry": mrtIfEntry,
       "mrtIfIndex": mrtIfIndex,
       "mrtIfName": mrtIfName,
       "mrtIfDescr": mrtIfDescr,
       "mrtIfSubrack": mrtIfSubrack,
       "mrtIfSlot": mrtIfSlot,
       "mrtIfTxPort": mrtIfTxPort,
       "mrtIfRxPort": mrtIfRxPort,
       "mrtIfInvPhysIndexOrZero": mrtIfInvPhysIndexOrZero,
       "mrtIfFormat": mrtIfFormat,
       "mrtIfHighSpeed": mrtIfHighSpeed,
       "mrtIfHighSpeedMin": mrtIfHighSpeedMin,
       "mrtIfHighSpeedMax": mrtIfHighSpeedMax,
       "mrtIfPowerLevel": mrtIfPowerLevel,
       "mrtIfPowerLevelHighThreshold": mrtIfPowerLevelHighThreshold,
       "mrtIfPowerLevelLowThreshold": mrtIfPowerLevelLowThreshold,
       "mrtIfLaserStatus": mrtIfLaserStatus,
       "mrtIfAdminStatus": mrtIfAdminStatus,
       "mrtIfOperStatus": mrtIfOperStatus,
       "mrtIfLossOfSignal": mrtIfLossOfSignal,
       "mrtIfReceivedPowerHigh": mrtIfReceivedPowerHigh,
       "mrtIfReceivedPowerLow": mrtIfReceivedPowerLow,
       "mrtIfLaserBiasHigh": mrtIfLaserBiasHigh,
       "mrtIfErroredSeconds": mrtIfErroredSeconds,
       "mrtIfSeverelyErroredSeconds": mrtIfSeverelyErroredSeconds,
       "mrtIfBackgroundBlockErrors": mrtIfBackgroundBlockErrors,
       "mrtIfUnavailableSeconds": mrtIfUnavailableSeconds,
       "mrtIfLossOfFrame": mrtIfLossOfFrame,
       "mrtIfMsAlarmIndicationSignalC2W": mrtIfMsAlarmIndicationSignalC2W,
       "mrtIfRemoteDefectIndication": mrtIfRemoteDefectIndication,
       "mrtIfLossOfSync": mrtIfLossOfSync,
       "mrtIfBitrateMismatch": mrtIfBitrateMismatch,
       "mrtIfLaserBias": mrtIfLaserBias,
       "mrtIfLaserBiasThreshold": mrtIfLaserBiasThreshold,
       "mrtIfJ0PathTrace": mrtIfJ0PathTrace,
       "mrtIfAuAlarmIndicationSignalW2C": mrtIfAuAlarmIndicationSignalW2C,
       "mrtIfAuLossOfPointerW2C": mrtIfAuLossOfPointerW2C,
       "mrtIfTxSignalStatus": mrtIfTxSignalStatus,
       "mrtIfTruncVc4": mrtIfTruncVc4,
       "mrtIfAuAlarmIndicationSignalC2W": mrtIfAuAlarmIndicationSignalC2W,
       "mrtIfAuLossOfPointerC2W": mrtIfAuLossOfPointerC2W,
       "mrtIfTraceIntrusionMode": mrtIfTraceIntrusionMode,
       "mrtIfTraceTransmitted": mrtIfTraceTransmitted,
       "mrtIfTraceReceived": mrtIfTraceReceived,
       "mrtIfTraceExpected": mrtIfTraceExpected,
       "mrtIfTraceAlarmMode": mrtIfTraceAlarmMode,
       "mrtIfTraceMismatch": mrtIfTraceMismatch,
       "mrtIfTruncVc4Status": mrtIfTruncVc4Status,
       "mrtIfMsAlarmIndicationSignalW2C": mrtIfMsAlarmIndicationSignalW2C,
       "mrtIfForwardAls": mrtIfForwardAls,
       "mrtIfSuppressRemoteAlarms": mrtIfSuppressRemoteAlarms,
       "mrtIfConfigurationCommand": mrtIfConfigurationCommand,
       "mrtIfTrxCodeMismatch": mrtIfTrxCodeMismatch,
       "mrtIfTrxBitrateUnavailable": mrtIfTrxBitrateUnavailable,
       "mrtIfTrxMissing": mrtIfTrxMissing,
       "mrtIfTrxClass": mrtIfTrxClass,
       "mrtIfEntityId": mrtIfEntityId,
       "mrtIfTransmitterFailed": mrtIfTransmitterFailed,
       "mrtIfReceiverSensitivity": mrtIfReceiverSensitivity,
       "mrtIfPowerLevelLowRelativeThreshold": mrtIfPowerLevelLowRelativeThreshold,
       "mrtIfFarEndLoopback": mrtIfFarEndLoopback,
       "mrtIfConfigureModeCommand": mrtIfConfigureModeCommand,
       "mrtIfTrxMode": mrtIfTrxMode,
       "mrtIfExpectedTxFrequency": mrtIfExpectedTxFrequency,
       "mrtIfTxFrequency": mrtIfTxFrequency,
       "mrtIfUnexpectedTxFrequency": mrtIfUnexpectedTxFrequency,
       "mrtIfIllegalFrequency": mrtIfIllegalFrequency,
       "mrtIfTrxMedia": mrtIfTrxMedia,
       "mrtIfTrxMediaMismatch": mrtIfTrxMediaMismatch,
       "mrtIfLaserForcedOn": mrtIfLaserForcedOn,
       "mrtIfTruncAutoNegotiationMode": mrtIfTruncAutoNegotiationMode,
       "mrtIfObjectProperty": mrtIfObjectProperty,
       "mrtIfTxPowerLevel": mrtIfTxPowerLevel,
       "mrtIfLaserTempActual": mrtIfLaserTempActual,
       "mrtIfHighSpeed2": mrtIfHighSpeed2,
       "mrtIfRxSignalStatus": mrtIfRxSignalStatus,
       "lumentisMrtNotifications": lumentisMrtNotifications,
       "mrtNotifyPrefix": mrtNotifyPrefix,
       "mrtIfTxSignalStatusDown": mrtIfTxSignalStatusDown,
       "mrtIfTxSignalStatusUp": mrtIfTxSignalStatusUp,
       "mrtIfTxSignalStatusDegraded": mrtIfTxSignalStatusDegraded}
)
