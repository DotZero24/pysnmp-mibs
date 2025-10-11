# SNMP MIB module (SOCOMECUPSSTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/socomec/SOCOMECUPSSTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:06:29 2025
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

(AutonomousType,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )





class NonNegativeInteger(Integer32):
    """Custom type NonNegativeInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SocomecUPS_ObjectIdentity = ObjectIdentity
socomecUPS = _SocomecUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1)
)
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1)
)
_Connectsts_ObjectIdentity = ObjectIdentity
connectsts = _Connectsts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10)
)
_StsObjects_ObjectIdentity = ObjectIdentity
stsObjects = _StsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1)
)
_StsIdent_ObjectIdentity = ObjectIdentity
stsIdent = _StsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 1)
)


class _StsIdentModel_Type(DisplayString):
    """Custom type stsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_StsIdentModel_Type.__name__ = "DisplayString"
_StsIdentModel_Object = MibScalar
stsIdentModel = _StsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 1, 1),
    _StsIdentModel_Type()
)
stsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsIdentModel.setStatus("mandatory")


class _StsIdentSerialNumber_Type(DisplayString):
    """Custom type stsIdentSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_StsIdentSerialNumber_Type.__name__ = "DisplayString"
_StsIdentSerialNumber_Object = MibScalar
stsIdentSerialNumber = _StsIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 1, 2),
    _StsIdentSerialNumber_Type()
)
stsIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsIdentSerialNumber.setStatus("mandatory")


class _StsIdentFirmwareVersion_Type(DisplayString):
    """Custom type stsIdentFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_StsIdentFirmwareVersion_Type.__name__ = "DisplayString"
_StsIdentFirmwareVersion_Object = MibScalar
stsIdentFirmwareVersion = _StsIdentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 1, 3),
    _StsIdentFirmwareVersion_Type()
)
stsIdentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsIdentFirmwareVersion.setStatus("mandatory")


class _StsIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type stsIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_StsIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_StsIdentAgentSoftwareVersion_Object = MibScalar
stsIdentAgentSoftwareVersion = _StsIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 1, 4),
    _StsIdentAgentSoftwareVersion_Type()
)
stsIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsIdentAgentSoftwareVersion.setStatus("mandatory")
_StsSource1_ObjectIdentity = ObjectIdentity
stsSource1 = _StsSource1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 2)
)


class _StsSource1Status_Type(Integer32):
    """Custom type stsSource1Status based on Integer32"""
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
        *(("unknown", 1),
          ("source1OK", 2),
          ("source1Critical", 3),
          ("source1OutTol", 4),
          ("source1Absent", 5))
    )


_StsSource1Status_Type.__name__ = "Integer32"
_StsSource1Status_Object = MibScalar
stsSource1Status = _StsSource1Status_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 2, 1),
    _StsSource1Status_Type()
)
stsSource1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsSource1Status.setStatus("mandatory")


class _StsSource1Prefered_Type(Integer32):
    """Custom type stsSource1Prefered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_StsSource1Prefered_Type.__name__ = "Integer32"
_StsSource1Prefered_Object = MibScalar
stsSource1Prefered = _StsSource1Prefered_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 2, 2),
    _StsSource1Prefered_Type()
)
stsSource1Prefered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsSource1Prefered.setStatus("mandatory")
_StsSource1Frequency_Type = Integer32
_StsSource1Frequency_Object = MibScalar
stsSource1Frequency = _StsSource1Frequency_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 2, 3),
    _StsSource1Frequency_Type()
)
stsSource1Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsSource1Frequency.setStatus("mandatory")
_StsSource1NumLines_Type = Integer32
_StsSource1NumLines_Object = MibScalar
stsSource1NumLines = _StsSource1NumLines_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 2, 4),
    _StsSource1NumLines_Type()
)
stsSource1NumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsSource1NumLines.setStatus("mandatory")
_StsSource1Table_Object = MibTable
stsSource1Table = _StsSource1Table_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 2, 5)
)
if mibBuilder.loadTexts:
    stsSource1Table.setStatus("mandatory")
_StsSource1Entry_Object = MibTableRow
stsSource1Entry = _StsSource1Entry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 2, 5, 1)
)
stsSource1Entry.setIndexNames(
    (0, "SOCOMECUPSSTS-MIB", "stsSource1LineIndex"),
)
if mibBuilder.loadTexts:
    stsSource1Entry.setStatus("mandatory")


class _StsSource1LineIndex_Type(Integer32):
    """Custom type stsSource1LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StsSource1LineIndex_Type.__name__ = "Integer32"
