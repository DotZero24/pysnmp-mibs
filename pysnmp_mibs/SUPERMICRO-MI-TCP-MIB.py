# SNMP MIB module (SUPERMICRO-MI-TCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-MI-TCP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:44 2025
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

(fsMIStdTcpConnectionEntry,) = mibBuilder.importSymbols(
    "SUPERMICRO-MI-TCP-IPVX-MIB",
    "fsMIStdTcpConnectionEntry")


# MODULE-IDENTITY

fsMITcp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMITcpGlobalTraceDebug_Type = Integer32
_FsMITcpGlobalTraceDebug_Object = MibScalar
fsMITcpGlobalTraceDebug = _FsMITcpGlobalTraceDebug_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 1),
    _FsMITcpGlobalTraceDebug_Type()
)
fsMITcpGlobalTraceDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITcpGlobalTraceDebug.setStatus("current")
_FsMIContextTable_Object = MibTable
fsMIContextTable = _FsMIContextTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 2)
)
if mibBuilder.loadTexts:
    fsMIContextTable.setStatus("current")
_FsMIContextEntry_Object = MibTableRow
fsMIContextEntry = _FsMIContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 2, 1)
)
fsMIContextEntry.setIndexNames(
    (0, "SUPERMICRO-MI-TCP-MIB", "fsMITcpContextId"),
)
if mibBuilder.loadTexts:
    fsMIContextEntry.setStatus("current")


class _FsMITcpContextId_Type(Integer32):
    """Custom type fsMITcpContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpContextId_Type.__name__ = "Integer32"
_FsMITcpContextId_Object = MibTableColumn
fsMITcpContextId = _FsMITcpContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 2, 1, 1),
    _FsMITcpContextId_Type()
)
fsMITcpContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMITcpContextId.setStatus("current")


class _FsMITcpAckOption_Type(Integer32):
    """Custom type fsMITcpAckOption based on Integer32"""
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


_FsMITcpAckOption_Type.__name__ = "Integer32"
_FsMITcpAckOption_Object = MibTableColumn
fsMITcpAckOption = _FsMITcpAckOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 2, 1, 2),
    _FsMITcpAckOption_Type()
)
fsMITcpAckOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITcpAckOption.setStatus("current")
_FsMITcpTimeStampOption_Type = TruthValue
_FsMITcpTimeStampOption_Object = MibTableColumn
fsMITcpTimeStampOption = _FsMITcpTimeStampOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 2, 1, 3),
    _FsMITcpTimeStampOption_Type()
)
fsMITcpTimeStampOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITcpTimeStampOption.setStatus("current")
_FsMITcpBigWndOption_Type = TruthValue
_FsMITcpBigWndOption_Object = MibTableColumn
fsMITcpBigWndOption = _FsMITcpBigWndOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 2, 1, 4),
    _FsMITcpBigWndOption_Type()
)
fsMITcpBigWndOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITcpBigWndOption.setStatus("current")
_FsMITcpIncrIniWnd_Type = TruthValue
_FsMITcpIncrIniWnd_Object = MibTableColumn
fsMITcpIncrIniWnd = _FsMITcpIncrIniWnd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 2, 1, 5),
    _FsMITcpIncrIniWnd_Type()
)
fsMITcpIncrIniWnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITcpIncrIniWnd.setStatus("current")
_FsMITcpMaxNumOfTCB_Type = Integer32
_FsMITcpMaxNumOfTCB_Object = MibTableColumn
fsMITcpMaxNumOfTCB = _FsMITcpMaxNumOfTCB_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 2, 1, 6),
    _FsMITcpMaxNumOfTCB_Type()
)
fsMITcpMaxNumOfTCB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITcpMaxNumOfTCB.setStatus("current")
_FsMITcpTraceDebug_Type = Integer32
_FsMITcpTraceDebug_Object = MibTableColumn
fsMITcpTraceDebug = _FsMITcpTraceDebug_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 2, 1, 7),
    _FsMITcpTraceDebug_Type()
)
fsMITcpTraceDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITcpTraceDebug.setStatus("current")


class _FsMITcpMaxReTries_Type(Integer32):
    """Custom type fsMITcpMaxReTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_FsMITcpMaxReTries_Type.__name__ = "Integer32"
_FsMITcpMaxReTries_Object = MibTableColumn
fsMITcpMaxReTries = _FsMITcpMaxReTries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 2, 1, 8),
    _FsMITcpMaxReTries_Type()
)
fsMITcpMaxReTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITcpMaxReTries.setStatus("current")


