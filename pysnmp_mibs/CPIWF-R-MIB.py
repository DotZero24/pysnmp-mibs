# SNMP MIB module (CPIWF-R-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/CPIWF-R-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:57 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cpIwfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 5)
)
if mibBuilder.loadTexts:
    cpIwfMIB.setRevisions(
        ("2000-08-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RadExperimental_ObjectIdentity = ObjectIdentity
radExperimental = _RadExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20)
)
_CpIwfMIBObjects_ObjectIdentity = ObjectIdentity
cpIwfMIBObjects = _CpIwfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1)
)
_CpIwf_ObjectIdentity = ObjectIdentity
cpIwf = _CpIwf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 1)
)
_CpIwfIfIndex_Type = Integer32
_CpIwfIfIndex_Object = MibScalar
cpIwfIfIndex = _CpIwfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 1, 1),
    _CpIwfIfIndex_Type()
)
cpIwfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIfIndex.setStatus("current")
_CpIwfVpi_Type = Integer32
_CpIwfVpi_Object = MibScalar
cpIwfVpi = _CpIwfVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 1, 2),
    _CpIwfVpi_Type()
)
cpIwfVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfVpi.setStatus("current")
_CpIwfVci_Type = Integer32
_CpIwfVci_Object = MibScalar
cpIwfVci = _CpIwfVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 1, 3),
    _CpIwfVci_Type()
)
cpIwfVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfVci.setStatus("current")


class _CpIwfVccMib_Type(Integer32):
    """Custom type cpIwfVccMib based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("af-nm-0165", 1),
          ("rfc2515", 2))
    )


_CpIwfVccMib_Type.__name__ = "Integer32"
_CpIwfVccMib_Object = MibScalar
cpIwfVccMib = _CpIwfVccMib_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 1, 4),
    _CpIwfVccMib_Type()
)
cpIwfVccMib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfVccMib.setStatus("current")
_CpIwfNumPotsPorts_Type = Integer32
_CpIwfNumPotsPorts_Object = MibScalar
cpIwfNumPotsPorts = _CpIwfNumPotsPorts_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 1, 5),
    _CpIwfNumPotsPorts_Type()
)
cpIwfNumPotsPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfNumPotsPorts.setStatus("current")
_CpIwfNumIsdnBriPorts_Type = Integer32
_CpIwfNumIsdnBriPorts_Object = MibScalar
cpIwfNumIsdnBriPorts = _CpIwfNumIsdnBriPorts_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 1, 6),
    _CpIwfNumIsdnBriPorts_Type()
)
cpIwfNumIsdnBriPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfNumIsdnBriPorts.setStatus("current")


class _CpIwfTimingReference_Type(Integer32):
    """Custom type cpIwfTimingReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ntr", 1),
          ("adaptiveVoice", 2),
          ("freeRun", 3))
    )


_CpIwfTimingReference_Type.__name__ = "Integer32"
_CpIwfTimingReference_Object = MibScalar
cpIwfTimingReference = _CpIwfTimingReference_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 1, 7),
    _CpIwfTimingReference_Type()
)
cpIwfTimingReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfTimingReference.setStatus("current")


class _CpIwfPotsPortEncodingSelectionMode_Type(Integer32):
    """Custom type cpIwfPotsPortEncodingSelectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("independent", 1),
          ("master-slave", 2))
    )


_CpIwfPotsPortEncodingSelectionMode_Type.__name__ = "Integer32"
_CpIwfPotsPortEncodingSelectionMode_Object = MibScalar
cpIwfPotsPortEncodingSelectionMode = _CpIwfPotsPortEncodingSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 1, 8),
    _CpIwfPotsPortEncodingSelectionMode_Type()
)
cpIwfPotsPortEncodingSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfPotsPortEncodingSelectionMode.setStatus("current")


class _CpIwfIsdnBriPortEncodingSelectionMode_Type(Integer32):
    """Custom type cpIwfIsdnBriPortEncodingSelectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("independent", 1),
          ("master-slave", 2))
    )


_CpIwfIsdnBriPortEncodingSelectionMode_Type.__name__ = "Integer32"
_CpIwfIsdnBriPortEncodingSelectionMode_Object = MibScalar
cpIwfIsdnBriPortEncodingSelectionMode = _CpIwfIsdnBriPortEncodingSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 1, 9),
    _CpIwfIsdnBriPortEncodingSelectionMode_Type()
)
cpIwfIsdnBriPortEncodingSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortEncodingSelectionMode.setStatus("current")
_CpIwfNumDs0Bundles_Type = Integer32
_CpIwfNumDs0Bundles_Object = MibScalar
cpIwfNumDs0Bundles = _CpIwfNumDs0Bundles_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 1, 10),
    _CpIwfNumDs0Bundles_Type()
)
cpIwfNumDs0Bundles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfNumDs0Bundles.setStatus("current")
_CpIwfLineSignaling_Type = OctetString
_CpIwfLineSignaling_Object = MibScalar
cpIwfLineSignaling = _CpIwfLineSignaling_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 1, 11),
    _CpIwfLineSignaling_Type()
)
cpIwfLineSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfLineSignaling.setStatus("current")
_CpIwfNumIsdnPriPorts_Type = Integer32
_CpIwfNumIsdnPriPorts_Object = MibScalar
cpIwfNumIsdnPriPorts = _CpIwfNumIsdnPriPorts_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 1, 28),
    _CpIwfNumIsdnPriPorts_Type()
)
cpIwfNumIsdnPriPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfNumIsdnPriPorts.setStatus("current")


class _CpIwfIsdnPriPortEncodingSelectionMode_Type(Integer32):
    """Custom type cpIwfIsdnPriPortEncodingSelectionMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("independent", 1),
          ("masterSlave", 2))
    )


_CpIwfIsdnPriPortEncodingSelectionMode_Type.__name__ = "Integer32"
_CpIwfIsdnPriPortEncodingSelectionMode_Object = MibScalar
cpIwfIsdnPriPortEncodingSelectionMode = _CpIwfIsdnPriPortEncodingSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 1, 29),
    _CpIwfIsdnPriPortEncodingSelectionMode_Type()
)
cpIwfIsdnPriPortEncodingSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfIsdnPriPortEncodingSelectionMode.setStatus("current")
_CpIwfAal2Profile_ObjectIdentity = ObjectIdentity
cpIwfAal2Profile = _CpIwfAal2Profile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 2)
)
_CpIwfAal2ApplicationIdentifier_Type = Integer32
_CpIwfAal2ApplicationIdentifier_Object = MibScalar
cpIwfAal2ApplicationIdentifier = _CpIwfAal2ApplicationIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 2, 1),
    _CpIwfAal2ApplicationIdentifier_Type()
)
cpIwfAal2ApplicationIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfAal2ApplicationIdentifier.setStatus("current")


class _CpIwfAal2CpsMaxMultiplexedChannels_Type(Integer32):
    """Custom type cpIwfAal2CpsMaxMultiplexedChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CpIwfAal2CpsMaxMultiplexedChannels_Type.__name__ = "Integer32"
_CpIwfAal2CpsMaxMultiplexedChannels_Object = MibScalar
cpIwfAal2CpsMaxMultiplexedChannels = _CpIwfAal2CpsMaxMultiplexedChannels_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 2, 2),
    _CpIwfAal2CpsMaxMultiplexedChannels_Type()
)
cpIwfAal2CpsMaxMultiplexedChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfAal2CpsMaxMultiplexedChannels.setStatus("current")


class _CpIwfAal2CpsMaxSDULength_Type(Integer32):
    """Custom type cpIwfAal2CpsMaxSDULength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(45, 45),
        ValueRangeConstraint(64, 64),
    )


_CpIwfAal2CpsMaxSDULength_Type.__name__ = "Integer32"
_CpIwfAal2CpsMaxSDULength_Object = MibScalar
cpIwfAal2CpsMaxSDULength = _CpIwfAal2CpsMaxSDULength_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 2, 3),
    _CpIwfAal2CpsMaxSDULength_Type()
)
cpIwfAal2CpsMaxSDULength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfAal2CpsMaxSDULength.setStatus("current")


class _CpIwfAal2CpsCIDLowerLimit_Type(Integer32):
    """Custom type cpIwfAal2CpsCIDLowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_CpIwfAal2CpsCIDLowerLimit_Type.__name__ = "Integer32"
_CpIwfAal2CpsCIDLowerLimit_Object = MibScalar
cpIwfAal2CpsCIDLowerLimit = _CpIwfAal2CpsCIDLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 2, 4),
    _CpIwfAal2CpsCIDLowerLimit_Type()
)
cpIwfAal2CpsCIDLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfAal2CpsCIDLowerLimit.setStatus("current")


class _CpIwfAal2CpsCIDUpperLimit_Type(Integer32):
    """Custom type cpIwfAal2CpsCIDUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_CpIwfAal2CpsCIDUpperLimit_Type.__name__ = "Integer32"
_CpIwfAal2CpsCIDUpperLimit_Object = MibScalar
cpIwfAal2CpsCIDUpperLimit = _CpIwfAal2CpsCIDUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 2, 5),
    _CpIwfAal2CpsCIDUpperLimit_Type()
)
cpIwfAal2CpsCIDUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfAal2CpsCIDUpperLimit.setStatus("current")


class _CpIwfAal2CpsOptimisation_Type(Integer32):
    """Custom type cpIwfAal2CpsOptimisation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleCpsPacketPerCpsPduNoOverlap", 1),
          ("multipleCpsPacketPerCpsPduWithOverlap", 2))
    )


_CpIwfAal2CpsOptimisation_Type.__name__ = "Integer32"
_CpIwfAal2CpsOptimisation_Object = MibScalar
cpIwfAal2CpsOptimisation = _CpIwfAal2CpsOptimisation_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 2, 6),
    _CpIwfAal2CpsOptimisation_Type()
)
cpIwfAal2CpsOptimisation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfAal2CpsOptimisation.setStatus("current")


class _CpIwfAal2SscsFaxModulationTransport_Type(Integer32):
    """Custom type cpIwfAal2SscsFaxModulationTransport based on Integer32"""
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


_CpIwfAal2SscsFaxModulationTransport_Type.__name__ = "Integer32"
_CpIwfAal2SscsFaxModulationTransport_Object = MibScalar
cpIwfAal2SscsFaxModulationTransport = _CpIwfAal2SscsFaxModulationTransport_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 2, 7),
    _CpIwfAal2SscsFaxModulationTransport_Type()
)
cpIwfAal2SscsFaxModulationTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfAal2SscsFaxModulationTransport.setStatus("current")


class _CpIwfAal2SscsCasSignalingTransport_Type(Integer32):
    """Custom type cpIwfAal2SscsCasSignalingTransport based on Integer32"""
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


_CpIwfAal2SscsCasSignalingTransport_Type.__name__ = "Integer32"
_CpIwfAal2SscsCasSignalingTransport_Object = MibScalar
cpIwfAal2SscsCasSignalingTransport = _CpIwfAal2SscsCasSignalingTransport_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 2, 8),
    _CpIwfAal2SscsCasSignalingTransport_Type()
)
cpIwfAal2SscsCasSignalingTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfAal2SscsCasSignalingTransport.setStatus("current")


class _CpIwfAal2SscsDtmfDigitPacketTransport_Type(Integer32):
    """Custom type cpIwfAal2SscsDtmfDigitPacketTransport based on Integer32"""
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


_CpIwfAal2SscsDtmfDigitPacketTransport_Type.__name__ = "Integer32"
_CpIwfAal2SscsDtmfDigitPacketTransport_Object = MibScalar
cpIwfAal2SscsDtmfDigitPacketTransport = _CpIwfAal2SscsDtmfDigitPacketTransport_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 2, 9),
    _CpIwfAal2SscsDtmfDigitPacketTransport_Type()
)
cpIwfAal2SscsDtmfDigitPacketTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfAal2SscsDtmfDigitPacketTransport.setStatus("current")


class _CpIwfAal2SscsPcmEncoding_Type(Integer32):
    """Custom type cpIwfAal2SscsPcmEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a-law", 1),
          ("u-law", 2))
    )


_CpIwfAal2SscsPcmEncoding_Type.__name__ = "Integer32"
_CpIwfAal2SscsPcmEncoding_Object = MibScalar
cpIwfAal2SscsPcmEncoding = _CpIwfAal2SscsPcmEncoding_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 2, 10),
    _CpIwfAal2SscsPcmEncoding_Type()
)
cpIwfAal2SscsPcmEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfAal2SscsPcmEncoding.setStatus("current")
_CpIwfAal2SscsMaxSssarSduLength_Type = Integer32
_CpIwfAal2SscsMaxSssarSduLength_Object = MibScalar
cpIwfAal2SscsMaxSssarSduLength = _CpIwfAal2SscsMaxSssarSduLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 2, 11),
    _CpIwfAal2SscsMaxSssarSduLength_Type()
)
cpIwfAal2SscsMaxSssarSduLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfAal2SscsMaxSssarSduLength.setStatus("current")


class _CpIwfAal2SscsPredefinedProfileIdentifier_Type(Integer32):
    """Custom type cpIwfAal2SscsPredefinedProfileIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CpIwfAal2SscsPredefinedProfileIdentifier_Type.__name__ = "Integer32"
_CpIwfAal2SscsPredefinedProfileIdentifier_Object = MibScalar
cpIwfAal2SscsPredefinedProfileIdentifier = _CpIwfAal2SscsPredefinedProfileIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 2, 12),
    _CpIwfAal2SscsPredefinedProfileIdentifier_Type()
)
cpIwfAal2SscsPredefinedProfileIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfAal2SscsPredefinedProfileIdentifier.setStatus("current")
_CpIwfAal2SscsIeeeOui_Type = Integer32
_CpIwfAal2SscsIeeeOui_Object = MibScalar
cpIwfAal2SscsIeeeOui = _CpIwfAal2SscsIeeeOui_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 2, 13),
    _CpIwfAal2SscsIeeeOui_Type()
)
cpIwfAal2SscsIeeeOui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfAal2SscsIeeeOui.setStatus("current")
_CpIwfPotsPortTable_Object = MibTable
cpIwfPotsPortTable = _CpIwfPotsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 3)
)
if mibBuilder.loadTexts:
    cpIwfPotsPortTable.setStatus("current")
