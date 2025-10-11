# SNMP MIB module (SUPERMICRO-TCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-TCP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:57 2025
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tcpConnectionEntry,) = mibBuilder.importSymbols(
    "TCP-MIB",
    "tcpConnectionEntry")


# MODULE-IDENTITY

fstcp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18)
)
if mibBuilder.loadTexts:
    fstcp.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _FsTcpAckOption_Type(Integer32):
    """Custom type fsTcpAckOption based on Integer32"""
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
        *(("none", 1),
          ("sack", 2),
          ("nak", 3),
          ("fstrxmt", 4))
    )


_FsTcpAckOption_Type.__name__ = "Integer32"
_FsTcpAckOption_Object = MibScalar
fsTcpAckOption = _FsTcpAckOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 1),
    _FsTcpAckOption_Type()
)
fsTcpAckOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTcpAckOption.setStatus("current")
_FsTcpTimeStampOption_Type = TruthValue
_FsTcpTimeStampOption_Object = MibScalar
fsTcpTimeStampOption = _FsTcpTimeStampOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 2),
    _FsTcpTimeStampOption_Type()
)
fsTcpTimeStampOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTcpTimeStampOption.setStatus("current")
_FsTcpBigWndOption_Type = TruthValue
_FsTcpBigWndOption_Object = MibScalar
fsTcpBigWndOption = _FsTcpBigWndOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 3),
    _FsTcpBigWndOption_Type()
)
fsTcpBigWndOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTcpBigWndOption.setStatus("current")
_FsTcpIncrIniWnd_Type = TruthValue
_FsTcpIncrIniWnd_Object = MibScalar
fsTcpIncrIniWnd = _FsTcpIncrIniWnd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 4),
    _FsTcpIncrIniWnd_Type()
)
fsTcpIncrIniWnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTcpIncrIniWnd.setStatus("current")
_FsTcpMaxNumOfTCB_Type = Integer32
_FsTcpMaxNumOfTCB_Object = MibScalar
fsTcpMaxNumOfTCB = _FsTcpMaxNumOfTCB_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 5),
    _FsTcpMaxNumOfTCB_Type()
)
fsTcpMaxNumOfTCB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTcpMaxNumOfTCB.setStatus("current")
_FsTcpTraceDebug_Type = Integer32
_FsTcpTraceDebug_Object = MibScalar
fsTcpTraceDebug = _FsTcpTraceDebug_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 6),
    _FsTcpTraceDebug_Type()
)
fsTcpTraceDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTcpTraceDebug.setStatus("current")
_FsTcpConnTable_Object = MibTable
fsTcpConnTable = _FsTcpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7)
)
if mibBuilder.loadTexts:
    fsTcpConnTable.setStatus("current")
_FsTcpConnEntry_Object = MibTableRow
fsTcpConnEntry = _FsTcpConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1)
)
fsTcpConnEntry.setIndexNames(
    (0, "SUPERMICRO-TCP-MIB", "fsTcpConnLocalAddress"),
    (0, "SUPERMICRO-TCP-MIB", "fsTcpConnLocalPort"),
    (0, "SUPERMICRO-TCP-MIB", "fsTcpConnRemAddress"),
    (0, "SUPERMICRO-TCP-MIB", "fsTcpConnRemPort"),
)
if mibBuilder.loadTexts:
    fsTcpConnEntry.setStatus("current")
_FsTcpConnLocalAddress_Type = IpAddress
_FsTcpConnLocalAddress_Object = MibTableColumn
fsTcpConnLocalAddress = _FsTcpConnLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 1),
    _FsTcpConnLocalAddress_Type()
)
fsTcpConnLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTcpConnLocalAddress.setStatus("current")


