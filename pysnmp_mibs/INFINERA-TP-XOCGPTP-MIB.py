# SNMP MIB module (INFINERA-TP-XOCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-XOCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:25 2025
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

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(FloatHundredths,
 FloatTenths,
 InfnAutoTunable,
 InfnChassisType,
 InfnEnableDisable,
 InfnEncoding,
 InfnModulation,
 InfnOperationalState,
 InfnPicStatus) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "FloatTenths",
    "InfnAutoTunable",
    "InfnChassisType",
    "InfnEnableDisable",
    "InfnEncoding",
    "InfnModulation",
    "InfnOperationalState",
    "InfnPicStatus")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

xOcgPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51)
)
if mibBuilder.loadTexts:
    xOcgPtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XOcgPtpTable_Object = MibTable
xOcgPtpTable = _XOcgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1)
)
if mibBuilder.loadTexts:
    xOcgPtpTable.setStatus("current")
_XOcgPtpEntry_Object = MibTableRow
xOcgPtpEntry = _XOcgPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1)
)
xOcgPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xOcgPtpEntry.setStatus("current")


class _XOcgPtpPmHistStatsEnable_Type(Integer32):
    """Custom type xOcgPtpPmHistStatsEnable based on Integer32"""
    defaultValue = 1

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


_XOcgPtpPmHistStatsEnable_Type.__name__ = "Integer32"
_XOcgPtpPmHistStatsEnable_Object = MibTableColumn
xOcgPtpPmHistStatsEnable = _XOcgPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 1),
    _XOcgPtpPmHistStatsEnable_Type()
)
xOcgPtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xOcgPtpPmHistStatsEnable.setStatus("current")


