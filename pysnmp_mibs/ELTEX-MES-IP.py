# SNMP MIB module (ELTEX-MES-IP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-IP
# Produced by pysmi-1.6.2 at Fri Oct 10 19:49:54 2025
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

(EltexBgpAsSize,
 EltexBgpOriginCode,
 EltexBgpRouteMapAsPathAction) = mibBuilder.importSymbols(
    "ELTEX-BGP-MIB",
    "EltexBgpAsSize",
    "EltexBgpOriginCode",
    "EltexBgpRouteMapAsPathAction")

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(inetCidrRouteEntry,) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "inetCidrRouteEntry")

(rlRouteMapPbrEntry,) = mibBuilder.importSymbols(
    "MARVELL-ROUTEMAP-MIB",
    "rlRouteMapPbrEntry")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(rlInetRoutingDistanceEntry,
 rlInetStaticRouteEntry) = mibBuilder.importSymbols(
    "RADLAN-IPv6",
    "rlInetRoutingDistanceEntry",
    "rlInetStaticRouteEntry")

(RlRedistDstProtocol,) = mibBuilder.importSymbols(
    "RADLAN-Redistribute",
    "RlRedistDstProtocol")

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

eltMesIpSpec = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91)
)
if mibBuilder.loadTexts:
    eltMesIpSpec.setRevisions(
        ("2006-06-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltMesRouteMapPermitOrDeny(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )



class EltInetCidrRouteInstallStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failure", 2))
    )



# MIB Managed Objects in the order of their OIDs

_EltMesOspf_ObjectIdentity = ObjectIdentity
eltMesOspf = _EltMesOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1)
)
_EltMesArpSpec_ObjectIdentity = ObjectIdentity
eltMesArpSpec = _EltMesArpSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 3)
)
_EltMesInetRouting_ObjectIdentity = ObjectIdentity
eltMesInetRouting = _EltMesInetRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4)
)
_EltInetRoutingDistanceTable_Object = MibTable
eltInetRoutingDistanceTable = _EltInetRoutingDistanceTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 1)
)
if mibBuilder.loadTexts:
    eltInetRoutingDistanceTable.setStatus("current")
_EltInetRoutingDistanceEntry_Object = MibTableRow
eltInetRoutingDistanceEntry = _EltInetRoutingDistanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 1, 1)
)
if mibBuilder.loadTexts:
    eltInetRoutingDistanceEntry.setStatus("current")


class _EltInetRoutingDistanceBgpInternal_Type(Integer32):
    """Custom type eltInetRoutingDistanceBgpInternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EltInetRoutingDistanceBgpInternal_Type.__name__ = "Integer32"
_EltInetRoutingDistanceBgpInternal_Object = MibTableColumn
eltInetRoutingDistanceBgpInternal = _EltInetRoutingDistanceBgpInternal_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 1, 1, 1),
    _EltInetRoutingDistanceBgpInternal_Type()
)
eltInetRoutingDistanceBgpInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltInetRoutingDistanceBgpInternal.setStatus("current")


class _EltInetRoutingDistanceBgpExternal_Type(Integer32):
    """Custom type eltInetRoutingDistanceBgpExternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EltInetRoutingDistanceBgpExternal_Type.__name__ = "Integer32"
_EltInetRoutingDistanceBgpExternal_Object = MibTableColumn
eltInetRoutingDistanceBgpExternal = _EltInetRoutingDistanceBgpExternal_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 1, 1, 2),
    _EltInetRoutingDistanceBgpExternal_Type()
)
eltInetRoutingDistanceBgpExternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltInetRoutingDistanceBgpExternal.setStatus("current")


class _EltInetRoutingDistanceIsisl1Internal_Type(Integer32):
    """Custom type eltInetRoutingDistanceIsisl1Internal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EltInetRoutingDistanceIsisl1Internal_Type.__name__ = "Integer32"
_EltInetRoutingDistanceIsisl1Internal_Object = MibTableColumn
eltInetRoutingDistanceIsisl1Internal = _EltInetRoutingDistanceIsisl1Internal_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 1, 1, 3),
    _EltInetRoutingDistanceIsisl1Internal_Type()
)
eltInetRoutingDistanceIsisl1Internal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltInetRoutingDistanceIsisl1Internal.setStatus("current")


class _EltInetRoutingDistanceIsisl2Internal_Type(Integer32):
    """Custom type eltInetRoutingDistanceIsisl2Internal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EltInetRoutingDistanceIsisl2Internal_Type.__name__ = "Integer32"
_EltInetRoutingDistanceIsisl2Internal_Object = MibTableColumn
eltInetRoutingDistanceIsisl2Internal = _EltInetRoutingDistanceIsisl2Internal_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 1, 1, 4),
    _EltInetRoutingDistanceIsisl2Internal_Type()
)
eltInetRoutingDistanceIsisl2Internal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltInetRoutingDistanceIsisl2Internal.setStatus("current")


