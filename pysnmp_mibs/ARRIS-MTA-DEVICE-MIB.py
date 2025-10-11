# SNMP MIB module (ARRIS-MTA-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/arris/ARRIS-MTA-DEVICE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:10:20 2025
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

(arrisProdIdCM,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arrisProdIdCM")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

arrisMtaDevMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3)
)
if mibBuilder.loadTexts:
    arrisMtaDevMib.setRevisions(
        ("1915-06-25 00:00",
         "1915-01-20 00:00",
         "1912-05-02 00:00",
         "1912-03-16 00:00",
         "1912-03-15 00:00",
         "1912-03-06 00:00",
         "1912-02-28 00:00",
         "1912-02-21 00:00",
         "1911-04-18 00:00",
         "1911-04-07 00:00",
         "1910-06-22 00:00",
         "1910-05-05 00:00",
         "1910-03-03 00:00",
         "1910-02-10 00:00",
         "1910-01-20 00:00",
         "1909-06-30 00:00",
         "1909-05-04 00:00",
         "1909-04-29 00:00",
         "1909-04-20 00:00",
         "1908-12-02 00:00",
         "1909-02-02 00:00",
         "1908-09-22 00:00",
         "1908-06-17 00:00",
         "1908-06-10 00:00",
         "1908-04-12 00:00",
         "1908-04-22 00:00",
         "1908-04-01 00:00",
         "1908-02-22 00:00",
         "1908-02-04 00:00",
         "1908-01-29 00:00",
         "1908-01-17 00:00",
         "1908-01-17 00:00",
         "1911-07-13 00:00",
         "1910-07-30 00:00",
         "1907-07-27 00:00",
         "1907-04-09 00:00",
         "1906-11-29 00:00",
         "1906-03-29 00:00",
         "1906-02-17 00:00",
         "1905-02-01 00:00",
         "1905-07-27 00:00",
         "1905-02-01 00:00",
         "1905-01-04 00:00",
         "1904-12-16 00:00",
         "1903-07-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ArrsMtaDevProvMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("docsisOnly", 0),
          ("fullPacketCable", 1),
          ("packetCableMinusKDC", 2),
          ("cps", 3),
          ("gupi", 4),
          ("singleMAC", 5),
          ("basic1", 6),
          ("basic2", 7),
          ("gupiEncryptedMtaConfig", 8),
          ("gupiMacMta", 9),
          ("gupiEncryptedMacMta", 10),
          ("gupiTftpSvrOverride", 11))
    )



class CodecType(TextualConvention, Integer32):
    status = "obsolete"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("g711u", 1),
          ("g711a", 2),
          ("g7231", 3),
          ("g729", 4),
          ("g729a", 5),
          ("g729e", 6),
          ("g726", 7),
          ("g728", 8))
    )



class PacketizationPeriodType(TextualConvention, Integer32):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30)
        )
    )
    namedValues = NamedValues(
        *(("ten", 10),
          ("twenty", 20),
          ("thirty", 30))
    )



class SignalingProtocol(TextualConvention, Integer32):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ncs", 1))
    )



# MIB Managed Objects in the order of their OIDs

_ArrisMtaDevMibObjects_ObjectIdentity = ObjectIdentity
arrisMtaDevMibObjects = _ArrisMtaDevMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1)
)
_ArrisMtaDevBase_ObjectIdentity = ObjectIdentity
arrisMtaDevBase = _ArrisMtaDevBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1)
)
_ArrisMtaDevMonitoringMib_ObjectIdentity = ObjectIdentity
arrisMtaDevMonitoringMib = _ArrisMtaDevMonitoringMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1)
)
_ArrisMtaDevControl_ObjectIdentity = ObjectIdentity
arrisMtaDevControl = _ArrisMtaDevControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 1)
)
_ArrisMtaDevResetCallStats_Type = TruthValue
_ArrisMtaDevResetCallStats_Object = MibScalar
arrisMtaDevResetCallStats = _ArrisMtaDevResetCallStats_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 1, 1),
    _ArrisMtaDevResetCallStats_Type()
)
arrisMtaDevResetCallStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevResetCallStats.setStatus("current")


class _ArrisMtaDevEnableCallpSigTrace_Type(Integer32):
    """Custom type arrisMtaDevEnableCallpSigTrace based on Integer32"""
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


_ArrisMtaDevEnableCallpSigTrace_Type.__name__ = "Integer32"
_ArrisMtaDevEnableCallpSigTrace_Object = MibScalar
arrisMtaDevEnableCallpSigTrace = _ArrisMtaDevEnableCallpSigTrace_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 1, 2),
    _ArrisMtaDevEnableCallpSigTrace_Type()
)
arrisMtaDevEnableCallpSigTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEnableCallpSigTrace.setStatus("current")


class _ArrisMtaDevEnableCallStatsSyslogRpt_Type(Integer32):
    """Custom type arrisMtaDevEnableCallStatsSyslogRpt based on Integer32"""
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


_ArrisMtaDevEnableCallStatsSyslogRpt_Type.__name__ = "Integer32"
_ArrisMtaDevEnableCallStatsSyslogRpt_Object = MibScalar
arrisMtaDevEnableCallStatsSyslogRpt = _ArrisMtaDevEnableCallStatsSyslogRpt_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 1, 3),
    _ArrisMtaDevEnableCallStatsSyslogRpt_Type()
)
arrisMtaDevEnableCallStatsSyslogRpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEnableCallStatsSyslogRpt.setStatus("current")


class _ArrisMtaDevSwDnldNoSvcImpact_Type(Integer32):
    """Custom type arrisMtaDevSwDnldNoSvcImpact based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("strictEnable", 2))
    )


_ArrisMtaDevSwDnldNoSvcImpact_Type.__name__ = "Integer32"
_ArrisMtaDevSwDnldNoSvcImpact_Object = MibScalar
arrisMtaDevSwDnldNoSvcImpact = _ArrisMtaDevSwDnldNoSvcImpact_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 1, 4),
    _ArrisMtaDevSwDnldNoSvcImpact_Type()
)
arrisMtaDevSwDnldNoSvcImpact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevSwDnldNoSvcImpact.setStatus("current")


class _ArrisMtaDevEnableCallSigLastMsgRpt_Type(Integer32):
    """Custom type arrisMtaDevEnableCallSigLastMsgRpt based on Integer32"""
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


_ArrisMtaDevEnableCallSigLastMsgRpt_Type.__name__ = "Integer32"
_ArrisMtaDevEnableCallSigLastMsgRpt_Object = MibScalar
arrisMtaDevEnableCallSigLastMsgRpt = _ArrisMtaDevEnableCallSigLastMsgRpt_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 1, 5),
    _ArrisMtaDevEnableCallSigLastMsgRpt_Type()
)
arrisMtaDevEnableCallSigLastMsgRpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEnableCallSigLastMsgRpt.setStatus("current")


class _ArrisMtaDevNsadSwDnldStatus_Type(Integer32):
    """Custom type arrisMtaDevNsadSwDnldStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download-Idle", 0),
          ("download-Acceptance-In-Progress", 1),
          ("download-Application-Pending", 2))
    )


_ArrisMtaDevNsadSwDnldStatus_Type.__name__ = "Integer32"
_ArrisMtaDevNsadSwDnldStatus_Object = MibScalar
arrisMtaDevNsadSwDnldStatus = _ArrisMtaDevNsadSwDnldStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 1, 6),
    _ArrisMtaDevNsadSwDnldStatus_Type()
)
arrisMtaDevNsadSwDnldStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevNsadSwDnldStatus.setStatus("current")
_ArrisMtaDevRestoreNvmFactoryDefault_Type = TruthValue
_ArrisMtaDevRestoreNvmFactoryDefault_Object = MibScalar
arrisMtaDevRestoreNvmFactoryDefault = _ArrisMtaDevRestoreNvmFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 1, 7),
    _ArrisMtaDevRestoreNvmFactoryDefault_Type()
)
arrisMtaDevRestoreNvmFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevRestoreNvmFactoryDefault.setStatus("current")


class _ArrisMtaDevEnableLogging_Type(Integer32):
    """Custom type arrisMtaDevEnableLogging based on Integer32"""
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


_ArrisMtaDevEnableLogging_Type.__name__ = "Integer32"
_ArrisMtaDevEnableLogging_Object = MibScalar
arrisMtaDevEnableLogging = _ArrisMtaDevEnableLogging_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 1, 8),
    _ArrisMtaDevEnableLogging_Type()
)
arrisMtaDevEnableLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEnableLogging.setStatus("current")


class _ArrisMtaDevLoggingContext_Type(Integer32):
    """Custom type arrisMtaDevLoggingContext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mgcp", 0),
          ("cm-dhcp", 1),
          ("mta-dhcp", 2),
          ("dsx", 3))
    )


_ArrisMtaDevLoggingContext_Type.__name__ = "Integer32"
_ArrisMtaDevLoggingContext_Object = MibScalar
arrisMtaDevLoggingContext = _ArrisMtaDevLoggingContext_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 1, 9),
    _ArrisMtaDevLoggingContext_Type()
)
arrisMtaDevLoggingContext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevLoggingContext.setStatus("current")


class _ArrisMtaDevEnablePacketLossConcealment_Type(Integer32):
    """Custom type arrisMtaDevEnablePacketLossConcealment based on Integer32"""
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


_ArrisMtaDevEnablePacketLossConcealment_Type.__name__ = "Integer32"
_ArrisMtaDevEnablePacketLossConcealment_Object = MibScalar
arrisMtaDevEnablePacketLossConcealment = _ArrisMtaDevEnablePacketLossConcealment_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 1, 10),
    _ArrisMtaDevEnablePacketLossConcealment_Type()
)
arrisMtaDevEnablePacketLossConcealment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEnablePacketLossConcealment.setStatus("current")


class _ArrisMtaDevEnableRTCPStaticInterval_Type(Integer32):
    """Custom type arrisMtaDevEnableRTCPStaticInterval based on Integer32"""
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


_ArrisMtaDevEnableRTCPStaticInterval_Type.__name__ = "Integer32"
_ArrisMtaDevEnableRTCPStaticInterval_Object = MibScalar
arrisMtaDevEnableRTCPStaticInterval = _ArrisMtaDevEnableRTCPStaticInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 1, 11),
    _ArrisMtaDevEnableRTCPStaticInterval_Type()
)
arrisMtaDevEnableRTCPStaticInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEnableRTCPStaticInterval.setStatus("current")
_ArrisMtaDevTrace_ObjectIdentity = ObjectIdentity
arrisMtaDevTrace = _ArrisMtaDevTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2)
)
_ArrisMtaDevRtpTxPktsTotal_Type = Integer32
_ArrisMtaDevRtpTxPktsTotal_Object = MibScalar
arrisMtaDevRtpTxPktsTotal = _ArrisMtaDevRtpTxPktsTotal_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 1),
    _ArrisMtaDevRtpTxPktsTotal_Type()
)
arrisMtaDevRtpTxPktsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevRtpTxPktsTotal.setStatus("current")
_ArrisMtaDevRtpRxPktsTotal_Type = Integer32
_ArrisMtaDevRtpRxPktsTotal_Object = MibScalar
arrisMtaDevRtpRxPktsTotal = _ArrisMtaDevRtpRxPktsTotal_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 2),
    _ArrisMtaDevRtpRxPktsTotal_Type()
)
arrisMtaDevRtpRxPktsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevRtpRxPktsTotal.setStatus("current")
_ArrisMtaDevRtpPercentPktsLostTotal_Type = Integer32
_ArrisMtaDevRtpPercentPktsLostTotal_Object = MibScalar
arrisMtaDevRtpPercentPktsLostTotal = _ArrisMtaDevRtpPercentPktsLostTotal_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 3),
    _ArrisMtaDevRtpPercentPktsLostTotal_Type()
)
arrisMtaDevRtpPercentPktsLostTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevRtpPercentPktsLostTotal.setStatus("current")


class _ArrisMtaDevProvState_Type(Integer32):
    """Custom type arrisMtaDevProvState based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("dhcpBound", 1),
          ("dnsReqProvSvrIP", 2),
          ("kdcHostNameDnsReq", 3),
          ("kdcHostNameDnsRply", 4),
          ("kdcIpDnsReq", 5),
          ("kdcIpDnsRply", 6),
          ("asReqSent", 7),
          ("asRplyRcvd", 8),
          ("tgsReqSent", 9),
          ("tgsRplyRcvd", 10),
          ("apReqSent", 11),
          ("apRplyRcvd", 12),
          ("enrollmentInform", 13),
          ("cfgUrlSet", 14),
          ("dnsReqTftpSvrIp", 15),
          ("cfgFileReq", 16),
          ("rcvCfgFile", 17),
          ("syslogMsgProvComplete", 18),
          ("statusInform", 19),
          ("provcomplete", 20))
    )


_ArrisMtaDevProvState_Type.__name__ = "Integer32"
_ArrisMtaDevProvState_Object = MibScalar
arrisMtaDevProvState = _ArrisMtaDevProvState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 4),
    _ArrisMtaDevProvState_Type()
)
arrisMtaDevProvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevProvState.setStatus("current")


class _ArrisMtaDevSWUpgradeStatus_Type(Integer32):
    """Custom type arrisMtaDevSWUpgradeStatus based on Integer32"""
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
        *(("inProgress", 1),
          ("completeFromProvisioning", 2),
          ("completeFromMgt", 3),
          ("failed", 4),
          ("other", 5))
    )


_ArrisMtaDevSWUpgradeStatus_Type.__name__ = "Integer32"
_ArrisMtaDevSWUpgradeStatus_Object = MibScalar
arrisMtaDevSWUpgradeStatus = _ArrisMtaDevSWUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 5),
    _ArrisMtaDevSWUpgradeStatus_Type()
)
arrisMtaDevSWUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSWUpgradeStatus.setStatus("current")
_ArrisMtaDevSignalingAvgLatency_Type = Integer32
_ArrisMtaDevSignalingAvgLatency_Object = MibScalar
arrisMtaDevSignalingAvgLatency = _ArrisMtaDevSignalingAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 6),
    _ArrisMtaDevSignalingAvgLatency_Type()
)
arrisMtaDevSignalingAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingAvgLatency.setStatus("current")
_ArrisMtaDevSignalingTxSuccessfulMsgCnt_Type = Integer32
_ArrisMtaDevSignalingTxSuccessfulMsgCnt_Object = MibScalar
arrisMtaDevSignalingTxSuccessfulMsgCnt = _ArrisMtaDevSignalingTxSuccessfulMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 7),
    _ArrisMtaDevSignalingTxSuccessfulMsgCnt_Type()
)
arrisMtaDevSignalingTxSuccessfulMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingTxSuccessfulMsgCnt.setStatus("current")
_ArrisMtaDevSignalingRxSuccessfulMsgCnt_Type = Integer32
_ArrisMtaDevSignalingRxSuccessfulMsgCnt_Object = MibScalar
arrisMtaDevSignalingRxSuccessfulMsgCnt = _ArrisMtaDevSignalingRxSuccessfulMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 8),
    _ArrisMtaDevSignalingRxSuccessfulMsgCnt_Type()
)
arrisMtaDevSignalingRxSuccessfulMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingRxSuccessfulMsgCnt.setStatus("current")
_ArrisMtaDevSignalingTxNAKCnt_Type = Integer32
_ArrisMtaDevSignalingTxNAKCnt_Object = MibScalar
arrisMtaDevSignalingTxNAKCnt = _ArrisMtaDevSignalingTxNAKCnt_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 9),
    _ArrisMtaDevSignalingTxNAKCnt_Type()
)
arrisMtaDevSignalingTxNAKCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingTxNAKCnt.setStatus("current")
_ArrisMtaDevSignalingRxNAKCnt_Type = Integer32
_ArrisMtaDevSignalingRxNAKCnt_Object = MibScalar
arrisMtaDevSignalingRxNAKCnt = _ArrisMtaDevSignalingRxNAKCnt_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 10),
    _ArrisMtaDevSignalingRxNAKCnt_Type()
)
arrisMtaDevSignalingRxNAKCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingRxNAKCnt.setStatus("current")
_ArrisMtaDevSignalingRxNoACKCnt_Type = Integer32
_ArrisMtaDevSignalingRxNoACKCnt_Object = MibScalar
arrisMtaDevSignalingRxNoACKCnt = _ArrisMtaDevSignalingRxNoACKCnt_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 11),
    _ArrisMtaDevSignalingRxNoACKCnt_Type()
)
arrisMtaDevSignalingRxNoACKCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingRxNoACKCnt.setStatus("current")
_ArrisMtaDevSignalingLastMsg1_Type = SnmpAdminString
_ArrisMtaDevSignalingLastMsg1_Object = MibScalar
arrisMtaDevSignalingLastMsg1 = _ArrisMtaDevSignalingLastMsg1_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 12),
    _ArrisMtaDevSignalingLastMsg1_Type()
)
arrisMtaDevSignalingLastMsg1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingLastMsg1.setStatus("current")
_ArrisMtaDevSignalingLastMsg2_Type = SnmpAdminString
_ArrisMtaDevSignalingLastMsg2_Object = MibScalar
arrisMtaDevSignalingLastMsg2 = _ArrisMtaDevSignalingLastMsg2_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 13),
    _ArrisMtaDevSignalingLastMsg2_Type()
)
arrisMtaDevSignalingLastMsg2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingLastMsg2.setStatus("current")
_ArrisMtaDevSignalingLastMsg3_Type = SnmpAdminString
_ArrisMtaDevSignalingLastMsg3_Object = MibScalar
arrisMtaDevSignalingLastMsg3 = _ArrisMtaDevSignalingLastMsg3_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 14),
    _ArrisMtaDevSignalingLastMsg3_Type()
)
arrisMtaDevSignalingLastMsg3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingLastMsg3.setStatus("current")
_ArrisMtaDevSignalingLastMsg4_Type = SnmpAdminString
_ArrisMtaDevSignalingLastMsg4_Object = MibScalar
arrisMtaDevSignalingLastMsg4 = _ArrisMtaDevSignalingLastMsg4_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 15),
    _ArrisMtaDevSignalingLastMsg4_Type()
)
arrisMtaDevSignalingLastMsg4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingLastMsg4.setStatus("current")
_ArrisMtaDevSignalingLastMsg5_Type = SnmpAdminString
_ArrisMtaDevSignalingLastMsg5_Object = MibScalar
arrisMtaDevSignalingLastMsg5 = _ArrisMtaDevSignalingLastMsg5_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 16),
    _ArrisMtaDevSignalingLastMsg5_Type()
)
arrisMtaDevSignalingLastMsg5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingLastMsg5.setStatus("current")
_ArrisMtaDevSignalingLastMsg6_Type = SnmpAdminString
_ArrisMtaDevSignalingLastMsg6_Object = MibScalar
arrisMtaDevSignalingLastMsg6 = _ArrisMtaDevSignalingLastMsg6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 17),
    _ArrisMtaDevSignalingLastMsg6_Type()
)
arrisMtaDevSignalingLastMsg6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingLastMsg6.setStatus("current")
_ArrisMtaDevSignalingLastMsg7_Type = SnmpAdminString
_ArrisMtaDevSignalingLastMsg7_Object = MibScalar
arrisMtaDevSignalingLastMsg7 = _ArrisMtaDevSignalingLastMsg7_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 18),
    _ArrisMtaDevSignalingLastMsg7_Type()
)
arrisMtaDevSignalingLastMsg7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingLastMsg7.setStatus("current")
_ArrisMtaDevSignalingLastMsg8_Type = SnmpAdminString
_ArrisMtaDevSignalingLastMsg8_Object = MibScalar
arrisMtaDevSignalingLastMsg8 = _ArrisMtaDevSignalingLastMsg8_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 19),
    _ArrisMtaDevSignalingLastMsg8_Type()
)
arrisMtaDevSignalingLastMsg8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingLastMsg8.setStatus("current")
_ArrisMtaDevSignalingLastMsg9_Type = SnmpAdminString
_ArrisMtaDevSignalingLastMsg9_Object = MibScalar
arrisMtaDevSignalingLastMsg9 = _ArrisMtaDevSignalingLastMsg9_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 20),
    _ArrisMtaDevSignalingLastMsg9_Type()
)
arrisMtaDevSignalingLastMsg9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingLastMsg9.setStatus("current")
_ArrisMtaDevSignalingLastMsg10_Type = SnmpAdminString
_ArrisMtaDevSignalingLastMsg10_Object = MibScalar
arrisMtaDevSignalingLastMsg10 = _ArrisMtaDevSignalingLastMsg10_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 21),
    _ArrisMtaDevSignalingLastMsg10_Type()
)
arrisMtaDevSignalingLastMsg10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingLastMsg10.setStatus("current")
_ArrisMtaDevSignalingLastMsg11_Type = SnmpAdminString
_ArrisMtaDevSignalingLastMsg11_Object = MibScalar
arrisMtaDevSignalingLastMsg11 = _ArrisMtaDevSignalingLastMsg11_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 22),
    _ArrisMtaDevSignalingLastMsg11_Type()
)
arrisMtaDevSignalingLastMsg11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingLastMsg11.setStatus("current")
_ArrisMtaDevSignalingLastMsg12_Type = SnmpAdminString
_ArrisMtaDevSignalingLastMsg12_Object = MibScalar
arrisMtaDevSignalingLastMsg12 = _ArrisMtaDevSignalingLastMsg12_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 23),
    _ArrisMtaDevSignalingLastMsg12_Type()
)
arrisMtaDevSignalingLastMsg12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingLastMsg12.setStatus("current")
_ArrisMtaDevSignalingLastMsg13_Type = SnmpAdminString
_ArrisMtaDevSignalingLastMsg13_Object = MibScalar
arrisMtaDevSignalingLastMsg13 = _ArrisMtaDevSignalingLastMsg13_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 24),
    _ArrisMtaDevSignalingLastMsg13_Type()
)
arrisMtaDevSignalingLastMsg13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingLastMsg13.setStatus("current")
_ArrisMtaDevSignalingLastMsg14_Type = SnmpAdminString
_ArrisMtaDevSignalingLastMsg14_Object = MibScalar
arrisMtaDevSignalingLastMsg14 = _ArrisMtaDevSignalingLastMsg14_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 25),
    _ArrisMtaDevSignalingLastMsg14_Type()
)
arrisMtaDevSignalingLastMsg14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingLastMsg14.setStatus("current")
_ArrisMtaDevSignalingLastMsg15_Type = SnmpAdminString
_ArrisMtaDevSignalingLastMsg15_Object = MibScalar
arrisMtaDevSignalingLastMsg15 = _ArrisMtaDevSignalingLastMsg15_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 26),
    _ArrisMtaDevSignalingLastMsg15_Type()
)
arrisMtaDevSignalingLastMsg15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingLastMsg15.setStatus("current")
_ArrisMtaDevSignalingLastMsg16_Type = SnmpAdminString
_ArrisMtaDevSignalingLastMsg16_Object = MibScalar
arrisMtaDevSignalingLastMsg16 = _ArrisMtaDevSignalingLastMsg16_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 27),
    _ArrisMtaDevSignalingLastMsg16_Type()
)
arrisMtaDevSignalingLastMsg16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevSignalingLastMsg16.setStatus("current")
_ArrisMtaDevEstimatedMinutesRemaining_Type = Integer32
_ArrisMtaDevEstimatedMinutesRemaining_Object = MibScalar
arrisMtaDevEstimatedMinutesRemaining = _ArrisMtaDevEstimatedMinutesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 44),
    _ArrisMtaDevEstimatedMinutesRemaining_Type()
)
arrisMtaDevEstimatedMinutesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevEstimatedMinutesRemaining.setStatus("current")
if mibBuilder.loadTexts:
    arrisMtaDevEstimatedMinutesRemaining.setUnits("minutes")
_ArrisMtaDevEstimatedChargeRemaining_Type = Integer32
_ArrisMtaDevEstimatedChargeRemaining_Object = MibScalar
arrisMtaDevEstimatedChargeRemaining = _ArrisMtaDevEstimatedChargeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 45),
    _ArrisMtaDevEstimatedChargeRemaining_Type()
)
arrisMtaDevEstimatedChargeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevEstimatedChargeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    arrisMtaDevEstimatedChargeRemaining.setUnits("percent")
_ArrisMtaDevCallStatsTable_Object = MibTable
arrisMtaDevCallStatsTable = _ArrisMtaDevCallStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 46)
)
if mibBuilder.loadTexts:
    arrisMtaDevCallStatsTable.setStatus("current")
