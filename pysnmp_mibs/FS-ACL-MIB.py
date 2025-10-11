# SNMP MIB module (FS-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-ACL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:15 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus",
    "IfIndex")

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

fsAclMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17)
)
if mibBuilder.loadTexts:
    fsAclMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsAclMIBObjects_ObjectIdentity = ObjectIdentity
fsAclMIBObjects = _FsAclMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1)
)
_FsAclTable_Object = MibTable
fsAclTable = _FsAclTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 1)
)
if mibBuilder.loadTexts:
    fsAclTable.setStatus("current")
_FsAclEntry_Object = MibTableRow
fsAclEntry = _FsAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 1, 1)
)
fsAclEntry.setIndexNames(
    (0, "FS-ACL-MIB", "fsAclName"),
)
if mibBuilder.loadTexts:
    fsAclEntry.setStatus("current")


class _FsAclName_Type(DisplayString):
    """Custom type fsAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsAclName_Type.__name__ = "DisplayString"
_FsAclName_Object = MibTableColumn
fsAclName = _FsAclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 1, 1, 1),
    _FsAclName_Type()
)
fsAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAclName.setStatus("current")


class _FsAclMode_Type(Integer32):
    """Custom type fsAclMode based on Integer32"""
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
        *(("acl-ip-standard", 1),
          ("acl-ip-extended", 2),
          ("acl-mac-extended", 3),
          ("acl-expert", 4),
          ("acl-ipv6-extended", 5))
    )


_FsAclMode_Type.__name__ = "Integer32"
_FsAclMode_Object = MibTableColumn
fsAclMode = _FsAclMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 1, 1, 2),
    _FsAclMode_Type()
)
fsAclMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAclMode.setStatus("current")
_FsAclEntryStatus_Type = ConfigStatus
_FsAclEntryStatus_Object = MibTableColumn
fsAclEntryStatus = _FsAclEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 1, 1, 3),
    _FsAclEntryStatus_Type()
)
fsAclEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAclEntryStatus.setStatus("current")
_FsAclIfTable_Object = MibTable
fsAclIfTable = _FsAclIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 3)
)
if mibBuilder.loadTexts:
    fsAclIfTable.setStatus("current")
_FsAclIfEntry_Object = MibTableRow
fsAclIfEntry = _FsAclIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 3, 1)
)
fsAclIfEntry.setIndexNames(
    (0, "FS-ACL-MIB", "fsAclIfIndex"),
)
if mibBuilder.loadTexts:
    fsAclIfEntry.setStatus("current")
_FsAclIfIndex_Type = IfIndex
_FsAclIfIndex_Object = MibTableColumn
fsAclIfIndex = _FsAclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 3, 1, 1),
    _FsAclIfIndex_Type()
)
fsAclIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAclIfIndex.setStatus("current")
_FsAclIfMaxEntryNum_Type = Integer32
_FsAclIfMaxEntryNum_Object = MibTableColumn
fsAclIfMaxEntryNum = _FsAclIfMaxEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 3, 1, 2),
    _FsAclIfMaxEntryNum_Type()
)
fsAclIfMaxEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAclIfMaxEntryNum.setStatus("current")
_FsAclIfCurruntEntryNum_Type = Integer32
_FsAclIfCurruntEntryNum_Object = MibTableColumn
fsAclIfCurruntEntryNum = _FsAclIfCurruntEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 3, 1, 3),
    _FsAclIfCurruntEntryNum_Type()
)
fsAclIfCurruntEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAclIfCurruntEntryNum.setStatus("current")


class _FsIfInAclName_Type(DisplayString):
    """Custom type fsIfInAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsIfInAclName_Type.__name__ = "DisplayString"
_FsIfInAclName_Object = MibTableColumn
fsIfInAclName = _FsIfInAclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 3, 1, 4),
    _FsIfInAclName_Type()
)
fsIfInAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfInAclName.setStatus("current")


class _FsIfOutAclName_Type(DisplayString):
    """Custom type fsIfOutAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsIfOutAclName_Type.__name__ = "DisplayString"
_FsIfOutAclName_Object = MibTableColumn
fsIfOutAclName = _FsIfOutAclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 3, 1, 5),
    _FsIfOutAclName_Type()
)
fsIfOutAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfOutAclName.setStatus("current")
_FsAclIf6MaxEntryNum_Type = Integer32
_FsAclIf6MaxEntryNum_Object = MibTableColumn
fsAclIf6MaxEntryNum = _FsAclIf6MaxEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 3, 1, 6),
    _FsAclIf6MaxEntryNum_Type()
)
fsAclIf6MaxEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAclIf6MaxEntryNum.setStatus("current")
_FsAclIf6CurruntEntryNum_Type = Integer32
_FsAclIf6CurruntEntryNum_Object = MibTableColumn
fsAclIf6CurruntEntryNum = _FsAclIf6CurruntEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 3, 1, 7),
    _FsAclIf6CurruntEntryNum_Type()
)
fsAclIf6CurruntEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAclIf6CurruntEntryNum.setStatus("current")


class _FsIf6InAclName_Type(DisplayString):
    """Custom type fsIf6InAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsIf6InAclName_Type.__name__ = "DisplayString"