class _EltInetRoutingDistanceIsisl1External_Type(Integer32):
    """Custom type eltInetRoutingDistanceIsisl1External based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EltInetRoutingDistanceIsisl1External_Type.__name__ = "Integer32"
_EltInetRoutingDistanceIsisl1External_Object = MibTableColumn
eltInetRoutingDistanceIsisl1External = _EltInetRoutingDistanceIsisl1External_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 1, 1, 5),
    _EltInetRoutingDistanceIsisl1External_Type()
)
eltInetRoutingDistanceIsisl1External.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltInetRoutingDistanceIsisl1External.setStatus("current")


class _EltInetRoutingDistanceIsisl2External_Type(Integer32):
    """Custom type eltInetRoutingDistanceIsisl2External based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EltInetRoutingDistanceIsisl2External_Type.__name__ = "Integer32"
_EltInetRoutingDistanceIsisl2External_Object = MibTableColumn
eltInetRoutingDistanceIsisl2External = _EltInetRoutingDistanceIsisl2External_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 1, 1, 6),
    _EltInetRoutingDistanceIsisl2External_Type()
)
eltInetRoutingDistanceIsisl2External.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltInetRoutingDistanceIsisl2External.setStatus("current")
_EltInetStaticRouteTable_Object = MibTable
eltInetStaticRouteTable = _EltInetStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 2)
)
if mibBuilder.loadTexts:
    eltInetStaticRouteTable.setStatus("current")
_EltInetStaticRouteEntry_Object = MibTableRow
eltInetStaticRouteEntry = _EltInetStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 2, 1)
)
if mibBuilder.loadTexts:
    eltInetStaticRouteEntry.setStatus("current")


class _EltInetStaticRouteName_Type(DisplayString):
    """Custom type eltInetStaticRouteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EltInetStaticRouteName_Type.__name__ = "DisplayString"
_EltInetStaticRouteName_Object = MibTableColumn
eltInetStaticRouteName = _EltInetStaticRouteName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 2, 1, 1),
    _EltInetStaticRouteName_Type()
)
eltInetStaticRouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltInetStaticRouteName.setStatus("current")
_EltInetSummAddrTable_Object = MibTable
eltInetSummAddrTable = _EltInetSummAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 3)
)
if mibBuilder.loadTexts:
    eltInetSummAddrTable.setStatus("current")
_EltInetSummAddrEntry_Object = MibTableRow
eltInetSummAddrEntry = _EltInetSummAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 3, 1)
)
eltInetSummAddrEntry.setIndexNames(
    (0, "ELTEX-MES-IP", "eltInetSummAddrTargetProtocol"),
    (0, "ELTEX-MES-IP", "eltInetSummAddrTargetInstance"),
    (0, "ELTEX-MES-IP", "eltInetSummAddrAddrType"),
    (0, "ELTEX-MES-IP", "eltInetSummAddrAddress"),
    (0, "ELTEX-MES-IP", "eltInetSummAddrAddrPfxLen"),
)
if mibBuilder.loadTexts:
    eltInetSummAddrEntry.setStatus("current")
_EltInetSummAddrTargetProtocol_Type = RlRedistDstProtocol
_EltInetSummAddrTargetProtocol_Object = MibTableColumn
eltInetSummAddrTargetProtocol = _EltInetSummAddrTargetProtocol_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 3, 1, 1),
    _EltInetSummAddrTargetProtocol_Type()
)
eltInetSummAddrTargetProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltInetSummAddrTargetProtocol.setStatus("current")
_EltInetSummAddrTargetInstance_Type = Unsigned32
_EltInetSummAddrTargetInstance_Object = MibTableColumn
eltInetSummAddrTargetInstance = _EltInetSummAddrTargetInstance_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 3, 1, 2),
    _EltInetSummAddrTargetInstance_Type()
)
eltInetSummAddrTargetInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltInetSummAddrTargetInstance.setStatus("current")
_EltInetSummAddrAddrType_Type = InetAddressType
_EltInetSummAddrAddrType_Object = MibTableColumn
eltInetSummAddrAddrType = _EltInetSummAddrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 3, 1, 3),
    _EltInetSummAddrAddrType_Type()
)
eltInetSummAddrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltInetSummAddrAddrType.setStatus("current")


class _EltInetSummAddrAddress_Type(InetAddress):
    """Custom type eltInetSummAddrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EltInetSummAddrAddress_Type.__name__ = "InetAddress"
_EltInetSummAddrAddress_Object = MibTableColumn
eltInetSummAddrAddress = _EltInetSummAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 3, 1, 4),
    _EltInetSummAddrAddress_Type()
)
eltInetSummAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltInetSummAddrAddress.setStatus("current")


