# SNMP MIB module (QTECH-WEB-PORTAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-WEB-PORTAL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:48 2025
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

qtechWebPortalMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69)
)
if mibBuilder.loadTexts:
    qtechWebPortalMIB.setRevisions(
        ("2010-02-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechWebPortalMIBObjects_ObjectIdentity = ObjectIdentity
qtechWebPortalMIBObjects = _QtechWebPortalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1)
)
_QtechWebPortalGlobalMIBObjects_ObjectIdentity = ObjectIdentity
qtechWebPortalGlobalMIBObjects = _QtechWebPortalGlobalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 1)
)


class _QtechWebPortalGlbWebAuthType_Type(Integer32):
    """Custom type qtechWebPortalGlbWebAuthType based on Integer32"""
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


_QtechWebPortalGlbWebAuthType_Type.__name__ = "Integer32"
_QtechWebPortalGlbWebAuthType_Object = MibScalar
qtechWebPortalGlbWebAuthType = _QtechWebPortalGlbWebAuthType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 1, 1),
    _QtechWebPortalGlbWebAuthType_Type()
)
qtechWebPortalGlbWebAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWebPortalGlbWebAuthType.setStatus("current")


class _QtechWebPortalGlbMethodList_Type(DisplayString):
    """Custom type qtechWebPortalGlbMethodList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_QtechWebPortalGlbMethodList_Type.__name__ = "DisplayString"
_QtechWebPortalGlbMethodList_Object = MibScalar
qtechWebPortalGlbMethodList = _QtechWebPortalGlbMethodList_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 1, 2),
    _QtechWebPortalGlbMethodList_Type()
)
qtechWebPortalGlbMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWebPortalGlbMethodList.setStatus("current")


class _QtechWebPortalGlbCustomizedPageName_Type(DisplayString):
    """Custom type qtechWebPortalGlbCustomizedPageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_QtechWebPortalGlbCustomizedPageName_Type.__name__ = "DisplayString"
_QtechWebPortalGlbCustomizedPageName_Object = MibScalar
qtechWebPortalGlbCustomizedPageName = _QtechWebPortalGlbCustomizedPageName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 1, 3),
    _QtechWebPortalGlbCustomizedPageName_Type()
)
qtechWebPortalGlbCustomizedPageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWebPortalGlbCustomizedPageName.setStatus("current")


class _QtechWebPortalGlbExternalWebPortalURL_Type(DisplayString):
    """Custom type qtechWebPortalGlbExternalWebPortalURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_QtechWebPortalGlbExternalWebPortalURL_Type.__name__ = "DisplayString"
_QtechWebPortalGlbExternalWebPortalURL_Object = MibScalar
qtechWebPortalGlbExternalWebPortalURL = _QtechWebPortalGlbExternalWebPortalURL_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 1, 4),
    _QtechWebPortalGlbExternalWebPortalURL_Type()
)
qtechWebPortalGlbExternalWebPortalURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWebPortalGlbExternalWebPortalURL.setStatus("current")


class _QtechWebPortalGlbCustomizedLogoName_Type(DisplayString):
    """Custom type qtechWebPortalGlbCustomizedLogoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_QtechWebPortalGlbCustomizedLogoName_Type.__name__ = "DisplayString"
_QtechWebPortalGlbCustomizedLogoName_Object = MibScalar
qtechWebPortalGlbCustomizedLogoName = _QtechWebPortalGlbCustomizedLogoName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 1, 5),
    _QtechWebPortalGlbCustomizedLogoName_Type()
)
qtechWebPortalGlbCustomizedLogoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWebPortalGlbCustomizedLogoName.setStatus("current")


class _QtechWebPortalGlbEchoManufacturerLogo_Type(Integer32):
    """Custom type qtechWebPortalGlbEchoManufacturerLogo based on Integer32"""
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


_QtechWebPortalGlbEchoManufacturerLogo_Type.__name__ = "Integer32"
_QtechWebPortalGlbEchoManufacturerLogo_Object = MibScalar
qtechWebPortalGlbEchoManufacturerLogo = _QtechWebPortalGlbEchoManufacturerLogo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 1, 6),
    _QtechWebPortalGlbEchoManufacturerLogo_Type()
)
qtechWebPortalGlbEchoManufacturerLogo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWebPortalGlbEchoManufacturerLogo.setStatus("current")


