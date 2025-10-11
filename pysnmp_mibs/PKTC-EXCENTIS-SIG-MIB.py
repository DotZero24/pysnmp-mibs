# SNMP MIB module (PKTC-EXCENTIS-SIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rfc/PKTC-EXCENTIS-SIG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:21:35 2025
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

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(excentis,) = mibBuilder.importSymbols(
    "EXCENTIS-MIB",
    "excentis")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pktcExcentisSigMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7432, 2)
)
if mibBuilder.loadTexts:
    pktcExcentisSigMib.setRevisions(
        ("2005-09-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TenthdBm(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class PktcCodecType(TextualConvention, Integer32):
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
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("g729", 3),
          ("reserved", 4),
          ("g729E", 5),
          ("pcmu", 6),
          ("g726at32", 7),
          ("g728", 8),
          ("pcma", 9),
          ("g726at16", 10),
          ("g726at24", 11),
          ("g726at40", 12),
          ("ilbc", 13),
          ("bv16", 14))
    )



class PktcRingCadence(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 36),
    )



class PktcSigType(TextualConvention, Integer32):
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
        *(("other", 1),
          ("reserved", 2),
          ("ncs", 3))
    )



# MIB Managed Objects in the order of their OIDs

_PktcSigNotification_ObjectIdentity = ObjectIdentity
pktcSigNotification = _PktcSigNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7432, 2, 0)
)
_PktcSigMibObjects_ObjectIdentity = ObjectIdentity
pktcSigMibObjects = _PktcSigMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1)
)
_PktcSigDevConfigObjects_ObjectIdentity = ObjectIdentity
pktcSigDevConfigObjects = _PktcSigDevConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1)
)
_PktcSigDevCodecTable_Object = MibTable
pktcSigDevCodecTable = _PktcSigDevCodecTable_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pktcSigDevCodecTable.setStatus("current")
_PktcSigDevCodecEntry_Object = MibTableRow
pktcSigDevCodecEntry = _PktcSigDevCodecEntry_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 1, 1)
)
pktcSigDevCodecEntry.setIndexNames(
    (0, "PKTC-EXCENTIS-SIG-MIB", "pktcSigDevCodecComboIndex"),
    (0, "PKTC-EXCENTIS-SIG-MIB", "pktcSigDevCodecType"),
)
if mibBuilder.loadTexts:
    pktcSigDevCodecEntry.setStatus("current")


class _PktcSigDevCodecComboIndex_Type(Unsigned32):
    """Custom type pktcSigDevCodecComboIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PktcSigDevCodecComboIndex_Type.__name__ = "Unsigned32"
_PktcSigDevCodecComboIndex_Object = MibTableColumn
pktcSigDevCodecComboIndex = _PktcSigDevCodecComboIndex_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 1, 1, 1),
    _PktcSigDevCodecComboIndex_Type()
)
pktcSigDevCodecComboIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcSigDevCodecComboIndex.setStatus("current")
_PktcSigDevCodecType_Type = PktcCodecType
_PktcSigDevCodecType_Object = MibTableColumn
pktcSigDevCodecType = _PktcSigDevCodecType_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 1, 1, 2),
    _PktcSigDevCodecType_Type()
)
pktcSigDevCodecType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcSigDevCodecType.setStatus("current")


class _PktcSigDevCodecMax_Type(Unsigned32):
    """Custom type pktcSigDevCodecMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PktcSigDevCodecMax_Type.__name__ = "Unsigned32"
_PktcSigDevCodecMax_Object = MibTableColumn
pktcSigDevCodecMax = _PktcSigDevCodecMax_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 1, 1, 3),
    _PktcSigDevCodecMax_Type()
)
pktcSigDevCodecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevCodecMax.setStatus("current")
_PktcSigDevEchoCancellation_Type = TruthValue
_PktcSigDevEchoCancellation_Object = MibScalar
pktcSigDevEchoCancellation = _PktcSigDevEchoCancellation_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 2),
    _PktcSigDevEchoCancellation_Type()
)
pktcSigDevEchoCancellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevEchoCancellation.setStatus("current")
_PktcSigDevSilenceSuppression_Type = TruthValue
_PktcSigDevSilenceSuppression_Object = MibScalar
pktcSigDevSilenceSuppression = _PktcSigDevSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 3),
    _PktcSigDevSilenceSuppression_Type()
)
pktcSigDevSilenceSuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevSilenceSuppression.setStatus("current")


class _PktcSigDevCallerIdSigProtocol_Type(Integer32):
    """Custom type pktcSigDevCallerIdSigProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fsk", 1),
          ("dtmf", 2))
    )


_PktcSigDevCallerIdSigProtocol_Type.__name__ = "Integer32"
_PktcSigDevCallerIdSigProtocol_Object = MibScalar
pktcSigDevCallerIdSigProtocol = _PktcSigDevCallerIdSigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 4),
    _PktcSigDevCallerIdSigProtocol_Type()
)
pktcSigDevCallerIdSigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevCallerIdSigProtocol.setStatus("current")
_PktcSigDevR0Cadence_Type = PktcRingCadence
_PktcSigDevR0Cadence_Object = MibScalar
pktcSigDevR0Cadence = _PktcSigDevR0Cadence_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 5),
    _PktcSigDevR0Cadence_Type()
)
pktcSigDevR0Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR0Cadence.setStatus("current")
_PktcSigDevR1Cadence_Type = PktcRingCadence
_PktcSigDevR1Cadence_Object = MibScalar
pktcSigDevR1Cadence = _PktcSigDevR1Cadence_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 6),
    _PktcSigDevR1Cadence_Type()
)
pktcSigDevR1Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR1Cadence.setStatus("current")
_PktcSigDevR2Cadence_Type = PktcRingCadence
_PktcSigDevR2Cadence_Object = MibScalar
pktcSigDevR2Cadence = _PktcSigDevR2Cadence_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 7),
    _PktcSigDevR2Cadence_Type()
)
pktcSigDevR2Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR2Cadence.setStatus("current")
_PktcSigDevR3Cadence_Type = PktcRingCadence
_PktcSigDevR3Cadence_Object = MibScalar
pktcSigDevR3Cadence = _PktcSigDevR3Cadence_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 8),
    _PktcSigDevR3Cadence_Type()
)
pktcSigDevR3Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR3Cadence.setStatus("current")
_PktcSigDevR4Cadence_Type = PktcRingCadence
_PktcSigDevR4Cadence_Object = MibScalar
pktcSigDevR4Cadence = _PktcSigDevR4Cadence_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 9),
    _PktcSigDevR4Cadence_Type()
)
pktcSigDevR4Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR4Cadence.setStatus("current")
_PktcSigDevR5Cadence_Type = PktcRingCadence
_PktcSigDevR5Cadence_Object = MibScalar
pktcSigDevR5Cadence = _PktcSigDevR5Cadence_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 10),
    _PktcSigDevR5Cadence_Type()
)
pktcSigDevR5Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR5Cadence.setStatus("current")
_PktcSigDevR6Cadence_Type = PktcRingCadence
_PktcSigDevR6Cadence_Object = MibScalar
pktcSigDevR6Cadence = _PktcSigDevR6Cadence_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 11),
    _PktcSigDevR6Cadence_Type()
)
pktcSigDevR6Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR6Cadence.setStatus("current")
_PktcSigDevR7Cadence_Type = PktcRingCadence
_PktcSigDevR7Cadence_Object = MibScalar
pktcSigDevR7Cadence = _PktcSigDevR7Cadence_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 12),
    _PktcSigDevR7Cadence_Type()
)
pktcSigDevR7Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR7Cadence.setStatus("current")
_PktcSigDevRgCadence_Type = PktcRingCadence
_PktcSigDevRgCadence_Object = MibScalar
pktcSigDevRgCadence = _PktcSigDevRgCadence_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 13),
    _PktcSigDevRgCadence_Type()
)
pktcSigDevRgCadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevRgCadence.setStatus("current")
_PktcSigDevRsCadence_Type = PktcRingCadence
_PktcSigDevRsCadence_Object = MibScalar
pktcSigDevRsCadence = _PktcSigDevRsCadence_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 14),
    _PktcSigDevRsCadence_Type()
)
pktcSigDevRsCadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevRsCadence.setStatus("current")


class _PktcSigDefCallSigDscp_Type(Dscp):
    """Custom type pktcSigDefCallSigDscp based on Dscp"""
    defaultValue = 0


_PktcSigDefCallSigDscp_Type.__name__ = "Dscp"
_PktcSigDefCallSigDscp_Object = MibScalar
pktcSigDefCallSigDscp = _PktcSigDefCallSigDscp_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 15),
    _PktcSigDefCallSigDscp_Type()
)
pktcSigDefCallSigDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDefCallSigDscp.setStatus("current")


class _PktcSigDefMediaStreamDscp_Type(Dscp):
    """Custom type pktcSigDefMediaStreamDscp based on Dscp"""
    defaultValue = 0


_PktcSigDefMediaStreamDscp_Type.__name__ = "Dscp"
_PktcSigDefMediaStreamDscp_Object = MibScalar
pktcSigDefMediaStreamDscp = _PktcSigDefMediaStreamDscp_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 16),
    _PktcSigDefMediaStreamDscp_Type()
)
pktcSigDefMediaStreamDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDefMediaStreamDscp.setStatus("current")
_PktcSigCapabilityTable_Object = MibTable
pktcSigCapabilityTable = _PktcSigCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 17)
)
if mibBuilder.loadTexts:
    pktcSigCapabilityTable.setStatus("current")
_PktcSigCapabilityEntry_Object = MibTableRow
pktcSigCapabilityEntry = _PktcSigCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 17, 1)
)
pktcSigCapabilityEntry.setIndexNames(
    (0, "PKTC-EXCENTIS-SIG-MIB", "pktcSignalingIndex"),
)
if mibBuilder.loadTexts:
    pktcSigCapabilityEntry.setStatus("current")


class _PktcSignalingIndex_Type(Unsigned32):
    """Custom type pktcSignalingIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PktcSignalingIndex_Type.__name__ = "Unsigned32"
