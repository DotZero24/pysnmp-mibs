# SNMP MIB module (SWTICH-SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWTICH-SERVICE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:31 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

rcService = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcServiceScalar_ObjectIdentity = ObjectIdentity
rcServiceScalar = _RcServiceScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 1)
)


class _RcServiceDefaultSdp1PortIndex_Type(Integer32):
    """Custom type rcServiceDefaultSdp1PortIndex based on Integer32"""
    defaultValue = 0


_RcServiceDefaultSdp1PortIndex_Type.__name__ = "Integer32"
_RcServiceDefaultSdp1PortIndex_Object = MibScalar
rcServiceDefaultSdp1PortIndex = _RcServiceDefaultSdp1PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 1, 1),
    _RcServiceDefaultSdp1PortIndex_Type()
)
rcServiceDefaultSdp1PortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcServiceDefaultSdp1PortIndex.setStatus("current")


class _RcServiceDefaultSdp2PortIndex_Type(Integer32):
    """Custom type rcServiceDefaultSdp2PortIndex based on Integer32"""
    defaultValue = 0


_RcServiceDefaultSdp2PortIndex_Type.__name__ = "Integer32"
_RcServiceDefaultSdp2PortIndex_Object = MibScalar
rcServiceDefaultSdp2PortIndex = _RcServiceDefaultSdp2PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 1, 2),
    _RcServiceDefaultSdp2PortIndex_Type()
)
rcServiceDefaultSdp2PortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcServiceDefaultSdp2PortIndex.setStatus("current")
_RcServiceEtherSamTrapEnable_Type = TruthValue
_RcServiceEtherSamTrapEnable_Object = MibScalar
rcServiceEtherSamTrapEnable = _RcServiceEtherSamTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 1, 3),
    _RcServiceEtherSamTrapEnable_Type()
)
rcServiceEtherSamTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcServiceEtherSamTrapEnable.setStatus("current")
_RcServiceCosLabelNameTable_Object = MibTable
rcServiceCosLabelNameTable = _RcServiceCosLabelNameTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 2)
)
if mibBuilder.loadTexts:
    rcServiceCosLabelNameTable.setStatus("current")
_RcServiceCosLabelNameEntry_Object = MibTableRow
rcServiceCosLabelNameEntry = _RcServiceCosLabelNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 2, 1)
)
rcServiceCosLabelNameEntry.setIndexNames(
    (0, "SWTICH-SERVICE-MIB", "rcServiceCosLabel"),
)
if mibBuilder.loadTexts:
    rcServiceCosLabelNameEntry.setStatus("current")


class _RcServiceCosLabel_Type(Integer32):
    """Custom type rcServiceCosLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcServiceCosLabel_Type.__name__ = "Integer32"
_RcServiceCosLabel_Object = MibTableColumn
rcServiceCosLabel = _RcServiceCosLabel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 2, 1, 1),
    _RcServiceCosLabel_Type()
)
rcServiceCosLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcServiceCosLabel.setStatus("current")


class _RcServiceCosLabelName_Type(OctetString):
    """Custom type rcServiceCosLabelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RcServiceCosLabelName_Type.__name__ = "OctetString"
_RcServiceCosLabelName_Object = MibTableColumn
rcServiceCosLabelName = _RcServiceCosLabelName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 2, 1, 2),
    _RcServiceCosLabelName_Type()
)
rcServiceCosLabelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcServiceCosLabelName.setStatus("current")
_RcServiceNetworkInterfaceTable_Object = MibTable
rcServiceNetworkInterfaceTable = _RcServiceNetworkInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3)
)
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceTable.setStatus("current")
_RcServiceNetworkInterfaceEntry_Object = MibTableRow
rcServiceNetworkInterfaceEntry = _RcServiceNetworkInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1)
)
rcServiceNetworkInterfaceEntry.setIndexNames(
    (0, "SWTICH-SERVICE-MIB", "rcServiceNetworkInterfacePortIndex"),
)
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceEntry.setStatus("current")
_RcServiceNetworkInterfacePortIndex_Type = Integer32
_RcServiceNetworkInterfacePortIndex_Object = MibTableColumn
rcServiceNetworkInterfacePortIndex = _RcServiceNetworkInterfacePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 1),
    _RcServiceNetworkInterfacePortIndex_Type()
)
rcServiceNetworkInterfacePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfacePortIndex.setStatus("current")


class _RcServiceNetworkInterfaceType_Type(Integer32):
    """Custom type rcServiceNetworkInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inni", 0),
          ("enni", 1),
          ("uni", 2),
          ("channel", 3))
    )


_RcServiceNetworkInterfaceType_Type.__name__ = "Integer32"
_RcServiceNetworkInterfaceType_Object = MibTableColumn
rcServiceNetworkInterfaceType = _RcServiceNetworkInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 2),
    _RcServiceNetworkInterfaceType_Type()
)
rcServiceNetworkInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceType.setStatus("current")


class _RcServiceNetworkInterfaceID_Type(OctetString):
    """Custom type rcServiceNetworkInterfaceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_RcServiceNetworkInterfaceID_Type.__name__ = "OctetString"
_RcServiceNetworkInterfaceID_Object = MibTableColumn
rcServiceNetworkInterfaceID = _RcServiceNetworkInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 3),
    _RcServiceNetworkInterfaceID_Type()
)
rcServiceNetworkInterfaceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceID.setStatus("current")


class _RcServiceNetworkInterfacePhysicalMedium_Type(Integer32):
    """Custom type rcServiceNetworkInterfacePhysicalMedium based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              16,
              18,
              22,
              30,
              31,
              33,
              37)
        )
    )
    namedValues = NamedValues(
        *(("dot3-unknownPhy", 0),
          ("dot3-10BASE-T", 5),
          ("dot3-100BASE-TX", 16),
          ("dot3-100BASE-FX", 18),
          ("dot3-1000BASE-X", 22),
          ("dot3-1000BASE-T", 30),
          ("dot3-10GBASE-X", 31),
          ("dot3-10GBASE-R", 33),
          ("dot3-10GBASE-W", 37))
    )


_RcServiceNetworkInterfacePhysicalMedium_Type.__name__ = "Integer32"
_RcServiceNetworkInterfacePhysicalMedium_Object = MibTableColumn
rcServiceNetworkInterfacePhysicalMedium = _RcServiceNetworkInterfacePhysicalMedium_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 4),
    _RcServiceNetworkInterfacePhysicalMedium_Type()
)
rcServiceNetworkInterfacePhysicalMedium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfacePhysicalMedium.setStatus("current")


class _RcServiceNetworkInterfaceSpeed_Type(Integer32):
    """Custom type rcServiceNetworkInterfaceSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("speedUnknown", 0),
          ("m10", 1),
          ("m100", 2),
          ("autonegom10-100", 3),
          ("autonegom10-100-1000", 4),
          ("g1", 5),
          ("g10", 6),
          ("autonegofiber1000", 7))
    )


_RcServiceNetworkInterfaceSpeed_Type.__name__ = "Integer32"
_RcServiceNetworkInterfaceSpeed_Object = MibTableColumn
rcServiceNetworkInterfaceSpeed = _RcServiceNetworkInterfaceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 5),
    _RcServiceNetworkInterfaceSpeed_Type()
)
rcServiceNetworkInterfaceSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceSpeed.setStatus("current")


class _RcServiceNetworkInterfaceDuplexMode_Type(Integer32):
    """Custom type rcServiceNetworkInterfaceDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("duplexUnknown", 0),
          ("duplexAutoNego", 1),
          ("duplexFull", 2),
          ("duplexHalf", 3))
    )


_RcServiceNetworkInterfaceDuplexMode_Type.__name__ = "Integer32"
_RcServiceNetworkInterfaceDuplexMode_Object = MibTableColumn
rcServiceNetworkInterfaceDuplexMode = _RcServiceNetworkInterfaceDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 6),
    _RcServiceNetworkInterfaceDuplexMode_Type()
)
rcServiceNetworkInterfaceDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceDuplexMode.setStatus("current")


class _RcServiceNetworkInterfaceMacLayer_Type(Integer32):
    """Custom type rcServiceNetworkInterfaceMacLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("ieee802dot3-2005", 0)
    )


_RcServiceNetworkInterfaceMacLayer_Type.__name__ = "Integer32"
_RcServiceNetworkInterfaceMacLayer_Object = MibTableColumn
rcServiceNetworkInterfaceMacLayer = _RcServiceNetworkInterfaceMacLayer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 7),
    _RcServiceNetworkInterfaceMacLayer_Type()
)
rcServiceNetworkInterfaceMacLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceMacLayer.setStatus("current")
_RcServiceNetworkInterfaceMtu_Type = Integer32
_RcServiceNetworkInterfaceMtu_Object = MibTableColumn
rcServiceNetworkInterfaceMtu = _RcServiceNetworkInterfaceMtu_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 8),
    _RcServiceNetworkInterfaceMtu_Type()
)
rcServiceNetworkInterfaceMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceMtu.setStatus("current")
_RcServiceNetworkInterfaceServiceMultiplexing_Type = TruthValue
_RcServiceNetworkInterfaceServiceMultiplexing_Object = MibTableColumn
rcServiceNetworkInterfaceServiceMultiplexing = _RcServiceNetworkInterfaceServiceMultiplexing_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 9),
    _RcServiceNetworkInterfaceServiceMultiplexing_Type()
)
rcServiceNetworkInterfaceServiceMultiplexing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceServiceMultiplexing.setStatus("current")
_RcServiceNetworkInterfaceBundling_Type = TruthValue
_RcServiceNetworkInterfaceBundling_Object = MibTableColumn
rcServiceNetworkInterfaceBundling = _RcServiceNetworkInterfaceBundling_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 10),
    _RcServiceNetworkInterfaceBundling_Type()
)
rcServiceNetworkInterfaceBundling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceBundling.setStatus("current")
_RcServiceNetworkInterfaceAllToOneBundling_Type = TruthValue
_RcServiceNetworkInterfaceAllToOneBundling_Object = MibTableColumn
rcServiceNetworkInterfaceAllToOneBundling = _RcServiceNetworkInterfaceAllToOneBundling_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 11),
    _RcServiceNetworkInterfaceAllToOneBundling_Type()
)
rcServiceNetworkInterfaceAllToOneBundling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceAllToOneBundling.setStatus("current")


class _RcServiceNetworkInterfaceDefaultCVlan_Type(Integer32):
    """Custom type rcServiceNetworkInterfaceDefaultCVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcServiceNetworkInterfaceDefaultCVlan_Type.__name__ = "Integer32"
_RcServiceNetworkInterfaceDefaultCVlan_Object = MibTableColumn
rcServiceNetworkInterfaceDefaultCVlan = _RcServiceNetworkInterfaceDefaultCVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 12),
    _RcServiceNetworkInterfaceDefaultCVlan_Type()
)
rcServiceNetworkInterfaceDefaultCVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceDefaultCVlan.setStatus("current")
_RcServiceNetworkInterfacMaxEvcs_Type = Integer32
_RcServiceNetworkInterfacMaxEvcs_Object = MibTableColumn
rcServiceNetworkInterfacMaxEvcs = _RcServiceNetworkInterfacMaxEvcs_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 13),
    _RcServiceNetworkInterfacMaxEvcs_Type()
)
rcServiceNetworkInterfacMaxEvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfacMaxEvcs.setStatus("current")
_RcServiceNetworkInterfaceMaxOvcs_Type = Integer32
_RcServiceNetworkInterfaceMaxOvcs_Object = MibTableColumn
rcServiceNetworkInterfaceMaxOvcs = _RcServiceNetworkInterfaceMaxOvcs_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 14),
    _RcServiceNetworkInterfaceMaxOvcs_Type()
)
rcServiceNetworkInterfaceMaxOvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceMaxOvcs.setStatus("current")
_RcServiceNetworkInterfaceInBwProfileIndex_Type = Integer32
_RcServiceNetworkInterfaceInBwProfileIndex_Object = MibTableColumn
rcServiceNetworkInterfaceInBwProfileIndex = _RcServiceNetworkInterfaceInBwProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 15),
    _RcServiceNetworkInterfaceInBwProfileIndex_Type()
)
rcServiceNetworkInterfaceInBwProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceInBwProfileIndex.setStatus("current")
_RcServiceNetworkInterfaceOutBwProfileIndex_Type = Integer32
_RcServiceNetworkInterfaceOutBwProfileIndex_Object = MibTableColumn
rcServiceNetworkInterfaceOutBwProfileIndex = _RcServiceNetworkInterfaceOutBwProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 16),
    _RcServiceNetworkInterfaceOutBwProfileIndex_Type()
)
rcServiceNetworkInterfaceOutBwProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceOutBwProfileIndex.setStatus("current")
_RcServiceNetworkInterfaceL2cpProfileIndex_Type = Integer32
_RcServiceNetworkInterfaceL2cpProfileIndex_Object = MibTableColumn
rcServiceNetworkInterfaceL2cpProfileIndex = _RcServiceNetworkInterfaceL2cpProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 17),
    _RcServiceNetworkInterfaceL2cpProfileIndex_Type()
)
rcServiceNetworkInterfaceL2cpProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceL2cpProfileIndex.setStatus("current")


class _RcServiceNetworkInterfaceFrameFormat_Type(Integer32):
    """Custom type rcServiceNetworkInterfaceFrameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("untag", 0),
          ("tag", 1),
          ("dtag", 2))
    )


_RcServiceNetworkInterfaceFrameFormat_Type.__name__ = "Integer32"
_RcServiceNetworkInterfaceFrameFormat_Object = MibTableColumn
rcServiceNetworkInterfaceFrameFormat = _RcServiceNetworkInterfaceFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 18),
    _RcServiceNetworkInterfaceFrameFormat_Type()
)
rcServiceNetworkInterfaceFrameFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceFrameFormat.setStatus("current")


