# SNMP MIB module (LUM-OA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-OA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:06 2025
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
 lumOaMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumOaMIB")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lumOaMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 20)
)
if mibBuilder.loadTexts:
    lumOaMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-11-30 00:00",
         "2016-05-30 00:00",
         "2014-05-16 00:00",
         "2012-11-01 00:00",
         "2012-03-30 00:00",
         "2011-12-20 00:00",
         "2011-04-27 00:00",
         "2005-01-27 00:00",
         "2002-09-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumOaConfs_ObjectIdentity = ObjectIdentity
lumOaConfs = _LumOaConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1)
)
_LumOaGroups_ObjectIdentity = ObjectIdentity
lumOaGroups = _LumOaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1)
)
_LumOaCompl_ObjectIdentity = ObjectIdentity
lumOaCompl = _LumOaCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2)
)
_LumOaMinimalGroups_ObjectIdentity = ObjectIdentity
lumOaMinimalGroups = _LumOaMinimalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 3)
)
_LumOaMinimalCompl_ObjectIdentity = ObjectIdentity
lumOaMinimalCompl = _LumOaMinimalCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 4)
)
_LumOaMIBObjects_ObjectIdentity = ObjectIdentity
lumOaMIBObjects = _LumOaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2)
)
_OaGeneral_ObjectIdentity = ObjectIdentity
oaGeneral = _OaGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 1)
)
_OaGeneralLastChangeTime_Type = DateAndTime
_OaGeneralLastChangeTime_Object = MibScalar
oaGeneralLastChangeTime = _OaGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 1, 1),
    _OaGeneralLastChangeTime_Type()
)
oaGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaGeneralLastChangeTime.setStatus("current")
_OaGeneralStateLastChangeTime_Type = DateAndTime
_OaGeneralStateLastChangeTime_Object = MibScalar
oaGeneralStateLastChangeTime = _OaGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 1, 2),
    _OaGeneralStateLastChangeTime_Type()
)
oaGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaGeneralStateLastChangeTime.setStatus("current")
_OaGeneralOaIfTableSize_Type = Unsigned32
_OaGeneralOaIfTableSize_Object = MibScalar
oaGeneralOaIfTableSize = _OaGeneralOaIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 1, 3),
    _OaGeneralOaIfTableSize_Type()
)
oaGeneralOaIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaGeneralOaIfTableSize.setStatus("current")
_OaGeneralVoaIfTableSize_Type = Unsigned32
_OaGeneralVoaIfTableSize_Object = MibScalar
oaGeneralVoaIfTableSize = _OaGeneralVoaIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 1, 4),
    _OaGeneralVoaIfTableSize_Type()
)
oaGeneralVoaIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaGeneralVoaIfTableSize.setStatus("current")
_OaGeneralVoaClientIfTableSize_Type = Unsigned32
_OaGeneralVoaClientIfTableSize_Object = MibScalar
oaGeneralVoaClientIfTableSize = _OaGeneralVoaClientIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 1, 5),
    _OaGeneralVoaClientIfTableSize_Type()
)
oaGeneralVoaClientIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaGeneralVoaClientIfTableSize.setStatus("current")
_OaGeneralVoaLineIfTableSize_Type = Unsigned32
_OaGeneralVoaLineIfTableSize_Object = MibScalar
oaGeneralVoaLineIfTableSize = _OaGeneralVoaLineIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 1, 6),
    _OaGeneralVoaLineIfTableSize_Type()
)
oaGeneralVoaLineIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaGeneralVoaLineIfTableSize.setStatus("current")
_OaGeneralOaModuleTableSize_Type = Unsigned32
_OaGeneralOaModuleTableSize_Object = MibScalar
oaGeneralOaModuleTableSize = _OaGeneralOaModuleTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 1, 7),
    _OaGeneralOaModuleTableSize_Type()
)
oaGeneralOaModuleTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaGeneralOaModuleTableSize.setStatus("current")
_OaIfList_ObjectIdentity = ObjectIdentity
oaIfList = _OaIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2)
)
_OaIfTable_Object = MibTable
oaIfTable = _OaIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1)
)
if mibBuilder.loadTexts:
    oaIfTable.setStatus("current")
_OaIfEntry_Object = MibTableRow
oaIfEntry = _OaIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1)
)
oaIfEntry.setIndexNames(
    (0, "LUM-OA-MIB", "oaIfIndex"),
)
if mibBuilder.loadTexts:
    oaIfEntry.setStatus("current")


class _OaIfIndex_Type(Unsigned32):
    """Custom type oaIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OaIfIndex_Type.__name__ = "Unsigned32"
_OaIfIndex_Object = MibTableColumn
oaIfIndex = _OaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 1),
    _OaIfIndex_Type()
)
oaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfIndex.setStatus("current")
_OaIfName_Type = MgmtNameString
_OaIfName_Object = MibTableColumn
oaIfName = _OaIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 2),
    _OaIfName_Type()
)
oaIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfName.setStatus("current")


class _OaIfDescr_Type(DisplayString):
    """Custom type oaIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_OaIfDescr_Type.__name__ = "DisplayString"
_OaIfDescr_Object = MibTableColumn
oaIfDescr = _OaIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 3),
    _OaIfDescr_Type()
)
oaIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaIfDescr.setStatus("current")
_OaIfSubrack_Type = SubrackNumber
_OaIfSubrack_Object = MibTableColumn
oaIfSubrack = _OaIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 4),
    _OaIfSubrack_Type()
)
oaIfSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oaIfSubrack.setStatus("current")
_OaIfSlot_Type = SlotNumber
_OaIfSlot_Object = MibTableColumn
oaIfSlot = _OaIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 5),
    _OaIfSlot_Type()
)
oaIfSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oaIfSlot.setStatus("current")
_OaIfTxPort_Type = PortNumber
_OaIfTxPort_Object = MibTableColumn
oaIfTxPort = _OaIfTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 6),
    _OaIfTxPort_Type()
)
oaIfTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oaIfTxPort.setStatus("current")
_OaIfRxPort_Type = PortNumber
_OaIfRxPort_Object = MibTableColumn
oaIfRxPort = _OaIfRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 7),
    _OaIfRxPort_Type()
)
oaIfRxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oaIfRxPort.setStatus("current")


class _OaIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type oaIfInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_OaIfInvPhysIndexOrZero_Object = MibTableColumn
oaIfInvPhysIndexOrZero = _OaIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 8),
    _OaIfInvPhysIndexOrZero_Type()
)
oaIfInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfInvPhysIndexOrZero.setStatus("current")


class _OaIfAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type oaIfAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_OaIfAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_OaIfAdminStatus_Object = MibTableColumn
oaIfAdminStatus = _OaIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 9),
    _OaIfAdminStatus_Type()
)
oaIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaIfAdminStatus.setStatus("current")


class _OaIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type oaIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_OaIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_OaIfOperStatus_Object = MibTableColumn
oaIfOperStatus = _OaIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 10),
    _OaIfOperStatus_Type()
)
oaIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfOperStatus.setStatus("current")


class _OaIfLaserStatus_Type(Integer32):
    """Custom type oaIfLaserStatus based on Integer32"""
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


_OaIfLaserStatus_Type.__name__ = "Integer32"
_OaIfLaserStatus_Object = MibTableColumn
oaIfLaserStatus = _OaIfLaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 11),
    _OaIfLaserStatus_Type()
)
oaIfLaserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfLaserStatus.setStatus("current")


class _OaIfAmplifierType_Type(Integer32):
    """Custom type oaIfAmplifierType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("pre25ad", 1),
          ("pre25tm", 2),
          ("pow10", 3),
          ("pre10ad", 4),
          ("pre10tm", 5),
          ("constantGain", 6),
          ("constantSignalPower", 7),
          ("constantPower", 8),
          ("constantGainLI", 9),
          ("constantGainHI", 10))
    )


_OaIfAmplifierType_Type.__name__ = "Integer32"
_OaIfAmplifierType_Object = MibTableColumn
oaIfAmplifierType = _OaIfAmplifierType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 12),
    _OaIfAmplifierType_Type()
)
oaIfAmplifierType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oaIfAmplifierType.setStatus("current")


class _OaIfWantedAbsolutePowerLevel_Type(Integer32):
    """Custom type oaIfWantedAbsolutePowerLevel based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 195),
    )


_OaIfWantedAbsolutePowerLevel_Type.__name__ = "Integer32"
_OaIfWantedAbsolutePowerLevel_Object = MibTableColumn
oaIfWantedAbsolutePowerLevel = _OaIfWantedAbsolutePowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 13),
    _OaIfWantedAbsolutePowerLevel_Type()
)
oaIfWantedAbsolutePowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaIfWantedAbsolutePowerLevel.setStatus("current")


class _OaIfWantedRelativePowerLevel_Type(Integer32):
    """Custom type oaIfWantedRelativePowerLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 60),
    )


_OaIfWantedRelativePowerLevel_Type.__name__ = "Integer32"
_OaIfWantedRelativePowerLevel_Object = MibTableColumn
oaIfWantedRelativePowerLevel = _OaIfWantedRelativePowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 14),
    _OaIfWantedRelativePowerLevel_Type()
)
oaIfWantedRelativePowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaIfWantedRelativePowerLevel.setStatus("current")


class _OaIfWantedGain_Type(Integer32):
    """Custom type oaIfWantedGain based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(130, 330),
    )


_OaIfWantedGain_Type.__name__ = "Integer32"
_OaIfWantedGain_Object = MibTableColumn
oaIfWantedGain = _OaIfWantedGain_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 15),
    _OaIfWantedGain_Type()
)
oaIfWantedGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaIfWantedGain.setStatus("current")


class _OaIfFrequencyMin_Type(LambdaFrequency):
    """Custom type oaIfFrequencyMin based on LambdaFrequency"""
    defaultValue = 19210


_OaIfFrequencyMin_Type.__name__ = "LambdaFrequency"
_OaIfFrequencyMin_Object = MibTableColumn
oaIfFrequencyMin = _OaIfFrequencyMin_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 16),
    _OaIfFrequencyMin_Type()
)
oaIfFrequencyMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaIfFrequencyMin.setStatus("current")


class _OaIfFrequencyMax_Type(LambdaFrequency):
    """Custom type oaIfFrequencyMax based on LambdaFrequency"""
    defaultValue = 19590


_OaIfFrequencyMax_Type.__name__ = "LambdaFrequency"
_OaIfFrequencyMax_Object = MibTableColumn
oaIfFrequencyMax = _OaIfFrequencyMax_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 17),
    _OaIfFrequencyMax_Type()
)
oaIfFrequencyMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaIfFrequencyMax.setStatus("current")
_OaIfNominalTxPower_Type = Integer32
_OaIfNominalTxPower_Object = MibTableColumn
oaIfNominalTxPower = _OaIfNominalTxPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 18),
    _OaIfNominalTxPower_Type()
)
oaIfNominalTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfNominalTxPower.setStatus("current")
_OaIfTxPowerLevel_Type = Integer32
_OaIfTxPowerLevel_Object = MibTableColumn
oaIfTxPowerLevel = _OaIfTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 19),
    _OaIfTxPowerLevel_Type()
)
oaIfTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfTxPowerLevel.setStatus("current")
_OaIfRxPowerLevel_Type = Integer32
_OaIfRxPowerLevel_Object = MibTableColumn
oaIfRxPowerLevel = _OaIfRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 20),
    _OaIfRxPowerLevel_Type()
)
oaIfRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfRxPowerLevel.setStatus("current")


class _OaIfRxPowerLevelLowThreshold_Type(Integer32):
    """Custom type oaIfRxPowerLevelLowThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 80),
    )


_OaIfRxPowerLevelLowThreshold_Type.__name__ = "Integer32"
_OaIfRxPowerLevelLowThreshold_Object = MibTableColumn
oaIfRxPowerLevelLowThreshold = _OaIfRxPowerLevelLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 21),
    _OaIfRxPowerLevelLowThreshold_Type()
)
oaIfRxPowerLevelLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaIfRxPowerLevelLowThreshold.setStatus("current")
_OaIfLaserBias_Type = Unsigned32
_OaIfLaserBias_Object = MibTableColumn
oaIfLaserBias = _OaIfLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 22),
    _OaIfLaserBias_Type()
)
oaIfLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfLaserBias.setStatus("current")
_OaIfNominalLaserTemp_Type = Unsigned32
_OaIfNominalLaserTemp_Object = MibTableColumn
oaIfNominalLaserTemp = _OaIfNominalLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 23),
    _OaIfNominalLaserTemp_Type()
)
oaIfNominalLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfNominalLaserTemp.setStatus("current")
_OaIfRelativeLaserTemp_Type = Integer32
_OaIfRelativeLaserTemp_Object = MibTableColumn
oaIfRelativeLaserTemp = _OaIfRelativeLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 24),
    _OaIfRelativeLaserTemp_Type()
)
oaIfRelativeLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfRelativeLaserTemp.setStatus("current")


class _OaIfLossOfSignalThreshold_Type(Integer32):
    """Custom type oaIfLossOfSignalThreshold based on Integer32"""
    defaultValue = -560

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-560, 80),
    )


_OaIfLossOfSignalThreshold_Type.__name__ = "Integer32"
_OaIfLossOfSignalThreshold_Object = MibTableColumn
oaIfLossOfSignalThreshold = _OaIfLossOfSignalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 25),
    _OaIfLossOfSignalThreshold_Type()
)
oaIfLossOfSignalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaIfLossOfSignalThreshold.setStatus("current")
_OaIfLossOfSignal_Type = FaultStatus
_OaIfLossOfSignal_Object = MibTableColumn
oaIfLossOfSignal = _OaIfLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 26),
    _OaIfLossOfSignal_Type()
)
oaIfLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfLossOfSignal.setStatus("current")
_OaIfPumpLaserTempHigh_Type = FaultStatus
_OaIfPumpLaserTempHigh_Object = MibTableColumn
oaIfPumpLaserTempHigh = _OaIfPumpLaserTempHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 27),
    _OaIfPumpLaserTempHigh_Type()
)
oaIfPumpLaserTempHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfPumpLaserTempHigh.setStatus("current")
_OaIfRegulationProblemRxPowerHigh_Type = FaultStatus
_OaIfRegulationProblemRxPowerHigh_Object = MibTableColumn
oaIfRegulationProblemRxPowerHigh = _OaIfRegulationProblemRxPowerHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 28),
    _OaIfRegulationProblemRxPowerHigh_Type()
)
oaIfRegulationProblemRxPowerHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfRegulationProblemRxPowerHigh.setStatus("current")
_OaIfRegulationProblemTxPowerHigh_Type = FaultStatus
_OaIfRegulationProblemTxPowerHigh_Object = MibTableColumn
oaIfRegulationProblemTxPowerHigh = _OaIfRegulationProblemTxPowerHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 29),
    _OaIfRegulationProblemTxPowerHigh_Type()
)
oaIfRegulationProblemTxPowerHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfRegulationProblemTxPowerHigh.setStatus("current")
_OaIfRegulationProblemTxPowerLow_Type = FaultStatus
_OaIfRegulationProblemTxPowerLow_Object = MibTableColumn
oaIfRegulationProblemTxPowerLow = _OaIfRegulationProblemTxPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 30),
    _OaIfRegulationProblemTxPowerLow_Type()
)
oaIfRegulationProblemTxPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfRegulationProblemTxPowerLow.setStatus("current")
_OaIfReceivedPowerLow_Type = FaultStatus
_OaIfReceivedPowerLow_Object = MibTableColumn
oaIfReceivedPowerLow = _OaIfReceivedPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 31),
    _OaIfReceivedPowerLow_Type()
)
oaIfReceivedPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfReceivedPowerLow.setStatus("current")
_OaIfLaserBiasHigh_Type = FaultStatus
_OaIfLaserBiasHigh_Object = MibTableColumn
oaIfLaserBiasHigh = _OaIfLaserBiasHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 32),
    _OaIfLaserBiasHigh_Type()
)
oaIfLaserBiasHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfLaserBiasHigh.setStatus("current")
_OaIfLaserTempControlFault_Type = FaultStatus
_OaIfLaserTempControlFault_Object = MibTableColumn
oaIfLaserTempControlFault = _OaIfLaserTempControlFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 33),
    _OaIfLaserTempControlFault_Type()
)
oaIfLaserTempControlFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfLaserTempControlFault.setStatus("current")
_OaIfHwMissing_Type = FaultStatus
_OaIfHwMissing_Object = MibTableColumn
oaIfHwMissing = _OaIfHwMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 34),
    _OaIfHwMissing_Type()
)
oaIfHwMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfHwMissing.setStatus("deprecated")
_OaIfConfigurationCommand_Type = CommandString
_OaIfConfigurationCommand_Object = MibTableColumn
oaIfConfigurationCommand = _OaIfConfigurationCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 35),
    _OaIfConfigurationCommand_Type()
)
oaIfConfigurationCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfConfigurationCommand.setStatus("current")
_OaIfPumpLaserTempLow_Type = FaultStatus
_OaIfPumpLaserTempLow_Object = MibTableColumn
oaIfPumpLaserTempLow = _OaIfPumpLaserTempLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 36),
    _OaIfPumpLaserTempLow_Type()
)
oaIfPumpLaserTempLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfPumpLaserTempLow.setStatus("current")


class _OaIfLaserTempLowRelativeThreshold_Type(Integer32):
    """Custom type oaIfLaserTempLowRelativeThreshold based on Integer32"""
    defaultValue = -30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 150),
    )


_OaIfLaserTempLowRelativeThreshold_Type.__name__ = "Integer32"
_OaIfLaserTempLowRelativeThreshold_Object = MibTableColumn
oaIfLaserTempLowRelativeThreshold = _OaIfLaserTempLowRelativeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 37),
    _OaIfLaserTempLowRelativeThreshold_Type()
)
oaIfLaserTempLowRelativeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaIfLaserTempLowRelativeThreshold.setStatus("current")


class _OaIfLaserTempHighRelativeThreshold_Type(Integer32):
    """Custom type oaIfLaserTempHighRelativeThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-250, 450),
    )


