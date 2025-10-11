# SNMP MIB module (ELECTROLINE-COMMON-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-COMMON-TEST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:07:06 2025
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

(commonPrivate,) = mibBuilder.importSymbols(
    "ELECTROLINE-COMMON-ROOT-MIB",
    "commonPrivate")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class TenthCelsius(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


# MIB Managed Objects in the order of their OIDs



class _SwMode_Type(Integer32):
    """Custom type swMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              30)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("testOnly", 1),
          ("cmOnly", 2),
          ("scanFeatureInDiagnosticMode", 30))
    )


_SwMode_Type.__name__ = "Integer32"
_SwMode_Object = MibScalar
swMode = _SwMode_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 1),
    _SwMode_Type()
)
swMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMode.setStatus("current")
_ProdTest_ObjectIdentity = ObjectIdentity
prodTest = _ProdTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2)
)
if mibBuilder.loadTexts:
    prodTest.setStatus("current")
_ProdInventory_ObjectIdentity = ObjectIdentity
prodInventory = _ProdInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2, 1)
)
if mibBuilder.loadTexts:
    prodInventory.setStatus("current")
_ProdInvHwType_Type = Integer32
_ProdInvHwType_Object = MibScalar
prodInvHwType = _ProdInvHwType_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2, 1, 1),
    _ProdInvHwType_Type()
)
prodInvHwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prodInvHwType.setStatus("current")
_ProdInvHwMinorRev_Type = Integer32
_ProdInvHwMinorRev_Object = MibScalar
prodInvHwMinorRev = _ProdInvHwMinorRev_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2, 1, 2),
    _ProdInvHwMinorRev_Type()
)
prodInvHwMinorRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prodInvHwMinorRev.setStatus("current")
_ProdInvHwMajorRev_Type = Integer32
_ProdInvHwMajorRev_Object = MibScalar
prodInvHwMajorRev = _ProdInvHwMajorRev_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2, 1, 3),
    _ProdInvHwMajorRev_Type()
)
prodInvHwMajorRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prodInvHwMajorRev.setStatus("current")
_ProdInvHwDrvRev_Type = Integer32
_ProdInvHwDrvRev_Object = MibScalar
prodInvHwDrvRev = _ProdInvHwDrvRev_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2, 1, 4),
    _ProdInvHwDrvRev_Type()
)
prodInvHwDrvRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prodInvHwDrvRev.setStatus("current")


class _ProdModelNumber_Type(OctetString):
    """Custom type prodModelNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ProdModelNumber_Type.__name__ = "OctetString"
_ProdModelNumber_Object = MibScalar
prodModelNumber = _ProdModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2, 1, 5),
    _ProdModelNumber_Type()
)
prodModelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prodModelNumber.setStatus("current")
_ProdManufacturingInfo_ObjectIdentity = ObjectIdentity
prodManufacturingInfo = _ProdManufacturingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2, 1, 10)
)
if mibBuilder.loadTexts:
    prodManufacturingInfo.setStatus("current")
_ProdMfcDateTime_Type = DateAndTime
_ProdMfcDateTime_Object = MibScalar
prodMfcDateTime = _ProdMfcDateTime_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2, 1, 10, 1),
    _ProdMfcDateTime_Type()
)
prodMfcDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prodMfcDateTime.setStatus("current")
_ProdMfcTestSwVersion_Type = OctetString
_ProdMfcTestSwVersion_Object = MibScalar
prodMfcTestSwVersion = _ProdMfcTestSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2, 1, 10, 2),
    _ProdMfcTestSwVersion_Type()
)
prodMfcTestSwVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prodMfcTestSwVersion.setStatus("current")
_ProdConfiguration_ObjectIdentity = ObjectIdentity
prodConfiguration = _ProdConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2, 2)
)
if mibBuilder.loadTexts:
    prodConfiguration.setStatus("current")


class _ProdFormatFlash_Type(Integer32):
    """Custom type prodFormatFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("format", 1)
    )


_ProdFormatFlash_Type.__name__ = "Integer32"
_ProdFormatFlash_Object = MibScalar
prodFormatFlash = _ProdFormatFlash_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2, 2, 1),
    _ProdFormatFlash_Type()
)
prodFormatFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prodFormatFlash.setStatus("current")


class _ProdDocsisMode_Type(Integer32):
    """Custom type prodDocsisMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("docsis", 1),
          ("euroDocsis", 2))
    )


_ProdDocsisMode_Type.__name__ = "Integer32"
_ProdDocsisMode_Object = MibScalar
prodDocsisMode = _ProdDocsisMode_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2, 2, 2),
    _ProdDocsisMode_Type()
)
prodDocsisMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prodDocsisMode.setStatus("current")
_LedsControl_ObjectIdentity = ObjectIdentity
ledsControl = _LedsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2, 3)
)
if mibBuilder.loadTexts:
    ledsControl.setStatus("current")
_LedsControlTable_Object = MibTable
ledsControlTable = _LedsControlTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ledsControlTable.setStatus("current")
_LedsControlEntry_Object = MibTableRow
ledsControlEntry = _LedsControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2, 3, 1, 1)
)
ledsControlEntry.setIndexNames(
    (0, "ELECTROLINE-COMMON-TEST-MIB", "ledId"),
)
if mibBuilder.loadTexts:
    ledsControlEntry.setStatus("current")
