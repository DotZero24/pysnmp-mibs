# SNMP MIB module (FS-ACL-CONTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-ACL-CONTEXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:03 2025
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

fsAclVCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66)
)
if mibBuilder.loadTexts:
    fsAclVCMIB.setRevisions(
        ("2009-12-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsAclVCMIBObjects_ObjectIdentity = ObjectIdentity
fsAclVCMIBObjects = _FsAclVCMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1)
)
_FsAclVCTable_Object = MibTable
fsAclVCTable = _FsAclVCTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 1)
)
if mibBuilder.loadTexts:
    fsAclVCTable.setStatus("current")
_FsAclVCEntry_Object = MibTableRow
fsAclVCEntry = _FsAclVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 1, 1)
)
fsAclVCEntry.setIndexNames(
    (0, "FS-ACL-CONTEXT-MIB", "fsAclContextNameVC"),
    (0, "FS-ACL-CONTEXT-MIB", "fsAclNameVC"),
)
if mibBuilder.loadTexts:
    fsAclVCEntry.setStatus("current")


class _FsAclContextNameVC_Type(DisplayString):
    """Custom type fsAclContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_FsAclContextNameVC_Type.__name__ = "DisplayString"
_FsAclContextNameVC_Object = MibTableColumn
fsAclContextNameVC = _FsAclContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 1, 1, 1),
    _FsAclContextNameVC_Type()
)
fsAclContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAclContextNameVC.setStatus("current")


class _FsAclNameVC_Type(DisplayString):
    """Custom type fsAclNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsAclNameVC_Type.__name__ = "DisplayString"
_FsAclNameVC_Object = MibTableColumn
fsAclNameVC = _FsAclNameVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 1, 1, 2),
    _FsAclNameVC_Type()
)
fsAclNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAclNameVC.setStatus("current")


class _FsAclModeVC_Type(Integer32):
    """Custom type fsAclModeVC based on Integer32"""
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


_FsAclModeVC_Type.__name__ = "Integer32"
_FsAclModeVC_Object = MibTableColumn
fsAclModeVC = _FsAclModeVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 1, 1, 3),
    _FsAclModeVC_Type()
)
fsAclModeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAclModeVC.setStatus("current")
_FsAclEntryStatusVC_Type = ConfigStatus
_FsAclEntryStatusVC_Object = MibTableColumn
fsAclEntryStatusVC = _FsAclEntryStatusVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 1, 1, 4),
    _FsAclEntryStatusVC_Type()
)
fsAclEntryStatusVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAclEntryStatusVC.setStatus("current")
_FsAclIfVCTable_Object = MibTable
fsAclIfVCTable = _FsAclIfVCTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 2)
)
if mibBuilder.loadTexts:
    fsAclIfVCTable.setStatus("current")
_FsAclIfVCEntry_Object = MibTableRow
fsAclIfVCEntry = _FsAclIfVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 2, 1)
)
fsAclIfVCEntry.setIndexNames(
    (0, "FS-ACL-CONTEXT-MIB", "fsAclIfContextNameVC"),
    (0, "FS-ACL-CONTEXT-MIB", "fsAclIfIndexVC"),
)
if mibBuilder.loadTexts:
    fsAclIfVCEntry.setStatus("current")


class _FsAclIfContextNameVC_Type(DisplayString):
    """Custom type fsAclIfContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_FsAclIfContextNameVC_Type.__name__ = "DisplayString"
_FsAclIfContextNameVC_Object = MibTableColumn
fsAclIfContextNameVC = _FsAclIfContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 2, 1, 1),
    _FsAclIfContextNameVC_Type()
)
fsAclIfContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAclIfContextNameVC.setStatus("current")
_FsAclIfIndexVC_Type = IfIndex
_FsAclIfIndexVC_Object = MibTableColumn
fsAclIfIndexVC = _FsAclIfIndexVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 2, 1, 2),
    _FsAclIfIndexVC_Type()
)
fsAclIfIndexVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAclIfIndexVC.setStatus("current")
_FsAclIfMaxEntryNumVC_Type = Integer32
_FsAclIfMaxEntryNumVC_Object = MibTableColumn
fsAclIfMaxEntryNumVC = _FsAclIfMaxEntryNumVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 2, 1, 3),
    _FsAclIfMaxEntryNumVC_Type()
)
fsAclIfMaxEntryNumVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAclIfMaxEntryNumVC.setStatus("current")
_FsAclIfCurruntEntryNumVC_Type = Integer32
_FsAclIfCurruntEntryNumVC_Object = MibTableColumn
fsAclIfCurruntEntryNumVC = _FsAclIfCurruntEntryNumVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 2, 1, 4),
    _FsAclIfCurruntEntryNumVC_Type()
)
fsAclIfCurruntEntryNumVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAclIfCurruntEntryNumVC.setStatus("current")


class _FsIfInAclNameVC_Type(DisplayString):
    """Custom type fsIfInAclNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsIfInAclNameVC_Type.__name__ = "DisplayString"