class _FsTcpConnLocalPort_Type(Integer32):
    """Custom type fsTcpConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnLocalPort_Type.__name__ = "Integer32"
_FsTcpConnLocalPort_Object = MibTableColumn
fsTcpConnLocalPort = _FsTcpConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 2),
    _FsTcpConnLocalPort_Type()
)
fsTcpConnLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTcpConnLocalPort.setStatus("current")
_FsTcpConnRemAddress_Type = IpAddress
_FsTcpConnRemAddress_Object = MibTableColumn
fsTcpConnRemAddress = _FsTcpConnRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 3),
    _FsTcpConnRemAddress_Type()
)
fsTcpConnRemAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTcpConnRemAddress.setStatus("current")


class _FsTcpConnRemPort_Type(Integer32):
    """Custom type fsTcpConnRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnRemPort_Type.__name__ = "Integer32"
_FsTcpConnRemPort_Object = MibTableColumn
fsTcpConnRemPort = _FsTcpConnRemPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 4),
    _FsTcpConnRemPort_Type()
)
fsTcpConnRemPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTcpConnRemPort.setStatus("current")


class _FsTcpConnOutState_Type(Integer32):
    """Custom type fsTcpConnOutState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnOutState_Type.__name__ = "Integer32"
_FsTcpConnOutState_Object = MibTableColumn
fsTcpConnOutState = _FsTcpConnOutState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 5),
    _FsTcpConnOutState_Type()
)
fsTcpConnOutState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnOutState.setStatus("current")


class _FsTcpConnSWindow_Type(Integer32):
    """Custom type fsTcpConnSWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnSWindow_Type.__name__ = "Integer32"
_FsTcpConnSWindow_Object = MibTableColumn
fsTcpConnSWindow = _FsTcpConnSWindow_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 6),
    _FsTcpConnSWindow_Type()
)
fsTcpConnSWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnSWindow.setStatus("current")


class _FsTcpConnRWindow_Type(Integer32):
    """Custom type fsTcpConnRWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnRWindow_Type.__name__ = "Integer32"
_FsTcpConnRWindow_Object = MibTableColumn
fsTcpConnRWindow = _FsTcpConnRWindow_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 7),
    _FsTcpConnRWindow_Type()
)
fsTcpConnRWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnRWindow.setStatus("current")


class _FsTcpConnCWindow_Type(Integer32):
    """Custom type fsTcpConnCWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnCWindow_Type.__name__ = "Integer32"
_FsTcpConnCWindow_Object = MibTableColumn
fsTcpConnCWindow = _FsTcpConnCWindow_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 8),
    _FsTcpConnCWindow_Type()
)
fsTcpConnCWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnCWindow.setStatus("current")


class _FsTcpConnSSThresh_Type(Integer32):
    """Custom type fsTcpConnSSThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnSSThresh_Type.__name__ = "Integer32"
_FsTcpConnSSThresh_Object = MibTableColumn
fsTcpConnSSThresh = _FsTcpConnSSThresh_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 9),
    _FsTcpConnSSThresh_Type()
)
fsTcpConnSSThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnSSThresh.setStatus("current")


class _FsTcpConnSMSS_Type(Integer32):
    """Custom type fsTcpConnSMSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnSMSS_Type.__name__ = "Integer32"
_FsTcpConnSMSS_Object = MibTableColumn
fsTcpConnSMSS = _FsTcpConnSMSS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 10),
    _FsTcpConnSMSS_Type()
)
fsTcpConnSMSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnSMSS.setStatus("current")


class _FsTcpConnRMSS_Type(Integer32):
    """Custom type fsTcpConnRMSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnRMSS_Type.__name__ = "Integer32"
_FsTcpConnRMSS_Object = MibTableColumn
fsTcpConnRMSS = _FsTcpConnRMSS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 11),
    _FsTcpConnRMSS_Type()
)
fsTcpConnRMSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnRMSS.setStatus("current")


class _FsTcpConnSRT_Type(Integer32):
    """Custom type fsTcpConnSRT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnSRT_Type.__name__ = "Integer32"
_FsTcpConnSRT_Object = MibTableColumn
fsTcpConnSRT = _FsTcpConnSRT_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 12),
    _FsTcpConnSRT_Type()
)
fsTcpConnSRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnSRT.setStatus("current")


