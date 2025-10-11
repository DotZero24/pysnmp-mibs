# SNMP MIB module (NEWTEC-DVBMODULATOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-DVBMODULATOR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:52 2025
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

(Float32TC,) = mibBuilder.importSymbols(
    "FLOAT-TC-MIB",
    "Float32TC")

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcAlarmState,
 NtcEnable) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState",
    "NtcEnable")

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

ntcDvbModulator = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000)
)
if mibBuilder.loadTexts:
    ntcDvbModulator.setRevisions(
        ("2017-07-10 12:00",
         "2016-12-05 12:00",
         "2016-05-17 09:00",
         "2015-09-25 11:00",
         "2015-02-19 09:00",
         "2015-01-30 08:00",
         "2014-09-09 09:00",
         "2014-09-04 12:00",
         "2014-07-15 08:00",
         "2014-02-03 12:00",
         "2013-10-28 10:00",
         "2013-07-05 06:00",
         "2013-05-22 06:00",
         "2013-03-27 10:00",
         "2013-01-08 12:00",
         "2012-06-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcDvbModObjects_ObjectIdentity = ObjectIdentity
ntcDvbModObjects = _NtcDvbModObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1)
)
if mibBuilder.loadTexts:
    ntcDvbModObjects.setStatus("current")


class _NtcDvbModMode_Type(Integer32):
    """Custom type ntcDvbModMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("dvbs", 0),
          ("dvbs2", 1),
          ("s2ext", 3),
          ("turbo", 4),
          ("amcdvbs", 5),
          ("amcnbc", 6),
          ("dvbs2x", 7),
          ("amcdl", 8))
    )


_NtcDvbModMode_Type.__name__ = "Integer32"
_NtcDvbModMode_Object = MibScalar
ntcDvbModMode = _NtcDvbModMode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 1),
    _NtcDvbModMode_Type()
)
ntcDvbModMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModMode.setStatus("current")


class _NtcDvbModTransmit_Type(NtcEnable):
    """Custom type ntcDvbModTransmit based on NtcEnable"""
    defaultValue = 0


_NtcDvbModTransmit_Type.__name__ = "NtcEnable"
_NtcDvbModTransmit_Object = MibScalar
ntcDvbModTransmit = _NtcDvbModTransmit_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 2),
    _NtcDvbModTransmit_Type()
)
ntcDvbModTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModTransmit.setStatus("current")


class _NtcDvbModTransmitState_Type(Integer32):
    """Custom type ntcDvbModTransmitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcDvbModTransmitState_Type.__name__ = "Integer32"
_NtcDvbModTransmitState_Object = MibScalar
ntcDvbModTransmitState = _NtcDvbModTransmitState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 3),
    _NtcDvbModTransmitState_Type()
)
ntcDvbModTransmitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModTransmitState.setStatus("current")


class _NtcDvbModTxCtrlGenDeviceAlarm_Type(Integer32):
    """Custom type ntcDvbModTxCtrlGenDeviceAlarm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disableTransmit", 0),
          ("noImpact", 1))
    )


_NtcDvbModTxCtrlGenDeviceAlarm_Type.__name__ = "Integer32"
_NtcDvbModTxCtrlGenDeviceAlarm_Object = MibScalar
ntcDvbModTxCtrlGenDeviceAlarm = _NtcDvbModTxCtrlGenDeviceAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 4),
    _NtcDvbModTxCtrlGenDeviceAlarm_Type()
)
ntcDvbModTxCtrlGenDeviceAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModTxCtrlGenDeviceAlarm.setStatus("current")


class _NtcDvbModTxCtrlGenInterfaceAlarm_Type(Integer32):
    """Custom type ntcDvbModTxCtrlGenInterfaceAlarm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disableTransmit", 0),
          ("noImpact", 1))
    )


_NtcDvbModTxCtrlGenInterfaceAlarm_Type.__name__ = "Integer32"
_NtcDvbModTxCtrlGenInterfaceAlarm_Object = MibScalar
ntcDvbModTxCtrlGenInterfaceAlarm = _NtcDvbModTxCtrlGenInterfaceAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 5),
    _NtcDvbModTxCtrlGenInterfaceAlarm_Type()
)
ntcDvbModTxCtrlGenInterfaceAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModTxCtrlGenInterfaceAlarm.setStatus("current")


class _NtcDvbModOutputFrequency_Type(Unsigned32):
    """Custom type ntcDvbModOutputFrequency based on Unsigned32"""
    defaultValue = 2000000000


_NtcDvbModOutputFrequency_Type.__name__ = "Unsigned32"
_NtcDvbModOutputFrequency_Object = MibScalar
ntcDvbModOutputFrequency = _NtcDvbModOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 6),
    _NtcDvbModOutputFrequency_Type()
)
ntcDvbModOutputFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModOutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModOutputFrequency.setUnits("Hz")


class _NtcDvbModRollOff_Type(Integer32):
    """Custom type ntcDvbModRollOff based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("rolloff2", 0),
          ("rolloff5", 1),
          ("rolloff10", 2),
          ("rolloff15", 3),
          ("rolloff20", 4),
          ("rolloff25", 5),
          ("rolloff35", 6))
    )


_NtcDvbModRollOff_Type.__name__ = "Integer32"
_NtcDvbModRollOff_Object = MibScalar
ntcDvbModRollOff = _NtcDvbModRollOff_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 7),
    _NtcDvbModRollOff_Type()
)
ntcDvbModRollOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModRollOff.setStatus("current")
_NtcDvbModOccupiedBandWidth_Type = Unsigned32
_NtcDvbModOccupiedBandWidth_Object = MibScalar
ntcDvbModOccupiedBandWidth = _NtcDvbModOccupiedBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 8),
    _NtcDvbModOccupiedBandWidth_Type()
)
ntcDvbModOccupiedBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModOccupiedBandWidth.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModOccupiedBandWidth.setUnits("Hz")


class _NtcDvbModOutputBand_Type(Integer32):
    """Custom type ntcDvbModOutputBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lBand", 0),
          ("ifBand", 1))
    )


_NtcDvbModOutputBand_Type.__name__ = "Integer32"
_NtcDvbModOutputBand_Object = MibScalar
ntcDvbModOutputBand = _NtcDvbModOutputBand_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 9),
    _NtcDvbModOutputBand_Type()
)
ntcDvbModOutputBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModOutputBand.setStatus("current")


class _NtcDvbModSpectrumPolarity_Type(Integer32):
    """Custom type ntcDvbModSpectrumPolarity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("directSpectrum", 1),
          ("invertedSpectrum", 2))
    )


_NtcDvbModSpectrumPolarity_Type.__name__ = "Integer32"
_NtcDvbModSpectrumPolarity_Object = MibScalar
ntcDvbModSpectrumPolarity = _NtcDvbModSpectrumPolarity_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 10),
    _NtcDvbModSpectrumPolarity_Type()
)
ntcDvbModSpectrumPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModSpectrumPolarity.setStatus("current")


class _NtcDvbModOutputLevel_Type(Integer32):
    """Custom type ntcDvbModOutputLevel based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 100),
    )


_NtcDvbModOutputLevel_Type.__name__ = "Integer32"
_NtcDvbModOutputLevel_Object = MibScalar
ntcDvbModOutputLevel = _NtcDvbModOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 11),
    _NtcDvbModOutputLevel_Type()
)
ntcDvbModOutputLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModOutputLevel.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModOutputLevel.setUnits("dBm")


class _NtcDvbModClockOutput_Type(Integer32):
    """Custom type ntcDvbModClockOutput based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("e10Mhz", 1))
    )


_NtcDvbModClockOutput_Type.__name__ = "Integer32"
_NtcDvbModClockOutput_Object = MibScalar
ntcDvbModClockOutput = _NtcDvbModClockOutput_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 12),
    _NtcDvbModClockOutput_Type()
)
ntcDvbModClockOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModClockOutput.setStatus("current")


class _NtcDvbModCarrierModulation_Type(Integer32):
    """Custom type ntcDvbModCarrierModulation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("purecarrier", 0),
          ("on", 1),
          ("testclkdiv4", 3),
          ("testclkdiv8", 4),
          ("testclkdiv16", 5),
          ("dvbcid", 6))
    )


_NtcDvbModCarrierModulation_Type.__name__ = "Integer32"
_NtcDvbModCarrierModulation_Object = MibScalar
ntcDvbModCarrierModulation = _NtcDvbModCarrierModulation_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 13),
    _NtcDvbModCarrierModulation_Type()
)
ntcDvbModCarrierModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModCarrierModulation.setStatus("current")


class _NtcDvbModAmplSlopeEqualizer_Type(Integer32):
    """Custom type ntcDvbModAmplSlopeEqualizer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7, 7),
    )


_NtcDvbModAmplSlopeEqualizer_Type.__name__ = "Integer32"
_NtcDvbModAmplSlopeEqualizer_Object = MibScalar
ntcDvbModAmplSlopeEqualizer = _NtcDvbModAmplSlopeEqualizer_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 14),
    _NtcDvbModAmplSlopeEqualizer_Type()
)
ntcDvbModAmplSlopeEqualizer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAmplSlopeEqualizer.setStatus("current")
_NtcDvbModDvbs2Acm_ObjectIdentity = ObjectIdentity
ntcDvbModDvbs2Acm = _NtcDvbModDvbs2Acm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 15)
)
if mibBuilder.loadTexts:
    ntcDvbModDvbs2Acm.setStatus("current")


class _NtcDvbModDvbs2AcmSymbolRate_Type(Unsigned32):
    """Custom type ntcDvbModDvbs2AcmSymbolRate based on Unsigned32"""
    defaultValue = 10000000


_NtcDvbModDvbs2AcmSymbolRate_Type.__name__ = "Unsigned32"
_NtcDvbModDvbs2AcmSymbolRate_Object = MibScalar
ntcDvbModDvbs2AcmSymbolRate = _NtcDvbModDvbs2AcmSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 15, 1),
    _NtcDvbModDvbs2AcmSymbolRate_Type()
)
ntcDvbModDvbs2AcmSymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2AcmSymbolRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2AcmSymbolRate.setUnits("baud")
_NtcDvbModDvbs2_ObjectIdentity = ObjectIdentity
ntcDvbModDvbs2 = _NtcDvbModDvbs2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 16)
)
if mibBuilder.loadTexts:
    ntcDvbModDvbs2.setStatus("current")


class _NtcDvbModDvbs2Isi_Type(Unsigned32):
    """Custom type ntcDvbModDvbs2Isi based on Unsigned32"""
    defaultValue = 171

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NtcDvbModDvbs2Isi_Type.__name__ = "Unsigned32"
_NtcDvbModDvbs2Isi_Object = MibScalar
ntcDvbModDvbs2Isi = _NtcDvbModDvbs2Isi_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 16, 1),
    _NtcDvbModDvbs2Isi_Type()
)
ntcDvbModDvbs2Isi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2Isi.setStatus("deprecated")


class _NtcDvbModDvbs2FrameType_Type(Integer32):
    """Custom type ntcDvbModDvbs2FrameType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("short", 0),
          ("normal", 1))
    )


_NtcDvbModDvbs2FrameType_Type.__name__ = "Integer32"
_NtcDvbModDvbs2FrameType_Object = MibScalar
ntcDvbModDvbs2FrameType = _NtcDvbModDvbs2FrameType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 16, 2),
    _NtcDvbModDvbs2FrameType_Type()
)
ntcDvbModDvbs2FrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2FrameType.setStatus("current")


class _NtcDvbModDvbs2ModCod_Type(Integer32):
    """Custom type ntcDvbModDvbs2ModCod based on Integer32"""
    defaultValue = 7

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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80)
        )
    )
    namedValues = NamedValues(
        *(("qpsk14", 1),
          ("qpsk13", 2),
          ("qpsk25", 3),
          ("qpsk12", 4),
          ("qpsk35", 5),
          ("qpsk23", 6),
          ("qpsk34", 7),
          ("qpsk45", 8),
          ("qpsk56", 9),
          ("qpsk89", 10),
          ("qpsk910", 11),
          ("e8psk35", 12),
          ("e8psk23", 13),
          ("e8psk34", 14),
          ("e8psk56", 15),
          ("e8psk89", 16),
          ("e8psk910", 17),
          ("e16apsk23", 18),
          ("e16apsk34", 19),
          ("e16apsk45", 20),
          ("e16apsk56", 21),
          ("e16apsk89", 22),
          ("e16apsk910", 23),
          ("e32apsk34", 24),
          ("e32apsk45", 25),
          ("e32apsk56", 26),
          ("e32apsk89", 27),
          ("e32apsk910", 28),
          ("qpsk1345", 29),
          ("qpsk920", 30),
          ("qpsk1120", 31),
          ("e8apsk59l", 32),
          ("e8apsk2645l", 33),
          ("e8psk2336", 34),
          ("e8psk2536", 35),
          ("e8psk1318", 36),
          ("e16apsk12l", 37),
          ("e16apsk815l", 38),
          ("e16apsk59l", 39),
          ("e16apsk2645", 40),
          ("e16apsk35", 41),
          ("e16apsk35l", 42),
          ("e16apsk2845", 43),
          ("e16apsk2336", 44),
          ("e16apsk23l", 45),
          ("e16apsk2536", 46),
          ("e16apsk1318", 47),
          ("e16apsk79", 48),
          ("e16apsk7790", 49),
          ("e32apsk23l", 50),
          ("e32apsk3245", 51),
          ("e32apsk1115", 52),
          ("e32apsk79", 53),
          ("e64apsk3245l", 54),
          ("e64apsk1115", 55),
          ("e64apsk79", 56),
          ("e64apsk45", 57),
          ("e64apsk56", 58),
          ("e128apsk34", 59),
          ("e128apsk79", 60),
          ("e256apsk2945l", 61),
          ("e256apsk23l", 62),
          ("e256apsk3145l", 63),
          ("e256apsk3245", 64),
          ("e256apsk1115l", 65),
          ("e256apsk34", 66),
          ("qpsk1145", 67),
          ("qpsk415", 68),
          ("qpsk1445", 69),
          ("qpsk715", 70),
          ("qpsk815", 71),
          ("qpsk3245", 72),
          ("e8psk715", 73),
          ("e8psk815", 74),
          ("e8psk2645", 75),
          ("e8psk3245", 76),
          ("e16apsk715", 77),
          ("e16apsk815", 78),
          ("e16apsk3245", 79),
          ("e32apsk23", 80))
    )