class _FsMITcpClearStatistics_Type(Integer32):
    """Custom type fsMITcpClearStatistics based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsMITcpClearStatistics_Type.__name__ = "Integer32"
_FsMITcpClearStatistics_Object = MibTableColumn
fsMITcpClearStatistics = _FsMITcpClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 2, 1, 9),
    _FsMITcpClearStatistics_Type()
)
fsMITcpClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITcpClearStatistics.setStatus("current")


class _FsMITcpTrapAdminStatus_Type(Integer32):
    """Custom type fsMITcpTrapAdminStatus based on Integer32"""
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


_FsMITcpTrapAdminStatus_Type.__name__ = "Integer32"
_FsMITcpTrapAdminStatus_Object = MibTableColumn
fsMITcpTrapAdminStatus = _FsMITcpTrapAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 2, 1, 10),
    _FsMITcpTrapAdminStatus_Type()
)
fsMITcpTrapAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITcpTrapAdminStatus.setStatus("current")
_FsMITcpConnTable_Object = MibTable
fsMITcpConnTable = _FsMITcpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3)
)
if mibBuilder.loadTexts:
    fsMITcpConnTable.setStatus("current")
_FsMITcpConnEntry_Object = MibTableRow
fsMITcpConnEntry = _FsMITcpConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1)
)
fsMITcpConnEntry.setIndexNames(
    (0, "SUPERMICRO-MI-TCP-MIB", "fsMITcpContextId"),
    (0, "SUPERMICRO-MI-TCP-MIB", "fsMITcpConnLocalAddress"),
    (0, "SUPERMICRO-MI-TCP-MIB", "fsMITcpConnLocalPort"),
    (0, "SUPERMICRO-MI-TCP-MIB", "fsMITcpConnRemAddress"),
    (0, "SUPERMICRO-MI-TCP-MIB", "fsMITcpConnRemPort"),
)
if mibBuilder.loadTexts:
    fsMITcpConnEntry.setStatus("current")
_FsMITcpConnLocalAddress_Type = IpAddress
_FsMITcpConnLocalAddress_Object = MibTableColumn
fsMITcpConnLocalAddress = _FsMITcpConnLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 2),
    _FsMITcpConnLocalAddress_Type()
)
fsMITcpConnLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMITcpConnLocalAddress.setStatus("current")


class _FsMITcpConnLocalPort_Type(Integer32):
    """Custom type fsMITcpConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnLocalPort_Type.__name__ = "Integer32"
_FsMITcpConnLocalPort_Object = MibTableColumn
fsMITcpConnLocalPort = _FsMITcpConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 3),
    _FsMITcpConnLocalPort_Type()
)
fsMITcpConnLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMITcpConnLocalPort.setStatus("current")
_FsMITcpConnRemAddress_Type = IpAddress
_FsMITcpConnRemAddress_Object = MibTableColumn
fsMITcpConnRemAddress = _FsMITcpConnRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 4),
    _FsMITcpConnRemAddress_Type()
)
fsMITcpConnRemAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMITcpConnRemAddress.setStatus("current")


class _FsMITcpConnRemPort_Type(Integer32):
    """Custom type fsMITcpConnRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnRemPort_Type.__name__ = "Integer32"
_FsMITcpConnRemPort_Object = MibTableColumn
fsMITcpConnRemPort = _FsMITcpConnRemPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 5),
    _FsMITcpConnRemPort_Type()
)
fsMITcpConnRemPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMITcpConnRemPort.setStatus("current")


class _FsMITcpConnOutState_Type(Integer32):
    """Custom type fsMITcpConnOutState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnOutState_Type.__name__ = "Integer32"
_FsMITcpConnOutState_Object = MibTableColumn
fsMITcpConnOutState = _FsMITcpConnOutState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 6),
    _FsMITcpConnOutState_Type()
)
fsMITcpConnOutState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnOutState.setStatus("current")


class _FsMITcpConnSWindow_Type(Integer32):
    """Custom type fsMITcpConnSWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnSWindow_Type.__name__ = "Integer32"
_FsMITcpConnSWindow_Object = MibTableColumn
fsMITcpConnSWindow = _FsMITcpConnSWindow_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 7),
    _FsMITcpConnSWindow_Type()
)
fsMITcpConnSWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnSWindow.setStatus("current")


class _FsMITcpConnRWindow_Type(Integer32):
    """Custom type fsMITcpConnRWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnRWindow_Type.__name__ = "Integer32"
_FsMITcpConnRWindow_Object = MibTableColumn
fsMITcpConnRWindow = _FsMITcpConnRWindow_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 8),
    _FsMITcpConnRWindow_Type()
)
fsMITcpConnRWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnRWindow.setStatus("current")


