# SNMP MIB module (RLE-FALCON-EM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/chatsworth/RLE-FALCON-EM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:52:01 2025
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

(TruthValue,) = mibBuilder.importSymbols(
    "RFC1253-MIB",
    "TruthValue")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rle_ObjectIdentity = ObjectIdentity
rle = _Rle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1)
)
_Falcon_em_ObjectIdentity = ObjectIdentity
falcon_em = _Falcon_em_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5)
)
_Falcon_emMIB_ObjectIdentity = ObjectIdentity
falcon_emMIB = _Falcon_emMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1)
)
_FalconIdent_ObjectIdentity = ObjectIdentity
falconIdent = _FalconIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 1)
)
_FalconIdentManufacturer_Type = DisplayString
_FalconIdentManufacturer_Object = MibScalar
falconIdentManufacturer = _FalconIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 1, 1),
    _FalconIdentManufacturer_Type()
)
falconIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconIdentManufacturer.setStatus("mandatory")
_FalconIdentModel_Type = DisplayString
_FalconIdentModel_Object = MibScalar
falconIdentModel = _FalconIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 1, 2),
    _FalconIdentModel_Type()
)
falconIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconIdentModel.setStatus("mandatory")
_FalconIdentSoftwareVersion_Type = DisplayString
_FalconIdentSoftwareVersion_Object = MibScalar
falconIdentSoftwareVersion = _FalconIdentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 1, 3),
    _FalconIdentSoftwareVersion_Type()
)
falconIdentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconIdentSoftwareVersion.setStatus("mandatory")
_FalconIdentSpecific_Type = ObjectIdentifier
_FalconIdentSpecific_Object = MibScalar
falconIdentSpecific = _FalconIdentSpecific_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 1, 4),
    _FalconIdentSpecific_Type()
)
falconIdentSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconIdentSpecific.setStatus("mandatory")
_FalconOptionCards_ObjectIdentity = ObjectIdentity
falconOptionCards = _FalconOptionCards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 1, 5)
)


class _FalconOptionCard1_Type(Integer32):
    """Custom type falconOptionCard1 based on Integer32"""
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
        *(("notInstalled", 0),
          ("analog12input12relay", 1),
          ("digital12input12relay", 2),
          ("digital24input", 3))
    )


_FalconOptionCard1_Type.__name__ = "Integer32"
_FalconOptionCard1_Object = MibScalar
falconOptionCard1 = _FalconOptionCard1_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 1, 5, 1),
    _FalconOptionCard1_Type()
)
falconOptionCard1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconOptionCard1.setStatus("mandatory")


class _FalconOptionCard2_Type(Integer32):
    """Custom type falconOptionCard2 based on Integer32"""
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
        *(("notInstalled", 0),
          ("analog12input12relay", 1),
          ("digital12input12relay", 2),
          ("digital24input", 3))
    )


_FalconOptionCard2_Type.__name__ = "Integer32"
_FalconOptionCard2_Object = MibScalar
falconOptionCard2 = _FalconOptionCard2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 1, 5, 2),
    _FalconOptionCard2_Type()
)
falconOptionCard2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconOptionCard2.setStatus("mandatory")


class _FalconOptionCard3_Type(Integer32):
    """Custom type falconOptionCard3 based on Integer32"""
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
        *(("notInstalled", 0),
          ("analog12input12relay", 1),
          ("digital12input12relay", 2),
          ("digital24input", 3))
    )


_FalconOptionCard3_Type.__name__ = "Integer32"
_FalconOptionCard3_Object = MibScalar
falconOptionCard3 = _FalconOptionCard3_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 1, 5, 3),
    _FalconOptionCard3_Type()
)
falconOptionCard3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconOptionCard3.setStatus("mandatory")


class _FalconOptionCard4_Type(Integer32):
    """Custom type falconOptionCard4 based on Integer32"""
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
        *(("notInstalled", 0),
          ("analog12input12relay", 1),
          ("digital12input12relay", 2),
          ("digital24input", 3))
    )


_FalconOptionCard4_Type.__name__ = "Integer32"
_FalconOptionCard4_Object = MibScalar
falconOptionCard4 = _FalconOptionCard4_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 1, 5, 4),
    _FalconOptionCard4_Type()
)
falconOptionCard4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconOptionCard4.setStatus("mandatory")
_FalconSystem_ObjectIdentity = ObjectIdentity
falconSystem = _FalconSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 2)
)
_FalconSystemSettings_ObjectIdentity = ObjectIdentity
falconSystemSettings = _FalconSystemSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 2, 1)
)
_FalconClock_Type = DisplayString
_FalconClock_Object = MibScalar
falconClock = _FalconClock_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 2, 1, 1),
    _FalconClock_Type()
)
falconClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconClock.setStatus("mandatory")


class _FalconDoorAlarmBypass_Type(Integer32):
    """Custom type falconDoorAlarmBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconDoorAlarmBypass_Type.__name__ = "Integer32"
_FalconDoorAlarmBypass_Object = MibScalar
falconDoorAlarmBypass = _FalconDoorAlarmBypass_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 2, 1, 2),
    _FalconDoorAlarmBypass_Type()
)
falconDoorAlarmBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconDoorAlarmBypass.setStatus("mandatory")


class _FalconInputVoltage_Type(Integer32):
    """Custom type falconInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInputVoltage_Type.__name__ = "Integer32"
_FalconInputVoltage_Object = MibScalar
falconInputVoltage = _FalconInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 2, 1, 3),
    _FalconInputVoltage_Type()
)
falconInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInputVoltage.setStatus("mandatory")


class _FalconLowBatteryThreshold_Type(Integer32):
    """Custom type falconLowBatteryThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconLowBatteryThreshold_Type.__name__ = "Integer32"
_FalconLowBatteryThreshold_Object = MibScalar
falconLowBatteryThreshold = _FalconLowBatteryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 2, 1, 4),
    _FalconLowBatteryThreshold_Type()
)
falconLowBatteryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconLowBatteryThreshold.setStatus("mandatory")


class _FalconAnalogAverage_Type(Integer32):
    """Custom type falconAnalogAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_FalconAnalogAverage_Type.__name__ = "Integer32"
_FalconAnalogAverage_Object = MibScalar
falconAnalogAverage = _FalconAnalogAverage_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 2, 1, 5),
    _FalconAnalogAverage_Type()
)
falconAnalogAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconAnalogAverage.setStatus("mandatory")
_FalconPagerStatusString_Type = DisplayString
_FalconPagerStatusString_Object = MibScalar
falconPagerStatusString = _FalconPagerStatusString_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 2, 1, 6),
    _FalconPagerStatusString_Type()
)
falconPagerStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconPagerStatusString.setStatus("mandatory")
_FalconWebUser_Type = DisplayString
_FalconWebUser_Object = MibScalar
falconWebUser = _FalconWebUser_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 2, 1, 7),
    _FalconWebUser_Type()
)
falconWebUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconWebUser.setStatus("mandatory")


class _FalconMaintenanceMode_Type(Integer32):
    """Custom type falconMaintenanceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("active", 1))
    )


_FalconMaintenanceMode_Type.__name__ = "Integer32"
_FalconMaintenanceMode_Object = MibScalar
falconMaintenanceMode = _FalconMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 2, 1, 8),
    _FalconMaintenanceMode_Type()
)
falconMaintenanceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconMaintenanceMode.setStatus("mandatory")
_FalconKeypad_ObjectIdentity = ObjectIdentity
falconKeypad = _FalconKeypad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 2, 2)
)
_FalconKeypadUsers_Type = Integer32
_FalconKeypadUsers_Object = MibScalar
falconKeypadUsers = _FalconKeypadUsers_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 2, 2, 1),
    _FalconKeypadUsers_Type()
)
falconKeypadUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconKeypadUsers.setStatus("mandatory")
_FalconKeypadUsersTable_Object = MibTable
falconKeypadUsersTable = _FalconKeypadUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    falconKeypadUsersTable.setStatus("mandatory")
_FalconKeypadUserEntry_Object = MibTableRow
falconKeypadUserEntry = _FalconKeypadUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 2, 2, 2, 1)
)
falconKeypadUserEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconKeypadUserIndex"),
)
if mibBuilder.loadTexts:
    falconKeypadUserEntry.setStatus("mandatory")
_FalconKeypadUserIndex_Type = Integer32
_FalconKeypadUserIndex_Object = MibTableColumn
falconKeypadUserIndex = _FalconKeypadUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 2, 2, 2, 1, 1),
    _FalconKeypadUserIndex_Type()
)
falconKeypadUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconKeypadUserIndex.setStatus("mandatory")
_FalconKeypadCode_Type = DisplayString
_FalconKeypadCode_Object = MibTableColumn
falconKeypadCode = _FalconKeypadCode_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 2, 2, 2, 1, 2),
    _FalconKeypadCode_Type()
)
falconKeypadCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode.setStatus("mandatory")
_FalconKeypadName_Type = DisplayString
_FalconKeypadName_Object = MibTableColumn
falconKeypadName = _FalconKeypadName_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 2, 2, 2, 1, 3),
    _FalconKeypadName_Type()
)
falconKeypadName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName.setStatus("mandatory")
_FalconInputs_ObjectIdentity = ObjectIdentity
falconInputs = _FalconInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3)
)
_FalconInputPorts_ObjectIdentity = ObjectIdentity
falconInputPorts = _FalconInputPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1)
)
_FalconNumberOfInputPorts_Type = Integer32
_FalconNumberOfInputPorts_Object = MibScalar
falconNumberOfInputPorts = _FalconNumberOfInputPorts_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 1),
    _FalconNumberOfInputPorts_Type()
)
falconNumberOfInputPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconNumberOfInputPorts.setStatus("mandatory")
_FalconInputTable_Object = MibTable
falconInputTable = _FalconInputTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    falconInputTable.setStatus("mandatory")
_FalconInputEntry_Object = MibTableRow
falconInputEntry = _FalconInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 2, 1)
)
falconInputEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconInputIndex"),
)
if mibBuilder.loadTexts:
    falconInputEntry.setStatus("mandatory")
_FalconInputIndex_Type = Integer32
_FalconInputIndex_Object = MibTableColumn
falconInputIndex = _FalconInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 2, 1, 1),
    _FalconInputIndex_Type()
)
falconInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInputIndex.setStatus("mandatory")


class _FalconInputType_Type(Integer32):
    """Custom type falconInputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 0),
          ("analog", 1),
          ("digital", 2))
    )


_FalconInputType_Type.__name__ = "Integer32"
_FalconInputType_Object = MibTableColumn
falconInputType = _FalconInputType_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 2, 1, 2),
    _FalconInputType_Type()
)
falconInputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInputType.setStatus("mandatory")


class _FalconInputState_Type(Integer32):
    """Custom type falconInputState based on Integer32"""
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
        *(("notInstalled", 0),
          ("notConfigured", 1),
          ("analog4to20Installed", 2),
          ("digitalNOInstalled", 3),
          ("digitalNCInstalled", 4),
          ("digitalSTInstalled", 5))
    )


_FalconInputState_Type.__name__ = "Integer32"
_FalconInputState_Object = MibTableColumn
falconInputState = _FalconInputState_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 2, 1, 3),
    _FalconInputState_Type()
)
falconInputState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInputState.setStatus("mandatory")


class _FalconInputReading_Type(Integer32):
    """Custom type falconInputReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInputReading_Type.__name__ = "Integer32"
_FalconInputReading_Object = MibTableColumn
falconInputReading = _FalconInputReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 2, 1, 4),
    _FalconInputReading_Type()
)
falconInputReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInputReading.setStatus("mandatory")


class _FalconInputGain_Type(Integer32):
    """Custom type falconInputGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInputGain_Type.__name__ = "Integer32"
_FalconInputGain_Object = MibTableColumn
falconInputGain = _FalconInputGain_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 2, 1, 5),
    _FalconInputGain_Type()
)
falconInputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInputGain.setStatus("mandatory")


class _FalconInputOffset_Type(Integer32):
    """Custom type falconInputOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInputOffset_Type.__name__ = "Integer32"
_FalconInputOffset_Object = MibTableColumn
falconInputOffset = _FalconInputOffset_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 2, 1, 6),
    _FalconInputOffset_Type()
)
falconInputOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInputOffset.setStatus("mandatory")
_FalconInputLabel_Type = DisplayString
_FalconInputLabel_Object = MibTableColumn
falconInputLabel = _FalconInputLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 2, 1, 7),
    _FalconInputLabel_Type()
)
falconInputLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInputLabel.setStatus("mandatory")
_FalconInputUOM_Type = DisplayString
_FalconInputUOM_Object = MibTableColumn
falconInputUOM = _FalconInputUOM_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 2, 1, 8),
    _FalconInputUOM_Type()
)
falconInputUOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInputUOM.setStatus("mandatory")


class _FalconInputHighLimit2_Type(Integer32):
    """Custom type falconInputHighLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInputHighLimit2_Type.__name__ = "Integer32"
_FalconInputHighLimit2_Object = MibTableColumn
falconInputHighLimit2 = _FalconInputHighLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 2, 1, 9),
    _FalconInputHighLimit2_Type()
)
falconInputHighLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInputHighLimit2.setStatus("mandatory")


class _FalconInputHighLimit_Type(Integer32):
    """Custom type falconInputHighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInputHighLimit_Type.__name__ = "Integer32"
_FalconInputHighLimit_Object = MibTableColumn
falconInputHighLimit = _FalconInputHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 2, 1, 10),
    _FalconInputHighLimit_Type()
)
falconInputHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInputHighLimit.setStatus("mandatory")


class _FalconInputLowLimit_Type(Integer32):
    """Custom type falconInputLowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInputLowLimit_Type.__name__ = "Integer32"
_FalconInputLowLimit_Object = MibTableColumn
falconInputLowLimit = _FalconInputLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 2, 1, 11),
    _FalconInputLowLimit_Type()
)
falconInputLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInputLowLimit.setStatus("mandatory")


class _FalconInputLowLimit2_Type(Integer32):
    """Custom type falconInputLowLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInputLowLimit2_Type.__name__ = "Integer32"
_FalconInputLowLimit2_Object = MibTableColumn
falconInputLowLimit2 = _FalconInputLowLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 2, 1, 12),
    _FalconInputLowLimit2_Type()
)
falconInputLowLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInputLowLimit2.setStatus("mandatory")


class _FalconInputDelay_Type(Integer32):
    """Custom type falconInputDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInputDelay_Type.__name__ = "Integer32"
_FalconInputDelay_Object = MibTableColumn
falconInputDelay = _FalconInputDelay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 2, 1, 13),
    _FalconInputDelay_Type()
)
falconInputDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInputDelay.setStatus("mandatory")


class _FalconInputHysteresis_Type(Integer32):
    """Custom type falconInputHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FalconInputHysteresis_Type.__name__ = "Integer32"
_FalconInputHysteresis_Object = MibTableColumn
falconInputHysteresis = _FalconInputHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 2, 1, 14),
    _FalconInputHysteresis_Type()
)
falconInputHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInputHysteresis.setStatus("mandatory")


class _FalconInputSchedule_Type(Integer32):
    """Custom type falconInputSchedule based on Integer32"""
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
          ("a", 1),
          ("b", 2))
    )


_FalconInputSchedule_Type.__name__ = "Integer32"
_FalconInputSchedule_Object = MibTableColumn
falconInputSchedule = _FalconInputSchedule_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 2, 1, 15),
    _FalconInputSchedule_Type()
)
falconInputSchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInputSchedule.setStatus("mandatory")
_FalconInputDigOffLabel_Type = DisplayString
_FalconInputDigOffLabel_Object = MibTableColumn
falconInputDigOffLabel = _FalconInputDigOffLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 1, 2, 1, 16),
    _FalconInputDigOffLabel_Type()
)
falconInputDigOffLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInputDigOffLabel.setStatus("mandatory")
_FalconTHSensors_ObjectIdentity = ObjectIdentity
falconTHSensors = _FalconTHSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2)
)
_FalconTempSensors_ObjectIdentity = ObjectIdentity
falconTempSensors = _FalconTempSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 1)
)
_FalconNumberOfTempSensors_Type = Integer32
_FalconNumberOfTempSensors_Object = MibScalar
falconNumberOfTempSensors = _FalconNumberOfTempSensors_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 1, 1),
    _FalconNumberOfTempSensors_Type()
)
falconNumberOfTempSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconNumberOfTempSensors.setStatus("mandatory")
_FalconTSTable_Object = MibTable
falconTSTable = _FalconTSTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    falconTSTable.setStatus("mandatory")
_FalconTSEntry_Object = MibTableRow
falconTSEntry = _FalconTSEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 1, 2, 1)
)
falconTSEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconTSIndex"),
)
if mibBuilder.loadTexts:
    falconTSEntry.setStatus("mandatory")
_FalconTSIndex_Type = Integer32
_FalconTSIndex_Object = MibTableColumn
falconTSIndex = _FalconTSIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 1, 2, 1, 1),
    _FalconTSIndex_Type()
)
falconTSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconTSIndex.setStatus("mandatory")


class _FalconTemperatureSensorState_Type(Integer32):
    """Custom type falconTemperatureSensorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("degF", 0),
          ("degC", 1))
    )


_FalconTemperatureSensorState_Type.__name__ = "Integer32"
_FalconTemperatureSensorState_Object = MibTableColumn
falconTemperatureSensorState = _FalconTemperatureSensorState_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 1, 2, 1, 2),
    _FalconTemperatureSensorState_Type()
)
falconTemperatureSensorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconTemperatureSensorState.setStatus("mandatory")


class _FalconTemperatureSensorReading_Type(Integer32):
    """Custom type falconTemperatureSensorReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconTemperatureSensorReading_Type.__name__ = "Integer32"
_FalconTemperatureSensorReading_Object = MibTableColumn
falconTemperatureSensorReading = _FalconTemperatureSensorReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 1, 2, 1, 3),
    _FalconTemperatureSensorReading_Type()
)
falconTemperatureSensorReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconTemperatureSensorReading.setStatus("mandatory")


class _FalconTemperatureSensorOffset_Type(Integer32):
    """Custom type falconTemperatureSensorOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconTemperatureSensorOffset_Type.__name__ = "Integer32"
_FalconTemperatureSensorOffset_Object = MibTableColumn
falconTemperatureSensorOffset = _FalconTemperatureSensorOffset_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 1, 2, 1, 4),
    _FalconTemperatureSensorOffset_Type()
)
falconTemperatureSensorOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconTemperatureSensorOffset.setStatus("mandatory")
_FalconTemperatureSensorLabel_Type = DisplayString
_FalconTemperatureSensorLabel_Object = MibTableColumn
falconTemperatureSensorLabel = _FalconTemperatureSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 1, 2, 1, 5),
    _FalconTemperatureSensorLabel_Type()
)
falconTemperatureSensorLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconTemperatureSensorLabel.setStatus("mandatory")
_FalconTemperatureSensorUOM_Type = DisplayString
_FalconTemperatureSensorUOM_Object = MibTableColumn
falconTemperatureSensorUOM = _FalconTemperatureSensorUOM_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 1, 2, 1, 6),
    _FalconTemperatureSensorUOM_Type()
)
falconTemperatureSensorUOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconTemperatureSensorUOM.setStatus("mandatory")


class _FalconTemperatureSensorHighLimit2_Type(Integer32):
    """Custom type falconTemperatureSensorHighLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconTemperatureSensorHighLimit2_Type.__name__ = "Integer32"
_FalconTemperatureSensorHighLimit2_Object = MibTableColumn
falconTemperatureSensorHighLimit2 = _FalconTemperatureSensorHighLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 1, 2, 1, 7),
    _FalconTemperatureSensorHighLimit2_Type()
)
falconTemperatureSensorHighLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconTemperatureSensorHighLimit2.setStatus("mandatory")


class _FalconTemperatureSensorHighLimit_Type(Integer32):
    """Custom type falconTemperatureSensorHighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconTemperatureSensorHighLimit_Type.__name__ = "Integer32"
_FalconTemperatureSensorHighLimit_Object = MibTableColumn
falconTemperatureSensorHighLimit = _FalconTemperatureSensorHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 1, 2, 1, 8),
    _FalconTemperatureSensorHighLimit_Type()
)
falconTemperatureSensorHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconTemperatureSensorHighLimit.setStatus("mandatory")


class _FalconTemperatureSensorLowLimit_Type(Integer32):
    """Custom type falconTemperatureSensorLowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconTemperatureSensorLowLimit_Type.__name__ = "Integer32"
_FalconTemperatureSensorLowLimit_Object = MibTableColumn
falconTemperatureSensorLowLimit = _FalconTemperatureSensorLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 1, 2, 1, 9),
    _FalconTemperatureSensorLowLimit_Type()
)
falconTemperatureSensorLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconTemperatureSensorLowLimit.setStatus("mandatory")


class _FalconTemperatureSensorLowLimit2_Type(Integer32):
    """Custom type falconTemperatureSensorLowLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconTemperatureSensorLowLimit2_Type.__name__ = "Integer32"
_FalconTemperatureSensorLowLimit2_Object = MibTableColumn
falconTemperatureSensorLowLimit2 = _FalconTemperatureSensorLowLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 1, 2, 1, 10),
    _FalconTemperatureSensorLowLimit2_Type()
)
falconTemperatureSensorLowLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconTemperatureSensorLowLimit2.setStatus("mandatory")


class _FalconTemperatureSensorDelay_Type(Integer32):
    """Custom type falconTemperatureSensorDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconTemperatureSensorDelay_Type.__name__ = "Integer32"
_FalconTemperatureSensorDelay_Object = MibTableColumn
falconTemperatureSensorDelay = _FalconTemperatureSensorDelay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 1, 2, 1, 11),
    _FalconTemperatureSensorDelay_Type()
)
falconTemperatureSensorDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconTemperatureSensorDelay.setStatus("mandatory")


class _FalconTemperatureSensorHysteresis_Type(Integer32):
    """Custom type falconTemperatureSensorHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FalconTemperatureSensorHysteresis_Type.__name__ = "Integer32"
_FalconTemperatureSensorHysteresis_Object = MibTableColumn
falconTemperatureSensorHysteresis = _FalconTemperatureSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 1, 2, 1, 12),
    _FalconTemperatureSensorHysteresis_Type()
)
falconTemperatureSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconTemperatureSensorHysteresis.setStatus("mandatory")


class _FalconTemperatureSensorSchedule_Type(Integer32):
    """Custom type falconTemperatureSensorSchedule based on Integer32"""
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
          ("a", 1),
          ("b", 2))
    )


_FalconTemperatureSensorSchedule_Type.__name__ = "Integer32"
_FalconTemperatureSensorSchedule_Object = MibTableColumn
falconTemperatureSensorSchedule = _FalconTemperatureSensorSchedule_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 1, 2, 1, 13),
    _FalconTemperatureSensorSchedule_Type()
)
falconTemperatureSensorSchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconTemperatureSensorSchedule.setStatus("mandatory")
_FalconHumiditySensors_ObjectIdentity = ObjectIdentity
falconHumiditySensors = _FalconHumiditySensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 2)
)
_FalconNumberOfHumiditySensors_Type = Integer32
_FalconNumberOfHumiditySensors_Object = MibScalar
falconNumberOfHumiditySensors = _FalconNumberOfHumiditySensors_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 2, 1),
    _FalconNumberOfHumiditySensors_Type()
)
falconNumberOfHumiditySensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconNumberOfHumiditySensors.setStatus("mandatory")
_FalconHSTable_Object = MibTable
falconHSTable = _FalconHSTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    falconHSTable.setStatus("mandatory")
_FalconHSEntry_Object = MibTableRow
falconHSEntry = _FalconHSEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 2, 2, 1)
)
falconHSEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconHSIndex"),
)
if mibBuilder.loadTexts:
    falconHSEntry.setStatus("mandatory")
_FalconHSIndex_Type = Integer32
_FalconHSIndex_Object = MibTableColumn
falconHSIndex = _FalconHSIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 2, 2, 1, 1),
    _FalconHSIndex_Type()
)
falconHSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconHSIndex.setStatus("mandatory")


class _FalconHumiditySensorState_Type(Integer32):
    """Custom type falconHumiditySensorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("RelativeHumidity", 1)
    )


_FalconHumiditySensorState_Type.__name__ = "Integer32"
_FalconHumiditySensorState_Object = MibTableColumn
falconHumiditySensorState = _FalconHumiditySensorState_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 2, 2, 1, 2),
    _FalconHumiditySensorState_Type()
)
falconHumiditySensorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconHumiditySensorState.setStatus("mandatory")


class _FalconHumiditySensorReading_Type(Integer32):
    """Custom type falconHumiditySensorReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconHumiditySensorReading_Type.__name__ = "Integer32"
_FalconHumiditySensorReading_Object = MibTableColumn
falconHumiditySensorReading = _FalconHumiditySensorReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 2, 2, 1, 3),
    _FalconHumiditySensorReading_Type()
)
falconHumiditySensorReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconHumiditySensorReading.setStatus("mandatory")


class _FalconHumiditySensorOffset_Type(Integer32):
    """Custom type falconHumiditySensorOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconHumiditySensorOffset_Type.__name__ = "Integer32"
_FalconHumiditySensorOffset_Object = MibTableColumn
falconHumiditySensorOffset = _FalconHumiditySensorOffset_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 2, 2, 1, 4),
    _FalconHumiditySensorOffset_Type()
)
falconHumiditySensorOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconHumiditySensorOffset.setStatus("mandatory")
_FalconHumiditySensorLabel_Type = DisplayString
_FalconHumiditySensorLabel_Object = MibTableColumn
falconHumiditySensorLabel = _FalconHumiditySensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 2, 2, 1, 5),
    _FalconHumiditySensorLabel_Type()
)
falconHumiditySensorLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconHumiditySensorLabel.setStatus("mandatory")
_FalconHumiditySensorUOM_Type = DisplayString
_FalconHumiditySensorUOM_Object = MibTableColumn
falconHumiditySensorUOM = _FalconHumiditySensorUOM_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 2, 2, 1, 6),
    _FalconHumiditySensorUOM_Type()
)
falconHumiditySensorUOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconHumiditySensorUOM.setStatus("mandatory")


class _FalconHumiditySensorHighLimit2_Type(Integer32):
    """Custom type falconHumiditySensorHighLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconHumiditySensorHighLimit2_Type.__name__ = "Integer32"
_FalconHumiditySensorHighLimit2_Object = MibTableColumn
falconHumiditySensorHighLimit2 = _FalconHumiditySensorHighLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 2, 2, 1, 7),
    _FalconHumiditySensorHighLimit2_Type()
)
falconHumiditySensorHighLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconHumiditySensorHighLimit2.setStatus("mandatory")


class _FalconHumiditySensorHighLimit_Type(Integer32):
    """Custom type falconHumiditySensorHighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconHumiditySensorHighLimit_Type.__name__ = "Integer32"
_FalconHumiditySensorHighLimit_Object = MibTableColumn
falconHumiditySensorHighLimit = _FalconHumiditySensorHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 2, 2, 1, 8),
    _FalconHumiditySensorHighLimit_Type()
)
falconHumiditySensorHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconHumiditySensorHighLimit.setStatus("mandatory")


class _FalconHumiditySensorLowLimit_Type(Integer32):
    """Custom type falconHumiditySensorLowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconHumiditySensorLowLimit_Type.__name__ = "Integer32"
_FalconHumiditySensorLowLimit_Object = MibTableColumn
falconHumiditySensorLowLimit = _FalconHumiditySensorLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 2, 2, 1, 9),
    _FalconHumiditySensorLowLimit_Type()
)
falconHumiditySensorLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconHumiditySensorLowLimit.setStatus("mandatory")


class _FalconHumiditySensorLowLimit2_Type(Integer32):
    """Custom type falconHumiditySensorLowLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconHumiditySensorLowLimit2_Type.__name__ = "Integer32"
_FalconHumiditySensorLowLimit2_Object = MibTableColumn
falconHumiditySensorLowLimit2 = _FalconHumiditySensorLowLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 2, 2, 1, 10),
    _FalconHumiditySensorLowLimit2_Type()
)
falconHumiditySensorLowLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconHumiditySensorLowLimit2.setStatus("mandatory")


class _FalconHumiditySensorDelay_Type(Integer32):
    """Custom type falconHumiditySensorDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconHumiditySensorDelay_Type.__name__ = "Integer32"
_FalconHumiditySensorDelay_Object = MibTableColumn
falconHumiditySensorDelay = _FalconHumiditySensorDelay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 2, 2, 1, 11),
    _FalconHumiditySensorDelay_Type()
)
falconHumiditySensorDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconHumiditySensorDelay.setStatus("mandatory")


class _FalconHumiditySensorHysteresis_Type(Integer32):
    """Custom type falconHumiditySensorHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FalconHumiditySensorHysteresis_Type.__name__ = "Integer32"
_FalconHumiditySensorHysteresis_Object = MibTableColumn
falconHumiditySensorHysteresis = _FalconHumiditySensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 2, 2, 1, 12),
    _FalconHumiditySensorHysteresis_Type()
)
falconHumiditySensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconHumiditySensorHysteresis.setStatus("mandatory")


class _FalconHumiditySensorSchedule_Type(Integer32):
    """Custom type falconHumiditySensorSchedule based on Integer32"""
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
          ("a", 1),
          ("b", 2))
    )


_FalconHumiditySensorSchedule_Type.__name__ = "Integer32"
_FalconHumiditySensorSchedule_Object = MibTableColumn
falconHumiditySensorSchedule = _FalconHumiditySensorSchedule_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 3, 2, 2, 2, 1, 13),
    _FalconHumiditySensorSchedule_Type()
)
falconHumiditySensorSchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconHumiditySensorSchedule.setStatus("mandatory")
_FalconOutputs_ObjectIdentity = ObjectIdentity
falconOutputs = _FalconOutputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 4)
)
_FalconRelays_ObjectIdentity = ObjectIdentity
falconRelays = _FalconRelays_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 4, 1)
)
_FalconNumberOfRelays_Type = Integer32
_FalconNumberOfRelays_Object = MibScalar
falconNumberOfRelays = _FalconNumberOfRelays_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 4, 1, 1),
    _FalconNumberOfRelays_Type()
)
falconNumberOfRelays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconNumberOfRelays.setStatus("mandatory")
_FalconRelayTable_Object = MibTable
falconRelayTable = _FalconRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    falconRelayTable.setStatus("mandatory")
_FalconRelayEntry_Object = MibTableRow
falconRelayEntry = _FalconRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 4, 1, 2, 1)
)
falconRelayEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconRelayIndex"),
)
if mibBuilder.loadTexts:
    falconRelayEntry.setStatus("mandatory")
_FalconRelayIndex_Type = Integer32
_FalconRelayIndex_Object = MibTableColumn
falconRelayIndex = _FalconRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 4, 1, 2, 1, 1),
    _FalconRelayIndex_Type()
)
falconRelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconRelayIndex.setStatus("mandatory")


class _FalconRelayState_Type(Integer32):
    """Custom type falconRelayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("normallyOff", 1),
          ("normallyOn", 2),
          ("forceOn", 3),
          ("forceOff", 4),
          ("keypadControlled", 5),
          ("buttonControlled", 8),
          ("modbusControlled", 9))
    )


_FalconRelayState_Type.__name__ = "Integer32"
_FalconRelayState_Object = MibTableColumn
falconRelayState = _FalconRelayState_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 4, 1, 2, 1, 2),
    _FalconRelayState_Type()
)
falconRelayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelayState.setStatus("mandatory")


class _FalconRelayStatus_Type(Integer32):
    """Custom type falconRelayStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("normalOff", 1),
          ("normalOn", 2),
          ("forcedOn", 3),
          ("forcedOff", 4),
          ("keycodeActive", 5),
          ("alarmedActive", 6),
          ("scheduledActive", 7),
          ("buttonActive", 8),
          ("modbusActive", 9))
    )


_FalconRelayStatus_Type.__name__ = "Integer32"
_FalconRelayStatus_Object = MibTableColumn
falconRelayStatus = _FalconRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 4, 1, 2, 1, 3),
    _FalconRelayStatus_Type()
)
falconRelayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconRelayStatus.setStatus("mandatory")
_FalconRelayLabel_Type = DisplayString
_FalconRelayLabel_Object = MibTableColumn
falconRelayLabel = _FalconRelayLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 4, 1, 2, 1, 4),
    _FalconRelayLabel_Type()
)
falconRelayLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelayLabel.setStatus("mandatory")


class _FalconRelayTime_Type(Integer32):
    """Custom type falconRelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconRelayTime_Type.__name__ = "Integer32"
_FalconRelayTime_Object = MibTableColumn
falconRelayTime = _FalconRelayTime_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 4, 1, 2, 1, 5),
    _FalconRelayTime_Type()
)
falconRelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelayTime.setStatus("mandatory")


class _FalconRelaySchedule_Type(Integer32):
    """Custom type falconRelaySchedule based on Integer32"""
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
          ("a", 1),
          ("b", 2))
    )


_FalconRelaySchedule_Type.__name__ = "Integer32"
_FalconRelaySchedule_Object = MibTableColumn
falconRelaySchedule = _FalconRelaySchedule_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 4, 1, 2, 1, 6),
    _FalconRelaySchedule_Type()
)
falconRelaySchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconRelaySchedule.setStatus("mandatory")
_FalconAlarms_ObjectIdentity = ObjectIdentity
falconAlarms = _FalconAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5)
)
_FalconAlarmsPresent_Type = Gauge32
_FalconAlarmsPresent_Object = MibScalar
falconAlarmsPresent = _FalconAlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 1),
    _FalconAlarmsPresent_Type()
)
falconAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconAlarmsPresent.setStatus("mandatory")
_FalconAlarmTable_Object = MibTable
falconAlarmTable = _FalconAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 2)
)
if mibBuilder.loadTexts:
    falconAlarmTable.setStatus("mandatory")
_FalconAlarmEntry_Object = MibTableRow
falconAlarmEntry = _FalconAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 2, 1)
)
falconAlarmEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconAlarmId"),
)
if mibBuilder.loadTexts:
    falconAlarmEntry.setStatus("mandatory")
