# SNMP MIB module (QTECH-MPLS-VPN-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-MPLS-VPN-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:50 2025
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

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp")

(VPNIdOrZero,) = mibBuilder.importSymbols(
    "VPN-TC-STD-MIB",
    "VPNIdOrZero")


# MODULE-IDENTITY

qtechMplsVPNMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122)
)
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtMIB.setRevisions(
        ("2013-01-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechMplsVPNMgmtMIBObjects_ObjectIdentity = ObjectIdentity
qtechMplsVPNMgmtMIBObjects = _QtechMplsVPNMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1)
)
_QtechMplsVPNMgmtVrf_ObjectIdentity = ObjectIdentity
qtechMplsVPNMgmtVrf = _QtechMplsVPNMgmtVrf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 1)
)
_QtechMplsVPNMgmtVrfTable_Object = MibTable
qtechMplsVPNMgmtVrfTable = _QtechMplsVPNMgmtVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtVrfTable.setStatus("current")
_QtechMplsVPNMgmtVrfEntry_Object = MibTableRow
qtechMplsVPNMgmtVrfEntry = _QtechMplsVPNMgmtVrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 1, 1, 1)
)
qtechMplsVPNMgmtVrfEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
)
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtVrfEntry.setStatus("current")
_QtechMplsVPNMgmtVrfName_Type = DisplayString
_QtechMplsVPNMgmtVrfName_Object = MibTableColumn
qtechMplsVPNMgmtVrfName = _QtechMplsVPNMgmtVrfName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 1, 1, 1, 1),
    _QtechMplsVPNMgmtVrfName_Type()
)
qtechMplsVPNMgmtVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtVrfName.setStatus("current")
_QtechMplsVPNMgmtVrfIntfFault_Type = Unsigned32
_QtechMplsVPNMgmtVrfIntfFault_Object = MibTableColumn
qtechMplsVPNMgmtVrfIntfFault = _QtechMplsVPNMgmtVrfIntfFault_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 1, 1, 1, 2),
    _QtechMplsVPNMgmtVrfIntfFault_Type()
)
qtechMplsVPNMgmtVrfIntfFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtVrfIntfFault.setStatus("current")
_QtechMplsVPNMgmtVrfVpnId_Type = VPNIdOrZero
_QtechMplsVPNMgmtVrfVpnId_Object = MibTableColumn
qtechMplsVPNMgmtVrfVpnId = _QtechMplsVPNMgmtVrfVpnId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 1, 1, 1, 3),
    _QtechMplsVPNMgmtVrfVpnId_Type()
)
qtechMplsVPNMgmtVrfVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtVrfVpnId.setStatus("current")