class _FsMITcpConnCWindow_Type(Integer32):
    """Custom type fsMITcpConnCWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnCWindow_Type.__name__ = "Integer32"
_FsMITcpConnCWindow_Object = MibTableColumn
fsMITcpConnCWindow = _FsMITcpConnCWindow_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 9),
    _FsMITcpConnCWindow_Type()
)
fsMITcpConnCWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnCWindow.setStatus("current")


class _FsMITcpConnSSThresh_Type(Integer32):
    """Custom type fsMITcpConnSSThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnSSThresh_Type.__name__ = "Integer32"
_FsMITcpConnSSThresh_Object = MibTableColumn
fsMITcpConnSSThresh = _FsMITcpConnSSThresh_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 10),
    _FsMITcpConnSSThresh_Type()
)
fsMITcpConnSSThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnSSThresh.setStatus("current")


class _FsMITcpConnSMSS_Type(Integer32):
    """Custom type fsMITcpConnSMSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnSMSS_Type.__name__ = "Integer32"
_FsMITcpConnSMSS_Object = MibTableColumn
fsMITcpConnSMSS = _FsMITcpConnSMSS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 11),
    _FsMITcpConnSMSS_Type()
)
fsMITcpConnSMSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnSMSS.setStatus("current")


class _FsMITcpConnRMSS_Type(Integer32):
    """Custom type fsMITcpConnRMSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnRMSS_Type.__name__ = "Integer32"
_FsMITcpConnRMSS_Object = MibTableColumn
fsMITcpConnRMSS = _FsMITcpConnRMSS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 12),
    _FsMITcpConnRMSS_Type()
)
fsMITcpConnRMSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnRMSS.setStatus("current")


class _FsMITcpConnSRT_Type(Integer32):
    """Custom type fsMITcpConnSRT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnSRT_Type.__name__ = "Integer32"
_FsMITcpConnSRT_Object = MibTableColumn
fsMITcpConnSRT = _FsMITcpConnSRT_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 13),
    _FsMITcpConnSRT_Type()
)
fsMITcpConnSRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnSRT.setStatus("current")


class _FsMITcpConnRTDE_Type(Integer32):
    """Custom type fsMITcpConnRTDE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnRTDE_Type.__name__ = "Integer32"
_FsMITcpConnRTDE_Object = MibTableColumn
fsMITcpConnRTDE = _FsMITcpConnRTDE_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 14),
    _FsMITcpConnRTDE_Type()
)
fsMITcpConnRTDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnRTDE.setStatus("current")


class _FsMITcpConnPersist_Type(Integer32):
    """Custom type fsMITcpConnPersist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnPersist_Type.__name__ = "Integer32"
_FsMITcpConnPersist_Object = MibTableColumn
fsMITcpConnPersist = _FsMITcpConnPersist_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 15),
    _FsMITcpConnPersist_Type()
)
fsMITcpConnPersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnPersist.setStatus("current")


class _FsMITcpConnRexmt_Type(Integer32):
    """Custom type fsMITcpConnRexmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnRexmt_Type.__name__ = "Integer32"
_FsMITcpConnRexmt_Object = MibTableColumn
fsMITcpConnRexmt = _FsMITcpConnRexmt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 16),
    _FsMITcpConnRexmt_Type()
)
fsMITcpConnRexmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnRexmt.setStatus("current")


class _FsMITcpConnRexmtCnt_Type(Integer32):
    """Custom type fsMITcpConnRexmtCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnRexmtCnt_Type.__name__ = "Integer32"
_FsMITcpConnRexmtCnt_Object = MibTableColumn
fsMITcpConnRexmtCnt = _FsMITcpConnRexmtCnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 17),
    _FsMITcpConnRexmtCnt_Type()
)
fsMITcpConnRexmtCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnRexmtCnt.setStatus("current")


class _FsMITcpConnSBCount_Type(Integer32):
    """Custom type fsMITcpConnSBCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnSBCount_Type.__name__ = "Integer32"
_FsMITcpConnSBCount_Object = MibTableColumn
fsMITcpConnSBCount = _FsMITcpConnSBCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 18),
    _FsMITcpConnSBCount_Type()
)
fsMITcpConnSBCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnSBCount.setStatus("current")


