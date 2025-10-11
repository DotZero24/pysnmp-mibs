# SNMP MIB module (ALU-IP-TRANSPORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/ALU-IP-TRANSPORT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:53:38 2025
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

(aluSARConfs,
 aluSARMIBModules,
 aluSARNotifyPrefix,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARNotifyPrefix",
    "aluSARObjs")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(svcBaseInfoEntry,
 svcId) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcBaseInfoEntry",
    "svcId")

(TDSCPName,
 TFCName,
 TItemDescription,
 TLNamedItemOrEmpty,
 TProfile,
 TTcpUdpPort,
 TmnxActionType,
 TmnxAdminState,
 TmnxCustId,
 TmnxEnabledDisabled,
 TmnxOperState,
 TmnxPortID,
 TmnxServId) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TDSCPName",
    "TFCName",
    "TItemDescription",
    "TLNamedItemOrEmpty",
    "TProfile",
    "TTcpUdpPort",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxCustId",
    "TmnxEnabledDisabled",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId")


# MODULE-IDENTITY

aluIpTransportMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 20)
)
if mibBuilder.loadTexts:
    aluIpTransportMIBModule.setRevisions(
        ("2016-02-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluIpTransportRemHostId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class AluIpTransportRemHostSessState(TextualConvention, Integer32):
    status = "current"
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
        *(("invalid", 0),
          ("ready", 1),
          ("connecting", 2),
          ("connected", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AluIpTransportConformance_ObjectIdentity = ObjectIdentity
aluIpTransportConformance = _AluIpTransportConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 22)
)
_AluIpTransportCompliances_ObjectIdentity = ObjectIdentity
aluIpTransportCompliances = _AluIpTransportCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 22, 1)
)
_AluIpTransportGroups_ObjectIdentity = ObjectIdentity
aluIpTransportGroups = _AluIpTransportGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 22, 2)
)
_AluIpTransportV8v0Groups_ObjectIdentity = ObjectIdentity
aluIpTransportV8v0Groups = _AluIpTransportV8v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 22, 2, 1)
)
_AluIpTransportObjs_ObjectIdentity = ObjectIdentity
aluIpTransportObjs = _AluIpTransportObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22)
)
_AluIpTransportConfigTimestamps_ObjectIdentity = ObjectIdentity
aluIpTransportConfigTimestamps = _AluIpTransportConfigTimestamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 1)
)
_AluIpTransportTableLastChanged_Type = TimeStamp
_AluIpTransportTableLastChanged_Object = MibScalar
aluIpTransportTableLastChanged = _AluIpTransportTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 1, 1),
    _AluIpTransportTableLastChanged_Type()
)
aluIpTransportTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportTableLastChanged.setStatus("current")
_AluIpTransportRemHostTblLastChgd_Type = TimeStamp
_AluIpTransportRemHostTblLastChgd_Object = MibScalar
aluIpTransportRemHostTblLastChgd = _AluIpTransportRemHostTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 1, 2),
    _AluIpTransportRemHostTblLastChgd_Type()
)
aluIpTransportRemHostTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostTblLastChgd.setStatus("current")
_AluIpTransportConfigurations_ObjectIdentity = ObjectIdentity
aluIpTransportConfigurations = _AluIpTransportConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2)
)
_AluIpTransportTable_Object = MibTable
aluIpTransportTable = _AluIpTransportTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1)
)
if mibBuilder.loadTexts:
    aluIpTransportTable.setStatus("current")
_AluIpTransportEntry_Object = MibTableRow
aluIpTransportEntry = _AluIpTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1)
)
aluIpTransportEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALU-IP-TRANSPORT-MIB", "aluIpTransportPortId"),
)
if mibBuilder.loadTexts:
    aluIpTransportEntry.setStatus("current")
_AluIpTransportPortId_Type = TmnxPortID
_AluIpTransportPortId_Object = MibTableColumn
aluIpTransportPortId = _AluIpTransportPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 1),
    _AluIpTransportPortId_Type()
)
aluIpTransportPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluIpTransportPortId.setStatus("current")
_AluIpTransportLastMgmtChange_Type = TimeStamp
_AluIpTransportLastMgmtChange_Object = MibTableColumn
aluIpTransportLastMgmtChange = _AluIpTransportLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 2),
    _AluIpTransportLastMgmtChange_Type()
)
aluIpTransportLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportLastMgmtChange.setStatus("current")
_AluIpTransportRowStatus_Type = RowStatus
_AluIpTransportRowStatus_Object = MibTableColumn
aluIpTransportRowStatus = _AluIpTransportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 3),
    _AluIpTransportRowStatus_Type()
)
aluIpTransportRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportRowStatus.setStatus("current")


class _AluIpTransportAdminState_Type(TmnxAdminState):
    """Custom type aluIpTransportAdminState based on TmnxAdminState"""
    defaultValue = 3


_AluIpTransportAdminState_Type.__name__ = "TmnxAdminState"
_AluIpTransportAdminState_Object = MibTableColumn
aluIpTransportAdminState = _AluIpTransportAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 4),
    _AluIpTransportAdminState_Type()
)
aluIpTransportAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportAdminState.setStatus("current")


class _AluIpTransportDescription_Type(TItemDescription):
    """Custom type aluIpTransportDescription based on TItemDescription"""
    defaultHexValue = ""


_AluIpTransportDescription_Type.__name__ = "TItemDescription"
_AluIpTransportDescription_Object = MibTableColumn
aluIpTransportDescription = _AluIpTransportDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 5),
    _AluIpTransportDescription_Type()
)
aluIpTransportDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportDescription.setStatus("current")


class _AluIpTransportTcpConnMaxRetries_Type(Unsigned32):
    """Custom type aluIpTransportTcpConnMaxRetries based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AluIpTransportTcpConnMaxRetries_Type.__name__ = "Unsigned32"
_AluIpTransportTcpConnMaxRetries_Object = MibTableColumn
aluIpTransportTcpConnMaxRetries = _AluIpTransportTcpConnMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 6),
    _AluIpTransportTcpConnMaxRetries_Type()
)
aluIpTransportTcpConnMaxRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportTcpConnMaxRetries.setStatus("current")


class _AluIpTransportTcpConnRetryIntvl_Type(Unsigned32):
    """Custom type aluIpTransportTcpConnRetryIntvl based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_AluIpTransportTcpConnRetryIntvl_Type.__name__ = "Unsigned32"
_AluIpTransportTcpConnRetryIntvl_Object = MibTableColumn
aluIpTransportTcpConnRetryIntvl = _AluIpTransportTcpConnRetryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 7),
    _AluIpTransportTcpConnRetryIntvl_Type()
)
aluIpTransportTcpConnRetryIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportTcpConnRetryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    aluIpTransportTcpConnRetryIntvl.setUnits("seconds")


