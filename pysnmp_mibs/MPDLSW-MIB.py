# SNMP MIB module (MPDLSW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MPDLSW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:05 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mpDLSwMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DlswCktTable_Object = MibTable
dlswCktTable = _DlswCktTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1)
)
if mibBuilder.loadTexts:
    dlswCktTable.setStatus("current")
_DlswCktEntry_Object = MibTableRow
dlswCktEntry = _DlswCktEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1)
)
dlswCktEntry.setIndexNames(
    (0, "MPDLSW-MIB", "cktIndex"),
)
if mibBuilder.loadTexts:
    dlswCktEntry.setStatus("current")
_CktIndex_Type = Counter32
_CktIndex_Object = MibTableColumn
cktIndex = _CktIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 1),
    _CktIndex_Type()
)
cktIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktIndex.setStatus("current")
_CktPeer_Type = OctetString
_CktPeer_Object = MibTableColumn
cktPeer = _CktPeer_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 2),
    _CktPeer_Type()
)
cktPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktPeer.setStatus("current")


class _CktState_Type(Integer32):
    """Custom type cktState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 1),
          ("resov-pending", 2),
          ("ckt-start", 3),
          ("ckt-pending", 4),
          ("connect-pending", 5),
          ("ckt-established", 6),
          ("connected", 7),
          ("ckt-restart", 8),
          ("ckt-disconnect-pending", 9),
          ("ckt-restart-pending", 10),
          ("ckt-halt-pending", 11),
          ("ckt-halt-pendin-noack", 12))
    )


_CktState_Type.__name__ = "Integer32"
_CktState_Object = MibTableColumn
cktState = _CktState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 3),
    _CktState_Type()
)
cktState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktState.setStatus("current")
_CktTarMac_Type = OctetString
_CktTarMac_Object = MibTableColumn
cktTarMac = _CktTarMac_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 4),
    _CktTarMac_Type()
)
cktTarMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktTarMac.setStatus("current")
_CktOrgMac_Type = OctetString
_CktOrgMac_Object = MibTableColumn
cktOrgMac = _CktOrgMac_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 5),
    _CktOrgMac_Type()
)
cktOrgMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOrgMac.setStatus("current")
_CktTarSap_Type = Integer32
_CktTarSap_Object = MibTableColumn
cktTarSap = _CktTarSap_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 6),
    _CktTarSap_Type()
)
cktTarSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktTarSap.setStatus("current")
_CktOrgSap_Type = Integer32
_CktOrgSap_Object = MibTableColumn
cktOrgSap = _CktOrgSap_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 7),
    _CktOrgSap_Type()
)
cktOrgSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktOrgSap.setStatus("current")
_CktUpTime_Type = OctetString
_CktUpTime_Object = MibTableColumn
cktUpTime = _CktUpTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 8),
    _CktUpTime_Type()
)
cktUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktUpTime.setStatus("current")
_CktRxBytes_Type = Counter32
_CktRxBytes_Object = MibTableColumn
cktRxBytes = _CktRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 9),
    _CktRxBytes_Type()
)
cktRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRxBytes.setStatus("current")
_CktTxBytes_Type = Counter32
_CktTxBytes_Object = MibTableColumn
cktTxBytes = _CktTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 10),
    _CktTxBytes_Type()
)
cktTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktTxBytes.setStatus("current")
_CktRxIFrames_Type = Counter32
_CktRxIFrames_Object = MibTableColumn
cktRxIFrames = _CktRxIFrames_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 11),
    _CktRxIFrames_Type()
)
cktRxIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRxIFrames.setStatus("current")
_CktTxIFrames_Type = Counter32
_CktTxIFrames_Object = MibTableColumn
cktTxIFrames = _CktTxIFrames_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 12),
    _CktTxIFrames_Type()
)
cktTxIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktTxIFrames.setStatus("current")
_CktRxXIDFrames_Type = Counter32
_CktRxXIDFrames_Object = MibTableColumn
cktRxXIDFrames = _CktRxXIDFrames_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 13),
    _CktRxXIDFrames_Type()
)
cktRxXIDFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRxXIDFrames.setStatus("current")
_CktTxXIDFrames_Type = Counter32
_CktTxXIDFrames_Object = MibTableColumn
cktTxXIDFrames = _CktTxXIDFrames_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 14),
    _CktTxXIDFrames_Type()
)
cktTxXIDFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktTxXIDFrames.setStatus("current")
_CktRxUIFrames_Type = Counter32
_CktRxUIFrames_Object = MibTableColumn
cktRxUIFrames = _CktRxUIFrames_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 15),
    _CktRxUIFrames_Type()
)
cktRxUIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRxUIFrames.setStatus("current")
_CktTxUIFrames_Type = Counter32
_CktTxUIFrames_Object = MibTableColumn
cktTxUIFrames = _CktTxUIFrames_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 16),
    _CktTxUIFrames_Type()
)
cktTxUIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktTxUIFrames.setStatus("current")
_CktRxCurWin_Type = Counter32
_CktRxCurWin_Object = MibTableColumn
cktRxCurWin = _CktRxCurWin_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 17),
    _CktRxCurWin_Type()
)
cktRxCurWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRxCurWin.setStatus("current")
_CktRxGrantUnits_Type = Counter32
_CktRxGrantUnits_Object = MibTableColumn
cktRxGrantUnits = _CktRxGrantUnits_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 18),
    _CktRxGrantUnits_Type()
)
cktRxGrantUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktRxGrantUnits.setStatus("current")
_CktTxCurWin_Type = Counter32
_CktTxCurWin_Object = MibTableColumn
cktTxCurWin = _CktTxCurWin_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 19),
    _CktTxCurWin_Type()
)
cktTxCurWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktTxCurWin.setStatus("current")
_CktTxGrantUnits_Type = Counter32
_CktTxGrantUnits_Object = MibTableColumn
cktTxGrantUnits = _CktTxGrantUnits_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 1, 1, 20),
    _CktTxGrantUnits_Type()
)
cktTxGrantUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cktTxGrantUnits.setStatus("current")
_DlswPeerTable_Object = MibTable
dlswPeerTable = _DlswPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2)
)
if mibBuilder.loadTexts:
    dlswPeerTable.setStatus("current")
_DlswPeerEntry_Object = MibTableRow
dlswPeerEntry = _DlswPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1)
)
dlswPeerEntry.setIndexNames(
    (0, "MPDLSW-MIB", "peerIndex"),
)
if mibBuilder.loadTexts:
    dlswPeerEntry.setStatus("current")
_PeerIndex_Type = Counter32
_PeerIndex_Object = MibTableColumn
peerIndex = _PeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 1),
    _PeerIndex_Type()
)
peerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    peerIndex.setStatus("current")
_PeerIpAddr_Type = IpAddress
_PeerIpAddr_Object = MibTableColumn
peerIpAddr = _PeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 2),
    _PeerIpAddr_Type()
)
peerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    peerIpAddr.setStatus("current")


class _PeerCost_Type(Integer32):
    """Custom type peerCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_PeerCost_Type.__name__ = "Integer32"