class _FsMITcpConnSBSize_Type(Integer32):
    """Custom type fsMITcpConnSBSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnSBSize_Type.__name__ = "Integer32"
_FsMITcpConnSBSize_Object = MibTableColumn
fsMITcpConnSBSize = _FsMITcpConnSBSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 19),
    _FsMITcpConnSBSize_Type()
)
fsMITcpConnSBSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnSBSize.setStatus("current")


class _FsMITcpConnRBCount_Type(Integer32):
    """Custom type fsMITcpConnRBCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnRBCount_Type.__name__ = "Integer32"
_FsMITcpConnRBCount_Object = MibTableColumn
fsMITcpConnRBCount = _FsMITcpConnRBCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 20),
    _FsMITcpConnRBCount_Type()
)
fsMITcpConnRBCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnRBCount.setStatus("current")


class _FsMITcpConnRBSize_Type(Integer32):
    """Custom type fsMITcpConnRBSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnRBSize_Type.__name__ = "Integer32"
_FsMITcpConnRBSize_Object = MibTableColumn
fsMITcpConnRBSize = _FsMITcpConnRBSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 21),
    _FsMITcpConnRBSize_Type()
)
fsMITcpConnRBSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnRBSize.setStatus("current")


class _FsMITcpKaMainTmr_Type(Integer32):
    """Custom type fsMITcpKaMainTmr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpKaMainTmr_Type.__name__ = "Integer32"
_FsMITcpKaMainTmr_Object = MibTableColumn
fsMITcpKaMainTmr = _FsMITcpKaMainTmr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 22),
    _FsMITcpKaMainTmr_Type()
)
fsMITcpKaMainTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITcpKaMainTmr.setStatus("current")


class _FsMITcpKaRetransTmr_Type(Integer32):
    """Custom type fsMITcpKaRetransTmr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMITcpKaRetransTmr_Type.__name__ = "Integer32"
_FsMITcpKaRetransTmr_Object = MibTableColumn
fsMITcpKaRetransTmr = _FsMITcpKaRetransTmr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 23),
    _FsMITcpKaRetransTmr_Type()
)
fsMITcpKaRetransTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITcpKaRetransTmr.setStatus("current")


class _FsMITcpKaRetransCnt_Type(Integer32):
    """Custom type fsMITcpKaRetransCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMITcpKaRetransCnt_Type.__name__ = "Integer32"
_FsMITcpKaRetransCnt_Object = MibTableColumn
fsMITcpKaRetransCnt = _FsMITcpKaRetransCnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 3, 1, 24),
    _FsMITcpKaRetransCnt_Type()
)
fsMITcpKaRetransCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMITcpKaRetransCnt.setStatus("current")
_FsMITcpExtConnTable_Object = MibTable
fsMITcpExtConnTable = _FsMITcpExtConnTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 4)
)
if mibBuilder.loadTexts:
    fsMITcpExtConnTable.setStatus("current")
_FsMITcpExtConnEntry_Object = MibTableRow
fsMITcpExtConnEntry = _FsMITcpExtConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 4, 1)
)
if mibBuilder.loadTexts:
    fsMITcpExtConnEntry.setStatus("current")
_FsMITcpConnMD5Option_Type = TruthValue
_FsMITcpConnMD5Option_Object = MibTableColumn
fsMITcpConnMD5Option = _FsMITcpConnMD5Option_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 4, 1, 1),
    _FsMITcpConnMD5Option_Type()
)
fsMITcpConnMD5Option.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnMD5Option.setStatus("current")


class _FsMITcpConnMD5ErrCtr_Type(Integer32):
    """Custom type fsMITcpConnMD5ErrCtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMITcpConnMD5ErrCtr_Type.__name__ = "Integer32"
_FsMITcpConnMD5ErrCtr_Object = MibTableColumn
fsMITcpConnMD5ErrCtr = _FsMITcpConnMD5ErrCtr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 4, 1, 2),
    _FsMITcpConnMD5ErrCtr_Type()
)
fsMITcpConnMD5ErrCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnMD5ErrCtr.setStatus("current")
_FsMITcpConnTcpAOOption_Type = TruthValue
_FsMITcpConnTcpAOOption_Object = MibTableColumn
fsMITcpConnTcpAOOption = _FsMITcpConnTcpAOOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 4, 1, 3),
    _FsMITcpConnTcpAOOption_Type()
)
fsMITcpConnTcpAOOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConnTcpAOOption.setStatus("current")


class _FsMITcpConTcpAOCurKeyId_Type(Integer32):
    """Custom type fsMITcpConTcpAOCurKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMITcpConTcpAOCurKeyId_Type.__name__ = "Integer32"
