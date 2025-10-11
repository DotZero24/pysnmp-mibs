# SNMP MIB module (ALCATEL-ENT1-IPV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-IPV6-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:10:18 2025
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

(softentIND1Ipv6,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1Ipv6")

(alaVirtualRouterName,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-VIRTUALROUTER-MIB",
    "alaVirtualRouterName")

(ipv6IfIndex,
 ipv6RouteEntry) = mibBuilder.importSymbols(
    "IPV6-MIB",
    "ipv6IfIndex",
    "ipv6RouteEntry")

(Ipv6Address,
 Ipv6IfIndexOrZero) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6IfIndexOrZero")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1IPv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1IPv6MIB.setRevisions(
        ("2016-04-12 00:00",
         "2015-03-24 00:00",
         "2014-10-14 00:00",
         "2014-09-18 00:00",
         "2014-08-12 00:00",
         "2014-05-20 00:00",
         "2014-02-28 00:00",
         "2013-07-30 00:00",
         "2013-07-29 00:00",
         "2013-03-13 00:00",
         "2012-02-07 00:00",
         "2011-03-09 00:00",
         "2010-05-13 00:00",
         "2010-01-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaIPv6AddressPrefix(TextualConvention, OctetString):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class AlaIPv6RAFilterTrustedSourceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("netAddress", 2),
          ("physAddress", 3))
    )



class AlaIPv6RAFilterTrustedSourceValue(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class AlaIPv6RAFilterTrustedSourceIfIndex(TextualConvention, OctetString):
    status = "current"
    displayHint = "4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1IPv6MIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1IPv6MIBNotifications = _AlcatelIND1IPv6MIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1IPv6MIBNotifications.setStatus("current")
_AlcatelIND1IPv6MIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1IPv6MIBObjects = _AlcatelIND1IPv6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1)
)
_AlaIPv6Config_ObjectIdentity = ObjectIdentity
alaIPv6Config = _AlaIPv6Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 1)
)


class _AlaIPv6ClearNeighbors_Type(Integer32):
    """Custom type alaIPv6ClearNeighbors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AlaIPv6ClearNeighbors_Type.__name__ = "Integer32"
_AlaIPv6ClearNeighbors_Object = MibScalar
alaIPv6ClearNeighbors = _AlaIPv6ClearNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 1, 1),
    _AlaIPv6ClearNeighbors_Type()
)
alaIPv6ClearNeighbors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIPv6ClearNeighbors.setStatus("current")


class _AlaIPv6ClearTraffic_Type(Integer32):
    """Custom type alaIPv6ClearTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AlaIPv6ClearTraffic_Type.__name__ = "Integer32"
_AlaIPv6ClearTraffic_Object = MibScalar
alaIPv6ClearTraffic = _AlaIPv6ClearTraffic_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 1, 2),
    _AlaIPv6ClearTraffic_Type()
)
alaIPv6ClearTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIPv6ClearTraffic.setStatus("current")


class _AlaIPv6ClearPMTUTable_Type(Integer32):
    """Custom type alaIPv6ClearPMTUTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AlaIPv6ClearPMTUTable_Type.__name__ = "Integer32"
_AlaIPv6ClearPMTUTable_Object = MibScalar
alaIPv6ClearPMTUTable = _AlaIPv6ClearPMTUTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 1, 3),
    _AlaIPv6ClearPMTUTable_Type()
)
alaIPv6ClearPMTUTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIPv6ClearPMTUTable.setStatus("current")


class _AlaIPv6PMTUMinLifetime_Type(Unsigned32):
    """Custom type alaIPv6PMTUMinLifetime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1440),
    )


_AlaIPv6PMTUMinLifetime_Type.__name__ = "Unsigned32"
_AlaIPv6PMTUMinLifetime_Object = MibScalar
alaIPv6PMTUMinLifetime = _AlaIPv6PMTUMinLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 1, 4),
    _AlaIPv6PMTUMinLifetime_Type()
)
alaIPv6PMTUMinLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIPv6PMTUMinLifetime.setStatus("current")
if mibBuilder.loadTexts:
    alaIPv6PMTUMinLifetime.setUnits("minutes")


class _AlaIPv6NeighborStaleLifetime_Type(Unsigned32):
    """Custom type alaIPv6NeighborStaleLifetime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2880),
    )


_AlaIPv6NeighborStaleLifetime_Type.__name__ = "Unsigned32"
_AlaIPv6NeighborStaleLifetime_Object = MibScalar
alaIPv6NeighborStaleLifetime = _AlaIPv6NeighborStaleLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 1, 5),
    _AlaIPv6NeighborStaleLifetime_Type()
)
alaIPv6NeighborStaleLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIPv6NeighborStaleLifetime.setStatus("current")
if mibBuilder.loadTexts:
    alaIPv6NeighborStaleLifetime.setUnits("minutes")


class _AlaIPv6GlobalID_Type(OctetString):
    """Custom type alaIPv6GlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_AlaIPv6GlobalID_Type.__name__ = "OctetString"
_AlaIPv6GlobalID_Object = MibScalar
alaIPv6GlobalID = _AlaIPv6GlobalID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 1, 6),
    _AlaIPv6GlobalID_Type()
)
alaIPv6GlobalID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIPv6GlobalID.setStatus("current")


class _AlaIPv6VirtualSourceMAC_Type(Integer32):
    """Custom type alaIPv6VirtualSourceMAC based on Integer32"""
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


_AlaIPv6VirtualSourceMAC_Type.__name__ = "Integer32"
_AlaIPv6VirtualSourceMAC_Object = MibScalar
alaIPv6VirtualSourceMAC = _AlaIPv6VirtualSourceMAC_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 1, 7),
    _AlaIPv6VirtualSourceMAC_Type()
)
alaIPv6VirtualSourceMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIPv6VirtualSourceMAC.setStatus("current")


class _AlaIPv6NeighborLimit_Type(Unsigned32):
    """Custom type alaIPv6NeighborLimit based on Unsigned32"""
    defaultValue = 8000


_AlaIPv6NeighborLimit_Type.__name__ = "Unsigned32"
_AlaIPv6NeighborLimit_Object = MibScalar
alaIPv6NeighborLimit = _AlaIPv6NeighborLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 1, 8),
    _AlaIPv6NeighborLimit_Type()
)
alaIPv6NeighborLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIPv6NeighborLimit.setStatus("current")


class _AlaIPv6NeighborVRFLimit_Type(Unsigned32):
    """Custom type alaIPv6NeighborVRFLimit based on Unsigned32"""
    defaultValue = 0


_AlaIPv6NeighborVRFLimit_Type.__name__ = "Unsigned32"
_AlaIPv6NeighborVRFLimit_Object = MibScalar
alaIPv6NeighborVRFLimit = _AlaIPv6NeighborVRFLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 1, 9),
    _AlaIPv6NeighborVRFLimit_Type()
)
alaIPv6NeighborVRFLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIPv6NeighborVRFLimit.setStatus("current")
_AlaIPv6InterfaceTable_Object = MibTable
alaIPv6InterfaceTable = _AlaIPv6InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaIPv6InterfaceTable.setStatus("current")
_AlaIPv6InterfaceEntry_Object = MibTableRow
alaIPv6InterfaceEntry = _AlaIPv6InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1)
)
alaIPv6InterfaceEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
)
if mibBuilder.loadTexts:
    alaIPv6InterfaceEntry.setStatus("current")
_AlaIPv6InterfaceRowStatus_Type = RowStatus
_AlaIPv6InterfaceRowStatus_Object = MibTableColumn
alaIPv6InterfaceRowStatus = _AlaIPv6InterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 1),
    _AlaIPv6InterfaceRowStatus_Type()
)
alaIPv6InterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceRowStatus.setStatus("current")


class _AlaIPv6InterfaceDescription_Type(SnmpAdminString):
    """Custom type alaIPv6InterfaceDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AlaIPv6InterfaceDescription_Type.__name__ = "SnmpAdminString"
_AlaIPv6InterfaceDescription_Object = MibTableColumn
alaIPv6InterfaceDescription = _AlaIPv6InterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 2),
    _AlaIPv6InterfaceDescription_Type()
)
alaIPv6InterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6InterfaceDescription.setStatus("current")
_AlaIPv6InterfaceMtu_Type = Unsigned32
_AlaIPv6InterfaceMtu_Object = MibTableColumn
alaIPv6InterfaceMtu = _AlaIPv6InterfaceMtu_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 3),
    _AlaIPv6InterfaceMtu_Type()
)
alaIPv6InterfaceMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceMtu.setStatus("current")


class _AlaIPv6InterfaceType_Type(Integer32):
    """Custom type alaIPv6InterfaceType based on Integer32"""
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
        *(("other", 1),
          ("vlan", 2),
          ("tunnel", 3),
          ("loopback", 4))
    )


_AlaIPv6InterfaceType_Type.__name__ = "Integer32"
_AlaIPv6InterfaceType_Object = MibTableColumn
alaIPv6InterfaceType = _AlaIPv6InterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 4),
    _AlaIPv6InterfaceType_Type()
)
alaIPv6InterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6InterfaceType.setStatus("current")


class _AlaIPv6InterfaceAdminStatus_Type(Integer32):
    """Custom type alaIPv6InterfaceAdminStatus based on Integer32"""
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


_AlaIPv6InterfaceAdminStatus_Type.__name__ = "Integer32"
_AlaIPv6InterfaceAdminStatus_Object = MibTableColumn
alaIPv6InterfaceAdminStatus = _AlaIPv6InterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 5),
    _AlaIPv6InterfaceAdminStatus_Type()
)
alaIPv6InterfaceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceAdminStatus.setStatus("current")


class _AlaIPv6InterfaceSendRouterAdvertisements_Type(Integer32):
    """Custom type alaIPv6InterfaceSendRouterAdvertisements based on Integer32"""
    defaultValue = 1

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


_AlaIPv6InterfaceSendRouterAdvertisements_Type.__name__ = "Integer32"
_AlaIPv6InterfaceSendRouterAdvertisements_Object = MibTableColumn
alaIPv6InterfaceSendRouterAdvertisements = _AlaIPv6InterfaceSendRouterAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 6),
    _AlaIPv6InterfaceSendRouterAdvertisements_Type()
)
alaIPv6InterfaceSendRouterAdvertisements.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceSendRouterAdvertisements.setStatus("current")


class _AlaIPv6InterfaceMaxRtrAdvInterval_Type(Unsigned32):
    """Custom type alaIPv6InterfaceMaxRtrAdvInterval based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_AlaIPv6InterfaceMaxRtrAdvInterval_Type.__name__ = "Unsigned32"
_AlaIPv6InterfaceMaxRtrAdvInterval_Object = MibTableColumn
alaIPv6InterfaceMaxRtrAdvInterval = _AlaIPv6InterfaceMaxRtrAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 7),
    _AlaIPv6InterfaceMaxRtrAdvInterval_Type()
)
alaIPv6InterfaceMaxRtrAdvInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceMaxRtrAdvInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaIPv6InterfaceMaxRtrAdvInterval.setUnits("seconds")


class _AlaIPv6InterfaceAdvManagedFlag_Type(TruthValue):
    """Custom type alaIPv6InterfaceAdvManagedFlag based on TruthValue"""
    defaultValue = 2


_AlaIPv6InterfaceAdvManagedFlag_Type.__name__ = "TruthValue"
_AlaIPv6InterfaceAdvManagedFlag_Object = MibTableColumn
alaIPv6InterfaceAdvManagedFlag = _AlaIPv6InterfaceAdvManagedFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 8),
    _AlaIPv6InterfaceAdvManagedFlag_Type()
)
alaIPv6InterfaceAdvManagedFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceAdvManagedFlag.setStatus("current")