_StsSource1LineIndex_Object = MibTableColumn
stsSource1LineIndex = _StsSource1LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 2, 5, 1, 1),
    _StsSource1LineIndex_Type()
)
stsSource1LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsSource1LineIndex.setStatus("mandatory")
_StsSource1Voltage_Type = Integer32
_StsSource1Voltage_Object = MibTableColumn
stsSource1Voltage = _StsSource1Voltage_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 2, 5, 1, 2),
    _StsSource1Voltage_Type()
)
stsSource1Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsSource1Voltage.setStatus("mandatory")
_StsSource2_ObjectIdentity = ObjectIdentity
stsSource2 = _StsSource2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 3)
)


class _StsSource2Status_Type(Integer32):
    """Custom type stsSource2Status based on Integer32"""
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
        *(("unknown", 1),
          ("source2OK", 2),
          ("source2Critical", 3),
          ("source2OutTol", 4),
          ("source2Absent", 5))
    )


_StsSource2Status_Type.__name__ = "Integer32"
_StsSource2Status_Object = MibScalar
stsSource2Status = _StsSource2Status_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 3, 1),
    _StsSource2Status_Type()
)
stsSource2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsSource2Status.setStatus("mandatory")


class _StsSource2Prefered_Type(Integer32):
    """Custom type stsSource2Prefered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_StsSource2Prefered_Type.__name__ = "Integer32"
_StsSource2Prefered_Object = MibScalar
stsSource2Prefered = _StsSource2Prefered_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 3, 2),
    _StsSource2Prefered_Type()
)
stsSource2Prefered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsSource2Prefered.setStatus("mandatory")
_StsSource2Frequency_Type = Integer32
_StsSource2Frequency_Object = MibScalar
stsSource2Frequency = _StsSource2Frequency_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 3, 3),
    _StsSource2Frequency_Type()
)
stsSource2Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsSource2Frequency.setStatus("mandatory")
_StsSource2NumLines_Type = Integer32
_StsSource2NumLines_Object = MibScalar
stsSource2NumLines = _StsSource2NumLines_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 3, 4),
    _StsSource2NumLines_Type()
)
stsSource2NumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsSource2NumLines.setStatus("mandatory")
_StsSource2Table_Object = MibTable
stsSource2Table = _StsSource2Table_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 3, 5)
)
if mibBuilder.loadTexts:
    stsSource2Table.setStatus("mandatory")
_StsSource2Entry_Object = MibTableRow
stsSource2Entry = _StsSource2Entry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 3, 5, 1)
)
stsSource2Entry.setIndexNames(
    (0, "SOCOMECUPSSTS-MIB", "stsSource2LineIndex"),
)
if mibBuilder.loadTexts:
    stsSource2Entry.setStatus("mandatory")


class _StsSource2LineIndex_Type(Integer32):
    """Custom type stsSource2LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StsSource2LineIndex_Type.__name__ = "Integer32"