_FsIf6InAclName_Object = MibTableColumn
fsIf6InAclName = _FsIf6InAclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 3, 1, 8),
    _FsIf6InAclName_Type()
)
fsIf6InAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIf6InAclName.setStatus("current")


class _FsIf6OutAclName_Type(DisplayString):
    """Custom type fsIf6OutAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsIf6OutAclName_Type.__name__ = "DisplayString"
_FsIf6OutAclName_Object = MibTableColumn
fsIf6OutAclName = _FsIf6OutAclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 3, 1, 9),
    _FsIf6OutAclName_Type()
)
fsIf6OutAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIf6OutAclName.setStatus("current")
_FsAceExtTable_Object = MibTable
fsAceExtTable = _FsAceExtTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4)
)
if mibBuilder.loadTexts:
    fsAceExtTable.setStatus("current")
_FsAceExtEntry_Object = MibTableRow
fsAceExtEntry = _FsAceExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1)
)
fsAceExtEntry.setIndexNames(
    (0, "FS-ACL-MIB", "fsAceExtAclName"),
    (0, "FS-ACL-MIB", "fsAceExtIndex"),
)
if mibBuilder.loadTexts:
    fsAceExtEntry.setStatus("current")


class _FsAceExtAclName_Type(DisplayString):
    """Custom type fsAceExtAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsAceExtAclName_Type.__name__ = "DisplayString"
_FsAceExtAclName_Object = MibTableColumn
fsAceExtAclName = _FsAceExtAclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 1),
    _FsAceExtAclName_Type()
)
fsAceExtAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAceExtAclName.setStatus("current")


class _FsAceExtIndex_Type(Integer32):
    """Custom type fsAceExtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsAceExtIndex_Type.__name__ = "Integer32"
_FsAceExtIndex_Object = MibTableColumn
fsAceExtIndex = _FsAceExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 2),
    _FsAceExtIndex_Type()
)
fsAceExtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAceExtIndex.setStatus("current")


class _FsAceExtIfAnyVID_Type(TruthValue):
    """Custom type fsAceExtIfAnyVID based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyVID_Type.__name__ = "TruthValue"
_FsAceExtIfAnyVID_Object = MibTableColumn
fsAceExtIfAnyVID = _FsAceExtIfAnyVID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 3),
    _FsAceExtIfAnyVID_Type()
)
fsAceExtIfAnyVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyVID.setStatus("current")


class _FsAceExtVID_Type(Unsigned32):
    """Custom type fsAceExtVID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_FsAceExtVID_Type.__name__ = "Unsigned32"
_FsAceExtVID_Object = MibTableColumn
fsAceExtVID = _FsAceExtVID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 4),
    _FsAceExtVID_Type()
)
fsAceExtVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtVID.setStatus("current")


class _FsAceExtIfAnySourceIp_Type(TruthValue):
    """Custom type fsAceExtIfAnySourceIp based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnySourceIp_Type.__name__ = "TruthValue"
_FsAceExtIfAnySourceIp_Object = MibTableColumn
fsAceExtIfAnySourceIp = _FsAceExtIfAnySourceIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 5),
    _FsAceExtIfAnySourceIp_Type()
)
fsAceExtIfAnySourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnySourceIp.setStatus("current")
_FsAceExtSourceIp_Type = IpAddress
_FsAceExtSourceIp_Object = MibTableColumn
fsAceExtSourceIp = _FsAceExtSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 6),
    _FsAceExtSourceIp_Type()
)
fsAceExtSourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtSourceIp.setStatus("current")


class _FsAceExtIfAnySourceWildCard_Type(TruthValue):
    """Custom type fsAceExtIfAnySourceWildCard based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnySourceWildCard_Type.__name__ = "TruthValue"
_FsAceExtIfAnySourceWildCard_Object = MibTableColumn
fsAceExtIfAnySourceWildCard = _FsAceExtIfAnySourceWildCard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 7),
    _FsAceExtIfAnySourceWildCard_Type()
)
fsAceExtIfAnySourceWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnySourceWildCard.setStatus("current")
_FsAceExtSourceWildCard_Type = IpAddress
_FsAceExtSourceWildCard_Object = MibTableColumn
fsAceExtSourceWildCard = _FsAceExtSourceWildCard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 8),
    _FsAceExtSourceWildCard_Type()
)
fsAceExtSourceWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtSourceWildCard.setStatus("current")


class _FsAceExtIfAnySourceMacAddr_Type(TruthValue):
    """Custom type fsAceExtIfAnySourceMacAddr based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnySourceMacAddr_Type.__name__ = "TruthValue"
