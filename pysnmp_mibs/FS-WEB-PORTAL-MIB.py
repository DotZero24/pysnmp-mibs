# SNMP MIB module (FS-WEB-PORTAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-WEB-PORTAL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:48 2025
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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsWebPortalMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69)
)
if mibBuilder.loadTexts:
    fsWebPortalMIB.setRevisions(
        ("2010-02-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsWebPortalMIBObjects_ObjectIdentity = ObjectIdentity
fsWebPortalMIBObjects = _FsWebPortalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1)
)
_FsWebPortalGlobalMIBObjects_ObjectIdentity = ObjectIdentity
fsWebPortalGlobalMIBObjects = _FsWebPortalGlobalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 1)
)


class _FsWebPortalGlbWebAuthType_Type(Integer32):
    """Custom type fsWebPortalGlbWebAuthType based on Integer32"""
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
        *(("internal", 0),
          ("customized", 1),
          ("external", 2))
    )


_FsWebPortalGlbWebAuthType_Type.__name__ = "Integer32"
_FsWebPortalGlbWebAuthType_Object = MibScalar
fsWebPortalGlbWebAuthType = _FsWebPortalGlbWebAuthType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 1, 1),
    _FsWebPortalGlbWebAuthType_Type()
)
fsWebPortalGlbWebAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWebPortalGlbWebAuthType.setStatus("current")


class _FsWebPortalGlbMethodList_Type(DisplayString):
    """Custom type fsWebPortalGlbMethodList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_FsWebPortalGlbMethodList_Type.__name__ = "DisplayString"
_FsWebPortalGlbMethodList_Object = MibScalar
fsWebPortalGlbMethodList = _FsWebPortalGlbMethodList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 1, 2),
    _FsWebPortalGlbMethodList_Type()
)
fsWebPortalGlbMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWebPortalGlbMethodList.setStatus("current")


class _FsWebPortalGlbCustomizedPageName_Type(DisplayString):
    """Custom type fsWebPortalGlbCustomizedPageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_FsWebPortalGlbCustomizedPageName_Type.__name__ = "DisplayString"
_FsWebPortalGlbCustomizedPageName_Object = MibScalar
fsWebPortalGlbCustomizedPageName = _FsWebPortalGlbCustomizedPageName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 1, 3),
    _FsWebPortalGlbCustomizedPageName_Type()
)
fsWebPortalGlbCustomizedPageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWebPortalGlbCustomizedPageName.setStatus("current")


class _FsWebPortalGlbExternalWebPortalURL_Type(DisplayString):
    """Custom type fsWebPortalGlbExternalWebPortalURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_FsWebPortalGlbExternalWebPortalURL_Type.__name__ = "DisplayString"
_FsWebPortalGlbExternalWebPortalURL_Object = MibScalar
fsWebPortalGlbExternalWebPortalURL = _FsWebPortalGlbExternalWebPortalURL_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 1, 4),
    _FsWebPortalGlbExternalWebPortalURL_Type()
)
fsWebPortalGlbExternalWebPortalURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWebPortalGlbExternalWebPortalURL.setStatus("current")


class _FsWebPortalGlbCustomizedLogoName_Type(DisplayString):
    """Custom type fsWebPortalGlbCustomizedLogoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_FsWebPortalGlbCustomizedLogoName_Type.__name__ = "DisplayString"
_FsWebPortalGlbCustomizedLogoName_Object = MibScalar
fsWebPortalGlbCustomizedLogoName = _FsWebPortalGlbCustomizedLogoName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 1, 5),
    _FsWebPortalGlbCustomizedLogoName_Type()
)
fsWebPortalGlbCustomizedLogoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWebPortalGlbCustomizedLogoName.setStatus("current")


class _FsWebPortalGlbEchoManufacturerLogo_Type(Integer32):
    """Custom type fsWebPortalGlbEchoManufacturerLogo based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsWebPortalGlbEchoManufacturerLogo_Type.__name__ = "Integer32"
_FsWebPortalGlbEchoManufacturerLogo_Object = MibScalar
fsWebPortalGlbEchoManufacturerLogo = _FsWebPortalGlbEchoManufacturerLogo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 1, 6),
    _FsWebPortalGlbEchoManufacturerLogo_Type()
)
fsWebPortalGlbEchoManufacturerLogo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWebPortalGlbEchoManufacturerLogo.setStatus("current")


class _FsWebPortalGlbWelcomeMsg_Type(OctetString):
    """Custom type fsWebPortalGlbWelcomeMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2047),
    )


