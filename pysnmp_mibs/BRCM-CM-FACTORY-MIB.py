# SNMP MIB module (BRCM-CM-FACTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-CM-FACTORY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:52 2025
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

(cableDataFactory,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-FACTORY-MIB",
    "cableDataFactory")

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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cablemodemFactory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cablemodemFactory.setRevisions(
        ("2011-04-20 00:00",
         "2011-01-17 00:00",
         "2010-12-10 00:00",
         "2010-08-18 00:00",
         "2009-10-07 00:00",
         "2008-08-26 00:00",
         "2007-02-05 00:00",
         "2007-02-02 00:00",
         "2006-01-27 00:00",
         "2005-11-14 00:00",
         "2005-05-10 00:00",
         "2004-12-30 00:00",
         "2004-12-14 00:00",
         "2004-06-01 00:00",
         "2004-03-24 00:00",
         "2003-08-13 00:00",
         "2003-05-21 00:00",
         "2002-12-23 00:00",
         "2002-12-12 00:00",
         "2002-11-12 00:00",
         "2002-06-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmFactoryBase_ObjectIdentity = ObjectIdentity
cmFactoryBase = _CmFactoryBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 1)
)


class _CmFactOperMode_Type(Integer32):
    """Custom type cmFactOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("docsis", 1),
          ("diagnostic", 2))
    )


_CmFactOperMode_Type.__name__ = "Integer32"
_CmFactOperMode_Object = MibScalar
cmFactOperMode = _CmFactOperMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 1, 1),
    _CmFactOperMode_Type()
)
cmFactOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFactOperMode.setStatus("current")
_CmFactSwBcmVersion_Type = DisplayString
_CmFactSwBcmVersion_Object = MibScalar
cmFactSwBcmVersion = _CmFactSwBcmVersion_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 1, 2),
    _CmFactSwBcmVersion_Type()
)
cmFactSwBcmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFactSwBcmVersion.setStatus("current")
_CmFactSwDateTime_Type = DisplayString
_CmFactSwDateTime_Object = MibScalar
cmFactSwDateTime = _CmFactSwDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 1, 3),
    _CmFactSwDateTime_Type()
)
cmFactSwDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFactSwDateTime.setStatus("current")
_CmFactSwBuiltBy_Type = DisplayString
_CmFactSwBuiltBy_Object = MibScalar
cmFactSwBuiltBy = _CmFactSwBuiltBy_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 1, 4),
    _CmFactSwBuiltBy_Type()
)
cmFactSwBuiltBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFactSwBuiltBy.setStatus("current")
_CmFactSwFeatures_Type = DisplayString
_CmFactSwFeatures_Object = MibScalar
cmFactSwFeatures = _CmFactSwFeatures_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 1, 5),
    _CmFactSwFeatures_Type()
)
cmFactSwFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFactSwFeatures.setStatus("current")
_CmFactAckCelEnable_Type = TruthValue
_CmFactAckCelEnable_Object = MibScalar
cmFactAckCelEnable = _CmFactAckCelEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 1, 6),
    _CmFactAckCelEnable_Type()
)
cmFactAckCelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFactAckCelEnable.setStatus("current")
_CmFactNonstdUpstreamEnable_Type = TruthValue
_CmFactNonstdUpstreamEnable_Object = MibScalar
cmFactNonstdUpstreamEnable = _CmFactNonstdUpstreamEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 1, 7),
    _CmFactNonstdUpstreamEnable_Type()
)
cmFactNonstdUpstreamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFactNonstdUpstreamEnable.setStatus("current")
_CmFactPowerSaveModeEnable_Type = TruthValue
_CmFactPowerSaveModeEnable_Object = MibScalar
cmFactPowerSaveModeEnable = _CmFactPowerSaveModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 1, 8),
    _CmFactPowerSaveModeEnable_Type()
)
cmFactPowerSaveModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFactPowerSaveModeEnable.setStatus("current")
_CmFactOptimized3420FreqMapEnable_Type = TruthValue
_CmFactOptimized3420FreqMapEnable_Object = MibScalar
cmFactOptimized3420FreqMapEnable = _CmFactOptimized3420FreqMapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 1, 9),
    _CmFactOptimized3420FreqMapEnable_Type()
)
cmFactOptimized3420FreqMapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFactOptimized3420FreqMapEnable.setStatus("current")
_CmFactHighOutputPAEnable_Type = TruthValue
_CmFactHighOutputPAEnable_Object = MibScalar
cmFactHighOutputPAEnable = _CmFactHighOutputPAEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 1, 10),
    _CmFactHighOutputPAEnable_Type()
)
cmFactHighOutputPAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFactHighOutputPAEnable.setStatus("current")
_CmFactChannelBondingEnable_Type = TruthValue
_CmFactChannelBondingEnable_Object = MibScalar
cmFactChannelBondingEnable = _CmFactChannelBondingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 1, 11),
    _CmFactChannelBondingEnable_Type()
)
cmFactChannelBondingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFactChannelBondingEnable.setStatus("current")


class _CmFactEnabledTuners_Type(Integer32):
    """Custom type cmFactEnabledTuners based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CmFactEnabledTuners_Type.__name__ = "Integer32"
