# SNMP MIB module (G6-WEB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-WEB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:07 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

management = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3)
)
if mibBuilder.loadTexts:
    management.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Web_ObjectIdentity = ObjectIdentity
web = _Web_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63)
)


class _WebProtocol_Type(Integer32):
    """Custom type webProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("httpUnsecure", 1),
          ("httpsSecure", 2))
    )


_WebProtocol_Type.__name__ = "Integer32"
_WebProtocol_Object = MibScalar
webProtocol = _WebProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 1),
    _WebProtocol_Type()
)
webProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webProtocol.setStatus("current")


class _WebWebTimeout_Type(Integer32):
    """Custom type webWebTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WebWebTimeout_Type.__name__ = "Integer32"
_WebWebTimeout_Object = MibScalar
webWebTimeout = _WebWebTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 2),
    _WebWebTimeout_Type()
)
webWebTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webWebTimeout.setStatus("current")


class _WebHttpPortWeb_Type(Integer32):
    """Custom type webHttpPortWeb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WebHttpPortWeb_Type.__name__ = "Integer32"
_WebHttpPortWeb_Object = MibScalar
webHttpPortWeb = _WebHttpPortWeb_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 3),
    _WebHttpPortWeb_Type()
)
webHttpPortWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webHttpPortWeb.setStatus("current")


class _WebHttpsPortWeb_Type(Integer32):
    """Custom type webHttpsPortWeb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WebHttpsPortWeb_Type.__name__ = "Integer32"
_WebHttpsPortWeb_Object = MibScalar
webHttpsPortWeb = _WebHttpsPortWeb_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 4),
    _WebHttpsPortWeb_Type()
)
webHttpsPortWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webHttpsPortWeb.setStatus("current")


class _WebCertificateSource_Type(Integer32):
    """Custom type webCertificateSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("intern", 0),
          ("custom", 1))
    )


_WebCertificateSource_Type.__name__ = "Integer32"
_WebCertificateSource_Object = MibScalar
webCertificateSource = _WebCertificateSource_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 5),
    _WebCertificateSource_Type()
)
webCertificateSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webCertificateSource.setStatus("current")
_WebLoginMessage_Type = DisplayString
_WebLoginMessage_Object = MibScalar
webLoginMessage = _WebLoginMessage_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 6),
    _WebLoginMessage_Type()
)
webLoginMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webLoginMessage.setStatus("current")
_GuiPageTable_Object = MibTable
guiPageTable = _GuiPageTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 7)
)
if mibBuilder.loadTexts:
    guiPageTable.setStatus("current")
_GuiPageEntry_Object = MibTableRow
guiPageEntry = _GuiPageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 7, 1)
)
guiPageEntry.setIndexNames(
    (0, "G6-WEB-MIB", "guiPageIndex"),
)
if mibBuilder.loadTexts:
    guiPageEntry.setStatus("current")


class _GuiPageIndex_Type(Integer32):
    """Custom type guiPageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_GuiPageIndex_Type.__name__ = "Integer32"
_GuiPageIndex_Object = MibTableColumn
guiPageIndex = _GuiPageIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 7, 1, 1),
    _GuiPageIndex_Type()
)
guiPageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    guiPageIndex.setStatus("current")
_GuiPageName_Type = DisplayString
_GuiPageName_Object = MibTableColumn
guiPageName = _GuiPageName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 7, 1, 2),
    _GuiPageName_Type()
)
guiPageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiPageName.setStatus("current")


class _GuiPageGuiMode_Type(Integer32):
    """Custom type guiPageGuiMode based on Integer32"""
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
        *(("disabled", 0),
          ("displayOnly", 1),
          ("normal", 2),
          ("remoteOnly", 3))
    )


_GuiPageGuiMode_Type.__name__ = "Integer32"
_GuiPageGuiMode_Object = MibTableColumn
guiPageGuiMode = _GuiPageGuiMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 7, 1, 3),
    _GuiPageGuiMode_Type()
)
guiPageGuiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiPageGuiMode.setStatus("current")