_OaIfLaserTempHighRelativeThreshold_Type.__name__ = "Integer32"
_OaIfLaserTempHighRelativeThreshold_Object = MibTableColumn
oaIfLaserTempHighRelativeThreshold = _OaIfLaserTempHighRelativeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 38),
    _OaIfLaserTempHighRelativeThreshold_Type()
)
oaIfLaserTempHighRelativeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaIfLaserTempHighRelativeThreshold.setStatus("current")
_OaIfAmpTypeNotSupportedByHw_Type = FaultStatus
_OaIfAmpTypeNotSupportedByHw_Object = MibTableColumn
oaIfAmpTypeNotSupportedByHw = _OaIfAmpTypeNotSupportedByHw_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 39),
    _OaIfAmpTypeNotSupportedByHw_Type()
)
oaIfAmpTypeNotSupportedByHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfAmpTypeNotSupportedByHw.setStatus("current")


class _OaIfWantedSignalPowerLevel_Type(Integer32):
    """Custom type oaIfWantedSignalPowerLevel based on Integer32"""
    defaultValue = -100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, -50),
    )


_OaIfWantedSignalPowerLevel_Type.__name__ = "Integer32"
_OaIfWantedSignalPowerLevel_Object = MibTableColumn
oaIfWantedSignalPowerLevel = _OaIfWantedSignalPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 40),
    _OaIfWantedSignalPowerLevel_Type()
)
oaIfWantedSignalPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaIfWantedSignalPowerLevel.setStatus("current")
_OaIfObjectProperty_Type = ObjectProperty
_OaIfObjectProperty_Object = MibTableColumn
oaIfObjectProperty = _OaIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 41),
    _OaIfObjectProperty_Type()
)
oaIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfObjectProperty.setStatus("current")


class _OaIfLaserForcedOn_Type(Integer32):
    """Custom type oaIfLaserForcedOn based on Integer32"""
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


_OaIfLaserForcedOn_Type.__name__ = "Integer32"
_OaIfLaserForcedOn_Object = MibTableColumn
oaIfLaserForcedOn = _OaIfLaserForcedOn_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 42),
    _OaIfLaserForcedOn_Type()
)
oaIfLaserForcedOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaIfLaserForcedOn.setStatus("current")
_OaIfActualLaserTemp_Type = Integer32
_OaIfActualLaserTemp_Object = MibTableColumn
oaIfActualLaserTemp = _OaIfActualLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 43),
    _OaIfActualLaserTemp_Type()
)
oaIfActualLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfActualLaserTemp.setStatus("current")


class _OaIfAutomaticPowerShutdown_Type(Integer32):
    """Custom type oaIfAutomaticPowerShutdown based on Integer32"""
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


_OaIfAutomaticPowerShutdown_Type.__name__ = "Integer32"
_OaIfAutomaticPowerShutdown_Object = MibTableColumn
oaIfAutomaticPowerShutdown = _OaIfAutomaticPowerShutdown_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 44),
    _OaIfAutomaticPowerShutdown_Type()
)
oaIfAutomaticPowerShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaIfAutomaticPowerShutdown.setStatus("current")
_OaIfDisabled_Type = FaultStatus
_OaIfDisabled_Object = MibTableColumn
oaIfDisabled = _OaIfDisabled_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 45),
    _OaIfDisabled_Type()
)
oaIfDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfDisabled.setStatus("current")


class _OaIfWantedPowerLimit_Type(Integer32):
    """Custom type oaIfWantedPowerLimit based on Integer32"""
    defaultValue = 167

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-70, 195),
    )


_OaIfWantedPowerLimit_Type.__name__ = "Integer32"
_OaIfWantedPowerLimit_Object = MibTableColumn
oaIfWantedPowerLimit = _OaIfWantedPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 46),
    _OaIfWantedPowerLimit_Type()
)
oaIfWantedPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaIfWantedPowerLimit.setStatus("current")
_OaIfModuleInfo_Type = DisplayString
_OaIfModuleInfo_Object = MibTableColumn
oaIfModuleInfo = _OaIfModuleInfo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 47),
    _OaIfModuleInfo_Type()
)
oaIfModuleInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfModuleInfo.setStatus("current")
_OaIfMonitorInsertionLoss_Type = DisplayString
_OaIfMonitorInsertionLoss_Object = MibTableColumn
oaIfMonitorInsertionLoss = _OaIfMonitorInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 48),
    _OaIfMonitorInsertionLoss_Type()
)
oaIfMonitorInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfMonitorInsertionLoss.setStatus("current")
_OaIfNumMonitorInsertionLoss_Type = Unsigned32
_OaIfNumMonitorInsertionLoss_Object = MibTableColumn
oaIfNumMonitorInsertionLoss = _OaIfNumMonitorInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 49),
    _OaIfNumMonitorInsertionLoss_Type()
)
oaIfNumMonitorInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfNumMonitorInsertionLoss.setStatus("current")


class _OaIfFunctionalType_Type(Integer32):
    """Custom type oaIfFunctionalType based on Integer32"""
    defaultValue = 1

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
        *(("undefined", 1),
          ("preAmp", 2),
          ("offLinePreAmp", 3),
          ("lineAmp", 4),
          ("booster", 5))
    )


_OaIfFunctionalType_Type.__name__ = "Integer32"
_OaIfFunctionalType_Object = MibTableColumn
oaIfFunctionalType = _OaIfFunctionalType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 50),
    _OaIfFunctionalType_Type()
)
oaIfFunctionalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaIfFunctionalType.setStatus("current")
_OaIfActualGain_Type = Integer32
_OaIfActualGain_Object = MibTableColumn
oaIfActualGain = _OaIfActualGain_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 51),
    _OaIfActualGain_Type()
)
oaIfActualGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfActualGain.setStatus("current")
_OaIfSaturationFault_Type = FaultStatus
_OaIfSaturationFault_Object = MibTableColumn
oaIfSaturationFault = _OaIfSaturationFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 52),
    _OaIfSaturationFault_Type()
)
oaIfSaturationFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfSaturationFault.setStatus("current")


class _OaIfWantedGainTilt_Type(Integer32):
    """Custom type oaIfWantedGainTilt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_OaIfWantedGainTilt_Type.__name__ = "Integer32"
_OaIfWantedGainTilt_Object = MibTableColumn
oaIfWantedGainTilt = _OaIfWantedGainTilt_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 53),
    _OaIfWantedGainTilt_Type()
)
oaIfWantedGainTilt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaIfWantedGainTilt.setStatus("current")


class _OaIfTxPowerLevelLowThreshold_Type(Integer32):
    """Custom type oaIfTxPowerLevelLowThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 207),
    )


_OaIfTxPowerLevelLowThreshold_Type.__name__ = "Integer32"
_OaIfTxPowerLevelLowThreshold_Object = MibTableColumn
oaIfTxPowerLevelLowThreshold = _OaIfTxPowerLevelLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 54),
    _OaIfTxPowerLevelLowThreshold_Type()
)
oaIfTxPowerLevelLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaIfTxPowerLevelLowThreshold.setStatus("current")
_OaIfLaserPumpBias_Type = Unsigned32
_OaIfLaserPumpBias_Object = MibTableColumn
oaIfLaserPumpBias = _OaIfLaserPumpBias_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 55),
    _OaIfLaserPumpBias_Type()
)
oaIfLaserPumpBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfLaserPumpBias.setStatus("current")
_OaIfCaseTempOutOfrange_Type = FaultStatus
_OaIfCaseTempOutOfrange_Object = MibTableColumn
oaIfCaseTempOutOfrange = _OaIfCaseTempOutOfrange_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 56),
    _OaIfCaseTempOutOfrange_Type()
)
oaIfCaseTempOutOfrange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfCaseTempOutOfrange.setStatus("current")
_OaIfLaserTempOutOfRange_Type = FaultStatus
_OaIfLaserTempOutOfRange_Object = MibTableColumn
oaIfLaserTempOutOfRange = _OaIfLaserTempOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 57),
    _OaIfLaserTempOutOfRange_Type()
)
oaIfLaserTempOutOfRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfLaserTempOutOfRange.setStatus("current")
_OaIfSupportsReadMonitorInsertionLoss_Type = TruthValue
_OaIfSupportsReadMonitorInsertionLoss_Object = MibTableColumn
oaIfSupportsReadMonitorInsertionLoss = _OaIfSupportsReadMonitorInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 58),
    _OaIfSupportsReadMonitorInsertionLoss_Type()
)
oaIfSupportsReadMonitorInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfSupportsReadMonitorInsertionLoss.setStatus("current")


class _OaIfTxSignalStatus_Type(Integer32):
    """Custom type oaIfTxSignalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("degraded", 2),
          ("up", 3),
          ("notApplicable", 2147483647))
    )


_OaIfTxSignalStatus_Type.__name__ = "Integer32"
_OaIfTxSignalStatus_Object = MibTableColumn
oaIfTxSignalStatus = _OaIfTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 59),
    _OaIfTxSignalStatus_Type()
)
oaIfTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfTxSignalStatus.setStatus("current")


class _OaIfRxSignalStatus_Type(Integer32):
    """Custom type oaIfRxSignalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("degraded", 2),
          ("up", 3),
          ("notApplicable", 2147483647))
    )


_OaIfRxSignalStatus_Type.__name__ = "Integer32"
_OaIfRxSignalStatus_Object = MibTableColumn
oaIfRxSignalStatus = _OaIfRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 60),
    _OaIfRxSignalStatus_Type()
)
oaIfRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfRxSignalStatus.setStatus("current")
_OaIfOutputPowerFail_Type = FaultStatus
_OaIfOutputPowerFail_Object = MibTableColumn
oaIfOutputPowerFail = _OaIfOutputPowerFail_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 2, 1, 1, 61),
    _OaIfOutputPowerFail_Type()
)
oaIfOutputPowerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaIfOutputPowerFail.setStatus("current")
_LumentisOaNotifications_ObjectIdentity = ObjectIdentity
lumentisOaNotifications = _LumentisOaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 3)
)
_OaVoaIfList_ObjectIdentity = ObjectIdentity
oaVoaIfList = _OaVoaIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4)
)
_OaVoaIfTable_Object = MibTable
oaVoaIfTable = _OaVoaIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1)
)
if mibBuilder.loadTexts:
    oaVoaIfTable.setStatus("current")
_OaVoaIfEntry_Object = MibTableRow
oaVoaIfEntry = _OaVoaIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1)
)
oaVoaIfEntry.setIndexNames(
    (0, "LUM-OA-MIB", "oaVoaIfIndex"),
)
if mibBuilder.loadTexts:
    oaVoaIfEntry.setStatus("current")


class _OaVoaIfIndex_Type(Unsigned32):
    """Custom type oaVoaIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OaVoaIfIndex_Type.__name__ = "Unsigned32"
_OaVoaIfIndex_Object = MibTableColumn
oaVoaIfIndex = _OaVoaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 1),
    _OaVoaIfIndex_Type()
)
oaVoaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaIfIndex.setStatus("current")
_OaVoaIfName_Type = MgmtNameString
_OaVoaIfName_Object = MibTableColumn
oaVoaIfName = _OaVoaIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 2),
    _OaVoaIfName_Type()
)
oaVoaIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaIfName.setStatus("current")


class _OaVoaIfDescr_Type(DisplayString):
    """Custom type oaVoaIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_OaVoaIfDescr_Type.__name__ = "DisplayString"
_OaVoaIfDescr_Object = MibTableColumn
oaVoaIfDescr = _OaVoaIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 3),
    _OaVoaIfDescr_Type()
)
oaVoaIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaVoaIfDescr.setStatus("current")
_OaVoaIfSubrack_Type = SubrackNumber
_OaVoaIfSubrack_Object = MibTableColumn
oaVoaIfSubrack = _OaVoaIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 4),
    _OaVoaIfSubrack_Type()
)
oaVoaIfSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaIfSubrack.setStatus("current")
_OaVoaIfSlot_Type = SlotNumber
_OaVoaIfSlot_Object = MibTableColumn
oaVoaIfSlot = _OaVoaIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 5),
    _OaVoaIfSlot_Type()
)
oaVoaIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaIfSlot.setStatus("current")
_OaVoaIfTxPort_Type = PortNumber
_OaVoaIfTxPort_Object = MibTableColumn
oaVoaIfTxPort = _OaVoaIfTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 6),
    _OaVoaIfTxPort_Type()
)
oaVoaIfTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaIfTxPort.setStatus("current")
_OaVoaIfRxPort_Type = PortNumber
_OaVoaIfRxPort_Object = MibTableColumn
oaVoaIfRxPort = _OaVoaIfRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 7),
    _OaVoaIfRxPort_Type()
)
oaVoaIfRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaIfRxPort.setStatus("current")


class _OaVoaIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type oaVoaIfInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaVoaIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_OaVoaIfInvPhysIndexOrZero_Object = MibTableColumn
oaVoaIfInvPhysIndexOrZero = _OaVoaIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 8),
    _OaVoaIfInvPhysIndexOrZero_Type()
)
oaVoaIfInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaIfInvPhysIndexOrZero.setStatus("current")
_OaVoaIfAdminStatus_Type = BoardOrInterfaceAdminStatus
_OaVoaIfAdminStatus_Object = MibTableColumn
oaVoaIfAdminStatus = _OaVoaIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 9),
    _OaVoaIfAdminStatus_Type()
)
oaVoaIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaVoaIfAdminStatus.setStatus("current")


class _OaVoaIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type oaVoaIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_OaVoaIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_OaVoaIfOperStatus_Object = MibTableColumn
oaVoaIfOperStatus = _OaVoaIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 10),
    _OaVoaIfOperStatus_Type()
)
oaVoaIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaIfOperStatus.setStatus("current")
_OaVoaIfObjectProperty_Type = ObjectProperty
_OaVoaIfObjectProperty_Object = MibTableColumn
oaVoaIfObjectProperty = _OaVoaIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 11),
    _OaVoaIfObjectProperty_Type()
)
oaVoaIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaIfObjectProperty.setStatus("current")


class _OaVoaIfControlMode_Type(Integer32):
    """Custom type oaVoaIfControlMode based on Integer32"""
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
        *(("constPower", 1),
          ("constAttenuation", 2),
          ("constPowerAtInstallation", 3))
    )


_OaVoaIfControlMode_Type.__name__ = "Integer32"
_OaVoaIfControlMode_Object = MibTableColumn
oaVoaIfControlMode = _OaVoaIfControlMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 12),
    _OaVoaIfControlMode_Type()
)
oaVoaIfControlMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oaVoaIfControlMode.setStatus("current")


class _OaVoaIfWantedOutputPower_Type(Integer32):
    """Custom type oaVoaIfWantedOutputPower based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 170),
    )


_OaVoaIfWantedOutputPower_Type.__name__ = "Integer32"
_OaVoaIfWantedOutputPower_Object = MibTableColumn
oaVoaIfWantedOutputPower = _OaVoaIfWantedOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 13),
    _OaVoaIfWantedOutputPower_Type()
)
oaVoaIfWantedOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaVoaIfWantedOutputPower.setStatus("current")
_OaVoaIfCurrentOutputPower_Type = Integer32
_OaVoaIfCurrentOutputPower_Object = MibTableColumn
oaVoaIfCurrentOutputPower = _OaVoaIfCurrentOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 14),
    _OaVoaIfCurrentOutputPower_Type()
)
oaVoaIfCurrentOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaIfCurrentOutputPower.setStatus("current")


class _OaVoaIfRegulationRange_Type(Unsigned32):
    """Custom type oaVoaIfRegulationRange based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_OaVoaIfRegulationRange_Type.__name__ = "Unsigned32"
_OaVoaIfRegulationRange_Object = MibTableColumn
oaVoaIfRegulationRange = _OaVoaIfRegulationRange_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 15),
    _OaVoaIfRegulationRange_Type()
)
oaVoaIfRegulationRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaVoaIfRegulationRange.setStatus("current")


