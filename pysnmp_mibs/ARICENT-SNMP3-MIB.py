# SNMP MIB module (ARICENT-SNMP3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-SNMP3-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:27 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(SnmpTagValue,
 snmpTargetAddrEntry) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "SnmpTagValue",
    "snmpTargetAddrEntry")

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
 enterprises,
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
    "enterprises",
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

futuresnmp3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 112)
)
if mibBuilder.loadTexts:
    futuresnmp3.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnmpInInformResponses_Type = Counter32
_SnmpInInformResponses_Object = MibScalar
snmpInInformResponses = _SnmpInInformResponses_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 1),
    _SnmpInInformResponses_Type()
)
snmpInInformResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInInformResponses.setStatus("current")
_SnmpOutInformRequests_Type = Counter32
_SnmpOutInformRequests_Object = MibScalar
snmpOutInformRequests = _SnmpOutInformRequests_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 2),
    _SnmpOutInformRequests_Type()
)
snmpOutInformRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutInformRequests.setStatus("current")
_SnmpInformDrops_Type = Counter32
_SnmpInformDrops_Object = MibScalar
snmpInformDrops = _SnmpInformDrops_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 3),
    _SnmpInformDrops_Type()
)
snmpInformDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInformDrops.setStatus("current")
_SnmpInformAwaitingAck_Type = Counter32
_SnmpInformAwaitingAck_Object = MibScalar
snmpInformAwaitingAck = _SnmpInformAwaitingAck_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 4),
    _SnmpInformAwaitingAck_Type()
)
snmpInformAwaitingAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInformAwaitingAck.setStatus("current")


class _SnmpListenTrapPort_Type(Unsigned32):
    """Custom type snmpListenTrapPort based on Unsigned32"""
    defaultValue = 162

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpListenTrapPort_Type.__name__ = "Unsigned32"
_SnmpListenTrapPort_Object = MibScalar
snmpListenTrapPort = _SnmpListenTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 5),
    _SnmpListenTrapPort_Type()
)
snmpListenTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpListenTrapPort.setStatus("current")


class _SnmpOverTcpStatus_Type(Integer32):
    """Custom type snmpOverTcpStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SnmpOverTcpStatus_Type.__name__ = "Integer32"
_SnmpOverTcpStatus_Object = MibScalar
snmpOverTcpStatus = _SnmpOverTcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 6),
    _SnmpOverTcpStatus_Type()
)
snmpOverTcpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpOverTcpStatus.setStatus("current")


class _SnmpListenTcpPort_Type(Unsigned32):
    """Custom type snmpListenTcpPort based on Unsigned32"""
    defaultValue = 161

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpListenTcpPort_Type.__name__ = "Unsigned32"
_SnmpListenTcpPort_Object = MibScalar
snmpListenTcpPort = _SnmpListenTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 7),
    _SnmpListenTcpPort_Type()
)
snmpListenTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpListenTcpPort.setStatus("current")


class _SnmpTrapOverTcpStatus_Type(Integer32):
    """Custom type snmpTrapOverTcpStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SnmpTrapOverTcpStatus_Type.__name__ = "Integer32"
_SnmpTrapOverTcpStatus_Object = MibScalar
snmpTrapOverTcpStatus = _SnmpTrapOverTcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 8),
    _SnmpTrapOverTcpStatus_Type()
)
snmpTrapOverTcpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapOverTcpStatus.setStatus("current")


class _SnmpListenTcpTrapPort_Type(Unsigned32):
    """Custom type snmpListenTcpTrapPort based on Unsigned32"""
    defaultValue = 162

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpListenTcpTrapPort_Type.__name__ = "Unsigned32"
_SnmpListenTcpTrapPort_Object = MibScalar
snmpListenTcpTrapPort = _SnmpListenTcpTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 9),
    _SnmpListenTcpTrapPort_Type()
)
snmpListenTcpTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpListenTcpTrapPort.setStatus("current")
_SnmpInformCntTable_Object = MibTable
snmpInformCntTable = _SnmpInformCntTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 10)
)
if mibBuilder.loadTexts:
    snmpInformCntTable.setStatus("current")
_SnmpInformCntEntry_Object = MibTableRow
snmpInformCntEntry = _SnmpInformCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 10, 1)
)
snmpInformCntEntry.setIndexNames(
    (0, "ARICENT-SNMP3-MIB", "snmpInformTgtAddrName"),
)
if mibBuilder.loadTexts:
    snmpInformCntEntry.setStatus("current")