class _EltInetSummAddrAddrPfxLen_Type(Unsigned32):
    """Custom type eltInetSummAddrAddrPfxLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_EltInetSummAddrAddrPfxLen_Type.__name__ = "Unsigned32"
_EltInetSummAddrAddrPfxLen_Object = MibTableColumn
eltInetSummAddrAddrPfxLen = _EltInetSummAddrAddrPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 3, 1, 5),
    _EltInetSummAddrAddrPfxLen_Type()
)
eltInetSummAddrAddrPfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltInetSummAddrAddrPfxLen.setStatus("current")
_EltInetSummAddrRowStatus_Type = RowStatus
_EltInetSummAddrRowStatus_Object = MibTableColumn
eltInetSummAddrRowStatus = _EltInetSummAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 3, 1, 6),
    _EltInetSummAddrRowStatus_Type()
)
eltInetSummAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltInetSummAddrRowStatus.setStatus("current")


class _EltInetSummAddrAdvertise_Type(TruthValue):
    """Custom type eltInetSummAddrAdvertise based on TruthValue"""
    defaultValue = 1


_EltInetSummAddrAdvertise_Type.__name__ = "TruthValue"
_EltInetSummAddrAdvertise_Object = MibTableColumn
eltInetSummAddrAdvertise = _EltInetSummAddrAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 3, 1, 7),
    _EltInetSummAddrAdvertise_Type()
)
eltInetSummAddrAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltInetSummAddrAdvertise.setStatus("current")
_EltInetCidrRouteTable_Object = MibTable
eltInetCidrRouteTable = _EltInetCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 4)
)
if mibBuilder.loadTexts:
    eltInetCidrRouteTable.setStatus("current")
_EltInetCidrRouteEntry_Object = MibTableRow
eltInetCidrRouteEntry = _EltInetCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 4, 1)
)
if mibBuilder.loadTexts:
    eltInetCidrRouteEntry.setStatus("current")
_EltInetCidrRouteInstallStatus_Type = EltInetCidrRouteInstallStatus
_EltInetCidrRouteInstallStatus_Object = MibTableColumn
eltInetCidrRouteInstallStatus = _EltInetCidrRouteInstallStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 4, 4, 1, 1),
    _EltInetCidrRouteInstallStatus_Type()
)
eltInetCidrRouteInstallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltInetCidrRouteInstallStatus.setStatus("current")
_EltMesRouteMap_ObjectIdentity = ObjectIdentity
eltMesRouteMap = _EltMesRouteMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5)
)
_EltMesRouteMapTable_Object = MibTable
eltMesRouteMapTable = _EltMesRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1)
)
if mibBuilder.loadTexts:
    eltMesRouteMapTable.setStatus("current")
_EltMesRouteMapEntry_Object = MibTableRow
eltMesRouteMapEntry = _EltMesRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesRouteMapEntry.setStatus("current")


class _EltMesRouteMapMatchAddrPrefixListName_Type(DisplayString):
    """Custom type eltMesRouteMapMatchAddrPrefixListName based on DisplayString"""
    defaultValue = OctetString("")


_EltMesRouteMapMatchAddrPrefixListName_Type.__name__ = "DisplayString"
_EltMesRouteMapMatchAddrPrefixListName_Object = MibTableColumn
eltMesRouteMapMatchAddrPrefixListName = _EltMesRouteMapMatchAddrPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 1),
    _EltMesRouteMapMatchAddrPrefixListName_Type()
)
eltMesRouteMapMatchAddrPrefixListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapMatchAddrPrefixListName.setStatus("current")


class _EltMesRouteMapMatchNextPrefixListName_Type(DisplayString):
    """Custom type eltMesRouteMapMatchNextPrefixListName based on DisplayString"""
    defaultValue = OctetString("")


_EltMesRouteMapMatchNextPrefixListName_Type.__name__ = "DisplayString"
_EltMesRouteMapMatchNextPrefixListName_Object = MibTableColumn
eltMesRouteMapMatchNextPrefixListName = _EltMesRouteMapMatchNextPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 2),
    _EltMesRouteMapMatchNextPrefixListName_Type()
)
eltMesRouteMapMatchNextPrefixListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapMatchNextPrefixListName.setStatus("current")


class _EltMesRouteMapMatchSourcePrefixListName_Type(DisplayString):
    """Custom type eltMesRouteMapMatchSourcePrefixListName based on DisplayString"""
    defaultValue = OctetString("")


_EltMesRouteMapMatchSourcePrefixListName_Type.__name__ = "DisplayString"
_EltMesRouteMapMatchSourcePrefixListName_Object = MibTableColumn
eltMesRouteMapMatchSourcePrefixListName = _EltMesRouteMapMatchSourcePrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 3),
    _EltMesRouteMapMatchSourcePrefixListName_Type()
)
eltMesRouteMapMatchSourcePrefixListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapMatchSourcePrefixListName.setStatus("current")


class _EltMesRouteMapMatchLocPref_Type(Unsigned32):
    """Custom type eltMesRouteMapMatchLocPref based on Unsigned32"""
    defaultValue = 0


_EltMesRouteMapMatchLocPref_Type.__name__ = "Unsigned32"
_EltMesRouteMapMatchLocPref_Object = MibTableColumn
eltMesRouteMapMatchLocPref = _EltMesRouteMapMatchLocPref_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 4),
    _EltMesRouteMapMatchLocPref_Type()
)
eltMesRouteMapMatchLocPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapMatchLocPref.setStatus("current")


class _EltMesRouteMapMatchLocPrefDef_Type(TruthValue):
    """Custom type eltMesRouteMapMatchLocPrefDef based on TruthValue"""
    defaultValue = 2


_EltMesRouteMapMatchLocPrefDef_Type.__name__ = "TruthValue"
_EltMesRouteMapMatchLocPrefDef_Object = MibTableColumn
eltMesRouteMapMatchLocPrefDef = _EltMesRouteMapMatchLocPrefDef_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 5),
    _EltMesRouteMapMatchLocPrefDef_Type()
)
eltMesRouteMapMatchLocPrefDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapMatchLocPrefDef.setStatus("current")


class _EltMesRouteMapMatchMed_Type(Unsigned32):
    """Custom type eltMesRouteMapMatchMed based on Unsigned32"""
    defaultValue = 0


_EltMesRouteMapMatchMed_Type.__name__ = "Unsigned32"
_EltMesRouteMapMatchMed_Object = MibTableColumn
eltMesRouteMapMatchMed = _EltMesRouteMapMatchMed_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 6),
    _EltMesRouteMapMatchMed_Type()
)
eltMesRouteMapMatchMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapMatchMed.setStatus("current")


class _EltMesRouteMapMatchMedDef_Type(TruthValue):
    """Custom type eltMesRouteMapMatchMedDef based on TruthValue"""
    defaultValue = 2


_EltMesRouteMapMatchMedDef_Type.__name__ = "TruthValue"
_EltMesRouteMapMatchMedDef_Object = MibTableColumn
eltMesRouteMapMatchMedDef = _EltMesRouteMapMatchMedDef_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 7),
    _EltMesRouteMapMatchMedDef_Type()
)
eltMesRouteMapMatchMedDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapMatchMedDef.setStatus("current")


class _EltMesRouteMapMatchOrigin_Type(EltexBgpOriginCode):
    """Custom type eltMesRouteMapMatchOrigin based on EltexBgpOriginCode"""
    defaultValue = 2


_EltMesRouteMapMatchOrigin_Type.__name__ = "EltexBgpOriginCode"
_EltMesRouteMapMatchOrigin_Object = MibTableColumn
eltMesRouteMapMatchOrigin = _EltMesRouteMapMatchOrigin_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 8),
    _EltMesRouteMapMatchOrigin_Type()
)
eltMesRouteMapMatchOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapMatchOrigin.setStatus("current")


class _EltMesRouteMapMatchOriginDef_Type(TruthValue):
    """Custom type eltMesRouteMapMatchOriginDef based on TruthValue"""
    defaultValue = 2


_EltMesRouteMapMatchOriginDef_Type.__name__ = "TruthValue"
_EltMesRouteMapMatchOriginDef_Object = MibTableColumn
eltMesRouteMapMatchOriginDef = _EltMesRouteMapMatchOriginDef_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 9),
    _EltMesRouteMapMatchOriginDef_Type()
)
eltMesRouteMapMatchOriginDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapMatchOriginDef.setStatus("current")


class _EltMesRouteMapMatchAnd_Type(TruthValue):
    """Custom type eltMesRouteMapMatchAnd based on TruthValue"""
    defaultValue = 2


_EltMesRouteMapMatchAnd_Type.__name__ = "TruthValue"
_EltMesRouteMapMatchAnd_Object = MibTableColumn
eltMesRouteMapMatchAnd = _EltMesRouteMapMatchAnd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 10),
    _EltMesRouteMapMatchAnd_Type()
)
eltMesRouteMapMatchAnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapMatchAnd.setStatus("current")


class _EltMesRouteMapActionAS_Type(Unsigned32):
    """Custom type eltMesRouteMapActionAS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EltMesRouteMapActionAS_Type.__name__ = "Unsigned32"