_CpIwfPotsPortEntry_Object = MibTableRow
cpIwfPotsPortEntry = _CpIwfPotsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 3, 1)
)
cpIwfPotsPortEntry.setIndexNames(
    (0, "CPIWF-R-MIB", "cpIwfPotsPortNumber"),
)
if mibBuilder.loadTexts:
    cpIwfPotsPortEntry.setStatus("current")
_CpIwfPotsPortNumber_Type = Integer32
_CpIwfPotsPortNumber_Object = MibTableColumn
cpIwfPotsPortNumber = _CpIwfPotsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 3, 1, 1),
    _CpIwfPotsPortNumber_Type()
)
cpIwfPotsPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpIwfPotsPortNumber.setStatus("current")
_CpIwfPotsPortPhysicalPort_Type = Integer32
_CpIwfPotsPortPhysicalPort_Object = MibTableColumn
cpIwfPotsPortPhysicalPort = _CpIwfPotsPortPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 3, 1, 2),
    _CpIwfPotsPortPhysicalPort_Type()
)
cpIwfPotsPortPhysicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfPotsPortPhysicalPort.setStatus("current")


class _CpIwfPotsPortChannelId_Type(Integer32):
    """Custom type cpIwfPotsPortChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_CpIwfPotsPortChannelId_Type.__name__ = "Integer32"
_CpIwfPotsPortChannelId_Object = MibTableColumn
cpIwfPotsPortChannelId = _CpIwfPotsPortChannelId_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 3, 1, 3),
    _CpIwfPotsPortChannelId_Type()
)
cpIwfPotsPortChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfPotsPortChannelId.setStatus("current")


class _CpIwfPotsPortTestMode_Type(Integer32):
    """Custom type cpIwfPotsPortTestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("codecLoopback", 2),
          ("aal2Loopback", 3))
    )


_CpIwfPotsPortTestMode_Type.__name__ = "Integer32"
_CpIwfPotsPortTestMode_Object = MibTableColumn
cpIwfPotsPortTestMode = _CpIwfPotsPortTestMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 3, 1, 4),
    _CpIwfPotsPortTestMode_Type()
)
cpIwfPotsPortTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfPotsPortTestMode.setStatus("current")


class _CpIwfPotsPortSignalingMethod_Type(Integer32):
    """Custom type cpIwfPotsPortSignalingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loopStartNormalBattery", 1),
          ("loopStartReverseBattery", 2),
          ("groundStart", 3))
    )


_CpIwfPotsPortSignalingMethod_Type.__name__ = "Integer32"
_CpIwfPotsPortSignalingMethod_Object = MibTableColumn
cpIwfPotsPortSignalingMethod = _CpIwfPotsPortSignalingMethod_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 3, 1, 5),
    _CpIwfPotsPortSignalingMethod_Type()
)
cpIwfPotsPortSignalingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfPotsPortSignalingMethod.setStatus("current")


class _CpIwfPotsPortRxBytesPerCell_Type(Integer32):
    """Custom type cpIwfPotsPortRxBytesPerCell based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 44),
    )


_CpIwfPotsPortRxBytesPerCell_Type.__name__ = "Integer32"
_CpIwfPotsPortRxBytesPerCell_Object = MibTableColumn
cpIwfPotsPortRxBytesPerCell = _CpIwfPotsPortRxBytesPerCell_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 3, 1, 6),
    _CpIwfPotsPortRxBytesPerCell_Type()
)
cpIwfPotsPortRxBytesPerCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfPotsPortRxBytesPerCell.setStatus("current")


class _CpIwfPotsPortTxBytesPerCell_Type(Integer32):
    """Custom type cpIwfPotsPortTxBytesPerCell based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 44),
    )


_CpIwfPotsPortTxBytesPerCell_Type.__name__ = "Integer32"
_CpIwfPotsPortTxBytesPerCell_Object = MibTableColumn
cpIwfPotsPortTxBytesPerCell = _CpIwfPotsPortTxBytesPerCell_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 3, 1, 7),
    _CpIwfPotsPortTxBytesPerCell_Type()
)
cpIwfPotsPortTxBytesPerCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfPotsPortTxBytesPerCell.setStatus("current")


class _CpIwfPotsPortContCheck_Type(Integer32):
    """Custom type cpIwfPotsPortContCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off-two-way", 2),
          ("on-source", 3),
          ("on-sink", 4),
          ("on-two-way", 5),
          ("off-sink", 6),
          ("off-source", 7))
    )


_CpIwfPotsPortContCheck_Type.__name__ = "Integer32"
_CpIwfPotsPortContCheck_Object = MibTableColumn
cpIwfPotsPortContCheck = _CpIwfPotsPortContCheck_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 3, 1, 8),
    _CpIwfPotsPortContCheck_Type()
)
cpIwfPotsPortContCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfPotsPortContCheck.setStatus("current")


class _CpIwfPotsPortStatus_Type(Integer32):
    """Custom type cpIwfPotsPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("busy", 2),
          ("idle", 3),
          ("faulty", 4),
          ("underTest", 5))
    )


_CpIwfPotsPortStatus_Type.__name__ = "Integer32"
_CpIwfPotsPortStatus_Object = MibTableColumn
cpIwfPotsPortStatus = _CpIwfPotsPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 3, 1, 9),
    _CpIwfPotsPortStatus_Type()
)
cpIwfPotsPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfPotsPortStatus.setStatus("current")
_CpIwfIsdnBriPortTable_Object = MibTable
cpIwfIsdnBriPortTable = _CpIwfIsdnBriPortTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 4)
)
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortTable.setStatus("current")
_CpIwfIsdnBriPortEntry_Object = MibTableRow
cpIwfIsdnBriPortEntry = _CpIwfIsdnBriPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 4, 1)
)
cpIwfIsdnBriPortEntry.setIndexNames(
    (0, "CPIWF-R-MIB", "cpIwfIsdnBriPortNumber"),
)
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortEntry.setStatus("current")
_CpIwfIsdnBriPortNumber_Type = Integer32
_CpIwfIsdnBriPortNumber_Object = MibTableColumn
cpIwfIsdnBriPortNumber = _CpIwfIsdnBriPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 4, 1, 1),
    _CpIwfIsdnBriPortNumber_Type()
)
cpIwfIsdnBriPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortNumber.setStatus("current")
_CpIwfIsdnBriPortPhysicalPort_Type = Integer32
_CpIwfIsdnBriPortPhysicalPort_Object = MibTableColumn
cpIwfIsdnBriPortPhysicalPort = _CpIwfIsdnBriPortPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 4, 1, 2),
    _CpIwfIsdnBriPortPhysicalPort_Type()
)
cpIwfIsdnBriPortPhysicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortPhysicalPort.setStatus("current")


class _CpIwfIsdnBriPortChannelIdD_Type(Integer32):
    """Custom type cpIwfIsdnBriPortChannelIdD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_CpIwfIsdnBriPortChannelIdD_Type.__name__ = "Integer32"
_CpIwfIsdnBriPortChannelIdD_Object = MibTableColumn
cpIwfIsdnBriPortChannelIdD = _CpIwfIsdnBriPortChannelIdD_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 4, 1, 3),
    _CpIwfIsdnBriPortChannelIdD_Type()
)
cpIwfIsdnBriPortChannelIdD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortChannelIdD.setStatus("current")


class _CpIwfIsdnBriPortChannelIdB1_Type(Integer32):
    """Custom type cpIwfIsdnBriPortChannelIdB1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_CpIwfIsdnBriPortChannelIdB1_Type.__name__ = "Integer32"
_CpIwfIsdnBriPortChannelIdB1_Object = MibTableColumn
cpIwfIsdnBriPortChannelIdB1 = _CpIwfIsdnBriPortChannelIdB1_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 4, 1, 4),
    _CpIwfIsdnBriPortChannelIdB1_Type()
)
cpIwfIsdnBriPortChannelIdB1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortChannelIdB1.setStatus("current")


class _CpIwfIsdnBriPortChannelIdB2_Type(Integer32):
    """Custom type cpIwfIsdnBriPortChannelIdB2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_CpIwfIsdnBriPortChannelIdB2_Type.__name__ = "Integer32"
_CpIwfIsdnBriPortChannelIdB2_Object = MibTableColumn
cpIwfIsdnBriPortChannelIdB2 = _CpIwfIsdnBriPortChannelIdB2_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 4, 1, 5),
    _CpIwfIsdnBriPortChannelIdB2_Type()
)
cpIwfIsdnBriPortChannelIdB2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortChannelIdB2.setStatus("current")


class _CpIwfIsdnBriPortRxBytesPerCell_Type(Integer32):
    """Custom type cpIwfIsdnBriPortRxBytesPerCell based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 44),
    )


_CpIwfIsdnBriPortRxBytesPerCell_Type.__name__ = "Integer32"
_CpIwfIsdnBriPortRxBytesPerCell_Object = MibTableColumn
cpIwfIsdnBriPortRxBytesPerCell = _CpIwfIsdnBriPortRxBytesPerCell_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 4, 1, 6),
    _CpIwfIsdnBriPortRxBytesPerCell_Type()
)
cpIwfIsdnBriPortRxBytesPerCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortRxBytesPerCell.setStatus("current")


class _CpIwfIsdnBriPortTxBytesPerCell_Type(Integer32):
    """Custom type cpIwfIsdnBriPortTxBytesPerCell based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 44),
    )


_CpIwfIsdnBriPortTxBytesPerCell_Type.__name__ = "Integer32"
_CpIwfIsdnBriPortTxBytesPerCell_Object = MibTableColumn
cpIwfIsdnBriPortTxBytesPerCell = _CpIwfIsdnBriPortTxBytesPerCell_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 4, 1, 7),
    _CpIwfIsdnBriPortTxBytesPerCell_Type()
)
cpIwfIsdnBriPortTxBytesPerCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortTxBytesPerCell.setStatus("current")


class _CpIwfIsdnBriPortContCheck_Type(Integer32):
    """Custom type cpIwfIsdnBriPortContCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off-two-way", 2),
          ("on-source", 3),
          ("on-sink", 4),
          ("on-two-way", 5),
          ("off-sink", 6),
          ("off-source", 7))
    )


_CpIwfIsdnBriPortContCheck_Type.__name__ = "Integer32"
_CpIwfIsdnBriPortContCheck_Object = MibTableColumn
cpIwfIsdnBriPortContCheck = _CpIwfIsdnBriPortContCheck_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 4, 1, 8),
    _CpIwfIsdnBriPortContCheck_Type()
)
cpIwfIsdnBriPortContCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortContCheck.setStatus("current")


class _CpIwfIsdnBriPortEchoCanceler_Type(Integer32):
    """Custom type cpIwfIsdnBriPortEchoCanceler based on Integer32"""
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
        *(("notApplicable", 1),
          ("b1-Off-B2-Off", 2),
          ("b1-Off-B2-On", 3),
          ("b1-On-B2-off", 4),
          ("b1-On-B2-On", 5))
    )


_CpIwfIsdnBriPortEchoCanceler_Type.__name__ = "Integer32"
_CpIwfIsdnBriPortEchoCanceler_Object = MibTableColumn
cpIwfIsdnBriPortEchoCanceler = _CpIwfIsdnBriPortEchoCanceler_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 4, 1, 9),
    _CpIwfIsdnBriPortEchoCanceler_Type()
)
cpIwfIsdnBriPortEchoCanceler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortEchoCanceler.setStatus("current")


class _CpIwfIsdnBriPortL1Status_Type(Integer32):
    """Custom type cpIwfIsdnBriPortL1Status based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("deactivated", 2),
          ("accessActivated", 3),
          ("accessDeactivated", 4),
          ("losLofDeactivated", 5),
          ("losLofActivated", 6),
          ("lostSignal", 7),
          ("lostFrame", 8),
          ("deactivateST", 9),
          ("activateST", 10),
          ("sendInfo2", 11),
          ("sendInfo4", 12),
          ("frameSlip", 13),
          ("loopActivated", 14),
          ("loopNotStopped", 15))
    )


_CpIwfIsdnBriPortL1Status_Type.__name__ = "Integer32"
_CpIwfIsdnBriPortL1Status_Object = MibTableColumn
cpIwfIsdnBriPortL1Status = _CpIwfIsdnBriPortL1Status_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 4, 1, 10),
    _CpIwfIsdnBriPortL1Status_Type()
)
cpIwfIsdnBriPortL1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortL1Status.setStatus("current")


class _CpIwfIsdnBriPortDChRxPCMStatus_Type(Integer32):
    """Custom type cpIwfIsdnBriPortDChRxPCMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("close", 2),
          ("open", 3))
    )


_CpIwfIsdnBriPortDChRxPCMStatus_Type.__name__ = "Integer32"
_CpIwfIsdnBriPortDChRxPCMStatus_Object = MibTableColumn
cpIwfIsdnBriPortDChRxPCMStatus = _CpIwfIsdnBriPortDChRxPCMStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 4, 1, 11),
    _CpIwfIsdnBriPortDChRxPCMStatus_Type()
)
cpIwfIsdnBriPortDChRxPCMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortDChRxPCMStatus.setStatus("current")


class _CpIwfIsdnBriPortB1ChRxPCMStatus_Type(Integer32):
    """Custom type cpIwfIsdnBriPortB1ChRxPCMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("close", 2),
          ("open", 3))
    )


_CpIwfIsdnBriPortB1ChRxPCMStatus_Type.__name__ = "Integer32"
_CpIwfIsdnBriPortB1ChRxPCMStatus_Object = MibTableColumn
cpIwfIsdnBriPortB1ChRxPCMStatus = _CpIwfIsdnBriPortB1ChRxPCMStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 4, 1, 12),
    _CpIwfIsdnBriPortB1ChRxPCMStatus_Type()
)
cpIwfIsdnBriPortB1ChRxPCMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortB1ChRxPCMStatus.setStatus("current")


