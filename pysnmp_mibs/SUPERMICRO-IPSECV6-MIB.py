# SNMP MIB module (SUPERMICRO-IPSECV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-IPSECV6-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:10 2025
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
 enterprises,
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
    "enterprises",
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

fsipv6Sec = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29)
)
if mibBuilder.loadTexts:
    fsipv6Sec.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Ipv6IfIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_Fsipv6SecScalars_ObjectIdentity = ObjectIdentity
fsipv6SecScalars = _Fsipv6SecScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 1)
)


class _Fsipv6SecGlobalStatus_Type(Integer32):
    """Custom type fsipv6SecGlobalStatus based on Integer32"""
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


_Fsipv6SecGlobalStatus_Type.__name__ = "Integer32"
_Fsipv6SecGlobalStatus_Object = MibScalar
fsipv6SecGlobalStatus = _Fsipv6SecGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 1, 1),
    _Fsipv6SecGlobalStatus_Type()
)
fsipv6SecGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecGlobalStatus.setStatus("current")
_Fsipv6SecVersion_Type = Counter32
_Fsipv6SecVersion_Object = MibScalar
fsipv6SecVersion = _Fsipv6SecVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 1, 2),
    _Fsipv6SecVersion_Type()
)
fsipv6SecVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecVersion.setStatus("current")


class _Fsipv6SecGlobalDebug_Type(Integer32):
    """Custom type fsipv6SecGlobalDebug based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disableall", 0),
          ("enableall", 1),
          ("initshut", 2),
          ("manageMent", 3),
          ("dataPath", 4),
          ("ctrlPath", 5),
          ("pktDump", 6),
          ("osresource", 7),
          ("allfailure", 8),
          ("buffer", 9))
    )


_Fsipv6SecGlobalDebug_Type.__name__ = "Integer32"
_Fsipv6SecGlobalDebug_Object = MibScalar
fsipv6SecGlobalDebug = _Fsipv6SecGlobalDebug_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 1, 3),
    _Fsipv6SecGlobalDebug_Type()
)
fsipv6SecGlobalDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecGlobalDebug.setStatus("current")


class _Fsipv6SecMaxSA_Type(Integer32):
    """Custom type fsipv6SecMaxSA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsipv6SecMaxSA_Type.__name__ = "Integer32"
_Fsipv6SecMaxSA_Object = MibScalar
fsipv6SecMaxSA = _Fsipv6SecMaxSA_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 1, 4),
    _Fsipv6SecMaxSA_Type()
)
fsipv6SecMaxSA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecMaxSA.setStatus("deprecated")
_Fsipv6SecConfig_ObjectIdentity = ObjectIdentity
fsipv6SecConfig = _Fsipv6SecConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2)
)
_Fsipv6SecSelectorTable_Object = MibTable
fsipv6SecSelectorTable = _Fsipv6SecSelectorTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 1)
)
if mibBuilder.loadTexts:
    fsipv6SecSelectorTable.setStatus("current")
_FsIpv6SecSelectorEntry_Object = MibTableRow
fsIpv6SecSelectorEntry = _FsIpv6SecSelectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 1, 1)
)
fsIpv6SecSelectorEntry.setIndexNames(
    (0, "SUPERMICRO-IPSECV6-MIB", "fsipv6SelIfIndex"),
    (0, "SUPERMICRO-IPSECV6-MIB", "fsipv6SelProtoIndex"),
    (0, "SUPERMICRO-IPSECV6-MIB", "fsipv6SelAccessIndex"),
    (0, "SUPERMICRO-IPSECV6-MIB", "fsipv6SelPort"),
    (0, "SUPERMICRO-IPSECV6-MIB", "fsipv6SelPktDirection"),
)
if mibBuilder.loadTexts:
    fsIpv6SecSelectorEntry.setStatus("current")


class _Fsipv6SelIfIndex_Type(Integer32):
    """Custom type fsipv6SelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsipv6SelIfIndex_Type.__name__ = "Integer32"
_Fsipv6SelIfIndex_Object = MibTableColumn
fsipv6SelIfIndex = _Fsipv6SelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 1, 1, 1),
    _Fsipv6SelIfIndex_Type()
)
fsipv6SelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsipv6SelIfIndex.setStatus("current")


class _Fsipv6SelProtoIndex_Type(Integer32):
    """Custom type fsipv6SelProtoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17,
              50,
              51,
              58,
              9000)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17),
          ("espproto", 50),
          ("ahproto", 51),
          ("icmpv6", 58),
          ("any", 9000))
    )


_Fsipv6SelProtoIndex_Type.__name__ = "Integer32"
_Fsipv6SelProtoIndex_Object = MibTableColumn
fsipv6SelProtoIndex = _Fsipv6SelProtoIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 1, 1, 2),
    _Fsipv6SelProtoIndex_Type()
)
fsipv6SelProtoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsipv6SelProtoIndex.setStatus("current")


class _Fsipv6SelAccessIndex_Type(Integer32):
    """Custom type fsipv6SelAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsipv6SelAccessIndex_Type.__name__ = "Integer32"
_Fsipv6SelAccessIndex_Object = MibTableColumn
fsipv6SelAccessIndex = _Fsipv6SelAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 1, 1, 3),
    _Fsipv6SelAccessIndex_Type()
)
fsipv6SelAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsipv6SelAccessIndex.setStatus("current")


class _Fsipv6SelPort_Type(Integer32):
    """Custom type fsipv6SelPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsipv6SelPort_Type.__name__ = "Integer32"
