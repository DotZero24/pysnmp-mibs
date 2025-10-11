# SNMP MIB module (MX-FXO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-FXO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:08 2025
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

(MxEnableState,) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState")

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

fxoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45)
)
if mibBuilder.loadTexts:
    fxoMIB.setRevisions(
        ("2012-06-04 00:00",
         "2008-08-25 00:00",
         "2008-07-15 00:00",
         "2005-08-23 00:00",
         "2005-07-04 00:00",
         "2004-08-04 00:00",
         "2003-11-06 00:00",
         "2003-10-20 00:00",
         "2003-09-25 00:00",
         "2003-08-19 00:00",
         "2003-02-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FxoMIBObjects_ObjectIdentity = ObjectIdentity
fxoMIBObjects = _FxoMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1)
)
_FxoLinePropertiesCustomization_ObjectIdentity = ObjectIdentity
fxoLinePropertiesCustomization = _FxoLinePropertiesCustomization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 5)
)


class _FxoDialtoneDetectionMode_Type(Integer32):
    """Custom type fxoDialtoneDetectionMode based on Integer32"""
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
          ("countryTone", 1))
    )


_FxoDialtoneDetectionMode_Type.__name__ = "Integer32"
_FxoDialtoneDetectionMode_Object = MibScalar
fxoDialtoneDetectionMode = _FxoDialtoneDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 5, 5),
    _FxoDialtoneDetectionMode_Type()
)
fxoDialtoneDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoDialtoneDetectionMode.setStatus("current")


class _FxoDialtoneDetectionTimeout_Type(Unsigned32):
    """Custom type fxoDialtoneDetectionTimeout based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1300, 10000),
    )


_FxoDialtoneDetectionTimeout_Type.__name__ = "Unsigned32"
_FxoDialtoneDetectionTimeout_Object = MibScalar
fxoDialtoneDetectionTimeout = _FxoDialtoneDetectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 5, 10),
    _FxoDialtoneDetectionTimeout_Type()
)
fxoDialtoneDetectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoDialtoneDetectionTimeout.setStatus("current")


class _FxoCallerIdDetectionRange_Type(Integer32):
    """Custom type fxoCallerIdDetectionRange based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("low", 1))
    )


_FxoCallerIdDetectionRange_Type.__name__ = "Integer32"
_FxoCallerIdDetectionRange_Object = MibScalar
fxoCallerIdDetectionRange = _FxoCallerIdDetectionRange_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 5, 15),
    _FxoCallerIdDetectionRange_Type()
)
fxoCallerIdDetectionRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoCallerIdDetectionRange.setStatus("current")


class _FxoAnswerSupervisionMode_Type(Integer32):
    """Custom type fxoAnswerSupervisionMode based on Integer32"""
    defaultValue = 0

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
          ("batteryReversal", 1),
          ("billingTone", 2))
    )


_FxoAnswerSupervisionMode_Type.__name__ = "Integer32"
_FxoAnswerSupervisionMode_Object = MibScalar
fxoAnswerSupervisionMode = _FxoAnswerSupervisionMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 5, 50),
    _FxoAnswerSupervisionMode_Type()
)
fxoAnswerSupervisionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoAnswerSupervisionMode.setStatus("current")
_FxoLineFaultDetection_ObjectIdentity = ObjectIdentity
fxoLineFaultDetection = _FxoLineFaultDetection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 10)
)


class _FxoLineFaultDetectionEnable_Type(MxEnableState):
    """Custom type fxoLineFaultDetectionEnable based on MxEnableState"""
    defaultValue = 1


_FxoLineFaultDetectionEnable_Type.__name__ = "MxEnableState"
_FxoLineFaultDetectionEnable_Object = MibScalar
fxoLineFaultDetectionEnable = _FxoLineFaultDetectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 10, 5),
    _FxoLineFaultDetectionEnable_Type()
)
fxoLineFaultDetectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoLineFaultDetectionEnable.setStatus("current")