_FsIfInAclNameVC_Object = MibTableColumn
fsIfInAclNameVC = _FsIfInAclNameVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 2, 1, 5),
    _FsIfInAclNameVC_Type()
)
fsIfInAclNameVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfInAclNameVC.setStatus("current")


class _FsIfOutAclNameVC_Type(DisplayString):
    """Custom type fsIfOutAclNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsIfOutAclNameVC_Type.__name__ = "DisplayString"
_FsIfOutAclNameVC_Object = MibTableColumn
fsIfOutAclNameVC = _FsIfOutAclNameVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 2, 1, 6),
    _FsIfOutAclNameVC_Type()
)
fsIfOutAclNameVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfOutAclNameVC.setStatus("current")
_FsAceExtVCTable_Object = MibTable
fsAceExtVCTable = _FsAceExtVCTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3)
)
if mibBuilder.loadTexts:
    fsAceExtVCTable.setStatus("current")
_FsAceExtVCEntry_Object = MibTableRow
fsAceExtVCEntry = _FsAceExtVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1)
)
fsAceExtVCEntry.setIndexNames(
    (0, "FS-ACL-CONTEXT-MIB", "fsAceExtContextNameVC"),
    (0, "FS-ACL-CONTEXT-MIB", "fsAceExtAclNameVC"),
    (0, "FS-ACL-CONTEXT-MIB", "fsAceExtIndexVC"),
)
if mibBuilder.loadTexts:
    fsAceExtVCEntry.setStatus("current")


class _FsAceExtContextNameVC_Type(DisplayString):
    """Custom type fsAceExtContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_FsAceExtContextNameVC_Type.__name__ = "DisplayString"
_FsAceExtContextNameVC_Object = MibTableColumn
fsAceExtContextNameVC = _FsAceExtContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 1),
    _FsAceExtContextNameVC_Type()
)
fsAceExtContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAceExtContextNameVC.setStatus("current")


class _FsAceExtAclNameVC_Type(DisplayString):
    """Custom type fsAceExtAclNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsAceExtAclNameVC_Type.__name__ = "DisplayString"
_FsAceExtAclNameVC_Object = MibTableColumn
fsAceExtAclNameVC = _FsAceExtAclNameVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 2),
    _FsAceExtAclNameVC_Type()
)
fsAceExtAclNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAceExtAclNameVC.setStatus("current")


class _FsAceExtIndexVC_Type(Integer32):
    """Custom type fsAceExtIndexVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsAceExtIndexVC_Type.__name__ = "Integer32"
_FsAceExtIndexVC_Object = MibTableColumn
fsAceExtIndexVC = _FsAceExtIndexVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 3),
    _FsAceExtIndexVC_Type()
)
fsAceExtIndexVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAceExtIndexVC.setStatus("current")


class _FsAceExtIfAnyVIDVC_Type(TruthValue):
    """Custom type fsAceExtIfAnyVIDVC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyVIDVC_Type.__name__ = "TruthValue"
_FsAceExtIfAnyVIDVC_Object = MibTableColumn
fsAceExtIfAnyVIDVC = _FsAceExtIfAnyVIDVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 4),
    _FsAceExtIfAnyVIDVC_Type()
)
fsAceExtIfAnyVIDVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyVIDVC.setStatus("current")


class _FsAceExtVIDVC_Type(Unsigned32):
    """Custom type fsAceExtVIDVC based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_FsAceExtVIDVC_Type.__name__ = "Unsigned32"
_FsAceExtVIDVC_Object = MibTableColumn
fsAceExtVIDVC = _FsAceExtVIDVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 5),
    _FsAceExtVIDVC_Type()
)
fsAceExtVIDVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtVIDVC.setStatus("current")


class _FsAceExtIfAnySourceIpVC_Type(TruthValue):
    """Custom type fsAceExtIfAnySourceIpVC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnySourceIpVC_Type.__name__ = "TruthValue"
_FsAceExtIfAnySourceIpVC_Object = MibTableColumn
fsAceExtIfAnySourceIpVC = _FsAceExtIfAnySourceIpVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 6),
    _FsAceExtIfAnySourceIpVC_Type()
)
fsAceExtIfAnySourceIpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnySourceIpVC.setStatus("current")
_FsAceExtSourceIpVC_Type = IpAddress
_FsAceExtSourceIpVC_Object = MibTableColumn
fsAceExtSourceIpVC = _FsAceExtSourceIpVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 7),
    _FsAceExtSourceIpVC_Type()
)
fsAceExtSourceIpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtSourceIpVC.setStatus("current")


class _FsAceExtIfAnySourceWildCardVC_Type(TruthValue):
    """Custom type fsAceExtIfAnySourceWildCardVC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnySourceWildCardVC_Type.__name__ = "TruthValue"
_FsAceExtIfAnySourceWildCardVC_Object = MibTableColumn
fsAceExtIfAnySourceWildCardVC = _FsAceExtIfAnySourceWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 8),
    _FsAceExtIfAnySourceWildCardVC_Type()
)
fsAceExtIfAnySourceWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnySourceWildCardVC.setStatus("current")
_FsAceExtSourceWildCardVC_Type = IpAddress
_FsAceExtSourceWildCardVC_Object = MibTableColumn
fsAceExtSourceWildCardVC = _FsAceExtSourceWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 9),
    _FsAceExtSourceWildCardVC_Type()
)
fsAceExtSourceWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtSourceWildCardVC.setStatus("current")


