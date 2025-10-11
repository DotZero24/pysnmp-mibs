# SNMP MIB module (BACHMANN-BLUENET2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/bachmann/BACHMANN-BLUENET2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:07:25 2025
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

(bachmann,) = mibBuilder.importSymbols(
    "BACHMANN-SMI-MIB",
    "bachmann")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysObjectID,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysObjectID")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

blueNet2Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2)
)
if mibBuilder.loadTexts:
    blueNet2Mib.setRevisions(
        ("2015-07-01 00:00",
         "2015-06-01 00:00",
         "2015-02-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BlueNet2ComponentStates(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("warning", 2),
          ("alarm", 3))
    )



class BlueNet2EntitySources(TextualConvention, Integer32):
    status = "current"
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
        *(("other", 1),
          ("device", 2),
          ("sensor", 3),
          ("circuit", 4),
          ("phase", 5),
          ("fuse", 6),
          ("socket", 7),
          ("socketgroup", 8),
          ("rcm", 9))
    )



class BlueNet2EntityStates(TextualConvention, Integer32):
    status = "current"
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
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45)
        )
    )
    namedValues = NamedValues(
        *(("expected", 0),
          ("undefined", 1),
          ("errorHigh", 3),
          ("errorLow", 4),
          ("warningHigh", 5),
          ("warningLow", 6),
          ("lost", 7),
          ("deactivate", 8),
          ("onAlarmIdentidy", 9),
          ("offAlarmIdentify", 10),
          ("onAlarm", 11),
          ("offAlarm", 12),
          ("onWarningIdentify", 13),
          ("offWarningIdentify", 14),
          ("onWarning", 15),
          ("offWarning", 16),
          ("onIdentify", 17),
          ("offIdentify", 18),
          ("on", 19),
          ("off", 20),
          ("onChildAlarm", 21),
          ("offChildAlarm", 22),
          ("onChildWarning", 23),
          ("offChildWarning", 24),
          ("childAlarm", 25),
          ("childWarning", 26),
          ("lostChild", 27),
          ("updateInProgress", 36),
          ("updateError", 37),
          ("onGoingSwitch", 38),
          ("high", 39),
          ("low", 40),
          ("alarm", 41),
          ("warning", 42),
          ("ok", 43),
          ("disabled", 44),
          ("fwVersionTooNew", 45))
    )



class BlueNet2EntityBits(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class BlueNet2DataSourceTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              7,
              8,
              9,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
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
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              80,
              81,
              82,
              83,
              84,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("voltage", 1),
          ("peakVoltage", 2),
          ("current", 4),
          ("peakCurrent", 5),
          ("differentialCurrentAc", 7),
          ("differentialCurrentDc", 8),
          ("neutralCurrent", 9),
          ("phaseAngle", 16),
          ("powerFactor", 17),
          ("apparentPower", 18),
          ("activePower", 19),
          ("peakActivePower", 20),
          ("peakActivePowerUser", 21),
          ("reactivePower", 22),
          ("frequency", 23),
          ("peakNeutralCurrent", 24),
          ("apparentEnergyAccumulated", 32),
          ("apparentEnergyDelta", 33),
          ("reactiveEnergyAccumulated", 34),
          ("reactiveEnergyDelta", 35),
          ("activeEnergyAccumulated", 36),
          ("activeEnergyDelta", 37),
          ("activeEnergyAccumulatedUser", 38),
          ("activeEnergyRuntime", 39),
          ("customEnergyRuntimeUser", 40),
          ("fuseState", 48),
          ("orientation", 49),
          ("usb", 50),
          ("socketState", 51),
          ("pduState", 52),
          ("sensorState", 53),
          ("circuitState", 54),
          ("phaseState", 55),
          ("rcdState", 56),
          ("socketGroupState", 57),
          ("globalState", 58),
          ("sensorType", 64),
          ("circuitType", 65),
          ("fuseType", 66),
          ("socketType", 67),
          ("socketColor", 68),
          ("phaseType", 69),
          ("pduType", 70),
          ("rcmType", 71),
          ("deltaVoltage12", 80),
          ("deltaVoltage23", 81),
          ("deltaVoltage31", 82),
          ("rcmACPeak", 83),
          ("rcmDCPeak", 84),
          ("temperature", 256),
          ("humidity", 257),
          ("ioInputChannel1", 258),
          ("ioInputChannel2", 259),
          ("ioInputChannel3", 260),
          ("ioInputChannel4", 261),
          ("ioOutputChannel1", 262),
          ("ioOutputChannel2", 263),
          ("ioOutputChannel3", 264),
          ("ioOutputChannel4", 265),
          ("dewPoint", 266),
          ("pressure", 267),
          ("diffPressure", 268),
          ("co2Equivalent", 269),
          ("tvoc", 270),
          ("unspecified", 65535))
    )



class BlueNet2DataSourceUnits(TextualConvention, Integer32):
    status = "current"
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
              16,
              17,
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
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              255)
        )
    )
    namedValues = NamedValues(
        *(("metre", 1),
          ("kilogram", 2),
          ("second", 3),
          ("ampere", 4),
          ("kelvin", 5),
          ("mole", 6),
          ("candela", 7),
          ("radian", 16),
          ("steradian", 17),
          ("hertz", 32),
          ("newton", 33),
          ("pascal", 34),
          ("joule", 35),
          ("watt", 36),
          ("coulomb", 37),
          ("volt", 38),
          ("farad", 39),
          ("ohm", 40),
          ("siemens", 41),
          ("weber", 42),
          ("tesla", 43),
          ("henry", 44),
          ("celsius", 45),
          ("lumen", 46),
          ("lux", 47),
          ("becquerel", 48),
          ("gray", 49),
          ("sievert", 50),
          ("katal", 51),
          ("grade", 64),
          ("degree", 65),
          ("aMinuteAngle", 66),
          ("aSecondAngle", 67),
          ("litre", 68),
          ("are", 69),
          ("hectare", 70),
          ("minute", 71),
          ("hour", 72),
          ("day", 73),
          ("year", 74),
          ("gram", 75),
          ("tonne", 76),
          ("bar", 78),
          ("poise", 79),
          ("stokes", 80),
          ("electronvolt", 81),
          ("atomicMass", 82),
          ("astronomic", 83),
          ("parsec", 84),
          ("metrePerS2", 85),
          ("newtonMetre", 86),
          ("s2", 87),
          ("m2", 88),
          ("m3", 89),
          ("pascalSecond", 90),
          ("jPerKgK", 91),
          ("wPerMK", 92),
          ("jPerMoleK", 93),
          ("wPerM2Sr", 94),
          ("katPerM3", 95),
          ("kiloWattHour", 240),
          ("percentage", 241),
          ("va", 242),
          ("var", 243),
          ("kiloVaHour", 244),
          ("kiloVarHour", 245),
          ("milliAmpere", 246),
          ("unit", 255))
    )



class BlueNet2InfoMessageSources(TextualConvention, Integer32):
    status = "current"
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
        *(("other", 1),
          ("device", 2),
          ("sensor", 3),
          ("variable", 4))
    )



class BlueNet2SocketModes(TextualConvention, Integer32):
    status = "current"
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
        *(("switchedOn", 1),
          ("switchedOff", 2),
          ("switchedOnAndOff", 3),
          ("notAvailable", 4),
          ("notSwitchable", 5))
    )



class BlueNet2SocketMembers(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class BlueNet2GPIOModes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 2),
          ("s0", 6),
          ("undefined", 7))
    )



class BlueNet2GPIOSwitch(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2),
          ("switchable", 3),
          ("notSwitchable", 5))
    )



class BlueNet2RcmSelftestCommand(TextualConvention, Integer32):
    status = "current"
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
        *(("selftestWithoutAnyNotification", 0),
          ("selftestWithAlarmNotifyOnly", 1),
          ("selftestWithSelftestNotifyOnly", 2),
          ("selftestWithAlarmAndSelftestNotify", 3),
          ("selftestCommand", 4))
    )



class BlueNet2RcmSelftestResult(TextualConvention, Integer32):
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("notRun", 0),
          ("notReachable", 1),
          ("success", 2),
          ("failure", 3),
          ("partialSuccess", 4),
          ("cancelled", 5),
          ("notApplicable", 255))
    )



# MIB Managed Objects in the order of their OIDs

_BlueNet2Notifications_ObjectIdentity = ObjectIdentity
blueNet2Notifications = _BlueNet2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 0)
)
_BlueNet2NotificationPrefix_ObjectIdentity = ObjectIdentity
blueNet2NotificationPrefix = _BlueNet2NotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 0, 0)
)
_BlueNet2Products_ObjectIdentity = ObjectIdentity
blueNet2Products = _BlueNet2Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 1)
)
_BlueNet2Objects_ObjectIdentity = ObjectIdentity
blueNet2Objects = _BlueNet2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2)
)
_BlueNet2Identification_ObjectIdentity = ObjectIdentity
blueNet2Identification = _BlueNet2Identification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 1)
)


class _BlueNet2IdProductVendor_Type(DisplayString):
    """Custom type blueNet2IdProductVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2IdProductVendor_Type.__name__ = "DisplayString"
_BlueNet2IdProductVendor_Object = MibScalar
blueNet2IdProductVendor = _BlueNet2IdProductVendor_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 1, 1),
    _BlueNet2IdProductVendor_Type()
)
blueNet2IdProductVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2IdProductVendor.setStatus("current")


class _BlueNet2IdProductName_Type(DisplayString):
    """Custom type blueNet2IdProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2IdProductName_Type.__name__ = "DisplayString"
_BlueNet2IdProductName_Object = MibScalar
blueNet2IdProductName = _BlueNet2IdProductName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 1, 2),
    _BlueNet2IdProductName_Type()
)
blueNet2IdProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2IdProductName.setStatus("current")


class _BlueNet2IdProductURI_Type(DisplayString):
    """Custom type blueNet2IdProductURI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2IdProductURI_Type.__name__ = "DisplayString"
_BlueNet2IdProductURI_Object = MibScalar
blueNet2IdProductURI = _BlueNet2IdProductURI_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 1, 3),
    _BlueNet2IdProductURI_Type()
)
blueNet2IdProductURI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2IdProductURI.setStatus("current")


class _BlueNet2IdProductPartNr_Type(DisplayString):
    """Custom type blueNet2IdProductPartNr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2IdProductPartNr_Type.__name__ = "DisplayString"
_BlueNet2IdProductPartNr_Object = MibScalar
blueNet2IdProductPartNr = _BlueNet2IdProductPartNr_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 1, 4),
    _BlueNet2IdProductPartNr_Type()
)
blueNet2IdProductPartNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2IdProductPartNr.setStatus("current")


class _BlueNet2IdProductSNr_Type(DisplayString):
    """Custom type blueNet2IdProductSNr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2IdProductSNr_Type.__name__ = "DisplayString"
_BlueNet2IdProductSNr_Object = MibScalar
blueNet2IdProductSNr = _BlueNet2IdProductSNr_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 1, 5),
    _BlueNet2IdProductSNr_Type()
)
blueNet2IdProductSNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2IdProductSNr.setStatus("current")


class _BlueNet2IdProductDate_Type(DisplayString):
    """Custom type blueNet2IdProductDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2IdProductDate_Type.__name__ = "DisplayString"
_BlueNet2IdProductDate_Object = MibScalar
blueNet2IdProductDate = _BlueNet2IdProductDate_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 1, 6),
    _BlueNet2IdProductDate_Type()
)
blueNet2IdProductDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2IdProductDate.setStatus("current")


class _BlueNet2IdProductFacility_Type(Integer32):
    """Custom type blueNet2IdProductFacility based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("neutralCurrent", 0),
          ("fuse", 1),
          ("rcd", 2),
          ("identify", 3),
          ("switch", 4),
          ("oneInlet", 5),
          ("monitoredPerOutlet", 6),
          ("monitoredPerPhase", 7),
          ("spd", 8))
    )


_BlueNet2IdProductFacility_Type.__name__ = "Integer32"
_BlueNet2IdProductFacility_Object = MibScalar
blueNet2IdProductFacility = _BlueNet2IdProductFacility_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 1, 7),
    _BlueNet2IdProductFacility_Type()
)
blueNet2IdProductFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2IdProductFacility.setStatus("current")
_BlueNet2IdProductCaps_Type = Unsigned32
_BlueNet2IdProductCaps_Object = MibScalar
blueNet2IdProductCaps = _BlueNet2IdProductCaps_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 1, 8),
    _BlueNet2IdProductCaps_Type()
)
blueNet2IdProductCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2IdProductCaps.setStatus("current")


class _BlueNet2IdProductFwV_Type(DisplayString):
    """Custom type blueNet2IdProductFwV based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2IdProductFwV_Type.__name__ = "DisplayString"
_BlueNet2IdProductFwV_Object = MibScalar
blueNet2IdProductFwV = _BlueNet2IdProductFwV_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 1, 9),
    _BlueNet2IdProductFwV_Type()
)
blueNet2IdProductFwV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2IdProductFwV.setStatus("current")


class _BlueNet2IdProductHwV_Type(DisplayString):
    """Custom type blueNet2IdProductHwV based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2IdProductHwV_Type.__name__ = "DisplayString"
_BlueNet2IdProductHwV_Object = MibScalar
blueNet2IdProductHwV = _BlueNet2IdProductHwV_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 1, 10),
    _BlueNet2IdProductHwV_Type()
)
blueNet2IdProductHwV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2IdProductHwV.setStatus("current")


class _BlueNet2IdProductSwV_Type(DisplayString):
    """Custom type blueNet2IdProductSwV based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2IdProductSwV_Type.__name__ = "DisplayString"
_BlueNet2IdProductSwV_Object = MibScalar
blueNet2IdProductSwV = _BlueNet2IdProductSwV_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 1, 11),
    _BlueNet2IdProductSwV_Type()
)
blueNet2IdProductSwV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2IdProductSwV.setStatus("current")


class _BlueNet2IdProductOsV_Type(DisplayString):
    """Custom type blueNet2IdProductOsV based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2IdProductOsV_Type.__name__ = "DisplayString"
_BlueNet2IdProductOsV_Object = MibScalar
blueNet2IdProductOsV = _BlueNet2IdProductOsV_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 1, 12),
    _BlueNet2IdProductOsV_Type()
)
blueNet2IdProductOsV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2IdProductOsV.setStatus("current")


class _BlueNet2IdProductArch_Type(DisplayString):
    """Custom type blueNet2IdProductArch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2IdProductArch_Type.__name__ = "DisplayString"
_BlueNet2IdProductArch_Object = MibScalar
blueNet2IdProductArch = _BlueNet2IdProductArch_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 1, 13),
    _BlueNet2IdProductArch_Type()
)
blueNet2IdProductArch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2IdProductArch.setStatus("current")


class _BlueNet2IdProductMAC_Type(DisplayString):
    """Custom type blueNet2IdProductMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2IdProductMAC_Type.__name__ = "DisplayString"
_BlueNet2IdProductMAC_Object = MibScalar
blueNet2IdProductMAC = _BlueNet2IdProductMAC_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 1, 14),
    _BlueNet2IdProductMAC_Type()
)
blueNet2IdProductMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2IdProductMAC.setStatus("current")
_BlueNet2Information_ObjectIdentity = ObjectIdentity
blueNet2Information = _BlueNet2Information_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2)
)
_BlueNet2InfoUpTime_Type = Unsigned32
_BlueNet2InfoUpTime_Object = MibScalar
blueNet2InfoUpTime = _BlueNet2InfoUpTime_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2, 1),
    _BlueNet2InfoUpTime_Type()
)
blueNet2InfoUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2InfoUpTime.setStatus("current")
_BlueNet2InfoOverallStatus_Type = BlueNet2ComponentStates
_BlueNet2InfoOverallStatus_Object = MibScalar
blueNet2InfoOverallStatus = _BlueNet2InfoOverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2, 2),
    _BlueNet2InfoOverallStatus_Type()
)
blueNet2InfoOverallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2InfoOverallStatus.setStatus("current")
_BlueNet2InfoNumberOfChanges_Type = Unsigned32
_BlueNet2InfoNumberOfChanges_Object = MibScalar
blueNet2InfoNumberOfChanges = _BlueNet2InfoNumberOfChanges_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2, 3),
    _BlueNet2InfoNumberOfChanges_Type()
)
blueNet2InfoNumberOfChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2InfoNumberOfChanges.setStatus("current")
_BlueNet2InfoLastChange_Type = TimeTicks
_BlueNet2InfoLastChange_Object = MibScalar
blueNet2InfoLastChange = _BlueNet2InfoLastChange_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2, 4),
    _BlueNet2InfoLastChange_Type()
)
blueNet2InfoLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2InfoLastChange.setStatus("current")
_BlueNet2InfoAccumulatedStatus_Type = BlueNet2EntityBits
_BlueNet2InfoAccumulatedStatus_Object = MibScalar
blueNet2InfoAccumulatedStatus = _BlueNet2InfoAccumulatedStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2, 5),
    _BlueNet2InfoAccumulatedStatus_Type()
)
blueNet2InfoAccumulatedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2InfoAccumulatedStatus.setStatus("current")
_BlueNet2InfoLoadTable_Object = MibTable
blueNet2InfoLoadTable = _BlueNet2InfoLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2, 6)
)
if mibBuilder.loadTexts:
    blueNet2InfoLoadTable.setStatus("current")
_BlueNet2InfoLoadEntry_Object = MibTableRow
blueNet2InfoLoadEntry = _BlueNet2InfoLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2, 6, 1)
)
blueNet2InfoLoadEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2InfoLoadIndex"),
)
if mibBuilder.loadTexts:
    blueNet2InfoLoadEntry.setStatus("current")


class _BlueNet2InfoLoadIndex_Type(Unsigned32):
    """Custom type blueNet2InfoLoadIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BlueNet2InfoLoadIndex_Type.__name__ = "Unsigned32"
_BlueNet2InfoLoadIndex_Object = MibTableColumn
blueNet2InfoLoadIndex = _BlueNet2InfoLoadIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2, 6, 1, 1),
    _BlueNet2InfoLoadIndex_Type()
)
blueNet2InfoLoadIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2InfoLoadIndex.setStatus("current")
_BlueNet2InfoLoadAverage_Type = Unsigned32
_BlueNet2InfoLoadAverage_Object = MibTableColumn
blueNet2InfoLoadAverage = _BlueNet2InfoLoadAverage_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2, 6, 1, 2),
    _BlueNet2InfoLoadAverage_Type()
)
blueNet2InfoLoadAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2InfoLoadAverage.setStatus("current")
_BlueNet2InfoMessageTable_Object = MibTable
blueNet2InfoMessageTable = _BlueNet2InfoMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2, 7)
)
if mibBuilder.loadTexts:
    blueNet2InfoMessageTable.setStatus("current")
_BlueNet2InfoMessageEntry_Object = MibTableRow
blueNet2InfoMessageEntry = _BlueNet2InfoMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2, 7, 1)
)
blueNet2InfoMessageEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2InfoMessageSource"),
)
if mibBuilder.loadTexts:
    blueNet2InfoMessageEntry.setStatus("current")
_BlueNet2InfoMessageSource_Type = BlueNet2InfoMessageSources
_BlueNet2InfoMessageSource_Object = MibTableColumn
blueNet2InfoMessageSource = _BlueNet2InfoMessageSource_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2, 7, 1, 1),
    _BlueNet2InfoMessageSource_Type()
)
blueNet2InfoMessageSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2InfoMessageSource.setStatus("current")
_BlueNet2InfoMessageStatus_Type = BlueNet2ComponentStates
_BlueNet2InfoMessageStatus_Object = MibTableColumn
blueNet2InfoMessageStatus = _BlueNet2InfoMessageStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2, 7, 1, 2),
    _BlueNet2InfoMessageStatus_Type()
)
blueNet2InfoMessageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2InfoMessageStatus.setStatus("current")
_BlueNet2InfoMessageTime_Type = TimeTicks
_BlueNet2InfoMessageTime_Object = MibTableColumn
blueNet2InfoMessageTime = _BlueNet2InfoMessageTime_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2, 7, 1, 3),
    _BlueNet2InfoMessageTime_Type()
)
blueNet2InfoMessageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2InfoMessageTime.setStatus("current")


class _BlueNet2InfoMessageText_Type(DisplayString):
    """Custom type blueNet2InfoMessageText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2InfoMessageText_Type.__name__ = "DisplayString"
_BlueNet2InfoMessageText_Object = MibTableColumn
blueNet2InfoMessageText = _BlueNet2InfoMessageText_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2, 7, 1, 4),
    _BlueNet2InfoMessageText_Type()
)
blueNet2InfoMessageText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2InfoMessageText.setStatus("current")
_BlueNet2InfoMessageNumberOfOks_Type = Unsigned32
_BlueNet2InfoMessageNumberOfOks_Object = MibTableColumn
blueNet2InfoMessageNumberOfOks = _BlueNet2InfoMessageNumberOfOks_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2, 7, 1, 5),
    _BlueNet2InfoMessageNumberOfOks_Type()
)
blueNet2InfoMessageNumberOfOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2InfoMessageNumberOfOks.setStatus("current")
_BlueNet2InfoMessageNumberOfWarnings_Type = Unsigned32
_BlueNet2InfoMessageNumberOfWarnings_Object = MibTableColumn
blueNet2InfoMessageNumberOfWarnings = _BlueNet2InfoMessageNumberOfWarnings_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2, 7, 1, 6),
    _BlueNet2InfoMessageNumberOfWarnings_Type()
)
blueNet2InfoMessageNumberOfWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2InfoMessageNumberOfWarnings.setStatus("current")
_BlueNet2InfoMessageNumberOfErrors_Type = Unsigned32
_BlueNet2InfoMessageNumberOfErrors_Object = MibTableColumn
blueNet2InfoMessageNumberOfErrors = _BlueNet2InfoMessageNumberOfErrors_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 2, 7, 1, 7),
    _BlueNet2InfoMessageNumberOfErrors_Type()
)
blueNet2InfoMessageNumberOfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2InfoMessageNumberOfErrors.setStatus("current")
_BlueNet2Configuration_ObjectIdentity = ObjectIdentity
blueNet2Configuration = _BlueNet2Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3)
)


class _BlueNet2Alias_Type(DisplayString):
    """Custom type blueNet2Alias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2Alias_Type.__name__ = "DisplayString"
_BlueNet2Alias_Object = MibScalar
blueNet2Alias = _BlueNet2Alias_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 1),
    _BlueNet2Alias_Type()
)
blueNet2Alias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2Alias.setStatus("current")


class _BlueNet2Language_Type(Integer32):
    """Custom type blueNet2Language based on Integer32"""
    defaultValue = 2

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
        *(("other", 1),
          ("english", 2),
          ("german", 3),
          ("french", 4))
    )


_BlueNet2Language_Type.__name__ = "Integer32"
_BlueNet2Language_Object = MibScalar
blueNet2Language = _BlueNet2Language_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 2),
    _BlueNet2Language_Type()
)
blueNet2Language.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2Language.setStatus("deprecated")
_BlueNet2DateTime_Type = DateAndTime
_BlueNet2DateTime_Object = MibScalar
blueNet2DateTime = _BlueNet2DateTime_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 3),
    _BlueNet2DateTime_Type()
)
blueNet2DateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2DateTime.setStatus("current")
_BlueNet2Protocols_ObjectIdentity = ObjectIdentity
blueNet2Protocols = _BlueNet2Protocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4)
)


class _BlueNet2FtpAccess_Type(Integer32):
    """Custom type blueNet2FtpAccess based on Integer32"""
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


_BlueNet2FtpAccess_Type.__name__ = "Integer32"
_BlueNet2FtpAccess_Object = MibScalar
blueNet2FtpAccess = _BlueNet2FtpAccess_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 1),
    _BlueNet2FtpAccess_Type()
)
blueNet2FtpAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2FtpAccess.setStatus("current")


class _BlueNet2FtpPort_Type(Unsigned32):
    """Custom type blueNet2FtpPort based on Unsigned32"""
    defaultValue = 21

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BlueNet2FtpPort_Type.__name__ = "Unsigned32"
_BlueNet2FtpPort_Object = MibScalar
blueNet2FtpPort = _BlueNet2FtpPort_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 2),
    _BlueNet2FtpPort_Type()
)
blueNet2FtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2FtpPort.setStatus("current")


class _BlueNet2HttpAccess_Type(Bits):
    """Custom type blueNet2HttpAccess based on Bits"""
    defaultBinValue = "01"

    namedValues = NamedValues(
        *(("httpEnabled", 0),
          ("httpsEnabled", 1))
    )

_BlueNet2HttpAccess_Type.__name__ = "Bits"
_BlueNet2HttpAccess_Object = MibScalar
blueNet2HttpAccess = _BlueNet2HttpAccess_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 3),
    _BlueNet2HttpAccess_Type()
)
blueNet2HttpAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2HttpAccess.setStatus("current")


class _BlueNet2HttpPort_Type(Unsigned32):
    """Custom type blueNet2HttpPort based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BlueNet2HttpPort_Type.__name__ = "Unsigned32"
_BlueNet2HttpPort_Object = MibScalar
blueNet2HttpPort = _BlueNet2HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 4),
    _BlueNet2HttpPort_Type()
)
blueNet2HttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2HttpPort.setStatus("current")


class _BlueNet2HttpsPort_Type(Unsigned32):
    """Custom type blueNet2HttpsPort based on Unsigned32"""
    defaultValue = 443

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BlueNet2HttpsPort_Type.__name__ = "Unsigned32"
_BlueNet2HttpsPort_Object = MibScalar
blueNet2HttpsPort = _BlueNet2HttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 5),
    _BlueNet2HttpsPort_Type()
)
blueNet2HttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2HttpsPort.setStatus("current")


class _BlueNet2SftpAccess_Type(Integer32):
    """Custom type blueNet2SftpAccess based on Integer32"""
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


_BlueNet2SftpAccess_Type.__name__ = "Integer32"
_BlueNet2SftpAccess_Object = MibScalar
blueNet2SftpAccess = _BlueNet2SftpAccess_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 6),
    _BlueNet2SftpAccess_Type()
)
blueNet2SftpAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SftpAccess.setStatus("deprecated")


class _BlueNet2SftpPort_Type(Unsigned32):
    """Custom type blueNet2SftpPort based on Unsigned32"""
    defaultValue = 115

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BlueNet2SftpPort_Type.__name__ = "Unsigned32"
_BlueNet2SftpPort_Object = MibScalar
blueNet2SftpPort = _BlueNet2SftpPort_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 7),
    _BlueNet2SftpPort_Type()
)
blueNet2SftpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SftpPort.setStatus("deprecated")


class _BlueNet2SshAccess_Type(Integer32):
    """Custom type blueNet2SshAccess based on Integer32"""
    defaultValue = 2

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


_BlueNet2SshAccess_Type.__name__ = "Integer32"
_BlueNet2SshAccess_Object = MibScalar
blueNet2SshAccess = _BlueNet2SshAccess_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 8),
    _BlueNet2SshAccess_Type()
)
blueNet2SshAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SshAccess.setStatus("current")


class _BlueNet2SshPort_Type(Unsigned32):
    """Custom type blueNet2SshPort based on Unsigned32"""
    defaultValue = 22

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BlueNet2SshPort_Type.__name__ = "Unsigned32"
_BlueNet2SshPort_Object = MibScalar
blueNet2SshPort = _BlueNet2SshPort_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 9),
    _BlueNet2SshPort_Type()
)
blueNet2SshPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SshPort.setStatus("current")


class _BlueNet2TelnetAccess_Type(Integer32):
    """Custom type blueNet2TelnetAccess based on Integer32"""
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


_BlueNet2TelnetAccess_Type.__name__ = "Integer32"
_BlueNet2TelnetAccess_Object = MibScalar
blueNet2TelnetAccess = _BlueNet2TelnetAccess_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 10),
    _BlueNet2TelnetAccess_Type()
)
blueNet2TelnetAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2TelnetAccess.setStatus("deprecated")


class _BlueNet2TelnetPort_Type(Unsigned32):
    """Custom type blueNet2TelnetPort based on Unsigned32"""
    defaultValue = 23

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BlueNet2TelnetPort_Type.__name__ = "Unsigned32"
_BlueNet2TelnetPort_Object = MibScalar
blueNet2TelnetPort = _BlueNet2TelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 11),
    _BlueNet2TelnetPort_Type()
)
blueNet2TelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2TelnetPort.setStatus("deprecated")
_BlueNet2Snmp_ObjectIdentity = ObjectIdentity
blueNet2Snmp = _BlueNet2Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 12)
)


class _BlueNet2SnmpVersions_Type(Bits):
    """Custom type blueNet2SnmpVersions based on Bits"""
    defaultBinValue = "111"

    namedValues = NamedValues(
        *(("snmpv1", 0),
          ("snmpv2c", 1),
          ("snmpv3", 2))
    )

_BlueNet2SnmpVersions_Type.__name__ = "Bits"
_BlueNet2SnmpVersions_Object = MibScalar
blueNet2SnmpVersions = _BlueNet2SnmpVersions_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 12, 1),
    _BlueNet2SnmpVersions_Type()
)
blueNet2SnmpVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SnmpVersions.setStatus("current")


class _BlueNet2MaxTrapReceivers_Type(Unsigned32):
    """Custom type blueNet2MaxTrapReceivers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_BlueNet2MaxTrapReceivers_Type.__name__ = "Unsigned32"
