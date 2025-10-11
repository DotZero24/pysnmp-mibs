# SNMP MIB module (LUM-ROADM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-ROADM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:36 2025
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
 lumRoadmMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumRoadmMIB")

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

lumRoadmMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 31)
)
if mibBuilder.loadTexts:
    lumRoadmMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-11-30 00:00",
         "2016-01-11 00:00",
         "2011-12-20 00:00",
         "2011-02-04 00:00",
         "2007-04-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumRoadmConfs_ObjectIdentity = ObjectIdentity
lumRoadmConfs = _LumRoadmConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1)
)
_LumRoadmGroups_ObjectIdentity = ObjectIdentity
lumRoadmGroups = _LumRoadmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 1)
)
_LumRoadmCompl_ObjectIdentity = ObjectIdentity
lumRoadmCompl = _LumRoadmCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 2)
)
_LumRoadmMinimalGroups_ObjectIdentity = ObjectIdentity
lumRoadmMinimalGroups = _LumRoadmMinimalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 3)
)
_LumRoadmMinimalCompl_ObjectIdentity = ObjectIdentity
lumRoadmMinimalCompl = _LumRoadmMinimalCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 4)
)
_LumRoadmMIBObjects_ObjectIdentity = ObjectIdentity
lumRoadmMIBObjects = _LumRoadmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2)
)
_RoadmGeneral_ObjectIdentity = ObjectIdentity
roadmGeneral = _RoadmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 1)
)
_RoadmGeneralConfigLastChangeTime_Type = DateAndTime
_RoadmGeneralConfigLastChangeTime_Object = MibScalar
roadmGeneralConfigLastChangeTime = _RoadmGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 1, 1),
    _RoadmGeneralConfigLastChangeTime_Type()
)
roadmGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGeneralConfigLastChangeTime.setStatus("current")
_RoadmGeneralStateLastChangeTime_Type = DateAndTime
_RoadmGeneralStateLastChangeTime_Object = MibScalar
roadmGeneralStateLastChangeTime = _RoadmGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 1, 2),
    _RoadmGeneralStateLastChangeTime_Type()
)
roadmGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGeneralStateLastChangeTime.setStatus("current")
_RoadmGeneralRoadmAddDropIfTableSize_Type = Unsigned32
_RoadmGeneralRoadmAddDropIfTableSize_Object = MibScalar
roadmGeneralRoadmAddDropIfTableSize = _RoadmGeneralRoadmAddDropIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 1, 3),
    _RoadmGeneralRoadmAddDropIfTableSize_Type()
)
roadmGeneralRoadmAddDropIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGeneralRoadmAddDropIfTableSize.setStatus("current")
_RoadmGeneralRoadmLineIfTableSize_Type = Unsigned32
_RoadmGeneralRoadmLineIfTableSize_Object = MibScalar
roadmGeneralRoadmLineIfTableSize = _RoadmGeneralRoadmLineIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 1, 4),
    _RoadmGeneralRoadmLineIfTableSize_Type()
)
roadmGeneralRoadmLineIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGeneralRoadmLineIfTableSize.setStatus("current")
_RoadmGeneralRoadmGroupRoadmTableSize_Type = Unsigned32
_RoadmGeneralRoadmGroupRoadmTableSize_Object = MibScalar
roadmGeneralRoadmGroupRoadmTableSize = _RoadmGeneralRoadmGroupRoadmTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 1, 5),
    _RoadmGeneralRoadmGroupRoadmTableSize_Type()
)
roadmGeneralRoadmGroupRoadmTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGeneralRoadmGroupRoadmTableSize.setStatus("current")
_RoadmGeneralRoadmGroupLineTableSize_Type = Unsigned32
_RoadmGeneralRoadmGroupLineTableSize_Object = MibScalar
roadmGeneralRoadmGroupLineTableSize = _RoadmGeneralRoadmGroupLineTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 1, 6),
    _RoadmGeneralRoadmGroupLineTableSize_Type()
)
roadmGeneralRoadmGroupLineTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGeneralRoadmGroupLineTableSize.setStatus("current")
_RoadmGeneralRoadmLineTableSize_Type = Unsigned32
_RoadmGeneralRoadmLineTableSize_Object = MibScalar
roadmGeneralRoadmLineTableSize = _RoadmGeneralRoadmLineTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 1, 7),
    _RoadmGeneralRoadmLineTableSize_Type()
)
roadmGeneralRoadmLineTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGeneralRoadmLineTableSize.setStatus("current")
_RoadmGeneralChannelTableSize_Type = Unsigned32
_RoadmGeneralChannelTableSize_Object = MibScalar
roadmGeneralChannelTableSize = _RoadmGeneralChannelTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 1, 8),
    _RoadmGeneralChannelTableSize_Type()
)
roadmGeneralChannelTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGeneralChannelTableSize.setStatus("current")
_RoadmAddDropIfList_ObjectIdentity = ObjectIdentity
roadmAddDropIfList = _RoadmAddDropIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2)
)
_RoadmAddDropIfTable_Object = MibTable
roadmAddDropIfTable = _RoadmAddDropIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1)
)
if mibBuilder.loadTexts:
    roadmAddDropIfTable.setStatus("current")
_RoadmAddDropIfEntry_Object = MibTableRow
roadmAddDropIfEntry = _RoadmAddDropIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1)
)
roadmAddDropIfEntry.setIndexNames(
    (0, "LUM-ROADM-MIB", "roadmAddDropIfIndex"),
)
if mibBuilder.loadTexts:
    roadmAddDropIfEntry.setStatus("current")


class _RoadmAddDropIfIndex_Type(Unsigned32):
    """Custom type roadmAddDropIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RoadmAddDropIfIndex_Type.__name__ = "Unsigned32"
_RoadmAddDropIfIndex_Object = MibTableColumn
roadmAddDropIfIndex = _RoadmAddDropIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 1),
    _RoadmAddDropIfIndex_Type()
)
roadmAddDropIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfIndex.setStatus("current")
_RoadmAddDropIfName_Type = MgmtNameString
_RoadmAddDropIfName_Object = MibTableColumn
roadmAddDropIfName = _RoadmAddDropIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 2),
    _RoadmAddDropIfName_Type()
)
roadmAddDropIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfName.setStatus("current")


class _RoadmAddDropIfDescr_Type(DisplayString):
    """Custom type roadmAddDropIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_RoadmAddDropIfDescr_Type.__name__ = "DisplayString"
_RoadmAddDropIfDescr_Object = MibTableColumn
roadmAddDropIfDescr = _RoadmAddDropIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 3),
    _RoadmAddDropIfDescr_Type()
)
roadmAddDropIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roadmAddDropIfDescr.setStatus("current")
_RoadmAddDropIfSubrack_Type = SubrackNumber
_RoadmAddDropIfSubrack_Object = MibTableColumn
roadmAddDropIfSubrack = _RoadmAddDropIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 4),
    _RoadmAddDropIfSubrack_Type()
)
roadmAddDropIfSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmAddDropIfSubrack.setStatus("current")
_RoadmAddDropIfSlot_Type = SlotNumber
_RoadmAddDropIfSlot_Object = MibTableColumn
roadmAddDropIfSlot = _RoadmAddDropIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 5),
    _RoadmAddDropIfSlot_Type()
)
roadmAddDropIfSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmAddDropIfSlot.setStatus("current")
_RoadmAddDropIfTxPort_Type = PortNumber
_RoadmAddDropIfTxPort_Object = MibTableColumn
roadmAddDropIfTxPort = _RoadmAddDropIfTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 6),
    _RoadmAddDropIfTxPort_Type()
)
roadmAddDropIfTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmAddDropIfTxPort.setStatus("current")
_RoadmAddDropIfRxPort_Type = PortNumber
_RoadmAddDropIfRxPort_Object = MibTableColumn
roadmAddDropIfRxPort = _RoadmAddDropIfRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 7),
    _RoadmAddDropIfRxPort_Type()
)
roadmAddDropIfRxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmAddDropIfRxPort.setStatus("current")


class _RoadmAddDropIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type roadmAddDropIfInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RoadmAddDropIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_RoadmAddDropIfInvPhysIndexOrZero_Object = MibTableColumn
roadmAddDropIfInvPhysIndexOrZero = _RoadmAddDropIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 8),
    _RoadmAddDropIfInvPhysIndexOrZero_Type()
)
roadmAddDropIfInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfInvPhysIndexOrZero.setStatus("current")


class _RoadmAddDropIfAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type roadmAddDropIfAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 1


_RoadmAddDropIfAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_RoadmAddDropIfAdminStatus_Object = MibTableColumn
roadmAddDropIfAdminStatus = _RoadmAddDropIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 9),
    _RoadmAddDropIfAdminStatus_Type()
)
roadmAddDropIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roadmAddDropIfAdminStatus.setStatus("current")


class _RoadmAddDropIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type roadmAddDropIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_RoadmAddDropIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_RoadmAddDropIfOperStatus_Object = MibTableColumn
roadmAddDropIfOperStatus = _RoadmAddDropIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 10),
    _RoadmAddDropIfOperStatus_Type()
)
roadmAddDropIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfOperStatus.setStatus("current")


class _RoadmAddDropIfTemperature_Type(Integer32):
    """Custom type roadmAddDropIfTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_RoadmAddDropIfTemperature_Type.__name__ = "Integer32"
_RoadmAddDropIfTemperature_Object = MibTableColumn
roadmAddDropIfTemperature = _RoadmAddDropIfTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 11),
    _RoadmAddDropIfTemperature_Type()
)
roadmAddDropIfTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfTemperature.setStatus("current")


class _RoadmAddDropIfDropFrequencyMin_Type(LambdaFrequency):
    """Custom type roadmAddDropIfDropFrequencyMin based on LambdaFrequency"""
    defaultValue = 0


_RoadmAddDropIfDropFrequencyMin_Type.__name__ = "LambdaFrequency"
_RoadmAddDropIfDropFrequencyMin_Object = MibTableColumn
roadmAddDropIfDropFrequencyMin = _RoadmAddDropIfDropFrequencyMin_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 12),
    _RoadmAddDropIfDropFrequencyMin_Type()
)
roadmAddDropIfDropFrequencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfDropFrequencyMin.setStatus("current")


class _RoadmAddDropIfDropFrequencyMax_Type(LambdaFrequency):
    """Custom type roadmAddDropIfDropFrequencyMax based on LambdaFrequency"""
    defaultValue = 0


_RoadmAddDropIfDropFrequencyMax_Type.__name__ = "LambdaFrequency"
_RoadmAddDropIfDropFrequencyMax_Object = MibTableColumn
roadmAddDropIfDropFrequencyMax = _RoadmAddDropIfDropFrequencyMax_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 13),
    _RoadmAddDropIfDropFrequencyMax_Type()
)
roadmAddDropIfDropFrequencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfDropFrequencyMax.setStatus("current")
_RoadmAddDropIfObjectProperty_Type = ObjectProperty
_RoadmAddDropIfObjectProperty_Object = MibTableColumn
roadmAddDropIfObjectProperty = _RoadmAddDropIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 14),
    _RoadmAddDropIfObjectProperty_Type()
)
roadmAddDropIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfObjectProperty.setStatus("current")
_RoadmAddDropIfConfigurationCommand_Type = CommandString
_RoadmAddDropIfConfigurationCommand_Object = MibTableColumn
roadmAddDropIfConfigurationCommand = _RoadmAddDropIfConfigurationCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 15),
    _RoadmAddDropIfConfigurationCommand_Type()
)
roadmAddDropIfConfigurationCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfConfigurationCommand.setStatus("current")
_RoadmAddDropIfModuleFailure_Type = FaultStatus
_RoadmAddDropIfModuleFailure_Object = MibTableColumn
roadmAddDropIfModuleFailure = _RoadmAddDropIfModuleFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 16),
    _RoadmAddDropIfModuleFailure_Type()
)
roadmAddDropIfModuleFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfModuleFailure.setStatus("current")


class _RoadmAddDropIfTxSignalStatus_Type(Integer32):
    """Custom type roadmAddDropIfTxSignalStatus based on Integer32"""
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


_RoadmAddDropIfTxSignalStatus_Type.__name__ = "Integer32"
_RoadmAddDropIfTxSignalStatus_Object = MibTableColumn
roadmAddDropIfTxSignalStatus = _RoadmAddDropIfTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 17),
    _RoadmAddDropIfTxSignalStatus_Type()
)
roadmAddDropIfTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfTxSignalStatus.setStatus("current")


class _RoadmAddDropIfMode_Type(Integer32):
    """Custom type roadmAddDropIfMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("express", 1),
          ("drop", 2))
    )


_RoadmAddDropIfMode_Type.__name__ = "Integer32"
_RoadmAddDropIfMode_Object = MibTableColumn
roadmAddDropIfMode = _RoadmAddDropIfMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 18),
    _RoadmAddDropIfMode_Type()
)
roadmAddDropIfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfMode.setStatus("current")


class _RoadmAddDropIfDescr2_Type(DisplayString):
    """Custom type roadmAddDropIfDescr2 based on DisplayString"""
    defaultValue = OctetString("")


_RoadmAddDropIfDescr2_Type.__name__ = "DisplayString"
_RoadmAddDropIfDescr2_Object = MibTableColumn
roadmAddDropIfDescr2 = _RoadmAddDropIfDescr2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 19),
    _RoadmAddDropIfDescr2_Type()
)
roadmAddDropIfDescr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roadmAddDropIfDescr2.setStatus("current")


