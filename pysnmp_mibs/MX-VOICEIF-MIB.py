# SNMP MIB module (MX-VOICEIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-VOICEIF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:12 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(mediatrixConfig,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixConfig")

(MxEnableState,
 MxFloatingPoint) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState",
    "MxFloatingPoint")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

voiceIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30)
)
if mibBuilder.loadTexts:
    voiceIfMIB.setRevisions(
        ("2009-08-31 00:00",
         "2009-04-06 00:00",
         "2009-04-01 00:00",
         "2009-02-11 00:00",
         "2008-11-07 00:00",
         "2008-04-08 00:00",
         "2007-10-10 00:00",
         "2007-07-04 00:00",
         "2006-03-06 00:00",
         "2005-07-18 00:00",
         "2005-03-17 00:00",
         "2004-05-25 00:00",
         "2004-04-13 00:00",
         "2003-11-10 00:00",
         "2003-08-12 00:00",
         "2003-08-06 00:00",
         "2003-07-24 00:00",
         "2003-07-21 00:00",
         "2003-06-20 00:00",
         "2003-05-21 00:00",
         "2003-05-01 00:00",
         "2003-04-01 00:00",
         "2003-02-11 00:00",
         "2003-01-16 00:00",
         "2002-12-19 00:00",
         "2002-09-16 00:00",
         "2002-08-30 00:00",
         "2002-08-12 00:00",
         "2002-07-31 00:00",
         "2002-06-06 00:00",
         "2002-04-26 00:00",
         "2002-01-11 00:00",
         "2001-08-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VoiceIfMIBObjects_ObjectIdentity = ObjectIdentity
voiceIfMIBObjects = _VoiceIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1)
)


class _VoiceIfAllowDtmfOobRecovery_Type(MxEnableState):
    """Custom type voiceIfAllowDtmfOobRecovery based on MxEnableState"""
    defaultValue = 0


_VoiceIfAllowDtmfOobRecovery_Type.__name__ = "MxEnableState"
_VoiceIfAllowDtmfOobRecovery_Object = MibScalar
voiceIfAllowDtmfOobRecovery = _VoiceIfAllowDtmfOobRecovery_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 5),
    _VoiceIfAllowDtmfOobRecovery_Type()
)
voiceIfAllowDtmfOobRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfAllowDtmfOobRecovery.setStatus("current")
_VoiceIfTable_Object = MibTable
voiceIfTable = _VoiceIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10)
)
if mibBuilder.loadTexts:
    voiceIfTable.setStatus("current")
_VoiceIfEntry_Object = MibTableRow
voiceIfEntry = _VoiceIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10, 1)
)
voiceIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voiceIfEntry.setStatus("current")


class _VoiceIfAdaptativeJitterBufferEnable_Type(Integer32):
    """Custom type voiceIfAdaptativeJitterBufferEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_VoiceIfAdaptativeJitterBufferEnable_Type.__name__ = "Integer32"
_VoiceIfAdaptativeJitterBufferEnable_Object = MibTableColumn
voiceIfAdaptativeJitterBufferEnable = _VoiceIfAdaptativeJitterBufferEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10, 1, 5),
    _VoiceIfAdaptativeJitterBufferEnable_Type()
)
voiceIfAdaptativeJitterBufferEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfAdaptativeJitterBufferEnable.setStatus("current")


class _VoiceIfTargetJitterBufferLength_Type(Unsigned32):
    """Custom type voiceIfTargetJitterBufferLength based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_VoiceIfTargetJitterBufferLength_Type.__name__ = "Unsigned32"
_VoiceIfTargetJitterBufferLength_Object = MibTableColumn
voiceIfTargetJitterBufferLength = _VoiceIfTargetJitterBufferLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10, 1, 6),
    _VoiceIfTargetJitterBufferLength_Type()
)
voiceIfTargetJitterBufferLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfTargetJitterBufferLength.setStatus("current")


class _VoiceIfMaxJitterBufferLength_Type(Unsigned32):
    """Custom type voiceIfMaxJitterBufferLength based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_VoiceIfMaxJitterBufferLength_Type.__name__ = "Unsigned32"
_VoiceIfMaxJitterBufferLength_Object = MibTableColumn
voiceIfMaxJitterBufferLength = _VoiceIfMaxJitterBufferLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10, 1, 7),
    _VoiceIfMaxJitterBufferLength_Type()
)
voiceIfMaxJitterBufferLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfMaxJitterBufferLength.setStatus("current")


class _VoiceIfG711VoiceActivityDetectionEnable_Type(Integer32):
    """Custom type voiceIfG711VoiceActivityDetectionEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("transparent", 1),
          ("conservative", 2))
    )


_VoiceIfG711VoiceActivityDetectionEnable_Type.__name__ = "Integer32"
_VoiceIfG711VoiceActivityDetectionEnable_Object = MibTableColumn
voiceIfG711VoiceActivityDetectionEnable = _VoiceIfG711VoiceActivityDetectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10, 1, 10),
    _VoiceIfG711VoiceActivityDetectionEnable_Type()
)
voiceIfG711VoiceActivityDetectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfG711VoiceActivityDetectionEnable.setStatus("current")


class _VoiceIfEchoCancellationEnable_Type(MxEnableState):
    """Custom type voiceIfEchoCancellationEnable based on MxEnableState"""
    defaultValue = 1


_VoiceIfEchoCancellationEnable_Type.__name__ = "MxEnableState"
_VoiceIfEchoCancellationEnable_Object = MibTableColumn
voiceIfEchoCancellationEnable = _VoiceIfEchoCancellationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10, 1, 11),
    _VoiceIfEchoCancellationEnable_Type()
)
voiceIfEchoCancellationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfEchoCancellationEnable.setStatus("current")


class _VoiceIfG711ComfortNoiseGenerationEnable_Type(Integer32):
    """Custom type voiceIfG711ComfortNoiseGenerationEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("whiteNoise", 1),
          ("customNoise", 2))
    )


_VoiceIfG711ComfortNoiseGenerationEnable_Type.__name__ = "Integer32"
_VoiceIfG711ComfortNoiseGenerationEnable_Object = MibTableColumn
voiceIfG711ComfortNoiseGenerationEnable = _VoiceIfG711ComfortNoiseGenerationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10, 1, 12),
    _VoiceIfG711ComfortNoiseGenerationEnable_Type()
)
voiceIfG711ComfortNoiseGenerationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfG711ComfortNoiseGenerationEnable.setStatus("current")


class _VoiceIfBaseGainConfigurationSource_Type(Integer32):
    """Custom type voiceIfBaseGainConfigurationSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("useCustomConfiguration", 0),
          ("useDefaultCountryConfiguration", 1))
    )