_BlueNet2MaxTrapReceivers_Object = MibScalar
blueNet2MaxTrapReceivers = _BlueNet2MaxTrapReceivers_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 12, 2),
    _BlueNet2MaxTrapReceivers_Type()
)
blueNet2MaxTrapReceivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2MaxTrapReceivers.setStatus("current")
_BlueNet2TrapReceiverTable_Object = MibTable
blueNet2TrapReceiverTable = _BlueNet2TrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 12, 3)
)
if mibBuilder.loadTexts:
    blueNet2TrapReceiverTable.setStatus("current")
_BlueNet2TrapReceiverEntry_Object = MibTableRow
blueNet2TrapReceiverEntry = _BlueNet2TrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 12, 3, 1)
)
blueNet2TrapReceiverEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2TrapReceiverIndex"),
)
if mibBuilder.loadTexts:
    blueNet2TrapReceiverEntry.setStatus("current")


class _BlueNet2TrapReceiverIndex_Type(Unsigned32):
    """Custom type blueNet2TrapReceiverIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_BlueNet2TrapReceiverIndex_Type.__name__ = "Unsigned32"
_BlueNet2TrapReceiverIndex_Object = MibTableColumn
blueNet2TrapReceiverIndex = _BlueNet2TrapReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 12, 3, 1, 1),
    _BlueNet2TrapReceiverIndex_Type()
)
blueNet2TrapReceiverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2TrapReceiverIndex.setStatus("current")
_BlueNet2TrapReceiverRowStatus_Type = RowStatus
_BlueNet2TrapReceiverRowStatus_Object = MibTableColumn
blueNet2TrapReceiverRowStatus = _BlueNet2TrapReceiverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 12, 3, 1, 2),
    _BlueNet2TrapReceiverRowStatus_Type()
)
blueNet2TrapReceiverRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    blueNet2TrapReceiverRowStatus.setStatus("current")


class _BlueNet2TrapReceiverProtocol_Type(Integer32):
    """Custom type blueNet2TrapReceiverProtocol based on Integer32"""
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
        *(("snmpv1Trap", 1),
          ("snmpv2cTrap", 2),
          ("snmpv2cInform", 3),
          ("snmpv3Trap", 4),
          ("snmpv3Inform", 5))
    )


_BlueNet2TrapReceiverProtocol_Type.__name__ = "Integer32"
_BlueNet2TrapReceiverProtocol_Object = MibTableColumn
blueNet2TrapReceiverProtocol = _BlueNet2TrapReceiverProtocol_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 12, 3, 1, 3),
    _BlueNet2TrapReceiverProtocol_Type()
)
blueNet2TrapReceiverProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2TrapReceiverProtocol.setStatus("current")


class _BlueNet2TrapReceiverAddress_Type(DisplayString):
    """Custom type blueNet2TrapReceiverAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BlueNet2TrapReceiverAddress_Type.__name__ = "DisplayString"
_BlueNet2TrapReceiverAddress_Object = MibTableColumn
blueNet2TrapReceiverAddress = _BlueNet2TrapReceiverAddress_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 12, 3, 1, 4),
    _BlueNet2TrapReceiverAddress_Type()
)
blueNet2TrapReceiverAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2TrapReceiverAddress.setStatus("current")


class _BlueNet2TrapReceiverFriendlyName_Type(DisplayString):
    """Custom type blueNet2TrapReceiverFriendlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BlueNet2TrapReceiverFriendlyName_Type.__name__ = "DisplayString"
_BlueNet2TrapReceiverFriendlyName_Object = MibTableColumn
blueNet2TrapReceiverFriendlyName = _BlueNet2TrapReceiverFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 12, 3, 1, 5),
    _BlueNet2TrapReceiverFriendlyName_Type()
)
blueNet2TrapReceiverFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2TrapReceiverFriendlyName.setStatus("deprecated")


class _BlueNet2TrapReceiverDescription_Type(DisplayString):
    """Custom type blueNet2TrapReceiverDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2TrapReceiverDescription_Type.__name__ = "DisplayString"
_BlueNet2TrapReceiverDescription_Object = MibTableColumn
blueNet2TrapReceiverDescription = _BlueNet2TrapReceiverDescription_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 12, 3, 1, 6),
    _BlueNet2TrapReceiverDescription_Type()
)
blueNet2TrapReceiverDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2TrapReceiverDescription.setStatus("deprecated")


class _BlueNet2TrapReceiverCommunity_Type(DisplayString):
    """Custom type blueNet2TrapReceiverCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BlueNet2TrapReceiverCommunity_Type.__name__ = "DisplayString"
_BlueNet2TrapReceiverCommunity_Object = MibTableColumn
blueNet2TrapReceiverCommunity = _BlueNet2TrapReceiverCommunity_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 12, 3, 1, 7),
    _BlueNet2TrapReceiverCommunity_Type()
)
blueNet2TrapReceiverCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2TrapReceiverCommunity.setStatus("current")


class _BlueNet2TrapReceiverUsername_Type(DisplayString):
    """Custom type blueNet2TrapReceiverUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BlueNet2TrapReceiverUsername_Type.__name__ = "DisplayString"
_BlueNet2TrapReceiverUsername_Object = MibTableColumn
blueNet2TrapReceiverUsername = _BlueNet2TrapReceiverUsername_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 12, 3, 1, 8),
    _BlueNet2TrapReceiverUsername_Type()
)
blueNet2TrapReceiverUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2TrapReceiverUsername.setStatus("current")
_BlueNet2Modbus_ObjectIdentity = ObjectIdentity
blueNet2Modbus = _BlueNet2Modbus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 13)
)


class _BlueNet2ModbusVersions_Type(Bits):
    """Custom type blueNet2ModbusVersions based on Bits"""
    defaultBinValue = "01"

    namedValues = NamedValues(
        *(("rtu", 0),
          ("tcp", 1))
    )

_BlueNet2ModbusVersions_Type.__name__ = "Bits"
_BlueNet2ModbusVersions_Object = MibScalar
blueNet2ModbusVersions = _BlueNet2ModbusVersions_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 13, 1),
    _BlueNet2ModbusVersions_Type()
)
blueNet2ModbusVersions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2ModbusVersions.setStatus("current")


class _BlueNet2ModbusService_Type(Integer32):
    """Custom type blueNet2ModbusService based on Integer32"""
    defaultValue = 1

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
        *(("disabled", 1),
          ("readonly", 2),
          ("writeonly", 3),
          ("readwrite", 4))
    )


_BlueNet2ModbusService_Type.__name__ = "Integer32"
_BlueNet2ModbusService_Object = MibScalar
blueNet2ModbusService = _BlueNet2ModbusService_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 13, 2),
    _BlueNet2ModbusService_Type()
)
blueNet2ModbusService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2ModbusService.setStatus("deprecated")


class _BlueNet2ModbusTcpPort_Type(Unsigned32):
    """Custom type blueNet2ModbusTcpPort based on Unsigned32"""
    defaultValue = 502

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BlueNet2ModbusTcpPort_Type.__name__ = "Unsigned32"
_BlueNet2ModbusTcpPort_Object = MibScalar
blueNet2ModbusTcpPort = _BlueNet2ModbusTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 13, 3),
    _BlueNet2ModbusTcpPort_Type()
)
blueNet2ModbusTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2ModbusTcpPort.setStatus("current")


class _BlueNet2ModbusSerialMode_Type(DisplayString):
    """Custom type blueNet2ModbusSerialMode based on DisplayString"""
    defaultValue = OctetString("115200,8,N,1")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2ModbusSerialMode_Type.__name__ = "DisplayString"
_BlueNet2ModbusSerialMode_Object = MibScalar
blueNet2ModbusSerialMode = _BlueNet2ModbusSerialMode_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 13, 4),
    _BlueNet2ModbusSerialMode_Type()
)
blueNet2ModbusSerialMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2ModbusSerialMode.setStatus("deprecated")


class _BlueNet2MaxModbusTcpMasters_Type(Unsigned32):
    """Custom type blueNet2MaxModbusTcpMasters based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_BlueNet2MaxModbusTcpMasters_Type.__name__ = "Unsigned32"
_BlueNet2MaxModbusTcpMasters_Object = MibScalar
blueNet2MaxModbusTcpMasters = _BlueNet2MaxModbusTcpMasters_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 13, 5),
    _BlueNet2MaxModbusTcpMasters_Type()
)
blueNet2MaxModbusTcpMasters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2MaxModbusTcpMasters.setStatus("current")
_BlueNet2ModbusTcpTable_Object = MibTable
blueNet2ModbusTcpTable = _BlueNet2ModbusTcpTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 13, 6)
)
if mibBuilder.loadTexts:
    blueNet2ModbusTcpTable.setStatus("deprecated")
_BlueNet2ModbusTcpEntry_Object = MibTableRow
blueNet2ModbusTcpEntry = _BlueNet2ModbusTcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 13, 6, 1)
)
blueNet2ModbusTcpEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2ModbusTcpIndex"),
)
if mibBuilder.loadTexts:
    blueNet2ModbusTcpEntry.setStatus("deprecated")


class _BlueNet2ModbusTcpIndex_Type(Unsigned32):
    """Custom type blueNet2ModbusTcpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_BlueNet2ModbusTcpIndex_Type.__name__ = "Unsigned32"
_BlueNet2ModbusTcpIndex_Object = MibTableColumn
blueNet2ModbusTcpIndex = _BlueNet2ModbusTcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 13, 6, 1, 1),
    _BlueNet2ModbusTcpIndex_Type()
)
blueNet2ModbusTcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2ModbusTcpIndex.setStatus("deprecated")
_BlueNet2ModbusTcpRowStatus_Type = RowStatus
_BlueNet2ModbusTcpRowStatus_Object = MibTableColumn
blueNet2ModbusTcpRowStatus = _BlueNet2ModbusTcpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 13, 6, 1, 2),
    _BlueNet2ModbusTcpRowStatus_Type()
)
blueNet2ModbusTcpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    blueNet2ModbusTcpRowStatus.setStatus("deprecated")


class _BlueNet2ModbusTcpAccess_Type(Integer32):
    """Custom type blueNet2ModbusTcpAccess based on Integer32"""
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
        *(("noaccess", 1),
          ("readonly", 2),
          ("writeonly", 3),
          ("readwrite", 4))
    )


_BlueNet2ModbusTcpAccess_Type.__name__ = "Integer32"
_BlueNet2ModbusTcpAccess_Object = MibTableColumn
blueNet2ModbusTcpAccess = _BlueNet2ModbusTcpAccess_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 13, 6, 1, 3),
    _BlueNet2ModbusTcpAccess_Type()
)
blueNet2ModbusTcpAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2ModbusTcpAccess.setStatus("deprecated")


class _BlueNet2ModbusTcpMaster_Type(DisplayString):
    """Custom type blueNet2ModbusTcpMaster based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BlueNet2ModbusTcpMaster_Type.__name__ = "DisplayString"
_BlueNet2ModbusTcpMaster_Object = MibTableColumn
blueNet2ModbusTcpMaster = _BlueNet2ModbusTcpMaster_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 13, 6, 1, 4),
    _BlueNet2ModbusTcpMaster_Type()
)
blueNet2ModbusTcpMaster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2ModbusTcpMaster.setStatus("deprecated")


class _BlueNet2ModbusTcpFriendlyName_Type(DisplayString):
    """Custom type blueNet2ModbusTcpFriendlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BlueNet2ModbusTcpFriendlyName_Type.__name__ = "DisplayString"
_BlueNet2ModbusTcpFriendlyName_Object = MibTableColumn
blueNet2ModbusTcpFriendlyName = _BlueNet2ModbusTcpFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 13, 6, 1, 5),
    _BlueNet2ModbusTcpFriendlyName_Type()
)
blueNet2ModbusTcpFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2ModbusTcpFriendlyName.setStatus("deprecated")


class _BlueNet2ModbusTcpDescription_Type(DisplayString):
    """Custom type blueNet2ModbusTcpDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2ModbusTcpDescription_Type.__name__ = "DisplayString"
_BlueNet2ModbusTcpDescription_Object = MibTableColumn
blueNet2ModbusTcpDescription = _BlueNet2ModbusTcpDescription_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 13, 6, 1, 6),
    _BlueNet2ModbusTcpDescription_Type()
)
blueNet2ModbusTcpDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2ModbusTcpDescription.setStatus("deprecated")
_BlueNet2Ntp_ObjectIdentity = ObjectIdentity
blueNet2Ntp = _BlueNet2Ntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 14)
)


class _BlueNet2NtpService_Type(Integer32):
    """Custom type blueNet2NtpService based on Integer32"""
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


_BlueNet2NtpService_Type.__name__ = "Integer32"
_BlueNet2NtpService_Object = MibScalar
blueNet2NtpService = _BlueNet2NtpService_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 14, 1),
    _BlueNet2NtpService_Type()
)
blueNet2NtpService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2NtpService.setStatus("current")


class _BlueNet2NtpPort_Type(Unsigned32):
    """Custom type blueNet2NtpPort based on Unsigned32"""
    defaultValue = 123

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BlueNet2NtpPort_Type.__name__ = "Unsigned32"
_BlueNet2NtpPort_Object = MibScalar
blueNet2NtpPort = _BlueNet2NtpPort_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 14, 2),
    _BlueNet2NtpPort_Type()
)
blueNet2NtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2NtpPort.setStatus("current")


class _BlueNet2NtpTimeZone_Type(Integer32):
    """Custom type blueNet2NtpTimeZone based on Integer32"""
    defaultValue = 79

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 107),
    )


_BlueNet2NtpTimeZone_Type.__name__ = "Integer32"
_BlueNet2NtpTimeZone_Object = MibScalar
blueNet2NtpTimeZone = _BlueNet2NtpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 14, 3),
    _BlueNet2NtpTimeZone_Type()
)
blueNet2NtpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2NtpTimeZone.setStatus("current")


class _BlueNet2MaxNtpServers_Type(Unsigned32):
    """Custom type blueNet2MaxNtpServers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BlueNet2MaxNtpServers_Type.__name__ = "Unsigned32"
_BlueNet2MaxNtpServers_Object = MibScalar
blueNet2MaxNtpServers = _BlueNet2MaxNtpServers_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 14, 4),
    _BlueNet2MaxNtpServers_Type()
)
blueNet2MaxNtpServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2MaxNtpServers.setStatus("current")
_BlueNet2NtpServerTable_Object = MibTable
blueNet2NtpServerTable = _BlueNet2NtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 14, 5)
)
if mibBuilder.loadTexts:
    blueNet2NtpServerTable.setStatus("current")
_BlueNet2NtpServerEntry_Object = MibTableRow
blueNet2NtpServerEntry = _BlueNet2NtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 14, 5, 1)
)
blueNet2NtpServerEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2NtpServerIndex"),
)
if mibBuilder.loadTexts:
    blueNet2NtpServerEntry.setStatus("current")


class _BlueNet2NtpServerIndex_Type(Unsigned32):
    """Custom type blueNet2NtpServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BlueNet2NtpServerIndex_Type.__name__ = "Unsigned32"
_BlueNet2NtpServerIndex_Object = MibTableColumn
blueNet2NtpServerIndex = _BlueNet2NtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 14, 5, 1, 1),
    _BlueNet2NtpServerIndex_Type()
)
blueNet2NtpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2NtpServerIndex.setStatus("current")
_BlueNet2NtpServerRowStatus_Type = RowStatus
_BlueNet2NtpServerRowStatus_Object = MibTableColumn
blueNet2NtpServerRowStatus = _BlueNet2NtpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 14, 5, 1, 2),
    _BlueNet2NtpServerRowStatus_Type()
)
blueNet2NtpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    blueNet2NtpServerRowStatus.setStatus("current")


class _BlueNet2NtpServerAddress_Type(DisplayString):
    """Custom type blueNet2NtpServerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BlueNet2NtpServerAddress_Type.__name__ = "DisplayString"
_BlueNet2NtpServerAddress_Object = MibTableColumn
blueNet2NtpServerAddress = _BlueNet2NtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 14, 5, 1, 3),
    _BlueNet2NtpServerAddress_Type()
)
blueNet2NtpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2NtpServerAddress.setStatus("current")


class _BlueNet2NtpServerFriendlyName_Type(DisplayString):
    """Custom type blueNet2NtpServerFriendlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BlueNet2NtpServerFriendlyName_Type.__name__ = "DisplayString"
_BlueNet2NtpServerFriendlyName_Object = MibTableColumn
blueNet2NtpServerFriendlyName = _BlueNet2NtpServerFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 14, 5, 1, 4),
    _BlueNet2NtpServerFriendlyName_Type()
)
blueNet2NtpServerFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2NtpServerFriendlyName.setStatus("deprecated")


class _BlueNet2NtpServerDescription_Type(DisplayString):
    """Custom type blueNet2NtpServerDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2NtpServerDescription_Type.__name__ = "DisplayString"
_BlueNet2NtpServerDescription_Object = MibTableColumn
blueNet2NtpServerDescription = _BlueNet2NtpServerDescription_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 14, 5, 1, 5),
    _BlueNet2NtpServerDescription_Type()
)
blueNet2NtpServerDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2NtpServerDescription.setStatus("deprecated")
_BlueNet2Smtp_ObjectIdentity = ObjectIdentity
blueNet2Smtp = _BlueNet2Smtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 15)
)


class _BlueNet2SmtpService_Type(Integer32):
    """Custom type blueNet2SmtpService based on Integer32"""
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


_BlueNet2SmtpService_Type.__name__ = "Integer32"
_BlueNet2SmtpService_Object = MibScalar
blueNet2SmtpService = _BlueNet2SmtpService_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 15, 1),
    _BlueNet2SmtpService_Type()
)
blueNet2SmtpService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SmtpService.setStatus("current")


class _BlueNet2SmtpPort_Type(Unsigned32):
    """Custom type blueNet2SmtpPort based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BlueNet2SmtpPort_Type.__name__ = "Unsigned32"
_BlueNet2SmtpPort_Object = MibScalar
blueNet2SmtpPort = _BlueNet2SmtpPort_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 15, 2),
    _BlueNet2SmtpPort_Type()
)
blueNet2SmtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SmtpPort.setStatus("current")


class _BlueNet2SmtpServer_Type(DisplayString):
    """Custom type blueNet2SmtpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BlueNet2SmtpServer_Type.__name__ = "DisplayString"
_BlueNet2SmtpServer_Object = MibScalar
blueNet2SmtpServer = _BlueNet2SmtpServer_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 15, 3),
    _BlueNet2SmtpServer_Type()
)
blueNet2SmtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SmtpServer.setStatus("current")


class _BlueNet2SmtpAuth_Type(Integer32):
    """Custom type blueNet2SmtpAuth based on Integer32"""
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


_BlueNet2SmtpAuth_Type.__name__ = "Integer32"
_BlueNet2SmtpAuth_Object = MibScalar
blueNet2SmtpAuth = _BlueNet2SmtpAuth_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 15, 4),
    _BlueNet2SmtpAuth_Type()
)
blueNet2SmtpAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SmtpAuth.setStatus("current")


class _BlueNet2SmtpUsername_Type(DisplayString):
    """Custom type blueNet2SmtpUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BlueNet2SmtpUsername_Type.__name__ = "DisplayString"
_BlueNet2SmtpUsername_Object = MibScalar
blueNet2SmtpUsername = _BlueNet2SmtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 15, 5),
    _BlueNet2SmtpUsername_Type()
)
blueNet2SmtpUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SmtpUsername.setStatus("current")


class _BlueNet2SmtpPassword_Type(DisplayString):
    """Custom type blueNet2SmtpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BlueNet2SmtpPassword_Type.__name__ = "DisplayString"
_BlueNet2SmtpPassword_Object = MibScalar
blueNet2SmtpPassword = _BlueNet2SmtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 15, 6),
    _BlueNet2SmtpPassword_Type()
)
blueNet2SmtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SmtpPassword.setStatus("current")


class _BlueNet2SmtpFrom_Type(DisplayString):
    """Custom type blueNet2SmtpFrom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BlueNet2SmtpFrom_Type.__name__ = "DisplayString"
_BlueNet2SmtpFrom_Object = MibScalar
blueNet2SmtpFrom = _BlueNet2SmtpFrom_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 15, 7),
    _BlueNet2SmtpFrom_Type()
)
blueNet2SmtpFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SmtpFrom.setStatus("current")


class _BlueNet2SmtpReply_Type(DisplayString):
    """Custom type blueNet2SmtpReply based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BlueNet2SmtpReply_Type.__name__ = "DisplayString"
_BlueNet2SmtpReply_Object = MibScalar
blueNet2SmtpReply = _BlueNet2SmtpReply_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 15, 8),
    _BlueNet2SmtpReply_Type()
)
blueNet2SmtpReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SmtpReply.setStatus("current")


class _BlueNet2MaxSmtpReceivers_Type(Unsigned32):
    """Custom type blueNet2MaxSmtpReceivers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_BlueNet2MaxSmtpReceivers_Type.__name__ = "Unsigned32"
_BlueNet2MaxSmtpReceivers_Object = MibScalar
blueNet2MaxSmtpReceivers = _BlueNet2MaxSmtpReceivers_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 15, 9),
    _BlueNet2MaxSmtpReceivers_Type()
)
blueNet2MaxSmtpReceivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2MaxSmtpReceivers.setStatus("current")
_BlueNet2SmtpReceiverTable_Object = MibTable
blueNet2SmtpReceiverTable = _BlueNet2SmtpReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 15, 10)
)
if mibBuilder.loadTexts:
    blueNet2SmtpReceiverTable.setStatus("deprecated")
_BlueNet2SmtpReceiverEntry_Object = MibTableRow
blueNet2SmtpReceiverEntry = _BlueNet2SmtpReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 15, 10, 1)
)
blueNet2SmtpReceiverEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2SmtpReceiverIndex"),
)
if mibBuilder.loadTexts:
    blueNet2SmtpReceiverEntry.setStatus("deprecated")


class _BlueNet2SmtpReceiverIndex_Type(Unsigned32):
    """Custom type blueNet2SmtpReceiverIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_BlueNet2SmtpReceiverIndex_Type.__name__ = "Unsigned32"
_BlueNet2SmtpReceiverIndex_Object = MibTableColumn
blueNet2SmtpReceiverIndex = _BlueNet2SmtpReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 15, 10, 1, 1),
    _BlueNet2SmtpReceiverIndex_Type()
)
blueNet2SmtpReceiverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SmtpReceiverIndex.setStatus("deprecated")
_BlueNet2SmtpReceiverRowStatus_Type = RowStatus
_BlueNet2SmtpReceiverRowStatus_Object = MibTableColumn
blueNet2SmtpReceiverRowStatus = _BlueNet2SmtpReceiverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 15, 10, 1, 2),
    _BlueNet2SmtpReceiverRowStatus_Type()
)
blueNet2SmtpReceiverRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    blueNet2SmtpReceiverRowStatus.setStatus("deprecated")


class _BlueNet2SmtpReceiverAddress_Type(DisplayString):
    """Custom type blueNet2SmtpReceiverAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BlueNet2SmtpReceiverAddress_Type.__name__ = "DisplayString"
_BlueNet2SmtpReceiverAddress_Object = MibTableColumn
blueNet2SmtpReceiverAddress = _BlueNet2SmtpReceiverAddress_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 15, 10, 1, 3),
    _BlueNet2SmtpReceiverAddress_Type()
)
blueNet2SmtpReceiverAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SmtpReceiverAddress.setStatus("deprecated")


class _BlueNet2SmtpReceiverFriendlyName_Type(DisplayString):
    """Custom type blueNet2SmtpReceiverFriendlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BlueNet2SmtpReceiverFriendlyName_Type.__name__ = "DisplayString"
_BlueNet2SmtpReceiverFriendlyName_Object = MibTableColumn
blueNet2SmtpReceiverFriendlyName = _BlueNet2SmtpReceiverFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 15, 10, 1, 4),
    _BlueNet2SmtpReceiverFriendlyName_Type()
)
blueNet2SmtpReceiverFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SmtpReceiverFriendlyName.setStatus("deprecated")


class _BlueNet2SmtpReceiverDescription_Type(DisplayString):
    """Custom type blueNet2SmtpReceiverDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2SmtpReceiverDescription_Type.__name__ = "DisplayString"
_BlueNet2SmtpReceiverDescription_Object = MibTableColumn
blueNet2SmtpReceiverDescription = _BlueNet2SmtpReceiverDescription_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 15, 10, 1, 5),
    _BlueNet2SmtpReceiverDescription_Type()
)
blueNet2SmtpReceiverDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SmtpReceiverDescription.setStatus("deprecated")
_BlueNet2Syslog_ObjectIdentity = ObjectIdentity
blueNet2Syslog = _BlueNet2Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 16)
)


class _BlueNet2SyslogService_Type(Integer32):
    """Custom type blueNet2SyslogService based on Integer32"""
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


_BlueNet2SyslogService_Type.__name__ = "Integer32"
_BlueNet2SyslogService_Object = MibScalar
blueNet2SyslogService = _BlueNet2SyslogService_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 16, 1),
    _BlueNet2SyslogService_Type()
)
blueNet2SyslogService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SyslogService.setStatus("current")


class _BlueNet2SyslogFacility_Type(Integer32):
    """Custom type blueNet2SyslogFacility based on Integer32"""
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
        *(("local0", 1),
          ("local1", 2),
          ("local2", 3),
          ("local3", 4),
          ("local4", 5),
          ("local5", 6),
          ("local6", 7),
          ("local7", 8))
    )


_BlueNet2SyslogFacility_Type.__name__ = "Integer32"
_BlueNet2SyslogFacility_Object = MibScalar
blueNet2SyslogFacility = _BlueNet2SyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 16, 2),
    _BlueNet2SyslogFacility_Type()
)
blueNet2SyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SyslogFacility.setStatus("current")


class _BlueNet2MaxSyslogServers_Type(Unsigned32):
    """Custom type blueNet2MaxSyslogServers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BlueNet2MaxSyslogServers_Type.__name__ = "Unsigned32"
_BlueNet2MaxSyslogServers_Object = MibScalar
blueNet2MaxSyslogServers = _BlueNet2MaxSyslogServers_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 16, 3),
    _BlueNet2MaxSyslogServers_Type()
)
blueNet2MaxSyslogServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2MaxSyslogServers.setStatus("current")
_BlueNet2SyslogServerTable_Object = MibTable
blueNet2SyslogServerTable = _BlueNet2SyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 16, 4)
)
if mibBuilder.loadTexts:
    blueNet2SyslogServerTable.setStatus("current")
_BlueNet2SyslogServerEntry_Object = MibTableRow
blueNet2SyslogServerEntry = _BlueNet2SyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 16, 4, 1)
)
blueNet2SyslogServerEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2SyslogServerIndex"),
)
if mibBuilder.loadTexts:
    blueNet2SyslogServerEntry.setStatus("current")