_FsAceExtIfAnySourceMacAddr_Object = MibTableColumn
fsAceExtIfAnySourceMacAddr = _FsAceExtIfAnySourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 9),
    _FsAceExtIfAnySourceMacAddr_Type()
)
fsAceExtIfAnySourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnySourceMacAddr.setStatus("current")
_FsAceExtSourceMacAddr_Type = MacAddress
_FsAceExtSourceMacAddr_Object = MibTableColumn
fsAceExtSourceMacAddr = _FsAceExtSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 10),
    _FsAceExtSourceMacAddr_Type()
)
fsAceExtSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtSourceMacAddr.setStatus("current")


class _FsAceExtIfAnyDestIp_Type(TruthValue):
    """Custom type fsAceExtIfAnyDestIp based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyDestIp_Type.__name__ = "TruthValue"
_FsAceExtIfAnyDestIp_Object = MibTableColumn
fsAceExtIfAnyDestIp = _FsAceExtIfAnyDestIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 11),
    _FsAceExtIfAnyDestIp_Type()
)
fsAceExtIfAnyDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyDestIp.setStatus("current")
_FsAceExtDestIp_Type = IpAddress
_FsAceExtDestIp_Object = MibTableColumn
fsAceExtDestIp = _FsAceExtDestIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 12),
    _FsAceExtDestIp_Type()
)
fsAceExtDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtDestIp.setStatus("current")


class _FsAceExtIfAnyDestWildCard_Type(TruthValue):
    """Custom type fsAceExtIfAnyDestWildCard based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyDestWildCard_Type.__name__ = "TruthValue"
_FsAceExtIfAnyDestWildCard_Object = MibTableColumn
fsAceExtIfAnyDestWildCard = _FsAceExtIfAnyDestWildCard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 13),
    _FsAceExtIfAnyDestWildCard_Type()
)
fsAceExtIfAnyDestWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyDestWildCard.setStatus("current")
_FsAceExtDestIpWildCard_Type = IpAddress
_FsAceExtDestIpWildCard_Object = MibTableColumn
fsAceExtDestIpWildCard = _FsAceExtDestIpWildCard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 14),
    _FsAceExtDestIpWildCard_Type()
)
fsAceExtDestIpWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtDestIpWildCard.setStatus("current")


class _FsAceExtIfAnyDestMacAddr_Type(TruthValue):
    """Custom type fsAceExtIfAnyDestMacAddr based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyDestMacAddr_Type.__name__ = "TruthValue"
_FsAceExtIfAnyDestMacAddr_Object = MibTableColumn
fsAceExtIfAnyDestMacAddr = _FsAceExtIfAnyDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 15),
    _FsAceExtIfAnyDestMacAddr_Type()
)
fsAceExtIfAnyDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyDestMacAddr.setStatus("current")
_FsAceExtDestMacAddr_Type = MacAddress
_FsAceExtDestMacAddr_Object = MibTableColumn
fsAceExtDestMacAddr = _FsAceExtDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 16),
    _FsAceExtDestMacAddr_Type()
)
fsAceExtDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtDestMacAddr.setStatus("current")


class _FsAceExtIfAnyEtherLikeType_Type(TruthValue):
    """Custom type fsAceExtIfAnyEtherLikeType based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyEtherLikeType_Type.__name__ = "TruthValue"
_FsAceExtIfAnyEtherLikeType_Object = MibTableColumn
fsAceExtIfAnyEtherLikeType = _FsAceExtIfAnyEtherLikeType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 17),
    _FsAceExtIfAnyEtherLikeType_Type()
)
fsAceExtIfAnyEtherLikeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyEtherLikeType.setStatus("current")
_FsAceExtEtherLikeType_Type = Integer32
_FsAceExtEtherLikeType_Object = MibTableColumn
fsAceExtEtherLikeType = _FsAceExtEtherLikeType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 18),
    _FsAceExtEtherLikeType_Type()
)
fsAceExtEtherLikeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtEtherLikeType.setStatus("current")


class _FsAceExtIfAnyIpProtocolField_Type(TruthValue):
    """Custom type fsAceExtIfAnyIpProtocolField based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyIpProtocolField_Type.__name__ = "TruthValue"
_FsAceExtIfAnyIpProtocolField_Object = MibTableColumn
fsAceExtIfAnyIpProtocolField = _FsAceExtIfAnyIpProtocolField_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 19),
    _FsAceExtIfAnyIpProtocolField_Type()
)
fsAceExtIfAnyIpProtocolField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyIpProtocolField.setStatus("current")
_FsAceExtIpProtocolField_Type = Integer32
_FsAceExtIpProtocolField_Object = MibTableColumn
fsAceExtIpProtocolField = _FsAceExtIpProtocolField_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 20),
    _FsAceExtIpProtocolField_Type()
)
fsAceExtIpProtocolField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIpProtocolField.setStatus("current")
_FsAceExtSourceProtocolPort_Type = Integer32
_FsAceExtSourceProtocolPort_Object = MibTableColumn
fsAceExtSourceProtocolPort = _FsAceExtSourceProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 21),
    _FsAceExtSourceProtocolPort_Type()
)
fsAceExtSourceProtocolPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtSourceProtocolPort.setStatus("current")
_FsAceExtDestProtocolPort_Type = Integer32
_FsAceExtDestProtocolPort_Object = MibTableColumn
fsAceExtDestProtocolPort = _FsAceExtDestProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 22),
    _FsAceExtDestProtocolPort_Type()
)
fsAceExtDestProtocolPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtDestProtocolPort.setStatus("current")


class _FsAceExtIfAnyProtocolType_Type(TruthValue):
    """Custom type fsAceExtIfAnyProtocolType based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyProtocolType_Type.__name__ = "TruthValue"
