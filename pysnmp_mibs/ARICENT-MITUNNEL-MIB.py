# SNMP MIB module (ARICENT-MITUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-MITUNNEL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:57 2025
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

(fsMIStdIpContextId,) = mibBuilder.importSymbols(
    "ARICENT-MISTD-IPVX-MIB",
    "fsMIStdIpContextId")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsMITunlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39)
)
if mibBuilder.loadTexts:
    fsMITunlMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FsMITunlType(TextualConvention, Integer32):
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
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("direct", 2),
          ("gre", 3),
          ("minimal", 4),
          ("l2tp", 5),
          ("pptp", 6),
          ("l2f", 7),
          ("udp", 8),
          ("atmp", 9),
          ("msdp", 10),
          ("sixToFour", 11),
          ("sixOverFour", 12),
          ("isatap", 13),
          ("teredo", 14),
          ("compat", 15),
          ("ipv6ip", 16))
    )



class FsIPv6FlowLabelOrAny(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1048575),
    )



# MIB Managed Objects in the order of their OIDs

_FsMITunlMIBObjects_ObjectIdentity = ObjectIdentity
fsMITunlMIBObjects = _FsMITunlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1)
)
_FsMITunl_ObjectIdentity = ObjectIdentity
fsMITunl = _FsMITunl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1)
)
_FsMITunlIfTable_Object = MibTable
fsMITunlIfTable = _FsMITunlIfTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsMITunlIfTable.setStatus("current")
_FsMITunlIfEntry_Object = MibTableRow
fsMITunlIfEntry = _FsMITunlIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1)
)
fsMITunlIfEntry.setIndexNames(
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
    (0, "ARICENT-MITUNNEL-MIB", "fsMITunlIfAddressType"),
    (0, "ARICENT-MITUNNEL-MIB", "fsMITunlIfLocalInetAddress"),
    (0, "ARICENT-MITUNNEL-MIB", "fsMITunlIfRemoteInetAddress"),
    (0, "ARICENT-MITUNNEL-MIB", "fsMITunlIfEncapsMethod"),
    (0, "ARICENT-MITUNNEL-MIB", "fsMITunlIfConfigID"),
)
if mibBuilder.loadTexts:
    fsMITunlIfEntry.setStatus("current")
_FsMITunlIfAddressType_Type = InetAddressType
_FsMITunlIfAddressType_Object = MibTableColumn
fsMITunlIfAddressType = _FsMITunlIfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 1),
    _FsMITunlIfAddressType_Type()
)
fsMITunlIfAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMITunlIfAddressType.setStatus("current")


class _FsMITunlIfLocalInetAddress_Type(InetAddress):
    """Custom type fsMITunlIfLocalInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMITunlIfLocalInetAddress_Type.__name__ = "InetAddress"
_FsMITunlIfLocalInetAddress_Object = MibTableColumn
fsMITunlIfLocalInetAddress = _FsMITunlIfLocalInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 2),
    _FsMITunlIfLocalInetAddress_Type()
)
fsMITunlIfLocalInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMITunlIfLocalInetAddress.setStatus("current")


class _FsMITunlIfRemoteInetAddress_Type(InetAddress):
    """Custom type fsMITunlIfRemoteInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMITunlIfRemoteInetAddress_Type.__name__ = "InetAddress"
_FsMITunlIfRemoteInetAddress_Object = MibTableColumn
fsMITunlIfRemoteInetAddress = _FsMITunlIfRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 3),
    _FsMITunlIfRemoteInetAddress_Type()
)
fsMITunlIfRemoteInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMITunlIfRemoteInetAddress.setStatus("current")
_FsMITunlIfEncapsMethod_Type = FsMITunlType
_FsMITunlIfEncapsMethod_Object = MibTableColumn
fsMITunlIfEncapsMethod = _FsMITunlIfEncapsMethod_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 4),
    _FsMITunlIfEncapsMethod_Type()
)
fsMITunlIfEncapsMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMITunlIfEncapsMethod.setStatus("current")