class _QtechMplsVPNMgmtVrfVpnIdType_Type(Integer32):
    """Custom type qtechMplsVPNMgmtVrfVpnIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l3vpn", 1),
          ("l2vpn", 2),
          ("other", 3))
    )


_QtechMplsVPNMgmtVrfVpnIdType_Type.__name__ = "Integer32"
_QtechMplsVPNMgmtVrfVpnIdType_Object = MibTableColumn
qtechMplsVPNMgmtVrfVpnIdType = _QtechMplsVPNMgmtVrfVpnIdType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 1, 1, 1, 4),
    _QtechMplsVPNMgmtVrfVpnIdType_Type()
)
qtechMplsVPNMgmtVrfVpnIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtVrfVpnIdType.setStatus("current")
_QtechMplsVPNMgmtRoute_ObjectIdentity = ObjectIdentity
qtechMplsVPNMgmtRoute = _QtechMplsVPNMgmtRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 2)
)
_QtechMplsVPNMgmtVrfRteTable_Object = MibTable
qtechMplsVPNMgmtVrfRteTable = _QtechMplsVPNMgmtVrfRteTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 2, 1)
)
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtVrfRteTable.setStatus("current")
_QtechMplsVPNMgmtVrfRteEntry_Object = MibTableRow
qtechMplsVPNMgmtVrfRteEntry = _QtechMplsVPNMgmtVrfRteEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 2, 1, 1)
)
qtechMplsVPNMgmtVrfRteEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
    (0, "QTECH-MPLS-VPN-MGMT-MIB", "qtechMplsVPNMgmtRteDestType"),
    (0, "QTECH-MPLS-VPN-MGMT-MIB", "qtechMplsVPNMgmtRteDest"),
    (0, "QTECH-MPLS-VPN-MGMT-MIB", "qtechMplsVPNMgmtRtePfxLen"),
    (0, "QTECH-MPLS-VPN-MGMT-MIB", "qtechMplsVPNMgmtRtePolicy"),
    (0, "QTECH-MPLS-VPN-MGMT-MIB", "qtechMplsVPNMgmtRteNHopType"),
    (0, "QTECH-MPLS-VPN-MGMT-MIB", "qtechMplsVPNMgmtRteNextHop"),
)
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtVrfRteEntry.setStatus("current")
_QtechMplsVPNMgmtRteDestType_Type = InetAddressType
_QtechMplsVPNMgmtRteDestType_Object = MibTableColumn
qtechMplsVPNMgmtRteDestType = _QtechMplsVPNMgmtRteDestType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 2, 1, 1, 1),
    _QtechMplsVPNMgmtRteDestType_Type()
)
qtechMplsVPNMgmtRteDestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtRteDestType.setStatus("current")
_QtechMplsVPNMgmtRteDest_Type = InetAddress
_QtechMplsVPNMgmtRteDest_Object = MibTableColumn
qtechMplsVPNMgmtRteDest = _QtechMplsVPNMgmtRteDest_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 2, 1, 1, 2),
    _QtechMplsVPNMgmtRteDest_Type()
)
qtechMplsVPNMgmtRteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtRteDest.setStatus("current")


class _QtechMplsVPNMgmtRtePfxLen_Type(InetAddressPrefixLength):
    """Custom type qtechMplsVPNMgmtRtePfxLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_QtechMplsVPNMgmtRtePfxLen_Type.__name__ = "InetAddressPrefixLength"