_ArrisMtaDevCallStatsEntry_Object = MibTableRow
arrisMtaDevCallStatsEntry = _ArrisMtaDevCallStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 46, 1)
)
arrisMtaDevCallStatsEntry.setIndexNames(
    (0, "ARRIS-MTA-DEVICE-MIB", "arrisMtaDevCallStatsIndex"),
)
if mibBuilder.loadTexts:
    arrisMtaDevCallStatsEntry.setStatus("current")
_ArrisMtaDevCallStatsIndex_Type = Integer32
_ArrisMtaDevCallStatsIndex_Object = MibTableColumn
arrisMtaDevCallStatsIndex = _ArrisMtaDevCallStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 46, 1, 1),
    _ArrisMtaDevCallStatsIndex_Type()
)
arrisMtaDevCallStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisMtaDevCallStatsIndex.setStatus("current")
_ArrisMtaDevCallStatsRtpTxPkts_Type = Integer32
_ArrisMtaDevCallStatsRtpTxPkts_Object = MibTableColumn
arrisMtaDevCallStatsRtpTxPkts = _ArrisMtaDevCallStatsRtpTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 46, 1, 2),
    _ArrisMtaDevCallStatsRtpTxPkts_Type()
)
arrisMtaDevCallStatsRtpTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevCallStatsRtpTxPkts.setStatus("current")
_ArrisMtaDevCallStatsRtpRxPkts_Type = Integer32
_ArrisMtaDevCallStatsRtpRxPkts_Object = MibTableColumn
arrisMtaDevCallStatsRtpRxPkts = _ArrisMtaDevCallStatsRtpRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 46, 1, 3),
    _ArrisMtaDevCallStatsRtpRxPkts_Type()
)
arrisMtaDevCallStatsRtpRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevCallStatsRtpRxPkts.setStatus("current")
_ArrisMtaDevCallStatsRtpPercentPktsLost_Type = Integer32
_ArrisMtaDevCallStatsRtpPercentPktsLost_Object = MibTableColumn
arrisMtaDevCallStatsRtpPercentPktsLost = _ArrisMtaDevCallStatsRtpPercentPktsLost_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 46, 1, 4),
    _ArrisMtaDevCallStatsRtpPercentPktsLost_Type()
)
arrisMtaDevCallStatsRtpPercentPktsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevCallStatsRtpPercentPktsLost.setStatus("current")
_ArrisMtaDevCallStatsAvgJitter_Type = Integer32
_ArrisMtaDevCallStatsAvgJitter_Object = MibTableColumn
arrisMtaDevCallStatsAvgJitter = _ArrisMtaDevCallStatsAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 46, 1, 5),
    _ArrisMtaDevCallStatsAvgJitter_Type()
)
arrisMtaDevCallStatsAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevCallStatsAvgJitter.setStatus("current")
_ArrisMtaDevCallStatsMaxJitter_Type = Integer32
_ArrisMtaDevCallStatsMaxJitter_Object = MibTableColumn
arrisMtaDevCallStatsMaxJitter = _ArrisMtaDevCallStatsMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 46, 1, 6),
    _ArrisMtaDevCallStatsMaxJitter_Type()
)
arrisMtaDevCallStatsMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevCallStatsMaxJitter.setStatus("current")
_ArrisMtaDevCallStatsAvgLatency_Type = Integer32
_ArrisMtaDevCallStatsAvgLatency_Object = MibTableColumn
arrisMtaDevCallStatsAvgLatency = _ArrisMtaDevCallStatsAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 46, 1, 7),
    _ArrisMtaDevCallStatsAvgLatency_Type()
)
arrisMtaDevCallStatsAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevCallStatsAvgLatency.setStatus("current")


class _ArrisMtaDevCallStatsHookStatus_Type(Integer32):
    """Custom type arrisMtaDevCallStatsHookStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("onHook", 0),
          ("offHook", 1))
    )


_ArrisMtaDevCallStatsHookStatus_Type.__name__ = "Integer32"
_ArrisMtaDevCallStatsHookStatus_Object = MibTableColumn
arrisMtaDevCallStatsHookStatus = _ArrisMtaDevCallStatsHookStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 46, 1, 9),
    _ArrisMtaDevCallStatsHookStatus_Type()
)
arrisMtaDevCallStatsHookStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevCallStatsHookStatus.setStatus("current")


class _ArrisMtaDevCallStatsSLICStatus_Type(Integer32):
    """Custom type arrisMtaDevCallStatsSLICStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("overtemp", 1))
    )


_ArrisMtaDevCallStatsSLICStatus_Type.__name__ = "Integer32"
_ArrisMtaDevCallStatsSLICStatus_Object = MibTableColumn
arrisMtaDevCallStatsSLICStatus = _ArrisMtaDevCallStatsSLICStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 46, 1, 10),
    _ArrisMtaDevCallStatsSLICStatus_Type()
)
arrisMtaDevCallStatsSLICStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevCallStatsSLICStatus.setStatus("current")


class _ArrisMtaDevCallStatsEndPntOpStatus_Type(Integer32):
    """Custom type arrisMtaDevCallStatsEndPntOpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_ArrisMtaDevCallStatsEndPntOpStatus_Type.__name__ = "Integer32"
_ArrisMtaDevCallStatsEndPntOpStatus_Object = MibTableColumn
arrisMtaDevCallStatsEndPntOpStatus = _ArrisMtaDevCallStatsEndPntOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 46, 1, 11),
    _ArrisMtaDevCallStatsEndPntOpStatus_Type()
)
arrisMtaDevCallStatsEndPntOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevCallStatsEndPntOpStatus.setStatus("current")


class _ArrisMtaDevCallStatsLineSubState_Type(Bits):
    """Custom type arrisMtaDevCallStatsLineSubState based on Bits"""
    namedValues = NamedValues(
        *(("normal", 0),
          ("diagsPending", 1),
          ("diagsFailed", 2),
          ("lcProtection", 3),
          ("dspFail", 4))
    )

_ArrisMtaDevCallStatsLineSubState_Type.__name__ = "Bits"
_ArrisMtaDevCallStatsLineSubState_Object = MibTableColumn
arrisMtaDevCallStatsLineSubState = _ArrisMtaDevCallStatsLineSubState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 46, 1, 12),
    _ArrisMtaDevCallStatsLineSubState_Type()
)
arrisMtaDevCallStatsLineSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevCallStatsLineSubState.setStatus("current")
_ArrisMtaDevRtpPktsLostTotal_Type = Integer32
_ArrisMtaDevRtpPktsLostTotal_Object = MibScalar
arrisMtaDevRtpPktsLostTotal = _ArrisMtaDevRtpPktsLostTotal_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 47),
    _ArrisMtaDevRtpPktsLostTotal_Type()
)
arrisMtaDevRtpPktsLostTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevRtpPktsLostTotal.setStatus("current")
_ArrisMtaDevLastCallStartTime_Type = DateAndTime
_ArrisMtaDevLastCallStartTime_Object = MibScalar
arrisMtaDevLastCallStartTime = _ArrisMtaDevLastCallStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 48),
    _ArrisMtaDevLastCallStartTime_Type()
)
arrisMtaDevLastCallStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevLastCallStartTime.setStatus("current")
_ArrisMtaDevLastCallEndTime_Type = DateAndTime
_ArrisMtaDevLastCallEndTime_Object = MibScalar
arrisMtaDevLastCallEndTime = _ArrisMtaDevLastCallEndTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 2, 49),
    _ArrisMtaDevLastCallEndTime_Type()
)
arrisMtaDevLastCallEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevLastCallEndTime.setStatus("current")
_ArrisMtaDevParameters_ObjectIdentity = ObjectIdentity
arrisMtaDevParameters = _ArrisMtaDevParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 3)
)
_ArrisMtaDevMaxCpeAllowed_Type = Integer32
_ArrisMtaDevMaxCpeAllowed_Object = MibScalar
arrisMtaDevMaxCpeAllowed = _ArrisMtaDevMaxCpeAllowed_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 3, 1),
    _ArrisMtaDevMaxCpeAllowed_Type()
)
arrisMtaDevMaxCpeAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevMaxCpeAllowed.setStatus("current")


class _ArrisMtaDevNetworkAccess_Type(Integer32):
    """Custom type arrisMtaDevNetworkAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ArrisMtaDevNetworkAccess_Type.__name__ = "Integer32"
_ArrisMtaDevNetworkAccess_Object = MibScalar
arrisMtaDevNetworkAccess = _ArrisMtaDevNetworkAccess_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 3, 2),
    _ArrisMtaDevNetworkAccess_Type()
)
arrisMtaDevNetworkAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevNetworkAccess.setStatus("current")
_ArrisMtaDevLineParameterTable_Object = MibTable
arrisMtaDevLineParameterTable = _ArrisMtaDevLineParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    arrisMtaDevLineParameterTable.setStatus("current")
_ArrisMtaDevLineParameterEntry_Object = MibTableRow
arrisMtaDevLineParameterEntry = _ArrisMtaDevLineParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 3, 3, 1)
)
arrisMtaDevLineParameterEntry.setIndexNames(
    (0, "ARRIS-MTA-DEVICE-MIB", "arrisMtaDevInterfaceIndex"),
)
if mibBuilder.loadTexts:
    arrisMtaDevLineParameterEntry.setStatus("current")
_ArrisMtaDevInterfaceIndex_Type = Integer32
_ArrisMtaDevInterfaceIndex_Object = MibTableColumn
arrisMtaDevInterfaceIndex = _ArrisMtaDevInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 3, 3, 1, 1),
    _ArrisMtaDevInterfaceIndex_Type()
)
arrisMtaDevInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevInterfaceIndex.setStatus("current")
_ArrisMtaDevPktcDevEvEndpointName_Type = SnmpAdminString
_ArrisMtaDevPktcDevEvEndpointName_Object = MibTableColumn
arrisMtaDevPktcDevEvEndpointName = _ArrisMtaDevPktcDevEvEndpointName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 3, 3, 1, 2),
    _ArrisMtaDevPktcDevEvEndpointName_Type()
)
arrisMtaDevPktcDevEvEndpointName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevPktcDevEvEndpointName.setStatus("current")
_ArrisMtaDevActiveConnections_Type = Integer32
_ArrisMtaDevActiveConnections_Object = MibTableColumn
arrisMtaDevActiveConnections = _ArrisMtaDevActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 3, 3, 1, 3),
    _ArrisMtaDevActiveConnections_Type()
)
arrisMtaDevActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevActiveConnections.setStatus("current")
_ArrisMtaDevLineMWIActive_Type = TruthValue
_ArrisMtaDevLineMWIActive_Object = MibTableColumn
arrisMtaDevLineMWIActive = _ArrisMtaDevLineMWIActive_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 3, 3, 1, 4),
    _ArrisMtaDevLineMWIActive_Type()
)
arrisMtaDevLineMWIActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevLineMWIActive.setStatus("current")
_ArrisMtaDevUpSvcFlowParameterTable_Object = MibTable
arrisMtaDevUpSvcFlowParameterTable = _ArrisMtaDevUpSvcFlowParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    arrisMtaDevUpSvcFlowParameterTable.setStatus("current")
_ArrisMtaDevUpSvcFlowParameterEntry_Object = MibTableRow
arrisMtaDevUpSvcFlowParameterEntry = _ArrisMtaDevUpSvcFlowParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 3, 4, 1)
)
arrisMtaDevUpSvcFlowParameterEntry.setIndexNames(
    (0, "ARRIS-MTA-DEVICE-MIB", "arrisMtaDevDocsQosParamUpSvcFlowSFID"),
)
if mibBuilder.loadTexts:
    arrisMtaDevUpSvcFlowParameterEntry.setStatus("current")
_ArrisMtaDevDocsQosParamUpSvcFlowSFID_Type = Integer32
_ArrisMtaDevDocsQosParamUpSvcFlowSFID_Object = MibTableColumn
arrisMtaDevDocsQosParamUpSvcFlowSFID = _ArrisMtaDevDocsQosParamUpSvcFlowSFID_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 3, 4, 1, 1),
    _ArrisMtaDevDocsQosParamUpSvcFlowSFID_Type()
)
arrisMtaDevDocsQosParamUpSvcFlowSFID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDocsQosParamUpSvcFlowSFID.setStatus("current")
_ArrisMtaDevDocsQosParamUpSvcFlowSchedulingType_Type = Integer32
_ArrisMtaDevDocsQosParamUpSvcFlowSchedulingType_Object = MibTableColumn
arrisMtaDevDocsQosParamUpSvcFlowSchedulingType = _ArrisMtaDevDocsQosParamUpSvcFlowSchedulingType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 3, 4, 1, 2),
    _ArrisMtaDevDocsQosParamUpSvcFlowSchedulingType_Type()
)
arrisMtaDevDocsQosParamUpSvcFlowSchedulingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDocsQosParamUpSvcFlowSchedulingType.setStatus("current")


class _ArrisMtaDevQosMode_Type(Integer32):
    """Custom type arrisMtaDevQosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort-FullDQos-PCMM", 0),
          ("dsxMode", 1))
    )


_ArrisMtaDevQosMode_Type.__name__ = "Integer32"
_ArrisMtaDevQosMode_Object = MibScalar
arrisMtaDevQosMode = _ArrisMtaDevQosMode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 3, 5),
    _ArrisMtaDevQosMode_Type()
)
arrisMtaDevQosMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevQosMode.setStatus("current")


class _ArrisMtaDevEventFormat_Type(Integer32):
    """Custom type arrisMtaDevEventFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pktc10", 0),
          ("pktc15", 1))
    )


_ArrisMtaDevEventFormat_Type.__name__ = "Integer32"
_ArrisMtaDevEventFormat_Object = MibScalar
arrisMtaDevEventFormat = _ArrisMtaDevEventFormat_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 3, 6),
    _ArrisMtaDevEventFormat_Type()
)
arrisMtaDevEventFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevEventFormat.setStatus("current")
_ArrisMtaDevVqm_ObjectIdentity = ObjectIdentity
arrisMtaDevVqm = _ArrisMtaDevVqm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 4)
)


class _ArrisMtaDevVqmLine_Type(Integer32):
    """Custom type arrisMtaDevVqmLine based on Integer32"""
    defaultValue = 1


_ArrisMtaDevVqmLine_Type.__name__ = "Integer32"
_ArrisMtaDevVqmLine_Object = MibScalar
arrisMtaDevVqmLine = _ArrisMtaDevVqmLine_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 4, 1),
    _ArrisMtaDevVqmLine_Type()
)
arrisMtaDevVqmLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevVqmLine.setStatus("current")


class _ArrisMtaDevVqmClear_Type(Integer32):
    """Custom type arrisMtaDevVqmClear based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("single-line", 0),
          ("all-lines", 1))
    )


_ArrisMtaDevVqmClear_Type.__name__ = "Integer32"
_ArrisMtaDevVqmClear_Object = MibScalar
arrisMtaDevVqmClear = _ArrisMtaDevVqmClear_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 4, 2),
    _ArrisMtaDevVqmClear_Type()
)
arrisMtaDevVqmClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevVqmClear.setStatus("current")


class _ArrisMtaDevVqmEnable_Type(Integer32):
    """Custom type arrisMtaDevVqmEnable based on Integer32"""
    defaultValue = 1

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


_ArrisMtaDevVqmEnable_Type.__name__ = "Integer32"
_ArrisMtaDevVqmEnable_Object = MibScalar
arrisMtaDevVqmEnable = _ArrisMtaDevVqmEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 4, 3),
    _ArrisMtaDevVqmEnable_Type()
)
arrisMtaDevVqmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevVqmEnable.setStatus("current")
_ArrisMtaDevVqmCallNumberTable_Object = MibTable
arrisMtaDevVqmCallNumberTable = _ArrisMtaDevVqmCallNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    arrisMtaDevVqmCallNumberTable.setStatus("current")
_ArrisMtaDevVqmCallNumberEntry_Object = MibTableRow
arrisMtaDevVqmCallNumberEntry = _ArrisMtaDevVqmCallNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 4, 4, 1)
)
arrisMtaDevVqmCallNumberEntry.setIndexNames(
    (0, "ARRIS-MTA-DEVICE-MIB", "arrisMtaDevVqmCallNumberIndex"),
)
if mibBuilder.loadTexts:
    arrisMtaDevVqmCallNumberEntry.setStatus("current")
_ArrisMtaDevVqmCallNumberIndex_Type = Integer32
_ArrisMtaDevVqmCallNumberIndex_Object = MibTableColumn
arrisMtaDevVqmCallNumberIndex = _ArrisMtaDevVqmCallNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 4, 4, 1, 1),
    _ArrisMtaDevVqmCallNumberIndex_Type()
)
arrisMtaDevVqmCallNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisMtaDevVqmCallNumberIndex.setStatus("current")
_ArrisMtaDevVqmCallNumberIds_Type = DisplayString
_ArrisMtaDevVqmCallNumberIds_Object = MibTableColumn
arrisMtaDevVqmCallNumberIds = _ArrisMtaDevVqmCallNumberIds_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 4, 4, 1, 2),
    _ArrisMtaDevVqmCallNumberIds_Type()
)
arrisMtaDevVqmCallNumberIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevVqmCallNumberIds.setStatus("current")


class _ArrisMtaDevVqmCallNumberIdentifier_Type(Integer32):
    """Custom type arrisMtaDevVqmCallNumberIdentifier based on Integer32"""
    defaultValue = 1


_ArrisMtaDevVqmCallNumberIdentifier_Type.__name__ = "Integer32"
_ArrisMtaDevVqmCallNumberIdentifier_Object = MibScalar
arrisMtaDevVqmCallNumberIdentifier = _ArrisMtaDevVqmCallNumberIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 4, 5),
    _ArrisMtaDevVqmCallNumberIdentifier_Type()
)
arrisMtaDevVqmCallNumberIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevVqmCallNumberIdentifier.setStatus("current")
_ArrisMtaDevVqmMetricTable_Object = MibTable
arrisMtaDevVqmMetricTable = _ArrisMtaDevVqmMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 4, 6)
)
if mibBuilder.loadTexts:
    arrisMtaDevVqmMetricTable.setStatus("current")
_ArrisMtaDevVqmMetricEntry_Object = MibTableRow
arrisMtaDevVqmMetricEntry = _ArrisMtaDevVqmMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 4, 6, 1)
)
arrisMtaDevVqmMetricEntry.setIndexNames(
    (0, "ARRIS-MTA-DEVICE-MIB", "arrisMtaDevVqmMetricIndex"),
)
if mibBuilder.loadTexts:
    arrisMtaDevVqmMetricEntry.setStatus("current")


class _ArrisMtaDevVqmMetricIndex_Type(Integer32):
    """Custom type arrisMtaDevVqmMetricIndex based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69)
        )
    )
    namedValues = NamedValues(
        *(("callEndTime", 1),
          ("callStartTime", 2),
          ("callDuration", 3),
          ("lineNumber", 4),
          ("remIpAddress", 5),
          ("cwErrors", 6),
          ("cwErrorRate", 7),
          ("dsSNR", 8),
          ("microReflections", 9),
          ("dsPwr", 10),
          ("usPwr", 11),
          ("eqiAverage", 12),
          ("eqiMin", 13),
          ("eqiMax", 14),
          ("eqiInstantaneous", 15),
          ("mOS-LQ", 16),
          ("mOS-CQ", 17),
          ("rERL", 18),
          ("signalLevel", 19),
          ("noiseLevel", 20),
          ("lossRate", 21),
          ("plConcealment", 22),
          ("discardRate", 23),
          ("burstDensity", 24),
          ("gapDensity", 25),
          ("burstDuration", 26),
          ("gapDuration", 27),
          ("rTDelay", 28),
          ("endSystemDelay", 29),
          ("minGapSize", 30),
          ("rFactor", 31),
          ("extRFactor", 32),
          ("jbAdaptive", 33),
          ("jbRate", 34),
          ("jBNomDelay", 35),
          ("jBMaxDelay", 36),
          ("jBAbsMaxDelay", 37),
          ("mOS-LQRem", 38),
          ("mOS-CQRem", 39),
          ("rERLRem", 40),
          ("signalLevelRem", 41),
          ("noiseLevelRem", 42),
          ("lossRateRem", 43),
          ("plConcealmentRem", 44),
          ("discardRateRem", 45),
          ("burstDensityRem", 46),
          ("gapDensityRem", 47),
          ("burstDurationRem", 48),
          ("gapDurationRem", 49),
          ("rTDelayRem", 50),
          ("endSystemDelayRem", 51),
          ("minGapSizeRem", 52),
          ("rFactorRem", 53),
          ("extRFactorRem", 54),
          ("jbAdaptiveRem", 55),
          ("jbRateRem", 56),
          ("jBNomDelayRem", 57),
          ("jBMaxDelayRem", 58),
          ("jBAbsMaxDelayRem", 59),
          ("txPackets", 60),
          ("txOctets", 61),
          ("rxPackets", 62),
          ("rxOctets", 63),
          ("packetLoss", 64),
          ("intervalJitter", 65),
          ("originator", 66),
          ("intervalJitterRem", 67),
          ("txcodec", 68),
          ("rxcodec", 69))
    )


_ArrisMtaDevVqmMetricIndex_Type.__name__ = "Integer32"
_ArrisMtaDevVqmMetricIndex_Object = MibTableColumn
arrisMtaDevVqmMetricIndex = _ArrisMtaDevVqmMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 4, 6, 1, 1),
    _ArrisMtaDevVqmMetricIndex_Type()
)
arrisMtaDevVqmMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisMtaDevVqmMetricIndex.setStatus("current")
_ArrisMtaDevVqmMetricValues_Type = DisplayString
_ArrisMtaDevVqmMetricValues_Object = MibTableColumn
arrisMtaDevVqmMetricValues = _ArrisMtaDevVqmMetricValues_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 4, 6, 1, 2),
    _ArrisMtaDevVqmMetricValues_Type()
)
arrisMtaDevVqmMetricValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevVqmMetricValues.setStatus("current")
_ArrisMtaDevVqmThresholds_Type = DisplayString
_ArrisMtaDevVqmThresholds_Object = MibTableColumn
arrisMtaDevVqmThresholds = _ArrisMtaDevVqmThresholds_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 4, 6, 1, 3),
    _ArrisMtaDevVqmThresholds_Type()
)
arrisMtaDevVqmThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevVqmThresholds.setStatus("current")


class _ArrisMtaDevVqmEnableRemote_Type(Integer32):
    """Custom type arrisMtaDevVqmEnableRemote based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("forceDisable", 1),
          ("forceEnable", 2),
          ("default", 3))
    )


_ArrisMtaDevVqmEnableRemote_Type.__name__ = "Integer32"
_ArrisMtaDevVqmEnableRemote_Object = MibScalar
arrisMtaDevVqmEnableRemote = _ArrisMtaDevVqmEnableRemote_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 4, 7),
    _ArrisMtaDevVqmEnableRemote_Type()
)
arrisMtaDevVqmEnableRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevVqmEnableRemote.setStatus("current")


class _ArrisMtaDevVqmThresholdEnable_Type(Integer32):
    """Custom type arrisMtaDevVqmThresholdEnable based on Integer32"""
    defaultValue = 0


_ArrisMtaDevVqmThresholdEnable_Type.__name__ = "Integer32"
_ArrisMtaDevVqmThresholdEnable_Object = MibScalar
arrisMtaDevVqmThresholdEnable = _ArrisMtaDevVqmThresholdEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 4, 8),
    _ArrisMtaDevVqmThresholdEnable_Type()
)
arrisMtaDevVqmThresholdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevVqmThresholdEnable.setStatus("current")


class _ArrisMtaDevVqmHistorySize_Type(Integer32):
    """Custom type arrisMtaDevVqmHistorySize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 50),
    )