class _RcServiceNetworkInterfaceLinks_Type(Integer32):
    """Custom type rcServiceNetworkInterfaceLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RcServiceNetworkInterfaceLinks_Type.__name__ = "Integer32"
_RcServiceNetworkInterfaceLinks_Object = MibTableColumn
rcServiceNetworkInterfaceLinks = _RcServiceNetworkInterfaceLinks_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 19),
    _RcServiceNetworkInterfaceLinks_Type()
)
rcServiceNetworkInterfaceLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceLinks.setStatus("current")


class _RcServiceNetworkInterfaceResiliencyMechanisms_Type(Integer32):
    """Custom type rcServiceNetworkInterfaceResiliencyMechanisms based on Integer32"""
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
          ("linkaggregation", 1),
          ("other", 2))
    )


_RcServiceNetworkInterfaceResiliencyMechanisms_Type.__name__ = "Integer32"
_RcServiceNetworkInterfaceResiliencyMechanisms_Object = MibTableColumn
rcServiceNetworkInterfaceResiliencyMechanisms = _RcServiceNetworkInterfaceResiliencyMechanisms_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 20),
    _RcServiceNetworkInterfaceResiliencyMechanisms_Type()
)
rcServiceNetworkInterfaceResiliencyMechanisms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceResiliencyMechanisms.setStatus("current")
_RcServiceNetworkInterfaceMaxEndPointPerOvc_Type = Integer32
_RcServiceNetworkInterfaceMaxEndPointPerOvc_Object = MibTableColumn
rcServiceNetworkInterfaceMaxEndPointPerOvc = _RcServiceNetworkInterfaceMaxEndPointPerOvc_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 3, 1, 21),
    _RcServiceNetworkInterfaceMaxEndPointPerOvc_Type()
)
rcServiceNetworkInterfaceMaxEndPointPerOvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceMaxEndPointPerOvc.setStatus("current")
_RcServiceNetworkInterfaceEndPointMapTable_Object = MibTable
rcServiceNetworkInterfaceEndPointMapTable = _RcServiceNetworkInterfaceEndPointMapTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 4)
)
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceEndPointMapTable.setStatus("current")
_RcServiceNetworkInterfaceEndPointMapEntry_Object = MibTableRow
rcServiceNetworkInterfaceEndPointMapEntry = _RcServiceNetworkInterfaceEndPointMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 4, 1)
)
rcServiceNetworkInterfaceEndPointMapEntry.setIndexNames(
    (0, "SWTICH-SERVICE-MIB", "rcServiceNetworkInterfacePortIndex"),
    (0, "SWTICH-SERVICE-MIB", "rcServiceNetworkInterfaceEndPointMapSVlan"),
)
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceEndPointMapEntry.setStatus("current")
_RcServiceNetworkInterfaceEndPointMapSVlan_Type = Integer32
_RcServiceNetworkInterfaceEndPointMapSVlan_Object = MibTableColumn
rcServiceNetworkInterfaceEndPointMapSVlan = _RcServiceNetworkInterfaceEndPointMapSVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 4, 1, 1),
    _RcServiceNetworkInterfaceEndPointMapSVlan_Type()
)
rcServiceNetworkInterfaceEndPointMapSVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceEndPointMapSVlan.setStatus("current")


class _RcServiceNetworkInterfaceEndPointMapEndPointID_Type(OctetString):
    """Custom type rcServiceNetworkInterfaceEndPointMapEndPointID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 91),
    )


_RcServiceNetworkInterfaceEndPointMapEndPointID_Type.__name__ = "OctetString"
_RcServiceNetworkInterfaceEndPointMapEndPointID_Object = MibTableColumn
rcServiceNetworkInterfaceEndPointMapEndPointID = _RcServiceNetworkInterfaceEndPointMapEndPointID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 4, 1, 2),
    _RcServiceNetworkInterfaceEndPointMapEndPointID_Type()
)
rcServiceNetworkInterfaceEndPointMapEndPointID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceEndPointMapEndPointID.setStatus("current")


class _RcServiceNetworkInterfaceEndPointMapEndPointType_Type(Integer32):
    """Custom type rcServiceNetworkInterfaceEndPointMapEndPointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ovc-endpoint", 0),
          ("typex", 1))
    )


_RcServiceNetworkInterfaceEndPointMapEndPointType_Type.__name__ = "Integer32"
_RcServiceNetworkInterfaceEndPointMapEndPointType_Object = MibTableColumn
rcServiceNetworkInterfaceEndPointMapEndPointType = _RcServiceNetworkInterfaceEndPointMapEndPointType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 4, 1, 3),
    _RcServiceNetworkInterfaceEndPointMapEndPointType_Type()
)
rcServiceNetworkInterfaceEndPointMapEndPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceNetworkInterfaceEndPointMapEndPointType.setStatus("current")
_RcServiceTable_Object = MibTable
rcServiceTable = _RcServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5)
)
if mibBuilder.loadTexts:
    rcServiceTable.setStatus("current")
_RcServiceEntry_Object = MibTableRow
rcServiceEntry = _RcServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1)
)
rcServiceEntry.setIndexNames(
    (0, "SWTICH-SERVICE-MIB", "rcServiceID"),
)
if mibBuilder.loadTexts:
    rcServiceEntry.setStatus("current")


class _RcServiceID_Type(OctetString):
    """Custom type rcServiceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_RcServiceID_Type.__name__ = "OctetString"
_RcServiceID_Object = MibTableColumn
rcServiceID = _RcServiceID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 1),
    _RcServiceID_Type()
)
rcServiceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcServiceID.setStatus("current")


class _RcServiceType_Type(Integer32):
    """Custom type rcServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eline", 0),
          ("elan", 1),
          ("etree", 2),
          ("eaccess", 3))
    )


_RcServiceType_Type.__name__ = "Integer32"
_RcServiceType_Object = MibTableColumn
rcServiceType = _RcServiceType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 2),
    _RcServiceType_Type()
)
rcServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceType.setStatus("current")


class _RcServiceCustomerNameID_Type(OctetString):
    """Custom type rcServiceCustomerNameID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RcServiceCustomerNameID_Type.__name__ = "OctetString"
_RcServiceCustomerNameID_Object = MibTableColumn
rcServiceCustomerNameID = _RcServiceCustomerNameID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 3),
    _RcServiceCustomerNameID_Type()
)
rcServiceCustomerNameID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceCustomerNameID.setStatus("current")
_RcServiceMaxUnis_Type = Integer32
_RcServiceMaxUnis_Object = MibTableColumn
rcServiceMaxUnis = _RcServiceMaxUnis_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 4),
    _RcServiceMaxUnis_Type()
)
rcServiceMaxUnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceMaxUnis.setStatus("current")
_RcServiceMaxEnnis_Type = Integer32
_RcServiceMaxEnnis_Object = MibTableColumn
rcServiceMaxEnnis = _RcServiceMaxEnnis_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 5),
    _RcServiceMaxEnnis_Type()
)
rcServiceMaxEnnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceMaxEnnis.setStatus("current")
_RcServiceMTU_Type = Integer32
_RcServiceMTU_Object = MibTableColumn
rcServiceMTU = _RcServiceMTU_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 6),
    _RcServiceMTU_Type()
)
rcServiceMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceMTU.setStatus("current")
_RcServiceCVlanPreservation_Type = TruthValue
_RcServiceCVlanPreservation_Object = MibTableColumn
rcServiceCVlanPreservation = _RcServiceCVlanPreservation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 7),
    _RcServiceCVlanPreservation_Type()
)
rcServiceCVlanPreservation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceCVlanPreservation.setStatus("current")
_RcServiceCCosPreservation_Type = TruthValue
_RcServiceCCosPreservation_Object = MibTableColumn
rcServiceCCosPreservation = _RcServiceCCosPreservation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 8),
    _RcServiceCCosPreservation_Type()
)
rcServiceCCosPreservation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceCCosPreservation.setStatus("current")
_RcServiceSVlanPreservation_Type = TruthValue
_RcServiceSVlanPreservation_Object = MibTableColumn
rcServiceSVlanPreservation = _RcServiceSVlanPreservation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 9),
    _RcServiceSVlanPreservation_Type()
)
rcServiceSVlanPreservation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceSVlanPreservation.setStatus("current")
_RcServiceSCosPreservation_Type = TruthValue
_RcServiceSCosPreservation_Object = MibTableColumn
rcServiceSCosPreservation = _RcServiceSCosPreservation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 10),
    _RcServiceSCosPreservation_Type()
)
rcServiceSCosPreservation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceSCosPreservation.setStatus("current")
_RcServiceColorForward_Type = TruthValue
_RcServiceColorForward_Object = MibTableColumn
rcServiceColorForward = _RcServiceColorForward_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 11),
    _RcServiceColorForward_Type()
)
rcServiceColorForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceColorForward.setStatus("current")
_RcServiceUnicastDelivery_Type = TruthValue
_RcServiceUnicastDelivery_Object = MibTableColumn
rcServiceUnicastDelivery = _RcServiceUnicastDelivery_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 12),
    _RcServiceUnicastDelivery_Type()
)
rcServiceUnicastDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceUnicastDelivery.setStatus("current")
_RcServiceMulticastDelivery_Type = TruthValue
_RcServiceMulticastDelivery_Object = MibTableColumn
rcServiceMulticastDelivery = _RcServiceMulticastDelivery_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 13),
    _RcServiceMulticastDelivery_Type()
)
rcServiceMulticastDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceMulticastDelivery.setStatus("current")
_RcServiceBroadcastDelivery_Type = TruthValue
_RcServiceBroadcastDelivery_Object = MibTableColumn
rcServiceBroadcastDelivery = _RcServiceBroadcastDelivery_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 14),
    _RcServiceBroadcastDelivery_Type()
)
rcServiceBroadcastDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceBroadcastDelivery.setStatus("current")
_RcServiceL2cpPass_Type = TruthValue
_RcServiceL2cpPass_Object = MibTableColumn
rcServiceL2cpPass = _RcServiceL2cpPass_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 15),
    _RcServiceL2cpPass_Type()
)
rcServiceL2cpPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceL2cpPass.setStatus("current")


class _RcServiceCosType_Type(Integer32):
    """Custom type rcServiceCosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cos-unknown", 0),
          ("cos-baseon-service", 1),
          ("cos-baseon-cos", 2),
          ("cos-baseon-dscp", 3))
    )


_RcServiceCosType_Type.__name__ = "Integer32"
_RcServiceCosType_Object = MibTableColumn
rcServiceCosType = _RcServiceCosType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 16),
    _RcServiceCosType_Type()
)
rcServiceCosType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceCosType.setStatus("current")
_RcServiceVCCosLabel_Type = Integer32
_RcServiceVCCosLabel_Object = MibTableColumn
rcServiceVCCosLabel = _RcServiceVCCosLabel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 17),
    _RcServiceVCCosLabel_Type()
)
rcServiceVCCosLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceVCCosLabel.setStatus("current")
_RcServiceCosMapProfileIndex_Type = Integer32
_RcServiceCosMapProfileIndex_Object = MibTableColumn
rcServiceCosMapProfileIndex = _RcServiceCosMapProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 18),
    _RcServiceCosMapProfileIndex_Type()
)
rcServiceCosMapProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceCosMapProfileIndex.setStatus("current")
_RcServiceDscpMapProfileIndex_Type = Integer32
_RcServiceDscpMapProfileIndex_Object = MibTableColumn
rcServiceDscpMapProfileIndex = _RcServiceDscpMapProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 19),
    _RcServiceDscpMapProfileIndex_Type()
)
rcServiceDscpMapProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceDscpMapProfileIndex.setStatus("current")


class _RcServiceSdpType_Type(Integer32):
    """Custom type rcServiceSdpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdp-none", 0),
          ("sdp-vlan", 1),
          ("sdp-mpls", 2))
    )


_RcServiceSdpType_Type.__name__ = "Integer32"
_RcServiceSdpType_Object = MibTableColumn
rcServiceSdpType = _RcServiceSdpType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 20),
    _RcServiceSdpType_Type()
)
rcServiceSdpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceSdpType.setStatus("current")
_RcServiceSdpIndex_Type = Integer32
_RcServiceSdpIndex_Object = MibTableColumn
rcServiceSdpIndex = _RcServiceSdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 21),
    _RcServiceSdpIndex_Type()
)
rcServiceSdpIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceSdpIndex.setStatus("current")
_RcServicePTIndex_Type = Integer32
_RcServicePTIndex_Object = MibTableColumn
rcServicePTIndex = _RcServicePTIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 22),
    _RcServicePTIndex_Type()
)
rcServicePTIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServicePTIndex.setStatus("current")
_RcServiceMaintenanceTimeStart_Type = DateAndTime
_RcServiceMaintenanceTimeStart_Object = MibTableColumn
rcServiceMaintenanceTimeStart = _RcServiceMaintenanceTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 23),
    _RcServiceMaintenanceTimeStart_Type()
)
rcServiceMaintenanceTimeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceMaintenanceTimeStart.setStatus("current")
_RcServiceMaintenanceTimeStop_Type = DateAndTime
_RcServiceMaintenanceTimeStop_Object = MibTableColumn
rcServiceMaintenanceTimeStop = _RcServiceMaintenanceTimeStop_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 24),
    _RcServiceMaintenanceTimeStop_Type()
)
rcServiceMaintenanceTimeStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceMaintenanceTimeStop.setStatus("current")
_RcServicePerfermanceTestScheduleLife_Type = Unsigned32
_RcServicePerfermanceTestScheduleLife_Object = MibTableColumn
rcServicePerfermanceTestScheduleLife = _RcServicePerfermanceTestScheduleLife_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 25),
    _RcServicePerfermanceTestScheduleLife_Type()
)
rcServicePerfermanceTestScheduleLife.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServicePerfermanceTestScheduleLife.setStatus("current")
_RcServicePerfermanceTestSchedulePeriod_Type = Unsigned32
_RcServicePerfermanceTestSchedulePeriod_Object = MibTableColumn
rcServicePerfermanceTestSchedulePeriod = _RcServicePerfermanceTestSchedulePeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 26),
    _RcServicePerfermanceTestSchedulePeriod_Type()
)
rcServicePerfermanceTestSchedulePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServicePerfermanceTestSchedulePeriod.setStatus("current")
_RcServicePerfermanceTestScheduleInterval_Type = Unsigned32
_RcServicePerfermanceTestScheduleInterval_Object = MibTableColumn
rcServicePerfermanceTestScheduleInterval = _RcServicePerfermanceTestScheduleInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 27),
    _RcServicePerfermanceTestScheduleInterval_Type()
)
rcServicePerfermanceTestScheduleInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServicePerfermanceTestScheduleInterval.setStatus("current")
_RcServicePerfermanceTestOperate_Type = TruthValue
_RcServicePerfermanceTestOperate_Object = MibTableColumn
rcServicePerfermanceTestOperate = _RcServicePerfermanceTestOperate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 28),
    _RcServicePerfermanceTestOperate_Type()
)
rcServicePerfermanceTestOperate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServicePerfermanceTestOperate.setStatus("current")


