# SNMP MIB module (LUM-DCN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-DCN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:15 2025
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

(lumDcnMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumDcnMIB",
    "lumModules")

(BoardOrInterfaceAdminStatus,
 BoardOrInterfaceOperStatus,
 CommandString,
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
    "CommandString",
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

lumDcnMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 21)
)
if mibBuilder.loadTexts:
    lumDcnMIBModule.setRevisions(
        ("2018-06-29 00:00",
         "2017-12-08 00:00",
         "2017-06-15 00:00",
         "2016-11-30 00:00",
         "2016-01-11 00:00",
         "2015-11-30 00:00",
         "2015-05-29 00:00",
         "2011-12-20 09:45",
         "2011-08-16 09:45",
         "2010-02-01 00:00",
         "2003-02-12 00:00",
         "2002-11-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DcnSignalType(TextualConvention, Integer32):
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
          ("electrical", 1),
          ("optical", 2))
    )



class DcnOscMode(TextualConvention, Integer32):
    status = "current"
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
        *(("icn", 0),
          ("dcn", 1),
          ("customer", 2),
          ("mixed", 3),
          ("unused", 4),
          ("lan", 5),
          ("customerOpto", 6),
          ("mixedOpto", 7))
    )



# MIB Managed Objects in the order of their OIDs

_LumDcnConfs_ObjectIdentity = ObjectIdentity
lumDcnConfs = _LumDcnConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1)
)
_LumDcnGroups_ObjectIdentity = ObjectIdentity
lumDcnGroups = _LumDcnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1)
)
_LumDcnCompl_ObjectIdentity = ObjectIdentity
lumDcnCompl = _LumDcnCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 2)
)
_LumDcnMIBObjects_ObjectIdentity = ObjectIdentity
lumDcnMIBObjects = _LumDcnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2)
)
_DcnGeneral_ObjectIdentity = ObjectIdentity
dcnGeneral = _DcnGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 1)
)
_DcnGeneralLastChangeTime_Type = DateAndTime
_DcnGeneralLastChangeTime_Object = MibScalar
dcnGeneralLastChangeTime = _DcnGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 1, 1),
    _DcnGeneralLastChangeTime_Type()
)
dcnGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnGeneralLastChangeTime.setStatus("current")
_DcnGeneralStateLastChangeTime_Type = DateAndTime
_DcnGeneralStateLastChangeTime_Object = MibScalar
dcnGeneralStateLastChangeTime = _DcnGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 1, 2),
    _DcnGeneralStateLastChangeTime_Type()
)
dcnGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnGeneralStateLastChangeTime.setStatus("current")
_DcnGeneralDcnIfTableSize_Type = Unsigned32
_DcnGeneralDcnIfTableSize_Object = MibScalar
dcnGeneralDcnIfTableSize = _DcnGeneralDcnIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 1, 3),
    _DcnGeneralDcnIfTableSize_Type()
)
dcnGeneralDcnIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnGeneralDcnIfTableSize.setStatus("current")
_DcnGeneralDcnPppTableSize_Type = Unsigned32
_DcnGeneralDcnPppTableSize_Object = MibScalar
dcnGeneralDcnPppTableSize = _DcnGeneralDcnPppTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 1, 4),
    _DcnGeneralDcnPppTableSize_Type()
)
dcnGeneralDcnPppTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnGeneralDcnPppTableSize.setStatus("current")
_DcnGeneralDcnEthTableSize_Type = Unsigned32
_DcnGeneralDcnEthTableSize_Object = MibScalar
dcnGeneralDcnEthTableSize = _DcnGeneralDcnEthTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 1, 5),
    _DcnGeneralDcnEthTableSize_Type()
)
dcnGeneralDcnEthTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnGeneralDcnEthTableSize.setStatus("current")
_DcnGeneralDcnCcTableSize_Type = Unsigned32
_DcnGeneralDcnCcTableSize_Object = MibScalar
dcnGeneralDcnCcTableSize = _DcnGeneralDcnCcTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 1, 6),
    _DcnGeneralDcnCcTableSize_Type()
)
dcnGeneralDcnCcTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnGeneralDcnCcTableSize.setStatus("current")
_DcnIfList_ObjectIdentity = ObjectIdentity
dcnIfList = _DcnIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2)
)
_DcnIfTable_Object = MibTable
dcnIfTable = _DcnIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dcnIfTable.setStatus("current")
_DcnIfEntry_Object = MibTableRow
dcnIfEntry = _DcnIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1)
)
dcnIfEntry.setIndexNames(
    (0, "LUM-DCN-MIB", "dcnIfIndex"),
)
if mibBuilder.loadTexts:
    dcnIfEntry.setStatus("current")


class _DcnIfIndex_Type(Unsigned32):
    """Custom type dcnIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DcnIfIndex_Type.__name__ = "Unsigned32"
_DcnIfIndex_Object = MibTableColumn
dcnIfIndex = _DcnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 1),
    _DcnIfIndex_Type()
)
dcnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfIndex.setStatus("current")
_DcnIfName_Type = MgmtNameString
_DcnIfName_Object = MibTableColumn
dcnIfName = _DcnIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 2),
    _DcnIfName_Type()
)
dcnIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfName.setStatus("current")


class _DcnIfDescr_Type(DisplayString):
    """Custom type dcnIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_DcnIfDescr_Type.__name__ = "DisplayString"
_DcnIfDescr_Object = MibTableColumn
dcnIfDescr = _DcnIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 3),
    _DcnIfDescr_Type()
)
dcnIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnIfDescr.setStatus("current")
_DcnIfSubrack_Type = SubrackNumber
_DcnIfSubrack_Object = MibTableColumn
dcnIfSubrack = _DcnIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 4),
    _DcnIfSubrack_Type()
)
dcnIfSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfSubrack.setStatus("current")
_DcnIfSlot_Type = SlotNumber
_DcnIfSlot_Object = MibTableColumn
dcnIfSlot = _DcnIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 5),
    _DcnIfSlot_Type()
)
dcnIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfSlot.setStatus("current")
_DcnIfTxPort_Type = PortNumber
_DcnIfTxPort_Object = MibTableColumn
dcnIfTxPort = _DcnIfTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 6),
    _DcnIfTxPort_Type()
)
dcnIfTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfTxPort.setStatus("current")
_DcnIfRxPort_Type = PortNumber
_DcnIfRxPort_Object = MibTableColumn
dcnIfRxPort = _DcnIfRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 7),
    _DcnIfRxPort_Type()
)
dcnIfRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfRxPort.setStatus("current")


class _DcnIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type dcnIfInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DcnIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_DcnIfInvPhysIndexOrZero_Object = MibTableColumn
dcnIfInvPhysIndexOrZero = _DcnIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 8),
    _DcnIfInvPhysIndexOrZero_Type()
)
dcnIfInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfInvPhysIndexOrZero.setStatus("current")
_DcnIfType_Type = DcnSignalType
_DcnIfType_Object = MibTableColumn
dcnIfType = _DcnIfType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 9),
    _DcnIfType_Type()
)
dcnIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfType.setStatus("current")


class _DcnIfMaxSpeed_Type(Gauge32):
    """Custom type dcnIfMaxSpeed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_DcnIfMaxSpeed_Type.__name__ = "Gauge32"
_DcnIfMaxSpeed_Object = MibTableColumn
dcnIfMaxSpeed = _DcnIfMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 10),
    _DcnIfMaxSpeed_Type()
)
dcnIfMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfMaxSpeed.setStatus("current")


class _DcnIfOscMode_Type(DcnOscMode):
    """Custom type dcnIfOscMode based on DcnOscMode"""
    defaultValue = 1


_DcnIfOscMode_Type.__name__ = "DcnOscMode"
_DcnIfOscMode_Object = MibTableColumn
dcnIfOscMode = _DcnIfOscMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 11),
    _DcnIfOscMode_Type()
)
dcnIfOscMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnIfOscMode.setStatus("current")


class _DcnIfAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type dcnIfAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 1


_DcnIfAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_DcnIfAdminStatus_Object = MibTableColumn
dcnIfAdminStatus = _DcnIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 12),
    _DcnIfAdminStatus_Type()
)
dcnIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnIfAdminStatus.setStatus("current")


class _DcnIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type dcnIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_DcnIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_DcnIfOperStatus_Object = MibTableColumn
dcnIfOperStatus = _DcnIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 13),
    _DcnIfOperStatus_Type()
)
dcnIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfOperStatus.setStatus("current")


class _DcnIfTxSignalStatus_Type(Integer32):
    """Custom type dcnIfTxSignalStatus based on Integer32"""
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


_DcnIfTxSignalStatus_Type.__name__ = "Integer32"
_DcnIfTxSignalStatus_Object = MibTableColumn
dcnIfTxSignalStatus = _DcnIfTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 14),
    _DcnIfTxSignalStatus_Type()
)
dcnIfTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfTxSignalStatus.setStatus("current")
_DcnIfLinkDown_Type = FaultStatus
_DcnIfLinkDown_Object = MibTableColumn
dcnIfLinkDown = _DcnIfLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 15),
    _DcnIfLinkDown_Type()
)
dcnIfLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfLinkDown.setStatus("current")
_DcnIfTxFrequency_Type = LambdaFrequency
_DcnIfTxFrequency_Object = MibTableColumn
dcnIfTxFrequency = _DcnIfTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 16),
    _DcnIfTxFrequency_Type()
)
dcnIfTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfTxFrequency.setStatus("current")
_DcnIfObjectProperty_Type = ObjectProperty
_DcnIfObjectProperty_Object = MibTableColumn
dcnIfObjectProperty = _DcnIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 17),
    _DcnIfObjectProperty_Type()
)
dcnIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfObjectProperty.setStatus("current")


class _DcnIfLaserStatus_Type(Integer32):
    """Custom type dcnIfLaserStatus based on Integer32"""
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


_DcnIfLaserStatus_Type.__name__ = "Integer32"
_DcnIfLaserStatus_Object = MibTableColumn
dcnIfLaserStatus = _DcnIfLaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 18),
    _DcnIfLaserStatus_Type()
)
dcnIfLaserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfLaserStatus.setStatus("current")
_DcnIfPowerLevel_Type = Integer32
_DcnIfPowerLevel_Object = MibTableColumn
dcnIfPowerLevel = _DcnIfPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 19),
    _DcnIfPowerLevel_Type()
)
dcnIfPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfPowerLevel.setStatus("current")
_DcnIfTxPowerLevel_Type = Integer32
_DcnIfTxPowerLevel_Object = MibTableColumn
dcnIfTxPowerLevel = _DcnIfTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 20),
    _DcnIfTxPowerLevel_Type()
)
dcnIfTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfTxPowerLevel.setStatus("current")
_DcnIfReceiverSensitivity_Type = Integer32
_DcnIfReceiverSensitivity_Object = MibTableColumn
dcnIfReceiverSensitivity = _DcnIfReceiverSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 21),
    _DcnIfReceiverSensitivity_Type()
)
dcnIfReceiverSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfReceiverSensitivity.setStatus("current")


class _DcnIfPowerLevelLowRelativeThreshold_Type(Integer32):
    """Custom type dcnIfPowerLevelLowRelativeThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_DcnIfPowerLevelLowRelativeThreshold_Type.__name__ = "Integer32"
_DcnIfPowerLevelLowRelativeThreshold_Object = MibTableColumn
dcnIfPowerLevelLowRelativeThreshold = _DcnIfPowerLevelLowRelativeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 22),
    _DcnIfPowerLevelLowRelativeThreshold_Type()
)
dcnIfPowerLevelLowRelativeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnIfPowerLevelLowRelativeThreshold.setStatus("current")
_DcnIfLaserTempActual_Type = Integer32
_DcnIfLaserTempActual_Object = MibTableColumn
dcnIfLaserTempActual = _DcnIfLaserTempActual_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 23),
    _DcnIfLaserTempActual_Type()
)
dcnIfLaserTempActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfLaserTempActual.setStatus("current")