_ArrisMtaDevVqmHistorySize_Type.__name__ = "Integer32"
_ArrisMtaDevVqmHistorySize_Object = MibScalar
arrisMtaDevVqmHistorySize = _ArrisMtaDevVqmHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 4, 9),
    _ArrisMtaDevVqmHistorySize_Type()
)
arrisMtaDevVqmHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevVqmHistorySize.setStatus("current")
_ArrisMtaDevVqmCallNumberIdentifierLastCall_Type = Integer32
_ArrisMtaDevVqmCallNumberIdentifierLastCall_Object = MibScalar
arrisMtaDevVqmCallNumberIdentifierLastCall = _ArrisMtaDevVqmCallNumberIdentifierLastCall_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 1, 4, 10),
    _ArrisMtaDevVqmCallNumberIdentifierLastCall_Type()
)
arrisMtaDevVqmCallNumberIdentifierLastCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevVqmCallNumberIdentifierLastCall.setStatus("current")
_ArrisMtaDevDhcp_ObjectIdentity = ObjectIdentity
arrisMtaDevDhcp = _ArrisMtaDevDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2)
)
_ArrisMtaDevDhcpMtaParameters_ObjectIdentity = ObjectIdentity
arrisMtaDevDhcpMtaParameters = _ArrisMtaDevDhcpMtaParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 1)
)
_ArrisMtaDevDhcpMtaIpFQDN_Type = SnmpAdminString
_ArrisMtaDevDhcpMtaIpFQDN_Object = MibScalar
arrisMtaDevDhcpMtaIpFQDN = _ArrisMtaDevDhcpMtaIpFQDN_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 1, 1),
    _ArrisMtaDevDhcpMtaIpFQDN_Type()
)
arrisMtaDevDhcpMtaIpFQDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpMtaIpFQDN.setStatus("current")
_ArrisMtaDevDhcpMtaIpAddr_Type = IpAddress
_ArrisMtaDevDhcpMtaIpAddr_Object = MibScalar
arrisMtaDevDhcpMtaIpAddr = _ArrisMtaDevDhcpMtaIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 1, 2),
    _ArrisMtaDevDhcpMtaIpAddr_Type()
)
arrisMtaDevDhcpMtaIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpMtaIpAddr.setStatus("current")
_ArrisMtaDevDhcpMtaSubNetMask_Type = IpAddress
_ArrisMtaDevDhcpMtaSubNetMask_Object = MibScalar
arrisMtaDevDhcpMtaSubNetMask = _ArrisMtaDevDhcpMtaSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 1, 3),
    _ArrisMtaDevDhcpMtaSubNetMask_Type()
)
arrisMtaDevDhcpMtaSubNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpMtaSubNetMask.setStatus("current")
_ArrisMtaDevDhcpMtaGatewayIpAddr_Type = IpAddress
_ArrisMtaDevDhcpMtaGatewayIpAddr_Object = MibScalar
arrisMtaDevDhcpMtaGatewayIpAddr = _ArrisMtaDevDhcpMtaGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 1, 4),
    _ArrisMtaDevDhcpMtaGatewayIpAddr_Type()
)
arrisMtaDevDhcpMtaGatewayIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpMtaGatewayIpAddr.setStatus("current")
_ArrisMtaDevDhcpMtaConfigFile_Type = SnmpAdminString
_ArrisMtaDevDhcpMtaConfigFile_Object = MibScalar
arrisMtaDevDhcpMtaConfigFile = _ArrisMtaDevDhcpMtaConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 1, 5),
    _ArrisMtaDevDhcpMtaConfigFile_Type()
)
arrisMtaDevDhcpMtaConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpMtaConfigFile.setStatus("current")
_ArrisMtaDevDhcpSvrParameters_ObjectIdentity = ObjectIdentity
arrisMtaDevDhcpSvrParameters = _ArrisMtaDevDhcpSvrParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 2)
)


class _ArrisMtaDevDhcpState_Type(Integer32):
    """Custom type arrisMtaDevDhcpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("discover", 1),
          ("selecting", 2),
          ("requesting", 3),
          ("bound", 4),
          ("renew", 5),
          ("rebind", 6))
    )


_ArrisMtaDevDhcpState_Type.__name__ = "Integer32"
_ArrisMtaDevDhcpState_Object = MibScalar
arrisMtaDevDhcpState = _ArrisMtaDevDhcpState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 2, 1),
    _ArrisMtaDevDhcpState_Type()
)
arrisMtaDevDhcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpState.setStatus("current")
_ArrisMtaDevDhcpPrimaryDhcpSvrIpAddr_Type = IpAddress
_ArrisMtaDevDhcpPrimaryDhcpSvrIpAddr_Object = MibScalar
arrisMtaDevDhcpPrimaryDhcpSvrIpAddr = _ArrisMtaDevDhcpPrimaryDhcpSvrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 2, 2),
    _ArrisMtaDevDhcpPrimaryDhcpSvrIpAddr_Type()
)
arrisMtaDevDhcpPrimaryDhcpSvrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpPrimaryDhcpSvrIpAddr.setStatus("current")
_ArrisMtaDevDhcpSecondaryDhcpSvrIpAddr_Type = IpAddress
_ArrisMtaDevDhcpSecondaryDhcpSvrIpAddr_Object = MibScalar
arrisMtaDevDhcpSecondaryDhcpSvrIpAddr = _ArrisMtaDevDhcpSecondaryDhcpSvrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 2, 3),
    _ArrisMtaDevDhcpSecondaryDhcpSvrIpAddr_Type()
)
arrisMtaDevDhcpSecondaryDhcpSvrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpSecondaryDhcpSvrIpAddr.setStatus("current")
_ArrisMtaDevDhcpPrimaryDNSSvrIpAddr_Type = IpAddress
_ArrisMtaDevDhcpPrimaryDNSSvrIpAddr_Object = MibScalar
arrisMtaDevDhcpPrimaryDNSSvrIpAddr = _ArrisMtaDevDhcpPrimaryDNSSvrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 2, 4),
    _ArrisMtaDevDhcpPrimaryDNSSvrIpAddr_Type()
)
arrisMtaDevDhcpPrimaryDNSSvrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpPrimaryDNSSvrIpAddr.setStatus("current")
_ArrisMtaDevDhcpSecondaryDNSSvrIpAddr_Type = IpAddress
_ArrisMtaDevDhcpSecondaryDNSSvrIpAddr_Object = MibScalar
arrisMtaDevDhcpSecondaryDNSSvrIpAddr = _ArrisMtaDevDhcpSecondaryDNSSvrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 2, 5),
    _ArrisMtaDevDhcpSecondaryDNSSvrIpAddr_Type()
)
arrisMtaDevDhcpSecondaryDNSSvrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpSecondaryDNSSvrIpAddr.setStatus("current")
_ArrisMtaDevDhcpLeaseParameters_ObjectIdentity = ObjectIdentity
arrisMtaDevDhcpLeaseParameters = _ArrisMtaDevDhcpLeaseParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 3)
)
_ArrisMtaDevDhcpOfferedLeaseTime_Type = Integer32
_ArrisMtaDevDhcpOfferedLeaseTime_Object = MibScalar
arrisMtaDevDhcpOfferedLeaseTime = _ArrisMtaDevDhcpOfferedLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 3, 1),
    _ArrisMtaDevDhcpOfferedLeaseTime_Type()
)
arrisMtaDevDhcpOfferedLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpOfferedLeaseTime.setStatus("current")
_ArrisMtaDevDhcpLeaseTimeRemaining_Type = Integer32
_ArrisMtaDevDhcpLeaseTimeRemaining_Object = MibScalar
arrisMtaDevDhcpLeaseTimeRemaining = _ArrisMtaDevDhcpLeaseTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 3, 2),
    _ArrisMtaDevDhcpLeaseTimeRemaining_Type()
)
arrisMtaDevDhcpLeaseTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpLeaseTimeRemaining.setStatus("current")
_ArrisMtaDevDhcpTimeUntilRenew_Type = Integer32
_ArrisMtaDevDhcpTimeUntilRenew_Object = MibScalar
arrisMtaDevDhcpTimeUntilRenew = _ArrisMtaDevDhcpTimeUntilRenew_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 3, 3),
    _ArrisMtaDevDhcpTimeUntilRenew_Type()
)
arrisMtaDevDhcpTimeUntilRenew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpTimeUntilRenew.setStatus("current")
_ArrisMtaDevDhcpTimeUntilRebind_Type = Integer32
_ArrisMtaDevDhcpTimeUntilRebind_Object = MibScalar
arrisMtaDevDhcpTimeUntilRebind = _ArrisMtaDevDhcpTimeUntilRebind_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 3, 4),
    _ArrisMtaDevDhcpTimeUntilRebind_Type()
)
arrisMtaDevDhcpTimeUntilRebind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpTimeUntilRebind.setStatus("current")
_ArrisMtaDevDhcpPktcOptParameters_ObjectIdentity = ObjectIdentity
arrisMtaDevDhcpPktcOptParameters = _ArrisMtaDevDhcpPktcOptParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 4)
)
_ArrisMtaDevDhcpPktcOptionId_Type = Integer32
_ArrisMtaDevDhcpPktcOptionId_Object = MibScalar
arrisMtaDevDhcpPktcOptionId = _ArrisMtaDevDhcpPktcOptionId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 4, 1),
    _ArrisMtaDevDhcpPktcOptionId_Type()
)
arrisMtaDevDhcpPktcOptionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpPktcOptionId.setStatus("current")
_ArrisMtaDevDhcpSvcProviderSnmpEntity_Type = SnmpAdminString
_ArrisMtaDevDhcpSvcProviderSnmpEntity_Object = MibScalar
arrisMtaDevDhcpSvcProviderSnmpEntity = _ArrisMtaDevDhcpSvcProviderSnmpEntity_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 4, 2),
    _ArrisMtaDevDhcpSvcProviderSnmpEntity_Type()
)
arrisMtaDevDhcpSvcProviderSnmpEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpSvcProviderSnmpEntity.setStatus("current")
_ArrisMtaDevDhcpKerberosRealmFqdn_Type = SnmpAdminString
_ArrisMtaDevDhcpKerberosRealmFqdn_Object = MibScalar
arrisMtaDevDhcpKerberosRealmFqdn = _ArrisMtaDevDhcpKerberosRealmFqdn_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 4, 3),
    _ArrisMtaDevDhcpKerberosRealmFqdn_Type()
)
arrisMtaDevDhcpKerberosRealmFqdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpKerberosRealmFqdn.setStatus("current")
_ArrisMtaDevDhcpRequestTgt_Type = SnmpAdminString
_ArrisMtaDevDhcpRequestTgt_Object = MibScalar
arrisMtaDevDhcpRequestTgt = _ArrisMtaDevDhcpRequestTgt_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 4, 4),
    _ArrisMtaDevDhcpRequestTgt_Type()
)
arrisMtaDevDhcpRequestTgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpRequestTgt.setStatus("current")
_ArrisMtaDevDhcpProvTimer_Type = Integer32
_ArrisMtaDevDhcpProvTimer_Object = MibScalar
arrisMtaDevDhcpProvTimer = _ArrisMtaDevDhcpProvTimer_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 4, 5),
    _ArrisMtaDevDhcpProvTimer_Type()
)
arrisMtaDevDhcpProvTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpProvTimer.setStatus("current")


class _ArrisMtaDevDhcpSecTicketInvalid_Type(Bits):
    """Custom type arrisMtaDevDhcpSecTicketInvalid based on Bits"""
    namedValues = NamedValues(
        *(("invalidateProvOnReboot", 0),
          ("invalidateAllCmsOnReboot", 1))
    )

_ArrisMtaDevDhcpSecTicketInvalid_Type.__name__ = "Bits"
_ArrisMtaDevDhcpSecTicketInvalid_Object = MibScalar
arrisMtaDevDhcpSecTicketInvalid = _ArrisMtaDevDhcpSecTicketInvalid_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 1, 2, 4, 6),
    _ArrisMtaDevDhcpSecTicketInvalid_Type()
)
arrisMtaDevDhcpSecTicketInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpSecTicketInvalid.setStatus("current")
_ArrisMtaDevSetup_ObjectIdentity = ObjectIdentity
arrisMtaDevSetup = _ArrisMtaDevSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2)
)
_ArrisMtaDevOperationalSetup_ObjectIdentity = ObjectIdentity
arrisMtaDevOperationalSetup = _ArrisMtaDevOperationalSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3)
)


class _ArrisMtaDevVPNomJitterBuffer_Type(Integer32):
    """Custom type arrisMtaDevVPNomJitterBuffer based on Integer32"""
    defaultValue = 1

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
        *(("packetizationRatex1", 1),
          ("packetizationRatex2", 2),
          ("packetizationRatex3", 3),
          ("packetizationRatex4", 4))
    )


_ArrisMtaDevVPNomJitterBuffer_Type.__name__ = "Integer32"
_ArrisMtaDevVPNomJitterBuffer_Object = MibScalar
arrisMtaDevVPNomJitterBuffer = _ArrisMtaDevVPNomJitterBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 1),
    _ArrisMtaDevVPNomJitterBuffer_Type()
)
arrisMtaDevVPNomJitterBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevVPNomJitterBuffer.setStatus("current")


class _ArrisMtaDevVPJitterBufferMode_Type(Integer32):
    """Custom type arrisMtaDevVPJitterBufferMode based on Integer32"""
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
        *(("adaptive", 1),
          ("fixed", 2),
          ("auto", 3))
    )


_ArrisMtaDevVPJitterBufferMode_Type.__name__ = "Integer32"
_ArrisMtaDevVPJitterBufferMode_Object = MibScalar
arrisMtaDevVPJitterBufferMode = _ArrisMtaDevVPJitterBufferMode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 2),
    _ArrisMtaDevVPJitterBufferMode_Type()
)
arrisMtaDevVPJitterBufferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevVPJitterBufferMode.setStatus("current")


class _ArrisMtaDevRTPTxQueueSize_Type(Integer32):
    """Custom type arrisMtaDevRTPTxQueueSize based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 20),
    )


_ArrisMtaDevRTPTxQueueSize_Type.__name__ = "Integer32"
_ArrisMtaDevRTPTxQueueSize_Object = MibScalar
arrisMtaDevRTPTxQueueSize = _ArrisMtaDevRTPTxQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 3),
    _ArrisMtaDevRTPTxQueueSize_Type()
)
arrisMtaDevRTPTxQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevRTPTxQueueSize.setStatus("current")


class _ArrisMtaDevEchoCancellerTailLength_Type(Integer32):
    """Custom type arrisMtaDevEchoCancellerTailLength based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eightMs", 1),
          ("thirtyTwoMs", 2))
    )


_ArrisMtaDevEchoCancellerTailLength_Type.__name__ = "Integer32"
_ArrisMtaDevEchoCancellerTailLength_Object = MibScalar
arrisMtaDevEchoCancellerTailLength = _ArrisMtaDevEchoCancellerTailLength_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 4),
    _ArrisMtaDevEchoCancellerTailLength_Type()
)
arrisMtaDevEchoCancellerTailLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEchoCancellerTailLength.setStatus("current")


class _ArrisMtaDevDspHandleNonPhaseReversedTone_Type(Integer32):
    """Custom type arrisMtaDevDspHandleNonPhaseReversedTone based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("onECANEnable", 2),
          ("onECANDisabled", 3))
    )


_ArrisMtaDevDspHandleNonPhaseReversedTone_Type.__name__ = "Integer32"
_ArrisMtaDevDspHandleNonPhaseReversedTone_Object = MibScalar
arrisMtaDevDspHandleNonPhaseReversedTone = _ArrisMtaDevDspHandleNonPhaseReversedTone_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 5),
    _ArrisMtaDevDspHandleNonPhaseReversedTone_Type()
)
arrisMtaDevDspHandleNonPhaseReversedTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevDspHandleNonPhaseReversedTone.setStatus("current")
_ArrisMtaDevProvMethodIndicator_Type = ArrsMtaDevProvMethod
_ArrisMtaDevProvMethodIndicator_Object = MibScalar
arrisMtaDevProvMethodIndicator = _ArrisMtaDevProvMethodIndicator_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 6),
    _ArrisMtaDevProvMethodIndicator_Type()
)
arrisMtaDevProvMethodIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevProvMethodIndicator.setStatus("current")
_ArrisMtaCfgRTPDynPortStart_Type = Integer32
_ArrisMtaCfgRTPDynPortStart_Object = MibScalar
arrisMtaCfgRTPDynPortStart = _ArrisMtaCfgRTPDynPortStart_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 7),
    _ArrisMtaCfgRTPDynPortStart_Type()
)
arrisMtaCfgRTPDynPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaCfgRTPDynPortStart.setStatus("current")
_ArrisMtaCfgRTPDynPortEnd_Type = Integer32
_ArrisMtaCfgRTPDynPortEnd_Object = MibScalar
arrisMtaCfgRTPDynPortEnd = _ArrisMtaCfgRTPDynPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 8),
    _ArrisMtaCfgRTPDynPortEnd_Type()
)
arrisMtaCfgRTPDynPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaCfgRTPDynPortEnd.setStatus("current")


class _ArrisMtaDevVPMaxJitterBuffer_Type(Integer32):
    """Custom type arrisMtaDevVPMaxJitterBuffer based on Integer32"""
    defaultValue = 6

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
        *(("packetizationRatex1", 1),
          ("packetizationRatex2", 2),
          ("packetizationRatex3", 3),
          ("packetizationRatex4", 4),
          ("packetizationRatex5", 5),
          ("packetizationRatex6", 6))
    )


_ArrisMtaDevVPMaxJitterBuffer_Type.__name__ = "Integer32"
_ArrisMtaDevVPMaxJitterBuffer_Object = MibScalar
arrisMtaDevVPMaxJitterBuffer = _ArrisMtaDevVPMaxJitterBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 9),
    _ArrisMtaDevVPMaxJitterBuffer_Type()
)
arrisMtaDevVPMaxJitterBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevVPMaxJitterBuffer.setStatus("current")
_ArrisMtaDevOptionality_ObjectIdentity = ObjectIdentity
arrisMtaDevOptionality = _ArrisMtaDevOptionality_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 10)
)
_ArrisMtaDevOptionality8ChnlKey_Type = SnmpAdminString
_ArrisMtaDevOptionality8ChnlKey_Object = MibScalar
arrisMtaDevOptionality8ChnlKey = _ArrisMtaDevOptionality8ChnlKey_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 10, 1),
    _ArrisMtaDevOptionality8ChnlKey_Type()
)
arrisMtaDevOptionality8ChnlKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevOptionality8ChnlKey.setStatus("deprecated")


class _ArrisMtaDevOptionality8ChnlEnable_Type(Integer32):
    """Custom type arrisMtaDevOptionality8ChnlEnable based on Integer32"""
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
        *(("enabled", 1),
          ("disabled", 2),
          ("enabled-needs-to-be-reset", 3),
          ("disabled-needs-to-be-reset", 4))
    )


_ArrisMtaDevOptionality8ChnlEnable_Type.__name__ = "Integer32"
_ArrisMtaDevOptionality8ChnlEnable_Object = MibScalar
arrisMtaDevOptionality8ChnlEnable = _ArrisMtaDevOptionality8ChnlEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 10, 2),
    _ArrisMtaDevOptionality8ChnlEnable_Type()
)
arrisMtaDevOptionality8ChnlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevOptionality8ChnlEnable.setStatus("deprecated")
_ArrisMtaDevOptionalityLoopDiagKey_Type = SnmpAdminString
_ArrisMtaDevOptionalityLoopDiagKey_Object = MibScalar
arrisMtaDevOptionalityLoopDiagKey = _ArrisMtaDevOptionalityLoopDiagKey_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 10, 3),
    _ArrisMtaDevOptionalityLoopDiagKey_Type()
)
arrisMtaDevOptionalityLoopDiagKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevOptionalityLoopDiagKey.setStatus("deprecated")
_ArrisMtaDevLoopVoltageMgmt_ObjectIdentity = ObjectIdentity
arrisMtaDevLoopVoltageMgmt = _ArrisMtaDevLoopVoltageMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 11)
)
_ArrisMtaDevLoopVoltageKey_Type = SnmpAdminString
_ArrisMtaDevLoopVoltageKey_Object = MibScalar
arrisMtaDevLoopVoltageKey = _ArrisMtaDevLoopVoltageKey_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 11, 1),
    _ArrisMtaDevLoopVoltageKey_Type()
)
arrisMtaDevLoopVoltageKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevLoopVoltageKey.setStatus("current")


class _ArrisMtaDevLoopVoltagePolicy_Type(Integer32):
    """Custom type arrisMtaDevLoopVoltagePolicy based on Integer32"""
    defaultValue = 4

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
        *(("always-voltage-present", 1),
          ("rf-carrier-voltage-present", 2),
          ("in-service-voltage-present", 3),
          ("default-operation", 4))
    )


_ArrisMtaDevLoopVoltagePolicy_Type.__name__ = "Integer32"
_ArrisMtaDevLoopVoltagePolicy_Object = MibScalar
arrisMtaDevLoopVoltagePolicy = _ArrisMtaDevLoopVoltagePolicy_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 11, 2),
    _ArrisMtaDevLoopVoltagePolicy_Type()
)
arrisMtaDevLoopVoltagePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevLoopVoltagePolicy.setStatus("current")


class _ArrisMtaDevLoopVoltageResetTimeout_Type(Integer32):
    """Custom type arrisMtaDevLoopVoltageResetTimeout based on Integer32"""
    defaultValue = 300


_ArrisMtaDevLoopVoltageResetTimeout_Type.__name__ = "Integer32"
_ArrisMtaDevLoopVoltageResetTimeout_Object = MibScalar
arrisMtaDevLoopVoltageResetTimeout = _ArrisMtaDevLoopVoltageResetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 11, 3),
    _ArrisMtaDevLoopVoltageResetTimeout_Type()
)
arrisMtaDevLoopVoltageResetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevLoopVoltageResetTimeout.setStatus("current")
if mibBuilder.loadTexts:
    arrisMtaDevLoopVoltageResetTimeout.setUnits("seconds")


class _ArrisMtaDevLoopVoltageMaintTimeout_Type(Integer32):
    """Custom type arrisMtaDevLoopVoltageMaintTimeout based on Integer32"""
    defaultValue = 0


_ArrisMtaDevLoopVoltageMaintTimeout_Type.__name__ = "Integer32"
_ArrisMtaDevLoopVoltageMaintTimeout_Object = MibScalar
arrisMtaDevLoopVoltageMaintTimeout = _ArrisMtaDevLoopVoltageMaintTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 11, 4),
    _ArrisMtaDevLoopVoltageMaintTimeout_Type()
)
arrisMtaDevLoopVoltageMaintTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevLoopVoltageMaintTimeout.setStatus("current")
if mibBuilder.loadTexts:
    arrisMtaDevLoopVoltageMaintTimeout.setUnits("minutes")
_ArrisMtaDevGainControl_ObjectIdentity = ObjectIdentity
arrisMtaDevGainControl = _ArrisMtaDevGainControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 12)
)


class _ArrisMtaDevGainControlFSK_Type(Integer32):
    """Custom type arrisMtaDevGainControlFSK based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 2),
    )


_ArrisMtaDevGainControlFSK_Type.__name__ = "Integer32"
_ArrisMtaDevGainControlFSK_Object = MibScalar
arrisMtaDevGainControlFSK = _ArrisMtaDevGainControlFSK_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 12, 1),
    _ArrisMtaDevGainControlFSK_Type()
)
arrisMtaDevGainControlFSK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevGainControlFSK.setStatus("current")


class _ArrisMtaDevGainControlCAS_Type(Integer32):
    """Custom type arrisMtaDevGainControlCAS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2),
    )


_ArrisMtaDevGainControlCAS_Type.__name__ = "Integer32"
_ArrisMtaDevGainControlCAS_Object = MibScalar
arrisMtaDevGainControlCAS = _ArrisMtaDevGainControlCAS_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 12, 2),
    _ArrisMtaDevGainControlCAS_Type()
)
arrisMtaDevGainControlCAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevGainControlCAS.setStatus("current")


class _ArrisMtaDevGainControlLocalTone_Type(Integer32):
    """Custom type arrisMtaDevGainControlLocalTone based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2),
    )


_ArrisMtaDevGainControlLocalTone_Type.__name__ = "Integer32"
_ArrisMtaDevGainControlLocalTone_Object = MibScalar
arrisMtaDevGainControlLocalTone = _ArrisMtaDevGainControlLocalTone_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 12, 3),
    _ArrisMtaDevGainControlLocalTone_Type()
)
arrisMtaDevGainControlLocalTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevGainControlLocalTone.setStatus("current")


class _ArrisMtaDevGainControlNetworkTone_Type(Integer32):
    """Custom type arrisMtaDevGainControlNetworkTone based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2),
    )


