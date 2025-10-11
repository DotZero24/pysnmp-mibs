# SNMP MIB module (ELTEX-MES-ISS-VLAN-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-VLAN-TUNNEL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:48:07 2025
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

(TunnelStatus,
 fsVlanDiscardStatsEntry,
 fsVlanTunnelProtocolEntry,
 fsVlanTunnelProtocolStatsEntry) = mibBuilder.importSymbols(
    "ARICENT-VLAN-EXT-MIB",
    "TunnelStatus",
    "fsVlanDiscardStatsEntry",
    "fsVlanTunnelProtocolEntry",
    "fsVlanTunnelProtocolStatsEntry")

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

eltMesIssVlanTunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21)
)
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelMIB.setRevisions(
        ("2021-06-29 00:00",
         "2020-07-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIssVlanTunnelObjects_ObjectIdentity = ObjectIdentity
eltMesIssVlanTunnelObjects = _EltMesIssVlanTunnelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1)
)
_EltMesIssVlanTunnelPvstAddress_Type = MacAddress
_EltMesIssVlanTunnelPvstAddress_Object = MibScalar
eltMesIssVlanTunnelPvstAddress = _EltMesIssVlanTunnelPvstAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 1),
    _EltMesIssVlanTunnelPvstAddress_Type()
)
eltMesIssVlanTunnelPvstAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelPvstAddress.setStatus("current")
_EltMesIssVlanTunnelVtpAddress_Type = MacAddress
_EltMesIssVlanTunnelVtpAddress_Object = MibScalar
eltMesIssVlanTunnelVtpAddress = _EltMesIssVlanTunnelVtpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 2),
    _EltMesIssVlanTunnelVtpAddress_Type()
)
eltMesIssVlanTunnelVtpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelVtpAddress.setStatus("current")
_EltMesIssVlanTunnelOspfAddress_Type = MacAddress
_EltMesIssVlanTunnelOspfAddress_Object = MibScalar
eltMesIssVlanTunnelOspfAddress = _EltMesIssVlanTunnelOspfAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 3),
    _EltMesIssVlanTunnelOspfAddress_Type()
)
eltMesIssVlanTunnelOspfAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelOspfAddress.setStatus("current")
_EltMesIssVlanTunnelRipAddress_Type = MacAddress
_EltMesIssVlanTunnelRipAddress_Object = MibScalar
eltMesIssVlanTunnelRipAddress = _EltMesIssVlanTunnelRipAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 4),
    _EltMesIssVlanTunnelRipAddress_Type()
)
eltMesIssVlanTunnelRipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelRipAddress.setStatus("current")
_EltMesIssVlanTunnelVrrpAddress_Type = MacAddress
_EltMesIssVlanTunnelVrrpAddress_Object = MibScalar
eltMesIssVlanTunnelVrrpAddress = _EltMesIssVlanTunnelVrrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 5),
    _EltMesIssVlanTunnelVrrpAddress_Type()
)
eltMesIssVlanTunnelVrrpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelVrrpAddress.setStatus("current")
_EltMesIssVlanTunnelProtocolTable_Object = MibTable
eltMesIssVlanTunnelProtocolTable = _EltMesIssVlanTunnelProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 6)
)
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolTable.setStatus("current")
_EltMesIssVlanTunnelProtocolEntry_Object = MibTableRow
eltMesIssVlanTunnelProtocolEntry = _EltMesIssVlanTunnelProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 6, 1)
)
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolEntry.setStatus("current")
_EltMesIssVlanTunnelProtocolPvst_Type = TunnelStatus
_EltMesIssVlanTunnelProtocolPvst_Object = MibTableColumn
eltMesIssVlanTunnelProtocolPvst = _EltMesIssVlanTunnelProtocolPvst_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 6, 1, 1),
    _EltMesIssVlanTunnelProtocolPvst_Type()
)
eltMesIssVlanTunnelProtocolPvst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolPvst.setStatus("current")
_EltMesIssVlanTunnelProtocolVtp_Type = TunnelStatus
_EltMesIssVlanTunnelProtocolVtp_Object = MibTableColumn
eltMesIssVlanTunnelProtocolVtp = _EltMesIssVlanTunnelProtocolVtp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 6, 1, 2),
    _EltMesIssVlanTunnelProtocolVtp_Type()
)
eltMesIssVlanTunnelProtocolVtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolVtp.setStatus("current")
_EltMesIssVlanTunnelProtocolOspf_Type = TunnelStatus
_EltMesIssVlanTunnelProtocolOspf_Object = MibTableColumn
eltMesIssVlanTunnelProtocolOspf = _EltMesIssVlanTunnelProtocolOspf_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 6, 1, 3),
    _EltMesIssVlanTunnelProtocolOspf_Type()
)
eltMesIssVlanTunnelProtocolOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolOspf.setStatus("current")
_EltMesIssVlanTunnelProtocolRip_Type = TunnelStatus
_EltMesIssVlanTunnelProtocolRip_Object = MibTableColumn
eltMesIssVlanTunnelProtocolRip = _EltMesIssVlanTunnelProtocolRip_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 6, 1, 4),
    _EltMesIssVlanTunnelProtocolRip_Type()
)
eltMesIssVlanTunnelProtocolRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolRip.setStatus("current")
_EltMesIssVlanTunnelProtocolVrrp_Type = TunnelStatus
_EltMesIssVlanTunnelProtocolVrrp_Object = MibTableColumn
eltMesIssVlanTunnelProtocolVrrp = _EltMesIssVlanTunnelProtocolVrrp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 6, 1, 5),
    _EltMesIssVlanTunnelProtocolVrrp_Type()
)
eltMesIssVlanTunnelProtocolVrrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolVrrp.setStatus("current")
_EltMesIssVlanTunnelProtocolStatsTable_Object = MibTable
eltMesIssVlanTunnelProtocolStatsTable = _EltMesIssVlanTunnelProtocolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 7)
)
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolStatsTable.setStatus("current")
_EltMesIssVlanTunnelProtocolStatsEntry_Object = MibTableRow
eltMesIssVlanTunnelProtocolStatsEntry = _EltMesIssVlanTunnelProtocolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 7, 1)
)
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolStatsEntry.setStatus("current")
_EltMesIssVlanTunnelProtocolPvstPktsRecvd_Type = Counter32
_EltMesIssVlanTunnelProtocolPvstPktsRecvd_Object = MibTableColumn
eltMesIssVlanTunnelProtocolPvstPktsRecvd = _EltMesIssVlanTunnelProtocolPvstPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 7, 1, 1),
    _EltMesIssVlanTunnelProtocolPvstPktsRecvd_Type()
)
eltMesIssVlanTunnelProtocolPvstPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolPvstPktsRecvd.setStatus("current")
_EltMesIssVlanTunnelProtocolPvstPktsSent_Type = Counter32
_EltMesIssVlanTunnelProtocolPvstPktsSent_Object = MibTableColumn
eltMesIssVlanTunnelProtocolPvstPktsSent = _EltMesIssVlanTunnelProtocolPvstPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 7, 1, 2),
    _EltMesIssVlanTunnelProtocolPvstPktsSent_Type()
)
eltMesIssVlanTunnelProtocolPvstPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolPvstPktsSent.setStatus("current")
_EltMesIssVlanTunnelProtocolVtpPktsRecvd_Type = Counter32
_EltMesIssVlanTunnelProtocolVtpPktsRecvd_Object = MibTableColumn
eltMesIssVlanTunnelProtocolVtpPktsRecvd = _EltMesIssVlanTunnelProtocolVtpPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 7, 1, 3),
    _EltMesIssVlanTunnelProtocolVtpPktsRecvd_Type()
)
eltMesIssVlanTunnelProtocolVtpPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolVtpPktsRecvd.setStatus("current")
_EltMesIssVlanTunnelProtocolVtpPktsSent_Type = Counter32
_EltMesIssVlanTunnelProtocolVtpPktsSent_Object = MibTableColumn
eltMesIssVlanTunnelProtocolVtpPktsSent = _EltMesIssVlanTunnelProtocolVtpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 7, 1, 4),
    _EltMesIssVlanTunnelProtocolVtpPktsSent_Type()
)
eltMesIssVlanTunnelProtocolVtpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolVtpPktsSent.setStatus("current")
_EltMesIssVlanTunnelProtocolOspfPktsRecvd_Type = Counter32
_EltMesIssVlanTunnelProtocolOspfPktsRecvd_Object = MibTableColumn
eltMesIssVlanTunnelProtocolOspfPktsRecvd = _EltMesIssVlanTunnelProtocolOspfPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 7, 1, 5),
    _EltMesIssVlanTunnelProtocolOspfPktsRecvd_Type()
)
eltMesIssVlanTunnelProtocolOspfPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolOspfPktsRecvd.setStatus("current")
_EltMesIssVlanTunnelProtocolOspfPktsSent_Type = Counter32
_EltMesIssVlanTunnelProtocolOspfPktsSent_Object = MibTableColumn
eltMesIssVlanTunnelProtocolOspfPktsSent = _EltMesIssVlanTunnelProtocolOspfPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 7, 1, 6),
    _EltMesIssVlanTunnelProtocolOspfPktsSent_Type()
)
eltMesIssVlanTunnelProtocolOspfPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolOspfPktsSent.setStatus("current")
_EltMesIssVlanTunnelProtocolRipPktsRecvd_Type = Counter32
_EltMesIssVlanTunnelProtocolRipPktsRecvd_Object = MibTableColumn
eltMesIssVlanTunnelProtocolRipPktsRecvd = _EltMesIssVlanTunnelProtocolRipPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 7, 1, 7),
    _EltMesIssVlanTunnelProtocolRipPktsRecvd_Type()
)
eltMesIssVlanTunnelProtocolRipPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolRipPktsRecvd.setStatus("current")
_EltMesIssVlanTunnelProtocolRipPktsSent_Type = Counter32
_EltMesIssVlanTunnelProtocolRipPktsSent_Object = MibTableColumn
eltMesIssVlanTunnelProtocolRipPktsSent = _EltMesIssVlanTunnelProtocolRipPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 7, 1, 8),
    _EltMesIssVlanTunnelProtocolRipPktsSent_Type()
)
eltMesIssVlanTunnelProtocolRipPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolRipPktsSent.setStatus("current")
_EltMesIssVlanTunnelProtocolVrrpPktsRecvd_Type = Counter32
_EltMesIssVlanTunnelProtocolVrrpPktsRecvd_Object = MibTableColumn
eltMesIssVlanTunnelProtocolVrrpPktsRecvd = _EltMesIssVlanTunnelProtocolVrrpPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 7, 1, 9),
    _EltMesIssVlanTunnelProtocolVrrpPktsRecvd_Type()
)
eltMesIssVlanTunnelProtocolVrrpPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolVrrpPktsRecvd.setStatus("current")
_EltMesIssVlanTunnelProtocolVrrpPktsSent_Type = Counter32
_EltMesIssVlanTunnelProtocolVrrpPktsSent_Object = MibTableColumn
eltMesIssVlanTunnelProtocolVrrpPktsSent = _EltMesIssVlanTunnelProtocolVrrpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 1, 7, 1, 10),
    _EltMesIssVlanTunnelProtocolVrrpPktsSent_Type()
)
eltMesIssVlanTunnelProtocolVrrpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanTunnelProtocolVrrpPktsSent.setStatus("current")
_EltMesIssVlanDiscardObjects_ObjectIdentity = ObjectIdentity
eltMesIssVlanDiscardObjects = _EltMesIssVlanDiscardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 2)
)
_EltMesIssVlanDiscardStatsTable_Object = MibTable
eltMesIssVlanDiscardStatsTable = _EltMesIssVlanDiscardStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 2, 1)
)
if mibBuilder.loadTexts:
    eltMesIssVlanDiscardStatsTable.setStatus("current")
