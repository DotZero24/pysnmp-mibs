# SNMP MIB module (LUM-OCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-OCM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:27 2025
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
 lumOcmMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumOcmMIB")

(BoardOrInterfaceAdminStatus,
 BoardOrInterfaceOperStatus,
 CommandString,
 FaultStatus,
 LambdaFrequency,
 MgmtNameString,
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

lumOcmMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 33)
)
if mibBuilder.loadTexts:
    lumOcmMIBModule.setRevisions(
        ("2018-06-15 00:00",
         "2017-12-15 00:00",
         "2017-06-15 00:00",
         "2016-01-11 00:00",
         "2014-05-16 00:00",
         "2008-01-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumOcmConfs_ObjectIdentity = ObjectIdentity
lumOcmConfs = _LumOcmConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 1)
)
_LumOcmGroups_ObjectIdentity = ObjectIdentity
lumOcmGroups = _LumOcmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 1, 1)
)
_LumOcmCompl_ObjectIdentity = ObjectIdentity
lumOcmCompl = _LumOcmCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 1, 2)
)
_LumOcmMinimalGroups_ObjectIdentity = ObjectIdentity
lumOcmMinimalGroups = _LumOcmMinimalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 1, 3)
)
_LumOcmMinimalCompl_ObjectIdentity = ObjectIdentity
lumOcmMinimalCompl = _LumOcmMinimalCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 1, 4)
)
_LumOcmMIBObjects_ObjectIdentity = ObjectIdentity
lumOcmMIBObjects = _LumOcmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2)
)
_OcmGeneral_ObjectIdentity = ObjectIdentity
ocmGeneral = _OcmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 1)
)
_OcmGeneralLastChangeTime_Type = DateAndTime
_OcmGeneralLastChangeTime_Object = MibScalar
ocmGeneralLastChangeTime = _OcmGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 1, 1),
    _OcmGeneralLastChangeTime_Type()
)
ocmGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmGeneralLastChangeTime.setStatus("current")
_OcmGeneralStateLastChangeTime_Type = DateAndTime
_OcmGeneralStateLastChangeTime_Object = MibScalar
ocmGeneralStateLastChangeTime = _OcmGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 1, 2),
    _OcmGeneralStateLastChangeTime_Type()
)
ocmGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmGeneralStateLastChangeTime.setStatus("current")
_OcmGeneralOcmIfTableSize_Type = Unsigned32
_OcmGeneralOcmIfTableSize_Object = MibScalar
ocmGeneralOcmIfTableSize = _OcmGeneralOcmIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 1, 3),
    _OcmGeneralOcmIfTableSize_Type()
)
ocmGeneralOcmIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmGeneralOcmIfTableSize.setStatus("current")
_OcmGeneralOcmChannelTableSize_Type = Unsigned32
_OcmGeneralOcmChannelTableSize_Object = MibScalar
ocmGeneralOcmChannelTableSize = _OcmGeneralOcmChannelTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 1, 4),
    _OcmGeneralOcmChannelTableSize_Type()
)
ocmGeneralOcmChannelTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmGeneralOcmChannelTableSize.setStatus("current")
_OcmIfList_ObjectIdentity = ObjectIdentity
ocmIfList = _OcmIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2)
)
_OcmIfTable_Object = MibTable
ocmIfTable = _OcmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ocmIfTable.setStatus("current")
_OcmIfEntry_Object = MibTableRow
ocmIfEntry = _OcmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1)
)
ocmIfEntry.setIndexNames(
    (0, "LUM-OCM-MIB", "ocmIfIndex"),
)
if mibBuilder.loadTexts:
    ocmIfEntry.setStatus("current")


class _OcmIfIndex_Type(Unsigned32):
    """Custom type ocmIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OcmIfIndex_Type.__name__ = "Unsigned32"
_OcmIfIndex_Object = MibTableColumn
ocmIfIndex = _OcmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 1),
    _OcmIfIndex_Type()
)
ocmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfIndex.setStatus("current")
_OcmIfName_Type = MgmtNameString
_OcmIfName_Object = MibTableColumn
ocmIfName = _OcmIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 2),
    _OcmIfName_Type()
)
ocmIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfName.setStatus("current")


class _OcmIfDescr_Type(DisplayString):
    """Custom type ocmIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_OcmIfDescr_Type.__name__ = "DisplayString"
_OcmIfDescr_Object = MibTableColumn
ocmIfDescr = _OcmIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 3),
    _OcmIfDescr_Type()
)
ocmIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocmIfDescr.setStatus("current")
_OcmIfSubrack_Type = SubrackNumber
_OcmIfSubrack_Object = MibTableColumn
ocmIfSubrack = _OcmIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 4),
    _OcmIfSubrack_Type()
)
ocmIfSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocmIfSubrack.setStatus("current")
_OcmIfSlot_Type = SlotNumber
_OcmIfSlot_Object = MibTableColumn
ocmIfSlot = _OcmIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 5),
    _OcmIfSlot_Type()
)
ocmIfSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocmIfSlot.setStatus("current")
_OcmIfRxPort_Type = PortNumber
_OcmIfRxPort_Object = MibTableColumn
ocmIfRxPort = _OcmIfRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 6),
    _OcmIfRxPort_Type()
)
ocmIfRxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocmIfRxPort.setStatus("current")


