# SNMP MIB module (HPN-ICF-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPN-ICF-ACL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:35:31 2025
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfAcl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8)
)
if mibBuilder.loadTexts:
    hpnicfAcl.setRevisions(
        ("2014-07-22 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RuleAction(TextualConvention, Integer32):
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
        *(("invalid", 1),
          ("permit", 2),
          ("deny", 3))
    )



class CounterClear(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("nouse", 2))
    )



class PortOp(TextualConvention, Integer32):
    status = "current"
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
        *(("invalid", 0),
          ("lt", 1),
          ("eq", 2),
          ("gt", 3),
          ("neq", 4),
          ("range", 5))
    )



class DSCPValue(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )



class TCPFlag(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("tcpack", 1),
          ("tcpfin", 2),
          ("tcppsh", 3),
          ("tcprst", 4),
          ("tcpsyn", 5),
          ("tcpurg", 6))
    )



class FragmentFlag(TextualConvention, Integer32):
    status = "current"
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
        *(("invalid", 0),
          ("fragment", 1),
          ("fragmentSubseq", 2),
          ("nonFragment", 3),
          ("nonSubseq", 4))
    )



class AddressFlag(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("t64SrcAddrPre64DestAddrPre", 1),
          ("t64SrcAddrPre64DestAddrSuf", 2),
          ("t64SrcAddrSuf64DestAddrPre", 3),
          ("t64SrcAddrSuf64DestAddrSuf", 4),
          ("t128SourceAddress", 5),
          ("t128DestinationAddress", 6))
    )



class DirectionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfAclMibObjects_ObjectIdentity = ObjectIdentity
hpnicfAclMibObjects = _HpnicfAclMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1)
)


class _HpnicfAclMode_Type(Integer32):
    """Custom type hpnicfAclMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkBased", 1),
          ("ipBased", 2))
    )


_HpnicfAclMode_Type.__name__ = "Integer32"
_HpnicfAclMode_Object = MibScalar
hpnicfAclMode = _HpnicfAclMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 1),
    _HpnicfAclMode_Type()
)
hpnicfAclMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfAclMode.setStatus("current")
_HpnicfAclNumGroupTable_Object = MibTable
hpnicfAclNumGroupTable = _HpnicfAclNumGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfAclNumGroupTable.setStatus("current")
_HpnicfAclNumGroupEntry_Object = MibTableRow
hpnicfAclNumGroupEntry = _HpnicfAclNumGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 2, 1)
)
hpnicfAclNumGroupEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNumGroupAclNum"),
)
if mibBuilder.loadTexts:
    hpnicfAclNumGroupEntry.setStatus("current")


class _HpnicfAclNumGroupAclNum_Type(Integer32):
    """Custom type hpnicfAclNumGroupAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 5999),
    )


_HpnicfAclNumGroupAclNum_Type.__name__ = "Integer32"
_HpnicfAclNumGroupAclNum_Object = MibTableColumn
hpnicfAclNumGroupAclNum = _HpnicfAclNumGroupAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 2, 1, 1),
    _HpnicfAclNumGroupAclNum_Type()
)
hpnicfAclNumGroupAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclNumGroupAclNum.setStatus("current")


class _HpnicfAclNumGroupMatchOrder_Type(Integer32):
    """Custom type hpnicfAclNumGroupMatchOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 1),
          ("auto", 2))
    )


_HpnicfAclNumGroupMatchOrder_Type.__name__ = "Integer32"
_HpnicfAclNumGroupMatchOrder_Object = MibTableColumn
hpnicfAclNumGroupMatchOrder = _HpnicfAclNumGroupMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 2, 1, 2),
    _HpnicfAclNumGroupMatchOrder_Type()
)
hpnicfAclNumGroupMatchOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNumGroupMatchOrder.setStatus("current")
_HpnicfAclNumGroupSubitemNum_Type = Integer32
_HpnicfAclNumGroupSubitemNum_Object = MibTableColumn
hpnicfAclNumGroupSubitemNum = _HpnicfAclNumGroupSubitemNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 2, 1, 3),
    _HpnicfAclNumGroupSubitemNum_Type()
)
hpnicfAclNumGroupSubitemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclNumGroupSubitemNum.setStatus("current")


class _HpnicfAclNumGroupDescription_Type(OctetString):
    """Custom type hpnicfAclNumGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfAclNumGroupDescription_Type.__name__ = "OctetString"
_HpnicfAclNumGroupDescription_Object = MibTableColumn
hpnicfAclNumGroupDescription = _HpnicfAclNumGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 2, 1, 4),
    _HpnicfAclNumGroupDescription_Type()
)
hpnicfAclNumGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfAclNumGroupDescription.setStatus("current")


class _HpnicfAclNumGroupCountClear_Type(Integer32):
    """Custom type hpnicfAclNumGroupCountClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("nouse", 2))
    )


_HpnicfAclNumGroupCountClear_Type.__name__ = "Integer32"
_HpnicfAclNumGroupCountClear_Object = MibTableColumn
hpnicfAclNumGroupCountClear = _HpnicfAclNumGroupCountClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 2, 1, 5),
    _HpnicfAclNumGroupCountClear_Type()
)
hpnicfAclNumGroupCountClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNumGroupCountClear.setStatus("current")
_HpnicfAclNumGroupRowStatus_Type = RowStatus
_HpnicfAclNumGroupRowStatus_Object = MibTableColumn
hpnicfAclNumGroupRowStatus = _HpnicfAclNumGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 2, 1, 6),
    _HpnicfAclNumGroupRowStatus_Type()
)
hpnicfAclNumGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNumGroupRowStatus.setStatus("current")
_HpnicfAclNameGroupTable_Object = MibTable
hpnicfAclNameGroupTable = _HpnicfAclNameGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfAclNameGroupTable.setStatus("current")
_HpnicfAclNameGroupEntry_Object = MibTableRow
hpnicfAclNameGroupEntry = _HpnicfAclNameGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 3, 1)
)
hpnicfAclNameGroupEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNameGroupIndex"),
)
if mibBuilder.loadTexts:
    hpnicfAclNameGroupEntry.setStatus("current")


class _HpnicfAclNameGroupIndex_Type(Integer32):
    """Custom type hpnicfAclNameGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfAclNameGroupIndex_Type.__name__ = "Integer32"
_HpnicfAclNameGroupIndex_Object = MibTableColumn
hpnicfAclNameGroupIndex = _HpnicfAclNameGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 3, 1, 1),
    _HpnicfAclNameGroupIndex_Type()
)
hpnicfAclNameGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclNameGroupIndex.setStatus("current")


class _HpnicfAclNameGroupCreateName_Type(OctetString):
    """Custom type hpnicfAclNameGroupCreateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclNameGroupCreateName_Type.__name__ = "OctetString"
_HpnicfAclNameGroupCreateName_Object = MibTableColumn
hpnicfAclNameGroupCreateName = _HpnicfAclNameGroupCreateName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 3, 1, 2),
    _HpnicfAclNameGroupCreateName_Type()
)
hpnicfAclNameGroupCreateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNameGroupCreateName.setStatus("current")


class _HpnicfAclNameGroupTypes_Type(Integer32):
    """Custom type hpnicfAclNameGroupTypes based on Integer32"""
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
        *(("basic", 1),
          ("advanced", 2),
          ("ifBased", 3),
          ("link", 4),
          ("user", 5))
    )


_HpnicfAclNameGroupTypes_Type.__name__ = "Integer32"
_HpnicfAclNameGroupTypes_Object = MibTableColumn
hpnicfAclNameGroupTypes = _HpnicfAclNameGroupTypes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 3, 1, 3),
    _HpnicfAclNameGroupTypes_Type()
)
hpnicfAclNameGroupTypes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNameGroupTypes.setStatus("current")


class _HpnicfAclNameGroupMatchOrder_Type(Integer32):
    """Custom type hpnicfAclNameGroupMatchOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 1),
          ("auto", 2))
    )


_HpnicfAclNameGroupMatchOrder_Type.__name__ = "Integer32"
_HpnicfAclNameGroupMatchOrder_Object = MibTableColumn
hpnicfAclNameGroupMatchOrder = _HpnicfAclNameGroupMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 3, 1, 4),
    _HpnicfAclNameGroupMatchOrder_Type()
)
hpnicfAclNameGroupMatchOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNameGroupMatchOrder.setStatus("current")


class _HpnicfAclNameGroupSubitemNum_Type(Integer32):
    """Custom type hpnicfAclNameGroupSubitemNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HpnicfAclNameGroupSubitemNum_Type.__name__ = "Integer32"
_HpnicfAclNameGroupSubitemNum_Object = MibTableColumn
hpnicfAclNameGroupSubitemNum = _HpnicfAclNameGroupSubitemNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 3, 1, 5),
    _HpnicfAclNameGroupSubitemNum_Type()
)
hpnicfAclNameGroupSubitemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclNameGroupSubitemNum.setStatus("current")
_HpnicfAclNameGroupRowStatus_Type = RowStatus
_HpnicfAclNameGroupRowStatus_Object = MibTableColumn
hpnicfAclNameGroupRowStatus = _HpnicfAclNameGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 3, 1, 6),
    _HpnicfAclNameGroupRowStatus_Type()
)
hpnicfAclNameGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNameGroupRowStatus.setStatus("current")
_HpnicfAclBasicRuleTable_Object = MibTable
hpnicfAclBasicRuleTable = _HpnicfAclBasicRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfAclBasicRuleTable.setStatus("current")
_HpnicfAclBasicRuleEntry_Object = MibTableRow
hpnicfAclBasicRuleEntry = _HpnicfAclBasicRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 4, 1)
)
hpnicfAclBasicRuleEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclBasicAclNum"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclBasicSubitem"),
)
if mibBuilder.loadTexts:
    hpnicfAclBasicRuleEntry.setStatus("current")


class _HpnicfAclBasicAclNum_Type(Integer32):
    """Custom type hpnicfAclBasicAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfAclBasicAclNum_Type.__name__ = "Integer32"
_HpnicfAclBasicAclNum_Object = MibTableColumn
hpnicfAclBasicAclNum = _HpnicfAclBasicAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 4, 1, 1),
    _HpnicfAclBasicAclNum_Type()
)
hpnicfAclBasicAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclBasicAclNum.setStatus("current")


class _HpnicfAclBasicSubitem_Type(Integer32):
    """Custom type hpnicfAclBasicSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclBasicSubitem_Type.__name__ = "Integer32"
_HpnicfAclBasicSubitem_Object = MibTableColumn
hpnicfAclBasicSubitem = _HpnicfAclBasicSubitem_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 4, 1, 2),
    _HpnicfAclBasicSubitem_Type()
)
hpnicfAclBasicSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclBasicSubitem.setStatus("current")


class _HpnicfAclBasicAct_Type(Integer32):
    """Custom type hpnicfAclBasicAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_HpnicfAclBasicAct_Type.__name__ = "Integer32"
_HpnicfAclBasicAct_Object = MibTableColumn
hpnicfAclBasicAct = _HpnicfAclBasicAct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 4, 1, 3),
    _HpnicfAclBasicAct_Type()
)
hpnicfAclBasicAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclBasicAct.setStatus("current")
_HpnicfAclBasicSrcIp_Type = IpAddress
_HpnicfAclBasicSrcIp_Object = MibTableColumn
hpnicfAclBasicSrcIp = _HpnicfAclBasicSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 4, 1, 4),
    _HpnicfAclBasicSrcIp_Type()
)
hpnicfAclBasicSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclBasicSrcIp.setStatus("current")
_HpnicfAclBasicSrcWild_Type = IpAddress
_HpnicfAclBasicSrcWild_Object = MibTableColumn
hpnicfAclBasicSrcWild = _HpnicfAclBasicSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 4, 1, 5),
    _HpnicfAclBasicSrcWild_Type()
)
hpnicfAclBasicSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclBasicSrcWild.setStatus("current")


class _HpnicfAclBasicTimeRangeName_Type(OctetString):
    """Custom type hpnicfAclBasicTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclBasicTimeRangeName_Type.__name__ = "OctetString"
_HpnicfAclBasicTimeRangeName_Object = MibTableColumn
hpnicfAclBasicTimeRangeName = _HpnicfAclBasicTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 4, 1, 6),
    _HpnicfAclBasicTimeRangeName_Type()
)
hpnicfAclBasicTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclBasicTimeRangeName.setStatus("current")
_HpnicfAclBasicFragments_Type = TruthValue
_HpnicfAclBasicFragments_Object = MibTableColumn
hpnicfAclBasicFragments = _HpnicfAclBasicFragments_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 4, 1, 7),
    _HpnicfAclBasicFragments_Type()
)
hpnicfAclBasicFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclBasicFragments.setStatus("current")
_HpnicfAclBasicLog_Type = TruthValue
_HpnicfAclBasicLog_Object = MibTableColumn
hpnicfAclBasicLog = _HpnicfAclBasicLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 4, 1, 8),
    _HpnicfAclBasicLog_Type()
)
hpnicfAclBasicLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclBasicLog.setStatus("current")
_HpnicfAclBasicEnable_Type = TruthValue
_HpnicfAclBasicEnable_Object = MibTableColumn
hpnicfAclBasicEnable = _HpnicfAclBasicEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 4, 1, 9),
    _HpnicfAclBasicEnable_Type()
)
hpnicfAclBasicEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclBasicEnable.setStatus("current")
_HpnicfAclBasicCount_Type = Counter32
_HpnicfAclBasicCount_Object = MibTableColumn
hpnicfAclBasicCount = _HpnicfAclBasicCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 4, 1, 10),
    _HpnicfAclBasicCount_Type()
)
hpnicfAclBasicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclBasicCount.setStatus("current")


class _HpnicfAclBasicCountClear_Type(Integer32):
    """Custom type hpnicfAclBasicCountClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("nouse", 2))
    )


_HpnicfAclBasicCountClear_Type.__name__ = "Integer32"
_HpnicfAclBasicCountClear_Object = MibTableColumn
hpnicfAclBasicCountClear = _HpnicfAclBasicCountClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 4, 1, 11),
    _HpnicfAclBasicCountClear_Type()
)
hpnicfAclBasicCountClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclBasicCountClear.setStatus("current")
_HpnicfAclBasicRowStatus_Type = RowStatus
_HpnicfAclBasicRowStatus_Object = MibTableColumn
hpnicfAclBasicRowStatus = _HpnicfAclBasicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 4, 1, 12),
    _HpnicfAclBasicRowStatus_Type()
)
hpnicfAclBasicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclBasicRowStatus.setStatus("current")
_HpnicfAclAdvancedRuleTable_Object = MibTable
hpnicfAclAdvancedRuleTable = _HpnicfAclAdvancedRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfAclAdvancedRuleTable.setStatus("current")
_HpnicfAclAdvancedRuleEntry_Object = MibTableRow
hpnicfAclAdvancedRuleEntry = _HpnicfAclAdvancedRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1)
)
hpnicfAclAdvancedRuleEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclAdvancedAclNum"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclAdvancedSubitem"),
)
if mibBuilder.loadTexts:
    hpnicfAclAdvancedRuleEntry.setStatus("current")


class _HpnicfAclAdvancedAclNum_Type(Integer32):
    """Custom type hpnicfAclAdvancedAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfAclAdvancedAclNum_Type.__name__ = "Integer32"
_HpnicfAclAdvancedAclNum_Object = MibTableColumn
hpnicfAclAdvancedAclNum = _HpnicfAclAdvancedAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 1),
    _HpnicfAclAdvancedAclNum_Type()
)
hpnicfAclAdvancedAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedAclNum.setStatus("current")


class _HpnicfAclAdvancedSubitem_Type(Integer32):
    """Custom type hpnicfAclAdvancedSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclAdvancedSubitem_Type.__name__ = "Integer32"
_HpnicfAclAdvancedSubitem_Object = MibTableColumn
hpnicfAclAdvancedSubitem = _HpnicfAclAdvancedSubitem_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 2),
    _HpnicfAclAdvancedSubitem_Type()
)
hpnicfAclAdvancedSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedSubitem.setStatus("current")


class _HpnicfAclAdvancedAct_Type(Integer32):
    """Custom type hpnicfAclAdvancedAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_HpnicfAclAdvancedAct_Type.__name__ = "Integer32"
_HpnicfAclAdvancedAct_Object = MibTableColumn
hpnicfAclAdvancedAct = _HpnicfAclAdvancedAct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 3),
    _HpnicfAclAdvancedAct_Type()
)
hpnicfAclAdvancedAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedAct.setStatus("current")


class _HpnicfAclAdvancedProtocol_Type(Integer32):
    """Custom type hpnicfAclAdvancedProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfAclAdvancedProtocol_Type.__name__ = "Integer32"
_HpnicfAclAdvancedProtocol_Object = MibTableColumn
hpnicfAclAdvancedProtocol = _HpnicfAclAdvancedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 4),
    _HpnicfAclAdvancedProtocol_Type()
)
hpnicfAclAdvancedProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedProtocol.setStatus("current")
_HpnicfAclAdvancedSrcIp_Type = IpAddress
_HpnicfAclAdvancedSrcIp_Object = MibTableColumn
hpnicfAclAdvancedSrcIp = _HpnicfAclAdvancedSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 5),
    _HpnicfAclAdvancedSrcIp_Type()
)
hpnicfAclAdvancedSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedSrcIp.setStatus("current")
_HpnicfAclAdvancedSrcWild_Type = IpAddress
_HpnicfAclAdvancedSrcWild_Object = MibTableColumn
hpnicfAclAdvancedSrcWild = _HpnicfAclAdvancedSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 6),
    _HpnicfAclAdvancedSrcWild_Type()
)
hpnicfAclAdvancedSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedSrcWild.setStatus("current")


class _HpnicfAclAdvancedSrcOp_Type(Integer32):
    """Custom type hpnicfAclAdvancedSrcOp based on Integer32"""
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
        *(("invalid", 0),
          ("lt", 1),
          ("eq", 2),
          ("gt", 3),
          ("neq", 4),
          ("range", 5))
    )


_HpnicfAclAdvancedSrcOp_Type.__name__ = "Integer32"
_HpnicfAclAdvancedSrcOp_Object = MibTableColumn
hpnicfAclAdvancedSrcOp = _HpnicfAclAdvancedSrcOp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 7),
    _HpnicfAclAdvancedSrcOp_Type()
)
hpnicfAclAdvancedSrcOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedSrcOp.setStatus("current")


class _HpnicfAclAdvancedSrcPort1_Type(Integer32):
    """Custom type hpnicfAclAdvancedSrcPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclAdvancedSrcPort1_Type.__name__ = "Integer32"
_HpnicfAclAdvancedSrcPort1_Object = MibTableColumn
hpnicfAclAdvancedSrcPort1 = _HpnicfAclAdvancedSrcPort1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 8),
    _HpnicfAclAdvancedSrcPort1_Type()
)
hpnicfAclAdvancedSrcPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedSrcPort1.setStatus("current")


class _HpnicfAclAdvancedSrcPort2_Type(Integer32):
    """Custom type hpnicfAclAdvancedSrcPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclAdvancedSrcPort2_Type.__name__ = "Integer32"
_HpnicfAclAdvancedSrcPort2_Object = MibTableColumn
hpnicfAclAdvancedSrcPort2 = _HpnicfAclAdvancedSrcPort2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 9),
    _HpnicfAclAdvancedSrcPort2_Type()
)
hpnicfAclAdvancedSrcPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedSrcPort2.setStatus("current")
_HpnicfAclAdvancedDestIp_Type = IpAddress
_HpnicfAclAdvancedDestIp_Object = MibTableColumn
hpnicfAclAdvancedDestIp = _HpnicfAclAdvancedDestIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 10),
    _HpnicfAclAdvancedDestIp_Type()
)
hpnicfAclAdvancedDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedDestIp.setStatus("current")
_HpnicfAclAdvancedDestWild_Type = IpAddress
_HpnicfAclAdvancedDestWild_Object = MibTableColumn
hpnicfAclAdvancedDestWild = _HpnicfAclAdvancedDestWild_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 11),
    _HpnicfAclAdvancedDestWild_Type()
)
hpnicfAclAdvancedDestWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedDestWild.setStatus("current")


class _HpnicfAclAdvancedDestOp_Type(Integer32):
    """Custom type hpnicfAclAdvancedDestOp based on Integer32"""
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
        *(("invalid", 0),
          ("lt", 1),
          ("eq", 2),
          ("gt", 3),
          ("neq", 4),
          ("range", 5))
    )


_HpnicfAclAdvancedDestOp_Type.__name__ = "Integer32"
_HpnicfAclAdvancedDestOp_Object = MibTableColumn
hpnicfAclAdvancedDestOp = _HpnicfAclAdvancedDestOp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 12),
    _HpnicfAclAdvancedDestOp_Type()
)
hpnicfAclAdvancedDestOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedDestOp.setStatus("current")


class _HpnicfAclAdvancedDestPort1_Type(Integer32):
    """Custom type hpnicfAclAdvancedDestPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclAdvancedDestPort1_Type.__name__ = "Integer32"
_HpnicfAclAdvancedDestPort1_Object = MibTableColumn
hpnicfAclAdvancedDestPort1 = _HpnicfAclAdvancedDestPort1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 13),
    _HpnicfAclAdvancedDestPort1_Type()
)
hpnicfAclAdvancedDestPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedDestPort1.setStatus("current")


class _HpnicfAclAdvancedDestPort2_Type(Integer32):
    """Custom type hpnicfAclAdvancedDestPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclAdvancedDestPort2_Type.__name__ = "Integer32"
_HpnicfAclAdvancedDestPort2_Object = MibTableColumn
hpnicfAclAdvancedDestPort2 = _HpnicfAclAdvancedDestPort2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 14),
    _HpnicfAclAdvancedDestPort2_Type()
)
hpnicfAclAdvancedDestPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedDestPort2.setStatus("current")


class _HpnicfAclAdvancedPrecedence_Type(Integer32):
    """Custom type hpnicfAclAdvancedPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfAclAdvancedPrecedence_Type.__name__ = "Integer32"
_HpnicfAclAdvancedPrecedence_Object = MibTableColumn
hpnicfAclAdvancedPrecedence = _HpnicfAclAdvancedPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 15),
    _HpnicfAclAdvancedPrecedence_Type()
)
hpnicfAclAdvancedPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedPrecedence.setStatus("current")


class _HpnicfAclAdvancedTos_Type(Integer32):
    """Custom type hpnicfAclAdvancedTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_HpnicfAclAdvancedTos_Type.__name__ = "Integer32"
_HpnicfAclAdvancedTos_Object = MibTableColumn
hpnicfAclAdvancedTos = _HpnicfAclAdvancedTos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 16),
    _HpnicfAclAdvancedTos_Type()
)
hpnicfAclAdvancedTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedTos.setStatus("current")


class _HpnicfAclAdvancedDscp_Type(Integer32):
    """Custom type hpnicfAclAdvancedDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfAclAdvancedDscp_Type.__name__ = "Integer32"
_HpnicfAclAdvancedDscp_Object = MibTableColumn
hpnicfAclAdvancedDscp = _HpnicfAclAdvancedDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 17),
    _HpnicfAclAdvancedDscp_Type()
)
hpnicfAclAdvancedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedDscp.setStatus("current")


class _HpnicfAclAdvancedEstablish_Type(TruthValue):
    """Custom type hpnicfAclAdvancedEstablish based on TruthValue"""
    defaultValue = 2


_HpnicfAclAdvancedEstablish_Type.__name__ = "TruthValue"
_HpnicfAclAdvancedEstablish_Object = MibTableColumn
hpnicfAclAdvancedEstablish = _HpnicfAclAdvancedEstablish_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 18),
    _HpnicfAclAdvancedEstablish_Type()
)
hpnicfAclAdvancedEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedEstablish.setStatus("current")


class _HpnicfAclAdvancedTimeRangeName_Type(OctetString):
    """Custom type hpnicfAclAdvancedTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclAdvancedTimeRangeName_Type.__name__ = "OctetString"
_HpnicfAclAdvancedTimeRangeName_Object = MibTableColumn
hpnicfAclAdvancedTimeRangeName = _HpnicfAclAdvancedTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 19),
    _HpnicfAclAdvancedTimeRangeName_Type()
)
hpnicfAclAdvancedTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedTimeRangeName.setStatus("current")


class _HpnicfAclAdvancedIcmpType_Type(Integer32):
    """Custom type hpnicfAclAdvancedIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfAclAdvancedIcmpType_Type.__name__ = "Integer32"
_HpnicfAclAdvancedIcmpType_Object = MibTableColumn
hpnicfAclAdvancedIcmpType = _HpnicfAclAdvancedIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 20),
    _HpnicfAclAdvancedIcmpType_Type()
)
hpnicfAclAdvancedIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedIcmpType.setStatus("current")


class _HpnicfAclAdvancedIcmpCode_Type(Integer32):
    """Custom type hpnicfAclAdvancedIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfAclAdvancedIcmpCode_Type.__name__ = "Integer32"
_HpnicfAclAdvancedIcmpCode_Object = MibTableColumn
hpnicfAclAdvancedIcmpCode = _HpnicfAclAdvancedIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 21),
    _HpnicfAclAdvancedIcmpCode_Type()
)
hpnicfAclAdvancedIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedIcmpCode.setStatus("current")
_HpnicfAclAdvancedFragments_Type = TruthValue
_HpnicfAclAdvancedFragments_Object = MibTableColumn
hpnicfAclAdvancedFragments = _HpnicfAclAdvancedFragments_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 22),
    _HpnicfAclAdvancedFragments_Type()
)
hpnicfAclAdvancedFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedFragments.setStatus("current")
_HpnicfAclAdvancedLog_Type = TruthValue
_HpnicfAclAdvancedLog_Object = MibTableColumn
hpnicfAclAdvancedLog = _HpnicfAclAdvancedLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 23),
    _HpnicfAclAdvancedLog_Type()
)
hpnicfAclAdvancedLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedLog.setStatus("current")
_HpnicfAclAdvancedEnable_Type = TruthValue
_HpnicfAclAdvancedEnable_Object = MibTableColumn
hpnicfAclAdvancedEnable = _HpnicfAclAdvancedEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 24),
    _HpnicfAclAdvancedEnable_Type()
)
hpnicfAclAdvancedEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedEnable.setStatus("current")
_HpnicfAclAdvancedCount_Type = Counter32
_HpnicfAclAdvancedCount_Object = MibTableColumn
hpnicfAclAdvancedCount = _HpnicfAclAdvancedCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 25),
    _HpnicfAclAdvancedCount_Type()
)
hpnicfAclAdvancedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedCount.setStatus("current")


class _HpnicfAclAdvancedCountClear_Type(Integer32):
    """Custom type hpnicfAclAdvancedCountClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("nouse", 2))
    )


_HpnicfAclAdvancedCountClear_Type.__name__ = "Integer32"
_HpnicfAclAdvancedCountClear_Object = MibTableColumn
hpnicfAclAdvancedCountClear = _HpnicfAclAdvancedCountClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 26),
    _HpnicfAclAdvancedCountClear_Type()
)
hpnicfAclAdvancedCountClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedCountClear.setStatus("current")
_HpnicfAclAdvancedRowStatus_Type = RowStatus
_HpnicfAclAdvancedRowStatus_Object = MibTableColumn
hpnicfAclAdvancedRowStatus = _HpnicfAclAdvancedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 5, 1, 27),
    _HpnicfAclAdvancedRowStatus_Type()
)
hpnicfAclAdvancedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclAdvancedRowStatus.setStatus("current")
_HpnicfAclIfRuleTable_Object = MibTable
hpnicfAclIfRuleTable = _HpnicfAclIfRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfAclIfRuleTable.setStatus("current")
_HpnicfAclIfRuleEntry_Object = MibTableRow
hpnicfAclIfRuleEntry = _HpnicfAclIfRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 6, 1)
)
hpnicfAclIfRuleEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclIfAclNum"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclIfSubitem"),
)
if mibBuilder.loadTexts:
    hpnicfAclIfRuleEntry.setStatus("current")


class _HpnicfAclIfAclNum_Type(Integer32):
    """Custom type hpnicfAclIfAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 1999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfAclIfAclNum_Type.__name__ = "Integer32"
_HpnicfAclIfAclNum_Object = MibTableColumn
hpnicfAclIfAclNum = _HpnicfAclIfAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 6, 1, 1),
    _HpnicfAclIfAclNum_Type()
)
hpnicfAclIfAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclIfAclNum.setStatus("current")


class _HpnicfAclIfSubitem_Type(Integer32):
    """Custom type hpnicfAclIfSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclIfSubitem_Type.__name__ = "Integer32"
_HpnicfAclIfSubitem_Object = MibTableColumn
hpnicfAclIfSubitem = _HpnicfAclIfSubitem_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 6, 1, 2),
    _HpnicfAclIfSubitem_Type()
)
hpnicfAclIfSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclIfSubitem.setStatus("current")


class _HpnicfAclIfAct_Type(Integer32):
    """Custom type hpnicfAclIfAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_HpnicfAclIfAct_Type.__name__ = "Integer32"
_HpnicfAclIfAct_Object = MibTableColumn
hpnicfAclIfAct = _HpnicfAclIfAct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 6, 1, 3),
    _HpnicfAclIfAct_Type()
)
hpnicfAclIfAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIfAct.setStatus("current")


class _HpnicfAclIfIndex_Type(Integer32):
    """Custom type hpnicfAclIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfAclIfIndex_Type.__name__ = "Integer32"
_HpnicfAclIfIndex_Object = MibTableColumn
hpnicfAclIfIndex = _HpnicfAclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 6, 1, 4),
    _HpnicfAclIfIndex_Type()
)
hpnicfAclIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIfIndex.setStatus("current")
_HpnicfAclIfAny_Type = TruthValue
_HpnicfAclIfAny_Object = MibTableColumn
hpnicfAclIfAny = _HpnicfAclIfAny_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 6, 1, 5),
    _HpnicfAclIfAny_Type()
)
hpnicfAclIfAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIfAny.setStatus("current")


class _HpnicfAclIfTimeRangeName_Type(OctetString):
    """Custom type hpnicfAclIfTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclIfTimeRangeName_Type.__name__ = "OctetString"
_HpnicfAclIfTimeRangeName_Object = MibTableColumn
hpnicfAclIfTimeRangeName = _HpnicfAclIfTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 6, 1, 6),
    _HpnicfAclIfTimeRangeName_Type()
)
hpnicfAclIfTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIfTimeRangeName.setStatus("current")
_HpnicfAclIfLog_Type = TruthValue
_HpnicfAclIfLog_Object = MibTableColumn
hpnicfAclIfLog = _HpnicfAclIfLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 6, 1, 7),
    _HpnicfAclIfLog_Type()
)
hpnicfAclIfLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIfLog.setStatus("current")
_HpnicfAclIfEnable_Type = TruthValue
_HpnicfAclIfEnable_Object = MibTableColumn
hpnicfAclIfEnable = _HpnicfAclIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 6, 1, 8),
    _HpnicfAclIfEnable_Type()
)
hpnicfAclIfEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclIfEnable.setStatus("current")
_HpnicfAclIfCount_Type = Counter32
_HpnicfAclIfCount_Object = MibTableColumn
hpnicfAclIfCount = _HpnicfAclIfCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 6, 1, 9),
    _HpnicfAclIfCount_Type()
)
hpnicfAclIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclIfCount.setStatus("current")


class _HpnicfAclIfCountClear_Type(Integer32):
    """Custom type hpnicfAclIfCountClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("nouse", 2))
    )


_HpnicfAclIfCountClear_Type.__name__ = "Integer32"
_HpnicfAclIfCountClear_Object = MibTableColumn
hpnicfAclIfCountClear = _HpnicfAclIfCountClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 6, 1, 10),
    _HpnicfAclIfCountClear_Type()
)
hpnicfAclIfCountClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIfCountClear.setStatus("current")
_HpnicfAclIfRowStatus_Type = RowStatus
_HpnicfAclIfRowStatus_Object = MibTableColumn
hpnicfAclIfRowStatus = _HpnicfAclIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 6, 1, 11),
    _HpnicfAclIfRowStatus_Type()
)
hpnicfAclIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIfRowStatus.setStatus("current")
_HpnicfAclLinkTable_Object = MibTable
hpnicfAclLinkTable = _HpnicfAclLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfAclLinkTable.setStatus("current")
_HpnicfAclLinkEntry_Object = MibTableRow
hpnicfAclLinkEntry = _HpnicfAclLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1)
)
hpnicfAclLinkEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclLinkAclNum"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclLinkSubitem"),
)
if mibBuilder.loadTexts:
    hpnicfAclLinkEntry.setStatus("current")


class _HpnicfAclLinkAclNum_Type(Integer32):
    """Custom type hpnicfAclLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfAclLinkAclNum_Type.__name__ = "Integer32"
_HpnicfAclLinkAclNum_Object = MibTableColumn
hpnicfAclLinkAclNum = _HpnicfAclLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 1),
    _HpnicfAclLinkAclNum_Type()
)
hpnicfAclLinkAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclLinkAclNum.setStatus("current")


class _HpnicfAclLinkSubitem_Type(Integer32):
    """Custom type hpnicfAclLinkSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclLinkSubitem_Type.__name__ = "Integer32"
_HpnicfAclLinkSubitem_Object = MibTableColumn
hpnicfAclLinkSubitem = _HpnicfAclLinkSubitem_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 2),
    _HpnicfAclLinkSubitem_Type()
)
hpnicfAclLinkSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclLinkSubitem.setStatus("current")


class _HpnicfAclLinkAct_Type(Integer32):
    """Custom type hpnicfAclLinkAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_HpnicfAclLinkAct_Type.__name__ = "Integer32"
_HpnicfAclLinkAct_Object = MibTableColumn
hpnicfAclLinkAct = _HpnicfAclLinkAct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 3),
    _HpnicfAclLinkAct_Type()
)
hpnicfAclLinkAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkAct.setStatus("current")


class _HpnicfAclLinkProtocol_Type(Integer32):
    """Custom type hpnicfAclLinkProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2048,
              2054,
              32821,
              34887,
              34915,
              34916)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("ip", 2048),
          ("arp", 2054),
          ("rarp", 32821),
          ("mpls", 34887),
          ("pppoeControl", 34915),
          ("pppoeData", 34916))
    )


_HpnicfAclLinkProtocol_Type.__name__ = "Integer32"
_HpnicfAclLinkProtocol_Object = MibTableColumn
hpnicfAclLinkProtocol = _HpnicfAclLinkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 4),
    _HpnicfAclLinkProtocol_Type()
)
hpnicfAclLinkProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkProtocol.setStatus("current")


class _HpnicfAclLinkFormatType_Type(Integer32):
    """Custom type hpnicfAclLinkFormatType based on Integer32"""
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
        *(("invalid", 0),
          ("ethernetII", 1),
          ("snap", 2),
          ("ieee802Dot3And2", 3),
          ("ieee802Dot3", 4))
    )


_HpnicfAclLinkFormatType_Type.__name__ = "Integer32"
_HpnicfAclLinkFormatType_Object = MibTableColumn
hpnicfAclLinkFormatType = _HpnicfAclLinkFormatType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 5),
    _HpnicfAclLinkFormatType_Type()
)
hpnicfAclLinkFormatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkFormatType.setStatus("current")


class _HpnicfAclLinkVlanTag_Type(Integer32):
    """Custom type hpnicfAclLinkVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("tagged", 1),
          ("untagged", 2))
    )


_HpnicfAclLinkVlanTag_Type.__name__ = "Integer32"
_HpnicfAclLinkVlanTag_Object = MibTableColumn
hpnicfAclLinkVlanTag = _HpnicfAclLinkVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 6),
    _HpnicfAclLinkVlanTag_Type()
)
hpnicfAclLinkVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkVlanTag.setStatus("current")


class _HpnicfAclLinkVlanPri_Type(Integer32):
    """Custom type hpnicfAclLinkVlanPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfAclLinkVlanPri_Type.__name__ = "Integer32"
_HpnicfAclLinkVlanPri_Object = MibTableColumn
hpnicfAclLinkVlanPri = _HpnicfAclLinkVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 7),
    _HpnicfAclLinkVlanPri_Type()
)
hpnicfAclLinkVlanPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkVlanPri.setStatus("current")


class _HpnicfAclLinkSrcVlanId_Type(Integer32):
    """Custom type hpnicfAclLinkSrcVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfAclLinkSrcVlanId_Type.__name__ = "Integer32"
_HpnicfAclLinkSrcVlanId_Object = MibTableColumn
hpnicfAclLinkSrcVlanId = _HpnicfAclLinkSrcVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 8),
    _HpnicfAclLinkSrcVlanId_Type()
)
hpnicfAclLinkSrcVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkSrcVlanId.setStatus("current")
_HpnicfAclLinkSrcMac_Type = MacAddress
_HpnicfAclLinkSrcMac_Object = MibTableColumn
hpnicfAclLinkSrcMac = _HpnicfAclLinkSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 9),
    _HpnicfAclLinkSrcMac_Type()
)
hpnicfAclLinkSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkSrcMac.setStatus("current")
_HpnicfAclLinkSrcMacWild_Type = MacAddress
_HpnicfAclLinkSrcMacWild_Object = MibTableColumn
hpnicfAclLinkSrcMacWild = _HpnicfAclLinkSrcMacWild_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 10),
    _HpnicfAclLinkSrcMacWild_Type()
)
hpnicfAclLinkSrcMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkSrcMacWild.setStatus("current")


