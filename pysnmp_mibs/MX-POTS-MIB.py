# SNMP MIB module (MX-POTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-POTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:30 2025
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

(mediatrixServices,) = mibBuilder.importSymbols(
    "MX-SMI2",
    "mediatrixServices")

(MxActivationState,
 MxAdvancedIpPort,
 MxDigitMap,
 MxEnableState,
 MxIpAddress,
 MxIpHostName,
 MxIpPort,
 MxIpSubnetMask) = mibBuilder.importSymbols(
    "MX-TC",
    "MxActivationState",
    "MxAdvancedIpPort",
    "MxDigitMap",
    "MxEnableState",
    "MxIpAddress",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSubnetMask")

(MxFloat32,
 MxIpAddr,
 MxIpAddrMask,
 MxIpAddrPort,
 MxIpHostNamePort,
 MxUInt64,
 MxUri,
 MxUrl) = mibBuilder.importSymbols(
    "MX-TC2",
    "MxFloat32",
    "MxIpAddr",
    "MxIpAddrMask",
    "MxIpAddrPort",
    "MxIpHostNamePort",
    "MxUInt64",
    "MxUri",
    "MxUrl")

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

potsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PotsMIBObjects_ObjectIdentity = ObjectIdentity
potsMIBObjects = _PotsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1)
)
_LineTable_Object = MibTable
lineTable = _LineTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 100)
)
if mibBuilder.loadTexts:
    lineTable.setStatus("current")
_LineEntry_Object = MibTableRow
lineEntry = _LineEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 100, 1)
)
lineEntry.setIndexNames(
    (0, "MX-POTS-MIB", "lineId"),
)
if mibBuilder.loadTexts:
    lineEntry.setStatus("current")
_LineId_Type = OctetString
_LineId_Object = MibTableColumn
lineId = _LineId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 100, 1, 100),
    _LineId_Type()
)
lineId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineId.setStatus("current")


class _LineTypeStatus_Type(Integer32):
    """Custom type lineTypeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("fxs", 100),
          ("fxo", 200))
    )


_LineTypeStatus_Type.__name__ = "Integer32"
_LineTypeStatus_Object = MibTableColumn
lineTypeStatus = _LineTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 100, 1, 200),
    _LineTypeStatus_Type()
)
lineTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineTypeStatus.setStatus("current")


class _LineState_Type(Integer32):
    """Custom type lineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("idle", 100),
          ("inUse", 200),
          ("disabled", 300),
          ("bypass", 400),
          ("down", 500))
    )


_LineState_Type.__name__ = "Integer32"
_LineState_Object = MibTableColumn
lineState = _LineState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 100, 1, 300),
    _LineState_Type()
)
lineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineState.setStatus("current")


class _CallerIdCustomization_Type(Integer32):
    """Custom type callerIdCustomization based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("country", 100),
          ("etsiDtmf", 200),
          ("etsiFsk", 300))
    )


_CallerIdCustomization_Type.__name__ = "Integer32"
_CallerIdCustomization_Object = MibScalar
callerIdCustomization = _CallerIdCustomization_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 200),
    _CallerIdCustomization_Type()
)
callerIdCustomization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callerIdCustomization.setStatus("current")


class _DtmfMapDigitDetection_Type(Integer32):
    """Custom type dtmfMapDigitDetection based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("whenPressed", 100),
          ("whenReleased", 200))
    )


_DtmfMapDigitDetection_Type.__name__ = "Integer32"
_DtmfMapDigitDetection_Object = MibScalar
dtmfMapDigitDetection = _DtmfMapDigitDetection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 300),
    _DtmfMapDigitDetection_Type()
)
dtmfMapDigitDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtmfMapDigitDetection.setStatus("current")


class _VocalUnitInformation_Type(Integer32):
    """Custom type vocalUnitInformation based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("all", 200))
    )


_VocalUnitInformation_Type.__name__ = "Integer32"
_VocalUnitInformation_Object = MibScalar
vocalUnitInformation = _VocalUnitInformation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 400),
    _VocalUnitInformation_Type()
)
vocalUnitInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vocalUnitInformation.setStatus("current")


class _CallerIdTransmission_Type(Integer32):
    """Custom type callerIdTransmission based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700)
        )
    )
    namedValues = NamedValues(
        *(("country", 100),
          ("firstRing", 200),
          ("ringPulse", 300),
          ("lineReversalRingPulse", 400),
          ("dtAs", 500),
          ("lineReversalDtAs", 600),
          ("noRingPulse", 700))
    )


_CallerIdTransmission_Type.__name__ = "Integer32"
_CallerIdTransmission_Object = MibScalar
callerIdTransmission = _CallerIdTransmission_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 500),
    _CallerIdTransmission_Type()
)
callerIdTransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callerIdTransmission.setStatus("current")
_FxsGroup_ObjectIdentity = ObjectIdentity
fxsGroup = _FxsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000)
)


class _FxsLineSupervisionMode_Type(Integer32):
    """Custom type fxsLineSupervisionMode based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("dropOnDisconnect", 200),
          ("reversalOnIdle", 300),
          ("reversalOnEstablished", 400))
    )


_FxsLineSupervisionMode_Type.__name__ = "Integer32"
_FxsLineSupervisionMode_Object = MibScalar
fxsLineSupervisionMode = _FxsLineSupervisionMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 100),
    _FxsLineSupervisionMode_Type()
)
fxsLineSupervisionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsLineSupervisionMode.setStatus("current")


class _FxsDisconnectDelay_Type(Unsigned32):
    """Custom type fxsDisconnectDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_FxsDisconnectDelay_Type.__name__ = "Unsigned32"
_FxsDisconnectDelay_Object = MibScalar
fxsDisconnectDelay = _FxsDisconnectDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 200),
    _FxsDisconnectDelay_Type()
)
fxsDisconnectDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsDisconnectDelay.setStatus("current")


class _FxsInbandRingback_Type(MxEnableState):
    """Custom type fxsInbandRingback based on MxEnableState"""
    defaultValue = 0


_FxsInbandRingback_Type.__name__ = "MxEnableState"
_FxsInbandRingback_Object = MibScalar
fxsInbandRingback = _FxsInbandRingback_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 300),
    _FxsInbandRingback_Type()
)
fxsInbandRingback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsInbandRingback.setStatus("current")


