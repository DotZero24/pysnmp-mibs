# SNMP MIB module (NEWTEC-BISSSCRAMBLER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-BISSSCRAMBLER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:56 2025
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

ntcBissScrambler = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100)
)
if mibBuilder.loadTexts:
    ntcBissScrambler.setRevisions(
        ("2017-07-10 12:00",
         "2014-09-09 09:00",
         "2013-07-02 10:00",
         "2013-03-27 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcBissScrObjects_ObjectIdentity = ObjectIdentity
ntcBissScrObjects = _NtcBissScrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1)
)
if mibBuilder.loadTexts:
    ntcBissScrObjects.setStatus("current")


class _NtcBissScrambling_Type(NtcEnable):
    """Custom type ntcBissScrambling based on NtcEnable"""
    defaultValue = 0


_NtcBissScrambling_Type.__name__ = "NtcEnable"
_NtcBissScrambling_Object = MibScalar
ntcBissScrambling = _NtcBissScrambling_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 1),
    _NtcBissScrambling_Type()
)
ntcBissScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBissScrambling.setStatus("current")


class _NtcBissScramblingMode_Type(Integer32):
    """Custom type ntcBissScramblingMode based on Integer32"""
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
          ("raw", 1))
    )


_NtcBissScramblingMode_Type.__name__ = "Integer32"
_NtcBissScramblingMode_Object = MibScalar
ntcBissScramblingMode = _NtcBissScramblingMode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 2),
    _NtcBissScramblingMode_Type()
)
ntcBissScramblingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBissScramblingMode.setStatus("current")


class _NtcBissKeyParity_Type(Integer32):
    """Custom type ntcBissKeyParity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("odd", 0),
          ("even", 1))
    )


_NtcBissKeyParity_Type.__name__ = "Integer32"
_NtcBissKeyParity_Object = MibScalar
ntcBissKeyParity = _NtcBissKeyParity_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 3),
    _NtcBissKeyParity_Type()
)
ntcBissKeyParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBissKeyParity.setStatus("current")


class _NtcBissScramblingSuppression_Type(Integer32):
    """Custom type ntcBissScramblingSuppression based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NtcBissScramblingSuppression_Type.__name__ = "Integer32"
_NtcBissScramblingSuppression_Object = MibScalar
ntcBissScramblingSuppression = _NtcBissScramblingSuppression_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 4),
    _NtcBissScramblingSuppression_Type()
)
ntcBissScramblingSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBissScramblingSuppression.setStatus("current")


class _NtcBissMinRawUnscrambledPid_Type(Unsigned32):
    """Custom type ntcBissMinRawUnscrambledPid based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8190),
    )


_NtcBissMinRawUnscrambledPid_Type.__name__ = "Unsigned32"
_NtcBissMinRawUnscrambledPid_Object = MibScalar
ntcBissMinRawUnscrambledPid = _NtcBissMinRawUnscrambledPid_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 5),
    _NtcBissMinRawUnscrambledPid_Type()
)
ntcBissMinRawUnscrambledPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBissMinRawUnscrambledPid.setStatus("current")


class _NtcBissMaxRawUnscrambledPid_Type(Unsigned32):
    """Custom type ntcBissMaxRawUnscrambledPid based on Unsigned32"""
    defaultValue = 31

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8190),
    )


_NtcBissMaxRawUnscrambledPid_Type.__name__ = "Unsigned32"
_NtcBissMaxRawUnscrambledPid_Object = MibScalar
ntcBissMaxRawUnscrambledPid = _NtcBissMaxRawUnscrambledPid_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 6),
    _NtcBissMaxRawUnscrambledPid_Type()
)
ntcBissMaxRawUnscrambledPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBissMaxRawUnscrambledPid.setStatus("current")
_NtcBissScrKeys_ObjectIdentity = ObjectIdentity
ntcBissScrKeys = _NtcBissScrKeys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 7)
)
if mibBuilder.loadTexts:
    ntcBissScrKeys.setStatus("current")


class _NtcBissClearKeys_Type(Integer32):
    """Custom type ntcBissClearKeys based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("donothing", 0),
          ("clearkeys", 1))
    )


_NtcBissClearKeys_Type.__name__ = "Integer32"
_NtcBissClearKeys_Object = MibScalar
ntcBissClearKeys = _NtcBissClearKeys_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 7, 1),
    _NtcBissClearKeys_Type()
)
ntcBissClearKeys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBissClearKeys.setStatus("current")