class _AluIpTransportTcpConnInactTimout_Type(Unsigned32):
    """Custom type aluIpTransportTcpConnInactTimout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluIpTransportTcpConnInactTimout_Type.__name__ = "Unsigned32"
_AluIpTransportTcpConnInactTimout_Object = MibTableColumn
aluIpTransportTcpConnInactTimout = _AluIpTransportTcpConnInactTimout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 8),
    _AluIpTransportTcpConnInactTimout_Type()
)
aluIpTransportTcpConnInactTimout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportTcpConnInactTimout.setStatus("current")
if mibBuilder.loadTexts:
    aluIpTransportTcpConnInactTimout.setUnits("seconds")


class _AluIpTransportFilterUnknownHost_Type(TmnxEnabledDisabled):
    """Custom type aluIpTransportFilterUnknownHost based on TmnxEnabledDisabled"""
    defaultValue = 2


_AluIpTransportFilterUnknownHost_Type.__name__ = "TmnxEnabledDisabled"
_AluIpTransportFilterUnknownHost_Object = MibTableColumn
aluIpTransportFilterUnknownHost = _AluIpTransportFilterUnknownHost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 9),
    _AluIpTransportFilterUnknownHost_Type()
)
aluIpTransportFilterUnknownHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportFilterUnknownHost.setStatus("current")


class _AluIpTransportDscpName_Type(TDSCPName):
    """Custom type aluIpTransportDscpName based on TDSCPName"""
    defaultValue = OctetString("ef")


_AluIpTransportDscpName_Type.__name__ = "TDSCPName"
_AluIpTransportDscpName_Object = MibTableColumn
aluIpTransportDscpName = _AluIpTransportDscpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 10),
    _AluIpTransportDscpName_Type()
)
aluIpTransportDscpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportDscpName.setStatus("current")


class _AluIpTransportFcName_Type(TFCName):
    """Custom type aluIpTransportFcName based on TFCName"""
    defaultValue = OctetString("ef")


_AluIpTransportFcName_Type.__name__ = "TFCName"
_AluIpTransportFcName_Object = MibTableColumn
aluIpTransportFcName = _AluIpTransportFcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 11),
    _AluIpTransportFcName_Type()
)
aluIpTransportFcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportFcName.setStatus("current")


class _AluIpTransportProfile_Type(TProfile):
    """Custom type aluIpTransportProfile based on TProfile"""
    defaultValue = 1


_AluIpTransportProfile_Type.__name__ = "TProfile"
_AluIpTransportProfile_Object = MibTableColumn
aluIpTransportProfile = _AluIpTransportProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 12),
    _AluIpTransportProfile_Type()
)
aluIpTransportProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportProfile.setStatus("current")


class _AluIpTransportLocHostIpAddrType_Type(InetAddressType):
    """Custom type aluIpTransportLocHostIpAddrType based on InetAddressType"""
    defaultValue = 0

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1))
    )


_AluIpTransportLocHostIpAddrType_Type.__name__ = "InetAddressType"
_AluIpTransportLocHostIpAddrType_Object = MibTableColumn
aluIpTransportLocHostIpAddrType = _AluIpTransportLocHostIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 13),
    _AluIpTransportLocHostIpAddrType_Type()
)
aluIpTransportLocHostIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportLocHostIpAddrType.setStatus("current")


class _AluIpTransportLocHostIpAddr_Type(InetAddress):
    """Custom type aluIpTransportLocHostIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AluIpTransportLocHostIpAddr_Type.__name__ = "InetAddress"
_AluIpTransportLocHostIpAddr_Object = MibTableColumn
aluIpTransportLocHostIpAddr = _AluIpTransportLocHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 14),
    _AluIpTransportLocHostIpAddr_Type()
)
aluIpTransportLocHostIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportLocHostIpAddr.setStatus("current")


class _AluIpTransportLocHostPortNum_Type(TTcpUdpPort):
    """Custom type aluIpTransportLocHostPortNum based on TTcpUdpPort"""
    defaultValue = 0

    subtypeSpec = TTcpUdpPort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1026, 49150),
    )


_AluIpTransportLocHostPortNum_Type.__name__ = "TTcpUdpPort"
_AluIpTransportLocHostPortNum_Object = MibTableColumn
aluIpTransportLocHostPortNum = _AluIpTransportLocHostPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 15),
    _AluIpTransportLocHostPortNum_Type()
)
aluIpTransportLocHostPortNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportLocHostPortNum.setStatus("current")


class _AluIpTransportLocHostIpProtocol_Type(Integer32):
    """Custom type aluIpTransportLocHostIpProtocol based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("unset", -1),
          ("tcp", 6),
          ("udp", 17))
    )


_AluIpTransportLocHostIpProtocol_Type.__name__ = "Integer32"
_AluIpTransportLocHostIpProtocol_Object = MibTableColumn
aluIpTransportLocHostIpProtocol = _AluIpTransportLocHostIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 16),
    _AluIpTransportLocHostIpProtocol_Type()
)
aluIpTransportLocHostIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportLocHostIpProtocol.setStatus("current")
_AluIpTransportNumRemHosts_Type = Unsigned32
_AluIpTransportNumRemHosts_Object = MibTableColumn
aluIpTransportNumRemHosts = _AluIpTransportNumRemHosts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 17),
    _AluIpTransportNumRemHosts_Type()
)
aluIpTransportNumRemHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportNumRemHosts.setStatus("current")
_AluIpTransportOperState_Type = TmnxOperState
_AluIpTransportOperState_Object = MibTableColumn
aluIpTransportOperState = _AluIpTransportOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 18),
    _AluIpTransportOperState_Type()
)
aluIpTransportOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportOperState.setStatus("current")


class _AluIpTransportOperFlags_Type(Bits):
    """Custom type aluIpTransportOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("iptAdminDown", 0),
          ("svcAdminDown", 1),
          ("portOperDown", 2),
          ("noIfAddress", 3),
          ("ifOperDown", 4),
          ("portNumInUse", 5),
          ("portNumReserved", 6))
    )

_AluIpTransportOperFlags_Type.__name__ = "Bits"
_AluIpTransportOperFlags_Object = MibTableColumn
aluIpTransportOperFlags = _AluIpTransportOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 19),
    _AluIpTransportOperFlags_Type()
)
aluIpTransportOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportOperFlags.setStatus("current")
_AluIpTransportLastOperChange_Type = TimeStamp
_AluIpTransportLastOperChange_Object = MibTableColumn
aluIpTransportLastOperChange = _AluIpTransportLastOperChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 1, 1, 20),
    _AluIpTransportLastOperChange_Type()
)
aluIpTransportLastOperChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportLastOperChange.setStatus("current")
_AluIpTransportRemHostTable_Object = MibTable
aluIpTransportRemHostTable = _AluIpTransportRemHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 2)
)
if mibBuilder.loadTexts:
    aluIpTransportRemHostTable.setStatus("current")
_AluIpTransportRemHostEntry_Object = MibTableRow
aluIpTransportRemHostEntry = _AluIpTransportRemHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 2, 1)
)
aluIpTransportRemHostEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALU-IP-TRANSPORT-MIB", "aluIpTransportPortId"),
    (0, "ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostId"),
)
if mibBuilder.loadTexts:
    aluIpTransportRemHostEntry.setStatus("current")
_AluIpTransportRemHostId_Type = AluIpTransportRemHostId
_AluIpTransportRemHostId_Object = MibTableColumn
aluIpTransportRemHostId = _AluIpTransportRemHostId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 2, 1, 1),
    _AluIpTransportRemHostId_Type()
)
aluIpTransportRemHostId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluIpTransportRemHostId.setStatus("current")
_AluIpTransportRemHostLastChanged_Type = TimeStamp
_AluIpTransportRemHostLastChanged_Object = MibTableColumn
aluIpTransportRemHostLastChanged = _AluIpTransportRemHostLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 2, 1, 2),
    _AluIpTransportRemHostLastChanged_Type()
)
aluIpTransportRemHostLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostLastChanged.setStatus("current")
_AluIpTransportRemHostRowStatus_Type = RowStatus
_AluIpTransportRemHostRowStatus_Object = MibTableColumn
aluIpTransportRemHostRowStatus = _AluIpTransportRemHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 2, 1, 3),
    _AluIpTransportRemHostRowStatus_Type()
)
aluIpTransportRemHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportRemHostRowStatus.setStatus("current")


