# SNMP MIB module (H3C-MPLSEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-MPLSEXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:51 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cMplsExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142)
)
if mibBuilder.loadTexts:
    h3cMplsExt.setRevisions(
        ("2017-02-17 18:00",
         "2015-06-16 18:00",
         "2014-12-17 12:00",
         "2013-06-13 18:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cMplsExtObjects_ObjectIdentity = ObjectIdentity
h3cMplsExtObjects = _H3cMplsExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1)
)
_H3cMplsExtScalarGroup_ObjectIdentity = ObjectIdentity
h3cMplsExtScalarGroup = _H3cMplsExtScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 1)
)


class _H3cMplsExtLsrID_Type(OctetString):
    """Custom type h3cMplsExtLsrID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cMplsExtLsrID_Type.__name__ = "OctetString"
_H3cMplsExtLsrID_Object = MibScalar
h3cMplsExtLsrID = _H3cMplsExtLsrID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 1, 1),
    _H3cMplsExtLsrID_Type()
)
h3cMplsExtLsrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMplsExtLsrID.setStatus("current")
_H3cMplsExtLdpStatus_Type = TruthValue
_H3cMplsExtLdpStatus_Object = MibScalar
h3cMplsExtLdpStatus = _H3cMplsExtLdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 1, 2),
    _H3cMplsExtLdpStatus_Type()
)
h3cMplsExtLdpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMplsExtLdpStatus.setStatus("current")
_H3cMplsExtTable_Object = MibTable
h3cMplsExtTable = _H3cMplsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 2)
)
if mibBuilder.loadTexts:
    h3cMplsExtTable.setStatus("current")
_H3cMplsExtEntry_Object = MibTableRow
h3cMplsExtEntry = _H3cMplsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 2, 1)
)
h3cMplsExtEntry.setIndexNames(
    (0, "H3C-MPLSEXT-MIB", "h3cMplsExtIndex"),
)
if mibBuilder.loadTexts:
    h3cMplsExtEntry.setStatus("current")


class _H3cMplsExtIndex_Type(Unsigned32):
    """Custom type h3cMplsExtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cMplsExtIndex_Type.__name__ = "Unsigned32"
_H3cMplsExtIndex_Object = MibTableColumn
h3cMplsExtIndex = _H3cMplsExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 2, 1, 1),
    _H3cMplsExtIndex_Type()
)
h3cMplsExtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMplsExtIndex.setStatus("current")


class _H3cMplsExtCapability_Type(TruthValue):
    """Custom type h3cMplsExtCapability based on TruthValue"""
    defaultValue = 2


_H3cMplsExtCapability_Type.__name__ = "TruthValue"
_H3cMplsExtCapability_Object = MibTableColumn
h3cMplsExtCapability = _H3cMplsExtCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 2, 1, 2),
    _H3cMplsExtCapability_Type()
)
h3cMplsExtCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsExtCapability.setStatus("current")


class _H3cMplsExtMtu_Type(Unsigned32):
    """Custom type h3cMplsExtMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(46, 65535),
    )


_H3cMplsExtMtu_Type.__name__ = "Unsigned32"
_H3cMplsExtMtu_Object = MibTableColumn
h3cMplsExtMtu = _H3cMplsExtMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 2, 1, 3),
    _H3cMplsExtMtu_Type()
)
h3cMplsExtMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsExtMtu.setStatus("current")
_H3cMplsExtRowStatus_Type = RowStatus
_H3cMplsExtRowStatus_Object = MibTableColumn
h3cMplsExtRowStatus = _H3cMplsExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 2, 1, 4),
    _H3cMplsExtRowStatus_Type()
)
h3cMplsExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsExtRowStatus.setStatus("current")
_H3cMplsExtLdpTable_Object = MibTable
h3cMplsExtLdpTable = _H3cMplsExtLdpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 3)
)
if mibBuilder.loadTexts:
    h3cMplsExtLdpTable.setStatus("current")
_H3cMplsExtLdpEntry_Object = MibTableRow
h3cMplsExtLdpEntry = _H3cMplsExtLdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 3, 1)
)
h3cMplsExtLdpEntry.setIndexNames(
    (0, "H3C-MPLSEXT-MIB", "h3cMplsExtLdpIndex"),
)
if mibBuilder.loadTexts:
    h3cMplsExtLdpEntry.setStatus("current")


class _H3cMplsExtLdpIndex_Type(Unsigned32):
    """Custom type h3cMplsExtLdpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cMplsExtLdpIndex_Type.__name__ = "Unsigned32"