class _OaVoaIfWantedAttenuation_Type(Unsigned32):
    """Custom type oaVoaIfWantedAttenuation based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_OaVoaIfWantedAttenuation_Type.__name__ = "Unsigned32"
_OaVoaIfWantedAttenuation_Object = MibTableColumn
oaVoaIfWantedAttenuation = _OaVoaIfWantedAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 16),
    _OaVoaIfWantedAttenuation_Type()
)
oaVoaIfWantedAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaVoaIfWantedAttenuation.setStatus("current")
_OaVoaIfCurrentAttenuation_Type = Unsigned32
_OaVoaIfCurrentAttenuation_Object = MibTableColumn
oaVoaIfCurrentAttenuation = _OaVoaIfCurrentAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 17),
    _OaVoaIfCurrentAttenuation_Type()
)
oaVoaIfCurrentAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaIfCurrentAttenuation.setStatus("current")
_OaVoaIfSamplePeriod_Type = Unsigned32
_OaVoaIfSamplePeriod_Object = MibTableColumn
oaVoaIfSamplePeriod = _OaVoaIfSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 18),
    _OaVoaIfSamplePeriod_Type()
)
oaVoaIfSamplePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaIfSamplePeriod.setStatus("current")
_OaVoaIfOuputPowerControlFailure_Type = FaultStatus
_OaVoaIfOuputPowerControlFailure_Object = MibTableColumn
oaVoaIfOuputPowerControlFailure = _OaVoaIfOuputPowerControlFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 19),
    _OaVoaIfOuputPowerControlFailure_Type()
)
oaVoaIfOuputPowerControlFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaIfOuputPowerControlFailure.setStatus("current")
_OaVoaIfCurrentPowerOutOfRange_Type = FaultStatus
_OaVoaIfCurrentPowerOutOfRange_Object = MibTableColumn
oaVoaIfCurrentPowerOutOfRange = _OaVoaIfCurrentPowerOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 20),
    _OaVoaIfCurrentPowerOutOfRange_Type()
)
oaVoaIfCurrentPowerOutOfRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaIfCurrentPowerOutOfRange.setStatus("current")
_OaVoaIfConfigurationCommand_Type = CommandString
_OaVoaIfConfigurationCommand_Object = MibTableColumn
oaVoaIfConfigurationCommand = _OaVoaIfConfigurationCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 21),
    _OaVoaIfConfigurationCommand_Type()
)
oaVoaIfConfigurationCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaIfConfigurationCommand.setStatus("current")
_OaVoaIfInInstallationMode_Type = FaultStatus
_OaVoaIfInInstallationMode_Object = MibTableColumn
oaVoaIfInInstallationMode = _OaVoaIfInInstallationMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 4, 1, 1, 22),
    _OaVoaIfInInstallationMode_Type()
)
oaVoaIfInInstallationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaIfInInstallationMode.setStatus("current")
_OaVoaClientIfList_ObjectIdentity = ObjectIdentity
oaVoaClientIfList = _OaVoaClientIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5)
)
_OaVoaClientIfTable_Object = MibTable
oaVoaClientIfTable = _OaVoaClientIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1)
)
if mibBuilder.loadTexts:
    oaVoaClientIfTable.setStatus("current")
_OaVoaClientIfEntry_Object = MibTableRow
oaVoaClientIfEntry = _OaVoaClientIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1)
)
oaVoaClientIfEntry.setIndexNames(
    (0, "LUM-OA-MIB", "oaVoaClientIfIndex"),
)
if mibBuilder.loadTexts:
    oaVoaClientIfEntry.setStatus("current")


class _OaVoaClientIfIndex_Type(Unsigned32):
    """Custom type oaVoaClientIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OaVoaClientIfIndex_Type.__name__ = "Unsigned32"
_OaVoaClientIfIndex_Object = MibTableColumn
oaVoaClientIfIndex = _OaVoaClientIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 1),
    _OaVoaClientIfIndex_Type()
)
oaVoaClientIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfIndex.setStatus("current")
_OaVoaClientIfName_Type = MgmtNameString
_OaVoaClientIfName_Object = MibTableColumn
oaVoaClientIfName = _OaVoaClientIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 2),
    _OaVoaClientIfName_Type()
)
oaVoaClientIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfName.setStatus("current")


class _OaVoaClientIfDescr_Type(DisplayString):
    """Custom type oaVoaClientIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_OaVoaClientIfDescr_Type.__name__ = "DisplayString"
_OaVoaClientIfDescr_Object = MibTableColumn
oaVoaClientIfDescr = _OaVoaClientIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 3),
    _OaVoaClientIfDescr_Type()
)
oaVoaClientIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaVoaClientIfDescr.setStatus("current")
_OaVoaClientIfSubrack_Type = SubrackNumber
_OaVoaClientIfSubrack_Object = MibTableColumn
oaVoaClientIfSubrack = _OaVoaClientIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 4),
    _OaVoaClientIfSubrack_Type()
)
oaVoaClientIfSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfSubrack.setStatus("current")
_OaVoaClientIfSlot_Type = SlotNumber
_OaVoaClientIfSlot_Object = MibTableColumn
oaVoaClientIfSlot = _OaVoaClientIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 5),
    _OaVoaClientIfSlot_Type()
)
oaVoaClientIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfSlot.setStatus("current")
_OaVoaClientIfTxPort_Type = PortNumber
_OaVoaClientIfTxPort_Object = MibTableColumn
oaVoaClientIfTxPort = _OaVoaClientIfTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 6),
    _OaVoaClientIfTxPort_Type()
)
oaVoaClientIfTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfTxPort.setStatus("current")
_OaVoaClientIfRxPort_Type = PortNumber
_OaVoaClientIfRxPort_Object = MibTableColumn
oaVoaClientIfRxPort = _OaVoaClientIfRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 7),
    _OaVoaClientIfRxPort_Type()
)
oaVoaClientIfRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfRxPort.setStatus("current")


class _OaVoaClientIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type oaVoaClientIfInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaVoaClientIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_OaVoaClientIfInvPhysIndexOrZero_Object = MibTableColumn
oaVoaClientIfInvPhysIndexOrZero = _OaVoaClientIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 8),
    _OaVoaClientIfInvPhysIndexOrZero_Type()
)
oaVoaClientIfInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfInvPhysIndexOrZero.setStatus("current")


class _OaVoaClientIfAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type oaVoaClientIfAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_OaVoaClientIfAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_OaVoaClientIfAdminStatus_Object = MibTableColumn
oaVoaClientIfAdminStatus = _OaVoaClientIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 9),
    _OaVoaClientIfAdminStatus_Type()
)
oaVoaClientIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaVoaClientIfAdminStatus.setStatus("current")


class _OaVoaClientIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type oaVoaClientIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_OaVoaClientIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_OaVoaClientIfOperStatus_Object = MibTableColumn
oaVoaClientIfOperStatus = _OaVoaClientIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 10),
    _OaVoaClientIfOperStatus_Type()
)
oaVoaClientIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfOperStatus.setStatus("current")
_OaVoaClientIfObjectProperty_Type = ObjectProperty
_OaVoaClientIfObjectProperty_Object = MibTableColumn
oaVoaClientIfObjectProperty = _OaVoaClientIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 11),
    _OaVoaClientIfObjectProperty_Type()
)
oaVoaClientIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfObjectProperty.setStatus("current")


class _OaVoaClientIfControlMode_Type(Integer32):
    """Custom type oaVoaClientIfControlMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("constAttenuation", 1)
    )


_OaVoaClientIfControlMode_Type.__name__ = "Integer32"
_OaVoaClientIfControlMode_Object = MibTableColumn
oaVoaClientIfControlMode = _OaVoaClientIfControlMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 12),
    _OaVoaClientIfControlMode_Type()
)
oaVoaClientIfControlMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oaVoaClientIfControlMode.setStatus("current")


class _OaVoaClientIfWantedAttenuation_Type(Unsigned32):
    """Custom type oaVoaClientIfWantedAttenuation based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_OaVoaClientIfWantedAttenuation_Type.__name__ = "Unsigned32"
_OaVoaClientIfWantedAttenuation_Object = MibTableColumn
oaVoaClientIfWantedAttenuation = _OaVoaClientIfWantedAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 13),
    _OaVoaClientIfWantedAttenuation_Type()
)
oaVoaClientIfWantedAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaVoaClientIfWantedAttenuation.setStatus("current")
_OaVoaClientIfCurrentAttenuation_Type = Unsigned32
_OaVoaClientIfCurrentAttenuation_Object = MibTableColumn
oaVoaClientIfCurrentAttenuation = _OaVoaClientIfCurrentAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 14),
    _OaVoaClientIfCurrentAttenuation_Type()
)
oaVoaClientIfCurrentAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfCurrentAttenuation.setStatus("current")
_OaVoaClientIfLambda_Type = LambdaFrequency
_OaVoaClientIfLambda_Object = MibTableColumn
oaVoaClientIfLambda = _OaVoaClientIfLambda_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 15),
    _OaVoaClientIfLambda_Type()
)
oaVoaClientIfLambda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfLambda.setStatus("current")


class _OaVoaClientIfAbsoluteAttenuation_Type(Unsigned32):
    """Custom type oaVoaClientIfAbsoluteAttenuation based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OaVoaClientIfAbsoluteAttenuation_Type.__name__ = "Unsigned32"
_OaVoaClientIfAbsoluteAttenuation_Object = MibTableColumn
oaVoaClientIfAbsoluteAttenuation = _OaVoaClientIfAbsoluteAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 16),
    _OaVoaClientIfAbsoluteAttenuation_Type()
)
oaVoaClientIfAbsoluteAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaVoaClientIfAbsoluteAttenuation.setStatus("current")


class _OaVoaClientIfVoa2CurrentAttenuation_Type(Unsigned32):
    """Custom type oaVoaClientIfVoa2CurrentAttenuation based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OaVoaClientIfVoa2CurrentAttenuation_Type.__name__ = "Unsigned32"
_OaVoaClientIfVoa2CurrentAttenuation_Object = MibTableColumn
oaVoaClientIfVoa2CurrentAttenuation = _OaVoaClientIfVoa2CurrentAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 17),
    _OaVoaClientIfVoa2CurrentAttenuation_Type()
)
oaVoaClientIfVoa2CurrentAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfVoa2CurrentAttenuation.setStatus("current")


class _OaVoaClientIfDecreaseAttenuation_Type(Unsigned32):
    """Custom type oaVoaClientIfDecreaseAttenuation based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OaVoaClientIfDecreaseAttenuation_Type.__name__ = "Unsigned32"
_OaVoaClientIfDecreaseAttenuation_Object = MibTableColumn
oaVoaClientIfDecreaseAttenuation = _OaVoaClientIfDecreaseAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 18),
    _OaVoaClientIfDecreaseAttenuation_Type()
)
oaVoaClientIfDecreaseAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaVoaClientIfDecreaseAttenuation.setStatus("current")


class _OaVoaClientIfIncreaseAttenuation_Type(Unsigned32):
    """Custom type oaVoaClientIfIncreaseAttenuation based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OaVoaClientIfIncreaseAttenuation_Type.__name__ = "Unsigned32"
_OaVoaClientIfIncreaseAttenuation_Object = MibTableColumn
oaVoaClientIfIncreaseAttenuation = _OaVoaClientIfIncreaseAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 19),
    _OaVoaClientIfIncreaseAttenuation_Type()
)
oaVoaClientIfIncreaseAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaVoaClientIfIncreaseAttenuation.setStatus("current")


class _OaVoaClientIfInsertionLoss_Type(Unsigned32):
    """Custom type oaVoaClientIfInsertionLoss based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_OaVoaClientIfInsertionLoss_Type.__name__ = "Unsigned32"
_OaVoaClientIfInsertionLoss_Object = MibTableColumn
oaVoaClientIfInsertionLoss = _OaVoaClientIfInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 20),
    _OaVoaClientIfInsertionLoss_Type()
)
oaVoaClientIfInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfInsertionLoss.setStatus("current")


class _OaVoaClientIfExpectedFrequency_Type(LambdaFrequency):
    """Custom type oaVoaClientIfExpectedFrequency based on LambdaFrequency"""
    defaultValue = 0


_OaVoaClientIfExpectedFrequency_Type.__name__ = "LambdaFrequency"
_OaVoaClientIfExpectedFrequency_Object = MibTableColumn
oaVoaClientIfExpectedFrequency = _OaVoaClientIfExpectedFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 21),
    _OaVoaClientIfExpectedFrequency_Type()
)
oaVoaClientIfExpectedFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaVoaClientIfExpectedFrequency.setStatus("current")
_OaVoaClientIfSfpMissing_Type = FaultStatus
_OaVoaClientIfSfpMissing_Object = MibTableColumn
oaVoaClientIfSfpMissing = _OaVoaClientIfSfpMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 22),
    _OaVoaClientIfSfpMissing_Type()
)
oaVoaClientIfSfpMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfSfpMissing.setStatus("current")


class _OaVoaClientIfSfpClass_Type(DisplayString):
    """Custom type oaVoaClientIfSfpClass based on DisplayString"""
    defaultValue = OctetString("")


_OaVoaClientIfSfpClass_Type.__name__ = "DisplayString"
_OaVoaClientIfSfpClass_Object = MibTableColumn
oaVoaClientIfSfpClass = _OaVoaClientIfSfpClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 23),
    _OaVoaClientIfSfpClass_Type()
)
oaVoaClientIfSfpClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfSfpClass.setStatus("current")
_OaVoaClientIfSfpTransmitterFailed_Type = FaultStatus
_OaVoaClientIfSfpTransmitterFailed_Object = MibTableColumn
oaVoaClientIfSfpTransmitterFailed = _OaVoaClientIfSfpTransmitterFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 24),
    _OaVoaClientIfSfpTransmitterFailed_Type()
)
oaVoaClientIfSfpTransmitterFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfSfpTransmitterFailed.setStatus("current")
_OaVoaClientIfSfpMediaMismatch_Type = FaultStatus
_OaVoaClientIfSfpMediaMismatch_Object = MibTableColumn
oaVoaClientIfSfpMediaMismatch = _OaVoaClientIfSfpMediaMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 25),
    _OaVoaClientIfSfpMediaMismatch_Type()
)
oaVoaClientIfSfpMediaMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfSfpMediaMismatch.setStatus("current")
_OaVoaClientIfLossOfSignal_Type = FaultStatus
_OaVoaClientIfLossOfSignal_Object = MibTableColumn
oaVoaClientIfLossOfSignal = _OaVoaClientIfLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 26),
    _OaVoaClientIfLossOfSignal_Type()
)
oaVoaClientIfLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfLossOfSignal.setStatus("current")
_OaVoaClientIfSfpCodeMismatch_Type = FaultStatus
_OaVoaClientIfSfpCodeMismatch_Object = MibTableColumn
oaVoaClientIfSfpCodeMismatch = _OaVoaClientIfSfpCodeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 27),
    _OaVoaClientIfSfpCodeMismatch_Type()
)
oaVoaClientIfSfpCodeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfSfpCodeMismatch.setStatus("current")
_OaVoaClientIfAttenuationConfigMismatch_Type = FaultStatus
_OaVoaClientIfAttenuationConfigMismatch_Object = MibTableColumn
oaVoaClientIfAttenuationConfigMismatch = _OaVoaClientIfAttenuationConfigMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 5, 1, 1, 28),
    _OaVoaClientIfAttenuationConfigMismatch_Type()
)
oaVoaClientIfAttenuationConfigMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaClientIfAttenuationConfigMismatch.setStatus("current")
_OaVoaLineIfList_ObjectIdentity = ObjectIdentity
oaVoaLineIfList = _OaVoaLineIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 6)
)
_OaVoaLineIfTable_Object = MibTable
oaVoaLineIfTable = _OaVoaLineIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 6, 1)
)
if mibBuilder.loadTexts:
    oaVoaLineIfTable.setStatus("current")
_OaVoaLineIfEntry_Object = MibTableRow
oaVoaLineIfEntry = _OaVoaLineIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 6, 1, 1)
)
oaVoaLineIfEntry.setIndexNames(
    (0, "LUM-OA-MIB", "oaVoaLineIfIndex"),
)
if mibBuilder.loadTexts:
    oaVoaLineIfEntry.setStatus("current")


class _OaVoaLineIfIndex_Type(Unsigned32):
    """Custom type oaVoaLineIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OaVoaLineIfIndex_Type.__name__ = "Unsigned32"
_OaVoaLineIfIndex_Object = MibTableColumn
oaVoaLineIfIndex = _OaVoaLineIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 6, 1, 1, 1),
    _OaVoaLineIfIndex_Type()
)
oaVoaLineIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaLineIfIndex.setStatus("current")
_OaVoaLineIfName_Type = MgmtNameString
_OaVoaLineIfName_Object = MibTableColumn
oaVoaLineIfName = _OaVoaLineIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 6, 1, 1, 2),
    _OaVoaLineIfName_Type()
)
oaVoaLineIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaLineIfName.setStatus("current")


class _OaVoaLineIfDescr_Type(DisplayString):
    """Custom type oaVoaLineIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_OaVoaLineIfDescr_Type.__name__ = "DisplayString"
_OaVoaLineIfDescr_Object = MibTableColumn
oaVoaLineIfDescr = _OaVoaLineIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 6, 1, 1, 3),
    _OaVoaLineIfDescr_Type()
)
oaVoaLineIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaVoaLineIfDescr.setStatus("current")
_OaVoaLineIfSubrack_Type = SubrackNumber
_OaVoaLineIfSubrack_Object = MibTableColumn
oaVoaLineIfSubrack = _OaVoaLineIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 6, 1, 1, 4),
    _OaVoaLineIfSubrack_Type()
)
oaVoaLineIfSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oaVoaLineIfSubrack.setStatus("current")
_OaVoaLineIfSlot_Type = SlotNumber
_OaVoaLineIfSlot_Object = MibTableColumn
oaVoaLineIfSlot = _OaVoaLineIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 6, 1, 1, 5),
    _OaVoaLineIfSlot_Type()
)
oaVoaLineIfSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oaVoaLineIfSlot.setStatus("current")
_OaVoaLineIfTxPort_Type = PortNumber
_OaVoaLineIfTxPort_Object = MibTableColumn
oaVoaLineIfTxPort = _OaVoaLineIfTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 6, 1, 1, 6),
    _OaVoaLineIfTxPort_Type()
)
oaVoaLineIfTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oaVoaLineIfTxPort.setStatus("current")
_OaVoaLineIfRxPort_Type = PortNumber
_OaVoaLineIfRxPort_Object = MibTableColumn
oaVoaLineIfRxPort = _OaVoaLineIfRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 6, 1, 1, 7),
    _OaVoaLineIfRxPort_Type()
)
oaVoaLineIfRxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oaVoaLineIfRxPort.setStatus("current")


class _OaVoaLineIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type oaVoaLineIfInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaVoaLineIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_OaVoaLineIfInvPhysIndexOrZero_Object = MibTableColumn
oaVoaLineIfInvPhysIndexOrZero = _OaVoaLineIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 6, 1, 1, 8),
    _OaVoaLineIfInvPhysIndexOrZero_Type()
)
oaVoaLineIfInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaLineIfInvPhysIndexOrZero.setStatus("current")