class _SnmpInformTgtAddrName_Type(SnmpAdminString):
    """Custom type snmpInformTgtAddrName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpInformTgtAddrName_Type.__name__ = "SnmpAdminString"
_SnmpInformTgtAddrName_Object = MibTableColumn
snmpInformTgtAddrName = _SnmpInformTgtAddrName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 10, 1, 1),
    _SnmpInformTgtAddrName_Type()
)
snmpInformTgtAddrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpInformTgtAddrName.setStatus("current")
_SnmpInformSent_Type = Counter32
_SnmpInformSent_Object = MibTableColumn
snmpInformSent = _SnmpInformSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 10, 1, 2),
    _SnmpInformSent_Type()
)
snmpInformSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInformSent.setStatus("current")
_SnmpInformAwaitAck_Type = Counter32
_SnmpInformAwaitAck_Object = MibTableColumn
snmpInformAwaitAck = _SnmpInformAwaitAck_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 10, 1, 3),
    _SnmpInformAwaitAck_Type()
)
snmpInformAwaitAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInformAwaitAck.setStatus("current")
_SnmpInformRetried_Type = Counter32
_SnmpInformRetried_Object = MibTableColumn
snmpInformRetried = _SnmpInformRetried_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 10, 1, 4),
    _SnmpInformRetried_Type()
)
snmpInformRetried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInformRetried.setStatus("current")
_SnmpInformDropped_Type = Counter32
_SnmpInformDropped_Object = MibTableColumn
snmpInformDropped = _SnmpInformDropped_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 10, 1, 5),
    _SnmpInformDropped_Type()
)
snmpInformDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInformDropped.setStatus("current")
_SnmpInformFailed_Type = Counter32
_SnmpInformFailed_Object = MibTableColumn
snmpInformFailed = _SnmpInformFailed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 10, 1, 6),
    _SnmpInformFailed_Type()
)
snmpInformFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInformFailed.setStatus("current")
_SnmpInformResponses_Type = Counter32
_SnmpInformResponses_Object = MibTableColumn
snmpInformResponses = _SnmpInformResponses_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 10, 1, 7),
    _SnmpInformResponses_Type()
)
snmpInformResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInformResponses.setStatus("current")


class _SnmpColdStartTrapControl_Type(Integer32):
    """Custom type snmpColdStartTrapControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SnmpColdStartTrapControl_Type.__name__ = "Integer32"
_SnmpColdStartTrapControl_Object = MibScalar
snmpColdStartTrapControl = _SnmpColdStartTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 11),
    _SnmpColdStartTrapControl_Type()
)
snmpColdStartTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpColdStartTrapControl.setStatus("current")


class _SnmpAgentControl_Type(Integer32):
    """Custom type snmpAgentControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SnmpAgentControl_Type.__name__ = "Integer32"
_SnmpAgentControl_Object = MibScalar
snmpAgentControl = _SnmpAgentControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 12),
    _SnmpAgentControl_Type()
)
snmpAgentControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentControl.setStatus("current")


class _SnmpAllowedPduVersions_Type(Integer32):
    """Custom type snmpAllowedPduVersions based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v3", 1),
          ("v1v2", 2),
          ("v1v2v3", 3))
    )


_SnmpAllowedPduVersions_Type.__name__ = "Integer32"
_SnmpAllowedPduVersions_Object = MibScalar
snmpAllowedPduVersions = _SnmpAllowedPduVersions_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 13),
    _SnmpAllowedPduVersions_Type()
)
snmpAllowedPduVersions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAllowedPduVersions.setStatus("current")


class _SnmpMinimumSecurityRequired_Type(Integer32):
    """Custom type snmpMinimumSecurityRequired based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("authenticated", 2),
          ("encrypted", 3))
    )


_SnmpMinimumSecurityRequired_Type.__name__ = "Integer32"
_SnmpMinimumSecurityRequired_Object = MibScalar
snmpMinimumSecurityRequired = _SnmpMinimumSecurityRequired_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 14),
    _SnmpMinimumSecurityRequired_Type()
)
snmpMinimumSecurityRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpMinimumSecurityRequired.setStatus("current")
_Futuresnmpagentx_ObjectIdentity = ObjectIdentity
futuresnmpagentx = _Futuresnmpagentx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15)
)


class _SnmpAgentxTransportDomain_Type(Integer32):
    """Custom type snmpAgentxTransportDomain based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("tcp", 1)
    )


_SnmpAgentxTransportDomain_Type.__name__ = "Integer32"
_SnmpAgentxTransportDomain_Object = MibScalar
snmpAgentxTransportDomain = _SnmpAgentxTransportDomain_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 1),
    _SnmpAgentxTransportDomain_Type()
)
snmpAgentxTransportDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentxTransportDomain.setStatus("current")