_PktcSignalingIndex_Object = MibTableColumn
pktcSignalingIndex = _PktcSignalingIndex_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 17, 1, 1),
    _PktcSignalingIndex_Type()
)
pktcSignalingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcSignalingIndex.setStatus("current")
_PktcSignalingType_Type = PktcSigType
_PktcSignalingType_Object = MibTableColumn
pktcSignalingType = _PktcSignalingType_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 17, 1, 2),
    _PktcSignalingType_Type()
)
pktcSignalingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSignalingType.setStatus("current")
_PktcSignalingVersion_Type = SnmpAdminString
_PktcSignalingVersion_Object = MibTableColumn
pktcSignalingVersion = _PktcSignalingVersion_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 17, 1, 3),
    _PktcSignalingVersion_Type()
)
pktcSignalingVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSignalingVersion.setStatus("current")
_PktcSignalingVendorExtension_Type = SnmpAdminString
_PktcSignalingVendorExtension_Object = MibTableColumn
pktcSignalingVendorExtension = _PktcSignalingVendorExtension_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 17, 1, 4),
    _PktcSignalingVendorExtension_Type()
)
pktcSignalingVendorExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSignalingVendorExtension.setStatus("current")


class _PktcSigDefNcsReceiveUdpPort_Type(InetPortNumber):
    """Custom type pktcSigDefNcsReceiveUdpPort based on InetPortNumber"""
    defaultValue = 2427

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_PktcSigDefNcsReceiveUdpPort_Type.__name__ = "InetPortNumber"
_PktcSigDefNcsReceiveUdpPort_Object = MibScalar
pktcSigDefNcsReceiveUdpPort = _PktcSigDefNcsReceiveUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 18),
    _PktcSigDefNcsReceiveUdpPort_Type()
)
pktcSigDefNcsReceiveUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDefNcsReceiveUdpPort.setStatus("current")


class _PktcSigPowerRingFrequency_Type(Integer32):
    """Custom type pktcSigPowerRingFrequency based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("f20Hz", 1),
          ("f25Hz", 2),
          ("f33Point33Hz", 3),
          ("f50Hz", 4),
          ("f15Hz", 5),
          ("f16Hz", 6),
          ("f22Hz", 7),
          ("f23Hz", 8),
          ("f45Hz", 9))
    )


_PktcSigPowerRingFrequency_Type.__name__ = "Integer32"
_PktcSigPowerRingFrequency_Object = MibScalar
pktcSigPowerRingFrequency = _PktcSigPowerRingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 19),
    _PktcSigPowerRingFrequency_Type()
)
pktcSigPowerRingFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigPowerRingFrequency.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigPowerRingFrequency.setUnits("Hertz")
_PktcSigPulseSignalTable_Object = MibTable
pktcSigPulseSignalTable = _PktcSigPulseSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 20)
)
if mibBuilder.loadTexts:
    pktcSigPulseSignalTable.setStatus("current")
_PktcSigPulseSignalEntry_Object = MibTableRow
pktcSigPulseSignalEntry = _PktcSigPulseSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 20, 1)
)
pktcSigPulseSignalEntry.setIndexNames(
    (0, "PKTC-EXCENTIS-SIG-MIB", "pktcSigPulseSignalType"),
)
if mibBuilder.loadTexts:
    pktcSigPulseSignalEntry.setStatus("current")


class _PktcSigPulseSignalType_Type(Integer32):
    """Custom type pktcSigPulseSignalType based on Integer32"""
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
        *(("initialRing", 1),
          ("pulseLoopClose", 2),
          ("pulseLoopOpen", 3),
          ("enableMeterPulse", 4),
          ("meterPulseBurst", 5),
          ("pulseNoBattery", 6),
          ("pulseNormalPolarity", 7),
          ("pulseReducedBattery", 8),
          ("pulseReversePolarity", 9))
    )


_PktcSigPulseSignalType_Type.__name__ = "Integer32"
_PktcSigPulseSignalType_Object = MibTableColumn
pktcSigPulseSignalType = _PktcSigPulseSignalType_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 20, 1, 1),
    _PktcSigPulseSignalType_Type()
)
pktcSigPulseSignalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcSigPulseSignalType.setStatus("current")


class _PktcSigPulseSignalFrequency_Type(Integer32):
    """Custom type pktcSigPulseSignalFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("twentyfive", 1),
          ("twelvethousand", 2),
          ("sixteenthousand", 3))
    )


_PktcSigPulseSignalFrequency_Type.__name__ = "Integer32"
_PktcSigPulseSignalFrequency_Object = MibTableColumn
pktcSigPulseSignalFrequency = _PktcSigPulseSignalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 20, 1, 2),
    _PktcSigPulseSignalFrequency_Type()
)
pktcSigPulseSignalFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigPulseSignalFrequency.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigPulseSignalFrequency.setUnits("Hertz")


class _PktcSigPulseSignalDbLevel_Type(TenthdBm):
    """Custom type pktcSigPulseSignalDbLevel based on TenthdBm"""
    defaultValue = -135

    subtypeSpec = TenthdBm.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-350, 0),
    )


_PktcSigPulseSignalDbLevel_Type.__name__ = "TenthdBm"
_PktcSigPulseSignalDbLevel_Object = MibTableColumn
pktcSigPulseSignalDbLevel = _PktcSigPulseSignalDbLevel_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 20, 1, 3),
    _PktcSigPulseSignalDbLevel_Type()
)
pktcSigPulseSignalDbLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigPulseSignalDbLevel.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigPulseSignalDbLevel.setUnits("dBm")


class _PktcSigPulseSignalDuration_Type(Unsigned32):
    """Custom type pktcSigPulseSignalDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_PktcSigPulseSignalDuration_Type.__name__ = "Unsigned32"
_PktcSigPulseSignalDuration_Object = MibTableColumn
pktcSigPulseSignalDuration = _PktcSigPulseSignalDuration_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 20, 1, 4),
    _PktcSigPulseSignalDuration_Type()
)
pktcSigPulseSignalDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigPulseSignalDuration.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigPulseSignalDuration.setUnits("Milliseconds")


class _PktcSigPulseSignalPulseInterval_Type(Unsigned32):
    """Custom type pktcSigPulseSignalPulseInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_PktcSigPulseSignalPulseInterval_Type.__name__ = "Unsigned32"
_PktcSigPulseSignalPulseInterval_Object = MibTableColumn
pktcSigPulseSignalPulseInterval = _PktcSigPulseSignalPulseInterval_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 20, 1, 5),
    _PktcSigPulseSignalPulseInterval_Type()
)
pktcSigPulseSignalPulseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigPulseSignalPulseInterval.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigPulseSignalPulseInterval.setUnits("Milliseconds")
_PktcSigPulseSignalRepeatCount_Type = Unsigned32
_PktcSigPulseSignalRepeatCount_Object = MibTableColumn
pktcSigPulseSignalRepeatCount = _PktcSigPulseSignalRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 20, 1, 6),
    _PktcSigPulseSignalRepeatCount_Type()
)
pktcSigPulseSignalRepeatCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigPulseSignalRepeatCount.setStatus("current")


class _PktcSigDevCIDMode_Type(Integer32):
    """Custom type pktcSigDevCIDMode based on Integer32"""
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
        *(("duringRingingETS", 1),
          ("dtAsETS", 2),
          ("rpAsETS", 3),
          ("lrAsETS", 4),
          ("lrETS", 5))
    )


_PktcSigDevCIDMode_Type.__name__ = "Integer32"
_PktcSigDevCIDMode_Object = MibScalar
pktcSigDevCIDMode = _PktcSigDevCIDMode_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 21),
    _PktcSigDevCIDMode_Type()
)
pktcSigDevCIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevCIDMode.setStatus("current")


class _PktcSigDevCIDFskAfterRing_Type(Unsigned32):
    """Custom type pktcSigDevCIDFskAfterRing based on Unsigned32"""
    defaultValue = 550

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 2000),
    )