class _CpIwfIsdnBriPortB2ChRxPCMStatus_Type(Integer32):
    """Custom type cpIwfIsdnBriPortB2ChRxPCMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("close", 2),
          ("open", 3))
    )


_CpIwfIsdnBriPortB2ChRxPCMStatus_Type.__name__ = "Integer32"
_CpIwfIsdnBriPortB2ChRxPCMStatus_Object = MibTableColumn
cpIwfIsdnBriPortB2ChRxPCMStatus = _CpIwfIsdnBriPortB2ChRxPCMStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 4, 1, 13),
    _CpIwfIsdnBriPortB2ChRxPCMStatus_Type()
)
cpIwfIsdnBriPortB2ChRxPCMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortB2ChRxPCMStatus.setStatus("current")


class _CpIwfIsdnBriPortDChTxPCMStatus_Type(Integer32):
    """Custom type cpIwfIsdnBriPortDChTxPCMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("close", 2),
          ("open", 3))
    )


_CpIwfIsdnBriPortDChTxPCMStatus_Type.__name__ = "Integer32"
_CpIwfIsdnBriPortDChTxPCMStatus_Object = MibTableColumn
cpIwfIsdnBriPortDChTxPCMStatus = _CpIwfIsdnBriPortDChTxPCMStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 4, 1, 14),
    _CpIwfIsdnBriPortDChTxPCMStatus_Type()
)
cpIwfIsdnBriPortDChTxPCMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortDChTxPCMStatus.setStatus("current")


class _CpIwfIsdnBriPortB1ChTxPCMStatus_Type(Integer32):
    """Custom type cpIwfIsdnBriPortB1ChTxPCMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("close", 2),
          ("open", 3))
    )


_CpIwfIsdnBriPortB1ChTxPCMStatus_Type.__name__ = "Integer32"
_CpIwfIsdnBriPortB1ChTxPCMStatus_Object = MibTableColumn
cpIwfIsdnBriPortB1ChTxPCMStatus = _CpIwfIsdnBriPortB1ChTxPCMStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 4, 1, 15),
    _CpIwfIsdnBriPortB1ChTxPCMStatus_Type()
)
cpIwfIsdnBriPortB1ChTxPCMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortB1ChTxPCMStatus.setStatus("current")


class _CpIwfIsdnBriPortB2ChTxPCMStatus_Type(Integer32):
    """Custom type cpIwfIsdnBriPortB2ChTxPCMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("close", 2),
          ("open", 3))
    )


_CpIwfIsdnBriPortB2ChTxPCMStatus_Type.__name__ = "Integer32"
_CpIwfIsdnBriPortB2ChTxPCMStatus_Object = MibTableColumn
cpIwfIsdnBriPortB2ChTxPCMStatus = _CpIwfIsdnBriPortB2ChTxPCMStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 4, 1, 16),
    _CpIwfIsdnBriPortB2ChTxPCMStatus_Type()
)
cpIwfIsdnBriPortB2ChTxPCMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortB2ChTxPCMStatus.setStatus("current")
_CpIwfDs0BundleTable_Object = MibTable
cpIwfDs0BundleTable = _CpIwfDs0BundleTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 5)
)
if mibBuilder.loadTexts:
    cpIwfDs0BundleTable.setStatus("current")
_CpIwfDs0BundleEntry_Object = MibTableRow
cpIwfDs0BundleEntry = _CpIwfDs0BundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 5, 1)
)
cpIwfDs0BundleEntry.setIndexNames(
    (0, "CPIWF-R-MIB", "cpIwfDs0BundleNumber"),
)
if mibBuilder.loadTexts:
    cpIwfDs0BundleEntry.setStatus("current")
_CpIwfDs0BundleNumber_Type = Integer32
_CpIwfDs0BundleNumber_Object = MibTableColumn
cpIwfDs0BundleNumber = _CpIwfDs0BundleNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 5, 1, 1),
    _CpIwfDs0BundleNumber_Type()
)
cpIwfDs0BundleNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpIwfDs0BundleNumber.setStatus("current")
_CpIwfDs0BundleIfIndex_Type = Integer32
_CpIwfDs0BundleIfIndex_Object = MibTableColumn
cpIwfDs0BundleIfIndex = _CpIwfDs0BundleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 5, 1, 2),
    _CpIwfDs0BundleIfIndex_Type()
)
cpIwfDs0BundleIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfDs0BundleIfIndex.setStatus("current")


class _CpIwfDs0BundleChannelId_Type(Integer32):
    """Custom type cpIwfDs0BundleChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_CpIwfDs0BundleChannelId_Type.__name__ = "Integer32"
_CpIwfDs0BundleChannelId_Object = MibTableColumn
cpIwfDs0BundleChannelId = _CpIwfDs0BundleChannelId_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 5, 1, 3),
    _CpIwfDs0BundleChannelId_Type()
)
cpIwfDs0BundleChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfDs0BundleChannelId.setStatus("current")


class _CpIwfDs0BundleRxBytesPerCell_Type(Integer32):
    """Custom type cpIwfDs0BundleRxBytesPerCell based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 44),
    )


_CpIwfDs0BundleRxBytesPerCell_Type.__name__ = "Integer32"
_CpIwfDs0BundleRxBytesPerCell_Object = MibTableColumn
cpIwfDs0BundleRxBytesPerCell = _CpIwfDs0BundleRxBytesPerCell_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 5, 1, 6),
    _CpIwfDs0BundleRxBytesPerCell_Type()
)
cpIwfDs0BundleRxBytesPerCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfDs0BundleRxBytesPerCell.setStatus("current")


class _CpIwfDs0BundleTxBytesPerCell_Type(Integer32):
    """Custom type cpIwfDs0BundleTxBytesPerCell based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 44),
    )


_CpIwfDs0BundleTxBytesPerCell_Type.__name__ = "Integer32"
_CpIwfDs0BundleTxBytesPerCell_Object = MibTableColumn
cpIwfDs0BundleTxBytesPerCell = _CpIwfDs0BundleTxBytesPerCell_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 5, 1, 7),
    _CpIwfDs0BundleTxBytesPerCell_Type()
)
cpIwfDs0BundleTxBytesPerCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfDs0BundleTxBytesPerCell.setStatus("current")


class _CpIwfDs0BundleContCheck_Type(Integer32):
    """Custom type cpIwfDs0BundleContCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off-two-way", 2),
          ("on-source", 3),
          ("on-sink", 4),
          ("on-two-way", 5),
          ("off-sink", 6),
          ("off-source", 7))
    )


_CpIwfDs0BundleContCheck_Type.__name__ = "Integer32"
_CpIwfDs0BundleContCheck_Object = MibTableColumn
cpIwfDs0BundleContCheck = _CpIwfDs0BundleContCheck_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 5, 1, 8),
    _CpIwfDs0BundleContCheck_Type()
)
cpIwfDs0BundleContCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfDs0BundleContCheck.setStatus("current")
_CpIwfDs0BundleLineSignaling_Type = OctetString
_CpIwfDs0BundleLineSignaling_Object = MibTableColumn
cpIwfDs0BundleLineSignaling = _CpIwfDs0BundleLineSignaling_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 5, 1, 9),
    _CpIwfDs0BundleLineSignaling_Type()
)
cpIwfDs0BundleLineSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfDs0BundleLineSignaling.setStatus("current")
_CpIwfStats_ObjectIdentity = ObjectIdentity
cpIwfStats = _CpIwfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 6)
)
_CpIwfAal2Stats_ObjectIdentity = ObjectIdentity
cpIwfAal2Stats = _CpIwfAal2Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 7)
)
_CpIwfAal2StatsCpsInPkts_Type = Counter32
_CpIwfAal2StatsCpsInPkts_Object = MibScalar
cpIwfAal2StatsCpsInPkts = _CpIwfAal2StatsCpsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 7, 1),
    _CpIwfAal2StatsCpsInPkts_Type()
)
cpIwfAal2StatsCpsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfAal2StatsCpsInPkts.setStatus("current")
_CpIwfAal2StatsCpsOutPkts_Type = Counter32
_CpIwfAal2StatsCpsOutPkts_Object = MibScalar
cpIwfAal2StatsCpsOutPkts = _CpIwfAal2StatsCpsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 7, 2),
    _CpIwfAal2StatsCpsOutPkts_Type()
)
cpIwfAal2StatsCpsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfAal2StatsCpsOutPkts.setStatus("current")
_CpIwfAal2StatsCpsParityErrors_Type = Counter32
_CpIwfAal2StatsCpsParityErrors_Object = MibScalar
cpIwfAal2StatsCpsParityErrors = _CpIwfAal2StatsCpsParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 7, 3),
    _CpIwfAal2StatsCpsParityErrors_Type()
)
cpIwfAal2StatsCpsParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfAal2StatsCpsParityErrors.setStatus("current")
_CpIwfAal2StatsCpsSeqNumErrors_Type = Counter32
_CpIwfAal2StatsCpsSeqNumErrors_Object = MibScalar
cpIwfAal2StatsCpsSeqNumErrors = _CpIwfAal2StatsCpsSeqNumErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 7, 4),
    _CpIwfAal2StatsCpsSeqNumErrors_Type()
)
cpIwfAal2StatsCpsSeqNumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfAal2StatsCpsSeqNumErrors.setStatus("current")
_CpIwfAal2StatsCpsOsfErrors_Type = Counter32
_CpIwfAal2StatsCpsOsfErrors_Object = MibScalar
cpIwfAal2StatsCpsOsfErrors = _CpIwfAal2StatsCpsOsfErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 7, 5),
    _CpIwfAal2StatsCpsOsfErrors_Type()
)
cpIwfAal2StatsCpsOsfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfAal2StatsCpsOsfErrors.setStatus("current")
_CpIwfAal2StatsCpsHecErrors_Type = Counter32
_CpIwfAal2StatsCpsHecErrors_Object = MibScalar
cpIwfAal2StatsCpsHecErrors = _CpIwfAal2StatsCpsHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 7, 6),
    _CpIwfAal2StatsCpsHecErrors_Type()
)
cpIwfAal2StatsCpsHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfAal2StatsCpsHecErrors.setStatus("current")
_CpIwfAal2StatsCpsUuiErrors_Type = Counter32
_CpIwfAal2StatsCpsUuiErrors_Object = MibScalar
cpIwfAal2StatsCpsUuiErrors = _CpIwfAal2StatsCpsUuiErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 7, 7),
    _CpIwfAal2StatsCpsUuiErrors_Type()
)
cpIwfAal2StatsCpsUuiErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfAal2StatsCpsUuiErrors.setStatus("current")
_CpIwfAal2StatsCpsCidErrors_Type = Counter32
_CpIwfAal2StatsCpsCidErrors_Object = MibScalar
cpIwfAal2StatsCpsCidErrors = _CpIwfAal2StatsCpsCidErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 7, 8),
    _CpIwfAal2StatsCpsCidErrors_Type()
)
cpIwfAal2StatsCpsCidErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfAal2StatsCpsCidErrors.setStatus("current")
_CpIwfV5Pstn_ObjectIdentity = ObjectIdentity
cpIwfV5Pstn = _CpIwfV5Pstn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8)
)
_CpIwfV5PstnGeneral_ObjectIdentity = ObjectIdentity
cpIwfV5PstnGeneral = _CpIwfV5PstnGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 1)
)


class _CpIwfCallCollisionPriority_Type(Integer32):
    """Custom type cpIwfCallCollisionPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("originatingCallPriority", 2),
          ("terminatingCallPriority", 3))
    )


_CpIwfCallCollisionPriority_Type.__name__ = "Integer32"
_CpIwfCallCollisionPriority_Object = MibScalar
cpIwfCallCollisionPriority = _CpIwfCallCollisionPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 1, 1),
    _CpIwfCallCollisionPriority_Type()
)
cpIwfCallCollisionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfCallCollisionPriority.setStatus("current")


class _CpIwfNationalProfile_Type(Integer32):
    """Custom type cpIwfNationalProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("nationalProfile1", 2),
          ("nationalProfile2", 3),
          ("nationalProfile3", 4),
          ("nationalProfile4", 5),
          ("nationalProfile5", 6),
          ("nationalprofile6", 7),
          ("nationalProfile7", 8),
          ("nationalProfile8", 9),
          ("nationalProfile9", 10),
          ("nationalProfile10", 11))
    )


_CpIwfNationalProfile_Type.__name__ = "Integer32"
_CpIwfNationalProfile_Object = MibScalar
cpIwfNationalProfile = _CpIwfNationalProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 1, 2),
    _CpIwfNationalProfile_Type()
)
cpIwfNationalProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfNationalProfile.setStatus("current")


