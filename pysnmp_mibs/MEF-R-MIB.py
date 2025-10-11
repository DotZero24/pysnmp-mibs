# SNMP MIB module (MEF-R-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/MEF-R-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:03 2025
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

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(radExperimental,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "radExperimental")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mefMIBR = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TCVlanId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class TCBurstSizeV2(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"


class TCV2DefaultUserPriority(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class TCEthFrameHandling(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("untagged", 1),
          ("noChange", 2),
          ("changeVlan", 3),
          ("addVlan", 4),
          ("removeVlan", 5),
          ("rangeVlan", 6))
    )



class TCSLAPrioritySource(TextualConvention, Integer32):
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
        *(("defUserPrio", 1),
          ("ieee802dot1p", 2),
          ("tos", 3),
          ("diffServ", 4),
          ("ieee802dot1q", 5),
          ("copy", 6),
          ("userMarkingTable", 7),
          ("spVlanId", 8),
          ("spVlanIdAndPBit", 9))
    )



class TCEvcId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )



class TCVTIdV2(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_MefObjects_ObjectIdentity = ObjectIdentity
mefObjects = _MefObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1)
)
_MefrScalarObjects_ObjectIdentity = ObjectIdentity
mefrScalarObjects = _MefrScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 1)
)


class _MefrBwRoundUp_Type(TruthValue):
    """Custom type mefrBwRoundUp based on TruthValue"""
    defaultValue = 2


_MefrBwRoundUp_Type.__name__ = "TruthValue"
_MefrBwRoundUp_Object = MibScalar
mefrBwRoundUp = _MefrBwRoundUp_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 1, 1),
    _MefrBwRoundUp_Type()
)
mefrBwRoundUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefrBwRoundUp.setStatus("current")


class _MefrEnvelopeRanks_Type(Unsigned32):
    """Custom type mefrEnvelopeRanks based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_MefrEnvelopeRanks_Type.__name__ = "Unsigned32"
_MefrEnvelopeRanks_Object = MibScalar
mefrEnvelopeRanks = _MefrEnvelopeRanks_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 1, 2),
    _MefrEnvelopeRanks_Type()
)
mefrEnvelopeRanks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefrEnvelopeRanks.setStatus("current")


class _HsQBlockMapping_Type(Integer32):
    """Custom type hsQBlockMapping based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("slot1", 1),
          ("slot4", 4))
    )


_HsQBlockMapping_Type.__name__ = "Integer32"
_HsQBlockMapping_Object = MibScalar
hsQBlockMapping = _HsQBlockMapping_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 1, 3),
    _HsQBlockMapping_Type()
)
hsQBlockMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hsQBlockMapping.setStatus("current")
_BwProfileObjects_ObjectIdentity = ObjectIdentity
bwProfileObjects = _BwProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3)
)
_BwProfileTable_Object = MibTable
bwProfileTable = _BwProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    bwProfileTable.setStatus("current")
_BwProfileEntry_Object = MibTableRow
bwProfileEntry = _BwProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 1, 1)
)
bwProfileEntry.setIndexNames(
    (0, "MEF-R-MIB", "bwProfileID"),
    (0, "MEF-R-MIB", "bwProfileIndex"),
)
if mibBuilder.loadTexts:
    bwProfileEntry.setStatus("current")
_BwProfileID_Type = TCVTIdV2
_BwProfileID_Object = MibTableColumn
bwProfileID = _BwProfileID_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 1, 1, 1),
    _BwProfileID_Type()
)
bwProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bwProfileID.setStatus("current")
_BwProfileIndex_Type = Unsigned32
_BwProfileIndex_Object = MibTableColumn
bwProfileIndex = _BwProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 1, 1, 2),
    _BwProfileIndex_Type()
)
bwProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bwProfileIndex.setStatus("current")
_BwProfileRowStatus_Type = RowStatus
_BwProfileRowStatus_Object = MibTableColumn
bwProfileRowStatus = _BwProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 1, 1, 3),
    _BwProfileRowStatus_Type()
)
bwProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwProfileRowStatus.setStatus("current")
_BwProfileCIR_Type = Unsigned32
_BwProfileCIR_Object = MibTableColumn
bwProfileCIR = _BwProfileCIR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 1, 1, 4),
    _BwProfileCIR_Type()
)
bwProfileCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwProfileCIR.setStatus("current")
if mibBuilder.loadTexts:
    bwProfileCIR.setUnits("Kbps")
_BwProfileCBS_Type = TCBurstSizeV2
_BwProfileCBS_Object = MibTableColumn
bwProfileCBS = _BwProfileCBS_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 1, 1, 5),
    _BwProfileCBS_Type()
)
bwProfileCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwProfileCBS.setStatus("current")
if mibBuilder.loadTexts:
    bwProfileCBS.setUnits("Octets")
_BwProfileEIR_Type = Unsigned32
_BwProfileEIR_Object = MibTableColumn
bwProfileEIR = _BwProfileEIR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 1, 1, 8),
    _BwProfileEIR_Type()
)
bwProfileEIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwProfileEIR.setStatus("current")
if mibBuilder.loadTexts:
    bwProfileEIR.setUnits("Kbps")
_BwProfileEBS_Type = TCBurstSizeV2
_BwProfileEBS_Object = MibTableColumn
bwProfileEBS = _BwProfileEBS_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 1, 1, 9),
    _BwProfileEBS_Type()
)
bwProfileEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwProfileEBS.setStatus("current")
if mibBuilder.loadTexts:
    bwProfileEBS.setUnits("Octets")


class _BwProfileColorAware_Type(TruthValue):
    """Custom type bwProfileColorAware based on TruthValue"""
    defaultValue = 2


_BwProfileColorAware_Type.__name__ = "TruthValue"
_BwProfileColorAware_Object = MibTableColumn
bwProfileColorAware = _BwProfileColorAware_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 1, 1, 12),
    _BwProfileColorAware_Type()
)
bwProfileColorAware.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwProfileColorAware.setStatus("current")


class _BwProfileColorAwareAdmissionOption_Type(TruthValue):
    """Custom type bwProfileColorAwareAdmissionOption based on TruthValue"""
    defaultValue = 2


_BwProfileColorAwareAdmissionOption_Type.__name__ = "TruthValue"
_BwProfileColorAwareAdmissionOption_Object = MibTableColumn
bwProfileColorAwareAdmissionOption = _BwProfileColorAwareAdmissionOption_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 1, 1, 13),
    _BwProfileColorAwareAdmissionOption_Type()
)
bwProfileColorAwareAdmissionOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwProfileColorAwareAdmissionOption.setStatus("current")
_BwProfileName_Type = SnmpAdminString
_BwProfileName_Object = MibTableColumn
bwProfileName = _BwProfileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 1, 1, 14),
    _BwProfileName_Type()
)
bwProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwProfileName.setStatus("current")


class _BwProfileGranularity_Type(Integer32):
    """Custom type bwProfileGranularity based on Integer32"""
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
        *(("r64kbps", 2),
          ("r1Mbps", 3),
          ("r10Mbps", 4),
          ("r100Mbps", 5))
    )


_BwProfileGranularity_Type.__name__ = "Integer32"
_BwProfileGranularity_Object = MibTableColumn
bwProfileGranularity = _BwProfileGranularity_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 1, 1, 15),
    _BwProfileGranularity_Type()
)
bwProfileGranularity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwProfileGranularity.setStatus("current")


class _BwProfilePolicedTraffic_Type(Integer32):
    """Custom type bwProfilePolicedTraffic based on Integer32"""
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
        *(("all", 2),
          ("broadcast", 3),
          ("multicast", 4),
          ("unknownUnicast", 5),
          ("broadcastAndMulticast", 6),
          ("broadcastAndMulticastAndUnknownUnicast", 7))
    )


