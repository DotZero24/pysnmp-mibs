# SNMP MIB module (Juniper-INET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/junose/Juniper-INET-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:06:10 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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
 Opaque,
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
    "Opaque",
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

juniInetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82)
)
if mibBuilder.loadTexts:
    juniInetMIB.setRevisions(
        ("2010-08-03 09:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniInetObjects_ObjectIdentity = ObjectIdentity
juniInetObjects = _JuniInetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 1)
)
_JuniInetRoute_ObjectIdentity = ObjectIdentity
juniInetRoute = _JuniInetRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 1, 1)
)
_JuniInetStaticRouteTable_Object = MibTable
juniInetStaticRouteTable = _JuniInetStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniInetStaticRouteTable.setStatus("current")
_JuniInetStaticRouteEntry_Object = MibTableRow
juniInetStaticRouteEntry = _JuniInetStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 1, 1, 1, 1)
)
juniInetStaticRouteEntry.setIndexNames(
    (0, "Juniper-INET-MIB", "juniInetRouteDestType"),
    (0, "Juniper-INET-MIB", "juniInetRouteDest"),
    (0, "Juniper-INET-MIB", "juniInetRoutePfxLen"),
    (0, "Juniper-INET-MIB", "juniInetRoutePolicy"),
    (0, "Juniper-INET-MIB", "juniInetRouteNextHopType"),
    (0, "Juniper-INET-MIB", "juniInetRouteNextHop"),
    (0, "Juniper-INET-MIB", "juniInetRouteStaticPref"),
)
if mibBuilder.loadTexts:
    juniInetStaticRouteEntry.setStatus("current")
_JuniInetRouteDestType_Type = InetAddressType
_JuniInetRouteDestType_Object = MibTableColumn
juniInetRouteDestType = _JuniInetRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 1, 1, 1, 1, 1),
    _JuniInetRouteDestType_Type()
)
juniInetRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniInetRouteDestType.setStatus("current")
_JuniInetRouteDest_Type = InetAddress
_JuniInetRouteDest_Object = MibTableColumn
juniInetRouteDest = _JuniInetRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 1, 1, 1, 1, 2),
    _JuniInetRouteDest_Type()
)
juniInetRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniInetRouteDest.setStatus("current")
_JuniInetRoutePfxLen_Type = InetAddressPrefixLength
_JuniInetRoutePfxLen_Object = MibTableColumn
juniInetRoutePfxLen = _JuniInetRoutePfxLen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 1, 1, 1, 1, 3),
    _JuniInetRoutePfxLen_Type()
)
juniInetRoutePfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniInetRoutePfxLen.setStatus("current")
_JuniInetRoutePolicy_Type = ObjectIdentifier
_JuniInetRoutePolicy_Object = MibTableColumn
juniInetRoutePolicy = _JuniInetRoutePolicy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 1, 1, 1, 1, 4),
    _JuniInetRoutePolicy_Type()
)
juniInetRoutePolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniInetRoutePolicy.setStatus("current")
_JuniInetRouteNextHopType_Type = InetAddressType
_JuniInetRouteNextHopType_Object = MibTableColumn
juniInetRouteNextHopType = _JuniInetRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 1, 1, 1, 1, 5),
    _JuniInetRouteNextHopType_Type()
)
juniInetRouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniInetRouteNextHopType.setStatus("current")
_JuniInetRouteNextHop_Type = InetAddress
_JuniInetRouteNextHop_Object = MibTableColumn
juniInetRouteNextHop = _JuniInetRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 1, 1, 1, 1, 6),
    _JuniInetRouteNextHop_Type()
)
juniInetRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniInetRouteNextHop.setStatus("current")


class _JuniInetRouteStaticPref_Type(Integer32):
    """Custom type juniInetRouteStaticPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniInetRouteStaticPref_Type.__name__ = "Integer32"
_JuniInetRouteStaticPref_Object = MibTableColumn
juniInetRouteStaticPref = _JuniInetRouteStaticPref_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 1, 1, 1, 1, 7),
    _JuniInetRouteStaticPref_Type()
)
juniInetRouteStaticPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniInetRouteStaticPref.setStatus("current")
_JuniInetRouteStaticRowStatus_Type = RowStatus
_JuniInetRouteStaticRowStatus_Object = MibTableColumn
juniInetRouteStaticRowStatus = _JuniInetRouteStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 1, 1, 1, 1, 8),
    _JuniInetRouteStaticRowStatus_Type()
)
juniInetRouteStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniInetRouteStaticRowStatus.setStatus("current")
_JuniInetRouteIfIndex_Type = InterfaceIndexOrZero
_JuniInetRouteIfIndex_Object = MibTableColumn
juniInetRouteIfIndex = _JuniInetRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 1, 1, 1, 1, 9),
    _JuniInetRouteIfIndex_Type()
)
juniInetRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniInetRouteIfIndex.setStatus("current")


class _JuniInetRouteStaticStatus_Type(Integer32):
    """Custom type juniInetRouteStaticStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1),
          ("incomplete", 2))
    )


_JuniInetRouteStaticStatus_Type.__name__ = "Integer32"
_JuniInetRouteStaticStatus_Object = MibTableColumn
juniInetRouteStaticStatus = _JuniInetRouteStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 1, 1, 1, 1, 10),
    _JuniInetRouteStaticStatus_Type()
)
juniInetRouteStaticStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniInetRouteStaticStatus.setStatus("current")


