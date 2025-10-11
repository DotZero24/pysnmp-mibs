# SNMP MIB module (ZTE-AN-PWE3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-PWE3-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:05 2025
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
 experimental,
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
    "experimental",
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

(ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnPwe3Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnPwe3GlobalObjects_ObjectIdentity = ObjectIdentity
zxAnPwe3GlobalObjects = _ZxAnPwe3GlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 1)
)


class _ZxAnPwe3McptTimer1_Type(Integer32):
    """Custom type zxAnPwe3McptTimer1 based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 4095),
    )


_ZxAnPwe3McptTimer1_Type.__name__ = "Integer32"
_ZxAnPwe3McptTimer1_Object = MibScalar
zxAnPwe3McptTimer1 = _ZxAnPwe3McptTimer1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 1, 1),
    _ZxAnPwe3McptTimer1_Type()
)
zxAnPwe3McptTimer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPwe3McptTimer1.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPwe3McptTimer1.setUnits("millisecond")


class _ZxAnPwe3McptTimer2_Type(Integer32):
    """Custom type zxAnPwe3McptTimer2 based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 4095),
    )


_ZxAnPwe3McptTimer2_Type.__name__ = "Integer32"
_ZxAnPwe3McptTimer2_Object = MibScalar
zxAnPwe3McptTimer2 = _ZxAnPwe3McptTimer2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 1, 2),
    _ZxAnPwe3McptTimer2_Type()
)
zxAnPwe3McptTimer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPwe3McptTimer2.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPwe3McptTimer2.setUnits("millisecond")


class _ZxAnPwe3McptTimer3_Type(Integer32):
    """Custom type zxAnPwe3McptTimer3 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 4095),
    )


_ZxAnPwe3McptTimer3_Type.__name__ = "Integer32"
_ZxAnPwe3McptTimer3_Object = MibScalar
zxAnPwe3McptTimer3 = _ZxAnPwe3McptTimer3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 1, 3),
    _ZxAnPwe3McptTimer3_Type()
)
zxAnPwe3McptTimer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPwe3McptTimer3.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPwe3McptTimer3.setUnits("millisecond")
_ZxAnPwe3Objects_ObjectIdentity = ObjectIdentity
zxAnPwe3Objects = _ZxAnPwe3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2)
)
_ZxAnPwe3PortAtmEncapTable_Object = MibTable
zxAnPwe3PortAtmEncapTable = _ZxAnPwe3PortAtmEncapTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 1)
)
if mibBuilder.loadTexts:
    zxAnPwe3PortAtmEncapTable.setStatus("current")
_ZxAnPwe3PortAtmEncapEntry_Object = MibTableRow
zxAnPwe3PortAtmEncapEntry = _ZxAnPwe3PortAtmEncapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 1, 1)
)
zxAnPwe3PortAtmEncapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-AN-PWE3-MIB", "zxAnPwe3PvcId"),
)
if mibBuilder.loadTexts:
    zxAnPwe3PortAtmEncapEntry.setStatus("current")
_ZxAnPwe3PvcId_Type = Integer32
_ZxAnPwe3PvcId_Object = MibTableColumn
zxAnPwe3PvcId = _ZxAnPwe3PvcId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 1, 1, 1),
    _ZxAnPwe3PvcId_Type()
)
zxAnPwe3PvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPwe3PvcId.setStatus("current")


class _ZxAnPwe3PortMaxCellsPerPacket_Type(Integer32):
    """Custom type zxAnPwe3PortMaxCellsPerPacket based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_ZxAnPwe3PortMaxCellsPerPacket_Type.__name__ = "Integer32"
_ZxAnPwe3PortMaxCellsPerPacket_Object = MibTableColumn
zxAnPwe3PortMaxCellsPerPacket = _ZxAnPwe3PortMaxCellsPerPacket_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 1, 1, 2),
    _ZxAnPwe3PortMaxCellsPerPacket_Type()
)
zxAnPwe3PortMaxCellsPerPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPwe3PortMaxCellsPerPacket.setStatus("current")