_Fsipv6SelPort_Object = MibTableColumn
fsipv6SelPort = _Fsipv6SelPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 1, 1, 4),
    _Fsipv6SelPort_Type()
)
fsipv6SelPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsipv6SelPort.setStatus("current")


class _Fsipv6SelPktDirection_Type(Integer32):
    """Custom type fsipv6SelPktDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2),
          ("any", 3))
    )


_Fsipv6SelPktDirection_Type.__name__ = "Integer32"
_Fsipv6SelPktDirection_Object = MibTableColumn
fsipv6SelPktDirection = _Fsipv6SelPktDirection_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 1, 1, 5),
    _Fsipv6SelPktDirection_Type()
)
fsipv6SelPktDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsipv6SelPktDirection.setStatus("current")


class _Fsipv6SelFilterFlag_Type(Integer32):
    """Custom type fsipv6SelFilterFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("allow", 2))
    )


_Fsipv6SelFilterFlag_Type.__name__ = "Integer32"
_Fsipv6SelFilterFlag_Object = MibTableColumn
fsipv6SelFilterFlag = _Fsipv6SelFilterFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 1, 1, 6),
    _Fsipv6SelFilterFlag_Type()
)
fsipv6SelFilterFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SelFilterFlag.setStatus("current")


class _Fsipv6SelPolicyIndex_Type(Integer32):
    """Custom type fsipv6SelPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsipv6SelPolicyIndex_Type.__name__ = "Integer32"
_Fsipv6SelPolicyIndex_Object = MibTableColumn
fsipv6SelPolicyIndex = _Fsipv6SelPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 1, 1, 7),
    _Fsipv6SelPolicyIndex_Type()
)
fsipv6SelPolicyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SelPolicyIndex.setStatus("current")


class _Fsipv6SelIfIpAddress_Type(OctetString):
    """Custom type fsipv6SelIfIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fsipv6SelIfIpAddress_Type.__name__ = "OctetString"
_Fsipv6SelIfIpAddress_Object = MibTableColumn
fsipv6SelIfIpAddress = _Fsipv6SelIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 1, 1, 8),
    _Fsipv6SelIfIpAddress_Type()
)
fsipv6SelIfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SelIfIpAddress.setStatus("current")
_Fsipv6SelStatus_Type = RowStatus
_Fsipv6SelStatus_Object = MibTableColumn
fsipv6SelStatus = _Fsipv6SelStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 1, 1, 9),
    _Fsipv6SelStatus_Type()
)
fsipv6SelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsipv6SelStatus.setStatus("current")
_Fsipv6SecAccessTable_Object = MibTable
fsipv6SecAccessTable = _Fsipv6SecAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 2)
)
if mibBuilder.loadTexts:
    fsipv6SecAccessTable.setStatus("current")
_FsIpv6SecAccessEntry_Object = MibTableRow
fsIpv6SecAccessEntry = _FsIpv6SecAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 2, 1)
)
fsIpv6SecAccessEntry.setIndexNames(
    (0, "SUPERMICRO-IPSECV6-MIB", "fsipv6SecAccessIndex"),
)
if mibBuilder.loadTexts:
    fsIpv6SecAccessEntry.setStatus("current")


class _Fsipv6SecAccessIndex_Type(Integer32):
    """Custom type fsipv6SecAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsipv6SecAccessIndex_Type.__name__ = "Integer32"
_Fsipv6SecAccessIndex_Object = MibTableColumn
fsipv6SecAccessIndex = _Fsipv6SecAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 2, 1, 1),
    _Fsipv6SecAccessIndex_Type()
)
fsipv6SecAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsipv6SecAccessIndex.setStatus("current")
_Fsipv6SecAccessStatus_Type = RowStatus
_Fsipv6SecAccessStatus_Object = MibTableColumn
fsipv6SecAccessStatus = _Fsipv6SecAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 2, 1, 2),
    _Fsipv6SecAccessStatus_Type()
)
fsipv6SecAccessStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsipv6SecAccessStatus.setStatus("current")


class _Fsipv6SecSrcNet_Type(OctetString):
    """Custom type fsipv6SecSrcNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fsipv6SecSrcNet_Type.__name__ = "OctetString"
_Fsipv6SecSrcNet_Object = MibTableColumn
fsipv6SecSrcNet = _Fsipv6SecSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 2, 1, 3),
    _Fsipv6SecSrcNet_Type()
)
fsipv6SecSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecSrcNet.setStatus("current")


class _Fsipv6SecSrcAddrPrefixLen_Type(Integer32):
    """Custom type fsipv6SecSrcAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Fsipv6SecSrcAddrPrefixLen_Type.__name__ = "Integer32"
_Fsipv6SecSrcAddrPrefixLen_Object = MibTableColumn
fsipv6SecSrcAddrPrefixLen = _Fsipv6SecSrcAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 2, 1, 4),
    _Fsipv6SecSrcAddrPrefixLen_Type()
)
fsipv6SecSrcAddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecSrcAddrPrefixLen.setStatus("current")


class _Fsipv6SecDestNet_Type(OctetString):
    """Custom type fsipv6SecDestNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fsipv6SecDestNet_Type.__name__ = "OctetString"
