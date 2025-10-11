# SNMP MIB module (MX-FXS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-FXS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:47 2025
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

(mediatrixConfig,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixConfig")

(MxDigitMap,
 MxEnableState) = mibBuilder.importSymbols(
    "MX-TC",
    "MxDigitMap",
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

fxsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40)
)
if mibBuilder.loadTexts:
    fxsMIB.setRevisions(
        ("2009-08-05 00:00",
         "2009-07-24 00:00",
         "2009-01-26 00:00",
         "2008-11-27 00:00",
         "2007-05-18 00:00",
         "2006-12-21 00:00",
         "2006-02-13 00:00",
         "2006-01-30 00:00",
         "2005-11-07 00:00",
         "2005-03-30 00:00",
         "2005-01-27 00:00",
         "2004-11-24 00:00",
         "2004-09-27 00:00",
         "2002-08-30 00:00",
         "2002-08-22 00:00",
         "2001-11-05 00:00",
         "2001-08-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FxsMIBObjects_ObjectIdentity = ObjectIdentity
fxsMIBObjects = _FxsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1)
)


class _FxsByPassEnable_Type(Integer32):
    """Custom type fxsByPassEnable based on Integer32"""
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


_FxsByPassEnable_Type.__name__ = "Integer32"
_FxsByPassEnable_Object = MibScalar
fxsByPassEnable = _FxsByPassEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 1),
    _FxsByPassEnable_Type()
)
fxsByPassEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsByPassEnable.setStatus("current")


class _FxsLoopCurrent_Type(Unsigned32):
    """Custom type fxsLoopCurrent based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 50),
    )


_FxsLoopCurrent_Type.__name__ = "Unsigned32"
_FxsLoopCurrent_Object = MibScalar
fxsLoopCurrent = _FxsLoopCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 2),
    _FxsLoopCurrent_Type()
)
fxsLoopCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsLoopCurrent.setStatus("current")


class _FxsFlashHookDetectionDelayMin_Type(Unsigned32):
    """Custom type fxsFlashHookDetectionDelayMin based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1200),
    )


_FxsFlashHookDetectionDelayMin_Type.__name__ = "Unsigned32"
_FxsFlashHookDetectionDelayMin_Object = MibScalar
fxsFlashHookDetectionDelayMin = _FxsFlashHookDetectionDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 3),
    _FxsFlashHookDetectionDelayMin_Type()
)
fxsFlashHookDetectionDelayMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsFlashHookDetectionDelayMin.setStatus("current")


class _FxsFlashHookDetectionDelayMax_Type(Unsigned32):
    """Custom type fxsFlashHookDetectionDelayMax based on Unsigned32"""
    defaultValue = 1200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1200),
    )


_FxsFlashHookDetectionDelayMax_Type.__name__ = "Unsigned32"
_FxsFlashHookDetectionDelayMax_Object = MibScalar
fxsFlashHookDetectionDelayMax = _FxsFlashHookDetectionDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 4),
    _FxsFlashHookDetectionDelayMax_Type()
)
fxsFlashHookDetectionDelayMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsFlashHookDetectionDelayMax.setStatus("current")


class _FxsLoopCurrentDropEnable_Type(MxEnableState):
    """Custom type fxsLoopCurrentDropEnable based on MxEnableState"""
    defaultValue = 0


_FxsLoopCurrentDropEnable_Type.__name__ = "MxEnableState"
_FxsLoopCurrentDropEnable_Object = MibScalar
fxsLoopCurrentDropEnable = _FxsLoopCurrentDropEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 50),
    _FxsLoopCurrentDropEnable_Type()
)
fxsLoopCurrentDropEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsLoopCurrentDropEnable.setStatus("current")


class _FxsCalleeHangupSupervision_Type(MxEnableState):
    """Custom type fxsCalleeHangupSupervision based on MxEnableState"""
    defaultValue = 0


_FxsCalleeHangupSupervision_Type.__name__ = "MxEnableState"
_FxsCalleeHangupSupervision_Object = MibScalar
fxsCalleeHangupSupervision = _FxsCalleeHangupSupervision_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 75),
    _FxsCalleeHangupSupervision_Type()
)
fxsCalleeHangupSupervision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsCalleeHangupSupervision.setStatus("current")