class _BlueNet2SyslogServerIndex_Type(Unsigned32):
    """Custom type blueNet2SyslogServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BlueNet2SyslogServerIndex_Type.__name__ = "Unsigned32"
_BlueNet2SyslogServerIndex_Object = MibTableColumn
blueNet2SyslogServerIndex = _BlueNet2SyslogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 16, 4, 1, 1),
    _BlueNet2SyslogServerIndex_Type()
)
blueNet2SyslogServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SyslogServerIndex.setStatus("current")
_BlueNet2SyslogServerRowStatus_Type = RowStatus
_BlueNet2SyslogServerRowStatus_Object = MibTableColumn
blueNet2SyslogServerRowStatus = _BlueNet2SyslogServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 16, 4, 1, 2),
    _BlueNet2SyslogServerRowStatus_Type()
)
blueNet2SyslogServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    blueNet2SyslogServerRowStatus.setStatus("current")


class _BlueNet2SyslogServerAddress_Type(DisplayString):
    """Custom type blueNet2SyslogServerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BlueNet2SyslogServerAddress_Type.__name__ = "DisplayString"
_BlueNet2SyslogServerAddress_Object = MibTableColumn
blueNet2SyslogServerAddress = _BlueNet2SyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 16, 4, 1, 3),
    _BlueNet2SyslogServerAddress_Type()
)
blueNet2SyslogServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SyslogServerAddress.setStatus("current")


class _BlueNet2SyslogServerPort_Type(Unsigned32):
    """Custom type blueNet2SyslogServerPort based on Unsigned32"""
    defaultValue = 514

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BlueNet2SyslogServerPort_Type.__name__ = "Unsigned32"
_BlueNet2SyslogServerPort_Object = MibTableColumn
blueNet2SyslogServerPort = _BlueNet2SyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 16, 4, 1, 4),
    _BlueNet2SyslogServerPort_Type()
)
blueNet2SyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SyslogServerPort.setStatus("current")


class _BlueNet2SyslogServerFriendlyName_Type(DisplayString):
    """Custom type blueNet2SyslogServerFriendlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BlueNet2SyslogServerFriendlyName_Type.__name__ = "DisplayString"
_BlueNet2SyslogServerFriendlyName_Object = MibTableColumn
blueNet2SyslogServerFriendlyName = _BlueNet2SyslogServerFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 16, 4, 1, 5),
    _BlueNet2SyslogServerFriendlyName_Type()
)
blueNet2SyslogServerFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SyslogServerFriendlyName.setStatus("deprecated")


class _BlueNet2SyslogServerDescription_Type(DisplayString):
    """Custom type blueNet2SyslogServerDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2SyslogServerDescription_Type.__name__ = "DisplayString"
_BlueNet2SyslogServerDescription_Object = MibTableColumn
blueNet2SyslogServerDescription = _BlueNet2SyslogServerDescription_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 16, 4, 1, 6),
    _BlueNet2SyslogServerDescription_Type()
)
blueNet2SyslogServerDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SyslogServerDescription.setStatus("deprecated")


class _BlueNet2SyslogServerProtocol_Type(Integer32):
    """Custom type blueNet2SyslogServerProtocol based on Integer32"""
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
        *(("udp", 1),
          ("tcp", 2),
          ("relp", 3))
    )


_BlueNet2SyslogServerProtocol_Type.__name__ = "Integer32"
_BlueNet2SyslogServerProtocol_Object = MibTableColumn
blueNet2SyslogServerProtocol = _BlueNet2SyslogServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 3, 4, 16, 4, 1, 7),
    _BlueNet2SyslogServerProtocol_Type()
)
blueNet2SyslogServerProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SyslogServerProtocol.setStatus("current")
_BlueNet2Devices_ObjectIdentity = ObjectIdentity
blueNet2Devices = _BlueNet2Devices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4)
)
_BlueNet2DeviceInfo_ObjectIdentity = ObjectIdentity
blueNet2DeviceInfo = _BlueNet2DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 1)
)
_BlueNet2OverallDeviceStatus_Type = BlueNet2ComponentStates
_BlueNet2OverallDeviceStatus_Object = MibScalar
blueNet2OverallDeviceStatus = _BlueNet2OverallDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 1, 1),
    _BlueNet2OverallDeviceStatus_Type()
)
blueNet2OverallDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2OverallDeviceStatus.setStatus("current")
_BlueNet2NumberOfDevices_Type = Unsigned32
_BlueNet2NumberOfDevices_Object = MibScalar
blueNet2NumberOfDevices = _BlueNet2NumberOfDevices_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 1, 2),
    _BlueNet2NumberOfDevices_Type()
)
blueNet2NumberOfDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2NumberOfDevices.setStatus("current")
_BlueNet2LastChangeOverallDeviceStatus_Type = TimeTicks
_BlueNet2LastChangeOverallDeviceStatus_Object = MibScalar
blueNet2LastChangeOverallDeviceStatus = _BlueNet2LastChangeOverallDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 1, 3),
    _BlueNet2LastChangeOverallDeviceStatus_Type()
)
blueNet2LastChangeOverallDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeOverallDeviceStatus.setStatus("current")
_BlueNet2LastChangeNumberOfDevices_Type = TimeTicks
_BlueNet2LastChangeNumberOfDevices_Object = MibScalar
blueNet2LastChangeNumberOfDevices = _BlueNet2LastChangeNumberOfDevices_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 1, 4),
    _BlueNet2LastChangeNumberOfDevices_Type()
)
blueNet2LastChangeNumberOfDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeNumberOfDevices.setStatus("current")
_BlueNet2LastChangeDeviceSettings_Type = TimeTicks
_BlueNet2LastChangeDeviceSettings_Object = MibScalar
blueNet2LastChangeDeviceSettings = _BlueNet2LastChangeDeviceSettings_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 1, 5),
    _BlueNet2LastChangeDeviceSettings_Type()
)
blueNet2LastChangeDeviceSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeDeviceSettings.setStatus("current")
_BlueNet2LastChangeDevices_Type = TimeTicks
_BlueNet2LastChangeDevices_Object = MibScalar
blueNet2LastChangeDevices = _BlueNet2LastChangeDevices_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 1, 6),
    _BlueNet2LastChangeDevices_Type()
)
blueNet2LastChangeDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeDevices.setStatus("current")
_BlueNet2DevicesAccumulatedStatus_Type = BlueNet2EntityBits
_BlueNet2DevicesAccumulatedStatus_Object = MibScalar
blueNet2DevicesAccumulatedStatus = _BlueNet2DevicesAccumulatedStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 1, 7),
    _BlueNet2DevicesAccumulatedStatus_Type()
)
blueNet2DevicesAccumulatedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DevicesAccumulatedStatus.setStatus("current")
_BlueNet2DeviceTable_Object = MibTable
blueNet2DeviceTable = _BlueNet2DeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    blueNet2DeviceTable.setStatus("current")
_BlueNet2DeviceEntry_Object = MibTableRow
blueNet2DeviceEntry = _BlueNet2DeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1)
)
blueNet2DeviceEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2DeviceIndex"),
)
if mibBuilder.loadTexts:
    blueNet2DeviceEntry.setStatus("current")


class _BlueNet2DeviceIndex_Type(Unsigned32):
    """Custom type blueNet2DeviceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_BlueNet2DeviceIndex_Type.__name__ = "Unsigned32"
_BlueNet2DeviceIndex_Object = MibTableColumn
blueNet2DeviceIndex = _BlueNet2DeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 1),
    _BlueNet2DeviceIndex_Type()
)
blueNet2DeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2DeviceIndex.setStatus("current")


class _BlueNet2DeviceGuid_Type(OctetString):
    """Custom type blueNet2DeviceGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2DeviceGuid_Type.__name__ = "OctetString"
_BlueNet2DeviceGuid_Object = MibTableColumn
blueNet2DeviceGuid = _BlueNet2DeviceGuid_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 2),
    _BlueNet2DeviceGuid_Type()
)
blueNet2DeviceGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceGuid.setStatus("current")


class _BlueNet2DeviceName_Type(DisplayString):
    """Custom type blueNet2DeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BlueNet2DeviceName_Type.__name__ = "DisplayString"
_BlueNet2DeviceName_Object = MibTableColumn
blueNet2DeviceName = _BlueNet2DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 3),
    _BlueNet2DeviceName_Type()
)
blueNet2DeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceName.setStatus("current")


class _BlueNet2DeviceFriendlyName_Type(DisplayString):
    """Custom type blueNet2DeviceFriendlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BlueNet2DeviceFriendlyName_Type.__name__ = "DisplayString"
_BlueNet2DeviceFriendlyName_Object = MibTableColumn
blueNet2DeviceFriendlyName = _BlueNet2DeviceFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 4),
    _BlueNet2DeviceFriendlyName_Type()
)
blueNet2DeviceFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2DeviceFriendlyName.setStatus("current")


class _BlueNet2DeviceDescription_Type(DisplayString):
    """Custom type blueNet2DeviceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2DeviceDescription_Type.__name__ = "DisplayString"
_BlueNet2DeviceDescription_Object = MibTableColumn
blueNet2DeviceDescription = _BlueNet2DeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 5),
    _BlueNet2DeviceDescription_Type()
)
blueNet2DeviceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2DeviceDescription.setStatus("current")
_BlueNet2DeviceType_Type = ObjectIdentifier
_BlueNet2DeviceType_Object = MibTableColumn
blueNet2DeviceType = _BlueNet2DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 6),
    _BlueNet2DeviceType_Type()
)
blueNet2DeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceType.setStatus("current")
_BlueNet2DeviceStatus_Type = BlueNet2EntityStates
_BlueNet2DeviceStatus_Object = MibTableColumn
blueNet2DeviceStatus = _BlueNet2DeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 7),
    _BlueNet2DeviceStatus_Type()
)
blueNet2DeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceStatus.setStatus("current")


class _BlueNet2DeviceAlarm_Type(DisplayString):
    """Custom type blueNet2DeviceAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2DeviceAlarm_Type.__name__ = "DisplayString"
_BlueNet2DeviceAlarm_Object = MibTableColumn
blueNet2DeviceAlarm = _BlueNet2DeviceAlarm_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 8),
    _BlueNet2DeviceAlarm_Type()
)
blueNet2DeviceAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceAlarm.setStatus("deprecated")
_BlueNet2DeviceLastChange_Type = TimeTicks
_BlueNet2DeviceLastChange_Object = MibTableColumn
blueNet2DeviceLastChange = _BlueNet2DeviceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 9),
    _BlueNet2DeviceLastChange_Type()
)
blueNet2DeviceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceLastChange.setStatus("current")
_BlueNet2DeviceEntPhysicalIndex_Type = Unsigned32
_BlueNet2DeviceEntPhysicalIndex_Object = MibTableColumn
blueNet2DeviceEntPhysicalIndex = _BlueNet2DeviceEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 10),
    _BlueNet2DeviceEntPhysicalIndex_Type()
)
blueNet2DeviceEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceEntPhysicalIndex.setStatus("current")


class _BlueNet2DevicePartNr_Type(DisplayString):
    """Custom type blueNet2DevicePartNr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2DevicePartNr_Type.__name__ = "DisplayString"
_BlueNet2DevicePartNr_Object = MibTableColumn
blueNet2DevicePartNr = _BlueNet2DevicePartNr_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 11),
    _BlueNet2DevicePartNr_Type()
)
blueNet2DevicePartNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DevicePartNr.setStatus("current")


class _BlueNet2DeviceSNr_Type(DisplayString):
    """Custom type blueNet2DeviceSNr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2DeviceSNr_Type.__name__ = "DisplayString"
_BlueNet2DeviceSNr_Object = MibTableColumn
blueNet2DeviceSNr = _BlueNet2DeviceSNr_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 12),
    _BlueNet2DeviceSNr_Type()
)
blueNet2DeviceSNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceSNr.setStatus("current")


class _BlueNet2DeviceFwV_Type(DisplayString):
    """Custom type blueNet2DeviceFwV based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2DeviceFwV_Type.__name__ = "DisplayString"
_BlueNet2DeviceFwV_Object = MibTableColumn
blueNet2DeviceFwV = _BlueNet2DeviceFwV_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 13),
    _BlueNet2DeviceFwV_Type()
)
blueNet2DeviceFwV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceFwV.setStatus("current")


class _BlueNet2DeviceHwV_Type(DisplayString):
    """Custom type blueNet2DeviceHwV based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2DeviceHwV_Type.__name__ = "DisplayString"
_BlueNet2DeviceHwV_Object = MibTableColumn
blueNet2DeviceHwV = _BlueNet2DeviceHwV_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 14),
    _BlueNet2DeviceHwV_Type()
)
blueNet2DeviceHwV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceHwV.setStatus("current")


class _BlueNet2DeviceSwV_Type(DisplayString):
    """Custom type blueNet2DeviceSwV based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2DeviceSwV_Type.__name__ = "DisplayString"
_BlueNet2DeviceSwV_Object = MibTableColumn
blueNet2DeviceSwV = _BlueNet2DeviceSwV_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 15),
    _BlueNet2DeviceSwV_Type()
)
blueNet2DeviceSwV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceSwV.setStatus("current")


class _BlueNet2DeviceOsV_Type(DisplayString):
    """Custom type blueNet2DeviceOsV based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2DeviceOsV_Type.__name__ = "DisplayString"
_BlueNet2DeviceOsV_Object = MibTableColumn
blueNet2DeviceOsV = _BlueNet2DeviceOsV_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 16),
    _BlueNet2DeviceOsV_Type()
)
blueNet2DeviceOsV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceOsV.setStatus("current")


class _BlueNet2DeviceMAC_Type(DisplayString):
    """Custom type blueNet2DeviceMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2DeviceMAC_Type.__name__ = "DisplayString"
_BlueNet2DeviceMAC_Object = MibTableColumn
blueNet2DeviceMAC = _BlueNet2DeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 17),
    _BlueNet2DeviceMAC_Type()
)
blueNet2DeviceMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceMAC.setStatus("current")
_BlueNet2DeviceNumberOfSensors_Type = Unsigned32
_BlueNet2DeviceNumberOfSensors_Object = MibTableColumn
blueNet2DeviceNumberOfSensors = _BlueNet2DeviceNumberOfSensors_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 18),
    _BlueNet2DeviceNumberOfSensors_Type()
)
blueNet2DeviceNumberOfSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceNumberOfSensors.setStatus("current")
_BlueNet2DeviceNumberOfCircuits_Type = Unsigned32
_BlueNet2DeviceNumberOfCircuits_Object = MibTableColumn
blueNet2DeviceNumberOfCircuits = _BlueNet2DeviceNumberOfCircuits_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 19),
    _BlueNet2DeviceNumberOfCircuits_Type()
)
blueNet2DeviceNumberOfCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceNumberOfCircuits.setStatus("current")
_BlueNet2DeviceNumberOfPhases_Type = Unsigned32
_BlueNet2DeviceNumberOfPhases_Object = MibTableColumn
blueNet2DeviceNumberOfPhases = _BlueNet2DeviceNumberOfPhases_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 20),
    _BlueNet2DeviceNumberOfPhases_Type()
)
blueNet2DeviceNumberOfPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceNumberOfPhases.setStatus("current")
_BlueNet2DeviceNumberOfFuses_Type = Unsigned32
_BlueNet2DeviceNumberOfFuses_Object = MibTableColumn
blueNet2DeviceNumberOfFuses = _BlueNet2DeviceNumberOfFuses_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 21),
    _BlueNet2DeviceNumberOfFuses_Type()
)
blueNet2DeviceNumberOfFuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceNumberOfFuses.setStatus("current")
_BlueNet2DeviceNumberOfSockets_Type = Unsigned32
_BlueNet2DeviceNumberOfSockets_Object = MibTableColumn
blueNet2DeviceNumberOfSockets = _BlueNet2DeviceNumberOfSockets_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 22),
    _BlueNet2DeviceNumberOfSockets_Type()
)
blueNet2DeviceNumberOfSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceNumberOfSockets.setStatus("current")
_BlueNet2DeviceNumberOfRCMs_Type = Unsigned32
_BlueNet2DeviceNumberOfRCMs_Object = MibTableColumn
blueNet2DeviceNumberOfRCMs = _BlueNet2DeviceNumberOfRCMs_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 23),
    _BlueNet2DeviceNumberOfRCMs_Type()
)
blueNet2DeviceNumberOfRCMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceNumberOfRCMs.setStatus("current")
_BlueNet2DeviceNumberOfVars_Type = Unsigned32
_BlueNet2DeviceNumberOfVars_Object = MibTableColumn
blueNet2DeviceNumberOfVars = _BlueNet2DeviceNumberOfVars_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 24),
    _BlueNet2DeviceNumberOfVars_Type()
)
blueNet2DeviceNumberOfVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceNumberOfVars.setStatus("current")


class _BlueNet2DeviceLocation_Type(DisplayString):
    """Custom type blueNet2DeviceLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2DeviceLocation_Type.__name__ = "DisplayString"
_BlueNet2DeviceLocation_Object = MibTableColumn
blueNet2DeviceLocation = _BlueNet2DeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 25),
    _BlueNet2DeviceLocation_Type()
)
blueNet2DeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2DeviceLocation.setStatus("current")


class _BlueNet2DeviceProductDate_Type(DisplayString):
    """Custom type blueNet2DeviceProductDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2DeviceProductDate_Type.__name__ = "DisplayString"
_BlueNet2DeviceProductDate_Object = MibTableColumn
blueNet2DeviceProductDate = _BlueNet2DeviceProductDate_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 26),
    _BlueNet2DeviceProductDate_Type()
)
blueNet2DeviceProductDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceProductDate.setStatus("current")
_BlueNet2DeviceModbusAddr_Type = Integer32
_BlueNet2DeviceModbusAddr_Object = MibTableColumn
blueNet2DeviceModbusAddr = _BlueNet2DeviceModbusAddr_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 27),
    _BlueNet2DeviceModbusAddr_Type()
)
blueNet2DeviceModbusAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceModbusAddr.setStatus("current")
_BlueNet2DeviceNumberOfSPDs_Type = Unsigned32
_BlueNet2DeviceNumberOfSPDs_Object = MibTableColumn
blueNet2DeviceNumberOfSPDs = _BlueNet2DeviceNumberOfSPDs_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 4, 2, 1, 28),
    _BlueNet2DeviceNumberOfSPDs_Type()
)
blueNet2DeviceNumberOfSPDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2DeviceNumberOfSPDs.setStatus("current")
_BlueNet2Sensors_ObjectIdentity = ObjectIdentity
blueNet2Sensors = _BlueNet2Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5)
)
_BlueNet2SensorInfo_ObjectIdentity = ObjectIdentity
blueNet2SensorInfo = _BlueNet2SensorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 1)
)
_BlueNet2OverallSensorStatus_Type = BlueNet2ComponentStates
_BlueNet2OverallSensorStatus_Object = MibScalar
blueNet2OverallSensorStatus = _BlueNet2OverallSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 1, 1),
    _BlueNet2OverallSensorStatus_Type()
)
blueNet2OverallSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2OverallSensorStatus.setStatus("current")
_BlueNet2NumberOfSensors_Type = Unsigned32
_BlueNet2NumberOfSensors_Object = MibScalar
blueNet2NumberOfSensors = _BlueNet2NumberOfSensors_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 1, 2),
    _BlueNet2NumberOfSensors_Type()
)
blueNet2NumberOfSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2NumberOfSensors.setStatus("current")
_BlueNet2LastChangeOverallSensorStatus_Type = TimeTicks
_BlueNet2LastChangeOverallSensorStatus_Object = MibScalar
blueNet2LastChangeOverallSensorStatus = _BlueNet2LastChangeOverallSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 1, 3),
    _BlueNet2LastChangeOverallSensorStatus_Type()
)
blueNet2LastChangeOverallSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeOverallSensorStatus.setStatus("current")
_BlueNet2LastChangeNumberOfSensors_Type = TimeTicks
_BlueNet2LastChangeNumberOfSensors_Object = MibScalar
blueNet2LastChangeNumberOfSensors = _BlueNet2LastChangeNumberOfSensors_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 1, 4),
    _BlueNet2LastChangeNumberOfSensors_Type()
)
blueNet2LastChangeNumberOfSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeNumberOfSensors.setStatus("current")
_BlueNet2LastChangeSensorSettings_Type = TimeTicks
_BlueNet2LastChangeSensorSettings_Object = MibScalar
blueNet2LastChangeSensorSettings = _BlueNet2LastChangeSensorSettings_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 1, 5),
    _BlueNet2LastChangeSensorSettings_Type()
)
blueNet2LastChangeSensorSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeSensorSettings.setStatus("current")
_BlueNet2LastChangeSensors_Type = TimeTicks
_BlueNet2LastChangeSensors_Object = MibScalar
blueNet2LastChangeSensors = _BlueNet2LastChangeSensors_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 1, 6),
    _BlueNet2LastChangeSensors_Type()
)
blueNet2LastChangeSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeSensors.setStatus("current")
_BlueNet2SensorsAccumulatedStatus_Type = BlueNet2EntityBits
_BlueNet2SensorsAccumulatedStatus_Object = MibScalar
blueNet2SensorsAccumulatedStatus = _BlueNet2SensorsAccumulatedStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 1, 7),
    _BlueNet2SensorsAccumulatedStatus_Type()
)
blueNet2SensorsAccumulatedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SensorsAccumulatedStatus.setStatus("current")
_BlueNet2SensorTable_Object = MibTable
blueNet2SensorTable = _BlueNet2SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    blueNet2SensorTable.setStatus("current")
_BlueNet2SensorEntry_Object = MibTableRow
blueNet2SensorEntry = _BlueNet2SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 2, 1)
)
blueNet2SensorEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2SensorDevice"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2SensorIndex"),
)
if mibBuilder.loadTexts:
    blueNet2SensorEntry.setStatus("current")


class _BlueNet2SensorDevice_Type(Unsigned32):
    """Custom type blueNet2SensorDevice based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_BlueNet2SensorDevice_Type.__name__ = "Unsigned32"
_BlueNet2SensorDevice_Object = MibTableColumn
blueNet2SensorDevice = _BlueNet2SensorDevice_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 2, 1, 1),
    _BlueNet2SensorDevice_Type()
)
blueNet2SensorDevice.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SensorDevice.setStatus("current")


class _BlueNet2SensorIndex_Type(Unsigned32):
    """Custom type blueNet2SensorIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BlueNet2SensorIndex_Type.__name__ = "Unsigned32"
_BlueNet2SensorIndex_Object = MibTableColumn
blueNet2SensorIndex = _BlueNet2SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 2, 1, 2),
    _BlueNet2SensorIndex_Type()
)
blueNet2SensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SensorIndex.setStatus("current")


class _BlueNet2SensorGuid_Type(OctetString):
    """Custom type blueNet2SensorGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2SensorGuid_Type.__name__ = "OctetString"
_BlueNet2SensorGuid_Object = MibTableColumn
blueNet2SensorGuid = _BlueNet2SensorGuid_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 2, 1, 3),
    _BlueNet2SensorGuid_Type()
)
blueNet2SensorGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SensorGuid.setStatus("current")


class _BlueNet2SensorName_Type(DisplayString):
    """Custom type blueNet2SensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BlueNet2SensorName_Type.__name__ = "DisplayString"
_BlueNet2SensorName_Object = MibTableColumn
blueNet2SensorName = _BlueNet2SensorName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 2, 1, 4),
    _BlueNet2SensorName_Type()
)
blueNet2SensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SensorName.setStatus("current")


class _BlueNet2SensorFriendlyName_Type(DisplayString):
    """Custom type blueNet2SensorFriendlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BlueNet2SensorFriendlyName_Type.__name__ = "DisplayString"
_BlueNet2SensorFriendlyName_Object = MibTableColumn
blueNet2SensorFriendlyName = _BlueNet2SensorFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 2, 1, 5),
    _BlueNet2SensorFriendlyName_Type()
)
blueNet2SensorFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SensorFriendlyName.setStatus("current")


class _BlueNet2SensorDescription_Type(DisplayString):
    """Custom type blueNet2SensorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2SensorDescription_Type.__name__ = "DisplayString"
_BlueNet2SensorDescription_Object = MibTableColumn
blueNet2SensorDescription = _BlueNet2SensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 2, 1, 6),
    _BlueNet2SensorDescription_Type()
)
blueNet2SensorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SensorDescription.setStatus("current")
_BlueNet2SensorType_Type = ObjectIdentifier
_BlueNet2SensorType_Object = MibTableColumn
blueNet2SensorType = _BlueNet2SensorType_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 2, 1, 7),
    _BlueNet2SensorType_Type()
)
blueNet2SensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SensorType.setStatus("current")
_BlueNet2SensorStatus_Type = BlueNet2EntityStates
_BlueNet2SensorStatus_Object = MibTableColumn
blueNet2SensorStatus = _BlueNet2SensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 2, 1, 8),
    _BlueNet2SensorStatus_Type()
)
blueNet2SensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SensorStatus.setStatus("current")


class _BlueNet2SensorAlarm_Type(DisplayString):
    """Custom type blueNet2SensorAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2SensorAlarm_Type.__name__ = "DisplayString"
_BlueNet2SensorAlarm_Object = MibTableColumn
blueNet2SensorAlarm = _BlueNet2SensorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 2, 1, 9),
    _BlueNet2SensorAlarm_Type()
)
blueNet2SensorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SensorAlarm.setStatus("current")
_BlueNet2SensorLastChange_Type = TimeTicks
_BlueNet2SensorLastChange_Object = MibTableColumn
blueNet2SensorLastChange = _BlueNet2SensorLastChange_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 2, 1, 10),
    _BlueNet2SensorLastChange_Type()
)
blueNet2SensorLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SensorLastChange.setStatus("current")
_BlueNet2SensorEntPhysicalIndex_Type = Unsigned32
_BlueNet2SensorEntPhysicalIndex_Object = MibTableColumn
blueNet2SensorEntPhysicalIndex = _BlueNet2SensorEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 2, 1, 11),
    _BlueNet2SensorEntPhysicalIndex_Type()
)
blueNet2SensorEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SensorEntPhysicalIndex.setStatus("current")
_BlueNet2SensorNumberOfVars_Type = Unsigned32
_BlueNet2SensorNumberOfVars_Object = MibTableColumn
blueNet2SensorNumberOfVars = _BlueNet2SensorNumberOfVars_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 2, 1, 12),
    _BlueNet2SensorNumberOfVars_Type()
)
blueNet2SensorNumberOfVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SensorNumberOfVars.setStatus("current")


class _BlueNet2SensorHwV_Type(DisplayString):
    """Custom type blueNet2SensorHwV based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2SensorHwV_Type.__name__ = "DisplayString"
_BlueNet2SensorHwV_Object = MibTableColumn
blueNet2SensorHwV = _BlueNet2SensorHwV_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 2, 1, 13),
    _BlueNet2SensorHwV_Type()
)
blueNet2SensorHwV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SensorHwV.setStatus("current")


class _BlueNet2SensorFwV_Type(DisplayString):
    """Custom type blueNet2SensorFwV based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BlueNet2SensorFwV_Type.__name__ = "DisplayString"
_BlueNet2SensorFwV_Object = MibTableColumn
blueNet2SensorFwV = _BlueNet2SensorFwV_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 2, 1, 14),
    _BlueNet2SensorFwV_Type()
)
blueNet2SensorFwV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SensorFwV.setStatus("current")