_BwProfilePolicedTraffic_Type.__name__ = "Integer32"
_BwProfilePolicedTraffic_Object = MibTableColumn
bwProfilePolicedTraffic = _BwProfilePolicedTraffic_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 1, 1, 16),
    _BwProfilePolicedTraffic_Type()
)
bwProfilePolicedTraffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwProfilePolicedTraffic.setStatus("current")
_BwProfileCompensation_Type = Unsigned32
_BwProfileCompensation_Object = MibTableColumn
bwProfileCompensation = _BwProfileCompensation_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 1, 1, 17),
    _BwProfileCompensation_Type()
)
bwProfileCompensation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwProfileCompensation.setStatus("current")
if mibBuilder.loadTexts:
    bwProfileCompensation.setUnits("Octets")
_EnvelopeBwProfileTable_Object = MibTable
envelopeBwProfileTable = _EnvelopeBwProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 2)
)
if mibBuilder.loadTexts:
    envelopeBwProfileTable.setStatus("current")
_EnvelopeBwProfileEntry_Object = MibTableRow
envelopeBwProfileEntry = _EnvelopeBwProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 2, 1)
)
envelopeBwProfileEntry.setIndexNames(
    (0, "MEF-R-MIB", "envelopeBwProfileIndex"),
)
if mibBuilder.loadTexts:
    envelopeBwProfileEntry.setStatus("current")
_EnvelopeBwProfileIndex_Type = Unsigned32
_EnvelopeBwProfileIndex_Object = MibTableColumn
envelopeBwProfileIndex = _EnvelopeBwProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 2, 1, 1),
    _EnvelopeBwProfileIndex_Type()
)
envelopeBwProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    envelopeBwProfileIndex.setStatus("current")


class _EnvelopeBwProfileName_Type(SnmpAdminString):
    """Custom type envelopeBwProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EnvelopeBwProfileName_Type.__name__ = "SnmpAdminString"
_EnvelopeBwProfileName_Object = MibTableColumn
envelopeBwProfileName = _EnvelopeBwProfileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 2, 1, 2),
    _EnvelopeBwProfileName_Type()
)
envelopeBwProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    envelopeBwProfileName.setStatus("current")
_EnvelopeBwProfileRowStatus_Type = RowStatus
_EnvelopeBwProfileRowStatus_Object = MibTableColumn
envelopeBwProfileRowStatus = _EnvelopeBwProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 2, 1, 3),
    _EnvelopeBwProfileRowStatus_Type()
)
envelopeBwProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    envelopeBwProfileRowStatus.setStatus("current")


class _EnvelopeBwProfileCouplingFlagPolicy_Type(Integer32):
    """Custom type envelopeBwProfileCouplingFlagPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("sharingExcessBw", 2),
          ("uncoupledBwSharing", 3))
    )


_EnvelopeBwProfileCouplingFlagPolicy_Type.__name__ = "Integer32"
_EnvelopeBwProfileCouplingFlagPolicy_Object = MibTableColumn
envelopeBwProfileCouplingFlagPolicy = _EnvelopeBwProfileCouplingFlagPolicy_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 2, 1, 4),
    _EnvelopeBwProfileCouplingFlagPolicy_Type()
)
envelopeBwProfileCouplingFlagPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    envelopeBwProfileCouplingFlagPolicy.setStatus("current")


class _EnvelopeBwProfileCouplingFlag0_Type(Unsigned32):
    """Custom type envelopeBwProfileCouplingFlag0 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_EnvelopeBwProfileCouplingFlag0_Type.__name__ = "Unsigned32"
_EnvelopeBwProfileCouplingFlag0_Object = MibTableColumn
envelopeBwProfileCouplingFlag0 = _EnvelopeBwProfileCouplingFlag0_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 2, 1, 5),
    _EnvelopeBwProfileCouplingFlag0_Type()
)
envelopeBwProfileCouplingFlag0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    envelopeBwProfileCouplingFlag0.setStatus("current")


class _EnvelopeBwProfileColorMode_Type(Integer32):
    """Custom type envelopeBwProfileColorMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("colorAware", 1),
          ("colorBlind", 2))
    )


_EnvelopeBwProfileColorMode_Type.__name__ = "Integer32"
_EnvelopeBwProfileColorMode_Object = MibTableColumn
envelopeBwProfileColorMode = _EnvelopeBwProfileColorMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 2, 1, 6),
    _EnvelopeBwProfileColorMode_Type()
)
envelopeBwProfileColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    envelopeBwProfileColorMode.setStatus("current")


class _EnvelopeBwProfileCompensation_Type(Unsigned32):
    """Custom type envelopeBwProfileCompensation based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_EnvelopeBwProfileCompensation_Type.__name__ = "Unsigned32"
_EnvelopeBwProfileCompensation_Object = MibTableColumn
envelopeBwProfileCompensation = _EnvelopeBwProfileCompensation_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 2, 1, 7),
    _EnvelopeBwProfileCompensation_Type()
)
envelopeBwProfileCompensation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    envelopeBwProfileCompensation.setStatus("current")
if mibBuilder.loadTexts:
    envelopeBwProfileCompensation.setUnits("bytes")
_EnvelopeBwProfileCosTable_Object = MibTable
envelopeBwProfileCosTable = _EnvelopeBwProfileCosTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 3)
)
if mibBuilder.loadTexts:
    envelopeBwProfileCosTable.setStatus("current")
_EnvelopeBwProfileCosEntry_Object = MibTableRow
envelopeBwProfileCosEntry = _EnvelopeBwProfileCosEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 3, 1)
)
envelopeBwProfileCosEntry.setIndexNames(
    (0, "MEF-R-MIB", "envelopeBwProfileIndex"),
    (0, "MEF-R-MIB", "envelopeBwProfileCosIndex"),
)
if mibBuilder.loadTexts:
    envelopeBwProfileCosEntry.setStatus("current")


class _EnvelopeBwProfileCosIndex_Type(Unsigned32):
    """Custom type envelopeBwProfileCosIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EnvelopeBwProfileCosIndex_Type.__name__ = "Unsigned32"
_EnvelopeBwProfileCosIndex_Object = MibTableColumn
envelopeBwProfileCosIndex = _EnvelopeBwProfileCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 3, 1, 1),
    _EnvelopeBwProfileCosIndex_Type()
)
envelopeBwProfileCosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    envelopeBwProfileCosIndex.setStatus("current")
_EnvelopeBwProfileCosRowStatus_Type = RowStatus
_EnvelopeBwProfileCosRowStatus_Object = MibTableColumn
envelopeBwProfileCosRowStatus = _EnvelopeBwProfileCosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 3, 1, 2),
    _EnvelopeBwProfileCosRowStatus_Type()
)
envelopeBwProfileCosRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    envelopeBwProfileCosRowStatus.setStatus("current")


class _EnvelopeBwProfileCosCir_Type(Gauge32):
    """Custom type envelopeBwProfileCosCir based on Gauge32"""
    defaultValue = 0


_EnvelopeBwProfileCosCir_Type.__name__ = "Gauge32"
_EnvelopeBwProfileCosCir_Object = MibTableColumn
envelopeBwProfileCosCir = _EnvelopeBwProfileCosCir_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 3, 1, 3),
    _EnvelopeBwProfileCosCir_Type()
)
envelopeBwProfileCosCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    envelopeBwProfileCosCir.setStatus("current")
if mibBuilder.loadTexts:
    envelopeBwProfileCosCir.setUnits("kbps")


class _EnvelopeBwProfileCosCirMax_Type(Gauge32):
    """Custom type envelopeBwProfileCosCirMax based on Gauge32"""
    defaultValue = 10000000