_QtechMplsVPNMgmtRtePfxLen_Object = MibTableColumn
qtechMplsVPNMgmtRtePfxLen = _QtechMplsVPNMgmtRtePfxLen_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 2, 1, 1, 3),
    _QtechMplsVPNMgmtRtePfxLen_Type()
)
qtechMplsVPNMgmtRtePfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtRtePfxLen.setStatus("current")
_QtechMplsVPNMgmtRtePolicy_Type = ObjectIdentifier
_QtechMplsVPNMgmtRtePolicy_Object = MibTableColumn
qtechMplsVPNMgmtRtePolicy = _QtechMplsVPNMgmtRtePolicy_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 2, 1, 1, 4),
    _QtechMplsVPNMgmtRtePolicy_Type()
)
qtechMplsVPNMgmtRtePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtRtePolicy.setStatus("current")
_QtechMplsVPNMgmtRteNHopType_Type = InetAddressType
_QtechMplsVPNMgmtRteNHopType_Object = MibTableColumn
qtechMplsVPNMgmtRteNHopType = _QtechMplsVPNMgmtRteNHopType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 2, 1, 1, 5),
    _QtechMplsVPNMgmtRteNHopType_Type()
)
qtechMplsVPNMgmtRteNHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtRteNHopType.setStatus("current")
_QtechMplsVPNMgmtRteNextHop_Type = InetAddress
_QtechMplsVPNMgmtRteNextHop_Object = MibTableColumn
qtechMplsVPNMgmtRteNextHop = _QtechMplsVPNMgmtRteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 2, 1, 1, 6),
    _QtechMplsVPNMgmtRteNextHop_Type()
)
qtechMplsVPNMgmtRteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtRteNextHop.setStatus("current")
_QtechMplsVPNMgmtRteDscp_Type = Dscp
_QtechMplsVPNMgmtRteDscp_Object = MibTableColumn
qtechMplsVPNMgmtRteDscp = _QtechMplsVPNMgmtRteDscp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 2, 1, 1, 7),
    _QtechMplsVPNMgmtRteDscp_Type()
)
qtechMplsVPNMgmtRteDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtRteDscp.setStatus("current")
_QtechMplsVPNMgmtRteStorageType_Type = StorageType
_QtechMplsVPNMgmtRteStorageType_Object = MibTableColumn
qtechMplsVPNMgmtRteStorageType = _QtechMplsVPNMgmtRteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 2, 1, 1, 8),
    _QtechMplsVPNMgmtRteStorageType_Type()
)
qtechMplsVPNMgmtRteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtRteStorageType.setStatus("current")
_QtechMplsVPNMgmtQos_ObjectIdentity = ObjectIdentity
qtechMplsVPNMgmtQos = _QtechMplsVPNMgmtQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3)
)
_QtechMplsVPNMgmtQosLSP_ObjectIdentity = ObjectIdentity
qtechMplsVPNMgmtQosLSP = _QtechMplsVPNMgmtQosLSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3, 1)
)
_QtechMplsVPNMgmtLSPNum_Type = Unsigned32
_QtechMplsVPNMgmtLSPNum_Object = MibScalar
qtechMplsVPNMgmtLSPNum = _QtechMplsVPNMgmtLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3, 1, 1),
    _QtechMplsVPNMgmtLSPNum_Type()
)
qtechMplsVPNMgmtLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtLSPNum.setStatus("current")
_QtechMplsVPNMgmtBackupLSPNum_Type = Unsigned32
_QtechMplsVPNMgmtBackupLSPNum_Object = MibScalar
qtechMplsVPNMgmtBackupLSPNum = _QtechMplsVPNMgmtBackupLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3, 1, 2),
    _QtechMplsVPNMgmtBackupLSPNum_Type()
)
qtechMplsVPNMgmtBackupLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtBackupLSPNum.setStatus("current")
_QtechMplsVPNMgmtLDPLSPNum_Type = Unsigned32
_QtechMplsVPNMgmtLDPLSPNum_Object = MibScalar
qtechMplsVPNMgmtLDPLSPNum = _QtechMplsVPNMgmtLDPLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3, 1, 3),
    _QtechMplsVPNMgmtLDPLSPNum_Type()
)
qtechMplsVPNMgmtLDPLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtLDPLSPNum.setStatus("current")
_QtechMplsVPNMgmtBGPLSPNum_Type = Unsigned32
_QtechMplsVPNMgmtBGPLSPNum_Object = MibScalar
qtechMplsVPNMgmtBGPLSPNum = _QtechMplsVPNMgmtBGPLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3, 1, 4),
    _QtechMplsVPNMgmtBGPLSPNum_Type()
)
qtechMplsVPNMgmtBGPLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtBGPLSPNum.setStatus("current")
_QtechMplsVPNMgmtStaticLSPNum_Type = Unsigned32
_QtechMplsVPNMgmtStaticLSPNum_Object = MibScalar
qtechMplsVPNMgmtStaticLSPNum = _QtechMplsVPNMgmtStaticLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3, 1, 5),
    _QtechMplsVPNMgmtStaticLSPNum_Type()
)
qtechMplsVPNMgmtStaticLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtStaticLSPNum.setStatus("current")
_QtechMplsVPNMgmtCRLDPLSPNum_Type = Unsigned32
_QtechMplsVPNMgmtCRLDPLSPNum_Object = MibScalar
qtechMplsVPNMgmtCRLDPLSPNum = _QtechMplsVPNMgmtCRLDPLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3, 1, 6),
    _QtechMplsVPNMgmtCRLDPLSPNum_Type()
)
qtechMplsVPNMgmtCRLDPLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtCRLDPLSPNum.setStatus("current")
_QtechMplsVPNMgmtRsvpLSPNum_Type = Unsigned32
_QtechMplsVPNMgmtRsvpLSPNum_Object = MibScalar
qtechMplsVPNMgmtRsvpLSPNum = _QtechMplsVPNMgmtRsvpLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3, 1, 7),
    _QtechMplsVPNMgmtRsvpLSPNum_Type()
)
qtechMplsVPNMgmtRsvpLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtRsvpLSPNum.setStatus("current")
_QtechMplsVPNMgmtBFDLSPNum_Type = Unsigned32
_QtechMplsVPNMgmtBFDLSPNum_Object = MibScalar
qtechMplsVPNMgmtBFDLSPNum = _QtechMplsVPNMgmtBFDLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3, 1, 8),
    _QtechMplsVPNMgmtBFDLSPNum_Type()
)
qtechMplsVPNMgmtBFDLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtBFDLSPNum.setStatus("current")
_QtechMplsVPNMgmtOAMLSPNum_Type = Unsigned32
_QtechMplsVPNMgmtOAMLSPNum_Object = MibScalar
qtechMplsVPNMgmtOAMLSPNum = _QtechMplsVPNMgmtOAMLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3, 1, 9),
    _QtechMplsVPNMgmtOAMLSPNum_Type()
)
qtechMplsVPNMgmtOAMLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtOAMLSPNum.setStatus("current")
_QtechMplsVPNMgmtIngressLSPNum_Type = Unsigned32
_QtechMplsVPNMgmtIngressLSPNum_Object = MibScalar
qtechMplsVPNMgmtIngressLSPNum = _QtechMplsVPNMgmtIngressLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3, 1, 10),
    _QtechMplsVPNMgmtIngressLSPNum_Type()
)
qtechMplsVPNMgmtIngressLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtIngressLSPNum.setStatus("current")
_QtechMplsVPNMgmtTransitLSPNum_Type = Unsigned32
_QtechMplsVPNMgmtTransitLSPNum_Object = MibScalar
qtechMplsVPNMgmtTransitLSPNum = _QtechMplsVPNMgmtTransitLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3, 1, 11),
    _QtechMplsVPNMgmtTransitLSPNum_Type()
)
qtechMplsVPNMgmtTransitLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtTransitLSPNum.setStatus("current")
_QtechMplsVPNMgmtEgressLSPNum_Type = Unsigned32
_QtechMplsVPNMgmtEgressLSPNum_Object = MibScalar
qtechMplsVPNMgmtEgressLSPNum = _QtechMplsVPNMgmtEgressLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3, 1, 12),
    _QtechMplsVPNMgmtEgressLSPNum_Type()
)
qtechMplsVPNMgmtEgressLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVPNMgmtEgressLSPNum.setStatus("current")
_QtechMplsVPNMgmtQosFault_ObjectIdentity = ObjectIdentity
qtechMplsVPNMgmtQosFault = _QtechMplsVPNMgmtQosFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3, 2)
)
_QtechMplsLSPFaultBFD_Type = Unsigned32
_QtechMplsLSPFaultBFD_Object = MibScalar
qtechMplsLSPFaultBFD = _QtechMplsLSPFaultBFD_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3, 2, 1),
    _QtechMplsLSPFaultBFD_Type()
)
qtechMplsLSPFaultBFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsLSPFaultBFD.setStatus("current")
_QtechMplsLSPFaultOAM_Type = Unsigned32
_QtechMplsLSPFaultOAM_Object = MibScalar
qtechMplsLSPFaultOAM = _QtechMplsLSPFaultOAM_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3, 2, 2),
    _QtechMplsLSPFaultOAM_Type()
)
qtechMplsLSPFaultOAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsLSPFaultOAM.setStatus("current")
_QtechMplsVrfFault_Type = Unsigned32
_QtechMplsVrfFault_Object = MibScalar
qtechMplsVrfFault = _QtechMplsVrfFault_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3, 2, 3),
    _QtechMplsVrfFault_Type()
)
qtechMplsVrfFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVrfFault.setStatus("current")
_QtechMplsPWFault_Type = Unsigned32
_QtechMplsPWFault_Object = MibScalar
qtechMplsPWFault = _QtechMplsPWFault_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 1, 3, 2, 4),
    _QtechMplsPWFault_Type()
)
qtechMplsPWFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsPWFault.setStatus("current")
_QtechMplsVPNMgmtMIBConformance_ObjectIdentity = ObjectIdentity
qtechMplsVPNMgmtMIBConformance = _QtechMplsVPNMgmtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 122, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-MPLS-VPN-MGMT-MIB",
    **{"qtechMplsVPNMgmtMIB": qtechMplsVPNMgmtMIB,
       "qtechMplsVPNMgmtMIBObjects": qtechMplsVPNMgmtMIBObjects,
       "qtechMplsVPNMgmtVrf": qtechMplsVPNMgmtVrf,
       "qtechMplsVPNMgmtVrfTable": qtechMplsVPNMgmtVrfTable,
       "qtechMplsVPNMgmtVrfEntry": qtechMplsVPNMgmtVrfEntry,
       "qtechMplsVPNMgmtVrfName": qtechMplsVPNMgmtVrfName,
       "qtechMplsVPNMgmtVrfIntfFault": qtechMplsVPNMgmtVrfIntfFault,
       "qtechMplsVPNMgmtVrfVpnId": qtechMplsVPNMgmtVrfVpnId,
       "qtechMplsVPNMgmtVrfVpnIdType": qtechMplsVPNMgmtVrfVpnIdType,
       "qtechMplsVPNMgmtRoute": qtechMplsVPNMgmtRoute,
       "qtechMplsVPNMgmtVrfRteTable": qtechMplsVPNMgmtVrfRteTable,
       "qtechMplsVPNMgmtVrfRteEntry": qtechMplsVPNMgmtVrfRteEntry,
       "qtechMplsVPNMgmtRteDestType": qtechMplsVPNMgmtRteDestType,
       "qtechMplsVPNMgmtRteDest": qtechMplsVPNMgmtRteDest,
       "qtechMplsVPNMgmtRtePfxLen": qtechMplsVPNMgmtRtePfxLen,
       "qtechMplsVPNMgmtRtePolicy": qtechMplsVPNMgmtRtePolicy,
       "qtechMplsVPNMgmtRteNHopType": qtechMplsVPNMgmtRteNHopType,
       "qtechMplsVPNMgmtRteNextHop": qtechMplsVPNMgmtRteNextHop,
       "qtechMplsVPNMgmtRteDscp": qtechMplsVPNMgmtRteDscp,
       "qtechMplsVPNMgmtRteStorageType": qtechMplsVPNMgmtRteStorageType,
       "qtechMplsVPNMgmtQos": qtechMplsVPNMgmtQos,
       "qtechMplsVPNMgmtQosLSP": qtechMplsVPNMgmtQosLSP,
       "qtechMplsVPNMgmtLSPNum": qtechMplsVPNMgmtLSPNum,
       "qtechMplsVPNMgmtBackupLSPNum": qtechMplsVPNMgmtBackupLSPNum,
       "qtechMplsVPNMgmtLDPLSPNum": qtechMplsVPNMgmtLDPLSPNum,
       "qtechMplsVPNMgmtBGPLSPNum": qtechMplsVPNMgmtBGPLSPNum,
       "qtechMplsVPNMgmtStaticLSPNum": qtechMplsVPNMgmtStaticLSPNum,
       "qtechMplsVPNMgmtCRLDPLSPNum": qtechMplsVPNMgmtCRLDPLSPNum,
       "qtechMplsVPNMgmtRsvpLSPNum": qtechMplsVPNMgmtRsvpLSPNum,
       "qtechMplsVPNMgmtBFDLSPNum": qtechMplsVPNMgmtBFDLSPNum,
       "qtechMplsVPNMgmtOAMLSPNum": qtechMplsVPNMgmtOAMLSPNum,
       "qtechMplsVPNMgmtIngressLSPNum": qtechMplsVPNMgmtIngressLSPNum,
       "qtechMplsVPNMgmtTransitLSPNum": qtechMplsVPNMgmtTransitLSPNum,
       "qtechMplsVPNMgmtEgressLSPNum": qtechMplsVPNMgmtEgressLSPNum,
       "qtechMplsVPNMgmtQosFault": qtechMplsVPNMgmtQosFault,
       "qtechMplsLSPFaultBFD": qtechMplsLSPFaultBFD,
       "qtechMplsLSPFaultOAM": qtechMplsLSPFaultOAM,
       "qtechMplsVrfFault": qtechMplsVrfFault,
       "qtechMplsPWFault": qtechMplsPWFault,
       "qtechMplsVPNMgmtMIBConformance": qtechMplsVPNMgmtMIBConformance}
)