class _FxsShutdownBehavior_Type(Integer32):
    """Custom type fxsShutdownBehavior based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("disabledTone", 100),
          ("powerDrop", 200))
    )


_FxsShutdownBehavior_Type.__name__ = "Integer32"
_FxsShutdownBehavior_Object = MibScalar
fxsShutdownBehavior = _FxsShutdownBehavior_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 400),
    _FxsShutdownBehavior_Type()
)
fxsShutdownBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsShutdownBehavior.setStatus("current")


class _FxsPowerDropOnDisconnectDuration_Type(Unsigned32):
    """Custom type fxsPowerDropOnDisconnectDuration based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_FxsPowerDropOnDisconnectDuration_Type.__name__ = "Unsigned32"
_FxsPowerDropOnDisconnectDuration_Object = MibScalar
fxsPowerDropOnDisconnectDuration = _FxsPowerDropOnDisconnectDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 500),
    _FxsPowerDropOnDisconnectDuration_Type()
)
fxsPowerDropOnDisconnectDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPowerDropOnDisconnectDuration.setStatus("current")


class _FxsServiceActivation_Type(Integer32):
    """Custom type fxsServiceActivation based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("flashHook", 100),
          ("flashHookAndDigit", 200))
    )


_FxsServiceActivation_Type.__name__ = "Integer32"
_FxsServiceActivation_Object = MibScalar
fxsServiceActivation = _FxsServiceActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 600),
    _FxsServiceActivation_Type()
)
fxsServiceActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsServiceActivation.setStatus("current")


class _FxsCallerIdPrivateCallingPartyName_Type(OctetString):
    """Custom type fxsCallerIdPrivateCallingPartyName based on OctetString"""
    defaultValue = OctetString("Anonymous")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FxsCallerIdPrivateCallingPartyName_Type.__name__ = "OctetString"
_FxsCallerIdPrivateCallingPartyName_Object = MibScalar
fxsCallerIdPrivateCallingPartyName = _FxsCallerIdPrivateCallingPartyName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 700),
    _FxsCallerIdPrivateCallingPartyName_Type()
)
fxsCallerIdPrivateCallingPartyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsCallerIdPrivateCallingPartyName.setStatus("current")


class _FxsSipMessageAlertingEnable_Type(MxEnableState):
    """Custom type fxsSipMessageAlertingEnable based on MxEnableState"""
    defaultValue = 0


_FxsSipMessageAlertingEnable_Type.__name__ = "MxEnableState"
_FxsSipMessageAlertingEnable_Object = MibScalar
fxsSipMessageAlertingEnable = _FxsSipMessageAlertingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 800),
    _FxsSipMessageAlertingEnable_Type()
)
fxsSipMessageAlertingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsSipMessageAlertingEnable.setStatus("current")
_FxsCountryCustomizationGroup_ObjectIdentity = ObjectIdentity
fxsCountryCustomizationGroup = _FxsCountryCustomizationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10000)
)


class _FxsCountryCustomizationOverride_Type(MxEnableState):
    """Custom type fxsCountryCustomizationOverride based on MxEnableState"""
    defaultValue = 0


_FxsCountryCustomizationOverride_Type.__name__ = "MxEnableState"
_FxsCountryCustomizationOverride_Object = MibScalar
fxsCountryCustomizationOverride = _FxsCountryCustomizationOverride_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10000, 100),
    _FxsCountryCustomizationOverride_Type()
)
fxsCountryCustomizationOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsCountryCustomizationOverride.setStatus("current")


class _FxsCountryCustomizationLoopCurrent_Type(Unsigned32):
    """Custom type fxsCountryCustomizationLoopCurrent based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 32),
    )


_FxsCountryCustomizationLoopCurrent_Type.__name__ = "Unsigned32"
_FxsCountryCustomizationLoopCurrent_Object = MibScalar
fxsCountryCustomizationLoopCurrent = _FxsCountryCustomizationLoopCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10000, 200),
    _FxsCountryCustomizationLoopCurrent_Type()
)
fxsCountryCustomizationLoopCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsCountryCustomizationLoopCurrent.setStatus("current")


class _FxsCountryCustomizationFlashHookDetectionRange_Type(OctetString):
    """Custom type fxsCountryCustomizationFlashHookDetectionRange based on OctetString"""
    defaultValue = OctetString("100-1200")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 9),
    )


_FxsCountryCustomizationFlashHookDetectionRange_Type.__name__ = "OctetString"
_FxsCountryCustomizationFlashHookDetectionRange_Object = MibScalar
fxsCountryCustomizationFlashHookDetectionRange = _FxsCountryCustomizationFlashHookDetectionRange_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10000, 300),
    _FxsCountryCustomizationFlashHookDetectionRange_Type()
)
fxsCountryCustomizationFlashHookDetectionRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsCountryCustomizationFlashHookDetectionRange.setStatus("current")
_FxsBypassGroup_ObjectIdentity = ObjectIdentity
fxsBypassGroup = _FxsBypassGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10100)
)
_FxsBypassTable_Object = MibTable
fxsBypassTable = _FxsBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10100, 1000)
)
if mibBuilder.loadTexts:
    fxsBypassTable.setStatus("current")
_FxsBypassEntry_Object = MibTableRow
fxsBypassEntry = _FxsBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10100, 1000, 1)
)
fxsBypassEntry.setIndexNames(
    (0, "MX-POTS-MIB", "fxsBypassId"),
)
if mibBuilder.loadTexts:
    fxsBypassEntry.setStatus("current")
_FxsBypassId_Type = OctetString
_FxsBypassId_Object = MibTableColumn
fxsBypassId = _FxsBypassId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10100, 1000, 1, 100),
    _FxsBypassId_Type()
)
fxsBypassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsBypassId.setStatus("current")


class _FxsBypassActivation_Type(Integer32):
    """Custom type fxsBypassActivation based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 100),
          ("endpointDisabled", 200),
          ("onDemand", 300))
    )


_FxsBypassActivation_Type.__name__ = "Integer32"
_FxsBypassActivation_Object = MibTableColumn
fxsBypassActivation = _FxsBypassActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10100, 1000, 1, 200),
    _FxsBypassActivation_Type()
)
fxsBypassActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsBypassActivation.setStatus("current")


class _FxsBypassActivationDtmfMap_Type(MxDigitMap):
    """Custom type fxsBypassActivationDtmfMap based on MxDigitMap"""
    defaultValue = OctetString("")


_FxsBypassActivationDtmfMap_Type.__name__ = "MxDigitMap"
_FxsBypassActivationDtmfMap_Object = MibTableColumn
fxsBypassActivationDtmfMap = _FxsBypassActivationDtmfMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10100, 1000, 1, 300),
    _FxsBypassActivationDtmfMap_Type()
)
fxsBypassActivationDtmfMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsBypassActivationDtmfMap.setStatus("current")


class _FxsBypassDeactivationTimeout_Type(Unsigned32):
    """Custom type fxsBypassDeactivationTimeout based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FxsBypassDeactivationTimeout_Type.__name__ = "Unsigned32"
