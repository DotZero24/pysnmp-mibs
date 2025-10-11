# SNMP MIB module (ELTEX-MES-eltBrgMulticast-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-eltBrgMulticast-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:49:07 2025
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

(eltMesMacMulticast,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMesMacMulticast")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

(rlIgmpMldSnoopVlanEntry,) = mibBuilder.importSymbols(
    "RADLAN-rlMacMulticast-MIB",
    "rlIgmpMldSnoopVlanEntry")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesMacMulticastFilter_ObjectIdentity = ObjectIdentity
eltMesMacMulticastFilter = _EltMesMacMulticastFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 1)
)
_EltMesMacMulticastFilterPerVlan_ObjectIdentity = ObjectIdentity
eltMesMacMulticastFilterPerVlan = _EltMesMacMulticastFilterPerVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 1, 1)
)


class _EltMacMulticastUnregFilterEnableVlanId1To1024_Type(OctetString):
    """Custom type eltMacMulticastUnregFilterEnableVlanId1To1024 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltMacMulticastUnregFilterEnableVlanId1To1024_Type.__name__ = "OctetString"
_EltMacMulticastUnregFilterEnableVlanId1To1024_Object = MibScalar
eltMacMulticastUnregFilterEnableVlanId1To1024 = _EltMacMulticastUnregFilterEnableVlanId1To1024_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 1, 1, 1),
    _EltMacMulticastUnregFilterEnableVlanId1To1024_Type()
)
eltMacMulticastUnregFilterEnableVlanId1To1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMacMulticastUnregFilterEnableVlanId1To1024.setStatus("current")


class _EltMacMulticastUnregFilterEnableVlanId1025To2048_Type(OctetString):
    """Custom type eltMacMulticastUnregFilterEnableVlanId1025To2048 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltMacMulticastUnregFilterEnableVlanId1025To2048_Type.__name__ = "OctetString"
_EltMacMulticastUnregFilterEnableVlanId1025To2048_Object = MibScalar
eltMacMulticastUnregFilterEnableVlanId1025To2048 = _EltMacMulticastUnregFilterEnableVlanId1025To2048_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 1, 1, 2),
    _EltMacMulticastUnregFilterEnableVlanId1025To2048_Type()
)
eltMacMulticastUnregFilterEnableVlanId1025To2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMacMulticastUnregFilterEnableVlanId1025To2048.setStatus("current")


class _EltMacMulticastUnregFilterEnableVlanId2049To3072_Type(OctetString):
    """Custom type eltMacMulticastUnregFilterEnableVlanId2049To3072 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltMacMulticastUnregFilterEnableVlanId2049To3072_Type.__name__ = "OctetString"
_EltMacMulticastUnregFilterEnableVlanId2049To3072_Object = MibScalar
eltMacMulticastUnregFilterEnableVlanId2049To3072 = _EltMacMulticastUnregFilterEnableVlanId2049To3072_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 1, 1, 3),
    _EltMacMulticastUnregFilterEnableVlanId2049To3072_Type()
)
eltMacMulticastUnregFilterEnableVlanId2049To3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMacMulticastUnregFilterEnableVlanId2049To3072.setStatus("current")


class _EltMacMulticastUnregFilterEnableVlanId3073To4094_Type(OctetString):
    """Custom type eltMacMulticastUnregFilterEnableVlanId3073To4094 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltMacMulticastUnregFilterEnableVlanId3073To4094_Type.__name__ = "OctetString"
_EltMacMulticastUnregFilterEnableVlanId3073To4094_Object = MibScalar
eltMacMulticastUnregFilterEnableVlanId3073To4094 = _EltMacMulticastUnregFilterEnableVlanId3073To4094_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 1, 1, 4),
    _EltMacMulticastUnregFilterEnableVlanId3073To4094_Type()
)
eltMacMulticastUnregFilterEnableVlanId3073To4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMacMulticastUnregFilterEnableVlanId3073To4094.setStatus("current")
_EltMesMldSnoop_ObjectIdentity = ObjectIdentity
eltMesMldSnoop = _EltMesMldSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 5)
)
_EltIgmpMldSnoopVlanTable_Object = MibTable
eltIgmpMldSnoopVlanTable = _EltIgmpMldSnoopVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 5, 5)
)
if mibBuilder.loadTexts:
    eltIgmpMldSnoopVlanTable.setStatus("current")