class _OcmIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type ocmIfInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OcmIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_OcmIfInvPhysIndexOrZero_Object = MibTableColumn
ocmIfInvPhysIndexOrZero = _OcmIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 7),
    _OcmIfInvPhysIndexOrZero_Type()
)
ocmIfInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfInvPhysIndexOrZero.setStatus("current")


class _OcmIfAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type ocmIfAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_OcmIfAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_OcmIfAdminStatus_Object = MibTableColumn
ocmIfAdminStatus = _OcmIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 8),
    _OcmIfAdminStatus_Type()
)
ocmIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocmIfAdminStatus.setStatus("current")


class _OcmIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type ocmIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_OcmIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_OcmIfOperStatus_Object = MibTableColumn
ocmIfOperStatus = _OcmIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 9),
    _OcmIfOperStatus_Type()
)
ocmIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfOperStatus.setStatus("current")


class _OcmIfPowerThreshold_Type(Integer32):
    """Custom type ocmIfPowerThreshold based on Integer32"""
    defaultValue = -24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_OcmIfPowerThreshold_Type.__name__ = "Integer32"
_OcmIfPowerThreshold_Object = MibTableColumn
ocmIfPowerThreshold = _OcmIfPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 12),
    _OcmIfPowerThreshold_Type()
)
ocmIfPowerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocmIfPowerThreshold.setStatus("current")
_OcmIfUpdateLastChangeTime_Type = DateAndTime
_OcmIfUpdateLastChangeTime_Object = MibTableColumn
ocmIfUpdateLastChangeTime = _OcmIfUpdateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 13),
    _OcmIfUpdateLastChangeTime_Type()
)
ocmIfUpdateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfUpdateLastChangeTime.setStatus("current")


class _OcmIfConnectedSubrack_Type(SubrackNumber):
    """Custom type ocmIfConnectedSubrack based on SubrackNumber"""
    defaultValue = 0


_OcmIfConnectedSubrack_Type.__name__ = "SubrackNumber"
_OcmIfConnectedSubrack_Object = MibTableColumn
ocmIfConnectedSubrack = _OcmIfConnectedSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 14),
    _OcmIfConnectedSubrack_Type()
)
ocmIfConnectedSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocmIfConnectedSubrack.setStatus("current")


class _OcmIfConnectedSlot_Type(SlotNumber):
    """Custom type ocmIfConnectedSlot based on SlotNumber"""
    defaultValue = 0


_OcmIfConnectedSlot_Type.__name__ = "SlotNumber"
_OcmIfConnectedSlot_Object = MibTableColumn
ocmIfConnectedSlot = _OcmIfConnectedSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 15),
    _OcmIfConnectedSlot_Type()
)
ocmIfConnectedSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocmIfConnectedSlot.setStatus("current")


class _OcmIfConnectedPort_Type(PortNumber):
    """Custom type ocmIfConnectedPort based on PortNumber"""
    defaultValue = 0


_OcmIfConnectedPort_Type.__name__ = "PortNumber"
_OcmIfConnectedPort_Object = MibTableColumn
ocmIfConnectedPort = _OcmIfConnectedPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 16),
    _OcmIfConnectedPort_Type()
)
ocmIfConnectedPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocmIfConnectedPort.setStatus("current")


class _OcmIfActivePort_Type(PortNumber):
    """Custom type ocmIfActivePort based on PortNumber"""
    defaultValue = 1


_OcmIfActivePort_Type.__name__ = "PortNumber"
_OcmIfActivePort_Object = MibTableColumn
ocmIfActivePort = _OcmIfActivePort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 17),
    _OcmIfActivePort_Type()
)
ocmIfActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfActivePort.setStatus("current")


class _OcmIfControlMode_Type(Integer32):
    """Custom type ocmIfControlMode based on Integer32"""
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
          ("commissioning", 2))
    )