class _BlueNet2SensorSNr_Type(DisplayString):
    """Custom type blueNet2SensorSNr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BlueNet2SensorSNr_Type.__name__ = "DisplayString"
_BlueNet2SensorSNr_Object = MibTableColumn
blueNet2SensorSNr = _BlueNet2SensorSNr_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 2, 1, 15),
    _BlueNet2SensorSNr_Type()
)
blueNet2SensorSNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SensorSNr.setStatus("current")
_BlueNet2SensorVariableTable_Object = MibTable
blueNet2SensorVariableTable = _BlueNet2SensorVariableTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 3)
)
if mibBuilder.loadTexts:
    blueNet2SensorVariableTable.setStatus("current")
_BlueNet2SensorVariableEntry_Object = MibTableRow
blueNet2SensorVariableEntry = _BlueNet2SensorVariableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 3, 1)
)
blueNet2SensorVariableEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2SensorDeviceIndex"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2SensorSensorIndex"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2SensorVariableIndex"),
)
if mibBuilder.loadTexts:
    blueNet2SensorVariableEntry.setStatus("current")


class _BlueNet2SensorDeviceIndex_Type(Unsigned32):
    """Custom type blueNet2SensorDeviceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_BlueNet2SensorDeviceIndex_Type.__name__ = "Unsigned32"
_BlueNet2SensorDeviceIndex_Object = MibTableColumn
blueNet2SensorDeviceIndex = _BlueNet2SensorDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 3, 1, 1),
    _BlueNet2SensorDeviceIndex_Type()
)
blueNet2SensorDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SensorDeviceIndex.setStatus("current")


class _BlueNet2SensorSensorIndex_Type(Unsigned32):
    """Custom type blueNet2SensorSensorIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BlueNet2SensorSensorIndex_Type.__name__ = "Unsigned32"
_BlueNet2SensorSensorIndex_Object = MibTableColumn
blueNet2SensorSensorIndex = _BlueNet2SensorSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 3, 1, 2),
    _BlueNet2SensorSensorIndex_Type()
)
blueNet2SensorSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SensorSensorIndex.setStatus("current")


class _BlueNet2SensorVariableIndex_Type(Unsigned32):
    """Custom type blueNet2SensorVariableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BlueNet2SensorVariableIndex_Type.__name__ = "Unsigned32"
_BlueNet2SensorVariableIndex_Object = MibTableColumn
blueNet2SensorVariableIndex = _BlueNet2SensorVariableIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 3, 1, 3),
    _BlueNet2SensorVariableIndex_Type()
)
blueNet2SensorVariableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SensorVariableIndex.setStatus("current")


class _BlueNet2SensorVariableGuid_Type(OctetString):
    """Custom type blueNet2SensorVariableGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2SensorVariableGuid_Type.__name__ = "OctetString"
_BlueNet2SensorVariableGuid_Object = MibTableColumn
blueNet2SensorVariableGuid = _BlueNet2SensorVariableGuid_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 3, 1, 4),
    _BlueNet2SensorVariableGuid_Type()
)
blueNet2SensorVariableGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SensorVariableGuid.setStatus("current")


class _BlueNet2SensorVariableName_Type(DisplayString):
    """Custom type blueNet2SensorVariableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BlueNet2SensorVariableName_Type.__name__ = "DisplayString"
_BlueNet2SensorVariableName_Object = MibTableColumn
blueNet2SensorVariableName = _BlueNet2SensorVariableName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 3, 1, 5),
    _BlueNet2SensorVariableName_Type()
)
blueNet2SensorVariableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SensorVariableName.setStatus("current")


class _BlueNet2SensorVariableFriendlyName_Type(DisplayString):
    """Custom type blueNet2SensorVariableFriendlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BlueNet2SensorVariableFriendlyName_Type.__name__ = "DisplayString"
_BlueNet2SensorVariableFriendlyName_Object = MibTableColumn
blueNet2SensorVariableFriendlyName = _BlueNet2SensorVariableFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 3, 1, 6),
    _BlueNet2SensorVariableFriendlyName_Type()
)
blueNet2SensorVariableFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SensorVariableFriendlyName.setStatus("current")


class _BlueNet2SensorVariableDescription_Type(DisplayString):
    """Custom type blueNet2SensorVariableDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2SensorVariableDescription_Type.__name__ = "DisplayString"
_BlueNet2SensorVariableDescription_Object = MibTableColumn
blueNet2SensorVariableDescription = _BlueNet2SensorVariableDescription_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 3, 1, 7),
    _BlueNet2SensorVariableDescription_Type()
)
blueNet2SensorVariableDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SensorVariableDescription.setStatus("current")
_BlueNet2SensorVariableGPIOMode_Type = BlueNet2GPIOModes
_BlueNet2SensorVariableGPIOMode_Object = MibTableColumn
blueNet2SensorVariableGPIOMode = _BlueNet2SensorVariableGPIOMode_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 3, 1, 8),
    _BlueNet2SensorVariableGPIOMode_Type()
)
blueNet2SensorVariableGPIOMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SensorVariableGPIOMode.setStatus("current")
_BlueNet2SensorVariableGPIOSwitch_Type = BlueNet2GPIOSwitch
_BlueNet2SensorVariableGPIOSwitch_Object = MibTableColumn
blueNet2SensorVariableGPIOSwitch = _BlueNet2SensorVariableGPIOSwitch_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 3, 1, 9),
    _BlueNet2SensorVariableGPIOSwitch_Type()
)
blueNet2SensorVariableGPIOSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SensorVariableGPIOSwitch.setStatus("current")
_BlueNet2SensorVariableGPIOState_Type = BlueNet2EntityStates
_BlueNet2SensorVariableGPIOState_Object = MibTableColumn
blueNet2SensorVariableGPIOState = _BlueNet2SensorVariableGPIOState_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 5, 3, 1, 10),
    _BlueNet2SensorVariableGPIOState_Type()
)
blueNet2SensorVariableGPIOState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SensorVariableGPIOState.setStatus("current")
_BlueNet2Circuits_ObjectIdentity = ObjectIdentity
blueNet2Circuits = _BlueNet2Circuits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6)
)
_BlueNet2CircuitInfo_ObjectIdentity = ObjectIdentity
blueNet2CircuitInfo = _BlueNet2CircuitInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 1)
)
_BlueNet2OverallCircuitStatus_Type = BlueNet2ComponentStates
_BlueNet2OverallCircuitStatus_Object = MibScalar
blueNet2OverallCircuitStatus = _BlueNet2OverallCircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 1, 1),
    _BlueNet2OverallCircuitStatus_Type()
)
blueNet2OverallCircuitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2OverallCircuitStatus.setStatus("current")
_BlueNet2NumberOfCircuits_Type = Unsigned32
_BlueNet2NumberOfCircuits_Object = MibScalar
blueNet2NumberOfCircuits = _BlueNet2NumberOfCircuits_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 1, 2),
    _BlueNet2NumberOfCircuits_Type()
)
blueNet2NumberOfCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2NumberOfCircuits.setStatus("current")
_BlueNet2LastChangeOverallCircuitStatus_Type = TimeTicks
_BlueNet2LastChangeOverallCircuitStatus_Object = MibScalar
blueNet2LastChangeOverallCircuitStatus = _BlueNet2LastChangeOverallCircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 1, 3),
    _BlueNet2LastChangeOverallCircuitStatus_Type()
)
blueNet2LastChangeOverallCircuitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeOverallCircuitStatus.setStatus("current")
_BlueNet2LastChangeNumberOfCircuits_Type = TimeTicks
_BlueNet2LastChangeNumberOfCircuits_Object = MibScalar
blueNet2LastChangeNumberOfCircuits = _BlueNet2LastChangeNumberOfCircuits_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 1, 4),
    _BlueNet2LastChangeNumberOfCircuits_Type()
)
blueNet2LastChangeNumberOfCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeNumberOfCircuits.setStatus("current")
_BlueNet2LastChangeCircuitSettings_Type = TimeTicks
_BlueNet2LastChangeCircuitSettings_Object = MibScalar
blueNet2LastChangeCircuitSettings = _BlueNet2LastChangeCircuitSettings_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 1, 5),
    _BlueNet2LastChangeCircuitSettings_Type()
)
blueNet2LastChangeCircuitSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeCircuitSettings.setStatus("current")
_BlueNet2LastChangeCircuits_Type = TimeTicks
_BlueNet2LastChangeCircuits_Object = MibScalar
blueNet2LastChangeCircuits = _BlueNet2LastChangeCircuits_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 1, 6),
    _BlueNet2LastChangeCircuits_Type()
)
blueNet2LastChangeCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeCircuits.setStatus("current")
_BlueNet2CircuitTable_Object = MibTable
blueNet2CircuitTable = _BlueNet2CircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 2)
)
if mibBuilder.loadTexts:
    blueNet2CircuitTable.setStatus("current")
_BlueNet2CircuitEntry_Object = MibTableRow
blueNet2CircuitEntry = _BlueNet2CircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 2, 1)
)
blueNet2CircuitEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2CircuitDevice"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2CircuitIndex"),
)
if mibBuilder.loadTexts:
    blueNet2CircuitEntry.setStatus("current")


class _BlueNet2CircuitDevice_Type(Unsigned32):
    """Custom type blueNet2CircuitDevice based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_BlueNet2CircuitDevice_Type.__name__ = "Unsigned32"
_BlueNet2CircuitDevice_Object = MibTableColumn
blueNet2CircuitDevice = _BlueNet2CircuitDevice_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 2, 1, 1),
    _BlueNet2CircuitDevice_Type()
)
blueNet2CircuitDevice.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2CircuitDevice.setStatus("current")


class _BlueNet2CircuitIndex_Type(Unsigned32):
    """Custom type blueNet2CircuitIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_BlueNet2CircuitIndex_Type.__name__ = "Unsigned32"
_BlueNet2CircuitIndex_Object = MibTableColumn
blueNet2CircuitIndex = _BlueNet2CircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 2, 1, 2),
    _BlueNet2CircuitIndex_Type()
)
blueNet2CircuitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2CircuitIndex.setStatus("current")


class _BlueNet2CircuitGuid_Type(OctetString):
    """Custom type blueNet2CircuitGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2CircuitGuid_Type.__name__ = "OctetString"
_BlueNet2CircuitGuid_Object = MibTableColumn
blueNet2CircuitGuid = _BlueNet2CircuitGuid_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 2, 1, 3),
    _BlueNet2CircuitGuid_Type()
)
blueNet2CircuitGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2CircuitGuid.setStatus("current")


class _BlueNet2CircuitName_Type(DisplayString):
    """Custom type blueNet2CircuitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BlueNet2CircuitName_Type.__name__ = "DisplayString"
_BlueNet2CircuitName_Object = MibTableColumn
blueNet2CircuitName = _BlueNet2CircuitName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 2, 1, 4),
    _BlueNet2CircuitName_Type()
)
blueNet2CircuitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2CircuitName.setStatus("current")


class _BlueNet2CircuitFriendlyName_Type(DisplayString):
    """Custom type blueNet2CircuitFriendlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BlueNet2CircuitFriendlyName_Type.__name__ = "DisplayString"
_BlueNet2CircuitFriendlyName_Object = MibTableColumn
blueNet2CircuitFriendlyName = _BlueNet2CircuitFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 2, 1, 5),
    _BlueNet2CircuitFriendlyName_Type()
)
blueNet2CircuitFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2CircuitFriendlyName.setStatus("current")


class _BlueNet2CircuitDescription_Type(DisplayString):
    """Custom type blueNet2CircuitDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2CircuitDescription_Type.__name__ = "DisplayString"
_BlueNet2CircuitDescription_Object = MibTableColumn
blueNet2CircuitDescription = _BlueNet2CircuitDescription_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 2, 1, 6),
    _BlueNet2CircuitDescription_Type()
)
blueNet2CircuitDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2CircuitDescription.setStatus("current")
_BlueNet2CircuitType_Type = ObjectIdentifier
_BlueNet2CircuitType_Object = MibTableColumn
blueNet2CircuitType = _BlueNet2CircuitType_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 2, 1, 7),
    _BlueNet2CircuitType_Type()
)
blueNet2CircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2CircuitType.setStatus("current")
_BlueNet2CircuitStatus_Type = BlueNet2EntityStates
_BlueNet2CircuitStatus_Object = MibTableColumn
blueNet2CircuitStatus = _BlueNet2CircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 2, 1, 8),
    _BlueNet2CircuitStatus_Type()
)
blueNet2CircuitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2CircuitStatus.setStatus("current")
_BlueNet2CircuitNumberOfPhases_Type = Unsigned32
_BlueNet2CircuitNumberOfPhases_Object = MibTableColumn
blueNet2CircuitNumberOfPhases = _BlueNet2CircuitNumberOfPhases_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 2, 1, 9),
    _BlueNet2CircuitNumberOfPhases_Type()
)
blueNet2CircuitNumberOfPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2CircuitNumberOfPhases.setStatus("current")
_BlueNet2PhaseTable_Object = MibTable
blueNet2PhaseTable = _BlueNet2PhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 3)
)
if mibBuilder.loadTexts:
    blueNet2PhaseTable.setStatus("current")
_BlueNet2PhaseEntry_Object = MibTableRow
blueNet2PhaseEntry = _BlueNet2PhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 3, 1)
)
blueNet2PhaseEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2PhaseDevice"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2PhaseCircuit"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2PhaseIndex"),
)
if mibBuilder.loadTexts:
    blueNet2PhaseEntry.setStatus("current")


class _BlueNet2PhaseDevice_Type(Unsigned32):
    """Custom type blueNet2PhaseDevice based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_BlueNet2PhaseDevice_Type.__name__ = "Unsigned32"
_BlueNet2PhaseDevice_Object = MibTableColumn
blueNet2PhaseDevice = _BlueNet2PhaseDevice_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 3, 1, 1),
    _BlueNet2PhaseDevice_Type()
)
blueNet2PhaseDevice.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2PhaseDevice.setStatus("current")


class _BlueNet2PhaseCircuit_Type(Unsigned32):
    """Custom type blueNet2PhaseCircuit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_BlueNet2PhaseCircuit_Type.__name__ = "Unsigned32"
_BlueNet2PhaseCircuit_Object = MibTableColumn
blueNet2PhaseCircuit = _BlueNet2PhaseCircuit_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 3, 1, 2),
    _BlueNet2PhaseCircuit_Type()
)
blueNet2PhaseCircuit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2PhaseCircuit.setStatus("current")


class _BlueNet2PhaseIndex_Type(Unsigned32):
    """Custom type blueNet2PhaseIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BlueNet2PhaseIndex_Type.__name__ = "Unsigned32"
_BlueNet2PhaseIndex_Object = MibTableColumn
blueNet2PhaseIndex = _BlueNet2PhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 3, 1, 3),
    _BlueNet2PhaseIndex_Type()
)
blueNet2PhaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2PhaseIndex.setStatus("current")


class _BlueNet2PhaseGuid_Type(OctetString):
    """Custom type blueNet2PhaseGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2PhaseGuid_Type.__name__ = "OctetString"
_BlueNet2PhaseGuid_Object = MibTableColumn
blueNet2PhaseGuid = _BlueNet2PhaseGuid_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 3, 1, 4),
    _BlueNet2PhaseGuid_Type()
)
blueNet2PhaseGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2PhaseGuid.setStatus("current")


class _BlueNet2PhaseName_Type(DisplayString):
    """Custom type blueNet2PhaseName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BlueNet2PhaseName_Type.__name__ = "DisplayString"
_BlueNet2PhaseName_Object = MibTableColumn
blueNet2PhaseName = _BlueNet2PhaseName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 3, 1, 5),
    _BlueNet2PhaseName_Type()
)
blueNet2PhaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2PhaseName.setStatus("current")


class _BlueNet2PhaseFriendlyName_Type(DisplayString):
    """Custom type blueNet2PhaseFriendlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BlueNet2PhaseFriendlyName_Type.__name__ = "DisplayString"
_BlueNet2PhaseFriendlyName_Object = MibTableColumn
blueNet2PhaseFriendlyName = _BlueNet2PhaseFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 3, 1, 6),
    _BlueNet2PhaseFriendlyName_Type()
)
blueNet2PhaseFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2PhaseFriendlyName.setStatus("current")


class _BlueNet2PhaseDescription_Type(DisplayString):
    """Custom type blueNet2PhaseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2PhaseDescription_Type.__name__ = "DisplayString"
_BlueNet2PhaseDescription_Object = MibTableColumn
blueNet2PhaseDescription = _BlueNet2PhaseDescription_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 3, 1, 7),
    _BlueNet2PhaseDescription_Type()
)
blueNet2PhaseDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2PhaseDescription.setStatus("current")
_BlueNet2PhaseStatus_Type = BlueNet2EntityStates
_BlueNet2PhaseStatus_Object = MibTableColumn
blueNet2PhaseStatus = _BlueNet2PhaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 3, 1, 8),
    _BlueNet2PhaseStatus_Type()
)
blueNet2PhaseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2PhaseStatus.setStatus("current")
_BlueNet2PhaseNumberOfFuses_Type = Unsigned32
_BlueNet2PhaseNumberOfFuses_Object = MibTableColumn
blueNet2PhaseNumberOfFuses = _BlueNet2PhaseNumberOfFuses_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 3, 1, 9),
    _BlueNet2PhaseNumberOfFuses_Type()
)
blueNet2PhaseNumberOfFuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2PhaseNumberOfFuses.setStatus("current")
_BlueNet2FuseTable_Object = MibTable
blueNet2FuseTable = _BlueNet2FuseTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 4)
)
if mibBuilder.loadTexts:
    blueNet2FuseTable.setStatus("current")
_BlueNet2FuseEntry_Object = MibTableRow
blueNet2FuseEntry = _BlueNet2FuseEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 4, 1)
)
blueNet2FuseEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2FuseDevice"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2FuseCircuit"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2FusePhase"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2FuseIndex"),
)
if mibBuilder.loadTexts:
    blueNet2FuseEntry.setStatus("current")


class _BlueNet2FuseDevice_Type(Unsigned32):
    """Custom type blueNet2FuseDevice based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_BlueNet2FuseDevice_Type.__name__ = "Unsigned32"
_BlueNet2FuseDevice_Object = MibTableColumn
blueNet2FuseDevice = _BlueNet2FuseDevice_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 4, 1, 1),
    _BlueNet2FuseDevice_Type()
)
blueNet2FuseDevice.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2FuseDevice.setStatus("current")


class _BlueNet2FuseCircuit_Type(Unsigned32):
    """Custom type blueNet2FuseCircuit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_BlueNet2FuseCircuit_Type.__name__ = "Unsigned32"
_BlueNet2FuseCircuit_Object = MibTableColumn
blueNet2FuseCircuit = _BlueNet2FuseCircuit_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 4, 1, 2),
    _BlueNet2FuseCircuit_Type()
)
blueNet2FuseCircuit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2FuseCircuit.setStatus("current")


class _BlueNet2FusePhase_Type(Unsigned32):
    """Custom type blueNet2FusePhase based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BlueNet2FusePhase_Type.__name__ = "Unsigned32"
_BlueNet2FusePhase_Object = MibTableColumn
blueNet2FusePhase = _BlueNet2FusePhase_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 4, 1, 3),
    _BlueNet2FusePhase_Type()
)
blueNet2FusePhase.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2FusePhase.setStatus("current")


class _BlueNet2FuseIndex_Type(Unsigned32):
    """Custom type blueNet2FuseIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BlueNet2FuseIndex_Type.__name__ = "Unsigned32"
_BlueNet2FuseIndex_Object = MibTableColumn
blueNet2FuseIndex = _BlueNet2FuseIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 4, 1, 4),
    _BlueNet2FuseIndex_Type()
)
blueNet2FuseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2FuseIndex.setStatus("current")


class _BlueNet2FuseGuid_Type(OctetString):
    """Custom type blueNet2FuseGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2FuseGuid_Type.__name__ = "OctetString"
_BlueNet2FuseGuid_Object = MibTableColumn
blueNet2FuseGuid = _BlueNet2FuseGuid_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 4, 1, 5),
    _BlueNet2FuseGuid_Type()
)
blueNet2FuseGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2FuseGuid.setStatus("current")


class _BlueNet2FuseName_Type(DisplayString):
    """Custom type blueNet2FuseName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BlueNet2FuseName_Type.__name__ = "DisplayString"
_BlueNet2FuseName_Object = MibTableColumn
blueNet2FuseName = _BlueNet2FuseName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 4, 1, 6),
    _BlueNet2FuseName_Type()
)
blueNet2FuseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2FuseName.setStatus("current")


class _BlueNet2FuseFriendlyName_Type(DisplayString):
    """Custom type blueNet2FuseFriendlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BlueNet2FuseFriendlyName_Type.__name__ = "DisplayString"
_BlueNet2FuseFriendlyName_Object = MibTableColumn
blueNet2FuseFriendlyName = _BlueNet2FuseFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 4, 1, 7),
    _BlueNet2FuseFriendlyName_Type()
)
blueNet2FuseFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2FuseFriendlyName.setStatus("current")


class _BlueNet2FuseDescription_Type(DisplayString):
    """Custom type blueNet2FuseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2FuseDescription_Type.__name__ = "DisplayString"
_BlueNet2FuseDescription_Object = MibTableColumn
blueNet2FuseDescription = _BlueNet2FuseDescription_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 4, 1, 8),
    _BlueNet2FuseDescription_Type()
)
blueNet2FuseDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2FuseDescription.setStatus("current")
_BlueNet2FuseType_Type = ObjectIdentifier
_BlueNet2FuseType_Object = MibTableColumn
blueNet2FuseType = _BlueNet2FuseType_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 4, 1, 9),
    _BlueNet2FuseType_Type()
)
blueNet2FuseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2FuseType.setStatus("current")
_BlueNet2FuseStatus_Type = BlueNet2EntityStates
_BlueNet2FuseStatus_Object = MibTableColumn
blueNet2FuseStatus = _BlueNet2FuseStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 4, 1, 10),
    _BlueNet2FuseStatus_Type()
)
blueNet2FuseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2FuseStatus.setStatus("current")
_BlueNet2FuseNumberOfSockets_Type = Unsigned32
_BlueNet2FuseNumberOfSockets_Object = MibTableColumn
blueNet2FuseNumberOfSockets = _BlueNet2FuseNumberOfSockets_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 4, 1, 11),
    _BlueNet2FuseNumberOfSockets_Type()
)
blueNet2FuseNumberOfSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2FuseNumberOfSockets.setStatus("current")
_BlueNet2SocketTable_Object = MibTable
blueNet2SocketTable = _BlueNet2SocketTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 5)
)
if mibBuilder.loadTexts:
    blueNet2SocketTable.setStatus("current")
_BlueNet2SocketEntry_Object = MibTableRow
blueNet2SocketEntry = _BlueNet2SocketEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 5, 1)
)
blueNet2SocketEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2SocketDevice"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2SocketCircuit"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2SocketPhase"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2SocketIndex"),
)
if mibBuilder.loadTexts:
    blueNet2SocketEntry.setStatus("current")


class _BlueNet2SocketDevice_Type(Unsigned32):
    """Custom type blueNet2SocketDevice based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_BlueNet2SocketDevice_Type.__name__ = "Unsigned32"
_BlueNet2SocketDevice_Object = MibTableColumn
blueNet2SocketDevice = _BlueNet2SocketDevice_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 5, 1, 1),
    _BlueNet2SocketDevice_Type()
)
blueNet2SocketDevice.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SocketDevice.setStatus("current")


class _BlueNet2SocketCircuit_Type(Unsigned32):
    """Custom type blueNet2SocketCircuit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_BlueNet2SocketCircuit_Type.__name__ = "Unsigned32"
_BlueNet2SocketCircuit_Object = MibTableColumn
blueNet2SocketCircuit = _BlueNet2SocketCircuit_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 5, 1, 2),
    _BlueNet2SocketCircuit_Type()
)
blueNet2SocketCircuit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SocketCircuit.setStatus("current")


class _BlueNet2SocketPhase_Type(Unsigned32):
    """Custom type blueNet2SocketPhase based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_BlueNet2SocketPhase_Type.__name__ = "Unsigned32"
_BlueNet2SocketPhase_Object = MibTableColumn
blueNet2SocketPhase = _BlueNet2SocketPhase_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 5, 1, 3),
    _BlueNet2SocketPhase_Type()
)
blueNet2SocketPhase.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SocketPhase.setStatus("current")


class _BlueNet2SocketFuse_Type(Unsigned32):
    """Custom type blueNet2SocketFuse based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BlueNet2SocketFuse_Type.__name__ = "Unsigned32"
_BlueNet2SocketFuse_Object = MibTableColumn
blueNet2SocketFuse = _BlueNet2SocketFuse_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 5, 1, 4),
    _BlueNet2SocketFuse_Type()
)
blueNet2SocketFuse.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SocketFuse.setStatus("current")


class _BlueNet2SocketIndex_Type(Unsigned32):
    """Custom type blueNet2SocketIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_BlueNet2SocketIndex_Type.__name__ = "Unsigned32"
_BlueNet2SocketIndex_Object = MibTableColumn
blueNet2SocketIndex = _BlueNet2SocketIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 5, 1, 5),
    _BlueNet2SocketIndex_Type()
)
blueNet2SocketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SocketIndex.setStatus("current")


class _BlueNet2SocketGuid_Type(OctetString):
    """Custom type blueNet2SocketGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2SocketGuid_Type.__name__ = "OctetString"
_BlueNet2SocketGuid_Object = MibTableColumn
blueNet2SocketGuid = _BlueNet2SocketGuid_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 5, 1, 6),
    _BlueNet2SocketGuid_Type()
)
blueNet2SocketGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SocketGuid.setStatus("current")


class _BlueNet2SocketName_Type(DisplayString):
    """Custom type blueNet2SocketName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BlueNet2SocketName_Type.__name__ = "DisplayString"
_BlueNet2SocketName_Object = MibTableColumn
blueNet2SocketName = _BlueNet2SocketName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 5, 1, 7),
    _BlueNet2SocketName_Type()
)
blueNet2SocketName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SocketName.setStatus("current")


class _BlueNet2SocketFriendlyName_Type(DisplayString):
    """Custom type blueNet2SocketFriendlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BlueNet2SocketFriendlyName_Type.__name__ = "DisplayString"
_BlueNet2SocketFriendlyName_Object = MibTableColumn
blueNet2SocketFriendlyName = _BlueNet2SocketFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 5, 1, 8),
    _BlueNet2SocketFriendlyName_Type()
)
blueNet2SocketFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SocketFriendlyName.setStatus("current")


class _BlueNet2SocketDescription_Type(DisplayString):
    """Custom type blueNet2SocketDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2SocketDescription_Type.__name__ = "DisplayString"
_BlueNet2SocketDescription_Object = MibTableColumn
blueNet2SocketDescription = _BlueNet2SocketDescription_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 5, 1, 9),
    _BlueNet2SocketDescription_Type()
)
blueNet2SocketDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SocketDescription.setStatus("current")
_BlueNet2SocketType_Type = ObjectIdentifier
_BlueNet2SocketType_Object = MibTableColumn
blueNet2SocketType = _BlueNet2SocketType_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 5, 1, 10),
    _BlueNet2SocketType_Type()
)
blueNet2SocketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SocketType.setStatus("current")
_BlueNet2SocketStatus_Type = BlueNet2EntityStates
_BlueNet2SocketStatus_Object = MibTableColumn
blueNet2SocketStatus = _BlueNet2SocketStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 5, 1, 11),
    _BlueNet2SocketStatus_Type()
)
blueNet2SocketStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SocketStatus.setStatus("current")
_BlueNet2SocketMode_Type = BlueNet2SocketModes
_BlueNet2SocketMode_Object = MibTableColumn
blueNet2SocketMode = _BlueNet2SocketMode_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 5, 1, 12),
    _BlueNet2SocketMode_Type()
)
blueNet2SocketMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SocketMode.setStatus("current")
_BlueNet2SocketIdentify_Type = BlueNet2SocketModes
_BlueNet2SocketIdentify_Object = MibTableColumn
blueNet2SocketIdentify = _BlueNet2SocketIdentify_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 5, 1, 13),
    _BlueNet2SocketIdentify_Type()
)
blueNet2SocketIdentify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SocketIdentify.setStatus("current")