class _RoadmAddDropIfSpacingMode_Type(Integer32):
    """Custom type roadmAddDropIfSpacingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("spacing100GHz", 1),
          ("spacing50GHz", 2))
    )


_RoadmAddDropIfSpacingMode_Type.__name__ = "Integer32"
_RoadmAddDropIfSpacingMode_Object = MibTableColumn
roadmAddDropIfSpacingMode = _RoadmAddDropIfSpacingMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 20),
    _RoadmAddDropIfSpacingMode_Type()
)
roadmAddDropIfSpacingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfSpacingMode.setStatus("current")


class _RoadmAddDropIfGuardChannel1_Type(LambdaFrequency):
    """Custom type roadmAddDropIfGuardChannel1 based on LambdaFrequency"""
    defaultValue = 0


_RoadmAddDropIfGuardChannel1_Type.__name__ = "LambdaFrequency"
_RoadmAddDropIfGuardChannel1_Object = MibTableColumn
roadmAddDropIfGuardChannel1 = _RoadmAddDropIfGuardChannel1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 21),
    _RoadmAddDropIfGuardChannel1_Type()
)
roadmAddDropIfGuardChannel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfGuardChannel1.setStatus("current")


class _RoadmAddDropIfGuardChannel2_Type(LambdaFrequency):
    """Custom type roadmAddDropIfGuardChannel2 based on LambdaFrequency"""
    defaultValue = 0


_RoadmAddDropIfGuardChannel2_Type.__name__ = "LambdaFrequency"
_RoadmAddDropIfGuardChannel2_Object = MibTableColumn
roadmAddDropIfGuardChannel2 = _RoadmAddDropIfGuardChannel2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 22),
    _RoadmAddDropIfGuardChannel2_Type()
)
roadmAddDropIfGuardChannel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfGuardChannel2.setStatus("current")


class _RoadmAddDropIfDropFrequencyLimitMin_Type(LambdaFrequency):
    """Custom type roadmAddDropIfDropFrequencyLimitMin based on LambdaFrequency"""
    defaultValue = 0


_RoadmAddDropIfDropFrequencyLimitMin_Type.__name__ = "LambdaFrequency"
_RoadmAddDropIfDropFrequencyLimitMin_Object = MibTableColumn
roadmAddDropIfDropFrequencyLimitMin = _RoadmAddDropIfDropFrequencyLimitMin_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 23),
    _RoadmAddDropIfDropFrequencyLimitMin_Type()
)
roadmAddDropIfDropFrequencyLimitMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmAddDropIfDropFrequencyLimitMin.setStatus("current")


class _RoadmAddDropIfDropFrequencyLimitMax_Type(LambdaFrequency):
    """Custom type roadmAddDropIfDropFrequencyLimitMax based on LambdaFrequency"""
    defaultValue = 0


_RoadmAddDropIfDropFrequencyLimitMax_Type.__name__ = "LambdaFrequency"
_RoadmAddDropIfDropFrequencyLimitMax_Object = MibTableColumn
roadmAddDropIfDropFrequencyLimitMax = _RoadmAddDropIfDropFrequencyLimitMax_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 24),
    _RoadmAddDropIfDropFrequencyLimitMax_Type()
)
roadmAddDropIfDropFrequencyLimitMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmAddDropIfDropFrequencyLimitMax.setStatus("current")
_RoadmAddDropIfLimitConfigurationCommand_Type = CommandString
_RoadmAddDropIfLimitConfigurationCommand_Object = MibTableColumn
roadmAddDropIfLimitConfigurationCommand = _RoadmAddDropIfLimitConfigurationCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 25),
    _RoadmAddDropIfLimitConfigurationCommand_Type()
)
roadmAddDropIfLimitConfigurationCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfLimitConfigurationCommand.setStatus("current")


class _RoadmAddDropIfGroupRoadmMode_Type(Integer32):
    """Custom type roadmAddDropIfGroupRoadmMode based on Integer32"""
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


_RoadmAddDropIfGroupRoadmMode_Type.__name__ = "Integer32"
_RoadmAddDropIfGroupRoadmMode_Object = MibTableColumn
roadmAddDropIfGroupRoadmMode = _RoadmAddDropIfGroupRoadmMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 26),
    _RoadmAddDropIfGroupRoadmMode_Type()
)
roadmAddDropIfGroupRoadmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfGroupRoadmMode.setStatus("current")


class _RoadmAddDropIfPasswd_Type(DisplayString):
    """Custom type roadmAddDropIfPasswd based on DisplayString"""
    defaultValue = OctetString("-")


_RoadmAddDropIfPasswd_Type.__name__ = "DisplayString"
_RoadmAddDropIfPasswd_Object = MibTableColumn
roadmAddDropIfPasswd = _RoadmAddDropIfPasswd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 27),
    _RoadmAddDropIfPasswd_Type()
)
roadmAddDropIfPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmAddDropIfPasswd.setStatus("current")
_RoadmAddDropIfPasswdConfig_Type = CommandString
_RoadmAddDropIfPasswdConfig_Object = MibTableColumn
roadmAddDropIfPasswdConfig = _RoadmAddDropIfPasswdConfig_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 28),
    _RoadmAddDropIfPasswdConfig_Type()
)
roadmAddDropIfPasswdConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfPasswdConfig.setStatus("current")


class _RoadmAddDropIfGroupLineMode_Type(Integer32):
    """Custom type roadmAddDropIfGroupLineMode based on Integer32"""
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


_RoadmAddDropIfGroupLineMode_Type.__name__ = "Integer32"
_RoadmAddDropIfGroupLineMode_Object = MibTableColumn
roadmAddDropIfGroupLineMode = _RoadmAddDropIfGroupLineMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 29),
    _RoadmAddDropIfGroupLineMode_Type()
)
roadmAddDropIfGroupLineMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfGroupLineMode.setStatus("current")
_RoadmAddDropIfNoOfConnectedChannels_Type = Unsigned32
_RoadmAddDropIfNoOfConnectedChannels_Object = MibTableColumn
roadmAddDropIfNoOfConnectedChannels = _RoadmAddDropIfNoOfConnectedChannels_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 30),
    _RoadmAddDropIfNoOfConnectedChannels_Type()
)
roadmAddDropIfNoOfConnectedChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfNoOfConnectedChannels.setStatus("current")
_RoadmAddDropIfViewChannelList_Type = DisplayString
_RoadmAddDropIfViewChannelList_Object = MibTableColumn
roadmAddDropIfViewChannelList = _RoadmAddDropIfViewChannelList_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 31),
    _RoadmAddDropIfViewChannelList_Type()
)
roadmAddDropIfViewChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfViewChannelList.setStatus("current")
_RoadmAddDropIfConnectedChannelMask_Type = DisplayString
_RoadmAddDropIfConnectedChannelMask_Object = MibTableColumn
roadmAddDropIfConnectedChannelMask = _RoadmAddDropIfConnectedChannelMask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 32),
    _RoadmAddDropIfConnectedChannelMask_Type()
)
roadmAddDropIfConnectedChannelMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmAddDropIfConnectedChannelMask.setStatus("current")
_RoadmAddDropIfAddChannelCommand_Type = CommandString
_RoadmAddDropIfAddChannelCommand_Object = MibTableColumn
roadmAddDropIfAddChannelCommand = _RoadmAddDropIfAddChannelCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 33),
    _RoadmAddDropIfAddChannelCommand_Type()
)
roadmAddDropIfAddChannelCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfAddChannelCommand.setStatus("current")
_RoadmAddDropIfUnlinkChannelCommand_Type = CommandString
_RoadmAddDropIfUnlinkChannelCommand_Object = MibTableColumn
roadmAddDropIfUnlinkChannelCommand = _RoadmAddDropIfUnlinkChannelCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 34),
    _RoadmAddDropIfUnlinkChannelCommand_Type()
)
roadmAddDropIfUnlinkChannelCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfUnlinkChannelCommand.setStatus("current")
_RoadmAddDropIfUnlinkAllChannelsCommand_Type = CommandString
_RoadmAddDropIfUnlinkAllChannelsCommand_Object = MibTableColumn
roadmAddDropIfUnlinkAllChannelsCommand = _RoadmAddDropIfUnlinkAllChannelsCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 35),
    _RoadmAddDropIfUnlinkAllChannelsCommand_Type()
)
roadmAddDropIfUnlinkAllChannelsCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfUnlinkAllChannelsCommand.setStatus("current")
_RoadmAddDropIfSetAttenuationCommand_Type = CommandString
_RoadmAddDropIfSetAttenuationCommand_Object = MibTableColumn
roadmAddDropIfSetAttenuationCommand = _RoadmAddDropIfSetAttenuationCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 36),
    _RoadmAddDropIfSetAttenuationCommand_Type()
)
roadmAddDropIfSetAttenuationCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfSetAttenuationCommand.setStatus("current")
_RoadmAddDropIfAdjustAttenuationDeltaCommand_Type = CommandString
_RoadmAddDropIfAdjustAttenuationDeltaCommand_Object = MibTableColumn
roadmAddDropIfAdjustAttenuationDeltaCommand = _RoadmAddDropIfAdjustAttenuationDeltaCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 37),
    _RoadmAddDropIfAdjustAttenuationDeltaCommand_Type()
)
roadmAddDropIfAdjustAttenuationDeltaCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfAdjustAttenuationDeltaCommand.setStatus("current")


class _RoadmAddDropIfConnectChannelCmd_Type(Unsigned32):
    """Custom type roadmAddDropIfConnectChannelCmd based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_RoadmAddDropIfConnectChannelCmd_Type.__name__ = "Unsigned32"
_RoadmAddDropIfConnectChannelCmd_Object = MibTableColumn
roadmAddDropIfConnectChannelCmd = _RoadmAddDropIfConnectChannelCmd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 38),
    _RoadmAddDropIfConnectChannelCmd_Type()
)
roadmAddDropIfConnectChannelCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roadmAddDropIfConnectChannelCmd.setStatus("current")


class _RoadmAddDropIfDisconnectChannelCmd_Type(Unsigned32):
    """Custom type roadmAddDropIfDisconnectChannelCmd based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_RoadmAddDropIfDisconnectChannelCmd_Type.__name__ = "Unsigned32"
_RoadmAddDropIfDisconnectChannelCmd_Object = MibTableColumn
roadmAddDropIfDisconnectChannelCmd = _RoadmAddDropIfDisconnectChannelCmd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 39),
    _RoadmAddDropIfDisconnectChannelCmd_Type()
)
roadmAddDropIfDisconnectChannelCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roadmAddDropIfDisconnectChannelCmd.setStatus("current")
_RoadmAddDropIfGroupIndex_Type = Unsigned32
_RoadmAddDropIfGroupIndex_Object = MibTableColumn
roadmAddDropIfGroupIndex = _RoadmAddDropIfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 40),
    _RoadmAddDropIfGroupIndex_Type()
)
roadmAddDropIfGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfGroupIndex.setStatus("current")
_RoadmAddDropIfAddAllChannelCommand_Type = CommandString
_RoadmAddDropIfAddAllChannelCommand_Object = MibTableColumn
roadmAddDropIfAddAllChannelCommand = _RoadmAddDropIfAddAllChannelCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 41),
    _RoadmAddDropIfAddAllChannelCommand_Type()
)
roadmAddDropIfAddAllChannelCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfAddAllChannelCommand.setStatus("current")
_RoadmAddDropIfSetAdminStatusCommand_Type = CommandString
_RoadmAddDropIfSetAdminStatusCommand_Object = MibTableColumn
roadmAddDropIfSetAdminStatusCommand = _RoadmAddDropIfSetAdminStatusCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 42),
    _RoadmAddDropIfSetAdminStatusCommand_Type()
)
roadmAddDropIfSetAdminStatusCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfSetAdminStatusCommand.setStatus("current")


class _RoadmAddDropIfSpacingHwCapability_Type(Integer32):
    """Custom type roadmAddDropIfSpacingHwCapability based on Integer32"""
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
        *(("spacingHwCap100GHz", 1),
          ("spacingHwCap50GHz", 2),
          ("spacingHwCapFlex125", 3))
    )


_RoadmAddDropIfSpacingHwCapability_Type.__name__ = "Integer32"
_RoadmAddDropIfSpacingHwCapability_Object = MibTableColumn
roadmAddDropIfSpacingHwCapability = _RoadmAddDropIfSpacingHwCapability_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 2, 1, 1, 43),
    _RoadmAddDropIfSpacingHwCapability_Type()
)
roadmAddDropIfSpacingHwCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmAddDropIfSpacingHwCapability.setStatus("current")
_RoadmLineIfList_ObjectIdentity = ObjectIdentity
roadmLineIfList = _RoadmLineIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3)
)
_RoadmLineIfTable_Object = MibTable
roadmLineIfTable = _RoadmLineIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1)
)
if mibBuilder.loadTexts:
    roadmLineIfTable.setStatus("current")
_RoadmLineIfEntry_Object = MibTableRow
roadmLineIfEntry = _RoadmLineIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1)
)
roadmLineIfEntry.setIndexNames(
    (0, "LUM-ROADM-MIB", "roadmLineIfIndex"),
)
if mibBuilder.loadTexts:
    roadmLineIfEntry.setStatus("current")


class _RoadmLineIfIndex_Type(Unsigned32):
    """Custom type roadmLineIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RoadmLineIfIndex_Type.__name__ = "Unsigned32"
_RoadmLineIfIndex_Object = MibTableColumn
roadmLineIfIndex = _RoadmLineIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1, 1),
    _RoadmLineIfIndex_Type()
)
roadmLineIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmLineIfIndex.setStatus("current")
_RoadmLineIfName_Type = MgmtNameString
_RoadmLineIfName_Object = MibTableColumn
roadmLineIfName = _RoadmLineIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1, 2),
    _RoadmLineIfName_Type()
)
roadmLineIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmLineIfName.setStatus("current")