_FsAceExtIfAnyProtocolType_Object = MibTableColumn
fsAceExtIfAnyProtocolType = _FsAceExtIfAnyProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 23),
    _FsAceExtIfAnyProtocolType_Type()
)
fsAceExtIfAnyProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyProtocolType.setStatus("current")
_FsAceExtProtocolType_Type = Integer32
_FsAceExtProtocolType_Object = MibTableColumn
fsAceExtProtocolType = _FsAceExtProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 24),
    _FsAceExtProtocolType_Type()
)
fsAceExtProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtProtocolType.setStatus("current")


class _FsAceExtFlowAction_Type(Integer32):
    """Custom type fsAceExtFlowAction based on Integer32"""
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


_FsAceExtFlowAction_Type.__name__ = "Integer32"
_FsAceExtFlowAction_Object = MibTableColumn
fsAceExtFlowAction = _FsAceExtFlowAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 25),
    _FsAceExtFlowAction_Type()
)
fsAceExtFlowAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtFlowAction.setStatus("current")
_FsAceExtEntryStauts_Type = RowStatus
_FsAceExtEntryStauts_Object = MibTableColumn
fsAceExtEntryStauts = _FsAceExtEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 26),
    _FsAceExtEntryStauts_Type()
)
fsAceExtEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtEntryStauts.setStatus("current")


class _FsAceExtTimeRangeName_Type(DisplayString):
    """Custom type fsAceExtTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsAceExtTimeRangeName_Type.__name__ = "DisplayString"
_FsAceExtTimeRangeName_Object = MibTableColumn
fsAceExtTimeRangeName = _FsAceExtTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 27),
    _FsAceExtTimeRangeName_Type()
)
fsAceExtTimeRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtTimeRangeName.setStatus("current")


class _FsAceExtSourcePortOp_Type(Integer32):
    """Custom type fsAceExtSourcePortOp based on Integer32"""
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
        *(("noOperator", 1),
          ("lt", 2),
          ("gt", 3),
          ("eq", 4),
          ("neq", 5),
          ("range", 6))
    )


_FsAceExtSourcePortOp_Type.__name__ = "Integer32"
_FsAceExtSourcePortOp_Object = MibTableColumn
fsAceExtSourcePortOp = _FsAceExtSourcePortOp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 28),
    _FsAceExtSourcePortOp_Type()
)
fsAceExtSourcePortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtSourcePortOp.setStatus("current")
_FsAceExtSourceProtocolPortRange_Type = Integer32
_FsAceExtSourceProtocolPortRange_Object = MibTableColumn
fsAceExtSourceProtocolPortRange = _FsAceExtSourceProtocolPortRange_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 29),
    _FsAceExtSourceProtocolPortRange_Type()
)
fsAceExtSourceProtocolPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtSourceProtocolPortRange.setStatus("current")


class _FsAceExtDestPortOp_Type(Integer32):
    """Custom type fsAceExtDestPortOp based on Integer32"""
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
        *(("noOperator", 1),
          ("lt", 2),
          ("gt", 3),
          ("eq", 4),
          ("neq", 5),
          ("range", 6))
    )


_FsAceExtDestPortOp_Type.__name__ = "Integer32"
_FsAceExtDestPortOp_Object = MibTableColumn
fsAceExtDestPortOp = _FsAceExtDestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 30),
    _FsAceExtDestPortOp_Type()
)
fsAceExtDestPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtDestPortOp.setStatus("current")
_FsAceExtDestProtocolPortRange_Type = Integer32
_FsAceExtDestProtocolPortRange_Object = MibTableColumn
fsAceExtDestProtocolPortRange = _FsAceExtDestProtocolPortRange_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 31),
    _FsAceExtDestProtocolPortRange_Type()
)
fsAceExtDestProtocolPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtDestProtocolPortRange.setStatus("current")


class _FsAceExtIfAnyCos_Type(TruthValue):
    """Custom type fsAceExtIfAnyCos based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyCos_Type.__name__ = "TruthValue"
_FsAceExtIfAnyCos_Object = MibTableColumn
fsAceExtIfAnyCos = _FsAceExtIfAnyCos_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 32),
    _FsAceExtIfAnyCos_Type()
)
fsAceExtIfAnyCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtIfAnyCos.setStatus("current")
_FsAceExtCos_Type = Integer32
_FsAceExtCos_Object = MibTableColumn
fsAceExtCos = _FsAceExtCos_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 33),
    _FsAceExtCos_Type()
)
fsAceExtCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtCos.setStatus("current")


