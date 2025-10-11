# SNMP MIB module (QTECH-ACL-CONTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-ACL-CONTEXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:25 2025
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

qtechAclVCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66)
)
if mibBuilder.loadTexts:
    qtechAclVCMIB.setRevisions(
        ("2009-12-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechAclVCMIBObjects_ObjectIdentity = ObjectIdentity
qtechAclVCMIBObjects = _QtechAclVCMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1)
)
_QtechAclVCTable_Object = MibTable
qtechAclVCTable = _QtechAclVCTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 1)
)
if mibBuilder.loadTexts:
    qtechAclVCTable.setStatus("current")
_QtechAclVCEntry_Object = MibTableRow
qtechAclVCEntry = _QtechAclVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 1, 1)
)
qtechAclVCEntry.setIndexNames(
    (0, "QTECH-ACL-CONTEXT-MIB", "qtechAclContextNameVC"),
    (0, "QTECH-ACL-CONTEXT-MIB", "qtechAclNameVC"),
)
if mibBuilder.loadTexts:
    qtechAclVCEntry.setStatus("current")


class _QtechAclContextNameVC_Type(DisplayString):
    """Custom type qtechAclContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_QtechAclContextNameVC_Type.__name__ = "DisplayString"
_QtechAclContextNameVC_Object = MibTableColumn
qtechAclContextNameVC = _QtechAclContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 1, 1, 1),
    _QtechAclContextNameVC_Type()
)
qtechAclContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAclContextNameVC.setStatus("current")


class _QtechAclNameVC_Type(DisplayString):
    """Custom type qtechAclNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechAclNameVC_Type.__name__ = "DisplayString"
_QtechAclNameVC_Object = MibTableColumn
qtechAclNameVC = _QtechAclNameVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 1, 1, 2),
    _QtechAclNameVC_Type()
)
qtechAclNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAclNameVC.setStatus("current")


class _QtechAclModeVC_Type(Integer32):
    """Custom type qtechAclModeVC based on Integer32"""
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


_QtechAclModeVC_Type.__name__ = "Integer32"
_QtechAclModeVC_Object = MibTableColumn
qtechAclModeVC = _QtechAclModeVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 1, 1, 3),
    _QtechAclModeVC_Type()
)
qtechAclModeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAclModeVC.setStatus("current")
_QtechAclEntryStatusVC_Type = ConfigStatus
_QtechAclEntryStatusVC_Object = MibTableColumn
qtechAclEntryStatusVC = _QtechAclEntryStatusVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 1, 1, 4),
    _QtechAclEntryStatusVC_Type()
)
qtechAclEntryStatusVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAclEntryStatusVC.setStatus("current")
_QtechAclIfVCTable_Object = MibTable
qtechAclIfVCTable = _QtechAclIfVCTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 2)
)
if mibBuilder.loadTexts:
    qtechAclIfVCTable.setStatus("current")
_QtechAclIfVCEntry_Object = MibTableRow
qtechAclIfVCEntry = _QtechAclIfVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 2, 1)
)
qtechAclIfVCEntry.setIndexNames(
    (0, "QTECH-ACL-CONTEXT-MIB", "qtechAclIfContextNameVC"),
    (0, "QTECH-ACL-CONTEXT-MIB", "qtechAclIfIndexVC"),
)
if mibBuilder.loadTexts:
    qtechAclIfVCEntry.setStatus("current")


class _QtechAclIfContextNameVC_Type(DisplayString):
    """Custom type qtechAclIfContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_QtechAclIfContextNameVC_Type.__name__ = "DisplayString"
_QtechAclIfContextNameVC_Object = MibTableColumn
qtechAclIfContextNameVC = _QtechAclIfContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 2, 1, 1),
    _QtechAclIfContextNameVC_Type()
)
qtechAclIfContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAclIfContextNameVC.setStatus("current")
_QtechAclIfIndexVC_Type = IfIndex
_QtechAclIfIndexVC_Object = MibTableColumn
qtechAclIfIndexVC = _QtechAclIfIndexVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 2, 1, 2),
    _QtechAclIfIndexVC_Type()
)
qtechAclIfIndexVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAclIfIndexVC.setStatus("current")
_QtechAclIfMaxEntryNumVC_Type = Integer32
_QtechAclIfMaxEntryNumVC_Object = MibTableColumn
qtechAclIfMaxEntryNumVC = _QtechAclIfMaxEntryNumVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 2, 1, 3),
    _QtechAclIfMaxEntryNumVC_Type()
)
qtechAclIfMaxEntryNumVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAclIfMaxEntryNumVC.setStatus("current")
_QtechAclIfCurruntEntryNumVC_Type = Integer32
_QtechAclIfCurruntEntryNumVC_Object = MibTableColumn
qtechAclIfCurruntEntryNumVC = _QtechAclIfCurruntEntryNumVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 2, 1, 4),
    _QtechAclIfCurruntEntryNumVC_Type()
)
qtechAclIfCurruntEntryNumVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAclIfCurruntEntryNumVC.setStatus("current")


class _QtechIfInAclNameVC_Type(DisplayString):
    """Custom type qtechIfInAclNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechIfInAclNameVC_Type.__name__ = "DisplayString"