class _RcServiceL2LoopbackEtherType_Type(Integer32):
    """Custom type rcServiceL2LoopbackEtherType based on Integer32"""
    defaultValue = 2208


_RcServiceL2LoopbackEtherType_Type.__name__ = "Integer32"
_RcServiceL2LoopbackEtherType_Object = MibTableColumn
rcServiceL2LoopbackEtherType = _RcServiceL2LoopbackEtherType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 29),
    _RcServiceL2LoopbackEtherType_Type()
)
rcServiceL2LoopbackEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceL2LoopbackEtherType.setStatus("current")
_RcServiceL2LoopbackOperate_Type = TruthValue
_RcServiceL2LoopbackOperate_Object = MibTableColumn
rcServiceL2LoopbackOperate = _RcServiceL2LoopbackOperate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 30),
    _RcServiceL2LoopbackOperate_Type()
)
rcServiceL2LoopbackOperate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceL2LoopbackOperate.setStatus("current")


class _RcServiceEtherSamPerformanceDuration_Type(Integer32):
    """Custom type rcServiceEtherSamPerformanceDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 1440),
    )


_RcServiceEtherSamPerformanceDuration_Type.__name__ = "Integer32"
_RcServiceEtherSamPerformanceDuration_Object = MibTableColumn
rcServiceEtherSamPerformanceDuration = _RcServiceEtherSamPerformanceDuration_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 31),
    _RcServiceEtherSamPerformanceDuration_Type()
)
rcServiceEtherSamPerformanceDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceEtherSamPerformanceDuration.setStatus("current")


class _RcServiceEtherSamPerformanceBW_Type(Unsigned32):
    """Custom type rcServiceEtherSamPerformanceBW based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcServiceEtherSamPerformanceBW_Type.__name__ = "Unsigned32"
_RcServiceEtherSamPerformanceBW_Object = MibTableColumn
rcServiceEtherSamPerformanceBW = _RcServiceEtherSamPerformanceBW_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 32),
    _RcServiceEtherSamPerformanceBW_Type()
)
rcServiceEtherSamPerformanceBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceEtherSamPerformanceBW.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceEtherSamPerformanceBW.setUnits("milli-percent")


class _RcServiceEtherSamFlowProfileIndex_Type(Integer32):
    """Custom type rcServiceEtherSamFlowProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RcServiceEtherSamFlowProfileIndex_Type.__name__ = "Integer32"
_RcServiceEtherSamFlowProfileIndex_Object = MibTableColumn
rcServiceEtherSamFlowProfileIndex = _RcServiceEtherSamFlowProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 33),
    _RcServiceEtherSamFlowProfileIndex_Type()
)
rcServiceEtherSamFlowProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceEtherSamFlowProfileIndex.setStatus("current")


class _RcServiceEtherSamCfgBypassUni_Type(TruthValue):
    """Custom type rcServiceEtherSamCfgBypassUni based on TruthValue"""
    defaultValue = 2


_RcServiceEtherSamCfgBypassUni_Type.__name__ = "TruthValue"
_RcServiceEtherSamCfgBypassUni_Object = MibTableColumn
rcServiceEtherSamCfgBypassUni = _RcServiceEtherSamCfgBypassUni_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 34),
    _RcServiceEtherSamCfgBypassUni_Type()
)
rcServiceEtherSamCfgBypassUni.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceEtherSamCfgBypassUni.setStatus("current")
_RcServiceEtherSamTestElapsedTime_Type = TimeInterval
_RcServiceEtherSamTestElapsedTime_Object = MibTableColumn
rcServiceEtherSamTestElapsedTime = _RcServiceEtherSamTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 35),
    _RcServiceEtherSamTestElapsedTime_Type()
)
rcServiceEtherSamTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceEtherSamTestElapsedTime.setStatus("current")


class _RcServiceEtherSamTestType_Type(Integer32):
    """Custom type rcServiceEtherSamTestType based on Integer32"""
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
        *(("configuration", 1),
          ("performance", 2),
          ("both", 3),
          ("rfc2544", 4),
          ("performance-inservice", 5))
    )


_RcServiceEtherSamTestType_Type.__name__ = "Integer32"
_RcServiceEtherSamTestType_Object = MibTableColumn
rcServiceEtherSamTestType = _RcServiceEtherSamTestType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 36),
    _RcServiceEtherSamTestType_Type()
)
rcServiceEtherSamTestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceEtherSamTestType.setStatus("current")
_RcServiceEtherSamOperate_Type = TruthValue
_RcServiceEtherSamOperate_Object = MibTableColumn
rcServiceEtherSamOperate = _RcServiceEtherSamOperate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 37),
    _RcServiceEtherSamOperate_Type()
)
rcServiceEtherSamOperate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceEtherSamOperate.setStatus("current")


class _RcServiceEtherSamTestResult_Type(Integer32):
    """Custom type rcServiceEtherSamTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_RcServiceEtherSamTestResult_Type.__name__ = "Integer32"
_RcServiceEtherSamTestResult_Object = MibTableColumn
rcServiceEtherSamTestResult = _RcServiceEtherSamTestResult_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 38),
    _RcServiceEtherSamTestResult_Type()
)
rcServiceEtherSamTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceEtherSamTestResult.setStatus("current")
_RcServiceEtherSamTimeCfgWillTake_Type = TimeInterval
_RcServiceEtherSamTimeCfgWillTake_Object = MibTableColumn
rcServiceEtherSamTimeCfgWillTake = _RcServiceEtherSamTimeCfgWillTake_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 39),
    _RcServiceEtherSamTimeCfgWillTake_Type()
)
rcServiceEtherSamTimeCfgWillTake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceEtherSamTimeCfgWillTake.setStatus("current")


class _RcServiceEtherSamClearResult_Type(TruthValue):
    """Custom type rcServiceEtherSamClearResult based on TruthValue"""
    defaultValue = 2


_RcServiceEtherSamClearResult_Type.__name__ = "TruthValue"
_RcServiceEtherSamClearResult_Object = MibTableColumn
rcServiceEtherSamClearResult = _RcServiceEtherSamClearResult_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 40),
    _RcServiceEtherSamClearResult_Type()
)
rcServiceEtherSamClearResult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceEtherSamClearResult.setStatus("current")
_RcServiceMdIndex_Type = Unsigned32
_RcServiceMdIndex_Object = MibTableColumn
rcServiceMdIndex = _RcServiceMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 41),
    _RcServiceMdIndex_Type()
)
rcServiceMdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceMdIndex.setStatus("current")
_RcServiceMaIndex_Type = Unsigned32
_RcServiceMaIndex_Object = MibTableColumn
rcServiceMaIndex = _RcServiceMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 42),
    _RcServiceMaIndex_Type()
)
rcServiceMaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceMaIndex.setStatus("current")
_RcServiceOperStatus_Type = TruthValue
_RcServiceOperStatus_Object = MibTableColumn
rcServiceOperStatus = _RcServiceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 43),
    _RcServiceOperStatus_Type()
)
rcServiceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceOperStatus.setStatus("current")


class _RcServiceCcStatus_Type(Integer32):
    """Custom type rcServiceCcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full-work", 0),
          ("part-work", 1),
          ("no-work", 2))
    )


_RcServiceCcStatus_Type.__name__ = "Integer32"
_RcServiceCcStatus_Object = MibTableColumn
rcServiceCcStatus = _RcServiceCcStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 44),
    _RcServiceCcStatus_Type()
)
rcServiceCcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceCcStatus.setStatus("current")


class _RcServicePerfermanceTestType_Type(Integer32):
    """Custom type rcServicePerfermanceTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lmLmm", 1),
          ("lmSlm", 2))
    )


_RcServicePerfermanceTestType_Type.__name__ = "Integer32"
_RcServicePerfermanceTestType_Object = MibTableColumn
rcServicePerfermanceTestType = _RcServicePerfermanceTestType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 45),
    _RcServicePerfermanceTestType_Type()
)
rcServicePerfermanceTestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServicePerfermanceTestType.setStatus("current")


class _RcServiceEtherSamSlaJitterType_Type(Integer32):
    """Custom type rcServiceEtherSamSlaJitterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dm", 1),
          ("l2loopback", 2))
    )


_RcServiceEtherSamSlaJitterType_Type.__name__ = "Integer32"
_RcServiceEtherSamSlaJitterType_Object = MibTableColumn
rcServiceEtherSamSlaJitterType = _RcServiceEtherSamSlaJitterType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 46),
    _RcServiceEtherSamSlaJitterType_Type()
)
rcServiceEtherSamSlaJitterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceEtherSamSlaJitterType.setStatus("current")
_RcServiceRowStatus_Type = RowStatus
_RcServiceRowStatus_Object = MibTableColumn
rcServiceRowStatus = _RcServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 5, 1, 100),
    _RcServiceRowStatus_Type()
)
rcServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceRowStatus.setStatus("current")
_RcServiceCustomerTable_Object = MibTable
rcServiceCustomerTable = _RcServiceCustomerTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 6)
)
if mibBuilder.loadTexts:
    rcServiceCustomerTable.setStatus("current")
_RcServiceCustomerEntry_Object = MibTableRow
rcServiceCustomerEntry = _RcServiceCustomerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 6, 1)
)
rcServiceCustomerEntry.setIndexNames(
    (0, "SWTICH-SERVICE-MIB", "rcServiceCustomerName"),
)
if mibBuilder.loadTexts:
    rcServiceCustomerEntry.setStatus("current")


class _RcServiceCustomerName_Type(OctetString):
    """Custom type rcServiceCustomerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RcServiceCustomerName_Type.__name__ = "OctetString"
_RcServiceCustomerName_Object = MibTableColumn
rcServiceCustomerName = _RcServiceCustomerName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 6, 1, 1),
    _RcServiceCustomerName_Type()
)
rcServiceCustomerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcServiceCustomerName.setStatus("current")


class _RcServiceCustomerContact_Type(OctetString):
    """Custom type rcServiceCustomerContact based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RcServiceCustomerContact_Type.__name__ = "OctetString"
_RcServiceCustomerContact_Object = MibTableColumn
rcServiceCustomerContact = _RcServiceCustomerContact_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 6, 1, 2),
    _RcServiceCustomerContact_Type()
)
rcServiceCustomerContact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceCustomerContact.setStatus("current")


class _RcServiceCustomerPhone_Type(OctetString):
    """Custom type rcServiceCustomerPhone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RcServiceCustomerPhone_Type.__name__ = "OctetString"
_RcServiceCustomerPhone_Object = MibTableColumn
rcServiceCustomerPhone = _RcServiceCustomerPhone_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 6, 1, 3),
    _RcServiceCustomerPhone_Type()
)
rcServiceCustomerPhone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceCustomerPhone.setStatus("current")
_RcServiceCustomerRowStatus_Type = RowStatus
_RcServiceCustomerRowStatus_Object = MibTableColumn
rcServiceCustomerRowStatus = _RcServiceCustomerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 6, 1, 4),
    _RcServiceCustomerRowStatus_Type()
)
rcServiceCustomerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceCustomerRowStatus.setStatus("current")
_RcServiceCosLabelTable_Object = MibTable
rcServiceCosLabelTable = _RcServiceCosLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 7)
)
if mibBuilder.loadTexts:
    rcServiceCosLabelTable.setStatus("current")
_RcServiceCosLabelEntry_Object = MibTableRow
rcServiceCosLabelEntry = _RcServiceCosLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 7, 1)
)
rcServiceCosLabelEntry.setIndexNames(
    (0, "SWTICH-SERVICE-MIB", "rcServiceID"),
    (0, "SWTICH-SERVICE-MIB", "rcServiceCosLabel"),
)
if mibBuilder.loadTexts:
    rcServiceCosLabelEntry.setStatus("current")