class _FsAceExtIfAnySourceMacAddrVC_Type(TruthValue):
    """Custom type fsAceExtIfAnySourceMacAddrVC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnySourceMacAddrVC_Type.__name__ = "TruthValue"
_FsAceExtIfAnySourceMacAddrVC_Object = MibTableColumn
fsAceExtIfAnySourceMacAddrVC = _FsAceExtIfAnySourceMacAddrVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 10),
    _FsAceExtIfAnySourceMacAddrVC_Type()
)
fsAceExtIfAnySourceMacAddrVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnySourceMacAddrVC.setStatus("current")
_FsAceExtSourceMacAddrVC_Type = MacAddress
_FsAceExtSourceMacAddrVC_Object = MibTableColumn
fsAceExtSourceMacAddrVC = _FsAceExtSourceMacAddrVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 11),
    _FsAceExtSourceMacAddrVC_Type()
)
fsAceExtSourceMacAddrVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtSourceMacAddrVC.setStatus("current")


class _FsAceExtIfAnyDestIpVC_Type(TruthValue):
    """Custom type fsAceExtIfAnyDestIpVC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyDestIpVC_Type.__name__ = "TruthValue"
_FsAceExtIfAnyDestIpVC_Object = MibTableColumn
fsAceExtIfAnyDestIpVC = _FsAceExtIfAnyDestIpVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 12),
    _FsAceExtIfAnyDestIpVC_Type()
)
fsAceExtIfAnyDestIpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyDestIpVC.setStatus("current")
_FsAceExtDestIpVC_Type = IpAddress
_FsAceExtDestIpVC_Object = MibTableColumn
fsAceExtDestIpVC = _FsAceExtDestIpVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 13),
    _FsAceExtDestIpVC_Type()
)
fsAceExtDestIpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtDestIpVC.setStatus("current")


class _FsAceExtIfAnyDestWildCardVC_Type(TruthValue):
    """Custom type fsAceExtIfAnyDestWildCardVC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyDestWildCardVC_Type.__name__ = "TruthValue"
_FsAceExtIfAnyDestWildCardVC_Object = MibTableColumn
fsAceExtIfAnyDestWildCardVC = _FsAceExtIfAnyDestWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 14),
    _FsAceExtIfAnyDestWildCardVC_Type()
)
fsAceExtIfAnyDestWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyDestWildCardVC.setStatus("current")
_FsAceExtDestIpWildCardVC_Type = IpAddress
_FsAceExtDestIpWildCardVC_Object = MibTableColumn
fsAceExtDestIpWildCardVC = _FsAceExtDestIpWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 15),
    _FsAceExtDestIpWildCardVC_Type()
)
fsAceExtDestIpWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtDestIpWildCardVC.setStatus("current")


class _FsAceExtIfAnyDestMacAddrVC_Type(TruthValue):
    """Custom type fsAceExtIfAnyDestMacAddrVC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyDestMacAddrVC_Type.__name__ = "TruthValue"
_FsAceExtIfAnyDestMacAddrVC_Object = MibTableColumn
fsAceExtIfAnyDestMacAddrVC = _FsAceExtIfAnyDestMacAddrVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 16),
    _FsAceExtIfAnyDestMacAddrVC_Type()
)
fsAceExtIfAnyDestMacAddrVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyDestMacAddrVC.setStatus("current")
_FsAceExtDestMacAddrVC_Type = MacAddress
_FsAceExtDestMacAddrVC_Object = MibTableColumn
fsAceExtDestMacAddrVC = _FsAceExtDestMacAddrVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 17),
    _FsAceExtDestMacAddrVC_Type()
)
fsAceExtDestMacAddrVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtDestMacAddrVC.setStatus("current")


class _FsAceExtIfAnyEtherLikeTypeVC_Type(TruthValue):
    """Custom type fsAceExtIfAnyEtherLikeTypeVC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyEtherLikeTypeVC_Type.__name__ = "TruthValue"
_FsAceExtIfAnyEtherLikeTypeVC_Object = MibTableColumn
fsAceExtIfAnyEtherLikeTypeVC = _FsAceExtIfAnyEtherLikeTypeVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 18),
    _FsAceExtIfAnyEtherLikeTypeVC_Type()
)
fsAceExtIfAnyEtherLikeTypeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyEtherLikeTypeVC.setStatus("current")
_FsAceExtEtherLikeTypeVC_Type = Integer32
_FsAceExtEtherLikeTypeVC_Object = MibTableColumn
fsAceExtEtherLikeTypeVC = _FsAceExtEtherLikeTypeVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 19),
    _FsAceExtEtherLikeTypeVC_Type()
)
fsAceExtEtherLikeTypeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtEtherLikeTypeVC.setStatus("current")


class _FsAceExtIfAnyIpProtocolFieldVC_Type(TruthValue):
    """Custom type fsAceExtIfAnyIpProtocolFieldVC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyIpProtocolFieldVC_Type.__name__ = "TruthValue"