_QtechIfInAclNameVC_Object = MibTableColumn
qtechIfInAclNameVC = _QtechIfInAclNameVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 2, 1, 5),
    _QtechIfInAclNameVC_Type()
)
qtechIfInAclNameVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfInAclNameVC.setStatus("current")


class _QtechIfOutAclNameVC_Type(DisplayString):
    """Custom type qtechIfOutAclNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechIfOutAclNameVC_Type.__name__ = "DisplayString"
_QtechIfOutAclNameVC_Object = MibTableColumn
qtechIfOutAclNameVC = _QtechIfOutAclNameVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 2, 1, 6),
    _QtechIfOutAclNameVC_Type()
)
qtechIfOutAclNameVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfOutAclNameVC.setStatus("current")
_QtechAceExtVCTable_Object = MibTable
qtechAceExtVCTable = _QtechAceExtVCTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3)
)
if mibBuilder.loadTexts:
    qtechAceExtVCTable.setStatus("current")
_QtechAceExtVCEntry_Object = MibTableRow
qtechAceExtVCEntry = _QtechAceExtVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1)
)
qtechAceExtVCEntry.setIndexNames(
    (0, "QTECH-ACL-CONTEXT-MIB", "qtechAceExtContextNameVC"),
    (0, "QTECH-ACL-CONTEXT-MIB", "qtechAceExtAclNameVC"),
    (0, "QTECH-ACL-CONTEXT-MIB", "qtechAceExtIndexVC"),
)
if mibBuilder.loadTexts:
    qtechAceExtVCEntry.setStatus("current")


class _QtechAceExtContextNameVC_Type(DisplayString):
    """Custom type qtechAceExtContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_QtechAceExtContextNameVC_Type.__name__ = "DisplayString"
_QtechAceExtContextNameVC_Object = MibTableColumn
qtechAceExtContextNameVC = _QtechAceExtContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 1),
    _QtechAceExtContextNameVC_Type()
)
qtechAceExtContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAceExtContextNameVC.setStatus("current")


class _QtechAceExtAclNameVC_Type(DisplayString):
    """Custom type qtechAceExtAclNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechAceExtAclNameVC_Type.__name__ = "DisplayString"
_QtechAceExtAclNameVC_Object = MibTableColumn
qtechAceExtAclNameVC = _QtechAceExtAclNameVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 2),
    _QtechAceExtAclNameVC_Type()
)
qtechAceExtAclNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAceExtAclNameVC.setStatus("current")


class _QtechAceExtIndexVC_Type(Integer32):
    """Custom type qtechAceExtIndexVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechAceExtIndexVC_Type.__name__ = "Integer32"
_QtechAceExtIndexVC_Object = MibTableColumn
qtechAceExtIndexVC = _QtechAceExtIndexVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 3),
    _QtechAceExtIndexVC_Type()
)
qtechAceExtIndexVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAceExtIndexVC.setStatus("current")


class _QtechAceExtIfAnyVIDVC_Type(TruthValue):
    """Custom type qtechAceExtIfAnyVIDVC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyVIDVC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyVIDVC_Object = MibTableColumn
qtechAceExtIfAnyVIDVC = _QtechAceExtIfAnyVIDVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 4),
    _QtechAceExtIfAnyVIDVC_Type()
)
qtechAceExtIfAnyVIDVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyVIDVC.setStatus("current")


class _QtechAceExtVIDVC_Type(Unsigned32):
    """Custom type qtechAceExtVIDVC based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_QtechAceExtVIDVC_Type.__name__ = "Unsigned32"
_QtechAceExtVIDVC_Object = MibTableColumn
qtechAceExtVIDVC = _QtechAceExtVIDVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 5),
    _QtechAceExtVIDVC_Type()
)
qtechAceExtVIDVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtVIDVC.setStatus("current")


class _QtechAceExtIfAnySourceIpVC_Type(TruthValue):
    """Custom type qtechAceExtIfAnySourceIpVC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnySourceIpVC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnySourceIpVC_Object = MibTableColumn
qtechAceExtIfAnySourceIpVC = _QtechAceExtIfAnySourceIpVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 6),
    _QtechAceExtIfAnySourceIpVC_Type()
)
qtechAceExtIfAnySourceIpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnySourceIpVC.setStatus("current")
_QtechAceExtSourceIpVC_Type = IpAddress
_QtechAceExtSourceIpVC_Object = MibTableColumn
qtechAceExtSourceIpVC = _QtechAceExtSourceIpVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 7),
    _QtechAceExtSourceIpVC_Type()
)
qtechAceExtSourceIpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtSourceIpVC.setStatus("current")


class _QtechAceExtIfAnySourceWildCardVC_Type(TruthValue):
    """Custom type qtechAceExtIfAnySourceWildCardVC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnySourceWildCardVC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnySourceWildCardVC_Object = MibTableColumn