class _AluIpTransportRemHostName_Type(TLNamedItemOrEmpty):
    """Custom type aluIpTransportRemHostName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_AluIpTransportRemHostName_Type.__name__ = "TLNamedItemOrEmpty"
_AluIpTransportRemHostName_Object = MibTableColumn
aluIpTransportRemHostName = _AluIpTransportRemHostName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 2, 1, 4),
    _AluIpTransportRemHostName_Type()
)
aluIpTransportRemHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportRemHostName.setStatus("current")


class _AluIpTransportRemHostDescription_Type(TItemDescription):
    """Custom type aluIpTransportRemHostDescription based on TItemDescription"""
    defaultHexValue = ""


_AluIpTransportRemHostDescription_Type.__name__ = "TItemDescription"
_AluIpTransportRemHostDescription_Object = MibTableColumn
aluIpTransportRemHostDescription = _AluIpTransportRemHostDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 2, 1, 5),
    _AluIpTransportRemHostDescription_Type()
)
aluIpTransportRemHostDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportRemHostDescription.setStatus("current")
_AluIpTransportRemHostIpAddrType_Type = InetAddressType
_AluIpTransportRemHostIpAddrType_Object = MibTableColumn
aluIpTransportRemHostIpAddrType = _AluIpTransportRemHostIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 2, 1, 6),
    _AluIpTransportRemHostIpAddrType_Type()
)
aluIpTransportRemHostIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportRemHostIpAddrType.setStatus("current")


class _AluIpTransportRemHostIpAddr_Type(InetAddress):
    """Custom type aluIpTransportRemHostIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AluIpTransportRemHostIpAddr_Type.__name__ = "InetAddress"
_AluIpTransportRemHostIpAddr_Object = MibTableColumn
aluIpTransportRemHostIpAddr = _AluIpTransportRemHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 2, 1, 7),
    _AluIpTransportRemHostIpAddr_Type()
)
aluIpTransportRemHostIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportRemHostIpAddr.setStatus("current")


class _AluIpTransportRemHostPortNum_Type(TTcpUdpPort):
    """Custom type aluIpTransportRemHostPortNum based on TTcpUdpPort"""
    subtypeSpec = TTcpUdpPort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluIpTransportRemHostPortNum_Type.__name__ = "TTcpUdpPort"
_AluIpTransportRemHostPortNum_Object = MibTableColumn
aluIpTransportRemHostPortNum = _AluIpTransportRemHostPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 2, 1, 8),
    _AluIpTransportRemHostPortNum_Type()
)
aluIpTransportRemHostPortNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportRemHostPortNum.setStatus("current")
_AluIpTransportRemHostSessState_Type = AluIpTransportRemHostSessState
_AluIpTransportRemHostSessState_Object = MibTableColumn
aluIpTransportRemHostSessState = _AluIpTransportRemHostSessState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 2, 1, 9),
    _AluIpTransportRemHostSessState_Type()
)
aluIpTransportRemHostSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostSessState.setStatus("current")
_AluIpTransportRemHostSessUpTime_Type = Unsigned32
_AluIpTransportRemHostSessUpTime_Object = MibTableColumn
aluIpTransportRemHostSessUpTime = _AluIpTransportRemHostSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 2, 1, 10),
    _AluIpTransportRemHostSessUpTime_Type()
)
aluIpTransportRemHostSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostSessUpTime.setStatus("current")
if mibBuilder.loadTexts:
    aluIpTransportRemHostSessUpTime.setUnits("seconds")


class _AluIpTransportRemHostLastConnect_Type(DisplayString):
    """Custom type aluIpTransportRemHostLastConnect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AluIpTransportRemHostLastConnect_Type.__name__ = "DisplayString"
_AluIpTransportRemHostLastConnect_Object = MibTableColumn
aluIpTransportRemHostLastConnect = _AluIpTransportRemHostLastConnect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 2, 1, 11),
    _AluIpTransportRemHostLastConnect_Type()
)
aluIpTransportRemHostLastConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostLastConnect.setStatus("current")


class _AluIpTransportRemHostCheckTcp_Type(TmnxActionType):
    """Custom type aluIpTransportRemHostCheckTcp based on TmnxActionType"""
    defaultValue = 2


_AluIpTransportRemHostCheckTcp_Type.__name__ = "TmnxActionType"
_AluIpTransportRemHostCheckTcp_Object = MibTableColumn
aluIpTransportRemHostCheckTcp = _AluIpTransportRemHostCheckTcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 2, 1, 12),
    _AluIpTransportRemHostCheckTcp_Type()
)
aluIpTransportRemHostCheckTcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluIpTransportRemHostCheckTcp.setStatus("current")


class _AluIpTransportRemHostCheckTcpRes_Type(Integer32):
    """Custom type aluIpTransportRemHostCheckTcpRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("pass", 2),
          ("fail", 3))
    )


_AluIpTransportRemHostCheckTcpRes_Type.__name__ = "Integer32"
_AluIpTransportRemHostCheckTcpRes_Object = MibTableColumn
aluIpTransportRemHostCheckTcpRes = _AluIpTransportRemHostCheckTcpRes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 2, 1, 13),
    _AluIpTransportRemHostCheckTcpRes_Type()
)
aluIpTransportRemHostCheckTcpRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostCheckTcpRes.setStatus("current")