_RcServiceCosLabelPerfermanceTestEnable_Type = TruthValue
_RcServiceCosLabelPerfermanceTestEnable_Object = MibTableColumn
rcServiceCosLabelPerfermanceTestEnable = _RcServiceCosLabelPerfermanceTestEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 7, 1, 1),
    _RcServiceCosLabelPerfermanceTestEnable_Type()
)
rcServiceCosLabelPerfermanceTestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcServiceCosLabelPerfermanceTestEnable.setStatus("current")
_RcServiceCosLabelEtherSAMEnable_Type = TruthValue
_RcServiceCosLabelEtherSAMEnable_Object = MibTableColumn
rcServiceCosLabelEtherSAMEnable = _RcServiceCosLabelEtherSAMEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 7, 1, 2),
    _RcServiceCosLabelEtherSAMEnable_Type()
)
rcServiceCosLabelEtherSAMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcServiceCosLabelEtherSAMEnable.setStatus("current")
_RcServiceEndPointTable_Object = MibTable
rcServiceEndPointTable = _RcServiceEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 8)
)
if mibBuilder.loadTexts:
    rcServiceEndPointTable.setStatus("current")
_RcServiceEndPointEntry_Object = MibTableRow
rcServiceEndPointEntry = _RcServiceEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 8, 1)
)
rcServiceEndPointEntry.setIndexNames(
    (0, "SWTICH-SERVICE-MIB", "rcServiceID"),
    (0, "SWTICH-SERVICE-MIB", "rcServiceNetworkInterfaceID"),
)
if mibBuilder.loadTexts:
    rcServiceEndPointEntry.setStatus("current")


class _RcServiceEndPointType_Type(Integer32):
    """Custom type rcServiceEndPointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("evc-per-uni", 1),
          ("ovc-per-uni", 2),
          ("ovc-per-enni", 3))
    )


_RcServiceEndPointType_Type.__name__ = "Integer32"
_RcServiceEndPointType_Object = MibTableColumn
rcServiceEndPointType = _RcServiceEndPointType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 8, 1, 1),
    _RcServiceEndPointType_Type()
)
rcServiceEndPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceEndPointType.setStatus("current")


class _RcServiceEndPointMPType_Type(Integer32):
    """Custom type rcServiceEndPointMPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("root", 1),
          ("leaf", 2))
    )


_RcServiceEndPointMPType_Type.__name__ = "Integer32"
_RcServiceEndPointMPType_Object = MibTableColumn
rcServiceEndPointMPType = _RcServiceEndPointMPType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 8, 1, 2),
    _RcServiceEndPointMPType_Type()
)
rcServiceEndPointMPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceEndPointMPType.setStatus("current")


class _RcServiceEndPointMapCVlans_Type(OctetString):
    """Custom type rcServiceEndPointMapCVlans based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_RcServiceEndPointMapCVlans_Type.__name__ = "OctetString"
_RcServiceEndPointMapCVlans_Object = MibTableColumn
rcServiceEndPointMapCVlans = _RcServiceEndPointMapCVlans_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 8, 1, 3),
    _RcServiceEndPointMapCVlans_Type()
)
rcServiceEndPointMapCVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceEndPointMapCVlans.setStatus("current")
_RcServiceEndPointInBwProfileIndex_Type = Integer32
_RcServiceEndPointInBwProfileIndex_Object = MibTableColumn
rcServiceEndPointInBwProfileIndex = _RcServiceEndPointInBwProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 8, 1, 4),
    _RcServiceEndPointInBwProfileIndex_Type()
)
rcServiceEndPointInBwProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceEndPointInBwProfileIndex.setStatus("current")
_RcServiceEndPointOutBwProfileIndex_Type = Integer32
_RcServiceEndPointOutBwProfileIndex_Object = MibTableColumn
rcServiceEndPointOutBwProfileIndex = _RcServiceEndPointOutBwProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 8, 1, 5),
    _RcServiceEndPointOutBwProfileIndex_Type()
)
rcServiceEndPointOutBwProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceEndPointOutBwProfileIndex.setStatus("current")


class _RcServiceEndPointLMep_Type(Unsigned32):
    """Custom type rcServiceEndPointLMep based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_RcServiceEndPointLMep_Type.__name__ = "Unsigned32"
_RcServiceEndPointLMep_Object = MibTableColumn
rcServiceEndPointLMep = _RcServiceEndPointLMep_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 8, 1, 6),
    _RcServiceEndPointLMep_Type()
)
rcServiceEndPointLMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceEndPointLMep.setStatus("current")
_RcServiceEndPointCCEnable_Type = TruthValue
_RcServiceEndPointCCEnable_Object = MibTableColumn
rcServiceEndPointCCEnable = _RcServiceEndPointCCEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 8, 1, 7),
    _RcServiceEndPointCCEnable_Type()
)
rcServiceEndPointCCEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceEndPointCCEnable.setStatus("current")
_RcServiceEndPointPMEnable_Type = TruthValue
_RcServiceEndPointPMEnable_Object = MibTableColumn
rcServiceEndPointPMEnable = _RcServiceEndPointPMEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 8, 1, 8),
    _RcServiceEndPointPMEnable_Type()
)
rcServiceEndPointPMEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceEndPointPMEnable.setStatus("current")
_RcServiceEndPointRowStatus_Type = RowStatus
_RcServiceEndPointRowStatus_Object = MibTableColumn
rcServiceEndPointRowStatus = _RcServiceEndPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 8, 1, 100),
    _RcServiceEndPointRowStatus_Type()
)
rcServiceEndPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceEndPointRowStatus.setStatus("current")
_RcServicesEndPointCosLabelTable_Object = MibTable
rcServicesEndPointCosLabelTable = _RcServicesEndPointCosLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 9)
)
if mibBuilder.loadTexts:
    rcServicesEndPointCosLabelTable.setStatus("current")
_RcServicesEndPointCosLabelEntry_Object = MibTableRow
rcServicesEndPointCosLabelEntry = _RcServicesEndPointCosLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 9, 1)
)
rcServicesEndPointCosLabelEntry.setIndexNames(
    (0, "SWTICH-SERVICE-MIB", "rcServiceID"),
    (0, "SWTICH-SERVICE-MIB", "rcServiceNetworkInterfaceID"),
    (0, "SWTICH-SERVICE-MIB", "rcServiceCosLabel"),
)
if mibBuilder.loadTexts:
    rcServicesEndPointCosLabelEntry.setStatus("current")
_RcServiceEndPointCosLabelInBwProfileIndex_Type = Integer32
_RcServiceEndPointCosLabelInBwProfileIndex_Object = MibTableColumn
rcServiceEndPointCosLabelInBwProfileIndex = _RcServiceEndPointCosLabelInBwProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 9, 1, 1),
    _RcServiceEndPointCosLabelInBwProfileIndex_Type()
)
rcServiceEndPointCosLabelInBwProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceEndPointCosLabelInBwProfileIndex.setStatus("current")
_RcServiceEndPointCosLabelOutBwProfileIndex_Type = Integer32
_RcServiceEndPointCosLabelOutBwProfileIndex_Object = MibTableColumn
rcServiceEndPointCosLabelOutBwProfileIndex = _RcServiceEndPointCosLabelOutBwProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 9, 1, 2),
    _RcServiceEndPointCosLabelOutBwProfileIndex_Type()
)
rcServiceEndPointCosLabelOutBwProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceEndPointCosLabelOutBwProfileIndex.setStatus("current")
_RcServiceFarEndPointTable_Object = MibTable
rcServiceFarEndPointTable = _RcServiceFarEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 10)
)
if mibBuilder.loadTexts:
    rcServiceFarEndPointTable.setStatus("current")
_RcServiceFarEndPointEntry_Object = MibTableRow
rcServiceFarEndPointEntry = _RcServiceFarEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 10, 1)
)
rcServiceFarEndPointEntry.setIndexNames(
    (0, "SWTICH-SERVICE-MIB", "rcServiceID"),
    (0, "SWTICH-SERVICE-MIB", "rcServiceNetworkInterfaceID"),
    (0, "SWTICH-SERVICE-MIB", "rcServiceFarEndNetworkInterfaceID"),
)
if mibBuilder.loadTexts:
    rcServiceFarEndPointEntry.setStatus("current")


class _RcServiceFarEndNetworkInterfaceID_Type(OctetString):
    """Custom type rcServiceFarEndNetworkInterfaceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_RcServiceFarEndNetworkInterfaceID_Type.__name__ = "OctetString"
_RcServiceFarEndNetworkInterfaceID_Object = MibTableColumn
rcServiceFarEndNetworkInterfaceID = _RcServiceFarEndNetworkInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 10, 1, 1),
    _RcServiceFarEndNetworkInterfaceID_Type()
)
rcServiceFarEndNetworkInterfaceID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceFarEndNetworkInterfaceID.setStatus("current")


class _RcServiceFarEndPointRMep_Type(Unsigned32):
    """Custom type rcServiceFarEndPointRMep based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_RcServiceFarEndPointRMep_Type.__name__ = "Unsigned32"
_RcServiceFarEndPointRMep_Object = MibTableColumn
rcServiceFarEndPointRMep = _RcServiceFarEndPointRMep_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 10, 1, 2),
    _RcServiceFarEndPointRMep_Type()
)
rcServiceFarEndPointRMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceFarEndPointRMep.setStatus("current")
_RcServiceFarEndPointPerfermanceTestEnable_Type = TruthValue
_RcServiceFarEndPointPerfermanceTestEnable_Object = MibTableColumn
rcServiceFarEndPointPerfermanceTestEnable = _RcServiceFarEndPointPerfermanceTestEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 10, 1, 3),
    _RcServiceFarEndPointPerfermanceTestEnable_Type()
)
rcServiceFarEndPointPerfermanceTestEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceFarEndPointPerfermanceTestEnable.setStatus("current")
_RcServiceFarEndPointEtherSAMEnable_Type = TruthValue
_RcServiceFarEndPointEtherSAMEnable_Object = MibTableColumn
rcServiceFarEndPointEtherSAMEnable = _RcServiceFarEndPointEtherSAMEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 10, 1, 4),
    _RcServiceFarEndPointEtherSAMEnable_Type()
)
rcServiceFarEndPointEtherSAMEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceFarEndPointEtherSAMEnable.setStatus("current")
_RcServiceFarEndPointL2LoopbackEnable_Type = TruthValue
_RcServiceFarEndPointL2LoopbackEnable_Object = MibTableColumn
rcServiceFarEndPointL2LoopbackEnable = _RcServiceFarEndPointL2LoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 10, 1, 5),
    _RcServiceFarEndPointL2LoopbackEnable_Type()
)
rcServiceFarEndPointL2LoopbackEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceFarEndPointL2LoopbackEnable.setStatus("current")


class _RcServiceFarEndPointCcStatus_Type(Integer32):
    """Custom type rcServiceFarEndPointCcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("DEFECT-NONE", 0),
          ("DEFECT-RDI-CCM", 1),
          ("DEFECT-MAC-STATUS", 2),
          ("DEFECT-REMOTE-CCM", 3),
          ("DEFECT-ERROR-CCM", 4),
          ("DEFECT-XCON-CCM", 5))
    )


_RcServiceFarEndPointCcStatus_Type.__name__ = "Integer32"
_RcServiceFarEndPointCcStatus_Object = MibTableColumn
rcServiceFarEndPointCcStatus = _RcServiceFarEndPointCcStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 10, 1, 6),
    _RcServiceFarEndPointCcStatus_Type()
)
rcServiceFarEndPointCcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCcStatus.setStatus("current")
_RcServiceFarEndPointIPAddressType_Type = InetAddressType
_RcServiceFarEndPointIPAddressType_Object = MibTableColumn
rcServiceFarEndPointIPAddressType = _RcServiceFarEndPointIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 10, 1, 7),
    _RcServiceFarEndPointIPAddressType_Type()
)
rcServiceFarEndPointIPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceFarEndPointIPAddressType.setStatus("current")
_RcServiceFarEndPointIPAddress_Type = InetAddress
_RcServiceFarEndPointIPAddress_Object = MibTableColumn
rcServiceFarEndPointIPAddress = _RcServiceFarEndPointIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 10, 1, 8),
    _RcServiceFarEndPointIPAddress_Type()
)
rcServiceFarEndPointIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceFarEndPointIPAddress.setStatus("current")
_RcServiceFarEndPointMacAddress_Type = MacAddress
_RcServiceFarEndPointMacAddress_Object = MibTableColumn
rcServiceFarEndPointMacAddress = _RcServiceFarEndPointMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 10, 1, 9),
    _RcServiceFarEndPointMacAddress_Type()
)
rcServiceFarEndPointMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceFarEndPointMacAddress.setStatus("current")


class _RcServiceFarEndPointType_Type(Integer32):
    """Custom type rcServiceFarEndPointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("farend-rmep", 1),
          ("farend-ip", 2),
          ("farend_mac", 3))
    )