_VoiceIfBaseGainConfigurationSource_Type.__name__ = "Integer32"
_VoiceIfBaseGainConfigurationSource_Object = MibTableColumn
voiceIfBaseGainConfigurationSource = _VoiceIfBaseGainConfigurationSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10, 1, 17),
    _VoiceIfBaseGainConfigurationSource_Type()
)
voiceIfBaseGainConfigurationSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfBaseGainConfigurationSource.setStatus("deprecated")


class _VoiceIfUserInputGainOffset_Type(MxFloatingPoint):
    """Custom type voiceIfUserInputGainOffset based on MxFloatingPoint"""
    defaultValue = OctetString("0")


_VoiceIfUserInputGainOffset_Type.__name__ = "MxFloatingPoint"
_VoiceIfUserInputGainOffset_Object = MibTableColumn
voiceIfUserInputGainOffset = _VoiceIfUserInputGainOffset_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10, 1, 20),
    _VoiceIfUserInputGainOffset_Type()
)
voiceIfUserInputGainOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfUserInputGainOffset.setStatus("current")


class _VoiceIfUserOutputGainOffset_Type(MxFloatingPoint):
    """Custom type voiceIfUserOutputGainOffset based on MxFloatingPoint"""
    defaultValue = OctetString("0")


_VoiceIfUserOutputGainOffset_Type.__name__ = "MxFloatingPoint"
_VoiceIfUserOutputGainOffset_Object = MibTableColumn
voiceIfUserOutputGainOffset = _VoiceIfUserOutputGainOffset_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10, 1, 21),
    _VoiceIfUserOutputGainOffset_Type()
)
voiceIfUserOutputGainOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfUserOutputGainOffset.setStatus("current")


class _VoiceIfBaseInputGain_Type(Unsigned32):
    """Custom type voiceIfBaseInputGain based on Unsigned32"""
    defaultValue = 5785

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VoiceIfBaseInputGain_Type.__name__ = "Unsigned32"
_VoiceIfBaseInputGain_Object = MibTableColumn
voiceIfBaseInputGain = _VoiceIfBaseInputGain_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10, 1, 22),
    _VoiceIfBaseInputGain_Type()
)
voiceIfBaseInputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfBaseInputGain.setStatus("deprecated")


class _VoiceIfBaseOutputGain_Type(Unsigned32):
    """Custom type voiceIfBaseOutputGain based on Unsigned32"""
    defaultValue = 2052

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VoiceIfBaseOutputGain_Type.__name__ = "Unsigned32"
_VoiceIfBaseOutputGain_Object = MibTableColumn
voiceIfBaseOutputGain = _VoiceIfBaseOutputGain_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10, 1, 23),
    _VoiceIfBaseOutputGain_Type()
)
voiceIfBaseOutputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfBaseOutputGain.setStatus("deprecated")


class _VoiceIfBaseInputGainOffset_Type(MxFloatingPoint):
    """Custom type voiceIfBaseInputGainOffset based on MxFloatingPoint"""
    defaultValue = OctetString("0")


_VoiceIfBaseInputGainOffset_Type.__name__ = "MxFloatingPoint"
_VoiceIfBaseInputGainOffset_Object = MibTableColumn
voiceIfBaseInputGainOffset = _VoiceIfBaseInputGainOffset_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10, 1, 24),
    _VoiceIfBaseInputGainOffset_Type()
)
voiceIfBaseInputGainOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfBaseInputGainOffset.setStatus("deprecated")


class _VoiceIfBaseOutputGainOffset_Type(MxFloatingPoint):
    """Custom type voiceIfBaseOutputGainOffset based on MxFloatingPoint"""
    defaultValue = OctetString("0")


_VoiceIfBaseOutputGainOffset_Type.__name__ = "MxFloatingPoint"
_VoiceIfBaseOutputGainOffset_Object = MibTableColumn
voiceIfBaseOutputGainOffset = _VoiceIfBaseOutputGainOffset_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10, 1, 25),
    _VoiceIfBaseOutputGainOffset_Type()
)
voiceIfBaseOutputGainOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfBaseOutputGainOffset.setStatus("deprecated")


class _VoiceIfNlpThresholdLevel_Type(Unsigned32):
    """Custom type voiceIfNlpThresholdLevel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VoiceIfNlpThresholdLevel_Type.__name__ = "Unsigned32"
_VoiceIfNlpThresholdLevel_Object = MibTableColumn
voiceIfNlpThresholdLevel = _VoiceIfNlpThresholdLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10, 1, 35),
    _VoiceIfNlpThresholdLevel_Type()
)
voiceIfNlpThresholdLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfNlpThresholdLevel.setStatus("deprecated")


class _VoiceIfG729VoiceActivityDetectionEnable_Type(MxEnableState):
    """Custom type voiceIfG729VoiceActivityDetectionEnable based on MxEnableState"""
    defaultValue = 1


_VoiceIfG729VoiceActivityDetectionEnable_Type.__name__ = "MxEnableState"
_VoiceIfG729VoiceActivityDetectionEnable_Object = MibTableColumn
voiceIfG729VoiceActivityDetectionEnable = _VoiceIfG729VoiceActivityDetectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10, 1, 50),
    _VoiceIfG729VoiceActivityDetectionEnable_Type()
)
voiceIfG729VoiceActivityDetectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfG729VoiceActivityDetectionEnable.setStatus("current")


class _VoiceIfG723VoiceActivityDetectionEnable_Type(MxEnableState):
    """Custom type voiceIfG723VoiceActivityDetectionEnable based on MxEnableState"""
    defaultValue = 1


_VoiceIfG723VoiceActivityDetectionEnable_Type.__name__ = "MxEnableState"
_VoiceIfG723VoiceActivityDetectionEnable_Object = MibTableColumn
voiceIfG723VoiceActivityDetectionEnable = _VoiceIfG723VoiceActivityDetectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10, 1, 80),
    _VoiceIfG723VoiceActivityDetectionEnable_Type()
)
voiceIfG723VoiceActivityDetectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfG723VoiceActivityDetectionEnable.setStatus("current")


class _VoiceIfSignalLimiterLevel_Type(Integer32):
    """Custom type voiceIfSignalLimiterLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_VoiceIfSignalLimiterLevel_Type.__name__ = "Integer32"