_ArrisMtaDevGainControlNetworkTone_Type.__name__ = "Integer32"
_ArrisMtaDevGainControlNetworkTone_Object = MibScalar
arrisMtaDevGainControlNetworkTone = _ArrisMtaDevGainControlNetworkTone_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 12, 4),
    _ArrisMtaDevGainControlNetworkTone_Type()
)
arrisMtaDevGainControlNetworkTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevGainControlNetworkTone.setStatus("current")


class _ArrisMtaDevGainControlLocalDTMF_Type(Integer32):
    """Custom type arrisMtaDevGainControlLocalDTMF based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 9),
    )


_ArrisMtaDevGainControlLocalDTMF_Type.__name__ = "Integer32"
_ArrisMtaDevGainControlLocalDTMF_Object = MibScalar
arrisMtaDevGainControlLocalDTMF = _ArrisMtaDevGainControlLocalDTMF_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 12, 5),
    _ArrisMtaDevGainControlLocalDTMF_Type()
)
arrisMtaDevGainControlLocalDTMF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevGainControlLocalDTMF.setStatus("current")


class _ArrisMtaDevGainControlNetworkDTMF_Type(Integer32):
    """Custom type arrisMtaDevGainControlNetworkDTMF based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9, 9),
    )


_ArrisMtaDevGainControlNetworkDTMF_Type.__name__ = "Integer32"
_ArrisMtaDevGainControlNetworkDTMF_Object = MibScalar
arrisMtaDevGainControlNetworkDTMF = _ArrisMtaDevGainControlNetworkDTMF_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 12, 6),
    _ArrisMtaDevGainControlNetworkDTMF_Type()
)
arrisMtaDevGainControlNetworkDTMF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevGainControlNetworkDTMF.setStatus("current")


class _ArrisMtaDevGainControlTxVoice_Type(Integer32):
    """Custom type arrisMtaDevGainControlTxVoice based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-16, 16),
    )


_ArrisMtaDevGainControlTxVoice_Type.__name__ = "Integer32"
_ArrisMtaDevGainControlTxVoice_Object = MibScalar
arrisMtaDevGainControlTxVoice = _ArrisMtaDevGainControlTxVoice_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 12, 7),
    _ArrisMtaDevGainControlTxVoice_Type()
)
arrisMtaDevGainControlTxVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevGainControlTxVoice.setStatus("current")


class _ArrisMtaDevGainControlRxVoice_Type(Integer32):
    """Custom type arrisMtaDevGainControlRxVoice based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-16, 16),
    )


_ArrisMtaDevGainControlRxVoice_Type.__name__ = "Integer32"
_ArrisMtaDevGainControlRxVoice_Object = MibScalar
arrisMtaDevGainControlRxVoice = _ArrisMtaDevGainControlRxVoice_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 12, 8),
    _ArrisMtaDevGainControlRxVoice_Type()
)
arrisMtaDevGainControlRxVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevGainControlRxVoice.setStatus("current")


class _ArrisMtaDevEnableIndexTenEleven_Type(Integer32):
    """Custom type arrisMtaDevEnableIndexTenEleven based on Integer32"""
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


_ArrisMtaDevEnableIndexTenEleven_Type.__name__ = "Integer32"
_ArrisMtaDevEnableIndexTenEleven_Object = MibScalar
arrisMtaDevEnableIndexTenEleven = _ArrisMtaDevEnableIndexTenEleven_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 13),
    _ArrisMtaDevEnableIndexTenEleven_Type()
)
arrisMtaDevEnableIndexTenEleven.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEnableIndexTenEleven.setStatus("current")


class _ArrisMtaDevDspCpsSetting_Type(Integer32):
    """Custom type arrisMtaDevDspCpsSetting based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ArrisMtaDevDspCpsSetting_Type.__name__ = "Integer32"
_ArrisMtaDevDspCpsSetting_Object = MibScalar
arrisMtaDevDspCpsSetting = _ArrisMtaDevDspCpsSetting_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 14),
    _ArrisMtaDevDspCpsSetting_Type()
)
arrisMtaDevDspCpsSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevDspCpsSetting.setStatus("current")
_ArrisMtaDevDiag_ObjectIdentity = ObjectIdentity
arrisMtaDevDiag = _ArrisMtaDevDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 15)
)
_ArrisMtaDevDiagLoopTable_Object = MibTable
arrisMtaDevDiagLoopTable = _ArrisMtaDevDiagLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 15, 1)
)
if mibBuilder.loadTexts:
    arrisMtaDevDiagLoopTable.setStatus("current")
_ArrisMtaDevDiagLoopEntry_Object = MibTableRow
arrisMtaDevDiagLoopEntry = _ArrisMtaDevDiagLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 15, 1, 1)
)
arrisMtaDevDiagLoopEntry.setIndexNames(
    (0, "ARRIS-MTA-DEVICE-MIB", "arrisMtaDevDiagLoopIndex"),
)
if mibBuilder.loadTexts:
    arrisMtaDevDiagLoopEntry.setStatus("current")
_ArrisMtaDevDiagLoopIndex_Type = Integer32
_ArrisMtaDevDiagLoopIndex_Object = MibTableColumn
arrisMtaDevDiagLoopIndex = _ArrisMtaDevDiagLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 15, 1, 1, 1),
    _ArrisMtaDevDiagLoopIndex_Type()
)
arrisMtaDevDiagLoopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisMtaDevDiagLoopIndex.setStatus("current")
_ArrisMtaDevDiagLoopTime_Type = DisplayString
_ArrisMtaDevDiagLoopTime_Object = MibTableColumn
arrisMtaDevDiagLoopTime = _ArrisMtaDevDiagLoopTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 15, 1, 1, 2),
    _ArrisMtaDevDiagLoopTime_Type()
)
arrisMtaDevDiagLoopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDiagLoopTime.setStatus("current")
_ArrisMtaDevDiagLoopRequest_Type = TruthValue
_ArrisMtaDevDiagLoopRequest_Object = MibTableColumn
arrisMtaDevDiagLoopRequest = _ArrisMtaDevDiagLoopRequest_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 15, 1, 1, 3),
    _ArrisMtaDevDiagLoopRequest_Type()
)
arrisMtaDevDiagLoopRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevDiagLoopRequest.setStatus("current")


class _ArrisMtaDevDiagLoopLastResult_Type(Integer32):
    """Custom type arrisMtaDevDiagLoopLastResult based on Integer32"""
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
        *(("diagnostics-passed", 1),
          ("hazardous-potential-test-failure", 2),
          ("foreign-emf-test-failure", 3),
          ("resistive-faults-test-failure", 4),
          ("receiver-offhook-test-failure", 5),
          ("ringer-test-failure", 6),
          ("invalid-state-to-init-diags", 7),
          ("line-is-unprovisioned", 8),
          ("diagnostics-results-pending", 9),
          ("not-started", 10),
          ("unsupported", 11),
          ("ringer-test-warning", 12))
    )


_ArrisMtaDevDiagLoopLastResult_Type.__name__ = "Integer32"
_ArrisMtaDevDiagLoopLastResult_Object = MibTableColumn
arrisMtaDevDiagLoopLastResult = _ArrisMtaDevDiagLoopLastResult_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 15, 1, 1, 4),
    _ArrisMtaDevDiagLoopLastResult_Type()
)
arrisMtaDevDiagLoopLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDiagLoopLastResult.setStatus("current")
_ArrisMtaDevDiagLoopHazardousPotentialTest_Type = DisplayString
_ArrisMtaDevDiagLoopHazardousPotentialTest_Object = MibTableColumn
arrisMtaDevDiagLoopHazardousPotentialTest = _ArrisMtaDevDiagLoopHazardousPotentialTest_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 15, 1, 1, 5),
    _ArrisMtaDevDiagLoopHazardousPotentialTest_Type()
)
arrisMtaDevDiagLoopHazardousPotentialTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDiagLoopHazardousPotentialTest.setStatus("current")
_ArrisMtaDevDiagLoopForeignEmfTest_Type = DisplayString
_ArrisMtaDevDiagLoopForeignEmfTest_Object = MibTableColumn
arrisMtaDevDiagLoopForeignEmfTest = _ArrisMtaDevDiagLoopForeignEmfTest_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 15, 1, 1, 6),
    _ArrisMtaDevDiagLoopForeignEmfTest_Type()
)
arrisMtaDevDiagLoopForeignEmfTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDiagLoopForeignEmfTest.setStatus("current")
_ArrisMtaDevDiagLoopResistiveFaultsTest_Type = DisplayString
_ArrisMtaDevDiagLoopResistiveFaultsTest_Object = MibTableColumn
arrisMtaDevDiagLoopResistiveFaultsTest = _ArrisMtaDevDiagLoopResistiveFaultsTest_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 15, 1, 1, 7),
    _ArrisMtaDevDiagLoopResistiveFaultsTest_Type()
)
arrisMtaDevDiagLoopResistiveFaultsTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDiagLoopResistiveFaultsTest.setStatus("current")
_ArrisMtaDevDiagLoopReceiverOffHookTest_Type = DisplayString
_ArrisMtaDevDiagLoopReceiverOffHookTest_Object = MibTableColumn
arrisMtaDevDiagLoopReceiverOffHookTest = _ArrisMtaDevDiagLoopReceiverOffHookTest_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 15, 1, 1, 8),
    _ArrisMtaDevDiagLoopReceiverOffHookTest_Type()
)
arrisMtaDevDiagLoopReceiverOffHookTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDiagLoopReceiverOffHookTest.setStatus("current")
_ArrisMtaDevDiagLoopRingerTest_Type = DisplayString
_ArrisMtaDevDiagLoopRingerTest_Object = MibTableColumn
arrisMtaDevDiagLoopRingerTest = _ArrisMtaDevDiagLoopRingerTest_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 15, 1, 1, 9),
    _ArrisMtaDevDiagLoopRingerTest_Type()
)
arrisMtaDevDiagLoopRingerTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDiagLoopRingerTest.setStatus("current")


class _ArrisMtaDevVbdOverwriteLineBitmap_Type(Integer32):
    """Custom type arrisMtaDevVbdOverwriteLineBitmap based on Integer32"""
    defaultValue = 0


_ArrisMtaDevVbdOverwriteLineBitmap_Type.__name__ = "Integer32"
_ArrisMtaDevVbdOverwriteLineBitmap_Object = MibScalar
arrisMtaDevVbdOverwriteLineBitmap = _ArrisMtaDevVbdOverwriteLineBitmap_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 16),
    _ArrisMtaDevVbdOverwriteLineBitmap_Type()
)
arrisMtaDevVbdOverwriteLineBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevVbdOverwriteLineBitmap.setStatus("current")


class _ArrisMtaDevVbdOverwriteMinJitterBuffer_Type(Integer32):
    """Custom type arrisMtaDevVbdOverwriteMinJitterBuffer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 160),
    )


_ArrisMtaDevVbdOverwriteMinJitterBuffer_Type.__name__ = "Integer32"
_ArrisMtaDevVbdOverwriteMinJitterBuffer_Object = MibScalar
arrisMtaDevVbdOverwriteMinJitterBuffer = _ArrisMtaDevVbdOverwriteMinJitterBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 17),
    _ArrisMtaDevVbdOverwriteMinJitterBuffer_Type()
)
arrisMtaDevVbdOverwriteMinJitterBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevVbdOverwriteMinJitterBuffer.setStatus("current")


class _ArrisMtaDevVbdOverwriteNomJitterBuffer_Type(Integer32):
    """Custom type arrisMtaDevVbdOverwriteNomJitterBuffer based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 160),
    )


_ArrisMtaDevVbdOverwriteNomJitterBuffer_Type.__name__ = "Integer32"
_ArrisMtaDevVbdOverwriteNomJitterBuffer_Object = MibScalar
arrisMtaDevVbdOverwriteNomJitterBuffer = _ArrisMtaDevVbdOverwriteNomJitterBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 18),
    _ArrisMtaDevVbdOverwriteNomJitterBuffer_Type()
)
arrisMtaDevVbdOverwriteNomJitterBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevVbdOverwriteNomJitterBuffer.setStatus("current")


class _ArrisMtaDevVbdOverwriteMaxJitterBuffer_Type(Integer32):
    """Custom type arrisMtaDevVbdOverwriteMaxJitterBuffer based on Integer32"""
    defaultValue = 160

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 160),
    )


_ArrisMtaDevVbdOverwriteMaxJitterBuffer_Type.__name__ = "Integer32"
_ArrisMtaDevVbdOverwriteMaxJitterBuffer_Object = MibScalar
arrisMtaDevVbdOverwriteMaxJitterBuffer = _ArrisMtaDevVbdOverwriteMaxJitterBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 19),
    _ArrisMtaDevVbdOverwriteMaxJitterBuffer_Type()
)
arrisMtaDevVbdOverwriteMaxJitterBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevVbdOverwriteMaxJitterBuffer.setStatus("current")


class _ArrisMtaDevEventHideFQDNandIPAddress_Type(Integer32):
    """Custom type arrisMtaDevEventHideFQDNandIPAddress based on Integer32"""
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


_ArrisMtaDevEventHideFQDNandIPAddress_Type.__name__ = "Integer32"
_ArrisMtaDevEventHideFQDNandIPAddress_Object = MibScalar
arrisMtaDevEventHideFQDNandIPAddress = _ArrisMtaDevEventHideFQDNandIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 20),
    _ArrisMtaDevEventHideFQDNandIPAddress_Type()
)
arrisMtaDevEventHideFQDNandIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEventHideFQDNandIPAddress.setStatus("current")


class _ArrisMtaDevDhcpOptionOverride_Type(Integer32):
    """Custom type arrisMtaDevDhcpOptionOverride based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ArrisMtaDevDhcpOptionOverride_Type.__name__ = "Integer32"
_ArrisMtaDevDhcpOptionOverride_Object = MibScalar
arrisMtaDevDhcpOptionOverride = _ArrisMtaDevDhcpOptionOverride_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 21),
    _ArrisMtaDevDhcpOptionOverride_Type()
)
arrisMtaDevDhcpOptionOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpOptionOverride.setStatus("current")
_ArrisMtaDevTFTPServerAddrOverrideFQDN_Type = DisplayString
_ArrisMtaDevTFTPServerAddrOverrideFQDN_Object = MibScalar
arrisMtaDevTFTPServerAddrOverrideFQDN = _ArrisMtaDevTFTPServerAddrOverrideFQDN_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 22),
    _ArrisMtaDevTFTPServerAddrOverrideFQDN_Type()
)
arrisMtaDevTFTPServerAddrOverrideFQDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevTFTPServerAddrOverrideFQDN.setStatus("current")


class _ArrisMtaDevDefaultReasonNoCIDName_Type(Integer32):
    """Custom type arrisMtaDevDefaultReasonNoCIDName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 0),
          ("private", 1),
          ("sendnothing", 2),
          ("sdmf", 3),
          ("excludeName", 4))
    )


_ArrisMtaDevDefaultReasonNoCIDName_Type.__name__ = "Integer32"
_ArrisMtaDevDefaultReasonNoCIDName_Object = MibScalar
arrisMtaDevDefaultReasonNoCIDName = _ArrisMtaDevDefaultReasonNoCIDName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 23),
    _ArrisMtaDevDefaultReasonNoCIDName_Type()
)
arrisMtaDevDefaultReasonNoCIDName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevDefaultReasonNoCIDName.setStatus("current")
_ArrisMtaDevSipConfigFileURL_Type = SnmpAdminString
_ArrisMtaDevSipConfigFileURL_Object = MibScalar
arrisMtaDevSipConfigFileURL = _ArrisMtaDevSipConfigFileURL_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 24),
    _ArrisMtaDevSipConfigFileURL_Type()
)
arrisMtaDevSipConfigFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevSipConfigFileURL.setStatus("current")


class _ArrisMtaDevSipDwnldConfig_Type(Integer32):
    """Custom type arrisMtaDevSipDwnldConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ArrisMtaDevSipDwnldConfig_Type.__name__ = "Integer32"
_ArrisMtaDevSipDwnldConfig_Object = MibScalar
arrisMtaDevSipDwnldConfig = _ArrisMtaDevSipDwnldConfig_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 25),
    _ArrisMtaDevSipDwnldConfig_Type()
)
arrisMtaDevSipDwnldConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevSipDwnldConfig.setStatus("current")


class _ArrisMtaDevSpecialConfigurationOverrideEnable_Type(Bits):
    """Custom type arrisMtaDevSpecialConfigurationOverrideEnable based on Bits"""
    defaultHexValue = "00000000"

    namedValues = NamedValues(
        *(("enableDhcpOption60SubOpt18Ovrd", 0),
          ("unused1", 1),
          ("unused2", 2),
          ("unused3", 3),
          ("unused4", 4),
          ("unused5", 5),
          ("unused6", 6),
          ("unused7", 7),
          ("unused8", 8),
          ("unused9", 9),
          ("unused10", 10),
          ("unused11", 11),
          ("unused12", 12),
          ("unused13", 13),
          ("unused14", 14),
          ("unused15", 15),
          ("unused16", 16),
          ("unused17", 17),
          ("unused18", 18),
          ("unused19", 19),
          ("unused20", 20),
          ("unused21", 21),
          ("unused22", 22),
          ("unused23", 23),
          ("unused24", 24),
          ("unused25", 25),
          ("unused26", 26),
          ("unused27", 27),
          ("unused28", 28),
          ("unused29", 29),
          ("unused30", 30),
          ("unused31", 31))
    )

_ArrisMtaDevSpecialConfigurationOverrideEnable_Type.__name__ = "Bits"
_ArrisMtaDevSpecialConfigurationOverrideEnable_Object = MibScalar
arrisMtaDevSpecialConfigurationOverrideEnable = _ArrisMtaDevSpecialConfigurationOverrideEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 26),
    _ArrisMtaDevSpecialConfigurationOverrideEnable_Type()
)
arrisMtaDevSpecialConfigurationOverrideEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevSpecialConfigurationOverrideEnable.setStatus("current")


class _ArrisMtaDevRtcpTosValue_Type(Integer32):
    """Custom type arrisMtaDevRtcpTosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ArrisMtaDevRtcpTosValue_Type.__name__ = "Integer32"
_ArrisMtaDevRtcpTosValue_Object = MibScalar
arrisMtaDevRtcpTosValue = _ArrisMtaDevRtcpTosValue_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 27),
    _ArrisMtaDevRtcpTosValue_Type()
)
arrisMtaDevRtcpTosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevRtcpTosValue.setStatus("current")


class _ArrisMtaDevAutomaticOsiDelay_Type(Integer32):
    """Custom type arrisMtaDevAutomaticOsiDelay based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ArrisMtaDevAutomaticOsiDelay_Type.__name__ = "Integer32"
_ArrisMtaDevAutomaticOsiDelay_Object = MibScalar
arrisMtaDevAutomaticOsiDelay = _ArrisMtaDevAutomaticOsiDelay_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 28),
    _ArrisMtaDevAutomaticOsiDelay_Type()
)
arrisMtaDevAutomaticOsiDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevAutomaticOsiDelay.setStatus("current")
if mibBuilder.loadTexts:
    arrisMtaDevAutomaticOsiDelay.setUnits("100 milliseconds")


class _ArrisMtaDevCustomJitterBufferEnabled_Type(Integer32):
    """Custom type arrisMtaDevCustomJitterBufferEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ArrisMtaDevCustomJitterBufferEnabled_Type.__name__ = "Integer32"
_ArrisMtaDevCustomJitterBufferEnabled_Object = MibScalar
arrisMtaDevCustomJitterBufferEnabled = _ArrisMtaDevCustomJitterBufferEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 29),
    _ArrisMtaDevCustomJitterBufferEnabled_Type()
)
arrisMtaDevCustomJitterBufferEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevCustomJitterBufferEnabled.setStatus("current")


class _ArrisMtaDevCustomMinJitterBuffer_Type(Integer32):
    """Custom type arrisMtaDevCustomMinJitterBuffer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 160),
    )


_ArrisMtaDevCustomMinJitterBuffer_Type.__name__ = "Integer32"
_ArrisMtaDevCustomMinJitterBuffer_Object = MibScalar
arrisMtaDevCustomMinJitterBuffer = _ArrisMtaDevCustomMinJitterBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 30),
    _ArrisMtaDevCustomMinJitterBuffer_Type()
)
arrisMtaDevCustomMinJitterBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevCustomMinJitterBuffer.setStatus("current")


class _ArrisMtaDevCustomNomJitterBuffer_Type(Integer32):
    """Custom type arrisMtaDevCustomNomJitterBuffer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 160),
    )


_ArrisMtaDevCustomNomJitterBuffer_Type.__name__ = "Integer32"
_ArrisMtaDevCustomNomJitterBuffer_Object = MibScalar
arrisMtaDevCustomNomJitterBuffer = _ArrisMtaDevCustomNomJitterBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 31),
    _ArrisMtaDevCustomNomJitterBuffer_Type()
)
arrisMtaDevCustomNomJitterBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevCustomNomJitterBuffer.setStatus("current")


class _ArrisMtaDevCustomMaxJitterBuffer_Type(Integer32):
    """Custom type arrisMtaDevCustomMaxJitterBuffer based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 160),
    )


_ArrisMtaDevCustomMaxJitterBuffer_Type.__name__ = "Integer32"
_ArrisMtaDevCustomMaxJitterBuffer_Object = MibScalar
arrisMtaDevCustomMaxJitterBuffer = _ArrisMtaDevCustomMaxJitterBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 32),
    _ArrisMtaDevCustomMaxJitterBuffer_Type()
)
arrisMtaDevCustomMaxJitterBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevCustomMaxJitterBuffer.setStatus("current")


class _ArrisMtaDevEnableDHCPLog_Type(Integer32):
    """Custom type arrisMtaDevEnableDHCPLog based on Integer32"""
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


_ArrisMtaDevEnableDHCPLog_Type.__name__ = "Integer32"
_ArrisMtaDevEnableDHCPLog_Object = MibScalar
arrisMtaDevEnableDHCPLog = _ArrisMtaDevEnableDHCPLog_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 33),
    _ArrisMtaDevEnableDHCPLog_Type()
)
arrisMtaDevEnableDHCPLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEnableDHCPLog.setStatus("current")


class _ArrisMtaDevEnableMGCPLog_Type(Integer32):
    """Custom type arrisMtaDevEnableMGCPLog based on Integer32"""
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


_ArrisMtaDevEnableMGCPLog_Type.__name__ = "Integer32"
_ArrisMtaDevEnableMGCPLog_Object = MibScalar
arrisMtaDevEnableMGCPLog = _ArrisMtaDevEnableMGCPLog_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 34),
    _ArrisMtaDevEnableMGCPLog_Type()
)
arrisMtaDevEnableMGCPLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEnableMGCPLog.setStatus("current")


class _ArrisMtaDevClearDHCPLog_Type(Integer32):
    """Custom type arrisMtaDevClearDHCPLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_ArrisMtaDevClearDHCPLog_Type.__name__ = "Integer32"
_ArrisMtaDevClearDHCPLog_Object = MibScalar
arrisMtaDevClearDHCPLog = _ArrisMtaDevClearDHCPLog_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 35),
    _ArrisMtaDevClearDHCPLog_Type()
)
arrisMtaDevClearDHCPLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevClearDHCPLog.setStatus("current")


class _ArrisMtaDevClearMGCPLog_Type(Integer32):
    """Custom type arrisMtaDevClearMGCPLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_ArrisMtaDevClearMGCPLog_Type.__name__ = "Integer32"
_ArrisMtaDevClearMGCPLog_Object = MibScalar
arrisMtaDevClearMGCPLog = _ArrisMtaDevClearMGCPLog_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 36),
    _ArrisMtaDevClearMGCPLog_Type()
)
arrisMtaDevClearMGCPLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevClearMGCPLog.setStatus("current")


class _ArrisMtaDevTDDReportToCMS_Type(Integer32):
    """Custom type arrisMtaDevTDDReportToCMS based on Integer32"""
    defaultValue = 1

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


_ArrisMtaDevTDDReportToCMS_Type.__name__ = "Integer32"
_ArrisMtaDevTDDReportToCMS_Object = MibScalar
arrisMtaDevTDDReportToCMS = _ArrisMtaDevTDDReportToCMS_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 37),
    _ArrisMtaDevTDDReportToCMS_Type()
)
arrisMtaDevTDDReportToCMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevTDDReportToCMS.setStatus("current")