class _AlaIPv6InterfaceAdvOtherConfigFlag_Type(TruthValue):
    """Custom type alaIPv6InterfaceAdvOtherConfigFlag based on TruthValue"""
    defaultValue = 2


_AlaIPv6InterfaceAdvOtherConfigFlag_Type.__name__ = "TruthValue"
_AlaIPv6InterfaceAdvOtherConfigFlag_Object = MibTableColumn
alaIPv6InterfaceAdvOtherConfigFlag = _AlaIPv6InterfaceAdvOtherConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 9),
    _AlaIPv6InterfaceAdvOtherConfigFlag_Type()
)
alaIPv6InterfaceAdvOtherConfigFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceAdvOtherConfigFlag.setStatus("current")


class _AlaIPv6InterfaceAdvReachableTime_Type(Unsigned32):
    """Custom type alaIPv6InterfaceAdvReachableTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_AlaIPv6InterfaceAdvReachableTime_Type.__name__ = "Unsigned32"
_AlaIPv6InterfaceAdvReachableTime_Object = MibTableColumn
alaIPv6InterfaceAdvReachableTime = _AlaIPv6InterfaceAdvReachableTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 10),
    _AlaIPv6InterfaceAdvReachableTime_Type()
)
alaIPv6InterfaceAdvReachableTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceAdvReachableTime.setStatus("current")
if mibBuilder.loadTexts:
    alaIPv6InterfaceAdvReachableTime.setUnits("milliseconds")


class _AlaIPv6InterfaceAdvRetransTimer_Type(Unsigned32):
    """Custom type alaIPv6InterfaceAdvRetransTimer based on Unsigned32"""
    defaultValue = 0


_AlaIPv6InterfaceAdvRetransTimer_Type.__name__ = "Unsigned32"
_AlaIPv6InterfaceAdvRetransTimer_Object = MibTableColumn
alaIPv6InterfaceAdvRetransTimer = _AlaIPv6InterfaceAdvRetransTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 11),
    _AlaIPv6InterfaceAdvRetransTimer_Type()
)
alaIPv6InterfaceAdvRetransTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceAdvRetransTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaIPv6InterfaceAdvRetransTimer.setUnits("milliseconds")


class _AlaIPv6InterfaceAdvDefaultLifetime_Type(Unsigned32):
    """Custom type alaIPv6InterfaceAdvDefaultLifetime based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
    )


_AlaIPv6InterfaceAdvDefaultLifetime_Type.__name__ = "Unsigned32"
_AlaIPv6InterfaceAdvDefaultLifetime_Object = MibTableColumn
alaIPv6InterfaceAdvDefaultLifetime = _AlaIPv6InterfaceAdvDefaultLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 12),
    _AlaIPv6InterfaceAdvDefaultLifetime_Type()
)
alaIPv6InterfaceAdvDefaultLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceAdvDefaultLifetime.setStatus("current")
if mibBuilder.loadTexts:
    alaIPv6InterfaceAdvDefaultLifetime.setUnits("seconds")


class _AlaIPv6InterfaceName_Type(SnmpAdminString):
    """Custom type alaIPv6InterfaceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaIPv6InterfaceName_Type.__name__ = "SnmpAdminString"
_AlaIPv6InterfaceName_Object = MibTableColumn
alaIPv6InterfaceName = _AlaIPv6InterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 13),
    _AlaIPv6InterfaceName_Type()
)
alaIPv6InterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceName.setStatus("current")


class _AlaIPv6InterfaceAdvSendMtu_Type(TruthValue):
    """Custom type alaIPv6InterfaceAdvSendMtu based on TruthValue"""
    defaultValue = 2


_AlaIPv6InterfaceAdvSendMtu_Type.__name__ = "TruthValue"
_AlaIPv6InterfaceAdvSendMtu_Object = MibTableColumn
alaIPv6InterfaceAdvSendMtu = _AlaIPv6InterfaceAdvSendMtu_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 14),
    _AlaIPv6InterfaceAdvSendMtu_Type()
)
alaIPv6InterfaceAdvSendMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceAdvSendMtu.setStatus("current")
_AlaIPv6InterfaceReachableTime_Type = Unsigned32
_AlaIPv6InterfaceReachableTime_Object = MibTableColumn
alaIPv6InterfaceReachableTime = _AlaIPv6InterfaceReachableTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 15),
    _AlaIPv6InterfaceReachableTime_Type()
)
alaIPv6InterfaceReachableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6InterfaceReachableTime.setStatus("current")
if mibBuilder.loadTexts:
    alaIPv6InterfaceReachableTime.setUnits("seconds")


class _AlaIPv6InterfaceBaseReachableTime_Type(Unsigned32):
    """Custom type alaIPv6InterfaceBaseReachableTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_AlaIPv6InterfaceBaseReachableTime_Type.__name__ = "Unsigned32"
_AlaIPv6InterfaceBaseReachableTime_Object = MibTableColumn
alaIPv6InterfaceBaseReachableTime = _AlaIPv6InterfaceBaseReachableTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 16),
    _AlaIPv6InterfaceBaseReachableTime_Type()
)
alaIPv6InterfaceBaseReachableTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceBaseReachableTime.setStatus("current")
if mibBuilder.loadTexts:
    alaIPv6InterfaceBaseReachableTime.setUnits("seconds")


class _AlaIPv6InterfaceMinRtrAdvInterval_Type(Unsigned32):
    """Custom type alaIPv6InterfaceMinRtrAdvInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1350),
    )


_AlaIPv6InterfaceMinRtrAdvInterval_Type.__name__ = "Unsigned32"
_AlaIPv6InterfaceMinRtrAdvInterval_Object = MibTableColumn
alaIPv6InterfaceMinRtrAdvInterval = _AlaIPv6InterfaceMinRtrAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 17),
    _AlaIPv6InterfaceMinRtrAdvInterval_Type()
)
alaIPv6InterfaceMinRtrAdvInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceMinRtrAdvInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaIPv6InterfaceMinRtrAdvInterval.setUnits("seconds")


class _AlaIPv6InterfaceClockSkew_Type(Unsigned32):
    """Custom type alaIPv6InterfaceClockSkew based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AlaIPv6InterfaceClockSkew_Type.__name__ = "Unsigned32"
_AlaIPv6InterfaceClockSkew_Object = MibTableColumn
alaIPv6InterfaceClockSkew = _AlaIPv6InterfaceClockSkew_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 18),
    _AlaIPv6InterfaceClockSkew_Type()
)
alaIPv6InterfaceClockSkew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceClockSkew.setStatus("current")
if mibBuilder.loadTexts:
    alaIPv6InterfaceClockSkew.setUnits("seconds")


class _AlaIPv6InterfaceRetransTimer_Type(Unsigned32):
    """Custom type alaIPv6InterfaceRetransTimer based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 30000),
    )


_AlaIPv6InterfaceRetransTimer_Type.__name__ = "Unsigned32"
_AlaIPv6InterfaceRetransTimer_Object = MibTableColumn
alaIPv6InterfaceRetransTimer = _AlaIPv6InterfaceRetransTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 19),
    _AlaIPv6InterfaceRetransTimer_Type()
)
alaIPv6InterfaceRetransTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceRetransTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaIPv6InterfaceRetransTimer.setUnits("milliseconds")


class _AlaIPv6InterfaceDADTransmits_Type(Unsigned32):
    """Custom type alaIPv6InterfaceDADTransmits based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AlaIPv6InterfaceDADTransmits_Type.__name__ = "Unsigned32"
_AlaIPv6InterfaceDADTransmits_Object = MibTableColumn
alaIPv6InterfaceDADTransmits = _AlaIPv6InterfaceDADTransmits_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 20),
    _AlaIPv6InterfaceDADTransmits_Type()
)
alaIPv6InterfaceDADTransmits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceDADTransmits.setStatus("current")


class _AlaIPv6InterfaceAdvHopLimit_Type(Unsigned32):
    """Custom type alaIPv6InterfaceAdvHopLimit based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaIPv6InterfaceAdvHopLimit_Type.__name__ = "Unsigned32"
_AlaIPv6InterfaceAdvHopLimit_Object = MibTableColumn
alaIPv6InterfaceAdvHopLimit = _AlaIPv6InterfaceAdvHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 21),
    _AlaIPv6InterfaceAdvHopLimit_Type()
)
alaIPv6InterfaceAdvHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceAdvHopLimit.setStatus("current")


class _AlaIPv6InterfaceLPND_Type(Integer32):
    """Custom type alaIPv6InterfaceLPND based on Integer32"""
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


_AlaIPv6InterfaceLPND_Type.__name__ = "Integer32"
_AlaIPv6InterfaceLPND_Object = MibTableColumn
alaIPv6InterfaceLPND = _AlaIPv6InterfaceLPND_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 22),
    _AlaIPv6InterfaceLPND_Type()
)
alaIPv6InterfaceLPND.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceLPND.setStatus("current")


class _AlaIPv6InterfaceRAFilter_Type(Integer32):
    """Custom type alaIPv6InterfaceRAFilter based on Integer32"""
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


_AlaIPv6InterfaceRAFilter_Type.__name__ = "Integer32"
_AlaIPv6InterfaceRAFilter_Object = MibTableColumn
alaIPv6InterfaceRAFilter = _AlaIPv6InterfaceRAFilter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 23),
    _AlaIPv6InterfaceRAFilter_Type()
)
alaIPv6InterfaceRAFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceRAFilter.setStatus("deprecated")


class _AlaIPv6InterfaceNeighborLimit_Type(Unsigned32):
    """Custom type alaIPv6InterfaceNeighborLimit based on Unsigned32"""
    defaultValue = 0


_AlaIPv6InterfaceNeighborLimit_Type.__name__ = "Unsigned32"
_AlaIPv6InterfaceNeighborLimit_Object = MibTableColumn
alaIPv6InterfaceNeighborLimit = _AlaIPv6InterfaceNeighborLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 24),
    _AlaIPv6InterfaceNeighborLimit_Type()
)
alaIPv6InterfaceNeighborLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceNeighborLimit.setStatus("current")


class _AlaIPv6InterfaceRetransBackoff_Type(Unsigned32):
    """Custom type alaIPv6InterfaceRetransBackoff based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AlaIPv6InterfaceRetransBackoff_Type.__name__ = "Unsigned32"
_AlaIPv6InterfaceRetransBackoff_Object = MibTableColumn
alaIPv6InterfaceRetransBackoff = _AlaIPv6InterfaceRetransBackoff_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 25),
    _AlaIPv6InterfaceRetransBackoff_Type()
)
alaIPv6InterfaceRetransBackoff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceRetransBackoff.setStatus("current")


class _AlaIPv6InterfaceRetransMax_Type(Unsigned32):
    """Custom type alaIPv6InterfaceRetransMax based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AlaIPv6InterfaceRetransMax_Type.__name__ = "Unsigned32"
_AlaIPv6InterfaceRetransMax_Object = MibTableColumn
alaIPv6InterfaceRetransMax = _AlaIPv6InterfaceRetransMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 26),
    _AlaIPv6InterfaceRetransMax_Type()
)
alaIPv6InterfaceRetransMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceRetransMax.setStatus("current")


class _AlaIPv6InterfaceRouterPreference_Type(Integer32):
    """Custom type alaIPv6InterfaceRouterPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("medium", 0),
          ("high", 1),
          ("low", 3))
    )


