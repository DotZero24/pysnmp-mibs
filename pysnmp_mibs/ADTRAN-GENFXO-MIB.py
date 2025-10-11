# SNMP MIB module (ADTRAN-GENFXO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENFXO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:42 2025
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

(adGenFxo,
 adGenFxoID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenFxo",
    "adGenFxoID")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

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

adGenFxoIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 38, 1)
)
if mibBuilder.loadTexts:
    adGenFxoIdentity.setRevisions(
        ("2018-04-04 00:00",
         "2014-06-12 00:00",
         "2012-08-22 00:00",
         "2011-09-12 00:00",
         "2011-02-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdGenFxoInterfaceFxsLocation(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )



# MIB Managed Objects in the order of their OIDs

_AdGenFxoProvisioning_ObjectIdentity = ObjectIdentity
adGenFxoProvisioning = _AdGenFxoProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1)
)
_AdGenFxoDeviceProv_ObjectIdentity = ObjectIdentity
adGenFxoDeviceProv = _AdGenFxoDeviceProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 1)
)
_AdGenFxoInterfaceProv_ObjectIdentity = ObjectIdentity
adGenFxoInterfaceProv = _AdGenFxoInterfaceProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2)
)
_AdGenFxoInterfaceProvTable_Object = MibTable
adGenFxoInterfaceProvTable = _AdGenFxoInterfaceProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adGenFxoInterfaceProvTable.setStatus("current")
_AdGenFxoInterfaceProvEntry_Object = MibTableRow
adGenFxoInterfaceProvEntry = _AdGenFxoInterfaceProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2, 1, 1)
)
adGenFxoInterfaceProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenFxoInterfaceProvEntry.setStatus("current")
_AdGenFxoInterfaceLastErrorString_Type = DisplayString
_AdGenFxoInterfaceLastErrorString_Object = MibTableColumn
adGenFxoInterfaceLastErrorString = _AdGenFxoInterfaceLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2, 1, 1, 1),
    _AdGenFxoInterfaceLastErrorString_Type()
)
adGenFxoInterfaceLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFxoInterfaceLastErrorString.setStatus("current")


class _AdGenFxoInterfaceSignalingMode_Type(Integer32):
    """Custom type adGenFxoInterfaceSignalingMode based on Integer32"""
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
        *(("loopStart", 1),
          ("groundStart", 2),
          ("tr08sp", 3),
          ("tr08uvg", 4))
    )


_AdGenFxoInterfaceSignalingMode_Type.__name__ = "Integer32"
_AdGenFxoInterfaceSignalingMode_Object = MibTableColumn
adGenFxoInterfaceSignalingMode = _AdGenFxoInterfaceSignalingMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2, 1, 1, 2),
    _AdGenFxoInterfaceSignalingMode_Type()
)
adGenFxoInterfaceSignalingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenFxoInterfaceSignalingMode.setStatus("current")
_AdGenFxoInterfaceTxGain_Type = Integer32
_AdGenFxoInterfaceTxGain_Object = MibTableColumn
adGenFxoInterfaceTxGain = _AdGenFxoInterfaceTxGain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2, 1, 1, 3),
    _AdGenFxoInterfaceTxGain_Type()
)
adGenFxoInterfaceTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenFxoInterfaceTxGain.setStatus("current")
if mibBuilder.loadTexts:
    adGenFxoInterfaceTxGain.setUnits("0.1dB")
_AdGenFxoInterfaceMinTxGain_Type = Integer32
_AdGenFxoInterfaceMinTxGain_Object = MibTableColumn
adGenFxoInterfaceMinTxGain = _AdGenFxoInterfaceMinTxGain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2, 1, 1, 4),
    _AdGenFxoInterfaceMinTxGain_Type()
)
adGenFxoInterfaceMinTxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFxoInterfaceMinTxGain.setStatus("current")
if mibBuilder.loadTexts:
    adGenFxoInterfaceMinTxGain.setUnits("0.1dB")