class _RoadmLineIfDescr_Type(DisplayString):
    """Custom type roadmLineIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_RoadmLineIfDescr_Type.__name__ = "DisplayString"
_RoadmLineIfDescr_Object = MibTableColumn
roadmLineIfDescr = _RoadmLineIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1, 3),
    _RoadmLineIfDescr_Type()
)
roadmLineIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roadmLineIfDescr.setStatus("current")
_RoadmLineIfSubrack_Type = SubrackNumber
_RoadmLineIfSubrack_Object = MibTableColumn
roadmLineIfSubrack = _RoadmLineIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1, 4),
    _RoadmLineIfSubrack_Type()
)
roadmLineIfSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmLineIfSubrack.setStatus("current")
_RoadmLineIfSlot_Type = SlotNumber
_RoadmLineIfSlot_Object = MibTableColumn
roadmLineIfSlot = _RoadmLineIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1, 5),
    _RoadmLineIfSlot_Type()
)
roadmLineIfSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmLineIfSlot.setStatus("current")
_RoadmLineIfTxPort_Type = PortNumber
_RoadmLineIfTxPort_Object = MibTableColumn
roadmLineIfTxPort = _RoadmLineIfTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1, 6),
    _RoadmLineIfTxPort_Type()
)
roadmLineIfTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmLineIfTxPort.setStatus("current")
_RoadmLineIfRxPort_Type = PortNumber
_RoadmLineIfRxPort_Object = MibTableColumn
roadmLineIfRxPort = _RoadmLineIfRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1, 7),
    _RoadmLineIfRxPort_Type()
)
roadmLineIfRxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmLineIfRxPort.setStatus("current")


class _RoadmLineIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type roadmLineIfInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RoadmLineIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_RoadmLineIfInvPhysIndexOrZero_Object = MibTableColumn
roadmLineIfInvPhysIndexOrZero = _RoadmLineIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1, 8),
    _RoadmLineIfInvPhysIndexOrZero_Type()
)
roadmLineIfInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmLineIfInvPhysIndexOrZero.setStatus("current")


class _RoadmLineIfAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type roadmLineIfAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_RoadmLineIfAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_RoadmLineIfAdminStatus_Object = MibTableColumn
roadmLineIfAdminStatus = _RoadmLineIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1, 9),
    _RoadmLineIfAdminStatus_Type()
)
roadmLineIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roadmLineIfAdminStatus.setStatus("current")


class _RoadmLineIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type roadmLineIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_RoadmLineIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_RoadmLineIfOperStatus_Object = MibTableColumn
roadmLineIfOperStatus = _RoadmLineIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1, 10),
    _RoadmLineIfOperStatus_Type()
)
roadmLineIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmLineIfOperStatus.setStatus("current")
_RoadmLineIfObjectProperty_Type = ObjectProperty
_RoadmLineIfObjectProperty_Object = MibTableColumn
roadmLineIfObjectProperty = _RoadmLineIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1, 11),
    _RoadmLineIfObjectProperty_Type()
)
roadmLineIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmLineIfObjectProperty.setStatus("current")


class _RoadmLineIfTxSignalStatus_Type(Integer32):
    """Custom type roadmLineIfTxSignalStatus based on Integer32"""
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


_RoadmLineIfTxSignalStatus_Type.__name__ = "Integer32"
_RoadmLineIfTxSignalStatus_Object = MibTableColumn
roadmLineIfTxSignalStatus = _RoadmLineIfTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1, 12),
    _RoadmLineIfTxSignalStatus_Type()
)
roadmLineIfTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmLineIfTxSignalStatus.setStatus("current")
_RoadmLineIfNoOfConnectedChannels_Type = Unsigned32
_RoadmLineIfNoOfConnectedChannels_Object = MibTableColumn
roadmLineIfNoOfConnectedChannels = _RoadmLineIfNoOfConnectedChannels_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1, 13),
    _RoadmLineIfNoOfConnectedChannels_Type()
)
roadmLineIfNoOfConnectedChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmLineIfNoOfConnectedChannels.setStatus("current")
_RoadmLineIfViewChannelList_Type = DisplayString
_RoadmLineIfViewChannelList_Object = MibTableColumn
roadmLineIfViewChannelList = _RoadmLineIfViewChannelList_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1, 14),
    _RoadmLineIfViewChannelList_Type()
)
roadmLineIfViewChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmLineIfViewChannelList.setStatus("current")
_RoadmLineIfSetAttenuationCommand_Type = CommandString
_RoadmLineIfSetAttenuationCommand_Object = MibTableColumn
roadmLineIfSetAttenuationCommand = _RoadmLineIfSetAttenuationCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1, 15),
    _RoadmLineIfSetAttenuationCommand_Type()
)
roadmLineIfSetAttenuationCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmLineIfSetAttenuationCommand.setStatus("current")
_RoadmLineIfAdjustAttenuationDeltaCommand_Type = CommandString
_RoadmLineIfAdjustAttenuationDeltaCommand_Object = MibTableColumn
roadmLineIfAdjustAttenuationDeltaCommand = _RoadmLineIfAdjustAttenuationDeltaCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1, 16),
    _RoadmLineIfAdjustAttenuationDeltaCommand_Type()
)
roadmLineIfAdjustAttenuationDeltaCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmLineIfAdjustAttenuationDeltaCommand.setStatus("current")
_RoadmLineIfMonitorInsertionLoss_Type = Unsigned32
_RoadmLineIfMonitorInsertionLoss_Object = MibTableColumn
roadmLineIfMonitorInsertionLoss = _RoadmLineIfMonitorInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1, 17),
    _RoadmLineIfMonitorInsertionLoss_Type()
)
roadmLineIfMonitorInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmLineIfMonitorInsertionLoss.setStatus("current")
_RoadmLineIfSetAdminStatusCommand_Type = CommandString
_RoadmLineIfSetAdminStatusCommand_Object = MibTableColumn
roadmLineIfSetAdminStatusCommand = _RoadmLineIfSetAdminStatusCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 3, 1, 1, 18),
    _RoadmLineIfSetAdminStatusCommand_Type()
)
roadmLineIfSetAdminStatusCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmLineIfSetAdminStatusCommand.setStatus("current")
_RoadmGroupRoadmList_ObjectIdentity = ObjectIdentity
roadmGroupRoadmList = _RoadmGroupRoadmList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4)
)
_RoadmGroupRoadmTable_Object = MibTable
roadmGroupRoadmTable = _RoadmGroupRoadmTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1)
)
if mibBuilder.loadTexts:
    roadmGroupRoadmTable.setStatus("current")
_RoadmGroupRoadmEntry_Object = MibTableRow
roadmGroupRoadmEntry = _RoadmGroupRoadmEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1)
)
roadmGroupRoadmEntry.setIndexNames(
    (0, "LUM-ROADM-MIB", "roadmGroupRoadmIndex"),
)
if mibBuilder.loadTexts:
    roadmGroupRoadmEntry.setStatus("current")


class _RoadmGroupRoadmIndex_Type(Unsigned32):
    """Custom type roadmGroupRoadmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RoadmGroupRoadmIndex_Type.__name__ = "Unsigned32"
_RoadmGroupRoadmIndex_Object = MibTableColumn
roadmGroupRoadmIndex = _RoadmGroupRoadmIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 1),
    _RoadmGroupRoadmIndex_Type()
)
roadmGroupRoadmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupRoadmIndex.setStatus("current")


class _RoadmGroupRoadmName_Type(MgmtNameString):
    """Custom type roadmGroupRoadmName based on MgmtNameString"""
    defaultValue = OctetString("")


_RoadmGroupRoadmName_Type.__name__ = "MgmtNameString"
_RoadmGroupRoadmName_Object = MibTableColumn
roadmGroupRoadmName = _RoadmGroupRoadmName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 2),
    _RoadmGroupRoadmName_Type()
)
roadmGroupRoadmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupRoadmName.setStatus("current")


class _RoadmGroupRoadmDescr_Type(DisplayString):
    """Custom type roadmGroupRoadmDescr based on DisplayString"""
    defaultValue = OctetString("")


_RoadmGroupRoadmDescr_Type.__name__ = "DisplayString"
_RoadmGroupRoadmDescr_Object = MibTableColumn
roadmGroupRoadmDescr = _RoadmGroupRoadmDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 3),
    _RoadmGroupRoadmDescr_Type()
)
roadmGroupRoadmDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roadmGroupRoadmDescr.setStatus("current")


class _RoadmGroupRoadmRightSubrack_Type(SubrackNumber):
    """Custom type roadmGroupRoadmRightSubrack based on SubrackNumber"""
    defaultValue = 0


_RoadmGroupRoadmRightSubrack_Type.__name__ = "SubrackNumber"
_RoadmGroupRoadmRightSubrack_Object = MibTableColumn
roadmGroupRoadmRightSubrack = _RoadmGroupRoadmRightSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 4),
    _RoadmGroupRoadmRightSubrack_Type()
)
roadmGroupRoadmRightSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmGroupRoadmRightSubrack.setStatus("current")


class _RoadmGroupRoadmRightSlot_Type(SlotNumber):
    """Custom type roadmGroupRoadmRightSlot based on SlotNumber"""
    defaultValue = 0


_RoadmGroupRoadmRightSlot_Type.__name__ = "SlotNumber"
_RoadmGroupRoadmRightSlot_Object = MibTableColumn
roadmGroupRoadmRightSlot = _RoadmGroupRoadmRightSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 5),
    _RoadmGroupRoadmRightSlot_Type()
)
roadmGroupRoadmRightSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmGroupRoadmRightSlot.setStatus("current")


class _RoadmGroupRoadmRightPort_Type(PortNumber):
    """Custom type roadmGroupRoadmRightPort based on PortNumber"""
    defaultValue = 0


_RoadmGroupRoadmRightPort_Type.__name__ = "PortNumber"
_RoadmGroupRoadmRightPort_Object = MibTableColumn
roadmGroupRoadmRightPort = _RoadmGroupRoadmRightPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 6),
    _RoadmGroupRoadmRightPort_Type()
)
roadmGroupRoadmRightPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmGroupRoadmRightPort.setStatus("current")


class _RoadmGroupRoadmLeftSubrack_Type(SubrackNumber):
    """Custom type roadmGroupRoadmLeftSubrack based on SubrackNumber"""
    defaultValue = 0


_RoadmGroupRoadmLeftSubrack_Type.__name__ = "SubrackNumber"
_RoadmGroupRoadmLeftSubrack_Object = MibTableColumn
roadmGroupRoadmLeftSubrack = _RoadmGroupRoadmLeftSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 7),
    _RoadmGroupRoadmLeftSubrack_Type()
)
roadmGroupRoadmLeftSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmGroupRoadmLeftSubrack.setStatus("current")


class _RoadmGroupRoadmLeftSlot_Type(SlotNumber):
    """Custom type roadmGroupRoadmLeftSlot based on SlotNumber"""
    defaultValue = 0


_RoadmGroupRoadmLeftSlot_Type.__name__ = "SlotNumber"
_RoadmGroupRoadmLeftSlot_Object = MibTableColumn
roadmGroupRoadmLeftSlot = _RoadmGroupRoadmLeftSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 8),
    _RoadmGroupRoadmLeftSlot_Type()
)
roadmGroupRoadmLeftSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmGroupRoadmLeftSlot.setStatus("current")


class _RoadmGroupRoadmLeftPort_Type(PortNumber):
    """Custom type roadmGroupRoadmLeftPort based on PortNumber"""
    defaultValue = 0


_RoadmGroupRoadmLeftPort_Type.__name__ = "PortNumber"
_RoadmGroupRoadmLeftPort_Object = MibTableColumn
roadmGroupRoadmLeftPort = _RoadmGroupRoadmLeftPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 9),
    _RoadmGroupRoadmLeftPort_Type()
)
roadmGroupRoadmLeftPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmGroupRoadmLeftPort.setStatus("current")


class _RoadmGroupRoadmAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type roadmGroupRoadmAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 1


_RoadmGroupRoadmAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_RoadmGroupRoadmAdminStatus_Object = MibTableColumn
roadmGroupRoadmAdminStatus = _RoadmGroupRoadmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 11),
    _RoadmGroupRoadmAdminStatus_Type()
)
roadmGroupRoadmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roadmGroupRoadmAdminStatus.setStatus("current")
_RoadmGroupRoadmObjectProperty_Type = ObjectProperty
_RoadmGroupRoadmObjectProperty_Object = MibTableColumn
roadmGroupRoadmObjectProperty = _RoadmGroupRoadmObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 12),
    _RoadmGroupRoadmObjectProperty_Type()
)
roadmGroupRoadmObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupRoadmObjectProperty.setStatus("current")


class _RoadmGroupRoadmDataAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type roadmGroupRoadmDataAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_RoadmGroupRoadmDataAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_RoadmGroupRoadmDataAdminStatus_Object = MibTableColumn
roadmGroupRoadmDataAdminStatus = _RoadmGroupRoadmDataAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 14),
    _RoadmGroupRoadmDataAdminStatus_Type()
)
roadmGroupRoadmDataAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roadmGroupRoadmDataAdminStatus.setStatus("current")


class _RoadmGroupRoadmDataDropFrequencyMin_Type(LambdaFrequency):
    """Custom type roadmGroupRoadmDataDropFrequencyMin based on LambdaFrequency"""
    defaultValue = 0


_RoadmGroupRoadmDataDropFrequencyMin_Type.__name__ = "LambdaFrequency"
_RoadmGroupRoadmDataDropFrequencyMin_Object = MibTableColumn
roadmGroupRoadmDataDropFrequencyMin = _RoadmGroupRoadmDataDropFrequencyMin_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 15),
    _RoadmGroupRoadmDataDropFrequencyMin_Type()
)
roadmGroupRoadmDataDropFrequencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupRoadmDataDropFrequencyMin.setStatus("current")


class _RoadmGroupRoadmDataDropFrequencyMax_Type(LambdaFrequency):
    """Custom type roadmGroupRoadmDataDropFrequencyMax based on LambdaFrequency"""
    defaultValue = 0


_RoadmGroupRoadmDataDropFrequencyMax_Type.__name__ = "LambdaFrequency"
_RoadmGroupRoadmDataDropFrequencyMax_Object = MibTableColumn
roadmGroupRoadmDataDropFrequencyMax = _RoadmGroupRoadmDataDropFrequencyMax_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 16),
    _RoadmGroupRoadmDataDropFrequencyMax_Type()
)
roadmGroupRoadmDataDropFrequencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupRoadmDataDropFrequencyMax.setStatus("current")