class _GuiPageColorScheme_Type(Integer32):
    """Custom type guiPageColorScheme based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("gray", 0),
          ("blue", 1),
          ("red", 2),
          ("lime", 3),
          ("yellow", 4),
          ("pink", 5),
          ("cyan", 6),
          ("green", 7),
          ("orange", 8),
          ("purple", 9),
          ("teal", 10))
    )


_GuiPageColorScheme_Type.__name__ = "Integer32"
_GuiPageColorScheme_Object = MibTableColumn
guiPageColorScheme = _GuiPageColorScheme_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 7, 1, 4),
    _GuiPageColorScheme_Type()
)
guiPageColorScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiPageColorScheme.setStatus("current")
_GuiPageLimitedToUsers_Type = DisplayString
_GuiPageLimitedToUsers_Object = MibTableColumn
guiPageLimitedToUsers = _GuiPageLimitedToUsers_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 7, 1, 5),
    _GuiPageLimitedToUsers_Type()
)
guiPageLimitedToUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiPageLimitedToUsers.setStatus("current")
_GuiPageOptions_Type = DisplayString
_GuiPageOptions_Object = MibTableColumn
guiPageOptions = _GuiPageOptions_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 7, 1, 6),
    _GuiPageOptions_Type()
)
guiPageOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiPageOptions.setStatus("current")
_GuiElementTable_Object = MibTable
guiElementTable = _GuiElementTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8)
)
if mibBuilder.loadTexts:
    guiElementTable.setStatus("current")
_GuiElementEntry_Object = MibTableRow
guiElementEntry = _GuiElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1)
)
guiElementEntry.setIndexNames(
    (0, "G6-WEB-MIB", "guiElementIndex"),
)
if mibBuilder.loadTexts:
    guiElementEntry.setStatus("current")


class _GuiElementIndex_Type(Integer32):
    """Custom type guiElementIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GuiElementIndex_Type.__name__ = "Integer32"
_GuiElementIndex_Object = MibTableColumn
guiElementIndex = _GuiElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 1),
    _GuiElementIndex_Type()
)
guiElementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    guiElementIndex.setStatus("current")
_GuiElementName_Type = DisplayString
_GuiElementName_Object = MibTableColumn
guiElementName = _GuiElementName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 2),
    _GuiElementName_Type()
)
guiElementName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementName.setStatus("current")


class _GuiElementType_Type(Integer32):
    """Custom type guiElementType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              11,
              12,
              13,
              14,
              15,
              30,
              31,
              32,
              33,
              34,
              50,
              51,
              52,
              53,
              54,
              55)
        )
    )
    namedValues = NamedValues(
        *(("label", 10),
          ("image", 11),
          ("hyperLink", 12),
          ("space", 13),
          ("line", 14),
          ("frame", 15),
          ("button", 30),
          ("selectBox", 31),
          ("slider", 32),
          ("radioButton", 33),
          ("toggle", 34),
          ("textBox", 50),
          ("barGraph", 51),
          ("gauge", 52),
          ("symbol", 53),
          ("diagram", 54),
          ("input", 55))
    )


_GuiElementType_Type.__name__ = "Integer32"
_GuiElementType_Object = MibTableColumn
guiElementType = _GuiElementType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 3),
    _GuiElementType_Type()
)
guiElementType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementType.setStatus("current")
_GuiElementPage_Type = DisplayString
_GuiElementPage_Object = MibTableColumn
guiElementPage = _GuiElementPage_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 4),
    _GuiElementPage_Type()
)
guiElementPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementPage.setStatus("current")


class _GuiElementVisibility_Type(Integer32):
    """Custom type guiElementVisibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("hidden", 1),
          ("disabled", 2))
    )


_GuiElementVisibility_Type.__name__ = "Integer32"
_GuiElementVisibility_Object = MibTableColumn
guiElementVisibility = _GuiElementVisibility_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 5),
    _GuiElementVisibility_Type()
)
guiElementVisibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementVisibility.setStatus("current")


class _GuiElementAutoSave_Type(Integer32):
    """Custom type guiElementAutoSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GuiElementAutoSave_Type.__name__ = "Integer32"
_GuiElementAutoSave_Object = MibTableColumn
guiElementAutoSave = _GuiElementAutoSave_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 6),
    _GuiElementAutoSave_Type()
)
guiElementAutoSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementAutoSave.setStatus("current")


class _GuiElementRemoteAccessible_Type(Integer32):
    """Custom type guiElementRemoteAccessible based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GuiElementRemoteAccessible_Type.__name__ = "Integer32"