_LedId_Type = Integer32
_LedId_Object = MibTableColumn
ledId = _LedId_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2, 3, 1, 1, 1),
    _LedId_Type()
)
ledId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledId.setStatus("current")


class _LedState_Type(Integer32):
    """Custom type ledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_LedState_Type.__name__ = "Integer32"
_LedState_Object = MibTableColumn
ledState = _LedState_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2, 3, 1, 1, 2),
    _LedState_Type()
)
ledState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledState.setStatus("current")
_LedDesc_Type = OctetString
_LedDesc_Object = MibTableColumn
ledDesc = _LedDesc_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 2, 3, 1, 1, 3),
    _LedDesc_Type()
)
ledDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledDesc.setStatus("current")
_ElineSpectrumAnalyzer_ObjectIdentity = ObjectIdentity
elineSpectrumAnalyzer = _ElineSpectrumAnalyzer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 3)
)
if mibBuilder.loadTexts:
    elineSpectrumAnalyzer.setStatus("current")
_PlantPower_ObjectIdentity = ObjectIdentity
plantPower = _PlantPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 3, 1)
)
if mibBuilder.loadTexts:
    plantPower.setStatus("current")
_PlantPowerStartFrequency_Type = Integer32
_PlantPowerStartFrequency_Object = MibScalar
plantPowerStartFrequency = _PlantPowerStartFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 3, 1, 1),
    _PlantPowerStartFrequency_Type()
)
plantPowerStartFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plantPowerStartFrequency.setStatus("current")
_PlantPowerStopFrequency_Type = Integer32
_PlantPowerStopFrequency_Object = MibScalar
plantPowerStopFrequency = _PlantPowerStopFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 3, 1, 2),
    _PlantPowerStopFrequency_Type()
)
plantPowerStopFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plantPowerStopFrequency.setStatus("current")
_PlantPowerNbAverage_Type = Integer32
_PlantPowerNbAverage_Object = MibScalar
plantPowerNbAverage = _PlantPowerNbAverage_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 3, 1, 3),
    _PlantPowerNbAverage_Type()
)
plantPowerNbAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plantPowerNbAverage.setStatus("current")
_PlantPowerPower_Type = Integer32
_PlantPowerPower_Object = MibScalar
plantPowerPower = _PlantPowerPower_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 3, 1, 4),
    _PlantPowerPower_Type()
)
plantPowerPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plantPowerPower.setStatus("current")
_PlanPowerRBW_Type = Integer32
_PlanPowerRBW_Object = MibScalar
planPowerRBW = _PlanPowerRBW_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 3, 1, 5),
    _PlanPowerRBW_Type()
)
planPowerRBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    planPowerRBW.setStatus("current")
_PlantPowerNbBins_Type = Integer32
_PlantPowerNbBins_Object = MibScalar
plantPowerNbBins = _PlantPowerNbBins_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 3, 1, 6),
    _PlantPowerNbBins_Type()
)
plantPowerNbBins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plantPowerNbBins.setStatus("current")
_PrivateStatus_ObjectIdentity = ObjectIdentity
privateStatus = _PrivateStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 4)
)
if mibBuilder.loadTexts:
    privateStatus.setStatus("current")
_DieTemperature_Type = TenthCelsius
_DieTemperature_Object = MibScalar
dieTemperature = _DieTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4, 4, 1),
    _DieTemperature_Type()
)
dieTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dieTemperature.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-COMMON-TEST-MIB",
    **{"TenthCelsius": TenthCelsius,
       "swMode": swMode,
       "prodTest": prodTest,
       "prodInventory": prodInventory,
       "prodInvHwType": prodInvHwType,
       "prodInvHwMinorRev": prodInvHwMinorRev,
       "prodInvHwMajorRev": prodInvHwMajorRev,
       "prodInvHwDrvRev": prodInvHwDrvRev,
       "prodModelNumber": prodModelNumber,
       "prodManufacturingInfo": prodManufacturingInfo,
       "prodMfcDateTime": prodMfcDateTime,
       "prodMfcTestSwVersion": prodMfcTestSwVersion,
       "prodConfiguration": prodConfiguration,
       "prodFormatFlash": prodFormatFlash,
       "prodDocsisMode": prodDocsisMode,
       "ledsControl": ledsControl,
       "ledsControlTable": ledsControlTable,
       "ledsControlEntry": ledsControlEntry,
       "ledId": ledId,
       "ledState": ledState,
       "ledDesc": ledDesc,
       "elineSpectrumAnalyzer": elineSpectrumAnalyzer,
       "plantPower": plantPower,
       "plantPowerStartFrequency": plantPowerStartFrequency,
       "plantPowerStopFrequency": plantPowerStopFrequency,
       "plantPowerNbAverage": plantPowerNbAverage,
       "plantPowerPower": plantPowerPower,
       "planPowerRBW": planPowerRBW,
       "plantPowerNbBins": plantPowerNbBins,
       "privateStatus": privateStatus,
       "dieTemperature": dieTemperature}
)