_EnvelopeBwProfileCosCirMax_Type.__name__ = "Gauge32"
_EnvelopeBwProfileCosCirMax_Object = MibTableColumn
envelopeBwProfileCosCirMax = _EnvelopeBwProfileCosCirMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 3, 1, 4),
    _EnvelopeBwProfileCosCirMax_Type()
)
envelopeBwProfileCosCirMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    envelopeBwProfileCosCirMax.setStatus("current")
if mibBuilder.loadTexts:
    envelopeBwProfileCosCirMax.setUnits("kbps")


class _EnvelopeBwProfileCosCbs_Type(Gauge32):
    """Custom type envelopeBwProfileCosCbs based on Gauge32"""
    defaultValue = 0


_EnvelopeBwProfileCosCbs_Type.__name__ = "Gauge32"
_EnvelopeBwProfileCosCbs_Object = MibTableColumn
envelopeBwProfileCosCbs = _EnvelopeBwProfileCosCbs_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 3, 1, 5),
    _EnvelopeBwProfileCosCbs_Type()
)
envelopeBwProfileCosCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    envelopeBwProfileCosCbs.setStatus("current")
if mibBuilder.loadTexts:
    envelopeBwProfileCosCbs.setUnits("bytes")


class _EnvelopeBwProfileCosEir_Type(Gauge32):
    """Custom type envelopeBwProfileCosEir based on Gauge32"""
    defaultValue = 0


_EnvelopeBwProfileCosEir_Type.__name__ = "Gauge32"
_EnvelopeBwProfileCosEir_Object = MibTableColumn
envelopeBwProfileCosEir = _EnvelopeBwProfileCosEir_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 3, 1, 6),
    _EnvelopeBwProfileCosEir_Type()
)
envelopeBwProfileCosEir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    envelopeBwProfileCosEir.setStatus("current")
if mibBuilder.loadTexts:
    envelopeBwProfileCosEir.setUnits("kbps")


class _EnvelopeBwProfileCosEirMax_Type(Gauge32):
    """Custom type envelopeBwProfileCosEirMax based on Gauge32"""
    defaultValue = 10000000


_EnvelopeBwProfileCosEirMax_Type.__name__ = "Gauge32"
_EnvelopeBwProfileCosEirMax_Object = MibTableColumn
envelopeBwProfileCosEirMax = _EnvelopeBwProfileCosEirMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 3, 1, 7),
    _EnvelopeBwProfileCosEirMax_Type()
)
envelopeBwProfileCosEirMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    envelopeBwProfileCosEirMax.setStatus("current")
if mibBuilder.loadTexts:
    envelopeBwProfileCosEirMax.setUnits("kbps")


class _EnvelopeBwProfileCosEbs_Type(Gauge32):
    """Custom type envelopeBwProfileCosEbs based on Gauge32"""
    defaultValue = 0


_EnvelopeBwProfileCosEbs_Type.__name__ = "Gauge32"
_EnvelopeBwProfileCosEbs_Object = MibTableColumn
envelopeBwProfileCosEbs = _EnvelopeBwProfileCosEbs_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 3, 1, 8),
    _EnvelopeBwProfileCosEbs_Type()
)
envelopeBwProfileCosEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    envelopeBwProfileCosEbs.setStatus("current")
if mibBuilder.loadTexts:
    envelopeBwProfileCosEbs.setUnits("bytes")


class _EnvelopeBwProfileCoSCouplingFlag_Type(Unsigned32):
    """Custom type envelopeBwProfileCoSCouplingFlag based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_EnvelopeBwProfileCoSCouplingFlag_Type.__name__ = "Unsigned32"
_EnvelopeBwProfileCoSCouplingFlag_Object = MibTableColumn
envelopeBwProfileCoSCouplingFlag = _EnvelopeBwProfileCoSCouplingFlag_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 3, 3, 1, 9),
    _EnvelopeBwProfileCoSCouplingFlag_Type()
)
envelopeBwProfileCoSCouplingFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    envelopeBwProfileCoSCouplingFlag.setStatus("current")
_CPObjects_ObjectIdentity = ObjectIdentity
cPObjects = _CPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 4)
)
_CPProfileTable_Object = MibTable
cPProfileTable = _CPProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cPProfileTable.setStatus("current")
_CPProfileEntry_Object = MibTableRow
cPProfileEntry = _CPProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 4, 1, 1)
)
cPProfileEntry.setIndexNames(
    (0, "MEF-R-MIB", "cPProfileIndex"),
    (0, "MEF-R-MIB", "cPProfileRunningIndex"),
)
if mibBuilder.loadTexts:
    cPProfileEntry.setStatus("current")


class _CPProfileIndex_Type(Integer32):
    """Custom type cPProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CPProfileIndex_Type.__name__ = "Integer32"
_CPProfileIndex_Object = MibTableColumn
cPProfileIndex = _CPProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 4, 1, 1, 1),
    _CPProfileIndex_Type()
)
cPProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPProfileIndex.setStatus("current")


class _CPProfileRunningIndex_Type(Integer32):
    """Custom type cPProfileRunningIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CPProfileRunningIndex_Type.__name__ = "Integer32"
_CPProfileRunningIndex_Object = MibTableColumn
cPProfileRunningIndex = _CPProfileRunningIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 4, 1, 1, 2),
    _CPProfileRunningIndex_Type()
)
cPProfileRunningIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPProfileRunningIndex.setStatus("current")
_CPProfileRowStatus_Type = RowStatus
_CPProfileRowStatus_Object = MibTableColumn
cPProfileRowStatus = _CPProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 4, 1, 1, 3),
    _CPProfileRowStatus_Type()
)
cPProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPProfileRowStatus.setStatus("current")
_CPProfileMacAddress_Type = MacAddress
_CPProfileMacAddress_Object = MibTableColumn
cPProfileMacAddress = _CPProfileMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 4, 1, 1, 4),
    _CPProfileMacAddress_Type()
)
cPProfileMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPProfileMacAddress.setStatus("current")


class _CPProfileMacProcessing_Type(Integer32):
    """Custom type cPProfileMacProcessing based on Integer32"""
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
        *(("ignore", 1),
          ("discard", 2),
          ("peer", 3),
          ("tunnel", 4),
          ("macChangeTunnel", 5))
    )


_CPProfileMacProcessing_Type.__name__ = "Integer32"
_CPProfileMacProcessing_Object = MibTableColumn
cPProfileMacProcessing = _CPProfileMacProcessing_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 4, 1, 1, 5),
    _CPProfileMacProcessing_Type()
)
cPProfileMacProcessing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPProfileMacProcessing.setStatus("current")
_CPProfileName_Type = SnmpAdminString
_CPProfileName_Object = MibTableColumn
cPProfileName = _CPProfileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 4, 1, 1, 6),
    _CPProfileName_Type()
)
cPProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPProfileName.setStatus("current")


class _CPProfileProtocol_Type(Integer32):
    """Custom type cPProfileProtocol based on Integer32"""
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
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("efmOam", 2),
          ("portAuthentication", 3),
          ("lacp", 4),
          ("garp", 5),
          ("stp", 6),
          ("cdp", 7),
          ("vtp", 8),
          ("lldp", 9),
          ("pvstp", 10),
          ("pagp", 11),
          ("udld", 14),
          ("dtp", 15),
          ("loopback", 16))
    )


_CPProfileProtocol_Type.__name__ = "Integer32"
_CPProfileProtocol_Object = MibTableColumn
cPProfileProtocol = _CPProfileProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 4, 1, 1, 7),
    _CPProfileProtocol_Type()
)
cPProfileProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPProfileProtocol.setStatus("current")
_L2cpStatTable_Object = MibTable
l2cpStatTable = _L2cpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 4, 2)
)
if mibBuilder.loadTexts:
    l2cpStatTable.setStatus("current")
_L2cpStatEntry_Object = MibTableRow
l2cpStatEntry = _L2cpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 4, 2, 1)
)
l2cpStatEntry.setIndexNames(
    (0, "MEF-R-MIB", "l2cpStatPortIndex"),
    (0, "MEF-R-MIB", "l2cpStatProtocol"),
    (0, "MEF-R-MIB", "l2cpStatMacAddress"),
)
if mibBuilder.loadTexts:
    l2cpStatEntry.setStatus("current")


class _L2cpStatPortIndex_Type(Integer32):
    """Custom type l2cpStatPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_L2cpStatPortIndex_Type.__name__ = "Integer32"