_EltIgmpMldSnoopVlanEntry_Object = MibTableRow
eltIgmpMldSnoopVlanEntry = _EltIgmpMldSnoopVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 5, 5, 1)
)
if mibBuilder.loadTexts:
    eltIgmpMldSnoopVlanEntry.setStatus("current")


class _EltIgmpMldSnoopVlanIsImmediateLeaveHostBased_Type(TruthValue):
    """Custom type eltIgmpMldSnoopVlanIsImmediateLeaveHostBased based on TruthValue"""
    defaultValue = 2


_EltIgmpMldSnoopVlanIsImmediateLeaveHostBased_Type.__name__ = "TruthValue"
_EltIgmpMldSnoopVlanIsImmediateLeaveHostBased_Object = MibTableColumn
eltIgmpMldSnoopVlanIsImmediateLeaveHostBased = _EltIgmpMldSnoopVlanIsImmediateLeaveHostBased_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 5, 5, 1, 1),
    _EltIgmpMldSnoopVlanIsImmediateLeaveHostBased_Type()
)
eltIgmpMldSnoopVlanIsImmediateLeaveHostBased.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIgmpMldSnoopVlanIsImmediateLeaveHostBased.setStatus("current")


class _EltIgmpMldSnoopVlanCos_Type(Integer32):
    """Custom type eltIgmpMldSnoopVlanCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_EltIgmpMldSnoopVlanCos_Type.__name__ = "Integer32"
_EltIgmpMldSnoopVlanCos_Object = MibTableColumn
eltIgmpMldSnoopVlanCos = _EltIgmpMldSnoopVlanCos_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 5, 5, 1, 2),
    _EltIgmpMldSnoopVlanCos_Type()
)
eltIgmpMldSnoopVlanCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIgmpMldSnoopVlanCos.setStatus("current")
_EltIgmpMldSnoopVlanReplaceSourceIp_Type = InetAddress
_EltIgmpMldSnoopVlanReplaceSourceIp_Object = MibTableColumn
eltIgmpMldSnoopVlanReplaceSourceIp = _EltIgmpMldSnoopVlanReplaceSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 5, 5, 1, 3),
    _EltIgmpMldSnoopVlanReplaceSourceIp_Type()
)
eltIgmpMldSnoopVlanReplaceSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIgmpMldSnoopVlanReplaceSourceIp.setStatus("current")


class _EltIgmpMldSnoopVlanProxyReportEnable_Type(TruthValue):
    """Custom type eltIgmpMldSnoopVlanProxyReportEnable based on TruthValue"""
    defaultValue = 2


_EltIgmpMldSnoopVlanProxyReportEnable_Type.__name__ = "TruthValue"
_EltIgmpMldSnoopVlanProxyReportEnable_Object = MibTableColumn
eltIgmpMldSnoopVlanProxyReportEnable = _EltIgmpMldSnoopVlanProxyReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 5, 5, 1, 4),
    _EltIgmpMldSnoopVlanProxyReportEnable_Type()
)
eltIgmpMldSnoopVlanProxyReportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIgmpMldSnoopVlanProxyReportEnable.setStatus("current")


class _EltIgmpMldSnoopVlanProxyReportVersion_Type(Integer32):
    """Custom type eltIgmpMldSnoopVlanProxyReportVersion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_EltIgmpMldSnoopVlanProxyReportVersion_Type.__name__ = "Integer32"
_EltIgmpMldSnoopVlanProxyReportVersion_Object = MibTableColumn
eltIgmpMldSnoopVlanProxyReportVersion = _EltIgmpMldSnoopVlanProxyReportVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 5, 5, 1, 5),
    _EltIgmpMldSnoopVlanProxyReportVersion_Type()
)
eltIgmpMldSnoopVlanProxyReportVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIgmpMldSnoopVlanProxyReportVersion.setStatus("current")