_PktcSigDevCIDFskAfterRing_Type.__name__ = "Unsigned32"
_PktcSigDevCIDFskAfterRing_Object = MibScalar
pktcSigDevCIDFskAfterRing = _PktcSigDevCIDFskAfterRing_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 22),
    _PktcSigDevCIDFskAfterRing_Type()
)
pktcSigDevCIDFskAfterRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevCIDFskAfterRing.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevCIDFskAfterRing.setUnits("Milliseconds")


class _PktcSigDevCIDFskAfterDTAS_Type(Unsigned32):
    """Custom type pktcSigDevCIDFskAfterDTAS based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(45, 500),
    )


_PktcSigDevCIDFskAfterDTAS_Type.__name__ = "Unsigned32"
_PktcSigDevCIDFskAfterDTAS_Object = MibScalar
pktcSigDevCIDFskAfterDTAS = _PktcSigDevCIDFskAfterDTAS_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 23),
    _PktcSigDevCIDFskAfterDTAS_Type()
)
pktcSigDevCIDFskAfterDTAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevCIDFskAfterDTAS.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevCIDFskAfterDTAS.setUnits("Milliseconds")


class _PktcSigDevCIDFskAfterRPAS_Type(Unsigned32):
    """Custom type pktcSigDevCIDFskAfterRPAS based on Unsigned32"""
    defaultValue = 650

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 800),
    )


_PktcSigDevCIDFskAfterRPAS_Type.__name__ = "Unsigned32"
_PktcSigDevCIDFskAfterRPAS_Object = MibScalar
pktcSigDevCIDFskAfterRPAS = _PktcSigDevCIDFskAfterRPAS_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 24),
    _PktcSigDevCIDFskAfterRPAS_Type()
)
pktcSigDevCIDFskAfterRPAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevCIDFskAfterRPAS.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevCIDFskAfterRPAS.setUnits("Milliseconds")


class _PktcSigDevCIDRingAfterFSK_Type(Unsigned32):
    """Custom type pktcSigDevCIDRingAfterFSK based on Unsigned32"""
    defaultValue = 250

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_PktcSigDevCIDRingAfterFSK_Type.__name__ = "Unsigned32"
_PktcSigDevCIDRingAfterFSK_Object = MibScalar
pktcSigDevCIDRingAfterFSK = _PktcSigDevCIDRingAfterFSK_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 25),
    _PktcSigDevCIDRingAfterFSK_Type()
)
pktcSigDevCIDRingAfterFSK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevCIDRingAfterFSK.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevCIDRingAfterFSK.setUnits("Milliseconds")


class _PktcSigDevCIDDTASAfterLR_Type(Unsigned32):
    """Custom type pktcSigDevCIDDTASAfterLR based on Unsigned32"""
    defaultValue = 250

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 655),
    )


_PktcSigDevCIDDTASAfterLR_Type.__name__ = "Unsigned32"
_PktcSigDevCIDDTASAfterLR_Object = MibScalar
pktcSigDevCIDDTASAfterLR = _PktcSigDevCIDDTASAfterLR_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 26),
    _PktcSigDevCIDDTASAfterLR_Type()
)
pktcSigDevCIDDTASAfterLR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevCIDDTASAfterLR.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevCIDDTASAfterLR.setUnits("Milliseconds")


class _PktcSigDevVmwiMode_Type(Integer32):
    """Custom type pktcSigDevVmwiMode based on Integer32"""
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
        *(("dtAsETS", 1),
          ("rpAsETS", 2),
          ("lrAsETS", 3),
          ("osi", 4),
          ("lrETS", 5))
    )


_PktcSigDevVmwiMode_Type.__name__ = "Integer32"
_PktcSigDevVmwiMode_Object = MibScalar
pktcSigDevVmwiMode = _PktcSigDevVmwiMode_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 27),
    _PktcSigDevVmwiMode_Type()
)
pktcSigDevVmwiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevVmwiMode.setStatus("current")


class _PktcSigDevVmwiFskAfterDTAS_Type(Unsigned32):
    """Custom type pktcSigDevVmwiFskAfterDTAS based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(45, 500),
    )


_PktcSigDevVmwiFskAfterDTAS_Type.__name__ = "Unsigned32"
_PktcSigDevVmwiFskAfterDTAS_Object = MibScalar
pktcSigDevVmwiFskAfterDTAS = _PktcSigDevVmwiFskAfterDTAS_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 28),
    _PktcSigDevVmwiFskAfterDTAS_Type()
)
pktcSigDevVmwiFskAfterDTAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevVmwiFskAfterDTAS.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevVmwiFskAfterDTAS.setUnits("Milliseconds")


class _PktcSigDevVmwiFskAfterRPAS_Type(Unsigned32):
    """Custom type pktcSigDevVmwiFskAfterRPAS based on Unsigned32"""
    defaultValue = 650

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 800),
    )


_PktcSigDevVmwiFskAfterRPAS_Type.__name__ = "Unsigned32"
_PktcSigDevVmwiFskAfterRPAS_Object = MibScalar
pktcSigDevVmwiFskAfterRPAS = _PktcSigDevVmwiFskAfterRPAS_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 29),
    _PktcSigDevVmwiFskAfterRPAS_Type()
)
pktcSigDevVmwiFskAfterRPAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevVmwiFskAfterRPAS.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevVmwiFskAfterRPAS.setUnits("Milliseconds")


class _PktcSigDevVmwiDTASAfterLR_Type(Unsigned32):
    """Custom type pktcSigDevVmwiDTASAfterLR based on Unsigned32"""
    defaultValue = 250

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 655),
    )


_PktcSigDevVmwiDTASAfterLR_Type.__name__ = "Unsigned32"
_PktcSigDevVmwiDTASAfterLR_Object = MibScalar
pktcSigDevVmwiDTASAfterLR = _PktcSigDevVmwiDTASAfterLR_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 30),
    _PktcSigDevVmwiDTASAfterLR_Type()
)
pktcSigDevVmwiDTASAfterLR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevVmwiDTASAfterLR.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevVmwiDTASAfterLR.setUnits("Milliseconds")
_PktcSigDevRingCadenceTable_Object = MibTable
pktcSigDevRingCadenceTable = _PktcSigDevRingCadenceTable_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 31)
)
if mibBuilder.loadTexts:
    pktcSigDevRingCadenceTable.setStatus("current")
_PktcSigDevRingCadenceEntry_Object = MibTableRow
pktcSigDevRingCadenceEntry = _PktcSigDevRingCadenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 31, 1)
)
pktcSigDevRingCadenceEntry.setIndexNames(
    (0, "PKTC-EXCENTIS-SIG-MIB", "pktcSigDevRingCadenceIndex"),
)
if mibBuilder.loadTexts:
    pktcSigDevRingCadenceEntry.setStatus("current")


class _PktcSigDevRingCadenceIndex_Type(Unsigned32):
    """Custom type pktcSigDevRingCadenceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_PktcSigDevRingCadenceIndex_Type.__name__ = "Unsigned32"
_PktcSigDevRingCadenceIndex_Object = MibTableColumn
pktcSigDevRingCadenceIndex = _PktcSigDevRingCadenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 31, 1, 1),
    _PktcSigDevRingCadenceIndex_Type()
)
pktcSigDevRingCadenceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcSigDevRingCadenceIndex.setStatus("current")
_PktcSigDevRingCadence_Type = PktcRingCadence
_PktcSigDevRingCadence_Object = MibTableColumn
pktcSigDevRingCadence = _PktcSigDevRingCadence_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 31, 1, 2),
    _PktcSigDevRingCadence_Type()
)
pktcSigDevRingCadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevRingCadence.setStatus("current")
_PktcSigDevToneTable_Object = MibTable
pktcSigDevToneTable = _PktcSigDevToneTable_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 32)
)
if mibBuilder.loadTexts:
    pktcSigDevToneTable.setStatus("current")
_PktcSigDevToneEntry_Object = MibTableRow
pktcSigDevToneEntry = _PktcSigDevToneEntry_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 32, 1)
)
pktcSigDevToneEntry.setIndexNames(
    (0, "PKTC-EXCENTIS-SIG-MIB", "pktcSigDevToneType"),
)
if mibBuilder.loadTexts:
    pktcSigDevToneEntry.setStatus("current")


class _PktcSigDevToneType_Type(Integer32):
    """Custom type pktcSigDevToneType based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("busy", 1),
          ("confirmation", 2),
          ("dial", 3),
          ("messageWaiting", 4),
          ("offHookWarning", 5),
          ("ringBack", 6),
          ("reOrder", 7),
          ("stutterdial", 8),
          ("callWaiting1", 9),
          ("callWaiting2", 10),
          ("callWaiting3", 11),
          ("callWaiting4", 12),
          ("alertingSignal", 13),
          ("specialDial", 14),
          ("specialInfo", 15),
          ("release", 16),
          ("congestion", 17),
          ("userDefined1", 18),
          ("userDefined2", 19),
          ("userDefined3", 20),
          ("userDefined4", 21))
    )