_CmFactEnabledTuners_Object = MibScalar
cmFactEnabledTuners = _CmFactEnabledTuners_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 1, 12),
    _CmFactEnabledTuners_Type()
)
cmFactEnabledTuners.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFactEnabledTuners.setStatus("current")


class _CmFactAnnex_Type(Integer32):
    """Custom type cmFactAnnex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("annexB", 0),
          ("annexA", 1),
          ("annexJ", 2),
          ("annexOther", 3),
          ("annexC", 4))
    )


_CmFactAnnex_Type.__name__ = "Integer32"
_CmFactAnnex_Object = MibScalar
cmFactAnnex = _CmFactAnnex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 1, 13),
    _CmFactAnnex_Type()
)
cmFactAnnex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFactAnnex.setStatus("current")


class _CmFactExtendedUsTxPowerCapability_Type(Integer32):
    """Custom type cmFactExtendedUsTxPowerCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(205, 244),
    )


_CmFactExtendedUsTxPowerCapability_Type.__name__ = "Integer32"
_CmFactExtendedUsTxPowerCapability_Object = MibScalar
cmFactExtendedUsTxPowerCapability = _CmFactExtendedUsTxPowerCapability_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 1, 14),
    _CmFactExtendedUsTxPowerCapability_Type()
)
cmFactExtendedUsTxPowerCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFactExtendedUsTxPowerCapability.setStatus("current")
if mibBuilder.loadTexts:
    cmFactExtendedUsTxPowerCapability.setUnits("quarter dBmV")
_CmFactoryBaselinePrivacy_ObjectIdentity = ObjectIdentity
cmFactoryBaselinePrivacy = _CmFactoryBaselinePrivacy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 2)
)
_CmBpiPublicKey_Type = OctetString
_CmBpiPublicKey_Object = MibScalar
cmBpiPublicKey = _CmBpiPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 2, 1),
    _CmBpiPublicKey_Type()
)
cmBpiPublicKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmBpiPublicKey.setStatus("current")
_CmBpiPrivateKey_Type = OctetString
_CmBpiPrivateKey_Object = MibScalar
cmBpiPrivateKey = _CmBpiPrivateKey_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 2, 2),
    _CmBpiPrivateKey_Type()
)
cmBpiPrivateKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmBpiPrivateKey.setStatus("current")
_CmBpiPlusRootPublicKey_Type = OctetString
_CmBpiPlusRootPublicKey_Object = MibScalar
cmBpiPlusRootPublicKey = _CmBpiPlusRootPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 2, 3),
    _CmBpiPlusRootPublicKey_Type()
)
cmBpiPlusRootPublicKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmBpiPlusRootPublicKey.setStatus("current")
_CmBpiPlusCmCertificate_Type = OctetString
_CmBpiPlusCmCertificate_Object = MibScalar
cmBpiPlusCmCertificate = _CmBpiPlusCmCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 2, 4),
    _CmBpiPlusCmCertificate_Type()
)
cmBpiPlusCmCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmBpiPlusCmCertificate.setStatus("current")
_CmBpiPlusCaCertificate_Type = OctetString
_CmBpiPlusCaCertificate_Object = MibScalar
cmBpiPlusCaCertificate = _CmBpiPlusCaCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 2, 5),
    _CmBpiPlusCaCertificate_Type()
)
cmBpiPlusCaCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmBpiPlusCaCertificate.setStatus("current")
_CmFactoryDownstreamCalibration_ObjectIdentity = ObjectIdentity
cmFactoryDownstreamCalibration = _CmFactoryDownstreamCalibration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 3)
)


