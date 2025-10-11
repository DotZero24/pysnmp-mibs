# SNMP MIB module (FS-MPLS-VPN-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-MPLS-VPN-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:03 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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

fsMplsVPNMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122)
)
if mibBuilder.loadTexts:
    fsMplsVPNMgmtMIB.setRevisions(
        ("2013-01-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMplsVPNMgmtMIBObjects_ObjectIdentity = ObjectIdentity
fsMplsVPNMgmtMIBObjects = _FsMplsVPNMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1)
)
_FsMplsVPNMgmtVrf_ObjectIdentity = ObjectIdentity
fsMplsVPNMgmtVrf = _FsMplsVPNMgmtVrf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 1)
)
_FsMplsVPNMgmtVrfTable_Object = MibTable
fsMplsVPNMgmtVrfTable = _FsMplsVPNMgmtVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsMplsVPNMgmtVrfTable.setStatus("current")
_FsMplsVPNMgmtVrfEntry_Object = MibTableRow
fsMplsVPNMgmtVrfEntry = _FsMplsVPNMgmtVrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 1, 1, 1)
)
fsMplsVPNMgmtVrfEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
)
if mibBuilder.loadTexts:
    fsMplsVPNMgmtVrfEntry.setStatus("current")
_FsMplsVPNMgmtVrfName_Type = DisplayString
_FsMplsVPNMgmtVrfName_Object = MibTableColumn
fsMplsVPNMgmtVrfName = _FsMplsVPNMgmtVrfName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 1, 1, 1, 1),
    _FsMplsVPNMgmtVrfName_Type()
)
fsMplsVPNMgmtVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtVrfName.setStatus("current")
_FsMplsVPNMgmtVrfIntfFault_Type = Unsigned32
_FsMplsVPNMgmtVrfIntfFault_Object = MibTableColumn
fsMplsVPNMgmtVrfIntfFault = _FsMplsVPNMgmtVrfIntfFault_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 1, 1, 1, 2),
    _FsMplsVPNMgmtVrfIntfFault_Type()
)
fsMplsVPNMgmtVrfIntfFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtVrfIntfFault.setStatus("current")
_FsMplsVPNMgmtVrfVpnId_Type = VPNIdOrZero
_FsMplsVPNMgmtVrfVpnId_Object = MibTableColumn
fsMplsVPNMgmtVrfVpnId = _FsMplsVPNMgmtVrfVpnId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 1, 1, 1, 3),
    _FsMplsVPNMgmtVrfVpnId_Type()
)
fsMplsVPNMgmtVrfVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtVrfVpnId.setStatus("current")


class _FsMplsVPNMgmtVrfVpnIdType_Type(Integer32):
    """Custom type fsMplsVPNMgmtVrfVpnIdType based on Integer32"""
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


_FsMplsVPNMgmtVrfVpnIdType_Type.__name__ = "Integer32"
_FsMplsVPNMgmtVrfVpnIdType_Object = MibTableColumn
fsMplsVPNMgmtVrfVpnIdType = _FsMplsVPNMgmtVrfVpnIdType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 1, 1, 1, 4),
    _FsMplsVPNMgmtVrfVpnIdType_Type()
)
fsMplsVPNMgmtVrfVpnIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtVrfVpnIdType.setStatus("current")
_FsMplsVPNMgmtRoute_ObjectIdentity = ObjectIdentity
fsMplsVPNMgmtRoute = _FsMplsVPNMgmtRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 2)
)
_FsMplsVPNMgmtVrfRteTable_Object = MibTable
fsMplsVPNMgmtVrfRteTable = _FsMplsVPNMgmtVrfRteTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsMplsVPNMgmtVrfRteTable.setStatus("current")
_FsMplsVPNMgmtVrfRteEntry_Object = MibTableRow
fsMplsVPNMgmtVrfRteEntry = _FsMplsVPNMgmtVrfRteEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 2, 1, 1)
)
fsMplsVPNMgmtVrfRteEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
    (0, "FS-MPLS-VPN-MGMT-MIB", "fsMplsVPNMgmtRteDestType"),
    (0, "FS-MPLS-VPN-MGMT-MIB", "fsMplsVPNMgmtRteDest"),
    (0, "FS-MPLS-VPN-MGMT-MIB", "fsMplsVPNMgmtRtePfxLen"),
    (0, "FS-MPLS-VPN-MGMT-MIB", "fsMplsVPNMgmtRtePolicy"),
    (0, "FS-MPLS-VPN-MGMT-MIB", "fsMplsVPNMgmtRteNHopType"),
    (0, "FS-MPLS-VPN-MGMT-MIB", "fsMplsVPNMgmtRteNextHop"),
)
if mibBuilder.loadTexts:
    fsMplsVPNMgmtVrfRteEntry.setStatus("current")
