# SNMP MIB module (MAIPU-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-PPP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:04 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mpPppMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PppConfTable_Object = MibTable
pppConfTable = _PppConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1)
)
if mibBuilder.loadTexts:
    pppConfTable.setStatus("current")
_PppConfEntry_Object = MibTableRow
pppConfEntry = _PppConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1)
)
pppConfEntry.setIndexNames(
    (0, "MAIPU-PPP-MIB", "pppIfIndex"),
)
if mibBuilder.loadTexts:
    pppConfEntry.setStatus("current")
_PppIfIndex_Type = Integer32
_PppIfIndex_Object = MibTableColumn
pppIfIndex = _PppIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 1),
    _PppIfIndex_Type()
)
pppIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIfIndex.setStatus("current")


class _PppIpNeg_Type(Integer32):
    """Custom type pppIpNeg based on Integer32"""
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


_PppIpNeg_Type.__name__ = "Integer32"
_PppIpNeg_Object = MibTableColumn
pppIpNeg = _PppIpNeg_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 2),
    _PppIpNeg_Type()
)
pppIpNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppIpNeg.setStatus("current")
_PppDefIpAddr_Type = IpAddress
_PppDefIpAddr_Object = MibTableColumn
pppDefIpAddr = _PppDefIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 3),
    _PppDefIpAddr_Type()
)
pppDefIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppDefIpAddr.setStatus("current")


class _PppDefIpDhcp_Type(Integer32):
    """Custom type pppDefIpDhcp based on Integer32"""
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


_PppDefIpDhcp_Type.__name__ = "Integer32"
_PppDefIpDhcp_Object = MibTableColumn
pppDefIpDhcp = _PppDefIpDhcp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 4),
    _PppDefIpDhcp_Type()
)
pppDefIpDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppDefIpDhcp.setStatus("current")


class _PppDefIpPool_Type(Integer32):
    """Custom type pppDefIpPool based on Integer32"""
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


_PppDefIpPool_Type.__name__ = "Integer32"
_PppDefIpPool_Object = MibTableColumn
pppDefIpPool = _PppDefIpPool_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 5),
    _PppDefIpPool_Type()
)
pppDefIpPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppDefIpPool.setStatus("current")
_PppDefIpPoolName_Type = OctetString
_PppDefIpPoolName_Object = MibScalar
pppDefIpPoolName = _PppDefIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 6),
    _PppDefIpPoolName_Type()
)
pppDefIpPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppDefIpPoolName.setStatus("current")


class _PppAc_Type(Integer32):
    """Custom type pppAc based on Integer32"""
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


_PppAc_Type.__name__ = "Integer32"
_PppAc_Object = MibTableColumn
pppAc = _PppAc_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 7),
    _PppAc_Type()
)
pppAc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAc.setStatus("current")
_PppAccountName_Type = OctetString
_PppAccountName_Object = MibTableColumn
pppAccountName = _PppAccountName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 8),
    _PppAccountName_Type()
)
pppAccountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAccountName.setStatus("current")


class _PppAuthChap_Type(Integer32):
    """Custom type pppAuthChap based on Integer32"""
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


_PppAuthChap_Type.__name__ = "Integer32"
_PppAuthChap_Object = MibTableColumn
pppAuthChap = _PppAuthChap_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 9),
    _PppAuthChap_Type()
)
pppAuthChap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthChap.setStatus("current")
_PppAuthChapName_Type = OctetString
_PppAuthChapName_Object = MibTableColumn
pppAuthChapName = _PppAuthChapName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 10),
    _PppAuthChapName_Type()
)
pppAuthChapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthChapName.setStatus("current")
_PppChapHostName_Type = OctetString
_PppChapHostName_Object = MibTableColumn
pppChapHostName = _PppChapHostName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 11),
    _PppChapHostName_Type()
)
pppChapHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppChapHostName.setStatus("current")


class _PppAuthPap_Type(Integer32):
    """Custom type pppAuthPap based on Integer32"""
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


_PppAuthPap_Type.__name__ = "Integer32"
_PppAuthPap_Object = MibTableColumn
pppAuthPap = _PppAuthPap_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 12),
    _PppAuthPap_Type()
)
pppAuthPap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthPap.setStatus("current")
_PppAuthPapName_Type = OctetString
_PppAuthPapName_Object = MibTableColumn
pppAuthPapName = _PppAuthPapName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 13),
    _PppAuthPapName_Type()
)
pppAuthPapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthPapName.setStatus("current")
_PppPapUsername_Type = OctetString
_PppPapUsername_Object = MibTableColumn
pppPapUsername = _PppPapUsername_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 14),
    _PppPapUsername_Type()
)
pppPapUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppPapUsername.setStatus("current")
_PppPapPassword_Type = OctetString
_PppPapPassword_Object = MibTableColumn
pppPapPassword = _PppPapPassword_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 15),
    _PppPapPassword_Type()
)
pppPapPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppPapPassword.setStatus("current")