_StsSource2LineIndex_Object = MibTableColumn
stsSource2LineIndex = _StsSource2LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 3, 5, 1, 1),
    _StsSource2LineIndex_Type()
)
stsSource2LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsSource2LineIndex.setStatus("mandatory")
_StsSource2Voltage_Type = Integer32
_StsSource2Voltage_Object = MibTableColumn
stsSource2Voltage = _StsSource2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 3, 5, 1, 2),
    _StsSource2Voltage_Type()
)
stsSource2Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsSource2Voltage.setStatus("mandatory")
_StsSources_ObjectIdentity = ObjectIdentity
stsSources = _StsSources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 4)
)


class _StsSourcesInteraction_Type(Integer32):
    """Custom type stsSourcesInteraction based on Integer32"""
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
        *(("unknown", 1),
          ("synchron", 2),
          ("sliding", 3),
          ("asychron", 4))
    )


_StsSourcesInteraction_Type.__name__ = "Integer32"
_StsSourcesInteraction_Object = MibScalar
stsSourcesInteraction = _StsSourcesInteraction_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 4, 1),
    _StsSourcesInteraction_Type()
)
stsSourcesInteraction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsSourcesInteraction.setStatus("mandatory")
_StsOutput_ObjectIdentity = ObjectIdentity
stsOutput = _StsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 5)
)


class _StsOutputLoadStatus_Type(Integer32):
    """Custom type stsOutputLoadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("outputLoadOnPreferredSource", 2),
          ("outputLoadOnAlternateSource", 3),
          ("outputLoadOFF", 4),
          ("outputLoadOnMBP1", 5),
          ("outputLoadOnMBP2", 6))
    )


_StsOutputLoadStatus_Type.__name__ = "Integer32"
_StsOutputLoadStatus_Object = MibScalar
stsOutputLoadStatus = _StsOutputLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 5, 1),
    _StsOutputLoadStatus_Type()
)
stsOutputLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputLoadStatus.setStatus("mandatory")


class _StsOutputStatus_Type(Integer32):
    """Custom type stsOutputStatus based on Integer32"""
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
        *(("unknown", 1),
          ("outputOnSwitch1", 2),
          ("outputOnSwitch2", 3),
          ("outputOFF", 4))
    )


_StsOutputStatus_Type.__name__ = "Integer32"
_StsOutputStatus_Object = MibScalar
stsOutputStatus = _StsOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 5, 2),
    _StsOutputStatus_Type()
)
stsOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputStatus.setStatus("mandatory")
_StsOutputFrequency_Type = Integer32
_StsOutputFrequency_Object = MibScalar
stsOutputFrequency = _StsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 5, 3),
    _StsOutputFrequency_Type()
)
stsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputFrequency.setStatus("mandatory")
_StsOutputLoadRate_Type = Integer32
_StsOutputLoadRate_Object = MibScalar
stsOutputLoadRate = _StsOutputLoadRate_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 5, 4),
    _StsOutputLoadRate_Type()
)
stsOutputLoadRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputLoadRate.setStatus("mandatory")
_StsOutputNumLines_Type = Integer32
_StsOutputNumLines_Object = MibScalar
stsOutputNumLines = _StsOutputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 5, 5),
    _StsOutputNumLines_Type()
)
stsOutputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputNumLines.setStatus("mandatory")
_StsOutputTable_Object = MibTable
stsOutputTable = _StsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 5, 6)
)
if mibBuilder.loadTexts:
    stsOutputTable.setStatus("mandatory")
_StsOutputEntry_Object = MibTableRow
stsOutputEntry = _StsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 5, 6, 1)
)
stsOutputEntry.setIndexNames(
    (0, "SOCOMECUPSSTS-MIB", "stsOutputLineIndex"),
)
if mibBuilder.loadTexts:
    stsOutputEntry.setStatus("mandatory")


class _StsOutputLineIndex_Type(Integer32):
    """Custom type stsOutputLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StsOutputLineIndex_Type.__name__ = "Integer32"