_L2cpStatPortIndex_Object = MibTableColumn
l2cpStatPortIndex = _L2cpStatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 4, 2, 1, 1),
    _L2cpStatPortIndex_Type()
)
l2cpStatPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2cpStatPortIndex.setStatus("current")


class _L2cpStatProtocol_Type(Integer32):
    """Custom type l2cpStatProtocol based on Integer32"""
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
        *(("none", 1),
          ("other", 2),
          ("all", 3),
          ("efmOam", 4),
          ("portAuthentication", 5),
          ("lacp", 6),
          ("garp", 7),
          ("stp", 8),
          ("cdp", 9),
          ("vtp", 10),
          ("lldp", 11),
          ("pvstp", 12),
          ("pagp", 13),
          ("udld", 14),
          ("dtp", 15))
    )


_L2cpStatProtocol_Type.__name__ = "Integer32"
_L2cpStatProtocol_Object = MibTableColumn
l2cpStatProtocol = _L2cpStatProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 4, 2, 1, 2),
    _L2cpStatProtocol_Type()
)
l2cpStatProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2cpStatProtocol.setStatus("current")
_L2cpStatMacAddress_Type = MacAddress
_L2cpStatMacAddress_Object = MibTableColumn
l2cpStatMacAddress = _L2cpStatMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 4, 2, 1, 3),
    _L2cpStatMacAddress_Type()
)
l2cpStatMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2cpStatMacAddress.setStatus("current")
_L2cpStatEncapsulatedFrames_Type = Counter32
_L2cpStatEncapsulatedFrames_Object = MibTableColumn
l2cpStatEncapsulatedFrames = _L2cpStatEncapsulatedFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 4, 2, 1, 4),
    _L2cpStatEncapsulatedFrames_Type()
)
l2cpStatEncapsulatedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2cpStatEncapsulatedFrames.setStatus("current")
_L2cpStatDecapsulatedFrames_Type = Counter32
_L2cpStatDecapsulatedFrames_Object = MibTableColumn
l2cpStatDecapsulatedFrames = _L2cpStatDecapsulatedFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 4, 2, 1, 5),
    _L2cpStatDecapsulatedFrames_Type()
)
l2cpStatDecapsulatedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2cpStatDecapsulatedFrames.setStatus("current")
_UniObjects_ObjectIdentity = ObjectIdentity
uniObjects = _UniObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 5)
)
_UniTable_Object = MibTable
uniTable = _UniTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 5, 1)
)
if mibBuilder.loadTexts:
    uniTable.setStatus("current")
_UniEntry_Object = MibTableRow
uniEntry = _UniEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 5, 1, 1)
)
uniEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MEF-R-MIB", "uniRunningIndex"),
)
if mibBuilder.loadTexts:
    uniEntry.setStatus("current")
_UniRunningIndex_Type = Unsigned32
_UniRunningIndex_Object = MibTableColumn
uniRunningIndex = _UniRunningIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 5, 1, 1, 1),
    _UniRunningIndex_Type()
)
uniRunningIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniRunningIndex.setStatus("current")
_UniRowStatus_Type = RowStatus
_UniRowStatus_Object = MibTableColumn
uniRowStatus = _UniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 5, 1, 1, 2),
    _UniRowStatus_Type()
)
uniRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniRowStatus.setStatus("current")
_UniLayer2CPProcessingProfile_Type = Integer32
_UniLayer2CPProcessingProfile_Object = MibTableColumn
uniLayer2CPProcessingProfile = _UniLayer2CPProcessingProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 5, 1, 1, 12),
    _UniLayer2CPProcessingProfile_Type()
)
uniLayer2CPProcessingProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniLayer2CPProcessingProfile.setStatus("current")
_UniPerUniBWprofile_Type = TCVTIdV2
_UniPerUniBWprofile_Object = MibTableColumn
uniPerUniBWprofile = _UniPerUniBWprofile_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 5, 1, 1, 13),
    _UniPerUniBWprofile_Type()
)
uniPerUniBWprofile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniPerUniBWprofile.setStatus("current")
_UniSpTagProtocolIdentifier_Type = Integer32
_UniSpTagProtocolIdentifier_Object = MibTableColumn
uniSpTagProtocolIdentifier = _UniSpTagProtocolIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 5, 1, 1, 22),
    _UniSpTagProtocolIdentifier_Type()
)
uniSpTagProtocolIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniSpTagProtocolIdentifier.setStatus("current")


class _UniPacketColoring_Type(Integer32):
    """Custom type uniPacketColoring based on Integer32"""
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
          ("deiColoring", 2),
          ("priorityLsbColoring", 3))
    )


_UniPacketColoring_Type.__name__ = "Integer32"
_UniPacketColoring_Object = MibTableColumn
uniPacketColoring = _UniPacketColoring_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 5, 1, 1, 23),
    _UniPacketColoring_Type()
)
uniPacketColoring.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniPacketColoring.setStatus("current")