class _XOcgPtpOcgPowerControlLoop_Type(Integer32):
    """Custom type xOcgPtpOcgPowerControlLoop based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("unknown", 3))
    )


_XOcgPtpOcgPowerControlLoop_Type.__name__ = "Integer32"
_XOcgPtpOcgPowerControlLoop_Object = MibTableColumn
xOcgPtpOcgPowerControlLoop = _XOcgPtpOcgPowerControlLoop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 2),
    _XOcgPtpOcgPowerControlLoop_Type()
)
xOcgPtpOcgPowerControlLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xOcgPtpOcgPowerControlLoop.setStatus("current")
_XOcgPtpTxPicState_Type = InfnPicStatus
_XOcgPtpTxPicState_Object = MibTableColumn
xOcgPtpTxPicState = _XOcgPtpTxPicState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 3),
    _XOcgPtpTxPicState_Type()
)
xOcgPtpTxPicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpTxPicState.setStatus("current")
_XOcgPtpRxPicState_Type = InfnPicStatus
_XOcgPtpRxPicState_Object = MibTableColumn
xOcgPtpRxPicState = _XOcgPtpRxPicState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 4),
    _XOcgPtpRxPicState_Type()
)
xOcgPtpRxPicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpRxPicState.setStatus("current")


class _XOcgPtpDlmEqptTyp_Type(InfnChassisType):
    """Custom type xOcgPtpDlmEqptTyp based on InfnChassisType"""
    defaultValue = 6


_XOcgPtpDlmEqptTyp_Type.__name__ = "InfnChassisType"
_XOcgPtpDlmEqptTyp_Object = MibTableColumn
xOcgPtpDlmEqptTyp = _XOcgPtpDlmEqptTyp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 5),
    _XOcgPtpDlmEqptTyp_Type()
)
xOcgPtpDlmEqptTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpDlmEqptTyp.setStatus("current")
_XOcgPtpChannelCount_Type = FloatTenths
_XOcgPtpChannelCount_Object = MibTableColumn
xOcgPtpChannelCount = _XOcgPtpChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 6),
    _XOcgPtpChannelCount_Type()
)
xOcgPtpChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpChannelCount.setStatus("current")


class _XOcgPtpLineSystemMode_Type(Integer32):
    """Custom type xOcgPtpLineSystemMode based on Integer32"""
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
        *(("modeocg", 1),
          ("modeopenwave", 2),
          ("modescg", 3),
          ("modescgpassivemux-1", 4))
    )


_XOcgPtpLineSystemMode_Type.__name__ = "Integer32"
_XOcgPtpLineSystemMode_Object = MibTableColumn
xOcgPtpLineSystemMode = _XOcgPtpLineSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 7),
    _XOcgPtpLineSystemMode_Type()
)
xOcgPtpLineSystemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpLineSystemMode.setStatus("current")
_XOcgPtpProvisionedPeerTp_Type = DisplayString
_XOcgPtpProvisionedPeerTp_Object = MibTableColumn
xOcgPtpProvisionedPeerTp = _XOcgPtpProvisionedPeerTp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 8),
    _XOcgPtpProvisionedPeerTp_Type()
)
xOcgPtpProvisionedPeerTp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xOcgPtpProvisionedPeerTp.setStatus("current")
_XOcgPtpDiscoveredPeerTp_Type = DisplayString
_XOcgPtpDiscoveredPeerTp_Object = MibTableColumn
xOcgPtpDiscoveredPeerTp = _XOcgPtpDiscoveredPeerTp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 9),
    _XOcgPtpDiscoveredPeerTp_Type()
)
xOcgPtpDiscoveredPeerTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpDiscoveredPeerTp.setStatus("current")


class _XOcgPtpAutoDiscoveryPeerLm_Type(InfnOperationalState):
    """Custom type xOcgPtpAutoDiscoveryPeerLm based on InfnOperationalState"""
    defaultValue = 1


_XOcgPtpAutoDiscoveryPeerLm_Type.__name__ = "InfnOperationalState"
_XOcgPtpAutoDiscoveryPeerLm_Object = MibTableColumn
xOcgPtpAutoDiscoveryPeerLm = _XOcgPtpAutoDiscoveryPeerLm_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 10),
    _XOcgPtpAutoDiscoveryPeerLm_Type()
)
xOcgPtpAutoDiscoveryPeerLm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xOcgPtpAutoDiscoveryPeerLm.setStatus("current")
_XOcgPtpOpenwaveTargetTxOcgPower_Type = FloatTenths
_XOcgPtpOpenwaveTargetTxOcgPower_Object = MibTableColumn
xOcgPtpOpenwaveTargetTxOcgPower = _XOcgPtpOpenwaveTargetTxOcgPower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 11),
    _XOcgPtpOpenwaveTargetTxOcgPower_Type()
)
xOcgPtpOpenwaveTargetTxOcgPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xOcgPtpOpenwaveTargetTxOcgPower.setStatus("current")


class _XOcgPtpProvisionedEncodingMode_Type(InfnEncoding):
    """Custom type xOcgPtpProvisionedEncodingMode based on InfnEncoding"""
    defaultValue = 1


_XOcgPtpProvisionedEncodingMode_Type.__name__ = "InfnEncoding"
_XOcgPtpProvisionedEncodingMode_Object = MibTableColumn
xOcgPtpProvisionedEncodingMode = _XOcgPtpProvisionedEncodingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 12),
    _XOcgPtpProvisionedEncodingMode_Type()
)
xOcgPtpProvisionedEncodingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xOcgPtpProvisionedEncodingMode.setStatus("current")


class _XOcgPtpInstalledEncodingMode_Type(InfnEncoding):
    """Custom type xOcgPtpInstalledEncodingMode based on InfnEncoding"""
    defaultValue = 1


_XOcgPtpInstalledEncodingMode_Type.__name__ = "InfnEncoding"
_XOcgPtpInstalledEncodingMode_Object = MibTableColumn
xOcgPtpInstalledEncodingMode = _XOcgPtpInstalledEncodingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 13),
    _XOcgPtpInstalledEncodingMode_Type()
)
xOcgPtpInstalledEncodingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpInstalledEncodingMode.setStatus("current")


class _XOcgPtpAutomaticTunable_Type(InfnAutoTunable):
    """Custom type xOcgPtpAutomaticTunable based on InfnAutoTunable"""
    defaultValue = 2


_XOcgPtpAutomaticTunable_Type.__name__ = "InfnAutoTunable"
_XOcgPtpAutomaticTunable_Object = MibTableColumn
xOcgPtpAutomaticTunable = _XOcgPtpAutomaticTunable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 14),
    _XOcgPtpAutomaticTunable_Type()
)
xOcgPtpAutomaticTunable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xOcgPtpAutomaticTunable.setStatus("current")
_XOcgPtpAvailableTunableOcgNumbers_Type = Integer32
_XOcgPtpAvailableTunableOcgNumbers_Object = MibTableColumn
xOcgPtpAvailableTunableOcgNumbers = _XOcgPtpAvailableTunableOcgNumbers_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 15),
    _XOcgPtpAvailableTunableOcgNumbers_Type()
)
xOcgPtpAvailableTunableOcgNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpAvailableTunableOcgNumbers.setStatus("current")
_XOcgPtpTunableOcgNumber_Type = Integer32
_XOcgPtpTunableOcgNumber_Object = MibTableColumn
xOcgPtpTunableOcgNumber = _XOcgPtpTunableOcgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 16),
    _XOcgPtpTunableOcgNumber_Type()
)
xOcgPtpTunableOcgNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xOcgPtpTunableOcgNumber.setStatus("current")
_XOcgPtpRemainingTunabilityOperatingHours_Type = Integer32
_XOcgPtpRemainingTunabilityOperatingHours_Object = MibTableColumn
xOcgPtpRemainingTunabilityOperatingHours = _XOcgPtpRemainingTunabilityOperatingHours_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 17),
    _XOcgPtpRemainingTunabilityOperatingHours_Type()
)
xOcgPtpRemainingTunabilityOperatingHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpRemainingTunabilityOperatingHours.setStatus("current")
_XOcgPtpCurOcgNumber_Type = Integer32
_XOcgPtpCurOcgNumber_Object = MibTableColumn
xOcgPtpCurOcgNumber = _XOcgPtpCurOcgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 18),
    _XOcgPtpCurOcgNumber_Type()
)
xOcgPtpCurOcgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpCurOcgNumber.setStatus("current")
_XOcgPtpGain_Type = FloatTenths
_XOcgPtpGain_Object = MibTableColumn
xOcgPtpGain = _XOcgPtpGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 19),
    _XOcgPtpGain_Type()
)
xOcgPtpGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xOcgPtpGain.setStatus("current")
_XOcgPtpMaxFruGain_Type = FloatHundredths
_XOcgPtpMaxFruGain_Object = MibTableColumn
xOcgPtpMaxFruGain = _XOcgPtpMaxFruGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 20),
    _XOcgPtpMaxFruGain_Type()
)
xOcgPtpMaxFruGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpMaxFruGain.setStatus("current")
_XOcgPtpRxEdfaOutputPowerTarget_Type = FloatTenths
_XOcgPtpRxEdfaOutputPowerTarget_Object = MibTableColumn
xOcgPtpRxEdfaOutputPowerTarget = _XOcgPtpRxEdfaOutputPowerTarget_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 21),
    _XOcgPtpRxEdfaOutputPowerTarget_Type()
)
xOcgPtpRxEdfaOutputPowerTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpRxEdfaOutputPowerTarget.setStatus("current")
_XOcgPtpOcgTxTTI_Type = DisplayString
_XOcgPtpOcgTxTTI_Object = MibTableColumn
xOcgPtpOcgTxTTI = _XOcgPtpOcgTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 22),
    _XOcgPtpOcgTxTTI_Type()
)
xOcgPtpOcgTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xOcgPtpOcgTxTTI.setStatus("current")
_XOcgPtpOcgExpectedTTI_Type = DisplayString
_XOcgPtpOcgExpectedTTI_Object = MibTableColumn
xOcgPtpOcgExpectedTTI = _XOcgPtpOcgExpectedTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 23),
    _XOcgPtpOcgExpectedTTI_Type()
)
xOcgPtpOcgExpectedTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xOcgPtpOcgExpectedTTI.setStatus("current")
_XOcgPtpOcgReceivedTTI_Type = DisplayString
_XOcgPtpOcgReceivedTTI_Object = MibTableColumn
xOcgPtpOcgReceivedTTI = _XOcgPtpOcgReceivedTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 24),
    _XOcgPtpOcgReceivedTTI_Type()
)
xOcgPtpOcgReceivedTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpOcgReceivedTTI.setStatus("current")
_XOcgPtpLoopback_Type = TruthValue
_XOcgPtpLoopback_Object = MibTableColumn
xOcgPtpLoopback = _XOcgPtpLoopback_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 25),
    _XOcgPtpLoopback_Type()
)
xOcgPtpLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xOcgPtpLoopback.setStatus("current")
_XOcgPtpBwQmax_Type = FloatTenths
_XOcgPtpBwQmax_Object = MibTableColumn
xOcgPtpBwQmax = _XOcgPtpBwQmax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 26),
    _XOcgPtpBwQmax_Type()
)
xOcgPtpBwQmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpBwQmax.setStatus("current")
_XOcgPtpBwQused_Type = FloatTenths
_XOcgPtpBwQused_Object = MibTableColumn
xOcgPtpBwQused = _XOcgPtpBwQused_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 27),
    _XOcgPtpBwQused_Type()
)
xOcgPtpBwQused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpBwQused.setStatus("current")
_XOcgPtpBwQlicensed_Type = FloatTenths
_XOcgPtpBwQlicensed_Object = MibTableColumn
xOcgPtpBwQlicensed = _XOcgPtpBwQlicensed_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 1, 1, 28),
    _XOcgPtpBwQlicensed_Type()
)
xOcgPtpBwQlicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpBwQlicensed.setStatus("current")
_XOcgPtpConformance_ObjectIdentity = ObjectIdentity
xOcgPtpConformance = _XOcgPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 3)
)
_XOcgPtpCompliances_ObjectIdentity = ObjectIdentity
xOcgPtpCompliances = _XOcgPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 3, 1)
)
_XOcgPtpGroups_ObjectIdentity = ObjectIdentity
xOcgPtpGroups = _XOcgPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 3, 2)
)

# Managed Objects groups

xOcgPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 3, 2, 1)
)
xOcgPtpGroup.setObjects(
      *(("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpPmHistStatsEnable"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpOcgPowerControlLoop"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpTxPicState"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpRxPicState"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpDlmEqptTyp"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpChannelCount"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpLineSystemMode"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpProvisionedPeerTp"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpDiscoveredPeerTp"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpAutoDiscoveryPeerLm"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpOpenwaveTargetTxOcgPower"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpProvisionedEncodingMode"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpInstalledEncodingMode"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpAutomaticTunable"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpAvailableTunableOcgNumbers"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpTunableOcgNumber"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpRemainingTunabilityOperatingHours"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpCurOcgNumber"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpGain"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpMaxFruGain"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpRxEdfaOutputPowerTarget"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpOcgTxTTI"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpOcgExpectedTTI"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpOcgReceivedTTI"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpLoopback"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpBwQmax"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpBwQused"),
        ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpBwQlicensed"))
)
if mibBuilder.loadTexts:
    xOcgPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xOcgPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 51, 3, 1, 1)
)
xOcgPtpCompliance.setObjects(
    ("INFINERA-TP-XOCGPTP-MIB", "xOcgPtpGroup")
)
if mibBuilder.loadTexts:
    xOcgPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-XOCGPTP-MIB",
    **{"xOcgPtpMIB": xOcgPtpMIB,
       "xOcgPtpTable": xOcgPtpTable,
       "xOcgPtpEntry": xOcgPtpEntry,
       "xOcgPtpPmHistStatsEnable": xOcgPtpPmHistStatsEnable,
       "xOcgPtpOcgPowerControlLoop": xOcgPtpOcgPowerControlLoop,
       "xOcgPtpTxPicState": xOcgPtpTxPicState,
       "xOcgPtpRxPicState": xOcgPtpRxPicState,
       "xOcgPtpDlmEqptTyp": xOcgPtpDlmEqptTyp,
       "xOcgPtpChannelCount": xOcgPtpChannelCount,
       "xOcgPtpLineSystemMode": xOcgPtpLineSystemMode,
       "xOcgPtpProvisionedPeerTp": xOcgPtpProvisionedPeerTp,
       "xOcgPtpDiscoveredPeerTp": xOcgPtpDiscoveredPeerTp,
       "xOcgPtpAutoDiscoveryPeerLm": xOcgPtpAutoDiscoveryPeerLm,
       "xOcgPtpOpenwaveTargetTxOcgPower": xOcgPtpOpenwaveTargetTxOcgPower,
       "xOcgPtpProvisionedEncodingMode": xOcgPtpProvisionedEncodingMode,
       "xOcgPtpInstalledEncodingMode": xOcgPtpInstalledEncodingMode,
       "xOcgPtpAutomaticTunable": xOcgPtpAutomaticTunable,
       "xOcgPtpAvailableTunableOcgNumbers": xOcgPtpAvailableTunableOcgNumbers,
       "xOcgPtpTunableOcgNumber": xOcgPtpTunableOcgNumber,
       "xOcgPtpRemainingTunabilityOperatingHours": xOcgPtpRemainingTunabilityOperatingHours,
       "xOcgPtpCurOcgNumber": xOcgPtpCurOcgNumber,
       "xOcgPtpGain": xOcgPtpGain,
       "xOcgPtpMaxFruGain": xOcgPtpMaxFruGain,
       "xOcgPtpRxEdfaOutputPowerTarget": xOcgPtpRxEdfaOutputPowerTarget,
       "xOcgPtpOcgTxTTI": xOcgPtpOcgTxTTI,
       "xOcgPtpOcgExpectedTTI": xOcgPtpOcgExpectedTTI,
       "xOcgPtpOcgReceivedTTI": xOcgPtpOcgReceivedTTI,
       "xOcgPtpLoopback": xOcgPtpLoopback,
       "xOcgPtpBwQmax": xOcgPtpBwQmax,
       "xOcgPtpBwQused": xOcgPtpBwQused,
       "xOcgPtpBwQlicensed": xOcgPtpBwQlicensed,
       "xOcgPtpConformance": xOcgPtpConformance,
       "xOcgPtpCompliances": xOcgPtpCompliances,
       "xOcgPtpCompliance": xOcgPtpCompliance,
       "xOcgPtpGroups": xOcgPtpGroups,
       "xOcgPtpGroup": xOcgPtpGroup}
)