class _OaVoaLineIfAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type oaVoaLineIfAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_OaVoaLineIfAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_OaVoaLineIfAdminStatus_Object = MibTableColumn
oaVoaLineIfAdminStatus = _OaVoaLineIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 6, 1, 1, 9),
    _OaVoaLineIfAdminStatus_Type()
)
oaVoaLineIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaVoaLineIfAdminStatus.setStatus("current")


class _OaVoaLineIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type oaVoaLineIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_OaVoaLineIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_OaVoaLineIfOperStatus_Object = MibTableColumn
oaVoaLineIfOperStatus = _OaVoaLineIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 6, 1, 1, 10),
    _OaVoaLineIfOperStatus_Type()
)
oaVoaLineIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaLineIfOperStatus.setStatus("current")
_OaVoaLineIfModuleFailure_Type = FaultStatus
_OaVoaLineIfModuleFailure_Object = MibTableColumn
oaVoaLineIfModuleFailure = _OaVoaLineIfModuleFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 6, 1, 1, 11),
    _OaVoaLineIfModuleFailure_Type()
)
oaVoaLineIfModuleFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaLineIfModuleFailure.setStatus("current")
_OaVoaLineIfObjectProperty_Type = ObjectProperty
_OaVoaLineIfObjectProperty_Object = MibTableColumn
oaVoaLineIfObjectProperty = _OaVoaLineIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 6, 1, 1, 12),
    _OaVoaLineIfObjectProperty_Type()
)
oaVoaLineIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVoaLineIfObjectProperty.setStatus("current")
_OaModuleList_ObjectIdentity = ObjectIdentity
oaModuleList = _OaModuleList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7)
)
_OaModuleTable_Object = MibTable
oaModuleTable = _OaModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1)
)
if mibBuilder.loadTexts:
    oaModuleTable.setStatus("current")
_OaModuleEntry_Object = MibTableRow
oaModuleEntry = _OaModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1)
)
oaModuleEntry.setIndexNames(
    (0, "LUM-OA-MIB", "oaModuleIndex"),
)
if mibBuilder.loadTexts:
    oaModuleEntry.setStatus("current")