_H3cMplsExtLdpIndex_Object = MibTableColumn
h3cMplsExtLdpIndex = _H3cMplsExtLdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 3, 1, 1),
    _H3cMplsExtLdpIndex_Type()
)
h3cMplsExtLdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMplsExtLdpIndex.setStatus("current")


class _H3cMplsExtLdpCapability_Type(TruthValue):
    """Custom type h3cMplsExtLdpCapability based on TruthValue"""
    defaultValue = 2


_H3cMplsExtLdpCapability_Type.__name__ = "TruthValue"
_H3cMplsExtLdpCapability_Object = MibTableColumn
h3cMplsExtLdpCapability = _H3cMplsExtLdpCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 3, 1, 2),
    _H3cMplsExtLdpCapability_Type()
)
h3cMplsExtLdpCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsExtLdpCapability.setStatus("current")
_H3cMplsExtLdpRowStatus_Type = RowStatus
_H3cMplsExtLdpRowStatus_Object = MibTableColumn
h3cMplsExtLdpRowStatus = _H3cMplsExtLdpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 3, 1, 3),
    _H3cMplsExtLdpRowStatus_Type()
)
h3cMplsExtLdpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsExtLdpRowStatus.setStatus("current")
_H3cMplsExtBfdTable_Object = MibTable
h3cMplsExtBfdTable = _H3cMplsExtBfdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 4)
)
if mibBuilder.loadTexts:
    h3cMplsExtBfdTable.setStatus("current")
_H3cMplsExtBfdEntry_Object = MibTableRow
h3cMplsExtBfdEntry = _H3cMplsExtBfdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 4, 1)
)
h3cMplsExtBfdEntry.setIndexNames(
    (0, "H3C-MPLSEXT-MIB", "h3cMplsExtBfdLocalDiscr"),
)
if mibBuilder.loadTexts:
    h3cMplsExtBfdEntry.setStatus("current")


class _H3cMplsExtBfdLocalDiscr_Type(Unsigned32):
    """Custom type h3cMplsExtBfdLocalDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cMplsExtBfdLocalDiscr_Type.__name__ = "Unsigned32"
_H3cMplsExtBfdLocalDiscr_Object = MibTableColumn
h3cMplsExtBfdLocalDiscr = _H3cMplsExtBfdLocalDiscr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 4, 1, 1),
    _H3cMplsExtBfdLocalDiscr_Type()
)
h3cMplsExtBfdLocalDiscr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMplsExtBfdLocalDiscr.setStatus("current")


class _H3cMplsExtBfdType_Type(Integer32):
    """Custom type h3cMplsExtBfdType based on Integer32"""
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
          ("lsp", 2),
          ("vpwsPw", 3),
          ("vplsPw", 4),
          ("te", 5))
    )


_H3cMplsExtBfdType_Type.__name__ = "Integer32"
_H3cMplsExtBfdType_Object = MibTableColumn
h3cMplsExtBfdType = _H3cMplsExtBfdType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 4, 1, 2),
    _H3cMplsExtBfdType_Type()
)
h3cMplsExtBfdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtBfdType.setStatus("current")
_H3cMplsExtBfdBindIfIndex_Type = InterfaceIndexOrZero
_H3cMplsExtBfdBindIfIndex_Object = MibTableColumn
h3cMplsExtBfdBindIfIndex = _H3cMplsExtBfdBindIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 4, 1, 3),
    _H3cMplsExtBfdBindIfIndex_Type()
)
h3cMplsExtBfdBindIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtBfdBindIfIndex.setStatus("current")


class _H3cMplsExtBfdBindIfName_Type(DisplayString):
    """Custom type h3cMplsExtBfdBindIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cMplsExtBfdBindIfName_Type.__name__ = "DisplayString"
