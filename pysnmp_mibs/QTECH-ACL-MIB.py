# SNMP MIB module (QTECH-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-ACL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:26 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "QTECH-TC",
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

qtechAclMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17)
)
if mibBuilder.loadTexts:
    qtechAclMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechAclMIBObjects_ObjectIdentity = ObjectIdentity
qtechAclMIBObjects = _QtechAclMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1)
)
_QtechAclTable_Object = MibTable
qtechAclTable = _QtechAclTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 1)
)
if mibBuilder.loadTexts:
    qtechAclTable.setStatus("current")
_QtechAclEntry_Object = MibTableRow
qtechAclEntry = _QtechAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 1, 1)
)
qtechAclEntry.setIndexNames(
    (0, "QTECH-ACL-MIB", "qtechAclName"),
)
if mibBuilder.loadTexts:
    qtechAclEntry.setStatus("current")


class _QtechAclName_Type(DisplayString):
    """Custom type qtechAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechAclName_Type.__name__ = "DisplayString"
_QtechAclName_Object = MibTableColumn
qtechAclName = _QtechAclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 1, 1, 1),
    _QtechAclName_Type()
)
qtechAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAclName.setStatus("current")


class _QtechAclMode_Type(Integer32):
    """Custom type qtechAclMode based on Integer32"""
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


_QtechAclMode_Type.__name__ = "Integer32"
_QtechAclMode_Object = MibTableColumn
qtechAclMode = _QtechAclMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 1, 1, 2),
    _QtechAclMode_Type()
)
qtechAclMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAclMode.setStatus("current")
_QtechAclEntryStatus_Type = ConfigStatus
_QtechAclEntryStatus_Object = MibTableColumn
qtechAclEntryStatus = _QtechAclEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 1, 1, 3),
    _QtechAclEntryStatus_Type()
)
qtechAclEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAclEntryStatus.setStatus("current")
_QtechAclIfTable_Object = MibTable
qtechAclIfTable = _QtechAclIfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 3)
)
if mibBuilder.loadTexts:
    qtechAclIfTable.setStatus("current")
_QtechAclIfEntry_Object = MibTableRow
qtechAclIfEntry = _QtechAclIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 3, 1)
)
qtechAclIfEntry.setIndexNames(
    (0, "QTECH-ACL-MIB", "qtechAclIfIndex"),
)
if mibBuilder.loadTexts:
    qtechAclIfEntry.setStatus("current")
_QtechAclIfIndex_Type = IfIndex
_QtechAclIfIndex_Object = MibTableColumn
qtechAclIfIndex = _QtechAclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 3, 1, 1),
    _QtechAclIfIndex_Type()
)
qtechAclIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAclIfIndex.setStatus("current")
_QtechAclIfMaxEntryNum_Type = Integer32
_QtechAclIfMaxEntryNum_Object = MibTableColumn
qtechAclIfMaxEntryNum = _QtechAclIfMaxEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 3, 1, 2),
    _QtechAclIfMaxEntryNum_Type()
)
qtechAclIfMaxEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAclIfMaxEntryNum.setStatus("current")
_QtechAclIfCurruntEntryNum_Type = Integer32
_QtechAclIfCurruntEntryNum_Object = MibTableColumn
qtechAclIfCurruntEntryNum = _QtechAclIfCurruntEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 3, 1, 3),
    _QtechAclIfCurruntEntryNum_Type()
)
qtechAclIfCurruntEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAclIfCurruntEntryNum.setStatus("current")


class _QtechIfInAclName_Type(DisplayString):
    """Custom type qtechIfInAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechIfInAclName_Type.__name__ = "DisplayString"
_QtechIfInAclName_Object = MibTableColumn
qtechIfInAclName = _QtechIfInAclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 3, 1, 4),
    _QtechIfInAclName_Type()
)
qtechIfInAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfInAclName.setStatus("current")


class _QtechIfOutAclName_Type(DisplayString):
    """Custom type qtechIfOutAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechIfOutAclName_Type.__name__ = "DisplayString"
_QtechIfOutAclName_Object = MibTableColumn
qtechIfOutAclName = _QtechIfOutAclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 3, 1, 5),
    _QtechIfOutAclName_Type()
)
qtechIfOutAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfOutAclName.setStatus("current")
_QtechAclIf6MaxEntryNum_Type = Integer32
_QtechAclIf6MaxEntryNum_Object = MibTableColumn
qtechAclIf6MaxEntryNum = _QtechAclIf6MaxEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 3, 1, 6),
    _QtechAclIf6MaxEntryNum_Type()
)
qtechAclIf6MaxEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAclIf6MaxEntryNum.setStatus("current")
_QtechAclIf6CurruntEntryNum_Type = Integer32
_QtechAclIf6CurruntEntryNum_Object = MibTableColumn
qtechAclIf6CurruntEntryNum = _QtechAclIf6CurruntEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 3, 1, 7),
    _QtechAclIf6CurruntEntryNum_Type()
)
qtechAclIf6CurruntEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAclIf6CurruntEntryNum.setStatus("current")


class _QtechIf6InAclName_Type(DisplayString):
    """Custom type qtechIf6InAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechIf6InAclName_Type.__name__ = "DisplayString"