_FalconAlarmId_Type = PositiveInteger
_FalconAlarmId_Object = MibTableColumn
falconAlarmId = _FalconAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 2, 1, 1),
    _FalconAlarmId_Type()
)
falconAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    falconAlarmId.setStatus("mandatory")
_FalconAlarmDescr_Type = ObjectIdentifier
_FalconAlarmDescr_Object = MibTableColumn
falconAlarmDescr = _FalconAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 2, 1, 2),
    _FalconAlarmDescr_Type()
)
falconAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconAlarmDescr.setStatus("mandatory")
_FalconWellKnownAlarms_ObjectIdentity = ObjectIdentity
falconWellKnownAlarms = _FalconWellKnownAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3)
)
_FalconInput1DigAlarm_Type = ObjectIdentifier
_FalconInput1DigAlarm_Object = MibScalar
falconInput1DigAlarm = _FalconInput1DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 10),
    _FalconInput1DigAlarm_Type()
)
falconInput1DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput1DigAlarm.setStatus("mandatory")
_FalconInput1HighAlarm_Type = ObjectIdentifier
_FalconInput1HighAlarm_Object = MibScalar
falconInput1HighAlarm = _FalconInput1HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 11),
    _FalconInput1HighAlarm_Type()
)
falconInput1HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput1HighAlarm.setStatus("mandatory")
_FalconInput1LowAlarm_Type = ObjectIdentifier
_FalconInput1LowAlarm_Object = MibScalar
falconInput1LowAlarm = _FalconInput1LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 12),
    _FalconInput1LowAlarm_Type()
)
falconInput1LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput1LowAlarm.setStatus("mandatory")
_FalconInput1High2Alarm_Type = ObjectIdentifier
_FalconInput1High2Alarm_Object = MibScalar
falconInput1High2Alarm = _FalconInput1High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 13),
    _FalconInput1High2Alarm_Type()
)
falconInput1High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput1High2Alarm.setStatus("mandatory")
_FalconInput1Low2Alarm_Type = ObjectIdentifier
_FalconInput1Low2Alarm_Object = MibScalar
falconInput1Low2Alarm = _FalconInput1Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 14),
    _FalconInput1Low2Alarm_Type()
)
falconInput1Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput1Low2Alarm.setStatus("mandatory")
_FalconInput2DigAlarm_Type = ObjectIdentifier
_FalconInput2DigAlarm_Object = MibScalar
falconInput2DigAlarm = _FalconInput2DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 20),
    _FalconInput2DigAlarm_Type()
)
falconInput2DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput2DigAlarm.setStatus("mandatory")
_FalconInput2HighAlarm_Type = ObjectIdentifier
_FalconInput2HighAlarm_Object = MibScalar
falconInput2HighAlarm = _FalconInput2HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 21),
    _FalconInput2HighAlarm_Type()
)
falconInput2HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput2HighAlarm.setStatus("mandatory")
_FalconInput2LowAlarm_Type = ObjectIdentifier
_FalconInput2LowAlarm_Object = MibScalar
falconInput2LowAlarm = _FalconInput2LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 22),
    _FalconInput2LowAlarm_Type()
)
falconInput2LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput2LowAlarm.setStatus("mandatory")
_FalconInput2High2Alarm_Type = ObjectIdentifier
_FalconInput2High2Alarm_Object = MibScalar
falconInput2High2Alarm = _FalconInput2High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 23),
    _FalconInput2High2Alarm_Type()
)
falconInput2High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput2High2Alarm.setStatus("mandatory")
_FalconInput2Low2Alarm_Type = ObjectIdentifier
_FalconInput2Low2Alarm_Object = MibScalar
falconInput2Low2Alarm = _FalconInput2Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 24),
    _FalconInput2Low2Alarm_Type()
)
falconInput2Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput2Low2Alarm.setStatus("mandatory")
_FalconInput3DigAlarm_Type = ObjectIdentifier
_FalconInput3DigAlarm_Object = MibScalar
falconInput3DigAlarm = _FalconInput3DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 30),
    _FalconInput3DigAlarm_Type()
)
falconInput3DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput3DigAlarm.setStatus("mandatory")
_FalconInput3HighAlarm_Type = ObjectIdentifier
_FalconInput3HighAlarm_Object = MibScalar
falconInput3HighAlarm = _FalconInput3HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 31),
    _FalconInput3HighAlarm_Type()
)
falconInput3HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput3HighAlarm.setStatus("mandatory")
_FalconInput3LowAlarm_Type = ObjectIdentifier
_FalconInput3LowAlarm_Object = MibScalar
falconInput3LowAlarm = _FalconInput3LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 32),
    _FalconInput3LowAlarm_Type()
)
falconInput3LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput3LowAlarm.setStatus("mandatory")
_FalconInput3High2Alarm_Type = ObjectIdentifier
_FalconInput3High2Alarm_Object = MibScalar
falconInput3High2Alarm = _FalconInput3High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 33),
    _FalconInput3High2Alarm_Type()
)
falconInput3High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput3High2Alarm.setStatus("mandatory")
_FalconInput3Low2Alarm_Type = ObjectIdentifier
_FalconInput3Low2Alarm_Object = MibScalar
falconInput3Low2Alarm = _FalconInput3Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 34),
    _FalconInput3Low2Alarm_Type()
)
falconInput3Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput3Low2Alarm.setStatus("mandatory")
_FalconInput4DigAlarm_Type = ObjectIdentifier
_FalconInput4DigAlarm_Object = MibScalar
falconInput4DigAlarm = _FalconInput4DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 40),
    _FalconInput4DigAlarm_Type()
)
falconInput4DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput4DigAlarm.setStatus("mandatory")
_FalconInput4HighAlarm_Type = ObjectIdentifier
_FalconInput4HighAlarm_Object = MibScalar
falconInput4HighAlarm = _FalconInput4HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 41),
    _FalconInput4HighAlarm_Type()
)
falconInput4HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput4HighAlarm.setStatus("mandatory")
_FalconInput4LowAlarm_Type = ObjectIdentifier
_FalconInput4LowAlarm_Object = MibScalar
falconInput4LowAlarm = _FalconInput4LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 42),
    _FalconInput4LowAlarm_Type()
)
falconInput4LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput4LowAlarm.setStatus("mandatory")
_FalconInput4High2Alarm_Type = ObjectIdentifier
_FalconInput4High2Alarm_Object = MibScalar
falconInput4High2Alarm = _FalconInput4High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 43),
    _FalconInput4High2Alarm_Type()
)
falconInput4High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput4High2Alarm.setStatus("mandatory")
_FalconInput4Low2Alarm_Type = ObjectIdentifier
_FalconInput4Low2Alarm_Object = MibScalar
falconInput4Low2Alarm = _FalconInput4Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 44),
    _FalconInput4Low2Alarm_Type()
)
falconInput4Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput4Low2Alarm.setStatus("mandatory")
_FalconInput5DigAlarm_Type = ObjectIdentifier
_FalconInput5DigAlarm_Object = MibScalar
falconInput5DigAlarm = _FalconInput5DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 50),
    _FalconInput5DigAlarm_Type()
)
falconInput5DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput5DigAlarm.setStatus("mandatory")
_FalconInput5HighAlarm_Type = ObjectIdentifier
_FalconInput5HighAlarm_Object = MibScalar
falconInput5HighAlarm = _FalconInput5HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 51),
    _FalconInput5HighAlarm_Type()
)
falconInput5HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput5HighAlarm.setStatus("mandatory")
_FalconInput5LowAlarm_Type = ObjectIdentifier
_FalconInput5LowAlarm_Object = MibScalar
falconInput5LowAlarm = _FalconInput5LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 52),
    _FalconInput5LowAlarm_Type()
)
falconInput5LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput5LowAlarm.setStatus("mandatory")
_FalconInput5High2Alarm_Type = ObjectIdentifier
_FalconInput5High2Alarm_Object = MibScalar
falconInput5High2Alarm = _FalconInput5High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 53),
    _FalconInput5High2Alarm_Type()
)
falconInput5High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput5High2Alarm.setStatus("mandatory")
_FalconInput5Low2Alarm_Type = ObjectIdentifier
_FalconInput5Low2Alarm_Object = MibScalar
falconInput5Low2Alarm = _FalconInput5Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 54),
    _FalconInput5Low2Alarm_Type()
)
falconInput5Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput5Low2Alarm.setStatus("mandatory")
_FalconInput6DigAlarm_Type = ObjectIdentifier
_FalconInput6DigAlarm_Object = MibScalar
falconInput6DigAlarm = _FalconInput6DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 60),
    _FalconInput6DigAlarm_Type()
)
falconInput6DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput6DigAlarm.setStatus("mandatory")
_FalconInput6HighAlarm_Type = ObjectIdentifier
_FalconInput6HighAlarm_Object = MibScalar
falconInput6HighAlarm = _FalconInput6HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 61),
    _FalconInput6HighAlarm_Type()
)
falconInput6HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput6HighAlarm.setStatus("mandatory")
_FalconInput6LowAlarm_Type = ObjectIdentifier
_FalconInput6LowAlarm_Object = MibScalar
falconInput6LowAlarm = _FalconInput6LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 62),
    _FalconInput6LowAlarm_Type()
)
falconInput6LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput6LowAlarm.setStatus("mandatory")
_FalconInput6High2Alarm_Type = ObjectIdentifier
_FalconInput6High2Alarm_Object = MibScalar
falconInput6High2Alarm = _FalconInput6High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 63),
    _FalconInput6High2Alarm_Type()
)
falconInput6High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput6High2Alarm.setStatus("mandatory")
_FalconInput6Low2Alarm_Type = ObjectIdentifier
_FalconInput6Low2Alarm_Object = MibScalar
falconInput6Low2Alarm = _FalconInput6Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 64),
    _FalconInput6Low2Alarm_Type()
)
falconInput6Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput6Low2Alarm.setStatus("mandatory")
_FalconInput7DigAlarm_Type = ObjectIdentifier
_FalconInput7DigAlarm_Object = MibScalar
falconInput7DigAlarm = _FalconInput7DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 70),
    _FalconInput7DigAlarm_Type()
)
falconInput7DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput7DigAlarm.setStatus("mandatory")
_FalconInput7HighAlarm_Type = ObjectIdentifier
_FalconInput7HighAlarm_Object = MibScalar
falconInput7HighAlarm = _FalconInput7HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 71),
    _FalconInput7HighAlarm_Type()
)
falconInput7HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput7HighAlarm.setStatus("mandatory")
_FalconInput7LowAlarm_Type = ObjectIdentifier
_FalconInput7LowAlarm_Object = MibScalar
falconInput7LowAlarm = _FalconInput7LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 72),
    _FalconInput7LowAlarm_Type()
)
falconInput7LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput7LowAlarm.setStatus("mandatory")
_FalconInput7High2Alarm_Type = ObjectIdentifier
_FalconInput7High2Alarm_Object = MibScalar
falconInput7High2Alarm = _FalconInput7High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 73),
    _FalconInput7High2Alarm_Type()
)
falconInput7High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput7High2Alarm.setStatus("mandatory")
_FalconInput7Low2Alarm_Type = ObjectIdentifier
_FalconInput7Low2Alarm_Object = MibScalar
falconInput7Low2Alarm = _FalconInput7Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 74),
    _FalconInput7Low2Alarm_Type()
)
falconInput7Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput7Low2Alarm.setStatus("mandatory")
_FalconInput8DigAlarm_Type = ObjectIdentifier
_FalconInput8DigAlarm_Object = MibScalar
falconInput8DigAlarm = _FalconInput8DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 80),
    _FalconInput8DigAlarm_Type()
)
falconInput8DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput8DigAlarm.setStatus("mandatory")
_FalconInput8HighAlarm_Type = ObjectIdentifier
_FalconInput8HighAlarm_Object = MibScalar
falconInput8HighAlarm = _FalconInput8HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 81),
    _FalconInput8HighAlarm_Type()
)
falconInput8HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput8HighAlarm.setStatus("mandatory")
_FalconInput8LowAlarm_Type = ObjectIdentifier
_FalconInput8LowAlarm_Object = MibScalar
falconInput8LowAlarm = _FalconInput8LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 82),
    _FalconInput8LowAlarm_Type()
)
falconInput8LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput8LowAlarm.setStatus("mandatory")
_FalconInput8High2Alarm_Type = ObjectIdentifier
_FalconInput8High2Alarm_Object = MibScalar
falconInput8High2Alarm = _FalconInput8High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 83),
    _FalconInput8High2Alarm_Type()
)
falconInput8High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput8High2Alarm.setStatus("mandatory")
_FalconInput8Low2Alarm_Type = ObjectIdentifier
_FalconInput8Low2Alarm_Object = MibScalar
falconInput8Low2Alarm = _FalconInput8Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 84),
    _FalconInput8Low2Alarm_Type()
)
falconInput8Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput8Low2Alarm.setStatus("mandatory")
_FalconInput9DigAlarm_Type = ObjectIdentifier
_FalconInput9DigAlarm_Object = MibScalar
falconInput9DigAlarm = _FalconInput9DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1010),
    _FalconInput9DigAlarm_Type()
)
falconInput9DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput9DigAlarm.setStatus("mandatory")
_FalconInput9HighAlarm_Type = ObjectIdentifier
_FalconInput9HighAlarm_Object = MibScalar
falconInput9HighAlarm = _FalconInput9HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1011),
    _FalconInput9HighAlarm_Type()
)
falconInput9HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput9HighAlarm.setStatus("mandatory")
_FalconInput9LowAlarm_Type = ObjectIdentifier
_FalconInput9LowAlarm_Object = MibScalar
falconInput9LowAlarm = _FalconInput9LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1012),
    _FalconInput9LowAlarm_Type()
)
falconInput9LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput9LowAlarm.setStatus("mandatory")
_FalconInput9High2Alarm_Type = ObjectIdentifier
_FalconInput9High2Alarm_Object = MibScalar
falconInput9High2Alarm = _FalconInput9High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1013),
    _FalconInput9High2Alarm_Type()
)
falconInput9High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput9High2Alarm.setStatus("mandatory")
_FalconInput9Low2Alarm_Type = ObjectIdentifier
_FalconInput9Low2Alarm_Object = MibScalar
falconInput9Low2Alarm = _FalconInput9Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1014),
    _FalconInput9Low2Alarm_Type()
)
falconInput9Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput9Low2Alarm.setStatus("mandatory")
_FalconInput10DigAlarm_Type = ObjectIdentifier
_FalconInput10DigAlarm_Object = MibScalar
falconInput10DigAlarm = _FalconInput10DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1020),
    _FalconInput10DigAlarm_Type()
)
falconInput10DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput10DigAlarm.setStatus("mandatory")
_FalconInput10HighAlarm_Type = ObjectIdentifier
_FalconInput10HighAlarm_Object = MibScalar
falconInput10HighAlarm = _FalconInput10HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1021),
    _FalconInput10HighAlarm_Type()
)
falconInput10HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput10HighAlarm.setStatus("mandatory")
_FalconInput10LowAlarm_Type = ObjectIdentifier
_FalconInput10LowAlarm_Object = MibScalar
falconInput10LowAlarm = _FalconInput10LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1022),
    _FalconInput10LowAlarm_Type()
)
falconInput10LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput10LowAlarm.setStatus("mandatory")
_FalconInput10High2Alarm_Type = ObjectIdentifier
_FalconInput10High2Alarm_Object = MibScalar
falconInput10High2Alarm = _FalconInput10High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1023),
    _FalconInput10High2Alarm_Type()
)
falconInput10High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput10High2Alarm.setStatus("mandatory")
_FalconInput10Low2Alarm_Type = ObjectIdentifier
_FalconInput10Low2Alarm_Object = MibScalar
falconInput10Low2Alarm = _FalconInput10Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1024),
    _FalconInput10Low2Alarm_Type()
)
falconInput10Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput10Low2Alarm.setStatus("mandatory")
_FalconInput11DigAlarm_Type = ObjectIdentifier
_FalconInput11DigAlarm_Object = MibScalar
falconInput11DigAlarm = _FalconInput11DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1030),
    _FalconInput11DigAlarm_Type()
)
falconInput11DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput11DigAlarm.setStatus("mandatory")
_FalconInput11HighAlarm_Type = ObjectIdentifier
_FalconInput11HighAlarm_Object = MibScalar
falconInput11HighAlarm = _FalconInput11HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1031),
    _FalconInput11HighAlarm_Type()
)
falconInput11HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput11HighAlarm.setStatus("mandatory")
_FalconInput11LowAlarm_Type = ObjectIdentifier
_FalconInput11LowAlarm_Object = MibScalar
falconInput11LowAlarm = _FalconInput11LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1032),
    _FalconInput11LowAlarm_Type()
)
falconInput11LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput11LowAlarm.setStatus("mandatory")
_FalconInput11High2Alarm_Type = ObjectIdentifier
_FalconInput11High2Alarm_Object = MibScalar
falconInput11High2Alarm = _FalconInput11High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1033),
    _FalconInput11High2Alarm_Type()
)
falconInput11High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput11High2Alarm.setStatus("mandatory")
_FalconInput11Low2Alarm_Type = ObjectIdentifier
_FalconInput11Low2Alarm_Object = MibScalar
falconInput11Low2Alarm = _FalconInput11Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1034),
    _FalconInput11Low2Alarm_Type()
)
falconInput11Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput11Low2Alarm.setStatus("mandatory")
_FalconInput12DigAlarm_Type = ObjectIdentifier
_FalconInput12DigAlarm_Object = MibScalar
falconInput12DigAlarm = _FalconInput12DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1040),
    _FalconInput12DigAlarm_Type()
)
falconInput12DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput12DigAlarm.setStatus("mandatory")
_FalconInput12HighAlarm_Type = ObjectIdentifier
_FalconInput12HighAlarm_Object = MibScalar
falconInput12HighAlarm = _FalconInput12HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1041),
    _FalconInput12HighAlarm_Type()
)
falconInput12HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput12HighAlarm.setStatus("mandatory")
_FalconInput12LowAlarm_Type = ObjectIdentifier
_FalconInput12LowAlarm_Object = MibScalar
falconInput12LowAlarm = _FalconInput12LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1042),
    _FalconInput12LowAlarm_Type()
)
falconInput12LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput12LowAlarm.setStatus("mandatory")
_FalconInput12High2Alarm_Type = ObjectIdentifier
_FalconInput12High2Alarm_Object = MibScalar
falconInput12High2Alarm = _FalconInput12High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1043),
    _FalconInput12High2Alarm_Type()
)
falconInput12High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput12High2Alarm.setStatus("mandatory")
_FalconInput12Low2Alarm_Type = ObjectIdentifier
_FalconInput12Low2Alarm_Object = MibScalar
falconInput12Low2Alarm = _FalconInput12Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1044),
    _FalconInput12Low2Alarm_Type()
)
falconInput12Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput12Low2Alarm.setStatus("mandatory")
_FalconInput13DigAlarm_Type = ObjectIdentifier
_FalconInput13DigAlarm_Object = MibScalar
falconInput13DigAlarm = _FalconInput13DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1050),
    _FalconInput13DigAlarm_Type()
)
falconInput13DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput13DigAlarm.setStatus("mandatory")
_FalconInput13HighAlarm_Type = ObjectIdentifier
_FalconInput13HighAlarm_Object = MibScalar
falconInput13HighAlarm = _FalconInput13HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1051),
    _FalconInput13HighAlarm_Type()
)
falconInput13HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput13HighAlarm.setStatus("mandatory")
_FalconInput13LowAlarm_Type = ObjectIdentifier
_FalconInput13LowAlarm_Object = MibScalar
falconInput13LowAlarm = _FalconInput13LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1052),
    _FalconInput13LowAlarm_Type()
)
falconInput13LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput13LowAlarm.setStatus("mandatory")
_FalconInput13High2Alarm_Type = ObjectIdentifier
_FalconInput13High2Alarm_Object = MibScalar
falconInput13High2Alarm = _FalconInput13High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1053),
    _FalconInput13High2Alarm_Type()
)
falconInput13High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput13High2Alarm.setStatus("mandatory")
_FalconInput13Low2Alarm_Type = ObjectIdentifier
_FalconInput13Low2Alarm_Object = MibScalar
falconInput13Low2Alarm = _FalconInput13Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1054),
    _FalconInput13Low2Alarm_Type()
)
falconInput13Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput13Low2Alarm.setStatus("mandatory")
_FalconInput14DigAlarm_Type = ObjectIdentifier
_FalconInput14DigAlarm_Object = MibScalar
falconInput14DigAlarm = _FalconInput14DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1060),
    _FalconInput14DigAlarm_Type()
)
falconInput14DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput14DigAlarm.setStatus("mandatory")
_FalconInput14HighAlarm_Type = ObjectIdentifier
_FalconInput14HighAlarm_Object = MibScalar
falconInput14HighAlarm = _FalconInput14HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1061),
    _FalconInput14HighAlarm_Type()
)
falconInput14HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput14HighAlarm.setStatus("mandatory")
_FalconInput14LowAlarm_Type = ObjectIdentifier
_FalconInput14LowAlarm_Object = MibScalar
falconInput14LowAlarm = _FalconInput14LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1062),
    _FalconInput14LowAlarm_Type()
)
falconInput14LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput14LowAlarm.setStatus("mandatory")
_FalconInput14High2Alarm_Type = ObjectIdentifier
_FalconInput14High2Alarm_Object = MibScalar
falconInput14High2Alarm = _FalconInput14High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1063),
    _FalconInput14High2Alarm_Type()
)
falconInput14High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput14High2Alarm.setStatus("mandatory")
_FalconInput14Low2Alarm_Type = ObjectIdentifier
_FalconInput14Low2Alarm_Object = MibScalar
falconInput14Low2Alarm = _FalconInput14Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1064),
    _FalconInput14Low2Alarm_Type()
)
falconInput14Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput14Low2Alarm.setStatus("mandatory")
_FalconInput15DigAlarm_Type = ObjectIdentifier
_FalconInput15DigAlarm_Object = MibScalar
falconInput15DigAlarm = _FalconInput15DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1070),
    _FalconInput15DigAlarm_Type()
)
falconInput15DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput15DigAlarm.setStatus("mandatory")
_FalconInput15HighAlarm_Type = ObjectIdentifier
_FalconInput15HighAlarm_Object = MibScalar
falconInput15HighAlarm = _FalconInput15HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1071),
    _FalconInput15HighAlarm_Type()
)
falconInput15HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput15HighAlarm.setStatus("mandatory")
_FalconInput15LowAlarm_Type = ObjectIdentifier
_FalconInput15LowAlarm_Object = MibScalar
falconInput15LowAlarm = _FalconInput15LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1072),
    _FalconInput15LowAlarm_Type()
)
falconInput15LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput15LowAlarm.setStatus("mandatory")
_FalconInput15High2Alarm_Type = ObjectIdentifier
_FalconInput15High2Alarm_Object = MibScalar
falconInput15High2Alarm = _FalconInput15High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1073),
    _FalconInput15High2Alarm_Type()
)
falconInput15High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput15High2Alarm.setStatus("mandatory")
_FalconInput15Low2Alarm_Type = ObjectIdentifier
_FalconInput15Low2Alarm_Object = MibScalar
falconInput15Low2Alarm = _FalconInput15Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1074),
    _FalconInput15Low2Alarm_Type()
)
falconInput15Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput15Low2Alarm.setStatus("mandatory")
_FalconInput16DigAlarm_Type = ObjectIdentifier
_FalconInput16DigAlarm_Object = MibScalar
falconInput16DigAlarm = _FalconInput16DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1080),
    _FalconInput16DigAlarm_Type()
)
falconInput16DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput16DigAlarm.setStatus("mandatory")
_FalconInput16HighAlarm_Type = ObjectIdentifier
_FalconInput16HighAlarm_Object = MibScalar
falconInput16HighAlarm = _FalconInput16HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1081),
    _FalconInput16HighAlarm_Type()
)
falconInput16HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput16HighAlarm.setStatus("mandatory")
_FalconInput16LowAlarm_Type = ObjectIdentifier
_FalconInput16LowAlarm_Object = MibScalar
falconInput16LowAlarm = _FalconInput16LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1082),
    _FalconInput16LowAlarm_Type()
)
falconInput16LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput16LowAlarm.setStatus("mandatory")
_FalconInput16High2Alarm_Type = ObjectIdentifier
_FalconInput16High2Alarm_Object = MibScalar
falconInput16High2Alarm = _FalconInput16High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1083),
    _FalconInput16High2Alarm_Type()
)
falconInput16High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput16High2Alarm.setStatus("mandatory")
_FalconInput16Low2Alarm_Type = ObjectIdentifier
_FalconInput16Low2Alarm_Object = MibScalar
falconInput16Low2Alarm = _FalconInput16Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1084),
    _FalconInput16Low2Alarm_Type()
)
falconInput16Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput16Low2Alarm.setStatus("mandatory")
_FalconInput17DigAlarm_Type = ObjectIdentifier
_FalconInput17DigAlarm_Object = MibScalar
falconInput17DigAlarm = _FalconInput17DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1090),
    _FalconInput17DigAlarm_Type()
)
falconInput17DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput17DigAlarm.setStatus("mandatory")
_FalconInput17HighAlarm_Type = ObjectIdentifier
_FalconInput17HighAlarm_Object = MibScalar
falconInput17HighAlarm = _FalconInput17HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1091),
    _FalconInput17HighAlarm_Type()
)
falconInput17HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput17HighAlarm.setStatus("mandatory")
_FalconInput17LowAlarm_Type = ObjectIdentifier
_FalconInput17LowAlarm_Object = MibScalar
falconInput17LowAlarm = _FalconInput17LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1092),
    _FalconInput17LowAlarm_Type()
)
falconInput17LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput17LowAlarm.setStatus("mandatory")
_FalconInput17High2Alarm_Type = ObjectIdentifier
_FalconInput17High2Alarm_Object = MibScalar
falconInput17High2Alarm = _FalconInput17High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1093),
    _FalconInput17High2Alarm_Type()
)
falconInput17High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput17High2Alarm.setStatus("mandatory")
_FalconInput17Low2Alarm_Type = ObjectIdentifier
_FalconInput17Low2Alarm_Object = MibScalar
falconInput17Low2Alarm = _FalconInput17Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1094),
    _FalconInput17Low2Alarm_Type()
)
falconInput17Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput17Low2Alarm.setStatus("mandatory")
_FalconInput18DigAlarm_Type = ObjectIdentifier
_FalconInput18DigAlarm_Object = MibScalar
falconInput18DigAlarm = _FalconInput18DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1100),
    _FalconInput18DigAlarm_Type()
)
falconInput18DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput18DigAlarm.setStatus("mandatory")
_FalconInput18HighAlarm_Type = ObjectIdentifier
_FalconInput18HighAlarm_Object = MibScalar
falconInput18HighAlarm = _FalconInput18HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1101),
    _FalconInput18HighAlarm_Type()
)
falconInput18HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput18HighAlarm.setStatus("mandatory")
_FalconInput18LowAlarm_Type = ObjectIdentifier
_FalconInput18LowAlarm_Object = MibScalar
falconInput18LowAlarm = _FalconInput18LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1102),
    _FalconInput18LowAlarm_Type()
)
falconInput18LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput18LowAlarm.setStatus("mandatory")
_FalconInput18High2Alarm_Type = ObjectIdentifier
_FalconInput18High2Alarm_Object = MibScalar
falconInput18High2Alarm = _FalconInput18High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1103),
    _FalconInput18High2Alarm_Type()
)
falconInput18High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput18High2Alarm.setStatus("mandatory")
_FalconInput18Low2Alarm_Type = ObjectIdentifier
_FalconInput18Low2Alarm_Object = MibScalar
falconInput18Low2Alarm = _FalconInput18Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1104),
    _FalconInput18Low2Alarm_Type()
)
falconInput18Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput18Low2Alarm.setStatus("mandatory")
_FalconInput19DigAlarm_Type = ObjectIdentifier
_FalconInput19DigAlarm_Object = MibScalar
falconInput19DigAlarm = _FalconInput19DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1110),
    _FalconInput19DigAlarm_Type()
)
falconInput19DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput19DigAlarm.setStatus("mandatory")
_FalconInput19HighAlarm_Type = ObjectIdentifier
_FalconInput19HighAlarm_Object = MibScalar
falconInput19HighAlarm = _FalconInput19HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1111),
    _FalconInput19HighAlarm_Type()
)
falconInput19HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput19HighAlarm.setStatus("mandatory")
_FalconInput19LowAlarm_Type = ObjectIdentifier
_FalconInput19LowAlarm_Object = MibScalar
falconInput19LowAlarm = _FalconInput19LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1112),
    _FalconInput19LowAlarm_Type()
)
falconInput19LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput19LowAlarm.setStatus("mandatory")
_FalconInput19High2Alarm_Type = ObjectIdentifier
_FalconInput19High2Alarm_Object = MibScalar
falconInput19High2Alarm = _FalconInput19High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1113),
    _FalconInput19High2Alarm_Type()
)
falconInput19High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput19High2Alarm.setStatus("mandatory")
_FalconInput19Low2Alarm_Type = ObjectIdentifier
_FalconInput19Low2Alarm_Object = MibScalar
falconInput19Low2Alarm = _FalconInput19Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1114),
    _FalconInput19Low2Alarm_Type()
)
falconInput19Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput19Low2Alarm.setStatus("mandatory")
_FalconInput20DigAlarm_Type = ObjectIdentifier
_FalconInput20DigAlarm_Object = MibScalar
falconInput20DigAlarm = _FalconInput20DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1120),
    _FalconInput20DigAlarm_Type()
)
falconInput20DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput20DigAlarm.setStatus("mandatory")
_FalconInput20HighAlarm_Type = ObjectIdentifier
_FalconInput20HighAlarm_Object = MibScalar
falconInput20HighAlarm = _FalconInput20HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1121),
    _FalconInput20HighAlarm_Type()
)
falconInput20HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput20HighAlarm.setStatus("mandatory")
_FalconInput20LowAlarm_Type = ObjectIdentifier
_FalconInput20LowAlarm_Object = MibScalar
falconInput20LowAlarm = _FalconInput20LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1122),
    _FalconInput20LowAlarm_Type()
)
falconInput20LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput20LowAlarm.setStatus("mandatory")
_FalconInput20High2Alarm_Type = ObjectIdentifier
_FalconInput20High2Alarm_Object = MibScalar
falconInput20High2Alarm = _FalconInput20High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1123),
    _FalconInput20High2Alarm_Type()
)
falconInput20High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput20High2Alarm.setStatus("mandatory")
_FalconInput20Low2Alarm_Type = ObjectIdentifier
_FalconInput20Low2Alarm_Object = MibScalar
falconInput20Low2Alarm = _FalconInput20Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1124),
    _FalconInput20Low2Alarm_Type()
)
falconInput20Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput20Low2Alarm.setStatus("mandatory")
_FalconInput21DigAlarm_Type = ObjectIdentifier
_FalconInput21DigAlarm_Object = MibScalar
falconInput21DigAlarm = _FalconInput21DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1130),
    _FalconInput21DigAlarm_Type()
)
falconInput21DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput21DigAlarm.setStatus("mandatory")
_FalconInput22DigAlarm_Type = ObjectIdentifier
_FalconInput22DigAlarm_Object = MibScalar
falconInput22DigAlarm = _FalconInput22DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1140),
    _FalconInput22DigAlarm_Type()
)
falconInput22DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput22DigAlarm.setStatus("mandatory")
_FalconInput23DigAlarm_Type = ObjectIdentifier
_FalconInput23DigAlarm_Object = MibScalar
falconInput23DigAlarm = _FalconInput23DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1150),
    _FalconInput23DigAlarm_Type()
)
falconInput23DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput23DigAlarm.setStatus("mandatory")
_FalconInput24DigAlarm_Type = ObjectIdentifier
_FalconInput24DigAlarm_Object = MibScalar
falconInput24DigAlarm = _FalconInput24DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1160),
    _FalconInput24DigAlarm_Type()
)
falconInput24DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput24DigAlarm.setStatus("mandatory")
_FalconInput25DigAlarm_Type = ObjectIdentifier
_FalconInput25DigAlarm_Object = MibScalar
falconInput25DigAlarm = _FalconInput25DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1170),
    _FalconInput25DigAlarm_Type()
)
falconInput25DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput25DigAlarm.setStatus("mandatory")
_FalconInput26DigAlarm_Type = ObjectIdentifier
_FalconInput26DigAlarm_Object = MibScalar
falconInput26DigAlarm = _FalconInput26DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1180),
    _FalconInput26DigAlarm_Type()
)
falconInput26DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput26DigAlarm.setStatus("mandatory")
_FalconInput27DigAlarm_Type = ObjectIdentifier
_FalconInput27DigAlarm_Object = MibScalar
falconInput27DigAlarm = _FalconInput27DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1190),
    _FalconInput27DigAlarm_Type()
)
falconInput27DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput27DigAlarm.setStatus("mandatory")
_FalconInput28DigAlarm_Type = ObjectIdentifier
_FalconInput28DigAlarm_Object = MibScalar
falconInput28DigAlarm = _FalconInput28DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1200),
    _FalconInput28DigAlarm_Type()
)
falconInput28DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput28DigAlarm.setStatus("mandatory")
_FalconInput29DigAlarm_Type = ObjectIdentifier
_FalconInput29DigAlarm_Object = MibScalar
falconInput29DigAlarm = _FalconInput29DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1210),
    _FalconInput29DigAlarm_Type()
)
falconInput29DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput29DigAlarm.setStatus("mandatory")
_FalconInput30DigAlarm_Type = ObjectIdentifier
_FalconInput30DigAlarm_Object = MibScalar
falconInput30DigAlarm = _FalconInput30DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1220),
    _FalconInput30DigAlarm_Type()
)
falconInput30DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput30DigAlarm.setStatus("mandatory")
_FalconInput31DigAlarm_Type = ObjectIdentifier
_FalconInput31DigAlarm_Object = MibScalar
falconInput31DigAlarm = _FalconInput31DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1230),
    _FalconInput31DigAlarm_Type()
)
falconInput31DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput31DigAlarm.setStatus("mandatory")
_FalconInput32DigAlarm_Type = ObjectIdentifier
_FalconInput32DigAlarm_Object = MibScalar
falconInput32DigAlarm = _FalconInput32DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 1240),
    _FalconInput32DigAlarm_Type()
)
falconInput32DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput32DigAlarm.setStatus("mandatory")
_FalconInput33DigAlarm_Type = ObjectIdentifier
_FalconInput33DigAlarm_Object = MibScalar
falconInput33DigAlarm = _FalconInput33DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2010),
    _FalconInput33DigAlarm_Type()
)
falconInput33DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput33DigAlarm.setStatus("mandatory")
_FalconInput33HighAlarm_Type = ObjectIdentifier
_FalconInput33HighAlarm_Object = MibScalar
falconInput33HighAlarm = _FalconInput33HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2011),
    _FalconInput33HighAlarm_Type()
)
falconInput33HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput33HighAlarm.setStatus("mandatory")
_FalconInput33LowAlarm_Type = ObjectIdentifier
_FalconInput33LowAlarm_Object = MibScalar
falconInput33LowAlarm = _FalconInput33LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2012),
    _FalconInput33LowAlarm_Type()
)
falconInput33LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput33LowAlarm.setStatus("mandatory")
_FalconInput33High2Alarm_Type = ObjectIdentifier
_FalconInput33High2Alarm_Object = MibScalar
falconInput33High2Alarm = _FalconInput33High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2013),
    _FalconInput33High2Alarm_Type()
)
falconInput33High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput33High2Alarm.setStatus("mandatory")
_FalconInput33Low2Alarm_Type = ObjectIdentifier
_FalconInput33Low2Alarm_Object = MibScalar
falconInput33Low2Alarm = _FalconInput33Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2014),
    _FalconInput33Low2Alarm_Type()
)
falconInput33Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput33Low2Alarm.setStatus("mandatory")
_FalconInput34DigAlarm_Type = ObjectIdentifier
_FalconInput34DigAlarm_Object = MibScalar
falconInput34DigAlarm = _FalconInput34DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2020),
    _FalconInput34DigAlarm_Type()
)
falconInput34DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput34DigAlarm.setStatus("mandatory")
_FalconInput34HighAlarm_Type = ObjectIdentifier
_FalconInput34HighAlarm_Object = MibScalar
falconInput34HighAlarm = _FalconInput34HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2021),
    _FalconInput34HighAlarm_Type()
)
falconInput34HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput34HighAlarm.setStatus("mandatory")
_FalconInput34LowAlarm_Type = ObjectIdentifier
_FalconInput34LowAlarm_Object = MibScalar
falconInput34LowAlarm = _FalconInput34LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2022),
    _FalconInput34LowAlarm_Type()
)
falconInput34LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput34LowAlarm.setStatus("mandatory")
_FalconInput34High2Alarm_Type = ObjectIdentifier
_FalconInput34High2Alarm_Object = MibScalar
falconInput34High2Alarm = _FalconInput34High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2023),
    _FalconInput34High2Alarm_Type()
)
falconInput34High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput34High2Alarm.setStatus("mandatory")
_FalconInput34Low2Alarm_Type = ObjectIdentifier
_FalconInput34Low2Alarm_Object = MibScalar
falconInput34Low2Alarm = _FalconInput34Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2024),
    _FalconInput34Low2Alarm_Type()
)
falconInput34Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput34Low2Alarm.setStatus("mandatory")
_FalconInput35DigAlarm_Type = ObjectIdentifier
_FalconInput35DigAlarm_Object = MibScalar
falconInput35DigAlarm = _FalconInput35DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2030),
    _FalconInput35DigAlarm_Type()
)
falconInput35DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput35DigAlarm.setStatus("mandatory")
_FalconInput35HighAlarm_Type = ObjectIdentifier
_FalconInput35HighAlarm_Object = MibScalar
falconInput35HighAlarm = _FalconInput35HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2031),
    _FalconInput35HighAlarm_Type()
)
falconInput35HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput35HighAlarm.setStatus("mandatory")
_FalconInput35LowAlarm_Type = ObjectIdentifier
_FalconInput35LowAlarm_Object = MibScalar
falconInput35LowAlarm = _FalconInput35LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2032),
    _FalconInput35LowAlarm_Type()
)
falconInput35LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput35LowAlarm.setStatus("mandatory")
_FalconInput35High2Alarm_Type = ObjectIdentifier
_FalconInput35High2Alarm_Object = MibScalar
falconInput35High2Alarm = _FalconInput35High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2033),
    _FalconInput35High2Alarm_Type()
)
falconInput35High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput35High2Alarm.setStatus("mandatory")
_FalconInput35Low2Alarm_Type = ObjectIdentifier
_FalconInput35Low2Alarm_Object = MibScalar
falconInput35Low2Alarm = _FalconInput35Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2034),
    _FalconInput35Low2Alarm_Type()
)
falconInput35Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput35Low2Alarm.setStatus("mandatory")
_FalconInput36DigAlarm_Type = ObjectIdentifier
_FalconInput36DigAlarm_Object = MibScalar
falconInput36DigAlarm = _FalconInput36DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2040),
    _FalconInput36DigAlarm_Type()
)
falconInput36DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput36DigAlarm.setStatus("mandatory")
_FalconInput36HighAlarm_Type = ObjectIdentifier
_FalconInput36HighAlarm_Object = MibScalar
falconInput36HighAlarm = _FalconInput36HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2041),
    _FalconInput36HighAlarm_Type()
)
falconInput36HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput36HighAlarm.setStatus("mandatory")
_FalconInput36LowAlarm_Type = ObjectIdentifier
_FalconInput36LowAlarm_Object = MibScalar
falconInput36LowAlarm = _FalconInput36LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2042),
    _FalconInput36LowAlarm_Type()
)
falconInput36LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput36LowAlarm.setStatus("mandatory")
_FalconInput36High2Alarm_Type = ObjectIdentifier
_FalconInput36High2Alarm_Object = MibScalar
falconInput36High2Alarm = _FalconInput36High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2043),
    _FalconInput36High2Alarm_Type()
)
falconInput36High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput36High2Alarm.setStatus("mandatory")
_FalconInput36Low2Alarm_Type = ObjectIdentifier
_FalconInput36Low2Alarm_Object = MibScalar
falconInput36Low2Alarm = _FalconInput36Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2044),
    _FalconInput36Low2Alarm_Type()
)
falconInput36Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput36Low2Alarm.setStatus("mandatory")
_FalconInput37DigAlarm_Type = ObjectIdentifier
_FalconInput37DigAlarm_Object = MibScalar
falconInput37DigAlarm = _FalconInput37DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2050),
    _FalconInput37DigAlarm_Type()
)
falconInput37DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput37DigAlarm.setStatus("mandatory")
_FalconInput37HighAlarm_Type = ObjectIdentifier
_FalconInput37HighAlarm_Object = MibScalar
falconInput37HighAlarm = _FalconInput37HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2051),
    _FalconInput37HighAlarm_Type()
)
falconInput37HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput37HighAlarm.setStatus("mandatory")
_FalconInput37LowAlarm_Type = ObjectIdentifier
_FalconInput37LowAlarm_Object = MibScalar
falconInput37LowAlarm = _FalconInput37LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2052),
    _FalconInput37LowAlarm_Type()
)
falconInput37LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput37LowAlarm.setStatus("mandatory")
_FalconInput37High2Alarm_Type = ObjectIdentifier
_FalconInput37High2Alarm_Object = MibScalar
falconInput37High2Alarm = _FalconInput37High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2053),
    _FalconInput37High2Alarm_Type()
)
falconInput37High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput37High2Alarm.setStatus("mandatory")
_FalconInput37Low2Alarm_Type = ObjectIdentifier
_FalconInput37Low2Alarm_Object = MibScalar
falconInput37Low2Alarm = _FalconInput37Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2054),
    _FalconInput37Low2Alarm_Type()
)
falconInput37Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput37Low2Alarm.setStatus("mandatory")
_FalconInput38DigAlarm_Type = ObjectIdentifier
_FalconInput38DigAlarm_Object = MibScalar
falconInput38DigAlarm = _FalconInput38DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2060),
    _FalconInput38DigAlarm_Type()
)
falconInput38DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput38DigAlarm.setStatus("mandatory")
_FalconInput38HighAlarm_Type = ObjectIdentifier
_FalconInput38HighAlarm_Object = MibScalar
falconInput38HighAlarm = _FalconInput38HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2061),
    _FalconInput38HighAlarm_Type()
)
falconInput38HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput38HighAlarm.setStatus("mandatory")
_FalconInput38LowAlarm_Type = ObjectIdentifier
_FalconInput38LowAlarm_Object = MibScalar
falconInput38LowAlarm = _FalconInput38LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2062),
    _FalconInput38LowAlarm_Type()
)
falconInput38LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput38LowAlarm.setStatus("mandatory")
_FalconInput38High2Alarm_Type = ObjectIdentifier
_FalconInput38High2Alarm_Object = MibScalar
falconInput38High2Alarm = _FalconInput38High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2063),
    _FalconInput38High2Alarm_Type()
)
falconInput38High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput38High2Alarm.setStatus("mandatory")
_FalconInput38Low2Alarm_Type = ObjectIdentifier
_FalconInput38Low2Alarm_Object = MibScalar
falconInput38Low2Alarm = _FalconInput38Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2064),
    _FalconInput38Low2Alarm_Type()
)
falconInput38Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput38Low2Alarm.setStatus("mandatory")
_FalconInput39DigAlarm_Type = ObjectIdentifier
_FalconInput39DigAlarm_Object = MibScalar
falconInput39DigAlarm = _FalconInput39DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2070),
    _FalconInput39DigAlarm_Type()
)
falconInput39DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput39DigAlarm.setStatus("mandatory")
_FalconInput39HighAlarm_Type = ObjectIdentifier
_FalconInput39HighAlarm_Object = MibScalar
falconInput39HighAlarm = _FalconInput39HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2071),
    _FalconInput39HighAlarm_Type()
)
falconInput39HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput39HighAlarm.setStatus("mandatory")
_FalconInput39LowAlarm_Type = ObjectIdentifier
_FalconInput39LowAlarm_Object = MibScalar
falconInput39LowAlarm = _FalconInput39LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2072),
    _FalconInput39LowAlarm_Type()
)
falconInput39LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput39LowAlarm.setStatus("mandatory")
_FalconInput39High2Alarm_Type = ObjectIdentifier
_FalconInput39High2Alarm_Object = MibScalar
falconInput39High2Alarm = _FalconInput39High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2073),
    _FalconInput39High2Alarm_Type()
)
falconInput39High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput39High2Alarm.setStatus("mandatory")
_FalconInput39Low2Alarm_Type = ObjectIdentifier
_FalconInput39Low2Alarm_Object = MibScalar
falconInput39Low2Alarm = _FalconInput39Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2074),
    _FalconInput39Low2Alarm_Type()
)
falconInput39Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput39Low2Alarm.setStatus("mandatory")
_FalconInput40DigAlarm_Type = ObjectIdentifier
_FalconInput40DigAlarm_Object = MibScalar
falconInput40DigAlarm = _FalconInput40DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2080),
    _FalconInput40DigAlarm_Type()
)
falconInput40DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput40DigAlarm.setStatus("mandatory")
_FalconInput40HighAlarm_Type = ObjectIdentifier
_FalconInput40HighAlarm_Object = MibScalar
falconInput40HighAlarm = _FalconInput40HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2081),
    _FalconInput40HighAlarm_Type()
)
falconInput40HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput40HighAlarm.setStatus("mandatory")
_FalconInput40LowAlarm_Type = ObjectIdentifier
_FalconInput40LowAlarm_Object = MibScalar
falconInput40LowAlarm = _FalconInput40LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2082),
    _FalconInput40LowAlarm_Type()
)
falconInput40LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput40LowAlarm.setStatus("mandatory")
_FalconInput40High2Alarm_Type = ObjectIdentifier
_FalconInput40High2Alarm_Object = MibScalar
falconInput40High2Alarm = _FalconInput40High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2083),
    _FalconInput40High2Alarm_Type()
)
falconInput40High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput40High2Alarm.setStatus("mandatory")
_FalconInput40Low2Alarm_Type = ObjectIdentifier
_FalconInput40Low2Alarm_Object = MibScalar
falconInput40Low2Alarm = _FalconInput40Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2084),
    _FalconInput40Low2Alarm_Type()
)
falconInput40Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput40Low2Alarm.setStatus("mandatory")
_FalconInput41DigAlarm_Type = ObjectIdentifier
_FalconInput41DigAlarm_Object = MibScalar
falconInput41DigAlarm = _FalconInput41DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2090),
    _FalconInput41DigAlarm_Type()
)
falconInput41DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput41DigAlarm.setStatus("mandatory")
_FalconInput41HighAlarm_Type = ObjectIdentifier
_FalconInput41HighAlarm_Object = MibScalar
falconInput41HighAlarm = _FalconInput41HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2091),
    _FalconInput41HighAlarm_Type()
)
falconInput41HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput41HighAlarm.setStatus("mandatory")
_FalconInput41LowAlarm_Type = ObjectIdentifier
_FalconInput41LowAlarm_Object = MibScalar
falconInput41LowAlarm = _FalconInput41LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2092),
    _FalconInput41LowAlarm_Type()
)
falconInput41LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput41LowAlarm.setStatus("mandatory")
_FalconInput41High2Alarm_Type = ObjectIdentifier
_FalconInput41High2Alarm_Object = MibScalar
falconInput41High2Alarm = _FalconInput41High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2093),
    _FalconInput41High2Alarm_Type()
)
falconInput41High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput41High2Alarm.setStatus("mandatory")
_FalconInput41Low2Alarm_Type = ObjectIdentifier
_FalconInput41Low2Alarm_Object = MibScalar
falconInput41Low2Alarm = _FalconInput41Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2094),
    _FalconInput41Low2Alarm_Type()
)
falconInput41Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput41Low2Alarm.setStatus("mandatory")
_FalconInput42DigAlarm_Type = ObjectIdentifier
_FalconInput42DigAlarm_Object = MibScalar
falconInput42DigAlarm = _FalconInput42DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2100),
    _FalconInput42DigAlarm_Type()
)
falconInput42DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput42DigAlarm.setStatus("mandatory")
_FalconInput42HighAlarm_Type = ObjectIdentifier
_FalconInput42HighAlarm_Object = MibScalar
falconInput42HighAlarm = _FalconInput42HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2101),
    _FalconInput42HighAlarm_Type()
)
falconInput42HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput42HighAlarm.setStatus("mandatory")
_FalconInput42LowAlarm_Type = ObjectIdentifier
_FalconInput42LowAlarm_Object = MibScalar
falconInput42LowAlarm = _FalconInput42LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2102),
    _FalconInput42LowAlarm_Type()
)
falconInput42LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput42LowAlarm.setStatus("mandatory")
_FalconInput42High2Alarm_Type = ObjectIdentifier
_FalconInput42High2Alarm_Object = MibScalar
falconInput42High2Alarm = _FalconInput42High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2103),
    _FalconInput42High2Alarm_Type()
)
falconInput42High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput42High2Alarm.setStatus("mandatory")
_FalconInput42Low2Alarm_Type = ObjectIdentifier
_FalconInput42Low2Alarm_Object = MibScalar
falconInput42Low2Alarm = _FalconInput42Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2104),
    _FalconInput42Low2Alarm_Type()
)
falconInput42Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput42Low2Alarm.setStatus("mandatory")
_FalconInput43DigAlarm_Type = ObjectIdentifier
_FalconInput43DigAlarm_Object = MibScalar
falconInput43DigAlarm = _FalconInput43DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2110),
    _FalconInput43DigAlarm_Type()
)
falconInput43DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput43DigAlarm.setStatus("mandatory")
_FalconInput43HighAlarm_Type = ObjectIdentifier
_FalconInput43HighAlarm_Object = MibScalar
falconInput43HighAlarm = _FalconInput43HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2111),
    _FalconInput43HighAlarm_Type()
)
falconInput43HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput43HighAlarm.setStatus("mandatory")
_FalconInput43LowAlarm_Type = ObjectIdentifier
_FalconInput43LowAlarm_Object = MibScalar
falconInput43LowAlarm = _FalconInput43LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2112),
    _FalconInput43LowAlarm_Type()
)
falconInput43LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput43LowAlarm.setStatus("mandatory")
_FalconInput43High2Alarm_Type = ObjectIdentifier
_FalconInput43High2Alarm_Object = MibScalar
falconInput43High2Alarm = _FalconInput43High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2113),
    _FalconInput43High2Alarm_Type()
)
falconInput43High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput43High2Alarm.setStatus("mandatory")
_FalconInput43Low2Alarm_Type = ObjectIdentifier
_FalconInput43Low2Alarm_Object = MibScalar
falconInput43Low2Alarm = _FalconInput43Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2114),
    _FalconInput43Low2Alarm_Type()
)
falconInput43Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput43Low2Alarm.setStatus("mandatory")
_FalconInput44DigAlarm_Type = ObjectIdentifier
_FalconInput44DigAlarm_Object = MibScalar
falconInput44DigAlarm = _FalconInput44DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2120),
    _FalconInput44DigAlarm_Type()
)
falconInput44DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput44DigAlarm.setStatus("mandatory")
_FalconInput44HighAlarm_Type = ObjectIdentifier
_FalconInput44HighAlarm_Object = MibScalar
falconInput44HighAlarm = _FalconInput44HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2121),
    _FalconInput44HighAlarm_Type()
)
falconInput44HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput44HighAlarm.setStatus("mandatory")
_FalconInput44LowAlarm_Type = ObjectIdentifier
_FalconInput44LowAlarm_Object = MibScalar
falconInput44LowAlarm = _FalconInput44LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2122),
    _FalconInput44LowAlarm_Type()
)
falconInput44LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput44LowAlarm.setStatus("mandatory")
_FalconInput44High2Alarm_Type = ObjectIdentifier
_FalconInput44High2Alarm_Object = MibScalar
falconInput44High2Alarm = _FalconInput44High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2123),
    _FalconInput44High2Alarm_Type()
)
falconInput44High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput44High2Alarm.setStatus("mandatory")
_FalconInput44Low2Alarm_Type = ObjectIdentifier
_FalconInput44Low2Alarm_Object = MibScalar
falconInput44Low2Alarm = _FalconInput44Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2124),
    _FalconInput44Low2Alarm_Type()
)
falconInput44Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput44Low2Alarm.setStatus("mandatory")
_FalconInput45DigAlarm_Type = ObjectIdentifier
_FalconInput45DigAlarm_Object = MibScalar
falconInput45DigAlarm = _FalconInput45DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2130),
    _FalconInput45DigAlarm_Type()
)
falconInput45DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput45DigAlarm.setStatus("mandatory")
_FalconInput46DigAlarm_Type = ObjectIdentifier
_FalconInput46DigAlarm_Object = MibScalar
falconInput46DigAlarm = _FalconInput46DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2140),
    _FalconInput46DigAlarm_Type()
)
falconInput46DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput46DigAlarm.setStatus("mandatory")
_FalconInput47DigAlarm_Type = ObjectIdentifier
_FalconInput47DigAlarm_Object = MibScalar
falconInput47DigAlarm = _FalconInput47DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2150),
    _FalconInput47DigAlarm_Type()
)
falconInput47DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput47DigAlarm.setStatus("mandatory")
_FalconInput48DigAlarm_Type = ObjectIdentifier
_FalconInput48DigAlarm_Object = MibScalar
falconInput48DigAlarm = _FalconInput48DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2160),
    _FalconInput48DigAlarm_Type()
)
falconInput48DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput48DigAlarm.setStatus("mandatory")
_FalconInput49DigAlarm_Type = ObjectIdentifier
_FalconInput49DigAlarm_Object = MibScalar
falconInput49DigAlarm = _FalconInput49DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2170),
    _FalconInput49DigAlarm_Type()
)
falconInput49DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput49DigAlarm.setStatus("mandatory")
_FalconInput50DigAlarm_Type = ObjectIdentifier
_FalconInput50DigAlarm_Object = MibScalar
falconInput50DigAlarm = _FalconInput50DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2180),
    _FalconInput50DigAlarm_Type()
)
falconInput50DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput50DigAlarm.setStatus("mandatory")
_FalconInput51DigAlarm_Type = ObjectIdentifier
_FalconInput51DigAlarm_Object = MibScalar
falconInput51DigAlarm = _FalconInput51DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2190),
    _FalconInput51DigAlarm_Type()
)
falconInput51DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput51DigAlarm.setStatus("mandatory")
_FalconInput52DigAlarm_Type = ObjectIdentifier
_FalconInput52DigAlarm_Object = MibScalar
falconInput52DigAlarm = _FalconInput52DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2200),
    _FalconInput52DigAlarm_Type()
)
falconInput52DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput52DigAlarm.setStatus("mandatory")
_FalconInput53DigAlarm_Type = ObjectIdentifier
_FalconInput53DigAlarm_Object = MibScalar
falconInput53DigAlarm = _FalconInput53DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2210),
    _FalconInput53DigAlarm_Type()
)
falconInput53DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput53DigAlarm.setStatus("mandatory")
_FalconInput54DigAlarm_Type = ObjectIdentifier
_FalconInput54DigAlarm_Object = MibScalar
falconInput54DigAlarm = _FalconInput54DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2220),
    _FalconInput54DigAlarm_Type()
)
falconInput54DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput54DigAlarm.setStatus("mandatory")
_FalconInput55DigAlarm_Type = ObjectIdentifier
_FalconInput55DigAlarm_Object = MibScalar
falconInput55DigAlarm = _FalconInput55DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2230),
    _FalconInput55DigAlarm_Type()
)
falconInput55DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput55DigAlarm.setStatus("mandatory")
_FalconInput56DigAlarm_Type = ObjectIdentifier
_FalconInput56DigAlarm_Object = MibScalar
falconInput56DigAlarm = _FalconInput56DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 2240),
    _FalconInput56DigAlarm_Type()
)
falconInput56DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput56DigAlarm.setStatus("mandatory")
_FalconInput57DigAlarm_Type = ObjectIdentifier
_FalconInput57DigAlarm_Object = MibScalar
falconInput57DigAlarm = _FalconInput57DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3010),
    _FalconInput57DigAlarm_Type()
)
falconInput57DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput57DigAlarm.setStatus("mandatory")
_FalconInput57HighAlarm_Type = ObjectIdentifier
_FalconInput57HighAlarm_Object = MibScalar
falconInput57HighAlarm = _FalconInput57HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3011),
    _FalconInput57HighAlarm_Type()
)
falconInput57HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput57HighAlarm.setStatus("mandatory")
_FalconInput57LowAlarm_Type = ObjectIdentifier
_FalconInput57LowAlarm_Object = MibScalar
falconInput57LowAlarm = _FalconInput57LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3012),
    _FalconInput57LowAlarm_Type()
)
falconInput57LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput57LowAlarm.setStatus("mandatory")
_FalconInput57High2Alarm_Type = ObjectIdentifier
_FalconInput57High2Alarm_Object = MibScalar
falconInput57High2Alarm = _FalconInput57High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3013),
    _FalconInput57High2Alarm_Type()
)
falconInput57High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput57High2Alarm.setStatus("mandatory")
_FalconInput57Low2Alarm_Type = ObjectIdentifier
_FalconInput57Low2Alarm_Object = MibScalar
falconInput57Low2Alarm = _FalconInput57Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3014),
    _FalconInput57Low2Alarm_Type()
)
falconInput57Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput57Low2Alarm.setStatus("mandatory")
_FalconInput58DigAlarm_Type = ObjectIdentifier
_FalconInput58DigAlarm_Object = MibScalar
falconInput58DigAlarm = _FalconInput58DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3020),
    _FalconInput58DigAlarm_Type()
)
falconInput58DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput58DigAlarm.setStatus("mandatory")
_FalconInput58HighAlarm_Type = ObjectIdentifier
_FalconInput58HighAlarm_Object = MibScalar
falconInput58HighAlarm = _FalconInput58HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3021),
    _FalconInput58HighAlarm_Type()
)
falconInput58HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput58HighAlarm.setStatus("mandatory")
_FalconInput58LowAlarm_Type = ObjectIdentifier
_FalconInput58LowAlarm_Object = MibScalar
falconInput58LowAlarm = _FalconInput58LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3022),
    _FalconInput58LowAlarm_Type()
)
falconInput58LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput58LowAlarm.setStatus("mandatory")
_FalconInput58High2Alarm_Type = ObjectIdentifier
_FalconInput58High2Alarm_Object = MibScalar
falconInput58High2Alarm = _FalconInput58High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3023),
    _FalconInput58High2Alarm_Type()
)
falconInput58High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput58High2Alarm.setStatus("mandatory")
_FalconInput58Low2Alarm_Type = ObjectIdentifier
_FalconInput58Low2Alarm_Object = MibScalar
falconInput58Low2Alarm = _FalconInput58Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3024),
    _FalconInput58Low2Alarm_Type()
)
falconInput58Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput58Low2Alarm.setStatus("mandatory")
_FalconInput59DigAlarm_Type = ObjectIdentifier
_FalconInput59DigAlarm_Object = MibScalar
falconInput59DigAlarm = _FalconInput59DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3030),
    _FalconInput59DigAlarm_Type()
)
falconInput59DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput59DigAlarm.setStatus("mandatory")
_FalconInput59HighAlarm_Type = ObjectIdentifier
_FalconInput59HighAlarm_Object = MibScalar
falconInput59HighAlarm = _FalconInput59HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3031),
    _FalconInput59HighAlarm_Type()
)
falconInput59HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput59HighAlarm.setStatus("mandatory")
_FalconInput59LowAlarm_Type = ObjectIdentifier
_FalconInput59LowAlarm_Object = MibScalar
falconInput59LowAlarm = _FalconInput59LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3032),
    _FalconInput59LowAlarm_Type()
)
falconInput59LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput59LowAlarm.setStatus("mandatory")
_FalconInput59High2Alarm_Type = ObjectIdentifier
_FalconInput59High2Alarm_Object = MibScalar
falconInput59High2Alarm = _FalconInput59High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3033),
    _FalconInput59High2Alarm_Type()
)
falconInput59High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput59High2Alarm.setStatus("mandatory")
_FalconInput59Low2Alarm_Type = ObjectIdentifier
_FalconInput59Low2Alarm_Object = MibScalar
falconInput59Low2Alarm = _FalconInput59Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3034),
    _FalconInput59Low2Alarm_Type()
)
falconInput59Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput59Low2Alarm.setStatus("mandatory")
_FalconInput60DigAlarm_Type = ObjectIdentifier
_FalconInput60DigAlarm_Object = MibScalar
falconInput60DigAlarm = _FalconInput60DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3040),
    _FalconInput60DigAlarm_Type()
)
falconInput60DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput60DigAlarm.setStatus("mandatory")
_FalconInput60HighAlarm_Type = ObjectIdentifier
_FalconInput60HighAlarm_Object = MibScalar
falconInput60HighAlarm = _FalconInput60HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3041),
    _FalconInput60HighAlarm_Type()
)
falconInput60HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput60HighAlarm.setStatus("mandatory")
_FalconInput60LowAlarm_Type = ObjectIdentifier
_FalconInput60LowAlarm_Object = MibScalar
falconInput60LowAlarm = _FalconInput60LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3042),
    _FalconInput60LowAlarm_Type()
)
falconInput60LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput60LowAlarm.setStatus("mandatory")
_FalconInput60High2Alarm_Type = ObjectIdentifier
_FalconInput60High2Alarm_Object = MibScalar
falconInput60High2Alarm = _FalconInput60High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3043),
    _FalconInput60High2Alarm_Type()
)
falconInput60High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput60High2Alarm.setStatus("mandatory")
_FalconInput60Low2Alarm_Type = ObjectIdentifier
_FalconInput60Low2Alarm_Object = MibScalar
falconInput60Low2Alarm = _FalconInput60Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3044),
    _FalconInput60Low2Alarm_Type()
)
falconInput60Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput60Low2Alarm.setStatus("mandatory")
_FalconInput61DigAlarm_Type = ObjectIdentifier
_FalconInput61DigAlarm_Object = MibScalar
falconInput61DigAlarm = _FalconInput61DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3050),
    _FalconInput61DigAlarm_Type()
)
falconInput61DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput61DigAlarm.setStatus("mandatory")
_FalconInput61HighAlarm_Type = ObjectIdentifier
_FalconInput61HighAlarm_Object = MibScalar
falconInput61HighAlarm = _FalconInput61HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3051),
    _FalconInput61HighAlarm_Type()
)
falconInput61HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput61HighAlarm.setStatus("mandatory")
_FalconInput61LowAlarm_Type = ObjectIdentifier
_FalconInput61LowAlarm_Object = MibScalar
falconInput61LowAlarm = _FalconInput61LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3052),
    _FalconInput61LowAlarm_Type()
)
falconInput61LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput61LowAlarm.setStatus("mandatory")
_FalconInput61High2Alarm_Type = ObjectIdentifier
_FalconInput61High2Alarm_Object = MibScalar
falconInput61High2Alarm = _FalconInput61High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3053),
    _FalconInput61High2Alarm_Type()
)
falconInput61High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput61High2Alarm.setStatus("mandatory")
_FalconInput61Low2Alarm_Type = ObjectIdentifier
_FalconInput61Low2Alarm_Object = MibScalar
falconInput61Low2Alarm = _FalconInput61Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3054),
    _FalconInput61Low2Alarm_Type()
)
falconInput61Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput61Low2Alarm.setStatus("mandatory")
_FalconInput62DigAlarm_Type = ObjectIdentifier
_FalconInput62DigAlarm_Object = MibScalar
falconInput62DigAlarm = _FalconInput62DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3060),
    _FalconInput62DigAlarm_Type()
)
falconInput62DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput62DigAlarm.setStatus("mandatory")
_FalconInput62HighAlarm_Type = ObjectIdentifier
_FalconInput62HighAlarm_Object = MibScalar
falconInput62HighAlarm = _FalconInput62HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3061),
    _FalconInput62HighAlarm_Type()
)
falconInput62HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput62HighAlarm.setStatus("mandatory")
_FalconInput62LowAlarm_Type = ObjectIdentifier
_FalconInput62LowAlarm_Object = MibScalar
falconInput62LowAlarm = _FalconInput62LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3062),
    _FalconInput62LowAlarm_Type()
)
falconInput62LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput62LowAlarm.setStatus("mandatory")
_FalconInput62High2Alarm_Type = ObjectIdentifier
_FalconInput62High2Alarm_Object = MibScalar
falconInput62High2Alarm = _FalconInput62High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3063),
    _FalconInput62High2Alarm_Type()
)
falconInput62High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput62High2Alarm.setStatus("mandatory")
_FalconInput62Low2Alarm_Type = ObjectIdentifier
_FalconInput62Low2Alarm_Object = MibScalar
falconInput62Low2Alarm = _FalconInput62Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3064),
    _FalconInput62Low2Alarm_Type()
)
falconInput62Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput62Low2Alarm.setStatus("mandatory")
_FalconInput63DigAlarm_Type = ObjectIdentifier
_FalconInput63DigAlarm_Object = MibScalar
falconInput63DigAlarm = _FalconInput63DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3070),
    _FalconInput63DigAlarm_Type()
)
falconInput63DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput63DigAlarm.setStatus("mandatory")
_FalconInput63HighAlarm_Type = ObjectIdentifier
_FalconInput63HighAlarm_Object = MibScalar
falconInput63HighAlarm = _FalconInput63HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3071),
    _FalconInput63HighAlarm_Type()
)
falconInput63HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput63HighAlarm.setStatus("mandatory")
_FalconInput63LowAlarm_Type = ObjectIdentifier
_FalconInput63LowAlarm_Object = MibScalar
falconInput63LowAlarm = _FalconInput63LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3072),
    _FalconInput63LowAlarm_Type()
)
falconInput63LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput63LowAlarm.setStatus("mandatory")
_FalconInput63High2Alarm_Type = ObjectIdentifier
_FalconInput63High2Alarm_Object = MibScalar
falconInput63High2Alarm = _FalconInput63High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3073),
    _FalconInput63High2Alarm_Type()
)
falconInput63High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput63High2Alarm.setStatus("mandatory")
_FalconInput63Low2Alarm_Type = ObjectIdentifier
_FalconInput63Low2Alarm_Object = MibScalar
falconInput63Low2Alarm = _FalconInput63Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3074),
    _FalconInput63Low2Alarm_Type()
)
falconInput63Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput63Low2Alarm.setStatus("mandatory")
_FalconInput64DigAlarm_Type = ObjectIdentifier
_FalconInput64DigAlarm_Object = MibScalar
falconInput64DigAlarm = _FalconInput64DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3080),
    _FalconInput64DigAlarm_Type()
)
falconInput64DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput64DigAlarm.setStatus("mandatory")
_FalconInput64HighAlarm_Type = ObjectIdentifier
_FalconInput64HighAlarm_Object = MibScalar
falconInput64HighAlarm = _FalconInput64HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3081),
    _FalconInput64HighAlarm_Type()
)
falconInput64HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput64HighAlarm.setStatus("mandatory")
_FalconInput64LowAlarm_Type = ObjectIdentifier
_FalconInput64LowAlarm_Object = MibScalar
falconInput64LowAlarm = _FalconInput64LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3082),
    _FalconInput64LowAlarm_Type()
)
falconInput64LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput64LowAlarm.setStatus("mandatory")
_FalconInput64High2Alarm_Type = ObjectIdentifier
_FalconInput64High2Alarm_Object = MibScalar
falconInput64High2Alarm = _FalconInput64High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3083),
    _FalconInput64High2Alarm_Type()
)
falconInput64High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput64High2Alarm.setStatus("mandatory")
_FalconInput64Low2Alarm_Type = ObjectIdentifier
_FalconInput64Low2Alarm_Object = MibScalar
falconInput64Low2Alarm = _FalconInput64Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3084),
    _FalconInput64Low2Alarm_Type()
)
falconInput64Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput64Low2Alarm.setStatus("mandatory")
_FalconInput65DigAlarm_Type = ObjectIdentifier
_FalconInput65DigAlarm_Object = MibScalar
falconInput65DigAlarm = _FalconInput65DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3090),
    _FalconInput65DigAlarm_Type()
)
falconInput65DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput65DigAlarm.setStatus("mandatory")
_FalconInput65HighAlarm_Type = ObjectIdentifier
_FalconInput65HighAlarm_Object = MibScalar
falconInput65HighAlarm = _FalconInput65HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3091),
    _FalconInput65HighAlarm_Type()
)
falconInput65HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput65HighAlarm.setStatus("mandatory")
_FalconInput65LowAlarm_Type = ObjectIdentifier
_FalconInput65LowAlarm_Object = MibScalar
falconInput65LowAlarm = _FalconInput65LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3092),
    _FalconInput65LowAlarm_Type()
)
falconInput65LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput65LowAlarm.setStatus("mandatory")
_FalconInput65High2Alarm_Type = ObjectIdentifier
_FalconInput65High2Alarm_Object = MibScalar
falconInput65High2Alarm = _FalconInput65High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3093),
    _FalconInput65High2Alarm_Type()
)
falconInput65High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput65High2Alarm.setStatus("mandatory")
_FalconInput65Low2Alarm_Type = ObjectIdentifier
_FalconInput65Low2Alarm_Object = MibScalar
falconInput65Low2Alarm = _FalconInput65Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3094),
    _FalconInput65Low2Alarm_Type()
)
falconInput65Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput65Low2Alarm.setStatus("mandatory")
_FalconInput66DigAlarm_Type = ObjectIdentifier
_FalconInput66DigAlarm_Object = MibScalar
falconInput66DigAlarm = _FalconInput66DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3100),
    _FalconInput66DigAlarm_Type()
)
falconInput66DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput66DigAlarm.setStatus("mandatory")
_FalconInput66HighAlarm_Type = ObjectIdentifier
_FalconInput66HighAlarm_Object = MibScalar
falconInput66HighAlarm = _FalconInput66HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3101),
    _FalconInput66HighAlarm_Type()
)
falconInput66HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput66HighAlarm.setStatus("mandatory")
_FalconInput66LowAlarm_Type = ObjectIdentifier
_FalconInput66LowAlarm_Object = MibScalar
falconInput66LowAlarm = _FalconInput66LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3102),
    _FalconInput66LowAlarm_Type()
)
falconInput66LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput66LowAlarm.setStatus("mandatory")
_FalconInput66High2Alarm_Type = ObjectIdentifier
_FalconInput66High2Alarm_Object = MibScalar
falconInput66High2Alarm = _FalconInput66High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3103),
    _FalconInput66High2Alarm_Type()
)
falconInput66High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput66High2Alarm.setStatus("mandatory")
_FalconInput66Low2Alarm_Type = ObjectIdentifier
_FalconInput66Low2Alarm_Object = MibScalar
falconInput66Low2Alarm = _FalconInput66Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3104),
    _FalconInput66Low2Alarm_Type()
)
falconInput66Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput66Low2Alarm.setStatus("mandatory")
_FalconInput67DigAlarm_Type = ObjectIdentifier
_FalconInput67DigAlarm_Object = MibScalar
falconInput67DigAlarm = _FalconInput67DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3110),
    _FalconInput67DigAlarm_Type()
)
falconInput67DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput67DigAlarm.setStatus("mandatory")
_FalconInput67HighAlarm_Type = ObjectIdentifier
_FalconInput67HighAlarm_Object = MibScalar
falconInput67HighAlarm = _FalconInput67HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3111),
    _FalconInput67HighAlarm_Type()
)
falconInput67HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput67HighAlarm.setStatus("mandatory")
_FalconInput67LowAlarm_Type = ObjectIdentifier
_FalconInput67LowAlarm_Object = MibScalar
falconInput67LowAlarm = _FalconInput67LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3112),
    _FalconInput67LowAlarm_Type()
)
falconInput67LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput67LowAlarm.setStatus("mandatory")
_FalconInput67High2Alarm_Type = ObjectIdentifier
_FalconInput67High2Alarm_Object = MibScalar
falconInput67High2Alarm = _FalconInput67High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3113),
    _FalconInput67High2Alarm_Type()
)
falconInput67High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput67High2Alarm.setStatus("mandatory")
_FalconInput67Low2Alarm_Type = ObjectIdentifier
_FalconInput67Low2Alarm_Object = MibScalar
falconInput67Low2Alarm = _FalconInput67Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3114),
    _FalconInput67Low2Alarm_Type()
)
falconInput67Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput67Low2Alarm.setStatus("mandatory")
_FalconInput68DigAlarm_Type = ObjectIdentifier
_FalconInput68DigAlarm_Object = MibScalar
falconInput68DigAlarm = _FalconInput68DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3120),
    _FalconInput68DigAlarm_Type()
)
falconInput68DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput68DigAlarm.setStatus("mandatory")
_FalconInput68HighAlarm_Type = ObjectIdentifier
_FalconInput68HighAlarm_Object = MibScalar
falconInput68HighAlarm = _FalconInput68HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3121),
    _FalconInput68HighAlarm_Type()
)
falconInput68HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput68HighAlarm.setStatus("mandatory")
_FalconInput68LowAlarm_Type = ObjectIdentifier
_FalconInput68LowAlarm_Object = MibScalar
falconInput68LowAlarm = _FalconInput68LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3122),
    _FalconInput68LowAlarm_Type()
)
falconInput68LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput68LowAlarm.setStatus("mandatory")
_FalconInput68High2Alarm_Type = ObjectIdentifier
_FalconInput68High2Alarm_Object = MibScalar
falconInput68High2Alarm = _FalconInput68High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3123),
    _FalconInput68High2Alarm_Type()
)
falconInput68High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput68High2Alarm.setStatus("mandatory")
_FalconInput68Low2Alarm_Type = ObjectIdentifier
_FalconInput68Low2Alarm_Object = MibScalar
falconInput68Low2Alarm = _FalconInput68Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3124),
    _FalconInput68Low2Alarm_Type()
)
falconInput68Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput68Low2Alarm.setStatus("mandatory")
_FalconInput69DigAlarm_Type = ObjectIdentifier
_FalconInput69DigAlarm_Object = MibScalar
falconInput69DigAlarm = _FalconInput69DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3130),
    _FalconInput69DigAlarm_Type()
)
falconInput69DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput69DigAlarm.setStatus("mandatory")
_FalconInput70DigAlarm_Type = ObjectIdentifier
_FalconInput70DigAlarm_Object = MibScalar
falconInput70DigAlarm = _FalconInput70DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3140),
    _FalconInput70DigAlarm_Type()
)
falconInput70DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput70DigAlarm.setStatus("mandatory")
_FalconInput71DigAlarm_Type = ObjectIdentifier
_FalconInput71DigAlarm_Object = MibScalar
falconInput71DigAlarm = _FalconInput71DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3150),
    _FalconInput71DigAlarm_Type()
)
falconInput71DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput71DigAlarm.setStatus("mandatory")
_FalconInput72DigAlarm_Type = ObjectIdentifier
_FalconInput72DigAlarm_Object = MibScalar
falconInput72DigAlarm = _FalconInput72DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3160),
    _FalconInput72DigAlarm_Type()
)
falconInput72DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput72DigAlarm.setStatus("mandatory")
_FalconInput73DigAlarm_Type = ObjectIdentifier
_FalconInput73DigAlarm_Object = MibScalar
falconInput73DigAlarm = _FalconInput73DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3170),
    _FalconInput73DigAlarm_Type()
)
falconInput73DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput73DigAlarm.setStatus("mandatory")
_FalconInput74DigAlarm_Type = ObjectIdentifier
_FalconInput74DigAlarm_Object = MibScalar
falconInput74DigAlarm = _FalconInput74DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3180),
    _FalconInput74DigAlarm_Type()
)
falconInput74DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput74DigAlarm.setStatus("mandatory")
_FalconInput75DigAlarm_Type = ObjectIdentifier
_FalconInput75DigAlarm_Object = MibScalar
falconInput75DigAlarm = _FalconInput75DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3190),
    _FalconInput75DigAlarm_Type()
)
falconInput75DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput75DigAlarm.setStatus("mandatory")
_FalconInput76DigAlarm_Type = ObjectIdentifier
_FalconInput76DigAlarm_Object = MibScalar
falconInput76DigAlarm = _FalconInput76DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3200),
    _FalconInput76DigAlarm_Type()
)
falconInput76DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput76DigAlarm.setStatus("mandatory")
_FalconInput77DigAlarm_Type = ObjectIdentifier
_FalconInput77DigAlarm_Object = MibScalar
falconInput77DigAlarm = _FalconInput77DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3210),
    _FalconInput77DigAlarm_Type()
)
falconInput77DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput77DigAlarm.setStatus("mandatory")
_FalconInput78DigAlarm_Type = ObjectIdentifier
_FalconInput78DigAlarm_Object = MibScalar
falconInput78DigAlarm = _FalconInput78DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3220),
    _FalconInput78DigAlarm_Type()
)
falconInput78DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput78DigAlarm.setStatus("mandatory")
_FalconInput79DigAlarm_Type = ObjectIdentifier
_FalconInput79DigAlarm_Object = MibScalar
falconInput79DigAlarm = _FalconInput79DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3230),
    _FalconInput79DigAlarm_Type()
)
falconInput79DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput79DigAlarm.setStatus("mandatory")
_FalconInput80DigAlarm_Type = ObjectIdentifier
_FalconInput80DigAlarm_Object = MibScalar
falconInput80DigAlarm = _FalconInput80DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 3240),
    _FalconInput80DigAlarm_Type()
)
falconInput80DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput80DigAlarm.setStatus("mandatory")
_FalconInput81DigAlarm_Type = ObjectIdentifier
_FalconInput81DigAlarm_Object = MibScalar
falconInput81DigAlarm = _FalconInput81DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4010),
    _FalconInput81DigAlarm_Type()
)
falconInput81DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput81DigAlarm.setStatus("mandatory")
_FalconInput81HighAlarm_Type = ObjectIdentifier
_FalconInput81HighAlarm_Object = MibScalar
falconInput81HighAlarm = _FalconInput81HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4011),
    _FalconInput81HighAlarm_Type()
)
falconInput81HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput81HighAlarm.setStatus("mandatory")
_FalconInput81LowAlarm_Type = ObjectIdentifier
_FalconInput81LowAlarm_Object = MibScalar
falconInput81LowAlarm = _FalconInput81LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4012),
    _FalconInput81LowAlarm_Type()
)
falconInput81LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput81LowAlarm.setStatus("mandatory")
_FalconInput81High2Alarm_Type = ObjectIdentifier
_FalconInput81High2Alarm_Object = MibScalar
falconInput81High2Alarm = _FalconInput81High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4013),
    _FalconInput81High2Alarm_Type()
)
falconInput81High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput81High2Alarm.setStatus("mandatory")
_FalconInput81Low2Alarm_Type = ObjectIdentifier
_FalconInput81Low2Alarm_Object = MibScalar
falconInput81Low2Alarm = _FalconInput81Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4014),
    _FalconInput81Low2Alarm_Type()
)
falconInput81Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput81Low2Alarm.setStatus("mandatory")
_FalconInput82DigAlarm_Type = ObjectIdentifier
_FalconInput82DigAlarm_Object = MibScalar
falconInput82DigAlarm = _FalconInput82DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4020),
    _FalconInput82DigAlarm_Type()
)
falconInput82DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput82DigAlarm.setStatus("mandatory")
_FalconInput82HighAlarm_Type = ObjectIdentifier
_FalconInput82HighAlarm_Object = MibScalar
falconInput82HighAlarm = _FalconInput82HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4021),
    _FalconInput82HighAlarm_Type()
)
falconInput82HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput82HighAlarm.setStatus("mandatory")
_FalconInput82LowAlarm_Type = ObjectIdentifier
_FalconInput82LowAlarm_Object = MibScalar
falconInput82LowAlarm = _FalconInput82LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4022),
    _FalconInput82LowAlarm_Type()
)
falconInput82LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput82LowAlarm.setStatus("mandatory")
_FalconInput82High2Alarm_Type = ObjectIdentifier
_FalconInput82High2Alarm_Object = MibScalar
falconInput82High2Alarm = _FalconInput82High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4023),
    _FalconInput82High2Alarm_Type()
)
falconInput82High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput82High2Alarm.setStatus("mandatory")
_FalconInput82Low2Alarm_Type = ObjectIdentifier
_FalconInput82Low2Alarm_Object = MibScalar
falconInput82Low2Alarm = _FalconInput82Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4024),
    _FalconInput82Low2Alarm_Type()
)
falconInput82Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput82Low2Alarm.setStatus("mandatory")
_FalconInput83DigAlarm_Type = ObjectIdentifier
_FalconInput83DigAlarm_Object = MibScalar
falconInput83DigAlarm = _FalconInput83DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4030),
    _FalconInput83DigAlarm_Type()
)
falconInput83DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput83DigAlarm.setStatus("mandatory")
_FalconInput83HighAlarm_Type = ObjectIdentifier
_FalconInput83HighAlarm_Object = MibScalar
falconInput83HighAlarm = _FalconInput83HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4031),
    _FalconInput83HighAlarm_Type()
)
falconInput83HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput83HighAlarm.setStatus("mandatory")
_FalconInput83LowAlarm_Type = ObjectIdentifier
_FalconInput83LowAlarm_Object = MibScalar
falconInput83LowAlarm = _FalconInput83LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4032),
    _FalconInput83LowAlarm_Type()
)
falconInput83LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput83LowAlarm.setStatus("mandatory")
_FalconInput83High2Alarm_Type = ObjectIdentifier
_FalconInput83High2Alarm_Object = MibScalar
falconInput83High2Alarm = _FalconInput83High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4033),
    _FalconInput83High2Alarm_Type()
)
falconInput83High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput83High2Alarm.setStatus("mandatory")
_FalconInput83Low2Alarm_Type = ObjectIdentifier
_FalconInput83Low2Alarm_Object = MibScalar
falconInput83Low2Alarm = _FalconInput83Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4034),
    _FalconInput83Low2Alarm_Type()
)
falconInput83Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput83Low2Alarm.setStatus("mandatory")
_FalconInput84DigAlarm_Type = ObjectIdentifier
_FalconInput84DigAlarm_Object = MibScalar
falconInput84DigAlarm = _FalconInput84DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4040),
    _FalconInput84DigAlarm_Type()
)
falconInput84DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput84DigAlarm.setStatus("mandatory")
_FalconInput84HighAlarm_Type = ObjectIdentifier
_FalconInput84HighAlarm_Object = MibScalar
falconInput84HighAlarm = _FalconInput84HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4041),
    _FalconInput84HighAlarm_Type()
)
falconInput84HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput84HighAlarm.setStatus("mandatory")
_FalconInput84LowAlarm_Type = ObjectIdentifier
_FalconInput84LowAlarm_Object = MibScalar
falconInput84LowAlarm = _FalconInput84LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4042),
    _FalconInput84LowAlarm_Type()
)
falconInput84LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput84LowAlarm.setStatus("mandatory")
_FalconInput84High2Alarm_Type = ObjectIdentifier
_FalconInput84High2Alarm_Object = MibScalar
falconInput84High2Alarm = _FalconInput84High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4043),
    _FalconInput84High2Alarm_Type()
)
falconInput84High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput84High2Alarm.setStatus("mandatory")
_FalconInput84Low2Alarm_Type = ObjectIdentifier
_FalconInput84Low2Alarm_Object = MibScalar
falconInput84Low2Alarm = _FalconInput84Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4044),
    _FalconInput84Low2Alarm_Type()
)
falconInput84Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput84Low2Alarm.setStatus("mandatory")
_FalconInput85DigAlarm_Type = ObjectIdentifier
_FalconInput85DigAlarm_Object = MibScalar
falconInput85DigAlarm = _FalconInput85DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4050),
    _FalconInput85DigAlarm_Type()
)
falconInput85DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput85DigAlarm.setStatus("mandatory")
_FalconInput85HighAlarm_Type = ObjectIdentifier
_FalconInput85HighAlarm_Object = MibScalar
falconInput85HighAlarm = _FalconInput85HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4051),
    _FalconInput85HighAlarm_Type()
)
falconInput85HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput85HighAlarm.setStatus("mandatory")
_FalconInput85LowAlarm_Type = ObjectIdentifier
_FalconInput85LowAlarm_Object = MibScalar
falconInput85LowAlarm = _FalconInput85LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4052),
    _FalconInput85LowAlarm_Type()
)
falconInput85LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput85LowAlarm.setStatus("mandatory")
_FalconInput85High2Alarm_Type = ObjectIdentifier
_FalconInput85High2Alarm_Object = MibScalar
falconInput85High2Alarm = _FalconInput85High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4053),
    _FalconInput85High2Alarm_Type()
)
falconInput85High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput85High2Alarm.setStatus("mandatory")
_FalconInput85Low2Alarm_Type = ObjectIdentifier
_FalconInput85Low2Alarm_Object = MibScalar
falconInput85Low2Alarm = _FalconInput85Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4054),
    _FalconInput85Low2Alarm_Type()
)
falconInput85Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput85Low2Alarm.setStatus("mandatory")
_FalconInput86DigAlarm_Type = ObjectIdentifier
_FalconInput86DigAlarm_Object = MibScalar
falconInput86DigAlarm = _FalconInput86DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4060),
    _FalconInput86DigAlarm_Type()
)
falconInput86DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput86DigAlarm.setStatus("mandatory")
_FalconInput86HighAlarm_Type = ObjectIdentifier
_FalconInput86HighAlarm_Object = MibScalar
falconInput86HighAlarm = _FalconInput86HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4061),
    _FalconInput86HighAlarm_Type()
)
falconInput86HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput86HighAlarm.setStatus("mandatory")
_FalconInput86LowAlarm_Type = ObjectIdentifier
_FalconInput86LowAlarm_Object = MibScalar
falconInput86LowAlarm = _FalconInput86LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4062),
    _FalconInput86LowAlarm_Type()
)
falconInput86LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput86LowAlarm.setStatus("mandatory")
_FalconInput86High2Alarm_Type = ObjectIdentifier
_FalconInput86High2Alarm_Object = MibScalar
falconInput86High2Alarm = _FalconInput86High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4063),
    _FalconInput86High2Alarm_Type()
)
falconInput86High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput86High2Alarm.setStatus("mandatory")
_FalconInput86Low2Alarm_Type = ObjectIdentifier
_FalconInput86Low2Alarm_Object = MibScalar
falconInput86Low2Alarm = _FalconInput86Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4064),
    _FalconInput86Low2Alarm_Type()
)
falconInput86Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput86Low2Alarm.setStatus("mandatory")
_FalconInput87DigAlarm_Type = ObjectIdentifier
_FalconInput87DigAlarm_Object = MibScalar
falconInput87DigAlarm = _FalconInput87DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4070),
    _FalconInput87DigAlarm_Type()
)
falconInput87DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput87DigAlarm.setStatus("mandatory")
_FalconInput87HighAlarm_Type = ObjectIdentifier
_FalconInput87HighAlarm_Object = MibScalar
falconInput87HighAlarm = _FalconInput87HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4071),
    _FalconInput87HighAlarm_Type()
)
falconInput87HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput87HighAlarm.setStatus("mandatory")
_FalconInput87LowAlarm_Type = ObjectIdentifier
_FalconInput87LowAlarm_Object = MibScalar
falconInput87LowAlarm = _FalconInput87LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4072),
    _FalconInput87LowAlarm_Type()
)
falconInput87LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput87LowAlarm.setStatus("mandatory")
_FalconInput87High2Alarm_Type = ObjectIdentifier
_FalconInput87High2Alarm_Object = MibScalar
falconInput87High2Alarm = _FalconInput87High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4073),
    _FalconInput87High2Alarm_Type()
)
falconInput87High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput87High2Alarm.setStatus("mandatory")
_FalconInput87Low2Alarm_Type = ObjectIdentifier
_FalconInput87Low2Alarm_Object = MibScalar
falconInput87Low2Alarm = _FalconInput87Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4074),
    _FalconInput87Low2Alarm_Type()
)
falconInput87Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput87Low2Alarm.setStatus("mandatory")
_FalconInput88DigAlarm_Type = ObjectIdentifier
_FalconInput88DigAlarm_Object = MibScalar
falconInput88DigAlarm = _FalconInput88DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4080),
    _FalconInput88DigAlarm_Type()
)
falconInput88DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput88DigAlarm.setStatus("mandatory")
_FalconInput88HighAlarm_Type = ObjectIdentifier
_FalconInput88HighAlarm_Object = MibScalar
falconInput88HighAlarm = _FalconInput88HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4081),
    _FalconInput88HighAlarm_Type()
)
falconInput88HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput88HighAlarm.setStatus("mandatory")
_FalconInput88LowAlarm_Type = ObjectIdentifier
_FalconInput88LowAlarm_Object = MibScalar
falconInput88LowAlarm = _FalconInput88LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4082),
    _FalconInput88LowAlarm_Type()
)
falconInput88LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput88LowAlarm.setStatus("mandatory")
_FalconInput88High2Alarm_Type = ObjectIdentifier
_FalconInput88High2Alarm_Object = MibScalar
falconInput88High2Alarm = _FalconInput88High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4083),
    _FalconInput88High2Alarm_Type()
)
falconInput88High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput88High2Alarm.setStatus("mandatory")
_FalconInput88Low2Alarm_Type = ObjectIdentifier
_FalconInput88Low2Alarm_Object = MibScalar
falconInput88Low2Alarm = _FalconInput88Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4084),
    _FalconInput88Low2Alarm_Type()
)
falconInput88Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput88Low2Alarm.setStatus("mandatory")
_FalconInput89DigAlarm_Type = ObjectIdentifier
_FalconInput89DigAlarm_Object = MibScalar
falconInput89DigAlarm = _FalconInput89DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4090),
    _FalconInput89DigAlarm_Type()
)
falconInput89DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput89DigAlarm.setStatus("mandatory")
_FalconInput89HighAlarm_Type = ObjectIdentifier
_FalconInput89HighAlarm_Object = MibScalar
falconInput89HighAlarm = _FalconInput89HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4091),
    _FalconInput89HighAlarm_Type()
)
falconInput89HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput89HighAlarm.setStatus("mandatory")
_FalconInput89LowAlarm_Type = ObjectIdentifier
_FalconInput89LowAlarm_Object = MibScalar
falconInput89LowAlarm = _FalconInput89LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4092),
    _FalconInput89LowAlarm_Type()
)
falconInput89LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput89LowAlarm.setStatus("mandatory")
_FalconInput89High2Alarm_Type = ObjectIdentifier
_FalconInput89High2Alarm_Object = MibScalar
falconInput89High2Alarm = _FalconInput89High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4093),
    _FalconInput89High2Alarm_Type()
)
falconInput89High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput89High2Alarm.setStatus("mandatory")
_FalconInput89Low2Alarm_Type = ObjectIdentifier
_FalconInput89Low2Alarm_Object = MibScalar
falconInput89Low2Alarm = _FalconInput89Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4094),
    _FalconInput89Low2Alarm_Type()
)
falconInput89Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput89Low2Alarm.setStatus("mandatory")
_FalconInput90DigAlarm_Type = ObjectIdentifier
_FalconInput90DigAlarm_Object = MibScalar
falconInput90DigAlarm = _FalconInput90DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4100),
    _FalconInput90DigAlarm_Type()
)
falconInput90DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput90DigAlarm.setStatus("mandatory")
_FalconInput90HighAlarm_Type = ObjectIdentifier
_FalconInput90HighAlarm_Object = MibScalar
falconInput90HighAlarm = _FalconInput90HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4101),
    _FalconInput90HighAlarm_Type()
)
falconInput90HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput90HighAlarm.setStatus("mandatory")
_FalconInput90LowAlarm_Type = ObjectIdentifier
_FalconInput90LowAlarm_Object = MibScalar
falconInput90LowAlarm = _FalconInput90LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4102),
    _FalconInput90LowAlarm_Type()
)
falconInput90LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput90LowAlarm.setStatus("mandatory")
_FalconInput90High2Alarm_Type = ObjectIdentifier
_FalconInput90High2Alarm_Object = MibScalar
falconInput90High2Alarm = _FalconInput90High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4103),
    _FalconInput90High2Alarm_Type()
)
falconInput90High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput90High2Alarm.setStatus("mandatory")
_FalconInput90Low2Alarm_Type = ObjectIdentifier
_FalconInput90Low2Alarm_Object = MibScalar
falconInput90Low2Alarm = _FalconInput90Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4104),
    _FalconInput90Low2Alarm_Type()
)
falconInput90Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput90Low2Alarm.setStatus("mandatory")
_FalconInput91DigAlarm_Type = ObjectIdentifier
_FalconInput91DigAlarm_Object = MibScalar
falconInput91DigAlarm = _FalconInput91DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4110),
    _FalconInput91DigAlarm_Type()
)
falconInput91DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput91DigAlarm.setStatus("mandatory")
_FalconInput91HighAlarm_Type = ObjectIdentifier
_FalconInput91HighAlarm_Object = MibScalar
falconInput91HighAlarm = _FalconInput91HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4111),
    _FalconInput91HighAlarm_Type()
)
falconInput91HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput91HighAlarm.setStatus("mandatory")
_FalconInput91LowAlarm_Type = ObjectIdentifier
_FalconInput91LowAlarm_Object = MibScalar
falconInput91LowAlarm = _FalconInput91LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4112),
    _FalconInput91LowAlarm_Type()
)
falconInput91LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput91LowAlarm.setStatus("mandatory")
_FalconInput91High2Alarm_Type = ObjectIdentifier
_FalconInput91High2Alarm_Object = MibScalar
falconInput91High2Alarm = _FalconInput91High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4113),
    _FalconInput91High2Alarm_Type()
)
falconInput91High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput91High2Alarm.setStatus("mandatory")
_FalconInput91Low2Alarm_Type = ObjectIdentifier
_FalconInput91Low2Alarm_Object = MibScalar
falconInput91Low2Alarm = _FalconInput91Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4114),
    _FalconInput91Low2Alarm_Type()
)
falconInput91Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput91Low2Alarm.setStatus("mandatory")
_FalconInput92DigAlarm_Type = ObjectIdentifier
_FalconInput92DigAlarm_Object = MibScalar
falconInput92DigAlarm = _FalconInput92DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4120),
    _FalconInput92DigAlarm_Type()
)
falconInput92DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput92DigAlarm.setStatus("mandatory")
_FalconInput92HighAlarm_Type = ObjectIdentifier
_FalconInput92HighAlarm_Object = MibScalar
falconInput92HighAlarm = _FalconInput92HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4121),
    _FalconInput92HighAlarm_Type()
)
falconInput92HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput92HighAlarm.setStatus("mandatory")
_FalconInput92LowAlarm_Type = ObjectIdentifier
_FalconInput92LowAlarm_Object = MibScalar
falconInput92LowAlarm = _FalconInput92LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4122),
    _FalconInput92LowAlarm_Type()
)
falconInput92LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput92LowAlarm.setStatus("mandatory")
_FalconInput92High2Alarm_Type = ObjectIdentifier
_FalconInput92High2Alarm_Object = MibScalar
falconInput92High2Alarm = _FalconInput92High2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4123),
    _FalconInput92High2Alarm_Type()
)
falconInput92High2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput92High2Alarm.setStatus("mandatory")
_FalconInput92Low2Alarm_Type = ObjectIdentifier
_FalconInput92Low2Alarm_Object = MibScalar
falconInput92Low2Alarm = _FalconInput92Low2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4124),
    _FalconInput92Low2Alarm_Type()
)
falconInput92Low2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput92Low2Alarm.setStatus("mandatory")
_FalconInput93DigAlarm_Type = ObjectIdentifier
_FalconInput93DigAlarm_Object = MibScalar
falconInput93DigAlarm = _FalconInput93DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4130),
    _FalconInput93DigAlarm_Type()
)
falconInput93DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput93DigAlarm.setStatus("mandatory")
_FalconInput94DigAlarm_Type = ObjectIdentifier
_FalconInput94DigAlarm_Object = MibScalar
falconInput94DigAlarm = _FalconInput94DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4140),
    _FalconInput94DigAlarm_Type()
)
falconInput94DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput94DigAlarm.setStatus("mandatory")
_FalconInput95DigAlarm_Type = ObjectIdentifier
_FalconInput95DigAlarm_Object = MibScalar
falconInput95DigAlarm = _FalconInput95DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4150),
    _FalconInput95DigAlarm_Type()
)
falconInput95DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput95DigAlarm.setStatus("mandatory")
_FalconInput96DigAlarm_Type = ObjectIdentifier
_FalconInput96DigAlarm_Object = MibScalar
falconInput96DigAlarm = _FalconInput96DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4160),
    _FalconInput96DigAlarm_Type()
)
falconInput96DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput96DigAlarm.setStatus("mandatory")
_FalconInput97DigAlarm_Type = ObjectIdentifier
_FalconInput97DigAlarm_Object = MibScalar
falconInput97DigAlarm = _FalconInput97DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4170),
    _FalconInput97DigAlarm_Type()
)
falconInput97DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput97DigAlarm.setStatus("mandatory")
_FalconInput98DigAlarm_Type = ObjectIdentifier
_FalconInput98DigAlarm_Object = MibScalar
falconInput98DigAlarm = _FalconInput98DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4180),
    _FalconInput98DigAlarm_Type()
)
falconInput98DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput98DigAlarm.setStatus("mandatory")
_FalconInput99DigAlarm_Type = ObjectIdentifier
_FalconInput99DigAlarm_Object = MibScalar
falconInput99DigAlarm = _FalconInput99DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4190),
    _FalconInput99DigAlarm_Type()
)
falconInput99DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput99DigAlarm.setStatus("mandatory")
_FalconInput100DigAlarm_Type = ObjectIdentifier
_FalconInput100DigAlarm_Object = MibScalar
falconInput100DigAlarm = _FalconInput100DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4200),
    _FalconInput100DigAlarm_Type()
)
falconInput100DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput100DigAlarm.setStatus("mandatory")
_FalconInput101DigAlarm_Type = ObjectIdentifier
_FalconInput101DigAlarm_Object = MibScalar
falconInput101DigAlarm = _FalconInput101DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4210),
    _FalconInput101DigAlarm_Type()
)
falconInput101DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput101DigAlarm.setStatus("mandatory")
_FalconInput102DigAlarm_Type = ObjectIdentifier
_FalconInput102DigAlarm_Object = MibScalar
falconInput102DigAlarm = _FalconInput102DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4220),
    _FalconInput102DigAlarm_Type()
)
falconInput102DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput102DigAlarm.setStatus("mandatory")
_FalconInput103DigAlarm_Type = ObjectIdentifier
_FalconInput103DigAlarm_Object = MibScalar
falconInput103DigAlarm = _FalconInput103DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4230),
    _FalconInput103DigAlarm_Type()
)
falconInput103DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput103DigAlarm.setStatus("mandatory")
_FalconInput104DigAlarm_Type = ObjectIdentifier
_FalconInput104DigAlarm_Object = MibScalar
falconInput104DigAlarm = _FalconInput104DigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 4240),
    _FalconInput104DigAlarm_Type()
)
falconInput104DigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput104DigAlarm.setStatus("mandatory")
_FalconTemperatureSensorHighAlarm_Type = ObjectIdentifier
_FalconTemperatureSensorHighAlarm_Object = MibScalar
falconTemperatureSensorHighAlarm = _FalconTemperatureSensorHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 5011),
    _FalconTemperatureSensorHighAlarm_Type()
)
falconTemperatureSensorHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconTemperatureSensorHighAlarm.setStatus("mandatory")
_FalconTemperatureSensorLowAlarm_Type = ObjectIdentifier
_FalconTemperatureSensorLowAlarm_Object = MibScalar
falconTemperatureSensorLowAlarm = _FalconTemperatureSensorLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 5012),
    _FalconTemperatureSensorLowAlarm_Type()
)
falconTemperatureSensorLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconTemperatureSensorLowAlarm.setStatus("mandatory")
_FalconTemperatureSensorHigh2Alarm_Type = ObjectIdentifier
_FalconTemperatureSensorHigh2Alarm_Object = MibScalar
falconTemperatureSensorHigh2Alarm = _FalconTemperatureSensorHigh2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 5013),
    _FalconTemperatureSensorHigh2Alarm_Type()
)
falconTemperatureSensorHigh2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconTemperatureSensorHigh2Alarm.setStatus("mandatory")
_FalconTemperatureSensorLow2Alarm_Type = ObjectIdentifier
_FalconTemperatureSensorLow2Alarm_Object = MibScalar
falconTemperatureSensorLow2Alarm = _FalconTemperatureSensorLow2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 5014),
    _FalconTemperatureSensorLow2Alarm_Type()
)
falconTemperatureSensorLow2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconTemperatureSensorLow2Alarm.setStatus("mandatory")
_FalconHumiditySensorHighAlarm_Type = ObjectIdentifier
_FalconHumiditySensorHighAlarm_Object = MibScalar
falconHumiditySensorHighAlarm = _FalconHumiditySensorHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 5021),
    _FalconHumiditySensorHighAlarm_Type()
)
falconHumiditySensorHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconHumiditySensorHighAlarm.setStatus("mandatory")
_FalconHumiditySensorLowAlarm_Type = ObjectIdentifier
_FalconHumiditySensorLowAlarm_Object = MibScalar
falconHumiditySensorLowAlarm = _FalconHumiditySensorLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 5022),
    _FalconHumiditySensorLowAlarm_Type()
)
falconHumiditySensorLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconHumiditySensorLowAlarm.setStatus("mandatory")
_FalconHumiditySensorHigh2Alarm_Type = ObjectIdentifier
_FalconHumiditySensorHigh2Alarm_Object = MibScalar
falconHumiditySensorHigh2Alarm = _FalconHumiditySensorHigh2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 5023),
    _FalconHumiditySensorHigh2Alarm_Type()
)
falconHumiditySensorHigh2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconHumiditySensorHigh2Alarm.setStatus("mandatory")
_FalconHumiditySensorLow2Alarm_Type = ObjectIdentifier
_FalconHumiditySensorLow2Alarm_Object = MibScalar
falconHumiditySensorLow2Alarm = _FalconHumiditySensorLow2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 5024),
    _FalconHumiditySensorLow2Alarm_Type()
)
falconHumiditySensorLow2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconHumiditySensorLow2Alarm.setStatus("mandatory")
_FalconLowBatteryAlarm_Type = ObjectIdentifier
_FalconLowBatteryAlarm_Object = MibScalar
falconLowBatteryAlarm = _FalconLowBatteryAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 5, 3, 6010),
    _FalconLowBatteryAlarm_Type()
)
falconLowBatteryAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconLowBatteryAlarm.setStatus("mandatory")
_FalconTraps_ObjectIdentity = ObjectIdentity
falconTraps = _FalconTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 6)
)
_FalconAlarmHistory_ObjectIdentity = ObjectIdentity
falconAlarmHistory = _FalconAlarmHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 7)
)
_FalconAlarmHistoryEntries_Type = Gauge32
_FalconAlarmHistoryEntries_Object = MibScalar
falconAlarmHistoryEntries = _FalconAlarmHistoryEntries_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 7, 1),
    _FalconAlarmHistoryEntries_Type()
)
falconAlarmHistoryEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconAlarmHistoryEntries.setStatus("mandatory")