class _NtcBissEvenSessionWord_Type(DisplayString):
    """Custom type ntcBissEvenSessionWord based on DisplayString"""
    defaultValue = OctetString("************")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_NtcBissEvenSessionWord_Type.__name__ = "DisplayString"
_NtcBissEvenSessionWord_Object = MibScalar
ntcBissEvenSessionWord = _NtcBissEvenSessionWord_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 7, 2),
    _NtcBissEvenSessionWord_Type()
)
ntcBissEvenSessionWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBissEvenSessionWord.setStatus("current")


class _NtcBissOddSessionWord_Type(DisplayString):
    """Custom type ntcBissOddSessionWord based on DisplayString"""
    defaultValue = OctetString("************")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_NtcBissOddSessionWord_Type.__name__ = "DisplayString"
_NtcBissOddSessionWord_Object = MibScalar
ntcBissOddSessionWord = _NtcBissOddSessionWord_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 7, 3),
    _NtcBissOddSessionWord_Type()
)
ntcBissOddSessionWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBissOddSessionWord.setStatus("current")


class _NtcBissEncryptedEvenSessionWord_Type(DisplayString):
    """Custom type ntcBissEncryptedEvenSessionWord based on DisplayString"""
    defaultValue = OctetString("****************")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_NtcBissEncryptedEvenSessionWord_Type.__name__ = "DisplayString"
_NtcBissEncryptedEvenSessionWord_Object = MibScalar
ntcBissEncryptedEvenSessionWord = _NtcBissEncryptedEvenSessionWord_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 7, 4),
    _NtcBissEncryptedEvenSessionWord_Type()
)
ntcBissEncryptedEvenSessionWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBissEncryptedEvenSessionWord.setStatus("current")


class _NtcBissEncryptedOddSessionWord_Type(DisplayString):
    """Custom type ntcBissEncryptedOddSessionWord based on DisplayString"""
    defaultValue = OctetString("****************")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_NtcBissEncryptedOddSessionWord_Type.__name__ = "DisplayString"
_NtcBissEncryptedOddSessionWord_Object = MibScalar
ntcBissEncryptedOddSessionWord = _NtcBissEncryptedOddSessionWord_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 7, 5),
    _NtcBissEncryptedOddSessionWord_Type()
)
ntcBissEncryptedOddSessionWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBissEncryptedOddSessionWord.setStatus("current")


class _NtcBissInKeyEncryptionMode_Type(Integer32):
    """Custom type ntcBissInKeyEncryptionMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("buried", 0),
          ("injected", 1))
    )


_NtcBissInKeyEncryptionMode_Type.__name__ = "Integer32"
_NtcBissInKeyEncryptionMode_Object = MibScalar
ntcBissInKeyEncryptionMode = _NtcBissInKeyEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 7, 6),
    _NtcBissInKeyEncryptionMode_Type()
)
ntcBissInKeyEncryptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBissInKeyEncryptionMode.setStatus("current")


class _NtcBissInjectedId_Type(DisplayString):
    """Custom type ntcBissInjectedId based on DisplayString"""
    defaultValue = OctetString("00000000000000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )
    fixed_length = 14


_NtcBissInjectedId_Type.__name__ = "DisplayString"
_NtcBissInjectedId_Object = MibScalar
ntcBissInjectedId = _NtcBissInjectedId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 7, 7),
    _NtcBissInjectedId_Type()
)
ntcBissInjectedId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBissInjectedId.setStatus("current")


class _NtcBissBuriedId_Type(DisplayString):
    """Custom type ntcBissBuriedId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )
    fixed_length = 14


_NtcBissBuriedId_Type.__name__ = "DisplayString"
_NtcBissBuriedId_Object = MibScalar
ntcBissBuriedId = _NtcBissBuriedId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 7, 8),
    _NtcBissBuriedId_Type()
)
ntcBissBuriedId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBissBuriedId.setStatus("current")


class _NtcBissSetupId_Type(DisplayString):
    """Custom type ntcBissSetupId based on DisplayString"""
    defaultValue = OctetString("BD28121969BD")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_NtcBissSetupId_Type.__name__ = "DisplayString"
