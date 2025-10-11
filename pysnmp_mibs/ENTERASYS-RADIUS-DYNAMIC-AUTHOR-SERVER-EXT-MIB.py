# SNMP MIB module (ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:22 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysRadiusDynAuthorServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80)
)
if mibBuilder.loadTexts:
    etsysRadiusDynAuthorServerMIB.setRevisions(
        ("2016-05-18 14:06",
         "2011-12-19 13:24")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysRadiusDynAuthorServerMIBObjects_ObjectIdentity = ObjectIdentity
etsysRadiusDynAuthorServerMIBObjects = _EtsysRadiusDynAuthorServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1)
)


class _EtsysRadiusDynAuthorServerEnable_Type(Integer32):
    """Custom type etsysRadiusDynAuthorServerEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EtsysRadiusDynAuthorServerEnable_Type.__name__ = "Integer32"
_EtsysRadiusDynAuthorServerEnable_Object = MibScalar
etsysRadiusDynAuthorServerEnable = _EtsysRadiusDynAuthorServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 1),
    _EtsysRadiusDynAuthorServerEnable_Type()
)
etsysRadiusDynAuthorServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusDynAuthorServerEnable.setStatus("current")
_EtsysRadiusDynAuthorServerClientTable_Object = MibTable
etsysRadiusDynAuthorServerClientTable = _EtsysRadiusDynAuthorServerClientTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2)
)
if mibBuilder.loadTexts:
    etsysRadiusDynAuthorServerClientTable.setStatus("current")
_EtsysRadiusDynAuthorServerClientEntry_Object = MibTableRow
etsysRadiusDynAuthorServerClientEntry = _EtsysRadiusDynAuthorServerClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1)
)
etsysRadiusDynAuthorServerClientEntry.setIndexNames(
    (0, "ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientIndex"),
)
if mibBuilder.loadTexts:
    etsysRadiusDynAuthorServerClientEntry.setStatus("current")


class _EtsysRadiusDynAuthorServerClientIndex_Type(Integer32):
    """Custom type etsysRadiusDynAuthorServerClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysRadiusDynAuthorServerClientIndex_Type.__name__ = "Integer32"
_EtsysRadiusDynAuthorServerClientIndex_Object = MibTableColumn
etsysRadiusDynAuthorServerClientIndex = _EtsysRadiusDynAuthorServerClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1, 1),
    _EtsysRadiusDynAuthorServerClientIndex_Type()
)
etsysRadiusDynAuthorServerClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysRadiusDynAuthorServerClientIndex.setStatus("current")


class _EtsysRadiusDynAuthorServerClientAddressType_Type(InetAddressType):
    """Custom type etsysRadiusDynAuthorServerClientAddressType based on InetAddressType"""
    defaultValue = 1


_EtsysRadiusDynAuthorServerClientAddressType_Type.__name__ = "InetAddressType"
_EtsysRadiusDynAuthorServerClientAddressType_Object = MibTableColumn
etsysRadiusDynAuthorServerClientAddressType = _EtsysRadiusDynAuthorServerClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1, 2),
    _EtsysRadiusDynAuthorServerClientAddressType_Type()
)
etsysRadiusDynAuthorServerClientAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusDynAuthorServerClientAddressType.setStatus("current")


class _EtsysRadiusDynAuthorServerClientAddress_Type(InetAddress):
    """Custom type etsysRadiusDynAuthorServerClientAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EtsysRadiusDynAuthorServerClientAddress_Type.__name__ = "InetAddress"
_EtsysRadiusDynAuthorServerClientAddress_Object = MibTableColumn
etsysRadiusDynAuthorServerClientAddress = _EtsysRadiusDynAuthorServerClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1, 3),
    _EtsysRadiusDynAuthorServerClientAddress_Type()
)
etsysRadiusDynAuthorServerClientAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusDynAuthorServerClientAddress.setStatus("current")


class _EtsysRadiusDynAuthorServerClientSecret_Type(OctetString):
    """Custom type etsysRadiusDynAuthorServerClientSecret based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysRadiusDynAuthorServerClientSecret_Type.__name__ = "OctetString"