class _CmDsCalFrequency_Type(Integer32):
    """Custom type cmDsCalFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CmDsCalFrequency_Type.__name__ = "Integer32"
_CmDsCalFrequency_Object = MibScalar
cmDsCalFrequency = _CmDsCalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 3, 1),
    _CmDsCalFrequency_Type()
)
cmDsCalFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalFrequency.setUnits("hertz")


class _CmDsCalModulation_Type(Integer32):
    """Custom type cmDsCalModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("qam64", 3),
          ("qam256", 4),
          ("qam1024", 5))
    )


_CmDsCalModulation_Type.__name__ = "Integer32"
_CmDsCalModulation_Object = MibScalar
cmDsCalModulation = _CmDsCalModulation_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 3, 2),
    _CmDsCalModulation_Type()
)
cmDsCalModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalModulation.setStatus("current")
_CmDsCalLockNow_Type = TruthValue
_CmDsCalLockNow_Object = MibScalar
cmDsCalLockNow = _CmDsCalLockNow_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 3, 3),
    _CmDsCalLockNow_Type()
)
cmDsCalLockNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalLockNow.setStatus("current")
_CmDsCalQamLocked_Type = TruthValue
_CmDsCalQamLocked_Object = MibScalar
cmDsCalQamLocked = _CmDsCalQamLocked_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 3, 4),
    _CmDsCalQamLocked_Type()
)
cmDsCalQamLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalQamLocked.setStatus("current")
_CmDsCalFecLocked_Type = TruthValue
_CmDsCalFecLocked_Object = MibScalar
cmDsCalFecLocked = _CmDsCalFecLocked_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 3, 5),
    _CmDsCalFecLocked_Type()
)
cmDsCalFecLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalFecLocked.setStatus("current")
_CmDsCalZeroOffsets_Type = TruthValue
_CmDsCalZeroOffsets_Object = MibScalar
cmDsCalZeroOffsets = _CmDsCalZeroOffsets_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 3, 6),
    _CmDsCalZeroOffsets_Type()
)
cmDsCalZeroOffsets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalZeroOffsets.setStatus("current")
_CmDsCalNumOffsets_Type = Unsigned32
_CmDsCalNumOffsets_Object = MibScalar
cmDsCalNumOffsets = _CmDsCalNumOffsets_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 3, 7),
    _CmDsCalNumOffsets_Type()
)
cmDsCalNumOffsets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalNumOffsets.setStatus("current")
_CmDsCalOffsetTable_Object = MibTable
cmDsCalOffsetTable = _CmDsCalOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    cmDsCalOffsetTable.setStatus("current")
_CmDsCalOffsetEntry_Object = MibTableRow
cmDsCalOffsetEntry = _CmDsCalOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 3, 8, 1)
)
cmDsCalOffsetEntry.setIndexNames(
    (0, "BRCM-CM-FACTORY-MIB", "cmDsCalOffsetIndex"),
)
if mibBuilder.loadTexts:
    cmDsCalOffsetEntry.setStatus("current")