class _HpnicfAclLinkSrcIfIndex_Type(Integer32):
    """Custom type hpnicfAclLinkSrcIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfAclLinkSrcIfIndex_Type.__name__ = "Integer32"
_HpnicfAclLinkSrcIfIndex_Object = MibTableColumn
hpnicfAclLinkSrcIfIndex = _HpnicfAclLinkSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 11),
    _HpnicfAclLinkSrcIfIndex_Type()
)
hpnicfAclLinkSrcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkSrcIfIndex.setStatus("current")
_HpnicfAclLinkSrcAny_Type = TruthValue
_HpnicfAclLinkSrcAny_Object = MibTableColumn
hpnicfAclLinkSrcAny = _HpnicfAclLinkSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 12),
    _HpnicfAclLinkSrcAny_Type()
)
hpnicfAclLinkSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkSrcAny.setStatus("current")


class _HpnicfAclLinkDestVlanId_Type(Integer32):
    """Custom type hpnicfAclLinkDestVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfAclLinkDestVlanId_Type.__name__ = "Integer32"
_HpnicfAclLinkDestVlanId_Object = MibTableColumn
hpnicfAclLinkDestVlanId = _HpnicfAclLinkDestVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 13),
    _HpnicfAclLinkDestVlanId_Type()
)
hpnicfAclLinkDestVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkDestVlanId.setStatus("current")
_HpnicfAclLinkDestMac_Type = MacAddress
_HpnicfAclLinkDestMac_Object = MibTableColumn
hpnicfAclLinkDestMac = _HpnicfAclLinkDestMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 14),
    _HpnicfAclLinkDestMac_Type()
)
hpnicfAclLinkDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkDestMac.setStatus("current")
_HpnicfAclLinkDestMacWild_Type = MacAddress
_HpnicfAclLinkDestMacWild_Object = MibTableColumn
hpnicfAclLinkDestMacWild = _HpnicfAclLinkDestMacWild_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 15),
    _HpnicfAclLinkDestMacWild_Type()
)
hpnicfAclLinkDestMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkDestMacWild.setStatus("current")


class _HpnicfAclLinkDestIfIndex_Type(Integer32):
    """Custom type hpnicfAclLinkDestIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfAclLinkDestIfIndex_Type.__name__ = "Integer32"
_HpnicfAclLinkDestIfIndex_Object = MibTableColumn
hpnicfAclLinkDestIfIndex = _HpnicfAclLinkDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 16),
    _HpnicfAclLinkDestIfIndex_Type()
)
hpnicfAclLinkDestIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkDestIfIndex.setStatus("current")
_HpnicfAclLinkDestAny_Type = TruthValue
_HpnicfAclLinkDestAny_Object = MibTableColumn
hpnicfAclLinkDestAny = _HpnicfAclLinkDestAny_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 17),
    _HpnicfAclLinkDestAny_Type()
)
hpnicfAclLinkDestAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkDestAny.setStatus("current")


class _HpnicfAclLinkTimeRangeName_Type(OctetString):
    """Custom type hpnicfAclLinkTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclLinkTimeRangeName_Type.__name__ = "OctetString"
_HpnicfAclLinkTimeRangeName_Object = MibTableColumn
hpnicfAclLinkTimeRangeName = _HpnicfAclLinkTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 18),
    _HpnicfAclLinkTimeRangeName_Type()
)
hpnicfAclLinkTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkTimeRangeName.setStatus("current")
_HpnicfAclLinkEnable_Type = TruthValue
_HpnicfAclLinkEnable_Object = MibTableColumn
hpnicfAclLinkEnable = _HpnicfAclLinkEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 19),
    _HpnicfAclLinkEnable_Type()
)
hpnicfAclLinkEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclLinkEnable.setStatus("current")
_HpnicfAclLinkRowStatus_Type = RowStatus
_HpnicfAclLinkRowStatus_Object = MibTableColumn
hpnicfAclLinkRowStatus = _HpnicfAclLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 20),
    _HpnicfAclLinkRowStatus_Type()
)
hpnicfAclLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkRowStatus.setStatus("current")


class _HpnicfAclLinkTypeCode_Type(OctetString):
    """Custom type hpnicfAclLinkTypeCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclLinkTypeCode_Type.__name__ = "OctetString"
_HpnicfAclLinkTypeCode_Object = MibTableColumn
hpnicfAclLinkTypeCode = _HpnicfAclLinkTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 21),
    _HpnicfAclLinkTypeCode_Type()
)
hpnicfAclLinkTypeCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkTypeCode.setStatus("current")


class _HpnicfAclLinkTypeMask_Type(OctetString):
    """Custom type hpnicfAclLinkTypeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclLinkTypeMask_Type.__name__ = "OctetString"
_HpnicfAclLinkTypeMask_Object = MibTableColumn
hpnicfAclLinkTypeMask = _HpnicfAclLinkTypeMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 22),
    _HpnicfAclLinkTypeMask_Type()
)
hpnicfAclLinkTypeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkTypeMask.setStatus("current")


class _HpnicfAclLinkLsapCode_Type(OctetString):
    """Custom type hpnicfAclLinkLsapCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclLinkLsapCode_Type.__name__ = "OctetString"
_HpnicfAclLinkLsapCode_Object = MibTableColumn
hpnicfAclLinkLsapCode = _HpnicfAclLinkLsapCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 23),
    _HpnicfAclLinkLsapCode_Type()
)
hpnicfAclLinkLsapCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkLsapCode.setStatus("current")


class _HpnicfAclLinkLsapMask_Type(OctetString):
    """Custom type hpnicfAclLinkLsapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclLinkLsapMask_Type.__name__ = "OctetString"
_HpnicfAclLinkLsapMask_Object = MibTableColumn
hpnicfAclLinkLsapMask = _HpnicfAclLinkLsapMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 24),
    _HpnicfAclLinkLsapMask_Type()
)
hpnicfAclLinkLsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkLsapMask.setStatus("current")


class _HpnicfAclLinkL2LabelRangeOp_Type(Integer32):
    """Custom type hpnicfAclLinkL2LabelRangeOp based on Integer32"""
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
        *(("invalid", 0),
          ("lt", 1),
          ("eq", 2),
          ("gt", 3),
          ("neq", 4),
          ("range", 5))
    )


_HpnicfAclLinkL2LabelRangeOp_Type.__name__ = "Integer32"
_HpnicfAclLinkL2LabelRangeOp_Object = MibTableColumn
hpnicfAclLinkL2LabelRangeOp = _HpnicfAclLinkL2LabelRangeOp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 25),
    _HpnicfAclLinkL2LabelRangeOp_Type()
)
hpnicfAclLinkL2LabelRangeOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkL2LabelRangeOp.setStatus("current")
_HpnicfAclLinkL2LabelRangeBegin_Type = Integer32
_HpnicfAclLinkL2LabelRangeBegin_Object = MibTableColumn
hpnicfAclLinkL2LabelRangeBegin = _HpnicfAclLinkL2LabelRangeBegin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 26),
    _HpnicfAclLinkL2LabelRangeBegin_Type()
)
hpnicfAclLinkL2LabelRangeBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkL2LabelRangeBegin.setStatus("current")
_HpnicfAclLinkL2LabelRangeEnd_Type = Integer32
_HpnicfAclLinkL2LabelRangeEnd_Object = MibTableColumn
hpnicfAclLinkL2LabelRangeEnd = _HpnicfAclLinkL2LabelRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 27),
    _HpnicfAclLinkL2LabelRangeEnd_Type()
)
hpnicfAclLinkL2LabelRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkL2LabelRangeEnd.setStatus("current")
_HpnicfAclLinkMplsExp_Type = Integer32
_HpnicfAclLinkMplsExp_Object = MibTableColumn
hpnicfAclLinkMplsExp = _HpnicfAclLinkMplsExp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 7, 1, 28),
    _HpnicfAclLinkMplsExp_Type()
)
hpnicfAclLinkMplsExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclLinkMplsExp.setStatus("current")
_HpnicfAclUserTable_Object = MibTable
hpnicfAclUserTable = _HpnicfAclUserTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 8)
)
if mibBuilder.loadTexts:
    hpnicfAclUserTable.setStatus("current")
_HpnicfAclUserEntry_Object = MibTableRow
hpnicfAclUserEntry = _HpnicfAclUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 8, 1)
)
hpnicfAclUserEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclUserAclNum"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclUserSubitem"),
)
if mibBuilder.loadTexts:
    hpnicfAclUserEntry.setStatus("current")


class _HpnicfAclUserAclNum_Type(Integer32):
    """Custom type hpnicfAclUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfAclUserAclNum_Type.__name__ = "Integer32"
_HpnicfAclUserAclNum_Object = MibTableColumn
hpnicfAclUserAclNum = _HpnicfAclUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 8, 1, 1),
    _HpnicfAclUserAclNum_Type()
)
hpnicfAclUserAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclUserAclNum.setStatus("current")


class _HpnicfAclUserSubitem_Type(Integer32):
    """Custom type hpnicfAclUserSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclUserSubitem_Type.__name__ = "Integer32"
_HpnicfAclUserSubitem_Object = MibTableColumn
hpnicfAclUserSubitem = _HpnicfAclUserSubitem_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 8, 1, 2),
    _HpnicfAclUserSubitem_Type()
)
hpnicfAclUserSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclUserSubitem.setStatus("current")


class _HpnicfAclUserAct_Type(Integer32):
    """Custom type hpnicfAclUserAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_HpnicfAclUserAct_Type.__name__ = "Integer32"
_HpnicfAclUserAct_Object = MibTableColumn
hpnicfAclUserAct = _HpnicfAclUserAct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 8, 1, 3),
    _HpnicfAclUserAct_Type()
)
hpnicfAclUserAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclUserAct.setStatus("current")


class _HpnicfAclUserFormatType_Type(Integer32):
    """Custom type hpnicfAclUserFormatType based on Integer32"""
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
        *(("invalid", 0),
          ("ethernetII", 1),
          ("snap", 2),
          ("ieee802Dot2And3", 3),
          ("ieee802Dot4", 4))
    )


_HpnicfAclUserFormatType_Type.__name__ = "Integer32"
_HpnicfAclUserFormatType_Object = MibTableColumn
hpnicfAclUserFormatType = _HpnicfAclUserFormatType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 8, 1, 4),
    _HpnicfAclUserFormatType_Type()
)
hpnicfAclUserFormatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclUserFormatType.setStatus("current")


class _HpnicfAclUserVlanTag_Type(Integer32):
    """Custom type hpnicfAclUserVlanTag based on Integer32"""
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
        *(("invalid", 0),
          ("tagged", 1),
          ("untagged", 2))
    )


_HpnicfAclUserVlanTag_Type.__name__ = "Integer32"
_HpnicfAclUserVlanTag_Object = MibTableColumn
hpnicfAclUserVlanTag = _HpnicfAclUserVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 8, 1, 5),
    _HpnicfAclUserVlanTag_Type()
)
hpnicfAclUserVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclUserVlanTag.setStatus("current")


class _HpnicfAclUserRuleStr_Type(OctetString):
    """Custom type hpnicfAclUserRuleStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_HpnicfAclUserRuleStr_Type.__name__ = "OctetString"
_HpnicfAclUserRuleStr_Object = MibTableColumn
hpnicfAclUserRuleStr = _HpnicfAclUserRuleStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 8, 1, 6),
    _HpnicfAclUserRuleStr_Type()
)
hpnicfAclUserRuleStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclUserRuleStr.setStatus("current")


class _HpnicfAclUserRuleMask_Type(OctetString):
    """Custom type hpnicfAclUserRuleMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_HpnicfAclUserRuleMask_Type.__name__ = "OctetString"
_HpnicfAclUserRuleMask_Object = MibTableColumn
hpnicfAclUserRuleMask = _HpnicfAclUserRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 8, 1, 7),
    _HpnicfAclUserRuleMask_Type()
)
hpnicfAclUserRuleMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclUserRuleMask.setStatus("current")


class _HpnicfAclUserTimeRangeName_Type(OctetString):
    """Custom type hpnicfAclUserTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclUserTimeRangeName_Type.__name__ = "OctetString"
_HpnicfAclUserTimeRangeName_Object = MibTableColumn
hpnicfAclUserTimeRangeName = _HpnicfAclUserTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 8, 1, 8),
    _HpnicfAclUserTimeRangeName_Type()
)
hpnicfAclUserTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclUserTimeRangeName.setStatus("current")
_HpnicfAclUserEnable_Type = TruthValue
_HpnicfAclUserEnable_Object = MibTableColumn
hpnicfAclUserEnable = _HpnicfAclUserEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 8, 1, 9),
    _HpnicfAclUserEnable_Type()
)
hpnicfAclUserEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclUserEnable.setStatus("current")
_HpnicfAclUserRowStatus_Type = RowStatus
_HpnicfAclUserRowStatus_Object = MibTableColumn
hpnicfAclUserRowStatus = _HpnicfAclUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 8, 1, 10),
    _HpnicfAclUserRowStatus_Type()
)
hpnicfAclUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclUserRowStatus.setStatus("current")
_HpnicfAclActiveTable_Object = MibTable
hpnicfAclActiveTable = _HpnicfAclActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 9)
)
if mibBuilder.loadTexts:
    hpnicfAclActiveTable.setStatus("current")
_HpnicfAclActiveEntry_Object = MibTableRow
hpnicfAclActiveEntry = _HpnicfAclActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 9, 1)
)
hpnicfAclActiveEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclActiveAclIndex"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclActiveIfIndex"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclActiveVlanID"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclActiveDirection"),
)
if mibBuilder.loadTexts:
    hpnicfAclActiveEntry.setStatus("current")


class _HpnicfAclActiveAclIndex_Type(Integer32):
    """Custom type hpnicfAclActiveAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfAclActiveAclIndex_Type.__name__ = "Integer32"
_HpnicfAclActiveAclIndex_Object = MibTableColumn
hpnicfAclActiveAclIndex = _HpnicfAclActiveAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 9, 1, 1),
    _HpnicfAclActiveAclIndex_Type()
)
hpnicfAclActiveAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclActiveAclIndex.setStatus("current")


class _HpnicfAclActiveIfIndex_Type(Integer32):
    """Custom type hpnicfAclActiveIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfAclActiveIfIndex_Type.__name__ = "Integer32"
_HpnicfAclActiveIfIndex_Object = MibTableColumn
hpnicfAclActiveIfIndex = _HpnicfAclActiveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 9, 1, 2),
    _HpnicfAclActiveIfIndex_Type()
)
hpnicfAclActiveIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclActiveIfIndex.setStatus("current")
_HpnicfAclActiveVlanID_Type = Integer32
_HpnicfAclActiveVlanID_Object = MibTableColumn
hpnicfAclActiveVlanID = _HpnicfAclActiveVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 9, 1, 3),
    _HpnicfAclActiveVlanID_Type()
)
hpnicfAclActiveVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclActiveVlanID.setStatus("current")


class _HpnicfAclActiveDirection_Type(Integer32):
    """Custom type hpnicfAclActiveDirection based on Integer32"""
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
        *(("invalid", 0),
          ("input", 1),
          ("output", 2),
          ("both", 3))
    )


_HpnicfAclActiveDirection_Type.__name__ = "Integer32"
_HpnicfAclActiveDirection_Object = MibTableColumn
hpnicfAclActiveDirection = _HpnicfAclActiveDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 9, 1, 4),
    _HpnicfAclActiveDirection_Type()
)
hpnicfAclActiveDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclActiveDirection.setStatus("current")


class _HpnicfAclActiveUserAclNum_Type(Integer32):
    """Custom type hpnicfAclActiveUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfAclActiveUserAclNum_Type.__name__ = "Integer32"
_HpnicfAclActiveUserAclNum_Object = MibTableColumn
hpnicfAclActiveUserAclNum = _HpnicfAclActiveUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 9, 1, 5),
    _HpnicfAclActiveUserAclNum_Type()
)
hpnicfAclActiveUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclActiveUserAclNum.setStatus("current")


class _HpnicfAclActiveUserAclSubitem_Type(Integer32):
    """Custom type hpnicfAclActiveUserAclSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclActiveUserAclSubitem_Type.__name__ = "Integer32"
_HpnicfAclActiveUserAclSubitem_Object = MibTableColumn
hpnicfAclActiveUserAclSubitem = _HpnicfAclActiveUserAclSubitem_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 9, 1, 6),
    _HpnicfAclActiveUserAclSubitem_Type()
)
hpnicfAclActiveUserAclSubitem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclActiveUserAclSubitem.setStatus("current")


class _HpnicfAclActiveIpAclNum_Type(Integer32):
    """Custom type hpnicfAclActiveIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfAclActiveIpAclNum_Type.__name__ = "Integer32"
_HpnicfAclActiveIpAclNum_Object = MibTableColumn
hpnicfAclActiveIpAclNum = _HpnicfAclActiveIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 9, 1, 7),
    _HpnicfAclActiveIpAclNum_Type()
)
hpnicfAclActiveIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclActiveIpAclNum.setStatus("current")


class _HpnicfAclActiveIpAclSubitem_Type(Integer32):
    """Custom type hpnicfAclActiveIpAclSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclActiveIpAclSubitem_Type.__name__ = "Integer32"
_HpnicfAclActiveIpAclSubitem_Object = MibTableColumn
hpnicfAclActiveIpAclSubitem = _HpnicfAclActiveIpAclSubitem_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 9, 1, 8),
    _HpnicfAclActiveIpAclSubitem_Type()
)
hpnicfAclActiveIpAclSubitem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclActiveIpAclSubitem.setStatus("current")


class _HpnicfAclActiveLinkAclNum_Type(Integer32):
    """Custom type hpnicfAclActiveLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfAclActiveLinkAclNum_Type.__name__ = "Integer32"
_HpnicfAclActiveLinkAclNum_Object = MibTableColumn
hpnicfAclActiveLinkAclNum = _HpnicfAclActiveLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 9, 1, 9),
    _HpnicfAclActiveLinkAclNum_Type()
)
hpnicfAclActiveLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclActiveLinkAclNum.setStatus("current")


class _HpnicfAclActiveLinkAclSubitem_Type(Integer32):
    """Custom type hpnicfAclActiveLinkAclSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclActiveLinkAclSubitem_Type.__name__ = "Integer32"
_HpnicfAclActiveLinkAclSubitem_Object = MibTableColumn
hpnicfAclActiveLinkAclSubitem = _HpnicfAclActiveLinkAclSubitem_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 9, 1, 10),
    _HpnicfAclActiveLinkAclSubitem_Type()
)
hpnicfAclActiveLinkAclSubitem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclActiveLinkAclSubitem.setStatus("current")
_HpnicfAclActiveRuntime_Type = TruthValue
_HpnicfAclActiveRuntime_Object = MibTableColumn
hpnicfAclActiveRuntime = _HpnicfAclActiveRuntime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 9, 1, 11),
    _HpnicfAclActiveRuntime_Type()
)
hpnicfAclActiveRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclActiveRuntime.setStatus("current")
_HpnicfAclActiveRowStatus_Type = RowStatus
_HpnicfAclActiveRowStatus_Object = MibTableColumn
hpnicfAclActiveRowStatus = _HpnicfAclActiveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 9, 1, 12),
    _HpnicfAclActiveRowStatus_Type()
)
hpnicfAclActiveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclActiveRowStatus.setStatus("current")
_HpnicfAclIDSTable_Object = MibTable
hpnicfAclIDSTable = _HpnicfAclIDSTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 10)
)
if mibBuilder.loadTexts:
    hpnicfAclIDSTable.setStatus("current")
_HpnicfAclIDSEntry_Object = MibTableRow
hpnicfAclIDSEntry = _HpnicfAclIDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 10, 1)
)
hpnicfAclIDSEntry.setIndexNames(
    (1, "HPN-ICF-ACL-MIB", "hpnicfAclIDSName"),
)
if mibBuilder.loadTexts:
    hpnicfAclIDSEntry.setStatus("current")


class _HpnicfAclIDSName_Type(OctetString):
    """Custom type hpnicfAclIDSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfAclIDSName_Type.__name__ = "OctetString"
_HpnicfAclIDSName_Object = MibTableColumn
hpnicfAclIDSName = _HpnicfAclIDSName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 10, 1, 1),
    _HpnicfAclIDSName_Type()
)
hpnicfAclIDSName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclIDSName.setStatus("current")
_HpnicfAclIDSSrcMac_Type = MacAddress
_HpnicfAclIDSSrcMac_Object = MibTableColumn
hpnicfAclIDSSrcMac = _HpnicfAclIDSSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 10, 1, 2),
    _HpnicfAclIDSSrcMac_Type()
)
hpnicfAclIDSSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIDSSrcMac.setStatus("current")
_HpnicfAclIDSDestMac_Type = MacAddress
_HpnicfAclIDSDestMac_Object = MibTableColumn
hpnicfAclIDSDestMac = _HpnicfAclIDSDestMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 10, 1, 3),
    _HpnicfAclIDSDestMac_Type()
)
hpnicfAclIDSDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIDSDestMac.setStatus("current")
_HpnicfAclIDSSrcIp_Type = IpAddress
_HpnicfAclIDSSrcIp_Object = MibTableColumn
hpnicfAclIDSSrcIp = _HpnicfAclIDSSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 10, 1, 4),
    _HpnicfAclIDSSrcIp_Type()
)
hpnicfAclIDSSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIDSSrcIp.setStatus("current")
_HpnicfAclIDSSrcWild_Type = IpAddress
_HpnicfAclIDSSrcWild_Object = MibTableColumn
hpnicfAclIDSSrcWild = _HpnicfAclIDSSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 10, 1, 5),
    _HpnicfAclIDSSrcWild_Type()
)
hpnicfAclIDSSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIDSSrcWild.setStatus("current")
_HpnicfAclIDSDestIp_Type = IpAddress
_HpnicfAclIDSDestIp_Object = MibTableColumn
hpnicfAclIDSDestIp = _HpnicfAclIDSDestIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 10, 1, 6),
    _HpnicfAclIDSDestIp_Type()
)
hpnicfAclIDSDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIDSDestIp.setStatus("current")
_HpnicfAclIDSDestWild_Type = IpAddress
_HpnicfAclIDSDestWild_Object = MibTableColumn
hpnicfAclIDSDestWild = _HpnicfAclIDSDestWild_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 10, 1, 7),
    _HpnicfAclIDSDestWild_Type()
)
hpnicfAclIDSDestWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIDSDestWild.setStatus("current")


class _HpnicfAclIDSSrcPort_Type(Integer32):
    """Custom type hpnicfAclIDSSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclIDSSrcPort_Type.__name__ = "Integer32"
_HpnicfAclIDSSrcPort_Object = MibTableColumn
hpnicfAclIDSSrcPort = _HpnicfAclIDSSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 10, 1, 8),
    _HpnicfAclIDSSrcPort_Type()
)
hpnicfAclIDSSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIDSSrcPort.setStatus("current")


class _HpnicfAclIDSDestPort_Type(Integer32):
    """Custom type hpnicfAclIDSDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclIDSDestPort_Type.__name__ = "Integer32"
_HpnicfAclIDSDestPort_Object = MibTableColumn
hpnicfAclIDSDestPort = _HpnicfAclIDSDestPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 10, 1, 9),
    _HpnicfAclIDSDestPort_Type()
)
hpnicfAclIDSDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIDSDestPort.setStatus("current")


class _HpnicfAclIDSProtocol_Type(Integer32):
    """Custom type hpnicfAclIDSProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfAclIDSProtocol_Type.__name__ = "Integer32"
_HpnicfAclIDSProtocol_Object = MibTableColumn
hpnicfAclIDSProtocol = _HpnicfAclIDSProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 10, 1, 10),
    _HpnicfAclIDSProtocol_Type()
)
hpnicfAclIDSProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIDSProtocol.setStatus("current")


class _HpnicfAclIDSDenyTime_Type(Unsigned32):
    """Custom type hpnicfAclIDSDenyTime based on Unsigned32"""
    defaultValue = 0


_HpnicfAclIDSDenyTime_Type.__name__ = "Unsigned32"
_HpnicfAclIDSDenyTime_Object = MibTableColumn
hpnicfAclIDSDenyTime = _HpnicfAclIDSDenyTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 10, 1, 11),
    _HpnicfAclIDSDenyTime_Type()
)
hpnicfAclIDSDenyTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIDSDenyTime.setStatus("current")


class _HpnicfAclIDSAct_Type(Integer32):
    """Custom type hpnicfAclIDSAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_HpnicfAclIDSAct_Type.__name__ = "Integer32"
_HpnicfAclIDSAct_Object = MibTableColumn
hpnicfAclIDSAct = _HpnicfAclIDSAct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 10, 1, 12),
    _HpnicfAclIDSAct_Type()
)
hpnicfAclIDSAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIDSAct.setStatus("current")
_HpnicfAclIDSRowStatus_Type = RowStatus
_HpnicfAclIDSRowStatus_Object = MibTableColumn
hpnicfAclIDSRowStatus = _HpnicfAclIDSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 1, 10, 1, 13),
    _HpnicfAclIDSRowStatus_Type()
)
hpnicfAclIDSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIDSRowStatus.setStatus("current")
_HpnicfAclMib2Objects_ObjectIdentity = ObjectIdentity
hpnicfAclMib2Objects = _HpnicfAclMib2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2)
)
_HpnicfAclMib2GlobalGroup_ObjectIdentity = ObjectIdentity
hpnicfAclMib2GlobalGroup = _HpnicfAclMib2GlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1)
)
_HpnicfAclMib2NodesGroup_ObjectIdentity = ObjectIdentity
hpnicfAclMib2NodesGroup = _HpnicfAclMib2NodesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 1)
)


class _HpnicfAclMib2Mode_Type(Integer32):
    """Custom type hpnicfAclMib2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkBased", 1),
          ("ipBased", 2))
    )


_HpnicfAclMib2Mode_Type.__name__ = "Integer32"
_HpnicfAclMib2Mode_Object = MibScalar
hpnicfAclMib2Mode = _HpnicfAclMib2Mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 1, 1),
    _HpnicfAclMib2Mode_Type()
)
hpnicfAclMib2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfAclMib2Mode.setStatus("current")
_HpnicfAclMib2Version_Type = Integer32
_HpnicfAclMib2Version_Object = MibScalar
hpnicfAclMib2Version = _HpnicfAclMib2Version_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 1, 2),
    _HpnicfAclMib2Version_Type()
)
hpnicfAclMib2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclMib2Version.setStatus("current")


class _HpnicfAclMib2ObjectsCapabilities_Type(Bits):
    """Custom type hpnicfAclMib2ObjectsCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("hpnicfAclMib2Mode", 0),
          ("hpnicfAclVersion", 1),
          ("hpnicfAclMib2ObjectsCapabilities", 2),
          ("hpnicfAclMib2CapabilityTable", 3),
          ("hpnicfAclNumberGroupTable", 4),
          ("hpnicfAclIPAclBasicTable", 5),
          ("hpnicfAclIPAclAdvancedTable", 6),
          ("hpnicfAclMACTable", 7),
          ("hpnicfAclEnUserTable", 8),
          ("hpnicfAclMib2ProcessingStatus", 9))
    )

_HpnicfAclMib2ObjectsCapabilities_Type.__name__ = "Bits"
_HpnicfAclMib2ObjectsCapabilities_Object = MibScalar
hpnicfAclMib2ObjectsCapabilities = _HpnicfAclMib2ObjectsCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 1, 3),
    _HpnicfAclMib2ObjectsCapabilities_Type()
)
hpnicfAclMib2ObjectsCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclMib2ObjectsCapabilities.setStatus("current")


class _HpnicfAclMib2ProcessingStatus_Type(Integer32):
    """Custom type hpnicfAclMib2ProcessingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("processing", 1),
          ("done", 2))
    )


_HpnicfAclMib2ProcessingStatus_Type.__name__ = "Integer32"
_HpnicfAclMib2ProcessingStatus_Object = MibScalar
hpnicfAclMib2ProcessingStatus = _HpnicfAclMib2ProcessingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 1, 4),
    _HpnicfAclMib2ProcessingStatus_Type()
)
hpnicfAclMib2ProcessingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclMib2ProcessingStatus.setStatus("current")
_HpnicfAclMib2CapabilityTable_Object = MibTable
hpnicfAclMib2CapabilityTable = _HpnicfAclMib2CapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfAclMib2CapabilityTable.setStatus("current")
_HpnicfAclMib2CapabilityEntry_Object = MibTableRow
hpnicfAclMib2CapabilityEntry = _HpnicfAclMib2CapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 2, 1)
)
hpnicfAclMib2CapabilityEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclMib2EntityType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclMib2EntityIndex"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclMib2ModuleIndex"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclMib2CharacteristicsIndex"),
)
if mibBuilder.loadTexts:
    hpnicfAclMib2CapabilityEntry.setStatus("current")


class _HpnicfAclMib2EntityType_Type(Integer32):
    """Custom type hpnicfAclMib2EntityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("interface", 2))
    )


_HpnicfAclMib2EntityType_Type.__name__ = "Integer32"
_HpnicfAclMib2EntityType_Object = MibTableColumn
hpnicfAclMib2EntityType = _HpnicfAclMib2EntityType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 2, 1, 1),
    _HpnicfAclMib2EntityType_Type()
)
hpnicfAclMib2EntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclMib2EntityType.setStatus("current")


class _HpnicfAclMib2EntityIndex_Type(Integer32):
    """Custom type hpnicfAclMib2EntityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfAclMib2EntityIndex_Type.__name__ = "Integer32"
_HpnicfAclMib2EntityIndex_Object = MibTableColumn
hpnicfAclMib2EntityIndex = _HpnicfAclMib2EntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 2, 1, 2),
    _HpnicfAclMib2EntityIndex_Type()
)
hpnicfAclMib2EntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclMib2EntityIndex.setStatus("current")


class _HpnicfAclMib2ModuleIndex_Type(Integer32):
    """Custom type hpnicfAclMib2ModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("layer3", 1),
          ("layer2", 2),
          ("userDefined", 3))
    )


_HpnicfAclMib2ModuleIndex_Type.__name__ = "Integer32"
_HpnicfAclMib2ModuleIndex_Object = MibTableColumn
hpnicfAclMib2ModuleIndex = _HpnicfAclMib2ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 2, 1, 3),
    _HpnicfAclMib2ModuleIndex_Type()
)
hpnicfAclMib2ModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclMib2ModuleIndex.setStatus("current")


class _HpnicfAclMib2CharacteristicsIndex_Type(Integer32):
    """Custom type hpnicfAclMib2CharacteristicsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfAclMib2CharacteristicsIndex_Type.__name__ = "Integer32"
_HpnicfAclMib2CharacteristicsIndex_Object = MibTableColumn
hpnicfAclMib2CharacteristicsIndex = _HpnicfAclMib2CharacteristicsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 2, 1, 4),
    _HpnicfAclMib2CharacteristicsIndex_Type()
)
hpnicfAclMib2CharacteristicsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclMib2CharacteristicsIndex.setStatus("current")


class _HpnicfAclMib2CharacteristicsDesc_Type(OctetString):
    """Custom type hpnicfAclMib2CharacteristicsDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclMib2CharacteristicsDesc_Type.__name__ = "OctetString"
_HpnicfAclMib2CharacteristicsDesc_Object = MibTableColumn
hpnicfAclMib2CharacteristicsDesc = _HpnicfAclMib2CharacteristicsDesc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 2, 1, 5),
    _HpnicfAclMib2CharacteristicsDesc_Type()
)
hpnicfAclMib2CharacteristicsDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclMib2CharacteristicsDesc.setStatus("current")
_HpnicfAclMib2CharacteristicsValue_Type = Unsigned32
_HpnicfAclMib2CharacteristicsValue_Object = MibTableColumn
hpnicfAclMib2CharacteristicsValue = _HpnicfAclMib2CharacteristicsValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 2, 1, 6),
    _HpnicfAclMib2CharacteristicsValue_Type()
)
hpnicfAclMib2CharacteristicsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclMib2CharacteristicsValue.setStatus("current")
_HpnicfAclNumberGroupTable_Object = MibTable
hpnicfAclNumberGroupTable = _HpnicfAclNumberGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfAclNumberGroupTable.setStatus("current")
_HpnicfAclNumberGroupEntry_Object = MibTableRow
hpnicfAclNumberGroupEntry = _HpnicfAclNumberGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 3, 1)
)
hpnicfAclNumberGroupEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNumberGroupType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNumberGroupIndex"),
)
if mibBuilder.loadTexts:
    hpnicfAclNumberGroupEntry.setStatus("current")


class _HpnicfAclNumberGroupType_Type(Integer32):
    """Custom type hpnicfAclNumberGroupType based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("mac", 3),
          ("user", 4))
    )


_HpnicfAclNumberGroupType_Type.__name__ = "Integer32"
_HpnicfAclNumberGroupType_Object = MibTableColumn
hpnicfAclNumberGroupType = _HpnicfAclNumberGroupType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 3, 1, 1),
    _HpnicfAclNumberGroupType_Type()
)
hpnicfAclNumberGroupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclNumberGroupType.setStatus("current")


class _HpnicfAclNumberGroupIndex_Type(Integer32):
    """Custom type hpnicfAclNumberGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 5999),
        ValueRangeConstraint(10000, 42767),
    )


_HpnicfAclNumberGroupIndex_Type.__name__ = "Integer32"
_HpnicfAclNumberGroupIndex_Object = MibTableColumn
hpnicfAclNumberGroupIndex = _HpnicfAclNumberGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 3, 1, 2),
    _HpnicfAclNumberGroupIndex_Type()
)
hpnicfAclNumberGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclNumberGroupIndex.setStatus("current")
_HpnicfAclNumberGroupRowStatus_Type = RowStatus
_HpnicfAclNumberGroupRowStatus_Object = MibTableColumn
hpnicfAclNumberGroupRowStatus = _HpnicfAclNumberGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 3, 1, 3),
    _HpnicfAclNumberGroupRowStatus_Type()
)
hpnicfAclNumberGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNumberGroupRowStatus.setStatus("current")


class _HpnicfAclNumberGroupMatchOrder_Type(Integer32):
    """Custom type hpnicfAclNumberGroupMatchOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 1),
          ("auto", 2))
    )


_HpnicfAclNumberGroupMatchOrder_Type.__name__ = "Integer32"
_HpnicfAclNumberGroupMatchOrder_Object = MibTableColumn
hpnicfAclNumberGroupMatchOrder = _HpnicfAclNumberGroupMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 3, 1, 4),
    _HpnicfAclNumberGroupMatchOrder_Type()
)
hpnicfAclNumberGroupMatchOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNumberGroupMatchOrder.setStatus("current")


class _HpnicfAclNumberGroupStep_Type(Integer32):
    """Custom type hpnicfAclNumberGroupStep based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HpnicfAclNumberGroupStep_Type.__name__ = "Integer32"
_HpnicfAclNumberGroupStep_Object = MibTableColumn
hpnicfAclNumberGroupStep = _HpnicfAclNumberGroupStep_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 3, 1, 5),
    _HpnicfAclNumberGroupStep_Type()
)
hpnicfAclNumberGroupStep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNumberGroupStep.setStatus("current")


class _HpnicfAclNumberGroupDescription_Type(OctetString):
    """Custom type hpnicfAclNumberGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfAclNumberGroupDescription_Type.__name__ = "OctetString"
_HpnicfAclNumberGroupDescription_Object = MibTableColumn
hpnicfAclNumberGroupDescription = _HpnicfAclNumberGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 3, 1, 6),
    _HpnicfAclNumberGroupDescription_Type()
)
hpnicfAclNumberGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNumberGroupDescription.setStatus("current")


class _HpnicfAclNumberGroupCountClear_Type(CounterClear):
    """Custom type hpnicfAclNumberGroupCountClear based on CounterClear"""
    defaultValue = 2


_HpnicfAclNumberGroupCountClear_Type.__name__ = "CounterClear"
_HpnicfAclNumberGroupCountClear_Object = MibTableColumn
hpnicfAclNumberGroupCountClear = _HpnicfAclNumberGroupCountClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 3, 1, 7),
    _HpnicfAclNumberGroupCountClear_Type()
)
hpnicfAclNumberGroupCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfAclNumberGroupCountClear.setStatus("current")
_HpnicfAclNumberGroupRuleCounter_Type = Counter32
_HpnicfAclNumberGroupRuleCounter_Object = MibTableColumn
hpnicfAclNumberGroupRuleCounter = _HpnicfAclNumberGroupRuleCounter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 3, 1, 8),
    _HpnicfAclNumberGroupRuleCounter_Type()
)
hpnicfAclNumberGroupRuleCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclNumberGroupRuleCounter.setStatus("current")