_VoiceIfSignalLimiterLevel_Object = MibTableColumn
voiceIfSignalLimiterLevel = _VoiceIfSignalLimiterLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 10, 1, 90),
    _VoiceIfSignalLimiterLevel_Type()
)
voiceIfSignalLimiterLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfSignalLimiterLevel.setStatus("current")
_VoiceIfCodecTable_Object = MibTable
voiceIfCodecTable = _VoiceIfCodecTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20)
)
if mibBuilder.loadTexts:
    voiceIfCodecTable.setStatus("current")
_VoiceIfCodecEntry_Object = MibTableRow
voiceIfCodecEntry = _VoiceIfCodecEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1)
)
voiceIfCodecEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voiceIfCodecEntry.setStatus("current")


class _VoiceIfCodecPreferred_Type(Integer32):
    """Custom type voiceIfCodecPreferred based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("pcmu", 1),
          ("pcma", 2),
          ("g723", 3),
          ("g729", 4),
          ("g726-16kbps", 5),
          ("g726-24kbps", 6),
          ("g726-32kbps", 7),
          ("g726-40kbps", 8))
    )


_VoiceIfCodecPreferred_Type.__name__ = "Integer32"
_VoiceIfCodecPreferred_Object = MibTableColumn
voiceIfCodecPreferred = _VoiceIfCodecPreferred_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 1),
    _VoiceIfCodecPreferred_Type()
)
voiceIfCodecPreferred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecPreferred.setStatus("current")


class _VoiceIfCodecPcmuEnable_Type(Integer32):
    """Custom type voiceIfCodecPcmuEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_VoiceIfCodecPcmuEnable_Type.__name__ = "Integer32"
_VoiceIfCodecPcmuEnable_Object = MibTableColumn
voiceIfCodecPcmuEnable = _VoiceIfCodecPcmuEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 5),
    _VoiceIfCodecPcmuEnable_Type()
)
voiceIfCodecPcmuEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecPcmuEnable.setStatus("current")


class _VoiceIfCodecPcmuMinPTime_Type(Unsigned32):
    """Custom type voiceIfCodecPcmuMinPTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
    )


_VoiceIfCodecPcmuMinPTime_Type.__name__ = "Unsigned32"
_VoiceIfCodecPcmuMinPTime_Object = MibTableColumn
voiceIfCodecPcmuMinPTime = _VoiceIfCodecPcmuMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 6),
    _VoiceIfCodecPcmuMinPTime_Type()
)
voiceIfCodecPcmuMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecPcmuMinPTime.setStatus("current")


class _VoiceIfCodecPcmuMaxPTime_Type(Unsigned32):
    """Custom type voiceIfCodecPcmuMaxPTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
    )


_VoiceIfCodecPcmuMaxPTime_Type.__name__ = "Unsigned32"
_VoiceIfCodecPcmuMaxPTime_Object = MibTableColumn
voiceIfCodecPcmuMaxPTime = _VoiceIfCodecPcmuMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 7),
    _VoiceIfCodecPcmuMaxPTime_Type()
)
voiceIfCodecPcmuMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecPcmuMaxPTime.setStatus("current")


class _VoiceIfCodecPcmaEnable_Type(Integer32):
    """Custom type voiceIfCodecPcmaEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_VoiceIfCodecPcmaEnable_Type.__name__ = "Integer32"
_VoiceIfCodecPcmaEnable_Object = MibTableColumn
voiceIfCodecPcmaEnable = _VoiceIfCodecPcmaEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 11),
    _VoiceIfCodecPcmaEnable_Type()
)
voiceIfCodecPcmaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecPcmaEnable.setStatus("current")


class _VoiceIfCodecPcmaMinPTime_Type(Unsigned32):
    """Custom type voiceIfCodecPcmaMinPTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
    )


_VoiceIfCodecPcmaMinPTime_Type.__name__ = "Unsigned32"
_VoiceIfCodecPcmaMinPTime_Object = MibTableColumn
voiceIfCodecPcmaMinPTime = _VoiceIfCodecPcmaMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 12),
    _VoiceIfCodecPcmaMinPTime_Type()
)
voiceIfCodecPcmaMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecPcmaMinPTime.setStatus("current")


class _VoiceIfCodecPcmaMaxPTime_Type(Unsigned32):
    """Custom type voiceIfCodecPcmaMaxPTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
    )


_VoiceIfCodecPcmaMaxPTime_Type.__name__ = "Unsigned32"
_VoiceIfCodecPcmaMaxPTime_Object = MibTableColumn
voiceIfCodecPcmaMaxPTime = _VoiceIfCodecPcmaMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 13),
    _VoiceIfCodecPcmaMaxPTime_Type()
)
voiceIfCodecPcmaMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecPcmaMaxPTime.setStatus("current")


class _VoiceIfCodecG723Enable_Type(Integer32):
    """Custom type voiceIfCodecG723Enable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("g723-53kbs", 1),
          ("g723-63kbs", 2))
    )


_VoiceIfCodecG723Enable_Type.__name__ = "Integer32"
_VoiceIfCodecG723Enable_Object = MibTableColumn
voiceIfCodecG723Enable = _VoiceIfCodecG723Enable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 17),
    _VoiceIfCodecG723Enable_Type()
)
voiceIfCodecG723Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG723Enable.setStatus("current")


class _VoiceIfCodecG723MinPTime_Type(Unsigned32):
    """Custom type voiceIfCodecG723MinPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(120, 120),
    )


_VoiceIfCodecG723MinPTime_Type.__name__ = "Unsigned32"
_VoiceIfCodecG723MinPTime_Object = MibTableColumn
voiceIfCodecG723MinPTime = _VoiceIfCodecG723MinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 18),
    _VoiceIfCodecG723MinPTime_Type()
)
voiceIfCodecG723MinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG723MinPTime.setStatus("current")


class _VoiceIfCodecG723MaxPTime_Type(Unsigned32):
    """Custom type voiceIfCodecG723MaxPTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(120, 120),
    )