qtechAceExtIfAnySourceWildCardVC = _QtechAceExtIfAnySourceWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 8),
    _QtechAceExtIfAnySourceWildCardVC_Type()
)
qtechAceExtIfAnySourceWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnySourceWildCardVC.setStatus("current")
_QtechAceExtSourceWildCardVC_Type = IpAddress
_QtechAceExtSourceWildCardVC_Object = MibTableColumn
qtechAceExtSourceWildCardVC = _QtechAceExtSourceWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 9),
    _QtechAceExtSourceWildCardVC_Type()
)
qtechAceExtSourceWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtSourceWildCardVC.setStatus("current")


class _QtechAceExtIfAnySourceMacAddrVC_Type(TruthValue):
    """Custom type qtechAceExtIfAnySourceMacAddrVC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnySourceMacAddrVC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnySourceMacAddrVC_Object = MibTableColumn
qtechAceExtIfAnySourceMacAddrVC = _QtechAceExtIfAnySourceMacAddrVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 10),
    _QtechAceExtIfAnySourceMacAddrVC_Type()
)
qtechAceExtIfAnySourceMacAddrVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnySourceMacAddrVC.setStatus("current")
_QtechAceExtSourceMacAddrVC_Type = MacAddress
_QtechAceExtSourceMacAddrVC_Object = MibTableColumn
qtechAceExtSourceMacAddrVC = _QtechAceExtSourceMacAddrVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 11),
    _QtechAceExtSourceMacAddrVC_Type()
)
qtechAceExtSourceMacAddrVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtSourceMacAddrVC.setStatus("current")


class _QtechAceExtIfAnyDestIpVC_Type(TruthValue):
    """Custom type qtechAceExtIfAnyDestIpVC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyDestIpVC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyDestIpVC_Object = MibTableColumn
qtechAceExtIfAnyDestIpVC = _QtechAceExtIfAnyDestIpVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 12),
    _QtechAceExtIfAnyDestIpVC_Type()
)
qtechAceExtIfAnyDestIpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyDestIpVC.setStatus("current")
_QtechAceExtDestIpVC_Type = IpAddress
_QtechAceExtDestIpVC_Object = MibTableColumn
qtechAceExtDestIpVC = _QtechAceExtDestIpVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 13),
    _QtechAceExtDestIpVC_Type()
)
qtechAceExtDestIpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtDestIpVC.setStatus("current")


class _QtechAceExtIfAnyDestWildCardVC_Type(TruthValue):
    """Custom type qtechAceExtIfAnyDestWildCardVC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyDestWildCardVC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyDestWildCardVC_Object = MibTableColumn
qtechAceExtIfAnyDestWildCardVC = _QtechAceExtIfAnyDestWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 14),
    _QtechAceExtIfAnyDestWildCardVC_Type()
)
qtechAceExtIfAnyDestWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyDestWildCardVC.setStatus("current")
_QtechAceExtDestIpWildCardVC_Type = IpAddress
_QtechAceExtDestIpWildCardVC_Object = MibTableColumn
qtechAceExtDestIpWildCardVC = _QtechAceExtDestIpWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 15),
    _QtechAceExtDestIpWildCardVC_Type()
)
qtechAceExtDestIpWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtDestIpWildCardVC.setStatus("current")


class _QtechAceExtIfAnyDestMacAddrVC_Type(TruthValue):
    """Custom type qtechAceExtIfAnyDestMacAddrVC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyDestMacAddrVC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyDestMacAddrVC_Object = MibTableColumn
qtechAceExtIfAnyDestMacAddrVC = _QtechAceExtIfAnyDestMacAddrVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 16),
    _QtechAceExtIfAnyDestMacAddrVC_Type()
)
qtechAceExtIfAnyDestMacAddrVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyDestMacAddrVC.setStatus("current")
_QtechAceExtDestMacAddrVC_Type = MacAddress
_QtechAceExtDestMacAddrVC_Object = MibTableColumn
qtechAceExtDestMacAddrVC = _QtechAceExtDestMacAddrVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 17),
    _QtechAceExtDestMacAddrVC_Type()
)
qtechAceExtDestMacAddrVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtDestMacAddrVC.setStatus("current")


class _QtechAceExtIfAnyEtherLikeTypeVC_Type(TruthValue):
    """Custom type qtechAceExtIfAnyEtherLikeTypeVC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyEtherLikeTypeVC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyEtherLikeTypeVC_Object = MibTableColumn
qtechAceExtIfAnyEtherLikeTypeVC = _QtechAceExtIfAnyEtherLikeTypeVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 18),
    _QtechAceExtIfAnyEtherLikeTypeVC_Type()
)
qtechAceExtIfAnyEtherLikeTypeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyEtherLikeTypeVC.setStatus("current")
_QtechAceExtEtherLikeTypeVC_Type = Integer32
_QtechAceExtEtherLikeTypeVC_Object = MibTableColumn
qtechAceExtEtherLikeTypeVC = _QtechAceExtEtherLikeTypeVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 19),
    _QtechAceExtEtherLikeTypeVC_Type()
)
qtechAceExtEtherLikeTypeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtEtherLikeTypeVC.setStatus("current")


class _QtechAceExtIfAnyIpProtocolFieldVC_Type(TruthValue):
    """Custom type qtechAceExtIfAnyIpProtocolFieldVC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyIpProtocolFieldVC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyIpProtocolFieldVC_Object = MibTableColumn