_NtcDvbModDvbs2ModCod_Type.__name__ = "Integer32"
_NtcDvbModDvbs2ModCod_Object = MibScalar
ntcDvbModDvbs2ModCod = _NtcDvbModDvbs2ModCod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 16, 3),
    _NtcDvbModDvbs2ModCod_Type()
)
ntcDvbModDvbs2ModCod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2ModCod.setStatus("current")


class _NtcDvbModDvbs2Pilots_Type(NtcEnable):
    """Custom type ntcDvbModDvbs2Pilots based on NtcEnable"""
    defaultValue = 0


_NtcDvbModDvbs2Pilots_Type.__name__ = "NtcEnable"
_NtcDvbModDvbs2Pilots_Object = MibScalar
ntcDvbModDvbs2Pilots = _NtcDvbModDvbs2Pilots_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 16, 4),
    _NtcDvbModDvbs2Pilots_Type()
)
ntcDvbModDvbs2Pilots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2Pilots.setStatus("current")


class _NtcDvbModDvbs2RatePriority_Type(Integer32):
    """Custom type ntcDvbModDvbs2RatePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("symbolrate", 0),
          ("bitrate", 1))
    )


_NtcDvbModDvbs2RatePriority_Type.__name__ = "Integer32"
_NtcDvbModDvbs2RatePriority_Object = MibScalar
ntcDvbModDvbs2RatePriority = _NtcDvbModDvbs2RatePriority_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 16, 5),
    _NtcDvbModDvbs2RatePriority_Type()
)
ntcDvbModDvbs2RatePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2RatePriority.setStatus("deprecated")


class _NtcDvbModDvbs2SymbolRate_Type(Unsigned32):
    """Custom type ntcDvbModDvbs2SymbolRate based on Unsigned32"""
    defaultValue = 10000000


_NtcDvbModDvbs2SymbolRate_Type.__name__ = "Unsigned32"
_NtcDvbModDvbs2SymbolRate_Object = MibScalar
ntcDvbModDvbs2SymbolRate = _NtcDvbModDvbs2SymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 16, 6),
    _NtcDvbModDvbs2SymbolRate_Type()
)
ntcDvbModDvbs2SymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2SymbolRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2SymbolRate.setUnits("baud")


class _NtcDvbModDvbs2BitRate_Type(Unsigned32):
    """Custom type ntcDvbModDvbs2BitRate based on Unsigned32"""
    defaultValue = 5000000


_NtcDvbModDvbs2BitRate_Type.__name__ = "Unsigned32"
_NtcDvbModDvbs2BitRate_Object = MibScalar
ntcDvbModDvbs2BitRate = _NtcDvbModDvbs2BitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 16, 7),
    _NtcDvbModDvbs2BitRate_Type()
)
ntcDvbModDvbs2BitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2BitRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2BitRate.setUnits("bps")
_NtcDvbModDvbs2MeasuredPktCount_Type = Counter32
_NtcDvbModDvbs2MeasuredPktCount_Object = MibScalar
ntcDvbModDvbs2MeasuredPktCount = _NtcDvbModDvbs2MeasuredPktCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 16, 8),
    _NtcDvbModDvbs2MeasuredPktCount_Type()
)
ntcDvbModDvbs2MeasuredPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2MeasuredPktCount.setStatus("deprecated")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2MeasuredPktCount.setUnits("packets")
_NtcDvbModDvbs2MeasuredBitRate_Type = Unsigned32
_NtcDvbModDvbs2MeasuredBitRate_Object = MibScalar
ntcDvbModDvbs2MeasuredBitRate = _NtcDvbModDvbs2MeasuredBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 16, 9),
    _NtcDvbModDvbs2MeasuredBitRate_Type()
)
ntcDvbModDvbs2MeasuredBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2MeasuredBitRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2MeasuredBitRate.setUnits("bps")


class _NtcDvbModDvbs2PhyLayerEfficiency_Type(Integer32):
    """Custom type ntcDvbModDvbs2PhyLayerEfficiency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_NtcDvbModDvbs2PhyLayerEfficiency_Type.__name__ = "Integer32"
_NtcDvbModDvbs2PhyLayerEfficiency_Object = MibScalar
ntcDvbModDvbs2PhyLayerEfficiency = _NtcDvbModDvbs2PhyLayerEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 16, 10),
    _NtcDvbModDvbs2PhyLayerEfficiency_Type()
)
ntcDvbModDvbs2PhyLayerEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2PhyLayerEfficiency.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2PhyLayerEfficiency.setUnits("%")


class _NtcDvbModDvbs2BbLayerEfficiency_Type(Integer32):
    """Custom type ntcDvbModDvbs2BbLayerEfficiency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_NtcDvbModDvbs2BbLayerEfficiency_Type.__name__ = "Integer32"
_NtcDvbModDvbs2BbLayerEfficiency_Object = MibScalar
ntcDvbModDvbs2BbLayerEfficiency = _NtcDvbModDvbs2BbLayerEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 16, 11),
    _NtcDvbModDvbs2BbLayerEfficiency_Type()
)
ntcDvbModDvbs2BbLayerEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2BbLayerEfficiency.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2BbLayerEfficiency.setUnits("%")


class _NtcDvbModDvbs2DumPlScramblMode_Type(Integer32):
    """Custom type ntcDvbModDvbs2DumPlScramblMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dvbs2standard", 0),
          ("continuous", 1))
    )


_NtcDvbModDvbs2DumPlScramblMode_Type.__name__ = "Integer32"
_NtcDvbModDvbs2DumPlScramblMode_Object = MibScalar
ntcDvbModDvbs2DumPlScramblMode = _NtcDvbModDvbs2DumPlScramblMode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 16, 12),
    _NtcDvbModDvbs2DumPlScramblMode_Type()
)
ntcDvbModDvbs2DumPlScramblMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2DumPlScramblMode.setStatus("current")


class _NtcDvbModDvbs2PlScrambSig_Type(Unsigned32):
    """Custom type ntcDvbModDvbs2PlScrambSig based on Unsigned32"""
    defaultValue = 0


_NtcDvbModDvbs2PlScrambSig_Type.__name__ = "Unsigned32"
_NtcDvbModDvbs2PlScrambSig_Object = MibScalar
ntcDvbModDvbs2PlScrambSig = _NtcDvbModDvbs2PlScrambSig_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 16, 13),
    _NtcDvbModDvbs2PlScrambSig_Type()
)
ntcDvbModDvbs2PlScrambSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2PlScrambSig.setStatus("current")


class _NtcDvbModDvbs2Reset_Type(Integer32):
    """Custom type ntcDvbModDvbs2Reset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("counting", 0),
          ("reset", 1))
    )


_NtcDvbModDvbs2Reset_Type.__name__ = "Integer32"
_NtcDvbModDvbs2Reset_Object = MibScalar
ntcDvbModDvbs2Reset = _NtcDvbModDvbs2Reset_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 16, 14),
    _NtcDvbModDvbs2Reset_Type()
)
ntcDvbModDvbs2Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2Reset.setStatus("deprecated")


class _NtcDvbModDvbs2RollOffSignalling_Type(Integer32):
    """Custom type ntcDvbModDvbs2RollOffSignalling based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("standard", 0),
          ("reserved", 1))
    )


_NtcDvbModDvbs2RollOffSignalling_Type.__name__ = "Integer32"
_NtcDvbModDvbs2RollOffSignalling_Object = MibScalar
ntcDvbModDvbs2RollOffSignalling = _NtcDvbModDvbs2RollOffSignalling_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 16, 15),
    _NtcDvbModDvbs2RollOffSignalling_Type()
)
ntcDvbModDvbs2RollOffSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDvbs2RollOffSignalling.setStatus("current")
_NtcDvbModDvbs_ObjectIdentity = ObjectIdentity
ntcDvbModDvbs = _NtcDvbModDvbs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 17)
)
if mibBuilder.loadTexts:
    ntcDvbModDvbs.setStatus("current")


class _NtcDvbModDvbsModCod_Type(Integer32):
    """Custom type ntcDvbModDvbsModCod based on Integer32"""
    defaultValue = 3

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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("qpsk12", 1),
          ("qpsk23", 2),
          ("qpsk34", 3),
          ("qpsk56", 4),
          ("qpsk67", 5),
          ("qpsk78", 6),
          ("e8psk23", 7),
          ("e8psk56", 8),
          ("e8psk89", 9),
          ("e16qam34", 10),
          ("e16qam78", 11))
    )


_NtcDvbModDvbsModCod_Type.__name__ = "Integer32"
_NtcDvbModDvbsModCod_Object = MibScalar
ntcDvbModDvbsModCod = _NtcDvbModDvbsModCod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 17, 1),
    _NtcDvbModDvbsModCod_Type()
)
ntcDvbModDvbsModCod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDvbsModCod.setStatus("current")


class _NtcDvbModDvbsRatePriority_Type(Integer32):
    """Custom type ntcDvbModDvbsRatePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("symbolrate", 0),
          ("bitrate", 1))
    )


_NtcDvbModDvbsRatePriority_Type.__name__ = "Integer32"
_NtcDvbModDvbsRatePriority_Object = MibScalar
ntcDvbModDvbsRatePriority = _NtcDvbModDvbsRatePriority_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 17, 2),
    _NtcDvbModDvbsRatePriority_Type()
)
ntcDvbModDvbsRatePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDvbsRatePriority.setStatus("deprecated")


class _NtcDvbModDvbsSymbolRate_Type(Unsigned32):
    """Custom type ntcDvbModDvbsSymbolRate based on Unsigned32"""
    defaultValue = 10000000


_NtcDvbModDvbsSymbolRate_Type.__name__ = "Unsigned32"
_NtcDvbModDvbsSymbolRate_Object = MibScalar
ntcDvbModDvbsSymbolRate = _NtcDvbModDvbsSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 17, 3),
    _NtcDvbModDvbsSymbolRate_Type()
)
ntcDvbModDvbsSymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDvbsSymbolRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    ntcDvbModDvbsSymbolRate.setUnits("baud")


class _NtcDvbModDvbsBitRate_Type(Unsigned32):
    """Custom type ntcDvbModDvbsBitRate based on Unsigned32"""
    defaultValue = 5000000


_NtcDvbModDvbsBitRate_Type.__name__ = "Unsigned32"
_NtcDvbModDvbsBitRate_Object = MibScalar
ntcDvbModDvbsBitRate = _NtcDvbModDvbsBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 17, 4),
    _NtcDvbModDvbsBitRate_Type()
)
ntcDvbModDvbsBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDvbsBitRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    ntcDvbModDvbsBitRate.setUnits("bps")
_NtcDvbModDvbsMeasuredPktCount_Type = Counter32
_NtcDvbModDvbsMeasuredPktCount_Object = MibScalar
ntcDvbModDvbsMeasuredPktCount = _NtcDvbModDvbsMeasuredPktCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 17, 5),
    _NtcDvbModDvbsMeasuredPktCount_Type()
)
ntcDvbModDvbsMeasuredPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModDvbsMeasuredPktCount.setStatus("deprecated")
if mibBuilder.loadTexts:
    ntcDvbModDvbsMeasuredPktCount.setUnits("packets")
_NtcDvbModDvbsMeasuredBitRate_Type = Unsigned32
_NtcDvbModDvbsMeasuredBitRate_Object = MibScalar
ntcDvbModDvbsMeasuredBitRate = _NtcDvbModDvbsMeasuredBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 17, 6),
    _NtcDvbModDvbsMeasuredBitRate_Type()
)
ntcDvbModDvbsMeasuredBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModDvbsMeasuredBitRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    ntcDvbModDvbsMeasuredBitRate.setUnits("bps")


class _NtcDvbModDvbsReset_Type(Integer32):
    """Custom type ntcDvbModDvbsReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("counting", 0),
          ("reset", 1))
    )


_NtcDvbModDvbsReset_Type.__name__ = "Integer32"
_NtcDvbModDvbsReset_Object = MibScalar
ntcDvbModDvbsReset = _NtcDvbModDvbsReset_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 17, 7),
    _NtcDvbModDvbsReset_Type()
)
ntcDvbModDvbsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDvbsReset.setStatus("deprecated")
_NtcDvbModEqualink_ObjectIdentity = ObjectIdentity
ntcDvbModEqualink = _NtcDvbModEqualink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 18)
)
if mibBuilder.loadTexts:
    ntcDvbModEqualink.setStatus("current")
