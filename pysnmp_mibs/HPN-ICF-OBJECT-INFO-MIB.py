# SNMP MIB module (HPN-ICF-OBJECT-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPN-ICF-OBJECT-INFO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:41:26 2025
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfObjectInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55)
)
if mibBuilder.loadTexts:
    hpnicfObjectInfo.setRevisions(
        ("2004-12-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfObjectInformation_ObjectIdentity = ObjectIdentity
hpnicfObjectInformation = _HpnicfObjectInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1)
)
_HpnicfObjectInfoTable_Object = MibTable
hpnicfObjectInfoTable = _HpnicfObjectInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfObjectInfoTable.setStatus("current")
_HpnicfObjectInfoEntry_Object = MibTableRow
hpnicfObjectInfoEntry = _HpnicfObjectInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1)
)
hpnicfObjectInfoEntry.setIndexNames(
    (0, "HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoOID"),
    (0, "HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoType"),
    (0, "HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoTypeExtension"),
)
if mibBuilder.loadTexts:
    hpnicfObjectInfoEntry.setStatus("current")
_HpnicfObjectInfoOID_Type = ObjectIdentifier
_HpnicfObjectInfoOID_Object = MibTableColumn
hpnicfObjectInfoOID = _HpnicfObjectInfoOID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1, 1),
    _HpnicfObjectInfoOID_Type()
)
hpnicfObjectInfoOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfObjectInfoOID.setStatus("current")


class _HpnicfObjectInfoType_Type(Integer32):
    """Custom type hpnicfObjectInfoType based on Integer32"""
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
        *(("reserved", 1),
          ("accessType", 2),
          ("dataType", 3),
          ("dataRange", 4),
          ("dataLength", 5))
    )


_HpnicfObjectInfoType_Type.__name__ = "Integer32"
_HpnicfObjectInfoType_Object = MibTableColumn
hpnicfObjectInfoType = _HpnicfObjectInfoType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1, 2),
    _HpnicfObjectInfoType_Type()
)
hpnicfObjectInfoType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfObjectInfoType.setStatus("current")


class _HpnicfObjectInfoTypeExtension_Type(OctetString):
    """Custom type hpnicfObjectInfoTypeExtension based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_HpnicfObjectInfoTypeExtension_Type.__name__ = "OctetString"
_HpnicfObjectInfoTypeExtension_Object = MibTableColumn
hpnicfObjectInfoTypeExtension = _HpnicfObjectInfoTypeExtension_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1, 3),
    _HpnicfObjectInfoTypeExtension_Type()
)
hpnicfObjectInfoTypeExtension.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfObjectInfoTypeExtension.setStatus("current")
_HpnicfObjectInfoValue_Type = OctetString
_HpnicfObjectInfoValue_Object = MibTableColumn
hpnicfObjectInfoValue = _HpnicfObjectInfoValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1, 4),
    _HpnicfObjectInfoValue_Type()
)
hpnicfObjectInfoValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfObjectInfoValue.setStatus("current")
_HpnicfObjectInfoMIBConformance_ObjectIdentity = ObjectIdentity
hpnicfObjectInfoMIBConformance = _HpnicfObjectInfoMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2)
)
_HpnicfObjectInfoMIBCompliances_ObjectIdentity = ObjectIdentity
hpnicfObjectInfoMIBCompliances = _HpnicfObjectInfoMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2, 1)
)
_HpnicfObjectInfoMIBGroups_ObjectIdentity = ObjectIdentity
hpnicfObjectInfoMIBGroups = _HpnicfObjectInfoMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2, 2)
)

# Managed Objects groups

hpnicfObjectInfoTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2, 2, 1)
)
hpnicfObjectInfoTableGroup.setObjects(
    ("HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoValue")
)
if mibBuilder.loadTexts:
    hpnicfObjectInfoTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpnicfObjectInfoMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2, 1, 1)
)
hpnicfObjectInfoMIBCompliance.setObjects(
    ("HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoTableGroup")
)
if mibBuilder.loadTexts:
    hpnicfObjectInfoMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-OBJECT-INFO-MIB",
    **{"hpnicfObjectInfo": hpnicfObjectInfo,
       "hpnicfObjectInformation": hpnicfObjectInformation,
       "hpnicfObjectInfoTable": hpnicfObjectInfoTable,
       "hpnicfObjectInfoEntry": hpnicfObjectInfoEntry,
       "hpnicfObjectInfoOID": hpnicfObjectInfoOID,
       "hpnicfObjectInfoType": hpnicfObjectInfoType,
       "hpnicfObjectInfoTypeExtension": hpnicfObjectInfoTypeExtension,
       "hpnicfObjectInfoValue": hpnicfObjectInfoValue,
       "hpnicfObjectInfoMIBConformance": hpnicfObjectInfoMIBConformance,
       "hpnicfObjectInfoMIBCompliances": hpnicfObjectInfoMIBCompliances,
       "hpnicfObjectInfoMIBCompliance": hpnicfObjectInfoMIBCompliance,
       "hpnicfObjectInfoMIBGroups": hpnicfObjectInfoMIBGroups,
       "hpnicfObjectInfoTableGroup": hpnicfObjectInfoTableGroup}
)