class _EltIgmpMldSnoopVlanGsqSuppress_Type(TruthValue):
    """Custom type eltIgmpMldSnoopVlanGsqSuppress based on TruthValue"""
    defaultValue = 2


_EltIgmpMldSnoopVlanGsqSuppress_Type.__name__ = "TruthValue"
_EltIgmpMldSnoopVlanGsqSuppress_Object = MibTableColumn
eltIgmpMldSnoopVlanGsqSuppress = _EltIgmpMldSnoopVlanGsqSuppress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 5, 5, 1, 6),
    _EltIgmpMldSnoopVlanGsqSuppress_Type()
)
eltIgmpMldSnoopVlanGsqSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIgmpMldSnoopVlanGsqSuppress.setStatus("current")
_EltIgmpMldSnoopVlanImmediateLeavePortlist_Type = PortList
_EltIgmpMldSnoopVlanImmediateLeavePortlist_Object = MibTableColumn
eltIgmpMldSnoopVlanImmediateLeavePortlist = _EltIgmpMldSnoopVlanImmediateLeavePortlist_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 5, 5, 1, 7),
    _EltIgmpMldSnoopVlanImmediateLeavePortlist_Type()
)
eltIgmpMldSnoopVlanImmediateLeavePortlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIgmpMldSnoopVlanImmediateLeavePortlist.setStatus("current")
_EltIgmpMldSnoopVlanHostBasedPortlist_Type = PortList
_EltIgmpMldSnoopVlanHostBasedPortlist_Object = MibTableColumn
eltIgmpMldSnoopVlanHostBasedPortlist = _EltIgmpMldSnoopVlanHostBasedPortlist_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 5, 5, 1, 8),
    _EltIgmpMldSnoopVlanHostBasedPortlist_Type()
)
eltIgmpMldSnoopVlanHostBasedPortlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIgmpMldSnoopVlanHostBasedPortlist.setStatus("current")
_EltMesPimSnoop_ObjectIdentity = ObjectIdentity
eltMesPimSnoop = _EltMesPimSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6)
)
_EltMesPimSnoopObjects_ObjectIdentity = ObjectIdentity
eltMesPimSnoopObjects = _EltMesPimSnoopObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1)
)
_EltMesPimSnoopGlobals_ObjectIdentity = ObjectIdentity
eltMesPimSnoopGlobals = _EltMesPimSnoopGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 1)
)


class _EltPimSnoopEnable_Type(TruthValue):
    """Custom type eltPimSnoopEnable based on TruthValue"""
    defaultValue = 2


_EltPimSnoopEnable_Type.__name__ = "TruthValue"
_EltPimSnoopEnable_Object = MibScalar
eltPimSnoopEnable = _EltPimSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 1, 1),
    _EltPimSnoopEnable_Type()
)
eltPimSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPimSnoopEnable.setStatus("current")
_EltMesPimSnoopConfigs_ObjectIdentity = ObjectIdentity
eltMesPimSnoopConfigs = _EltMesPimSnoopConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 2)
)
_EltPimSnoopVlanConfigTable_Object = MibTable
eltPimSnoopVlanConfigTable = _EltPimSnoopVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltPimSnoopVlanConfigTable.setStatus("current")
_EltPimSnoopVlanConfigEntry_Object = MibTableRow
eltPimSnoopVlanConfigEntry = _EltPimSnoopVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 2, 1, 1)
)
eltPimSnoopVlanConfigEntry.setIndexNames(
    (0, "ELTEX-MES-eltBrgMulticast-MIB", "eltPimSnoopVlanConfigVlanTag"),
)
if mibBuilder.loadTexts:
    eltPimSnoopVlanConfigEntry.setStatus("current")
_EltPimSnoopVlanConfigVlanTag_Type = VlanIndex
_EltPimSnoopVlanConfigVlanTag_Object = MibTableColumn
eltPimSnoopVlanConfigVlanTag = _EltPimSnoopVlanConfigVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 2, 1, 1, 1),
    _EltPimSnoopVlanConfigVlanTag_Type()
)
eltPimSnoopVlanConfigVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopVlanConfigVlanTag.setStatus("current")