class _HpnicfAclNumberGroupName_Type(OctetString):
    """Custom type hpnicfAclNumberGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfAclNumberGroupName_Type.__name__ = "OctetString"
_HpnicfAclNumberGroupName_Object = MibTableColumn
hpnicfAclNumberGroupName = _HpnicfAclNumberGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 3, 1, 9),
    _HpnicfAclNumberGroupName_Type()
)
hpnicfAclNumberGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNumberGroupName.setStatus("current")
_HpnicfAclNamedGroupTable_Object = MibTable
hpnicfAclNamedGroupTable = _HpnicfAclNamedGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfAclNamedGroupTable.setStatus("current")
_HpnicfAclNamedGroupEntry_Object = MibTableRow
hpnicfAclNamedGroupEntry = _HpnicfAclNamedGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 4, 1)
)
hpnicfAclNamedGroupEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNumberGroupType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNamedGroupCategory"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNamedGroupName"),
)
if mibBuilder.loadTexts:
    hpnicfAclNamedGroupEntry.setStatus("current")


class _HpnicfAclNamedGroupCategory_Type(Integer32):
    """Custom type hpnicfAclNamedGroupCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("basic", 1),
          ("advanced", 2))
    )


_HpnicfAclNamedGroupCategory_Type.__name__ = "Integer32"
_HpnicfAclNamedGroupCategory_Object = MibTableColumn
hpnicfAclNamedGroupCategory = _HpnicfAclNamedGroupCategory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 4, 1, 1),
    _HpnicfAclNamedGroupCategory_Type()
)
hpnicfAclNamedGroupCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclNamedGroupCategory.setStatus("current")


class _HpnicfAclNamedGroupName_Type(OctetString):
    """Custom type hpnicfAclNamedGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HpnicfAclNamedGroupName_Type.__name__ = "OctetString"
_HpnicfAclNamedGroupName_Object = MibTableColumn
hpnicfAclNamedGroupName = _HpnicfAclNamedGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 4, 1, 2),
    _HpnicfAclNamedGroupName_Type()
)
hpnicfAclNamedGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclNamedGroupName.setStatus("current")
_HpnicfAclNamedGroupRowStatus_Type = RowStatus
_HpnicfAclNamedGroupRowStatus_Object = MibTableColumn
hpnicfAclNamedGroupRowStatus = _HpnicfAclNamedGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 4, 1, 3),
    _HpnicfAclNamedGroupRowStatus_Type()
)
hpnicfAclNamedGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedGroupRowStatus.setStatus("current")


class _HpnicfAclNamedGroupMatchOrder_Type(Integer32):
    """Custom type hpnicfAclNamedGroupMatchOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 1),
          ("auto", 2))
    )


_HpnicfAclNamedGroupMatchOrder_Type.__name__ = "Integer32"
_HpnicfAclNamedGroupMatchOrder_Object = MibTableColumn
hpnicfAclNamedGroupMatchOrder = _HpnicfAclNamedGroupMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 4, 1, 4),
    _HpnicfAclNamedGroupMatchOrder_Type()
)
hpnicfAclNamedGroupMatchOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedGroupMatchOrder.setStatus("current")


class _HpnicfAclNamedGroupStep_Type(Integer32):
    """Custom type hpnicfAclNamedGroupStep based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HpnicfAclNamedGroupStep_Type.__name__ = "Integer32"
_HpnicfAclNamedGroupStep_Object = MibTableColumn
hpnicfAclNamedGroupStep = _HpnicfAclNamedGroupStep_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 4, 1, 5),
    _HpnicfAclNamedGroupStep_Type()
)
hpnicfAclNamedGroupStep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedGroupStep.setStatus("current")


class _HpnicfAclNamedGroupDescription_Type(OctetString):
    """Custom type hpnicfAclNamedGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfAclNamedGroupDescription_Type.__name__ = "OctetString"
_HpnicfAclNamedGroupDescription_Object = MibTableColumn
hpnicfAclNamedGroupDescription = _HpnicfAclNamedGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 4, 1, 6),
    _HpnicfAclNamedGroupDescription_Type()
)
hpnicfAclNamedGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedGroupDescription.setStatus("current")


class _HpnicfAclNamedGroupCountClear_Type(CounterClear):
    """Custom type hpnicfAclNamedGroupCountClear based on CounterClear"""
    defaultValue = 2


_HpnicfAclNamedGroupCountClear_Type.__name__ = "CounterClear"
_HpnicfAclNamedGroupCountClear_Object = MibTableColumn
hpnicfAclNamedGroupCountClear = _HpnicfAclNamedGroupCountClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 4, 1, 7),
    _HpnicfAclNamedGroupCountClear_Type()
)
hpnicfAclNamedGroupCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfAclNamedGroupCountClear.setStatus("current")
_HpnicfAclNamedGroupRuleCounter_Type = Counter32
_HpnicfAclNamedGroupRuleCounter_Object = MibTableColumn
hpnicfAclNamedGroupRuleCounter = _HpnicfAclNamedGroupRuleCounter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 1, 4, 1, 8),
    _HpnicfAclNamedGroupRuleCounter_Type()
)
hpnicfAclNamedGroupRuleCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclNamedGroupRuleCounter.setStatus("current")
_HpnicfAclIPAclGroup_ObjectIdentity = ObjectIdentity
hpnicfAclIPAclGroup = _HpnicfAclIPAclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2)
)
_HpnicfAclIPAclBasicTable_Object = MibTable
hpnicfAclIPAclBasicTable = _HpnicfAclIPAclBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicTable.setStatus("current")
_HpnicfAclIPAclBasicEntry_Object = MibTableRow
hpnicfAclIPAclBasicEntry = _HpnicfAclIPAclBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1)
)
hpnicfAclIPAclBasicEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNumberGroupType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNumberGroupIndex"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclIPAclBasicRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicEntry.setStatus("current")


class _HpnicfAclIPAclBasicRuleIndex_Type(Integer32):
    """Custom type hpnicfAclIPAclBasicRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HpnicfAclIPAclBasicRuleIndex_Type.__name__ = "Integer32"
_HpnicfAclIPAclBasicRuleIndex_Object = MibTableColumn
hpnicfAclIPAclBasicRuleIndex = _HpnicfAclIPAclBasicRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 1),
    _HpnicfAclIPAclBasicRuleIndex_Type()
)
hpnicfAclIPAclBasicRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicRuleIndex.setStatus("current")
_HpnicfAclIPAclBasicRowStatus_Type = RowStatus
_HpnicfAclIPAclBasicRowStatus_Object = MibTableColumn
hpnicfAclIPAclBasicRowStatus = _HpnicfAclIPAclBasicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 2),
    _HpnicfAclIPAclBasicRowStatus_Type()
)
hpnicfAclIPAclBasicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicRowStatus.setStatus("current")
_HpnicfAclIPAclBasicAct_Type = RuleAction
_HpnicfAclIPAclBasicAct_Object = MibTableColumn
hpnicfAclIPAclBasicAct = _HpnicfAclIPAclBasicAct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 3),
    _HpnicfAclIPAclBasicAct_Type()
)
hpnicfAclIPAclBasicAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicAct.setStatus("current")
_HpnicfAclIPAclBasicSrcAddrType_Type = InetAddressType
_HpnicfAclIPAclBasicSrcAddrType_Object = MibTableColumn
hpnicfAclIPAclBasicSrcAddrType = _HpnicfAclIPAclBasicSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 4),
    _HpnicfAclIPAclBasicSrcAddrType_Type()
)
hpnicfAclIPAclBasicSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicSrcAddrType.setStatus("current")
_HpnicfAclIPAclBasicSrcAddr_Type = InetAddress
_HpnicfAclIPAclBasicSrcAddr_Object = MibTableColumn
hpnicfAclIPAclBasicSrcAddr = _HpnicfAclIPAclBasicSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 5),
    _HpnicfAclIPAclBasicSrcAddr_Type()
)
hpnicfAclIPAclBasicSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicSrcAddr.setStatus("current")
_HpnicfAclIPAclBasicSrcPrefix_Type = InetAddressPrefixLength
_HpnicfAclIPAclBasicSrcPrefix_Object = MibTableColumn
hpnicfAclIPAclBasicSrcPrefix = _HpnicfAclIPAclBasicSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 6),
    _HpnicfAclIPAclBasicSrcPrefix_Type()
)
hpnicfAclIPAclBasicSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicSrcPrefix.setStatus("current")


class _HpnicfAclIPAclBasicSrcAny_Type(TruthValue):
    """Custom type hpnicfAclIPAclBasicSrcAny based on TruthValue"""
    defaultValue = 1


_HpnicfAclIPAclBasicSrcAny_Type.__name__ = "TruthValue"
_HpnicfAclIPAclBasicSrcAny_Object = MibTableColumn
hpnicfAclIPAclBasicSrcAny = _HpnicfAclIPAclBasicSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 7),
    _HpnicfAclIPAclBasicSrcAny_Type()
)
hpnicfAclIPAclBasicSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicSrcAny.setStatus("current")
_HpnicfAclIPAclBasicSrcWild_Type = IpAddress
_HpnicfAclIPAclBasicSrcWild_Object = MibTableColumn
hpnicfAclIPAclBasicSrcWild = _HpnicfAclIPAclBasicSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 8),
    _HpnicfAclIPAclBasicSrcWild_Type()
)
hpnicfAclIPAclBasicSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicSrcWild.setStatus("current")


class _HpnicfAclIPAclBasicTimeRangeName_Type(OctetString):
    """Custom type hpnicfAclIPAclBasicTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclIPAclBasicTimeRangeName_Type.__name__ = "OctetString"
_HpnicfAclIPAclBasicTimeRangeName_Object = MibTableColumn
hpnicfAclIPAclBasicTimeRangeName = _HpnicfAclIPAclBasicTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 9),
    _HpnicfAclIPAclBasicTimeRangeName_Type()
)
hpnicfAclIPAclBasicTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicTimeRangeName.setStatus("current")


class _HpnicfAclIPAclBasicFragmentFlag_Type(FragmentFlag):
    """Custom type hpnicfAclIPAclBasicFragmentFlag based on FragmentFlag"""
    defaultValue = 0


_HpnicfAclIPAclBasicFragmentFlag_Type.__name__ = "FragmentFlag"
_HpnicfAclIPAclBasicFragmentFlag_Object = MibTableColumn
hpnicfAclIPAclBasicFragmentFlag = _HpnicfAclIPAclBasicFragmentFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 10),
    _HpnicfAclIPAclBasicFragmentFlag_Type()
)
hpnicfAclIPAclBasicFragmentFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicFragmentFlag.setStatus("current")


class _HpnicfAclIPAclBasicLog_Type(TruthValue):
    """Custom type hpnicfAclIPAclBasicLog based on TruthValue"""
    defaultValue = 2


_HpnicfAclIPAclBasicLog_Type.__name__ = "TruthValue"
_HpnicfAclIPAclBasicLog_Object = MibTableColumn
hpnicfAclIPAclBasicLog = _HpnicfAclIPAclBasicLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 11),
    _HpnicfAclIPAclBasicLog_Type()
)
hpnicfAclIPAclBasicLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicLog.setStatus("current")
_HpnicfAclIPAclBasicCount_Type = Unsigned32
_HpnicfAclIPAclBasicCount_Object = MibTableColumn
hpnicfAclIPAclBasicCount = _HpnicfAclIPAclBasicCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 12),
    _HpnicfAclIPAclBasicCount_Type()
)
hpnicfAclIPAclBasicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicCount.setStatus("current")


class _HpnicfAclIPAclBasicCountClear_Type(CounterClear):
    """Custom type hpnicfAclIPAclBasicCountClear based on CounterClear"""
    defaultValue = 2


_HpnicfAclIPAclBasicCountClear_Type.__name__ = "CounterClear"
_HpnicfAclIPAclBasicCountClear_Object = MibTableColumn
hpnicfAclIPAclBasicCountClear = _HpnicfAclIPAclBasicCountClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 13),
    _HpnicfAclIPAclBasicCountClear_Type()
)
hpnicfAclIPAclBasicCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicCountClear.setStatus("current")


class _HpnicfAclIPAclBasicEnable_Type(TruthValue):
    """Custom type hpnicfAclIPAclBasicEnable based on TruthValue"""
    defaultValue = 2


_HpnicfAclIPAclBasicEnable_Type.__name__ = "TruthValue"
_HpnicfAclIPAclBasicEnable_Object = MibTableColumn
hpnicfAclIPAclBasicEnable = _HpnicfAclIPAclBasicEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 14),
    _HpnicfAclIPAclBasicEnable_Type()
)
hpnicfAclIPAclBasicEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicEnable.setStatus("current")


class _HpnicfAclIPAclBasicVpnInstanceName_Type(OctetString):
    """Custom type hpnicfAclIPAclBasicVpnInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclIPAclBasicVpnInstanceName_Type.__name__ = "OctetString"
_HpnicfAclIPAclBasicVpnInstanceName_Object = MibTableColumn
hpnicfAclIPAclBasicVpnInstanceName = _HpnicfAclIPAclBasicVpnInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 15),
    _HpnicfAclIPAclBasicVpnInstanceName_Type()
)
hpnicfAclIPAclBasicVpnInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicVpnInstanceName.setStatus("current")


class _HpnicfAclIPAclBasicComment_Type(OctetString):
    """Custom type hpnicfAclIPAclBasicComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfAclIPAclBasicComment_Type.__name__ = "OctetString"
_HpnicfAclIPAclBasicComment_Object = MibTableColumn
hpnicfAclIPAclBasicComment = _HpnicfAclIPAclBasicComment_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 16),
    _HpnicfAclIPAclBasicComment_Type()
)
hpnicfAclIPAclBasicComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicComment.setStatus("current")


class _HpnicfAclIPAclBasicCounting_Type(TruthValue):
    """Custom type hpnicfAclIPAclBasicCounting based on TruthValue"""
    defaultValue = 2


_HpnicfAclIPAclBasicCounting_Type.__name__ = "TruthValue"
_HpnicfAclIPAclBasicCounting_Object = MibTableColumn
hpnicfAclIPAclBasicCounting = _HpnicfAclIPAclBasicCounting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 17),
    _HpnicfAclIPAclBasicCounting_Type()
)
hpnicfAclIPAclBasicCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicCounting.setStatus("current")


class _HpnicfAclIPAclBasicRouteTypeAny_Type(TruthValue):
    """Custom type hpnicfAclIPAclBasicRouteTypeAny based on TruthValue"""
    defaultValue = 2


_HpnicfAclIPAclBasicRouteTypeAny_Type.__name__ = "TruthValue"
_HpnicfAclIPAclBasicRouteTypeAny_Object = MibTableColumn
hpnicfAclIPAclBasicRouteTypeAny = _HpnicfAclIPAclBasicRouteTypeAny_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 18),
    _HpnicfAclIPAclBasicRouteTypeAny_Type()
)
hpnicfAclIPAclBasicRouteTypeAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicRouteTypeAny.setStatus("current")


class _HpnicfAclIPAclBasicRouteTypeValue_Type(Integer32):
    """Custom type hpnicfAclIPAclBasicRouteTypeValue based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfAclIPAclBasicRouteTypeValue_Type.__name__ = "Integer32"
_HpnicfAclIPAclBasicRouteTypeValue_Object = MibTableColumn
hpnicfAclIPAclBasicRouteTypeValue = _HpnicfAclIPAclBasicRouteTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 2, 1, 19),
    _HpnicfAclIPAclBasicRouteTypeValue_Type()
)
hpnicfAclIPAclBasicRouteTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclBasicRouteTypeValue.setStatus("current")
_HpnicfAclIPAclAdvancedTable_Object = MibTable
hpnicfAclIPAclAdvancedTable = _HpnicfAclIPAclAdvancedTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedTable.setStatus("current")
_HpnicfAclIPAclAdvancedEntry_Object = MibTableRow
hpnicfAclIPAclAdvancedEntry = _HpnicfAclIPAclAdvancedEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1)
)
hpnicfAclIPAclAdvancedEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNumberGroupType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNumberGroupIndex"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclIPAclAdvancedRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedEntry.setStatus("current")


class _HpnicfAclIPAclAdvancedRuleIndex_Type(Integer32):
    """Custom type hpnicfAclIPAclAdvancedRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HpnicfAclIPAclAdvancedRuleIndex_Type.__name__ = "Integer32"
_HpnicfAclIPAclAdvancedRuleIndex_Object = MibTableColumn
hpnicfAclIPAclAdvancedRuleIndex = _HpnicfAclIPAclAdvancedRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 1),
    _HpnicfAclIPAclAdvancedRuleIndex_Type()
)
hpnicfAclIPAclAdvancedRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedRuleIndex.setStatus("current")
_HpnicfAclIPAclAdvancedRowStatus_Type = RowStatus
_HpnicfAclIPAclAdvancedRowStatus_Object = MibTableColumn
hpnicfAclIPAclAdvancedRowStatus = _HpnicfAclIPAclAdvancedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 2),
    _HpnicfAclIPAclAdvancedRowStatus_Type()
)
hpnicfAclIPAclAdvancedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedRowStatus.setStatus("current")
_HpnicfAclIPAclAdvancedAct_Type = RuleAction
_HpnicfAclIPAclAdvancedAct_Object = MibTableColumn
hpnicfAclIPAclAdvancedAct = _HpnicfAclIPAclAdvancedAct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 3),
    _HpnicfAclIPAclAdvancedAct_Type()
)
hpnicfAclIPAclAdvancedAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedAct.setStatus("current")


class _HpnicfAclIPAclAdvancedProtocol_Type(Integer32):
    """Custom type hpnicfAclIPAclAdvancedProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfAclIPAclAdvancedProtocol_Type.__name__ = "Integer32"
_HpnicfAclIPAclAdvancedProtocol_Object = MibTableColumn
hpnicfAclIPAclAdvancedProtocol = _HpnicfAclIPAclAdvancedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 4),
    _HpnicfAclIPAclAdvancedProtocol_Type()
)
hpnicfAclIPAclAdvancedProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedProtocol.setStatus("current")


class _HpnicfAclIPAclAdvancedAddrFlag_Type(AddressFlag):
    """Custom type hpnicfAclIPAclAdvancedAddrFlag based on AddressFlag"""
    defaultValue = 0


_HpnicfAclIPAclAdvancedAddrFlag_Type.__name__ = "AddressFlag"
_HpnicfAclIPAclAdvancedAddrFlag_Object = MibTableColumn
hpnicfAclIPAclAdvancedAddrFlag = _HpnicfAclIPAclAdvancedAddrFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 5),
    _HpnicfAclIPAclAdvancedAddrFlag_Type()
)
hpnicfAclIPAclAdvancedAddrFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedAddrFlag.setStatus("current")
_HpnicfAclIPAclAdvancedSrcAddrType_Type = InetAddressType
_HpnicfAclIPAclAdvancedSrcAddrType_Object = MibTableColumn
hpnicfAclIPAclAdvancedSrcAddrType = _HpnicfAclIPAclAdvancedSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 6),
    _HpnicfAclIPAclAdvancedSrcAddrType_Type()
)
hpnicfAclIPAclAdvancedSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedSrcAddrType.setStatus("current")
_HpnicfAclIPAclAdvancedSrcAddr_Type = InetAddress
_HpnicfAclIPAclAdvancedSrcAddr_Object = MibTableColumn
hpnicfAclIPAclAdvancedSrcAddr = _HpnicfAclIPAclAdvancedSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 7),
    _HpnicfAclIPAclAdvancedSrcAddr_Type()
)
hpnicfAclIPAclAdvancedSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedSrcAddr.setStatus("current")
_HpnicfAclIPAclAdvancedSrcPrefix_Type = InetAddressPrefixLength
_HpnicfAclIPAclAdvancedSrcPrefix_Object = MibTableColumn
hpnicfAclIPAclAdvancedSrcPrefix = _HpnicfAclIPAclAdvancedSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 8),
    _HpnicfAclIPAclAdvancedSrcPrefix_Type()
)
hpnicfAclIPAclAdvancedSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedSrcPrefix.setStatus("current")


class _HpnicfAclIPAclAdvancedSrcAny_Type(TruthValue):
    """Custom type hpnicfAclIPAclAdvancedSrcAny based on TruthValue"""
    defaultValue = 1


_HpnicfAclIPAclAdvancedSrcAny_Type.__name__ = "TruthValue"
_HpnicfAclIPAclAdvancedSrcAny_Object = MibTableColumn
hpnicfAclIPAclAdvancedSrcAny = _HpnicfAclIPAclAdvancedSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 9),
    _HpnicfAclIPAclAdvancedSrcAny_Type()
)
hpnicfAclIPAclAdvancedSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedSrcAny.setStatus("current")
_HpnicfAclIPAclAdvancedSrcWild_Type = IpAddress
_HpnicfAclIPAclAdvancedSrcWild_Object = MibTableColumn
hpnicfAclIPAclAdvancedSrcWild = _HpnicfAclIPAclAdvancedSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 10),
    _HpnicfAclIPAclAdvancedSrcWild_Type()
)
hpnicfAclIPAclAdvancedSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedSrcWild.setStatus("current")


class _HpnicfAclIPAclAdvancedSrcOp_Type(PortOp):
    """Custom type hpnicfAclIPAclAdvancedSrcOp based on PortOp"""
    defaultValue = 0


_HpnicfAclIPAclAdvancedSrcOp_Type.__name__ = "PortOp"
_HpnicfAclIPAclAdvancedSrcOp_Object = MibTableColumn
hpnicfAclIPAclAdvancedSrcOp = _HpnicfAclIPAclAdvancedSrcOp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 11),
    _HpnicfAclIPAclAdvancedSrcOp_Type()
)
hpnicfAclIPAclAdvancedSrcOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedSrcOp.setStatus("current")


class _HpnicfAclIPAclAdvancedSrcPort1_Type(Integer32):
    """Custom type hpnicfAclIPAclAdvancedSrcPort1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclIPAclAdvancedSrcPort1_Type.__name__ = "Integer32"
_HpnicfAclIPAclAdvancedSrcPort1_Object = MibTableColumn
hpnicfAclIPAclAdvancedSrcPort1 = _HpnicfAclIPAclAdvancedSrcPort1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 12),
    _HpnicfAclIPAclAdvancedSrcPort1_Type()
)
hpnicfAclIPAclAdvancedSrcPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedSrcPort1.setStatus("current")


class _HpnicfAclIPAclAdvancedSrcPort2_Type(Integer32):
    """Custom type hpnicfAclIPAclAdvancedSrcPort2 based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclIPAclAdvancedSrcPort2_Type.__name__ = "Integer32"
_HpnicfAclIPAclAdvancedSrcPort2_Object = MibTableColumn
hpnicfAclIPAclAdvancedSrcPort2 = _HpnicfAclIPAclAdvancedSrcPort2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 13),
    _HpnicfAclIPAclAdvancedSrcPort2_Type()
)
hpnicfAclIPAclAdvancedSrcPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedSrcPort2.setStatus("current")
_HpnicfAclIPAclAdvancedDestAddrType_Type = InetAddressType
_HpnicfAclIPAclAdvancedDestAddrType_Object = MibTableColumn
hpnicfAclIPAclAdvancedDestAddrType = _HpnicfAclIPAclAdvancedDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 14),
    _HpnicfAclIPAclAdvancedDestAddrType_Type()
)
hpnicfAclIPAclAdvancedDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedDestAddrType.setStatus("current")
_HpnicfAclIPAclAdvancedDestAddr_Type = InetAddress
_HpnicfAclIPAclAdvancedDestAddr_Object = MibTableColumn
hpnicfAclIPAclAdvancedDestAddr = _HpnicfAclIPAclAdvancedDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 15),
    _HpnicfAclIPAclAdvancedDestAddr_Type()
)
hpnicfAclIPAclAdvancedDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedDestAddr.setStatus("current")
_HpnicfAclIPAclAdvancedDestPrefix_Type = InetAddressPrefixLength
_HpnicfAclIPAclAdvancedDestPrefix_Object = MibTableColumn
hpnicfAclIPAclAdvancedDestPrefix = _HpnicfAclIPAclAdvancedDestPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 16),
    _HpnicfAclIPAclAdvancedDestPrefix_Type()
)
hpnicfAclIPAclAdvancedDestPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedDestPrefix.setStatus("current")


class _HpnicfAclIPAclAdvancedDestAny_Type(TruthValue):
    """Custom type hpnicfAclIPAclAdvancedDestAny based on TruthValue"""
    defaultValue = 1


_HpnicfAclIPAclAdvancedDestAny_Type.__name__ = "TruthValue"
_HpnicfAclIPAclAdvancedDestAny_Object = MibTableColumn
hpnicfAclIPAclAdvancedDestAny = _HpnicfAclIPAclAdvancedDestAny_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 17),
    _HpnicfAclIPAclAdvancedDestAny_Type()
)
hpnicfAclIPAclAdvancedDestAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedDestAny.setStatus("current")
_HpnicfAclIPAclAdvancedDestWild_Type = IpAddress
_HpnicfAclIPAclAdvancedDestWild_Object = MibTableColumn
hpnicfAclIPAclAdvancedDestWild = _HpnicfAclIPAclAdvancedDestWild_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 18),
    _HpnicfAclIPAclAdvancedDestWild_Type()
)
hpnicfAclIPAclAdvancedDestWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedDestWild.setStatus("current")


class _HpnicfAclIPAclAdvancedDestOp_Type(PortOp):
    """Custom type hpnicfAclIPAclAdvancedDestOp based on PortOp"""
    defaultValue = 0


_HpnicfAclIPAclAdvancedDestOp_Type.__name__ = "PortOp"
_HpnicfAclIPAclAdvancedDestOp_Object = MibTableColumn
hpnicfAclIPAclAdvancedDestOp = _HpnicfAclIPAclAdvancedDestOp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 19),
    _HpnicfAclIPAclAdvancedDestOp_Type()
)
hpnicfAclIPAclAdvancedDestOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedDestOp.setStatus("current")


class _HpnicfAclIPAclAdvancedDestPort1_Type(Integer32):
    """Custom type hpnicfAclIPAclAdvancedDestPort1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclIPAclAdvancedDestPort1_Type.__name__ = "Integer32"
_HpnicfAclIPAclAdvancedDestPort1_Object = MibTableColumn
hpnicfAclIPAclAdvancedDestPort1 = _HpnicfAclIPAclAdvancedDestPort1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 20),
    _HpnicfAclIPAclAdvancedDestPort1_Type()
)
hpnicfAclIPAclAdvancedDestPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedDestPort1.setStatus("current")


class _HpnicfAclIPAclAdvancedDestPort2_Type(Integer32):
    """Custom type hpnicfAclIPAclAdvancedDestPort2 based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclIPAclAdvancedDestPort2_Type.__name__ = "Integer32"
_HpnicfAclIPAclAdvancedDestPort2_Object = MibTableColumn
hpnicfAclIPAclAdvancedDestPort2 = _HpnicfAclIPAclAdvancedDestPort2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 21),
    _HpnicfAclIPAclAdvancedDestPort2_Type()
)
hpnicfAclIPAclAdvancedDestPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedDestPort2.setStatus("current")


class _HpnicfAclIPAclAdvancedIcmpType_Type(Integer32):
    """Custom type hpnicfAclIPAclAdvancedIcmpType based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfAclIPAclAdvancedIcmpType_Type.__name__ = "Integer32"
_HpnicfAclIPAclAdvancedIcmpType_Object = MibTableColumn
hpnicfAclIPAclAdvancedIcmpType = _HpnicfAclIPAclAdvancedIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 22),
    _HpnicfAclIPAclAdvancedIcmpType_Type()
)
hpnicfAclIPAclAdvancedIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedIcmpType.setStatus("current")


class _HpnicfAclIPAclAdvancedIcmpCode_Type(Integer32):
    """Custom type hpnicfAclIPAclAdvancedIcmpCode based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfAclIPAclAdvancedIcmpCode_Type.__name__ = "Integer32"
_HpnicfAclIPAclAdvancedIcmpCode_Object = MibTableColumn
hpnicfAclIPAclAdvancedIcmpCode = _HpnicfAclIPAclAdvancedIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 23),
    _HpnicfAclIPAclAdvancedIcmpCode_Type()
)
hpnicfAclIPAclAdvancedIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedIcmpCode.setStatus("current")


class _HpnicfAclIPAclAdvancedPrecedence_Type(Integer32):
    """Custom type hpnicfAclIPAclAdvancedPrecedence based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfAclIPAclAdvancedPrecedence_Type.__name__ = "Integer32"
_HpnicfAclIPAclAdvancedPrecedence_Object = MibTableColumn
hpnicfAclIPAclAdvancedPrecedence = _HpnicfAclIPAclAdvancedPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 24),
    _HpnicfAclIPAclAdvancedPrecedence_Type()
)
hpnicfAclIPAclAdvancedPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedPrecedence.setStatus("current")


class _HpnicfAclIPAclAdvancedTos_Type(Integer32):
    """Custom type hpnicfAclIPAclAdvancedTos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_HpnicfAclIPAclAdvancedTos_Type.__name__ = "Integer32"
_HpnicfAclIPAclAdvancedTos_Object = MibTableColumn
hpnicfAclIPAclAdvancedTos = _HpnicfAclIPAclAdvancedTos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 25),
    _HpnicfAclIPAclAdvancedTos_Type()
)
hpnicfAclIPAclAdvancedTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedTos.setStatus("current")


class _HpnicfAclIPAclAdvancedDscp_Type(DSCPValue):
    """Custom type hpnicfAclIPAclAdvancedDscp based on DSCPValue"""
    defaultValue = 255


_HpnicfAclIPAclAdvancedDscp_Type.__name__ = "DSCPValue"
_HpnicfAclIPAclAdvancedDscp_Object = MibTableColumn
hpnicfAclIPAclAdvancedDscp = _HpnicfAclIPAclAdvancedDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 26),
    _HpnicfAclIPAclAdvancedDscp_Type()
)
hpnicfAclIPAclAdvancedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedDscp.setStatus("current")


class _HpnicfAclIPAclAdvancedTimeRangeName_Type(OctetString):
    """Custom type hpnicfAclIPAclAdvancedTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclIPAclAdvancedTimeRangeName_Type.__name__ = "OctetString"
_HpnicfAclIPAclAdvancedTimeRangeName_Object = MibTableColumn
hpnicfAclIPAclAdvancedTimeRangeName = _HpnicfAclIPAclAdvancedTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 27),
    _HpnicfAclIPAclAdvancedTimeRangeName_Type()
)
hpnicfAclIPAclAdvancedTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedTimeRangeName.setStatus("current")


class _HpnicfAclIPAclAdvancedTCPFlag_Type(TCPFlag):
    """Custom type hpnicfAclIPAclAdvancedTCPFlag based on TCPFlag"""
    defaultValue = 0


_HpnicfAclIPAclAdvancedTCPFlag_Type.__name__ = "TCPFlag"
_HpnicfAclIPAclAdvancedTCPFlag_Object = MibTableColumn
hpnicfAclIPAclAdvancedTCPFlag = _HpnicfAclIPAclAdvancedTCPFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 28),
    _HpnicfAclIPAclAdvancedTCPFlag_Type()
)
hpnicfAclIPAclAdvancedTCPFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedTCPFlag.setStatus("current")


class _HpnicfAclIPAclAdvancedFragmentFlag_Type(FragmentFlag):
    """Custom type hpnicfAclIPAclAdvancedFragmentFlag based on FragmentFlag"""
    defaultValue = 0


_HpnicfAclIPAclAdvancedFragmentFlag_Type.__name__ = "FragmentFlag"
_HpnicfAclIPAclAdvancedFragmentFlag_Object = MibTableColumn
hpnicfAclIPAclAdvancedFragmentFlag = _HpnicfAclIPAclAdvancedFragmentFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 29),
    _HpnicfAclIPAclAdvancedFragmentFlag_Type()
)
hpnicfAclIPAclAdvancedFragmentFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedFragmentFlag.setStatus("current")


class _HpnicfAclIPAclAdvancedLog_Type(TruthValue):
    """Custom type hpnicfAclIPAclAdvancedLog based on TruthValue"""
    defaultValue = 2


_HpnicfAclIPAclAdvancedLog_Type.__name__ = "TruthValue"
_HpnicfAclIPAclAdvancedLog_Object = MibTableColumn
hpnicfAclIPAclAdvancedLog = _HpnicfAclIPAclAdvancedLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 30),
    _HpnicfAclIPAclAdvancedLog_Type()
)
hpnicfAclIPAclAdvancedLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedLog.setStatus("current")
_HpnicfAclIPAclAdvancedCount_Type = Unsigned32
_HpnicfAclIPAclAdvancedCount_Object = MibTableColumn
hpnicfAclIPAclAdvancedCount = _HpnicfAclIPAclAdvancedCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 31),
    _HpnicfAclIPAclAdvancedCount_Type()
)
hpnicfAclIPAclAdvancedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedCount.setStatus("current")


class _HpnicfAclIPAclAdvancedCountClear_Type(CounterClear):
    """Custom type hpnicfAclIPAclAdvancedCountClear based on CounterClear"""
    defaultValue = 2


_HpnicfAclIPAclAdvancedCountClear_Type.__name__ = "CounterClear"
_HpnicfAclIPAclAdvancedCountClear_Object = MibTableColumn
hpnicfAclIPAclAdvancedCountClear = _HpnicfAclIPAclAdvancedCountClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 32),
    _HpnicfAclIPAclAdvancedCountClear_Type()
)
hpnicfAclIPAclAdvancedCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedCountClear.setStatus("current")


class _HpnicfAclIPAclAdvancedEnable_Type(TruthValue):
    """Custom type hpnicfAclIPAclAdvancedEnable based on TruthValue"""
    defaultValue = 2


_HpnicfAclIPAclAdvancedEnable_Type.__name__ = "TruthValue"
_HpnicfAclIPAclAdvancedEnable_Object = MibTableColumn
hpnicfAclIPAclAdvancedEnable = _HpnicfAclIPAclAdvancedEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 33),
    _HpnicfAclIPAclAdvancedEnable_Type()
)
hpnicfAclIPAclAdvancedEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedEnable.setStatus("current")


class _HpnicfAclIPAclAdvancedVpnInstanceName_Type(OctetString):
    """Custom type hpnicfAclIPAclAdvancedVpnInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclIPAclAdvancedVpnInstanceName_Type.__name__ = "OctetString"
_HpnicfAclIPAclAdvancedVpnInstanceName_Object = MibTableColumn
hpnicfAclIPAclAdvancedVpnInstanceName = _HpnicfAclIPAclAdvancedVpnInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 34),
    _HpnicfAclIPAclAdvancedVpnInstanceName_Type()
)
hpnicfAclIPAclAdvancedVpnInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedVpnInstanceName.setStatus("current")


class _HpnicfAclIPAclAdvancedComment_Type(OctetString):
    """Custom type hpnicfAclIPAclAdvancedComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfAclIPAclAdvancedComment_Type.__name__ = "OctetString"
_HpnicfAclIPAclAdvancedComment_Object = MibTableColumn
hpnicfAclIPAclAdvancedComment = _HpnicfAclIPAclAdvancedComment_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 35),
    _HpnicfAclIPAclAdvancedComment_Type()
)
hpnicfAclIPAclAdvancedComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedComment.setStatus("current")
_HpnicfAclIPAclAdvancedReflective_Type = TruthValue
_HpnicfAclIPAclAdvancedReflective_Object = MibTableColumn
hpnicfAclIPAclAdvancedReflective = _HpnicfAclIPAclAdvancedReflective_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 36),
    _HpnicfAclIPAclAdvancedReflective_Type()
)
hpnicfAclIPAclAdvancedReflective.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedReflective.setStatus("current")


class _HpnicfAclIPAclAdvancedCounting_Type(TruthValue):
    """Custom type hpnicfAclIPAclAdvancedCounting based on TruthValue"""
    defaultValue = 2


_HpnicfAclIPAclAdvancedCounting_Type.__name__ = "TruthValue"
_HpnicfAclIPAclAdvancedCounting_Object = MibTableColumn
hpnicfAclIPAclAdvancedCounting = _HpnicfAclIPAclAdvancedCounting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 37),
    _HpnicfAclIPAclAdvancedCounting_Type()
)
hpnicfAclIPAclAdvancedCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedCounting.setStatus("current")


class _HpnicfAclIPAclAdvancedTCPFlagMask_Type(Bits):
    """Custom type hpnicfAclIPAclAdvancedTCPFlagMask based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("tcpack", 0),
          ("tcpfin", 1),
          ("tcppsh", 2),
          ("tcprst", 3),
          ("tcpsyn", 4),
          ("tcpurg", 5))
    )

_HpnicfAclIPAclAdvancedTCPFlagMask_Type.__name__ = "Bits"
_HpnicfAclIPAclAdvancedTCPFlagMask_Object = MibTableColumn
hpnicfAclIPAclAdvancedTCPFlagMask = _HpnicfAclIPAclAdvancedTCPFlagMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 38),
    _HpnicfAclIPAclAdvancedTCPFlagMask_Type()
)
hpnicfAclIPAclAdvancedTCPFlagMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedTCPFlagMask.setStatus("current")


class _HpnicfAclIPAclAdvancedTCPFlagValue_Type(Bits):
    """Custom type hpnicfAclIPAclAdvancedTCPFlagValue based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("tcpack", 0),
          ("tcpfin", 1),
          ("tcppsh", 2),
          ("tcprst", 3),
          ("tcpsyn", 4),
          ("tcpurg", 5))
    )