class _CmDsCalOffsetIndex_Type(Integer32):
    """Custom type cmDsCalOffsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CmDsCalOffsetIndex_Type.__name__ = "Integer32"
_CmDsCalOffsetIndex_Object = MibTableColumn
cmDsCalOffsetIndex = _CmDsCalOffsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 3, 8, 1, 1),
    _CmDsCalOffsetIndex_Type()
)
cmDsCalOffsetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmDsCalOffsetIndex.setStatus("current")
_CmDsCalOffsetFrequency_Type = Integer32
_CmDsCalOffsetFrequency_Object = MibTableColumn
cmDsCalOffsetFrequency = _CmDsCalOffsetFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 3, 8, 1, 2),
    _CmDsCalOffsetFrequency_Type()
)
cmDsCalOffsetFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalOffsetFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalOffsetFrequency.setUnits("hertz")
_CmDsCalOffsetPower_Type = Integer32
_CmDsCalOffsetPower_Object = MibTableColumn
cmDsCalOffsetPower = _CmDsCalOffsetPower_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 3, 8, 1, 3),
    _CmDsCalOffsetPower_Type()
)
cmDsCalOffsetPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalOffsetPower.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalOffsetPower.setUnits("hundredth dBmV")


class _CmDsCalChannelNumber_Type(Integer32):
    """Custom type cmDsCalChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CmDsCalChannelNumber_Type.__name__ = "Integer32"
_CmDsCalChannelNumber_Object = MibScalar
cmDsCalChannelNumber = _CmDsCalChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 3, 9),
    _CmDsCalChannelNumber_Type()
)
cmDsCalChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalChannelNumber.setStatus("current")
_CmFactoryUpstreamCalibration_ObjectIdentity = ObjectIdentity
cmFactoryUpstreamCalibration = _CmFactoryUpstreamCalibration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 4)
)


class _CmUsCalFrequency_Type(Integer32):
    """Custom type cmUsCalFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CmUsCalFrequency_Type.__name__ = "Integer32"
_CmUsCalFrequency_Object = MibScalar
cmUsCalFrequency = _CmUsCalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 4, 1),
    _CmUsCalFrequency_Type()
)
cmUsCalFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cmUsCalFrequency.setUnits("hertz")


class _CmUsCalChannelWidth_Type(Integer32):
    """Custom type cmUsCalChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000000),
    )


_CmUsCalChannelWidth_Type.__name__ = "Integer32"
_CmUsCalChannelWidth_Object = MibScalar
cmUsCalChannelWidth = _CmUsCalChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 4, 2),
    _CmUsCalChannelWidth_Type()
)
cmUsCalChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalChannelWidth.setStatus("current")
if mibBuilder.loadTexts:
    cmUsCalChannelWidth.setUnits("hertz")


class _CmUsCalModulation_Type(Integer32):
    """Custom type cmUsCalModulation based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("cw", 1),
          ("qpsk", 2),
          ("qam16", 3),
          ("qam8", 4),
          ("qam32", 5),
          ("qam64", 6),
          ("qam128", 7),
          ("qam256", 8))
    )


_CmUsCalModulation_Type.__name__ = "Integer32"
_CmUsCalModulation_Object = MibScalar
cmUsCalModulation = _CmUsCalModulation_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 4, 3),
    _CmUsCalModulation_Type()
)
cmUsCalModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalModulation.setStatus("current")
_CmUsCalTxPower_Type = Integer32
_CmUsCalTxPower_Object = MibScalar
cmUsCalTxPower = _CmUsCalTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 4, 4),
    _CmUsCalTxPower_Type()
)
cmUsCalTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalTxPower.setStatus("current")
if mibBuilder.loadTexts:
    cmUsCalTxPower.setUnits("hundredth dBmV")
_CmUsCalZeroOffsets_Type = TruthValue
_CmUsCalZeroOffsets_Object = MibScalar
cmUsCalZeroOffsets = _CmUsCalZeroOffsets_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 4, 5),
    _CmUsCalZeroOffsets_Type()
)
cmUsCalZeroOffsets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalZeroOffsets.setStatus("current")
_CmUsCalNumOffsets_Type = Unsigned32
_CmUsCalNumOffsets_Object = MibScalar
cmUsCalNumOffsets = _CmUsCalNumOffsets_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 4, 6),
    _CmUsCalNumOffsets_Type()
)
cmUsCalNumOffsets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmUsCalNumOffsets.setStatus("current")
_CmUsCalOffsetTable_Object = MibTable
cmUsCalOffsetTable = _CmUsCalOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 4, 7)
)
if mibBuilder.loadTexts:
    cmUsCalOffsetTable.setStatus("current")
_CmUsCalOffsetEntry_Object = MibTableRow
cmUsCalOffsetEntry = _CmUsCalOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 4, 7, 1)
)
cmUsCalOffsetEntry.setIndexNames(
    (0, "BRCM-CM-FACTORY-MIB", "cmUsCalOffsetIndex"),
)
if mibBuilder.loadTexts:
    cmUsCalOffsetEntry.setStatus("current")


class _CmUsCalOffsetIndex_Type(Integer32):
    """Custom type cmUsCalOffsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CmUsCalOffsetIndex_Type.__name__ = "Integer32"