class _JuniInetRouteStaticNextHopAS_Type(Integer32):
    """Custom type juniInetRouteStaticNextHopAS based on Integer32"""
    defaultValue = 0


_JuniInetRouteStaticNextHopAS_Type.__name__ = "Integer32"
_JuniInetRouteStaticNextHopAS_Object = MibTableColumn
juniInetRouteStaticNextHopAS = _JuniInetRouteStaticNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 1, 1, 1, 1, 11),
    _JuniInetRouteStaticNextHopAS_Type()
)
juniInetRouteStaticNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniInetRouteStaticNextHopAS.setStatus("current")


class _JuniInetRouteStaticMetric_Type(Integer32):
    """Custom type juniInetRouteStaticMetric based on Integer32"""
    defaultValue = -1


_JuniInetRouteStaticMetric_Type.__name__ = "Integer32"
_JuniInetRouteStaticMetric_Object = MibTableColumn
juniInetRouteStaticMetric = _JuniInetRouteStaticMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 1, 1, 1, 1, 12),
    _JuniInetRouteStaticMetric_Type()
)
juniInetRouteStaticMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniInetRouteStaticMetric.setStatus("current")


class _JuniInetRouteStaticTag_Type(Unsigned32):
    """Custom type juniInetRouteStaticTag based on Unsigned32"""
    defaultValue = 0


_JuniInetRouteStaticTag_Type.__name__ = "Unsigned32"
_JuniInetRouteStaticTag_Object = MibTableColumn
juniInetRouteStaticTag = _JuniInetRouteStaticTag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 1, 1, 1, 1, 13),
    _JuniInetRouteStaticTag_Type()
)
juniInetRouteStaticTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniInetRouteStaticTag.setStatus("current")


class _JuniInetRouteStaticNullIntf_Type(Integer32):
    """Custom type juniInetRouteStaticNullIntf based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("reject", 2))
    )


_JuniInetRouteStaticNullIntf_Type.__name__ = "Integer32"
_JuniInetRouteStaticNullIntf_Object = MibTableColumn
juniInetRouteStaticNullIntf = _JuniInetRouteStaticNullIntf_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 1, 1, 1, 1, 14),
    _JuniInetRouteStaticNullIntf_Type()
)
juniInetRouteStaticNullIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniInetRouteStaticNullIntf.setStatus("current")
_JuniInetConformance_ObjectIdentity = ObjectIdentity
juniInetConformance = _JuniInetConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 2)
)
_JuniInetCompliances_ObjectIdentity = ObjectIdentity
juniInetCompliances = _JuniInetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 2, 1)
)
_JuniInetGroups_ObjectIdentity = ObjectIdentity
juniInetGroups = _JuniInetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 2, 2)
)

# Managed Objects groups

juniInetRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 2, 2, 1)
)
juniInetRouteGroup.setObjects(
      *(("Juniper-INET-MIB", "juniInetRouteStaticRowStatus"),
        ("Juniper-INET-MIB", "juniInetRouteIfIndex"),
        ("Juniper-INET-MIB", "juniInetRouteStaticStatus"),
        ("Juniper-INET-MIB", "juniInetRouteStaticNextHopAS"),
        ("Juniper-INET-MIB", "juniInetRouteStaticMetric"),
        ("Juniper-INET-MIB", "juniInetRouteStaticTag"),
        ("Juniper-INET-MIB", "juniInetRouteStaticNullIntf"))
)
if mibBuilder.loadTexts:
    juniInetRouteGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniInetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82, 2, 1, 1)
)
juniInetCompliance.setObjects(
    ("Juniper-INET-MIB", "juniInetRouteGroup")
)
if mibBuilder.loadTexts:
    juniInetCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-INET-MIB",
    **{"juniInetMIB": juniInetMIB,
       "juniInetObjects": juniInetObjects,
       "juniInetRoute": juniInetRoute,
       "juniInetStaticRouteTable": juniInetStaticRouteTable,
       "juniInetStaticRouteEntry": juniInetStaticRouteEntry,
       "juniInetRouteDestType": juniInetRouteDestType,
       "juniInetRouteDest": juniInetRouteDest,
       "juniInetRoutePfxLen": juniInetRoutePfxLen,
       "juniInetRoutePolicy": juniInetRoutePolicy,
       "juniInetRouteNextHopType": juniInetRouteNextHopType,
       "juniInetRouteNextHop": juniInetRouteNextHop,
       "juniInetRouteStaticPref": juniInetRouteStaticPref,
       "juniInetRouteStaticRowStatus": juniInetRouteStaticRowStatus,
       "juniInetRouteIfIndex": juniInetRouteIfIndex,
       "juniInetRouteStaticStatus": juniInetRouteStaticStatus,
       "juniInetRouteStaticNextHopAS": juniInetRouteStaticNextHopAS,
       "juniInetRouteStaticMetric": juniInetRouteStaticMetric,
       "juniInetRouteStaticTag": juniInetRouteStaticTag,
       "juniInetRouteStaticNullIntf": juniInetRouteStaticNullIntf,
       "juniInetConformance": juniInetConformance,
       "juniInetCompliances": juniInetCompliances,
       "juniInetCompliance": juniInetCompliance,
       "juniInetGroups": juniInetGroups,
       "juniInetRouteGroup": juniInetRouteGroup}
)