class _FsTcpConnRTDE_Type(Integer32):
    """Custom type fsTcpConnRTDE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnRTDE_Type.__name__ = "Integer32"
_FsTcpConnRTDE_Object = MibTableColumn
fsTcpConnRTDE = _FsTcpConnRTDE_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 13),
    _FsTcpConnRTDE_Type()
)
fsTcpConnRTDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnRTDE.setStatus("current")


class _FsTcpConnPersist_Type(Integer32):
    """Custom type fsTcpConnPersist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnPersist_Type.__name__ = "Integer32"
_FsTcpConnPersist_Object = MibTableColumn
fsTcpConnPersist = _FsTcpConnPersist_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 14),
    _FsTcpConnPersist_Type()
)
fsTcpConnPersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnPersist.setStatus("current")


class _FsTcpConnRexmt_Type(Integer32):
    """Custom type fsTcpConnRexmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnRexmt_Type.__name__ = "Integer32"
_FsTcpConnRexmt_Object = MibTableColumn
fsTcpConnRexmt = _FsTcpConnRexmt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 15),
    _FsTcpConnRexmt_Type()
)
fsTcpConnRexmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnRexmt.setStatus("current")


class _FsTcpConnRexmtCnt_Type(Integer32):
    """Custom type fsTcpConnRexmtCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnRexmtCnt_Type.__name__ = "Integer32"
_FsTcpConnRexmtCnt_Object = MibTableColumn
fsTcpConnRexmtCnt = _FsTcpConnRexmtCnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 16),
    _FsTcpConnRexmtCnt_Type()
)
fsTcpConnRexmtCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnRexmtCnt.setStatus("current")


class _FsTcpConnSBCount_Type(Integer32):
    """Custom type fsTcpConnSBCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnSBCount_Type.__name__ = "Integer32"
_FsTcpConnSBCount_Object = MibTableColumn
fsTcpConnSBCount = _FsTcpConnSBCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 17),
    _FsTcpConnSBCount_Type()
)
fsTcpConnSBCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnSBCount.setStatus("current")


class _FsTcpConnSBSize_Type(Integer32):
    """Custom type fsTcpConnSBSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnSBSize_Type.__name__ = "Integer32"
_FsTcpConnSBSize_Object = MibTableColumn
fsTcpConnSBSize = _FsTcpConnSBSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 18),
    _FsTcpConnSBSize_Type()
)
fsTcpConnSBSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnSBSize.setStatus("current")


class _FsTcpConnRBCount_Type(Integer32):
    """Custom type fsTcpConnRBCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnRBCount_Type.__name__ = "Integer32"
_FsTcpConnRBCount_Object = MibTableColumn
fsTcpConnRBCount = _FsTcpConnRBCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 19),
    _FsTcpConnRBCount_Type()
)
fsTcpConnRBCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnRBCount.setStatus("current")


class _FsTcpConnRBSize_Type(Integer32):
    """Custom type fsTcpConnRBSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnRBSize_Type.__name__ = "Integer32"
_FsTcpConnRBSize_Object = MibTableColumn
fsTcpConnRBSize = _FsTcpConnRBSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 20),
    _FsTcpConnRBSize_Type()
)
fsTcpConnRBSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnRBSize.setStatus("current")


class _FsTcpKaMainTmr_Type(Integer32):
    """Custom type fsTcpKaMainTmr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpKaMainTmr_Type.__name__ = "Integer32"
_FsTcpKaMainTmr_Object = MibTableColumn
fsTcpKaMainTmr = _FsTcpKaMainTmr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 21),
    _FsTcpKaMainTmr_Type()
)
fsTcpKaMainTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTcpKaMainTmr.setStatus("current")


class _FsTcpKaRetransTmr_Type(Integer32):
    """Custom type fsTcpKaRetransTmr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsTcpKaRetransTmr_Type.__name__ = "Integer32"