class _PppAuthMsChap_Type(Integer32):
    """Custom type pppAuthMsChap based on Integer32"""
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


_PppAuthMsChap_Type.__name__ = "Integer32"
_PppAuthMsChap_Object = MibTableColumn
pppAuthMsChap = _PppAuthMsChap_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 16),
    _PppAuthMsChap_Type()
)
pppAuthMsChap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthMsChap.setStatus("current")
_PppAuthMsChapName_Type = OctetString
_PppAuthMsChapName_Object = MibTableColumn
pppAuthMsChapName = _PppAuthMsChapName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 17),
    _PppAuthMsChapName_Type()
)
pppAuthMsChapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthMsChapName.setStatus("current")


class _PppCallbackReq_Type(Integer32):
    """Custom type pppCallbackReq based on Integer32"""
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


_PppCallbackReq_Type.__name__ = "Integer32"
_PppCallbackReq_Object = MibTableColumn
pppCallbackReq = _PppCallbackReq_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 18),
    _PppCallbackReq_Type()
)
pppCallbackReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppCallbackReq.setStatus("current")


class _PppCallbackAcc_Type(Integer32):
    """Custom type pppCallbackAcc based on Integer32"""
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


_PppCallbackAcc_Type.__name__ = "Integer32"
_PppCallbackAcc_Object = MibTableColumn
pppCallbackAcc = _PppCallbackAcc_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 19),
    _PppCallbackAcc_Type()
)
pppCallbackAcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppCallbackAcc.setStatus("current")


class _PppCdp_Type(Integer32):
    """Custom type pppCdp based on Integer32"""
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


_PppCdp_Type.__name__ = "Integer32"
_PppCdp_Object = MibTableColumn
pppCdp = _PppCdp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 20),
    _PppCdp_Type()
)
pppCdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppCdp.setStatus("current")


class _PppComprePredictor_Type(Integer32):
    """Custom type pppComprePredictor based on Integer32"""
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


_PppComprePredictor_Type.__name__ = "Integer32"
_PppComprePredictor_Object = MibTableColumn
pppComprePredictor = _PppComprePredictor_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 21),
    _PppComprePredictor_Type()
)
pppComprePredictor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppComprePredictor.setStatus("current")


class _PppCompreStacker_Type(Integer32):
    """Custom type pppCompreStacker based on Integer32"""
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


_PppCompreStacker_Type.__name__ = "Integer32"
_PppCompreStacker_Object = MibTableColumn
pppCompreStacker = _PppCompreStacker_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 22),
    _PppCompreStacker_Type()
)
pppCompreStacker.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppCompreStacker.setStatus("current")
_PppEncDesKey_Type = OctetString
_PppEncDesKey_Object = MibTableColumn
pppEncDesKey = _PppEncDesKey_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 23),
    _PppEncDesKey_Type()
)
pppEncDesKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppEncDesKey.setStatus("current")
_PppEnc3DesKey_Type = OctetString
_PppEnc3DesKey_Object = MibTableColumn
pppEnc3DesKey = _PppEnc3DesKey_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 24),
    _PppEnc3DesKey_Type()
)
pppEnc3DesKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppEnc3DesKey.setStatus("current")
_PppEncDesBisKey_Type = OctetString
_PppEncDesBisKey_Object = MibTableColumn
pppEncDesBisKey = _PppEncDesBisKey_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 25),
    _PppEncDesBisKey_Type()
)
pppEncDesBisKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppEncDesBisKey.setStatus("current")


class _PppMultilink_Type(Integer32):
    """Custom type pppMultilink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("bap", 3))
    )


_PppMultilink_Type.__name__ = "Integer32"
_PppMultilink_Object = MibTableColumn
pppMultilink = _PppMultilink_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 26),
    _PppMultilink_Type()
)
pppMultilink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppMultilink.setStatus("current")


class _PppPc_Type(Integer32):
    """Custom type pppPc based on Integer32"""
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


_PppPc_Type.__name__ = "Integer32"
_PppPc_Object = MibTableColumn
pppPc = _PppPc_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 27),
    _PppPc_Type()
)
pppPc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppPc.setStatus("current")


class _PppReliableLink_Type(Integer32):
    """Custom type pppReliableLink based on Integer32"""
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


_PppReliableLink_Type.__name__ = "Integer32"
_PppReliableLink_Object = MibTableColumn
pppReliableLink = _PppReliableLink_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 28),
    _PppReliableLink_Type()
)
pppReliableLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppReliableLink.setStatus("current")


class _PppTimeoutAuth_Type(Integer32):
    """Custom type pppTimeoutAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PppTimeoutAuth_Type.__name__ = "Integer32"