class _CpIwfMeterPulseFrequency_Type(Integer32):
    """Custom type cpIwfMeterPulseFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12000, 12000),
        ValueRangeConstraint(16000, 16000),
    )


_CpIwfMeterPulseFrequency_Type.__name__ = "Integer32"
_CpIwfMeterPulseFrequency_Object = MibScalar
cpIwfMeterPulseFrequency = _CpIwfMeterPulseFrequency_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 1, 3),
    _CpIwfMeterPulseFrequency_Type()
)
cpIwfMeterPulseFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfMeterPulseFrequency.setStatus("current")
_CpIwfOffHookMinTime_Type = Integer32
_CpIwfOffHookMinTime_Object = MibScalar
cpIwfOffHookMinTime = _CpIwfOffHookMinTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 1, 4),
    _CpIwfOffHookMinTime_Type()
)
cpIwfOffHookMinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfOffHookMinTime.setStatus("current")
_CpIwfOnHookMinTime_Type = Integer32
_CpIwfOnHookMinTime_Object = MibScalar
cpIwfOnHookMinTime = _CpIwfOnHookMinTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 1, 5),
    _CpIwfOnHookMinTime_Type()
)
cpIwfOnHookMinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfOnHookMinTime.setStatus("current")
_CpIwfRegisterRecallMinTime_Type = Integer32
_CpIwfRegisterRecallMinTime_Object = MibScalar
cpIwfRegisterRecallMinTime = _CpIwfRegisterRecallMinTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 1, 6),
    _CpIwfRegisterRecallMinTime_Type()
)
cpIwfRegisterRecallMinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfRegisterRecallMinTime.setStatus("current")
_CpIwfDigitMinBreakPeriod_Type = Integer32
_CpIwfDigitMinBreakPeriod_Object = MibScalar
cpIwfDigitMinBreakPeriod = _CpIwfDigitMinBreakPeriod_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 1, 7),
    _CpIwfDigitMinBreakPeriod_Type()
)
cpIwfDigitMinBreakPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfDigitMinBreakPeriod.setStatus("current")
_CpIwfDigitMaxBreakPeriod_Type = Integer32
_CpIwfDigitMaxBreakPeriod_Object = MibScalar
cpIwfDigitMaxBreakPeriod = _CpIwfDigitMaxBreakPeriod_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 1, 8),
    _CpIwfDigitMaxBreakPeriod_Type()
)
cpIwfDigitMaxBreakPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfDigitMaxBreakPeriod.setStatus("current")
_CpIwfDigitMinMakePeriod_Type = Integer32
_CpIwfDigitMinMakePeriod_Object = MibScalar
cpIwfDigitMinMakePeriod = _CpIwfDigitMinMakePeriod_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 1, 9),
    _CpIwfDigitMinMakePeriod_Type()
)
cpIwfDigitMinMakePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfDigitMinMakePeriod.setStatus("current")
_CpIwfDigitMaxMakePeriod_Type = Integer32
_CpIwfDigitMaxMakePeriod_Object = MibScalar
cpIwfDigitMaxMakePeriod = _CpIwfDigitMaxMakePeriod_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 1, 10),
    _CpIwfDigitMaxMakePeriod_Type()
)
cpIwfDigitMaxMakePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfDigitMaxMakePeriod.setStatus("current")
_CpIwfInterDigitTime_Type = Integer32
_CpIwfInterDigitTime_Object = MibScalar
cpIwfInterDigitTime = _CpIwfInterDigitTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 1, 11),
    _CpIwfInterDigitTime_Type()
)
cpIwfInterDigitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfInterDigitTime.setStatus("current")
_CpIwfCadencedRingingTypeTable_Object = MibTable
cpIwfCadencedRingingTypeTable = _CpIwfCadencedRingingTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2)
)
if mibBuilder.loadTexts:
    cpIwfCadencedRingingTypeTable.setStatus("current")
_CpIwfCadencedRingingTypeEntry_Object = MibTableRow
cpIwfCadencedRingingTypeEntry = _CpIwfCadencedRingingTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1)
)
cpIwfCadencedRingingTypeEntry.setIndexNames(
    (0, "CPIWF-R-MIB", "cpIwfCadencedRingingType"),
)
if mibBuilder.loadTexts:
    cpIwfCadencedRingingTypeEntry.setStatus("current")


class _CpIwfCadencedRingingType_Type(Integer32):
    """Custom type cpIwfCadencedRingingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CpIwfCadencedRingingType_Type.__name__ = "Integer32"
_CpIwfCadencedRingingType_Object = MibTableColumn
cpIwfCadencedRingingType = _CpIwfCadencedRingingType_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 1),
    _CpIwfCadencedRingingType_Type()
)
cpIwfCadencedRingingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingType.setStatus("current")


class _CpIwfCadencedRingingNumPeriods_Type(Integer32):
    """Custom type cpIwfCadencedRingingNumPeriods based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CpIwfCadencedRingingNumPeriods_Type.__name__ = "Integer32"
_CpIwfCadencedRingingNumPeriods_Object = MibTableColumn
cpIwfCadencedRingingNumPeriods = _CpIwfCadencedRingingNumPeriods_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 2),
    _CpIwfCadencedRingingNumPeriods_Type()
)
cpIwfCadencedRingingNumPeriods.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingNumPeriods.setStatus("current")


class _CpIwfCadencedRingingOnPeriod1_Type(Integer32):
    """Custom type cpIwfCadencedRingingOnPeriod1 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOnPeriod1_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOnPeriod1_Object = MibTableColumn
cpIwfCadencedRingingOnPeriod1 = _CpIwfCadencedRingingOnPeriod1_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 3),
    _CpIwfCadencedRingingOnPeriod1_Type()
)
cpIwfCadencedRingingOnPeriod1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOnPeriod1.setStatus("current")


class _CpIwfCadencedRingingOffPeriod1_Type(Integer32):
    """Custom type cpIwfCadencedRingingOffPeriod1 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOffPeriod1_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOffPeriod1_Object = MibTableColumn
cpIwfCadencedRingingOffPeriod1 = _CpIwfCadencedRingingOffPeriod1_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 4),
    _CpIwfCadencedRingingOffPeriod1_Type()
)
cpIwfCadencedRingingOffPeriod1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOffPeriod1.setStatus("current")


class _CpIwfCadencedRingingOnPeriod2_Type(Integer32):
    """Custom type cpIwfCadencedRingingOnPeriod2 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOnPeriod2_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOnPeriod2_Object = MibTableColumn
cpIwfCadencedRingingOnPeriod2 = _CpIwfCadencedRingingOnPeriod2_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 5),
    _CpIwfCadencedRingingOnPeriod2_Type()
)
cpIwfCadencedRingingOnPeriod2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOnPeriod2.setStatus("current")


class _CpIwfCadencedRingingOffPeriod2_Type(Integer32):
    """Custom type cpIwfCadencedRingingOffPeriod2 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOffPeriod2_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOffPeriod2_Object = MibTableColumn
cpIwfCadencedRingingOffPeriod2 = _CpIwfCadencedRingingOffPeriod2_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 6),
    _CpIwfCadencedRingingOffPeriod2_Type()
)
cpIwfCadencedRingingOffPeriod2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOffPeriod2.setStatus("current")


class _CpIwfCadencedRingingOnPeriod3_Type(Integer32):
    """Custom type cpIwfCadencedRingingOnPeriod3 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOnPeriod3_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOnPeriod3_Object = MibTableColumn
cpIwfCadencedRingingOnPeriod3 = _CpIwfCadencedRingingOnPeriod3_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 7),
    _CpIwfCadencedRingingOnPeriod3_Type()
)
cpIwfCadencedRingingOnPeriod3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOnPeriod3.setStatus("current")


class _CpIwfCadencedRingingOffPeriod3_Type(Integer32):
    """Custom type cpIwfCadencedRingingOffPeriod3 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOffPeriod3_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOffPeriod3_Object = MibTableColumn
cpIwfCadencedRingingOffPeriod3 = _CpIwfCadencedRingingOffPeriod3_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 8),
    _CpIwfCadencedRingingOffPeriod3_Type()
)
cpIwfCadencedRingingOffPeriod3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOffPeriod3.setStatus("current")


class _CpIwfCadencedRingingOnPeriod4_Type(Integer32):
    """Custom type cpIwfCadencedRingingOnPeriod4 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOnPeriod4_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOnPeriod4_Object = MibTableColumn
cpIwfCadencedRingingOnPeriod4 = _CpIwfCadencedRingingOnPeriod4_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 9),
    _CpIwfCadencedRingingOnPeriod4_Type()
)
cpIwfCadencedRingingOnPeriod4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOnPeriod4.setStatus("current")


class _CpIwfCadencedRingingOffPeriod4_Type(Integer32):
    """Custom type cpIwfCadencedRingingOffPeriod4 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOffPeriod4_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOffPeriod4_Object = MibTableColumn
cpIwfCadencedRingingOffPeriod4 = _CpIwfCadencedRingingOffPeriod4_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 10),
    _CpIwfCadencedRingingOffPeriod4_Type()
)
cpIwfCadencedRingingOffPeriod4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOffPeriod4.setStatus("current")


class _CpIwfCadencedRingingOnPeriod5_Type(Integer32):
    """Custom type cpIwfCadencedRingingOnPeriod5 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOnPeriod5_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOnPeriod5_Object = MibTableColumn
cpIwfCadencedRingingOnPeriod5 = _CpIwfCadencedRingingOnPeriod5_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 11),
    _CpIwfCadencedRingingOnPeriod5_Type()
)
cpIwfCadencedRingingOnPeriod5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOnPeriod5.setStatus("current")


class _CpIwfCadencedRingingOffPeriod5_Type(Integer32):
    """Custom type cpIwfCadencedRingingOffPeriod5 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOffPeriod5_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOffPeriod5_Object = MibTableColumn
cpIwfCadencedRingingOffPeriod5 = _CpIwfCadencedRingingOffPeriod5_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 12),
    _CpIwfCadencedRingingOffPeriod5_Type()
)
cpIwfCadencedRingingOffPeriod5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOffPeriod5.setStatus("current")


class _CpIwfCadencedRingingOnPeriod6_Type(Integer32):
    """Custom type cpIwfCadencedRingingOnPeriod6 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOnPeriod6_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOnPeriod6_Object = MibTableColumn
cpIwfCadencedRingingOnPeriod6 = _CpIwfCadencedRingingOnPeriod6_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 13),
    _CpIwfCadencedRingingOnPeriod6_Type()
)
cpIwfCadencedRingingOnPeriod6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOnPeriod6.setStatus("current")


class _CpIwfCadencedRingingOffPeriod6_Type(Integer32):
    """Custom type cpIwfCadencedRingingOffPeriod6 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOffPeriod6_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOffPeriod6_Object = MibTableColumn
cpIwfCadencedRingingOffPeriod6 = _CpIwfCadencedRingingOffPeriod6_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 14),
    _CpIwfCadencedRingingOffPeriod6_Type()
)
cpIwfCadencedRingingOffPeriod6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOffPeriod6.setStatus("current")


class _CpIwfCadencedRingingOnPeriod7_Type(Integer32):
    """Custom type cpIwfCadencedRingingOnPeriod7 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOnPeriod7_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOnPeriod7_Object = MibTableColumn
cpIwfCadencedRingingOnPeriod7 = _CpIwfCadencedRingingOnPeriod7_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 15),
    _CpIwfCadencedRingingOnPeriod7_Type()
)
cpIwfCadencedRingingOnPeriod7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOnPeriod7.setStatus("current")


class _CpIwfCadencedRingingOffPeriod7_Type(Integer32):
    """Custom type cpIwfCadencedRingingOffPeriod7 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOffPeriod7_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOffPeriod7_Object = MibTableColumn
cpIwfCadencedRingingOffPeriod7 = _CpIwfCadencedRingingOffPeriod7_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 16),
    _CpIwfCadencedRingingOffPeriod7_Type()
)
cpIwfCadencedRingingOffPeriod7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOffPeriod7.setStatus("current")


class _CpIwfCadencedRingingOnPeriod8_Type(Integer32):
    """Custom type cpIwfCadencedRingingOnPeriod8 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOnPeriod8_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOnPeriod8_Object = MibTableColumn
cpIwfCadencedRingingOnPeriod8 = _CpIwfCadencedRingingOnPeriod8_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 17),
    _CpIwfCadencedRingingOnPeriod8_Type()
)
cpIwfCadencedRingingOnPeriod8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOnPeriod8.setStatus("current")


class _CpIwfCadencedRingingOffPeriod8_Type(Integer32):
    """Custom type cpIwfCadencedRingingOffPeriod8 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOffPeriod8_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOffPeriod8_Object = MibTableColumn
cpIwfCadencedRingingOffPeriod8 = _CpIwfCadencedRingingOffPeriod8_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 18),
    _CpIwfCadencedRingingOffPeriod8_Type()
)
cpIwfCadencedRingingOffPeriod8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOffPeriod8.setStatus("current")


class _CpIwfCadencedRingingOnPeriod9_Type(Integer32):
    """Custom type cpIwfCadencedRingingOnPeriod9 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOnPeriod9_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOnPeriod9_Object = MibTableColumn
cpIwfCadencedRingingOnPeriod9 = _CpIwfCadencedRingingOnPeriod9_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 19),
    _CpIwfCadencedRingingOnPeriod9_Type()
)
cpIwfCadencedRingingOnPeriod9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOnPeriod9.setStatus("current")


class _CpIwfCadencedRingingOffPeriod9_Type(Integer32):
    """Custom type cpIwfCadencedRingingOffPeriod9 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOffPeriod9_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOffPeriod9_Object = MibTableColumn
cpIwfCadencedRingingOffPeriod9 = _CpIwfCadencedRingingOffPeriod9_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 20),
    _CpIwfCadencedRingingOffPeriod9_Type()
)
cpIwfCadencedRingingOffPeriod9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOffPeriod9.setStatus("current")


class _CpIwfCadencedRingingOnPeriod10_Type(Integer32):
    """Custom type cpIwfCadencedRingingOnPeriod10 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOnPeriod10_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOnPeriod10_Object = MibTableColumn
cpIwfCadencedRingingOnPeriod10 = _CpIwfCadencedRingingOnPeriod10_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 21),
    _CpIwfCadencedRingingOnPeriod10_Type()
)
cpIwfCadencedRingingOnPeriod10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOnPeriod10.setStatus("current")


class _CpIwfCadencedRingingOffPeriod10_Type(Integer32):
    """Custom type cpIwfCadencedRingingOffPeriod10 based on Integer32"""
    defaultValue = 1000


_CpIwfCadencedRingingOffPeriod10_Type.__name__ = "Integer32"
_CpIwfCadencedRingingOffPeriod10_Object = MibTableColumn
cpIwfCadencedRingingOffPeriod10 = _CpIwfCadencedRingingOffPeriod10_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 22),
    _CpIwfCadencedRingingOffPeriod10_Type()
)
cpIwfCadencedRingingOffPeriod10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingOffPeriod10.setStatus("current")
_CpIwfCadencedRingingTypeRowStatus_Type = RowStatus
_CpIwfCadencedRingingTypeRowStatus_Object = MibTableColumn
cpIwfCadencedRingingTypeRowStatus = _CpIwfCadencedRingingTypeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 2, 1, 23),
    _CpIwfCadencedRingingTypeRowStatus_Type()
)
cpIwfCadencedRingingTypeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfCadencedRingingTypeRowStatus.setStatus("current")
_CpIwfPulseDurationTypeTable_Object = MibTable
cpIwfPulseDurationTypeTable = _CpIwfPulseDurationTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 3)
)
if mibBuilder.loadTexts:
    cpIwfPulseDurationTypeTable.setStatus("current")
_CpIwfPulseDurationTypeEntry_Object = MibTableRow
cpIwfPulseDurationTypeEntry = _CpIwfPulseDurationTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 3, 1)
)
cpIwfPulseDurationTypeEntry.setIndexNames(
    (0, "CPIWF-R-MIB", "cpIwfPulseType"),
    (0, "CPIWF-R-MIB", "cpIwfPulseDurationType"),
)
if mibBuilder.loadTexts:
    cpIwfPulseDurationTypeEntry.setStatus("current")