_NtcDvbModEqlnkLinear_ObjectIdentity = ObjectIdentity
ntcDvbModEqlnkLinear = _NtcDvbModEqlnkLinear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 18, 1)
)
if mibBuilder.loadTexts:
    ntcDvbModEqlnkLinear.setStatus("current")


class _NtcDvbModEqlnkLinMode_Type(NtcEnable):
    """Custom type ntcDvbModEqlnkLinMode based on NtcEnable"""
    defaultValue = 0


_NtcDvbModEqlnkLinMode_Type.__name__ = "NtcEnable"
_NtcDvbModEqlnkLinMode_Object = MibScalar
ntcDvbModEqlnkLinMode = _NtcDvbModEqlnkLinMode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 18, 1, 1),
    _NtcDvbModEqlnkLinMode_Type()
)
ntcDvbModEqlnkLinMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModEqlnkLinMode.setStatus("current")


class _NtcDvbModEqlnkLinState_Type(Integer32):
    """Custom type ntcDvbModEqlnkLinState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcDvbModEqlnkLinState_Type.__name__ = "Integer32"
_NtcDvbModEqlnkLinState_Object = MibScalar
ntcDvbModEqlnkLinState = _NtcDvbModEqlnkLinState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 18, 1, 2),
    _NtcDvbModEqlnkLinState_Type()
)
ntcDvbModEqlnkLinState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModEqlnkLinState.setStatus("current")


class _NtcDvbModEqlnkLinInfo_Type(DisplayString):
    """Custom type ntcDvbModEqlnkLinInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_NtcDvbModEqlnkLinInfo_Type.__name__ = "DisplayString"
_NtcDvbModEqlnkLinInfo_Object = MibScalar
ntcDvbModEqlnkLinInfo = _NtcDvbModEqlnkLinInfo_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 18, 1, 3),
    _NtcDvbModEqlnkLinInfo_Type()
)
ntcDvbModEqlnkLinInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModEqlnkLinInfo.setStatus("current")
_NtcDvbModEqlnkLinConf_ObjectIdentity = ObjectIdentity
ntcDvbModEqlnkLinConf = _NtcDvbModEqlnkLinConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 18, 1, 4)
)
if mibBuilder.loadTexts:
    ntcDvbModEqlnkLinConf.setStatus("current")
_NtcDvbModEqlnkLinApp_ObjectIdentity = ObjectIdentity
ntcDvbModEqlnkLinApp = _NtcDvbModEqlnkLinApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 18, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ntcDvbModEqlnkLinApp.setStatus("current")


class _NtcDvbModEqlnkLinAppOutFreq_Type(Unsigned32):
    """Custom type ntcDvbModEqlnkLinAppOutFreq based on Unsigned32"""
    defaultValue = 1450000000


_NtcDvbModEqlnkLinAppOutFreq_Type.__name__ = "Unsigned32"
_NtcDvbModEqlnkLinAppOutFreq_Object = MibScalar
ntcDvbModEqlnkLinAppOutFreq = _NtcDvbModEqlnkLinAppOutFreq_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 18, 1, 4, 1, 1),
    _NtcDvbModEqlnkLinAppOutFreq_Type()
)
ntcDvbModEqlnkLinAppOutFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModEqlnkLinAppOutFreq.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModEqlnkLinAppOutFreq.setUnits("Hz")


class _NtcDvbModEqlnkLinAppRollOff_Type(Integer32):
    """Custom type ntcDvbModEqlnkLinAppRollOff based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("rolloff2", 0),
          ("rolloff5", 1),
          ("rolloff10", 2),
          ("rolloff15", 3),
          ("rolloff20", 4),
          ("rolloff25", 5),
          ("rolloff35", 6))
    )


_NtcDvbModEqlnkLinAppRollOff_Type.__name__ = "Integer32"
_NtcDvbModEqlnkLinAppRollOff_Object = MibScalar
ntcDvbModEqlnkLinAppRollOff = _NtcDvbModEqlnkLinAppRollOff_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 18, 1, 4, 1, 2),
    _NtcDvbModEqlnkLinAppRollOff_Type()
)
ntcDvbModEqlnkLinAppRollOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModEqlnkLinAppRollOff.setStatus("current")


class _NtcDvbModEqlnkLinAppSymRate_Type(Unsigned32):
    """Custom type ntcDvbModEqlnkLinAppSymRate based on Unsigned32"""
    defaultValue = 5000000


_NtcDvbModEqlnkLinAppSymRate_Type.__name__ = "Unsigned32"
_NtcDvbModEqlnkLinAppSymRate_Object = MibScalar
ntcDvbModEqlnkLinAppSymRate = _NtcDvbModEqlnkLinAppSymRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 18, 1, 4, 1, 3),
    _NtcDvbModEqlnkLinAppSymRate_Type()
)
ntcDvbModEqlnkLinAppSymRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModEqlnkLinAppSymRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModEqlnkLinAppSymRate.setUnits("baud")
_NtcDvbModEqlnkNonlinear_ObjectIdentity = ObjectIdentity
ntcDvbModEqlnkNonlinear = _NtcDvbModEqlnkNonlinear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 18, 2)
)
if mibBuilder.loadTexts:
    ntcDvbModEqlnkNonlinear.setStatus("current")


class _NtcDvbModEqlnkNonlinMode_Type(NtcEnable):
    """Custom type ntcDvbModEqlnkNonlinMode based on NtcEnable"""
    defaultValue = 0


_NtcDvbModEqlnkNonlinMode_Type.__name__ = "NtcEnable"
_NtcDvbModEqlnkNonlinMode_Object = MibScalar
ntcDvbModEqlnkNonlinMode = _NtcDvbModEqlnkNonlinMode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 18, 2, 1),
    _NtcDvbModEqlnkNonlinMode_Type()
)
ntcDvbModEqlnkNonlinMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModEqlnkNonlinMode.setStatus("current")


class _NtcDvbModEqlnkNonlinState_Type(Integer32):
    """Custom type ntcDvbModEqlnkNonlinState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcDvbModEqlnkNonlinState_Type.__name__ = "Integer32"
_NtcDvbModEqlnkNonlinState_Object = MibScalar
ntcDvbModEqlnkNonlinState = _NtcDvbModEqlnkNonlinState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 18, 2, 2),
    _NtcDvbModEqlnkNonlinState_Type()
)
ntcDvbModEqlnkNonlinState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModEqlnkNonlinState.setStatus("current")


class _NtcDvbModEqlnkNonlinInfo_Type(DisplayString):
    """Custom type ntcDvbModEqlnkNonlinInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_NtcDvbModEqlnkNonlinInfo_Type.__name__ = "DisplayString"
_NtcDvbModEqlnkNonlinInfo_Object = MibScalar
ntcDvbModEqlnkNonlinInfo = _NtcDvbModEqlnkNonlinInfo_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 18, 2, 3),
    _NtcDvbModEqlnkNonlinInfo_Type()
)
ntcDvbModEqlnkNonlinInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModEqlnkNonlinInfo.setStatus("current")
_NtcDvbModEqlnkNonlinConf_ObjectIdentity = ObjectIdentity
ntcDvbModEqlnkNonlinConf = _NtcDvbModEqlnkNonlinConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 18, 2, 4)
)
if mibBuilder.loadTexts:
    ntcDvbModEqlnkNonlinConf.setStatus("current")
_NtcDvbModEqlnkNonlinApp_ObjectIdentity = ObjectIdentity
ntcDvbModEqlnkNonlinApp = _NtcDvbModEqlnkNonlinApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 18, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ntcDvbModEqlnkNonlinApp.setStatus("current")


class _NtcDvbModEqlnkNonlinAppOutFreq_Type(Unsigned32):
    """Custom type ntcDvbModEqlnkNonlinAppOutFreq based on Unsigned32"""
    defaultValue = 1450000000


_NtcDvbModEqlnkNonlinAppOutFreq_Type.__name__ = "Unsigned32"
_NtcDvbModEqlnkNonlinAppOutFreq_Object = MibScalar
ntcDvbModEqlnkNonlinAppOutFreq = _NtcDvbModEqlnkNonlinAppOutFreq_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 18, 2, 4, 1, 1),
    _NtcDvbModEqlnkNonlinAppOutFreq_Type()
)
ntcDvbModEqlnkNonlinAppOutFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModEqlnkNonlinAppOutFreq.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModEqlnkNonlinAppOutFreq.setUnits("Hz")


class _NtcDvbModEqlnkNonlinAppVersion_Type(Unsigned32):
    """Custom type ntcDvbModEqlnkNonlinAppVersion based on Unsigned32"""
    defaultValue = 2


_NtcDvbModEqlnkNonlinAppVersion_Type.__name__ = "Unsigned32"
_NtcDvbModEqlnkNonlinAppVersion_Object = MibScalar
ntcDvbModEqlnkNonlinAppVersion = _NtcDvbModEqlnkNonlinAppVersion_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 18, 2, 4, 1, 2),
    _NtcDvbModEqlnkNonlinAppVersion_Type()
)
ntcDvbModEqlnkNonlinAppVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModEqlnkNonlinAppVersion.setStatus("current")
_NtcDvbModAlarm_ObjectIdentity = ObjectIdentity
ntcDvbModAlarm = _NtcDvbModAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19)
)
if mibBuilder.loadTexts:
    ntcDvbModAlarm.setStatus("current")
_NtcDvbModAlmGeneralModulator_Type = NtcAlarmState
_NtcDvbModAlmGeneralModulator_Object = MibScalar
ntcDvbModAlmGeneralModulator = _NtcDvbModAlmGeneralModulator_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 1),
    _NtcDvbModAlmGeneralModulator_Type()
)
ntcDvbModAlmGeneralModulator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmGeneralModulator.setStatus("current")
_NtcDvbModAlmNoInputSignal_Type = NtcAlarmState
_NtcDvbModAlmNoInputSignal_Object = MibScalar
ntcDvbModAlmNoInputSignal = _NtcDvbModAlmNoInputSignal_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 2),
    _NtcDvbModAlmNoInputSignal_Type()
)
ntcDvbModAlmNoInputSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmNoInputSignal.setStatus("current")
_NtcDvbModAlmBufferUnderflow_Type = NtcAlarmState
_NtcDvbModAlmBufferUnderflow_Object = MibScalar
ntcDvbModAlmBufferUnderflow = _NtcDvbModAlmBufferUnderflow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 3),
    _NtcDvbModAlmBufferUnderflow_Type()
)
ntcDvbModAlmBufferUnderflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmBufferUnderflow.setStatus("current")
_NtcDvbModAlmBufferOverflow_Type = NtcAlarmState
_NtcDvbModAlmBufferOverflow_Object = MibScalar
ntcDvbModAlmBufferOverflow = _NtcDvbModAlmBufferOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 4),
    _NtcDvbModAlmBufferOverflow_Type()
)
ntcDvbModAlmBufferOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmBufferOverflow.setStatus("current")
_NtcDvbModAlmNoInputFrameSync_Type = NtcAlarmState
_NtcDvbModAlmNoInputFrameSync_Object = MibScalar
ntcDvbModAlmNoInputFrameSync = _NtcDvbModAlmNoInputFrameSync_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 5),
    _NtcDvbModAlmNoInputFrameSync_Type()
)
ntcDvbModAlmNoInputFrameSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmNoInputFrameSync.setStatus("current")
_NtcDvbModAlmNoBaseBandFrameSync_Type = NtcAlarmState
_NtcDvbModAlmNoBaseBandFrameSync_Object = MibScalar
ntcDvbModAlmNoBaseBandFrameSync = _NtcDvbModAlmNoBaseBandFrameSync_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 6),
    _NtcDvbModAlmNoBaseBandFrameSync_Type()
)
ntcDvbModAlmNoBaseBandFrameSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmNoBaseBandFrameSync.setStatus("current")
_NtcDvbModAlmNoPhyLayerFrameSync_Type = NtcAlarmState
_NtcDvbModAlmNoPhyLayerFrameSync_Object = MibScalar
ntcDvbModAlmNoPhyLayerFrameSync = _NtcDvbModAlmNoPhyLayerFrameSync_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 7),
    _NtcDvbModAlmNoPhyLayerFrameSync_Type()
)
ntcDvbModAlmNoPhyLayerFrameSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmNoPhyLayerFrameSync.setStatus("current")
_NtcDvbModAlmSynthFail_Type = NtcAlarmState
_NtcDvbModAlmSynthFail_Object = MibScalar
ntcDvbModAlmSynthFail = _NtcDvbModAlmSynthFail_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 8),
    _NtcDvbModAlmSynthFail_Type()
)
ntcDvbModAlmSynthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmSynthFail.setStatus("current")
_NtcDvbModAlmRefSynthOutOfLock_Type = NtcAlarmState
_NtcDvbModAlmRefSynthOutOfLock_Object = MibScalar
ntcDvbModAlmRefSynthOutOfLock = _NtcDvbModAlmRefSynthOutOfLock_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 9),
    _NtcDvbModAlmRefSynthOutOfLock_Type()
)
ntcDvbModAlmRefSynthOutOfLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmRefSynthOutOfLock.setStatus("current")
_NtcDvbModAlmLo1SynthOutOfLock_Type = NtcAlarmState
_NtcDvbModAlmLo1SynthOutOfLock_Object = MibScalar
ntcDvbModAlmLo1SynthOutOfLock = _NtcDvbModAlmLo1SynthOutOfLock_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 10),
    _NtcDvbModAlmLo1SynthOutOfLock_Type()
)
ntcDvbModAlmLo1SynthOutOfLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmLo1SynthOutOfLock.setStatus("current")
_NtcDvbModAlmLo2SynthOutOfLock_Type = NtcAlarmState
_NtcDvbModAlmLo2SynthOutOfLock_Object = MibScalar
ntcDvbModAlmLo2SynthOutOfLock = _NtcDvbModAlmLo2SynthOutOfLock_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 11),
    _NtcDvbModAlmLo2SynthOutOfLock_Type()
)
ntcDvbModAlmLo2SynthOutOfLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmLo2SynthOutOfLock.setStatus("current")
_NtcDvbModAlmNoCalibrationData_Type = NtcAlarmState
_NtcDvbModAlmNoCalibrationData_Object = MibScalar
ntcDvbModAlmNoCalibrationData = _NtcDvbModAlmNoCalibrationData_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 12),
    _NtcDvbModAlmNoCalibrationData_Type()
)
ntcDvbModAlmNoCalibrationData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmNoCalibrationData.setStatus("current")
_NtcDvbModAlmDacFailure_Type = NtcAlarmState
_NtcDvbModAlmDacFailure_Object = MibScalar
ntcDvbModAlmDacFailure = _NtcDvbModAlmDacFailure_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 13),
    _NtcDvbModAlmDacFailure_Type()
)
ntcDvbModAlmDacFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmDacFailure.setStatus("current")
_NtcDvbModAlmBucPowerMinCurrent_Type = NtcAlarmState
_NtcDvbModAlmBucPowerMinCurrent_Object = MibScalar
ntcDvbModAlmBucPowerMinCurrent = _NtcDvbModAlmBucPowerMinCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 14),
    _NtcDvbModAlmBucPowerMinCurrent_Type()
)
ntcDvbModAlmBucPowerMinCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmBucPowerMinCurrent.setStatus("current")
_NtcDvbModAlmBucPowerOverload_Type = NtcAlarmState
_NtcDvbModAlmBucPowerOverload_Object = MibScalar
ntcDvbModAlmBucPowerOverload = _NtcDvbModAlmBucPowerOverload_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 15),
    _NtcDvbModAlmBucPowerOverload_Type()
)
ntcDvbModAlmBucPowerOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmBucPowerOverload.setStatus("current")
_NtcDvbModAlmBucPowerSupply_Type = NtcAlarmState
_NtcDvbModAlmBucPowerSupply_Object = MibScalar
ntcDvbModAlmBucPowerSupply = _NtcDvbModAlmBucPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 16),
    _NtcDvbModAlmBucPowerSupply_Type()
)
ntcDvbModAlmBucPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmBucPowerSupply.setStatus("current")
_NtcDvbModAlmBucPowerCap_Type = NtcAlarmState
_NtcDvbModAlmBucPowerCap_Object = MibScalar
ntcDvbModAlmBucPowerCap = _NtcDvbModAlmBucPowerCap_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 17),
    _NtcDvbModAlmBucPowerCap_Type()
)
ntcDvbModAlmBucPowerCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmBucPowerCap.setStatus("current")
_NtcDvbModAlmBucPowerShortCircuit_Type = NtcAlarmState
_NtcDvbModAlmBucPowerShortCircuit_Object = MibScalar
ntcDvbModAlmBucPowerShortCircuit = _NtcDvbModAlmBucPowerShortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 18),
    _NtcDvbModAlmBucPowerShortCircuit_Type()
)
ntcDvbModAlmBucPowerShortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmBucPowerShortCircuit.setStatus("current")
_NtcDvbModAlmBucPowerHardware_Type = NtcAlarmState
_NtcDvbModAlmBucPowerHardware_Object = MibScalar
ntcDvbModAlmBucPowerHardware = _NtcDvbModAlmBucPowerHardware_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 19, 19),
    _NtcDvbModAlmBucPowerHardware_Type()
)
ntcDvbModAlmBucPowerHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAlmBucPowerHardware.setStatus("current")


class _NtcDvbModInputType_Type(Integer32):
    """Custom type ntcDvbModInputType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ts", 0),
          ("bbf", 1))
    )