_FsAceExtIfAnyIpProtocolFieldVC_Object = MibTableColumn
fsAceExtIfAnyIpProtocolFieldVC = _FsAceExtIfAnyIpProtocolFieldVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 20),
    _FsAceExtIfAnyIpProtocolFieldVC_Type()
)
fsAceExtIfAnyIpProtocolFieldVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyIpProtocolFieldVC.setStatus("current")
_FsAceExtIpProtocolFieldVC_Type = Integer32
_FsAceExtIpProtocolFieldVC_Object = MibTableColumn
fsAceExtIpProtocolFieldVC = _FsAceExtIpProtocolFieldVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 21),
    _FsAceExtIpProtocolFieldVC_Type()
)
fsAceExtIpProtocolFieldVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIpProtocolFieldVC.setStatus("current")
_FsAceExtSourceProtocolPortVC_Type = Integer32
_FsAceExtSourceProtocolPortVC_Object = MibTableColumn
fsAceExtSourceProtocolPortVC = _FsAceExtSourceProtocolPortVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 22),
    _FsAceExtSourceProtocolPortVC_Type()
)
fsAceExtSourceProtocolPortVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtSourceProtocolPortVC.setStatus("current")
_FsAceExtDestProtocolPortVC_Type = Integer32
_FsAceExtDestProtocolPortVC_Object = MibTableColumn
fsAceExtDestProtocolPortVC = _FsAceExtDestProtocolPortVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 23),
    _FsAceExtDestProtocolPortVC_Type()
)
fsAceExtDestProtocolPortVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtDestProtocolPortVC.setStatus("current")


class _FsAceExtIfAnyProtocolTypeVC_Type(TruthValue):
    """Custom type fsAceExtIfAnyProtocolTypeVC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyProtocolTypeVC_Type.__name__ = "TruthValue"
_FsAceExtIfAnyProtocolTypeVC_Object = MibTableColumn
fsAceExtIfAnyProtocolTypeVC = _FsAceExtIfAnyProtocolTypeVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 24),
    _FsAceExtIfAnyProtocolTypeVC_Type()
)
fsAceExtIfAnyProtocolTypeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyProtocolTypeVC.setStatus("current")
_FsAceExtProtocolTypeVC_Type = Integer32
_FsAceExtProtocolTypeVC_Object = MibTableColumn
fsAceExtProtocolTypeVC = _FsAceExtProtocolTypeVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 25),
    _FsAceExtProtocolTypeVC_Type()
)
fsAceExtProtocolTypeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtProtocolTypeVC.setStatus("current")


class _FsAceExtFlowActionVC_Type(Integer32):
    """Custom type fsAceExtFlowActionVC based on Integer32"""
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


_FsAceExtFlowActionVC_Type.__name__ = "Integer32"
_FsAceExtFlowActionVC_Object = MibTableColumn
fsAceExtFlowActionVC = _FsAceExtFlowActionVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 26),
    _FsAceExtFlowActionVC_Type()
)
fsAceExtFlowActionVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtFlowActionVC.setStatus("current")
_FsAceExtEntryStautsVC_Type = RowStatus
_FsAceExtEntryStautsVC_Object = MibTableColumn
fsAceExtEntryStautsVC = _FsAceExtEntryStautsVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 27),
    _FsAceExtEntryStautsVC_Type()
)
fsAceExtEntryStautsVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtEntryStautsVC.setStatus("current")


class _FsAceExtTimeRangeNameVC_Type(DisplayString):
    """Custom type fsAceExtTimeRangeNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsAceExtTimeRangeNameVC_Type.__name__ = "DisplayString"
_FsAceExtTimeRangeNameVC_Object = MibTableColumn
fsAceExtTimeRangeNameVC = _FsAceExtTimeRangeNameVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 28),
    _FsAceExtTimeRangeNameVC_Type()
)
fsAceExtTimeRangeNameVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtTimeRangeNameVC.setStatus("current")


class _FsAceExtSourcePortOpVC_Type(Integer32):
    """Custom type fsAceExtSourcePortOpVC based on Integer32"""
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


_FsAceExtSourcePortOpVC_Type.__name__ = "Integer32"
_FsAceExtSourcePortOpVC_Object = MibTableColumn
fsAceExtSourcePortOpVC = _FsAceExtSourcePortOpVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 29),
    _FsAceExtSourcePortOpVC_Type()
)
fsAceExtSourcePortOpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtSourcePortOpVC.setStatus("current")
_FsAceExtSourceProtocolPortRangeVC_Type = Integer32
_FsAceExtSourceProtocolPortRangeVC_Object = MibTableColumn
fsAceExtSourceProtocolPortRangeVC = _FsAceExtSourceProtocolPortRangeVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 30),
    _FsAceExtSourceProtocolPortRangeVC_Type()
)
fsAceExtSourceProtocolPortRangeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtSourceProtocolPortRangeVC.setStatus("current")