class _UniPerUniEgressAction_Type(Integer32):
    """Custom type uniPerUniEgressAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("addSpTag", 2))
    )


_UniPerUniEgressAction_Type.__name__ = "Integer32"
_UniPerUniEgressAction_Object = MibTableColumn
uniPerUniEgressAction = _UniPerUniEgressAction_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 5, 1, 1, 27),
    _UniPerUniEgressAction_Type()
)
uniPerUniEgressAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniPerUniEgressAction.setStatus("current")
_UniQueueGroupName_Type = SnmpAdminString
_UniQueueGroupName_Object = MibTableColumn
uniQueueGroupName = _UniQueueGroupName_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 5, 1, 1, 33),
    _UniQueueGroupName_Type()
)
uniQueueGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniQueueGroupName.setStatus("current")


class _UniClassifierKey_Type(Bits):
    """Custom type uniClassifierKey based on Bits"""
    namedValues = NamedValues(
        *(("vlan", 0),
          ("innerVlan", 1),
          ("pBit", 2),
          ("ipPrecedence", 3),
          ("ipDscp", 4),
          ("srcIpAddr", 5),
          ("destIpAddr", 6),
          ("legacy", 7),
          ("dscp", 8),
          ("macSrcAddr", 9),
          ("macDestAddr", 10),
          ("etherType", 11),
          ("myMac", 12),
          ("untagged", 13))
    )

_UniClassifierKey_Type.__name__ = "Bits"
_UniClassifierKey_Object = MibTableColumn
uniClassifierKey = _UniClassifierKey_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 5, 1, 1, 36),
    _UniClassifierKey_Type()
)
uniClassifierKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniClassifierKey.setStatus("current")
_EvcObjects_ObjectIdentity = ObjectIdentity
evcObjects = _EvcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6)
)
_FlowTable_Object = MibTable
flowTable = _FlowTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3)
)
if mibBuilder.loadTexts:
    flowTable.setStatus("current")
_FlowEntry_Object = MibTableRow
flowEntry = _FlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1)
)
flowEntry.setIndexNames(
    (0, "MEF-R-MIB", "flowIdx1"),
    (0, "MEF-R-MIB", "flowIdx2"),
)
if mibBuilder.loadTexts:
    flowEntry.setStatus("current")
_FlowIdx1_Type = Unsigned32
_FlowIdx1_Object = MibTableColumn
flowIdx1 = _FlowIdx1_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 1),
    _FlowIdx1_Type()
)
flowIdx1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowIdx1.setStatus("current")
_FlowIdx2_Type = Unsigned32
_FlowIdx2_Object = MibTableColumn
flowIdx2 = _FlowIdx2_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 2),
    _FlowIdx2_Type()
)
flowIdx2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowIdx2.setStatus("current")
_FlowName_Type = SnmpAdminString
_FlowName_Object = MibTableColumn
flowName = _FlowName_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 3),
    _FlowName_Type()
)
flowName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowName.setStatus("current")
_FlowRowStatus_Type = RowStatus
_FlowRowStatus_Object = MibTableColumn
flowRowStatus = _FlowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 4),
    _FlowRowStatus_Type()
)
flowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowRowStatus.setStatus("current")
_FlowBWprofile_Type = TCVTIdV2
_FlowBWprofile_Object = MibTableColumn
flowBWprofile = _FlowBWprofile_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 5),
    _FlowBWprofile_Type()
)
flowBWprofile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowBWprofile.setStatus("current")
_FlowFixedCos_Type = Unsigned32
_FlowFixedCos_Object = MibTableColumn
flowFixedCos = _FlowFixedCos_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 6),
    _FlowFixedCos_Type()
)
flowFixedCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowFixedCos.setStatus("current")
_FlowCOSProfile_Type = Unsigned32
_FlowCOSProfile_Object = MibTableColumn
flowCOSProfile = _FlowCOSProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 7),
    _FlowCOSProfile_Type()
)
flowCOSProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowCOSProfile.setStatus("current")
_FlowQBlock_Type = ObjectIdentifier
_FlowQBlock_Object = MibTableColumn
flowQBlock = _FlowQBlock_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 8),
    _FlowQBlock_Type()
)
flowQBlock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowQBlock.setStatus("current")
_FlowMappingProfile_Type = Unsigned32
_FlowMappingProfile_Object = MibTableColumn
flowMappingProfile = _FlowMappingProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 9),
    _FlowMappingProfile_Type()
)
flowMappingProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowMappingProfile.setStatus("current")
_FlowFixedMarking_Type = Unsigned32
_FlowFixedMarking_Object = MibTableColumn
flowFixedMarking = _FlowFixedMarking_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 10),
    _FlowFixedMarking_Type()
)
flowFixedMarking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowFixedMarking.setStatus("current")
_FlowMarkingProfile_Type = Unsigned32
_FlowMarkingProfile_Object = MibTableColumn
flowMarkingProfile = _FlowMarkingProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 11),
    _FlowMarkingProfile_Type()
)
flowMarkingProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowMarkingProfile.setStatus("current")


class _FlowOuterVlanTagging_Type(Integer32):
    """Custom type flowOuterVlanTagging based on Integer32"""
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
        *(("add", 1),
          ("overwrite", 2),
          ("preserve", 3),
          ("remove", 4))
    )


_FlowOuterVlanTagging_Type.__name__ = "Integer32"
_FlowOuterVlanTagging_Object = MibTableColumn
flowOuterVlanTagging = _FlowOuterVlanTagging_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 12),
    _FlowOuterVlanTagging_Type()
)
flowOuterVlanTagging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowOuterVlanTagging.setStatus("current")
_FlowOuterVlan_Type = Unsigned32
_FlowOuterVlan_Object = MibTableColumn
flowOuterVlan = _FlowOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 13),
    _FlowOuterVlan_Type()
)
flowOuterVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowOuterVlan.setStatus("current")


class _FlowInnerVlanTagging_Type(Integer32):
    """Custom type flowInnerVlanTagging based on Integer32"""
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
        *(("add", 1),
          ("overwrite", 2),
          ("preserve", 3),
          ("remove", 4))
    )


_FlowInnerVlanTagging_Type.__name__ = "Integer32"
_FlowInnerVlanTagging_Object = MibTableColumn
flowInnerVlanTagging = _FlowInnerVlanTagging_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 14),
    _FlowInnerVlanTagging_Type()
)
flowInnerVlanTagging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowInnerVlanTagging.setStatus("current")
_FlowInnerVlan_Type = Unsigned32
_FlowInnerVlan_Object = MibTableColumn
flowInnerVlan = _FlowInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 15),
    _FlowInnerVlan_Type()
)
flowInnerVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowInnerVlan.setStatus("current")
_FlowEgressPort_Type = Unsigned32
_FlowEgressPort_Object = MibTableColumn
flowEgressPort = _FlowEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 16),
    _FlowEgressPort_Type()
)
flowEgressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowEgressPort.setStatus("current")
_FlowIngressPort_Type = Unsigned32
_FlowIngressPort_Object = MibTableColumn
flowIngressPort = _FlowIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 17),
    _FlowIngressPort_Type()
)
flowIngressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowIngressPort.setStatus("current")
_FlowInnerFixedMarking_Type = Unsigned32
_FlowInnerFixedMarking_Object = MibTableColumn
flowInnerFixedMarking = _FlowInnerFixedMarking_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 18),
    _FlowInnerFixedMarking_Type()
)
flowInnerFixedMarking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowInnerFixedMarking.setStatus("current")
_FlowInnerMarkingProfile_Type = Unsigned32
_FlowInnerMarkingProfile_Object = MibTableColumn
flowInnerMarkingProfile = _FlowInnerMarkingProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 19),
    _FlowInnerMarkingProfile_Type()
)
flowInnerMarkingProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowInnerMarkingProfile.setStatus("current")


class _FlowDropAction_Type(Integer32):
    """Custom type flowDropAction based on Integer32"""
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
          ("disable", 2),
          ("enable", 3))
    )


_FlowDropAction_Type.__name__ = "Integer32"
_FlowDropAction_Object = MibTableColumn
flowDropAction = _FlowDropAction_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 20),
    _FlowDropAction_Type()
)
flowDropAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowDropAction.setStatus("current")
_FlowPriority_Type = Unsigned32
_FlowPriority_Object = MibTableColumn
flowPriority = _FlowPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 21),
    _FlowPriority_Type()
)
flowPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowPriority.setStatus("current")
_FlowMarkOuterFixedMarking_Type = Unsigned32
_FlowMarkOuterFixedMarking_Object = MibTableColumn
flowMarkOuterFixedMarking = _FlowMarkOuterFixedMarking_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 22),
    _FlowMarkOuterFixedMarking_Type()
)
flowMarkOuterFixedMarking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowMarkOuterFixedMarking.setStatus("current")
_FlowMarkOuterMarkingProfile_Type = Unsigned32
_FlowMarkOuterMarkingProfile_Object = MibTableColumn
flowMarkOuterMarkingProfile = _FlowMarkOuterMarkingProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 23),
    _FlowMarkOuterMarkingProfile_Type()
)
flowMarkOuterMarkingProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowMarkOuterMarkingProfile.setStatus("current")
_FlowMarkInnerFixedMarking_Type = Unsigned32
_FlowMarkInnerFixedMarking_Object = MibTableColumn
flowMarkInnerFixedMarking = _FlowMarkInnerFixedMarking_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 24),
    _FlowMarkInnerFixedMarking_Type()
)
flowMarkInnerFixedMarking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowMarkInnerFixedMarking.setStatus("current")
_FlowMarkInnerMarkingProfile_Type = Unsigned32
_FlowMarkInnerMarkingProfile_Object = MibTableColumn
flowMarkInnerMarkingProfile = _FlowMarkInnerMarkingProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 25),
    _FlowMarkInnerMarkingProfile_Type()
)
flowMarkInnerMarkingProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowMarkInnerMarkingProfile.setStatus("current")


class _FlowMarkOuterVlanTagging_Type(Bits):
    """Custom type flowMarkOuterVlanTagging based on Bits"""
    namedValues = NamedValues(
        *(("overwritePbit", 0),
          ("overwriteVlan", 1),
          ("overwriteEtherType", 2))
    )

_FlowMarkOuterVlanTagging_Type.__name__ = "Bits"
_FlowMarkOuterVlanTagging_Object = MibTableColumn
flowMarkOuterVlanTagging = _FlowMarkOuterVlanTagging_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 26),
    _FlowMarkOuterVlanTagging_Type()
)
flowMarkOuterVlanTagging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowMarkOuterVlanTagging.setStatus("current")
_FlowMarkOuterVlan_Type = Unsigned32
_FlowMarkOuterVlan_Object = MibTableColumn
flowMarkOuterVlan = _FlowMarkOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 27),
    _FlowMarkOuterVlan_Type()
)
flowMarkOuterVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowMarkOuterVlan.setStatus("current")


class _FlowMarkInnerVlanTagging_Type(Bits):
    """Custom type flowMarkInnerVlanTagging based on Bits"""
    namedValues = NamedValues(
        *(("overwritePbit", 0),
          ("overwriteVlan", 1),
          ("overwriteEtherType", 2))
    )

_FlowMarkInnerVlanTagging_Type.__name__ = "Bits"
_FlowMarkInnerVlanTagging_Object = MibTableColumn
flowMarkInnerVlanTagging = _FlowMarkInnerVlanTagging_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 28),
    _FlowMarkInnerVlanTagging_Type()
)
flowMarkInnerVlanTagging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowMarkInnerVlanTagging.setStatus("current")
_FlowMarkInnerVlan_Type = Unsigned32
_FlowMarkInnerVlan_Object = MibTableColumn
flowMarkInnerVlan = _FlowMarkInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 29),
    _FlowMarkInnerVlan_Type()
)
flowMarkInnerVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowMarkInnerVlan.setStatus("current")
_FlowPolicerAggregate_Type = Unsigned32
_FlowPolicerAggregate_Object = MibTableColumn
flowPolicerAggregate = _FlowPolicerAggregate_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 30),
    _FlowPolicerAggregate_Type()
)
flowPolicerAggregate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowPolicerAggregate.setStatus("current")


class _FlowMarkMacTagging_Type(Bits):
    """Custom type flowMarkMacTagging based on Bits"""
    namedValues = NamedValues(
        *(("swapMacSrcAndDst", 0),
          ("overwriteSrcMac", 1),
          ("overwriteDstMac", 2))
    )

_FlowMarkMacTagging_Type.__name__ = "Bits"
_FlowMarkMacTagging_Object = MibTableColumn
flowMarkMacTagging = _FlowMarkMacTagging_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 32),
    _FlowMarkMacTagging_Type()
)
flowMarkMacTagging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowMarkMacTagging.setStatus("current")


class _FlowMarkIpTagging_Type(Bits):
    """Custom type flowMarkIpTagging based on Bits"""
    namedValues = NamedValues(
        *(("swapIpSrcAndDst", 0),
          ("overwriteSrcIp", 1),
          ("overwriteDstIp", 2))
    )

_FlowMarkIpTagging_Type.__name__ = "Bits"
_FlowMarkIpTagging_Object = MibTableColumn
flowMarkIpTagging = _FlowMarkIpTagging_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 33),
    _FlowMarkIpTagging_Type()
)
flowMarkIpTagging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowMarkIpTagging.setStatus("current")
_FlowLayer2CPProcessingProfile_Type = Unsigned32
_FlowLayer2CPProcessingProfile_Object = MibTableColumn
flowLayer2CPProcessingProfile = _FlowLayer2CPProcessingProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 38),
    _FlowLayer2CPProcessingProfile_Type()
)
flowLayer2CPProcessingProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowLayer2CPProcessingProfile.setStatus("current")


class _FlowIngressColorMapping_Type(Integer32):
    """Custom type flowIngressColorMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2),
          ("colorProfile", 255))
    )