_StsOutputLineIndex_Object = MibTableColumn
stsOutputLineIndex = _StsOutputLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 5, 6, 1, 1),
    _StsOutputLineIndex_Type()
)
stsOutputLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputLineIndex.setStatus("mandatory")
_StsOutputVoltage_Type = Integer32
_StsOutputVoltage_Object = MibTableColumn
stsOutputVoltage = _StsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 5, 6, 1, 2),
    _StsOutputVoltage_Type()
)
stsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputVoltage.setStatus("mandatory")
_StsOutputCurrent_Type = Integer32
_StsOutputCurrent_Object = MibTableColumn
stsOutputCurrent = _StsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 5, 6, 1, 3),
    _StsOutputCurrent_Type()
)
stsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputCurrent.setStatus("mandatory")
_StsOutputkVA_Type = Integer32
_StsOutputkVA_Object = MibTableColumn
stsOutputkVA = _StsOutputkVA_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 5, 6, 1, 4),
    _StsOutputkVA_Type()
)
stsOutputkVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputkVA.setStatus("mandatory")
_StsOutputkW_Type = Integer32
_StsOutputkW_Object = MibTableColumn
stsOutputkW = _StsOutputkW_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 5, 6, 1, 5),
    _StsOutputkW_Type()
)
stsOutputkW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputkW.setStatus("mandatory")
_StsOutputCrestFactor_Type = Integer32
_StsOutputCrestFactor_Object = MibTableColumn
stsOutputCrestFactor = _StsOutputCrestFactor_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 5, 6, 1, 6),
    _StsOutputCrestFactor_Type()
)
stsOutputCrestFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputCrestFactor.setStatus("mandatory")
_StsOutputPowerFactor_Type = Integer32
_StsOutputPowerFactor_Object = MibTableColumn
stsOutputPowerFactor = _StsOutputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 5, 6, 1, 7),
    _StsOutputPowerFactor_Type()
)
stsOutputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputPowerFactor.setStatus("mandatory")
_StsAlarm_ObjectIdentity = ObjectIdentity
stsAlarm = _StsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 6)
)
_StsWellKnownAlarms_ObjectIdentity = ObjectIdentity
stsWellKnownAlarms = _StsWellKnownAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 6, 1)
)
_StsImminentStop_Type = Integer32
_StsImminentStop_Object = MibScalar
stsImminentStop = _StsImminentStop_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 6, 1, 1),
    _StsImminentStop_Type()
)
stsImminentStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsImminentStop.setStatus("mandatory")
_StsTransferImpossible_Type = Integer32
_StsTransferImpossible_Object = MibScalar
stsTransferImpossible = _StsTransferImpossible_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 6, 1, 2),
    _StsTransferImpossible_Type()
)
stsTransferImpossible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsTransferImpossible.setStatus("mandatory")
_StsConsecutiveDetection_Type = Integer32
_StsConsecutiveDetection_Object = MibScalar
stsConsecutiveDetection = _StsConsecutiveDetection_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 6, 1, 3),
    _StsConsecutiveDetection_Type()
)
stsConsecutiveDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsConsecutiveDetection.setStatus("mandatory")
_StsOverload_Type = Integer32
_StsOverload_Object = MibScalar
stsOverload = _StsOverload_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 6, 1, 4),
    _StsOverload_Type()
)
stsOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOverload.setStatus("mandatory")
_StsString1Alarm_Type = Integer32
_StsString1Alarm_Object = MibScalar
stsString1Alarm = _StsString1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 6, 1, 5),
    _StsString1Alarm_Type()
)
stsString1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsString1Alarm.setStatus("mandatory")
_StsString2Alarm_Type = Integer32
_StsString2Alarm_Object = MibScalar
stsString2Alarm = _StsString2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 6, 1, 6),
    _StsString2Alarm_Type()
)
stsString2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsString2Alarm.setStatus("mandatory")
_StsPreventiveMaintenance_Type = Integer32
_StsPreventiveMaintenance_Object = MibScalar
stsPreventiveMaintenance = _StsPreventiveMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 6, 1, 7),
    _StsPreventiveMaintenance_Type()
)
stsPreventiveMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsPreventiveMaintenance.setStatus("mandatory")
_StsGeneralAlarm_Type = Integer32
_StsGeneralAlarm_Object = MibScalar
stsGeneralAlarm = _StsGeneralAlarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 6, 1, 8),
    _StsGeneralAlarm_Type()
)
stsGeneralAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsGeneralAlarm.setStatus("mandatory")
_StsCustomInputAlarm_Type = Integer32
_StsCustomInputAlarm_Object = MibScalar
stsCustomInputAlarm = _StsCustomInputAlarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 6, 1, 9),
    _StsCustomInputAlarm_Type()
)
stsCustomInputAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsCustomInputAlarm.setStatus("mandatory")
_StsAgent_ObjectIdentity = ObjectIdentity
stsAgent = _StsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 7)
)
_StsAgentTrapString_Type = DisplayString
_StsAgentTrapString_Object = MibScalar
stsAgentTrapString = _StsAgentTrapString_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 1, 7, 1),
    _StsAgentTrapString_Type()
)
stsAgentTrapString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsAgentTrapString.setStatus("mandatory")
_StsTraps_ObjectIdentity = ObjectIdentity
stsTraps = _StsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 2)
)