_FxsBypassDeactivationTimeout_Object = MibTableColumn
fxsBypassDeactivationTimeout = _FxsBypassDeactivationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10100, 1000, 1, 400),
    _FxsBypassDeactivationTimeout_Type()
)
fxsBypassDeactivationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsBypassDeactivationTimeout.setStatus("current")
_FxsMessageWaitingIndicatorGroup_ObjectIdentity = ObjectIdentity
fxsMessageWaitingIndicatorGroup = _FxsMessageWaitingIndicatorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10200)
)


class _FxsDefaultMessageWaitingIndicatorActivation_Type(Integer32):
    """Custom type fxsDefaultMessageWaitingIndicatorActivation based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 100),
          ("tone", 200),
          ("visual", 300),
          ("toneAndVisual", 400))
    )


_FxsDefaultMessageWaitingIndicatorActivation_Type.__name__ = "Integer32"
_FxsDefaultMessageWaitingIndicatorActivation_Object = MibScalar
fxsDefaultMessageWaitingIndicatorActivation = _FxsDefaultMessageWaitingIndicatorActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10200, 100),
    _FxsDefaultMessageWaitingIndicatorActivation_Type()
)
fxsDefaultMessageWaitingIndicatorActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsDefaultMessageWaitingIndicatorActivation.setStatus("current")


class _FxsDefaultVisualMessageWaitingIndicatorType_Type(Integer32):
    """Custom type fxsDefaultVisualMessageWaitingIndicatorType based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("fsk", 100),
          ("fskAndVoltage", 200))
    )


_FxsDefaultVisualMessageWaitingIndicatorType_Type.__name__ = "Integer32"
_FxsDefaultVisualMessageWaitingIndicatorType_Object = MibScalar
fxsDefaultVisualMessageWaitingIndicatorType = _FxsDefaultVisualMessageWaitingIndicatorType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10200, 150),
    _FxsDefaultVisualMessageWaitingIndicatorType_Type()
)
fxsDefaultVisualMessageWaitingIndicatorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsDefaultVisualMessageWaitingIndicatorType.setStatus("current")
_FxsSpecificMessageWaitingIndicatorTable_Object = MibTable
fxsSpecificMessageWaitingIndicatorTable = _FxsSpecificMessageWaitingIndicatorTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10200, 200)
)
if mibBuilder.loadTexts:
    fxsSpecificMessageWaitingIndicatorTable.setStatus("current")
_FxsSpecificMessageWaitingIndicatorEntry_Object = MibTableRow
fxsSpecificMessageWaitingIndicatorEntry = _FxsSpecificMessageWaitingIndicatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10200, 200, 1)
)
fxsSpecificMessageWaitingIndicatorEntry.setIndexNames(
    (0, "MX-POTS-MIB", "fxsSpecificMessageWaitingIndicatorId"),
)
if mibBuilder.loadTexts:
    fxsSpecificMessageWaitingIndicatorEntry.setStatus("current")
_FxsSpecificMessageWaitingIndicatorId_Type = OctetString
_FxsSpecificMessageWaitingIndicatorId_Object = MibTableColumn
fxsSpecificMessageWaitingIndicatorId = _FxsSpecificMessageWaitingIndicatorId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10200, 200, 1, 100),
    _FxsSpecificMessageWaitingIndicatorId_Type()
)
fxsSpecificMessageWaitingIndicatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsSpecificMessageWaitingIndicatorId.setStatus("current")


class _FxsSpecificMessageWaitingIndicatorEnableConfig_Type(MxEnableState):
    """Custom type fxsSpecificMessageWaitingIndicatorEnableConfig based on MxEnableState"""
    defaultValue = 0


_FxsSpecificMessageWaitingIndicatorEnableConfig_Type.__name__ = "MxEnableState"
_FxsSpecificMessageWaitingIndicatorEnableConfig_Object = MibTableColumn
fxsSpecificMessageWaitingIndicatorEnableConfig = _FxsSpecificMessageWaitingIndicatorEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10200, 200, 1, 200),
    _FxsSpecificMessageWaitingIndicatorEnableConfig_Type()
)
fxsSpecificMessageWaitingIndicatorEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsSpecificMessageWaitingIndicatorEnableConfig.setStatus("current")


class _FxsSpecificMessageWaitingIndicatorActivation_Type(Integer32):
    """Custom type fxsSpecificMessageWaitingIndicatorActivation based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 100),
          ("tone", 200),
          ("visual", 300),
          ("toneAndVisual", 400))
    )


_FxsSpecificMessageWaitingIndicatorActivation_Type.__name__ = "Integer32"
_FxsSpecificMessageWaitingIndicatorActivation_Object = MibTableColumn
fxsSpecificMessageWaitingIndicatorActivation = _FxsSpecificMessageWaitingIndicatorActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10200, 200, 1, 300),
    _FxsSpecificMessageWaitingIndicatorActivation_Type()
)
fxsSpecificMessageWaitingIndicatorActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsSpecificMessageWaitingIndicatorActivation.setStatus("current")
_FxsCallGroup_ObjectIdentity = ObjectIdentity
fxsCallGroup = _FxsCallGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10300)
)


class _FxsDefaultAutoCancelTimeout_Type(Unsigned32):
    """Custom type fxsDefaultAutoCancelTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FxsDefaultAutoCancelTimeout_Type.__name__ = "Unsigned32"
_FxsDefaultAutoCancelTimeout_Object = MibScalar
fxsDefaultAutoCancelTimeout = _FxsDefaultAutoCancelTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10300, 100),
    _FxsDefaultAutoCancelTimeout_Type()
)
fxsDefaultAutoCancelTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsDefaultAutoCancelTimeout.setStatus("current")
_FxsEmergencyCallGroup_ObjectIdentity = ObjectIdentity
fxsEmergencyCallGroup = _FxsEmergencyCallGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10400)
)