_Fsipv6SecDestNet_Object = MibTableColumn
fsipv6SecDestNet = _Fsipv6SecDestNet_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 2, 1, 5),
    _Fsipv6SecDestNet_Type()
)
fsipv6SecDestNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecDestNet.setStatus("current")


class _Fsipv6SecDestAddrPrefixLen_Type(Integer32):
    """Custom type fsipv6SecDestAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Fsipv6SecDestAddrPrefixLen_Type.__name__ = "Integer32"
_Fsipv6SecDestAddrPrefixLen_Object = MibTableColumn
fsipv6SecDestAddrPrefixLen = _Fsipv6SecDestAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 2, 1, 6),
    _Fsipv6SecDestAddrPrefixLen_Type()
)
fsipv6SecDestAddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecDestAddrPrefixLen.setStatus("current")
_Fsipv6SecPolicyTable_Object = MibTable
fsipv6SecPolicyTable = _Fsipv6SecPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 3)
)
if mibBuilder.loadTexts:
    fsipv6SecPolicyTable.setStatus("current")
_FsIpv6SecPolicyEntry_Object = MibTableRow
fsIpv6SecPolicyEntry = _FsIpv6SecPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 3, 1)
)
fsIpv6SecPolicyEntry.setIndexNames(
    (0, "SUPERMICRO-IPSECV6-MIB", "fsipv6SecPolicyIndex"),
)
if mibBuilder.loadTexts:
    fsIpv6SecPolicyEntry.setStatus("current")


class _Fsipv6SecPolicyIndex_Type(Integer32):
    """Custom type fsipv6SecPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsipv6SecPolicyIndex_Type.__name__ = "Integer32"
_Fsipv6SecPolicyIndex_Object = MibTableColumn
fsipv6SecPolicyIndex = _Fsipv6SecPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 3, 1, 1),
    _Fsipv6SecPolicyIndex_Type()
)
fsipv6SecPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsipv6SecPolicyIndex.setStatus("current")


class _Fsipv6SecPolicyFlag_Type(Integer32):
    """Custom type fsipv6SecPolicyFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("apply", 3),
          ("bypass", 4))
    )


_Fsipv6SecPolicyFlag_Type.__name__ = "Integer32"
_Fsipv6SecPolicyFlag_Object = MibTableColumn
fsipv6SecPolicyFlag = _Fsipv6SecPolicyFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 3, 1, 2),
    _Fsipv6SecPolicyFlag_Type()
)
fsipv6SecPolicyFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecPolicyFlag.setStatus("current")


class _Fsipv6SecPolicyMode_Type(Integer32):
    """Custom type fsipv6SecPolicyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("automatic", 2))
    )


_Fsipv6SecPolicyMode_Type.__name__ = "Integer32"
_Fsipv6SecPolicyMode_Object = MibTableColumn
fsipv6SecPolicyMode = _Fsipv6SecPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 3, 1, 3),
    _Fsipv6SecPolicyMode_Type()
)
fsipv6SecPolicyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecPolicyMode.setStatus("current")
_Fsipv6SecPolicySaBundle_Type = DisplayString
_Fsipv6SecPolicySaBundle_Object = MibTableColumn
fsipv6SecPolicySaBundle = _Fsipv6SecPolicySaBundle_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 3, 1, 4),
    _Fsipv6SecPolicySaBundle_Type()
)
fsipv6SecPolicySaBundle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecPolicySaBundle.setStatus("current")


class _Fsipv6SecPolicyOptionsIndex_Type(Integer32):
    """Custom type fsipv6SecPolicyOptionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsipv6SecPolicyOptionsIndex_Type.__name__ = "Integer32"
_Fsipv6SecPolicyOptionsIndex_Object = MibTableColumn
fsipv6SecPolicyOptionsIndex = _Fsipv6SecPolicyOptionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 3, 1, 5),
    _Fsipv6SecPolicyOptionsIndex_Type()
)
fsipv6SecPolicyOptionsIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecPolicyOptionsIndex.setStatus("current")
_Fsipv6SecPolicyStatus_Type = RowStatus
_Fsipv6SecPolicyStatus_Object = MibTableColumn
fsipv6SecPolicyStatus = _Fsipv6SecPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 3, 1, 6),
    _Fsipv6SecPolicyStatus_Type()
)
fsipv6SecPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsipv6SecPolicyStatus.setStatus("current")
_Fsipv6SecAssocTable_Object = MibTable
fsipv6SecAssocTable = _Fsipv6SecAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 4)
)
if mibBuilder.loadTexts:
    fsipv6SecAssocTable.setStatus("current")
_Fsipv6SecAssocEntry_Object = MibTableRow
fsipv6SecAssocEntry = _Fsipv6SecAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 4, 1)
)
fsipv6SecAssocEntry.setIndexNames(
    (0, "SUPERMICRO-IPSECV6-MIB", "fsipv6SecAssocIndex"),
)
if mibBuilder.loadTexts:
    fsipv6SecAssocEntry.setStatus("current")


class _Fsipv6SecAssocIndex_Type(Integer32):
    """Custom type fsipv6SecAssocIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsipv6SecAssocIndex_Type.__name__ = "Integer32"