class _ZxAnPwe3PortMcptTimer_Type(Integer32):
    """Custom type zxAnPwe3PortMcptTimer based on Integer32"""
    defaultValue = 0

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
        *(("noUse", 0),
          ("zxAnPwe3McptTimer1", 1),
          ("zxAnPwe3McptTimer2", 2),
          ("zxAnPwe3McptTimer3", 3))
    )


_ZxAnPwe3PortMcptTimer_Type.__name__ = "Integer32"
_ZxAnPwe3PortMcptTimer_Object = MibTableColumn
zxAnPwe3PortMcptTimer = _ZxAnPwe3PortMcptTimer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 1, 1, 3),
    _ZxAnPwe3PortMcptTimer_Type()
)
zxAnPwe3PortMcptTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPwe3PortMcptTimer.setStatus("current")


class _ZxAnPwe3PortEncapsulationType_Type(Integer32):
    """Custom type zxAnPwe3PortEncapsulationType based on Integer32"""
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
        *(("encapUnknown", 0),
          ("encapAtmAal01to1", 1),
          ("encapAtmAal0nto1", 2),
          ("encapAtmAal5pdu", 3),
          ("encapEthAal5sdu", 4))
    )


_ZxAnPwe3PortEncapsulationType_Type.__name__ = "Integer32"
_ZxAnPwe3PortEncapsulationType_Object = MibTableColumn
zxAnPwe3PortEncapsulationType = _ZxAnPwe3PortEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 1, 1, 4),
    _ZxAnPwe3PortEncapsulationType_Type()
)
zxAnPwe3PortEncapsulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPwe3PortEncapsulationType.setStatus("current")
_ZxAnPwe3PortToVCMappingTable_Object = MibTable
zxAnPwe3PortToVCMappingTable = _ZxAnPwe3PortToVCMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnPwe3PortToVCMappingTable.setStatus("current")
_ZxAnPwe3PortToVCMappingEntry_Object = MibTableRow
zxAnPwe3PortToVCMappingEntry = _ZxAnPwe3PortToVCMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 2, 1)
)
zxAnPwe3PortToVCMappingEntry.setIndexNames(
    (0, "ZTE-AN-PWE3-MIB", "zxAnPwe3PortIndex"),
    (0, "ZTE-AN-PWE3-MIB", "zxAnPwe3Vcid"),
)
if mibBuilder.loadTexts:
    zxAnPwe3PortToVCMappingEntry.setStatus("current")
_ZxAnPwe3PortIndex_Type = ZxAnIfindex
_ZxAnPwe3PortIndex_Object = MibTableColumn
zxAnPwe3PortIndex = _ZxAnPwe3PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 2, 1, 1),
    _ZxAnPwe3PortIndex_Type()
)
zxAnPwe3PortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPwe3PortIndex.setStatus("current")