class _FxoLineSeizureTimeout_Type(Unsigned32):
    """Custom type fxoLineSeizureTimeout based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 10000),
    )


_FxoLineSeizureTimeout_Type.__name__ = "Unsigned32"
_FxoLineSeizureTimeout_Object = MibScalar
fxoLineSeizureTimeout = _FxoLineSeizureTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 10, 10),
    _FxoLineSeizureTimeout_Type()
)
fxoLineSeizureTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoLineSeizureTimeout.setStatus("current")
_FxoIfLineStatusTable_Object = MibTable
fxoIfLineStatusTable = _FxoIfLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 10, 15)
)
if mibBuilder.loadTexts:
    fxoIfLineStatusTable.setStatus("current")
_FxoIfLineStatusEntry_Object = MibTableRow
fxoIfLineStatusEntry = _FxoIfLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 10, 15, 5)
)
fxoIfLineStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fxoIfLineStatusEntry.setStatus("current")


class _FxoLineStatus_Type(Integer32):
    """Custom type fxoLineStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("connected", 1),
          ("disconnected", 2))
    )


_FxoLineStatus_Type.__name__ = "Integer32"
_FxoLineStatus_Object = MibTableColumn
fxoLineStatus = _FxoLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 10, 15, 5, 5),
    _FxoLineStatus_Type()
)
fxoLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxoLineStatus.setStatus("current")
_FxoIfAnsweringDelayTable_Object = MibTable
fxoIfAnsweringDelayTable = _FxoIfAnsweringDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 15)
)
if mibBuilder.loadTexts:
    fxoIfAnsweringDelayTable.setStatus("current")
_FxoIfAnsweringDelayEntry_Object = MibTableRow
fxoIfAnsweringDelayEntry = _FxoIfAnsweringDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 15, 5)
)
fxoIfAnsweringDelayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fxoIfAnsweringDelayEntry.setStatus("current")


class _FxoPreAnswerDelay_Type(Unsigned32):
    """Custom type fxoPreAnswerDelay based on Unsigned32"""
    defaultValue = 8000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_FxoPreAnswerDelay_Type.__name__ = "Unsigned32"
_FxoPreAnswerDelay_Object = MibTableColumn
fxoPreAnswerDelay = _FxoPreAnswerDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 15, 5, 5),
    _FxoPreAnswerDelay_Type()
)
fxoPreAnswerDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoPreAnswerDelay.setStatus("current")


class _FxoAnswerOnCallerIdDetectionEnable_Type(MxEnableState):
    """Custom type fxoAnswerOnCallerIdDetectionEnable based on MxEnableState"""
    defaultValue = 1


_FxoAnswerOnCallerIdDetectionEnable_Type.__name__ = "MxEnableState"
_FxoAnswerOnCallerIdDetectionEnable_Object = MibTableColumn
fxoAnswerOnCallerIdDetectionEnable = _FxoAnswerOnCallerIdDetectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 15, 5, 10),
    _FxoAnswerOnCallerIdDetectionEnable_Type()
)
fxoAnswerOnCallerIdDetectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoAnswerOnCallerIdDetectionEnable.setStatus("current")


class _FxoWaitForCalleeToAnswerEnable_Type(MxEnableState):
    """Custom type fxoWaitForCalleeToAnswerEnable based on MxEnableState"""
    defaultValue = 0


_FxoWaitForCalleeToAnswerEnable_Type.__name__ = "MxEnableState"
_FxoWaitForCalleeToAnswerEnable_Object = MibTableColumn
fxoWaitForCalleeToAnswerEnable = _FxoWaitForCalleeToAnswerEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 15, 5, 60),
    _FxoWaitForCalleeToAnswerEnable_Type()
)
fxoWaitForCalleeToAnswerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoWaitForCalleeToAnswerEnable.setStatus("current")
_FxoForcedEndOfCallCustomization_ObjectIdentity = ObjectIdentity
fxoForcedEndOfCallCustomization = _FxoForcedEndOfCallCustomization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 20)
)


class _FxoFeocOnCallFailureEnable_Type(MxEnableState):
    """Custom type fxoFeocOnCallFailureEnable based on MxEnableState"""
    defaultValue = 1