_OcmIfControlMode_Type.__name__ = "Integer32"
_OcmIfControlMode_Object = MibTableColumn
ocmIfControlMode = _OcmIfControlMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 18),
    _OcmIfControlMode_Type()
)
ocmIfControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfControlMode.setStatus("current")
_OcmIfReferenceTime_Type = DisplayString
_OcmIfReferenceTime_Object = MibTableColumn
ocmIfReferenceTime = _OcmIfReferenceTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 21),
    _OcmIfReferenceTime_Type()
)
ocmIfReferenceTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocmIfReferenceTime.setStatus("current")
_OcmIfSwitchFailure_Type = FaultStatus
_OcmIfSwitchFailure_Object = MibTableColumn
ocmIfSwitchFailure = _OcmIfSwitchFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 22),
    _OcmIfSwitchFailure_Type()
)
ocmIfSwitchFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfSwitchFailure.setStatus("current")
_OcmIfDataSourceNotDefined_Type = FaultStatus
_OcmIfDataSourceNotDefined_Object = MibTableColumn
ocmIfDataSourceNotDefined = _OcmIfDataSourceNotDefined_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 23),
    _OcmIfDataSourceNotDefined_Type()
)
ocmIfDataSourceNotDefined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfDataSourceNotDefined.setStatus("current")
_OcmIfCommissioningMode_Type = FaultStatus
_OcmIfCommissioningMode_Object = MibTableColumn
ocmIfCommissioningMode = _OcmIfCommissioningMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 24),
    _OcmIfCommissioningMode_Type()
)
ocmIfCommissioningMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfCommissioningMode.setStatus("current")
_OcmIfModuleFailure_Type = FaultStatus
_OcmIfModuleFailure_Object = MibTableColumn
ocmIfModuleFailure = _OcmIfModuleFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 25),
    _OcmIfModuleFailure_Type()
)
ocmIfModuleFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfModuleFailure.setStatus("current")
_OcmIfConfigurationCommand_Type = CommandString
_OcmIfConfigurationCommand_Object = MibTableColumn
ocmIfConfigurationCommand = _OcmIfConfigurationCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 26),
    _OcmIfConfigurationCommand_Type()
)
ocmIfConfigurationCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfConfigurationCommand.setStatus("current")
_OcmIfChangeConnectedPort_Type = CommandString
_OcmIfChangeConnectedPort_Object = MibTableColumn
ocmIfChangeConnectedPort = _OcmIfChangeConnectedPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 27),
    _OcmIfChangeConnectedPort_Type()
)
ocmIfChangeConnectedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfChangeConnectedPort.setStatus("current")
_OcmIfSaveReference_Type = CommandString
_OcmIfSaveReference_Object = MibTableColumn
ocmIfSaveReference = _OcmIfSaveReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 28),
    _OcmIfSaveReference_Type()
)
ocmIfSaveReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfSaveReference.setStatus("current")


class _OcmIfPowerOffset_Type(Integer32):
    """Custom type ocmIfPowerOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 350),
    )


_OcmIfPowerOffset_Type.__name__ = "Integer32"
_OcmIfPowerOffset_Object = MibTableColumn
ocmIfPowerOffset = _OcmIfPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 29),
    _OcmIfPowerOffset_Type()
)
ocmIfPowerOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocmIfPowerOffset.setStatus("current")


class _OcmIfConnectedBoardType_Type(Integer32):
    """Custom type ocmIfConnectedBoardType based on Integer32"""
    defaultValue = 1

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
        *(("oa", 1),
          ("roadm", 2),
          ("oa26c", 3),
          ("mdu40", 4),
          ("other", 5),
          ("oaraed21hg", 6),
          ("oaraed20lg", 7))
    )


_OcmIfConnectedBoardType_Type.__name__ = "Integer32"
_OcmIfConnectedBoardType_Object = MibTableColumn
ocmIfConnectedBoardType = _OcmIfConnectedBoardType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 30),
    _OcmIfConnectedBoardType_Type()
)
ocmIfConnectedBoardType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocmIfConnectedBoardType.setStatus("current")
_OcmIfChangeConnectedBoardType_Type = CommandString
_OcmIfChangeConnectedBoardType_Object = MibTableColumn
ocmIfChangeConnectedBoardType = _OcmIfChangeConnectedBoardType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 31),
    _OcmIfChangeConnectedBoardType_Type()
)
ocmIfChangeConnectedBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfChangeConnectedBoardType.setStatus("current")
_OcmIfMaxPowerLevel_Type = Integer32
_OcmIfMaxPowerLevel_Object = MibTableColumn
ocmIfMaxPowerLevel = _OcmIfMaxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 32),
    _OcmIfMaxPowerLevel_Type()
)
ocmIfMaxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfMaxPowerLevel.setStatus("current")
_OcmIfMinPowerLevel_Type = Integer32
_OcmIfMinPowerLevel_Object = MibTableColumn
ocmIfMinPowerLevel = _OcmIfMinPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 33),
    _OcmIfMinPowerLevel_Type()
)
ocmIfMinPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfMinPowerLevel.setStatus("current")
_OcmIfDeltaPower_Type = Integer32
_OcmIfDeltaPower_Object = MibTableColumn
ocmIfDeltaPower = _OcmIfDeltaPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 34),
    _OcmIfDeltaPower_Type()
)
ocmIfDeltaPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfDeltaPower.setStatus("current")
_OcmIfChangePowerThreshold_Type = CommandString
_OcmIfChangePowerThreshold_Object = MibTableColumn
ocmIfChangePowerThreshold = _OcmIfChangePowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 35),
    _OcmIfChangePowerThreshold_Type()
)
ocmIfChangePowerThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfChangePowerThreshold.setStatus("current")
_OcmIfChangePowerOffset_Type = CommandString
_OcmIfChangePowerOffset_Object = MibTableColumn
ocmIfChangePowerOffset = _OcmIfChangePowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 36),
    _OcmIfChangePowerOffset_Type()
)
ocmIfChangePowerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfChangePowerOffset.setStatus("current")


class _OcmIfPowerOffsetAdjustment_Type(Integer32):
    """Custom type ocmIfPowerOffsetAdjustment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 350),
    )