_QtechIf6InAclName_Object = MibTableColumn
qtechIf6InAclName = _QtechIf6InAclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 3, 1, 8),
    _QtechIf6InAclName_Type()
)
qtechIf6InAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIf6InAclName.setStatus("current")


class _QtechIf6OutAclName_Type(DisplayString):
    """Custom type qtechIf6OutAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechIf6OutAclName_Type.__name__ = "DisplayString"
_QtechIf6OutAclName_Object = MibTableColumn
qtechIf6OutAclName = _QtechIf6OutAclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 3, 1, 9),
    _QtechIf6OutAclName_Type()
)
qtechIf6OutAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIf6OutAclName.setStatus("current")
_QtechAceExtTable_Object = MibTable
qtechAceExtTable = _QtechAceExtTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4)
)
if mibBuilder.loadTexts:
    qtechAceExtTable.setStatus("current")
_QtechAceExtEntry_Object = MibTableRow
qtechAceExtEntry = _QtechAceExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1)
)
qtechAceExtEntry.setIndexNames(
    (0, "QTECH-ACL-MIB", "qtechAceExtAclName"),
    (0, "QTECH-ACL-MIB", "qtechAceExtIndex"),
)
if mibBuilder.loadTexts:
    qtechAceExtEntry.setStatus("current")


class _QtechAceExtAclName_Type(DisplayString):
    """Custom type qtechAceExtAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechAceExtAclName_Type.__name__ = "DisplayString"
_QtechAceExtAclName_Object = MibTableColumn
qtechAceExtAclName = _QtechAceExtAclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 1),
    _QtechAceExtAclName_Type()
)
qtechAceExtAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAceExtAclName.setStatus("current")


class _QtechAceExtIndex_Type(Integer32):
    """Custom type qtechAceExtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechAceExtIndex_Type.__name__ = "Integer32"
_QtechAceExtIndex_Object = MibTableColumn
qtechAceExtIndex = _QtechAceExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 2),
    _QtechAceExtIndex_Type()
)
qtechAceExtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAceExtIndex.setStatus("current")


class _QtechAceExtIfAnyVID_Type(TruthValue):
    """Custom type qtechAceExtIfAnyVID based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyVID_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyVID_Object = MibTableColumn
qtechAceExtIfAnyVID = _QtechAceExtIfAnyVID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 3),
    _QtechAceExtIfAnyVID_Type()
)
qtechAceExtIfAnyVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyVID.setStatus("current")


class _QtechAceExtVID_Type(Unsigned32):
    """Custom type qtechAceExtVID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_QtechAceExtVID_Type.__name__ = "Unsigned32"
_QtechAceExtVID_Object = MibTableColumn
qtechAceExtVID = _QtechAceExtVID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 4),
    _QtechAceExtVID_Type()
)
qtechAceExtVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtVID.setStatus("current")


class _QtechAceExtIfAnySourceIp_Type(TruthValue):
    """Custom type qtechAceExtIfAnySourceIp based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnySourceIp_Type.__name__ = "TruthValue"
_QtechAceExtIfAnySourceIp_Object = MibTableColumn
qtechAceExtIfAnySourceIp = _QtechAceExtIfAnySourceIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 5),
    _QtechAceExtIfAnySourceIp_Type()
)
qtechAceExtIfAnySourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnySourceIp.setStatus("current")
_QtechAceExtSourceIp_Type = IpAddress
_QtechAceExtSourceIp_Object = MibTableColumn
qtechAceExtSourceIp = _QtechAceExtSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 6),
    _QtechAceExtSourceIp_Type()
)
qtechAceExtSourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtSourceIp.setStatus("current")


class _QtechAceExtIfAnySourceWildCard_Type(TruthValue):
    """Custom type qtechAceExtIfAnySourceWildCard based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnySourceWildCard_Type.__name__ = "TruthValue"
_QtechAceExtIfAnySourceWildCard_Object = MibTableColumn
qtechAceExtIfAnySourceWildCard = _QtechAceExtIfAnySourceWildCard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 7),
    _QtechAceExtIfAnySourceWildCard_Type()
)
qtechAceExtIfAnySourceWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnySourceWildCard.setStatus("current")
_QtechAceExtSourceWildCard_Type = IpAddress
_QtechAceExtSourceWildCard_Object = MibTableColumn
qtechAceExtSourceWildCard = _QtechAceExtSourceWildCard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 8),
    _QtechAceExtSourceWildCard_Type()
)
qtechAceExtSourceWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtSourceWildCard.setStatus("current")


class _QtechAceExtIfAnySourceMacAddr_Type(TruthValue):
    """Custom type qtechAceExtIfAnySourceMacAddr based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnySourceMacAddr_Type.__name__ = "TruthValue"