class _ArrisMtaDevAutomaticCallResourceRecovery_Type(Integer32):
    """Custom type arrisMtaDevAutomaticCallResourceRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_ArrisMtaDevAutomaticCallResourceRecovery_Type.__name__ = "Integer32"
_ArrisMtaDevAutomaticCallResourceRecovery_Object = MibScalar
arrisMtaDevAutomaticCallResourceRecovery = _ArrisMtaDevAutomaticCallResourceRecovery_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 38),
    _ArrisMtaDevAutomaticCallResourceRecovery_Type()
)
arrisMtaDevAutomaticCallResourceRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevAutomaticCallResourceRecovery.setStatus("current")
if mibBuilder.loadTexts:
    arrisMtaDevAutomaticCallResourceRecovery.setUnits("seconds")


class _ArrisMtaDevPacketcableProvisioningFlow_Type(Integer32):
    """Custom type arrisMtaDevPacketcableProvisioningFlow based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("secure", 0),
          ("hybrid2", 1),
          ("hybrid1", 2),
          ("basic2", 3),
          ("basic1", 4),
          ("none", 5))
    )


_ArrisMtaDevPacketcableProvisioningFlow_Type.__name__ = "Integer32"
_ArrisMtaDevPacketcableProvisioningFlow_Object = MibScalar
arrisMtaDevPacketcableProvisioningFlow = _ArrisMtaDevPacketcableProvisioningFlow_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 39),
    _ArrisMtaDevPacketcableProvisioningFlow_Type()
)
arrisMtaDevPacketcableProvisioningFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevPacketcableProvisioningFlow.setStatus("current")
_ArrisMtaDevLevelControl_ObjectIdentity = ObjectIdentity
arrisMtaDevLevelControl = _ArrisMtaDevLevelControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 40)
)


class _ArrisMtaDevLevelControlOffHookEnable_Type(Integer32):
    """Custom type arrisMtaDevLevelControlOffHookEnable based on Integer32"""
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


_ArrisMtaDevLevelControlOffHookEnable_Type.__name__ = "Integer32"
_ArrisMtaDevLevelControlOffHookEnable_Object = MibScalar
arrisMtaDevLevelControlOffHookEnable = _ArrisMtaDevLevelControlOffHookEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 40, 1),
    _ArrisMtaDevLevelControlOffHookEnable_Type()
)
arrisMtaDevLevelControlOffHookEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevLevelControlOffHookEnable.setStatus("current")


class _ArrisMtaDevLevelControlOffHookFSK_Type(Integer32):
    """Custom type arrisMtaDevLevelControlOffHookFSK based on Integer32"""
    defaultValue = -15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32, -10),
    )


_ArrisMtaDevLevelControlOffHookFSK_Type.__name__ = "Integer32"
_ArrisMtaDevLevelControlOffHookFSK_Object = MibScalar
arrisMtaDevLevelControlOffHookFSK = _ArrisMtaDevLevelControlOffHookFSK_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 40, 2),
    _ArrisMtaDevLevelControlOffHookFSK_Type()
)
arrisMtaDevLevelControlOffHookFSK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevLevelControlOffHookFSK.setStatus("current")


class _ArrisMtaDevLevelControlOffHookCAS_Type(Integer32):
    """Custom type arrisMtaDevLevelControlOffHookCAS based on Integer32"""
    defaultValue = -15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32, -10),
    )


_ArrisMtaDevLevelControlOffHookCAS_Type.__name__ = "Integer32"
_ArrisMtaDevLevelControlOffHookCAS_Object = MibScalar
arrisMtaDevLevelControlOffHookCAS = _ArrisMtaDevLevelControlOffHookCAS_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 40, 3),
    _ArrisMtaDevLevelControlOffHookCAS_Type()
)
arrisMtaDevLevelControlOffHookCAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevLevelControlOffHookCAS.setStatus("current")


class _ArrisMtaDevOffHookFskDelay_Type(Integer32):
    """Custom type arrisMtaDevOffHookFskDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_ArrisMtaDevOffHookFskDelay_Type.__name__ = "Integer32"
_ArrisMtaDevOffHookFskDelay_Object = MibScalar
arrisMtaDevOffHookFskDelay = _ArrisMtaDevOffHookFskDelay_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 41),
    _ArrisMtaDevOffHookFskDelay_Type()
)
arrisMtaDevOffHookFskDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevOffHookFskDelay.setStatus("current")
if mibBuilder.loadTexts:
    arrisMtaDevOffHookFskDelay.setUnits("milliseconds")


class _ArrisMtaDevT38Timeout_Type(Integer32):
    """Custom type arrisMtaDevT38Timeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ArrisMtaDevT38Timeout_Type.__name__ = "Integer32"
_ArrisMtaDevT38Timeout_Object = MibScalar
arrisMtaDevT38Timeout = _ArrisMtaDevT38Timeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 42),
    _ArrisMtaDevT38Timeout_Type()
)
arrisMtaDevT38Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevT38Timeout.setStatus("current")
if mibBuilder.loadTexts:
    arrisMtaDevT38Timeout.setUnits("seconds")


class _ArrisMtaDevSuperG3FaxRelay_Type(Integer32):
    """Custom type arrisMtaDevSuperG3FaxRelay based on Integer32"""
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


_ArrisMtaDevSuperG3FaxRelay_Type.__name__ = "Integer32"
_ArrisMtaDevSuperG3FaxRelay_Object = MibScalar
arrisMtaDevSuperG3FaxRelay = _ArrisMtaDevSuperG3FaxRelay_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 43),
    _ArrisMtaDevSuperG3FaxRelay_Type()
)
arrisMtaDevSuperG3FaxRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevSuperG3FaxRelay.setStatus("current")


class _ArrisMtaDevDTMFEndEventForceAscending_Type(Integer32):
    """Custom type arrisMtaDevDTMFEndEventForceAscending based on Integer32"""
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


_ArrisMtaDevDTMFEndEventForceAscending_Type.__name__ = "Integer32"
_ArrisMtaDevDTMFEndEventForceAscending_Object = MibScalar
arrisMtaDevDTMFEndEventForceAscending = _ArrisMtaDevDTMFEndEventForceAscending_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 44),
    _ArrisMtaDevDTMFEndEventForceAscending_Type()
)
arrisMtaDevDTMFEndEventForceAscending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevDTMFEndEventForceAscending.setStatus("current")


class _ArrisMtaDevDspHandleBellModemTone_Type(Integer32):
    """Custom type arrisMtaDevDspHandleBellModemTone based on Integer32"""
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


_ArrisMtaDevDspHandleBellModemTone_Type.__name__ = "Integer32"
_ArrisMtaDevDspHandleBellModemTone_Object = MibScalar
arrisMtaDevDspHandleBellModemTone = _ArrisMtaDevDspHandleBellModemTone_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 45),
    _ArrisMtaDevDspHandleBellModemTone_Type()
)
arrisMtaDevDspHandleBellModemTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevDspHandleBellModemTone.setStatus("current")


class _ArrisMtaDevDhcpSubOpt3Immediate_Type(Integer32):
    """Custom type arrisMtaDevDhcpSubOpt3Immediate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ArrisMtaDevDhcpSubOpt3Immediate_Type.__name__ = "Integer32"
_ArrisMtaDevDhcpSubOpt3Immediate_Object = MibScalar
arrisMtaDevDhcpSubOpt3Immediate = _ArrisMtaDevDhcpSubOpt3Immediate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 46),
    _ArrisMtaDevDhcpSubOpt3Immediate_Type()
)
arrisMtaDevDhcpSubOpt3Immediate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevDhcpSubOpt3Immediate.setStatus("current")


class _ArrisMtaDevMaxCallPServiceFlows_Type(Integer32):
    """Custom type arrisMtaDevMaxCallPServiceFlows based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ArrisMtaDevMaxCallPServiceFlows_Type.__name__ = "Integer32"
_ArrisMtaDevMaxCallPServiceFlows_Object = MibScalar
arrisMtaDevMaxCallPServiceFlows = _ArrisMtaDevMaxCallPServiceFlows_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 47),
    _ArrisMtaDevMaxCallPServiceFlows_Type()
)
arrisMtaDevMaxCallPServiceFlows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevMaxCallPServiceFlows.setStatus("current")
_ArrisMtaDevCmIp_ObjectIdentity = ObjectIdentity
arrisMtaDevCmIp = _ArrisMtaDevCmIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 48)
)
_ArrisMtaDevCmIpTable_Object = MibTable
arrisMtaDevCmIpTable = _ArrisMtaDevCmIpTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 48, 1)
)
if mibBuilder.loadTexts:
    arrisMtaDevCmIpTable.setStatus("current")
_ArrisMtaDevCmIpEntry_Object = MibTableRow
arrisMtaDevCmIpEntry = _ArrisMtaDevCmIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 48, 1, 1)
)
arrisMtaDevCmIpEntry.setIndexNames(
    (0, "ARRIS-MTA-DEVICE-MIB", "arrisMtaDevCmIpIndex"),
)
if mibBuilder.loadTexts:
    arrisMtaDevCmIpEntry.setStatus("current")


class _ArrisMtaDevCmIpIndex_Type(Integer32):
    """Custom type arrisMtaDevCmIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_ArrisMtaDevCmIpIndex_Type.__name__ = "Integer32"
_ArrisMtaDevCmIpIndex_Object = MibTableColumn
arrisMtaDevCmIpIndex = _ArrisMtaDevCmIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 48, 1, 1, 1),
    _ArrisMtaDevCmIpIndex_Type()
)
arrisMtaDevCmIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisMtaDevCmIpIndex.setStatus("current")
_ArrisMtaDevCmIpAddressType_Type = InetAddressType
_ArrisMtaDevCmIpAddressType_Object = MibTableColumn
arrisMtaDevCmIpAddressType = _ArrisMtaDevCmIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 48, 1, 1, 2),
    _ArrisMtaDevCmIpAddressType_Type()
)
arrisMtaDevCmIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevCmIpAddressType.setStatus("current")
_ArrisMtaDevCmIpAddress_Type = InetAddress
_ArrisMtaDevCmIpAddress_Object = MibTableColumn
arrisMtaDevCmIpAddress = _ArrisMtaDevCmIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 48, 1, 1, 3),
    _ArrisMtaDevCmIpAddress_Type()
)
arrisMtaDevCmIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevCmIpAddress.setStatus("current")


class _ArrisMtaDevCmIpPhysAddress_Type(PhysAddress):
    """Custom type arrisMtaDevCmIpPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_ArrisMtaDevCmIpPhysAddress_Type.__name__ = "PhysAddress"
_ArrisMtaDevCmIpPhysAddress_Object = MibTableColumn
arrisMtaDevCmIpPhysAddress = _ArrisMtaDevCmIpPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 48, 1, 1, 4),
    _ArrisMtaDevCmIpPhysAddress_Type()
)
arrisMtaDevCmIpPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevCmIpPhysAddress.setStatus("current")


class _ArrisMtaDevHDAudioDefaultPayloadType_Type(Integer32):
    """Custom type arrisMtaDevHDAudioDefaultPayloadType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic", 1))
    )


_ArrisMtaDevHDAudioDefaultPayloadType_Type.__name__ = "Integer32"
_ArrisMtaDevHDAudioDefaultPayloadType_Object = MibScalar
arrisMtaDevHDAudioDefaultPayloadType = _ArrisMtaDevHDAudioDefaultPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 49),
    _ArrisMtaDevHDAudioDefaultPayloadType_Type()
)
arrisMtaDevHDAudioDefaultPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevHDAudioDefaultPayloadType.setStatus("current")


class _ArrisMtaDevWBSLIC_Type(Integer32):
    """Custom type arrisMtaDevWBSLIC based on Integer32"""
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


_ArrisMtaDevWBSLIC_Type.__name__ = "Integer32"
_ArrisMtaDevWBSLIC_Object = MibScalar
arrisMtaDevWBSLIC = _ArrisMtaDevWBSLIC_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 50),
    _ArrisMtaDevWBSLIC_Type()
)
arrisMtaDevWBSLIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevWBSLIC.setStatus("current")
_ArrisMtaDevProvisionedCodecArray_Type = DisplayString
_ArrisMtaDevProvisionedCodecArray_Object = MibScalar
arrisMtaDevProvisionedCodecArray = _ArrisMtaDevProvisionedCodecArray_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 51),
    _ArrisMtaDevProvisionedCodecArray_Type()
)
arrisMtaDevProvisionedCodecArray.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevProvisionedCodecArray.setStatus("current")


class _ArrisMtaDevHDAudioG722SampleRate_Type(Integer32):
    """Custom type arrisMtaDevHDAudioG722SampleRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate8000", 0),
          ("rate16000", 1),
          ("rateDynamic", 2))
    )


_ArrisMtaDevHDAudioG722SampleRate_Type.__name__ = "Integer32"
_ArrisMtaDevHDAudioG722SampleRate_Object = MibScalar
arrisMtaDevHDAudioG722SampleRate = _ArrisMtaDevHDAudioG722SampleRate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 52),
    _ArrisMtaDevHDAudioG722SampleRate_Type()
)
arrisMtaDevHDAudioG722SampleRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevHDAudioG722SampleRate.setStatus("current")


class _ArrisMtaDevHDAudioEnable_Type(Integer32):
    """Custom type arrisMtaDevHDAudioEnable based on Integer32"""
    defaultValue = 1

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


_ArrisMtaDevHDAudioEnable_Type.__name__ = "Integer32"
_ArrisMtaDevHDAudioEnable_Object = MibScalar
arrisMtaDevHDAudioEnable = _ArrisMtaDevHDAudioEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 53),
    _ArrisMtaDevHDAudioEnable_Type()
)
arrisMtaDevHDAudioEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevHDAudioEnable.setStatus("current")


class _ArrisMtaDevRtcpJitterDisabled_Type(Integer32):
    """Custom type arrisMtaDevRtcpJitterDisabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ArrisMtaDevRtcpJitterDisabled_Type.__name__ = "Integer32"
_ArrisMtaDevRtcpJitterDisabled_Object = MibScalar
arrisMtaDevRtcpJitterDisabled = _ArrisMtaDevRtcpJitterDisabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 3, 54),
    _ArrisMtaDevRtcpJitterDisabled_Type()
)
arrisMtaDevRtcpJitterDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevRtcpJitterDisabled.setStatus("current")
_ArrisMtaDevEndPntSetup_ObjectIdentity = ObjectIdentity
arrisMtaDevEndPntSetup = _ArrisMtaDevEndPntSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 4)
)
_ArrisMtaDevEndPntTable_Object = MibTable
arrisMtaDevEndPntTable = _ArrisMtaDevEndPntTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 4, 3)
)
if mibBuilder.loadTexts:
    arrisMtaDevEndPntTable.setStatus("current")
_ArrisMtaDevEndPntEntry_Object = MibTableRow
arrisMtaDevEndPntEntry = _ArrisMtaDevEndPntEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 4, 3, 1)
)
arrisMtaDevEndPntEntry.setIndexNames(
    (0, "ARRIS-MTA-DEVICE-MIB", "arrisMtaDevEndPntIndex"),
)
if mibBuilder.loadTexts:
    arrisMtaDevEndPntEntry.setStatus("current")
_ArrisMtaDevEndPntIndex_Type = Integer32
_ArrisMtaDevEndPntIndex_Object = MibTableColumn
arrisMtaDevEndPntIndex = _ArrisMtaDevEndPntIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 4, 3, 1, 1),
    _ArrisMtaDevEndPntIndex_Type()
)
arrisMtaDevEndPntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisMtaDevEndPntIndex.setStatus("current")


class _ArrisMtaDevEndPntDialingMethod_Type(Integer32):
    """Custom type arrisMtaDevEndPntDialingMethod based on Integer32"""
    defaultValue = 1

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
        *(("tone", 1),
          ("pulse", 2),
          ("toneAndPulse", 3),
          ("pulseWithDTMFRelay", 4),
          ("toneAndPulseWithDTMFRelay", 5))
    )


_ArrisMtaDevEndPntDialingMethod_Type.__name__ = "Integer32"
_ArrisMtaDevEndPntDialingMethod_Object = MibTableColumn
arrisMtaDevEndPntDialingMethod = _ArrisMtaDevEndPntDialingMethod_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 4, 3, 1, 24),
    _ArrisMtaDevEndPntDialingMethod_Type()
)
arrisMtaDevEndPntDialingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEndPntDialingMethod.setStatus("current")


class _ArrisMtaDevEndPntRingingWaveform_Type(Integer32):
    """Custom type arrisMtaDevEndPntRingingWaveform based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("sinusoidal", 2))
    )


_ArrisMtaDevEndPntRingingWaveform_Type.__name__ = "Integer32"
_ArrisMtaDevEndPntRingingWaveform_Object = MibTableColumn
arrisMtaDevEndPntRingingWaveform = _ArrisMtaDevEndPntRingingWaveform_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 4, 3, 1, 25),
    _ArrisMtaDevEndPntRingingWaveform_Type()
)
arrisMtaDevEndPntRingingWaveform.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEndPntRingingWaveform.setStatus("current")


class _ArrisMtaDevEndPntFaxOnlyLineTimeout_Type(Integer32):
    """Custom type arrisMtaDevEndPntFaxOnlyLineTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_ArrisMtaDevEndPntFaxOnlyLineTimeout_Type.__name__ = "Integer32"
_ArrisMtaDevEndPntFaxOnlyLineTimeout_Object = MibTableColumn
arrisMtaDevEndPntFaxOnlyLineTimeout = _ArrisMtaDevEndPntFaxOnlyLineTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 4, 3, 1, 26),
    _ArrisMtaDevEndPntFaxOnlyLineTimeout_Type()
)
arrisMtaDevEndPntFaxOnlyLineTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEndPntFaxOnlyLineTimeout.setStatus("current")


class _ArrisMtaDevPersistentLineStatus_Type(Integer32):
    """Custom type arrisMtaDevPersistentLineStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 0),
          ("forceDisable", 1))
    )


_ArrisMtaDevPersistentLineStatus_Type.__name__ = "Integer32"
_ArrisMtaDevPersistentLineStatus_Object = MibTableColumn
arrisMtaDevPersistentLineStatus = _ArrisMtaDevPersistentLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 4, 3, 1, 27),
    _ArrisMtaDevPersistentLineStatus_Type()
)
arrisMtaDevPersistentLineStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevPersistentLineStatus.setStatus("current")


class _ArrisMtaDevEndPntCallWaitingRepeatSteady_Type(Integer32):
    """Custom type arrisMtaDevEndPntCallWaitingRepeatSteady based on Integer32"""
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


_ArrisMtaDevEndPntCallWaitingRepeatSteady_Type.__name__ = "Integer32"
_ArrisMtaDevEndPntCallWaitingRepeatSteady_Object = MibTableColumn
arrisMtaDevEndPntCallWaitingRepeatSteady = _ArrisMtaDevEndPntCallWaitingRepeatSteady_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 4, 3, 1, 28),
    _ArrisMtaDevEndPntCallWaitingRepeatSteady_Type()
)
arrisMtaDevEndPntCallWaitingRepeatSteady.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEndPntCallWaitingRepeatSteady.setStatus("current")


class _ArrisMtaDevEndPntCIDEnable_Type(Integer32):
    """Custom type arrisMtaDevEndPntCIDEnable based on Integer32"""
    defaultValue = 1

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


_ArrisMtaDevEndPntCIDEnable_Type.__name__ = "Integer32"
_ArrisMtaDevEndPntCIDEnable_Object = MibTableColumn
arrisMtaDevEndPntCIDEnable = _ArrisMtaDevEndPntCIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 4, 3, 1, 29),
    _ArrisMtaDevEndPntCIDEnable_Type()
)
arrisMtaDevEndPntCIDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEndPntCIDEnable.setStatus("current")


class _ArrisMtaDevEndPntCIDNameEnable_Type(Integer32):
    """Custom type arrisMtaDevEndPntCIDNameEnable based on Integer32"""
    defaultValue = 1

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


_ArrisMtaDevEndPntCIDNameEnable_Type.__name__ = "Integer32"
_ArrisMtaDevEndPntCIDNameEnable_Object = MibTableColumn
arrisMtaDevEndPntCIDNameEnable = _ArrisMtaDevEndPntCIDNameEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 4, 3, 1, 30),
    _ArrisMtaDevEndPntCIDNameEnable_Type()
)
arrisMtaDevEndPntCIDNameEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEndPntCIDNameEnable.setStatus("current")


class _ArrisMtaDevEndPntCIDDateTimeEnable_Type(Integer32):
    """Custom type arrisMtaDevEndPntCIDDateTimeEnable based on Integer32"""
    defaultValue = 1

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


_ArrisMtaDevEndPntCIDDateTimeEnable_Type.__name__ = "Integer32"
_ArrisMtaDevEndPntCIDDateTimeEnable_Object = MibTableColumn
arrisMtaDevEndPntCIDDateTimeEnable = _ArrisMtaDevEndPntCIDDateTimeEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 4, 3, 1, 31),
    _ArrisMtaDevEndPntCIDDateTimeEnable_Type()
)
arrisMtaDevEndPntCIDDateTimeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEndPntCIDDateTimeEnable.setStatus("current")


class _ArrisMtaDevEndPntLoopReversal_Type(Integer32):
    """Custom type arrisMtaDevEndPntLoopReversal based on Integer32"""
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


_ArrisMtaDevEndPntLoopReversal_Type.__name__ = "Integer32"
_ArrisMtaDevEndPntLoopReversal_Object = MibTableColumn
arrisMtaDevEndPntLoopReversal = _ArrisMtaDevEndPntLoopReversal_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 4, 3, 1, 32),
    _ArrisMtaDevEndPntLoopReversal_Type()
)
arrisMtaDevEndPntLoopReversal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEndPntLoopReversal.setStatus("current")


class _ArrisMtaDevEndPntGainControlTxVoice_Type(Integer32):
    """Custom type arrisMtaDevEndPntGainControlTxVoice based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-128,
              -16,
              -15,
              -14,
              -13,
              -12,
              -11,
              -10,
              -9,
              -8,
              -7,
              -6,
              -5,
              -4,
              -3,
              -2,
              -1,
              0,
              1,
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
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("disabled", -128),
          ("dBm-16", -16),
          ("dBm-15", -15),
          ("dBm-14", -14),
          ("dBm-13", -13),
          ("dBm-12", -12),
          ("dBm-11", -11),
          ("dBm-10", -10),
          ("dBm-9", -9),
          ("dBm-8", -8),
          ("dBm-7", -7),
          ("dBm-6", -6),
          ("dBm-5", -5),
          ("dBm-4", -4),
          ("dBm-3", -3),
          ("dBm-2", -2),
          ("dBm-1", -1),
          ("dBm0", 0),
          ("dBm1", 1),
          ("dBm2", 2),
          ("dBm3", 3),
          ("dBm4", 4),
          ("dBm5", 5),
          ("dBm6", 6),
          ("dBm7", 7),
          ("dBm8", 8),
          ("dBm9", 9),
          ("dBm10", 10),
          ("dBm11", 11),
          ("dBm12", 12),
          ("dBm13", 13),
          ("dBm14", 14),
          ("dBm15", 15),
          ("dBm16", 16))
    )


_ArrisMtaDevEndPntGainControlTxVoice_Type.__name__ = "Integer32"
_ArrisMtaDevEndPntGainControlTxVoice_Object = MibTableColumn
arrisMtaDevEndPntGainControlTxVoice = _ArrisMtaDevEndPntGainControlTxVoice_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 4, 3, 1, 33),
    _ArrisMtaDevEndPntGainControlTxVoice_Type()
)
arrisMtaDevEndPntGainControlTxVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEndPntGainControlTxVoice.setStatus("current")


class _ArrisMtaDevEndPntGainControlRxVoice_Type(Integer32):
    """Custom type arrisMtaDevEndPntGainControlRxVoice based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-128,
              -16,
              -15,
              -14,
              -13,
              -12,
              -11,
              -10,
              -9,
              -8,
              -7,
              -6,
              -5,
              -4,
              -3,
              -2,
              -1,
              0,
              1,
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
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("disabled", -128),
          ("dBm-16", -16),
          ("dBm-15", -15),
          ("dBm-14", -14),
          ("dBm-13", -13),
          ("dBm-12", -12),
          ("dBm-11", -11),
          ("dBm-10", -10),
          ("dBm-9", -9),
          ("dBm-8", -8),
          ("dBm-7", -7),
          ("dBm-6", -6),
          ("dBm-5", -5),
          ("dBm-4", -4),
          ("dBm-3", -3),
          ("dBm-2", -2),
          ("dBm-1", -1),
          ("dBm0", 0),
          ("dBm1", 1),
          ("dBm2", 2),
          ("dBm3", 3),
          ("dBm4", 4),
          ("dBm5", 5),
          ("dBm6", 6),
          ("dBm7", 7),
          ("dBm8", 8),
          ("dBm9", 9),
          ("dBm10", 10),
          ("dBm11", 11),
          ("dBm12", 12),
          ("dBm13", 13),
          ("dBm14", 14),
          ("dBm15", 15),
          ("dBm16", 16))
    )