_OcmIfPowerOffsetAdjustment_Type.__name__ = "Integer32"
_OcmIfPowerOffsetAdjustment_Object = MibTableColumn
ocmIfPowerOffsetAdjustment = _OcmIfPowerOffsetAdjustment_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 37),
    _OcmIfPowerOffsetAdjustment_Type()
)
ocmIfPowerOffsetAdjustment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfPowerOffsetAdjustment.setStatus("current")


class _OcmIfSpacingMode_Type(Integer32):
    """Custom type ocmIfSpacingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("spacing50GHz", 1)
    )


_OcmIfSpacingMode_Type.__name__ = "Integer32"
_OcmIfSpacingMode_Object = MibTableColumn
ocmIfSpacingMode = _OcmIfSpacingMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 38),
    _OcmIfSpacingMode_Type()
)
ocmIfSpacingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocmIfSpacingMode.setStatus("current")
_OcmIfHighInputPower_Type = FaultStatus
_OcmIfHighInputPower_Object = MibTableColumn
ocmIfHighInputPower = _OcmIfHighInputPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 2, 1, 1, 39),
    _OcmIfHighInputPower_Type()
)
ocmIfHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmIfHighInputPower.setStatus("current")
_OcmChannelList_ObjectIdentity = ObjectIdentity
ocmChannelList = _OcmChannelList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 3)
)
_OcmChannelTable_Object = MibTable
ocmChannelTable = _OcmChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ocmChannelTable.setStatus("current")
_OcmChannelEntry_Object = MibTableRow
ocmChannelEntry = _OcmChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 3, 1, 1)
)
ocmChannelEntry.setIndexNames(
    (0, "LUM-OCM-MIB", "ocmChannelIndex"),
)
if mibBuilder.loadTexts:
    ocmChannelEntry.setStatus("current")


class _OcmChannelIndex_Type(Unsigned32):
    """Custom type ocmChannelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OcmChannelIndex_Type.__name__ = "Unsigned32"
_OcmChannelIndex_Object = MibTableColumn
ocmChannelIndex = _OcmChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 3, 1, 1, 1),
    _OcmChannelIndex_Type()
)
ocmChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChannelIndex.setStatus("current")
_OcmChannelName_Type = MgmtNameString
_OcmChannelName_Object = MibTableColumn
ocmChannelName = _OcmChannelName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 3, 1, 1, 2),
    _OcmChannelName_Type()
)
ocmChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChannelName.setStatus("current")
_OcmChannelFrequency_Type = LambdaFrequency
_OcmChannelFrequency_Object = MibTableColumn
ocmChannelFrequency = _OcmChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 3, 1, 1, 3),
    _OcmChannelFrequency_Type()
)
ocmChannelFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocmChannelFrequency.setStatus("current")
_OcmChannelPowerLevel_Type = Integer32
_OcmChannelPowerLevel_Object = MibTableColumn
ocmChannelPowerLevel = _OcmChannelPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 3, 1, 1, 4),
    _OcmChannelPowerLevel_Type()
)
ocmChannelPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChannelPowerLevel.setStatus("current")
_OcmChannelUpdateLastChangeTime_Type = DateAndTime
_OcmChannelUpdateLastChangeTime_Object = MibTableColumn
ocmChannelUpdateLastChangeTime = _OcmChannelUpdateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 3, 1, 1, 5),
    _OcmChannelUpdateLastChangeTime_Type()
)
ocmChannelUpdateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChannelUpdateLastChangeTime.setStatus("current")


class _OcmChannelOcmRefIfIndex_Type(Unsigned32):
    """Custom type ocmChannelOcmRefIfIndex based on Unsigned32"""
    defaultValue = 1


_OcmChannelOcmRefIfIndex_Type.__name__ = "Unsigned32"
_OcmChannelOcmRefIfIndex_Object = MibTableColumn
ocmChannelOcmRefIfIndex = _OcmChannelOcmRefIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 3, 1, 1, 6),
    _OcmChannelOcmRefIfIndex_Type()
)
ocmChannelOcmRefIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChannelOcmRefIfIndex.setStatus("current")