_PktcSigDevToneType_Type.__name__ = "Integer32"
_PktcSigDevToneType_Object = MibTableColumn
pktcSigDevToneType = _PktcSigDevToneType_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 32, 1, 1),
    _PktcSigDevToneType_Type()
)
pktcSigDevToneType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcSigDevToneType.setStatus("current")


class _PktcSigDevToneWholeToneRepeatCount_Type(Unsigned32):
    """Custom type pktcSigDevToneWholeToneRepeatCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_PktcSigDevToneWholeToneRepeatCount_Type.__name__ = "Unsigned32"
_PktcSigDevToneWholeToneRepeatCount_Object = MibTableColumn
pktcSigDevToneWholeToneRepeatCount = _PktcSigDevToneWholeToneRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 32, 1, 2),
    _PktcSigDevToneWholeToneRepeatCount_Type()
)
pktcSigDevToneWholeToneRepeatCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevToneWholeToneRepeatCount.setStatus("current")
_PktcSigDevToneSteady_Type = TruthValue
_PktcSigDevToneSteady_Object = MibTableColumn
pktcSigDevToneSteady = _PktcSigDevToneSteady_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 32, 1, 3),
    _PktcSigDevToneSteady_Type()
)
pktcSigDevToneSteady.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevToneSteady.setStatus("current")
_PktcSigDevMultiFreqToneTable_Object = MibTable
pktcSigDevMultiFreqToneTable = _PktcSigDevMultiFreqToneTable_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 33)
)
if mibBuilder.loadTexts:
    pktcSigDevMultiFreqToneTable.setStatus("current")
_PktcSigDevMultiFreqToneEntry_Object = MibTableRow
pktcSigDevMultiFreqToneEntry = _PktcSigDevMultiFreqToneEntry_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 33, 1)
)
pktcSigDevMultiFreqToneEntry.setIndexNames(
    (0, "PKTC-EXCENTIS-SIG-MIB", "pktcSigDevToneType"),
    (0, "PKTC-EXCENTIS-SIG-MIB", "pktcSigDevToneNumber"),
)
if mibBuilder.loadTexts:
    pktcSigDevMultiFreqToneEntry.setStatus("current")


class _PktcSigDevToneNumber_Type(Unsigned32):
    """Custom type pktcSigDevToneNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PktcSigDevToneNumber_Type.__name__ = "Unsigned32"
_PktcSigDevToneNumber_Object = MibTableColumn
pktcSigDevToneNumber = _PktcSigDevToneNumber_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 33, 1, 1),
    _PktcSigDevToneNumber_Type()
)
pktcSigDevToneNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcSigDevToneNumber.setStatus("current")


class _PktcSigDevToneFirstFreqValue_Type(Unsigned32):
    """Custom type pktcSigDevToneFirstFreqValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_PktcSigDevToneFirstFreqValue_Type.__name__ = "Unsigned32"
_PktcSigDevToneFirstFreqValue_Object = MibTableColumn
pktcSigDevToneFirstFreqValue = _PktcSigDevToneFirstFreqValue_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 33, 1, 2),
    _PktcSigDevToneFirstFreqValue_Type()
)
pktcSigDevToneFirstFreqValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevToneFirstFreqValue.setStatus("current")


class _PktcSigDevToneSecondFreqValue_Type(Unsigned32):
    """Custom type pktcSigDevToneSecondFreqValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_PktcSigDevToneSecondFreqValue_Type.__name__ = "Unsigned32"
_PktcSigDevToneSecondFreqValue_Object = MibTableColumn
pktcSigDevToneSecondFreqValue = _PktcSigDevToneSecondFreqValue_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 33, 1, 3),
    _PktcSigDevToneSecondFreqValue_Type()
)
pktcSigDevToneSecondFreqValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevToneSecondFreqValue.setStatus("current")


class _PktcSigDevToneThirdFreqValue_Type(Unsigned32):
    """Custom type pktcSigDevToneThirdFreqValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_PktcSigDevToneThirdFreqValue_Type.__name__ = "Unsigned32"
_PktcSigDevToneThirdFreqValue_Object = MibTableColumn
pktcSigDevToneThirdFreqValue = _PktcSigDevToneThirdFreqValue_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 33, 1, 4),
    _PktcSigDevToneThirdFreqValue_Type()
)
pktcSigDevToneThirdFreqValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevToneThirdFreqValue.setStatus("current")


class _PktcSigDevToneFourthFreqValue_Type(Unsigned32):
    """Custom type pktcSigDevToneFourthFreqValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_PktcSigDevToneFourthFreqValue_Type.__name__ = "Unsigned32"
_PktcSigDevToneFourthFreqValue_Object = MibTableColumn
pktcSigDevToneFourthFreqValue = _PktcSigDevToneFourthFreqValue_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 33, 1, 5),
    _PktcSigDevToneFourthFreqValue_Type()
)
pktcSigDevToneFourthFreqValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevToneFourthFreqValue.setStatus("current")


class _PktcSigDevToneFreqMode_Type(Integer32):
    """Custom type pktcSigDevToneFreqMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("firstModulatedBySecond", 1),
          ("summation", 2))
    )


_PktcSigDevToneFreqMode_Type.__name__ = "Integer32"
_PktcSigDevToneFreqMode_Object = MibTableColumn
pktcSigDevToneFreqMode = _PktcSigDevToneFreqMode_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 33, 1, 6),
    _PktcSigDevToneFreqMode_Type()
)
pktcSigDevToneFreqMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevToneFreqMode.setStatus("current")


class _PktcSigDevToneFreqAmpModePrtg_Type(Integer32):
    """Custom type pktcSigDevToneFreqAmpModePrtg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PktcSigDevToneFreqAmpModePrtg_Type.__name__ = "Integer32"
_PktcSigDevToneFreqAmpModePrtg_Object = MibTableColumn
pktcSigDevToneFreqAmpModePrtg = _PktcSigDevToneFreqAmpModePrtg_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 33, 1, 7),
    _PktcSigDevToneFreqAmpModePrtg_Type()
)
pktcSigDevToneFreqAmpModePrtg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevToneFreqAmpModePrtg.setStatus("current")


class _PktcSigDevToneDbLevel_Type(TenthdBm):
    """Custom type pktcSigDevToneDbLevel based on TenthdBm"""
    defaultValue = -40

    subtypeSpec = TenthdBm.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-250, -30),
    )


_PktcSigDevToneDbLevel_Type.__name__ = "TenthdBm"
_PktcSigDevToneDbLevel_Object = MibTableColumn
pktcSigDevToneDbLevel = _PktcSigDevToneDbLevel_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 33, 1, 8),
    _PktcSigDevToneDbLevel_Type()
)
pktcSigDevToneDbLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevToneDbLevel.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevToneDbLevel.setUnits("dBm")


class _PktcSigDevToneFreqOnDuration_Type(Unsigned32):
    """Custom type pktcSigDevToneFreqOnDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_PktcSigDevToneFreqOnDuration_Type.__name__ = "Unsigned32"
_PktcSigDevToneFreqOnDuration_Object = MibTableColumn
pktcSigDevToneFreqOnDuration = _PktcSigDevToneFreqOnDuration_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 33, 1, 9),
    _PktcSigDevToneFreqOnDuration_Type()
)
pktcSigDevToneFreqOnDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevToneFreqOnDuration.setStatus("current")


class _PktcSigDevToneFreqOffDuration_Type(Unsigned32):
    """Custom type pktcSigDevToneFreqOffDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_PktcSigDevToneFreqOffDuration_Type.__name__ = "Unsigned32"
_PktcSigDevToneFreqOffDuration_Object = MibTableColumn
pktcSigDevToneFreqOffDuration = _PktcSigDevToneFreqOffDuration_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 33, 1, 10),
    _PktcSigDevToneFreqOffDuration_Type()
)
pktcSigDevToneFreqOffDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevToneFreqOffDuration.setStatus("current")


class _PktcSigDevToneFreqRepeatCount_Type(Unsigned32):
    """Custom type pktcSigDevToneFreqRepeatCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_PktcSigDevToneFreqRepeatCount_Type.__name__ = "Unsigned32"
_PktcSigDevToneFreqRepeatCount_Object = MibTableColumn
pktcSigDevToneFreqRepeatCount = _PktcSigDevToneFreqRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 1, 33, 1, 11),
    _PktcSigDevToneFreqRepeatCount_Type()
)
pktcSigDevToneFreqRepeatCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevToneFreqRepeatCount.setStatus("current")
_PktcNcsEndPntConfigObjects_ObjectIdentity = ObjectIdentity
pktcNcsEndPntConfigObjects = _PktcNcsEndPntConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2)
)
_PktcNcsEndPntConfigTable_Object = MibTable
pktcNcsEndPntConfigTable = _PktcNcsEndPntConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigTable.setStatus("current")
_PktcNcsEndPntConfigEntry_Object = MibTableRow
pktcNcsEndPntConfigEntry = _PktcNcsEndPntConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1)
)
pktcNcsEndPntConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigEntry.setStatus("current")


class _PktcNcsEndPntConfigCallAgentId_Type(SnmpAdminString):
    """Custom type pktcNcsEndPntConfigCallAgentId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 255),
    )