class _QtechWebPortalGlbWelcomeMsg_Type(OctetString):
    """Custom type qtechWebPortalGlbWelcomeMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2047),
    )


_QtechWebPortalGlbWelcomeMsg_Type.__name__ = "OctetString"
_QtechWebPortalGlbWelcomeMsg_Object = MibScalar
qtechWebPortalGlbWelcomeMsg = _QtechWebPortalGlbWelcomeMsg_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 1, 7),
    _QtechWebPortalGlbWelcomeMsg_Type()
)
qtechWebPortalGlbWelcomeMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWebPortalGlbWelcomeMsg.setStatus("current")


class _QtechWebPortalGlbWebPageTitle_Type(DisplayString):
    """Custom type qtechWebPortalGlbWebPageTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_QtechWebPortalGlbWebPageTitle_Type.__name__ = "DisplayString"
_QtechWebPortalGlbWebPageTitle_Object = MibScalar
qtechWebPortalGlbWebPageTitle = _QtechWebPortalGlbWebPageTitle_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 1, 8),
    _QtechWebPortalGlbWebPageTitle_Type()
)
qtechWebPortalGlbWebPageTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWebPortalGlbWebPageTitle.setStatus("current")
_QtechWebPortalLocalMIBObjects_ObjectIdentity = ObjectIdentity
qtechWebPortalLocalMIBObjects = _QtechWebPortalLocalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 2)
)
_QtechWebPortalAuthTable_Object = MibTable
qtechWebPortalAuthTable = _QtechWebPortalAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 2, 1)
)
if mibBuilder.loadTexts:
    qtechWebPortalAuthTable.setStatus("current")
_QtechWebPortalAuthEntry_Object = MibTableRow
qtechWebPortalAuthEntry = _QtechWebPortalAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 2, 1, 1)
)
qtechWebPortalAuthEntry.setIndexNames(
    (0, "QTECH-WEB-PORTAL-MIB", "qtechWebPortalNetMode"),
    (0, "QTECH-WEB-PORTAL-MIB", "qtechWebPortalNetID"),
)
if mibBuilder.loadTexts:
    qtechWebPortalAuthEntry.setStatus("current")


class _QtechWebPortalNetMode_Type(Integer32):
    """Custom type qtechWebPortalNetMode based on Integer32"""
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


_QtechWebPortalNetMode_Type.__name__ = "Integer32"
_QtechWebPortalNetMode_Object = MibTableColumn
qtechWebPortalNetMode = _QtechWebPortalNetMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 2, 1, 1, 1),
    _QtechWebPortalNetMode_Type()
)
qtechWebPortalNetMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWebPortalNetMode.setStatus("current")


class _QtechWebPortalNetID_Type(Integer32):
    """Custom type qtechWebPortalNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_QtechWebPortalNetID_Type.__name__ = "Integer32"
_QtechWebPortalNetID_Object = MibTableColumn
qtechWebPortalNetID = _QtechWebPortalNetID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 2, 1, 1, 2),
    _QtechWebPortalNetID_Type()
)
qtechWebPortalNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWebPortalNetID.setStatus("current")


class _QtechWebPortalWebAuthType_Type(Integer32):
    """Custom type qtechWebPortalWebAuthType based on Integer32"""
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


_QtechWebPortalWebAuthType_Type.__name__ = "Integer32"
_QtechWebPortalWebAuthType_Object = MibTableColumn
qtechWebPortalWebAuthType = _QtechWebPortalWebAuthType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 2, 1, 1, 3),
    _QtechWebPortalWebAuthType_Type()
)
qtechWebPortalWebAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebPortalWebAuthType.setStatus("current")


class _QtechWebPortalUseGlbConfigFlag_Type(Integer32):
    """Custom type qtechWebPortalUseGlbConfigFlag based on Integer32"""
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


_QtechWebPortalUseGlbConfigFlag_Type.__name__ = "Integer32"
_QtechWebPortalUseGlbConfigFlag_Object = MibTableColumn
qtechWebPortalUseGlbConfigFlag = _QtechWebPortalUseGlbConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 2, 1, 1, 4),
    _QtechWebPortalUseGlbConfigFlag_Type()
)
qtechWebPortalUseGlbConfigFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebPortalUseGlbConfigFlag.setStatus("current")


class _QtechWebPortalMetholdList_Type(DisplayString):
    """Custom type qtechWebPortalMetholdList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechWebPortalMetholdList_Type.__name__ = "DisplayString"