_VoiceIfCodecG723MaxPTime_Type.__name__ = "Unsigned32"
_VoiceIfCodecG723MaxPTime_Object = MibTableColumn
voiceIfCodecG723MaxPTime = _VoiceIfCodecG723MaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 19),
    _VoiceIfCodecG723MaxPTime_Type()
)
voiceIfCodecG723MaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG723MaxPTime.setStatus("current")


class _VoiceIfCodecG729Enable_Type(Integer32):
    """Custom type voiceIfCodecG729Enable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_VoiceIfCodecG729Enable_Type.__name__ = "Integer32"
_VoiceIfCodecG729Enable_Object = MibTableColumn
voiceIfCodecG729Enable = _VoiceIfCodecG729Enable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 23),
    _VoiceIfCodecG729Enable_Type()
)
voiceIfCodecG729Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG729Enable.setStatus("current")


class _VoiceIfCodecG729MinPTime_Type(Unsigned32):
    """Custom type voiceIfCodecG729MinPTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
    )


_VoiceIfCodecG729MinPTime_Type.__name__ = "Unsigned32"
_VoiceIfCodecG729MinPTime_Object = MibTableColumn
voiceIfCodecG729MinPTime = _VoiceIfCodecG729MinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 24),
    _VoiceIfCodecG729MinPTime_Type()
)
voiceIfCodecG729MinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG729MinPTime.setStatus("current")


class _VoiceIfCodecG729MaxPTime_Type(Unsigned32):
    """Custom type voiceIfCodecG729MaxPTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
    )


_VoiceIfCodecG729MaxPTime_Type.__name__ = "Unsigned32"
_VoiceIfCodecG729MaxPTime_Object = MibTableColumn
voiceIfCodecG729MaxPTime = _VoiceIfCodecG729MaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 25),
    _VoiceIfCodecG729MaxPTime_Type()
)
voiceIfCodecG729MaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG729MaxPTime.setStatus("current")


class _VoiceIfCodecG72616kbpsEnable_Type(Integer32):
    """Custom type voiceIfCodecG72616kbpsEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_VoiceIfCodecG72616kbpsEnable_Type.__name__ = "Integer32"
_VoiceIfCodecG72616kbpsEnable_Object = MibTableColumn
voiceIfCodecG72616kbpsEnable = _VoiceIfCodecG72616kbpsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 50),
    _VoiceIfCodecG72616kbpsEnable_Type()
)
voiceIfCodecG72616kbpsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG72616kbpsEnable.setStatus("current")


class _VoiceIfCodecG72616kbpsPayloadType_Type(Unsigned32):
    """Custom type voiceIfCodecG72616kbpsPayloadType based on Unsigned32"""
    defaultValue = 97

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_VoiceIfCodecG72616kbpsPayloadType_Type.__name__ = "Unsigned32"
_VoiceIfCodecG72616kbpsPayloadType_Object = MibTableColumn
voiceIfCodecG72616kbpsPayloadType = _VoiceIfCodecG72616kbpsPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 55),
    _VoiceIfCodecG72616kbpsPayloadType_Type()
)
voiceIfCodecG72616kbpsPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG72616kbpsPayloadType.setStatus("current")


class _VoiceIfCodecG72616kbpsMinPTime_Type(Unsigned32):
    """Custom type voiceIfCodecG72616kbpsMinPTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
    )


_VoiceIfCodecG72616kbpsMinPTime_Type.__name__ = "Unsigned32"
_VoiceIfCodecG72616kbpsMinPTime_Object = MibTableColumn
voiceIfCodecG72616kbpsMinPTime = _VoiceIfCodecG72616kbpsMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 60),
    _VoiceIfCodecG72616kbpsMinPTime_Type()
)
voiceIfCodecG72616kbpsMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG72616kbpsMinPTime.setStatus("current")


class _VoiceIfCodecG72616kbpsMaxPTime_Type(Unsigned32):
    """Custom type voiceIfCodecG72616kbpsMaxPTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
    )


_VoiceIfCodecG72616kbpsMaxPTime_Type.__name__ = "Unsigned32"
_VoiceIfCodecG72616kbpsMaxPTime_Object = MibTableColumn
voiceIfCodecG72616kbpsMaxPTime = _VoiceIfCodecG72616kbpsMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 65),
    _VoiceIfCodecG72616kbpsMaxPTime_Type()
)
voiceIfCodecG72616kbpsMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG72616kbpsMaxPTime.setStatus("current")


class _VoiceIfCodecG72624kbpsEnable_Type(Integer32):
    """Custom type voiceIfCodecG72624kbpsEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_VoiceIfCodecG72624kbpsEnable_Type.__name__ = "Integer32"
_VoiceIfCodecG72624kbpsEnable_Object = MibTableColumn
voiceIfCodecG72624kbpsEnable = _VoiceIfCodecG72624kbpsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 70),
    _VoiceIfCodecG72624kbpsEnable_Type()
)
voiceIfCodecG72624kbpsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG72624kbpsEnable.setStatus("current")


class _VoiceIfCodecG72624kbpsPayloadType_Type(Unsigned32):
    """Custom type voiceIfCodecG72624kbpsPayloadType based on Unsigned32"""
    defaultValue = 98

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_VoiceIfCodecG72624kbpsPayloadType_Type.__name__ = "Unsigned32"
_VoiceIfCodecG72624kbpsPayloadType_Object = MibTableColumn
voiceIfCodecG72624kbpsPayloadType = _VoiceIfCodecG72624kbpsPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 75),
    _VoiceIfCodecG72624kbpsPayloadType_Type()
)
voiceIfCodecG72624kbpsPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG72624kbpsPayloadType.setStatus("current")


class _VoiceIfCodecG72624kbpsMinPTime_Type(Unsigned32):
    """Custom type voiceIfCodecG72624kbpsMinPTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
    )


_VoiceIfCodecG72624kbpsMinPTime_Type.__name__ = "Unsigned32"
_VoiceIfCodecG72624kbpsMinPTime_Object = MibTableColumn
voiceIfCodecG72624kbpsMinPTime = _VoiceIfCodecG72624kbpsMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 80),
    _VoiceIfCodecG72624kbpsMinPTime_Type()
)
voiceIfCodecG72624kbpsMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG72624kbpsMinPTime.setStatus("current")