class _DcnIfTrxClass_Type(DisplayString):
    """Custom type dcnIfTrxClass based on DisplayString"""
    defaultValue = OctetString("")


_DcnIfTrxClass_Type.__name__ = "DisplayString"
_DcnIfTrxClass_Object = MibTableColumn
dcnIfTrxClass = _DcnIfTrxClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 24),
    _DcnIfTrxClass_Type()
)
dcnIfTrxClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfTrxClass.setStatus("current")
_DcnIfHighSpeedMin_Type = Gauge32
_DcnIfHighSpeedMin_Object = MibTableColumn
dcnIfHighSpeedMin = _DcnIfHighSpeedMin_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 25),
    _DcnIfHighSpeedMin_Type()
)
dcnIfHighSpeedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfHighSpeedMin.setStatus("current")
_DcnIfHighSpeedMax_Type = Gauge32
_DcnIfHighSpeedMax_Object = MibTableColumn
dcnIfHighSpeedMax = _DcnIfHighSpeedMax_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 26),
    _DcnIfHighSpeedMax_Type()
)
dcnIfHighSpeedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfHighSpeedMax.setStatus("current")


class _DcnIfExpectedTxFrequency_Type(LambdaFrequency):
    """Custom type dcnIfExpectedTxFrequency based on LambdaFrequency"""
    defaultValue = 0


_DcnIfExpectedTxFrequency_Type.__name__ = "LambdaFrequency"
_DcnIfExpectedTxFrequency_Object = MibTableColumn
dcnIfExpectedTxFrequency = _DcnIfExpectedTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 27),
    _DcnIfExpectedTxFrequency_Type()
)
dcnIfExpectedTxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnIfExpectedTxFrequency.setStatus("current")
_DcnIfLaserBias_Type = Unsigned32
_DcnIfLaserBias_Object = MibTableColumn
dcnIfLaserBias = _DcnIfLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 28),
    _DcnIfLaserBias_Type()
)
dcnIfLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfLaserBias.setStatus("current")
_DcnIfLossOfSignal_Type = FaultStatus
_DcnIfLossOfSignal_Object = MibTableColumn
dcnIfLossOfSignal = _DcnIfLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 29),
    _DcnIfLossOfSignal_Type()
)
dcnIfLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfLossOfSignal.setStatus("current")
_DcnIfTrxCodeMismatch_Type = FaultStatus
_DcnIfTrxCodeMismatch_Object = MibTableColumn
dcnIfTrxCodeMismatch = _DcnIfTrxCodeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 30),
    _DcnIfTrxCodeMismatch_Type()
)
dcnIfTrxCodeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfTrxCodeMismatch.setStatus("current")
_DcnIfTrxBitrateUnavailable_Type = FaultStatus
_DcnIfTrxBitrateUnavailable_Object = MibTableColumn
dcnIfTrxBitrateUnavailable = _DcnIfTrxBitrateUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 31),
    _DcnIfTrxBitrateUnavailable_Type()
)
dcnIfTrxBitrateUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfTrxBitrateUnavailable.setStatus("current")
_DcnIfTrxMissing_Type = FaultStatus
_DcnIfTrxMissing_Object = MibTableColumn
dcnIfTrxMissing = _DcnIfTrxMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 32),
    _DcnIfTrxMissing_Type()
)
dcnIfTrxMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfTrxMissing.setStatus("current")
_DcnIfTransmitterFailed_Type = FaultStatus
_DcnIfTransmitterFailed_Object = MibTableColumn
dcnIfTransmitterFailed = _DcnIfTransmitterFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 33),
    _DcnIfTransmitterFailed_Type()
)
dcnIfTransmitterFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfTransmitterFailed.setStatus("current")
_DcnIfIllegalFrequency_Type = FaultStatus
_DcnIfIllegalFrequency_Object = MibTableColumn
dcnIfIllegalFrequency = _DcnIfIllegalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 34),
    _DcnIfIllegalFrequency_Type()
)
dcnIfIllegalFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfIllegalFrequency.setStatus("current")
_DcnIfUnexpectedTxFrequency_Type = FaultStatus
_DcnIfUnexpectedTxFrequency_Object = MibTableColumn
dcnIfUnexpectedTxFrequency = _DcnIfUnexpectedTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 35),
    _DcnIfUnexpectedTxFrequency_Type()
)
dcnIfUnexpectedTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfUnexpectedTxFrequency.setStatus("current")
_DcnIfReceivedPowerHigh_Type = FaultStatus
_DcnIfReceivedPowerHigh_Object = MibTableColumn
dcnIfReceivedPowerHigh = _DcnIfReceivedPowerHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 36),
    _DcnIfReceivedPowerHigh_Type()
)
dcnIfReceivedPowerHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfReceivedPowerHigh.setStatus("current")
_DcnIfReceivedPowerLow_Type = FaultStatus
_DcnIfReceivedPowerLow_Object = MibTableColumn
dcnIfReceivedPowerLow = _DcnIfReceivedPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 37),
    _DcnIfReceivedPowerLow_Type()
)
dcnIfReceivedPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfReceivedPowerLow.setStatus("current")
_DcnIfTrxMediaMismatch_Type = FaultStatus
_DcnIfTrxMediaMismatch_Object = MibTableColumn
dcnIfTrxMediaMismatch = _DcnIfTrxMediaMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 38),
    _DcnIfTrxMediaMismatch_Type()
)
dcnIfTrxMediaMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfTrxMediaMismatch.setStatus("current")
_DcnIfProtocolVersionMismatch_Type = FaultStatus
_DcnIfProtocolVersionMismatch_Object = MibTableColumn
dcnIfProtocolVersionMismatch = _DcnIfProtocolVersionMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 39),
    _DcnIfProtocolVersionMismatch_Type()
)
dcnIfProtocolVersionMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfProtocolVersionMismatch.setStatus("current")
_DcnIfRemoteDefectIndication_Type = FaultStatus
_DcnIfRemoteDefectIndication_Object = MibTableColumn
dcnIfRemoteDefectIndication = _DcnIfRemoteDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 40),
    _DcnIfRemoteDefectIndication_Type()
)
dcnIfRemoteDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfRemoteDefectIndication.setStatus("current")


class _DcnIfTraceTransmitted_Type(DisplayString):
    """Custom type dcnIfTraceTransmitted based on DisplayString"""
    defaultValue = OctetString("")


_DcnIfTraceTransmitted_Type.__name__ = "DisplayString"
_DcnIfTraceTransmitted_Object = MibTableColumn
dcnIfTraceTransmitted = _DcnIfTraceTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 41),
    _DcnIfTraceTransmitted_Type()
)
dcnIfTraceTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnIfTraceTransmitted.setStatus("current")
_DcnIfTraceReceived_Type = DisplayString
_DcnIfTraceReceived_Object = MibTableColumn
dcnIfTraceReceived = _DcnIfTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 42),
    _DcnIfTraceReceived_Type()
)
dcnIfTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfTraceReceived.setStatus("current")


class _DcnIfTraceExpected_Type(DisplayString):
    """Custom type dcnIfTraceExpected based on DisplayString"""
    defaultValue = OctetString("")


_DcnIfTraceExpected_Type.__name__ = "DisplayString"
_DcnIfTraceExpected_Object = MibTableColumn
dcnIfTraceExpected = _DcnIfTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 43),
    _DcnIfTraceExpected_Type()
)
dcnIfTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnIfTraceExpected.setStatus("current")


class _DcnIfTraceAlarmMode_Type(Integer32):
    """Custom type dcnIfTraceAlarmMode based on Integer32"""
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


_DcnIfTraceAlarmMode_Type.__name__ = "Integer32"
_DcnIfTraceAlarmMode_Object = MibTableColumn
dcnIfTraceAlarmMode = _DcnIfTraceAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 44),
    _DcnIfTraceAlarmMode_Type()
)
dcnIfTraceAlarmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnIfTraceAlarmMode.setStatus("current")
_DcnIfTraceMismatch_Type = FaultStatus
_DcnIfTraceMismatch_Object = MibTableColumn
dcnIfTraceMismatch = _DcnIfTraceMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 55),
    _DcnIfTraceMismatch_Type()
)
dcnIfTraceMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfTraceMismatch.setStatus("current")


class _DcnIfLaserMode_Type(Integer32):
    """Custom type dcnIfLaserMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("als", 2))
    )


_DcnIfLaserMode_Type.__name__ = "Integer32"
_DcnIfLaserMode_Object = MibTableColumn
dcnIfLaserMode = _DcnIfLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 56),
    _DcnIfLaserMode_Type()
)
dcnIfLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnIfLaserMode.setStatus("current")
_DcnIfLinkSupervisionFailure_Type = FaultStatus
_DcnIfLinkSupervisionFailure_Object = MibTableColumn
dcnIfLinkSupervisionFailure = _DcnIfLinkSupervisionFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 57),
    _DcnIfLinkSupervisionFailure_Type()
)
dcnIfLinkSupervisionFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfLinkSupervisionFailure.setStatus("current")
_DcnIfAid_Type = DisplayString
_DcnIfAid_Object = MibTableColumn
dcnIfAid = _DcnIfAid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 58),
    _DcnIfAid_Type()
)
dcnIfAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfAid.setStatus("current")
_DcnIfPhysicalLocation_Type = DisplayString
_DcnIfPhysicalLocation_Object = MibTableColumn
dcnIfPhysicalLocation = _DcnIfPhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 2, 1, 1, 59),
    _DcnIfPhysicalLocation_Type()
)
dcnIfPhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnIfPhysicalLocation.setStatus("current")
_LumentisDcnNotifications_ObjectIdentity = ObjectIdentity
lumentisDcnNotifications = _LumentisDcnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 3)
)
_DcnNotifyPrefix_ObjectIdentity = ObjectIdentity
dcnNotifyPrefix = _DcnNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 3, 0)
)
_DcnPppList_ObjectIdentity = ObjectIdentity
dcnPppList = _DcnPppList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4)
)
_DcnPppTable_Object = MibTable
dcnPppTable = _DcnPppTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1)
)
if mibBuilder.loadTexts:
    dcnPppTable.setStatus("current")
_DcnPppEntry_Object = MibTableRow
dcnPppEntry = _DcnPppEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1)
)
dcnPppEntry.setIndexNames(
    (0, "LUM-DCN-MIB", "dcnPppIndex"),
)
if mibBuilder.loadTexts:
    dcnPppEntry.setStatus("current")


class _DcnPppIndex_Type(Unsigned32):
    """Custom type dcnPppIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DcnPppIndex_Type.__name__ = "Unsigned32"
_DcnPppIndex_Object = MibTableColumn
dcnPppIndex = _DcnPppIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 1),
    _DcnPppIndex_Type()
)
dcnPppIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnPppIndex.setStatus("current")
_DcnPppName_Type = MgmtNameString
_DcnPppName_Object = MibTableColumn
dcnPppName = _DcnPppName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 2),
    _DcnPppName_Type()
)
dcnPppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnPppName.setStatus("current")


class _DcnPppDescr_Type(DisplayString):
    """Custom type dcnPppDescr based on DisplayString"""
    defaultValue = OctetString("")