_ArrisMtaDevEndPntGainControlRxVoice_Type.__name__ = "Integer32"
_ArrisMtaDevEndPntGainControlRxVoice_Object = MibTableColumn
arrisMtaDevEndPntGainControlRxVoice = _ArrisMtaDevEndPntGainControlRxVoice_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 4, 3, 1, 34),
    _ArrisMtaDevEndPntGainControlRxVoice_Type()
)
arrisMtaDevEndPntGainControlRxVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEndPntGainControlRxVoice.setStatus("current")


class _ArrisMtaDevEndPntHDAudioEnable_Type(Integer32):
    """Custom type arrisMtaDevEndPntHDAudioEnable based on Integer32"""
    defaultValue = 1

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


_ArrisMtaDevEndPntHDAudioEnable_Type.__name__ = "Integer32"
_ArrisMtaDevEndPntHDAudioEnable_Object = MibTableColumn
arrisMtaDevEndPntHDAudioEnable = _ArrisMtaDevEndPntHDAudioEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 4, 3, 1, 35),
    _ArrisMtaDevEndPntHDAudioEnable_Type()
)
arrisMtaDevEndPntHDAudioEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevEndPntHDAudioEnable.setStatus("current")


class _ArrisMtaDevEndPntHDAudioStatus_Type(Integer32):
    """Custom type arrisMtaDevEndPntHDAudioStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("notprovisioned", 2))
    )


_ArrisMtaDevEndPntHDAudioStatus_Type.__name__ = "Integer32"
_ArrisMtaDevEndPntHDAudioStatus_Object = MibTableColumn
arrisMtaDevEndPntHDAudioStatus = _ArrisMtaDevEndPntHDAudioStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 4, 3, 1, 36),
    _ArrisMtaDevEndPntHDAudioStatus_Type()
)
arrisMtaDevEndPntHDAudioStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevEndPntHDAudioStatus.setStatus("current")


class _ArrisMtaDevEndPntCallPState_Type(Integer32):
    """Custom type arrisMtaDevEndPntCallPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("out-of-service", 1),
          ("redialing", 2),
          ("idle", 3),
          ("predial", 4),
          ("dialing", 5),
          ("calling", 6),
          ("ringing", 7),
          ("connected", 8),
          ("waithook", 9),
          ("connected-alerting", 10),
          ("call-waiting", 11),
          ("three-way-calling", 12),
          ("conference", 13),
          ("predial-holding", 14),
          ("dialing-holding", 15),
          ("calling-holding", 16),
          ("waithook-holding", 17),
          ("waithook-alerting", 18),
          ("flash-digit", 19),
          ("stranded-call", 20),
          ("conf-before-answer", 21),
          ("autocall-ringing", 22),
          ("emergency-inject", 23),
          ("wait-reg", 24),
          ("restart", 25),
          ("disconnected", 26),
          ("inservice", 27))
    )


_ArrisMtaDevEndPntCallPState_Type.__name__ = "Integer32"
_ArrisMtaDevEndPntCallPState_Object = MibTableColumn
arrisMtaDevEndPntCallPState = _ArrisMtaDevEndPntCallPState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 2, 4, 3, 1, 37),
    _ArrisMtaDevEndPntCallPState_Type()
)
arrisMtaDevEndPntCallPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevEndPntCallPState.setStatus("current")
_ArrisMtaDevPowerSupplyTelemetry_ObjectIdentity = ObjectIdentity
arrisMtaDevPowerSupplyTelemetry = _ArrisMtaDevPowerSupplyTelemetry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3)
)
_ArrisMtaDevPwrSupplyBase_ObjectIdentity = ObjectIdentity
arrisMtaDevPwrSupplyBase = _ArrisMtaDevPwrSupplyBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 2)
)
_ArrisMtaDevBatteryChargerFWRev_Type = SnmpAdminString
_ArrisMtaDevBatteryChargerFWRev_Object = MibScalar
arrisMtaDevBatteryChargerFWRev = _ArrisMtaDevBatteryChargerFWRev_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 2, 1),
    _ArrisMtaDevBatteryChargerFWRev_Type()
)
arrisMtaDevBatteryChargerFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevBatteryChargerFWRev.setStatus("current")
_ArrisMtaDevPwrSupplyControl_ObjectIdentity = ObjectIdentity
arrisMtaDevPwrSupplyControl = _ArrisMtaDevPwrSupplyControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3)
)


class _ArrisMtaDevPwrSupplyEnableDataShutdown_Type(Integer32):
    """Custom type arrisMtaDevPwrSupplyEnableDataShutdown based on Integer32"""
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


_ArrisMtaDevPwrSupplyEnableDataShutdown_Type.__name__ = "Integer32"
_ArrisMtaDevPwrSupplyEnableDataShutdown_Object = MibScalar
arrisMtaDevPwrSupplyEnableDataShutdown = _ArrisMtaDevPwrSupplyEnableDataShutdown_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3, 1),
    _ArrisMtaDevPwrSupplyEnableDataShutdown_Type()
)
arrisMtaDevPwrSupplyEnableDataShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyEnableDataShutdown.setStatus("current")


class _ArrisMtaDevPwrSupplyEnableWifiShutdown_Type(Integer32):
    """Custom type arrisMtaDevPwrSupplyEnableWifiShutdown based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ArrisMtaDevPwrSupplyEnableWifiShutdown_Type.__name__ = "Integer32"
_ArrisMtaDevPwrSupplyEnableWifiShutdown_Object = MibScalar
arrisMtaDevPwrSupplyEnableWifiShutdown = _ArrisMtaDevPwrSupplyEnableWifiShutdown_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3, 2),
    _ArrisMtaDevPwrSupplyEnableWifiShutdown_Type()
)
arrisMtaDevPwrSupplyEnableWifiShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyEnableWifiShutdown.setStatus("current")
_ArrisMtaDevPwrSupplyLowBatteryThresh_Type = Integer32
_ArrisMtaDevPwrSupplyLowBatteryThresh_Object = MibScalar
arrisMtaDevPwrSupplyLowBatteryThresh = _ArrisMtaDevPwrSupplyLowBatteryThresh_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3, 3),
    _ArrisMtaDevPwrSupplyLowBatteryThresh_Type()
)
arrisMtaDevPwrSupplyLowBatteryThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyLowBatteryThresh.setStatus("current")
_ArrisMtaDevPwrSupplyTypicalIdlePwr_Type = Integer32
_ArrisMtaDevPwrSupplyTypicalIdlePwr_Object = MibScalar
arrisMtaDevPwrSupplyTypicalIdlePwr = _ArrisMtaDevPwrSupplyTypicalIdlePwr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3, 4),
    _ArrisMtaDevPwrSupplyTypicalIdlePwr_Type()
)
arrisMtaDevPwrSupplyTypicalIdlePwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyTypicalIdlePwr.setStatus("current")
_ArrisMtaDevPwrSupplyReplaceBatThresh_Type = Integer32
_ArrisMtaDevPwrSupplyReplaceBatThresh_Object = MibScalar
arrisMtaDevPwrSupplyReplaceBatThresh = _ArrisMtaDevPwrSupplyReplaceBatThresh_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3, 5),
    _ArrisMtaDevPwrSupplyReplaceBatThresh_Type()
)
arrisMtaDevPwrSupplyReplaceBatThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyReplaceBatThresh.setStatus("current")
_ArrisMtaDevPwrSupplyChargeState_Type = Integer32
_ArrisMtaDevPwrSupplyChargeState_Object = MibScalar
arrisMtaDevPwrSupplyChargeState = _ArrisMtaDevPwrSupplyChargeState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3, 6),
    _ArrisMtaDevPwrSupplyChargeState_Type()
)
arrisMtaDevPwrSupplyChargeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyChargeState.setStatus("current")


class _ArrisMtaDevPwrSupplyBatteryTest_Type(Integer32):
    """Custom type arrisMtaDevPwrSupplyBatteryTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("testScheduled", 0),
          ("disableAutoTesting", 1),
          ("testInProgress", 2),
          ("testPending", 3))
    )


_ArrisMtaDevPwrSupplyBatteryTest_Type.__name__ = "Integer32"
_ArrisMtaDevPwrSupplyBatteryTest_Object = MibScalar
arrisMtaDevPwrSupplyBatteryTest = _ArrisMtaDevPwrSupplyBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3, 8),
    _ArrisMtaDevPwrSupplyBatteryTest_Type()
)
arrisMtaDevPwrSupplyBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyBatteryTest.setStatus("current")
_ArrisMtaDevPwrSupplyConfigRunTime_Type = Integer32
_ArrisMtaDevPwrSupplyConfigRunTime_Object = MibScalar
arrisMtaDevPwrSupplyConfigRunTime = _ArrisMtaDevPwrSupplyConfigRunTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3, 9),
    _ArrisMtaDevPwrSupplyConfigRunTime_Type()
)
arrisMtaDevPwrSupplyConfigRunTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyConfigRunTime.setStatus("current")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyConfigRunTime.setUnits("minutes")
_ArrisMtaDevPwrSupplyConfigReplaceBatTime_Type = Integer32
_ArrisMtaDevPwrSupplyConfigReplaceBatTime_Object = MibScalar
arrisMtaDevPwrSupplyConfigReplaceBatTime = _ArrisMtaDevPwrSupplyConfigReplaceBatTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3, 10),
    _ArrisMtaDevPwrSupplyConfigReplaceBatTime_Type()
)
arrisMtaDevPwrSupplyConfigReplaceBatTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyConfigReplaceBatTime.setStatus("current")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyConfigReplaceBatTime.setUnits("minutes")
_ArrisMtaDevPwrSupplyConfigReplaceBatTime2_Type = Integer32
_ArrisMtaDevPwrSupplyConfigReplaceBatTime2_Object = MibScalar
arrisMtaDevPwrSupplyConfigReplaceBatTime2 = _ArrisMtaDevPwrSupplyConfigReplaceBatTime2_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3, 11),
    _ArrisMtaDevPwrSupplyConfigReplaceBatTime2_Type()
)
arrisMtaDevPwrSupplyConfigReplaceBatTime2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyConfigReplaceBatTime2.setStatus("current")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyConfigReplaceBatTime2.setUnits("minutes")


class _ArrisMtaDevPwrSupplyOverTempAlarmControl_Type(Integer32):
    """Custom type arrisMtaDevPwrSupplyOverTempAlarmControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("pendingenable", 2),
          ("pendingdisable", 3))
    )


_ArrisMtaDevPwrSupplyOverTempAlarmControl_Type.__name__ = "Integer32"
_ArrisMtaDevPwrSupplyOverTempAlarmControl_Object = MibScalar
arrisMtaDevPwrSupplyOverTempAlarmControl = _ArrisMtaDevPwrSupplyOverTempAlarmControl_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3, 12),
    _ArrisMtaDevPwrSupplyOverTempAlarmControl_Type()
)
arrisMtaDevPwrSupplyOverTempAlarmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyOverTempAlarmControl.setStatus("current")
_ArrisMtaDevPwrSupplyOverTempAlarmThreshold_Type = Integer32
_ArrisMtaDevPwrSupplyOverTempAlarmThreshold_Object = MibScalar
arrisMtaDevPwrSupplyOverTempAlarmThreshold = _ArrisMtaDevPwrSupplyOverTempAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3, 13),
    _ArrisMtaDevPwrSupplyOverTempAlarmThreshold_Type()
)
arrisMtaDevPwrSupplyOverTempAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyOverTempAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyOverTempAlarmThreshold.setUnits("degrees-C")
_ArrisMtaDevPwrSupplyTemperature_Type = SnmpAdminString
_ArrisMtaDevPwrSupplyTemperature_Object = MibScalar
arrisMtaDevPwrSupplyTemperature = _ArrisMtaDevPwrSupplyTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3, 14),
    _ArrisMtaDevPwrSupplyTemperature_Type()
)
arrisMtaDevPwrSupplyTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyTemperature.setStatus("current")


class _ArrisMtaDevPwrSupplyHiTempBatteryShutdownControl_Type(Integer32):
    """Custom type arrisMtaDevPwrSupplyHiTempBatteryShutdownControl based on Integer32"""
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


_ArrisMtaDevPwrSupplyHiTempBatteryShutdownControl_Type.__name__ = "Integer32"
_ArrisMtaDevPwrSupplyHiTempBatteryShutdownControl_Object = MibScalar
arrisMtaDevPwrSupplyHiTempBatteryShutdownControl = _ArrisMtaDevPwrSupplyHiTempBatteryShutdownControl_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3, 15),
    _ArrisMtaDevPwrSupplyHiTempBatteryShutdownControl_Type()
)
arrisMtaDevPwrSupplyHiTempBatteryShutdownControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyHiTempBatteryShutdownControl.setStatus("current")
_ArrisMtaDevPwrSupplyHighestTemperature_Type = SnmpAdminString
_ArrisMtaDevPwrSupplyHighestTemperature_Object = MibScalar
arrisMtaDevPwrSupplyHighestTemperature = _ArrisMtaDevPwrSupplyHighestTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3, 16),
    _ArrisMtaDevPwrSupplyHighestTemperature_Type()
)
arrisMtaDevPwrSupplyHighestTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyHighestTemperature.setStatus("current")
_ArrisMtaDevPwrSupplyHighestTemperatureTime_Type = SnmpAdminString
_ArrisMtaDevPwrSupplyHighestTemperatureTime_Object = MibScalar
arrisMtaDevPwrSupplyHighestTemperatureTime = _ArrisMtaDevPwrSupplyHighestTemperatureTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3, 17),
    _ArrisMtaDevPwrSupplyHighestTemperatureTime_Type()
)
arrisMtaDevPwrSupplyHighestTemperatureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyHighestTemperatureTime.setStatus("current")


class _ArrisMtaDevPwrSupplyHighestTemperatureClear_Type(Integer32):
    """Custom type arrisMtaDevPwrSupplyHighestTemperatureClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_ArrisMtaDevPwrSupplyHighestTemperatureClear_Type.__name__ = "Integer32"
_ArrisMtaDevPwrSupplyHighestTemperatureClear_Object = MibScalar
arrisMtaDevPwrSupplyHighestTemperatureClear = _ArrisMtaDevPwrSupplyHighestTemperatureClear_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3, 18),
    _ArrisMtaDevPwrSupplyHighestTemperatureClear_Type()
)
arrisMtaDevPwrSupplyHighestTemperatureClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyHighestTemperatureClear.setStatus("current")
_ArrisMtaDevPwrSupplyControlChargerReset_Type = TruthValue
_ArrisMtaDevPwrSupplyControlChargerReset_Object = MibScalar
arrisMtaDevPwrSupplyControlChargerReset = _ArrisMtaDevPwrSupplyControlChargerReset_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 3, 19),
    _ArrisMtaDevPwrSupplyControlChargerReset_Type()
)
arrisMtaDevPwrSupplyControlChargerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyControlChargerReset.setStatus("current")
_ArrisMtaDevPwrSupplyTimers_ObjectIdentity = ObjectIdentity
arrisMtaDevPwrSupplyTimers = _ArrisMtaDevPwrSupplyTimers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 4)
)
_ArrisMtaDevPwrSupplyDataShutdownTime_Type = Integer32
_ArrisMtaDevPwrSupplyDataShutdownTime_Object = MibScalar
arrisMtaDevPwrSupplyDataShutdownTime = _ArrisMtaDevPwrSupplyDataShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 4, 1),
    _ArrisMtaDevPwrSupplyDataShutdownTime_Type()
)
arrisMtaDevPwrSupplyDataShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyDataShutdownTime.setStatus("current")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyDataShutdownTime.setUnits("seconds")
_ArrisMtaDevPwrSupplyFullChargeTime_Type = Integer32
_ArrisMtaDevPwrSupplyFullChargeTime_Object = MibScalar
arrisMtaDevPwrSupplyFullChargeTime = _ArrisMtaDevPwrSupplyFullChargeTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 4, 2),
    _ArrisMtaDevPwrSupplyFullChargeTime_Type()
)
arrisMtaDevPwrSupplyFullChargeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyFullChargeTime.setStatus("current")
_ArrisMtaDevPwrSupplyStats_ObjectIdentity = ObjectIdentity
arrisMtaDevPwrSupplyStats = _ArrisMtaDevPwrSupplyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5)
)
_ArrisMtaDevBatteryStatusTable_Object = MibTable
arrisMtaDevBatteryStatusTable = _ArrisMtaDevBatteryStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 3)
)
if mibBuilder.loadTexts:
    arrisMtaDevBatteryStatusTable.setStatus("current")
_ArrisMtaDevBatteryStatusEntry_Object = MibTableRow
arrisMtaDevBatteryStatusEntry = _ArrisMtaDevBatteryStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 3, 1)
)
arrisMtaDevBatteryStatusEntry.setIndexNames(
    (0, "ARRIS-MTA-DEVICE-MIB", "arrisMtaDevBatteryStatusIndex"),
)
if mibBuilder.loadTexts:
    arrisMtaDevBatteryStatusEntry.setStatus("current")
_ArrisMtaDevBatteryStatusIndex_Type = Integer32
_ArrisMtaDevBatteryStatusIndex_Object = MibTableColumn
arrisMtaDevBatteryStatusIndex = _ArrisMtaDevBatteryStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 3, 1, 1),
    _ArrisMtaDevBatteryStatusIndex_Type()
)
arrisMtaDevBatteryStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisMtaDevBatteryStatusIndex.setStatus("current")