class _AluIpTransportRemHostCheckTcpInf_Type(DisplayString):
    """Custom type aluIpTransportRemHostCheckTcpInf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AluIpTransportRemHostCheckTcpInf_Type.__name__ = "DisplayString"
_AluIpTransportRemHostCheckTcpInf_Object = MibTableColumn
aluIpTransportRemHostCheckTcpInf = _AluIpTransportRemHostCheckTcpInf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 2, 1, 14),
    _AluIpTransportRemHostCheckTcpInf_Type()
)
aluIpTransportRemHostCheckTcpInf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostCheckTcpInf.setStatus("current")
_AluIpTransportSvcBaseExtTable_Object = MibTable
aluIpTransportSvcBaseExtTable = _AluIpTransportSvcBaseExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 3)
)
if mibBuilder.loadTexts:
    aluIpTransportSvcBaseExtTable.setStatus("current")
_AluIpTransportSvcBaseExtEntry_Object = MibTableRow
aluIpTransportSvcBaseExtEntry = _AluIpTransportSvcBaseExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 3, 1)
)
if mibBuilder.loadTexts:
    aluIpTransportSvcBaseExtEntry.setStatus("current")
_AluIpTransportSvcBaseExtNumIpts_Type = Unsigned32
_AluIpTransportSvcBaseExtNumIpts_Object = MibTableColumn
aluIpTransportSvcBaseExtNumIpts = _AluIpTransportSvcBaseExtNumIpts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 2, 3, 1, 1),
    _AluIpTransportSvcBaseExtNumIpts_Type()
)
aluIpTransportSvcBaseExtNumIpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportSvcBaseExtNumIpts.setStatus("current")
_AluIpTransportNameObjects_ObjectIdentity = ObjectIdentity
aluIpTransportNameObjects = _AluIpTransportNameObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 3)
)
_AluIpTransportRemHostNameTable_Object = MibTable
aluIpTransportRemHostNameTable = _AluIpTransportRemHostNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 3, 1)
)
if mibBuilder.loadTexts:
    aluIpTransportRemHostNameTable.setStatus("current")
_AluIpTransportRemHostNameEntry_Object = MibTableRow
aluIpTransportRemHostNameEntry = _AluIpTransportRemHostNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 3, 1, 1)
)
aluIpTransportRemHostNameEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALU-IP-TRANSPORT-MIB", "aluIpTransportPortId"),
    (0, "ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostName"),
)
if mibBuilder.loadTexts:
    aluIpTransportRemHostNameEntry.setStatus("current")
_AluIpTransportRemHostNameId_Type = AluIpTransportRemHostId
_AluIpTransportRemHostNameId_Object = MibTableColumn
aluIpTransportRemHostNameId = _AluIpTransportRemHostNameId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 3, 1, 1, 1),
    _AluIpTransportRemHostNameId_Type()
)
aluIpTransportRemHostNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostNameId.setStatus("current")
_AluIpTransportStatus_ObjectIdentity = ObjectIdentity
aluIpTransportStatus = _AluIpTransportStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 4)
)
_AluIpTransportStatsObjects_ObjectIdentity = ObjectIdentity
aluIpTransportStatsObjects = _AluIpTransportStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5)
)
_AluIpTransportStatsTable_Object = MibTable
aluIpTransportStatsTable = _AluIpTransportStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1)
)
if mibBuilder.loadTexts:
    aluIpTransportStatsTable.setStatus("current")
_AluIpTransportStatsEntry_Object = MibTableRow
aluIpTransportStatsEntry = _AluIpTransportStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1)
)
aluIpTransportStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALU-IP-TRANSPORT-MIB", "aluIpTransportPortId"),
)
if mibBuilder.loadTexts:
    aluIpTransportStatsEntry.setStatus("current")
_AluIpTransportKnwRemPktsSent_Type = Counter64
_AluIpTransportKnwRemPktsSent_Object = MibTableColumn
aluIpTransportKnwRemPktsSent = _AluIpTransportKnwRemPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 1),
    _AluIpTransportKnwRemPktsSent_Type()
)
aluIpTransportKnwRemPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportKnwRemPktsSent.setStatus("current")
_AluIpTransportKnwRemCharsSent_Type = Counter64
_AluIpTransportKnwRemCharsSent_Object = MibTableColumn
aluIpTransportKnwRemCharsSent = _AluIpTransportKnwRemCharsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 2),
    _AluIpTransportKnwRemCharsSent_Type()
)
aluIpTransportKnwRemCharsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportKnwRemCharsSent.setStatus("current")
_AluIpTransportKnwRemPktsRcvd_Type = Counter64
_AluIpTransportKnwRemPktsRcvd_Object = MibTableColumn
aluIpTransportKnwRemPktsRcvd = _AluIpTransportKnwRemPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 3),
    _AluIpTransportKnwRemPktsRcvd_Type()
)
aluIpTransportKnwRemPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportKnwRemPktsRcvd.setStatus("current")
_AluIpTransportKnwRemCharsRcvd_Type = Counter64
_AluIpTransportKnwRemCharsRcvd_Object = MibTableColumn
aluIpTransportKnwRemCharsRcvd = _AluIpTransportKnwRemCharsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 4),
    _AluIpTransportKnwRemCharsRcvd_Type()
)
aluIpTransportKnwRemCharsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportKnwRemCharsRcvd.setStatus("current")
_AluIpTransportKnwRemConnsTo_Type = Counter32
_AluIpTransportKnwRemConnsTo_Object = MibTableColumn
aluIpTransportKnwRemConnsTo = _AluIpTransportKnwRemConnsTo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 5),
    _AluIpTransportKnwRemConnsTo_Type()
)
aluIpTransportKnwRemConnsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportKnwRemConnsTo.setStatus("current")
_AluIpTransportKnwRemConnsFrom_Type = Counter32
_AluIpTransportKnwRemConnsFrom_Object = MibTableColumn
aluIpTransportKnwRemConnsFrom = _AluIpTransportKnwRemConnsFrom_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 6),
    _AluIpTransportKnwRemConnsFrom_Type()
)
aluIpTransportKnwRemConnsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportKnwRemConnsFrom.setStatus("current")
_AluIpTransportKnwRemConnRetries_Type = Counter32
_AluIpTransportKnwRemConnRetries_Object = MibTableColumn
aluIpTransportKnwRemConnRetries = _AluIpTransportKnwRemConnRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 7),
    _AluIpTransportKnwRemConnRetries_Type()
)
aluIpTransportKnwRemConnRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportKnwRemConnRetries.setStatus("current")
_AluIpTransportKnwRemConnFails_Type = Counter32
_AluIpTransportKnwRemConnFails_Object = MibTableColumn
aluIpTransportKnwRemConnFails = _AluIpTransportKnwRemConnFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 8),
    _AluIpTransportKnwRemConnFails_Type()
)
aluIpTransportKnwRemConnFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportKnwRemConnFails.setStatus("current")
_AluIpTransportKnwRemCurrConns_Type = Unsigned32
_AluIpTransportKnwRemCurrConns_Object = MibTableColumn
aluIpTransportKnwRemCurrConns = _AluIpTransportKnwRemCurrConns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 9),
    _AluIpTransportKnwRemCurrConns_Type()
)
aluIpTransportKnwRemCurrConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportKnwRemCurrConns.setStatus("current")
_AluIpTransportUnkRemPktsSent_Type = Counter64
_AluIpTransportUnkRemPktsSent_Object = MibTableColumn
aluIpTransportUnkRemPktsSent = _AluIpTransportUnkRemPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 10),
    _AluIpTransportUnkRemPktsSent_Type()
)
aluIpTransportUnkRemPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportUnkRemPktsSent.setStatus("current")
_AluIpTransportUnkRemCharsSent_Type = Counter64
_AluIpTransportUnkRemCharsSent_Object = MibTableColumn
aluIpTransportUnkRemCharsSent = _AluIpTransportUnkRemCharsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 11),
    _AluIpTransportUnkRemCharsSent_Type()
)
aluIpTransportUnkRemCharsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportUnkRemCharsSent.setStatus("current")
_AluIpTransportUnkRemPktsRcvd_Type = Counter64
_AluIpTransportUnkRemPktsRcvd_Object = MibTableColumn
aluIpTransportUnkRemPktsRcvd = _AluIpTransportUnkRemPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 12),
    _AluIpTransportUnkRemPktsRcvd_Type()
)
aluIpTransportUnkRemPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportUnkRemPktsRcvd.setStatus("current")
_AluIpTransportUnkRemCharsRcvd_Type = Counter64
_AluIpTransportUnkRemCharsRcvd_Object = MibTableColumn
aluIpTransportUnkRemCharsRcvd = _AluIpTransportUnkRemCharsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 13),
    _AluIpTransportUnkRemCharsRcvd_Type()
)
aluIpTransportUnkRemCharsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportUnkRemCharsRcvd.setStatus("current")
_AluIpTransportUnkRemSuccConnsFrm_Type = Counter32
_AluIpTransportUnkRemSuccConnsFrm_Object = MibTableColumn
aluIpTransportUnkRemSuccConnsFrm = _AluIpTransportUnkRemSuccConnsFrm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 14),
    _AluIpTransportUnkRemSuccConnsFrm_Type()
)
aluIpTransportUnkRemSuccConnsFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportUnkRemSuccConnsFrm.setStatus("current")
_AluIpTransportUnkRemRejectsFiltr_Type = Counter32
_AluIpTransportUnkRemRejectsFiltr_Object = MibTableColumn
aluIpTransportUnkRemRejectsFiltr = _AluIpTransportUnkRemRejectsFiltr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 15),
    _AluIpTransportUnkRemRejectsFiltr_Type()
)
aluIpTransportUnkRemRejectsFiltr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportUnkRemRejectsFiltr.setStatus("current")
_AluIpTransportUnkRemRejectsResrc_Type = Counter32
_AluIpTransportUnkRemRejectsResrc_Object = MibTableColumn
aluIpTransportUnkRemRejectsResrc = _AluIpTransportUnkRemRejectsResrc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 16),
    _AluIpTransportUnkRemRejectsResrc_Type()
)
aluIpTransportUnkRemRejectsResrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportUnkRemRejectsResrc.setStatus("current")
_AluIpTransportUnkRemInactTimouts_Type = Counter32
_AluIpTransportUnkRemInactTimouts_Object = MibTableColumn
aluIpTransportUnkRemInactTimouts = _AluIpTransportUnkRemInactTimouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 17),
    _AluIpTransportUnkRemInactTimouts_Type()
)
aluIpTransportUnkRemInactTimouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportUnkRemInactTimouts.setStatus("current")
_AluIpTransportUnkRemLastIpAddrTy_Type = InetAddressType
_AluIpTransportUnkRemLastIpAddrTy_Object = MibTableColumn
aluIpTransportUnkRemLastIpAddrTy = _AluIpTransportUnkRemLastIpAddrTy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 18),
    _AluIpTransportUnkRemLastIpAddrTy_Type()
)
aluIpTransportUnkRemLastIpAddrTy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportUnkRemLastIpAddrTy.setStatus("current")


class _AluIpTransportUnkRemLastIpAddr_Type(InetAddress):
    """Custom type aluIpTransportUnkRemLastIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AluIpTransportUnkRemLastIpAddr_Type.__name__ = "InetAddress"