class _ZxAnPwe3Vcid_Type(Unsigned32):
    """Custom type zxAnPwe3Vcid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ZxAnPwe3Vcid_Type.__name__ = "Unsigned32"
_ZxAnPwe3Vcid_Object = MibTableColumn
zxAnPwe3Vcid = _ZxAnPwe3Vcid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 2, 1, 2),
    _ZxAnPwe3Vcid_Type()
)
zxAnPwe3Vcid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPwe3Vcid.setStatus("current")
_ZxAnPwe3PeerAddress_Type = IpAddress
_ZxAnPwe3PeerAddress_Object = MibTableColumn
zxAnPwe3PeerAddress = _ZxAnPwe3PeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 2, 1, 3),
    _ZxAnPwe3PeerAddress_Type()
)
zxAnPwe3PeerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPwe3PeerAddress.setStatus("current")


class _ZxAnPwe3ControlWordEnable_Type(Integer32):
    """Custom type zxAnPwe3ControlWordEnable based on Integer32"""
    defaultValue = 2

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


_ZxAnPwe3ControlWordEnable_Type.__name__ = "Integer32"
_ZxAnPwe3ControlWordEnable_Object = MibTableColumn
zxAnPwe3ControlWordEnable = _ZxAnPwe3ControlWordEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 2, 1, 4),
    _ZxAnPwe3ControlWordEnable_Type()
)
zxAnPwe3ControlWordEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPwe3ControlWordEnable.setStatus("current")


class _ZxAnPwe3SequenceEnable_Type(Integer32):
    """Custom type zxAnPwe3SequenceEnable based on Integer32"""
    defaultValue = 2

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


_ZxAnPwe3SequenceEnable_Type.__name__ = "Integer32"
_ZxAnPwe3SequenceEnable_Object = MibTableColumn
zxAnPwe3SequenceEnable = _ZxAnPwe3SequenceEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 2, 1, 5),
    _ZxAnPwe3SequenceEnable_Type()
)
zxAnPwe3SequenceEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPwe3SequenceEnable.setStatus("current")
_ZxAnPwe3PortVCMappingRowStatus_Type = RowStatus
_ZxAnPwe3PortVCMappingRowStatus_Object = MibTableColumn
zxAnPwe3PortVCMappingRowStatus = _ZxAnPwe3PortVCMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 2, 1, 50),
    _ZxAnPwe3PortVCMappingRowStatus_Type()
)
zxAnPwe3PortVCMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPwe3PortVCMappingRowStatus.setStatus("current")
_ZxAnPwe3PwTable_Object = MibTable
zxAnPwe3PwTable = _ZxAnPwe3PwTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4)
)
if mibBuilder.loadTexts:
    zxAnPwe3PwTable.setStatus("current")
_ZxAnPwe3PwEntry_Object = MibTableRow
zxAnPwe3PwEntry = _ZxAnPwe3PwEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1)
)
zxAnPwe3PwEntry.setIndexNames(
    (0, "ZTE-AN-PWE3-MIB", "zxAnPwe3PwVcId"),
)
if mibBuilder.loadTexts:
    zxAnPwe3PwEntry.setStatus("current")


class _ZxAnPwe3PwVcId_Type(Unsigned32):
    """Custom type zxAnPwe3PwVcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ZxAnPwe3PwVcId_Type.__name__ = "Unsigned32"
_ZxAnPwe3PwVcId_Object = MibTableColumn
zxAnPwe3PwVcId = _ZxAnPwe3PwVcId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 1),
    _ZxAnPwe3PwVcId_Type()
)
zxAnPwe3PwVcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPwe3PwVcId.setStatus("current")


class _ZxAnPwe3PwType_Type(Integer32):
    """Custom type zxAnPwe3PwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pwUnknown", 0),
          ("pwSpoke", 1),
          ("pwHub", 2))
    )


_ZxAnPwe3PwType_Type.__name__ = "Integer32"
_ZxAnPwe3PwType_Object = MibTableColumn
zxAnPwe3PwType = _ZxAnPwe3PwType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 2),
    _ZxAnPwe3PwType_Type()
)
zxAnPwe3PwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwType.setStatus("current")


class _ZxAnPwe3PwEncapType_Type(Integer32):
    """Custom type zxAnPwe3PwEncapType based on Integer32"""
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("encapUnknown", 0),
          ("encapFrDlci", 1),
          ("encapAtmAal5", 2),
          ("encapAtmTranscell", 3),
          ("encapEthVlan", 4),
          ("encapEth", 5),
          ("encapHdlc", 6),
          ("encapPpp", 7),
          ("encapCem", 8),
          ("encapAtmVcc", 9),
          ("encapAtmVpc", 10))
    )


_ZxAnPwe3PwEncapType_Type.__name__ = "Integer32"
_ZxAnPwe3PwEncapType_Object = MibTableColumn
zxAnPwe3PwEncapType = _ZxAnPwe3PwEncapType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 3),
    _ZxAnPwe3PwEncapType_Type()
)
zxAnPwe3PwEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwEncapType.setStatus("current")
_ZxAnPwe3PwVlanid_Type = Integer32
_ZxAnPwe3PwVlanid_Object = MibTableColumn
zxAnPwe3PwVlanid = _ZxAnPwe3PwVlanid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 4),
    _ZxAnPwe3PwVlanid_Type()
)
zxAnPwe3PwVlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwVlanid.setStatus("current")


class _ZxAnPwe3PwPsnType_Type(Integer32):
    """Custom type zxAnPwe3PwPsnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknownTunnel", 0),
          ("mplsTunnel", 1),
          ("teTunnel", 2))
    )