_FxoFeocOnCallFailureEnable_Type.__name__ = "MxEnableState"
_FxoFeocOnCallFailureEnable_Object = MibScalar
fxoFeocOnCallFailureEnable = _FxoFeocOnCallFailureEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 20, 5),
    _FxoFeocOnCallFailureEnable_Type()
)
fxoFeocOnCallFailureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoFeocOnCallFailureEnable.setStatus("current")


class _FxoFeocOnCallFailureTimeout_Type(Unsigned32):
    """Custom type fxoFeocOnCallFailureTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_FxoFeocOnCallFailureTimeout_Type.__name__ = "Unsigned32"
_FxoFeocOnCallFailureTimeout_Object = MibScalar
fxoFeocOnCallFailureTimeout = _FxoFeocOnCallFailureTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 20, 10),
    _FxoFeocOnCallFailureTimeout_Type()
)
fxoFeocOnCallFailureTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoFeocOnCallFailureTimeout.setStatus("current")


class _FxoFeocOnSilenceDetectionMode_Type(Integer32):
    """Custom type fxoFeocOnSilenceDetectionMode based on Integer32"""
    defaultValue = 0

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
        *(("disable", 0),
          ("onScnSilent", 1),
          ("onIpSilent", 2),
          ("onIpAndScnSilent", 3),
          ("onIpOrScnSilent", 4))
    )


_FxoFeocOnSilenceDetectionMode_Type.__name__ = "Integer32"
_FxoFeocOnSilenceDetectionMode_Object = MibScalar
fxoFeocOnSilenceDetectionMode = _FxoFeocOnSilenceDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 20, 15),
    _FxoFeocOnSilenceDetectionMode_Type()
)
fxoFeocOnSilenceDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoFeocOnSilenceDetectionMode.setStatus("current")


class _FxoFeocOnSilenceDetectionTimeout_Type(Unsigned32):
    """Custom type fxoFeocOnSilenceDetectionTimeout based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_FxoFeocOnSilenceDetectionTimeout_Type.__name__ = "Unsigned32"
_FxoFeocOnSilenceDetectionTimeout_Object = MibScalar
fxoFeocOnSilenceDetectionTimeout = _FxoFeocOnSilenceDetectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 20, 20),
    _FxoFeocOnSilenceDetectionTimeout_Type()
)
fxoFeocOnSilenceDetectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoFeocOnSilenceDetectionTimeout.setStatus("current")


class _FxoFeocOnToneDetectionMode_Type(Integer32):
    """Custom type fxoFeocOnToneDetectionMode based on Integer32"""
    defaultValue = 1

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
          ("countryTone", 1),
          ("customTone", 2))
    )


_FxoFeocOnToneDetectionMode_Type.__name__ = "Integer32"
_FxoFeocOnToneDetectionMode_Object = MibScalar
fxoFeocOnToneDetectionMode = _FxoFeocOnToneDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 20, 25),
    _FxoFeocOnToneDetectionMode_Type()
)
fxoFeocOnToneDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoFeocOnToneDetectionMode.setStatus("current")
_FxoEndOfCallToneCustomSettings_ObjectIdentity = ObjectIdentity
fxoEndOfCallToneCustomSettings = _FxoEndOfCallToneCustomSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 20, 30)
)


class _FxoEndOfCallToneCustomFrequency_Type(Unsigned32):
    """Custom type fxoEndOfCallToneCustomFrequency based on Unsigned32"""
    defaultValue = 440

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(350, 620),
    )


_FxoEndOfCallToneCustomFrequency_Type.__name__ = "Unsigned32"
_FxoEndOfCallToneCustomFrequency_Object = MibScalar
fxoEndOfCallToneCustomFrequency = _FxoEndOfCallToneCustomFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 20, 30, 5),
    _FxoEndOfCallToneCustomFrequency_Type()
)
fxoEndOfCallToneCustomFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoEndOfCallToneCustomFrequency.setStatus("current")


