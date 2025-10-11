# SNMP MIB module (INFINERA-TP-OTSPtp-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-OTSPtp-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:13 2025
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

(FloatTenths,
 InfnDcmType,
 InfnEnableDisable,
 InfnEqptType,
 InfnFiberType,
 InfnPmHistStatsControl,
 InfnTimReptMode) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnDcmType",
    "InfnEnableDisable",
    "InfnEqptType",
    "InfnFiberType",
    "InfnPmHistStatsControl",
    "InfnTimReptMode")

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

otsPTPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14)
)
if mibBuilder.loadTexts:
    otsPTPMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OtsPTPTable_Object = MibTable
otsPTPTable = _OtsPTPTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1)
)
if mibBuilder.loadTexts:
    otsPTPTable.setStatus("current")
_OtsPTPEntry_Object = MibTableRow
otsPTPEntry = _OtsPTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1)
)
otsPTPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    otsPTPEntry.setStatus("current")
_OtsPTPDiscoveredNeighborTP_Type = DisplayString
_OtsPTPDiscoveredNeighborTP_Object = MibTableColumn
otsPTPDiscoveredNeighborTP = _OtsPTPDiscoveredNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 1),
    _OtsPTPDiscoveredNeighborTP_Type()
)
otsPTPDiscoveredNeighborTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPTPDiscoveredNeighborTP.setStatus("current")
_OtsPTPProvisionedNeighborTP_Type = DisplayString
_OtsPTPProvisionedNeighborTP_Object = MibTableColumn
otsPTPProvisionedNeighborTP = _OtsPTPProvisionedNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 2),
    _OtsPTPProvisionedNeighborTP_Type()
)
otsPTPProvisionedNeighborTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPTPProvisionedNeighborTP.setStatus("current")


class _OtsPtpSupportedOpticalSpectrum_Type(Integer32):
    """Custom type otsPtpSupportedOpticalSpectrum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cband", 1),
          ("extendedcband", 2))
    )


_OtsPtpSupportedOpticalSpectrum_Type.__name__ = "Integer32"
_OtsPtpSupportedOpticalSpectrum_Object = MibTableColumn
otsPtpSupportedOpticalSpectrum = _OtsPtpSupportedOpticalSpectrum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 3),
    _OtsPtpSupportedOpticalSpectrum_Type()
)
otsPtpSupportedOpticalSpectrum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpSupportedOpticalSpectrum.setStatus("current")


class _OtsPtpOperationalOpticalSpectrum_Type(Integer32):
    """Custom type otsPtpOperationalOpticalSpectrum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cband", 1),
          ("extendedcband", 2))
    )


_OtsPtpOperationalOpticalSpectrum_Type.__name__ = "Integer32"
_OtsPtpOperationalOpticalSpectrum_Object = MibTableColumn
otsPtpOperationalOpticalSpectrum = _OtsPtpOperationalOpticalSpectrum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 4),
    _OtsPtpOperationalOpticalSpectrum_Type()
)
otsPtpOperationalOpticalSpectrum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpOperationalOpticalSpectrum.setStatus("current")