_Fsipv6SecAssocIndex_Object = MibTableColumn
fsipv6SecAssocIndex = _Fsipv6SecAssocIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 4, 1, 1),
    _Fsipv6SecAssocIndex_Type()
)
fsipv6SecAssocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsipv6SecAssocIndex.setStatus("current")


class _Fsipv6SecAssocDstAddr_Type(OctetString):
    """Custom type fsipv6SecAssocDstAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fsipv6SecAssocDstAddr_Type.__name__ = "OctetString"
_Fsipv6SecAssocDstAddr_Object = MibTableColumn
fsipv6SecAssocDstAddr = _Fsipv6SecAssocDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 4, 1, 2),
    _Fsipv6SecAssocDstAddr_Type()
)
fsipv6SecAssocDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecAssocDstAddr.setStatus("current")


class _Fsipv6SecAssocProtocol_Type(Integer32):
    """Custom type fsipv6SecAssocProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              51)
        )
    )
    namedValues = NamedValues(
        *(("espproto", 50),
          ("ahproto", 51))
    )


_Fsipv6SecAssocProtocol_Type.__name__ = "Integer32"
_Fsipv6SecAssocProtocol_Object = MibTableColumn
fsipv6SecAssocProtocol = _Fsipv6SecAssocProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 4, 1, 3),
    _Fsipv6SecAssocProtocol_Type()
)
fsipv6SecAssocProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecAssocProtocol.setStatus("current")


class _Fsipv6SecAssocSpi_Type(Integer32):
    """Custom type fsipv6SecAssocSpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2147483647),
    )


_Fsipv6SecAssocSpi_Type.__name__ = "Integer32"
_Fsipv6SecAssocSpi_Object = MibTableColumn
fsipv6SecAssocSpi = _Fsipv6SecAssocSpi_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 4, 1, 4),
    _Fsipv6SecAssocSpi_Type()
)
fsipv6SecAssocSpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecAssocSpi.setStatus("current")


class _Fsipv6SecAssocMode_Type(Integer32):
    """Custom type fsipv6SecAssocMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tunnel", 1),
          ("transport", 2))
    )


_Fsipv6SecAssocMode_Type.__name__ = "Integer32"
_Fsipv6SecAssocMode_Object = MibTableColumn
fsipv6SecAssocMode = _Fsipv6SecAssocMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 4, 1, 5),
    _Fsipv6SecAssocMode_Type()
)
fsipv6SecAssocMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecAssocMode.setStatus("current")


class _Fsipv6SecAssocAhAlgo_Type(Integer32):
    """Custom type fsipv6SecAssocAhAlgo based on Integer32"""
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
        *(("null", 0),
          ("hmacmd5", 1),
          ("hmacsha1", 2),
          ("keyedmd5", 3),
          ("md5", 4))
    )


_Fsipv6SecAssocAhAlgo_Type.__name__ = "Integer32"
_Fsipv6SecAssocAhAlgo_Object = MibTableColumn
fsipv6SecAssocAhAlgo = _Fsipv6SecAssocAhAlgo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 4, 1, 6),
    _Fsipv6SecAssocAhAlgo_Type()
)
fsipv6SecAssocAhAlgo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecAssocAhAlgo.setStatus("current")


class _Fsipv6SecAssocAhKey_Type(OctetString):
    """Custom type fsipv6SecAssocAhKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Fsipv6SecAssocAhKey_Type.__name__ = "OctetString"
_Fsipv6SecAssocAhKey_Object = MibTableColumn
fsipv6SecAssocAhKey = _Fsipv6SecAssocAhKey_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 4, 1, 7),
    _Fsipv6SecAssocAhKey_Type()
)
fsipv6SecAssocAhKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecAssocAhKey.setStatus("current")


class _Fsipv6SecAssocEspAlgo_Type(Integer32):
    """Custom type fsipv6SecAssocEspAlgo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("descbc", 2),
          ("threedescbc", 3),
          ("null", 11),
          ("aes", 12))
    )


_Fsipv6SecAssocEspAlgo_Type.__name__ = "Integer32"
_Fsipv6SecAssocEspAlgo_Object = MibTableColumn
fsipv6SecAssocEspAlgo = _Fsipv6SecAssocEspAlgo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 4, 1, 8),
    _Fsipv6SecAssocEspAlgo_Type()
)
fsipv6SecAssocEspAlgo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecAssocEspAlgo.setStatus("current")


class _Fsipv6SecAssocEspKey_Type(OctetString):
    """Custom type fsipv6SecAssocEspKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Fsipv6SecAssocEspKey_Type.__name__ = "OctetString"
_Fsipv6SecAssocEspKey_Object = MibTableColumn
fsipv6SecAssocEspKey = _Fsipv6SecAssocEspKey_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 4, 1, 9),
    _Fsipv6SecAssocEspKey_Type()
)
fsipv6SecAssocEspKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecAssocEspKey.setStatus("current")


class _Fsipv6SecAssocEspKey2_Type(OctetString):
    """Custom type fsipv6SecAssocEspKey2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Fsipv6SecAssocEspKey2_Type.__name__ = "OctetString"
_Fsipv6SecAssocEspKey2_Object = MibTableColumn
fsipv6SecAssocEspKey2 = _Fsipv6SecAssocEspKey2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 4, 1, 10),
    _Fsipv6SecAssocEspKey2_Type()
)
fsipv6SecAssocEspKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecAssocEspKey2.setStatus("current")