class _BlueNet2SocketMemberIndex_Type(Unsigned32):
    """Custom type blueNet2SocketMemberIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_BlueNet2SocketMemberIndex_Type.__name__ = "Unsigned32"
_BlueNet2SocketMemberIndex_Object = MibTableColumn
blueNet2SocketMemberIndex = _BlueNet2SocketMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 5, 1, 14),
    _BlueNet2SocketMemberIndex_Type()
)
blueNet2SocketMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SocketMemberIndex.setStatus("current")
_BlueNet2RcmTable_Object = MibTable
blueNet2RcmTable = _BlueNet2RcmTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6)
)
if mibBuilder.loadTexts:
    blueNet2RcmTable.setStatus("current")
_BlueNet2RcmEntry_Object = MibTableRow
blueNet2RcmEntry = _BlueNet2RcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1)
)
blueNet2RcmEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2RcmDevice"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2RcmCircuit"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2RcmPhase"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2RcmFuse"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2RcmSocket"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2RcmIndex"),
)
if mibBuilder.loadTexts:
    blueNet2RcmEntry.setStatus("current")


class _BlueNet2RcmDevice_Type(Unsigned32):
    """Custom type blueNet2RcmDevice based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_BlueNet2RcmDevice_Type.__name__ = "Unsigned32"
_BlueNet2RcmDevice_Object = MibTableColumn
blueNet2RcmDevice = _BlueNet2RcmDevice_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1, 1),
    _BlueNet2RcmDevice_Type()
)
blueNet2RcmDevice.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2RcmDevice.setStatus("current")


class _BlueNet2RcmCircuit_Type(Unsigned32):
    """Custom type blueNet2RcmCircuit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BlueNet2RcmCircuit_Type.__name__ = "Unsigned32"
_BlueNet2RcmCircuit_Object = MibTableColumn
blueNet2RcmCircuit = _BlueNet2RcmCircuit_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1, 2),
    _BlueNet2RcmCircuit_Type()
)
blueNet2RcmCircuit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2RcmCircuit.setStatus("current")


class _BlueNet2RcmPhase_Type(Unsigned32):
    """Custom type blueNet2RcmPhase based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_BlueNet2RcmPhase_Type.__name__ = "Unsigned32"
_BlueNet2RcmPhase_Object = MibTableColumn
blueNet2RcmPhase = _BlueNet2RcmPhase_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1, 3),
    _BlueNet2RcmPhase_Type()
)
blueNet2RcmPhase.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2RcmPhase.setStatus("current")


class _BlueNet2RcmFuse_Type(Unsigned32):
    """Custom type blueNet2RcmFuse based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BlueNet2RcmFuse_Type.__name__ = "Unsigned32"
_BlueNet2RcmFuse_Object = MibTableColumn
blueNet2RcmFuse = _BlueNet2RcmFuse_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1, 4),
    _BlueNet2RcmFuse_Type()
)
blueNet2RcmFuse.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2RcmFuse.setStatus("current")


class _BlueNet2RcmSocket_Type(Unsigned32):
    """Custom type blueNet2RcmSocket based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_BlueNet2RcmSocket_Type.__name__ = "Unsigned32"
_BlueNet2RcmSocket_Object = MibTableColumn
blueNet2RcmSocket = _BlueNet2RcmSocket_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1, 5),
    _BlueNet2RcmSocket_Type()
)
blueNet2RcmSocket.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2RcmSocket.setStatus("current")


class _BlueNet2RcmIndex_Type(Unsigned32):
    """Custom type blueNet2RcmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_BlueNet2RcmIndex_Type.__name__ = "Unsigned32"
_BlueNet2RcmIndex_Object = MibTableColumn
blueNet2RcmIndex = _BlueNet2RcmIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1, 6),
    _BlueNet2RcmIndex_Type()
)
blueNet2RcmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2RcmIndex.setStatus("current")


class _BlueNet2RcmGuid_Type(OctetString):
    """Custom type blueNet2RcmGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2RcmGuid_Type.__name__ = "OctetString"
_BlueNet2RcmGuid_Object = MibTableColumn
blueNet2RcmGuid = _BlueNet2RcmGuid_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1, 7),
    _BlueNet2RcmGuid_Type()
)
blueNet2RcmGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2RcmGuid.setStatus("current")


class _BlueNet2RcmName_Type(DisplayString):
    """Custom type blueNet2RcmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BlueNet2RcmName_Type.__name__ = "DisplayString"
_BlueNet2RcmName_Object = MibTableColumn
blueNet2RcmName = _BlueNet2RcmName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1, 8),
    _BlueNet2RcmName_Type()
)
blueNet2RcmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2RcmName.setStatus("current")


class _BlueNet2RcmFriendlyName_Type(DisplayString):
    """Custom type blueNet2RcmFriendlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BlueNet2RcmFriendlyName_Type.__name__ = "DisplayString"
_BlueNet2RcmFriendlyName_Object = MibTableColumn
blueNet2RcmFriendlyName = _BlueNet2RcmFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1, 9),
    _BlueNet2RcmFriendlyName_Type()
)
blueNet2RcmFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2RcmFriendlyName.setStatus("current")


class _BlueNet2RcmDescription_Type(DisplayString):
    """Custom type blueNet2RcmDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2RcmDescription_Type.__name__ = "DisplayString"
_BlueNet2RcmDescription_Object = MibTableColumn
blueNet2RcmDescription = _BlueNet2RcmDescription_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1, 10),
    _BlueNet2RcmDescription_Type()
)
blueNet2RcmDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2RcmDescription.setStatus("current")
_BlueNet2RcmType_Type = ObjectIdentifier
_BlueNet2RcmType_Object = MibTableColumn
blueNet2RcmType = _BlueNet2RcmType_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1, 11),
    _BlueNet2RcmType_Type()
)
blueNet2RcmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2RcmType.setStatus("current")
_BlueNet2RcmStatus_Type = BlueNet2EntityStates
_BlueNet2RcmStatus_Object = MibTableColumn
blueNet2RcmStatus = _BlueNet2RcmStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1, 12),
    _BlueNet2RcmStatus_Type()
)
blueNet2RcmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2RcmStatus.setStatus("current")
_BlueNet2RcmSelftestCommand_Type = BlueNet2RcmSelftestCommand
_BlueNet2RcmSelftestCommand_Object = MibTableColumn
blueNet2RcmSelftestCommand = _BlueNet2RcmSelftestCommand_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1, 13),
    _BlueNet2RcmSelftestCommand_Type()
)
blueNet2RcmSelftestCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2RcmSelftestCommand.setStatus("current")
_BlueNet2RcmSelftestResultValue_Type = BlueNet2RcmSelftestResult
_BlueNet2RcmSelftestResultValue_Object = MibTableColumn
blueNet2RcmSelftestResultValue = _BlueNet2RcmSelftestResultValue_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1, 14),
    _BlueNet2RcmSelftestResultValue_Type()
)
blueNet2RcmSelftestResultValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2RcmSelftestResultValue.setStatus("current")
_BlueNet2RcmSelftestResultACvalue_Type = BlueNet2RcmSelftestResult
_BlueNet2RcmSelftestResultACvalue_Object = MibTableColumn
blueNet2RcmSelftestResultACvalue = _BlueNet2RcmSelftestResultACvalue_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1, 15),
    _BlueNet2RcmSelftestResultACvalue_Type()
)
blueNet2RcmSelftestResultACvalue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2RcmSelftestResultACvalue.setStatus("current")
_BlueNet2RcmSelftestResultDCvalue_Type = BlueNet2RcmSelftestResult
_BlueNet2RcmSelftestResultDCvalue_Object = MibTableColumn
blueNet2RcmSelftestResultDCvalue = _BlueNet2RcmSelftestResultDCvalue_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1, 16),
    _BlueNet2RcmSelftestResultDCvalue_Type()
)
blueNet2RcmSelftestResultDCvalue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2RcmSelftestResultDCvalue.setStatus("current")
_BlueNet2RcmSelftestTimeStamp_Type = DateAndTime
_BlueNet2RcmSelftestTimeStamp_Object = MibTableColumn
blueNet2RcmSelftestTimeStamp = _BlueNet2RcmSelftestTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1, 17),
    _BlueNet2RcmSelftestTimeStamp_Type()
)
blueNet2RcmSelftestTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2RcmSelftestTimeStamp.setStatus("current")


class _BlueNet2RcmSelftestResultStr_Type(DisplayString):
    """Custom type blueNet2RcmSelftestResultStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2RcmSelftestResultStr_Type.__name__ = "DisplayString"
_BlueNet2RcmSelftestResultStr_Object = MibTableColumn
blueNet2RcmSelftestResultStr = _BlueNet2RcmSelftestResultStr_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 6, 1, 18),
    _BlueNet2RcmSelftestResultStr_Type()
)
blueNet2RcmSelftestResultStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2RcmSelftestResultStr.setStatus("current")
_BlueNet2SpdTable_Object = MibTable
blueNet2SpdTable = _BlueNet2SpdTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 7)
)
if mibBuilder.loadTexts:
    blueNet2SpdTable.setStatus("current")
_BlueNet2SpdEntry_Object = MibTableRow
blueNet2SpdEntry = _BlueNet2SpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 7, 1)
)
blueNet2SpdEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2SpdDevice"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2SpdCircuit"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2SpdPhase"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2SpdFuse"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2SpdSocket"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2SpdIndex"),
)
if mibBuilder.loadTexts:
    blueNet2SpdEntry.setStatus("current")


class _BlueNet2SpdDevice_Type(Unsigned32):
    """Custom type blueNet2SpdDevice based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_BlueNet2SpdDevice_Type.__name__ = "Unsigned32"
_BlueNet2SpdDevice_Object = MibTableColumn
blueNet2SpdDevice = _BlueNet2SpdDevice_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 7, 1, 1),
    _BlueNet2SpdDevice_Type()
)
blueNet2SpdDevice.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SpdDevice.setStatus("current")


class _BlueNet2SpdCircuit_Type(Unsigned32):
    """Custom type blueNet2SpdCircuit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_BlueNet2SpdCircuit_Type.__name__ = "Unsigned32"
_BlueNet2SpdCircuit_Object = MibTableColumn
blueNet2SpdCircuit = _BlueNet2SpdCircuit_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 7, 1, 2),
    _BlueNet2SpdCircuit_Type()
)
blueNet2SpdCircuit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SpdCircuit.setStatus("current")


class _BlueNet2SpdPhase_Type(Unsigned32):
    """Custom type blueNet2SpdPhase based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_BlueNet2SpdPhase_Type.__name__ = "Unsigned32"
_BlueNet2SpdPhase_Object = MibTableColumn
blueNet2SpdPhase = _BlueNet2SpdPhase_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 7, 1, 3),
    _BlueNet2SpdPhase_Type()
)
blueNet2SpdPhase.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SpdPhase.setStatus("current")


class _BlueNet2SpdFuse_Type(Unsigned32):
    """Custom type blueNet2SpdFuse based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BlueNet2SpdFuse_Type.__name__ = "Unsigned32"
_BlueNet2SpdFuse_Object = MibTableColumn
blueNet2SpdFuse = _BlueNet2SpdFuse_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 7, 1, 4),
    _BlueNet2SpdFuse_Type()
)
blueNet2SpdFuse.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SpdFuse.setStatus("current")


class _BlueNet2SpdSocket_Type(Unsigned32):
    """Custom type blueNet2SpdSocket based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_BlueNet2SpdSocket_Type.__name__ = "Unsigned32"
_BlueNet2SpdSocket_Object = MibTableColumn
blueNet2SpdSocket = _BlueNet2SpdSocket_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 7, 1, 5),
    _BlueNet2SpdSocket_Type()
)
blueNet2SpdSocket.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SpdSocket.setStatus("current")


class _BlueNet2SpdIndex_Type(Unsigned32):
    """Custom type blueNet2SpdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BlueNet2SpdIndex_Type.__name__ = "Unsigned32"
_BlueNet2SpdIndex_Object = MibTableColumn
blueNet2SpdIndex = _BlueNet2SpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 7, 1, 6),
    _BlueNet2SpdIndex_Type()
)
blueNet2SpdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SpdIndex.setStatus("current")


class _BlueNet2SpdGuid_Type(OctetString):
    """Custom type blueNet2SpdGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2SpdGuid_Type.__name__ = "OctetString"
_BlueNet2SpdGuid_Object = MibTableColumn
blueNet2SpdGuid = _BlueNet2SpdGuid_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 7, 1, 7),
    _BlueNet2SpdGuid_Type()
)
blueNet2SpdGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SpdGuid.setStatus("current")


class _BlueNet2SpdName_Type(DisplayString):
    """Custom type blueNet2SpdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BlueNet2SpdName_Type.__name__ = "DisplayString"
_BlueNet2SpdName_Object = MibTableColumn
blueNet2SpdName = _BlueNet2SpdName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 7, 1, 8),
    _BlueNet2SpdName_Type()
)
blueNet2SpdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SpdName.setStatus("current")


class _BlueNet2SpdFriendlyName_Type(DisplayString):
    """Custom type blueNet2SpdFriendlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BlueNet2SpdFriendlyName_Type.__name__ = "DisplayString"
_BlueNet2SpdFriendlyName_Object = MibTableColumn
blueNet2SpdFriendlyName = _BlueNet2SpdFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 7, 1, 9),
    _BlueNet2SpdFriendlyName_Type()
)
blueNet2SpdFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SpdFriendlyName.setStatus("current")


class _BlueNet2SpdDescription_Type(DisplayString):
    """Custom type blueNet2SpdDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2SpdDescription_Type.__name__ = "DisplayString"
_BlueNet2SpdDescription_Object = MibTableColumn
blueNet2SpdDescription = _BlueNet2SpdDescription_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 7, 1, 10),
    _BlueNet2SpdDescription_Type()
)
blueNet2SpdDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SpdDescription.setStatus("current")
_BlueNet2SpdType_Type = ObjectIdentifier
_BlueNet2SpdType_Object = MibTableColumn
blueNet2SpdType = _BlueNet2SpdType_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 7, 1, 11),
    _BlueNet2SpdType_Type()
)
blueNet2SpdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SpdType.setStatus("current")
_BlueNet2SpdStatus_Type = BlueNet2EntityStates
_BlueNet2SpdStatus_Object = MibTableColumn
blueNet2SpdStatus = _BlueNet2SpdStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 6, 7, 1, 12),
    _BlueNet2SpdStatus_Type()
)
blueNet2SpdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SpdStatus.setStatus("current")
_BlueNet2SocketGroups_ObjectIdentity = ObjectIdentity
blueNet2SocketGroups = _BlueNet2SocketGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7)
)
_BlueNet2SocketGroupInfo_ObjectIdentity = ObjectIdentity
blueNet2SocketGroupInfo = _BlueNet2SocketGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 1)
)
_BlueNet2OverallSocketGroupStatus_Type = BlueNet2ComponentStates
_BlueNet2OverallSocketGroupStatus_Object = MibScalar
blueNet2OverallSocketGroupStatus = _BlueNet2OverallSocketGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 1, 1),
    _BlueNet2OverallSocketGroupStatus_Type()
)
blueNet2OverallSocketGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2OverallSocketGroupStatus.setStatus("current")


class _BlueNet2NumberOfSocketGroups_Type(Unsigned32):
    """Custom type blueNet2NumberOfSocketGroups based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BlueNet2NumberOfSocketGroups_Type.__name__ = "Unsigned32"
_BlueNet2NumberOfSocketGroups_Object = MibScalar
blueNet2NumberOfSocketGroups = _BlueNet2NumberOfSocketGroups_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 1, 2),
    _BlueNet2NumberOfSocketGroups_Type()
)
blueNet2NumberOfSocketGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2NumberOfSocketGroups.setStatus("current")
_BlueNet2LastChangeOverallSocketGroupStatus_Type = TimeTicks
_BlueNet2LastChangeOverallSocketGroupStatus_Object = MibScalar
blueNet2LastChangeOverallSocketGroupStatus = _BlueNet2LastChangeOverallSocketGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 1, 3),
    _BlueNet2LastChangeOverallSocketGroupStatus_Type()
)
blueNet2LastChangeOverallSocketGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeOverallSocketGroupStatus.setStatus("current")
_BlueNet2LastChangeNumberOfSocketGroups_Type = TimeTicks
_BlueNet2LastChangeNumberOfSocketGroups_Object = MibScalar
blueNet2LastChangeNumberOfSocketGroups = _BlueNet2LastChangeNumberOfSocketGroups_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 1, 4),
    _BlueNet2LastChangeNumberOfSocketGroups_Type()
)
blueNet2LastChangeNumberOfSocketGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeNumberOfSocketGroups.setStatus("current")
_BlueNet2LastChangeSocketGroupSettings_Type = TimeTicks
_BlueNet2LastChangeSocketGroupSettings_Object = MibScalar
blueNet2LastChangeSocketGroupSettings = _BlueNet2LastChangeSocketGroupSettings_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 1, 5),
    _BlueNet2LastChangeSocketGroupSettings_Type()
)
blueNet2LastChangeSocketGroupSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeSocketGroupSettings.setStatus("current")
_BlueNet2LastChangeSocketGroups_Type = TimeTicks
_BlueNet2LastChangeSocketGroups_Object = MibScalar
blueNet2LastChangeSocketGroups = _BlueNet2LastChangeSocketGroups_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 1, 6),
    _BlueNet2LastChangeSocketGroups_Type()
)
blueNet2LastChangeSocketGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeSocketGroups.setStatus("current")
_BlueNet2SocketGroupsAccumulatedStatus_Type = BlueNet2EntityBits
_BlueNet2SocketGroupsAccumulatedStatus_Object = MibScalar
blueNet2SocketGroupsAccumulatedStatus = _BlueNet2SocketGroupsAccumulatedStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 1, 7),
    _BlueNet2SocketGroupsAccumulatedStatus_Type()
)
blueNet2SocketGroupsAccumulatedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SocketGroupsAccumulatedStatus.setStatus("current")


class _BlueNet2SocketGroupsInUse_Type(Unsigned32):
    """Custom type blueNet2SocketGroupsInUse based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BlueNet2SocketGroupsInUse_Type.__name__ = "Unsigned32"
_BlueNet2SocketGroupsInUse_Object = MibScalar
blueNet2SocketGroupsInUse = _BlueNet2SocketGroupsInUse_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 1, 8),
    _BlueNet2SocketGroupsInUse_Type()
)
blueNet2SocketGroupsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SocketGroupsInUse.setStatus("current")


class _BlueNet2MaxSocketGroups_Type(Unsigned32):
    """Custom type blueNet2MaxSocketGroups based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BlueNet2MaxSocketGroups_Type.__name__ = "Unsigned32"
_BlueNet2MaxSocketGroups_Object = MibScalar
blueNet2MaxSocketGroups = _BlueNet2MaxSocketGroups_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 1, 9),
    _BlueNet2MaxSocketGroups_Type()
)
blueNet2MaxSocketGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2MaxSocketGroups.setStatus("current")
_BlueNet2SocketGroupTable_Object = MibTable
blueNet2SocketGroupTable = _BlueNet2SocketGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 2)
)
if mibBuilder.loadTexts:
    blueNet2SocketGroupTable.setStatus("current")
_BlueNet2SocketGroupEntry_Object = MibTableRow
blueNet2SocketGroupEntry = _BlueNet2SocketGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 2, 1)
)
blueNet2SocketGroupEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2SocketGroupIndex"),
)
if mibBuilder.loadTexts:
    blueNet2SocketGroupEntry.setStatus("current")


class _BlueNet2SocketGroupIndex_Type(Unsigned32):
    """Custom type blueNet2SocketGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BlueNet2SocketGroupIndex_Type.__name__ = "Unsigned32"
_BlueNet2SocketGroupIndex_Object = MibTableColumn
blueNet2SocketGroupIndex = _BlueNet2SocketGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 2, 1, 1),
    _BlueNet2SocketGroupIndex_Type()
)
blueNet2SocketGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2SocketGroupIndex.setStatus("current")
_BlueNet2SocketGroupRowStatus_Type = RowStatus
_BlueNet2SocketGroupRowStatus_Object = MibTableColumn
blueNet2SocketGroupRowStatus = _BlueNet2SocketGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 2, 1, 2),
    _BlueNet2SocketGroupRowStatus_Type()
)
blueNet2SocketGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    blueNet2SocketGroupRowStatus.setStatus("current")


class _BlueNet2SocketGroupGuid_Type(OctetString):
    """Custom type blueNet2SocketGroupGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2SocketGroupGuid_Type.__name__ = "OctetString"
_BlueNet2SocketGroupGuid_Object = MibTableColumn
blueNet2SocketGroupGuid = _BlueNet2SocketGroupGuid_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 2, 1, 3),
    _BlueNet2SocketGroupGuid_Type()
)
blueNet2SocketGroupGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SocketGroupGuid.setStatus("current")


class _BlueNet2SocketGroupName_Type(DisplayString):
    """Custom type blueNet2SocketGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BlueNet2SocketGroupName_Type.__name__ = "DisplayString"
_BlueNet2SocketGroupName_Object = MibTableColumn
blueNet2SocketGroupName = _BlueNet2SocketGroupName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 2, 1, 4),
    _BlueNet2SocketGroupName_Type()
)
blueNet2SocketGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SocketGroupName.setStatus("current")


class _BlueNet2SocketGroupFriendlyName_Type(DisplayString):
    """Custom type blueNet2SocketGroupFriendlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BlueNet2SocketGroupFriendlyName_Type.__name__ = "DisplayString"
_BlueNet2SocketGroupFriendlyName_Object = MibTableColumn
blueNet2SocketGroupFriendlyName = _BlueNet2SocketGroupFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 2, 1, 5),
    _BlueNet2SocketGroupFriendlyName_Type()
)
blueNet2SocketGroupFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SocketGroupFriendlyName.setStatus("current")


class _BlueNet2SocketGroupDescription_Type(DisplayString):
    """Custom type blueNet2SocketGroupDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2SocketGroupDescription_Type.__name__ = "DisplayString"
_BlueNet2SocketGroupDescription_Object = MibTableColumn
blueNet2SocketGroupDescription = _BlueNet2SocketGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 2, 1, 6),
    _BlueNet2SocketGroupDescription_Type()
)
blueNet2SocketGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SocketGroupDescription.setStatus("current")
_BlueNet2SocketGroupStatus_Type = BlueNet2EntityStates
_BlueNet2SocketGroupStatus_Object = MibTableColumn
blueNet2SocketGroupStatus = _BlueNet2SocketGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 2, 1, 7),
    _BlueNet2SocketGroupStatus_Type()
)
blueNet2SocketGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SocketGroupStatus.setStatus("current")
_BlueNet2SocketGroupMode_Type = BlueNet2SocketModes
_BlueNet2SocketGroupMode_Object = MibTableColumn
blueNet2SocketGroupMode = _BlueNet2SocketGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 2, 1, 8),
    _BlueNet2SocketGroupMode_Type()
)
blueNet2SocketGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SocketGroupMode.setStatus("current")
_BlueNet2SocketGroupIdentify_Type = BlueNet2SocketModes
_BlueNet2SocketGroupIdentify_Object = MibTableColumn
blueNet2SocketGroupIdentify = _BlueNet2SocketGroupIdentify_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 2, 1, 9),
    _BlueNet2SocketGroupIdentify_Type()
)
blueNet2SocketGroupIdentify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SocketGroupIdentify.setStatus("current")
_BlueNet2SocketGroupEntPhysicalIndex_Type = Unsigned32
_BlueNet2SocketGroupEntPhysicalIndex_Object = MibTableColumn
blueNet2SocketGroupEntPhysicalIndex = _BlueNet2SocketGroupEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 2, 1, 10),
    _BlueNet2SocketGroupEntPhysicalIndex_Type()
)
blueNet2SocketGroupEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SocketGroupEntPhysicalIndex.setStatus("current")
_BlueNet2SocketGroupAccumulatedStatus_Type = BlueNet2EntityBits
_BlueNet2SocketGroupAccumulatedStatus_Object = MibTableColumn
blueNet2SocketGroupAccumulatedStatus = _BlueNet2SocketGroupAccumulatedStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 2, 1, 11),
    _BlueNet2SocketGroupAccumulatedStatus_Type()
)
blueNet2SocketGroupAccumulatedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2SocketGroupAccumulatedStatus.setStatus("current")
_BlueNet2SocketGroupMembers_Type = BlueNet2SocketMembers
_BlueNet2SocketGroupMembers_Object = MibTableColumn
blueNet2SocketGroupMembers = _BlueNet2SocketGroupMembers_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 7, 2, 1, 12),
    _BlueNet2SocketGroupMembers_Type()
)
blueNet2SocketGroupMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2SocketGroupMembers.setStatus("current")
_BlueNet2Variables_ObjectIdentity = ObjectIdentity
blueNet2Variables = _BlueNet2Variables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8)
)
_BlueNet2VariableInfo_ObjectIdentity = ObjectIdentity
blueNet2VariableInfo = _BlueNet2VariableInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 1)
)
_BlueNet2OverallVariableStatus_Type = BlueNet2ComponentStates
_BlueNet2OverallVariableStatus_Object = MibScalar
blueNet2OverallVariableStatus = _BlueNet2OverallVariableStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 1, 1),
    _BlueNet2OverallVariableStatus_Type()
)
blueNet2OverallVariableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2OverallVariableStatus.setStatus("current")


class _BlueNet2NumberOfVariables_Type(Unsigned32):
    """Custom type blueNet2NumberOfVariables based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BlueNet2NumberOfVariables_Type.__name__ = "Unsigned32"
_BlueNet2NumberOfVariables_Object = MibScalar
blueNet2NumberOfVariables = _BlueNet2NumberOfVariables_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 1, 2),
    _BlueNet2NumberOfVariables_Type()
)
blueNet2NumberOfVariables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2NumberOfVariables.setStatus("current")
_BlueNet2LastChangeOverallVariableStatus_Type = TimeTicks
_BlueNet2LastChangeOverallVariableStatus_Object = MibScalar
blueNet2LastChangeOverallVariableStatus = _BlueNet2LastChangeOverallVariableStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 1, 3),
    _BlueNet2LastChangeOverallVariableStatus_Type()
)
blueNet2LastChangeOverallVariableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeOverallVariableStatus.setStatus("current")
_BlueNet2LastChangeNumberOfVariables_Type = TimeTicks
_BlueNet2LastChangeNumberOfVariables_Object = MibScalar
blueNet2LastChangeNumberOfVariables = _BlueNet2LastChangeNumberOfVariables_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 1, 4),
    _BlueNet2LastChangeNumberOfVariables_Type()
)
blueNet2LastChangeNumberOfVariables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeNumberOfVariables.setStatus("current")
_BlueNet2LastChangeVariableSettings_Type = TimeTicks
_BlueNet2LastChangeVariableSettings_Object = MibScalar
blueNet2LastChangeVariableSettings = _BlueNet2LastChangeVariableSettings_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 1, 5),
    _BlueNet2LastChangeVariableSettings_Type()
)
blueNet2LastChangeVariableSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeVariableSettings.setStatus("current")
_BlueNet2LastChangeVariableStatus_Type = TimeTicks
_BlueNet2LastChangeVariableStatus_Object = MibScalar
blueNet2LastChangeVariableStatus = _BlueNet2LastChangeVariableStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 1, 6),
    _BlueNet2LastChangeVariableStatus_Type()
)
blueNet2LastChangeVariableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeVariableStatus.setStatus("current")
_BlueNet2VariablesAccumulatedStatus_Type = BlueNet2EntityBits
_BlueNet2VariablesAccumulatedStatus_Object = MibScalar
blueNet2VariablesAccumulatedStatus = _BlueNet2VariablesAccumulatedStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 1, 7),
    _BlueNet2VariablesAccumulatedStatus_Type()
)
blueNet2VariablesAccumulatedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariablesAccumulatedStatus.setStatus("current")
_BlueNet2NumberOfChangesVariableScaling_Type = Unsigned32
_BlueNet2NumberOfChangesVariableScaling_Object = MibScalar
blueNet2NumberOfChangesVariableScaling = _BlueNet2NumberOfChangesVariableScaling_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 1, 8),
    _BlueNet2NumberOfChangesVariableScaling_Type()
)
blueNet2NumberOfChangesVariableScaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2NumberOfChangesVariableScaling.setStatus("current")
_BlueNet2LastChangeVariableScaling_Type = TimeTicks
_BlueNet2LastChangeVariableScaling_Object = MibScalar
blueNet2LastChangeVariableScaling = _BlueNet2LastChangeVariableScaling_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 1, 9),
    _BlueNet2LastChangeVariableScaling_Type()
)
blueNet2LastChangeVariableScaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeVariableScaling.setStatus("current")
_BlueNet2LastChangeVariableReset_Type = TimeTicks
_BlueNet2LastChangeVariableReset_Object = MibScalar
blueNet2LastChangeVariableReset = _BlueNet2LastChangeVariableReset_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 1, 10),
    _BlueNet2LastChangeVariableReset_Type()
)
blueNet2LastChangeVariableReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2LastChangeVariableReset.setStatus("current")
_BlueNet2VariableTable_Object = MibTable
blueNet2VariableTable = _BlueNet2VariableTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 2)
)
if mibBuilder.loadTexts:
    blueNet2VariableTable.setStatus("current")
_BlueNet2VariableEntry_Object = MibTableRow
blueNet2VariableEntry = _BlueNet2VariableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 2, 1)
)
blueNet2VariableEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2VariableId"),
)
if mibBuilder.loadTexts:
    blueNet2VariableEntry.setStatus("current")


class _BlueNet2VariableId_Type(OctetString):
    """Custom type blueNet2VariableId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2VariableId_Type.__name__ = "OctetString"