_PppTimeoutAuth_Object = MibTableColumn
pppTimeoutAuth = _PppTimeoutAuth_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 29),
    _PppTimeoutAuth_Type()
)
pppTimeoutAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppTimeoutAuth.setStatus("current")


class _PppTimeoutIpcp_Type(Integer32):
    """Custom type pppTimeoutIpcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PppTimeoutIpcp_Type.__name__ = "Integer32"
_PppTimeoutIpcp_Object = MibTableColumn
pppTimeoutIpcp = _PppTimeoutIpcp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 30),
    _PppTimeoutIpcp_Type()
)
pppTimeoutIpcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppTimeoutIpcp.setStatus("current")


class _PppTimeoutRetry_Type(Integer32):
    """Custom type pppTimeoutRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PppTimeoutRetry_Type.__name__ = "Integer32"
_PppTimeoutRetry_Object = MibTableColumn
pppTimeoutRetry = _PppTimeoutRetry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 31),
    _PppTimeoutRetry_Type()
)
pppTimeoutRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppTimeoutRetry.setStatus("current")
_PppMultilinkBap_Type = Integer32
_PppMultilinkBap_Object = MibTableColumn
pppMultilinkBap = _PppMultilinkBap_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 1, 1, 32),
    _PppMultilinkBap_Type()
)
pppMultilinkBap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppMultilinkBap.setStatus("current")
_PppStatTable_Object = MibTable
pppStatTable = _PppStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2)
)
if mibBuilder.loadTexts:
    pppStatTable.setStatus("current")
_PppStatEntry_Object = MibTableRow
pppStatEntry = _PppStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1)
)
pppStatEntry.setIndexNames(
    (0, "MAIPU-PPP-MIB", "pppStatIfIndex"),
)
if mibBuilder.loadTexts:
    pppStatEntry.setStatus("current")
_PppStatIfIndex_Type = Integer32
_PppStatIfIndex_Object = MibTableColumn
pppStatIfIndex = _PppStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 1),
    _PppStatIfIndex_Type()
)
pppStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppStatIfIndex.setStatus("current")


class _PppLcpPhase_Type(Integer32):
    """Custom type pppLcpPhase based on Integer32"""
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
        *(("dead", 1),
          ("establish", 2),
          ("authenticate", 3),
          ("network", 4),
          ("terminate", 5))
    )


_PppLcpPhase_Type.__name__ = "Integer32"
_PppLcpPhase_Object = MibTableColumn
pppLcpPhase = _PppLcpPhase_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 2),
    _PppLcpPhase_Type()
)
pppLcpPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLcpPhase.setStatus("current")