_FsMITcpConTcpAOCurKeyId_Object = MibTableColumn
fsMITcpConTcpAOCurKeyId = _FsMITcpConTcpAOCurKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 4, 1, 4),
    _FsMITcpConTcpAOCurKeyId_Type()
)
fsMITcpConTcpAOCurKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConTcpAOCurKeyId.setStatus("current")


class _FsMITcpConTcpAORnextKeyId_Type(Integer32):
    """Custom type fsMITcpConTcpAORnextKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMITcpConTcpAORnextKeyId_Type.__name__ = "Integer32"
_FsMITcpConTcpAORnextKeyId_Object = MibTableColumn
fsMITcpConTcpAORnextKeyId = _FsMITcpConTcpAORnextKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 4, 1, 5),
    _FsMITcpConTcpAORnextKeyId_Type()
)
fsMITcpConTcpAORnextKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConTcpAORnextKeyId.setStatus("current")


class _FsMITcpConTcpAORcvKeyId_Type(Integer32):
    """Custom type fsMITcpConTcpAORcvKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMITcpConTcpAORcvKeyId_Type.__name__ = "Integer32"
_FsMITcpConTcpAORcvKeyId_Object = MibTableColumn
fsMITcpConTcpAORcvKeyId = _FsMITcpConTcpAORcvKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 4, 1, 6),
    _FsMITcpConTcpAORcvKeyId_Type()
)
fsMITcpConTcpAORcvKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConTcpAORcvKeyId.setStatus("current")