_NtcBissSetupId_Object = MibScalar
ntcBissSetupId = _NtcBissSetupId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 7, 9),
    _NtcBissSetupId_Type()
)
ntcBissSetupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBissSetupId.setStatus("current")
_NtcBissMonitor_ObjectIdentity = ObjectIdentity
ntcBissMonitor = _NtcBissMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 8)
)
if mibBuilder.loadTexts:
    ntcBissMonitor.setStatus("current")


class _NtcBissScramblingState_Type(Integer32):
    """Custom type ntcBissScramblingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scrambling", 0),
          ("suppressed", 1),
          ("unscrambled", 2))
    )


_NtcBissScramblingState_Type.__name__ = "Integer32"
_NtcBissScramblingState_Object = MibScalar
ntcBissScramblingState = _NtcBissScramblingState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 8, 1),
    _NtcBissScramblingState_Type()
)
ntcBissScramblingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBissScramblingState.setStatus("current")


class _NtcBissSessionWordChanged_Type(DisplayString):
    """Custom type ntcBissSessionWordChanged based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtcBissSessionWordChanged_Type.__name__ = "DisplayString"
_NtcBissSessionWordChanged_Object = MibScalar
ntcBissSessionWordChanged = _NtcBissSessionWordChanged_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 8, 2),
    _NtcBissSessionWordChanged_Type()
)
ntcBissSessionWordChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBissSessionWordChanged.setStatus("current")
_NtcBissAlarms_ObjectIdentity = ObjectIdentity
ntcBissAlarms = _NtcBissAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 9)
)
if mibBuilder.loadTexts:
    ntcBissAlarms.setStatus("current")
_NtcGeneralBissError_Type = NtcAlarmState
_NtcGeneralBissError_Object = MibScalar
ntcGeneralBissError = _NtcGeneralBissError_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 9, 1),
    _NtcGeneralBissError_Type()
)
ntcGeneralBissError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGeneralBissError.setStatus("current")
_NtcPatError_Type = NtcAlarmState
_NtcPatError_Object = MibScalar
ntcPatError = _NtcPatError_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 9, 2),
    _NtcPatError_Type()
)
ntcPatError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcPatError.setStatus("current")
_NtcPmtError_Type = NtcAlarmState
_NtcPmtError_Object = MibScalar
ntcPmtError = _NtcPmtError_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 9, 3),
    _NtcPmtError_Type()
)
ntcPmtError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcPmtError.setStatus("current")
_NtcCatError_Type = NtcAlarmState
_NtcCatError_Object = MibScalar
ntcCatError = _NtcCatError_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 9, 4),
    _NtcCatError_Type()
)
ntcCatError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcCatError.setStatus("current")
_NtcAlreadyScrambled_Type = NtcAlarmState
_NtcAlreadyScrambled_Object = MibScalar
ntcAlreadyScrambled = _NtcAlreadyScrambled_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 9, 5),
    _NtcAlreadyScrambled_Type()
)
ntcAlreadyScrambled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAlreadyScrambled.setStatus("current")
_NtcCaDescriptorFoundOnInput_Type = NtcAlarmState
_NtcCaDescriptorFoundOnInput_Object = MibScalar
ntcCaDescriptorFoundOnInput = _NtcCaDescriptorFoundOnInput_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 9, 6),
    _NtcCaDescriptorFoundOnInput_Type()
)
ntcCaDescriptorFoundOnInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcCaDescriptorFoundOnInput.setStatus("current")
_NtcScramblingError_Type = NtcAlarmState
_NtcScramblingError_Object = MibScalar
ntcScramblingError = _NtcScramblingError_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 9, 7),
    _NtcScramblingError_Type()
)
ntcScramblingError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcScramblingError.setStatus("current")
_NtcSwRefusedError_Type = NtcAlarmState
_NtcSwRefusedError_Object = MibScalar
ntcSwRefusedError = _NtcSwRefusedError_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 1, 9, 8),
    _NtcSwRefusedError_Type()
)
ntcSwRefusedError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcSwRefusedError.setStatus("current")
_NtcBissScrConformance_ObjectIdentity = ObjectIdentity
ntcBissScrConformance = _NtcBissScrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 2)
)
if mibBuilder.loadTexts:
    ntcBissScrConformance.setStatus("current")