class _OtsPtpExpectedSpanLossRange_Type(Integer32):
    """Custom type otsPtpExpectedSpanLossRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("under25dB", 1),
          ("over25dB", 2))
    )


_OtsPtpExpectedSpanLossRange_Type.__name__ = "Integer32"
_OtsPtpExpectedSpanLossRange_Object = MibTableColumn
otsPtpExpectedSpanLossRange = _OtsPtpExpectedSpanLossRange_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 5),
    _OtsPtpExpectedSpanLossRange_Type()
)
otsPtpExpectedSpanLossRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPtpExpectedSpanLossRange.setStatus("current")


class _OtsPtpAlsPilotSignalState_Type(Integer32):
    """Custom type otsPtpAlsPilotSignalState based on Integer32"""
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
        *(("unknown", 1),
          ("normal", 2),
          ("nosignal", 3),
          ("remoteRxFault", 4),
          ("localRxFault", 5))
    )


_OtsPtpAlsPilotSignalState_Type.__name__ = "Integer32"
_OtsPtpAlsPilotSignalState_Object = MibTableColumn
otsPtpAlsPilotSignalState = _OtsPtpAlsPilotSignalState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 6),
    _OtsPtpAlsPilotSignalState_Type()
)
otsPtpAlsPilotSignalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpAlsPilotSignalState.setStatus("current")


class _OtsPTPTxFiberType_Type(InfnFiberType):
    """Custom type otsPTPTxFiberType based on InfnFiberType"""
    defaultValue = 2


_OtsPTPTxFiberType_Type.__name__ = "InfnFiberType"
_OtsPTPTxFiberType_Object = MibTableColumn
otsPTPTxFiberType = _OtsPTPTxFiberType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 7),
    _OtsPTPTxFiberType_Type()
)
otsPTPTxFiberType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPTPTxFiberType.setStatus("current")
_OtsPtpProvRxFiberType_Type = InfnFiberType
_OtsPtpProvRxFiberType_Object = MibTableColumn
otsPtpProvRxFiberType = _OtsPtpProvRxFiberType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 8),
    _OtsPtpProvRxFiberType_Type()
)
otsPtpProvRxFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpProvRxFiberType.setStatus("current")


class _OtsPTPRxFiberType_Type(InfnFiberType):
    """Custom type otsPTPRxFiberType based on InfnFiberType"""
    defaultValue = 1


_OtsPTPRxFiberType_Type.__name__ = "InfnFiberType"
_OtsPTPRxFiberType_Object = MibTableColumn
otsPTPRxFiberType = _OtsPTPRxFiberType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 9),
    _OtsPTPRxFiberType_Type()
)
otsPTPRxFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPTPRxFiberType.setStatus("current")
_OtsPtpAssociatedPeerTxFiberType_Type = InfnFiberType
_OtsPtpAssociatedPeerTxFiberType_Object = MibTableColumn
otsPtpAssociatedPeerTxFiberType = _OtsPtpAssociatedPeerTxFiberType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 10),
    _OtsPtpAssociatedPeerTxFiberType_Type()
)
otsPtpAssociatedPeerTxFiberType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPtpAssociatedPeerTxFiberType.setStatus("current")


class _OtsPTPPmHistStatsEnable_Type(InfnPmHistStatsControl):
    """Custom type otsPTPPmHistStatsEnable based on InfnPmHistStatsControl"""
    defaultValue = 1


_OtsPTPPmHistStatsEnable_Type.__name__ = "InfnPmHistStatsControl"
_OtsPTPPmHistStatsEnable_Object = MibTableColumn
otsPTPPmHistStatsEnable = _OtsPTPPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 11),
    _OtsPTPPmHistStatsEnable_Type()
)
otsPTPPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPTPPmHistStatsEnable.setStatus("current")


class _OtsPtpLinkType_Type(Integer32):
    """Custom type otsPtpLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linktype1", 1),
          ("linktype2", 2))
    )