_EltMesRouteMapActionAS_Object = MibTableColumn
eltMesRouteMapActionAS = _EltMesRouteMapActionAS_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 11),
    _EltMesRouteMapActionAS_Type()
)
eltMesRouteMapActionAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapActionAS.setStatus("current")


class _EltMesRouteMapActionASOperation_Type(EltexBgpRouteMapAsPathAction):
    """Custom type eltMesRouteMapActionASOperation based on EltexBgpRouteMapAsPathAction"""
    defaultValue = 0


_EltMesRouteMapActionASOperation_Type.__name__ = "EltexBgpRouteMapAsPathAction"
_EltMesRouteMapActionASOperation_Object = MibTableColumn
eltMesRouteMapActionASOperation = _EltMesRouteMapActionASOperation_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 12),
    _EltMesRouteMapActionASOperation_Type()
)
eltMesRouteMapActionASOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapActionASOperation.setStatus("current")


class _EltMesRouteMapActionASLimUpper_Type(Unsigned32):
    """Custom type eltMesRouteMapActionASLimUpper based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EltMesRouteMapActionASLimUpper_Type.__name__ = "Unsigned32"
_EltMesRouteMapActionASLimUpper_Object = MibTableColumn
eltMesRouteMapActionASLimUpper = _EltMesRouteMapActionASLimUpper_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 13),
    _EltMesRouteMapActionASLimUpper_Type()
)
eltMesRouteMapActionASLimUpper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapActionASLimUpper.setStatus("current")


class _EltMesRouteMapActionASLimUpperDef_Type(TruthValue):
    """Custom type eltMesRouteMapActionASLimUpperDef based on TruthValue"""
    defaultValue = 2


_EltMesRouteMapActionASLimUpperDef_Type.__name__ = "TruthValue"
_EltMesRouteMapActionASLimUpperDef_Object = MibTableColumn
eltMesRouteMapActionASLimUpperDef = _EltMesRouteMapActionASLimUpperDef_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 14),
    _EltMesRouteMapActionASLimUpperDef_Type()
)
eltMesRouteMapActionASLimUpperDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapActionASLimUpperDef.setStatus("current")


class _EltMesRouteMapActionAsPrependCount_Type(Unsigned32):
    """Custom type eltMesRouteMapActionAsPrependCount based on Unsigned32"""
    defaultValue = 0


_EltMesRouteMapActionAsPrependCount_Type.__name__ = "Unsigned32"
_EltMesRouteMapActionAsPrependCount_Object = MibTableColumn
eltMesRouteMapActionAsPrependCount = _EltMesRouteMapActionAsPrependCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 15),
    _EltMesRouteMapActionAsPrependCount_Type()
)
eltMesRouteMapActionAsPrependCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapActionAsPrependCount.setStatus("current")


class _EltMesRouteMapActionAsPrependSize_Type(EltexBgpAsSize):
    """Custom type eltMesRouteMapActionAsPrependSize based on EltexBgpAsSize"""
    defaultValue = 2


_EltMesRouteMapActionAsPrependSize_Type.__name__ = "EltexBgpAsSize"
_EltMesRouteMapActionAsPrependSize_Object = MibTableColumn
eltMesRouteMapActionAsPrependSize = _EltMesRouteMapActionAsPrependSize_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 16),
    _EltMesRouteMapActionAsPrependSize_Type()
)
eltMesRouteMapActionAsPrependSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapActionAsPrependSize.setStatus("current")


class _EltMesRouteMapActionAsPrependAsVals_Type(OctetString):
    """Custom type eltMesRouteMapActionAsPrependAsVals based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltMesRouteMapActionAsPrependAsVals_Type.__name__ = "OctetString"