_FsWebPortalGlbWelcomeMsg_Type.__name__ = "OctetString"
_FsWebPortalGlbWelcomeMsg_Object = MibScalar
fsWebPortalGlbWelcomeMsg = _FsWebPortalGlbWelcomeMsg_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 1, 7),
    _FsWebPortalGlbWelcomeMsg_Type()
)
fsWebPortalGlbWelcomeMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWebPortalGlbWelcomeMsg.setStatus("current")


class _FsWebPortalGlbWebPageTitle_Type(DisplayString):
    """Custom type fsWebPortalGlbWebPageTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_FsWebPortalGlbWebPageTitle_Type.__name__ = "DisplayString"
_FsWebPortalGlbWebPageTitle_Object = MibScalar
fsWebPortalGlbWebPageTitle = _FsWebPortalGlbWebPageTitle_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 1, 8),
    _FsWebPortalGlbWebPageTitle_Type()
)
fsWebPortalGlbWebPageTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWebPortalGlbWebPageTitle.setStatus("current")
_FsWebPortalLocalMIBObjects_ObjectIdentity = ObjectIdentity
fsWebPortalLocalMIBObjects = _FsWebPortalLocalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 2)
)
_FsWebPortalAuthTable_Object = MibTable
fsWebPortalAuthTable = _FsWebPortalAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsWebPortalAuthTable.setStatus("current")
_FsWebPortalAuthEntry_Object = MibTableRow
fsWebPortalAuthEntry = _FsWebPortalAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 2, 1, 1)
)
fsWebPortalAuthEntry.setIndexNames(
    (0, "FS-WEB-PORTAL-MIB", "fsWebPortalNetMode"),
    (0, "FS-WEB-PORTAL-MIB", "fsWebPortalNetID"),
)
if mibBuilder.loadTexts:
    fsWebPortalAuthEntry.setStatus("current")


class _FsWebPortalNetMode_Type(Integer32):
    """Custom type fsWebPortalNetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wlan", 1),
          ("ethernet", 2),
          ("vlan", 3))
    )


_FsWebPortalNetMode_Type.__name__ = "Integer32"
_FsWebPortalNetMode_Object = MibTableColumn
fsWebPortalNetMode = _FsWebPortalNetMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 2, 1, 1, 1),
    _FsWebPortalNetMode_Type()
)
fsWebPortalNetMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWebPortalNetMode.setStatus("current")


class _FsWebPortalNetID_Type(Integer32):
    """Custom type fsWebPortalNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_FsWebPortalNetID_Type.__name__ = "Integer32"
_FsWebPortalNetID_Object = MibTableColumn
fsWebPortalNetID = _FsWebPortalNetID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 2, 1, 1, 2),
    _FsWebPortalNetID_Type()
)
fsWebPortalNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWebPortalNetID.setStatus("current")


class _FsWebPortalWebAuthType_Type(Integer32):
    """Custom type fsWebPortalWebAuthType based on Integer32"""
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
        *(("internal", 0),
          ("customized", 1),
          ("external", 2))
    )


_FsWebPortalWebAuthType_Type.__name__ = "Integer32"
_FsWebPortalWebAuthType_Object = MibTableColumn
fsWebPortalWebAuthType = _FsWebPortalWebAuthType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 2, 1, 1, 3),
    _FsWebPortalWebAuthType_Type()
)
fsWebPortalWebAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebPortalWebAuthType.setStatus("current")


class _FsWebPortalUseGlbConfigFlag_Type(Integer32):
    """Custom type fsWebPortalUseGlbConfigFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsWebPortalUseGlbConfigFlag_Type.__name__ = "Integer32"
_FsWebPortalUseGlbConfigFlag_Object = MibTableColumn
fsWebPortalUseGlbConfigFlag = _FsWebPortalUseGlbConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 2, 1, 1, 4),
    _FsWebPortalUseGlbConfigFlag_Type()
)
fsWebPortalUseGlbConfigFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebPortalUseGlbConfigFlag.setStatus("current")