_FlowIngressColorMapping_Type.__name__ = "Integer32"
_FlowIngressColorMapping_Object = MibTableColumn
flowIngressColorMapping = _FlowIngressColorMapping_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 39),
    _FlowIngressColorMapping_Type()
)
flowIngressColorMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowIngressColorMapping.setStatus("current")
_FlowIngressColorProfile_Type = Unsigned32
_FlowIngressColorProfile_Object = MibTableColumn
flowIngressColorProfile = _FlowIngressColorProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 40),
    _FlowIngressColorProfile_Type()
)
flowIngressColorProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowIngressColorProfile.setStatus("current")
_FlowCosMapping_Type = Unsigned32
_FlowCosMapping_Object = MibTableColumn
flowCosMapping = _FlowCosMapping_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 41),
    _FlowCosMapping_Type()
)
flowCosMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowCosMapping.setStatus("current")
_FlowCosMappingProfile_Type = Unsigned32
_FlowCosMappingProfile_Object = MibTableColumn
flowCosMappingProfile = _FlowCosMappingProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 42),
    _FlowCosMappingProfile_Type()
)
flowCosMappingProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowCosMappingProfile.setStatus("current")


class _FlowStatus_Type(Bits):
    """Custom type flowStatus based on Bits"""
    namedValues = NamedValues(
        *(("operStat", 0),
          ("adminStatDown", 1),
          ("ingressOperStatNotUp", 2),
          ("egressOperStatNotUp", 3),
          ("test", 4),
          ("lackOfResources", 5),
          ("cfmOamFailure", 6),
          ("y1564Test", 7),
          ("rfc2544Test", 8),
          ("mef46Loop", 9))
    )

_FlowStatus_Type.__name__ = "Bits"
_FlowStatus_Object = MibTableColumn
flowStatus = _FlowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 47),
    _FlowStatus_Type()
)
flowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowStatus.setStatus("current")


class _FlowServiceIdName_Type(SnmpAdminString):
    """Custom type flowServiceIdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FlowServiceIdName_Type.__name__ = "SnmpAdminString"
_FlowServiceIdName_Object = MibTableColumn
flowServiceIdName = _FlowServiceIdName_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 49),
    _FlowServiceIdName_Type()
)
flowServiceIdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowServiceIdName.setStatus("current")


class _FlowPolicerType_Type(Integer32):
    """Custom type flowPolicerType based on Integer32"""
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
        *(("none", 1),
          ("regular", 2),
          ("aggregate", 3),
          ("envelope", 4),
          ("regularAccountingOnly", 5))
    )


_FlowPolicerType_Type.__name__ = "Integer32"
_FlowPolicerType_Object = MibTableColumn
flowPolicerType = _FlowPolicerType_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 51),
    _FlowPolicerType_Type()
)
flowPolicerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowPolicerType.setStatus("current")


class _FlowMultiCosCounters_Type(Bits):
    """Custom type flowMultiCosCounters based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("cos0", 0),
          ("cos1", 1),
          ("cos2", 2),
          ("cos3", 3),
          ("cos4", 4),
          ("cos5", 5),
          ("cos6", 6),
          ("cos7", 7))
    )

_FlowMultiCosCounters_Type.__name__ = "Bits"
_FlowMultiCosCounters_Object = MibTableColumn
flowMultiCosCounters = _FlowMultiCosCounters_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 52),
    _FlowMultiCosCounters_Type()
)
flowMultiCosCounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowMultiCosCounters.setStatus("current")