class _FxsEmergencyCallOverride_Type(Integer32):
    """Custom type fxsEmergencyCallOverride based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("noOverride", 100),
          ("noServices", 200),
          ("noDisconnect", 300))
    )


_FxsEmergencyCallOverride_Type.__name__ = "Integer32"
_FxsEmergencyCallOverride_Object = MibScalar
fxsEmergencyCallOverride = _FxsEmergencyCallOverride_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10400, 100),
    _FxsEmergencyCallOverride_Type()
)
fxsEmergencyCallOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsEmergencyCallOverride.setStatus("current")


class _FxsEmergencyRingTimeout_Type(Unsigned32):
    """Custom type fxsEmergencyRingTimeout based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180000),
    )


_FxsEmergencyRingTimeout_Type.__name__ = "Unsigned32"
_FxsEmergencyRingTimeout_Object = MibScalar
fxsEmergencyRingTimeout = _FxsEmergencyRingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10400, 200),
    _FxsEmergencyRingTimeout_Type()
)
fxsEmergencyRingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsEmergencyRingTimeout.setStatus("current")
_FxsRingGroup_ObjectIdentity = ObjectIdentity
fxsRingGroup = _FxsRingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10500)
)
_FxsDistinctiveRingTable_Object = MibTable
fxsDistinctiveRingTable = _FxsDistinctiveRingTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10500, 100)
)
if mibBuilder.loadTexts:
    fxsDistinctiveRingTable.setStatus("current")
_FxsDistinctiveRingEntry_Object = MibTableRow
fxsDistinctiveRingEntry = _FxsDistinctiveRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10500, 100, 1)
)
fxsDistinctiveRingEntry.setIndexNames(
    (0, "MX-POTS-MIB", "fxsDistinctiveRingIndex"),
)
if mibBuilder.loadTexts:
    fxsDistinctiveRingEntry.setStatus("current")


class _FxsDistinctiveRingIndex_Type(Unsigned32):
    """Custom type fxsDistinctiveRingIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_FxsDistinctiveRingIndex_Type.__name__ = "Unsigned32"
_FxsDistinctiveRingIndex_Object = MibTableColumn
fxsDistinctiveRingIndex = _FxsDistinctiveRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10500, 100, 1, 100),
    _FxsDistinctiveRingIndex_Type()
)
fxsDistinctiveRingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsDistinctiveRingIndex.setStatus("current")


class _FxsDistinctiveRingRingId_Type(OctetString):
    """Custom type fxsDistinctiveRingRingId based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_FxsDistinctiveRingRingId_Type.__name__ = "OctetString"
_FxsDistinctiveRingRingId_Object = MibTableColumn
fxsDistinctiveRingRingId = _FxsDistinctiveRingRingId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10500, 100, 1, 200),
    _FxsDistinctiveRingRingId_Type()
)
fxsDistinctiveRingRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsDistinctiveRingRingId.setStatus("current")


class _FxsDistinctiveRingPattern_Type(OctetString):
    """Custom type fxsDistinctiveRingPattern based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_FxsDistinctiveRingPattern_Type.__name__ = "OctetString"
_FxsDistinctiveRingPattern_Object = MibTableColumn
fxsDistinctiveRingPattern = _FxsDistinctiveRingPattern_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10500, 100, 1, 300),
    _FxsDistinctiveRingPattern_Type()
)
fxsDistinctiveRingPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsDistinctiveRingPattern.setStatus("current")
_FxsCallerIdGroup_ObjectIdentity = ObjectIdentity
fxsCallerIdGroup = _FxsCallerIdGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10600)
)
_FxsCallerIdTable_Object = MibTable
fxsCallerIdTable = _FxsCallerIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10600, 100)
)
if mibBuilder.loadTexts:
    fxsCallerIdTable.setStatus("current")
_FxsCallerIdEntry_Object = MibTableRow
fxsCallerIdEntry = _FxsCallerIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10600, 100, 1)
)
fxsCallerIdEntry.setIndexNames(
    (0, "MX-POTS-MIB", "fxsCallerIdId"),
)
if mibBuilder.loadTexts:
    fxsCallerIdEntry.setStatus("current")
_FxsCallerIdId_Type = OctetString
_FxsCallerIdId_Object = MibTableColumn
fxsCallerIdId = _FxsCallerIdId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10600, 100, 1, 150),
    _FxsCallerIdId_Type()
)
fxsCallerIdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsCallerIdId.setStatus("current")


class _FxsCallerIdActivation_Type(MxEnableState):
    """Custom type fxsCallerIdActivation based on MxEnableState"""
    defaultValue = 1


_FxsCallerIdActivation_Type.__name__ = "MxEnableState"
_FxsCallerIdActivation_Object = MibTableColumn
fxsCallerIdActivation = _FxsCallerIdActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 10600, 100, 1, 300),
    _FxsCallerIdActivation_Type()
)
fxsCallerIdActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsCallerIdActivation.setStatus("current")
_FxsInteropGroup_ObjectIdentity = ObjectIdentity
fxsInteropGroup = _FxsInteropGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 50000)
)


class _FxsInteropPlayLocalRingbackWhenNoMediaStream_Type(MxEnableState):
    """Custom type fxsInteropPlayLocalRingbackWhenNoMediaStream based on MxEnableState"""
    defaultValue = 0


_FxsInteropPlayLocalRingbackWhenNoMediaStream_Type.__name__ = "MxEnableState"
_FxsInteropPlayLocalRingbackWhenNoMediaStream_Object = MibScalar
fxsInteropPlayLocalRingbackWhenNoMediaStream = _FxsInteropPlayLocalRingbackWhenNoMediaStream_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 10000, 50000, 100),
    _FxsInteropPlayLocalRingbackWhenNoMediaStream_Type()
)
fxsInteropPlayLocalRingbackWhenNoMediaStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsInteropPlayLocalRingbackWhenNoMediaStream.setStatus("current")
_FxoGroup_ObjectIdentity = ObjectIdentity
fxoGroup = _FxoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000)
)


class _FxoPreDialDelay_Type(Unsigned32):
    """Custom type fxoPreDialDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_FxoPreDialDelay_Type.__name__ = "Unsigned32"
_FxoPreDialDelay_Object = MibScalar
fxoPreDialDelay = _FxoPreDialDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 100),
    _FxoPreDialDelay_Type()
)
fxoPreDialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoPreDialDelay.setStatus("current")