_QtechWebPortalMetholdList_Object = MibTableColumn
qtechWebPortalMetholdList = _QtechWebPortalMetholdList_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 2, 1, 1, 5),
    _QtechWebPortalMetholdList_Type()
)
qtechWebPortalMetholdList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebPortalMetholdList.setStatus("current")


class _QtechWebPortalCustomizedPageName_Type(DisplayString):
    """Custom type qtechWebPortalCustomizedPageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_QtechWebPortalCustomizedPageName_Type.__name__ = "DisplayString"
_QtechWebPortalCustomizedPageName_Object = MibTableColumn
qtechWebPortalCustomizedPageName = _QtechWebPortalCustomizedPageName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 2, 1, 1, 6),
    _QtechWebPortalCustomizedPageName_Type()
)
qtechWebPortalCustomizedPageName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebPortalCustomizedPageName.setStatus("current")


class _QtechWebPortalExtWebPortalURL_Type(DisplayString):
    """Custom type qtechWebPortalExtWebPortalURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_QtechWebPortalExtWebPortalURL_Type.__name__ = "DisplayString"
_QtechWebPortalExtWebPortalURL_Object = MibTableColumn
qtechWebPortalExtWebPortalURL = _QtechWebPortalExtWebPortalURL_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 2, 1, 1, 7),
    _QtechWebPortalExtWebPortalURL_Type()
)
qtechWebPortalExtWebPortalURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebPortalExtWebPortalURL.setStatus("current")


class _QtechWebPortalCustomizedLogoName_Type(DisplayString):
    """Custom type qtechWebPortalCustomizedLogoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_QtechWebPortalCustomizedLogoName_Type.__name__ = "DisplayString"
_QtechWebPortalCustomizedLogoName_Object = MibTableColumn
qtechWebPortalCustomizedLogoName = _QtechWebPortalCustomizedLogoName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 2, 1, 1, 8),
    _QtechWebPortalCustomizedLogoName_Type()
)
qtechWebPortalCustomizedLogoName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebPortalCustomizedLogoName.setStatus("current")


class _QtechWebPortalEchoManufacturerLogo_Type(Integer32):
    """Custom type qtechWebPortalEchoManufacturerLogo based on Integer32"""
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


_QtechWebPortalEchoManufacturerLogo_Type.__name__ = "Integer32"
_QtechWebPortalEchoManufacturerLogo_Object = MibTableColumn
qtechWebPortalEchoManufacturerLogo = _QtechWebPortalEchoManufacturerLogo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 2, 1, 1, 9),
    _QtechWebPortalEchoManufacturerLogo_Type()
)
qtechWebPortalEchoManufacturerLogo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebPortalEchoManufacturerLogo.setStatus("current")


class _QtechWebPortalWelcomeMsg_Type(OctetString):
    """Custom type qtechWebPortalWelcomeMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2047),
    )


_QtechWebPortalWelcomeMsg_Type.__name__ = "OctetString"
_QtechWebPortalWelcomeMsg_Object = MibTableColumn
qtechWebPortalWelcomeMsg = _QtechWebPortalWelcomeMsg_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 2, 1, 1, 10),
    _QtechWebPortalWelcomeMsg_Type()
)
qtechWebPortalWelcomeMsg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebPortalWelcomeMsg.setStatus("current")