_BlueNet2VariableId_Object = MibTableColumn
blueNet2VariableId = _BlueNet2VariableId_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 2, 1, 1),
    _BlueNet2VariableId_Type()
)
blueNet2VariableId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2VariableId.setStatus("current")


class _BlueNet2VariableGuid_Type(OctetString):
    """Custom type blueNet2VariableGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2VariableGuid_Type.__name__ = "OctetString"
_BlueNet2VariableGuid_Object = MibTableColumn
blueNet2VariableGuid = _BlueNet2VariableGuid_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 2, 1, 2),
    _BlueNet2VariableGuid_Type()
)
blueNet2VariableGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableGuid.setStatus("current")


class _BlueNet2VariableName_Type(DisplayString):
    """Custom type blueNet2VariableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BlueNet2VariableName_Type.__name__ = "DisplayString"
_BlueNet2VariableName_Object = MibTableColumn
blueNet2VariableName = _BlueNet2VariableName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 2, 1, 3),
    _BlueNet2VariableName_Type()
)
blueNet2VariableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableName.setStatus("current")


class _BlueNet2VariableFriendlyName_Type(DisplayString):
    """Custom type blueNet2VariableFriendlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BlueNet2VariableFriendlyName_Type.__name__ = "DisplayString"
_BlueNet2VariableFriendlyName_Object = MibTableColumn
blueNet2VariableFriendlyName = _BlueNet2VariableFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 2, 1, 4),
    _BlueNet2VariableFriendlyName_Type()
)
blueNet2VariableFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableFriendlyName.setStatus("current")


class _BlueNet2VariableDescription_Type(DisplayString):
    """Custom type blueNet2VariableDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2VariableDescription_Type.__name__ = "DisplayString"
_BlueNet2VariableDescription_Object = MibTableColumn
blueNet2VariableDescription = _BlueNet2VariableDescription_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 2, 1, 5),
    _BlueNet2VariableDescription_Type()
)
blueNet2VariableDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableDescription.setStatus("current")
_BlueNet2VariableType_Type = BlueNet2DataSourceTypes
_BlueNet2VariableType_Object = MibTableColumn
blueNet2VariableType = _BlueNet2VariableType_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 2, 1, 6),
    _BlueNet2VariableType_Type()
)
blueNet2VariableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableType.setStatus("current")
_BlueNet2VariableStatus_Type = BlueNet2EntityStates
_BlueNet2VariableStatus_Object = MibTableColumn
blueNet2VariableStatus = _BlueNet2VariableStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 2, 1, 7),
    _BlueNet2VariableStatus_Type()
)
blueNet2VariableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableStatus.setStatus("current")


class _BlueNet2VariableAlarm_Type(DisplayString):
    """Custom type blueNet2VariableAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BlueNet2VariableAlarm_Type.__name__ = "DisplayString"
_BlueNet2VariableAlarm_Object = MibTableColumn
blueNet2VariableAlarm = _BlueNet2VariableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 2, 1, 8),
    _BlueNet2VariableAlarm_Type()
)
blueNet2VariableAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableAlarm.setStatus("current")
_BlueNet2VariableScaling_Type = Integer32
_BlueNet2VariableScaling_Object = MibTableColumn
blueNet2VariableScaling = _BlueNet2VariableScaling_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 2, 1, 9),
    _BlueNet2VariableScaling_Type()
)
blueNet2VariableScaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableScaling.setStatus("current")
_BlueNet2VariableUnit_Type = BlueNet2DataSourceUnits
_BlueNet2VariableUnit_Object = MibTableColumn
blueNet2VariableUnit = _BlueNet2VariableUnit_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 2, 1, 10),
    _BlueNet2VariableUnit_Type()
)
blueNet2VariableUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableUnit.setStatus("current")


class _BlueNet2VariableSetPoint_Type(Integer32):
    """Custom type blueNet2VariableSetPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("available", 2))
    )


_BlueNet2VariableSetPoint_Type.__name__ = "Integer32"
_BlueNet2VariableSetPoint_Object = MibTableColumn
blueNet2VariableSetPoint = _BlueNet2VariableSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 2, 1, 11),
    _BlueNet2VariableSetPoint_Type()
)
blueNet2VariableSetPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableSetPoint.setStatus("current")


class _BlueNet2VariableMode_Type(Integer32):
    """Custom type blueNet2VariableMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resettable", 0),
          ("reset", 1),
          ("noReset", 2))
    )


_BlueNet2VariableMode_Type.__name__ = "Integer32"
_BlueNet2VariableMode_Object = MibTableColumn
blueNet2VariableMode = _BlueNet2VariableMode_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 2, 1, 12),
    _BlueNet2VariableMode_Type()
)
blueNet2VariableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2VariableMode.setStatus("current")
_BlueNet2VariableEntPhysicalIndex_Type = Unsigned32
_BlueNet2VariableEntPhysicalIndex_Object = MibTableColumn
blueNet2VariableEntPhysicalIndex = _BlueNet2VariableEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 2, 1, 13),
    _BlueNet2VariableEntPhysicalIndex_Type()
)
blueNet2VariableEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableEntPhysicalIndex.setStatus("current")
_BlueNet2VariableSetPointTable_Object = MibTable
blueNet2VariableSetPointTable = _BlueNet2VariableSetPointTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 3)
)
if mibBuilder.loadTexts:
    blueNet2VariableSetPointTable.setStatus("current")
_BlueNet2VariableSetPointEntry_Object = MibTableRow
blueNet2VariableSetPointEntry = _BlueNet2VariableSetPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 3, 1)
)
blueNet2VariableSetPointEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointGuid"),
)
if mibBuilder.loadTexts:
    blueNet2VariableSetPointEntry.setStatus("current")


class _BlueNet2VariableSetPointGuid_Type(OctetString):
    """Custom type blueNet2VariableSetPointGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2VariableSetPointGuid_Type.__name__ = "OctetString"
_BlueNet2VariableSetPointGuid_Object = MibTableColumn
blueNet2VariableSetPointGuid = _BlueNet2VariableSetPointGuid_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 3, 1, 1),
    _BlueNet2VariableSetPointGuid_Type()
)
blueNet2VariableSetPointGuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2VariableSetPointGuid.setStatus("current")


class _BlueNet2VariableSetPointType_Type(Bits):
    """Custom type blueNet2VariableSetPointType based on Bits"""
    namedValues = NamedValues(
        *(("highAlarm", 0),
          ("lowAlarm", 1),
          ("highWarning", 2),
          ("lowWarning", 3))
    )

_BlueNet2VariableSetPointType_Type.__name__ = "Bits"
_BlueNet2VariableSetPointType_Object = MibTableColumn
blueNet2VariableSetPointType = _BlueNet2VariableSetPointType_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 3, 1, 2),
    _BlueNet2VariableSetPointType_Type()
)
blueNet2VariableSetPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableSetPointType.setStatus("current")
_BlueNet2VariableSetPointMinValue_Type = Integer32
_BlueNet2VariableSetPointMinValue_Object = MibTableColumn
blueNet2VariableSetPointMinValue = _BlueNet2VariableSetPointMinValue_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 3, 1, 3),
    _BlueNet2VariableSetPointMinValue_Type()
)
blueNet2VariableSetPointMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableSetPointMinValue.setStatus("current")
_BlueNet2VariableSetPointMaxValue_Type = Integer32
_BlueNet2VariableSetPointMaxValue_Object = MibTableColumn
blueNet2VariableSetPointMaxValue = _BlueNet2VariableSetPointMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 3, 1, 4),
    _BlueNet2VariableSetPointMaxValue_Type()
)
blueNet2VariableSetPointMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableSetPointMaxValue.setStatus("current")
_BlueNet2VariableSetPointLowerAlarm_Type = Integer32
_BlueNet2VariableSetPointLowerAlarm_Object = MibTableColumn
blueNet2VariableSetPointLowerAlarm = _BlueNet2VariableSetPointLowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 3, 1, 5),
    _BlueNet2VariableSetPointLowerAlarm_Type()
)
blueNet2VariableSetPointLowerAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2VariableSetPointLowerAlarm.setStatus("current")
_BlueNet2VariableSetPointLowerWarning_Type = Integer32
_BlueNet2VariableSetPointLowerWarning_Object = MibTableColumn
blueNet2VariableSetPointLowerWarning = _BlueNet2VariableSetPointLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 3, 1, 6),
    _BlueNet2VariableSetPointLowerWarning_Type()
)
blueNet2VariableSetPointLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2VariableSetPointLowerWarning.setStatus("current")
_BlueNet2VariableSetPointUpperWarning_Type = Integer32
_BlueNet2VariableSetPointUpperWarning_Object = MibTableColumn
blueNet2VariableSetPointUpperWarning = _BlueNet2VariableSetPointUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 3, 1, 7),
    _BlueNet2VariableSetPointUpperWarning_Type()
)
blueNet2VariableSetPointUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2VariableSetPointUpperWarning.setStatus("current")
_BlueNet2VariableSetPointUpperAlarm_Type = Integer32
_BlueNet2VariableSetPointUpperAlarm_Object = MibTableColumn
blueNet2VariableSetPointUpperAlarm = _BlueNet2VariableSetPointUpperAlarm_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 3, 1, 8),
    _BlueNet2VariableSetPointUpperAlarm_Type()
)
blueNet2VariableSetPointUpperAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2VariableSetPointUpperAlarm.setStatus("current")


class _BlueNet2VariableSetPointHysteresis_Type(Unsigned32):
    """Custom type blueNet2VariableSetPointHysteresis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BlueNet2VariableSetPointHysteresis_Type.__name__ = "Unsigned32"
_BlueNet2VariableSetPointHysteresis_Object = MibTableColumn
blueNet2VariableSetPointHysteresis = _BlueNet2VariableSetPointHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 3, 1, 9),
    _BlueNet2VariableSetPointHysteresis_Type()
)
blueNet2VariableSetPointHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2VariableSetPointHysteresis.setStatus("current")


class _BlueNet2VariableSetPointRcmACUpperAlarmThreshold_Type(DisplayString):
    """Custom type blueNet2VariableSetPointRcmACUpperAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BlueNet2VariableSetPointRcmACUpperAlarmThreshold_Type.__name__ = "DisplayString"
_BlueNet2VariableSetPointRcmACUpperAlarmThreshold_Object = MibTableColumn
blueNet2VariableSetPointRcmACUpperAlarmThreshold = _BlueNet2VariableSetPointRcmACUpperAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 3, 1, 10),
    _BlueNet2VariableSetPointRcmACUpperAlarmThreshold_Type()
)
blueNet2VariableSetPointRcmACUpperAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2VariableSetPointRcmACUpperAlarmThreshold.setStatus("current")


class _BlueNet2VariableSetPointRcmACUpperAlarmGradient_Type(DisplayString):
    """Custom type blueNet2VariableSetPointRcmACUpperAlarmGradient based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BlueNet2VariableSetPointRcmACUpperAlarmGradient_Type.__name__ = "DisplayString"
_BlueNet2VariableSetPointRcmACUpperAlarmGradient_Object = MibTableColumn
blueNet2VariableSetPointRcmACUpperAlarmGradient = _BlueNet2VariableSetPointRcmACUpperAlarmGradient_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 3, 1, 11),
    _BlueNet2VariableSetPointRcmACUpperAlarmGradient_Type()
)
blueNet2VariableSetPointRcmACUpperAlarmGradient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2VariableSetPointRcmACUpperAlarmGradient.setStatus("current")


class _BlueNet2VariableSetPointRcmACUpperWarningThreshold_Type(DisplayString):
    """Custom type blueNet2VariableSetPointRcmACUpperWarningThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BlueNet2VariableSetPointRcmACUpperWarningThreshold_Type.__name__ = "DisplayString"
_BlueNet2VariableSetPointRcmACUpperWarningThreshold_Object = MibTableColumn
blueNet2VariableSetPointRcmACUpperWarningThreshold = _BlueNet2VariableSetPointRcmACUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 3, 1, 12),
    _BlueNet2VariableSetPointRcmACUpperWarningThreshold_Type()
)
blueNet2VariableSetPointRcmACUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2VariableSetPointRcmACUpperWarningThreshold.setStatus("current")


class _BlueNet2VariableSetPointRcmACUpperWarningGradient_Type(DisplayString):
    """Custom type blueNet2VariableSetPointRcmACUpperWarningGradient based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BlueNet2VariableSetPointRcmACUpperWarningGradient_Type.__name__ = "DisplayString"
_BlueNet2VariableSetPointRcmACUpperWarningGradient_Object = MibTableColumn
blueNet2VariableSetPointRcmACUpperWarningGradient = _BlueNet2VariableSetPointRcmACUpperWarningGradient_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 3, 1, 13),
    _BlueNet2VariableSetPointRcmACUpperWarningGradient_Type()
)
blueNet2VariableSetPointRcmACUpperWarningGradient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blueNet2VariableSetPointRcmACUpperWarningGradient.setStatus("current")
_BlueNet2VariableDataTable_Object = MibTable
blueNet2VariableDataTable = _BlueNet2VariableDataTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 4)
)
if mibBuilder.loadTexts:
    blueNet2VariableDataTable.setStatus("current")
_BlueNet2VariableDataEntry_Object = MibTableRow
blueNet2VariableDataEntry = _BlueNet2VariableDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 4, 1)
)
blueNet2VariableDataEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2VariableGuid"),
)
if mibBuilder.loadTexts:
    blueNet2VariableDataEntry.setStatus("current")


class _BlueNet2VariableDataId_Type(OctetString):
    """Custom type blueNet2VariableDataId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2VariableDataId_Type.__name__ = "OctetString"
_BlueNet2VariableDataId_Object = MibTableColumn
blueNet2VariableDataId = _BlueNet2VariableDataId_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 4, 1, 1),
    _BlueNet2VariableDataId_Type()
)
blueNet2VariableDataId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2VariableDataId.setStatus("current")


class _BlueNet2VariableDataGuid_Type(OctetString):
    """Custom type blueNet2VariableDataGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2VariableDataGuid_Type.__name__ = "OctetString"
_BlueNet2VariableDataGuid_Object = MibTableColumn
blueNet2VariableDataGuid = _BlueNet2VariableDataGuid_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 4, 1, 2),
    _BlueNet2VariableDataGuid_Type()
)
blueNet2VariableDataGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableDataGuid.setStatus("current")
_BlueNet2VariableDataType_Type = BlueNet2DataSourceTypes
_BlueNet2VariableDataType_Object = MibTableColumn
blueNet2VariableDataType = _BlueNet2VariableDataType_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 4, 1, 3),
    _BlueNet2VariableDataType_Type()
)
blueNet2VariableDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableDataType.setStatus("current")
_BlueNet2VariableDataStatus_Type = BlueNet2EntityStates
_BlueNet2VariableDataStatus_Object = MibTableColumn
blueNet2VariableDataStatus = _BlueNet2VariableDataStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 4, 1, 4),
    _BlueNet2VariableDataStatus_Type()
)
blueNet2VariableDataStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableDataStatus.setStatus("current")
_BlueNet2VariableDataValue_Type = Integer32
_BlueNet2VariableDataValue_Object = MibTableColumn
blueNet2VariableDataValue = _BlueNet2VariableDataValue_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 4, 1, 5),
    _BlueNet2VariableDataValue_Type()
)
blueNet2VariableDataValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableDataValue.setStatus("current")
_BlueNet2VariableDataDateTime_Type = DateAndTime
_BlueNet2VariableDataDateTime_Object = MibTableColumn
blueNet2VariableDataDateTime = _BlueNet2VariableDataDateTime_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 4, 1, 6),
    _BlueNet2VariableDataDateTime_Type()
)
blueNet2VariableDataDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableDataDateTime.setStatus("current")
_BlueNet2VariableDataByTypeTable_Object = MibTable
blueNet2VariableDataByTypeTable = _BlueNet2VariableDataByTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 5)
)
if mibBuilder.loadTexts:
    blueNet2VariableDataByTypeTable.setStatus("current")
_BlueNet2VariableDataByTypeEntry_Object = MibTableRow
blueNet2VariableDataByTypeEntry = _BlueNet2VariableDataByTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 5, 1)
)
blueNet2VariableDataByTypeEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2VariableDataByType"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2VariableDataByTypeGuid"),
)
if mibBuilder.loadTexts:
    blueNet2VariableDataByTypeEntry.setStatus("current")
_BlueNet2VariableDataByType_Type = BlueNet2DataSourceTypes
_BlueNet2VariableDataByType_Object = MibTableColumn
blueNet2VariableDataByType = _BlueNet2VariableDataByType_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 5, 1, 1),
    _BlueNet2VariableDataByType_Type()
)
blueNet2VariableDataByType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2VariableDataByType.setStatus("current")


class _BlueNet2VariableDataByTypeGuid_Type(OctetString):
    """Custom type blueNet2VariableDataByTypeGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2VariableDataByTypeGuid_Type.__name__ = "OctetString"
_BlueNet2VariableDataByTypeGuid_Object = MibTableColumn
blueNet2VariableDataByTypeGuid = _BlueNet2VariableDataByTypeGuid_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 5, 1, 2),
    _BlueNet2VariableDataByTypeGuid_Type()
)
blueNet2VariableDataByTypeGuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2VariableDataByTypeGuid.setStatus("current")
_BlueNet2VariableDataByTypeType_Type = BlueNet2DataSourceTypes
_BlueNet2VariableDataByTypeType_Object = MibTableColumn
blueNet2VariableDataByTypeType = _BlueNet2VariableDataByTypeType_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 5, 1, 3),
    _BlueNet2VariableDataByTypeType_Type()
)
blueNet2VariableDataByTypeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableDataByTypeType.setStatus("current")
_BlueNet2VariableDataByTypeStatus_Type = BlueNet2EntityStates
_BlueNet2VariableDataByTypeStatus_Object = MibTableColumn
blueNet2VariableDataByTypeStatus = _BlueNet2VariableDataByTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 5, 1, 4),
    _BlueNet2VariableDataByTypeStatus_Type()
)
blueNet2VariableDataByTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableDataByTypeStatus.setStatus("current")
_BlueNet2VariableDataByTypeValue_Type = Integer32
_BlueNet2VariableDataByTypeValue_Object = MibTableColumn
blueNet2VariableDataByTypeValue = _BlueNet2VariableDataByTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 5, 1, 5),
    _BlueNet2VariableDataByTypeValue_Type()
)
blueNet2VariableDataByTypeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableDataByTypeValue.setStatus("current")
_BlueNet2VariableDataByTypeDateTime_Type = DateAndTime
_BlueNet2VariableDataByTypeDateTime_Object = MibTableColumn
blueNet2VariableDataByTypeDateTime = _BlueNet2VariableDataByTypeDateTime_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 5, 1, 6),
    _BlueNet2VariableDataByTypeDateTime_Type()
)
blueNet2VariableDataByTypeDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableDataByTypeDateTime.setStatus("current")
_BlueNet2VariableDataByStateTable_Object = MibTable
blueNet2VariableDataByStateTable = _BlueNet2VariableDataByStateTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 6)
)
if mibBuilder.loadTexts:
    blueNet2VariableDataByStateTable.setStatus("deprecated")
_BlueNet2VariableDataByStateEntry_Object = MibTableRow
blueNet2VariableDataByStateEntry = _BlueNet2VariableDataByStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 6, 1)
)
blueNet2VariableDataByStateEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2VariableDataByState"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2VariableDataByStateGuid"),
)
if mibBuilder.loadTexts:
    blueNet2VariableDataByStateEntry.setStatus("deprecated")
_BlueNet2VariableDataByState_Type = BlueNet2EntityStates
_BlueNet2VariableDataByState_Object = MibTableColumn
blueNet2VariableDataByState = _BlueNet2VariableDataByState_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 6, 1, 1),
    _BlueNet2VariableDataByState_Type()
)
blueNet2VariableDataByState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2VariableDataByState.setStatus("deprecated")


class _BlueNet2VariableDataByStateGuid_Type(OctetString):
    """Custom type blueNet2VariableDataByStateGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2VariableDataByStateGuid_Type.__name__ = "OctetString"
_BlueNet2VariableDataByStateGuid_Object = MibTableColumn
blueNet2VariableDataByStateGuid = _BlueNet2VariableDataByStateGuid_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 6, 1, 2),
    _BlueNet2VariableDataByStateGuid_Type()
)
blueNet2VariableDataByStateGuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2VariableDataByStateGuid.setStatus("deprecated")
_BlueNet2VariableDataByStateType_Type = BlueNet2DataSourceTypes
_BlueNet2VariableDataByStateType_Object = MibTableColumn
blueNet2VariableDataByStateType = _BlueNet2VariableDataByStateType_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 6, 1, 3),
    _BlueNet2VariableDataByStateType_Type()
)
blueNet2VariableDataByStateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableDataByStateType.setStatus("deprecated")
_BlueNet2VariableDataByStateStatus_Type = BlueNet2EntityStates
_BlueNet2VariableDataByStateStatus_Object = MibTableColumn
blueNet2VariableDataByStateStatus = _BlueNet2VariableDataByStateStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 6, 1, 4),
    _BlueNet2VariableDataByStateStatus_Type()
)
blueNet2VariableDataByStateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableDataByStateStatus.setStatus("deprecated")
_BlueNet2VariableDataByStateValue_Type = Integer32
_BlueNet2VariableDataByStateValue_Object = MibTableColumn
blueNet2VariableDataByStateValue = _BlueNet2VariableDataByStateValue_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 6, 1, 5),
    _BlueNet2VariableDataByStateValue_Type()
)
blueNet2VariableDataByStateValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableDataByStateValue.setStatus("deprecated")
_BlueNet2VariableDataByStateDateTime_Type = DateAndTime
_BlueNet2VariableDataByStateDateTime_Object = MibTableColumn
blueNet2VariableDataByStateDateTime = _BlueNet2VariableDataByStateDateTime_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 6, 1, 6),
    _BlueNet2VariableDataByStateDateTime_Type()
)
blueNet2VariableDataByStateDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableDataByStateDateTime.setStatus("deprecated")
_BlueNet2VariableDataBySourceTable_Object = MibTable
blueNet2VariableDataBySourceTable = _BlueNet2VariableDataBySourceTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 7)
)
if mibBuilder.loadTexts:
    blueNet2VariableDataBySourceTable.setStatus("current")
_BlueNet2VariableDataBySourceEntry_Object = MibTableRow
blueNet2VariableDataBySourceEntry = _BlueNet2VariableDataBySourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 7, 1)
)
blueNet2VariableDataBySourceEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2VariableDataBySource"),
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2VariableDataBySourceGuid"),
)
if mibBuilder.loadTexts:
    blueNet2VariableDataBySourceEntry.setStatus("current")
_BlueNet2VariableDataBySource_Type = BlueNet2EntitySources
_BlueNet2VariableDataBySource_Object = MibTableColumn
blueNet2VariableDataBySource = _BlueNet2VariableDataBySource_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 7, 1, 1),
    _BlueNet2VariableDataBySource_Type()
)
blueNet2VariableDataBySource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2VariableDataBySource.setStatus("current")


class _BlueNet2VariableDataBySourceGuid_Type(OctetString):
    """Custom type blueNet2VariableDataBySourceGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2VariableDataBySourceGuid_Type.__name__ = "OctetString"
_BlueNet2VariableDataBySourceGuid_Object = MibTableColumn
blueNet2VariableDataBySourceGuid = _BlueNet2VariableDataBySourceGuid_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 7, 1, 2),
    _BlueNet2VariableDataBySourceGuid_Type()
)
blueNet2VariableDataBySourceGuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2VariableDataBySourceGuid.setStatus("current")
_BlueNet2VariableDataBySourceType_Type = BlueNet2DataSourceTypes
_BlueNet2VariableDataBySourceType_Object = MibTableColumn
blueNet2VariableDataBySourceType = _BlueNet2VariableDataBySourceType_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 7, 1, 3),
    _BlueNet2VariableDataBySourceType_Type()
)
blueNet2VariableDataBySourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableDataBySourceType.setStatus("current")
_BlueNet2VariableDataBySourceStatus_Type = BlueNet2EntityStates
_BlueNet2VariableDataBySourceStatus_Object = MibTableColumn
blueNet2VariableDataBySourceStatus = _BlueNet2VariableDataBySourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 7, 1, 4),
    _BlueNet2VariableDataBySourceStatus_Type()
)
blueNet2VariableDataBySourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableDataBySourceStatus.setStatus("current")
_BlueNet2VariableDataBySourceValue_Type = Integer32
_BlueNet2VariableDataBySourceValue_Object = MibTableColumn
blueNet2VariableDataBySourceValue = _BlueNet2VariableDataBySourceValue_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 7, 1, 5),
    _BlueNet2VariableDataBySourceValue_Type()
)
blueNet2VariableDataBySourceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableDataBySourceValue.setStatus("current")
_BlueNet2VariableDataBySourceDateTime_Type = DateAndTime
_BlueNet2VariableDataBySourceDateTime_Object = MibTableColumn
blueNet2VariableDataBySourceDateTime = _BlueNet2VariableDataBySourceDateTime_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 8, 7, 1, 6),
    _BlueNet2VariableDataBySourceDateTime_Type()
)
blueNet2VariableDataBySourceDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2VariableDataBySourceDateTime.setStatus("current")
_BlueNet2MPStates_ObjectIdentity = ObjectIdentity
blueNet2MPStates = _BlueNet2MPStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 9)
)
_BlueNet2MPTable_Object = MibTable
blueNet2MPTable = _BlueNet2MPTable_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 9, 1)
)
if mibBuilder.loadTexts:
    blueNet2MPTable.setStatus("current")
_BlueNet2MPEntry_Object = MibTableRow
blueNet2MPEntry = _BlueNet2MPEntry_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 9, 1, 1)
)
blueNet2MPEntry.setIndexNames(
    (0, "BACHMANN-BLUENET2-MIB", "blueNet2MPID"),
)
if mibBuilder.loadTexts:
    blueNet2MPEntry.setStatus("current")


class _BlueNet2MPID_Type(OctetString):
    """Custom type blueNet2MPID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2MPID_Type.__name__ = "OctetString"
_BlueNet2MPID_Object = MibTableColumn
blueNet2MPID = _BlueNet2MPID_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 9, 1, 1, 1),
    _BlueNet2MPID_Type()
)
blueNet2MPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blueNet2MPID.setStatus("current")


class _BlueNet2MPGuid_Type(OctetString):
    """Custom type blueNet2MPGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BlueNet2MPGuid_Type.__name__ = "OctetString"