class _FxsCalleeHangupDelay_Type(Unsigned32):
    """Custom type fxsCalleeHangupDelay based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_FxsCalleeHangupDelay_Type.__name__ = "Unsigned32"
_FxsCalleeHangupDelay_Object = MibScalar
fxsCalleeHangupDelay = _FxsCalleeHangupDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 100),
    _FxsCalleeHangupDelay_Type()
)
fxsCalleeHangupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsCalleeHangupDelay.setStatus("current")


class _FxsReversalOnIdleEnable_Type(MxEnableState):
    """Custom type fxsReversalOnIdleEnable based on MxEnableState"""
    defaultValue = 0


_FxsReversalOnIdleEnable_Type.__name__ = "MxEnableState"
_FxsReversalOnIdleEnable_Object = MibScalar
fxsReversalOnIdleEnable = _FxsReversalOnIdleEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 125),
    _FxsReversalOnIdleEnable_Type()
)
fxsReversalOnIdleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsReversalOnIdleEnable.setStatus("deprecated")


class _FxsPolarityAndDenialBehavior_Type(Integer32):
    """Custom type fxsPolarityAndDenialBehavior based on Integer32"""
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
        *(("noReversal", 0),
          ("reversalOnIdle", 1),
          ("reversalOnEstablished", 2))
    )


_FxsPolarityAndDenialBehavior_Type.__name__ = "Integer32"
_FxsPolarityAndDenialBehavior_Object = MibScalar
fxsPolarityAndDenialBehavior = _FxsPolarityAndDenialBehavior_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 135),
    _FxsPolarityAndDenialBehavior_Type()
)
fxsPolarityAndDenialBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPolarityAndDenialBehavior.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 140),
    _FxsPowerDropOnDisconnectDuration_Type()
)
fxsPowerDropOnDisconnectDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPowerDropOnDisconnectDuration.setStatus("current")


class _FxsBlankAnonymousCallerId_Type(MxEnableState):
    """Custom type fxsBlankAnonymousCallerId based on MxEnableState"""
    defaultValue = 0


_FxsBlankAnonymousCallerId_Type.__name__ = "MxEnableState"
_FxsBlankAnonymousCallerId_Object = MibScalar
fxsBlankAnonymousCallerId = _FxsBlankAnonymousCallerId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 150),
    _FxsBlankAnonymousCallerId_Type()
)
fxsBlankAnonymousCallerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsBlankAnonymousCallerId.setStatus("current")


class _FxsFskMarkoutBits_Type(Unsigned32):
    """Custom type fxsFskMarkoutBits based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5280),
    )


_FxsFskMarkoutBits_Type.__name__ = "Unsigned32"
_FxsFskMarkoutBits_Object = MibScalar
fxsFskMarkoutBits = _FxsFskMarkoutBits_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 155),
    _FxsFskMarkoutBits_Type()
)
fxsFskMarkoutBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsFskMarkoutBits.setStatus("current")


class _FxsCallingNumberCriteria_Type(OctetString):
    """Custom type fxsCallingNumberCriteria based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FxsCallingNumberCriteria_Type.__name__ = "OctetString"
_FxsCallingNumberCriteria_Object = MibScalar
fxsCallingNumberCriteria = _FxsCallingNumberCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 160),
    _FxsCallingNumberCriteria_Type()
)
fxsCallingNumberCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsCallingNumberCriteria.setStatus("current")


class _FxsCallingNumberTransformation_Type(OctetString):
    """Custom type fxsCallingNumberTransformation based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FxsCallingNumberTransformation_Type.__name__ = "OctetString"
_FxsCallingNumberTransformation_Object = MibScalar
fxsCallingNumberTransformation = _FxsCallingNumberTransformation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 161),
    _FxsCallingNumberTransformation_Type()
)
fxsCallingNumberTransformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsCallingNumberTransformation.setStatus("current")
_FxsEpSpecificLoopCurrentTable_Object = MibTable
fxsEpSpecificLoopCurrentTable = _FxsEpSpecificLoopCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 190)
)
if mibBuilder.loadTexts:
    fxsEpSpecificLoopCurrentTable.setStatus("current")