qtechAceExtIfAnyIpProtocolFieldVC = _QtechAceExtIfAnyIpProtocolFieldVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 20),
    _QtechAceExtIfAnyIpProtocolFieldVC_Type()
)
qtechAceExtIfAnyIpProtocolFieldVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyIpProtocolFieldVC.setStatus("current")
_QtechAceExtIpProtocolFieldVC_Type = Integer32
_QtechAceExtIpProtocolFieldVC_Object = MibTableColumn
qtechAceExtIpProtocolFieldVC = _QtechAceExtIpProtocolFieldVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 21),
    _QtechAceExtIpProtocolFieldVC_Type()
)
qtechAceExtIpProtocolFieldVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIpProtocolFieldVC.setStatus("current")
_QtechAceExtSourceProtocolPortVC_Type = Integer32
_QtechAceExtSourceProtocolPortVC_Object = MibTableColumn
qtechAceExtSourceProtocolPortVC = _QtechAceExtSourceProtocolPortVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 22),
    _QtechAceExtSourceProtocolPortVC_Type()
)
qtechAceExtSourceProtocolPortVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtSourceProtocolPortVC.setStatus("current")
_QtechAceExtDestProtocolPortVC_Type = Integer32
_QtechAceExtDestProtocolPortVC_Object = MibTableColumn
qtechAceExtDestProtocolPortVC = _QtechAceExtDestProtocolPortVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 23),
    _QtechAceExtDestProtocolPortVC_Type()
)
qtechAceExtDestProtocolPortVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtDestProtocolPortVC.setStatus("current")


class _QtechAceExtIfAnyProtocolTypeVC_Type(TruthValue):
    """Custom type qtechAceExtIfAnyProtocolTypeVC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyProtocolTypeVC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyProtocolTypeVC_Object = MibTableColumn
qtechAceExtIfAnyProtocolTypeVC = _QtechAceExtIfAnyProtocolTypeVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 24),
    _QtechAceExtIfAnyProtocolTypeVC_Type()
)
qtechAceExtIfAnyProtocolTypeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyProtocolTypeVC.setStatus("current")
_QtechAceExtProtocolTypeVC_Type = Integer32
_QtechAceExtProtocolTypeVC_Object = MibTableColumn
qtechAceExtProtocolTypeVC = _QtechAceExtProtocolTypeVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 25),
    _QtechAceExtProtocolTypeVC_Type()
)
qtechAceExtProtocolTypeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtProtocolTypeVC.setStatus("current")


class _QtechAceExtFlowActionVC_Type(Integer32):
    """Custom type qtechAceExtFlowActionVC based on Integer32"""
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


_QtechAceExtFlowActionVC_Type.__name__ = "Integer32"
_QtechAceExtFlowActionVC_Object = MibTableColumn
qtechAceExtFlowActionVC = _QtechAceExtFlowActionVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 26),
    _QtechAceExtFlowActionVC_Type()
)
qtechAceExtFlowActionVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtFlowActionVC.setStatus("current")
_QtechAceExtEntryStautsVC_Type = RowStatus
_QtechAceExtEntryStautsVC_Object = MibTableColumn
qtechAceExtEntryStautsVC = _QtechAceExtEntryStautsVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 27),
    _QtechAceExtEntryStautsVC_Type()
)
qtechAceExtEntryStautsVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtEntryStautsVC.setStatus("current")


class _QtechAceExtTimeRangeNameVC_Type(DisplayString):
    """Custom type qtechAceExtTimeRangeNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechAceExtTimeRangeNameVC_Type.__name__ = "DisplayString"
_QtechAceExtTimeRangeNameVC_Object = MibTableColumn
qtechAceExtTimeRangeNameVC = _QtechAceExtTimeRangeNameVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 28),
    _QtechAceExtTimeRangeNameVC_Type()
)
qtechAceExtTimeRangeNameVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtTimeRangeNameVC.setStatus("current")


class _QtechAceExtSourcePortOpVC_Type(Integer32):
    """Custom type qtechAceExtSourcePortOpVC based on Integer32"""
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


_QtechAceExtSourcePortOpVC_Type.__name__ = "Integer32"
_QtechAceExtSourcePortOpVC_Object = MibTableColumn
qtechAceExtSourcePortOpVC = _QtechAceExtSourcePortOpVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 29),
    _QtechAceExtSourcePortOpVC_Type()
)
qtechAceExtSourcePortOpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtSourcePortOpVC.setStatus("current")
_QtechAceExtSourceProtocolPortRangeVC_Type = Integer32
_QtechAceExtSourceProtocolPortRangeVC_Object = MibTableColumn
qtechAceExtSourceProtocolPortRangeVC = _QtechAceExtSourceProtocolPortRangeVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 30),
    _QtechAceExtSourceProtocolPortRangeVC_Type()
)
qtechAceExtSourceProtocolPortRangeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtSourceProtocolPortRangeVC.setStatus("current")