class _FxoDialToneDetectionMode_Type(Integer32):
    """Custom type fxoDialToneDetectionMode based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("disable", 100),
          ("countryTone", 200))
    )


_FxoDialToneDetectionMode_Type.__name__ = "Integer32"
_FxoDialToneDetectionMode_Object = MibScalar
fxoDialToneDetectionMode = _FxoDialToneDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 200),
    _FxoDialToneDetectionMode_Type()
)
fxoDialToneDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoDialToneDetectionMode.setStatus("current")


class _FxoDialToneDetectionTimeout_Type(Unsigned32):
    """Custom type fxoDialToneDetectionTimeout based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1300, 10000),
    )


_FxoDialToneDetectionTimeout_Type.__name__ = "Unsigned32"
_FxoDialToneDetectionTimeout_Object = MibScalar
fxoDialToneDetectionTimeout = _FxoDialToneDetectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 300),
    _FxoDialToneDetectionTimeout_Type()
)
fxoDialToneDetectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoDialToneDetectionTimeout.setStatus("current")
_FxoAnsweringDelayTable_Object = MibTable
fxoAnsweringDelayTable = _FxoAnsweringDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 5000)
)
if mibBuilder.loadTexts:
    fxoAnsweringDelayTable.setStatus("current")
_FxoAnsweringDelayEntry_Object = MibTableRow
fxoAnsweringDelayEntry = _FxoAnsweringDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 5000, 1)
)
fxoAnsweringDelayEntry.setIndexNames(
    (0, "MX-POTS-MIB", "fxoAnsweringDelayId"),
)
if mibBuilder.loadTexts:
    fxoAnsweringDelayEntry.setStatus("current")
_FxoAnsweringDelayId_Type = OctetString
_FxoAnsweringDelayId_Object = MibTableColumn
fxoAnsweringDelayId = _FxoAnsweringDelayId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 5000, 1, 100),
    _FxoAnsweringDelayId_Type()
)
fxoAnsweringDelayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxoAnsweringDelayId.setStatus("current")


class _FxoAnsweringDelayWaitBeforeAnsweringDelay_Type(Unsigned32):
    """Custom type fxoAnsweringDelayWaitBeforeAnsweringDelay based on Unsigned32"""
    defaultValue = 8000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_FxoAnsweringDelayWaitBeforeAnsweringDelay_Type.__name__ = "Unsigned32"
_FxoAnsweringDelayWaitBeforeAnsweringDelay_Object = MibTableColumn
fxoAnsweringDelayWaitBeforeAnsweringDelay = _FxoAnsweringDelayWaitBeforeAnsweringDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 5000, 1, 200),
    _FxoAnsweringDelayWaitBeforeAnsweringDelay_Type()
)
fxoAnsweringDelayWaitBeforeAnsweringDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoAnsweringDelayWaitBeforeAnsweringDelay.setStatus("current")


class _FxoAnsweringDelayAnsweringOnCallerIdDetection_Type(MxEnableState):
    """Custom type fxoAnsweringDelayAnsweringOnCallerIdDetection based on MxEnableState"""
    defaultValue = 1


_FxoAnsweringDelayAnsweringOnCallerIdDetection_Type.__name__ = "MxEnableState"
_FxoAnsweringDelayAnsweringOnCallerIdDetection_Object = MibTableColumn
fxoAnsweringDelayAnsweringOnCallerIdDetection = _FxoAnsweringDelayAnsweringOnCallerIdDetection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 5000, 1, 300),
    _FxoAnsweringDelayAnsweringOnCallerIdDetection_Type()
)
fxoAnsweringDelayAnsweringOnCallerIdDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoAnsweringDelayAnsweringOnCallerIdDetection.setStatus("current")


class _FxoAnsweringDelayWaitForCalleeToAnswer_Type(MxEnableState):
    """Custom type fxoAnsweringDelayWaitForCalleeToAnswer based on MxEnableState"""
    defaultValue = 0


_FxoAnsweringDelayWaitForCalleeToAnswer_Type.__name__ = "MxEnableState"
_FxoAnsweringDelayWaitForCalleeToAnswer_Object = MibTableColumn
fxoAnsweringDelayWaitForCalleeToAnswer = _FxoAnsweringDelayWaitForCalleeToAnswer_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 5000, 1, 400),
    _FxoAnsweringDelayWaitForCalleeToAnswer_Type()
)
fxoAnsweringDelayWaitForCalleeToAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoAnsweringDelayWaitForCalleeToAnswer.setStatus("current")
_FxoIncomingCallBehaviorTable_Object = MibTable
fxoIncomingCallBehaviorTable = _FxoIncomingCallBehaviorTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 5100)
)
if mibBuilder.loadTexts:
    fxoIncomingCallBehaviorTable.setStatus("current")
_FxoIncomingCallBehaviorEntry_Object = MibTableRow
fxoIncomingCallBehaviorEntry = _FxoIncomingCallBehaviorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 5100, 1)
)
fxoIncomingCallBehaviorEntry.setIndexNames(
    (0, "MX-POTS-MIB", "fxoIncomingCallBehaviorId"),
)
if mibBuilder.loadTexts:
    fxoIncomingCallBehaviorEntry.setStatus("current")
_FxoIncomingCallBehaviorId_Type = OctetString
_FxoIncomingCallBehaviorId_Object = MibTableColumn
fxoIncomingCallBehaviorId = _FxoIncomingCallBehaviorId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 5100, 1, 100),
    _FxoIncomingCallBehaviorId_Type()
)
fxoIncomingCallBehaviorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxoIncomingCallBehaviorId.setStatus("current")