_DcnPppDescr_Type.__name__ = "DisplayString"
_DcnPppDescr_Object = MibTableColumn
dcnPppDescr = _DcnPppDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 3),
    _DcnPppDescr_Type()
)
dcnPppDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnPppDescr.setStatus("current")
_DcnPppTxSubrack_Type = SubrackNumber
_DcnPppTxSubrack_Object = MibTableColumn
dcnPppTxSubrack = _DcnPppTxSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 4),
    _DcnPppTxSubrack_Type()
)
dcnPppTxSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcnPppTxSubrack.setStatus("current")
_DcnPppTxSlot_Type = SlotNumber
_DcnPppTxSlot_Object = MibTableColumn
dcnPppTxSlot = _DcnPppTxSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 5),
    _DcnPppTxSlot_Type()
)
dcnPppTxSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcnPppTxSlot.setStatus("current")
_DcnPppTxPort_Type = PortNumber
_DcnPppTxPort_Object = MibTableColumn
dcnPppTxPort = _DcnPppTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 6),
    _DcnPppTxPort_Type()
)
dcnPppTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcnPppTxPort.setStatus("current")
_DcnPppRxSubrack_Type = SubrackNumber
_DcnPppRxSubrack_Object = MibTableColumn
dcnPppRxSubrack = _DcnPppRxSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 7),
    _DcnPppRxSubrack_Type()
)
dcnPppRxSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcnPppRxSubrack.setStatus("current")
_DcnPppRxSlot_Type = SlotNumber
_DcnPppRxSlot_Object = MibTableColumn
dcnPppRxSlot = _DcnPppRxSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 8),
    _DcnPppRxSlot_Type()
)
dcnPppRxSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcnPppRxSlot.setStatus("current")
_DcnPppRxPort_Type = PortNumber
_DcnPppRxPort_Object = MibTableColumn
dcnPppRxPort = _DcnPppRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 9),
    _DcnPppRxPort_Type()
)
dcnPppRxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcnPppRxPort.setStatus("current")


class _DcnPppInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type dcnPppInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DcnPppInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_DcnPppInvPhysIndexOrZero_Object = MibTableColumn
dcnPppInvPhysIndexOrZero = _DcnPppInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 10),
    _DcnPppInvPhysIndexOrZero_Type()
)
dcnPppInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnPppInvPhysIndexOrZero.setStatus("current")


class _DcnPppType_Type(Integer32):
    """Custom type dcnPppType based on Integer32"""
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
        *(("proprietary", 1),
          ("osc", 2),
          ("sdh", 3),
          ("g709", 4),
          ("sonet", 5))
    )


_DcnPppType_Type.__name__ = "Integer32"
_DcnPppType_Object = MibTableColumn
dcnPppType = _DcnPppType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 11),
    _DcnPppType_Type()
)
dcnPppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnPppType.setStatus("current")


class _DcnPppAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type dcnPppAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_DcnPppAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_DcnPppAdminStatus_Object = MibTableColumn
dcnPppAdminStatus = _DcnPppAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 12),
    _DcnPppAdminStatus_Type()
)
dcnPppAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnPppAdminStatus.setStatus("current")


class _DcnPppOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type dcnPppOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_DcnPppOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_DcnPppOperStatus_Object = MibTableColumn
dcnPppOperStatus = _DcnPppOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 13),
    _DcnPppOperStatus_Type()
)
dcnPppOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnPppOperStatus.setStatus("current")
_DcnPppRouteName_Type = MgmtNameString
_DcnPppRouteName_Object = MibTableColumn
dcnPppRouteName = _DcnPppRouteName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 14),
    _DcnPppRouteName_Type()
)
dcnPppRouteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnPppRouteName.setStatus("current")
_DcnPppDialCommand_Type = CommandString
_DcnPppDialCommand_Object = MibTableColumn
dcnPppDialCommand = _DcnPppDialCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 15),
    _DcnPppDialCommand_Type()
)
dcnPppDialCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnPppDialCommand.setStatus("current")
_DcnPppAcceptCommand_Type = CommandString
_DcnPppAcceptCommand_Object = MibTableColumn
dcnPppAcceptCommand = _DcnPppAcceptCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 16),
    _DcnPppAcceptCommand_Type()
)
dcnPppAcceptCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnPppAcceptCommand.setStatus("current")


class _DcnPppLogicalLinkId_Type(Integer32):
    """Custom type dcnPppLogicalLinkId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 11),
    )


_DcnPppLogicalLinkId_Type.__name__ = "Integer32"
_DcnPppLogicalLinkId_Object = MibTableColumn
dcnPppLogicalLinkId = _DcnPppLogicalLinkId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 17),
    _DcnPppLogicalLinkId_Type()
)
dcnPppLogicalLinkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcnPppLogicalLinkId.setStatus("current")
_DcnPppObjectProperty_Type = ObjectProperty
_DcnPppObjectProperty_Object = MibTableColumn
dcnPppObjectProperty = _DcnPppObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 18),
    _DcnPppObjectProperty_Type()
)
dcnPppObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnPppObjectProperty.setStatus("current")


class _DcnPppGccChannel_Type(Integer32):
    """Custom type dcnPppGccChannel based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2),
    )


_DcnPppGccChannel_Type.__name__ = "Integer32"
_DcnPppGccChannel_Object = MibTableColumn
dcnPppGccChannel = _DcnPppGccChannel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 19),
    _DcnPppGccChannel_Type()
)
dcnPppGccChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcnPppGccChannel.setStatus("current")


class _DcnPppVlanId_Type(Integer32):
    """Custom type dcnPppVlanId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4095),
    )


_DcnPppVlanId_Type.__name__ = "Integer32"
_DcnPppVlanId_Object = MibTableColumn
dcnPppVlanId = _DcnPppVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 20),
    _DcnPppVlanId_Type()
)
dcnPppVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcnPppVlanId.setStatus("current")


class _DcnPppVlanEtherType_Type(Integer32):
    """Custom type dcnPppVlanEtherType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qTag0x8100", 1),
          ("sTag0x88a8", 2))
    )


_DcnPppVlanEtherType_Type.__name__ = "Integer32"
_DcnPppVlanEtherType_Object = MibTableColumn
dcnPppVlanEtherType = _DcnPppVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 21),
    _DcnPppVlanEtherType_Type()
)
dcnPppVlanEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnPppVlanEtherType.setStatus("current")
_DcnPppTxIfNo_Type = PortNumber
_DcnPppTxIfNo_Object = MibTableColumn
dcnPppTxIfNo = _DcnPppTxIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 22),
    _DcnPppTxIfNo_Type()
)
dcnPppTxIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcnPppTxIfNo.setStatus("current")
_DcnPppRxIfNo_Type = PortNumber
_DcnPppRxIfNo_Object = MibTableColumn
dcnPppRxIfNo = _DcnPppRxIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 4, 1, 1, 23),
    _DcnPppRxIfNo_Type()
)
dcnPppRxIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcnPppRxIfNo.setStatus("current")
_DcnAddress_ObjectIdentity = ObjectIdentity
dcnAddress = _DcnAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 5)
)
_DcnAddressCurrentPppAddress_Type = IpAddress
_DcnAddressCurrentPppAddress_Object = MibScalar
dcnAddressCurrentPppAddress = _DcnAddressCurrentPppAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 5, 1),
    _DcnAddressCurrentPppAddress_Type()
)
dcnAddressCurrentPppAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnAddressCurrentPppAddress.setStatus("current")
_DcnAddressNextPppAddress_Type = IpAddress
_DcnAddressNextPppAddress_Object = MibScalar
dcnAddressNextPppAddress = _DcnAddressNextPppAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 5, 2),
    _DcnAddressNextPppAddress_Type()
)
dcnAddressNextPppAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnAddressNextPppAddress.setStatus("current")
_DcnEthList_ObjectIdentity = ObjectIdentity
dcnEthList = _DcnEthList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6)
)
_DcnEthTable_Object = MibTable
dcnEthTable = _DcnEthTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6, 1)
)
if mibBuilder.loadTexts:
    dcnEthTable.setStatus("current")
_DcnEthEntry_Object = MibTableRow
dcnEthEntry = _DcnEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6, 1, 1)
)
dcnEthEntry.setIndexNames(
    (0, "LUM-DCN-MIB", "dcnEthIndex"),
)
if mibBuilder.loadTexts:
    dcnEthEntry.setStatus("current")


class _DcnEthIndex_Type(Unsigned32):
    """Custom type dcnEthIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DcnEthIndex_Type.__name__ = "Unsigned32"
_DcnEthIndex_Object = MibTableColumn
dcnEthIndex = _DcnEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6, 1, 1, 1),
    _DcnEthIndex_Type()
)
dcnEthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnEthIndex.setStatus("current")
_DcnEthName_Type = MgmtNameString
_DcnEthName_Object = MibTableColumn
dcnEthName = _DcnEthName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6, 1, 1, 2),
    _DcnEthName_Type()
)
dcnEthName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnEthName.setStatus("current")


class _DcnEthDescr_Type(DisplayString):
    """Custom type dcnEthDescr based on DisplayString"""
    defaultValue = OctetString("")


_DcnEthDescr_Type.__name__ = "DisplayString"
_DcnEthDescr_Object = MibTableColumn
dcnEthDescr = _DcnEthDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6, 1, 1, 3),
    _DcnEthDescr_Type()
)
dcnEthDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnEthDescr.setStatus("current")
_DcnEthSubrack_Type = SubrackNumber
_DcnEthSubrack_Object = MibTableColumn
dcnEthSubrack = _DcnEthSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6, 1, 1, 4),
    _DcnEthSubrack_Type()
)
dcnEthSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnEthSubrack.setStatus("current")
_DcnEthSlot_Type = SlotNumber
_DcnEthSlot_Object = MibTableColumn
dcnEthSlot = _DcnEthSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6, 1, 1, 5),
    _DcnEthSlot_Type()
)
dcnEthSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnEthSlot.setStatus("current")
_DcnEthPort_Type = PortNumber
_DcnEthPort_Object = MibTableColumn
dcnEthPort = _DcnEthPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6, 1, 1, 6),
    _DcnEthPort_Type()
)
dcnEthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnEthPort.setStatus("current")


class _DcnEthAutoNegotiationMode_Type(Integer32):
    """Custom type dcnEthAutoNegotiationMode based on Integer32"""
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


_DcnEthAutoNegotiationMode_Type.__name__ = "Integer32"
_DcnEthAutoNegotiationMode_Object = MibTableColumn
dcnEthAutoNegotiationMode = _DcnEthAutoNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6, 1, 1, 7),
    _DcnEthAutoNegotiationMode_Type()
)
dcnEthAutoNegotiationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcnEthAutoNegotiationMode.setStatus("current")


class _DcnEthLinkStatus_Type(Integer32):
    """Custom type dcnEthLinkStatus based on Integer32"""
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
          ("down", 1),
          ("unknown", 2))
    )


_DcnEthLinkStatus_Type.__name__ = "Integer32"
_DcnEthLinkStatus_Object = MibTableColumn
dcnEthLinkStatus = _DcnEthLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6, 1, 1, 8),
    _DcnEthLinkStatus_Type()
)
dcnEthLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnEthLinkStatus.setStatus("current")


class _DcnEthSpeed_Type(Integer32):
    """Custom type dcnEthSpeed based on Integer32"""
    defaultValue = 2

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
        *(("mbps10", 0),
          ("mbps100", 1),
          ("auto", 2),
          ("mbps1000", 3))
    )


_DcnEthSpeed_Type.__name__ = "Integer32"
_DcnEthSpeed_Object = MibTableColumn
dcnEthSpeed = _DcnEthSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6, 1, 1, 9),
    _DcnEthSpeed_Type()
)
dcnEthSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcnEthSpeed.setStatus("current")


class _DcnEthDuplexCapability_Type(Integer32):
    """Custom type dcnEthDuplexCapability based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("half", 1),
          ("full", 2),
          ("both", 3))
    )


_DcnEthDuplexCapability_Type.__name__ = "Integer32"
_DcnEthDuplexCapability_Object = MibTableColumn
dcnEthDuplexCapability = _DcnEthDuplexCapability_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6, 1, 1, 10),
    _DcnEthDuplexCapability_Type()
)
dcnEthDuplexCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcnEthDuplexCapability.setStatus("current")