_OtsPtpLinkType_Type.__name__ = "Integer32"
_OtsPtpLinkType_Object = MibTableColumn
otsPtpLinkType = _OtsPtpLinkType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 12),
    _OtsPtpLinkType_Type()
)
otsPtpLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPtpLinkType.setStatus("current")
_OtsPTPRxAssociatedOtsptp_Type = DisplayString
_OtsPTPRxAssociatedOtsptp_Object = MibTableColumn
otsPTPRxAssociatedOtsptp = _OtsPTPRxAssociatedOtsptp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 13),
    _OtsPTPRxAssociatedOtsptp_Type()
)
otsPTPRxAssociatedOtsptp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPTPRxAssociatedOtsptp.setStatus("current")
_OtsPTPTxAssociatedOtsptp_Type = DisplayString
_OtsPTPTxAssociatedOtsptp_Object = MibTableColumn
otsPTPTxAssociatedOtsptp = _OtsPTPTxAssociatedOtsptp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 14),
    _OtsPTPTxAssociatedOtsptp_Type()
)
otsPTPTxAssociatedOtsptp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPTPTxAssociatedOtsptp.setStatus("current")
_OtsPTPTxAssociatedOtsEqptType_Type = InfnEqptType
_OtsPTPTxAssociatedOtsEqptType_Object = MibTableColumn
otsPTPTxAssociatedOtsEqptType = _OtsPTPTxAssociatedOtsEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 15),
    _OtsPTPTxAssociatedOtsEqptType_Type()
)
otsPTPTxAssociatedOtsEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPTPTxAssociatedOtsEqptType.setStatus("current")
_OtsPTPRxAssociatedOtsEqptType_Type = InfnEqptType
_OtsPTPRxAssociatedOtsEqptType_Object = MibTableColumn
otsPTPRxAssociatedOtsEqptType = _OtsPTPRxAssociatedOtsEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 16),
    _OtsPTPRxAssociatedOtsEqptType_Type()
)
otsPTPRxAssociatedOtsEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPTPRxAssociatedOtsEqptType.setStatus("current")


class _OtsPTPSpanDistance_Type(FloatTenths):
    """Custom type otsPTPSpanDistance based on FloatTenths"""
    defaultValue = 0


_OtsPTPSpanDistance_Type.__name__ = "FloatTenths"
_OtsPTPSpanDistance_Object = MibTableColumn
otsPTPSpanDistance = _OtsPTPSpanDistance_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 17),
    _OtsPTPSpanDistance_Type()
)
otsPTPSpanDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPTPSpanDistance.setStatus("current")


class _OtsPTPInlineDcmType_Type(InfnDcmType):
    """Custom type otsPTPInlineDcmType based on InfnDcmType"""
    defaultValue = 25


_OtsPTPInlineDcmType_Type.__name__ = "InfnDcmType"
_OtsPTPInlineDcmType_Object = MibTableColumn
otsPTPInlineDcmType = _OtsPTPInlineDcmType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 18),
    _OtsPTPInlineDcmType_Type()
)
otsPTPInlineDcmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPTPInlineDcmType.setStatus("current")


class _OtsPTPPreSpanPad_Type(FloatTenths):
    """Custom type otsPTPPreSpanPad based on FloatTenths"""
    defaultValue = 0


_OtsPTPPreSpanPad_Type.__name__ = "FloatTenths"
_OtsPTPPreSpanPad_Object = MibTableColumn
otsPTPPreSpanPad = _OtsPTPPreSpanPad_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 19),
    _OtsPTPPreSpanPad_Type()
)
otsPTPPreSpanPad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPTPPreSpanPad.setStatus("current")


class _OtsPTPPostSpanPad_Type(FloatTenths):
    """Custom type otsPTPPostSpanPad based on FloatTenths"""
    defaultValue = 0