_HpnicfAclIPAclAdvancedTCPFlagValue_Type.__name__ = "Bits"
_HpnicfAclIPAclAdvancedTCPFlagValue_Object = MibTableColumn
hpnicfAclIPAclAdvancedTCPFlagValue = _HpnicfAclIPAclAdvancedTCPFlagValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 39),
    _HpnicfAclIPAclAdvancedTCPFlagValue_Type()
)
hpnicfAclIPAclAdvancedTCPFlagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedTCPFlagValue.setStatus("current")


class _HpnicfAclIPAclAdvancedRouteTypeAny_Type(TruthValue):
    """Custom type hpnicfAclIPAclAdvancedRouteTypeAny based on TruthValue"""
    defaultValue = 2


_HpnicfAclIPAclAdvancedRouteTypeAny_Type.__name__ = "TruthValue"
_HpnicfAclIPAclAdvancedRouteTypeAny_Object = MibTableColumn
hpnicfAclIPAclAdvancedRouteTypeAny = _HpnicfAclIPAclAdvancedRouteTypeAny_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 40),
    _HpnicfAclIPAclAdvancedRouteTypeAny_Type()
)
hpnicfAclIPAclAdvancedRouteTypeAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedRouteTypeAny.setStatus("current")


class _HpnicfAclIPAclAdvancedRouteTypeValue_Type(Integer32):
    """Custom type hpnicfAclIPAclAdvancedRouteTypeValue based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfAclIPAclAdvancedRouteTypeValue_Type.__name__ = "Integer32"
_HpnicfAclIPAclAdvancedRouteTypeValue_Object = MibTableColumn
hpnicfAclIPAclAdvancedRouteTypeValue = _HpnicfAclIPAclAdvancedRouteTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 41),
    _HpnicfAclIPAclAdvancedRouteTypeValue_Type()
)
hpnicfAclIPAclAdvancedRouteTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedRouteTypeValue.setStatus("current")


class _HpnicfAclIPAclAdvancedFlowLabel_Type(Unsigned32):
    """Custom type hpnicfAclIPAclAdvancedFlowLabel based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_HpnicfAclIPAclAdvancedFlowLabel_Type.__name__ = "Unsigned32"
_HpnicfAclIPAclAdvancedFlowLabel_Object = MibTableColumn
hpnicfAclIPAclAdvancedFlowLabel = _HpnicfAclIPAclAdvancedFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 42),
    _HpnicfAclIPAclAdvancedFlowLabel_Type()
)
hpnicfAclIPAclAdvancedFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedFlowLabel.setStatus("current")
_HpnicfAclIPAclAdvancedSrcSuffix_Type = Unsigned32
_HpnicfAclIPAclAdvancedSrcSuffix_Object = MibTableColumn
hpnicfAclIPAclAdvancedSrcSuffix = _HpnicfAclIPAclAdvancedSrcSuffix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 43),
    _HpnicfAclIPAclAdvancedSrcSuffix_Type()
)
hpnicfAclIPAclAdvancedSrcSuffix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedSrcSuffix.setStatus("current")
_HpnicfAclIPAclAdvancedDestSuffix_Type = Unsigned32
_HpnicfAclIPAclAdvancedDestSuffix_Object = MibTableColumn
hpnicfAclIPAclAdvancedDestSuffix = _HpnicfAclIPAclAdvancedDestSuffix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 3, 1, 44),
    _HpnicfAclIPAclAdvancedDestSuffix_Type()
)
hpnicfAclIPAclAdvancedDestSuffix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclAdvancedDestSuffix.setStatus("current")
_HpnicfAclIPAclNamedBscTable_Object = MibTable
hpnicfAclIPAclNamedBscTable = _HpnicfAclIPAclNamedBscTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscTable.setStatus("current")
_HpnicfAclIPAclNamedBscEntry_Object = MibTableRow
hpnicfAclIPAclNamedBscEntry = _HpnicfAclIPAclNamedBscEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1)
)
hpnicfAclIPAclNamedBscEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNumberGroupType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNamedGroupName"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclIPAclBasicRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscEntry.setStatus("current")
_HpnicfAclIPAclNamedBscRowStatus_Type = RowStatus
_HpnicfAclIPAclNamedBscRowStatus_Object = MibTableColumn
hpnicfAclIPAclNamedBscRowStatus = _HpnicfAclIPAclNamedBscRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1, 1),
    _HpnicfAclIPAclNamedBscRowStatus_Type()
)
hpnicfAclIPAclNamedBscRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscRowStatus.setStatus("current")
_HpnicfAclIPAclNamedBscAct_Type = RuleAction
_HpnicfAclIPAclNamedBscAct_Object = MibTableColumn
hpnicfAclIPAclNamedBscAct = _HpnicfAclIPAclNamedBscAct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1, 2),
    _HpnicfAclIPAclNamedBscAct_Type()
)
hpnicfAclIPAclNamedBscAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscAct.setStatus("current")
_HpnicfAclIPAclNamedBscSrcAddrType_Type = InetAddressType
_HpnicfAclIPAclNamedBscSrcAddrType_Object = MibTableColumn
hpnicfAclIPAclNamedBscSrcAddrType = _HpnicfAclIPAclNamedBscSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1, 3),
    _HpnicfAclIPAclNamedBscSrcAddrType_Type()
)
hpnicfAclIPAclNamedBscSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscSrcAddrType.setStatus("current")
_HpnicfAclIPAclNamedBscSrcAddr_Type = InetAddress
_HpnicfAclIPAclNamedBscSrcAddr_Object = MibTableColumn
hpnicfAclIPAclNamedBscSrcAddr = _HpnicfAclIPAclNamedBscSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1, 4),
    _HpnicfAclIPAclNamedBscSrcAddr_Type()
)
hpnicfAclIPAclNamedBscSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscSrcAddr.setStatus("current")
_HpnicfAclIPAclNamedBscSrcPrefix_Type = InetAddressPrefixLength
_HpnicfAclIPAclNamedBscSrcPrefix_Object = MibTableColumn
hpnicfAclIPAclNamedBscSrcPrefix = _HpnicfAclIPAclNamedBscSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1, 5),
    _HpnicfAclIPAclNamedBscSrcPrefix_Type()
)
hpnicfAclIPAclNamedBscSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscSrcPrefix.setStatus("current")


class _HpnicfAclIPAclNamedBscSrcAny_Type(TruthValue):
    """Custom type hpnicfAclIPAclNamedBscSrcAny based on TruthValue"""
    defaultValue = 1


_HpnicfAclIPAclNamedBscSrcAny_Type.__name__ = "TruthValue"
_HpnicfAclIPAclNamedBscSrcAny_Object = MibTableColumn
hpnicfAclIPAclNamedBscSrcAny = _HpnicfAclIPAclNamedBscSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1, 6),
    _HpnicfAclIPAclNamedBscSrcAny_Type()
)
hpnicfAclIPAclNamedBscSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscSrcAny.setStatus("current")
_HpnicfAclIPAclNamedBscSrcWild_Type = IpAddress
_HpnicfAclIPAclNamedBscSrcWild_Object = MibTableColumn
hpnicfAclIPAclNamedBscSrcWild = _HpnicfAclIPAclNamedBscSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1, 7),
    _HpnicfAclIPAclNamedBscSrcWild_Type()
)
hpnicfAclIPAclNamedBscSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscSrcWild.setStatus("current")


class _HpnicfAclIPAclNamedBscTRangeName_Type(OctetString):
    """Custom type hpnicfAclIPAclNamedBscTRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclIPAclNamedBscTRangeName_Type.__name__ = "OctetString"
_HpnicfAclIPAclNamedBscTRangeName_Object = MibTableColumn
hpnicfAclIPAclNamedBscTRangeName = _HpnicfAclIPAclNamedBscTRangeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1, 8),
    _HpnicfAclIPAclNamedBscTRangeName_Type()
)
hpnicfAclIPAclNamedBscTRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscTRangeName.setStatus("current")


class _HpnicfAclIPAclNamedBscFragmentFlag_Type(FragmentFlag):
    """Custom type hpnicfAclIPAclNamedBscFragmentFlag based on FragmentFlag"""
    defaultValue = 0


_HpnicfAclIPAclNamedBscFragmentFlag_Type.__name__ = "FragmentFlag"
_HpnicfAclIPAclNamedBscFragmentFlag_Object = MibTableColumn
hpnicfAclIPAclNamedBscFragmentFlag = _HpnicfAclIPAclNamedBscFragmentFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1, 9),
    _HpnicfAclIPAclNamedBscFragmentFlag_Type()
)
hpnicfAclIPAclNamedBscFragmentFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscFragmentFlag.setStatus("current")


class _HpnicfAclIPAclNamedBscLog_Type(TruthValue):
    """Custom type hpnicfAclIPAclNamedBscLog based on TruthValue"""
    defaultValue = 2


_HpnicfAclIPAclNamedBscLog_Type.__name__ = "TruthValue"
_HpnicfAclIPAclNamedBscLog_Object = MibTableColumn
hpnicfAclIPAclNamedBscLog = _HpnicfAclIPAclNamedBscLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1, 10),
    _HpnicfAclIPAclNamedBscLog_Type()
)
hpnicfAclIPAclNamedBscLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscLog.setStatus("current")
_HpnicfAclIPAclNamedBscCount_Type = Unsigned32
_HpnicfAclIPAclNamedBscCount_Object = MibTableColumn
hpnicfAclIPAclNamedBscCount = _HpnicfAclIPAclNamedBscCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1, 11),
    _HpnicfAclIPAclNamedBscCount_Type()
)
hpnicfAclIPAclNamedBscCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscCount.setStatus("current")


class _HpnicfAclIPAclNamedBscCountClear_Type(CounterClear):
    """Custom type hpnicfAclIPAclNamedBscCountClear based on CounterClear"""
    defaultValue = 2


_HpnicfAclIPAclNamedBscCountClear_Type.__name__ = "CounterClear"
_HpnicfAclIPAclNamedBscCountClear_Object = MibTableColumn
hpnicfAclIPAclNamedBscCountClear = _HpnicfAclIPAclNamedBscCountClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1, 12),
    _HpnicfAclIPAclNamedBscCountClear_Type()
)
hpnicfAclIPAclNamedBscCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscCountClear.setStatus("current")


class _HpnicfAclIPAclNamedBscEnable_Type(TruthValue):
    """Custom type hpnicfAclIPAclNamedBscEnable based on TruthValue"""
    defaultValue = 2


_HpnicfAclIPAclNamedBscEnable_Type.__name__ = "TruthValue"
_HpnicfAclIPAclNamedBscEnable_Object = MibTableColumn
hpnicfAclIPAclNamedBscEnable = _HpnicfAclIPAclNamedBscEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1, 13),
    _HpnicfAclIPAclNamedBscEnable_Type()
)
hpnicfAclIPAclNamedBscEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscEnable.setStatus("current")


class _HpnicfAclIPAclNamedBscVpnInstName_Type(OctetString):
    """Custom type hpnicfAclIPAclNamedBscVpnInstName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclIPAclNamedBscVpnInstName_Type.__name__ = "OctetString"
_HpnicfAclIPAclNamedBscVpnInstName_Object = MibTableColumn
hpnicfAclIPAclNamedBscVpnInstName = _HpnicfAclIPAclNamedBscVpnInstName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1, 14),
    _HpnicfAclIPAclNamedBscVpnInstName_Type()
)
hpnicfAclIPAclNamedBscVpnInstName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscVpnInstName.setStatus("current")


class _HpnicfAclIPAclNamedBscComment_Type(OctetString):
    """Custom type hpnicfAclIPAclNamedBscComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfAclIPAclNamedBscComment_Type.__name__ = "OctetString"
_HpnicfAclIPAclNamedBscComment_Object = MibTableColumn
hpnicfAclIPAclNamedBscComment = _HpnicfAclIPAclNamedBscComment_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1, 15),
    _HpnicfAclIPAclNamedBscComment_Type()
)
hpnicfAclIPAclNamedBscComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscComment.setStatus("current")


class _HpnicfAclIPAclNamedBscCounting_Type(TruthValue):
    """Custom type hpnicfAclIPAclNamedBscCounting based on TruthValue"""
    defaultValue = 2


_HpnicfAclIPAclNamedBscCounting_Type.__name__ = "TruthValue"
_HpnicfAclIPAclNamedBscCounting_Object = MibTableColumn
hpnicfAclIPAclNamedBscCounting = _HpnicfAclIPAclNamedBscCounting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1, 16),
    _HpnicfAclIPAclNamedBscCounting_Type()
)
hpnicfAclIPAclNamedBscCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscCounting.setStatus("current")


class _HpnicfAclIPAclNamedBscRouteTypeAny_Type(TruthValue):
    """Custom type hpnicfAclIPAclNamedBscRouteTypeAny based on TruthValue"""
    defaultValue = 2


_HpnicfAclIPAclNamedBscRouteTypeAny_Type.__name__ = "TruthValue"
_HpnicfAclIPAclNamedBscRouteTypeAny_Object = MibTableColumn
hpnicfAclIPAclNamedBscRouteTypeAny = _HpnicfAclIPAclNamedBscRouteTypeAny_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1, 17),
    _HpnicfAclIPAclNamedBscRouteTypeAny_Type()
)
hpnicfAclIPAclNamedBscRouteTypeAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscRouteTypeAny.setStatus("current")


class _HpnicfAclIPAclNamedBscRouteTypeValue_Type(Integer32):
    """Custom type hpnicfAclIPAclNamedBscRouteTypeValue based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfAclIPAclNamedBscRouteTypeValue_Type.__name__ = "Integer32"
_HpnicfAclIPAclNamedBscRouteTypeValue_Object = MibTableColumn
hpnicfAclIPAclNamedBscRouteTypeValue = _HpnicfAclIPAclNamedBscRouteTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 4, 1, 18),
    _HpnicfAclIPAclNamedBscRouteTypeValue_Type()
)
hpnicfAclIPAclNamedBscRouteTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedBscRouteTypeValue.setStatus("current")
_HpnicfAclIPAclNamedAdvTable_Object = MibTable
hpnicfAclIPAclNamedAdvTable = _HpnicfAclIPAclNamedAdvTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvTable.setStatus("current")
_HpnicfAclIPAclNamedAdvEntry_Object = MibTableRow
hpnicfAclIPAclNamedAdvEntry = _HpnicfAclIPAclNamedAdvEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1)
)
hpnicfAclIPAclNamedAdvEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNumberGroupType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNamedGroupName"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclIPAclAdvancedRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvEntry.setStatus("current")
_HpnicfAclIPAclNamedAdvRowStatus_Type = RowStatus
_HpnicfAclIPAclNamedAdvRowStatus_Object = MibTableColumn
hpnicfAclIPAclNamedAdvRowStatus = _HpnicfAclIPAclNamedAdvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 1),
    _HpnicfAclIPAclNamedAdvRowStatus_Type()
)
hpnicfAclIPAclNamedAdvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvRowStatus.setStatus("current")
_HpnicfAclIPAclNamedAdvAct_Type = RuleAction
_HpnicfAclIPAclNamedAdvAct_Object = MibTableColumn
hpnicfAclIPAclNamedAdvAct = _HpnicfAclIPAclNamedAdvAct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 2),
    _HpnicfAclIPAclNamedAdvAct_Type()
)
hpnicfAclIPAclNamedAdvAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvAct.setStatus("current")


class _HpnicfAclIPAclNamedAdvProtocol_Type(Integer32):
    """Custom type hpnicfAclIPAclNamedAdvProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfAclIPAclNamedAdvProtocol_Type.__name__ = "Integer32"
_HpnicfAclIPAclNamedAdvProtocol_Object = MibTableColumn
hpnicfAclIPAclNamedAdvProtocol = _HpnicfAclIPAclNamedAdvProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 3),
    _HpnicfAclIPAclNamedAdvProtocol_Type()
)
hpnicfAclIPAclNamedAdvProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvProtocol.setStatus("current")


class _HpnicfAclIPAclNamedAdvAddrFlag_Type(AddressFlag):
    """Custom type hpnicfAclIPAclNamedAdvAddrFlag based on AddressFlag"""
    defaultValue = 0


_HpnicfAclIPAclNamedAdvAddrFlag_Type.__name__ = "AddressFlag"
_HpnicfAclIPAclNamedAdvAddrFlag_Object = MibTableColumn
hpnicfAclIPAclNamedAdvAddrFlag = _HpnicfAclIPAclNamedAdvAddrFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 4),
    _HpnicfAclIPAclNamedAdvAddrFlag_Type()
)
hpnicfAclIPAclNamedAdvAddrFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvAddrFlag.setStatus("current")
_HpnicfAclIPAclNamedAdvSrcAddrType_Type = InetAddressType
_HpnicfAclIPAclNamedAdvSrcAddrType_Object = MibTableColumn
hpnicfAclIPAclNamedAdvSrcAddrType = _HpnicfAclIPAclNamedAdvSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 5),
    _HpnicfAclIPAclNamedAdvSrcAddrType_Type()
)
hpnicfAclIPAclNamedAdvSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvSrcAddrType.setStatus("current")
_HpnicfAclIPAclNamedAdvSrcAddr_Type = InetAddress
_HpnicfAclIPAclNamedAdvSrcAddr_Object = MibTableColumn
hpnicfAclIPAclNamedAdvSrcAddr = _HpnicfAclIPAclNamedAdvSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 6),
    _HpnicfAclIPAclNamedAdvSrcAddr_Type()
)
hpnicfAclIPAclNamedAdvSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvSrcAddr.setStatus("current")
_HpnicfAclIPAclNamedAdvSrcPrefix_Type = InetAddressPrefixLength
_HpnicfAclIPAclNamedAdvSrcPrefix_Object = MibTableColumn
hpnicfAclIPAclNamedAdvSrcPrefix = _HpnicfAclIPAclNamedAdvSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 7),
    _HpnicfAclIPAclNamedAdvSrcPrefix_Type()
)
hpnicfAclIPAclNamedAdvSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvSrcPrefix.setStatus("current")


class _HpnicfAclIPAclNamedAdvSrcAny_Type(TruthValue):
    """Custom type hpnicfAclIPAclNamedAdvSrcAny based on TruthValue"""
    defaultValue = 1


_HpnicfAclIPAclNamedAdvSrcAny_Type.__name__ = "TruthValue"
_HpnicfAclIPAclNamedAdvSrcAny_Object = MibTableColumn
hpnicfAclIPAclNamedAdvSrcAny = _HpnicfAclIPAclNamedAdvSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 8),
    _HpnicfAclIPAclNamedAdvSrcAny_Type()
)
hpnicfAclIPAclNamedAdvSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvSrcAny.setStatus("current")
_HpnicfAclIPAclNamedAdvSrcWild_Type = IpAddress
_HpnicfAclIPAclNamedAdvSrcWild_Object = MibTableColumn
hpnicfAclIPAclNamedAdvSrcWild = _HpnicfAclIPAclNamedAdvSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 9),
    _HpnicfAclIPAclNamedAdvSrcWild_Type()
)
hpnicfAclIPAclNamedAdvSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvSrcWild.setStatus("current")


class _HpnicfAclIPAclNamedAdvSrcOp_Type(PortOp):
    """Custom type hpnicfAclIPAclNamedAdvSrcOp based on PortOp"""
    defaultValue = 0


_HpnicfAclIPAclNamedAdvSrcOp_Type.__name__ = "PortOp"
_HpnicfAclIPAclNamedAdvSrcOp_Object = MibTableColumn
hpnicfAclIPAclNamedAdvSrcOp = _HpnicfAclIPAclNamedAdvSrcOp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 10),
    _HpnicfAclIPAclNamedAdvSrcOp_Type()
)
hpnicfAclIPAclNamedAdvSrcOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvSrcOp.setStatus("current")


class _HpnicfAclIPAclNamedAdvSrcPort1_Type(Integer32):
    """Custom type hpnicfAclIPAclNamedAdvSrcPort1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclIPAclNamedAdvSrcPort1_Type.__name__ = "Integer32"
_HpnicfAclIPAclNamedAdvSrcPort1_Object = MibTableColumn
hpnicfAclIPAclNamedAdvSrcPort1 = _HpnicfAclIPAclNamedAdvSrcPort1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 11),
    _HpnicfAclIPAclNamedAdvSrcPort1_Type()
)
hpnicfAclIPAclNamedAdvSrcPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvSrcPort1.setStatus("current")


class _HpnicfAclIPAclNamedAdvSrcPort2_Type(Integer32):
    """Custom type hpnicfAclIPAclNamedAdvSrcPort2 based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclIPAclNamedAdvSrcPort2_Type.__name__ = "Integer32"
_HpnicfAclIPAclNamedAdvSrcPort2_Object = MibTableColumn
hpnicfAclIPAclNamedAdvSrcPort2 = _HpnicfAclIPAclNamedAdvSrcPort2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 12),
    _HpnicfAclIPAclNamedAdvSrcPort2_Type()
)
hpnicfAclIPAclNamedAdvSrcPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvSrcPort2.setStatus("current")
_HpnicfAclIPAclNamedAdvDstAddrType_Type = InetAddressType
_HpnicfAclIPAclNamedAdvDstAddrType_Object = MibTableColumn
hpnicfAclIPAclNamedAdvDstAddrType = _HpnicfAclIPAclNamedAdvDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 13),
    _HpnicfAclIPAclNamedAdvDstAddrType_Type()
)
hpnicfAclIPAclNamedAdvDstAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvDstAddrType.setStatus("current")
_HpnicfAclIPAclNamedAdvDstAddr_Type = InetAddress
_HpnicfAclIPAclNamedAdvDstAddr_Object = MibTableColumn
hpnicfAclIPAclNamedAdvDstAddr = _HpnicfAclIPAclNamedAdvDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 14),
    _HpnicfAclIPAclNamedAdvDstAddr_Type()
)
hpnicfAclIPAclNamedAdvDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvDstAddr.setStatus("current")
_HpnicfAclIPAclNamedAdvDstPrefix_Type = InetAddressPrefixLength
_HpnicfAclIPAclNamedAdvDstPrefix_Object = MibTableColumn
hpnicfAclIPAclNamedAdvDstPrefix = _HpnicfAclIPAclNamedAdvDstPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 15),
    _HpnicfAclIPAclNamedAdvDstPrefix_Type()
)
hpnicfAclIPAclNamedAdvDstPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvDstPrefix.setStatus("current")


class _HpnicfAclIPAclNamedAdvDstAny_Type(TruthValue):
    """Custom type hpnicfAclIPAclNamedAdvDstAny based on TruthValue"""
    defaultValue = 1


_HpnicfAclIPAclNamedAdvDstAny_Type.__name__ = "TruthValue"
_HpnicfAclIPAclNamedAdvDstAny_Object = MibTableColumn
hpnicfAclIPAclNamedAdvDstAny = _HpnicfAclIPAclNamedAdvDstAny_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 16),
    _HpnicfAclIPAclNamedAdvDstAny_Type()
)
hpnicfAclIPAclNamedAdvDstAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvDstAny.setStatus("current")
_HpnicfAclIPAclNamedAdvDstWild_Type = IpAddress
_HpnicfAclIPAclNamedAdvDstWild_Object = MibTableColumn
hpnicfAclIPAclNamedAdvDstWild = _HpnicfAclIPAclNamedAdvDstWild_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 17),
    _HpnicfAclIPAclNamedAdvDstWild_Type()
)
hpnicfAclIPAclNamedAdvDstWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvDstWild.setStatus("current")


class _HpnicfAclIPAclNamedAdvDstOp_Type(PortOp):
    """Custom type hpnicfAclIPAclNamedAdvDstOp based on PortOp"""
    defaultValue = 0


_HpnicfAclIPAclNamedAdvDstOp_Type.__name__ = "PortOp"
_HpnicfAclIPAclNamedAdvDstOp_Object = MibTableColumn
hpnicfAclIPAclNamedAdvDstOp = _HpnicfAclIPAclNamedAdvDstOp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 18),
    _HpnicfAclIPAclNamedAdvDstOp_Type()
)
hpnicfAclIPAclNamedAdvDstOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvDstOp.setStatus("current")


class _HpnicfAclIPAclNamedAdvDstPort1_Type(Integer32):
    """Custom type hpnicfAclIPAclNamedAdvDstPort1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclIPAclNamedAdvDstPort1_Type.__name__ = "Integer32"
_HpnicfAclIPAclNamedAdvDstPort1_Object = MibTableColumn
hpnicfAclIPAclNamedAdvDstPort1 = _HpnicfAclIPAclNamedAdvDstPort1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 19),
    _HpnicfAclIPAclNamedAdvDstPort1_Type()
)
hpnicfAclIPAclNamedAdvDstPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvDstPort1.setStatus("current")


class _HpnicfAclIPAclNamedAdvDstPort2_Type(Integer32):
    """Custom type hpnicfAclIPAclNamedAdvDstPort2 based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclIPAclNamedAdvDstPort2_Type.__name__ = "Integer32"
_HpnicfAclIPAclNamedAdvDstPort2_Object = MibTableColumn
hpnicfAclIPAclNamedAdvDstPort2 = _HpnicfAclIPAclNamedAdvDstPort2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 20),
    _HpnicfAclIPAclNamedAdvDstPort2_Type()
)
hpnicfAclIPAclNamedAdvDstPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvDstPort2.setStatus("current")


class _HpnicfAclIPAclNamedAdvIcmpType_Type(Integer32):
    """Custom type hpnicfAclIPAclNamedAdvIcmpType based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfAclIPAclNamedAdvIcmpType_Type.__name__ = "Integer32"
_HpnicfAclIPAclNamedAdvIcmpType_Object = MibTableColumn
hpnicfAclIPAclNamedAdvIcmpType = _HpnicfAclIPAclNamedAdvIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 21),
    _HpnicfAclIPAclNamedAdvIcmpType_Type()
)
hpnicfAclIPAclNamedAdvIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvIcmpType.setStatus("current")


class _HpnicfAclIPAclNamedAdvIcmpCode_Type(Integer32):
    """Custom type hpnicfAclIPAclNamedAdvIcmpCode based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfAclIPAclNamedAdvIcmpCode_Type.__name__ = "Integer32"
_HpnicfAclIPAclNamedAdvIcmpCode_Object = MibTableColumn
hpnicfAclIPAclNamedAdvIcmpCode = _HpnicfAclIPAclNamedAdvIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 22),
    _HpnicfAclIPAclNamedAdvIcmpCode_Type()
)
hpnicfAclIPAclNamedAdvIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvIcmpCode.setStatus("current")


class _HpnicfAclIPAclNamedAdvPrecedence_Type(Integer32):
    """Custom type hpnicfAclIPAclNamedAdvPrecedence based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfAclIPAclNamedAdvPrecedence_Type.__name__ = "Integer32"
_HpnicfAclIPAclNamedAdvPrecedence_Object = MibTableColumn
hpnicfAclIPAclNamedAdvPrecedence = _HpnicfAclIPAclNamedAdvPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 23),
    _HpnicfAclIPAclNamedAdvPrecedence_Type()
)
hpnicfAclIPAclNamedAdvPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvPrecedence.setStatus("current")


class _HpnicfAclIPAclNamedAdvTos_Type(Integer32):
    """Custom type hpnicfAclIPAclNamedAdvTos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_HpnicfAclIPAclNamedAdvTos_Type.__name__ = "Integer32"
_HpnicfAclIPAclNamedAdvTos_Object = MibTableColumn
hpnicfAclIPAclNamedAdvTos = _HpnicfAclIPAclNamedAdvTos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 24),
    _HpnicfAclIPAclNamedAdvTos_Type()
)
hpnicfAclIPAclNamedAdvTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvTos.setStatus("current")


class _HpnicfAclIPAclNamedAdvDscp_Type(DSCPValue):
    """Custom type hpnicfAclIPAclNamedAdvDscp based on DSCPValue"""
    defaultValue = 255


_HpnicfAclIPAclNamedAdvDscp_Type.__name__ = "DSCPValue"
_HpnicfAclIPAclNamedAdvDscp_Object = MibTableColumn
hpnicfAclIPAclNamedAdvDscp = _HpnicfAclIPAclNamedAdvDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 25),
    _HpnicfAclIPAclNamedAdvDscp_Type()
)
hpnicfAclIPAclNamedAdvDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvDscp.setStatus("current")


class _HpnicfAclIPAclNamedAdvTRangeName_Type(OctetString):
    """Custom type hpnicfAclIPAclNamedAdvTRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclIPAclNamedAdvTRangeName_Type.__name__ = "OctetString"
_HpnicfAclIPAclNamedAdvTRangeName_Object = MibTableColumn
hpnicfAclIPAclNamedAdvTRangeName = _HpnicfAclIPAclNamedAdvTRangeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 26),
    _HpnicfAclIPAclNamedAdvTRangeName_Type()
)
hpnicfAclIPAclNamedAdvTRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvTRangeName.setStatus("current")


class _HpnicfAclIPAclNamedAdvTCPFlag_Type(TCPFlag):
    """Custom type hpnicfAclIPAclNamedAdvTCPFlag based on TCPFlag"""
    defaultValue = 0


_HpnicfAclIPAclNamedAdvTCPFlag_Type.__name__ = "TCPFlag"
_HpnicfAclIPAclNamedAdvTCPFlag_Object = MibTableColumn
hpnicfAclIPAclNamedAdvTCPFlag = _HpnicfAclIPAclNamedAdvTCPFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 27),
    _HpnicfAclIPAclNamedAdvTCPFlag_Type()
)
hpnicfAclIPAclNamedAdvTCPFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvTCPFlag.setStatus("current")


class _HpnicfAclIPAclNamedAdvFragmentFlag_Type(FragmentFlag):
    """Custom type hpnicfAclIPAclNamedAdvFragmentFlag based on FragmentFlag"""
    defaultValue = 0


_HpnicfAclIPAclNamedAdvFragmentFlag_Type.__name__ = "FragmentFlag"
_HpnicfAclIPAclNamedAdvFragmentFlag_Object = MibTableColumn
hpnicfAclIPAclNamedAdvFragmentFlag = _HpnicfAclIPAclNamedAdvFragmentFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 28),
    _HpnicfAclIPAclNamedAdvFragmentFlag_Type()
)
hpnicfAclIPAclNamedAdvFragmentFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvFragmentFlag.setStatus("current")


class _HpnicfAclIPAclNamedAdvLog_Type(TruthValue):
    """Custom type hpnicfAclIPAclNamedAdvLog based on TruthValue"""
    defaultValue = 2


_HpnicfAclIPAclNamedAdvLog_Type.__name__ = "TruthValue"
_HpnicfAclIPAclNamedAdvLog_Object = MibTableColumn
hpnicfAclIPAclNamedAdvLog = _HpnicfAclIPAclNamedAdvLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 29),
    _HpnicfAclIPAclNamedAdvLog_Type()
)
hpnicfAclIPAclNamedAdvLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvLog.setStatus("current")
_HpnicfAclIPAclNamedAdvCount_Type = Unsigned32
_HpnicfAclIPAclNamedAdvCount_Object = MibTableColumn
hpnicfAclIPAclNamedAdvCount = _HpnicfAclIPAclNamedAdvCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 30),
    _HpnicfAclIPAclNamedAdvCount_Type()
)
hpnicfAclIPAclNamedAdvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvCount.setStatus("current")


class _HpnicfAclIPAclNamedAdvCountClear_Type(CounterClear):
    """Custom type hpnicfAclIPAclNamedAdvCountClear based on CounterClear"""
    defaultValue = 2


_HpnicfAclIPAclNamedAdvCountClear_Type.__name__ = "CounterClear"
_HpnicfAclIPAclNamedAdvCountClear_Object = MibTableColumn
hpnicfAclIPAclNamedAdvCountClear = _HpnicfAclIPAclNamedAdvCountClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 31),
    _HpnicfAclIPAclNamedAdvCountClear_Type()
)
hpnicfAclIPAclNamedAdvCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvCountClear.setStatus("current")


class _HpnicfAclIPAclNamedAdvEnable_Type(TruthValue):
    """Custom type hpnicfAclIPAclNamedAdvEnable based on TruthValue"""
    defaultValue = 2


_HpnicfAclIPAclNamedAdvEnable_Type.__name__ = "TruthValue"
_HpnicfAclIPAclNamedAdvEnable_Object = MibTableColumn
hpnicfAclIPAclNamedAdvEnable = _HpnicfAclIPAclNamedAdvEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 32),
    _HpnicfAclIPAclNamedAdvEnable_Type()
)
hpnicfAclIPAclNamedAdvEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvEnable.setStatus("current")


class _HpnicfAclIPAclNamedAdvVpnInstName_Type(OctetString):
    """Custom type hpnicfAclIPAclNamedAdvVpnInstName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclIPAclNamedAdvVpnInstName_Type.__name__ = "OctetString"
_HpnicfAclIPAclNamedAdvVpnInstName_Object = MibTableColumn
hpnicfAclIPAclNamedAdvVpnInstName = _HpnicfAclIPAclNamedAdvVpnInstName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 33),
    _HpnicfAclIPAclNamedAdvVpnInstName_Type()
)
hpnicfAclIPAclNamedAdvVpnInstName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvVpnInstName.setStatus("current")


class _HpnicfAclIPAclNamedAdvComment_Type(OctetString):
    """Custom type hpnicfAclIPAclNamedAdvComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfAclIPAclNamedAdvComment_Type.__name__ = "OctetString"
_HpnicfAclIPAclNamedAdvComment_Object = MibTableColumn
hpnicfAclIPAclNamedAdvComment = _HpnicfAclIPAclNamedAdvComment_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 34),
    _HpnicfAclIPAclNamedAdvComment_Type()
)
hpnicfAclIPAclNamedAdvComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvComment.setStatus("current")
_HpnicfAclIPAclNamedAdvReflective_Type = TruthValue
_HpnicfAclIPAclNamedAdvReflective_Object = MibTableColumn
hpnicfAclIPAclNamedAdvReflective = _HpnicfAclIPAclNamedAdvReflective_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 35),
    _HpnicfAclIPAclNamedAdvReflective_Type()
)
hpnicfAclIPAclNamedAdvReflective.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvReflective.setStatus("current")


class _HpnicfAclIPAclNamedAdvCounting_Type(TruthValue):
    """Custom type hpnicfAclIPAclNamedAdvCounting based on TruthValue"""
    defaultValue = 2


_HpnicfAclIPAclNamedAdvCounting_Type.__name__ = "TruthValue"
_HpnicfAclIPAclNamedAdvCounting_Object = MibTableColumn
hpnicfAclIPAclNamedAdvCounting = _HpnicfAclIPAclNamedAdvCounting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 36),
    _HpnicfAclIPAclNamedAdvCounting_Type()
)
hpnicfAclIPAclNamedAdvCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvCounting.setStatus("current")


class _HpnicfAclIPAclNamedAdvTCPFlagMask_Type(Bits):
    """Custom type hpnicfAclIPAclNamedAdvTCPFlagMask based on Bits"""
    namedValues = NamedValues(
        *(("tcpack", 0),
          ("tcpfin", 1),
          ("tcppsh", 2),
          ("tcprst", 3),
          ("tcpsyn", 4),
          ("tcpurg", 5))
    )

_HpnicfAclIPAclNamedAdvTCPFlagMask_Type.__name__ = "Bits"
_HpnicfAclIPAclNamedAdvTCPFlagMask_Object = MibTableColumn
hpnicfAclIPAclNamedAdvTCPFlagMask = _HpnicfAclIPAclNamedAdvTCPFlagMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 37),
    _HpnicfAclIPAclNamedAdvTCPFlagMask_Type()
)
hpnicfAclIPAclNamedAdvTCPFlagMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvTCPFlagMask.setStatus("current")


class _HpnicfAclIPAclNamedAdvTCPFlagValue_Type(Bits):
    """Custom type hpnicfAclIPAclNamedAdvTCPFlagValue based on Bits"""
    namedValues = NamedValues(
        *(("tcpack", 0),
          ("tcpfin", 1),
          ("tcppsh", 2),
          ("tcprst", 3),
          ("tcpsyn", 4),
          ("tcpurg", 5))
    )

_HpnicfAclIPAclNamedAdvTCPFlagValue_Type.__name__ = "Bits"
_HpnicfAclIPAclNamedAdvTCPFlagValue_Object = MibTableColumn
hpnicfAclIPAclNamedAdvTCPFlagValue = _HpnicfAclIPAclNamedAdvTCPFlagValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 38),
    _HpnicfAclIPAclNamedAdvTCPFlagValue_Type()
)
hpnicfAclIPAclNamedAdvTCPFlagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvTCPFlagValue.setStatus("current")


class _HpnicfAclIPAclNamedAdvRouteTypeAny_Type(TruthValue):
    """Custom type hpnicfAclIPAclNamedAdvRouteTypeAny based on TruthValue"""
    defaultValue = 2