class _DcnEthRateLimit_Type(Integer32):
    """Custom type dcnEthRateLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 125),
    )


_DcnEthRateLimit_Type.__name__ = "Integer32"
_DcnEthRateLimit_Object = MibTableColumn
dcnEthRateLimit = _DcnEthRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6, 1, 1, 11),
    _DcnEthRateLimit_Type()
)
dcnEthRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnEthRateLimit.setStatus("current")


class _DcnEthFlowControlMode_Type(Integer32):
    """Custom type dcnEthFlowControlMode based on Integer32"""
    defaultValue = 4

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


_DcnEthFlowControlMode_Type.__name__ = "Integer32"
_DcnEthFlowControlMode_Object = MibTableColumn
dcnEthFlowControlMode = _DcnEthFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6, 1, 1, 12),
    _DcnEthFlowControlMode_Type()
)
dcnEthFlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnEthFlowControlMode.setStatus("current")
_DcnEthObjectProperty_Type = ObjectProperty
_DcnEthObjectProperty_Object = MibTableColumn
dcnEthObjectProperty = _DcnEthObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6, 1, 1, 13),
    _DcnEthObjectProperty_Type()
)
dcnEthObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnEthObjectProperty.setStatus("current")
_DcnEthChangeSpeedCommand_Type = CommandString
_DcnEthChangeSpeedCommand_Object = MibTableColumn
dcnEthChangeSpeedCommand = _DcnEthChangeSpeedCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6, 1, 1, 15),
    _DcnEthChangeSpeedCommand_Type()
)
dcnEthChangeSpeedCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnEthChangeSpeedCommand.setStatus("current")


class _DcnEthAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type dcnEthAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_DcnEthAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_DcnEthAdminStatus_Object = MibTableColumn
dcnEthAdminStatus = _DcnEthAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6, 1, 1, 16),
    _DcnEthAdminStatus_Type()
)
dcnEthAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnEthAdminStatus.setStatus("current")


class _DcnEthOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type dcnEthOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_DcnEthOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_DcnEthOperStatus_Object = MibTableColumn
dcnEthOperStatus = _DcnEthOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 6, 1, 1, 17),
    _DcnEthOperStatus_Type()
)
dcnEthOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnEthOperStatus.setStatus("current")
_DcnCcList_ObjectIdentity = ObjectIdentity
dcnCcList = _DcnCcList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 7)
)
_DcnCcTable_Object = MibTable
dcnCcTable = _DcnCcTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 7, 1)
)
if mibBuilder.loadTexts:
    dcnCcTable.setStatus("current")
_DcnCcEntry_Object = MibTableRow
dcnCcEntry = _DcnCcEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 7, 1, 1)
)
dcnCcEntry.setIndexNames(
    (0, "LUM-DCN-MIB", "dcnCcIndex"),
)
if mibBuilder.loadTexts:
    dcnCcEntry.setStatus("current")


class _DcnCcIndex_Type(Unsigned32):
    """Custom type dcnCcIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DcnCcIndex_Type.__name__ = "Unsigned32"
_DcnCcIndex_Object = MibTableColumn
dcnCcIndex = _DcnCcIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 7, 1, 1, 1),
    _DcnCcIndex_Type()
)
dcnCcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnCcIndex.setStatus("current")
_DcnCcName_Type = MgmtNameString
_DcnCcName_Object = MibTableColumn
dcnCcName = _DcnCcName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 7, 1, 1, 2),
    _DcnCcName_Type()
)
dcnCcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnCcName.setStatus("current")


class _DcnCcDescr_Type(DisplayString):
    """Custom type dcnCcDescr based on DisplayString"""
    defaultValue = OctetString("")


_DcnCcDescr_Type.__name__ = "DisplayString"
_DcnCcDescr_Object = MibTableColumn
dcnCcDescr = _DcnCcDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 7, 1, 1, 3),
    _DcnCcDescr_Type()
)
dcnCcDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnCcDescr.setStatus("current")
_DcnCcSubrack_Type = SubrackNumber
_DcnCcSubrack_Object = MibTableColumn
dcnCcSubrack = _DcnCcSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 7, 1, 1, 4),
    _DcnCcSubrack_Type()
)
dcnCcSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnCcSubrack.setStatus("current")
_DcnCcSlot_Type = SlotNumber
_DcnCcSlot_Object = MibTableColumn
dcnCcSlot = _DcnCcSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 7, 1, 1, 5),
    _DcnCcSlot_Type()
)
dcnCcSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnCcSlot.setStatus("current")
_DcnCcTxPort_Type = PortNumber
_DcnCcTxPort_Object = MibTableColumn
dcnCcTxPort = _DcnCcTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 7, 1, 1, 6),
    _DcnCcTxPort_Type()
)
dcnCcTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnCcTxPort.setStatus("current")
_DcnCcRxPort_Type = PortNumber
_DcnCcRxPort_Object = MibTableColumn
dcnCcRxPort = _DcnCcRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 7, 1, 1, 7),
    _DcnCcRxPort_Type()
)
dcnCcRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnCcRxPort.setStatus("current")


class _DcnCcAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type dcnCcAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 1


_DcnCcAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_DcnCcAdminStatus_Object = MibTableColumn
dcnCcAdminStatus = _DcnCcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 7, 1, 1, 8),
    _DcnCcAdminStatus_Type()
)
dcnCcAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnCcAdminStatus.setStatus("current")


class _DcnCcChannelStatus_Type(Integer32):
    """Custom type dcnCcChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("down", 2),
          ("calling", 3),
          ("up", 4),
          ("waitToHangup", 5),
          ("broken", 6),
          ("restarting", 7))
    )


_DcnCcChannelStatus_Type.__name__ = "Integer32"
_DcnCcChannelStatus_Object = MibTableColumn
dcnCcChannelStatus = _DcnCcChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 7, 1, 1, 9),
    _DcnCcChannelStatus_Type()
)
dcnCcChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnCcChannelStatus.setStatus("current")
_DcnCcErrorCounter_Type = Counter32
_DcnCcErrorCounter_Object = MibTableColumn
dcnCcErrorCounter = _DcnCcErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 7, 1, 1, 10),
    _DcnCcErrorCounter_Type()
)
dcnCcErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnCcErrorCounter.setStatus("current")


class _DcnCcResetCounter_Type(Integer32):
    """Custom type dcnCcResetCounter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_DcnCcResetCounter_Type.__name__ = "Integer32"
_DcnCcResetCounter_Object = MibTableColumn
dcnCcResetCounter = _DcnCcResetCounter_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 7, 1, 1, 11),
    _DcnCcResetCounter_Type()
)
dcnCcResetCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnCcResetCounter.setStatus("current")
_DcnCcFecFailure_Type = FaultStatus
_DcnCcFecFailure_Object = MibTableColumn
dcnCcFecFailure = _DcnCcFecFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 7, 1, 1, 12),
    _DcnCcFecFailure_Type()
)
dcnCcFecFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnCcFecFailure.setStatus("current")
_DcnCcTrxNotSupportCommChannel_Type = FaultStatus
_DcnCcTrxNotSupportCommChannel_Object = MibTableColumn
dcnCcTrxNotSupportCommChannel = _DcnCcTrxNotSupportCommChannel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 7, 1, 1, 13),
    _DcnCcTrxNotSupportCommChannel_Type()
)
dcnCcTrxNotSupportCommChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnCcTrxNotSupportCommChannel.setStatus("current")
_DcnCcConfigurationMismatch_Type = FaultStatus
_DcnCcConfigurationMismatch_Object = MibTableColumn
dcnCcConfigurationMismatch = _DcnCcConfigurationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 7, 1, 1, 14),
    _DcnCcConfigurationMismatch_Type()
)
dcnCcConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnCcConfigurationMismatch.setStatus("current")

# Managed Objects groups

dcnGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 1)
)
dcnGeneralGroup.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralLastChangeTime"),
        ("LUM-DCN-MIB", "dcnGeneralStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    dcnGeneralGroup.setStatus("deprecated")

dcnIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 2)
)
dcnIfGroup.setObjects(
      *(("LUM-DCN-MIB", "dcnIfIndex"),
        ("LUM-DCN-MIB", "dcnIfName"),
        ("LUM-DCN-MIB", "dcnIfDescr"),
        ("LUM-DCN-MIB", "dcnIfSubrack"),
        ("LUM-DCN-MIB", "dcnIfSlot"),
        ("LUM-DCN-MIB", "dcnIfTxPort"),
        ("LUM-DCN-MIB", "dcnIfRxPort"),
        ("LUM-DCN-MIB", "dcnIfInvPhysIndexOrZero"),
        ("LUM-DCN-MIB", "dcnIfType"),
        ("LUM-DCN-MIB", "dcnIfMaxSpeed"),
        ("LUM-DCN-MIB", "dcnIfOscMode"),
        ("LUM-DCN-MIB", "dcnIfAdminStatus"),
        ("LUM-DCN-MIB", "dcnIfOperStatus"),
        ("LUM-DCN-MIB", "dcnIfTxSignalStatus"),
        ("LUM-DCN-MIB", "dcnIfLinkDown"))
)
if mibBuilder.loadTexts:
    dcnIfGroup.setStatus("deprecated")

dcnPppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 4)
)
dcnPppGroup.setObjects(
      *(("LUM-DCN-MIB", "dcnPppIndex"),
        ("LUM-DCN-MIB", "dcnPppName"),
        ("LUM-DCN-MIB", "dcnPppDescr"),
        ("LUM-DCN-MIB", "dcnPppTxSubrack"),
        ("LUM-DCN-MIB", "dcnPppTxSlot"),
        ("LUM-DCN-MIB", "dcnPppTxPort"),
        ("LUM-DCN-MIB", "dcnPppRxSubrack"),
        ("LUM-DCN-MIB", "dcnPppRxSlot"),
        ("LUM-DCN-MIB", "dcnPppRxPort"),
        ("LUM-DCN-MIB", "dcnPppInvPhysIndexOrZero"),
        ("LUM-DCN-MIB", "dcnPppType"),
        ("LUM-DCN-MIB", "dcnPppAdminStatus"))
)
if mibBuilder.loadTexts:
    dcnPppGroup.setStatus("deprecated")

dcnPppGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 5)
)
dcnPppGroupV2.setObjects(
      *(("LUM-DCN-MIB", "dcnPppIndex"),
        ("LUM-DCN-MIB", "dcnPppName"),
        ("LUM-DCN-MIB", "dcnPppDescr"),
        ("LUM-DCN-MIB", "dcnPppTxSubrack"),
        ("LUM-DCN-MIB", "dcnPppTxSlot"),
        ("LUM-DCN-MIB", "dcnPppTxPort"),
        ("LUM-DCN-MIB", "dcnPppRxSubrack"),
        ("LUM-DCN-MIB", "dcnPppRxSlot"),
        ("LUM-DCN-MIB", "dcnPppRxPort"),
        ("LUM-DCN-MIB", "dcnPppInvPhysIndexOrZero"),
        ("LUM-DCN-MIB", "dcnPppType"),
        ("LUM-DCN-MIB", "dcnPppAdminStatus"),
        ("LUM-DCN-MIB", "dcnPppOperStatus"))
)
if mibBuilder.loadTexts:
    dcnPppGroupV2.setStatus("deprecated")

dcnAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 6)
)
dcnAddressGroup.setObjects(
      *(("LUM-DCN-MIB", "dcnAddressCurrentPppAddress"),
        ("LUM-DCN-MIB", "dcnAddressNextPppAddress"))
)
if mibBuilder.loadTexts:
    dcnAddressGroup.setStatus("current")

dcnPppGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 7)
)
dcnPppGroupV3.setObjects(
      *(("LUM-DCN-MIB", "dcnPppIndex"),
        ("LUM-DCN-MIB", "dcnPppName"),
        ("LUM-DCN-MIB", "dcnPppDescr"),
        ("LUM-DCN-MIB", "dcnPppTxSubrack"),
        ("LUM-DCN-MIB", "dcnPppTxSlot"),
        ("LUM-DCN-MIB", "dcnPppTxPort"),
        ("LUM-DCN-MIB", "dcnPppRxSubrack"),
        ("LUM-DCN-MIB", "dcnPppRxSlot"),
        ("LUM-DCN-MIB", "dcnPppRxPort"),
        ("LUM-DCN-MIB", "dcnPppInvPhysIndexOrZero"),
        ("LUM-DCN-MIB", "dcnPppType"),
        ("LUM-DCN-MIB", "dcnPppAdminStatus"),
        ("LUM-DCN-MIB", "dcnPppOperStatus"),
        ("LUM-DCN-MIB", "dcnPppDialCommand"),
        ("LUM-DCN-MIB", "dcnPppAcceptCommand"))
)
if mibBuilder.loadTexts:
    dcnPppGroupV3.setStatus("deprecated")

dcnPppGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 8)
)
dcnPppGroupV4.setObjects(
      *(("LUM-DCN-MIB", "dcnPppIndex"),
        ("LUM-DCN-MIB", "dcnPppName"),
        ("LUM-DCN-MIB", "dcnPppDescr"),
        ("LUM-DCN-MIB", "dcnPppTxSubrack"),
        ("LUM-DCN-MIB", "dcnPppTxSlot"),
        ("LUM-DCN-MIB", "dcnPppTxPort"),
        ("LUM-DCN-MIB", "dcnPppRxSubrack"),
        ("LUM-DCN-MIB", "dcnPppRxSlot"),
        ("LUM-DCN-MIB", "dcnPppRxPort"),
        ("LUM-DCN-MIB", "dcnPppInvPhysIndexOrZero"),
        ("LUM-DCN-MIB", "dcnPppType"),
        ("LUM-DCN-MIB", "dcnPppAdminStatus"),
        ("LUM-DCN-MIB", "dcnPppOperStatus"),
        ("LUM-DCN-MIB", "dcnPppDialCommand"),
        ("LUM-DCN-MIB", "dcnPppAcceptCommand"),
        ("LUM-DCN-MIB", "dcnPppLogicalLinkId"))
)
if mibBuilder.loadTexts:
    dcnPppGroupV4.setStatus("deprecated")

dcnGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 9)
)
dcnGeneralGroupV2.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralLastChangeTime"),
        ("LUM-DCN-MIB", "dcnGeneralStateLastChangeTime"),
        ("LUM-DCN-MIB", "dcnGeneralDcnIfTableSize"),
        ("LUM-DCN-MIB", "dcnGeneralDcnPppTableSize"))
)
if mibBuilder.loadTexts:
    dcnGeneralGroupV2.setStatus("deprecated")

dcnIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 10)
)
dcnIfGroupV2.setObjects(
      *(("LUM-DCN-MIB", "dcnIfIndex"),
        ("LUM-DCN-MIB", "dcnIfName"),
        ("LUM-DCN-MIB", "dcnIfDescr"),
        ("LUM-DCN-MIB", "dcnIfSubrack"),
        ("LUM-DCN-MIB", "dcnIfSlot"),
        ("LUM-DCN-MIB", "dcnIfTxPort"),
        ("LUM-DCN-MIB", "dcnIfRxPort"),
        ("LUM-DCN-MIB", "dcnIfInvPhysIndexOrZero"),
        ("LUM-DCN-MIB", "dcnIfType"),
        ("LUM-DCN-MIB", "dcnIfMaxSpeed"),
        ("LUM-DCN-MIB", "dcnIfOscMode"),
        ("LUM-DCN-MIB", "dcnIfAdminStatus"),
        ("LUM-DCN-MIB", "dcnIfOperStatus"),
        ("LUM-DCN-MIB", "dcnIfTxSignalStatus"),
        ("LUM-DCN-MIB", "dcnIfLinkDown"),
        ("LUM-DCN-MIB", "dcnIfTxFrequency"),
        ("LUM-DCN-MIB", "dcnIfObjectProperty"))
)
if mibBuilder.loadTexts:
    dcnIfGroupV2.setStatus("deprecated")

dcnPppGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 11)
)
dcnPppGroupV5.setObjects(
      *(("LUM-DCN-MIB", "dcnPppIndex"),
        ("LUM-DCN-MIB", "dcnPppName"),
        ("LUM-DCN-MIB", "dcnPppDescr"),
        ("LUM-DCN-MIB", "dcnPppTxSubrack"),
        ("LUM-DCN-MIB", "dcnPppTxSlot"),
        ("LUM-DCN-MIB", "dcnPppTxPort"),
        ("LUM-DCN-MIB", "dcnPppRxSubrack"),
        ("LUM-DCN-MIB", "dcnPppRxSlot"),
        ("LUM-DCN-MIB", "dcnPppRxPort"),
        ("LUM-DCN-MIB", "dcnPppInvPhysIndexOrZero"),
        ("LUM-DCN-MIB", "dcnPppType"),
        ("LUM-DCN-MIB", "dcnPppAdminStatus"),
        ("LUM-DCN-MIB", "dcnPppOperStatus"),
        ("LUM-DCN-MIB", "dcnPppRouteName"),
        ("LUM-DCN-MIB", "dcnPppDialCommand"),
        ("LUM-DCN-MIB", "dcnPppAcceptCommand"),
        ("LUM-DCN-MIB", "dcnPppLogicalLinkId"),
        ("LUM-DCN-MIB", "dcnPppObjectProperty"))
)
if mibBuilder.loadTexts:
    dcnPppGroupV5.setStatus("deprecated")

dcnIfGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 12)
)
dcnIfGroupV3.setObjects(
      *(("LUM-DCN-MIB", "dcnIfIndex"),
        ("LUM-DCN-MIB", "dcnIfName"),
        ("LUM-DCN-MIB", "dcnIfDescr"),
        ("LUM-DCN-MIB", "dcnIfSubrack"),
        ("LUM-DCN-MIB", "dcnIfSlot"),
        ("LUM-DCN-MIB", "dcnIfTxPort"),
        ("LUM-DCN-MIB", "dcnIfRxPort"),
        ("LUM-DCN-MIB", "dcnIfInvPhysIndexOrZero"),
        ("LUM-DCN-MIB", "dcnIfType"),
        ("LUM-DCN-MIB", "dcnIfMaxSpeed"),
        ("LUM-DCN-MIB", "dcnIfOscMode"),
        ("LUM-DCN-MIB", "dcnIfAdminStatus"),
        ("LUM-DCN-MIB", "dcnIfOperStatus"),
        ("LUM-DCN-MIB", "dcnIfTxSignalStatus"),
        ("LUM-DCN-MIB", "dcnIfLinkDown"),
        ("LUM-DCN-MIB", "dcnIfTxFrequency"),
        ("LUM-DCN-MIB", "dcnIfObjectProperty"),
        ("LUM-DCN-MIB", "dcnIfLaserStatus"),
        ("LUM-DCN-MIB", "dcnIfHighSpeedMin"),
        ("LUM-DCN-MIB", "dcnIfHighSpeedMax"),
        ("LUM-DCN-MIB", "dcnIfTrxClass"),
        ("LUM-DCN-MIB", "dcnIfReceiverSensitivity"),
        ("LUM-DCN-MIB", "dcnIfPowerLevelLowRelativeThreshold"),
        ("LUM-DCN-MIB", "dcnIfPowerLevel"),
        ("LUM-DCN-MIB", "dcnIfTxPowerLevel"),
        ("LUM-DCN-MIB", "dcnIfLaserTempActual"),
        ("LUM-DCN-MIB", "dcnIfExpectedTxFrequency"),
        ("LUM-DCN-MIB", "dcnIfLaserBias"),
        ("LUM-DCN-MIB", "dcnIfLossOfSignal"),
        ("LUM-DCN-MIB", "dcnIfTrxBitrateUnavailable"),
        ("LUM-DCN-MIB", "dcnIfTrxMissing"),
        ("LUM-DCN-MIB", "dcnIfTrxCodeMismatch"),
        ("LUM-DCN-MIB", "dcnIfTransmitterFailed"),
        ("LUM-DCN-MIB", "dcnIfIllegalFrequency"),
        ("LUM-DCN-MIB", "dcnIfUnexpectedTxFrequency"),
        ("LUM-DCN-MIB", "dcnIfReceivedPowerHigh"),
        ("LUM-DCN-MIB", "dcnIfReceivedPowerLow"),
        ("LUM-DCN-MIB", "dcnIfTrxMediaMismatch"))
)
if mibBuilder.loadTexts:
    dcnIfGroupV3.setStatus("deprecated")

dcnIfGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 13)
)
dcnIfGroupV4.setObjects(
      *(("LUM-DCN-MIB", "dcnIfIndex"),
        ("LUM-DCN-MIB", "dcnIfName"),
        ("LUM-DCN-MIB", "dcnIfDescr"),
        ("LUM-DCN-MIB", "dcnIfSubrack"),
        ("LUM-DCN-MIB", "dcnIfSlot"),
        ("LUM-DCN-MIB", "dcnIfTxPort"),
        ("LUM-DCN-MIB", "dcnIfRxPort"),
        ("LUM-DCN-MIB", "dcnIfInvPhysIndexOrZero"),
        ("LUM-DCN-MIB", "dcnIfType"),
        ("LUM-DCN-MIB", "dcnIfMaxSpeed"),
        ("LUM-DCN-MIB", "dcnIfOscMode"),
        ("LUM-DCN-MIB", "dcnIfAdminStatus"),
        ("LUM-DCN-MIB", "dcnIfOperStatus"),
        ("LUM-DCN-MIB", "dcnIfTxSignalStatus"),
        ("LUM-DCN-MIB", "dcnIfLinkDown"),
        ("LUM-DCN-MIB", "dcnIfTxFrequency"),
        ("LUM-DCN-MIB", "dcnIfObjectProperty"),
        ("LUM-DCN-MIB", "dcnIfLaserStatus"),
        ("LUM-DCN-MIB", "dcnIfHighSpeedMin"),
        ("LUM-DCN-MIB", "dcnIfHighSpeedMax"),
        ("LUM-DCN-MIB", "dcnIfTrxClass"),
        ("LUM-DCN-MIB", "dcnIfReceiverSensitivity"),
        ("LUM-DCN-MIB", "dcnIfPowerLevelLowRelativeThreshold"),
        ("LUM-DCN-MIB", "dcnIfPowerLevel"),
        ("LUM-DCN-MIB", "dcnIfTxPowerLevel"),
        ("LUM-DCN-MIB", "dcnIfLaserTempActual"),
        ("LUM-DCN-MIB", "dcnIfExpectedTxFrequency"),
        ("LUM-DCN-MIB", "dcnIfLaserBias"),
        ("LUM-DCN-MIB", "dcnIfLossOfSignal"),
        ("LUM-DCN-MIB", "dcnIfTrxBitrateUnavailable"),
        ("LUM-DCN-MIB", "dcnIfTrxMissing"),
        ("LUM-DCN-MIB", "dcnIfTrxCodeMismatch"),
        ("LUM-DCN-MIB", "dcnIfTransmitterFailed"),
        ("LUM-DCN-MIB", "dcnIfIllegalFrequency"),
        ("LUM-DCN-MIB", "dcnIfUnexpectedTxFrequency"),
        ("LUM-DCN-MIB", "dcnIfReceivedPowerHigh"),
        ("LUM-DCN-MIB", "dcnIfReceivedPowerLow"),
        ("LUM-DCN-MIB", "dcnIfTrxMediaMismatch"),
        ("LUM-DCN-MIB", "dcnIfProtocolVersionMismatch"),
        ("LUM-DCN-MIB", "dcnIfRemoteDefectIndication"),
        ("LUM-DCN-MIB", "dcnIfTraceTransmitted"),
        ("LUM-DCN-MIB", "dcnIfTraceReceived"),
        ("LUM-DCN-MIB", "dcnIfTraceExpected"),
        ("LUM-DCN-MIB", "dcnIfTraceAlarmMode"),
        ("LUM-DCN-MIB", "dcnIfTraceMismatch"),
        ("LUM-DCN-MIB", "dcnIfLaserMode"),
        ("LUM-DCN-MIB", "dcnIfLinkSupervisionFailure"))
)
if mibBuilder.loadTexts:
    dcnIfGroupV4.setStatus("deprecated")

dcnPppGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 14)
)
dcnPppGroupV6.setObjects(
      *(("LUM-DCN-MIB", "dcnPppIndex"),
        ("LUM-DCN-MIB", "dcnPppName"),
        ("LUM-DCN-MIB", "dcnPppDescr"),
        ("LUM-DCN-MIB", "dcnPppTxSubrack"),
        ("LUM-DCN-MIB", "dcnPppTxSlot"),
        ("LUM-DCN-MIB", "dcnPppTxPort"),
        ("LUM-DCN-MIB", "dcnPppRxSubrack"),
        ("LUM-DCN-MIB", "dcnPppRxSlot"),
        ("LUM-DCN-MIB", "dcnPppRxPort"),
        ("LUM-DCN-MIB", "dcnPppInvPhysIndexOrZero"),
        ("LUM-DCN-MIB", "dcnPppType"),
        ("LUM-DCN-MIB", "dcnPppAdminStatus"),
        ("LUM-DCN-MIB", "dcnPppOperStatus"),
        ("LUM-DCN-MIB", "dcnPppRouteName"),
        ("LUM-DCN-MIB", "dcnPppDialCommand"),
        ("LUM-DCN-MIB", "dcnPppAcceptCommand"),
        ("LUM-DCN-MIB", "dcnPppLogicalLinkId"),
        ("LUM-DCN-MIB", "dcnPppObjectProperty"),
        ("LUM-DCN-MIB", "dcnPppGccChannel"))
)
if mibBuilder.loadTexts:
    dcnPppGroupV6.setStatus("deprecated")

dcnEthGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 15)
)
dcnEthGroupV1.setObjects(
      *(("LUM-DCN-MIB", "dcnEthIndex"),
        ("LUM-DCN-MIB", "dcnEthName"),
        ("LUM-DCN-MIB", "dcnEthDescr"),
        ("LUM-DCN-MIB", "dcnEthSubrack"),
        ("LUM-DCN-MIB", "dcnEthSlot"),
        ("LUM-DCN-MIB", "dcnEthPort"),
        ("LUM-DCN-MIB", "dcnEthAutoNegotiationMode"),
        ("LUM-DCN-MIB", "dcnEthLinkStatus"),
        ("LUM-DCN-MIB", "dcnEthSpeed"),
        ("LUM-DCN-MIB", "dcnEthDuplexCapability"),
        ("LUM-DCN-MIB", "dcnEthRateLimit"),
        ("LUM-DCN-MIB", "dcnEthFlowControlMode"),
        ("LUM-DCN-MIB", "dcnEthObjectProperty"))
)
if mibBuilder.loadTexts:
    dcnEthGroupV1.setStatus("deprecated")

dcnGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 16)
)
dcnGeneralGroupV3.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralLastChangeTime"),
        ("LUM-DCN-MIB", "dcnGeneralStateLastChangeTime"),
        ("LUM-DCN-MIB", "dcnGeneralDcnIfTableSize"),
        ("LUM-DCN-MIB", "dcnGeneralDcnPppTableSize"))
)
if mibBuilder.loadTexts:
    dcnGeneralGroupV3.setStatus("current")

dcnEthGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 17)
)
dcnEthGroupV2.setObjects(
      *(("LUM-DCN-MIB", "dcnEthIndex"),
        ("LUM-DCN-MIB", "dcnEthName"),
        ("LUM-DCN-MIB", "dcnEthDescr"),
        ("LUM-DCN-MIB", "dcnEthSubrack"),
        ("LUM-DCN-MIB", "dcnEthSlot"),
        ("LUM-DCN-MIB", "dcnEthPort"),
        ("LUM-DCN-MIB", "dcnEthAutoNegotiationMode"),
        ("LUM-DCN-MIB", "dcnEthLinkStatus"),
        ("LUM-DCN-MIB", "dcnEthSpeed"),
        ("LUM-DCN-MIB", "dcnEthDuplexCapability"),
        ("LUM-DCN-MIB", "dcnEthRateLimit"),
        ("LUM-DCN-MIB", "dcnEthFlowControlMode"),
        ("LUM-DCN-MIB", "dcnEthObjectProperty"),
        ("LUM-DCN-MIB", "dcnEthChangeSpeedCommand"))
)
if mibBuilder.loadTexts:
    dcnEthGroupV2.setStatus("deprecated")

dcnCcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 18)
)
dcnCcGroup.setObjects(
      *(("LUM-DCN-MIB", "dcnCcIndex"),
        ("LUM-DCN-MIB", "dcnCcName"),
        ("LUM-DCN-MIB", "dcnCcDescr"),
        ("LUM-DCN-MIB", "dcnCcSubrack"),
        ("LUM-DCN-MIB", "dcnCcSlot"),
        ("LUM-DCN-MIB", "dcnCcTxPort"),
        ("LUM-DCN-MIB", "dcnCcRxPort"),
        ("LUM-DCN-MIB", "dcnCcAdminStatus"),
        ("LUM-DCN-MIB", "dcnCcChannelStatus"),
        ("LUM-DCN-MIB", "dcnCcErrorCounter"),
        ("LUM-DCN-MIB", "dcnCcResetCounter"),
        ("LUM-DCN-MIB", "dcnCcFecFailure"),
        ("LUM-DCN-MIB", "dcnCcTrxNotSupportCommChannel"),
        ("LUM-DCN-MIB", "dcnCcConfigurationMismatch"))
)
if mibBuilder.loadTexts:
    dcnCcGroup.setStatus("current")

dcnIfGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 19)
)
dcnIfGroupV5.setObjects(
      *(("LUM-DCN-MIB", "dcnIfIndex"),
        ("LUM-DCN-MIB", "dcnIfName"),
        ("LUM-DCN-MIB", "dcnIfDescr"),
        ("LUM-DCN-MIB", "dcnIfSubrack"),
        ("LUM-DCN-MIB", "dcnIfSlot"),
        ("LUM-DCN-MIB", "dcnIfTxPort"),
        ("LUM-DCN-MIB", "dcnIfRxPort"),
        ("LUM-DCN-MIB", "dcnIfInvPhysIndexOrZero"),
        ("LUM-DCN-MIB", "dcnIfType"),
        ("LUM-DCN-MIB", "dcnIfMaxSpeed"),
        ("LUM-DCN-MIB", "dcnIfOscMode"),
        ("LUM-DCN-MIB", "dcnIfAdminStatus"),
        ("LUM-DCN-MIB", "dcnIfOperStatus"),
        ("LUM-DCN-MIB", "dcnIfTxSignalStatus"),
        ("LUM-DCN-MIB", "dcnIfLinkDown"),
        ("LUM-DCN-MIB", "dcnIfTxFrequency"),
        ("LUM-DCN-MIB", "dcnIfObjectProperty"),
        ("LUM-DCN-MIB", "dcnIfLaserStatus"),
        ("LUM-DCN-MIB", "dcnIfHighSpeedMin"),
        ("LUM-DCN-MIB", "dcnIfHighSpeedMax"),
        ("LUM-DCN-MIB", "dcnIfTrxClass"),
        ("LUM-DCN-MIB", "dcnIfReceiverSensitivity"),
        ("LUM-DCN-MIB", "dcnIfPowerLevelLowRelativeThreshold"),
        ("LUM-DCN-MIB", "dcnIfPowerLevel"),
        ("LUM-DCN-MIB", "dcnIfTxPowerLevel"),
        ("LUM-DCN-MIB", "dcnIfLaserTempActual"),
        ("LUM-DCN-MIB", "dcnIfExpectedTxFrequency"),
        ("LUM-DCN-MIB", "dcnIfLaserBias"),
        ("LUM-DCN-MIB", "dcnIfLossOfSignal"),
        ("LUM-DCN-MIB", "dcnIfTrxBitrateUnavailable"),
        ("LUM-DCN-MIB", "dcnIfTrxMissing"),
        ("LUM-DCN-MIB", "dcnIfTrxCodeMismatch"),
        ("LUM-DCN-MIB", "dcnIfTransmitterFailed"),
        ("LUM-DCN-MIB", "dcnIfIllegalFrequency"),
        ("LUM-DCN-MIB", "dcnIfUnexpectedTxFrequency"),
        ("LUM-DCN-MIB", "dcnIfReceivedPowerHigh"),
        ("LUM-DCN-MIB", "dcnIfReceivedPowerLow"),
        ("LUM-DCN-MIB", "dcnIfTrxMediaMismatch"),
        ("LUM-DCN-MIB", "dcnIfProtocolVersionMismatch"),
        ("LUM-DCN-MIB", "dcnIfRemoteDefectIndication"),
        ("LUM-DCN-MIB", "dcnIfTraceTransmitted"),
        ("LUM-DCN-MIB", "dcnIfTraceReceived"),
        ("LUM-DCN-MIB", "dcnIfTraceExpected"),
        ("LUM-DCN-MIB", "dcnIfTraceAlarmMode"),
        ("LUM-DCN-MIB", "dcnIfTraceMismatch"),
        ("LUM-DCN-MIB", "dcnIfLaserMode"),
        ("LUM-DCN-MIB", "dcnIfLinkSupervisionFailure"),
        ("LUM-DCN-MIB", "dcnIfAid"),
        ("LUM-DCN-MIB", "dcnIfPhysicalLocation"))
)
if mibBuilder.loadTexts:
    dcnIfGroupV5.setStatus("current")

dcnPppGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 20)
)
dcnPppGroupV7.setObjects(
      *(("LUM-DCN-MIB", "dcnPppIndex"),
        ("LUM-DCN-MIB", "dcnPppName"),
        ("LUM-DCN-MIB", "dcnPppDescr"),
        ("LUM-DCN-MIB", "dcnPppTxSubrack"),
        ("LUM-DCN-MIB", "dcnPppTxSlot"),
        ("LUM-DCN-MIB", "dcnPppTxPort"),
        ("LUM-DCN-MIB", "dcnPppRxSubrack"),
        ("LUM-DCN-MIB", "dcnPppRxSlot"),
        ("LUM-DCN-MIB", "dcnPppRxPort"),
        ("LUM-DCN-MIB", "dcnPppInvPhysIndexOrZero"),
        ("LUM-DCN-MIB", "dcnPppType"),
        ("LUM-DCN-MIB", "dcnPppAdminStatus"),
        ("LUM-DCN-MIB", "dcnPppOperStatus"),
        ("LUM-DCN-MIB", "dcnPppRouteName"),
        ("LUM-DCN-MIB", "dcnPppDialCommand"),
        ("LUM-DCN-MIB", "dcnPppAcceptCommand"),
        ("LUM-DCN-MIB", "dcnPppLogicalLinkId"),
        ("LUM-DCN-MIB", "dcnPppObjectProperty"),
        ("LUM-DCN-MIB", "dcnPppGccChannel"),
        ("LUM-DCN-MIB", "dcnPppVlanId"),
        ("LUM-DCN-MIB", "dcnPppVlanEtherType"))
)
if mibBuilder.loadTexts:
    dcnPppGroupV7.setStatus("deprecated")

dcnEthGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 21)
)
dcnEthGroupV3.setObjects(
      *(("LUM-DCN-MIB", "dcnEthIndex"),
        ("LUM-DCN-MIB", "dcnEthName"),
        ("LUM-DCN-MIB", "dcnEthDescr"),
        ("LUM-DCN-MIB", "dcnEthSubrack"),
        ("LUM-DCN-MIB", "dcnEthSlot"),
        ("LUM-DCN-MIB", "dcnEthPort"),
        ("LUM-DCN-MIB", "dcnEthAutoNegotiationMode"),
        ("LUM-DCN-MIB", "dcnEthLinkStatus"),
        ("LUM-DCN-MIB", "dcnEthSpeed"),
        ("LUM-DCN-MIB", "dcnEthDuplexCapability"),
        ("LUM-DCN-MIB", "dcnEthRateLimit"),
        ("LUM-DCN-MIB", "dcnEthFlowControlMode"),
        ("LUM-DCN-MIB", "dcnEthObjectProperty"),
        ("LUM-DCN-MIB", "dcnEthChangeSpeedCommand"),
        ("LUM-DCN-MIB", "dcnEthAdminStatus"),
        ("LUM-DCN-MIB", "dcnEthOperStatus"))
)
if mibBuilder.loadTexts:
    dcnEthGroupV3.setStatus("current")

dcnPppGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 22)
)
dcnPppGroupV8.setObjects(
      *(("LUM-DCN-MIB", "dcnPppIndex"),
        ("LUM-DCN-MIB", "dcnPppName"),
        ("LUM-DCN-MIB", "dcnPppDescr"),
        ("LUM-DCN-MIB", "dcnPppTxSubrack"),
        ("LUM-DCN-MIB", "dcnPppTxSlot"),
        ("LUM-DCN-MIB", "dcnPppTxIfNo"),
        ("LUM-DCN-MIB", "dcnPppTxPort"),
        ("LUM-DCN-MIB", "dcnPppRxSubrack"),
        ("LUM-DCN-MIB", "dcnPppRxSlot"),
        ("LUM-DCN-MIB", "dcnPppRxIfNo"),
        ("LUM-DCN-MIB", "dcnPppRxPort"),
        ("LUM-DCN-MIB", "dcnPppInvPhysIndexOrZero"),
        ("LUM-DCN-MIB", "dcnPppType"),
        ("LUM-DCN-MIB", "dcnPppAdminStatus"),
        ("LUM-DCN-MIB", "dcnPppOperStatus"),
        ("LUM-DCN-MIB", "dcnPppRouteName"),
        ("LUM-DCN-MIB", "dcnPppDialCommand"),
        ("LUM-DCN-MIB", "dcnPppAcceptCommand"),
        ("LUM-DCN-MIB", "dcnPppLogicalLinkId"),
        ("LUM-DCN-MIB", "dcnPppObjectProperty"),
        ("LUM-DCN-MIB", "dcnPppGccChannel"),
        ("LUM-DCN-MIB", "dcnPppVlanId"),
        ("LUM-DCN-MIB", "dcnPppVlanEtherType"))
)
if mibBuilder.loadTexts:
    dcnPppGroupV8.setStatus("current")


# Notification objects

dcnIfTxSignalStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 3, 0, 1)
)
dcnIfTxSignalStatusDown.setObjects(
      *(("LUM-DCN-MIB", "dcnIfIndex"),
        ("LUM-DCN-MIB", "dcnIfName"),
        ("LUM-DCN-MIB", "dcnIfSubrack"),
        ("LUM-DCN-MIB", "dcnIfSlot"),
        ("LUM-DCN-MIB", "dcnIfTxPort"),
        ("LUM-DCN-MIB", "dcnIfRxPort"),
        ("LUM-DCN-MIB", "dcnIfTxSignalStatus"))
)
if mibBuilder.loadTexts:
    dcnIfTxSignalStatusDown.setStatus(
        "current"
    )

dcnIfTxSignalStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 2, 3, 0, 2)
)
dcnIfTxSignalStatusUp.setObjects(
      *(("LUM-DCN-MIB", "dcnIfIndex"),
        ("LUM-DCN-MIB", "dcnIfName"),
        ("LUM-DCN-MIB", "dcnIfSubrack"),
        ("LUM-DCN-MIB", "dcnIfSlot"),
        ("LUM-DCN-MIB", "dcnIfTxPort"),
        ("LUM-DCN-MIB", "dcnIfRxPort"),
        ("LUM-DCN-MIB", "dcnIfTxSignalStatus"))
)
if mibBuilder.loadTexts:
    dcnIfTxSignalStatusUp.setStatus(
        "current"
    )


# Notifications groups

dcnNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 1, 3)
)
dcnNotificationGroup.setObjects(
      *(("LUM-DCN-MIB", "dcnIfTxSignalStatusDown"),
        ("LUM-DCN-MIB", "dcnIfTxSignalStatusUp"))
)
if mibBuilder.loadTexts:
    dcnNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lumDcnBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 2, 1)
)
lumDcnBasicComplV1.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralGroup"),
        ("LUM-DCN-MIB", "dcnIfGroup"),
        ("LUM-DCN-MIB", "dcnNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumDcnBasicComplV1.setStatus(
        "deprecated"
    )

lumDcnBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 2, 2)
)
lumDcnBasicComplV2.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralGroup"),
        ("LUM-DCN-MIB", "dcnIfGroup"),
        ("LUM-DCN-MIB", "dcnNotificationGroup"),
        ("LUM-DCN-MIB", "dcnPppGroup"))
)
if mibBuilder.loadTexts:
    lumDcnBasicComplV2.setStatus(
        "deprecated"
    )

lumDcnBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 2, 3)
)
lumDcnBasicComplV3.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralGroup"),
        ("LUM-DCN-MIB", "dcnIfGroup"),
        ("LUM-DCN-MIB", "dcnNotificationGroup"),
        ("LUM-DCN-MIB", "dcnPppGroupV2"))
)
if mibBuilder.loadTexts:
    lumDcnBasicComplV3.setStatus(
        "deprecated"
    )

lumDcnBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 2, 4)
)
lumDcnBasicComplV4.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralGroup"),
        ("LUM-DCN-MIB", "dcnIfGroup"),
        ("LUM-DCN-MIB", "dcnNotificationGroup"),
        ("LUM-DCN-MIB", "dcnPppGroupV2"),
        ("LUM-DCN-MIB", "dcnAddressGroup"))
)
if mibBuilder.loadTexts:
    lumDcnBasicComplV4.setStatus(
        "deprecated"
    )

lumDcnBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 2, 5)
)
lumDcnBasicComplV5.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralGroup"),
        ("LUM-DCN-MIB", "dcnIfGroup"),
        ("LUM-DCN-MIB", "dcnNotificationGroup"),
        ("LUM-DCN-MIB", "dcnPppGroupV3"),
        ("LUM-DCN-MIB", "dcnAddressGroup"))
)
if mibBuilder.loadTexts:
    lumDcnBasicComplV5.setStatus(
        "deprecated"
    )

lumDcnBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 2, 6)
)
lumDcnBasicComplV6.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralGroupV2"),
        ("LUM-DCN-MIB", "dcnIfGroup"),
        ("LUM-DCN-MIB", "dcnNotificationGroup"),
        ("LUM-DCN-MIB", "dcnPppGroupV4"),
        ("LUM-DCN-MIB", "dcnAddressGroup"))
)
if mibBuilder.loadTexts:
    lumDcnBasicComplV6.setStatus(
        "deprecated"
    )

lumDcnBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 2, 7)
)
lumDcnBasicComplV7.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralGroupV2"),
        ("LUM-DCN-MIB", "dcnIfGroupV2"),
        ("LUM-DCN-MIB", "dcnNotificationGroup"),
        ("LUM-DCN-MIB", "dcnPppGroupV5"),
        ("LUM-DCN-MIB", "dcnAddressGroup"))
)
if mibBuilder.loadTexts:
    lumDcnBasicComplV7.setStatus(
        "deprecated"
    )

lumDcnBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 2, 8)
)
lumDcnBasicComplV8.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralGroupV2"),
        ("LUM-DCN-MIB", "dcnIfGroupV3"),
        ("LUM-DCN-MIB", "dcnNotificationGroup"),
        ("LUM-DCN-MIB", "dcnPppGroupV5"),
        ("LUM-DCN-MIB", "dcnAddressGroup"))
)
if mibBuilder.loadTexts:
    lumDcnBasicComplV8.setStatus(
        "deprecated"
    )

lumDcnBasicComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 2, 9)
)
lumDcnBasicComplV9.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralGroupV2"),
        ("LUM-DCN-MIB", "dcnIfGroupV4"),
        ("LUM-DCN-MIB", "dcnNotificationGroup"),
        ("LUM-DCN-MIB", "dcnPppGroupV5"),
        ("LUM-DCN-MIB", "dcnAddressGroup"))
)
if mibBuilder.loadTexts:
    lumDcnBasicComplV9.setStatus(
        "deprecated"
    )

lumDcnBasicComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 2, 10)
)
lumDcnBasicComplV10.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralGroupV2"),
        ("LUM-DCN-MIB", "dcnIfGroupV4"),
        ("LUM-DCN-MIB", "dcnNotificationGroup"),
        ("LUM-DCN-MIB", "dcnPppGroupV6"),
        ("LUM-DCN-MIB", "dcnAddressGroup"))
)
if mibBuilder.loadTexts:
    lumDcnBasicComplV10.setStatus(
        "deprecated"
    )

lumDcnBasicComplV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 2, 11)
)
lumDcnBasicComplV11.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralGroupV2"),
        ("LUM-DCN-MIB", "dcnIfGroupV4"),
        ("LUM-DCN-MIB", "dcnNotificationGroup"),
        ("LUM-DCN-MIB", "dcnPppGroupV6"),
        ("LUM-DCN-MIB", "dcnAddressGroup"),
        ("LUM-DCN-MIB", "dcnEthGroupV1"))
)
if mibBuilder.loadTexts:
    lumDcnBasicComplV11.setStatus(
        "deprecated"
    )

lumDcnBasicComplV12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 2, 12)
)
lumDcnBasicComplV12.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralGroupV3"),
        ("LUM-DCN-MIB", "dcnIfGroupV4"),
        ("LUM-DCN-MIB", "dcnNotificationGroup"),
        ("LUM-DCN-MIB", "dcnPppGroupV6"),
        ("LUM-DCN-MIB", "dcnAddressGroup"),
        ("LUM-DCN-MIB", "dcnEthGroupV2"))
)
if mibBuilder.loadTexts:
    lumDcnBasicComplV12.setStatus(
        "deprecated"
    )

lumDcnBasicComplV13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 2, 13)
)
lumDcnBasicComplV13.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralGroupV3"),
        ("LUM-DCN-MIB", "dcnIfGroupV4"),
        ("LUM-DCN-MIB", "dcnNotificationGroup"),
        ("LUM-DCN-MIB", "dcnPppGroupV6"),
        ("LUM-DCN-MIB", "dcnAddressGroup"),
        ("LUM-DCN-MIB", "dcnEthGroupV2"),
        ("LUM-DCN-MIB", "dcnCcGroup"))
)
if mibBuilder.loadTexts:
    lumDcnBasicComplV13.setStatus(
        "deprecated"
    )

lumDcnBasicComplV14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 2, 14)
)
lumDcnBasicComplV14.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralGroupV3"),
        ("LUM-DCN-MIB", "dcnIfGroupV5"),
        ("LUM-DCN-MIB", "dcnNotificationGroup"),
        ("LUM-DCN-MIB", "dcnPppGroupV6"),
        ("LUM-DCN-MIB", "dcnAddressGroup"),
        ("LUM-DCN-MIB", "dcnEthGroupV2"),
        ("LUM-DCN-MIB", "dcnCcGroup"))
)
if mibBuilder.loadTexts:
    lumDcnBasicComplV14.setStatus(
        "deprecated"
    )

lumDcnBasicComplV15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 2, 15)
)
lumDcnBasicComplV15.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralGroupV3"),
        ("LUM-DCN-MIB", "dcnIfGroupV5"),
        ("LUM-DCN-MIB", "dcnNotificationGroup"),
        ("LUM-DCN-MIB", "dcnPppGroupV7"),
        ("LUM-DCN-MIB", "dcnAddressGroup"),
        ("LUM-DCN-MIB", "dcnEthGroupV3"),
        ("LUM-DCN-MIB", "dcnCcGroup"))
)
if mibBuilder.loadTexts:
    lumDcnBasicComplV15.setStatus(
        "deprecated"
    )

lumDcnBasicComplV16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 2, 16)
)
lumDcnBasicComplV16.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralGroupV3"),
        ("LUM-DCN-MIB", "dcnIfGroupV5"),
        ("LUM-DCN-MIB", "dcnNotificationGroup"),
        ("LUM-DCN-MIB", "dcnPppGroupV7"),
        ("LUM-DCN-MIB", "dcnAddressGroup"),
        ("LUM-DCN-MIB", "dcnEthGroupV3"),
        ("LUM-DCN-MIB", "dcnCcGroup"))
)
if mibBuilder.loadTexts:
    lumDcnBasicComplV16.setStatus(
        "deprecated"
    )