class _SnmpAgentxMasterAgentAddr_Type(OctetString):
    """Custom type snmpAgentxMasterAgentAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SnmpAgentxMasterAgentAddr_Type.__name__ = "OctetString"
_SnmpAgentxMasterAgentAddr_Object = MibScalar
snmpAgentxMasterAgentAddr = _SnmpAgentxMasterAgentAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 2),
    _SnmpAgentxMasterAgentAddr_Type()
)
snmpAgentxMasterAgentAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentxMasterAgentAddr.setStatus("current")


class _SnmpAgentxMasterAgentPortNo_Type(Unsigned32):
    """Custom type snmpAgentxMasterAgentPortNo based on Unsigned32"""
    defaultValue = 705


_SnmpAgentxMasterAgentPortNo_Type.__name__ = "Unsigned32"
_SnmpAgentxMasterAgentPortNo_Object = MibScalar
snmpAgentxMasterAgentPortNo = _SnmpAgentxMasterAgentPortNo_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 3),
    _SnmpAgentxMasterAgentPortNo_Type()
)
snmpAgentxMasterAgentPortNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentxMasterAgentPortNo.setStatus("current")
_SnmpAgentxSubAgentInPkts_Type = Counter32
_SnmpAgentxSubAgentInPkts_Object = MibScalar
snmpAgentxSubAgentInPkts = _SnmpAgentxSubAgentInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 4),
    _SnmpAgentxSubAgentInPkts_Type()
)
snmpAgentxSubAgentInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentInPkts.setStatus("current")
_SnmpAgentxSubAgentOutPkts_Type = Counter32
_SnmpAgentxSubAgentOutPkts_Object = MibScalar
snmpAgentxSubAgentOutPkts = _SnmpAgentxSubAgentOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 5),
    _SnmpAgentxSubAgentOutPkts_Type()
)
snmpAgentxSubAgentOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentOutPkts.setStatus("current")
_SnmpAgentxSubAgentPktDrops_Type = Counter32
_SnmpAgentxSubAgentPktDrops_Object = MibScalar
snmpAgentxSubAgentPktDrops = _SnmpAgentxSubAgentPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 6),
    _SnmpAgentxSubAgentPktDrops_Type()
)
snmpAgentxSubAgentPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentPktDrops.setStatus("current")
_SnmpAgentxSubAgentParseDrops_Type = Counter32
_SnmpAgentxSubAgentParseDrops_Object = MibScalar
snmpAgentxSubAgentParseDrops = _SnmpAgentxSubAgentParseDrops_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 7),
    _SnmpAgentxSubAgentParseDrops_Type()
)
snmpAgentxSubAgentParseDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentParseDrops.setStatus("current")
_SnmpAgentxSubAgentInOpenFail_Type = Counter32
_SnmpAgentxSubAgentInOpenFail_Object = MibScalar
snmpAgentxSubAgentInOpenFail = _SnmpAgentxSubAgentInOpenFail_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 8),
    _SnmpAgentxSubAgentInOpenFail_Type()
)
snmpAgentxSubAgentInOpenFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentInOpenFail.setStatus("current")
_SnmpAgentxSubAgentOpenPktCnt_Type = Counter32
_SnmpAgentxSubAgentOpenPktCnt_Object = MibScalar
snmpAgentxSubAgentOpenPktCnt = _SnmpAgentxSubAgentOpenPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 9),
    _SnmpAgentxSubAgentOpenPktCnt_Type()
)
snmpAgentxSubAgentOpenPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentOpenPktCnt.setStatus("current")
_SnmpAgentxSubAgentInClosePktCnt_Type = Counter32
_SnmpAgentxSubAgentInClosePktCnt_Object = MibScalar
snmpAgentxSubAgentInClosePktCnt = _SnmpAgentxSubAgentInClosePktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 10),
    _SnmpAgentxSubAgentInClosePktCnt_Type()
)
snmpAgentxSubAgentInClosePktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentInClosePktCnt.setStatus("current")
_SnmpAgentxSubAgentOutClosePktCnt_Type = Counter32
_SnmpAgentxSubAgentOutClosePktCnt_Object = MibScalar
snmpAgentxSubAgentOutClosePktCnt = _SnmpAgentxSubAgentOutClosePktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 11),
    _SnmpAgentxSubAgentOutClosePktCnt_Type()
)
snmpAgentxSubAgentOutClosePktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentOutClosePktCnt.setStatus("current")
_SnmpAgentxSubAgentIdAllocPktCnt_Type = Counter32
_SnmpAgentxSubAgentIdAllocPktCnt_Object = MibScalar
snmpAgentxSubAgentIdAllocPktCnt = _SnmpAgentxSubAgentIdAllocPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 12),
    _SnmpAgentxSubAgentIdAllocPktCnt_Type()
)
snmpAgentxSubAgentIdAllocPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentIdAllocPktCnt.setStatus("current")
_SnmpAgentxSubAgentIdDllocPktCnt_Type = Counter32
_SnmpAgentxSubAgentIdDllocPktCnt_Object = MibScalar
snmpAgentxSubAgentIdDllocPktCnt = _SnmpAgentxSubAgentIdDllocPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 13),
    _SnmpAgentxSubAgentIdDllocPktCnt_Type()
)
snmpAgentxSubAgentIdDllocPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentIdDllocPktCnt.setStatus("current")
_SnmpAgentxSubAgentRegPktCnt_Type = Counter32
_SnmpAgentxSubAgentRegPktCnt_Object = MibScalar
snmpAgentxSubAgentRegPktCnt = _SnmpAgentxSubAgentRegPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 14),
    _SnmpAgentxSubAgentRegPktCnt_Type()
)
snmpAgentxSubAgentRegPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentRegPktCnt.setStatus("current")
_SnmpAgentxSubAgentUnRegPktCnt_Type = Counter32
_SnmpAgentxSubAgentUnRegPktCnt_Object = MibScalar
snmpAgentxSubAgentUnRegPktCnt = _SnmpAgentxSubAgentUnRegPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 15),
    _SnmpAgentxSubAgentUnRegPktCnt_Type()
)
snmpAgentxSubAgentUnRegPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentUnRegPktCnt.setStatus("current")
_SnmpAgentxSubAgentAddCapsCnt_Type = Counter32
_SnmpAgentxSubAgentAddCapsCnt_Object = MibScalar
snmpAgentxSubAgentAddCapsCnt = _SnmpAgentxSubAgentAddCapsCnt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 16),
    _SnmpAgentxSubAgentAddCapsCnt_Type()
)
snmpAgentxSubAgentAddCapsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentAddCapsCnt.setStatus("current")
_SnmpAgentxSubAgentRemCapsCnt_Type = Counter32
_SnmpAgentxSubAgentRemCapsCnt_Object = MibScalar
snmpAgentxSubAgentRemCapsCnt = _SnmpAgentxSubAgentRemCapsCnt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 17),
    _SnmpAgentxSubAgentRemCapsCnt_Type()
)
snmpAgentxSubAgentRemCapsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentRemCapsCnt.setStatus("current")
_SnmpAgentxSubAgentNotifyPktCnt_Type = Counter32
_SnmpAgentxSubAgentNotifyPktCnt_Object = MibScalar
snmpAgentxSubAgentNotifyPktCnt = _SnmpAgentxSubAgentNotifyPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 18),
    _SnmpAgentxSubAgentNotifyPktCnt_Type()
)
snmpAgentxSubAgentNotifyPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentNotifyPktCnt.setStatus("current")
_SnmpAgentxSubAgentPingCnt_Type = Counter32
_SnmpAgentxSubAgentPingCnt_Object = MibScalar
snmpAgentxSubAgentPingCnt = _SnmpAgentxSubAgentPingCnt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 19),
    _SnmpAgentxSubAgentPingCnt_Type()
)
snmpAgentxSubAgentPingCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentPingCnt.setStatus("current")
_SnmpAgentxSubAgentInGets_Type = Counter32
_SnmpAgentxSubAgentInGets_Object = MibScalar
snmpAgentxSubAgentInGets = _SnmpAgentxSubAgentInGets_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 20),
    _SnmpAgentxSubAgentInGets_Type()
)
snmpAgentxSubAgentInGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentInGets.setStatus("current")
_SnmpAgentxSubAgentInGetNexts_Type = Counter32
_SnmpAgentxSubAgentInGetNexts_Object = MibScalar
snmpAgentxSubAgentInGetNexts = _SnmpAgentxSubAgentInGetNexts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 21),
    _SnmpAgentxSubAgentInGetNexts_Type()
)
snmpAgentxSubAgentInGetNexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentInGetNexts.setStatus("current")
_SnmpAgentxSubAgentInGetBulks_Type = Counter32
_SnmpAgentxSubAgentInGetBulks_Object = MibScalar
snmpAgentxSubAgentInGetBulks = _SnmpAgentxSubAgentInGetBulks_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 22),
    _SnmpAgentxSubAgentInGetBulks_Type()
)
snmpAgentxSubAgentInGetBulks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentInGetBulks.setStatus("current")
_SnmpAgentxSubAgentInTestSets_Type = Counter32
_SnmpAgentxSubAgentInTestSets_Object = MibScalar
snmpAgentxSubAgentInTestSets = _SnmpAgentxSubAgentInTestSets_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 23),
    _SnmpAgentxSubAgentInTestSets_Type()
)
snmpAgentxSubAgentInTestSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentInTestSets.setStatus("current")
_SnmpAgentxSubAgentInCommits_Type = Counter32
_SnmpAgentxSubAgentInCommits_Object = MibScalar
snmpAgentxSubAgentInCommits = _SnmpAgentxSubAgentInCommits_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 24),
    _SnmpAgentxSubAgentInCommits_Type()
)
snmpAgentxSubAgentInCommits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentInCommits.setStatus("current")
_SnmpAgentxSubAgentInCleanups_Type = Counter32
_SnmpAgentxSubAgentInCleanups_Object = MibScalar
snmpAgentxSubAgentInCleanups = _SnmpAgentxSubAgentInCleanups_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 25),
    _SnmpAgentxSubAgentInCleanups_Type()
)
snmpAgentxSubAgentInCleanups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentInCleanups.setStatus("current")
_SnmpAgentxSubAgentInUndos_Type = Counter32
_SnmpAgentxSubAgentInUndos_Object = MibScalar
snmpAgentxSubAgentInUndos = _SnmpAgentxSubAgentInUndos_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 26),
    _SnmpAgentxSubAgentInUndos_Type()
)
snmpAgentxSubAgentInUndos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentInUndos.setStatus("current")
_SnmpAgentxSubAgentOutResponse_Type = Counter32
_SnmpAgentxSubAgentOutResponse_Object = MibScalar
snmpAgentxSubAgentOutResponse = _SnmpAgentxSubAgentOutResponse_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 27),
    _SnmpAgentxSubAgentOutResponse_Type()
)
snmpAgentxSubAgentOutResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentOutResponse.setStatus("current")
_SnmpAgentxSubAgentInResponse_Type = Counter32
_SnmpAgentxSubAgentInResponse_Object = MibScalar
snmpAgentxSubAgentInResponse = _SnmpAgentxSubAgentInResponse_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 28),
    _SnmpAgentxSubAgentInResponse_Type()
)
snmpAgentxSubAgentInResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentInResponse.setStatus("current")


class _SnmpAgentxSubAgentControl_Type(Integer32):
    """Custom type snmpAgentxSubAgentControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SnmpAgentxSubAgentControl_Type.__name__ = "Integer32"