_ZxAnPwe3PwPsnType_Type.__name__ = "Integer32"
_ZxAnPwe3PwPsnType_Object = MibTableColumn
zxAnPwe3PwPsnType = _ZxAnPwe3PwPsnType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 5),
    _ZxAnPwe3PwPsnType_Type()
)
zxAnPwe3PwPsnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwPsnType.setStatus("current")
_ZxAnPwe3PwTunnelid_Type = Unsigned32
_ZxAnPwe3PwTunnelid_Object = MibTableColumn
zxAnPwe3PwTunnelid = _ZxAnPwe3PwTunnelid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 6),
    _ZxAnPwe3PwTunnelid_Type()
)
zxAnPwe3PwTunnelid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwTunnelid.setStatus("current")


class _ZxAnPwe3PwInlabel_Type(Unsigned32):
    """Custom type zxAnPwe3PwInlabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_ZxAnPwe3PwInlabel_Type.__name__ = "Unsigned32"
_ZxAnPwe3PwInlabel_Object = MibTableColumn
zxAnPwe3PwInlabel = _ZxAnPwe3PwInlabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 7),
    _ZxAnPwe3PwInlabel_Type()
)
zxAnPwe3PwInlabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwInlabel.setStatus("current")


class _ZxAnPwe3PwOutlabel_Type(Unsigned32):
    """Custom type zxAnPwe3PwOutlabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_ZxAnPwe3PwOutlabel_Type.__name__ = "Unsigned32"
_ZxAnPwe3PwOutlabel_Object = MibTableColumn
zxAnPwe3PwOutlabel = _ZxAnPwe3PwOutlabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 8),
    _ZxAnPwe3PwOutlabel_Type()
)
zxAnPwe3PwOutlabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwOutlabel.setStatus("current")


class _ZxAnPwe3PwCbit_Type(Integer32):
    """Custom type zxAnPwe3PwCbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cwordDisable", 0),
          ("cwordEnable", 1))
    )


_ZxAnPwe3PwCbit_Type.__name__ = "Integer32"
_ZxAnPwe3PwCbit_Object = MibTableColumn
zxAnPwe3PwCbit = _ZxAnPwe3PwCbit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 9),
    _ZxAnPwe3PwCbit_Type()
)
zxAnPwe3PwCbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwCbit.setStatus("current")


class _ZxAnPwe3PwStatus_Type(Integer32):
    """Custom type zxAnPwe3PwStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notEstablished", 0),
          ("established", 1))
    )


_ZxAnPwe3PwStatus_Type.__name__ = "Integer32"
_ZxAnPwe3PwStatus_Object = MibTableColumn
zxAnPwe3PwStatus = _ZxAnPwe3PwStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 10),
    _ZxAnPwe3PwStatus_Type()
)
zxAnPwe3PwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwStatus.setStatus("current")
_ZxAnPwe3PwLocalGroupId_Type = Unsigned32
_ZxAnPwe3PwLocalGroupId_Object = MibTableColumn
zxAnPwe3PwLocalGroupId = _ZxAnPwe3PwLocalGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 11),
    _ZxAnPwe3PwLocalGroupId_Type()
)
zxAnPwe3PwLocalGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwLocalGroupId.setStatus("current")


