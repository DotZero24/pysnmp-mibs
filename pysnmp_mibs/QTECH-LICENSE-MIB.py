# SNMP MIB module (QTECH-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-LICENSE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:21 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

qtechLicenseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57)
)
if mibBuilder.loadTexts:
    qtechLicenseMIB.setRevisions(
        ("2009-09-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechLicenseMIBObjects_ObjectIdentity = ObjectIdentity
qtechLicenseMIBObjects = _QtechLicenseMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 1)
)
_QtechShowLicense_Type = Integer32
_QtechShowLicense_Object = MibScalar
qtechShowLicense = _QtechShowLicense_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 1, 1),
    _QtechShowLicense_Type()
)
qtechShowLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechShowLicense.setStatus("current")
_QtechLicenseTable_Object = MibTable
qtechLicenseTable = _QtechLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 1, 2)
)
if mibBuilder.loadTexts:
    qtechLicenseTable.setStatus("current")
_QtechLicenseEntry_Object = MibTableRow
qtechLicenseEntry = _QtechLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 1, 2, 1)
)
qtechLicenseEntry.setIndexNames(
    (0, "QTECH-LICENSE-MIB", "qtechLicenseIndex"),
)
if mibBuilder.loadTexts:
    qtechLicenseEntry.setStatus("current")
_QtechLicenseIndex_Type = Integer32
_QtechLicenseIndex_Object = MibTableColumn
qtechLicenseIndex = _QtechLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 1, 2, 1, 1),
    _QtechLicenseIndex_Type()
)
qtechLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechLicenseIndex.setStatus("current")
_QtechLicenseString_Type = DisplayString
_QtechLicenseString_Object = MibTableColumn
qtechLicenseString = _QtechLicenseString_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 1, 2, 1, 2),
    _QtechLicenseString_Type()
)
qtechLicenseString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLicenseString.setStatus("current")
_QtechLicenseValue_Type = Integer32
_QtechLicenseValue_Object = MibTableColumn
qtechLicenseValue = _QtechLicenseValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 1, 2, 1, 3),
    _QtechLicenseValue_Type()
)
qtechLicenseValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLicenseValue.setStatus("current")
_QtechLicenseMIBConformance_ObjectIdentity = ObjectIdentity
qtechLicenseMIBConformance = _QtechLicenseMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 2)
)
_QtechLicenseMIBCompliances_ObjectIdentity = ObjectIdentity
qtechLicenseMIBCompliances = _QtechLicenseMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 2, 1)
)
_QtechLicenseMIBGroups_ObjectIdentity = ObjectIdentity
qtechLicenseMIBGroups = _QtechLicenseMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 2, 2)
)

# Managed Objects groups

qtechLicenseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 2, 2, 1)
)
qtechLicenseMIBGroup.setObjects(
      *(("QTECH-LICENSE-MIB", "qtechShowLicense"),
        ("QTECH-LICENSE-MIB", "qtechLicenseString"),
        ("QTECH-LICENSE-MIB", "qtechLicenseValue"))
)
if mibBuilder.loadTexts:
    qtechLicenseMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechLicenseMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 2, 1, 1)
)
qtechLicenseMIBCompliance.setObjects(
    ("QTECH-LICENSE-MIB", "qtechLicenseMIBGroup")
)
if mibBuilder.loadTexts:
    qtechLicenseMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-LICENSE-MIB",
    **{"qtechLicenseMIB": qtechLicenseMIB,
       "qtechLicenseMIBObjects": qtechLicenseMIBObjects,
       "qtechShowLicense": qtechShowLicense,
       "qtechLicenseTable": qtechLicenseTable,
       "qtechLicenseEntry": qtechLicenseEntry,
       "qtechLicenseIndex": qtechLicenseIndex,
       "qtechLicenseString": qtechLicenseString,
       "qtechLicenseValue": qtechLicenseValue,
       "qtechLicenseMIBConformance": qtechLicenseMIBConformance,
       "qtechLicenseMIBCompliances": qtechLicenseMIBCompliances,
       "qtechLicenseMIBCompliance": qtechLicenseMIBCompliance,
       "qtechLicenseMIBGroups": qtechLicenseMIBGroups,
       "qtechLicenseMIBGroup": qtechLicenseMIBGroup}
)