_SnmpAgentxSubAgentControl_Object = MibScalar
snmpAgentxSubAgentControl = _SnmpAgentxSubAgentControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 29),
    _SnmpAgentxSubAgentControl_Type()
)
snmpAgentxSubAgentControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentxSubAgentControl.setStatus("current")


class _SnmpAgentxContextName_Type(OctetString):
    """Custom type snmpAgentxContextName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpAgentxContextName_Type.__name__ = "OctetString"
_SnmpAgentxContextName_Object = MibScalar
snmpAgentxContextName = _SnmpAgentxContextName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 15, 30),
    _SnmpAgentxContextName_Type()
)
snmpAgentxContextName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentxContextName.setStatus("current")
_SnmpInRollbackErrs_Type = Counter32
_SnmpInRollbackErrs_Object = MibScalar
snmpInRollbackErrs = _SnmpInRollbackErrs_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 16),
    _SnmpInRollbackErrs_Type()
)
snmpInRollbackErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInRollbackErrs.setStatus("current")


class _SnmpProxyListenTrapPort_Type(Unsigned32):
    """Custom type snmpProxyListenTrapPort based on Unsigned32"""
    defaultValue = 162

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpProxyListenTrapPort_Type.__name__ = "Unsigned32"
_SnmpProxyListenTrapPort_Object = MibScalar
snmpProxyListenTrapPort = _SnmpProxyListenTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 17),
    _SnmpProxyListenTrapPort_Type()
)
snmpProxyListenTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProxyListenTrapPort.setStatus("current")
_FsSnmpProxyTable_Object = MibTable
fsSnmpProxyTable = _FsSnmpProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 18)
)
if mibBuilder.loadTexts:
    fsSnmpProxyTable.setStatus("current")
_FsSnmpProxyEntry_Object = MibTableRow
fsSnmpProxyEntry = _FsSnmpProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 18, 1)
)
fsSnmpProxyEntry.setIndexNames(
    (1, "ARICENT-SNMP3-MIB", "fsSnmpProxyMibName"),
)
if mibBuilder.loadTexts:
    fsSnmpProxyEntry.setStatus("current")


class _FsSnmpProxyMibName_Type(SnmpAdminString):
    """Custom type fsSnmpProxyMibName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsSnmpProxyMibName_Type.__name__ = "SnmpAdminString"