class _QtechAceExtDestPortOpVC_Type(Integer32):
    """Custom type qtechAceExtDestPortOpVC based on Integer32"""
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


_QtechAceExtDestPortOpVC_Type.__name__ = "Integer32"
_QtechAceExtDestPortOpVC_Object = MibTableColumn
qtechAceExtDestPortOpVC = _QtechAceExtDestPortOpVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 31),
    _QtechAceExtDestPortOpVC_Type()
)
qtechAceExtDestPortOpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtDestPortOpVC.setStatus("current")
_QtechAceExtDestProtocolPortRangeVC_Type = Integer32
_QtechAceExtDestProtocolPortRangeVC_Object = MibTableColumn
qtechAceExtDestProtocolPortRangeVC = _QtechAceExtDestProtocolPortRangeVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 32),
    _QtechAceExtDestProtocolPortRangeVC_Type()
)
qtechAceExtDestProtocolPortRangeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtDestProtocolPortRangeVC.setStatus("current")


class _QtechAceExtIfAnyCosVC_Type(TruthValue):
    """Custom type qtechAceExtIfAnyCosVC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyCosVC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyCosVC_Object = MibTableColumn
qtechAceExtIfAnyCosVC = _QtechAceExtIfAnyCosVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 33),
    _QtechAceExtIfAnyCosVC_Type()
)
qtechAceExtIfAnyCosVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyCosVC.setStatus("current")
_QtechAceExtCosVC_Type = Integer32
_QtechAceExtCosVC_Object = MibTableColumn
qtechAceExtCosVC = _QtechAceExtCosVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 34),
    _QtechAceExtCosVC_Type()
)
qtechAceExtCosVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtCosVC.setStatus("current")


class _QtechAceExtIfAnyIpPrecVC_Type(TruthValue):
    """Custom type qtechAceExtIfAnyIpPrecVC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyIpPrecVC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyIpPrecVC_Object = MibTableColumn
qtechAceExtIfAnyIpPrecVC = _QtechAceExtIfAnyIpPrecVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 35),
    _QtechAceExtIfAnyIpPrecVC_Type()
)
qtechAceExtIfAnyIpPrecVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyIpPrecVC.setStatus("current")
_QtechAceExtIpPrecVC_Type = Integer32
_QtechAceExtIpPrecVC_Object = MibTableColumn
qtechAceExtIpPrecVC = _QtechAceExtIpPrecVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 36),
    _QtechAceExtIpPrecVC_Type()
)
qtechAceExtIpPrecVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIpPrecVC.setStatus("current")


class _QtechAceExtIfAnyDscpVC_Type(TruthValue):
    """Custom type qtechAceExtIfAnyDscpVC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyDscpVC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyDscpVC_Object = MibTableColumn
qtechAceExtIfAnyDscpVC = _QtechAceExtIfAnyDscpVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 37),
    _QtechAceExtIfAnyDscpVC_Type()
)
qtechAceExtIfAnyDscpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyDscpVC.setStatus("current")
_QtechAceExtDscpVC_Type = Integer32
_QtechAceExtDscpVC_Object = MibTableColumn
qtechAceExtDscpVC = _QtechAceExtDscpVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 38),
    _QtechAceExtDscpVC_Type()
)
qtechAceExtDscpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtDscpVC.setStatus("current")


class _QtechAceExtIfAnyTcpFlagVC_Type(TruthValue):
    """Custom type qtechAceExtIfAnyTcpFlagVC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyTcpFlagVC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyTcpFlagVC_Object = MibTableColumn
qtechAceExtIfAnyTcpFlagVC = _QtechAceExtIfAnyTcpFlagVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 39),
    _QtechAceExtIfAnyTcpFlagVC_Type()
)
qtechAceExtIfAnyTcpFlagVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyTcpFlagVC.setStatus("current")
_QtechAceExtTcpFlagVC_Type = Integer32
_QtechAceExtTcpFlagVC_Object = MibTableColumn
qtechAceExtTcpFlagVC = _QtechAceExtTcpFlagVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 40),
    _QtechAceExtTcpFlagVC_Type()
)
qtechAceExtTcpFlagVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtTcpFlagVC.setStatus("current")


class _QtechAceExtIfAnySourceMacAddrWildCardVC_Type(TruthValue):
    """Custom type qtechAceExtIfAnySourceMacAddrWildCardVC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnySourceMacAddrWildCardVC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnySourceMacAddrWildCardVC_Object = MibTableColumn
qtechAceExtIfAnySourceMacAddrWildCardVC = _QtechAceExtIfAnySourceMacAddrWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 41),
    _QtechAceExtIfAnySourceMacAddrWildCardVC_Type()
)
qtechAceExtIfAnySourceMacAddrWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnySourceMacAddrWildCardVC.setStatus("current")
_QtechAceExtSourceMacAddrWildCardVC_Type = MacAddress
_QtechAceExtSourceMacAddrWildCardVC_Object = MibTableColumn
qtechAceExtSourceMacAddrWildCardVC = _QtechAceExtSourceMacAddrWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 42),
    _QtechAceExtSourceMacAddrWildCardVC_Type()
)
qtechAceExtSourceMacAddrWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtSourceMacAddrWildCardVC.setStatus("current")


class _QtechAceExtIfAnyDestMacAddrWildCardVC_Type(TruthValue):
    """Custom type qtechAceExtIfAnyDestMacAddrWildCardVC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyDestMacAddrWildCardVC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyDestMacAddrWildCardVC_Object = MibTableColumn