class _VoiceIfCodecG72624kbpsMaxPTime_Type(Unsigned32):
    """Custom type voiceIfCodecG72624kbpsMaxPTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
    )


_VoiceIfCodecG72624kbpsMaxPTime_Type.__name__ = "Unsigned32"
_VoiceIfCodecG72624kbpsMaxPTime_Object = MibTableColumn
voiceIfCodecG72624kbpsMaxPTime = _VoiceIfCodecG72624kbpsMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 85),
    _VoiceIfCodecG72624kbpsMaxPTime_Type()
)
voiceIfCodecG72624kbpsMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG72624kbpsMaxPTime.setStatus("current")


class _VoiceIfCodecG72632kbpsEnable_Type(Integer32):
    """Custom type voiceIfCodecG72632kbpsEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_VoiceIfCodecG72632kbpsEnable_Type.__name__ = "Integer32"
_VoiceIfCodecG72632kbpsEnable_Object = MibTableColumn
voiceIfCodecG72632kbpsEnable = _VoiceIfCodecG72632kbpsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 90),
    _VoiceIfCodecG72632kbpsEnable_Type()
)
voiceIfCodecG72632kbpsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG72632kbpsEnable.setStatus("current")


class _VoiceIfCodecG72632kbpsPayloadType_Type(Unsigned32):
    """Custom type voiceIfCodecG72632kbpsPayloadType based on Unsigned32"""
    defaultValue = 99

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_VoiceIfCodecG72632kbpsPayloadType_Type.__name__ = "Unsigned32"
_VoiceIfCodecG72632kbpsPayloadType_Object = MibTableColumn
voiceIfCodecG72632kbpsPayloadType = _VoiceIfCodecG72632kbpsPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 100),
    _VoiceIfCodecG72632kbpsPayloadType_Type()
)
voiceIfCodecG72632kbpsPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG72632kbpsPayloadType.setStatus("current")


class _VoiceIfCodecG72632kbpsMinPTime_Type(Unsigned32):
    """Custom type voiceIfCodecG72632kbpsMinPTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
    )


_VoiceIfCodecG72632kbpsMinPTime_Type.__name__ = "Unsigned32"
_VoiceIfCodecG72632kbpsMinPTime_Object = MibTableColumn
voiceIfCodecG72632kbpsMinPTime = _VoiceIfCodecG72632kbpsMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 105),
    _VoiceIfCodecG72632kbpsMinPTime_Type()
)
voiceIfCodecG72632kbpsMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG72632kbpsMinPTime.setStatus("current")


class _VoiceIfCodecG72632kbpsMaxPTime_Type(Unsigned32):
    """Custom type voiceIfCodecG72632kbpsMaxPTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
    )


_VoiceIfCodecG72632kbpsMaxPTime_Type.__name__ = "Unsigned32"
_VoiceIfCodecG72632kbpsMaxPTime_Object = MibTableColumn
voiceIfCodecG72632kbpsMaxPTime = _VoiceIfCodecG72632kbpsMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 110),
    _VoiceIfCodecG72632kbpsMaxPTime_Type()
)
voiceIfCodecG72632kbpsMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG72632kbpsMaxPTime.setStatus("current")


class _VoiceIfCodecG72640kbpsEnable_Type(Integer32):
    """Custom type voiceIfCodecG72640kbpsEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_VoiceIfCodecG72640kbpsEnable_Type.__name__ = "Integer32"
_VoiceIfCodecG72640kbpsEnable_Object = MibTableColumn
voiceIfCodecG72640kbpsEnable = _VoiceIfCodecG72640kbpsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 115),
    _VoiceIfCodecG72640kbpsEnable_Type()
)
voiceIfCodecG72640kbpsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG72640kbpsEnable.setStatus("current")


class _VoiceIfCodecG72640kbpsPayloadType_Type(Unsigned32):
    """Custom type voiceIfCodecG72640kbpsPayloadType based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_VoiceIfCodecG72640kbpsPayloadType_Type.__name__ = "Unsigned32"
_VoiceIfCodecG72640kbpsPayloadType_Object = MibTableColumn
voiceIfCodecG72640kbpsPayloadType = _VoiceIfCodecG72640kbpsPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 120),
    _VoiceIfCodecG72640kbpsPayloadType_Type()
)
voiceIfCodecG72640kbpsPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG72640kbpsPayloadType.setStatus("current")


class _VoiceIfCodecG72640kbpsMinPTime_Type(Unsigned32):
    """Custom type voiceIfCodecG72640kbpsMinPTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
    )


_VoiceIfCodecG72640kbpsMinPTime_Type.__name__ = "Unsigned32"
_VoiceIfCodecG72640kbpsMinPTime_Object = MibTableColumn
voiceIfCodecG72640kbpsMinPTime = _VoiceIfCodecG72640kbpsMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 125),
    _VoiceIfCodecG72640kbpsMinPTime_Type()
)
voiceIfCodecG72640kbpsMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG72640kbpsMinPTime.setStatus("current")


class _VoiceIfCodecG72640kbpsMaxPTime_Type(Unsigned32):
    """Custom type voiceIfCodecG72640kbpsMaxPTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
    )


_VoiceIfCodecG72640kbpsMaxPTime_Type.__name__ = "Unsigned32"
_VoiceIfCodecG72640kbpsMaxPTime_Object = MibTableColumn
voiceIfCodecG72640kbpsMaxPTime = _VoiceIfCodecG72640kbpsMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 20, 1, 130),
    _VoiceIfCodecG72640kbpsMaxPTime_Type()
)
voiceIfCodecG72640kbpsMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfCodecG72640kbpsMaxPTime.setStatus("current")
_VoiceIfDtmfTransportTable_Object = MibTable
voiceIfDtmfTransportTable = _VoiceIfDtmfTransportTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 30)
)
if mibBuilder.loadTexts:
    voiceIfDtmfTransportTable.setStatus("current")
_VoiceIfDtmfTransportEntry_Object = MibTableRow
voiceIfDtmfTransportEntry = _VoiceIfDtmfTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 30, 1)
)
voiceIfDtmfTransportEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voiceIfDtmfTransportEntry.setStatus("current")


class _VoiceIfDtmfTransport_Type(Integer32):
    """Custom type voiceIfDtmfTransport based on Integer32"""
    defaultValue = 0

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
        *(("inBand", 0),
          ("outOfBandUsingRtp", 1),
          ("outOfBandUsingSignalingProtocol", 2),
          ("signalingProtocolDependent", 3))
    )