_EtsysRadiusDynAuthorServerClientSecret_Object = MibTableColumn
etsysRadiusDynAuthorServerClientSecret = _EtsysRadiusDynAuthorServerClientSecret_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1, 4),
    _EtsysRadiusDynAuthorServerClientSecret_Type()
)
etsysRadiusDynAuthorServerClientSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusDynAuthorServerClientSecret.setStatus("current")
_EtsysRadiusDynAuthorServerClientSecretEntered_Type = TruthValue
_EtsysRadiusDynAuthorServerClientSecretEntered_Object = MibTableColumn
etsysRadiusDynAuthorServerClientSecretEntered = _EtsysRadiusDynAuthorServerClientSecretEntered_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1, 5),
    _EtsysRadiusDynAuthorServerClientSecretEntered_Type()
)
etsysRadiusDynAuthorServerClientSecretEntered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusDynAuthorServerClientSecretEntered.setStatus("current")
_EtsysRadiusDynAuthorServerClientStatus_Type = RowStatus
_EtsysRadiusDynAuthorServerClientStatus_Object = MibTableColumn
etsysRadiusDynAuthorServerClientStatus = _EtsysRadiusDynAuthorServerClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1, 6),
    _EtsysRadiusDynAuthorServerClientStatus_Type()
)
etsysRadiusDynAuthorServerClientStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusDynAuthorServerClientStatus.setStatus("current")


class _EtsysRadiusDynAuthorClientServerClientAddressType_Type(InetAddressType):
    """Custom type etsysRadiusDynAuthorClientServerClientAddressType based on InetAddressType"""
    defaultValue = 1


_EtsysRadiusDynAuthorClientServerClientAddressType_Type.__name__ = "InetAddressType"
_EtsysRadiusDynAuthorClientServerClientAddressType_Object = MibTableColumn
etsysRadiusDynAuthorClientServerClientAddressType = _EtsysRadiusDynAuthorClientServerClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1, 7),
    _EtsysRadiusDynAuthorClientServerClientAddressType_Type()
)
etsysRadiusDynAuthorClientServerClientAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusDynAuthorClientServerClientAddressType.setStatus("current")


class _EtsysRadiusDynAuthorClientServerClientAddress_Type(InetAddress):
    """Custom type etsysRadiusDynAuthorClientServerClientAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EtsysRadiusDynAuthorClientServerClientAddress_Type.__name__ = "InetAddress"
_EtsysRadiusDynAuthorClientServerClientAddress_Object = MibTableColumn
etsysRadiusDynAuthorClientServerClientAddress = _EtsysRadiusDynAuthorClientServerClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1, 8),
    _EtsysRadiusDynAuthorClientServerClientAddress_Type()
)
etsysRadiusDynAuthorClientServerClientAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusDynAuthorClientServerClientAddress.setStatus("current")


class _EtsysRadiusDynAuthorClientServerClientVirtualRouterName_Type(OctetString):
    """Custom type etsysRadiusDynAuthorClientServerClientVirtualRouterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EtsysRadiusDynAuthorClientServerClientVirtualRouterName_Type.__name__ = "OctetString"
_EtsysRadiusDynAuthorClientServerClientVirtualRouterName_Object = MibTableColumn
etsysRadiusDynAuthorClientServerClientVirtualRouterName = _EtsysRadiusDynAuthorClientServerClientVirtualRouterName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1, 9),
    _EtsysRadiusDynAuthorClientServerClientVirtualRouterName_Type()
)
etsysRadiusDynAuthorClientServerClientVirtualRouterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusDynAuthorClientServerClientVirtualRouterName.setStatus("current")
_EtsysRadiusDynAuthorServerMIBConformance_ObjectIdentity = ObjectIdentity
etsysRadiusDynAuthorServerMIBConformance = _EtsysRadiusDynAuthorServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 2)
)
_EtsysRadiusDynAuthorServerMIBCompliances_ObjectIdentity = ObjectIdentity
etsysRadiusDynAuthorServerMIBCompliances = _EtsysRadiusDynAuthorServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 2, 1)
)
_EtsysRadiusDynAuthorServerMIBGroups_ObjectIdentity = ObjectIdentity
etsysRadiusDynAuthorServerMIBGroups = _EtsysRadiusDynAuthorServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 2, 2)
)