_CmUsCalOffsetIndex_Object = MibTableColumn
cmUsCalOffsetIndex = _CmUsCalOffsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 4, 7, 1, 1),
    _CmUsCalOffsetIndex_Type()
)
cmUsCalOffsetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmUsCalOffsetIndex.setStatus("current")
_CmUsCalOffsetFrequency_Type = Integer32
_CmUsCalOffsetFrequency_Object = MibTableColumn
cmUsCalOffsetFrequency = _CmUsCalOffsetFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 4, 7, 1, 2),
    _CmUsCalOffsetFrequency_Type()
)
cmUsCalOffsetFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmUsCalOffsetFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cmUsCalOffsetFrequency.setUnits("hundredth MHz")
_CmUsCalOffsetPower_Type = Integer32
_CmUsCalOffsetPower_Object = MibTableColumn
cmUsCalOffsetPower = _CmUsCalOffsetPower_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 4, 7, 1, 3),
    _CmUsCalOffsetPower_Type()
)
cmUsCalOffsetPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalOffsetPower.setStatus("current")
if mibBuilder.loadTexts:
    cmUsCalOffsetPower.setUnits("hundredth dBmV")


class _CmUsCalChannelNumber_Type(Integer32):
    """Custom type cmUsCalChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CmUsCalChannelNumber_Type.__name__ = "Integer32"
_CmUsCalChannelNumber_Object = MibScalar
cmUsCalChannelNumber = _CmUsCalChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 4, 8),
    _CmUsCalChannelNumber_Type()
)
cmUsCalChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalChannelNumber.setStatus("current")
_CmFactoryHardware_ObjectIdentity = ObjectIdentity
cmFactoryHardware = _CmFactoryHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 5)
)


class _CmHwSTATHR_Type(Unsigned32):
    """Custom type cmHwSTATHR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmHwSTATHR_Type.__name__ = "Unsigned32"
_CmHwSTATHR_Object = MibScalar
cmHwSTATHR = _CmHwSTATHR_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 5, 1),
    _CmHwSTATHR_Type()
)
cmHwSTATHR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmHwSTATHR.setStatus("current")
_CmHwSTAGI_Type = Unsigned32
_CmHwSTAGI_Object = MibScalar
cmHwSTAGI = _CmHwSTAGI_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 5, 2),
    _CmHwSTAGI_Type()
)
cmHwSTAGI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmHwSTAGI.setStatus("current")
_CmHwSTAGT_Type = Unsigned32
_CmHwSTAGT_Object = MibScalar
cmHwSTAGT = _CmHwSTAGT_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 5, 3),
    _CmHwSTAGT_Type()
)
cmHwSTAGT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmHwSTAGT.setStatus("current")
_CmHwAdvanceMapRunAheadEnable_Type = TruthValue
_CmHwAdvanceMapRunAheadEnable_Object = MibScalar
cmHwAdvanceMapRunAheadEnable = _CmHwAdvanceMapRunAheadEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 5, 4),
    _CmHwAdvanceMapRunAheadEnable_Type()
)
cmHwAdvanceMapRunAheadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmHwAdvanceMapRunAheadEnable.setStatus("current")
_CmFactoryOtp_ObjectIdentity = ObjectIdentity
cmFactoryOtp = _CmFactoryOtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 6)
)
_CmOtpIsProgrammed_Type = TruthValue
_CmOtpIsProgrammed_Object = MibScalar
cmOtpIsProgrammed = _CmOtpIsProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 6, 1),
    _CmOtpIsProgrammed_Type()
)
cmOtpIsProgrammed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOtpIsProgrammed.setStatus("current")
_CmOtpProgramNow_Type = TruthValue
_CmOtpProgramNow_Object = MibScalar
cmOtpProgramNow = _CmOtpProgramNow_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 6, 2),
    _CmOtpProgramNow_Type()
)
cmOtpProgramNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmOtpProgramNow.setStatus("current")