_HpnicfAclIPAclNamedAdvRouteTypeAny_Type.__name__ = "TruthValue"
_HpnicfAclIPAclNamedAdvRouteTypeAny_Object = MibTableColumn
hpnicfAclIPAclNamedAdvRouteTypeAny = _HpnicfAclIPAclNamedAdvRouteTypeAny_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 39),
    _HpnicfAclIPAclNamedAdvRouteTypeAny_Type()
)
hpnicfAclIPAclNamedAdvRouteTypeAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvRouteTypeAny.setStatus("current")


class _HpnicfAclIPAclNamedAdvRouteTypeValue_Type(Integer32):
    """Custom type hpnicfAclIPAclNamedAdvRouteTypeValue based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfAclIPAclNamedAdvRouteTypeValue_Type.__name__ = "Integer32"
_HpnicfAclIPAclNamedAdvRouteTypeValue_Object = MibTableColumn
hpnicfAclIPAclNamedAdvRouteTypeValue = _HpnicfAclIPAclNamedAdvRouteTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 40),
    _HpnicfAclIPAclNamedAdvRouteTypeValue_Type()
)
hpnicfAclIPAclNamedAdvRouteTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvRouteTypeValue.setStatus("current")


class _HpnicfAclIPAclNamedAdvFlowLabel_Type(Unsigned32):
    """Custom type hpnicfAclIPAclNamedAdvFlowLabel based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_HpnicfAclIPAclNamedAdvFlowLabel_Type.__name__ = "Unsigned32"
_HpnicfAclIPAclNamedAdvFlowLabel_Object = MibTableColumn
hpnicfAclIPAclNamedAdvFlowLabel = _HpnicfAclIPAclNamedAdvFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 41),
    _HpnicfAclIPAclNamedAdvFlowLabel_Type()
)
hpnicfAclIPAclNamedAdvFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvFlowLabel.setStatus("current")
_HpnicfAclIPAclNamedAdvSrcSuffix_Type = Unsigned32
_HpnicfAclIPAclNamedAdvSrcSuffix_Object = MibTableColumn
hpnicfAclIPAclNamedAdvSrcSuffix = _HpnicfAclIPAclNamedAdvSrcSuffix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 42),
    _HpnicfAclIPAclNamedAdvSrcSuffix_Type()
)
hpnicfAclIPAclNamedAdvSrcSuffix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvSrcSuffix.setStatus("current")
_HpnicfAclIPAclNamedAdvDstSuffix_Type = Unsigned32
_HpnicfAclIPAclNamedAdvDstSuffix_Object = MibTableColumn
hpnicfAclIPAclNamedAdvDstSuffix = _HpnicfAclIPAclNamedAdvDstSuffix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 2, 5, 1, 43),
    _HpnicfAclIPAclNamedAdvDstSuffix_Type()
)
hpnicfAclIPAclNamedAdvDstSuffix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIPAclNamedAdvDstSuffix.setStatus("current")
_HpnicfAclMACAclGroup_ObjectIdentity = ObjectIdentity
hpnicfAclMACAclGroup = _HpnicfAclMACAclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3)
)
_HpnicfAclMACTable_Object = MibTable
hpnicfAclMACTable = _HpnicfAclMACTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfAclMACTable.setStatus("current")
_HpnicfAclMACEntry_Object = MibTableRow
hpnicfAclMACEntry = _HpnicfAclMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1)
)
hpnicfAclMACEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNumberGroupType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNumberGroupIndex"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclMACRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfAclMACEntry.setStatus("current")


class _HpnicfAclMACRuleIndex_Type(Integer32):
    """Custom type hpnicfAclMACRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HpnicfAclMACRuleIndex_Type.__name__ = "Integer32"
_HpnicfAclMACRuleIndex_Object = MibTableColumn
hpnicfAclMACRuleIndex = _HpnicfAclMACRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 1),
    _HpnicfAclMACRuleIndex_Type()
)
hpnicfAclMACRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclMACRuleIndex.setStatus("current")
_HpnicfAclMACRowStatus_Type = RowStatus
_HpnicfAclMACRowStatus_Object = MibTableColumn
hpnicfAclMACRowStatus = _HpnicfAclMACRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 2),
    _HpnicfAclMACRowStatus_Type()
)
hpnicfAclMACRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclMACRowStatus.setStatus("current")
_HpnicfAclMACAct_Type = RuleAction
_HpnicfAclMACAct_Object = MibTableColumn
hpnicfAclMACAct = _HpnicfAclMACAct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 3),
    _HpnicfAclMACAct_Type()
)
hpnicfAclMACAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclMACAct.setStatus("current")


class _HpnicfAclMACTypeCode_Type(OctetString):
    """Custom type hpnicfAclMACTypeCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclMACTypeCode_Type.__name__ = "OctetString"
_HpnicfAclMACTypeCode_Object = MibTableColumn
hpnicfAclMACTypeCode = _HpnicfAclMACTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 4),
    _HpnicfAclMACTypeCode_Type()
)
hpnicfAclMACTypeCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclMACTypeCode.setStatus("current")


class _HpnicfAclMACTypeMask_Type(OctetString):
    """Custom type hpnicfAclMACTypeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclMACTypeMask_Type.__name__ = "OctetString"
_HpnicfAclMACTypeMask_Object = MibTableColumn
hpnicfAclMACTypeMask = _HpnicfAclMACTypeMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 5),
    _HpnicfAclMACTypeMask_Type()
)
hpnicfAclMACTypeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclMACTypeMask.setStatus("current")
_HpnicfAclMACSrcMac_Type = MacAddress
_HpnicfAclMACSrcMac_Object = MibTableColumn
hpnicfAclMACSrcMac = _HpnicfAclMACSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 6),
    _HpnicfAclMACSrcMac_Type()
)
hpnicfAclMACSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclMACSrcMac.setStatus("current")
_HpnicfAclMACSrcMacWild_Type = MacAddress
_HpnicfAclMACSrcMacWild_Object = MibTableColumn
hpnicfAclMACSrcMacWild = _HpnicfAclMACSrcMacWild_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 7),
    _HpnicfAclMACSrcMacWild_Type()
)
hpnicfAclMACSrcMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclMACSrcMacWild.setStatus("current")
_HpnicfAclMACDestMac_Type = MacAddress
_HpnicfAclMACDestMac_Object = MibTableColumn
hpnicfAclMACDestMac = _HpnicfAclMACDestMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 8),
    _HpnicfAclMACDestMac_Type()
)
hpnicfAclMACDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclMACDestMac.setStatus("current")
_HpnicfAclMACDestMacWild_Type = MacAddress
_HpnicfAclMACDestMacWild_Object = MibTableColumn
hpnicfAclMACDestMacWild = _HpnicfAclMACDestMacWild_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 9),
    _HpnicfAclMACDestMacWild_Type()
)
hpnicfAclMACDestMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclMACDestMacWild.setStatus("current")


class _HpnicfAclMACLsapCode_Type(OctetString):
    """Custom type hpnicfAclMACLsapCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclMACLsapCode_Type.__name__ = "OctetString"
_HpnicfAclMACLsapCode_Object = MibTableColumn
hpnicfAclMACLsapCode = _HpnicfAclMACLsapCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 10),
    _HpnicfAclMACLsapCode_Type()
)
hpnicfAclMACLsapCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclMACLsapCode.setStatus("current")


class _HpnicfAclMACLsapMask_Type(OctetString):
    """Custom type hpnicfAclMACLsapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclMACLsapMask_Type.__name__ = "OctetString"
_HpnicfAclMACLsapMask_Object = MibTableColumn
hpnicfAclMACLsapMask = _HpnicfAclMACLsapMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 11),
    _HpnicfAclMACLsapMask_Type()
)
hpnicfAclMACLsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclMACLsapMask.setStatus("current")


class _HpnicfAclMACCos_Type(Integer32):
    """Custom type hpnicfAclMACCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfAclMACCos_Type.__name__ = "Integer32"
_HpnicfAclMACCos_Object = MibTableColumn
hpnicfAclMACCos = _HpnicfAclMACCos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 12),
    _HpnicfAclMACCos_Type()
)
hpnicfAclMACCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclMACCos.setStatus("current")


class _HpnicfAclMACTimeRangeName_Type(OctetString):
    """Custom type hpnicfAclMACTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclMACTimeRangeName_Type.__name__ = "OctetString"
_HpnicfAclMACTimeRangeName_Object = MibTableColumn
hpnicfAclMACTimeRangeName = _HpnicfAclMACTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 13),
    _HpnicfAclMACTimeRangeName_Type()
)
hpnicfAclMACTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclMACTimeRangeName.setStatus("current")
_HpnicfAclMACCount_Type = Unsigned32
_HpnicfAclMACCount_Object = MibTableColumn
hpnicfAclMACCount = _HpnicfAclMACCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 14),
    _HpnicfAclMACCount_Type()
)
hpnicfAclMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclMACCount.setStatus("current")


class _HpnicfAclMACCountClear_Type(CounterClear):
    """Custom type hpnicfAclMACCountClear based on CounterClear"""
    defaultValue = 2


_HpnicfAclMACCountClear_Type.__name__ = "CounterClear"
_HpnicfAclMACCountClear_Object = MibTableColumn
hpnicfAclMACCountClear = _HpnicfAclMACCountClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 15),
    _HpnicfAclMACCountClear_Type()
)
hpnicfAclMACCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfAclMACCountClear.setStatus("current")


class _HpnicfAclMACEnable_Type(TruthValue):
    """Custom type hpnicfAclMACEnable based on TruthValue"""
    defaultValue = 2


_HpnicfAclMACEnable_Type.__name__ = "TruthValue"
_HpnicfAclMACEnable_Object = MibTableColumn
hpnicfAclMACEnable = _HpnicfAclMACEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 16),
    _HpnicfAclMACEnable_Type()
)
hpnicfAclMACEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclMACEnable.setStatus("current")


class _HpnicfAclMACComment_Type(OctetString):
    """Custom type hpnicfAclMACComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfAclMACComment_Type.__name__ = "OctetString"
_HpnicfAclMACComment_Object = MibTableColumn
hpnicfAclMACComment = _HpnicfAclMACComment_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 17),
    _HpnicfAclMACComment_Type()
)
hpnicfAclMACComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclMACComment.setStatus("current")


class _HpnicfAclMACLog_Type(TruthValue):
    """Custom type hpnicfAclMACLog based on TruthValue"""
    defaultValue = 2


_HpnicfAclMACLog_Type.__name__ = "TruthValue"
_HpnicfAclMACLog_Object = MibTableColumn
hpnicfAclMACLog = _HpnicfAclMACLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 18),
    _HpnicfAclMACLog_Type()
)
hpnicfAclMACLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclMACLog.setStatus("current")


class _HpnicfAclMACCounting_Type(TruthValue):
    """Custom type hpnicfAclMACCounting based on TruthValue"""
    defaultValue = 2


_HpnicfAclMACCounting_Type.__name__ = "TruthValue"
_HpnicfAclMACCounting_Object = MibTableColumn
hpnicfAclMACCounting = _HpnicfAclMACCounting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 1, 1, 19),
    _HpnicfAclMACCounting_Type()
)
hpnicfAclMACCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclMACCounting.setStatus("current")
_HpnicfAclNamedMACTable_Object = MibTable
hpnicfAclNamedMACTable = _HpnicfAclNamedMACTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfAclNamedMACTable.setStatus("current")
_HpnicfAclNamedMACEntry_Object = MibTableRow
hpnicfAclNamedMACEntry = _HpnicfAclNamedMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1)
)
hpnicfAclNamedMACEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNumberGroupType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNamedGroupName"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclMACRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfAclNamedMACEntry.setStatus("current")
_HpnicfAclNamedMACRowStatus_Type = RowStatus
_HpnicfAclNamedMACRowStatus_Object = MibTableColumn
hpnicfAclNamedMACRowStatus = _HpnicfAclNamedMACRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1, 1),
    _HpnicfAclNamedMACRowStatus_Type()
)
hpnicfAclNamedMACRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedMACRowStatus.setStatus("current")
_HpnicfAclNamedMACAct_Type = RuleAction
_HpnicfAclNamedMACAct_Object = MibTableColumn
hpnicfAclNamedMACAct = _HpnicfAclNamedMACAct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1, 2),
    _HpnicfAclNamedMACAct_Type()
)
hpnicfAclNamedMACAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedMACAct.setStatus("current")


class _HpnicfAclNamedMACTypeCode_Type(OctetString):
    """Custom type hpnicfAclNamedMACTypeCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclNamedMACTypeCode_Type.__name__ = "OctetString"
_HpnicfAclNamedMACTypeCode_Object = MibTableColumn
hpnicfAclNamedMACTypeCode = _HpnicfAclNamedMACTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1, 3),
    _HpnicfAclNamedMACTypeCode_Type()
)
hpnicfAclNamedMACTypeCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedMACTypeCode.setStatus("current")


class _HpnicfAclNamedMACTypeMask_Type(OctetString):
    """Custom type hpnicfAclNamedMACTypeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclNamedMACTypeMask_Type.__name__ = "OctetString"
_HpnicfAclNamedMACTypeMask_Object = MibTableColumn
hpnicfAclNamedMACTypeMask = _HpnicfAclNamedMACTypeMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1, 4),
    _HpnicfAclNamedMACTypeMask_Type()
)
hpnicfAclNamedMACTypeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedMACTypeMask.setStatus("current")
_HpnicfAclNamedMACSrcMac_Type = MacAddress
_HpnicfAclNamedMACSrcMac_Object = MibTableColumn
hpnicfAclNamedMACSrcMac = _HpnicfAclNamedMACSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1, 5),
    _HpnicfAclNamedMACSrcMac_Type()
)
hpnicfAclNamedMACSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedMACSrcMac.setStatus("current")
_HpnicfAclNamedMACSrcMacWild_Type = MacAddress
_HpnicfAclNamedMACSrcMacWild_Object = MibTableColumn
hpnicfAclNamedMACSrcMacWild = _HpnicfAclNamedMACSrcMacWild_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1, 6),
    _HpnicfAclNamedMACSrcMacWild_Type()
)
hpnicfAclNamedMACSrcMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedMACSrcMacWild.setStatus("current")
_HpnicfAclNamedMACDstMac_Type = MacAddress
_HpnicfAclNamedMACDstMac_Object = MibTableColumn
hpnicfAclNamedMACDstMac = _HpnicfAclNamedMACDstMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1, 7),
    _HpnicfAclNamedMACDstMac_Type()
)
hpnicfAclNamedMACDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedMACDstMac.setStatus("current")
_HpnicfAclNamedMACDstMacWild_Type = MacAddress
_HpnicfAclNamedMACDstMacWild_Object = MibTableColumn
hpnicfAclNamedMACDstMacWild = _HpnicfAclNamedMACDstMacWild_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1, 8),
    _HpnicfAclNamedMACDstMacWild_Type()
)
hpnicfAclNamedMACDstMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedMACDstMacWild.setStatus("current")


class _HpnicfAclNamedMACLsapCode_Type(OctetString):
    """Custom type hpnicfAclNamedMACLsapCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclNamedMACLsapCode_Type.__name__ = "OctetString"
_HpnicfAclNamedMACLsapCode_Object = MibTableColumn
hpnicfAclNamedMACLsapCode = _HpnicfAclNamedMACLsapCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1, 9),
    _HpnicfAclNamedMACLsapCode_Type()
)
hpnicfAclNamedMACLsapCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedMACLsapCode.setStatus("current")


class _HpnicfAclNamedMACLsapMask_Type(OctetString):
    """Custom type hpnicfAclNamedMACLsapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclNamedMACLsapMask_Type.__name__ = "OctetString"
_HpnicfAclNamedMACLsapMask_Object = MibTableColumn
hpnicfAclNamedMACLsapMask = _HpnicfAclNamedMACLsapMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1, 10),
    _HpnicfAclNamedMACLsapMask_Type()
)
hpnicfAclNamedMACLsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedMACLsapMask.setStatus("current")


class _HpnicfAclNamedMACCos_Type(Integer32):
    """Custom type hpnicfAclNamedMACCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfAclNamedMACCos_Type.__name__ = "Integer32"
_HpnicfAclNamedMACCos_Object = MibTableColumn
hpnicfAclNamedMACCos = _HpnicfAclNamedMACCos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1, 11),
    _HpnicfAclNamedMACCos_Type()
)
hpnicfAclNamedMACCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedMACCos.setStatus("current")


class _HpnicfAclNamedMACTimeRangeName_Type(OctetString):
    """Custom type hpnicfAclNamedMACTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclNamedMACTimeRangeName_Type.__name__ = "OctetString"
_HpnicfAclNamedMACTimeRangeName_Object = MibTableColumn
hpnicfAclNamedMACTimeRangeName = _HpnicfAclNamedMACTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1, 12),
    _HpnicfAclNamedMACTimeRangeName_Type()
)
hpnicfAclNamedMACTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedMACTimeRangeName.setStatus("current")
_HpnicfAclNamedMACCount_Type = Unsigned32
_HpnicfAclNamedMACCount_Object = MibTableColumn
hpnicfAclNamedMACCount = _HpnicfAclNamedMACCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1, 13),
    _HpnicfAclNamedMACCount_Type()
)
hpnicfAclNamedMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclNamedMACCount.setStatus("current")


class _HpnicfAclNamedMACCountClear_Type(CounterClear):
    """Custom type hpnicfAclNamedMACCountClear based on CounterClear"""
    defaultValue = 2


_HpnicfAclNamedMACCountClear_Type.__name__ = "CounterClear"
_HpnicfAclNamedMACCountClear_Object = MibTableColumn
hpnicfAclNamedMACCountClear = _HpnicfAclNamedMACCountClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1, 14),
    _HpnicfAclNamedMACCountClear_Type()
)
hpnicfAclNamedMACCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfAclNamedMACCountClear.setStatus("current")


class _HpnicfAclNamedMACEnable_Type(TruthValue):
    """Custom type hpnicfAclNamedMACEnable based on TruthValue"""
    defaultValue = 2


_HpnicfAclNamedMACEnable_Type.__name__ = "TruthValue"
_HpnicfAclNamedMACEnable_Object = MibTableColumn
hpnicfAclNamedMACEnable = _HpnicfAclNamedMACEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1, 15),
    _HpnicfAclNamedMACEnable_Type()
)
hpnicfAclNamedMACEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclNamedMACEnable.setStatus("current")


class _HpnicfAclNamedMACComment_Type(OctetString):
    """Custom type hpnicfAclNamedMACComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfAclNamedMACComment_Type.__name__ = "OctetString"
_HpnicfAclNamedMACComment_Object = MibTableColumn
hpnicfAclNamedMACComment = _HpnicfAclNamedMACComment_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1, 16),
    _HpnicfAclNamedMACComment_Type()
)
hpnicfAclNamedMACComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedMACComment.setStatus("current")


class _HpnicfAclNamedMACLog_Type(TruthValue):
    """Custom type hpnicfAclNamedMACLog based on TruthValue"""
    defaultValue = 2


_HpnicfAclNamedMACLog_Type.__name__ = "TruthValue"
_HpnicfAclNamedMACLog_Object = MibTableColumn
hpnicfAclNamedMACLog = _HpnicfAclNamedMACLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1, 17),
    _HpnicfAclNamedMACLog_Type()
)
hpnicfAclNamedMACLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedMACLog.setStatus("current")


class _HpnicfAclNamedMACCounting_Type(TruthValue):
    """Custom type hpnicfAclNamedMACCounting based on TruthValue"""
    defaultValue = 2


_HpnicfAclNamedMACCounting_Type.__name__ = "TruthValue"
_HpnicfAclNamedMACCounting_Object = MibTableColumn
hpnicfAclNamedMACCounting = _HpnicfAclNamedMACCounting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 3, 2, 1, 18),
    _HpnicfAclNamedMACCounting_Type()
)
hpnicfAclNamedMACCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedMACCounting.setStatus("current")
_HpnicfAclEnUserAclGroup_ObjectIdentity = ObjectIdentity
hpnicfAclEnUserAclGroup = _HpnicfAclEnUserAclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4)
)
_HpnicfAclEnUserTable_Object = MibTable
hpnicfAclEnUserTable = _HpnicfAclEnUserTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3)
)
if mibBuilder.loadTexts:
    hpnicfAclEnUserTable.setStatus("current")
_HpnicfAclEnUserEntry_Object = MibTableRow
hpnicfAclEnUserEntry = _HpnicfAclEnUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3, 1)
)
hpnicfAclEnUserEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNumberGroupType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNumberGroupIndex"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclEnUserRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfAclEnUserEntry.setStatus("current")


class _HpnicfAclEnUserRuleIndex_Type(Integer32):
    """Custom type hpnicfAclEnUserRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HpnicfAclEnUserRuleIndex_Type.__name__ = "Integer32"
_HpnicfAclEnUserRuleIndex_Object = MibTableColumn
hpnicfAclEnUserRuleIndex = _HpnicfAclEnUserRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3, 1, 1),
    _HpnicfAclEnUserRuleIndex_Type()
)
hpnicfAclEnUserRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclEnUserRuleIndex.setStatus("current")
_HpnicfAclEnUserRowStatus_Type = RowStatus
_HpnicfAclEnUserRowStatus_Object = MibTableColumn
hpnicfAclEnUserRowStatus = _HpnicfAclEnUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3, 1, 2),
    _HpnicfAclEnUserRowStatus_Type()
)
hpnicfAclEnUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclEnUserRowStatus.setStatus("current")
_HpnicfAclEnUserAct_Type = RuleAction
_HpnicfAclEnUserAct_Object = MibTableColumn
hpnicfAclEnUserAct = _HpnicfAclEnUserAct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3, 1, 3),
    _HpnicfAclEnUserAct_Type()
)
hpnicfAclEnUserAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclEnUserAct.setStatus("current")


class _HpnicfAclEnUserStartString_Type(OctetString):
    """Custom type hpnicfAclEnUserStartString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclEnUserStartString_Type.__name__ = "OctetString"
_HpnicfAclEnUserStartString_Object = MibTableColumn
hpnicfAclEnUserStartString = _HpnicfAclEnUserStartString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3, 1, 4),
    _HpnicfAclEnUserStartString_Type()
)
hpnicfAclEnUserStartString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclEnUserStartString.setStatus("current")


class _HpnicfAclEnUserL2String_Type(OctetString):
    """Custom type hpnicfAclEnUserL2String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclEnUserL2String_Type.__name__ = "OctetString"
_HpnicfAclEnUserL2String_Object = MibTableColumn
hpnicfAclEnUserL2String = _HpnicfAclEnUserL2String_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3, 1, 5),
    _HpnicfAclEnUserL2String_Type()
)
hpnicfAclEnUserL2String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclEnUserL2String.setStatus("current")


class _HpnicfAclEnUserMplsString_Type(OctetString):
    """Custom type hpnicfAclEnUserMplsString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclEnUserMplsString_Type.__name__ = "OctetString"
_HpnicfAclEnUserMplsString_Object = MibTableColumn
hpnicfAclEnUserMplsString = _HpnicfAclEnUserMplsString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3, 1, 6),
    _HpnicfAclEnUserMplsString_Type()
)
hpnicfAclEnUserMplsString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclEnUserMplsString.setStatus("current")


class _HpnicfAclEnUserIPv4String_Type(OctetString):
    """Custom type hpnicfAclEnUserIPv4String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclEnUserIPv4String_Type.__name__ = "OctetString"
_HpnicfAclEnUserIPv4String_Object = MibTableColumn
hpnicfAclEnUserIPv4String = _HpnicfAclEnUserIPv4String_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3, 1, 7),
    _HpnicfAclEnUserIPv4String_Type()
)
hpnicfAclEnUserIPv4String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclEnUserIPv4String.setStatus("current")


class _HpnicfAclEnUserIPv6String_Type(OctetString):
    """Custom type hpnicfAclEnUserIPv6String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclEnUserIPv6String_Type.__name__ = "OctetString"
_HpnicfAclEnUserIPv6String_Object = MibTableColumn
hpnicfAclEnUserIPv6String = _HpnicfAclEnUserIPv6String_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3, 1, 8),
    _HpnicfAclEnUserIPv6String_Type()
)
hpnicfAclEnUserIPv6String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclEnUserIPv6String.setStatus("current")


class _HpnicfAclEnUserL4String_Type(OctetString):
    """Custom type hpnicfAclEnUserL4String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclEnUserL4String_Type.__name__ = "OctetString"
_HpnicfAclEnUserL4String_Object = MibTableColumn
hpnicfAclEnUserL4String = _HpnicfAclEnUserL4String_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3, 1, 9),
    _HpnicfAclEnUserL4String_Type()
)
hpnicfAclEnUserL4String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclEnUserL4String.setStatus("current")


class _HpnicfAclEnUserL5String_Type(OctetString):
    """Custom type hpnicfAclEnUserL5String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclEnUserL5String_Type.__name__ = "OctetString"
_HpnicfAclEnUserL5String_Object = MibTableColumn
hpnicfAclEnUserL5String = _HpnicfAclEnUserL5String_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3, 1, 10),
    _HpnicfAclEnUserL5String_Type()
)
hpnicfAclEnUserL5String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclEnUserL5String.setStatus("current")


class _HpnicfAclEnUserTimeRangeName_Type(OctetString):
    """Custom type hpnicfAclEnUserTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclEnUserTimeRangeName_Type.__name__ = "OctetString"
_HpnicfAclEnUserTimeRangeName_Object = MibTableColumn
hpnicfAclEnUserTimeRangeName = _HpnicfAclEnUserTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3, 1, 11),
    _HpnicfAclEnUserTimeRangeName_Type()
)
hpnicfAclEnUserTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclEnUserTimeRangeName.setStatus("current")
_HpnicfAclEnUserCount_Type = Unsigned32
_HpnicfAclEnUserCount_Object = MibTableColumn
hpnicfAclEnUserCount = _HpnicfAclEnUserCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3, 1, 12),
    _HpnicfAclEnUserCount_Type()
)
hpnicfAclEnUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclEnUserCount.setStatus("current")
_HpnicfAclEnUserCountClear_Type = CounterClear
_HpnicfAclEnUserCountClear_Object = MibTableColumn
hpnicfAclEnUserCountClear = _HpnicfAclEnUserCountClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3, 1, 13),
    _HpnicfAclEnUserCountClear_Type()
)
hpnicfAclEnUserCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfAclEnUserCountClear.setStatus("current")


class _HpnicfAclEnUserEnable_Type(TruthValue):
    """Custom type hpnicfAclEnUserEnable based on TruthValue"""
    defaultValue = 2


_HpnicfAclEnUserEnable_Type.__name__ = "TruthValue"
_HpnicfAclEnUserEnable_Object = MibTableColumn
hpnicfAclEnUserEnable = _HpnicfAclEnUserEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3, 1, 14),
    _HpnicfAclEnUserEnable_Type()
)
hpnicfAclEnUserEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclEnUserEnable.setStatus("current")


class _HpnicfAclEnUserComment_Type(OctetString):
    """Custom type hpnicfAclEnUserComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfAclEnUserComment_Type.__name__ = "OctetString"
_HpnicfAclEnUserComment_Object = MibTableColumn
hpnicfAclEnUserComment = _HpnicfAclEnUserComment_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3, 1, 15),
    _HpnicfAclEnUserComment_Type()
)
hpnicfAclEnUserComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclEnUserComment.setStatus("current")


class _HpnicfAclEnUserLog_Type(TruthValue):
    """Custom type hpnicfAclEnUserLog based on TruthValue"""
    defaultValue = 2


_HpnicfAclEnUserLog_Type.__name__ = "TruthValue"
_HpnicfAclEnUserLog_Object = MibTableColumn
hpnicfAclEnUserLog = _HpnicfAclEnUserLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3, 1, 16),
    _HpnicfAclEnUserLog_Type()
)
hpnicfAclEnUserLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclEnUserLog.setStatus("current")


class _HpnicfAclEnUserCounting_Type(TruthValue):
    """Custom type hpnicfAclEnUserCounting based on TruthValue"""
    defaultValue = 2


_HpnicfAclEnUserCounting_Type.__name__ = "TruthValue"
_HpnicfAclEnUserCounting_Object = MibTableColumn
hpnicfAclEnUserCounting = _HpnicfAclEnUserCounting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 3, 1, 17),
    _HpnicfAclEnUserCounting_Type()
)
hpnicfAclEnUserCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclEnUserCounting.setStatus("current")
_HpnicfAclNamedUserTable_Object = MibTable
hpnicfAclNamedUserTable = _HpnicfAclNamedUserTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 4)
)
if mibBuilder.loadTexts:
    hpnicfAclNamedUserTable.setStatus("current")
_HpnicfAclNamedUserEntry_Object = MibTableRow
hpnicfAclNamedUserEntry = _HpnicfAclNamedUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 4, 1)
)
hpnicfAclNamedUserEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNumberGroupType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclNamedGroupName"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclEnUserRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfAclNamedUserEntry.setStatus("current")
_HpnicfAclNamedUserRowStatus_Type = RowStatus
_HpnicfAclNamedUserRowStatus_Object = MibTableColumn
hpnicfAclNamedUserRowStatus = _HpnicfAclNamedUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 4, 1, 1),
    _HpnicfAclNamedUserRowStatus_Type()
)
hpnicfAclNamedUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedUserRowStatus.setStatus("current")
_HpnicfAclNamedUserAct_Type = RuleAction
_HpnicfAclNamedUserAct_Object = MibTableColumn
hpnicfAclNamedUserAct = _HpnicfAclNamedUserAct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 4, 1, 2),
    _HpnicfAclNamedUserAct_Type()
)
hpnicfAclNamedUserAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedUserAct.setStatus("current")


class _HpnicfAclNamedUserStartString_Type(OctetString):
    """Custom type hpnicfAclNamedUserStartString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclNamedUserStartString_Type.__name__ = "OctetString"
_HpnicfAclNamedUserStartString_Object = MibTableColumn
hpnicfAclNamedUserStartString = _HpnicfAclNamedUserStartString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 4, 1, 3),
    _HpnicfAclNamedUserStartString_Type()
)
hpnicfAclNamedUserStartString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedUserStartString.setStatus("current")


class _HpnicfAclNamedUserL2String_Type(OctetString):
    """Custom type hpnicfAclNamedUserL2String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclNamedUserL2String_Type.__name__ = "OctetString"
_HpnicfAclNamedUserL2String_Object = MibTableColumn
hpnicfAclNamedUserL2String = _HpnicfAclNamedUserL2String_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 4, 1, 4),
    _HpnicfAclNamedUserL2String_Type()
)
hpnicfAclNamedUserL2String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedUserL2String.setStatus("current")


class _HpnicfAclNamedUserMplsString_Type(OctetString):
    """Custom type hpnicfAclNamedUserMplsString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclNamedUserMplsString_Type.__name__ = "OctetString"
_HpnicfAclNamedUserMplsString_Object = MibTableColumn
hpnicfAclNamedUserMplsString = _HpnicfAclNamedUserMplsString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 4, 1, 5),
    _HpnicfAclNamedUserMplsString_Type()
)
hpnicfAclNamedUserMplsString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedUserMplsString.setStatus("current")


class _HpnicfAclNamedUserIPv4String_Type(OctetString):
    """Custom type hpnicfAclNamedUserIPv4String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclNamedUserIPv4String_Type.__name__ = "OctetString"
_HpnicfAclNamedUserIPv4String_Object = MibTableColumn
hpnicfAclNamedUserIPv4String = _HpnicfAclNamedUserIPv4String_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 4, 1, 6),
    _HpnicfAclNamedUserIPv4String_Type()
)
hpnicfAclNamedUserIPv4String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedUserIPv4String.setStatus("current")


class _HpnicfAclNamedUserIPv6String_Type(OctetString):
    """Custom type hpnicfAclNamedUserIPv6String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclNamedUserIPv6String_Type.__name__ = "OctetString"
_HpnicfAclNamedUserIPv6String_Object = MibTableColumn
hpnicfAclNamedUserIPv6String = _HpnicfAclNamedUserIPv6String_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 4, 1, 7),
    _HpnicfAclNamedUserIPv6String_Type()
)
hpnicfAclNamedUserIPv6String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedUserIPv6String.setStatus("current")


class _HpnicfAclNamedUserL4String_Type(OctetString):
    """Custom type hpnicfAclNamedUserL4String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclNamedUserL4String_Type.__name__ = "OctetString"
_HpnicfAclNamedUserL4String_Object = MibTableColumn
hpnicfAclNamedUserL4String = _HpnicfAclNamedUserL4String_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 4, 1, 8),
    _HpnicfAclNamedUserL4String_Type()
)
hpnicfAclNamedUserL4String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedUserL4String.setStatus("current")


class _HpnicfAclNamedUserL5String_Type(OctetString):
    """Custom type hpnicfAclNamedUserL5String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclNamedUserL5String_Type.__name__ = "OctetString"
_HpnicfAclNamedUserL5String_Object = MibTableColumn
hpnicfAclNamedUserL5String = _HpnicfAclNamedUserL5String_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 4, 1, 9),
    _HpnicfAclNamedUserL5String_Type()
)
hpnicfAclNamedUserL5String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedUserL5String.setStatus("current")


class _HpnicfAclNamedUserTimeRangeName_Type(OctetString):
    """Custom type hpnicfAclNamedUserTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAclNamedUserTimeRangeName_Type.__name__ = "OctetString"
_HpnicfAclNamedUserTimeRangeName_Object = MibTableColumn
hpnicfAclNamedUserTimeRangeName = _HpnicfAclNamedUserTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 4, 1, 10),
    _HpnicfAclNamedUserTimeRangeName_Type()
)
hpnicfAclNamedUserTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedUserTimeRangeName.setStatus("current")
_HpnicfAclNamedUserCount_Type = Unsigned32
_HpnicfAclNamedUserCount_Object = MibTableColumn
hpnicfAclNamedUserCount = _HpnicfAclNamedUserCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 4, 1, 11),
    _HpnicfAclNamedUserCount_Type()
)
hpnicfAclNamedUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclNamedUserCount.setStatus("current")
_HpnicfAclNamedUserCountClear_Type = CounterClear
_HpnicfAclNamedUserCountClear_Object = MibTableColumn
hpnicfAclNamedUserCountClear = _HpnicfAclNamedUserCountClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 4, 1, 12),
    _HpnicfAclNamedUserCountClear_Type()
)
hpnicfAclNamedUserCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfAclNamedUserCountClear.setStatus("current")


class _HpnicfAclNamedUserEnable_Type(TruthValue):
    """Custom type hpnicfAclNamedUserEnable based on TruthValue"""
    defaultValue = 2


_HpnicfAclNamedUserEnable_Type.__name__ = "TruthValue"
_HpnicfAclNamedUserEnable_Object = MibTableColumn
hpnicfAclNamedUserEnable = _HpnicfAclNamedUserEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 4, 1, 13),
    _HpnicfAclNamedUserEnable_Type()
)
hpnicfAclNamedUserEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclNamedUserEnable.setStatus("current")


class _HpnicfAclNamedUserComment_Type(OctetString):
    """Custom type hpnicfAclNamedUserComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfAclNamedUserComment_Type.__name__ = "OctetString"
_HpnicfAclNamedUserComment_Object = MibTableColumn
hpnicfAclNamedUserComment = _HpnicfAclNamedUserComment_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 4, 1, 14),
    _HpnicfAclNamedUserComment_Type()
)
hpnicfAclNamedUserComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedUserComment.setStatus("current")


class _HpnicfAclNamedUserLog_Type(TruthValue):
    """Custom type hpnicfAclNamedUserLog based on TruthValue"""
    defaultValue = 2


_HpnicfAclNamedUserLog_Type.__name__ = "TruthValue"
_HpnicfAclNamedUserLog_Object = MibTableColumn
hpnicfAclNamedUserLog = _HpnicfAclNamedUserLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 4, 1, 15),
    _HpnicfAclNamedUserLog_Type()
)
hpnicfAclNamedUserLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedUserLog.setStatus("current")


class _HpnicfAclNamedUserCounting_Type(TruthValue):
    """Custom type hpnicfAclNamedUserCounting based on TruthValue"""
    defaultValue = 2


_HpnicfAclNamedUserCounting_Type.__name__ = "TruthValue"
_HpnicfAclNamedUserCounting_Object = MibTableColumn
hpnicfAclNamedUserCounting = _HpnicfAclNamedUserCounting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 4, 4, 1, 16),
    _HpnicfAclNamedUserCounting_Type()
)
hpnicfAclNamedUserCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclNamedUserCounting.setStatus("current")
_HpnicfAclResourceGroup_ObjectIdentity = ObjectIdentity
hpnicfAclResourceGroup = _HpnicfAclResourceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 5)
)
_HpnicfAclResourceUsageTable_Object = MibTable
hpnicfAclResourceUsageTable = _HpnicfAclResourceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 5, 1)
)
if mibBuilder.loadTexts:
    hpnicfAclResourceUsageTable.setStatus("current")
_HpnicfAclResourceUsageEntry_Object = MibTableRow
hpnicfAclResourceUsageEntry = _HpnicfAclResourceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 5, 1, 1)
)
hpnicfAclResourceUsageEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclResourceChassis"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclResourceSlot"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclResourceChip"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclResourceType"),
)
if mibBuilder.loadTexts:
    hpnicfAclResourceUsageEntry.setStatus("current")