_FsMplsVPNMgmtRteDestType_Type = InetAddressType
_FsMplsVPNMgmtRteDestType_Object = MibTableColumn
fsMplsVPNMgmtRteDestType = _FsMplsVPNMgmtRteDestType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 2, 1, 1, 1),
    _FsMplsVPNMgmtRteDestType_Type()
)
fsMplsVPNMgmtRteDestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtRteDestType.setStatus("current")
_FsMplsVPNMgmtRteDest_Type = InetAddress
_FsMplsVPNMgmtRteDest_Object = MibTableColumn
fsMplsVPNMgmtRteDest = _FsMplsVPNMgmtRteDest_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 2, 1, 1, 2),
    _FsMplsVPNMgmtRteDest_Type()
)
fsMplsVPNMgmtRteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtRteDest.setStatus("current")


class _FsMplsVPNMgmtRtePfxLen_Type(InetAddressPrefixLength):
    """Custom type fsMplsVPNMgmtRtePfxLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsMplsVPNMgmtRtePfxLen_Type.__name__ = "InetAddressPrefixLength"
_FsMplsVPNMgmtRtePfxLen_Object = MibTableColumn
fsMplsVPNMgmtRtePfxLen = _FsMplsVPNMgmtRtePfxLen_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 2, 1, 1, 3),
    _FsMplsVPNMgmtRtePfxLen_Type()
)
fsMplsVPNMgmtRtePfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtRtePfxLen.setStatus("current")
_FsMplsVPNMgmtRtePolicy_Type = ObjectIdentifier
_FsMplsVPNMgmtRtePolicy_Object = MibTableColumn
fsMplsVPNMgmtRtePolicy = _FsMplsVPNMgmtRtePolicy_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 2, 1, 1, 4),
    _FsMplsVPNMgmtRtePolicy_Type()
)
fsMplsVPNMgmtRtePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtRtePolicy.setStatus("current")
_FsMplsVPNMgmtRteNHopType_Type = InetAddressType
_FsMplsVPNMgmtRteNHopType_Object = MibTableColumn
fsMplsVPNMgmtRteNHopType = _FsMplsVPNMgmtRteNHopType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 2, 1, 1, 5),
    _FsMplsVPNMgmtRteNHopType_Type()
)
fsMplsVPNMgmtRteNHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtRteNHopType.setStatus("current")
_FsMplsVPNMgmtRteNextHop_Type = InetAddress
_FsMplsVPNMgmtRteNextHop_Object = MibTableColumn
fsMplsVPNMgmtRteNextHop = _FsMplsVPNMgmtRteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 2, 1, 1, 6),
    _FsMplsVPNMgmtRteNextHop_Type()
)
fsMplsVPNMgmtRteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtRteNextHop.setStatus("current")
_FsMplsVPNMgmtRteDscp_Type = Dscp
_FsMplsVPNMgmtRteDscp_Object = MibTableColumn
fsMplsVPNMgmtRteDscp = _FsMplsVPNMgmtRteDscp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 2, 1, 1, 7),
    _FsMplsVPNMgmtRteDscp_Type()
)
fsMplsVPNMgmtRteDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtRteDscp.setStatus("current")
_FsMplsVPNMgmtRteStorageType_Type = StorageType
_FsMplsVPNMgmtRteStorageType_Object = MibTableColumn
fsMplsVPNMgmtRteStorageType = _FsMplsVPNMgmtRteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 2, 1, 1, 8),
    _FsMplsVPNMgmtRteStorageType_Type()
)
fsMplsVPNMgmtRteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtRteStorageType.setStatus("current")
_FsMplsVPNMgmtQos_ObjectIdentity = ObjectIdentity
fsMplsVPNMgmtQos = _FsMplsVPNMgmtQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3)
)
_FsMplsVPNMgmtQosLSP_ObjectIdentity = ObjectIdentity
fsMplsVPNMgmtQosLSP = _FsMplsVPNMgmtQosLSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3, 1)
)
_FsMplsVPNMgmtLSPNum_Type = Unsigned32
_FsMplsVPNMgmtLSPNum_Object = MibScalar
fsMplsVPNMgmtLSPNum = _FsMplsVPNMgmtLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3, 1, 1),
    _FsMplsVPNMgmtLSPNum_Type()
)
fsMplsVPNMgmtLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtLSPNum.setStatus("current")
_FsMplsVPNMgmtBackupLSPNum_Type = Unsigned32
_FsMplsVPNMgmtBackupLSPNum_Object = MibScalar
fsMplsVPNMgmtBackupLSPNum = _FsMplsVPNMgmtBackupLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3, 1, 2),
    _FsMplsVPNMgmtBackupLSPNum_Type()
)
fsMplsVPNMgmtBackupLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtBackupLSPNum.setStatus("current")
_FsMplsVPNMgmtLDPLSPNum_Type = Unsigned32
_FsMplsVPNMgmtLDPLSPNum_Object = MibScalar
fsMplsVPNMgmtLDPLSPNum = _FsMplsVPNMgmtLDPLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3, 1, 3),
    _FsMplsVPNMgmtLDPLSPNum_Type()
)
fsMplsVPNMgmtLDPLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtLDPLSPNum.setStatus("current")
_FsMplsVPNMgmtBGPLSPNum_Type = Unsigned32
_FsMplsVPNMgmtBGPLSPNum_Object = MibScalar
fsMplsVPNMgmtBGPLSPNum = _FsMplsVPNMgmtBGPLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3, 1, 4),
    _FsMplsVPNMgmtBGPLSPNum_Type()
)
fsMplsVPNMgmtBGPLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtBGPLSPNum.setStatus("current")
_FsMplsVPNMgmtStaticLSPNum_Type = Unsigned32
_FsMplsVPNMgmtStaticLSPNum_Object = MibScalar
fsMplsVPNMgmtStaticLSPNum = _FsMplsVPNMgmtStaticLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3, 1, 5),
    _FsMplsVPNMgmtStaticLSPNum_Type()
)
fsMplsVPNMgmtStaticLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtStaticLSPNum.setStatus("current")
_FsMplsVPNMgmtCRLDPLSPNum_Type = Unsigned32
_FsMplsVPNMgmtCRLDPLSPNum_Object = MibScalar
fsMplsVPNMgmtCRLDPLSPNum = _FsMplsVPNMgmtCRLDPLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3, 1, 6),
    _FsMplsVPNMgmtCRLDPLSPNum_Type()
)
fsMplsVPNMgmtCRLDPLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtCRLDPLSPNum.setStatus("current")
_FsMplsVPNMgmtRsvpLSPNum_Type = Unsigned32
_FsMplsVPNMgmtRsvpLSPNum_Object = MibScalar
fsMplsVPNMgmtRsvpLSPNum = _FsMplsVPNMgmtRsvpLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3, 1, 7),
    _FsMplsVPNMgmtRsvpLSPNum_Type()
)
fsMplsVPNMgmtRsvpLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtRsvpLSPNum.setStatus("current")
_FsMplsVPNMgmtBFDLSPNum_Type = Unsigned32
_FsMplsVPNMgmtBFDLSPNum_Object = MibScalar
fsMplsVPNMgmtBFDLSPNum = _FsMplsVPNMgmtBFDLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3, 1, 8),
    _FsMplsVPNMgmtBFDLSPNum_Type()
)
fsMplsVPNMgmtBFDLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtBFDLSPNum.setStatus("current")
_FsMplsVPNMgmtOAMLSPNum_Type = Unsigned32
_FsMplsVPNMgmtOAMLSPNum_Object = MibScalar
fsMplsVPNMgmtOAMLSPNum = _FsMplsVPNMgmtOAMLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3, 1, 9),
    _FsMplsVPNMgmtOAMLSPNum_Type()
)
fsMplsVPNMgmtOAMLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtOAMLSPNum.setStatus("current")
_FsMplsVPNMgmtIngressLSPNum_Type = Unsigned32
_FsMplsVPNMgmtIngressLSPNum_Object = MibScalar
fsMplsVPNMgmtIngressLSPNum = _FsMplsVPNMgmtIngressLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3, 1, 10),
    _FsMplsVPNMgmtIngressLSPNum_Type()
)
fsMplsVPNMgmtIngressLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtIngressLSPNum.setStatus("current")
_FsMplsVPNMgmtTransitLSPNum_Type = Unsigned32
_FsMplsVPNMgmtTransitLSPNum_Object = MibScalar
fsMplsVPNMgmtTransitLSPNum = _FsMplsVPNMgmtTransitLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3, 1, 11),
    _FsMplsVPNMgmtTransitLSPNum_Type()
)
fsMplsVPNMgmtTransitLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtTransitLSPNum.setStatus("current")
_FsMplsVPNMgmtEgressLSPNum_Type = Unsigned32
_FsMplsVPNMgmtEgressLSPNum_Object = MibScalar
fsMplsVPNMgmtEgressLSPNum = _FsMplsVPNMgmtEgressLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3, 1, 12),
    _FsMplsVPNMgmtEgressLSPNum_Type()
)
fsMplsVPNMgmtEgressLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVPNMgmtEgressLSPNum.setStatus("current")
_FsMplsVPNMgmtQosFault_ObjectIdentity = ObjectIdentity
fsMplsVPNMgmtQosFault = _FsMplsVPNMgmtQosFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3, 2)
)
_FsMplsLSPFaultBFD_Type = Unsigned32
_FsMplsLSPFaultBFD_Object = MibScalar
fsMplsLSPFaultBFD = _FsMplsLSPFaultBFD_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3, 2, 1),
    _FsMplsLSPFaultBFD_Type()
)
fsMplsLSPFaultBFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsLSPFaultBFD.setStatus("current")
_FsMplsLSPFaultOAM_Type = Unsigned32
_FsMplsLSPFaultOAM_Object = MibScalar
fsMplsLSPFaultOAM = _FsMplsLSPFaultOAM_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3, 2, 2),
    _FsMplsLSPFaultOAM_Type()
)
fsMplsLSPFaultOAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsLSPFaultOAM.setStatus("current")
_FsMplsVrfFault_Type = Unsigned32
_FsMplsVrfFault_Object = MibScalar
fsMplsVrfFault = _FsMplsVrfFault_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3, 2, 3),
    _FsMplsVrfFault_Type()
)
fsMplsVrfFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVrfFault.setStatus("current")
_FsMplsPWFault_Type = Unsigned32
_FsMplsPWFault_Object = MibScalar
fsMplsPWFault = _FsMplsPWFault_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 1, 3, 2, 4),
    _FsMplsPWFault_Type()
)
fsMplsPWFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsPWFault.setStatus("current")
_FsMplsVPNMgmtMIBConformance_ObjectIdentity = ObjectIdentity
fsMplsVPNMgmtMIBConformance = _FsMplsVPNMgmtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 122, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-MPLS-VPN-MGMT-MIB",
    **{"fsMplsVPNMgmtMIB": fsMplsVPNMgmtMIB,
       "fsMplsVPNMgmtMIBObjects": fsMplsVPNMgmtMIBObjects,
       "fsMplsVPNMgmtVrf": fsMplsVPNMgmtVrf,
       "fsMplsVPNMgmtVrfTable": fsMplsVPNMgmtVrfTable,
       "fsMplsVPNMgmtVrfEntry": fsMplsVPNMgmtVrfEntry,
       "fsMplsVPNMgmtVrfName": fsMplsVPNMgmtVrfName,
       "fsMplsVPNMgmtVrfIntfFault": fsMplsVPNMgmtVrfIntfFault,
       "fsMplsVPNMgmtVrfVpnId": fsMplsVPNMgmtVrfVpnId,
       "fsMplsVPNMgmtVrfVpnIdType": fsMplsVPNMgmtVrfVpnIdType,
       "fsMplsVPNMgmtRoute": fsMplsVPNMgmtRoute,
       "fsMplsVPNMgmtVrfRteTable": fsMplsVPNMgmtVrfRteTable,
       "fsMplsVPNMgmtVrfRteEntry": fsMplsVPNMgmtVrfRteEntry,
       "fsMplsVPNMgmtRteDestType": fsMplsVPNMgmtRteDestType,
       "fsMplsVPNMgmtRteDest": fsMplsVPNMgmtRteDest,
       "fsMplsVPNMgmtRtePfxLen": fsMplsVPNMgmtRtePfxLen,
       "fsMplsVPNMgmtRtePolicy": fsMplsVPNMgmtRtePolicy,
       "fsMplsVPNMgmtRteNHopType": fsMplsVPNMgmtRteNHopType,
       "fsMplsVPNMgmtRteNextHop": fsMplsVPNMgmtRteNextHop,
       "fsMplsVPNMgmtRteDscp": fsMplsVPNMgmtRteDscp,
       "fsMplsVPNMgmtRteStorageType": fsMplsVPNMgmtRteStorageType,
       "fsMplsVPNMgmtQos": fsMplsVPNMgmtQos,
       "fsMplsVPNMgmtQosLSP": fsMplsVPNMgmtQosLSP,
       "fsMplsVPNMgmtLSPNum": fsMplsVPNMgmtLSPNum,
       "fsMplsVPNMgmtBackupLSPNum": fsMplsVPNMgmtBackupLSPNum,
       "fsMplsVPNMgmtLDPLSPNum": fsMplsVPNMgmtLDPLSPNum,
       "fsMplsVPNMgmtBGPLSPNum": fsMplsVPNMgmtBGPLSPNum,
       "fsMplsVPNMgmtStaticLSPNum": fsMplsVPNMgmtStaticLSPNum,
       "fsMplsVPNMgmtCRLDPLSPNum": fsMplsVPNMgmtCRLDPLSPNum,
       "fsMplsVPNMgmtRsvpLSPNum": fsMplsVPNMgmtRsvpLSPNum,
       "fsMplsVPNMgmtBFDLSPNum": fsMplsVPNMgmtBFDLSPNum,
       "fsMplsVPNMgmtOAMLSPNum": fsMplsVPNMgmtOAMLSPNum,
       "fsMplsVPNMgmtIngressLSPNum": fsMplsVPNMgmtIngressLSPNum,
       "fsMplsVPNMgmtTransitLSPNum": fsMplsVPNMgmtTransitLSPNum,
       "fsMplsVPNMgmtEgressLSPNum": fsMplsVPNMgmtEgressLSPNum,
       "fsMplsVPNMgmtQosFault": fsMplsVPNMgmtQosFault,
       "fsMplsLSPFaultBFD": fsMplsLSPFaultBFD,
       "fsMplsLSPFaultOAM": fsMplsLSPFaultOAM,
       "fsMplsVrfFault": fsMplsVrfFault,
       "fsMplsPWFault": fsMplsPWFault,
       "fsMplsVPNMgmtMIBConformance": fsMplsVPNMgmtMIBConformance}
)