class _CmOtpProgramResult_Type(Integer32):
    """Custom type cmOtpProgramResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAttempted", -1),
          ("success", 0),
          ("failedAlreadyProgrammed", 1),
          ("failedProgrammingNotSupported", 2),
          ("failedHardwareFailure", 3))
    )


_CmOtpProgramResult_Type.__name__ = "Integer32"
_CmOtpProgramResult_Object = MibScalar
cmOtpProgramResult = _CmOtpProgramResult_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 6, 3),
    _CmOtpProgramResult_Type()
)
cmOtpProgramResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOtpProgramResult.setStatus("current")


class _CmOtpRawBitsSize_Type(Unsigned32):
    """Custom type cmOtpRawBitsSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CmOtpRawBitsSize_Type.__name__ = "Unsigned32"
_CmOtpRawBitsSize_Object = MibScalar
cmOtpRawBitsSize = _CmOtpRawBitsSize_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 6, 4),
    _CmOtpRawBitsSize_Type()
)
cmOtpRawBitsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOtpRawBitsSize.setStatus("current")
_CmOtpRawBits_Type = Unsigned32
_CmOtpRawBits_Object = MibScalar
cmOtpRawBits = _CmOtpRawBits_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 6, 5),
    _CmOtpRawBits_Type()
)
cmOtpRawBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmOtpRawBits.setStatus("current")


class _CmOtpCustomerDefinedBitsSize_Type(Unsigned32):
    """Custom type cmOtpCustomerDefinedBitsSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CmOtpCustomerDefinedBitsSize_Type.__name__ = "Unsigned32"
_CmOtpCustomerDefinedBitsSize_Object = MibScalar
cmOtpCustomerDefinedBitsSize = _CmOtpCustomerDefinedBitsSize_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 6, 6),
    _CmOtpCustomerDefinedBitsSize_Type()
)
cmOtpCustomerDefinedBitsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOtpCustomerDefinedBitsSize.setStatus("current")
_CmOtpCustomerDefinedBits_Type = Unsigned32
_CmOtpCustomerDefinedBits_Object = MibScalar
cmOtpCustomerDefinedBits = _CmOtpCustomerDefinedBits_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 6, 7),
    _CmOtpCustomerDefinedBits_Type()
)
cmOtpCustomerDefinedBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmOtpCustomerDefinedBits.setStatus("current")


class _CmOtpSecurityLevel_Type(Integer32):
    """Custom type cmOtpSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSecurity", 0),
          ("partialSecurity", 1),
          ("fullSecurity", 2))
    )