class _ZxAnPwe3PwLocalEncapType_Type(Integer32):
    """Custom type zxAnPwe3PwLocalEncapType based on Integer32"""
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("encapUnknown", 0),
          ("encapFrDlci", 1),
          ("encapAtmAal5", 2),
          ("encapAtmTranscell", 3),
          ("encapEthVlan", 4),
          ("encapEth", 5),
          ("encapHdlc", 6),
          ("encapPpp", 7),
          ("encapCem", 8),
          ("encapAtmVcc", 9),
          ("encapAtmVpc", 10))
    )


_ZxAnPwe3PwLocalEncapType_Type.__name__ = "Integer32"
_ZxAnPwe3PwLocalEncapType_Object = MibTableColumn
zxAnPwe3PwLocalEncapType = _ZxAnPwe3PwLocalEncapType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 12),
    _ZxAnPwe3PwLocalEncapType_Type()
)
zxAnPwe3PwLocalEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwLocalEncapType.setStatus("current")


class _ZxAnPwe3PwLocalLabel_Type(Unsigned32):
    """Custom type zxAnPwe3PwLocalLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_ZxAnPwe3PwLocalLabel_Type.__name__ = "Unsigned32"
_ZxAnPwe3PwLocalLabel_Object = MibTableColumn
zxAnPwe3PwLocalLabel = _ZxAnPwe3PwLocalLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 13),
    _ZxAnPwe3PwLocalLabel_Type()
)
zxAnPwe3PwLocalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwLocalLabel.setStatus("current")


class _ZxAnPwe3PwLocalCbit_Type(Integer32):
    """Custom type zxAnPwe3PwLocalCbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cwordDisable", 0),
          ("cwordEnable", 1))
    )


_ZxAnPwe3PwLocalCbit_Type.__name__ = "Integer32"
_ZxAnPwe3PwLocalCbit_Object = MibTableColumn
zxAnPwe3PwLocalCbit = _ZxAnPwe3PwLocalCbit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 14),
    _ZxAnPwe3PwLocalCbit_Type()
)
zxAnPwe3PwLocalCbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwLocalCbit.setStatus("current")


class _ZxAnPwe3PwLocalPortName_Type(DisplayString):
    """Custom type zxAnPwe3PwLocalPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnPwe3PwLocalPortName_Type.__name__ = "DisplayString"
_ZxAnPwe3PwLocalPortName_Object = MibTableColumn
zxAnPwe3PwLocalPortName = _ZxAnPwe3PwLocalPortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 15),
    _ZxAnPwe3PwLocalPortName_Type()
)
zxAnPwe3PwLocalPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwLocalPortName.setStatus("current")
_ZxAnPwe3PwLocalRouterId_Type = IpAddress
_ZxAnPwe3PwLocalRouterId_Object = MibTableColumn
zxAnPwe3PwLocalRouterId = _ZxAnPwe3PwLocalRouterId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 16),
    _ZxAnPwe3PwLocalRouterId_Type()
)
zxAnPwe3PwLocalRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwLocalRouterId.setStatus("current")


class _ZxAnPwe3PwLocalIfMtu_Type(Unsigned32):
    """Custom type zxAnPwe3PwLocalIfMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnPwe3PwLocalIfMtu_Type.__name__ = "Unsigned32"
_ZxAnPwe3PwLocalIfMtu_Object = MibTableColumn
zxAnPwe3PwLocalIfMtu = _ZxAnPwe3PwLocalIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 17),
    _ZxAnPwe3PwLocalIfMtu_Type()
)
zxAnPwe3PwLocalIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwLocalIfMtu.setStatus("current")
_ZxAnPwe3PwRemoteGroupId_Type = Unsigned32
_ZxAnPwe3PwRemoteGroupId_Object = MibTableColumn
zxAnPwe3PwRemoteGroupId = _ZxAnPwe3PwRemoteGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 18),
    _ZxAnPwe3PwRemoteGroupId_Type()
)
zxAnPwe3PwRemoteGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwRemoteGroupId.setStatus("current")


