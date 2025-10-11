# SNMP MIB module (ARICENT-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-TUNNEL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:41:56 2025
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

fsTunlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 95)
)
if mibBuilder.loadTexts:
    fsTunlMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FsTunlType(TextualConvention, Integer32):
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
              16,
              17)
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
          ("ipv6ip", 16),
          ("openflow", 17))
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

_FsTunlMIBObjects_ObjectIdentity = ObjectIdentity
fsTunlMIBObjects = _FsTunlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1)
)
_FsTunl_ObjectIdentity = ObjectIdentity
fsTunl = _FsTunl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1)
)
_FsTunlIfTable_Object = MibTable
fsTunlIfTable = _FsTunlIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsTunlIfTable.setStatus("current")
_FsTunlIfEntry_Object = MibTableRow
fsTunlIfEntry = _FsTunlIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1)
)
fsTunlIfEntry.setIndexNames(
    (0, "ARICENT-TUNNEL-MIB", "fsTunlIfAddressType"),
    (0, "ARICENT-TUNNEL-MIB", "fsTunlIfLocalInetAddress"),
    (0, "ARICENT-TUNNEL-MIB", "fsTunlIfRemoteInetAddress"),
    (0, "ARICENT-TUNNEL-MIB", "fsTunlIfEncapsMethod"),
    (0, "ARICENT-TUNNEL-MIB", "fsTunlIfConfigID"),
)
if mibBuilder.loadTexts:
    fsTunlIfEntry.setStatus("current")
_FsTunlIfAddressType_Type = InetAddressType
_FsTunlIfAddressType_Object = MibTableColumn
fsTunlIfAddressType = _FsTunlIfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 1),
    _FsTunlIfAddressType_Type()
)
fsTunlIfAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTunlIfAddressType.setStatus("current")
_FsTunlIfLocalInetAddress_Type = InetAddress
_FsTunlIfLocalInetAddress_Object = MibTableColumn
fsTunlIfLocalInetAddress = _FsTunlIfLocalInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 2),
    _FsTunlIfLocalInetAddress_Type()
)
fsTunlIfLocalInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTunlIfLocalInetAddress.setStatus("current")
_FsTunlIfRemoteInetAddress_Type = InetAddress
_FsTunlIfRemoteInetAddress_Object = MibTableColumn
fsTunlIfRemoteInetAddress = _FsTunlIfRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 3),
    _FsTunlIfRemoteInetAddress_Type()
)
fsTunlIfRemoteInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTunlIfRemoteInetAddress.setStatus("current")
_FsTunlIfEncapsMethod_Type = FsTunlType
_FsTunlIfEncapsMethod_Object = MibTableColumn
fsTunlIfEncapsMethod = _FsTunlIfEncapsMethod_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 4),
    _FsTunlIfEncapsMethod_Type()
)
fsTunlIfEncapsMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTunlIfEncapsMethod.setStatus("current")


class _FsTunlIfConfigID_Type(Integer32):
    """Custom type fsTunlIfConfigID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsTunlIfConfigID_Type.__name__ = "Integer32"
_FsTunlIfConfigID_Object = MibTableColumn
fsTunlIfConfigID = _FsTunlIfConfigID_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 5),
    _FsTunlIfConfigID_Type()
)
fsTunlIfConfigID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTunlIfConfigID.setStatus("current")


class _FsTunlIfHopLimit_Type(Integer32):
    """Custom type fsTunlIfHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsTunlIfHopLimit_Type.__name__ = "Integer32"
_FsTunlIfHopLimit_Object = MibTableColumn
fsTunlIfHopLimit = _FsTunlIfHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 6),
    _FsTunlIfHopLimit_Type()
)
fsTunlIfHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTunlIfHopLimit.setStatus("current")


class _FsTunlIfSecurity_Type(Integer32):
    """Custom type fsTunlIfSecurity based on Integer32"""
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


_FsTunlIfSecurity_Type.__name__ = "Integer32"
_FsTunlIfSecurity_Object = MibTableColumn
fsTunlIfSecurity = _FsTunlIfSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 7),
    _FsTunlIfSecurity_Type()
)
fsTunlIfSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTunlIfSecurity.setStatus("current")


class _FsTunlIfTOS_Type(Integer32):
    """Custom type fsTunlIfTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 63),
    )


_FsTunlIfTOS_Type.__name__ = "Integer32"
_FsTunlIfTOS_Object = MibTableColumn
fsTunlIfTOS = _FsTunlIfTOS_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 8),
    _FsTunlIfTOS_Type()
)
fsTunlIfTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTunlIfTOS.setStatus("current")
_FsTunlIfFlowLabel_Type = FsIPv6FlowLabelOrAny
_FsTunlIfFlowLabel_Object = MibTableColumn
fsTunlIfFlowLabel = _FsTunlIfFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 9),
    _FsTunlIfFlowLabel_Type()
)
fsTunlIfFlowLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTunlIfFlowLabel.setStatus("current")


class _FsTunlIfMTU_Type(Integer32):
    """Custom type fsTunlIfMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1280, 1500),
    )


_FsTunlIfMTU_Type.__name__ = "Integer32"
_FsTunlIfMTU_Object = MibTableColumn
fsTunlIfMTU = _FsTunlIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 10),
    _FsTunlIfMTU_Type()
)
fsTunlIfMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTunlIfMTU.setStatus("current")


class _FsTunlIfDirFlag_Type(Integer32):
    """Custom type fsTunlIfDirFlag based on Integer32"""
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