_NtcBissScrConfCompliance_ObjectIdentity = ObjectIdentity
ntcBissScrConfCompliance = _NtcBissScrConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 2, 1)
)
if mibBuilder.loadTexts:
    ntcBissScrConfCompliance.setStatus("current")
_NtcBissScrConfGroup_ObjectIdentity = ObjectIdentity
ntcBissScrConfGroup = _NtcBissScrConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 2, 2)
)
if mibBuilder.loadTexts:
    ntcBissScrConfGroup.setStatus("current")

# Managed Objects groups

ntcBissScrConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 2, 2, 1)
)
ntcBissScrConfGrpV1Standard.setObjects(
      *(("NEWTEC-BISSSCRAMBLER-MIB", "ntcBissScrambling"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcBissScramblingMode"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcBissKeyParity"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcBissScramblingSuppression"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcBissMinRawUnscrambledPid"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcBissMaxRawUnscrambledPid"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcBissClearKeys"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcBissEvenSessionWord"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcBissOddSessionWord"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcBissEncryptedEvenSessionWord"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcBissEncryptedOddSessionWord"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcBissInKeyEncryptionMode"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcBissInjectedId"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcBissBuriedId"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcBissSetupId"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcBissScramblingState"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcBissSessionWordChanged"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcGeneralBissError"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcPatError"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcPmtError"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcCatError"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcAlreadyScrambled"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcCaDescriptorFoundOnInput"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcScramblingError"),
        ("NEWTEC-BISSSCRAMBLER-MIB", "ntcSwRefusedError"))
)
if mibBuilder.loadTexts:
    ntcBissScrConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcBissScrConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3100, 2, 1, 1)
)
ntcBissScrConfCompV1Standard.setObjects(
    ("NEWTEC-BISSSCRAMBLER-MIB", "ntcBissScrConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcBissScrConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-BISSSCRAMBLER-MIB",
    **{"ntcBissScrambler": ntcBissScrambler,
       "ntcBissScrObjects": ntcBissScrObjects,
       "ntcBissScrambling": ntcBissScrambling,
       "ntcBissScramblingMode": ntcBissScramblingMode,
       "ntcBissKeyParity": ntcBissKeyParity,
       "ntcBissScramblingSuppression": ntcBissScramblingSuppression,
       "ntcBissMinRawUnscrambledPid": ntcBissMinRawUnscrambledPid,
       "ntcBissMaxRawUnscrambledPid": ntcBissMaxRawUnscrambledPid,
       "ntcBissScrKeys": ntcBissScrKeys,
       "ntcBissClearKeys": ntcBissClearKeys,
       "ntcBissEvenSessionWord": ntcBissEvenSessionWord,
       "ntcBissOddSessionWord": ntcBissOddSessionWord,
       "ntcBissEncryptedEvenSessionWord": ntcBissEncryptedEvenSessionWord,
       "ntcBissEncryptedOddSessionWord": ntcBissEncryptedOddSessionWord,
       "ntcBissInKeyEncryptionMode": ntcBissInKeyEncryptionMode,
       "ntcBissInjectedId": ntcBissInjectedId,
       "ntcBissBuriedId": ntcBissBuriedId,
       "ntcBissSetupId": ntcBissSetupId,
       "ntcBissMonitor": ntcBissMonitor,
       "ntcBissScramblingState": ntcBissScramblingState,
       "ntcBissSessionWordChanged": ntcBissSessionWordChanged,
       "ntcBissAlarms": ntcBissAlarms,
       "ntcGeneralBissError": ntcGeneralBissError,
       "ntcPatError": ntcPatError,
       "ntcPmtError": ntcPmtError,
       "ntcCatError": ntcCatError,
       "ntcAlreadyScrambled": ntcAlreadyScrambled,
       "ntcCaDescriptorFoundOnInput": ntcCaDescriptorFoundOnInput,
       "ntcScramblingError": ntcScramblingError,
       "ntcSwRefusedError": ntcSwRefusedError,
       "ntcBissScrConformance": ntcBissScrConformance,
       "ntcBissScrConfCompliance": ntcBissScrConfCompliance,
       "ntcBissScrConfCompV1Standard": ntcBissScrConfCompV1Standard,
       "ntcBissScrConfGroup": ntcBissScrConfGroup,
       "ntcBissScrConfGrpV1Standard": ntcBissScrConfGrpV1Standard}
)