_FsTcpKaRetransTmr_Object = MibTableColumn
fsTcpKaRetransTmr = _FsTcpKaRetransTmr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 22),
    _FsTcpKaRetransTmr_Type()
)
fsTcpKaRetransTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTcpKaRetransTmr.setStatus("current")


class _FsTcpKaRetransCnt_Type(Integer32):
    """Custom type fsTcpKaRetransCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsTcpKaRetransCnt_Type.__name__ = "Integer32"
_FsTcpKaRetransCnt_Object = MibTableColumn
fsTcpKaRetransCnt = _FsTcpKaRetransCnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 7, 1, 23),
    _FsTcpKaRetransCnt_Type()
)
fsTcpKaRetransCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTcpKaRetransCnt.setStatus("current")
_FsTcpExtConnTable_Object = MibTable
fsTcpExtConnTable = _FsTcpExtConnTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 8)
)
if mibBuilder.loadTexts:
    fsTcpExtConnTable.setStatus("current")
_FsTcpExtConnEntry_Object = MibTableRow
fsTcpExtConnEntry = _FsTcpExtConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 8, 1)
)
if mibBuilder.loadTexts:
    fsTcpExtConnEntry.setStatus("current")
_FsTcpConnMD5Option_Type = TruthValue
_FsTcpConnMD5Option_Object = MibTableColumn
fsTcpConnMD5Option = _FsTcpConnMD5Option_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 8, 1, 1),
    _FsTcpConnMD5Option_Type()
)
fsTcpConnMD5Option.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnMD5Option.setStatus("current")


class _FsTcpConnMD5ErrCtr_Type(Integer32):
    """Custom type fsTcpConnMD5ErrCtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTcpConnMD5ErrCtr_Type.__name__ = "Integer32"
_FsTcpConnMD5ErrCtr_Object = MibTableColumn
fsTcpConnMD5ErrCtr = _FsTcpConnMD5ErrCtr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 8, 1, 2),
    _FsTcpConnMD5ErrCtr_Type()
)
fsTcpConnMD5ErrCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnMD5ErrCtr.setStatus("current")
_FsTcpConnTcpAOOption_Type = TruthValue
_FsTcpConnTcpAOOption_Object = MibTableColumn
fsTcpConnTcpAOOption = _FsTcpConnTcpAOOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 8, 1, 3),
    _FsTcpConnTcpAOOption_Type()
)
fsTcpConnTcpAOOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConnTcpAOOption.setStatus("current")


class _FsTcpConTcpAOCurKeyId_Type(Integer32):
    """Custom type fsTcpConTcpAOCurKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsTcpConTcpAOCurKeyId_Type.__name__ = "Integer32"
_FsTcpConTcpAOCurKeyId_Object = MibTableColumn
fsTcpConTcpAOCurKeyId = _FsTcpConTcpAOCurKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 8, 1, 4),
    _FsTcpConTcpAOCurKeyId_Type()
)
fsTcpConTcpAOCurKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConTcpAOCurKeyId.setStatus("current")


class _FsTcpConTcpAORnextKeyId_Type(Integer32):
    """Custom type fsTcpConTcpAORnextKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsTcpConTcpAORnextKeyId_Type.__name__ = "Integer32"
_FsTcpConTcpAORnextKeyId_Object = MibTableColumn
fsTcpConTcpAORnextKeyId = _FsTcpConTcpAORnextKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 8, 1, 5),
    _FsTcpConTcpAORnextKeyId_Type()
)
fsTcpConTcpAORnextKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConTcpAORnextKeyId.setStatus("current")


class _FsTcpConTcpAORcvKeyId_Type(Integer32):
    """Custom type fsTcpConTcpAORcvKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsTcpConTcpAORcvKeyId_Type.__name__ = "Integer32"
_FsTcpConTcpAORcvKeyId_Object = MibTableColumn
fsTcpConTcpAORcvKeyId = _FsTcpConTcpAORcvKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 8, 1, 6),
    _FsTcpConTcpAORcvKeyId_Type()
)
fsTcpConTcpAORcvKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConTcpAORcvKeyId.setStatus("current")


class _FsTcpConTcpAORcvRnextKeyId_Type(Integer32):
    """Custom type fsTcpConTcpAORcvRnextKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsTcpConTcpAORcvRnextKeyId_Type.__name__ = "Integer32"