class _Fsipv6SecAssocEspKey3_Type(OctetString):
    """Custom type fsipv6SecAssocEspKey3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Fsipv6SecAssocEspKey3_Type.__name__ = "OctetString"
_Fsipv6SecAssocEspKey3_Object = MibTableColumn
fsipv6SecAssocEspKey3 = _Fsipv6SecAssocEspKey3_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 4, 1, 11),
    _Fsipv6SecAssocEspKey3_Type()
)
fsipv6SecAssocEspKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecAssocEspKey3.setStatus("current")


class _Fsipv6SecAssocLifetimeInBytes_Type(Integer32):
    """Custom type fsipv6SecAssocLifetimeInBytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Fsipv6SecAssocLifetimeInBytes_Type.__name__ = "Integer32"
_Fsipv6SecAssocLifetimeInBytes_Object = MibTableColumn
fsipv6SecAssocLifetimeInBytes = _Fsipv6SecAssocLifetimeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 4, 1, 12),
    _Fsipv6SecAssocLifetimeInBytes_Type()
)
fsipv6SecAssocLifetimeInBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecAssocLifetimeInBytes.setStatus("current")


class _Fsipv6SecAssocLifetime_Type(Integer32):
    """Custom type fsipv6SecAssocLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(300, 2592000),
    )


_Fsipv6SecAssocLifetime_Type.__name__ = "Integer32"
_Fsipv6SecAssocLifetime_Object = MibTableColumn
fsipv6SecAssocLifetime = _Fsipv6SecAssocLifetime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 4, 1, 13),
    _Fsipv6SecAssocLifetime_Type()
)
fsipv6SecAssocLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecAssocLifetime.setStatus("current")


class _Fsipv6SecAssocAntiReplay_Type(Integer32):
    """Custom type fsipv6SecAssocAntiReplay based on Integer32"""
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


_Fsipv6SecAssocAntiReplay_Type.__name__ = "Integer32"
_Fsipv6SecAssocAntiReplay_Object = MibTableColumn
fsipv6SecAssocAntiReplay = _Fsipv6SecAssocAntiReplay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 4, 1, 14),
    _Fsipv6SecAssocAntiReplay_Type()
)
fsipv6SecAssocAntiReplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsipv6SecAssocAntiReplay.setStatus("current")
_Fsipv6SecAssocStatus_Type = RowStatus
_Fsipv6SecAssocStatus_Object = MibTableColumn
fsipv6SecAssocStatus = _Fsipv6SecAssocStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 2, 4, 1, 15),
    _Fsipv6SecAssocStatus_Type()
)
fsipv6SecAssocStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsipv6SecAssocStatus.setStatus("current")
_Fsipv6SecStats_ObjectIdentity = ObjectIdentity
fsipv6SecStats = _Fsipv6SecStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3)
)
_Fsipv6SecIfStatsTable_Object = MibTable
fsipv6SecIfStatsTable = _Fsipv6SecIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 1)
)
if mibBuilder.loadTexts:
    fsipv6SecIfStatsTable.setStatus("current")
_FsIpv6SecIfStatsEntry_Object = MibTableRow
fsIpv6SecIfStatsEntry = _FsIpv6SecIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 1, 1)
)
fsIpv6SecIfStatsEntry.setIndexNames(
    (0, "SUPERMICRO-IPSECV6-MIB", "fsipv6SecIfIndex"),
)
if mibBuilder.loadTexts:
    fsIpv6SecIfStatsEntry.setStatus("current")


class _Fsipv6SecIfIndex_Type(Integer32):
    """Custom type fsipv6SecIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Fsipv6SecIfIndex_Type.__name__ = "Integer32"
_Fsipv6SecIfIndex_Object = MibTableColumn
fsipv6SecIfIndex = _Fsipv6SecIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 1, 1, 1),
    _Fsipv6SecIfIndex_Type()
)
fsipv6SecIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsipv6SecIfIndex.setStatus("current")
_Fsipv6SecIfInPkts_Type = Counter32
_Fsipv6SecIfInPkts_Object = MibTableColumn
fsipv6SecIfInPkts = _Fsipv6SecIfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 1, 1, 2),
    _Fsipv6SecIfInPkts_Type()
)
fsipv6SecIfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecIfInPkts.setStatus("current")
_Fsipv6SecIfOutPkts_Type = Counter32
_Fsipv6SecIfOutPkts_Object = MibTableColumn
fsipv6SecIfOutPkts = _Fsipv6SecIfOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 1, 1, 3),
    _Fsipv6SecIfOutPkts_Type()
)
fsipv6SecIfOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecIfOutPkts.setStatus("current")
_Fsipv6SecIfPktsApply_Type = Counter32
_Fsipv6SecIfPktsApply_Object = MibTableColumn
fsipv6SecIfPktsApply = _Fsipv6SecIfPktsApply_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 1, 1, 4),
    _Fsipv6SecIfPktsApply_Type()
)
fsipv6SecIfPktsApply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecIfPktsApply.setStatus("current")
_Fsipv6SecIfPktsDiscard_Type = Counter32
_Fsipv6SecIfPktsDiscard_Object = MibTableColumn
fsipv6SecIfPktsDiscard = _Fsipv6SecIfPktsDiscard_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 1, 1, 5),
    _Fsipv6SecIfPktsDiscard_Type()
)
fsipv6SecIfPktsDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecIfPktsDiscard.setStatus("current")
_Fsipv6SecIfPktsBypass_Type = Counter32
_Fsipv6SecIfPktsBypass_Object = MibTableColumn
fsipv6SecIfPktsBypass = _Fsipv6SecIfPktsBypass_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 1, 1, 6),
    _Fsipv6SecIfPktsBypass_Type()
)
fsipv6SecIfPktsBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecIfPktsBypass.setStatus("current")
_Fsipv6SecAhEspStatsTable_Object = MibTable
fsipv6SecAhEspStatsTable = _Fsipv6SecAhEspStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 2)
)
if mibBuilder.loadTexts:
    fsipv6SecAhEspStatsTable.setStatus("current")