_NtcDvbModInputType_Type.__name__ = "Integer32"
_NtcDvbModInputType_Object = MibScalar
ntcDvbModInputType = _NtcDvbModInputType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 20),
    _NtcDvbModInputType_Type()
)
ntcDvbModInputType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModInputType.setStatus("current")
_NtcDvbModRfCid_ObjectIdentity = ObjectIdentity
ntcDvbModRfCid = _NtcDvbModRfCid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 21)
)
if mibBuilder.loadTexts:
    ntcDvbModRfCid.setStatus("current")


class _NtcDvbModRfCidEnable_Type(Integer32):
    """Custom type ntcDvbModRfCidEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcDvbModRfCidEnable_Type.__name__ = "Integer32"
_NtcDvbModRfCidEnable_Object = MibScalar
ntcDvbModRfCidEnable = _NtcDvbModRfCidEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 21, 1),
    _NtcDvbModRfCidEnable_Type()
)
ntcDvbModRfCidEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModRfCidEnable.setStatus("current")


class _NtcDvbModRfCidId_Type(DisplayString):
    """Custom type ntcDvbModRfCidId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtcDvbModRfCidId_Type.__name__ = "DisplayString"
_NtcDvbModRfCidId_Object = MibScalar
ntcDvbModRfCidId = _NtcDvbModRfCidId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 21, 2),
    _NtcDvbModRfCidId_Type()
)
ntcDvbModRfCidId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModRfCidId.setStatus("current")
_NtcDvbModRfCidFormat_Type = Unsigned32
_NtcDvbModRfCidFormat_Object = MibScalar
ntcDvbModRfCidFormat = _NtcDvbModRfCidFormat_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 21, 3),
    _NtcDvbModRfCidFormat_Type()
)
ntcDvbModRfCidFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModRfCidFormat.setStatus("current")


class _NtcDvbModRfCidSendGeoCord_Type(Integer32):
    """Custom type ntcDvbModRfCidSendGeoCord based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcDvbModRfCidSendGeoCord_Type.__name__ = "Integer32"
_NtcDvbModRfCidSendGeoCord_Object = MibScalar
ntcDvbModRfCidSendGeoCord = _NtcDvbModRfCidSendGeoCord_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 21, 4),
    _NtcDvbModRfCidSendGeoCord_Type()
)
ntcDvbModRfCidSendGeoCord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModRfCidSendGeoCord.setStatus("current")


class _NtcDvbModRfCidLatitude_Type(Float32TC):
    """Custom type ntcDvbModRfCidLatitude based on Float32TC"""
    defaultHexValue = "00000000"


_NtcDvbModRfCidLatitude_Type.__name__ = "Float32TC"
_NtcDvbModRfCidLatitude_Object = MibScalar
ntcDvbModRfCidLatitude = _NtcDvbModRfCidLatitude_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 21, 5),
    _NtcDvbModRfCidLatitude_Type()
)
ntcDvbModRfCidLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModRfCidLatitude.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModRfCidLatitude.setUnits("deg.")


class _NtcDvbModRfCidLongitude_Type(Float32TC):
    """Custom type ntcDvbModRfCidLongitude based on Float32TC"""
    defaultHexValue = "00000000"


_NtcDvbModRfCidLongitude_Type.__name__ = "Float32TC"
_NtcDvbModRfCidLongitude_Object = MibScalar
ntcDvbModRfCidLongitude = _NtcDvbModRfCidLongitude_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 21, 6),
    _NtcDvbModRfCidLongitude_Type()
)
ntcDvbModRfCidLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModRfCidLongitude.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModRfCidLongitude.setUnits("deg.")


class _NtcDvbModRfCidPhone_Type(DisplayString):
    """Custom type ntcDvbModRfCidPhone based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtcDvbModRfCidPhone_Type.__name__ = "DisplayString"
_NtcDvbModRfCidPhone_Object = MibScalar
ntcDvbModRfCidPhone = _NtcDvbModRfCidPhone_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 21, 7),
    _NtcDvbModRfCidPhone_Type()
)
ntcDvbModRfCidPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModRfCidPhone.setStatus("current")


class _NtcDvbModRfCidData_Type(DisplayString):
    """Custom type ntcDvbModRfCidData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_NtcDvbModRfCidData_Type.__name__ = "DisplayString"
_NtcDvbModRfCidData_Object = MibScalar
ntcDvbModRfCidData = _NtcDvbModRfCidData_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 21, 8),
    _NtcDvbModRfCidData_Type()
)
ntcDvbModRfCidData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModRfCidData.setStatus("current")


class _NtcDvbModRfCidLatitudeString_Type(DisplayString):
    """Custom type ntcDvbModRfCidLatitudeString based on DisplayString"""
    defaultValue = OctetString("0.0000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_NtcDvbModRfCidLatitudeString_Type.__name__ = "DisplayString"
_NtcDvbModRfCidLatitudeString_Object = MibScalar
ntcDvbModRfCidLatitudeString = _NtcDvbModRfCidLatitudeString_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 21, 9),
    _NtcDvbModRfCidLatitudeString_Type()
)
ntcDvbModRfCidLatitudeString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModRfCidLatitudeString.setStatus("current")


class _NtcDvbModRfCidLongitudeString_Type(DisplayString):
    """Custom type ntcDvbModRfCidLongitudeString based on DisplayString"""
    defaultValue = OctetString("0.0000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_NtcDvbModRfCidLongitudeString_Type.__name__ = "DisplayString"
_NtcDvbModRfCidLongitudeString_Object = MibScalar
ntcDvbModRfCidLongitudeString = _NtcDvbModRfCidLongitudeString_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 21, 10),
    _NtcDvbModRfCidLongitudeString_Type()
)
ntcDvbModRfCidLongitudeString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModRfCidLongitudeString.setStatus("current")
_NtcDvbModDcBuc_ObjectIdentity = ObjectIdentity
ntcDvbModDcBuc = _NtcDvbModDcBuc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 22)
)
if mibBuilder.loadTexts:
    ntcDvbModDcBuc.setStatus("current")


class _NtcDvbModDcBucEnable_Type(Integer32):
    """Custom type ntcDvbModDcBucEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcDvbModDcBucEnable_Type.__name__ = "Integer32"
_NtcDvbModDcBucEnable_Object = MibScalar
ntcDvbModDcBucEnable = _NtcDvbModDcBucEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 22, 1),
    _NtcDvbModDcBucEnable_Type()
)
ntcDvbModDcBucEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDcBucEnable.setStatus("current")


class _NtcDvbModDcBucVoltage_Type(Integer32):
    """Custom type ntcDvbModDcBucVoltage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e24V", 0),
          ("e48V", 1))
    )


_NtcDvbModDcBucVoltage_Type.__name__ = "Integer32"
_NtcDvbModDcBucVoltage_Object = MibScalar
ntcDvbModDcBucVoltage = _NtcDvbModDcBucVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 22, 2),
    _NtcDvbModDcBucVoltage_Type()
)
ntcDvbModDcBucVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDcBucVoltage.setStatus("current")


class _NtcDvbModDcBucOutVoltage_Type(Integer32):
    """Custom type ntcDvbModDcBucOutVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_NtcDvbModDcBucOutVoltage_Type.__name__ = "Integer32"
_NtcDvbModDcBucOutVoltage_Object = MibScalar
ntcDvbModDcBucOutVoltage = _NtcDvbModDcBucOutVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 22, 3),
    _NtcDvbModDcBucOutVoltage_Type()
)
ntcDvbModDcBucOutVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModDcBucOutVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModDcBucOutVoltage.setUnits("mV")


class _NtcDvbModDcBucOutCurrent_Type(Integer32):
    """Custom type ntcDvbModDcBucOutCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_NtcDvbModDcBucOutCurrent_Type.__name__ = "Integer32"
_NtcDvbModDcBucOutCurrent_Object = MibScalar
ntcDvbModDcBucOutCurrent = _NtcDvbModDcBucOutCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 22, 4),
    _NtcDvbModDcBucOutCurrent_Type()
)
ntcDvbModDcBucOutCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModDcBucOutCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModDcBucOutCurrent.setUnits("mA")


class _NtcDvbModDcBucMinCurrent_Type(Integer32):
    """Custom type ntcDvbModDcBucMinCurrent based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_NtcDvbModDcBucMinCurrent_Type.__name__ = "Integer32"
_NtcDvbModDcBucMinCurrent_Object = MibScalar
ntcDvbModDcBucMinCurrent = _NtcDvbModDcBucMinCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 22, 5),
    _NtcDvbModDcBucMinCurrent_Type()
)
ntcDvbModDcBucMinCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDcBucMinCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModDcBucMinCurrent.setUnits("mA")