class _RoadmGroupRoadmDataDropFrequencyLimitMin_Type(LambdaFrequency):
    """Custom type roadmGroupRoadmDataDropFrequencyLimitMin based on LambdaFrequency"""
    defaultValue = 0


_RoadmGroupRoadmDataDropFrequencyLimitMin_Type.__name__ = "LambdaFrequency"
_RoadmGroupRoadmDataDropFrequencyLimitMin_Object = MibTableColumn
roadmGroupRoadmDataDropFrequencyLimitMin = _RoadmGroupRoadmDataDropFrequencyLimitMin_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 17),
    _RoadmGroupRoadmDataDropFrequencyLimitMin_Type()
)
roadmGroupRoadmDataDropFrequencyLimitMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmGroupRoadmDataDropFrequencyLimitMin.setStatus("current")


class _RoadmGroupRoadmDataDropFrequencyLimitMax_Type(LambdaFrequency):
    """Custom type roadmGroupRoadmDataDropFrequencyLimitMax based on LambdaFrequency"""
    defaultValue = 0


_RoadmGroupRoadmDataDropFrequencyLimitMax_Type.__name__ = "LambdaFrequency"
_RoadmGroupRoadmDataDropFrequencyLimitMax_Object = MibTableColumn
roadmGroupRoadmDataDropFrequencyLimitMax = _RoadmGroupRoadmDataDropFrequencyLimitMax_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 18),
    _RoadmGroupRoadmDataDropFrequencyLimitMax_Type()
)
roadmGroupRoadmDataDropFrequencyLimitMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmGroupRoadmDataDropFrequencyLimitMax.setStatus("current")


class _RoadmGroupRoadmDataMode_Type(Integer32):
    """Custom type roadmGroupRoadmDataMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("express", 1),
          ("drop", 2))
    )


_RoadmGroupRoadmDataMode_Type.__name__ = "Integer32"
_RoadmGroupRoadmDataMode_Object = MibTableColumn
roadmGroupRoadmDataMode = _RoadmGroupRoadmDataMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 19),
    _RoadmGroupRoadmDataMode_Type()
)
roadmGroupRoadmDataMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmGroupRoadmDataMode.setStatus("current")


class _RoadmGroupRoadmDataSpacingMode_Type(Integer32):
    """Custom type roadmGroupRoadmDataSpacingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("spacing100GHz", 1),
          ("spacing50GHz", 2))
    )


_RoadmGroupRoadmDataSpacingMode_Type.__name__ = "Integer32"
_RoadmGroupRoadmDataSpacingMode_Object = MibTableColumn
roadmGroupRoadmDataSpacingMode = _RoadmGroupRoadmDataSpacingMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 20),
    _RoadmGroupRoadmDataSpacingMode_Type()
)
roadmGroupRoadmDataSpacingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmGroupRoadmDataSpacingMode.setStatus("current")
_RoadmGroupRoadmConfigurationCommand_Type = CommandString
_RoadmGroupRoadmConfigurationCommand_Object = MibTableColumn
roadmGroupRoadmConfigurationCommand = _RoadmGroupRoadmConfigurationCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 21),
    _RoadmGroupRoadmConfigurationCommand_Type()
)
roadmGroupRoadmConfigurationCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupRoadmConfigurationCommand.setStatus("current")
_RoadmGroupRoadmLimitConfigurationCommand_Type = CommandString
_RoadmGroupRoadmLimitConfigurationCommand_Object = MibTableColumn
roadmGroupRoadmLimitConfigurationCommand = _RoadmGroupRoadmLimitConfigurationCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 22),
    _RoadmGroupRoadmLimitConfigurationCommand_Type()
)
roadmGroupRoadmLimitConfigurationCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupRoadmLimitConfigurationCommand.setStatus("current")


class _RoadmGroupRoadmPasswd_Type(DisplayString):
    """Custom type roadmGroupRoadmPasswd based on DisplayString"""
    defaultValue = OctetString("")


_RoadmGroupRoadmPasswd_Type.__name__ = "DisplayString"
_RoadmGroupRoadmPasswd_Object = MibTableColumn
roadmGroupRoadmPasswd = _RoadmGroupRoadmPasswd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 23),
    _RoadmGroupRoadmPasswd_Type()
)
roadmGroupRoadmPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmGroupRoadmPasswd.setStatus("current")
_RoadmGroupRoadmPasswdConfig_Type = CommandString
_RoadmGroupRoadmPasswdConfig_Object = MibTableColumn
roadmGroupRoadmPasswdConfig = _RoadmGroupRoadmPasswdConfig_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 24),
    _RoadmGroupRoadmPasswdConfig_Type()
)
roadmGroupRoadmPasswdConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupRoadmPasswdConfig.setStatus("current")


class _RoadmGroupRoadmDataGuardChannel1_Type(LambdaFrequency):
    """Custom type roadmGroupRoadmDataGuardChannel1 based on LambdaFrequency"""
    defaultValue = 0


_RoadmGroupRoadmDataGuardChannel1_Type.__name__ = "LambdaFrequency"
_RoadmGroupRoadmDataGuardChannel1_Object = MibTableColumn
roadmGroupRoadmDataGuardChannel1 = _RoadmGroupRoadmDataGuardChannel1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 25),
    _RoadmGroupRoadmDataGuardChannel1_Type()
)
roadmGroupRoadmDataGuardChannel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupRoadmDataGuardChannel1.setStatus("current")


class _RoadmGroupRoadmDataGuardChannel2_Type(LambdaFrequency):
    """Custom type roadmGroupRoadmDataGuardChannel2 based on LambdaFrequency"""
    defaultValue = 0


_RoadmGroupRoadmDataGuardChannel2_Type.__name__ = "LambdaFrequency"
_RoadmGroupRoadmDataGuardChannel2_Object = MibTableColumn
roadmGroupRoadmDataGuardChannel2 = _RoadmGroupRoadmDataGuardChannel2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 26),
    _RoadmGroupRoadmDataGuardChannel2_Type()
)
roadmGroupRoadmDataGuardChannel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupRoadmDataGuardChannel2.setStatus("current")
_RoadmGroupRoadmNoOfConnectedChannels_Type = Unsigned32
_RoadmGroupRoadmNoOfConnectedChannels_Object = MibTableColumn
roadmGroupRoadmNoOfConnectedChannels = _RoadmGroupRoadmNoOfConnectedChannels_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 27),
    _RoadmGroupRoadmNoOfConnectedChannels_Type()
)
roadmGroupRoadmNoOfConnectedChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupRoadmNoOfConnectedChannels.setStatus("current")
_RoadmGroupRoadmViewChannelList_Type = DisplayString
_RoadmGroupRoadmViewChannelList_Object = MibTableColumn
roadmGroupRoadmViewChannelList = _RoadmGroupRoadmViewChannelList_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 28),
    _RoadmGroupRoadmViewChannelList_Type()
)
roadmGroupRoadmViewChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupRoadmViewChannelList.setStatus("current")
_RoadmGroupRoadmConnectedChannelMask_Type = DisplayString
_RoadmGroupRoadmConnectedChannelMask_Object = MibTableColumn
roadmGroupRoadmConnectedChannelMask = _RoadmGroupRoadmConnectedChannelMask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 29),
    _RoadmGroupRoadmConnectedChannelMask_Type()
)
roadmGroupRoadmConnectedChannelMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmGroupRoadmConnectedChannelMask.setStatus("current")
_RoadmGroupRoadmAddChannelCommand_Type = CommandString
_RoadmGroupRoadmAddChannelCommand_Object = MibTableColumn
roadmGroupRoadmAddChannelCommand = _RoadmGroupRoadmAddChannelCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 30),
    _RoadmGroupRoadmAddChannelCommand_Type()
)
roadmGroupRoadmAddChannelCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupRoadmAddChannelCommand.setStatus("current")
_RoadmGroupRoadmUnlinkChannelCommand_Type = CommandString
_RoadmGroupRoadmUnlinkChannelCommand_Object = MibTableColumn
roadmGroupRoadmUnlinkChannelCommand = _RoadmGroupRoadmUnlinkChannelCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 31),
    _RoadmGroupRoadmUnlinkChannelCommand_Type()
)
roadmGroupRoadmUnlinkChannelCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupRoadmUnlinkChannelCommand.setStatus("current")
_RoadmGroupRoadmUnlinkAllChannelsCommand_Type = CommandString
_RoadmGroupRoadmUnlinkAllChannelsCommand_Object = MibTableColumn
roadmGroupRoadmUnlinkAllChannelsCommand = _RoadmGroupRoadmUnlinkAllChannelsCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 32),
    _RoadmGroupRoadmUnlinkAllChannelsCommand_Type()
)
roadmGroupRoadmUnlinkAllChannelsCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupRoadmUnlinkAllChannelsCommand.setStatus("current")


class _RoadmGroupRoadmConnectChannelCmd_Type(Unsigned32):
    """Custom type roadmGroupRoadmConnectChannelCmd based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_RoadmGroupRoadmConnectChannelCmd_Type.__name__ = "Unsigned32"
_RoadmGroupRoadmConnectChannelCmd_Object = MibTableColumn
roadmGroupRoadmConnectChannelCmd = _RoadmGroupRoadmConnectChannelCmd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 33),
    _RoadmGroupRoadmConnectChannelCmd_Type()
)
roadmGroupRoadmConnectChannelCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roadmGroupRoadmConnectChannelCmd.setStatus("current")


class _RoadmGroupRoadmDisconnectChannelCmd_Type(Unsigned32):
    """Custom type roadmGroupRoadmDisconnectChannelCmd based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_RoadmGroupRoadmDisconnectChannelCmd_Type.__name__ = "Unsigned32"
_RoadmGroupRoadmDisconnectChannelCmd_Object = MibTableColumn
roadmGroupRoadmDisconnectChannelCmd = _RoadmGroupRoadmDisconnectChannelCmd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 34),
    _RoadmGroupRoadmDisconnectChannelCmd_Type()
)
roadmGroupRoadmDisconnectChannelCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roadmGroupRoadmDisconnectChannelCmd.setStatus("current")
_RoadmGroupRoadmAddAllChannelCommand_Type = CommandString
_RoadmGroupRoadmAddAllChannelCommand_Object = MibTableColumn
roadmGroupRoadmAddAllChannelCommand = _RoadmGroupRoadmAddAllChannelCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 4, 1, 1, 35),
    _RoadmGroupRoadmAddAllChannelCommand_Type()
)
roadmGroupRoadmAddAllChannelCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupRoadmAddAllChannelCommand.setStatus("current")
_RoadmGroupLineList_ObjectIdentity = ObjectIdentity
roadmGroupLineList = _RoadmGroupLineList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 5)
)
_RoadmGroupLineTable_Object = MibTable
roadmGroupLineTable = _RoadmGroupLineTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 5, 1)
)
if mibBuilder.loadTexts:
    roadmGroupLineTable.setStatus("current")
_RoadmGroupLineEntry_Object = MibTableRow
roadmGroupLineEntry = _RoadmGroupLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 5, 1, 1)
)
roadmGroupLineEntry.setIndexNames(
    (0, "LUM-ROADM-MIB", "roadmGroupLineIndex"),
)
if mibBuilder.loadTexts:
    roadmGroupLineEntry.setStatus("current")


class _RoadmGroupLineIndex_Type(Unsigned32):
    """Custom type roadmGroupLineIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RoadmGroupLineIndex_Type.__name__ = "Unsigned32"
_RoadmGroupLineIndex_Object = MibTableColumn
roadmGroupLineIndex = _RoadmGroupLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 5, 1, 1, 1),
    _RoadmGroupLineIndex_Type()
)
roadmGroupLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupLineIndex.setStatus("current")


class _RoadmGroupLineName_Type(MgmtNameString):
    """Custom type roadmGroupLineName based on MgmtNameString"""
    defaultValue = OctetString("")


_RoadmGroupLineName_Type.__name__ = "MgmtNameString"
_RoadmGroupLineName_Object = MibTableColumn
roadmGroupLineName = _RoadmGroupLineName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 5, 1, 1, 2),
    _RoadmGroupLineName_Type()
)
roadmGroupLineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupLineName.setStatus("current")


class _RoadmGroupLineDescr_Type(DisplayString):
    """Custom type roadmGroupLineDescr based on DisplayString"""
    defaultValue = OctetString("")


_RoadmGroupLineDescr_Type.__name__ = "DisplayString"
_RoadmGroupLineDescr_Object = MibTableColumn
roadmGroupLineDescr = _RoadmGroupLineDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 5, 1, 1, 3),
    _RoadmGroupLineDescr_Type()
)
roadmGroupLineDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roadmGroupLineDescr.setStatus("current")


class _RoadmGroupLineSubrack_Type(SubrackNumber):
    """Custom type roadmGroupLineSubrack based on SubrackNumber"""
    defaultValue = 0


_RoadmGroupLineSubrack_Type.__name__ = "SubrackNumber"
_RoadmGroupLineSubrack_Object = MibTableColumn
roadmGroupLineSubrack = _RoadmGroupLineSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 5, 1, 1, 4),
    _RoadmGroupLineSubrack_Type()
)
roadmGroupLineSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmGroupLineSubrack.setStatus("current")


class _RoadmGroupLineSlot_Type(SlotNumber):
    """Custom type roadmGroupLineSlot based on SlotNumber"""
    defaultValue = 0


_RoadmGroupLineSlot_Type.__name__ = "SlotNumber"
_RoadmGroupLineSlot_Object = MibTableColumn
roadmGroupLineSlot = _RoadmGroupLineSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 5, 1, 1, 5),
    _RoadmGroupLineSlot_Type()
)
roadmGroupLineSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmGroupLineSlot.setStatus("current")


class _RoadmGroupLinePort_Type(PortNumber):
    """Custom type roadmGroupLinePort based on PortNumber"""
    defaultValue = 0


_RoadmGroupLinePort_Type.__name__ = "PortNumber"
_RoadmGroupLinePort_Object = MibTableColumn
roadmGroupLinePort = _RoadmGroupLinePort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 5, 1, 1, 6),
    _RoadmGroupLinePort_Type()
)
roadmGroupLinePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmGroupLinePort.setStatus("current")


class _RoadmGroupLineAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type roadmGroupLineAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_RoadmGroupLineAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_RoadmGroupLineAdminStatus_Object = MibTableColumn
roadmGroupLineAdminStatus = _RoadmGroupLineAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 5, 1, 1, 7),
    _RoadmGroupLineAdminStatus_Type()
)
roadmGroupLineAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupLineAdminStatus.setStatus("current")
_RoadmGroupLineObjectProperty_Type = ObjectProperty
_RoadmGroupLineObjectProperty_Object = MibTableColumn
roadmGroupLineObjectProperty = _RoadmGroupLineObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 5, 1, 1, 8),
    _RoadmGroupLineObjectProperty_Type()
)
roadmGroupLineObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupLineObjectProperty.setStatus("current")
_RoadmGroupLineCreateLineCommand_Type = CommandString
_RoadmGroupLineCreateLineCommand_Object = MibTableColumn
roadmGroupLineCreateLineCommand = _RoadmGroupLineCreateLineCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 5, 1, 1, 9),
    _RoadmGroupLineCreateLineCommand_Type()
)
roadmGroupLineCreateLineCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupLineCreateLineCommand.setStatus("current")
_RoadmGroupLineDeleteLineCommand_Type = CommandString
_RoadmGroupLineDeleteLineCommand_Object = MibTableColumn
roadmGroupLineDeleteLineCommand = _RoadmGroupLineDeleteLineCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 5, 1, 1, 10),
    _RoadmGroupLineDeleteLineCommand_Type()
)
roadmGroupLineDeleteLineCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupLineDeleteLineCommand.setStatus("current")


class _RoadmGroupLineNoOfLines_Type(Unsigned32):
    """Custom type roadmGroupLineNoOfLines based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_RoadmGroupLineNoOfLines_Type.__name__ = "Unsigned32"