_FsTcpConTcpAORcvRnextKeyId_Object = MibTableColumn
fsTcpConTcpAORcvRnextKeyId = _FsTcpConTcpAORcvRnextKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 8, 1, 7),
    _FsTcpConTcpAORcvRnextKeyId_Type()
)
fsTcpConTcpAORcvRnextKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConTcpAORcvRnextKeyId.setStatus("current")
_FsTcpConTcpAOConnErrCtr_Type = Counter32
_FsTcpConTcpAOConnErrCtr_Object = MibTableColumn
fsTcpConTcpAOConnErrCtr = _FsTcpConTcpAOConnErrCtr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 8, 1, 8),
    _FsTcpConTcpAOConnErrCtr_Type()
)
fsTcpConTcpAOConnErrCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConTcpAOConnErrCtr.setStatus("current")
_FsTcpConTcpAOSndSne_Type = Integer32
_FsTcpConTcpAOSndSne_Object = MibTableColumn
fsTcpConTcpAOSndSne = _FsTcpConTcpAOSndSne_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 8, 1, 9),
    _FsTcpConTcpAOSndSne_Type()
)
fsTcpConTcpAOSndSne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConTcpAOSndSne.setStatus("current")
_FsTcpConTcpAORcvSne_Type = Integer32
_FsTcpConTcpAORcvSne_Object = MibTableColumn
fsTcpConTcpAORcvSne = _FsTcpConTcpAORcvSne_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 8, 1, 10),
    _FsTcpConTcpAORcvSne_Type()
)
fsTcpConTcpAORcvSne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConTcpAORcvSne.setStatus("current")


