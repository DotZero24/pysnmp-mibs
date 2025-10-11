# SNMP MIB module (MX-PRODUCT-NAMING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-PRODUCT-NAMING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:59 2025
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

(mediatrixProducts,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixProducts")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

productNamingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000)
)
if mibBuilder.loadTexts:
    productNamingMIB.setRevisions(
        ("2011-06-28 00:00",
         "2009-10-01 00:00",
         "2008-08-12 00:00",
         "2008-06-17 00:00",
         "2007-12-11 00:00",
         "2007-03-21 00:00",
         "2007-01-08 00:00",
         "2005-06-23 00:00",
         "2005-04-15 00:00",
         "2004-02-02 00:00",
         "2003-02-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ProductNamingMIBObjects_ObjectIdentity = ObjectIdentity
productNamingMIBObjects = _ProductNamingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1)
)


class _ProductNamingPlatformName_Type(OctetString):
    """Custom type productNamingPlatformName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ProductNamingPlatformName_Type.__name__ = "OctetString"
_ProductNamingPlatformName_Object = MibScalar
productNamingPlatformName = _ProductNamingPlatformName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 15),
    _ProductNamingPlatformName_Type()
)
productNamingPlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNamingPlatformName.setStatus("current")
_ProductNamingPlatforms_ObjectIdentity = ObjectIdentity
productNamingPlatforms = _ProductNamingPlatforms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20)
)


class _ProductNaming1102_Type(OctetString):
    """Custom type productNaming1102 based on OctetString"""
    defaultValue = OctetString("Mediatrix 1102")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNaming1102_Type.__name__ = "OctetString"
_ProductNaming1102_Object = MibScalar
productNaming1102 = _ProductNaming1102_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 5),
    _ProductNaming1102_Type()
)
productNaming1102.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNaming1102.setStatus("current")


class _ProductNaming1104_Type(OctetString):
    """Custom type productNaming1104 based on OctetString"""
    defaultValue = OctetString("Mediatrix 1104")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNaming1104_Type.__name__ = "OctetString"
_ProductNaming1104_Object = MibScalar
productNaming1104 = _ProductNaming1104_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 10),
    _ProductNaming1104_Type()
)
productNaming1104.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNaming1104.setStatus("current")


class _ProductNaming1124_Type(OctetString):
    """Custom type productNaming1124 based on OctetString"""
    defaultValue = OctetString("Mediatrix 1124")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNaming1124_Type.__name__ = "OctetString"
_ProductNaming1124_Object = MibScalar
productNaming1124 = _ProductNaming1124_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 15),
    _ProductNaming1124_Type()
)
productNaming1124.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNaming1124.setStatus("current")


class _ProductNaming1204_Type(OctetString):
    """Custom type productNaming1204 based on OctetString"""
    defaultValue = OctetString("Mediatrix 1204")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNaming1204_Type.__name__ = "OctetString"
_ProductNaming1204_Object = MibScalar
productNaming1204 = _ProductNaming1204_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 20),
    _ProductNaming1204_Type()
)
productNaming1204.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNaming1204.setStatus("current")


class _ProductNaming2102_Type(OctetString):
    """Custom type productNaming2102 based on OctetString"""
    defaultValue = OctetString("Mediatrix 2102")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNaming2102_Type.__name__ = "OctetString"
_ProductNaming2102_Object = MibScalar
productNaming2102 = _ProductNaming2102_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 25),
    _ProductNaming2102_Type()
)
productNaming2102.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNaming2102.setStatus("current")


class _ProductNamingLiaison312_Type(OctetString):
    """Custom type productNamingLiaison312 based on OctetString"""
    defaultValue = OctetString("Mediatrix Liaison 312")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNamingLiaison312_Type.__name__ = "OctetString"
_ProductNamingLiaison312_Object = MibScalar
productNamingLiaison312 = _ProductNamingLiaison312_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 30),
    _ProductNamingLiaison312_Type()
)
productNamingLiaison312.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNamingLiaison312.setStatus("current")


class _ProductNamingLiaison322_Type(OctetString):
    """Custom type productNamingLiaison322 based on OctetString"""
    defaultValue = OctetString("Mediatrix Liaison 322")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNamingLiaison322_Type.__name__ = "OctetString"
_ProductNamingLiaison322_Object = MibScalar
productNamingLiaison322 = _ProductNamingLiaison322_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 35),
    _ProductNamingLiaison322_Type()
)
productNamingLiaison322.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNamingLiaison322.setStatus("current")


class _ProductNamingLiaison512_Type(OctetString):
    """Custom type productNamingLiaison512 based on OctetString"""
    defaultValue = OctetString("Mediatrix Liaison 512")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNamingLiaison512_Type.__name__ = "OctetString"
_ProductNamingLiaison512_Object = MibScalar
productNamingLiaison512 = _ProductNamingLiaison512_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 75),
    _ProductNamingLiaison512_Type()
)
productNamingLiaison512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNamingLiaison512.setStatus("current")


class _ProductNamingLiaison522_Type(OctetString):
    """Custom type productNamingLiaison522 based on OctetString"""
    defaultValue = OctetString("Mediatrix Liaison 522")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNamingLiaison522_Type.__name__ = "OctetString"
_ProductNamingLiaison522_Object = MibScalar
productNamingLiaison522 = _ProductNamingLiaison522_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 80),
    _ProductNamingLiaison522_Type()
)
productNamingLiaison522.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNamingLiaison522.setStatus("current")


class _ProductNaming0102_Type(OctetString):
    """Custom type productNaming0102 based on OctetString"""
    defaultValue = OctetString("Mediatrix 0102")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNaming0102_Type.__name__ = "OctetString"
_ProductNaming0102_Object = MibScalar
productNaming0102 = _ProductNaming0102_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 83),
    _ProductNaming0102_Type()
)
productNaming0102.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNaming0102.setStatus("current")


class _ProductNaming4102_Type(OctetString):
    """Custom type productNaming4102 based on OctetString"""
    defaultValue = OctetString("Mediatrix 4102")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNaming4102_Type.__name__ = "OctetString"
_ProductNaming4102_Object = MibScalar
productNaming4102 = _ProductNaming4102_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 84),
    _ProductNaming4102_Type()
)
productNaming4102.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNaming4102.setStatus("current")


class _ProductNaming4104_Type(OctetString):
    """Custom type productNaming4104 based on OctetString"""
    defaultValue = OctetString("Mediatrix 4104")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNaming4104_Type.__name__ = "OctetString"
_ProductNaming4104_Object = MibScalar
productNaming4104 = _ProductNaming4104_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 85),
    _ProductNaming4104_Type()
)
productNaming4104.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNaming4104.setStatus("current")


class _ProductNaming4104Plus_Type(OctetString):
    """Custom type productNaming4104Plus based on OctetString"""
    defaultValue = OctetString("Mediatrix 4104plus")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNaming4104Plus_Type.__name__ = "OctetString"
_ProductNaming4104Plus_Object = MibScalar
productNaming4104Plus = _ProductNaming4104Plus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 88),
    _ProductNaming4104Plus_Type()
)
productNaming4104Plus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNaming4104Plus.setStatus("current")


class _ProductNaming4108_Type(OctetString):
    """Custom type productNaming4108 based on OctetString"""
    defaultValue = OctetString("Mediatrix 4108")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNaming4108_Type.__name__ = "OctetString"
_ProductNaming4108_Object = MibScalar
productNaming4108 = _ProductNaming4108_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 90),
    _ProductNaming4108_Type()
)
productNaming4108.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNaming4108.setStatus("current")


class _ProductNaming4116_Type(OctetString):
    """Custom type productNaming4116 based on OctetString"""
    defaultValue = OctetString("Mediatrix 4116")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNaming4116_Type.__name__ = "OctetString"
_ProductNaming4116_Object = MibScalar
productNaming4116 = _ProductNaming4116_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 95),
    _ProductNaming4116_Type()
)
productNaming4116.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNaming4116.setStatus("current")


class _ProductNaming4124_Type(OctetString):
    """Custom type productNaming4124 based on OctetString"""
    defaultValue = OctetString("Mediatrix 4124")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNaming4124_Type.__name__ = "OctetString"
_ProductNaming4124_Object = MibScalar
productNaming4124 = _ProductNaming4124_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 100),
    _ProductNaming4124_Type()
)
productNaming4124.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNaming4124.setStatus("current")


class _ProductNamingLP16_Type(OctetString):
    """Custom type productNamingLP16 based on OctetString"""
    defaultValue = OctetString("Mediatrix LP16")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNamingLP16_Type.__name__ = "OctetString"
_ProductNamingLP16_Object = MibScalar
productNamingLP16 = _ProductNamingLP16_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 105),
    _ProductNamingLP16_Type()
)
productNamingLP16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNamingLP16.setStatus("current")


class _ProductNamingLP24_Type(OctetString):
    """Custom type productNamingLP24 based on OctetString"""
    defaultValue = OctetString("Mediatrix LP24")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNamingLP24_Type.__name__ = "OctetString"
_ProductNamingLP24_Object = MibScalar
productNamingLP24 = _ProductNamingLP24_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 110),
    _ProductNamingLP24_Type()
)
productNamingLP24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNamingLP24.setStatus("current")


class _ProductNamingLE46VM_Type(OctetString):
    """Custom type productNamingLE46VM based on OctetString"""
    defaultValue = OctetString("Ciena LE46 VM")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProductNamingLE46VM_Type.__name__ = "OctetString"
_ProductNamingLE46VM_Object = MibScalar
productNamingLE46VM = _ProductNamingLE46VM_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 1, 20, 120),
    _ProductNamingLE46VM_Type()
)
productNamingLE46VM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productNamingLE46VM.setStatus("current")
_ProductNamingConformance_ObjectIdentity = ObjectIdentity
productNamingConformance = _ProductNamingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 5)
)
_ProductNamingCompliances_ObjectIdentity = ObjectIdentity
productNamingCompliances = _ProductNamingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 5, 1)
)
_ProductNamingGroups_ObjectIdentity = ObjectIdentity
productNamingGroups = _ProductNamingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 5, 5)
)

# Managed Objects groups

productNamingPlatformsVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 5, 5, 10)
)
productNamingPlatformsVer1.setObjects(
      *(("MX-PRODUCT-NAMING-MIB", "productNamingPlatformName"),
        ("MX-PRODUCT-NAMING-MIB", "productNaming1102"),
        ("MX-PRODUCT-NAMING-MIB", "productNaming1104"),
        ("MX-PRODUCT-NAMING-MIB", "productNaming1124"),
        ("MX-PRODUCT-NAMING-MIB", "productNaming1204"),
        ("MX-PRODUCT-NAMING-MIB", "productNaming2102"),
        ("MX-PRODUCT-NAMING-MIB", "productNamingLiaison512"),
        ("MX-PRODUCT-NAMING-MIB", "productNamingLiaison522"),
        ("MX-PRODUCT-NAMING-MIB", "productNaming0102"),
        ("MX-PRODUCT-NAMING-MIB", "productNaming4102"),
        ("MX-PRODUCT-NAMING-MIB", "productNaming4104"),
        ("MX-PRODUCT-NAMING-MIB", "productNaming4104Plus"),
        ("MX-PRODUCT-NAMING-MIB", "productNaming4108"),
        ("MX-PRODUCT-NAMING-MIB", "productNaming4116"),
        ("MX-PRODUCT-NAMING-MIB", "productNaming4124"),
        ("MX-PRODUCT-NAMING-MIB", "productNamingLP16"),
        ("MX-PRODUCT-NAMING-MIB", "productNamingLP24"),
        ("MX-PRODUCT-NAMING-MIB", "productNamingLE46VM"))
)
if mibBuilder.loadTexts:
    productNamingPlatformsVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

productNamingComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 1, 1000, 5, 1, 1)
)
productNamingComplVer1.setObjects(
    ("MX-PRODUCT-NAMING-MIB", "productNamingPlatformsVer1")
)
if mibBuilder.loadTexts:
    productNamingComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-PRODUCT-NAMING-MIB",
    **{"productNamingMIB": productNamingMIB,
       "productNamingMIBObjects": productNamingMIBObjects,
       "productNamingPlatformName": productNamingPlatformName,
       "productNamingPlatforms": productNamingPlatforms,
       "productNaming1102": productNaming1102,
       "productNaming1104": productNaming1104,
       "productNaming1124": productNaming1124,
       "productNaming1204": productNaming1204,
       "productNaming2102": productNaming2102,
       "productNamingLiaison312": productNamingLiaison312,
       "productNamingLiaison322": productNamingLiaison322,
       "productNamingLiaison512": productNamingLiaison512,
       "productNamingLiaison522": productNamingLiaison522,
       "productNaming0102": productNaming0102,
       "productNaming4102": productNaming4102,
       "productNaming4104": productNaming4104,
       "productNaming4104Plus": productNaming4104Plus,
       "productNaming4108": productNaming4108,
       "productNaming4116": productNaming4116,
       "productNaming4124": productNaming4124,
       "productNamingLP16": productNamingLP16,
       "productNamingLP24": productNamingLP24,
       "productNamingLE46VM": productNamingLE46VM,
       "productNamingConformance": productNamingConformance,
       "productNamingCompliances": productNamingCompliances,
       "productNamingComplVer1": productNamingComplVer1,
       "productNamingGroups": productNamingGroups,
       "productNamingPlatformsVer1": productNamingPlatformsVer1}
)