_FsIpv6SecAhEspStatsEntry_Object = MibTableRow
fsIpv6SecAhEspStatsEntry = _FsIpv6SecAhEspStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 2, 1)
)
fsIpv6SecAhEspStatsEntry.setIndexNames(
    (0, "SUPERMICRO-IPSECV6-MIB", "fsipv6SecAhEspIfIndex"),
)
if mibBuilder.loadTexts:
    fsIpv6SecAhEspStatsEntry.setStatus("current")


class _Fsipv6SecAhEspIfIndex_Type(Integer32):
    """Custom type fsipv6SecAhEspIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Fsipv6SecAhEspIfIndex_Type.__name__ = "Integer32"
_Fsipv6SecAhEspIfIndex_Object = MibTableColumn
fsipv6SecAhEspIfIndex = _Fsipv6SecAhEspIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 2, 1, 1),
    _Fsipv6SecAhEspIfIndex_Type()
)
fsipv6SecAhEspIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsipv6SecAhEspIfIndex.setStatus("current")
_Fsipv6SecInAhPkts_Type = Counter32
_Fsipv6SecInAhPkts_Object = MibTableColumn
fsipv6SecInAhPkts = _Fsipv6SecInAhPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 2, 1, 2),
    _Fsipv6SecInAhPkts_Type()
)
fsipv6SecInAhPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecInAhPkts.setStatus("current")
_Fsipv6SecOutAhPkts_Type = Counter32
_Fsipv6SecOutAhPkts_Object = MibTableColumn
fsipv6SecOutAhPkts = _Fsipv6SecOutAhPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 2, 1, 3),
    _Fsipv6SecOutAhPkts_Type()
)
fsipv6SecOutAhPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecOutAhPkts.setStatus("current")
_Fsipv6SecAhPktsAllow_Type = Counter32
_Fsipv6SecAhPktsAllow_Object = MibTableColumn
fsipv6SecAhPktsAllow = _Fsipv6SecAhPktsAllow_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 2, 1, 4),
    _Fsipv6SecAhPktsAllow_Type()
)
fsipv6SecAhPktsAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecAhPktsAllow.setStatus("current")
_Fsipv6SecAhPktsDiscard_Type = Counter32
_Fsipv6SecAhPktsDiscard_Object = MibTableColumn
fsipv6SecAhPktsDiscard = _Fsipv6SecAhPktsDiscard_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 2, 1, 5),
    _Fsipv6SecAhPktsDiscard_Type()
)
fsipv6SecAhPktsDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecAhPktsDiscard.setStatus("current")
_Fsipv6SecInEspPkts_Type = Counter32
_Fsipv6SecInEspPkts_Object = MibTableColumn
fsipv6SecInEspPkts = _Fsipv6SecInEspPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 2, 1, 6),
    _Fsipv6SecInEspPkts_Type()
)
fsipv6SecInEspPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecInEspPkts.setStatus("current")
_Fsipv6SecOutEspPkts_Type = Counter32
_Fsipv6SecOutEspPkts_Object = MibTableColumn
fsipv6SecOutEspPkts = _Fsipv6SecOutEspPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 2, 1, 7),
    _Fsipv6SecOutEspPkts_Type()
)
fsipv6SecOutEspPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecOutEspPkts.setStatus("current")
_Fsipv6SecEspPktsAllow_Type = Counter32
_Fsipv6SecEspPktsAllow_Object = MibTableColumn
fsipv6SecEspPktsAllow = _Fsipv6SecEspPktsAllow_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 2, 1, 8),
    _Fsipv6SecEspPktsAllow_Type()
)
fsipv6SecEspPktsAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecEspPktsAllow.setStatus("current")
_Fsipv6SecEspPktsDiscard_Type = Counter32
_Fsipv6SecEspPktsDiscard_Object = MibTableColumn
fsipv6SecEspPktsDiscard = _Fsipv6SecEspPktsDiscard_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 2, 1, 9),
    _Fsipv6SecEspPktsDiscard_Type()
)
fsipv6SecEspPktsDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecEspPktsDiscard.setStatus("current")
_Fsipv6SecAhEspIntruTable_Object = MibTable
fsipv6SecAhEspIntruTable = _Fsipv6SecAhEspIntruTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 3)
)
if mibBuilder.loadTexts:
    fsipv6SecAhEspIntruTable.setStatus("current")
_FsIpv6SecAhEspIntruEntry_Object = MibTableRow
fsIpv6SecAhEspIntruEntry = _FsIpv6SecAhEspIntruEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 3, 1)
)
fsIpv6SecAhEspIntruEntry.setIndexNames(
    (0, "SUPERMICRO-IPSECV6-MIB", "fsipv6SecAhEspIntruIndex"),
)
if mibBuilder.loadTexts:
    fsIpv6SecAhEspIntruEntry.setStatus("current")


class _Fsipv6SecAhEspIntruIndex_Type(Integer32):
    """Custom type fsipv6SecAhEspIntruIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsipv6SecAhEspIntruIndex_Type.__name__ = "Integer32"