class _CpIwfPulseType_Type(Integer32):
    """Custom type cpIwfPulseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CpIwfPulseType_Type.__name__ = "Integer32"
_CpIwfPulseType_Object = MibTableColumn
cpIwfPulseType = _CpIwfPulseType_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 3, 1, 1),
    _CpIwfPulseType_Type()
)
cpIwfPulseType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpIwfPulseType.setStatus("current")


class _CpIwfPulseDurationType_Type(Integer32):
    """Custom type cpIwfPulseDurationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_CpIwfPulseDurationType_Type.__name__ = "Integer32"
_CpIwfPulseDurationType_Object = MibTableColumn
cpIwfPulseDurationType = _CpIwfPulseDurationType_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 3, 1, 2),
    _CpIwfPulseDurationType_Type()
)
cpIwfPulseDurationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpIwfPulseDurationType.setStatus("current")


class _CpIwfPulseDurationNumPeriods_Type(Integer32):
    """Custom type cpIwfPulseDurationNumPeriods based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_CpIwfPulseDurationNumPeriods_Type.__name__ = "Integer32"
_CpIwfPulseDurationNumPeriods_Object = MibTableColumn
cpIwfPulseDurationNumPeriods = _CpIwfPulseDurationNumPeriods_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 3, 1, 3),
    _CpIwfPulseDurationNumPeriods_Type()
)
cpIwfPulseDurationNumPeriods.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfPulseDurationNumPeriods.setStatus("current")


class _CpIwfPulseDurationOnPeriod1_Type(Integer32):
    """Custom type cpIwfPulseDurationOnPeriod1 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_CpIwfPulseDurationOnPeriod1_Type.__name__ = "Integer32"
_CpIwfPulseDurationOnPeriod1_Object = MibTableColumn
cpIwfPulseDurationOnPeriod1 = _CpIwfPulseDurationOnPeriod1_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 3, 1, 4),
    _CpIwfPulseDurationOnPeriod1_Type()
)
cpIwfPulseDurationOnPeriod1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfPulseDurationOnPeriod1.setStatus("current")


class _CpIwfPulseDurationOffPeriod1_Type(Integer32):
    """Custom type cpIwfPulseDurationOffPeriod1 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_CpIwfPulseDurationOffPeriod1_Type.__name__ = "Integer32"
_CpIwfPulseDurationOffPeriod1_Object = MibTableColumn
cpIwfPulseDurationOffPeriod1 = _CpIwfPulseDurationOffPeriod1_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 3, 1, 5),
    _CpIwfPulseDurationOffPeriod1_Type()
)
cpIwfPulseDurationOffPeriod1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfPulseDurationOffPeriod1.setStatus("current")


class _CpIwfPulseDurationOnPeriod2_Type(Integer32):
    """Custom type cpIwfPulseDurationOnPeriod2 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_CpIwfPulseDurationOnPeriod2_Type.__name__ = "Integer32"
_CpIwfPulseDurationOnPeriod2_Object = MibTableColumn
cpIwfPulseDurationOnPeriod2 = _CpIwfPulseDurationOnPeriod2_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 3, 1, 6),
    _CpIwfPulseDurationOnPeriod2_Type()
)
cpIwfPulseDurationOnPeriod2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfPulseDurationOnPeriod2.setStatus("current")


class _CpIwfPulseDurationOffPeriod2_Type(Integer32):
    """Custom type cpIwfPulseDurationOffPeriod2 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_CpIwfPulseDurationOffPeriod2_Type.__name__ = "Integer32"
_CpIwfPulseDurationOffPeriod2_Object = MibTableColumn
cpIwfPulseDurationOffPeriod2 = _CpIwfPulseDurationOffPeriod2_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 3, 1, 7),
    _CpIwfPulseDurationOffPeriod2_Type()
)
cpIwfPulseDurationOffPeriod2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfPulseDurationOffPeriod2.setStatus("current")


class _CpIwfPulseDurationOnPeriod3_Type(Integer32):
    """Custom type cpIwfPulseDurationOnPeriod3 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_CpIwfPulseDurationOnPeriod3_Type.__name__ = "Integer32"
_CpIwfPulseDurationOnPeriod3_Object = MibTableColumn
cpIwfPulseDurationOnPeriod3 = _CpIwfPulseDurationOnPeriod3_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 3, 1, 8),
    _CpIwfPulseDurationOnPeriod3_Type()
)
cpIwfPulseDurationOnPeriod3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfPulseDurationOnPeriod3.setStatus("current")


class _CpIwfPulseDurationOffPeriod3_Type(Integer32):
    """Custom type cpIwfPulseDurationOffPeriod3 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_CpIwfPulseDurationOffPeriod3_Type.__name__ = "Integer32"
_CpIwfPulseDurationOffPeriod3_Object = MibTableColumn
cpIwfPulseDurationOffPeriod3 = _CpIwfPulseDurationOffPeriod3_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 3, 1, 9),
    _CpIwfPulseDurationOffPeriod3_Type()
)
cpIwfPulseDurationOffPeriod3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfPulseDurationOffPeriod3.setStatus("current")


class _CpIwfPulseDurationOnPeriod4_Type(Integer32):
    """Custom type cpIwfPulseDurationOnPeriod4 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_CpIwfPulseDurationOnPeriod4_Type.__name__ = "Integer32"
_CpIwfPulseDurationOnPeriod4_Object = MibTableColumn
cpIwfPulseDurationOnPeriod4 = _CpIwfPulseDurationOnPeriod4_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 3, 1, 10),
    _CpIwfPulseDurationOnPeriod4_Type()
)
cpIwfPulseDurationOnPeriod4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfPulseDurationOnPeriod4.setStatus("current")


class _CpIwfPulseDurationOffPeriod4_Type(Integer32):
    """Custom type cpIwfPulseDurationOffPeriod4 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_CpIwfPulseDurationOffPeriod4_Type.__name__ = "Integer32"
_CpIwfPulseDurationOffPeriod4_Object = MibTableColumn
cpIwfPulseDurationOffPeriod4 = _CpIwfPulseDurationOffPeriod4_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 3, 1, 11),
    _CpIwfPulseDurationOffPeriod4_Type()
)
cpIwfPulseDurationOffPeriod4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfPulseDurationOffPeriod4.setStatus("current")


class _CpIwfPulseDurationOnPeriod5_Type(Integer32):
    """Custom type cpIwfPulseDurationOnPeriod5 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_CpIwfPulseDurationOnPeriod5_Type.__name__ = "Integer32"
_CpIwfPulseDurationOnPeriod5_Object = MibTableColumn
cpIwfPulseDurationOnPeriod5 = _CpIwfPulseDurationOnPeriod5_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 3, 1, 12),
    _CpIwfPulseDurationOnPeriod5_Type()
)
cpIwfPulseDurationOnPeriod5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfPulseDurationOnPeriod5.setStatus("current")


class _CpIwfPulseDurationOffPeriod5_Type(Integer32):
    """Custom type cpIwfPulseDurationOffPeriod5 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_CpIwfPulseDurationOffPeriod5_Type.__name__ = "Integer32"
_CpIwfPulseDurationOffPeriod5_Object = MibTableColumn
cpIwfPulseDurationOffPeriod5 = _CpIwfPulseDurationOffPeriod5_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 3, 1, 13),
    _CpIwfPulseDurationOffPeriod5_Type()
)
cpIwfPulseDurationOffPeriod5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfPulseDurationOffPeriod5.setStatus("current")
_CpIwfPulseDurationTypeRowStatus_Type = RowStatus
_CpIwfPulseDurationTypeRowStatus_Object = MibTableColumn
cpIwfPulseDurationTypeRowStatus = _CpIwfPulseDurationTypeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 3, 1, 14),
    _CpIwfPulseDurationTypeRowStatus_Type()
)
cpIwfPulseDurationTypeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfPulseDurationTypeRowStatus.setStatus("current")
_CpIwfDurationTypeTable_Object = MibTable
cpIwfDurationTypeTable = _CpIwfDurationTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 4)
)
if mibBuilder.loadTexts:
    cpIwfDurationTypeTable.setStatus("current")
_CpIwfDurationTypeEntry_Object = MibTableRow
cpIwfDurationTypeEntry = _CpIwfDurationTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 4, 1)
)
cpIwfDurationTypeEntry.setIndexNames(
    (0, "CPIWF-R-MIB", "cpIwfSignal"),
    (0, "CPIWF-R-MIB", "cpIwfDurationType"),
)
if mibBuilder.loadTexts:
    cpIwfDurationTypeEntry.setStatus("current")


class _CpIwfSignal_Type(Integer32):
    """Custom type cpIwfSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CpIwfSignal_Type.__name__ = "Integer32"
_CpIwfSignal_Object = MibTableColumn
cpIwfSignal = _CpIwfSignal_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 4, 1, 1),
    _CpIwfSignal_Type()
)
cpIwfSignal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpIwfSignal.setStatus("current")


class _CpIwfDurationType_Type(Integer32):
    """Custom type cpIwfDurationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CpIwfDurationType_Type.__name__ = "Integer32"
_CpIwfDurationType_Object = MibTableColumn
cpIwfDurationType = _CpIwfDurationType_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 4, 1, 2),
    _CpIwfDurationType_Type()
)
cpIwfDurationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpIwfDurationType.setStatus("current")
_CpIwfDuration_Type = Integer32
_CpIwfDuration_Object = MibTableColumn
cpIwfDuration = _CpIwfDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 4, 1, 3),
    _CpIwfDuration_Type()
)
cpIwfDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfDuration.setStatus("current")
_CpIwfDurationTypeRowStatus_Type = RowStatus
_CpIwfDurationTypeRowStatus_Object = MibTableColumn
cpIwfDurationTypeRowStatus = _CpIwfDurationTypeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 4, 1, 4),
    _CpIwfDurationTypeRowStatus_Type()
)
cpIwfDurationTypeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfDurationTypeRowStatus.setStatus("current")
_CpIwfRateTypeTable_Object = MibTable
cpIwfRateTypeTable = _CpIwfRateTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 5)
)
if mibBuilder.loadTexts:
    cpIwfRateTypeTable.setStatus("current")
_CpIwfRateTypeEntry_Object = MibTableRow
cpIwfRateTypeEntry = _CpIwfRateTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 5, 1)
)
cpIwfRateTypeEntry.setIndexNames(
    (0, "CPIWF-R-MIB", "cpIwfRateType"),
)
if mibBuilder.loadTexts:
    cpIwfRateTypeEntry.setStatus("current")


class _CpIwfRateType_Type(Integer32):
    """Custom type cpIwfRateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_CpIwfRateType_Type.__name__ = "Integer32"
_CpIwfRateType_Object = MibTableColumn
cpIwfRateType = _CpIwfRateType_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 5, 1, 1),
    _CpIwfRateType_Type()
)
cpIwfRateType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpIwfRateType.setStatus("current")
_CpIwfRate_Type = Integer32
_CpIwfRate_Object = MibTableColumn
cpIwfRate = _CpIwfRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 5, 1, 2),
    _CpIwfRate_Type()
)
cpIwfRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfRate.setStatus("current")
_CpIwfRateTypeRowStatus_Type = RowStatus
_CpIwfRateTypeRowStatus_Object = MibTableColumn
cpIwfRateTypeRowStatus = _CpIwfRateTypeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 5, 1, 3),
    _CpIwfRateTypeRowStatus_Type()
)
cpIwfRateTypeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfRateTypeRowStatus.setStatus("current")
_CpIwfAttenuationValueTable_Object = MibTable
cpIwfAttenuationValueTable = _CpIwfAttenuationValueTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 6)
)
if mibBuilder.loadTexts:
    cpIwfAttenuationValueTable.setStatus("current")
_CpIwfAttenuationValueEntry_Object = MibTableRow
cpIwfAttenuationValueEntry = _CpIwfAttenuationValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 6, 1)
)
cpIwfAttenuationValueEntry.setIndexNames(
    (0, "CPIWF-R-MIB", "cpIwfAttenuationValue"),
)
if mibBuilder.loadTexts:
    cpIwfAttenuationValueEntry.setStatus("current")


class _CpIwfAttenuationValue_Type(Integer32):
    """Custom type cpIwfAttenuationValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CpIwfAttenuationValue_Type.__name__ = "Integer32"
_CpIwfAttenuationValue_Object = MibTableColumn
cpIwfAttenuationValue = _CpIwfAttenuationValue_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 6, 1, 1),
    _CpIwfAttenuationValue_Type()
)
cpIwfAttenuationValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpIwfAttenuationValue.setStatus("current")


class _CpIwfAttenuation_Type(Integer32):
    """Custom type cpIwfAttenuation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("neg10dB", 2),
          ("neg8dB", 3),
          ("neg6dB", 4),
          ("neg4dB", 5),
          ("neg2dB", 6),
          ("zerodB", 7),
          ("pos2dB", 8),
          ("pos4dB", 9),
          ("pos5dB", 10))
    )


_CpIwfAttenuation_Type.__name__ = "Integer32"
_CpIwfAttenuation_Object = MibTableColumn
cpIwfAttenuation = _CpIwfAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 6, 1, 2),
    _CpIwfAttenuation_Type()
)
cpIwfAttenuation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfAttenuation.setStatus("current")
_CpIwfAttenuationValueRowStatus_Type = RowStatus
_CpIwfAttenuationValueRowStatus_Object = MibTableColumn
cpIwfAttenuationValueRowStatus = _CpIwfAttenuationValueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 6, 1, 3),
    _CpIwfAttenuationValueRowStatus_Type()
)
cpIwfAttenuationValueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfAttenuationValueRowStatus.setStatus("current")