_FsSnmpProxyMibName_Object = MibTableColumn
fsSnmpProxyMibName = _FsSnmpProxyMibName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 18, 1, 1),
    _FsSnmpProxyMibName_Type()
)
fsSnmpProxyMibName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnmpProxyMibName.setStatus("current")


class _FsSnmpProxyMibType_Type(Integer32):
    """Custom type fsSnmpProxyMibType based on Integer32"""
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
        *(("read", 1),
          ("write", 2),
          ("trap", 3),
          ("inform", 4))
    )


_FsSnmpProxyMibType_Type.__name__ = "Integer32"
_FsSnmpProxyMibType_Object = MibTableColumn
fsSnmpProxyMibType = _FsSnmpProxyMibType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 18, 1, 2),
    _FsSnmpProxyMibType_Type()
)
fsSnmpProxyMibType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSnmpProxyMibType.setStatus("current")
_FsSnmpProxyMibId_Type = ObjectIdentifier
_FsSnmpProxyMibId_Object = MibTableColumn
fsSnmpProxyMibId = _FsSnmpProxyMibId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 18, 1, 3),
    _FsSnmpProxyMibId_Type()
)
fsSnmpProxyMibId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSnmpProxyMibId.setStatus("current")
_FsSnmpProxyMibTargetParamsIn_Type = SnmpAdminString
_FsSnmpProxyMibTargetParamsIn_Object = MibTableColumn
fsSnmpProxyMibTargetParamsIn = _FsSnmpProxyMibTargetParamsIn_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 18, 1, 4),
    _FsSnmpProxyMibTargetParamsIn_Type()
)
fsSnmpProxyMibTargetParamsIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSnmpProxyMibTargetParamsIn.setStatus("current")
_FsSnmpProxyMibSingleTargetOut_Type = SnmpAdminString
_FsSnmpProxyMibSingleTargetOut_Object = MibTableColumn
fsSnmpProxyMibSingleTargetOut = _FsSnmpProxyMibSingleTargetOut_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 18, 1, 5),
    _FsSnmpProxyMibSingleTargetOut_Type()
)
fsSnmpProxyMibSingleTargetOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSnmpProxyMibSingleTargetOut.setStatus("current")
_FsSnmpProxyMibMultipleTargetOut_Type = SnmpTagValue
_FsSnmpProxyMibMultipleTargetOut_Object = MibTableColumn
fsSnmpProxyMibMultipleTargetOut = _FsSnmpProxyMibMultipleTargetOut_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 18, 1, 6),
    _FsSnmpProxyMibMultipleTargetOut_Type()
)
fsSnmpProxyMibMultipleTargetOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSnmpProxyMibMultipleTargetOut.setStatus("current")