class _FsMITunlIfConfigID_Type(Integer32):
    """Custom type fsMITunlIfConfigID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsMITunlIfConfigID_Type.__name__ = "Integer32"
_FsMITunlIfConfigID_Object = MibTableColumn
fsMITunlIfConfigID = _FsMITunlIfConfigID_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 5),
    _FsMITunlIfConfigID_Type()
)
fsMITunlIfConfigID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMITunlIfConfigID.setStatus("current")


class _FsMITunlIfHopLimit_Type(Integer32):
    """Custom type fsMITunlIfHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMITunlIfHopLimit_Type.__name__ = "Integer32"
_FsMITunlIfHopLimit_Object = MibTableColumn
fsMITunlIfHopLimit = _FsMITunlIfHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 6),
    _FsMITunlIfHopLimit_Type()
)
fsMITunlIfHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITunlIfHopLimit.setStatus("current")


class _FsMITunlIfSecurity_Type(Integer32):
    """Custom type fsMITunlIfSecurity based on Integer32"""
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
          ("ipsec", 2),
          ("other", 3))
    )


_FsMITunlIfSecurity_Type.__name__ = "Integer32"
_FsMITunlIfSecurity_Object = MibTableColumn
fsMITunlIfSecurity = _FsMITunlIfSecurity_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 7),
    _FsMITunlIfSecurity_Type()
)
fsMITunlIfSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITunlIfSecurity.setStatus("current")


class _FsMITunlIfTOS_Type(Integer32):
    """Custom type fsMITunlIfTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 63),
    )


_FsMITunlIfTOS_Type.__name__ = "Integer32"
_FsMITunlIfTOS_Object = MibTableColumn
fsMITunlIfTOS = _FsMITunlIfTOS_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 8),
    _FsMITunlIfTOS_Type()
)
fsMITunlIfTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITunlIfTOS.setStatus("current")
_FsMITunlIfFlowLabel_Type = FsIPv6FlowLabelOrAny
_FsMITunlIfFlowLabel_Object = MibTableColumn
fsMITunlIfFlowLabel = _FsMITunlIfFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 9),
    _FsMITunlIfFlowLabel_Type()
)
fsMITunlIfFlowLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITunlIfFlowLabel.setStatus("current")


class _FsMITunlIfMTU_Type(Integer32):
    """Custom type fsMITunlIfMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1280, 1500),
    )


_FsMITunlIfMTU_Type.__name__ = "Integer32"
_FsMITunlIfMTU_Object = MibTableColumn
fsMITunlIfMTU = _FsMITunlIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 10),
    _FsMITunlIfMTU_Type()
)
fsMITunlIfMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITunlIfMTU.setStatus("current")


class _FsMITunlIfDirFlag_Type(Integer32):
    """Custom type fsMITunlIfDirFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unidirectional", 1),
          ("bidirectional", 2))
    )


_FsMITunlIfDirFlag_Type.__name__ = "Integer32"
_FsMITunlIfDirFlag_Object = MibTableColumn
fsMITunlIfDirFlag = _FsMITunlIfDirFlag_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 11),
    _FsMITunlIfDirFlag_Type()
)
fsMITunlIfDirFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITunlIfDirFlag.setStatus("current")


class _FsMITunlIfDirection_Type(Integer32):
    """Custom type fsMITunlIfDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_FsMITunlIfDirection_Type.__name__ = "Integer32"
_FsMITunlIfDirection_Object = MibTableColumn
fsMITunlIfDirection = _FsMITunlIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 12),
    _FsMITunlIfDirection_Type()
)
fsMITunlIfDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITunlIfDirection.setStatus("current")


class _FsMITunlIfEncaplmt_Type(Unsigned32):
    """Custom type fsMITunlIfEncaplmt based on Unsigned32"""
    defaultValue = 4


_FsMITunlIfEncaplmt_Type.__name__ = "Unsigned32"
_FsMITunlIfEncaplmt_Object = MibTableColumn
fsMITunlIfEncaplmt = _FsMITunlIfEncaplmt_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 13),
    _FsMITunlIfEncaplmt_Type()
)
fsMITunlIfEncaplmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITunlIfEncaplmt.setStatus("current")


class _FsMITunlIfEncapOption_Type(Integer32):
    """Custom type fsMITunlIfEncapOption based on Integer32"""
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