class _ZxAnPwe3PwRemoteEncapType_Type(Integer32):
    """Custom type zxAnPwe3PwRemoteEncapType based on Integer32"""
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("encapUnknown", 0),
          ("encapFrDlci", 1),
          ("encapAtmAal5", 2),
          ("encapAtmTranscell", 3),
          ("encapEthVlan", 4),
          ("encapEth", 5),
          ("encapHdlc", 6),
          ("encapPpp", 7),
          ("encapCem", 8),
          ("encapAtmVcc", 9),
          ("encapAtmVpc", 10))
    )


_ZxAnPwe3PwRemoteEncapType_Type.__name__ = "Integer32"
_ZxAnPwe3PwRemoteEncapType_Object = MibTableColumn
zxAnPwe3PwRemoteEncapType = _ZxAnPwe3PwRemoteEncapType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 19),
    _ZxAnPwe3PwRemoteEncapType_Type()
)
zxAnPwe3PwRemoteEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwRemoteEncapType.setStatus("current")
_ZxAnPwe3PwRemoteLabel_Type = Unsigned32
_ZxAnPwe3PwRemoteLabel_Object = MibTableColumn
zxAnPwe3PwRemoteLabel = _ZxAnPwe3PwRemoteLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 20),
    _ZxAnPwe3PwRemoteLabel_Type()
)
zxAnPwe3PwRemoteLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwRemoteLabel.setStatus("current")


class _ZxAnPwe3PwRemoteCbit_Type(Integer32):
    """Custom type zxAnPwe3PwRemoteCbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cwordDisable", 0),
          ("cwordEnable", 1))
    )


_ZxAnPwe3PwRemoteCbit_Type.__name__ = "Integer32"
_ZxAnPwe3PwRemoteCbit_Object = MibTableColumn
zxAnPwe3PwRemoteCbit = _ZxAnPwe3PwRemoteCbit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 21),
    _ZxAnPwe3PwRemoteCbit_Type()
)
zxAnPwe3PwRemoteCbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwRemoteCbit.setStatus("current")


class _ZxAnPwe3PwRemotePortName_Type(DisplayString):
    """Custom type zxAnPwe3PwRemotePortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnPwe3PwRemotePortName_Type.__name__ = "DisplayString"