class _FsAceExtIfAnyIpPrec_Type(TruthValue):
    """Custom type fsAceExtIfAnyIpPrec based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyIpPrec_Type.__name__ = "TruthValue"
_FsAceExtIfAnyIpPrec_Object = MibTableColumn
fsAceExtIfAnyIpPrec = _FsAceExtIfAnyIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 34),
    _FsAceExtIfAnyIpPrec_Type()
)
fsAceExtIfAnyIpPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtIfAnyIpPrec.setStatus("current")
_FsAceExtIpPrec_Type = Integer32
_FsAceExtIpPrec_Object = MibTableColumn
fsAceExtIpPrec = _FsAceExtIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 35),
    _FsAceExtIpPrec_Type()
)
fsAceExtIpPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtIpPrec.setStatus("current")


class _FsAceExtIfAnyDscp_Type(TruthValue):
    """Custom type fsAceExtIfAnyDscp based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyDscp_Type.__name__ = "TruthValue"
_FsAceExtIfAnyDscp_Object = MibTableColumn
fsAceExtIfAnyDscp = _FsAceExtIfAnyDscp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 36),
    _FsAceExtIfAnyDscp_Type()
)
fsAceExtIfAnyDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtIfAnyDscp.setStatus("current")
_FsAceExtDscp_Type = Integer32
_FsAceExtDscp_Object = MibTableColumn
fsAceExtDscp = _FsAceExtDscp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 37),
    _FsAceExtDscp_Type()
)
fsAceExtDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtDscp.setStatus("current")


class _FsAceExtIfAnyTcpFlag_Type(TruthValue):
    """Custom type fsAceExtIfAnyTcpFlag based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyTcpFlag_Type.__name__ = "TruthValue"
_FsAceExtIfAnyTcpFlag_Object = MibTableColumn
fsAceExtIfAnyTcpFlag = _FsAceExtIfAnyTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 38),
    _FsAceExtIfAnyTcpFlag_Type()
)
fsAceExtIfAnyTcpFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtIfAnyTcpFlag.setStatus("current")
_FsAceExtTcpFlag_Type = Integer32
_FsAceExtTcpFlag_Object = MibTableColumn
fsAceExtTcpFlag = _FsAceExtTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 39),
    _FsAceExtTcpFlag_Type()
)
fsAceExtTcpFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtTcpFlag.setStatus("current")


class _FsAceExtIfAnySourceMacAddrWildCard_Type(TruthValue):
    """Custom type fsAceExtIfAnySourceMacAddrWildCard based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnySourceMacAddrWildCard_Type.__name__ = "TruthValue"
_FsAceExtIfAnySourceMacAddrWildCard_Object = MibTableColumn
fsAceExtIfAnySourceMacAddrWildCard = _FsAceExtIfAnySourceMacAddrWildCard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 40),
    _FsAceExtIfAnySourceMacAddrWildCard_Type()
)
fsAceExtIfAnySourceMacAddrWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtIfAnySourceMacAddrWildCard.setStatus("current")
_FsAceExtSourceMacAddrWildCard_Type = MacAddress
_FsAceExtSourceMacAddrWildCard_Object = MibTableColumn
fsAceExtSourceMacAddrWildCard = _FsAceExtSourceMacAddrWildCard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 41),
    _FsAceExtSourceMacAddrWildCard_Type()
)
fsAceExtSourceMacAddrWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtSourceMacAddrWildCard.setStatus("current")


class _FsAceExtIfAnyDestMacAddrWildCard_Type(TruthValue):
    """Custom type fsAceExtIfAnyDestMacAddrWildCard based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyDestMacAddrWildCard_Type.__name__ = "TruthValue"
_FsAceExtIfAnyDestMacAddrWildCard_Object = MibTableColumn
fsAceExtIfAnyDestMacAddrWildCard = _FsAceExtIfAnyDestMacAddrWildCard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 42),
    _FsAceExtIfAnyDestMacAddrWildCard_Type()
)
fsAceExtIfAnyDestMacAddrWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtIfAnyDestMacAddrWildCard.setStatus("current")
_FsAceExtDestMacAddrWildCard_Type = MacAddress
_FsAceExtDestMacAddrWildCard_Object = MibTableColumn
fsAceExtDestMacAddrWildCard = _FsAceExtDestMacAddrWildCard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 43),
    _FsAceExtDestMacAddrWildCard_Type()
)
fsAceExtDestMacAddrWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtDestMacAddrWildCard.setStatus("current")


class _FsAceExtIfAnySourceIp6_Type(TruthValue):
    """Custom type fsAceExtIfAnySourceIp6 based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnySourceIp6_Type.__name__ = "TruthValue"
_FsAceExtIfAnySourceIp6_Object = MibTableColumn
fsAceExtIfAnySourceIp6 = _FsAceExtIfAnySourceIp6_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 44),
    _FsAceExtIfAnySourceIp6_Type()
)
fsAceExtIfAnySourceIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtIfAnySourceIp6.setStatus("current")