_QtechAceExtIfAnySourceMacAddr_Object = MibTableColumn
qtechAceExtIfAnySourceMacAddr = _QtechAceExtIfAnySourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 9),
    _QtechAceExtIfAnySourceMacAddr_Type()
)
qtechAceExtIfAnySourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnySourceMacAddr.setStatus("current")
_QtechAceExtSourceMacAddr_Type = MacAddress
_QtechAceExtSourceMacAddr_Object = MibTableColumn
qtechAceExtSourceMacAddr = _QtechAceExtSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 10),
    _QtechAceExtSourceMacAddr_Type()
)
qtechAceExtSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtSourceMacAddr.setStatus("current")


class _QtechAceExtIfAnyDestIp_Type(TruthValue):
    """Custom type qtechAceExtIfAnyDestIp based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyDestIp_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyDestIp_Object = MibTableColumn
qtechAceExtIfAnyDestIp = _QtechAceExtIfAnyDestIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 11),
    _QtechAceExtIfAnyDestIp_Type()
)
qtechAceExtIfAnyDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyDestIp.setStatus("current")
_QtechAceExtDestIp_Type = IpAddress
_QtechAceExtDestIp_Object = MibTableColumn
qtechAceExtDestIp = _QtechAceExtDestIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 12),
    _QtechAceExtDestIp_Type()
)
qtechAceExtDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtDestIp.setStatus("current")


class _QtechAceExtIfAnyDestWildCard_Type(TruthValue):
    """Custom type qtechAceExtIfAnyDestWildCard based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyDestWildCard_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyDestWildCard_Object = MibTableColumn
qtechAceExtIfAnyDestWildCard = _QtechAceExtIfAnyDestWildCard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 13),
    _QtechAceExtIfAnyDestWildCard_Type()
)
qtechAceExtIfAnyDestWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyDestWildCard.setStatus("current")
_QtechAceExtDestIpWildCard_Type = IpAddress
_QtechAceExtDestIpWildCard_Object = MibTableColumn
qtechAceExtDestIpWildCard = _QtechAceExtDestIpWildCard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 14),
    _QtechAceExtDestIpWildCard_Type()
)
qtechAceExtDestIpWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtDestIpWildCard.setStatus("current")


class _QtechAceExtIfAnyDestMacAddr_Type(TruthValue):
    """Custom type qtechAceExtIfAnyDestMacAddr based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyDestMacAddr_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyDestMacAddr_Object = MibTableColumn
qtechAceExtIfAnyDestMacAddr = _QtechAceExtIfAnyDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 15),
    _QtechAceExtIfAnyDestMacAddr_Type()
)
qtechAceExtIfAnyDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyDestMacAddr.setStatus("current")
_QtechAceExtDestMacAddr_Type = MacAddress
_QtechAceExtDestMacAddr_Object = MibTableColumn
qtechAceExtDestMacAddr = _QtechAceExtDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 16),
    _QtechAceExtDestMacAddr_Type()
)
qtechAceExtDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtDestMacAddr.setStatus("current")


class _QtechAceExtIfAnyEtherLikeType_Type(TruthValue):
    """Custom type qtechAceExtIfAnyEtherLikeType based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyEtherLikeType_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyEtherLikeType_Object = MibTableColumn
qtechAceExtIfAnyEtherLikeType = _QtechAceExtIfAnyEtherLikeType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 17),
    _QtechAceExtIfAnyEtherLikeType_Type()
)
qtechAceExtIfAnyEtherLikeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyEtherLikeType.setStatus("current")
_QtechAceExtEtherLikeType_Type = Integer32
_QtechAceExtEtherLikeType_Object = MibTableColumn
qtechAceExtEtherLikeType = _QtechAceExtEtherLikeType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 18),
    _QtechAceExtEtherLikeType_Type()
)
qtechAceExtEtherLikeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtEtherLikeType.setStatus("current")


class _QtechAceExtIfAnyIpProtocolField_Type(TruthValue):
    """Custom type qtechAceExtIfAnyIpProtocolField based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyIpProtocolField_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyIpProtocolField_Object = MibTableColumn
qtechAceExtIfAnyIpProtocolField = _QtechAceExtIfAnyIpProtocolField_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 19),
    _QtechAceExtIfAnyIpProtocolField_Type()
)
qtechAceExtIfAnyIpProtocolField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyIpProtocolField.setStatus("current")
_QtechAceExtIpProtocolField_Type = Integer32
_QtechAceExtIpProtocolField_Object = MibTableColumn
qtechAceExtIpProtocolField = _QtechAceExtIpProtocolField_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 20),
    _QtechAceExtIpProtocolField_Type()
)
qtechAceExtIpProtocolField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIpProtocolField.setStatus("current")
_QtechAceExtSourceProtocolPort_Type = Integer32
_QtechAceExtSourceProtocolPort_Object = MibTableColumn
qtechAceExtSourceProtocolPort = _QtechAceExtSourceProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 21),
    _QtechAceExtSourceProtocolPort_Type()
)
qtechAceExtSourceProtocolPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtSourceProtocolPort.setStatus("current")
_QtechAceExtDestProtocolPort_Type = Integer32
_QtechAceExtDestProtocolPort_Object = MibTableColumn
qtechAceExtDestProtocolPort = _QtechAceExtDestProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 22),
    _QtechAceExtDestProtocolPort_Type()
)
qtechAceExtDestProtocolPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtDestProtocolPort.setStatus("current")


class _QtechAceExtIfAnyProtocolType_Type(TruthValue):
    """Custom type qtechAceExtIfAnyProtocolType based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyProtocolType_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyProtocolType_Object = MibTableColumn