_PeerCost_Object = MibTableColumn
peerCost = _PeerCost_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 3),
    _PeerCost_Type()
)
peerCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    peerCost.setStatus("current")


class _PeerKeepalive_Type(Integer32):
    """Custom type peerKeepalive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_PeerKeepalive_Type.__name__ = "Integer32"
_PeerKeepalive_Object = MibTableColumn
peerKeepalive = _PeerKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 4),
    _PeerKeepalive_Type()
)
peerKeepalive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    peerKeepalive.setStatus("current")


class _PeerType_Type(Integer32):
    """Custom type peerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("conf", 1),
          ("prom", 2))
    )


_PeerType_Type.__name__ = "Integer32"
_PeerType_Object = MibTableColumn
peerType = _PeerType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 5),
    _PeerType_Type()
)
peerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerType.setStatus("current")


class _PeerState_Type(Integer32):
    """Custom type peerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 1),
          ("wait-wr", 2),
          ("wait-rd", 3),
          ("connecting", 4),
          ("connect", 5))
    )


_PeerState_Type.__name__ = "Integer32"
_PeerState_Object = MibTableColumn
peerState = _PeerState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 6),
    _PeerState_Type()
)
peerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerState.setStatus("current")
_PeerUpTick_Type = OctetString
_PeerUpTick_Object = MibTableColumn
peerUpTick = _PeerUpTick_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 7),
    _PeerUpTick_Type()
)
peerUpTick.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerUpTick.setStatus("current")
_PeerRxPacks_Type = Counter32
_PeerRxPacks_Object = MibTableColumn
peerRxPacks = _PeerRxPacks_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 8),
    _PeerRxPacks_Type()
)
peerRxPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerRxPacks.setStatus("current")
_PeerTxPacks_Type = Counter32
_PeerTxPacks_Object = MibTableColumn
peerTxPacks = _PeerTxPacks_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 9),
    _PeerTxPacks_Type()
)
peerTxPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerTxPacks.setStatus("current")
_PeerDropPacks_Type = Counter32
_PeerDropPacks_Object = MibTableColumn
peerDropPacks = _PeerDropPacks_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 10),
    _PeerDropPacks_Type()
)
peerDropPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerDropPacks.setStatus("current")
_PeerVendorID_Type = Integer32
_PeerVendorID_Object = MibTableColumn
peerVendorID = _PeerVendorID_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 11),
    _PeerVendorID_Type()
)
peerVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerVendorID.setStatus("current")
_PeerVersion_Type = Integer32
_PeerVersion_Object = MibTableColumn
peerVersion = _PeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 12),
    _PeerVersion_Type()
)
peerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerVersion.setStatus("current")
_PeerRelease_Type = Integer32
_PeerRelease_Object = MibTableColumn
peerRelease = _PeerRelease_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 13),
    _PeerRelease_Type()
)
peerRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerRelease.setStatus("current")
_PeerGloblInitWin_Type = Integer32
_PeerGloblInitWin_Object = MibTableColumn
peerGloblInitWin = _PeerGloblInitWin_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 14),
    _PeerGloblInitWin_Type()
)
peerGloblInitWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerGloblInitWin.setStatus("current")
_PeerSupportSap_Type = OctetString
_PeerSupportSap_Object = MibTableColumn
peerSupportSap = _PeerSupportSap_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 15),
    _PeerSupportSap_Type()
)
peerSupportSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerSupportSap.setStatus("current")
_PeerTcpSessionNum_Type = Integer32
_PeerTcpSessionNum_Object = MibTableColumn
peerTcpSessionNum = _PeerTcpSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 16),
    _PeerTcpSessionNum_Type()
)
peerTcpSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerTcpSessionNum.setStatus("current")
_PeerMulticastCapable_Type = Integer32
_PeerMulticastCapable_Object = MibTableColumn
peerMulticastCapable = _PeerMulticastCapable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 17),
    _PeerMulticastCapable_Type()
)
peerMulticastCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerMulticastCapable.setStatus("current")
_PeerUdpUnicastSupport_Type = Integer32
_PeerUdpUnicastSupport_Object = MibTableColumn
peerUdpUnicastSupport = _PeerUdpUnicastSupport_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 18),
    _PeerUdpUnicastSupport_Type()
)
peerUdpUnicastSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerUdpUnicastSupport.setStatus("current")
_PeerBorderPeerCapable_Type = Integer32
_PeerBorderPeerCapable_Object = MibTableColumn
peerBorderPeerCapable = _PeerBorderPeerCapable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 19),
    _PeerBorderPeerCapable_Type()
)
peerBorderPeerCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerBorderPeerCapable.setStatus("current")
_PeerCapCost_Type = Integer32
_PeerCapCost_Object = MibTableColumn
peerCapCost = _PeerCapCost_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 20),
    _PeerCapCost_Type()
)
peerCapCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerCapCost.setStatus("current")
_PeerBiuSegment_Type = Integer32
_PeerBiuSegment_Object = MibTableColumn
peerBiuSegment = _PeerBiuSegment_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 21),
    _PeerBiuSegment_Type()
)
peerBiuSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerBiuSegment.setStatus("current")
_PeerGroup_Type = Integer32
_PeerGroup_Object = MibTableColumn
peerGroup = _PeerGroup_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 22),
    _PeerGroup_Type()
)
peerGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerGroup.setStatus("current")
_PeerLocalAck_Type = Integer32
_PeerLocalAck_Object = MibTableColumn
peerLocalAck = _PeerLocalAck_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 23),
    _PeerLocalAck_Type()
)
peerLocalAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerLocalAck.setStatus("current")
_PeerPriority_Type = Integer32
_PeerPriority_Object = MibTableColumn
peerPriority = _PeerPriority_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 24),
    _PeerPriority_Type()
)
peerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerPriority.setStatus("current")
_PeerVersionString_Type = OctetString
_PeerVersionString_Object = MibTableColumn
peerVersionString = _PeerVersionString_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 25),
    _PeerVersionString_Type()
)
peerVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerVersionString.setStatus("current")
_PeerStatus_Type = RowStatus
_PeerStatus_Object = MibTableColumn
peerStatus = _PeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 2, 1, 26),
    _PeerStatus_Type()
)
peerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    peerStatus.setStatus("current")
_DlswLocal_ObjectIdentity = ObjectIdentity
dlswLocal = _DlswLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 3)
)
if mibBuilder.loadTexts:
    dlswLocal.setStatus("current")
_LocalIpAddr_Type = OctetString
_LocalIpAddr_Object = MibScalar
localIpAddr = _LocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 3, 1),
    _LocalIpAddr_Type()
)
localIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localIpAddr.setStatus("current")


class _LocalPeerType_Type(Integer32):
    """Custom type localPeerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("conf", 1),
          ("prom", 2))
    )