_AdGenFxoInterfaceMaxTxGain_Type = Integer32
_AdGenFxoInterfaceMaxTxGain_Object = MibTableColumn
adGenFxoInterfaceMaxTxGain = _AdGenFxoInterfaceMaxTxGain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2, 1, 1, 5),
    _AdGenFxoInterfaceMaxTxGain_Type()
)
adGenFxoInterfaceMaxTxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFxoInterfaceMaxTxGain.setStatus("current")
if mibBuilder.loadTexts:
    adGenFxoInterfaceMaxTxGain.setUnits("0.1dB")
_AdGenFxoInterfaceRxGain_Type = Integer32
_AdGenFxoInterfaceRxGain_Object = MibTableColumn
adGenFxoInterfaceRxGain = _AdGenFxoInterfaceRxGain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2, 1, 1, 6),
    _AdGenFxoInterfaceRxGain_Type()
)
adGenFxoInterfaceRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenFxoInterfaceRxGain.setStatus("current")
if mibBuilder.loadTexts:
    adGenFxoInterfaceRxGain.setUnits("0.1dB")
_AdGenFxoInterfaceMinRxGain_Type = Integer32
_AdGenFxoInterfaceMinRxGain_Object = MibTableColumn
adGenFxoInterfaceMinRxGain = _AdGenFxoInterfaceMinRxGain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2, 1, 1, 7),
    _AdGenFxoInterfaceMinRxGain_Type()
)
adGenFxoInterfaceMinRxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFxoInterfaceMinRxGain.setStatus("current")
if mibBuilder.loadTexts:
    adGenFxoInterfaceMinRxGain.setUnits("0.1dB")
_AdGenFxoInterfaceMaxRxGain_Type = Integer32
_AdGenFxoInterfaceMaxRxGain_Object = MibTableColumn
adGenFxoInterfaceMaxRxGain = _AdGenFxoInterfaceMaxRxGain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2, 1, 1, 8),
    _AdGenFxoInterfaceMaxRxGain_Type()
)
adGenFxoInterfaceMaxRxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFxoInterfaceMaxRxGain.setStatus("current")
if mibBuilder.loadTexts:
    adGenFxoInterfaceMaxRxGain.setUnits("0.1dB")


class _AdGenFxoInterfaceImpedance_Type(Integer32):
    """Custom type adGenFxoInterfaceImpedance based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("z600r", 1),
          ("z900z", 2),
          ("z1", 3),
          ("z2", 4),
          ("z3", 5),
          ("z4", 6),
          ("z5", 7),
          ("z6", 8),
          ("z7", 9),
          ("z8", 10),
          ("z9", 11),
          ("z10", 12))
    )


_AdGenFxoInterfaceImpedance_Type.__name__ = "Integer32"
_AdGenFxoInterfaceImpedance_Object = MibTableColumn
adGenFxoInterfaceImpedance = _AdGenFxoInterfaceImpedance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2, 1, 1, 9),
    _AdGenFxoInterfaceImpedance_Type()
)
adGenFxoInterfaceImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenFxoInterfaceImpedance.setStatus("current")


class _AdGenFxoInterfaceCWCIdAckGenDelay_Type(Unsigned32):
    """Custom type adGenFxoInterfaceCWCIdAckGenDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenFxoInterfaceCWCIdAckGenDelay_Type.__name__ = "Unsigned32"
_AdGenFxoInterfaceCWCIdAckGenDelay_Object = MibTableColumn
adGenFxoInterfaceCWCIdAckGenDelay = _AdGenFxoInterfaceCWCIdAckGenDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2, 1, 1, 10),
    _AdGenFxoInterfaceCWCIdAckGenDelay_Type()
)
adGenFxoInterfaceCWCIdAckGenDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenFxoInterfaceCWCIdAckGenDelay.setStatus("current")