_AlaIPv6InterfaceRouterPreference_Type.__name__ = "Integer32"
_AlaIPv6InterfaceRouterPreference_Object = MibTableColumn
alaIPv6InterfaceRouterPreference = _AlaIPv6InterfaceRouterPreference_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 2, 1, 27),
    _AlaIPv6InterfaceRouterPreference_Type()
)
alaIPv6InterfaceRouterPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceRouterPreference.setStatus("current")
_AlaIPv6TunnelConfig_ObjectIdentity = ObjectIdentity
alaIPv6TunnelConfig = _AlaIPv6TunnelConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 3)
)
_AlaIPv6ConfigTunnelTable_Object = MibTable
alaIPv6ConfigTunnelTable = _AlaIPv6ConfigTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    alaIPv6ConfigTunnelTable.setStatus("current")
_AlaIPv6ConfigTunnelEntry_Object = MibTableRow
alaIPv6ConfigTunnelEntry = _AlaIPv6ConfigTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 3, 2, 1)
)
alaIPv6ConfigTunnelEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
)
if mibBuilder.loadTexts:
    alaIPv6ConfigTunnelEntry.setStatus("current")
_AlaIPv6ConfigTunnelV4Source_Type = IpAddress
_AlaIPv6ConfigTunnelV4Source_Object = MibTableColumn
alaIPv6ConfigTunnelV4Source = _AlaIPv6ConfigTunnelV4Source_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 3, 2, 1, 1),
    _AlaIPv6ConfigTunnelV4Source_Type()
)
alaIPv6ConfigTunnelV4Source.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6ConfigTunnelV4Source.setStatus("current")
_AlaIPv6ConfigTunnelV4Dest_Type = IpAddress
_AlaIPv6ConfigTunnelV4Dest_Object = MibTableColumn
alaIPv6ConfigTunnelV4Dest = _AlaIPv6ConfigTunnelV4Dest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 3, 2, 1, 2),
    _AlaIPv6ConfigTunnelV4Dest_Type()
)
alaIPv6ConfigTunnelV4Dest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6ConfigTunnelV4Dest.setStatus("current")
_AlaIPv6InterfaceAddressTable_Object = MibTable
alaIPv6InterfaceAddressTable = _AlaIPv6InterfaceAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaIPv6InterfaceAddressTable.setStatus("current")
_AlaIPv6InterfaceAddressEntry_Object = MibTableRow
alaIPv6InterfaceAddressEntry = _AlaIPv6InterfaceAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 4, 1)
)
alaIPv6InterfaceAddressEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
    (0, "ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceAddress"),
)
if mibBuilder.loadTexts:
    alaIPv6InterfaceAddressEntry.setStatus("current")
_AlaIPv6InterfaceAddressRowStatus_Type = RowStatus
_AlaIPv6InterfaceAddressRowStatus_Object = MibTableColumn
alaIPv6InterfaceAddressRowStatus = _AlaIPv6InterfaceAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 4, 1, 1),
    _AlaIPv6InterfaceAddressRowStatus_Type()
)
alaIPv6InterfaceAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceAddressRowStatus.setStatus("current")
_AlaIPv6InterfaceAddress_Type = Ipv6Address
_AlaIPv6InterfaceAddress_Object = MibTableColumn
alaIPv6InterfaceAddress = _AlaIPv6InterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 4, 1, 2),
    _AlaIPv6InterfaceAddress_Type()
)
alaIPv6InterfaceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPv6InterfaceAddress.setStatus("current")


class _AlaIPv6InterfaceAddressPrefixLength_Type(Unsigned32):
    """Custom type alaIPv6InterfaceAddressPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 128),
    )


_AlaIPv6InterfaceAddressPrefixLength_Type.__name__ = "Unsigned32"
_AlaIPv6InterfaceAddressPrefixLength_Object = MibTableColumn
alaIPv6InterfaceAddressPrefixLength = _AlaIPv6InterfaceAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 4, 1, 3),
    _AlaIPv6InterfaceAddressPrefixLength_Type()
)
alaIPv6InterfaceAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceAddressPrefixLength.setStatus("current")


class _AlaIPv6InterfaceAddressAnycastFlag_Type(TruthValue):
    """Custom type alaIPv6InterfaceAddressAnycastFlag based on TruthValue"""
    defaultValue = 2


_AlaIPv6InterfaceAddressAnycastFlag_Type.__name__ = "TruthValue"
_AlaIPv6InterfaceAddressAnycastFlag_Object = MibTableColumn
alaIPv6InterfaceAddressAnycastFlag = _AlaIPv6InterfaceAddressAnycastFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 4, 1, 4),
    _AlaIPv6InterfaceAddressAnycastFlag_Type()
)
alaIPv6InterfaceAddressAnycastFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceAddressAnycastFlag.setStatus("current")


class _AlaIPv6InterfaceAddressDADStatus_Type(Integer32):
    """Custom type alaIPv6InterfaceAddressDADStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("pending", 1),
          ("duplicate", 2),
          ("passed", 3),
          ("check", 4))
    )


_AlaIPv6InterfaceAddressDADStatus_Type.__name__ = "Integer32"
_AlaIPv6InterfaceAddressDADStatus_Object = MibTableColumn
alaIPv6InterfaceAddressDADStatus = _AlaIPv6InterfaceAddressDADStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 4, 1, 5),
    _AlaIPv6InterfaceAddressDADStatus_Type()
)
alaIPv6InterfaceAddressDADStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceAddressDADStatus.setStatus("current")
_AlaIPv6InterfaceEUI64AddressTable_Object = MibTable
alaIPv6InterfaceEUI64AddressTable = _AlaIPv6InterfaceEUI64AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaIPv6InterfaceEUI64AddressTable.setStatus("current")
_AlaIPv6InterfaceEUI64AddressEntry_Object = MibTableRow
alaIPv6InterfaceEUI64AddressEntry = _AlaIPv6InterfaceEUI64AddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 5, 1)
)
alaIPv6InterfaceEUI64AddressEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
    (0, "ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceEUI64AddressPrefix"),
)
if mibBuilder.loadTexts:
    alaIPv6InterfaceEUI64AddressEntry.setStatus("current")
_AlaIPv6InterfaceEUI64AddressRowStatus_Type = RowStatus
_AlaIPv6InterfaceEUI64AddressRowStatus_Object = MibTableColumn
alaIPv6InterfaceEUI64AddressRowStatus = _AlaIPv6InterfaceEUI64AddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 5, 1, 1),
    _AlaIPv6InterfaceEUI64AddressRowStatus_Type()
)
alaIPv6InterfaceEUI64AddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceEUI64AddressRowStatus.setStatus("current")
_AlaIPv6InterfaceEUI64AddressPrefix_Type = AlaIPv6AddressPrefix
_AlaIPv6InterfaceEUI64AddressPrefix_Object = MibTableColumn
alaIPv6InterfaceEUI64AddressPrefix = _AlaIPv6InterfaceEUI64AddressPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 5, 1, 2),
    _AlaIPv6InterfaceEUI64AddressPrefix_Type()
)
alaIPv6InterfaceEUI64AddressPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPv6InterfaceEUI64AddressPrefix.setStatus("current")
_AlaIPv6InterfaceEUI64AddressPrefixLength_Type = Unsigned32
_AlaIPv6InterfaceEUI64AddressPrefixLength_Object = MibTableColumn
alaIPv6InterfaceEUI64AddressPrefixLength = _AlaIPv6InterfaceEUI64AddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 5, 1, 3),
    _AlaIPv6InterfaceEUI64AddressPrefixLength_Type()
)
alaIPv6InterfaceEUI64AddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfaceEUI64AddressPrefixLength.setStatus("current")


class _AlaIPv6InterfaceEUI64AddressIdentifier_Type(OctetString):
    """Custom type alaIPv6InterfaceEUI64AddressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_AlaIPv6InterfaceEUI64AddressIdentifier_Type.__name__ = "OctetString"
_AlaIPv6InterfaceEUI64AddressIdentifier_Object = MibTableColumn
alaIPv6InterfaceEUI64AddressIdentifier = _AlaIPv6InterfaceEUI64AddressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 5, 1, 4),
    _AlaIPv6InterfaceEUI64AddressIdentifier_Type()
)
alaIPv6InterfaceEUI64AddressIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6InterfaceEUI64AddressIdentifier.setStatus("current")
_AlaIPv6NeighborTable_Object = MibTable
alaIPv6NeighborTable = _AlaIPv6NeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaIPv6NeighborTable.setStatus("current")
_AlaIPv6NeighborEntry_Object = MibTableRow
alaIPv6NeighborEntry = _AlaIPv6NeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 6, 1)
)
alaIPv6NeighborEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
    (0, "ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborNetAddress"),
)
if mibBuilder.loadTexts:
    alaIPv6NeighborEntry.setStatus("current")
_AlaIPv6NeighborNetAddress_Type = Ipv6Address
_AlaIPv6NeighborNetAddress_Object = MibTableColumn
alaIPv6NeighborNetAddress = _AlaIPv6NeighborNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 6, 1, 1),
    _AlaIPv6NeighborNetAddress_Type()
)
alaIPv6NeighborNetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPv6NeighborNetAddress.setStatus("current")
_AlaIPv6NeighborPhysAddress_Type = PhysAddress
_AlaIPv6NeighborPhysAddress_Object = MibTableColumn
alaIPv6NeighborPhysAddress = _AlaIPv6NeighborPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 6, 1, 2),
    _AlaIPv6NeighborPhysAddress_Type()
)
alaIPv6NeighborPhysAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6NeighborPhysAddress.setStatus("current")
_AlaIPv6NeighborSlot_Type = Unsigned32
_AlaIPv6NeighborSlot_Object = MibTableColumn
alaIPv6NeighborSlot = _AlaIPv6NeighborSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 6, 1, 3),
    _AlaIPv6NeighborSlot_Type()
)
alaIPv6NeighborSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6NeighborSlot.setStatus("deprecated")
_AlaIPv6NeighborPort_Type = Unsigned32
_AlaIPv6NeighborPort_Object = MibTableColumn
alaIPv6NeighborPort = _AlaIPv6NeighborPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 6, 1, 4),
    _AlaIPv6NeighborPort_Type()
)
alaIPv6NeighborPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6NeighborPort.setStatus("deprecated")


class _AlaIPv6NeighborType_Type(Integer32):
    """Custom type alaIPv6NeighborType based on Integer32"""
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
        *(("other", 1),
          ("dynamic", 2),
          ("static", 3),
          ("local", 4))
    )


_AlaIPv6NeighborType_Type.__name__ = "Integer32"
_AlaIPv6NeighborType_Object = MibTableColumn
alaIPv6NeighborType = _AlaIPv6NeighborType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 6, 1, 5),
    _AlaIPv6NeighborType_Type()
)
alaIPv6NeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6NeighborType.setStatus("current")


class _AlaIPv6NeighborState_Type(Integer32):
    """Custom type alaIPv6NeighborState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 1),
          ("stale", 2),
          ("delay", 3),
          ("probe", 4),
          ("invalid", 5),
          ("unknown", 6))
    )


_AlaIPv6NeighborState_Type.__name__ = "Integer32"
_AlaIPv6NeighborState_Object = MibTableColumn
alaIPv6NeighborState = _AlaIPv6NeighborState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 6, 1, 6),
    _AlaIPv6NeighborState_Type()
)
alaIPv6NeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6NeighborState.setStatus("deprecated")
_AlaIPv6NeighborLastUpdated_Type = TimeStamp
_AlaIPv6NeighborLastUpdated_Object = MibTableColumn
alaIPv6NeighborLastUpdated = _AlaIPv6NeighborLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 6, 1, 7),
    _AlaIPv6NeighborLastUpdated_Type()
)
alaIPv6NeighborLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6NeighborLastUpdated.setStatus("current")
_AlaIPv6NeighborRowStatus_Type = RowStatus
_AlaIPv6NeighborRowStatus_Object = MibTableColumn
alaIPv6NeighborRowStatus = _AlaIPv6NeighborRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 6, 1, 8),
    _AlaIPv6NeighborRowStatus_Type()
)
alaIPv6NeighborRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6NeighborRowStatus.setStatus("current")
_AlaIPv6NeighborLifetime_Type = Unsigned32
_AlaIPv6NeighborLifetime_Object = MibTableColumn
alaIPv6NeighborLifetime = _AlaIPv6NeighborLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 6, 1, 9),
    _AlaIPv6NeighborLifetime_Type()
)
alaIPv6NeighborLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6NeighborLifetime.setStatus("current")
if mibBuilder.loadTexts:
    alaIPv6NeighborLifetime.setUnits("seconds")