_LocalPeerType_Type.__name__ = "Integer32"
_LocalPeerType_Object = MibScalar
localPeerType = _LocalPeerType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 3, 2),
    _LocalPeerType_Type()
)
localPeerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localPeerType.setStatus("current")


class _LocalDisable_Type(Integer32):
    """Custom type localDisable based on Integer32"""
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


_LocalDisable_Type.__name__ = "Integer32"
_LocalDisable_Object = MibScalar
localDisable = _LocalDisable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 3, 3),
    _LocalDisable_Type()
)
localDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localDisable.setStatus("current")


class _LocalKeepalive_Type(Integer32):
    """Custom type localKeepalive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_LocalKeepalive_Type.__name__ = "Integer32"
_LocalKeepalive_Object = MibScalar
localKeepalive = _LocalKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 3, 4),
    _LocalKeepalive_Type()
)
localKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localKeepalive.setStatus("current")
_LocalBrGrp_Type = OctetString
_LocalBrGrp_Object = MibScalar
localBrGrp = _LocalBrGrp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 3, 5),
    _LocalBrGrp_Type()
)
localBrGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localBrGrp.setStatus("current")


class _LocalGlobalInitWin_Type(Integer32):
    """Custom type localGlobalInitWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_LocalGlobalInitWin_Type.__name__ = "Integer32"