class _FsAceExtDestPortOpVC_Type(Integer32):
    """Custom type fsAceExtDestPortOpVC based on Integer32"""
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


_FsAceExtDestPortOpVC_Type.__name__ = "Integer32"
_FsAceExtDestPortOpVC_Object = MibTableColumn
fsAceExtDestPortOpVC = _FsAceExtDestPortOpVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 31),
    _FsAceExtDestPortOpVC_Type()
)
fsAceExtDestPortOpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtDestPortOpVC.setStatus("current")
_FsAceExtDestProtocolPortRangeVC_Type = Integer32
_FsAceExtDestProtocolPortRangeVC_Object = MibTableColumn
fsAceExtDestProtocolPortRangeVC = _FsAceExtDestProtocolPortRangeVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 32),
    _FsAceExtDestProtocolPortRangeVC_Type()
)
fsAceExtDestProtocolPortRangeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtDestProtocolPortRangeVC.setStatus("current")


class _FsAceExtIfAnyCosVC_Type(TruthValue):
    """Custom type fsAceExtIfAnyCosVC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyCosVC_Type.__name__ = "TruthValue"
_FsAceExtIfAnyCosVC_Object = MibTableColumn
fsAceExtIfAnyCosVC = _FsAceExtIfAnyCosVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 33),
    _FsAceExtIfAnyCosVC_Type()
)
fsAceExtIfAnyCosVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyCosVC.setStatus("current")
_FsAceExtCosVC_Type = Integer32
_FsAceExtCosVC_Object = MibTableColumn
fsAceExtCosVC = _FsAceExtCosVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 34),
    _FsAceExtCosVC_Type()
)
fsAceExtCosVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtCosVC.setStatus("current")


class _FsAceExtIfAnyIpPrecVC_Type(TruthValue):
    """Custom type fsAceExtIfAnyIpPrecVC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyIpPrecVC_Type.__name__ = "TruthValue"
_FsAceExtIfAnyIpPrecVC_Object = MibTableColumn
fsAceExtIfAnyIpPrecVC = _FsAceExtIfAnyIpPrecVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 35),
    _FsAceExtIfAnyIpPrecVC_Type()
)
fsAceExtIfAnyIpPrecVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyIpPrecVC.setStatus("current")
_FsAceExtIpPrecVC_Type = Integer32
_FsAceExtIpPrecVC_Object = MibTableColumn
fsAceExtIpPrecVC = _FsAceExtIpPrecVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 36),
    _FsAceExtIpPrecVC_Type()
)
fsAceExtIpPrecVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIpPrecVC.setStatus("current")


class _FsAceExtIfAnyDscpVC_Type(TruthValue):
    """Custom type fsAceExtIfAnyDscpVC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyDscpVC_Type.__name__ = "TruthValue"
_FsAceExtIfAnyDscpVC_Object = MibTableColumn
fsAceExtIfAnyDscpVC = _FsAceExtIfAnyDscpVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 37),
    _FsAceExtIfAnyDscpVC_Type()
)
fsAceExtIfAnyDscpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyDscpVC.setStatus("current")
_FsAceExtDscpVC_Type = Integer32
_FsAceExtDscpVC_Object = MibTableColumn
fsAceExtDscpVC = _FsAceExtDscpVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 38),
    _FsAceExtDscpVC_Type()
)
fsAceExtDscpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtDscpVC.setStatus("current")


class _FsAceExtIfAnyTcpFlagVC_Type(TruthValue):
    """Custom type fsAceExtIfAnyTcpFlagVC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyTcpFlagVC_Type.__name__ = "TruthValue"
_FsAceExtIfAnyTcpFlagVC_Object = MibTableColumn
fsAceExtIfAnyTcpFlagVC = _FsAceExtIfAnyTcpFlagVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 39),
    _FsAceExtIfAnyTcpFlagVC_Type()
)
fsAceExtIfAnyTcpFlagVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyTcpFlagVC.setStatus("current")
_FsAceExtTcpFlagVC_Type = Integer32
_FsAceExtTcpFlagVC_Object = MibTableColumn
fsAceExtTcpFlagVC = _FsAceExtTcpFlagVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 40),
    _FsAceExtTcpFlagVC_Type()
)
fsAceExtTcpFlagVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtTcpFlagVC.setStatus("current")


class _FsAceExtIfAnySourceMacAddrWildCardVC_Type(TruthValue):
    """Custom type fsAceExtIfAnySourceMacAddrWildCardVC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnySourceMacAddrWildCardVC_Type.__name__ = "TruthValue"
_FsAceExtIfAnySourceMacAddrWildCardVC_Object = MibTableColumn
fsAceExtIfAnySourceMacAddrWildCardVC = _FsAceExtIfAnySourceMacAddrWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 41),
    _FsAceExtIfAnySourceMacAddrWildCardVC_Type()
)
fsAceExtIfAnySourceMacAddrWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnySourceMacAddrWildCardVC.setStatus("current")
_FsAceExtSourceMacAddrWildCardVC_Type = MacAddress
_FsAceExtSourceMacAddrWildCardVC_Object = MibTableColumn
fsAceExtSourceMacAddrWildCardVC = _FsAceExtSourceMacAddrWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 42),
    _FsAceExtSourceMacAddrWildCardVC_Type()
)
fsAceExtSourceMacAddrWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtSourceMacAddrWildCardVC.setStatus("current")


class _FsAceExtIfAnyDestMacAddrWildCardVC_Type(TruthValue):
    """Custom type fsAceExtIfAnyDestMacAddrWildCardVC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyDestMacAddrWildCardVC_Type.__name__ = "TruthValue"