class _FalconAlarmHistoryClear_Type(Integer32):
    """Custom type falconAlarmHistoryClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearBuffer", 1)
    )


_FalconAlarmHistoryClear_Type.__name__ = "Integer32"
_FalconAlarmHistoryClear_Object = MibScalar
falconAlarmHistoryClear = _FalconAlarmHistoryClear_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 7, 2),
    _FalconAlarmHistoryClear_Type()
)
falconAlarmHistoryClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconAlarmHistoryClear.setStatus("mandatory")
_FalconAlarmHistoryTable_Object = MibTable
falconAlarmHistoryTable = _FalconAlarmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 7, 3)
)
if mibBuilder.loadTexts:
    falconAlarmHistoryTable.setStatus("mandatory")
_FalconAlarmHistoryEntry_Object = MibTableRow
falconAlarmHistoryEntry = _FalconAlarmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 7, 3, 1)
)
falconAlarmHistoryEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconAlarmHistoryId"),
)
if mibBuilder.loadTexts:
    falconAlarmHistoryEntry.setStatus("mandatory")
_FalconAlarmHistoryId_Type = PositiveInteger
_FalconAlarmHistoryId_Object = MibTableColumn
falconAlarmHistoryId = _FalconAlarmHistoryId_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 7, 3, 1, 1),
    _FalconAlarmHistoryId_Type()
)
falconAlarmHistoryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    falconAlarmHistoryId.setStatus("mandatory")
_FalconAlarmHistoryText_Type = DisplayString
_FalconAlarmHistoryText_Object = MibTableColumn
falconAlarmHistoryText = _FalconAlarmHistoryText_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 7, 3, 1, 2),
    _FalconAlarmHistoryText_Type()
)
falconAlarmHistoryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconAlarmHistoryText.setStatus("mandatory")
_FalconTrapSettings_ObjectIdentity = ObjectIdentity
falconTrapSettings = _FalconTrapSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 8)
)


class _FalconPersistantTraps_Type(Integer32):
    """Custom type falconPersistantTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FalconPersistantTraps_Type.__name__ = "Integer32"