_LocalGlobalInitWin_Object = MibScalar
localGlobalInitWin = _LocalGlobalInitWin_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 3, 6),
    _LocalGlobalInitWin_Type()
)
localGlobalInitWin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localGlobalInitWin.setStatus("current")
_LocalSupportSap_Type = OctetString
_LocalSupportSap_Object = MibScalar
localSupportSap = _LocalSupportSap_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 3, 7),
    _LocalSupportSap_Type()
)
localSupportSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localSupportSap.setStatus("current")
_LocalICanReach_Type = Integer32
_LocalICanReach_Object = MibScalar
localICanReach = _LocalICanReach_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 3, 8),
    _LocalICanReach_Type()
)
localICanReach.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localICanReach.setStatus("current")
_LocalVersion_Type = Integer32
_LocalVersion_Object = MibScalar
localVersion = _LocalVersion_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 3, 9),
    _LocalVersion_Type()
)
localVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localVersion.setStatus("current")
_LocalVendorId_Type = OctetString
_LocalVendorId_Object = MibScalar
localVendorId = _LocalVendorId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 3, 10),
    _LocalVendorId_Type()
)
localVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localVendorId.setStatus("current")
_LocalVersionString_Type = OctetString
_LocalVersionString_Object = MibScalar
localVersionString = _LocalVersionString_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 22, 3, 11),
    _LocalVersionString_Type()
)
localVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localVersionString.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPDLSW-MIB",
    **{"mpDLSwMib": mpDLSwMib,
       "dlswCktTable": dlswCktTable,
       "dlswCktEntry": dlswCktEntry,
       "cktIndex": cktIndex,
       "cktPeer": cktPeer,
       "cktState": cktState,
       "cktTarMac": cktTarMac,
       "cktOrgMac": cktOrgMac,
       "cktTarSap": cktTarSap,
       "cktOrgSap": cktOrgSap,
       "cktUpTime": cktUpTime,
       "cktRxBytes": cktRxBytes,
       "cktTxBytes": cktTxBytes,
       "cktRxIFrames": cktRxIFrames,
       "cktTxIFrames": cktTxIFrames,
       "cktRxXIDFrames": cktRxXIDFrames,
       "cktTxXIDFrames": cktTxXIDFrames,
       "cktRxUIFrames": cktRxUIFrames,
       "cktTxUIFrames": cktTxUIFrames,
       "cktRxCurWin": cktRxCurWin,
       "cktRxGrantUnits": cktRxGrantUnits,
       "cktTxCurWin": cktTxCurWin,
       "cktTxGrantUnits": cktTxGrantUnits,
       "dlswPeerTable": dlswPeerTable,
       "dlswPeerEntry": dlswPeerEntry,
       "peerIndex": peerIndex,
       "peerIpAddr": peerIpAddr,
       "peerCost": peerCost,
       "peerKeepalive": peerKeepalive,
       "peerType": peerType,
       "peerState": peerState,
       "peerUpTick": peerUpTick,
       "peerRxPacks": peerRxPacks,
       "peerTxPacks": peerTxPacks,
       "peerDropPacks": peerDropPacks,
       "peerVendorID": peerVendorID,
       "peerVersion": peerVersion,
       "peerRelease": peerRelease,
       "peerGloblInitWin": peerGloblInitWin,
       "peerSupportSap": peerSupportSap,
       "peerTcpSessionNum": peerTcpSessionNum,
       "peerMulticastCapable": peerMulticastCapable,
       "peerUdpUnicastSupport": peerUdpUnicastSupport,
       "peerBorderPeerCapable": peerBorderPeerCapable,
       "peerCapCost": peerCapCost,
       "peerBiuSegment": peerBiuSegment,
       "peerGroup": peerGroup,
       "peerLocalAck": peerLocalAck,
       "peerPriority": peerPriority,
       "peerVersionString": peerVersionString,
       "peerStatus": peerStatus,
       "dlswLocal": dlswLocal,
       "localIpAddr": localIpAddr,
       "localPeerType": localPeerType,
       "localDisable": localDisable,
       "localKeepalive": localKeepalive,
       "localBrGrp": localBrGrp,
       "localGlobalInitWin": localGlobalInitWin,
       "localSupportSap": localSupportSap,
       "localICanReach": localICanReach,
       "localVersion": localVersion,
       "localVendorId": localVendorId,
       "localVersionString": localVersionString}
)