_EltMesIssVlanDiscardStatsEntry_Object = MibTableRow
eltMesIssVlanDiscardStatsEntry = _EltMesIssVlanDiscardStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssVlanDiscardStatsEntry.setStatus("current")
_EltMesIssVlanDiscardPvstPktsRx_Type = Counter32
_EltMesIssVlanDiscardPvstPktsRx_Object = MibTableColumn
eltMesIssVlanDiscardPvstPktsRx = _EltMesIssVlanDiscardPvstPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 2, 1, 1, 1),
    _EltMesIssVlanDiscardPvstPktsRx_Type()
)
eltMesIssVlanDiscardPvstPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanDiscardPvstPktsRx.setStatus("current")
_EltMesIssVlanDiscardPvstPktsTx_Type = Counter32
_EltMesIssVlanDiscardPvstPktsTx_Object = MibTableColumn
eltMesIssVlanDiscardPvstPktsTx = _EltMesIssVlanDiscardPvstPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 2, 1, 1, 2),
    _EltMesIssVlanDiscardPvstPktsTx_Type()
)
eltMesIssVlanDiscardPvstPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanDiscardPvstPktsTx.setStatus("current")
_EltMesIssVlanDiscardVtpPktsRx_Type = Counter32
_EltMesIssVlanDiscardVtpPktsRx_Object = MibTableColumn
eltMesIssVlanDiscardVtpPktsRx = _EltMesIssVlanDiscardVtpPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 2, 1, 1, 3),
    _EltMesIssVlanDiscardVtpPktsRx_Type()
)
eltMesIssVlanDiscardVtpPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanDiscardVtpPktsRx.setStatus("current")
_EltMesIssVlanDiscardVtpPktsTx_Type = Counter32
_EltMesIssVlanDiscardVtpPktsTx_Object = MibTableColumn
eltMesIssVlanDiscardVtpPktsTx = _EltMesIssVlanDiscardVtpPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 2, 1, 1, 4),
    _EltMesIssVlanDiscardVtpPktsTx_Type()
)
eltMesIssVlanDiscardVtpPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanDiscardVtpPktsTx.setStatus("current")
_EltMesIssVlanDiscardOspfPktsRx_Type = Counter32
_EltMesIssVlanDiscardOspfPktsRx_Object = MibTableColumn
eltMesIssVlanDiscardOspfPktsRx = _EltMesIssVlanDiscardOspfPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 2, 1, 1, 5),
    _EltMesIssVlanDiscardOspfPktsRx_Type()
)
eltMesIssVlanDiscardOspfPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanDiscardOspfPktsRx.setStatus("current")
_EltMesIssVlanDiscardOspfPktsTx_Type = Counter32
_EltMesIssVlanDiscardOspfPktsTx_Object = MibTableColumn
eltMesIssVlanDiscardOspfPktsTx = _EltMesIssVlanDiscardOspfPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 2, 1, 1, 6),
    _EltMesIssVlanDiscardOspfPktsTx_Type()
)
eltMesIssVlanDiscardOspfPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanDiscardOspfPktsTx.setStatus("current")
_EltMesIssVlanDiscardRipPktsRx_Type = Counter32
_EltMesIssVlanDiscardRipPktsRx_Object = MibTableColumn
eltMesIssVlanDiscardRipPktsRx = _EltMesIssVlanDiscardRipPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 2, 1, 1, 7),
    _EltMesIssVlanDiscardRipPktsRx_Type()
)
eltMesIssVlanDiscardRipPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanDiscardRipPktsRx.setStatus("current")
_EltMesIssVlanDiscardRipPktsTx_Type = Counter32
_EltMesIssVlanDiscardRipPktsTx_Object = MibTableColumn
eltMesIssVlanDiscardRipPktsTx = _EltMesIssVlanDiscardRipPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 2, 1, 1, 8),
    _EltMesIssVlanDiscardRipPktsTx_Type()
)
eltMesIssVlanDiscardRipPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanDiscardRipPktsTx.setStatus("current")
_EltMesIssVlanDiscardVrrpPktsRx_Type = Counter32
_EltMesIssVlanDiscardVrrpPktsRx_Object = MibTableColumn
eltMesIssVlanDiscardVrrpPktsRx = _EltMesIssVlanDiscardVrrpPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 2, 1, 1, 9),
    _EltMesIssVlanDiscardVrrpPktsRx_Type()
)
eltMesIssVlanDiscardVrrpPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanDiscardVrrpPktsRx.setStatus("current")
_EltMesIssVlanDiscardVrrpPktsTx_Type = Counter32
_EltMesIssVlanDiscardVrrpPktsTx_Object = MibTableColumn
eltMesIssVlanDiscardVrrpPktsTx = _EltMesIssVlanDiscardVrrpPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21, 2, 1, 1, 10),
    _EltMesIssVlanDiscardVrrpPktsTx_Type()
)
eltMesIssVlanDiscardVrrpPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssVlanDiscardVrrpPktsTx.setStatus("current")
fsVlanTunnelProtocolEntry.registerAugmentions(
    ("ELTEX-MES-ISS-VLAN-TUNNEL-MIB",
     "eltMesIssVlanTunnelProtocolEntry")
)
eltMesIssVlanTunnelProtocolEntry.setIndexNames(*fsVlanTunnelProtocolEntry.getIndexNames())
fsVlanTunnelProtocolStatsEntry.registerAugmentions(
    ("ELTEX-MES-ISS-VLAN-TUNNEL-MIB",
     "eltMesIssVlanTunnelProtocolStatsEntry")
)
eltMesIssVlanTunnelProtocolStatsEntry.setIndexNames(*fsVlanTunnelProtocolStatsEntry.getIndexNames())
fsVlanDiscardStatsEntry.registerAugmentions(
    ("ELTEX-MES-ISS-VLAN-TUNNEL-MIB",
     "eltMesIssVlanDiscardStatsEntry")
)
eltMesIssVlanDiscardStatsEntry.setIndexNames(*fsVlanDiscardStatsEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-VLAN-TUNNEL-MIB",
    **{"eltMesIssVlanTunnelMIB": eltMesIssVlanTunnelMIB,
       "eltMesIssVlanTunnelObjects": eltMesIssVlanTunnelObjects,
       "eltMesIssVlanTunnelPvstAddress": eltMesIssVlanTunnelPvstAddress,
       "eltMesIssVlanTunnelVtpAddress": eltMesIssVlanTunnelVtpAddress,
       "eltMesIssVlanTunnelOspfAddress": eltMesIssVlanTunnelOspfAddress,
       "eltMesIssVlanTunnelRipAddress": eltMesIssVlanTunnelRipAddress,
       "eltMesIssVlanTunnelVrrpAddress": eltMesIssVlanTunnelVrrpAddress,
       "eltMesIssVlanTunnelProtocolTable": eltMesIssVlanTunnelProtocolTable,
       "eltMesIssVlanTunnelProtocolEntry": eltMesIssVlanTunnelProtocolEntry,
       "eltMesIssVlanTunnelProtocolPvst": eltMesIssVlanTunnelProtocolPvst,
       "eltMesIssVlanTunnelProtocolVtp": eltMesIssVlanTunnelProtocolVtp,
       "eltMesIssVlanTunnelProtocolOspf": eltMesIssVlanTunnelProtocolOspf,
       "eltMesIssVlanTunnelProtocolRip": eltMesIssVlanTunnelProtocolRip,
       "eltMesIssVlanTunnelProtocolVrrp": eltMesIssVlanTunnelProtocolVrrp,
       "eltMesIssVlanTunnelProtocolStatsTable": eltMesIssVlanTunnelProtocolStatsTable,
       "eltMesIssVlanTunnelProtocolStatsEntry": eltMesIssVlanTunnelProtocolStatsEntry,
       "eltMesIssVlanTunnelProtocolPvstPktsRecvd": eltMesIssVlanTunnelProtocolPvstPktsRecvd,
       "eltMesIssVlanTunnelProtocolPvstPktsSent": eltMesIssVlanTunnelProtocolPvstPktsSent,
       "eltMesIssVlanTunnelProtocolVtpPktsRecvd": eltMesIssVlanTunnelProtocolVtpPktsRecvd,
       "eltMesIssVlanTunnelProtocolVtpPktsSent": eltMesIssVlanTunnelProtocolVtpPktsSent,
       "eltMesIssVlanTunnelProtocolOspfPktsRecvd": eltMesIssVlanTunnelProtocolOspfPktsRecvd,
       "eltMesIssVlanTunnelProtocolOspfPktsSent": eltMesIssVlanTunnelProtocolOspfPktsSent,
       "eltMesIssVlanTunnelProtocolRipPktsRecvd": eltMesIssVlanTunnelProtocolRipPktsRecvd,
       "eltMesIssVlanTunnelProtocolRipPktsSent": eltMesIssVlanTunnelProtocolRipPktsSent,
       "eltMesIssVlanTunnelProtocolVrrpPktsRecvd": eltMesIssVlanTunnelProtocolVrrpPktsRecvd,
       "eltMesIssVlanTunnelProtocolVrrpPktsSent": eltMesIssVlanTunnelProtocolVrrpPktsSent,
       "eltMesIssVlanDiscardObjects": eltMesIssVlanDiscardObjects,
       "eltMesIssVlanDiscardStatsTable": eltMesIssVlanDiscardStatsTable,
       "eltMesIssVlanDiscardStatsEntry": eltMesIssVlanDiscardStatsEntry,
       "eltMesIssVlanDiscardPvstPktsRx": eltMesIssVlanDiscardPvstPktsRx,
       "eltMesIssVlanDiscardPvstPktsTx": eltMesIssVlanDiscardPvstPktsTx,
       "eltMesIssVlanDiscardVtpPktsRx": eltMesIssVlanDiscardVtpPktsRx,
       "eltMesIssVlanDiscardVtpPktsTx": eltMesIssVlanDiscardVtpPktsTx,
       "eltMesIssVlanDiscardOspfPktsRx": eltMesIssVlanDiscardOspfPktsRx,
       "eltMesIssVlanDiscardOspfPktsTx": eltMesIssVlanDiscardOspfPktsTx,
       "eltMesIssVlanDiscardRipPktsRx": eltMesIssVlanDiscardRipPktsRx,
       "eltMesIssVlanDiscardRipPktsTx": eltMesIssVlanDiscardRipPktsTx,
       "eltMesIssVlanDiscardVrrpPktsRx": eltMesIssVlanDiscardVrrpPktsRx,
       "eltMesIssVlanDiscardVrrpPktsTx": eltMesIssVlanDiscardVrrpPktsTx}
)