_FsMITunlIfEncapOption_Type.__name__ = "Integer32"
_FsMITunlIfEncapOption_Object = MibTableColumn
fsMITunlIfEncapOption = _FsMITunlIfEncapOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 14),
    _FsMITunlIfEncapOption_Type()
)
fsMITunlIfEncapOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITunlIfEncapOption.setStatus("current")
_FsMITunlIfIndex_Type = InterfaceIndexOrZero
_FsMITunlIfIndex_Object = MibTableColumn
fsMITunlIfIndex = _FsMITunlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 15),
    _FsMITunlIfIndex_Type()
)
fsMITunlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITunlIfIndex.setStatus("current")


class _FsMITunlIfAlias_Type(DisplayString):
    """Custom type fsMITunlIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FsMITunlIfAlias_Type.__name__ = "DisplayString"
_FsMITunlIfAlias_Object = MibTableColumn
fsMITunlIfAlias = _FsMITunlIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 16),
    _FsMITunlIfAlias_Type()
)
fsMITunlIfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITunlIfAlias.setStatus("current")


class _FsMITunlIfCksumFlag_Type(TruthValue):
    """Custom type fsMITunlIfCksumFlag based on TruthValue"""
    defaultValue = 2


_FsMITunlIfCksumFlag_Type.__name__ = "TruthValue"
_FsMITunlIfCksumFlag_Object = MibTableColumn
fsMITunlIfCksumFlag = _FsMITunlIfCksumFlag_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 17),
    _FsMITunlIfCksumFlag_Type()
)
fsMITunlIfCksumFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITunlIfCksumFlag.setStatus("current")


class _FsMITunlIfPmtuFlag_Type(TruthValue):
    """Custom type fsMITunlIfPmtuFlag based on TruthValue"""
    defaultValue = 2


_FsMITunlIfPmtuFlag_Type.__name__ = "TruthValue"
_FsMITunlIfPmtuFlag_Object = MibTableColumn
fsMITunlIfPmtuFlag = _FsMITunlIfPmtuFlag_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 18),
    _FsMITunlIfPmtuFlag_Type()
)
fsMITunlIfPmtuFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITunlIfPmtuFlag.setStatus("current")
_FsMITunlIfStatus_Type = RowStatus
_FsMITunlIfStatus_Object = MibTableColumn
fsMITunlIfStatus = _FsMITunlIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 39, 1, 1, 1, 1, 19),
    _FsMITunlIfStatus_Type()
)
fsMITunlIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMITunlIfStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-MITUNNEL-MIB",
    **{"FsMITunlType": FsMITunlType,
       "FsIPv6FlowLabelOrAny": FsIPv6FlowLabelOrAny,
       "fsMITunlMIB": fsMITunlMIB,
       "fsMITunlMIBObjects": fsMITunlMIBObjects,
       "fsMITunl": fsMITunl,
       "fsMITunlIfTable": fsMITunlIfTable,
       "fsMITunlIfEntry": fsMITunlIfEntry,
       "fsMITunlIfAddressType": fsMITunlIfAddressType,
       "fsMITunlIfLocalInetAddress": fsMITunlIfLocalInetAddress,
       "fsMITunlIfRemoteInetAddress": fsMITunlIfRemoteInetAddress,
       "fsMITunlIfEncapsMethod": fsMITunlIfEncapsMethod,
       "fsMITunlIfConfigID": fsMITunlIfConfigID,
       "fsMITunlIfHopLimit": fsMITunlIfHopLimit,
       "fsMITunlIfSecurity": fsMITunlIfSecurity,
       "fsMITunlIfTOS": fsMITunlIfTOS,
       "fsMITunlIfFlowLabel": fsMITunlIfFlowLabel,
       "fsMITunlIfMTU": fsMITunlIfMTU,
       "fsMITunlIfDirFlag": fsMITunlIfDirFlag,
       "fsMITunlIfDirection": fsMITunlIfDirection,
       "fsMITunlIfEncaplmt": fsMITunlIfEncaplmt,
       "fsMITunlIfEncapOption": fsMITunlIfEncapOption,
       "fsMITunlIfIndex": fsMITunlIfIndex,
       "fsMITunlIfAlias": fsMITunlIfAlias,
       "fsMITunlIfCksumFlag": fsMITunlIfCksumFlag,
       "fsMITunlIfPmtuFlag": fsMITunlIfPmtuFlag,
       "fsMITunlIfStatus": fsMITunlIfStatus}
)