_FalconPersistantTraps_Object = MibScalar
falconPersistantTraps = _FalconPersistantTraps_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 8, 1),
    _FalconPersistantTraps_Type()
)
falconPersistantTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconPersistantTraps.setStatus("mandatory")


class _FalconAlarmAcknowledge_Type(Integer32):
    """Custom type falconAlarmAcknowledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("acknowledgeAlarms", 1)
    )


_FalconAlarmAcknowledge_Type.__name__ = "Integer32"
_FalconAlarmAcknowledge_Object = MibScalar
falconAlarmAcknowledge = _FalconAlarmAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 8, 2),
    _FalconAlarmAcknowledge_Type()
)
falconAlarmAcknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconAlarmAcknowledge.setStatus("mandatory")
_FalconSchedules_ObjectIdentity = ObjectIdentity
falconSchedules = _FalconSchedules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 9)
)


class _FalconScheduleABeginDOW_Type(Integer32):
    """Custom type falconScheduleABeginDOW based on Integer32"""
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
        *(("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7))
    )


_FalconScheduleABeginDOW_Type.__name__ = "Integer32"
_FalconScheduleABeginDOW_Object = MibScalar
falconScheduleABeginDOW = _FalconScheduleABeginDOW_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 9, 1),
    _FalconScheduleABeginDOW_Type()
)
falconScheduleABeginDOW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconScheduleABeginDOW.setStatus("mandatory")


class _FalconScheduleAEndDOW_Type(Integer32):
    """Custom type falconScheduleAEndDOW based on Integer32"""
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
        *(("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7))
    )


_FalconScheduleAEndDOW_Type.__name__ = "Integer32"
_FalconScheduleAEndDOW_Object = MibScalar
falconScheduleAEndDOW = _FalconScheduleAEndDOW_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 9, 2),
    _FalconScheduleAEndDOW_Type()
)
falconScheduleAEndDOW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconScheduleAEndDOW.setStatus("mandatory")
_FalconScheduleABeginTime_Type = DisplayString
_FalconScheduleABeginTime_Object = MibScalar
falconScheduleABeginTime = _FalconScheduleABeginTime_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 9, 3),
    _FalconScheduleABeginTime_Type()
)
falconScheduleABeginTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconScheduleABeginTime.setStatus("mandatory")
_FalconScheduleAEndTime_Type = DisplayString
_FalconScheduleAEndTime_Object = MibScalar
falconScheduleAEndTime = _FalconScheduleAEndTime_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 9, 4),
    _FalconScheduleAEndTime_Type()
)
falconScheduleAEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconScheduleAEndTime.setStatus("mandatory")


class _FalconScheduleBBeginDOW_Type(Integer32):
    """Custom type falconScheduleBBeginDOW based on Integer32"""
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
        *(("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7))
    )


_FalconScheduleBBeginDOW_Type.__name__ = "Integer32"
_FalconScheduleBBeginDOW_Object = MibScalar
falconScheduleBBeginDOW = _FalconScheduleBBeginDOW_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 9, 5),
    _FalconScheduleBBeginDOW_Type()
)
falconScheduleBBeginDOW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconScheduleBBeginDOW.setStatus("mandatory")


class _FalconScheduleBEndDOW_Type(Integer32):
    """Custom type falconScheduleBEndDOW based on Integer32"""
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
        *(("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7))
    )


_FalconScheduleBEndDOW_Type.__name__ = "Integer32"
_FalconScheduleBEndDOW_Object = MibScalar
falconScheduleBEndDOW = _FalconScheduleBEndDOW_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 9, 6),
    _FalconScheduleBEndDOW_Type()
)
falconScheduleBEndDOW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconScheduleBEndDOW.setStatus("mandatory")
_FalconScheduleBBeginTime_Type = DisplayString
_FalconScheduleBBeginTime_Object = MibScalar
falconScheduleBBeginTime = _FalconScheduleBBeginTime_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 9, 7),
    _FalconScheduleBBeginTime_Type()
)
falconScheduleBBeginTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconScheduleBBeginTime.setStatus("mandatory")
_FalconScheduleBEndTime_Type = DisplayString
_FalconScheduleBEndTime_Object = MibScalar
falconScheduleBEndTime = _FalconScheduleBEndTime_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 9, 8),
    _FalconScheduleBEndTime_Type()
)
falconScheduleBEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconScheduleBEndTime.setStatus("mandatory")
_FalconPortTrap_ObjectIdentity = ObjectIdentity
falconPortTrap = _FalconPortTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10)
)
_FalconPortTrapClear_ObjectIdentity = ObjectIdentity
falconPortTrapClear = _FalconPortTrapClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11)
)
_FalconXbus_ObjectIdentity = ObjectIdentity
falconXbus = _FalconXbus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12)
)
_FalconBCMs_ObjectIdentity = ObjectIdentity
falconBCMs = _FalconBCMs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1)
)
_FalconBCM01_ObjectIdentity = ObjectIdentity
falconBCM01 = _FalconBCM01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 1)
)
_FalconBCM01Label_Type = DisplayString
_FalconBCM01Label_Object = MibScalar
falconBCM01Label = _FalconBCM01Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 1, 1),
    _FalconBCM01Label_Type()
)
falconBCM01Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM01Label.setStatus("mandatory")
_FalconBCM01CBTable_Object = MibTable
falconBCM01CBTable = _FalconBCM01CBTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    falconBCM01CBTable.setStatus("mandatory")
_FalconBCM01CBEntry_Object = MibTableRow
falconBCM01CBEntry = _FalconBCM01CBEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 1, 2, 1)
)
falconBCM01CBEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconBCM01CBIndex"),
)
if mibBuilder.loadTexts:
    falconBCM01CBEntry.setStatus("mandatory")
_FalconBCM01CBIndex_Type = Integer32
_FalconBCM01CBIndex_Object = MibTableColumn
falconBCM01CBIndex = _FalconBCM01CBIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 1, 2, 1, 1),
    _FalconBCM01CBIndex_Type()
)
falconBCM01CBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM01CBIndex.setStatus("mandatory")


class _FalconBCM01CBStatus_Type(Integer32):
    """Custom type falconBCM01CBStatus based on Integer32"""
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
        *(("notConfigured", 0),
          ("offline", 1),
          ("normal", 2),
          ("zeroAmpAlarm", 3),
          ("warning", 4),
          ("alarm", 5))
    )


_FalconBCM01CBStatus_Type.__name__ = "Integer32"
_FalconBCM01CBStatus_Object = MibTableColumn
falconBCM01CBStatus = _FalconBCM01CBStatus_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 1, 2, 1, 2),
    _FalconBCM01CBStatus_Type()
)
falconBCM01CBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM01CBStatus.setStatus("mandatory")


class _FalconBCM01CBReading_Type(Integer32):
    """Custom type falconBCM01CBReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconBCM01CBReading_Type.__name__ = "Integer32"