class _AdGenFxoInterfaceCWCIdAckGenEnable_Type(Integer32):
    """Custom type adGenFxoInterfaceCWCIdAckGenEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdGenFxoInterfaceCWCIdAckGenEnable_Type.__name__ = "Integer32"
_AdGenFxoInterfaceCWCIdAckGenEnable_Object = MibTableColumn
adGenFxoInterfaceCWCIdAckGenEnable = _AdGenFxoInterfaceCWCIdAckGenEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2, 1, 1, 11),
    _AdGenFxoInterfaceCWCIdAckGenEnable_Type()
)
adGenFxoInterfaceCWCIdAckGenEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenFxoInterfaceCWCIdAckGenEnable.setStatus("current")
_AdGenFxoInterfaceTargetFxsLocation_Type = AdGenFxoInterfaceFxsLocation
_AdGenFxoInterfaceTargetFxsLocation_Object = MibTableColumn
adGenFxoInterfaceTargetFxsLocation = _AdGenFxoInterfaceTargetFxsLocation_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2, 1, 1, 12),
    _AdGenFxoInterfaceTargetFxsLocation_Type()
)
adGenFxoInterfaceTargetFxsLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenFxoInterfaceTargetFxsLocation.setStatus("current")


class _AdGenFxoInterfaceRingTripMode_Type(Integer32):
    """Custom type adGenFxoInterfaceRingTripMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("forced", 2),
          ("delayed", 3))
    )


_AdGenFxoInterfaceRingTripMode_Type.__name__ = "Integer32"
_AdGenFxoInterfaceRingTripMode_Object = MibTableColumn
adGenFxoInterfaceRingTripMode = _AdGenFxoInterfaceRingTripMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2, 1, 1, 13),
    _AdGenFxoInterfaceRingTripMode_Type()
)
adGenFxoInterfaceRingTripMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenFxoInterfaceRingTripMode.setStatus("current")


class _AdGenFxoInterfaceRingTripDuration_Type(Unsigned32):
    """Custom type adGenFxoInterfaceRingTripDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 300),
    )


_AdGenFxoInterfaceRingTripDuration_Type.__name__ = "Unsigned32"
_AdGenFxoInterfaceRingTripDuration_Object = MibTableColumn
adGenFxoInterfaceRingTripDuration = _AdGenFxoInterfaceRingTripDuration_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2, 1, 1, 14),
    _AdGenFxoInterfaceRingTripDuration_Type()
)
adGenFxoInterfaceRingTripDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenFxoInterfaceRingTripDuration.setStatus("current")
if mibBuilder.loadTexts:
    adGenFxoInterfaceRingTripDuration.setUnits("milliseconds")


class _AdGenFxoInterfaceRingTripMuteInterval_Type(Unsigned32):
    """Custom type adGenFxoInterfaceRingTripMuteInterval based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )


_AdGenFxoInterfaceRingTripMuteInterval_Type.__name__ = "Unsigned32"
_AdGenFxoInterfaceRingTripMuteInterval_Object = MibTableColumn
adGenFxoInterfaceRingTripMuteInterval = _AdGenFxoInterfaceRingTripMuteInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2, 1, 1, 15),
    _AdGenFxoInterfaceRingTripMuteInterval_Type()
)
adGenFxoInterfaceRingTripMuteInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenFxoInterfaceRingTripMuteInterval.setStatus("current")
if mibBuilder.loadTexts:
    adGenFxoInterfaceRingTripMuteInterval.setUnits("milliseconds")