_VoiceIfDtmfTransport_Type.__name__ = "Integer32"
_VoiceIfDtmfTransport_Object = MibTableColumn
voiceIfDtmfTransport = _VoiceIfDtmfTransport_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 30, 1, 1),
    _VoiceIfDtmfTransport_Type()
)
voiceIfDtmfTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfDtmfTransport.setStatus("current")


class _VoiceIfDtmfPayloadType_Type(Unsigned32):
    """Custom type voiceIfDtmfPayloadType based on Unsigned32"""
    defaultValue = 96

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_VoiceIfDtmfPayloadType_Type.__name__ = "Unsigned32"
_VoiceIfDtmfPayloadType_Object = MibTableColumn
voiceIfDtmfPayloadType = _VoiceIfDtmfPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 30, 1, 5),
    _VoiceIfDtmfPayloadType_Type()
)
voiceIfDtmfPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfDtmfPayloadType.setStatus("current")


class _VoiceIfDtmfEnforceDefaultEvents_Type(MxEnableState):
    """Custom type voiceIfDtmfEnforceDefaultEvents based on MxEnableState"""
    defaultValue = 1


_VoiceIfDtmfEnforceDefaultEvents_Type.__name__ = "MxEnableState"
_VoiceIfDtmfEnforceDefaultEvents_Object = MibTableColumn
voiceIfDtmfEnforceDefaultEvents = _VoiceIfDtmfEnforceDefaultEvents_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 30, 1, 55),
    _VoiceIfDtmfEnforceDefaultEvents_Type()
)
voiceIfDtmfEnforceDefaultEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfDtmfEnforceDefaultEvents.setStatus("current")
_VoiceIfDtmfDetectionTable_Object = MibTable
voiceIfDtmfDetectionTable = _VoiceIfDtmfDetectionTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 40)
)
if mibBuilder.loadTexts:
    voiceIfDtmfDetectionTable.setStatus("current")
_VoiceIfDtmfDetectionEntry_Object = MibTableRow
voiceIfDtmfDetectionEntry = _VoiceIfDtmfDetectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 40, 1)
)
voiceIfDtmfDetectionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voiceIfDtmfDetectionEntry.setStatus("current")


class _VoiceIfDtmfDetectionRiseTimeCriteria_Type(Integer32):
    """Custom type voiceIfDtmfDetectionRiseTimeCriteria based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("checkSr", 100),
          ("confirmSnr", 200))
    )


_VoiceIfDtmfDetectionRiseTimeCriteria_Type.__name__ = "Integer32"
_VoiceIfDtmfDetectionRiseTimeCriteria_Object = MibTableColumn
voiceIfDtmfDetectionRiseTimeCriteria = _VoiceIfDtmfDetectionRiseTimeCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 40, 1, 10),
    _VoiceIfDtmfDetectionRiseTimeCriteria_Type()
)
voiceIfDtmfDetectionRiseTimeCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfDtmfDetectionRiseTimeCriteria.setStatus("current")


class _VoiceIfDtmfDetectionMaxPowerThreshold_Type(Integer32):
    """Custom type voiceIfDtmfDetectionMaxPowerThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 1),
    )


_VoiceIfDtmfDetectionMaxPowerThreshold_Type.__name__ = "Integer32"
_VoiceIfDtmfDetectionMaxPowerThreshold_Object = MibTableColumn
voiceIfDtmfDetectionMaxPowerThreshold = _VoiceIfDtmfDetectionMaxPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 40, 1, 20),
    _VoiceIfDtmfDetectionMaxPowerThreshold_Type()
)
voiceIfDtmfDetectionMaxPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfDtmfDetectionMaxPowerThreshold.setStatus("current")


class _VoiceIfDtmfDetectionMinPowerThreshold_Type(Integer32):
    """Custom type voiceIfDtmfDetectionMinPowerThreshold based on Integer32"""
    defaultValue = -30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-45, -10),
    )


_VoiceIfDtmfDetectionMinPowerThreshold_Type.__name__ = "Integer32"
_VoiceIfDtmfDetectionMinPowerThreshold_Object = MibTableColumn
voiceIfDtmfDetectionMinPowerThreshold = _VoiceIfDtmfDetectionMinPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 40, 1, 30),
    _VoiceIfDtmfDetectionMinPowerThreshold_Type()
)
voiceIfDtmfDetectionMinPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfDtmfDetectionMinPowerThreshold.setStatus("current")


class _VoiceIfDtmfDetectionBreakPowerThreshold_Type(Integer32):
    """Custom type voiceIfDtmfDetectionBreakPowerThreshold based on Integer32"""
    defaultValue = -32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-45, -12),
    )


_VoiceIfDtmfDetectionBreakPowerThreshold_Type.__name__ = "Integer32"
_VoiceIfDtmfDetectionBreakPowerThreshold_Object = MibTableColumn
voiceIfDtmfDetectionBreakPowerThreshold = _VoiceIfDtmfDetectionBreakPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 40, 1, 40),
    _VoiceIfDtmfDetectionBreakPowerThreshold_Type()
)
voiceIfDtmfDetectionBreakPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfDtmfDetectionBreakPowerThreshold.setStatus("current")


class _VoiceIfDtmfDetectionPositiveTwist_Type(Unsigned32):
    """Custom type voiceIfDtmfDetectionPositiveTwist based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_VoiceIfDtmfDetectionPositiveTwist_Type.__name__ = "Unsigned32"
_VoiceIfDtmfDetectionPositiveTwist_Object = MibTableColumn
voiceIfDtmfDetectionPositiveTwist = _VoiceIfDtmfDetectionPositiveTwist_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 40, 1, 50),
    _VoiceIfDtmfDetectionPositiveTwist_Type()
)
voiceIfDtmfDetectionPositiveTwist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfDtmfDetectionPositiveTwist.setStatus("current")


class _VoiceIfDtmfDetectionNegativeTwist_Type(Unsigned32):
    """Custom type voiceIfDtmfDetectionNegativeTwist based on Unsigned32"""
    defaultValue = 9

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_VoiceIfDtmfDetectionNegativeTwist_Type.__name__ = "Unsigned32"
_VoiceIfDtmfDetectionNegativeTwist_Object = MibTableColumn
voiceIfDtmfDetectionNegativeTwist = _VoiceIfDtmfDetectionNegativeTwist_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 40, 1, 60),
    _VoiceIfDtmfDetectionNegativeTwist_Type()
)
voiceIfDtmfDetectionNegativeTwist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfDtmfDetectionNegativeTwist.setStatus("current")


class _VoiceIfDtmfDetectionMinDuration_Type(Unsigned32):
    """Custom type voiceIfDtmfDetectionMinDuration based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 5000),
    )