qtechAceExtIfAnyProtocolType = _QtechAceExtIfAnyProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 23),
    _QtechAceExtIfAnyProtocolType_Type()
)
qtechAceExtIfAnyProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyProtocolType.setStatus("current")
_QtechAceExtProtocolType_Type = Integer32
_QtechAceExtProtocolType_Object = MibTableColumn
qtechAceExtProtocolType = _QtechAceExtProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 24),
    _QtechAceExtProtocolType_Type()
)
qtechAceExtProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtProtocolType.setStatus("current")


class _QtechAceExtFlowAction_Type(Integer32):
    """Custom type qtechAceExtFlowAction based on Integer32"""
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


_QtechAceExtFlowAction_Type.__name__ = "Integer32"
_QtechAceExtFlowAction_Object = MibTableColumn
qtechAceExtFlowAction = _QtechAceExtFlowAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 25),
    _QtechAceExtFlowAction_Type()
)
qtechAceExtFlowAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtFlowAction.setStatus("current")
_QtechAceExtEntryStauts_Type = RowStatus
_QtechAceExtEntryStauts_Object = MibTableColumn
qtechAceExtEntryStauts = _QtechAceExtEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 26),
    _QtechAceExtEntryStauts_Type()
)
qtechAceExtEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtEntryStauts.setStatus("current")


class _QtechAceExtTimeRangeName_Type(DisplayString):
    """Custom type qtechAceExtTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechAceExtTimeRangeName_Type.__name__ = "DisplayString"
_QtechAceExtTimeRangeName_Object = MibTableColumn
qtechAceExtTimeRangeName = _QtechAceExtTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 27),
    _QtechAceExtTimeRangeName_Type()
)
qtechAceExtTimeRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtTimeRangeName.setStatus("current")


class _QtechAceExtSourcePortOp_Type(Integer32):
    """Custom type qtechAceExtSourcePortOp based on Integer32"""
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


_QtechAceExtSourcePortOp_Type.__name__ = "Integer32"
_QtechAceExtSourcePortOp_Object = MibTableColumn
qtechAceExtSourcePortOp = _QtechAceExtSourcePortOp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 28),
    _QtechAceExtSourcePortOp_Type()
)
qtechAceExtSourcePortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtSourcePortOp.setStatus("current")
_QtechAceExtSourceProtocolPortRange_Type = Integer32
_QtechAceExtSourceProtocolPortRange_Object = MibTableColumn
qtechAceExtSourceProtocolPortRange = _QtechAceExtSourceProtocolPortRange_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 29),
    _QtechAceExtSourceProtocolPortRange_Type()
)
qtechAceExtSourceProtocolPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtSourceProtocolPortRange.setStatus("current")


class _QtechAceExtDestPortOp_Type(Integer32):
    """Custom type qtechAceExtDestPortOp based on Integer32"""
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


_QtechAceExtDestPortOp_Type.__name__ = "Integer32"
_QtechAceExtDestPortOp_Object = MibTableColumn
qtechAceExtDestPortOp = _QtechAceExtDestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 30),
    _QtechAceExtDestPortOp_Type()
)
qtechAceExtDestPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtDestPortOp.setStatus("current")
_QtechAceExtDestProtocolPortRange_Type = Integer32
_QtechAceExtDestProtocolPortRange_Object = MibTableColumn
qtechAceExtDestProtocolPortRange = _QtechAceExtDestProtocolPortRange_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 31),
    _QtechAceExtDestProtocolPortRange_Type()
)
qtechAceExtDestProtocolPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtDestProtocolPortRange.setStatus("current")


class _QtechAceExtIfAnyCos_Type(TruthValue):
    """Custom type qtechAceExtIfAnyCos based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyCos_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyCos_Object = MibTableColumn
qtechAceExtIfAnyCos = _QtechAceExtIfAnyCos_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 32),
    _QtechAceExtIfAnyCos_Type()
)
qtechAceExtIfAnyCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyCos.setStatus("current")
_QtechAceExtCos_Type = Integer32
_QtechAceExtCos_Object = MibTableColumn
qtechAceExtCos = _QtechAceExtCos_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 33),
    _QtechAceExtCos_Type()
)
qtechAceExtCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtCos.setStatus("current")