class _FxoIncomingCallBehaviorNotAllowedBehavior_Type(Integer32):
    """Custom type fxoIncomingCallBehaviorNotAllowedBehavior based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("doNotAnswer", 100),
          ("playCongestionTone", 200))
    )


_FxoIncomingCallBehaviorNotAllowedBehavior_Type.__name__ = "Integer32"
_FxoIncomingCallBehaviorNotAllowedBehavior_Object = MibTableColumn
fxoIncomingCallBehaviorNotAllowedBehavior = _FxoIncomingCallBehaviorNotAllowedBehavior_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 5100, 1, 200),
    _FxoIncomingCallBehaviorNotAllowedBehavior_Type()
)
fxoIncomingCallBehaviorNotAllowedBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoIncomingCallBehaviorNotAllowedBehavior.setStatus("current")
_FxoCustomBasicParametersTable_Object = MibTable
fxoCustomBasicParametersTable = _FxoCustomBasicParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 5200)
)
if mibBuilder.loadTexts:
    fxoCustomBasicParametersTable.setStatus("current")
_FxoCustomBasicParametersEntry_Object = MibTableRow
fxoCustomBasicParametersEntry = _FxoCustomBasicParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 5200, 1)
)
fxoCustomBasicParametersEntry.setIndexNames(
    (0, "MX-POTS-MIB", "fxoCustomBasicParametersId"),
)
if mibBuilder.loadTexts:
    fxoCustomBasicParametersEntry.setStatus("current")
_FxoCustomBasicParametersId_Type = OctetString
_FxoCustomBasicParametersId_Object = MibTableColumn
fxoCustomBasicParametersId = _FxoCustomBasicParametersId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 5200, 1, 100),
    _FxoCustomBasicParametersId_Type()
)
fxoCustomBasicParametersId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxoCustomBasicParametersId.setStatus("current")


class _FxoCustomBasicParametersOverrideDefaultCountryParameters_Type(MxEnableState):
    """Custom type fxoCustomBasicParametersOverrideDefaultCountryParameters based on MxEnableState"""
    defaultValue = 0


_FxoCustomBasicParametersOverrideDefaultCountryParameters_Type.__name__ = "MxEnableState"
_FxoCustomBasicParametersOverrideDefaultCountryParameters_Object = MibTableColumn
fxoCustomBasicParametersOverrideDefaultCountryParameters = _FxoCustomBasicParametersOverrideDefaultCountryParameters_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 5200, 1, 200),
    _FxoCustomBasicParametersOverrideDefaultCountryParameters_Type()
)
fxoCustomBasicParametersOverrideDefaultCountryParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoCustomBasicParametersOverrideDefaultCountryParameters.setStatus("current")


class _FxoCustomBasicParametersImpedance_Type(Integer32):
    """Custom type fxoCustomBasicParametersImpedance based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700,
              800,
              900,
              1000,
              1100,
              1200,
              1300,
              1400,
              1500,
              1600,
              1700,
              1800,
              1900,
              2000,
              2100,
              2200,
              2300,
              2400)
        )
    )
    namedValues = NamedValues(
        *(("i600", 100),
          ("i600LongLoop", 200),
          ("i900", 300),
          ("australia", 400),
          ("austria", 500),
          ("belgium", 600),
          ("brazil", 700),
          ("china", 800),
          ("czechRepublic", 900),
          ("denmark", 1000),
          ("finland", 1100),
          ("france", 1200),
          ("germany", 1300),
          ("greece", 1400),
          ("italy", 1500),
          ("japan", 1600),
          ("netherlands", 1700),
          ("newZealand", 1800),
          ("norway", 1900),
          ("russia", 2000),
          ("slovakia", 2100),
          ("spain", 2200),
          ("sweden", 2300),
          ("uK", 2400))
    )


_FxoCustomBasicParametersImpedance_Type.__name__ = "Integer32"
_FxoCustomBasicParametersImpedance_Object = MibTableColumn
fxoCustomBasicParametersImpedance = _FxoCustomBasicParametersImpedance_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 5200, 1, 300),
    _FxoCustomBasicParametersImpedance_Type()
)
fxoCustomBasicParametersImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoCustomBasicParametersImpedance.setStatus("current")


class _FxoCustomBasicParametersDigitalHybrid_Type(OctetString):
    """Custom type fxoCustomBasicParametersDigitalHybrid based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_FxoCustomBasicParametersDigitalHybrid_Type.__name__ = "OctetString"
_FxoCustomBasicParametersDigitalHybrid_Object = MibTableColumn
fxoCustomBasicParametersDigitalHybrid = _FxoCustomBasicParametersDigitalHybrid_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 5200, 1, 400),
    _FxoCustomBasicParametersDigitalHybrid_Type()
)
fxoCustomBasicParametersDigitalHybrid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoCustomBasicParametersDigitalHybrid.setStatus("current")


class _FxoCustomBasicParametersReset_Type(Integer32):
    """Custom type fxoCustomBasicParametersReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("reset", 10))
    )


_FxoCustomBasicParametersReset_Type.__name__ = "Integer32"
_FxoCustomBasicParametersReset_Object = MibTableColumn
fxoCustomBasicParametersReset = _FxoCustomBasicParametersReset_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 5200, 1, 10000),
    _FxoCustomBasicParametersReset_Type()
)
fxoCustomBasicParametersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoCustomBasicParametersReset.setStatus("current")
_FxoLinkStateVerificationGroup_ObjectIdentity = ObjectIdentity
fxoLinkStateVerificationGroup = _FxoLinkStateVerificationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 10100)
)
_FxoLinkStateTable_Object = MibTable
fxoLinkStateTable = _FxoLinkStateTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 10100, 100)
)
if mibBuilder.loadTexts:
    fxoLinkStateTable.setStatus("current")
_FxoLinkStateEntry_Object = MibTableRow
fxoLinkStateEntry = _FxoLinkStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 10100, 100, 1)
)
fxoLinkStateEntry.setIndexNames(
    (0, "MX-POTS-MIB", "fxoLinkStateId"),
)
if mibBuilder.loadTexts:
    fxoLinkStateEntry.setStatus("current")
_FxoLinkStateId_Type = OctetString
_FxoLinkStateId_Object = MibTableColumn
fxoLinkStateId = _FxoLinkStateId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 10100, 100, 1, 100),
    _FxoLinkStateId_Type()
)
fxoLinkStateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxoLinkStateId.setStatus("current")


class _FxoLinkStateLinkState_Type(Integer32):
    """Custom type fxoLinkStateLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 100),
          ("up", 200),
          ("down", 300))
    )


_FxoLinkStateLinkState_Type.__name__ = "Integer32"
_FxoLinkStateLinkState_Object = MibTableColumn
fxoLinkStateLinkState = _FxoLinkStateLinkState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 10100, 100, 1, 200),
    _FxoLinkStateLinkState_Type()
)
fxoLinkStateLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxoLinkStateLinkState.setStatus("current")


class _FxoLinkStateVerification_Type(MxEnableState):
    """Custom type fxoLinkStateVerification based on MxEnableState"""
    defaultValue = 1


_FxoLinkStateVerification_Type.__name__ = "MxEnableState"
_FxoLinkStateVerification_Object = MibScalar
fxoLinkStateVerification = _FxoLinkStateVerification_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 10100, 200),
    _FxoLinkStateVerification_Type()
)
fxoLinkStateVerification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoLinkStateVerification.setStatus("current")


class _FxoLinkStateVerificationTimeout_Type(Unsigned32):
    """Custom type fxoLinkStateVerificationTimeout based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 10000),
    )