class _FsWebPortalMetholdList_Type(DisplayString):
    """Custom type fsWebPortalMetholdList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsWebPortalMetholdList_Type.__name__ = "DisplayString"
_FsWebPortalMetholdList_Object = MibTableColumn
fsWebPortalMetholdList = _FsWebPortalMetholdList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 2, 1, 1, 5),
    _FsWebPortalMetholdList_Type()
)
fsWebPortalMetholdList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebPortalMetholdList.setStatus("current")


class _FsWebPortalCustomizedPageName_Type(DisplayString):
    """Custom type fsWebPortalCustomizedPageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_FsWebPortalCustomizedPageName_Type.__name__ = "DisplayString"
_FsWebPortalCustomizedPageName_Object = MibTableColumn
fsWebPortalCustomizedPageName = _FsWebPortalCustomizedPageName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 2, 1, 1, 6),
    _FsWebPortalCustomizedPageName_Type()
)
fsWebPortalCustomizedPageName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebPortalCustomizedPageName.setStatus("current")


class _FsWebPortalExtWebPortalURL_Type(DisplayString):
    """Custom type fsWebPortalExtWebPortalURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_FsWebPortalExtWebPortalURL_Type.__name__ = "DisplayString"
_FsWebPortalExtWebPortalURL_Object = MibTableColumn
fsWebPortalExtWebPortalURL = _FsWebPortalExtWebPortalURL_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 2, 1, 1, 7),
    _FsWebPortalExtWebPortalURL_Type()
)
fsWebPortalExtWebPortalURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebPortalExtWebPortalURL.setStatus("current")


class _FsWebPortalCustomizedLogoName_Type(DisplayString):
    """Custom type fsWebPortalCustomizedLogoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_FsWebPortalCustomizedLogoName_Type.__name__ = "DisplayString"
_FsWebPortalCustomizedLogoName_Object = MibTableColumn
fsWebPortalCustomizedLogoName = _FsWebPortalCustomizedLogoName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 2, 1, 1, 8),
    _FsWebPortalCustomizedLogoName_Type()
)
fsWebPortalCustomizedLogoName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebPortalCustomizedLogoName.setStatus("current")


class _FsWebPortalEchoManufacturerLogo_Type(Integer32):
    """Custom type fsWebPortalEchoManufacturerLogo based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsWebPortalEchoManufacturerLogo_Type.__name__ = "Integer32"
_FsWebPortalEchoManufacturerLogo_Object = MibTableColumn
fsWebPortalEchoManufacturerLogo = _FsWebPortalEchoManufacturerLogo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 2, 1, 1, 9),
    _FsWebPortalEchoManufacturerLogo_Type()
)
fsWebPortalEchoManufacturerLogo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebPortalEchoManufacturerLogo.setStatus("current")


class _FsWebPortalWelcomeMsg_Type(OctetString):
    """Custom type fsWebPortalWelcomeMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2047),
    )


_FsWebPortalWelcomeMsg_Type.__name__ = "OctetString"
_FsWebPortalWelcomeMsg_Object = MibTableColumn
fsWebPortalWelcomeMsg = _FsWebPortalWelcomeMsg_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 2, 1, 1, 10),
    _FsWebPortalWelcomeMsg_Type()
)
fsWebPortalWelcomeMsg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebPortalWelcomeMsg.setStatus("current")