class _QtechAceExtIfAnyIpPrec_Type(TruthValue):
    """Custom type qtechAceExtIfAnyIpPrec based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyIpPrec_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyIpPrec_Object = MibTableColumn
qtechAceExtIfAnyIpPrec = _QtechAceExtIfAnyIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 34),
    _QtechAceExtIfAnyIpPrec_Type()
)
qtechAceExtIfAnyIpPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyIpPrec.setStatus("current")
_QtechAceExtIpPrec_Type = Integer32
_QtechAceExtIpPrec_Object = MibTableColumn
qtechAceExtIpPrec = _QtechAceExtIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 35),
    _QtechAceExtIpPrec_Type()
)
qtechAceExtIpPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtIpPrec.setStatus("current")


class _QtechAceExtIfAnyDscp_Type(TruthValue):
    """Custom type qtechAceExtIfAnyDscp based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyDscp_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyDscp_Object = MibTableColumn
qtechAceExtIfAnyDscp = _QtechAceExtIfAnyDscp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 36),
    _QtechAceExtIfAnyDscp_Type()
)
qtechAceExtIfAnyDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyDscp.setStatus("current")
_QtechAceExtDscp_Type = Integer32
_QtechAceExtDscp_Object = MibTableColumn
qtechAceExtDscp = _QtechAceExtDscp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 37),
    _QtechAceExtDscp_Type()
)
qtechAceExtDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtDscp.setStatus("current")


class _QtechAceExtIfAnyTcpFlag_Type(TruthValue):
    """Custom type qtechAceExtIfAnyTcpFlag based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyTcpFlag_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyTcpFlag_Object = MibTableColumn
qtechAceExtIfAnyTcpFlag = _QtechAceExtIfAnyTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 38),
    _QtechAceExtIfAnyTcpFlag_Type()
)
qtechAceExtIfAnyTcpFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyTcpFlag.setStatus("current")
_QtechAceExtTcpFlag_Type = Integer32
_QtechAceExtTcpFlag_Object = MibTableColumn
qtechAceExtTcpFlag = _QtechAceExtTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 39),
    _QtechAceExtTcpFlag_Type()
)
qtechAceExtTcpFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtTcpFlag.setStatus("current")


class _QtechAceExtIfAnySourceMacAddrWildCard_Type(TruthValue):
    """Custom type qtechAceExtIfAnySourceMacAddrWildCard based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnySourceMacAddrWildCard_Type.__name__ = "TruthValue"
_QtechAceExtIfAnySourceMacAddrWildCard_Object = MibTableColumn
qtechAceExtIfAnySourceMacAddrWildCard = _QtechAceExtIfAnySourceMacAddrWildCard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 40),
    _QtechAceExtIfAnySourceMacAddrWildCard_Type()
)
qtechAceExtIfAnySourceMacAddrWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtIfAnySourceMacAddrWildCard.setStatus("current")
_QtechAceExtSourceMacAddrWildCard_Type = MacAddress
_QtechAceExtSourceMacAddrWildCard_Object = MibTableColumn
qtechAceExtSourceMacAddrWildCard = _QtechAceExtSourceMacAddrWildCard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 41),
    _QtechAceExtSourceMacAddrWildCard_Type()
)
qtechAceExtSourceMacAddrWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtSourceMacAddrWildCard.setStatus("current")


class _QtechAceExtIfAnyDestMacAddrWildCard_Type(TruthValue):
    """Custom type qtechAceExtIfAnyDestMacAddrWildCard based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyDestMacAddrWildCard_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyDestMacAddrWildCard_Object = MibTableColumn
qtechAceExtIfAnyDestMacAddrWildCard = _QtechAceExtIfAnyDestMacAddrWildCard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 42),
    _QtechAceExtIfAnyDestMacAddrWildCard_Type()
)
qtechAceExtIfAnyDestMacAddrWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyDestMacAddrWildCard.setStatus("current")
_QtechAceExtDestMacAddrWildCard_Type = MacAddress
_QtechAceExtDestMacAddrWildCard_Object = MibTableColumn
qtechAceExtDestMacAddrWildCard = _QtechAceExtDestMacAddrWildCard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 43),
    _QtechAceExtDestMacAddrWildCard_Type()
)
qtechAceExtDestMacAddrWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtDestMacAddrWildCard.setStatus("current")


class _QtechAceExtIfAnySourceIp6_Type(TruthValue):
    """Custom type qtechAceExtIfAnySourceIp6 based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnySourceIp6_Type.__name__ = "TruthValue"
_QtechAceExtIfAnySourceIp6_Object = MibTableColumn
qtechAceExtIfAnySourceIp6 = _QtechAceExtIfAnySourceIp6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 44),
    _QtechAceExtIfAnySourceIp6_Type()
)
qtechAceExtIfAnySourceIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtIfAnySourceIp6.setStatus("current")