class _NtcDvbModRatePriority_Type(Integer32):
    """Custom type ntcDvbModRatePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("symbolrate", 0),
          ("bitrate", 1))
    )


_NtcDvbModRatePriority_Type.__name__ = "Integer32"
_NtcDvbModRatePriority_Object = MibScalar
ntcDvbModRatePriority = _NtcDvbModRatePriority_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 23),
    _NtcDvbModRatePriority_Type()
)
ntcDvbModRatePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModRatePriority.setStatus("current")


class _NtcDvbModSymbolRate_Type(Unsigned32):
    """Custom type ntcDvbModSymbolRate based on Unsigned32"""
    defaultValue = 10000000


_NtcDvbModSymbolRate_Type.__name__ = "Unsigned32"
_NtcDvbModSymbolRate_Object = MibScalar
ntcDvbModSymbolRate = _NtcDvbModSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 24),
    _NtcDvbModSymbolRate_Type()
)
ntcDvbModSymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModSymbolRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModSymbolRate.setUnits("baud")


class _NtcDvbModBitRate_Type(Unsigned32):
    """Custom type ntcDvbModBitRate based on Unsigned32"""
    defaultValue = 5000000


_NtcDvbModBitRate_Type.__name__ = "Unsigned32"
_NtcDvbModBitRate_Object = MibScalar
ntcDvbModBitRate = _NtcDvbModBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 25),
    _NtcDvbModBitRate_Type()
)
ntcDvbModBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModBitRate.setUnits("bps")
_NtcDvbModMeasuredPktCount_Type = Counter32
_NtcDvbModMeasuredPktCount_Object = MibScalar
ntcDvbModMeasuredPktCount = _NtcDvbModMeasuredPktCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 26),
    _NtcDvbModMeasuredPktCount_Type()
)
ntcDvbModMeasuredPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModMeasuredPktCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModMeasuredPktCount.setUnits("packets")
_NtcDvbModMeasuredBitRate_Type = Unsigned32
_NtcDvbModMeasuredBitRate_Object = MibScalar
ntcDvbModMeasuredBitRate = _NtcDvbModMeasuredBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 27),
    _NtcDvbModMeasuredBitRate_Type()
)
ntcDvbModMeasuredBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModMeasuredBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModMeasuredBitRate.setUnits("bps")


class _NtcDvbModReset_Type(Integer32):
    """Custom type ntcDvbModReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("counting", 0),
          ("reset", 1))
    )


_NtcDvbModReset_Type.__name__ = "Integer32"
_NtcDvbModReset_Object = MibScalar
ntcDvbModReset = _NtcDvbModReset_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 28),
    _NtcDvbModReset_Type()
)
ntcDvbModReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModReset.setStatus("current")
_NtcDvbModS2Ext_ObjectIdentity = ObjectIdentity
ntcDvbModS2Ext = _NtcDvbModS2Ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 29)
)
if mibBuilder.loadTexts:
    ntcDvbModS2Ext.setStatus("current")


class _NtcDvbModS2ExtModCod_Type(Integer32):
    """Custom type ntcDvbModS2ExtModCod based on Integer32"""
    defaultValue = 129

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("qpsk45180", 129),
          ("qpsk60180", 130),
          ("qpsk72180", 131),
          ("qpsk80180", 132),
          ("qpsk90180", 133),
          ("qpsk100180", 134),
          ("qpsk108180", 135),
          ("qpsk114180", 136),
          ("qpsk120180", 137),
          ("qpsk126180", 138),
          ("qpsk135180", 139),
          ("qpsk144180", 140),
          ("qpsk150180", 141),
          ("qpsk160180", 142),
          ("qpsk162180", 143),
          ("e8psk80180", 144),
          ("e8psk90180", 145),
          ("e8psk100180", 146),
          ("e8psk108180", 147),
          ("e8psk114180", 148),
          ("e8psk120180", 149),
          ("e8psk126180", 150),
          ("e8psk135180", 151),
          ("e8psk144180", 152),
          ("e8psk150180", 153),
          ("e16apsk80180", 154),
          ("e16apsk90180", 155),
          ("e16apsk100180", 156),
          ("e16apsk108180", 157),
          ("e16apsk114180", 158),
          ("e16apsk120180", 159),
          ("e16apsk126180", 160),
          ("e16apsk135180", 161),
          ("e16apsk144180", 162),
          ("e16apsk150180", 163),
          ("e16apsk160180", 164),
          ("e16apsk162180", 165),
          ("e32apsk100180", 166),
          ("e32apsk108180", 167),
          ("e32apsk114180", 168),
          ("e32apsk120180", 169),
          ("e32apsk126180", 170),
          ("e32apsk135180", 171),
          ("e32apsk144180", 172),
          ("e32apsk150180", 173),
          ("e32apsk160180", 174),
          ("e32apsk162180", 175),
          ("e64apsk90180", 176),
          ("e64apsk100180", 177),
          ("e64apsk108180", 178),
          ("e64apsk114180", 179),
          ("e64apsk120180", 180),
          ("e64apsk126180", 181),
          ("e64apsk135180", 182),
          ("e64apsk144180", 183),
          ("e64apsk150180", 184),
          ("e64apsk160180", 185),
          ("e64apsk162180", 186),
          ("e8pskl80180", 187),
          ("e8pskl90180", 188),
          ("e8pskl100180", 189),
          ("e8pskl108180", 190),
          ("e8pskl114180", 191),
          ("e8pskl120180", 192),
          ("e16apskl80180", 193),
          ("e16apskl90180", 194),
          ("e16apskl100180", 195),
          ("e16apskl108180", 196),
          ("e16apskl114180", 197),
          ("e16apskl120180", 198),
          ("e16apskl126180", 199),
          ("e16apskl135180", 200),
          ("e16apskl144180", 201),
          ("e16apskl150180", 202),
          ("e16apskl160180", 203),
          ("e16apskl162180", 204),
          ("e64apskl90180", 205),
          ("e64apskl100180", 206),
          ("e64apskl108180", 207),
          ("e64apskl114180", 208),
          ("e64apskl120180", 209),
          ("e64apskl126180", 210),
          ("e64apskl135180", 211),
          ("e64apskl144180", 212),
          ("e64apskl150180", 213),
          ("e64apskl160180", 214),
          ("e64apskl162180", 215))
    )


_NtcDvbModS2ExtModCod_Type.__name__ = "Integer32"
_NtcDvbModS2ExtModCod_Object = MibScalar
ntcDvbModS2ExtModCod = _NtcDvbModS2ExtModCod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 29, 1),
    _NtcDvbModS2ExtModCod_Type()
)
ntcDvbModS2ExtModCod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModS2ExtModCod.setStatus("current")


class _NtcDvbModS2ExtPhyLayerEfficiency_Type(Integer32):
    """Custom type ntcDvbModS2ExtPhyLayerEfficiency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_NtcDvbModS2ExtPhyLayerEfficiency_Type.__name__ = "Integer32"
_NtcDvbModS2ExtPhyLayerEfficiency_Object = MibScalar
ntcDvbModS2ExtPhyLayerEfficiency = _NtcDvbModS2ExtPhyLayerEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 29, 2),
    _NtcDvbModS2ExtPhyLayerEfficiency_Type()
)
ntcDvbModS2ExtPhyLayerEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModS2ExtPhyLayerEfficiency.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModS2ExtPhyLayerEfficiency.setUnits("%")


class _NtcDvbModS2ExtBbLayerEfficiency_Type(Integer32):
    """Custom type ntcDvbModS2ExtBbLayerEfficiency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_NtcDvbModS2ExtBbLayerEfficiency_Type.__name__ = "Integer32"
_NtcDvbModS2ExtBbLayerEfficiency_Object = MibScalar
ntcDvbModS2ExtBbLayerEfficiency = _NtcDvbModS2ExtBbLayerEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 29, 3),
    _NtcDvbModS2ExtBbLayerEfficiency_Type()
)
ntcDvbModS2ExtBbLayerEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModS2ExtBbLayerEfficiency.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModS2ExtBbLayerEfficiency.setUnits("%")


class _NtcDvbModS2ExtDumPlScramblMode_Type(Integer32):
    """Custom type ntcDvbModS2ExtDumPlScramblMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dvbs2standard", 0),
          ("continuous", 1))
    )


_NtcDvbModS2ExtDumPlScramblMode_Type.__name__ = "Integer32"
_NtcDvbModS2ExtDumPlScramblMode_Object = MibScalar
ntcDvbModS2ExtDumPlScramblMode = _NtcDvbModS2ExtDumPlScramblMode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 29, 4),
    _NtcDvbModS2ExtDumPlScramblMode_Type()
)
ntcDvbModS2ExtDumPlScramblMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModS2ExtDumPlScramblMode.setStatus("current")


class _NtcDvbModS2ExtPlScrambSig_Type(Unsigned32):
    """Custom type ntcDvbModS2ExtPlScrambSig based on Unsigned32"""
    defaultValue = 0


_NtcDvbModS2ExtPlScrambSig_Type.__name__ = "Unsigned32"
_NtcDvbModS2ExtPlScrambSig_Object = MibScalar
ntcDvbModS2ExtPlScrambSig = _NtcDvbModS2ExtPlScrambSig_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 29, 5),
    _NtcDvbModS2ExtPlScrambSig_Type()
)
ntcDvbModS2ExtPlScrambSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModS2ExtPlScrambSig.setStatus("current")


class _NtcDvbModS2ExtRollOffSignalling_Type(Integer32):
    """Custom type ntcDvbModS2ExtRollOffSignalling based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("standard", 0),
          ("reserved", 1))
    )


_NtcDvbModS2ExtRollOffSignalling_Type.__name__ = "Integer32"
_NtcDvbModS2ExtRollOffSignalling_Object = MibScalar
ntcDvbModS2ExtRollOffSignalling = _NtcDvbModS2ExtRollOffSignalling_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 29, 6),
    _NtcDvbModS2ExtRollOffSignalling_Type()
)
ntcDvbModS2ExtRollOffSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModS2ExtRollOffSignalling.setStatus("current")
_NtcDvbModTurbo_ObjectIdentity = ObjectIdentity
ntcDvbModTurbo = _NtcDvbModTurbo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 30)
)
if mibBuilder.loadTexts:
    ntcDvbModTurbo.setStatus("current")


class _NtcDvbModTurboModCod_Type(Integer32):
    """Custom type ntcDvbModTurboModCod based on Integer32"""
    defaultValue = 2

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
        *(("qpsk12", 1),
          ("qpsk34", 2),
          ("qpsk23", 3),
          ("qpsk56", 4),
          ("qpsk78", 5),
          ("e8psk23", 6),
          ("e8psk34", 7),
          ("e8psk45", 8),
          ("e8psk56", 9),
          ("e8psk89", 10))
    )


_NtcDvbModTurboModCod_Type.__name__ = "Integer32"
_NtcDvbModTurboModCod_Object = MibScalar
ntcDvbModTurboModCod = _NtcDvbModTurboModCod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 30, 1),
    _NtcDvbModTurboModCod_Type()
)
ntcDvbModTurboModCod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModTurboModCod.setStatus("current")


class _NtcDvbModTurboDeleteSync_Type(Integer32):
    """Custom type ntcDvbModTurboDeleteSync based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcDvbModTurboDeleteSync_Type.__name__ = "Integer32"
_NtcDvbModTurboDeleteSync_Object = MibScalar
ntcDvbModTurboDeleteSync = _NtcDvbModTurboDeleteSync_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 30, 2),
    _NtcDvbModTurboDeleteSync_Type()
)
ntcDvbModTurboDeleteSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModTurboDeleteSync.setStatus("current")
_NtcDvbModAmcDvbs_ObjectIdentity = ObjectIdentity
ntcDvbModAmcDvbs = _NtcDvbModAmcDvbs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 31)
)
if mibBuilder.loadTexts:
    ntcDvbModAmcDvbs.setStatus("current")


class _NtcDvbModAmcDvbsModCod_Type(Integer32):
    """Custom type ntcDvbModAmcDvbsModCod based on Integer32"""
    defaultValue = 3

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
        *(("qpsk12", 1),
          ("qpsk23", 2),
          ("qpsk34", 3),
          ("qpsk56", 4),
          ("qpsk78", 5))
    )


_NtcDvbModAmcDvbsModCod_Type.__name__ = "Integer32"
_NtcDvbModAmcDvbsModCod_Object = MibScalar
ntcDvbModAmcDvbsModCod = _NtcDvbModAmcDvbsModCod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 31, 1),
    _NtcDvbModAmcDvbsModCod_Type()
)
ntcDvbModAmcDvbsModCod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAmcDvbsModCod.setStatus("current")
_NtcDvbModAmcNbc_ObjectIdentity = ObjectIdentity
ntcDvbModAmcNbc = _NtcDvbModAmcNbc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 32)
)
if mibBuilder.loadTexts:
    ntcDvbModAmcNbc.setStatus("current")


class _NtcDvbModAmcNbcFrameType_Type(Integer32):
    """Custom type ntcDvbModAmcNbcFrameType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("short", 0),
          ("normal", 1))
    )


_NtcDvbModAmcNbcFrameType_Type.__name__ = "Integer32"
_NtcDvbModAmcNbcFrameType_Object = MibScalar
ntcDvbModAmcNbcFrameType = _NtcDvbModAmcNbcFrameType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 32, 1),
    _NtcDvbModAmcNbcFrameType_Type()
)
ntcDvbModAmcNbcFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAmcNbcFrameType.setStatus("current")


class _NtcDvbModAmcNbcModCod_Type(Integer32):
    """Custom type ntcDvbModAmcNbcModCod based on Integer32"""
    defaultValue = 4

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
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("qpsk12", 1),
          ("qpsk35", 2),
          ("qpsk23", 3),
          ("qpsk34", 4),
          ("qpsk45", 5),
          ("qpsk56", 6),
          ("qpsk89", 7),
          ("qpsk910", 8),
          ("e8psk35", 9),
          ("e8psk23", 10),
          ("e8psk34", 11),
          ("e8psk56", 12),
          ("e8psk89", 13),
          ("e8psk910", 14))
    )