class _FsAceExtSourceIp6_Type(OctetString):
    """Custom type fsAceExtSourceIp6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsAceExtSourceIp6_Type.__name__ = "OctetString"
_FsAceExtSourceIp6_Object = MibTableColumn
fsAceExtSourceIp6 = _FsAceExtSourceIp6_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 45),
    _FsAceExtSourceIp6_Type()
)
fsAceExtSourceIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtSourceIp6.setStatus("current")


class _FsAceExtIfAnySourceIp6WildCard_Type(TruthValue):
    """Custom type fsAceExtIfAnySourceIp6WildCard based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnySourceIp6WildCard_Type.__name__ = "TruthValue"
_FsAceExtIfAnySourceIp6WildCard_Object = MibTableColumn
fsAceExtIfAnySourceIp6WildCard = _FsAceExtIfAnySourceIp6WildCard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 46),
    _FsAceExtIfAnySourceIp6WildCard_Type()
)
fsAceExtIfAnySourceIp6WildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtIfAnySourceIp6WildCard.setStatus("current")


class _FsAceExtSourceIp6WildCard_Type(OctetString):
    """Custom type fsAceExtSourceIp6WildCard based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsAceExtSourceIp6WildCard_Type.__name__ = "OctetString"
_FsAceExtSourceIp6WildCard_Object = MibTableColumn
fsAceExtSourceIp6WildCard = _FsAceExtSourceIp6WildCard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 47),
    _FsAceExtSourceIp6WildCard_Type()
)
fsAceExtSourceIp6WildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtSourceIp6WildCard.setStatus("current")


class _FsAceExtIfAnyDestIp6_Type(TruthValue):
    """Custom type fsAceExtIfAnyDestIp6 based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyDestIp6_Type.__name__ = "TruthValue"
_FsAceExtIfAnyDestIp6_Object = MibTableColumn
fsAceExtIfAnyDestIp6 = _FsAceExtIfAnyDestIp6_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 48),
    _FsAceExtIfAnyDestIp6_Type()
)
fsAceExtIfAnyDestIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtIfAnyDestIp6.setStatus("current")


class _FsAceExtDestIp6_Type(OctetString):
    """Custom type fsAceExtDestIp6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsAceExtDestIp6_Type.__name__ = "OctetString"
_FsAceExtDestIp6_Object = MibTableColumn
fsAceExtDestIp6 = _FsAceExtDestIp6_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 49),
    _FsAceExtDestIp6_Type()
)
fsAceExtDestIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtDestIp6.setStatus("current")


class _FsAceExtIfAnyDestIp6WildCard_Type(TruthValue):
    """Custom type fsAceExtIfAnyDestIp6WildCard based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyDestIp6WildCard_Type.__name__ = "TruthValue"
_FsAceExtIfAnyDestIp6WildCard_Object = MibTableColumn
fsAceExtIfAnyDestIp6WildCard = _FsAceExtIfAnyDestIp6WildCard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 50),
    _FsAceExtIfAnyDestIp6WildCard_Type()
)
fsAceExtIfAnyDestIp6WildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtIfAnyDestIp6WildCard.setStatus("current")