_FxoLinkStateVerificationTimeout_Type.__name__ = "Unsigned32"
_FxoLinkStateVerificationTimeout_Object = MibScalar
fxoLinkStateVerificationTimeout = _FxoLinkStateVerificationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 10100, 300),
    _FxoLinkStateVerificationTimeout_Type()
)
fxoLinkStateVerificationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoLinkStateVerificationTimeout.setStatus("current")
_FxoForceEndOfCallGroup_ObjectIdentity = ObjectIdentity
fxoForceEndOfCallGroup = _FxoForceEndOfCallGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 10200)
)


class _FxoFeocOnCallFailureEnable_Type(MxEnableState):
    """Custom type fxoFeocOnCallFailureEnable based on MxEnableState"""
    defaultValue = 1


_FxoFeocOnCallFailureEnable_Type.__name__ = "MxEnableState"
_FxoFeocOnCallFailureEnable_Object = MibScalar
fxoFeocOnCallFailureEnable = _FxoFeocOnCallFailureEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 10200, 100),
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 10200, 200),
    _FxoFeocOnCallFailureTimeout_Type()
)
fxoFeocOnCallFailureTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoFeocOnCallFailureTimeout.setStatus("current")


class _FxoFeocOnSilenceDetectionMode_Type(Integer32):
    """Custom type fxoFeocOnSilenceDetectionMode based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              400)
        )
    )
    namedValues = NamedValues(
        *(("disable", 100),
          ("inbountAndOutboundSilent", 400))
    )


_FxoFeocOnSilenceDetectionMode_Type.__name__ = "Integer32"
_FxoFeocOnSilenceDetectionMode_Object = MibScalar
fxoFeocOnSilenceDetectionMode = _FxoFeocOnSilenceDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 10200, 300),
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 10200, 400),
    _FxoFeocOnSilenceDetectionTimeout_Type()
)
fxoFeocOnSilenceDetectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoFeocOnSilenceDetectionTimeout.setStatus("current")


class _FxoFeocOnToneDetectionMode_Type(Integer32):
    """Custom type fxoFeocOnToneDetectionMode based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("disable", 100),
          ("countryTone", 200),
          ("customTone", 300))
    )


_FxoFeocOnToneDetectionMode_Type.__name__ = "Integer32"
_FxoFeocOnToneDetectionMode_Object = MibScalar
fxoFeocOnToneDetectionMode = _FxoFeocOnToneDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 10200, 500),
    _FxoFeocOnToneDetectionMode_Type()
)
fxoFeocOnToneDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoFeocOnToneDetectionMode.setStatus("current")
_FxoForceEndOfCallToneCustomSettingsGroup_ObjectIdentity = ObjectIdentity
fxoForceEndOfCallToneCustomSettingsGroup = _FxoForceEndOfCallToneCustomSettingsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 10200, 10000)
)


class _FxoFeocToneCustomFrequency_Type(Unsigned32):
    """Custom type fxoFeocToneCustomFrequency based on Unsigned32"""
    defaultValue = 440

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(350, 620),
    )


_FxoFeocToneCustomFrequency_Type.__name__ = "Unsigned32"
_FxoFeocToneCustomFrequency_Object = MibScalar
fxoFeocToneCustomFrequency = _FxoFeocToneCustomFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 10200, 10000, 100),
    _FxoFeocToneCustomFrequency_Type()
)
fxoFeocToneCustomFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoFeocToneCustomFrequency.setStatus("current")


class _FxoFeocToneCustomCadence_Type(OctetString):
    """Custom type fxoFeocToneCustomCadence based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FxoFeocToneCustomCadence_Type.__name__ = "OctetString"
_FxoFeocToneCustomCadence_Object = MibScalar
fxoFeocToneCustomCadence = _FxoFeocToneCustomCadence_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 10200, 10000, 200),
    _FxoFeocToneCustomCadence_Type()
)
fxoFeocToneCustomCadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoFeocToneCustomCadence.setStatus("current")


class _FxoFeocToneCustomRepetition_Type(Unsigned32):
    """Custom type fxoFeocToneCustomRepetition based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_FxoFeocToneCustomRepetition_Type.__name__ = "Unsigned32"
_FxoFeocToneCustomRepetition_Object = MibScalar
fxoFeocToneCustomRepetition = _FxoFeocToneCustomRepetition_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 20000, 10200, 10000, 300),
    _FxoFeocToneCustomRepetition_Type()
)
fxoFeocToneCustomRepetition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoFeocToneCustomRepetition.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 60010)
)


class _MinSeverity_Type(Integer32):
    """Custom type minSeverity based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("debug", 100),
          ("info", 200),
          ("warning", 300),
          ("error", 400),
          ("critical", 500))
    )


_MinSeverity_Type.__name__ = "Integer32"
_MinSeverity_Object = MibScalar
minSeverity = _MinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 60020)
)


class _NeedRestartInfo_Type(Integer32):
    """Custom type needRestartInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 100))
    )


