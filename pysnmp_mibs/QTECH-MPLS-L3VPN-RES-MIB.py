# SNMP MIB module (QTECH-MPLS-L3VPN-RES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-MPLS-L3VPN-RES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:11 2025
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

(bgp4PathAttrIpAddrPrefix,
 bgp4PathAttrIpAddrPrefixLen,
 bgp4PathAttrPeer) = mibBuilder.importSymbols(
    "BGP4-MIB",
    "bgp4PathAttrIpAddrPrefix",
    "bgp4PathAttrIpAddrPrefixLen",
    "bgp4PathAttrPeer")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(mplsL3VpnVrfName,) = mibBuilder.importSymbols(
    "MPLS-L3VPN-STD-MIB",
    "mplsL3VpnVrfName")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

qtechmplsL3VpnResMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 123)
)
if mibBuilder.loadTexts:
    qtechmplsL3VpnResMIB.setRevisions(
        ("2013-02-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechmplsL3VpnResMIBObjects_ObjectIdentity = ObjectIdentity
qtechmplsL3VpnResMIBObjects = _QtechmplsL3VpnResMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 123, 1)
)
_QtechmplsL3VpnResTable_Object = MibTable
qtechmplsL3VpnResTable = _QtechmplsL3VpnResTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 123, 1, 1)
)
if mibBuilder.loadTexts:
    qtechmplsL3VpnResTable.setStatus("current")
_QtechmplsL3VpnResEntry_Object = MibTableRow
qtechmplsL3VpnResEntry = _QtechmplsL3VpnResEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 123, 1, 1, 1)
)
qtechmplsL3VpnResEntry.setIndexNames(
    (0, "QTECH-MPLS-L3VPN-RES-MIB", "qtechmplsL3VpnResPeAddr"),
    (0, "QTECH-MPLS-L3VPN-RES-MIB", "qtechmplsL3VpnResVrfName"),
)
if mibBuilder.loadTexts:
    qtechmplsL3VpnResEntry.setStatus("current")
_QtechmplsL3VpnResPeAddr_Type = InetAddress
_QtechmplsL3VpnResPeAddr_Object = MibTableColumn
qtechmplsL3VpnResPeAddr = _QtechmplsL3VpnResPeAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 123, 1, 1, 1, 1),
    _QtechmplsL3VpnResPeAddr_Type()
)
qtechmplsL3VpnResPeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnResPeAddr.setStatus("current")
_QtechmplsL3VpnResVrfName_Type = DisplayString
_QtechmplsL3VpnResVrfName_Object = MibTableColumn
qtechmplsL3VpnResVrfName = _QtechmplsL3VpnResVrfName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 123, 1, 1, 1, 2),
    _QtechmplsL3VpnResVrfName_Type()
)
qtechmplsL3VpnResVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnResVrfName.setStatus("current")
_QtechmplsL3VpnResRtCollect_Type = DisplayString
_QtechmplsL3VpnResRtCollect_Object = MibTableColumn
qtechmplsL3VpnResRtCollect = _QtechmplsL3VpnResRtCollect_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 123, 1, 1, 1, 3),
    _QtechmplsL3VpnResRtCollect_Type()
)
qtechmplsL3VpnResRtCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechmplsL3VpnResRtCollect.setStatus("current")
_QtechmplsL3VpnResRdCollect_Type = DisplayString
_QtechmplsL3VpnResRdCollect_Object = MibTableColumn
qtechmplsL3VpnResRdCollect = _QtechmplsL3VpnResRdCollect_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 123, 1, 1, 1, 4),
    _QtechmplsL3VpnResRdCollect_Type()
)
qtechmplsL3VpnResRdCollect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnResRdCollect.setStatus("current")
_QtechmplsL3VpnResIntfAddr_Type = InetAddress
_QtechmplsL3VpnResIntfAddr_Object = MibTableColumn
qtechmplsL3VpnResIntfAddr = _QtechmplsL3VpnResIntfAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 123, 1, 1, 1, 5),
    _QtechmplsL3VpnResIntfAddr_Type()
)
qtechmplsL3VpnResIntfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnResIntfAddr.setStatus("current")
_QtechmplsL3VpnResImptRt_Type = DisplayString
_QtechmplsL3VpnResImptRt_Object = MibTableColumn
qtechmplsL3VpnResImptRt = _QtechmplsL3VpnResImptRt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 123, 1, 1, 1, 6),
    _QtechmplsL3VpnResImptRt_Type()
)
qtechmplsL3VpnResImptRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnResImptRt.setStatus("current")
_QtechmplsL3VpnResExptRt_Type = DisplayString
_QtechmplsL3VpnResExptRt_Object = MibTableColumn
qtechmplsL3VpnResExptRt = _QtechmplsL3VpnResExptRt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 123, 1, 1, 1, 7),
    _QtechmplsL3VpnResExptRt_Type()
)
qtechmplsL3VpnResExptRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnResExptRt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-MPLS-L3VPN-RES-MIB",
    **{"qtechmplsL3VpnResMIB": qtechmplsL3VpnResMIB,
       "qtechmplsL3VpnResMIBObjects": qtechmplsL3VpnResMIBObjects,
       "qtechmplsL3VpnResTable": qtechmplsL3VpnResTable,
       "qtechmplsL3VpnResEntry": qtechmplsL3VpnResEntry,
       "qtechmplsL3VpnResPeAddr": qtechmplsL3VpnResPeAddr,
       "qtechmplsL3VpnResVrfName": qtechmplsL3VpnResVrfName,
       "qtechmplsL3VpnResRtCollect": qtechmplsL3VpnResRtCollect,
       "qtechmplsL3VpnResRdCollect": qtechmplsL3VpnResRdCollect,
       "qtechmplsL3VpnResIntfAddr": qtechmplsL3VpnResIntfAddr,
       "qtechmplsL3VpnResImptRt": qtechmplsL3VpnResImptRt,
       "qtechmplsL3VpnResExptRt": qtechmplsL3VpnResExptRt}
)