_Fsipv6SecAhEspIntruIndex_Object = MibTableColumn
fsipv6SecAhEspIntruIndex = _Fsipv6SecAhEspIntruIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 3, 1, 1),
    _Fsipv6SecAhEspIntruIndex_Type()
)
fsipv6SecAhEspIntruIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsipv6SecAhEspIntruIndex.setStatus("current")


class _Fsipv6SecAhEspIntruIfIndex_Type(Integer32):
    """Custom type fsipv6SecAhEspIntruIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Fsipv6SecAhEspIntruIfIndex_Type.__name__ = "Integer32"
_Fsipv6SecAhEspIntruIfIndex_Object = MibTableColumn
fsipv6SecAhEspIntruIfIndex = _Fsipv6SecAhEspIntruIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 3, 1, 2),
    _Fsipv6SecAhEspIntruIfIndex_Type()
)
fsipv6SecAhEspIntruIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecAhEspIntruIfIndex.setStatus("current")


class _Fsipv6SecAhEspIntruSrcAddr_Type(OctetString):
    """Custom type fsipv6SecAhEspIntruSrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fsipv6SecAhEspIntruSrcAddr_Type.__name__ = "OctetString"
_Fsipv6SecAhEspIntruSrcAddr_Object = MibTableColumn
fsipv6SecAhEspIntruSrcAddr = _Fsipv6SecAhEspIntruSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 3, 1, 3),
    _Fsipv6SecAhEspIntruSrcAddr_Type()
)
fsipv6SecAhEspIntruSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecAhEspIntruSrcAddr.setStatus("current")


class _Fsipv6SecAhEspIntruDestAddr_Type(OctetString):
    """Custom type fsipv6SecAhEspIntruDestAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fsipv6SecAhEspIntruDestAddr_Type.__name__ = "OctetString"
_Fsipv6SecAhEspIntruDestAddr_Object = MibTableColumn
fsipv6SecAhEspIntruDestAddr = _Fsipv6SecAhEspIntruDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 3, 1, 4),
    _Fsipv6SecAhEspIntruDestAddr_Type()
)
fsipv6SecAhEspIntruDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecAhEspIntruDestAddr.setStatus("current")


class _Fsipv6SecAhEspIntruProto_Type(Integer32):
    """Custom type fsipv6SecAhEspIntruProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              51)
        )
    )
    namedValues = NamedValues(
        *(("espproto", 50),
          ("ahproto", 51))
    )