class _AdGenFxoCircuitIdentifier_Type(DisplayString):
    """Custom type adGenFxoCircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdGenFxoCircuitIdentifier_Type.__name__ = "DisplayString"
_AdGenFxoCircuitIdentifier_Object = MibTableColumn
adGenFxoCircuitIdentifier = _AdGenFxoCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 1, 2, 1, 1, 16),
    _AdGenFxoCircuitIdentifier_Type()
)
adGenFxoCircuitIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenFxoCircuitIdentifier.setStatus("current")
_AdGenFxoStatus_ObjectIdentity = ObjectIdentity
adGenFxoStatus = _AdGenFxoStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2)
)
_AdGenFxoDeviceStatus_ObjectIdentity = ObjectIdentity
adGenFxoDeviceStatus = _AdGenFxoDeviceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2, 1)
)
_AdGenFxoInterfaceStatus_ObjectIdentity = ObjectIdentity
adGenFxoInterfaceStatus = _AdGenFxoInterfaceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2, 2)
)
_AdGenFxoInterfaceStatusTable_Object = MibTable
adGenFxoInterfaceStatusTable = _AdGenFxoInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2, 2, 1)
)
if mibBuilder.loadTexts:
    adGenFxoInterfaceStatusTable.setStatus("current")
_AdGenFxoInterfaceStatusEntry_Object = MibTableRow
adGenFxoInterfaceStatusEntry = _AdGenFxoInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2, 2, 1, 1)
)
adGenFxoInterfaceStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenFxoInterfaceStatusEntry.setStatus("current")


class _AdGenFxoPortActive_Type(Integer32):
    """Custom type adGenFxoPortActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("disabled", 3))
    )


_AdGenFxoPortActive_Type.__name__ = "Integer32"
_AdGenFxoPortActive_Object = MibTableColumn
adGenFxoPortActive = _AdGenFxoPortActive_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2, 2, 1, 1, 1),
    _AdGenFxoPortActive_Type()
)
adGenFxoPortActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFxoPortActive.setStatus("current")


class _AdGenFxoLoopFeed_Type(Integer32):
    """Custom type adGenFxoLoopFeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("ringGround", 3))
    )


_AdGenFxoLoopFeed_Type.__name__ = "Integer32"
_AdGenFxoLoopFeed_Object = MibTableColumn
adGenFxoLoopFeed = _AdGenFxoLoopFeed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2, 2, 1, 1, 2),
    _AdGenFxoLoopFeed_Type()
)
adGenFxoLoopFeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFxoLoopFeed.setStatus("current")


class _AdGenFxoLoopState_Type(Integer32):
    """Custom type adGenFxoLoopState based on Integer32"""
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
        *(("lcf", 1),
          ("rlcf", 2),
          ("noBatt", 3),
          ("tipOpen", 4),
          ("ringing", 5))
    )


_AdGenFxoLoopState_Type.__name__ = "Integer32"
_AdGenFxoLoopState_Object = MibTableColumn
adGenFxoLoopState = _AdGenFxoLoopState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2, 2, 1, 1, 3),
    _AdGenFxoLoopState_Type()
)
adGenFxoLoopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFxoLoopState.setStatus("current")


class _AdGenFxoTestActive_Type(Integer32):
    """Custom type adGenFxoTestActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("disabled", 3))
    )


_AdGenFxoTestActive_Type.__name__ = "Integer32"
_AdGenFxoTestActive_Object = MibTableColumn
adGenFxoTestActive = _AdGenFxoTestActive_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2, 2, 1, 1, 4),
    _AdGenFxoTestActive_Type()
)
adGenFxoTestActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFxoTestActive.setStatus("current")
_AdGenFxoRxVoicePackets_Type = Unsigned32
_AdGenFxoRxVoicePackets_Object = MibTableColumn
adGenFxoRxVoicePackets = _AdGenFxoRxVoicePackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2, 2, 1, 1, 5),
    _AdGenFxoRxVoicePackets_Type()
)
adGenFxoRxVoicePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFxoRxVoicePackets.setStatus("current")
_AdGenFxoRxControlPackets_Type = Unsigned32
_AdGenFxoRxControlPackets_Object = MibTableColumn
adGenFxoRxControlPackets = _AdGenFxoRxControlPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2, 2, 1, 1, 6),
    _AdGenFxoRxControlPackets_Type()
)
adGenFxoRxControlPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFxoRxControlPackets.setStatus("current")
_AdGenFxoTxVoicePackets_Type = Unsigned32
_AdGenFxoTxVoicePackets_Object = MibTableColumn
adGenFxoTxVoicePackets = _AdGenFxoTxVoicePackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2, 2, 1, 1, 7),
    _AdGenFxoTxVoicePackets_Type()
)
adGenFxoTxVoicePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFxoTxVoicePackets.setStatus("current")
_AdGenFxoTxControlPackets_Type = Unsigned32
_AdGenFxoTxControlPackets_Object = MibTableColumn
adGenFxoTxControlPackets = _AdGenFxoTxControlPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2, 2, 1, 1, 8),
    _AdGenFxoTxControlPackets_Type()
)
adGenFxoTxControlPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFxoTxControlPackets.setStatus("current")