class _ArrisMtaDevBatteryOperState_Type(Integer32):
    """Custom type arrisMtaDevBatteryOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 0),
          ("invalid", 1),
          ("shutdownWarning", 2),
          ("batteryReversedShorted", 3),
          ("batteryLow-replaceBattery-acFail", 4),
          ("batteryLow-replaceBattery", 5),
          ("batteryLow-acFail", 6),
          ("batteryLow", 7),
          ("batteryMissing", 8),
          ("acFail-replaceBattery", 9),
          ("replaceBattery", 10),
          ("acFail", 11),
          ("normal", 12),
          ("testInProgress", 13),
          ("chargerFailure", 14))
    )


_ArrisMtaDevBatteryOperState_Type.__name__ = "Integer32"
_ArrisMtaDevBatteryOperState_Object = MibTableColumn
arrisMtaDevBatteryOperState = _ArrisMtaDevBatteryOperState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 3, 1, 2),
    _ArrisMtaDevBatteryOperState_Type()
)
arrisMtaDevBatteryOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevBatteryOperState.setStatus("current")
_ArrisMtaDevBatteryLastStateChange_Type = TimeStamp
_ArrisMtaDevBatteryLastStateChange_Object = MibTableColumn
arrisMtaDevBatteryLastStateChange = _ArrisMtaDevBatteryLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 3, 1, 3),
    _ArrisMtaDevBatteryLastStateChange_Type()
)
arrisMtaDevBatteryLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevBatteryLastStateChange.setStatus("current")
_ArrisMtaDevBatteryOperSubState_Type = SnmpAdminString
_ArrisMtaDevBatteryOperSubState_Object = MibTableColumn
arrisMtaDevBatteryOperSubState = _ArrisMtaDevBatteryOperSubState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 3, 1, 4),
    _ArrisMtaDevBatteryOperSubState_Type()
)
arrisMtaDevBatteryOperSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevBatteryOperSubState.setStatus("current")
_ArrisMtaDevBatteryOrderingCode_Type = SnmpAdminString
_ArrisMtaDevBatteryOrderingCode_Object = MibTableColumn
arrisMtaDevBatteryOrderingCode = _ArrisMtaDevBatteryOrderingCode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 3, 1, 5),
    _ArrisMtaDevBatteryOrderingCode_Type()
)
arrisMtaDevBatteryOrderingCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevBatteryOrderingCode.setStatus("current")
_ArrisMtaDevBatteryEprom_Type = SnmpAdminString
_ArrisMtaDevBatteryEprom_Object = MibTableColumn
arrisMtaDevBatteryEprom = _ArrisMtaDevBatteryEprom_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 3, 1, 6),
    _ArrisMtaDevBatteryEprom_Type()
)
arrisMtaDevBatteryEprom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevBatteryEprom.setStatus("current")
_ArrisMtaDevPwrSupplyBatteryTestTime_Type = Integer32
_ArrisMtaDevPwrSupplyBatteryTestTime_Object = MibScalar
arrisMtaDevPwrSupplyBatteryTestTime = _ArrisMtaDevPwrSupplyBatteryTestTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 4),
    _ArrisMtaDevPwrSupplyBatteryTestTime_Type()
)
arrisMtaDevPwrSupplyBatteryTestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyBatteryTestTime.setStatus("current")
_ArrisMtaDevPwrSupplyRatedBatCapacity_Type = Integer32
_ArrisMtaDevPwrSupplyRatedBatCapacity_Object = MibScalar
arrisMtaDevPwrSupplyRatedBatCapacity = _ArrisMtaDevPwrSupplyRatedBatCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 5),
    _ArrisMtaDevPwrSupplyRatedBatCapacity_Type()
)
arrisMtaDevPwrSupplyRatedBatCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyRatedBatCapacity.setStatus("current")
_ArrisMtaDevPwrSupplyTestedBatCapacity_Type = Integer32
_ArrisMtaDevPwrSupplyTestedBatCapacity_Object = MibScalar
arrisMtaDevPwrSupplyTestedBatCapacity = _ArrisMtaDevPwrSupplyTestedBatCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 6),
    _ArrisMtaDevPwrSupplyTestedBatCapacity_Type()
)
arrisMtaDevPwrSupplyTestedBatCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyTestedBatCapacity.setStatus("current")
_ArrisMtaDevPwrSupplyBatStateOfCharge_Type = Integer32
_ArrisMtaDevPwrSupplyBatStateOfCharge_Object = MibScalar
arrisMtaDevPwrSupplyBatStateOfCharge = _ArrisMtaDevPwrSupplyBatStateOfCharge_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 7),
    _ArrisMtaDevPwrSupplyBatStateOfCharge_Type()
)
arrisMtaDevPwrSupplyBatStateOfCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyBatStateOfCharge.setStatus("current")
_ArrisMtaDevPwrSupplyReadBatteryPwr_Type = Integer32
_ArrisMtaDevPwrSupplyReadBatteryPwr_Object = MibScalar
arrisMtaDevPwrSupplyReadBatteryPwr = _ArrisMtaDevPwrSupplyReadBatteryPwr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 8),
    _ArrisMtaDevPwrSupplyReadBatteryPwr_Type()
)
arrisMtaDevPwrSupplyReadBatteryPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyReadBatteryPwr.setStatus("current")
_ArrisMtaDevPwrSupplySecondsOnBattery_Type = Integer32
_ArrisMtaDevPwrSupplySecondsOnBattery_Object = MibScalar
arrisMtaDevPwrSupplySecondsOnBattery = _ArrisMtaDevPwrSupplySecondsOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 9),
    _ArrisMtaDevPwrSupplySecondsOnBattery_Type()
)
arrisMtaDevPwrSupplySecondsOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplySecondsOnBattery.setStatus("current")
_ArrisMtaDevPwrSupplyBatRatedMinutes_Type = Integer32
_ArrisMtaDevPwrSupplyBatRatedMinutes_Object = MibScalar
arrisMtaDevPwrSupplyBatRatedMinutes = _ArrisMtaDevPwrSupplyBatRatedMinutes_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 10),
    _ArrisMtaDevPwrSupplyBatRatedMinutes_Type()
)
arrisMtaDevPwrSupplyBatRatedMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyBatRatedMinutes.setStatus("current")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyBatRatedMinutes.setUnits("minutes")
_ArrisMtaDevPwrSupplyBatAvailableMinutes_Type = Integer32
_ArrisMtaDevPwrSupplyBatAvailableMinutes_Object = MibScalar
arrisMtaDevPwrSupplyBatAvailableMinutes = _ArrisMtaDevPwrSupplyBatAvailableMinutes_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 11),
    _ArrisMtaDevPwrSupplyBatAvailableMinutes_Type()
)
arrisMtaDevPwrSupplyBatAvailableMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyBatAvailableMinutes.setStatus("current")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyBatAvailableMinutes.setUnits("minutes")
_ArrisMtaDevPwrSupplySecondsOnBattery2_Type = Integer32
_ArrisMtaDevPwrSupplySecondsOnBattery2_Object = MibScalar
arrisMtaDevPwrSupplySecondsOnBattery2 = _ArrisMtaDevPwrSupplySecondsOnBattery2_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 12),
    _ArrisMtaDevPwrSupplySecondsOnBattery2_Type()
)
arrisMtaDevPwrSupplySecondsOnBattery2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplySecondsOnBattery2.setStatus("current")
_ArrisMtaDevPwrSupplyBatRatedMinutes2_Type = Integer32
_ArrisMtaDevPwrSupplyBatRatedMinutes2_Object = MibScalar
arrisMtaDevPwrSupplyBatRatedMinutes2 = _ArrisMtaDevPwrSupplyBatRatedMinutes2_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 13),
    _ArrisMtaDevPwrSupplyBatRatedMinutes2_Type()
)
arrisMtaDevPwrSupplyBatRatedMinutes2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyBatRatedMinutes2.setStatus("current")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyBatRatedMinutes2.setUnits("minutes")
_ArrisMtaDevPwrSupplyBatAvailableMinutes2_Type = Integer32
_ArrisMtaDevPwrSupplyBatAvailableMinutes2_Object = MibScalar
arrisMtaDevPwrSupplyBatAvailableMinutes2 = _ArrisMtaDevPwrSupplyBatAvailableMinutes2_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 14),
    _ArrisMtaDevPwrSupplyBatAvailableMinutes2_Type()
)
arrisMtaDevPwrSupplyBatAvailableMinutes2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyBatAvailableMinutes2.setStatus("current")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyBatAvailableMinutes2.setUnits("minutes")
_ArrisMtaDevPwrSupplyTelemetryValues_Type = SnmpAdminString
_ArrisMtaDevPwrSupplyTelemetryValues_Object = MibScalar
arrisMtaDevPwrSupplyTelemetryValues = _ArrisMtaDevPwrSupplyTelemetryValues_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 5, 15),
    _ArrisMtaDevPwrSupplyTelemetryValues_Type()
)
arrisMtaDevPwrSupplyTelemetryValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevPwrSupplyTelemetryValues.setStatus("current")
_ArrisMtaDevPwrSupplyAlarm_ObjectIdentity = ObjectIdentity
arrisMtaDevPwrSupplyAlarm = _ArrisMtaDevPwrSupplyAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 6)
)
_Ac_Fail_ObjectIdentity = ObjectIdentity
ac_Fail = _Ac_Fail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 6, 1)
)
_ChargerOverTemp_Shutdown_ObjectIdentity = ObjectIdentity
chargerOverTemp_Shutdown = _ChargerOverTemp_Shutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 6, 2)
)
_ChargerTemperature_High_ObjectIdentity = ObjectIdentity
chargerTemperature_High = _ChargerTemperature_High_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 6, 3)
)
_BatteryCharger_Disabled_ObjectIdentity = ObjectIdentity
batteryCharger_Disabled = _BatteryCharger_Disabled_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 6, 4)
)
_ChargerDownload_Failed_ObjectIdentity = ObjectIdentity
chargerDownload_Failed = _ChargerDownload_Failed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 6, 5)
)
_Battery_Mismatch_ObjectIdentity = ObjectIdentity
battery_Mismatch = _Battery_Mismatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 6, 6)
)
_UpsAlarmBatteryBad_ObjectIdentity = ObjectIdentity
upsAlarmBatteryBad = _UpsAlarmBatteryBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 6, 7)
)
_UpsAlarmLowBattery_ObjectIdentity = ObjectIdentity
upsAlarmLowBattery = _UpsAlarmLowBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 6, 8)
)
_UpsAlarmDepletedBattery_ObjectIdentity = ObjectIdentity
upsAlarmDepletedBattery = _UpsAlarmDepletedBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 6, 9)
)
_UpsAlarmUpsOutputOff_ObjectIdentity = ObjectIdentity
upsAlarmUpsOutputOff = _UpsAlarmUpsOutputOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 6, 10)
)
_UpsAlarmOutputOffAsRequested_ObjectIdentity = ObjectIdentity
upsAlarmOutputOffAsRequested = _UpsAlarmOutputOffAsRequested_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 6, 11)
)
_UpsAlarmGeneralFault_ObjectIdentity = ObjectIdentity
upsAlarmGeneralFault = _UpsAlarmGeneralFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 6, 12)
)
_UpsAlarmShutdownImminent_ObjectIdentity = ObjectIdentity
upsAlarmShutdownImminent = _UpsAlarmShutdownImminent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 6, 13)
)
_UpsAlarmBatteryMissing_ObjectIdentity = ObjectIdentity
upsAlarmBatteryMissing = _UpsAlarmBatteryMissing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 6, 14)
)
_UpsAlarmAwaitingPower_ObjectIdentity = ObjectIdentity
upsAlarmAwaitingPower = _UpsAlarmAwaitingPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 6, 15)
)
_UpsAlarmShutdownPending_ObjectIdentity = ObjectIdentity
upsAlarmShutdownPending = _UpsAlarmShutdownPending_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 3, 6, 16)
)
_ArrisMtaDevLineCard_ObjectIdentity = ObjectIdentity
arrisMtaDevLineCard = _ArrisMtaDevLineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 4)
)
_ArrisMtaDevLineCardTable_Object = MibTable
arrisMtaDevLineCardTable = _ArrisMtaDevLineCardTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    arrisMtaDevLineCardTable.setStatus("current")
_ArrisMtaDevLineCardEntry_Object = MibTableRow
arrisMtaDevLineCardEntry = _ArrisMtaDevLineCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 4, 1, 1)
)
arrisMtaDevLineCardEntry.setIndexNames(
    (0, "ARRIS-MTA-DEVICE-MIB", "arrisMtaDevLineCardLineNumber"),
)
if mibBuilder.loadTexts:
    arrisMtaDevLineCardEntry.setStatus("current")
_ArrisMtaDevLineCardLineNumber_Type = Integer32
_ArrisMtaDevLineCardLineNumber_Object = MibTableColumn
arrisMtaDevLineCardLineNumber = _ArrisMtaDevLineCardLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 4, 1, 1, 1),
    _ArrisMtaDevLineCardLineNumber_Type()
)
arrisMtaDevLineCardLineNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisMtaDevLineCardLineNumber.setStatus("current")


class _ArrisMtaDevLineCardState_Type(Integer32):
    """Custom type arrisMtaDevLineCardState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7,
              14)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("addressing", 2),
          ("talking", 3),
          ("frwd-disc", 5),
          ("ringing", 6),
          ("onhook-tx", 7),
          ("plo", 14))
    )


_ArrisMtaDevLineCardState_Type.__name__ = "Integer32"
_ArrisMtaDevLineCardState_Object = MibTableColumn
arrisMtaDevLineCardState = _ArrisMtaDevLineCardState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 4, 1, 1, 2),
    _ArrisMtaDevLineCardState_Type()
)
arrisMtaDevLineCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevLineCardState.setStatus("current")
_ArrisMtaDispSignal_ObjectIdentity = ObjectIdentity
arrisMtaDispSignal = _ArrisMtaDispSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 5)
)
_ArrisMtaDispSignalTable_Object = MibTable
arrisMtaDispSignalTable = _ArrisMtaDispSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    arrisMtaDispSignalTable.setStatus("current")
_ArrisMtaDispSignalEntry_Object = MibTableRow
arrisMtaDispSignalEntry = _ArrisMtaDispSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 5, 1, 1)
)
arrisMtaDispSignalEntry.setIndexNames(
    (0, "ARRIS-MTA-DEVICE-MIB", "arrisMtaDevDispSignalLogindex"),
)
if mibBuilder.loadTexts:
    arrisMtaDispSignalEntry.setStatus("current")


class _ArrisMtaDevDispSignalLogindex_Type(Integer32):
    """Custom type arrisMtaDevDispSignalLogindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ArrisMtaDevDispSignalLogindex_Type.__name__ = "Integer32"
_ArrisMtaDevDispSignalLogindex_Object = MibTableColumn
arrisMtaDevDispSignalLogindex = _ArrisMtaDevDispSignalLogindex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 5, 1, 1, 1),
    _ArrisMtaDevDispSignalLogindex_Type()
)
arrisMtaDevDispSignalLogindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisMtaDevDispSignalLogindex.setStatus("current")


class _ArrisMtaDevDispSignalLog_Type(OctetString):
    """Custom type arrisMtaDevDispSignalLog based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_ArrisMtaDevDispSignalLog_Type.__name__ = "OctetString"
_ArrisMtaDevDispSignalLog_Object = MibTableColumn
arrisMtaDevDispSignalLog = _ArrisMtaDevDispSignalLog_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 5, 1, 1, 2),
    _ArrisMtaDevDispSignalLog_Type()
)
arrisMtaDevDispSignalLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtaDevDispSignalLog.setStatus("current")
_ArrisMtadocsQosService_ObjectIdentity = ObjectIdentity
arrisMtadocsQosService = _ArrisMtadocsQosService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 6)
)
_ArrisMtadocsQosServiceTable_Object = MibTable
arrisMtadocsQosServiceTable = _ArrisMtadocsQosServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    arrisMtadocsQosServiceTable.setStatus("current")
_ArrisMtadocsQosServiceEntry_Object = MibTableRow
arrisMtadocsQosServiceEntry = _ArrisMtadocsQosServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 6, 1, 1)
)
arrisMtadocsQosServiceEntry.setIndexNames(
    (0, "ARRIS-MTA-DEVICE-MIB", "arrisMtadocsQosServiceIndex"),
)
if mibBuilder.loadTexts:
    arrisMtadocsQosServiceEntry.setStatus("current")


class _ArrisMtadocsQosServiceIndex_Type(Integer32):
    """Custom type arrisMtadocsQosServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ArrisMtadocsQosServiceIndex_Type.__name__ = "Integer32"
_ArrisMtadocsQosServiceIndex_Object = MibTableColumn
arrisMtadocsQosServiceIndex = _ArrisMtadocsQosServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 6, 1, 1, 1),
    _ArrisMtadocsQosServiceIndex_Type()
)
arrisMtadocsQosServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisMtadocsQosServiceIndex.setStatus("current")
_ArrisMtadocsQosServiceFlowID_Type = Integer32
_ArrisMtadocsQosServiceFlowID_Object = MibTableColumn
arrisMtadocsQosServiceFlowID = _ArrisMtadocsQosServiceFlowID_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 6, 1, 1, 2),
    _ArrisMtadocsQosServiceFlowID_Type()
)
arrisMtadocsQosServiceFlowID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtadocsQosServiceFlowID.setStatus("current")
_ArrisMtadocsQosServiceClassName_Type = OctetString
_ArrisMtadocsQosServiceClassName_Object = MibTableColumn
arrisMtadocsQosServiceClassName = _ArrisMtadocsQosServiceClassName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 6, 1, 1, 3),
    _ArrisMtadocsQosServiceClassName_Type()
)
arrisMtadocsQosServiceClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtadocsQosServiceClassName.setStatus("current")
_ArrisMtdocsQosServiceFlowDirection_Type = OctetString
_ArrisMtdocsQosServiceFlowDirection_Object = MibTableColumn
arrisMtdocsQosServiceFlowDirection = _ArrisMtdocsQosServiceFlowDirection_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 6, 1, 1, 4),
    _ArrisMtdocsQosServiceFlowDirection_Type()
)
arrisMtdocsQosServiceFlowDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtdocsQosServiceFlowDirection.setStatus("current")
_ArrisMtdocsQosServicePrimaryFlow_Type = OctetString
_ArrisMtdocsQosServicePrimaryFlow_Object = MibTableColumn
arrisMtdocsQosServicePrimaryFlow = _ArrisMtdocsQosServicePrimaryFlow_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 6, 1, 1, 5),
    _ArrisMtdocsQosServicePrimaryFlow_Type()
)
arrisMtdocsQosServicePrimaryFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtdocsQosServicePrimaryFlow.setStatus("current")
_ArrisMtadocsQosTrafficType_Type = OctetString
_ArrisMtadocsQosTrafficType_Object = MibTableColumn
arrisMtadocsQosTrafficType = _ArrisMtadocsQosTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 6, 1, 1, 6),
    _ArrisMtadocsQosTrafficType_Type()
)
arrisMtadocsQosTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtadocsQosTrafficType.setStatus("current")
_ArrisMtadocsQosServicePackets_Type = Integer32
_ArrisMtadocsQosServicePackets_Object = MibTableColumn
arrisMtadocsQosServicePackets = _ArrisMtadocsQosServicePackets_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 6, 1, 1, 7),
    _ArrisMtadocsQosServicePackets_Type()
)
arrisMtadocsQosServicePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtadocsQosServicePackets.setStatus("current")


class _ArrisMtadocsQosDisableLoggin_Type(Integer32):
    """Custom type arrisMtadocsQosDisableLoggin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableLoggin", 1),
          ("enableLoggin", 2))
    )


_ArrisMtadocsQosDisableLoggin_Type.__name__ = "Integer32"
_ArrisMtadocsQosDisableLoggin_Object = MibScalar
arrisMtadocsQosDisableLoggin = _ArrisMtadocsQosDisableLoggin_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 6, 2),
    _ArrisMtadocsQosDisableLoggin_Type()
)
arrisMtadocsQosDisableLoggin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtadocsQosDisableLoggin.setStatus("current")
_ArrisMtadocsQosLogClear_Type = TruthValue
_ArrisMtadocsQosLogClear_Object = MibScalar
arrisMtadocsQosLogClear = _ArrisMtadocsQosLogClear_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 6, 3),
    _ArrisMtadocsQosLogClear_Type()
)
arrisMtadocsQosLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtadocsQosLogClear.setStatus("current")
_ArrisMtadocsQosShowDsxLogTable_Object = MibTable
arrisMtadocsQosShowDsxLogTable = _ArrisMtadocsQosShowDsxLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 6, 4)
)
if mibBuilder.loadTexts:
    arrisMtadocsQosShowDsxLogTable.setStatus("current")
_ArrisMtadocsQosShowDsxLogEntry_Object = MibTableRow
arrisMtadocsQosShowDsxLogEntry = _ArrisMtadocsQosShowDsxLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 6, 4, 1)
)
arrisMtadocsQosShowDsxLogEntry.setIndexNames(
    (0, "ARRIS-MTA-DEVICE-MIB", "arrisMtadocsQosShowDsxLogIndex"),
)
if mibBuilder.loadTexts:
    arrisMtadocsQosShowDsxLogEntry.setStatus("current")


class _ArrisMtadocsQosShowDsxLogIndex_Type(Integer32):
    """Custom type arrisMtadocsQosShowDsxLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ArrisMtadocsQosShowDsxLogIndex_Type.__name__ = "Integer32"
_ArrisMtadocsQosShowDsxLogIndex_Object = MibTableColumn
arrisMtadocsQosShowDsxLogIndex = _ArrisMtadocsQosShowDsxLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 6, 4, 1, 1),
    _ArrisMtadocsQosShowDsxLogIndex_Type()
)
arrisMtadocsQosShowDsxLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisMtadocsQosShowDsxLogIndex.setStatus("current")


class _ArrisMtadocsQosShowDsxLog_Type(OctetString):
    """Custom type arrisMtadocsQosShowDsxLog based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_ArrisMtadocsQosShowDsxLog_Type.__name__ = "OctetString"