class _PppLcpState_Type(Integer32):
    """Custom type pppLcpState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("starting", 2),
          ("closed", 3),
          ("stopped", 4),
          ("closing", 5),
          ("stopping", 6),
          ("requestSent", 7),
          ("ackReceived", 8),
          ("ackSent", 9),
          ("opened", 10))
    )


_PppLcpState_Type.__name__ = "Integer32"
_PppLcpState_Object = MibTableColumn
pppLcpState = _PppLcpState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 3),
    _PppLcpState_Type()
)
pppLcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLcpState.setStatus("current")
_PppLcpMru_Type = Integer32
_PppLcpMru_Object = MibTableColumn
pppLcpMru = _PppLcpMru_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 4),
    _PppLcpMru_Type()
)
pppLcpMru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLcpMru.setStatus("current")
_PppLcpMtu_Type = Integer32
_PppLcpMtu_Object = MibTableColumn
pppLcpMtu = _PppLcpMtu_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 5),
    _PppLcpMtu_Type()
)
pppLcpMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLcpMtu.setStatus("current")
_PppLcpAsyncMap_Type = Integer32
_PppLcpAsyncMap_Object = MibTableColumn
pppLcpAsyncMap = _PppLcpAsyncMap_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 6),
    _PppLcpAsyncMap_Type()
)
pppLcpAsyncMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLcpAsyncMap.setStatus("current")
_PppLcpLocalMagicNo_Type = Integer32
_PppLcpLocalMagicNo_Object = MibTableColumn
pppLcpLocalMagicNo = _PppLcpLocalMagicNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 7),
    _PppLcpLocalMagicNo_Type()
)
pppLcpLocalMagicNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLcpLocalMagicNo.setStatus("current")
_PppLcpProtoFieldComp_Type = Integer32
_PppLcpProtoFieldComp_Object = MibTableColumn
pppLcpProtoFieldComp = _PppLcpProtoFieldComp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 8),
    _PppLcpProtoFieldComp_Type()
)
pppLcpProtoFieldComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLcpProtoFieldComp.setStatus("current")
_PppLcpACFieldComp_Type = Integer32
_PppLcpACFieldComp_Object = MibTableColumn
pppLcpACFieldComp = _PppLcpACFieldComp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 9),
    _PppLcpACFieldComp_Type()
)
pppLcpACFieldComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLcpACFieldComp.setStatus("current")
_PppLcpEchoTimer_Type = Integer32
_PppLcpEchoTimer_Object = MibTableColumn
pppLcpEchoTimer = _PppLcpEchoTimer_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 10),
    _PppLcpEchoTimer_Type()
)
pppLcpEchoTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLcpEchoTimer.setStatus("current")
_PppLcpEchoPend_Type = Integer32
_PppLcpEchoPend_Object = MibTableColumn
pppLcpEchoPend = _PppLcpEchoPend_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 11),
    _PppLcpEchoPend_Type()
)
pppLcpEchoPend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLcpEchoPend.setStatus("current")
_PppLcpEchoNo_Type = Integer32
_PppLcpEchoNo_Object = MibTableColumn
pppLcpEchoNo = _PppLcpEchoNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 12),
    _PppLcpEchoNo_Type()
)
pppLcpEchoNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLcpEchoNo.setStatus("current")
_PppLcpEchoInter_Type = Integer32
_PppLcpEchoInter_Object = MibTableColumn
pppLcpEchoInter = _PppLcpEchoInter_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 13),
    _PppLcpEchoInter_Type()
)
pppLcpEchoInter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLcpEchoInter.setStatus("current")
_PppLcpEchoFails_Type = Integer32
_PppLcpEchoFails_Object = MibTableColumn
pppLcpEchoFails = _PppLcpEchoFails_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 14),
    _PppLcpEchoFails_Type()
)
pppLcpEchoFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLcpEchoFails.setStatus("current")


class _PppIpcpState_Type(Integer32):
    """Custom type pppIpcpState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("starting", 2),
          ("closed", 3),
          ("stopped", 4),
          ("closing", 5),
          ("stopping", 6),
          ("requestSent", 7),
          ("ackReceived", 8),
          ("ackSent", 9),
          ("opened", 10))
    )


_PppIpcpState_Type.__name__ = "Integer32"
_PppIpcpState_Object = MibTableColumn
pppIpcpState = _PppIpcpState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 15),
    _PppIpcpState_Type()
)
pppIpcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIpcpState.setStatus("current")
_PppIpcpLocalIPAddr_Type = IpAddress
_PppIpcpLocalIPAddr_Object = MibTableColumn
pppIpcpLocalIPAddr = _PppIpcpLocalIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 16),
    _PppIpcpLocalIPAddr_Type()
)
pppIpcpLocalIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIpcpLocalIPAddr.setStatus("current")
_PppIpcpRemIPAddr_Type = IpAddress
_PppIpcpRemIPAddr_Object = MibTableColumn
pppIpcpRemIPAddr = _PppIpcpRemIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 17),
    _PppIpcpRemIPAddr_Type()
)
pppIpcpRemIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIpcpRemIPAddr.setStatus("current")
_PppIpcpVJCompProto_Type = Integer32
_PppIpcpVJCompProto_Object = MibTableColumn
pppIpcpVJCompProto = _PppIpcpVJCompProto_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 18),
    _PppIpcpVJCompProto_Type()
)
pppIpcpVJCompProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIpcpVJCompProto.setStatus("current")
_PppIpcpVJCompPassive_Type = Integer32
_PppIpcpVJCompPassive_Object = MibTableColumn
pppIpcpVJCompPassive = _PppIpcpVJCompPassive_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 19),
    _PppIpcpVJCompPassive_Type()
)
pppIpcpVJCompPassive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIpcpVJCompPassive.setStatus("current")
_PppIpcpRtpCompProto_Type = Integer32
_PppIpcpRtpCompProto_Object = MibTableColumn
pppIpcpRtpCompProto = _PppIpcpRtpCompProto_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 20),
    _PppIpcpRtpCompProto_Type()
)
pppIpcpRtpCompProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIpcpRtpCompProto.setStatus("current")
_PppIpcpRtpCompPassive_Type = Integer32
_PppIpcpRtpCompPassive_Object = MibTableColumn
pppIpcpRtpCompPassive = _PppIpcpRtpCompPassive_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 21),
    _PppIpcpRtpCompPassive_Type()
)
pppIpcpRtpCompPassive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIpcpRtpCompPassive.setStatus("current")