# Managed Objects groups

etsysRadiusDynAuthorServerMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 2, 2, 1)
)
etsysRadiusDynAuthorServerMIBGroup.setObjects(
      *(("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerEnable"),
        ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientAddressType"),
        ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientAddress"),
        ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientSecret"),
        ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientSecretEntered"),
        ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientStatus"))
)
if mibBuilder.loadTexts:
    etsysRadiusDynAuthorServerMIBGroup.setStatus("deprecated")

etsysRadiusDynAuthorServerMIBGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 2, 2, 2)
)
etsysRadiusDynAuthorServerMIBGroup2.setObjects(
      *(("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerEnable"),
        ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientAddressType"),
        ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientAddress"),
        ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientSecret"),
        ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientSecretEntered"),
        ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientStatus"),
        ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorClientServerClientAddressType"),
        ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorClientServerClientAddress"),
        ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorClientServerClientVirtualRouterName"))
)
if mibBuilder.loadTexts:
    etsysRadiusDynAuthorServerMIBGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysRadiusDynAuthorServerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 2, 1, 1)
)
etsysRadiusDynAuthorServerMIBCompliance.setObjects(
    ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerMIBGroup")
)
if mibBuilder.loadTexts:
    etsysRadiusDynAuthorServerMIBCompliance.setStatus(
        "deprecated"
    )

etsysRadiusDynAuthorServerMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 2, 1, 2)
)
etsysRadiusDynAuthorServerMIBCompliance2.setObjects(
    ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerMIBGroup2")
)
if mibBuilder.loadTexts:
    etsysRadiusDynAuthorServerMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB",
    **{"etsysRadiusDynAuthorServerMIB": etsysRadiusDynAuthorServerMIB,
       "etsysRadiusDynAuthorServerMIBObjects": etsysRadiusDynAuthorServerMIBObjects,
       "etsysRadiusDynAuthorServerEnable": etsysRadiusDynAuthorServerEnable,
       "etsysRadiusDynAuthorServerClientTable": etsysRadiusDynAuthorServerClientTable,
       "etsysRadiusDynAuthorServerClientEntry": etsysRadiusDynAuthorServerClientEntry,
       "etsysRadiusDynAuthorServerClientIndex": etsysRadiusDynAuthorServerClientIndex,
       "etsysRadiusDynAuthorServerClientAddressType": etsysRadiusDynAuthorServerClientAddressType,
       "etsysRadiusDynAuthorServerClientAddress": etsysRadiusDynAuthorServerClientAddress,
       "etsysRadiusDynAuthorServerClientSecret": etsysRadiusDynAuthorServerClientSecret,
       "etsysRadiusDynAuthorServerClientSecretEntered": etsysRadiusDynAuthorServerClientSecretEntered,
       "etsysRadiusDynAuthorServerClientStatus": etsysRadiusDynAuthorServerClientStatus,
       "etsysRadiusDynAuthorClientServerClientAddressType": etsysRadiusDynAuthorClientServerClientAddressType,
       "etsysRadiusDynAuthorClientServerClientAddress": etsysRadiusDynAuthorClientServerClientAddress,
       "etsysRadiusDynAuthorClientServerClientVirtualRouterName": etsysRadiusDynAuthorClientServerClientVirtualRouterName,
       "etsysRadiusDynAuthorServerMIBConformance": etsysRadiusDynAuthorServerMIBConformance,
       "etsysRadiusDynAuthorServerMIBCompliances": etsysRadiusDynAuthorServerMIBCompliances,
       "etsysRadiusDynAuthorServerMIBCompliance": etsysRadiusDynAuthorServerMIBCompliance,
       "etsysRadiusDynAuthorServerMIBCompliance2": etsysRadiusDynAuthorServerMIBCompliance2,
       "etsysRadiusDynAuthorServerMIBGroups": etsysRadiusDynAuthorServerMIBGroups,
       "etsysRadiusDynAuthorServerMIBGroup": etsysRadiusDynAuthorServerMIBGroup,
       "etsysRadiusDynAuthorServerMIBGroup2": etsysRadiusDynAuthorServerMIBGroup2}
)