_H3cMplsExtBfdBindIfName_Object = MibTableColumn
h3cMplsExtBfdBindIfName = _H3cMplsExtBfdBindIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 4, 1, 4),
    _H3cMplsExtBfdBindIfName_Type()
)
h3cMplsExtBfdBindIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtBfdBindIfName.setStatus("current")


class _H3cMplsExtBfdXcIndex_Type(OctetString):
    """Custom type h3cMplsExtBfdXcIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_H3cMplsExtBfdXcIndex_Type.__name__ = "OctetString"
_H3cMplsExtBfdXcIndex_Object = MibTableColumn
h3cMplsExtBfdXcIndex = _H3cMplsExtBfdXcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 4, 1, 5),
    _H3cMplsExtBfdXcIndex_Type()
)
h3cMplsExtBfdXcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtBfdXcIndex.setStatus("current")


class _H3cMplsExtBfdPwBackupFlag_Type(Integer32):
    """Custom type h3cMplsExtBfdPwBackupFlag based on Integer32"""
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
          ("primary", 2),
          ("backup", 3))
    )


_H3cMplsExtBfdPwBackupFlag_Type.__name__ = "Integer32"
_H3cMplsExtBfdPwBackupFlag_Object = MibTableColumn
h3cMplsExtBfdPwBackupFlag = _H3cMplsExtBfdPwBackupFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 4, 1, 6),
    _H3cMplsExtBfdPwBackupFlag_Type()
)
h3cMplsExtBfdPwBackupFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtBfdPwBackupFlag.setStatus("current")


class _H3cMplsExtBfdPwId_Type(Unsigned32):
    """Custom type h3cMplsExtBfdPwId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_H3cMplsExtBfdPwId_Type.__name__ = "Unsigned32"
_H3cMplsExtBfdPwId_Object = MibTableColumn
h3cMplsExtBfdPwId = _H3cMplsExtBfdPwId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 4, 1, 7),
    _H3cMplsExtBfdPwId_Type()
)
h3cMplsExtBfdPwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtBfdPwId.setStatus("current")