_GuiElementRemoteAccessible_Object = MibTableColumn
guiElementRemoteAccessible = _GuiElementRemoteAccessible_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 7),
    _GuiElementRemoteAccessible_Type()
)
guiElementRemoteAccessible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementRemoteAccessible.setStatus("current")
_GuiElementSensorAttribute_Type = DisplayString
_GuiElementSensorAttribute_Object = MibTableColumn
guiElementSensorAttribute = _GuiElementSensorAttribute_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 8),
    _GuiElementSensorAttribute_Type()
)
guiElementSensorAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementSensorAttribute.setStatus("current")
_GuiElementScriptName_Type = DisplayString
_GuiElementScriptName_Object = MibTableColumn
guiElementScriptName = _GuiElementScriptName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 9),
    _GuiElementScriptName_Type()
)
guiElementScriptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementScriptName.setStatus("current")
_GuiElementWatchedElement_Type = DisplayString
_GuiElementWatchedElement_Object = MibTableColumn
guiElementWatchedElement = _GuiElementWatchedElement_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 10),
    _GuiElementWatchedElement_Type()
)
guiElementWatchedElement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementWatchedElement.setStatus("current")
_GuiElementOrder_Type = Unsigned32
_GuiElementOrder_Object = MibTableColumn
guiElementOrder = _GuiElementOrder_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 11),
    _GuiElementOrder_Type()
)
guiElementOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementOrder.setStatus("current")
_GuiElementHeight_Type = DisplayString
_GuiElementHeight_Object = MibTableColumn
guiElementHeight = _GuiElementHeight_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 12),
    _GuiElementHeight_Type()
)
guiElementHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementHeight.setStatus("current")
_GuiElementWidth_Type = DisplayString
_GuiElementWidth_Object = MibTableColumn
guiElementWidth = _GuiElementWidth_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 13),
    _GuiElementWidth_Type()
)
guiElementWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementWidth.setStatus("current")
_GuiElementTopMargin_Type = DisplayString
_GuiElementTopMargin_Object = MibTableColumn
guiElementTopMargin = _GuiElementTopMargin_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 14),
    _GuiElementTopMargin_Type()
)
guiElementTopMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementTopMargin.setStatus("current")
_GuiElementLeftMargin_Type = DisplayString
_GuiElementLeftMargin_Object = MibTableColumn
guiElementLeftMargin = _GuiElementLeftMargin_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 15),
    _GuiElementLeftMargin_Type()
)
guiElementLeftMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementLeftMargin.setStatus("current")
_GuiElementHeader_Type = DisplayString
_GuiElementHeader_Object = MibTableColumn
guiElementHeader = _GuiElementHeader_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 16),
    _GuiElementHeader_Type()
)
guiElementHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementHeader.setStatus("current")
_GuiElementText_Type = DisplayString
_GuiElementText_Object = MibTableColumn
guiElementText = _GuiElementText_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 17),
    _GuiElementText_Type()
)
guiElementText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementText.setStatus("current")
_GuiElementValue_Type = DisplayString
_GuiElementValue_Object = MibTableColumn
guiElementValue = _GuiElementValue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 18),
    _GuiElementValue_Type()
)
guiElementValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementValue.setStatus("current")
_GuiElementStartValue_Type = DisplayString
_GuiElementStartValue_Object = MibTableColumn
guiElementStartValue = _GuiElementStartValue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 19),
    _GuiElementStartValue_Type()
)
guiElementStartValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementStartValue.setStatus("current")
_GuiElementImage_Type = DisplayString
_GuiElementImage_Object = MibTableColumn
guiElementImage = _GuiElementImage_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 20),
    _GuiElementImage_Type()
)
guiElementImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementImage.setStatus("current")
_GuiElementOptions_Type = DisplayString
_GuiElementOptions_Object = MibTableColumn
guiElementOptions = _GuiElementOptions_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 63, 8, 1, 21),
    _GuiElementOptions_Type()
)
guiElementOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guiElementOptions.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-WEB-MIB",
    **{"management": management,
       "web": web,
       "webProtocol": webProtocol,
       "webWebTimeout": webWebTimeout,
       "webHttpPortWeb": webHttpPortWeb,
       "webHttpsPortWeb": webHttpsPortWeb,
       "webCertificateSource": webCertificateSource,
       "webLoginMessage": webLoginMessage,
       "guiPageTable": guiPageTable,
       "guiPageEntry": guiPageEntry,
       "guiPageIndex": guiPageIndex,
       "guiPageName": guiPageName,
       "guiPageGuiMode": guiPageGuiMode,
       "guiPageColorScheme": guiPageColorScheme,
       "guiPageLimitedToUsers": guiPageLimitedToUsers,
       "guiPageOptions": guiPageOptions,
       "guiElementTable": guiElementTable,
       "guiElementEntry": guiElementEntry,
       "guiElementIndex": guiElementIndex,
       "guiElementName": guiElementName,
       "guiElementType": guiElementType,
       "guiElementPage": guiElementPage,
       "guiElementVisibility": guiElementVisibility,
       "guiElementAutoSave": guiElementAutoSave,
       "guiElementRemoteAccessible": guiElementRemoteAccessible,
       "guiElementSensorAttribute": guiElementSensorAttribute,
       "guiElementScriptName": guiElementScriptName,
       "guiElementWatchedElement": guiElementWatchedElement,
       "guiElementOrder": guiElementOrder,
       "guiElementHeight": guiElementHeight,
       "guiElementWidth": guiElementWidth,
       "guiElementTopMargin": guiElementTopMargin,
       "guiElementLeftMargin": guiElementLeftMargin,
       "guiElementHeader": guiElementHeader,
       "guiElementText": guiElementText,
       "guiElementValue": guiElementValue,
       "guiElementStartValue": guiElementStartValue,
       "guiElementImage": guiElementImage,
       "guiElementOptions": guiElementOptions}
)