class _EltPimSnoopVlanConfigEnable_Type(TruthValue):
    """Custom type eltPimSnoopVlanConfigEnable based on TruthValue"""
    defaultValue = 2


_EltPimSnoopVlanConfigEnable_Type.__name__ = "TruthValue"
_EltPimSnoopVlanConfigEnable_Object = MibTableColumn
eltPimSnoopVlanConfigEnable = _EltPimSnoopVlanConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 2, 1, 1, 2),
    _EltPimSnoopVlanConfigEnable_Type()
)
eltPimSnoopVlanConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPimSnoopVlanConfigEnable.setStatus("current")
_EltMesPimSnoopStatictics_ObjectIdentity = ObjectIdentity
eltMesPimSnoopStatictics = _EltMesPimSnoopStatictics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3)
)
_EltPimSnoopMembershipTable_Object = MibTable
eltPimSnoopMembershipTable = _EltPimSnoopMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltPimSnoopMembershipTable.setStatus("current")
_EltPimSnoopMembershipEntry_Object = MibTableRow
eltPimSnoopMembershipEntry = _EltPimSnoopMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 1, 1)
)
eltPimSnoopMembershipEntry.setIndexNames(
    (0, "ELTEX-MES-eltBrgMulticast-MIB", "eltPimSnoopMembershipVlanTag"),
    (0, "ELTEX-MES-eltBrgMulticast-MIB", "eltPimSnoopMembershipGroupIpAddressType"),
    (0, "ELTEX-MES-eltBrgMulticast-MIB", "eltPimSnoopMembershipGroupIpAddress"),
    (0, "ELTEX-MES-eltBrgMulticast-MIB", "eltPimSnoopMembershipSourceIpAddressType"),
    (0, "ELTEX-MES-eltBrgMulticast-MIB", "eltPimSnoopMembershipSourceIpAddress"),
    (0, "ELTEX-MES-eltBrgMulticast-MIB", "eltPimSnoopMembershipOutgoingPort"),
)
if mibBuilder.loadTexts:
    eltPimSnoopMembershipEntry.setStatus("current")
_EltPimSnoopMembershipVlanTag_Type = VlanIndex
_EltPimSnoopMembershipVlanTag_Object = MibTableColumn
eltPimSnoopMembershipVlanTag = _EltPimSnoopMembershipVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 1, 1, 1),
    _EltPimSnoopMembershipVlanTag_Type()
)
eltPimSnoopMembershipVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopMembershipVlanTag.setStatus("current")
_EltPimSnoopMembershipGroupIpAddressType_Type = InetAddressType
_EltPimSnoopMembershipGroupIpAddressType_Object = MibTableColumn
eltPimSnoopMembershipGroupIpAddressType = _EltPimSnoopMembershipGroupIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 1, 1, 2),
    _EltPimSnoopMembershipGroupIpAddressType_Type()
)
eltPimSnoopMembershipGroupIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopMembershipGroupIpAddressType.setStatus("current")
_EltPimSnoopMembershipGroupIpAddress_Type = InetAddress
_EltPimSnoopMembershipGroupIpAddress_Object = MibTableColumn
eltPimSnoopMembershipGroupIpAddress = _EltPimSnoopMembershipGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 1, 1, 3),
    _EltPimSnoopMembershipGroupIpAddress_Type()
)
eltPimSnoopMembershipGroupIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopMembershipGroupIpAddress.setStatus("current")
_EltPimSnoopMembershipSourceIpAddressType_Type = InetAddressType
_EltPimSnoopMembershipSourceIpAddressType_Object = MibTableColumn
eltPimSnoopMembershipSourceIpAddressType = _EltPimSnoopMembershipSourceIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 1, 1, 4),
    _EltPimSnoopMembershipSourceIpAddressType_Type()
)
eltPimSnoopMembershipSourceIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopMembershipSourceIpAddressType.setStatus("current")
_EltPimSnoopMembershipSourceIpAddress_Type = InetAddress
_EltPimSnoopMembershipSourceIpAddress_Object = MibTableColumn
eltPimSnoopMembershipSourceIpAddress = _EltPimSnoopMembershipSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 1, 1, 5),
    _EltPimSnoopMembershipSourceIpAddress_Type()
)
eltPimSnoopMembershipSourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopMembershipSourceIpAddress.setStatus("current")
_EltPimSnoopMembershipOutgoingPort_Type = InterfaceIndex
_EltPimSnoopMembershipOutgoingPort_Object = MibTableColumn
eltPimSnoopMembershipOutgoingPort = _EltPimSnoopMembershipOutgoingPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 1, 1, 6),
    _EltPimSnoopMembershipOutgoingPort_Type()
)
eltPimSnoopMembershipOutgoingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopMembershipOutgoingPort.setStatus("current")
_EltPimSnoopMembershipExpiryTime_Type = Integer32
_EltPimSnoopMembershipExpiryTime_Object = MibTableColumn
eltPimSnoopMembershipExpiryTime = _EltPimSnoopMembershipExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 1, 1, 7),
    _EltPimSnoopMembershipExpiryTime_Type()
)
eltPimSnoopMembershipExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopMembershipExpiryTime.setStatus("current")
_EltPimSnoopNeighborTable_Object = MibTable
eltPimSnoopNeighborTable = _EltPimSnoopNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 2)
)
if mibBuilder.loadTexts:
    eltPimSnoopNeighborTable.setStatus("current")