_FsAceExtIfAnyDestMacAddrWildCardVC_Object = MibTableColumn
fsAceExtIfAnyDestMacAddrWildCardVC = _FsAceExtIfAnyDestMacAddrWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 43),
    _FsAceExtIfAnyDestMacAddrWildCardVC_Type()
)
fsAceExtIfAnyDestMacAddrWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyDestMacAddrWildCardVC.setStatus("current")
_FsAceExtDestMacAddrWildCardVC_Type = MacAddress
_FsAceExtDestMacAddrWildCardVC_Object = MibTableColumn
fsAceExtDestMacAddrWildCardVC = _FsAceExtDestMacAddrWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 44),
    _FsAceExtDestMacAddrWildCardVC_Type()
)
fsAceExtDestMacAddrWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtDestMacAddrWildCardVC.setStatus("current")


class _FsAceExtIfAnySourceIp6VC_Type(TruthValue):
    """Custom type fsAceExtIfAnySourceIp6VC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnySourceIp6VC_Type.__name__ = "TruthValue"
_FsAceExtIfAnySourceIp6VC_Object = MibTableColumn
fsAceExtIfAnySourceIp6VC = _FsAceExtIfAnySourceIp6VC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 45),
    _FsAceExtIfAnySourceIp6VC_Type()
)
fsAceExtIfAnySourceIp6VC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnySourceIp6VC.setStatus("current")


class _FsAceExtSourceIp6VC_Type(OctetString):
    """Custom type fsAceExtSourceIp6VC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsAceExtSourceIp6VC_Type.__name__ = "OctetString"
_FsAceExtSourceIp6VC_Object = MibTableColumn
fsAceExtSourceIp6VC = _FsAceExtSourceIp6VC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 46),
    _FsAceExtSourceIp6VC_Type()
)
fsAceExtSourceIp6VC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtSourceIp6VC.setStatus("current")


class _FsAceExtIfAnySourceIp6WildCardVC_Type(TruthValue):
    """Custom type fsAceExtIfAnySourceIp6WildCardVC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnySourceIp6WildCardVC_Type.__name__ = "TruthValue"
_FsAceExtIfAnySourceIp6WildCardVC_Object = MibTableColumn
fsAceExtIfAnySourceIp6WildCardVC = _FsAceExtIfAnySourceIp6WildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 47),
    _FsAceExtIfAnySourceIp6WildCardVC_Type()
)
fsAceExtIfAnySourceIp6WildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnySourceIp6WildCardVC.setStatus("current")


class _FsAceExtSourceIp6WildCardVC_Type(OctetString):
    """Custom type fsAceExtSourceIp6WildCardVC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsAceExtSourceIp6WildCardVC_Type.__name__ = "OctetString"
_FsAceExtSourceIp6WildCardVC_Object = MibTableColumn
fsAceExtSourceIp6WildCardVC = _FsAceExtSourceIp6WildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 48),
    _FsAceExtSourceIp6WildCardVC_Type()
)
fsAceExtSourceIp6WildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtSourceIp6WildCardVC.setStatus("current")


class _FsAceExtIfAnyDestIp6VC_Type(TruthValue):
    """Custom type fsAceExtIfAnyDestIp6VC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyDestIp6VC_Type.__name__ = "TruthValue"
_FsAceExtIfAnyDestIp6VC_Object = MibTableColumn
fsAceExtIfAnyDestIp6VC = _FsAceExtIfAnyDestIp6VC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 49),
    _FsAceExtIfAnyDestIp6VC_Type()
)
fsAceExtIfAnyDestIp6VC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyDestIp6VC.setStatus("current")


class _FsAceExtDestIp6VC_Type(OctetString):
    """Custom type fsAceExtDestIp6VC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsAceExtDestIp6VC_Type.__name__ = "OctetString"
_FsAceExtDestIp6VC_Object = MibTableColumn
fsAceExtDestIp6VC = _FsAceExtDestIp6VC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 50),
    _FsAceExtDestIp6VC_Type()
)
fsAceExtDestIp6VC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtDestIp6VC.setStatus("current")


class _FsAceExtIfAnyDestIp6WildCardVC_Type(TruthValue):
    """Custom type fsAceExtIfAnyDestIp6WildCardVC based on TruthValue"""
    defaultValue = 1


_FsAceExtIfAnyDestIp6WildCardVC_Type.__name__ = "TruthValue"
_FsAceExtIfAnyDestIp6WildCardVC_Object = MibTableColumn
fsAceExtIfAnyDestIp6WildCardVC = _FsAceExtIfAnyDestIp6WildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 51),
    _FsAceExtIfAnyDestIp6WildCardVC_Type()
)
fsAceExtIfAnyDestIp6WildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtIfAnyDestIp6WildCardVC.setStatus("current")