qtechAceExtIfAnyDestMacAddrWildCardVC = _QtechAceExtIfAnyDestMacAddrWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 43),
    _QtechAceExtIfAnyDestMacAddrWildCardVC_Type()
)
qtechAceExtIfAnyDestMacAddrWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyDestMacAddrWildCardVC.setStatus("current")
_QtechAceExtDestMacAddrWildCardVC_Type = MacAddress
_QtechAceExtDestMacAddrWildCardVC_Object = MibTableColumn
qtechAceExtDestMacAddrWildCardVC = _QtechAceExtDestMacAddrWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 44),
    _QtechAceExtDestMacAddrWildCardVC_Type()
)
qtechAceExtDestMacAddrWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtDestMacAddrWildCardVC.setStatus("current")


class _QtechAceExtIfAnySourceIp6VC_Type(TruthValue):
    """Custom type qtechAceExtIfAnySourceIp6VC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnySourceIp6VC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnySourceIp6VC_Object = MibTableColumn
qtechAceExtIfAnySourceIp6VC = _QtechAceExtIfAnySourceIp6VC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 45),
    _QtechAceExtIfAnySourceIp6VC_Type()
)
qtechAceExtIfAnySourceIp6VC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnySourceIp6VC.setStatus("current")


class _QtechAceExtSourceIp6VC_Type(OctetString):
    """Custom type qtechAceExtSourceIp6VC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_QtechAceExtSourceIp6VC_Type.__name__ = "OctetString"
_QtechAceExtSourceIp6VC_Object = MibTableColumn
qtechAceExtSourceIp6VC = _QtechAceExtSourceIp6VC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 46),
    _QtechAceExtSourceIp6VC_Type()
)
qtechAceExtSourceIp6VC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtSourceIp6VC.setStatus("current")


class _QtechAceExtIfAnySourceIp6WildCardVC_Type(TruthValue):
    """Custom type qtechAceExtIfAnySourceIp6WildCardVC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnySourceIp6WildCardVC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnySourceIp6WildCardVC_Object = MibTableColumn
qtechAceExtIfAnySourceIp6WildCardVC = _QtechAceExtIfAnySourceIp6WildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 47),
    _QtechAceExtIfAnySourceIp6WildCardVC_Type()
)
qtechAceExtIfAnySourceIp6WildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnySourceIp6WildCardVC.setStatus("current")


class _QtechAceExtSourceIp6WildCardVC_Type(OctetString):
    """Custom type qtechAceExtSourceIp6WildCardVC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_QtechAceExtSourceIp6WildCardVC_Type.__name__ = "OctetString"
_QtechAceExtSourceIp6WildCardVC_Object = MibTableColumn
qtechAceExtSourceIp6WildCardVC = _QtechAceExtSourceIp6WildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 48),
    _QtechAceExtSourceIp6WildCardVC_Type()
)
qtechAceExtSourceIp6WildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtSourceIp6WildCardVC.setStatus("current")


class _QtechAceExtIfAnyDestIp6VC_Type(TruthValue):
    """Custom type qtechAceExtIfAnyDestIp6VC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyDestIp6VC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyDestIp6VC_Object = MibTableColumn
qtechAceExtIfAnyDestIp6VC = _QtechAceExtIfAnyDestIp6VC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 49),
    _QtechAceExtIfAnyDestIp6VC_Type()
)
qtechAceExtIfAnyDestIp6VC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyDestIp6VC.setStatus("current")


class _QtechAceExtDestIp6VC_Type(OctetString):
    """Custom type qtechAceExtDestIp6VC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_QtechAceExtDestIp6VC_Type.__name__ = "OctetString"
_QtechAceExtDestIp6VC_Object = MibTableColumn
qtechAceExtDestIp6VC = _QtechAceExtDestIp6VC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 50),
    _QtechAceExtDestIp6VC_Type()
)
qtechAceExtDestIp6VC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtDestIp6VC.setStatus("current")


class _QtechAceExtIfAnyDestIp6WildCardVC_Type(TruthValue):
    """Custom type qtechAceExtIfAnyDestIp6WildCardVC based on TruthValue"""
    defaultValue = 1


_QtechAceExtIfAnyDestIp6WildCardVC_Type.__name__ = "TruthValue"
_QtechAceExtIfAnyDestIp6WildCardVC_Object = MibTableColumn
qtechAceExtIfAnyDestIp6WildCardVC = _QtechAceExtIfAnyDestIp6WildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 51),
    _QtechAceExtIfAnyDestIp6WildCardVC_Type()
)
qtechAceExtIfAnyDestIp6WildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtIfAnyDestIp6WildCardVC.setStatus("current")