class _FlowClassifierType_Type(Integer32):
    """Custom type flowClassifierType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flowClassifier", 1),
          ("portClassifier", 2))
    )


_FlowClassifierType_Type.__name__ = "Integer32"
_FlowClassifierType_Object = MibTableColumn
flowClassifierType = _FlowClassifierType_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 53),
    _FlowClassifierType_Type()
)
flowClassifierType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowClassifierType.setStatus("current")
_FlowIngressPortClassifier_Type = InterfaceIndexOrZero
_FlowIngressPortClassifier_Object = MibTableColumn
flowIngressPortClassifier = _FlowIngressPortClassifier_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 54),
    _FlowIngressPortClassifier_Type()
)
flowIngressPortClassifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowIngressPortClassifier.setStatus("current")


class _FlowDscpMarkingProfile_Type(Unsigned32):
    """Custom type flowDscpMarkingProfile based on Unsigned32"""
    defaultValue = 0


_FlowDscpMarkingProfile_Type.__name__ = "Unsigned32"
_FlowDscpMarkingProfile_Object = MibTableColumn
flowDscpMarkingProfile = _FlowDscpMarkingProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 3, 1, 55),
    _FlowDscpMarkingProfile_Type()
)
flowDscpMarkingProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowDscpMarkingProfile.setStatus("current")
_FlowMapping_ObjectIdentity = ObjectIdentity
flowMapping = _FlowMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 4)
)
_ServiceIdTable_Object = MibTable
serviceIdTable = _ServiceIdTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 4, 2)
)
if mibBuilder.loadTexts:
    serviceIdTable.setStatus("current")
_ServiceIdEntry_Object = MibTableRow
serviceIdEntry = _ServiceIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 4, 2, 1)
)
serviceIdEntry.setIndexNames(
    (0, "MEF-R-MIB", "serviceIdName"),
    (1, "MEF-R-MIB", "serviceIdRowPointer"),
)
if mibBuilder.loadTexts:
    serviceIdEntry.setStatus("current")


class _ServiceIdName_Type(SnmpAdminString):
    """Custom type serviceIdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ServiceIdName_Type.__name__ = "SnmpAdminString"
_ServiceIdName_Object = MibTableColumn
serviceIdName = _ServiceIdName_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 4, 2, 1, 1),
    _ServiceIdName_Type()
)
serviceIdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serviceIdName.setStatus("current")
_ServiceIdRowPointer_Type = RowPointer
_ServiceIdRowPointer_Object = MibTableColumn
serviceIdRowPointer = _ServiceIdRowPointer_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 4, 2, 1, 2),
    _ServiceIdRowPointer_Type()
)
serviceIdRowPointer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serviceIdRowPointer.setStatus("current")


class _ServiceIdEntityType_Type(Integer32):
    """Custom type serviceIdEntityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flow", 1),
          ("erpVlan", 2),
          ("ma", 3))
    )


_ServiceIdEntityType_Type.__name__ = "Integer32"
_ServiceIdEntityType_Object = MibTableColumn
serviceIdEntityType = _ServiceIdEntityType_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 4, 2, 1, 3),
    _ServiceIdEntityType_Type()
)
serviceIdEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceIdEntityType.setStatus("current")
_ServiceIdRowStatus_Type = RowStatus
_ServiceIdRowStatus_Object = MibTableColumn
serviceIdRowStatus = _ServiceIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 4, 2, 1, 5),
    _ServiceIdRowStatus_Type()
)
serviceIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceIdRowStatus.setStatus("current")
_ServiceIdCmdTable_Object = MibTable
serviceIdCmdTable = _ServiceIdCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 4, 3)
)
if mibBuilder.loadTexts:
    serviceIdCmdTable.setStatus("current")
_ServiceIdCmdEntry_Object = MibTableRow
serviceIdCmdEntry = _ServiceIdCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 4, 3, 1)
)
serviceIdCmdEntry.setIndexNames(
    (0, "MEF-R-MIB", "serviceIdName"),
)
if mibBuilder.loadTexts:
    serviceIdCmdEntry.setStatus("current")
_ServiceIdCmdRowStatus_Type = RowStatus
_ServiceIdCmdRowStatus_Object = MibTableColumn
serviceIdCmdRowStatus = _ServiceIdCmdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 4, 3, 1, 1),
    _ServiceIdCmdRowStatus_Type()
)
serviceIdCmdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceIdCmdRowStatus.setStatus("current")
_ServiceIdCmdVlan_Type = Unsigned32
_ServiceIdCmdVlan_Object = MibTableColumn
serviceIdCmdVlan = _ServiceIdCmdVlan_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 4, 3, 1, 2),
    _ServiceIdCmdVlan_Type()
)
serviceIdCmdVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceIdCmdVlan.setStatus("current")
_ServiceIdCmdInnerVlan_Type = Unsigned32
_ServiceIdCmdInnerVlan_Object = MibTableColumn
serviceIdCmdInnerVlan = _ServiceIdCmdInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 4, 3, 1, 3),
    _ServiceIdCmdInnerVlan_Type()
)
serviceIdCmdInnerVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceIdCmdInnerVlan.setStatus("current")
_ServiceIdCmdPortIdx_Type = Unsigned32
_ServiceIdCmdPortIdx_Object = MibTableColumn
serviceIdCmdPortIdx = _ServiceIdCmdPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 4, 3, 1, 4),
    _ServiceIdCmdPortIdx_Type()
)
serviceIdCmdPortIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceIdCmdPortIdx.setStatus("current")
_PmFlowCmdTable_Object = MibTable
pmFlowCmdTable = _PmFlowCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 6)
)
if mibBuilder.loadTexts:
    pmFlowCmdTable.setStatus("current")
_PmFlowCmdEntry_Object = MibTableRow
pmFlowCmdEntry = _PmFlowCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 6, 1)
)
pmFlowCmdEntry.setIndexNames(
    (0, "MEF-R-MIB", "pmFlowCmdIndex"),
)
if mibBuilder.loadTexts:
    pmFlowCmdEntry.setStatus("current")
_PmFlowCmdIndex_Type = Unsigned32
_PmFlowCmdIndex_Object = MibTableColumn
pmFlowCmdIndex = _PmFlowCmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 6, 1, 1),
    _PmFlowCmdIndex_Type()
)
pmFlowCmdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmFlowCmdIndex.setStatus("current")


class _PmFlowCmdWithOAMTraffic_Type(Integer32):
    """Custom type pmFlowCmdWithOAMTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("yes", 2),
          ("no", 3))
    )