_CmOtpSecurityLevel_Type.__name__ = "Integer32"
_CmOtpSecurityLevel_Object = MibScalar
cmOtpSecurityLevel = _CmOtpSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 6, 8),
    _CmOtpSecurityLevel_Type()
)
cmOtpSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmOtpSecurityLevel.setStatus("current")
_CmOtpJtagDisabled_Type = TruthValue
_CmOtpJtagDisabled_Object = MibScalar
cmOtpJtagDisabled = _CmOtpJtagDisabled_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 6, 9),
    _CmOtpJtagDisabled_Type()
)
cmOtpJtagDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmOtpJtagDisabled.setStatus("current")
_CmOtpConsoleDisabled_Type = TruthValue
_CmOtpConsoleDisabled_Object = MibScalar
cmOtpConsoleDisabled = _CmOtpConsoleDisabled_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 6, 10),
    _CmOtpConsoleDisabled_Type()
)
cmOtpConsoleDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmOtpConsoleDisabled.setStatus("current")
_CmOtpSpiSlaveDisabled_Type = TruthValue
_CmOtpSpiSlaveDisabled_Object = MibScalar
cmOtpSpiSlaveDisabled = _CmOtpSpiSlaveDisabled_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 6, 11),
    _CmOtpSpiSlaveDisabled_Type()
)
cmOtpSpiSlaveDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmOtpSpiSlaveDisabled.setStatus("current")