_AluIpTransportUnkRemLastIpAddr_Object = MibTableColumn
aluIpTransportUnkRemLastIpAddr = _AluIpTransportUnkRemLastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 19),
    _AluIpTransportUnkRemLastIpAddr_Type()
)
aluIpTransportUnkRemLastIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportUnkRemLastIpAddr.setStatus("current")


class _AluIpTransportUnkRemLastPortNum_Type(TTcpUdpPort):
    """Custom type aluIpTransportUnkRemLastPortNum based on TTcpUdpPort"""
    subtypeSpec = TTcpUdpPort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_AluIpTransportUnkRemLastPortNum_Type.__name__ = "TTcpUdpPort"
_AluIpTransportUnkRemLastPortNum_Object = MibTableColumn
aluIpTransportUnkRemLastPortNum = _AluIpTransportUnkRemLastPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 20),
    _AluIpTransportUnkRemLastPortNum_Type()
)
aluIpTransportUnkRemLastPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportUnkRemLastPortNum.setStatus("current")
_AluIpTransportUnkRemCurrConns_Type = Unsigned32
_AluIpTransportUnkRemCurrConns_Object = MibTableColumn
aluIpTransportUnkRemCurrConns = _AluIpTransportUnkRemCurrConns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 21),
    _AluIpTransportUnkRemCurrConns_Type()
)
aluIpTransportUnkRemCurrConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportUnkRemCurrConns.setStatus("current")
_AluIpTransportPktsDropNoRemHost_Type = Counter64
_AluIpTransportPktsDropNoRemHost_Object = MibTableColumn
aluIpTransportPktsDropNoRemHost = _AluIpTransportPktsDropNoRemHost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 1, 1, 22),
    _AluIpTransportPktsDropNoRemHost_Type()
)
aluIpTransportPktsDropNoRemHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportPktsDropNoRemHost.setStatus("current")
_AluIpTransportRemHostStatsTable_Object = MibTable
aluIpTransportRemHostStatsTable = _AluIpTransportRemHostStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 2)
)
if mibBuilder.loadTexts:
    aluIpTransportRemHostStatsTable.setStatus("current")
_AluIpTransportRemHostStatsEntry_Object = MibTableRow
aluIpTransportRemHostStatsEntry = _AluIpTransportRemHostStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 2, 1)
)
aluIpTransportRemHostStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALU-IP-TRANSPORT-MIB", "aluIpTransportPortId"),
    (0, "ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostId"),
)
if mibBuilder.loadTexts:
    aluIpTransportRemHostStatsEntry.setStatus("current")
_AluIpTransportRemHostPktsSent_Type = Counter64
_AluIpTransportRemHostPktsSent_Object = MibTableColumn
aluIpTransportRemHostPktsSent = _AluIpTransportRemHostPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 2, 1, 1),
    _AluIpTransportRemHostPktsSent_Type()
)
aluIpTransportRemHostPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostPktsSent.setStatus("current")
_AluIpTransportRemHostCharsSent_Type = Counter64
_AluIpTransportRemHostCharsSent_Object = MibTableColumn
aluIpTransportRemHostCharsSent = _AluIpTransportRemHostCharsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 2, 1, 2),
    _AluIpTransportRemHostCharsSent_Type()
)
aluIpTransportRemHostCharsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostCharsSent.setStatus("current")
_AluIpTransportRemHostPktsDrop_Type = Counter64
_AluIpTransportRemHostPktsDrop_Object = MibTableColumn
aluIpTransportRemHostPktsDrop = _AluIpTransportRemHostPktsDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 2, 1, 3),
    _AluIpTransportRemHostPktsDrop_Type()
)
aluIpTransportRemHostPktsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostPktsDrop.setStatus("current")
_AluIpTransportRemHostCharsDrop_Type = Counter64
_AluIpTransportRemHostCharsDrop_Object = MibTableColumn
aluIpTransportRemHostCharsDrop = _AluIpTransportRemHostCharsDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 2, 1, 4),
    _AluIpTransportRemHostCharsDrop_Type()
)
aluIpTransportRemHostCharsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostCharsDrop.setStatus("current")
_AluIpTransportRemHostPktsRcvd_Type = Counter64
_AluIpTransportRemHostPktsRcvd_Object = MibTableColumn
aluIpTransportRemHostPktsRcvd = _AluIpTransportRemHostPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 2, 1, 5),
    _AluIpTransportRemHostPktsRcvd_Type()
)
aluIpTransportRemHostPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostPktsRcvd.setStatus("current")
_AluIpTransportRemHostCharsRcvd_Type = Counter64
_AluIpTransportRemHostCharsRcvd_Object = MibTableColumn
aluIpTransportRemHostCharsRcvd = _AluIpTransportRemHostCharsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 2, 1, 6),
    _AluIpTransportRemHostCharsRcvd_Type()
)
aluIpTransportRemHostCharsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostCharsRcvd.setStatus("current")
_AluIpTransportRemHostConnsTo_Type = Counter32
_AluIpTransportRemHostConnsTo_Object = MibTableColumn
aluIpTransportRemHostConnsTo = _AluIpTransportRemHostConnsTo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 2, 1, 7),
    _AluIpTransportRemHostConnsTo_Type()
)
aluIpTransportRemHostConnsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostConnsTo.setStatus("current")
_AluIpTransportRemHostConnsFrom_Type = Counter32
_AluIpTransportRemHostConnsFrom_Object = MibTableColumn
aluIpTransportRemHostConnsFrom = _AluIpTransportRemHostConnsFrom_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 2, 1, 8),
    _AluIpTransportRemHostConnsFrom_Type()
)
aluIpTransportRemHostConnsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostConnsFrom.setStatus("current")
_AluIpTransportRemHostConnRetries_Type = Counter32
_AluIpTransportRemHostConnRetries_Object = MibTableColumn
aluIpTransportRemHostConnRetries = _AluIpTransportRemHostConnRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 2, 1, 9),
    _AluIpTransportRemHostConnRetries_Type()
)
aluIpTransportRemHostConnRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostConnRetries.setStatus("current")
_AluIpTransportRemHostConnFails_Type = Counter32
_AluIpTransportRemHostConnFails_Object = MibTableColumn
aluIpTransportRemHostConnFails = _AluIpTransportRemHostConnFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 2, 1, 10),
    _AluIpTransportRemHostConnFails_Type()
)
aluIpTransportRemHostConnFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostConnFails.setStatus("current")
_AluIpTransportRemHostConnsCloFar_Type = Counter32
_AluIpTransportRemHostConnsCloFar_Object = MibTableColumn
aluIpTransportRemHostConnsCloFar = _AluIpTransportRemHostConnsCloFar_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 2, 1, 11),
    _AluIpTransportRemHostConnsCloFar_Type()
)
aluIpTransportRemHostConnsCloFar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostConnsCloFar.setStatus("current")
_AluIpTransportRemHostInactTmouts_Type = Counter32
_AluIpTransportRemHostInactTmouts_Object = MibTableColumn
aluIpTransportRemHostInactTmouts = _AluIpTransportRemHostInactTmouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 2, 1, 12),
    _AluIpTransportRemHostInactTmouts_Type()
)
aluIpTransportRemHostInactTmouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportRemHostInactTmouts.setStatus("current")
_AluIpTransportURemHostStatsTable_Object = MibTable
aluIpTransportURemHostStatsTable = _AluIpTransportURemHostStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 3)
)
if mibBuilder.loadTexts:
    aluIpTransportURemHostStatsTable.setStatus("current")