_FxsEpSpecificLoopCurrentEntry_Object = MibTableRow
fxsEpSpecificLoopCurrentEntry = _FxsEpSpecificLoopCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 190, 1)
)
fxsEpSpecificLoopCurrentEntry.setIndexNames(
    (0, "MX-FXS-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fxsEpSpecificLoopCurrentEntry.setStatus("current")


class _FxsEpSpecificLoopCurrentOverrideEnable_Type(MxEnableState):
    """Custom type fxsEpSpecificLoopCurrentOverrideEnable based on MxEnableState"""
    defaultValue = 0


_FxsEpSpecificLoopCurrentOverrideEnable_Type.__name__ = "MxEnableState"
_FxsEpSpecificLoopCurrentOverrideEnable_Object = MibTableColumn
fxsEpSpecificLoopCurrentOverrideEnable = _FxsEpSpecificLoopCurrentOverrideEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 190, 1, 10),
    _FxsEpSpecificLoopCurrentOverrideEnable_Type()
)
fxsEpSpecificLoopCurrentOverrideEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsEpSpecificLoopCurrentOverrideEnable.setStatus("current")


class _FxsEpSpecificLoopCurrentOverride_Type(Unsigned32):
    """Custom type fxsEpSpecificLoopCurrentOverride based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 50),
    )


_FxsEpSpecificLoopCurrentOverride_Type.__name__ = "Unsigned32"
_FxsEpSpecificLoopCurrentOverride_Object = MibTableColumn
fxsEpSpecificLoopCurrentOverride = _FxsEpSpecificLoopCurrentOverride_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 190, 1, 20),
    _FxsEpSpecificLoopCurrentOverride_Type()
)
fxsEpSpecificLoopCurrentOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsEpSpecificLoopCurrentOverride.setStatus("current")
_FxsEmergencyBypass_ObjectIdentity = ObjectIdentity
fxsEmergencyBypass = _FxsEmergencyBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 200)
)


class _FxsEmergencyBypassEnable_Type(MxEnableState):
    """Custom type fxsEmergencyBypassEnable based on MxEnableState"""
    defaultValue = 0


_FxsEmergencyBypassEnable_Type.__name__ = "MxEnableState"
_FxsEmergencyBypassEnable_Object = MibScalar
fxsEmergencyBypassEnable = _FxsEmergencyBypassEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 200, 50),
    _FxsEmergencyBypassEnable_Type()
)
fxsEmergencyBypassEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsEmergencyBypassEnable.setStatus("current")


class _FxsEmergencyBypassTimeout_Type(Unsigned32):
    """Custom type fxsEmergencyBypassTimeout based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_FxsEmergencyBypassTimeout_Type.__name__ = "Unsigned32"
_FxsEmergencyBypassTimeout_Object = MibScalar
fxsEmergencyBypassTimeout = _FxsEmergencyBypassTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 200, 100),
    _FxsEmergencyBypassTimeout_Type()
)
fxsEmergencyBypassTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsEmergencyBypassTimeout.setStatus("current")


class _FxsEmergencyBypassDialMap_Type(MxDigitMap):
    """Custom type fxsEmergencyBypassDialMap based on MxDigitMap"""
    defaultValue = OctetString("")


_FxsEmergencyBypassDialMap_Type.__name__ = "MxDigitMap"
_FxsEmergencyBypassDialMap_Object = MibScalar
fxsEmergencyBypassDialMap = _FxsEmergencyBypassDialMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 200, 150),
    _FxsEmergencyBypassDialMap_Type()
)
fxsEmergencyBypassDialMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsEmergencyBypassDialMap.setStatus("current")