lumDcnBasicComplV17 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20, 1, 2, 17)
)
lumDcnBasicComplV17.setObjects(
      *(("LUM-DCN-MIB", "dcnGeneralGroupV3"),
        ("LUM-DCN-MIB", "dcnIfGroupV5"),
        ("LUM-DCN-MIB", "dcnNotificationGroup"),
        ("LUM-DCN-MIB", "dcnPppGroupV8"),
        ("LUM-DCN-MIB", "dcnAddressGroup"),
        ("LUM-DCN-MIB", "dcnEthGroupV3"),
        ("LUM-DCN-MIB", "dcnCcGroup"))
)
if mibBuilder.loadTexts:
    lumDcnBasicComplV17.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-DCN-MIB",
    **{"DcnSignalType": DcnSignalType,
       "DcnOscMode": DcnOscMode,
       "lumDcnMIBModule": lumDcnMIBModule,
       "lumDcnConfs": lumDcnConfs,
       "lumDcnGroups": lumDcnGroups,
       "dcnGeneralGroup": dcnGeneralGroup,
       "dcnIfGroup": dcnIfGroup,
       "dcnNotificationGroup": dcnNotificationGroup,
       "dcnPppGroup": dcnPppGroup,
       "dcnPppGroupV2": dcnPppGroupV2,
       "dcnAddressGroup": dcnAddressGroup,
       "dcnPppGroupV3": dcnPppGroupV3,
       "dcnPppGroupV4": dcnPppGroupV4,
       "dcnGeneralGroupV2": dcnGeneralGroupV2,
       "dcnIfGroupV2": dcnIfGroupV2,
       "dcnPppGroupV5": dcnPppGroupV5,
       "dcnIfGroupV3": dcnIfGroupV3,
       "dcnIfGroupV4": dcnIfGroupV4,
       "dcnPppGroupV6": dcnPppGroupV6,
       "dcnEthGroupV1": dcnEthGroupV1,
       "dcnGeneralGroupV3": dcnGeneralGroupV3,
       "dcnEthGroupV2": dcnEthGroupV2,
       "dcnCcGroup": dcnCcGroup,
       "dcnIfGroupV5": dcnIfGroupV5,
       "dcnPppGroupV7": dcnPppGroupV7,
       "dcnEthGroupV3": dcnEthGroupV3,
       "dcnPppGroupV8": dcnPppGroupV8,
       "lumDcnCompl": lumDcnCompl,
       "lumDcnBasicComplV1": lumDcnBasicComplV1,
       "lumDcnBasicComplV2": lumDcnBasicComplV2,
       "lumDcnBasicComplV3": lumDcnBasicComplV3,
       "lumDcnBasicComplV4": lumDcnBasicComplV4,
       "lumDcnBasicComplV5": lumDcnBasicComplV5,
       "lumDcnBasicComplV6": lumDcnBasicComplV6,
       "lumDcnBasicComplV7": lumDcnBasicComplV7,
       "lumDcnBasicComplV8": lumDcnBasicComplV8,
       "lumDcnBasicComplV9": lumDcnBasicComplV9,
       "lumDcnBasicComplV10": lumDcnBasicComplV10,
       "lumDcnBasicComplV11": lumDcnBasicComplV11,
       "lumDcnBasicComplV12": lumDcnBasicComplV12,
       "lumDcnBasicComplV13": lumDcnBasicComplV13,
       "lumDcnBasicComplV14": lumDcnBasicComplV14,
       "lumDcnBasicComplV15": lumDcnBasicComplV15,
       "lumDcnBasicComplV16": lumDcnBasicComplV16,
       "lumDcnBasicComplV17": lumDcnBasicComplV17,
       "lumDcnMIBObjects": lumDcnMIBObjects,
       "dcnGeneral": dcnGeneral,
       "dcnGeneralLastChangeTime": dcnGeneralLastChangeTime,
       "dcnGeneralStateLastChangeTime": dcnGeneralStateLastChangeTime,
       "dcnGeneralDcnIfTableSize": dcnGeneralDcnIfTableSize,
       "dcnGeneralDcnPppTableSize": dcnGeneralDcnPppTableSize,
       "dcnGeneralDcnEthTableSize": dcnGeneralDcnEthTableSize,
       "dcnGeneralDcnCcTableSize": dcnGeneralDcnCcTableSize,
       "dcnIfList": dcnIfList,
       "dcnIfTable": dcnIfTable,
       "dcnIfEntry": dcnIfEntry,
       "dcnIfIndex": dcnIfIndex,
       "dcnIfName": dcnIfName,
       "dcnIfDescr": dcnIfDescr,
       "dcnIfSubrack": dcnIfSubrack,
       "dcnIfSlot": dcnIfSlot,
       "dcnIfTxPort": dcnIfTxPort,
       "dcnIfRxPort": dcnIfRxPort,
       "dcnIfInvPhysIndexOrZero": dcnIfInvPhysIndexOrZero,
       "dcnIfType": dcnIfType,
       "dcnIfMaxSpeed": dcnIfMaxSpeed,
       "dcnIfOscMode": dcnIfOscMode,
       "dcnIfAdminStatus": dcnIfAdminStatus,
       "dcnIfOperStatus": dcnIfOperStatus,
       "dcnIfTxSignalStatus": dcnIfTxSignalStatus,
       "dcnIfLinkDown": dcnIfLinkDown,
       "dcnIfTxFrequency": dcnIfTxFrequency,
       "dcnIfObjectProperty": dcnIfObjectProperty,
       "dcnIfLaserStatus": dcnIfLaserStatus,
       "dcnIfPowerLevel": dcnIfPowerLevel,
       "dcnIfTxPowerLevel": dcnIfTxPowerLevel,
       "dcnIfReceiverSensitivity": dcnIfReceiverSensitivity,
       "dcnIfPowerLevelLowRelativeThreshold": dcnIfPowerLevelLowRelativeThreshold,
       "dcnIfLaserTempActual": dcnIfLaserTempActual,
       "dcnIfTrxClass": dcnIfTrxClass,
       "dcnIfHighSpeedMin": dcnIfHighSpeedMin,
       "dcnIfHighSpeedMax": dcnIfHighSpeedMax,
       "dcnIfExpectedTxFrequency": dcnIfExpectedTxFrequency,
       "dcnIfLaserBias": dcnIfLaserBias,
       "dcnIfLossOfSignal": dcnIfLossOfSignal,
       "dcnIfTrxCodeMismatch": dcnIfTrxCodeMismatch,
       "dcnIfTrxBitrateUnavailable": dcnIfTrxBitrateUnavailable,
       "dcnIfTrxMissing": dcnIfTrxMissing,
       "dcnIfTransmitterFailed": dcnIfTransmitterFailed,
       "dcnIfIllegalFrequency": dcnIfIllegalFrequency,
       "dcnIfUnexpectedTxFrequency": dcnIfUnexpectedTxFrequency,
       "dcnIfReceivedPowerHigh": dcnIfReceivedPowerHigh,
       "dcnIfReceivedPowerLow": dcnIfReceivedPowerLow,
       "dcnIfTrxMediaMismatch": dcnIfTrxMediaMismatch,
       "dcnIfProtocolVersionMismatch": dcnIfProtocolVersionMismatch,
       "dcnIfRemoteDefectIndication": dcnIfRemoteDefectIndication,
       "dcnIfTraceTransmitted": dcnIfTraceTransmitted,
       "dcnIfTraceReceived": dcnIfTraceReceived,
       "dcnIfTraceExpected": dcnIfTraceExpected,
       "dcnIfTraceAlarmMode": dcnIfTraceAlarmMode,
       "dcnIfTraceMismatch": dcnIfTraceMismatch,
       "dcnIfLaserMode": dcnIfLaserMode,
       "dcnIfLinkSupervisionFailure": dcnIfLinkSupervisionFailure,
       "dcnIfAid": dcnIfAid,
       "dcnIfPhysicalLocation": dcnIfPhysicalLocation,
       "lumentisDcnNotifications": lumentisDcnNotifications,
       "dcnNotifyPrefix": dcnNotifyPrefix,
       "dcnIfTxSignalStatusDown": dcnIfTxSignalStatusDown,
       "dcnIfTxSignalStatusUp": dcnIfTxSignalStatusUp,
       "dcnPppList": dcnPppList,
       "dcnPppTable": dcnPppTable,
       "dcnPppEntry": dcnPppEntry,
       "dcnPppIndex": dcnPppIndex,
       "dcnPppName": dcnPppName,
       "dcnPppDescr": dcnPppDescr,
       "dcnPppTxSubrack": dcnPppTxSubrack,
       "dcnPppTxSlot": dcnPppTxSlot,
       "dcnPppTxPort": dcnPppTxPort,
       "dcnPppRxSubrack": dcnPppRxSubrack,
       "dcnPppRxSlot": dcnPppRxSlot,
       "dcnPppRxPort": dcnPppRxPort,
       "dcnPppInvPhysIndexOrZero": dcnPppInvPhysIndexOrZero,
       "dcnPppType": dcnPppType,
       "dcnPppAdminStatus": dcnPppAdminStatus,
       "dcnPppOperStatus": dcnPppOperStatus,
       "dcnPppRouteName": dcnPppRouteName,
       "dcnPppDialCommand": dcnPppDialCommand,
       "dcnPppAcceptCommand": dcnPppAcceptCommand,
       "dcnPppLogicalLinkId": dcnPppLogicalLinkId,
       "dcnPppObjectProperty": dcnPppObjectProperty,
       "dcnPppGccChannel": dcnPppGccChannel,
       "dcnPppVlanId": dcnPppVlanId,
       "dcnPppVlanEtherType": dcnPppVlanEtherType,
       "dcnPppTxIfNo": dcnPppTxIfNo,
       "dcnPppRxIfNo": dcnPppRxIfNo,
       "dcnAddress": dcnAddress,
       "dcnAddressCurrentPppAddress": dcnAddressCurrentPppAddress,
       "dcnAddressNextPppAddress": dcnAddressNextPppAddress,
       "dcnEthList": dcnEthList,
       "dcnEthTable": dcnEthTable,
       "dcnEthEntry": dcnEthEntry,
       "dcnEthIndex": dcnEthIndex,
       "dcnEthName": dcnEthName,
       "dcnEthDescr": dcnEthDescr,
       "dcnEthSubrack": dcnEthSubrack,
       "dcnEthSlot": dcnEthSlot,
       "dcnEthPort": dcnEthPort,
       "dcnEthAutoNegotiationMode": dcnEthAutoNegotiationMode,
       "dcnEthLinkStatus": dcnEthLinkStatus,
       "dcnEthSpeed": dcnEthSpeed,
       "dcnEthDuplexCapability": dcnEthDuplexCapability,
       "dcnEthRateLimit": dcnEthRateLimit,
       "dcnEthFlowControlMode": dcnEthFlowControlMode,
       "dcnEthObjectProperty": dcnEthObjectProperty,
       "dcnEthChangeSpeedCommand": dcnEthChangeSpeedCommand,
       "dcnEthAdminStatus": dcnEthAdminStatus,
       "dcnEthOperStatus": dcnEthOperStatus,
       "dcnCcList": dcnCcList,
       "dcnCcTable": dcnCcTable,
       "dcnCcEntry": dcnCcEntry,
       "dcnCcIndex": dcnCcIndex,
       "dcnCcName": dcnCcName,
       "dcnCcDescr": dcnCcDescr,
       "dcnCcSubrack": dcnCcSubrack,
       "dcnCcSlot": dcnCcSlot,
       "dcnCcTxPort": dcnCcTxPort,
       "dcnCcRxPort": dcnCcRxPort,
       "dcnCcAdminStatus": dcnCcAdminStatus,
       "dcnCcChannelStatus": dcnCcChannelStatus,
       "dcnCcErrorCounter": dcnCcErrorCounter,
       "dcnCcResetCounter": dcnCcResetCounter,
       "dcnCcFecFailure": dcnCcFecFailure,
       "dcnCcTrxNotSupportCommChannel": dcnCcTrxNotSupportCommChannel,
       "dcnCcConfigurationMismatch": dcnCcConfigurationMismatch}
)