class _H3cMplsExtBfdVsiIndex_Type(Unsigned32):
    """Custom type h3cMplsExtBfdVsiIndex based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cMplsExtBfdVsiIndex_Type.__name__ = "Unsigned32"
_H3cMplsExtBfdVsiIndex_Object = MibTableColumn
h3cMplsExtBfdVsiIndex = _H3cMplsExtBfdVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 4, 1, 8),
    _H3cMplsExtBfdVsiIndex_Type()
)
h3cMplsExtBfdVsiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtBfdVsiIndex.setStatus("current")
_H3cMplsExtBfdPwPeerIpType_Type = InetAddressType
_H3cMplsExtBfdPwPeerIpType_Object = MibTableColumn
h3cMplsExtBfdPwPeerIpType = _H3cMplsExtBfdPwPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 4, 1, 9),
    _H3cMplsExtBfdPwPeerIpType_Type()
)
h3cMplsExtBfdPwPeerIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtBfdPwPeerIpType.setStatus("current")
_H3cMplsExtBfdPwPeerIp_Type = InetAddress
_H3cMplsExtBfdPwPeerIp_Object = MibTableColumn
h3cMplsExtBfdPwPeerIp = _H3cMplsExtBfdPwPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 4, 1, 10),
    _H3cMplsExtBfdPwPeerIp_Type()
)
h3cMplsExtBfdPwPeerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtBfdPwPeerIp.setStatus("current")


class _H3cMplsExtBfdPwSPE_Type(Integer32):
    """Custom type h3cMplsExtBfdPwSPE based on Integer32"""
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
          ("upe", 2),
          ("spe", 3))
    )


_H3cMplsExtBfdPwSPE_Type.__name__ = "Integer32"
_H3cMplsExtBfdPwSPE_Object = MibTableColumn
h3cMplsExtBfdPwSPE = _H3cMplsExtBfdPwSPE_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 4, 1, 11),
    _H3cMplsExtBfdPwSPE_Type()
)
h3cMplsExtBfdPwSPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtBfdPwSPE.setStatus("current")


class _H3cMplsExtBfdPwEncapType_Type(Integer32):
    """Custom type h3cMplsExtBfdPwEncapType based on Integer32"""
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
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("frDlciMartini", 2),
          ("atmAal5Sdu", 3),
          ("atmTransCell", 4),
          ("vlan", 5),
          ("ethernet", 6),
          ("hdlc", 7),
          ("ppp", 8),
          ("cesom", 9),
          ("atmNto1Vcc", 10),
          ("atmNto1Vpc", 11),
          ("ipInterworking", 12),
          ("atm1to1Vcc", 13),
          ("atm1to1Vpc", 14),
          ("atmAal5Pdu", 15),
          ("frPort", 16),
          ("cep", 17),
          ("satopE1", 18),
          ("satopT1", 19),
          ("satopE3", 20),
          ("satopT3", 21),
          ("esopsnBasic", 22),
          ("tdmoipAal1Mode", 23),
          ("tdmCesopsnWithCas", 24),
          ("tdmoipAal2Mode", 25),
          ("frDlci", 26))
    )


_H3cMplsExtBfdPwEncapType_Type.__name__ = "Integer32"
_H3cMplsExtBfdPwEncapType_Object = MibTableColumn
h3cMplsExtBfdPwEncapType = _H3cMplsExtBfdPwEncapType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 4, 1, 12),
    _H3cMplsExtBfdPwEncapType_Type()
)
h3cMplsExtBfdPwEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtBfdPwEncapType.setStatus("current")
_H3cMplsExtVpnStatsTable_Object = MibTable
h3cMplsExtVpnStatsTable = _H3cMplsExtVpnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 5)
)
if mibBuilder.loadTexts:
    h3cMplsExtVpnStatsTable.setStatus("current")
_H3cMplsExtVpnStatsEntry_Object = MibTableRow
h3cMplsExtVpnStatsEntry = _H3cMplsExtVpnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 5, 1)
)
h3cMplsExtVpnStatsEntry.setIndexNames(
    (0, "H3C-MPLSEXT-MIB", "h3cMplsExtVpnStatsVrfIndex"),
)
if mibBuilder.loadTexts:
    h3cMplsExtVpnStatsEntry.setStatus("current")


class _H3cMplsExtVpnStatsVrfIndex_Type(Unsigned32):
    """Custom type h3cMplsExtVpnStatsVrfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cMplsExtVpnStatsVrfIndex_Type.__name__ = "Unsigned32"
_H3cMplsExtVpnStatsVrfIndex_Object = MibTableColumn
h3cMplsExtVpnStatsVrfIndex = _H3cMplsExtVpnStatsVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 5, 1, 1),
    _H3cMplsExtVpnStatsVrfIndex_Type()
)
h3cMplsExtVpnStatsVrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMplsExtVpnStatsVrfIndex.setStatus("current")