class _FxsEmergencyBypassDialDelay_Type(Unsigned32):
    """Custom type fxsEmergencyBypassDialDelay based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FxsEmergencyBypassDialDelay_Type.__name__ = "Unsigned32"
_FxsEmergencyBypassDialDelay_Object = MibScalar
fxsEmergencyBypassDialDelay = _FxsEmergencyBypassDialDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 1, 200, 200),
    _FxsEmergencyBypassDialDelay_Type()
)
fxsEmergencyBypassDialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsEmergencyBypassDialDelay.setStatus("current")
_FxsConformance_ObjectIdentity = ObjectIdentity
fxsConformance = _FxsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 2)
)
_FxsCompliances_ObjectIdentity = ObjectIdentity
fxsCompliances = _FxsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 2, 1)
)
_FxsGroups_ObjectIdentity = ObjectIdentity
fxsGroups = _FxsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 2, 5)
)

# Managed Objects groups

fxsGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 2, 5, 5)
)
fxsGroupVer1.setObjects(
      *(("MX-FXS-MIB", "fxsByPassEnable"),
        ("MX-FXS-MIB", "fxsLoopCurrent"),
        ("MX-FXS-MIB", "fxsFlashHookDetectionDelayMin"),
        ("MX-FXS-MIB", "fxsFlashHookDetectionDelayMax"),
        ("MX-FXS-MIB", "fxsLoopCurrentDropEnable"),
        ("MX-FXS-MIB", "fxsCalleeHangupSupervision"),
        ("MX-FXS-MIB", "fxsCalleeHangupDelay"),
        ("MX-FXS-MIB", "fxsReversalOnIdleEnable"),
        ("MX-FXS-MIB", "fxsPolarityAndDenialBehavior"),
        ("MX-FXS-MIB", "fxsPowerDropOnDisconnectDuration"),
        ("MX-FXS-MIB", "fxsBlankAnonymousCallerId"),
        ("MX-FXS-MIB", "fxsFskMarkoutBits"),
        ("MX-FXS-MIB", "fxsCallingNumberCriteria"),
        ("MX-FXS-MIB", "fxsCallingNumberTransformation"))
)
if mibBuilder.loadTexts:
    fxsGroupVer1.setStatus("current")

fxsEmergencyBypassGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 2, 5, 10)
)
fxsEmergencyBypassGroupVer1.setObjects(
      *(("MX-FXS-MIB", "fxsEmergencyBypassEnable"),
        ("MX-FXS-MIB", "fxsEmergencyBypassTimeout"),
        ("MX-FXS-MIB", "fxsEmergencyBypassDialMap"),
        ("MX-FXS-MIB", "fxsEmergencyBypassDialDelay"))
)
if mibBuilder.loadTexts:
    fxsEmergencyBypassGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fxsComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 40, 2, 1, 1)
)
fxsComplVer1.setObjects(
      *(("MX-FXS-MIB", "fxsGroupVer1"),
        ("MX-FXS-MIB", "fxsEmergencyBypassGroupVer1"))
)
if mibBuilder.loadTexts:
    fxsComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-FXS-MIB",
    **{"fxsMIB": fxsMIB,
       "fxsMIBObjects": fxsMIBObjects,
       "fxsByPassEnable": fxsByPassEnable,
       "fxsLoopCurrent": fxsLoopCurrent,
       "fxsFlashHookDetectionDelayMin": fxsFlashHookDetectionDelayMin,
       "fxsFlashHookDetectionDelayMax": fxsFlashHookDetectionDelayMax,
       "fxsLoopCurrentDropEnable": fxsLoopCurrentDropEnable,
       "fxsCalleeHangupSupervision": fxsCalleeHangupSupervision,
       "fxsCalleeHangupDelay": fxsCalleeHangupDelay,
       "fxsReversalOnIdleEnable": fxsReversalOnIdleEnable,
       "fxsPolarityAndDenialBehavior": fxsPolarityAndDenialBehavior,
       "fxsPowerDropOnDisconnectDuration": fxsPowerDropOnDisconnectDuration,
       "fxsBlankAnonymousCallerId": fxsBlankAnonymousCallerId,
       "fxsFskMarkoutBits": fxsFskMarkoutBits,
       "fxsCallingNumberCriteria": fxsCallingNumberCriteria,
       "fxsCallingNumberTransformation": fxsCallingNumberTransformation,
       "fxsEpSpecificLoopCurrentTable": fxsEpSpecificLoopCurrentTable,
       "fxsEpSpecificLoopCurrentEntry": fxsEpSpecificLoopCurrentEntry,
       "fxsEpSpecificLoopCurrentOverrideEnable": fxsEpSpecificLoopCurrentOverrideEnable,
       "fxsEpSpecificLoopCurrentOverride": fxsEpSpecificLoopCurrentOverride,
       "fxsEmergencyBypass": fxsEmergencyBypass,
       "fxsEmergencyBypassEnable": fxsEmergencyBypassEnable,
       "fxsEmergencyBypassTimeout": fxsEmergencyBypassTimeout,
       "fxsEmergencyBypassDialMap": fxsEmergencyBypassDialMap,
       "fxsEmergencyBypassDialDelay": fxsEmergencyBypassDialDelay,
       "fxsConformance": fxsConformance,
       "fxsCompliances": fxsCompliances,
       "fxsComplVer1": fxsComplVer1,
       "fxsGroups": fxsGroups,
       "fxsGroupVer1": fxsGroupVer1,
       "fxsEmergencyBypassGroupVer1": fxsEmergencyBypassGroupVer1}
)
