# SNMP MIB module (ENTERASYS-ACTIVATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-ACTIVATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:30 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

etsysActivationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999)
)
if mibBuilder.loadTexts:
    etsysActivationMIB.setRevisions(
        ("2002-04-18 14:54",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnterasysKeyType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noKey", 1),
          ("unknownKeyType", 2),
          ("productKey", 3),
          ("demoKey", 4))
    )



class EnterasysFeature(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1xAuthentication", 1),
          ("pointToMultipoint", 2))
    )



# MIB Managed Objects in the order of their OIDs

_EtsysActivationObjects_ObjectIdentity = ObjectIdentity
etsysActivationObjects = _EtsysActivationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1)
)
_EtsysActivationBaseBranch_ObjectIdentity = ObjectIdentity
etsysActivationBaseBranch = _EtsysActivationBaseBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1)
)


class _EtsysMaxActivationKeyRow_Type(Integer32):
    """Custom type etsysMaxActivationKeyRow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysMaxActivationKeyRow_Type.__name__ = "Integer32"
_EtsysMaxActivationKeyRow_Object = MibScalar
etsysMaxActivationKeyRow = _EtsysMaxActivationKeyRow_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 1),
    _EtsysMaxActivationKeyRow_Type()
)
etsysMaxActivationKeyRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMaxActivationKeyRow.setStatus("current")
_EtsysActivationKeyTable_Object = MibTable
etsysActivationKeyTable = _EtsysActivationKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2)
)
if mibBuilder.loadTexts:
    etsysActivationKeyTable.setStatus("current")
_EtsysActivationKeyEntry_Object = MibTableRow
etsysActivationKeyEntry = _EtsysActivationKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1)
)
etsysActivationKeyEntry.setIndexNames(
    (0, "ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyRow"),
)
if mibBuilder.loadTexts:
    etsysActivationKeyEntry.setStatus("current")


class _EtsysActivationKeyRow_Type(Integer32):
    """Custom type etsysActivationKeyRow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysActivationKeyRow_Type.__name__ = "Integer32"
_EtsysActivationKeyRow_Object = MibTableColumn
etsysActivationKeyRow = _EtsysActivationKeyRow_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 1),
    _EtsysActivationKeyRow_Type()
)
etsysActivationKeyRow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysActivationKeyRow.setStatus("current")
_EtsysActivationLicenseString_Type = SnmpAdminString
_EtsysActivationLicenseString_Object = MibTableColumn
etsysActivationLicenseString = _EtsysActivationLicenseString_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 2),
    _EtsysActivationLicenseString_Type()
)
etsysActivationLicenseString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysActivationLicenseString.setStatus("current")
_EtsysActivationKeyValue_Type = SnmpAdminString
_EtsysActivationKeyValue_Object = MibTableColumn
etsysActivationKeyValue = _EtsysActivationKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 3),
    _EtsysActivationKeyValue_Type()
)
etsysActivationKeyValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysActivationKeyValue.setStatus("current")
_EtsysActivationKeyType_Type = EnterasysKeyType
_EtsysActivationKeyType_Object = MibTableColumn
etsysActivationKeyType = _EtsysActivationKeyType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 4),
    _EtsysActivationKeyType_Type()
)
etsysActivationKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysActivationKeyType.setStatus("current")
_EtsysActivationKeyStatus_Type = RowStatus
_EtsysActivationKeyStatus_Object = MibTableColumn
etsysActivationKeyStatus = _EtsysActivationKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 5),
    _EtsysActivationKeyStatus_Type()
)
etsysActivationKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysActivationKeyStatus.setStatus("current")
_EtsysActivationKeyFeatureTable_Object = MibTable
etsysActivationKeyFeatureTable = _EtsysActivationKeyFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 3)
)
if mibBuilder.loadTexts:
    etsysActivationKeyFeatureTable.setStatus("current")