class _PppCdpcpState_Type(Integer32):
    """Custom type pppCdpcpState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("starting", 2),
          ("closed", 3),
          ("stopped", 4),
          ("closing", 5),
          ("stopping", 6),
          ("requestSent", 7),
          ("ackReceived", 8),
          ("ackSent", 9),
          ("opened", 10))
    )


_PppCdpcpState_Type.__name__ = "Integer32"
_PppCdpcpState_Object = MibTableColumn
pppCdpcpState = _PppCdpcpState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 22),
    _PppCdpcpState_Type()
)
pppCdpcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCdpcpState.setStatus("current")


class _PppCcpState_Type(Integer32):
    """Custom type pppCcpState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("starting", 2),
          ("closed", 3),
          ("stopped", 4),
          ("closing", 5),
          ("stopping", 6),
          ("requestSent", 7),
          ("ackReceived", 8),
          ("ackSent", 9),
          ("opened", 10))
    )


_PppCcpState_Type.__name__ = "Integer32"
_PppCcpState_Object = MibTableColumn
pppCcpState = _PppCcpState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 23),
    _PppCcpState_Type()
)
pppCcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCcpState.setStatus("current")


class _PppEcpState_Type(Integer32):
    """Custom type pppEcpState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("starting", 2),
          ("closed", 3),
          ("stopped", 4),
          ("closing", 5),
          ("stopping", 6),
          ("requestSent", 7),
          ("ackReceived", 8),
          ("ackSent", 9),
          ("opened", 10))
    )


_PppEcpState_Type.__name__ = "Integer32"
_PppEcpState_Object = MibTableColumn
pppEcpState = _PppEcpState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 24),
    _PppEcpState_Type()
)
pppEcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEcpState.setStatus("current")


class _PppPapClientState_Type(Integer32):
    """Custom type pppPapClientState based on Integer32"""
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
        *(("initial", 1),
          ("closed", 2),
          ("pending", 3),
          ("authenticationReq", 4),
          ("open", 5),
          ("badAuthentication", 6))
    )


_PppPapClientState_Type.__name__ = "Integer32"
_PppPapClientState_Object = MibTableColumn
pppPapClientState = _PppPapClientState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 25),
    _PppPapClientState_Type()
)
pppPapClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppPapClientState.setStatus("current")


class _PppPapServerState_Type(Integer32):
    """Custom type pppPapServerState based on Integer32"""
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
        *(("initial", 1),
          ("closed", 2),
          ("pending", 3),
          ("listen", 4),
          ("open", 5),
          ("badAuthentication", 6))
    )


_PppPapServerState_Type.__name__ = "Integer32"
_PppPapServerState_Object = MibTableColumn
pppPapServerState = _PppPapServerState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 26),
    _PppPapServerState_Type()
)
pppPapServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppPapServerState.setStatus("current")


class _PppChapClientState_Type(Integer32):
    """Custom type pppChapClientState based on Integer32"""
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
        *(("initial", 1),
          ("closed", 2),
          ("pending", 3),
          ("listen", 4),
          ("response", 5),
          ("open", 6))
    )


_PppChapClientState_Type.__name__ = "Integer32"
_PppChapClientState_Object = MibTableColumn
pppChapClientState = _PppChapClientState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 27),
    _PppChapClientState_Type()
)
pppChapClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppChapClientState.setStatus("current")


class _PppChapServerState_Type(Integer32):
    """Custom type pppChapServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("closed", 2),
          ("pending", 3),
          ("initialChallenge", 4),
          ("oepn", 5),
          ("rechallenge", 6),
          ("badAuthentication", 7))
    )