class _QtechAceExtDestIp6WildCardVC_Type(OctetString):
    """Custom type qtechAceExtDestIp6WildCardVC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_QtechAceExtDestIp6WildCardVC_Type.__name__ = "OctetString"
_QtechAceExtDestIp6WildCardVC_Object = MibTableColumn
qtechAceExtDestIp6WildCardVC = _QtechAceExtDestIp6WildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 1, 3, 1, 52),
    _QtechAceExtDestIp6WildCardVC_Type()
)
qtechAceExtDestIp6WildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAceExtDestIp6WildCardVC.setStatus("current")
_QtechAclVCMIBConformance_ObjectIdentity = ObjectIdentity
qtechAclVCMIBConformance = _QtechAclVCMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 2)
)
_QtechAclVCMIBCompliances_ObjectIdentity = ObjectIdentity
qtechAclVCMIBCompliances = _QtechAclVCMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 2, 1)
)
_QtechAclVCMIBGroups_ObjectIdentity = ObjectIdentity
qtechAclVCMIBGroups = _QtechAclVCMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 2, 2)
)

# Managed Objects groups

qtechAclVCMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 2, 2, 1)
)
qtechAclVCMIBGroup.setObjects(
      *(("QTECH-ACL-CONTEXT-MIB", "qtechAclContextNameVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAclNameVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAclModeVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAclEntryStatusVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtContextNameVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtAclNameVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIndexVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnyVIDVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtVIDVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnySourceIpVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtSourceIpVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnySourceWildCardVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtSourceWildCardVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnySourceMacAddrVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtSourceMacAddrVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnyDestIpVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtDestIpVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnyDestWildCardVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtDestIpWildCardVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnyDestMacAddrVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtDestMacAddrVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnyEtherLikeTypeVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtEtherLikeTypeVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnyIpProtocolFieldVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIpProtocolFieldVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtSourceProtocolPortVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtDestProtocolPortVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtProtocolTypeVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtProtocolTypeVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtFlowActionVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtEntryStautsVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtTimeRangeNameVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtSourcePortOpVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtSourceProtocolPortRangeVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtDestPortOpVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtDestProtocolPortRangeVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnyCosVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtCosVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnyIpPrecVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIpPrecVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnyDscpVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtDscpVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnyTcpFlagVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtTcpFlagVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnySourceMacAddrWildCardVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtSourceMacAddrWildCardVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnyDestMacAddrWildCardVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtDestMacAddrWildCardVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnySourceIp6VC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtSourceIp6VC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnySourceIp6WildCardVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtSourceIp6WildCardVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnyDestIp6VC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtDestIp6VC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtIfAnyDestIp6WildCardVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAceExtDestIp6WildCardVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAclIfContextNameVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAclIfIndexVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAclIfMaxEntryNumVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechAclIfCurruntEntryNumVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechIfInAclNameVC"),
        ("QTECH-ACL-CONTEXT-MIB", "qtechIfOutAclNameVC"))
)
if mibBuilder.loadTexts:
    qtechAclVCMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechAclVCMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 66, 2, 1, 1)
)
qtechAclVCMIBCompliance.setObjects(
    ("QTECH-ACL-CONTEXT-MIB", "qtechAclVCMIBGroup")
)
if mibBuilder.loadTexts:
    qtechAclVCMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-ACL-CONTEXT-MIB",
    **{"qtechAclVCMIB": qtechAclVCMIB,
       "qtechAclVCMIBObjects": qtechAclVCMIBObjects,
       "qtechAclVCTable": qtechAclVCTable,
       "qtechAclVCEntry": qtechAclVCEntry,
       "qtechAclContextNameVC": qtechAclContextNameVC,
       "qtechAclNameVC": qtechAclNameVC,
       "qtechAclModeVC": qtechAclModeVC,
       "qtechAclEntryStatusVC": qtechAclEntryStatusVC,
       "qtechAclIfVCTable": qtechAclIfVCTable,
       "qtechAclIfVCEntry": qtechAclIfVCEntry,
       "qtechAclIfContextNameVC": qtechAclIfContextNameVC,
       "qtechAclIfIndexVC": qtechAclIfIndexVC,
       "qtechAclIfMaxEntryNumVC": qtechAclIfMaxEntryNumVC,
       "qtechAclIfCurruntEntryNumVC": qtechAclIfCurruntEntryNumVC,
       "qtechIfInAclNameVC": qtechIfInAclNameVC,
       "qtechIfOutAclNameVC": qtechIfOutAclNameVC,
       "qtechAceExtVCTable": qtechAceExtVCTable,
       "qtechAceExtVCEntry": qtechAceExtVCEntry,
       "qtechAceExtContextNameVC": qtechAceExtContextNameVC,
       "qtechAceExtAclNameVC": qtechAceExtAclNameVC,
       "qtechAceExtIndexVC": qtechAceExtIndexVC,
       "qtechAceExtIfAnyVIDVC": qtechAceExtIfAnyVIDVC,
       "qtechAceExtVIDVC": qtechAceExtVIDVC,
       "qtechAceExtIfAnySourceIpVC": qtechAceExtIfAnySourceIpVC,
       "qtechAceExtSourceIpVC": qtechAceExtSourceIpVC,
       "qtechAceExtIfAnySourceWildCardVC": qtechAceExtIfAnySourceWildCardVC,
       "qtechAceExtSourceWildCardVC": qtechAceExtSourceWildCardVC,
       "qtechAceExtIfAnySourceMacAddrVC": qtechAceExtIfAnySourceMacAddrVC,
       "qtechAceExtSourceMacAddrVC": qtechAceExtSourceMacAddrVC,
       "qtechAceExtIfAnyDestIpVC": qtechAceExtIfAnyDestIpVC,
       "qtechAceExtDestIpVC": qtechAceExtDestIpVC,
       "qtechAceExtIfAnyDestWildCardVC": qtechAceExtIfAnyDestWildCardVC,
       "qtechAceExtDestIpWildCardVC": qtechAceExtDestIpWildCardVC,
       "qtechAceExtIfAnyDestMacAddrVC": qtechAceExtIfAnyDestMacAddrVC,
       "qtechAceExtDestMacAddrVC": qtechAceExtDestMacAddrVC,
       "qtechAceExtIfAnyEtherLikeTypeVC": qtechAceExtIfAnyEtherLikeTypeVC,
       "qtechAceExtEtherLikeTypeVC": qtechAceExtEtherLikeTypeVC,
       "qtechAceExtIfAnyIpProtocolFieldVC": qtechAceExtIfAnyIpProtocolFieldVC,
       "qtechAceExtIpProtocolFieldVC": qtechAceExtIpProtocolFieldVC,
       "qtechAceExtSourceProtocolPortVC": qtechAceExtSourceProtocolPortVC,
       "qtechAceExtDestProtocolPortVC": qtechAceExtDestProtocolPortVC,
       "qtechAceExtIfAnyProtocolTypeVC": qtechAceExtIfAnyProtocolTypeVC,
       "qtechAceExtProtocolTypeVC": qtechAceExtProtocolTypeVC,
       "qtechAceExtFlowActionVC": qtechAceExtFlowActionVC,
       "qtechAceExtEntryStautsVC": qtechAceExtEntryStautsVC,
       "qtechAceExtTimeRangeNameVC": qtechAceExtTimeRangeNameVC,
       "qtechAceExtSourcePortOpVC": qtechAceExtSourcePortOpVC,
       "qtechAceExtSourceProtocolPortRangeVC": qtechAceExtSourceProtocolPortRangeVC,
       "qtechAceExtDestPortOpVC": qtechAceExtDestPortOpVC,
       "qtechAceExtDestProtocolPortRangeVC": qtechAceExtDestProtocolPortRangeVC,
       "qtechAceExtIfAnyCosVC": qtechAceExtIfAnyCosVC,
       "qtechAceExtCosVC": qtechAceExtCosVC,
       "qtechAceExtIfAnyIpPrecVC": qtechAceExtIfAnyIpPrecVC,
       "qtechAceExtIpPrecVC": qtechAceExtIpPrecVC,
       "qtechAceExtIfAnyDscpVC": qtechAceExtIfAnyDscpVC,
       "qtechAceExtDscpVC": qtechAceExtDscpVC,
       "qtechAceExtIfAnyTcpFlagVC": qtechAceExtIfAnyTcpFlagVC,
       "qtechAceExtTcpFlagVC": qtechAceExtTcpFlagVC,
       "qtechAceExtIfAnySourceMacAddrWildCardVC": qtechAceExtIfAnySourceMacAddrWildCardVC,
       "qtechAceExtSourceMacAddrWildCardVC": qtechAceExtSourceMacAddrWildCardVC,
       "qtechAceExtIfAnyDestMacAddrWildCardVC": qtechAceExtIfAnyDestMacAddrWildCardVC,
       "qtechAceExtDestMacAddrWildCardVC": qtechAceExtDestMacAddrWildCardVC,
       "qtechAceExtIfAnySourceIp6VC": qtechAceExtIfAnySourceIp6VC,
       "qtechAceExtSourceIp6VC": qtechAceExtSourceIp6VC,
       "qtechAceExtIfAnySourceIp6WildCardVC": qtechAceExtIfAnySourceIp6WildCardVC,
       "qtechAceExtSourceIp6WildCardVC": qtechAceExtSourceIp6WildCardVC,
       "qtechAceExtIfAnyDestIp6VC": qtechAceExtIfAnyDestIp6VC,
       "qtechAceExtDestIp6VC": qtechAceExtDestIp6VC,
       "qtechAceExtIfAnyDestIp6WildCardVC": qtechAceExtIfAnyDestIp6WildCardVC,
       "qtechAceExtDestIp6WildCardVC": qtechAceExtDestIp6WildCardVC,
       "qtechAclVCMIBConformance": qtechAclVCMIBConformance,
       "qtechAclVCMIBCompliances": qtechAclVCMIBCompliances,
       "qtechAclVCMIBCompliance": qtechAclVCMIBCompliance,
       "qtechAclVCMIBGroups": qtechAclVCMIBGroups,
       "qtechAclVCMIBGroup": qtechAclVCMIBGroup}
)