_HpnicfAclResourceChassis_Type = Unsigned32
_HpnicfAclResourceChassis_Object = MibTableColumn
hpnicfAclResourceChassis = _HpnicfAclResourceChassis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 5, 1, 1, 1),
    _HpnicfAclResourceChassis_Type()
)
hpnicfAclResourceChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclResourceChassis.setStatus("current")
_HpnicfAclResourceSlot_Type = Unsigned32
_HpnicfAclResourceSlot_Object = MibTableColumn
hpnicfAclResourceSlot = _HpnicfAclResourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 5, 1, 1, 2),
    _HpnicfAclResourceSlot_Type()
)
hpnicfAclResourceSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclResourceSlot.setStatus("current")
_HpnicfAclResourceChip_Type = Unsigned32
_HpnicfAclResourceChip_Object = MibTableColumn
hpnicfAclResourceChip = _HpnicfAclResourceChip_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 5, 1, 1, 3),
    _HpnicfAclResourceChip_Type()
)
hpnicfAclResourceChip.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclResourceChip.setStatus("current")


class _HpnicfAclResourceType_Type(Integer32):
    """Custom type hpnicfAclResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfAclResourceType_Type.__name__ = "Integer32"
_HpnicfAclResourceType_Object = MibTableColumn
hpnicfAclResourceType = _HpnicfAclResourceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 5, 1, 1, 4),
    _HpnicfAclResourceType_Type()
)
hpnicfAclResourceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclResourceType.setStatus("current")


class _HpnicfAclPortRange_Type(OctetString):
    """Custom type hpnicfAclPortRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclPortRange_Type.__name__ = "OctetString"
_HpnicfAclPortRange_Object = MibTableColumn
hpnicfAclPortRange = _HpnicfAclPortRange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 5, 1, 1, 5),
    _HpnicfAclPortRange_Type()
)
hpnicfAclPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclPortRange.setStatus("current")
_HpnicfAclResourceTotal_Type = Unsigned32
_HpnicfAclResourceTotal_Object = MibTableColumn
hpnicfAclResourceTotal = _HpnicfAclResourceTotal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 5, 1, 1, 6),
    _HpnicfAclResourceTotal_Type()
)
hpnicfAclResourceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclResourceTotal.setStatus("current")
_HpnicfAclResourceReserved_Type = Unsigned32
_HpnicfAclResourceReserved_Object = MibTableColumn
hpnicfAclResourceReserved = _HpnicfAclResourceReserved_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 5, 1, 1, 7),
    _HpnicfAclResourceReserved_Type()
)
hpnicfAclResourceReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclResourceReserved.setStatus("current")
_HpnicfAclResourceConfigured_Type = Unsigned32
_HpnicfAclResourceConfigured_Object = MibTableColumn
hpnicfAclResourceConfigured = _HpnicfAclResourceConfigured_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 5, 1, 1, 8),
    _HpnicfAclResourceConfigured_Type()
)
hpnicfAclResourceConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclResourceConfigured.setStatus("current")
_HpnicfAclResourceUsagePercent_Type = Unsigned32
_HpnicfAclResourceUsagePercent_Object = MibTableColumn
hpnicfAclResourceUsagePercent = _HpnicfAclResourceUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 5, 1, 1, 9),
    _HpnicfAclResourceUsagePercent_Type()
)
hpnicfAclResourceUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclResourceUsagePercent.setStatus("current")


class _HpnicfAclResourceTypeDescription_Type(OctetString):
    """Custom type hpnicfAclResourceTypeDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HpnicfAclResourceTypeDescription_Type.__name__ = "OctetString"
_HpnicfAclResourceTypeDescription_Object = MibTableColumn
hpnicfAclResourceTypeDescription = _HpnicfAclResourceTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 5, 1, 1, 10),
    _HpnicfAclResourceTypeDescription_Type()
)
hpnicfAclResourceTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAclResourceTypeDescription.setStatus("current")
_HpnicfAclIntervalGroup_ObjectIdentity = ObjectIdentity
hpnicfAclIntervalGroup = _HpnicfAclIntervalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 6)
)
_HpnicfAclIntervalTable_Object = MibTable
hpnicfAclIntervalTable = _HpnicfAclIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 6, 1)
)
if mibBuilder.loadTexts:
    hpnicfAclIntervalTable.setStatus("current")
_HpnicfAclIntervalEntry_Object = MibTableRow
hpnicfAclIntervalEntry = _HpnicfAclIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 6, 1, 1)
)
hpnicfAclIntervalEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfAclIntervalType"),
)
if mibBuilder.loadTexts:
    hpnicfAclIntervalEntry.setStatus("current")


class _HpnicfAclIntervalType_Type(Integer32):
    """Custom type hpnicfAclIntervalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("logging", 1),
          ("trap", 2))
    )


_HpnicfAclIntervalType_Type.__name__ = "Integer32"
_HpnicfAclIntervalType_Object = MibTableColumn
hpnicfAclIntervalType = _HpnicfAclIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 6, 1, 1, 1),
    _HpnicfAclIntervalType_Type()
)
hpnicfAclIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAclIntervalType.setStatus("current")


class _HpnicfAclIntervalValue_Type(Integer32):
    """Custom type hpnicfAclIntervalValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1440),
    )


_HpnicfAclIntervalValue_Type.__name__ = "Integer32"
_HpnicfAclIntervalValue_Object = MibTableColumn
hpnicfAclIntervalValue = _HpnicfAclIntervalValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 6, 1, 1, 2),
    _HpnicfAclIntervalValue_Type()
)
hpnicfAclIntervalValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIntervalValue.setStatus("current")
_HpnicfAclIntervalRowStatus_Type = RowStatus
_HpnicfAclIntervalRowStatus_Object = MibTableColumn
hpnicfAclIntervalRowStatus = _HpnicfAclIntervalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 2, 6, 1, 1, 3),
    _HpnicfAclIntervalRowStatus_Type()
)
hpnicfAclIntervalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAclIntervalRowStatus.setStatus("current")
_HpnicfAclPacketFilterObjects_ObjectIdentity = ObjectIdentity
hpnicfAclPacketFilterObjects = _HpnicfAclPacketFilterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3)
)
_HpnicfPfilterScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfPfilterScalarGroup = _HpnicfPfilterScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 1)
)


class _HpnicfPfilterDefaultAction_Type(Integer32):
    """Custom type hpnicfPfilterDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_HpnicfPfilterDefaultAction_Type.__name__ = "Integer32"
_HpnicfPfilterDefaultAction_Object = MibScalar
hpnicfPfilterDefaultAction = _HpnicfPfilterDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 1, 1),
    _HpnicfPfilterDefaultAction_Type()
)
hpnicfPfilterDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPfilterDefaultAction.setStatus("current")


class _HpnicfPfilterProcessingStatus_Type(Integer32):
    """Custom type hpnicfPfilterProcessingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("processing", 1),
          ("done", 2))
    )


_HpnicfPfilterProcessingStatus_Type.__name__ = "Integer32"
_HpnicfPfilterProcessingStatus_Object = MibScalar
hpnicfPfilterProcessingStatus = _HpnicfPfilterProcessingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 1, 2),
    _HpnicfPfilterProcessingStatus_Type()
)
hpnicfPfilterProcessingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilterProcessingStatus.setStatus("current")
_HpnicfPfilterApplyTable_Object = MibTable
hpnicfPfilterApplyTable = _HpnicfPfilterApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfPfilterApplyTable.setStatus("current")
_HpnicfPfilterApplyEntry_Object = MibTableRow
hpnicfPfilterApplyEntry = _HpnicfPfilterApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 2, 1)
)
hpnicfPfilterApplyEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterApplyObjType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterApplyObjIndex"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterApplyDirection"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterApplyAclType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterApplyAclIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPfilterApplyEntry.setStatus("current")


class _HpnicfPfilterApplyObjType_Type(Integer32):
    """Custom type hpnicfPfilterApplyObjType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("vlan", 2),
          ("global", 3))
    )


_HpnicfPfilterApplyObjType_Type.__name__ = "Integer32"
_HpnicfPfilterApplyObjType_Object = MibTableColumn
hpnicfPfilterApplyObjType = _HpnicfPfilterApplyObjType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 2, 1, 1),
    _HpnicfPfilterApplyObjType_Type()
)
hpnicfPfilterApplyObjType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilterApplyObjType.setStatus("current")


class _HpnicfPfilterApplyObjIndex_Type(Integer32):
    """Custom type hpnicfPfilterApplyObjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfPfilterApplyObjIndex_Type.__name__ = "Integer32"
_HpnicfPfilterApplyObjIndex_Object = MibTableColumn
hpnicfPfilterApplyObjIndex = _HpnicfPfilterApplyObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 2, 1, 2),
    _HpnicfPfilterApplyObjIndex_Type()
)
hpnicfPfilterApplyObjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilterApplyObjIndex.setStatus("current")
_HpnicfPfilterApplyDirection_Type = DirectionType
_HpnicfPfilterApplyDirection_Object = MibTableColumn
hpnicfPfilterApplyDirection = _HpnicfPfilterApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 2, 1, 3),
    _HpnicfPfilterApplyDirection_Type()
)
hpnicfPfilterApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilterApplyDirection.setStatus("current")


class _HpnicfPfilterApplyAclType_Type(Integer32):
    """Custom type hpnicfPfilterApplyAclType based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("default", 3),
          ("mac", 4),
          ("user", 5))
    )


_HpnicfPfilterApplyAclType_Type.__name__ = "Integer32"
_HpnicfPfilterApplyAclType_Object = MibTableColumn
hpnicfPfilterApplyAclType = _HpnicfPfilterApplyAclType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 2, 1, 4),
    _HpnicfPfilterApplyAclType_Type()
)
hpnicfPfilterApplyAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilterApplyAclType.setStatus("current")


class _HpnicfPfilterApplyAclIndex_Type(Integer32):
    """Custom type hpnicfPfilterApplyAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 5999),
    )


_HpnicfPfilterApplyAclIndex_Type.__name__ = "Integer32"
_HpnicfPfilterApplyAclIndex_Object = MibTableColumn
hpnicfPfilterApplyAclIndex = _HpnicfPfilterApplyAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 2, 1, 5),
    _HpnicfPfilterApplyAclIndex_Type()
)
hpnicfPfilterApplyAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilterApplyAclIndex.setStatus("current")


class _HpnicfPfilterApplyHardCount_Type(TruthValue):
    """Custom type hpnicfPfilterApplyHardCount based on TruthValue"""
    defaultValue = 2


_HpnicfPfilterApplyHardCount_Type.__name__ = "TruthValue"
_HpnicfPfilterApplyHardCount_Object = MibTableColumn
hpnicfPfilterApplyHardCount = _HpnicfPfilterApplyHardCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 2, 1, 6),
    _HpnicfPfilterApplyHardCount_Type()
)
hpnicfPfilterApplyHardCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPfilterApplyHardCount.setStatus("current")
_HpnicfPfilterApplySequence_Type = Unsigned32
_HpnicfPfilterApplySequence_Object = MibTableColumn
hpnicfPfilterApplySequence = _HpnicfPfilterApplySequence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 2, 1, 7),
    _HpnicfPfilterApplySequence_Type()
)
hpnicfPfilterApplySequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilterApplySequence.setStatus("current")
_HpnicfPfilterApplyCountClear_Type = CounterClear
_HpnicfPfilterApplyCountClear_Object = MibTableColumn
hpnicfPfilterApplyCountClear = _HpnicfPfilterApplyCountClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 2, 1, 8),
    _HpnicfPfilterApplyCountClear_Type()
)
hpnicfPfilterApplyCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPfilterApplyCountClear.setStatus("current")
_HpnicfPfilterApplyRowStatus_Type = RowStatus
_HpnicfPfilterApplyRowStatus_Object = MibTableColumn
hpnicfPfilterApplyRowStatus = _HpnicfPfilterApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 2, 1, 9),
    _HpnicfPfilterApplyRowStatus_Type()
)
hpnicfPfilterApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPfilterApplyRowStatus.setStatus("current")
_HpnicfPfilterAclGroupRunInfoTable_Object = MibTable
hpnicfPfilterAclGroupRunInfoTable = _HpnicfPfilterAclGroupRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 3)
)
if mibBuilder.loadTexts:
    hpnicfPfilterAclGroupRunInfoTable.setStatus("current")
_HpnicfPfilterAclGroupRunInfoEntry_Object = MibTableRow
hpnicfPfilterAclGroupRunInfoEntry = _HpnicfPfilterAclGroupRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 3, 1)
)
hpnicfPfilterAclGroupRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterRunApplyObjType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterRunApplyObjIndex"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterRunApplyDirection"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterRunApplyAclType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterRunApplyAclIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPfilterAclGroupRunInfoEntry.setStatus("current")


class _HpnicfPfilterRunApplyObjType_Type(Integer32):
    """Custom type hpnicfPfilterRunApplyObjType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("vlan", 2),
          ("global", 3))
    )


_HpnicfPfilterRunApplyObjType_Type.__name__ = "Integer32"
_HpnicfPfilterRunApplyObjType_Object = MibTableColumn
hpnicfPfilterRunApplyObjType = _HpnicfPfilterRunApplyObjType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 3, 1, 1),
    _HpnicfPfilterRunApplyObjType_Type()
)
hpnicfPfilterRunApplyObjType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilterRunApplyObjType.setStatus("current")


class _HpnicfPfilterRunApplyObjIndex_Type(Integer32):
    """Custom type hpnicfPfilterRunApplyObjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfPfilterRunApplyObjIndex_Type.__name__ = "Integer32"
_HpnicfPfilterRunApplyObjIndex_Object = MibTableColumn
hpnicfPfilterRunApplyObjIndex = _HpnicfPfilterRunApplyObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 3, 1, 2),
    _HpnicfPfilterRunApplyObjIndex_Type()
)
hpnicfPfilterRunApplyObjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilterRunApplyObjIndex.setStatus("current")
_HpnicfPfilterRunApplyDirection_Type = DirectionType
_HpnicfPfilterRunApplyDirection_Object = MibTableColumn
hpnicfPfilterRunApplyDirection = _HpnicfPfilterRunApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 3, 1, 3),
    _HpnicfPfilterRunApplyDirection_Type()
)
hpnicfPfilterRunApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilterRunApplyDirection.setStatus("current")


class _HpnicfPfilterRunApplyAclType_Type(Integer32):
    """Custom type hpnicfPfilterRunApplyAclType based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("default", 3),
          ("mac", 4),
          ("user", 5))
    )


_HpnicfPfilterRunApplyAclType_Type.__name__ = "Integer32"
_HpnicfPfilterRunApplyAclType_Object = MibTableColumn
hpnicfPfilterRunApplyAclType = _HpnicfPfilterRunApplyAclType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 3, 1, 4),
    _HpnicfPfilterRunApplyAclType_Type()
)
hpnicfPfilterRunApplyAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilterRunApplyAclType.setStatus("current")


class _HpnicfPfilterRunApplyAclIndex_Type(Integer32):
    """Custom type hpnicfPfilterRunApplyAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
        ValueRangeConstraint(2000, 5999),
    )


_HpnicfPfilterRunApplyAclIndex_Type.__name__ = "Integer32"
_HpnicfPfilterRunApplyAclIndex_Object = MibTableColumn
hpnicfPfilterRunApplyAclIndex = _HpnicfPfilterRunApplyAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 3, 1, 5),
    _HpnicfPfilterRunApplyAclIndex_Type()
)
hpnicfPfilterRunApplyAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilterRunApplyAclIndex.setStatus("current")


class _HpnicfPfilterAclGroupStatus_Type(Integer32):
    """Custom type hpnicfPfilterAclGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2),
          ("partialSuccess", 3))
    )


_HpnicfPfilterAclGroupStatus_Type.__name__ = "Integer32"
_HpnicfPfilterAclGroupStatus_Object = MibTableColumn
hpnicfPfilterAclGroupStatus = _HpnicfPfilterAclGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 3, 1, 6),
    _HpnicfPfilterAclGroupStatus_Type()
)
hpnicfPfilterAclGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilterAclGroupStatus.setStatus("current")


class _HpnicfPfilterAclGroupCountStatus_Type(Integer32):
    """Custom type hpnicfPfilterAclGroupCountStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2),
          ("partialSuccess", 3))
    )


_HpnicfPfilterAclGroupCountStatus_Type.__name__ = "Integer32"
_HpnicfPfilterAclGroupCountStatus_Object = MibTableColumn
hpnicfPfilterAclGroupCountStatus = _HpnicfPfilterAclGroupCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 3, 1, 7),
    _HpnicfPfilterAclGroupCountStatus_Type()
)
hpnicfPfilterAclGroupCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilterAclGroupCountStatus.setStatus("current")
_HpnicfPfilterAclGroupPermitPkts_Type = Counter64
_HpnicfPfilterAclGroupPermitPkts_Object = MibTableColumn
hpnicfPfilterAclGroupPermitPkts = _HpnicfPfilterAclGroupPermitPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 3, 1, 8),
    _HpnicfPfilterAclGroupPermitPkts_Type()
)
hpnicfPfilterAclGroupPermitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilterAclGroupPermitPkts.setStatus("current")
_HpnicfPfilterAclGroupPermitBytes_Type = Counter64
_HpnicfPfilterAclGroupPermitBytes_Object = MibTableColumn
hpnicfPfilterAclGroupPermitBytes = _HpnicfPfilterAclGroupPermitBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 3, 1, 9),
    _HpnicfPfilterAclGroupPermitBytes_Type()
)
hpnicfPfilterAclGroupPermitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilterAclGroupPermitBytes.setStatus("current")
_HpnicfPfilterAclGroupDenyPkts_Type = Counter64
_HpnicfPfilterAclGroupDenyPkts_Object = MibTableColumn
hpnicfPfilterAclGroupDenyPkts = _HpnicfPfilterAclGroupDenyPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 3, 1, 10),
    _HpnicfPfilterAclGroupDenyPkts_Type()
)
hpnicfPfilterAclGroupDenyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilterAclGroupDenyPkts.setStatus("current")
_HpnicfPfilterAclGroupDenyBytes_Type = Counter64
_HpnicfPfilterAclGroupDenyBytes_Object = MibTableColumn
hpnicfPfilterAclGroupDenyBytes = _HpnicfPfilterAclGroupDenyBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 3, 1, 11),
    _HpnicfPfilterAclGroupDenyBytes_Type()
)
hpnicfPfilterAclGroupDenyBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilterAclGroupDenyBytes.setStatus("current")
_HpnicfPfilterAclRuleRunInfoTable_Object = MibTable
hpnicfPfilterAclRuleRunInfoTable = _HpnicfPfilterAclRuleRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 4)
)
if mibBuilder.loadTexts:
    hpnicfPfilterAclRuleRunInfoTable.setStatus("current")
_HpnicfPfilterAclRuleRunInfoEntry_Object = MibTableRow
hpnicfPfilterAclRuleRunInfoEntry = _HpnicfPfilterAclRuleRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 4, 1)
)
hpnicfPfilterAclRuleRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterRunApplyObjType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterRunApplyObjIndex"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterRunApplyDirection"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterRunApplyAclType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterRunApplyAclIndex"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterAclRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPfilterAclRuleRunInfoEntry.setStatus("current")


class _HpnicfPfilterAclRuleIndex_Type(Integer32):
    """Custom type hpnicfPfilterAclRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HpnicfPfilterAclRuleIndex_Type.__name__ = "Integer32"
_HpnicfPfilterAclRuleIndex_Object = MibTableColumn
hpnicfPfilterAclRuleIndex = _HpnicfPfilterAclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 4, 1, 1),
    _HpnicfPfilterAclRuleIndex_Type()
)
hpnicfPfilterAclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilterAclRuleIndex.setStatus("current")


class _HpnicfPfilterAclRuleStatus_Type(Integer32):
    """Custom type hpnicfPfilterAclRuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2),
          ("partialSuccess", 3))
    )


_HpnicfPfilterAclRuleStatus_Type.__name__ = "Integer32"
_HpnicfPfilterAclRuleStatus_Object = MibTableColumn
hpnicfPfilterAclRuleStatus = _HpnicfPfilterAclRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 4, 1, 2),
    _HpnicfPfilterAclRuleStatus_Type()
)
hpnicfPfilterAclRuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilterAclRuleStatus.setStatus("current")


class _HpnicfPfilterAclRuleCountStatus_Type(Integer32):
    """Custom type hpnicfPfilterAclRuleCountStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2),
          ("partialSuccess", 3))
    )


_HpnicfPfilterAclRuleCountStatus_Type.__name__ = "Integer32"
_HpnicfPfilterAclRuleCountStatus_Object = MibTableColumn
hpnicfPfilterAclRuleCountStatus = _HpnicfPfilterAclRuleCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 4, 1, 3),
    _HpnicfPfilterAclRuleCountStatus_Type()
)
hpnicfPfilterAclRuleCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilterAclRuleCountStatus.setStatus("current")
_HpnicfPfilterAclRuleMatchPackets_Type = Counter64
_HpnicfPfilterAclRuleMatchPackets_Object = MibTableColumn
hpnicfPfilterAclRuleMatchPackets = _HpnicfPfilterAclRuleMatchPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 4, 1, 4),
    _HpnicfPfilterAclRuleMatchPackets_Type()
)
hpnicfPfilterAclRuleMatchPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilterAclRuleMatchPackets.setStatus("current")
_HpnicfPfilterAclRuleMatchBytes_Type = Counter64
_HpnicfPfilterAclRuleMatchBytes_Object = MibTableColumn
hpnicfPfilterAclRuleMatchBytes = _HpnicfPfilterAclRuleMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 4, 1, 5),
    _HpnicfPfilterAclRuleMatchBytes_Type()
)
hpnicfPfilterAclRuleMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilterAclRuleMatchBytes.setStatus("current")
_HpnicfPfilterStatisticSumTable_Object = MibTable
hpnicfPfilterStatisticSumTable = _HpnicfPfilterStatisticSumTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 5)
)
if mibBuilder.loadTexts:
    hpnicfPfilterStatisticSumTable.setStatus("current")
_HpnicfPfilterStatisticSumEntry_Object = MibTableRow
hpnicfPfilterStatisticSumEntry = _HpnicfPfilterStatisticSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 5, 1)
)
hpnicfPfilterStatisticSumEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterSumDirection"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterSumAclType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterSumAclIndex"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilterSumRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPfilterStatisticSumEntry.setStatus("current")
_HpnicfPfilterSumDirection_Type = DirectionType
_HpnicfPfilterSumDirection_Object = MibTableColumn
hpnicfPfilterSumDirection = _HpnicfPfilterSumDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 5, 1, 1),
    _HpnicfPfilterSumDirection_Type()
)
hpnicfPfilterSumDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilterSumDirection.setStatus("current")


class _HpnicfPfilterSumAclType_Type(Integer32):
    """Custom type hpnicfPfilterSumAclType based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("mac", 3),
          ("user", 4))
    )


_HpnicfPfilterSumAclType_Type.__name__ = "Integer32"
_HpnicfPfilterSumAclType_Object = MibTableColumn
hpnicfPfilterSumAclType = _HpnicfPfilterSumAclType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 5, 1, 2),
    _HpnicfPfilterSumAclType_Type()
)
hpnicfPfilterSumAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilterSumAclType.setStatus("current")


class _HpnicfPfilterSumAclIndex_Type(Integer32):
    """Custom type hpnicfPfilterSumAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 5999),
    )


_HpnicfPfilterSumAclIndex_Type.__name__ = "Integer32"
_HpnicfPfilterSumAclIndex_Object = MibTableColumn
hpnicfPfilterSumAclIndex = _HpnicfPfilterSumAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 5, 1, 3),
    _HpnicfPfilterSumAclIndex_Type()
)
hpnicfPfilterSumAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilterSumAclIndex.setStatus("current")


class _HpnicfPfilterSumRuleIndex_Type(Integer32):
    """Custom type hpnicfPfilterSumRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HpnicfPfilterSumRuleIndex_Type.__name__ = "Integer32"
_HpnicfPfilterSumRuleIndex_Object = MibTableColumn
hpnicfPfilterSumRuleIndex = _HpnicfPfilterSumRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 5, 1, 4),
    _HpnicfPfilterSumRuleIndex_Type()
)
hpnicfPfilterSumRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilterSumRuleIndex.setStatus("current")
_HpnicfPfilterSumRuleMatchPackets_Type = Counter64
_HpnicfPfilterSumRuleMatchPackets_Object = MibTableColumn
hpnicfPfilterSumRuleMatchPackets = _HpnicfPfilterSumRuleMatchPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 5, 1, 5),
    _HpnicfPfilterSumRuleMatchPackets_Type()
)
hpnicfPfilterSumRuleMatchPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilterSumRuleMatchPackets.setStatus("current")
_HpnicfPfilterSumRuleMatchBytes_Type = Counter64
_HpnicfPfilterSumRuleMatchBytes_Object = MibTableColumn
hpnicfPfilterSumRuleMatchBytes = _HpnicfPfilterSumRuleMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 5, 1, 6),
    _HpnicfPfilterSumRuleMatchBytes_Type()
)
hpnicfPfilterSumRuleMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilterSumRuleMatchBytes.setStatus("current")
_HpnicfPfilter2ApplyTable_Object = MibTable
hpnicfPfilter2ApplyTable = _HpnicfPfilter2ApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 6)
)
if mibBuilder.loadTexts:
    hpnicfPfilter2ApplyTable.setStatus("current")
_HpnicfPfilter2ApplyEntry_Object = MibTableRow
hpnicfPfilter2ApplyEntry = _HpnicfPfilter2ApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 6, 1)
)
hpnicfPfilter2ApplyEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2ApplyObjType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2ApplyObjIndex"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2ApplyDirection"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2ApplyAclType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2ApplyAclIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPfilter2ApplyEntry.setStatus("current")


class _HpnicfPfilter2ApplyObjType_Type(Integer32):
    """Custom type hpnicfPfilter2ApplyObjType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("vlan", 2),
          ("global", 3))
    )


_HpnicfPfilter2ApplyObjType_Type.__name__ = "Integer32"
_HpnicfPfilter2ApplyObjType_Object = MibTableColumn
hpnicfPfilter2ApplyObjType = _HpnicfPfilter2ApplyObjType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 6, 1, 1),
    _HpnicfPfilter2ApplyObjType_Type()
)
hpnicfPfilter2ApplyObjType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPfilter2ApplyObjType.setStatus("current")


class _HpnicfPfilter2ApplyObjIndex_Type(Integer32):
    """Custom type hpnicfPfilter2ApplyObjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfPfilter2ApplyObjIndex_Type.__name__ = "Integer32"
_HpnicfPfilter2ApplyObjIndex_Object = MibTableColumn
hpnicfPfilter2ApplyObjIndex = _HpnicfPfilter2ApplyObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 6, 1, 2),
    _HpnicfPfilter2ApplyObjIndex_Type()
)
hpnicfPfilter2ApplyObjIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPfilter2ApplyObjIndex.setStatus("current")
_HpnicfPfilter2ApplyDirection_Type = DirectionType
_HpnicfPfilter2ApplyDirection_Object = MibTableColumn
hpnicfPfilter2ApplyDirection = _HpnicfPfilter2ApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 6, 1, 3),
    _HpnicfPfilter2ApplyDirection_Type()
)
hpnicfPfilter2ApplyDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPfilter2ApplyDirection.setStatus("current")


class _HpnicfPfilter2ApplyAclType_Type(Integer32):
    """Custom type hpnicfPfilter2ApplyAclType based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("default", 3),
          ("mac", 4),
          ("user", 5))
    )


_HpnicfPfilter2ApplyAclType_Type.__name__ = "Integer32"
_HpnicfPfilter2ApplyAclType_Object = MibTableColumn
hpnicfPfilter2ApplyAclType = _HpnicfPfilter2ApplyAclType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 6, 1, 4),
    _HpnicfPfilter2ApplyAclType_Type()
)
hpnicfPfilter2ApplyAclType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPfilter2ApplyAclType.setStatus("current")


class _HpnicfPfilter2ApplyAclIndex_Type(OctetString):
    """Custom type hpnicfPfilter2ApplyAclIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HpnicfPfilter2ApplyAclIndex_Type.__name__ = "OctetString"
_HpnicfPfilter2ApplyAclIndex_Object = MibTableColumn
hpnicfPfilter2ApplyAclIndex = _HpnicfPfilter2ApplyAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 6, 1, 5),
    _HpnicfPfilter2ApplyAclIndex_Type()
)
hpnicfPfilter2ApplyAclIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPfilter2ApplyAclIndex.setStatus("current")


class _HpnicfPfilter2ApplyHardCount_Type(TruthValue):
    """Custom type hpnicfPfilter2ApplyHardCount based on TruthValue"""
    defaultValue = 2


_HpnicfPfilter2ApplyHardCount_Type.__name__ = "TruthValue"
_HpnicfPfilter2ApplyHardCount_Object = MibTableColumn
hpnicfPfilter2ApplyHardCount = _HpnicfPfilter2ApplyHardCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 6, 1, 6),
    _HpnicfPfilter2ApplyHardCount_Type()
)
hpnicfPfilter2ApplyHardCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPfilter2ApplyHardCount.setStatus("current")
_HpnicfPfilter2ApplySequence_Type = Unsigned32
_HpnicfPfilter2ApplySequence_Object = MibTableColumn
hpnicfPfilter2ApplySequence = _HpnicfPfilter2ApplySequence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 6, 1, 7),
    _HpnicfPfilter2ApplySequence_Type()
)
hpnicfPfilter2ApplySequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilter2ApplySequence.setStatus("current")


class _HpnicfPfilter2ApplyCountClear_Type(CounterClear):
    """Custom type hpnicfPfilter2ApplyCountClear based on CounterClear"""
    defaultValue = 2


_HpnicfPfilter2ApplyCountClear_Type.__name__ = "CounterClear"
_HpnicfPfilter2ApplyCountClear_Object = MibTableColumn
hpnicfPfilter2ApplyCountClear = _HpnicfPfilter2ApplyCountClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 6, 1, 8),
    _HpnicfPfilter2ApplyCountClear_Type()
)
hpnicfPfilter2ApplyCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPfilter2ApplyCountClear.setStatus("current")
_HpnicfPfilter2ApplyRowStatus_Type = RowStatus
_HpnicfPfilter2ApplyRowStatus_Object = MibTableColumn
hpnicfPfilter2ApplyRowStatus = _HpnicfPfilter2ApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 6, 1, 9),
    _HpnicfPfilter2ApplyRowStatus_Type()
)
hpnicfPfilter2ApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPfilter2ApplyRowStatus.setStatus("current")
_HpnicfPfilter2AclGroupRunInfoTable_Object = MibTable
hpnicfPfilter2AclGroupRunInfoTable = _HpnicfPfilter2AclGroupRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 7)
)
if mibBuilder.loadTexts:
    hpnicfPfilter2AclGroupRunInfoTable.setStatus("current")
_HpnicfPfilter2AclGroupRunInfoEntry_Object = MibTableRow
hpnicfPfilter2AclGroupRunInfoEntry = _HpnicfPfilter2AclGroupRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 7, 1)
)
hpnicfPfilter2AclGroupRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2RunApplyObjType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2RunApplyObjIndex"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2RunApplyDirection"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2RunApplyAclType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2RunApplyAclIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPfilter2AclGroupRunInfoEntry.setStatus("current")


class _HpnicfPfilter2RunApplyObjType_Type(Integer32):
    """Custom type hpnicfPfilter2RunApplyObjType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("vlan", 2),
          ("global", 3))
    )


_HpnicfPfilter2RunApplyObjType_Type.__name__ = "Integer32"
_HpnicfPfilter2RunApplyObjType_Object = MibTableColumn
hpnicfPfilter2RunApplyObjType = _HpnicfPfilter2RunApplyObjType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 7, 1, 1),
    _HpnicfPfilter2RunApplyObjType_Type()
)
hpnicfPfilter2RunApplyObjType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilter2RunApplyObjType.setStatus("current")


class _HpnicfPfilter2RunApplyObjIndex_Type(Integer32):
    """Custom type hpnicfPfilter2RunApplyObjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfPfilter2RunApplyObjIndex_Type.__name__ = "Integer32"
_HpnicfPfilter2RunApplyObjIndex_Object = MibTableColumn
hpnicfPfilter2RunApplyObjIndex = _HpnicfPfilter2RunApplyObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 7, 1, 2),
    _HpnicfPfilter2RunApplyObjIndex_Type()
)
hpnicfPfilter2RunApplyObjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilter2RunApplyObjIndex.setStatus("current")
_HpnicfPfilter2RunApplyDirection_Type = DirectionType
_HpnicfPfilter2RunApplyDirection_Object = MibTableColumn
hpnicfPfilter2RunApplyDirection = _HpnicfPfilter2RunApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 7, 1, 3),
    _HpnicfPfilter2RunApplyDirection_Type()
)
hpnicfPfilter2RunApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilter2RunApplyDirection.setStatus("current")


class _HpnicfPfilter2RunApplyAclType_Type(Integer32):
    """Custom type hpnicfPfilter2RunApplyAclType based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("default", 3),
          ("mac", 4),
          ("user", 5))
    )


_HpnicfPfilter2RunApplyAclType_Type.__name__ = "Integer32"
_HpnicfPfilter2RunApplyAclType_Object = MibTableColumn
hpnicfPfilter2RunApplyAclType = _HpnicfPfilter2RunApplyAclType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 7, 1, 4),
    _HpnicfPfilter2RunApplyAclType_Type()
)
hpnicfPfilter2RunApplyAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilter2RunApplyAclType.setStatus("current")


class _HpnicfPfilter2RunApplyAclIndex_Type(OctetString):
    """Custom type hpnicfPfilter2RunApplyAclIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HpnicfPfilter2RunApplyAclIndex_Type.__name__ = "OctetString"
_HpnicfPfilter2RunApplyAclIndex_Object = MibTableColumn
hpnicfPfilter2RunApplyAclIndex = _HpnicfPfilter2RunApplyAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 7, 1, 5),
    _HpnicfPfilter2RunApplyAclIndex_Type()
)
hpnicfPfilter2RunApplyAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilter2RunApplyAclIndex.setStatus("current")


class _HpnicfPfilter2AclGroupStatus_Type(Integer32):
    """Custom type hpnicfPfilter2AclGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2),
          ("partialSuccess", 3))
    )


_HpnicfPfilter2AclGroupStatus_Type.__name__ = "Integer32"
_HpnicfPfilter2AclGroupStatus_Object = MibTableColumn
hpnicfPfilter2AclGroupStatus = _HpnicfPfilter2AclGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 7, 1, 6),
    _HpnicfPfilter2AclGroupStatus_Type()
)
hpnicfPfilter2AclGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilter2AclGroupStatus.setStatus("current")


class _HpnicfPfilter2AclGroupCountStatus_Type(Integer32):
    """Custom type hpnicfPfilter2AclGroupCountStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2),
          ("partialSuccess", 3))
    )


_HpnicfPfilter2AclGroupCountStatus_Type.__name__ = "Integer32"
_HpnicfPfilter2AclGroupCountStatus_Object = MibTableColumn
hpnicfPfilter2AclGroupCountStatus = _HpnicfPfilter2AclGroupCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 7, 1, 7),
    _HpnicfPfilter2AclGroupCountStatus_Type()
)
hpnicfPfilter2AclGroupCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilter2AclGroupCountStatus.setStatus("current")
_HpnicfPfilter2AclGroupPermitPkts_Type = Counter64
_HpnicfPfilter2AclGroupPermitPkts_Object = MibTableColumn
hpnicfPfilter2AclGroupPermitPkts = _HpnicfPfilter2AclGroupPermitPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 7, 1, 8),
    _HpnicfPfilter2AclGroupPermitPkts_Type()
)
hpnicfPfilter2AclGroupPermitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilter2AclGroupPermitPkts.setStatus("current")
_HpnicfPfilter2AclGroupPermitBytes_Type = Counter64
_HpnicfPfilter2AclGroupPermitBytes_Object = MibTableColumn
hpnicfPfilter2AclGroupPermitBytes = _HpnicfPfilter2AclGroupPermitBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 7, 1, 9),
    _HpnicfPfilter2AclGroupPermitBytes_Type()
)
hpnicfPfilter2AclGroupPermitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilter2AclGroupPermitBytes.setStatus("current")
_HpnicfPfilter2AclGroupDenyPkts_Type = Counter64
_HpnicfPfilter2AclGroupDenyPkts_Object = MibTableColumn
hpnicfPfilter2AclGroupDenyPkts = _HpnicfPfilter2AclGroupDenyPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 7, 1, 10),
    _HpnicfPfilter2AclGroupDenyPkts_Type()
)
hpnicfPfilter2AclGroupDenyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilter2AclGroupDenyPkts.setStatus("current")
_HpnicfPfilter2AclGroupDenyBytes_Type = Counter64
_HpnicfPfilter2AclGroupDenyBytes_Object = MibTableColumn
hpnicfPfilter2AclGroupDenyBytes = _HpnicfPfilter2AclGroupDenyBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 7, 1, 11),
    _HpnicfPfilter2AclGroupDenyBytes_Type()
)
hpnicfPfilter2AclGroupDenyBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilter2AclGroupDenyBytes.setStatus("current")
_HpnicfPfilter2AclRuleRunInfoTable_Object = MibTable
hpnicfPfilter2AclRuleRunInfoTable = _HpnicfPfilter2AclRuleRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 8)
)
if mibBuilder.loadTexts:
    hpnicfPfilter2AclRuleRunInfoTable.setStatus("current")
_HpnicfPfilter2AclRuleRunInfoEntry_Object = MibTableRow
hpnicfPfilter2AclRuleRunInfoEntry = _HpnicfPfilter2AclRuleRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 8, 1)
)
hpnicfPfilter2AclRuleRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2RunApplyObjType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2RunApplyObjIndex"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2RunApplyDirection"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2RunApplyAclType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2RunApplyAclIndex"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2AclRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPfilter2AclRuleRunInfoEntry.setStatus("current")


class _HpnicfPfilter2AclRuleIndex_Type(Integer32):
    """Custom type hpnicfPfilter2AclRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HpnicfPfilter2AclRuleIndex_Type.__name__ = "Integer32"