_BlueNet2MPGuid_Object = MibTableColumn
blueNet2MPGuid = _BlueNet2MPGuid_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 9, 1, 1, 2),
    _BlueNet2MPGuid_Type()
)
blueNet2MPGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2MPGuid.setStatus("current")


class _BlueNet2MPName_Type(DisplayString):
    """Custom type blueNet2MPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BlueNet2MPName_Type.__name__ = "DisplayString"
_BlueNet2MPName_Object = MibTableColumn
blueNet2MPName = _BlueNet2MPName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 9, 1, 1, 3),
    _BlueNet2MPName_Type()
)
blueNet2MPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2MPName.setStatus("current")


class _BlueNet2MPFriendlyName_Type(DisplayString):
    """Custom type blueNet2MPFriendlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BlueNet2MPFriendlyName_Type.__name__ = "DisplayString"
_BlueNet2MPFriendlyName_Object = MibTableColumn
blueNet2MPFriendlyName = _BlueNet2MPFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 9, 1, 1, 4),
    _BlueNet2MPFriendlyName_Type()
)
blueNet2MPFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2MPFriendlyName.setStatus("current")
_BlueNet2MPState_Type = BlueNet2EntityStates
_BlueNet2MPState_Object = MibTableColumn
blueNet2MPState = _BlueNet2MPState_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 9, 1, 1, 5),
    _BlueNet2MPState_Type()
)
blueNet2MPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2MPState.setStatus("current")
_BlueNet2MPTimeStamp_Type = DateAndTime
_BlueNet2MPTimeStamp_Object = MibTableColumn
blueNet2MPTimeStamp = _BlueNet2MPTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 31770, 2, 2, 9, 1, 1, 6),
    _BlueNet2MPTimeStamp_Type()
)
blueNet2MPTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueNet2MPTimeStamp.setStatus("current")
_BlueNet2Traps_ObjectIdentity = ObjectIdentity
blueNet2Traps = _BlueNet2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 3)
)
_BlueNet2TrapPrefix_ObjectIdentity = ObjectIdentity
blueNet2TrapPrefix = _BlueNet2TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 3, 0)
)
_BlueNet2Conformance_ObjectIdentity = ObjectIdentity
blueNet2Conformance = _BlueNet2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4)
)
_BlueNet2Compliances_ObjectIdentity = ObjectIdentity
blueNet2Compliances = _BlueNet2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 1)
)
_BlueNet2Groups_ObjectIdentity = ObjectIdentity
blueNet2Groups = _BlueNet2Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2)
)

# Managed Objects groups

blueNet2TrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 1)
)
blueNet2TrapGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2DeviceGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceAlarm"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorAlarm"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataValue"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointLowerAlarm"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointLowerWarning"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointUpperWarning"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointUpperAlarm"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2TrapGroup.setStatus("current")

blueNet2IdentificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 3)
)
blueNet2IdentificationGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2IdProductVendor"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2IdProductURI"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2IdProductName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2IdProductPartNr"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2IdProductSNr"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2IdProductDate"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2IdProductFacility"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2IdProductCaps"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2IdProductFwV"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2IdProductHwV"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2IdProductSwV"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2IdProductOsV"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2IdProductArch"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2IdProductMAC"))
)
if mibBuilder.loadTexts:
    blueNet2IdentificationGroup.setStatus("current")

blueNet2InformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 4)
)
blueNet2InformationGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2InfoUpTime"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2InfoOverallStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2InfoNumberOfChanges"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2InfoLastChange"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2InfoAccumulatedStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2InfoLoadAverage"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2InfoMessageStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2InfoMessageTime"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2InfoMessageText"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2InfoMessageNumberOfOks"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2InfoMessageNumberOfWarnings"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2InfoMessageNumberOfErrors"))
)
if mibBuilder.loadTexts:
    blueNet2InformationGroup.setStatus("current")

blueNet2ConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 5)
)
blueNet2ConfigurationGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2Alias"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2Language"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2FtpAccess"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2FtpPort"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2HttpAccess"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2HttpPort"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2HttpsPort"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SftpAccess"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SftpPort"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SshAccess"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SshPort"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2TelnetAccess"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2TelnetPort"))
)
if mibBuilder.loadTexts:
    blueNet2ConfigurationGroup.setStatus("current")

blueNet2SnmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 6)
)
blueNet2SnmpGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2SnmpVersions"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2MaxTrapReceivers"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2TrapReceiverRowStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2TrapReceiverProtocol"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2TrapReceiverAddress"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2TrapReceiverFriendlyName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2TrapReceiverDescription"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2TrapReceiverCommunity"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2TrapReceiverUsername"))
)
if mibBuilder.loadTexts:
    blueNet2SnmpGroup.setStatus("current")

blueNet2ModbusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 7)
)
blueNet2ModbusGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2ModbusVersions"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2ModbusService"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2ModbusTcpPort"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2ModbusSerialMode"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2MaxModbusTcpMasters"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2ModbusTcpRowStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2ModbusTcpAccess"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2ModbusTcpMaster"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2ModbusTcpFriendlyName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2ModbusTcpDescription"))
)
if mibBuilder.loadTexts:
    blueNet2ModbusGroup.setStatus("current")

blueNet2NtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 8)
)
blueNet2NtpGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2DateTime"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2NtpService"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2NtpPort"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2NtpTimeZone"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2MaxNtpServers"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2NtpServerRowStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2NtpServerAddress"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2NtpServerFriendlyName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2NtpServerDescription"))
)
if mibBuilder.loadTexts:
    blueNet2NtpGroup.setStatus("current")

blueNet2SmtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 9)
)
blueNet2SmtpGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2SmtpService"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SmtpPort"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SmtpServer"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SmtpAuth"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SmtpUsername"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SmtpPassword"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SmtpFrom"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SmtpReply"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2MaxSmtpReceivers"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SmtpReceiverRowStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SmtpReceiverAddress"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SmtpReceiverFriendlyName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SmtpReceiverDescription"))
)
if mibBuilder.loadTexts:
    blueNet2SmtpGroup.setStatus("current")

blueNet2SyslogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 10)
)
blueNet2SyslogGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2SyslogService"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SyslogFacility"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2MaxSyslogServers"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SyslogServerRowStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SyslogServerAddress"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SyslogServerPort"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SyslogServerFriendlyName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SyslogServerDescription"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SyslogServerProtocol"))
)
if mibBuilder.loadTexts:
    blueNet2SyslogGroup.setStatus("current")

blueNet2DeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 11)
)
blueNet2DeviceGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2OverallDeviceStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2NumberOfDevices"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeOverallDeviceStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeNumberOfDevices"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeDeviceSettings"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeDevices"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DevicesAccumulatedStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceFriendlyName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceDescription"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceType"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceAlarm"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceLastChange"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceEntPhysicalIndex"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DevicePartNr"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceSNr"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceFwV"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceHwV"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceSwV"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceOsV"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceMAC"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceNumberOfSensors"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceNumberOfCircuits"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceNumberOfPhases"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceNumberOfFuses"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceNumberOfSockets"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceNumberOfRCMs"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceNumberOfVars"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceLocation"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceProductDate"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceModbusAddr"))
)
if mibBuilder.loadTexts:
    blueNet2DeviceGroup.setStatus("current")

blueNet2SensorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 12)
)
blueNet2SensorGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2OverallSensorStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2NumberOfSensors"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeOverallSensorStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeNumberOfSensors"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeSensorSettings"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeSensors"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorsAccumulatedStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorFriendlyName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorDescription"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorType"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorAlarm"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorLastChange"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorEntPhysicalIndex"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorNumberOfVars"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorHwV"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorFwV"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorSNr"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorVariableGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorVariableName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorVariableFriendlyName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorVariableDescription"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorVariableGPIOMode"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorVariableGPIOSwitch"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorVariableGPIOState"))
)
if mibBuilder.loadTexts:
    blueNet2SensorGroup.setStatus("current")

blueNet2CircuitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 13)
)
blueNet2CircuitGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2OverallCircuitStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2NumberOfCircuits"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeOverallCircuitStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeNumberOfCircuits"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeCircuitSettings"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeCircuits"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2CircuitGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2CircuitName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2CircuitFriendlyName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2CircuitDescription"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2CircuitType"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2CircuitStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2CircuitNumberOfPhases"))
)
if mibBuilder.loadTexts:
    blueNet2CircuitGroup.setStatus("current")

blueNet2PhaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 14)
)
blueNet2PhaseGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2PhaseGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2PhaseName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2PhaseFriendlyName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2PhaseDescription"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2PhaseStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2PhaseNumberOfFuses"))
)
if mibBuilder.loadTexts:
    blueNet2PhaseGroup.setStatus("current")

blueNet2FuseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 15)
)
blueNet2FuseGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2FuseGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2FuseName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2FuseFriendlyName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2FuseDescription"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2FuseType"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2FuseStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2FuseNumberOfSockets"))
)
if mibBuilder.loadTexts:
    blueNet2FuseGroup.setStatus("current")

blueNet2SocketGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 16)
)
blueNet2SocketGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2SocketGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketFriendlyName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketDescription"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketType"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketMode"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketIdentify"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketMemberIndex"))
)
if mibBuilder.loadTexts:
    blueNet2SocketGroup.setStatus("current")

blueNet2RcmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 17)
)
blueNet2RcmGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2RcmGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2RcmName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2RcmFriendlyName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2RcmDescription"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2RcmType"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2RcmStatus"))
)
if mibBuilder.loadTexts:
    blueNet2RcmGroup.setStatus("current")

blueNet2SocketGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 18)
)
blueNet2SocketGroupGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2OverallSocketGroupStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2NumberOfSocketGroups"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeOverallSocketGroupStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeNumberOfSocketGroups"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeSocketGroupSettings"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeSocketGroups"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketGroupsAccumulatedStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketGroupsInUse"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2MaxSocketGroups"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketGroupRowStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketGroupGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketGroupName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketGroupFriendlyName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketGroupDescription"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketGroupStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketGroupMode"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketGroupIdentify"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketGroupEntPhysicalIndex"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketGroupAccumulatedStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketGroupMembers"))
)
if mibBuilder.loadTexts:
    blueNet2SocketGroupGroup.setStatus("current")

blueNet2VariableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 19)
)
blueNet2VariableGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2OverallVariableStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2NumberOfVariables"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeOverallVariableStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeNumberOfVariables"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeVariableSettings"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeVariableStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariablesAccumulatedStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2NumberOfChangesVariableScaling"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeVariableScaling"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2LastChangeVariableReset"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableFriendlyName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDescription"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableType"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableAlarm"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableScaling"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableUnit"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPoint"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableMode"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableEntPhysicalIndex"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointType"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointMinValue"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointMaxValue"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointLowerAlarm"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointLowerWarning"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointUpperWarning"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointUpperAlarm"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointHysteresis"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointRcmACUpperAlarmThreshold"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointRcmACUpperAlarmGradient"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointRcmACUpperWarningThreshold"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointRcmACUpperWarningGradient"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataType"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataValue"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataDateTime"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataByTypeType"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataByTypeStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataByTypeValue"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataByTypeDateTime"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataByStateType"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataByStateStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataByStateValue"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataByStateDateTime"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataBySourceType"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataBySourceStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataBySourceValue"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataBySourceDateTime"))
)
if mibBuilder.loadTexts:
    blueNet2VariableGroup.setStatus("current")

blueNet2MPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 20)
)
blueNet2MPGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2MPGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2MPName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2MPFriendlyName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2MPState"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2MPTimeStamp"))
)
if mibBuilder.loadTexts:
    blueNet2MPGroup.setStatus("current")

blueNet2SpdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 21)
)
blueNet2SpdGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2SpdGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SpdName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SpdFriendlyName"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SpdDescription"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SpdType"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SpdStatus"))
)
if mibBuilder.loadTexts:
    blueNet2SpdGroup.setStatus("current")


# Notification objects

blueNet2PduStatusOkNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 0, 0, 1)
)
blueNet2PduStatusOkNotification.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2DeviceGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2PduStatusOkNotification.setStatus(
        "current"
    )

blueNet2PduStatusWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 0, 0, 2)
)
blueNet2PduStatusWarningNotification.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2DeviceGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2PduStatusWarningNotification.setStatus(
        "current"
    )

blueNet2PduStatusAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 0, 0, 3)
)
blueNet2PduStatusAlarmNotification.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2DeviceGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2PduStatusAlarmNotification.setStatus(
        "current"
    )

blueNet2SensorStatusOkNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 0, 0, 4)
)
blueNet2SensorStatusOkNotification.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2SensorGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2SensorStatusOkNotification.setStatus(
        "current"
    )

blueNet2SensorStatusWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 0, 0, 5)
)
blueNet2SensorStatusWarningNotification.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2SensorGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2SensorStatusWarningNotification.setStatus(
        "current"
    )

blueNet2SensorStatusAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 0, 0, 6)
)
blueNet2SensorStatusAlarmNotification.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2SensorGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2SensorStatusAlarmNotification.setStatus(
        "current"
    )

blueNet2VariableStatusOkNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 0, 0, 7)
)
blueNet2VariableStatusOkNotification.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataValue"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2VariableStatusOkNotification.setStatus(
        "current"
    )

blueNet2VariableLowerWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 0, 0, 8)
)
blueNet2VariableLowerWarningNotification.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataValue"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointLowerAlarm"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2VariableLowerWarningNotification.setStatus(
        "current"
    )

blueNet2VariableUpperWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 0, 0, 9)
)
blueNet2VariableUpperWarningNotification.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataValue"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointUpperWarning"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2VariableUpperWarningNotification.setStatus(
        "current"
    )

blueNet2VariableLowerAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 0, 0, 10)
)
blueNet2VariableLowerAlarmNotification.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataValue"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointLowerAlarm"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2VariableLowerAlarmNotification.setStatus(
        "current"
    )

blueNet2VariableUpperAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 0, 0, 11)
)
blueNet2VariableUpperAlarmNotification.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataValue"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointUpperAlarm"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2VariableUpperAlarmNotification.setStatus(
        "current"
    )

blueNet2ReconfigAgentNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 0, 0, 98)
)
blueNet2ReconfigAgentNotification.setObjects(
    ("SNMPv2-MIB", "sysObjectID")
)
if mibBuilder.loadTexts:
    blueNet2ReconfigAgentNotification.setStatus(
        "current"
    )

blueNet2ShutdownAgentNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 0, 0, 99)
)
blueNet2ShutdownAgentNotification.setObjects(
    ("SNMPv2-MIB", "sysObjectID")
)
if mibBuilder.loadTexts:
    blueNet2ShutdownAgentNotification.setStatus(
        "current"
    )

blueNet2PduStatusOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 3, 0, 1)
)
blueNet2PduStatusOkTrap.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2DeviceGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2PduStatusOkTrap.setStatus(
        "current"
    )

blueNet2PduStatusWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 3, 0, 2)
)
blueNet2PduStatusWarningTrap.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2DeviceGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2PduStatusWarningTrap.setStatus(
        "current"
    )

blueNet2PduStatusAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 3, 0, 3)
)
blueNet2PduStatusAlarmTrap.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2DeviceGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2PduStatusAlarmTrap.setStatus(
        "current"
    )

blueNet2SensorStatusOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 3, 0, 4)
)
blueNet2SensorStatusOkTrap.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2SensorGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2SensorStatusOkTrap.setStatus(
        "current"
    )

blueNet2SensorStatusWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 3, 0, 5)
)
blueNet2SensorStatusWarningTrap.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2SensorGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2SensorStatusWarningTrap.setStatus(
        "current"
    )

blueNet2SensorStatusAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 3, 0, 6)
)
blueNet2SensorStatusAlarmTrap.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2SensorGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2SensorStatusAlarmTrap.setStatus(
        "current"
    )

blueNet2VariableStatusOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 3, 0, 7)
)
blueNet2VariableStatusOkTrap.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataValue"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2VariableStatusOkTrap.setStatus(
        "current"
    )

blueNet2VariableLowerWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 3, 0, 8)
)
blueNet2VariableLowerWarningTrap.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataValue"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointLowerAlarm"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2VariableLowerWarningTrap.setStatus(
        "current"
    )

blueNet2VariableUpperWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 3, 0, 9)
)
blueNet2VariableUpperWarningTrap.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataValue"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointUpperWarning"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2VariableUpperWarningTrap.setStatus(
        "current"
    )

blueNet2VariableLowerAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 3, 0, 10)
)
blueNet2VariableLowerAlarmTrap.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataValue"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointLowerAlarm"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2VariableLowerAlarmTrap.setStatus(
        "current"
    )

blueNet2VariableUpperAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 3, 0, 11)
)
blueNet2VariableUpperAlarmTrap.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataGuid"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataStatus"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableDataValue"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableSetPointUpperAlarm"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableAlarm"))
)
if mibBuilder.loadTexts:
    blueNet2VariableUpperAlarmTrap.setStatus(
        "current"
    )

blueNet2RCMSelftestResultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 3, 0, 12)
)
blueNet2RCMSelftestResultTrap.setObjects(
    ("BACHMANN-BLUENET2-MIB", "blueNet2RcmSelftestResultStr")
)
if mibBuilder.loadTexts:
    blueNet2RCMSelftestResultTrap.setStatus(
        "current"
    )

blueNet2ReconfigAgentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 3, 0, 98)
)
blueNet2ReconfigAgentTrap.setObjects(
    ("SNMPv2-MIB", "sysObjectID")
)
if mibBuilder.loadTexts:
    blueNet2ReconfigAgentTrap.setStatus(
        "current"
    )

blueNet2ShutdownAgentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 31770, 2, 3, 0, 99)
)
blueNet2ShutdownAgentTrap.setObjects(
    ("SNMPv2-MIB", "sysObjectID")
)
if mibBuilder.loadTexts:
    blueNet2ShutdownAgentTrap.setStatus(
        "current"
    )


# Notifications groups

blueNet2NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 2, 2)
)
blueNet2NotificationGroup.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2PduStatusOkNotification"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2PduStatusWarningNotification"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2PduStatusAlarmNotification"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorStatusOkNotification"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorStatusWarningNotification"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorStatusAlarmNotification"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableStatusOkNotification"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableLowerWarningNotification"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableUpperWarningNotification"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableLowerAlarmNotification"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableUpperAlarmNotification"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2ReconfigAgentNotification"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2ShutdownAgentNotification"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2PduStatusOkTrap"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2PduStatusWarningTrap"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2PduStatusAlarmTrap"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorStatusOkTrap"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorStatusWarningTrap"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorStatusAlarmTrap"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableStatusOkTrap"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableLowerWarningTrap"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableUpperWarningTrap"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableLowerAlarmTrap"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableUpperAlarmTrap"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2RCMSelftestResultTrap"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2ReconfigAgentTrap"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2ShutdownAgentTrap"))
)
if mibBuilder.loadTexts:
    blueNet2NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