_PktcNcsEndPntConfigCallAgentId_Type.__name__ = "SnmpAdminString"
_PktcNcsEndPntConfigCallAgentId_Object = MibTableColumn
pktcNcsEndPntConfigCallAgentId = _PktcNcsEndPntConfigCallAgentId_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 1),
    _PktcNcsEndPntConfigCallAgentId_Type()
)
pktcNcsEndPntConfigCallAgentId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigCallAgentId.setStatus("current")


class _PktcNcsEndPntConfigCallAgentUdpPort_Type(InetPortNumber):
    """Custom type pktcNcsEndPntConfigCallAgentUdpPort based on InetPortNumber"""
    defaultValue = 2727

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_PktcNcsEndPntConfigCallAgentUdpPort_Type.__name__ = "InetPortNumber"
_PktcNcsEndPntConfigCallAgentUdpPort_Object = MibTableColumn
pktcNcsEndPntConfigCallAgentUdpPort = _PktcNcsEndPntConfigCallAgentUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 2),
    _PktcNcsEndPntConfigCallAgentUdpPort_Type()
)
pktcNcsEndPntConfigCallAgentUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigCallAgentUdpPort.setStatus("current")


class _PktcNcsEndPntConfigPartialDialTO_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigPartialDialTO based on Unsigned32"""
    defaultValue = 16


_PktcNcsEndPntConfigPartialDialTO_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigPartialDialTO_Object = MibTableColumn
pktcNcsEndPntConfigPartialDialTO = _PktcNcsEndPntConfigPartialDialTO_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 3),
    _PktcNcsEndPntConfigPartialDialTO_Type()
)
pktcNcsEndPntConfigPartialDialTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigPartialDialTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigPartialDialTO.setUnits("seconds")


class _PktcNcsEndPntConfigCriticalDialTO_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigCriticalDialTO based on Unsigned32"""
    defaultValue = 4


_PktcNcsEndPntConfigCriticalDialTO_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigCriticalDialTO_Object = MibTableColumn
pktcNcsEndPntConfigCriticalDialTO = _PktcNcsEndPntConfigCriticalDialTO_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 4),
    _PktcNcsEndPntConfigCriticalDialTO_Type()
)
pktcNcsEndPntConfigCriticalDialTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigCriticalDialTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigCriticalDialTO.setUnits("seconds")


class _PktcNcsEndPntConfigBusyToneTO_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigBusyToneTO based on Unsigned32"""
    defaultValue = 30


_PktcNcsEndPntConfigBusyToneTO_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigBusyToneTO_Object = MibTableColumn
pktcNcsEndPntConfigBusyToneTO = _PktcNcsEndPntConfigBusyToneTO_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 5),
    _PktcNcsEndPntConfigBusyToneTO_Type()
)
pktcNcsEndPntConfigBusyToneTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigBusyToneTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigBusyToneTO.setUnits("seconds")


class _PktcNcsEndPntConfigDialToneTO_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigDialToneTO based on Unsigned32"""
    defaultValue = 16


_PktcNcsEndPntConfigDialToneTO_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigDialToneTO_Object = MibTableColumn
pktcNcsEndPntConfigDialToneTO = _PktcNcsEndPntConfigDialToneTO_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 6),
    _PktcNcsEndPntConfigDialToneTO_Type()
)
pktcNcsEndPntConfigDialToneTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigDialToneTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigDialToneTO.setUnits("seconds")


class _PktcNcsEndPntConfigMessageWaitingTO_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigMessageWaitingTO based on Unsigned32"""
    defaultValue = 16


_PktcNcsEndPntConfigMessageWaitingTO_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigMessageWaitingTO_Object = MibTableColumn
pktcNcsEndPntConfigMessageWaitingTO = _PktcNcsEndPntConfigMessageWaitingTO_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 7),
    _PktcNcsEndPntConfigMessageWaitingTO_Type()
)
pktcNcsEndPntConfigMessageWaitingTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMessageWaitingTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMessageWaitingTO.setUnits("seconds")


class _PktcNcsEndPntConfigOffHookWarnToneTO_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigOffHookWarnToneTO based on Unsigned32"""
    defaultValue = 0


_PktcNcsEndPntConfigOffHookWarnToneTO_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigOffHookWarnToneTO_Object = MibTableColumn
pktcNcsEndPntConfigOffHookWarnToneTO = _PktcNcsEndPntConfigOffHookWarnToneTO_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 8),
    _PktcNcsEndPntConfigOffHookWarnToneTO_Type()
)
pktcNcsEndPntConfigOffHookWarnToneTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigOffHookWarnToneTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigOffHookWarnToneTO.setUnits("seconds")


class _PktcNcsEndPntConfigRingingTO_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigRingingTO based on Unsigned32"""
    defaultValue = 180


_PktcNcsEndPntConfigRingingTO_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigRingingTO_Object = MibTableColumn
pktcNcsEndPntConfigRingingTO = _PktcNcsEndPntConfigRingingTO_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 9),
    _PktcNcsEndPntConfigRingingTO_Type()
)
pktcNcsEndPntConfigRingingTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigRingingTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigRingingTO.setUnits("seconds")


class _PktcNcsEndPntConfigRingBackTO_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigRingBackTO based on Unsigned32"""
    defaultValue = 180


_PktcNcsEndPntConfigRingBackTO_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigRingBackTO_Object = MibTableColumn
pktcNcsEndPntConfigRingBackTO = _PktcNcsEndPntConfigRingBackTO_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 10),
    _PktcNcsEndPntConfigRingBackTO_Type()
)
pktcNcsEndPntConfigRingBackTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigRingBackTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigRingBackTO.setUnits("seconds")


class _PktcNcsEndPntConfigReorderToneTO_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigReorderToneTO based on Unsigned32"""
    defaultValue = 30


_PktcNcsEndPntConfigReorderToneTO_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigReorderToneTO_Object = MibTableColumn
pktcNcsEndPntConfigReorderToneTO = _PktcNcsEndPntConfigReorderToneTO_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 11),
    _PktcNcsEndPntConfigReorderToneTO_Type()
)
pktcNcsEndPntConfigReorderToneTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigReorderToneTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigReorderToneTO.setUnits("seconds")


class _PktcNcsEndPntConfigStutterDialToneTO_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigStutterDialToneTO based on Unsigned32"""
    defaultValue = 16


_PktcNcsEndPntConfigStutterDialToneTO_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigStutterDialToneTO_Object = MibTableColumn
pktcNcsEndPntConfigStutterDialToneTO = _PktcNcsEndPntConfigStutterDialToneTO_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 12),
    _PktcNcsEndPntConfigStutterDialToneTO_Type()
)
pktcNcsEndPntConfigStutterDialToneTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigStutterDialToneTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigStutterDialToneTO.setUnits("seconds")


class _PktcNcsEndPntConfigTSMax_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigTSMax based on Unsigned32"""
    defaultValue = 20


_PktcNcsEndPntConfigTSMax_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigTSMax_Object = MibTableColumn
pktcNcsEndPntConfigTSMax = _PktcNcsEndPntConfigTSMax_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 13),
    _PktcNcsEndPntConfigTSMax_Type()
)
pktcNcsEndPntConfigTSMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigTSMax.setStatus("current")


class _PktcNcsEndPntConfigMax1_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigMax1 based on Unsigned32"""
    defaultValue = 5


_PktcNcsEndPntConfigMax1_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigMax1_Object = MibTableColumn
pktcNcsEndPntConfigMax1 = _PktcNcsEndPntConfigMax1_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 14),
    _PktcNcsEndPntConfigMax1_Type()
)
pktcNcsEndPntConfigMax1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMax1.setStatus("current")


class _PktcNcsEndPntConfigMax2_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigMax2 based on Unsigned32"""
    defaultValue = 7


_PktcNcsEndPntConfigMax2_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigMax2_Object = MibTableColumn
pktcNcsEndPntConfigMax2 = _PktcNcsEndPntConfigMax2_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 15),
    _PktcNcsEndPntConfigMax2_Type()
)
pktcNcsEndPntConfigMax2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMax2.setStatus("current")


class _PktcNcsEndPntConfigMax1QEnable_Type(TruthValue):
    """Custom type pktcNcsEndPntConfigMax1QEnable based on TruthValue"""
    defaultValue = 1


_PktcNcsEndPntConfigMax1QEnable_Type.__name__ = "TruthValue"
_PktcNcsEndPntConfigMax1QEnable_Object = MibTableColumn
pktcNcsEndPntConfigMax1QEnable = _PktcNcsEndPntConfigMax1QEnable_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 16),
    _PktcNcsEndPntConfigMax1QEnable_Type()
)
pktcNcsEndPntConfigMax1QEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMax1QEnable.setStatus("current")


class _PktcNcsEndPntConfigMax2QEnable_Type(TruthValue):
    """Custom type pktcNcsEndPntConfigMax2QEnable based on TruthValue"""
    defaultValue = 1


_PktcNcsEndPntConfigMax2QEnable_Type.__name__ = "TruthValue"
_PktcNcsEndPntConfigMax2QEnable_Object = MibTableColumn
pktcNcsEndPntConfigMax2QEnable = _PktcNcsEndPntConfigMax2QEnable_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 17),
    _PktcNcsEndPntConfigMax2QEnable_Type()
)
pktcNcsEndPntConfigMax2QEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMax2QEnable.setStatus("current")


class _PktcNcsEndPntConfigMWD_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigMWD based on Unsigned32"""
    defaultValue = 600