class _AlaIPv6NeighborReachability_Type(Integer32):
    """Custom type alaIPv6NeighborReachability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("confirmed", 1),
          ("unconfirmed", 2),
          ("incomplete", 3))
    )


_AlaIPv6NeighborReachability_Type.__name__ = "Integer32"
_AlaIPv6NeighborReachability_Object = MibTableColumn
alaIPv6NeighborReachability = _AlaIPv6NeighborReachability_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 6, 1, 10),
    _AlaIPv6NeighborReachability_Type()
)
alaIPv6NeighborReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6NeighborReachability.setStatus("current")


class _AlaIPv6NeighborChassis_Type(Unsigned32):
    """Custom type alaIPv6NeighborChassis based on Unsigned32"""
    defaultValue = 0


_AlaIPv6NeighborChassis_Type.__name__ = "Unsigned32"
_AlaIPv6NeighborChassis_Object = MibTableColumn
alaIPv6NeighborChassis = _AlaIPv6NeighborChassis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 6, 1, 11),
    _AlaIPv6NeighborChassis_Type()
)
alaIPv6NeighborChassis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6NeighborChassis.setStatus("deprecated")
_AlaIPv6NeighborPortIfIndex_Type = Unsigned32
_AlaIPv6NeighborPortIfIndex_Object = MibTableColumn
alaIPv6NeighborPortIfIndex = _AlaIPv6NeighborPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 6, 1, 12),
    _AlaIPv6NeighborPortIfIndex_Type()
)
alaIPv6NeighborPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6NeighborPortIfIndex.setStatus("current")
_AlaIPv6StaticRouteTable_Object = MibTable
alaIPv6StaticRouteTable = _AlaIPv6StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaIPv6StaticRouteTable.setStatus("obsolete")
_AlaIPv6StaticRouteEntry_Object = MibTableRow
alaIPv6StaticRouteEntry = _AlaIPv6StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 7, 1)
)
alaIPv6StaticRouteEntry.setIndexNames(
    (0, "ALCATEL-ENT1-IPV6-MIB", "alaIPv6StaticRouteDest"),
    (0, "ALCATEL-ENT1-IPV6-MIB", "alaIPv6StaticRoutePfxLength"),
)
if mibBuilder.loadTexts:
    alaIPv6StaticRouteEntry.setStatus("obsolete")
_AlaIPv6StaticRouteDest_Type = Ipv6Address
_AlaIPv6StaticRouteDest_Object = MibTableColumn
alaIPv6StaticRouteDest = _AlaIPv6StaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 7, 1, 1),
    _AlaIPv6StaticRouteDest_Type()
)
alaIPv6StaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPv6StaticRouteDest.setStatus("obsolete")


class _AlaIPv6StaticRoutePfxLength_Type(Integer32):
    """Custom type alaIPv6StaticRoutePfxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AlaIPv6StaticRoutePfxLength_Type.__name__ = "Integer32"
_AlaIPv6StaticRoutePfxLength_Object = MibTableColumn
alaIPv6StaticRoutePfxLength = _AlaIPv6StaticRoutePfxLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 7, 1, 2),
    _AlaIPv6StaticRoutePfxLength_Type()
)
alaIPv6StaticRoutePfxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPv6StaticRoutePfxLength.setStatus("obsolete")


class _AlaIPv6StaticRouteIfIndex_Type(Ipv6IfIndexOrZero):
    """Custom type alaIPv6StaticRouteIfIndex based on Ipv6IfIndexOrZero"""
    defaultValue = 0


_AlaIPv6StaticRouteIfIndex_Type.__name__ = "Ipv6IfIndexOrZero"
_AlaIPv6StaticRouteIfIndex_Object = MibTableColumn
alaIPv6StaticRouteIfIndex = _AlaIPv6StaticRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 7, 1, 3),
    _AlaIPv6StaticRouteIfIndex_Type()
)
alaIPv6StaticRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6StaticRouteIfIndex.setStatus("obsolete")
_AlaIPv6StaticRouteNextHop_Type = Ipv6Address
_AlaIPv6StaticRouteNextHop_Object = MibTableColumn
alaIPv6StaticRouteNextHop = _AlaIPv6StaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 7, 1, 4),
    _AlaIPv6StaticRouteNextHop_Type()
)
alaIPv6StaticRouteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6StaticRouteNextHop.setStatus("obsolete")


class _AlaIPv6StaticRouteMetric_Type(Unsigned32):
    """Custom type alaIPv6StaticRouteMetric based on Unsigned32"""
    defaultValue = 1


_AlaIPv6StaticRouteMetric_Type.__name__ = "Unsigned32"
_AlaIPv6StaticRouteMetric_Object = MibTableColumn
alaIPv6StaticRouteMetric = _AlaIPv6StaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 7, 1, 5),
    _AlaIPv6StaticRouteMetric_Type()
)
alaIPv6StaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6StaticRouteMetric.setStatus("obsolete")
_AlaIPv6StaticRouteRowStatus_Type = RowStatus
_AlaIPv6StaticRouteRowStatus_Object = MibTableColumn
alaIPv6StaticRouteRowStatus = _AlaIPv6StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 7, 1, 6),
    _AlaIPv6StaticRouteRowStatus_Type()
)
alaIPv6StaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6StaticRouteRowStatus.setStatus("obsolete")
_AlaIPv6HostTable_Object = MibTable
alaIPv6HostTable = _AlaIPv6HostTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alaIPv6HostTable.setStatus("current")
_AlaIPv6HostEntry_Object = MibTableRow
alaIPv6HostEntry = _AlaIPv6HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 8, 1)
)
alaIPv6HostEntry.setIndexNames(
    (0, "ALCATEL-ENT1-IPV6-MIB", "alaIPv6HostName"),
    (0, "ALCATEL-ENT1-IPV6-MIB", "alaIPv6HostAddress"),
)
if mibBuilder.loadTexts:
    alaIPv6HostEntry.setStatus("current")


class _AlaIPv6HostName_Type(SnmpAdminString):
    """Custom type alaIPv6HostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AlaIPv6HostName_Type.__name__ = "SnmpAdminString"
_AlaIPv6HostName_Object = MibTableColumn
alaIPv6HostName = _AlaIPv6HostName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 8, 1, 1),
    _AlaIPv6HostName_Type()
)
alaIPv6HostName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPv6HostName.setStatus("current")
_AlaIPv6HostAddress_Type = Ipv6Address
_AlaIPv6HostAddress_Object = MibTableColumn
alaIPv6HostAddress = _AlaIPv6HostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 8, 1, 2),
    _AlaIPv6HostAddress_Type()
)
alaIPv6HostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPv6HostAddress.setStatus("current")
_AlaIPv6HostRowStatus_Type = RowStatus
_AlaIPv6HostRowStatus_Object = MibTableColumn
alaIPv6HostRowStatus = _AlaIPv6HostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 8, 1, 3),
    _AlaIPv6HostRowStatus_Type()
)
alaIPv6HostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6HostRowStatus.setStatus("current")
_AlaIPv6InterfacePrefixTable_Object = MibTable
alaIPv6InterfacePrefixTable = _AlaIPv6InterfacePrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaIPv6InterfacePrefixTable.setStatus("current")
_AlaIPv6InterfacePrefixEntry_Object = MibTableRow
alaIPv6InterfacePrefixEntry = _AlaIPv6InterfacePrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 9, 1)
)
alaIPv6InterfacePrefixEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
    (0, "ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfacePrefix"),
    (0, "ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfacePrefixLength"),
)
if mibBuilder.loadTexts:
    alaIPv6InterfacePrefixEntry.setStatus("current")
_AlaIPv6InterfacePrefixRowStatus_Type = RowStatus
_AlaIPv6InterfacePrefixRowStatus_Object = MibTableColumn
alaIPv6InterfacePrefixRowStatus = _AlaIPv6InterfacePrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 9, 1, 1),
    _AlaIPv6InterfacePrefixRowStatus_Type()
)
alaIPv6InterfacePrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfacePrefixRowStatus.setStatus("current")
_AlaIPv6InterfacePrefix_Type = Ipv6Address
_AlaIPv6InterfacePrefix_Object = MibTableColumn
alaIPv6InterfacePrefix = _AlaIPv6InterfacePrefix_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 9, 1, 2),
    _AlaIPv6InterfacePrefix_Type()
)
alaIPv6InterfacePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPv6InterfacePrefix.setStatus("current")


class _AlaIPv6InterfacePrefixLength_Type(Unsigned32):
    """Custom type alaIPv6InterfacePrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AlaIPv6InterfacePrefixLength_Type.__name__ = "Unsigned32"
_AlaIPv6InterfacePrefixLength_Object = MibTableColumn
alaIPv6InterfacePrefixLength = _AlaIPv6InterfacePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 9, 1, 3),
    _AlaIPv6InterfacePrefixLength_Type()
)
alaIPv6InterfacePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPv6InterfacePrefixLength.setStatus("current")


class _AlaIPv6InterfacePrefixValidLifetime_Type(Unsigned32):
    """Custom type alaIPv6InterfacePrefixValidLifetime based on Unsigned32"""
    defaultValue = 2592000


_AlaIPv6InterfacePrefixValidLifetime_Type.__name__ = "Unsigned32"
_AlaIPv6InterfacePrefixValidLifetime_Object = MibTableColumn
alaIPv6InterfacePrefixValidLifetime = _AlaIPv6InterfacePrefixValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 9, 1, 4),
    _AlaIPv6InterfacePrefixValidLifetime_Type()
)
alaIPv6InterfacePrefixValidLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfacePrefixValidLifetime.setStatus("current")
if mibBuilder.loadTexts:
    alaIPv6InterfacePrefixValidLifetime.setUnits("seconds")


class _AlaIPv6InterfacePrefixOnLinkFlag_Type(TruthValue):
    """Custom type alaIPv6InterfacePrefixOnLinkFlag based on TruthValue"""
    defaultValue = 1


_AlaIPv6InterfacePrefixOnLinkFlag_Type.__name__ = "TruthValue"
_AlaIPv6InterfacePrefixOnLinkFlag_Object = MibTableColumn
alaIPv6InterfacePrefixOnLinkFlag = _AlaIPv6InterfacePrefixOnLinkFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 9, 1, 5),
    _AlaIPv6InterfacePrefixOnLinkFlag_Type()
)
alaIPv6InterfacePrefixOnLinkFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfacePrefixOnLinkFlag.setStatus("current")


class _AlaIPv6InterfacePrefixPreferredLifetime_Type(Unsigned32):
    """Custom type alaIPv6InterfacePrefixPreferredLifetime based on Unsigned32"""
    defaultValue = 604800


_AlaIPv6InterfacePrefixPreferredLifetime_Type.__name__ = "Unsigned32"
_AlaIPv6InterfacePrefixPreferredLifetime_Object = MibTableColumn
alaIPv6InterfacePrefixPreferredLifetime = _AlaIPv6InterfacePrefixPreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 9, 1, 6),
    _AlaIPv6InterfacePrefixPreferredLifetime_Type()
)
alaIPv6InterfacePrefixPreferredLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfacePrefixPreferredLifetime.setStatus("current")
if mibBuilder.loadTexts:
    alaIPv6InterfacePrefixPreferredLifetime.setUnits("seconds")