class _FsAceExtDestIp6WildCard_Type(OctetString):
    """Custom type fsAceExtDestIp6WildCard based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsAceExtDestIp6WildCard_Type.__name__ = "OctetString"
_FsAceExtDestIp6WildCard_Object = MibTableColumn
fsAceExtDestIp6WildCard = _FsAceExtDestIp6WildCard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 1, 4, 1, 51),
    _FsAceExtDestIp6WildCard_Type()
)
fsAceExtDestIp6WildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAceExtDestIp6WildCard.setStatus("current")
_FsAclMIBConformance_ObjectIdentity = ObjectIdentity
fsAclMIBConformance = _FsAclMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 2)
)
_FsAclMIBCompliances_ObjectIdentity = ObjectIdentity
fsAclMIBCompliances = _FsAclMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 2, 1)
)
_FsAclMIBGroups_ObjectIdentity = ObjectIdentity
fsAclMIBGroups = _FsAclMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 2, 2)
)

# Managed Objects groups

fsAclMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 2, 2, 1)
)
fsAclMIBGroup.setObjects(
      *(("FS-ACL-MIB", "fsAclName"),
        ("FS-ACL-MIB", "fsAclMode"),
        ("FS-ACL-MIB", "fsAclEntryStatus"),
        ("FS-ACL-MIB", "fsAceExtAclName"),
        ("FS-ACL-MIB", "fsAceExtIndex"),
        ("FS-ACL-MIB", "fsAceExtIfAnyVID"),
        ("FS-ACL-MIB", "fsAceExtVID"),
        ("FS-ACL-MIB", "fsAceExtIfAnySourceIp"),
        ("FS-ACL-MIB", "fsAceExtSourceIp"),
        ("FS-ACL-MIB", "fsAceExtIfAnySourceWildCard"),
        ("FS-ACL-MIB", "fsAceExtSourceWildCard"),
        ("FS-ACL-MIB", "fsAceExtIfAnySourceMacAddr"),
        ("FS-ACL-MIB", "fsAceExtSourceMacAddr"),
        ("FS-ACL-MIB", "fsAceExtIfAnyDestIp"),
        ("FS-ACL-MIB", "fsAceExtDestIp"),
        ("FS-ACL-MIB", "fsAceExtIfAnyDestWildCard"),
        ("FS-ACL-MIB", "fsAceExtDestIpWildCard"),
        ("FS-ACL-MIB", "fsAceExtIfAnyDestMacAddr"),
        ("FS-ACL-MIB", "fsAceExtDestMacAddr"),
        ("FS-ACL-MIB", "fsAceExtIfAnyEtherLikeType"),
        ("FS-ACL-MIB", "fsAceExtEtherLikeType"),
        ("FS-ACL-MIB", "fsAceExtIfAnyIpProtocolField"),
        ("FS-ACL-MIB", "fsAceExtIpProtocolField"),
        ("FS-ACL-MIB", "fsAceExtSourceProtocolPort"),
        ("FS-ACL-MIB", "fsAceExtDestProtocolPort"),
        ("FS-ACL-MIB", "fsAceExtProtocolType"),
        ("FS-ACL-MIB", "fsAceExtProtocolType"),
        ("FS-ACL-MIB", "fsAceExtFlowAction"),
        ("FS-ACL-MIB", "fsAceExtEntryStauts"),
        ("FS-ACL-MIB", "fsAceExtTimeRangeName"),
        ("FS-ACL-MIB", "fsAceExtSourcePortOp"),
        ("FS-ACL-MIB", "fsAceExtSourceProtocolPortRange"),
        ("FS-ACL-MIB", "fsAceExtDestPortOp"),
        ("FS-ACL-MIB", "fsAceExtDestProtocolPortRange"),
        ("FS-ACL-MIB", "fsAceExtIfAnyCos"),
        ("FS-ACL-MIB", "fsAceExtCos"),
        ("FS-ACL-MIB", "fsAceExtIfAnyIpPrec"),
        ("FS-ACL-MIB", "fsAceExtIpPrec"),
        ("FS-ACL-MIB", "fsAceExtIfAnyDscp"),
        ("FS-ACL-MIB", "fsAceExtDscp"),
        ("FS-ACL-MIB", "fsAceExtIfAnyTcpFlag"),
        ("FS-ACL-MIB", "fsAceExtTcpFlag"),
        ("FS-ACL-MIB", "fsAceExtIfAnySourceMacAddrWildCard"),
        ("FS-ACL-MIB", "fsAceExtSourceMacAddrWildCard"),
        ("FS-ACL-MIB", "fsAceExtIfAnyDestMacAddrWildCard"),
        ("FS-ACL-MIB", "fsAceExtDestMacAddrWildCard"),
        ("FS-ACL-MIB", "fsAceExtIfAnySourceIp6"),
        ("FS-ACL-MIB", "fsAceExtSourceIp6"),
        ("FS-ACL-MIB", "fsAceExtIfAnySourceIp6WildCard"),
        ("FS-ACL-MIB", "fsAceExtSourceIp6WildCard"),
        ("FS-ACL-MIB", "fsAceExtIfAnyDestIp6"),
        ("FS-ACL-MIB", "fsAceExtDestIp6"),
        ("FS-ACL-MIB", "fsAceExtIfAnyDestIp6WildCard"),
        ("FS-ACL-MIB", "fsAceExtDestIp6WildCard"),
        ("FS-ACL-MIB", "fsAclIfIndex"),
        ("FS-ACL-MIB", "fsAclIfMaxEntryNum"),
        ("FS-ACL-MIB", "fsAclIfCurruntEntryNum"),
        ("FS-ACL-MIB", "fsIfInAclName"),
        ("FS-ACL-MIB", "fsIfOutAclName"))
)
if mibBuilder.loadTexts:
    fsAclMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsAclMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 17, 2, 1, 1)
)
fsAclMIBCompliance.setObjects(
    ("FS-ACL-MIB", "fsAclMIBGroup")
)
if mibBuilder.loadTexts:
    fsAclMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-ACL-MIB",
    **{"fsAclMIB": fsAclMIB,
       "fsAclMIBObjects": fsAclMIBObjects,
       "fsAclTable": fsAclTable,
       "fsAclEntry": fsAclEntry,
       "fsAclName": fsAclName,
       "fsAclMode": fsAclMode,
       "fsAclEntryStatus": fsAclEntryStatus,
       "fsAclIfTable": fsAclIfTable,
       "fsAclIfEntry": fsAclIfEntry,
       "fsAclIfIndex": fsAclIfIndex,
       "fsAclIfMaxEntryNum": fsAclIfMaxEntryNum,
       "fsAclIfCurruntEntryNum": fsAclIfCurruntEntryNum,
       "fsIfInAclName": fsIfInAclName,
       "fsIfOutAclName": fsIfOutAclName,
       "fsAclIf6MaxEntryNum": fsAclIf6MaxEntryNum,
       "fsAclIf6CurruntEntryNum": fsAclIf6CurruntEntryNum,
       "fsIf6InAclName": fsIf6InAclName,
       "fsIf6OutAclName": fsIf6OutAclName,
       "fsAceExtTable": fsAceExtTable,
       "fsAceExtEntry": fsAceExtEntry,
       "fsAceExtAclName": fsAceExtAclName,
       "fsAceExtIndex": fsAceExtIndex,
       "fsAceExtIfAnyVID": fsAceExtIfAnyVID,
       "fsAceExtVID": fsAceExtVID,
       "fsAceExtIfAnySourceIp": fsAceExtIfAnySourceIp,
       "fsAceExtSourceIp": fsAceExtSourceIp,
       "fsAceExtIfAnySourceWildCard": fsAceExtIfAnySourceWildCard,
       "fsAceExtSourceWildCard": fsAceExtSourceWildCard,
       "fsAceExtIfAnySourceMacAddr": fsAceExtIfAnySourceMacAddr,
       "fsAceExtSourceMacAddr": fsAceExtSourceMacAddr,
       "fsAceExtIfAnyDestIp": fsAceExtIfAnyDestIp,
       "fsAceExtDestIp": fsAceExtDestIp,
       "fsAceExtIfAnyDestWildCard": fsAceExtIfAnyDestWildCard,
       "fsAceExtDestIpWildCard": fsAceExtDestIpWildCard,
       "fsAceExtIfAnyDestMacAddr": fsAceExtIfAnyDestMacAddr,
       "fsAceExtDestMacAddr": fsAceExtDestMacAddr,
       "fsAceExtIfAnyEtherLikeType": fsAceExtIfAnyEtherLikeType,
       "fsAceExtEtherLikeType": fsAceExtEtherLikeType,
       "fsAceExtIfAnyIpProtocolField": fsAceExtIfAnyIpProtocolField,
       "fsAceExtIpProtocolField": fsAceExtIpProtocolField,
       "fsAceExtSourceProtocolPort": fsAceExtSourceProtocolPort,
       "fsAceExtDestProtocolPort": fsAceExtDestProtocolPort,
       "fsAceExtIfAnyProtocolType": fsAceExtIfAnyProtocolType,
       "fsAceExtProtocolType": fsAceExtProtocolType,
       "fsAceExtFlowAction": fsAceExtFlowAction,
       "fsAceExtEntryStauts": fsAceExtEntryStauts,
       "fsAceExtTimeRangeName": fsAceExtTimeRangeName,
       "fsAceExtSourcePortOp": fsAceExtSourcePortOp,
       "fsAceExtSourceProtocolPortRange": fsAceExtSourceProtocolPortRange,
       "fsAceExtDestPortOp": fsAceExtDestPortOp,
       "fsAceExtDestProtocolPortRange": fsAceExtDestProtocolPortRange,
       "fsAceExtIfAnyCos": fsAceExtIfAnyCos,
       "fsAceExtCos": fsAceExtCos,
       "fsAceExtIfAnyIpPrec": fsAceExtIfAnyIpPrec,
       "fsAceExtIpPrec": fsAceExtIpPrec,
       "fsAceExtIfAnyDscp": fsAceExtIfAnyDscp,
       "fsAceExtDscp": fsAceExtDscp,
       "fsAceExtIfAnyTcpFlag": fsAceExtIfAnyTcpFlag,
       "fsAceExtTcpFlag": fsAceExtTcpFlag,
       "fsAceExtIfAnySourceMacAddrWildCard": fsAceExtIfAnySourceMacAddrWildCard,
       "fsAceExtSourceMacAddrWildCard": fsAceExtSourceMacAddrWildCard,
       "fsAceExtIfAnyDestMacAddrWildCard": fsAceExtIfAnyDestMacAddrWildCard,
       "fsAceExtDestMacAddrWildCard": fsAceExtDestMacAddrWildCard,
       "fsAceExtIfAnySourceIp6": fsAceExtIfAnySourceIp6,
       "fsAceExtSourceIp6": fsAceExtSourceIp6,
       "fsAceExtIfAnySourceIp6WildCard": fsAceExtIfAnySourceIp6WildCard,
       "fsAceExtSourceIp6WildCard": fsAceExtSourceIp6WildCard,
       "fsAceExtIfAnyDestIp6": fsAceExtIfAnyDestIp6,
       "fsAceExtDestIp6": fsAceExtDestIp6,
       "fsAceExtIfAnyDestIp6WildCard": fsAceExtIfAnyDestIp6WildCard,
       "fsAceExtDestIp6WildCard": fsAceExtDestIp6WildCard,
       "fsAclMIBConformance": fsAclMIBConformance,
       "fsAclMIBCompliances": fsAclMIBCompliances,
       "fsAclMIBCompliance": fsAclMIBCompliance,
       "fsAclMIBGroups": fsAclMIBGroups,
       "fsAclMIBGroup": fsAclMIBGroup}
)