class _FxoEndOfCallToneCustomCadence_Type(OctetString):
    """Custom type fxoEndOfCallToneCustomCadence based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FxoEndOfCallToneCustomCadence_Type.__name__ = "OctetString"
_FxoEndOfCallToneCustomCadence_Object = MibScalar
fxoEndOfCallToneCustomCadence = _FxoEndOfCallToneCustomCadence_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 20, 30, 10),
    _FxoEndOfCallToneCustomCadence_Type()
)
fxoEndOfCallToneCustomCadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoEndOfCallToneCustomCadence.setStatus("current")


class _FxoEndOfCallToneCustomRepetition_Type(Unsigned32):
    """Custom type fxoEndOfCallToneCustomRepetition based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_FxoEndOfCallToneCustomRepetition_Type.__name__ = "Unsigned32"
_FxoEndOfCallToneCustomRepetition_Object = MibScalar
fxoEndOfCallToneCustomRepetition = _FxoEndOfCallToneCustomRepetition_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 20, 30, 15),
    _FxoEndOfCallToneCustomRepetition_Type()
)
fxoEndOfCallToneCustomRepetition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoEndOfCallToneCustomRepetition.setStatus("current")
_FxoIfAnalogLineTypeTable_Object = MibTable
fxoIfAnalogLineTypeTable = _FxoIfAnalogLineTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 25)
)
if mibBuilder.loadTexts:
    fxoIfAnalogLineTypeTable.setStatus("current")
_FxoIfAnalogLineTypeEntry_Object = MibTableRow
fxoIfAnalogLineTypeEntry = _FxoIfAnalogLineTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 25, 5)
)
fxoIfAnalogLineTypeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fxoIfAnalogLineTypeEntry.setStatus("current")


class _FxoIfAnalogLineType_Type(Integer32):
    """Custom type fxoIfAnalogLineType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loopStart", 0),
          ("groundStart", 1))
    )


_FxoIfAnalogLineType_Type.__name__ = "Integer32"
_FxoIfAnalogLineType_Object = MibTableColumn
fxoIfAnalogLineType = _FxoIfAnalogLineType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 25, 5, 5),
    _FxoIfAnalogLineType_Type()
)
fxoIfAnalogLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoIfAnalogLineType.setStatus("current")
_FxoIfIncomingCallNotAllowedBehaviorTable_Object = MibTable
fxoIfIncomingCallNotAllowedBehaviorTable = _FxoIfIncomingCallNotAllowedBehaviorTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 50)
)
if mibBuilder.loadTexts:
    fxoIfIncomingCallNotAllowedBehaviorTable.setStatus("current")
_FxoIfIncomingCallNotAllowedBehaviorEntry_Object = MibTableRow
fxoIfIncomingCallNotAllowedBehaviorEntry = _FxoIfIncomingCallNotAllowedBehaviorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 50, 5)
)
fxoIfIncomingCallNotAllowedBehaviorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fxoIfIncomingCallNotAllowedBehaviorEntry.setStatus("current")


class _FxoIfIncomingCallNotAllowedBehavior_Type(Integer32):
    """Custom type fxoIfIncomingCallNotAllowedBehavior based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNotAnswer", 0),
          ("playCongestionTone", 1))
    )


_FxoIfIncomingCallNotAllowedBehavior_Type.__name__ = "Integer32"
_FxoIfIncomingCallNotAllowedBehavior_Object = MibTableColumn
fxoIfIncomingCallNotAllowedBehavior = _FxoIfIncomingCallNotAllowedBehavior_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 50, 5, 5),
    _FxoIfIncomingCallNotAllowedBehavior_Type()
)
fxoIfIncomingCallNotAllowedBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoIfIncomingCallNotAllowedBehavior.setStatus("current")