class _AlaIPv6InterfacePrefixAutonomousFlag_Type(TruthValue):
    """Custom type alaIPv6InterfacePrefixAutonomousFlag based on TruthValue"""
    defaultValue = 1


_AlaIPv6InterfacePrefixAutonomousFlag_Type.__name__ = "TruthValue"
_AlaIPv6InterfacePrefixAutonomousFlag_Object = MibTableColumn
alaIPv6InterfacePrefixAutonomousFlag = _AlaIPv6InterfacePrefixAutonomousFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 9, 1, 7),
    _AlaIPv6InterfacePrefixAutonomousFlag_Type()
)
alaIPv6InterfacePrefixAutonomousFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfacePrefixAutonomousFlag.setStatus("current")


class _AlaIPv6InterfacePrefixSource_Type(Integer32):
    """Custom type alaIPv6InterfacePrefixSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("dynamic", 2),
          ("configured", 3))
    )


_AlaIPv6InterfacePrefixSource_Type.__name__ = "Integer32"
_AlaIPv6InterfacePrefixSource_Object = MibTableColumn
alaIPv6InterfacePrefixSource = _AlaIPv6InterfacePrefixSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 9, 1, 8),
    _AlaIPv6InterfacePrefixSource_Type()
)
alaIPv6InterfacePrefixSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6InterfacePrefixSource.setStatus("current")


class _AlaIPv6InterfacePrefixValidLifetimeDecrement_Type(TruthValue):
    """Custom type alaIPv6InterfacePrefixValidLifetimeDecrement based on TruthValue"""
    defaultValue = 2


_AlaIPv6InterfacePrefixValidLifetimeDecrement_Type.__name__ = "TruthValue"
_AlaIPv6InterfacePrefixValidLifetimeDecrement_Object = MibTableColumn
alaIPv6InterfacePrefixValidLifetimeDecrement = _AlaIPv6InterfacePrefixValidLifetimeDecrement_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 9, 1, 9),
    _AlaIPv6InterfacePrefixValidLifetimeDecrement_Type()
)
alaIPv6InterfacePrefixValidLifetimeDecrement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfacePrefixValidLifetimeDecrement.setStatus("current")
_AlaIPv6InterfacePrefixValidLifetimeExpire_Type = DateAndTime
_AlaIPv6InterfacePrefixValidLifetimeExpire_Object = MibTableColumn
alaIPv6InterfacePrefixValidLifetimeExpire = _AlaIPv6InterfacePrefixValidLifetimeExpire_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 9, 1, 10),
    _AlaIPv6InterfacePrefixValidLifetimeExpire_Type()
)
alaIPv6InterfacePrefixValidLifetimeExpire.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfacePrefixValidLifetimeExpire.setStatus("current")


class _AlaIPv6InterfacePrefixPreferredLifetimeDecrement_Type(TruthValue):
    """Custom type alaIPv6InterfacePrefixPreferredLifetimeDecrement based on TruthValue"""
    defaultValue = 2


_AlaIPv6InterfacePrefixPreferredLifetimeDecrement_Type.__name__ = "TruthValue"
_AlaIPv6InterfacePrefixPreferredLifetimeDecrement_Object = MibTableColumn
alaIPv6InterfacePrefixPreferredLifetimeDecrement = _AlaIPv6InterfacePrefixPreferredLifetimeDecrement_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 9, 1, 11),
    _AlaIPv6InterfacePrefixPreferredLifetimeDecrement_Type()
)
alaIPv6InterfacePrefixPreferredLifetimeDecrement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfacePrefixPreferredLifetimeDecrement.setStatus("current")
_AlaIPv6InterfacePrefixPreferredLifetimeExpire_Type = DateAndTime
_AlaIPv6InterfacePrefixPreferredLifetimeExpire_Object = MibTableColumn
alaIPv6InterfacePrefixPreferredLifetimeExpire = _AlaIPv6InterfacePrefixPreferredLifetimeExpire_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 9, 1, 12),
    _AlaIPv6InterfacePrefixPreferredLifetimeExpire_Type()
)
alaIPv6InterfacePrefixPreferredLifetimeExpire.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6InterfacePrefixPreferredLifetimeExpire.setStatus("current")
_AlaIPv6PMTUTable_Object = MibTable
alaIPv6PMTUTable = _AlaIPv6PMTUTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 10)
)
if mibBuilder.loadTexts:
    alaIPv6PMTUTable.setStatus("current")
_AlaIPv6PMTUEntry_Object = MibTableRow
alaIPv6PMTUEntry = _AlaIPv6PMTUEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 10, 1)
)
alaIPv6PMTUEntry.setIndexNames(
    (0, "ALCATEL-ENT1-IPV6-MIB", "alaIPv6PMTUDest"),
)
if mibBuilder.loadTexts:
    alaIPv6PMTUEntry.setStatus("current")
_AlaIPv6PMTUDest_Type = Ipv6Address
_AlaIPv6PMTUDest_Object = MibTableColumn
alaIPv6PMTUDest = _AlaIPv6PMTUDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 10, 1, 1),
    _AlaIPv6PMTUDest_Type()
)
alaIPv6PMTUDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPv6PMTUDest.setStatus("current")
_AlaIPv6PMTU_Type = Unsigned32
_AlaIPv6PMTU_Object = MibTableColumn
alaIPv6PMTU = _AlaIPv6PMTU_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 10, 1, 2),
    _AlaIPv6PMTU_Type()
)
alaIPv6PMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6PMTU.setStatus("current")
_AlaIPv6PMTUExpire_Type = Unsigned32
_AlaIPv6PMTUExpire_Object = MibTableColumn
alaIPv6PMTUExpire = _AlaIPv6PMTUExpire_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 10, 1, 3),
    _AlaIPv6PMTUExpire_Type()
)
alaIPv6PMTUExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6PMTUExpire.setStatus("current")
if mibBuilder.loadTexts:
    alaIPv6PMTUExpire.setUnits("minutes")
_AlaIPv6PMTUHits_Type = Counter32
_AlaIPv6PMTUHits_Object = MibTableColumn
alaIPv6PMTUHits = _AlaIPv6PMTUHits_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 10, 1, 4),
    _AlaIPv6PMTUHits_Type()
)
alaIPv6PMTUHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6PMTUHits.setStatus("current")
_AlaIPv6PMTUUpdates_Type = Counter32
_AlaIPv6PMTUUpdates_Object = MibTableColumn
alaIPv6PMTUUpdates = _AlaIPv6PMTUUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 10, 1, 5),
    _AlaIPv6PMTUUpdates_Type()
)
alaIPv6PMTUUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6PMTUUpdates.setStatus("current")
_AlaIPv6RouteFlagsTable_Object = MibTable
alaIPv6RouteFlagsTable = _AlaIPv6RouteFlagsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaIPv6RouteFlagsTable.setStatus("current")
_AlaIPv6RouteFlagsEntry_Object = MibTableRow
alaIPv6RouteFlagsEntry = _AlaIPv6RouteFlagsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    alaIPv6RouteFlagsEntry.setStatus("current")
_AlaIPv6RouteFlagsUp_Type = TruthValue
_AlaIPv6RouteFlagsUp_Object = MibTableColumn
alaIPv6RouteFlagsUp = _AlaIPv6RouteFlagsUp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 11, 1, 1),
    _AlaIPv6RouteFlagsUp_Type()
)
alaIPv6RouteFlagsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6RouteFlagsUp.setStatus("current")
_AlaIPv6RouteFlagsGateway_Type = TruthValue
_AlaIPv6RouteFlagsGateway_Object = MibTableColumn
alaIPv6RouteFlagsGateway = _AlaIPv6RouteFlagsGateway_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 11, 1, 2),
    _AlaIPv6RouteFlagsGateway_Type()
)
alaIPv6RouteFlagsGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6RouteFlagsGateway.setStatus("current")
_AlaIPv6RouteFlagsHost_Type = TruthValue
_AlaIPv6RouteFlagsHost_Object = MibTableColumn
alaIPv6RouteFlagsHost = _AlaIPv6RouteFlagsHost_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 11, 1, 3),
    _AlaIPv6RouteFlagsHost_Type()
)
alaIPv6RouteFlagsHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6RouteFlagsHost.setStatus("current")
_AlaIPv6RouteFlagsStatic_Type = TruthValue
_AlaIPv6RouteFlagsStatic_Object = MibTableColumn
alaIPv6RouteFlagsStatic = _AlaIPv6RouteFlagsStatic_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 11, 1, 4),
    _AlaIPv6RouteFlagsStatic_Type()
)
alaIPv6RouteFlagsStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6RouteFlagsStatic.setStatus("current")
_AlaIPv6RouteFlagsCloneable_Type = TruthValue
_AlaIPv6RouteFlagsCloneable_Object = MibTableColumn
alaIPv6RouteFlagsCloneable = _AlaIPv6RouteFlagsCloneable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 11, 1, 5),
    _AlaIPv6RouteFlagsCloneable_Type()
)
alaIPv6RouteFlagsCloneable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6RouteFlagsCloneable.setStatus("current")
_AlaIPv6RouteFlagsDiscard_Type = TruthValue
_AlaIPv6RouteFlagsDiscard_Object = MibTableColumn
alaIPv6RouteFlagsDiscard = _AlaIPv6RouteFlagsDiscard_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 11, 1, 6),
    _AlaIPv6RouteFlagsDiscard_Type()
)
alaIPv6RouteFlagsDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6RouteFlagsDiscard.setStatus("current")
_AlaIPv6RouteFlagsECMP_Type = TruthValue
_AlaIPv6RouteFlagsECMP_Object = MibTableColumn
alaIPv6RouteFlagsECMP = _AlaIPv6RouteFlagsECMP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 11, 1, 7),
    _AlaIPv6RouteFlagsECMP_Type()
)
alaIPv6RouteFlagsECMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6RouteFlagsECMP.setStatus("current")
_AlaIPv6RouteFlagsTransient_Type = TruthValue
_AlaIPv6RouteFlagsTransient_Object = MibTableColumn
alaIPv6RouteFlagsTransient = _AlaIPv6RouteFlagsTransient_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 11, 1, 8),
    _AlaIPv6RouteFlagsTransient_Type()
)
alaIPv6RouteFlagsTransient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPv6RouteFlagsTransient.setStatus("current")
_AlaIPv6LocalUnicastTable_Object = MibTable
alaIPv6LocalUnicastTable = _AlaIPv6LocalUnicastTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 13)
)
if mibBuilder.loadTexts:
    alaIPv6LocalUnicastTable.setStatus("current")
_AlaIPv6LocalUnicastEntry_Object = MibTableRow
alaIPv6LocalUnicastEntry = _AlaIPv6LocalUnicastEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 13, 1)
)
alaIPv6LocalUnicastEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
    (0, "ALCATEL-ENT1-IPV6-MIB", "alaIPv6LocalUnicastGlobalID"),
    (0, "ALCATEL-ENT1-IPV6-MIB", "alaIPv6LocalUnicastSubnetID"),
    (0, "ALCATEL-ENT1-IPV6-MIB", "alaIPv6LocalUnicastInterfaceID"),
)
if mibBuilder.loadTexts:
    alaIPv6LocalUnicastEntry.setStatus("current")


class _AlaIPv6LocalUnicastGlobalID_Type(OctetString):
    """Custom type alaIPv6LocalUnicastGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_AlaIPv6LocalUnicastGlobalID_Type.__name__ = "OctetString"
_AlaIPv6LocalUnicastGlobalID_Object = MibTableColumn
alaIPv6LocalUnicastGlobalID = _AlaIPv6LocalUnicastGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 13, 1, 1),
    _AlaIPv6LocalUnicastGlobalID_Type()
)
alaIPv6LocalUnicastGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPv6LocalUnicastGlobalID.setStatus("current")