_NtcDvbModAmcNbcModCod_Type.__name__ = "Integer32"
_NtcDvbModAmcNbcModCod_Object = MibScalar
ntcDvbModAmcNbcModCod = _NtcDvbModAmcNbcModCod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 32, 2),
    _NtcDvbModAmcNbcModCod_Type()
)
ntcDvbModAmcNbcModCod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAmcNbcModCod.setStatus("current")


class _NtcDvbModAmcNbcPilots_Type(NtcEnable):
    """Custom type ntcDvbModAmcNbcPilots based on NtcEnable"""
    defaultValue = 0


_NtcDvbModAmcNbcPilots_Type.__name__ = "NtcEnable"
_NtcDvbModAmcNbcPilots_Object = MibScalar
ntcDvbModAmcNbcPilots = _NtcDvbModAmcNbcPilots_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 32, 3),
    _NtcDvbModAmcNbcPilots_Type()
)
ntcDvbModAmcNbcPilots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAmcNbcPilots.setStatus("current")


class _NtcDvbModAmcNbcPLEfficiency_Type(Integer32):
    """Custom type ntcDvbModAmcNbcPLEfficiency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_NtcDvbModAmcNbcPLEfficiency_Type.__name__ = "Integer32"
_NtcDvbModAmcNbcPLEfficiency_Object = MibScalar
ntcDvbModAmcNbcPLEfficiency = _NtcDvbModAmcNbcPLEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 32, 4),
    _NtcDvbModAmcNbcPLEfficiency_Type()
)
ntcDvbModAmcNbcPLEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAmcNbcPLEfficiency.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModAmcNbcPLEfficiency.setUnits("%")


class _NtcDvbModAmcNbcBbLayerEfficiency_Type(Integer32):
    """Custom type ntcDvbModAmcNbcBbLayerEfficiency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_NtcDvbModAmcNbcBbLayerEfficiency_Type.__name__ = "Integer32"
_NtcDvbModAmcNbcBbLayerEfficiency_Object = MibScalar
ntcDvbModAmcNbcBbLayerEfficiency = _NtcDvbModAmcNbcBbLayerEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 32, 5),
    _NtcDvbModAmcNbcBbLayerEfficiency_Type()
)
ntcDvbModAmcNbcBbLayerEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModAmcNbcBbLayerEfficiency.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModAmcNbcBbLayerEfficiency.setUnits("%")


class _NtcDvbModAmcNbcPlHdrScrmSeq_Type(Unsigned32):
    """Custom type ntcDvbModAmcNbcPlHdrScrmSeq based on Unsigned32"""
    defaultValue = 0


_NtcDvbModAmcNbcPlHdrScrmSeq_Type.__name__ = "Unsigned32"
_NtcDvbModAmcNbcPlHdrScrmSeq_Object = MibScalar
ntcDvbModAmcNbcPlHdrScrmSeq = _NtcDvbModAmcNbcPlHdrScrmSeq_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 32, 6),
    _NtcDvbModAmcNbcPlHdrScrmSeq_Type()
)
ntcDvbModAmcNbcPlHdrScrmSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAmcNbcPlHdrScrmSeq.setStatus("current")


class _NtcDvbModAmcNbcRollOffSignalling_Type(Integer32):
    """Custom type ntcDvbModAmcNbcRollOffSignalling based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("standard", 0),
          ("reserved", 1))
    )


_NtcDvbModAmcNbcRollOffSignalling_Type.__name__ = "Integer32"
_NtcDvbModAmcNbcRollOffSignalling_Object = MibScalar
ntcDvbModAmcNbcRollOffSignalling = _NtcDvbModAmcNbcRollOffSignalling_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 32, 7),
    _NtcDvbModAmcNbcRollOffSignalling_Type()
)
ntcDvbModAmcNbcRollOffSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAmcNbcRollOffSignalling.setStatus("current")


class _NtcDvbModActualOutputLevel_Type(Integer32):
    """Custom type ntcDvbModActualOutputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-350, 100),
    )


_NtcDvbModActualOutputLevel_Type.__name__ = "Integer32"
_NtcDvbModActualOutputLevel_Object = MibScalar
ntcDvbModActualOutputLevel = _NtcDvbModActualOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 33),
    _NtcDvbModActualOutputLevel_Type()
)
ntcDvbModActualOutputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModActualOutputLevel.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModActualOutputLevel.setUnits("dBm")


class _NtcDvbModTransmitStateReason_Type(DisplayString):
    """Custom type ntcDvbModTransmitStateReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcDvbModTransmitStateReason_Type.__name__ = "DisplayString"
_NtcDvbModTransmitStateReason_Object = MibScalar
ntcDvbModTransmitStateReason = _NtcDvbModTransmitStateReason_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 34),
    _NtcDvbModTransmitStateReason_Type()
)
ntcDvbModTransmitStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModTransmitStateReason.setStatus("current")
_NtcDvbModLinkOpt_ObjectIdentity = ObjectIdentity
ntcDvbModLinkOpt = _NtcDvbModLinkOpt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 35)
)
if mibBuilder.loadTexts:
    ntcDvbModLinkOpt.setStatus("current")


class _NtcDvbModLinkOptTransMode_Type(Integer32):
    """Custom type ntcDvbModLinkOptTransMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("single", 1),
          ("multiple", 2),
          ("singlelin", 3))
    )


_NtcDvbModLinkOptTransMode_Type.__name__ = "Integer32"
_NtcDvbModLinkOptTransMode_Object = MibScalar
ntcDvbModLinkOptTransMode = _NtcDvbModLinkOptTransMode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 35, 1),
    _NtcDvbModLinkOptTransMode_Type()
)
ntcDvbModLinkOptTransMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModLinkOptTransMode.setStatus("current")


class _NtcDvbModMaxModulation_Type(Integer32):
    """Custom type ntcDvbModMaxModulation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
        *(("unspecified", 0),
          ("e4ary", 2),
          ("e8ary", 3),
          ("e16ary", 4),
          ("e32ary", 5),
          ("e64ary", 6),
          ("e128ary", 7),
          ("e256ary", 8))
    )


_NtcDvbModMaxModulation_Type.__name__ = "Integer32"
_NtcDvbModMaxModulation_Object = MibScalar
ntcDvbModMaxModulation = _NtcDvbModMaxModulation_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 35, 2),
    _NtcDvbModMaxModulation_Type()
)
ntcDvbModMaxModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModMaxModulation.setStatus("current")


class _NtcDvbModAllowChangesWhileTxOn_Type(NtcEnable):
    """Custom type ntcDvbModAllowChangesWhileTxOn based on NtcEnable"""
    defaultValue = 0


_NtcDvbModAllowChangesWhileTxOn_Type.__name__ = "NtcEnable"
_NtcDvbModAllowChangesWhileTxOn_Object = MibScalar
ntcDvbModAllowChangesWhileTxOn = _NtcDvbModAllowChangesWhileTxOn_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 36),
    _NtcDvbModAllowChangesWhileTxOn_Type()
)
ntcDvbModAllowChangesWhileTxOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAllowChangesWhileTxOn.setStatus("current")


class _NtcDvbModStandbyRedundancyState_Type(Integer32):
    """Custom type ntcDvbModStandbyRedundancyState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("standby", 0),
          ("active", 1))
    )


_NtcDvbModStandbyRedundancyState_Type.__name__ = "Integer32"
_NtcDvbModStandbyRedundancyState_Object = MibScalar
ntcDvbModStandbyRedundancyState = _NtcDvbModStandbyRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 37),
    _NtcDvbModStandbyRedundancyState_Type()
)
ntcDvbModStandbyRedundancyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModStandbyRedundancyState.setStatus("current")
_NtcDvbModDSNGProfiles_ObjectIdentity = ObjectIdentity
ntcDvbModDSNGProfiles = _NtcDvbModDSNGProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 38)
)
if mibBuilder.loadTexts:
    ntcDvbModDSNGProfiles.setStatus("current")


class _NtcDvbModDSNGProfilesProfile_Type(OctetString):
    """Custom type ntcDvbModDSNGProfilesProfile based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcDvbModDSNGProfilesProfile_Type.__name__ = "OctetString"
_NtcDvbModDSNGProfilesProfile_Object = MibScalar
ntcDvbModDSNGProfilesProfile = _NtcDvbModDSNGProfilesProfile_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 38, 38),
    _NtcDvbModDSNGProfilesProfile_Type()
)
ntcDvbModDSNGProfilesProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDSNGProfilesProfile.setStatus("current")


class _NtcDvbModDSNGProfilesLevel_Type(OctetString):
    """Custom type ntcDvbModDSNGProfilesLevel based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcDvbModDSNGProfilesLevel_Type.__name__ = "OctetString"
_NtcDvbModDSNGProfilesLevel_Object = MibScalar
ntcDvbModDSNGProfilesLevel = _NtcDvbModDSNGProfilesLevel_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 38, 39),
    _NtcDvbModDSNGProfilesLevel_Type()
)
ntcDvbModDSNGProfilesLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModDSNGProfilesLevel.setStatus("current")


class _NtcDvbModStreamMode_Type(Integer32):
    """Custom type ntcDvbModStreamMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multistream", 1),
          ("singlestream", 2))
    )


_NtcDvbModStreamMode_Type.__name__ = "Integer32"
_NtcDvbModStreamMode_Object = MibScalar
ntcDvbModStreamMode = _NtcDvbModStreamMode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 39),
    _NtcDvbModStreamMode_Type()
)
ntcDvbModStreamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModStreamMode.setStatus("current")
_NtcDvbModAmcDl_ObjectIdentity = ObjectIdentity
ntcDvbModAmcDl = _NtcDvbModAmcDl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 40)
)
if mibBuilder.loadTexts:
    ntcDvbModAmcDl.setStatus("current")


class _NtcDvbModAmcDlModCod_Type(Integer32):
    """Custom type ntcDvbModAmcDlModCod based on Integer32"""
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
        *(("qpsk12", 1),
          ("qpsk23", 2),
          ("qpsk67", 3))
    )


_NtcDvbModAmcDlModCod_Type.__name__ = "Integer32"
_NtcDvbModAmcDlModCod_Object = MibScalar
ntcDvbModAmcDlModCod = _NtcDvbModAmcDlModCod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 40, 1),
    _NtcDvbModAmcDlModCod_Type()
)
ntcDvbModAmcDlModCod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAmcDlModCod.setStatus("current")


class _NtcDvbModIfOutputLevel_Type(Integer32):
    """Custom type ntcDvbModIfOutputLevel based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-350, 50),
    )


_NtcDvbModIfOutputLevel_Type.__name__ = "Integer32"
_NtcDvbModIfOutputLevel_Object = MibScalar
ntcDvbModIfOutputLevel = _NtcDvbModIfOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 41),
    _NtcDvbModIfOutputLevel_Type()
)
ntcDvbModIfOutputLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModIfOutputLevel.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModIfOutputLevel.setUnits("dBm")


class _NtcDvbModLbandOutputLevel_Type(Integer32):
    """Custom type ntcDvbModLbandOutputLevel based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 50),
    )


_NtcDvbModLbandOutputLevel_Type.__name__ = "Integer32"
_NtcDvbModLbandOutputLevel_Object = MibScalar
ntcDvbModLbandOutputLevel = _NtcDvbModLbandOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 42),
    _NtcDvbModLbandOutputLevel_Type()
)
ntcDvbModLbandOutputLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModLbandOutputLevel.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModLbandOutputLevel.setUnits("dBm")


class _NtcDvbModIfOutputFrequency_Type(Integer32):
    """Custom type ntcDvbModIfOutputFrequency based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e70MHz", 1),
          ("e140MHz", 2))
    )


_NtcDvbModIfOutputFrequency_Type.__name__ = "Integer32"
_NtcDvbModIfOutputFrequency_Object = MibScalar
ntcDvbModIfOutputFrequency = _NtcDvbModIfOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 43),
    _NtcDvbModIfOutputFrequency_Type()
)
ntcDvbModIfOutputFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModIfOutputFrequency.setStatus("current")


class _NtcDvbModLbandOutputFrequency_Type(Unsigned32):
    """Custom type ntcDvbModLbandOutputFrequency based on Unsigned32"""
    defaultValue = 1250000000


_NtcDvbModLbandOutputFrequency_Type.__name__ = "Unsigned32"
_NtcDvbModLbandOutputFrequency_Object = MibScalar
ntcDvbModLbandOutputFrequency = _NtcDvbModLbandOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 44),
    _NtcDvbModLbandOutputFrequency_Type()
)
ntcDvbModLbandOutputFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModLbandOutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModLbandOutputFrequency.setUnits("Hz")


class _NtcDvbModLbandTx_Type(NtcEnable):
    """Custom type ntcDvbModLbandTx based on NtcEnable"""
    defaultValue = 0


_NtcDvbModLbandTx_Type.__name__ = "NtcEnable"
_NtcDvbModLbandTx_Object = MibScalar
ntcDvbModLbandTx = _NtcDvbModLbandTx_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 45),
    _NtcDvbModLbandTx_Type()
)
ntcDvbModLbandTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModLbandTx.setStatus("current")