_OtsPTPPostSpanPad_Type.__name__ = "FloatTenths"
_OtsPTPPostSpanPad_Object = MibTableColumn
otsPTPPostSpanPad = _OtsPTPPostSpanPad_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 20),
    _OtsPTPPostSpanPad_Type()
)
otsPTPPostSpanPad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPTPPostSpanPad.setStatus("current")
_OtsPTPAssociatedSltetp_Type = DisplayString
_OtsPTPAssociatedSltetp_Object = MibTableColumn
otsPTPAssociatedSltetp = _OtsPTPAssociatedSltetp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 21),
    _OtsPTPAssociatedSltetp_Type()
)
otsPTPAssociatedSltetp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPTPAssociatedSltetp.setStatus("current")
_OtsPtpRxAssociatedSltePtp_Type = DisplayString
_OtsPtpRxAssociatedSltePtp_Object = MibTableColumn
otsPtpRxAssociatedSltePtp = _OtsPtpRxAssociatedSltePtp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 22),
    _OtsPtpRxAssociatedSltePtp_Type()
)
otsPtpRxAssociatedSltePtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPtpRxAssociatedSltePtp.setStatus("current")
_OtsPtpAssociatedSltePtp_Type = DisplayString
_OtsPtpAssociatedSltePtp_Object = MibTableColumn
otsPtpAssociatedSltePtp = _OtsPtpAssociatedSltePtp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 23),
    _OtsPtpAssociatedSltePtp_Type()
)
otsPtpAssociatedSltePtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPtpAssociatedSltePtp.setStatus("current")
_OtsPtpTxAssociatedidlerPtp_Type = DisplayString
_OtsPtpTxAssociatedidlerPtp_Object = MibTableColumn
otsPtpTxAssociatedidlerPtp = _OtsPtpTxAssociatedidlerPtp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 24),
    _OtsPtpTxAssociatedidlerPtp_Type()
)
otsPtpTxAssociatedidlerPtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpTxAssociatedidlerPtp.setStatus("current")
_OtsPtpRxAssociatedidlerPtp_Type = DisplayString
_OtsPtpRxAssociatedidlerPtp_Object = MibTableColumn
otsPtpRxAssociatedidlerPtp = _OtsPtpRxAssociatedidlerPtp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 25),
    _OtsPtpRxAssociatedidlerPtp_Type()
)
otsPtpRxAssociatedidlerPtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpRxAssociatedidlerPtp.setStatus("current")
_OtsPTPTxEqptList_Type = DisplayString
_OtsPTPTxEqptList_Object = MibTableColumn
otsPTPTxEqptList = _OtsPTPTxEqptList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 26),
    _OtsPTPTxEqptList_Type()
)
otsPTPTxEqptList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPTPTxEqptList.setStatus("current")
_OtsPTPRxEqptList_Type = DisplayString
_OtsPTPRxEqptList_Object = MibTableColumn
otsPTPRxEqptList = _OtsPTPRxEqptList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 27),
    _OtsPTPRxEqptList_Type()
)
otsPTPRxEqptList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPTPRxEqptList.setStatus("current")


class _OtsPtpRxFiberTypeOverride_Type(Integer32):
    """Custom type otsPtpRxFiberTypeOverride based on Integer32"""
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