_EltPimSnoopNeighborEntry_Object = MibTableRow
eltPimSnoopNeighborEntry = _EltPimSnoopNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 2, 1)
)
eltPimSnoopNeighborEntry.setIndexNames(
    (0, "ELTEX-MES-eltBrgMulticast-MIB", "eltPimSnoopNeighborVlanTag"),
    (0, "ELTEX-MES-eltBrgMulticast-MIB", "eltPimSnoopNeighborIpAddressType"),
    (0, "ELTEX-MES-eltBrgMulticast-MIB", "eltPimSnoopNeighborIpAddress"),
)
if mibBuilder.loadTexts:
    eltPimSnoopNeighborEntry.setStatus("current")
_EltPimSnoopNeighborVlanTag_Type = VlanIndex
_EltPimSnoopNeighborVlanTag_Object = MibTableColumn
eltPimSnoopNeighborVlanTag = _EltPimSnoopNeighborVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 2, 1, 1),
    _EltPimSnoopNeighborVlanTag_Type()
)
eltPimSnoopNeighborVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopNeighborVlanTag.setStatus("current")
_EltPimSnoopNeighborIpAddressType_Type = InetAddressType
_EltPimSnoopNeighborIpAddressType_Object = MibTableColumn
eltPimSnoopNeighborIpAddressType = _EltPimSnoopNeighborIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 2, 1, 2),
    _EltPimSnoopNeighborIpAddressType_Type()
)
eltPimSnoopNeighborIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopNeighborIpAddressType.setStatus("current")
_EltPimSnoopNeighborIpAddress_Type = InetAddress
_EltPimSnoopNeighborIpAddress_Object = MibTableColumn
eltPimSnoopNeighborIpAddress = _EltPimSnoopNeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 2, 1, 3),
    _EltPimSnoopNeighborIpAddress_Type()
)
eltPimSnoopNeighborIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopNeighborIpAddress.setStatus("current")
_EltPimSnoopNeighborPort_Type = InterfaceIndex
_EltPimSnoopNeighborPort_Object = MibTableColumn
eltPimSnoopNeighborPort = _EltPimSnoopNeighborPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 2, 1, 4),
    _EltPimSnoopNeighborPort_Type()
)
eltPimSnoopNeighborPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopNeighborPort.setStatus("current")
_EltPimSnoopNeighborDrPriority_Type = Integer32
_EltPimSnoopNeighborDrPriority_Object = MibTableColumn
eltPimSnoopNeighborDrPriority = _EltPimSnoopNeighborDrPriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 2, 1, 5),
    _EltPimSnoopNeighborDrPriority_Type()
)
eltPimSnoopNeighborDrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopNeighborDrPriority.setStatus("current")
_EltPimSnoopNeighborExpiryTime_Type = Integer32
_EltPimSnoopNeighborExpiryTime_Object = MibTableColumn
eltPimSnoopNeighborExpiryTime = _EltPimSnoopNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 2, 1, 6),
    _EltPimSnoopNeighborExpiryTime_Type()
)
eltPimSnoopNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopNeighborExpiryTime.setStatus("current")
_EltPimSnoopVlanStatisticTable_Object = MibTable
eltPimSnoopVlanStatisticTable = _EltPimSnoopVlanStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 3)
)
if mibBuilder.loadTexts:
    eltPimSnoopVlanStatisticTable.setStatus("current")