class _FsSnmpProxyMibStorageType_Type(StorageType):
    """Custom type fsSnmpProxyMibStorageType based on StorageType"""
    defaultValue = 3


_FsSnmpProxyMibStorageType_Type.__name__ = "StorageType"
_FsSnmpProxyMibStorageType_Object = MibTableColumn
fsSnmpProxyMibStorageType = _FsSnmpProxyMibStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 18, 1, 7),
    _FsSnmpProxyMibStorageType_Type()
)
fsSnmpProxyMibStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSnmpProxyMibStorageType.setStatus("current")
_FsSnmpProxyMibRowStatus_Type = RowStatus
_FsSnmpProxyMibRowStatus_Object = MibTableColumn
fsSnmpProxyMibRowStatus = _FsSnmpProxyMibRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 18, 1, 8),
    _FsSnmpProxyMibRowStatus_Type()
)
fsSnmpProxyMibRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSnmpProxyMibRowStatus.setStatus("current")


class _FsSnmpListenAgentPort_Type(Unsigned32):
    """Custom type fsSnmpListenAgentPort based on Unsigned32"""
    defaultValue = 161

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsSnmpListenAgentPort_Type.__name__ = "Unsigned32"
_FsSnmpListenAgentPort_Object = MibScalar
fsSnmpListenAgentPort = _FsSnmpListenAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 19),
    _FsSnmpListenAgentPort_Type()
)
fsSnmpListenAgentPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnmpListenAgentPort.setStatus("current")
_Futuresnmptraps_ObjectIdentity = ObjectIdentity
futuresnmptraps = _Futuresnmptraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 112, 20)
)
_FsSnmpTrapFilterTable_Object = MibTable
fsSnmpTrapFilterTable = _FsSnmpTrapFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 20, 3)
)
if mibBuilder.loadTexts:
    fsSnmpTrapFilterTable.setStatus("current")
_FsSnmpTrapFilterEntry_Object = MibTableRow
fsSnmpTrapFilterEntry = _FsSnmpTrapFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 20, 3, 1)
)
fsSnmpTrapFilterEntry.setIndexNames(
    (1, "ARICENT-SNMP3-MIB", "fsSnmpTrapFilterOID"),
)
if mibBuilder.loadTexts:
    fsSnmpTrapFilterEntry.setStatus("current")