class _CpIwfTxAttenuation_Type(Integer32):
    """Custom type cpIwfTxAttenuation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("neg10dB", 2),
          ("neg8dB", 3),
          ("neg6dB", 4),
          ("neg4dB", 5),
          ("neg2dB", 6),
          ("zerodB", 7),
          ("pos2dB", 8),
          ("pos4dB", 9),
          ("pos5dB", 10))
    )


_CpIwfTxAttenuation_Type.__name__ = "Integer32"
_CpIwfTxAttenuation_Object = MibTableColumn
cpIwfTxAttenuation = _CpIwfTxAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 8, 6, 1, 4),
    _CpIwfTxAttenuation_Type()
)
cpIwfTxAttenuation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfTxAttenuation.setStatus("current")
_CpIwfUpstreamPhysicalBandwidth_Type = Integer32
_CpIwfUpstreamPhysicalBandwidth_Object = MibScalar
cpIwfUpstreamPhysicalBandwidth = _CpIwfUpstreamPhysicalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 9),
    _CpIwfUpstreamPhysicalBandwidth_Type()
)
cpIwfUpstreamPhysicalBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfUpstreamPhysicalBandwidth.setStatus("current")
_CpIwfDownstreamPhysicalBandwidth_Type = Integer32
_CpIwfDownstreamPhysicalBandwidth_Object = MibScalar
cpIwfDownstreamPhysicalBandwidth = _CpIwfDownstreamPhysicalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 10),
    _CpIwfDownstreamPhysicalBandwidth_Type()
)
cpIwfDownstreamPhysicalBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfDownstreamPhysicalBandwidth.setStatus("current")
_CpIwfIsdnPriPortTable_Object = MibTable
cpIwfIsdnPriPortTable = _CpIwfIsdnPriPortTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 13)
)
if mibBuilder.loadTexts:
    cpIwfIsdnPriPortTable.setStatus("current")
_CpIwfIsdnPriPortEntry_Object = MibTableRow
cpIwfIsdnPriPortEntry = _CpIwfIsdnPriPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 13, 1)
)
cpIwfIsdnPriPortEntry.setIndexNames(
    (0, "CPIWF-R-MIB", "isdnPriPortNumber"),
)
if mibBuilder.loadTexts:
    cpIwfIsdnPriPortEntry.setStatus("current")
_IsdnPriPortNumber_Type = Integer32
_IsdnPriPortNumber_Object = MibTableColumn
isdnPriPortNumber = _IsdnPriPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 13, 1, 1),
    _IsdnPriPortNumber_Type()
)
isdnPriPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnPriPortNumber.setStatus("current")
_IsdnPriPhysicalPort_Type = Integer32
_IsdnPriPhysicalPort_Object = MibTableColumn
isdnPriPhysicalPort = _IsdnPriPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 13, 1, 2),
    _IsdnPriPhysicalPort_Type()
)
isdnPriPhysicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnPriPhysicalPort.setStatus("current")
_IsdnPriNumBChannels_Type = Integer32
_IsdnPriNumBChannels_Object = MibTableColumn
isdnPriNumBChannels = _IsdnPriNumBChannels_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 13, 1, 3),
    _IsdnPriNumBChannels_Type()
)
isdnPriNumBChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPriNumBChannels.setStatus("current")


class _IsdnPriDAal2ChannelId_Type(Integer32):
    """Custom type isdnPriDAal2ChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_IsdnPriDAal2ChannelId_Type.__name__ = "Integer32"
_IsdnPriDAal2ChannelId_Object = MibTableColumn
isdnPriDAal2ChannelId = _IsdnPriDAal2ChannelId_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 13, 1, 4),
    _IsdnPriDAal2ChannelId_Type()
)
isdnPriDAal2ChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnPriDAal2ChannelId.setStatus("current")


class _IsdnPriPortLabel_Type(OctetString):
    """Custom type isdnPriPortLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IsdnPriPortLabel_Type.__name__ = "OctetString"
_IsdnPriPortLabel_Object = MibTableColumn
isdnPriPortLabel = _IsdnPriPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 13, 1, 5),
    _IsdnPriPortLabel_Type()
)
isdnPriPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnPriPortLabel.setStatus("current")


class _IsdnPriPortTestType_Type(Integer32):
    """Custom type isdnPriPortTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("physicalPortLoopback", 1),
          ("dChannelPhysicalPortLoopback", 2),
          ("dChannelAal2Loopback", 3))
    )


_IsdnPriPortTestType_Type.__name__ = "Integer32"
_IsdnPriPortTestType_Object = MibTableColumn
isdnPriPortTestType = _IsdnPriPortTestType_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 13, 1, 6),
    _IsdnPriPortTestType_Type()
)
isdnPriPortTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnPriPortTestType.setStatus("current")


class _IsdnPriPortChannelsStatus_Type(OctetString):
    """Custom type isdnPriPortChannelsStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_IsdnPriPortChannelsStatus_Type.__name__ = "OctetString"
_IsdnPriPortChannelsStatus_Object = MibTableColumn
isdnPriPortChannelsStatus = _IsdnPriPortChannelsStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 13, 1, 7),
    _IsdnPriPortChannelsStatus_Type()
)
isdnPriPortChannelsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnPriPortChannelsStatus.setStatus("current")
_CpIwfIsdnPriBChannelTable_Object = MibTable
cpIwfIsdnPriBChannelTable = _CpIwfIsdnPriBChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 14)
)
if mibBuilder.loadTexts:
    cpIwfIsdnPriBChannelTable.setStatus("current")
_CpIwfIsdnPriBChannelEntry_Object = MibTableRow
cpIwfIsdnPriBChannelEntry = _CpIwfIsdnPriBChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 14, 1)
)
cpIwfIsdnPriBChannelEntry.setIndexNames(
    (0, "CPIWF-R-MIB", "isdnPriPortNumber"),
    (0, "CPIWF-R-MIB", "isdnPriBChannelNumber"),
)
if mibBuilder.loadTexts:
    cpIwfIsdnPriBChannelEntry.setStatus("current")
_IsdnPriBChannelNumber_Type = Integer32
_IsdnPriBChannelNumber_Object = MibTableColumn
isdnPriBChannelNumber = _IsdnPriBChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 14, 1, 1),
    _IsdnPriBChannelNumber_Type()
)
isdnPriBChannelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnPriBChannelNumber.setStatus("current")


class _IsdnPriBAal2ChannelId_Type(Integer32):
    """Custom type isdnPriBAal2ChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_IsdnPriBAal2ChannelId_Type.__name__ = "Integer32"
_IsdnPriBAal2ChannelId_Object = MibTableColumn
isdnPriBAal2ChannelId = _IsdnPriBAal2ChannelId_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 14, 1, 2),
    _IsdnPriBAal2ChannelId_Type()
)
isdnPriBAal2ChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnPriBAal2ChannelId.setStatus("current")


class _IsdnPriBChannelAdminStatus_Type(Integer32):
    """Custom type isdnPriBChannelAdminStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("shuttingDown", 3),
          ("testing", 4))
    )


_IsdnPriBChannelAdminStatus_Type.__name__ = "Integer32"
_IsdnPriBChannelAdminStatus_Object = MibTableColumn
isdnPriBChannelAdminStatus = _IsdnPriBChannelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 14, 1, 3),
    _IsdnPriBChannelAdminStatus_Type()
)
isdnPriBChannelAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnPriBChannelAdminStatus.setStatus("current")


class _IsdnPriBChannelOperStatus_Type(Integer32):
    """Custom type isdnPriBChannelOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_IsdnPriBChannelOperStatus_Type.__name__ = "Integer32"
_IsdnPriBChannelOperStatus_Object = MibTableColumn
isdnPriBChannelOperStatus = _IsdnPriBChannelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 14, 1, 4),
    _IsdnPriBChannelOperStatus_Type()
)
isdnPriBChannelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPriBChannelOperStatus.setStatus("current")


class _IsdnPriBChannelLabel_Type(OctetString):
    """Custom type isdnPriBChannelLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IsdnPriBChannelLabel_Type.__name__ = "OctetString"
_IsdnPriBChannelLabel_Object = MibTableColumn
isdnPriBChannelLabel = _IsdnPriBChannelLabel_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 14, 1, 5),
    _IsdnPriBChannelLabel_Type()
)
isdnPriBChannelLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnPriBChannelLabel.setStatus("current")


class _IsdnPriBChannelTestType_Type(Integer32):
    """Custom type isdnPriBChannelTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bChannelPhysicalPortLoopback", 1),
          ("bChannelAal2Loopback", 2))
    )


_IsdnPriBChannelTestType_Type.__name__ = "Integer32"
_IsdnPriBChannelTestType_Object = MibTableColumn
isdnPriBChannelTestType = _IsdnPriBChannelTestType_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 14, 1, 6),
    _IsdnPriBChannelTestType_Type()
)
isdnPriBChannelTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnPriBChannelTestType.setStatus("current")