_FsTunlIfDirFlag_Type.__name__ = "Integer32"
_FsTunlIfDirFlag_Object = MibTableColumn
fsTunlIfDirFlag = _FsTunlIfDirFlag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 11),
    _FsTunlIfDirFlag_Type()
)
fsTunlIfDirFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTunlIfDirFlag.setStatus("current")


class _FsTunlIfDirection_Type(Integer32):
    """Custom type fsTunlIfDirection based on Integer32"""
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


_FsTunlIfDirection_Type.__name__ = "Integer32"
_FsTunlIfDirection_Object = MibTableColumn
fsTunlIfDirection = _FsTunlIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 12),
    _FsTunlIfDirection_Type()
)
fsTunlIfDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTunlIfDirection.setStatus("current")


class _FsTunlIfEncaplmt_Type(Unsigned32):
    """Custom type fsTunlIfEncaplmt based on Unsigned32"""
    defaultValue = 4


_FsTunlIfEncaplmt_Type.__name__ = "Unsigned32"
_FsTunlIfEncaplmt_Object = MibTableColumn
fsTunlIfEncaplmt = _FsTunlIfEncaplmt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 13),
    _FsTunlIfEncaplmt_Type()
)
fsTunlIfEncaplmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTunlIfEncaplmt.setStatus("current")


class _FsTunlIfEncapOption_Type(Integer32):
    """Custom type fsTunlIfEncapOption based on Integer32"""
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


_FsTunlIfEncapOption_Type.__name__ = "Integer32"
_FsTunlIfEncapOption_Object = MibTableColumn
fsTunlIfEncapOption = _FsTunlIfEncapOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 14),
    _FsTunlIfEncapOption_Type()
)
fsTunlIfEncapOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTunlIfEncapOption.setStatus("current")
_FsTunlIfIndex_Type = InterfaceIndexOrZero
_FsTunlIfIndex_Object = MibTableColumn
fsTunlIfIndex = _FsTunlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 15),
    _FsTunlIfIndex_Type()
)
fsTunlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTunlIfIndex.setStatus("current")


class _FsTunlIfAlias_Type(DisplayString):
    """Custom type fsTunlIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FsTunlIfAlias_Type.__name__ = "DisplayString"
_FsTunlIfAlias_Object = MibTableColumn
fsTunlIfAlias = _FsTunlIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 16),
    _FsTunlIfAlias_Type()
)
fsTunlIfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTunlIfAlias.setStatus("current")


class _FsTunlIfCksumFlag_Type(TruthValue):
    """Custom type fsTunlIfCksumFlag based on TruthValue"""
    defaultValue = 2


_FsTunlIfCksumFlag_Type.__name__ = "TruthValue"
_FsTunlIfCksumFlag_Object = MibTableColumn
fsTunlIfCksumFlag = _FsTunlIfCksumFlag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 17),
    _FsTunlIfCksumFlag_Type()
)
fsTunlIfCksumFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTunlIfCksumFlag.setStatus("current")


class _FsTunlIfPmtuFlag_Type(TruthValue):
    """Custom type fsTunlIfPmtuFlag based on TruthValue"""
    defaultValue = 2


_FsTunlIfPmtuFlag_Type.__name__ = "TruthValue"
_FsTunlIfPmtuFlag_Object = MibTableColumn
fsTunlIfPmtuFlag = _FsTunlIfPmtuFlag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 18),
    _FsTunlIfPmtuFlag_Type()
)
fsTunlIfPmtuFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTunlIfPmtuFlag.setStatus("current")
_FsTunlIfStatus_Type = RowStatus
_FsTunlIfStatus_Object = MibTableColumn
fsTunlIfStatus = _FsTunlIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 95, 1, 1, 1, 1, 19),
    _FsTunlIfStatus_Type()
)
fsTunlIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTunlIfStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-TUNNEL-MIB",
    **{"FsTunlType": FsTunlType,
       "FsIPv6FlowLabelOrAny": FsIPv6FlowLabelOrAny,
       "fsTunlMIB": fsTunlMIB,
       "fsTunlMIBObjects": fsTunlMIBObjects,
       "fsTunl": fsTunl,
       "fsTunlIfTable": fsTunlIfTable,
       "fsTunlIfEntry": fsTunlIfEntry,
       "fsTunlIfAddressType": fsTunlIfAddressType,
       "fsTunlIfLocalInetAddress": fsTunlIfLocalInetAddress,
       "fsTunlIfRemoteInetAddress": fsTunlIfRemoteInetAddress,
       "fsTunlIfEncapsMethod": fsTunlIfEncapsMethod,
       "fsTunlIfConfigID": fsTunlIfConfigID,
       "fsTunlIfHopLimit": fsTunlIfHopLimit,
       "fsTunlIfSecurity": fsTunlIfSecurity,
       "fsTunlIfTOS": fsTunlIfTOS,
       "fsTunlIfFlowLabel": fsTunlIfFlowLabel,
       "fsTunlIfMTU": fsTunlIfMTU,
       "fsTunlIfDirFlag": fsTunlIfDirFlag,
       "fsTunlIfDirection": fsTunlIfDirection,
       "fsTunlIfEncaplmt": fsTunlIfEncaplmt,
       "fsTunlIfEncapOption": fsTunlIfEncapOption,
       "fsTunlIfIndex": fsTunlIfIndex,
       "fsTunlIfAlias": fsTunlIfAlias,
       "fsTunlIfCksumFlag": fsTunlIfCksumFlag,
       "fsTunlIfPmtuFlag": fsTunlIfPmtuFlag,
       "fsTunlIfStatus": fsTunlIfStatus}
)