_FsSnmpTrapFilterOID_Type = ObjectIdentifier
_FsSnmpTrapFilterOID_Object = MibTableColumn
fsSnmpTrapFilterOID = _FsSnmpTrapFilterOID_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 20, 3, 1, 1),
    _FsSnmpTrapFilterOID_Type()
)
fsSnmpTrapFilterOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSnmpTrapFilterOID.setStatus("current")
_FsSnmpTrapFilterRowStatus_Type = RowStatus
_FsSnmpTrapFilterRowStatus_Object = MibTableColumn
fsSnmpTrapFilterRowStatus = _FsSnmpTrapFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 20, 3, 1, 2),
    _FsSnmpTrapFilterRowStatus_Type()
)
fsSnmpTrapFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSnmpTrapFilterRowStatus.setStatus("current")
_FsSnmpTarget_ObjectIdentity = ObjectIdentity
fsSnmpTarget = _FsSnmpTarget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 112, 25)
)
_FsSnmpTargetAddrTable_Object = MibTable
fsSnmpTargetAddrTable = _FsSnmpTargetAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 25, 1)
)
if mibBuilder.loadTexts:
    fsSnmpTargetAddrTable.setStatus("current")
_FsSnmpTargetAddrEntry_Object = MibTableRow
fsSnmpTargetAddrEntry = _FsSnmpTargetAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 25, 1, 1)
)
if mibBuilder.loadTexts:
    fsSnmpTargetAddrEntry.setStatus("current")