_EtsysActivationKeyFeatureEntry_Object = MibTableRow
etsysActivationKeyFeatureEntry = _EtsysActivationKeyFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 3, 1)
)
etsysActivationKeyFeatureEntry.setIndexNames(
    (0, "ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyRow"),
    (0, "ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyFeature"),
)
if mibBuilder.loadTexts:
    etsysActivationKeyFeatureEntry.setStatus("current")
_EtsysActivationKeyFeature_Type = EnterasysFeature
_EtsysActivationKeyFeature_Object = MibTableColumn
etsysActivationKeyFeature = _EtsysActivationKeyFeature_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 3, 1, 1),
    _EtsysActivationKeyFeature_Type()
)
etsysActivationKeyFeature.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysActivationKeyFeature.setStatus("current")
_EtsysActivationKeyRestrictions_Type = SnmpAdminString
_EtsysActivationKeyRestrictions_Object = MibTableColumn
etsysActivationKeyRestrictions = _EtsysActivationKeyRestrictions_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 3, 1, 2),
    _EtsysActivationKeyRestrictions_Type()
)
etsysActivationKeyRestrictions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysActivationKeyRestrictions.setStatus("current")
_EtsysActivationConformance_ObjectIdentity = ObjectIdentity
etsysActivationConformance = _EtsysActivationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2)
)
_EtsysActivationGroups_ObjectIdentity = ObjectIdentity
etsysActivationGroups = _EtsysActivationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2, 1)
)
_EtsysActivationCompliances_ObjectIdentity = ObjectIdentity
etsysActivationCompliances = _EtsysActivationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2, 2)
)

# Managed Objects groups

etsysActivationBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2, 1, 1)
)
etsysActivationBaseGroup.setObjects(
      *(("ENTERASYS-ACTIVATION-MIB", "etsysMaxActivationKeyRow"),
        ("ENTERASYS-ACTIVATION-MIB", "etsysActivationLicenseString"),
        ("ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyValue"),
        ("ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyType"),
        ("ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyStatus"),
        ("ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyRestrictions"))
)
if mibBuilder.loadTexts:
    etsysActivationBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysActivationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2, 2, 1)
)
etsysActivationCompliance.setObjects(
    ("ENTERASYS-ACTIVATION-MIB", "etsysActivationBaseGroup")
)
if mibBuilder.loadTexts:
    etsysActivationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-ACTIVATION-MIB",
    **{"EnterasysKeyType": EnterasysKeyType,
       "EnterasysFeature": EnterasysFeature,
       "etsysActivationMIB": etsysActivationMIB,
       "etsysActivationObjects": etsysActivationObjects,
       "etsysActivationBaseBranch": etsysActivationBaseBranch,
       "etsysMaxActivationKeyRow": etsysMaxActivationKeyRow,
       "etsysActivationKeyTable": etsysActivationKeyTable,
       "etsysActivationKeyEntry": etsysActivationKeyEntry,
       "etsysActivationKeyRow": etsysActivationKeyRow,
       "etsysActivationLicenseString": etsysActivationLicenseString,
       "etsysActivationKeyValue": etsysActivationKeyValue,
       "etsysActivationKeyType": etsysActivationKeyType,
       "etsysActivationKeyStatus": etsysActivationKeyStatus,
       "etsysActivationKeyFeatureTable": etsysActivationKeyFeatureTable,
       "etsysActivationKeyFeatureEntry": etsysActivationKeyFeatureEntry,
       "etsysActivationKeyFeature": etsysActivationKeyFeature,
       "etsysActivationKeyRestrictions": etsysActivationKeyRestrictions,
       "etsysActivationConformance": etsysActivationConformance,
       "etsysActivationGroups": etsysActivationGroups,
       "etsysActivationBaseGroup": etsysActivationBaseGroup,
       "etsysActivationCompliances": etsysActivationCompliances,
       "etsysActivationCompliance": etsysActivationCompliance}
)