class _NtcDvbModLbandTxState_Type(Integer32):
    """Custom type ntcDvbModLbandTxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcDvbModLbandTxState_Type.__name__ = "Integer32"
_NtcDvbModLbandTxState_Object = MibScalar
ntcDvbModLbandTxState = _NtcDvbModLbandTxState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 46),
    _NtcDvbModLbandTxState_Type()
)
ntcDvbModLbandTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModLbandTxState.setStatus("current")


class _NtcDvbModLbandTxStateReason_Type(DisplayString):
    """Custom type ntcDvbModLbandTxStateReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcDvbModLbandTxStateReason_Type.__name__ = "DisplayString"
_NtcDvbModLbandTxStateReason_Object = MibScalar
ntcDvbModLbandTxStateReason = _NtcDvbModLbandTxStateReason_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 47),
    _NtcDvbModLbandTxStateReason_Type()
)
ntcDvbModLbandTxStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModLbandTxStateReason.setStatus("current")
_NtcDvbModExtConv_ObjectIdentity = ObjectIdentity
ntcDvbModExtConv = _NtcDvbModExtConv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 48)
)
if mibBuilder.loadTexts:
    ntcDvbModExtConv.setStatus("current")


class _NtcDvbModExtConvEnable_Type(Integer32):
    """Custom type ntcDvbModExtConvEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcDvbModExtConvEnable_Type.__name__ = "Integer32"
_NtcDvbModExtConvEnable_Object = MibScalar
ntcDvbModExtConvEnable = _NtcDvbModExtConvEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 48, 1),
    _NtcDvbModExtConvEnable_Type()
)
ntcDvbModExtConvEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModExtConvEnable.setStatus("current")


class _NtcDvbModExtConvRfFrequency_Type(DisplayString):
    """Custom type ntcDvbModExtConvRfFrequency based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtcDvbModExtConvRfFrequency_Type.__name__ = "DisplayString"
_NtcDvbModExtConvRfFrequency_Object = MibScalar
ntcDvbModExtConvRfFrequency = _NtcDvbModExtConvRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 48, 2),
    _NtcDvbModExtConvRfFrequency_Type()
)
ntcDvbModExtConvRfFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModExtConvRfFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModExtConvRfFrequency.setUnits("Hz")


class _NtcDvbModExtConvLoFrequency_Type(DisplayString):
    """Custom type ntcDvbModExtConvLoFrequency based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtcDvbModExtConvLoFrequency_Type.__name__ = "DisplayString"
_NtcDvbModExtConvLoFrequency_Object = MibScalar
ntcDvbModExtConvLoFrequency = _NtcDvbModExtConvLoFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 48, 3),
    _NtcDvbModExtConvLoFrequency_Type()
)
ntcDvbModExtConvLoFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModExtConvLoFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModExtConvLoFrequency.setUnits("Hz")


class _NtcDvbModExtConvSpectrumInv_Type(Integer32):
    """Custom type ntcDvbModExtConvSpectrumInv based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("directSpectrum", 1),
          ("invertedSpectrum", 2))
    )


_NtcDvbModExtConvSpectrumInv_Type.__name__ = "Integer32"
_NtcDvbModExtConvSpectrumInv_Object = MibScalar
ntcDvbModExtConvSpectrumInv = _NtcDvbModExtConvSpectrumInv_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 48, 4),
    _NtcDvbModExtConvSpectrumInv_Type()
)
ntcDvbModExtConvSpectrumInv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModExtConvSpectrumInv.setStatus("current")
_NtcDvbModConv_ObjectIdentity = ObjectIdentity
ntcDvbModConv = _NtcDvbModConv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 49)
)
if mibBuilder.loadTexts:
    ntcDvbModConv.setStatus("current")


class _NtcDvbModConvRfFrequency_Type(DisplayString):
    """Custom type ntcDvbModConvRfFrequency based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtcDvbModConvRfFrequency_Type.__name__ = "DisplayString"
_NtcDvbModConvRfFrequency_Object = MibScalar
ntcDvbModConvRfFrequency = _NtcDvbModConvRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 49, 1),
    _NtcDvbModConvRfFrequency_Type()
)
ntcDvbModConvRfFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModConvRfFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModConvRfFrequency.setUnits("Hz")


class _NtcDvbModConvExtLbandTx_Type(Integer32):
    """Custom type ntcDvbModConvExtLbandTx based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcDvbModConvExtLbandTx_Type.__name__ = "Integer32"
_NtcDvbModConvExtLbandTx_Object = MibScalar
ntcDvbModConvExtLbandTx = _NtcDvbModConvExtLbandTx_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 49, 2),
    _NtcDvbModConvExtLbandTx_Type()
)
ntcDvbModConvExtLbandTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModConvExtLbandTx.setStatus("current")


class _NtcDvbModConvLoFrequency_Type(DisplayString):
    """Custom type ntcDvbModConvLoFrequency based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtcDvbModConvLoFrequency_Type.__name__ = "DisplayString"
_NtcDvbModConvLoFrequency_Object = MibScalar
ntcDvbModConvLoFrequency = _NtcDvbModConvLoFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 49, 3),
    _NtcDvbModConvLoFrequency_Type()
)
ntcDvbModConvLoFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModConvLoFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModConvLoFrequency.setUnits("Hz")


class _NtcDvbModConvRfGain_Type(Integer32):
    """Custom type ntcDvbModConvRfGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_NtcDvbModConvRfGain_Type.__name__ = "Integer32"
_NtcDvbModConvRfGain_Object = MibScalar
ntcDvbModConvRfGain = _NtcDvbModConvRfGain_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 49, 4),
    _NtcDvbModConvRfGain_Type()
)
ntcDvbModConvRfGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDvbModConvRfGain.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModConvRfGain.setUnits("dB")


class _NtcDvbModConvOutputLevel_Type(Integer32):
    """Custom type ntcDvbModConvOutputLevel based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_NtcDvbModConvOutputLevel_Type.__name__ = "Integer32"
_NtcDvbModConvOutputLevel_Object = MibScalar
ntcDvbModConvOutputLevel = _NtcDvbModConvOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 49, 5),
    _NtcDvbModConvOutputLevel_Type()
)
ntcDvbModConvOutputLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModConvOutputLevel.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModConvOutputLevel.setUnits("dBm")


class _NtcDvbModExtCableLoss_Type(Integer32):
    """Custom type ntcDvbModExtCableLoss based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-990, 990),
    )


_NtcDvbModExtCableLoss_Type.__name__ = "Integer32"
_NtcDvbModExtCableLoss_Object = MibScalar
ntcDvbModExtCableLoss = _NtcDvbModExtCableLoss_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 1, 50),
    _NtcDvbModExtCableLoss_Type()
)
ntcDvbModExtCableLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModExtCableLoss.setStatus("current")
if mibBuilder.loadTexts:
    ntcDvbModExtCableLoss.setUnits("dBm")
_NtcDvbModConformance_ObjectIdentity = ObjectIdentity
ntcDvbModConformance = _NtcDvbModConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 2)
)
if mibBuilder.loadTexts:
    ntcDvbModConformance.setStatus("current")
_NtcDvbModConfCompliance_ObjectIdentity = ObjectIdentity
ntcDvbModConfCompliance = _NtcDvbModConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 2, 1)
)
if mibBuilder.loadTexts:
    ntcDvbModConfCompliance.setStatus("current")
_NtcDvbModConfGroup_ObjectIdentity = ObjectIdentity
ntcDvbModConfGroup = _NtcDvbModConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 2, 2)
)
if mibBuilder.loadTexts:
    ntcDvbModConfGroup.setStatus("current")

# Managed Objects groups

ntcDvbModConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 2, 2, 1)
)
ntcDvbModConfGrpV1Standard.setObjects(
      *(("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModMode"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModTransmit"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModTransmitState"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModTxCtrlGenDeviceAlarm"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModTxCtrlGenInterfaceAlarm"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAllowChangesWhileTxOn"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModStandbyRedundancyState"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModOutputFrequency"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModRollOff"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModOccupiedBandWidth"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModOutputBand"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModSpectrumPolarity"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModOutputLevel"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModClockOutput"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModCarrierModulation"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAmplSlopeEqualizer"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbs2FrameType"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbs2ModCod"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbs2Pilots"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbs2PhyLayerEfficiency"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbs2BbLayerEfficiency"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbs2DumPlScramblMode"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbs2PlScrambSig"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbs2RollOffSignalling"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbsModCod"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModEqlnkLinMode"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModEqlnkLinState"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModEqlnkLinInfo"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModEqlnkLinAppOutFreq"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModEqlnkLinAppRollOff"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModEqlnkLinAppSymRate"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModEqlnkNonlinMode"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModEqlnkNonlinState"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModEqlnkNonlinInfo"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModEqlnkNonlinAppOutFreq"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModEqlnkNonlinAppVersion"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmGeneralModulator"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmNoInputSignal"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmBufferUnderflow"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmBufferOverflow"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmNoInputFrameSync"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmNoBaseBandFrameSync"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmNoPhyLayerFrameSync"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmSynthFail"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmRefSynthOutOfLock"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmLo1SynthOutOfLock"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmLo2SynthOutOfLock"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmNoCalibrationData"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmDacFailure"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmBucPowerMinCurrent"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmBucPowerOverload"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmBucPowerSupply"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmBucPowerCap"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmBucPowerShortCircuit"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAlmBucPowerHardware"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModInputType"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModRfCidEnable"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModRfCidId"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModRfCidFormat"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModRfCidSendGeoCord"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModRfCidLatitude"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModRfCidLongitude"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModRfCidPhone"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModRfCidData"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModRfCidLatitudeString"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModRfCidLongitudeString"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDcBucEnable"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDcBucVoltage"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDcBucOutVoltage"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDcBucOutCurrent"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDcBucMinCurrent"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModRatePriority"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModSymbolRate"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModBitRate"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModMeasuredPktCount"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModMeasuredBitRate"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModReset"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModS2ExtModCod"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModS2ExtPhyLayerEfficiency"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModS2ExtBbLayerEfficiency"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModS2ExtDumPlScramblMode"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModS2ExtPlScrambSig"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModS2ExtRollOffSignalling"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModTurboModCod"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModTurboDeleteSync"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAmcDvbsModCod"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAmcNbcFrameType"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAmcNbcModCod"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAmcNbcPilots"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAmcNbcPLEfficiency"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAmcNbcBbLayerEfficiency"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAmcNbcPlHdrScrmSeq"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAmcNbcRollOffSignalling"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModActualOutputLevel"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModTransmitStateReason"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModLinkOptTransMode"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModMaxModulation"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDSNGProfilesProfile"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDSNGProfilesLevel"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModStreamMode"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModAmcDlModCod"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModIfOutputLevel"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModLbandOutputLevel"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModIfOutputFrequency"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModLbandOutputFrequency"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModLbandTx"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModLbandTxState"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModLbandTxStateReason"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModExtConvEnable"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModExtConvRfFrequency"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModExtConvLoFrequency"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModExtConvSpectrumInv"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModConvRfFrequency"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModConvExtLbandTx"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModConvLoFrequency"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModConvRfGain"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModConvOutputLevel"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModExtCableLoss"))
)
if mibBuilder.loadTexts:
    ntcDvbModConfGrpV1Standard.setStatus("current")

ntcDvbModConfGrpObsolete = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 2, 2, 2)
)
ntcDvbModConfGrpObsolete.setObjects(
      *(("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbs2AcmSymbolRate"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbs2Isi"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbs2RatePriority"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbs2SymbolRate"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbs2BitRate"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbs2MeasuredPktCount"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbs2MeasuredBitRate"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbs2Reset"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbsRatePriority"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbsSymbolRate"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbsBitRate"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbsMeasuredPktCount"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbsMeasuredBitRate"),
        ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModDvbsReset"))
)
if mibBuilder.loadTexts:
    ntcDvbModConfGrpObsolete.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcDvbModConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1000, 2, 1, 1)
)
ntcDvbModConfCompV1Standard.setObjects(
    ("NEWTEC-DVBMODULATOR-MIB", "ntcDvbModConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcDvbModConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-DVBMODULATOR-MIB",
    **{"ntcDvbModulator": ntcDvbModulator,
       "ntcDvbModObjects": ntcDvbModObjects,
       "ntcDvbModMode": ntcDvbModMode,
       "ntcDvbModTransmit": ntcDvbModTransmit,
       "ntcDvbModTransmitState": ntcDvbModTransmitState,
       "ntcDvbModTxCtrlGenDeviceAlarm": ntcDvbModTxCtrlGenDeviceAlarm,
       "ntcDvbModTxCtrlGenInterfaceAlarm": ntcDvbModTxCtrlGenInterfaceAlarm,
       "ntcDvbModOutputFrequency": ntcDvbModOutputFrequency,
       "ntcDvbModRollOff": ntcDvbModRollOff,
       "ntcDvbModOccupiedBandWidth": ntcDvbModOccupiedBandWidth,
       "ntcDvbModOutputBand": ntcDvbModOutputBand,
       "ntcDvbModSpectrumPolarity": ntcDvbModSpectrumPolarity,
       "ntcDvbModOutputLevel": ntcDvbModOutputLevel,
       "ntcDvbModClockOutput": ntcDvbModClockOutput,
       "ntcDvbModCarrierModulation": ntcDvbModCarrierModulation,
       "ntcDvbModAmplSlopeEqualizer": ntcDvbModAmplSlopeEqualizer,
       "ntcDvbModDvbs2Acm": ntcDvbModDvbs2Acm,
       "ntcDvbModDvbs2AcmSymbolRate": ntcDvbModDvbs2AcmSymbolRate,
       "ntcDvbModDvbs2": ntcDvbModDvbs2,
       "ntcDvbModDvbs2Isi": ntcDvbModDvbs2Isi,
       "ntcDvbModDvbs2FrameType": ntcDvbModDvbs2FrameType,
       "ntcDvbModDvbs2ModCod": ntcDvbModDvbs2ModCod,
       "ntcDvbModDvbs2Pilots": ntcDvbModDvbs2Pilots,
       "ntcDvbModDvbs2RatePriority": ntcDvbModDvbs2RatePriority,
       "ntcDvbModDvbs2SymbolRate": ntcDvbModDvbs2SymbolRate,
       "ntcDvbModDvbs2BitRate": ntcDvbModDvbs2BitRate,
       "ntcDvbModDvbs2MeasuredPktCount": ntcDvbModDvbs2MeasuredPktCount,
       "ntcDvbModDvbs2MeasuredBitRate": ntcDvbModDvbs2MeasuredBitRate,
       "ntcDvbModDvbs2PhyLayerEfficiency": ntcDvbModDvbs2PhyLayerEfficiency,
       "ntcDvbModDvbs2BbLayerEfficiency": ntcDvbModDvbs2BbLayerEfficiency,
       "ntcDvbModDvbs2DumPlScramblMode": ntcDvbModDvbs2DumPlScramblMode,
       "ntcDvbModDvbs2PlScrambSig": ntcDvbModDvbs2PlScrambSig,
       "ntcDvbModDvbs2Reset": ntcDvbModDvbs2Reset,
       "ntcDvbModDvbs2RollOffSignalling": ntcDvbModDvbs2RollOffSignalling,
       "ntcDvbModDvbs": ntcDvbModDvbs,
       "ntcDvbModDvbsModCod": ntcDvbModDvbsModCod,
       "ntcDvbModDvbsRatePriority": ntcDvbModDvbsRatePriority,
       "ntcDvbModDvbsSymbolRate": ntcDvbModDvbsSymbolRate,
       "ntcDvbModDvbsBitRate": ntcDvbModDvbsBitRate,
       "ntcDvbModDvbsMeasuredPktCount": ntcDvbModDvbsMeasuredPktCount,
       "ntcDvbModDvbsMeasuredBitRate": ntcDvbModDvbsMeasuredBitRate,
       "ntcDvbModDvbsReset": ntcDvbModDvbsReset,
       "ntcDvbModEqualink": ntcDvbModEqualink,
       "ntcDvbModEqlnkLinear": ntcDvbModEqlnkLinear,
       "ntcDvbModEqlnkLinMode": ntcDvbModEqlnkLinMode,
       "ntcDvbModEqlnkLinState": ntcDvbModEqlnkLinState,
       "ntcDvbModEqlnkLinInfo": ntcDvbModEqlnkLinInfo,
       "ntcDvbModEqlnkLinConf": ntcDvbModEqlnkLinConf,
       "ntcDvbModEqlnkLinApp": ntcDvbModEqlnkLinApp,
       "ntcDvbModEqlnkLinAppOutFreq": ntcDvbModEqlnkLinAppOutFreq,
       "ntcDvbModEqlnkLinAppRollOff": ntcDvbModEqlnkLinAppRollOff,
       "ntcDvbModEqlnkLinAppSymRate": ntcDvbModEqlnkLinAppSymRate,
       "ntcDvbModEqlnkNonlinear": ntcDvbModEqlnkNonlinear,
       "ntcDvbModEqlnkNonlinMode": ntcDvbModEqlnkNonlinMode,
       "ntcDvbModEqlnkNonlinState": ntcDvbModEqlnkNonlinState,
       "ntcDvbModEqlnkNonlinInfo": ntcDvbModEqlnkNonlinInfo,
       "ntcDvbModEqlnkNonlinConf": ntcDvbModEqlnkNonlinConf,
       "ntcDvbModEqlnkNonlinApp": ntcDvbModEqlnkNonlinApp,
       "ntcDvbModEqlnkNonlinAppOutFreq": ntcDvbModEqlnkNonlinAppOutFreq,
       "ntcDvbModEqlnkNonlinAppVersion": ntcDvbModEqlnkNonlinAppVersion,
       "ntcDvbModAlarm": ntcDvbModAlarm,
       "ntcDvbModAlmGeneralModulator": ntcDvbModAlmGeneralModulator,
       "ntcDvbModAlmNoInputSignal": ntcDvbModAlmNoInputSignal,
       "ntcDvbModAlmBufferUnderflow": ntcDvbModAlmBufferUnderflow,
       "ntcDvbModAlmBufferOverflow": ntcDvbModAlmBufferOverflow,
       "ntcDvbModAlmNoInputFrameSync": ntcDvbModAlmNoInputFrameSync,
       "ntcDvbModAlmNoBaseBandFrameSync": ntcDvbModAlmNoBaseBandFrameSync,
       "ntcDvbModAlmNoPhyLayerFrameSync": ntcDvbModAlmNoPhyLayerFrameSync,
       "ntcDvbModAlmSynthFail": ntcDvbModAlmSynthFail,
       "ntcDvbModAlmRefSynthOutOfLock": ntcDvbModAlmRefSynthOutOfLock,
       "ntcDvbModAlmLo1SynthOutOfLock": ntcDvbModAlmLo1SynthOutOfLock,
       "ntcDvbModAlmLo2SynthOutOfLock": ntcDvbModAlmLo2SynthOutOfLock,
       "ntcDvbModAlmNoCalibrationData": ntcDvbModAlmNoCalibrationData,
       "ntcDvbModAlmDacFailure": ntcDvbModAlmDacFailure,
       "ntcDvbModAlmBucPowerMinCurrent": ntcDvbModAlmBucPowerMinCurrent,
       "ntcDvbModAlmBucPowerOverload": ntcDvbModAlmBucPowerOverload,
       "ntcDvbModAlmBucPowerSupply": ntcDvbModAlmBucPowerSupply,
       "ntcDvbModAlmBucPowerCap": ntcDvbModAlmBucPowerCap,
       "ntcDvbModAlmBucPowerShortCircuit": ntcDvbModAlmBucPowerShortCircuit,
       "ntcDvbModAlmBucPowerHardware": ntcDvbModAlmBucPowerHardware,
       "ntcDvbModInputType": ntcDvbModInputType,
       "ntcDvbModRfCid": ntcDvbModRfCid,
       "ntcDvbModRfCidEnable": ntcDvbModRfCidEnable,
       "ntcDvbModRfCidId": ntcDvbModRfCidId,
       "ntcDvbModRfCidFormat": ntcDvbModRfCidFormat,
       "ntcDvbModRfCidSendGeoCord": ntcDvbModRfCidSendGeoCord,
       "ntcDvbModRfCidLatitude": ntcDvbModRfCidLatitude,
       "ntcDvbModRfCidLongitude": ntcDvbModRfCidLongitude,
       "ntcDvbModRfCidPhone": ntcDvbModRfCidPhone,
       "ntcDvbModRfCidData": ntcDvbModRfCidData,
       "ntcDvbModRfCidLatitudeString": ntcDvbModRfCidLatitudeString,
       "ntcDvbModRfCidLongitudeString": ntcDvbModRfCidLongitudeString,
       "ntcDvbModDcBuc": ntcDvbModDcBuc,
       "ntcDvbModDcBucEnable": ntcDvbModDcBucEnable,
       "ntcDvbModDcBucVoltage": ntcDvbModDcBucVoltage,
       "ntcDvbModDcBucOutVoltage": ntcDvbModDcBucOutVoltage,
       "ntcDvbModDcBucOutCurrent": ntcDvbModDcBucOutCurrent,
       "ntcDvbModDcBucMinCurrent": ntcDvbModDcBucMinCurrent,
       "ntcDvbModRatePriority": ntcDvbModRatePriority,
       "ntcDvbModSymbolRate": ntcDvbModSymbolRate,
       "ntcDvbModBitRate": ntcDvbModBitRate,
       "ntcDvbModMeasuredPktCount": ntcDvbModMeasuredPktCount,
       "ntcDvbModMeasuredBitRate": ntcDvbModMeasuredBitRate,
       "ntcDvbModReset": ntcDvbModReset,
       "ntcDvbModS2Ext": ntcDvbModS2Ext,
       "ntcDvbModS2ExtModCod": ntcDvbModS2ExtModCod,
       "ntcDvbModS2ExtPhyLayerEfficiency": ntcDvbModS2ExtPhyLayerEfficiency,
       "ntcDvbModS2ExtBbLayerEfficiency": ntcDvbModS2ExtBbLayerEfficiency,
       "ntcDvbModS2ExtDumPlScramblMode": ntcDvbModS2ExtDumPlScramblMode,
       "ntcDvbModS2ExtPlScrambSig": ntcDvbModS2ExtPlScrambSig,
       "ntcDvbModS2ExtRollOffSignalling": ntcDvbModS2ExtRollOffSignalling,
       "ntcDvbModTurbo": ntcDvbModTurbo,
       "ntcDvbModTurboModCod": ntcDvbModTurboModCod,
       "ntcDvbModTurboDeleteSync": ntcDvbModTurboDeleteSync,
       "ntcDvbModAmcDvbs": ntcDvbModAmcDvbs,
       "ntcDvbModAmcDvbsModCod": ntcDvbModAmcDvbsModCod,
       "ntcDvbModAmcNbc": ntcDvbModAmcNbc,
       "ntcDvbModAmcNbcFrameType": ntcDvbModAmcNbcFrameType,
       "ntcDvbModAmcNbcModCod": ntcDvbModAmcNbcModCod,
       "ntcDvbModAmcNbcPilots": ntcDvbModAmcNbcPilots,
       "ntcDvbModAmcNbcPLEfficiency": ntcDvbModAmcNbcPLEfficiency,
       "ntcDvbModAmcNbcBbLayerEfficiency": ntcDvbModAmcNbcBbLayerEfficiency,
       "ntcDvbModAmcNbcPlHdrScrmSeq": ntcDvbModAmcNbcPlHdrScrmSeq,
       "ntcDvbModAmcNbcRollOffSignalling": ntcDvbModAmcNbcRollOffSignalling,
       "ntcDvbModActualOutputLevel": ntcDvbModActualOutputLevel,
       "ntcDvbModTransmitStateReason": ntcDvbModTransmitStateReason,
       "ntcDvbModLinkOpt": ntcDvbModLinkOpt,
       "ntcDvbModLinkOptTransMode": ntcDvbModLinkOptTransMode,
       "ntcDvbModMaxModulation": ntcDvbModMaxModulation,
       "ntcDvbModAllowChangesWhileTxOn": ntcDvbModAllowChangesWhileTxOn,
       "ntcDvbModStandbyRedundancyState": ntcDvbModStandbyRedundancyState,
       "ntcDvbModDSNGProfiles": ntcDvbModDSNGProfiles,
       "ntcDvbModDSNGProfilesProfile": ntcDvbModDSNGProfilesProfile,
       "ntcDvbModDSNGProfilesLevel": ntcDvbModDSNGProfilesLevel,
       "ntcDvbModStreamMode": ntcDvbModStreamMode,
       "ntcDvbModAmcDl": ntcDvbModAmcDl,
       "ntcDvbModAmcDlModCod": ntcDvbModAmcDlModCod,
       "ntcDvbModIfOutputLevel": ntcDvbModIfOutputLevel,
       "ntcDvbModLbandOutputLevel": ntcDvbModLbandOutputLevel,
       "ntcDvbModIfOutputFrequency": ntcDvbModIfOutputFrequency,
       "ntcDvbModLbandOutputFrequency": ntcDvbModLbandOutputFrequency,
       "ntcDvbModLbandTx": ntcDvbModLbandTx,
       "ntcDvbModLbandTxState": ntcDvbModLbandTxState,
       "ntcDvbModLbandTxStateReason": ntcDvbModLbandTxStateReason,
       "ntcDvbModExtConv": ntcDvbModExtConv,
       "ntcDvbModExtConvEnable": ntcDvbModExtConvEnable,
       "ntcDvbModExtConvRfFrequency": ntcDvbModExtConvRfFrequency,
       "ntcDvbModExtConvLoFrequency": ntcDvbModExtConvLoFrequency,
       "ntcDvbModExtConvSpectrumInv": ntcDvbModExtConvSpectrumInv,
       "ntcDvbModConv": ntcDvbModConv,
       "ntcDvbModConvRfFrequency": ntcDvbModConvRfFrequency,
       "ntcDvbModConvExtLbandTx": ntcDvbModConvExtLbandTx,
       "ntcDvbModConvLoFrequency": ntcDvbModConvLoFrequency,
       "ntcDvbModConvRfGain": ntcDvbModConvRfGain,
       "ntcDvbModConvOutputLevel": ntcDvbModConvOutputLevel,
       "ntcDvbModExtCableLoss": ntcDvbModExtCableLoss,
       "ntcDvbModConformance": ntcDvbModConformance,
       "ntcDvbModConfCompliance": ntcDvbModConfCompliance,
       "ntcDvbModConfCompV1Standard": ntcDvbModConfCompV1Standard,
       "ntcDvbModConfGroup": ntcDvbModConfGroup,
       "ntcDvbModConfGrpV1Standard": ntcDvbModConfGrpV1Standard,
       "ntcDvbModConfGrpObsolete": ntcDvbModConfGrpObsolete}
)