class _FxoConnectCallDelay_Type(Unsigned32):
    """Custom type fxoConnectCallDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_FxoConnectCallDelay_Type.__name__ = "Unsigned32"
_FxoConnectCallDelay_Object = MibScalar
fxoConnectCallDelay = _FxoConnectCallDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 1, 60),
    _FxoConnectCallDelay_Type()
)
fxoConnectCallDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoConnectCallDelay.setStatus("current")
_FxoConformance_ObjectIdentity = ObjectIdentity
fxoConformance = _FxoConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 5)
)
_FxoCompliances_ObjectIdentity = ObjectIdentity
fxoCompliances = _FxoCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 5, 1)
)
_FxoGroups_ObjectIdentity = ObjectIdentity
fxoGroups = _FxoGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 5, 5)
)

# Managed Objects groups

fxoBasicGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 5, 5, 5)
)
fxoBasicGroupVer1.setObjects(
    ("MX-FXO-MIB", "fxoConnectCallDelay")
)
if mibBuilder.loadTexts:
    fxoBasicGroupVer1.setStatus("current")

fxoLinePropertiesCustomizationVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 5, 5, 10)
)
fxoLinePropertiesCustomizationVer1.setObjects(
      *(("MX-FXO-MIB", "fxoDialtoneDetectionMode"),
        ("MX-FXO-MIB", "fxoDialtoneDetectionTimeout"),
        ("MX-FXO-MIB", "fxoCallerIdDetectionRange"))
)
if mibBuilder.loadTexts:
    fxoLinePropertiesCustomizationVer1.setStatus("current")

fxoLineFaultDetectionVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 5, 5, 15)
)
fxoLineFaultDetectionVer1.setObjects(
      *(("MX-FXO-MIB", "fxoLineFaultDetectionEnable"),
        ("MX-FXO-MIB", "fxoLineSeizureTimeout"),
        ("MX-FXO-MIB", "fxoLineStatus"))
)
if mibBuilder.loadTexts:
    fxoLineFaultDetectionVer1.setStatus("current")

fxoIfAnsweringDelayTableVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 5, 5, 20)
)
fxoIfAnsweringDelayTableVer1.setObjects(
      *(("MX-FXO-MIB", "fxoPreAnswerDelay"),
        ("MX-FXO-MIB", "fxoAnswerOnCallerIdDetectionEnable"),
        ("MX-FXO-MIB", "fxoWaitForCalleeToAnswerEnable"))
)
if mibBuilder.loadTexts:
    fxoIfAnsweringDelayTableVer1.setStatus("current")

fxoForcedEndOfCallVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 5, 5, 25)
)
fxoForcedEndOfCallVer1.setObjects(
      *(("MX-FXO-MIB", "fxoFeocOnCallFailureEnable"),
        ("MX-FXO-MIB", "fxoFeocOnCallFailureTimeout"),
        ("MX-FXO-MIB", "fxoFeocOnSilenceDetectionMode"),
        ("MX-FXO-MIB", "fxoFeocOnSilenceDetectionTimeout"),
        ("MX-FXO-MIB", "fxoFeocOnToneDetectionMode"),
        ("MX-FXO-MIB", "fxoEndOfCallToneCustomFrequency"),
        ("MX-FXO-MIB", "fxoEndOfCallToneCustomCadence"),
        ("MX-FXO-MIB", "fxoEndOfCallToneCustomRepetition"))
)
if mibBuilder.loadTexts:
    fxoForcedEndOfCallVer1.setStatus("current")

fxoIfAnalogLineTypeTableVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 5, 5, 30)
)
fxoIfAnalogLineTypeTableVer1.setObjects(
    ("MX-FXO-MIB", "fxoIfAnalogLineType")
)
if mibBuilder.loadTexts:
    fxoIfAnalogLineTypeTableVer1.setStatus("current")

fxoIfIncomingCallNotAllowedBehaviorTableVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 5, 5, 35)
)
fxoIfIncomingCallNotAllowedBehaviorTableVer1.setObjects(
    ("MX-FXO-MIB", "fxoIfIncomingCallNotAllowedBehavior")
)
if mibBuilder.loadTexts:
    fxoIfIncomingCallNotAllowedBehaviorTableVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fxoComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 45, 5, 1, 1)
)
fxoComplVer1.setObjects(
      *(("MX-FXO-MIB", "fxoBasicGroupVer1"),
        ("MX-FXO-MIB", "fxoLinePropertiesCustomizationVer1"),
        ("MX-FXO-MIB", "fxoLineFaultDetectionVer1"),
        ("MX-FXO-MIB", "fxoIfAnsweringDelayTableVer1"),
        ("MX-FXO-MIB", "fxoForcedEndOfCallVer1"),
        ("MX-FXO-MIB", "fxoIfAnalogLineTypeTableVer1"),
        ("MX-FXO-MIB", "fxoIfIncomingCallNotAllowedBehaviorTableVer1"))
)
if mibBuilder.loadTexts:
    fxoComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-FXO-MIB",
    **{"fxoMIB": fxoMIB,
       "fxoMIBObjects": fxoMIBObjects,
       "fxoLinePropertiesCustomization": fxoLinePropertiesCustomization,
       "fxoDialtoneDetectionMode": fxoDialtoneDetectionMode,
       "fxoDialtoneDetectionTimeout": fxoDialtoneDetectionTimeout,
       "fxoCallerIdDetectionRange": fxoCallerIdDetectionRange,
       "fxoAnswerSupervisionMode": fxoAnswerSupervisionMode,
       "fxoLineFaultDetection": fxoLineFaultDetection,
       "fxoLineFaultDetectionEnable": fxoLineFaultDetectionEnable,
       "fxoLineSeizureTimeout": fxoLineSeizureTimeout,
       "fxoIfLineStatusTable": fxoIfLineStatusTable,
       "fxoIfLineStatusEntry": fxoIfLineStatusEntry,
       "fxoLineStatus": fxoLineStatus,
       "fxoIfAnsweringDelayTable": fxoIfAnsweringDelayTable,
       "fxoIfAnsweringDelayEntry": fxoIfAnsweringDelayEntry,
       "fxoPreAnswerDelay": fxoPreAnswerDelay,
       "fxoAnswerOnCallerIdDetectionEnable": fxoAnswerOnCallerIdDetectionEnable,
       "fxoWaitForCalleeToAnswerEnable": fxoWaitForCalleeToAnswerEnable,
       "fxoForcedEndOfCallCustomization": fxoForcedEndOfCallCustomization,
       "fxoFeocOnCallFailureEnable": fxoFeocOnCallFailureEnable,
       "fxoFeocOnCallFailureTimeout": fxoFeocOnCallFailureTimeout,
       "fxoFeocOnSilenceDetectionMode": fxoFeocOnSilenceDetectionMode,
       "fxoFeocOnSilenceDetectionTimeout": fxoFeocOnSilenceDetectionTimeout,
       "fxoFeocOnToneDetectionMode": fxoFeocOnToneDetectionMode,
       "fxoEndOfCallToneCustomSettings": fxoEndOfCallToneCustomSettings,
       "fxoEndOfCallToneCustomFrequency": fxoEndOfCallToneCustomFrequency,
       "fxoEndOfCallToneCustomCadence": fxoEndOfCallToneCustomCadence,
       "fxoEndOfCallToneCustomRepetition": fxoEndOfCallToneCustomRepetition,
       "fxoIfAnalogLineTypeTable": fxoIfAnalogLineTypeTable,
       "fxoIfAnalogLineTypeEntry": fxoIfAnalogLineTypeEntry,
       "fxoIfAnalogLineType": fxoIfAnalogLineType,
       "fxoIfIncomingCallNotAllowedBehaviorTable": fxoIfIncomingCallNotAllowedBehaviorTable,
       "fxoIfIncomingCallNotAllowedBehaviorEntry": fxoIfIncomingCallNotAllowedBehaviorEntry,
       "fxoIfIncomingCallNotAllowedBehavior": fxoIfIncomingCallNotAllowedBehavior,
       "fxoConnectCallDelay": fxoConnectCallDelay,
       "fxoConformance": fxoConformance,
       "fxoCompliances": fxoCompliances,
       "fxoComplVer1": fxoComplVer1,
       "fxoGroups": fxoGroups,
       "fxoBasicGroupVer1": fxoBasicGroupVer1,
       "fxoLinePropertiesCustomizationVer1": fxoLinePropertiesCustomizationVer1,
       "fxoLineFaultDetectionVer1": fxoLineFaultDetectionVer1,
       "fxoIfAnsweringDelayTableVer1": fxoIfAnsweringDelayTableVer1,
       "fxoForcedEndOfCallVer1": fxoForcedEndOfCallVer1,
       "fxoIfAnalogLineTypeTableVer1": fxoIfAnalogLineTypeTableVer1,
       "fxoIfIncomingCallNotAllowedBehaviorTableVer1": fxoIfIncomingCallNotAllowedBehaviorTableVer1}
)