_ZxAnPwe3PwRemotePortName_Object = MibTableColumn
zxAnPwe3PwRemotePortName = _ZxAnPwe3PwRemotePortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 22),
    _ZxAnPwe3PwRemotePortName_Type()
)
zxAnPwe3PwRemotePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwRemotePortName.setStatus("current")
_ZxAnPwe3PwRemoteRouterId_Type = IpAddress
_ZxAnPwe3PwRemoteRouterId_Object = MibTableColumn
zxAnPwe3PwRemoteRouterId = _ZxAnPwe3PwRemoteRouterId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 23),
    _ZxAnPwe3PwRemoteRouterId_Type()
)
zxAnPwe3PwRemoteRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwRemoteRouterId.setStatus("current")
_ZxAnPwe3PwRemoteIfMtu_Type = Unsigned32
_ZxAnPwe3PwRemoteIfMtu_Object = MibTableColumn
zxAnPwe3PwRemoteIfMtu = _ZxAnPwe3PwRemoteIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 56, 2, 4, 1, 24),
    _ZxAnPwe3PwRemoteIfMtu_Type()
)
zxAnPwe3PwRemoteIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPwe3PwRemoteIfMtu.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-PWE3-MIB",
    **{"zxAnPwe3Mib": zxAnPwe3Mib,
       "zxAnPwe3GlobalObjects": zxAnPwe3GlobalObjects,
       "zxAnPwe3McptTimer1": zxAnPwe3McptTimer1,
       "zxAnPwe3McptTimer2": zxAnPwe3McptTimer2,
       "zxAnPwe3McptTimer3": zxAnPwe3McptTimer3,
       "zxAnPwe3Objects": zxAnPwe3Objects,
       "zxAnPwe3PortAtmEncapTable": zxAnPwe3PortAtmEncapTable,
       "zxAnPwe3PortAtmEncapEntry": zxAnPwe3PortAtmEncapEntry,
       "zxAnPwe3PvcId": zxAnPwe3PvcId,
       "zxAnPwe3PortMaxCellsPerPacket": zxAnPwe3PortMaxCellsPerPacket,
       "zxAnPwe3PortMcptTimer": zxAnPwe3PortMcptTimer,
       "zxAnPwe3PortEncapsulationType": zxAnPwe3PortEncapsulationType,
       "zxAnPwe3PortToVCMappingTable": zxAnPwe3PortToVCMappingTable,
       "zxAnPwe3PortToVCMappingEntry": zxAnPwe3PortToVCMappingEntry,
       "zxAnPwe3PortIndex": zxAnPwe3PortIndex,
       "zxAnPwe3Vcid": zxAnPwe3Vcid,
       "zxAnPwe3PeerAddress": zxAnPwe3PeerAddress,
       "zxAnPwe3ControlWordEnable": zxAnPwe3ControlWordEnable,
       "zxAnPwe3SequenceEnable": zxAnPwe3SequenceEnable,
       "zxAnPwe3PortVCMappingRowStatus": zxAnPwe3PortVCMappingRowStatus,
       "zxAnPwe3PwTable": zxAnPwe3PwTable,
       "zxAnPwe3PwEntry": zxAnPwe3PwEntry,
       "zxAnPwe3PwVcId": zxAnPwe3PwVcId,
       "zxAnPwe3PwType": zxAnPwe3PwType,
       "zxAnPwe3PwEncapType": zxAnPwe3PwEncapType,
       "zxAnPwe3PwVlanid": zxAnPwe3PwVlanid,
       "zxAnPwe3PwPsnType": zxAnPwe3PwPsnType,
       "zxAnPwe3PwTunnelid": zxAnPwe3PwTunnelid,
       "zxAnPwe3PwInlabel": zxAnPwe3PwInlabel,
       "zxAnPwe3PwOutlabel": zxAnPwe3PwOutlabel,
       "zxAnPwe3PwCbit": zxAnPwe3PwCbit,
       "zxAnPwe3PwStatus": zxAnPwe3PwStatus,
       "zxAnPwe3PwLocalGroupId": zxAnPwe3PwLocalGroupId,
       "zxAnPwe3PwLocalEncapType": zxAnPwe3PwLocalEncapType,
       "zxAnPwe3PwLocalLabel": zxAnPwe3PwLocalLabel,
       "zxAnPwe3PwLocalCbit": zxAnPwe3PwLocalCbit,
       "zxAnPwe3PwLocalPortName": zxAnPwe3PwLocalPortName,
       "zxAnPwe3PwLocalRouterId": zxAnPwe3PwLocalRouterId,
       "zxAnPwe3PwLocalIfMtu": zxAnPwe3PwLocalIfMtu,
       "zxAnPwe3PwRemoteGroupId": zxAnPwe3PwRemoteGroupId,
       "zxAnPwe3PwRemoteEncapType": zxAnPwe3PwRemoteEncapType,
       "zxAnPwe3PwRemoteLabel": zxAnPwe3PwRemoteLabel,
       "zxAnPwe3PwRemoteCbit": zxAnPwe3PwRemoteCbit,
       "zxAnPwe3PwRemotePortName": zxAnPwe3PwRemotePortName,
       "zxAnPwe3PwRemoteRouterId": zxAnPwe3PwRemoteRouterId,
       "zxAnPwe3PwRemoteIfMtu": zxAnPwe3PwRemoteIfMtu}
)