_RcServiceFarEndPointType_Type.__name__ = "Integer32"
_RcServiceFarEndPointType_Object = MibTableColumn
rcServiceFarEndPointType = _RcServiceFarEndPointType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 10, 1, 10),
    _RcServiceFarEndPointType_Type()
)
rcServiceFarEndPointType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceFarEndPointType.setStatus("current")
_RcServiceFarEndPointRowStatus_Type = RowStatus
_RcServiceFarEndPointRowStatus_Object = MibTableColumn
rcServiceFarEndPointRowStatus = _RcServiceFarEndPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 10, 1, 100),
    _RcServiceFarEndPointRowStatus_Type()
)
rcServiceFarEndPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceFarEndPointRowStatus.setStatus("current")
_RcServiceFarEndPointCosLabelTable_Object = MibTable
rcServiceFarEndPointCosLabelTable = _RcServiceFarEndPointCosLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11)
)
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelTable.setStatus("current")
_RcServiceFarEndPointCosLabelEntry_Object = MibTableRow
rcServiceFarEndPointCosLabelEntry = _RcServiceFarEndPointCosLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1)
)
rcServiceFarEndPointCosLabelEntry.setIndexNames(
    (0, "SWTICH-SERVICE-MIB", "rcServiceID"),
    (0, "SWTICH-SERVICE-MIB", "rcServiceNetworkInterfaceID"),
    (0, "SWTICH-SERVICE-MIB", "rcServiceFarEndNetworkInterfaceID"),
    (0, "SWTICH-SERVICE-MIB", "rcServiceCosLabel"),
)
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelEntry.setStatus("current")
_RcServiceFarEndPointCosLabelShortStartTime_Type = DateAndTime
_RcServiceFarEndPointCosLabelShortStartTime_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortStartTime = _RcServiceFarEndPointCosLabelShortStartTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 1),
    _RcServiceFarEndPointCosLabelShortStartTime_Type()
)
rcServiceFarEndPointCosLabelShortStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortStartTime.setStatus("current")
_RcServiceFarEndPointCosLabelShortTwowayFD_Type = Unsigned32
_RcServiceFarEndPointCosLabelShortTwowayFD_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortTwowayFD = _RcServiceFarEndPointCosLabelShortTwowayFD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 2),
    _RcServiceFarEndPointCosLabelShortTwowayFD_Type()
)
rcServiceFarEndPointCosLabelShortTwowayFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortTwowayFD.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortTwowayFD.setUnits("microseconds")
_RcServiceFarEndPointCosLabelShortTwowayMaxFD_Type = Unsigned32
_RcServiceFarEndPointCosLabelShortTwowayMaxFD_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortTwowayMaxFD = _RcServiceFarEndPointCosLabelShortTwowayMaxFD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 3),
    _RcServiceFarEndPointCosLabelShortTwowayMaxFD_Type()
)
rcServiceFarEndPointCosLabelShortTwowayMaxFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortTwowayMaxFD.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortTwowayMaxFD.setUnits("microseconds")
_RcServiceFarEndPointCosLabelShortTwowayMinFD_Type = Unsigned32
_RcServiceFarEndPointCosLabelShortTwowayMinFD_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortTwowayMinFD = _RcServiceFarEndPointCosLabelShortTwowayMinFD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 4),
    _RcServiceFarEndPointCosLabelShortTwowayMinFD_Type()
)
rcServiceFarEndPointCosLabelShortTwowayMinFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortTwowayMinFD.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortTwowayMinFD.setUnits("microseconds")
_RcServiceFarEndPointCosLabelShortTwowayMFD_Type = Unsigned32
_RcServiceFarEndPointCosLabelShortTwowayMFD_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortTwowayMFD = _RcServiceFarEndPointCosLabelShortTwowayMFD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 5),
    _RcServiceFarEndPointCosLabelShortTwowayMFD_Type()
)
rcServiceFarEndPointCosLabelShortTwowayMFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortTwowayMFD.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortTwowayMFD.setUnits("microseconds")
_RcServiceFarEndPointCosLabelShortTwowayFDR_Type = Unsigned32
_RcServiceFarEndPointCosLabelShortTwowayFDR_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortTwowayFDR = _RcServiceFarEndPointCosLabelShortTwowayFDR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 6),
    _RcServiceFarEndPointCosLabelShortTwowayFDR_Type()
)
rcServiceFarEndPointCosLabelShortTwowayFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortTwowayFDR.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortTwowayFDR.setUnits("microseconds")
_RcServiceFarEndPointCosLabelShortTwowayIFDV_Type = Unsigned32
_RcServiceFarEndPointCosLabelShortTwowayIFDV_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortTwowayIFDV = _RcServiceFarEndPointCosLabelShortTwowayIFDV_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 7),
    _RcServiceFarEndPointCosLabelShortTwowayIFDV_Type()
)
rcServiceFarEndPointCosLabelShortTwowayIFDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortTwowayIFDV.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortTwowayIFDV.setUnits("microseconds")
_RcServiceFarEndPointCosLabelShortTwowayMaxIFDV_Type = Unsigned32
_RcServiceFarEndPointCosLabelShortTwowayMaxIFDV_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortTwowayMaxIFDV = _RcServiceFarEndPointCosLabelShortTwowayMaxIFDV_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 8),
    _RcServiceFarEndPointCosLabelShortTwowayMaxIFDV_Type()
)
rcServiceFarEndPointCosLabelShortTwowayMaxIFDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortTwowayMaxIFDV.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortTwowayMaxIFDV.setUnits("microseconds")
_RcServiceFarEndPointCosLabelShortTwowayMinIFDV_Type = Unsigned32
_RcServiceFarEndPointCosLabelShortTwowayMinIFDV_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortTwowayMinIFDV = _RcServiceFarEndPointCosLabelShortTwowayMinIFDV_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 9),
    _RcServiceFarEndPointCosLabelShortTwowayMinIFDV_Type()
)
rcServiceFarEndPointCosLabelShortTwowayMinIFDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortTwowayMinIFDV.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortTwowayMinIFDV.setUnits("microseconds")
_RcServiceFarEndPointCosLabelShortTwowayMIFDV_Type = Unsigned32
_RcServiceFarEndPointCosLabelShortTwowayMIFDV_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortTwowayMIFDV = _RcServiceFarEndPointCosLabelShortTwowayMIFDV_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 10),
    _RcServiceFarEndPointCosLabelShortTwowayMIFDV_Type()
)
rcServiceFarEndPointCosLabelShortTwowayMIFDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortTwowayMIFDV.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortTwowayMIFDV.setUnits("microseconds")


class _RcServiceFarEndPointCosLabelShortForwardFLR_Type(Unsigned32):
    """Custom type rcServiceFarEndPointCosLabelShortForwardFLR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcServiceFarEndPointCosLabelShortForwardFLR_Type.__name__ = "Unsigned32"
_RcServiceFarEndPointCosLabelShortForwardFLR_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortForwardFLR = _RcServiceFarEndPointCosLabelShortForwardFLR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 11),
    _RcServiceFarEndPointCosLabelShortForwardFLR_Type()
)
rcServiceFarEndPointCosLabelShortForwardFLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortForwardFLR.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortForwardFLR.setUnits("milli-percent")


class _RcServiceFarEndPointCosLabelShortBackwardFLR_Type(Unsigned32):
    """Custom type rcServiceFarEndPointCosLabelShortBackwardFLR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcServiceFarEndPointCosLabelShortBackwardFLR_Type.__name__ = "Unsigned32"
_RcServiceFarEndPointCosLabelShortBackwardFLR_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortBackwardFLR = _RcServiceFarEndPointCosLabelShortBackwardFLR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 12),
    _RcServiceFarEndPointCosLabelShortBackwardFLR_Type()
)
rcServiceFarEndPointCosLabelShortBackwardFLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortBackwardFLR.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortBackwardFLR.setUnits("milli-percent")


class _RcServiceFarEndPointCosLabelShortForwardAvail_Type(Unsigned32):
    """Custom type rcServiceFarEndPointCosLabelShortForwardAvail based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcServiceFarEndPointCosLabelShortForwardAvail_Type.__name__ = "Unsigned32"
_RcServiceFarEndPointCosLabelShortForwardAvail_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortForwardAvail = _RcServiceFarEndPointCosLabelShortForwardAvail_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 13),
    _RcServiceFarEndPointCosLabelShortForwardAvail_Type()
)
rcServiceFarEndPointCosLabelShortForwardAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortForwardAvail.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortForwardAvail.setUnits("milli-percent")


class _RcServiceFarEndPointCosLabelShortBackwardAvail_Type(Unsigned32):
    """Custom type rcServiceFarEndPointCosLabelShortBackwardAvail based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcServiceFarEndPointCosLabelShortBackwardAvail_Type.__name__ = "Unsigned32"
_RcServiceFarEndPointCosLabelShortBackwardAvail_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortBackwardAvail = _RcServiceFarEndPointCosLabelShortBackwardAvail_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 14),
    _RcServiceFarEndPointCosLabelShortBackwardAvail_Type()
)
rcServiceFarEndPointCosLabelShortBackwardAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortBackwardAvail.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortBackwardAvail.setUnits("milli-percent")
_RcServiceFarEndPointCosLabelShortForwardHLI_Type = Unsigned32
_RcServiceFarEndPointCosLabelShortForwardHLI_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortForwardHLI = _RcServiceFarEndPointCosLabelShortForwardHLI_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 15),
    _RcServiceFarEndPointCosLabelShortForwardHLI_Type()
)
rcServiceFarEndPointCosLabelShortForwardHLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortForwardHLI.setStatus("current")
_RcServiceFarEndPointCosLabelShortBackwardHLI_Type = Unsigned32
_RcServiceFarEndPointCosLabelShortBackwardHLI_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortBackwardHLI = _RcServiceFarEndPointCosLabelShortBackwardHLI_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 16),
    _RcServiceFarEndPointCosLabelShortBackwardHLI_Type()
)
rcServiceFarEndPointCosLabelShortBackwardHLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortBackwardHLI.setStatus("current")
_RcServiceFarEndPointCosLabelShortForwardCHLI_Type = Unsigned32
_RcServiceFarEndPointCosLabelShortForwardCHLI_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortForwardCHLI = _RcServiceFarEndPointCosLabelShortForwardCHLI_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 17),
    _RcServiceFarEndPointCosLabelShortForwardCHLI_Type()
)
rcServiceFarEndPointCosLabelShortForwardCHLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortForwardCHLI.setStatus("current")
_RcServiceFarEndPointCosLabelShortBackwardCHLI_Type = Unsigned32
_RcServiceFarEndPointCosLabelShortBackwardCHLI_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortBackwardCHLI = _RcServiceFarEndPointCosLabelShortBackwardCHLI_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 18),
    _RcServiceFarEndPointCosLabelShortBackwardCHLI_Type()
)
rcServiceFarEndPointCosLabelShortBackwardCHLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortBackwardCHLI.setStatus("current")
_RcServiceFarEndPointCosLabelShortForwardFrameLost_Type = Unsigned32
_RcServiceFarEndPointCosLabelShortForwardFrameLost_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortForwardFrameLost = _RcServiceFarEndPointCosLabelShortForwardFrameLost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 19),
    _RcServiceFarEndPointCosLabelShortForwardFrameLost_Type()
)
rcServiceFarEndPointCosLabelShortForwardFrameLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortForwardFrameLost.setStatus("current")
_RcServiceFarEndPointCosLabelShortBackwardFrameLost_Type = Unsigned32
_RcServiceFarEndPointCosLabelShortBackwardFrameLost_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortBackwardFrameLost = _RcServiceFarEndPointCosLabelShortBackwardFrameLost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 20),
    _RcServiceFarEndPointCosLabelShortBackwardFrameLost_Type()
)
rcServiceFarEndPointCosLabelShortBackwardFrameLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortBackwardFrameLost.setStatus("current")
_RcServiceFarEndPointCosLabelShortForwardUnAvailSeconds_Type = Unsigned32
_RcServiceFarEndPointCosLabelShortForwardUnAvailSeconds_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortForwardUnAvailSeconds = _RcServiceFarEndPointCosLabelShortForwardUnAvailSeconds_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 21),
    _RcServiceFarEndPointCosLabelShortForwardUnAvailSeconds_Type()
)
rcServiceFarEndPointCosLabelShortForwardUnAvailSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortForwardUnAvailSeconds.setStatus("current")
_RcServiceFarEndPointCosLabelShortBackwardUnAvailSeconds_Type = Unsigned32
_RcServiceFarEndPointCosLabelShortBackwardUnAvailSeconds_Object = MibTableColumn
rcServiceFarEndPointCosLabelShortBackwardUnAvailSeconds = _RcServiceFarEndPointCosLabelShortBackwardUnAvailSeconds_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 22),
    _RcServiceFarEndPointCosLabelShortBackwardUnAvailSeconds_Type()
)
rcServiceFarEndPointCosLabelShortBackwardUnAvailSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelShortBackwardUnAvailSeconds.setStatus("current")
_RcServiceFarEndPointCosLabelLongStartTime_Type = DateAndTime
_RcServiceFarEndPointCosLabelLongStartTime_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongStartTime = _RcServiceFarEndPointCosLabelLongStartTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 23),
    _RcServiceFarEndPointCosLabelLongStartTime_Type()
)
rcServiceFarEndPointCosLabelLongStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongStartTime.setStatus("current")
_RcServiceFarEndPointCosLabelLongTwowayFD_Type = Unsigned32
_RcServiceFarEndPointCosLabelLongTwowayFD_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongTwowayFD = _RcServiceFarEndPointCosLabelLongTwowayFD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 24),
    _RcServiceFarEndPointCosLabelLongTwowayFD_Type()
)
rcServiceFarEndPointCosLabelLongTwowayFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongTwowayFD.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongTwowayFD.setUnits("microseconds")
_RcServiceFarEndPointCosLabelLongTwowayMaxFD_Type = Unsigned32
_RcServiceFarEndPointCosLabelLongTwowayMaxFD_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongTwowayMaxFD = _RcServiceFarEndPointCosLabelLongTwowayMaxFD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 25),
    _RcServiceFarEndPointCosLabelLongTwowayMaxFD_Type()
)
rcServiceFarEndPointCosLabelLongTwowayMaxFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongTwowayMaxFD.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongTwowayMaxFD.setUnits("microseconds")
_RcServiceFarEndPointCosLabelLongTwowayMinFD_Type = Unsigned32
_RcServiceFarEndPointCosLabelLongTwowayMinFD_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongTwowayMinFD = _RcServiceFarEndPointCosLabelLongTwowayMinFD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 26),
    _RcServiceFarEndPointCosLabelLongTwowayMinFD_Type()
)
rcServiceFarEndPointCosLabelLongTwowayMinFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongTwowayMinFD.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongTwowayMinFD.setUnits("microseconds")
_RcServiceFarEndPointCosLabelSlaConfigDMOperId_Type = Unsigned32
_RcServiceFarEndPointCosLabelSlaConfigDMOperId_Object = MibTableColumn
rcServiceFarEndPointCosLabelSlaConfigDMOperId = _RcServiceFarEndPointCosLabelSlaConfigDMOperId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 27),
    _RcServiceFarEndPointCosLabelSlaConfigDMOperId_Type()
)
rcServiceFarEndPointCosLabelSlaConfigDMOperId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelSlaConfigDMOperId.setStatus("current")
_RcServiceFarEndPointCosLabelSlaConfigLMOperId_Type = Unsigned32
_RcServiceFarEndPointCosLabelSlaConfigLMOperId_Object = MibTableColumn
rcServiceFarEndPointCosLabelSlaConfigLMOperId = _RcServiceFarEndPointCosLabelSlaConfigLMOperId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 28),
    _RcServiceFarEndPointCosLabelSlaConfigLMOperId_Type()
)
rcServiceFarEndPointCosLabelSlaConfigLMOperId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelSlaConfigLMOperId.setStatus("current")
_RcServiceFarEndPointCosLabelEtherSamServiceIndex_Type = Integer32
_RcServiceFarEndPointCosLabelEtherSamServiceIndex_Object = MibTableColumn
rcServiceFarEndPointCosLabelEtherSamServiceIndex = _RcServiceFarEndPointCosLabelEtherSamServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 29),
    _RcServiceFarEndPointCosLabelEtherSamServiceIndex_Type()
)
rcServiceFarEndPointCosLabelEtherSamServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelEtherSamServiceIndex.setStatus("current")
_RcServiceFarEndPointCosLabelLongTwowayMFD_Type = Unsigned32
_RcServiceFarEndPointCosLabelLongTwowayMFD_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongTwowayMFD = _RcServiceFarEndPointCosLabelLongTwowayMFD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 30),
    _RcServiceFarEndPointCosLabelLongTwowayMFD_Type()
)
rcServiceFarEndPointCosLabelLongTwowayMFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongTwowayMFD.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongTwowayMFD.setUnits("microseconds")
_RcServiceFarEndPointCosLabelLongTwowayFDR_Type = Unsigned32
_RcServiceFarEndPointCosLabelLongTwowayFDR_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongTwowayFDR = _RcServiceFarEndPointCosLabelLongTwowayFDR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 31),
    _RcServiceFarEndPointCosLabelLongTwowayFDR_Type()
)
rcServiceFarEndPointCosLabelLongTwowayFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongTwowayFDR.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongTwowayFDR.setUnits("microseconds")
_RcServiceFarEndPointCosLabelLongTwowayIFDV_Type = Unsigned32
_RcServiceFarEndPointCosLabelLongTwowayIFDV_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongTwowayIFDV = _RcServiceFarEndPointCosLabelLongTwowayIFDV_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 32),
    _RcServiceFarEndPointCosLabelLongTwowayIFDV_Type()
)
rcServiceFarEndPointCosLabelLongTwowayIFDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongTwowayIFDV.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongTwowayIFDV.setUnits("microseconds")
_RcServiceFarEndPointCosLabelLongTwowayMaxIFDV_Type = Unsigned32
_RcServiceFarEndPointCosLabelLongTwowayMaxIFDV_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongTwowayMaxIFDV = _RcServiceFarEndPointCosLabelLongTwowayMaxIFDV_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 33),
    _RcServiceFarEndPointCosLabelLongTwowayMaxIFDV_Type()
)
rcServiceFarEndPointCosLabelLongTwowayMaxIFDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongTwowayMaxIFDV.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongTwowayMaxIFDV.setUnits("microseconds")
_RcServiceFarEndPointCosLabelLongTwowayMinIFDV_Type = Unsigned32
_RcServiceFarEndPointCosLabelLongTwowayMinIFDV_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongTwowayMinIFDV = _RcServiceFarEndPointCosLabelLongTwowayMinIFDV_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 34),
    _RcServiceFarEndPointCosLabelLongTwowayMinIFDV_Type()
)
rcServiceFarEndPointCosLabelLongTwowayMinIFDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongTwowayMinIFDV.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongTwowayMinIFDV.setUnits("microseconds")
_RcServiceFarEndPointCosLabelLongTwowayMIFDV_Type = Unsigned32
_RcServiceFarEndPointCosLabelLongTwowayMIFDV_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongTwowayMIFDV = _RcServiceFarEndPointCosLabelLongTwowayMIFDV_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 35),
    _RcServiceFarEndPointCosLabelLongTwowayMIFDV_Type()
)
rcServiceFarEndPointCosLabelLongTwowayMIFDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongTwowayMIFDV.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongTwowayMIFDV.setUnits("microseconds")