class _QtechAceExtSourceIp6_Type(OctetString):
    """Custom type qtechAceExtSourceIp6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_QtechAceExtSourceIp6_Type.__name__ = "OctetString"
_QtechAceExtSourceIp6_Object = MibTableColumn
qtechAceExtSourceIp6 = _QtechAceExtSourceIp6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 45),
    _QtechAceExtSourceIp6_Type()
)
qtechAceExtSourceIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtSourceIp6.setStatus("current")


class _QtechAceExtIfAnySourceIp6WildCard_Type(TruthValue):
    """Custom type qtechAceExtIfAnySourceIp6WildCard based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnySourceIp6WildCard_Type.__name__ = "TruthValue"
_QtechAceExtIfAnySourceIp6WildCard_Object = MibTableColumn
qtechAceExtIfAnySourceIp6WildCard = _QtechAceExtIfAnySourceIp6WildCard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 46),
    _QtechAceExtIfAnySourceIp6WildCard_Type()
)
qtechAceExtIfAnySourceIp6WildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtIfAnySourceIp6WildCard.setStatus("current")


class _QtechAceExtSourceIp6WildCard_Type(OctetString):
    """Custom type qtechAceExtSourceIp6WildCard based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_QtechAceExtSourceIp6WildCard_Type.__name__ = "OctetString"
_QtechAceExtSourceIp6WildCard_Object = MibTableColumn
qtechAceExtSourceIp6WildCard = _QtechAceExtSourceIp6WildCard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 47),
    _QtechAceExtSourceIp6WildCard_Type()
)
qtechAceExtSourceIp6WildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtSourceIp6WildCard.setStatus("current")


class _QtechAceExtIfAnyDestIp6_Type(TruthValue):
    """Custom type qtechAceExtIfAnyDestIp6 based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyDestIp6_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyDestIp6_Object = MibTableColumn
qtechAceExtIfAnyDestIp6 = _QtechAceExtIfAnyDestIp6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 48),
    _QtechAceExtIfAnyDestIp6_Type()
)
qtechAceExtIfAnyDestIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyDestIp6.setStatus("current")


class _QtechAceExtDestIp6_Type(OctetString):
    """Custom type qtechAceExtDestIp6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_QtechAceExtDestIp6_Type.__name__ = "OctetString"
_QtechAceExtDestIp6_Object = MibTableColumn
qtechAceExtDestIp6 = _QtechAceExtDestIp6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 49),
    _QtechAceExtDestIp6_Type()
)
qtechAceExtDestIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtDestIp6.setStatus("current")


class _QtechAceExtIfAnyDestIp6WildCard_Type(TruthValue):
    """Custom type qtechAceExtIfAnyDestIp6WildCard based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyDestIp6WildCard_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyDestIp6WildCard_Object = MibTableColumn
qtechAceExtIfAnyDestIp6WildCard = _QtechAceExtIfAnyDestIp6WildCard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 50),
    _QtechAceExtIfAnyDestIp6WildCard_Type()
)
qtechAceExtIfAnyDestIp6WildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyDestIp6WildCard.setStatus("current")