_NeedRestartInfo_Type.__name__ = "Integer32"
_NeedRestartInfo_Object = MibScalar
needRestartInfo = _NeedRestartInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1800, 1, 60020, 100),
    _NeedRestartInfo_Type()
)
needRestartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    needRestartInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-POTS-MIB",
    **{"potsMIB": potsMIB,
       "potsMIBObjects": potsMIBObjects,
       "lineTable": lineTable,
       "lineEntry": lineEntry,
       "lineId": lineId,
       "lineTypeStatus": lineTypeStatus,
       "lineState": lineState,
       "callerIdCustomization": callerIdCustomization,
       "dtmfMapDigitDetection": dtmfMapDigitDetection,
       "vocalUnitInformation": vocalUnitInformation,
       "callerIdTransmission": callerIdTransmission,
       "fxsGroup": fxsGroup,
       "fxsLineSupervisionMode": fxsLineSupervisionMode,
       "fxsDisconnectDelay": fxsDisconnectDelay,
       "fxsInbandRingback": fxsInbandRingback,
       "fxsShutdownBehavior": fxsShutdownBehavior,
       "fxsPowerDropOnDisconnectDuration": fxsPowerDropOnDisconnectDuration,
       "fxsServiceActivation": fxsServiceActivation,
       "fxsCallerIdPrivateCallingPartyName": fxsCallerIdPrivateCallingPartyName,
       "fxsSipMessageAlertingEnable": fxsSipMessageAlertingEnable,
       "fxsCountryCustomizationGroup": fxsCountryCustomizationGroup,
       "fxsCountryCustomizationOverride": fxsCountryCustomizationOverride,
       "fxsCountryCustomizationLoopCurrent": fxsCountryCustomizationLoopCurrent,
       "fxsCountryCustomizationFlashHookDetectionRange": fxsCountryCustomizationFlashHookDetectionRange,
       "fxsBypassGroup": fxsBypassGroup,
       "fxsBypassTable": fxsBypassTable,
       "fxsBypassEntry": fxsBypassEntry,
       "fxsBypassId": fxsBypassId,
       "fxsBypassActivation": fxsBypassActivation,
       "fxsBypassActivationDtmfMap": fxsBypassActivationDtmfMap,
       "fxsBypassDeactivationTimeout": fxsBypassDeactivationTimeout,
       "fxsMessageWaitingIndicatorGroup": fxsMessageWaitingIndicatorGroup,
       "fxsDefaultMessageWaitingIndicatorActivation": fxsDefaultMessageWaitingIndicatorActivation,
       "fxsDefaultVisualMessageWaitingIndicatorType": fxsDefaultVisualMessageWaitingIndicatorType,
       "fxsSpecificMessageWaitingIndicatorTable": fxsSpecificMessageWaitingIndicatorTable,
       "fxsSpecificMessageWaitingIndicatorEntry": fxsSpecificMessageWaitingIndicatorEntry,
       "fxsSpecificMessageWaitingIndicatorId": fxsSpecificMessageWaitingIndicatorId,
       "fxsSpecificMessageWaitingIndicatorEnableConfig": fxsSpecificMessageWaitingIndicatorEnableConfig,
       "fxsSpecificMessageWaitingIndicatorActivation": fxsSpecificMessageWaitingIndicatorActivation,
       "fxsCallGroup": fxsCallGroup,
       "fxsDefaultAutoCancelTimeout": fxsDefaultAutoCancelTimeout,
       "fxsEmergencyCallGroup": fxsEmergencyCallGroup,
       "fxsEmergencyCallOverride": fxsEmergencyCallOverride,
       "fxsEmergencyRingTimeout": fxsEmergencyRingTimeout,
       "fxsRingGroup": fxsRingGroup,
       "fxsDistinctiveRingTable": fxsDistinctiveRingTable,
       "fxsDistinctiveRingEntry": fxsDistinctiveRingEntry,
       "fxsDistinctiveRingIndex": fxsDistinctiveRingIndex,
       "fxsDistinctiveRingRingId": fxsDistinctiveRingRingId,
       "fxsDistinctiveRingPattern": fxsDistinctiveRingPattern,
       "fxsCallerIdGroup": fxsCallerIdGroup,
       "fxsCallerIdTable": fxsCallerIdTable,
       "fxsCallerIdEntry": fxsCallerIdEntry,
       "fxsCallerIdId": fxsCallerIdId,
       "fxsCallerIdActivation": fxsCallerIdActivation,
       "fxsInteropGroup": fxsInteropGroup,
       "fxsInteropPlayLocalRingbackWhenNoMediaStream": fxsInteropPlayLocalRingbackWhenNoMediaStream,
       "fxoGroup": fxoGroup,
       "fxoPreDialDelay": fxoPreDialDelay,
       "fxoDialToneDetectionMode": fxoDialToneDetectionMode,
       "fxoDialToneDetectionTimeout": fxoDialToneDetectionTimeout,
       "fxoAnsweringDelayTable": fxoAnsweringDelayTable,
       "fxoAnsweringDelayEntry": fxoAnsweringDelayEntry,
       "fxoAnsweringDelayId": fxoAnsweringDelayId,
       "fxoAnsweringDelayWaitBeforeAnsweringDelay": fxoAnsweringDelayWaitBeforeAnsweringDelay,
       "fxoAnsweringDelayAnsweringOnCallerIdDetection": fxoAnsweringDelayAnsweringOnCallerIdDetection,
       "fxoAnsweringDelayWaitForCalleeToAnswer": fxoAnsweringDelayWaitForCalleeToAnswer,
       "fxoIncomingCallBehaviorTable": fxoIncomingCallBehaviorTable,
       "fxoIncomingCallBehaviorEntry": fxoIncomingCallBehaviorEntry,
       "fxoIncomingCallBehaviorId": fxoIncomingCallBehaviorId,
       "fxoIncomingCallBehaviorNotAllowedBehavior": fxoIncomingCallBehaviorNotAllowedBehavior,
       "fxoCustomBasicParametersTable": fxoCustomBasicParametersTable,
       "fxoCustomBasicParametersEntry": fxoCustomBasicParametersEntry,
       "fxoCustomBasicParametersId": fxoCustomBasicParametersId,
       "fxoCustomBasicParametersOverrideDefaultCountryParameters": fxoCustomBasicParametersOverrideDefaultCountryParameters,
       "fxoCustomBasicParametersImpedance": fxoCustomBasicParametersImpedance,
       "fxoCustomBasicParametersDigitalHybrid": fxoCustomBasicParametersDigitalHybrid,
       "fxoCustomBasicParametersReset": fxoCustomBasicParametersReset,
       "fxoLinkStateVerificationGroup": fxoLinkStateVerificationGroup,
       "fxoLinkStateTable": fxoLinkStateTable,
       "fxoLinkStateEntry": fxoLinkStateEntry,
       "fxoLinkStateId": fxoLinkStateId,
       "fxoLinkStateLinkState": fxoLinkStateLinkState,
       "fxoLinkStateVerification": fxoLinkStateVerification,
       "fxoLinkStateVerificationTimeout": fxoLinkStateVerificationTimeout,
       "fxoForceEndOfCallGroup": fxoForceEndOfCallGroup,
       "fxoFeocOnCallFailureEnable": fxoFeocOnCallFailureEnable,
       "fxoFeocOnCallFailureTimeout": fxoFeocOnCallFailureTimeout,
       "fxoFeocOnSilenceDetectionMode": fxoFeocOnSilenceDetectionMode,
       "fxoFeocOnSilenceDetectionTimeout": fxoFeocOnSilenceDetectionTimeout,
       "fxoFeocOnToneDetectionMode": fxoFeocOnToneDetectionMode,
       "fxoForceEndOfCallToneCustomSettingsGroup": fxoForceEndOfCallToneCustomSettingsGroup,
       "fxoFeocToneCustomFrequency": fxoFeocToneCustomFrequency,
       "fxoFeocToneCustomCadence": fxoFeocToneCustomCadence,
       "fxoFeocToneCustomRepetition": fxoFeocToneCustomRepetition,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