class _RcServiceFarEndPointCosLabelLongForwardFLR_Type(Unsigned32):
    """Custom type rcServiceFarEndPointCosLabelLongForwardFLR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcServiceFarEndPointCosLabelLongForwardFLR_Type.__name__ = "Unsigned32"
_RcServiceFarEndPointCosLabelLongForwardFLR_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongForwardFLR = _RcServiceFarEndPointCosLabelLongForwardFLR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 36),
    _RcServiceFarEndPointCosLabelLongForwardFLR_Type()
)
rcServiceFarEndPointCosLabelLongForwardFLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongForwardFLR.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongForwardFLR.setUnits("milli-percent")


class _RcServiceFarEndPointCosLabelLongBackwardFLR_Type(Unsigned32):
    """Custom type rcServiceFarEndPointCosLabelLongBackwardFLR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcServiceFarEndPointCosLabelLongBackwardFLR_Type.__name__ = "Unsigned32"
_RcServiceFarEndPointCosLabelLongBackwardFLR_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongBackwardFLR = _RcServiceFarEndPointCosLabelLongBackwardFLR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 37),
    _RcServiceFarEndPointCosLabelLongBackwardFLR_Type()
)
rcServiceFarEndPointCosLabelLongBackwardFLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongBackwardFLR.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongBackwardFLR.setUnits("milli-percent")


class _RcServiceFarEndPointCosLabelLongForwardAvail_Type(Unsigned32):
    """Custom type rcServiceFarEndPointCosLabelLongForwardAvail based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcServiceFarEndPointCosLabelLongForwardAvail_Type.__name__ = "Unsigned32"
_RcServiceFarEndPointCosLabelLongForwardAvail_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongForwardAvail = _RcServiceFarEndPointCosLabelLongForwardAvail_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 38),
    _RcServiceFarEndPointCosLabelLongForwardAvail_Type()
)
rcServiceFarEndPointCosLabelLongForwardAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongForwardAvail.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongForwardAvail.setUnits("milli-percent")


class _RcServiceFarEndPointCosLabelLongBackwardAvail_Type(Unsigned32):
    """Custom type rcServiceFarEndPointCosLabelLongBackwardAvail based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcServiceFarEndPointCosLabelLongBackwardAvail_Type.__name__ = "Unsigned32"
_RcServiceFarEndPointCosLabelLongBackwardAvail_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongBackwardAvail = _RcServiceFarEndPointCosLabelLongBackwardAvail_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 39),
    _RcServiceFarEndPointCosLabelLongBackwardAvail_Type()
)
rcServiceFarEndPointCosLabelLongBackwardAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongBackwardAvail.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongBackwardAvail.setUnits("milli-percent")
_RcServiceFarEndPointCosLabelLongForwardHLI_Type = Unsigned32
_RcServiceFarEndPointCosLabelLongForwardHLI_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongForwardHLI = _RcServiceFarEndPointCosLabelLongForwardHLI_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 40),
    _RcServiceFarEndPointCosLabelLongForwardHLI_Type()
)
rcServiceFarEndPointCosLabelLongForwardHLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongForwardHLI.setStatus("current")
_RcServiceFarEndPointCosLabelLongBackwardHLI_Type = Unsigned32
_RcServiceFarEndPointCosLabelLongBackwardHLI_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongBackwardHLI = _RcServiceFarEndPointCosLabelLongBackwardHLI_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 41),
    _RcServiceFarEndPointCosLabelLongBackwardHLI_Type()
)
rcServiceFarEndPointCosLabelLongBackwardHLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongBackwardHLI.setStatus("current")
_RcServiceFarEndPointCosLabelLongForwardCHLI_Type = Unsigned32
_RcServiceFarEndPointCosLabelLongForwardCHLI_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongForwardCHLI = _RcServiceFarEndPointCosLabelLongForwardCHLI_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 42),
    _RcServiceFarEndPointCosLabelLongForwardCHLI_Type()
)
rcServiceFarEndPointCosLabelLongForwardCHLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongForwardCHLI.setStatus("current")
_RcServiceFarEndPointCosLabelLongBackwardCHLI_Type = Unsigned32
_RcServiceFarEndPointCosLabelLongBackwardCHLI_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongBackwardCHLI = _RcServiceFarEndPointCosLabelLongBackwardCHLI_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 43),
    _RcServiceFarEndPointCosLabelLongBackwardCHLI_Type()
)
rcServiceFarEndPointCosLabelLongBackwardCHLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongBackwardCHLI.setStatus("current")
_RcServiceFarEndPointCosLabelLongForwardFrameLost_Type = Unsigned32
_RcServiceFarEndPointCosLabelLongForwardFrameLost_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongForwardFrameLost = _RcServiceFarEndPointCosLabelLongForwardFrameLost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 44),
    _RcServiceFarEndPointCosLabelLongForwardFrameLost_Type()
)
rcServiceFarEndPointCosLabelLongForwardFrameLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongForwardFrameLost.setStatus("current")
_RcServiceFarEndPointCosLabelLongBackwardFrameLost_Type = Unsigned32
_RcServiceFarEndPointCosLabelLongBackwardFrameLost_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongBackwardFrameLost = _RcServiceFarEndPointCosLabelLongBackwardFrameLost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 45),
    _RcServiceFarEndPointCosLabelLongBackwardFrameLost_Type()
)
rcServiceFarEndPointCosLabelLongBackwardFrameLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongBackwardFrameLost.setStatus("current")
_RcServiceFarEndPointCosLabelLongForwardUnAvailSeconds_Type = Unsigned32
_RcServiceFarEndPointCosLabelLongForwardUnAvailSeconds_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongForwardUnAvailSeconds = _RcServiceFarEndPointCosLabelLongForwardUnAvailSeconds_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 46),
    _RcServiceFarEndPointCosLabelLongForwardUnAvailSeconds_Type()
)
rcServiceFarEndPointCosLabelLongForwardUnAvailSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongForwardUnAvailSeconds.setStatus("current")
_RcServiceFarEndPointCosLabelLongBackwardUnAvailSeconds_Type = Unsigned32
_RcServiceFarEndPointCosLabelLongBackwardUnAvailSeconds_Object = MibTableColumn
rcServiceFarEndPointCosLabelLongBackwardUnAvailSeconds = _RcServiceFarEndPointCosLabelLongBackwardUnAvailSeconds_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 11, 1, 47),
    _RcServiceFarEndPointCosLabelLongBackwardUnAvailSeconds_Type()
)
rcServiceFarEndPointCosLabelLongBackwardUnAvailSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelLongBackwardUnAvailSeconds.setStatus("current")
_RcServiceSdpTable_Object = MibTable
rcServiceSdpTable = _RcServiceSdpTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 12)
)
if mibBuilder.loadTexts:
    rcServiceSdpTable.setStatus("current")
_RcServiceSdpEntry_Object = MibTableRow
rcServiceSdpEntry = _RcServiceSdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 12, 1)
)
rcServiceSdpEntry.setIndexNames(
    (0, "SWTICH-SERVICE-MIB", "rcServiceID"),
    (0, "SWTICH-SERVICE-MIB", "rcServiceNetworkInterfacePortIndex"),
)
if mibBuilder.loadTexts:
    rcServiceSdpEntry.setStatus("current")
_RcServiceSdpRowStatus_Type = RowStatus
_RcServiceSdpRowStatus_Object = MibTableColumn
rcServiceSdpRowStatus = _RcServiceSdpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 12, 1, 100),
    _RcServiceSdpRowStatus_Type()
)
rcServiceSdpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcServiceSdpRowStatus.setStatus("current")
_RcServiceFarEndPointCosLabelCurrentTable_Object = MibTable
rcServiceFarEndPointCosLabelCurrentTable = _RcServiceFarEndPointCosLabelCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 13)
)
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelCurrentTable.setStatus("current")
_RcServiceFarEndPointCosLabelCurrentEntry_Object = MibTableRow
rcServiceFarEndPointCosLabelCurrentEntry = _RcServiceFarEndPointCosLabelCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 13, 1)
)
rcServiceFarEndPointCosLabelCurrentEntry.setIndexNames(
    (0, "SWTICH-SERVICE-MIB", "rcServiceID"),
    (0, "SWTICH-SERVICE-MIB", "rcServiceNetworkInterfaceID"),
    (0, "SWTICH-SERVICE-MIB", "rcServiceFarEndNetworkInterfaceID"),
    (0, "SWTICH-SERVICE-MIB", "rcServiceCosLabel"),
)
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelCurrentEntry.setStatus("current")
_RcServiceFarEndPointCosLabelCurrentTwowayFD_Type = Unsigned32
_RcServiceFarEndPointCosLabelCurrentTwowayFD_Object = MibTableColumn
rcServiceFarEndPointCosLabelCurrentTwowayFD = _RcServiceFarEndPointCosLabelCurrentTwowayFD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 13, 1, 1),
    _RcServiceFarEndPointCosLabelCurrentTwowayFD_Type()
)
rcServiceFarEndPointCosLabelCurrentTwowayFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelCurrentTwowayFD.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelCurrentTwowayFD.setUnits("microseconds")
_RcServiceFarEndPointCosLabelCurrentTwowayIFDV_Type = Unsigned32
_RcServiceFarEndPointCosLabelCurrentTwowayIFDV_Object = MibTableColumn
rcServiceFarEndPointCosLabelCurrentTwowayIFDV = _RcServiceFarEndPointCosLabelCurrentTwowayIFDV_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 13, 1, 2),
    _RcServiceFarEndPointCosLabelCurrentTwowayIFDV_Type()
)
rcServiceFarEndPointCosLabelCurrentTwowayIFDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelCurrentTwowayIFDV.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelCurrentTwowayIFDV.setUnits("microseconds")