_Fsipv6SecAhEspIntruProto_Type.__name__ = "Integer32"
_Fsipv6SecAhEspIntruProto_Object = MibTableColumn
fsipv6SecAhEspIntruProto = _Fsipv6SecAhEspIntruProto_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 3, 1, 5),
    _Fsipv6SecAhEspIntruProto_Type()
)
fsipv6SecAhEspIntruProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecAhEspIntruProto.setStatus("current")
_Fsipv6SecAhEspIntruTime_Type = Counter32
_Fsipv6SecAhEspIntruTime_Object = MibTableColumn
fsipv6SecAhEspIntruTime = _Fsipv6SecAhEspIntruTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 29, 3, 3, 1, 6),
    _Fsipv6SecAhEspIntruTime_Type()
)
fsipv6SecAhEspIntruTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsipv6SecAhEspIntruTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-IPSECV6-MIB",
    **{"Ipv6IfIndex": Ipv6IfIndex,
       "fsipv6Sec": fsipv6Sec,
       "fsipv6SecScalars": fsipv6SecScalars,
       "fsipv6SecGlobalStatus": fsipv6SecGlobalStatus,
       "fsipv6SecVersion": fsipv6SecVersion,
       "fsipv6SecGlobalDebug": fsipv6SecGlobalDebug,
       "fsipv6SecMaxSA": fsipv6SecMaxSA,
       "fsipv6SecConfig": fsipv6SecConfig,
       "fsipv6SecSelectorTable": fsipv6SecSelectorTable,
       "fsIpv6SecSelectorEntry": fsIpv6SecSelectorEntry,
       "fsipv6SelIfIndex": fsipv6SelIfIndex,
       "fsipv6SelProtoIndex": fsipv6SelProtoIndex,
       "fsipv6SelAccessIndex": fsipv6SelAccessIndex,
       "fsipv6SelPort": fsipv6SelPort,
       "fsipv6SelPktDirection": fsipv6SelPktDirection,
       "fsipv6SelFilterFlag": fsipv6SelFilterFlag,
       "fsipv6SelPolicyIndex": fsipv6SelPolicyIndex,
       "fsipv6SelIfIpAddress": fsipv6SelIfIpAddress,
       "fsipv6SelStatus": fsipv6SelStatus,
       "fsipv6SecAccessTable": fsipv6SecAccessTable,
       "fsIpv6SecAccessEntry": fsIpv6SecAccessEntry,
       "fsipv6SecAccessIndex": fsipv6SecAccessIndex,
       "fsipv6SecAccessStatus": fsipv6SecAccessStatus,
       "fsipv6SecSrcNet": fsipv6SecSrcNet,
       "fsipv6SecSrcAddrPrefixLen": fsipv6SecSrcAddrPrefixLen,
       "fsipv6SecDestNet": fsipv6SecDestNet,
       "fsipv6SecDestAddrPrefixLen": fsipv6SecDestAddrPrefixLen,
       "fsipv6SecPolicyTable": fsipv6SecPolicyTable,
       "fsIpv6SecPolicyEntry": fsIpv6SecPolicyEntry,
       "fsipv6SecPolicyIndex": fsipv6SecPolicyIndex,
       "fsipv6SecPolicyFlag": fsipv6SecPolicyFlag,
       "fsipv6SecPolicyMode": fsipv6SecPolicyMode,
       "fsipv6SecPolicySaBundle": fsipv6SecPolicySaBundle,
       "fsipv6SecPolicyOptionsIndex": fsipv6SecPolicyOptionsIndex,
       "fsipv6SecPolicyStatus": fsipv6SecPolicyStatus,
       "fsipv6SecAssocTable": fsipv6SecAssocTable,
       "fsipv6SecAssocEntry": fsipv6SecAssocEntry,
       "fsipv6SecAssocIndex": fsipv6SecAssocIndex,
       "fsipv6SecAssocDstAddr": fsipv6SecAssocDstAddr,
       "fsipv6SecAssocProtocol": fsipv6SecAssocProtocol,
       "fsipv6SecAssocSpi": fsipv6SecAssocSpi,
       "fsipv6SecAssocMode": fsipv6SecAssocMode,
       "fsipv6SecAssocAhAlgo": fsipv6SecAssocAhAlgo,
       "fsipv6SecAssocAhKey": fsipv6SecAssocAhKey,
       "fsipv6SecAssocEspAlgo": fsipv6SecAssocEspAlgo,
       "fsipv6SecAssocEspKey": fsipv6SecAssocEspKey,
       "fsipv6SecAssocEspKey2": fsipv6SecAssocEspKey2,
       "fsipv6SecAssocEspKey3": fsipv6SecAssocEspKey3,
       "fsipv6SecAssocLifetimeInBytes": fsipv6SecAssocLifetimeInBytes,
       "fsipv6SecAssocLifetime": fsipv6SecAssocLifetime,
       "fsipv6SecAssocAntiReplay": fsipv6SecAssocAntiReplay,
       "fsipv6SecAssocStatus": fsipv6SecAssocStatus,
       "fsipv6SecStats": fsipv6SecStats,
       "fsipv6SecIfStatsTable": fsipv6SecIfStatsTable,
       "fsIpv6SecIfStatsEntry": fsIpv6SecIfStatsEntry,
       "fsipv6SecIfIndex": fsipv6SecIfIndex,
       "fsipv6SecIfInPkts": fsipv6SecIfInPkts,
       "fsipv6SecIfOutPkts": fsipv6SecIfOutPkts,
       "fsipv6SecIfPktsApply": fsipv6SecIfPktsApply,
       "fsipv6SecIfPktsDiscard": fsipv6SecIfPktsDiscard,
       "fsipv6SecIfPktsBypass": fsipv6SecIfPktsBypass,
       "fsipv6SecAhEspStatsTable": fsipv6SecAhEspStatsTable,
       "fsIpv6SecAhEspStatsEntry": fsIpv6SecAhEspStatsEntry,
       "fsipv6SecAhEspIfIndex": fsipv6SecAhEspIfIndex,
       "fsipv6SecInAhPkts": fsipv6SecInAhPkts,
       "fsipv6SecOutAhPkts": fsipv6SecOutAhPkts,
       "fsipv6SecAhPktsAllow": fsipv6SecAhPktsAllow,
       "fsipv6SecAhPktsDiscard": fsipv6SecAhPktsDiscard,
       "fsipv6SecInEspPkts": fsipv6SecInEspPkts,
       "fsipv6SecOutEspPkts": fsipv6SecOutEspPkts,
       "fsipv6SecEspPktsAllow": fsipv6SecEspPktsAllow,
       "fsipv6SecEspPktsDiscard": fsipv6SecEspPktsDiscard,
       "fsipv6SecAhEspIntruTable": fsipv6SecAhEspIntruTable,
       "fsIpv6SecAhEspIntruEntry": fsIpv6SecAhEspIntruEntry,
       "fsipv6SecAhEspIntruIndex": fsipv6SecAhEspIntruIndex,
       "fsipv6SecAhEspIntruIfIndex": fsipv6SecAhEspIntruIfIndex,
       "fsipv6SecAhEspIntruSrcAddr": fsipv6SecAhEspIntruSrcAddr,
       "fsipv6SecAhEspIntruDestAddr": fsipv6SecAhEspIntruDestAddr,
       "fsipv6SecAhEspIntruProto": fsipv6SecAhEspIntruProto,
       "fsipv6SecAhEspIntruTime": fsipv6SecAhEspIntruTime}
)