class _H3cMplsExtVpnStatsVpnName_Type(OctetString):
    """Custom type h3cMplsExtVpnStatsVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cMplsExtVpnStatsVpnName_Type.__name__ = "OctetString"
_H3cMplsExtVpnStatsVpnName_Object = MibTableColumn
h3cMplsExtVpnStatsVpnName = _H3cMplsExtVpnStatsVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 5, 1, 2),
    _H3cMplsExtVpnStatsVpnName_Type()
)
h3cMplsExtVpnStatsVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtVpnStatsVpnName.setStatus("current")
_H3cMplsExtVpnStatsInOctets_Type = Counter64
_H3cMplsExtVpnStatsInOctets_Object = MibTableColumn
h3cMplsExtVpnStatsInOctets = _H3cMplsExtVpnStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 5, 1, 3),
    _H3cMplsExtVpnStatsInOctets_Type()
)
h3cMplsExtVpnStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtVpnStatsInOctets.setStatus("current")
_H3cMplsExtVpnStatsInPackets_Type = Counter64
_H3cMplsExtVpnStatsInPackets_Object = MibTableColumn
h3cMplsExtVpnStatsInPackets = _H3cMplsExtVpnStatsInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 5, 1, 4),
    _H3cMplsExtVpnStatsInPackets_Type()
)
h3cMplsExtVpnStatsInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtVpnStatsInPackets.setStatus("current")
_H3cMplsExtVpnStatsInErrors_Type = Counter64
_H3cMplsExtVpnStatsInErrors_Object = MibTableColumn
h3cMplsExtVpnStatsInErrors = _H3cMplsExtVpnStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 5, 1, 5),
    _H3cMplsExtVpnStatsInErrors_Type()
)
h3cMplsExtVpnStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtVpnStatsInErrors.setStatus("current")
_H3cMplsExtVpnStatsInDiscards_Type = Counter64
_H3cMplsExtVpnStatsInDiscards_Object = MibTableColumn
h3cMplsExtVpnStatsInDiscards = _H3cMplsExtVpnStatsInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 5, 1, 6),
    _H3cMplsExtVpnStatsInDiscards_Type()
)
h3cMplsExtVpnStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtVpnStatsInDiscards.setStatus("current")
_H3cMplsExtVpnStatsOutOctets_Type = Counter64
_H3cMplsExtVpnStatsOutOctets_Object = MibTableColumn
h3cMplsExtVpnStatsOutOctets = _H3cMplsExtVpnStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 5, 1, 7),
    _H3cMplsExtVpnStatsOutOctets_Type()
)
h3cMplsExtVpnStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtVpnStatsOutOctets.setStatus("current")
_H3cMplsExtVpnStatsOutPackets_Type = Counter64
_H3cMplsExtVpnStatsOutPackets_Object = MibTableColumn
h3cMplsExtVpnStatsOutPackets = _H3cMplsExtVpnStatsOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 5, 1, 8),
    _H3cMplsExtVpnStatsOutPackets_Type()
)
h3cMplsExtVpnStatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtVpnStatsOutPackets.setStatus("current")
_H3cMplsExtVpnStatsOutErrors_Type = Counter64
_H3cMplsExtVpnStatsOutErrors_Object = MibTableColumn
h3cMplsExtVpnStatsOutErrors = _H3cMplsExtVpnStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 5, 1, 9),
    _H3cMplsExtVpnStatsOutErrors_Type()
)
h3cMplsExtVpnStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtVpnStatsOutErrors.setStatus("current")
_H3cMplsExtVpnStatsOutDiscards_Type = Counter64
_H3cMplsExtVpnStatsOutDiscards_Object = MibTableColumn
h3cMplsExtVpnStatsOutDiscards = _H3cMplsExtVpnStatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 5, 1, 10),
    _H3cMplsExtVpnStatsOutDiscards_Type()
)
h3cMplsExtVpnStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtVpnStatsOutDiscards.setStatus("current")
_H3cMplsExtVpnTable_Object = MibTable
h3cMplsExtVpnTable = _H3cMplsExtVpnTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 6)
)
if mibBuilder.loadTexts:
    h3cMplsExtVpnTable.setStatus("current")
_H3cMplsExtVpnEntry_Object = MibTableRow
h3cMplsExtVpnEntry = _H3cMplsExtVpnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 6, 1)
)
h3cMplsExtVpnEntry.setIndexNames(
    (0, "H3C-MPLSEXT-MIB", "h3cMplsExtVpnName"),
)
if mibBuilder.loadTexts:
    h3cMplsExtVpnEntry.setStatus("current")


class _H3cMplsExtVpnName_Type(OctetString):
    """Custom type h3cMplsExtVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cMplsExtVpnName_Type.__name__ = "OctetString"
_H3cMplsExtVpnName_Object = MibTableColumn
h3cMplsExtVpnName = _H3cMplsExtVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 6, 1, 1),
    _H3cMplsExtVpnName_Type()
)
h3cMplsExtVpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMplsExtVpnName.setStatus("current")