class _QtechWebPortalWebPageTitle_Type(DisplayString):
    """Custom type qtechWebPortalWebPageTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_QtechWebPortalWebPageTitle_Type.__name__ = "DisplayString"
_QtechWebPortalWebPageTitle_Object = MibTableColumn
qtechWebPortalWebPageTitle = _QtechWebPortalWebPageTitle_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 2, 1, 1, 11),
    _QtechWebPortalWebPageTitle_Type()
)
qtechWebPortalWebPageTitle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebPortalWebPageTitle.setStatus("current")
_QtechWebPortalEntryStatus_Type = RowStatus
_QtechWebPortalEntryStatus_Object = MibTableColumn
qtechWebPortalEntryStatus = _QtechWebPortalEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 1, 2, 1, 1, 12),
    _QtechWebPortalEntryStatus_Type()
)
qtechWebPortalEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebPortalEntryStatus.setStatus("current")
_QtechWebPortalMIBConformance_ObjectIdentity = ObjectIdentity
qtechWebPortalMIBConformance = _QtechWebPortalMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 2)
)
_QtechWebPortalMIBCompliances_ObjectIdentity = ObjectIdentity
qtechWebPortalMIBCompliances = _QtechWebPortalMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 2, 1)
)
_QtechWebPortalMIBGroups_ObjectIdentity = ObjectIdentity
qtechWebPortalMIBGroups = _QtechWebPortalMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 2, 2)
)

# Managed Objects groups

qtechWebPortalMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 2, 2, 1)
)
qtechWebPortalMIBGroup.setObjects(
      *(("QTECH-WEB-PORTAL-MIB", "qtechWebPortalGlbWebAuthType"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalGlbMethodList"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalGlbCustomizedPageName"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalGlbExternalWebPortalURL"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalGlbCustomizedLogoName"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalGlbEchoManufacturerLogo"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalGlbWelcomeMsg"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalGlbWebPageTitle"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalNetMode"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalNetID"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalWebAuthType"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalUseGlbConfigFlag"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalMetholdList"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalCustomizedPageName"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalExtWebPortalURL"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalCustomizedLogoName"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalEchoManufacturerLogo"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalWelcomeMsg"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalWebPageTitle"),
        ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalEntryStatus"))
)
if mibBuilder.loadTexts:
    qtechWebPortalMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechWebPortalMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 69, 2, 1, 1)
)
qtechWebPortalMIBCompliance.setObjects(
    ("QTECH-WEB-PORTAL-MIB", "qtechWebPortalMIBGroup")
)
if mibBuilder.loadTexts:
    qtechWebPortalMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-WEB-PORTAL-MIB",
    **{"qtechWebPortalMIB": qtechWebPortalMIB,
       "qtechWebPortalMIBObjects": qtechWebPortalMIBObjects,
       "qtechWebPortalGlobalMIBObjects": qtechWebPortalGlobalMIBObjects,
       "qtechWebPortalGlbWebAuthType": qtechWebPortalGlbWebAuthType,
       "qtechWebPortalGlbMethodList": qtechWebPortalGlbMethodList,
       "qtechWebPortalGlbCustomizedPageName": qtechWebPortalGlbCustomizedPageName,
       "qtechWebPortalGlbExternalWebPortalURL": qtechWebPortalGlbExternalWebPortalURL,
       "qtechWebPortalGlbCustomizedLogoName": qtechWebPortalGlbCustomizedLogoName,
       "qtechWebPortalGlbEchoManufacturerLogo": qtechWebPortalGlbEchoManufacturerLogo,
       "qtechWebPortalGlbWelcomeMsg": qtechWebPortalGlbWelcomeMsg,
       "qtechWebPortalGlbWebPageTitle": qtechWebPortalGlbWebPageTitle,
       "qtechWebPortalLocalMIBObjects": qtechWebPortalLocalMIBObjects,
       "qtechWebPortalAuthTable": qtechWebPortalAuthTable,
       "qtechWebPortalAuthEntry": qtechWebPortalAuthEntry,
       "qtechWebPortalNetMode": qtechWebPortalNetMode,
       "qtechWebPortalNetID": qtechWebPortalNetID,
       "qtechWebPortalWebAuthType": qtechWebPortalWebAuthType,
       "qtechWebPortalUseGlbConfigFlag": qtechWebPortalUseGlbConfigFlag,
       "qtechWebPortalMetholdList": qtechWebPortalMetholdList,
       "qtechWebPortalCustomizedPageName": qtechWebPortalCustomizedPageName,
       "qtechWebPortalExtWebPortalURL": qtechWebPortalExtWebPortalURL,
       "qtechWebPortalCustomizedLogoName": qtechWebPortalCustomizedLogoName,
       "qtechWebPortalEchoManufacturerLogo": qtechWebPortalEchoManufacturerLogo,
       "qtechWebPortalWelcomeMsg": qtechWebPortalWelcomeMsg,
       "qtechWebPortalWebPageTitle": qtechWebPortalWebPageTitle,
       "qtechWebPortalEntryStatus": qtechWebPortalEntryStatus,
       "qtechWebPortalMIBConformance": qtechWebPortalMIBConformance,
       "qtechWebPortalMIBCompliances": qtechWebPortalMIBCompliances,
       "qtechWebPortalMIBCompliance": qtechWebPortalMIBCompliance,
       "qtechWebPortalMIBGroups": qtechWebPortalMIBGroups,
       "qtechWebPortalMIBGroup": qtechWebPortalMIBGroup}
)