class _FsWebPortalWebPageTitle_Type(DisplayString):
    """Custom type fsWebPortalWebPageTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_FsWebPortalWebPageTitle_Type.__name__ = "DisplayString"
_FsWebPortalWebPageTitle_Object = MibTableColumn
fsWebPortalWebPageTitle = _FsWebPortalWebPageTitle_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 2, 1, 1, 11),
    _FsWebPortalWebPageTitle_Type()
)
fsWebPortalWebPageTitle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebPortalWebPageTitle.setStatus("current")
_FsWebPortalEntryStatus_Type = RowStatus
_FsWebPortalEntryStatus_Object = MibTableColumn
fsWebPortalEntryStatus = _FsWebPortalEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 1, 2, 1, 1, 12),
    _FsWebPortalEntryStatus_Type()
)
fsWebPortalEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebPortalEntryStatus.setStatus("current")
_FsWebPortalMIBConformance_ObjectIdentity = ObjectIdentity
fsWebPortalMIBConformance = _FsWebPortalMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 2)
)
_FsWebPortalMIBCompliances_ObjectIdentity = ObjectIdentity
fsWebPortalMIBCompliances = _FsWebPortalMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 2, 1)
)
_FsWebPortalMIBGroups_ObjectIdentity = ObjectIdentity
fsWebPortalMIBGroups = _FsWebPortalMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 2, 2)
)

# Managed Objects groups

fsWebPortalMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 2, 2, 1)
)
fsWebPortalMIBGroup.setObjects(
      *(("FS-WEB-PORTAL-MIB", "fsWebPortalGlbWebAuthType"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalGlbMethodList"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalGlbCustomizedPageName"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalGlbExternalWebPortalURL"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalGlbCustomizedLogoName"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalGlbEchoManufacturerLogo"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalGlbWelcomeMsg"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalGlbWebPageTitle"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalNetMode"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalNetID"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalWebAuthType"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalUseGlbConfigFlag"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalMetholdList"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalCustomizedPageName"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalExtWebPortalURL"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalCustomizedLogoName"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalEchoManufacturerLogo"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalWelcomeMsg"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalWebPageTitle"),
        ("FS-WEB-PORTAL-MIB", "fsWebPortalEntryStatus"))
)
if mibBuilder.loadTexts:
    fsWebPortalMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsWebPortalMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 69, 2, 1, 1)
)
fsWebPortalMIBCompliance.setObjects(
    ("FS-WEB-PORTAL-MIB", "fsWebPortalMIBGroup")
)
if mibBuilder.loadTexts:
    fsWebPortalMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-WEB-PORTAL-MIB",
    **{"fsWebPortalMIB": fsWebPortalMIB,
       "fsWebPortalMIBObjects": fsWebPortalMIBObjects,
       "fsWebPortalGlobalMIBObjects": fsWebPortalGlobalMIBObjects,
       "fsWebPortalGlbWebAuthType": fsWebPortalGlbWebAuthType,
       "fsWebPortalGlbMethodList": fsWebPortalGlbMethodList,
       "fsWebPortalGlbCustomizedPageName": fsWebPortalGlbCustomizedPageName,
       "fsWebPortalGlbExternalWebPortalURL": fsWebPortalGlbExternalWebPortalURL,
       "fsWebPortalGlbCustomizedLogoName": fsWebPortalGlbCustomizedLogoName,
       "fsWebPortalGlbEchoManufacturerLogo": fsWebPortalGlbEchoManufacturerLogo,
       "fsWebPortalGlbWelcomeMsg": fsWebPortalGlbWelcomeMsg,
       "fsWebPortalGlbWebPageTitle": fsWebPortalGlbWebPageTitle,
       "fsWebPortalLocalMIBObjects": fsWebPortalLocalMIBObjects,
       "fsWebPortalAuthTable": fsWebPortalAuthTable,
       "fsWebPortalAuthEntry": fsWebPortalAuthEntry,
       "fsWebPortalNetMode": fsWebPortalNetMode,
       "fsWebPortalNetID": fsWebPortalNetID,
       "fsWebPortalWebAuthType": fsWebPortalWebAuthType,
       "fsWebPortalUseGlbConfigFlag": fsWebPortalUseGlbConfigFlag,
       "fsWebPortalMetholdList": fsWebPortalMetholdList,
       "fsWebPortalCustomizedPageName": fsWebPortalCustomizedPageName,
       "fsWebPortalExtWebPortalURL": fsWebPortalExtWebPortalURL,
       "fsWebPortalCustomizedLogoName": fsWebPortalCustomizedLogoName,
       "fsWebPortalEchoManufacturerLogo": fsWebPortalEchoManufacturerLogo,
       "fsWebPortalWelcomeMsg": fsWebPortalWelcomeMsg,
       "fsWebPortalWebPageTitle": fsWebPortalWebPageTitle,
       "fsWebPortalEntryStatus": fsWebPortalEntryStatus,
       "fsWebPortalMIBConformance": fsWebPortalMIBConformance,
       "fsWebPortalMIBCompliances": fsWebPortalMIBCompliances,
       "fsWebPortalMIBCompliance": fsWebPortalMIBCompliance,
       "fsWebPortalMIBGroups": fsWebPortalMIBGroups,
       "fsWebPortalMIBGroup": fsWebPortalMIBGroup}
)