# Managed Objects groups


# Notification objects

stsTrapImminentStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 2, 0, 1)
)
stsTrapImminentStop.setObjects(
    ("SOCOMECUPSSTS-MIB", "stsAgentTrapString")
)
if mibBuilder.loadTexts:
    stsTrapImminentStop.setStatus(
        ""
    )

stsTrapOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 2, 0, 2)
)
stsTrapOverload.setObjects(
    ("SOCOMECUPSSTS-MIB", "stsAgentTrapString")
)
if mibBuilder.loadTexts:
    stsTrapOverload.setStatus(
        ""
    )

stsTrapSwitchOnPreferedSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 2, 0, 3)
)
stsTrapSwitchOnPreferedSource.setObjects(
    ("SOCOMECUPSSTS-MIB", "stsAgentTrapString")
)
if mibBuilder.loadTexts:
    stsTrapSwitchOnPreferedSource.setStatus(
        ""
    )

stsTrapSwitchOnAlternateSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 2, 0, 4)
)
stsTrapSwitchOnAlternateSource.setObjects(
    ("SOCOMECUPSSTS-MIB", "stsAgentTrapString")
)
if mibBuilder.loadTexts:
    stsTrapSwitchOnAlternateSource.setStatus(
        ""
    )

stsTrapSource1PreferredSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 2, 0, 5)
)
stsTrapSource1PreferredSource.setObjects(
    ("SOCOMECUPSSTS-MIB", "stsAgentTrapString")
)
if mibBuilder.loadTexts:
    stsTrapSource1PreferredSource.setStatus(
        ""
    )

stsTrapOutputLoadOFF = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 2, 0, 6)
)
stsTrapOutputLoadOFF.setObjects(
    ("SOCOMECUPSSTS-MIB", "stsAgentTrapString")
)
if mibBuilder.loadTexts:
    stsTrapOutputLoadOFF.setStatus(
        ""
    )

stsTrapGeneralAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 2, 0, 7)
)
stsTrapGeneralAlarm.setObjects(
    ("SOCOMECUPSSTS-MIB", "stsAgentTrapString")
)
if mibBuilder.loadTexts:
    stsTrapGeneralAlarm.setStatus(
        ""
    )

stsTrapAlarmCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 10, 2, 0, 8)
)
stsTrapAlarmCancelled.setObjects(
    ("SOCOMECUPSSTS-MIB", "stsAgentTrapString")
)
if mibBuilder.loadTexts:
    stsTrapAlarmCancelled.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SOCOMECUPSSTS-MIB",
    **{"PositiveInteger": PositiveInteger,
       "NonNegativeInteger": NonNegativeInteger,
       "socomecUPS": socomecUPS,
       "software": software,
       "network": network,
       "connectsts": connectsts,
       "stsObjects": stsObjects,
       "stsIdent": stsIdent,
       "stsIdentModel": stsIdentModel,
       "stsIdentSerialNumber": stsIdentSerialNumber,
       "stsIdentFirmwareVersion": stsIdentFirmwareVersion,
       "stsIdentAgentSoftwareVersion": stsIdentAgentSoftwareVersion,
       "stsSource1": stsSource1,
       "stsSource1Status": stsSource1Status,
       "stsSource1Prefered": stsSource1Prefered,
       "stsSource1Frequency": stsSource1Frequency,
       "stsSource1NumLines": stsSource1NumLines,
       "stsSource1Table": stsSource1Table,
       "stsSource1Entry": stsSource1Entry,
       "stsSource1LineIndex": stsSource1LineIndex,
       "stsSource1Voltage": stsSource1Voltage,
       "stsSource2": stsSource2,
       "stsSource2Status": stsSource2Status,
       "stsSource2Prefered": stsSource2Prefered,
       "stsSource2Frequency": stsSource2Frequency,
       "stsSource2NumLines": stsSource2NumLines,
       "stsSource2Table": stsSource2Table,
       "stsSource2Entry": stsSource2Entry,
       "stsSource2LineIndex": stsSource2LineIndex,
       "stsSource2Voltage": stsSource2Voltage,
       "stsSources": stsSources,
       "stsSourcesInteraction": stsSourcesInteraction,
       "stsOutput": stsOutput,
       "stsOutputLoadStatus": stsOutputLoadStatus,
       "stsOutputStatus": stsOutputStatus,
       "stsOutputFrequency": stsOutputFrequency,
       "stsOutputLoadRate": stsOutputLoadRate,
       "stsOutputNumLines": stsOutputNumLines,
       "stsOutputTable": stsOutputTable,
       "stsOutputEntry": stsOutputEntry,
       "stsOutputLineIndex": stsOutputLineIndex,
       "stsOutputVoltage": stsOutputVoltage,
       "stsOutputCurrent": stsOutputCurrent,
       "stsOutputkVA": stsOutputkVA,
       "stsOutputkW": stsOutputkW,
       "stsOutputCrestFactor": stsOutputCrestFactor,
       "stsOutputPowerFactor": stsOutputPowerFactor,
       "stsAlarm": stsAlarm,
       "stsWellKnownAlarms": stsWellKnownAlarms,
       "stsImminentStop": stsImminentStop,
       "stsTransferImpossible": stsTransferImpossible,
       "stsConsecutiveDetection": stsConsecutiveDetection,
       "stsOverload": stsOverload,
       "stsString1Alarm": stsString1Alarm,
       "stsString2Alarm": stsString2Alarm,
       "stsPreventiveMaintenance": stsPreventiveMaintenance,
       "stsGeneralAlarm": stsGeneralAlarm,
       "stsCustomInputAlarm": stsCustomInputAlarm,
       "stsAgent": stsAgent,
       "stsAgentTrapString": stsAgentTrapString,
       "stsTraps": stsTraps,
       "stsTrapImminentStop": stsTrapImminentStop,
       "stsTrapOverload": stsTrapOverload,
       "stsTrapSwitchOnPreferedSource": stsTrapSwitchOnPreferedSource,
       "stsTrapSwitchOnAlternateSource": stsTrapSwitchOnAlternateSource,
       "stsTrapSource1PreferredSource": stsTrapSource1PreferredSource,
       "stsTrapOutputLoadOFF": stsTrapOutputLoadOFF,
       "stsTrapGeneralAlarm": stsTrapGeneralAlarm,
       "stsTrapAlarmCancelled": stsTrapAlarmCancelled}
)