_OtsPtpRxFiberTypeOverride_Type.__name__ = "Integer32"
_OtsPtpRxFiberTypeOverride_Object = MibTableColumn
otsPtpRxFiberTypeOverride = _OtsPtpRxFiberTypeOverride_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 28),
    _OtsPtpRxFiberTypeOverride_Type()
)
otsPtpRxFiberTypeOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPtpRxFiberTypeOverride.setStatus("current")
_OtsptpOAMControl_Type = InfnEnableDisable
_OtsptpOAMControl_Object = MibTableColumn
otsptpOAMControl = _OtsptpOAMControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 29),
    _OtsptpOAMControl_Type()
)
otsptpOAMControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsptpOAMControl.setStatus("current")
_OtsptpRemoteOAMStatus_Type = InfnEnableDisable
_OtsptpRemoteOAMStatus_Object = MibTableColumn
otsptpRemoteOAMStatus = _OtsptpRemoteOAMStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 30),
    _OtsptpRemoteOAMStatus_Type()
)
otsptpRemoteOAMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsptpRemoteOAMStatus.setStatus("current")
_OtsptpTransmitTTI_Type = DisplayString
_OtsptpTransmitTTI_Object = MibTableColumn
otsptpTransmitTTI = _OtsptpTransmitTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 31),
    _OtsptpTransmitTTI_Type()
)
otsptpTransmitTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsptpTransmitTTI.setStatus("current")
_OtsptpRecievedTTI_Type = DisplayString
_OtsptpRecievedTTI_Object = MibTableColumn
otsptpRecievedTTI = _OtsptpRecievedTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 32),
    _OtsptpRecievedTTI_Type()
)
otsptpRecievedTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsptpRecievedTTI.setStatus("current")
_OtsptpAmpType_Type = Integer32
_OtsptpAmpType_Object = MibTableColumn
otsptpAmpType = _OtsptpAmpType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 33),
    _OtsptpAmpType_Type()
)
otsptpAmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsptpAmpType.setStatus("current")
_OtsPtpExpectedSAPI_Type = DisplayString
_OtsPtpExpectedSAPI_Object = MibTableColumn
otsPtpExpectedSAPI = _OtsPtpExpectedSAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 34),
    _OtsPtpExpectedSAPI_Type()
)
otsPtpExpectedSAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPtpExpectedSAPI.setStatus("current")
_OtsPtpExpectedDAPI_Type = DisplayString
_OtsPtpExpectedDAPI_Object = MibTableColumn
otsPtpExpectedDAPI = _OtsPtpExpectedDAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 35),
    _OtsPtpExpectedDAPI_Type()
)
otsPtpExpectedDAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPtpExpectedDAPI.setStatus("current")
_OtsPtpTimDetMode_Type = InfnTimReptMode
_OtsPtpTimDetMode_Object = MibTableColumn
otsPtpTimDetMode = _OtsPtpTimDetMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 36),
    _OtsPtpTimDetMode_Type()
)
otsPtpTimDetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPtpTimDetMode.setStatus("current")
_OtsPTPFiberLabelTx_Type = DisplayString
_OtsPTPFiberLabelTx_Object = MibTableColumn
otsPTPFiberLabelTx = _OtsPTPFiberLabelTx_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 1, 1, 37),
    _OtsPTPFiberLabelTx_Type()
)
otsPTPFiberLabelTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otsPTPFiberLabelTx.setStatus("current")
_OtsPTPConformance_ObjectIdentity = ObjectIdentity
otsPTPConformance = _OtsPTPConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 3)
)
_OtsPTPCompliances_ObjectIdentity = ObjectIdentity
otsPTPCompliances = _OtsPTPCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 3, 1)
)
_OtsPTPGroups_ObjectIdentity = ObjectIdentity
otsPTPGroups = _OtsPTPGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 3, 2)
)

# Managed Objects groups

otsPTPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 3, 2, 1)
)
otsPTPGroup.setObjects(
      *(("INFINERA-TP-OTSPtp-MIB", "otsPTPDiscoveredNeighborTP"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPTPProvisionedNeighborTP"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPtpSupportedOpticalSpectrum"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPtpOperationalOpticalSpectrum"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPtpExpectedSpanLossRange"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPtpAlsPilotSignalState"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPtpProvRxFiberType"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPtpAssociatedPeerTxFiberType"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPtpRxAssociatedSltePtp"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPtpAssociatedSltePtp"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPtpLinkType"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPtpRxAssociatedidlerPtp"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPtpTxAssociatedidlerPtp"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPTPTxFiberType"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPTPRxFiberType"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPTPPmHistStatsEnable"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPTPRxAssociatedOtsptp"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPTPTxAssociatedOtsptp"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPTPSpanDistance"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPTPInlineDcmType"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPTPPreSpanPad"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPTPPostSpanPad"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPTPTxEqptList"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPTPRxEqptList"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPTPTxAssociatedOtsEqptType"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPTPRxAssociatedOtsEqptType"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPTPAssociatedSltetp"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPtpRxFiberTypeOverride"),
        ("INFINERA-TP-OTSPtp-MIB", "otsptpOAMControl"),
        ("INFINERA-TP-OTSPtp-MIB", "otsptpRemoteOAMStatus"),
        ("INFINERA-TP-OTSPtp-MIB", "otsptpTransmitTTI"),
        ("INFINERA-TP-OTSPtp-MIB", "otsptpRecievedTTI"),
        ("INFINERA-TP-OTSPtp-MIB", "otsptpAmpType"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPtpExpectedSAPI"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPtpExpectedDAPI"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPtpTimDetMode"),
        ("INFINERA-TP-OTSPtp-MIB", "otsPTPFiberLabelTx"))
)
if mibBuilder.loadTexts:
    otsPTPGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

otsPTPCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 14, 3, 1, 1)
)
otsPTPCompliance.setObjects(
    ("INFINERA-TP-OTSPtp-MIB", "otsPTPGroup")
)
if mibBuilder.loadTexts:
    otsPTPCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-OTSPtp-MIB",
    **{"otsPTPMIB": otsPTPMIB,
       "otsPTPTable": otsPTPTable,
       "otsPTPEntry": otsPTPEntry,
       "otsPTPDiscoveredNeighborTP": otsPTPDiscoveredNeighborTP,
       "otsPTPProvisionedNeighborTP": otsPTPProvisionedNeighborTP,
       "otsPtpSupportedOpticalSpectrum": otsPtpSupportedOpticalSpectrum,
       "otsPtpOperationalOpticalSpectrum": otsPtpOperationalOpticalSpectrum,
       "otsPtpExpectedSpanLossRange": otsPtpExpectedSpanLossRange,
       "otsPtpAlsPilotSignalState": otsPtpAlsPilotSignalState,
       "otsPTPTxFiberType": otsPTPTxFiberType,
       "otsPtpProvRxFiberType": otsPtpProvRxFiberType,
       "otsPTPRxFiberType": otsPTPRxFiberType,
       "otsPtpAssociatedPeerTxFiberType": otsPtpAssociatedPeerTxFiberType,
       "otsPTPPmHistStatsEnable": otsPTPPmHistStatsEnable,
       "otsPtpLinkType": otsPtpLinkType,
       "otsPTPRxAssociatedOtsptp": otsPTPRxAssociatedOtsptp,
       "otsPTPTxAssociatedOtsptp": otsPTPTxAssociatedOtsptp,
       "otsPTPTxAssociatedOtsEqptType": otsPTPTxAssociatedOtsEqptType,
       "otsPTPRxAssociatedOtsEqptType": otsPTPRxAssociatedOtsEqptType,
       "otsPTPSpanDistance": otsPTPSpanDistance,
       "otsPTPInlineDcmType": otsPTPInlineDcmType,
       "otsPTPPreSpanPad": otsPTPPreSpanPad,
       "otsPTPPostSpanPad": otsPTPPostSpanPad,
       "otsPTPAssociatedSltetp": otsPTPAssociatedSltetp,
       "otsPtpRxAssociatedSltePtp": otsPtpRxAssociatedSltePtp,
       "otsPtpAssociatedSltePtp": otsPtpAssociatedSltePtp,
       "otsPtpTxAssociatedidlerPtp": otsPtpTxAssociatedidlerPtp,
       "otsPtpRxAssociatedidlerPtp": otsPtpRxAssociatedidlerPtp,
       "otsPTPTxEqptList": otsPTPTxEqptList,
       "otsPTPRxEqptList": otsPTPRxEqptList,
       "otsPtpRxFiberTypeOverride": otsPtpRxFiberTypeOverride,
       "otsptpOAMControl": otsptpOAMControl,
       "otsptpRemoteOAMStatus": otsptpRemoteOAMStatus,
       "otsptpTransmitTTI": otsptpTransmitTTI,
       "otsptpRecievedTTI": otsptpRecievedTTI,
       "otsptpAmpType": otsptpAmpType,
       "otsPtpExpectedSAPI": otsPtpExpectedSAPI,
       "otsPtpExpectedDAPI": otsPtpExpectedDAPI,
       "otsPtpTimDetMode": otsPtpTimDetMode,
       "otsPTPFiberLabelTx": otsPTPFiberLabelTx,
       "otsPTPConformance": otsPTPConformance,
       "otsPTPCompliances": otsPTPCompliances,
       "otsPTPCompliance": otsPTPCompliance,
       "otsPTPGroups": otsPTPGroups,
       "otsPTPGroup": otsPTPGroup}
)