_EltMesRouteMapActionAsPrependAsVals_Object = MibTableColumn
eltMesRouteMapActionAsPrependAsVals = _EltMesRouteMapActionAsPrependAsVals_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 17),
    _EltMesRouteMapActionAsPrependAsVals_Type()
)
eltMesRouteMapActionAsPrependAsVals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapActionAsPrependAsVals.setStatus("current")


class _EltMesRouteMapActionAsRemove_Type(DisplayString):
    """Custom type eltMesRouteMapActionAsRemove based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EltMesRouteMapActionAsRemove_Type.__name__ = "DisplayString"
_EltMesRouteMapActionAsRemove_Object = MibTableColumn
eltMesRouteMapActionAsRemove = _EltMesRouteMapActionAsRemove_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 18),
    _EltMesRouteMapActionAsRemove_Type()
)
eltMesRouteMapActionAsRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapActionAsRemove.setStatus("current")


class _EltMesRouteMapActionLocPref_Type(Unsigned32):
    """Custom type eltMesRouteMapActionLocPref based on Unsigned32"""
    defaultValue = 0


_EltMesRouteMapActionLocPref_Type.__name__ = "Unsigned32"
_EltMesRouteMapActionLocPref_Object = MibTableColumn
eltMesRouteMapActionLocPref = _EltMesRouteMapActionLocPref_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 19),
    _EltMesRouteMapActionLocPref_Type()
)
eltMesRouteMapActionLocPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapActionLocPref.setStatus("current")


class _EltMesRouteMapActionLocPrefDef_Type(TruthValue):
    """Custom type eltMesRouteMapActionLocPrefDef based on TruthValue"""
    defaultValue = 2


_EltMesRouteMapActionLocPrefDef_Type.__name__ = "TruthValue"
_EltMesRouteMapActionLocPrefDef_Object = MibTableColumn
eltMesRouteMapActionLocPrefDef = _EltMesRouteMapActionLocPrefDef_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 20),
    _EltMesRouteMapActionLocPrefDef_Type()
)
eltMesRouteMapActionLocPrefDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapActionLocPrefDef.setStatus("current")


class _EltMesRouteMapActionMed_Type(Unsigned32):
    """Custom type eltMesRouteMapActionMed based on Unsigned32"""
    defaultValue = 0


_EltMesRouteMapActionMed_Type.__name__ = "Unsigned32"
_EltMesRouteMapActionMed_Object = MibTableColumn
eltMesRouteMapActionMed = _EltMesRouteMapActionMed_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 21),
    _EltMesRouteMapActionMed_Type()
)
eltMesRouteMapActionMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapActionMed.setStatus("current")


class _EltMesRouteMapActionMedDef_Type(TruthValue):
    """Custom type eltMesRouteMapActionMedDef based on TruthValue"""
    defaultValue = 2


_EltMesRouteMapActionMedDef_Type.__name__ = "TruthValue"
_EltMesRouteMapActionMedDef_Object = MibTableColumn
eltMesRouteMapActionMedDef = _EltMesRouteMapActionMedDef_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 22),
    _EltMesRouteMapActionMedDef_Type()
)
eltMesRouteMapActionMedDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapActionMedDef.setStatus("current")


class _EltMesRouteMapActionOrigin_Type(EltexBgpOriginCode):
    """Custom type eltMesRouteMapActionOrigin based on EltexBgpOriginCode"""
    defaultValue = 2


_EltMesRouteMapActionOrigin_Type.__name__ = "EltexBgpOriginCode"
_EltMesRouteMapActionOrigin_Object = MibTableColumn
eltMesRouteMapActionOrigin = _EltMesRouteMapActionOrigin_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 23),
    _EltMesRouteMapActionOrigin_Type()
)
eltMesRouteMapActionOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapActionOrigin.setStatus("current")


class _EltMesRouteMapActionOriginDef_Type(TruthValue):
    """Custom type eltMesRouteMapActionOriginDef based on TruthValue"""
    defaultValue = 2


_EltMesRouteMapActionOriginDef_Type.__name__ = "TruthValue"
_EltMesRouteMapActionOriginDef_Object = MibTableColumn
eltMesRouteMapActionOriginDef = _EltMesRouteMapActionOriginDef_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 24),
    _EltMesRouteMapActionOriginDef_Type()
)
eltMesRouteMapActionOriginDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapActionOriginDef.setStatus("current")


class _EltMesRouteMapActionWeight_Type(Unsigned32):
    """Custom type eltMesRouteMapActionWeight based on Unsigned32"""
    defaultValue = 0


_EltMesRouteMapActionWeight_Type.__name__ = "Unsigned32"
_EltMesRouteMapActionWeight_Object = MibTableColumn
eltMesRouteMapActionWeight = _EltMesRouteMapActionWeight_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 25),
    _EltMesRouteMapActionWeight_Type()
)
eltMesRouteMapActionWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapActionWeight.setStatus("current")


class _EltMesRouteMapActionWeightDef_Type(TruthValue):
    """Custom type eltMesRouteMapActionWeightDef based on TruthValue"""
    defaultValue = 2


_EltMesRouteMapActionWeightDef_Type.__name__ = "TruthValue"
_EltMesRouteMapActionWeightDef_Object = MibTableColumn
eltMesRouteMapActionWeightDef = _EltMesRouteMapActionWeightDef_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 26),
    _EltMesRouteMapActionWeightDef_Type()
)
eltMesRouteMapActionWeightDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapActionWeightDef.setStatus("current")


class _EltMesRouteMapActionNextHopPeer_Type(TruthValue):
    """Custom type eltMesRouteMapActionNextHopPeer based on TruthValue"""
    defaultValue = 2


_EltMesRouteMapActionNextHopPeer_Type.__name__ = "TruthValue"
_EltMesRouteMapActionNextHopPeer_Object = MibTableColumn
eltMesRouteMapActionNextHopPeer = _EltMesRouteMapActionNextHopPeer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 27),
    _EltMesRouteMapActionNextHopPeer_Type()
)
eltMesRouteMapActionNextHopPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapActionNextHopPeer.setStatus("current")


class _EltMesRouteMapType_Type(EltMesRouteMapPermitOrDeny):
    """Custom type eltMesRouteMapType based on EltMesRouteMapPermitOrDeny"""
    defaultValue = 1


_EltMesRouteMapType_Type.__name__ = "EltMesRouteMapPermitOrDeny"
_EltMesRouteMapType_Object = MibTableColumn
eltMesRouteMapType = _EltMesRouteMapType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 28),
    _EltMesRouteMapType_Type()
)
eltMesRouteMapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapType.setStatus("current")


class _EltMesRouteMapContinue_Type(Unsigned32):
    """Custom type eltMesRouteMapContinue based on Unsigned32"""
    defaultValue = 0


_EltMesRouteMapContinue_Type.__name__ = "Unsigned32"
_EltMesRouteMapContinue_Object = MibTableColumn
eltMesRouteMapContinue = _EltMesRouteMapContinue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 5, 1, 1, 29),
    _EltMesRouteMapContinue_Type()
)
eltMesRouteMapContinue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesRouteMapContinue.setStatus("current")
_EltMesIpMgmt_ObjectIdentity = ObjectIdentity
eltMesIpMgmt = _EltMesIpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 6)
)
_EltIpMgmtInterfaceTable_Object = MibTable
eltIpMgmtInterfaceTable = _EltIpMgmtInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 6, 1)
)
if mibBuilder.loadTexts:
    eltIpMgmtInterfaceTable.setStatus("current")
_EltIpMgmtInterfaceEntry_Object = MibTableRow
eltIpMgmtInterfaceEntry = _EltIpMgmtInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 6, 1, 1)
)
eltIpMgmtInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltIpMgmtInterfaceEntry.setStatus("current")
_EltIpMgmtInterfaceOuterVlanTag_Type = VlanId
_EltIpMgmtInterfaceOuterVlanTag_Object = MibTableColumn
eltIpMgmtInterfaceOuterVlanTag = _EltIpMgmtInterfaceOuterVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 6, 1, 1, 1),
    _EltIpMgmtInterfaceOuterVlanTag_Type()
)
eltIpMgmtInterfaceOuterVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpMgmtInterfaceOuterVlanTag.setStatus("current")
_EltIpMgmtInterfaceRowStatus_Type = RowStatus
_EltIpMgmtInterfaceRowStatus_Object = MibTableColumn
eltIpMgmtInterfaceRowStatus = _EltIpMgmtInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 6, 1, 1, 2),
    _EltIpMgmtInterfaceRowStatus_Type()
)
eltIpMgmtInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltIpMgmtInterfaceRowStatus.setStatus("current")
rlInetRoutingDistanceEntry.registerAugmentions(
    ("ELTEX-MES-IP",
     "eltInetRoutingDistanceEntry")
)
eltInetRoutingDistanceEntry.setIndexNames(*rlInetRoutingDistanceEntry.getIndexNames())
rlInetStaticRouteEntry.registerAugmentions(
    ("ELTEX-MES-IP",
     "eltInetStaticRouteEntry")
)
eltInetStaticRouteEntry.setIndexNames(*rlInetStaticRouteEntry.getIndexNames())
inetCidrRouteEntry.registerAugmentions(
    ("ELTEX-MES-IP",
     "eltInetCidrRouteEntry")
)
eltInetCidrRouteEntry.setIndexNames(*inetCidrRouteEntry.getIndexNames())
rlRouteMapPbrEntry.registerAugmentions(
    ("ELTEX-MES-IP",
     "eltMesRouteMapEntry")
)
eltMesRouteMapEntry.setIndexNames(*rlRouteMapPbrEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-IP",
    **{"EltMesRouteMapPermitOrDeny": EltMesRouteMapPermitOrDeny,
       "EltInetCidrRouteInstallStatus": EltInetCidrRouteInstallStatus,
       "eltMesIpSpec": eltMesIpSpec,
       "eltMesOspf": eltMesOspf,
       "eltMesArpSpec": eltMesArpSpec,
       "eltMesInetRouting": eltMesInetRouting,
       "eltInetRoutingDistanceTable": eltInetRoutingDistanceTable,
       "eltInetRoutingDistanceEntry": eltInetRoutingDistanceEntry,
       "eltInetRoutingDistanceBgpInternal": eltInetRoutingDistanceBgpInternal,
       "eltInetRoutingDistanceBgpExternal": eltInetRoutingDistanceBgpExternal,
       "eltInetRoutingDistanceIsisl1Internal": eltInetRoutingDistanceIsisl1Internal,
       "eltInetRoutingDistanceIsisl2Internal": eltInetRoutingDistanceIsisl2Internal,
       "eltInetRoutingDistanceIsisl1External": eltInetRoutingDistanceIsisl1External,
       "eltInetRoutingDistanceIsisl2External": eltInetRoutingDistanceIsisl2External,
       "eltInetStaticRouteTable": eltInetStaticRouteTable,
       "eltInetStaticRouteEntry": eltInetStaticRouteEntry,
       "eltInetStaticRouteName": eltInetStaticRouteName,
       "eltInetSummAddrTable": eltInetSummAddrTable,
       "eltInetSummAddrEntry": eltInetSummAddrEntry,
       "eltInetSummAddrTargetProtocol": eltInetSummAddrTargetProtocol,
       "eltInetSummAddrTargetInstance": eltInetSummAddrTargetInstance,
       "eltInetSummAddrAddrType": eltInetSummAddrAddrType,
       "eltInetSummAddrAddress": eltInetSummAddrAddress,
       "eltInetSummAddrAddrPfxLen": eltInetSummAddrAddrPfxLen,
       "eltInetSummAddrRowStatus": eltInetSummAddrRowStatus,
       "eltInetSummAddrAdvertise": eltInetSummAddrAdvertise,
       "eltInetCidrRouteTable": eltInetCidrRouteTable,
       "eltInetCidrRouteEntry": eltInetCidrRouteEntry,
       "eltInetCidrRouteInstallStatus": eltInetCidrRouteInstallStatus,
       "eltMesRouteMap": eltMesRouteMap,
       "eltMesRouteMapTable": eltMesRouteMapTable,
       "eltMesRouteMapEntry": eltMesRouteMapEntry,
       "eltMesRouteMapMatchAddrPrefixListName": eltMesRouteMapMatchAddrPrefixListName,
       "eltMesRouteMapMatchNextPrefixListName": eltMesRouteMapMatchNextPrefixListName,
       "eltMesRouteMapMatchSourcePrefixListName": eltMesRouteMapMatchSourcePrefixListName,
       "eltMesRouteMapMatchLocPref": eltMesRouteMapMatchLocPref,
       "eltMesRouteMapMatchLocPrefDef": eltMesRouteMapMatchLocPrefDef,
       "eltMesRouteMapMatchMed": eltMesRouteMapMatchMed,
       "eltMesRouteMapMatchMedDef": eltMesRouteMapMatchMedDef,
       "eltMesRouteMapMatchOrigin": eltMesRouteMapMatchOrigin,
       "eltMesRouteMapMatchOriginDef": eltMesRouteMapMatchOriginDef,
       "eltMesRouteMapMatchAnd": eltMesRouteMapMatchAnd,
       "eltMesRouteMapActionAS": eltMesRouteMapActionAS,
       "eltMesRouteMapActionASOperation": eltMesRouteMapActionASOperation,
       "eltMesRouteMapActionASLimUpper": eltMesRouteMapActionASLimUpper,
       "eltMesRouteMapActionASLimUpperDef": eltMesRouteMapActionASLimUpperDef,
       "eltMesRouteMapActionAsPrependCount": eltMesRouteMapActionAsPrependCount,
       "eltMesRouteMapActionAsPrependSize": eltMesRouteMapActionAsPrependSize,
       "eltMesRouteMapActionAsPrependAsVals": eltMesRouteMapActionAsPrependAsVals,
       "eltMesRouteMapActionAsRemove": eltMesRouteMapActionAsRemove,
       "eltMesRouteMapActionLocPref": eltMesRouteMapActionLocPref,
       "eltMesRouteMapActionLocPrefDef": eltMesRouteMapActionLocPrefDef,
       "eltMesRouteMapActionMed": eltMesRouteMapActionMed,
       "eltMesRouteMapActionMedDef": eltMesRouteMapActionMedDef,
       "eltMesRouteMapActionOrigin": eltMesRouteMapActionOrigin,
       "eltMesRouteMapActionOriginDef": eltMesRouteMapActionOriginDef,
       "eltMesRouteMapActionWeight": eltMesRouteMapActionWeight,
       "eltMesRouteMapActionWeightDef": eltMesRouteMapActionWeightDef,
       "eltMesRouteMapActionNextHopPeer": eltMesRouteMapActionNextHopPeer,
       "eltMesRouteMapType": eltMesRouteMapType,
       "eltMesRouteMapContinue": eltMesRouteMapContinue,
       "eltMesIpMgmt": eltMesIpMgmt,
       "eltIpMgmtInterfaceTable": eltIpMgmtInterfaceTable,
       "eltIpMgmtInterfaceEntry": eltIpMgmtInterfaceEntry,
       "eltIpMgmtInterfaceOuterVlanTag": eltIpMgmtInterfaceOuterVlanTag,
       "eltIpMgmtInterfaceRowStatus": eltIpMgmtInterfaceRowStatus}
)