class _IsdnPriBChannelEchoCanceler_Type(Integer32):
    """Custom type isdnPriBChannelEchoCanceler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("off", 2),
          ("on", 3))
    )


_IsdnPriBChannelEchoCanceler_Type.__name__ = "Integer32"
_IsdnPriBChannelEchoCanceler_Object = MibTableColumn
isdnPriBChannelEchoCanceler = _IsdnPriBChannelEchoCanceler_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 14, 1, 7),
    _IsdnPriBChannelEchoCanceler_Type()
)
isdnPriBChannelEchoCanceler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnPriBChannelEchoCanceler.setStatus("current")
_CpIwfIsdnPriBChannelStatsTable_Object = MibTable
cpIwfIsdnPriBChannelStatsTable = _CpIwfIsdnPriBChannelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 15)
)
if mibBuilder.loadTexts:
    cpIwfIsdnPriBChannelStatsTable.setStatus("current")
_CpIwfIsdnPriBChannelStatsEntry_Object = MibTableRow
cpIwfIsdnPriBChannelStatsEntry = _CpIwfIsdnPriBChannelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 15, 1)
)
cpIwfIsdnPriBChannelStatsEntry.setIndexNames(
    (0, "CPIWF-R-MIB", "isdnPriPortNumber"),
    (0, "CPIWF-R-MIB", "isdnPriBChannelNumber"),
)
if mibBuilder.loadTexts:
    cpIwfIsdnPriBChannelStatsEntry.setStatus("current")
_CpIwfIsdnPriPortBChannelActiveSeconds_Type = Counter32
_CpIwfIsdnPriPortBChannelActiveSeconds_Object = MibTableColumn
cpIwfIsdnPriPortBChannelActiveSeconds = _CpIwfIsdnPriPortBChannelActiveSeconds_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 15, 1, 1),
    _CpIwfIsdnPriPortBChannelActiveSeconds_Type()
)
cpIwfIsdnPriPortBChannelActiveSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnPriPortBChannelActiveSeconds.setStatus("current")
_CpIwfIsdnPriPortBChannelFillerOctets_Type = Counter32
_CpIwfIsdnPriPortBChannelFillerOctets_Object = MibTableColumn
cpIwfIsdnPriPortBChannelFillerOctets = _CpIwfIsdnPriPortBChannelFillerOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 15, 1, 2),
    _CpIwfIsdnPriPortBChannelFillerOctets_Type()
)
cpIwfIsdnPriPortBChannelFillerOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnPriPortBChannelFillerOctets.setStatus("current")
_CpIwfIsdnPriPortBChannelDroppedOctets_Type = Counter32
_CpIwfIsdnPriPortBChannelDroppedOctets_Object = MibTableColumn
cpIwfIsdnPriPortBChannelDroppedOctets = _CpIwfIsdnPriPortBChannelDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 15, 1, 3),
    _CpIwfIsdnPriPortBChannelDroppedOctets_Type()
)
cpIwfIsdnPriPortBChannelDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnPriPortBChannelDroppedOctets.setStatus("current")
_CpIwfIsdnPriPortBChannelAal2TxCells_Type = Counter32
_CpIwfIsdnPriPortBChannelAal2TxCells_Object = MibTableColumn
cpIwfIsdnPriPortBChannelAal2TxCells = _CpIwfIsdnPriPortBChannelAal2TxCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 15, 1, 4),
    _CpIwfIsdnPriPortBChannelAal2TxCells_Type()
)
cpIwfIsdnPriPortBChannelAal2TxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnPriPortBChannelAal2TxCells.setStatus("current")
_CpIwfIsdnPriPortBChannelAal2RxCells_Type = Counter32
_CpIwfIsdnPriPortBChannelAal2RxCells_Object = MibTableColumn
cpIwfIsdnPriPortBChannelAal2RxCells = _CpIwfIsdnPriPortBChannelAal2RxCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 15, 1, 5),
    _CpIwfIsdnPriPortBChannelAal2RxCells_Type()
)
cpIwfIsdnPriPortBChannelAal2RxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnPriPortBChannelAal2RxCells.setStatus("current")
_CpIwfIsdnPriDChannelStatsTable_Object = MibTable
cpIwfIsdnPriDChannelStatsTable = _CpIwfIsdnPriDChannelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 17)
)
if mibBuilder.loadTexts:
    cpIwfIsdnPriDChannelStatsTable.setStatus("current")
_CpIwfIsdnPriDChannelStatsEntry_Object = MibTableRow
cpIwfIsdnPriDChannelStatsEntry = _CpIwfIsdnPriDChannelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 17, 1)
)
cpIwfIsdnPriDChannelStatsEntry.setIndexNames(
    (0, "CPIWF-R-MIB", "isdnPriPortNumber"),
)
if mibBuilder.loadTexts:
    cpIwfIsdnPriDChannelStatsEntry.setStatus("current")
_CpIwfIsdnPriPortDChannelActiveSeconds_Type = Counter32
_CpIwfIsdnPriPortDChannelActiveSeconds_Object = MibTableColumn
cpIwfIsdnPriPortDChannelActiveSeconds = _CpIwfIsdnPriPortDChannelActiveSeconds_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 17, 1, 1),
    _CpIwfIsdnPriPortDChannelActiveSeconds_Type()
)
cpIwfIsdnPriPortDChannelActiveSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnPriPortDChannelActiveSeconds.setStatus("current")
_CpIwfIsdnPriPortDChannelFillerOctets_Type = Counter32
_CpIwfIsdnPriPortDChannelFillerOctets_Object = MibTableColumn
cpIwfIsdnPriPortDChannelFillerOctets = _CpIwfIsdnPriPortDChannelFillerOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 17, 1, 2),
    _CpIwfIsdnPriPortDChannelFillerOctets_Type()
)
cpIwfIsdnPriPortDChannelFillerOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnPriPortDChannelFillerOctets.setStatus("current")
_CpIwfIsdnPriPortDChannelDroppedOctets_Type = Counter32
_CpIwfIsdnPriPortDChannelDroppedOctets_Object = MibTableColumn
cpIwfIsdnPriPortDChannelDroppedOctets = _CpIwfIsdnPriPortDChannelDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 17, 1, 3),
    _CpIwfIsdnPriPortDChannelDroppedOctets_Type()
)
cpIwfIsdnPriPortDChannelDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnPriPortDChannelDroppedOctets.setStatus("current")
_CpIwfIsdnPriPortDChannelAal2TxCells_Type = Counter32
_CpIwfIsdnPriPortDChannelAal2TxCells_Object = MibTableColumn
cpIwfIsdnPriPortDChannelAal2TxCells = _CpIwfIsdnPriPortDChannelAal2TxCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 17, 1, 4),
    _CpIwfIsdnPriPortDChannelAal2TxCells_Type()
)
cpIwfIsdnPriPortDChannelAal2TxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnPriPortDChannelAal2TxCells.setStatus("current")
_CpIwfIsdnPriPortDChannelAal2RxCells_Type = Counter32
_CpIwfIsdnPriPortDChannelAal2RxCells_Object = MibTableColumn
cpIwfIsdnPriPortDChannelAal2RxCells = _CpIwfIsdnPriPortDChannelAal2RxCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 17, 1, 5),
    _CpIwfIsdnPriPortDChannelAal2RxCells_Type()
)
cpIwfIsdnPriPortDChannelAal2RxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnPriPortDChannelAal2RxCells.setStatus("current")
_CpIwfIsdnPriPortDChannelHdlcTxCells_Type = Counter32
_CpIwfIsdnPriPortDChannelHdlcTxCells_Object = MibTableColumn
cpIwfIsdnPriPortDChannelHdlcTxCells = _CpIwfIsdnPriPortDChannelHdlcTxCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 17, 1, 6),
    _CpIwfIsdnPriPortDChannelHdlcTxCells_Type()
)
cpIwfIsdnPriPortDChannelHdlcTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnPriPortDChannelHdlcTxCells.setStatus("current")
_CpIwfIsdnPriPortDChannelHdlcRxCells_Type = Counter32
_CpIwfIsdnPriPortDChannelHdlcRxCells_Object = MibTableColumn
cpIwfIsdnPriPortDChannelHdlcRxCells = _CpIwfIsdnPriPortDChannelHdlcRxCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 17, 1, 7),
    _CpIwfIsdnPriPortDChannelHdlcRxCells_Type()
)
cpIwfIsdnPriPortDChannelHdlcRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnPriPortDChannelHdlcRxCells.setStatus("current")
_CpIwfIsdnPriPortDChannelSstedTxCells_Type = Counter32
_CpIwfIsdnPriPortDChannelSstedTxCells_Object = MibTableColumn
cpIwfIsdnPriPortDChannelSstedTxCells = _CpIwfIsdnPriPortDChannelSstedTxCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 17, 1, 8),
    _CpIwfIsdnPriPortDChannelSstedTxCells_Type()
)
cpIwfIsdnPriPortDChannelSstedTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnPriPortDChannelSstedTxCells.setStatus("current")
_CpIwfIsdnPriPortDChannelSstedRxCells_Type = Counter32
_CpIwfIsdnPriPortDChannelSstedRxCells_Object = MibTableColumn
cpIwfIsdnPriPortDChannelSstedRxCells = _CpIwfIsdnPriPortDChannelSstedRxCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 17, 1, 9),
    _CpIwfIsdnPriPortDChannelSstedRxCells_Type()
)
cpIwfIsdnPriPortDChannelSstedRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnPriPortDChannelSstedRxCells.setStatus("current")
_CpIwfIsdnBriPortStatTable_Object = MibTable
cpIwfIsdnBriPortStatTable = _CpIwfIsdnBriPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 18)
)
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortStatTable.setStatus("current")
_CpIwfIsdnBriPortStatEntry_Object = MibTableRow
cpIwfIsdnBriPortStatEntry = _CpIwfIsdnBriPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 18, 1)
)
cpIwfIsdnBriPortStatEntry.setIndexNames(
    (0, "CPIWF-R-MIB", "cpIwfIsdnBriPortNumber"),
    (0, "CPIWF-R-MIB", "cpIwfIsdnBriPortChannel"),
)
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortStatEntry.setStatus("current")


class _CpIwfIsdnBriPortChannel_Type(Integer32):
    """Custom type cpIwfIsdnBriPortChannel based on Integer32"""
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
        *(("wholePort", 1),
          ("briDchannel", 2),
          ("channelB1", 3),
          ("channelB2", 4))
    )


_CpIwfIsdnBriPortChannel_Type.__name__ = "Integer32"
_CpIwfIsdnBriPortChannel_Object = MibTableColumn
cpIwfIsdnBriPortChannel = _CpIwfIsdnBriPortChannel_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 18, 1, 1),
    _CpIwfIsdnBriPortChannel_Type()
)
cpIwfIsdnBriPortChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortChannel.setStatus("current")
_CpIwfIsdnBriPortHdlcFrames_Type = Counter32
_CpIwfIsdnBriPortHdlcFrames_Object = MibTableColumn
cpIwfIsdnBriPortHdlcFrames = _CpIwfIsdnBriPortHdlcFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 18, 1, 2),
    _CpIwfIsdnBriPortHdlcFrames_Type()
)
cpIwfIsdnBriPortHdlcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortHdlcFrames.setStatus("current")
_CpIwfIsdnBriPortHdlcErrors_Type = Counter32
_CpIwfIsdnBriPortHdlcErrors_Object = MibTableColumn
cpIwfIsdnBriPortHdlcErrors = _CpIwfIsdnBriPortHdlcErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 18, 1, 3),
    _CpIwfIsdnBriPortHdlcErrors_Type()
)
cpIwfIsdnBriPortHdlcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortHdlcErrors.setStatus("current")
_CpIwfIsdnBriPortSStedRxPacket_Type = Counter32
_CpIwfIsdnBriPortSStedRxPacket_Object = MibTableColumn
cpIwfIsdnBriPortSStedRxPacket = _CpIwfIsdnBriPortSStedRxPacket_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 18, 1, 4),
    _CpIwfIsdnBriPortSStedRxPacket_Type()
)
cpIwfIsdnBriPortSStedRxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortSStedRxPacket.setStatus("current")
_CpIwfIsdnBriPortSStedRxCRCErrors_Type = Counter32
_CpIwfIsdnBriPortSStedRxCRCErrors_Object = MibTableColumn
cpIwfIsdnBriPortSStedRxCRCErrors = _CpIwfIsdnBriPortSStedRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 18, 1, 5),
    _CpIwfIsdnBriPortSStedRxCRCErrors_Type()
)
cpIwfIsdnBriPortSStedRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortSStedRxCRCErrors.setStatus("current")
_CpIwfIsdnBriPortSStedRxLenErrors_Type = Counter32
_CpIwfIsdnBriPortSStedRxLenErrors_Object = MibTableColumn
cpIwfIsdnBriPortSStedRxLenErrors = _CpIwfIsdnBriPortSStedRxLenErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 18, 1, 6),
    _CpIwfIsdnBriPortSStedRxLenErrors_Type()
)
cpIwfIsdnBriPortSStedRxLenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortSStedRxLenErrors.setStatus("current")
_CpIwfIsdnBriPortSStedRxErrors_Type = Counter32
_CpIwfIsdnBriPortSStedRxErrors_Object = MibTableColumn
cpIwfIsdnBriPortSStedRxErrors = _CpIwfIsdnBriPortSStedRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 18, 1, 7),
    _CpIwfIsdnBriPortSStedRxErrors_Type()
)
cpIwfIsdnBriPortSStedRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortSStedRxErrors.setStatus("current")
_CpIwfIsdnBriChAAL2TxCells_Type = Counter32
_CpIwfIsdnBriChAAL2TxCells_Object = MibTableColumn
cpIwfIsdnBriChAAL2TxCells = _CpIwfIsdnBriChAAL2TxCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 18, 1, 8),
    _CpIwfIsdnBriChAAL2TxCells_Type()
)
cpIwfIsdnBriChAAL2TxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriChAAL2TxCells.setStatus("current")
_CpIwfIsdnBriChAAL2RxCells_Type = Counter32
_CpIwfIsdnBriChAAL2RxCells_Object = MibTableColumn
cpIwfIsdnBriChAAL2RxCells = _CpIwfIsdnBriChAAL2RxCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 18, 1, 9),
    _CpIwfIsdnBriChAAL2RxCells_Type()
)
cpIwfIsdnBriChAAL2RxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriChAAL2RxCells.setStatus("current")
_CpIwfIsdnBriChAAL2RxErrors_Type = Counter32
_CpIwfIsdnBriChAAL2RxErrors_Object = MibTableColumn
cpIwfIsdnBriChAAL2RxErrors = _CpIwfIsdnBriChAAL2RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 5, 1, 18, 1, 10),
    _CpIwfIsdnBriChAAL2RxErrors_Type()
)
cpIwfIsdnBriChAAL2RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriChAAL2RxErrors.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPIWF-R-MIB",
    **{"radExperimental": radExperimental,
       "cpIwfMIB": cpIwfMIB,
       "cpIwfMIBObjects": cpIwfMIBObjects,
       "cpIwf": cpIwf,
       "cpIwfIfIndex": cpIwfIfIndex,
       "cpIwfVpi": cpIwfVpi,
       "cpIwfVci": cpIwfVci,
       "cpIwfVccMib": cpIwfVccMib,
       "cpIwfNumPotsPorts": cpIwfNumPotsPorts,
       "cpIwfNumIsdnBriPorts": cpIwfNumIsdnBriPorts,
       "cpIwfTimingReference": cpIwfTimingReference,
       "cpIwfPotsPortEncodingSelectionMode": cpIwfPotsPortEncodingSelectionMode,
       "cpIwfIsdnBriPortEncodingSelectionMode": cpIwfIsdnBriPortEncodingSelectionMode,
       "cpIwfNumDs0Bundles": cpIwfNumDs0Bundles,
       "cpIwfLineSignaling": cpIwfLineSignaling,
       "cpIwfNumIsdnPriPorts": cpIwfNumIsdnPriPorts,
       "cpIwfIsdnPriPortEncodingSelectionMode": cpIwfIsdnPriPortEncodingSelectionMode,
       "cpIwfAal2Profile": cpIwfAal2Profile,
       "cpIwfAal2ApplicationIdentifier": cpIwfAal2ApplicationIdentifier,
       "cpIwfAal2CpsMaxMultiplexedChannels": cpIwfAal2CpsMaxMultiplexedChannels,
       "cpIwfAal2CpsMaxSDULength": cpIwfAal2CpsMaxSDULength,
       "cpIwfAal2CpsCIDLowerLimit": cpIwfAal2CpsCIDLowerLimit,
       "cpIwfAal2CpsCIDUpperLimit": cpIwfAal2CpsCIDUpperLimit,
       "cpIwfAal2CpsOptimisation": cpIwfAal2CpsOptimisation,
       "cpIwfAal2SscsFaxModulationTransport": cpIwfAal2SscsFaxModulationTransport,
       "cpIwfAal2SscsCasSignalingTransport": cpIwfAal2SscsCasSignalingTransport,
       "cpIwfAal2SscsDtmfDigitPacketTransport": cpIwfAal2SscsDtmfDigitPacketTransport,
       "cpIwfAal2SscsPcmEncoding": cpIwfAal2SscsPcmEncoding,
       "cpIwfAal2SscsMaxSssarSduLength": cpIwfAal2SscsMaxSssarSduLength,
       "cpIwfAal2SscsPredefinedProfileIdentifier": cpIwfAal2SscsPredefinedProfileIdentifier,
       "cpIwfAal2SscsIeeeOui": cpIwfAal2SscsIeeeOui,
       "cpIwfPotsPortTable": cpIwfPotsPortTable,
       "cpIwfPotsPortEntry": cpIwfPotsPortEntry,
       "cpIwfPotsPortNumber": cpIwfPotsPortNumber,
       "cpIwfPotsPortPhysicalPort": cpIwfPotsPortPhysicalPort,
       "cpIwfPotsPortChannelId": cpIwfPotsPortChannelId,
       "cpIwfPotsPortTestMode": cpIwfPotsPortTestMode,
       "cpIwfPotsPortSignalingMethod": cpIwfPotsPortSignalingMethod,
       "cpIwfPotsPortRxBytesPerCell": cpIwfPotsPortRxBytesPerCell,
       "cpIwfPotsPortTxBytesPerCell": cpIwfPotsPortTxBytesPerCell,
       "cpIwfPotsPortContCheck": cpIwfPotsPortContCheck,
       "cpIwfPotsPortStatus": cpIwfPotsPortStatus,
       "cpIwfIsdnBriPortTable": cpIwfIsdnBriPortTable,
       "cpIwfIsdnBriPortEntry": cpIwfIsdnBriPortEntry,
       "cpIwfIsdnBriPortNumber": cpIwfIsdnBriPortNumber,
       "cpIwfIsdnBriPortPhysicalPort": cpIwfIsdnBriPortPhysicalPort,
       "cpIwfIsdnBriPortChannelIdD": cpIwfIsdnBriPortChannelIdD,
       "cpIwfIsdnBriPortChannelIdB1": cpIwfIsdnBriPortChannelIdB1,
       "cpIwfIsdnBriPortChannelIdB2": cpIwfIsdnBriPortChannelIdB2,
       "cpIwfIsdnBriPortRxBytesPerCell": cpIwfIsdnBriPortRxBytesPerCell,
       "cpIwfIsdnBriPortTxBytesPerCell": cpIwfIsdnBriPortTxBytesPerCell,
       "cpIwfIsdnBriPortContCheck": cpIwfIsdnBriPortContCheck,
       "cpIwfIsdnBriPortEchoCanceler": cpIwfIsdnBriPortEchoCanceler,
       "cpIwfIsdnBriPortL1Status": cpIwfIsdnBriPortL1Status,
       "cpIwfIsdnBriPortDChRxPCMStatus": cpIwfIsdnBriPortDChRxPCMStatus,
       "cpIwfIsdnBriPortB1ChRxPCMStatus": cpIwfIsdnBriPortB1ChRxPCMStatus,
       "cpIwfIsdnBriPortB2ChRxPCMStatus": cpIwfIsdnBriPortB2ChRxPCMStatus,
       "cpIwfIsdnBriPortDChTxPCMStatus": cpIwfIsdnBriPortDChTxPCMStatus,
       "cpIwfIsdnBriPortB1ChTxPCMStatus": cpIwfIsdnBriPortB1ChTxPCMStatus,
       "cpIwfIsdnBriPortB2ChTxPCMStatus": cpIwfIsdnBriPortB2ChTxPCMStatus,
       "cpIwfDs0BundleTable": cpIwfDs0BundleTable,
       "cpIwfDs0BundleEntry": cpIwfDs0BundleEntry,
       "cpIwfDs0BundleNumber": cpIwfDs0BundleNumber,
       "cpIwfDs0BundleIfIndex": cpIwfDs0BundleIfIndex,
       "cpIwfDs0BundleChannelId": cpIwfDs0BundleChannelId,
       "cpIwfDs0BundleRxBytesPerCell": cpIwfDs0BundleRxBytesPerCell,
       "cpIwfDs0BundleTxBytesPerCell": cpIwfDs0BundleTxBytesPerCell,
       "cpIwfDs0BundleContCheck": cpIwfDs0BundleContCheck,
       "cpIwfDs0BundleLineSignaling": cpIwfDs0BundleLineSignaling,
       "cpIwfStats": cpIwfStats,
       "cpIwfAal2Stats": cpIwfAal2Stats,
       "cpIwfAal2StatsCpsInPkts": cpIwfAal2StatsCpsInPkts,
       "cpIwfAal2StatsCpsOutPkts": cpIwfAal2StatsCpsOutPkts,
       "cpIwfAal2StatsCpsParityErrors": cpIwfAal2StatsCpsParityErrors,
       "cpIwfAal2StatsCpsSeqNumErrors": cpIwfAal2StatsCpsSeqNumErrors,
       "cpIwfAal2StatsCpsOsfErrors": cpIwfAal2StatsCpsOsfErrors,
       "cpIwfAal2StatsCpsHecErrors": cpIwfAal2StatsCpsHecErrors,
       "cpIwfAal2StatsCpsUuiErrors": cpIwfAal2StatsCpsUuiErrors,
       "cpIwfAal2StatsCpsCidErrors": cpIwfAal2StatsCpsCidErrors,
       "cpIwfV5Pstn": cpIwfV5Pstn,
       "cpIwfV5PstnGeneral": cpIwfV5PstnGeneral,
       "cpIwfCallCollisionPriority": cpIwfCallCollisionPriority,
       "cpIwfNationalProfile": cpIwfNationalProfile,
       "cpIwfMeterPulseFrequency": cpIwfMeterPulseFrequency,
       "cpIwfOffHookMinTime": cpIwfOffHookMinTime,
       "cpIwfOnHookMinTime": cpIwfOnHookMinTime,
       "cpIwfRegisterRecallMinTime": cpIwfRegisterRecallMinTime,
       "cpIwfDigitMinBreakPeriod": cpIwfDigitMinBreakPeriod,
       "cpIwfDigitMaxBreakPeriod": cpIwfDigitMaxBreakPeriod,
       "cpIwfDigitMinMakePeriod": cpIwfDigitMinMakePeriod,
       "cpIwfDigitMaxMakePeriod": cpIwfDigitMaxMakePeriod,
       "cpIwfInterDigitTime": cpIwfInterDigitTime,
       "cpIwfCadencedRingingTypeTable": cpIwfCadencedRingingTypeTable,
       "cpIwfCadencedRingingTypeEntry": cpIwfCadencedRingingTypeEntry,
       "cpIwfCadencedRingingType": cpIwfCadencedRingingType,
       "cpIwfCadencedRingingNumPeriods": cpIwfCadencedRingingNumPeriods,
       "cpIwfCadencedRingingOnPeriod1": cpIwfCadencedRingingOnPeriod1,
       "cpIwfCadencedRingingOffPeriod1": cpIwfCadencedRingingOffPeriod1,
       "cpIwfCadencedRingingOnPeriod2": cpIwfCadencedRingingOnPeriod2,
       "cpIwfCadencedRingingOffPeriod2": cpIwfCadencedRingingOffPeriod2,
       "cpIwfCadencedRingingOnPeriod3": cpIwfCadencedRingingOnPeriod3,
       "cpIwfCadencedRingingOffPeriod3": cpIwfCadencedRingingOffPeriod3,
       "cpIwfCadencedRingingOnPeriod4": cpIwfCadencedRingingOnPeriod4,
       "cpIwfCadencedRingingOffPeriod4": cpIwfCadencedRingingOffPeriod4,
       "cpIwfCadencedRingingOnPeriod5": cpIwfCadencedRingingOnPeriod5,
       "cpIwfCadencedRingingOffPeriod5": cpIwfCadencedRingingOffPeriod5,
       "cpIwfCadencedRingingOnPeriod6": cpIwfCadencedRingingOnPeriod6,
       "cpIwfCadencedRingingOffPeriod6": cpIwfCadencedRingingOffPeriod6,
       "cpIwfCadencedRingingOnPeriod7": cpIwfCadencedRingingOnPeriod7,
       "cpIwfCadencedRingingOffPeriod7": cpIwfCadencedRingingOffPeriod7,
       "cpIwfCadencedRingingOnPeriod8": cpIwfCadencedRingingOnPeriod8,
       "cpIwfCadencedRingingOffPeriod8": cpIwfCadencedRingingOffPeriod8,
       "cpIwfCadencedRingingOnPeriod9": cpIwfCadencedRingingOnPeriod9,
       "cpIwfCadencedRingingOffPeriod9": cpIwfCadencedRingingOffPeriod9,
       "cpIwfCadencedRingingOnPeriod10": cpIwfCadencedRingingOnPeriod10,
       "cpIwfCadencedRingingOffPeriod10": cpIwfCadencedRingingOffPeriod10,
       "cpIwfCadencedRingingTypeRowStatus": cpIwfCadencedRingingTypeRowStatus,
       "cpIwfPulseDurationTypeTable": cpIwfPulseDurationTypeTable,
       "cpIwfPulseDurationTypeEntry": cpIwfPulseDurationTypeEntry,
       "cpIwfPulseType": cpIwfPulseType,
       "cpIwfPulseDurationType": cpIwfPulseDurationType,
       "cpIwfPulseDurationNumPeriods": cpIwfPulseDurationNumPeriods,
       "cpIwfPulseDurationOnPeriod1": cpIwfPulseDurationOnPeriod1,
       "cpIwfPulseDurationOffPeriod1": cpIwfPulseDurationOffPeriod1,
       "cpIwfPulseDurationOnPeriod2": cpIwfPulseDurationOnPeriod2,
       "cpIwfPulseDurationOffPeriod2": cpIwfPulseDurationOffPeriod2,
       "cpIwfPulseDurationOnPeriod3": cpIwfPulseDurationOnPeriod3,
       "cpIwfPulseDurationOffPeriod3": cpIwfPulseDurationOffPeriod3,
       "cpIwfPulseDurationOnPeriod4": cpIwfPulseDurationOnPeriod4,
       "cpIwfPulseDurationOffPeriod4": cpIwfPulseDurationOffPeriod4,
       "cpIwfPulseDurationOnPeriod5": cpIwfPulseDurationOnPeriod5,
       "cpIwfPulseDurationOffPeriod5": cpIwfPulseDurationOffPeriod5,
       "cpIwfPulseDurationTypeRowStatus": cpIwfPulseDurationTypeRowStatus,
       "cpIwfDurationTypeTable": cpIwfDurationTypeTable,
       "cpIwfDurationTypeEntry": cpIwfDurationTypeEntry,
       "cpIwfSignal": cpIwfSignal,
       "cpIwfDurationType": cpIwfDurationType,
       "cpIwfDuration": cpIwfDuration,
       "cpIwfDurationTypeRowStatus": cpIwfDurationTypeRowStatus,
       "cpIwfRateTypeTable": cpIwfRateTypeTable,
       "cpIwfRateTypeEntry": cpIwfRateTypeEntry,
       "cpIwfRateType": cpIwfRateType,
       "cpIwfRate": cpIwfRate,
       "cpIwfRateTypeRowStatus": cpIwfRateTypeRowStatus,
       "cpIwfAttenuationValueTable": cpIwfAttenuationValueTable,
       "cpIwfAttenuationValueEntry": cpIwfAttenuationValueEntry,
       "cpIwfAttenuationValue": cpIwfAttenuationValue,
       "cpIwfAttenuation": cpIwfAttenuation,
       "cpIwfAttenuationValueRowStatus": cpIwfAttenuationValueRowStatus,
       "cpIwfTxAttenuation": cpIwfTxAttenuation,
       "cpIwfUpstreamPhysicalBandwidth": cpIwfUpstreamPhysicalBandwidth,
       "cpIwfDownstreamPhysicalBandwidth": cpIwfDownstreamPhysicalBandwidth,
       "cpIwfIsdnPriPortTable": cpIwfIsdnPriPortTable,
       "cpIwfIsdnPriPortEntry": cpIwfIsdnPriPortEntry,
       "isdnPriPortNumber": isdnPriPortNumber,
       "isdnPriPhysicalPort": isdnPriPhysicalPort,
       "isdnPriNumBChannels": isdnPriNumBChannels,
       "isdnPriDAal2ChannelId": isdnPriDAal2ChannelId,
       "isdnPriPortLabel": isdnPriPortLabel,
       "isdnPriPortTestType": isdnPriPortTestType,
       "isdnPriPortChannelsStatus": isdnPriPortChannelsStatus,
       "cpIwfIsdnPriBChannelTable": cpIwfIsdnPriBChannelTable,
       "cpIwfIsdnPriBChannelEntry": cpIwfIsdnPriBChannelEntry,
       "isdnPriBChannelNumber": isdnPriBChannelNumber,
       "isdnPriBAal2ChannelId": isdnPriBAal2ChannelId,
       "isdnPriBChannelAdminStatus": isdnPriBChannelAdminStatus,
       "isdnPriBChannelOperStatus": isdnPriBChannelOperStatus,
       "isdnPriBChannelLabel": isdnPriBChannelLabel,
       "isdnPriBChannelTestType": isdnPriBChannelTestType,
       "isdnPriBChannelEchoCanceler": isdnPriBChannelEchoCanceler,
       "cpIwfIsdnPriBChannelStatsTable": cpIwfIsdnPriBChannelStatsTable,
       "cpIwfIsdnPriBChannelStatsEntry": cpIwfIsdnPriBChannelStatsEntry,
       "cpIwfIsdnPriPortBChannelActiveSeconds": cpIwfIsdnPriPortBChannelActiveSeconds,
       "cpIwfIsdnPriPortBChannelFillerOctets": cpIwfIsdnPriPortBChannelFillerOctets,
       "cpIwfIsdnPriPortBChannelDroppedOctets": cpIwfIsdnPriPortBChannelDroppedOctets,
       "cpIwfIsdnPriPortBChannelAal2TxCells": cpIwfIsdnPriPortBChannelAal2TxCells,
       "cpIwfIsdnPriPortBChannelAal2RxCells": cpIwfIsdnPriPortBChannelAal2RxCells,
       "cpIwfIsdnPriDChannelStatsTable": cpIwfIsdnPriDChannelStatsTable,
       "cpIwfIsdnPriDChannelStatsEntry": cpIwfIsdnPriDChannelStatsEntry,
       "cpIwfIsdnPriPortDChannelActiveSeconds": cpIwfIsdnPriPortDChannelActiveSeconds,
       "cpIwfIsdnPriPortDChannelFillerOctets": cpIwfIsdnPriPortDChannelFillerOctets,
       "cpIwfIsdnPriPortDChannelDroppedOctets": cpIwfIsdnPriPortDChannelDroppedOctets,
       "cpIwfIsdnPriPortDChannelAal2TxCells": cpIwfIsdnPriPortDChannelAal2TxCells,
       "cpIwfIsdnPriPortDChannelAal2RxCells": cpIwfIsdnPriPortDChannelAal2RxCells,
       "cpIwfIsdnPriPortDChannelHdlcTxCells": cpIwfIsdnPriPortDChannelHdlcTxCells,
       "cpIwfIsdnPriPortDChannelHdlcRxCells": cpIwfIsdnPriPortDChannelHdlcRxCells,
       "cpIwfIsdnPriPortDChannelSstedTxCells": cpIwfIsdnPriPortDChannelSstedTxCells,
       "cpIwfIsdnPriPortDChannelSstedRxCells": cpIwfIsdnPriPortDChannelSstedRxCells,
       "cpIwfIsdnBriPortStatTable": cpIwfIsdnBriPortStatTable,
       "cpIwfIsdnBriPortStatEntry": cpIwfIsdnBriPortStatEntry,
       "cpIwfIsdnBriPortChannel": cpIwfIsdnBriPortChannel,
       "cpIwfIsdnBriPortHdlcFrames": cpIwfIsdnBriPortHdlcFrames,
       "cpIwfIsdnBriPortHdlcErrors": cpIwfIsdnBriPortHdlcErrors,
       "cpIwfIsdnBriPortSStedRxPacket": cpIwfIsdnBriPortSStedRxPacket,
       "cpIwfIsdnBriPortSStedRxCRCErrors": cpIwfIsdnBriPortSStedRxCRCErrors,
       "cpIwfIsdnBriPortSStedRxLenErrors": cpIwfIsdnBriPortSStedRxLenErrors,
       "cpIwfIsdnBriPortSStedRxErrors": cpIwfIsdnBriPortSStedRxErrors,
       "cpIwfIsdnBriChAAL2TxCells": cpIwfIsdnBriChAAL2TxCells,
       "cpIwfIsdnBriChAAL2RxCells": cpIwfIsdnBriChAAL2RxCells,
       "cpIwfIsdnBriChAAL2RxErrors": cpIwfIsdnBriChAAL2RxErrors}
)