class _H3cMplsExtVrfIndex_Type(Unsigned32):
    """Custom type h3cMplsExtVrfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_H3cMplsExtVrfIndex_Type.__name__ = "Unsigned32"
_H3cMplsExtVrfIndex_Object = MibTableColumn
h3cMplsExtVrfIndex = _H3cMplsExtVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 142, 1, 6, 1, 2),
    _H3cMplsExtVrfIndex_Type()
)
h3cMplsExtVrfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsExtVrfIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-MPLSEXT-MIB",
    **{"h3cMplsExt": h3cMplsExt,
       "h3cMplsExtObjects": h3cMplsExtObjects,
       "h3cMplsExtScalarGroup": h3cMplsExtScalarGroup,
       "h3cMplsExtLsrID": h3cMplsExtLsrID,
       "h3cMplsExtLdpStatus": h3cMplsExtLdpStatus,
       "h3cMplsExtTable": h3cMplsExtTable,
       "h3cMplsExtEntry": h3cMplsExtEntry,
       "h3cMplsExtIndex": h3cMplsExtIndex,
       "h3cMplsExtCapability": h3cMplsExtCapability,
       "h3cMplsExtMtu": h3cMplsExtMtu,
       "h3cMplsExtRowStatus": h3cMplsExtRowStatus,
       "h3cMplsExtLdpTable": h3cMplsExtLdpTable,
       "h3cMplsExtLdpEntry": h3cMplsExtLdpEntry,
       "h3cMplsExtLdpIndex": h3cMplsExtLdpIndex,
       "h3cMplsExtLdpCapability": h3cMplsExtLdpCapability,
       "h3cMplsExtLdpRowStatus": h3cMplsExtLdpRowStatus,
       "h3cMplsExtBfdTable": h3cMplsExtBfdTable,
       "h3cMplsExtBfdEntry": h3cMplsExtBfdEntry,
       "h3cMplsExtBfdLocalDiscr": h3cMplsExtBfdLocalDiscr,
       "h3cMplsExtBfdType": h3cMplsExtBfdType,
       "h3cMplsExtBfdBindIfIndex": h3cMplsExtBfdBindIfIndex,
       "h3cMplsExtBfdBindIfName": h3cMplsExtBfdBindIfName,
       "h3cMplsExtBfdXcIndex": h3cMplsExtBfdXcIndex,
       "h3cMplsExtBfdPwBackupFlag": h3cMplsExtBfdPwBackupFlag,
       "h3cMplsExtBfdPwId": h3cMplsExtBfdPwId,
       "h3cMplsExtBfdVsiIndex": h3cMplsExtBfdVsiIndex,
       "h3cMplsExtBfdPwPeerIpType": h3cMplsExtBfdPwPeerIpType,
       "h3cMplsExtBfdPwPeerIp": h3cMplsExtBfdPwPeerIp,
       "h3cMplsExtBfdPwSPE": h3cMplsExtBfdPwSPE,
       "h3cMplsExtBfdPwEncapType": h3cMplsExtBfdPwEncapType,
       "h3cMplsExtVpnStatsTable": h3cMplsExtVpnStatsTable,
       "h3cMplsExtVpnStatsEntry": h3cMplsExtVpnStatsEntry,
       "h3cMplsExtVpnStatsVrfIndex": h3cMplsExtVpnStatsVrfIndex,
       "h3cMplsExtVpnStatsVpnName": h3cMplsExtVpnStatsVpnName,
       "h3cMplsExtVpnStatsInOctets": h3cMplsExtVpnStatsInOctets,
       "h3cMplsExtVpnStatsInPackets": h3cMplsExtVpnStatsInPackets,
       "h3cMplsExtVpnStatsInErrors": h3cMplsExtVpnStatsInErrors,
       "h3cMplsExtVpnStatsInDiscards": h3cMplsExtVpnStatsInDiscards,
       "h3cMplsExtVpnStatsOutOctets": h3cMplsExtVpnStatsOutOctets,
       "h3cMplsExtVpnStatsOutPackets": h3cMplsExtVpnStatsOutPackets,
       "h3cMplsExtVpnStatsOutErrors": h3cMplsExtVpnStatsOutErrors,
       "h3cMplsExtVpnStatsOutDiscards": h3cMplsExtVpnStatsOutDiscards,
       "h3cMplsExtVpnTable": h3cMplsExtVpnTable,
       "h3cMplsExtVpnEntry": h3cMplsExtVpnEntry,
       "h3cMplsExtVpnName": h3cMplsExtVpnName,
       "h3cMplsExtVrfIndex": h3cMplsExtVrfIndex}
)