class _FsAceExtDestIp6WildCardVC_Type(OctetString):
    """Custom type fsAceExtDestIp6WildCardVC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsAceExtDestIp6WildCardVC_Type.__name__ = "OctetString"
_FsAceExtDestIp6WildCardVC_Object = MibTableColumn
fsAceExtDestIp6WildCardVC = _FsAceExtDestIp6WildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 1, 3, 1, 52),
    _FsAceExtDestIp6WildCardVC_Type()
)
fsAceExtDestIp6WildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAceExtDestIp6WildCardVC.setStatus("current")
_FsAclVCMIBConformance_ObjectIdentity = ObjectIdentity
fsAclVCMIBConformance = _FsAclVCMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 2)
)
_FsAclVCMIBCompliances_ObjectIdentity = ObjectIdentity
fsAclVCMIBCompliances = _FsAclVCMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 2, 1)
)
_FsAclVCMIBGroups_ObjectIdentity = ObjectIdentity
fsAclVCMIBGroups = _FsAclVCMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 2, 2)
)

# Managed Objects groups

fsAclVCMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 2, 2, 1)
)
fsAclVCMIBGroup.setObjects(
      *(("FS-ACL-CONTEXT-MIB", "fsAclContextNameVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAclNameVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAclModeVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAclEntryStatusVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtContextNameVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtAclNameVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIndexVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnyVIDVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtVIDVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnySourceIpVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtSourceIpVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnySourceWildCardVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtSourceWildCardVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnySourceMacAddrVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtSourceMacAddrVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnyDestIpVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtDestIpVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnyDestWildCardVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtDestIpWildCardVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnyDestMacAddrVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtDestMacAddrVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnyEtherLikeTypeVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtEtherLikeTypeVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnyIpProtocolFieldVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIpProtocolFieldVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtSourceProtocolPortVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtDestProtocolPortVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtProtocolTypeVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtProtocolTypeVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtFlowActionVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtEntryStautsVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtTimeRangeNameVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtSourcePortOpVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtSourceProtocolPortRangeVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtDestPortOpVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtDestProtocolPortRangeVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnyCosVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtCosVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnyIpPrecVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIpPrecVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnyDscpVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtDscpVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnyTcpFlagVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtTcpFlagVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnySourceMacAddrWildCardVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtSourceMacAddrWildCardVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnyDestMacAddrWildCardVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtDestMacAddrWildCardVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnySourceIp6VC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtSourceIp6VC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnySourceIp6WildCardVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtSourceIp6WildCardVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnyDestIp6VC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtDestIp6VC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtIfAnyDestIp6WildCardVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAceExtDestIp6WildCardVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAclIfContextNameVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAclIfIndexVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAclIfMaxEntryNumVC"),
        ("FS-ACL-CONTEXT-MIB", "fsAclIfCurruntEntryNumVC"),
        ("FS-ACL-CONTEXT-MIB", "fsIfInAclNameVC"),
        ("FS-ACL-CONTEXT-MIB", "fsIfOutAclNameVC"))
)
if mibBuilder.loadTexts:
    fsAclVCMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsAclVCMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 66, 2, 1, 1)
)
fsAclVCMIBCompliance.setObjects(
    ("FS-ACL-CONTEXT-MIB", "fsAclVCMIBGroup")
)
if mibBuilder.loadTexts:
    fsAclVCMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-ACL-CONTEXT-MIB",
    **{"fsAclVCMIB": fsAclVCMIB,
       "fsAclVCMIBObjects": fsAclVCMIBObjects,
       "fsAclVCTable": fsAclVCTable,
       "fsAclVCEntry": fsAclVCEntry,
       "fsAclContextNameVC": fsAclContextNameVC,
       "fsAclNameVC": fsAclNameVC,
       "fsAclModeVC": fsAclModeVC,
       "fsAclEntryStatusVC": fsAclEntryStatusVC,
       "fsAclIfVCTable": fsAclIfVCTable,
       "fsAclIfVCEntry": fsAclIfVCEntry,
       "fsAclIfContextNameVC": fsAclIfContextNameVC,
       "fsAclIfIndexVC": fsAclIfIndexVC,
       "fsAclIfMaxEntryNumVC": fsAclIfMaxEntryNumVC,
       "fsAclIfCurruntEntryNumVC": fsAclIfCurruntEntryNumVC,
       "fsIfInAclNameVC": fsIfInAclNameVC,
       "fsIfOutAclNameVC": fsIfOutAclNameVC,
       "fsAceExtVCTable": fsAceExtVCTable,
       "fsAceExtVCEntry": fsAceExtVCEntry,
       "fsAceExtContextNameVC": fsAceExtContextNameVC,
       "fsAceExtAclNameVC": fsAceExtAclNameVC,
       "fsAceExtIndexVC": fsAceExtIndexVC,
       "fsAceExtIfAnyVIDVC": fsAceExtIfAnyVIDVC,
       "fsAceExtVIDVC": fsAceExtVIDVC,
       "fsAceExtIfAnySourceIpVC": fsAceExtIfAnySourceIpVC,
       "fsAceExtSourceIpVC": fsAceExtSourceIpVC,
       "fsAceExtIfAnySourceWildCardVC": fsAceExtIfAnySourceWildCardVC,
       "fsAceExtSourceWildCardVC": fsAceExtSourceWildCardVC,
       "fsAceExtIfAnySourceMacAddrVC": fsAceExtIfAnySourceMacAddrVC,
       "fsAceExtSourceMacAddrVC": fsAceExtSourceMacAddrVC,
       "fsAceExtIfAnyDestIpVC": fsAceExtIfAnyDestIpVC,
       "fsAceExtDestIpVC": fsAceExtDestIpVC,
       "fsAceExtIfAnyDestWildCardVC": fsAceExtIfAnyDestWildCardVC,
       "fsAceExtDestIpWildCardVC": fsAceExtDestIpWildCardVC,
       "fsAceExtIfAnyDestMacAddrVC": fsAceExtIfAnyDestMacAddrVC,
       "fsAceExtDestMacAddrVC": fsAceExtDestMacAddrVC,
       "fsAceExtIfAnyEtherLikeTypeVC": fsAceExtIfAnyEtherLikeTypeVC,
       "fsAceExtEtherLikeTypeVC": fsAceExtEtherLikeTypeVC,
       "fsAceExtIfAnyIpProtocolFieldVC": fsAceExtIfAnyIpProtocolFieldVC,
       "fsAceExtIpProtocolFieldVC": fsAceExtIpProtocolFieldVC,
       "fsAceExtSourceProtocolPortVC": fsAceExtSourceProtocolPortVC,
       "fsAceExtDestProtocolPortVC": fsAceExtDestProtocolPortVC,
       "fsAceExtIfAnyProtocolTypeVC": fsAceExtIfAnyProtocolTypeVC,
       "fsAceExtProtocolTypeVC": fsAceExtProtocolTypeVC,
       "fsAceExtFlowActionVC": fsAceExtFlowActionVC,
       "fsAceExtEntryStautsVC": fsAceExtEntryStautsVC,
       "fsAceExtTimeRangeNameVC": fsAceExtTimeRangeNameVC,
       "fsAceExtSourcePortOpVC": fsAceExtSourcePortOpVC,
       "fsAceExtSourceProtocolPortRangeVC": fsAceExtSourceProtocolPortRangeVC,
       "fsAceExtDestPortOpVC": fsAceExtDestPortOpVC,
       "fsAceExtDestProtocolPortRangeVC": fsAceExtDestProtocolPortRangeVC,
       "fsAceExtIfAnyCosVC": fsAceExtIfAnyCosVC,
       "fsAceExtCosVC": fsAceExtCosVC,
       "fsAceExtIfAnyIpPrecVC": fsAceExtIfAnyIpPrecVC,
       "fsAceExtIpPrecVC": fsAceExtIpPrecVC,
       "fsAceExtIfAnyDscpVC": fsAceExtIfAnyDscpVC,
       "fsAceExtDscpVC": fsAceExtDscpVC,
       "fsAceExtIfAnyTcpFlagVC": fsAceExtIfAnyTcpFlagVC,
       "fsAceExtTcpFlagVC": fsAceExtTcpFlagVC,
       "fsAceExtIfAnySourceMacAddrWildCardVC": fsAceExtIfAnySourceMacAddrWildCardVC,
       "fsAceExtSourceMacAddrWildCardVC": fsAceExtSourceMacAddrWildCardVC,
       "fsAceExtIfAnyDestMacAddrWildCardVC": fsAceExtIfAnyDestMacAddrWildCardVC,
       "fsAceExtDestMacAddrWildCardVC": fsAceExtDestMacAddrWildCardVC,
       "fsAceExtIfAnySourceIp6VC": fsAceExtIfAnySourceIp6VC,
       "fsAceExtSourceIp6VC": fsAceExtSourceIp6VC,
       "fsAceExtIfAnySourceIp6WildCardVC": fsAceExtIfAnySourceIp6WildCardVC,
       "fsAceExtSourceIp6WildCardVC": fsAceExtSourceIp6WildCardVC,
       "fsAceExtIfAnyDestIp6VC": fsAceExtIfAnyDestIp6VC,
       "fsAceExtDestIp6VC": fsAceExtDestIp6VC,
       "fsAceExtIfAnyDestIp6WildCardVC": fsAceExtIfAnyDestIp6WildCardVC,
       "fsAceExtDestIp6WildCardVC": fsAceExtDestIp6WildCardVC,
       "fsAclVCMIBConformance": fsAclVCMIBConformance,
       "fsAclVCMIBCompliances": fsAclVCMIBCompliances,
       "fsAclVCMIBCompliance": fsAclVCMIBCompliance,
       "fsAclVCMIBGroups": fsAclVCMIBGroups,
       "fsAclVCMIBGroup": fsAclVCMIBGroup}
)