class _FsTcpMaxReTries_Type(Integer32):
    """Custom type fsTcpMaxReTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_FsTcpMaxReTries_Type.__name__ = "Integer32"
_FsTcpMaxReTries_Object = MibScalar
fsTcpMaxReTries = _FsTcpMaxReTries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 9),
    _FsTcpMaxReTries_Type()
)
fsTcpMaxReTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTcpMaxReTries.setStatus("current")


class _FsTcpTrapAdminStatus_Type(Integer32):
    """Custom type fsTcpTrapAdminStatus based on Integer32"""
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


_FsTcpTrapAdminStatus_Type.__name__ = "Integer32"
_FsTcpTrapAdminStatus_Object = MibScalar
fsTcpTrapAdminStatus = _FsTcpTrapAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 10),
    _FsTcpTrapAdminStatus_Type()
)
fsTcpTrapAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTcpTrapAdminStatus.setStatus("current")
_FstcpNotification_ObjectIdentity = ObjectIdentity
fstcpNotification = _FstcpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 11)
)
_FstcpTrap_ObjectIdentity = ObjectIdentity
fstcpTrap = _FstcpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 11, 0)
)
_FstcpObjects_ObjectIdentity = ObjectIdentity
fstcpObjects = _FstcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 11, 1)
)
_FstcpAoLocalAddressType_Type = InetAddressType
_FstcpAoLocalAddressType_Object = MibScalar
fstcpAoLocalAddressType = _FstcpAoLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 11, 1, 1),
    _FstcpAoLocalAddressType_Type()
)
fstcpAoLocalAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fstcpAoLocalAddressType.setStatus("current")
_FstcpAoLocalAddress_Type = InetAddress
_FstcpAoLocalAddress_Object = MibScalar
fstcpAoLocalAddress = _FstcpAoLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 11, 1, 2),
    _FstcpAoLocalAddress_Type()
)
fstcpAoLocalAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fstcpAoLocalAddress.setStatus("current")
_FstcpAoLocalPort_Type = InetPortNumber
_FstcpAoLocalPort_Object = MibScalar
fstcpAoLocalPort = _FstcpAoLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 11, 1, 3),
    _FstcpAoLocalPort_Type()
)
fstcpAoLocalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fstcpAoLocalPort.setStatus("current")
_FstcpAoRemAddressType_Type = InetAddressType
_FstcpAoRemAddressType_Object = MibScalar
fstcpAoRemAddressType = _FstcpAoRemAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 11, 1, 4),
    _FstcpAoRemAddressType_Type()
)
fstcpAoRemAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fstcpAoRemAddressType.setStatus("current")
_FstcpAoRemAddress_Type = InetAddress
_FstcpAoRemAddress_Object = MibScalar
fstcpAoRemAddress = _FstcpAoRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 11, 1, 5),
    _FstcpAoRemAddress_Type()
)
fstcpAoRemAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fstcpAoRemAddress.setStatus("current")
_FstcpAoRemPort_Type = InetPortNumber
_FstcpAoRemPort_Object = MibScalar
fstcpAoRemPort = _FstcpAoRemPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 11, 1, 6),
    _FstcpAoRemPort_Type()
)
fstcpAoRemPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fstcpAoRemPort.setStatus("current")
_FsTcpAoConnTestTable_Object = MibTable
fsTcpAoConnTestTable = _FsTcpAoConnTestTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 12)
)
if mibBuilder.loadTexts:
    fsTcpAoConnTestTable.setStatus("current")
_FsTcpAoConnTestEntry_Object = MibTableRow
fsTcpAoConnTestEntry = _FsTcpAoConnTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 12, 1)
)
fsTcpAoConnTestEntry.setIndexNames(
    (0, "SUPERMICRO-TCP-MIB", "fsTcpAoConnTestLclAdrType"),
    (0, "SUPERMICRO-TCP-MIB", "fsTcpAoConnTestLclAdress"),
    (0, "SUPERMICRO-TCP-MIB", "fsTcpAoConnTestLclPort"),
    (0, "SUPERMICRO-TCP-MIB", "fsTcpAoConnTestRmtAdrType"),
    (0, "SUPERMICRO-TCP-MIB", "fsTcpAoConnTestRmtAdress"),
    (0, "SUPERMICRO-TCP-MIB", "fsTcpAoConnTestRmtPort"),
)
if mibBuilder.loadTexts:
    fsTcpAoConnTestEntry.setStatus("current")
_FsTcpAoConnTestLclAdrType_Type = InetAddressType
_FsTcpAoConnTestLclAdrType_Object = MibTableColumn
fsTcpAoConnTestLclAdrType = _FsTcpAoConnTestLclAdrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 12, 1, 1),
    _FsTcpAoConnTestLclAdrType_Type()
)
fsTcpAoConnTestLclAdrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTcpAoConnTestLclAdrType.setStatus("current")
_FsTcpAoConnTestLclAdress_Type = InetAddress
_FsTcpAoConnTestLclAdress_Object = MibTableColumn
fsTcpAoConnTestLclAdress = _FsTcpAoConnTestLclAdress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 12, 1, 2),
    _FsTcpAoConnTestLclAdress_Type()
)
fsTcpAoConnTestLclAdress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTcpAoConnTestLclAdress.setStatus("current")
_FsTcpAoConnTestLclPort_Type = InetPortNumber
_FsTcpAoConnTestLclPort_Object = MibTableColumn
fsTcpAoConnTestLclPort = _FsTcpAoConnTestLclPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 12, 1, 3),
    _FsTcpAoConnTestLclPort_Type()
)
fsTcpAoConnTestLclPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTcpAoConnTestLclPort.setStatus("current")
_FsTcpAoConnTestRmtAdrType_Type = InetAddressType
_FsTcpAoConnTestRmtAdrType_Object = MibTableColumn
fsTcpAoConnTestRmtAdrType = _FsTcpAoConnTestRmtAdrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 12, 1, 4),
    _FsTcpAoConnTestRmtAdrType_Type()
)
fsTcpAoConnTestRmtAdrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTcpAoConnTestRmtAdrType.setStatus("current")
_FsTcpAoConnTestRmtAdress_Type = InetAddress
_FsTcpAoConnTestRmtAdress_Object = MibTableColumn
fsTcpAoConnTestRmtAdress = _FsTcpAoConnTestRmtAdress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 12, 1, 5),
    _FsTcpAoConnTestRmtAdress_Type()
)
fsTcpAoConnTestRmtAdress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTcpAoConnTestRmtAdress.setStatus("current")
_FsTcpAoConnTestRmtPort_Type = InetPortNumber
_FsTcpAoConnTestRmtPort_Object = MibTableColumn
fsTcpAoConnTestRmtPort = _FsTcpAoConnTestRmtPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 12, 1, 6),
    _FsTcpAoConnTestRmtPort_Type()
)
fsTcpAoConnTestRmtPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTcpAoConnTestRmtPort.setStatus("current")
_FsTcpConTcpAOIcmpIgnCtr_Type = Counter32
_FsTcpConTcpAOIcmpIgnCtr_Object = MibTableColumn
fsTcpConTcpAOIcmpIgnCtr = _FsTcpConTcpAOIcmpIgnCtr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 12, 1, 7),
    _FsTcpConTcpAOIcmpIgnCtr_Type()
)
fsTcpConTcpAOIcmpIgnCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConTcpAOIcmpIgnCtr.setStatus("current")
_FsTcpConTcpAOSilentAccptCtr_Type = Counter32
_FsTcpConTcpAOSilentAccptCtr_Object = MibTableColumn
fsTcpConTcpAOSilentAccptCtr = _FsTcpConTcpAOSilentAccptCtr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 12, 1, 8),
    _FsTcpConTcpAOSilentAccptCtr_Type()
)
fsTcpConTcpAOSilentAccptCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTcpConTcpAOSilentAccptCtr.setStatus("current")
tcpConnectionEntry.registerAugmentions(
    ("SUPERMICRO-TCP-MIB",
     "fsTcpExtConnEntry")
)
fsTcpExtConnEntry.setIndexNames(*tcpConnectionEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fstcpAoAuthError = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 18, 11, 0, 1)
)
fstcpAoAuthError.setObjects(
      *(("SUPERMICRO-TCP-MIB", "fstcpAoLocalAddressType"),
        ("SUPERMICRO-TCP-MIB", "fstcpAoLocalAddress"),
        ("SUPERMICRO-TCP-MIB", "fstcpAoLocalPort"),
        ("SUPERMICRO-TCP-MIB", "fstcpAoRemAddressType"),
        ("SUPERMICRO-TCP-MIB", "fstcpAoRemAddress"),
        ("SUPERMICRO-TCP-MIB", "tcpConnectionRemPort"),
        ("SUPERMICRO-TCP-MIB", "fsTcpConTcpAOConnErrCtr"))
)
if mibBuilder.loadTexts:
    fstcpAoAuthError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-TCP-MIB",
    **{"fstcp": fstcp,
       "fsTcpAckOption": fsTcpAckOption,
       "fsTcpTimeStampOption": fsTcpTimeStampOption,
       "fsTcpBigWndOption": fsTcpBigWndOption,
       "fsTcpIncrIniWnd": fsTcpIncrIniWnd,
       "fsTcpMaxNumOfTCB": fsTcpMaxNumOfTCB,
       "fsTcpTraceDebug": fsTcpTraceDebug,
       "fsTcpConnTable": fsTcpConnTable,
       "fsTcpConnEntry": fsTcpConnEntry,
       "fsTcpConnLocalAddress": fsTcpConnLocalAddress,
       "fsTcpConnLocalPort": fsTcpConnLocalPort,
       "fsTcpConnRemAddress": fsTcpConnRemAddress,
       "fsTcpConnRemPort": fsTcpConnRemPort,
       "fsTcpConnOutState": fsTcpConnOutState,
       "fsTcpConnSWindow": fsTcpConnSWindow,
       "fsTcpConnRWindow": fsTcpConnRWindow,
       "fsTcpConnCWindow": fsTcpConnCWindow,
       "fsTcpConnSSThresh": fsTcpConnSSThresh,
       "fsTcpConnSMSS": fsTcpConnSMSS,
       "fsTcpConnRMSS": fsTcpConnRMSS,
       "fsTcpConnSRT": fsTcpConnSRT,
       "fsTcpConnRTDE": fsTcpConnRTDE,
       "fsTcpConnPersist": fsTcpConnPersist,
       "fsTcpConnRexmt": fsTcpConnRexmt,
       "fsTcpConnRexmtCnt": fsTcpConnRexmtCnt,
       "fsTcpConnSBCount": fsTcpConnSBCount,
       "fsTcpConnSBSize": fsTcpConnSBSize,
       "fsTcpConnRBCount": fsTcpConnRBCount,
       "fsTcpConnRBSize": fsTcpConnRBSize,
       "fsTcpKaMainTmr": fsTcpKaMainTmr,
       "fsTcpKaRetransTmr": fsTcpKaRetransTmr,
       "fsTcpKaRetransCnt": fsTcpKaRetransCnt,
       "fsTcpExtConnTable": fsTcpExtConnTable,
       "fsTcpExtConnEntry": fsTcpExtConnEntry,
       "fsTcpConnMD5Option": fsTcpConnMD5Option,
       "fsTcpConnMD5ErrCtr": fsTcpConnMD5ErrCtr,
       "fsTcpConnTcpAOOption": fsTcpConnTcpAOOption,
       "fsTcpConTcpAOCurKeyId": fsTcpConTcpAOCurKeyId,
       "fsTcpConTcpAORnextKeyId": fsTcpConTcpAORnextKeyId,
       "fsTcpConTcpAORcvKeyId": fsTcpConTcpAORcvKeyId,
       "fsTcpConTcpAORcvRnextKeyId": fsTcpConTcpAORcvRnextKeyId,
       "fsTcpConTcpAOConnErrCtr": fsTcpConTcpAOConnErrCtr,
       "fsTcpConTcpAOSndSne": fsTcpConTcpAOSndSne,
       "fsTcpConTcpAORcvSne": fsTcpConTcpAORcvSne,
       "fsTcpMaxReTries": fsTcpMaxReTries,
       "fsTcpTrapAdminStatus": fsTcpTrapAdminStatus,
       "fstcpNotification": fstcpNotification,
       "fstcpTrap": fstcpTrap,
       "fstcpAoAuthError": fstcpAoAuthError,
       "fstcpObjects": fstcpObjects,
       "fstcpAoLocalAddressType": fstcpAoLocalAddressType,
       "fstcpAoLocalAddress": fstcpAoLocalAddress,
       "fstcpAoLocalPort": fstcpAoLocalPort,
       "fstcpAoRemAddressType": fstcpAoRemAddressType,
       "fstcpAoRemAddress": fstcpAoRemAddress,
       "fstcpAoRemPort": fstcpAoRemPort,
       "fsTcpAoConnTestTable": fsTcpAoConnTestTable,
       "fsTcpAoConnTestEntry": fsTcpAoConnTestEntry,
       "fsTcpAoConnTestLclAdrType": fsTcpAoConnTestLclAdrType,
       "fsTcpAoConnTestLclAdress": fsTcpAoConnTestLclAdress,
       "fsTcpAoConnTestLclPort": fsTcpAoConnTestLclPort,
       "fsTcpAoConnTestRmtAdrType": fsTcpAoConnTestRmtAdrType,
       "fsTcpAoConnTestRmtAdress": fsTcpAoConnTestRmtAdress,
       "fsTcpAoConnTestRmtPort": fsTcpAoConnTestRmtPort,
       "fsTcpConTcpAOIcmpIgnCtr": fsTcpConTcpAOIcmpIgnCtr,
       "fsTcpConTcpAOSilentAccptCtr": fsTcpConTcpAOSilentAccptCtr}
)