_ArrisMtadocsQosShowDsxLog_Object = MibTableColumn
arrisMtadocsQosShowDsxLog = _ArrisMtadocsQosShowDsxLog_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3, 1, 6, 4, 1, 2),
    _ArrisMtadocsQosShowDsxLog_Type()
)
arrisMtadocsQosShowDsxLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisMtadocsQosShowDsxLog.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-MTA-DEVICE-MIB",
    **{"ArrsMtaDevProvMethod": ArrsMtaDevProvMethod,
       "CodecType": CodecType,
       "PacketizationPeriodType": PacketizationPeriodType,
       "SignalingProtocol": SignalingProtocol,
       "arrisMtaDevMib": arrisMtaDevMib,
       "arrisMtaDevMibObjects": arrisMtaDevMibObjects,
       "arrisMtaDevBase": arrisMtaDevBase,
       "arrisMtaDevMonitoringMib": arrisMtaDevMonitoringMib,
       "arrisMtaDevControl": arrisMtaDevControl,
       "arrisMtaDevResetCallStats": arrisMtaDevResetCallStats,
       "arrisMtaDevEnableCallpSigTrace": arrisMtaDevEnableCallpSigTrace,
       "arrisMtaDevEnableCallStatsSyslogRpt": arrisMtaDevEnableCallStatsSyslogRpt,
       "arrisMtaDevSwDnldNoSvcImpact": arrisMtaDevSwDnldNoSvcImpact,
       "arrisMtaDevEnableCallSigLastMsgRpt": arrisMtaDevEnableCallSigLastMsgRpt,
       "arrisMtaDevNsadSwDnldStatus": arrisMtaDevNsadSwDnldStatus,
       "arrisMtaDevRestoreNvmFactoryDefault": arrisMtaDevRestoreNvmFactoryDefault,
       "arrisMtaDevEnableLogging": arrisMtaDevEnableLogging,
       "arrisMtaDevLoggingContext": arrisMtaDevLoggingContext,
       "arrisMtaDevEnablePacketLossConcealment": arrisMtaDevEnablePacketLossConcealment,
       "arrisMtaDevEnableRTCPStaticInterval": arrisMtaDevEnableRTCPStaticInterval,
       "arrisMtaDevTrace": arrisMtaDevTrace,
       "arrisMtaDevRtpTxPktsTotal": arrisMtaDevRtpTxPktsTotal,
       "arrisMtaDevRtpRxPktsTotal": arrisMtaDevRtpRxPktsTotal,
       "arrisMtaDevRtpPercentPktsLostTotal": arrisMtaDevRtpPercentPktsLostTotal,
       "arrisMtaDevProvState": arrisMtaDevProvState,
       "arrisMtaDevSWUpgradeStatus": arrisMtaDevSWUpgradeStatus,
       "arrisMtaDevSignalingAvgLatency": arrisMtaDevSignalingAvgLatency,
       "arrisMtaDevSignalingTxSuccessfulMsgCnt": arrisMtaDevSignalingTxSuccessfulMsgCnt,
       "arrisMtaDevSignalingRxSuccessfulMsgCnt": arrisMtaDevSignalingRxSuccessfulMsgCnt,
       "arrisMtaDevSignalingTxNAKCnt": arrisMtaDevSignalingTxNAKCnt,
       "arrisMtaDevSignalingRxNAKCnt": arrisMtaDevSignalingRxNAKCnt,
       "arrisMtaDevSignalingRxNoACKCnt": arrisMtaDevSignalingRxNoACKCnt,
       "arrisMtaDevSignalingLastMsg1": arrisMtaDevSignalingLastMsg1,
       "arrisMtaDevSignalingLastMsg2": arrisMtaDevSignalingLastMsg2,
       "arrisMtaDevSignalingLastMsg3": arrisMtaDevSignalingLastMsg3,
       "arrisMtaDevSignalingLastMsg4": arrisMtaDevSignalingLastMsg4,
       "arrisMtaDevSignalingLastMsg5": arrisMtaDevSignalingLastMsg5,
       "arrisMtaDevSignalingLastMsg6": arrisMtaDevSignalingLastMsg6,
       "arrisMtaDevSignalingLastMsg7": arrisMtaDevSignalingLastMsg7,
       "arrisMtaDevSignalingLastMsg8": arrisMtaDevSignalingLastMsg8,
       "arrisMtaDevSignalingLastMsg9": arrisMtaDevSignalingLastMsg9,
       "arrisMtaDevSignalingLastMsg10": arrisMtaDevSignalingLastMsg10,
       "arrisMtaDevSignalingLastMsg11": arrisMtaDevSignalingLastMsg11,
       "arrisMtaDevSignalingLastMsg12": arrisMtaDevSignalingLastMsg12,
       "arrisMtaDevSignalingLastMsg13": arrisMtaDevSignalingLastMsg13,
       "arrisMtaDevSignalingLastMsg14": arrisMtaDevSignalingLastMsg14,
       "arrisMtaDevSignalingLastMsg15": arrisMtaDevSignalingLastMsg15,
       "arrisMtaDevSignalingLastMsg16": arrisMtaDevSignalingLastMsg16,
       "arrisMtaDevEstimatedMinutesRemaining": arrisMtaDevEstimatedMinutesRemaining,
       "arrisMtaDevEstimatedChargeRemaining": arrisMtaDevEstimatedChargeRemaining,
       "arrisMtaDevCallStatsTable": arrisMtaDevCallStatsTable,
       "arrisMtaDevCallStatsEntry": arrisMtaDevCallStatsEntry,
       "arrisMtaDevCallStatsIndex": arrisMtaDevCallStatsIndex,
       "arrisMtaDevCallStatsRtpTxPkts": arrisMtaDevCallStatsRtpTxPkts,
       "arrisMtaDevCallStatsRtpRxPkts": arrisMtaDevCallStatsRtpRxPkts,
       "arrisMtaDevCallStatsRtpPercentPktsLost": arrisMtaDevCallStatsRtpPercentPktsLost,
       "arrisMtaDevCallStatsAvgJitter": arrisMtaDevCallStatsAvgJitter,
       "arrisMtaDevCallStatsMaxJitter": arrisMtaDevCallStatsMaxJitter,
       "arrisMtaDevCallStatsAvgLatency": arrisMtaDevCallStatsAvgLatency,
       "arrisMtaDevCallStatsHookStatus": arrisMtaDevCallStatsHookStatus,
       "arrisMtaDevCallStatsSLICStatus": arrisMtaDevCallStatsSLICStatus,
       "arrisMtaDevCallStatsEndPntOpStatus": arrisMtaDevCallStatsEndPntOpStatus,
       "arrisMtaDevCallStatsLineSubState": arrisMtaDevCallStatsLineSubState,
       "arrisMtaDevRtpPktsLostTotal": arrisMtaDevRtpPktsLostTotal,
       "arrisMtaDevLastCallStartTime": arrisMtaDevLastCallStartTime,
       "arrisMtaDevLastCallEndTime": arrisMtaDevLastCallEndTime,
       "arrisMtaDevParameters": arrisMtaDevParameters,
       "arrisMtaDevMaxCpeAllowed": arrisMtaDevMaxCpeAllowed,
       "arrisMtaDevNetworkAccess": arrisMtaDevNetworkAccess,
       "arrisMtaDevLineParameterTable": arrisMtaDevLineParameterTable,
       "arrisMtaDevLineParameterEntry": arrisMtaDevLineParameterEntry,
       "arrisMtaDevInterfaceIndex": arrisMtaDevInterfaceIndex,
       "arrisMtaDevPktcDevEvEndpointName": arrisMtaDevPktcDevEvEndpointName,
       "arrisMtaDevActiveConnections": arrisMtaDevActiveConnections,
       "arrisMtaDevLineMWIActive": arrisMtaDevLineMWIActive,
       "arrisMtaDevUpSvcFlowParameterTable": arrisMtaDevUpSvcFlowParameterTable,
       "arrisMtaDevUpSvcFlowParameterEntry": arrisMtaDevUpSvcFlowParameterEntry,
       "arrisMtaDevDocsQosParamUpSvcFlowSFID": arrisMtaDevDocsQosParamUpSvcFlowSFID,
       "arrisMtaDevDocsQosParamUpSvcFlowSchedulingType": arrisMtaDevDocsQosParamUpSvcFlowSchedulingType,
       "arrisMtaDevQosMode": arrisMtaDevQosMode,
       "arrisMtaDevEventFormat": arrisMtaDevEventFormat,
       "arrisMtaDevVqm": arrisMtaDevVqm,
       "arrisMtaDevVqmLine": arrisMtaDevVqmLine,
       "arrisMtaDevVqmClear": arrisMtaDevVqmClear,
       "arrisMtaDevVqmEnable": arrisMtaDevVqmEnable,
       "arrisMtaDevVqmCallNumberTable": arrisMtaDevVqmCallNumberTable,
       "arrisMtaDevVqmCallNumberEntry": arrisMtaDevVqmCallNumberEntry,
       "arrisMtaDevVqmCallNumberIndex": arrisMtaDevVqmCallNumberIndex,
       "arrisMtaDevVqmCallNumberIds": arrisMtaDevVqmCallNumberIds,
       "arrisMtaDevVqmCallNumberIdentifier": arrisMtaDevVqmCallNumberIdentifier,
       "arrisMtaDevVqmMetricTable": arrisMtaDevVqmMetricTable,
       "arrisMtaDevVqmMetricEntry": arrisMtaDevVqmMetricEntry,
       "arrisMtaDevVqmMetricIndex": arrisMtaDevVqmMetricIndex,
       "arrisMtaDevVqmMetricValues": arrisMtaDevVqmMetricValues,
       "arrisMtaDevVqmThresholds": arrisMtaDevVqmThresholds,
       "arrisMtaDevVqmEnableRemote": arrisMtaDevVqmEnableRemote,
       "arrisMtaDevVqmThresholdEnable": arrisMtaDevVqmThresholdEnable,
       "arrisMtaDevVqmHistorySize": arrisMtaDevVqmHistorySize,
       "arrisMtaDevVqmCallNumberIdentifierLastCall": arrisMtaDevVqmCallNumberIdentifierLastCall,
       "arrisMtaDevDhcp": arrisMtaDevDhcp,
       "arrisMtaDevDhcpMtaParameters": arrisMtaDevDhcpMtaParameters,
       "arrisMtaDevDhcpMtaIpFQDN": arrisMtaDevDhcpMtaIpFQDN,
       "arrisMtaDevDhcpMtaIpAddr": arrisMtaDevDhcpMtaIpAddr,
       "arrisMtaDevDhcpMtaSubNetMask": arrisMtaDevDhcpMtaSubNetMask,
       "arrisMtaDevDhcpMtaGatewayIpAddr": arrisMtaDevDhcpMtaGatewayIpAddr,
       "arrisMtaDevDhcpMtaConfigFile": arrisMtaDevDhcpMtaConfigFile,
       "arrisMtaDevDhcpSvrParameters": arrisMtaDevDhcpSvrParameters,
       "arrisMtaDevDhcpState": arrisMtaDevDhcpState,
       "arrisMtaDevDhcpPrimaryDhcpSvrIpAddr": arrisMtaDevDhcpPrimaryDhcpSvrIpAddr,
       "arrisMtaDevDhcpSecondaryDhcpSvrIpAddr": arrisMtaDevDhcpSecondaryDhcpSvrIpAddr,
       "arrisMtaDevDhcpPrimaryDNSSvrIpAddr": arrisMtaDevDhcpPrimaryDNSSvrIpAddr,
       "arrisMtaDevDhcpSecondaryDNSSvrIpAddr": arrisMtaDevDhcpSecondaryDNSSvrIpAddr,
       "arrisMtaDevDhcpLeaseParameters": arrisMtaDevDhcpLeaseParameters,
       "arrisMtaDevDhcpOfferedLeaseTime": arrisMtaDevDhcpOfferedLeaseTime,
       "arrisMtaDevDhcpLeaseTimeRemaining": arrisMtaDevDhcpLeaseTimeRemaining,
       "arrisMtaDevDhcpTimeUntilRenew": arrisMtaDevDhcpTimeUntilRenew,
       "arrisMtaDevDhcpTimeUntilRebind": arrisMtaDevDhcpTimeUntilRebind,
       "arrisMtaDevDhcpPktcOptParameters": arrisMtaDevDhcpPktcOptParameters,
       "arrisMtaDevDhcpPktcOptionId": arrisMtaDevDhcpPktcOptionId,
       "arrisMtaDevDhcpSvcProviderSnmpEntity": arrisMtaDevDhcpSvcProviderSnmpEntity,
       "arrisMtaDevDhcpKerberosRealmFqdn": arrisMtaDevDhcpKerberosRealmFqdn,
       "arrisMtaDevDhcpRequestTgt": arrisMtaDevDhcpRequestTgt,
       "arrisMtaDevDhcpProvTimer": arrisMtaDevDhcpProvTimer,
       "arrisMtaDevDhcpSecTicketInvalid": arrisMtaDevDhcpSecTicketInvalid,
       "arrisMtaDevSetup": arrisMtaDevSetup,
       "arrisMtaDevOperationalSetup": arrisMtaDevOperationalSetup,
       "arrisMtaDevVPNomJitterBuffer": arrisMtaDevVPNomJitterBuffer,
       "arrisMtaDevVPJitterBufferMode": arrisMtaDevVPJitterBufferMode,
       "arrisMtaDevRTPTxQueueSize": arrisMtaDevRTPTxQueueSize,
       "arrisMtaDevEchoCancellerTailLength": arrisMtaDevEchoCancellerTailLength,
       "arrisMtaDevDspHandleNonPhaseReversedTone": arrisMtaDevDspHandleNonPhaseReversedTone,
       "arrisMtaDevProvMethodIndicator": arrisMtaDevProvMethodIndicator,
       "arrisMtaCfgRTPDynPortStart": arrisMtaCfgRTPDynPortStart,
       "arrisMtaCfgRTPDynPortEnd": arrisMtaCfgRTPDynPortEnd,
       "arrisMtaDevVPMaxJitterBuffer": arrisMtaDevVPMaxJitterBuffer,
       "arrisMtaDevOptionality": arrisMtaDevOptionality,
       "arrisMtaDevOptionality8ChnlKey": arrisMtaDevOptionality8ChnlKey,
       "arrisMtaDevOptionality8ChnlEnable": arrisMtaDevOptionality8ChnlEnable,
       "arrisMtaDevOptionalityLoopDiagKey": arrisMtaDevOptionalityLoopDiagKey,
       "arrisMtaDevLoopVoltageMgmt": arrisMtaDevLoopVoltageMgmt,
       "arrisMtaDevLoopVoltageKey": arrisMtaDevLoopVoltageKey,
       "arrisMtaDevLoopVoltagePolicy": arrisMtaDevLoopVoltagePolicy,
       "arrisMtaDevLoopVoltageResetTimeout": arrisMtaDevLoopVoltageResetTimeout,
       "arrisMtaDevLoopVoltageMaintTimeout": arrisMtaDevLoopVoltageMaintTimeout,
       "arrisMtaDevGainControl": arrisMtaDevGainControl,
       "arrisMtaDevGainControlFSK": arrisMtaDevGainControlFSK,
       "arrisMtaDevGainControlCAS": arrisMtaDevGainControlCAS,
       "arrisMtaDevGainControlLocalTone": arrisMtaDevGainControlLocalTone,
       "arrisMtaDevGainControlNetworkTone": arrisMtaDevGainControlNetworkTone,
       "arrisMtaDevGainControlLocalDTMF": arrisMtaDevGainControlLocalDTMF,
       "arrisMtaDevGainControlNetworkDTMF": arrisMtaDevGainControlNetworkDTMF,
       "arrisMtaDevGainControlTxVoice": arrisMtaDevGainControlTxVoice,
       "arrisMtaDevGainControlRxVoice": arrisMtaDevGainControlRxVoice,
       "arrisMtaDevEnableIndexTenEleven": arrisMtaDevEnableIndexTenEleven,
       "arrisMtaDevDspCpsSetting": arrisMtaDevDspCpsSetting,
       "arrisMtaDevDiag": arrisMtaDevDiag,
       "arrisMtaDevDiagLoopTable": arrisMtaDevDiagLoopTable,
       "arrisMtaDevDiagLoopEntry": arrisMtaDevDiagLoopEntry,
       "arrisMtaDevDiagLoopIndex": arrisMtaDevDiagLoopIndex,
       "arrisMtaDevDiagLoopTime": arrisMtaDevDiagLoopTime,
       "arrisMtaDevDiagLoopRequest": arrisMtaDevDiagLoopRequest,
       "arrisMtaDevDiagLoopLastResult": arrisMtaDevDiagLoopLastResult,
       "arrisMtaDevDiagLoopHazardousPotentialTest": arrisMtaDevDiagLoopHazardousPotentialTest,
       "arrisMtaDevDiagLoopForeignEmfTest": arrisMtaDevDiagLoopForeignEmfTest,
       "arrisMtaDevDiagLoopResistiveFaultsTest": arrisMtaDevDiagLoopResistiveFaultsTest,
       "arrisMtaDevDiagLoopReceiverOffHookTest": arrisMtaDevDiagLoopReceiverOffHookTest,
       "arrisMtaDevDiagLoopRingerTest": arrisMtaDevDiagLoopRingerTest,
       "arrisMtaDevVbdOverwriteLineBitmap": arrisMtaDevVbdOverwriteLineBitmap,
       "arrisMtaDevVbdOverwriteMinJitterBuffer": arrisMtaDevVbdOverwriteMinJitterBuffer,
       "arrisMtaDevVbdOverwriteNomJitterBuffer": arrisMtaDevVbdOverwriteNomJitterBuffer,
       "arrisMtaDevVbdOverwriteMaxJitterBuffer": arrisMtaDevVbdOverwriteMaxJitterBuffer,
       "arrisMtaDevEventHideFQDNandIPAddress": arrisMtaDevEventHideFQDNandIPAddress,
       "arrisMtaDevDhcpOptionOverride": arrisMtaDevDhcpOptionOverride,
       "arrisMtaDevTFTPServerAddrOverrideFQDN": arrisMtaDevTFTPServerAddrOverrideFQDN,
       "arrisMtaDevDefaultReasonNoCIDName": arrisMtaDevDefaultReasonNoCIDName,
       "arrisMtaDevSipConfigFileURL": arrisMtaDevSipConfigFileURL,
       "arrisMtaDevSipDwnldConfig": arrisMtaDevSipDwnldConfig,
       "arrisMtaDevSpecialConfigurationOverrideEnable": arrisMtaDevSpecialConfigurationOverrideEnable,
       "arrisMtaDevRtcpTosValue": arrisMtaDevRtcpTosValue,
       "arrisMtaDevAutomaticOsiDelay": arrisMtaDevAutomaticOsiDelay,
       "arrisMtaDevCustomJitterBufferEnabled": arrisMtaDevCustomJitterBufferEnabled,
       "arrisMtaDevCustomMinJitterBuffer": arrisMtaDevCustomMinJitterBuffer,
       "arrisMtaDevCustomNomJitterBuffer": arrisMtaDevCustomNomJitterBuffer,
       "arrisMtaDevCustomMaxJitterBuffer": arrisMtaDevCustomMaxJitterBuffer,
       "arrisMtaDevEnableDHCPLog": arrisMtaDevEnableDHCPLog,
       "arrisMtaDevEnableMGCPLog": arrisMtaDevEnableMGCPLog,
       "arrisMtaDevClearDHCPLog": arrisMtaDevClearDHCPLog,
       "arrisMtaDevClearMGCPLog": arrisMtaDevClearMGCPLog,
       "arrisMtaDevTDDReportToCMS": arrisMtaDevTDDReportToCMS,
       "arrisMtaDevAutomaticCallResourceRecovery": arrisMtaDevAutomaticCallResourceRecovery,
       "arrisMtaDevPacketcableProvisioningFlow": arrisMtaDevPacketcableProvisioningFlow,
       "arrisMtaDevLevelControl": arrisMtaDevLevelControl,
       "arrisMtaDevLevelControlOffHookEnable": arrisMtaDevLevelControlOffHookEnable,
       "arrisMtaDevLevelControlOffHookFSK": arrisMtaDevLevelControlOffHookFSK,
       "arrisMtaDevLevelControlOffHookCAS": arrisMtaDevLevelControlOffHookCAS,
       "arrisMtaDevOffHookFskDelay": arrisMtaDevOffHookFskDelay,
       "arrisMtaDevT38Timeout": arrisMtaDevT38Timeout,
       "arrisMtaDevSuperG3FaxRelay": arrisMtaDevSuperG3FaxRelay,
       "arrisMtaDevDTMFEndEventForceAscending": arrisMtaDevDTMFEndEventForceAscending,
       "arrisMtaDevDspHandleBellModemTone": arrisMtaDevDspHandleBellModemTone,
       "arrisMtaDevDhcpSubOpt3Immediate": arrisMtaDevDhcpSubOpt3Immediate,
       "arrisMtaDevMaxCallPServiceFlows": arrisMtaDevMaxCallPServiceFlows,
       "arrisMtaDevCmIp": arrisMtaDevCmIp,
       "arrisMtaDevCmIpTable": arrisMtaDevCmIpTable,
       "arrisMtaDevCmIpEntry": arrisMtaDevCmIpEntry,
       "arrisMtaDevCmIpIndex": arrisMtaDevCmIpIndex,
       "arrisMtaDevCmIpAddressType": arrisMtaDevCmIpAddressType,
       "arrisMtaDevCmIpAddress": arrisMtaDevCmIpAddress,
       "arrisMtaDevCmIpPhysAddress": arrisMtaDevCmIpPhysAddress,
       "arrisMtaDevHDAudioDefaultPayloadType": arrisMtaDevHDAudioDefaultPayloadType,
       "arrisMtaDevWBSLIC": arrisMtaDevWBSLIC,
       "arrisMtaDevProvisionedCodecArray": arrisMtaDevProvisionedCodecArray,
       "arrisMtaDevHDAudioG722SampleRate": arrisMtaDevHDAudioG722SampleRate,
       "arrisMtaDevHDAudioEnable": arrisMtaDevHDAudioEnable,
       "arrisMtaDevRtcpJitterDisabled": arrisMtaDevRtcpJitterDisabled,
       "arrisMtaDevEndPntSetup": arrisMtaDevEndPntSetup,
       "arrisMtaDevEndPntTable": arrisMtaDevEndPntTable,
       "arrisMtaDevEndPntEntry": arrisMtaDevEndPntEntry,
       "arrisMtaDevEndPntIndex": arrisMtaDevEndPntIndex,
       "arrisMtaDevEndPntDialingMethod": arrisMtaDevEndPntDialingMethod,
       "arrisMtaDevEndPntRingingWaveform": arrisMtaDevEndPntRingingWaveform,
       "arrisMtaDevEndPntFaxOnlyLineTimeout": arrisMtaDevEndPntFaxOnlyLineTimeout,
       "arrisMtaDevPersistentLineStatus": arrisMtaDevPersistentLineStatus,
       "arrisMtaDevEndPntCallWaitingRepeatSteady": arrisMtaDevEndPntCallWaitingRepeatSteady,
       "arrisMtaDevEndPntCIDEnable": arrisMtaDevEndPntCIDEnable,
       "arrisMtaDevEndPntCIDNameEnable": arrisMtaDevEndPntCIDNameEnable,
       "arrisMtaDevEndPntCIDDateTimeEnable": arrisMtaDevEndPntCIDDateTimeEnable,
       "arrisMtaDevEndPntLoopReversal": arrisMtaDevEndPntLoopReversal,
       "arrisMtaDevEndPntGainControlTxVoice": arrisMtaDevEndPntGainControlTxVoice,
       "arrisMtaDevEndPntGainControlRxVoice": arrisMtaDevEndPntGainControlRxVoice,
       "arrisMtaDevEndPntHDAudioEnable": arrisMtaDevEndPntHDAudioEnable,
       "arrisMtaDevEndPntHDAudioStatus": arrisMtaDevEndPntHDAudioStatus,
       "arrisMtaDevEndPntCallPState": arrisMtaDevEndPntCallPState,
       "arrisMtaDevPowerSupplyTelemetry": arrisMtaDevPowerSupplyTelemetry,
       "arrisMtaDevPwrSupplyBase": arrisMtaDevPwrSupplyBase,
       "arrisMtaDevBatteryChargerFWRev": arrisMtaDevBatteryChargerFWRev,
       "arrisMtaDevPwrSupplyControl": arrisMtaDevPwrSupplyControl,
       "arrisMtaDevPwrSupplyEnableDataShutdown": arrisMtaDevPwrSupplyEnableDataShutdown,
       "arrisMtaDevPwrSupplyEnableWifiShutdown": arrisMtaDevPwrSupplyEnableWifiShutdown,
       "arrisMtaDevPwrSupplyLowBatteryThresh": arrisMtaDevPwrSupplyLowBatteryThresh,
       "arrisMtaDevPwrSupplyTypicalIdlePwr": arrisMtaDevPwrSupplyTypicalIdlePwr,
       "arrisMtaDevPwrSupplyReplaceBatThresh": arrisMtaDevPwrSupplyReplaceBatThresh,
       "arrisMtaDevPwrSupplyChargeState": arrisMtaDevPwrSupplyChargeState,
       "arrisMtaDevPwrSupplyBatteryTest": arrisMtaDevPwrSupplyBatteryTest,
       "arrisMtaDevPwrSupplyConfigRunTime": arrisMtaDevPwrSupplyConfigRunTime,
       "arrisMtaDevPwrSupplyConfigReplaceBatTime": arrisMtaDevPwrSupplyConfigReplaceBatTime,
       "arrisMtaDevPwrSupplyConfigReplaceBatTime2": arrisMtaDevPwrSupplyConfigReplaceBatTime2,
       "arrisMtaDevPwrSupplyOverTempAlarmControl": arrisMtaDevPwrSupplyOverTempAlarmControl,
       "arrisMtaDevPwrSupplyOverTempAlarmThreshold": arrisMtaDevPwrSupplyOverTempAlarmThreshold,
       "arrisMtaDevPwrSupplyTemperature": arrisMtaDevPwrSupplyTemperature,
       "arrisMtaDevPwrSupplyHiTempBatteryShutdownControl": arrisMtaDevPwrSupplyHiTempBatteryShutdownControl,
       "arrisMtaDevPwrSupplyHighestTemperature": arrisMtaDevPwrSupplyHighestTemperature,
       "arrisMtaDevPwrSupplyHighestTemperatureTime": arrisMtaDevPwrSupplyHighestTemperatureTime,
       "arrisMtaDevPwrSupplyHighestTemperatureClear": arrisMtaDevPwrSupplyHighestTemperatureClear,
       "arrisMtaDevPwrSupplyControlChargerReset": arrisMtaDevPwrSupplyControlChargerReset,
       "arrisMtaDevPwrSupplyTimers": arrisMtaDevPwrSupplyTimers,
       "arrisMtaDevPwrSupplyDataShutdownTime": arrisMtaDevPwrSupplyDataShutdownTime,
       "arrisMtaDevPwrSupplyFullChargeTime": arrisMtaDevPwrSupplyFullChargeTime,
       "arrisMtaDevPwrSupplyStats": arrisMtaDevPwrSupplyStats,
       "arrisMtaDevBatteryStatusTable": arrisMtaDevBatteryStatusTable,
       "arrisMtaDevBatteryStatusEntry": arrisMtaDevBatteryStatusEntry,
       "arrisMtaDevBatteryStatusIndex": arrisMtaDevBatteryStatusIndex,
       "arrisMtaDevBatteryOperState": arrisMtaDevBatteryOperState,
       "arrisMtaDevBatteryLastStateChange": arrisMtaDevBatteryLastStateChange,
       "arrisMtaDevBatteryOperSubState": arrisMtaDevBatteryOperSubState,
       "arrisMtaDevBatteryOrderingCode": arrisMtaDevBatteryOrderingCode,
       "arrisMtaDevBatteryEprom": arrisMtaDevBatteryEprom,
       "arrisMtaDevPwrSupplyBatteryTestTime": arrisMtaDevPwrSupplyBatteryTestTime,
       "arrisMtaDevPwrSupplyRatedBatCapacity": arrisMtaDevPwrSupplyRatedBatCapacity,
       "arrisMtaDevPwrSupplyTestedBatCapacity": arrisMtaDevPwrSupplyTestedBatCapacity,
       "arrisMtaDevPwrSupplyBatStateOfCharge": arrisMtaDevPwrSupplyBatStateOfCharge,
       "arrisMtaDevPwrSupplyReadBatteryPwr": arrisMtaDevPwrSupplyReadBatteryPwr,
       "arrisMtaDevPwrSupplySecondsOnBattery": arrisMtaDevPwrSupplySecondsOnBattery,
       "arrisMtaDevPwrSupplyBatRatedMinutes": arrisMtaDevPwrSupplyBatRatedMinutes,
       "arrisMtaDevPwrSupplyBatAvailableMinutes": arrisMtaDevPwrSupplyBatAvailableMinutes,
       "arrisMtaDevPwrSupplySecondsOnBattery2": arrisMtaDevPwrSupplySecondsOnBattery2,
       "arrisMtaDevPwrSupplyBatRatedMinutes2": arrisMtaDevPwrSupplyBatRatedMinutes2,
       "arrisMtaDevPwrSupplyBatAvailableMinutes2": arrisMtaDevPwrSupplyBatAvailableMinutes2,
       "arrisMtaDevPwrSupplyTelemetryValues": arrisMtaDevPwrSupplyTelemetryValues,
       "arrisMtaDevPwrSupplyAlarm": arrisMtaDevPwrSupplyAlarm,
       "ac-Fail": ac_Fail,
       "chargerOverTemp-Shutdown": chargerOverTemp_Shutdown,
       "chargerTemperature-High": chargerTemperature_High,
       "batteryCharger-Disabled": batteryCharger_Disabled,
       "chargerDownload-Failed": chargerDownload_Failed,
       "battery-Mismatch": battery_Mismatch,
       "upsAlarmBatteryBad": upsAlarmBatteryBad,
       "upsAlarmLowBattery": upsAlarmLowBattery,
       "upsAlarmDepletedBattery": upsAlarmDepletedBattery,
       "upsAlarmUpsOutputOff": upsAlarmUpsOutputOff,
       "upsAlarmOutputOffAsRequested": upsAlarmOutputOffAsRequested,
       "upsAlarmGeneralFault": upsAlarmGeneralFault,
       "upsAlarmShutdownImminent": upsAlarmShutdownImminent,
       "upsAlarmBatteryMissing": upsAlarmBatteryMissing,
       "upsAlarmAwaitingPower": upsAlarmAwaitingPower,
       "upsAlarmShutdownPending": upsAlarmShutdownPending,
       "arrisMtaDevLineCard": arrisMtaDevLineCard,
       "arrisMtaDevLineCardTable": arrisMtaDevLineCardTable,
       "arrisMtaDevLineCardEntry": arrisMtaDevLineCardEntry,
       "arrisMtaDevLineCardLineNumber": arrisMtaDevLineCardLineNumber,
       "arrisMtaDevLineCardState": arrisMtaDevLineCardState,
       "arrisMtaDispSignal": arrisMtaDispSignal,
       "arrisMtaDispSignalTable": arrisMtaDispSignalTable,
       "arrisMtaDispSignalEntry": arrisMtaDispSignalEntry,
       "arrisMtaDevDispSignalLogindex": arrisMtaDevDispSignalLogindex,
       "arrisMtaDevDispSignalLog": arrisMtaDevDispSignalLog,
       "arrisMtadocsQosService": arrisMtadocsQosService,
       "arrisMtadocsQosServiceTable": arrisMtadocsQosServiceTable,
       "arrisMtadocsQosServiceEntry": arrisMtadocsQosServiceEntry,
       "arrisMtadocsQosServiceIndex": arrisMtadocsQosServiceIndex,
       "arrisMtadocsQosServiceFlowID": arrisMtadocsQosServiceFlowID,
       "arrisMtadocsQosServiceClassName": arrisMtadocsQosServiceClassName,
       "arrisMtdocsQosServiceFlowDirection": arrisMtdocsQosServiceFlowDirection,
       "arrisMtdocsQosServicePrimaryFlow": arrisMtdocsQosServicePrimaryFlow,
       "arrisMtadocsQosTrafficType": arrisMtadocsQosTrafficType,
       "arrisMtadocsQosServicePackets": arrisMtadocsQosServicePackets,
       "arrisMtadocsQosDisableLoggin": arrisMtadocsQosDisableLoggin,
       "arrisMtadocsQosLogClear": arrisMtadocsQosLogClear,
       "arrisMtadocsQosShowDsxLogTable": arrisMtadocsQosShowDsxLogTable,
       "arrisMtadocsQosShowDsxLogEntry": arrisMtadocsQosShowDsxLogEntry,
       "arrisMtadocsQosShowDsxLogIndex": arrisMtadocsQosShowDsxLogIndex,
       "arrisMtadocsQosShowDsxLog": arrisMtadocsQosShowDsxLog}
)