_FalconBCM01CBReading_Object = MibTableColumn
falconBCM01CBReading = _FalconBCM01CBReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 1, 2, 1, 3),
    _FalconBCM01CBReading_Type()
)
falconBCM01CBReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM01CBReading.setStatus("mandatory")
_FalconBCM01CBLabel_Type = DisplayString
_FalconBCM01CBLabel_Object = MibTableColumn
falconBCM01CBLabel = _FalconBCM01CBLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 1, 2, 1, 4),
    _FalconBCM01CBLabel_Type()
)
falconBCM01CBLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM01CBLabel.setStatus("mandatory")
_FalconBCM02_ObjectIdentity = ObjectIdentity
falconBCM02 = _FalconBCM02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 2)
)
_FalconBCM02Label_Type = DisplayString
_FalconBCM02Label_Object = MibScalar
falconBCM02Label = _FalconBCM02Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 2, 1),
    _FalconBCM02Label_Type()
)
falconBCM02Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM02Label.setStatus("mandatory")
_FalconBCM02CBTable_Object = MibTable
falconBCM02CBTable = _FalconBCM02CBTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 2, 2)
)
if mibBuilder.loadTexts:
    falconBCM02CBTable.setStatus("mandatory")
_FalconBCM02CBEntry_Object = MibTableRow
falconBCM02CBEntry = _FalconBCM02CBEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 2, 2, 1)
)
falconBCM02CBEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconBCM02CBIndex"),
)
if mibBuilder.loadTexts:
    falconBCM02CBEntry.setStatus("mandatory")
_FalconBCM02CBIndex_Type = Integer32
_FalconBCM02CBIndex_Object = MibTableColumn
falconBCM02CBIndex = _FalconBCM02CBIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 2, 2, 1, 1),
    _FalconBCM02CBIndex_Type()
)
falconBCM02CBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM02CBIndex.setStatus("mandatory")


class _FalconBCM02CBStatus_Type(Integer32):
    """Custom type falconBCM02CBStatus based on Integer32"""
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
        *(("notConfigured", 0),
          ("offline", 1),
          ("normal", 2),
          ("zeroAmpAlarm", 3),
          ("warning", 4),
          ("alarm", 5))
    )


_FalconBCM02CBStatus_Type.__name__ = "Integer32"
_FalconBCM02CBStatus_Object = MibTableColumn
falconBCM02CBStatus = _FalconBCM02CBStatus_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 2, 2, 1, 2),
    _FalconBCM02CBStatus_Type()
)
falconBCM02CBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM02CBStatus.setStatus("mandatory")


class _FalconBCM02CBReading_Type(Integer32):
    """Custom type falconBCM02CBReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconBCM02CBReading_Type.__name__ = "Integer32"
_FalconBCM02CBReading_Object = MibTableColumn
falconBCM02CBReading = _FalconBCM02CBReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 2, 2, 1, 3),
    _FalconBCM02CBReading_Type()
)
falconBCM02CBReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM02CBReading.setStatus("mandatory")
_FalconBCM02CBLabel_Type = DisplayString
_FalconBCM02CBLabel_Object = MibTableColumn
falconBCM02CBLabel = _FalconBCM02CBLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 2, 2, 1, 4),
    _FalconBCM02CBLabel_Type()
)
falconBCM02CBLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM02CBLabel.setStatus("mandatory")
_FalconBCM03_ObjectIdentity = ObjectIdentity
falconBCM03 = _FalconBCM03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 3)
)
_FalconBCM03Label_Type = DisplayString
_FalconBCM03Label_Object = MibScalar
falconBCM03Label = _FalconBCM03Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 3, 1),
    _FalconBCM03Label_Type()
)
falconBCM03Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM03Label.setStatus("mandatory")
_FalconBCM03CBTable_Object = MibTable
falconBCM03CBTable = _FalconBCM03CBTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 3, 2)
)
if mibBuilder.loadTexts:
    falconBCM03CBTable.setStatus("mandatory")
_FalconBCM03CBEntry_Object = MibTableRow
falconBCM03CBEntry = _FalconBCM03CBEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 3, 2, 1)
)
falconBCM03CBEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconBCM03CBIndex"),
)
if mibBuilder.loadTexts:
    falconBCM03CBEntry.setStatus("mandatory")
_FalconBCM03CBIndex_Type = Integer32
_FalconBCM03CBIndex_Object = MibTableColumn
falconBCM03CBIndex = _FalconBCM03CBIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 3, 2, 1, 1),
    _FalconBCM03CBIndex_Type()
)
falconBCM03CBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM03CBIndex.setStatus("mandatory")


class _FalconBCM03CBStatus_Type(Integer32):
    """Custom type falconBCM03CBStatus based on Integer32"""
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
        *(("notConfigured", 0),
          ("offline", 1),
          ("normal", 2),
          ("zeroAmpAlarm", 3),
          ("warning", 4),
          ("alarm", 5))
    )


_FalconBCM03CBStatus_Type.__name__ = "Integer32"
_FalconBCM03CBStatus_Object = MibTableColumn
falconBCM03CBStatus = _FalconBCM03CBStatus_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 3, 2, 1, 2),
    _FalconBCM03CBStatus_Type()
)
falconBCM03CBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM03CBStatus.setStatus("mandatory")


class _FalconBCM03CBReading_Type(Integer32):
    """Custom type falconBCM03CBReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconBCM03CBReading_Type.__name__ = "Integer32"
_FalconBCM03CBReading_Object = MibTableColumn
falconBCM03CBReading = _FalconBCM03CBReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 3, 2, 1, 3),
    _FalconBCM03CBReading_Type()
)
falconBCM03CBReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM03CBReading.setStatus("mandatory")
_FalconBCM03CBLabel_Type = DisplayString
_FalconBCM03CBLabel_Object = MibTableColumn
falconBCM03CBLabel = _FalconBCM03CBLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 3, 2, 1, 4),
    _FalconBCM03CBLabel_Type()
)
falconBCM03CBLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM03CBLabel.setStatus("mandatory")
_FalconBCM04_ObjectIdentity = ObjectIdentity
falconBCM04 = _FalconBCM04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 4)
)
_FalconBCM04Label_Type = DisplayString
_FalconBCM04Label_Object = MibScalar
falconBCM04Label = _FalconBCM04Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 4, 1),
    _FalconBCM04Label_Type()
)
falconBCM04Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM04Label.setStatus("mandatory")
_FalconBCM04CBTable_Object = MibTable
falconBCM04CBTable = _FalconBCM04CBTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 4, 2)
)
if mibBuilder.loadTexts:
    falconBCM04CBTable.setStatus("mandatory")
_FalconBCM04CBEntry_Object = MibTableRow
falconBCM04CBEntry = _FalconBCM04CBEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 4, 2, 1)
)
falconBCM04CBEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconBCM04CBIndex"),
)
if mibBuilder.loadTexts:
    falconBCM04CBEntry.setStatus("mandatory")
_FalconBCM04CBIndex_Type = Integer32
_FalconBCM04CBIndex_Object = MibTableColumn
falconBCM04CBIndex = _FalconBCM04CBIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 4, 2, 1, 1),
    _FalconBCM04CBIndex_Type()
)
falconBCM04CBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM04CBIndex.setStatus("mandatory")


class _FalconBCM04CBStatus_Type(Integer32):
    """Custom type falconBCM04CBStatus based on Integer32"""
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
        *(("notConfigured", 0),
          ("offline", 1),
          ("normal", 2),
          ("zeroAmpAlarm", 3),
          ("warning", 4),
          ("alarm", 5))
    )


_FalconBCM04CBStatus_Type.__name__ = "Integer32"
_FalconBCM04CBStatus_Object = MibTableColumn
falconBCM04CBStatus = _FalconBCM04CBStatus_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 4, 2, 1, 2),
    _FalconBCM04CBStatus_Type()
)
falconBCM04CBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM04CBStatus.setStatus("mandatory")


class _FalconBCM04CBReading_Type(Integer32):
    """Custom type falconBCM04CBReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconBCM04CBReading_Type.__name__ = "Integer32"
_FalconBCM04CBReading_Object = MibTableColumn
falconBCM04CBReading = _FalconBCM04CBReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 4, 2, 1, 3),
    _FalconBCM04CBReading_Type()
)
falconBCM04CBReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM04CBReading.setStatus("mandatory")
_FalconBCM04CBLabel_Type = DisplayString
_FalconBCM04CBLabel_Object = MibTableColumn
falconBCM04CBLabel = _FalconBCM04CBLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 4, 2, 1, 4),
    _FalconBCM04CBLabel_Type()
)
falconBCM04CBLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM04CBLabel.setStatus("mandatory")
_FalconBCM05_ObjectIdentity = ObjectIdentity
falconBCM05 = _FalconBCM05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 5)
)
_FalconBCM05Label_Type = DisplayString
_FalconBCM05Label_Object = MibScalar
falconBCM05Label = _FalconBCM05Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 5, 1),
    _FalconBCM05Label_Type()
)
falconBCM05Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM05Label.setStatus("mandatory")
_FalconBCM05CBTable_Object = MibTable
falconBCM05CBTable = _FalconBCM05CBTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 5, 2)
)
if mibBuilder.loadTexts:
    falconBCM05CBTable.setStatus("mandatory")
_FalconBCM05CBEntry_Object = MibTableRow
falconBCM05CBEntry = _FalconBCM05CBEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 5, 2, 1)
)
falconBCM05CBEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconBCM05CBIndex"),
)
if mibBuilder.loadTexts:
    falconBCM05CBEntry.setStatus("mandatory")
_FalconBCM05CBIndex_Type = Integer32
_FalconBCM05CBIndex_Object = MibTableColumn
falconBCM05CBIndex = _FalconBCM05CBIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 5, 2, 1, 1),
    _FalconBCM05CBIndex_Type()
)
falconBCM05CBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM05CBIndex.setStatus("mandatory")


class _FalconBCM05CBStatus_Type(Integer32):
    """Custom type falconBCM05CBStatus based on Integer32"""
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
        *(("notConfigured", 0),
          ("offline", 1),
          ("normal", 2),
          ("zeroAmpAlarm", 3),
          ("warning", 4),
          ("alarm", 5))
    )


_FalconBCM05CBStatus_Type.__name__ = "Integer32"
_FalconBCM05CBStatus_Object = MibTableColumn
falconBCM05CBStatus = _FalconBCM05CBStatus_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 5, 2, 1, 2),
    _FalconBCM05CBStatus_Type()
)
falconBCM05CBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM05CBStatus.setStatus("mandatory")


class _FalconBCM05CBReading_Type(Integer32):
    """Custom type falconBCM05CBReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconBCM05CBReading_Type.__name__ = "Integer32"
_FalconBCM05CBReading_Object = MibTableColumn
falconBCM05CBReading = _FalconBCM05CBReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 5, 2, 1, 3),
    _FalconBCM05CBReading_Type()
)
falconBCM05CBReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM05CBReading.setStatus("mandatory")
_FalconBCM05CBLabel_Type = DisplayString
_FalconBCM05CBLabel_Object = MibTableColumn
falconBCM05CBLabel = _FalconBCM05CBLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 5, 2, 1, 4),
    _FalconBCM05CBLabel_Type()
)
falconBCM05CBLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM05CBLabel.setStatus("mandatory")
_FalconBCM06_ObjectIdentity = ObjectIdentity
falconBCM06 = _FalconBCM06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 6)
)
_FalconBCM06Label_Type = DisplayString
_FalconBCM06Label_Object = MibScalar
falconBCM06Label = _FalconBCM06Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 6, 1),
    _FalconBCM06Label_Type()
)
falconBCM06Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM06Label.setStatus("mandatory")
_FalconBCM06CBTable_Object = MibTable
falconBCM06CBTable = _FalconBCM06CBTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 6, 2)
)
if mibBuilder.loadTexts:
    falconBCM06CBTable.setStatus("mandatory")
_FalconBCM06CBEntry_Object = MibTableRow
falconBCM06CBEntry = _FalconBCM06CBEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 6, 2, 1)
)
falconBCM06CBEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconBCM06CBIndex"),
)
if mibBuilder.loadTexts:
    falconBCM06CBEntry.setStatus("mandatory")
_FalconBCM06CBIndex_Type = Integer32
_FalconBCM06CBIndex_Object = MibTableColumn
falconBCM06CBIndex = _FalconBCM06CBIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 6, 2, 1, 1),
    _FalconBCM06CBIndex_Type()
)
falconBCM06CBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM06CBIndex.setStatus("mandatory")


class _FalconBCM06CBStatus_Type(Integer32):
    """Custom type falconBCM06CBStatus based on Integer32"""
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
        *(("notConfigured", 0),
          ("offline", 1),
          ("normal", 2),
          ("zeroAmpAlarm", 3),
          ("warning", 4),
          ("alarm", 5))
    )


_FalconBCM06CBStatus_Type.__name__ = "Integer32"
_FalconBCM06CBStatus_Object = MibTableColumn
falconBCM06CBStatus = _FalconBCM06CBStatus_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 6, 2, 1, 2),
    _FalconBCM06CBStatus_Type()
)
falconBCM06CBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM06CBStatus.setStatus("mandatory")


class _FalconBCM06CBReading_Type(Integer32):
    """Custom type falconBCM06CBReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconBCM06CBReading_Type.__name__ = "Integer32"
_FalconBCM06CBReading_Object = MibTableColumn
falconBCM06CBReading = _FalconBCM06CBReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 6, 2, 1, 3),
    _FalconBCM06CBReading_Type()
)
falconBCM06CBReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM06CBReading.setStatus("mandatory")
_FalconBCM06CBLabel_Type = DisplayString
_FalconBCM06CBLabel_Object = MibTableColumn
falconBCM06CBLabel = _FalconBCM06CBLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 6, 2, 1, 4),
    _FalconBCM06CBLabel_Type()
)
falconBCM06CBLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM06CBLabel.setStatus("mandatory")
_FalconBCM07_ObjectIdentity = ObjectIdentity
falconBCM07 = _FalconBCM07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 7)
)
_FalconBCM07Label_Type = DisplayString
_FalconBCM07Label_Object = MibScalar
falconBCM07Label = _FalconBCM07Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 7, 1),
    _FalconBCM07Label_Type()
)
falconBCM07Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM07Label.setStatus("mandatory")
_FalconBCM07CBTable_Object = MibTable
falconBCM07CBTable = _FalconBCM07CBTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 7, 2)
)
if mibBuilder.loadTexts:
    falconBCM07CBTable.setStatus("mandatory")
_FalconBCM07CBEntry_Object = MibTableRow
falconBCM07CBEntry = _FalconBCM07CBEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 7, 2, 1)
)
falconBCM07CBEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconBCM07CBIndex"),
)
if mibBuilder.loadTexts:
    falconBCM07CBEntry.setStatus("mandatory")
_FalconBCM07CBIndex_Type = Integer32
_FalconBCM07CBIndex_Object = MibTableColumn
falconBCM07CBIndex = _FalconBCM07CBIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 7, 2, 1, 1),
    _FalconBCM07CBIndex_Type()
)
falconBCM07CBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM07CBIndex.setStatus("mandatory")


class _FalconBCM07CBStatus_Type(Integer32):
    """Custom type falconBCM07CBStatus based on Integer32"""
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
        *(("notConfigured", 0),
          ("offline", 1),
          ("normal", 2),
          ("zeroAmpAlarm", 3),
          ("warning", 4),
          ("alarm", 5))
    )


_FalconBCM07CBStatus_Type.__name__ = "Integer32"
_FalconBCM07CBStatus_Object = MibTableColumn
falconBCM07CBStatus = _FalconBCM07CBStatus_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 7, 2, 1, 2),
    _FalconBCM07CBStatus_Type()
)
falconBCM07CBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM07CBStatus.setStatus("mandatory")


class _FalconBCM07CBReading_Type(Integer32):
    """Custom type falconBCM07CBReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconBCM07CBReading_Type.__name__ = "Integer32"
_FalconBCM07CBReading_Object = MibTableColumn
falconBCM07CBReading = _FalconBCM07CBReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 7, 2, 1, 3),
    _FalconBCM07CBReading_Type()
)
falconBCM07CBReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM07CBReading.setStatus("mandatory")
_FalconBCM07CBLabel_Type = DisplayString
_FalconBCM07CBLabel_Object = MibTableColumn
falconBCM07CBLabel = _FalconBCM07CBLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 7, 2, 1, 4),
    _FalconBCM07CBLabel_Type()
)
falconBCM07CBLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM07CBLabel.setStatus("mandatory")
_FalconBCM08_ObjectIdentity = ObjectIdentity
falconBCM08 = _FalconBCM08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 8)
)
_FalconBCM08Label_Type = DisplayString
_FalconBCM08Label_Object = MibScalar
falconBCM08Label = _FalconBCM08Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 8, 1),
    _FalconBCM08Label_Type()
)
falconBCM08Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM08Label.setStatus("mandatory")
_FalconBCM08CBTable_Object = MibTable
falconBCM08CBTable = _FalconBCM08CBTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 8, 2)
)
if mibBuilder.loadTexts:
    falconBCM08CBTable.setStatus("mandatory")
_FalconBCM08CBEntry_Object = MibTableRow
falconBCM08CBEntry = _FalconBCM08CBEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 8, 2, 1)
)
falconBCM08CBEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconBCM08CBIndex"),
)
if mibBuilder.loadTexts:
    falconBCM08CBEntry.setStatus("mandatory")
_FalconBCM08CBIndex_Type = Integer32
_FalconBCM08CBIndex_Object = MibTableColumn
falconBCM08CBIndex = _FalconBCM08CBIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 8, 2, 1, 1),
    _FalconBCM08CBIndex_Type()
)
falconBCM08CBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM08CBIndex.setStatus("mandatory")


class _FalconBCM08CBStatus_Type(Integer32):
    """Custom type falconBCM08CBStatus based on Integer32"""
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
        *(("notConfigured", 0),
          ("offline", 1),
          ("normal", 2),
          ("zeroAmpAlarm", 3),
          ("warning", 4),
          ("alarm", 5))
    )


_FalconBCM08CBStatus_Type.__name__ = "Integer32"
_FalconBCM08CBStatus_Object = MibTableColumn
falconBCM08CBStatus = _FalconBCM08CBStatus_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 8, 2, 1, 2),
    _FalconBCM08CBStatus_Type()
)
falconBCM08CBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM08CBStatus.setStatus("mandatory")


class _FalconBCM08CBReading_Type(Integer32):
    """Custom type falconBCM08CBReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconBCM08CBReading_Type.__name__ = "Integer32"
_FalconBCM08CBReading_Object = MibTableColumn
falconBCM08CBReading = _FalconBCM08CBReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 8, 2, 1, 3),
    _FalconBCM08CBReading_Type()
)
falconBCM08CBReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM08CBReading.setStatus("mandatory")
_FalconBCM08CBLabel_Type = DisplayString
_FalconBCM08CBLabel_Object = MibTableColumn
falconBCM08CBLabel = _FalconBCM08CBLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 8, 2, 1, 4),
    _FalconBCM08CBLabel_Type()
)
falconBCM08CBLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM08CBLabel.setStatus("mandatory")
_FalconBCM09_ObjectIdentity = ObjectIdentity
falconBCM09 = _FalconBCM09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 9)
)
_FalconBCM09Label_Type = DisplayString
_FalconBCM09Label_Object = MibScalar
falconBCM09Label = _FalconBCM09Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 9, 1),
    _FalconBCM09Label_Type()
)
falconBCM09Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM09Label.setStatus("mandatory")
_FalconBCM09CBTable_Object = MibTable
falconBCM09CBTable = _FalconBCM09CBTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 9, 2)
)
if mibBuilder.loadTexts:
    falconBCM09CBTable.setStatus("mandatory")
_FalconBCM09CBEntry_Object = MibTableRow
falconBCM09CBEntry = _FalconBCM09CBEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 9, 2, 1)
)
falconBCM09CBEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconBCM09CBIndex"),
)
if mibBuilder.loadTexts:
    falconBCM09CBEntry.setStatus("mandatory")
_FalconBCM09CBIndex_Type = Integer32
_FalconBCM09CBIndex_Object = MibTableColumn
falconBCM09CBIndex = _FalconBCM09CBIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 9, 2, 1, 1),
    _FalconBCM09CBIndex_Type()
)
falconBCM09CBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM09CBIndex.setStatus("mandatory")


class _FalconBCM09CBStatus_Type(Integer32):
    """Custom type falconBCM09CBStatus based on Integer32"""
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
        *(("notConfigured", 0),
          ("offline", 1),
          ("normal", 2),
          ("zeroAmpAlarm", 3),
          ("warning", 4),
          ("alarm", 5))
    )


_FalconBCM09CBStatus_Type.__name__ = "Integer32"
_FalconBCM09CBStatus_Object = MibTableColumn
falconBCM09CBStatus = _FalconBCM09CBStatus_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 9, 2, 1, 2),
    _FalconBCM09CBStatus_Type()
)
falconBCM09CBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM09CBStatus.setStatus("mandatory")


class _FalconBCM09CBReading_Type(Integer32):
    """Custom type falconBCM09CBReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconBCM09CBReading_Type.__name__ = "Integer32"
_FalconBCM09CBReading_Object = MibTableColumn
falconBCM09CBReading = _FalconBCM09CBReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 9, 2, 1, 3),
    _FalconBCM09CBReading_Type()
)
falconBCM09CBReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM09CBReading.setStatus("mandatory")
_FalconBCM09CBLabel_Type = DisplayString
_FalconBCM09CBLabel_Object = MibTableColumn
falconBCM09CBLabel = _FalconBCM09CBLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 9, 2, 1, 4),
    _FalconBCM09CBLabel_Type()
)
falconBCM09CBLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM09CBLabel.setStatus("mandatory")
_FalconBCM10_ObjectIdentity = ObjectIdentity
falconBCM10 = _FalconBCM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 10)
)
_FalconBCM10Label_Type = DisplayString
_FalconBCM10Label_Object = MibScalar
falconBCM10Label = _FalconBCM10Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 10, 1),
    _FalconBCM10Label_Type()
)
falconBCM10Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM10Label.setStatus("mandatory")
_FalconBCM10CBTable_Object = MibTable
falconBCM10CBTable = _FalconBCM10CBTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 10, 2)
)
if mibBuilder.loadTexts:
    falconBCM10CBTable.setStatus("mandatory")
_FalconBCM10CBEntry_Object = MibTableRow
falconBCM10CBEntry = _FalconBCM10CBEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 10, 2, 1)
)
falconBCM10CBEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconBCM10CBIndex"),
)
if mibBuilder.loadTexts:
    falconBCM10CBEntry.setStatus("mandatory")
_FalconBCM10CBIndex_Type = Integer32
_FalconBCM10CBIndex_Object = MibTableColumn
falconBCM10CBIndex = _FalconBCM10CBIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 10, 2, 1, 1),
    _FalconBCM10CBIndex_Type()
)
falconBCM10CBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM10CBIndex.setStatus("mandatory")


class _FalconBCM10CBStatus_Type(Integer32):
    """Custom type falconBCM10CBStatus based on Integer32"""
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
        *(("notConfigured", 0),
          ("offline", 1),
          ("normal", 2),
          ("zeroAmpAlarm", 3),
          ("warning", 4),
          ("alarm", 5))
    )


_FalconBCM10CBStatus_Type.__name__ = "Integer32"
_FalconBCM10CBStatus_Object = MibTableColumn
falconBCM10CBStatus = _FalconBCM10CBStatus_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 10, 2, 1, 2),
    _FalconBCM10CBStatus_Type()
)
falconBCM10CBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM10CBStatus.setStatus("mandatory")


class _FalconBCM10CBReading_Type(Integer32):
    """Custom type falconBCM10CBReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconBCM10CBReading_Type.__name__ = "Integer32"
_FalconBCM10CBReading_Object = MibTableColumn
falconBCM10CBReading = _FalconBCM10CBReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 10, 2, 1, 3),
    _FalconBCM10CBReading_Type()
)
falconBCM10CBReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM10CBReading.setStatus("mandatory")
_FalconBCM10CBLabel_Type = DisplayString
_FalconBCM10CBLabel_Object = MibTableColumn
falconBCM10CBLabel = _FalconBCM10CBLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 10, 2, 1, 4),
    _FalconBCM10CBLabel_Type()
)
falconBCM10CBLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM10CBLabel.setStatus("mandatory")
_FalconBCM11_ObjectIdentity = ObjectIdentity
falconBCM11 = _FalconBCM11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 11)
)
_FalconBCM11Label_Type = DisplayString
_FalconBCM11Label_Object = MibScalar
falconBCM11Label = _FalconBCM11Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 11, 1),
    _FalconBCM11Label_Type()
)
falconBCM11Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM11Label.setStatus("mandatory")
_FalconBCM11CBTable_Object = MibTable
falconBCM11CBTable = _FalconBCM11CBTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 11, 2)
)
if mibBuilder.loadTexts:
    falconBCM11CBTable.setStatus("mandatory")
_FalconBCM11CBEntry_Object = MibTableRow
falconBCM11CBEntry = _FalconBCM11CBEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 11, 2, 1)
)
falconBCM11CBEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconBCM11CBIndex"),
)
if mibBuilder.loadTexts:
    falconBCM11CBEntry.setStatus("mandatory")
_FalconBCM11CBIndex_Type = Integer32
_FalconBCM11CBIndex_Object = MibTableColumn
falconBCM11CBIndex = _FalconBCM11CBIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 11, 2, 1, 1),
    _FalconBCM11CBIndex_Type()
)
falconBCM11CBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM11CBIndex.setStatus("mandatory")


class _FalconBCM11CBStatus_Type(Integer32):
    """Custom type falconBCM11CBStatus based on Integer32"""
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
        *(("notConfigured", 0),
          ("offline", 1),
          ("normal", 2),
          ("zeroAmpAlarm", 3),
          ("warning", 4),
          ("alarm", 5))
    )


_FalconBCM11CBStatus_Type.__name__ = "Integer32"
_FalconBCM11CBStatus_Object = MibTableColumn
falconBCM11CBStatus = _FalconBCM11CBStatus_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 11, 2, 1, 2),
    _FalconBCM11CBStatus_Type()
)
falconBCM11CBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM11CBStatus.setStatus("mandatory")


class _FalconBCM11CBReading_Type(Integer32):
    """Custom type falconBCM11CBReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconBCM11CBReading_Type.__name__ = "Integer32"
_FalconBCM11CBReading_Object = MibTableColumn
falconBCM11CBReading = _FalconBCM11CBReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 11, 2, 1, 3),
    _FalconBCM11CBReading_Type()
)
falconBCM11CBReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM11CBReading.setStatus("mandatory")
_FalconBCM11CBLabel_Type = DisplayString
_FalconBCM11CBLabel_Object = MibTableColumn
falconBCM11CBLabel = _FalconBCM11CBLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 11, 2, 1, 4),
    _FalconBCM11CBLabel_Type()
)
falconBCM11CBLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM11CBLabel.setStatus("mandatory")
_FalconBCM12_ObjectIdentity = ObjectIdentity
falconBCM12 = _FalconBCM12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 12)
)
_FalconBCM12Label_Type = DisplayString
_FalconBCM12Label_Object = MibScalar
falconBCM12Label = _FalconBCM12Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 12, 1),
    _FalconBCM12Label_Type()
)
falconBCM12Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM12Label.setStatus("mandatory")
_FalconBCM12CBTable_Object = MibTable
falconBCM12CBTable = _FalconBCM12CBTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 12, 2)
)
if mibBuilder.loadTexts:
    falconBCM12CBTable.setStatus("mandatory")
_FalconBCM12CBEntry_Object = MibTableRow
falconBCM12CBEntry = _FalconBCM12CBEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 12, 2, 1)
)
falconBCM12CBEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconBCM12CBIndex"),
)
if mibBuilder.loadTexts:
    falconBCM12CBEntry.setStatus("mandatory")
_FalconBCM12CBIndex_Type = Integer32
_FalconBCM12CBIndex_Object = MibTableColumn
falconBCM12CBIndex = _FalconBCM12CBIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 12, 2, 1, 1),
    _FalconBCM12CBIndex_Type()
)
falconBCM12CBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM12CBIndex.setStatus("mandatory")


class _FalconBCM12CBStatus_Type(Integer32):
    """Custom type falconBCM12CBStatus based on Integer32"""
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
        *(("notConfigured", 0),
          ("offline", 1),
          ("normal", 2),
          ("zeroAmpAlarm", 3),
          ("warning", 4),
          ("alarm", 5))
    )


_FalconBCM12CBStatus_Type.__name__ = "Integer32"
_FalconBCM12CBStatus_Object = MibTableColumn
falconBCM12CBStatus = _FalconBCM12CBStatus_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 12, 2, 1, 2),
    _FalconBCM12CBStatus_Type()
)
falconBCM12CBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM12CBStatus.setStatus("mandatory")


class _FalconBCM12CBReading_Type(Integer32):
    """Custom type falconBCM12CBReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconBCM12CBReading_Type.__name__ = "Integer32"
_FalconBCM12CBReading_Object = MibTableColumn
falconBCM12CBReading = _FalconBCM12CBReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 12, 2, 1, 3),
    _FalconBCM12CBReading_Type()
)
falconBCM12CBReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM12CBReading.setStatus("mandatory")
_FalconBCM12CBLabel_Type = DisplayString
_FalconBCM12CBLabel_Object = MibTableColumn
falconBCM12CBLabel = _FalconBCM12CBLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 12, 2, 1, 4),
    _FalconBCM12CBLabel_Type()
)
falconBCM12CBLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM12CBLabel.setStatus("mandatory")
_FalconBCM13_ObjectIdentity = ObjectIdentity
falconBCM13 = _FalconBCM13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 13)
)
_FalconBCM13Label_Type = DisplayString
_FalconBCM13Label_Object = MibScalar
falconBCM13Label = _FalconBCM13Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 13, 1),
    _FalconBCM13Label_Type()
)
falconBCM13Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM13Label.setStatus("mandatory")
_FalconBCM13CBTable_Object = MibTable
falconBCM13CBTable = _FalconBCM13CBTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 13, 2)
)
if mibBuilder.loadTexts:
    falconBCM13CBTable.setStatus("mandatory")
_FalconBCM13CBEntry_Object = MibTableRow
falconBCM13CBEntry = _FalconBCM13CBEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 13, 2, 1)
)
falconBCM13CBEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconBCM13CBIndex"),
)
if mibBuilder.loadTexts:
    falconBCM13CBEntry.setStatus("mandatory")
_FalconBCM13CBIndex_Type = Integer32
_FalconBCM13CBIndex_Object = MibTableColumn
falconBCM13CBIndex = _FalconBCM13CBIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 13, 2, 1, 1),
    _FalconBCM13CBIndex_Type()
)
falconBCM13CBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM13CBIndex.setStatus("mandatory")


class _FalconBCM13CBStatus_Type(Integer32):
    """Custom type falconBCM13CBStatus based on Integer32"""
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
        *(("notConfigured", 0),
          ("offline", 1),
          ("normal", 2),
          ("zeroAmpAlarm", 3),
          ("warning", 4),
          ("alarm", 5))
    )


_FalconBCM13CBStatus_Type.__name__ = "Integer32"
_FalconBCM13CBStatus_Object = MibTableColumn
falconBCM13CBStatus = _FalconBCM13CBStatus_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 13, 2, 1, 2),
    _FalconBCM13CBStatus_Type()
)
falconBCM13CBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM13CBStatus.setStatus("mandatory")


class _FalconBCM13CBReading_Type(Integer32):
    """Custom type falconBCM13CBReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconBCM13CBReading_Type.__name__ = "Integer32"
_FalconBCM13CBReading_Object = MibTableColumn
falconBCM13CBReading = _FalconBCM13CBReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 13, 2, 1, 3),
    _FalconBCM13CBReading_Type()
)
falconBCM13CBReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM13CBReading.setStatus("mandatory")
_FalconBCM13CBLabel_Type = DisplayString
_FalconBCM13CBLabel_Object = MibTableColumn
falconBCM13CBLabel = _FalconBCM13CBLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 13, 2, 1, 4),
    _FalconBCM13CBLabel_Type()
)
falconBCM13CBLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM13CBLabel.setStatus("mandatory")
_FalconBCM14_ObjectIdentity = ObjectIdentity
falconBCM14 = _FalconBCM14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 14)
)
_FalconBCM14Label_Type = DisplayString
_FalconBCM14Label_Object = MibScalar
falconBCM14Label = _FalconBCM14Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 14, 1),
    _FalconBCM14Label_Type()
)
falconBCM14Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM14Label.setStatus("mandatory")
_FalconBCM14CBTable_Object = MibTable
falconBCM14CBTable = _FalconBCM14CBTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 14, 2)
)
if mibBuilder.loadTexts:
    falconBCM14CBTable.setStatus("mandatory")