class _AdGenFxoClearPortCounters_Type(Integer32):
    """Custom type adGenFxoClearPortCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AdGenFxoClearPortCounters_Type.__name__ = "Integer32"
_AdGenFxoClearPortCounters_Object = MibTableColumn
adGenFxoClearPortCounters = _AdGenFxoClearPortCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2, 2, 1, 1, 9),
    _AdGenFxoClearPortCounters_Type()
)
adGenFxoClearPortCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenFxoClearPortCounters.setStatus("current")
_AdGenFxoFindFxsMap_ObjectIdentity = ObjectIdentity
adGenFxoFindFxsMap = _AdGenFxoFindFxsMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2, 3)
)
_AdGenFxoFindFxsMapTable_Object = MibTable
adGenFxoFindFxsMapTable = _AdGenFxoFindFxsMapTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2, 3, 1)
)
if mibBuilder.loadTexts:
    adGenFxoFindFxsMapTable.setStatus("current")
_AdGenFxoFindFxsMapEntry_Object = MibTableRow
adGenFxoFindFxsMapEntry = _AdGenFxoFindFxsMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2, 3, 1, 1)
)
adGenFxoFindFxsMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (1, "ADTRAN-GENFXO-MIB", "adGenFxoInterfaceFxsIndex"),
)
if mibBuilder.loadTexts:
    adGenFxoFindFxsMapEntry.setStatus("current")
_AdGenFxoInterfaceFxsIndex_Type = AdGenFxoInterfaceFxsLocation
_AdGenFxoInterfaceFxsIndex_Object = MibTableColumn
adGenFxoInterfaceFxsIndex = _AdGenFxoInterfaceFxsIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2, 3, 1, 1, 1),
    _AdGenFxoInterfaceFxsIndex_Type()
)
adGenFxoInterfaceFxsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenFxoInterfaceFxsIndex.setStatus("current")
_AdGenFxoInterfaceFound_Type = InterfaceIndexOrZero
_AdGenFxoInterfaceFound_Object = MibTableColumn
adGenFxoInterfaceFound = _AdGenFxoInterfaceFound_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 2, 3, 1, 1, 2),
    _AdGenFxoInterfaceFound_Type()
)
adGenFxoInterfaceFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFxoInterfaceFound.setStatus("current")
_AdGenFxoTest_ObjectIdentity = ObjectIdentity
adGenFxoTest = _AdGenFxoTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 3)
)
_AdGenFxoDeviceTests_ObjectIdentity = ObjectIdentity
adGenFxoDeviceTests = _AdGenFxoDeviceTests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 3, 1)
)
_AdGenFxoInterfaceTests_ObjectIdentity = ObjectIdentity
adGenFxoInterfaceTests = _AdGenFxoInterfaceTests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 3, 2)
)
_AdGenFxoInterfaceTestsTable_Object = MibTable
adGenFxoInterfaceTestsTable = _AdGenFxoInterfaceTestsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 3, 2, 1)
)
if mibBuilder.loadTexts:
    adGenFxoInterfaceTestsTable.setStatus("current")
_AdGenFxoInterfaceTestsEntry_Object = MibTableRow
adGenFxoInterfaceTestsEntry = _AdGenFxoInterfaceTestsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 3, 2, 1, 1)
)
adGenFxoInterfaceTestsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenFxoInterfaceTestsEntry.setStatus("current")


class _AdGenFxoPortClearTest_Type(Integer32):
    """Custom type adGenFxoPortClearTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AdGenFxoPortClearTest_Type.__name__ = "Integer32"