_AluIpTransportURemHostStatsEntry_Object = MibTableRow
aluIpTransportURemHostStatsEntry = _AluIpTransportURemHostStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 3, 1)
)
aluIpTransportURemHostStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALU-IP-TRANSPORT-MIB", "aluIpTransportPortId"),
    (0, "ALU-IP-TRANSPORT-MIB", "aluIpTransportURemHostIpAddrType"),
    (0, "ALU-IP-TRANSPORT-MIB", "aluIpTransportURemHostIpAddr"),
    (0, "ALU-IP-TRANSPORT-MIB", "aluIpTransportURemHostPortNum"),
)
if mibBuilder.loadTexts:
    aluIpTransportURemHostStatsEntry.setStatus("current")
_AluIpTransportURemHostIpAddrType_Type = InetAddressType
_AluIpTransportURemHostIpAddrType_Object = MibTableColumn
aluIpTransportURemHostIpAddrType = _AluIpTransportURemHostIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 3, 1, 1),
    _AluIpTransportURemHostIpAddrType_Type()
)
aluIpTransportURemHostIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluIpTransportURemHostIpAddrType.setStatus("current")


class _AluIpTransportURemHostIpAddr_Type(InetAddress):
    """Custom type aluIpTransportURemHostIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AluIpTransportURemHostIpAddr_Type.__name__ = "InetAddress"
_AluIpTransportURemHostIpAddr_Object = MibTableColumn
aluIpTransportURemHostIpAddr = _AluIpTransportURemHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 3, 1, 2),
    _AluIpTransportURemHostIpAddr_Type()
)
aluIpTransportURemHostIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluIpTransportURemHostIpAddr.setStatus("current")


class _AluIpTransportURemHostPortNum_Type(TTcpUdpPort):
    """Custom type aluIpTransportURemHostPortNum based on TTcpUdpPort"""
    subtypeSpec = TTcpUdpPort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluIpTransportURemHostPortNum_Type.__name__ = "TTcpUdpPort"
_AluIpTransportURemHostPortNum_Object = MibTableColumn
aluIpTransportURemHostPortNum = _AluIpTransportURemHostPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 3, 1, 3),
    _AluIpTransportURemHostPortNum_Type()
)
aluIpTransportURemHostPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluIpTransportURemHostPortNum.setStatus("current")
_AluIpTransportURemHostPktsSent_Type = Counter64
_AluIpTransportURemHostPktsSent_Object = MibTableColumn
aluIpTransportURemHostPktsSent = _AluIpTransportURemHostPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 3, 1, 4),
    _AluIpTransportURemHostPktsSent_Type()
)
aluIpTransportURemHostPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportURemHostPktsSent.setStatus("current")
_AluIpTransportURemHostCharsSent_Type = Counter64
_AluIpTransportURemHostCharsSent_Object = MibTableColumn
aluIpTransportURemHostCharsSent = _AluIpTransportURemHostCharsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 3, 1, 5),
    _AluIpTransportURemHostCharsSent_Type()
)
aluIpTransportURemHostCharsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportURemHostCharsSent.setStatus("current")
_AluIpTransportURemHostPktsDrop_Type = Counter64
_AluIpTransportURemHostPktsDrop_Object = MibTableColumn
aluIpTransportURemHostPktsDrop = _AluIpTransportURemHostPktsDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 3, 1, 6),
    _AluIpTransportURemHostPktsDrop_Type()
)
aluIpTransportURemHostPktsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportURemHostPktsDrop.setStatus("current")
_AluIpTransportURemHostCharsDrop_Type = Counter64
_AluIpTransportURemHostCharsDrop_Object = MibTableColumn
aluIpTransportURemHostCharsDrop = _AluIpTransportURemHostCharsDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 3, 1, 7),
    _AluIpTransportURemHostCharsDrop_Type()
)
aluIpTransportURemHostCharsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportURemHostCharsDrop.setStatus("current")
_AluIpTransportURemHostPktsRcvd_Type = Counter64
_AluIpTransportURemHostPktsRcvd_Object = MibTableColumn
aluIpTransportURemHostPktsRcvd = _AluIpTransportURemHostPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 3, 1, 8),
    _AluIpTransportURemHostPktsRcvd_Type()
)
aluIpTransportURemHostPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportURemHostPktsRcvd.setStatus("current")
_AluIpTransportURemHostCharsRcvd_Type = Counter64
_AluIpTransportURemHostCharsRcvd_Object = MibTableColumn
aluIpTransportURemHostCharsRcvd = _AluIpTransportURemHostCharsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 3, 1, 9),
    _AluIpTransportURemHostCharsRcvd_Type()
)
aluIpTransportURemHostCharsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportURemHostCharsRcvd.setStatus("current")
_AluIpTransportURemHostSessState_Type = AluIpTransportRemHostSessState
_AluIpTransportURemHostSessState_Object = MibTableColumn
aluIpTransportURemHostSessState = _AluIpTransportURemHostSessState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 3, 1, 10),
    _AluIpTransportURemHostSessState_Type()
)
aluIpTransportURemHostSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportURemHostSessState.setStatus("current")
_AluIpTransportURemHostSessUpTime_Type = Unsigned32
_AluIpTransportURemHostSessUpTime_Object = MibTableColumn
aluIpTransportURemHostSessUpTime = _AluIpTransportURemHostSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 5, 3, 1, 11),
    _AluIpTransportURemHostSessUpTime_Type()
)
aluIpTransportURemHostSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportURemHostSessUpTime.setStatus("current")
if mibBuilder.loadTexts:
    aluIpTransportURemHostSessUpTime.setUnits("seconds")
_AluIpTransportNotifyObjects_ObjectIdentity = ObjectIdentity
aluIpTransportNotifyObjects = _AluIpTransportNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 6)
)
_AluIpTransportNotifyCustId_Type = TmnxCustId
_AluIpTransportNotifyCustId_Object = MibScalar
aluIpTransportNotifyCustId = _AluIpTransportNotifyCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 6, 1),
    _AluIpTransportNotifyCustId_Type()
)
aluIpTransportNotifyCustId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluIpTransportNotifyCustId.setStatus("current")
_AluIpTransportNotifySvcId_Type = TmnxServId
_AluIpTransportNotifySvcId_Object = MibScalar
aluIpTransportNotifySvcId = _AluIpTransportNotifySvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 6, 2),
    _AluIpTransportNotifySvcId_Type()
)
aluIpTransportNotifySvcId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluIpTransportNotifySvcId.setStatus("current")
_AluIpTransportNotifyPortId_Type = TmnxPortID
_AluIpTransportNotifyPortId_Object = MibScalar
aluIpTransportNotifyPortId = _AluIpTransportNotifyPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 22, 6, 3),
    _AluIpTransportNotifyPortId_Type()
)
aluIpTransportNotifyPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluIpTransportNotifyPortId.setStatus("current")
_AluIpTransportNotifyPrefix_ObjectIdentity = ObjectIdentity
aluIpTransportNotifyPrefix = _AluIpTransportNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 18)
)
_AluIpTransportNotifications_ObjectIdentity = ObjectIdentity
aluIpTransportNotifications = _AluIpTransportNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 18, 0)
)
svcBaseInfoEntry.registerAugmentions(
    ("ALU-IP-TRANSPORT-MIB",
     "aluIpTransportSvcBaseExtEntry")
)
aluIpTransportSvcBaseExtEntry.setIndexNames(*svcBaseInfoEntry.getIndexNames())

# Managed Objects groups

aluIpTransportV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 22, 2, 1, 1)
)
aluIpTransportV8v0Group.setObjects(
      *(("ALU-IP-TRANSPORT-MIB", "aluIpTransportTableLastChanged"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportLastMgmtChange"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRowStatus"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportAdminState"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportDescription"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportTcpConnMaxRetries"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportTcpConnRetryIntvl"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportTcpConnInactTimout"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportFilterUnknownHost"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportDscpName"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportFcName"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportProfile"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportLocHostIpAddrType"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportLocHostIpAddr"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportLocHostPortNum"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportLocHostIpProtocol"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportNumRemHosts"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportOperState"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportOperFlags"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportLastOperChange"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostTblLastChgd"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostLastChanged"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostRowStatus"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostName"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostDescription"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostIpAddrType"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostIpAddr"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostPortNum"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportSvcBaseExtNumIpts"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostNameId"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostSessState"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostSessUpTime"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostLastConnect"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostCheckTcp"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostCheckTcpRes"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostCheckTcpInf"))
)
if mibBuilder.loadTexts:
    aluIpTransportV8v0Group.setStatus("current")

aluIpTransportNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 22, 2, 1, 3)
)
aluIpTransportNotifyObjsGroup.setObjects(
      *(("ALU-IP-TRANSPORT-MIB", "aluIpTransportNotifyCustId"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportNotifySvcId"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportNotifyPortId"))
)
if mibBuilder.loadTexts:
    aluIpTransportNotifyObjsGroup.setStatus("current")

aluIpTransportStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 22, 2, 1, 4)
)
aluIpTransportStatsGroup.setObjects(
      *(("ALU-IP-TRANSPORT-MIB", "aluIpTransportKnwRemPktsSent"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportKnwRemCharsSent"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportKnwRemPktsRcvd"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportKnwRemCharsRcvd"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportKnwRemConnsTo"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportKnwRemConnsFrom"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportKnwRemConnRetries"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportKnwRemConnFails"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportKnwRemCurrConns"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportUnkRemPktsSent"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportUnkRemCharsSent"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportUnkRemPktsRcvd"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportUnkRemCharsRcvd"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportUnkRemSuccConnsFrm"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportUnkRemRejectsFiltr"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportUnkRemRejectsResrc"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportUnkRemInactTimouts"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportUnkRemLastIpAddrTy"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportUnkRemLastIpAddr"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportUnkRemLastPortNum"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportUnkRemCurrConns"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportPktsDropNoRemHost"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostPktsSent"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostCharsSent"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostPktsDrop"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostCharsDrop"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostPktsRcvd"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostCharsRcvd"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostConnsTo"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostConnsFrom"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostConnRetries"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostConnFails"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostConnsCloFar"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportRemHostInactTmouts"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportURemHostPktsSent"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportURemHostCharsSent"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportURemHostPktsDrop"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportURemHostCharsDrop"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportURemHostPktsRcvd"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportURemHostCharsRcvd"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportURemHostSessState"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportURemHostSessUpTime"))
)
if mibBuilder.loadTexts:
    aluIpTransportStatsGroup.setStatus("current")


# Notification objects

aluIpTransportStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 18, 0, 1)
)
aluIpTransportStateChanged.setObjects(
      *(("ALU-IP-TRANSPORT-MIB", "aluIpTransportNotifyCustId"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportNotifySvcId"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportNotifyPortId"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportAdminState"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportOperState"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportOperFlags"))
)
if mibBuilder.loadTexts:
    aluIpTransportStateChanged.setStatus(
        "current"
    )


# Notifications groups

aluIpTransportNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 22, 2, 1, 2)
)
aluIpTransportNotifyGroup.setObjects(
    ("ALU-IP-TRANSPORT-MIB", "aluIpTransportStateChanged")
)
if mibBuilder.loadTexts:
    aluIpTransportNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aluIpTransport7705V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 22, 1, 1)
)
aluIpTransport7705V8v0Compliance.setObjects(
      *(("ALU-IP-TRANSPORT-MIB", "aluIpTransportV8v0Group"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportNotifyGroup"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportNotifyObjsGroup"),
        ("ALU-IP-TRANSPORT-MIB", "aluIpTransportStatsGroup"))
)
if mibBuilder.loadTexts:
    aluIpTransport7705V8v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-IP-TRANSPORT-MIB",
    **{"AluIpTransportRemHostId": AluIpTransportRemHostId,
       "AluIpTransportRemHostSessState": AluIpTransportRemHostSessState,
       "aluIpTransportMIBModule": aluIpTransportMIBModule,
       "aluIpTransportConformance": aluIpTransportConformance,
       "aluIpTransportCompliances": aluIpTransportCompliances,
       "aluIpTransport7705V8v0Compliance": aluIpTransport7705V8v0Compliance,
       "aluIpTransportGroups": aluIpTransportGroups,
       "aluIpTransportV8v0Groups": aluIpTransportV8v0Groups,
       "aluIpTransportV8v0Group": aluIpTransportV8v0Group,
       "aluIpTransportNotifyGroup": aluIpTransportNotifyGroup,
       "aluIpTransportNotifyObjsGroup": aluIpTransportNotifyObjsGroup,
       "aluIpTransportStatsGroup": aluIpTransportStatsGroup,
       "aluIpTransportObjs": aluIpTransportObjs,
       "aluIpTransportConfigTimestamps": aluIpTransportConfigTimestamps,
       "aluIpTransportTableLastChanged": aluIpTransportTableLastChanged,
       "aluIpTransportRemHostTblLastChgd": aluIpTransportRemHostTblLastChgd,
       "aluIpTransportConfigurations": aluIpTransportConfigurations,
       "aluIpTransportTable": aluIpTransportTable,
       "aluIpTransportEntry": aluIpTransportEntry,
       "aluIpTransportPortId": aluIpTransportPortId,
       "aluIpTransportLastMgmtChange": aluIpTransportLastMgmtChange,
       "aluIpTransportRowStatus": aluIpTransportRowStatus,
       "aluIpTransportAdminState": aluIpTransportAdminState,
       "aluIpTransportDescription": aluIpTransportDescription,
       "aluIpTransportTcpConnMaxRetries": aluIpTransportTcpConnMaxRetries,
       "aluIpTransportTcpConnRetryIntvl": aluIpTransportTcpConnRetryIntvl,
       "aluIpTransportTcpConnInactTimout": aluIpTransportTcpConnInactTimout,
       "aluIpTransportFilterUnknownHost": aluIpTransportFilterUnknownHost,
       "aluIpTransportDscpName": aluIpTransportDscpName,
       "aluIpTransportFcName": aluIpTransportFcName,
       "aluIpTransportProfile": aluIpTransportProfile,
       "aluIpTransportLocHostIpAddrType": aluIpTransportLocHostIpAddrType,
       "aluIpTransportLocHostIpAddr": aluIpTransportLocHostIpAddr,
       "aluIpTransportLocHostPortNum": aluIpTransportLocHostPortNum,
       "aluIpTransportLocHostIpProtocol": aluIpTransportLocHostIpProtocol,
       "aluIpTransportNumRemHosts": aluIpTransportNumRemHosts,
       "aluIpTransportOperState": aluIpTransportOperState,
       "aluIpTransportOperFlags": aluIpTransportOperFlags,
       "aluIpTransportLastOperChange": aluIpTransportLastOperChange,
       "aluIpTransportRemHostTable": aluIpTransportRemHostTable,
       "aluIpTransportRemHostEntry": aluIpTransportRemHostEntry,
       "aluIpTransportRemHostId": aluIpTransportRemHostId,
       "aluIpTransportRemHostLastChanged": aluIpTransportRemHostLastChanged,
       "aluIpTransportRemHostRowStatus": aluIpTransportRemHostRowStatus,
       "aluIpTransportRemHostName": aluIpTransportRemHostName,
       "aluIpTransportRemHostDescription": aluIpTransportRemHostDescription,
       "aluIpTransportRemHostIpAddrType": aluIpTransportRemHostIpAddrType,
       "aluIpTransportRemHostIpAddr": aluIpTransportRemHostIpAddr,
       "aluIpTransportRemHostPortNum": aluIpTransportRemHostPortNum,
       "aluIpTransportRemHostSessState": aluIpTransportRemHostSessState,
       "aluIpTransportRemHostSessUpTime": aluIpTransportRemHostSessUpTime,
       "aluIpTransportRemHostLastConnect": aluIpTransportRemHostLastConnect,
       "aluIpTransportRemHostCheckTcp": aluIpTransportRemHostCheckTcp,
       "aluIpTransportRemHostCheckTcpRes": aluIpTransportRemHostCheckTcpRes,
       "aluIpTransportRemHostCheckTcpInf": aluIpTransportRemHostCheckTcpInf,
       "aluIpTransportSvcBaseExtTable": aluIpTransportSvcBaseExtTable,
       "aluIpTransportSvcBaseExtEntry": aluIpTransportSvcBaseExtEntry,
       "aluIpTransportSvcBaseExtNumIpts": aluIpTransportSvcBaseExtNumIpts,
       "aluIpTransportNameObjects": aluIpTransportNameObjects,
       "aluIpTransportRemHostNameTable": aluIpTransportRemHostNameTable,
       "aluIpTransportRemHostNameEntry": aluIpTransportRemHostNameEntry,
       "aluIpTransportRemHostNameId": aluIpTransportRemHostNameId,
       "aluIpTransportStatus": aluIpTransportStatus,
       "aluIpTransportStatsObjects": aluIpTransportStatsObjects,
       "aluIpTransportStatsTable": aluIpTransportStatsTable,
       "aluIpTransportStatsEntry": aluIpTransportStatsEntry,
       "aluIpTransportKnwRemPktsSent": aluIpTransportKnwRemPktsSent,
       "aluIpTransportKnwRemCharsSent": aluIpTransportKnwRemCharsSent,
       "aluIpTransportKnwRemPktsRcvd": aluIpTransportKnwRemPktsRcvd,
       "aluIpTransportKnwRemCharsRcvd": aluIpTransportKnwRemCharsRcvd,
       "aluIpTransportKnwRemConnsTo": aluIpTransportKnwRemConnsTo,
       "aluIpTransportKnwRemConnsFrom": aluIpTransportKnwRemConnsFrom,
       "aluIpTransportKnwRemConnRetries": aluIpTransportKnwRemConnRetries,
       "aluIpTransportKnwRemConnFails": aluIpTransportKnwRemConnFails,
       "aluIpTransportKnwRemCurrConns": aluIpTransportKnwRemCurrConns,
       "aluIpTransportUnkRemPktsSent": aluIpTransportUnkRemPktsSent,
       "aluIpTransportUnkRemCharsSent": aluIpTransportUnkRemCharsSent,
       "aluIpTransportUnkRemPktsRcvd": aluIpTransportUnkRemPktsRcvd,
       "aluIpTransportUnkRemCharsRcvd": aluIpTransportUnkRemCharsRcvd,
       "aluIpTransportUnkRemSuccConnsFrm": aluIpTransportUnkRemSuccConnsFrm,
       "aluIpTransportUnkRemRejectsFiltr": aluIpTransportUnkRemRejectsFiltr,
       "aluIpTransportUnkRemRejectsResrc": aluIpTransportUnkRemRejectsResrc,
       "aluIpTransportUnkRemInactTimouts": aluIpTransportUnkRemInactTimouts,
       "aluIpTransportUnkRemLastIpAddrTy": aluIpTransportUnkRemLastIpAddrTy,
       "aluIpTransportUnkRemLastIpAddr": aluIpTransportUnkRemLastIpAddr,
       "aluIpTransportUnkRemLastPortNum": aluIpTransportUnkRemLastPortNum,
       "aluIpTransportUnkRemCurrConns": aluIpTransportUnkRemCurrConns,
       "aluIpTransportPktsDropNoRemHost": aluIpTransportPktsDropNoRemHost,
       "aluIpTransportRemHostStatsTable": aluIpTransportRemHostStatsTable,
       "aluIpTransportRemHostStatsEntry": aluIpTransportRemHostStatsEntry,
       "aluIpTransportRemHostPktsSent": aluIpTransportRemHostPktsSent,
       "aluIpTransportRemHostCharsSent": aluIpTransportRemHostCharsSent,
       "aluIpTransportRemHostPktsDrop": aluIpTransportRemHostPktsDrop,
       "aluIpTransportRemHostCharsDrop": aluIpTransportRemHostCharsDrop,
       "aluIpTransportRemHostPktsRcvd": aluIpTransportRemHostPktsRcvd,
       "aluIpTransportRemHostCharsRcvd": aluIpTransportRemHostCharsRcvd,
       "aluIpTransportRemHostConnsTo": aluIpTransportRemHostConnsTo,
       "aluIpTransportRemHostConnsFrom": aluIpTransportRemHostConnsFrom,
       "aluIpTransportRemHostConnRetries": aluIpTransportRemHostConnRetries,
       "aluIpTransportRemHostConnFails": aluIpTransportRemHostConnFails,
       "aluIpTransportRemHostConnsCloFar": aluIpTransportRemHostConnsCloFar,
       "aluIpTransportRemHostInactTmouts": aluIpTransportRemHostInactTmouts,
       "aluIpTransportURemHostStatsTable": aluIpTransportURemHostStatsTable,
       "aluIpTransportURemHostStatsEntry": aluIpTransportURemHostStatsEntry,
       "aluIpTransportURemHostIpAddrType": aluIpTransportURemHostIpAddrType,
       "aluIpTransportURemHostIpAddr": aluIpTransportURemHostIpAddr,
       "aluIpTransportURemHostPortNum": aluIpTransportURemHostPortNum,
       "aluIpTransportURemHostPktsSent": aluIpTransportURemHostPktsSent,
       "aluIpTransportURemHostCharsSent": aluIpTransportURemHostCharsSent,
       "aluIpTransportURemHostPktsDrop": aluIpTransportURemHostPktsDrop,
       "aluIpTransportURemHostCharsDrop": aluIpTransportURemHostCharsDrop,
       "aluIpTransportURemHostPktsRcvd": aluIpTransportURemHostPktsRcvd,
       "aluIpTransportURemHostCharsRcvd": aluIpTransportURemHostCharsRcvd,
       "aluIpTransportURemHostSessState": aluIpTransportURemHostSessState,
       "aluIpTransportURemHostSessUpTime": aluIpTransportURemHostSessUpTime,
       "aluIpTransportNotifyObjects": aluIpTransportNotifyObjects,
       "aluIpTransportNotifyCustId": aluIpTransportNotifyCustId,
       "aluIpTransportNotifySvcId": aluIpTransportNotifySvcId,
       "aluIpTransportNotifyPortId": aluIpTransportNotifyPortId,
       "aluIpTransportNotifyPrefix": aluIpTransportNotifyPrefix,
       "aluIpTransportNotifications": aluIpTransportNotifications,
       "aluIpTransportStateChanged": aluIpTransportStateChanged}
)