_FalconBCM14CBEntry_Object = MibTableRow
falconBCM14CBEntry = _FalconBCM14CBEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 14, 2, 1)
)
falconBCM14CBEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconBCM14CBIndex"),
)
if mibBuilder.loadTexts:
    falconBCM14CBEntry.setStatus("mandatory")
_FalconBCM14CBIndex_Type = Integer32
_FalconBCM14CBIndex_Object = MibTableColumn
falconBCM14CBIndex = _FalconBCM14CBIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 14, 2, 1, 1),
    _FalconBCM14CBIndex_Type()
)
falconBCM14CBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM14CBIndex.setStatus("mandatory")


class _FalconBCM14CBStatus_Type(Integer32):
    """Custom type falconBCM14CBStatus based on Integer32"""
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
        *(("notConfigured", 0),
          ("offline", 1),
          ("normal", 2),
          ("zeroAmpAlarm", 3),
          ("warning", 4),
          ("alarm", 5))
    )


_FalconBCM14CBStatus_Type.__name__ = "Integer32"
_FalconBCM14CBStatus_Object = MibTableColumn
falconBCM14CBStatus = _FalconBCM14CBStatus_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 14, 2, 1, 2),
    _FalconBCM14CBStatus_Type()
)
falconBCM14CBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM14CBStatus.setStatus("mandatory")


class _FalconBCM14CBReading_Type(Integer32):
    """Custom type falconBCM14CBReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconBCM14CBReading_Type.__name__ = "Integer32"
_FalconBCM14CBReading_Object = MibTableColumn
falconBCM14CBReading = _FalconBCM14CBReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 14, 2, 1, 3),
    _FalconBCM14CBReading_Type()
)
falconBCM14CBReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM14CBReading.setStatus("mandatory")
_FalconBCM14CBLabel_Type = DisplayString
_FalconBCM14CBLabel_Object = MibTableColumn
falconBCM14CBLabel = _FalconBCM14CBLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 14, 2, 1, 4),
    _FalconBCM14CBLabel_Type()
)
falconBCM14CBLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM14CBLabel.setStatus("mandatory")
_FalconBCM15_ObjectIdentity = ObjectIdentity
falconBCM15 = _FalconBCM15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 15)
)
_FalconBCM15Label_Type = DisplayString
_FalconBCM15Label_Object = MibScalar
falconBCM15Label = _FalconBCM15Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 15, 1),
    _FalconBCM15Label_Type()
)
falconBCM15Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM15Label.setStatus("mandatory")
_FalconBCM15CBTable_Object = MibTable
falconBCM15CBTable = _FalconBCM15CBTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 15, 2)
)
if mibBuilder.loadTexts:
    falconBCM15CBTable.setStatus("mandatory")
_FalconBCM15CBEntry_Object = MibTableRow
falconBCM15CBEntry = _FalconBCM15CBEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 15, 2, 1)
)
falconBCM15CBEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconBCM15CBIndex"),
)
if mibBuilder.loadTexts:
    falconBCM15CBEntry.setStatus("mandatory")
_FalconBCM15CBIndex_Type = Integer32
_FalconBCM15CBIndex_Object = MibTableColumn
falconBCM15CBIndex = _FalconBCM15CBIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 15, 2, 1, 1),
    _FalconBCM15CBIndex_Type()
)
falconBCM15CBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM15CBIndex.setStatus("mandatory")


class _FalconBCM15CBStatus_Type(Integer32):
    """Custom type falconBCM15CBStatus based on Integer32"""
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
        *(("notConfigured", 0),
          ("offline", 1),
          ("normal", 2),
          ("zeroAmpAlarm", 3),
          ("warning", 4),
          ("alarm", 5))
    )


_FalconBCM15CBStatus_Type.__name__ = "Integer32"
_FalconBCM15CBStatus_Object = MibTableColumn
falconBCM15CBStatus = _FalconBCM15CBStatus_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 15, 2, 1, 2),
    _FalconBCM15CBStatus_Type()
)
falconBCM15CBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM15CBStatus.setStatus("mandatory")


class _FalconBCM15CBReading_Type(Integer32):
    """Custom type falconBCM15CBReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconBCM15CBReading_Type.__name__ = "Integer32"
_FalconBCM15CBReading_Object = MibTableColumn
falconBCM15CBReading = _FalconBCM15CBReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 15, 2, 1, 3),
    _FalconBCM15CBReading_Type()
)
falconBCM15CBReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM15CBReading.setStatus("mandatory")
_FalconBCM15CBLabel_Type = DisplayString
_FalconBCM15CBLabel_Object = MibTableColumn
falconBCM15CBLabel = _FalconBCM15CBLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 15, 2, 1, 4),
    _FalconBCM15CBLabel_Type()
)
falconBCM15CBLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM15CBLabel.setStatus("mandatory")
_FalconBCM16_ObjectIdentity = ObjectIdentity
falconBCM16 = _FalconBCM16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 16)
)
_FalconBCM16Label_Type = DisplayString
_FalconBCM16Label_Object = MibScalar
falconBCM16Label = _FalconBCM16Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 16, 1),
    _FalconBCM16Label_Type()
)
falconBCM16Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM16Label.setStatus("mandatory")
_FalconBCM16CBTable_Object = MibTable
falconBCM16CBTable = _FalconBCM16CBTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 16, 2)
)
if mibBuilder.loadTexts:
    falconBCM16CBTable.setStatus("mandatory")
_FalconBCM16CBEntry_Object = MibTableRow
falconBCM16CBEntry = _FalconBCM16CBEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 16, 2, 1)
)
falconBCM16CBEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconBCM16CBIndex"),
)
if mibBuilder.loadTexts:
    falconBCM16CBEntry.setStatus("mandatory")
_FalconBCM16CBIndex_Type = Integer32
_FalconBCM16CBIndex_Object = MibTableColumn
falconBCM16CBIndex = _FalconBCM16CBIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 16, 2, 1, 1),
    _FalconBCM16CBIndex_Type()
)
falconBCM16CBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM16CBIndex.setStatus("mandatory")


class _FalconBCM16CBStatus_Type(Integer32):
    """Custom type falconBCM16CBStatus based on Integer32"""
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
        *(("notConfigured", 0),
          ("offline", 1),
          ("normal", 2),
          ("zeroAmpAlarm", 3),
          ("warning", 4),
          ("alarm", 5))
    )


_FalconBCM16CBStatus_Type.__name__ = "Integer32"
_FalconBCM16CBStatus_Object = MibTableColumn
falconBCM16CBStatus = _FalconBCM16CBStatus_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 16, 2, 1, 2),
    _FalconBCM16CBStatus_Type()
)
falconBCM16CBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM16CBStatus.setStatus("mandatory")


class _FalconBCM16CBReading_Type(Integer32):
    """Custom type falconBCM16CBReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconBCM16CBReading_Type.__name__ = "Integer32"
_FalconBCM16CBReading_Object = MibTableColumn
falconBCM16CBReading = _FalconBCM16CBReading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 16, 2, 1, 3),
    _FalconBCM16CBReading_Type()
)
falconBCM16CBReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM16CBReading.setStatus("mandatory")
_FalconBCM16CBLabel_Type = DisplayString
_FalconBCM16CBLabel_Object = MibTableColumn
falconBCM16CBLabel = _FalconBCM16CBLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 1, 16, 2, 1, 4),
    _FalconBCM16CBLabel_Type()
)
falconBCM16CBLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconBCM16CBLabel.setStatus("mandatory")
_FalconBCMTrap_ObjectIdentity = ObjectIdentity
falconBCMTrap = _FalconBCMTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 2)
)
_FalconBCMTrapClear_ObjectIdentity = ObjectIdentity
falconBCMTrapClear = _FalconBCMTrapClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 3)
)
_FalconXbG628_ObjectIdentity = ObjectIdentity
falconXbG628 = _FalconXbG628_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 4)
)
_FalconXbUnits_ObjectIdentity = ObjectIdentity
falconXbUnits = _FalconXbUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 4, 1)
)
_FalconXbUnitsTable_Object = MibTable
falconXbUnitsTable = _FalconXbUnitsTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 4, 1, 1)
)
if mibBuilder.loadTexts:
    falconXbUnitsTable.setStatus("mandatory")
_FalconXbUnitsEntry_Object = MibTableRow
falconXbUnitsEntry = _FalconXbUnitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 4, 1, 1, 1)
)
falconXbUnitsEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
)
if mibBuilder.loadTexts:
    falconXbUnitsEntry.setStatus("mandatory")
_FalconXbUnitsIndex_Type = Integer32
_FalconXbUnitsIndex_Object = MibTableColumn
falconXbUnitsIndex = _FalconXbUnitsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 4, 1, 1, 1, 1),
    _FalconXbUnitsIndex_Type()
)
falconXbUnitsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconXbUnitsIndex.setStatus("mandatory")


class _FalconXbUnitsStatus_Type(Integer32):
    """Custom type falconXbUnitsStatus based on Integer32"""
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
        *(("notConfigured", 0),
          ("offline", 1),
          ("normal", 2),
          ("alarm", 3))
    )


_FalconXbUnitsStatus_Type.__name__ = "Integer32"
_FalconXbUnitsStatus_Object = MibTableColumn
falconXbUnitsStatus = _FalconXbUnitsStatus_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 4, 1, 1, 1, 2),
    _FalconXbUnitsStatus_Type()
)
falconXbUnitsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconXbUnitsStatus.setStatus("mandatory")
_FalconXbUnitsLabel_Type = DisplayString
_FalconXbUnitsLabel_Object = MibTableColumn
falconXbUnitsLabel = _FalconXbUnitsLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 4, 1, 1, 1, 3),
    _FalconXbUnitsLabel_Type()
)
falconXbUnitsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconXbUnitsLabel.setStatus("mandatory")
_FalconXbusTrapData_ObjectIdentity = ObjectIdentity
falconXbusTrapData = _FalconXbusTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 4, 2)
)
_FalconXbusTrapRegisterNumber_Type = PositiveInteger
_FalconXbusTrapRegisterNumber_Object = MibScalar
falconXbusTrapRegisterNumber = _FalconXbusTrapRegisterNumber_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 4, 2, 1),
    _FalconXbusTrapRegisterNumber_Type()
)
falconXbusTrapRegisterNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    falconXbusTrapRegisterNumber.setStatus("mandatory")
_FalconXbusTrapRegisterLabel_Type = DisplayString
_FalconXbusTrapRegisterLabel_Object = MibScalar
falconXbusTrapRegisterLabel = _FalconXbusTrapRegisterLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 4, 2, 2),
    _FalconXbusTrapRegisterLabel_Type()
)
falconXbusTrapRegisterLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    falconXbusTrapRegisterLabel.setStatus("mandatory")
_FalconXbusRegisterTable_Object = MibTable
falconXbusRegisterTable = _FalconXbusRegisterTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 4, 3)
)
if mibBuilder.loadTexts:
    falconXbusRegisterTable.setStatus("mandatory")
_FalconXbusRegisterEntry_Object = MibTableRow
falconXbusRegisterEntry = _FalconXbusRegisterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 4, 3, 1)
)
falconXbusRegisterEntry.setIndexNames(
    (0, "RLE-FALCON-EM-MIB", "falconXbusRegisterIndex"),
)
if mibBuilder.loadTexts:
    falconXbusRegisterEntry.setStatus("mandatory")
_FalconXbusRegisterIndex_Type = Integer32
_FalconXbusRegisterIndex_Object = MibTableColumn
falconXbusRegisterIndex = _FalconXbusRegisterIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 4, 3, 1, 1),
    _FalconXbusRegisterIndex_Type()
)
falconXbusRegisterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconXbusRegisterIndex.setStatus("mandatory")


class _FalconXbusRegisterType_Type(Integer32):
    """Custom type falconXbusRegisterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", 0),
          ("analog", 1),
          ("binary", 2))
    )


_FalconXbusRegisterType_Type.__name__ = "Integer32"
_FalconXbusRegisterType_Object = MibTableColumn
falconXbusRegisterType = _FalconXbusRegisterType_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 4, 3, 1, 2),
    _FalconXbusRegisterType_Type()
)
falconXbusRegisterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconXbusRegisterType.setStatus("mandatory")