class _FsMITcpConTcpAORcvRnextKeyId_Type(Integer32):
    """Custom type fsMITcpConTcpAORcvRnextKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMITcpConTcpAORcvRnextKeyId_Type.__name__ = "Integer32"
_FsMITcpConTcpAORcvRnextKeyId_Object = MibTableColumn
fsMITcpConTcpAORcvRnextKeyId = _FsMITcpConTcpAORcvRnextKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 4, 1, 7),
    _FsMITcpConTcpAORcvRnextKeyId_Type()
)
fsMITcpConTcpAORcvRnextKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConTcpAORcvRnextKeyId.setStatus("current")
_FsMITcpConTcpAOConnErrCtr_Type = Counter32
_FsMITcpConTcpAOConnErrCtr_Object = MibTableColumn
fsMITcpConTcpAOConnErrCtr = _FsMITcpConTcpAOConnErrCtr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 4, 1, 8),
    _FsMITcpConTcpAOConnErrCtr_Type()
)
fsMITcpConTcpAOConnErrCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConTcpAOConnErrCtr.setStatus("current")
_FsMITcpConTcpAOSndSne_Type = Integer32
_FsMITcpConTcpAOSndSne_Object = MibTableColumn
fsMITcpConTcpAOSndSne = _FsMITcpConTcpAOSndSne_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 4, 1, 9),
    _FsMITcpConTcpAOSndSne_Type()
)
fsMITcpConTcpAOSndSne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConTcpAOSndSne.setStatus("current")
_FsMITcpConTcpAORcvSne_Type = Integer32
_FsMITcpConTcpAORcvSne_Object = MibTableColumn
fsMITcpConTcpAORcvSne = _FsMITcpConTcpAORcvSne_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 4, 1, 10),
    _FsMITcpConTcpAORcvSne_Type()
)
fsMITcpConTcpAORcvSne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConTcpAORcvSne.setStatus("current")
_FsMITcpNotification_ObjectIdentity = ObjectIdentity
fsMITcpNotification = _FsMITcpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 5)
)
_FsMITcpTrap_ObjectIdentity = ObjectIdentity
fsMITcpTrap = _FsMITcpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 5, 0)
)
_FsMITcpObjects_ObjectIdentity = ObjectIdentity
fsMITcpObjects = _FsMITcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 5, 1)
)
_FsMITcpAoLocalAddressType_Type = InetAddressType
_FsMITcpAoLocalAddressType_Object = MibScalar
fsMITcpAoLocalAddressType = _FsMITcpAoLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 5, 1, 1),
    _FsMITcpAoLocalAddressType_Type()
)
fsMITcpAoLocalAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMITcpAoLocalAddressType.setStatus("current")
_FsMITcpAoLocalAddress_Type = InetAddress
_FsMITcpAoLocalAddress_Object = MibScalar
fsMITcpAoLocalAddress = _FsMITcpAoLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 5, 1, 2),
    _FsMITcpAoLocalAddress_Type()
)
fsMITcpAoLocalAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMITcpAoLocalAddress.setStatus("current")
_FsMITcpAoLocalPort_Type = InetPortNumber
_FsMITcpAoLocalPort_Object = MibScalar
fsMITcpAoLocalPort = _FsMITcpAoLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 5, 1, 3),
    _FsMITcpAoLocalPort_Type()
)
fsMITcpAoLocalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMITcpAoLocalPort.setStatus("current")
_FsMITcpAoRemAddressType_Type = InetAddressType
_FsMITcpAoRemAddressType_Object = MibScalar
fsMITcpAoRemAddressType = _FsMITcpAoRemAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 5, 1, 4),
    _FsMITcpAoRemAddressType_Type()
)
fsMITcpAoRemAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMITcpAoRemAddressType.setStatus("current")
_FsMITcpAoRemAddress_Type = InetAddress
_FsMITcpAoRemAddress_Object = MibScalar
fsMITcpAoRemAddress = _FsMITcpAoRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 5, 1, 5),
    _FsMITcpAoRemAddress_Type()
)
fsMITcpAoRemAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMITcpAoRemAddress.setStatus("current")
_FsMITcpAoRemPort_Type = InetPortNumber
_FsMITcpAoRemPort_Object = MibScalar
fsMITcpAoRemPort = _FsMITcpAoRemPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 5, 1, 6),
    _FsMITcpAoRemPort_Type()
)
fsMITcpAoRemPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMITcpAoRemPort.setStatus("current")
_FsMITcpAoContextId_Type = Integer32
_FsMITcpAoContextId_Object = MibScalar
fsMITcpAoContextId = _FsMITcpAoContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 5, 1, 7),
    _FsMITcpAoContextId_Type()
)
fsMITcpAoContextId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMITcpAoContextId.setStatus("current")
_FsMITcpAoConnTestTable_Object = MibTable
fsMITcpAoConnTestTable = _FsMITcpAoConnTestTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 6)
)
if mibBuilder.loadTexts:
    fsMITcpAoConnTestTable.setStatus("current")
_FsMITcpAoConnTestEntry_Object = MibTableRow
fsMITcpAoConnTestEntry = _FsMITcpAoConnTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 6, 1)
)
fsMITcpAoConnTestEntry.setIndexNames(
    (0, "SUPERMICRO-MI-TCP-MIB", "fsMITcpContextId"),
    (0, "SUPERMICRO-MI-TCP-MIB", "fsMITcpAoConnTestLclAdrType"),
    (0, "SUPERMICRO-MI-TCP-MIB", "fsMITcpAoConnTestLclAdress"),
    (0, "SUPERMICRO-MI-TCP-MIB", "fsMITcpAoConnTestLclPort"),
    (0, "SUPERMICRO-MI-TCP-MIB", "fsMITcpAoConnTestRmtAdrType"),
    (0, "SUPERMICRO-MI-TCP-MIB", "fsMITcpAoConnTestRmtAdress"),
    (0, "SUPERMICRO-MI-TCP-MIB", "fsMITcpAoConnTestRmtPort"),
)
if mibBuilder.loadTexts:
    fsMITcpAoConnTestEntry.setStatus("current")
_FsMITcpAoConnTestLclAdrType_Type = InetAddressType
_FsMITcpAoConnTestLclAdrType_Object = MibTableColumn
fsMITcpAoConnTestLclAdrType = _FsMITcpAoConnTestLclAdrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 6, 1, 2),
    _FsMITcpAoConnTestLclAdrType_Type()
)
fsMITcpAoConnTestLclAdrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMITcpAoConnTestLclAdrType.setStatus("current")
_FsMITcpAoConnTestLclAdress_Type = InetAddress
_FsMITcpAoConnTestLclAdress_Object = MibTableColumn
fsMITcpAoConnTestLclAdress = _FsMITcpAoConnTestLclAdress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 6, 1, 3),
    _FsMITcpAoConnTestLclAdress_Type()
)
fsMITcpAoConnTestLclAdress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMITcpAoConnTestLclAdress.setStatus("current")
_FsMITcpAoConnTestLclPort_Type = InetPortNumber
_FsMITcpAoConnTestLclPort_Object = MibTableColumn
fsMITcpAoConnTestLclPort = _FsMITcpAoConnTestLclPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 6, 1, 4),
    _FsMITcpAoConnTestLclPort_Type()
)
fsMITcpAoConnTestLclPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMITcpAoConnTestLclPort.setStatus("current")
_FsMITcpAoConnTestRmtAdrType_Type = InetAddressType
_FsMITcpAoConnTestRmtAdrType_Object = MibTableColumn
fsMITcpAoConnTestRmtAdrType = _FsMITcpAoConnTestRmtAdrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 6, 1, 5),
    _FsMITcpAoConnTestRmtAdrType_Type()
)
fsMITcpAoConnTestRmtAdrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMITcpAoConnTestRmtAdrType.setStatus("current")
_FsMITcpAoConnTestRmtAdress_Type = InetAddress
_FsMITcpAoConnTestRmtAdress_Object = MibTableColumn
fsMITcpAoConnTestRmtAdress = _FsMITcpAoConnTestRmtAdress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 6, 1, 6),
    _FsMITcpAoConnTestRmtAdress_Type()
)
fsMITcpAoConnTestRmtAdress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMITcpAoConnTestRmtAdress.setStatus("current")
_FsMITcpAoConnTestRmtPort_Type = InetPortNumber
_FsMITcpAoConnTestRmtPort_Object = MibTableColumn
fsMITcpAoConnTestRmtPort = _FsMITcpAoConnTestRmtPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 6, 1, 7),
    _FsMITcpAoConnTestRmtPort_Type()
)
fsMITcpAoConnTestRmtPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMITcpAoConnTestRmtPort.setStatus("current")
_FsMITcpConTcpAOIcmpIgnCtr_Type = Counter32
_FsMITcpConTcpAOIcmpIgnCtr_Object = MibTableColumn
fsMITcpConTcpAOIcmpIgnCtr = _FsMITcpConTcpAOIcmpIgnCtr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 6, 1, 8),
    _FsMITcpConTcpAOIcmpIgnCtr_Type()
)
fsMITcpConTcpAOIcmpIgnCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConTcpAOIcmpIgnCtr.setStatus("current")
_FsMITcpConTcpAOSilentAccptCtr_Type = Counter32
_FsMITcpConTcpAOSilentAccptCtr_Object = MibTableColumn
fsMITcpConTcpAOSilentAccptCtr = _FsMITcpConTcpAOSilentAccptCtr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 6, 1, 9),
    _FsMITcpConTcpAOSilentAccptCtr_Type()
)
fsMITcpConTcpAOSilentAccptCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMITcpConTcpAOSilentAccptCtr.setStatus("current")
fsMIStdTcpConnectionEntry.registerAugmentions(
    ("SUPERMICRO-MI-TCP-MIB",
     "fsMITcpExtConnEntry")
)
fsMITcpExtConnEntry.setIndexNames(*fsMIStdTcpConnectionEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fsMITcpAoAuthError = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 76, 5, 0, 1)
)
fsMITcpAoAuthError.setObjects(
      *(("SUPERMICRO-MI-TCP-MIB", "fsMITcpAoContextId"),
        ("SUPERMICRO-MI-TCP-MIB", "fsMITcpAoLocalAddressType"),
        ("SUPERMICRO-MI-TCP-MIB", "fsMITcpAoLocalAddress"),
        ("SUPERMICRO-MI-TCP-MIB", "fsMITcpAoLocalPort"),
        ("SUPERMICRO-MI-TCP-MIB", "fsMITcpAoRemAddressType"),
        ("SUPERMICRO-MI-TCP-MIB", "fsMITcpAoRemAddress"),
        ("SUPERMICRO-MI-TCP-MIB", "fsMITcpAoRemPort"),
        ("SUPERMICRO-MI-TCP-MIB", "fsMITcpConTcpAOConnErrCtr"))
)
if mibBuilder.loadTexts:
    fsMITcpAoAuthError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-MI-TCP-MIB",
    **{"fsMITcp": fsMITcp,
       "fsMITcpGlobalTraceDebug": fsMITcpGlobalTraceDebug,
       "fsMIContextTable": fsMIContextTable,
       "fsMIContextEntry": fsMIContextEntry,
       "fsMITcpContextId": fsMITcpContextId,
       "fsMITcpAckOption": fsMITcpAckOption,
       "fsMITcpTimeStampOption": fsMITcpTimeStampOption,
       "fsMITcpBigWndOption": fsMITcpBigWndOption,
       "fsMITcpIncrIniWnd": fsMITcpIncrIniWnd,
       "fsMITcpMaxNumOfTCB": fsMITcpMaxNumOfTCB,
       "fsMITcpTraceDebug": fsMITcpTraceDebug,
       "fsMITcpMaxReTries": fsMITcpMaxReTries,
       "fsMITcpClearStatistics": fsMITcpClearStatistics,
       "fsMITcpTrapAdminStatus": fsMITcpTrapAdminStatus,
       "fsMITcpConnTable": fsMITcpConnTable,
       "fsMITcpConnEntry": fsMITcpConnEntry,
       "fsMITcpConnLocalAddress": fsMITcpConnLocalAddress,
       "fsMITcpConnLocalPort": fsMITcpConnLocalPort,
       "fsMITcpConnRemAddress": fsMITcpConnRemAddress,
       "fsMITcpConnRemPort": fsMITcpConnRemPort,
       "fsMITcpConnOutState": fsMITcpConnOutState,
       "fsMITcpConnSWindow": fsMITcpConnSWindow,
       "fsMITcpConnRWindow": fsMITcpConnRWindow,
       "fsMITcpConnCWindow": fsMITcpConnCWindow,
       "fsMITcpConnSSThresh": fsMITcpConnSSThresh,
       "fsMITcpConnSMSS": fsMITcpConnSMSS,
       "fsMITcpConnRMSS": fsMITcpConnRMSS,
       "fsMITcpConnSRT": fsMITcpConnSRT,
       "fsMITcpConnRTDE": fsMITcpConnRTDE,
       "fsMITcpConnPersist": fsMITcpConnPersist,
       "fsMITcpConnRexmt": fsMITcpConnRexmt,
       "fsMITcpConnRexmtCnt": fsMITcpConnRexmtCnt,
       "fsMITcpConnSBCount": fsMITcpConnSBCount,
       "fsMITcpConnSBSize": fsMITcpConnSBSize,
       "fsMITcpConnRBCount": fsMITcpConnRBCount,
       "fsMITcpConnRBSize": fsMITcpConnRBSize,
       "fsMITcpKaMainTmr": fsMITcpKaMainTmr,
       "fsMITcpKaRetransTmr": fsMITcpKaRetransTmr,
       "fsMITcpKaRetransCnt": fsMITcpKaRetransCnt,
       "fsMITcpExtConnTable": fsMITcpExtConnTable,
       "fsMITcpExtConnEntry": fsMITcpExtConnEntry,
       "fsMITcpConnMD5Option": fsMITcpConnMD5Option,
       "fsMITcpConnMD5ErrCtr": fsMITcpConnMD5ErrCtr,
       "fsMITcpConnTcpAOOption": fsMITcpConnTcpAOOption,
       "fsMITcpConTcpAOCurKeyId": fsMITcpConTcpAOCurKeyId,
       "fsMITcpConTcpAORnextKeyId": fsMITcpConTcpAORnextKeyId,
       "fsMITcpConTcpAORcvKeyId": fsMITcpConTcpAORcvKeyId,
       "fsMITcpConTcpAORcvRnextKeyId": fsMITcpConTcpAORcvRnextKeyId,
       "fsMITcpConTcpAOConnErrCtr": fsMITcpConTcpAOConnErrCtr,
       "fsMITcpConTcpAOSndSne": fsMITcpConTcpAOSndSne,
       "fsMITcpConTcpAORcvSne": fsMITcpConTcpAORcvSne,
       "fsMITcpNotification": fsMITcpNotification,
       "fsMITcpTrap": fsMITcpTrap,
       "fsMITcpAoAuthError": fsMITcpAoAuthError,
       "fsMITcpObjects": fsMITcpObjects,
       "fsMITcpAoLocalAddressType": fsMITcpAoLocalAddressType,
       "fsMITcpAoLocalAddress": fsMITcpAoLocalAddress,
       "fsMITcpAoLocalPort": fsMITcpAoLocalPort,
       "fsMITcpAoRemAddressType": fsMITcpAoRemAddressType,
       "fsMITcpAoRemAddress": fsMITcpAoRemAddress,
       "fsMITcpAoRemPort": fsMITcpAoRemPort,
       "fsMITcpAoContextId": fsMITcpAoContextId,
       "fsMITcpAoConnTestTable": fsMITcpAoConnTestTable,
       "fsMITcpAoConnTestEntry": fsMITcpAoConnTestEntry,
       "fsMITcpAoConnTestLclAdrType": fsMITcpAoConnTestLclAdrType,
       "fsMITcpAoConnTestLclAdress": fsMITcpAoConnTestLclAdress,
       "fsMITcpAoConnTestLclPort": fsMITcpAoConnTestLclPort,
       "fsMITcpAoConnTestRmtAdrType": fsMITcpAoConnTestRmtAdrType,
       "fsMITcpAoConnTestRmtAdress": fsMITcpAoConnTestRmtAdress,
       "fsMITcpAoConnTestRmtPort": fsMITcpAoConnTestRmtPort,
       "fsMITcpConTcpAOIcmpIgnCtr": fsMITcpConTcpAOIcmpIgnCtr,
       "fsMITcpConTcpAOSilentAccptCtr": fsMITcpConTcpAOSilentAccptCtr}
)