_VoiceIfDtmfDetectionMinDuration_Type.__name__ = "Unsigned32"
_VoiceIfDtmfDetectionMinDuration_Object = MibTableColumn
voiceIfDtmfDetectionMinDuration = _VoiceIfDtmfDetectionMinDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 1, 40, 1, 70),
    _VoiceIfDtmfDetectionMinDuration_Type()
)
voiceIfDtmfDetectionMinDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceIfDtmfDetectionMinDuration.setStatus("current")
_VoiceIfConformance_ObjectIdentity = ObjectIdentity
voiceIfConformance = _VoiceIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 2)
)
_VoiceIfCompliances_ObjectIdentity = ObjectIdentity
voiceIfCompliances = _VoiceIfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 2, 1)
)
_VoiceIfGroups_ObjectIdentity = ObjectIdentity
voiceIfGroups = _VoiceIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 2, 2)
)

# Managed Objects groups

voiceIfCodecGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 2, 2, 1)
)
voiceIfCodecGroupVer1.setObjects(
      *(("MX-VOICEIF-MIB", "voiceIfCodecPreferred"),
        ("MX-VOICEIF-MIB", "voiceIfCodecPcmuEnable"),
        ("MX-VOICEIF-MIB", "voiceIfCodecPcmuMinPTime"),
        ("MX-VOICEIF-MIB", "voiceIfCodecPcmuMaxPTime"),
        ("MX-VOICEIF-MIB", "voiceIfCodecPcmaEnable"),
        ("MX-VOICEIF-MIB", "voiceIfCodecPcmaMinPTime"),
        ("MX-VOICEIF-MIB", "voiceIfCodecPcmaMaxPTime"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG723Enable"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG723MinPTime"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG723MaxPTime"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG729Enable"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG729MinPTime"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG729MaxPTime"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG72616kbpsEnable"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG72616kbpsPayloadType"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG72616kbpsMinPTime"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG72616kbpsMaxPTime"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG72624kbpsEnable"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG72624kbpsPayloadType"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG72624kbpsMinPTime"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG72624kbpsMaxPTime"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG72632kbpsEnable"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG72632kbpsPayloadType"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG72632kbpsMinPTime"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG72632kbpsMaxPTime"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG72640kbpsEnable"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG72640kbpsPayloadType"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG72640kbpsMinPTime"),
        ("MX-VOICEIF-MIB", "voiceIfCodecG72640kbpsMaxPTime"))
)
if mibBuilder.loadTexts:
    voiceIfCodecGroupVer1.setStatus("current")

voiceIfBasicGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 2, 2, 2)
)
voiceIfBasicGroupVer1.setObjects(
      *(("MX-VOICEIF-MIB", "voiceIfAdaptativeJitterBufferEnable"),
        ("MX-VOICEIF-MIB", "voiceIfTargetJitterBufferLength"),
        ("MX-VOICEIF-MIB", "voiceIfMaxJitterBufferLength"),
        ("MX-VOICEIF-MIB", "voiceIfG711VoiceActivityDetectionEnable"),
        ("MX-VOICEIF-MIB", "voiceIfEchoCancellationEnable"),
        ("MX-VOICEIF-MIB", "voiceIfG711ComfortNoiseGenerationEnable"),
        ("MX-VOICEIF-MIB", "voiceIfBaseGainConfigurationSource"),
        ("MX-VOICEIF-MIB", "voiceIfUserInputGainOffset"),
        ("MX-VOICEIF-MIB", "voiceIfUserOutputGainOffset"),
        ("MX-VOICEIF-MIB", "voiceIfBaseInputGain"),
        ("MX-VOICEIF-MIB", "voiceIfBaseOutputGain"),
        ("MX-VOICEIF-MIB", "voiceIfBaseInputGainOffset"),
        ("MX-VOICEIF-MIB", "voiceIfBaseOutputGainOffset"),
        ("MX-VOICEIF-MIB", "voiceIfNlpThresholdLevel"),
        ("MX-VOICEIF-MIB", "voiceIfG729VoiceActivityDetectionEnable"),
        ("MX-VOICEIF-MIB", "voiceIfG723VoiceActivityDetectionEnable"),
        ("MX-VOICEIF-MIB", "voiceIfSignalLimiterLevel"))
)
if mibBuilder.loadTexts:
    voiceIfBasicGroupVer1.setStatus("current")

voiceIfDtmfTransportBasicGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 2, 2, 3)
)
voiceIfDtmfTransportBasicGroupVer1.setObjects(
      *(("MX-VOICEIF-MIB", "voiceIfDtmfTransport"),
        ("MX-VOICEIF-MIB", "voiceIfDtmfPayloadType"),
        ("MX-VOICEIF-MIB", "voiceIfDtmfEnforceDefaultEvents"))
)
if mibBuilder.loadTexts:
    voiceIfDtmfTransportBasicGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

voiceIfComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 30, 2, 1, 1)
)
voiceIfComplVer1.setObjects(
      *(("MX-VOICEIF-MIB", "voiceIfBasicGroupVer1"),
        ("MX-VOICEIF-MIB", "voiceIfCodecGroupVer1"),
        ("MX-VOICEIF-MIB", "voiceIfDtmfTransportBasicGroupVer1"))
)
if mibBuilder.loadTexts:
    voiceIfComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-VOICEIF-MIB",
    **{"voiceIfMIB": voiceIfMIB,
       "voiceIfMIBObjects": voiceIfMIBObjects,
       "voiceIfAllowDtmfOobRecovery": voiceIfAllowDtmfOobRecovery,
       "voiceIfTable": voiceIfTable,
       "voiceIfEntry": voiceIfEntry,
       "voiceIfAdaptativeJitterBufferEnable": voiceIfAdaptativeJitterBufferEnable,
       "voiceIfTargetJitterBufferLength": voiceIfTargetJitterBufferLength,
       "voiceIfMaxJitterBufferLength": voiceIfMaxJitterBufferLength,
       "voiceIfG711VoiceActivityDetectionEnable": voiceIfG711VoiceActivityDetectionEnable,
       "voiceIfEchoCancellationEnable": voiceIfEchoCancellationEnable,
       "voiceIfG711ComfortNoiseGenerationEnable": voiceIfG711ComfortNoiseGenerationEnable,
       "voiceIfBaseGainConfigurationSource": voiceIfBaseGainConfigurationSource,
       "voiceIfUserInputGainOffset": voiceIfUserInputGainOffset,
       "voiceIfUserOutputGainOffset": voiceIfUserOutputGainOffset,
       "voiceIfBaseInputGain": voiceIfBaseInputGain,
       "voiceIfBaseOutputGain": voiceIfBaseOutputGain,
       "voiceIfBaseInputGainOffset": voiceIfBaseInputGainOffset,
       "voiceIfBaseOutputGainOffset": voiceIfBaseOutputGainOffset,
       "voiceIfNlpThresholdLevel": voiceIfNlpThresholdLevel,
       "voiceIfG729VoiceActivityDetectionEnable": voiceIfG729VoiceActivityDetectionEnable,
       "voiceIfG723VoiceActivityDetectionEnable": voiceIfG723VoiceActivityDetectionEnable,
       "voiceIfSignalLimiterLevel": voiceIfSignalLimiterLevel,
       "voiceIfCodecTable": voiceIfCodecTable,
       "voiceIfCodecEntry": voiceIfCodecEntry,
       "voiceIfCodecPreferred": voiceIfCodecPreferred,
       "voiceIfCodecPcmuEnable": voiceIfCodecPcmuEnable,
       "voiceIfCodecPcmuMinPTime": voiceIfCodecPcmuMinPTime,
       "voiceIfCodecPcmuMaxPTime": voiceIfCodecPcmuMaxPTime,
       "voiceIfCodecPcmaEnable": voiceIfCodecPcmaEnable,
       "voiceIfCodecPcmaMinPTime": voiceIfCodecPcmaMinPTime,
       "voiceIfCodecPcmaMaxPTime": voiceIfCodecPcmaMaxPTime,
       "voiceIfCodecG723Enable": voiceIfCodecG723Enable,
       "voiceIfCodecG723MinPTime": voiceIfCodecG723MinPTime,
       "voiceIfCodecG723MaxPTime": voiceIfCodecG723MaxPTime,
       "voiceIfCodecG729Enable": voiceIfCodecG729Enable,
       "voiceIfCodecG729MinPTime": voiceIfCodecG729MinPTime,
       "voiceIfCodecG729MaxPTime": voiceIfCodecG729MaxPTime,
       "voiceIfCodecG72616kbpsEnable": voiceIfCodecG72616kbpsEnable,
       "voiceIfCodecG72616kbpsPayloadType": voiceIfCodecG72616kbpsPayloadType,
       "voiceIfCodecG72616kbpsMinPTime": voiceIfCodecG72616kbpsMinPTime,
       "voiceIfCodecG72616kbpsMaxPTime": voiceIfCodecG72616kbpsMaxPTime,
       "voiceIfCodecG72624kbpsEnable": voiceIfCodecG72624kbpsEnable,
       "voiceIfCodecG72624kbpsPayloadType": voiceIfCodecG72624kbpsPayloadType,
       "voiceIfCodecG72624kbpsMinPTime": voiceIfCodecG72624kbpsMinPTime,
       "voiceIfCodecG72624kbpsMaxPTime": voiceIfCodecG72624kbpsMaxPTime,
       "voiceIfCodecG72632kbpsEnable": voiceIfCodecG72632kbpsEnable,
       "voiceIfCodecG72632kbpsPayloadType": voiceIfCodecG72632kbpsPayloadType,
       "voiceIfCodecG72632kbpsMinPTime": voiceIfCodecG72632kbpsMinPTime,
       "voiceIfCodecG72632kbpsMaxPTime": voiceIfCodecG72632kbpsMaxPTime,
       "voiceIfCodecG72640kbpsEnable": voiceIfCodecG72640kbpsEnable,
       "voiceIfCodecG72640kbpsPayloadType": voiceIfCodecG72640kbpsPayloadType,
       "voiceIfCodecG72640kbpsMinPTime": voiceIfCodecG72640kbpsMinPTime,
       "voiceIfCodecG72640kbpsMaxPTime": voiceIfCodecG72640kbpsMaxPTime,
       "voiceIfDtmfTransportTable": voiceIfDtmfTransportTable,
       "voiceIfDtmfTransportEntry": voiceIfDtmfTransportEntry,
       "voiceIfDtmfTransport": voiceIfDtmfTransport,
       "voiceIfDtmfPayloadType": voiceIfDtmfPayloadType,
       "voiceIfDtmfEnforceDefaultEvents": voiceIfDtmfEnforceDefaultEvents,
       "voiceIfDtmfDetectionTable": voiceIfDtmfDetectionTable,
       "voiceIfDtmfDetectionEntry": voiceIfDtmfDetectionEntry,
       "voiceIfDtmfDetectionRiseTimeCriteria": voiceIfDtmfDetectionRiseTimeCriteria,
       "voiceIfDtmfDetectionMaxPowerThreshold": voiceIfDtmfDetectionMaxPowerThreshold,
       "voiceIfDtmfDetectionMinPowerThreshold": voiceIfDtmfDetectionMinPowerThreshold,
       "voiceIfDtmfDetectionBreakPowerThreshold": voiceIfDtmfDetectionBreakPowerThreshold,
       "voiceIfDtmfDetectionPositiveTwist": voiceIfDtmfDetectionPositiveTwist,
       "voiceIfDtmfDetectionNegativeTwist": voiceIfDtmfDetectionNegativeTwist,
       "voiceIfDtmfDetectionMinDuration": voiceIfDtmfDetectionMinDuration,
       "voiceIfConformance": voiceIfConformance,
       "voiceIfCompliances": voiceIfCompliances,
       "voiceIfComplVer1": voiceIfComplVer1,
       "voiceIfGroups": voiceIfGroups,
       "voiceIfCodecGroupVer1": voiceIfCodecGroupVer1,
       "voiceIfBasicGroupVer1": voiceIfBasicGroupVer1,
       "voiceIfDtmfTransportBasicGroupVer1": voiceIfDtmfTransportBasicGroupVer1}
)