_HpnicfPfilter2AclRuleIndex_Object = MibTableColumn
hpnicfPfilter2AclRuleIndex = _HpnicfPfilter2AclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 8, 1, 1),
    _HpnicfPfilter2AclRuleIndex_Type()
)
hpnicfPfilter2AclRuleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPfilter2AclRuleIndex.setStatus("current")


class _HpnicfPfilter2AclRuleStatus_Type(Integer32):
    """Custom type hpnicfPfilter2AclRuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2),
          ("partialSuccess", 3))
    )


_HpnicfPfilter2AclRuleStatus_Type.__name__ = "Integer32"
_HpnicfPfilter2AclRuleStatus_Object = MibTableColumn
hpnicfPfilter2AclRuleStatus = _HpnicfPfilter2AclRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 8, 1, 2),
    _HpnicfPfilter2AclRuleStatus_Type()
)
hpnicfPfilter2AclRuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilter2AclRuleStatus.setStatus("current")


class _HpnicfPfilter2AclRuleCountStatus_Type(Integer32):
    """Custom type hpnicfPfilter2AclRuleCountStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2),
          ("partialSuccess", 3))
    )


_HpnicfPfilter2AclRuleCountStatus_Type.__name__ = "Integer32"
_HpnicfPfilter2AclRuleCountStatus_Object = MibTableColumn
hpnicfPfilter2AclRuleCountStatus = _HpnicfPfilter2AclRuleCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 8, 1, 3),
    _HpnicfPfilter2AclRuleCountStatus_Type()
)
hpnicfPfilter2AclRuleCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilter2AclRuleCountStatus.setStatus("current")
_HpnicfPfilter2AclRuleMatchPackets_Type = Counter64
_HpnicfPfilter2AclRuleMatchPackets_Object = MibTableColumn
hpnicfPfilter2AclRuleMatchPackets = _HpnicfPfilter2AclRuleMatchPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 8, 1, 4),
    _HpnicfPfilter2AclRuleMatchPackets_Type()
)
hpnicfPfilter2AclRuleMatchPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilter2AclRuleMatchPackets.setStatus("current")
_HpnicfPfilter2AclRuleMatchBytes_Type = Counter64
_HpnicfPfilter2AclRuleMatchBytes_Object = MibTableColumn
hpnicfPfilter2AclRuleMatchBytes = _HpnicfPfilter2AclRuleMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 8, 1, 5),
    _HpnicfPfilter2AclRuleMatchBytes_Type()
)
hpnicfPfilter2AclRuleMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilter2AclRuleMatchBytes.setStatus("current")
_HpnicfPfilter2StatisticSumTable_Object = MibTable
hpnicfPfilter2StatisticSumTable = _HpnicfPfilter2StatisticSumTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 9)
)
if mibBuilder.loadTexts:
    hpnicfPfilter2StatisticSumTable.setStatus("current")
_HpnicfPfilter2StatisticSumEntry_Object = MibTableRow
hpnicfPfilter2StatisticSumEntry = _HpnicfPfilter2StatisticSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 9, 1)
)
hpnicfPfilter2StatisticSumEntry.setIndexNames(
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2SumDirection"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2SumAclType"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2SumAclIndex"),
    (0, "HPN-ICF-ACL-MIB", "hpnicfPfilter2SumRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPfilter2StatisticSumEntry.setStatus("current")
_HpnicfPfilter2SumDirection_Type = DirectionType
_HpnicfPfilter2SumDirection_Object = MibTableColumn
hpnicfPfilter2SumDirection = _HpnicfPfilter2SumDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 9, 1, 1),
    _HpnicfPfilter2SumDirection_Type()
)
hpnicfPfilter2SumDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilter2SumDirection.setStatus("current")


class _HpnicfPfilter2SumAclType_Type(Integer32):
    """Custom type hpnicfPfilter2SumAclType based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("mac", 3),
          ("user", 4))
    )


_HpnicfPfilter2SumAclType_Type.__name__ = "Integer32"
_HpnicfPfilter2SumAclType_Object = MibTableColumn
hpnicfPfilter2SumAclType = _HpnicfPfilter2SumAclType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 9, 1, 2),
    _HpnicfPfilter2SumAclType_Type()
)
hpnicfPfilter2SumAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilter2SumAclType.setStatus("current")


class _HpnicfPfilter2SumAclIndex_Type(OctetString):
    """Custom type hpnicfPfilter2SumAclIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HpnicfPfilter2SumAclIndex_Type.__name__ = "OctetString"
_HpnicfPfilter2SumAclIndex_Object = MibTableColumn
hpnicfPfilter2SumAclIndex = _HpnicfPfilter2SumAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 9, 1, 3),
    _HpnicfPfilter2SumAclIndex_Type()
)
hpnicfPfilter2SumAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilter2SumAclIndex.setStatus("current")


class _HpnicfPfilter2SumRuleIndex_Type(Integer32):
    """Custom type hpnicfPfilter2SumRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HpnicfPfilter2SumRuleIndex_Type.__name__ = "Integer32"
_HpnicfPfilter2SumRuleIndex_Object = MibTableColumn
hpnicfPfilter2SumRuleIndex = _HpnicfPfilter2SumRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 9, 1, 4),
    _HpnicfPfilter2SumRuleIndex_Type()
)
hpnicfPfilter2SumRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPfilter2SumRuleIndex.setStatus("current")
_HpnicfPfilter2SumRuleMatchPackets_Type = Counter64
_HpnicfPfilter2SumRuleMatchPackets_Object = MibTableColumn
hpnicfPfilter2SumRuleMatchPackets = _HpnicfPfilter2SumRuleMatchPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 9, 1, 5),
    _HpnicfPfilter2SumRuleMatchPackets_Type()
)
hpnicfPfilter2SumRuleMatchPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilter2SumRuleMatchPackets.setStatus("current")
_HpnicfPfilter2SumRuleMatchBytes_Type = Counter64
_HpnicfPfilter2SumRuleMatchBytes_Object = MibTableColumn
hpnicfPfilter2SumRuleMatchBytes = _HpnicfPfilter2SumRuleMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 3, 9, 1, 6),
    _HpnicfPfilter2SumRuleMatchBytes_Type()
)
hpnicfPfilter2SumRuleMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPfilter2SumRuleMatchBytes.setStatus("current")
_HpnicfAclPacketfilterTrapObjects_ObjectIdentity = ObjectIdentity
hpnicfAclPacketfilterTrapObjects = _HpnicfAclPacketfilterTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4)
)
_HpnicfPfilterInterface_Type = OctetString
_HpnicfPfilterInterface_Object = MibScalar
hpnicfPfilterInterface = _HpnicfPfilterInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 1),
    _HpnicfPfilterInterface_Type()
)
hpnicfPfilterInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPfilterInterface.setStatus("current")


class _HpnicfPfilterDirection_Type(OctetString):
    """Custom type hpnicfPfilterDirection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfPfilterDirection_Type.__name__ = "OctetString"
_HpnicfPfilterDirection_Object = MibScalar
hpnicfPfilterDirection = _HpnicfPfilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 2),
    _HpnicfPfilterDirection_Type()
)
hpnicfPfilterDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPfilterDirection.setStatus("current")
_HpnicfPfilterACLNumber_Type = Integer32
_HpnicfPfilterACLNumber_Object = MibScalar
hpnicfPfilterACLNumber = _HpnicfPfilterACLNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 3),
    _HpnicfPfilterACLNumber_Type()
)
hpnicfPfilterACLNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPfilterACLNumber.setStatus("current")


class _HpnicfPfilterAction_Type(OctetString):
    """Custom type hpnicfPfilterAction based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfPfilterAction_Type.__name__ = "OctetString"
_HpnicfPfilterAction_Object = MibScalar
hpnicfPfilterAction = _HpnicfPfilterAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 4),
    _HpnicfPfilterAction_Type()
)
hpnicfPfilterAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPfilterAction.setStatus("current")


class _HpnicfMACfilterSourceMac_Type(OctetString):
    """Custom type hpnicfMACfilterSourceMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfMACfilterSourceMac_Type.__name__ = "OctetString"
_HpnicfMACfilterSourceMac_Object = MibScalar
hpnicfMACfilterSourceMac = _HpnicfMACfilterSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 5),
    _HpnicfMACfilterSourceMac_Type()
)
hpnicfMACfilterSourceMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMACfilterSourceMac.setStatus("current")


class _HpnicfMACfilterDestinationMac_Type(OctetString):
    """Custom type hpnicfMACfilterDestinationMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfMACfilterDestinationMac_Type.__name__ = "OctetString"
_HpnicfMACfilterDestinationMac_Object = MibScalar
hpnicfMACfilterDestinationMac = _HpnicfMACfilterDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 6),
    _HpnicfMACfilterDestinationMac_Type()
)
hpnicfMACfilterDestinationMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMACfilterDestinationMac.setStatus("current")
_HpnicfPfilterPacketNumber_Type = Integer32
_HpnicfPfilterPacketNumber_Object = MibScalar
hpnicfPfilterPacketNumber = _HpnicfPfilterPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 7),
    _HpnicfPfilterPacketNumber_Type()
)
hpnicfPfilterPacketNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPfilterPacketNumber.setStatus("current")


class _HpnicfPfilterReceiveInterface_Type(OctetString):
    """Custom type hpnicfPfilterReceiveInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfPfilterReceiveInterface_Type.__name__ = "OctetString"
_HpnicfPfilterReceiveInterface_Object = MibScalar
hpnicfPfilterReceiveInterface = _HpnicfPfilterReceiveInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 8),
    _HpnicfPfilterReceiveInterface_Type()
)
hpnicfPfilterReceiveInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPfilterReceiveInterface.setStatus("current")


class _HpnicfAclPacketIfName_Type(OctetString):
    """Custom type hpnicfAclPacketIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclPacketIfName_Type.__name__ = "OctetString"
_HpnicfAclPacketIfName_Object = MibScalar
hpnicfAclPacketIfName = _HpnicfAclPacketIfName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 9),
    _HpnicfAclPacketIfName_Type()
)
hpnicfAclPacketIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAclPacketIfName.setStatus("current")
_HpnicfAclPacketDirection_Type = DirectionType
_HpnicfAclPacketDirection_Object = MibScalar
hpnicfAclPacketDirection = _HpnicfAclPacketDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 10),
    _HpnicfAclPacketDirection_Type()
)
hpnicfAclPacketDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAclPacketDirection.setStatus("current")


class _HpnicfAclPacketBAGG_Type(Integer32):
    """Custom type hpnicfAclPacketBAGG based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_HpnicfAclPacketBAGG_Type.__name__ = "Integer32"
_HpnicfAclPacketBAGG_Object = MibScalar
hpnicfAclPacketBAGG = _HpnicfAclPacketBAGG_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 11),
    _HpnicfAclPacketBAGG_Type()
)
hpnicfAclPacketBAGG.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAclPacketBAGG.setStatus("current")


class _HpnicfAclPacketVlanID_Type(Integer32):
    """Custom type hpnicfAclPacketVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfAclPacketVlanID_Type.__name__ = "Integer32"
_HpnicfAclPacketVlanID_Object = MibScalar
hpnicfAclPacketVlanID = _HpnicfAclPacketVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 12),
    _HpnicfAclPacketVlanID_Type()
)
hpnicfAclPacketVlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAclPacketVlanID.setStatus("current")


class _HpnicfAclPacketSrcIP_Type(OctetString):
    """Custom type hpnicfAclPacketSrcIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclPacketSrcIP_Type.__name__ = "OctetString"
_HpnicfAclPacketSrcIP_Object = MibScalar
hpnicfAclPacketSrcIP = _HpnicfAclPacketSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 13),
    _HpnicfAclPacketSrcIP_Type()
)
hpnicfAclPacketSrcIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAclPacketSrcIP.setStatus("current")


class _HpnicfAclPacketDstIP_Type(OctetString):
    """Custom type hpnicfAclPacketDstIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAclPacketDstIP_Type.__name__ = "OctetString"
_HpnicfAclPacketDstIP_Object = MibScalar
hpnicfAclPacketDstIP = _HpnicfAclPacketDstIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 14),
    _HpnicfAclPacketDstIP_Type()
)
hpnicfAclPacketDstIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAclPacketDstIP.setStatus("current")


class _HpnicfAclPacketProtocol_Type(Integer32):
    """Custom type hpnicfAclPacketProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfAclPacketProtocol_Type.__name__ = "Integer32"
_HpnicfAclPacketProtocol_Object = MibScalar
hpnicfAclPacketProtocol = _HpnicfAclPacketProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 15),
    _HpnicfAclPacketProtocol_Type()
)
hpnicfAclPacketProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAclPacketProtocol.setStatus("current")


class _HpnicfAclPacketDscp_Type(DSCPValue):
    """Custom type hpnicfAclPacketDscp based on DSCPValue"""
    defaultValue = 255


_HpnicfAclPacketDscp_Type.__name__ = "DSCPValue"
_HpnicfAclPacketDscp_Object = MibScalar
hpnicfAclPacketDscp = _HpnicfAclPacketDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 16),
    _HpnicfAclPacketDscp_Type()
)
hpnicfAclPacketDscp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAclPacketDscp.setStatus("current")


class _HpnicfAclPacketFlowLabel_Type(Unsigned32):
    """Custom type hpnicfAclPacketFlowLabel based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_HpnicfAclPacketFlowLabel_Type.__name__ = "Unsigned32"
_HpnicfAclPacketFlowLabel_Object = MibScalar
hpnicfAclPacketFlowLabel = _HpnicfAclPacketFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 17),
    _HpnicfAclPacketFlowLabel_Type()
)
hpnicfAclPacketFlowLabel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAclPacketFlowLabel.setStatus("current")


class _HpnicfAclPacketIcmpIgmpType_Type(Integer32):
    """Custom type hpnicfAclPacketIcmpIgmpType based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfAclPacketIcmpIgmpType_Type.__name__ = "Integer32"
_HpnicfAclPacketIcmpIgmpType_Object = MibScalar
hpnicfAclPacketIcmpIgmpType = _HpnicfAclPacketIcmpIgmpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 18),
    _HpnicfAclPacketIcmpIgmpType_Type()
)
hpnicfAclPacketIcmpIgmpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAclPacketIcmpIgmpType.setStatus("current")


class _HpnicfAclPacketIcmpIgmpCode_Type(Integer32):
    """Custom type hpnicfAclPacketIcmpIgmpCode based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfAclPacketIcmpIgmpCode_Type.__name__ = "Integer32"
_HpnicfAclPacketIcmpIgmpCode_Object = MibScalar
hpnicfAclPacketIcmpIgmpCode = _HpnicfAclPacketIcmpIgmpCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 19),
    _HpnicfAclPacketIcmpIgmpCode_Type()
)
hpnicfAclPacketIcmpIgmpCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAclPacketIcmpIgmpCode.setStatus("current")


class _HpnicfAclPacketTcpFlags_Type(Integer32):
    """Custom type hpnicfAclPacketTcpFlags based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("tcpack", 1),
          ("tcpfin", 2),
          ("tcppsh", 3),
          ("tcprst", 4),
          ("tcpsyn", 5),
          ("tcpurg", 6),
          ("invalid", 255))
    )


_HpnicfAclPacketTcpFlags_Type.__name__ = "Integer32"
_HpnicfAclPacketTcpFlags_Object = MibScalar
hpnicfAclPacketTcpFlags = _HpnicfAclPacketTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 20),
    _HpnicfAclPacketTcpFlags_Type()
)
hpnicfAclPacketTcpFlags.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAclPacketTcpFlags.setStatus("current")


class _HpnicfAclPacketSrcPort_Type(Integer32):
    """Custom type hpnicfAclPacketSrcPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclPacketSrcPort_Type.__name__ = "Integer32"
_HpnicfAclPacketSrcPort_Object = MibScalar
hpnicfAclPacketSrcPort = _HpnicfAclPacketSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 21),
    _HpnicfAclPacketSrcPort_Type()
)
hpnicfAclPacketSrcPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAclPacketSrcPort.setStatus("current")


class _HpnicfAclPacketDstPort_Type(Integer32):
    """Custom type hpnicfAclPacketDstPort based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclPacketDstPort_Type.__name__ = "Integer32"
_HpnicfAclPacketDstPort_Object = MibScalar
hpnicfAclPacketDstPort = _HpnicfAclPacketDstPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 22),
    _HpnicfAclPacketDstPort_Type()
)
hpnicfAclPacketDstPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAclPacketDstPort.setStatus("current")
_HpnicfAclPacketSrcMacAddr_Type = MacAddress
_HpnicfAclPacketSrcMacAddr_Object = MibScalar
hpnicfAclPacketSrcMacAddr = _HpnicfAclPacketSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 23),
    _HpnicfAclPacketSrcMacAddr_Type()
)
hpnicfAclPacketSrcMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAclPacketSrcMacAddr.setStatus("current")
_HpnicfAclPacketDstMacAddr_Type = MacAddress
_HpnicfAclPacketDstMacAddr_Object = MibScalar
hpnicfAclPacketDstMacAddr = _HpnicfAclPacketDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 24),
    _HpnicfAclPacketDstMacAddr_Type()
)
hpnicfAclPacketDstMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAclPacketDstMacAddr.setStatus("current")


class _HpnicfAclPacketMacTypeLen_Type(Integer32):
    """Custom type hpnicfAclPacketMacTypeLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAclPacketMacTypeLen_Type.__name__ = "Integer32"
_HpnicfAclPacketMacTypeLen_Object = MibScalar
hpnicfAclPacketMacTypeLen = _HpnicfAclPacketMacTypeLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 25),
    _HpnicfAclPacketMacTypeLen_Type()
)
hpnicfAclPacketMacTypeLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAclPacketMacTypeLen.setStatus("current")


class _HpnicfAclPacketVlanPCP_Type(Integer32):
    """Custom type hpnicfAclPacketVlanPCP based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfAclPacketVlanPCP_Type.__name__ = "Integer32"
_HpnicfAclPacketVlanPCP_Object = MibScalar
hpnicfAclPacketVlanPCP = _HpnicfAclPacketVlanPCP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 4, 26),
    _HpnicfAclPacketVlanPCP_Type()
)
hpnicfAclPacketVlanPCP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAclPacketVlanPCP.setStatus("current")
_HpnicfAclPacketfilterTrap_ObjectIdentity = ObjectIdentity
hpnicfAclPacketfilterTrap = _HpnicfAclPacketfilterTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 5)
)
_HpnicfPfilterTrapPrefix_ObjectIdentity = ObjectIdentity
hpnicfPfilterTrapPrefix = _HpnicfPfilterTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 5, 0)
)

# Managed Objects groups


# Notification objects

hpnicfMACfilterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 5, 0, 1)
)
hpnicfMACfilterTrap.setObjects(
      *(("HPN-ICF-ACL-MIB", "hpnicfPfilterInterface"),
        ("HPN-ICF-ACL-MIB", "hpnicfPfilterDirection"),
        ("HPN-ICF-ACL-MIB", "hpnicfPfilterACLNumber"),
        ("HPN-ICF-ACL-MIB", "hpnicfPfilterAction"),
        ("HPN-ICF-ACL-MIB", "hpnicfMACfilterSourceMac"),
        ("HPN-ICF-ACL-MIB", "hpnicfMACfilterDestinationMac"),
        ("HPN-ICF-ACL-MIB", "hpnicfPfilterPacketNumber"),
        ("HPN-ICF-ACL-MIB", "hpnicfPfilterReceiveInterface"))
)
if mibBuilder.loadTexts:
    hpnicfMACfilterTrap.setStatus(
        "current"
    )

hpnicfAclRuleMatchCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 5, 0, 2)
)
hpnicfAclRuleMatchCount.setObjects(
      *(("HPN-ICF-ACL-MIB", "hpnicfPfilter2ApplyObjType"),
        ("HPN-ICF-ACL-MIB", "hpnicfPfilter2ApplyObjIndex"),
        ("HPN-ICF-ACL-MIB", "hpnicfPfilter2ApplyDirection"),
        ("HPN-ICF-ACL-MIB", "hpnicfPfilter2ApplyAclType"),
        ("HPN-ICF-ACL-MIB", "hpnicfPfilter2ApplyAclIndex"),
        ("HPN-ICF-ACL-MIB", "hpnicfPfilter2AclRuleIndex"),
        ("HPN-ICF-ACL-MIB", "hpnicfPfilter2AclRuleMatchPackets"))
)
if mibBuilder.loadTexts:
    hpnicfAclRuleMatchCount.setStatus(
        "current"
    )

hpnicfAclFirstIPv4PktCaptured = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 5, 0, 3)
)
hpnicfAclFirstIPv4PktCaptured.setObjects(
      *(("HPN-ICF-ACL-MIB", "hpnicfPfilter2ApplyAclIndex"),
        ("HPN-ICF-ACL-MIB", "hpnicfPfilter2AclRuleIndex"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketIfName"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketDirection"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketBAGG"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketVlanID"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketSrcIP"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketDstIP"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketProtocol"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketDscp"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketIcmpIgmpType"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketIcmpIgmpCode"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketTcpFlags"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketSrcPort"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketDstPort"))
)
if mibBuilder.loadTexts:
    hpnicfAclFirstIPv4PktCaptured.setStatus(
        "current"
    )

hpnicfAclFirstIPv6PktCaptured = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 5, 0, 4)
)
hpnicfAclFirstIPv6PktCaptured.setObjects(
      *(("HPN-ICF-ACL-MIB", "hpnicfPfilter2ApplyAclIndex"),
        ("HPN-ICF-ACL-MIB", "hpnicfPfilter2AclRuleIndex"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketIfName"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketDirection"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketBAGG"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketVlanID"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketSrcIP"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketDstIP"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketProtocol"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketDscp"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketFlowLabel"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketIcmpIgmpType"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketIcmpIgmpCode"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketTcpFlags"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketSrcPort"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketDstPort"))
)
if mibBuilder.loadTexts:
    hpnicfAclFirstIPv6PktCaptured.setStatus(
        "current"
    )