_PppChapServerState_Type.__name__ = "Integer32"
_PppChapServerState_Object = MibTableColumn
pppChapServerState = _PppChapServerState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 28),
    _PppChapServerState_Type()
)
pppChapServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppChapServerState.setStatus("current")
_PppLzsdcpState_Type = Integer32
_PppLzsdcpState_Object = MibTableColumn
pppLzsdcpState = _PppLzsdcpState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 29),
    _PppLzsdcpState_Type()
)
pppLzsdcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLzsdcpState.setStatus("current")
_PppPredictor_Type = Integer32
_PppPredictor_Object = MibTableColumn
pppPredictor = _PppPredictor_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 30),
    _PppPredictor_Type()
)
pppPredictor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppPredictor.setStatus("current")
_PppDes_Type = Integer32
_PppDes_Object = MibTableColumn
pppDes = _PppDes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 31),
    _PppDes_Type()
)
pppDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDes.setStatus("current")
_PppDesBis_Type = Integer32
_PppDesBis_Object = MibTableColumn
pppDesBis = _PppDesBis_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 32),
    _PppDesBis_Type()
)
pppDesBis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDesBis.setStatus("current")
_Ppp3Des_Type = Integer32
_Ppp3Des_Object = MibTableColumn
ppp3Des = _Ppp3Des_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 2, 1, 33),
    _Ppp3Des_Type()
)
ppp3Des.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppp3Des.setStatus("current")
_PppCompStatTable_Object = MibTable
pppCompStatTable = _PppCompStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 3)
)
if mibBuilder.loadTexts:
    pppCompStatTable.setStatus("current")
_PppCompStatEntry_Object = MibTableRow
pppCompStatEntry = _PppCompStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 3, 1)
)
pppCompStatEntry.setIndexNames(
    (0, "MAIPU-PPP-MIB", "pppCompStatIfIndex"),
)
if mibBuilder.loadTexts:
    pppCompStatEntry.setStatus("current")
_PppCompStatIfIndex_Type = Integer32
_PppCompStatIfIndex_Object = MibTableColumn
pppCompStatIfIndex = _PppCompStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 3, 1, 1),
    _PppCompStatIfIndex_Type()
)
pppCompStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCompStatIfIndex.setStatus("current")