class _QtechAceExtDestIp6WildCard_Type(OctetString):
    """Custom type qtechAceExtDestIp6WildCard based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_QtechAceExtDestIp6WildCard_Type.__name__ = "OctetString"
_QtechAceExtDestIp6WildCard_Object = MibTableColumn
qtechAceExtDestIp6WildCard = _QtechAceExtDestIp6WildCard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 1, 4, 1, 51),
    _QtechAceExtDestIp6WildCard_Type()
)
qtechAceExtDestIp6WildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAceExtDestIp6WildCard.setStatus("current")
_QtechAclMIBConformance_ObjectIdentity = ObjectIdentity
qtechAclMIBConformance = _QtechAclMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 2)
)
_QtechAclMIBCompliances_ObjectIdentity = ObjectIdentity
qtechAclMIBCompliances = _QtechAclMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 2, 1)
)
_QtechAclMIBGroups_ObjectIdentity = ObjectIdentity
qtechAclMIBGroups = _QtechAclMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 2, 2)
)

# Managed Objects groups

qtechAclMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 2, 2, 1)
)
qtechAclMIBGroup.setObjects(
      *(("QTECH-ACL-MIB", "qtechAclName"),
        ("QTECH-ACL-MIB", "qtechAclMode"),
        ("QTECH-ACL-MIB", "qtechAclEntryStatus"),
        ("QTECH-ACL-MIB", "qtechAceExtAclName"),
        ("QTECH-ACL-MIB", "qtechAceExtIndex"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnyVID"),
        ("QTECH-ACL-MIB", "qtechAceExtVID"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnySourceIp"),
        ("QTECH-ACL-MIB", "qtechAceExtSourceIp"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnySourceWildCard"),
        ("QTECH-ACL-MIB", "qtechAceExtSourceWildCard"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnySourceMacAddr"),
        ("QTECH-ACL-MIB", "qtechAceExtSourceMacAddr"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnyDestIp"),
        ("QTECH-ACL-MIB", "qtechAceExtDestIp"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnyDestWildCard"),
        ("QTECH-ACL-MIB", "qtechAceExtDestIpWildCard"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnyDestMacAddr"),
        ("QTECH-ACL-MIB", "qtechAceExtDestMacAddr"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnyEtherLikeType"),
        ("QTECH-ACL-MIB", "qtechAceExtEtherLikeType"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnyIpProtocolField"),
        ("QTECH-ACL-MIB", "qtechAceExtIpProtocolField"),
        ("QTECH-ACL-MIB", "qtechAceExtSourceProtocolPort"),
        ("QTECH-ACL-MIB", "qtechAceExtDestProtocolPort"),
        ("QTECH-ACL-MIB", "qtechAceExtProtocolType"),
        ("QTECH-ACL-MIB", "qtechAceExtProtocolType"),
        ("QTECH-ACL-MIB", "qtechAceExtFlowAction"),
        ("QTECH-ACL-MIB", "qtechAceExtEntryStauts"),
        ("QTECH-ACL-MIB", "qtechAceExtTimeRangeName"),
        ("QTECH-ACL-MIB", "qtechAceExtSourcePortOp"),
        ("QTECH-ACL-MIB", "qtechAceExtSourceProtocolPortRange"),
        ("QTECH-ACL-MIB", "qtechAceExtDestPortOp"),
        ("QTECH-ACL-MIB", "qtechAceExtDestProtocolPortRange"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnyCos"),
        ("QTECH-ACL-MIB", "qtechAceExtCos"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnyIpPrec"),
        ("QTECH-ACL-MIB", "qtechAceExtIpPrec"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnyDscp"),
        ("QTECH-ACL-MIB", "qtechAceExtDscp"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnyTcpFlag"),
        ("QTECH-ACL-MIB", "qtechAceExtTcpFlag"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnySourceMacAddrWildCard"),
        ("QTECH-ACL-MIB", "qtechAceExtSourceMacAddrWildCard"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnyDestMacAddrWildCard"),
        ("QTECH-ACL-MIB", "qtechAceExtDestMacAddrWildCard"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnySourceIp6"),
        ("QTECH-ACL-MIB", "qtechAceExtSourceIp6"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnySourceIp6WildCard"),
        ("QTECH-ACL-MIB", "qtechAceExtSourceIp6WildCard"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnyDestIp6"),
        ("QTECH-ACL-MIB", "qtechAceExtDestIp6"),
        ("QTECH-ACL-MIB", "qtechAceExtIfAnyDestIp6WildCard"),
        ("QTECH-ACL-MIB", "qtechAceExtDestIp6WildCard"),
        ("QTECH-ACL-MIB", "qtechAclIfIndex"),
        ("QTECH-ACL-MIB", "qtechAclIfMaxEntryNum"),
        ("QTECH-ACL-MIB", "qtechAclIfCurruntEntryNum"),
        ("QTECH-ACL-MIB", "qtechIfInAclName"),
        ("QTECH-ACL-MIB", "qtechIfOutAclName"))
)
if mibBuilder.loadTexts:
    qtechAclMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechAclMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 17, 2, 1, 1)
)
qtechAclMIBCompliance.setObjects(
    ("QTECH-ACL-MIB", "qtechAclMIBGroup")
)
if mibBuilder.loadTexts:
    qtechAclMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-ACL-MIB",
    **{"qtechAclMIB": qtechAclMIB,
       "qtechAclMIBObjects": qtechAclMIBObjects,
       "qtechAclTable": qtechAclTable,
       "qtechAclEntry": qtechAclEntry,
       "qtechAclName": qtechAclName,
       "qtechAclMode": qtechAclMode,
       "qtechAclEntryStatus": qtechAclEntryStatus,
       "qtechAclIfTable": qtechAclIfTable,
       "qtechAclIfEntry": qtechAclIfEntry,
       "qtechAclIfIndex": qtechAclIfIndex,
       "qtechAclIfMaxEntryNum": qtechAclIfMaxEntryNum,
       "qtechAclIfCurruntEntryNum": qtechAclIfCurruntEntryNum,
       "qtechIfInAclName": qtechIfInAclName,
       "qtechIfOutAclName": qtechIfOutAclName,
       "qtechAclIf6MaxEntryNum": qtechAclIf6MaxEntryNum,
       "qtechAclIf6CurruntEntryNum": qtechAclIf6CurruntEntryNum,
       "qtechIf6InAclName": qtechIf6InAclName,
       "qtechIf6OutAclName": qtechIf6OutAclName,
       "qtechAceExtTable": qtechAceExtTable,
       "qtechAceExtEntry": qtechAceExtEntry,
       "qtechAceExtAclName": qtechAceExtAclName,
       "qtechAceExtIndex": qtechAceExtIndex,
       "qtechAceExtIfAnyVID": qtechAceExtIfAnyVID,
       "qtechAceExtVID": qtechAceExtVID,
       "qtechAceExtIfAnySourceIp": qtechAceExtIfAnySourceIp,
       "qtechAceExtSourceIp": qtechAceExtSourceIp,
       "qtechAceExtIfAnySourceWildCard": qtechAceExtIfAnySourceWildCard,
       "qtechAceExtSourceWildCard": qtechAceExtSourceWildCard,
       "qtechAceExtIfAnySourceMacAddr": qtechAceExtIfAnySourceMacAddr,
       "qtechAceExtSourceMacAddr": qtechAceExtSourceMacAddr,
       "qtechAceExtIfAnyDestIp": qtechAceExtIfAnyDestIp,
       "qtechAceExtDestIp": qtechAceExtDestIp,
       "qtechAceExtIfAnyDestWildCard": qtechAceExtIfAnyDestWildCard,
       "qtechAceExtDestIpWildCard": qtechAceExtDestIpWildCard,
       "qtechAceExtIfAnyDestMacAddr": qtechAceExtIfAnyDestMacAddr,
       "qtechAceExtDestMacAddr": qtechAceExtDestMacAddr,
       "qtechAceExtIfAnyEtherLikeType": qtechAceExtIfAnyEtherLikeType,
       "qtechAceExtEtherLikeType": qtechAceExtEtherLikeType,
       "qtechAceExtIfAnyIpProtocolField": qtechAceExtIfAnyIpProtocolField,
       "qtechAceExtIpProtocolField": qtechAceExtIpProtocolField,
       "qtechAceExtSourceProtocolPort": qtechAceExtSourceProtocolPort,
       "qtechAceExtDestProtocolPort": qtechAceExtDestProtocolPort,
       "qtechAceExtIfAnyProtocolType": qtechAceExtIfAnyProtocolType,
       "qtechAceExtProtocolType": qtechAceExtProtocolType,
       "qtechAceExtFlowAction": qtechAceExtFlowAction,
       "qtechAceExtEntryStauts": qtechAceExtEntryStauts,
       "qtechAceExtTimeRangeName": qtechAceExtTimeRangeName,
       "qtechAceExtSourcePortOp": qtechAceExtSourcePortOp,
       "qtechAceExtSourceProtocolPortRange": qtechAceExtSourceProtocolPortRange,
       "qtechAceExtDestPortOp": qtechAceExtDestPortOp,
       "qtechAceExtDestProtocolPortRange": qtechAceExtDestProtocolPortRange,
       "qtechAceExtIfAnyCos": qtechAceExtIfAnyCos,
       "qtechAceExtCos": qtechAceExtCos,
       "qtechAceExtIfAnyIpPrec": qtechAceExtIfAnyIpPrec,
       "qtechAceExtIpPrec": qtechAceExtIpPrec,
       "qtechAceExtIfAnyDscp": qtechAceExtIfAnyDscp,
       "qtechAceExtDscp": qtechAceExtDscp,
       "qtechAceExtIfAnyTcpFlag": qtechAceExtIfAnyTcpFlag,
       "qtechAceExtTcpFlag": qtechAceExtTcpFlag,
       "qtechAceExtIfAnySourceMacAddrWildCard": qtechAceExtIfAnySourceMacAddrWildCard,
       "qtechAceExtSourceMacAddrWildCard": qtechAceExtSourceMacAddrWildCard,
       "qtechAceExtIfAnyDestMacAddrWildCard": qtechAceExtIfAnyDestMacAddrWildCard,
       "qtechAceExtDestMacAddrWildCard": qtechAceExtDestMacAddrWildCard,
       "qtechAceExtIfAnySourceIp6": qtechAceExtIfAnySourceIp6,
       "qtechAceExtSourceIp6": qtechAceExtSourceIp6,
       "qtechAceExtIfAnySourceIp6WildCard": qtechAceExtIfAnySourceIp6WildCard,
       "qtechAceExtSourceIp6WildCard": qtechAceExtSourceIp6WildCard,
       "qtechAceExtIfAnyDestIp6": qtechAceExtIfAnyDestIp6,
       "qtechAceExtDestIp6": qtechAceExtDestIp6,
       "qtechAceExtIfAnyDestIp6WildCard": qtechAceExtIfAnyDestIp6WildCard,
       "qtechAceExtDestIp6WildCard": qtechAceExtDestIp6WildCard,
       "qtechAclMIBConformance": qtechAclMIBConformance,
       "qtechAclMIBCompliances": qtechAclMIBCompliances,
       "qtechAclMIBCompliance": qtechAclMIBCompliance,
       "qtechAclMIBGroups": qtechAclMIBGroups,
       "qtechAclMIBGroup": qtechAclMIBGroup}
)