blueNet2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31770, 2, 4, 1, 1)
)
blueNet2Compliance.setObjects(
      *(("BACHMANN-BLUENET2-MIB", "blueNet2NotificationGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2TrapGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2IdentificationGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2InformationGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2ConfigurationGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2RcmGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SpdGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SmtpGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SnmpGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2NtpGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2ModbusGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2CircuitGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2MPGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2NotificationGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2TrapGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2IdentificationGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2InformationGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2ConfigurationGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2NtpGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SyslogGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SmtpGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SnmpGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2ModbusGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2DeviceGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SensorGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2CircuitGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2PhaseGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2FuseGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2SocketGroupGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2VariableGroup"),
        ("BACHMANN-BLUENET2-MIB", "blueNet2MPGroup"))
)
if mibBuilder.loadTexts:
    blueNet2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BACHMANN-BLUENET2-MIB",
    **{"BlueNet2ComponentStates": BlueNet2ComponentStates,
       "BlueNet2EntitySources": BlueNet2EntitySources,
       "BlueNet2EntityStates": BlueNet2EntityStates,
       "BlueNet2EntityBits": BlueNet2EntityBits,
       "BlueNet2DataSourceTypes": BlueNet2DataSourceTypes,
       "BlueNet2DataSourceUnits": BlueNet2DataSourceUnits,
       "BlueNet2InfoMessageSources": BlueNet2InfoMessageSources,
       "BlueNet2SocketModes": BlueNet2SocketModes,
       "BlueNet2SocketMembers": BlueNet2SocketMembers,
       "BlueNet2GPIOModes": BlueNet2GPIOModes,
       "BlueNet2GPIOSwitch": BlueNet2GPIOSwitch,
       "BlueNet2RcmSelftestCommand": BlueNet2RcmSelftestCommand,
       "BlueNet2RcmSelftestResult": BlueNet2RcmSelftestResult,
       "blueNet2Mib": blueNet2Mib,
       "blueNet2Notifications": blueNet2Notifications,
       "blueNet2NotificationPrefix": blueNet2NotificationPrefix,
       "blueNet2PduStatusOkNotification": blueNet2PduStatusOkNotification,
       "blueNet2PduStatusWarningNotification": blueNet2PduStatusWarningNotification,
       "blueNet2PduStatusAlarmNotification": blueNet2PduStatusAlarmNotification,
       "blueNet2SensorStatusOkNotification": blueNet2SensorStatusOkNotification,
       "blueNet2SensorStatusWarningNotification": blueNet2SensorStatusWarningNotification,
       "blueNet2SensorStatusAlarmNotification": blueNet2SensorStatusAlarmNotification,
       "blueNet2VariableStatusOkNotification": blueNet2VariableStatusOkNotification,
       "blueNet2VariableLowerWarningNotification": blueNet2VariableLowerWarningNotification,
       "blueNet2VariableUpperWarningNotification": blueNet2VariableUpperWarningNotification,
       "blueNet2VariableLowerAlarmNotification": blueNet2VariableLowerAlarmNotification,
       "blueNet2VariableUpperAlarmNotification": blueNet2VariableUpperAlarmNotification,
       "blueNet2ReconfigAgentNotification": blueNet2ReconfigAgentNotification,
       "blueNet2ShutdownAgentNotification": blueNet2ShutdownAgentNotification,
       "blueNet2Products": blueNet2Products,
       "blueNet2Objects": blueNet2Objects,
       "blueNet2Identification": blueNet2Identification,
       "blueNet2IdProductVendor": blueNet2IdProductVendor,
       "blueNet2IdProductName": blueNet2IdProductName,
       "blueNet2IdProductURI": blueNet2IdProductURI,
       "blueNet2IdProductPartNr": blueNet2IdProductPartNr,
       "blueNet2IdProductSNr": blueNet2IdProductSNr,
       "blueNet2IdProductDate": blueNet2IdProductDate,
       "blueNet2IdProductFacility": blueNet2IdProductFacility,
       "blueNet2IdProductCaps": blueNet2IdProductCaps,
       "blueNet2IdProductFwV": blueNet2IdProductFwV,
       "blueNet2IdProductHwV": blueNet2IdProductHwV,
       "blueNet2IdProductSwV": blueNet2IdProductSwV,
       "blueNet2IdProductOsV": blueNet2IdProductOsV,
       "blueNet2IdProductArch": blueNet2IdProductArch,
       "blueNet2IdProductMAC": blueNet2IdProductMAC,
       "blueNet2Information": blueNet2Information,
       "blueNet2InfoUpTime": blueNet2InfoUpTime,
       "blueNet2InfoOverallStatus": blueNet2InfoOverallStatus,
       "blueNet2InfoNumberOfChanges": blueNet2InfoNumberOfChanges,
       "blueNet2InfoLastChange": blueNet2InfoLastChange,
       "blueNet2InfoAccumulatedStatus": blueNet2InfoAccumulatedStatus,
       "blueNet2InfoLoadTable": blueNet2InfoLoadTable,
       "blueNet2InfoLoadEntry": blueNet2InfoLoadEntry,
       "blueNet2InfoLoadIndex": blueNet2InfoLoadIndex,
       "blueNet2InfoLoadAverage": blueNet2InfoLoadAverage,
       "blueNet2InfoMessageTable": blueNet2InfoMessageTable,
       "blueNet2InfoMessageEntry": blueNet2InfoMessageEntry,
       "blueNet2InfoMessageSource": blueNet2InfoMessageSource,
       "blueNet2InfoMessageStatus": blueNet2InfoMessageStatus,
       "blueNet2InfoMessageTime": blueNet2InfoMessageTime,
       "blueNet2InfoMessageText": blueNet2InfoMessageText,
       "blueNet2InfoMessageNumberOfOks": blueNet2InfoMessageNumberOfOks,
       "blueNet2InfoMessageNumberOfWarnings": blueNet2InfoMessageNumberOfWarnings,
       "blueNet2InfoMessageNumberOfErrors": blueNet2InfoMessageNumberOfErrors,
       "blueNet2Configuration": blueNet2Configuration,
       "blueNet2Alias": blueNet2Alias,
       "blueNet2Language": blueNet2Language,
       "blueNet2DateTime": blueNet2DateTime,
       "blueNet2Protocols": blueNet2Protocols,
       "blueNet2FtpAccess": blueNet2FtpAccess,
       "blueNet2FtpPort": blueNet2FtpPort,
       "blueNet2HttpAccess": blueNet2HttpAccess,
       "blueNet2HttpPort": blueNet2HttpPort,
       "blueNet2HttpsPort": blueNet2HttpsPort,
       "blueNet2SftpAccess": blueNet2SftpAccess,
       "blueNet2SftpPort": blueNet2SftpPort,
       "blueNet2SshAccess": blueNet2SshAccess,
       "blueNet2SshPort": blueNet2SshPort,
       "blueNet2TelnetAccess": blueNet2TelnetAccess,
       "blueNet2TelnetPort": blueNet2TelnetPort,
       "blueNet2Snmp": blueNet2Snmp,
       "blueNet2SnmpVersions": blueNet2SnmpVersions,
       "blueNet2MaxTrapReceivers": blueNet2MaxTrapReceivers,
       "blueNet2TrapReceiverTable": blueNet2TrapReceiverTable,
       "blueNet2TrapReceiverEntry": blueNet2TrapReceiverEntry,
       "blueNet2TrapReceiverIndex": blueNet2TrapReceiverIndex,
       "blueNet2TrapReceiverRowStatus": blueNet2TrapReceiverRowStatus,
       "blueNet2TrapReceiverProtocol": blueNet2TrapReceiverProtocol,
       "blueNet2TrapReceiverAddress": blueNet2TrapReceiverAddress,
       "blueNet2TrapReceiverFriendlyName": blueNet2TrapReceiverFriendlyName,
       "blueNet2TrapReceiverDescription": blueNet2TrapReceiverDescription,
       "blueNet2TrapReceiverCommunity": blueNet2TrapReceiverCommunity,
       "blueNet2TrapReceiverUsername": blueNet2TrapReceiverUsername,
       "blueNet2Modbus": blueNet2Modbus,
       "blueNet2ModbusVersions": blueNet2ModbusVersions,
       "blueNet2ModbusService": blueNet2ModbusService,
       "blueNet2ModbusTcpPort": blueNet2ModbusTcpPort,
       "blueNet2ModbusSerialMode": blueNet2ModbusSerialMode,
       "blueNet2MaxModbusTcpMasters": blueNet2MaxModbusTcpMasters,
       "blueNet2ModbusTcpTable": blueNet2ModbusTcpTable,
       "blueNet2ModbusTcpEntry": blueNet2ModbusTcpEntry,
       "blueNet2ModbusTcpIndex": blueNet2ModbusTcpIndex,
       "blueNet2ModbusTcpRowStatus": blueNet2ModbusTcpRowStatus,
       "blueNet2ModbusTcpAccess": blueNet2ModbusTcpAccess,
       "blueNet2ModbusTcpMaster": blueNet2ModbusTcpMaster,
       "blueNet2ModbusTcpFriendlyName": blueNet2ModbusTcpFriendlyName,
       "blueNet2ModbusTcpDescription": blueNet2ModbusTcpDescription,
       "blueNet2Ntp": blueNet2Ntp,
       "blueNet2NtpService": blueNet2NtpService,
       "blueNet2NtpPort": blueNet2NtpPort,
       "blueNet2NtpTimeZone": blueNet2NtpTimeZone,
       "blueNet2MaxNtpServers": blueNet2MaxNtpServers,
       "blueNet2NtpServerTable": blueNet2NtpServerTable,
       "blueNet2NtpServerEntry": blueNet2NtpServerEntry,
       "blueNet2NtpServerIndex": blueNet2NtpServerIndex,
       "blueNet2NtpServerRowStatus": blueNet2NtpServerRowStatus,
       "blueNet2NtpServerAddress": blueNet2NtpServerAddress,
       "blueNet2NtpServerFriendlyName": blueNet2NtpServerFriendlyName,
       "blueNet2NtpServerDescription": blueNet2NtpServerDescription,
       "blueNet2Smtp": blueNet2Smtp,
       "blueNet2SmtpService": blueNet2SmtpService,
       "blueNet2SmtpPort": blueNet2SmtpPort,
       "blueNet2SmtpServer": blueNet2SmtpServer,
       "blueNet2SmtpAuth": blueNet2SmtpAuth,
       "blueNet2SmtpUsername": blueNet2SmtpUsername,
       "blueNet2SmtpPassword": blueNet2SmtpPassword,
       "blueNet2SmtpFrom": blueNet2SmtpFrom,
       "blueNet2SmtpReply": blueNet2SmtpReply,
       "blueNet2MaxSmtpReceivers": blueNet2MaxSmtpReceivers,
       "blueNet2SmtpReceiverTable": blueNet2SmtpReceiverTable,
       "blueNet2SmtpReceiverEntry": blueNet2SmtpReceiverEntry,
       "blueNet2SmtpReceiverIndex": blueNet2SmtpReceiverIndex,
       "blueNet2SmtpReceiverRowStatus": blueNet2SmtpReceiverRowStatus,
       "blueNet2SmtpReceiverAddress": blueNet2SmtpReceiverAddress,
       "blueNet2SmtpReceiverFriendlyName": blueNet2SmtpReceiverFriendlyName,
       "blueNet2SmtpReceiverDescription": blueNet2SmtpReceiverDescription,
       "blueNet2Syslog": blueNet2Syslog,
       "blueNet2SyslogService": blueNet2SyslogService,
       "blueNet2SyslogFacility": blueNet2SyslogFacility,
       "blueNet2MaxSyslogServers": blueNet2MaxSyslogServers,
       "blueNet2SyslogServerTable": blueNet2SyslogServerTable,
       "blueNet2SyslogServerEntry": blueNet2SyslogServerEntry,
       "blueNet2SyslogServerIndex": blueNet2SyslogServerIndex,
       "blueNet2SyslogServerRowStatus": blueNet2SyslogServerRowStatus,
       "blueNet2SyslogServerAddress": blueNet2SyslogServerAddress,
       "blueNet2SyslogServerPort": blueNet2SyslogServerPort,
       "blueNet2SyslogServerFriendlyName": blueNet2SyslogServerFriendlyName,
       "blueNet2SyslogServerDescription": blueNet2SyslogServerDescription,
       "blueNet2SyslogServerProtocol": blueNet2SyslogServerProtocol,
       "blueNet2Devices": blueNet2Devices,
       "blueNet2DeviceInfo": blueNet2DeviceInfo,
       "blueNet2OverallDeviceStatus": blueNet2OverallDeviceStatus,
       "blueNet2NumberOfDevices": blueNet2NumberOfDevices,
       "blueNet2LastChangeOverallDeviceStatus": blueNet2LastChangeOverallDeviceStatus,
       "blueNet2LastChangeNumberOfDevices": blueNet2LastChangeNumberOfDevices,
       "blueNet2LastChangeDeviceSettings": blueNet2LastChangeDeviceSettings,
       "blueNet2LastChangeDevices": blueNet2LastChangeDevices,
       "blueNet2DevicesAccumulatedStatus": blueNet2DevicesAccumulatedStatus,
       "blueNet2DeviceTable": blueNet2DeviceTable,
       "blueNet2DeviceEntry": blueNet2DeviceEntry,
       "blueNet2DeviceIndex": blueNet2DeviceIndex,
       "blueNet2DeviceGuid": blueNet2DeviceGuid,
       "blueNet2DeviceName": blueNet2DeviceName,
       "blueNet2DeviceFriendlyName": blueNet2DeviceFriendlyName,
       "blueNet2DeviceDescription": blueNet2DeviceDescription,
       "blueNet2DeviceType": blueNet2DeviceType,
       "blueNet2DeviceStatus": blueNet2DeviceStatus,
       "blueNet2DeviceAlarm": blueNet2DeviceAlarm,
       "blueNet2DeviceLastChange": blueNet2DeviceLastChange,
       "blueNet2DeviceEntPhysicalIndex": blueNet2DeviceEntPhysicalIndex,
       "blueNet2DevicePartNr": blueNet2DevicePartNr,
       "blueNet2DeviceSNr": blueNet2DeviceSNr,
       "blueNet2DeviceFwV": blueNet2DeviceFwV,
       "blueNet2DeviceHwV": blueNet2DeviceHwV,
       "blueNet2DeviceSwV": blueNet2DeviceSwV,
       "blueNet2DeviceOsV": blueNet2DeviceOsV,
       "blueNet2DeviceMAC": blueNet2DeviceMAC,
       "blueNet2DeviceNumberOfSensors": blueNet2DeviceNumberOfSensors,
       "blueNet2DeviceNumberOfCircuits": blueNet2DeviceNumberOfCircuits,
       "blueNet2DeviceNumberOfPhases": blueNet2DeviceNumberOfPhases,
       "blueNet2DeviceNumberOfFuses": blueNet2DeviceNumberOfFuses,
       "blueNet2DeviceNumberOfSockets": blueNet2DeviceNumberOfSockets,
       "blueNet2DeviceNumberOfRCMs": blueNet2DeviceNumberOfRCMs,
       "blueNet2DeviceNumberOfVars": blueNet2DeviceNumberOfVars,
       "blueNet2DeviceLocation": blueNet2DeviceLocation,
       "blueNet2DeviceProductDate": blueNet2DeviceProductDate,
       "blueNet2DeviceModbusAddr": blueNet2DeviceModbusAddr,
       "blueNet2DeviceNumberOfSPDs": blueNet2DeviceNumberOfSPDs,
       "blueNet2Sensors": blueNet2Sensors,
       "blueNet2SensorInfo": blueNet2SensorInfo,
       "blueNet2OverallSensorStatus": blueNet2OverallSensorStatus,
       "blueNet2NumberOfSensors": blueNet2NumberOfSensors,
       "blueNet2LastChangeOverallSensorStatus": blueNet2LastChangeOverallSensorStatus,
       "blueNet2LastChangeNumberOfSensors": blueNet2LastChangeNumberOfSensors,
       "blueNet2LastChangeSensorSettings": blueNet2LastChangeSensorSettings,
       "blueNet2LastChangeSensors": blueNet2LastChangeSensors,
       "blueNet2SensorsAccumulatedStatus": blueNet2SensorsAccumulatedStatus,
       "blueNet2SensorTable": blueNet2SensorTable,
       "blueNet2SensorEntry": blueNet2SensorEntry,
       "blueNet2SensorDevice": blueNet2SensorDevice,
       "blueNet2SensorIndex": blueNet2SensorIndex,
       "blueNet2SensorGuid": blueNet2SensorGuid,
       "blueNet2SensorName": blueNet2SensorName,
       "blueNet2SensorFriendlyName": blueNet2SensorFriendlyName,
       "blueNet2SensorDescription": blueNet2SensorDescription,
       "blueNet2SensorType": blueNet2SensorType,
       "blueNet2SensorStatus": blueNet2SensorStatus,
       "blueNet2SensorAlarm": blueNet2SensorAlarm,
       "blueNet2SensorLastChange": blueNet2SensorLastChange,
       "blueNet2SensorEntPhysicalIndex": blueNet2SensorEntPhysicalIndex,
       "blueNet2SensorNumberOfVars": blueNet2SensorNumberOfVars,
       "blueNet2SensorHwV": blueNet2SensorHwV,
       "blueNet2SensorFwV": blueNet2SensorFwV,
       "blueNet2SensorSNr": blueNet2SensorSNr,
       "blueNet2SensorVariableTable": blueNet2SensorVariableTable,
       "blueNet2SensorVariableEntry": blueNet2SensorVariableEntry,
       "blueNet2SensorDeviceIndex": blueNet2SensorDeviceIndex,
       "blueNet2SensorSensorIndex": blueNet2SensorSensorIndex,
       "blueNet2SensorVariableIndex": blueNet2SensorVariableIndex,
       "blueNet2SensorVariableGuid": blueNet2SensorVariableGuid,
       "blueNet2SensorVariableName": blueNet2SensorVariableName,
       "blueNet2SensorVariableFriendlyName": blueNet2SensorVariableFriendlyName,
       "blueNet2SensorVariableDescription": blueNet2SensorVariableDescription,
       "blueNet2SensorVariableGPIOMode": blueNet2SensorVariableGPIOMode,
       "blueNet2SensorVariableGPIOSwitch": blueNet2SensorVariableGPIOSwitch,
       "blueNet2SensorVariableGPIOState": blueNet2SensorVariableGPIOState,
       "blueNet2Circuits": blueNet2Circuits,
       "blueNet2CircuitInfo": blueNet2CircuitInfo,
       "blueNet2OverallCircuitStatus": blueNet2OverallCircuitStatus,
       "blueNet2NumberOfCircuits": blueNet2NumberOfCircuits,
       "blueNet2LastChangeOverallCircuitStatus": blueNet2LastChangeOverallCircuitStatus,
       "blueNet2LastChangeNumberOfCircuits": blueNet2LastChangeNumberOfCircuits,
       "blueNet2LastChangeCircuitSettings": blueNet2LastChangeCircuitSettings,
       "blueNet2LastChangeCircuits": blueNet2LastChangeCircuits,
       "blueNet2CircuitTable": blueNet2CircuitTable,
       "blueNet2CircuitEntry": blueNet2CircuitEntry,
       "blueNet2CircuitDevice": blueNet2CircuitDevice,
       "blueNet2CircuitIndex": blueNet2CircuitIndex,
       "blueNet2CircuitGuid": blueNet2CircuitGuid,
       "blueNet2CircuitName": blueNet2CircuitName,
       "blueNet2CircuitFriendlyName": blueNet2CircuitFriendlyName,
       "blueNet2CircuitDescription": blueNet2CircuitDescription,
       "blueNet2CircuitType": blueNet2CircuitType,
       "blueNet2CircuitStatus": blueNet2CircuitStatus,
       "blueNet2CircuitNumberOfPhases": blueNet2CircuitNumberOfPhases,
       "blueNet2PhaseTable": blueNet2PhaseTable,
       "blueNet2PhaseEntry": blueNet2PhaseEntry,
       "blueNet2PhaseDevice": blueNet2PhaseDevice,
       "blueNet2PhaseCircuit": blueNet2PhaseCircuit,
       "blueNet2PhaseIndex": blueNet2PhaseIndex,
       "blueNet2PhaseGuid": blueNet2PhaseGuid,
       "blueNet2PhaseName": blueNet2PhaseName,
       "blueNet2PhaseFriendlyName": blueNet2PhaseFriendlyName,
       "blueNet2PhaseDescription": blueNet2PhaseDescription,
       "blueNet2PhaseStatus": blueNet2PhaseStatus,
       "blueNet2PhaseNumberOfFuses": blueNet2PhaseNumberOfFuses,
       "blueNet2FuseTable": blueNet2FuseTable,
       "blueNet2FuseEntry": blueNet2FuseEntry,
       "blueNet2FuseDevice": blueNet2FuseDevice,
       "blueNet2FuseCircuit": blueNet2FuseCircuit,
       "blueNet2FusePhase": blueNet2FusePhase,
       "blueNet2FuseIndex": blueNet2FuseIndex,
       "blueNet2FuseGuid": blueNet2FuseGuid,
       "blueNet2FuseName": blueNet2FuseName,
       "blueNet2FuseFriendlyName": blueNet2FuseFriendlyName,
       "blueNet2FuseDescription": blueNet2FuseDescription,
       "blueNet2FuseType": blueNet2FuseType,
       "blueNet2FuseStatus": blueNet2FuseStatus,
       "blueNet2FuseNumberOfSockets": blueNet2FuseNumberOfSockets,
       "blueNet2SocketTable": blueNet2SocketTable,
       "blueNet2SocketEntry": blueNet2SocketEntry,
       "blueNet2SocketDevice": blueNet2SocketDevice,
       "blueNet2SocketCircuit": blueNet2SocketCircuit,
       "blueNet2SocketPhase": blueNet2SocketPhase,
       "blueNet2SocketFuse": blueNet2SocketFuse,
       "blueNet2SocketIndex": blueNet2SocketIndex,
       "blueNet2SocketGuid": blueNet2SocketGuid,
       "blueNet2SocketName": blueNet2SocketName,
       "blueNet2SocketFriendlyName": blueNet2SocketFriendlyName,
       "blueNet2SocketDescription": blueNet2SocketDescription,
       "blueNet2SocketType": blueNet2SocketType,
       "blueNet2SocketStatus": blueNet2SocketStatus,
       "blueNet2SocketMode": blueNet2SocketMode,
       "blueNet2SocketIdentify": blueNet2SocketIdentify,
       "blueNet2SocketMemberIndex": blueNet2SocketMemberIndex,
       "blueNet2RcmTable": blueNet2RcmTable,
       "blueNet2RcmEntry": blueNet2RcmEntry,
       "blueNet2RcmDevice": blueNet2RcmDevice,
       "blueNet2RcmCircuit": blueNet2RcmCircuit,
       "blueNet2RcmPhase": blueNet2RcmPhase,
       "blueNet2RcmFuse": blueNet2RcmFuse,
       "blueNet2RcmSocket": blueNet2RcmSocket,
       "blueNet2RcmIndex": blueNet2RcmIndex,
       "blueNet2RcmGuid": blueNet2RcmGuid,
       "blueNet2RcmName": blueNet2RcmName,
       "blueNet2RcmFriendlyName": blueNet2RcmFriendlyName,
       "blueNet2RcmDescription": blueNet2RcmDescription,
       "blueNet2RcmType": blueNet2RcmType,
       "blueNet2RcmStatus": blueNet2RcmStatus,
       "blueNet2RcmSelftestCommand": blueNet2RcmSelftestCommand,
       "blueNet2RcmSelftestResultValue": blueNet2RcmSelftestResultValue,
       "blueNet2RcmSelftestResultACvalue": blueNet2RcmSelftestResultACvalue,
       "blueNet2RcmSelftestResultDCvalue": blueNet2RcmSelftestResultDCvalue,
       "blueNet2RcmSelftestTimeStamp": blueNet2RcmSelftestTimeStamp,
       "blueNet2RcmSelftestResultStr": blueNet2RcmSelftestResultStr,
       "blueNet2SpdTable": blueNet2SpdTable,
       "blueNet2SpdEntry": blueNet2SpdEntry,
       "blueNet2SpdDevice": blueNet2SpdDevice,
       "blueNet2SpdCircuit": blueNet2SpdCircuit,
       "blueNet2SpdPhase": blueNet2SpdPhase,
       "blueNet2SpdFuse": blueNet2SpdFuse,
       "blueNet2SpdSocket": blueNet2SpdSocket,
       "blueNet2SpdIndex": blueNet2SpdIndex,
       "blueNet2SpdGuid": blueNet2SpdGuid,
       "blueNet2SpdName": blueNet2SpdName,
       "blueNet2SpdFriendlyName": blueNet2SpdFriendlyName,
       "blueNet2SpdDescription": blueNet2SpdDescription,
       "blueNet2SpdType": blueNet2SpdType,
       "blueNet2SpdStatus": blueNet2SpdStatus,
       "blueNet2SocketGroups": blueNet2SocketGroups,
       "blueNet2SocketGroupInfo": blueNet2SocketGroupInfo,
       "blueNet2OverallSocketGroupStatus": blueNet2OverallSocketGroupStatus,
       "blueNet2NumberOfSocketGroups": blueNet2NumberOfSocketGroups,
       "blueNet2LastChangeOverallSocketGroupStatus": blueNet2LastChangeOverallSocketGroupStatus,
       "blueNet2LastChangeNumberOfSocketGroups": blueNet2LastChangeNumberOfSocketGroups,
       "blueNet2LastChangeSocketGroupSettings": blueNet2LastChangeSocketGroupSettings,
       "blueNet2LastChangeSocketGroups": blueNet2LastChangeSocketGroups,
       "blueNet2SocketGroupsAccumulatedStatus": blueNet2SocketGroupsAccumulatedStatus,
       "blueNet2SocketGroupsInUse": blueNet2SocketGroupsInUse,
       "blueNet2MaxSocketGroups": blueNet2MaxSocketGroups,
       "blueNet2SocketGroupTable": blueNet2SocketGroupTable,
       "blueNet2SocketGroupEntry": blueNet2SocketGroupEntry,
       "blueNet2SocketGroupIndex": blueNet2SocketGroupIndex,
       "blueNet2SocketGroupRowStatus": blueNet2SocketGroupRowStatus,
       "blueNet2SocketGroupGuid": blueNet2SocketGroupGuid,
       "blueNet2SocketGroupName": blueNet2SocketGroupName,
       "blueNet2SocketGroupFriendlyName": blueNet2SocketGroupFriendlyName,
       "blueNet2SocketGroupDescription": blueNet2SocketGroupDescription,
       "blueNet2SocketGroupStatus": blueNet2SocketGroupStatus,
       "blueNet2SocketGroupMode": blueNet2SocketGroupMode,
       "blueNet2SocketGroupIdentify": blueNet2SocketGroupIdentify,
       "blueNet2SocketGroupEntPhysicalIndex": blueNet2SocketGroupEntPhysicalIndex,
       "blueNet2SocketGroupAccumulatedStatus": blueNet2SocketGroupAccumulatedStatus,
       "blueNet2SocketGroupMembers": blueNet2SocketGroupMembers,
       "blueNet2Variables": blueNet2Variables,
       "blueNet2VariableInfo": blueNet2VariableInfo,
       "blueNet2OverallVariableStatus": blueNet2OverallVariableStatus,
       "blueNet2NumberOfVariables": blueNet2NumberOfVariables,
       "blueNet2LastChangeOverallVariableStatus": blueNet2LastChangeOverallVariableStatus,
       "blueNet2LastChangeNumberOfVariables": blueNet2LastChangeNumberOfVariables,
       "blueNet2LastChangeVariableSettings": blueNet2LastChangeVariableSettings,
       "blueNet2LastChangeVariableStatus": blueNet2LastChangeVariableStatus,
       "blueNet2VariablesAccumulatedStatus": blueNet2VariablesAccumulatedStatus,
       "blueNet2NumberOfChangesVariableScaling": blueNet2NumberOfChangesVariableScaling,
       "blueNet2LastChangeVariableScaling": blueNet2LastChangeVariableScaling,
       "blueNet2LastChangeVariableReset": blueNet2LastChangeVariableReset,
       "blueNet2VariableTable": blueNet2VariableTable,
       "blueNet2VariableEntry": blueNet2VariableEntry,
       "blueNet2VariableId": blueNet2VariableId,
       "blueNet2VariableGuid": blueNet2VariableGuid,
       "blueNet2VariableName": blueNet2VariableName,
       "blueNet2VariableFriendlyName": blueNet2VariableFriendlyName,
       "blueNet2VariableDescription": blueNet2VariableDescription,
       "blueNet2VariableType": blueNet2VariableType,
       "blueNet2VariableStatus": blueNet2VariableStatus,
       "blueNet2VariableAlarm": blueNet2VariableAlarm,
       "blueNet2VariableScaling": blueNet2VariableScaling,
       "blueNet2VariableUnit": blueNet2VariableUnit,
       "blueNet2VariableSetPoint": blueNet2VariableSetPoint,
       "blueNet2VariableMode": blueNet2VariableMode,
       "blueNet2VariableEntPhysicalIndex": blueNet2VariableEntPhysicalIndex,
       "blueNet2VariableSetPointTable": blueNet2VariableSetPointTable,
       "blueNet2VariableSetPointEntry": blueNet2VariableSetPointEntry,
       "blueNet2VariableSetPointGuid": blueNet2VariableSetPointGuid,
       "blueNet2VariableSetPointType": blueNet2VariableSetPointType,
       "blueNet2VariableSetPointMinValue": blueNet2VariableSetPointMinValue,
       "blueNet2VariableSetPointMaxValue": blueNet2VariableSetPointMaxValue,
       "blueNet2VariableSetPointLowerAlarm": blueNet2VariableSetPointLowerAlarm,
       "blueNet2VariableSetPointLowerWarning": blueNet2VariableSetPointLowerWarning,
       "blueNet2VariableSetPointUpperWarning": blueNet2VariableSetPointUpperWarning,
       "blueNet2VariableSetPointUpperAlarm": blueNet2VariableSetPointUpperAlarm,
       "blueNet2VariableSetPointHysteresis": blueNet2VariableSetPointHysteresis,
       "blueNet2VariableSetPointRcmACUpperAlarmThreshold": blueNet2VariableSetPointRcmACUpperAlarmThreshold,
       "blueNet2VariableSetPointRcmACUpperAlarmGradient": blueNet2VariableSetPointRcmACUpperAlarmGradient,
       "blueNet2VariableSetPointRcmACUpperWarningThreshold": blueNet2VariableSetPointRcmACUpperWarningThreshold,
       "blueNet2VariableSetPointRcmACUpperWarningGradient": blueNet2VariableSetPointRcmACUpperWarningGradient,
       "blueNet2VariableDataTable": blueNet2VariableDataTable,
       "blueNet2VariableDataEntry": blueNet2VariableDataEntry,
       "blueNet2VariableDataId": blueNet2VariableDataId,
       "blueNet2VariableDataGuid": blueNet2VariableDataGuid,
       "blueNet2VariableDataType": blueNet2VariableDataType,
       "blueNet2VariableDataStatus": blueNet2VariableDataStatus,
       "blueNet2VariableDataValue": blueNet2VariableDataValue,
       "blueNet2VariableDataDateTime": blueNet2VariableDataDateTime,
       "blueNet2VariableDataByTypeTable": blueNet2VariableDataByTypeTable,
       "blueNet2VariableDataByTypeEntry": blueNet2VariableDataByTypeEntry,
       "blueNet2VariableDataByType": blueNet2VariableDataByType,
       "blueNet2VariableDataByTypeGuid": blueNet2VariableDataByTypeGuid,
       "blueNet2VariableDataByTypeType": blueNet2VariableDataByTypeType,
       "blueNet2VariableDataByTypeStatus": blueNet2VariableDataByTypeStatus,
       "blueNet2VariableDataByTypeValue": blueNet2VariableDataByTypeValue,
       "blueNet2VariableDataByTypeDateTime": blueNet2VariableDataByTypeDateTime,
       "blueNet2VariableDataByStateTable": blueNet2VariableDataByStateTable,
       "blueNet2VariableDataByStateEntry": blueNet2VariableDataByStateEntry,
       "blueNet2VariableDataByState": blueNet2VariableDataByState,
       "blueNet2VariableDataByStateGuid": blueNet2VariableDataByStateGuid,
       "blueNet2VariableDataByStateType": blueNet2VariableDataByStateType,
       "blueNet2VariableDataByStateStatus": blueNet2VariableDataByStateStatus,
       "blueNet2VariableDataByStateValue": blueNet2VariableDataByStateValue,
       "blueNet2VariableDataByStateDateTime": blueNet2VariableDataByStateDateTime,
       "blueNet2VariableDataBySourceTable": blueNet2VariableDataBySourceTable,
       "blueNet2VariableDataBySourceEntry": blueNet2VariableDataBySourceEntry,
       "blueNet2VariableDataBySource": blueNet2VariableDataBySource,
       "blueNet2VariableDataBySourceGuid": blueNet2VariableDataBySourceGuid,
       "blueNet2VariableDataBySourceType": blueNet2VariableDataBySourceType,
       "blueNet2VariableDataBySourceStatus": blueNet2VariableDataBySourceStatus,
       "blueNet2VariableDataBySourceValue": blueNet2VariableDataBySourceValue,
       "blueNet2VariableDataBySourceDateTime": blueNet2VariableDataBySourceDateTime,
       "blueNet2MPStates": blueNet2MPStates,
       "blueNet2MPTable": blueNet2MPTable,
       "blueNet2MPEntry": blueNet2MPEntry,
       "blueNet2MPID": blueNet2MPID,
       "blueNet2MPGuid": blueNet2MPGuid,
       "blueNet2MPName": blueNet2MPName,
       "blueNet2MPFriendlyName": blueNet2MPFriendlyName,
       "blueNet2MPState": blueNet2MPState,
       "blueNet2MPTimeStamp": blueNet2MPTimeStamp,
       "blueNet2Traps": blueNet2Traps,
       "blueNet2TrapPrefix": blueNet2TrapPrefix,
       "blueNet2PduStatusOkTrap": blueNet2PduStatusOkTrap,
       "blueNet2PduStatusWarningTrap": blueNet2PduStatusWarningTrap,
       "blueNet2PduStatusAlarmTrap": blueNet2PduStatusAlarmTrap,
       "blueNet2SensorStatusOkTrap": blueNet2SensorStatusOkTrap,
       "blueNet2SensorStatusWarningTrap": blueNet2SensorStatusWarningTrap,
       "blueNet2SensorStatusAlarmTrap": blueNet2SensorStatusAlarmTrap,
       "blueNet2VariableStatusOkTrap": blueNet2VariableStatusOkTrap,
       "blueNet2VariableLowerWarningTrap": blueNet2VariableLowerWarningTrap,
       "blueNet2VariableUpperWarningTrap": blueNet2VariableUpperWarningTrap,
       "blueNet2VariableLowerAlarmTrap": blueNet2VariableLowerAlarmTrap,
       "blueNet2VariableUpperAlarmTrap": blueNet2VariableUpperAlarmTrap,
       "blueNet2RCMSelftestResultTrap": blueNet2RCMSelftestResultTrap,
       "blueNet2ReconfigAgentTrap": blueNet2ReconfigAgentTrap,
       "blueNet2ShutdownAgentTrap": blueNet2ShutdownAgentTrap,
       "blueNet2Conformance": blueNet2Conformance,
       "blueNet2Compliances": blueNet2Compliances,
       "blueNet2Compliance": blueNet2Compliance,
       "blueNet2Groups": blueNet2Groups,
       "blueNet2TrapGroup": blueNet2TrapGroup,
       "blueNet2NotificationGroup": blueNet2NotificationGroup,
       "blueNet2IdentificationGroup": blueNet2IdentificationGroup,
       "blueNet2InformationGroup": blueNet2InformationGroup,
       "blueNet2ConfigurationGroup": blueNet2ConfigurationGroup,
       "blueNet2SnmpGroup": blueNet2SnmpGroup,
       "blueNet2ModbusGroup": blueNet2ModbusGroup,
       "blueNet2NtpGroup": blueNet2NtpGroup,
       "blueNet2SmtpGroup": blueNet2SmtpGroup,
       "blueNet2SyslogGroup": blueNet2SyslogGroup,
       "blueNet2DeviceGroup": blueNet2DeviceGroup,
       "blueNet2SensorGroup": blueNet2SensorGroup,
       "blueNet2CircuitGroup": blueNet2CircuitGroup,
       "blueNet2PhaseGroup": blueNet2PhaseGroup,
       "blueNet2FuseGroup": blueNet2FuseGroup,
       "blueNet2SocketGroup": blueNet2SocketGroup,
       "blueNet2RcmGroup": blueNet2RcmGroup,
       "blueNet2SocketGroupGroup": blueNet2SocketGroupGroup,
       "blueNet2VariableGroup": blueNet2VariableGroup,
       "blueNet2MPGroup": blueNet2MPGroup,
       "blueNet2SpdGroup": blueNet2SpdGroup}
)