_AdGenFxoPortClearTest_Object = MibTableColumn
adGenFxoPortClearTest = _AdGenFxoPortClearTest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 3, 2, 1, 1, 1),
    _AdGenFxoPortClearTest_Type()
)
adGenFxoPortClearTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenFxoPortClearTest.setStatus("current")


class _AdGenFxo1004HzToneTest_Type(Integer32):
    """Custom type adGenFxo1004HzToneTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("near", 1),
          ("far", 2),
          ("disable", 3))
    )


_AdGenFxo1004HzToneTest_Type.__name__ = "Integer32"
_AdGenFxo1004HzToneTest_Object = MibTableColumn
adGenFxo1004HzToneTest = _AdGenFxo1004HzToneTest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 3, 2, 1, 1, 2),
    _AdGenFxo1004HzToneTest_Type()
)
adGenFxo1004HzToneTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenFxo1004HzToneTest.setStatus("current")


class _AdGenFxoLoopStateTest_Type(Integer32):
    """Custom type adGenFxoLoopStateTest based on Integer32"""
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
        *(("disable", 1),
          ("open", 2),
          ("close", 3),
          ("ringGround", 4))
    )


_AdGenFxoLoopStateTest_Type.__name__ = "Integer32"
_AdGenFxoLoopStateTest_Object = MibTableColumn
adGenFxoLoopStateTest = _AdGenFxoLoopStateTest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 3, 2, 1, 1, 3),
    _AdGenFxoLoopStateTest_Type()
)
adGenFxoLoopStateTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenFxoLoopStateTest.setStatus("current")


class _AdGenFxoInwardLoopbackTest_Type(Integer32):
    """Custom type adGenFxoInwardLoopbackTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdGenFxoInwardLoopbackTest_Type.__name__ = "Integer32"
_AdGenFxoInwardLoopbackTest_Object = MibTableColumn
adGenFxoInwardLoopbackTest = _AdGenFxoInwardLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 3, 2, 1, 1, 4),
    _AdGenFxoInwardLoopbackTest_Type()
)
adGenFxoInwardLoopbackTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenFxoInwardLoopbackTest.setStatus("current")