class _AlaIPv6LocalUnicastSubnetID_Type(OctetString):
    """Custom type alaIPv6LocalUnicastSubnetID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AlaIPv6LocalUnicastSubnetID_Type.__name__ = "OctetString"
_AlaIPv6LocalUnicastSubnetID_Object = MibTableColumn
alaIPv6LocalUnicastSubnetID = _AlaIPv6LocalUnicastSubnetID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 13, 1, 2),
    _AlaIPv6LocalUnicastSubnetID_Type()
)
alaIPv6LocalUnicastSubnetID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPv6LocalUnicastSubnetID.setStatus("current")


class _AlaIPv6LocalUnicastInterfaceID_Type(OctetString):
    """Custom type alaIPv6LocalUnicastInterfaceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_AlaIPv6LocalUnicastInterfaceID_Type.__name__ = "OctetString"
_AlaIPv6LocalUnicastInterfaceID_Object = MibTableColumn
alaIPv6LocalUnicastInterfaceID = _AlaIPv6LocalUnicastInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 13, 1, 3),
    _AlaIPv6LocalUnicastInterfaceID_Type()
)
alaIPv6LocalUnicastInterfaceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPv6LocalUnicastInterfaceID.setStatus("current")


class _AlaIPv6LocalUnicastPrefixLength_Type(Unsigned32):
    """Custom type alaIPv6LocalUnicastPrefixLength based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 128),
    )


_AlaIPv6LocalUnicastPrefixLength_Type.__name__ = "Unsigned32"
_AlaIPv6LocalUnicastPrefixLength_Object = MibTableColumn
alaIPv6LocalUnicastPrefixLength = _AlaIPv6LocalUnicastPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 13, 1, 4),
    _AlaIPv6LocalUnicastPrefixLength_Type()
)
alaIPv6LocalUnicastPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6LocalUnicastPrefixLength.setStatus("current")


class _AlaIPv6LocalUnicastEUI64_Type(TruthValue):
    """Custom type alaIPv6LocalUnicastEUI64 based on TruthValue"""
    defaultValue = 2


_AlaIPv6LocalUnicastEUI64_Type.__name__ = "TruthValue"
_AlaIPv6LocalUnicastEUI64_Object = MibTableColumn
alaIPv6LocalUnicastEUI64 = _AlaIPv6LocalUnicastEUI64_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 13, 1, 5),
    _AlaIPv6LocalUnicastEUI64_Type()
)
alaIPv6LocalUnicastEUI64.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6LocalUnicastEUI64.setStatus("current")
_AlaIPv6LocalUnicastRowStatus_Type = RowStatus
_AlaIPv6LocalUnicastRowStatus_Object = MibTableColumn
alaIPv6LocalUnicastRowStatus = _AlaIPv6LocalUnicastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 13, 1, 6),
    _AlaIPv6LocalUnicastRowStatus_Type()
)
alaIPv6LocalUnicastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6LocalUnicastRowStatus.setStatus("current")
_AlaIPv6RAFilterTrustedPortTable_Object = MibTable
alaIPv6RAFilterTrustedPortTable = _AlaIPv6RAFilterTrustedPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 15)
)
if mibBuilder.loadTexts:
    alaIPv6RAFilterTrustedPortTable.setStatus("deprecated")
_AlaIPv6RAFilterTrustedPortEntry_Object = MibTableRow
alaIPv6RAFilterTrustedPortEntry = _AlaIPv6RAFilterTrustedPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 15, 1)
)
alaIPv6RAFilterTrustedPortEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
    (0, "ALCATEL-ENT1-IPV6-MIB", "alaIPv6RAFilterTrustedPortIfIndex"),
)
if mibBuilder.loadTexts:
    alaIPv6RAFilterTrustedPortEntry.setStatus("deprecated")
_AlaIPv6RAFilterTrustedPortIfIndex_Type = Unsigned32
_AlaIPv6RAFilterTrustedPortIfIndex_Object = MibTableColumn
alaIPv6RAFilterTrustedPortIfIndex = _AlaIPv6RAFilterTrustedPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 15, 1, 1),
    _AlaIPv6RAFilterTrustedPortIfIndex_Type()
)
alaIPv6RAFilterTrustedPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPv6RAFilterTrustedPortIfIndex.setStatus("deprecated")
_AlaIPv6RAFilterTrustedPortRowStatus_Type = RowStatus
_AlaIPv6RAFilterTrustedPortRowStatus_Object = MibTableColumn
alaIPv6RAFilterTrustedPortRowStatus = _AlaIPv6RAFilterTrustedPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 15, 1, 2),
    _AlaIPv6RAFilterTrustedPortRowStatus_Type()
)
alaIPv6RAFilterTrustedPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6RAFilterTrustedPortRowStatus.setStatus("deprecated")
_AlaIPv6RAFilterInterfaceTable_Object = MibTable
alaIPv6RAFilterInterfaceTable = _AlaIPv6RAFilterInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 16)
)
if mibBuilder.loadTexts:
    alaIPv6RAFilterInterfaceTable.setStatus("current")
_AlaIPv6RAFilterInterfaceEntry_Object = MibTableRow
alaIPv6RAFilterInterfaceEntry = _AlaIPv6RAFilterInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 16, 1)
)
alaIPv6RAFilterInterfaceEntry.setIndexNames(
    (0, "ALCATEL-ENT1-IPV6-MIB", "alaIPv6RAFilterInterfaceVlan"),
)
if mibBuilder.loadTexts:
    alaIPv6RAFilterInterfaceEntry.setStatus("current")
_AlaIPv6RAFilterInterfaceVlan_Type = Unsigned32
_AlaIPv6RAFilterInterfaceVlan_Object = MibTableColumn
alaIPv6RAFilterInterfaceVlan = _AlaIPv6RAFilterInterfaceVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 16, 1, 1),
    _AlaIPv6RAFilterInterfaceVlan_Type()
)
alaIPv6RAFilterInterfaceVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPv6RAFilterInterfaceVlan.setStatus("current")


class _AlaIPv6RAFilterInterfaceAdminStatus_Type(Integer32):
    """Custom type alaIPv6RAFilterInterfaceAdminStatus based on Integer32"""
    defaultValue = 1

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


_AlaIPv6RAFilterInterfaceAdminStatus_Type.__name__ = "Integer32"
_AlaIPv6RAFilterInterfaceAdminStatus_Object = MibTableColumn
alaIPv6RAFilterInterfaceAdminStatus = _AlaIPv6RAFilterInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 16, 1, 2),
    _AlaIPv6RAFilterInterfaceAdminStatus_Type()
)
alaIPv6RAFilterInterfaceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6RAFilterInterfaceAdminStatus.setStatus("current")
_AlaIPv6RAFilterInterfaceRowStatus_Type = RowStatus
_AlaIPv6RAFilterInterfaceRowStatus_Object = MibTableColumn
alaIPv6RAFilterInterfaceRowStatus = _AlaIPv6RAFilterInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 16, 1, 3),
    _AlaIPv6RAFilterInterfaceRowStatus_Type()
)
alaIPv6RAFilterInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6RAFilterInterfaceRowStatus.setStatus("current")
_AlaIPv6RAFilterTrustedSourceTable_Object = MibTable
alaIPv6RAFilterTrustedSourceTable = _AlaIPv6RAFilterTrustedSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 17)
)
if mibBuilder.loadTexts:
    alaIPv6RAFilterTrustedSourceTable.setStatus("current")
_AlaIPv6RAFilterTrustedSourceEntry_Object = MibTableRow
alaIPv6RAFilterTrustedSourceEntry = _AlaIPv6RAFilterTrustedSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 17, 1)
)
alaIPv6RAFilterTrustedSourceEntry.setIndexNames(
    (0, "ALCATEL-ENT1-IPV6-MIB", "alaIPv6RAFilterInterfaceVlan"),
    (0, "ALCATEL-ENT1-IPV6-MIB", "alaIPv6RAFilterTrustedSourceType"),
    (0, "ALCATEL-ENT1-IPV6-MIB", "alaIPv6RAFilterTrustedSourceValue"),
)
if mibBuilder.loadTexts:
    alaIPv6RAFilterTrustedSourceEntry.setStatus("current")
_AlaIPv6RAFilterTrustedSourceType_Type = AlaIPv6RAFilterTrustedSourceType
_AlaIPv6RAFilterTrustedSourceType_Object = MibTableColumn
alaIPv6RAFilterTrustedSourceType = _AlaIPv6RAFilterTrustedSourceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 17, 1, 1),
    _AlaIPv6RAFilterTrustedSourceType_Type()
)
alaIPv6RAFilterTrustedSourceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPv6RAFilterTrustedSourceType.setStatus("current")
_AlaIPv6RAFilterTrustedSourceValue_Type = AlaIPv6RAFilterTrustedSourceValue
_AlaIPv6RAFilterTrustedSourceValue_Object = MibTableColumn
alaIPv6RAFilterTrustedSourceValue = _AlaIPv6RAFilterTrustedSourceValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 17, 1, 2),
    _AlaIPv6RAFilterTrustedSourceValue_Type()
)
alaIPv6RAFilterTrustedSourceValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPv6RAFilterTrustedSourceValue.setStatus("current")
_AlaIPv6RAFilterTrustedSourceRowStatus_Type = RowStatus
_AlaIPv6RAFilterTrustedSourceRowStatus_Object = MibTableColumn
alaIPv6RAFilterTrustedSourceRowStatus = _AlaIPv6RAFilterTrustedSourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 1, 17, 1, 3),
    _AlaIPv6RAFilterTrustedSourceRowStatus_Type()
)
alaIPv6RAFilterTrustedSourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPv6RAFilterTrustedSourceRowStatus.setStatus("current")
_AlcatelIND1IPv6MIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1IPv6MIBConformance = _AlcatelIND1IPv6MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2)
)
_AlcatelIND1IPv6MIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1IPv6MIBCompliances = _AlcatelIND1IPv6MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 1)
)
_AlcatelIND1IPv6MIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1IPv6MIBGroups = _AlcatelIND1IPv6MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 2)
)
ipv6RouteEntry.registerAugmentions(
    ("ALCATEL-ENT1-IPV6-MIB",
     "alaIPv6RouteFlagsEntry")
)
alaIPv6RouteFlagsEntry.setIndexNames(*ipv6RouteEntry.getIndexNames())

# Managed Objects groups

alaIPv6TunnelConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 2, 1)
)
alaIPv6TunnelConfigGroup.setObjects(
      *(("ALCATEL-ENT1-IPV6-MIB", "alaIPv6ConfigTunnelV4Source"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6ConfigTunnelV4Dest"))
)
if mibBuilder.loadTexts:
    alaIPv6TunnelConfigGroup.setStatus("current")

alaIPv6ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 2, 2)
)
alaIPv6ConfigGroup.setObjects(
      *(("ALCATEL-ENT1-IPV6-MIB", "alaIPv6ClearNeighbors"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6ClearTraffic"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6ClearPMTUTable"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6PMTUMinLifetime"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborStaleLifetime"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6GlobalID"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6VirtualSourceMAC"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborLimit"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborVRFLimit"))
)
if mibBuilder.loadTexts:
    alaIPv6ConfigGroup.setStatus("current")

alaIPv6NeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 2, 3)
)
alaIPv6NeighborGroup.setObjects(
      *(("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborPhysAddress"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborType"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborLastUpdated"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborRowStatus"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborLifetime"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborReachability"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborPortIfIndex"))
)
if mibBuilder.loadTexts:
    alaIPv6NeighborGroup.setStatus("current")

alaIPv6StaticRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 2, 4)
)
alaIPv6StaticRouteGroup.setObjects(
      *(("ALCATEL-ENT1-IPV6-MIB", "alaIPv6StaticRouteIfIndex"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6StaticRouteNextHop"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6StaticRouteMetric"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6StaticRouteRowStatus"))
)
if mibBuilder.loadTexts:
    alaIPv6StaticRouteGroup.setStatus("obsolete")

alaIPv6InterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 2, 5)
)
alaIPv6InterfaceGroup.setObjects(
      *(("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceRowStatus"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceDescription"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceMtu"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceType"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceAdminStatus"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceSendRouterAdvertisements"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceMaxRtrAdvInterval"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceAdvManagedFlag"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceAdvOtherConfigFlag"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceAdvReachableTime"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceAdvRetransTimer"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceAdvDefaultLifetime"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceName"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceAdvSendMtu"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceReachableTime"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceBaseReachableTime"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceMinRtrAdvInterval"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceClockSkew"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceRetransTimer"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceDADTransmits"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceAdvHopLimit"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceLPND"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceNeighborLimit"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceRetransBackoff"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceRetransMax"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceRouterPreference"))
)
if mibBuilder.loadTexts:
    alaIPv6InterfaceGroup.setStatus("current")

alaIPv6InterfaceAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 2, 6)
)
alaIPv6InterfaceAddressGroup.setObjects(
      *(("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceAddressRowStatus"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceAddressPrefixLength"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceAddressAnycastFlag"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceAddressDADStatus"))
)
if mibBuilder.loadTexts:
    alaIPv6InterfaceAddressGroup.setStatus("current")

alaIPv6InterfaceEUI64AddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 2, 7)
)
alaIPv6InterfaceEUI64AddressGroup.setObjects(
      *(("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceEUI64AddressRowStatus"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceEUI64AddressPrefixLength"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceEUI64AddressIdentifier"))
)
if mibBuilder.loadTexts:
    alaIPv6InterfaceEUI64AddressGroup.setStatus("current")

alaIPv6InterfacePrefixGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 2, 8)
)
alaIPv6InterfacePrefixGroup.setObjects(
      *(("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfacePrefixRowStatus"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfacePrefixValidLifetime"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfacePrefixOnLinkFlag"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfacePrefixPreferredLifetime"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfacePrefixAutonomousFlag"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfacePrefixSource"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfacePrefixValidLifetimeDecrement"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfacePrefixValidLifetimeExpire"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfacePrefixPreferredLifetimeDecrement"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfacePrefixPreferredLifetimeExpire"))
)
if mibBuilder.loadTexts:
    alaIPv6InterfacePrefixGroup.setStatus("current")

alaIPv6PMTUGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 2, 9)
)
alaIPv6PMTUGroup.setObjects(
      *(("ALCATEL-ENT1-IPV6-MIB", "alaIPv6PMTU"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6PMTUExpire"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6PMTUHits"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6PMTUUpdates"))
)
if mibBuilder.loadTexts:
    alaIPv6PMTUGroup.setStatus("current")

alaIPv6RouteFlagsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 2, 10)
)
alaIPv6RouteFlagsGroup.setObjects(
      *(("ALCATEL-ENT1-IPV6-MIB", "alaIPv6RouteFlagsUp"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6RouteFlagsGateway"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6RouteFlagsHost"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6RouteFlagsStatic"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6RouteFlagsCloneable"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6RouteFlagsDiscard"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6RouteFlagsECMP"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6RouteFlagsTransient"))
)
if mibBuilder.loadTexts:
    alaIPv6RouteFlagsGroup.setStatus("current")

alaIPv6LocalUnicastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 2, 11)
)
alaIPv6LocalUnicastGroup.setObjects(
      *(("ALCATEL-ENT1-IPV6-MIB", "alaIPv6LocalUnicastPrefixLength"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6LocalUnicastEUI64"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6LocalUnicastRowStatus"))
)
if mibBuilder.loadTexts:
    alaIPv6LocalUnicastGroup.setStatus("current")

alaIPv6HostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 2, 12)
)
alaIPv6HostGroup.setObjects(
    ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6HostRowStatus")
)
if mibBuilder.loadTexts:
    alaIPv6HostGroup.setStatus("current")

alcatelIND1IPv6DeprecatedObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 2, 14)
)
alcatelIND1IPv6DeprecatedObjectGroup.setObjects(
      *(("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborSlot"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborPort"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborState"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborChassis"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceRAFilter"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6RAFilterTrustedPortRowStatus"))
)
if mibBuilder.loadTexts:
    alcatelIND1IPv6DeprecatedObjectGroup.setStatus("current")

alaIPv6RAFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 2, 16)
)
alaIPv6RAFilterGroup.setObjects(
      *(("ALCATEL-ENT1-IPV6-MIB", "alaIPv6RAFilterInterfaceAdminStatus"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6RAFilterInterfaceRowStatus"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6RAFilterTrustedSourceRowStatus"))
)
if mibBuilder.loadTexts:
    alaIPv6RAFilterGroup.setStatus("current")


# Notification objects

ndpMaxLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 0, 1)
)
if mibBuilder.loadTexts:
    ndpMaxLimitReached.setStatus(
        "deprecated"
    )

alaIPv6NeighborLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 0, 2)
)
alaIPv6NeighborLimitExceeded.setObjects(
    ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborLimit")
)
if mibBuilder.loadTexts:
    alaIPv6NeighborLimitExceeded.setStatus(
        "current"
    )

alaIPv6NeighborVRFLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 0, 3)
)
alaIPv6NeighborVRFLimitExceeded.setObjects(
      *(("ALCATEL-ENT1-VIRTUALROUTER-MIB", "alaVirtualRouterName"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborVRFLimit"))
)
if mibBuilder.loadTexts:
    alaIPv6NeighborVRFLimitExceeded.setStatus(
        "current"
    )

alaIPv6InterfaceNeighborLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 0, 4)
)
alaIPv6InterfaceNeighborLimitExceeded.setObjects(
      *(("IPV6-MIB", "ipv6IfIndex"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceNeighborLimit"))
)
if mibBuilder.loadTexts:
    alaIPv6InterfaceNeighborLimitExceeded.setStatus(
        "current"
    )


# Notifications groups

alcatelIND1IPv6NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 2, 13)
)
alcatelIND1IPv6NotificationGroup.setObjects(
      *(("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborLimitExceeded"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborVRFLimitExceeded"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceNeighborLimitExceeded"))
)
if mibBuilder.loadTexts:
    alcatelIND1IPv6NotificationGroup.setStatus(
        "current"
    )

alcatelIND1IPv6DeprecatedNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 2, 15)
)
alcatelIND1IPv6DeprecatedNotificationGroup.setObjects(
    ("ALCATEL-ENT1-IPV6-MIB", "ndpMaxLimitReached")
)
if mibBuilder.loadTexts:
    alcatelIND1IPv6DeprecatedNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaIPv6Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 1, 2, 1, 1)
)
alaIPv6Compliance.setObjects(
      *(("ALCATEL-ENT1-IPV6-MIB", "alaIPv6TunnelConfigGroup"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6ConfigGroup"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6NeighborGroup"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceGroup"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceAddressGroup"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfaceEUI64AddressGroup"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6InterfacePrefixGroup"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6PMTUGroup"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6RouteFlagsGroup"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6LocalUnicastGroup"),
        ("ALCATEL-ENT1-IPV6-MIB", "alaIPv6RAFilterGroup"))
)
if mibBuilder.loadTexts:
    alaIPv6Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-IPV6-MIB",
    **{"AlaIPv6AddressPrefix": AlaIPv6AddressPrefix,
       "AlaIPv6RAFilterTrustedSourceType": AlaIPv6RAFilterTrustedSourceType,
       "AlaIPv6RAFilterTrustedSourceValue": AlaIPv6RAFilterTrustedSourceValue,
       "AlaIPv6RAFilterTrustedSourceIfIndex": AlaIPv6RAFilterTrustedSourceIfIndex,
       "alcatelIND1IPv6MIB": alcatelIND1IPv6MIB,
       "alcatelIND1IPv6MIBNotifications": alcatelIND1IPv6MIBNotifications,
       "ndpMaxLimitReached": ndpMaxLimitReached,
       "alaIPv6NeighborLimitExceeded": alaIPv6NeighborLimitExceeded,
       "alaIPv6NeighborVRFLimitExceeded": alaIPv6NeighborVRFLimitExceeded,
       "alaIPv6InterfaceNeighborLimitExceeded": alaIPv6InterfaceNeighborLimitExceeded,
       "alcatelIND1IPv6MIBObjects": alcatelIND1IPv6MIBObjects,
       "alaIPv6Config": alaIPv6Config,
       "alaIPv6ClearNeighbors": alaIPv6ClearNeighbors,
       "alaIPv6ClearTraffic": alaIPv6ClearTraffic,
       "alaIPv6ClearPMTUTable": alaIPv6ClearPMTUTable,
       "alaIPv6PMTUMinLifetime": alaIPv6PMTUMinLifetime,
       "alaIPv6NeighborStaleLifetime": alaIPv6NeighborStaleLifetime,
       "alaIPv6GlobalID": alaIPv6GlobalID,
       "alaIPv6VirtualSourceMAC": alaIPv6VirtualSourceMAC,
       "alaIPv6NeighborLimit": alaIPv6NeighborLimit,
       "alaIPv6NeighborVRFLimit": alaIPv6NeighborVRFLimit,
       "alaIPv6InterfaceTable": alaIPv6InterfaceTable,
       "alaIPv6InterfaceEntry": alaIPv6InterfaceEntry,
       "alaIPv6InterfaceRowStatus": alaIPv6InterfaceRowStatus,
       "alaIPv6InterfaceDescription": alaIPv6InterfaceDescription,
       "alaIPv6InterfaceMtu": alaIPv6InterfaceMtu,
       "alaIPv6InterfaceType": alaIPv6InterfaceType,
       "alaIPv6InterfaceAdminStatus": alaIPv6InterfaceAdminStatus,
       "alaIPv6InterfaceSendRouterAdvertisements": alaIPv6InterfaceSendRouterAdvertisements,
       "alaIPv6InterfaceMaxRtrAdvInterval": alaIPv6InterfaceMaxRtrAdvInterval,
       "alaIPv6InterfaceAdvManagedFlag": alaIPv6InterfaceAdvManagedFlag,
       "alaIPv6InterfaceAdvOtherConfigFlag": alaIPv6InterfaceAdvOtherConfigFlag,
       "alaIPv6InterfaceAdvReachableTime": alaIPv6InterfaceAdvReachableTime,
       "alaIPv6InterfaceAdvRetransTimer": alaIPv6InterfaceAdvRetransTimer,
       "alaIPv6InterfaceAdvDefaultLifetime": alaIPv6InterfaceAdvDefaultLifetime,
       "alaIPv6InterfaceName": alaIPv6InterfaceName,
       "alaIPv6InterfaceAdvSendMtu": alaIPv6InterfaceAdvSendMtu,
       "alaIPv6InterfaceReachableTime": alaIPv6InterfaceReachableTime,
       "alaIPv6InterfaceBaseReachableTime": alaIPv6InterfaceBaseReachableTime,
       "alaIPv6InterfaceMinRtrAdvInterval": alaIPv6InterfaceMinRtrAdvInterval,
       "alaIPv6InterfaceClockSkew": alaIPv6InterfaceClockSkew,
       "alaIPv6InterfaceRetransTimer": alaIPv6InterfaceRetransTimer,
       "alaIPv6InterfaceDADTransmits": alaIPv6InterfaceDADTransmits,
       "alaIPv6InterfaceAdvHopLimit": alaIPv6InterfaceAdvHopLimit,
       "alaIPv6InterfaceLPND": alaIPv6InterfaceLPND,
       "alaIPv6InterfaceRAFilter": alaIPv6InterfaceRAFilter,
       "alaIPv6InterfaceNeighborLimit": alaIPv6InterfaceNeighborLimit,
       "alaIPv6InterfaceRetransBackoff": alaIPv6InterfaceRetransBackoff,
       "alaIPv6InterfaceRetransMax": alaIPv6InterfaceRetransMax,
       "alaIPv6InterfaceRouterPreference": alaIPv6InterfaceRouterPreference,
       "alaIPv6TunnelConfig": alaIPv6TunnelConfig,
       "alaIPv6ConfigTunnelTable": alaIPv6ConfigTunnelTable,
       "alaIPv6ConfigTunnelEntry": alaIPv6ConfigTunnelEntry,
       "alaIPv6ConfigTunnelV4Source": alaIPv6ConfigTunnelV4Source,
       "alaIPv6ConfigTunnelV4Dest": alaIPv6ConfigTunnelV4Dest,
       "alaIPv6InterfaceAddressTable": alaIPv6InterfaceAddressTable,
       "alaIPv6InterfaceAddressEntry": alaIPv6InterfaceAddressEntry,
       "alaIPv6InterfaceAddressRowStatus": alaIPv6InterfaceAddressRowStatus,
       "alaIPv6InterfaceAddress": alaIPv6InterfaceAddress,
       "alaIPv6InterfaceAddressPrefixLength": alaIPv6InterfaceAddressPrefixLength,
       "alaIPv6InterfaceAddressAnycastFlag": alaIPv6InterfaceAddressAnycastFlag,
       "alaIPv6InterfaceAddressDADStatus": alaIPv6InterfaceAddressDADStatus,
       "alaIPv6InterfaceEUI64AddressTable": alaIPv6InterfaceEUI64AddressTable,
       "alaIPv6InterfaceEUI64AddressEntry": alaIPv6InterfaceEUI64AddressEntry,
       "alaIPv6InterfaceEUI64AddressRowStatus": alaIPv6InterfaceEUI64AddressRowStatus,
       "alaIPv6InterfaceEUI64AddressPrefix": alaIPv6InterfaceEUI64AddressPrefix,
       "alaIPv6InterfaceEUI64AddressPrefixLength": alaIPv6InterfaceEUI64AddressPrefixLength,
       "alaIPv6InterfaceEUI64AddressIdentifier": alaIPv6InterfaceEUI64AddressIdentifier,
       "alaIPv6NeighborTable": alaIPv6NeighborTable,
       "alaIPv6NeighborEntry": alaIPv6NeighborEntry,
       "alaIPv6NeighborNetAddress": alaIPv6NeighborNetAddress,
       "alaIPv6NeighborPhysAddress": alaIPv6NeighborPhysAddress,
       "alaIPv6NeighborSlot": alaIPv6NeighborSlot,
       "alaIPv6NeighborPort": alaIPv6NeighborPort,
       "alaIPv6NeighborType": alaIPv6NeighborType,
       "alaIPv6NeighborState": alaIPv6NeighborState,
       "alaIPv6NeighborLastUpdated": alaIPv6NeighborLastUpdated,
       "alaIPv6NeighborRowStatus": alaIPv6NeighborRowStatus,
       "alaIPv6NeighborLifetime": alaIPv6NeighborLifetime,
       "alaIPv6NeighborReachability": alaIPv6NeighborReachability,
       "alaIPv6NeighborChassis": alaIPv6NeighborChassis,
       "alaIPv6NeighborPortIfIndex": alaIPv6NeighborPortIfIndex,
       "alaIPv6StaticRouteTable": alaIPv6StaticRouteTable,
       "alaIPv6StaticRouteEntry": alaIPv6StaticRouteEntry,
       "alaIPv6StaticRouteDest": alaIPv6StaticRouteDest,
       "alaIPv6StaticRoutePfxLength": alaIPv6StaticRoutePfxLength,
       "alaIPv6StaticRouteIfIndex": alaIPv6StaticRouteIfIndex,
       "alaIPv6StaticRouteNextHop": alaIPv6StaticRouteNextHop,
       "alaIPv6StaticRouteMetric": alaIPv6StaticRouteMetric,
       "alaIPv6StaticRouteRowStatus": alaIPv6StaticRouteRowStatus,
       "alaIPv6HostTable": alaIPv6HostTable,
       "alaIPv6HostEntry": alaIPv6HostEntry,
       "alaIPv6HostName": alaIPv6HostName,
       "alaIPv6HostAddress": alaIPv6HostAddress,
       "alaIPv6HostRowStatus": alaIPv6HostRowStatus,
       "alaIPv6InterfacePrefixTable": alaIPv6InterfacePrefixTable,
       "alaIPv6InterfacePrefixEntry": alaIPv6InterfacePrefixEntry,
       "alaIPv6InterfacePrefixRowStatus": alaIPv6InterfacePrefixRowStatus,
       "alaIPv6InterfacePrefix": alaIPv6InterfacePrefix,
       "alaIPv6InterfacePrefixLength": alaIPv6InterfacePrefixLength,
       "alaIPv6InterfacePrefixValidLifetime": alaIPv6InterfacePrefixValidLifetime,
       "alaIPv6InterfacePrefixOnLinkFlag": alaIPv6InterfacePrefixOnLinkFlag,
       "alaIPv6InterfacePrefixPreferredLifetime": alaIPv6InterfacePrefixPreferredLifetime,
       "alaIPv6InterfacePrefixAutonomousFlag": alaIPv6InterfacePrefixAutonomousFlag,
       "alaIPv6InterfacePrefixSource": alaIPv6InterfacePrefixSource,
       "alaIPv6InterfacePrefixValidLifetimeDecrement": alaIPv6InterfacePrefixValidLifetimeDecrement,
       "alaIPv6InterfacePrefixValidLifetimeExpire": alaIPv6InterfacePrefixValidLifetimeExpire,
       "alaIPv6InterfacePrefixPreferredLifetimeDecrement": alaIPv6InterfacePrefixPreferredLifetimeDecrement,
       "alaIPv6InterfacePrefixPreferredLifetimeExpire": alaIPv6InterfacePrefixPreferredLifetimeExpire,
       "alaIPv6PMTUTable": alaIPv6PMTUTable,
       "alaIPv6PMTUEntry": alaIPv6PMTUEntry,
       "alaIPv6PMTUDest": alaIPv6PMTUDest,
       "alaIPv6PMTU": alaIPv6PMTU,
       "alaIPv6PMTUExpire": alaIPv6PMTUExpire,
       "alaIPv6PMTUHits": alaIPv6PMTUHits,
       "alaIPv6PMTUUpdates": alaIPv6PMTUUpdates,
       "alaIPv6RouteFlagsTable": alaIPv6RouteFlagsTable,
       "alaIPv6RouteFlagsEntry": alaIPv6RouteFlagsEntry,
       "alaIPv6RouteFlagsUp": alaIPv6RouteFlagsUp,
       "alaIPv6RouteFlagsGateway": alaIPv6RouteFlagsGateway,
       "alaIPv6RouteFlagsHost": alaIPv6RouteFlagsHost,
       "alaIPv6RouteFlagsStatic": alaIPv6RouteFlagsStatic,
       "alaIPv6RouteFlagsCloneable": alaIPv6RouteFlagsCloneable,
       "alaIPv6RouteFlagsDiscard": alaIPv6RouteFlagsDiscard,
       "alaIPv6RouteFlagsECMP": alaIPv6RouteFlagsECMP,
       "alaIPv6RouteFlagsTransient": alaIPv6RouteFlagsTransient,
       "alaIPv6LocalUnicastTable": alaIPv6LocalUnicastTable,
       "alaIPv6LocalUnicastEntry": alaIPv6LocalUnicastEntry,
       "alaIPv6LocalUnicastGlobalID": alaIPv6LocalUnicastGlobalID,
       "alaIPv6LocalUnicastSubnetID": alaIPv6LocalUnicastSubnetID,
       "alaIPv6LocalUnicastInterfaceID": alaIPv6LocalUnicastInterfaceID,
       "alaIPv6LocalUnicastPrefixLength": alaIPv6LocalUnicastPrefixLength,
       "alaIPv6LocalUnicastEUI64": alaIPv6LocalUnicastEUI64,
       "alaIPv6LocalUnicastRowStatus": alaIPv6LocalUnicastRowStatus,
       "alaIPv6RAFilterTrustedPortTable": alaIPv6RAFilterTrustedPortTable,
       "alaIPv6RAFilterTrustedPortEntry": alaIPv6RAFilterTrustedPortEntry,
       "alaIPv6RAFilterTrustedPortIfIndex": alaIPv6RAFilterTrustedPortIfIndex,
       "alaIPv6RAFilterTrustedPortRowStatus": alaIPv6RAFilterTrustedPortRowStatus,
       "alaIPv6RAFilterInterfaceTable": alaIPv6RAFilterInterfaceTable,
       "alaIPv6RAFilterInterfaceEntry": alaIPv6RAFilterInterfaceEntry,
       "alaIPv6RAFilterInterfaceVlan": alaIPv6RAFilterInterfaceVlan,
       "alaIPv6RAFilterInterfaceAdminStatus": alaIPv6RAFilterInterfaceAdminStatus,
       "alaIPv6RAFilterInterfaceRowStatus": alaIPv6RAFilterInterfaceRowStatus,
       "alaIPv6RAFilterTrustedSourceTable": alaIPv6RAFilterTrustedSourceTable,
       "alaIPv6RAFilterTrustedSourceEntry": alaIPv6RAFilterTrustedSourceEntry,
       "alaIPv6RAFilterTrustedSourceType": alaIPv6RAFilterTrustedSourceType,
       "alaIPv6RAFilterTrustedSourceValue": alaIPv6RAFilterTrustedSourceValue,
       "alaIPv6RAFilterTrustedSourceRowStatus": alaIPv6RAFilterTrustedSourceRowStatus,
       "alcatelIND1IPv6MIBConformance": alcatelIND1IPv6MIBConformance,
       "alcatelIND1IPv6MIBCompliances": alcatelIND1IPv6MIBCompliances,
       "alaIPv6Compliance": alaIPv6Compliance,
       "alcatelIND1IPv6MIBGroups": alcatelIND1IPv6MIBGroups,
       "alaIPv6TunnelConfigGroup": alaIPv6TunnelConfigGroup,
       "alaIPv6ConfigGroup": alaIPv6ConfigGroup,
       "alaIPv6NeighborGroup": alaIPv6NeighborGroup,
       "alaIPv6StaticRouteGroup": alaIPv6StaticRouteGroup,
       "alaIPv6InterfaceGroup": alaIPv6InterfaceGroup,
       "alaIPv6InterfaceAddressGroup": alaIPv6InterfaceAddressGroup,
       "alaIPv6InterfaceEUI64AddressGroup": alaIPv6InterfaceEUI64AddressGroup,
       "alaIPv6InterfacePrefixGroup": alaIPv6InterfacePrefixGroup,
       "alaIPv6PMTUGroup": alaIPv6PMTUGroup,
       "alaIPv6RouteFlagsGroup": alaIPv6RouteFlagsGroup,
       "alaIPv6LocalUnicastGroup": alaIPv6LocalUnicastGroup,
       "alaIPv6HostGroup": alaIPv6HostGroup,
       "alcatelIND1IPv6NotificationGroup": alcatelIND1IPv6NotificationGroup,
       "alcatelIND1IPv6DeprecatedObjectGroup": alcatelIND1IPv6DeprecatedObjectGroup,
       "alcatelIND1IPv6DeprecatedNotificationGroup": alcatelIND1IPv6DeprecatedNotificationGroup,
       "alaIPv6RAFilterGroup": alaIPv6RAFilterGroup}
)