_RoadmGroupLineNoOfLines_Object = MibTableColumn
roadmGroupLineNoOfLines = _RoadmGroupLineNoOfLines_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 5, 1, 1, 11),
    _RoadmGroupLineNoOfLines_Type()
)
roadmGroupLineNoOfLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmGroupLineNoOfLines.setStatus("current")
_RoadmLineList_ObjectIdentity = ObjectIdentity
roadmLineList = _RoadmLineList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 6)
)
_RoadmLineTable_Object = MibTable
roadmLineTable = _RoadmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 6, 1)
)
if mibBuilder.loadTexts:
    roadmLineTable.setStatus("current")
_RoadmLineEntry_Object = MibTableRow
roadmLineEntry = _RoadmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 6, 1, 1)
)
roadmLineEntry.setIndexNames(
    (0, "LUM-ROADM-MIB", "roadmLineIndex"),
)
if mibBuilder.loadTexts:
    roadmLineEntry.setStatus("current")


class _RoadmLineIndex_Type(Unsigned32):
    """Custom type roadmLineIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RoadmLineIndex_Type.__name__ = "Unsigned32"
_RoadmLineIndex_Object = MibTableColumn
roadmLineIndex = _RoadmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 6, 1, 1, 1),
    _RoadmLineIndex_Type()
)
roadmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmLineIndex.setStatus("current")


class _RoadmLineName_Type(MgmtNameString):
    """Custom type roadmLineName based on MgmtNameString"""
    defaultValue = OctetString("")


_RoadmLineName_Type.__name__ = "MgmtNameString"
_RoadmLineName_Object = MibTableColumn
roadmLineName = _RoadmLineName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 6, 1, 1, 2),
    _RoadmLineName_Type()
)
roadmLineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmLineName.setStatus("current")


class _RoadmLineDescr_Type(DisplayString):
    """Custom type roadmLineDescr based on DisplayString"""
    defaultValue = OctetString("")


_RoadmLineDescr_Type.__name__ = "DisplayString"
_RoadmLineDescr_Object = MibTableColumn
roadmLineDescr = _RoadmLineDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 6, 1, 1, 3),
    _RoadmLineDescr_Type()
)
roadmLineDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roadmLineDescr.setStatus("current")


class _RoadmLineSubrack_Type(SubrackNumber):
    """Custom type roadmLineSubrack based on SubrackNumber"""
    defaultValue = 0


_RoadmLineSubrack_Type.__name__ = "SubrackNumber"
_RoadmLineSubrack_Object = MibTableColumn
roadmLineSubrack = _RoadmLineSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 6, 1, 1, 4),
    _RoadmLineSubrack_Type()
)
roadmLineSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmLineSubrack.setStatus("current")


class _RoadmLineSlot_Type(SlotNumber):
    """Custom type roadmLineSlot based on SlotNumber"""
    defaultValue = 0


_RoadmLineSlot_Type.__name__ = "SlotNumber"
_RoadmLineSlot_Object = MibTableColumn
roadmLineSlot = _RoadmLineSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 6, 1, 1, 5),
    _RoadmLineSlot_Type()
)
roadmLineSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmLineSlot.setStatus("current")


class _RoadmLinePort_Type(PortNumber):
    """Custom type roadmLinePort based on PortNumber"""
    defaultValue = 0


_RoadmLinePort_Type.__name__ = "PortNumber"
_RoadmLinePort_Object = MibTableColumn
roadmLinePort = _RoadmLinePort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 6, 1, 1, 6),
    _RoadmLinePort_Type()
)
roadmLinePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmLinePort.setStatus("current")
_RoadmLineObjectProperty_Type = ObjectProperty
_RoadmLineObjectProperty_Object = MibTableColumn
roadmLineObjectProperty = _RoadmLineObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 6, 1, 1, 7),
    _RoadmLineObjectProperty_Type()
)
roadmLineObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmLineObjectProperty.setStatus("current")
_RoadmLineGroupId_Type = DisplayString
_RoadmLineGroupId_Object = MibTableColumn
roadmLineGroupId = _RoadmLineGroupId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 6, 1, 1, 8),
    _RoadmLineGroupId_Type()
)
roadmLineGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roadmLineGroupId.setStatus("current")
_RoadmLineFrequencyMismatch_Type = FaultStatus
_RoadmLineFrequencyMismatch_Object = MibTableColumn
roadmLineFrequencyMismatch = _RoadmLineFrequencyMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 6, 1, 1, 9),
    _RoadmLineFrequencyMismatch_Type()
)
roadmLineFrequencyMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmLineFrequencyMismatch.setStatus("current")
_RoadmLineFrequencyUsed_Type = FaultStatus
_RoadmLineFrequencyUsed_Object = MibTableColumn
roadmLineFrequencyUsed = _RoadmLineFrequencyUsed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 6, 1, 1, 10),
    _RoadmLineFrequencyUsed_Type()
)
roadmLineFrequencyUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmLineFrequencyUsed.setStatus("current")


class _RoadmLineAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type roadmLineAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_RoadmLineAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_RoadmLineAdminStatus_Object = MibTableColumn
roadmLineAdminStatus = _RoadmLineAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 6, 1, 1, 11),
    _RoadmLineAdminStatus_Type()
)
roadmLineAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roadmLineAdminStatus.setStatus("current")
_RoadmChannelList_ObjectIdentity = ObjectIdentity
roadmChannelList = _RoadmChannelList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 7)
)
_RoadmChannelTable_Object = MibTable
roadmChannelTable = _RoadmChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 7, 1)
)
if mibBuilder.loadTexts:
    roadmChannelTable.setStatus("current")
_RoadmChannelEntry_Object = MibTableRow
roadmChannelEntry = _RoadmChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 7, 1, 1)
)
roadmChannelEntry.setIndexNames(
    (0, "LUM-ROADM-MIB", "roadmChannelIndex"),
)
if mibBuilder.loadTexts:
    roadmChannelEntry.setStatus("current")


class _RoadmChannelIndex_Type(Unsigned32):
    """Custom type roadmChannelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RoadmChannelIndex_Type.__name__ = "Unsigned32"
_RoadmChannelIndex_Object = MibTableColumn
roadmChannelIndex = _RoadmChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 7, 1, 1, 1),
    _RoadmChannelIndex_Type()
)
roadmChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmChannelIndex.setStatus("current")


class _RoadmChannelName_Type(MgmtNameString):
    """Custom type roadmChannelName based on MgmtNameString"""
    defaultValue = OctetString("")


_RoadmChannelName_Type.__name__ = "MgmtNameString"
_RoadmChannelName_Object = MibTableColumn
roadmChannelName = _RoadmChannelName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 7, 1, 1, 2),
    _RoadmChannelName_Type()
)
roadmChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmChannelName.setStatus("current")


class _RoadmChannelFrequency_Type(LambdaFrequency):
    """Custom type roadmChannelFrequency based on LambdaFrequency"""
    defaultValue = 0


_RoadmChannelFrequency_Type.__name__ = "LambdaFrequency"
_RoadmChannelFrequency_Object = MibTableColumn
roadmChannelFrequency = _RoadmChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 7, 1, 1, 3),
    _RoadmChannelFrequency_Type()
)
roadmChannelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmChannelFrequency.setStatus("current")


class _RoadmChannelRoadmLineIfIndex_Type(Unsigned32):
    """Custom type roadmChannelRoadmLineIfIndex based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RoadmChannelRoadmLineIfIndex_Type.__name__ = "Unsigned32"
_RoadmChannelRoadmLineIfIndex_Object = MibTableColumn
roadmChannelRoadmLineIfIndex = _RoadmChannelRoadmLineIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 7, 1, 1, 4),
    _RoadmChannelRoadmLineIfIndex_Type()
)
roadmChannelRoadmLineIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmChannelRoadmLineIfIndex.setStatus("current")


class _RoadmChannelRoadmAddDropIfIndex_Type(Unsigned32):
    """Custom type roadmChannelRoadmAddDropIfIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RoadmChannelRoadmAddDropIfIndex_Type.__name__ = "Unsigned32"
_RoadmChannelRoadmAddDropIfIndex_Object = MibTableColumn
roadmChannelRoadmAddDropIfIndex = _RoadmChannelRoadmAddDropIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 7, 1, 1, 5),
    _RoadmChannelRoadmAddDropIfIndex_Type()
)
roadmChannelRoadmAddDropIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmChannelRoadmAddDropIfIndex.setStatus("current")


class _RoadmChannelAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type roadmChannelAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_RoadmChannelAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_RoadmChannelAdminStatus_Object = MibTableColumn
roadmChannelAdminStatus = _RoadmChannelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 7, 1, 1, 6),
    _RoadmChannelAdminStatus_Type()
)
roadmChannelAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roadmChannelAdminStatus.setStatus("current")


class _RoadmChannelOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type roadmChannelOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_RoadmChannelOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_RoadmChannelOperStatus_Object = MibTableColumn
roadmChannelOperStatus = _RoadmChannelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 7, 1, 1, 7),
    _RoadmChannelOperStatus_Type()
)
roadmChannelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmChannelOperStatus.setStatus("current")


class _RoadmChannelAttenuation_Type(Unsigned32):
    """Custom type roadmChannelAttenuation based on Unsigned32"""
    defaultValue = 150

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_RoadmChannelAttenuation_Type.__name__ = "Unsigned32"
_RoadmChannelAttenuation_Object = MibTableColumn
roadmChannelAttenuation = _RoadmChannelAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 7, 1, 1, 8),
    _RoadmChannelAttenuation_Type()
)
roadmChannelAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roadmChannelAttenuation.setStatus("current")


class _RoadmChannelConnectedToInterface_Type(DisplayString):
    """Custom type roadmChannelConnectedToInterface based on DisplayString"""
    defaultValue = OctetString("")


_RoadmChannelConnectedToInterface_Type.__name__ = "DisplayString"
_RoadmChannelConnectedToInterface_Object = MibTableColumn
roadmChannelConnectedToInterface = _RoadmChannelConnectedToInterface_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 7, 1, 1, 9),
    _RoadmChannelConnectedToInterface_Type()
)
roadmChannelConnectedToInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmChannelConnectedToInterface.setStatus("current")
_RoadmChannelConnectDisconnectCommand_Type = CommandString
_RoadmChannelConnectDisconnectCommand_Object = MibTableColumn
roadmChannelConnectDisconnectCommand = _RoadmChannelConnectDisconnectCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 2, 7, 1, 1, 10),
    _RoadmChannelConnectDisconnectCommand_Type()
)
roadmChannelConnectDisconnectCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roadmChannelConnectDisconnectCommand.setStatus("current")

# Managed Objects groups

roadmGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 1, 1)
)
roadmGeneralGroup.setObjects(
      *(("LUM-ROADM-MIB", "roadmGeneralConfigLastChangeTime"),
        ("LUM-ROADM-MIB", "roadmGeneralStateLastChangeTime"),
        ("LUM-ROADM-MIB", "roadmGeneralRoadmLineIfTableSize"),
        ("LUM-ROADM-MIB", "roadmGeneralRoadmAddDropIfTableSize"))
)
if mibBuilder.loadTexts:
    roadmGeneralGroup.setStatus("deprecated")

roadmAddDropIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 1, 2)
)
roadmAddDropIfGroup.setObjects(
      *(("LUM-ROADM-MIB", "roadmAddDropIfIndex"),
        ("LUM-ROADM-MIB", "roadmAddDropIfName"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDescr"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDescr2"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSubrack"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSlot"),
        ("LUM-ROADM-MIB", "roadmAddDropIfTxPort"),
        ("LUM-ROADM-MIB", "roadmAddDropIfRxPort"),
        ("LUM-ROADM-MIB", "roadmAddDropIfInvPhysIndexOrZero"),
        ("LUM-ROADM-MIB", "roadmAddDropIfAdminStatus"),
        ("LUM-ROADM-MIB", "roadmAddDropIfOperStatus"),
        ("LUM-ROADM-MIB", "roadmAddDropIfTemperature"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDropFrequencyMin"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDropFrequencyMax"),
        ("LUM-ROADM-MIB", "roadmAddDropIfObjectProperty"),
        ("LUM-ROADM-MIB", "roadmAddDropIfConfigurationCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfModuleFailure"),
        ("LUM-ROADM-MIB", "roadmAddDropIfTxSignalStatus"),
        ("LUM-ROADM-MIB", "roadmAddDropIfMode"))
)
if mibBuilder.loadTexts:
    roadmAddDropIfGroup.setStatus("deprecated")

roadmLineIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 1, 3)
)
roadmLineIfGroup.setObjects(
      *(("LUM-ROADM-MIB", "roadmLineIfIndex"),
        ("LUM-ROADM-MIB", "roadmLineIfName"),
        ("LUM-ROADM-MIB", "roadmLineIfDescr"),
        ("LUM-ROADM-MIB", "roadmLineIfSubrack"),
        ("LUM-ROADM-MIB", "roadmLineIfSlot"),
        ("LUM-ROADM-MIB", "roadmLineIfTxPort"),
        ("LUM-ROADM-MIB", "roadmLineIfRxPort"),
        ("LUM-ROADM-MIB", "roadmLineIfInvPhysIndexOrZero"),
        ("LUM-ROADM-MIB", "roadmLineIfAdminStatus"),
        ("LUM-ROADM-MIB", "roadmLineIfOperStatus"),
        ("LUM-ROADM-MIB", "roadmLineIfObjectProperty"),
        ("LUM-ROADM-MIB", "roadmLineIfTxSignalStatus"))
)
if mibBuilder.loadTexts:
    roadmLineIfGroup.setStatus("deprecated")

roadmAddDropIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 1, 4)
)
roadmAddDropIfGroupV2.setObjects(
      *(("LUM-ROADM-MIB", "roadmAddDropIfIndex"),
        ("LUM-ROADM-MIB", "roadmAddDropIfName"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDescr"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDescr2"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSubrack"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSlot"),
        ("LUM-ROADM-MIB", "roadmAddDropIfTxPort"),
        ("LUM-ROADM-MIB", "roadmAddDropIfRxPort"),
        ("LUM-ROADM-MIB", "roadmAddDropIfInvPhysIndexOrZero"),
        ("LUM-ROADM-MIB", "roadmAddDropIfAdminStatus"),
        ("LUM-ROADM-MIB", "roadmAddDropIfOperStatus"),
        ("LUM-ROADM-MIB", "roadmAddDropIfTemperature"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDropFrequencyMin"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDropFrequencyMax"),
        ("LUM-ROADM-MIB", "roadmAddDropIfObjectProperty"),
        ("LUM-ROADM-MIB", "roadmAddDropIfConfigurationCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfModuleFailure"),
        ("LUM-ROADM-MIB", "roadmAddDropIfTxSignalStatus"),
        ("LUM-ROADM-MIB", "roadmAddDropIfMode"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSpacingMode"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGuardChannel1"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGuardChannel2"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDropFrequencyLimitMin"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDropFrequencyLimitMax"),
        ("LUM-ROADM-MIB", "roadmAddDropIfLimitConfigurationCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGroupRoadmMode"),
        ("LUM-ROADM-MIB", "roadmAddDropIfPasswd"),
        ("LUM-ROADM-MIB", "roadmAddDropIfPasswdConfig"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGroupLineMode"))
)
if mibBuilder.loadTexts:
    roadmAddDropIfGroupV2.setStatus("deprecated")

roadmGroupRoadmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 1, 5)
)
roadmGroupRoadmGroup.setObjects(
      *(("LUM-ROADM-MIB", "roadmGroupRoadmIndex"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmName"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDescr"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmRightSubrack"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmRightSlot"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmRightPort"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmLeftSubrack"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmLeftSlot"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmLeftPort"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmAdminStatus"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmObjectProperty"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataAdminStatus"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataDropFrequencyMin"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataDropFrequencyMax"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataDropFrequencyLimitMin"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataDropFrequencyLimitMax"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataMode"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataSpacingMode"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmConfigurationCommand"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmLimitConfigurationCommand"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmPasswd"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmPasswdConfig"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataGuardChannel1"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataGuardChannel2"))
)
if mibBuilder.loadTexts:
    roadmGroupRoadmGroup.setStatus("deprecated")

roadmGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 1, 6)
)
roadmGeneralGroupV2.setObjects(
      *(("LUM-ROADM-MIB", "roadmGeneralConfigLastChangeTime"),
        ("LUM-ROADM-MIB", "roadmGeneralStateLastChangeTime"),
        ("LUM-ROADM-MIB", "roadmGeneralRoadmLineIfTableSize"),
        ("LUM-ROADM-MIB", "roadmGeneralRoadmAddDropIfTableSize"),
        ("LUM-ROADM-MIB", "roadmGeneralRoadmGroupRoadmTableSize"),
        ("LUM-ROADM-MIB", "roadmGeneralRoadmGroupLineTableSize"),
        ("LUM-ROADM-MIB", "roadmGeneralRoadmLineTableSize"))
)
if mibBuilder.loadTexts:
    roadmGeneralGroupV2.setStatus("deprecated")

roadmGroupLineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 1, 7)
)
roadmGroupLineGroup.setObjects(
      *(("LUM-ROADM-MIB", "roadmGroupLineIndex"),
        ("LUM-ROADM-MIB", "roadmGroupLineName"),
        ("LUM-ROADM-MIB", "roadmGroupLineDescr"),
        ("LUM-ROADM-MIB", "roadmGroupLineSubrack"),
        ("LUM-ROADM-MIB", "roadmGroupLineSlot"),
        ("LUM-ROADM-MIB", "roadmGroupLinePort"),
        ("LUM-ROADM-MIB", "roadmGroupLineAdminStatus"),
        ("LUM-ROADM-MIB", "roadmGroupLineObjectProperty"),
        ("LUM-ROADM-MIB", "roadmGroupLineCreateLineCommand"),
        ("LUM-ROADM-MIB", "roadmGroupLineDeleteLineCommand"),
        ("LUM-ROADM-MIB", "roadmGroupLineNoOfLines"))
)
if mibBuilder.loadTexts:
    roadmGroupLineGroup.setStatus("current")

roadmLineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 1, 8)
)
roadmLineGroup.setObjects(
      *(("LUM-ROADM-MIB", "roadmLineIndex"),
        ("LUM-ROADM-MIB", "roadmLineName"),
        ("LUM-ROADM-MIB", "roadmLineDescr"),
        ("LUM-ROADM-MIB", "roadmLineSubrack"),
        ("LUM-ROADM-MIB", "roadmLineSlot"),
        ("LUM-ROADM-MIB", "roadmLinePort"),
        ("LUM-ROADM-MIB", "roadmLineObjectProperty"),
        ("LUM-ROADM-MIB", "roadmLineGroupId"),
        ("LUM-ROADM-MIB", "roadmLineFrequencyMismatch"),
        ("LUM-ROADM-MIB", "roadmLineFrequencyUsed"),
        ("LUM-ROADM-MIB", "roadmLineAdminStatus"))
)
if mibBuilder.loadTexts:
    roadmLineGroup.setStatus("current")

roadmChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 1, 9)
)
roadmChannelGroup.setObjects(
      *(("LUM-ROADM-MIB", "roadmChannelIndex"),
        ("LUM-ROADM-MIB", "roadmChannelName"),
        ("LUM-ROADM-MIB", "roadmChannelFrequency"),
        ("LUM-ROADM-MIB", "roadmChannelRoadmLineIfIndex"),
        ("LUM-ROADM-MIB", "roadmChannelRoadmAddDropIfIndex"),
        ("LUM-ROADM-MIB", "roadmChannelAdminStatus"),
        ("LUM-ROADM-MIB", "roadmChannelOperStatus"),
        ("LUM-ROADM-MIB", "roadmChannelAttenuation"),
        ("LUM-ROADM-MIB", "roadmChannelConnectedToInterface"),
        ("LUM-ROADM-MIB", "roadmChannelConnectDisconnectCommand"))
)
if mibBuilder.loadTexts:
    roadmChannelGroup.setStatus("current")

roadmAddDropIfGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 1, 10)
)
roadmAddDropIfGroupV3.setObjects(
      *(("LUM-ROADM-MIB", "roadmAddDropIfIndex"),
        ("LUM-ROADM-MIB", "roadmAddDropIfName"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDescr"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDescr2"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSubrack"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSlot"),
        ("LUM-ROADM-MIB", "roadmAddDropIfTxPort"),
        ("LUM-ROADM-MIB", "roadmAddDropIfRxPort"),
        ("LUM-ROADM-MIB", "roadmAddDropIfInvPhysIndexOrZero"),
        ("LUM-ROADM-MIB", "roadmAddDropIfAdminStatus"),
        ("LUM-ROADM-MIB", "roadmAddDropIfOperStatus"),
        ("LUM-ROADM-MIB", "roadmAddDropIfTemperature"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDropFrequencyMin"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDropFrequencyMax"),
        ("LUM-ROADM-MIB", "roadmAddDropIfObjectProperty"),
        ("LUM-ROADM-MIB", "roadmAddDropIfConfigurationCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfModuleFailure"),
        ("LUM-ROADM-MIB", "roadmAddDropIfTxSignalStatus"),
        ("LUM-ROADM-MIB", "roadmAddDropIfMode"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSpacingMode"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGuardChannel1"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGuardChannel2"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDropFrequencyLimitMin"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDropFrequencyLimitMax"),
        ("LUM-ROADM-MIB", "roadmAddDropIfLimitConfigurationCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGroupRoadmMode"),
        ("LUM-ROADM-MIB", "roadmAddDropIfPasswd"),
        ("LUM-ROADM-MIB", "roadmAddDropIfPasswdConfig"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGroupLineMode"),
        ("LUM-ROADM-MIB", "roadmAddDropIfNoOfConnectedChannels"),
        ("LUM-ROADM-MIB", "roadmAddDropIfViewChannelList"),
        ("LUM-ROADM-MIB", "roadmAddDropIfConnectedChannelMask"),
        ("LUM-ROADM-MIB", "roadmAddDropIfAddChannelCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfUnlinkChannelCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfUnlinkAllChannelsCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSetAttenuationCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfAdjustAttenuationDeltaCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfConnectChannelCmd"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDisconnectChannelCmd"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGroupIndex"))
)
if mibBuilder.loadTexts:
    roadmAddDropIfGroupV3.setStatus("deprecated")

roadmLineIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 1, 11)
)
roadmLineIfGroupV2.setObjects(
      *(("LUM-ROADM-MIB", "roadmLineIfIndex"),
        ("LUM-ROADM-MIB", "roadmLineIfName"),
        ("LUM-ROADM-MIB", "roadmLineIfDescr"),
        ("LUM-ROADM-MIB", "roadmLineIfSubrack"),
        ("LUM-ROADM-MIB", "roadmLineIfSlot"),
        ("LUM-ROADM-MIB", "roadmLineIfTxPort"),
        ("LUM-ROADM-MIB", "roadmLineIfRxPort"),
        ("LUM-ROADM-MIB", "roadmLineIfInvPhysIndexOrZero"),
        ("LUM-ROADM-MIB", "roadmLineIfAdminStatus"),
        ("LUM-ROADM-MIB", "roadmLineIfOperStatus"),
        ("LUM-ROADM-MIB", "roadmLineIfObjectProperty"),
        ("LUM-ROADM-MIB", "roadmLineIfTxSignalStatus"),
        ("LUM-ROADM-MIB", "roadmLineIfNoOfConnectedChannels"),
        ("LUM-ROADM-MIB", "roadmLineIfViewChannelList"),
        ("LUM-ROADM-MIB", "roadmLineIfSetAttenuationCommand"),
        ("LUM-ROADM-MIB", "roadmLineIfAdjustAttenuationDeltaCommand"),
        ("LUM-ROADM-MIB", "roadmLineIfMonitorInsertionLoss"))
)
if mibBuilder.loadTexts:
    roadmLineIfGroupV2.setStatus("deprecated")

roadmGroupRoadmGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 1, 12)
)
roadmGroupRoadmGroupV2.setObjects(
      *(("LUM-ROADM-MIB", "roadmGroupRoadmIndex"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmName"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDescr"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmRightSubrack"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmRightSlot"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmRightPort"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmLeftSubrack"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmLeftSlot"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmLeftPort"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmAdminStatus"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmObjectProperty"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataAdminStatus"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataDropFrequencyMin"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataDropFrequencyMax"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataDropFrequencyLimitMin"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataDropFrequencyLimitMax"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataMode"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataSpacingMode"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmConfigurationCommand"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmLimitConfigurationCommand"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmPasswd"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmPasswdConfig"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataGuardChannel1"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataGuardChannel2"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmNoOfConnectedChannels"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmViewChannelList"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmConnectedChannelMask"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmAddChannelCommand"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmUnlinkChannelCommand"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmUnlinkAllChannelsCommand"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmConnectChannelCmd"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDisconnectChannelCmd"))
)
if mibBuilder.loadTexts:
    roadmGroupRoadmGroupV2.setStatus("deprecated")

roadmGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 1, 13)
)
roadmGeneralGroupV3.setObjects(
      *(("LUM-ROADM-MIB", "roadmGeneralConfigLastChangeTime"),
        ("LUM-ROADM-MIB", "roadmGeneralStateLastChangeTime"),
        ("LUM-ROADM-MIB", "roadmGeneralRoadmLineIfTableSize"),
        ("LUM-ROADM-MIB", "roadmGeneralRoadmAddDropIfTableSize"),
        ("LUM-ROADM-MIB", "roadmGeneralRoadmGroupRoadmTableSize"),
        ("LUM-ROADM-MIB", "roadmGeneralRoadmGroupLineTableSize"),
        ("LUM-ROADM-MIB", "roadmGeneralRoadmLineTableSize"),
        ("LUM-ROADM-MIB", "roadmGeneralChannelTableSize"))
)
if mibBuilder.loadTexts:
    roadmGeneralGroupV3.setStatus("current")

roadmAddDropIfGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 1, 14)
)
roadmAddDropIfGroupV4.setObjects(
      *(("LUM-ROADM-MIB", "roadmAddDropIfIndex"),
        ("LUM-ROADM-MIB", "roadmAddDropIfName"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDescr"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDescr2"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSubrack"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSlot"),
        ("LUM-ROADM-MIB", "roadmAddDropIfTxPort"),
        ("LUM-ROADM-MIB", "roadmAddDropIfRxPort"),
        ("LUM-ROADM-MIB", "roadmAddDropIfInvPhysIndexOrZero"),
        ("LUM-ROADM-MIB", "roadmAddDropIfAdminStatus"),
        ("LUM-ROADM-MIB", "roadmAddDropIfOperStatus"),
        ("LUM-ROADM-MIB", "roadmAddDropIfTemperature"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDropFrequencyMin"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDropFrequencyMax"),
        ("LUM-ROADM-MIB", "roadmAddDropIfObjectProperty"),
        ("LUM-ROADM-MIB", "roadmAddDropIfConfigurationCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfModuleFailure"),
        ("LUM-ROADM-MIB", "roadmAddDropIfTxSignalStatus"),
        ("LUM-ROADM-MIB", "roadmAddDropIfMode"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSpacingMode"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGuardChannel1"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGuardChannel2"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDropFrequencyLimitMin"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDropFrequencyLimitMax"),
        ("LUM-ROADM-MIB", "roadmAddDropIfLimitConfigurationCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGroupRoadmMode"),
        ("LUM-ROADM-MIB", "roadmAddDropIfPasswd"),
        ("LUM-ROADM-MIB", "roadmAddDropIfPasswdConfig"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGroupLineMode"),
        ("LUM-ROADM-MIB", "roadmAddDropIfNoOfConnectedChannels"),
        ("LUM-ROADM-MIB", "roadmAddDropIfViewChannelList"),
        ("LUM-ROADM-MIB", "roadmAddDropIfConnectedChannelMask"),
        ("LUM-ROADM-MIB", "roadmAddDropIfAddChannelCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfUnlinkChannelCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfUnlinkAllChannelsCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSetAttenuationCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfAdjustAttenuationDeltaCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfConnectChannelCmd"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDisconnectChannelCmd"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGroupIndex"),
        ("LUM-ROADM-MIB", "roadmAddDropIfAddAllChannelCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSetAdminStatusCommand"))
)
if mibBuilder.loadTexts:
    roadmAddDropIfGroupV4.setStatus("deprecated")

roadmGroupRoadmGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 1, 15)
)
roadmGroupRoadmGroupV3.setObjects(
      *(("LUM-ROADM-MIB", "roadmGroupRoadmIndex"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmName"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDescr"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmRightSubrack"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmRightSlot"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmRightPort"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmLeftSubrack"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmLeftSlot"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmLeftPort"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmAdminStatus"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmObjectProperty"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataAdminStatus"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataDropFrequencyMin"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataDropFrequencyMax"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataDropFrequencyLimitMin"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataDropFrequencyLimitMax"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataMode"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataSpacingMode"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmConfigurationCommand"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmLimitConfigurationCommand"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmPasswd"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmPasswdConfig"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataGuardChannel1"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDataGuardChannel2"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmNoOfConnectedChannels"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmViewChannelList"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmConnectedChannelMask"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmAddChannelCommand"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmUnlinkChannelCommand"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmUnlinkAllChannelsCommand"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmConnectChannelCmd"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmDisconnectChannelCmd"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmAddChannelCommand"))
)
if mibBuilder.loadTexts:
    roadmGroupRoadmGroupV3.setStatus("current")

roadmLineIfGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 1, 16)
)
roadmLineIfGroupV3.setObjects(
      *(("LUM-ROADM-MIB", "roadmLineIfIndex"),
        ("LUM-ROADM-MIB", "roadmLineIfName"),
        ("LUM-ROADM-MIB", "roadmLineIfDescr"),
        ("LUM-ROADM-MIB", "roadmLineIfSubrack"),
        ("LUM-ROADM-MIB", "roadmLineIfSlot"),
        ("LUM-ROADM-MIB", "roadmLineIfTxPort"),
        ("LUM-ROADM-MIB", "roadmLineIfRxPort"),
        ("LUM-ROADM-MIB", "roadmLineIfInvPhysIndexOrZero"),
        ("LUM-ROADM-MIB", "roadmLineIfAdminStatus"),
        ("LUM-ROADM-MIB", "roadmLineIfOperStatus"),
        ("LUM-ROADM-MIB", "roadmLineIfObjectProperty"),
        ("LUM-ROADM-MIB", "roadmLineIfTxSignalStatus"),
        ("LUM-ROADM-MIB", "roadmLineIfNoOfConnectedChannels"),
        ("LUM-ROADM-MIB", "roadmLineIfViewChannelList"),
        ("LUM-ROADM-MIB", "roadmLineIfSetAttenuationCommand"),
        ("LUM-ROADM-MIB", "roadmLineIfAdjustAttenuationDeltaCommand"),
        ("LUM-ROADM-MIB", "roadmLineIfMonitorInsertionLoss"),
        ("LUM-ROADM-MIB", "roadmLineIfSetAdminStatusCommand"))
)
if mibBuilder.loadTexts:
    roadmLineIfGroupV3.setStatus("current")

roadmAddDropIfGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 1, 17)
)
roadmAddDropIfGroupV5.setObjects(
      *(("LUM-ROADM-MIB", "roadmAddDropIfIndex"),
        ("LUM-ROADM-MIB", "roadmAddDropIfName"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDescr"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDescr2"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSubrack"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSlot"),
        ("LUM-ROADM-MIB", "roadmAddDropIfTxPort"),
        ("LUM-ROADM-MIB", "roadmAddDropIfRxPort"),
        ("LUM-ROADM-MIB", "roadmAddDropIfInvPhysIndexOrZero"),
        ("LUM-ROADM-MIB", "roadmAddDropIfAdminStatus"),
        ("LUM-ROADM-MIB", "roadmAddDropIfOperStatus"),
        ("LUM-ROADM-MIB", "roadmAddDropIfTemperature"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDropFrequencyMin"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDropFrequencyMax"),
        ("LUM-ROADM-MIB", "roadmAddDropIfObjectProperty"),
        ("LUM-ROADM-MIB", "roadmAddDropIfConfigurationCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfModuleFailure"),
        ("LUM-ROADM-MIB", "roadmAddDropIfTxSignalStatus"),
        ("LUM-ROADM-MIB", "roadmAddDropIfMode"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSpacingMode"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGuardChannel1"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGuardChannel2"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDropFrequencyLimitMin"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDropFrequencyLimitMax"),
        ("LUM-ROADM-MIB", "roadmAddDropIfLimitConfigurationCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGroupRoadmMode"),
        ("LUM-ROADM-MIB", "roadmAddDropIfPasswd"),
        ("LUM-ROADM-MIB", "roadmAddDropIfPasswdConfig"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGroupLineMode"),
        ("LUM-ROADM-MIB", "roadmAddDropIfNoOfConnectedChannels"),
        ("LUM-ROADM-MIB", "roadmAddDropIfViewChannelList"),
        ("LUM-ROADM-MIB", "roadmAddDropIfConnectedChannelMask"),
        ("LUM-ROADM-MIB", "roadmAddDropIfAddChannelCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfUnlinkChannelCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfUnlinkAllChannelsCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSetAttenuationCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfAdjustAttenuationDeltaCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfConnectChannelCmd"),
        ("LUM-ROADM-MIB", "roadmAddDropIfDisconnectChannelCmd"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGroupIndex"),
        ("LUM-ROADM-MIB", "roadmAddDropIfAddAllChannelCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSetAdminStatusCommand"),
        ("LUM-ROADM-MIB", "roadmAddDropIfSpacingHwCapability"))
)
if mibBuilder.loadTexts:
    roadmAddDropIfGroupV5.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumRoadmBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 2, 1)
)
lumRoadmBasicComplV1.setObjects(
      *(("LUM-ROADM-MIB", "roadmGeneralGroup"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGroup"),
        ("LUM-ROADM-MIB", "roadmLineIfGroup"))
)
if mibBuilder.loadTexts:
    lumRoadmBasicComplV1.setStatus(
        "deprecated"
    )

lumRoadmBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 2, 2)
)
lumRoadmBasicComplV2.setObjects(
      *(("LUM-ROADM-MIB", "roadmGeneralGroupV2"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGroupV2"),
        ("LUM-ROADM-MIB", "roadmLineIfGroup"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmGroup"),
        ("LUM-ROADM-MIB", "roadmGroupLineGroup"),
        ("LUM-ROADM-MIB", "roadmLineGroup"))
)
if mibBuilder.loadTexts:
    lumRoadmBasicComplV2.setStatus(
        "deprecated"
    )

lumRoadmBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 2, 3)
)
lumRoadmBasicComplV3.setObjects(
      *(("LUM-ROADM-MIB", "roadmGeneralGroupV3"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGroupV3"),
        ("LUM-ROADM-MIB", "roadmLineIfGroupV2"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmGroup"),
        ("LUM-ROADM-MIB", "roadmGroupLineGroup"),
        ("LUM-ROADM-MIB", "roadmLineGroup"),
        ("LUM-ROADM-MIB", "roadmChannelGroup"))
)
if mibBuilder.loadTexts:
    lumRoadmBasicComplV3.setStatus(
        "deprecated"
    )

lumRoadmBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 2, 4)
)
lumRoadmBasicComplV4.setObjects(
      *(("LUM-ROADM-MIB", "roadmGeneralGroupV3"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGroupV3"),
        ("LUM-ROADM-MIB", "roadmLineIfGroupV2"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmGroup"),
        ("LUM-ROADM-MIB", "roadmGroupLineGroup"),
        ("LUM-ROADM-MIB", "roadmLineGroup"),
        ("LUM-ROADM-MIB", "roadmChannelGroup"))
)
if mibBuilder.loadTexts:
    lumRoadmBasicComplV4.setStatus(
        "deprecated"
    )

lumRoadmBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 2, 5)
)
lumRoadmBasicComplV5.setObjects(
      *(("LUM-ROADM-MIB", "roadmGeneralGroupV3"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGroupV3"),
        ("LUM-ROADM-MIB", "roadmLineIfGroupV2"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmGroup"),
        ("LUM-ROADM-MIB", "roadmGroupLineGroup"),
        ("LUM-ROADM-MIB", "roadmLineGroup"),
        ("LUM-ROADM-MIB", "roadmChannelGroup"))
)
if mibBuilder.loadTexts:
    lumRoadmBasicComplV5.setStatus(
        "deprecated"
    )

lumRoadmBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 2, 6)
)
lumRoadmBasicComplV6.setObjects(
      *(("LUM-ROADM-MIB", "roadmGeneralGroupV3"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGroupV4"),
        ("LUM-ROADM-MIB", "roadmLineIfGroupV3"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmGroupV3"),
        ("LUM-ROADM-MIB", "roadmGroupLineGroup"),
        ("LUM-ROADM-MIB", "roadmLineGroup"),
        ("LUM-ROADM-MIB", "roadmChannelGroup"))
)
if mibBuilder.loadTexts:
    lumRoadmBasicComplV6.setStatus(
        "deprecated"
    )

lumRoadmBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31, 1, 2, 7)
)
lumRoadmBasicComplV7.setObjects(
      *(("LUM-ROADM-MIB", "roadmGeneralGroupV3"),
        ("LUM-ROADM-MIB", "roadmAddDropIfGroupV5"),
        ("LUM-ROADM-MIB", "roadmLineIfGroupV3"),
        ("LUM-ROADM-MIB", "roadmGroupRoadmGroupV3"),
        ("LUM-ROADM-MIB", "roadmGroupLineGroup"),
        ("LUM-ROADM-MIB", "roadmLineGroup"),
        ("LUM-ROADM-MIB", "roadmChannelGroup"))
)
if mibBuilder.loadTexts:
    lumRoadmBasicComplV7.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-ROADM-MIB",
    **{"lumRoadmMIBModule": lumRoadmMIBModule,
       "lumRoadmConfs": lumRoadmConfs,
       "lumRoadmGroups": lumRoadmGroups,
       "roadmGeneralGroup": roadmGeneralGroup,
       "roadmAddDropIfGroup": roadmAddDropIfGroup,
       "roadmLineIfGroup": roadmLineIfGroup,
       "roadmAddDropIfGroupV2": roadmAddDropIfGroupV2,
       "roadmGroupRoadmGroup": roadmGroupRoadmGroup,
       "roadmGeneralGroupV2": roadmGeneralGroupV2,
       "roadmGroupLineGroup": roadmGroupLineGroup,
       "roadmLineGroup": roadmLineGroup,
       "roadmChannelGroup": roadmChannelGroup,
       "roadmAddDropIfGroupV3": roadmAddDropIfGroupV3,
       "roadmLineIfGroupV2": roadmLineIfGroupV2,
       "roadmGroupRoadmGroupV2": roadmGroupRoadmGroupV2,
       "roadmGeneralGroupV3": roadmGeneralGroupV3,
       "roadmAddDropIfGroupV4": roadmAddDropIfGroupV4,
       "roadmGroupRoadmGroupV3": roadmGroupRoadmGroupV3,
       "roadmLineIfGroupV3": roadmLineIfGroupV3,
       "roadmAddDropIfGroupV5": roadmAddDropIfGroupV5,
       "lumRoadmCompl": lumRoadmCompl,
       "lumRoadmBasicComplV1": lumRoadmBasicComplV1,
       "lumRoadmBasicComplV2": lumRoadmBasicComplV2,
       "lumRoadmBasicComplV3": lumRoadmBasicComplV3,
       "lumRoadmBasicComplV4": lumRoadmBasicComplV4,
       "lumRoadmBasicComplV5": lumRoadmBasicComplV5,
       "lumRoadmBasicComplV6": lumRoadmBasicComplV6,
       "lumRoadmBasicComplV7": lumRoadmBasicComplV7,
       "lumRoadmMinimalGroups": lumRoadmMinimalGroups,
       "lumRoadmMinimalCompl": lumRoadmMinimalCompl,
       "lumRoadmMIBObjects": lumRoadmMIBObjects,
       "roadmGeneral": roadmGeneral,
       "roadmGeneralConfigLastChangeTime": roadmGeneralConfigLastChangeTime,
       "roadmGeneralStateLastChangeTime": roadmGeneralStateLastChangeTime,
       "roadmGeneralRoadmAddDropIfTableSize": roadmGeneralRoadmAddDropIfTableSize,
       "roadmGeneralRoadmLineIfTableSize": roadmGeneralRoadmLineIfTableSize,
       "roadmGeneralRoadmGroupRoadmTableSize": roadmGeneralRoadmGroupRoadmTableSize,
       "roadmGeneralRoadmGroupLineTableSize": roadmGeneralRoadmGroupLineTableSize,
       "roadmGeneralRoadmLineTableSize": roadmGeneralRoadmLineTableSize,
       "roadmGeneralChannelTableSize": roadmGeneralChannelTableSize,
       "roadmAddDropIfList": roadmAddDropIfList,
       "roadmAddDropIfTable": roadmAddDropIfTable,
       "roadmAddDropIfEntry": roadmAddDropIfEntry,
       "roadmAddDropIfIndex": roadmAddDropIfIndex,
       "roadmAddDropIfName": roadmAddDropIfName,
       "roadmAddDropIfDescr": roadmAddDropIfDescr,
       "roadmAddDropIfSubrack": roadmAddDropIfSubrack,
       "roadmAddDropIfSlot": roadmAddDropIfSlot,
       "roadmAddDropIfTxPort": roadmAddDropIfTxPort,
       "roadmAddDropIfRxPort": roadmAddDropIfRxPort,
       "roadmAddDropIfInvPhysIndexOrZero": roadmAddDropIfInvPhysIndexOrZero,
       "roadmAddDropIfAdminStatus": roadmAddDropIfAdminStatus,
       "roadmAddDropIfOperStatus": roadmAddDropIfOperStatus,
       "roadmAddDropIfTemperature": roadmAddDropIfTemperature,
       "roadmAddDropIfDropFrequencyMin": roadmAddDropIfDropFrequencyMin,
       "roadmAddDropIfDropFrequencyMax": roadmAddDropIfDropFrequencyMax,
       "roadmAddDropIfObjectProperty": roadmAddDropIfObjectProperty,
       "roadmAddDropIfConfigurationCommand": roadmAddDropIfConfigurationCommand,
       "roadmAddDropIfModuleFailure": roadmAddDropIfModuleFailure,
       "roadmAddDropIfTxSignalStatus": roadmAddDropIfTxSignalStatus,
       "roadmAddDropIfMode": roadmAddDropIfMode,
       "roadmAddDropIfDescr2": roadmAddDropIfDescr2,
       "roadmAddDropIfSpacingMode": roadmAddDropIfSpacingMode,
       "roadmAddDropIfGuardChannel1": roadmAddDropIfGuardChannel1,
       "roadmAddDropIfGuardChannel2": roadmAddDropIfGuardChannel2,
       "roadmAddDropIfDropFrequencyLimitMin": roadmAddDropIfDropFrequencyLimitMin,
       "roadmAddDropIfDropFrequencyLimitMax": roadmAddDropIfDropFrequencyLimitMax,
       "roadmAddDropIfLimitConfigurationCommand": roadmAddDropIfLimitConfigurationCommand,
       "roadmAddDropIfGroupRoadmMode": roadmAddDropIfGroupRoadmMode,
       "roadmAddDropIfPasswd": roadmAddDropIfPasswd,
       "roadmAddDropIfPasswdConfig": roadmAddDropIfPasswdConfig,
       "roadmAddDropIfGroupLineMode": roadmAddDropIfGroupLineMode,
       "roadmAddDropIfNoOfConnectedChannels": roadmAddDropIfNoOfConnectedChannels,
       "roadmAddDropIfViewChannelList": roadmAddDropIfViewChannelList,
       "roadmAddDropIfConnectedChannelMask": roadmAddDropIfConnectedChannelMask,
       "roadmAddDropIfAddChannelCommand": roadmAddDropIfAddChannelCommand,
       "roadmAddDropIfUnlinkChannelCommand": roadmAddDropIfUnlinkChannelCommand,
       "roadmAddDropIfUnlinkAllChannelsCommand": roadmAddDropIfUnlinkAllChannelsCommand,
       "roadmAddDropIfSetAttenuationCommand": roadmAddDropIfSetAttenuationCommand,
       "roadmAddDropIfAdjustAttenuationDeltaCommand": roadmAddDropIfAdjustAttenuationDeltaCommand,
       "roadmAddDropIfConnectChannelCmd": roadmAddDropIfConnectChannelCmd,
       "roadmAddDropIfDisconnectChannelCmd": roadmAddDropIfDisconnectChannelCmd,
       "roadmAddDropIfGroupIndex": roadmAddDropIfGroupIndex,
       "roadmAddDropIfAddAllChannelCommand": roadmAddDropIfAddAllChannelCommand,
       "roadmAddDropIfSetAdminStatusCommand": roadmAddDropIfSetAdminStatusCommand,
       "roadmAddDropIfSpacingHwCapability": roadmAddDropIfSpacingHwCapability,
       "roadmLineIfList": roadmLineIfList,
       "roadmLineIfTable": roadmLineIfTable,
       "roadmLineIfEntry": roadmLineIfEntry,
       "roadmLineIfIndex": roadmLineIfIndex,
       "roadmLineIfName": roadmLineIfName,
       "roadmLineIfDescr": roadmLineIfDescr,
       "roadmLineIfSubrack": roadmLineIfSubrack,
       "roadmLineIfSlot": roadmLineIfSlot,
       "roadmLineIfTxPort": roadmLineIfTxPort,
       "roadmLineIfRxPort": roadmLineIfRxPort,
       "roadmLineIfInvPhysIndexOrZero": roadmLineIfInvPhysIndexOrZero,
       "roadmLineIfAdminStatus": roadmLineIfAdminStatus,
       "roadmLineIfOperStatus": roadmLineIfOperStatus,
       "roadmLineIfObjectProperty": roadmLineIfObjectProperty,
       "roadmLineIfTxSignalStatus": roadmLineIfTxSignalStatus,
       "roadmLineIfNoOfConnectedChannels": roadmLineIfNoOfConnectedChannels,
       "roadmLineIfViewChannelList": roadmLineIfViewChannelList,
       "roadmLineIfSetAttenuationCommand": roadmLineIfSetAttenuationCommand,
       "roadmLineIfAdjustAttenuationDeltaCommand": roadmLineIfAdjustAttenuationDeltaCommand,
       "roadmLineIfMonitorInsertionLoss": roadmLineIfMonitorInsertionLoss,
       "roadmLineIfSetAdminStatusCommand": roadmLineIfSetAdminStatusCommand,
       "roadmGroupRoadmList": roadmGroupRoadmList,
       "roadmGroupRoadmTable": roadmGroupRoadmTable,
       "roadmGroupRoadmEntry": roadmGroupRoadmEntry,
       "roadmGroupRoadmIndex": roadmGroupRoadmIndex,
       "roadmGroupRoadmName": roadmGroupRoadmName,
       "roadmGroupRoadmDescr": roadmGroupRoadmDescr,
       "roadmGroupRoadmRightSubrack": roadmGroupRoadmRightSubrack,
       "roadmGroupRoadmRightSlot": roadmGroupRoadmRightSlot,
       "roadmGroupRoadmRightPort": roadmGroupRoadmRightPort,
       "roadmGroupRoadmLeftSubrack": roadmGroupRoadmLeftSubrack,
       "roadmGroupRoadmLeftSlot": roadmGroupRoadmLeftSlot,
       "roadmGroupRoadmLeftPort": roadmGroupRoadmLeftPort,
       "roadmGroupRoadmAdminStatus": roadmGroupRoadmAdminStatus,
       "roadmGroupRoadmObjectProperty": roadmGroupRoadmObjectProperty,
       "roadmGroupRoadmDataAdminStatus": roadmGroupRoadmDataAdminStatus,
       "roadmGroupRoadmDataDropFrequencyMin": roadmGroupRoadmDataDropFrequencyMin,
       "roadmGroupRoadmDataDropFrequencyMax": roadmGroupRoadmDataDropFrequencyMax,
       "roadmGroupRoadmDataDropFrequencyLimitMin": roadmGroupRoadmDataDropFrequencyLimitMin,
       "roadmGroupRoadmDataDropFrequencyLimitMax": roadmGroupRoadmDataDropFrequencyLimitMax,
       "roadmGroupRoadmDataMode": roadmGroupRoadmDataMode,
       "roadmGroupRoadmDataSpacingMode": roadmGroupRoadmDataSpacingMode,
       "roadmGroupRoadmConfigurationCommand": roadmGroupRoadmConfigurationCommand,
       "roadmGroupRoadmLimitConfigurationCommand": roadmGroupRoadmLimitConfigurationCommand,
       "roadmGroupRoadmPasswd": roadmGroupRoadmPasswd,
       "roadmGroupRoadmPasswdConfig": roadmGroupRoadmPasswdConfig,
       "roadmGroupRoadmDataGuardChannel1": roadmGroupRoadmDataGuardChannel1,
       "roadmGroupRoadmDataGuardChannel2": roadmGroupRoadmDataGuardChannel2,
       "roadmGroupRoadmNoOfConnectedChannels": roadmGroupRoadmNoOfConnectedChannels,
       "roadmGroupRoadmViewChannelList": roadmGroupRoadmViewChannelList,
       "roadmGroupRoadmConnectedChannelMask": roadmGroupRoadmConnectedChannelMask,
       "roadmGroupRoadmAddChannelCommand": roadmGroupRoadmAddChannelCommand,
       "roadmGroupRoadmUnlinkChannelCommand": roadmGroupRoadmUnlinkChannelCommand,
       "roadmGroupRoadmUnlinkAllChannelsCommand": roadmGroupRoadmUnlinkAllChannelsCommand,
       "roadmGroupRoadmConnectChannelCmd": roadmGroupRoadmConnectChannelCmd,
       "roadmGroupRoadmDisconnectChannelCmd": roadmGroupRoadmDisconnectChannelCmd,
       "roadmGroupRoadmAddAllChannelCommand": roadmGroupRoadmAddAllChannelCommand,
       "roadmGroupLineList": roadmGroupLineList,
       "roadmGroupLineTable": roadmGroupLineTable,
       "roadmGroupLineEntry": roadmGroupLineEntry,
       "roadmGroupLineIndex": roadmGroupLineIndex,
       "roadmGroupLineName": roadmGroupLineName,
       "roadmGroupLineDescr": roadmGroupLineDescr,
       "roadmGroupLineSubrack": roadmGroupLineSubrack,
       "roadmGroupLineSlot": roadmGroupLineSlot,
       "roadmGroupLinePort": roadmGroupLinePort,
       "roadmGroupLineAdminStatus": roadmGroupLineAdminStatus,
       "roadmGroupLineObjectProperty": roadmGroupLineObjectProperty,
       "roadmGroupLineCreateLineCommand": roadmGroupLineCreateLineCommand,
       "roadmGroupLineDeleteLineCommand": roadmGroupLineDeleteLineCommand,
       "roadmGroupLineNoOfLines": roadmGroupLineNoOfLines,
       "roadmLineList": roadmLineList,
       "roadmLineTable": roadmLineTable,
       "roadmLineEntry": roadmLineEntry,
       "roadmLineIndex": roadmLineIndex,
       "roadmLineName": roadmLineName,
       "roadmLineDescr": roadmLineDescr,
       "roadmLineSubrack": roadmLineSubrack,
       "roadmLineSlot": roadmLineSlot,
       "roadmLinePort": roadmLinePort,
       "roadmLineObjectProperty": roadmLineObjectProperty,
       "roadmLineGroupId": roadmLineGroupId,
       "roadmLineFrequencyMismatch": roadmLineFrequencyMismatch,
       "roadmLineFrequencyUsed": roadmLineFrequencyUsed,
       "roadmLineAdminStatus": roadmLineAdminStatus,
       "roadmChannelList": roadmChannelList,
       "roadmChannelTable": roadmChannelTable,
       "roadmChannelEntry": roadmChannelEntry,
       "roadmChannelIndex": roadmChannelIndex,
       "roadmChannelName": roadmChannelName,
       "roadmChannelFrequency": roadmChannelFrequency,
       "roadmChannelRoadmLineIfIndex": roadmChannelRoadmLineIfIndex,
       "roadmChannelRoadmAddDropIfIndex": roadmChannelRoadmAddDropIfIndex,
       "roadmChannelAdminStatus": roadmChannelAdminStatus,
       "roadmChannelOperStatus": roadmChannelOperStatus,
       "roadmChannelAttenuation": roadmChannelAttenuation,
       "roadmChannelConnectedToInterface": roadmChannelConnectedToInterface,
       "roadmChannelConnectDisconnectCommand": roadmChannelConnectDisconnectCommand}
)