class _FalconXbusRegisterData_Type(Integer32):
    """Custom type falconXbusRegisterData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconXbusRegisterData_Type.__name__ = "Integer32"
_FalconXbusRegisterData_Object = MibTableColumn
falconXbusRegisterData = _FalconXbusRegisterData_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 4, 3, 1, 3),
    _FalconXbusRegisterData_Type()
)
falconXbusRegisterData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconXbusRegisterData.setStatus("mandatory")
_FalconXbusRegisterLabel_Type = DisplayString
_FalconXbusRegisterLabel_Object = MibTableColumn
falconXbusRegisterLabel = _FalconXbusRegisterLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 4, 3, 1, 4),
    _FalconXbusRegisterLabel_Type()
)
falconXbusRegisterLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconXbusRegisterLabel.setStatus("mandatory")
_FalconXbusTraps_ObjectIdentity = ObjectIdentity
falconXbusTraps = _FalconXbusTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 5)
)
_FalconXbusTrapsClear_ObjectIdentity = ObjectIdentity
falconXbusTrapsClear = _FalconXbusTrapsClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 6)
)
_Fms_X_ObjectIdentity = ObjectIdentity
fms_X = _Fms_X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 2)
)
_Fms_A_ObjectIdentity = ObjectIdentity
fms_A = _Fms_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 3)
)
_Fms_B_ObjectIdentity = ObjectIdentity
fms_B = _Fms_B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 4)
)
_Fms_C_ObjectIdentity = ObjectIdentity
fms_C = _Fms_C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 5)
)
_Fms_AAxx_ObjectIdentity = ObjectIdentity
fms_AAxx = _Fms_AAxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 3300)
)
_Fms_AAAx_ObjectIdentity = ObjectIdentity
fms_AAAx = _Fms_AAAx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 3330)
)
_Fms_AAAA_ObjectIdentity = ObjectIdentity
fms_AAAA = _Fms_AAAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 3333)
)
_Fms_AAAC_ObjectIdentity = ObjectIdentity
fms_AAAC = _Fms_AAAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 3335)
)
_Fms_AABx_ObjectIdentity = ObjectIdentity
fms_AABx = _Fms_AABx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 3340)
)
_Fms_AABB_ObjectIdentity = ObjectIdentity
fms_AABB = _Fms_AABB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 3344)
)
_Fms_AACx_ObjectIdentity = ObjectIdentity
fms_AACx = _Fms_AACx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 3350)
)
_Fms_AACC_ObjectIdentity = ObjectIdentity
fms_AACC = _Fms_AACC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 3355)
)
_Fms_ABxx_ObjectIdentity = ObjectIdentity
fms_ABxx = _Fms_ABxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 3400)
)
_Fms_ABBx_ObjectIdentity = ObjectIdentity
fms_ABBx = _Fms_ABBx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 3440)
)
_Fms_ABBB_ObjectIdentity = ObjectIdentity
fms_ABBB = _Fms_ABBB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 3444)
)
_Fms_ABBC_ObjectIdentity = ObjectIdentity
fms_ABBC = _Fms_ABBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 3445)
)
_Fms_ABCx_ObjectIdentity = ObjectIdentity
fms_ABCx = _Fms_ABCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 3450)
)
_Fms_ABCC_ObjectIdentity = ObjectIdentity
fms_ABCC = _Fms_ABCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 3455)
)
_Fms_ACxx_ObjectIdentity = ObjectIdentity
fms_ACxx = _Fms_ACxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 3500)
)
_Fms_ACCx_ObjectIdentity = ObjectIdentity
fms_ACCx = _Fms_ACCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 3550)
)
_Fms_ACCC_ObjectIdentity = ObjectIdentity
fms_ACCC = _Fms_ACCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 3555)
)
_Fms_BBxx_ObjectIdentity = ObjectIdentity
fms_BBxx = _Fms_BBxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 4400)
)
_Fms_BBBx_ObjectIdentity = ObjectIdentity
fms_BBBx = _Fms_BBBx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 4440)
)
_Fms_BBBB_ObjectIdentity = ObjectIdentity
fms_BBBB = _Fms_BBBB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 4444)
)
_Fms_BBBC_ObjectIdentity = ObjectIdentity
fms_BBBC = _Fms_BBBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 4445)
)
_Fms_BBCx_ObjectIdentity = ObjectIdentity
fms_BBCx = _Fms_BBCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 4450)
)
_Fms_BBCC_ObjectIdentity = ObjectIdentity
fms_BBCC = _Fms_BBCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 4455)
)
_Fms_BCxx_ObjectIdentity = ObjectIdentity
fms_BCxx = _Fms_BCxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 4500)
)
_Fms_BCCx_ObjectIdentity = ObjectIdentity
fms_BCCx = _Fms_BCCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 4550)
)
_Fms_BCCC_ObjectIdentity = ObjectIdentity
fms_BCCC = _Fms_BCCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 4555)
)
_Fms_CxCC_ObjectIdentity = ObjectIdentity
fms_CxCC = _Fms_CxCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 5055)
)
_Fms_CCxx_ObjectIdentity = ObjectIdentity
fms_CCxx = _Fms_CCxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 5500)
)
_Fms_CCxC_ObjectIdentity = ObjectIdentity
fms_CCxC = _Fms_CCxC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 5505)
)
_Fms_CCCx_ObjectIdentity = ObjectIdentity
fms_CCCx = _Fms_CCCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 5550)
)
_Fms_CCCC_ObjectIdentity = ObjectIdentity
fms_CCCC = _Fms_CCCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 5555)
)

# Managed Objects groups


# Notification objects

falconAlarmEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 6, 0, 1)
)
if mibBuilder.loadTexts:
    falconAlarmEntryAdded.setStatus(
        ""
    )

falconAlarmEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 6, 0, 2)
)
if mibBuilder.loadTexts:
    falconAlarmEntryRemoved.setStatus(
        ""
    )

falconAccessGranted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 6, 0, 3)
)
if mibBuilder.loadTexts:
    falconAccessGranted.setStatus(
        ""
    )

falconAccessDenied = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 6, 0, 4)
)
if mibBuilder.loadTexts:
    falconAccessDenied.setStatus(
        ""
    )

falconPageUnsuccessful = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 6, 0, 5)
)
falconPageUnsuccessful.setObjects(
    ("RLE-FALCON-EM-MIB", "falconPagerStatusString")
)
if mibBuilder.loadTexts:
    falconPageUnsuccessful.setStatus(
        ""
    )

falconConfigurationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 6, 0, 6)
)
falconConfigurationChanged.setObjects(
    ("RLE-FALCON-EM-MIB", "falconWebUser")
)
if mibBuilder.loadTexts:
    falconConfigurationChanged.setStatus(
        ""
    )

falconPort01Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 1)
)
falconPort01Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort01Trap.setStatus(
        ""
    )

falconPort02Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 2)
)
falconPort02Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort02Trap.setStatus(
        ""
    )

falconPort03Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 3)
)
falconPort03Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort03Trap.setStatus(
        ""
    )

falconPort04Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 4)
)
falconPort04Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort04Trap.setStatus(
        ""
    )

falconPort05Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 5)
)
falconPort05Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort05Trap.setStatus(
        ""
    )

falconPort06Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 6)
)
falconPort06Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort06Trap.setStatus(
        ""
    )

falconPort07Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 7)
)
falconPort07Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort07Trap.setStatus(
        ""
    )

falconPort08Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 8)
)
falconPort08Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort08Trap.setStatus(
        ""
    )

falconPort09Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 9)
)
falconPort09Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort09Trap.setStatus(
        ""
    )

falconPort10Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 10)
)
falconPort10Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort10Trap.setStatus(
        ""
    )

falconPort11Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 11)
)
falconPort11Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort11Trap.setStatus(
        ""
    )

falconPort12Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 12)
)
falconPort12Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort12Trap.setStatus(
        ""
    )

falconPort13Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 13)
)
falconPort13Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort13Trap.setStatus(
        ""
    )

falconPort14Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 14)
)
falconPort14Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort14Trap.setStatus(
        ""
    )

falconPort15Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 15)
)
falconPort15Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort15Trap.setStatus(
        ""
    )

falconPort16Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 16)
)
falconPort16Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort16Trap.setStatus(
        ""
    )

falconPort17Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 17)
)
falconPort17Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort17Trap.setStatus(
        ""
    )

falconPort18Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 18)
)
falconPort18Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort18Trap.setStatus(
        ""
    )

falconPort19Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 19)
)
falconPort19Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort19Trap.setStatus(
        ""
    )

falconPort20Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 20)
)
falconPort20Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort20Trap.setStatus(
        ""
    )

falconPort21Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 21)
)
falconPort21Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort21Trap.setStatus(
        ""
    )

falconPort22Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 22)
)
falconPort22Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort22Trap.setStatus(
        ""
    )

falconPort23Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 23)
)
falconPort23Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort23Trap.setStatus(
        ""
    )

falconPort24Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 24)
)
falconPort24Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort24Trap.setStatus(
        ""
    )

falconPort25Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 25)
)
falconPort25Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort25Trap.setStatus(
        ""
    )

falconPort26Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 26)
)
falconPort26Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort26Trap.setStatus(
        ""
    )

falconPort27Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 27)
)
falconPort27Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort27Trap.setStatus(
        ""
    )

falconPort28Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 28)
)
falconPort28Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort28Trap.setStatus(
        ""
    )

falconPort29Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 29)
)
falconPort29Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort29Trap.setStatus(
        ""
    )

falconPort30Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 30)
)
falconPort30Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort30Trap.setStatus(
        ""
    )

falconPort31Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 31)
)
falconPort31Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort31Trap.setStatus(
        ""
    )

falconPort32Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 32)
)
falconPort32Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort32Trap.setStatus(
        ""
    )

falconPort33Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 33)
)
falconPort33Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort33Trap.setStatus(
        ""
    )

falconPort34Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 34)
)
falconPort34Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort34Trap.setStatus(
        ""
    )

falconPort35Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 35)
)
falconPort35Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort35Trap.setStatus(
        ""
    )

falconPort36Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 36)
)
falconPort36Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort36Trap.setStatus(
        ""
    )

falconPort37Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 37)
)
falconPort37Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort37Trap.setStatus(
        ""
    )

falconPort38Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 38)
)
falconPort38Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort38Trap.setStatus(
        ""
    )

falconPort39Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 39)
)
falconPort39Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort39Trap.setStatus(
        ""
    )

falconPort40Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 40)
)
falconPort40Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort40Trap.setStatus(
        ""
    )

falconPort41Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 41)
)
falconPort41Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort41Trap.setStatus(
        ""
    )

falconPort42Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 42)
)
falconPort42Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort42Trap.setStatus(
        ""
    )

falconPort43Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 43)
)
falconPort43Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort43Trap.setStatus(
        ""
    )

falconPort44Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 44)
)
falconPort44Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort44Trap.setStatus(
        ""
    )

falconPort45Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 45)
)
falconPort45Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort45Trap.setStatus(
        ""
    )

falconPort46Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 46)
)
falconPort46Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort46Trap.setStatus(
        ""
    )

falconPort47Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 47)
)
falconPort47Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort47Trap.setStatus(
        ""
    )

falconPort48Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 48)
)
falconPort48Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort48Trap.setStatus(
        ""
    )

falconPort49Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 49)
)
falconPort49Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort49Trap.setStatus(
        ""
    )

falconPort50Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 50)
)
falconPort50Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort50Trap.setStatus(
        ""
    )

falconPort51Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 51)
)
falconPort51Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort51Trap.setStatus(
        ""
    )

falconPort52Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 52)
)
falconPort52Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort52Trap.setStatus(
        ""
    )

falconPort53Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 53)
)
falconPort53Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort53Trap.setStatus(
        ""
    )

falconPort54Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 54)
)
falconPort54Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort54Trap.setStatus(
        ""
    )

falconPort55Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 55)
)
falconPort55Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort55Trap.setStatus(
        ""
    )

falconPort56Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 56)
)
falconPort56Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort56Trap.setStatus(
        ""
    )

falconPort57Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 57)
)
falconPort57Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort57Trap.setStatus(
        ""
    )

falconPort58Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 58)
)
falconPort58Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort58Trap.setStatus(
        ""
    )

falconPort59Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 59)
)
falconPort59Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort59Trap.setStatus(
        ""
    )

falconPort60Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 60)
)
falconPort60Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort60Trap.setStatus(
        ""
    )

falconPort61Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 61)
)
falconPort61Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort61Trap.setStatus(
        ""
    )

falconPort62Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 62)
)
falconPort62Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort62Trap.setStatus(
        ""
    )

falconPort63Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 63)
)
falconPort63Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort63Trap.setStatus(
        ""
    )

falconPort64Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 64)
)
falconPort64Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort64Trap.setStatus(
        ""
    )

falconPort65Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 65)
)
falconPort65Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort65Trap.setStatus(
        ""
    )

falconPort66Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 66)
)
falconPort66Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort66Trap.setStatus(
        ""
    )

falconPort67Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 67)
)
falconPort67Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort67Trap.setStatus(
        ""
    )

falconPort68Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 68)
)
falconPort68Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort68Trap.setStatus(
        ""
    )

falconPort69Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 69)
)
falconPort69Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort69Trap.setStatus(
        ""
    )

falconPort70Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 70)
)
falconPort70Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort70Trap.setStatus(
        ""
    )

falconPort71Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 71)
)
falconPort71Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort71Trap.setStatus(
        ""
    )

falconPort72Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 72)
)
falconPort72Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort72Trap.setStatus(
        ""
    )

falconPort73Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 73)
)
falconPort73Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort73Trap.setStatus(
        ""
    )

falconPort74Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 74)
)
falconPort74Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort74Trap.setStatus(
        ""
    )

falconPort75Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 75)
)
falconPort75Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort75Trap.setStatus(
        ""
    )

falconPort76Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 76)
)
falconPort76Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort76Trap.setStatus(
        ""
    )

falconPort77Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 77)
)
falconPort77Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort77Trap.setStatus(
        ""
    )

falconPort78Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 78)
)
falconPort78Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort78Trap.setStatus(
        ""
    )

falconPort79Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 79)
)
falconPort79Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort79Trap.setStatus(
        ""
    )

falconPort80Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 80)
)
falconPort80Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort80Trap.setStatus(
        ""
    )

falconPort81Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 81)
)
falconPort81Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort81Trap.setStatus(
        ""
    )

falconPort82Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 82)
)
falconPort82Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort82Trap.setStatus(
        ""
    )

falconPort83Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 83)
)
falconPort83Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort83Trap.setStatus(
        ""
    )

falconPort84Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 84)
)
falconPort84Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort84Trap.setStatus(
        ""
    )

falconPort85Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 85)
)
falconPort85Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort85Trap.setStatus(
        ""
    )

falconPort86Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 86)
)
falconPort86Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort86Trap.setStatus(
        ""
    )

falconPort87Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 87)
)
falconPort87Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort87Trap.setStatus(
        ""
    )

falconPort88Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 88)
)
falconPort88Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort88Trap.setStatus(
        ""
    )

falconPort89Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 89)
)
falconPort89Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort89Trap.setStatus(
        ""
    )

falconPort90Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 90)
)
falconPort90Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort90Trap.setStatus(
        ""
    )

falconPort91Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 91)
)
falconPort91Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort91Trap.setStatus(
        ""
    )

falconPort92Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 92)
)
falconPort92Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort92Trap.setStatus(
        ""
    )

falconPort93Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 93)
)
falconPort93Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort93Trap.setStatus(
        ""
    )

falconPort94Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 94)
)
falconPort94Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort94Trap.setStatus(
        ""
    )

falconPort95Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 95)
)
falconPort95Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort95Trap.setStatus(
        ""
    )

falconPort96Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 96)
)
falconPort96Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort96Trap.setStatus(
        ""
    )

falconPort97Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 97)
)
falconPort97Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort97Trap.setStatus(
        ""
    )

falconPort98Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 98)
)
falconPort98Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort98Trap.setStatus(
        ""
    )

falconPort99Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 99)
)
falconPort99Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort99Trap.setStatus(
        ""
    )

falconPort100Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 100)
)
falconPort100Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort100Trap.setStatus(
        ""
    )

falconPort101Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 101)
)
falconPort101Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort101Trap.setStatus(
        ""
    )

falconPort102Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 102)
)
falconPort102Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort102Trap.setStatus(
        ""
    )

falconPort103Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 103)
)
falconPort103Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort103Trap.setStatus(
        ""
    )

falconPort104Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 104)
)
falconPort104Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort104Trap.setStatus(
        ""
    )

falconTemperatureSensorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 105)
)
falconTemperatureSensorTrap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconTemperatureSensorLabel"),
        ("RLE-FALCON-EM-MIB", "falconTemperatureSensorReading"),
        ("RLE-FALCON-EM-MIB", "falconTemperatureSensorUOM"))
)
if mibBuilder.loadTexts:
    falconTemperatureSensorTrap.setStatus(
        ""
    )

falconHumiditySensorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 10, 0, 106)
)
falconHumiditySensorTrap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconHumiditySensorLabel"),
        ("RLE-FALCON-EM-MIB", "falconHumiditySensorReading"),
        ("RLE-FALCON-EM-MIB", "falconHumiditySensorUOM"))
)
if mibBuilder.loadTexts:
    falconHumiditySensorTrap.setStatus(
        ""
    )

falconPort01TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 1)
)
falconPort01TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort01TrapClear.setStatus(
        ""
    )

falconPort02TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 2)
)
falconPort02TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort02TrapClear.setStatus(
        ""
    )

falconPort03TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 3)
)
falconPort03TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort03TrapClear.setStatus(
        ""
    )

falconPort04TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 4)
)
falconPort04TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort04TrapClear.setStatus(
        ""
    )

falconPort05TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 5)
)
falconPort05TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort05TrapClear.setStatus(
        ""
    )

falconPort06TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 6)
)
falconPort06TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort06TrapClear.setStatus(
        ""
    )

falconPort07TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 7)
)
falconPort07TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort07TrapClear.setStatus(
        ""
    )

falconPort08TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 8)
)
falconPort08TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort08TrapClear.setStatus(
        ""
    )

falconPort09TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 9)
)
falconPort09TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort09TrapClear.setStatus(
        ""
    )

falconPort10TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 10)
)
falconPort10TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort10TrapClear.setStatus(
        ""
    )

falconPort11TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 11)
)
falconPort11TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort11TrapClear.setStatus(
        ""
    )

falconPort12TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 12)
)
falconPort12TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort12TrapClear.setStatus(
        ""
    )

falconPort13TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 13)
)
falconPort13TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort13TrapClear.setStatus(
        ""
    )

falconPort14TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 14)
)
falconPort14TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort14TrapClear.setStatus(
        ""
    )

falconPort15TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 15)
)
falconPort15TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort15TrapClear.setStatus(
        ""
    )

falconPort16TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 16)
)
falconPort16TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort16TrapClear.setStatus(
        ""
    )

falconPort17TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 17)
)
falconPort17TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort17TrapClear.setStatus(
        ""
    )

falconPort18TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 18)
)
falconPort18TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort18TrapClear.setStatus(
        ""
    )

falconPort19TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 19)
)
falconPort19TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort19TrapClear.setStatus(
        ""
    )

falconPort20TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 20)
)
falconPort20TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort20TrapClear.setStatus(
        ""
    )

falconPort21TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 21)
)
falconPort21TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort21TrapClear.setStatus(
        ""
    )

falconPort22TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 22)
)
falconPort22TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort22TrapClear.setStatus(
        ""
    )

falconPort23TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 23)
)
falconPort23TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort23TrapClear.setStatus(
        ""
    )

falconPort24TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 24)
)
falconPort24TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort24TrapClear.setStatus(
        ""
    )

falconPort25TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 25)
)
falconPort25TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort25TrapClear.setStatus(
        ""
    )

falconPort26TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 26)
)
falconPort26TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort26TrapClear.setStatus(
        ""
    )

falconPort27TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 27)
)
falconPort27TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort27TrapClear.setStatus(
        ""
    )

falconPort28TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 28)
)
falconPort28TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort28TrapClear.setStatus(
        ""
    )

falconPort29TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 29)
)
falconPort29TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort29TrapClear.setStatus(
        ""
    )

falconPort30TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 30)
)
falconPort30TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort30TrapClear.setStatus(
        ""
    )

falconPort31TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 31)
)
falconPort31TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort31TrapClear.setStatus(
        ""
    )

falconPort32TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 32)
)
falconPort32TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort32TrapClear.setStatus(
        ""
    )

falconPort33TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 33)
)
falconPort33TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort33TrapClear.setStatus(
        ""
    )

falconPort34TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 34)
)
falconPort34TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort34TrapClear.setStatus(
        ""
    )

falconPort35TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 35)
)
falconPort35TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort35TrapClear.setStatus(
        ""
    )

falconPort36TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 36)
)
falconPort36TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort36TrapClear.setStatus(
        ""
    )

falconPort37TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 37)
)
falconPort37TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort37TrapClear.setStatus(
        ""
    )

falconPort38TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 38)
)
falconPort38TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort38TrapClear.setStatus(
        ""
    )

falconPort39TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 39)
)
falconPort39TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort39TrapClear.setStatus(
        ""
    )

falconPort40TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 40)
)
falconPort40TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort40TrapClear.setStatus(
        ""
    )

falconPort41TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 41)
)
falconPort41TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort41TrapClear.setStatus(
        ""
    )

falconPort42TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 42)
)
falconPort42TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort42TrapClear.setStatus(
        ""
    )

falconPort43TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 43)
)
falconPort43TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort43TrapClear.setStatus(
        ""
    )

falconPort44TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 44)
)
falconPort44TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort44TrapClear.setStatus(
        ""
    )

falconPort45TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 45)
)
falconPort45TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort45TrapClear.setStatus(
        ""
    )

falconPort46TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 46)
)
falconPort46TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort46TrapClear.setStatus(
        ""
    )

falconPort47TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 47)
)
falconPort47TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort47TrapClear.setStatus(
        ""
    )

falconPort48TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 48)
)
falconPort48TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort48TrapClear.setStatus(
        ""
    )

falconPort49TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 49)
)
falconPort49TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort49TrapClear.setStatus(
        ""
    )

falconPort50TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 50)
)
falconPort50TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort50TrapClear.setStatus(
        ""
    )

falconPort51TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 51)
)
falconPort51TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort51TrapClear.setStatus(
        ""
    )

falconPort52TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 52)
)
falconPort52TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort52TrapClear.setStatus(
        ""
    )

falconPort53TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 53)
)
falconPort53TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort53TrapClear.setStatus(
        ""
    )

falconPort54TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 54)
)
falconPort54TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort54TrapClear.setStatus(
        ""
    )

falconPort55TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 55)
)
falconPort55TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort55TrapClear.setStatus(
        ""
    )

falconPort56TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 56)
)
falconPort56TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort56TrapClear.setStatus(
        ""
    )

falconPort57TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 57)
)
falconPort57TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort57TrapClear.setStatus(
        ""
    )

falconPort58TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 58)
)
falconPort58TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort58TrapClear.setStatus(
        ""
    )

falconPort59TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 59)
)
falconPort59TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort59TrapClear.setStatus(
        ""
    )

falconPort60TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 60)
)
falconPort60TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort60TrapClear.setStatus(
        ""
    )

falconPort61TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 61)
)
falconPort61TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort61TrapClear.setStatus(
        ""
    )

falconPort62TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 62)
)
falconPort62TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort62TrapClear.setStatus(
        ""
    )

falconPort63TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 63)
)
falconPort63TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort63TrapClear.setStatus(
        ""
    )

falconPort64TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 64)
)
falconPort64TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort64TrapClear.setStatus(
        ""
    )

falconPort65TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 65)
)
falconPort65TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort65TrapClear.setStatus(
        ""
    )

falconPort66TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 66)
)
falconPort66TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort66TrapClear.setStatus(
        ""
    )

falconPort67TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 67)
)
falconPort67TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort67TrapClear.setStatus(
        ""
    )

falconPort68TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 68)
)
falconPort68TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort68TrapClear.setStatus(
        ""
    )

falconPort69TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 69)
)
falconPort69TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort69TrapClear.setStatus(
        ""
    )

falconPort70TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 70)
)
falconPort70TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort70TrapClear.setStatus(
        ""
    )

falconPort71TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 71)
)
falconPort71TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort71TrapClear.setStatus(
        ""
    )

falconPort72TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 72)
)
falconPort72TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort72TrapClear.setStatus(
        ""
    )

falconPort73TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 73)
)
falconPort73TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort73TrapClear.setStatus(
        ""
    )

falconPort74TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 74)
)
falconPort74TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort74TrapClear.setStatus(
        ""
    )

falconPort75TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 75)
)
falconPort75TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort75TrapClear.setStatus(
        ""
    )

falconPort76TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 76)
)
falconPort76TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort76TrapClear.setStatus(
        ""
    )

falconPort77TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 77)
)
falconPort77TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort77TrapClear.setStatus(
        ""
    )

falconPort78TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 78)
)
falconPort78TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort78TrapClear.setStatus(
        ""
    )

falconPort79TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 79)
)
falconPort79TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort79TrapClear.setStatus(
        ""
    )

falconPort80TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 80)
)
falconPort80TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort80TrapClear.setStatus(
        ""
    )

falconPort81TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 81)
)
falconPort81TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort81TrapClear.setStatus(
        ""
    )

falconPort82TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 82)
)
falconPort82TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort82TrapClear.setStatus(
        ""
    )

falconPort83TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 83)
)
falconPort83TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort83TrapClear.setStatus(
        ""
    )

falconPort84TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 84)
)
falconPort84TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort84TrapClear.setStatus(
        ""
    )

falconPort85TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 85)
)
falconPort85TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort85TrapClear.setStatus(
        ""
    )

falconPort86TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 86)
)
falconPort86TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort86TrapClear.setStatus(
        ""
    )

falconPort87TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 87)
)
falconPort87TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort87TrapClear.setStatus(
        ""
    )

falconPort88TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 88)
)
falconPort88TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort88TrapClear.setStatus(
        ""
    )

falconPort89TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 89)
)
falconPort89TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort89TrapClear.setStatus(
        ""
    )

falconPort90TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 90)
)
falconPort90TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort90TrapClear.setStatus(
        ""
    )

falconPort91TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 91)
)
falconPort91TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort91TrapClear.setStatus(
        ""
    )

falconPort92TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 92)
)
falconPort92TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort92TrapClear.setStatus(
        ""
    )

falconPort93TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 93)
)
falconPort93TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort93TrapClear.setStatus(
        ""
    )

falconPort94TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 94)
)
falconPort94TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort94TrapClear.setStatus(
        ""
    )

falconPort95TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 95)
)
falconPort95TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort95TrapClear.setStatus(
        ""
    )

falconPort96TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 96)
)
falconPort96TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort96TrapClear.setStatus(
        ""
    )

falconPort97TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 97)
)
falconPort97TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort97TrapClear.setStatus(
        ""
    )

falconPort98TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 98)
)
falconPort98TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort98TrapClear.setStatus(
        ""
    )

falconPort99TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 99)
)
falconPort99TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort99TrapClear.setStatus(
        ""
    )

falconPort100TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 100)
)
falconPort100TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort100TrapClear.setStatus(
        ""
    )

falconPort101TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 101)
)
falconPort101TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort101TrapClear.setStatus(
        ""
    )

falconPort102TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 102)
)
falconPort102TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort102TrapClear.setStatus(
        ""
    )

falconPort103TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 103)
)
falconPort103TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort103TrapClear.setStatus(
        ""
    )

falconPort104TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 104)
)
falconPort104TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconInputLabel"),
        ("RLE-FALCON-EM-MIB", "falconInputReading"),
        ("RLE-FALCON-EM-MIB", "falconInputUOM"))
)
if mibBuilder.loadTexts:
    falconPort104TrapClear.setStatus(
        ""
    )

falconTemperatureSensorTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 105)
)
falconTemperatureSensorTrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconTemperatureSensorLabel"),
        ("RLE-FALCON-EM-MIB", "falconTemperatureSensorReading"),
        ("RLE-FALCON-EM-MIB", "falconTemperatureSensorUOM"))
)
if mibBuilder.loadTexts:
    falconTemperatureSensorTrapClear.setStatus(
        ""
    )

falconHumiditySensorTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 11, 0, 106)
)
falconHumiditySensorTrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconAlarmDescr"),
        ("RLE-FALCON-EM-MIB", "falconHumiditySensorLabel"),
        ("RLE-FALCON-EM-MIB", "falconHumiditySensorReading"),
        ("RLE-FALCON-EM-MIB", "falconHumiditySensorUOM"))
)
if mibBuilder.loadTexts:
    falconHumiditySensorTrapClear.setStatus(
        ""
    )

falconBCM01Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 2, 0, 1)
)
falconBCM01Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM01CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM01CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM01CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM01CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM01Trap.setStatus(
        ""
    )

falconBCM10Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 2, 0, 1)
)
falconBCM10Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM11CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM11CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM11CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM11CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM10Trap.setStatus(
        ""
    )

falconBCM02Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 2, 0, 2)
)
falconBCM02Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM02CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM02CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM02CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM02CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM02Trap.setStatus(
        ""
    )

falconBCM03Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 2, 0, 3)
)
falconBCM03Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM03CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM03CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM03CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM03CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM03Trap.setStatus(
        ""
    )

falconBCM04Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 2, 0, 4)
)
falconBCM04Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM04CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM04CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM04CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM04CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM04Trap.setStatus(
        ""
    )

falconBCM05Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 2, 0, 5)
)
falconBCM05Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM05CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM05CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM05CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM05CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM05Trap.setStatus(
        ""
    )

falconBCM06Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 2, 0, 6)
)
falconBCM06Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM06CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM06CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM06CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM06CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM06Trap.setStatus(
        ""
    )

falconBCM07Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 2, 0, 7)
)
falconBCM07Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM07CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM07CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM07CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM07CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM07Trap.setStatus(
        ""
    )

falconBCM08Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 2, 0, 8)
)
falconBCM08Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM08CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM08CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM08CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM08CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM08Trap.setStatus(
        ""
    )

falconBCM09Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 2, 0, 9)
)
falconBCM09Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM09CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM09CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM09CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM09CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM09Trap.setStatus(
        ""
    )

falconBCM11Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 2, 0, 11)
)
falconBCM11Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM11CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM11CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM11CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM11CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM11Trap.setStatus(
        ""
    )

falconBCM12Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 2, 0, 12)
)
falconBCM12Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM12CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM12CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM12CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM12CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM12Trap.setStatus(
        ""
    )

falconBCM13Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 2, 0, 13)
)
falconBCM13Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM13CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM13CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM13CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM13CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM13Trap.setStatus(
        ""
    )

falconBCM14Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 2, 0, 14)
)
falconBCM14Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM14CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM14CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM14CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM14CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM14Trap.setStatus(
        ""
    )

falconBCM15Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 2, 0, 15)
)
falconBCM15Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM15CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM15CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM15CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM15CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM15Trap.setStatus(
        ""
    )

falconBCM16Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 2, 0, 16)
)
falconBCM16Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM16CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM16CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM16CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM16CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM16Trap.setStatus(
        ""
    )

falconBCM01TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 3, 0, 1)
)
falconBCM01TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM01CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM01CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM01CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM01CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM01TrapClear.setStatus(
        ""
    )

falconBCM02TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 3, 0, 2)
)
falconBCM02TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM02CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM02CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM02CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM02CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM02TrapClear.setStatus(
        ""
    )

falconBCM03TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 3, 0, 3)
)
falconBCM03TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM03CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM03CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM03CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM03CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM03TrapClear.setStatus(
        ""
    )

falconBCM04TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 3, 0, 4)
)
falconBCM04TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM04CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM04CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM04CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM04CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM04TrapClear.setStatus(
        ""
    )

falconBCM05TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 3, 0, 5)
)
falconBCM05TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM05CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM05CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM05CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM05CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM05TrapClear.setStatus(
        ""
    )

falconBCM06TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 3, 0, 6)
)
falconBCM06TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM06CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM06CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM06CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM06CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM06TrapClear.setStatus(
        ""
    )

falconBCM07TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 3, 0, 7)
)
falconBCM07TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM07CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM07CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM07CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM07CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM07TrapClear.setStatus(
        ""
    )

falconBCM08TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 3, 0, 8)
)
falconBCM08TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM08CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM08CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM08CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM08CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM08TrapClear.setStatus(
        ""
    )

falconBCM09TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 3, 0, 9)
)
falconBCM09TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM09CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM09CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM09CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM09CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM09TrapClear.setStatus(
        ""
    )

falconBCM10TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 3, 0, 10)
)
falconBCM10TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM10CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM10CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM10CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM10CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM10TrapClear.setStatus(
        ""
    )

falconBCM11TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 3, 0, 11)
)
falconBCM11TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM11CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM11CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM11CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM11CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM11TrapClear.setStatus(
        ""
    )

falconBCM12TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 3, 0, 12)
)
falconBCM12TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM12CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM12CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM12CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM12CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM12TrapClear.setStatus(
        ""
    )

falconBCM13TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 3, 0, 13)
)
falconBCM13TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM13CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM13CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM13CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM13CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM13TrapClear.setStatus(
        ""
    )

falconBCM14TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 3, 0, 14)
)
falconBCM14TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM14CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM14CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM14CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM14CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM14TrapClear.setStatus(
        ""
    )

falconBCM15TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 3, 0, 15)
)
falconBCM15TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM15CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM15CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM15CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM15CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM15TrapClear.setStatus(
        ""
    )

falconBCM16TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 3, 0, 16)
)
falconBCM16TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconBCM16CBIndex"),
        ("RLE-FALCON-EM-MIB", "falconBCM16CBStatus"),
        ("RLE-FALCON-EM-MIB", "falconBCM16CBLabel"),
        ("RLE-FALCON-EM-MIB", "falconBCM16CBReading"))
)
if mibBuilder.loadTexts:
    falconBCM16TrapClear.setStatus(
        ""
    )

falconXbusUnit01Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 5, 0, 1)
)
falconXbusUnit01Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit01Trap.setStatus(
        ""
    )

falconXbusUnit02Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 5, 0, 2)
)
falconXbusUnit02Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit02Trap.setStatus(
        ""
    )

falconXbusUnit03Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 5, 0, 3)
)
falconXbusUnit03Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit03Trap.setStatus(
        ""
    )

falconXbusUnit04Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 5, 0, 4)
)
falconXbusUnit04Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit04Trap.setStatus(
        ""
    )

falconXbusUnit05Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 5, 0, 5)
)
falconXbusUnit05Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit05Trap.setStatus(
        ""
    )

falconXbusUnit06Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 5, 0, 6)
)
falconXbusUnit06Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit06Trap.setStatus(
        ""
    )

falconXbusUnit07Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 5, 0, 7)
)
falconXbusUnit07Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit07Trap.setStatus(
        ""
    )

falconXbusUnit08Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 5, 0, 8)
)
falconXbusUnit08Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit08Trap.setStatus(
        ""
    )

falconXbusUnit09Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 5, 0, 9)
)
falconXbusUnit09Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit09Trap.setStatus(
        ""
    )

falconXbusUnit10Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 5, 0, 10)
)
falconXbusUnit10Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit10Trap.setStatus(
        ""
    )

falconXbusUnit11Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 5, 0, 11)
)
falconXbusUnit11Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit11Trap.setStatus(
        ""
    )

falconXbusUnit12Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 5, 0, 12)
)
falconXbusUnit12Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit12Trap.setStatus(
        ""
    )

falconXbusUnit13Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 5, 0, 13)
)
falconXbusUnit13Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit13Trap.setStatus(
        ""
    )

falconXbusUnit14Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 5, 0, 14)
)
falconXbusUnit14Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit14Trap.setStatus(
        ""
    )

falconXbusUnit15Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 5, 0, 15)
)
falconXbusUnit15Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit15Trap.setStatus(
        ""
    )

falconXbusUnit16Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 5, 0, 16)
)
falconXbusUnit16Trap.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit16Trap.setStatus(
        ""
    )

falconXbusUnit01TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 6, 0, 1)
)
falconXbusUnit01TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit01TrapClear.setStatus(
        ""
    )

falconXbusUnit02TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 6, 0, 2)
)
falconXbusUnit02TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit02TrapClear.setStatus(
        ""
    )

falconXbusUnit03TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 6, 0, 3)
)
falconXbusUnit03TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit03TrapClear.setStatus(
        ""
    )

falconXbusUnit04TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 6, 0, 4)
)
falconXbusUnit04TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit04TrapClear.setStatus(
        ""
    )

falconXbusUnit05TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 6, 0, 5)
)
falconXbusUnit05TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit05TrapClear.setStatus(
        ""
    )

falconXbusUnit06TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 6, 0, 6)
)
falconXbusUnit06TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit06TrapClear.setStatus(
        ""
    )

falconXbusUnit07TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 6, 0, 7)
)
falconXbusUnit07TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit07TrapClear.setStatus(
        ""
    )

falconXbusUnit08TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 6, 0, 8)
)
falconXbusUnit08TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit08TrapClear.setStatus(
        ""
    )

falconXbusUnit09TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 6, 0, 9)
)
falconXbusUnit09TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit09TrapClear.setStatus(
        ""
    )

falconXbusUnit10TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 6, 0, 10)
)
falconXbusUnit10TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit10TrapClear.setStatus(
        ""
    )

falconXbusUnit11TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 6, 0, 11)
)
falconXbusUnit11TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit11TrapClear.setStatus(
        ""
    )

falconXbusUnit12TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 6, 0, 12)
)
falconXbusUnit12TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit12TrapClear.setStatus(
        ""
    )

falconXbusUnit13TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 6, 0, 13)
)
falconXbusUnit13TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit13TrapClear.setStatus(
        ""
    )

falconXbusUnit14TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 6, 0, 14)
)
falconXbusUnit14TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit14TrapClear.setStatus(
        ""
    )

falconXbusUnit15TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 6, 0, 15)
)
falconXbusUnit15TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit15TrapClear.setStatus(
        ""
    )

falconXbusUnit16TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 5, 1, 12, 6, 0, 16)
)
falconXbusUnit16TrapClear.setObjects(
      *(("RLE-FALCON-EM-MIB", "falconAlarmId"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsIndex"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsStatus"),
        ("RLE-FALCON-EM-MIB", "falconXbUnitsLabel"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterNumber"),
        ("RLE-FALCON-EM-MIB", "falconXbusTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    falconXbusUnit16TrapClear.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RLE-FALCON-EM-MIB",
    **{"PositiveInteger": PositiveInteger,
       "rle": rle,
       "products": products,
       "falcon-em": falcon_em,
       "falcon-emMIB": falcon_emMIB,
       "falconIdent": falconIdent,
       "falconIdentManufacturer": falconIdentManufacturer,
       "falconIdentModel": falconIdentModel,
       "falconIdentSoftwareVersion": falconIdentSoftwareVersion,
       "falconIdentSpecific": falconIdentSpecific,
       "falconOptionCards": falconOptionCards,
       "falconOptionCard1": falconOptionCard1,
       "falconOptionCard2": falconOptionCard2,
       "falconOptionCard3": falconOptionCard3,
       "falconOptionCard4": falconOptionCard4,
       "falconSystem": falconSystem,
       "falconSystemSettings": falconSystemSettings,
       "falconClock": falconClock,
       "falconDoorAlarmBypass": falconDoorAlarmBypass,
       "falconInputVoltage": falconInputVoltage,
       "falconLowBatteryThreshold": falconLowBatteryThreshold,
       "falconAnalogAverage": falconAnalogAverage,
       "falconPagerStatusString": falconPagerStatusString,
       "falconWebUser": falconWebUser,
       "falconMaintenanceMode": falconMaintenanceMode,
       "falconKeypad": falconKeypad,
       "falconKeypadUsers": falconKeypadUsers,
       "falconKeypadUsersTable": falconKeypadUsersTable,
       "falconKeypadUserEntry": falconKeypadUserEntry,
       "falconKeypadUserIndex": falconKeypadUserIndex,
       "falconKeypadCode": falconKeypadCode,
       "falconKeypadName": falconKeypadName,
       "falconInputs": falconInputs,
       "falconInputPorts": falconInputPorts,
       "falconNumberOfInputPorts": falconNumberOfInputPorts,
       "falconInputTable": falconInputTable,
       "falconInputEntry": falconInputEntry,
       "falconInputIndex": falconInputIndex,
       "falconInputType": falconInputType,
       "falconInputState": falconInputState,
       "falconInputReading": falconInputReading,
       "falconInputGain": falconInputGain,
       "falconInputOffset": falconInputOffset,
       "falconInputLabel": falconInputLabel,
       "falconInputUOM": falconInputUOM,
       "falconInputHighLimit2": falconInputHighLimit2,
       "falconInputHighLimit": falconInputHighLimit,
       "falconInputLowLimit": falconInputLowLimit,
       "falconInputLowLimit2": falconInputLowLimit2,
       "falconInputDelay": falconInputDelay,
       "falconInputHysteresis": falconInputHysteresis,
       "falconInputSchedule": falconInputSchedule,
       "falconInputDigOffLabel": falconInputDigOffLabel,
       "falconTHSensors": falconTHSensors,
       "falconTempSensors": falconTempSensors,
       "falconNumberOfTempSensors": falconNumberOfTempSensors,
       "falconTSTable": falconTSTable,
       "falconTSEntry": falconTSEntry,
       "falconTSIndex": falconTSIndex,
       "falconTemperatureSensorState": falconTemperatureSensorState,
       "falconTemperatureSensorReading": falconTemperatureSensorReading,
       "falconTemperatureSensorOffset": falconTemperatureSensorOffset,
       "falconTemperatureSensorLabel": falconTemperatureSensorLabel,
       "falconTemperatureSensorUOM": falconTemperatureSensorUOM,
       "falconTemperatureSensorHighLimit2": falconTemperatureSensorHighLimit2,
       "falconTemperatureSensorHighLimit": falconTemperatureSensorHighLimit,
       "falconTemperatureSensorLowLimit": falconTemperatureSensorLowLimit,
       "falconTemperatureSensorLowLimit2": falconTemperatureSensorLowLimit2,
       "falconTemperatureSensorDelay": falconTemperatureSensorDelay,
       "falconTemperatureSensorHysteresis": falconTemperatureSensorHysteresis,
       "falconTemperatureSensorSchedule": falconTemperatureSensorSchedule,
       "falconHumiditySensors": falconHumiditySensors,
       "falconNumberOfHumiditySensors": falconNumberOfHumiditySensors,
       "falconHSTable": falconHSTable,
       "falconHSEntry": falconHSEntry,
       "falconHSIndex": falconHSIndex,
       "falconHumiditySensorState": falconHumiditySensorState,
       "falconHumiditySensorReading": falconHumiditySensorReading,
       "falconHumiditySensorOffset": falconHumiditySensorOffset,
       "falconHumiditySensorLabel": falconHumiditySensorLabel,
       "falconHumiditySensorUOM": falconHumiditySensorUOM,
       "falconHumiditySensorHighLimit2": falconHumiditySensorHighLimit2,
       "falconHumiditySensorHighLimit": falconHumiditySensorHighLimit,
       "falconHumiditySensorLowLimit": falconHumiditySensorLowLimit,
       "falconHumiditySensorLowLimit2": falconHumiditySensorLowLimit2,
       "falconHumiditySensorDelay": falconHumiditySensorDelay,
       "falconHumiditySensorHysteresis": falconHumiditySensorHysteresis,
       "falconHumiditySensorSchedule": falconHumiditySensorSchedule,
       "falconOutputs": falconOutputs,
       "falconRelays": falconRelays,
       "falconNumberOfRelays": falconNumberOfRelays,
       "falconRelayTable": falconRelayTable,
       "falconRelayEntry": falconRelayEntry,
       "falconRelayIndex": falconRelayIndex,
       "falconRelayState": falconRelayState,
       "falconRelayStatus": falconRelayStatus,
       "falconRelayLabel": falconRelayLabel,
       "falconRelayTime": falconRelayTime,
       "falconRelaySchedule": falconRelaySchedule,
       "falconAlarms": falconAlarms,
       "falconAlarmsPresent": falconAlarmsPresent,
       "falconAlarmTable": falconAlarmTable,
       "falconAlarmEntry": falconAlarmEntry,
       "falconAlarmId": falconAlarmId,
       "falconAlarmDescr": falconAlarmDescr,
       "falconWellKnownAlarms": falconWellKnownAlarms,
       "falconInput1DigAlarm": falconInput1DigAlarm,
       "falconInput1HighAlarm": falconInput1HighAlarm,
       "falconInput1LowAlarm": falconInput1LowAlarm,
       "falconInput1High2Alarm": falconInput1High2Alarm,
       "falconInput1Low2Alarm": falconInput1Low2Alarm,
       "falconInput2DigAlarm": falconInput2DigAlarm,
       "falconInput2HighAlarm": falconInput2HighAlarm,
       "falconInput2LowAlarm": falconInput2LowAlarm,
       "falconInput2High2Alarm": falconInput2High2Alarm,
       "falconInput2Low2Alarm": falconInput2Low2Alarm,
       "falconInput3DigAlarm": falconInput3DigAlarm,
       "falconInput3HighAlarm": falconInput3HighAlarm,
       "falconInput3LowAlarm": falconInput3LowAlarm,
       "falconInput3High2Alarm": falconInput3High2Alarm,
       "falconInput3Low2Alarm": falconInput3Low2Alarm,
       "falconInput4DigAlarm": falconInput4DigAlarm,
       "falconInput4HighAlarm": falconInput4HighAlarm,
       "falconInput4LowAlarm": falconInput4LowAlarm,
       "falconInput4High2Alarm": falconInput4High2Alarm,
       "falconInput4Low2Alarm": falconInput4Low2Alarm,
       "falconInput5DigAlarm": falconInput5DigAlarm,
       "falconInput5HighAlarm": falconInput5HighAlarm,
       "falconInput5LowAlarm": falconInput5LowAlarm,
       "falconInput5High2Alarm": falconInput5High2Alarm,
       "falconInput5Low2Alarm": falconInput5Low2Alarm,
       "falconInput6DigAlarm": falconInput6DigAlarm,
       "falconInput6HighAlarm": falconInput6HighAlarm,
       "falconInput6LowAlarm": falconInput6LowAlarm,
       "falconInput6High2Alarm": falconInput6High2Alarm,
       "falconInput6Low2Alarm": falconInput6Low2Alarm,
       "falconInput7DigAlarm": falconInput7DigAlarm,
       "falconInput7HighAlarm": falconInput7HighAlarm,
       "falconInput7LowAlarm": falconInput7LowAlarm,
       "falconInput7High2Alarm": falconInput7High2Alarm,
       "falconInput7Low2Alarm": falconInput7Low2Alarm,
       "falconInput8DigAlarm": falconInput8DigAlarm,
       "falconInput8HighAlarm": falconInput8HighAlarm,
       "falconInput8LowAlarm": falconInput8LowAlarm,
       "falconInput8High2Alarm": falconInput8High2Alarm,
       "falconInput8Low2Alarm": falconInput8Low2Alarm,
       "falconInput9DigAlarm": falconInput9DigAlarm,
       "falconInput9HighAlarm": falconInput9HighAlarm,
       "falconInput9LowAlarm": falconInput9LowAlarm,
       "falconInput9High2Alarm": falconInput9High2Alarm,
       "falconInput9Low2Alarm": falconInput9Low2Alarm,
       "falconInput10DigAlarm": falconInput10DigAlarm,
       "falconInput10HighAlarm": falconInput10HighAlarm,
       "falconInput10LowAlarm": falconInput10LowAlarm,
       "falconInput10High2Alarm": falconInput10High2Alarm,
       "falconInput10Low2Alarm": falconInput10Low2Alarm,
       "falconInput11DigAlarm": falconInput11DigAlarm,
       "falconInput11HighAlarm": falconInput11HighAlarm,
       "falconInput11LowAlarm": falconInput11LowAlarm,
       "falconInput11High2Alarm": falconInput11High2Alarm,
       "falconInput11Low2Alarm": falconInput11Low2Alarm,
       "falconInput12DigAlarm": falconInput12DigAlarm,
       "falconInput12HighAlarm": falconInput12HighAlarm,
       "falconInput12LowAlarm": falconInput12LowAlarm,
       "falconInput12High2Alarm": falconInput12High2Alarm,
       "falconInput12Low2Alarm": falconInput12Low2Alarm,
       "falconInput13DigAlarm": falconInput13DigAlarm,
       "falconInput13HighAlarm": falconInput13HighAlarm,
       "falconInput13LowAlarm": falconInput13LowAlarm,
       "falconInput13High2Alarm": falconInput13High2Alarm,
       "falconInput13Low2Alarm": falconInput13Low2Alarm,
       "falconInput14DigAlarm": falconInput14DigAlarm,
       "falconInput14HighAlarm": falconInput14HighAlarm,
       "falconInput14LowAlarm": falconInput14LowAlarm,
       "falconInput14High2Alarm": falconInput14High2Alarm,
       "falconInput14Low2Alarm": falconInput14Low2Alarm,
       "falconInput15DigAlarm": falconInput15DigAlarm,
       "falconInput15HighAlarm": falconInput15HighAlarm,
       "falconInput15LowAlarm": falconInput15LowAlarm,
       "falconInput15High2Alarm": falconInput15High2Alarm,
       "falconInput15Low2Alarm": falconInput15Low2Alarm,
       "falconInput16DigAlarm": falconInput16DigAlarm,
       "falconInput16HighAlarm": falconInput16HighAlarm,
       "falconInput16LowAlarm": falconInput16LowAlarm,
       "falconInput16High2Alarm": falconInput16High2Alarm,
       "falconInput16Low2Alarm": falconInput16Low2Alarm,
       "falconInput17DigAlarm": falconInput17DigAlarm,
       "falconInput17HighAlarm": falconInput17HighAlarm,
       "falconInput17LowAlarm": falconInput17LowAlarm,
       "falconInput17High2Alarm": falconInput17High2Alarm,
       "falconInput17Low2Alarm": falconInput17Low2Alarm,
       "falconInput18DigAlarm": falconInput18DigAlarm,
       "falconInput18HighAlarm": falconInput18HighAlarm,
       "falconInput18LowAlarm": falconInput18LowAlarm,
       "falconInput18High2Alarm": falconInput18High2Alarm,
       "falconInput18Low2Alarm": falconInput18Low2Alarm,
       "falconInput19DigAlarm": falconInput19DigAlarm,
       "falconInput19HighAlarm": falconInput19HighAlarm,
       "falconInput19LowAlarm": falconInput19LowAlarm,
       "falconInput19High2Alarm": falconInput19High2Alarm,
       "falconInput19Low2Alarm": falconInput19Low2Alarm,
       "falconInput20DigAlarm": falconInput20DigAlarm,
       "falconInput20HighAlarm": falconInput20HighAlarm,
       "falconInput20LowAlarm": falconInput20LowAlarm,
       "falconInput20High2Alarm": falconInput20High2Alarm,
       "falconInput20Low2Alarm": falconInput20Low2Alarm,
       "falconInput21DigAlarm": falconInput21DigAlarm,
       "falconInput22DigAlarm": falconInput22DigAlarm,
       "falconInput23DigAlarm": falconInput23DigAlarm,
       "falconInput24DigAlarm": falconInput24DigAlarm,
       "falconInput25DigAlarm": falconInput25DigAlarm,
       "falconInput26DigAlarm": falconInput26DigAlarm,
       "falconInput27DigAlarm": falconInput27DigAlarm,
       "falconInput28DigAlarm": falconInput28DigAlarm,
       "falconInput29DigAlarm": falconInput29DigAlarm,
       "falconInput30DigAlarm": falconInput30DigAlarm,
       "falconInput31DigAlarm": falconInput31DigAlarm,
       "falconInput32DigAlarm": falconInput32DigAlarm,
       "falconInput33DigAlarm": falconInput33DigAlarm,
       "falconInput33HighAlarm": falconInput33HighAlarm,
       "falconInput33LowAlarm": falconInput33LowAlarm,
       "falconInput33High2Alarm": falconInput33High2Alarm,
       "falconInput33Low2Alarm": falconInput33Low2Alarm,
       "falconInput34DigAlarm": falconInput34DigAlarm,
       "falconInput34HighAlarm": falconInput34HighAlarm,
       "falconInput34LowAlarm": falconInput34LowAlarm,
       "falconInput34High2Alarm": falconInput34High2Alarm,
       "falconInput34Low2Alarm": falconInput34Low2Alarm,
       "falconInput35DigAlarm": falconInput35DigAlarm,
       "falconInput35HighAlarm": falconInput35HighAlarm,
       "falconInput35LowAlarm": falconInput35LowAlarm,
       "falconInput35High2Alarm": falconInput35High2Alarm,
       "falconInput35Low2Alarm": falconInput35Low2Alarm,
       "falconInput36DigAlarm": falconInput36DigAlarm,
       "falconInput36HighAlarm": falconInput36HighAlarm,
       "falconInput36LowAlarm": falconInput36LowAlarm,
       "falconInput36High2Alarm": falconInput36High2Alarm,
       "falconInput36Low2Alarm": falconInput36Low2Alarm,
       "falconInput37DigAlarm": falconInput37DigAlarm,
       "falconInput37HighAlarm": falconInput37HighAlarm,
       "falconInput37LowAlarm": falconInput37LowAlarm,
       "falconInput37High2Alarm": falconInput37High2Alarm,
       "falconInput37Low2Alarm": falconInput37Low2Alarm,
       "falconInput38DigAlarm": falconInput38DigAlarm,
       "falconInput38HighAlarm": falconInput38HighAlarm,
       "falconInput38LowAlarm": falconInput38LowAlarm,
       "falconInput38High2Alarm": falconInput38High2Alarm,
       "falconInput38Low2Alarm": falconInput38Low2Alarm,
       "falconInput39DigAlarm": falconInput39DigAlarm,
       "falconInput39HighAlarm": falconInput39HighAlarm,
       "falconInput39LowAlarm": falconInput39LowAlarm,
       "falconInput39High2Alarm": falconInput39High2Alarm,
       "falconInput39Low2Alarm": falconInput39Low2Alarm,
       "falconInput40DigAlarm": falconInput40DigAlarm,
       "falconInput40HighAlarm": falconInput40HighAlarm,
       "falconInput40LowAlarm": falconInput40LowAlarm,
       "falconInput40High2Alarm": falconInput40High2Alarm,
       "falconInput40Low2Alarm": falconInput40Low2Alarm,
       "falconInput41DigAlarm": falconInput41DigAlarm,
       "falconInput41HighAlarm": falconInput41HighAlarm,
       "falconInput41LowAlarm": falconInput41LowAlarm,
       "falconInput41High2Alarm": falconInput41High2Alarm,
       "falconInput41Low2Alarm": falconInput41Low2Alarm,
       "falconInput42DigAlarm": falconInput42DigAlarm,
       "falconInput42HighAlarm": falconInput42HighAlarm,
       "falconInput42LowAlarm": falconInput42LowAlarm,
       "falconInput42High2Alarm": falconInput42High2Alarm,
       "falconInput42Low2Alarm": falconInput42Low2Alarm,
       "falconInput43DigAlarm": falconInput43DigAlarm,
       "falconInput43HighAlarm": falconInput43HighAlarm,
       "falconInput43LowAlarm": falconInput43LowAlarm,
       "falconInput43High2Alarm": falconInput43High2Alarm,
       "falconInput43Low2Alarm": falconInput43Low2Alarm,
       "falconInput44DigAlarm": falconInput44DigAlarm,
       "falconInput44HighAlarm": falconInput44HighAlarm,
       "falconInput44LowAlarm": falconInput44LowAlarm,
       "falconInput44High2Alarm": falconInput44High2Alarm,
       "falconInput44Low2Alarm": falconInput44Low2Alarm,
       "falconInput45DigAlarm": falconInput45DigAlarm,
       "falconInput46DigAlarm": falconInput46DigAlarm,
       "falconInput47DigAlarm": falconInput47DigAlarm,
       "falconInput48DigAlarm": falconInput48DigAlarm,
       "falconInput49DigAlarm": falconInput49DigAlarm,
       "falconInput50DigAlarm": falconInput50DigAlarm,
       "falconInput51DigAlarm": falconInput51DigAlarm,
       "falconInput52DigAlarm": falconInput52DigAlarm,
       "falconInput53DigAlarm": falconInput53DigAlarm,
       "falconInput54DigAlarm": falconInput54DigAlarm,
       "falconInput55DigAlarm": falconInput55DigAlarm,
       "falconInput56DigAlarm": falconInput56DigAlarm,
       "falconInput57DigAlarm": falconInput57DigAlarm,
       "falconInput57HighAlarm": falconInput57HighAlarm,
       "falconInput57LowAlarm": falconInput57LowAlarm,
       "falconInput57High2Alarm": falconInput57High2Alarm,
       "falconInput57Low2Alarm": falconInput57Low2Alarm,
       "falconInput58DigAlarm": falconInput58DigAlarm,
       "falconInput58HighAlarm": falconInput58HighAlarm,
       "falconInput58LowAlarm": falconInput58LowAlarm,
       "falconInput58High2Alarm": falconInput58High2Alarm,
       "falconInput58Low2Alarm": falconInput58Low2Alarm,
       "falconInput59DigAlarm": falconInput59DigAlarm,
       "falconInput59HighAlarm": falconInput59HighAlarm,
       "falconInput59LowAlarm": falconInput59LowAlarm,
       "falconInput59High2Alarm": falconInput59High2Alarm,
       "falconInput59Low2Alarm": falconInput59Low2Alarm,
       "falconInput60DigAlarm": falconInput60DigAlarm,
       "falconInput60HighAlarm": falconInput60HighAlarm,
       "falconInput60LowAlarm": falconInput60LowAlarm,
       "falconInput60High2Alarm": falconInput60High2Alarm,
       "falconInput60Low2Alarm": falconInput60Low2Alarm,
       "falconInput61DigAlarm": falconInput61DigAlarm,
       "falconInput61HighAlarm": falconInput61HighAlarm,
       "falconInput61LowAlarm": falconInput61LowAlarm,
       "falconInput61High2Alarm": falconInput61High2Alarm,
       "falconInput61Low2Alarm": falconInput61Low2Alarm,
       "falconInput62DigAlarm": falconInput62DigAlarm,
       "falconInput62HighAlarm": falconInput62HighAlarm,
       "falconInput62LowAlarm": falconInput62LowAlarm,
       "falconInput62High2Alarm": falconInput62High2Alarm,
       "falconInput62Low2Alarm": falconInput62Low2Alarm,
       "falconInput63DigAlarm": falconInput63DigAlarm,
       "falconInput63HighAlarm": falconInput63HighAlarm,
       "falconInput63LowAlarm": falconInput63LowAlarm,
       "falconInput63High2Alarm": falconInput63High2Alarm,
       "falconInput63Low2Alarm": falconInput63Low2Alarm,
       "falconInput64DigAlarm": falconInput64DigAlarm,
       "falconInput64HighAlarm": falconInput64HighAlarm,
       "falconInput64LowAlarm": falconInput64LowAlarm,
       "falconInput64High2Alarm": falconInput64High2Alarm,
       "falconInput64Low2Alarm": falconInput64Low2Alarm,
       "falconInput65DigAlarm": falconInput65DigAlarm,
       "falconInput65HighAlarm": falconInput65HighAlarm,
       "falconInput65LowAlarm": falconInput65LowAlarm,
       "falconInput65High2Alarm": falconInput65High2Alarm,
       "falconInput65Low2Alarm": falconInput65Low2Alarm,
       "falconInput66DigAlarm": falconInput66DigAlarm,
       "falconInput66HighAlarm": falconInput66HighAlarm,
       "falconInput66LowAlarm": falconInput66LowAlarm,
       "falconInput66High2Alarm": falconInput66High2Alarm,
       "falconInput66Low2Alarm": falconInput66Low2Alarm,
       "falconInput67DigAlarm": falconInput67DigAlarm,
       "falconInput67HighAlarm": falconInput67HighAlarm,
       "falconInput67LowAlarm": falconInput67LowAlarm,
       "falconInput67High2Alarm": falconInput67High2Alarm,
       "falconInput67Low2Alarm": falconInput67Low2Alarm,
       "falconInput68DigAlarm": falconInput68DigAlarm,
       "falconInput68HighAlarm": falconInput68HighAlarm,
       "falconInput68LowAlarm": falconInput68LowAlarm,
       "falconInput68High2Alarm": falconInput68High2Alarm,
       "falconInput68Low2Alarm": falconInput68Low2Alarm,
       "falconInput69DigAlarm": falconInput69DigAlarm,
       "falconInput70DigAlarm": falconInput70DigAlarm,
       "falconInput71DigAlarm": falconInput71DigAlarm,
       "falconInput72DigAlarm": falconInput72DigAlarm,
       "falconInput73DigAlarm": falconInput73DigAlarm,
       "falconInput74DigAlarm": falconInput74DigAlarm,
       "falconInput75DigAlarm": falconInput75DigAlarm,
       "falconInput76DigAlarm": falconInput76DigAlarm,
       "falconInput77DigAlarm": falconInput77DigAlarm,
       "falconInput78DigAlarm": falconInput78DigAlarm,
       "falconInput79DigAlarm": falconInput79DigAlarm,
       "falconInput80DigAlarm": falconInput80DigAlarm,
       "falconInput81DigAlarm": falconInput81DigAlarm,
       "falconInput81HighAlarm": falconInput81HighAlarm,
       "falconInput81LowAlarm": falconInput81LowAlarm,
       "falconInput81High2Alarm": falconInput81High2Alarm,
       "falconInput81Low2Alarm": falconInput81Low2Alarm,
       "falconInput82DigAlarm": falconInput82DigAlarm,
       "falconInput82HighAlarm": falconInput82HighAlarm,
       "falconInput82LowAlarm": falconInput82LowAlarm,
       "falconInput82High2Alarm": falconInput82High2Alarm,
       "falconInput82Low2Alarm": falconInput82Low2Alarm,
       "falconInput83DigAlarm": falconInput83DigAlarm,
       "falconInput83HighAlarm": falconInput83HighAlarm,
       "falconInput83LowAlarm": falconInput83LowAlarm,
       "falconInput83High2Alarm": falconInput83High2Alarm,
       "falconInput83Low2Alarm": falconInput83Low2Alarm,
       "falconInput84DigAlarm": falconInput84DigAlarm,
       "falconInput84HighAlarm": falconInput84HighAlarm,
       "falconInput84LowAlarm": falconInput84LowAlarm,
       "falconInput84High2Alarm": falconInput84High2Alarm,
       "falconInput84Low2Alarm": falconInput84Low2Alarm,
       "falconInput85DigAlarm": falconInput85DigAlarm,
       "falconInput85HighAlarm": falconInput85HighAlarm,
       "falconInput85LowAlarm": falconInput85LowAlarm,
       "falconInput85High2Alarm": falconInput85High2Alarm,
       "falconInput85Low2Alarm": falconInput85Low2Alarm,
       "falconInput86DigAlarm": falconInput86DigAlarm,
       "falconInput86HighAlarm": falconInput86HighAlarm,
       "falconInput86LowAlarm": falconInput86LowAlarm,
       "falconInput86High2Alarm": falconInput86High2Alarm,
       "falconInput86Low2Alarm": falconInput86Low2Alarm,
       "falconInput87DigAlarm": falconInput87DigAlarm,
       "falconInput87HighAlarm": falconInput87HighAlarm,
       "falconInput87LowAlarm": falconInput87LowAlarm,
       "falconInput87High2Alarm": falconInput87High2Alarm,
       "falconInput87Low2Alarm": falconInput87Low2Alarm,
       "falconInput88DigAlarm": falconInput88DigAlarm,
       "falconInput88HighAlarm": falconInput88HighAlarm,
       "falconInput88LowAlarm": falconInput88LowAlarm,
       "falconInput88High2Alarm": falconInput88High2Alarm,
       "falconInput88Low2Alarm": falconInput88Low2Alarm,
       "falconInput89DigAlarm": falconInput89DigAlarm,
       "falconInput89HighAlarm": falconInput89HighAlarm,
       "falconInput89LowAlarm": falconInput89LowAlarm,
       "falconInput89High2Alarm": falconInput89High2Alarm,
       "falconInput89Low2Alarm": falconInput89Low2Alarm,
       "falconInput90DigAlarm": falconInput90DigAlarm,
       "falconInput90HighAlarm": falconInput90HighAlarm,
       "falconInput90LowAlarm": falconInput90LowAlarm,
       "falconInput90High2Alarm": falconInput90High2Alarm,
       "falconInput90Low2Alarm": falconInput90Low2Alarm,
       "falconInput91DigAlarm": falconInput91DigAlarm,
       "falconInput91HighAlarm": falconInput91HighAlarm,
       "falconInput91LowAlarm": falconInput91LowAlarm,
       "falconInput91High2Alarm": falconInput91High2Alarm,
       "falconInput91Low2Alarm": falconInput91Low2Alarm,
       "falconInput92DigAlarm": falconInput92DigAlarm,
       "falconInput92HighAlarm": falconInput92HighAlarm,
       "falconInput92LowAlarm": falconInput92LowAlarm,
       "falconInput92High2Alarm": falconInput92High2Alarm,
       "falconInput92Low2Alarm": falconInput92Low2Alarm,
       "falconInput93DigAlarm": falconInput93DigAlarm,
       "falconInput94DigAlarm": falconInput94DigAlarm,
       "falconInput95DigAlarm": falconInput95DigAlarm,
       "falconInput96DigAlarm": falconInput96DigAlarm,
       "falconInput97DigAlarm": falconInput97DigAlarm,
       "falconInput98DigAlarm": falconInput98DigAlarm,
       "falconInput99DigAlarm": falconInput99DigAlarm,
       "falconInput100DigAlarm": falconInput100DigAlarm,
       "falconInput101DigAlarm": falconInput101DigAlarm,
       "falconInput102DigAlarm": falconInput102DigAlarm,
       "falconInput103DigAlarm": falconInput103DigAlarm,
       "falconInput104DigAlarm": falconInput104DigAlarm,
       "falconTemperatureSensorHighAlarm": falconTemperatureSensorHighAlarm,
       "falconTemperatureSensorLowAlarm": falconTemperatureSensorLowAlarm,
       "falconTemperatureSensorHigh2Alarm": falconTemperatureSensorHigh2Alarm,
       "falconTemperatureSensorLow2Alarm": falconTemperatureSensorLow2Alarm,
       "falconHumiditySensorHighAlarm": falconHumiditySensorHighAlarm,
       "falconHumiditySensorLowAlarm": falconHumiditySensorLowAlarm,
       "falconHumiditySensorHigh2Alarm": falconHumiditySensorHigh2Alarm,
       "falconHumiditySensorLow2Alarm": falconHumiditySensorLow2Alarm,
       "falconLowBatteryAlarm": falconLowBatteryAlarm,
       "falconTraps": falconTraps,
       "falconAlarmEntryAdded": falconAlarmEntryAdded,
       "falconAlarmEntryRemoved": falconAlarmEntryRemoved,
       "falconAccessGranted": falconAccessGranted,
       "falconAccessDenied": falconAccessDenied,
       "falconPageUnsuccessful": falconPageUnsuccessful,
       "falconConfigurationChanged": falconConfigurationChanged,
       "falconAlarmHistory": falconAlarmHistory,
       "falconAlarmHistoryEntries": falconAlarmHistoryEntries,
       "falconAlarmHistoryClear": falconAlarmHistoryClear,
       "falconAlarmHistoryTable": falconAlarmHistoryTable,
       "falconAlarmHistoryEntry": falconAlarmHistoryEntry,
       "falconAlarmHistoryId": falconAlarmHistoryId,
       "falconAlarmHistoryText": falconAlarmHistoryText,
       "falconTrapSettings": falconTrapSettings,
       "falconPersistantTraps": falconPersistantTraps,
       "falconAlarmAcknowledge": falconAlarmAcknowledge,
       "falconSchedules": falconSchedules,
       "falconScheduleABeginDOW": falconScheduleABeginDOW,
       "falconScheduleAEndDOW": falconScheduleAEndDOW,
       "falconScheduleABeginTime": falconScheduleABeginTime,
       "falconScheduleAEndTime": falconScheduleAEndTime,
       "falconScheduleBBeginDOW": falconScheduleBBeginDOW,
       "falconScheduleBEndDOW": falconScheduleBEndDOW,
       "falconScheduleBBeginTime": falconScheduleBBeginTime,
       "falconScheduleBEndTime": falconScheduleBEndTime,
       "falconPortTrap": falconPortTrap,
       "falconPort01Trap": falconPort01Trap,
       "falconPort02Trap": falconPort02Trap,
       "falconPort03Trap": falconPort03Trap,
       "falconPort04Trap": falconPort04Trap,
       "falconPort05Trap": falconPort05Trap,
       "falconPort06Trap": falconPort06Trap,
       "falconPort07Trap": falconPort07Trap,
       "falconPort08Trap": falconPort08Trap,
       "falconPort09Trap": falconPort09Trap,
       "falconPort10Trap": falconPort10Trap,
       "falconPort11Trap": falconPort11Trap,
       "falconPort12Trap": falconPort12Trap,
       "falconPort13Trap": falconPort13Trap,
       "falconPort14Trap": falconPort14Trap,
       "falconPort15Trap": falconPort15Trap,
       "falconPort16Trap": falconPort16Trap,
       "falconPort17Trap": falconPort17Trap,
       "falconPort18Trap": falconPort18Trap,
       "falconPort19Trap": falconPort19Trap,
       "falconPort20Trap": falconPort20Trap,
       "falconPort21Trap": falconPort21Trap,
       "falconPort22Trap": falconPort22Trap,
       "falconPort23Trap": falconPort23Trap,
       "falconPort24Trap": falconPort24Trap,
       "falconPort25Trap": falconPort25Trap,
       "falconPort26Trap": falconPort26Trap,
       "falconPort27Trap": falconPort27Trap,
       "falconPort28Trap": falconPort28Trap,
       "falconPort29Trap": falconPort29Trap,
       "falconPort30Trap": falconPort30Trap,
       "falconPort31Trap": falconPort31Trap,
       "falconPort32Trap": falconPort32Trap,
       "falconPort33Trap": falconPort33Trap,
       "falconPort34Trap": falconPort34Trap,
       "falconPort35Trap": falconPort35Trap,
       "falconPort36Trap": falconPort36Trap,
       "falconPort37Trap": falconPort37Trap,
       "falconPort38Trap": falconPort38Trap,
       "falconPort39Trap": falconPort39Trap,
       "falconPort40Trap": falconPort40Trap,
       "falconPort41Trap": falconPort41Trap,
       "falconPort42Trap": falconPort42Trap,
       "falconPort43Trap": falconPort43Trap,
       "falconPort44Trap": falconPort44Trap,
       "falconPort45Trap": falconPort45Trap,
       "falconPort46Trap": falconPort46Trap,
       "falconPort47Trap": falconPort47Trap,
       "falconPort48Trap": falconPort48Trap,
       "falconPort49Trap": falconPort49Trap,
       "falconPort50Trap": falconPort50Trap,
       "falconPort51Trap": falconPort51Trap,
       "falconPort52Trap": falconPort52Trap,
       "falconPort53Trap": falconPort53Trap,
       "falconPort54Trap": falconPort54Trap,
       "falconPort55Trap": falconPort55Trap,
       "falconPort56Trap": falconPort56Trap,
       "falconPort57Trap": falconPort57Trap,
       "falconPort58Trap": falconPort58Trap,
       "falconPort59Trap": falconPort59Trap,
       "falconPort60Trap": falconPort60Trap,
       "falconPort61Trap": falconPort61Trap,
       "falconPort62Trap": falconPort62Trap,
       "falconPort63Trap": falconPort63Trap,
       "falconPort64Trap": falconPort64Trap,
       "falconPort65Trap": falconPort65Trap,
       "falconPort66Trap": falconPort66Trap,
       "falconPort67Trap": falconPort67Trap,
       "falconPort68Trap": falconPort68Trap,
       "falconPort69Trap": falconPort69Trap,
       "falconPort70Trap": falconPort70Trap,
       "falconPort71Trap": falconPort71Trap,
       "falconPort72Trap": falconPort72Trap,
       "falconPort73Trap": falconPort73Trap,
       "falconPort74Trap": falconPort74Trap,
       "falconPort75Trap": falconPort75Trap,
       "falconPort76Trap": falconPort76Trap,
       "falconPort77Trap": falconPort77Trap,
       "falconPort78Trap": falconPort78Trap,
       "falconPort79Trap": falconPort79Trap,
       "falconPort80Trap": falconPort80Trap,
       "falconPort81Trap": falconPort81Trap,
       "falconPort82Trap": falconPort82Trap,
       "falconPort83Trap": falconPort83Trap,
       "falconPort84Trap": falconPort84Trap,
       "falconPort85Trap": falconPort85Trap,
       "falconPort86Trap": falconPort86Trap,
       "falconPort87Trap": falconPort87Trap,
       "falconPort88Trap": falconPort88Trap,
       "falconPort89Trap": falconPort89Trap,
       "falconPort90Trap": falconPort90Trap,
       "falconPort91Trap": falconPort91Trap,
       "falconPort92Trap": falconPort92Trap,
       "falconPort93Trap": falconPort93Trap,
       "falconPort94Trap": falconPort94Trap,
       "falconPort95Trap": falconPort95Trap,
       "falconPort96Trap": falconPort96Trap,
       "falconPort97Trap": falconPort97Trap,
       "falconPort98Trap": falconPort98Trap,
       "falconPort99Trap": falconPort99Trap,
       "falconPort100Trap": falconPort100Trap,
       "falconPort101Trap": falconPort101Trap,
       "falconPort102Trap": falconPort102Trap,
       "falconPort103Trap": falconPort103Trap,
       "falconPort104Trap": falconPort104Trap,
       "falconTemperatureSensorTrap": falconTemperatureSensorTrap,
       "falconHumiditySensorTrap": falconHumiditySensorTrap,
       "falconPortTrapClear": falconPortTrapClear,
       "falconPort01TrapClear": falconPort01TrapClear,
       "falconPort02TrapClear": falconPort02TrapClear,
       "falconPort03TrapClear": falconPort03TrapClear,
       "falconPort04TrapClear": falconPort04TrapClear,
       "falconPort05TrapClear": falconPort05TrapClear,
       "falconPort06TrapClear": falconPort06TrapClear,
       "falconPort07TrapClear": falconPort07TrapClear,
       "falconPort08TrapClear": falconPort08TrapClear,
       "falconPort09TrapClear": falconPort09TrapClear,
       "falconPort10TrapClear": falconPort10TrapClear,
       "falconPort11TrapClear": falconPort11TrapClear,
       "falconPort12TrapClear": falconPort12TrapClear,
       "falconPort13TrapClear": falconPort13TrapClear,
       "falconPort14TrapClear": falconPort14TrapClear,
       "falconPort15TrapClear": falconPort15TrapClear,
       "falconPort16TrapClear": falconPort16TrapClear,
       "falconPort17TrapClear": falconPort17TrapClear,
       "falconPort18TrapClear": falconPort18TrapClear,
       "falconPort19TrapClear": falconPort19TrapClear,
       "falconPort20TrapClear": falconPort20TrapClear,
       "falconPort21TrapClear": falconPort21TrapClear,
       "falconPort22TrapClear": falconPort22TrapClear,
       "falconPort23TrapClear": falconPort23TrapClear,
       "falconPort24TrapClear": falconPort24TrapClear,
       "falconPort25TrapClear": falconPort25TrapClear,
       "falconPort26TrapClear": falconPort26TrapClear,
       "falconPort27TrapClear": falconPort27TrapClear,
       "falconPort28TrapClear": falconPort28TrapClear,
       "falconPort29TrapClear": falconPort29TrapClear,
       "falconPort30TrapClear": falconPort30TrapClear,
       "falconPort31TrapClear": falconPort31TrapClear,
       "falconPort32TrapClear": falconPort32TrapClear,
       "falconPort33TrapClear": falconPort33TrapClear,
       "falconPort34TrapClear": falconPort34TrapClear,
       "falconPort35TrapClear": falconPort35TrapClear,
       "falconPort36TrapClear": falconPort36TrapClear,
       "falconPort37TrapClear": falconPort37TrapClear,
       "falconPort38TrapClear": falconPort38TrapClear,
       "falconPort39TrapClear": falconPort39TrapClear,
       "falconPort40TrapClear": falconPort40TrapClear,
       "falconPort41TrapClear": falconPort41TrapClear,
       "falconPort42TrapClear": falconPort42TrapClear,
       "falconPort43TrapClear": falconPort43TrapClear,
       "falconPort44TrapClear": falconPort44TrapClear,
       "falconPort45TrapClear": falconPort45TrapClear,
       "falconPort46TrapClear": falconPort46TrapClear,
       "falconPort47TrapClear": falconPort47TrapClear,
       "falconPort48TrapClear": falconPort48TrapClear,
       "falconPort49TrapClear": falconPort49TrapClear,
       "falconPort50TrapClear": falconPort50TrapClear,
       "falconPort51TrapClear": falconPort51TrapClear,
       "falconPort52TrapClear": falconPort52TrapClear,
       "falconPort53TrapClear": falconPort53TrapClear,
       "falconPort54TrapClear": falconPort54TrapClear,
       "falconPort55TrapClear": falconPort55TrapClear,
       "falconPort56TrapClear": falconPort56TrapClear,
       "falconPort57TrapClear": falconPort57TrapClear,
       "falconPort58TrapClear": falconPort58TrapClear,
       "falconPort59TrapClear": falconPort59TrapClear,
       "falconPort60TrapClear": falconPort60TrapClear,
       "falconPort61TrapClear": falconPort61TrapClear,
       "falconPort62TrapClear": falconPort62TrapClear,
       "falconPort63TrapClear": falconPort63TrapClear,
       "falconPort64TrapClear": falconPort64TrapClear,
       "falconPort65TrapClear": falconPort65TrapClear,
       "falconPort66TrapClear": falconPort66TrapClear,
       "falconPort67TrapClear": falconPort67TrapClear,
       "falconPort68TrapClear": falconPort68TrapClear,
       "falconPort69TrapClear": falconPort69TrapClear,
       "falconPort70TrapClear": falconPort70TrapClear,
       "falconPort71TrapClear": falconPort71TrapClear,
       "falconPort72TrapClear": falconPort72TrapClear,
       "falconPort73TrapClear": falconPort73TrapClear,
       "falconPort74TrapClear": falconPort74TrapClear,
       "falconPort75TrapClear": falconPort75TrapClear,
       "falconPort76TrapClear": falconPort76TrapClear,
       "falconPort77TrapClear": falconPort77TrapClear,
       "falconPort78TrapClear": falconPort78TrapClear,
       "falconPort79TrapClear": falconPort79TrapClear,
       "falconPort80TrapClear": falconPort80TrapClear,
       "falconPort81TrapClear": falconPort81TrapClear,
       "falconPort82TrapClear": falconPort82TrapClear,
       "falconPort83TrapClear": falconPort83TrapClear,
       "falconPort84TrapClear": falconPort84TrapClear,
       "falconPort85TrapClear": falconPort85TrapClear,
       "falconPort86TrapClear": falconPort86TrapClear,
       "falconPort87TrapClear": falconPort87TrapClear,
       "falconPort88TrapClear": falconPort88TrapClear,
       "falconPort89TrapClear": falconPort89TrapClear,
       "falconPort90TrapClear": falconPort90TrapClear,
       "falconPort91TrapClear": falconPort91TrapClear,
       "falconPort92TrapClear": falconPort92TrapClear,
       "falconPort93TrapClear": falconPort93TrapClear,
       "falconPort94TrapClear": falconPort94TrapClear,
       "falconPort95TrapClear": falconPort95TrapClear,
       "falconPort96TrapClear": falconPort96TrapClear,
       "falconPort97TrapClear": falconPort97TrapClear,
       "falconPort98TrapClear": falconPort98TrapClear,
       "falconPort99TrapClear": falconPort99TrapClear,
       "falconPort100TrapClear": falconPort100TrapClear,
       "falconPort101TrapClear": falconPort101TrapClear,
       "falconPort102TrapClear": falconPort102TrapClear,
       "falconPort103TrapClear": falconPort103TrapClear,
       "falconPort104TrapClear": falconPort104TrapClear,
       "falconTemperatureSensorTrapClear": falconTemperatureSensorTrapClear,
       "falconHumiditySensorTrapClear": falconHumiditySensorTrapClear,
       "falconXbus": falconXbus,
       "falconBCMs": falconBCMs,
       "falconBCM01": falconBCM01,
       "falconBCM01Label": falconBCM01Label,
       "falconBCM01CBTable": falconBCM01CBTable,
       "falconBCM01CBEntry": falconBCM01CBEntry,
       "falconBCM01CBIndex": falconBCM01CBIndex,
       "falconBCM01CBStatus": falconBCM01CBStatus,
       "falconBCM01CBReading": falconBCM01CBReading,
       "falconBCM01CBLabel": falconBCM01CBLabel,
       "falconBCM02": falconBCM02,
       "falconBCM02Label": falconBCM02Label,
       "falconBCM02CBTable": falconBCM02CBTable,
       "falconBCM02CBEntry": falconBCM02CBEntry,
       "falconBCM02CBIndex": falconBCM02CBIndex,
       "falconBCM02CBStatus": falconBCM02CBStatus,
       "falconBCM02CBReading": falconBCM02CBReading,
       "falconBCM02CBLabel": falconBCM02CBLabel,
       "falconBCM03": falconBCM03,
       "falconBCM03Label": falconBCM03Label,
       "falconBCM03CBTable": falconBCM03CBTable,
       "falconBCM03CBEntry": falconBCM03CBEntry,
       "falconBCM03CBIndex": falconBCM03CBIndex,
       "falconBCM03CBStatus": falconBCM03CBStatus,
       "falconBCM03CBReading": falconBCM03CBReading,
       "falconBCM03CBLabel": falconBCM03CBLabel,
       "falconBCM04": falconBCM04,
       "falconBCM04Label": falconBCM04Label,
       "falconBCM04CBTable": falconBCM04CBTable,
       "falconBCM04CBEntry": falconBCM04CBEntry,
       "falconBCM04CBIndex": falconBCM04CBIndex,
       "falconBCM04CBStatus": falconBCM04CBStatus,
       "falconBCM04CBReading": falconBCM04CBReading,
       "falconBCM04CBLabel": falconBCM04CBLabel,
       "falconBCM05": falconBCM05,
       "falconBCM05Label": falconBCM05Label,
       "falconBCM05CBTable": falconBCM05CBTable,
       "falconBCM05CBEntry": falconBCM05CBEntry,
       "falconBCM05CBIndex": falconBCM05CBIndex,
       "falconBCM05CBStatus": falconBCM05CBStatus,
       "falconBCM05CBReading": falconBCM05CBReading,
       "falconBCM05CBLabel": falconBCM05CBLabel,
       "falconBCM06": falconBCM06,
       "falconBCM06Label": falconBCM06Label,
       "falconBCM06CBTable": falconBCM06CBTable,
       "falconBCM06CBEntry": falconBCM06CBEntry,
       "falconBCM06CBIndex": falconBCM06CBIndex,
       "falconBCM06CBStatus": falconBCM06CBStatus,
       "falconBCM06CBReading": falconBCM06CBReading,
       "falconBCM06CBLabel": falconBCM06CBLabel,
       "falconBCM07": falconBCM07,
       "falconBCM07Label": falconBCM07Label,
       "falconBCM07CBTable": falconBCM07CBTable,
       "falconBCM07CBEntry": falconBCM07CBEntry,
       "falconBCM07CBIndex": falconBCM07CBIndex,
       "falconBCM07CBStatus": falconBCM07CBStatus,
       "falconBCM07CBReading": falconBCM07CBReading,
       "falconBCM07CBLabel": falconBCM07CBLabel,
       "falconBCM08": falconBCM08,
       "falconBCM08Label": falconBCM08Label,
       "falconBCM08CBTable": falconBCM08CBTable,
       "falconBCM08CBEntry": falconBCM08CBEntry,
       "falconBCM08CBIndex": falconBCM08CBIndex,
       "falconBCM08CBStatus": falconBCM08CBStatus,
       "falconBCM08CBReading": falconBCM08CBReading,
       "falconBCM08CBLabel": falconBCM08CBLabel,
       "falconBCM09": falconBCM09,
       "falconBCM09Label": falconBCM09Label,
       "falconBCM09CBTable": falconBCM09CBTable,
       "falconBCM09CBEntry": falconBCM09CBEntry,
       "falconBCM09CBIndex": falconBCM09CBIndex,
       "falconBCM09CBStatus": falconBCM09CBStatus,
       "falconBCM09CBReading": falconBCM09CBReading,
       "falconBCM09CBLabel": falconBCM09CBLabel,
       "falconBCM10": falconBCM10,
       "falconBCM10Label": falconBCM10Label,
       "falconBCM10CBTable": falconBCM10CBTable,
       "falconBCM10CBEntry": falconBCM10CBEntry,
       "falconBCM10CBIndex": falconBCM10CBIndex,
       "falconBCM10CBStatus": falconBCM10CBStatus,
       "falconBCM10CBReading": falconBCM10CBReading,
       "falconBCM10CBLabel": falconBCM10CBLabel,
       "falconBCM11": falconBCM11,
       "falconBCM11Label": falconBCM11Label,
       "falconBCM11CBTable": falconBCM11CBTable,
       "falconBCM11CBEntry": falconBCM11CBEntry,
       "falconBCM11CBIndex": falconBCM11CBIndex,
       "falconBCM11CBStatus": falconBCM11CBStatus,
       "falconBCM11CBReading": falconBCM11CBReading,
       "falconBCM11CBLabel": falconBCM11CBLabel,
       "falconBCM12": falconBCM12,
       "falconBCM12Label": falconBCM12Label,
       "falconBCM12CBTable": falconBCM12CBTable,
       "falconBCM12CBEntry": falconBCM12CBEntry,
       "falconBCM12CBIndex": falconBCM12CBIndex,
       "falconBCM12CBStatus": falconBCM12CBStatus,
       "falconBCM12CBReading": falconBCM12CBReading,
       "falconBCM12CBLabel": falconBCM12CBLabel,
       "falconBCM13": falconBCM13,
       "falconBCM13Label": falconBCM13Label,
       "falconBCM13CBTable": falconBCM13CBTable,
       "falconBCM13CBEntry": falconBCM13CBEntry,
       "falconBCM13CBIndex": falconBCM13CBIndex,
       "falconBCM13CBStatus": falconBCM13CBStatus,
       "falconBCM13CBReading": falconBCM13CBReading,
       "falconBCM13CBLabel": falconBCM13CBLabel,
       "falconBCM14": falconBCM14,
       "falconBCM14Label": falconBCM14Label,
       "falconBCM14CBTable": falconBCM14CBTable,
       "falconBCM14CBEntry": falconBCM14CBEntry,
       "falconBCM14CBIndex": falconBCM14CBIndex,
       "falconBCM14CBStatus": falconBCM14CBStatus,
       "falconBCM14CBReading": falconBCM14CBReading,
       "falconBCM14CBLabel": falconBCM14CBLabel,
       "falconBCM15": falconBCM15,
       "falconBCM15Label": falconBCM15Label,
       "falconBCM15CBTable": falconBCM15CBTable,
       "falconBCM15CBEntry": falconBCM15CBEntry,
       "falconBCM15CBIndex": falconBCM15CBIndex,
       "falconBCM15CBStatus": falconBCM15CBStatus,
       "falconBCM15CBReading": falconBCM15CBReading,
       "falconBCM15CBLabel": falconBCM15CBLabel,
       "falconBCM16": falconBCM16,
       "falconBCM16Label": falconBCM16Label,
       "falconBCM16CBTable": falconBCM16CBTable,
       "falconBCM16CBEntry": falconBCM16CBEntry,
       "falconBCM16CBIndex": falconBCM16CBIndex,
       "falconBCM16CBStatus": falconBCM16CBStatus,
       "falconBCM16CBReading": falconBCM16CBReading,
       "falconBCM16CBLabel": falconBCM16CBLabel,
       "falconBCMTrap": falconBCMTrap,
       "falconBCM01Trap": falconBCM01Trap,
       "falconBCM10Trap": falconBCM10Trap,
       "falconBCM02Trap": falconBCM02Trap,
       "falconBCM03Trap": falconBCM03Trap,
       "falconBCM04Trap": falconBCM04Trap,
       "falconBCM05Trap": falconBCM05Trap,
       "falconBCM06Trap": falconBCM06Trap,
       "falconBCM07Trap": falconBCM07Trap,
       "falconBCM08Trap": falconBCM08Trap,
       "falconBCM09Trap": falconBCM09Trap,
       "falconBCM11Trap": falconBCM11Trap,
       "falconBCM12Trap": falconBCM12Trap,
       "falconBCM13Trap": falconBCM13Trap,
       "falconBCM14Trap": falconBCM14Trap,
       "falconBCM15Trap": falconBCM15Trap,
       "falconBCM16Trap": falconBCM16Trap,
       "falconBCMTrapClear": falconBCMTrapClear,
       "falconBCM01TrapClear": falconBCM01TrapClear,
       "falconBCM02TrapClear": falconBCM02TrapClear,
       "falconBCM03TrapClear": falconBCM03TrapClear,
       "falconBCM04TrapClear": falconBCM04TrapClear,
       "falconBCM05TrapClear": falconBCM05TrapClear,
       "falconBCM06TrapClear": falconBCM06TrapClear,
       "falconBCM07TrapClear": falconBCM07TrapClear,
       "falconBCM08TrapClear": falconBCM08TrapClear,
       "falconBCM09TrapClear": falconBCM09TrapClear,
       "falconBCM10TrapClear": falconBCM10TrapClear,
       "falconBCM11TrapClear": falconBCM11TrapClear,
       "falconBCM12TrapClear": falconBCM12TrapClear,
       "falconBCM13TrapClear": falconBCM13TrapClear,
       "falconBCM14TrapClear": falconBCM14TrapClear,
       "falconBCM15TrapClear": falconBCM15TrapClear,
       "falconBCM16TrapClear": falconBCM16TrapClear,
       "falconXbG628": falconXbG628,
       "falconXbUnits": falconXbUnits,
       "falconXbUnitsTable": falconXbUnitsTable,
       "falconXbUnitsEntry": falconXbUnitsEntry,
       "falconXbUnitsIndex": falconXbUnitsIndex,
       "falconXbUnitsStatus": falconXbUnitsStatus,
       "falconXbUnitsLabel": falconXbUnitsLabel,
       "falconXbusTrapData": falconXbusTrapData,
       "falconXbusTrapRegisterNumber": falconXbusTrapRegisterNumber,
       "falconXbusTrapRegisterLabel": falconXbusTrapRegisterLabel,
       "falconXbusRegisterTable": falconXbusRegisterTable,
       "falconXbusRegisterEntry": falconXbusRegisterEntry,
       "falconXbusRegisterIndex": falconXbusRegisterIndex,
       "falconXbusRegisterType": falconXbusRegisterType,
       "falconXbusRegisterData": falconXbusRegisterData,
       "falconXbusRegisterLabel": falconXbusRegisterLabel,
       "falconXbusTraps": falconXbusTraps,
       "falconXbusUnit01Trap": falconXbusUnit01Trap,
       "falconXbusUnit02Trap": falconXbusUnit02Trap,
       "falconXbusUnit03Trap": falconXbusUnit03Trap,
       "falconXbusUnit04Trap": falconXbusUnit04Trap,
       "falconXbusUnit05Trap": falconXbusUnit05Trap,
       "falconXbusUnit06Trap": falconXbusUnit06Trap,
       "falconXbusUnit07Trap": falconXbusUnit07Trap,
       "falconXbusUnit08Trap": falconXbusUnit08Trap,
       "falconXbusUnit09Trap": falconXbusUnit09Trap,
       "falconXbusUnit10Trap": falconXbusUnit10Trap,
       "falconXbusUnit11Trap": falconXbusUnit11Trap,
       "falconXbusUnit12Trap": falconXbusUnit12Trap,
       "falconXbusUnit13Trap": falconXbusUnit13Trap,
       "falconXbusUnit14Trap": falconXbusUnit14Trap,
       "falconXbusUnit15Trap": falconXbusUnit15Trap,
       "falconXbusUnit16Trap": falconXbusUnit16Trap,
       "falconXbusTrapsClear": falconXbusTrapsClear,
       "falconXbusUnit01TrapClear": falconXbusUnit01TrapClear,
       "falconXbusUnit02TrapClear": falconXbusUnit02TrapClear,
       "falconXbusUnit03TrapClear": falconXbusUnit03TrapClear,
       "falconXbusUnit04TrapClear": falconXbusUnit04TrapClear,
       "falconXbusUnit05TrapClear": falconXbusUnit05TrapClear,
       "falconXbusUnit06TrapClear": falconXbusUnit06TrapClear,
       "falconXbusUnit07TrapClear": falconXbusUnit07TrapClear,
       "falconXbusUnit08TrapClear": falconXbusUnit08TrapClear,
       "falconXbusUnit09TrapClear": falconXbusUnit09TrapClear,
       "falconXbusUnit10TrapClear": falconXbusUnit10TrapClear,
       "falconXbusUnit11TrapClear": falconXbusUnit11TrapClear,
       "falconXbusUnit12TrapClear": falconXbusUnit12TrapClear,
       "falconXbusUnit13TrapClear": falconXbusUnit13TrapClear,
       "falconXbusUnit14TrapClear": falconXbusUnit14TrapClear,
       "falconXbusUnit15TrapClear": falconXbusUnit15TrapClear,
       "falconXbusUnit16TrapClear": falconXbusUnit16TrapClear,
       "fms-X": fms_X,
       "fms-A": fms_A,
       "fms-B": fms_B,
       "fms-C": fms_C,
       "fms-AAxx": fms_AAxx,
       "fms-AAAx": fms_AAAx,
       "fms-AAAA": fms_AAAA,
       "fms-AAAC": fms_AAAC,
       "fms-AABx": fms_AABx,
       "fms-AABB": fms_AABB,
       "fms-AACx": fms_AACx,
       "fms-AACC": fms_AACC,
       "fms-ABxx": fms_ABxx,
       "fms-ABBx": fms_ABBx,
       "fms-ABBB": fms_ABBB,
       "fms-ABBC": fms_ABBC,
       "fms-ABCx": fms_ABCx,
       "fms-ABCC": fms_ABCC,
       "fms-ACxx": fms_ACxx,
       "fms-ACCx": fms_ACCx,
       "fms-ACCC": fms_ACCC,
       "fms-BBxx": fms_BBxx,
       "fms-BBBx": fms_BBBx,
       "fms-BBBB": fms_BBBB,
       "fms-BBBC": fms_BBBC,
       "fms-BBCx": fms_BBCx,
       "fms-BBCC": fms_BBCC,
       "fms-BCxx": fms_BCxx,
       "fms-BCCx": fms_BCCx,
       "fms-BCCC": fms_BCCC,
       "fms-CxCC": fms_CxCC,
       "fms-CCxx": fms_CCxx,
       "fms-CCxC": fms_CCxC,
       "fms-CCCx": fms_CCCx,
       "fms-CCCC": fms_CCCC}
)