class _RcServiceFarEndPointCosLabelCurrentForwardFLR_Type(Unsigned32):
    """Custom type rcServiceFarEndPointCosLabelCurrentForwardFLR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcServiceFarEndPointCosLabelCurrentForwardFLR_Type.__name__ = "Unsigned32"
_RcServiceFarEndPointCosLabelCurrentForwardFLR_Object = MibTableColumn
rcServiceFarEndPointCosLabelCurrentForwardFLR = _RcServiceFarEndPointCosLabelCurrentForwardFLR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 13, 1, 3),
    _RcServiceFarEndPointCosLabelCurrentForwardFLR_Type()
)
rcServiceFarEndPointCosLabelCurrentForwardFLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelCurrentForwardFLR.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelCurrentForwardFLR.setUnits("milli-percent")


class _RcServiceFarEndPointCosLabelCurrentBackwardFLR_Type(Unsigned32):
    """Custom type rcServiceFarEndPointCosLabelCurrentBackwardFLR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcServiceFarEndPointCosLabelCurrentBackwardFLR_Type.__name__ = "Unsigned32"
_RcServiceFarEndPointCosLabelCurrentBackwardFLR_Object = MibTableColumn
rcServiceFarEndPointCosLabelCurrentBackwardFLR = _RcServiceFarEndPointCosLabelCurrentBackwardFLR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 13, 1, 4),
    _RcServiceFarEndPointCosLabelCurrentBackwardFLR_Type()
)
rcServiceFarEndPointCosLabelCurrentBackwardFLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelCurrentBackwardFLR.setStatus("current")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelCurrentBackwardFLR.setUnits("milli-percent")
_RcServiceFarEndPointCosLabelCurrentForwardFrameLost_Type = Unsigned32
_RcServiceFarEndPointCosLabelCurrentForwardFrameLost_Object = MibTableColumn
rcServiceFarEndPointCosLabelCurrentForwardFrameLost = _RcServiceFarEndPointCosLabelCurrentForwardFrameLost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 13, 1, 5),
    _RcServiceFarEndPointCosLabelCurrentForwardFrameLost_Type()
)
rcServiceFarEndPointCosLabelCurrentForwardFrameLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelCurrentForwardFrameLost.setStatus("current")
_RcServiceFarEndPointCosLabelCurrentBackwardFrameLost_Type = Unsigned32
_RcServiceFarEndPointCosLabelCurrentBackwardFrameLost_Object = MibTableColumn
rcServiceFarEndPointCosLabelCurrentBackwardFrameLost = _RcServiceFarEndPointCosLabelCurrentBackwardFrameLost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 13, 1, 6),
    _RcServiceFarEndPointCosLabelCurrentBackwardFrameLost_Type()
)
rcServiceFarEndPointCosLabelCurrentBackwardFrameLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelCurrentBackwardFrameLost.setStatus("current")


class _RcServiceFarEndPointCosLabelCurrentForwardAvailStatus_Type(Integer32):
    """Custom type rcServiceFarEndPointCosLabelCurrentForwardAvailStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2),
          ("unknown", 3))
    )


_RcServiceFarEndPointCosLabelCurrentForwardAvailStatus_Type.__name__ = "Integer32"
_RcServiceFarEndPointCosLabelCurrentForwardAvailStatus_Object = MibTableColumn
rcServiceFarEndPointCosLabelCurrentForwardAvailStatus = _RcServiceFarEndPointCosLabelCurrentForwardAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 13, 1, 7),
    _RcServiceFarEndPointCosLabelCurrentForwardAvailStatus_Type()
)
rcServiceFarEndPointCosLabelCurrentForwardAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelCurrentForwardAvailStatus.setStatus("current")


class _RcServiceFarEndPointCosLabelCurrentBackwardAvailStatus_Type(Integer32):
    """Custom type rcServiceFarEndPointCosLabelCurrentBackwardAvailStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2),
          ("unknown", 3))
    )


_RcServiceFarEndPointCosLabelCurrentBackwardAvailStatus_Type.__name__ = "Integer32"
_RcServiceFarEndPointCosLabelCurrentBackwardAvailStatus_Object = MibTableColumn
rcServiceFarEndPointCosLabelCurrentBackwardAvailStatus = _RcServiceFarEndPointCosLabelCurrentBackwardAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 13, 1, 8),
    _RcServiceFarEndPointCosLabelCurrentBackwardAvailStatus_Type()
)
rcServiceFarEndPointCosLabelCurrentBackwardAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcServiceFarEndPointCosLabelCurrentBackwardAvailStatus.setStatus("current")
_RcServiceTrapGroup_ObjectIdentity = ObjectIdentity
rcServiceTrapGroup = _RcServiceTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 14)
)

# Managed Objects groups


# Notification objects

rcServiceEtherSamCfgTestFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 14, 1)
)
rcServiceEtherSamCfgTestFailTrap.setObjects(
      *(("SWTICH-SERVICE-MIB", "rcServiceID"),
        ("SWTICH-SERVICE-MIB", "rcServiceNetworkInterfaceID"),
        ("SWTICH-SERVICE-MIB", "rcServiceFarEndNetworkInterfaceID"))
)
if mibBuilder.loadTexts:
    rcServiceEtherSamCfgTestFailTrap.setStatus(
        "current"
    )

rcServiceEtherSamCfgTestSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 14, 2)
)
rcServiceEtherSamCfgTestSuccessTrap.setObjects(
      *(("SWTICH-SERVICE-MIB", "rcServiceID"),
        ("SWTICH-SERVICE-MIB", "rcServiceNetworkInterfaceID"),
        ("SWTICH-SERVICE-MIB", "rcServiceFarEndNetworkInterfaceID"))
)
if mibBuilder.loadTexts:
    rcServiceEtherSamCfgTestSuccessTrap.setStatus(
        "current"
    )

rcServiceEtherSamPfmTestFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 14, 3)
)
rcServiceEtherSamPfmTestFailTrap.setObjects(
      *(("SWTICH-SERVICE-MIB", "rcServiceID"),
        ("SWTICH-SERVICE-MIB", "rcServiceNetworkInterfaceID"),
        ("SWTICH-SERVICE-MIB", "rcServiceFarEndNetworkInterfaceID"))
)
if mibBuilder.loadTexts:
    rcServiceEtherSamPfmTestFailTrap.setStatus(
        "current"
    )

rcServiceEtherSamPfmTestSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 75, 14, 4)
)
rcServiceEtherSamPfmTestSuccessTrap.setObjects(
      *(("SWTICH-SERVICE-MIB", "rcServiceID"),
        ("SWTICH-SERVICE-MIB", "rcServiceNetworkInterfaceID"),
        ("SWTICH-SERVICE-MIB", "rcServiceFarEndNetworkInterfaceID"))
)
if mibBuilder.loadTexts:
    rcServiceEtherSamPfmTestSuccessTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWTICH-SERVICE-MIB",
    **{"rcService": rcService,
       "rcServiceScalar": rcServiceScalar,
       "rcServiceDefaultSdp1PortIndex": rcServiceDefaultSdp1PortIndex,
       "rcServiceDefaultSdp2PortIndex": rcServiceDefaultSdp2PortIndex,
       "rcServiceEtherSamTrapEnable": rcServiceEtherSamTrapEnable,
       "rcServiceCosLabelNameTable": rcServiceCosLabelNameTable,
       "rcServiceCosLabelNameEntry": rcServiceCosLabelNameEntry,
       "rcServiceCosLabel": rcServiceCosLabel,
       "rcServiceCosLabelName": rcServiceCosLabelName,
       "rcServiceNetworkInterfaceTable": rcServiceNetworkInterfaceTable,
       "rcServiceNetworkInterfaceEntry": rcServiceNetworkInterfaceEntry,
       "rcServiceNetworkInterfacePortIndex": rcServiceNetworkInterfacePortIndex,
       "rcServiceNetworkInterfaceType": rcServiceNetworkInterfaceType,
       "rcServiceNetworkInterfaceID": rcServiceNetworkInterfaceID,
       "rcServiceNetworkInterfacePhysicalMedium": rcServiceNetworkInterfacePhysicalMedium,
       "rcServiceNetworkInterfaceSpeed": rcServiceNetworkInterfaceSpeed,
       "rcServiceNetworkInterfaceDuplexMode": rcServiceNetworkInterfaceDuplexMode,
       "rcServiceNetworkInterfaceMacLayer": rcServiceNetworkInterfaceMacLayer,
       "rcServiceNetworkInterfaceMtu": rcServiceNetworkInterfaceMtu,
       "rcServiceNetworkInterfaceServiceMultiplexing": rcServiceNetworkInterfaceServiceMultiplexing,
       "rcServiceNetworkInterfaceBundling": rcServiceNetworkInterfaceBundling,
       "rcServiceNetworkInterfaceAllToOneBundling": rcServiceNetworkInterfaceAllToOneBundling,
       "rcServiceNetworkInterfaceDefaultCVlan": rcServiceNetworkInterfaceDefaultCVlan,
       "rcServiceNetworkInterfacMaxEvcs": rcServiceNetworkInterfacMaxEvcs,
       "rcServiceNetworkInterfaceMaxOvcs": rcServiceNetworkInterfaceMaxOvcs,
       "rcServiceNetworkInterfaceInBwProfileIndex": rcServiceNetworkInterfaceInBwProfileIndex,
       "rcServiceNetworkInterfaceOutBwProfileIndex": rcServiceNetworkInterfaceOutBwProfileIndex,
       "rcServiceNetworkInterfaceL2cpProfileIndex": rcServiceNetworkInterfaceL2cpProfileIndex,
       "rcServiceNetworkInterfaceFrameFormat": rcServiceNetworkInterfaceFrameFormat,
       "rcServiceNetworkInterfaceLinks": rcServiceNetworkInterfaceLinks,
       "rcServiceNetworkInterfaceResiliencyMechanisms": rcServiceNetworkInterfaceResiliencyMechanisms,
       "rcServiceNetworkInterfaceMaxEndPointPerOvc": rcServiceNetworkInterfaceMaxEndPointPerOvc,
       "rcServiceNetworkInterfaceEndPointMapTable": rcServiceNetworkInterfaceEndPointMapTable,
       "rcServiceNetworkInterfaceEndPointMapEntry": rcServiceNetworkInterfaceEndPointMapEntry,
       "rcServiceNetworkInterfaceEndPointMapSVlan": rcServiceNetworkInterfaceEndPointMapSVlan,
       "rcServiceNetworkInterfaceEndPointMapEndPointID": rcServiceNetworkInterfaceEndPointMapEndPointID,
       "rcServiceNetworkInterfaceEndPointMapEndPointType": rcServiceNetworkInterfaceEndPointMapEndPointType,
       "rcServiceTable": rcServiceTable,
       "rcServiceEntry": rcServiceEntry,
       "rcServiceID": rcServiceID,
       "rcServiceType": rcServiceType,
       "rcServiceCustomerNameID": rcServiceCustomerNameID,
       "rcServiceMaxUnis": rcServiceMaxUnis,
       "rcServiceMaxEnnis": rcServiceMaxEnnis,
       "rcServiceMTU": rcServiceMTU,
       "rcServiceCVlanPreservation": rcServiceCVlanPreservation,
       "rcServiceCCosPreservation": rcServiceCCosPreservation,
       "rcServiceSVlanPreservation": rcServiceSVlanPreservation,
       "rcServiceSCosPreservation": rcServiceSCosPreservation,
       "rcServiceColorForward": rcServiceColorForward,
       "rcServiceUnicastDelivery": rcServiceUnicastDelivery,
       "rcServiceMulticastDelivery": rcServiceMulticastDelivery,
       "rcServiceBroadcastDelivery": rcServiceBroadcastDelivery,
       "rcServiceL2cpPass": rcServiceL2cpPass,
       "rcServiceCosType": rcServiceCosType,
       "rcServiceVCCosLabel": rcServiceVCCosLabel,
       "rcServiceCosMapProfileIndex": rcServiceCosMapProfileIndex,
       "rcServiceDscpMapProfileIndex": rcServiceDscpMapProfileIndex,
       "rcServiceSdpType": rcServiceSdpType,
       "rcServiceSdpIndex": rcServiceSdpIndex,
       "rcServicePTIndex": rcServicePTIndex,
       "rcServiceMaintenanceTimeStart": rcServiceMaintenanceTimeStart,
       "rcServiceMaintenanceTimeStop": rcServiceMaintenanceTimeStop,
       "rcServicePerfermanceTestScheduleLife": rcServicePerfermanceTestScheduleLife,
       "rcServicePerfermanceTestSchedulePeriod": rcServicePerfermanceTestSchedulePeriod,
       "rcServicePerfermanceTestScheduleInterval": rcServicePerfermanceTestScheduleInterval,
       "rcServicePerfermanceTestOperate": rcServicePerfermanceTestOperate,
       "rcServiceL2LoopbackEtherType": rcServiceL2LoopbackEtherType,
       "rcServiceL2LoopbackOperate": rcServiceL2LoopbackOperate,
       "rcServiceEtherSamPerformanceDuration": rcServiceEtherSamPerformanceDuration,
       "rcServiceEtherSamPerformanceBW": rcServiceEtherSamPerformanceBW,
       "rcServiceEtherSamFlowProfileIndex": rcServiceEtherSamFlowProfileIndex,
       "rcServiceEtherSamCfgBypassUni": rcServiceEtherSamCfgBypassUni,
       "rcServiceEtherSamTestElapsedTime": rcServiceEtherSamTestElapsedTime,
       "rcServiceEtherSamTestType": rcServiceEtherSamTestType,
       "rcServiceEtherSamOperate": rcServiceEtherSamOperate,
       "rcServiceEtherSamTestResult": rcServiceEtherSamTestResult,
       "rcServiceEtherSamTimeCfgWillTake": rcServiceEtherSamTimeCfgWillTake,
       "rcServiceEtherSamClearResult": rcServiceEtherSamClearResult,
       "rcServiceMdIndex": rcServiceMdIndex,
       "rcServiceMaIndex": rcServiceMaIndex,
       "rcServiceOperStatus": rcServiceOperStatus,
       "rcServiceCcStatus": rcServiceCcStatus,
       "rcServicePerfermanceTestType": rcServicePerfermanceTestType,
       "rcServiceEtherSamSlaJitterType": rcServiceEtherSamSlaJitterType,
       "rcServiceRowStatus": rcServiceRowStatus,
       "rcServiceCustomerTable": rcServiceCustomerTable,
       "rcServiceCustomerEntry": rcServiceCustomerEntry,
       "rcServiceCustomerName": rcServiceCustomerName,
       "rcServiceCustomerContact": rcServiceCustomerContact,
       "rcServiceCustomerPhone": rcServiceCustomerPhone,
       "rcServiceCustomerRowStatus": rcServiceCustomerRowStatus,
       "rcServiceCosLabelTable": rcServiceCosLabelTable,
       "rcServiceCosLabelEntry": rcServiceCosLabelEntry,
       "rcServiceCosLabelPerfermanceTestEnable": rcServiceCosLabelPerfermanceTestEnable,
       "rcServiceCosLabelEtherSAMEnable": rcServiceCosLabelEtherSAMEnable,
       "rcServiceEndPointTable": rcServiceEndPointTable,
       "rcServiceEndPointEntry": rcServiceEndPointEntry,
       "rcServiceEndPointType": rcServiceEndPointType,
       "rcServiceEndPointMPType": rcServiceEndPointMPType,
       "rcServiceEndPointMapCVlans": rcServiceEndPointMapCVlans,
       "rcServiceEndPointInBwProfileIndex": rcServiceEndPointInBwProfileIndex,
       "rcServiceEndPointOutBwProfileIndex": rcServiceEndPointOutBwProfileIndex,
       "rcServiceEndPointLMep": rcServiceEndPointLMep,
       "rcServiceEndPointCCEnable": rcServiceEndPointCCEnable,
       "rcServiceEndPointPMEnable": rcServiceEndPointPMEnable,
       "rcServiceEndPointRowStatus": rcServiceEndPointRowStatus,
       "rcServicesEndPointCosLabelTable": rcServicesEndPointCosLabelTable,
       "rcServicesEndPointCosLabelEntry": rcServicesEndPointCosLabelEntry,
       "rcServiceEndPointCosLabelInBwProfileIndex": rcServiceEndPointCosLabelInBwProfileIndex,
       "rcServiceEndPointCosLabelOutBwProfileIndex": rcServiceEndPointCosLabelOutBwProfileIndex,
       "rcServiceFarEndPointTable": rcServiceFarEndPointTable,
       "rcServiceFarEndPointEntry": rcServiceFarEndPointEntry,
       "rcServiceFarEndNetworkInterfaceID": rcServiceFarEndNetworkInterfaceID,
       "rcServiceFarEndPointRMep": rcServiceFarEndPointRMep,
       "rcServiceFarEndPointPerfermanceTestEnable": rcServiceFarEndPointPerfermanceTestEnable,
       "rcServiceFarEndPointEtherSAMEnable": rcServiceFarEndPointEtherSAMEnable,
       "rcServiceFarEndPointL2LoopbackEnable": rcServiceFarEndPointL2LoopbackEnable,
       "rcServiceFarEndPointCcStatus": rcServiceFarEndPointCcStatus,
       "rcServiceFarEndPointIPAddressType": rcServiceFarEndPointIPAddressType,
       "rcServiceFarEndPointIPAddress": rcServiceFarEndPointIPAddress,
       "rcServiceFarEndPointMacAddress": rcServiceFarEndPointMacAddress,
       "rcServiceFarEndPointType": rcServiceFarEndPointType,
       "rcServiceFarEndPointRowStatus": rcServiceFarEndPointRowStatus,
       "rcServiceFarEndPointCosLabelTable": rcServiceFarEndPointCosLabelTable,
       "rcServiceFarEndPointCosLabelEntry": rcServiceFarEndPointCosLabelEntry,
       "rcServiceFarEndPointCosLabelShortStartTime": rcServiceFarEndPointCosLabelShortStartTime,
       "rcServiceFarEndPointCosLabelShortTwowayFD": rcServiceFarEndPointCosLabelShortTwowayFD,
       "rcServiceFarEndPointCosLabelShortTwowayMaxFD": rcServiceFarEndPointCosLabelShortTwowayMaxFD,
       "rcServiceFarEndPointCosLabelShortTwowayMinFD": rcServiceFarEndPointCosLabelShortTwowayMinFD,
       "rcServiceFarEndPointCosLabelShortTwowayMFD": rcServiceFarEndPointCosLabelShortTwowayMFD,
       "rcServiceFarEndPointCosLabelShortTwowayFDR": rcServiceFarEndPointCosLabelShortTwowayFDR,
       "rcServiceFarEndPointCosLabelShortTwowayIFDV": rcServiceFarEndPointCosLabelShortTwowayIFDV,
       "rcServiceFarEndPointCosLabelShortTwowayMaxIFDV": rcServiceFarEndPointCosLabelShortTwowayMaxIFDV,
       "rcServiceFarEndPointCosLabelShortTwowayMinIFDV": rcServiceFarEndPointCosLabelShortTwowayMinIFDV,
       "rcServiceFarEndPointCosLabelShortTwowayMIFDV": rcServiceFarEndPointCosLabelShortTwowayMIFDV,
       "rcServiceFarEndPointCosLabelShortForwardFLR": rcServiceFarEndPointCosLabelShortForwardFLR,
       "rcServiceFarEndPointCosLabelShortBackwardFLR": rcServiceFarEndPointCosLabelShortBackwardFLR,
       "rcServiceFarEndPointCosLabelShortForwardAvail": rcServiceFarEndPointCosLabelShortForwardAvail,
       "rcServiceFarEndPointCosLabelShortBackwardAvail": rcServiceFarEndPointCosLabelShortBackwardAvail,
       "rcServiceFarEndPointCosLabelShortForwardHLI": rcServiceFarEndPointCosLabelShortForwardHLI,
       "rcServiceFarEndPointCosLabelShortBackwardHLI": rcServiceFarEndPointCosLabelShortBackwardHLI,
       "rcServiceFarEndPointCosLabelShortForwardCHLI": rcServiceFarEndPointCosLabelShortForwardCHLI,
       "rcServiceFarEndPointCosLabelShortBackwardCHLI": rcServiceFarEndPointCosLabelShortBackwardCHLI,
       "rcServiceFarEndPointCosLabelShortForwardFrameLost": rcServiceFarEndPointCosLabelShortForwardFrameLost,
       "rcServiceFarEndPointCosLabelShortBackwardFrameLost": rcServiceFarEndPointCosLabelShortBackwardFrameLost,
       "rcServiceFarEndPointCosLabelShortForwardUnAvailSeconds": rcServiceFarEndPointCosLabelShortForwardUnAvailSeconds,
       "rcServiceFarEndPointCosLabelShortBackwardUnAvailSeconds": rcServiceFarEndPointCosLabelShortBackwardUnAvailSeconds,
       "rcServiceFarEndPointCosLabelLongStartTime": rcServiceFarEndPointCosLabelLongStartTime,
       "rcServiceFarEndPointCosLabelLongTwowayFD": rcServiceFarEndPointCosLabelLongTwowayFD,
       "rcServiceFarEndPointCosLabelLongTwowayMaxFD": rcServiceFarEndPointCosLabelLongTwowayMaxFD,
       "rcServiceFarEndPointCosLabelLongTwowayMinFD": rcServiceFarEndPointCosLabelLongTwowayMinFD,
       "rcServiceFarEndPointCosLabelSlaConfigDMOperId": rcServiceFarEndPointCosLabelSlaConfigDMOperId,
       "rcServiceFarEndPointCosLabelSlaConfigLMOperId": rcServiceFarEndPointCosLabelSlaConfigLMOperId,
       "rcServiceFarEndPointCosLabelEtherSamServiceIndex": rcServiceFarEndPointCosLabelEtherSamServiceIndex,
       "rcServiceFarEndPointCosLabelLongTwowayMFD": rcServiceFarEndPointCosLabelLongTwowayMFD,
       "rcServiceFarEndPointCosLabelLongTwowayFDR": rcServiceFarEndPointCosLabelLongTwowayFDR,
       "rcServiceFarEndPointCosLabelLongTwowayIFDV": rcServiceFarEndPointCosLabelLongTwowayIFDV,
       "rcServiceFarEndPointCosLabelLongTwowayMaxIFDV": rcServiceFarEndPointCosLabelLongTwowayMaxIFDV,
       "rcServiceFarEndPointCosLabelLongTwowayMinIFDV": rcServiceFarEndPointCosLabelLongTwowayMinIFDV,
       "rcServiceFarEndPointCosLabelLongTwowayMIFDV": rcServiceFarEndPointCosLabelLongTwowayMIFDV,
       "rcServiceFarEndPointCosLabelLongForwardFLR": rcServiceFarEndPointCosLabelLongForwardFLR,
       "rcServiceFarEndPointCosLabelLongBackwardFLR": rcServiceFarEndPointCosLabelLongBackwardFLR,
       "rcServiceFarEndPointCosLabelLongForwardAvail": rcServiceFarEndPointCosLabelLongForwardAvail,
       "rcServiceFarEndPointCosLabelLongBackwardAvail": rcServiceFarEndPointCosLabelLongBackwardAvail,
       "rcServiceFarEndPointCosLabelLongForwardHLI": rcServiceFarEndPointCosLabelLongForwardHLI,
       "rcServiceFarEndPointCosLabelLongBackwardHLI": rcServiceFarEndPointCosLabelLongBackwardHLI,
       "rcServiceFarEndPointCosLabelLongForwardCHLI": rcServiceFarEndPointCosLabelLongForwardCHLI,
       "rcServiceFarEndPointCosLabelLongBackwardCHLI": rcServiceFarEndPointCosLabelLongBackwardCHLI,
       "rcServiceFarEndPointCosLabelLongForwardFrameLost": rcServiceFarEndPointCosLabelLongForwardFrameLost,
       "rcServiceFarEndPointCosLabelLongBackwardFrameLost": rcServiceFarEndPointCosLabelLongBackwardFrameLost,
       "rcServiceFarEndPointCosLabelLongForwardUnAvailSeconds": rcServiceFarEndPointCosLabelLongForwardUnAvailSeconds,
       "rcServiceFarEndPointCosLabelLongBackwardUnAvailSeconds": rcServiceFarEndPointCosLabelLongBackwardUnAvailSeconds,
       "rcServiceSdpTable": rcServiceSdpTable,
       "rcServiceSdpEntry": rcServiceSdpEntry,
       "rcServiceSdpRowStatus": rcServiceSdpRowStatus,
       "rcServiceFarEndPointCosLabelCurrentTable": rcServiceFarEndPointCosLabelCurrentTable,
       "rcServiceFarEndPointCosLabelCurrentEntry": rcServiceFarEndPointCosLabelCurrentEntry,
       "rcServiceFarEndPointCosLabelCurrentTwowayFD": rcServiceFarEndPointCosLabelCurrentTwowayFD,
       "rcServiceFarEndPointCosLabelCurrentTwowayIFDV": rcServiceFarEndPointCosLabelCurrentTwowayIFDV,
       "rcServiceFarEndPointCosLabelCurrentForwardFLR": rcServiceFarEndPointCosLabelCurrentForwardFLR,
       "rcServiceFarEndPointCosLabelCurrentBackwardFLR": rcServiceFarEndPointCosLabelCurrentBackwardFLR,
       "rcServiceFarEndPointCosLabelCurrentForwardFrameLost": rcServiceFarEndPointCosLabelCurrentForwardFrameLost,
       "rcServiceFarEndPointCosLabelCurrentBackwardFrameLost": rcServiceFarEndPointCosLabelCurrentBackwardFrameLost,
       "rcServiceFarEndPointCosLabelCurrentForwardAvailStatus": rcServiceFarEndPointCosLabelCurrentForwardAvailStatus,
       "rcServiceFarEndPointCosLabelCurrentBackwardAvailStatus": rcServiceFarEndPointCosLabelCurrentBackwardAvailStatus,
       "rcServiceTrapGroup": rcServiceTrapGroup,
       "rcServiceEtherSamCfgTestFailTrap": rcServiceEtherSamCfgTestFailTrap,
       "rcServiceEtherSamCfgTestSuccessTrap": rcServiceEtherSamCfgTestSuccessTrap,
       "rcServiceEtherSamPfmTestFailTrap": rcServiceEtherSamPfmTestFailTrap,
       "rcServiceEtherSamPfmTestSuccessTrap": rcServiceEtherSamPfmTestSuccessTrap}
)