_PmFlowCmdWithOAMTraffic_Type.__name__ = "Integer32"
_PmFlowCmdWithOAMTraffic_Object = MibTableColumn
pmFlowCmdWithOAMTraffic = _PmFlowCmdWithOAMTraffic_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 8, 1, 6, 6, 1, 2),
    _PmFlowCmdWithOAMTraffic_Type()
)
pmFlowCmdWithOAMTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmFlowCmdWithOAMTraffic.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MEF-R-MIB",
    **{"TCVlanId": TCVlanId,
       "TCBurstSizeV2": TCBurstSizeV2,
       "TCV2DefaultUserPriority": TCV2DefaultUserPriority,
       "TCEthFrameHandling": TCEthFrameHandling,
       "TCSLAPrioritySource": TCSLAPrioritySource,
       "TCEvcId": TCEvcId,
       "TCVTIdV2": TCVTIdV2,
       "mefMIBR": mefMIBR,
       "mefObjects": mefObjects,
       "mefrScalarObjects": mefrScalarObjects,
       "mefrBwRoundUp": mefrBwRoundUp,
       "mefrEnvelopeRanks": mefrEnvelopeRanks,
       "hsQBlockMapping": hsQBlockMapping,
       "bwProfileObjects": bwProfileObjects,
       "bwProfileTable": bwProfileTable,
       "bwProfileEntry": bwProfileEntry,
       "bwProfileID": bwProfileID,
       "bwProfileIndex": bwProfileIndex,
       "bwProfileRowStatus": bwProfileRowStatus,
       "bwProfileCIR": bwProfileCIR,
       "bwProfileCBS": bwProfileCBS,
       "bwProfileEIR": bwProfileEIR,
       "bwProfileEBS": bwProfileEBS,
       "bwProfileColorAware": bwProfileColorAware,
       "bwProfileColorAwareAdmissionOption": bwProfileColorAwareAdmissionOption,
       "bwProfileName": bwProfileName,
       "bwProfileGranularity": bwProfileGranularity,
       "bwProfilePolicedTraffic": bwProfilePolicedTraffic,
       "bwProfileCompensation": bwProfileCompensation,
       "envelopeBwProfileTable": envelopeBwProfileTable,
       "envelopeBwProfileEntry": envelopeBwProfileEntry,
       "envelopeBwProfileIndex": envelopeBwProfileIndex,
       "envelopeBwProfileName": envelopeBwProfileName,
       "envelopeBwProfileRowStatus": envelopeBwProfileRowStatus,
       "envelopeBwProfileCouplingFlagPolicy": envelopeBwProfileCouplingFlagPolicy,
       "envelopeBwProfileCouplingFlag0": envelopeBwProfileCouplingFlag0,
       "envelopeBwProfileColorMode": envelopeBwProfileColorMode,
       "envelopeBwProfileCompensation": envelopeBwProfileCompensation,
       "envelopeBwProfileCosTable": envelopeBwProfileCosTable,
       "envelopeBwProfileCosEntry": envelopeBwProfileCosEntry,
       "envelopeBwProfileCosIndex": envelopeBwProfileCosIndex,
       "envelopeBwProfileCosRowStatus": envelopeBwProfileCosRowStatus,
       "envelopeBwProfileCosCir": envelopeBwProfileCosCir,
       "envelopeBwProfileCosCirMax": envelopeBwProfileCosCirMax,
       "envelopeBwProfileCosCbs": envelopeBwProfileCosCbs,
       "envelopeBwProfileCosEir": envelopeBwProfileCosEir,
       "envelopeBwProfileCosEirMax": envelopeBwProfileCosEirMax,
       "envelopeBwProfileCosEbs": envelopeBwProfileCosEbs,
       "envelopeBwProfileCoSCouplingFlag": envelopeBwProfileCoSCouplingFlag,
       "cPObjects": cPObjects,
       "cPProfileTable": cPProfileTable,
       "cPProfileEntry": cPProfileEntry,
       "cPProfileIndex": cPProfileIndex,
       "cPProfileRunningIndex": cPProfileRunningIndex,
       "cPProfileRowStatus": cPProfileRowStatus,
       "cPProfileMacAddress": cPProfileMacAddress,
       "cPProfileMacProcessing": cPProfileMacProcessing,
       "cPProfileName": cPProfileName,
       "cPProfileProtocol": cPProfileProtocol,
       "l2cpStatTable": l2cpStatTable,
       "l2cpStatEntry": l2cpStatEntry,
       "l2cpStatPortIndex": l2cpStatPortIndex,
       "l2cpStatProtocol": l2cpStatProtocol,
       "l2cpStatMacAddress": l2cpStatMacAddress,
       "l2cpStatEncapsulatedFrames": l2cpStatEncapsulatedFrames,
       "l2cpStatDecapsulatedFrames": l2cpStatDecapsulatedFrames,
       "uniObjects": uniObjects,
       "uniTable": uniTable,
       "uniEntry": uniEntry,
       "uniRunningIndex": uniRunningIndex,
       "uniRowStatus": uniRowStatus,
       "uniLayer2CPProcessingProfile": uniLayer2CPProcessingProfile,
       "uniPerUniBWprofile": uniPerUniBWprofile,
       "uniSpTagProtocolIdentifier": uniSpTagProtocolIdentifier,
       "uniPacketColoring": uniPacketColoring,
       "uniPerUniEgressAction": uniPerUniEgressAction,
       "uniQueueGroupName": uniQueueGroupName,
       "uniClassifierKey": uniClassifierKey,
       "evcObjects": evcObjects,
       "flowTable": flowTable,
       "flowEntry": flowEntry,
       "flowIdx1": flowIdx1,
       "flowIdx2": flowIdx2,
       "flowName": flowName,
       "flowRowStatus": flowRowStatus,
       "flowBWprofile": flowBWprofile,
       "flowFixedCos": flowFixedCos,
       "flowCOSProfile": flowCOSProfile,
       "flowQBlock": flowQBlock,
       "flowMappingProfile": flowMappingProfile,
       "flowFixedMarking": flowFixedMarking,
       "flowMarkingProfile": flowMarkingProfile,
       "flowOuterVlanTagging": flowOuterVlanTagging,
       "flowOuterVlan": flowOuterVlan,
       "flowInnerVlanTagging": flowInnerVlanTagging,
       "flowInnerVlan": flowInnerVlan,
       "flowEgressPort": flowEgressPort,
       "flowIngressPort": flowIngressPort,
       "flowInnerFixedMarking": flowInnerFixedMarking,
       "flowInnerMarkingProfile": flowInnerMarkingProfile,
       "flowDropAction": flowDropAction,
       "flowPriority": flowPriority,
       "flowMarkOuterFixedMarking": flowMarkOuterFixedMarking,
       "flowMarkOuterMarkingProfile": flowMarkOuterMarkingProfile,
       "flowMarkInnerFixedMarking": flowMarkInnerFixedMarking,
       "flowMarkInnerMarkingProfile": flowMarkInnerMarkingProfile,
       "flowMarkOuterVlanTagging": flowMarkOuterVlanTagging,
       "flowMarkOuterVlan": flowMarkOuterVlan,
       "flowMarkInnerVlanTagging": flowMarkInnerVlanTagging,
       "flowMarkInnerVlan": flowMarkInnerVlan,
       "flowPolicerAggregate": flowPolicerAggregate,
       "flowMarkMacTagging": flowMarkMacTagging,
       "flowMarkIpTagging": flowMarkIpTagging,
       "flowLayer2CPProcessingProfile": flowLayer2CPProcessingProfile,
       "flowIngressColorMapping": flowIngressColorMapping,
       "flowIngressColorProfile": flowIngressColorProfile,
       "flowCosMapping": flowCosMapping,
       "flowCosMappingProfile": flowCosMappingProfile,
       "flowStatus": flowStatus,
       "flowServiceIdName": flowServiceIdName,
       "flowPolicerType": flowPolicerType,
       "flowMultiCosCounters": flowMultiCosCounters,
       "flowClassifierType": flowClassifierType,
       "flowIngressPortClassifier": flowIngressPortClassifier,
       "flowDscpMarkingProfile": flowDscpMarkingProfile,
       "flowMapping": flowMapping,
       "serviceIdTable": serviceIdTable,
       "serviceIdEntry": serviceIdEntry,
       "serviceIdName": serviceIdName,
       "serviceIdRowPointer": serviceIdRowPointer,
       "serviceIdEntityType": serviceIdEntityType,
       "serviceIdRowStatus": serviceIdRowStatus,
       "serviceIdCmdTable": serviceIdCmdTable,
       "serviceIdCmdEntry": serviceIdCmdEntry,
       "serviceIdCmdRowStatus": serviceIdCmdRowStatus,
       "serviceIdCmdVlan": serviceIdCmdVlan,
       "serviceIdCmdInnerVlan": serviceIdCmdInnerVlan,
       "serviceIdCmdPortIdx": serviceIdCmdPortIdx,
       "pmFlowCmdTable": pmFlowCmdTable,
       "pmFlowCmdEntry": pmFlowCmdEntry,
       "pmFlowCmdIndex": pmFlowCmdIndex,
       "pmFlowCmdWithOAMTraffic": pmFlowCmdWithOAMTraffic}
)