class _OcmChannelReferencePowerLevel_Type(Integer32):
    """Custom type ocmChannelReferencePowerLevel based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_OcmChannelReferencePowerLevel_Type.__name__ = "Integer32"
_OcmChannelReferencePowerLevel_Object = MibTableColumn
ocmChannelReferencePowerLevel = _OcmChannelReferencePowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 3, 1, 1, 7),
    _OcmChannelReferencePowerLevel_Type()
)
ocmChannelReferencePowerLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocmChannelReferencePowerLevel.setStatus("current")
_OcmChannelReferenceTime_Type = DisplayString
_OcmChannelReferenceTime_Object = MibTableColumn
ocmChannelReferenceTime = _OcmChannelReferenceTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 3, 1, 1, 8),
    _OcmChannelReferenceTime_Type()
)
ocmChannelReferenceTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocmChannelReferenceTime.setStatus("current")
_OcmChannelSaveReference_Type = CommandString
_OcmChannelSaveReference_Object = MibTableColumn
ocmChannelSaveReference = _OcmChannelSaveReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 3, 1, 1, 9),
    _OcmChannelSaveReference_Type()
)
ocmChannelSaveReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChannelSaveReference.setStatus("current")
_LumentisOcmNotifications_ObjectIdentity = ObjectIdentity
lumentisOcmNotifications = _LumentisOcmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 2, 4)
)

# Managed Objects groups

ocmGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 1, 1, 1)
)
ocmGeneralGroup.setObjects(
      *(("LUM-OCM-MIB", "ocmGeneralLastChangeTime"),
        ("LUM-OCM-MIB", "ocmGeneralStateLastChangeTime"),
        ("LUM-OCM-MIB", "ocmGeneralOcmIfTableSize"))
)
if mibBuilder.loadTexts:
    ocmGeneralGroup.setStatus("current")

ocmIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 1, 1, 2)
)
ocmIfGroup.setObjects(
      *(("LUM-OCM-MIB", "ocmIfIndex"),
        ("LUM-OCM-MIB", "ocmIfName"),
        ("LUM-OCM-MIB", "ocmIfDescr"),
        ("LUM-OCM-MIB", "ocmIfSubrack"),
        ("LUM-OCM-MIB", "ocmIfSlot"),
        ("LUM-OCM-MIB", "ocmIfRxPort"),
        ("LUM-OCM-MIB", "ocmIfInvPhysIndexOrZero"),
        ("LUM-OCM-MIB", "ocmIfAdminStatus"),
        ("LUM-OCM-MIB", "ocmIfOperStatus"),
        ("LUM-OCM-MIB", "ocmIfPowerThreshold"),
        ("LUM-OCM-MIB", "ocmIfUpdateLastChangeTime"),
        ("LUM-OCM-MIB", "ocmIfConnectedSubrack"),
        ("LUM-OCM-MIB", "ocmIfConnectedSlot"),
        ("LUM-OCM-MIB", "ocmIfConnectedPort"),
        ("LUM-OCM-MIB", "ocmIfActivePort"),
        ("LUM-OCM-MIB", "ocmIfControlMode"),
        ("LUM-OCM-MIB", "ocmIfReferenceTime"),
        ("LUM-OCM-MIB", "ocmIfSwitchFailure"),
        ("LUM-OCM-MIB", "ocmIfDataSourceNotDefined"),
        ("LUM-OCM-MIB", "ocmIfCommissioningMode"),
        ("LUM-OCM-MIB", "ocmIfModuleFailure"),
        ("LUM-OCM-MIB", "ocmIfConfigurationCommand"),
        ("LUM-OCM-MIB", "ocmIfChangeConnectedPort"),
        ("LUM-OCM-MIB", "ocmIfSaveReference"),
        ("LUM-OCM-MIB", "ocmIfPowerOffset"),
        ("LUM-OCM-MIB", "ocmIfConnectedBoardType"),
        ("LUM-OCM-MIB", "ocmIfChangeConnectedBoardType"),
        ("LUM-OCM-MIB", "ocmIfMaxPowerLevel"),
        ("LUM-OCM-MIB", "ocmIfMinPowerLevel"),
        ("LUM-OCM-MIB", "ocmIfDeltaPower"))
)
if mibBuilder.loadTexts:
    ocmIfGroup.setStatus("deprecated")

ocmChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 1, 1, 3)
)
ocmChannelGroup.setObjects(
      *(("LUM-OCM-MIB", "ocmChannelIndex"),
        ("LUM-OCM-MIB", "ocmChannelName"),
        ("LUM-OCM-MIB", "ocmChannelFrequency"),
        ("LUM-OCM-MIB", "ocmChannelPowerLevel"),
        ("LUM-OCM-MIB", "ocmChannelUpdateLastChangeTime"),
        ("LUM-OCM-MIB", "ocmChannelOcmRefIfIndex"),
        ("LUM-OCM-MIB", "ocmChannelReferencePowerLevel"))
)
if mibBuilder.loadTexts:
    ocmChannelGroup.setStatus("deprecated")

ocmIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 1, 1, 4)
)
ocmIfGroupV2.setObjects(
      *(("LUM-OCM-MIB", "ocmIfIndex"),
        ("LUM-OCM-MIB", "ocmIfName"),
        ("LUM-OCM-MIB", "ocmIfDescr"),
        ("LUM-OCM-MIB", "ocmIfSubrack"),
        ("LUM-OCM-MIB", "ocmIfSlot"),
        ("LUM-OCM-MIB", "ocmIfRxPort"),
        ("LUM-OCM-MIB", "ocmIfInvPhysIndexOrZero"),
        ("LUM-OCM-MIB", "ocmIfAdminStatus"),
        ("LUM-OCM-MIB", "ocmIfOperStatus"),
        ("LUM-OCM-MIB", "ocmIfPowerThreshold"),
        ("LUM-OCM-MIB", "ocmIfUpdateLastChangeTime"),
        ("LUM-OCM-MIB", "ocmIfConnectedSubrack"),
        ("LUM-OCM-MIB", "ocmIfConnectedSlot"),
        ("LUM-OCM-MIB", "ocmIfConnectedPort"),
        ("LUM-OCM-MIB", "ocmIfActivePort"),
        ("LUM-OCM-MIB", "ocmIfControlMode"),
        ("LUM-OCM-MIB", "ocmIfReferenceTime"),
        ("LUM-OCM-MIB", "ocmIfSwitchFailure"),
        ("LUM-OCM-MIB", "ocmIfDataSourceNotDefined"),
        ("LUM-OCM-MIB", "ocmIfCommissioningMode"),
        ("LUM-OCM-MIB", "ocmIfModuleFailure"),
        ("LUM-OCM-MIB", "ocmIfConfigurationCommand"),
        ("LUM-OCM-MIB", "ocmIfChangeConnectedPort"),
        ("LUM-OCM-MIB", "ocmIfSaveReference"),
        ("LUM-OCM-MIB", "ocmIfPowerOffset"),
        ("LUM-OCM-MIB", "ocmIfConnectedBoardType"),
        ("LUM-OCM-MIB", "ocmIfChangeConnectedBoardType"),
        ("LUM-OCM-MIB", "ocmIfMaxPowerLevel"),
        ("LUM-OCM-MIB", "ocmIfMinPowerLevel"),
        ("LUM-OCM-MIB", "ocmIfDeltaPower"),
        ("LUM-OCM-MIB", "ocmIfChangePowerThreshold"),
        ("LUM-OCM-MIB", "ocmIfChangePowerOffset"))
)
if mibBuilder.loadTexts:
    ocmIfGroupV2.setStatus("deprecated")

ocmIfGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 1, 1, 5)
)
ocmIfGroupV3.setObjects(
      *(("LUM-OCM-MIB", "ocmIfIndex"),
        ("LUM-OCM-MIB", "ocmIfName"),
        ("LUM-OCM-MIB", "ocmIfDescr"),
        ("LUM-OCM-MIB", "ocmIfSubrack"),
        ("LUM-OCM-MIB", "ocmIfSlot"),
        ("LUM-OCM-MIB", "ocmIfRxPort"),
        ("LUM-OCM-MIB", "ocmIfInvPhysIndexOrZero"),
        ("LUM-OCM-MIB", "ocmIfAdminStatus"),
        ("LUM-OCM-MIB", "ocmIfOperStatus"),
        ("LUM-OCM-MIB", "ocmIfPowerThreshold"),
        ("LUM-OCM-MIB", "ocmIfUpdateLastChangeTime"),
        ("LUM-OCM-MIB", "ocmIfConnectedSubrack"),
        ("LUM-OCM-MIB", "ocmIfConnectedSlot"),
        ("LUM-OCM-MIB", "ocmIfConnectedPort"),
        ("LUM-OCM-MIB", "ocmIfActivePort"),
        ("LUM-OCM-MIB", "ocmIfControlMode"),
        ("LUM-OCM-MIB", "ocmIfReferenceTime"),
        ("LUM-OCM-MIB", "ocmIfSwitchFailure"),
        ("LUM-OCM-MIB", "ocmIfDataSourceNotDefined"),
        ("LUM-OCM-MIB", "ocmIfCommissioningMode"),
        ("LUM-OCM-MIB", "ocmIfModuleFailure"),
        ("LUM-OCM-MIB", "ocmIfConfigurationCommand"),
        ("LUM-OCM-MIB", "ocmIfChangeConnectedPort"),
        ("LUM-OCM-MIB", "ocmIfSaveReference"),
        ("LUM-OCM-MIB", "ocmIfPowerOffset"),
        ("LUM-OCM-MIB", "ocmIfConnectedBoardType"),
        ("LUM-OCM-MIB", "ocmIfChangeConnectedBoardType"),
        ("LUM-OCM-MIB", "ocmIfMaxPowerLevel"),
        ("LUM-OCM-MIB", "ocmIfMinPowerLevel"),
        ("LUM-OCM-MIB", "ocmIfDeltaPower"),
        ("LUM-OCM-MIB", "ocmIfChangePowerThreshold"),
        ("LUM-OCM-MIB", "ocmIfChangePowerOffset"),
        ("LUM-OCM-MIB", "ocmIfPowerOffsetAdjustment"))
)
if mibBuilder.loadTexts:
    ocmIfGroupV3.setStatus("deprecated")

ocmChannelGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 1, 1, 6)
)
ocmChannelGroupV2.setObjects(
      *(("LUM-OCM-MIB", "ocmChannelIndex"),
        ("LUM-OCM-MIB", "ocmChannelName"),
        ("LUM-OCM-MIB", "ocmChannelFrequency"),
        ("LUM-OCM-MIB", "ocmChannelPowerLevel"),
        ("LUM-OCM-MIB", "ocmChannelUpdateLastChangeTime"),
        ("LUM-OCM-MIB", "ocmChannelOcmRefIfIndex"),
        ("LUM-OCM-MIB", "ocmChannelReferencePowerLevel"),
        ("LUM-OCM-MIB", "ocmChannelReferenceTime"),
        ("LUM-OCM-MIB", "ocmChannelSaveReference"))
)
if mibBuilder.loadTexts:
    ocmChannelGroupV2.setStatus("current")

ocmIfGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 1, 1, 7)
)
ocmIfGroupV4.setObjects(
      *(("LUM-OCM-MIB", "ocmIfIndex"),
        ("LUM-OCM-MIB", "ocmIfName"),
        ("LUM-OCM-MIB", "ocmIfDescr"),
        ("LUM-OCM-MIB", "ocmIfSubrack"),
        ("LUM-OCM-MIB", "ocmIfSlot"),
        ("LUM-OCM-MIB", "ocmIfRxPort"),
        ("LUM-OCM-MIB", "ocmIfInvPhysIndexOrZero"),
        ("LUM-OCM-MIB", "ocmIfAdminStatus"),
        ("LUM-OCM-MIB", "ocmIfOperStatus"),
        ("LUM-OCM-MIB", "ocmIfPowerThreshold"),
        ("LUM-OCM-MIB", "ocmIfUpdateLastChangeTime"),
        ("LUM-OCM-MIB", "ocmIfConnectedSubrack"),
        ("LUM-OCM-MIB", "ocmIfConnectedSlot"),
        ("LUM-OCM-MIB", "ocmIfConnectedPort"),
        ("LUM-OCM-MIB", "ocmIfActivePort"),
        ("LUM-OCM-MIB", "ocmIfControlMode"),
        ("LUM-OCM-MIB", "ocmIfReferenceTime"),
        ("LUM-OCM-MIB", "ocmIfSwitchFailure"),
        ("LUM-OCM-MIB", "ocmIfDataSourceNotDefined"),
        ("LUM-OCM-MIB", "ocmIfCommissioningMode"),
        ("LUM-OCM-MIB", "ocmIfModuleFailure"),
        ("LUM-OCM-MIB", "ocmIfConfigurationCommand"),
        ("LUM-OCM-MIB", "ocmIfChangeConnectedPort"),
        ("LUM-OCM-MIB", "ocmIfSaveReference"),
        ("LUM-OCM-MIB", "ocmIfPowerOffset"),
        ("LUM-OCM-MIB", "ocmIfConnectedBoardType"),
        ("LUM-OCM-MIB", "ocmIfChangeConnectedBoardType"),
        ("LUM-OCM-MIB", "ocmIfMaxPowerLevel"),
        ("LUM-OCM-MIB", "ocmIfMinPowerLevel"),
        ("LUM-OCM-MIB", "ocmIfDeltaPower"),
        ("LUM-OCM-MIB", "ocmIfChangePowerThreshold"),
        ("LUM-OCM-MIB", "ocmIfChangePowerOffset"),
        ("LUM-OCM-MIB", "ocmIfPowerOffsetAdjustment"),
        ("LUM-OCM-MIB", "ocmIfSpacingMode"),
        ("LUM-OCM-MIB", "ocmIfHighInputPower"))
)
if mibBuilder.loadTexts:
    ocmIfGroupV4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumOcmBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 1, 2, 1)
)
lumOcmBasicComplV1.setObjects(
      *(("LUM-OCM-MIB", "ocmGeneralGroup"),
        ("LUM-OCM-MIB", "ocmIfGroup"),
        ("LUM-OCM-MIB", "ocmChannelGroup"))
)
if mibBuilder.loadTexts:
    lumOcmBasicComplV1.setStatus(
        "deprecated"
    )

lumOcmBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 1, 2, 2)
)
lumOcmBasicComplV2.setObjects(
      *(("LUM-OCM-MIB", "ocmGeneralGroup"),
        ("LUM-OCM-MIB", "ocmIfGroupV2"),
        ("LUM-OCM-MIB", "ocmChannelGroup"))
)
if mibBuilder.loadTexts:
    lumOcmBasicComplV2.setStatus(
        "deprecated"
    )

lumOcmBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 1, 2, 3)
)
lumOcmBasicComplV3.setObjects(
      *(("LUM-OCM-MIB", "ocmGeneralGroup"),
        ("LUM-OCM-MIB", "ocmIfGroupV3"),
        ("LUM-OCM-MIB", "ocmChannelGroup"))
)
if mibBuilder.loadTexts:
    lumOcmBasicComplV3.setStatus(
        "deprecated"
    )

lumOcmBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 1, 2, 4)
)
lumOcmBasicComplV4.setObjects(
      *(("LUM-OCM-MIB", "ocmGeneralGroup"),
        ("LUM-OCM-MIB", "ocmIfGroupV3"),
        ("LUM-OCM-MIB", "ocmChannelGroupV2"))
)
if mibBuilder.loadTexts:
    lumOcmBasicComplV4.setStatus(
        "deprecated"
    )

lumOcmBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 1, 2, 5)
)
lumOcmBasicComplV5.setObjects(
      *(("LUM-OCM-MIB", "ocmGeneralGroup"),
        ("LUM-OCM-MIB", "ocmIfGroupV4"),
        ("LUM-OCM-MIB", "ocmChannelGroupV2"))
)
if mibBuilder.loadTexts:
    lumOcmBasicComplV5.setStatus(
        "current"
    )

lumOcmMinimalComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33, 1, 4, 1)
)
lumOcmMinimalComplV1.setObjects(
      *(("LUM-OCM-MIB", "ocmGeneralGroup"),
        ("LUM-OCM-MIB", "ocmIfGroup"))
)
if mibBuilder.loadTexts:
    lumOcmMinimalComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-OCM-MIB",
    **{"lumOcmMIBModule": lumOcmMIBModule,
       "lumOcmConfs": lumOcmConfs,
       "lumOcmGroups": lumOcmGroups,
       "ocmGeneralGroup": ocmGeneralGroup,
       "ocmIfGroup": ocmIfGroup,
       "ocmChannelGroup": ocmChannelGroup,
       "ocmIfGroupV2": ocmIfGroupV2,
       "ocmIfGroupV3": ocmIfGroupV3,
       "ocmChannelGroupV2": ocmChannelGroupV2,
       "ocmIfGroupV4": ocmIfGroupV4,
       "lumOcmCompl": lumOcmCompl,
       "lumOcmBasicComplV1": lumOcmBasicComplV1,
       "lumOcmBasicComplV2": lumOcmBasicComplV2,
       "lumOcmBasicComplV3": lumOcmBasicComplV3,
       "lumOcmBasicComplV4": lumOcmBasicComplV4,
       "lumOcmBasicComplV5": lumOcmBasicComplV5,
       "lumOcmMinimalGroups": lumOcmMinimalGroups,
       "lumOcmMinimalCompl": lumOcmMinimalCompl,
       "lumOcmMinimalComplV1": lumOcmMinimalComplV1,
       "lumOcmMIBObjects": lumOcmMIBObjects,
       "ocmGeneral": ocmGeneral,
       "ocmGeneralLastChangeTime": ocmGeneralLastChangeTime,
       "ocmGeneralStateLastChangeTime": ocmGeneralStateLastChangeTime,
       "ocmGeneralOcmIfTableSize": ocmGeneralOcmIfTableSize,
       "ocmGeneralOcmChannelTableSize": ocmGeneralOcmChannelTableSize,
       "ocmIfList": ocmIfList,
       "ocmIfTable": ocmIfTable,
       "ocmIfEntry": ocmIfEntry,
       "ocmIfIndex": ocmIfIndex,
       "ocmIfName": ocmIfName,
       "ocmIfDescr": ocmIfDescr,
       "ocmIfSubrack": ocmIfSubrack,
       "ocmIfSlot": ocmIfSlot,
       "ocmIfRxPort": ocmIfRxPort,
       "ocmIfInvPhysIndexOrZero": ocmIfInvPhysIndexOrZero,
       "ocmIfAdminStatus": ocmIfAdminStatus,
       "ocmIfOperStatus": ocmIfOperStatus,
       "ocmIfPowerThreshold": ocmIfPowerThreshold,
       "ocmIfUpdateLastChangeTime": ocmIfUpdateLastChangeTime,
       "ocmIfConnectedSubrack": ocmIfConnectedSubrack,
       "ocmIfConnectedSlot": ocmIfConnectedSlot,
       "ocmIfConnectedPort": ocmIfConnectedPort,
       "ocmIfActivePort": ocmIfActivePort,
       "ocmIfControlMode": ocmIfControlMode,
       "ocmIfReferenceTime": ocmIfReferenceTime,
       "ocmIfSwitchFailure": ocmIfSwitchFailure,
       "ocmIfDataSourceNotDefined": ocmIfDataSourceNotDefined,
       "ocmIfCommissioningMode": ocmIfCommissioningMode,
       "ocmIfModuleFailure": ocmIfModuleFailure,
       "ocmIfConfigurationCommand": ocmIfConfigurationCommand,
       "ocmIfChangeConnectedPort": ocmIfChangeConnectedPort,
       "ocmIfSaveReference": ocmIfSaveReference,
       "ocmIfPowerOffset": ocmIfPowerOffset,
       "ocmIfConnectedBoardType": ocmIfConnectedBoardType,
       "ocmIfChangeConnectedBoardType": ocmIfChangeConnectedBoardType,
       "ocmIfMaxPowerLevel": ocmIfMaxPowerLevel,
       "ocmIfMinPowerLevel": ocmIfMinPowerLevel,
       "ocmIfDeltaPower": ocmIfDeltaPower,
       "ocmIfChangePowerThreshold": ocmIfChangePowerThreshold,
       "ocmIfChangePowerOffset": ocmIfChangePowerOffset,
       "ocmIfPowerOffsetAdjustment": ocmIfPowerOffsetAdjustment,
       "ocmIfSpacingMode": ocmIfSpacingMode,
       "ocmIfHighInputPower": ocmIfHighInputPower,
       "ocmChannelList": ocmChannelList,
       "ocmChannelTable": ocmChannelTable,
       "ocmChannelEntry": ocmChannelEntry,
       "ocmChannelIndex": ocmChannelIndex,
       "ocmChannelName": ocmChannelName,
       "ocmChannelFrequency": ocmChannelFrequency,
       "ocmChannelPowerLevel": ocmChannelPowerLevel,
       "ocmChannelUpdateLastChangeTime": ocmChannelUpdateLastChangeTime,
       "ocmChannelOcmRefIfIndex": ocmChannelOcmRefIfIndex,
       "ocmChannelReferencePowerLevel": ocmChannelReferencePowerLevel,
       "ocmChannelReferenceTime": ocmChannelReferenceTime,
       "ocmChannelSaveReference": ocmChannelSaveReference,
       "lumentisOcmNotifications": lumentisOcmNotifications}
)
