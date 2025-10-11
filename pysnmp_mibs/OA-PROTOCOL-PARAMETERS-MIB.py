# SNMP MIB module (OA-PROTOCOL-PARAMETERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OA-PROTOCOL-PARAMETERS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:36 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

oaProtocolParams = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 42)
)
if mibBuilder.loadTexts:
    oaProtocolParams.setRevisions(
        ("2008-11-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EntryValidator(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 2),
          ("delete", 3),
          ("create", 4),
          ("enable", 5),
          ("disable", 6))
    )



# MIB Managed Objects in the order of their OIDs

_Oaccess_ObjectIdentity = ObjectIdentity
oaccess = _Oaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926)
)
_OaManagement_ObjectIdentity = ObjectIdentity
oaManagement = _OaManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1)
)
_OaSnmpPrtcl_ObjectIdentity = ObjectIdentity
oaSnmpPrtcl = _OaSnmpPrtcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 42, 2)
)
_OaSnmpSecurStrTable_Object = MibTable
oaSnmpSecurStrTable = _OaSnmpSecurStrTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 42, 2, 2)
)
if mibBuilder.loadTexts:
    oaSnmpSecurStrTable.setStatus("current")
_OaSnmpSecurStrEntry_Object = MibTableRow
oaSnmpSecurStrEntry = _OaSnmpSecurStrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 42, 2, 2, 1)
)
oaSnmpSecurStrEntry.setIndexNames(
    (0, "OA-PROTOCOL-PARAMETERS-MIB", "oaSnmpSecurStrName"),
)
if mibBuilder.loadTexts:
    oaSnmpSecurStrEntry.setStatus("current")


class _OaSnmpSecurStrName_Type(DisplayString):
    """Custom type oaSnmpSecurStrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_OaSnmpSecurStrName_Type.__name__ = "DisplayString"
_OaSnmpSecurStrName_Object = MibTableColumn
oaSnmpSecurStrName = _OaSnmpSecurStrName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 42, 2, 2, 1, 1),
    _OaSnmpSecurStrName_Type()
)
oaSnmpSecurStrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaSnmpSecurStrName.setStatus("current")


class _OaSnmpSecurStrAccessPermission_Type(Integer32):
    """Custom type oaSnmpSecurStrAccessPermission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_OaSnmpSecurStrAccessPermission_Type.__name__ = "Integer32"
_OaSnmpSecurStrAccessPermission_Object = MibTableColumn
oaSnmpSecurStrAccessPermission = _OaSnmpSecurStrAccessPermission_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 42, 2, 2, 1, 2),
    _OaSnmpSecurStrAccessPermission_Type()
)
oaSnmpSecurStrAccessPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSnmpSecurStrAccessPermission.setStatus("current")
_OaSnmpSecurStrAdminStatus_Type = EntryValidator
_OaSnmpSecurStrAdminStatus_Object = MibTableColumn
oaSnmpSecurStrAdminStatus = _OaSnmpSecurStrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 42, 2, 2, 1, 11),
    _OaSnmpSecurStrAdminStatus_Type()
)
oaSnmpSecurStrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSnmpSecurStrAdminStatus.setStatus("current")
_OaPrtclConformance_ObjectIdentity = ObjectIdentity
oaPrtclConformance = _OaPrtclConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 42, 101)
)
_OaPrtclMIBCompliances_ObjectIdentity = ObjectIdentity
oaPrtclMIBCompliances = _OaPrtclMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 42, 101, 1)
)
_OaPrtclMIBGroups_ObjectIdentity = ObjectIdentity
oaPrtclMIBGroups = _OaPrtclMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 42, 101, 2)
)

# Managed Objects groups

oaSnmpSecurStrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 42, 101, 2, 1)
)
oaSnmpSecurStrGroup.setObjects(
      *(("OA-PROTOCOL-PARAMETERS-MIB", "oaSnmpSecurStrAccessPermission"),
        ("OA-PROTOCOL-PARAMETERS-MIB", "oaSnmpSecurStrAdminStatus"))
)
if mibBuilder.loadTexts:
    oaSnmpSecurStrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oaPrtclMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 1, 42, 101, 1, 1)
)
oaPrtclMIBCompliance.setObjects(
    ("OA-PROTOCOL-PARAMETERS-MIB", "oaSnmpSecurStrGroup")
)
if mibBuilder.loadTexts:
    oaPrtclMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-PROTOCOL-PARAMETERS-MIB",
    **{"EntryValidator": EntryValidator,
       "oaccess": oaccess,
       "oaManagement": oaManagement,
       "oaProtocolParams": oaProtocolParams,
       "oaSnmpPrtcl": oaSnmpPrtcl,
       "oaSnmpSecurStrTable": oaSnmpSecurStrTable,
       "oaSnmpSecurStrEntry": oaSnmpSecurStrEntry,
       "oaSnmpSecurStrName": oaSnmpSecurStrName,
       "oaSnmpSecurStrAccessPermission": oaSnmpSecurStrAccessPermission,
       "oaSnmpSecurStrAdminStatus": oaSnmpSecurStrAdminStatus,
       "oaPrtclConformance": oaPrtclConformance,
       "oaPrtclMIBCompliances": oaPrtclMIBCompliances,
       "oaPrtclMIBCompliance": oaPrtclMIBCompliance,
       "oaPrtclMIBGroups": oaPrtclMIBGroups,
       "oaSnmpSecurStrGroup": oaSnmpSecurStrGroup}
)