hpnicfAclFirstEthernetPktCaptured = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8, 5, 0, 5)
)
hpnicfAclFirstEthernetPktCaptured.setObjects(
      *(("HPN-ICF-ACL-MIB", "hpnicfPfilter2ApplyAclIndex"),
        ("HPN-ICF-ACL-MIB", "hpnicfPfilter2AclRuleIndex"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketIfName"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketDirection"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketBAGG"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketVlanID"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketSrcMacAddr"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketDstMacAddr"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketMacTypeLen"),
        ("HPN-ICF-ACL-MIB", "hpnicfAclPacketVlanPCP"))
)
if mibBuilder.loadTexts:
    hpnicfAclFirstEthernetPktCaptured.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-ACL-MIB",
    **{"RuleAction": RuleAction,
       "CounterClear": CounterClear,
       "PortOp": PortOp,
       "DSCPValue": DSCPValue,
       "TCPFlag": TCPFlag,
       "FragmentFlag": FragmentFlag,
       "AddressFlag": AddressFlag,
       "DirectionType": DirectionType,
       "hpnicfAcl": hpnicfAcl,
       "hpnicfAclMibObjects": hpnicfAclMibObjects,
       "hpnicfAclMode": hpnicfAclMode,
       "hpnicfAclNumGroupTable": hpnicfAclNumGroupTable,
       "hpnicfAclNumGroupEntry": hpnicfAclNumGroupEntry,
       "hpnicfAclNumGroupAclNum": hpnicfAclNumGroupAclNum,
       "hpnicfAclNumGroupMatchOrder": hpnicfAclNumGroupMatchOrder,
       "hpnicfAclNumGroupSubitemNum": hpnicfAclNumGroupSubitemNum,
       "hpnicfAclNumGroupDescription": hpnicfAclNumGroupDescription,
       "hpnicfAclNumGroupCountClear": hpnicfAclNumGroupCountClear,
       "hpnicfAclNumGroupRowStatus": hpnicfAclNumGroupRowStatus,
       "hpnicfAclNameGroupTable": hpnicfAclNameGroupTable,
       "hpnicfAclNameGroupEntry": hpnicfAclNameGroupEntry,
       "hpnicfAclNameGroupIndex": hpnicfAclNameGroupIndex,
       "hpnicfAclNameGroupCreateName": hpnicfAclNameGroupCreateName,
       "hpnicfAclNameGroupTypes": hpnicfAclNameGroupTypes,
       "hpnicfAclNameGroupMatchOrder": hpnicfAclNameGroupMatchOrder,
       "hpnicfAclNameGroupSubitemNum": hpnicfAclNameGroupSubitemNum,
       "hpnicfAclNameGroupRowStatus": hpnicfAclNameGroupRowStatus,
       "hpnicfAclBasicRuleTable": hpnicfAclBasicRuleTable,
       "hpnicfAclBasicRuleEntry": hpnicfAclBasicRuleEntry,
       "hpnicfAclBasicAclNum": hpnicfAclBasicAclNum,
       "hpnicfAclBasicSubitem": hpnicfAclBasicSubitem,
       "hpnicfAclBasicAct": hpnicfAclBasicAct,
       "hpnicfAclBasicSrcIp": hpnicfAclBasicSrcIp,
       "hpnicfAclBasicSrcWild": hpnicfAclBasicSrcWild,
       "hpnicfAclBasicTimeRangeName": hpnicfAclBasicTimeRangeName,
       "hpnicfAclBasicFragments": hpnicfAclBasicFragments,
       "hpnicfAclBasicLog": hpnicfAclBasicLog,
       "hpnicfAclBasicEnable": hpnicfAclBasicEnable,
       "hpnicfAclBasicCount": hpnicfAclBasicCount,
       "hpnicfAclBasicCountClear": hpnicfAclBasicCountClear,
       "hpnicfAclBasicRowStatus": hpnicfAclBasicRowStatus,
       "hpnicfAclAdvancedRuleTable": hpnicfAclAdvancedRuleTable,
       "hpnicfAclAdvancedRuleEntry": hpnicfAclAdvancedRuleEntry,
       "hpnicfAclAdvancedAclNum": hpnicfAclAdvancedAclNum,
       "hpnicfAclAdvancedSubitem": hpnicfAclAdvancedSubitem,
       "hpnicfAclAdvancedAct": hpnicfAclAdvancedAct,
       "hpnicfAclAdvancedProtocol": hpnicfAclAdvancedProtocol,
       "hpnicfAclAdvancedSrcIp": hpnicfAclAdvancedSrcIp,
       "hpnicfAclAdvancedSrcWild": hpnicfAclAdvancedSrcWild,
       "hpnicfAclAdvancedSrcOp": hpnicfAclAdvancedSrcOp,
       "hpnicfAclAdvancedSrcPort1": hpnicfAclAdvancedSrcPort1,
       "hpnicfAclAdvancedSrcPort2": hpnicfAclAdvancedSrcPort2,
       "hpnicfAclAdvancedDestIp": hpnicfAclAdvancedDestIp,
       "hpnicfAclAdvancedDestWild": hpnicfAclAdvancedDestWild,
       "hpnicfAclAdvancedDestOp": hpnicfAclAdvancedDestOp,
       "hpnicfAclAdvancedDestPort1": hpnicfAclAdvancedDestPort1,
       "hpnicfAclAdvancedDestPort2": hpnicfAclAdvancedDestPort2,
       "hpnicfAclAdvancedPrecedence": hpnicfAclAdvancedPrecedence,
       "hpnicfAclAdvancedTos": hpnicfAclAdvancedTos,
       "hpnicfAclAdvancedDscp": hpnicfAclAdvancedDscp,
       "hpnicfAclAdvancedEstablish": hpnicfAclAdvancedEstablish,
       "hpnicfAclAdvancedTimeRangeName": hpnicfAclAdvancedTimeRangeName,
       "hpnicfAclAdvancedIcmpType": hpnicfAclAdvancedIcmpType,
       "hpnicfAclAdvancedIcmpCode": hpnicfAclAdvancedIcmpCode,
       "hpnicfAclAdvancedFragments": hpnicfAclAdvancedFragments,
       "hpnicfAclAdvancedLog": hpnicfAclAdvancedLog,
       "hpnicfAclAdvancedEnable": hpnicfAclAdvancedEnable,
       "hpnicfAclAdvancedCount": hpnicfAclAdvancedCount,
       "hpnicfAclAdvancedCountClear": hpnicfAclAdvancedCountClear,
       "hpnicfAclAdvancedRowStatus": hpnicfAclAdvancedRowStatus,
       "hpnicfAclIfRuleTable": hpnicfAclIfRuleTable,
       "hpnicfAclIfRuleEntry": hpnicfAclIfRuleEntry,
       "hpnicfAclIfAclNum": hpnicfAclIfAclNum,
       "hpnicfAclIfSubitem": hpnicfAclIfSubitem,
       "hpnicfAclIfAct": hpnicfAclIfAct,
       "hpnicfAclIfIndex": hpnicfAclIfIndex,
       "hpnicfAclIfAny": hpnicfAclIfAny,
       "hpnicfAclIfTimeRangeName": hpnicfAclIfTimeRangeName,
       "hpnicfAclIfLog": hpnicfAclIfLog,
       "hpnicfAclIfEnable": hpnicfAclIfEnable,
       "hpnicfAclIfCount": hpnicfAclIfCount,
       "hpnicfAclIfCountClear": hpnicfAclIfCountClear,
       "hpnicfAclIfRowStatus": hpnicfAclIfRowStatus,
       "hpnicfAclLinkTable": hpnicfAclLinkTable,
       "hpnicfAclLinkEntry": hpnicfAclLinkEntry,
       "hpnicfAclLinkAclNum": hpnicfAclLinkAclNum,
       "hpnicfAclLinkSubitem": hpnicfAclLinkSubitem,
       "hpnicfAclLinkAct": hpnicfAclLinkAct,
       "hpnicfAclLinkProtocol": hpnicfAclLinkProtocol,
       "hpnicfAclLinkFormatType": hpnicfAclLinkFormatType,
       "hpnicfAclLinkVlanTag": hpnicfAclLinkVlanTag,
       "hpnicfAclLinkVlanPri": hpnicfAclLinkVlanPri,
       "hpnicfAclLinkSrcVlanId": hpnicfAclLinkSrcVlanId,
       "hpnicfAclLinkSrcMac": hpnicfAclLinkSrcMac,
       "hpnicfAclLinkSrcMacWild": hpnicfAclLinkSrcMacWild,
       "hpnicfAclLinkSrcIfIndex": hpnicfAclLinkSrcIfIndex,
       "hpnicfAclLinkSrcAny": hpnicfAclLinkSrcAny,
       "hpnicfAclLinkDestVlanId": hpnicfAclLinkDestVlanId,
       "hpnicfAclLinkDestMac": hpnicfAclLinkDestMac,
       "hpnicfAclLinkDestMacWild": hpnicfAclLinkDestMacWild,
       "hpnicfAclLinkDestIfIndex": hpnicfAclLinkDestIfIndex,
       "hpnicfAclLinkDestAny": hpnicfAclLinkDestAny,
       "hpnicfAclLinkTimeRangeName": hpnicfAclLinkTimeRangeName,
       "hpnicfAclLinkEnable": hpnicfAclLinkEnable,
       "hpnicfAclLinkRowStatus": hpnicfAclLinkRowStatus,
       "hpnicfAclLinkTypeCode": hpnicfAclLinkTypeCode,
       "hpnicfAclLinkTypeMask": hpnicfAclLinkTypeMask,
       "hpnicfAclLinkLsapCode": hpnicfAclLinkLsapCode,
       "hpnicfAclLinkLsapMask": hpnicfAclLinkLsapMask,
       "hpnicfAclLinkL2LabelRangeOp": hpnicfAclLinkL2LabelRangeOp,
       "hpnicfAclLinkL2LabelRangeBegin": hpnicfAclLinkL2LabelRangeBegin,
       "hpnicfAclLinkL2LabelRangeEnd": hpnicfAclLinkL2LabelRangeEnd,
       "hpnicfAclLinkMplsExp": hpnicfAclLinkMplsExp,
       "hpnicfAclUserTable": hpnicfAclUserTable,
       "hpnicfAclUserEntry": hpnicfAclUserEntry,
       "hpnicfAclUserAclNum": hpnicfAclUserAclNum,
       "hpnicfAclUserSubitem": hpnicfAclUserSubitem,
       "hpnicfAclUserAct": hpnicfAclUserAct,
       "hpnicfAclUserFormatType": hpnicfAclUserFormatType,
       "hpnicfAclUserVlanTag": hpnicfAclUserVlanTag,
       "hpnicfAclUserRuleStr": hpnicfAclUserRuleStr,
       "hpnicfAclUserRuleMask": hpnicfAclUserRuleMask,
       "hpnicfAclUserTimeRangeName": hpnicfAclUserTimeRangeName,
       "hpnicfAclUserEnable": hpnicfAclUserEnable,
       "hpnicfAclUserRowStatus": hpnicfAclUserRowStatus,
       "hpnicfAclActiveTable": hpnicfAclActiveTable,
       "hpnicfAclActiveEntry": hpnicfAclActiveEntry,
       "hpnicfAclActiveAclIndex": hpnicfAclActiveAclIndex,
       "hpnicfAclActiveIfIndex": hpnicfAclActiveIfIndex,
       "hpnicfAclActiveVlanID": hpnicfAclActiveVlanID,
       "hpnicfAclActiveDirection": hpnicfAclActiveDirection,
       "hpnicfAclActiveUserAclNum": hpnicfAclActiveUserAclNum,
       "hpnicfAclActiveUserAclSubitem": hpnicfAclActiveUserAclSubitem,
       "hpnicfAclActiveIpAclNum": hpnicfAclActiveIpAclNum,
       "hpnicfAclActiveIpAclSubitem": hpnicfAclActiveIpAclSubitem,
       "hpnicfAclActiveLinkAclNum": hpnicfAclActiveLinkAclNum,
       "hpnicfAclActiveLinkAclSubitem": hpnicfAclActiveLinkAclSubitem,
       "hpnicfAclActiveRuntime": hpnicfAclActiveRuntime,
       "hpnicfAclActiveRowStatus": hpnicfAclActiveRowStatus,
       "hpnicfAclIDSTable": hpnicfAclIDSTable,
       "hpnicfAclIDSEntry": hpnicfAclIDSEntry,
       "hpnicfAclIDSName": hpnicfAclIDSName,
       "hpnicfAclIDSSrcMac": hpnicfAclIDSSrcMac,
       "hpnicfAclIDSDestMac": hpnicfAclIDSDestMac,
       "hpnicfAclIDSSrcIp": hpnicfAclIDSSrcIp,
       "hpnicfAclIDSSrcWild": hpnicfAclIDSSrcWild,
       "hpnicfAclIDSDestIp": hpnicfAclIDSDestIp,
       "hpnicfAclIDSDestWild": hpnicfAclIDSDestWild,
       "hpnicfAclIDSSrcPort": hpnicfAclIDSSrcPort,
       "hpnicfAclIDSDestPort": hpnicfAclIDSDestPort,
       "hpnicfAclIDSProtocol": hpnicfAclIDSProtocol,
       "hpnicfAclIDSDenyTime": hpnicfAclIDSDenyTime,
       "hpnicfAclIDSAct": hpnicfAclIDSAct,
       "hpnicfAclIDSRowStatus": hpnicfAclIDSRowStatus,
       "hpnicfAclMib2Objects": hpnicfAclMib2Objects,
       "hpnicfAclMib2GlobalGroup": hpnicfAclMib2GlobalGroup,
       "hpnicfAclMib2NodesGroup": hpnicfAclMib2NodesGroup,
       "hpnicfAclMib2Mode": hpnicfAclMib2Mode,
       "hpnicfAclMib2Version": hpnicfAclMib2Version,
       "hpnicfAclMib2ObjectsCapabilities": hpnicfAclMib2ObjectsCapabilities,
       "hpnicfAclMib2ProcessingStatus": hpnicfAclMib2ProcessingStatus,
       "hpnicfAclMib2CapabilityTable": hpnicfAclMib2CapabilityTable,
       "hpnicfAclMib2CapabilityEntry": hpnicfAclMib2CapabilityEntry,
       "hpnicfAclMib2EntityType": hpnicfAclMib2EntityType,
       "hpnicfAclMib2EntityIndex": hpnicfAclMib2EntityIndex,
       "hpnicfAclMib2ModuleIndex": hpnicfAclMib2ModuleIndex,
       "hpnicfAclMib2CharacteristicsIndex": hpnicfAclMib2CharacteristicsIndex,
       "hpnicfAclMib2CharacteristicsDesc": hpnicfAclMib2CharacteristicsDesc,
       "hpnicfAclMib2CharacteristicsValue": hpnicfAclMib2CharacteristicsValue,
       "hpnicfAclNumberGroupTable": hpnicfAclNumberGroupTable,
       "hpnicfAclNumberGroupEntry": hpnicfAclNumberGroupEntry,
       "hpnicfAclNumberGroupType": hpnicfAclNumberGroupType,
       "hpnicfAclNumberGroupIndex": hpnicfAclNumberGroupIndex,
       "hpnicfAclNumberGroupRowStatus": hpnicfAclNumberGroupRowStatus,
       "hpnicfAclNumberGroupMatchOrder": hpnicfAclNumberGroupMatchOrder,
       "hpnicfAclNumberGroupStep": hpnicfAclNumberGroupStep,
       "hpnicfAclNumberGroupDescription": hpnicfAclNumberGroupDescription,
       "hpnicfAclNumberGroupCountClear": hpnicfAclNumberGroupCountClear,
       "hpnicfAclNumberGroupRuleCounter": hpnicfAclNumberGroupRuleCounter,
       "hpnicfAclNumberGroupName": hpnicfAclNumberGroupName,
       "hpnicfAclNamedGroupTable": hpnicfAclNamedGroupTable,
       "hpnicfAclNamedGroupEntry": hpnicfAclNamedGroupEntry,
       "hpnicfAclNamedGroupCategory": hpnicfAclNamedGroupCategory,
       "hpnicfAclNamedGroupName": hpnicfAclNamedGroupName,
       "hpnicfAclNamedGroupRowStatus": hpnicfAclNamedGroupRowStatus,
       "hpnicfAclNamedGroupMatchOrder": hpnicfAclNamedGroupMatchOrder,
       "hpnicfAclNamedGroupStep": hpnicfAclNamedGroupStep,
       "hpnicfAclNamedGroupDescription": hpnicfAclNamedGroupDescription,
       "hpnicfAclNamedGroupCountClear": hpnicfAclNamedGroupCountClear,
       "hpnicfAclNamedGroupRuleCounter": hpnicfAclNamedGroupRuleCounter,
       "hpnicfAclIPAclGroup": hpnicfAclIPAclGroup,
       "hpnicfAclIPAclBasicTable": hpnicfAclIPAclBasicTable,
       "hpnicfAclIPAclBasicEntry": hpnicfAclIPAclBasicEntry,
       "hpnicfAclIPAclBasicRuleIndex": hpnicfAclIPAclBasicRuleIndex,
       "hpnicfAclIPAclBasicRowStatus": hpnicfAclIPAclBasicRowStatus,
       "hpnicfAclIPAclBasicAct": hpnicfAclIPAclBasicAct,
       "hpnicfAclIPAclBasicSrcAddrType": hpnicfAclIPAclBasicSrcAddrType,
       "hpnicfAclIPAclBasicSrcAddr": hpnicfAclIPAclBasicSrcAddr,
       "hpnicfAclIPAclBasicSrcPrefix": hpnicfAclIPAclBasicSrcPrefix,
       "hpnicfAclIPAclBasicSrcAny": hpnicfAclIPAclBasicSrcAny,
       "hpnicfAclIPAclBasicSrcWild": hpnicfAclIPAclBasicSrcWild,
       "hpnicfAclIPAclBasicTimeRangeName": hpnicfAclIPAclBasicTimeRangeName,
       "hpnicfAclIPAclBasicFragmentFlag": hpnicfAclIPAclBasicFragmentFlag,
       "hpnicfAclIPAclBasicLog": hpnicfAclIPAclBasicLog,
       "hpnicfAclIPAclBasicCount": hpnicfAclIPAclBasicCount,
       "hpnicfAclIPAclBasicCountClear": hpnicfAclIPAclBasicCountClear,
       "hpnicfAclIPAclBasicEnable": hpnicfAclIPAclBasicEnable,
       "hpnicfAclIPAclBasicVpnInstanceName": hpnicfAclIPAclBasicVpnInstanceName,
       "hpnicfAclIPAclBasicComment": hpnicfAclIPAclBasicComment,
       "hpnicfAclIPAclBasicCounting": hpnicfAclIPAclBasicCounting,
       "hpnicfAclIPAclBasicRouteTypeAny": hpnicfAclIPAclBasicRouteTypeAny,
       "hpnicfAclIPAclBasicRouteTypeValue": hpnicfAclIPAclBasicRouteTypeValue,
       "hpnicfAclIPAclAdvancedTable": hpnicfAclIPAclAdvancedTable,
       "hpnicfAclIPAclAdvancedEntry": hpnicfAclIPAclAdvancedEntry,
       "hpnicfAclIPAclAdvancedRuleIndex": hpnicfAclIPAclAdvancedRuleIndex,
       "hpnicfAclIPAclAdvancedRowStatus": hpnicfAclIPAclAdvancedRowStatus,
       "hpnicfAclIPAclAdvancedAct": hpnicfAclIPAclAdvancedAct,
       "hpnicfAclIPAclAdvancedProtocol": hpnicfAclIPAclAdvancedProtocol,
       "hpnicfAclIPAclAdvancedAddrFlag": hpnicfAclIPAclAdvancedAddrFlag,
       "hpnicfAclIPAclAdvancedSrcAddrType": hpnicfAclIPAclAdvancedSrcAddrType,
       "hpnicfAclIPAclAdvancedSrcAddr": hpnicfAclIPAclAdvancedSrcAddr,
       "hpnicfAclIPAclAdvancedSrcPrefix": hpnicfAclIPAclAdvancedSrcPrefix,
       "hpnicfAclIPAclAdvancedSrcAny": hpnicfAclIPAclAdvancedSrcAny,
       "hpnicfAclIPAclAdvancedSrcWild": hpnicfAclIPAclAdvancedSrcWild,
       "hpnicfAclIPAclAdvancedSrcOp": hpnicfAclIPAclAdvancedSrcOp,
       "hpnicfAclIPAclAdvancedSrcPort1": hpnicfAclIPAclAdvancedSrcPort1,
       "hpnicfAclIPAclAdvancedSrcPort2": hpnicfAclIPAclAdvancedSrcPort2,
       "hpnicfAclIPAclAdvancedDestAddrType": hpnicfAclIPAclAdvancedDestAddrType,
       "hpnicfAclIPAclAdvancedDestAddr": hpnicfAclIPAclAdvancedDestAddr,
       "hpnicfAclIPAclAdvancedDestPrefix": hpnicfAclIPAclAdvancedDestPrefix,
       "hpnicfAclIPAclAdvancedDestAny": hpnicfAclIPAclAdvancedDestAny,
       "hpnicfAclIPAclAdvancedDestWild": hpnicfAclIPAclAdvancedDestWild,
       "hpnicfAclIPAclAdvancedDestOp": hpnicfAclIPAclAdvancedDestOp,
       "hpnicfAclIPAclAdvancedDestPort1": hpnicfAclIPAclAdvancedDestPort1,
       "hpnicfAclIPAclAdvancedDestPort2": hpnicfAclIPAclAdvancedDestPort2,
       "hpnicfAclIPAclAdvancedIcmpType": hpnicfAclIPAclAdvancedIcmpType,
       "hpnicfAclIPAclAdvancedIcmpCode": hpnicfAclIPAclAdvancedIcmpCode,
       "hpnicfAclIPAclAdvancedPrecedence": hpnicfAclIPAclAdvancedPrecedence,
       "hpnicfAclIPAclAdvancedTos": hpnicfAclIPAclAdvancedTos,
       "hpnicfAclIPAclAdvancedDscp": hpnicfAclIPAclAdvancedDscp,
       "hpnicfAclIPAclAdvancedTimeRangeName": hpnicfAclIPAclAdvancedTimeRangeName,
       "hpnicfAclIPAclAdvancedTCPFlag": hpnicfAclIPAclAdvancedTCPFlag,
       "hpnicfAclIPAclAdvancedFragmentFlag": hpnicfAclIPAclAdvancedFragmentFlag,
       "hpnicfAclIPAclAdvancedLog": hpnicfAclIPAclAdvancedLog,
       "hpnicfAclIPAclAdvancedCount": hpnicfAclIPAclAdvancedCount,
       "hpnicfAclIPAclAdvancedCountClear": hpnicfAclIPAclAdvancedCountClear,
       "hpnicfAclIPAclAdvancedEnable": hpnicfAclIPAclAdvancedEnable,
       "hpnicfAclIPAclAdvancedVpnInstanceName": hpnicfAclIPAclAdvancedVpnInstanceName,
       "hpnicfAclIPAclAdvancedComment": hpnicfAclIPAclAdvancedComment,
       "hpnicfAclIPAclAdvancedReflective": hpnicfAclIPAclAdvancedReflective,
       "hpnicfAclIPAclAdvancedCounting": hpnicfAclIPAclAdvancedCounting,
       "hpnicfAclIPAclAdvancedTCPFlagMask": hpnicfAclIPAclAdvancedTCPFlagMask,
       "hpnicfAclIPAclAdvancedTCPFlagValue": hpnicfAclIPAclAdvancedTCPFlagValue,
       "hpnicfAclIPAclAdvancedRouteTypeAny": hpnicfAclIPAclAdvancedRouteTypeAny,
       "hpnicfAclIPAclAdvancedRouteTypeValue": hpnicfAclIPAclAdvancedRouteTypeValue,
       "hpnicfAclIPAclAdvancedFlowLabel": hpnicfAclIPAclAdvancedFlowLabel,
       "hpnicfAclIPAclAdvancedSrcSuffix": hpnicfAclIPAclAdvancedSrcSuffix,
       "hpnicfAclIPAclAdvancedDestSuffix": hpnicfAclIPAclAdvancedDestSuffix,
       "hpnicfAclIPAclNamedBscTable": hpnicfAclIPAclNamedBscTable,
       "hpnicfAclIPAclNamedBscEntry": hpnicfAclIPAclNamedBscEntry,
       "hpnicfAclIPAclNamedBscRowStatus": hpnicfAclIPAclNamedBscRowStatus,
       "hpnicfAclIPAclNamedBscAct": hpnicfAclIPAclNamedBscAct,
       "hpnicfAclIPAclNamedBscSrcAddrType": hpnicfAclIPAclNamedBscSrcAddrType,
       "hpnicfAclIPAclNamedBscSrcAddr": hpnicfAclIPAclNamedBscSrcAddr,
       "hpnicfAclIPAclNamedBscSrcPrefix": hpnicfAclIPAclNamedBscSrcPrefix,
       "hpnicfAclIPAclNamedBscSrcAny": hpnicfAclIPAclNamedBscSrcAny,
       "hpnicfAclIPAclNamedBscSrcWild": hpnicfAclIPAclNamedBscSrcWild,
       "hpnicfAclIPAclNamedBscTRangeName": hpnicfAclIPAclNamedBscTRangeName,
       "hpnicfAclIPAclNamedBscFragmentFlag": hpnicfAclIPAclNamedBscFragmentFlag,
       "hpnicfAclIPAclNamedBscLog": hpnicfAclIPAclNamedBscLog,
       "hpnicfAclIPAclNamedBscCount": hpnicfAclIPAclNamedBscCount,
       "hpnicfAclIPAclNamedBscCountClear": hpnicfAclIPAclNamedBscCountClear,
       "hpnicfAclIPAclNamedBscEnable": hpnicfAclIPAclNamedBscEnable,
       "hpnicfAclIPAclNamedBscVpnInstName": hpnicfAclIPAclNamedBscVpnInstName,
       "hpnicfAclIPAclNamedBscComment": hpnicfAclIPAclNamedBscComment,
       "hpnicfAclIPAclNamedBscCounting": hpnicfAclIPAclNamedBscCounting,
       "hpnicfAclIPAclNamedBscRouteTypeAny": hpnicfAclIPAclNamedBscRouteTypeAny,
       "hpnicfAclIPAclNamedBscRouteTypeValue": hpnicfAclIPAclNamedBscRouteTypeValue,
       "hpnicfAclIPAclNamedAdvTable": hpnicfAclIPAclNamedAdvTable,
       "hpnicfAclIPAclNamedAdvEntry": hpnicfAclIPAclNamedAdvEntry,
       "hpnicfAclIPAclNamedAdvRowStatus": hpnicfAclIPAclNamedAdvRowStatus,
       "hpnicfAclIPAclNamedAdvAct": hpnicfAclIPAclNamedAdvAct,
       "hpnicfAclIPAclNamedAdvProtocol": hpnicfAclIPAclNamedAdvProtocol,
       "hpnicfAclIPAclNamedAdvAddrFlag": hpnicfAclIPAclNamedAdvAddrFlag,
       "hpnicfAclIPAclNamedAdvSrcAddrType": hpnicfAclIPAclNamedAdvSrcAddrType,
       "hpnicfAclIPAclNamedAdvSrcAddr": hpnicfAclIPAclNamedAdvSrcAddr,
       "hpnicfAclIPAclNamedAdvSrcPrefix": hpnicfAclIPAclNamedAdvSrcPrefix,
       "hpnicfAclIPAclNamedAdvSrcAny": hpnicfAclIPAclNamedAdvSrcAny,
       "hpnicfAclIPAclNamedAdvSrcWild": hpnicfAclIPAclNamedAdvSrcWild,
       "hpnicfAclIPAclNamedAdvSrcOp": hpnicfAclIPAclNamedAdvSrcOp,
       "hpnicfAclIPAclNamedAdvSrcPort1": hpnicfAclIPAclNamedAdvSrcPort1,
       "hpnicfAclIPAclNamedAdvSrcPort2": hpnicfAclIPAclNamedAdvSrcPort2,
       "hpnicfAclIPAclNamedAdvDstAddrType": hpnicfAclIPAclNamedAdvDstAddrType,
       "hpnicfAclIPAclNamedAdvDstAddr": hpnicfAclIPAclNamedAdvDstAddr,
       "hpnicfAclIPAclNamedAdvDstPrefix": hpnicfAclIPAclNamedAdvDstPrefix,
       "hpnicfAclIPAclNamedAdvDstAny": hpnicfAclIPAclNamedAdvDstAny,
       "hpnicfAclIPAclNamedAdvDstWild": hpnicfAclIPAclNamedAdvDstWild,
       "hpnicfAclIPAclNamedAdvDstOp": hpnicfAclIPAclNamedAdvDstOp,
       "hpnicfAclIPAclNamedAdvDstPort1": hpnicfAclIPAclNamedAdvDstPort1,
       "hpnicfAclIPAclNamedAdvDstPort2": hpnicfAclIPAclNamedAdvDstPort2,
       "hpnicfAclIPAclNamedAdvIcmpType": hpnicfAclIPAclNamedAdvIcmpType,
       "hpnicfAclIPAclNamedAdvIcmpCode": hpnicfAclIPAclNamedAdvIcmpCode,
       "hpnicfAclIPAclNamedAdvPrecedence": hpnicfAclIPAclNamedAdvPrecedence,
       "hpnicfAclIPAclNamedAdvTos": hpnicfAclIPAclNamedAdvTos,
       "hpnicfAclIPAclNamedAdvDscp": hpnicfAclIPAclNamedAdvDscp,
       "hpnicfAclIPAclNamedAdvTRangeName": hpnicfAclIPAclNamedAdvTRangeName,
       "hpnicfAclIPAclNamedAdvTCPFlag": hpnicfAclIPAclNamedAdvTCPFlag,
       "hpnicfAclIPAclNamedAdvFragmentFlag": hpnicfAclIPAclNamedAdvFragmentFlag,
       "hpnicfAclIPAclNamedAdvLog": hpnicfAclIPAclNamedAdvLog,
       "hpnicfAclIPAclNamedAdvCount": hpnicfAclIPAclNamedAdvCount,
       "hpnicfAclIPAclNamedAdvCountClear": hpnicfAclIPAclNamedAdvCountClear,
       "hpnicfAclIPAclNamedAdvEnable": hpnicfAclIPAclNamedAdvEnable,
       "hpnicfAclIPAclNamedAdvVpnInstName": hpnicfAclIPAclNamedAdvVpnInstName,
       "hpnicfAclIPAclNamedAdvComment": hpnicfAclIPAclNamedAdvComment,
       "hpnicfAclIPAclNamedAdvReflective": hpnicfAclIPAclNamedAdvReflective,
       "hpnicfAclIPAclNamedAdvCounting": hpnicfAclIPAclNamedAdvCounting,
       "hpnicfAclIPAclNamedAdvTCPFlagMask": hpnicfAclIPAclNamedAdvTCPFlagMask,
       "hpnicfAclIPAclNamedAdvTCPFlagValue": hpnicfAclIPAclNamedAdvTCPFlagValue,
       "hpnicfAclIPAclNamedAdvRouteTypeAny": hpnicfAclIPAclNamedAdvRouteTypeAny,
       "hpnicfAclIPAclNamedAdvRouteTypeValue": hpnicfAclIPAclNamedAdvRouteTypeValue,
       "hpnicfAclIPAclNamedAdvFlowLabel": hpnicfAclIPAclNamedAdvFlowLabel,
       "hpnicfAclIPAclNamedAdvSrcSuffix": hpnicfAclIPAclNamedAdvSrcSuffix,
       "hpnicfAclIPAclNamedAdvDstSuffix": hpnicfAclIPAclNamedAdvDstSuffix,
       "hpnicfAclMACAclGroup": hpnicfAclMACAclGroup,
       "hpnicfAclMACTable": hpnicfAclMACTable,
       "hpnicfAclMACEntry": hpnicfAclMACEntry,
       "hpnicfAclMACRuleIndex": hpnicfAclMACRuleIndex,
       "hpnicfAclMACRowStatus": hpnicfAclMACRowStatus,
       "hpnicfAclMACAct": hpnicfAclMACAct,
       "hpnicfAclMACTypeCode": hpnicfAclMACTypeCode,
       "hpnicfAclMACTypeMask": hpnicfAclMACTypeMask,
       "hpnicfAclMACSrcMac": hpnicfAclMACSrcMac,
       "hpnicfAclMACSrcMacWild": hpnicfAclMACSrcMacWild,
       "hpnicfAclMACDestMac": hpnicfAclMACDestMac,
       "hpnicfAclMACDestMacWild": hpnicfAclMACDestMacWild,
       "hpnicfAclMACLsapCode": hpnicfAclMACLsapCode,
       "hpnicfAclMACLsapMask": hpnicfAclMACLsapMask,
       "hpnicfAclMACCos": hpnicfAclMACCos,
       "hpnicfAclMACTimeRangeName": hpnicfAclMACTimeRangeName,
       "hpnicfAclMACCount": hpnicfAclMACCount,
       "hpnicfAclMACCountClear": hpnicfAclMACCountClear,
       "hpnicfAclMACEnable": hpnicfAclMACEnable,
       "hpnicfAclMACComment": hpnicfAclMACComment,
       "hpnicfAclMACLog": hpnicfAclMACLog,
       "hpnicfAclMACCounting": hpnicfAclMACCounting,
       "hpnicfAclNamedMACTable": hpnicfAclNamedMACTable,
       "hpnicfAclNamedMACEntry": hpnicfAclNamedMACEntry,
       "hpnicfAclNamedMACRowStatus": hpnicfAclNamedMACRowStatus,
       "hpnicfAclNamedMACAct": hpnicfAclNamedMACAct,
       "hpnicfAclNamedMACTypeCode": hpnicfAclNamedMACTypeCode,
       "hpnicfAclNamedMACTypeMask": hpnicfAclNamedMACTypeMask,
       "hpnicfAclNamedMACSrcMac": hpnicfAclNamedMACSrcMac,
       "hpnicfAclNamedMACSrcMacWild": hpnicfAclNamedMACSrcMacWild,
       "hpnicfAclNamedMACDstMac": hpnicfAclNamedMACDstMac,
       "hpnicfAclNamedMACDstMacWild": hpnicfAclNamedMACDstMacWild,
       "hpnicfAclNamedMACLsapCode": hpnicfAclNamedMACLsapCode,
       "hpnicfAclNamedMACLsapMask": hpnicfAclNamedMACLsapMask,
       "hpnicfAclNamedMACCos": hpnicfAclNamedMACCos,
       "hpnicfAclNamedMACTimeRangeName": hpnicfAclNamedMACTimeRangeName,
       "hpnicfAclNamedMACCount": hpnicfAclNamedMACCount,
       "hpnicfAclNamedMACCountClear": hpnicfAclNamedMACCountClear,
       "hpnicfAclNamedMACEnable": hpnicfAclNamedMACEnable,
       "hpnicfAclNamedMACComment": hpnicfAclNamedMACComment,
       "hpnicfAclNamedMACLog": hpnicfAclNamedMACLog,
       "hpnicfAclNamedMACCounting": hpnicfAclNamedMACCounting,
       "hpnicfAclEnUserAclGroup": hpnicfAclEnUserAclGroup,
       "hpnicfAclEnUserTable": hpnicfAclEnUserTable,
       "hpnicfAclEnUserEntry": hpnicfAclEnUserEntry,
       "hpnicfAclEnUserRuleIndex": hpnicfAclEnUserRuleIndex,
       "hpnicfAclEnUserRowStatus": hpnicfAclEnUserRowStatus,
       "hpnicfAclEnUserAct": hpnicfAclEnUserAct,
       "hpnicfAclEnUserStartString": hpnicfAclEnUserStartString,
       "hpnicfAclEnUserL2String": hpnicfAclEnUserL2String,
       "hpnicfAclEnUserMplsString": hpnicfAclEnUserMplsString,
       "hpnicfAclEnUserIPv4String": hpnicfAclEnUserIPv4String,
       "hpnicfAclEnUserIPv6String": hpnicfAclEnUserIPv6String,
       "hpnicfAclEnUserL4String": hpnicfAclEnUserL4String,
       "hpnicfAclEnUserL5String": hpnicfAclEnUserL5String,
       "hpnicfAclEnUserTimeRangeName": hpnicfAclEnUserTimeRangeName,
       "hpnicfAclEnUserCount": hpnicfAclEnUserCount,
       "hpnicfAclEnUserCountClear": hpnicfAclEnUserCountClear,
       "hpnicfAclEnUserEnable": hpnicfAclEnUserEnable,
       "hpnicfAclEnUserComment": hpnicfAclEnUserComment,
       "hpnicfAclEnUserLog": hpnicfAclEnUserLog,
       "hpnicfAclEnUserCounting": hpnicfAclEnUserCounting,
       "hpnicfAclNamedUserTable": hpnicfAclNamedUserTable,
       "hpnicfAclNamedUserEntry": hpnicfAclNamedUserEntry,
       "hpnicfAclNamedUserRowStatus": hpnicfAclNamedUserRowStatus,
       "hpnicfAclNamedUserAct": hpnicfAclNamedUserAct,
       "hpnicfAclNamedUserStartString": hpnicfAclNamedUserStartString,
       "hpnicfAclNamedUserL2String": hpnicfAclNamedUserL2String,
       "hpnicfAclNamedUserMplsString": hpnicfAclNamedUserMplsString,
       "hpnicfAclNamedUserIPv4String": hpnicfAclNamedUserIPv4String,
       "hpnicfAclNamedUserIPv6String": hpnicfAclNamedUserIPv6String,
       "hpnicfAclNamedUserL4String": hpnicfAclNamedUserL4String,
       "hpnicfAclNamedUserL5String": hpnicfAclNamedUserL5String,
       "hpnicfAclNamedUserTimeRangeName": hpnicfAclNamedUserTimeRangeName,
       "hpnicfAclNamedUserCount": hpnicfAclNamedUserCount,
       "hpnicfAclNamedUserCountClear": hpnicfAclNamedUserCountClear,
       "hpnicfAclNamedUserEnable": hpnicfAclNamedUserEnable,
       "hpnicfAclNamedUserComment": hpnicfAclNamedUserComment,
       "hpnicfAclNamedUserLog": hpnicfAclNamedUserLog,
       "hpnicfAclNamedUserCounting": hpnicfAclNamedUserCounting,
       "hpnicfAclResourceGroup": hpnicfAclResourceGroup,
       "hpnicfAclResourceUsageTable": hpnicfAclResourceUsageTable,
       "hpnicfAclResourceUsageEntry": hpnicfAclResourceUsageEntry,
       "hpnicfAclResourceChassis": hpnicfAclResourceChassis,
       "hpnicfAclResourceSlot": hpnicfAclResourceSlot,
       "hpnicfAclResourceChip": hpnicfAclResourceChip,
       "hpnicfAclResourceType": hpnicfAclResourceType,
       "hpnicfAclPortRange": hpnicfAclPortRange,
       "hpnicfAclResourceTotal": hpnicfAclResourceTotal,
       "hpnicfAclResourceReserved": hpnicfAclResourceReserved,
       "hpnicfAclResourceConfigured": hpnicfAclResourceConfigured,
       "hpnicfAclResourceUsagePercent": hpnicfAclResourceUsagePercent,
       "hpnicfAclResourceTypeDescription": hpnicfAclResourceTypeDescription,
       "hpnicfAclIntervalGroup": hpnicfAclIntervalGroup,
       "hpnicfAclIntervalTable": hpnicfAclIntervalTable,
       "hpnicfAclIntervalEntry": hpnicfAclIntervalEntry,
       "hpnicfAclIntervalType": hpnicfAclIntervalType,
       "hpnicfAclIntervalValue": hpnicfAclIntervalValue,
       "hpnicfAclIntervalRowStatus": hpnicfAclIntervalRowStatus,
       "hpnicfAclPacketFilterObjects": hpnicfAclPacketFilterObjects,
       "hpnicfPfilterScalarGroup": hpnicfPfilterScalarGroup,
       "hpnicfPfilterDefaultAction": hpnicfPfilterDefaultAction,
       "hpnicfPfilterProcessingStatus": hpnicfPfilterProcessingStatus,
       "hpnicfPfilterApplyTable": hpnicfPfilterApplyTable,
       "hpnicfPfilterApplyEntry": hpnicfPfilterApplyEntry,
       "hpnicfPfilterApplyObjType": hpnicfPfilterApplyObjType,
       "hpnicfPfilterApplyObjIndex": hpnicfPfilterApplyObjIndex,
       "hpnicfPfilterApplyDirection": hpnicfPfilterApplyDirection,
       "hpnicfPfilterApplyAclType": hpnicfPfilterApplyAclType,
       "hpnicfPfilterApplyAclIndex": hpnicfPfilterApplyAclIndex,
       "hpnicfPfilterApplyHardCount": hpnicfPfilterApplyHardCount,
       "hpnicfPfilterApplySequence": hpnicfPfilterApplySequence,
       "hpnicfPfilterApplyCountClear": hpnicfPfilterApplyCountClear,
       "hpnicfPfilterApplyRowStatus": hpnicfPfilterApplyRowStatus,
       "hpnicfPfilterAclGroupRunInfoTable": hpnicfPfilterAclGroupRunInfoTable,
       "hpnicfPfilterAclGroupRunInfoEntry": hpnicfPfilterAclGroupRunInfoEntry,
       "hpnicfPfilterRunApplyObjType": hpnicfPfilterRunApplyObjType,
       "hpnicfPfilterRunApplyObjIndex": hpnicfPfilterRunApplyObjIndex,
       "hpnicfPfilterRunApplyDirection": hpnicfPfilterRunApplyDirection,
       "hpnicfPfilterRunApplyAclType": hpnicfPfilterRunApplyAclType,
       "hpnicfPfilterRunApplyAclIndex": hpnicfPfilterRunApplyAclIndex,
       "hpnicfPfilterAclGroupStatus": hpnicfPfilterAclGroupStatus,
       "hpnicfPfilterAclGroupCountStatus": hpnicfPfilterAclGroupCountStatus,
       "hpnicfPfilterAclGroupPermitPkts": hpnicfPfilterAclGroupPermitPkts,
       "hpnicfPfilterAclGroupPermitBytes": hpnicfPfilterAclGroupPermitBytes,
       "hpnicfPfilterAclGroupDenyPkts": hpnicfPfilterAclGroupDenyPkts,
       "hpnicfPfilterAclGroupDenyBytes": hpnicfPfilterAclGroupDenyBytes,
       "hpnicfPfilterAclRuleRunInfoTable": hpnicfPfilterAclRuleRunInfoTable,
       "hpnicfPfilterAclRuleRunInfoEntry": hpnicfPfilterAclRuleRunInfoEntry,
       "hpnicfPfilterAclRuleIndex": hpnicfPfilterAclRuleIndex,
       "hpnicfPfilterAclRuleStatus": hpnicfPfilterAclRuleStatus,
       "hpnicfPfilterAclRuleCountStatus": hpnicfPfilterAclRuleCountStatus,
       "hpnicfPfilterAclRuleMatchPackets": hpnicfPfilterAclRuleMatchPackets,
       "hpnicfPfilterAclRuleMatchBytes": hpnicfPfilterAclRuleMatchBytes,
       "hpnicfPfilterStatisticSumTable": hpnicfPfilterStatisticSumTable,
       "hpnicfPfilterStatisticSumEntry": hpnicfPfilterStatisticSumEntry,
       "hpnicfPfilterSumDirection": hpnicfPfilterSumDirection,
       "hpnicfPfilterSumAclType": hpnicfPfilterSumAclType,
       "hpnicfPfilterSumAclIndex": hpnicfPfilterSumAclIndex,
       "hpnicfPfilterSumRuleIndex": hpnicfPfilterSumRuleIndex,
       "hpnicfPfilterSumRuleMatchPackets": hpnicfPfilterSumRuleMatchPackets,
       "hpnicfPfilterSumRuleMatchBytes": hpnicfPfilterSumRuleMatchBytes,
       "hpnicfPfilter2ApplyTable": hpnicfPfilter2ApplyTable,
       "hpnicfPfilter2ApplyEntry": hpnicfPfilter2ApplyEntry,
       "hpnicfPfilter2ApplyObjType": hpnicfPfilter2ApplyObjType,
       "hpnicfPfilter2ApplyObjIndex": hpnicfPfilter2ApplyObjIndex,
       "hpnicfPfilter2ApplyDirection": hpnicfPfilter2ApplyDirection,
       "hpnicfPfilter2ApplyAclType": hpnicfPfilter2ApplyAclType,
       "hpnicfPfilter2ApplyAclIndex": hpnicfPfilter2ApplyAclIndex,
       "hpnicfPfilter2ApplyHardCount": hpnicfPfilter2ApplyHardCount,
       "hpnicfPfilter2ApplySequence": hpnicfPfilter2ApplySequence,
       "hpnicfPfilter2ApplyCountClear": hpnicfPfilter2ApplyCountClear,
       "hpnicfPfilter2ApplyRowStatus": hpnicfPfilter2ApplyRowStatus,
       "hpnicfPfilter2AclGroupRunInfoTable": hpnicfPfilter2AclGroupRunInfoTable,
       "hpnicfPfilter2AclGroupRunInfoEntry": hpnicfPfilter2AclGroupRunInfoEntry,
       "hpnicfPfilter2RunApplyObjType": hpnicfPfilter2RunApplyObjType,
       "hpnicfPfilter2RunApplyObjIndex": hpnicfPfilter2RunApplyObjIndex,
       "hpnicfPfilter2RunApplyDirection": hpnicfPfilter2RunApplyDirection,
       "hpnicfPfilter2RunApplyAclType": hpnicfPfilter2RunApplyAclType,
       "hpnicfPfilter2RunApplyAclIndex": hpnicfPfilter2RunApplyAclIndex,
       "hpnicfPfilter2AclGroupStatus": hpnicfPfilter2AclGroupStatus,
       "hpnicfPfilter2AclGroupCountStatus": hpnicfPfilter2AclGroupCountStatus,
       "hpnicfPfilter2AclGroupPermitPkts": hpnicfPfilter2AclGroupPermitPkts,
       "hpnicfPfilter2AclGroupPermitBytes": hpnicfPfilter2AclGroupPermitBytes,
       "hpnicfPfilter2AclGroupDenyPkts": hpnicfPfilter2AclGroupDenyPkts,
       "hpnicfPfilter2AclGroupDenyBytes": hpnicfPfilter2AclGroupDenyBytes,
       "hpnicfPfilter2AclRuleRunInfoTable": hpnicfPfilter2AclRuleRunInfoTable,
       "hpnicfPfilter2AclRuleRunInfoEntry": hpnicfPfilter2AclRuleRunInfoEntry,
       "hpnicfPfilter2AclRuleIndex": hpnicfPfilter2AclRuleIndex,
       "hpnicfPfilter2AclRuleStatus": hpnicfPfilter2AclRuleStatus,
       "hpnicfPfilter2AclRuleCountStatus": hpnicfPfilter2AclRuleCountStatus,
       "hpnicfPfilter2AclRuleMatchPackets": hpnicfPfilter2AclRuleMatchPackets,
       "hpnicfPfilter2AclRuleMatchBytes": hpnicfPfilter2AclRuleMatchBytes,
       "hpnicfPfilter2StatisticSumTable": hpnicfPfilter2StatisticSumTable,
       "hpnicfPfilter2StatisticSumEntry": hpnicfPfilter2StatisticSumEntry,
       "hpnicfPfilter2SumDirection": hpnicfPfilter2SumDirection,
       "hpnicfPfilter2SumAclType": hpnicfPfilter2SumAclType,
       "hpnicfPfilter2SumAclIndex": hpnicfPfilter2SumAclIndex,
       "hpnicfPfilter2SumRuleIndex": hpnicfPfilter2SumRuleIndex,
       "hpnicfPfilter2SumRuleMatchPackets": hpnicfPfilter2SumRuleMatchPackets,
       "hpnicfPfilter2SumRuleMatchBytes": hpnicfPfilter2SumRuleMatchBytes,
       "hpnicfAclPacketfilterTrapObjects": hpnicfAclPacketfilterTrapObjects,
       "hpnicfPfilterInterface": hpnicfPfilterInterface,
       "hpnicfPfilterDirection": hpnicfPfilterDirection,
       "hpnicfPfilterACLNumber": hpnicfPfilterACLNumber,
       "hpnicfPfilterAction": hpnicfPfilterAction,
       "hpnicfMACfilterSourceMac": hpnicfMACfilterSourceMac,
       "hpnicfMACfilterDestinationMac": hpnicfMACfilterDestinationMac,
       "hpnicfPfilterPacketNumber": hpnicfPfilterPacketNumber,
       "hpnicfPfilterReceiveInterface": hpnicfPfilterReceiveInterface,
       "hpnicfAclPacketIfName": hpnicfAclPacketIfName,
       "hpnicfAclPacketDirection": hpnicfAclPacketDirection,
       "hpnicfAclPacketBAGG": hpnicfAclPacketBAGG,
       "hpnicfAclPacketVlanID": hpnicfAclPacketVlanID,
       "hpnicfAclPacketSrcIP": hpnicfAclPacketSrcIP,
       "hpnicfAclPacketDstIP": hpnicfAclPacketDstIP,
       "hpnicfAclPacketProtocol": hpnicfAclPacketProtocol,
       "hpnicfAclPacketDscp": hpnicfAclPacketDscp,
       "hpnicfAclPacketFlowLabel": hpnicfAclPacketFlowLabel,
       "hpnicfAclPacketIcmpIgmpType": hpnicfAclPacketIcmpIgmpType,
       "hpnicfAclPacketIcmpIgmpCode": hpnicfAclPacketIcmpIgmpCode,
       "hpnicfAclPacketTcpFlags": hpnicfAclPacketTcpFlags,
       "hpnicfAclPacketSrcPort": hpnicfAclPacketSrcPort,
       "hpnicfAclPacketDstPort": hpnicfAclPacketDstPort,
       "hpnicfAclPacketSrcMacAddr": hpnicfAclPacketSrcMacAddr,
       "hpnicfAclPacketDstMacAddr": hpnicfAclPacketDstMacAddr,
       "hpnicfAclPacketMacTypeLen": hpnicfAclPacketMacTypeLen,
       "hpnicfAclPacketVlanPCP": hpnicfAclPacketVlanPCP,
       "hpnicfAclPacketfilterTrap": hpnicfAclPacketfilterTrap,
       "hpnicfPfilterTrapPrefix": hpnicfPfilterTrapPrefix,
       "hpnicfMACfilterTrap": hpnicfMACfilterTrap,
       "hpnicfAclRuleMatchCount": hpnicfAclRuleMatchCount,
       "hpnicfAclFirstIPv4PktCaptured": hpnicfAclFirstIPv4PktCaptured,
       "hpnicfAclFirstIPv6PktCaptured": hpnicfAclFirstIPv6PktCaptured,
       "hpnicfAclFirstEthernetPktCaptured": hpnicfAclFirstEthernetPktCaptured}
)
