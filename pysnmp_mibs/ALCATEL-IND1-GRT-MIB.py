# SNMP MIB module (ALCATEL-IND1-GRT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel/ALCATEL-IND1-GRT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:08:52 2025
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

(routingIND1GlobalRouteTableMIB,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1GlobalRouteTableMIB")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1GRTMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1GRTMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaGrtRouteDistinguisher(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1GRTMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1GRTMIBConformance = _AlcatelIND1GRTMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 1)
)
_AlcatelIND1GRTMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1GRTMIBCompliances = _AlcatelIND1GRTMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 1, 1)
)
_AlcatelIND1GRTMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1GRTMIBGroups = _AlcatelIND1GRTMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 1, 2)
)
_AlcatelIND1GRTMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1GRTMIBObjects = _AlcatelIND1GRTMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2)
)
_AlaGrtConfig_ObjectIdentity = ObjectIdentity
alaGrtConfig = _AlaGrtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1)
)
_AlaGrtRouteTable_Object = MibTable
alaGrtRouteTable = _AlaGrtRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaGrtRouteTable.setStatus("current")
_AlaGrtRouteEntry_Object = MibTableRow
alaGrtRouteEntry = _AlaGrtRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1)
)
alaGrtRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-GRT-MIB", "alaGrtRouteDistinguisher"),
    (0, "ALCATEL-IND1-GRT-MIB", "alaGrtRouteDest"),
    (0, "ALCATEL-IND1-GRT-MIB", "alaGrtRouteMaskLen"),
    (0, "ALCATEL-IND1-GRT-MIB", "alaGrtRouteNextHop"),
)
if mibBuilder.loadTexts:
    alaGrtRouteEntry.setStatus("current")
_AlaGrtRouteDistinguisher_Type = AlaGrtRouteDistinguisher
_AlaGrtRouteDistinguisher_Object = MibTableColumn
alaGrtRouteDistinguisher = _AlaGrtRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1, 1),
    _AlaGrtRouteDistinguisher_Type()
)
alaGrtRouteDistinguisher.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrtRouteDistinguisher.setStatus("current")


class _AlaGrtRouteDest_Type(InetAddress):
    """Custom type alaGrtRouteDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaGrtRouteDest_Type.__name__ = "InetAddress"
_AlaGrtRouteDest_Object = MibTableColumn
alaGrtRouteDest = _AlaGrtRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1, 2),
    _AlaGrtRouteDest_Type()
)
alaGrtRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrtRouteDest.setStatus("current")
_AlaGrtRouteDestType_Type = InetAddressType
_AlaGrtRouteDestType_Object = MibTableColumn
alaGrtRouteDestType = _AlaGrtRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1, 3),
    _AlaGrtRouteDestType_Type()
)
alaGrtRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrtRouteDestType.setStatus("current")


class _AlaGrtRouteMaskLen_Type(Integer32):
    """Custom type alaGrtRouteMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaGrtRouteMaskLen_Type.__name__ = "Integer32"
_AlaGrtRouteMaskLen_Object = MibTableColumn
alaGrtRouteMaskLen = _AlaGrtRouteMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1, 4),
    _AlaGrtRouteMaskLen_Type()
)
alaGrtRouteMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrtRouteMaskLen.setStatus("current")


class _AlaGrtRouteNextHop_Type(InetAddress):
    """Custom type alaGrtRouteNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaGrtRouteNextHop_Type.__name__ = "InetAddress"
_AlaGrtRouteNextHop_Object = MibTableColumn
alaGrtRouteNextHop = _AlaGrtRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1, 5),
    _AlaGrtRouteNextHop_Type()
)
alaGrtRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrtRouteNextHop.setStatus("current")
_AlaGrtRouteNextHopType_Type = InetAddressType
_AlaGrtRouteNextHopType_Object = MibTableColumn
alaGrtRouteNextHopType = _AlaGrtRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1, 6),
    _AlaGrtRouteNextHopType_Type()
)
alaGrtRouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrtRouteNextHopType.setStatus("current")
_AlaGrtRouteMetric_Type = Unsigned32
_AlaGrtRouteMetric_Object = MibTableColumn
alaGrtRouteMetric = _AlaGrtRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1, 7),
    _AlaGrtRouteMetric_Type()
)
alaGrtRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGrtRouteMetric.setStatus("current")
_AlaGrtRouteTag_Type = Unsigned32
_AlaGrtRouteTag_Object = MibTableColumn
alaGrtRouteTag = _AlaGrtRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1, 8),
    _AlaGrtRouteTag_Type()
)
alaGrtRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGrtRouteTag.setStatus("current")
_AlaGrtRouteVrfName_Type = SnmpAdminString
_AlaGrtRouteVrfName_Object = MibTableColumn
alaGrtRouteVrfName = _AlaGrtRouteVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1, 9),
    _AlaGrtRouteVrfName_Type()
)
alaGrtRouteVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGrtRouteVrfName.setStatus("current")

# Managed Objects groups

alaGlobalRouteTableMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 1, 2, 1)
)
alaGlobalRouteTableMIBGroup.setObjects(
      *(("ALCATEL-IND1-GRT-MIB", "alaGrtRouteVrfName"),
        ("ALCATEL-IND1-GRT-MIB", "alaGrtRouteMetric"),
        ("ALCATEL-IND1-GRT-MIB", "alaGrtRouteTag"))
)
if mibBuilder.loadTexts:
    alaGlobalRouteTableMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaGlobalRouteTableCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 1, 1, 1)
)
alaGlobalRouteTableCompliance.setObjects(
    ("ALCATEL-IND1-GRT-MIB", "alaGlobalRouteTableMIBGroup")
)
if mibBuilder.loadTexts:
    alaGlobalRouteTableCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-GRT-MIB",
    **{"AlaGrtRouteDistinguisher": AlaGrtRouteDistinguisher,
       "alcatelIND1GRTMIB": alcatelIND1GRTMIB,
       "alcatelIND1GRTMIBConformance": alcatelIND1GRTMIBConformance,
       "alcatelIND1GRTMIBCompliances": alcatelIND1GRTMIBCompliances,
       "alaGlobalRouteTableCompliance": alaGlobalRouteTableCompliance,
       "alcatelIND1GRTMIBGroups": alcatelIND1GRTMIBGroups,
       "alaGlobalRouteTableMIBGroup": alaGlobalRouteTableMIBGroup,
       "alcatelIND1GRTMIBObjects": alcatelIND1GRTMIBObjects,
       "alaGrtConfig": alaGrtConfig,
       "alaGrtRouteTable": alaGrtRouteTable,
       "alaGrtRouteEntry": alaGrtRouteEntry,
       "alaGrtRouteDistinguisher": alaGrtRouteDistinguisher,
       "alaGrtRouteDest": alaGrtRouteDest,
       "alaGrtRouteDestType": alaGrtRouteDestType,
       "alaGrtRouteMaskLen": alaGrtRouteMaskLen,
       "alaGrtRouteNextHop": alaGrtRouteNextHop,
       "alaGrtRouteNextHopType": alaGrtRouteNextHopType,
       "alaGrtRouteMetric": alaGrtRouteMetric,
       "alaGrtRouteTag": alaGrtRouteTag,
       "alaGrtRouteVrfName": alaGrtRouteVrfName}
)