class _CmOtpMpiAccessControl_Type(Integer32):
    """Custom type cmOtpMpiAccessControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mpiFullAccess", 0),
          ("mpiRestrictedAccess", 1),
          ("mpiNoAccess", 3))
    )


_CmOtpMpiAccessControl_Type.__name__ = "Integer32"
_CmOtpMpiAccessControl_Object = MibScalar
cmOtpMpiAccessControl = _CmOtpMpiAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 6, 12),
    _CmOtpMpiAccessControl_Type()
)
cmOtpMpiAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmOtpMpiAccessControl.setStatus("current")
_CmOtpBootRomEnabled_Type = TruthValue
_CmOtpBootRomEnabled_Object = MibScalar
cmOtpBootRomEnabled = _CmOtpBootRomEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 6, 13),
    _CmOtpBootRomEnabled_Type()
)
cmOtpBootRomEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmOtpBootRomEnabled.setStatus("current")
_CmOtpRamScramblerEnabled_Type = TruthValue
_CmOtpRamScramblerEnabled_Object = MibScalar
cmOtpRamScramblerEnabled = _CmOtpRamScramblerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 6, 14),
    _CmOtpRamScramblerEnabled_Type()
)
cmOtpRamScramblerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmOtpRamScramblerEnabled.setStatus("current")
_CmFactoryFpm_ObjectIdentity = ObjectIdentity
cmFactoryFpm = _CmFactoryFpm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 7)
)
_CmFpmTokenDepletionWatchdogEnable_Type = TruthValue
_CmFpmTokenDepletionWatchdogEnable_Object = MibScalar
cmFpmTokenDepletionWatchdogEnable = _CmFpmTokenDepletionWatchdogEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 2, 7, 1),
    _CmFpmTokenDepletionWatchdogEnable_Type()
)
cmFpmTokenDepletionWatchdogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFpmTokenDepletionWatchdogEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-CM-FACTORY-MIB",
    **{"cablemodemFactory": cablemodemFactory,
       "cmFactoryBase": cmFactoryBase,
       "cmFactOperMode": cmFactOperMode,
       "cmFactSwBcmVersion": cmFactSwBcmVersion,
       "cmFactSwDateTime": cmFactSwDateTime,
       "cmFactSwBuiltBy": cmFactSwBuiltBy,
       "cmFactSwFeatures": cmFactSwFeatures,
       "cmFactAckCelEnable": cmFactAckCelEnable,
       "cmFactNonstdUpstreamEnable": cmFactNonstdUpstreamEnable,
       "cmFactPowerSaveModeEnable": cmFactPowerSaveModeEnable,
       "cmFactOptimized3420FreqMapEnable": cmFactOptimized3420FreqMapEnable,
       "cmFactHighOutputPAEnable": cmFactHighOutputPAEnable,
       "cmFactChannelBondingEnable": cmFactChannelBondingEnable,
       "cmFactEnabledTuners": cmFactEnabledTuners,
       "cmFactAnnex": cmFactAnnex,
       "cmFactExtendedUsTxPowerCapability": cmFactExtendedUsTxPowerCapability,
       "cmFactoryBaselinePrivacy": cmFactoryBaselinePrivacy,
       "cmBpiPublicKey": cmBpiPublicKey,
       "cmBpiPrivateKey": cmBpiPrivateKey,
       "cmBpiPlusRootPublicKey": cmBpiPlusRootPublicKey,
       "cmBpiPlusCmCertificate": cmBpiPlusCmCertificate,
       "cmBpiPlusCaCertificate": cmBpiPlusCaCertificate,
       "cmFactoryDownstreamCalibration": cmFactoryDownstreamCalibration,
       "cmDsCalFrequency": cmDsCalFrequency,
       "cmDsCalModulation": cmDsCalModulation,
       "cmDsCalLockNow": cmDsCalLockNow,
       "cmDsCalQamLocked": cmDsCalQamLocked,
       "cmDsCalFecLocked": cmDsCalFecLocked,
       "cmDsCalZeroOffsets": cmDsCalZeroOffsets,
       "cmDsCalNumOffsets": cmDsCalNumOffsets,
       "cmDsCalOffsetTable": cmDsCalOffsetTable,
       "cmDsCalOffsetEntry": cmDsCalOffsetEntry,
       "cmDsCalOffsetIndex": cmDsCalOffsetIndex,
       "cmDsCalOffsetFrequency": cmDsCalOffsetFrequency,
       "cmDsCalOffsetPower": cmDsCalOffsetPower,
       "cmDsCalChannelNumber": cmDsCalChannelNumber,
       "cmFactoryUpstreamCalibration": cmFactoryUpstreamCalibration,
       "cmUsCalFrequency": cmUsCalFrequency,
       "cmUsCalChannelWidth": cmUsCalChannelWidth,
       "cmUsCalModulation": cmUsCalModulation,
       "cmUsCalTxPower": cmUsCalTxPower,
       "cmUsCalZeroOffsets": cmUsCalZeroOffsets,
       "cmUsCalNumOffsets": cmUsCalNumOffsets,
       "cmUsCalOffsetTable": cmUsCalOffsetTable,
       "cmUsCalOffsetEntry": cmUsCalOffsetEntry,
       "cmUsCalOffsetIndex": cmUsCalOffsetIndex,
       "cmUsCalOffsetFrequency": cmUsCalOffsetFrequency,
       "cmUsCalOffsetPower": cmUsCalOffsetPower,
       "cmUsCalChannelNumber": cmUsCalChannelNumber,
       "cmFactoryHardware": cmFactoryHardware,
       "cmHwSTATHR": cmHwSTATHR,
       "cmHwSTAGI": cmHwSTAGI,
       "cmHwSTAGT": cmHwSTAGT,
       "cmHwAdvanceMapRunAheadEnable": cmHwAdvanceMapRunAheadEnable,
       "cmFactoryOtp": cmFactoryOtp,
       "cmOtpIsProgrammed": cmOtpIsProgrammed,
       "cmOtpProgramNow": cmOtpProgramNow,
       "cmOtpProgramResult": cmOtpProgramResult,
       "cmOtpRawBitsSize": cmOtpRawBitsSize,
       "cmOtpRawBits": cmOtpRawBits,
       "cmOtpCustomerDefinedBitsSize": cmOtpCustomerDefinedBitsSize,
       "cmOtpCustomerDefinedBits": cmOtpCustomerDefinedBits,
       "cmOtpSecurityLevel": cmOtpSecurityLevel,
       "cmOtpJtagDisabled": cmOtpJtagDisabled,
       "cmOtpConsoleDisabled": cmOtpConsoleDisabled,
       "cmOtpSpiSlaveDisabled": cmOtpSpiSlaveDisabled,
       "cmOtpMpiAccessControl": cmOtpMpiAccessControl,
       "cmOtpBootRomEnabled": cmOtpBootRomEnabled,
       "cmOtpRamScramblerEnabled": cmOtpRamScramblerEnabled,
       "cmFactoryFpm": cmFactoryFpm,
       "cmFpmTokenDepletionWatchdogEnable": cmFpmTokenDepletionWatchdogEnable}
)