_EltPimSnoopVlanStatisticEntry_Object = MibTableRow
eltPimSnoopVlanStatisticEntry = _EltPimSnoopVlanStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 3, 1)
)
eltPimSnoopVlanStatisticEntry.setIndexNames(
    (0, "ELTEX-MES-eltBrgMulticast-MIB", "eltPimSnoopVlanStatisticVlanTag"),
)
if mibBuilder.loadTexts:
    eltPimSnoopVlanStatisticEntry.setStatus("current")
_EltPimSnoopVlanStatisticVlanTag_Type = VlanIndex
_EltPimSnoopVlanStatisticVlanTag_Object = MibTableColumn
eltPimSnoopVlanStatisticVlanTag = _EltPimSnoopVlanStatisticVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 3, 1, 1),
    _EltPimSnoopVlanStatisticVlanTag_Type()
)
eltPimSnoopVlanStatisticVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopVlanStatisticVlanTag.setStatus("current")
_EltPimSnoopVlanStatisticEnable_Type = TruthValue
_EltPimSnoopVlanStatisticEnable_Object = MibTableColumn
eltPimSnoopVlanStatisticEnable = _EltPimSnoopVlanStatisticEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 3, 1, 2),
    _EltPimSnoopVlanStatisticEnable_Type()
)
eltPimSnoopVlanStatisticEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopVlanStatisticEnable.setStatus("current")
_EltPimSnoopVlanStatisticRouterPortList_Type = PortList
_EltPimSnoopVlanStatisticRouterPortList_Object = MibTableColumn
eltPimSnoopVlanStatisticRouterPortList = _EltPimSnoopVlanStatisticRouterPortList_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 3, 1, 3),
    _EltPimSnoopVlanStatisticRouterPortList_Type()
)
eltPimSnoopVlanStatisticRouterPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopVlanStatisticRouterPortList.setStatus("current")
_EltPimSnoopVlanStatisticNeighborsCount_Type = Integer32
_EltPimSnoopVlanStatisticNeighborsCount_Object = MibTableColumn
eltPimSnoopVlanStatisticNeighborsCount = _EltPimSnoopVlanStatisticNeighborsCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 3, 1, 4),
    _EltPimSnoopVlanStatisticNeighborsCount_Type()
)
eltPimSnoopVlanStatisticNeighborsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopVlanStatisticNeighborsCount.setStatus("current")
_EltPimSnoopVlanStatisticGroupsCount_Type = Integer32
_EltPimSnoopVlanStatisticGroupsCount_Object = MibTableColumn
eltPimSnoopVlanStatisticGroupsCount = _EltPimSnoopVlanStatisticGroupsCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 3, 1, 5),
    _EltPimSnoopVlanStatisticGroupsCount_Type()
)
eltPimSnoopVlanStatisticGroupsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopVlanStatisticGroupsCount.setStatus("current")
_EltPimSnoopVlanStatisticJoinedCount_Type = Integer32
_EltPimSnoopVlanStatisticJoinedCount_Object = MibTableColumn
eltPimSnoopVlanStatisticJoinedCount = _EltPimSnoopVlanStatisticJoinedCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 3, 1, 6),
    _EltPimSnoopVlanStatisticJoinedCount_Type()
)
eltPimSnoopVlanStatisticJoinedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopVlanStatisticJoinedCount.setStatus("current")
_EltPimSnoopVlanStatisticPrunedCount_Type = Integer32
_EltPimSnoopVlanStatisticPrunedCount_Object = MibTableColumn
eltPimSnoopVlanStatisticPrunedCount = _EltPimSnoopVlanStatisticPrunedCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 3, 1, 7),
    _EltPimSnoopVlanStatisticPrunedCount_Type()
)
eltPimSnoopVlanStatisticPrunedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopVlanStatisticPrunedCount.setStatus("current")
_EltPimSnoopVlanStatisticHelloCount_Type = Integer32
_EltPimSnoopVlanStatisticHelloCount_Object = MibTableColumn
eltPimSnoopVlanStatisticHelloCount = _EltPimSnoopVlanStatisticHelloCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 1, 3, 3, 1, 8),
    _EltPimSnoopVlanStatisticHelloCount_Type()
)
eltPimSnoopVlanStatisticHelloCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPimSnoopVlanStatisticHelloCount.setStatus("current")
_EltMesPimSnoopNotifications_ObjectIdentity = ObjectIdentity
eltMesPimSnoopNotifications = _EltMesPimSnoopNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 2)
)
_EltMesPimSnoopNotificationsPrefix_ObjectIdentity = ObjectIdentity
eltMesPimSnoopNotificationsPrefix = _EltMesPimSnoopNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 2, 0)
)
_EltMesPimSnoopConformance_ObjectIdentity = ObjectIdentity
eltMesPimSnoopConformance = _EltMesPimSnoopConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 6, 3)
)
rlIgmpMldSnoopVlanEntry.registerAugmentions(
    ("ELTEX-MES-eltBrgMulticast-MIB",
     "eltIgmpMldSnoopVlanEntry")
)
eltIgmpMldSnoopVlanEntry.setIndexNames(*rlIgmpMldSnoopVlanEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-eltBrgMulticast-MIB",
    **{"eltMesMacMulticastFilter": eltMesMacMulticastFilter,
       "eltMesMacMulticastFilterPerVlan": eltMesMacMulticastFilterPerVlan,
       "eltMacMulticastUnregFilterEnableVlanId1To1024": eltMacMulticastUnregFilterEnableVlanId1To1024,
       "eltMacMulticastUnregFilterEnableVlanId1025To2048": eltMacMulticastUnregFilterEnableVlanId1025To2048,
       "eltMacMulticastUnregFilterEnableVlanId2049To3072": eltMacMulticastUnregFilterEnableVlanId2049To3072,
       "eltMacMulticastUnregFilterEnableVlanId3073To4094": eltMacMulticastUnregFilterEnableVlanId3073To4094,
       "eltMesMldSnoop": eltMesMldSnoop,
       "eltIgmpMldSnoopVlanTable": eltIgmpMldSnoopVlanTable,
       "eltIgmpMldSnoopVlanEntry": eltIgmpMldSnoopVlanEntry,
       "eltIgmpMldSnoopVlanIsImmediateLeaveHostBased": eltIgmpMldSnoopVlanIsImmediateLeaveHostBased,
       "eltIgmpMldSnoopVlanCos": eltIgmpMldSnoopVlanCos,
       "eltIgmpMldSnoopVlanReplaceSourceIp": eltIgmpMldSnoopVlanReplaceSourceIp,
       "eltIgmpMldSnoopVlanProxyReportEnable": eltIgmpMldSnoopVlanProxyReportEnable,
       "eltIgmpMldSnoopVlanProxyReportVersion": eltIgmpMldSnoopVlanProxyReportVersion,
       "eltIgmpMldSnoopVlanGsqSuppress": eltIgmpMldSnoopVlanGsqSuppress,
       "eltIgmpMldSnoopVlanImmediateLeavePortlist": eltIgmpMldSnoopVlanImmediateLeavePortlist,
       "eltIgmpMldSnoopVlanHostBasedPortlist": eltIgmpMldSnoopVlanHostBasedPortlist,
       "eltMesPimSnoop": eltMesPimSnoop,
       "eltMesPimSnoopObjects": eltMesPimSnoopObjects,
       "eltMesPimSnoopGlobals": eltMesPimSnoopGlobals,
       "eltPimSnoopEnable": eltPimSnoopEnable,
       "eltMesPimSnoopConfigs": eltMesPimSnoopConfigs,
       "eltPimSnoopVlanConfigTable": eltPimSnoopVlanConfigTable,
       "eltPimSnoopVlanConfigEntry": eltPimSnoopVlanConfigEntry,
       "eltPimSnoopVlanConfigVlanTag": eltPimSnoopVlanConfigVlanTag,
       "eltPimSnoopVlanConfigEnable": eltPimSnoopVlanConfigEnable,
       "eltMesPimSnoopStatictics": eltMesPimSnoopStatictics,
       "eltPimSnoopMembershipTable": eltPimSnoopMembershipTable,
       "eltPimSnoopMembershipEntry": eltPimSnoopMembershipEntry,
       "eltPimSnoopMembershipVlanTag": eltPimSnoopMembershipVlanTag,
       "eltPimSnoopMembershipGroupIpAddressType": eltPimSnoopMembershipGroupIpAddressType,
       "eltPimSnoopMembershipGroupIpAddress": eltPimSnoopMembershipGroupIpAddress,
       "eltPimSnoopMembershipSourceIpAddressType": eltPimSnoopMembershipSourceIpAddressType,
       "eltPimSnoopMembershipSourceIpAddress": eltPimSnoopMembershipSourceIpAddress,
       "eltPimSnoopMembershipOutgoingPort": eltPimSnoopMembershipOutgoingPort,
       "eltPimSnoopMembershipExpiryTime": eltPimSnoopMembershipExpiryTime,
       "eltPimSnoopNeighborTable": eltPimSnoopNeighborTable,
       "eltPimSnoopNeighborEntry": eltPimSnoopNeighborEntry,
       "eltPimSnoopNeighborVlanTag": eltPimSnoopNeighborVlanTag,
       "eltPimSnoopNeighborIpAddressType": eltPimSnoopNeighborIpAddressType,
       "eltPimSnoopNeighborIpAddress": eltPimSnoopNeighborIpAddress,
       "eltPimSnoopNeighborPort": eltPimSnoopNeighborPort,
       "eltPimSnoopNeighborDrPriority": eltPimSnoopNeighborDrPriority,
       "eltPimSnoopNeighborExpiryTime": eltPimSnoopNeighborExpiryTime,
       "eltPimSnoopVlanStatisticTable": eltPimSnoopVlanStatisticTable,
       "eltPimSnoopVlanStatisticEntry": eltPimSnoopVlanStatisticEntry,
       "eltPimSnoopVlanStatisticVlanTag": eltPimSnoopVlanStatisticVlanTag,
       "eltPimSnoopVlanStatisticEnable": eltPimSnoopVlanStatisticEnable,
       "eltPimSnoopVlanStatisticRouterPortList": eltPimSnoopVlanStatisticRouterPortList,
       "eltPimSnoopVlanStatisticNeighborsCount": eltPimSnoopVlanStatisticNeighborsCount,
       "eltPimSnoopVlanStatisticGroupsCount": eltPimSnoopVlanStatisticGroupsCount,
       "eltPimSnoopVlanStatisticJoinedCount": eltPimSnoopVlanStatisticJoinedCount,
       "eltPimSnoopVlanStatisticPrunedCount": eltPimSnoopVlanStatisticPrunedCount,
       "eltPimSnoopVlanStatisticHelloCount": eltPimSnoopVlanStatisticHelloCount,
       "eltMesPimSnoopNotifications": eltMesPimSnoopNotifications,
       "eltMesPimSnoopNotificationsPrefix": eltMesPimSnoopNotificationsPrefix,
       "eltMesPimSnoopConformance": eltMesPimSnoopConformance}
)