_PktcNcsEndPntConfigMWD_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigMWD_Object = MibTableColumn
pktcNcsEndPntConfigMWD = _PktcNcsEndPntConfigMWD_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 18),
    _PktcNcsEndPntConfigMWD_Type()
)
pktcNcsEndPntConfigMWD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMWD.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMWD.setUnits("seconds")


class _PktcNcsEndPntConfigTdinit_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigTdinit based on Unsigned32"""
    defaultValue = 15


_PktcNcsEndPntConfigTdinit_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigTdinit_Object = MibTableColumn
pktcNcsEndPntConfigTdinit = _PktcNcsEndPntConfigTdinit_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 19),
    _PktcNcsEndPntConfigTdinit_Type()
)
pktcNcsEndPntConfigTdinit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigTdinit.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigTdinit.setUnits("seconds")


class _PktcNcsEndPntConfigTdmin_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigTdmin based on Unsigned32"""
    defaultValue = 15


_PktcNcsEndPntConfigTdmin_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigTdmin_Object = MibTableColumn
pktcNcsEndPntConfigTdmin = _PktcNcsEndPntConfigTdmin_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 20),
    _PktcNcsEndPntConfigTdmin_Type()
)
pktcNcsEndPntConfigTdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigTdmin.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigTdmin.setUnits("seconds")


class _PktcNcsEndPntConfigTdmax_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigTdmax based on Unsigned32"""
    defaultValue = 600


_PktcNcsEndPntConfigTdmax_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigTdmax_Object = MibTableColumn
pktcNcsEndPntConfigTdmax = _PktcNcsEndPntConfigTdmax_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 21),
    _PktcNcsEndPntConfigTdmax_Type()
)
pktcNcsEndPntConfigTdmax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigTdmax.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigTdmax.setUnits("seconds")


class _PktcNcsEndPntConfigRtoMax_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigRtoMax based on Unsigned32"""
    defaultValue = 4


_PktcNcsEndPntConfigRtoMax_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigRtoMax_Object = MibTableColumn
pktcNcsEndPntConfigRtoMax = _PktcNcsEndPntConfigRtoMax_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 22),
    _PktcNcsEndPntConfigRtoMax_Type()
)
pktcNcsEndPntConfigRtoMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigRtoMax.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigRtoMax.setUnits("seconds")


class _PktcNcsEndPntConfigRtoInit_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigRtoInit based on Unsigned32"""
    defaultValue = 200


_PktcNcsEndPntConfigRtoInit_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigRtoInit_Object = MibTableColumn
pktcNcsEndPntConfigRtoInit = _PktcNcsEndPntConfigRtoInit_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 23),
    _PktcNcsEndPntConfigRtoInit_Type()
)
pktcNcsEndPntConfigRtoInit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigRtoInit.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigRtoInit.setUnits("milliseconds")


class _PktcNcsEndPntConfigLongDurationKeepAlive_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigLongDurationKeepAlive based on Unsigned32"""
    defaultValue = 60


_PktcNcsEndPntConfigLongDurationKeepAlive_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigLongDurationKeepAlive_Object = MibTableColumn
pktcNcsEndPntConfigLongDurationKeepAlive = _PktcNcsEndPntConfigLongDurationKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 24),
    _PktcNcsEndPntConfigLongDurationKeepAlive_Type()
)
pktcNcsEndPntConfigLongDurationKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigLongDurationKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigLongDurationKeepAlive.setUnits("minutes")


class _PktcNcsEndPntConfigThist_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigThist based on Unsigned32"""
    defaultValue = 30


_PktcNcsEndPntConfigThist_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigThist_Object = MibTableColumn
pktcNcsEndPntConfigThist = _PktcNcsEndPntConfigThist_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 25),
    _PktcNcsEndPntConfigThist_Type()
)
pktcNcsEndPntConfigThist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigThist.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigThist.setUnits("seconds")
_PktcNcsEndPntConfigStatus_Type = RowStatus
_PktcNcsEndPntConfigStatus_Object = MibTableColumn
pktcNcsEndPntConfigStatus = _PktcNcsEndPntConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 26),
    _PktcNcsEndPntConfigStatus_Type()
)
pktcNcsEndPntConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigStatus.setStatus("current")


class _PktcNcsEndPntConfigCallWaitingMaxRep_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigCallWaitingMaxRep based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PktcNcsEndPntConfigCallWaitingMaxRep_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigCallWaitingMaxRep_Object = MibTableColumn
pktcNcsEndPntConfigCallWaitingMaxRep = _PktcNcsEndPntConfigCallWaitingMaxRep_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 27),
    _PktcNcsEndPntConfigCallWaitingMaxRep_Type()
)
pktcNcsEndPntConfigCallWaitingMaxRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigCallWaitingMaxRep.setStatus("current")


class _PktcNcsEndPntConfigCallWaitingDelay_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigCallWaitingDelay based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PktcNcsEndPntConfigCallWaitingDelay_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigCallWaitingDelay_Object = MibTableColumn
pktcNcsEndPntConfigCallWaitingDelay = _PktcNcsEndPntConfigCallWaitingDelay_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 28),
    _PktcNcsEndPntConfigCallWaitingDelay_Type()
)
pktcNcsEndPntConfigCallWaitingDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigCallWaitingDelay.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigCallWaitingDelay.setUnits("seconds")
_PktcNcsEndPntStatusCallIpAddressType_Type = InetAddressType
_PktcNcsEndPntStatusCallIpAddressType_Object = MibTableColumn
pktcNcsEndPntStatusCallIpAddressType = _PktcNcsEndPntStatusCallIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 29),
    _PktcNcsEndPntStatusCallIpAddressType_Type()
)
pktcNcsEndPntStatusCallIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcNcsEndPntStatusCallIpAddressType.setStatus("current")
_PktcNcsEndPntStatusCallIpAddress_Type = InetAddress
_PktcNcsEndPntStatusCallIpAddress_Object = MibTableColumn
pktcNcsEndPntStatusCallIpAddress = _PktcNcsEndPntStatusCallIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 30),
    _PktcNcsEndPntStatusCallIpAddress_Type()
)
pktcNcsEndPntStatusCallIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcNcsEndPntStatusCallIpAddress.setStatus("current")


class _PktcNcsEndPntStatusError_Type(Integer32):
    """Custom type pktcNcsEndPntStatusError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("noSecurityAssociation", 2),
          ("disconnected", 3))
    )


_PktcNcsEndPntStatusError_Type.__name__ = "Integer32"
_PktcNcsEndPntStatusError_Object = MibTableColumn
pktcNcsEndPntStatusError = _PktcNcsEndPntStatusError_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 31),
    _PktcNcsEndPntStatusError_Type()
)
pktcNcsEndPntStatusError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcNcsEndPntStatusError.setStatus("current")


class _PktcNcsEndPntConfigMinHookFlash_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigMinHookFlash based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1550),
    )


_PktcNcsEndPntConfigMinHookFlash_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigMinHookFlash_Object = MibTableColumn
pktcNcsEndPntConfigMinHookFlash = _PktcNcsEndPntConfigMinHookFlash_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 32),
    _PktcNcsEndPntConfigMinHookFlash_Type()
)
pktcNcsEndPntConfigMinHookFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMinHookFlash.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMinHookFlash.setUnits("Milliseconds")


class _PktcNcsEndPntConfigMaxHookFlash_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigMaxHookFlash based on Unsigned32"""
    defaultValue = 800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1550),
    )


_PktcNcsEndPntConfigMaxHookFlash_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigMaxHookFlash_Object = MibTableColumn
pktcNcsEndPntConfigMaxHookFlash = _PktcNcsEndPntConfigMaxHookFlash_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 33),
    _PktcNcsEndPntConfigMaxHookFlash_Type()
)
pktcNcsEndPntConfigMaxHookFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMaxHookFlash.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMaxHookFlash.setUnits("Milliseconds")


class _PktcNcsEndPntConfigPulseDialInterdigitTime_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigPulseDialInterdigitTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1500),
    )


_PktcNcsEndPntConfigPulseDialInterdigitTime_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigPulseDialInterdigitTime_Object = MibTableColumn
pktcNcsEndPntConfigPulseDialInterdigitTime = _PktcNcsEndPntConfigPulseDialInterdigitTime_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 34),
    _PktcNcsEndPntConfigPulseDialInterdigitTime_Type()
)
pktcNcsEndPntConfigPulseDialInterdigitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigPulseDialInterdigitTime.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigPulseDialInterdigitTime.setUnits("Milliseconds")


class _PktcNcsEndPntConfigPulseDialMinMakeTime_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigPulseDialMinMakeTime based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 200),
    )


_PktcNcsEndPntConfigPulseDialMinMakeTime_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigPulseDialMinMakeTime_Object = MibTableColumn
pktcNcsEndPntConfigPulseDialMinMakeTime = _PktcNcsEndPntConfigPulseDialMinMakeTime_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 35),
    _PktcNcsEndPntConfigPulseDialMinMakeTime_Type()
)
pktcNcsEndPntConfigPulseDialMinMakeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigPulseDialMinMakeTime.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigPulseDialMinMakeTime.setUnits("Milliseconds")


class _PktcNcsEndPntConfigPulseDialMaxMakeTime_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigPulseDialMaxMakeTime based on Unsigned32"""
    defaultValue = 55

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 200),
    )