class _OaModuleIndex_Type(Unsigned32):
    """Custom type oaModuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OaModuleIndex_Type.__name__ = "Unsigned32"
_OaModuleIndex_Object = MibTableColumn
oaModuleIndex = _OaModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 1),
    _OaModuleIndex_Type()
)
oaModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaModuleIndex.setStatus("current")
_OaModuleName_Type = MgmtNameString
_OaModuleName_Object = MibTableColumn
oaModuleName = _OaModuleName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 2),
    _OaModuleName_Type()
)
oaModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaModuleName.setStatus("current")


class _OaModuleDescr_Type(DisplayString):
    """Custom type oaModuleDescr based on DisplayString"""
    defaultValue = OctetString("")


_OaModuleDescr_Type.__name__ = "DisplayString"
_OaModuleDescr_Object = MibTableColumn
oaModuleDescr = _OaModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 3),
    _OaModuleDescr_Type()
)
oaModuleDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaModuleDescr.setStatus("current")
_OaModuleSubrack_Type = SubrackNumber
_OaModuleSubrack_Object = MibTableColumn
oaModuleSubrack = _OaModuleSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 4),
    _OaModuleSubrack_Type()
)
oaModuleSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaModuleSubrack.setStatus("current")
_OaModuleSlot_Type = SlotNumber
_OaModuleSlot_Object = MibTableColumn
oaModuleSlot = _OaModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 5),
    _OaModuleSlot_Type()
)
oaModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaModuleSlot.setStatus("current")
_OaModuleNumber_Type = PortNumber
_OaModuleNumber_Object = MibTableColumn
oaModuleNumber = _OaModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 6),
    _OaModuleNumber_Type()
)
oaModuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaModuleNumber.setStatus("current")


class _OaModuleInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type oaModuleInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaModuleInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_OaModuleInvPhysIndexOrZero_Object = MibTableColumn
oaModuleInvPhysIndexOrZero = _OaModuleInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 7),
    _OaModuleInvPhysIndexOrZero_Type()
)
oaModuleInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaModuleInvPhysIndexOrZero.setStatus("current")


class _OaModuleAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type oaModuleAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_OaModuleAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_OaModuleAdminStatus_Object = MibTableColumn
oaModuleAdminStatus = _OaModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 8),
    _OaModuleAdminStatus_Type()
)
oaModuleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaModuleAdminStatus.setStatus("current")


class _OaModuleOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type oaModuleOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_OaModuleOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_OaModuleOperStatus_Object = MibTableColumn
oaModuleOperStatus = _OaModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 9),
    _OaModuleOperStatus_Type()
)
oaModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaModuleOperStatus.setStatus("current")
_OaModuleObjectProperty_Type = ObjectProperty
_OaModuleObjectProperty_Object = MibTableColumn
oaModuleObjectProperty = _OaModuleObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 10),
    _OaModuleObjectProperty_Type()
)
oaModuleObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaModuleObjectProperty.setStatus("current")
_OaModuleNominalTemp_Type = Integer32
_OaModuleNominalTemp_Object = MibTableColumn
oaModuleNominalTemp = _OaModuleNominalTemp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 11),
    _OaModuleNominalTemp_Type()
)
oaModuleNominalTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaModuleNominalTemp.setStatus("current")
_OaModuleRelativeTemp_Type = Integer32
_OaModuleRelativeTemp_Object = MibTableColumn
oaModuleRelativeTemp = _OaModuleRelativeTemp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 12),
    _OaModuleRelativeTemp_Type()
)
oaModuleRelativeTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaModuleRelativeTemp.setStatus("current")
_OaModuleTempFailure_Type = FaultStatus
_OaModuleTempFailure_Object = MibTableColumn
oaModuleTempFailure = _OaModuleTempFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 13),
    _OaModuleTempFailure_Type()
)
oaModuleTempFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaModuleTempFailure.setStatus("current")
_OaModuleTemperature_Type = Integer32
_OaModuleTemperature_Object = MibTableColumn
oaModuleTemperature = _OaModuleTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 14),
    _OaModuleTemperature_Type()
)
oaModuleTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaModuleTemperature.setStatus("current")
_OaModuleCommunicationFailure_Type = FaultStatus
_OaModuleCommunicationFailure_Object = MibTableColumn
oaModuleCommunicationFailure = _OaModuleCommunicationFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 15),
    _OaModuleCommunicationFailure_Type()
)
oaModuleCommunicationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaModuleCommunicationFailure.setStatus("current")
_OaModuleModuleInfo_Type = DisplayString
_OaModuleModuleInfo_Object = MibTableColumn
oaModuleModuleInfo = _OaModuleModuleInfo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 16),
    _OaModuleModuleInfo_Type()
)
oaModuleModuleInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaModuleModuleInfo.setStatus("current")
_OaModuleVcomThresholdExceeded_Type = FaultStatus
_OaModuleVcomThresholdExceeded_Object = MibTableColumn
oaModuleVcomThresholdExceeded = _OaModuleVcomThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 17),
    _OaModuleVcomThresholdExceeded_Type()
)
oaModuleVcomThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaModuleVcomThresholdExceeded.setStatus("deprecated")
_OaModuleFirmwareUpgradeAvailable_Type = FaultStatus
_OaModuleFirmwareUpgradeAvailable_Object = MibTableColumn
oaModuleFirmwareUpgradeAvailable = _OaModuleFirmwareUpgradeAvailable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 18),
    _OaModuleFirmwareUpgradeAvailable_Type()
)
oaModuleFirmwareUpgradeAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaModuleFirmwareUpgradeAvailable.setStatus("current")
_OaModuleWarmingUp_Type = FaultStatus
_OaModuleWarmingUp_Object = MibTableColumn
oaModuleWarmingUp = _OaModuleWarmingUp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 19),
    _OaModuleWarmingUp_Type()
)
oaModuleWarmingUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaModuleWarmingUp.setStatus("current")
_OaModuleFailure_Type = FaultStatus
_OaModuleFailure_Object = MibTableColumn
oaModuleFailure = _OaModuleFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 2, 7, 1, 1, 20),
    _OaModuleFailure_Type()
)
oaModuleFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaModuleFailure.setStatus("current")

# Managed Objects groups

oaGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 1)
)
oaGeneralGroup.setObjects(
      *(("LUM-OA-MIB", "oaGeneralLastChangeTime"),
        ("LUM-OA-MIB", "oaGeneralStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    oaGeneralGroup.setStatus("deprecated")

oaIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 2)
)
oaIfGroup.setObjects(
      *(("LUM-OA-MIB", "oaIfIndex"),
        ("LUM-OA-MIB", "oaIfName"),
        ("LUM-OA-MIB", "oaIfDescr"),
        ("LUM-OA-MIB", "oaIfSubrack"),
        ("LUM-OA-MIB", "oaIfSlot"),
        ("LUM-OA-MIB", "oaIfTxPort"),
        ("LUM-OA-MIB", "oaIfRxPort"),
        ("LUM-OA-MIB", "oaIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaIfAdminStatus"),
        ("LUM-OA-MIB", "oaIfOperStatus"),
        ("LUM-OA-MIB", "oaIfLaserStatus"),
        ("LUM-OA-MIB", "oaIfAmplifierType"),
        ("LUM-OA-MIB", "oaIfWantedAbsolutePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedRelativePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedGain"),
        ("LUM-OA-MIB", "oaIfFrequencyMin"),
        ("LUM-OA-MIB", "oaIfFrequencyMax"),
        ("LUM-OA-MIB", "oaIfNominalTxPower"),
        ("LUM-OA-MIB", "oaIfTxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserBias"),
        ("LUM-OA-MIB", "oaIfNominalLaserTemp"),
        ("LUM-OA-MIB", "oaIfRelativeLaserTemp"),
        ("LUM-OA-MIB", "oaIfLossOfSignalThreshold"),
        ("LUM-OA-MIB", "oaIfLossOfSignal"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemRxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerLow"),
        ("LUM-OA-MIB", "oaIfReceivedPowerLow"),
        ("LUM-OA-MIB", "oaIfLaserBiasHigh"),
        ("LUM-OA-MIB", "oaIfLaserTempControlFault"),
        ("LUM-OA-MIB", "oaIfHwMissing"))
)
if mibBuilder.loadTexts:
    oaIfGroup.setStatus("deprecated")

oaIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 3)
)
oaIfGroupV2.setObjects(
      *(("LUM-OA-MIB", "oaIfIndex"),
        ("LUM-OA-MIB", "oaIfName"),
        ("LUM-OA-MIB", "oaIfDescr"),
        ("LUM-OA-MIB", "oaIfSubrack"),
        ("LUM-OA-MIB", "oaIfSlot"),
        ("LUM-OA-MIB", "oaIfTxPort"),
        ("LUM-OA-MIB", "oaIfRxPort"),
        ("LUM-OA-MIB", "oaIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaIfAdminStatus"),
        ("LUM-OA-MIB", "oaIfOperStatus"),
        ("LUM-OA-MIB", "oaIfLaserStatus"),
        ("LUM-OA-MIB", "oaIfAmplifierType"),
        ("LUM-OA-MIB", "oaIfWantedAbsolutePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedRelativePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedGain"),
        ("LUM-OA-MIB", "oaIfFrequencyMin"),
        ("LUM-OA-MIB", "oaIfFrequencyMax"),
        ("LUM-OA-MIB", "oaIfNominalTxPower"),
        ("LUM-OA-MIB", "oaIfTxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserBias"),
        ("LUM-OA-MIB", "oaIfNominalLaserTemp"),
        ("LUM-OA-MIB", "oaIfRelativeLaserTemp"),
        ("LUM-OA-MIB", "oaIfLossOfSignalThreshold"),
        ("LUM-OA-MIB", "oaIfLossOfSignal"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemRxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerLow"),
        ("LUM-OA-MIB", "oaIfReceivedPowerLow"),
        ("LUM-OA-MIB", "oaIfLaserBiasHigh"),
        ("LUM-OA-MIB", "oaIfLaserTempControlFault"))
)
if mibBuilder.loadTexts:
    oaIfGroupV2.setStatus("deprecated")

oaIfGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 4)
)
oaIfGroupV3.setObjects(
      *(("LUM-OA-MIB", "oaIfIndex"),
        ("LUM-OA-MIB", "oaIfName"),
        ("LUM-OA-MIB", "oaIfDescr"),
        ("LUM-OA-MIB", "oaIfSubrack"),
        ("LUM-OA-MIB", "oaIfSlot"),
        ("LUM-OA-MIB", "oaIfTxPort"),
        ("LUM-OA-MIB", "oaIfRxPort"),
        ("LUM-OA-MIB", "oaIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaIfAdminStatus"),
        ("LUM-OA-MIB", "oaIfOperStatus"),
        ("LUM-OA-MIB", "oaIfLaserStatus"),
        ("LUM-OA-MIB", "oaIfAmplifierType"),
        ("LUM-OA-MIB", "oaIfWantedAbsolutePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedRelativePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedGain"),
        ("LUM-OA-MIB", "oaIfFrequencyMin"),
        ("LUM-OA-MIB", "oaIfFrequencyMax"),
        ("LUM-OA-MIB", "oaIfNominalTxPower"),
        ("LUM-OA-MIB", "oaIfTxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserBias"),
        ("LUM-OA-MIB", "oaIfNominalLaserTemp"),
        ("LUM-OA-MIB", "oaIfRelativeLaserTemp"),
        ("LUM-OA-MIB", "oaIfLossOfSignalThreshold"),
        ("LUM-OA-MIB", "oaIfLossOfSignal"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemRxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerLow"),
        ("LUM-OA-MIB", "oaIfReceivedPowerLow"),
        ("LUM-OA-MIB", "oaIfLaserBiasHigh"),
        ("LUM-OA-MIB", "oaIfLaserTempControlFault"),
        ("LUM-OA-MIB", "oaIfConfigurationCommand"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempLow"),
        ("LUM-OA-MIB", "oaIfLaserTempLowRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfLaserTempHighRelativeThreshold"))
)
if mibBuilder.loadTexts:
    oaIfGroupV3.setStatus("deprecated")

oaGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 5)
)
oaGeneralGroupV2.setObjects(
      *(("LUM-OA-MIB", "oaGeneralLastChangeTime"),
        ("LUM-OA-MIB", "oaGeneralStateLastChangeTime"),
        ("LUM-OA-MIB", "oaGeneralOaIfTableSize"))
)
if mibBuilder.loadTexts:
    oaGeneralGroupV2.setStatus("current")

oaIfGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 6)
)
oaIfGroupV4.setObjects(
      *(("LUM-OA-MIB", "oaIfIndex"),
        ("LUM-OA-MIB", "oaIfName"),
        ("LUM-OA-MIB", "oaIfDescr"),
        ("LUM-OA-MIB", "oaIfSubrack"),
        ("LUM-OA-MIB", "oaIfSlot"),
        ("LUM-OA-MIB", "oaIfTxPort"),
        ("LUM-OA-MIB", "oaIfRxPort"),
        ("LUM-OA-MIB", "oaIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaIfAdminStatus"),
        ("LUM-OA-MIB", "oaIfOperStatus"),
        ("LUM-OA-MIB", "oaIfLaserStatus"),
        ("LUM-OA-MIB", "oaIfAmplifierType"),
        ("LUM-OA-MIB", "oaIfWantedAbsolutePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedRelativePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedGain"),
        ("LUM-OA-MIB", "oaIfFrequencyMin"),
        ("LUM-OA-MIB", "oaIfFrequencyMax"),
        ("LUM-OA-MIB", "oaIfNominalTxPower"),
        ("LUM-OA-MIB", "oaIfTxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserBias"),
        ("LUM-OA-MIB", "oaIfNominalLaserTemp"),
        ("LUM-OA-MIB", "oaIfRelativeLaserTemp"),
        ("LUM-OA-MIB", "oaIfLossOfSignalThreshold"),
        ("LUM-OA-MIB", "oaIfLossOfSignal"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemRxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerLow"),
        ("LUM-OA-MIB", "oaIfReceivedPowerLow"),
        ("LUM-OA-MIB", "oaIfLaserBiasHigh"),
        ("LUM-OA-MIB", "oaIfLaserTempControlFault"),
        ("LUM-OA-MIB", "oaIfConfigurationCommand"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempLow"),
        ("LUM-OA-MIB", "oaIfLaserTempLowRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfLaserTempHighRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfAmpTypeNotSupportedByHw"),
        ("LUM-OA-MIB", "oaIfWantedSignalPowerLevel"))
)
if mibBuilder.loadTexts:
    oaIfGroupV4.setStatus("deprecated")

oaIfGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 7)
)
oaIfGroupV5.setObjects(
      *(("LUM-OA-MIB", "oaIfIndex"),
        ("LUM-OA-MIB", "oaIfName"),
        ("LUM-OA-MIB", "oaIfDescr"),
        ("LUM-OA-MIB", "oaIfSubrack"),
        ("LUM-OA-MIB", "oaIfSlot"),
        ("LUM-OA-MIB", "oaIfTxPort"),
        ("LUM-OA-MIB", "oaIfRxPort"),
        ("LUM-OA-MIB", "oaIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaIfAdminStatus"),
        ("LUM-OA-MIB", "oaIfOperStatus"),
        ("LUM-OA-MIB", "oaIfLaserStatus"),
        ("LUM-OA-MIB", "oaIfAmplifierType"),
        ("LUM-OA-MIB", "oaIfWantedAbsolutePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedRelativePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedGain"),
        ("LUM-OA-MIB", "oaIfFrequencyMin"),
        ("LUM-OA-MIB", "oaIfFrequencyMax"),
        ("LUM-OA-MIB", "oaIfNominalTxPower"),
        ("LUM-OA-MIB", "oaIfTxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserBias"),
        ("LUM-OA-MIB", "oaIfNominalLaserTemp"),
        ("LUM-OA-MIB", "oaIfRelativeLaserTemp"),
        ("LUM-OA-MIB", "oaIfLossOfSignalThreshold"),
        ("LUM-OA-MIB", "oaIfLossOfSignal"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemRxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerLow"),
        ("LUM-OA-MIB", "oaIfReceivedPowerLow"),
        ("LUM-OA-MIB", "oaIfLaserBiasHigh"),
        ("LUM-OA-MIB", "oaIfLaserTempControlFault"),
        ("LUM-OA-MIB", "oaIfConfigurationCommand"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempLow"),
        ("LUM-OA-MIB", "oaIfLaserTempLowRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfLaserTempHighRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfAmpTypeNotSupportedByHw"),
        ("LUM-OA-MIB", "oaIfWantedSignalPowerLevel"),
        ("LUM-OA-MIB", "oaIfObjectProperty"),
        ("LUM-OA-MIB", "oaIfLaserForcedOn"),
        ("LUM-OA-MIB", "oaIfActualLaserTemp"),
        ("LUM-OA-MIB", "oaIfAutomaticPowerShutdown"))
)
if mibBuilder.loadTexts:
    oaIfGroupV5.setStatus("current")

oaIfGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 8)
)
oaIfGroupV6.setObjects(
      *(("LUM-OA-MIB", "oaIfIndex"),
        ("LUM-OA-MIB", "oaIfName"),
        ("LUM-OA-MIB", "oaIfDescr"),
        ("LUM-OA-MIB", "oaIfSubrack"),
        ("LUM-OA-MIB", "oaIfSlot"),
        ("LUM-OA-MIB", "oaIfTxPort"),
        ("LUM-OA-MIB", "oaIfRxPort"),
        ("LUM-OA-MIB", "oaIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaIfAdminStatus"),
        ("LUM-OA-MIB", "oaIfOperStatus"),
        ("LUM-OA-MIB", "oaIfLaserStatus"),
        ("LUM-OA-MIB", "oaIfAmplifierType"),
        ("LUM-OA-MIB", "oaIfWantedAbsolutePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedRelativePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedGain"),
        ("LUM-OA-MIB", "oaIfFrequencyMin"),
        ("LUM-OA-MIB", "oaIfFrequencyMax"),
        ("LUM-OA-MIB", "oaIfNominalTxPower"),
        ("LUM-OA-MIB", "oaIfTxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserBias"),
        ("LUM-OA-MIB", "oaIfNominalLaserTemp"),
        ("LUM-OA-MIB", "oaIfRelativeLaserTemp"),
        ("LUM-OA-MIB", "oaIfLossOfSignalThreshold"),
        ("LUM-OA-MIB", "oaIfLossOfSignal"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemRxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerLow"),
        ("LUM-OA-MIB", "oaIfReceivedPowerLow"),
        ("LUM-OA-MIB", "oaIfLaserBiasHigh"),
        ("LUM-OA-MIB", "oaIfLaserTempControlFault"),
        ("LUM-OA-MIB", "oaIfConfigurationCommand"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempLow"),
        ("LUM-OA-MIB", "oaIfLaserTempLowRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfLaserTempHighRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfAmpTypeNotSupportedByHw"),
        ("LUM-OA-MIB", "oaIfWantedSignalPowerLevel"),
        ("LUM-OA-MIB", "oaIfObjectProperty"),
        ("LUM-OA-MIB", "oaIfLaserForcedOn"),
        ("LUM-OA-MIB", "oaIfActualLaserTemp"),
        ("LUM-OA-MIB", "oaIfAutomaticPowerShutdown"),
        ("LUM-OA-MIB", "oaIfDisabled"))
)
if mibBuilder.loadTexts:
    oaIfGroupV6.setStatus("deprecated")

oaVoaIfGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 9)
)
oaVoaIfGroupV1.setObjects(
      *(("LUM-OA-MIB", "oaVoaIfIndex"),
        ("LUM-OA-MIB", "oaVoaIfName"),
        ("LUM-OA-MIB", "oaVoaIfDescr"),
        ("LUM-OA-MIB", "oaVoaIfSubrack"),
        ("LUM-OA-MIB", "oaVoaIfSlot"),
        ("LUM-OA-MIB", "oaVoaIfTxPort"),
        ("LUM-OA-MIB", "oaVoaIfRxPort"),
        ("LUM-OA-MIB", "oaVoaIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaVoaIfAdminStatus"),
        ("LUM-OA-MIB", "oaVoaIfOperStatus"),
        ("LUM-OA-MIB", "oaVoaIfObjectProperty"),
        ("LUM-OA-MIB", "oaVoaIfControlMode"),
        ("LUM-OA-MIB", "oaVoaIfWantedOutputPower"),
        ("LUM-OA-MIB", "oaVoaIfCurrentOutputPower"),
        ("LUM-OA-MIB", "oaVoaIfRegulationRange"),
        ("LUM-OA-MIB", "oaVoaIfWantedAttenuation"),
        ("LUM-OA-MIB", "oaVoaIfCurrentAttenuation"),
        ("LUM-OA-MIB", "oaVoaIfSamplePeriod"),
        ("LUM-OA-MIB", "oaVoaIfOuputPowerControlFailure"),
        ("LUM-OA-MIB", "oaVoaIfCurrentPowerOutOfRange"),
        ("LUM-OA-MIB", "oaVoaIfConfigurationCommand"),
        ("LUM-OA-MIB", "oaVoaIfInInstallationMode"))
)
if mibBuilder.loadTexts:
    oaVoaIfGroupV1.setStatus("current")

oaIfGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 10)
)
oaIfGroupV7.setObjects(
      *(("LUM-OA-MIB", "oaIfIndex"),
        ("LUM-OA-MIB", "oaIfName"),
        ("LUM-OA-MIB", "oaIfDescr"),
        ("LUM-OA-MIB", "oaIfSubrack"),
        ("LUM-OA-MIB", "oaIfSlot"),
        ("LUM-OA-MIB", "oaIfTxPort"),
        ("LUM-OA-MIB", "oaIfRxPort"),
        ("LUM-OA-MIB", "oaIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaIfAdminStatus"),
        ("LUM-OA-MIB", "oaIfOperStatus"),
        ("LUM-OA-MIB", "oaIfLaserStatus"),
        ("LUM-OA-MIB", "oaIfAmplifierType"),
        ("LUM-OA-MIB", "oaIfWantedAbsolutePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedRelativePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedGain"),
        ("LUM-OA-MIB", "oaIfFrequencyMin"),
        ("LUM-OA-MIB", "oaIfFrequencyMax"),
        ("LUM-OA-MIB", "oaIfNominalTxPower"),
        ("LUM-OA-MIB", "oaIfTxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserBias"),
        ("LUM-OA-MIB", "oaIfNominalLaserTemp"),
        ("LUM-OA-MIB", "oaIfRelativeLaserTemp"),
        ("LUM-OA-MIB", "oaIfLossOfSignalThreshold"),
        ("LUM-OA-MIB", "oaIfLossOfSignal"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemRxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerLow"),
        ("LUM-OA-MIB", "oaIfReceivedPowerLow"),
        ("LUM-OA-MIB", "oaIfLaserBiasHigh"),
        ("LUM-OA-MIB", "oaIfLaserTempControlFault"),
        ("LUM-OA-MIB", "oaIfConfigurationCommand"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempLow"),
        ("LUM-OA-MIB", "oaIfLaserTempLowRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfLaserTempHighRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfAmpTypeNotSupportedByHw"),
        ("LUM-OA-MIB", "oaIfWantedSignalPowerLevel"),
        ("LUM-OA-MIB", "oaIfObjectProperty"),
        ("LUM-OA-MIB", "oaIfLaserForcedOn"),
        ("LUM-OA-MIB", "oaIfActualLaserTemp"),
        ("LUM-OA-MIB", "oaIfAutomaticPowerShutdown"),
        ("LUM-OA-MIB", "oaIfDisabled"),
        ("LUM-OA-MIB", "oaIfWantedPowerLimit"))
)
if mibBuilder.loadTexts:
    oaIfGroupV7.setStatus("deprecated")

oaIfGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 11)
)
oaIfGroupV8.setObjects(
      *(("LUM-OA-MIB", "oaIfIndex"),
        ("LUM-OA-MIB", "oaIfName"),
        ("LUM-OA-MIB", "oaIfDescr"),
        ("LUM-OA-MIB", "oaIfSubrack"),
        ("LUM-OA-MIB", "oaIfSlot"),
        ("LUM-OA-MIB", "oaIfTxPort"),
        ("LUM-OA-MIB", "oaIfRxPort"),
        ("LUM-OA-MIB", "oaIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaIfAdminStatus"),
        ("LUM-OA-MIB", "oaIfOperStatus"),
        ("LUM-OA-MIB", "oaIfLaserStatus"),
        ("LUM-OA-MIB", "oaIfAmplifierType"),
        ("LUM-OA-MIB", "oaIfWantedAbsolutePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedRelativePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedGain"),
        ("LUM-OA-MIB", "oaIfFrequencyMin"),
        ("LUM-OA-MIB", "oaIfFrequencyMax"),
        ("LUM-OA-MIB", "oaIfNominalTxPower"),
        ("LUM-OA-MIB", "oaIfTxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserBias"),
        ("LUM-OA-MIB", "oaIfNominalLaserTemp"),
        ("LUM-OA-MIB", "oaIfRelativeLaserTemp"),
        ("LUM-OA-MIB", "oaIfLossOfSignalThreshold"),
        ("LUM-OA-MIB", "oaIfLossOfSignal"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemRxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerLow"),
        ("LUM-OA-MIB", "oaIfReceivedPowerLow"),
        ("LUM-OA-MIB", "oaIfLaserBiasHigh"),
        ("LUM-OA-MIB", "oaIfLaserTempControlFault"),
        ("LUM-OA-MIB", "oaIfConfigurationCommand"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempLow"),
        ("LUM-OA-MIB", "oaIfLaserTempLowRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfLaserTempHighRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfAmpTypeNotSupportedByHw"),
        ("LUM-OA-MIB", "oaIfWantedSignalPowerLevel"),
        ("LUM-OA-MIB", "oaIfObjectProperty"),
        ("LUM-OA-MIB", "oaIfLaserForcedOn"),
        ("LUM-OA-MIB", "oaIfActualLaserTemp"),
        ("LUM-OA-MIB", "oaIfAutomaticPowerShutdown"),
        ("LUM-OA-MIB", "oaIfDisabled"),
        ("LUM-OA-MIB", "oaIfWantedPowerLimit"),
        ("LUM-OA-MIB", "oaIfModuleInfo"))
)
if mibBuilder.loadTexts:
    oaIfGroupV8.setStatus("deprecated")

oaVoaClientIfGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 12)
)
oaVoaClientIfGroupV1.setObjects(
      *(("LUM-OA-MIB", "oaVoaClientIfIndex"),
        ("LUM-OA-MIB", "oaVoaClientIfName"),
        ("LUM-OA-MIB", "oaVoaClientIfDescr"),
        ("LUM-OA-MIB", "oaVoaClientIfSubrack"),
        ("LUM-OA-MIB", "oaVoaClientIfSlot"),
        ("LUM-OA-MIB", "oaVoaClientIfTxPort"),
        ("LUM-OA-MIB", "oaVoaClientIfRxPort"),
        ("LUM-OA-MIB", "oaVoaClientIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaVoaClientIfAdminStatus"),
        ("LUM-OA-MIB", "oaVoaClientIfOperStatus"),
        ("LUM-OA-MIB", "oaVoaClientIfObjectProperty"),
        ("LUM-OA-MIB", "oaVoaClientIfControlMode"),
        ("LUM-OA-MIB", "oaVoaClientIfWantedAttenuation"),
        ("LUM-OA-MIB", "oaVoaClientIfCurrentAttenuation"),
        ("LUM-OA-MIB", "oaVoaClientIfLambda"))
)
if mibBuilder.loadTexts:
    oaVoaClientIfGroupV1.setStatus("deprecated")

oaVoaLineIfGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 13)
)
oaVoaLineIfGroupV1.setObjects(
      *(("LUM-OA-MIB", "oaVoaLineIfIndex"),
        ("LUM-OA-MIB", "oaVoaLineIfName"),
        ("LUM-OA-MIB", "oaVoaLineIfDescr"),
        ("LUM-OA-MIB", "oaVoaLineIfSubrack"),
        ("LUM-OA-MIB", "oaVoaLineIfSlot"),
        ("LUM-OA-MIB", "oaVoaLineIfTxPort"),
        ("LUM-OA-MIB", "oaVoaLineIfRxPort"),
        ("LUM-OA-MIB", "oaVoaLineIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaVoaLineIfAdminStatus"),
        ("LUM-OA-MIB", "oaVoaLineIfOperStatus"),
        ("LUM-OA-MIB", "oaVoaLineIfModuleFailure"),
        ("LUM-OA-MIB", "oaVoaLineIfObjectProperty"))
)
if mibBuilder.loadTexts:
    oaVoaLineIfGroupV1.setStatus("current")

oaGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 14)
)
oaGeneralGroupV3.setObjects(
      *(("LUM-OA-MIB", "oaGeneralLastChangeTime"),
        ("LUM-OA-MIB", "oaGeneralStateLastChangeTime"),
        ("LUM-OA-MIB", "oaGeneralOaIfTableSize"),
        ("LUM-OA-MIB", "oaGeneralVoaIfTableSize"),
        ("LUM-OA-MIB", "oaGeneralVoaClientIfTableSize"),
        ("LUM-OA-MIB", "oaGeneralVoaLineIfTableSize"))
)
if mibBuilder.loadTexts:
    oaGeneralGroupV3.setStatus("deprecated")

oaVoaClientIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 15)
)
oaVoaClientIfGroupV2.setObjects(
      *(("LUM-OA-MIB", "oaVoaClientIfIndex"),
        ("LUM-OA-MIB", "oaVoaClientIfName"),
        ("LUM-OA-MIB", "oaVoaClientIfDescr"),
        ("LUM-OA-MIB", "oaVoaClientIfSubrack"),
        ("LUM-OA-MIB", "oaVoaClientIfSlot"),
        ("LUM-OA-MIB", "oaVoaClientIfTxPort"),
        ("LUM-OA-MIB", "oaVoaClientIfRxPort"),
        ("LUM-OA-MIB", "oaVoaClientIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaVoaClientIfAdminStatus"),
        ("LUM-OA-MIB", "oaVoaClientIfOperStatus"),
        ("LUM-OA-MIB", "oaVoaClientIfObjectProperty"),
        ("LUM-OA-MIB", "oaVoaClientIfControlMode"),
        ("LUM-OA-MIB", "oaVoaClientIfWantedAttenuation"),
        ("LUM-OA-MIB", "oaVoaClientIfCurrentAttenuation"),
        ("LUM-OA-MIB", "oaVoaClientIfLambda"),
        ("LUM-OA-MIB", "oaVoaClientIfAbsoluteAttenuation"),
        ("LUM-OA-MIB", "oaVoaClientIfVoa2CurrentAttenuation"),
        ("LUM-OA-MIB", "oaVoaClientIfDecreaseAttenuation"),
        ("LUM-OA-MIB", "oaVoaClientIfIncreaseAttenuation"),
        ("LUM-OA-MIB", "oaVoaClientIfInsertionLoss"),
        ("LUM-OA-MIB", "oaVoaClientIfExpectedFrequency"))
)
if mibBuilder.loadTexts:
    oaVoaClientIfGroupV2.setStatus("deprecated")

oaModuleGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 16)
)
oaModuleGroupV1.setObjects(
      *(("LUM-OA-MIB", "oaModuleIndex"),
        ("LUM-OA-MIB", "oaModuleName"),
        ("LUM-OA-MIB", "oaModuleDescr"),
        ("LUM-OA-MIB", "oaModuleSubrack"),
        ("LUM-OA-MIB", "oaModuleSlot"),
        ("LUM-OA-MIB", "oaModuleNumber"),
        ("LUM-OA-MIB", "oaModuleInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaModuleAdminStatus"),
        ("LUM-OA-MIB", "oaModuleOperStatus"),
        ("LUM-OA-MIB", "oaModuleObjectProperty"),
        ("LUM-OA-MIB", "oaModuleNominalTemp"),
        ("LUM-OA-MIB", "oaModuleRelativeTemp"),
        ("LUM-OA-MIB", "oaModuleTempFailure"))
)
if mibBuilder.loadTexts:
    oaModuleGroupV1.setStatus("deprecated")

oaGeneralGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 17)
)
oaGeneralGroupV4.setObjects(
      *(("LUM-OA-MIB", "oaGeneralLastChangeTime"),
        ("LUM-OA-MIB", "oaGeneralStateLastChangeTime"),
        ("LUM-OA-MIB", "oaGeneralOaIfTableSize"),
        ("LUM-OA-MIB", "oaGeneralVoaIfTableSize"),
        ("LUM-OA-MIB", "oaGeneralVoaClientIfTableSize"),
        ("LUM-OA-MIB", "oaGeneralVoaLineIfTableSize"),
        ("LUM-OA-MIB", "oaGeneralOaModuleTableSize"))
)
if mibBuilder.loadTexts:
    oaGeneralGroupV4.setStatus("current")

oaIfGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 18)
)
oaIfGroupV9.setObjects(
      *(("LUM-OA-MIB", "oaIfIndex"),
        ("LUM-OA-MIB", "oaIfName"),
        ("LUM-OA-MIB", "oaIfDescr"),
        ("LUM-OA-MIB", "oaIfSubrack"),
        ("LUM-OA-MIB", "oaIfSlot"),
        ("LUM-OA-MIB", "oaIfTxPort"),
        ("LUM-OA-MIB", "oaIfRxPort"),
        ("LUM-OA-MIB", "oaIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaIfAdminStatus"),
        ("LUM-OA-MIB", "oaIfOperStatus"),
        ("LUM-OA-MIB", "oaIfLaserStatus"),
        ("LUM-OA-MIB", "oaIfAmplifierType"),
        ("LUM-OA-MIB", "oaIfWantedAbsolutePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedRelativePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedGain"),
        ("LUM-OA-MIB", "oaIfFrequencyMin"),
        ("LUM-OA-MIB", "oaIfFrequencyMax"),
        ("LUM-OA-MIB", "oaIfNominalTxPower"),
        ("LUM-OA-MIB", "oaIfTxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserBias"),
        ("LUM-OA-MIB", "oaIfNominalLaserTemp"),
        ("LUM-OA-MIB", "oaIfRelativeLaserTemp"),
        ("LUM-OA-MIB", "oaIfLossOfSignalThreshold"),
        ("LUM-OA-MIB", "oaIfLossOfSignal"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemRxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerLow"),
        ("LUM-OA-MIB", "oaIfReceivedPowerLow"),
        ("LUM-OA-MIB", "oaIfLaserBiasHigh"),
        ("LUM-OA-MIB", "oaIfLaserTempControlFault"),
        ("LUM-OA-MIB", "oaIfConfigurationCommand"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempLow"),
        ("LUM-OA-MIB", "oaIfLaserTempLowRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfLaserTempHighRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfAmpTypeNotSupportedByHw"),
        ("LUM-OA-MIB", "oaIfWantedSignalPowerLevel"),
        ("LUM-OA-MIB", "oaIfObjectProperty"),
        ("LUM-OA-MIB", "oaIfLaserForcedOn"),
        ("LUM-OA-MIB", "oaIfActualLaserTemp"),
        ("LUM-OA-MIB", "oaIfAutomaticPowerShutdown"),
        ("LUM-OA-MIB", "oaIfDisabled"),
        ("LUM-OA-MIB", "oaIfWantedPowerLimit"),
        ("LUM-OA-MIB", "oaIfModuleInfo"),
        ("LUM-OA-MIB", "oaIfMonitorInsertionLoss"),
        ("LUM-OA-MIB", "oaIfNumMonitorInsertionLoss"),
        ("LUM-OA-MIB", "oaIfFunctionalType"))
)
if mibBuilder.loadTexts:
    oaIfGroupV9.setStatus("deprecated")

oaModuleGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 19)
)
oaModuleGroupV2.setObjects(
      *(("LUM-OA-MIB", "oaModuleIndex"),
        ("LUM-OA-MIB", "oaModuleName"),
        ("LUM-OA-MIB", "oaModuleDescr"),
        ("LUM-OA-MIB", "oaModuleSubrack"),
        ("LUM-OA-MIB", "oaModuleSlot"),
        ("LUM-OA-MIB", "oaModuleNumber"),
        ("LUM-OA-MIB", "oaModuleInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaModuleAdminStatus"),
        ("LUM-OA-MIB", "oaModuleOperStatus"),
        ("LUM-OA-MIB", "oaModuleObjectProperty"),
        ("LUM-OA-MIB", "oaModuleNominalTemp"),
        ("LUM-OA-MIB", "oaModuleRelativeTemp"),
        ("LUM-OA-MIB", "oaModuleTempFailure"),
        ("LUM-OA-MIB", "oaModuleTemperature"),
        ("LUM-OA-MIB", "oaModuleCommunicationFailure"),
        ("LUM-OA-MIB", "oaModuleModuleInfo"))
)
if mibBuilder.loadTexts:
    oaModuleGroupV2.setStatus("deprecated")

oaIfGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 20)
)
oaIfGroupV10.setObjects(
      *(("LUM-OA-MIB", "oaIfIndex"),
        ("LUM-OA-MIB", "oaIfName"),
        ("LUM-OA-MIB", "oaIfDescr"),
        ("LUM-OA-MIB", "oaIfSubrack"),
        ("LUM-OA-MIB", "oaIfSlot"),
        ("LUM-OA-MIB", "oaIfTxPort"),
        ("LUM-OA-MIB", "oaIfRxPort"),
        ("LUM-OA-MIB", "oaIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaIfAdminStatus"),
        ("LUM-OA-MIB", "oaIfOperStatus"),
        ("LUM-OA-MIB", "oaIfLaserStatus"),
        ("LUM-OA-MIB", "oaIfAmplifierType"),
        ("LUM-OA-MIB", "oaIfWantedAbsolutePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedRelativePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedGain"),
        ("LUM-OA-MIB", "oaIfFrequencyMin"),
        ("LUM-OA-MIB", "oaIfFrequencyMax"),
        ("LUM-OA-MIB", "oaIfNominalTxPower"),
        ("LUM-OA-MIB", "oaIfTxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserBias"),
        ("LUM-OA-MIB", "oaIfNominalLaserTemp"),
        ("LUM-OA-MIB", "oaIfRelativeLaserTemp"),
        ("LUM-OA-MIB", "oaIfLossOfSignalThreshold"),
        ("LUM-OA-MIB", "oaIfLossOfSignal"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemRxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerLow"),
        ("LUM-OA-MIB", "oaIfReceivedPowerLow"),
        ("LUM-OA-MIB", "oaIfLaserBiasHigh"),
        ("LUM-OA-MIB", "oaIfLaserTempControlFault"),
        ("LUM-OA-MIB", "oaIfConfigurationCommand"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempLow"),
        ("LUM-OA-MIB", "oaIfLaserTempLowRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfLaserTempHighRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfAmpTypeNotSupportedByHw"),
        ("LUM-OA-MIB", "oaIfWantedSignalPowerLevel"),
        ("LUM-OA-MIB", "oaIfObjectProperty"),
        ("LUM-OA-MIB", "oaIfLaserForcedOn"),
        ("LUM-OA-MIB", "oaIfActualLaserTemp"),
        ("LUM-OA-MIB", "oaIfAutomaticPowerShutdown"),
        ("LUM-OA-MIB", "oaIfDisabled"),
        ("LUM-OA-MIB", "oaIfWantedPowerLimit"),
        ("LUM-OA-MIB", "oaIfModuleInfo"),
        ("LUM-OA-MIB", "oaIfMonitorInsertionLoss"),
        ("LUM-OA-MIB", "oaIfNumMonitorInsertionLoss"),
        ("LUM-OA-MIB", "oaIfFunctionalType"),
        ("LUM-OA-MIB", "oaIfActualGain"),
        ("LUM-OA-MIB", "oaIfSaturationFault"))
)
if mibBuilder.loadTexts:
    oaIfGroupV10.setStatus("deprecated")

oaIfGroupV11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 21)
)
oaIfGroupV11.setObjects(
      *(("LUM-OA-MIB", "oaIfIndex"),
        ("LUM-OA-MIB", "oaIfName"),
        ("LUM-OA-MIB", "oaIfDescr"),
        ("LUM-OA-MIB", "oaIfSubrack"),
        ("LUM-OA-MIB", "oaIfSlot"),
        ("LUM-OA-MIB", "oaIfTxPort"),
        ("LUM-OA-MIB", "oaIfRxPort"),
        ("LUM-OA-MIB", "oaIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaIfAdminStatus"),
        ("LUM-OA-MIB", "oaIfOperStatus"),
        ("LUM-OA-MIB", "oaIfLaserStatus"),
        ("LUM-OA-MIB", "oaIfAmplifierType"),
        ("LUM-OA-MIB", "oaIfWantedAbsolutePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedRelativePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedGain"),
        ("LUM-OA-MIB", "oaIfFrequencyMin"),
        ("LUM-OA-MIB", "oaIfFrequencyMax"),
        ("LUM-OA-MIB", "oaIfNominalTxPower"),
        ("LUM-OA-MIB", "oaIfTxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserBias"),
        ("LUM-OA-MIB", "oaIfNominalLaserTemp"),
        ("LUM-OA-MIB", "oaIfRelativeLaserTemp"),
        ("LUM-OA-MIB", "oaIfLossOfSignalThreshold"),
        ("LUM-OA-MIB", "oaIfLossOfSignal"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemRxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerLow"),
        ("LUM-OA-MIB", "oaIfReceivedPowerLow"),
        ("LUM-OA-MIB", "oaIfLaserBiasHigh"),
        ("LUM-OA-MIB", "oaIfLaserTempControlFault"),
        ("LUM-OA-MIB", "oaIfConfigurationCommand"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempLow"),
        ("LUM-OA-MIB", "oaIfLaserTempLowRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfLaserTempHighRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfAmpTypeNotSupportedByHw"),
        ("LUM-OA-MIB", "oaIfWantedSignalPowerLevel"),
        ("LUM-OA-MIB", "oaIfObjectProperty"),
        ("LUM-OA-MIB", "oaIfLaserForcedOn"),
        ("LUM-OA-MIB", "oaIfActualLaserTemp"),
        ("LUM-OA-MIB", "oaIfAutomaticPowerShutdown"),
        ("LUM-OA-MIB", "oaIfDisabled"),
        ("LUM-OA-MIB", "oaIfWantedPowerLimit"),
        ("LUM-OA-MIB", "oaIfModuleInfo"),
        ("LUM-OA-MIB", "oaIfMonitorInsertionLoss"),
        ("LUM-OA-MIB", "oaIfNumMonitorInsertionLoss"),
        ("LUM-OA-MIB", "oaIfFunctionalType"),
        ("LUM-OA-MIB", "oaIfActualGain"),
        ("LUM-OA-MIB", "oaIfSaturationFault"),
        ("LUM-OA-MIB", "oaIfWantedGainTilt"))
)
if mibBuilder.loadTexts:
    oaIfGroupV11.setStatus("deprecated")

oaVoaClientIfGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 22)
)
oaVoaClientIfGroupV3.setObjects(
      *(("LUM-OA-MIB", "oaVoaClientIfIndex"),
        ("LUM-OA-MIB", "oaVoaClientIfName"),
        ("LUM-OA-MIB", "oaVoaClientIfDescr"),
        ("LUM-OA-MIB", "oaVoaClientIfSubrack"),
        ("LUM-OA-MIB", "oaVoaClientIfSlot"),
        ("LUM-OA-MIB", "oaVoaClientIfTxPort"),
        ("LUM-OA-MIB", "oaVoaClientIfRxPort"),
        ("LUM-OA-MIB", "oaVoaClientIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaVoaClientIfAdminStatus"),
        ("LUM-OA-MIB", "oaVoaClientIfOperStatus"),
        ("LUM-OA-MIB", "oaVoaClientIfObjectProperty"),
        ("LUM-OA-MIB", "oaVoaClientIfControlMode"),
        ("LUM-OA-MIB", "oaVoaClientIfWantedAttenuation"),
        ("LUM-OA-MIB", "oaVoaClientIfCurrentAttenuation"),
        ("LUM-OA-MIB", "oaVoaClientIfLambda"),
        ("LUM-OA-MIB", "oaVoaClientIfAbsoluteAttenuation"),
        ("LUM-OA-MIB", "oaVoaClientIfVoa2CurrentAttenuation"),
        ("LUM-OA-MIB", "oaVoaClientIfDecreaseAttenuation"),
        ("LUM-OA-MIB", "oaVoaClientIfIncreaseAttenuation"),
        ("LUM-OA-MIB", "oaVoaClientIfInsertionLoss"),
        ("LUM-OA-MIB", "oaVoaClientIfExpectedFrequency"),
        ("LUM-OA-MIB", "oaVoaClientIfSfpMissing"),
        ("LUM-OA-MIB", "oaVoaClientIfSfpClass"),
        ("LUM-OA-MIB", "oaVoaClientIfSfpTransmitterFailed"),
        ("LUM-OA-MIB", "oaVoaClientIfSfpMediaMismatch"),
        ("LUM-OA-MIB", "oaVoaClientIfLossOfSignal"),
        ("LUM-OA-MIB", "oaVoaClientIfSfpCodeMismatch"),
        ("LUM-OA-MIB", "oaVoaClientIfAttenuationConfigMismatch"))
)
if mibBuilder.loadTexts:
    oaVoaClientIfGroupV3.setStatus("current")

oaIfGroupV12 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 23)
)
oaIfGroupV12.setObjects(
      *(("LUM-OA-MIB", "oaIfIndex"),
        ("LUM-OA-MIB", "oaIfName"),
        ("LUM-OA-MIB", "oaIfDescr"),
        ("LUM-OA-MIB", "oaIfSubrack"),
        ("LUM-OA-MIB", "oaIfSlot"),
        ("LUM-OA-MIB", "oaIfTxPort"),
        ("LUM-OA-MIB", "oaIfRxPort"),
        ("LUM-OA-MIB", "oaIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaIfAdminStatus"),
        ("LUM-OA-MIB", "oaIfOperStatus"),
        ("LUM-OA-MIB", "oaIfLaserStatus"),
        ("LUM-OA-MIB", "oaIfAmplifierType"),
        ("LUM-OA-MIB", "oaIfWantedAbsolutePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedRelativePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedGain"),
        ("LUM-OA-MIB", "oaIfFrequencyMin"),
        ("LUM-OA-MIB", "oaIfFrequencyMax"),
        ("LUM-OA-MIB", "oaIfNominalTxPower"),
        ("LUM-OA-MIB", "oaIfTxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserBias"),
        ("LUM-OA-MIB", "oaIfNominalLaserTemp"),
        ("LUM-OA-MIB", "oaIfRelativeLaserTemp"),
        ("LUM-OA-MIB", "oaIfLossOfSignalThreshold"),
        ("LUM-OA-MIB", "oaIfLossOfSignal"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemRxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerLow"),
        ("LUM-OA-MIB", "oaIfReceivedPowerLow"),
        ("LUM-OA-MIB", "oaIfLaserBiasHigh"),
        ("LUM-OA-MIB", "oaIfLaserTempControlFault"),
        ("LUM-OA-MIB", "oaIfConfigurationCommand"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempLow"),
        ("LUM-OA-MIB", "oaIfLaserTempLowRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfLaserTempHighRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfAmpTypeNotSupportedByHw"),
        ("LUM-OA-MIB", "oaIfWantedSignalPowerLevel"),
        ("LUM-OA-MIB", "oaIfObjectProperty"),
        ("LUM-OA-MIB", "oaIfLaserForcedOn"),
        ("LUM-OA-MIB", "oaIfActualLaserTemp"),
        ("LUM-OA-MIB", "oaIfAutomaticPowerShutdown"),
        ("LUM-OA-MIB", "oaIfDisabled"),
        ("LUM-OA-MIB", "oaIfWantedPowerLimit"),
        ("LUM-OA-MIB", "oaIfModuleInfo"),
        ("LUM-OA-MIB", "oaIfMonitorInsertionLoss"),
        ("LUM-OA-MIB", "oaIfNumMonitorInsertionLoss"),
        ("LUM-OA-MIB", "oaIfFunctionalType"),
        ("LUM-OA-MIB", "oaIfActualGain"),
        ("LUM-OA-MIB", "oaIfSaturationFault"),
        ("LUM-OA-MIB", "oaIfWantedGainTilt"),
        ("LUM-OA-MIB", "oaIfTxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserPumpBias"),
        ("LUM-OA-MIB", "oaIfCaseTempOutOfrange"),
        ("LUM-OA-MIB", "oaIfLaserTempOutOfRange"))
)
if mibBuilder.loadTexts:
    oaIfGroupV12.setStatus("deprecated")

oaModuleGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 24)
)
oaModuleGroupV3.setObjects(
      *(("LUM-OA-MIB", "oaModuleIndex"),
        ("LUM-OA-MIB", "oaModuleName"),
        ("LUM-OA-MIB", "oaModuleDescr"),
        ("LUM-OA-MIB", "oaModuleSubrack"),
        ("LUM-OA-MIB", "oaModuleSlot"),
        ("LUM-OA-MIB", "oaModuleNumber"),
        ("LUM-OA-MIB", "oaModuleInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaModuleAdminStatus"),
        ("LUM-OA-MIB", "oaModuleOperStatus"),
        ("LUM-OA-MIB", "oaModuleObjectProperty"),
        ("LUM-OA-MIB", "oaModuleNominalTemp"),
        ("LUM-OA-MIB", "oaModuleRelativeTemp"),
        ("LUM-OA-MIB", "oaModuleTempFailure"),
        ("LUM-OA-MIB", "oaModuleTemperature"),
        ("LUM-OA-MIB", "oaModuleCommunicationFailure"),
        ("LUM-OA-MIB", "oaModuleModuleInfo"),
        ("LUM-OA-MIB", "oaModuleVcomThresholdExceeded"),
        ("LUM-OA-MIB", "oaModuleFirmwareUpgradeAvailable"))
)
if mibBuilder.loadTexts:
    oaModuleGroupV3.setStatus("deprecated")

oaIfGroupV13 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 25)
)
oaIfGroupV13.setObjects(
      *(("LUM-OA-MIB", "oaIfIndex"),
        ("LUM-OA-MIB", "oaIfName"),
        ("LUM-OA-MIB", "oaIfDescr"),
        ("LUM-OA-MIB", "oaIfSubrack"),
        ("LUM-OA-MIB", "oaIfSlot"),
        ("LUM-OA-MIB", "oaIfTxPort"),
        ("LUM-OA-MIB", "oaIfRxPort"),
        ("LUM-OA-MIB", "oaIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaIfAdminStatus"),
        ("LUM-OA-MIB", "oaIfOperStatus"),
        ("LUM-OA-MIB", "oaIfLaserStatus"),
        ("LUM-OA-MIB", "oaIfAmplifierType"),
        ("LUM-OA-MIB", "oaIfWantedAbsolutePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedRelativePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedGain"),
        ("LUM-OA-MIB", "oaIfFrequencyMin"),
        ("LUM-OA-MIB", "oaIfFrequencyMax"),
        ("LUM-OA-MIB", "oaIfNominalTxPower"),
        ("LUM-OA-MIB", "oaIfTxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserBias"),
        ("LUM-OA-MIB", "oaIfNominalLaserTemp"),
        ("LUM-OA-MIB", "oaIfRelativeLaserTemp"),
        ("LUM-OA-MIB", "oaIfLossOfSignalThreshold"),
        ("LUM-OA-MIB", "oaIfLossOfSignal"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemRxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerLow"),
        ("LUM-OA-MIB", "oaIfReceivedPowerLow"),
        ("LUM-OA-MIB", "oaIfLaserBiasHigh"),
        ("LUM-OA-MIB", "oaIfLaserTempControlFault"),
        ("LUM-OA-MIB", "oaIfConfigurationCommand"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempLow"),
        ("LUM-OA-MIB", "oaIfLaserTempLowRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfLaserTempHighRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfAmpTypeNotSupportedByHw"),
        ("LUM-OA-MIB", "oaIfWantedSignalPowerLevel"),
        ("LUM-OA-MIB", "oaIfObjectProperty"),
        ("LUM-OA-MIB", "oaIfLaserForcedOn"),
        ("LUM-OA-MIB", "oaIfActualLaserTemp"),
        ("LUM-OA-MIB", "oaIfAutomaticPowerShutdown"),
        ("LUM-OA-MIB", "oaIfDisabled"),
        ("LUM-OA-MIB", "oaIfWantedPowerLimit"),
        ("LUM-OA-MIB", "oaIfModuleInfo"),
        ("LUM-OA-MIB", "oaIfMonitorInsertionLoss"),
        ("LUM-OA-MIB", "oaIfNumMonitorInsertionLoss"),
        ("LUM-OA-MIB", "oaIfFunctionalType"),
        ("LUM-OA-MIB", "oaIfActualGain"),
        ("LUM-OA-MIB", "oaIfSaturationFault"),
        ("LUM-OA-MIB", "oaIfWantedGainTilt"),
        ("LUM-OA-MIB", "oaIfTxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserPumpBias"),
        ("LUM-OA-MIB", "oaIfCaseTempOutOfrange"),
        ("LUM-OA-MIB", "oaIfLaserTempOutOfRange"),
        ("LUM-OA-MIB", "oaIfSupportsReadMonitorInsertionLoss"))
)
if mibBuilder.loadTexts:
    oaIfGroupV13.setStatus("deprecated")

oaIfGroupV14 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 26)
)
oaIfGroupV14.setObjects(
      *(("LUM-OA-MIB", "oaIfIndex"),
        ("LUM-OA-MIB", "oaIfName"),
        ("LUM-OA-MIB", "oaIfDescr"),
        ("LUM-OA-MIB", "oaIfSubrack"),
        ("LUM-OA-MIB", "oaIfSlot"),
        ("LUM-OA-MIB", "oaIfTxPort"),
        ("LUM-OA-MIB", "oaIfRxPort"),
        ("LUM-OA-MIB", "oaIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaIfAdminStatus"),
        ("LUM-OA-MIB", "oaIfOperStatus"),
        ("LUM-OA-MIB", "oaIfLaserStatus"),
        ("LUM-OA-MIB", "oaIfAmplifierType"),
        ("LUM-OA-MIB", "oaIfWantedAbsolutePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedRelativePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedGain"),
        ("LUM-OA-MIB", "oaIfFrequencyMin"),
        ("LUM-OA-MIB", "oaIfFrequencyMax"),
        ("LUM-OA-MIB", "oaIfNominalTxPower"),
        ("LUM-OA-MIB", "oaIfTxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserBias"),
        ("LUM-OA-MIB", "oaIfNominalLaserTemp"),
        ("LUM-OA-MIB", "oaIfRelativeLaserTemp"),
        ("LUM-OA-MIB", "oaIfLossOfSignalThreshold"),
        ("LUM-OA-MIB", "oaIfLossOfSignal"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemRxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerLow"),
        ("LUM-OA-MIB", "oaIfReceivedPowerLow"),
        ("LUM-OA-MIB", "oaIfLaserBiasHigh"),
        ("LUM-OA-MIB", "oaIfLaserTempControlFault"),
        ("LUM-OA-MIB", "oaIfConfigurationCommand"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempLow"),
        ("LUM-OA-MIB", "oaIfLaserTempLowRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfLaserTempHighRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfAmpTypeNotSupportedByHw"),
        ("LUM-OA-MIB", "oaIfWantedSignalPowerLevel"),
        ("LUM-OA-MIB", "oaIfObjectProperty"),
        ("LUM-OA-MIB", "oaIfLaserForcedOn"),
        ("LUM-OA-MIB", "oaIfActualLaserTemp"),
        ("LUM-OA-MIB", "oaIfAutomaticPowerShutdown"),
        ("LUM-OA-MIB", "oaIfDisabled"),
        ("LUM-OA-MIB", "oaIfWantedPowerLimit"),
        ("LUM-OA-MIB", "oaIfModuleInfo"),
        ("LUM-OA-MIB", "oaIfMonitorInsertionLoss"),
        ("LUM-OA-MIB", "oaIfNumMonitorInsertionLoss"),
        ("LUM-OA-MIB", "oaIfFunctionalType"),
        ("LUM-OA-MIB", "oaIfActualGain"),
        ("LUM-OA-MIB", "oaIfSaturationFault"),
        ("LUM-OA-MIB", "oaIfWantedGainTilt"),
        ("LUM-OA-MIB", "oaIfTxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserPumpBias"),
        ("LUM-OA-MIB", "oaIfCaseTempOutOfrange"),
        ("LUM-OA-MIB", "oaIfLaserTempOutOfRange"),
        ("LUM-OA-MIB", "oaIfSupportsReadMonitorInsertionLoss"),
        ("LUM-OA-MIB", "oaIfTxSignalStatus"),
        ("LUM-OA-MIB", "oaIfRxSignalStatus"))
)
if mibBuilder.loadTexts:
    oaIfGroupV14.setStatus("current")

oaIfGroupV15 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 27)
)
oaIfGroupV15.setObjects(
      *(("LUM-OA-MIB", "oaIfIndex"),
        ("LUM-OA-MIB", "oaIfName"),
        ("LUM-OA-MIB", "oaIfDescr"),
        ("LUM-OA-MIB", "oaIfSubrack"),
        ("LUM-OA-MIB", "oaIfSlot"),
        ("LUM-OA-MIB", "oaIfTxPort"),
        ("LUM-OA-MIB", "oaIfRxPort"),
        ("LUM-OA-MIB", "oaIfInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaIfAdminStatus"),
        ("LUM-OA-MIB", "oaIfOperStatus"),
        ("LUM-OA-MIB", "oaIfLaserStatus"),
        ("LUM-OA-MIB", "oaIfAmplifierType"),
        ("LUM-OA-MIB", "oaIfWantedAbsolutePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedRelativePowerLevel"),
        ("LUM-OA-MIB", "oaIfWantedGain"),
        ("LUM-OA-MIB", "oaIfFrequencyMin"),
        ("LUM-OA-MIB", "oaIfFrequencyMax"),
        ("LUM-OA-MIB", "oaIfNominalTxPower"),
        ("LUM-OA-MIB", "oaIfTxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevel"),
        ("LUM-OA-MIB", "oaIfRxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserBias"),
        ("LUM-OA-MIB", "oaIfNominalLaserTemp"),
        ("LUM-OA-MIB", "oaIfRelativeLaserTemp"),
        ("LUM-OA-MIB", "oaIfLossOfSignalThreshold"),
        ("LUM-OA-MIB", "oaIfLossOfSignal"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemRxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerHigh"),
        ("LUM-OA-MIB", "oaIfRegulationProblemTxPowerLow"),
        ("LUM-OA-MIB", "oaIfReceivedPowerLow"),
        ("LUM-OA-MIB", "oaIfLaserBiasHigh"),
        ("LUM-OA-MIB", "oaIfLaserTempControlFault"),
        ("LUM-OA-MIB", "oaIfConfigurationCommand"),
        ("LUM-OA-MIB", "oaIfPumpLaserTempLow"),
        ("LUM-OA-MIB", "oaIfLaserTempLowRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfLaserTempHighRelativeThreshold"),
        ("LUM-OA-MIB", "oaIfAmpTypeNotSupportedByHw"),
        ("LUM-OA-MIB", "oaIfWantedSignalPowerLevel"),
        ("LUM-OA-MIB", "oaIfObjectProperty"),
        ("LUM-OA-MIB", "oaIfLaserForcedOn"),
        ("LUM-OA-MIB", "oaIfActualLaserTemp"),
        ("LUM-OA-MIB", "oaIfAutomaticPowerShutdown"),
        ("LUM-OA-MIB", "oaIfDisabled"),
        ("LUM-OA-MIB", "oaIfWantedPowerLimit"),
        ("LUM-OA-MIB", "oaIfModuleInfo"),
        ("LUM-OA-MIB", "oaIfMonitorInsertionLoss"),
        ("LUM-OA-MIB", "oaIfNumMonitorInsertionLoss"),
        ("LUM-OA-MIB", "oaIfFunctionalType"),
        ("LUM-OA-MIB", "oaIfActualGain"),
        ("LUM-OA-MIB", "oaIfSaturationFault"),
        ("LUM-OA-MIB", "oaIfWantedGainTilt"),
        ("LUM-OA-MIB", "oaIfTxPowerLevelLowThreshold"),
        ("LUM-OA-MIB", "oaIfLaserPumpBias"),
        ("LUM-OA-MIB", "oaIfCaseTempOutOfrange"),
        ("LUM-OA-MIB", "oaIfLaserTempOutOfRange"),
        ("LUM-OA-MIB", "oaIfSupportsReadMonitorInsertionLoss"),
        ("LUM-OA-MIB", "oaIfTxSignalStatus"),
        ("LUM-OA-MIB", "oaIfRxSignalStatus"),
        ("LUM-OA-MIB", "oaIfOutputPowerFail"))
)
if mibBuilder.loadTexts:
    oaIfGroupV15.setStatus("current")

oaModuleGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 1, 28)
)
oaModuleGroupV4.setObjects(
      *(("LUM-OA-MIB", "oaModuleIndex"),
        ("LUM-OA-MIB", "oaModuleName"),
        ("LUM-OA-MIB", "oaModuleDescr"),
        ("LUM-OA-MIB", "oaModuleSubrack"),
        ("LUM-OA-MIB", "oaModuleSlot"),
        ("LUM-OA-MIB", "oaModuleNumber"),
        ("LUM-OA-MIB", "oaModuleInvPhysIndexOrZero"),
        ("LUM-OA-MIB", "oaModuleAdminStatus"),
        ("LUM-OA-MIB", "oaModuleOperStatus"),
        ("LUM-OA-MIB", "oaModuleObjectProperty"),
        ("LUM-OA-MIB", "oaModuleNominalTemp"),
        ("LUM-OA-MIB", "oaModuleRelativeTemp"),
        ("LUM-OA-MIB", "oaModuleTempFailure"),
        ("LUM-OA-MIB", "oaModuleTemperature"),
        ("LUM-OA-MIB", "oaModuleCommunicationFailure"),
        ("LUM-OA-MIB", "oaModuleModuleInfo"),
        ("LUM-OA-MIB", "oaModuleFirmwareUpgradeAvailable"),
        ("LUM-OA-MIB", "oaModuleWarmingUp"),
        ("LUM-OA-MIB", "oaModuleFailure"))
)
if mibBuilder.loadTexts:
    oaModuleGroupV4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumOaBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 1)
)
lumOaBasicComplV1.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroup"),
        ("LUM-OA-MIB", "oaIfGroup"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV1.setStatus(
        "deprecated"
    )

lumOaBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 2)
)
lumOaBasicComplV2.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroup"),
        ("LUM-OA-MIB", "oaIfGroupV2"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV2.setStatus(
        "deprecated"
    )

lumOaBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 3)
)
lumOaBasicComplV3.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroup"),
        ("LUM-OA-MIB", "oaIfGroupV3"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV3.setStatus(
        "deprecated"
    )

lumOaBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 4)
)
lumOaBasicComplV4.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroupV2"),
        ("LUM-OA-MIB", "oaIfGroupV3"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV4.setStatus(
        "deprecated"
    )

lumOaBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 5)
)
lumOaBasicComplV5.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroupV2"),
        ("LUM-OA-MIB", "oaIfGroupV4"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV5.setStatus(
        "deprecated"
    )

lumOaBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 6)
)
lumOaBasicComplV6.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroupV2"),
        ("LUM-OA-MIB", "oaIfGroupV5"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV6.setStatus(
        "deprecated"
    )

lumOaBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 7)
)
lumOaBasicComplV7.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroupV2"),
        ("LUM-OA-MIB", "oaIfGroupV6"),
        ("LUM-OA-MIB", "oaVoaIfGroupV1"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV7.setStatus(
        "deprecated"
    )

lumOaBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 8)
)
lumOaBasicComplV8.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroupV2"),
        ("LUM-OA-MIB", "oaIfGroupV7"),
        ("LUM-OA-MIB", "oaVoaIfGroupV1"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV8.setStatus(
        "deprecated"
    )

lumOaBasicComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 9)
)
lumOaBasicComplV9.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroupV3"),
        ("LUM-OA-MIB", "oaIfGroupV8"),
        ("LUM-OA-MIB", "oaVoaIfGroupV1"),
        ("LUM-OA-MIB", "oaVoaClientIfGroupV1"),
        ("LUM-OA-MIB", "oaVoaLineIfGroupV1"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV9.setStatus(
        "deprecated"
    )

lumOaBasicComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 10)
)
lumOaBasicComplV10.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroupV4"),
        ("LUM-OA-MIB", "oaIfGroupV9"),
        ("LUM-OA-MIB", "oaVoaIfGroupV1"),
        ("LUM-OA-MIB", "oaVoaClientIfGroupV2"),
        ("LUM-OA-MIB", "oaVoaLineIfGroupV1"),
        ("LUM-OA-MIB", "oaModuleGroupV1"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV10.setStatus(
        "deprecated"
    )

lumOaBasicComplV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 11)
)
lumOaBasicComplV11.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroupV4"),
        ("LUM-OA-MIB", "oaIfGroupV9"),
        ("LUM-OA-MIB", "oaVoaIfGroupV1"),
        ("LUM-OA-MIB", "oaVoaClientIfGroupV2"),
        ("LUM-OA-MIB", "oaVoaLineIfGroupV1"),
        ("LUM-OA-MIB", "oaModuleGroupV2"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV11.setStatus(
        "deprecated"
    )

lumOaBasicComplV12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 12)
)
lumOaBasicComplV12.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroupV4"),
        ("LUM-OA-MIB", "oaIfGroupV10"),
        ("LUM-OA-MIB", "oaVoaIfGroupV1"),
        ("LUM-OA-MIB", "oaVoaClientIfGroupV2"),
        ("LUM-OA-MIB", "oaVoaLineIfGroupV1"),
        ("LUM-OA-MIB", "oaModuleGroupV2"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV12.setStatus(
        "deprecated"
    )

lumOaBasicComplV13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 13)
)
lumOaBasicComplV13.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroupV4"),
        ("LUM-OA-MIB", "oaIfGroupV11"),
        ("LUM-OA-MIB", "oaVoaIfGroupV1"),
        ("LUM-OA-MIB", "oaVoaClientIfGroupV2"),
        ("LUM-OA-MIB", "oaVoaLineIfGroupV1"),
        ("LUM-OA-MIB", "oaModuleGroupV2"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV13.setStatus(
        "deprecated"
    )

lumOaBasicComplV14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 14)
)
lumOaBasicComplV14.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroupV4"),
        ("LUM-OA-MIB", "oaIfGroupV11"),
        ("LUM-OA-MIB", "oaVoaIfGroupV1"),
        ("LUM-OA-MIB", "oaVoaClientIfGroupV3"),
        ("LUM-OA-MIB", "oaVoaLineIfGroupV1"),
        ("LUM-OA-MIB", "oaModuleGroupV2"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV14.setStatus(
        "deprecated"
    )

lumOaBasicComplV15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 15)
)
lumOaBasicComplV15.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroupV4"),
        ("LUM-OA-MIB", "oaIfGroupV12"),
        ("LUM-OA-MIB", "oaVoaIfGroupV1"),
        ("LUM-OA-MIB", "oaVoaClientIfGroupV3"),
        ("LUM-OA-MIB", "oaVoaLineIfGroupV1"),
        ("LUM-OA-MIB", "oaModuleGroupV2"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV15.setStatus(
        "deprecated"
    )

lumOaBasicComplV16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 16)
)
lumOaBasicComplV16.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroupV4"),
        ("LUM-OA-MIB", "oaIfGroupV13"),
        ("LUM-OA-MIB", "oaVoaIfGroupV1"),
        ("LUM-OA-MIB", "oaVoaClientIfGroupV3"),
        ("LUM-OA-MIB", "oaVoaLineIfGroupV1"),
        ("LUM-OA-MIB", "oaModuleGroupV3"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV16.setStatus(
        "deprecated"
    )

lumOaBasicComplV17 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 17)
)
lumOaBasicComplV17.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroupV4"),
        ("LUM-OA-MIB", "oaIfGroupV14"),
        ("LUM-OA-MIB", "oaVoaIfGroupV1"),
        ("LUM-OA-MIB", "oaVoaClientIfGroupV3"),
        ("LUM-OA-MIB", "oaVoaLineIfGroupV1"),
        ("LUM-OA-MIB", "oaModuleGroupV3"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV17.setStatus(
        "deprecated"
    )

lumOaBasicComplV18 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 18)
)
lumOaBasicComplV18.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroupV4"),
        ("LUM-OA-MIB", "oaIfGroupV15"),
        ("LUM-OA-MIB", "oaVoaIfGroupV1"),
        ("LUM-OA-MIB", "oaVoaClientIfGroupV3"),
        ("LUM-OA-MIB", "oaVoaLineIfGroupV1"),
        ("LUM-OA-MIB", "oaModuleGroupV3"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV18.setStatus(
        "deprecated"
    )

lumOaBasicComplV19 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 2, 19)
)
lumOaBasicComplV19.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroupV4"),
        ("LUM-OA-MIB", "oaIfGroupV15"),
        ("LUM-OA-MIB", "oaVoaIfGroupV1"),
        ("LUM-OA-MIB", "oaVoaClientIfGroupV3"),
        ("LUM-OA-MIB", "oaVoaLineIfGroupV1"),
        ("LUM-OA-MIB", "oaModuleGroupV4"))
)
if mibBuilder.loadTexts:
    lumOaBasicComplV19.setStatus(
        "current"
    )

lumOaMinimalComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19, 1, 4, 1)
)
lumOaMinimalComplV1.setObjects(
      *(("LUM-OA-MIB", "oaGeneralGroupV2"),
        ("LUM-OA-MIB", "oaIfGroupV5"))
)
if mibBuilder.loadTexts:
    lumOaMinimalComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-OA-MIB",
    **{"lumOaMIBModule": lumOaMIBModule,
       "lumOaConfs": lumOaConfs,
       "lumOaGroups": lumOaGroups,
       "oaGeneralGroup": oaGeneralGroup,
       "oaIfGroup": oaIfGroup,
       "oaIfGroupV2": oaIfGroupV2,
       "oaIfGroupV3": oaIfGroupV3,
       "oaGeneralGroupV2": oaGeneralGroupV2,
       "oaIfGroupV4": oaIfGroupV4,
       "oaIfGroupV5": oaIfGroupV5,
       "oaIfGroupV6": oaIfGroupV6,
       "oaVoaIfGroupV1": oaVoaIfGroupV1,
       "oaIfGroupV7": oaIfGroupV7,
       "oaIfGroupV8": oaIfGroupV8,
       "oaVoaClientIfGroupV1": oaVoaClientIfGroupV1,
       "oaVoaLineIfGroupV1": oaVoaLineIfGroupV1,
       "oaGeneralGroupV3": oaGeneralGroupV3,
       "oaVoaClientIfGroupV2": oaVoaClientIfGroupV2,
       "oaModuleGroupV1": oaModuleGroupV1,
       "oaGeneralGroupV4": oaGeneralGroupV4,
       "oaIfGroupV9": oaIfGroupV9,
       "oaModuleGroupV2": oaModuleGroupV2,
       "oaIfGroupV10": oaIfGroupV10,
       "oaIfGroupV11": oaIfGroupV11,
       "oaVoaClientIfGroupV3": oaVoaClientIfGroupV3,
       "oaIfGroupV12": oaIfGroupV12,
       "oaModuleGroupV3": oaModuleGroupV3,
       "oaIfGroupV13": oaIfGroupV13,
       "oaIfGroupV14": oaIfGroupV14,
       "oaIfGroupV15": oaIfGroupV15,
       "oaModuleGroupV4": oaModuleGroupV4,
       "lumOaCompl": lumOaCompl,
       "lumOaBasicComplV1": lumOaBasicComplV1,
       "lumOaBasicComplV2": lumOaBasicComplV2,
       "lumOaBasicComplV3": lumOaBasicComplV3,
       "lumOaBasicComplV4": lumOaBasicComplV4,
       "lumOaBasicComplV5": lumOaBasicComplV5,
       "lumOaBasicComplV6": lumOaBasicComplV6,
       "lumOaBasicComplV7": lumOaBasicComplV7,
       "lumOaBasicComplV8": lumOaBasicComplV8,
       "lumOaBasicComplV9": lumOaBasicComplV9,
       "lumOaBasicComplV10": lumOaBasicComplV10,
       "lumOaBasicComplV11": lumOaBasicComplV11,
       "lumOaBasicComplV12": lumOaBasicComplV12,
       "lumOaBasicComplV13": lumOaBasicComplV13,
       "lumOaBasicComplV14": lumOaBasicComplV14,
       "lumOaBasicComplV15": lumOaBasicComplV15,
       "lumOaBasicComplV16": lumOaBasicComplV16,
       "lumOaBasicComplV17": lumOaBasicComplV17,
       "lumOaBasicComplV18": lumOaBasicComplV18,
       "lumOaBasicComplV19": lumOaBasicComplV19,
       "lumOaMinimalGroups": lumOaMinimalGroups,
       "lumOaMinimalCompl": lumOaMinimalCompl,
       "lumOaMinimalComplV1": lumOaMinimalComplV1,
       "lumOaMIBObjects": lumOaMIBObjects,
       "oaGeneral": oaGeneral,
       "oaGeneralLastChangeTime": oaGeneralLastChangeTime,
       "oaGeneralStateLastChangeTime": oaGeneralStateLastChangeTime,
       "oaGeneralOaIfTableSize": oaGeneralOaIfTableSize,
       "oaGeneralVoaIfTableSize": oaGeneralVoaIfTableSize,
       "oaGeneralVoaClientIfTableSize": oaGeneralVoaClientIfTableSize,
       "oaGeneralVoaLineIfTableSize": oaGeneralVoaLineIfTableSize,
       "oaGeneralOaModuleTableSize": oaGeneralOaModuleTableSize,
       "oaIfList": oaIfList,
       "oaIfTable": oaIfTable,
       "oaIfEntry": oaIfEntry,
       "oaIfIndex": oaIfIndex,
       "oaIfName": oaIfName,
       "oaIfDescr": oaIfDescr,
       "oaIfSubrack": oaIfSubrack,
       "oaIfSlot": oaIfSlot,
       "oaIfTxPort": oaIfTxPort,
       "oaIfRxPort": oaIfRxPort,
       "oaIfInvPhysIndexOrZero": oaIfInvPhysIndexOrZero,
       "oaIfAdminStatus": oaIfAdminStatus,
       "oaIfOperStatus": oaIfOperStatus,
       "oaIfLaserStatus": oaIfLaserStatus,
       "oaIfAmplifierType": oaIfAmplifierType,
       "oaIfWantedAbsolutePowerLevel": oaIfWantedAbsolutePowerLevel,
       "oaIfWantedRelativePowerLevel": oaIfWantedRelativePowerLevel,
       "oaIfWantedGain": oaIfWantedGain,
       "oaIfFrequencyMin": oaIfFrequencyMin,
       "oaIfFrequencyMax": oaIfFrequencyMax,
       "oaIfNominalTxPower": oaIfNominalTxPower,
       "oaIfTxPowerLevel": oaIfTxPowerLevel,
       "oaIfRxPowerLevel": oaIfRxPowerLevel,
       "oaIfRxPowerLevelLowThreshold": oaIfRxPowerLevelLowThreshold,
       "oaIfLaserBias": oaIfLaserBias,
       "oaIfNominalLaserTemp": oaIfNominalLaserTemp,
       "oaIfRelativeLaserTemp": oaIfRelativeLaserTemp,
       "oaIfLossOfSignalThreshold": oaIfLossOfSignalThreshold,
       "oaIfLossOfSignal": oaIfLossOfSignal,
       "oaIfPumpLaserTempHigh": oaIfPumpLaserTempHigh,
       "oaIfRegulationProblemRxPowerHigh": oaIfRegulationProblemRxPowerHigh,
       "oaIfRegulationProblemTxPowerHigh": oaIfRegulationProblemTxPowerHigh,
       "oaIfRegulationProblemTxPowerLow": oaIfRegulationProblemTxPowerLow,
       "oaIfReceivedPowerLow": oaIfReceivedPowerLow,
       "oaIfLaserBiasHigh": oaIfLaserBiasHigh,
       "oaIfLaserTempControlFault": oaIfLaserTempControlFault,
       "oaIfHwMissing": oaIfHwMissing,
       "oaIfConfigurationCommand": oaIfConfigurationCommand,
       "oaIfPumpLaserTempLow": oaIfPumpLaserTempLow,
       "oaIfLaserTempLowRelativeThreshold": oaIfLaserTempLowRelativeThreshold,
       "oaIfLaserTempHighRelativeThreshold": oaIfLaserTempHighRelativeThreshold,
       "oaIfAmpTypeNotSupportedByHw": oaIfAmpTypeNotSupportedByHw,
       "oaIfWantedSignalPowerLevel": oaIfWantedSignalPowerLevel,
       "oaIfObjectProperty": oaIfObjectProperty,
       "oaIfLaserForcedOn": oaIfLaserForcedOn,
       "oaIfActualLaserTemp": oaIfActualLaserTemp,
       "oaIfAutomaticPowerShutdown": oaIfAutomaticPowerShutdown,
       "oaIfDisabled": oaIfDisabled,
       "oaIfWantedPowerLimit": oaIfWantedPowerLimit,
       "oaIfModuleInfo": oaIfModuleInfo,
       "oaIfMonitorInsertionLoss": oaIfMonitorInsertionLoss,
       "oaIfNumMonitorInsertionLoss": oaIfNumMonitorInsertionLoss,
       "oaIfFunctionalType": oaIfFunctionalType,
       "oaIfActualGain": oaIfActualGain,
       "oaIfSaturationFault": oaIfSaturationFault,
       "oaIfWantedGainTilt": oaIfWantedGainTilt,
       "oaIfTxPowerLevelLowThreshold": oaIfTxPowerLevelLowThreshold,
       "oaIfLaserPumpBias": oaIfLaserPumpBias,
       "oaIfCaseTempOutOfrange": oaIfCaseTempOutOfrange,
       "oaIfLaserTempOutOfRange": oaIfLaserTempOutOfRange,
       "oaIfSupportsReadMonitorInsertionLoss": oaIfSupportsReadMonitorInsertionLoss,
       "oaIfTxSignalStatus": oaIfTxSignalStatus,
       "oaIfRxSignalStatus": oaIfRxSignalStatus,
       "oaIfOutputPowerFail": oaIfOutputPowerFail,
       "lumentisOaNotifications": lumentisOaNotifications,
       "oaVoaIfList": oaVoaIfList,
       "oaVoaIfTable": oaVoaIfTable,
       "oaVoaIfEntry": oaVoaIfEntry,
       "oaVoaIfIndex": oaVoaIfIndex,
       "oaVoaIfName": oaVoaIfName,
       "oaVoaIfDescr": oaVoaIfDescr,
       "oaVoaIfSubrack": oaVoaIfSubrack,
       "oaVoaIfSlot": oaVoaIfSlot,
       "oaVoaIfTxPort": oaVoaIfTxPort,
       "oaVoaIfRxPort": oaVoaIfRxPort,
       "oaVoaIfInvPhysIndexOrZero": oaVoaIfInvPhysIndexOrZero,
       "oaVoaIfAdminStatus": oaVoaIfAdminStatus,
       "oaVoaIfOperStatus": oaVoaIfOperStatus,
       "oaVoaIfObjectProperty": oaVoaIfObjectProperty,
       "oaVoaIfControlMode": oaVoaIfControlMode,
       "oaVoaIfWantedOutputPower": oaVoaIfWantedOutputPower,
       "oaVoaIfCurrentOutputPower": oaVoaIfCurrentOutputPower,
       "oaVoaIfRegulationRange": oaVoaIfRegulationRange,
       "oaVoaIfWantedAttenuation": oaVoaIfWantedAttenuation,
       "oaVoaIfCurrentAttenuation": oaVoaIfCurrentAttenuation,
       "oaVoaIfSamplePeriod": oaVoaIfSamplePeriod,
       "oaVoaIfOuputPowerControlFailure": oaVoaIfOuputPowerControlFailure,
       "oaVoaIfCurrentPowerOutOfRange": oaVoaIfCurrentPowerOutOfRange,
       "oaVoaIfConfigurationCommand": oaVoaIfConfigurationCommand,
       "oaVoaIfInInstallationMode": oaVoaIfInInstallationMode,
       "oaVoaClientIfList": oaVoaClientIfList,
       "oaVoaClientIfTable": oaVoaClientIfTable,
       "oaVoaClientIfEntry": oaVoaClientIfEntry,
       "oaVoaClientIfIndex": oaVoaClientIfIndex,
       "oaVoaClientIfName": oaVoaClientIfName,
       "oaVoaClientIfDescr": oaVoaClientIfDescr,
       "oaVoaClientIfSubrack": oaVoaClientIfSubrack,
       "oaVoaClientIfSlot": oaVoaClientIfSlot,
       "oaVoaClientIfTxPort": oaVoaClientIfTxPort,
       "oaVoaClientIfRxPort": oaVoaClientIfRxPort,
       "oaVoaClientIfInvPhysIndexOrZero": oaVoaClientIfInvPhysIndexOrZero,
       "oaVoaClientIfAdminStatus": oaVoaClientIfAdminStatus,
       "oaVoaClientIfOperStatus": oaVoaClientIfOperStatus,
       "oaVoaClientIfObjectProperty": oaVoaClientIfObjectProperty,
       "oaVoaClientIfControlMode": oaVoaClientIfControlMode,
       "oaVoaClientIfWantedAttenuation": oaVoaClientIfWantedAttenuation,
       "oaVoaClientIfCurrentAttenuation": oaVoaClientIfCurrentAttenuation,
       "oaVoaClientIfLambda": oaVoaClientIfLambda,
       "oaVoaClientIfAbsoluteAttenuation": oaVoaClientIfAbsoluteAttenuation,
       "oaVoaClientIfVoa2CurrentAttenuation": oaVoaClientIfVoa2CurrentAttenuation,
       "oaVoaClientIfDecreaseAttenuation": oaVoaClientIfDecreaseAttenuation,
       "oaVoaClientIfIncreaseAttenuation": oaVoaClientIfIncreaseAttenuation,
       "oaVoaClientIfInsertionLoss": oaVoaClientIfInsertionLoss,
       "oaVoaClientIfExpectedFrequency": oaVoaClientIfExpectedFrequency,
       "oaVoaClientIfSfpMissing": oaVoaClientIfSfpMissing,
       "oaVoaClientIfSfpClass": oaVoaClientIfSfpClass,
       "oaVoaClientIfSfpTransmitterFailed": oaVoaClientIfSfpTransmitterFailed,
       "oaVoaClientIfSfpMediaMismatch": oaVoaClientIfSfpMediaMismatch,
       "oaVoaClientIfLossOfSignal": oaVoaClientIfLossOfSignal,
       "oaVoaClientIfSfpCodeMismatch": oaVoaClientIfSfpCodeMismatch,
       "oaVoaClientIfAttenuationConfigMismatch": oaVoaClientIfAttenuationConfigMismatch,
       "oaVoaLineIfList": oaVoaLineIfList,
       "oaVoaLineIfTable": oaVoaLineIfTable,
       "oaVoaLineIfEntry": oaVoaLineIfEntry,
       "oaVoaLineIfIndex": oaVoaLineIfIndex,
       "oaVoaLineIfName": oaVoaLineIfName,
       "oaVoaLineIfDescr": oaVoaLineIfDescr,
       "oaVoaLineIfSubrack": oaVoaLineIfSubrack,
       "oaVoaLineIfSlot": oaVoaLineIfSlot,
       "oaVoaLineIfTxPort": oaVoaLineIfTxPort,
       "oaVoaLineIfRxPort": oaVoaLineIfRxPort,
       "oaVoaLineIfInvPhysIndexOrZero": oaVoaLineIfInvPhysIndexOrZero,
       "oaVoaLineIfAdminStatus": oaVoaLineIfAdminStatus,
       "oaVoaLineIfOperStatus": oaVoaLineIfOperStatus,
       "oaVoaLineIfModuleFailure": oaVoaLineIfModuleFailure,
       "oaVoaLineIfObjectProperty": oaVoaLineIfObjectProperty,
       "oaModuleList": oaModuleList,
       "oaModuleTable": oaModuleTable,
       "oaModuleEntry": oaModuleEntry,
       "oaModuleIndex": oaModuleIndex,
       "oaModuleName": oaModuleName,
       "oaModuleDescr": oaModuleDescr,
       "oaModuleSubrack": oaModuleSubrack,
       "oaModuleSlot": oaModuleSlot,
       "oaModuleNumber": oaModuleNumber,
       "oaModuleInvPhysIndexOrZero": oaModuleInvPhysIndexOrZero,
       "oaModuleAdminStatus": oaModuleAdminStatus,
       "oaModuleOperStatus": oaModuleOperStatus,
       "oaModuleObjectProperty": oaModuleObjectProperty,
       "oaModuleNominalTemp": oaModuleNominalTemp,
       "oaModuleRelativeTemp": oaModuleRelativeTemp,
       "oaModuleTempFailure": oaModuleTempFailure,
       "oaModuleTemperature": oaModuleTemperature,
       "oaModuleCommunicationFailure": oaModuleCommunicationFailure,
       "oaModuleModuleInfo": oaModuleModuleInfo,
       "oaModuleVcomThresholdExceeded": oaModuleVcomThresholdExceeded,
       "oaModuleFirmwareUpgradeAvailable": oaModuleFirmwareUpgradeAvailable,
       "oaModuleWarmingUp": oaModuleWarmingUp,
       "oaModuleFailure": oaModuleFailure}
)