class _AdGenFxoOutwardLoopbackTest_Type(Integer32):
    """Custom type adGenFxoOutwardLoopbackTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdGenFxoOutwardLoopbackTest_Type.__name__ = "Integer32"
_AdGenFxoOutwardLoopbackTest_Object = MibTableColumn
adGenFxoOutwardLoopbackTest = _AdGenFxoOutwardLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 3, 2, 1, 1, 5),
    _AdGenFxoOutwardLoopbackTest_Type()
)
adGenFxoOutwardLoopbackTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenFxoOutwardLoopbackTest.setStatus("current")
_AdGenFxoAlarms_ObjectIdentity = ObjectIdentity
adGenFxoAlarms = _AdGenFxoAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 38, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENFXO-MIB",
    **{"AdGenFxoInterfaceFxsLocation": AdGenFxoInterfaceFxsLocation,
       "adGenFxoProvisioning": adGenFxoProvisioning,
       "adGenFxoDeviceProv": adGenFxoDeviceProv,
       "adGenFxoInterfaceProv": adGenFxoInterfaceProv,
       "adGenFxoInterfaceProvTable": adGenFxoInterfaceProvTable,
       "adGenFxoInterfaceProvEntry": adGenFxoInterfaceProvEntry,
       "adGenFxoInterfaceLastErrorString": adGenFxoInterfaceLastErrorString,
       "adGenFxoInterfaceSignalingMode": adGenFxoInterfaceSignalingMode,
       "adGenFxoInterfaceTxGain": adGenFxoInterfaceTxGain,
       "adGenFxoInterfaceMinTxGain": adGenFxoInterfaceMinTxGain,
       "adGenFxoInterfaceMaxTxGain": adGenFxoInterfaceMaxTxGain,
       "adGenFxoInterfaceRxGain": adGenFxoInterfaceRxGain,
       "adGenFxoInterfaceMinRxGain": adGenFxoInterfaceMinRxGain,
       "adGenFxoInterfaceMaxRxGain": adGenFxoInterfaceMaxRxGain,
       "adGenFxoInterfaceImpedance": adGenFxoInterfaceImpedance,
       "adGenFxoInterfaceCWCIdAckGenDelay": adGenFxoInterfaceCWCIdAckGenDelay,
       "adGenFxoInterfaceCWCIdAckGenEnable": adGenFxoInterfaceCWCIdAckGenEnable,
       "adGenFxoInterfaceTargetFxsLocation": adGenFxoInterfaceTargetFxsLocation,
       "adGenFxoInterfaceRingTripMode": adGenFxoInterfaceRingTripMode,
       "adGenFxoInterfaceRingTripDuration": adGenFxoInterfaceRingTripDuration,
       "adGenFxoInterfaceRingTripMuteInterval": adGenFxoInterfaceRingTripMuteInterval,
       "adGenFxoCircuitIdentifier": adGenFxoCircuitIdentifier,
       "adGenFxoStatus": adGenFxoStatus,
       "adGenFxoDeviceStatus": adGenFxoDeviceStatus,
       "adGenFxoInterfaceStatus": adGenFxoInterfaceStatus,
       "adGenFxoInterfaceStatusTable": adGenFxoInterfaceStatusTable,
       "adGenFxoInterfaceStatusEntry": adGenFxoInterfaceStatusEntry,
       "adGenFxoPortActive": adGenFxoPortActive,
       "adGenFxoLoopFeed": adGenFxoLoopFeed,
       "adGenFxoLoopState": adGenFxoLoopState,
       "adGenFxoTestActive": adGenFxoTestActive,
       "adGenFxoRxVoicePackets": adGenFxoRxVoicePackets,
       "adGenFxoRxControlPackets": adGenFxoRxControlPackets,
       "adGenFxoTxVoicePackets": adGenFxoTxVoicePackets,
       "adGenFxoTxControlPackets": adGenFxoTxControlPackets,
       "adGenFxoClearPortCounters": adGenFxoClearPortCounters,
       "adGenFxoFindFxsMap": adGenFxoFindFxsMap,
       "adGenFxoFindFxsMapTable": adGenFxoFindFxsMapTable,
       "adGenFxoFindFxsMapEntry": adGenFxoFindFxsMapEntry,
       "adGenFxoInterfaceFxsIndex": adGenFxoInterfaceFxsIndex,
       "adGenFxoInterfaceFound": adGenFxoInterfaceFound,
       "adGenFxoTest": adGenFxoTest,
       "adGenFxoDeviceTests": adGenFxoDeviceTests,
       "adGenFxoInterfaceTests": adGenFxoInterfaceTests,
       "adGenFxoInterfaceTestsTable": adGenFxoInterfaceTestsTable,
       "adGenFxoInterfaceTestsEntry": adGenFxoInterfaceTestsEntry,
       "adGenFxoPortClearTest": adGenFxoPortClearTest,
       "adGenFxo1004HzToneTest": adGenFxo1004HzToneTest,
       "adGenFxoLoopStateTest": adGenFxoLoopStateTest,
       "adGenFxoInwardLoopbackTest": adGenFxoInwardLoopbackTest,
       "adGenFxoOutwardLoopbackTest": adGenFxoOutwardLoopbackTest,
       "adGenFxoAlarms": adGenFxoAlarms,
       "adGenFxoIdentity": adGenFxoIdentity}
)