class _FsSnmpTargetHostName_Type(OctetString):
    """Custom type fsSnmpTargetHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsSnmpTargetHostName_Type.__name__ = "OctetString"
_FsSnmpTargetHostName_Object = MibTableColumn
fsSnmpTargetHostName = _FsSnmpTargetHostName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 112, 25, 1, 1, 1),
    _FsSnmpTargetHostName_Type()
)
fsSnmpTargetHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSnmpTargetHostName.setStatus("current")
snmpTargetAddrEntry.registerAugmentions(
    ("ARICENT-SNMP3-MIB",
     "fsSnmpTargetAddrEntry")
)
fsSnmpTargetAddrEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())

# Managed Objects groups


# Notification objects

snmpMIBRegisteredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 112, 20, 1)
)
snmpMIBRegisteredTrap.setObjects(
    ("ARICENT-SNMP3-MIB", "fsSnmpListenAgentPort")
)
if mibBuilder.loadTexts:
    snmpMIBRegisteredTrap.setStatus(
        "current"
    )

snmpMIBDeRegisteredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 112, 20, 2)
)
snmpMIBDeRegisteredTrap.setObjects(
    ("ARICENT-SNMP3-MIB", "fsSnmpListenAgentPort")
)
if mibBuilder.loadTexts:
    snmpMIBDeRegisteredTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-SNMP3-MIB",
    **{"futuresnmp3": futuresnmp3,
       "snmpInInformResponses": snmpInInformResponses,
       "snmpOutInformRequests": snmpOutInformRequests,
       "snmpInformDrops": snmpInformDrops,
       "snmpInformAwaitingAck": snmpInformAwaitingAck,
       "snmpListenTrapPort": snmpListenTrapPort,
       "snmpOverTcpStatus": snmpOverTcpStatus,
       "snmpListenTcpPort": snmpListenTcpPort,
       "snmpTrapOverTcpStatus": snmpTrapOverTcpStatus,
       "snmpListenTcpTrapPort": snmpListenTcpTrapPort,
       "snmpInformCntTable": snmpInformCntTable,
       "snmpInformCntEntry": snmpInformCntEntry,
       "snmpInformTgtAddrName": snmpInformTgtAddrName,
       "snmpInformSent": snmpInformSent,
       "snmpInformAwaitAck": snmpInformAwaitAck,
       "snmpInformRetried": snmpInformRetried,
       "snmpInformDropped": snmpInformDropped,
       "snmpInformFailed": snmpInformFailed,
       "snmpInformResponses": snmpInformResponses,
       "snmpColdStartTrapControl": snmpColdStartTrapControl,
       "snmpAgentControl": snmpAgentControl,
       "snmpAllowedPduVersions": snmpAllowedPduVersions,
       "snmpMinimumSecurityRequired": snmpMinimumSecurityRequired,
       "futuresnmpagentx": futuresnmpagentx,
       "snmpAgentxTransportDomain": snmpAgentxTransportDomain,
       "snmpAgentxMasterAgentAddr": snmpAgentxMasterAgentAddr,
       "snmpAgentxMasterAgentPortNo": snmpAgentxMasterAgentPortNo,
       "snmpAgentxSubAgentInPkts": snmpAgentxSubAgentInPkts,
       "snmpAgentxSubAgentOutPkts": snmpAgentxSubAgentOutPkts,
       "snmpAgentxSubAgentPktDrops": snmpAgentxSubAgentPktDrops,
       "snmpAgentxSubAgentParseDrops": snmpAgentxSubAgentParseDrops,
       "snmpAgentxSubAgentInOpenFail": snmpAgentxSubAgentInOpenFail,
       "snmpAgentxSubAgentOpenPktCnt": snmpAgentxSubAgentOpenPktCnt,
       "snmpAgentxSubAgentInClosePktCnt": snmpAgentxSubAgentInClosePktCnt,
       "snmpAgentxSubAgentOutClosePktCnt": snmpAgentxSubAgentOutClosePktCnt,
       "snmpAgentxSubAgentIdAllocPktCnt": snmpAgentxSubAgentIdAllocPktCnt,
       "snmpAgentxSubAgentIdDllocPktCnt": snmpAgentxSubAgentIdDllocPktCnt,
       "snmpAgentxSubAgentRegPktCnt": snmpAgentxSubAgentRegPktCnt,
       "snmpAgentxSubAgentUnRegPktCnt": snmpAgentxSubAgentUnRegPktCnt,
       "snmpAgentxSubAgentAddCapsCnt": snmpAgentxSubAgentAddCapsCnt,
       "snmpAgentxSubAgentRemCapsCnt": snmpAgentxSubAgentRemCapsCnt,
       "snmpAgentxSubAgentNotifyPktCnt": snmpAgentxSubAgentNotifyPktCnt,
       "snmpAgentxSubAgentPingCnt": snmpAgentxSubAgentPingCnt,
       "snmpAgentxSubAgentInGets": snmpAgentxSubAgentInGets,
       "snmpAgentxSubAgentInGetNexts": snmpAgentxSubAgentInGetNexts,
       "snmpAgentxSubAgentInGetBulks": snmpAgentxSubAgentInGetBulks,
       "snmpAgentxSubAgentInTestSets": snmpAgentxSubAgentInTestSets,
       "snmpAgentxSubAgentInCommits": snmpAgentxSubAgentInCommits,
       "snmpAgentxSubAgentInCleanups": snmpAgentxSubAgentInCleanups,
       "snmpAgentxSubAgentInUndos": snmpAgentxSubAgentInUndos,
       "snmpAgentxSubAgentOutResponse": snmpAgentxSubAgentOutResponse,
       "snmpAgentxSubAgentInResponse": snmpAgentxSubAgentInResponse,
       "snmpAgentxSubAgentControl": snmpAgentxSubAgentControl,
       "snmpAgentxContextName": snmpAgentxContextName,
       "snmpInRollbackErrs": snmpInRollbackErrs,
       "snmpProxyListenTrapPort": snmpProxyListenTrapPort,
       "fsSnmpProxyTable": fsSnmpProxyTable,
       "fsSnmpProxyEntry": fsSnmpProxyEntry,
       "fsSnmpProxyMibName": fsSnmpProxyMibName,
       "fsSnmpProxyMibType": fsSnmpProxyMibType,
       "fsSnmpProxyMibId": fsSnmpProxyMibId,
       "fsSnmpProxyMibTargetParamsIn": fsSnmpProxyMibTargetParamsIn,
       "fsSnmpProxyMibSingleTargetOut": fsSnmpProxyMibSingleTargetOut,
       "fsSnmpProxyMibMultipleTargetOut": fsSnmpProxyMibMultipleTargetOut,
       "fsSnmpProxyMibStorageType": fsSnmpProxyMibStorageType,
       "fsSnmpProxyMibRowStatus": fsSnmpProxyMibRowStatus,
       "fsSnmpListenAgentPort": fsSnmpListenAgentPort,
       "futuresnmptraps": futuresnmptraps,
       "snmpMIBRegisteredTrap": snmpMIBRegisteredTrap,
       "snmpMIBDeRegisteredTrap": snmpMIBDeRegisteredTrap,
       "fsSnmpTrapFilterTable": fsSnmpTrapFilterTable,
       "fsSnmpTrapFilterEntry": fsSnmpTrapFilterEntry,
       "fsSnmpTrapFilterOID": fsSnmpTrapFilterOID,
       "fsSnmpTrapFilterRowStatus": fsSnmpTrapFilterRowStatus,
       "fsSnmpTarget": fsSnmpTarget,
       "fsSnmpTargetAddrTable": fsSnmpTargetAddrTable,
       "fsSnmpTargetAddrEntry": fsSnmpTargetAddrEntry,
       "fsSnmpTargetHostName": fsSnmpTargetHostName}
)