class _PppCompType_Type(Integer32):
    """Custom type pppCompType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stacker", 1),
          ("predictor", 2))
    )


_PppCompType_Type.__name__ = "Integer32"
_PppCompType_Object = MibTableColumn
pppCompType = _PppCompType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 3, 1, 2),
    _PppCompType_Type()
)
pppCompType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCompType.setStatus("current")
_PppUncompBytes_Type = Counter32
_PppUncompBytes_Object = MibTableColumn
pppUncompBytes = _PppUncompBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 3, 1, 3),
    _PppUncompBytes_Type()
)
pppUncompBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppUncompBytes.setStatus("current")
_PppUncompPkts_Type = Counter32
_PppUncompPkts_Object = MibTableColumn
pppUncompPkts = _PppUncompPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 3, 1, 4),
    _PppUncompPkts_Type()
)
pppUncompPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppUncompPkts.setStatus("current")
_PppCompBytes_Type = Counter32
_PppCompBytes_Object = MibTableColumn
pppCompBytes = _PppCompBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 3, 1, 5),
    _PppCompBytes_Type()
)
pppCompBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCompBytes.setStatus("current")
_PppCompPkts_Type = Counter32
_PppCompPkts_Object = MibTableColumn
pppCompPkts = _PppCompPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 3, 1, 6),
    _PppCompPkts_Type()
)
pppCompPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCompPkts.setStatus("current")
_PppIncompBytes_Type = Counter32
_PppIncompBytes_Object = MibTableColumn
pppIncompBytes = _PppIncompBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 3, 1, 7),
    _PppIncompBytes_Type()
)
pppIncompBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIncompBytes.setStatus("current")
_PppIncompPkts_Type = Counter32
_PppIncompPkts_Object = MibTableColumn
pppIncompPkts = _PppIncompPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 3, 1, 8),
    _PppIncompPkts_Type()
)
pppIncompPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIncompPkts.setStatus("current")
_PppRecvBytes_Type = Counter32
_PppRecvBytes_Object = MibTableColumn
pppRecvBytes = _PppRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 3, 1, 9),
    _PppRecvBytes_Type()
)
pppRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppRecvBytes.setStatus("current")
_PppTransBytes_Type = Counter32
_PppTransBytes_Object = MibTableColumn
pppTransBytes = _PppTransBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 3, 1, 10),
    _PppTransBytes_Type()
)
pppTransBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppTransBytes.setStatus("current")
_PppCompRatio_Type = Integer32
_PppCompRatio_Object = MibTableColumn
pppCompRatio = _PppCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 3, 1, 11),
    _PppCompRatio_Type()
)
pppCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCompRatio.setStatus("current")
_PppMultiTable_Object = MibTable
pppMultiTable = _PppMultiTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 4)
)
if mibBuilder.loadTexts:
    pppMultiTable.setStatus("current")
_PppMultiEntry_Object = MibTableRow
pppMultiEntry = _PppMultiEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 4, 1)
)
pppMultiEntry.setIndexNames(
    (0, "MAIPU-PPP-MIB", "pppVirtualAccInt"),
)
if mibBuilder.loadTexts:
    pppMultiEntry.setStatus("current")
_PppVirtualAccInt_Type = OctetString
_PppVirtualAccInt_Object = MibTableColumn
pppVirtualAccInt = _PppVirtualAccInt_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 4, 1, 1),
    _PppVirtualAccInt_Type()
)
pppVirtualAccInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppVirtualAccInt.setStatus("current")
_PppLogicInt_Type = OctetString
_PppLogicInt_Object = MibTableColumn
pppLogicInt = _PppLogicInt_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 4, 1, 2),
    _PppLogicInt_Type()
)
pppLogicInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLogicInt.setStatus("current")
_PppLocalVirtualIpAddr_Type = IpAddress
_PppLocalVirtualIpAddr_Object = MibTableColumn
pppLocalVirtualIpAddr = _PppLocalVirtualIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 4, 1, 3),
    _PppLocalVirtualIpAddr_Type()
)
pppLocalVirtualIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLocalVirtualIpAddr.setStatus("current")
_PppRemVirtualIpAddr_Type = IpAddress
_PppRemVirtualIpAddr_Object = MibScalar
pppRemVirtualIpAddr = _PppRemVirtualIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 4, 1, 4),
    _PppRemVirtualIpAddr_Type()
)
pppRemVirtualIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppRemVirtualIpAddr.setStatus("current")
_PppMultiMemNum_Type = Integer32
_PppMultiMemNum_Object = MibTableColumn
pppMultiMemNum = _PppMultiMemNum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 4, 1, 5),
    _PppMultiMemNum_Type()
)
pppMultiMemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMultiMemNum.setStatus("current")
_PppMultiIntTable_Object = MibTable
pppMultiIntTable = _PppMultiIntTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 5)
)
if mibBuilder.loadTexts:
    pppMultiIntTable.setStatus("current")
_PppMultiIntEntry_Object = MibTableRow
pppMultiIntEntry = _PppMultiIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 5, 1)
)
pppMultiIntEntry.setIndexNames(
    (0, "MAIPU-PPP-MIB", "pppMultiIntIfIndex"),
)
if mibBuilder.loadTexts:
    pppMultiIntEntry.setStatus("current")
_PppMultiIntIfIndex_Type = Integer32
_PppMultiIntIfIndex_Object = MibTableColumn
pppMultiIntIfIndex = _PppMultiIntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 5, 1, 1),
    _PppMultiIntIfIndex_Type()
)
pppMultiIntIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMultiIntIfIndex.setStatus("current")
_PppMultiIntName_Type = OctetString
_PppMultiIntName_Object = MibTableColumn
pppMultiIntName = _PppMultiIntName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 5, 1, 2),
    _PppMultiIntName_Type()
)
pppMultiIntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMultiIntName.setStatus("current")
_PppMultiIntBBandWidth_Type = Integer32
_PppMultiIntBBandWidth_Object = MibTableColumn
pppMultiIntBBandWidth = _PppMultiIntBBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 5, 1, 3),
    _PppMultiIntBBandWidth_Type()
)
pppMultiIntBBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMultiIntBBandWidth.setStatus("current")
_PppVirtualIntName_Type = OctetString
_PppVirtualIntName_Object = MibTableColumn
pppVirtualIntName = _PppVirtualIntName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 5, 5, 1, 4),
    _PppVirtualIntName_Type()
)
pppVirtualIntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppVirtualIntName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-PPP-MIB",
    **{"mpPppMib": mpPppMib,
       "pppConfTable": pppConfTable,
       "pppConfEntry": pppConfEntry,
       "pppIfIndex": pppIfIndex,
       "pppIpNeg": pppIpNeg,
       "pppDefIpAddr": pppDefIpAddr,
       "pppDefIpDhcp": pppDefIpDhcp,
       "pppDefIpPool": pppDefIpPool,
       "pppDefIpPoolName": pppDefIpPoolName,
       "pppAc": pppAc,
       "pppAccountName": pppAccountName,
       "pppAuthChap": pppAuthChap,
       "pppAuthChapName": pppAuthChapName,
       "pppChapHostName": pppChapHostName,
       "pppAuthPap": pppAuthPap,
       "pppAuthPapName": pppAuthPapName,
       "pppPapUsername": pppPapUsername,
       "pppPapPassword": pppPapPassword,
       "pppAuthMsChap": pppAuthMsChap,
       "pppAuthMsChapName": pppAuthMsChapName,
       "pppCallbackReq": pppCallbackReq,
       "pppCallbackAcc": pppCallbackAcc,
       "pppCdp": pppCdp,
       "pppComprePredictor": pppComprePredictor,
       "pppCompreStacker": pppCompreStacker,
       "pppEncDesKey": pppEncDesKey,
       "pppEnc3DesKey": pppEnc3DesKey,
       "pppEncDesBisKey": pppEncDesBisKey,
       "pppMultilink": pppMultilink,
       "pppPc": pppPc,
       "pppReliableLink": pppReliableLink,
       "pppTimeoutAuth": pppTimeoutAuth,
       "pppTimeoutIpcp": pppTimeoutIpcp,
       "pppTimeoutRetry": pppTimeoutRetry,
       "pppMultilinkBap": pppMultilinkBap,
       "pppStatTable": pppStatTable,
       "pppStatEntry": pppStatEntry,
       "pppStatIfIndex": pppStatIfIndex,
       "pppLcpPhase": pppLcpPhase,
       "pppLcpState": pppLcpState,
       "pppLcpMru": pppLcpMru,
       "pppLcpMtu": pppLcpMtu,
       "pppLcpAsyncMap": pppLcpAsyncMap,
       "pppLcpLocalMagicNo": pppLcpLocalMagicNo,
       "pppLcpProtoFieldComp": pppLcpProtoFieldComp,
       "pppLcpACFieldComp": pppLcpACFieldComp,
       "pppLcpEchoTimer": pppLcpEchoTimer,
       "pppLcpEchoPend": pppLcpEchoPend,
       "pppLcpEchoNo": pppLcpEchoNo,
       "pppLcpEchoInter": pppLcpEchoInter,
       "pppLcpEchoFails": pppLcpEchoFails,
       "pppIpcpState": pppIpcpState,
       "pppIpcpLocalIPAddr": pppIpcpLocalIPAddr,
       "pppIpcpRemIPAddr": pppIpcpRemIPAddr,
       "pppIpcpVJCompProto": pppIpcpVJCompProto,
       "pppIpcpVJCompPassive": pppIpcpVJCompPassive,
       "pppIpcpRtpCompProto": pppIpcpRtpCompProto,
       "pppIpcpRtpCompPassive": pppIpcpRtpCompPassive,
       "pppCdpcpState": pppCdpcpState,
       "pppCcpState": pppCcpState,
       "pppEcpState": pppEcpState,
       "pppPapClientState": pppPapClientState,
       "pppPapServerState": pppPapServerState,
       "pppChapClientState": pppChapClientState,
       "pppChapServerState": pppChapServerState,
       "pppLzsdcpState": pppLzsdcpState,
       "pppPredictor": pppPredictor,
       "pppDes": pppDes,
       "pppDesBis": pppDesBis,
       "ppp3Des": ppp3Des,
       "pppCompStatTable": pppCompStatTable,
       "pppCompStatEntry": pppCompStatEntry,
       "pppCompStatIfIndex": pppCompStatIfIndex,
       "pppCompType": pppCompType,
       "pppUncompBytes": pppUncompBytes,
       "pppUncompPkts": pppUncompPkts,
       "pppCompBytes": pppCompBytes,
       "pppCompPkts": pppCompPkts,
       "pppIncompBytes": pppIncompBytes,
       "pppIncompPkts": pppIncompPkts,
       "pppRecvBytes": pppRecvBytes,
       "pppTransBytes": pppTransBytes,
       "pppCompRatio": pppCompRatio,
       "pppMultiTable": pppMultiTable,
       "pppMultiEntry": pppMultiEntry,
       "pppVirtualAccInt": pppVirtualAccInt,
       "pppLogicInt": pppLogicInt,
       "pppLocalVirtualIpAddr": pppLocalVirtualIpAddr,
       "pppRemVirtualIpAddr": pppRemVirtualIpAddr,
       "pppMultiMemNum": pppMultiMemNum,
       "pppMultiIntTable": pppMultiIntTable,
       "pppMultiIntEntry": pppMultiIntEntry,
       "pppMultiIntIfIndex": pppMultiIntIfIndex,
       "pppMultiIntName": pppMultiIntName,
       "pppMultiIntBBandWidth": pppMultiIntBBandWidth,
       "pppVirtualIntName": pppVirtualIntName}
)