_PktcNcsEndPntConfigPulseDialMaxMakeTime_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigPulseDialMaxMakeTime_Object = MibTableColumn
pktcNcsEndPntConfigPulseDialMaxMakeTime = _PktcNcsEndPntConfigPulseDialMaxMakeTime_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 36),
    _PktcNcsEndPntConfigPulseDialMaxMakeTime_Type()
)
pktcNcsEndPntConfigPulseDialMaxMakeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigPulseDialMaxMakeTime.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigPulseDialMaxMakeTime.setUnits("Milliseconds")


class _PktcNcsEndPntConfigPulseDialMinBreakTime_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigPulseDialMinBreakTime based on Unsigned32"""
    defaultValue = 45

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 200),
    )


_PktcNcsEndPntConfigPulseDialMinBreakTime_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigPulseDialMinBreakTime_Object = MibTableColumn
pktcNcsEndPntConfigPulseDialMinBreakTime = _PktcNcsEndPntConfigPulseDialMinBreakTime_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 37),
    _PktcNcsEndPntConfigPulseDialMinBreakTime_Type()
)
pktcNcsEndPntConfigPulseDialMinBreakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigPulseDialMinBreakTime.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigPulseDialMinBreakTime.setUnits("Milliseconds")


class _PktcNcsEndPntConfigPulseDialMaxBreakTime_Type(Unsigned32):
    """Custom type pktcNcsEndPntConfigPulseDialMaxBreakTime based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 200),
    )


_PktcNcsEndPntConfigPulseDialMaxBreakTime_Type.__name__ = "Unsigned32"
_PktcNcsEndPntConfigPulseDialMaxBreakTime_Object = MibTableColumn
pktcNcsEndPntConfigPulseDialMaxBreakTime = _PktcNcsEndPntConfigPulseDialMaxBreakTime_Object(
    (1, 3, 6, 1, 4, 1, 7432, 2, 1, 2, 1, 1, 38),
    _PktcNcsEndPntConfigPulseDialMaxBreakTime_Type()
)
pktcNcsEndPntConfigPulseDialMaxBreakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigPulseDialMaxBreakTime.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigPulseDialMaxBreakTime.setUnits("Milliseconds")
_PktcSigConformance_ObjectIdentity = ObjectIdentity
pktcSigConformance = _PktcSigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7432, 2, 2)
)
_PktcSigCompliances_ObjectIdentity = ObjectIdentity
pktcSigCompliances = _PktcSigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7432, 2, 2, 1)
)
_PktcSigGroups_ObjectIdentity = ObjectIdentity
pktcSigGroups = _PktcSigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7432, 2, 2, 2)
)

# Managed Objects groups

pktcSigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7432, 2, 2, 2, 1)
)
pktcSigGroup.setObjects(
      *(("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevCodecMax"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevEchoCancellation"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevSilenceSuppression"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevR0Cadence"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevR1Cadence"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevR2Cadence"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevR3Cadence"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevR4Cadence"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevR5Cadence"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevR6Cadence"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevR7Cadence"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevRgCadence"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevRsCadence"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDefCallSigDscp"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDefMediaStreamDscp"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevVmwiMode"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSignalingType"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSignalingVersion"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSignalingVendorExtension"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDefNcsReceiveUdpPort"))
)
if mibBuilder.loadTexts:
    pktcSigGroup.setStatus("current")

pktcNcsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7432, 2, 2, 2, 2)
)
pktcNcsGroup.setObjects(
      *(("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigCallAgentId"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigCallAgentUdpPort"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigPartialDialTO"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigCriticalDialTO"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigBusyToneTO"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigDialToneTO"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigMessageWaitingTO"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigOffHookWarnToneTO"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigRingingTO"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigRingBackTO"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigReorderToneTO"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigStutterDialToneTO"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigTSMax"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigMax1"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigMax2"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigMax1QEnable"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigMax2QEnable"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigMWD"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigTdinit"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigTdmin"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigTdmax"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigRtoMax"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigRtoInit"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigLongDurationKeepAlive"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigThist"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigStatus"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigCallWaitingMaxRep"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigCallWaitingDelay"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntStatusCallIpAddressType"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntStatusCallIpAddress"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntStatusError"))
)
if mibBuilder.loadTexts:
    pktcNcsGroup.setStatus("current")

pktcInternationalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7432, 2, 2, 2, 3)
)
pktcInternationalGroup.setObjects(
      *(("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigMinHookFlash"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigMaxHookFlash"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigPulseDialInterdigitTime"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigPulseDialMinMakeTime"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigPulseDialMaxMakeTime"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigPulseDialMinBreakTime"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsEndPntConfigPulseDialMaxBreakTime"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevRingCadence"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevCallerIdSigProtocol"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevCIDMode"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevCIDFskAfterRing"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevCIDFskAfterDTAS"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevCIDFskAfterRPAS"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevCIDRingAfterFSK"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevCIDDTASAfterLR"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevVmwiFskAfterDTAS"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevVmwiFskAfterRPAS"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevVmwiDTASAfterLR"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigPowerRingFrequency"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigPulseSignalFrequency"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigPulseSignalDbLevel"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigPulseSignalDuration"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigPulseSignalPulseInterval"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigPulseSignalRepeatCount"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevToneDbLevel"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevToneWholeToneRepeatCount"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevToneSteady"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevToneFirstFreqValue"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevToneSecondFreqValue"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevToneThirdFreqValue"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevToneFourthFreqValue"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevToneFreqMode"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevToneFreqAmpModePrtg"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevToneFreqOnDuration"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevToneFreqOffDuration"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcSigDevToneFreqRepeatCount"))
)
if mibBuilder.loadTexts:
    pktcInternationalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcSigBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7432, 2, 2, 1, 1)
)
pktcSigBasicCompliance.setObjects(
      *(("PKTC-EXCENTIS-SIG-MIB", "pktcSigGroup"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcNcsGroup"),
        ("PKTC-EXCENTIS-SIG-MIB", "pktcInternationalGroup"))
)
if mibBuilder.loadTexts:
    pktcSigBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKTC-EXCENTIS-SIG-MIB",
    **{"TenthdBm": TenthdBm,
       "PktcCodecType": PktcCodecType,
       "PktcRingCadence": PktcRingCadence,
       "PktcSigType": PktcSigType,
       "pktcExcentisSigMib": pktcExcentisSigMib,
       "pktcSigNotification": pktcSigNotification,
       "pktcSigMibObjects": pktcSigMibObjects,
       "pktcSigDevConfigObjects": pktcSigDevConfigObjects,
       "pktcSigDevCodecTable": pktcSigDevCodecTable,
       "pktcSigDevCodecEntry": pktcSigDevCodecEntry,
       "pktcSigDevCodecComboIndex": pktcSigDevCodecComboIndex,
       "pktcSigDevCodecType": pktcSigDevCodecType,
       "pktcSigDevCodecMax": pktcSigDevCodecMax,
       "pktcSigDevEchoCancellation": pktcSigDevEchoCancellation,
       "pktcSigDevSilenceSuppression": pktcSigDevSilenceSuppression,
       "pktcSigDevCallerIdSigProtocol": pktcSigDevCallerIdSigProtocol,
       "pktcSigDevR0Cadence": pktcSigDevR0Cadence,
       "pktcSigDevR1Cadence": pktcSigDevR1Cadence,
       "pktcSigDevR2Cadence": pktcSigDevR2Cadence,
       "pktcSigDevR3Cadence": pktcSigDevR3Cadence,
       "pktcSigDevR4Cadence": pktcSigDevR4Cadence,
       "pktcSigDevR5Cadence": pktcSigDevR5Cadence,
       "pktcSigDevR6Cadence": pktcSigDevR6Cadence,
       "pktcSigDevR7Cadence": pktcSigDevR7Cadence,
       "pktcSigDevRgCadence": pktcSigDevRgCadence,
       "pktcSigDevRsCadence": pktcSigDevRsCadence,
       "pktcSigDefCallSigDscp": pktcSigDefCallSigDscp,
       "pktcSigDefMediaStreamDscp": pktcSigDefMediaStreamDscp,
       "pktcSigCapabilityTable": pktcSigCapabilityTable,
       "pktcSigCapabilityEntry": pktcSigCapabilityEntry,
       "pktcSignalingIndex": pktcSignalingIndex,
       "pktcSignalingType": pktcSignalingType,
       "pktcSignalingVersion": pktcSignalingVersion,
       "pktcSignalingVendorExtension": pktcSignalingVendorExtension,
       "pktcSigDefNcsReceiveUdpPort": pktcSigDefNcsReceiveUdpPort,
       "pktcSigPowerRingFrequency": pktcSigPowerRingFrequency,
       "pktcSigPulseSignalTable": pktcSigPulseSignalTable,
       "pktcSigPulseSignalEntry": pktcSigPulseSignalEntry,
       "pktcSigPulseSignalType": pktcSigPulseSignalType,
       "pktcSigPulseSignalFrequency": pktcSigPulseSignalFrequency,
       "pktcSigPulseSignalDbLevel": pktcSigPulseSignalDbLevel,
       "pktcSigPulseSignalDuration": pktcSigPulseSignalDuration,
       "pktcSigPulseSignalPulseInterval": pktcSigPulseSignalPulseInterval,
       "pktcSigPulseSignalRepeatCount": pktcSigPulseSignalRepeatCount,
       "pktcSigDevCIDMode": pktcSigDevCIDMode,
       "pktcSigDevCIDFskAfterRing": pktcSigDevCIDFskAfterRing,
       "pktcSigDevCIDFskAfterDTAS": pktcSigDevCIDFskAfterDTAS,
       "pktcSigDevCIDFskAfterRPAS": pktcSigDevCIDFskAfterRPAS,
       "pktcSigDevCIDRingAfterFSK": pktcSigDevCIDRingAfterFSK,
       "pktcSigDevCIDDTASAfterLR": pktcSigDevCIDDTASAfterLR,
       "pktcSigDevVmwiMode": pktcSigDevVmwiMode,
       "pktcSigDevVmwiFskAfterDTAS": pktcSigDevVmwiFskAfterDTAS,
       "pktcSigDevVmwiFskAfterRPAS": pktcSigDevVmwiFskAfterRPAS,
       "pktcSigDevVmwiDTASAfterLR": pktcSigDevVmwiDTASAfterLR,
       "pktcSigDevRingCadenceTable": pktcSigDevRingCadenceTable,
       "pktcSigDevRingCadenceEntry": pktcSigDevRingCadenceEntry,
       "pktcSigDevRingCadenceIndex": pktcSigDevRingCadenceIndex,
       "pktcSigDevRingCadence": pktcSigDevRingCadence,
       "pktcSigDevToneTable": pktcSigDevToneTable,
       "pktcSigDevToneEntry": pktcSigDevToneEntry,
       "pktcSigDevToneType": pktcSigDevToneType,
       "pktcSigDevToneWholeToneRepeatCount": pktcSigDevToneWholeToneRepeatCount,
       "pktcSigDevToneSteady": pktcSigDevToneSteady,
       "pktcSigDevMultiFreqToneTable": pktcSigDevMultiFreqToneTable,
       "pktcSigDevMultiFreqToneEntry": pktcSigDevMultiFreqToneEntry,
       "pktcSigDevToneNumber": pktcSigDevToneNumber,
       "pktcSigDevToneFirstFreqValue": pktcSigDevToneFirstFreqValue,
       "pktcSigDevToneSecondFreqValue": pktcSigDevToneSecondFreqValue,
       "pktcSigDevToneThirdFreqValue": pktcSigDevToneThirdFreqValue,
       "pktcSigDevToneFourthFreqValue": pktcSigDevToneFourthFreqValue,
       "pktcSigDevToneFreqMode": pktcSigDevToneFreqMode,
       "pktcSigDevToneFreqAmpModePrtg": pktcSigDevToneFreqAmpModePrtg,
       "pktcSigDevToneDbLevel": pktcSigDevToneDbLevel,
       "pktcSigDevToneFreqOnDuration": pktcSigDevToneFreqOnDuration,
       "pktcSigDevToneFreqOffDuration": pktcSigDevToneFreqOffDuration,
       "pktcSigDevToneFreqRepeatCount": pktcSigDevToneFreqRepeatCount,
       "pktcNcsEndPntConfigObjects": pktcNcsEndPntConfigObjects,
       "pktcNcsEndPntConfigTable": pktcNcsEndPntConfigTable,
       "pktcNcsEndPntConfigEntry": pktcNcsEndPntConfigEntry,
       "pktcNcsEndPntConfigCallAgentId": pktcNcsEndPntConfigCallAgentId,
       "pktcNcsEndPntConfigCallAgentUdpPort": pktcNcsEndPntConfigCallAgentUdpPort,
       "pktcNcsEndPntConfigPartialDialTO": pktcNcsEndPntConfigPartialDialTO,
       "pktcNcsEndPntConfigCriticalDialTO": pktcNcsEndPntConfigCriticalDialTO,
       "pktcNcsEndPntConfigBusyToneTO": pktcNcsEndPntConfigBusyToneTO,
       "pktcNcsEndPntConfigDialToneTO": pktcNcsEndPntConfigDialToneTO,
       "pktcNcsEndPntConfigMessageWaitingTO": pktcNcsEndPntConfigMessageWaitingTO,
       "pktcNcsEndPntConfigOffHookWarnToneTO": pktcNcsEndPntConfigOffHookWarnToneTO,
       "pktcNcsEndPntConfigRingingTO": pktcNcsEndPntConfigRingingTO,
       "pktcNcsEndPntConfigRingBackTO": pktcNcsEndPntConfigRingBackTO,
       "pktcNcsEndPntConfigReorderToneTO": pktcNcsEndPntConfigReorderToneTO,
       "pktcNcsEndPntConfigStutterDialToneTO": pktcNcsEndPntConfigStutterDialToneTO,
       "pktcNcsEndPntConfigTSMax": pktcNcsEndPntConfigTSMax,
       "pktcNcsEndPntConfigMax1": pktcNcsEndPntConfigMax1,
       "pktcNcsEndPntConfigMax2": pktcNcsEndPntConfigMax2,
       "pktcNcsEndPntConfigMax1QEnable": pktcNcsEndPntConfigMax1QEnable,
       "pktcNcsEndPntConfigMax2QEnable": pktcNcsEndPntConfigMax2QEnable,
       "pktcNcsEndPntConfigMWD": pktcNcsEndPntConfigMWD,
       "pktcNcsEndPntConfigTdinit": pktcNcsEndPntConfigTdinit,
       "pktcNcsEndPntConfigTdmin": pktcNcsEndPntConfigTdmin,
       "pktcNcsEndPntConfigTdmax": pktcNcsEndPntConfigTdmax,
       "pktcNcsEndPntConfigRtoMax": pktcNcsEndPntConfigRtoMax,
       "pktcNcsEndPntConfigRtoInit": pktcNcsEndPntConfigRtoInit,
       "pktcNcsEndPntConfigLongDurationKeepAlive": pktcNcsEndPntConfigLongDurationKeepAlive,
       "pktcNcsEndPntConfigThist": pktcNcsEndPntConfigThist,
       "pktcNcsEndPntConfigStatus": pktcNcsEndPntConfigStatus,
       "pktcNcsEndPntConfigCallWaitingMaxRep": pktcNcsEndPntConfigCallWaitingMaxRep,
       "pktcNcsEndPntConfigCallWaitingDelay": pktcNcsEndPntConfigCallWaitingDelay,
       "pktcNcsEndPntStatusCallIpAddressType": pktcNcsEndPntStatusCallIpAddressType,
       "pktcNcsEndPntStatusCallIpAddress": pktcNcsEndPntStatusCallIpAddress,
       "pktcNcsEndPntStatusError": pktcNcsEndPntStatusError,
       "pktcNcsEndPntConfigMinHookFlash": pktcNcsEndPntConfigMinHookFlash,
       "pktcNcsEndPntConfigMaxHookFlash": pktcNcsEndPntConfigMaxHookFlash,
       "pktcNcsEndPntConfigPulseDialInterdigitTime": pktcNcsEndPntConfigPulseDialInterdigitTime,
       "pktcNcsEndPntConfigPulseDialMinMakeTime": pktcNcsEndPntConfigPulseDialMinMakeTime,
       "pktcNcsEndPntConfigPulseDialMaxMakeTime": pktcNcsEndPntConfigPulseDialMaxMakeTime,
       "pktcNcsEndPntConfigPulseDialMinBreakTime": pktcNcsEndPntConfigPulseDialMinBreakTime,
       "pktcNcsEndPntConfigPulseDialMaxBreakTime": pktcNcsEndPntConfigPulseDialMaxBreakTime,
       "pktcSigConformance": pktcSigConformance,
       "pktcSigCompliances": pktcSigCompliances,
       "pktcSigBasicCompliance": pktcSigBasicCompliance,
       "pktcSigGroups": pktcSigGroups,
       "pktcSigGroup": pktcSigGroup,
       "pktcNcsGroup": pktcNcsGroup,
       "pktcInternationalGroup": pktcInternationalGroup}
)
