# SNMP MIB module (DDOSSECURE4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/juniper/DDOSSECURE4-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:38:26 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ddossecure4MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4)
)
if mibBuilder.loadTexts:
    ddossecure4MIB.setRevisions(
        ("2014-04-25 00:00",
         "2013-11-01 00:00",
         "2012-02-17 00:00",
         "2011-09-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DefenseType(TextualConvention, Integer32):
    status = "current"
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("bandWidth", 1),
          ("flood", 2),
          ("blockedProtocol", 3),
          ("blockedState", 4),
          ("ipAttack", 5),
          ("tcpAttack", 6),
          ("udpAttack", 7),
          ("icmpAttack", 8),
          ("otherIpAttack", 9),
          ("fragmentAttack", 10),
          ("badIpPacket", 11),
          ("badTcpPacket", 12),
          ("badUdpPacket", 13),
          ("badIcmpPacket", 14),
          ("badOtherIpPacket", 15),
          ("overloadedProtectedIP", 16))
    )



class Direction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outbound", 1),
          ("inbound", 2))
    )



class LocalIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_DdossecureEvents_ObjectIdentity = ObjectIdentity
ddossecureEvents = _DdossecureEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0)
)
if mibBuilder.loadTexts:
    ddossecureEvents.setStatus("current")
_JddsAppliance_ObjectIdentity = ObjectIdentity
jddsAppliance = _JddsAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4)
)
_ApConfig_ObjectIdentity = ObjectIdentity
apConfig = _ApConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1)
)
_ApInterfaces_ObjectIdentity = ObjectIdentity
apInterfaces = _ApInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1)
)
_ApManagement_ObjectIdentity = ObjectIdentity
apManagement = _ApManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 1)
)
_ApMgmtIfIpAddress_Type = IpAddress
_ApMgmtIfIpAddress_Object = MibScalar
apMgmtIfIpAddress = _ApMgmtIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 1, 1),
    _ApMgmtIfIpAddress_Type()
)
apMgmtIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMgmtIfIpAddress.setStatus("current")
_ApMgmtIfNetmask_Type = IpAddress
_ApMgmtIfNetmask_Object = MibScalar
apMgmtIfNetmask = _ApMgmtIfNetmask_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 1, 2),
    _ApMgmtIfNetmask_Type()
)
apMgmtIfNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMgmtIfNetmask.setStatus("current")
_ApMgmtIfGwIpAddress_Type = IpAddress
_ApMgmtIfGwIpAddress_Object = MibScalar
apMgmtIfGwIpAddress = _ApMgmtIfGwIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 1, 3),
    _ApMgmtIfGwIpAddress_Type()
)
apMgmtIfGwIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMgmtIfGwIpAddress.setStatus("current")
_ApMgmtIfLinkMode_Type = DisplayString
_ApMgmtIfLinkMode_Object = MibScalar
apMgmtIfLinkMode = _ApMgmtIfLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 1, 4),
    _ApMgmtIfLinkMode_Type()
)
apMgmtIfLinkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMgmtIfLinkMode.setStatus("current")
_ApMgmtIfLinkFC_Type = DisplayString
_ApMgmtIfLinkFC_Object = MibScalar
apMgmtIfLinkFC = _ApMgmtIfLinkFC_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 1, 5),
    _ApMgmtIfLinkFC_Type()
)
apMgmtIfLinkFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMgmtIfLinkFC.setStatus("current")
_ApMgmtIfName_Type = DisplayString
_ApMgmtIfName_Object = MibScalar
apMgmtIfName = _ApMgmtIfName_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 1, 6),
    _ApMgmtIfName_Type()
)
apMgmtIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMgmtIfName.setStatus("current")
_ApInternet_ObjectIdentity = ObjectIdentity
apInternet = _ApInternet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 2)
)
_ApIntIfLinkMode_Type = DisplayString
_ApIntIfLinkMode_Object = MibScalar
apIntIfLinkMode = _ApIntIfLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 2, 1),
    _ApIntIfLinkMode_Type()
)
apIntIfLinkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIntIfLinkMode.setStatus("current")
_ApIntIfLinkFC_Type = DisplayString
_ApIntIfLinkFC_Object = MibScalar
apIntIfLinkFC = _ApIntIfLinkFC_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 2, 2),
    _ApIntIfLinkFC_Type()
)
apIntIfLinkFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIntIfLinkFC.setStatus("current")
_ApIntIfName_Type = DisplayString
_ApIntIfName_Object = MibScalar
apIntIfName = _ApIntIfName_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 2, 3),
    _ApIntIfName_Type()
)
apIntIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIntIfName.setStatus("current")
_ApProtectedInterface_ObjectIdentity = ObjectIdentity
apProtectedInterface = _ApProtectedInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 3)
)
_ApProtIfLinkMode_Type = DisplayString
_ApProtIfLinkMode_Object = MibScalar
apProtIfLinkMode = _ApProtIfLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 3, 1),
    _ApProtIfLinkMode_Type()
)
apProtIfLinkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProtIfLinkMode.setStatus("current")
_ApProtIfLinkFC_Type = DisplayString
_ApProtIfLinkFC_Object = MibScalar
apProtIfLinkFC = _ApProtIfLinkFC_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 3, 2),
    _ApProtIfLinkFC_Type()
)
apProtIfLinkFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProtIfLinkFC.setStatus("current")
_ApProtIfName_Type = DisplayString
_ApProtIfName_Object = MibScalar
apProtIfName = _ApProtIfName_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 3, 3),
    _ApProtIfName_Type()
)
apProtIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProtIfName.setStatus("current")
_ApDataShare_ObjectIdentity = ObjectIdentity
apDataShare = _ApDataShare_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 4)
)
_ApDataIfIpAddress_Type = IpAddress
_ApDataIfIpAddress_Object = MibScalar
apDataIfIpAddress = _ApDataIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 4, 1),
    _ApDataIfIpAddress_Type()
)
apDataIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDataIfIpAddress.setStatus("current")
_ApDataIfNetmask_Type = IpAddress
_ApDataIfNetmask_Object = MibScalar
apDataIfNetmask = _ApDataIfNetmask_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 4, 2),
    _ApDataIfNetmask_Type()
)
apDataIfNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDataIfNetmask.setStatus("current")
_ApDataIfLinkMode_Type = DisplayString
_ApDataIfLinkMode_Object = MibScalar
apDataIfLinkMode = _ApDataIfLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 4, 3),
    _ApDataIfLinkMode_Type()
)
apDataIfLinkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDataIfLinkMode.setStatus("current")
_ApDataIfLinkFC_Type = DisplayString
_ApDataIfLinkFC_Object = MibScalar
apDataIfLinkFC = _ApDataIfLinkFC_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 4, 4),
    _ApDataIfLinkFC_Type()
)
apDataIfLinkFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDataIfLinkFC.setStatus("current")
_ApDataIfName_Type = DisplayString
_ApDataIfName_Object = MibScalar
apDataIfName = _ApDataIfName_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 1, 4, 5),
    _ApDataIfName_Type()
)
apDataIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDataIfName.setStatus("current")
_ApAccess_ObjectIdentity = ObjectIdentity
apAccess = _ApAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 2)
)
_ApUserTable_Object = MibTable
apUserTable = _ApUserTable_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    apUserTable.setStatus("current")
_ApUserEntry_Object = MibTableRow
apUserEntry = _ApUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 2, 1, 1)
)
apUserEntry.setIndexNames(
    (0, "DDOSSECURE4-MIB", "apUserId"),
)
if mibBuilder.loadTexts:
    apUserEntry.setStatus("current")
_ApUserId_Type = LocalIndex
_ApUserId_Object = MibTableColumn
apUserId = _ApUserId_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 2, 1, 1, 1),
    _ApUserId_Type()
)
apUserId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apUserId.setStatus("current")
_ApUserName_Type = DisplayString
_ApUserName_Object = MibTableColumn
apUserName = _ApUserName_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 2, 1, 1, 2),
    _ApUserName_Type()
)
apUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUserName.setStatus("current")
_ApUserPermissions_Type = DisplayString
_ApUserPermissions_Object = MibTableColumn
apUserPermissions = _ApUserPermissions_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 2, 1, 1, 3),
    _ApUserPermissions_Type()
)
apUserPermissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUserPermissions.setStatus("current")
_ApSnmpAccessIpList_Type = DisplayString
_ApSnmpAccessIpList_Object = MibScalar
apSnmpAccessIpList = _ApSnmpAccessIpList_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 2, 3),
    _ApSnmpAccessIpList_Type()
)
apSnmpAccessIpList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSnmpAccessIpList.setStatus("current")
_ApHttpsAccessIpList_Type = DisplayString
_ApHttpsAccessIpList_Object = MibScalar
apHttpsAccessIpList = _ApHttpsAccessIpList_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 2, 4),
    _ApHttpsAccessIpList_Type()
)
apHttpsAccessIpList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apHttpsAccessIpList.setStatus("current")
_ApSshAccessIpList_Type = DisplayString
_ApSshAccessIpList_Object = MibScalar
apSshAccessIpList = _ApSshAccessIpList_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 2, 5),
    _ApSshAccessIpList_Type()
)
apSshAccessIpList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSshAccessIpList.setStatus("current")
_ApLogging_ObjectIdentity = ObjectIdentity
apLogging = _ApLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3)
)
_ApSyslogServer_Type = DisplayString
_ApSyslogServer_Object = MibScalar
apSyslogServer = _ApSyslogServer_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 1),
    _ApSyslogServer_Type()
)
apSyslogServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSyslogServer.setStatus("current")
_ApSyslogFacility_Type = DisplayString
_ApSyslogFacility_Object = MibScalar
apSyslogFacility = _ApSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 2),
    _ApSyslogFacility_Type()
)
apSyslogFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSyslogFacility.setStatus("current")
_ApSyslogPriority_Type = DisplayString
_ApSyslogPriority_Object = MibScalar
apSyslogPriority = _ApSyslogPriority_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 3),
    _ApSyslogPriority_Type()
)
apSyslogPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSyslogPriority.setStatus("current")
_ApWebtrendsServer_Type = DisplayString
_ApWebtrendsServer_Object = MibScalar
apWebtrendsServer = _ApWebtrendsServer_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 4),
    _ApWebtrendsServer_Type()
)
apWebtrendsServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWebtrendsServer.setStatus("current")
_ApWebtrendsFacility_Type = DisplayString
_ApWebtrendsFacility_Object = MibScalar
apWebtrendsFacility = _ApWebtrendsFacility_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 5),
    _ApWebtrendsFacility_Type()
)
apWebtrendsFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWebtrendsFacility.setStatus("current")
_ApWebtrendsPriority_Type = DisplayString
_ApWebtrendsPriority_Object = MibScalar
apWebtrendsPriority = _ApWebtrendsPriority_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 6),
    _ApWebtrendsPriority_Type()
)
apWebtrendsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWebtrendsPriority.setStatus("current")
_ApCreateIncidentsThreshold_ObjectIdentity = ObjectIdentity
apCreateIncidentsThreshold = _ApCreateIncidentsThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7)
)
_ApBandwidthCreateThresh_Type = TruthValue
_ApBandwidthCreateThresh_Object = MibScalar
apBandwidthCreateThresh = _ApBandwidthCreateThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 1),
    _ApBandwidthCreateThresh_Type()
)
apBandwidthCreateThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBandwidthCreateThresh.setStatus("current")
_ApBandwidthCreateThreshRate_Type = Gauge32
_ApBandwidthCreateThreshRate_Object = MibScalar
apBandwidthCreateThreshRate = _ApBandwidthCreateThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 2),
    _ApBandwidthCreateThreshRate_Type()
)
apBandwidthCreateThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBandwidthCreateThreshRate.setStatus("current")
_ApFloodCreateThresh_Type = TruthValue
_ApFloodCreateThresh_Object = MibScalar
apFloodCreateThresh = _ApFloodCreateThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 3),
    _ApFloodCreateThresh_Type()
)
apFloodCreateThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFloodCreateThresh.setStatus("current")
_ApFloodCreateThreshRate_Type = Gauge32
_ApFloodCreateThreshRate_Object = MibScalar
apFloodCreateThreshRate = _ApFloodCreateThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 4),
    _ApFloodCreateThreshRate_Type()
)
apFloodCreateThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFloodCreateThreshRate.setStatus("current")
_ApBlockedProtoCreateThresh_Type = TruthValue
_ApBlockedProtoCreateThresh_Object = MibScalar
apBlockedProtoCreateThresh = _ApBlockedProtoCreateThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 5),
    _ApBlockedProtoCreateThresh_Type()
)
apBlockedProtoCreateThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedProtoCreateThresh.setStatus("current")
_ApBlockedProtoCreateThreshRate_Type = Gauge32
_ApBlockedProtoCreateThreshRate_Object = MibScalar
apBlockedProtoCreateThreshRate = _ApBlockedProtoCreateThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 6),
    _ApBlockedProtoCreateThreshRate_Type()
)
apBlockedProtoCreateThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedProtoCreateThreshRate.setStatus("current")
_ApBlockedStateCreateThresh_Type = TruthValue
_ApBlockedStateCreateThresh_Object = MibScalar
apBlockedStateCreateThresh = _ApBlockedStateCreateThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 7),
    _ApBlockedStateCreateThresh_Type()
)
apBlockedStateCreateThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedStateCreateThresh.setStatus("current")
_ApBlockedStateCreateThreshRate_Type = Gauge32
_ApBlockedStateCreateThreshRate_Object = MibScalar
apBlockedStateCreateThreshRate = _ApBlockedStateCreateThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 8),
    _ApBlockedStateCreateThreshRate_Type()
)
apBlockedStateCreateThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedStateCreateThreshRate.setStatus("current")
_ApIpAttackCreateThresh_Type = TruthValue
_ApIpAttackCreateThresh_Object = MibScalar
apIpAttackCreateThresh = _ApIpAttackCreateThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 9),
    _ApIpAttackCreateThresh_Type()
)
apIpAttackCreateThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpAttackCreateThresh.setStatus("current")
_ApIpAttackCreateThreshRate_Type = Gauge32
_ApIpAttackCreateThreshRate_Object = MibScalar
apIpAttackCreateThreshRate = _ApIpAttackCreateThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 10),
    _ApIpAttackCreateThreshRate_Type()
)
apIpAttackCreateThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpAttackCreateThreshRate.setStatus("current")
_ApTcpAttackCreateThresh_Type = TruthValue
_ApTcpAttackCreateThresh_Object = MibScalar
apTcpAttackCreateThresh = _ApTcpAttackCreateThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 11),
    _ApTcpAttackCreateThresh_Type()
)
apTcpAttackCreateThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTcpAttackCreateThresh.setStatus("current")
_ApTcpAttackCreateThreshRate_Type = Gauge32
_ApTcpAttackCreateThreshRate_Object = MibScalar
apTcpAttackCreateThreshRate = _ApTcpAttackCreateThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 12),
    _ApTcpAttackCreateThreshRate_Type()
)
apTcpAttackCreateThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTcpAttackCreateThreshRate.setStatus("current")
_ApUdpAttackCreateThresh_Type = TruthValue
_ApUdpAttackCreateThresh_Object = MibScalar
apUdpAttackCreateThresh = _ApUdpAttackCreateThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 13),
    _ApUdpAttackCreateThresh_Type()
)
apUdpAttackCreateThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUdpAttackCreateThresh.setStatus("current")
_ApUdpAttackCreateThreshRate_Type = Gauge32
_ApUdpAttackCreateThreshRate_Object = MibScalar
apUdpAttackCreateThreshRate = _ApUdpAttackCreateThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 14),
    _ApUdpAttackCreateThreshRate_Type()
)
apUdpAttackCreateThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUdpAttackCreateThreshRate.setStatus("current")
_ApIcmpAttackCreateThresh_Type = TruthValue
_ApIcmpAttackCreateThresh_Object = MibScalar
apIcmpAttackCreateThresh = _ApIcmpAttackCreateThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 15),
    _ApIcmpAttackCreateThresh_Type()
)
apIcmpAttackCreateThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIcmpAttackCreateThresh.setStatus("current")
_ApIcmpAttackCreateThreshRate_Type = Gauge32
_ApIcmpAttackCreateThreshRate_Object = MibScalar
apIcmpAttackCreateThreshRate = _ApIcmpAttackCreateThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 16),
    _ApIcmpAttackCreateThreshRate_Type()
)
apIcmpAttackCreateThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIcmpAttackCreateThreshRate.setStatus("current")
_ApOtherIpAttackCreateThresh_Type = TruthValue
_ApOtherIpAttackCreateThresh_Object = MibScalar
apOtherIpAttackCreateThresh = _ApOtherIpAttackCreateThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 17),
    _ApOtherIpAttackCreateThresh_Type()
)
apOtherIpAttackCreateThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOtherIpAttackCreateThresh.setStatus("current")
_ApOtherIpAttackCreateThreshRate_Type = Gauge32
_ApOtherIpAttackCreateThreshRate_Object = MibScalar
apOtherIpAttackCreateThreshRate = _ApOtherIpAttackCreateThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 18),
    _ApOtherIpAttackCreateThreshRate_Type()
)
apOtherIpAttackCreateThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOtherIpAttackCreateThreshRate.setStatus("current")
_ApFragAttackCreateThresh_Type = TruthValue
_ApFragAttackCreateThresh_Object = MibScalar
apFragAttackCreateThresh = _ApFragAttackCreateThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 19),
    _ApFragAttackCreateThresh_Type()
)
apFragAttackCreateThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFragAttackCreateThresh.setStatus("current")
_ApFragAttackCreateThreshRate_Type = Gauge32
_ApFragAttackCreateThreshRate_Object = MibScalar
apFragAttackCreateThreshRate = _ApFragAttackCreateThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 20),
    _ApFragAttackCreateThreshRate_Type()
)
apFragAttackCreateThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFragAttackCreateThreshRate.setStatus("current")
_ApBadIpCreateThresh_Type = TruthValue
_ApBadIpCreateThresh_Object = MibScalar
apBadIpCreateThresh = _ApBadIpCreateThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 21),
    _ApBadIpCreateThresh_Type()
)
apBadIpCreateThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadIpCreateThresh.setStatus("current")
_ApBadIpCreateThreshRate_Type = Gauge32
_ApBadIpCreateThreshRate_Object = MibScalar
apBadIpCreateThreshRate = _ApBadIpCreateThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 22),
    _ApBadIpCreateThreshRate_Type()
)
apBadIpCreateThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadIpCreateThreshRate.setStatus("current")
_ApBadTcpCreateThresh_Type = TruthValue
_ApBadTcpCreateThresh_Object = MibScalar
apBadTcpCreateThresh = _ApBadTcpCreateThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 23),
    _ApBadTcpCreateThresh_Type()
)
apBadTcpCreateThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadTcpCreateThresh.setStatus("current")
_ApBadTcpCreateThreshRate_Type = Gauge32
_ApBadTcpCreateThreshRate_Object = MibScalar
apBadTcpCreateThreshRate = _ApBadTcpCreateThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 24),
    _ApBadTcpCreateThreshRate_Type()
)
apBadTcpCreateThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadTcpCreateThreshRate.setStatus("current")
_ApBadUdpCreateThresh_Type = TruthValue
_ApBadUdpCreateThresh_Object = MibScalar
apBadUdpCreateThresh = _ApBadUdpCreateThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 25),
    _ApBadUdpCreateThresh_Type()
)
apBadUdpCreateThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadUdpCreateThresh.setStatus("current")
_ApBadUdpCreateThreshRate_Type = Gauge32
_ApBadUdpCreateThreshRate_Object = MibScalar
apBadUdpCreateThreshRate = _ApBadUdpCreateThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 26),
    _ApBadUdpCreateThreshRate_Type()
)
apBadUdpCreateThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadUdpCreateThreshRate.setStatus("current")
_ApBadIcmpCreateThresh_Type = TruthValue
_ApBadIcmpCreateThresh_Object = MibScalar
apBadIcmpCreateThresh = _ApBadIcmpCreateThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 27),
    _ApBadIcmpCreateThresh_Type()
)
apBadIcmpCreateThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadIcmpCreateThresh.setStatus("current")
_ApBadIcmpCreateThreshRate_Type = Gauge32
_ApBadIcmpCreateThreshRate_Object = MibScalar
apBadIcmpCreateThreshRate = _ApBadIcmpCreateThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 28),
    _ApBadIcmpCreateThreshRate_Type()
)
apBadIcmpCreateThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadIcmpCreateThreshRate.setStatus("current")
_ApBadOtherIpCreateThresh_Type = TruthValue
_ApBadOtherIpCreateThresh_Object = MibScalar
apBadOtherIpCreateThresh = _ApBadOtherIpCreateThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 29),
    _ApBadOtherIpCreateThresh_Type()
)
apBadOtherIpCreateThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadOtherIpCreateThresh.setStatus("current")
_ApBadOtherIpCreateThreshRate_Type = Gauge32
_ApBadOtherIpCreateThreshRate_Object = MibScalar
apBadOtherIpCreateThreshRate = _ApBadOtherIpCreateThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 30),
    _ApBadOtherIpCreateThreshRate_Type()
)
apBadOtherIpCreateThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadOtherIpCreateThreshRate.setStatus("current")
_ApOverloadedIpCreateThresh_Type = TruthValue
_ApOverloadedIpCreateThresh_Object = MibScalar
apOverloadedIpCreateThresh = _ApOverloadedIpCreateThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 31),
    _ApOverloadedIpCreateThresh_Type()
)
apOverloadedIpCreateThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOverloadedIpCreateThresh.setStatus("current")
_ApOverloadedIpCreateThreshRate_Type = Gauge32
_ApOverloadedIpCreateThreshRate_Object = MibScalar
apOverloadedIpCreateThreshRate = _ApOverloadedIpCreateThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 7, 32),
    _ApOverloadedIpCreateThreshRate_Type()
)
apOverloadedIpCreateThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOverloadedIpCreateThreshRate.setStatus("current")
_ApViewIncidentsThresholds_ObjectIdentity = ObjectIdentity
apViewIncidentsThresholds = _ApViewIncidentsThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8)
)
_ApBandwidthViewThresh_Type = TruthValue
_ApBandwidthViewThresh_Object = MibScalar
apBandwidthViewThresh = _ApBandwidthViewThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 1),
    _ApBandwidthViewThresh_Type()
)
apBandwidthViewThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBandwidthViewThresh.setStatus("current")
_ApBandwidthViewThreshRate_Type = Gauge32
_ApBandwidthViewThreshRate_Object = MibScalar
apBandwidthViewThreshRate = _ApBandwidthViewThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 2),
    _ApBandwidthViewThreshRate_Type()
)
apBandwidthViewThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBandwidthViewThreshRate.setStatus("current")
_ApFloodViewThresh_Type = TruthValue
_ApFloodViewThresh_Object = MibScalar
apFloodViewThresh = _ApFloodViewThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 3),
    _ApFloodViewThresh_Type()
)
apFloodViewThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFloodViewThresh.setStatus("current")
_ApFloodViewThreshRate_Type = Gauge32
_ApFloodViewThreshRate_Object = MibScalar
apFloodViewThreshRate = _ApFloodViewThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 4),
    _ApFloodViewThreshRate_Type()
)
apFloodViewThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFloodViewThreshRate.setStatus("current")
_ApBlockedProtoViewThresh_Type = TruthValue
_ApBlockedProtoViewThresh_Object = MibScalar
apBlockedProtoViewThresh = _ApBlockedProtoViewThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 5),
    _ApBlockedProtoViewThresh_Type()
)
apBlockedProtoViewThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedProtoViewThresh.setStatus("current")
_ApBlockedProtoViewThreshRate_Type = Gauge32
_ApBlockedProtoViewThreshRate_Object = MibScalar
apBlockedProtoViewThreshRate = _ApBlockedProtoViewThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 6),
    _ApBlockedProtoViewThreshRate_Type()
)
apBlockedProtoViewThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedProtoViewThreshRate.setStatus("current")
_ApBlockedStateViewThresh_Type = TruthValue
_ApBlockedStateViewThresh_Object = MibScalar
apBlockedStateViewThresh = _ApBlockedStateViewThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 7),
    _ApBlockedStateViewThresh_Type()
)
apBlockedStateViewThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedStateViewThresh.setStatus("current")
_ApBlockedStateViewThreshRate_Type = Gauge32
_ApBlockedStateViewThreshRate_Object = MibScalar
apBlockedStateViewThreshRate = _ApBlockedStateViewThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 8),
    _ApBlockedStateViewThreshRate_Type()
)
apBlockedStateViewThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedStateViewThreshRate.setStatus("current")
_ApIpAttackViewThresh_Type = TruthValue
_ApIpAttackViewThresh_Object = MibScalar
apIpAttackViewThresh = _ApIpAttackViewThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 9),
    _ApIpAttackViewThresh_Type()
)
apIpAttackViewThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpAttackViewThresh.setStatus("current")
_ApIpAttackViewThreshRate_Type = Gauge32
_ApIpAttackViewThreshRate_Object = MibScalar
apIpAttackViewThreshRate = _ApIpAttackViewThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 10),
    _ApIpAttackViewThreshRate_Type()
)
apIpAttackViewThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpAttackViewThreshRate.setStatus("current")
_ApTcpAttackViewThresh_Type = TruthValue
_ApTcpAttackViewThresh_Object = MibScalar
apTcpAttackViewThresh = _ApTcpAttackViewThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 11),
    _ApTcpAttackViewThresh_Type()
)
apTcpAttackViewThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTcpAttackViewThresh.setStatus("current")
_ApTcpAttackViewThreshRate_Type = Gauge32
_ApTcpAttackViewThreshRate_Object = MibScalar
apTcpAttackViewThreshRate = _ApTcpAttackViewThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 12),
    _ApTcpAttackViewThreshRate_Type()
)
apTcpAttackViewThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTcpAttackViewThreshRate.setStatus("current")
_ApUdpAttackViewThresh_Type = TruthValue
_ApUdpAttackViewThresh_Object = MibScalar
apUdpAttackViewThresh = _ApUdpAttackViewThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 13),
    _ApUdpAttackViewThresh_Type()
)
apUdpAttackViewThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUdpAttackViewThresh.setStatus("current")
_ApUdpAttackViewThreshRate_Type = Gauge32
_ApUdpAttackViewThreshRate_Object = MibScalar
apUdpAttackViewThreshRate = _ApUdpAttackViewThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 14),
    _ApUdpAttackViewThreshRate_Type()
)
apUdpAttackViewThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUdpAttackViewThreshRate.setStatus("current")
_ApIcmpAttackViewThresh_Type = TruthValue
_ApIcmpAttackViewThresh_Object = MibScalar
apIcmpAttackViewThresh = _ApIcmpAttackViewThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 15),
    _ApIcmpAttackViewThresh_Type()
)
apIcmpAttackViewThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIcmpAttackViewThresh.setStatus("current")
_ApIcmpAttackViewThreshRate_Type = Gauge32
_ApIcmpAttackViewThreshRate_Object = MibScalar
apIcmpAttackViewThreshRate = _ApIcmpAttackViewThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 16),
    _ApIcmpAttackViewThreshRate_Type()
)
apIcmpAttackViewThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIcmpAttackViewThreshRate.setStatus("current")
_ApOtherIpAttackViewThresh_Type = TruthValue
_ApOtherIpAttackViewThresh_Object = MibScalar
apOtherIpAttackViewThresh = _ApOtherIpAttackViewThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 17),
    _ApOtherIpAttackViewThresh_Type()
)
apOtherIpAttackViewThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOtherIpAttackViewThresh.setStatus("current")
_ApOtherIpAttackViewThreshRate_Type = Gauge32
_ApOtherIpAttackViewThreshRate_Object = MibScalar
apOtherIpAttackViewThreshRate = _ApOtherIpAttackViewThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 18),
    _ApOtherIpAttackViewThreshRate_Type()
)
apOtherIpAttackViewThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOtherIpAttackViewThreshRate.setStatus("current")
_ApFragAttackViewThresh_Type = TruthValue
_ApFragAttackViewThresh_Object = MibScalar
apFragAttackViewThresh = _ApFragAttackViewThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 19),
    _ApFragAttackViewThresh_Type()
)
apFragAttackViewThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFragAttackViewThresh.setStatus("current")
_ApFragAttackViewThreshRate_Type = Gauge32
_ApFragAttackViewThreshRate_Object = MibScalar
apFragAttackViewThreshRate = _ApFragAttackViewThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 20),
    _ApFragAttackViewThreshRate_Type()
)
apFragAttackViewThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFragAttackViewThreshRate.setStatus("current")
_ApBadIpViewThresh_Type = TruthValue
_ApBadIpViewThresh_Object = MibScalar
apBadIpViewThresh = _ApBadIpViewThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 21),
    _ApBadIpViewThresh_Type()
)
apBadIpViewThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadIpViewThresh.setStatus("current")
_ApBadIpViewThreshRate_Type = Gauge32
_ApBadIpViewThreshRate_Object = MibScalar
apBadIpViewThreshRate = _ApBadIpViewThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 22),
    _ApBadIpViewThreshRate_Type()
)
apBadIpViewThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadIpViewThreshRate.setStatus("current")
_ApBadTcpViewThresh_Type = TruthValue
_ApBadTcpViewThresh_Object = MibScalar
apBadTcpViewThresh = _ApBadTcpViewThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 23),
    _ApBadTcpViewThresh_Type()
)
apBadTcpViewThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadTcpViewThresh.setStatus("current")
_ApBadTcpViewThreshRate_Type = Gauge32
_ApBadTcpViewThreshRate_Object = MibScalar
apBadTcpViewThreshRate = _ApBadTcpViewThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 24),
    _ApBadTcpViewThreshRate_Type()
)
apBadTcpViewThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadTcpViewThreshRate.setStatus("current")
_ApBadUdpViewThresh_Type = TruthValue
_ApBadUdpViewThresh_Object = MibScalar
apBadUdpViewThresh = _ApBadUdpViewThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 25),
    _ApBadUdpViewThresh_Type()
)
apBadUdpViewThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadUdpViewThresh.setStatus("current")
_ApBadUdpViewThreshRate_Type = Gauge32
_ApBadUdpViewThreshRate_Object = MibScalar
apBadUdpViewThreshRate = _ApBadUdpViewThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 26),
    _ApBadUdpViewThreshRate_Type()
)
apBadUdpViewThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadUdpViewThreshRate.setStatus("current")
_ApBadIcmpViewThresh_Type = TruthValue
_ApBadIcmpViewThresh_Object = MibScalar
apBadIcmpViewThresh = _ApBadIcmpViewThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 27),
    _ApBadIcmpViewThresh_Type()
)
apBadIcmpViewThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadIcmpViewThresh.setStatus("current")
_ApBadIcmpViewThreshRate_Type = Gauge32
_ApBadIcmpViewThreshRate_Object = MibScalar
apBadIcmpViewThreshRate = _ApBadIcmpViewThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 28),
    _ApBadIcmpViewThreshRate_Type()
)
apBadIcmpViewThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadIcmpViewThreshRate.setStatus("current")
_ApBadOtherIpViewThresh_Type = TruthValue
_ApBadOtherIpViewThresh_Object = MibScalar
apBadOtherIpViewThresh = _ApBadOtherIpViewThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 29),
    _ApBadOtherIpViewThresh_Type()
)
apBadOtherIpViewThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadOtherIpViewThresh.setStatus("current")
_ApBadOtherIpViewThreshRate_Type = Gauge32
_ApBadOtherIpViewThreshRate_Object = MibScalar
apBadOtherIpViewThreshRate = _ApBadOtherIpViewThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 30),
    _ApBadOtherIpViewThreshRate_Type()
)
apBadOtherIpViewThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadOtherIpViewThreshRate.setStatus("current")
_ApOverloadedIpViewThresh_Type = TruthValue
_ApOverloadedIpViewThresh_Object = MibScalar
apOverloadedIpViewThresh = _ApOverloadedIpViewThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 31),
    _ApOverloadedIpViewThresh_Type()
)
apOverloadedIpViewThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOverloadedIpViewThresh.setStatus("current")
_ApOverloadedIpViewThreshRate_Type = Gauge32
_ApOverloadedIpViewThreshRate_Object = MibScalar
apOverloadedIpViewThreshRate = _ApOverloadedIpViewThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 8, 32),
    _ApOverloadedIpViewThreshRate_Type()
)
apOverloadedIpViewThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOverloadedIpViewThreshRate.setStatus("current")
_ApWOffenderLogThreshold_ObjectIdentity = ObjectIdentity
apWOffenderLogThreshold = _ApWOffenderLogThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9)
)
_ApBandwidthOffThresh_Type = TruthValue
_ApBandwidthOffThresh_Object = MibScalar
apBandwidthOffThresh = _ApBandwidthOffThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 1),
    _ApBandwidthOffThresh_Type()
)
apBandwidthOffThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBandwidthOffThresh.setStatus("current")
_ApBandwidthOffThreshRate_Type = Gauge32
_ApBandwidthOffThreshRate_Object = MibScalar
apBandwidthOffThreshRate = _ApBandwidthOffThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 2),
    _ApBandwidthOffThreshRate_Type()
)
apBandwidthOffThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBandwidthOffThreshRate.setStatus("current")
_ApFloodOffThresh_Type = TruthValue
_ApFloodOffThresh_Object = MibScalar
apFloodOffThresh = _ApFloodOffThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 3),
    _ApFloodOffThresh_Type()
)
apFloodOffThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFloodOffThresh.setStatus("current")
_ApFloodOffThreshRate_Type = Gauge32
_ApFloodOffThreshRate_Object = MibScalar
apFloodOffThreshRate = _ApFloodOffThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 4),
    _ApFloodOffThreshRate_Type()
)
apFloodOffThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFloodOffThreshRate.setStatus("current")
_ApBlockedProtoOffThresh_Type = TruthValue
_ApBlockedProtoOffThresh_Object = MibScalar
apBlockedProtoOffThresh = _ApBlockedProtoOffThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 5),
    _ApBlockedProtoOffThresh_Type()
)
apBlockedProtoOffThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedProtoOffThresh.setStatus("current")
_ApBlockedProtoOffThreshRate_Type = Gauge32
_ApBlockedProtoOffThreshRate_Object = MibScalar
apBlockedProtoOffThreshRate = _ApBlockedProtoOffThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 6),
    _ApBlockedProtoOffThreshRate_Type()
)
apBlockedProtoOffThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedProtoOffThreshRate.setStatus("current")
_ApBlockedStateOffThresh_Type = TruthValue
_ApBlockedStateOffThresh_Object = MibScalar
apBlockedStateOffThresh = _ApBlockedStateOffThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 7),
    _ApBlockedStateOffThresh_Type()
)
apBlockedStateOffThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedStateOffThresh.setStatus("current")
_ApBlockedStateOffThreshRate_Type = Gauge32
_ApBlockedStateOffThreshRate_Object = MibScalar
apBlockedStateOffThreshRate = _ApBlockedStateOffThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 8),
    _ApBlockedStateOffThreshRate_Type()
)
apBlockedStateOffThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedStateOffThreshRate.setStatus("current")
_ApIpAttackOffThresh_Type = TruthValue
_ApIpAttackOffThresh_Object = MibScalar
apIpAttackOffThresh = _ApIpAttackOffThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 9),
    _ApIpAttackOffThresh_Type()
)
apIpAttackOffThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpAttackOffThresh.setStatus("current")
_ApIpAttackOffThreshRate_Type = Gauge32
_ApIpAttackOffThreshRate_Object = MibScalar
apIpAttackOffThreshRate = _ApIpAttackOffThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 10),
    _ApIpAttackOffThreshRate_Type()
)
apIpAttackOffThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpAttackOffThreshRate.setStatus("current")
_ApTcpAttackOffThresh_Type = TruthValue
_ApTcpAttackOffThresh_Object = MibScalar
apTcpAttackOffThresh = _ApTcpAttackOffThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 11),
    _ApTcpAttackOffThresh_Type()
)
apTcpAttackOffThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTcpAttackOffThresh.setStatus("current")
_ApTcpAttackOffThreshRate_Type = Gauge32
_ApTcpAttackOffThreshRate_Object = MibScalar
apTcpAttackOffThreshRate = _ApTcpAttackOffThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 12),
    _ApTcpAttackOffThreshRate_Type()
)
apTcpAttackOffThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTcpAttackOffThreshRate.setStatus("current")
_ApUdpAttackOffThresh_Type = TruthValue
_ApUdpAttackOffThresh_Object = MibScalar
apUdpAttackOffThresh = _ApUdpAttackOffThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 13),
    _ApUdpAttackOffThresh_Type()
)
apUdpAttackOffThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUdpAttackOffThresh.setStatus("current")
_ApUdpAttackOffThreshRate_Type = Gauge32
_ApUdpAttackOffThreshRate_Object = MibScalar
apUdpAttackOffThreshRate = _ApUdpAttackOffThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 14),
    _ApUdpAttackOffThreshRate_Type()
)
apUdpAttackOffThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUdpAttackOffThreshRate.setStatus("current")
_ApIcmpAttackOffThresh_Type = TruthValue
_ApIcmpAttackOffThresh_Object = MibScalar
apIcmpAttackOffThresh = _ApIcmpAttackOffThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 15),
    _ApIcmpAttackOffThresh_Type()
)
apIcmpAttackOffThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIcmpAttackOffThresh.setStatus("current")
_ApIcmpAttackOffThreshRate_Type = Gauge32
_ApIcmpAttackOffThreshRate_Object = MibScalar
apIcmpAttackOffThreshRate = _ApIcmpAttackOffThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 16),
    _ApIcmpAttackOffThreshRate_Type()
)
apIcmpAttackOffThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIcmpAttackOffThreshRate.setStatus("current")
_ApOtherIpAttackOffThresh_Type = TruthValue
_ApOtherIpAttackOffThresh_Object = MibScalar
apOtherIpAttackOffThresh = _ApOtherIpAttackOffThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 17),
    _ApOtherIpAttackOffThresh_Type()
)
apOtherIpAttackOffThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOtherIpAttackOffThresh.setStatus("current")
_ApOtherIpAttackOffThreshRate_Type = Gauge32
_ApOtherIpAttackOffThreshRate_Object = MibScalar
apOtherIpAttackOffThreshRate = _ApOtherIpAttackOffThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 18),
    _ApOtherIpAttackOffThreshRate_Type()
)
apOtherIpAttackOffThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOtherIpAttackOffThreshRate.setStatus("current")
_ApFragAttackOffThresh_Type = TruthValue
_ApFragAttackOffThresh_Object = MibScalar
apFragAttackOffThresh = _ApFragAttackOffThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 19),
    _ApFragAttackOffThresh_Type()
)
apFragAttackOffThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFragAttackOffThresh.setStatus("current")
_ApFragAttackOffThreshRate_Type = Gauge32
_ApFragAttackOffThreshRate_Object = MibScalar
apFragAttackOffThreshRate = _ApFragAttackOffThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 20),
    _ApFragAttackOffThreshRate_Type()
)
apFragAttackOffThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFragAttackOffThreshRate.setStatus("current")
_ApBadIpOffThresh_Type = TruthValue
_ApBadIpOffThresh_Object = MibScalar
apBadIpOffThresh = _ApBadIpOffThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 21),
    _ApBadIpOffThresh_Type()
)
apBadIpOffThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadIpOffThresh.setStatus("current")
_ApBadIpOffThreshRate_Type = Gauge32
_ApBadIpOffThreshRate_Object = MibScalar
apBadIpOffThreshRate = _ApBadIpOffThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 22),
    _ApBadIpOffThreshRate_Type()
)
apBadIpOffThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadIpOffThreshRate.setStatus("current")
_ApBadTcpOffThresh_Type = TruthValue
_ApBadTcpOffThresh_Object = MibScalar
apBadTcpOffThresh = _ApBadTcpOffThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 23),
    _ApBadTcpOffThresh_Type()
)
apBadTcpOffThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadTcpOffThresh.setStatus("current")
_ApBadTcpOffThreshRate_Type = Gauge32
_ApBadTcpOffThreshRate_Object = MibScalar
apBadTcpOffThreshRate = _ApBadTcpOffThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 24),
    _ApBadTcpOffThreshRate_Type()
)
apBadTcpOffThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadTcpOffThreshRate.setStatus("current")
_ApBadUdpOffThresh_Type = TruthValue
_ApBadUdpOffThresh_Object = MibScalar
apBadUdpOffThresh = _ApBadUdpOffThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 25),
    _ApBadUdpOffThresh_Type()
)
apBadUdpOffThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadUdpOffThresh.setStatus("current")
_ApBadUdpOffThreshRate_Type = Gauge32
_ApBadUdpOffThreshRate_Object = MibScalar
apBadUdpOffThreshRate = _ApBadUdpOffThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 26),
    _ApBadUdpOffThreshRate_Type()
)
apBadUdpOffThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadUdpOffThreshRate.setStatus("current")
_ApBadIcmpOffThresh_Type = TruthValue
_ApBadIcmpOffThresh_Object = MibScalar
apBadIcmpOffThresh = _ApBadIcmpOffThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 27),
    _ApBadIcmpOffThresh_Type()
)
apBadIcmpOffThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadIcmpOffThresh.setStatus("current")
_ApBadIcmpOffThreshRate_Type = Gauge32
_ApBadIcmpOffThreshRate_Object = MibScalar
apBadIcmpOffThreshRate = _ApBadIcmpOffThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 28),
    _ApBadIcmpOffThreshRate_Type()
)
apBadIcmpOffThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadIcmpOffThreshRate.setStatus("current")
_ApBadOtherIpOffThresh_Type = TruthValue
_ApBadOtherIpOffThresh_Object = MibScalar
apBadOtherIpOffThresh = _ApBadOtherIpOffThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 29),
    _ApBadOtherIpOffThresh_Type()
)
apBadOtherIpOffThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadOtherIpOffThresh.setStatus("current")
_ApBadOtherIpOffThreshRate_Type = Gauge32
_ApBadOtherIpOffThreshRate_Object = MibScalar
apBadOtherIpOffThreshRate = _ApBadOtherIpOffThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 30),
    _ApBadOtherIpOffThreshRate_Type()
)
apBadOtherIpOffThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadOtherIpOffThreshRate.setStatus("current")
_ApOverloadedIpOffThresh_Type = TruthValue
_ApOverloadedIpOffThresh_Object = MibScalar
apOverloadedIpOffThresh = _ApOverloadedIpOffThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 31),
    _ApOverloadedIpOffThresh_Type()
)
apOverloadedIpOffThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOverloadedIpOffThresh.setStatus("current")
_ApOverloadedIpOffThreshRate_Type = Gauge32
_ApOverloadedIpOffThreshRate_Object = MibScalar
apOverloadedIpOffThreshRate = _ApOverloadedIpOffThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 9, 32),
    _ApOverloadedIpOffThreshRate_Type()
)
apOverloadedIpOffThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOverloadedIpOffThreshRate.setStatus("current")
_ApIncidentAlertThreshold_ObjectIdentity = ObjectIdentity
apIncidentAlertThreshold = _ApIncidentAlertThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10)
)
_ApBandwidthAlertThresh_Type = TruthValue
_ApBandwidthAlertThresh_Object = MibScalar
apBandwidthAlertThresh = _ApBandwidthAlertThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 1),
    _ApBandwidthAlertThresh_Type()
)
apBandwidthAlertThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBandwidthAlertThresh.setStatus("current")
_ApBandwidthAlertThreshRate_Type = Gauge32
_ApBandwidthAlertThreshRate_Object = MibScalar
apBandwidthAlertThreshRate = _ApBandwidthAlertThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 2),
    _ApBandwidthAlertThreshRate_Type()
)
apBandwidthAlertThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBandwidthAlertThreshRate.setStatus("current")
_ApFloodAlertThresh_Type = TruthValue
_ApFloodAlertThresh_Object = MibScalar
apFloodAlertThresh = _ApFloodAlertThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 3),
    _ApFloodAlertThresh_Type()
)
apFloodAlertThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFloodAlertThresh.setStatus("current")
_ApFloodAlertThreshRate_Type = Gauge32
_ApFloodAlertThreshRate_Object = MibScalar
apFloodAlertThreshRate = _ApFloodAlertThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 4),
    _ApFloodAlertThreshRate_Type()
)
apFloodAlertThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFloodAlertThreshRate.setStatus("current")
_ApBlockedProtoAlertThresh_Type = TruthValue
_ApBlockedProtoAlertThresh_Object = MibScalar
apBlockedProtoAlertThresh = _ApBlockedProtoAlertThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 5),
    _ApBlockedProtoAlertThresh_Type()
)
apBlockedProtoAlertThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedProtoAlertThresh.setStatus("current")
_ApBlockedProtoAlertThreshRate_Type = Gauge32
_ApBlockedProtoAlertThreshRate_Object = MibScalar
apBlockedProtoAlertThreshRate = _ApBlockedProtoAlertThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 6),
    _ApBlockedProtoAlertThreshRate_Type()
)
apBlockedProtoAlertThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedProtoAlertThreshRate.setStatus("current")
_ApBlockedStateAlertThresh_Type = TruthValue
_ApBlockedStateAlertThresh_Object = MibScalar
apBlockedStateAlertThresh = _ApBlockedStateAlertThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 7),
    _ApBlockedStateAlertThresh_Type()
)
apBlockedStateAlertThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedStateAlertThresh.setStatus("current")
_ApBlockedStateAlertThreshRate_Type = Gauge32
_ApBlockedStateAlertThreshRate_Object = MibScalar
apBlockedStateAlertThreshRate = _ApBlockedStateAlertThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 8),
    _ApBlockedStateAlertThreshRate_Type()
)
apBlockedStateAlertThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedStateAlertThreshRate.setStatus("current")
_ApIpAttackAlertThresh_Type = TruthValue
_ApIpAttackAlertThresh_Object = MibScalar
apIpAttackAlertThresh = _ApIpAttackAlertThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 9),
    _ApIpAttackAlertThresh_Type()
)
apIpAttackAlertThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpAttackAlertThresh.setStatus("current")
_ApIpAttackAlertThreshRate_Type = Gauge32
_ApIpAttackAlertThreshRate_Object = MibScalar
apIpAttackAlertThreshRate = _ApIpAttackAlertThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 10),
    _ApIpAttackAlertThreshRate_Type()
)
apIpAttackAlertThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpAttackAlertThreshRate.setStatus("current")
_ApTcpAttackAlertThresh_Type = TruthValue
_ApTcpAttackAlertThresh_Object = MibScalar
apTcpAttackAlertThresh = _ApTcpAttackAlertThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 11),
    _ApTcpAttackAlertThresh_Type()
)
apTcpAttackAlertThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTcpAttackAlertThresh.setStatus("current")
_ApTcpAttackAlertThreshRate_Type = Gauge32
_ApTcpAttackAlertThreshRate_Object = MibScalar
apTcpAttackAlertThreshRate = _ApTcpAttackAlertThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 12),
    _ApTcpAttackAlertThreshRate_Type()
)
apTcpAttackAlertThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTcpAttackAlertThreshRate.setStatus("current")
_ApUdpAttackAlertThresh_Type = TruthValue
_ApUdpAttackAlertThresh_Object = MibScalar
apUdpAttackAlertThresh = _ApUdpAttackAlertThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 13),
    _ApUdpAttackAlertThresh_Type()
)
apUdpAttackAlertThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUdpAttackAlertThresh.setStatus("current")
_ApUdpAttackAlertThreshRate_Type = Gauge32
_ApUdpAttackAlertThreshRate_Object = MibScalar
apUdpAttackAlertThreshRate = _ApUdpAttackAlertThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 14),
    _ApUdpAttackAlertThreshRate_Type()
)
apUdpAttackAlertThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUdpAttackAlertThreshRate.setStatus("current")
_ApIcmpAttackAlertThresh_Type = TruthValue
_ApIcmpAttackAlertThresh_Object = MibScalar
apIcmpAttackAlertThresh = _ApIcmpAttackAlertThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 15),
    _ApIcmpAttackAlertThresh_Type()
)
apIcmpAttackAlertThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIcmpAttackAlertThresh.setStatus("current")
_ApIcmpAttackAlertThreshRate_Type = Gauge32
_ApIcmpAttackAlertThreshRate_Object = MibScalar
apIcmpAttackAlertThreshRate = _ApIcmpAttackAlertThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 16),
    _ApIcmpAttackAlertThreshRate_Type()
)
apIcmpAttackAlertThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIcmpAttackAlertThreshRate.setStatus("current")
_ApOtherIpAttackAlertThresh_Type = TruthValue
_ApOtherIpAttackAlertThresh_Object = MibScalar
apOtherIpAttackAlertThresh = _ApOtherIpAttackAlertThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 17),
    _ApOtherIpAttackAlertThresh_Type()
)
apOtherIpAttackAlertThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOtherIpAttackAlertThresh.setStatus("current")
_ApOtherIpAttackAlertThreshRate_Type = Gauge32
_ApOtherIpAttackAlertThreshRate_Object = MibScalar
apOtherIpAttackAlertThreshRate = _ApOtherIpAttackAlertThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 18),
    _ApOtherIpAttackAlertThreshRate_Type()
)
apOtherIpAttackAlertThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOtherIpAttackAlertThreshRate.setStatus("current")
_ApFragAttackAlertThresh_Type = TruthValue
_ApFragAttackAlertThresh_Object = MibScalar
apFragAttackAlertThresh = _ApFragAttackAlertThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 19),
    _ApFragAttackAlertThresh_Type()
)
apFragAttackAlertThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFragAttackAlertThresh.setStatus("current")
_ApFragAttackAlertThreshRate_Type = Gauge32
_ApFragAttackAlertThreshRate_Object = MibScalar
apFragAttackAlertThreshRate = _ApFragAttackAlertThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 20),
    _ApFragAttackAlertThreshRate_Type()
)
apFragAttackAlertThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFragAttackAlertThreshRate.setStatus("current")
_ApBadIpAlertThresh_Type = TruthValue
_ApBadIpAlertThresh_Object = MibScalar
apBadIpAlertThresh = _ApBadIpAlertThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 21),
    _ApBadIpAlertThresh_Type()
)
apBadIpAlertThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadIpAlertThresh.setStatus("current")
_ApBadIpAlertThreshRate_Type = Gauge32
_ApBadIpAlertThreshRate_Object = MibScalar
apBadIpAlertThreshRate = _ApBadIpAlertThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 22),
    _ApBadIpAlertThreshRate_Type()
)
apBadIpAlertThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadIpAlertThreshRate.setStatus("current")
_ApBadTcpAlertThresh_Type = TruthValue
_ApBadTcpAlertThresh_Object = MibScalar
apBadTcpAlertThresh = _ApBadTcpAlertThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 23),
    _ApBadTcpAlertThresh_Type()
)
apBadTcpAlertThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadTcpAlertThresh.setStatus("current")
_ApBadTcpAlertThreshRate_Type = Gauge32
_ApBadTcpAlertThreshRate_Object = MibScalar
apBadTcpAlertThreshRate = _ApBadTcpAlertThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 24),
    _ApBadTcpAlertThreshRate_Type()
)
apBadTcpAlertThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadTcpAlertThreshRate.setStatus("current")
_ApBadUdpAlertThresh_Type = TruthValue
_ApBadUdpAlertThresh_Object = MibScalar
apBadUdpAlertThresh = _ApBadUdpAlertThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 25),
    _ApBadUdpAlertThresh_Type()
)
apBadUdpAlertThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadUdpAlertThresh.setStatus("current")
_ApBadUdpAlertThreshRate_Type = Gauge32
_ApBadUdpAlertThreshRate_Object = MibScalar
apBadUdpAlertThreshRate = _ApBadUdpAlertThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 26),
    _ApBadUdpAlertThreshRate_Type()
)
apBadUdpAlertThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadUdpAlertThreshRate.setStatus("current")
_ApBadIcmpAlertThresh_Type = TruthValue
_ApBadIcmpAlertThresh_Object = MibScalar
apBadIcmpAlertThresh = _ApBadIcmpAlertThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 27),
    _ApBadIcmpAlertThresh_Type()
)
apBadIcmpAlertThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadIcmpAlertThresh.setStatus("current")
_ApBadIcmpAlertThreshRate_Type = Gauge32
_ApBadIcmpAlertThreshRate_Object = MibScalar
apBadIcmpAlertThreshRate = _ApBadIcmpAlertThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 28),
    _ApBadIcmpAlertThreshRate_Type()
)
apBadIcmpAlertThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadIcmpAlertThreshRate.setStatus("current")
_ApBadOtherIpAlertThresh_Type = TruthValue
_ApBadOtherIpAlertThresh_Object = MibScalar
apBadOtherIpAlertThresh = _ApBadOtherIpAlertThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 29),
    _ApBadOtherIpAlertThresh_Type()
)
apBadOtherIpAlertThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadOtherIpAlertThresh.setStatus("current")
_ApBadOtherIpAlertThreshRate_Type = Gauge32
_ApBadOtherIpAlertThreshRate_Object = MibScalar
apBadOtherIpAlertThreshRate = _ApBadOtherIpAlertThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 30),
    _ApBadOtherIpAlertThreshRate_Type()
)
apBadOtherIpAlertThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadOtherIpAlertThreshRate.setStatus("current")
_ApOverloadedIpAlertThresh_Type = TruthValue
_ApOverloadedIpAlertThresh_Object = MibScalar
apOverloadedIpAlertThresh = _ApOverloadedIpAlertThresh_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 31),
    _ApOverloadedIpAlertThresh_Type()
)
apOverloadedIpAlertThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOverloadedIpAlertThresh.setStatus("current")
_ApOverloadedIpAlertThreshRate_Type = Gauge32
_ApOverloadedIpAlertThreshRate_Object = MibScalar
apOverloadedIpAlertThreshRate = _ApOverloadedIpAlertThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 3, 10, 32),
    _ApOverloadedIpAlertThreshRate_Type()
)
apOverloadedIpAlertThreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOverloadedIpAlertThreshRate.setStatus("current")
_ApMail_ObjectIdentity = ObjectIdentity
apMail = _ApMail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 4)
)
_ApMailServer_Type = IpAddress
_ApMailServer_Object = MibScalar
apMailServer = _ApMailServer_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 4, 1),
    _ApMailServer_Type()
)
apMailServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMailServer.setStatus("current")
_ApMailFrom_Type = DisplayString
_ApMailFrom_Object = MibScalar
apMailFrom = _ApMailFrom_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 4, 2),
    _ApMailFrom_Type()
)
apMailFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMailFrom.setStatus("current")
_ApMailSubject_Type = DisplayString
_ApMailSubject_Object = MibScalar
apMailSubject = _ApMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 4, 3),
    _ApMailSubject_Type()
)
apMailSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMailSubject.setStatus("current")
_ApMailToList_Type = DisplayString
_ApMailToList_Object = MibScalar
apMailToList = _ApMailToList_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 4, 4),
    _ApMailToList_Type()
)
apMailToList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMailToList.setStatus("current")
_ApMailDailyStats_Type = TruthValue
_ApMailDailyStats_Object = MibScalar
apMailDailyStats = _ApMailDailyStats_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 4, 5),
    _ApMailDailyStats_Type()
)
apMailDailyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMailDailyStats.setStatus("current")
_ApMailAlerts_Type = TruthValue
_ApMailAlerts_Object = MibScalar
apMailAlerts = _ApMailAlerts_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 4, 6),
    _ApMailAlerts_Type()
)
apMailAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMailAlerts.setStatus("current")
_ApMailAlertInterval_Type = Gauge32
_ApMailAlertInterval_Object = MibScalar
apMailAlertInterval = _ApMailAlertInterval_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 4, 7),
    _ApMailAlertInterval_Type()
)
apMailAlertInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMailAlertInterval.setStatus("current")
_ApDebugConfig_ObjectIdentity = ObjectIdentity
apDebugConfig = _ApDebugConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 5)
)
_ApDebugBandwidthFlag_Type = TruthValue
_ApDebugBandwidthFlag_Object = MibScalar
apDebugBandwidthFlag = _ApDebugBandwidthFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 5, 1),
    _ApDebugBandwidthFlag_Type()
)
apDebugBandwidthFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDebugBandwidthFlag.setStatus("current")
_ApDebugFloodFlag_Type = TruthValue
_ApDebugFloodFlag_Object = MibScalar
apDebugFloodFlag = _ApDebugFloodFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 5, 2),
    _ApDebugFloodFlag_Type()
)
apDebugFloodFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDebugFloodFlag.setStatus("current")
_ApDebugBlockedProtocolFlag_Type = TruthValue
_ApDebugBlockedProtocolFlag_Object = MibScalar
apDebugBlockedProtocolFlag = _ApDebugBlockedProtocolFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 5, 3),
    _ApDebugBlockedProtocolFlag_Type()
)
apDebugBlockedProtocolFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDebugBlockedProtocolFlag.setStatus("current")
_ApDebugBlockedStateFlag_Type = TruthValue
_ApDebugBlockedStateFlag_Object = MibScalar
apDebugBlockedStateFlag = _ApDebugBlockedStateFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 5, 4),
    _ApDebugBlockedStateFlag_Type()
)
apDebugBlockedStateFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDebugBlockedStateFlag.setStatus("current")
_ApDebugIpAttackFlag_Type = TruthValue
_ApDebugIpAttackFlag_Object = MibScalar
apDebugIpAttackFlag = _ApDebugIpAttackFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 5, 5),
    _ApDebugIpAttackFlag_Type()
)
apDebugIpAttackFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDebugIpAttackFlag.setStatus("current")
_ApDebugTcpAttackFlag_Type = TruthValue
_ApDebugTcpAttackFlag_Object = MibScalar
apDebugTcpAttackFlag = _ApDebugTcpAttackFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 5, 6),
    _ApDebugTcpAttackFlag_Type()
)
apDebugTcpAttackFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDebugTcpAttackFlag.setStatus("current")
_ApDebugUdpAttackFlag_Type = TruthValue
_ApDebugUdpAttackFlag_Object = MibScalar
apDebugUdpAttackFlag = _ApDebugUdpAttackFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 5, 7),
    _ApDebugUdpAttackFlag_Type()
)
apDebugUdpAttackFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDebugUdpAttackFlag.setStatus("current")
_ApDebugIcmpAttackFlag_Type = TruthValue
_ApDebugIcmpAttackFlag_Object = MibScalar
apDebugIcmpAttackFlag = _ApDebugIcmpAttackFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 5, 8),
    _ApDebugIcmpAttackFlag_Type()
)
apDebugIcmpAttackFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDebugIcmpAttackFlag.setStatus("current")
_ApDebugOtherIpAttackFlag_Type = TruthValue
_ApDebugOtherIpAttackFlag_Object = MibScalar
apDebugOtherIpAttackFlag = _ApDebugOtherIpAttackFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 5, 9),
    _ApDebugOtherIpAttackFlag_Type()
)
apDebugOtherIpAttackFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDebugOtherIpAttackFlag.setStatus("current")
_ApDebugFragmentAttackFlag_Type = TruthValue
_ApDebugFragmentAttackFlag_Object = MibScalar
apDebugFragmentAttackFlag = _ApDebugFragmentAttackFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 5, 10),
    _ApDebugFragmentAttackFlag_Type()
)
apDebugFragmentAttackFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDebugFragmentAttackFlag.setStatus("current")
_ApDebugBadIpPacketFlag_Type = TruthValue
_ApDebugBadIpPacketFlag_Object = MibScalar
apDebugBadIpPacketFlag = _ApDebugBadIpPacketFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 5, 11),
    _ApDebugBadIpPacketFlag_Type()
)
apDebugBadIpPacketFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDebugBadIpPacketFlag.setStatus("current")
_ApDebugBadTcpPacketFlag_Type = TruthValue
_ApDebugBadTcpPacketFlag_Object = MibScalar
apDebugBadTcpPacketFlag = _ApDebugBadTcpPacketFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 5, 12),
    _ApDebugBadTcpPacketFlag_Type()
)
apDebugBadTcpPacketFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDebugBadTcpPacketFlag.setStatus("current")
_ApDebugBadUdpPacketFlag_Type = TruthValue
_ApDebugBadUdpPacketFlag_Object = MibScalar
apDebugBadUdpPacketFlag = _ApDebugBadUdpPacketFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 5, 13),
    _ApDebugBadUdpPacketFlag_Type()
)
apDebugBadUdpPacketFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDebugBadUdpPacketFlag.setStatus("current")
_ApDebugBadIcmpFlag_Type = TruthValue
_ApDebugBadIcmpFlag_Object = MibScalar
apDebugBadIcmpFlag = _ApDebugBadIcmpFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 5, 14),
    _ApDebugBadIcmpFlag_Type()
)
apDebugBadIcmpFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDebugBadIcmpFlag.setStatus("current")
_ApDebugBadOtherIpFlag_Type = TruthValue
_ApDebugBadOtherIpFlag_Object = MibScalar
apDebugBadOtherIpFlag = _ApDebugBadOtherIpFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 5, 15),
    _ApDebugBadOtherIpFlag_Type()
)
apDebugBadOtherIpFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDebugBadOtherIpFlag.setStatus("current")
_ApDebugOverloadProtectedIpFlag_Type = TruthValue
_ApDebugOverloadProtectedIpFlag_Object = MibScalar
apDebugOverloadProtectedIpFlag = _ApDebugOverloadProtectedIpFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 5, 16),
    _ApDebugOverloadProtectedIpFlag_Type()
)
apDebugOverloadProtectedIpFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDebugOverloadProtectedIpFlag.setStatus("current")
_ApOperationMode_Type = DisplayString
_ApOperationMode_Object = MibScalar
apOperationMode = _ApOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 6),
    _ApOperationMode_Type()
)
apOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOperationMode.setStatus("current")
_ApNtpServerList_Type = DisplayString
_ApNtpServerList_Object = MibScalar
apNtpServerList = _ApNtpServerList_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 7),
    _ApNtpServerList_Type()
)
apNtpServerList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNtpServerList.setStatus("current")
_ApTimeZone_Type = DisplayString
_ApTimeZone_Object = MibScalar
apTimeZone = _ApTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 8),
    _ApTimeZone_Type()
)
apTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTimeZone.setStatus("current")
_ApProtectedIpNetwork_Type = DisplayString
_ApProtectedIpNetwork_Object = MibScalar
apProtectedIpNetwork = _ApProtectedIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 9),
    _ApProtectedIpNetwork_Type()
)
apProtectedIpNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProtectedIpNetwork.setStatus("current")
_ApSnmp_ObjectIdentity = ObjectIdentity
apSnmp = _ApSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 10)
)
_ApSnmpRoCommunity_Type = DisplayString
_ApSnmpRoCommunity_Object = MibScalar
apSnmpRoCommunity = _ApSnmpRoCommunity_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 10, 1),
    _ApSnmpRoCommunity_Type()
)
apSnmpRoCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSnmpRoCommunity.setStatus("current")
_ApSnmpTrapCommunity_Type = DisplayString
_ApSnmpTrapCommunity_Object = MibScalar
apSnmpTrapCommunity = _ApSnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 10, 2),
    _ApSnmpTrapCommunity_Type()
)
apSnmpTrapCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSnmpTrapCommunity.setStatus("current")
_ApSnmpTrapIpAddressList_Type = DisplayString
_ApSnmpTrapIpAddressList_Object = MibScalar
apSnmpTrapIpAddressList = _ApSnmpTrapIpAddressList_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 10, 3),
    _ApSnmpTrapIpAddressList_Type()
)
apSnmpTrapIpAddressList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSnmpTrapIpAddressList.setStatus("current")
_ApAutoBlackList_ObjectIdentity = ObjectIdentity
apAutoBlackList = _ApAutoBlackList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 11)
)
_ApAutoblockEnable_Type = TruthValue
_ApAutoblockEnable_Object = MibScalar
apAutoblockEnable = _ApAutoblockEnable_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 11, 1),
    _ApAutoblockEnable_Type()
)
apAutoblockEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAutoblockEnable.setStatus("current")
_ApAutoblockRateT1_Type = Gauge32
_ApAutoblockRateT1_Object = MibScalar
apAutoblockRateT1 = _ApAutoblockRateT1_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 11, 2),
    _ApAutoblockRateT1_Type()
)
apAutoblockRateT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAutoblockRateT1.setStatus("current")
_ApAutoblockRateT2_Type = Gauge32
_ApAutoblockRateT2_Object = MibScalar
apAutoblockRateT2 = _ApAutoblockRateT2_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 11, 3),
    _ApAutoblockRateT2_Type()
)
apAutoblockRateT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAutoblockRateT2.setStatus("current")
_ApProtectedIpAutodetect_Type = TruthValue
_ApProtectedIpAutodetect_Object = MibScalar
apProtectedIpAutodetect = _ApProtectedIpAutodetect_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 12),
    _ApProtectedIpAutodetect_Type()
)
apProtectedIpAutodetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProtectedIpAutodetect.setStatus("current")
_ApTrackIndeterminate_Type = TruthValue
_ApTrackIndeterminate_Object = MibScalar
apTrackIndeterminate = _ApTrackIndeterminate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 1, 13),
    _ApTrackIndeterminate_Type()
)
apTrackIndeterminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrackIndeterminate.setStatus("current")
_ApState_ObjectIdentity = ObjectIdentity
apState = _ApState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2)
)
_ApDefenseFlags_ObjectIdentity = ObjectIdentity
apDefenseFlags = _ApDefenseFlags_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 1)
)
_ApBandwidth_Type = TruthValue
_ApBandwidth_Object = MibScalar
apBandwidth = _ApBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 1, 1),
    _ApBandwidth_Type()
)
apBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBandwidth.setStatus("current")
_ApFlood_Type = TruthValue
_ApFlood_Object = MibScalar
apFlood = _ApFlood_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 1, 2),
    _ApFlood_Type()
)
apFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlood.setStatus("current")
_ApBlockedProtocol_Type = TruthValue
_ApBlockedProtocol_Object = MibScalar
apBlockedProtocol = _ApBlockedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 1, 3),
    _ApBlockedProtocol_Type()
)
apBlockedProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedProtocol.setStatus("current")
_ApBlockedState_Type = TruthValue
_ApBlockedState_Object = MibScalar
apBlockedState = _ApBlockedState_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 1, 4),
    _ApBlockedState_Type()
)
apBlockedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedState.setStatus("current")
_ApIpAttack_Type = TruthValue
_ApIpAttack_Object = MibScalar
apIpAttack = _ApIpAttack_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 1, 5),
    _ApIpAttack_Type()
)
apIpAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpAttack.setStatus("current")
_ApTcpAttack_Type = TruthValue
_ApTcpAttack_Object = MibScalar
apTcpAttack = _ApTcpAttack_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 1, 6),
    _ApTcpAttack_Type()
)
apTcpAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTcpAttack.setStatus("current")
_ApUdpAttack_Type = TruthValue
_ApUdpAttack_Object = MibScalar
apUdpAttack = _ApUdpAttack_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 1, 7),
    _ApUdpAttack_Type()
)
apUdpAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUdpAttack.setStatus("current")
_ApIcmpAttack_Type = TruthValue
_ApIcmpAttack_Object = MibScalar
apIcmpAttack = _ApIcmpAttack_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 1, 8),
    _ApIcmpAttack_Type()
)
apIcmpAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIcmpAttack.setStatus("current")
_ApOtherIpAttack_Type = TruthValue
_ApOtherIpAttack_Object = MibScalar
apOtherIpAttack = _ApOtherIpAttack_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 1, 9),
    _ApOtherIpAttack_Type()
)
apOtherIpAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOtherIpAttack.setStatus("current")
_ApFragAttack_Type = TruthValue
_ApFragAttack_Object = MibScalar
apFragAttack = _ApFragAttack_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 1, 10),
    _ApFragAttack_Type()
)
apFragAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFragAttack.setStatus("current")
_ApBadIp_Type = TruthValue
_ApBadIp_Object = MibScalar
apBadIp = _ApBadIp_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 1, 11),
    _ApBadIp_Type()
)
apBadIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadIp.setStatus("current")
_ApBadTcp_Type = TruthValue
_ApBadTcp_Object = MibScalar
apBadTcp = _ApBadTcp_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 1, 12),
    _ApBadTcp_Type()
)
apBadTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadTcp.setStatus("current")
_ApBadUdp_Type = TruthValue
_ApBadUdp_Object = MibScalar
apBadUdp = _ApBadUdp_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 1, 13),
    _ApBadUdp_Type()
)
apBadUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadUdp.setStatus("current")
_ApBadIcmp_Type = TruthValue
_ApBadIcmp_Object = MibScalar
apBadIcmp = _ApBadIcmp_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 1, 14),
    _ApBadIcmp_Type()
)
apBadIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadIcmp.setStatus("current")
_ApBadOtherIp_Type = TruthValue
_ApBadOtherIp_Object = MibScalar
apBadOtherIp = _ApBadOtherIp_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 1, 15),
    _ApBadOtherIp_Type()
)
apBadOtherIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBadOtherIp.setStatus("current")
_ApOverloadedIp_Type = TruthValue
_ApOverloadedIp_Object = MibScalar
apOverloadedIp = _ApOverloadedIp_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 1, 16),
    _ApOverloadedIp_Type()
)
apOverloadedIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOverloadedIp.setStatus("current")
_ApTcpStates_ObjectIdentity = ObjectIdentity
apTcpStates = _ApTcpStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2)
)
_ApInSyn_Type = Counter32
_ApInSyn_Object = MibScalar
apInSyn = _ApInSyn_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1),
    _ApInSyn_Type()
)
apInSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInSyn.setStatus("current")
_ApOutSyn_Type = Counter32
_ApOutSyn_Object = MibScalar
apOutSyn = _ApOutSyn_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 2),
    _ApOutSyn_Type()
)
apOutSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutSyn.setStatus("current")
_ApInSynAck_Type = Counter32
_ApInSynAck_Object = MibScalar
apInSynAck = _ApInSynAck_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 3),
    _ApInSynAck_Type()
)
apInSynAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInSynAck.setStatus("current")
_ApOutSynAck_Type = Counter32
_ApOutSynAck_Object = MibScalar
apOutSynAck = _ApOutSynAck_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 4),
    _ApOutSynAck_Type()
)
apOutSynAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutSynAck.setStatus("current")
_ApInSynSyn_Type = Counter32
_ApInSynSyn_Object = MibScalar
apInSynSyn = _ApInSynSyn_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 5),
    _ApInSynSyn_Type()
)
apInSynSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInSynSyn.setStatus("current")
_ApOutSynSyn_Type = Counter32
_ApOutSynSyn_Object = MibScalar
apOutSynSyn = _ApOutSynSyn_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 6),
    _ApOutSynSyn_Type()
)
apOutSynSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutSynSyn.setStatus("current")
_ApInEst_Type = Counter32
_ApInEst_Object = MibScalar
apInEst = _ApInEst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 7),
    _ApInEst_Type()
)
apInEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInEst.setStatus("current")
_ApOutEst_Type = Counter32
_ApOutEst_Object = MibScalar
apOutEst = _ApOutEst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 8),
    _ApOutEst_Type()
)
apOutEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutEst.setStatus("current")
_ApInFin1Src_Type = Counter32
_ApInFin1Src_Object = MibScalar
apInFin1Src = _ApInFin1Src_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 9),
    _ApInFin1Src_Type()
)
apInFin1Src.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInFin1Src.setStatus("current")
_ApOutFin1Src_Type = Counter32
_ApOutFin1Src_Object = MibScalar
apOutFin1Src = _ApOutFin1Src_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 10),
    _ApOutFin1Src_Type()
)
apOutFin1Src.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutFin1Src.setStatus("current")
_ApInFin2Src_Type = Counter32
_ApInFin2Src_Object = MibScalar
apInFin2Src = _ApInFin2Src_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 11),
    _ApInFin2Src_Type()
)
apInFin2Src.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInFin2Src.setStatus("current")
_ApOutFin2Src_Type = Counter32
_ApOutFin2Src_Object = MibScalar
apOutFin2Src = _ApOutFin2Src_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 12),
    _ApOutFin2Src_Type()
)
apOutFin2Src.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutFin2Src.setStatus("current")
_ApInFin3Src_Type = Counter32
_ApInFin3Src_Object = MibScalar
apInFin3Src = _ApInFin3Src_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 13),
    _ApInFin3Src_Type()
)
apInFin3Src.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInFin3Src.setStatus("current")
_ApOutFin3Src_Type = Counter32
_ApOutFin3Src_Object = MibScalar
apOutFin3Src = _ApOutFin3Src_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 14),
    _ApOutFin3Src_Type()
)
apOutFin3Src.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutFin3Src.setStatus("current")
_ApInFinFin_Type = Counter32
_ApInFinFin_Object = MibScalar
apInFinFin = _ApInFinFin_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 15),
    _ApInFinFin_Type()
)
apInFinFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInFinFin.setStatus("current")
_ApOutFinFin_Type = Counter32
_ApOutFinFin_Object = MibScalar
apOutFinFin = _ApOutFinFin_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 16),
    _ApOutFinFin_Type()
)
apOutFinFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutFinFin.setStatus("current")
_ApInFin1Dst_Type = Counter32
_ApInFin1Dst_Object = MibScalar
apInFin1Dst = _ApInFin1Dst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 17),
    _ApInFin1Dst_Type()
)
apInFin1Dst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInFin1Dst.setStatus("current")
_ApOutFin1Dst_Type = Counter32
_ApOutFin1Dst_Object = MibScalar
apOutFin1Dst = _ApOutFin1Dst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 18),
    _ApOutFin1Dst_Type()
)
apOutFin1Dst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutFin1Dst.setStatus("current")
_ApInFin2Dst_Type = Counter32
_ApInFin2Dst_Object = MibScalar
apInFin2Dst = _ApInFin2Dst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 19),
    _ApInFin2Dst_Type()
)
apInFin2Dst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInFin2Dst.setStatus("current")
_ApOutFin2Dst_Type = Counter32
_ApOutFin2Dst_Object = MibScalar
apOutFin2Dst = _ApOutFin2Dst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 20),
    _ApOutFin2Dst_Type()
)
apOutFin2Dst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutFin2Dst.setStatus("current")
_ApInFin3Dst_Type = Counter32
_ApInFin3Dst_Object = MibScalar
apInFin3Dst = _ApInFin3Dst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 21),
    _ApInFin3Dst_Type()
)
apInFin3Dst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInFin3Dst.setStatus("current")
_ApOutFin3Dst_Type = Counter32
_ApOutFin3Dst_Object = MibScalar
apOutFin3Dst = _ApOutFin3Dst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 22),
    _ApOutFin3Dst_Type()
)
apOutFin3Dst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutFin3Dst.setStatus("current")
_ApInCls_Type = Counter32
_ApInCls_Object = MibScalar
apInCls = _ApInCls_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 23),
    _ApInCls_Type()
)
apInCls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInCls.setStatus("current")
_ApOutCls_Type = Counter32
_ApOutCls_Object = MibScalar
apOutCls = _ApOutCls_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 24),
    _ApOutCls_Type()
)
apOutCls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutCls.setStatus("current")
_ApInRst_Type = Counter32
_ApInRst_Object = MibScalar
apInRst = _ApInRst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 25),
    _ApInRst_Type()
)
apInRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInRst.setStatus("current")
_ApOutRst_Type = Counter32
_ApOutRst_Object = MibScalar
apOutRst = _ApOutRst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 26),
    _ApOutRst_Type()
)
apOutRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutRst.setStatus("current")
_ApInRstCls_Type = Counter32
_ApInRstCls_Object = MibScalar
apInRstCls = _ApInRstCls_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 27),
    _ApInRstCls_Type()
)
apInRstCls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInRstCls.setStatus("current")
_ApOutRstCls_Type = Counter32
_ApOutRstCls_Object = MibScalar
apOutRstCls = _ApOutRstCls_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 28),
    _ApOutRstCls_Type()
)
apOutRstCls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutRstCls.setStatus("current")
_ApInUnknown_Type = Counter32
_ApInUnknown_Object = MibScalar
apInUnknown = _ApInUnknown_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 29),
    _ApInUnknown_Type()
)
apInUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInUnknown.setStatus("current")
_ApOutUnknown_Type = Counter32
_ApOutUnknown_Object = MibScalar
apOutUnknown = _ApOutUnknown_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 30),
    _ApOutUnknown_Type()
)
apOutUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutUnknown.setStatus("current")
_ApInAck_Type = Counter32
_ApInAck_Object = MibScalar
apInAck = _ApInAck_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 31),
    _ApInAck_Type()
)
apInAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInAck.setStatus("current")
_ApOutAck_Type = Counter32
_ApOutAck_Object = MibScalar
apOutAck = _ApOutAck_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 32),
    _ApOutAck_Type()
)
apOutAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutAck.setStatus("current")
_ApInPendAck_Type = Counter32
_ApInPendAck_Object = MibScalar
apInPendAck = _ApInPendAck_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 33),
    _ApInPendAck_Type()
)
apInPendAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInPendAck.setStatus("current")
_ApOutPendAck_Type = Counter32
_ApOutPendAck_Object = MibScalar
apOutPendAck = _ApOutPendAck_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 34),
    _ApOutPendAck_Type()
)
apOutPendAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutPendAck.setStatus("current")
_ApInGet_Type = Counter32
_ApInGet_Object = MibScalar
apInGet = _ApInGet_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 35),
    _ApInGet_Type()
)
apInGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInGet.setStatus("current")
_ApOutGet_Type = Counter32
_ApOutGet_Object = MibScalar
apOutGet = _ApOutGet_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 36),
    _ApOutGet_Type()
)
apOutGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutGet.setStatus("current")
_ApInGets_Type = Counter32
_ApInGets_Object = MibScalar
apInGets = _ApInGets_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 37),
    _ApInGets_Type()
)
apInGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInGets.setStatus("current")
_ApOutGets_Type = Counter32
_ApOutGets_Object = MibScalar
apOutGets = _ApOutGets_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 38),
    _ApOutGets_Type()
)
apOutGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutGets.setStatus("current")
_ApInTotalBpsAvg_Type = Gauge32
_ApInTotalBpsAvg_Object = MibScalar
apInTotalBpsAvg = _ApInTotalBpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 901),
    _ApInTotalBpsAvg_Type()
)
apInTotalBpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInTotalBpsAvg.setStatus("current")
_ApOutTotalBpsAvg_Type = Gauge32
_ApOutTotalBpsAvg_Object = MibScalar
apOutTotalBpsAvg = _ApOutTotalBpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 902),
    _ApOutTotalBpsAvg_Type()
)
apOutTotalBpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutTotalBpsAvg.setStatus("current")
_ApInTotalPpsAvg_Type = Gauge32
_ApInTotalPpsAvg_Object = MibScalar
apInTotalPpsAvg = _ApInTotalPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 903),
    _ApInTotalPpsAvg_Type()
)
apInTotalPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInTotalPpsAvg.setStatus("current")
_ApOutTotalPpsAvg_Type = Gauge32
_ApOutTotalPpsAvg_Object = MibScalar
apOutTotalPpsAvg = _ApOutTotalPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 904),
    _ApOutTotalPpsAvg_Type()
)
apOutTotalPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutTotalPpsAvg.setStatus("current")
_ApInSmallPpsAvg_Type = Gauge32
_ApInSmallPpsAvg_Object = MibScalar
apInSmallPpsAvg = _ApInSmallPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 905),
    _ApInSmallPpsAvg_Type()
)
apInSmallPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInSmallPpsAvg.setStatus("current")
_ApOutSmallPpsAvg_Type = Gauge32
_ApOutSmallPpsAvg_Object = MibScalar
apOutSmallPpsAvg = _ApOutSmallPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 906),
    _ApOutSmallPpsAvg_Type()
)
apOutSmallPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutSmallPpsAvg.setStatus("current")
_ApInMediumPpsAvg_Type = Gauge32
_ApInMediumPpsAvg_Object = MibScalar
apInMediumPpsAvg = _ApInMediumPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 907),
    _ApInMediumPpsAvg_Type()
)
apInMediumPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInMediumPpsAvg.setStatus("current")
_ApOutMediumPpsAvg_Type = Gauge32
_ApOutMediumPpsAvg_Object = MibScalar
apOutMediumPpsAvg = _ApOutMediumPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 908),
    _ApOutMediumPpsAvg_Type()
)
apOutMediumPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutMediumPpsAvg.setStatus("current")
_ApInLargePpsAvg_Type = Gauge32
_ApInLargePpsAvg_Object = MibScalar
apInLargePpsAvg = _ApInLargePpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 909),
    _ApInLargePpsAvg_Type()
)
apInLargePpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInLargePpsAvg.setStatus("current")
_ApOutLargePpsAvg_Type = Gauge32
_ApOutLargePpsAvg_Object = MibScalar
apOutLargePpsAvg = _ApOutLargePpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 910),
    _ApOutLargePpsAvg_Type()
)
apOutLargePpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutLargePpsAvg.setStatus("current")
_ApInDroppedBpsAvg_Type = Gauge32
_ApInDroppedBpsAvg_Object = MibScalar
apInDroppedBpsAvg = _ApInDroppedBpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 911),
    _ApInDroppedBpsAvg_Type()
)
apInDroppedBpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInDroppedBpsAvg.setStatus("current")
_ApOutDroppedBpsAvg_Type = Gauge32
_ApOutDroppedBpsAvg_Object = MibScalar
apOutDroppedBpsAvg = _ApOutDroppedBpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 912),
    _ApOutDroppedBpsAvg_Type()
)
apOutDroppedBpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutDroppedBpsAvg.setStatus("current")
_ApInDroppedPpsAvg_Type = Gauge32
_ApInDroppedPpsAvg_Object = MibScalar
apInDroppedPpsAvg = _ApInDroppedPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 913),
    _ApInDroppedPpsAvg_Type()
)
apInDroppedPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInDroppedPpsAvg.setStatus("current")
_ApOutDroppedPpsAvg_Type = Gauge32
_ApOutDroppedPpsAvg_Object = MibScalar
apOutDroppedPpsAvg = _ApOutDroppedPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 914),
    _ApOutDroppedPpsAvg_Type()
)
apOutDroppedPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutDroppedPpsAvg.setStatus("current")
_ApInCharmDroppedBpsAvg_Type = Gauge32
_ApInCharmDroppedBpsAvg_Object = MibScalar
apInCharmDroppedBpsAvg = _ApInCharmDroppedBpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 915),
    _ApInCharmDroppedBpsAvg_Type()
)
apInCharmDroppedBpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInCharmDroppedBpsAvg.setStatus("current")
_ApOutCharmDroppedBpsAvg_Type = Gauge32
_ApOutCharmDroppedBpsAvg_Object = MibScalar
apOutCharmDroppedBpsAvg = _ApOutCharmDroppedBpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 916),
    _ApOutCharmDroppedBpsAvg_Type()
)
apOutCharmDroppedBpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutCharmDroppedBpsAvg.setStatus("current")
_ApInFilteredBwthPercentAvg_Type = Gauge32
_ApInFilteredBwthPercentAvg_Object = MibScalar
apInFilteredBwthPercentAvg = _ApInFilteredBwthPercentAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 917),
    _ApInFilteredBwthPercentAvg_Type()
)
apInFilteredBwthPercentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInFilteredBwthPercentAvg.setStatus("current")
_ApOutFilteredBwthPercentAvg_Type = Gauge32
_ApOutFilteredBwthPercentAvg_Object = MibScalar
apOutFilteredBwthPercentAvg = _ApOutFilteredBwthPercentAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 918),
    _ApOutFilteredBwthPercentAvg_Type()
)
apOutFilteredBwthPercentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutFilteredBwthPercentAvg.setStatus("current")
_ApInSynbacklogtallyAvg_Type = Gauge32
_ApInSynbacklogtallyAvg_Object = MibScalar
apInSynbacklogtallyAvg = _ApInSynbacklogtallyAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 919),
    _ApInSynbacklogtallyAvg_Type()
)
apInSynbacklogtallyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInSynbacklogtallyAvg.setStatus("current")
_ApOutSynbacklogtallyAvg_Type = Gauge32
_ApOutSynbacklogtallyAvg_Object = MibScalar
apOutSynbacklogtallyAvg = _ApOutSynbacklogtallyAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 920),
    _ApOutSynbacklogtallyAvg_Type()
)
apOutSynbacklogtallyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutSynbacklogtallyAvg.setStatus("current")
_ApInConnectionAvg_Type = Gauge32
_ApInConnectionAvg_Object = MibScalar
apInConnectionAvg = _ApInConnectionAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 921),
    _ApInConnectionAvg_Type()
)
apInConnectionAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInConnectionAvg.setStatus("current")
_ApOutConnectionAvg_Type = Gauge32
_ApOutConnectionAvg_Object = MibScalar
apOutConnectionAvg = _ApOutConnectionAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 922),
    _ApOutConnectionAvg_Type()
)
apOutConnectionAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutConnectionAvg.setStatus("current")
_ApInConnreqAvg_Type = Gauge32
_ApInConnreqAvg_Object = MibScalar
apInConnreqAvg = _ApInConnreqAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 923),
    _ApInConnreqAvg_Type()
)
apInConnreqAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInConnreqAvg.setStatus("current")
_ApOutConnreqAvg_Type = Gauge32
_ApOutConnreqAvg_Object = MibScalar
apOutConnreqAvg = _ApOutConnreqAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 924),
    _ApOutConnreqAvg_Type()
)
apOutConnreqAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutConnreqAvg.setStatus("current")
_ApInActiveHttpGetsAvg_Type = Gauge32
_ApInActiveHttpGetsAvg_Object = MibScalar
apInActiveHttpGetsAvg = _ApInActiveHttpGetsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 925),
    _ApInActiveHttpGetsAvg_Type()
)
apInActiveHttpGetsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInActiveHttpGetsAvg.setStatus("current")
_ApOutActiveHttpGetsAvg_Type = Gauge32
_ApOutActiveHttpGetsAvg_Object = MibScalar
apOutActiveHttpGetsAvg = _ApOutActiveHttpGetsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 926),
    _ApOutActiveHttpGetsAvg_Type()
)
apOutActiveHttpGetsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutActiveHttpGetsAvg.setStatus("current")
_ApInProtectBwthPktsAvg_Type = Gauge32
_ApInProtectBwthPktsAvg_Object = MibScalar
apInProtectBwthPktsAvg = _ApInProtectBwthPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 927),
    _ApInProtectBwthPktsAvg_Type()
)
apInProtectBwthPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInProtectBwthPktsAvg.setStatus("current")
_ApOutProtectBwthPktsAvg_Type = Gauge32
_ApOutProtectBwthPktsAvg_Object = MibScalar
apOutProtectBwthPktsAvg = _ApOutProtectBwthPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 928),
    _ApOutProtectBwthPktsAvg_Type()
)
apOutProtectBwthPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutProtectBwthPktsAvg.setStatus("current")
_ApInFloodPktsAvg_Type = Gauge32
_ApInFloodPktsAvg_Object = MibScalar
apInFloodPktsAvg = _ApInFloodPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 929),
    _ApInFloodPktsAvg_Type()
)
apInFloodPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInFloodPktsAvg.setStatus("current")
_ApOutFloodPktsAvg_Type = Gauge32
_ApOutFloodPktsAvg_Object = MibScalar
apOutFloodPktsAvg = _ApOutFloodPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 930),
    _ApOutFloodPktsAvg_Type()
)
apOutFloodPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutFloodPktsAvg.setStatus("current")
_ApInBlockedProtocolPktsAvg_Type = Gauge32
_ApInBlockedProtocolPktsAvg_Object = MibScalar
apInBlockedProtocolPktsAvg = _ApInBlockedProtocolPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 931),
    _ApInBlockedProtocolPktsAvg_Type()
)
apInBlockedProtocolPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBlockedProtocolPktsAvg.setStatus("current")
_ApOutBlockedProtocolPktsAvg_Type = Gauge32
_ApOutBlockedProtocolPktsAvg_Object = MibScalar
apOutBlockedProtocolPktsAvg = _ApOutBlockedProtocolPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 932),
    _ApOutBlockedProtocolPktsAvg_Type()
)
apOutBlockedProtocolPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBlockedProtocolPktsAvg.setStatus("current")
_ApInBlockedStatePktsAvg_Type = Gauge32
_ApInBlockedStatePktsAvg_Object = MibScalar
apInBlockedStatePktsAvg = _ApInBlockedStatePktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 933),
    _ApInBlockedStatePktsAvg_Type()
)
apInBlockedStatePktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBlockedStatePktsAvg.setStatus("current")
_ApOutBlockedStatePktsAvg_Type = Gauge32
_ApOutBlockedStatePktsAvg_Object = MibScalar
apOutBlockedStatePktsAvg = _ApOutBlockedStatePktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 934),
    _ApOutBlockedStatePktsAvg_Type()
)
apOutBlockedStatePktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBlockedStatePktsAvg.setStatus("current")
_ApInIpAttackPktsAvg_Type = Gauge32
_ApInIpAttackPktsAvg_Object = MibScalar
apInIpAttackPktsAvg = _ApInIpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 935),
    _ApInIpAttackPktsAvg_Type()
)
apInIpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInIpAttackPktsAvg.setStatus("current")
_ApOutIpAttackPktsAvg_Type = Gauge32
_ApOutIpAttackPktsAvg_Object = MibScalar
apOutIpAttackPktsAvg = _ApOutIpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 936),
    _ApOutIpAttackPktsAvg_Type()
)
apOutIpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutIpAttackPktsAvg.setStatus("current")
_ApInTcpAttackPktsAvg_Type = Gauge32
_ApInTcpAttackPktsAvg_Object = MibScalar
apInTcpAttackPktsAvg = _ApInTcpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 937),
    _ApInTcpAttackPktsAvg_Type()
)
apInTcpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInTcpAttackPktsAvg.setStatus("current")
_ApOutTcpAttackPktsAvg_Type = Gauge32
_ApOutTcpAttackPktsAvg_Object = MibScalar
apOutTcpAttackPktsAvg = _ApOutTcpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 938),
    _ApOutTcpAttackPktsAvg_Type()
)
apOutTcpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutTcpAttackPktsAvg.setStatus("current")
_ApInUdpAttackPktsAvg_Type = Gauge32
_ApInUdpAttackPktsAvg_Object = MibScalar
apInUdpAttackPktsAvg = _ApInUdpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 939),
    _ApInUdpAttackPktsAvg_Type()
)
apInUdpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInUdpAttackPktsAvg.setStatus("current")
_ApOutUdpAttackPktsAvg_Type = Gauge32
_ApOutUdpAttackPktsAvg_Object = MibScalar
apOutUdpAttackPktsAvg = _ApOutUdpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 940),
    _ApOutUdpAttackPktsAvg_Type()
)
apOutUdpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutUdpAttackPktsAvg.setStatus("current")
_ApInIcmpAttackPktsAvg_Type = Gauge32
_ApInIcmpAttackPktsAvg_Object = MibScalar
apInIcmpAttackPktsAvg = _ApInIcmpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 941),
    _ApInIcmpAttackPktsAvg_Type()
)
apInIcmpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInIcmpAttackPktsAvg.setStatus("current")
_ApOutIcmpAttackPktsAvg_Type = Gauge32
_ApOutIcmpAttackPktsAvg_Object = MibScalar
apOutIcmpAttackPktsAvg = _ApOutIcmpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 942),
    _ApOutIcmpAttackPktsAvg_Type()
)
apOutIcmpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutIcmpAttackPktsAvg.setStatus("current")
_ApInOtherIpAttackPktsAvg_Type = Gauge32
_ApInOtherIpAttackPktsAvg_Object = MibScalar
apInOtherIpAttackPktsAvg = _ApInOtherIpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 943),
    _ApInOtherIpAttackPktsAvg_Type()
)
apInOtherIpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInOtherIpAttackPktsAvg.setStatus("current")
_ApOutOtherIpAttackPktsAvg_Type = Gauge32
_ApOutOtherIpAttackPktsAvg_Object = MibScalar
apOutOtherIpAttackPktsAvg = _ApOutOtherIpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 944),
    _ApOutOtherIpAttackPktsAvg_Type()
)
apOutOtherIpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutOtherIpAttackPktsAvg.setStatus("current")
_ApInFragmentAttackPktsAvg_Type = Gauge32
_ApInFragmentAttackPktsAvg_Object = MibScalar
apInFragmentAttackPktsAvg = _ApInFragmentAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 945),
    _ApInFragmentAttackPktsAvg_Type()
)
apInFragmentAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInFragmentAttackPktsAvg.setStatus("current")
_ApOutFragmentAttackPktsAvg_Type = Gauge32
_ApOutFragmentAttackPktsAvg_Object = MibScalar
apOutFragmentAttackPktsAvg = _ApOutFragmentAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 946),
    _ApOutFragmentAttackPktsAvg_Type()
)
apOutFragmentAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutFragmentAttackPktsAvg.setStatus("current")
_ApInBadipPktsAvg_Type = Gauge32
_ApInBadipPktsAvg_Object = MibScalar
apInBadipPktsAvg = _ApInBadipPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 947),
    _ApInBadipPktsAvg_Type()
)
apInBadipPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBadipPktsAvg.setStatus("current")
_ApOutBadipPktsAvg_Type = Gauge32
_ApOutBadipPktsAvg_Object = MibScalar
apOutBadipPktsAvg = _ApOutBadipPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 948),
    _ApOutBadipPktsAvg_Type()
)
apOutBadipPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBadipPktsAvg.setStatus("current")
_ApInBadTcpPktsAvg_Type = Gauge32
_ApInBadTcpPktsAvg_Object = MibScalar
apInBadTcpPktsAvg = _ApInBadTcpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 949),
    _ApInBadTcpPktsAvg_Type()
)
apInBadTcpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBadTcpPktsAvg.setStatus("current")
_ApOutBadTcpPktsAvg_Type = Gauge32
_ApOutBadTcpPktsAvg_Object = MibScalar
apOutBadTcpPktsAvg = _ApOutBadTcpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 950),
    _ApOutBadTcpPktsAvg_Type()
)
apOutBadTcpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBadTcpPktsAvg.setStatus("current")
_ApInBadUdpPktsAvg_Type = Gauge32
_ApInBadUdpPktsAvg_Object = MibScalar
apInBadUdpPktsAvg = _ApInBadUdpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 951),
    _ApInBadUdpPktsAvg_Type()
)
apInBadUdpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBadUdpPktsAvg.setStatus("current")
_ApOutBadUdpPktsAvg_Type = Gauge32
_ApOutBadUdpPktsAvg_Object = MibScalar
apOutBadUdpPktsAvg = _ApOutBadUdpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 952),
    _ApOutBadUdpPktsAvg_Type()
)
apOutBadUdpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBadUdpPktsAvg.setStatus("current")
_ApInBadIcmpPktsAvg_Type = Gauge32
_ApInBadIcmpPktsAvg_Object = MibScalar
apInBadIcmpPktsAvg = _ApInBadIcmpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 953),
    _ApInBadIcmpPktsAvg_Type()
)
apInBadIcmpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBadIcmpPktsAvg.setStatus("current")
_ApOutBadIcmpPktsAvg_Type = Gauge32
_ApOutBadIcmpPktsAvg_Object = MibScalar
apOutBadIcmpPktsAvg = _ApOutBadIcmpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 954),
    _ApOutBadIcmpPktsAvg_Type()
)
apOutBadIcmpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBadIcmpPktsAvg.setStatus("current")
_ApInBadOtherIpPktsAvg_Type = Gauge32
_ApInBadOtherIpPktsAvg_Object = MibScalar
apInBadOtherIpPktsAvg = _ApInBadOtherIpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 955),
    _ApInBadOtherIpPktsAvg_Type()
)
apInBadOtherIpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBadOtherIpPktsAvg.setStatus("current")
_ApOutBadOtherIpPktsAvg_Type = Gauge32
_ApOutBadOtherIpPktsAvg_Object = MibScalar
apOutBadOtherIpPktsAvg = _ApOutBadOtherIpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 956),
    _ApOutBadOtherIpPktsAvg_Type()
)
apOutBadOtherIpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBadOtherIpPktsAvg.setStatus("current")
_ApInOverloadedAvg_Type = Gauge32
_ApInOverloadedAvg_Object = MibScalar
apInOverloadedAvg = _ApInOverloadedAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 957),
    _ApInOverloadedAvg_Type()
)
apInOverloadedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInOverloadedAvg.setStatus("current")
_ApOutOverloadedAvg_Type = Gauge32
_ApOutOverloadedAvg_Object = MibScalar
apOutOverloadedAvg = _ApOutOverloadedAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 958),
    _ApOutOverloadedAvg_Type()
)
apOutOverloadedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutOverloadedAvg.setStatus("current")
_ApInLatencyAvg_Type = Gauge32
_ApInLatencyAvg_Object = MibScalar
apInLatencyAvg = _ApInLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 959),
    _ApInLatencyAvg_Type()
)
apInLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInLatencyAvg.setStatus("current")
_ApOutLatencyAvg_Type = Gauge32
_ApOutLatencyAvg_Object = MibScalar
apOutLatencyAvg = _ApOutLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 960),
    _ApOutLatencyAvg_Type()
)
apOutLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutLatencyAvg.setStatus("current")
_ApInSmallPpsMax_Type = Gauge32
_ApInSmallPpsMax_Object = MibScalar
apInSmallPpsMax = _ApInSmallPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1001),
    _ApInSmallPpsMax_Type()
)
apInSmallPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInSmallPpsMax.setStatus("current")
_ApOutSmallPpsMax_Type = Gauge32
_ApOutSmallPpsMax_Object = MibScalar
apOutSmallPpsMax = _ApOutSmallPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1002),
    _ApOutSmallPpsMax_Type()
)
apOutSmallPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutSmallPpsMax.setStatus("current")
_ApInMediumPpsMax_Type = Gauge32
_ApInMediumPpsMax_Object = MibScalar
apInMediumPpsMax = _ApInMediumPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1003),
    _ApInMediumPpsMax_Type()
)
apInMediumPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInMediumPpsMax.setStatus("current")
_ApOutMediumPpsMax_Type = Gauge32
_ApOutMediumPpsMax_Object = MibScalar
apOutMediumPpsMax = _ApOutMediumPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1004),
    _ApOutMediumPpsMax_Type()
)
apOutMediumPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutMediumPpsMax.setStatus("current")
_ApInLargePpsMax_Type = Gauge32
_ApInLargePpsMax_Object = MibScalar
apInLargePpsMax = _ApInLargePpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1005),
    _ApInLargePpsMax_Type()
)
apInLargePpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInLargePpsMax.setStatus("current")
_ApOutLargePpsMax_Type = Gauge32
_ApOutLargePpsMax_Object = MibScalar
apOutLargePpsMax = _ApOutLargePpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1006),
    _ApOutLargePpsMax_Type()
)
apOutLargePpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutLargePpsMax.setStatus("current")
_ApInFilteredBwthPercentMax_Type = Gauge32
_ApInFilteredBwthPercentMax_Object = MibScalar
apInFilteredBwthPercentMax = _ApInFilteredBwthPercentMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1007),
    _ApInFilteredBwthPercentMax_Type()
)
apInFilteredBwthPercentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInFilteredBwthPercentMax.setStatus("current")
_ApOutFilteredBwthPercentMax_Type = Gauge32
_ApOutFilteredBwthPercentMax_Object = MibScalar
apOutFilteredBwthPercentMax = _ApOutFilteredBwthPercentMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1008),
    _ApOutFilteredBwthPercentMax_Type()
)
apOutFilteredBwthPercentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutFilteredBwthPercentMax.setStatus("current")
_ApInSynbacklogtallyMax_Type = Gauge32
_ApInSynbacklogtallyMax_Object = MibScalar
apInSynbacklogtallyMax = _ApInSynbacklogtallyMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1009),
    _ApInSynbacklogtallyMax_Type()
)
apInSynbacklogtallyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInSynbacklogtallyMax.setStatus("current")
_ApOutSynbacklogtallyMax_Type = Gauge32
_ApOutSynbacklogtallyMax_Object = MibScalar
apOutSynbacklogtallyMax = _ApOutSynbacklogtallyMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1010),
    _ApOutSynbacklogtallyMax_Type()
)
apOutSynbacklogtallyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutSynbacklogtallyMax.setStatus("current")
_ApInConnectionMax_Type = Gauge32
_ApInConnectionMax_Object = MibScalar
apInConnectionMax = _ApInConnectionMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1011),
    _ApInConnectionMax_Type()
)
apInConnectionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInConnectionMax.setStatus("current")
_ApOutConnectionMax_Type = Gauge32
_ApOutConnectionMax_Object = MibScalar
apOutConnectionMax = _ApOutConnectionMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1012),
    _ApOutConnectionMax_Type()
)
apOutConnectionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutConnectionMax.setStatus("current")
_ApInConnreqMax_Type = Gauge32
_ApInConnreqMax_Object = MibScalar
apInConnreqMax = _ApInConnreqMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1013),
    _ApInConnreqMax_Type()
)
apInConnreqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInConnreqMax.setStatus("current")
_ApOutConnreqMax_Type = Gauge32
_ApOutConnreqMax_Object = MibScalar
apOutConnreqMax = _ApOutConnreqMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1014),
    _ApOutConnreqMax_Type()
)
apOutConnreqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutConnreqMax.setStatus("current")
_ApInActiveHttpGetsMax_Type = Gauge32
_ApInActiveHttpGetsMax_Object = MibScalar
apInActiveHttpGetsMax = _ApInActiveHttpGetsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1015),
    _ApInActiveHttpGetsMax_Type()
)
apInActiveHttpGetsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInActiveHttpGetsMax.setStatus("current")
_ApOutActiveHttpGetsMax_Type = Gauge32
_ApOutActiveHttpGetsMax_Object = MibScalar
apOutActiveHttpGetsMax = _ApOutActiveHttpGetsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1016),
    _ApOutActiveHttpGetsMax_Type()
)
apOutActiveHttpGetsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutActiveHttpGetsMax.setStatus("current")
_ApInProtectBwthPktsMax_Type = Gauge32
_ApInProtectBwthPktsMax_Object = MibScalar
apInProtectBwthPktsMax = _ApInProtectBwthPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1017),
    _ApInProtectBwthPktsMax_Type()
)
apInProtectBwthPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInProtectBwthPktsMax.setStatus("current")
_ApOutProtectBwthPktsMax_Type = Gauge32
_ApOutProtectBwthPktsMax_Object = MibScalar
apOutProtectBwthPktsMax = _ApOutProtectBwthPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1018),
    _ApOutProtectBwthPktsMax_Type()
)
apOutProtectBwthPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutProtectBwthPktsMax.setStatus("current")
_ApInFloodPktsMax_Type = Gauge32
_ApInFloodPktsMax_Object = MibScalar
apInFloodPktsMax = _ApInFloodPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1019),
    _ApInFloodPktsMax_Type()
)
apInFloodPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInFloodPktsMax.setStatus("current")
_ApOutFloodPktsMax_Type = Gauge32
_ApOutFloodPktsMax_Object = MibScalar
apOutFloodPktsMax = _ApOutFloodPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1020),
    _ApOutFloodPktsMax_Type()
)
apOutFloodPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutFloodPktsMax.setStatus("current")
_ApInBlockedProtocolPktsMax_Type = Gauge32
_ApInBlockedProtocolPktsMax_Object = MibScalar
apInBlockedProtocolPktsMax = _ApInBlockedProtocolPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1021),
    _ApInBlockedProtocolPktsMax_Type()
)
apInBlockedProtocolPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBlockedProtocolPktsMax.setStatus("current")
_ApOutBlockedProtocolPktsMax_Type = Gauge32
_ApOutBlockedProtocolPktsMax_Object = MibScalar
apOutBlockedProtocolPktsMax = _ApOutBlockedProtocolPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1022),
    _ApOutBlockedProtocolPktsMax_Type()
)
apOutBlockedProtocolPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBlockedProtocolPktsMax.setStatus("current")
_ApInBlockedStatePktsMax_Type = Gauge32
_ApInBlockedStatePktsMax_Object = MibScalar
apInBlockedStatePktsMax = _ApInBlockedStatePktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1023),
    _ApInBlockedStatePktsMax_Type()
)
apInBlockedStatePktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBlockedStatePktsMax.setStatus("current")
_ApOutBlockedStatePktsMax_Type = Gauge32
_ApOutBlockedStatePktsMax_Object = MibScalar
apOutBlockedStatePktsMax = _ApOutBlockedStatePktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1024),
    _ApOutBlockedStatePktsMax_Type()
)
apOutBlockedStatePktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBlockedStatePktsMax.setStatus("current")
_ApInIpAttackPktsMax_Type = Gauge32
_ApInIpAttackPktsMax_Object = MibScalar
apInIpAttackPktsMax = _ApInIpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1025),
    _ApInIpAttackPktsMax_Type()
)
apInIpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInIpAttackPktsMax.setStatus("current")
_ApOutIpAttackPktsMax_Type = Gauge32
_ApOutIpAttackPktsMax_Object = MibScalar
apOutIpAttackPktsMax = _ApOutIpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1026),
    _ApOutIpAttackPktsMax_Type()
)
apOutIpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutIpAttackPktsMax.setStatus("current")
_ApInTcpAttackPktsMax_Type = Gauge32
_ApInTcpAttackPktsMax_Object = MibScalar
apInTcpAttackPktsMax = _ApInTcpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1027),
    _ApInTcpAttackPktsMax_Type()
)
apInTcpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInTcpAttackPktsMax.setStatus("current")
_ApOutTcpAttackPktsMax_Type = Gauge32
_ApOutTcpAttackPktsMax_Object = MibScalar
apOutTcpAttackPktsMax = _ApOutTcpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1028),
    _ApOutTcpAttackPktsMax_Type()
)
apOutTcpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutTcpAttackPktsMax.setStatus("current")
_ApInUdpAttackPktsMax_Type = Gauge32
_ApInUdpAttackPktsMax_Object = MibScalar
apInUdpAttackPktsMax = _ApInUdpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1029),
    _ApInUdpAttackPktsMax_Type()
)
apInUdpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInUdpAttackPktsMax.setStatus("current")
_ApOutUdpAttackPktsMax_Type = Gauge32
_ApOutUdpAttackPktsMax_Object = MibScalar
apOutUdpAttackPktsMax = _ApOutUdpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1030),
    _ApOutUdpAttackPktsMax_Type()
)
apOutUdpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutUdpAttackPktsMax.setStatus("current")
_ApInIcmpAttackPktsMax_Type = Gauge32
_ApInIcmpAttackPktsMax_Object = MibScalar
apInIcmpAttackPktsMax = _ApInIcmpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1031),
    _ApInIcmpAttackPktsMax_Type()
)
apInIcmpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInIcmpAttackPktsMax.setStatus("current")
_ApOutIcmpAttackPktsMax_Type = Gauge32
_ApOutIcmpAttackPktsMax_Object = MibScalar
apOutIcmpAttackPktsMax = _ApOutIcmpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1032),
    _ApOutIcmpAttackPktsMax_Type()
)
apOutIcmpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutIcmpAttackPktsMax.setStatus("current")
_ApInOtherIpAttackPktsMax_Type = Gauge32
_ApInOtherIpAttackPktsMax_Object = MibScalar
apInOtherIpAttackPktsMax = _ApInOtherIpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1033),
    _ApInOtherIpAttackPktsMax_Type()
)
apInOtherIpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInOtherIpAttackPktsMax.setStatus("current")
_ApOutOtherIpAttackPktsMax_Type = Gauge32
_ApOutOtherIpAttackPktsMax_Object = MibScalar
apOutOtherIpAttackPktsMax = _ApOutOtherIpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1034),
    _ApOutOtherIpAttackPktsMax_Type()
)
apOutOtherIpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutOtherIpAttackPktsMax.setStatus("current")
_ApInFragmentAttackPktsMax_Type = Gauge32
_ApInFragmentAttackPktsMax_Object = MibScalar
apInFragmentAttackPktsMax = _ApInFragmentAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1035),
    _ApInFragmentAttackPktsMax_Type()
)
apInFragmentAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInFragmentAttackPktsMax.setStatus("current")
_ApOutFragmentAttackPktsMax_Type = Gauge32
_ApOutFragmentAttackPktsMax_Object = MibScalar
apOutFragmentAttackPktsMax = _ApOutFragmentAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1036),
    _ApOutFragmentAttackPktsMax_Type()
)
apOutFragmentAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutFragmentAttackPktsMax.setStatus("current")
_ApInBadipPktsMax_Type = Gauge32
_ApInBadipPktsMax_Object = MibScalar
apInBadipPktsMax = _ApInBadipPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1037),
    _ApInBadipPktsMax_Type()
)
apInBadipPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBadipPktsMax.setStatus("current")
_ApOutBadipPktsMax_Type = Gauge32
_ApOutBadipPktsMax_Object = MibScalar
apOutBadipPktsMax = _ApOutBadipPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1038),
    _ApOutBadipPktsMax_Type()
)
apOutBadipPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBadipPktsMax.setStatus("current")
_ApInBadTcpPktsMax_Type = Gauge32
_ApInBadTcpPktsMax_Object = MibScalar
apInBadTcpPktsMax = _ApInBadTcpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1039),
    _ApInBadTcpPktsMax_Type()
)
apInBadTcpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBadTcpPktsMax.setStatus("current")
_ApOutBadTcpPktsMax_Type = Gauge32
_ApOutBadTcpPktsMax_Object = MibScalar
apOutBadTcpPktsMax = _ApOutBadTcpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1040),
    _ApOutBadTcpPktsMax_Type()
)
apOutBadTcpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBadTcpPktsMax.setStatus("current")
_ApInBadUdpPktsMax_Type = Gauge32
_ApInBadUdpPktsMax_Object = MibScalar
apInBadUdpPktsMax = _ApInBadUdpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1041),
    _ApInBadUdpPktsMax_Type()
)
apInBadUdpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBadUdpPktsMax.setStatus("current")
_ApOutBadUdpPktsMax_Type = Gauge32
_ApOutBadUdpPktsMax_Object = MibScalar
apOutBadUdpPktsMax = _ApOutBadUdpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1042),
    _ApOutBadUdpPktsMax_Type()
)
apOutBadUdpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBadUdpPktsMax.setStatus("current")
_ApInBadIcmpPktsMax_Type = Gauge32
_ApInBadIcmpPktsMax_Object = MibScalar
apInBadIcmpPktsMax = _ApInBadIcmpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1043),
    _ApInBadIcmpPktsMax_Type()
)
apInBadIcmpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBadIcmpPktsMax.setStatus("current")
_ApOutBadIcmpPktsMax_Type = Gauge32
_ApOutBadIcmpPktsMax_Object = MibScalar
apOutBadIcmpPktsMax = _ApOutBadIcmpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1044),
    _ApOutBadIcmpPktsMax_Type()
)
apOutBadIcmpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBadIcmpPktsMax.setStatus("current")
_ApInBadOtherIpPktsMax_Type = Gauge32
_ApInBadOtherIpPktsMax_Object = MibScalar
apInBadOtherIpPktsMax = _ApInBadOtherIpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1045),
    _ApInBadOtherIpPktsMax_Type()
)
apInBadOtherIpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBadOtherIpPktsMax.setStatus("current")
_ApOutBadOtherIpPktsMax_Type = Gauge32
_ApOutBadOtherIpPktsMax_Object = MibScalar
apOutBadOtherIpPktsMax = _ApOutBadOtherIpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1046),
    _ApOutBadOtherIpPktsMax_Type()
)
apOutBadOtherIpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBadOtherIpPktsMax.setStatus("current")
_ApInOverloadedMax_Type = Gauge32
_ApInOverloadedMax_Object = MibScalar
apInOverloadedMax = _ApInOverloadedMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1047),
    _ApInOverloadedMax_Type()
)
apInOverloadedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInOverloadedMax.setStatus("current")
_ApOutOverloadedMax_Type = Gauge32
_ApOutOverloadedMax_Object = MibScalar
apOutOverloadedMax = _ApOutOverloadedMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1048),
    _ApOutOverloadedMax_Type()
)
apOutOverloadedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutOverloadedMax.setStatus("current")
_ApInLatencyMax_Type = Gauge32
_ApInLatencyMax_Object = MibScalar
apInLatencyMax = _ApInLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1049),
    _ApInLatencyMax_Type()
)
apInLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInLatencyMax.setStatus("current")
_ApOutLatencyMax_Type = Gauge32
_ApOutLatencyMax_Object = MibScalar
apOutLatencyMax = _ApOutLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 2, 1050),
    _ApOutLatencyMax_Type()
)
apOutLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutLatencyMax.setStatus("current")
_ApIfStates_ObjectIdentity = ObjectIdentity
apIfStates = _ApIfStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 3)
)
_ApMgmtIfLinkModeState_Type = DisplayString
_ApMgmtIfLinkModeState_Object = MibScalar
apMgmtIfLinkModeState = _ApMgmtIfLinkModeState_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 3, 1),
    _ApMgmtIfLinkModeState_Type()
)
apMgmtIfLinkModeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMgmtIfLinkModeState.setStatus("current")
_ApIntIfLinkModeState_Type = DisplayString
_ApIntIfLinkModeState_Object = MibScalar
apIntIfLinkModeState = _ApIntIfLinkModeState_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 3, 2),
    _ApIntIfLinkModeState_Type()
)
apIntIfLinkModeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIntIfLinkModeState.setStatus("current")
_ApProtIfLinkModeState_Type = DisplayString
_ApProtIfLinkModeState_Object = MibScalar
apProtIfLinkModeState = _ApProtIfLinkModeState_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 3, 3),
    _ApProtIfLinkModeState_Type()
)
apProtIfLinkModeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProtIfLinkModeState.setStatus("current")
_ApMgmtIfLinkFCState_Type = DisplayString
_ApMgmtIfLinkFCState_Object = MibScalar
apMgmtIfLinkFCState = _ApMgmtIfLinkFCState_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 3, 4),
    _ApMgmtIfLinkFCState_Type()
)
apMgmtIfLinkFCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMgmtIfLinkFCState.setStatus("current")
_ApIntIfLinkFCState_Type = DisplayString
_ApIntIfLinkFCState_Object = MibScalar
apIntIfLinkFCState = _ApIntIfLinkFCState_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 3, 5),
    _ApIntIfLinkFCState_Type()
)
apIntIfLinkFCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIntIfLinkFCState.setStatus("current")
_ApProtIfLinkFCState_Type = DisplayString
_ApProtIfLinkFCState_Object = MibScalar
apProtIfLinkFCState = _ApProtIfLinkFCState_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 3, 6),
    _ApProtIfLinkFCState_Type()
)
apProtIfLinkFCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProtIfLinkFCState.setStatus("current")
_ApHighAvailabilityInfo_ObjectIdentity = ObjectIdentity
apHighAvailabilityInfo = _ApHighAvailabilityInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 4)
)


class _ApHaState_Type(Integer32):
    """Custom type apHaState based on Integer32"""
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
        *(("unknown", 1),
          ("probe", 2),
          ("standby", 3),
          ("active", 4),
          ("cripple", 5),
          ("standalone", 6),
          ("activesec", 7))
    )


_ApHaState_Type.__name__ = "Integer32"
_ApHaState_Object = MibScalar
apHaState = _ApHaState_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 4, 1),
    _ApHaState_Type()
)
apHaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apHaState.setStatus("current")
_ApHaPartnerList_Type = DisplayString
_ApHaPartnerList_Object = MibScalar
apHaPartnerList = _ApHaPartnerList_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 4, 2),
    _ApHaPartnerList_Type()
)
apHaPartnerList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apHaPartnerList.setStatus("current")
_ApHaPartnerTime_Type = TimeInterval
_ApHaPartnerTime_Object = MibScalar
apHaPartnerTime = _ApHaPartnerTime_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 4, 3),
    _ApHaPartnerTime_Type()
)
apHaPartnerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apHaPartnerTime.setStatus("current")
_ApStalledFlag_Type = TruthValue
_ApStalledFlag_Object = MibScalar
apStalledFlag = _ApStalledFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 5),
    _ApStalledFlag_Type()
)
apStalledFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStalledFlag.setStatus("current")
_ApOutputErrorIIFlag_Type = TruthValue
_ApOutputErrorIIFlag_Object = MibScalar
apOutputErrorIIFlag = _ApOutputErrorIIFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 6),
    _ApOutputErrorIIFlag_Type()
)
apOutputErrorIIFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutputErrorIIFlag.setStatus("current")
_ApOutputErrorPIFlag_Type = TruthValue
_ApOutputErrorPIFlag_Object = MibScalar
apOutputErrorPIFlag = _ApOutputErrorPIFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 7),
    _ApOutputErrorPIFlag_Type()
)
apOutputErrorPIFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutputErrorPIFlag.setStatus("current")
_ApOutputErrorMIFlag_Type = TruthValue
_ApOutputErrorMIFlag_Object = MibScalar
apOutputErrorMIFlag = _ApOutputErrorMIFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 8),
    _ApOutputErrorMIFlag_Type()
)
apOutputErrorMIFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutputErrorMIFlag.setStatus("current")
_ApNewConfigFlag_Type = TruthValue
_ApNewConfigFlag_Object = MibScalar
apNewConfigFlag = _ApNewConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 9),
    _ApNewConfigFlag_Type()
)
apNewConfigFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNewConfigFlag.setStatus("current")
_ApNotLicensedFlag_Type = TruthValue
_ApNotLicensedFlag_Object = MibScalar
apNotLicensedFlag = _ApNotLicensedFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 10),
    _ApNotLicensedFlag_Type()
)
apNotLicensedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNotLicensedFlag.setStatus("current")
_ApMacTableFullFlag_Type = TruthValue
_ApMacTableFullFlag_Object = MibScalar
apMacTableFullFlag = _ApMacTableFullFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 11),
    _ApMacTableFullFlag_Type()
)
apMacTableFullFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMacTableFullFlag.setStatus("current")
_ApProtectedTableFullFlag_Type = TruthValue
_ApProtectedTableFullFlag_Object = MibScalar
apProtectedTableFullFlag = _ApProtectedTableFullFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 12),
    _ApProtectedTableFullFlag_Type()
)
apProtectedTableFullFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProtectedTableFullFlag.setStatus("current")
_ApIncidentTableFullFlag_Type = TruthValue
_ApIncidentTableFullFlag_Object = MibScalar
apIncidentTableFullFlag = _ApIncidentTableFullFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 13),
    _ApIncidentTableFullFlag_Type()
)
apIncidentTableFullFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIncidentTableFullFlag.setStatus("current")
_ApTcpTableFullFlag_Type = TruthValue
_ApTcpTableFullFlag_Object = MibScalar
apTcpTableFullFlag = _ApTcpTableFullFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 14),
    _ApTcpTableFullFlag_Type()
)
apTcpTableFullFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTcpTableFullFlag.setStatus("current")
_ApUdpTableFullFlag_Type = TruthValue
_ApUdpTableFullFlag_Object = MibScalar
apUdpTableFullFlag = _ApUdpTableFullFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 15),
    _ApUdpTableFullFlag_Type()
)
apUdpTableFullFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUdpTableFullFlag.setStatus("current")
_ApIcmpTableFullFlag_Type = TruthValue
_ApIcmpTableFullFlag_Object = MibScalar
apIcmpTableFullFlag = _ApIcmpTableFullFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 16),
    _ApIcmpTableFullFlag_Type()
)
apIcmpTableFullFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIcmpTableFullFlag.setStatus("current")
_ApOtherIpTableFullFlag_Type = TruthValue
_ApOtherIpTableFullFlag_Object = MibScalar
apOtherIpTableFullFlag = _ApOtherIpTableFullFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 17),
    _ApOtherIpTableFullFlag_Type()
)
apOtherIpTableFullFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOtherIpTableFullFlag.setStatus("current")
_ApFragTableFullFlag_Type = TruthValue
_ApFragTableFullFlag_Object = MibScalar
apFragTableFullFlag = _ApFragTableFullFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 18),
    _ApFragTableFullFlag_Type()
)
apFragTableFullFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFragTableFullFlag.setStatus("current")
_ApFtpTableFullFlag_Type = TruthValue
_ApFtpTableFullFlag_Object = MibScalar
apFtpTableFullFlag = _ApFtpTableFullFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 19),
    _ApFtpTableFullFlag_Type()
)
apFtpTableFullFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFtpTableFullFlag.setStatus("current")
_ApBlockedTableFullFlag_Type = TruthValue
_ApBlockedTableFullFlag_Object = MibScalar
apBlockedTableFullFlag = _ApBlockedTableFullFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 20),
    _ApBlockedTableFullFlag_Type()
)
apBlockedTableFullFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlockedTableFullFlag.setStatus("current")
_ApShortCircuitFlag_Type = TruthValue
_ApShortCircuitFlag_Object = MibScalar
apShortCircuitFlag = _ApShortCircuitFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 21),
    _ApShortCircuitFlag_Type()
)
apShortCircuitFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apShortCircuitFlag.setStatus("current")
_ApInternetIfDisconnectedFlag_Type = TruthValue
_ApInternetIfDisconnectedFlag_Object = MibScalar
apInternetIfDisconnectedFlag = _ApInternetIfDisconnectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 22),
    _ApInternetIfDisconnectedFlag_Type()
)
apInternetIfDisconnectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInternetIfDisconnectedFlag.setStatus("current")
_ApProtectedIfDisconnectedFlag_Type = TruthValue
_ApProtectedIfDisconnectedFlag_Object = MibScalar
apProtectedIfDisconnectedFlag = _ApProtectedIfDisconnectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 23),
    _ApProtectedIfDisconnectedFlag_Type()
)
apProtectedIfDisconnectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProtectedIfDisconnectedFlag.setStatus("current")
_ApMgmtIfDisconnectedFlag_Type = TruthValue
_ApMgmtIfDisconnectedFlag_Object = MibScalar
apMgmtIfDisconnectedFlag = _ApMgmtIfDisconnectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 24),
    _ApMgmtIfDisconnectedFlag_Type()
)
apMgmtIfDisconnectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMgmtIfDisconnectedFlag.setStatus("current")
_ApUpgradingFlag_Type = TruthValue
_ApUpgradingFlag_Object = MibScalar
apUpgradingFlag = _ApUpgradingFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 25),
    _ApUpgradingFlag_Type()
)
apUpgradingFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUpgradingFlag.setStatus("current")
_ApProtectedIfTrafficFlag_Type = TruthValue
_ApProtectedIfTrafficFlag_Object = MibScalar
apProtectedIfTrafficFlag = _ApProtectedIfTrafficFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 26),
    _ApProtectedIfTrafficFlag_Type()
)
apProtectedIfTrafficFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProtectedIfTrafficFlag.setStatus("current")
_ApRoutingLoopFlag_Type = TruthValue
_ApRoutingLoopFlag_Object = MibScalar
apRoutingLoopFlag = _ApRoutingLoopFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 27),
    _ApRoutingLoopFlag_Type()
)
apRoutingLoopFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRoutingLoopFlag.setStatus("current")
_ApOfflineFlag_Type = TruthValue
_ApOfflineFlag_Object = MibScalar
apOfflineFlag = _ApOfflineFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 28),
    _ApOfflineFlag_Type()
)
apOfflineFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOfflineFlag.setStatus("current")
_ApStateLearningFlag_Type = TruthValue
_ApStateLearningFlag_Object = MibScalar
apStateLearningFlag = _ApStateLearningFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 29),
    _ApStateLearningFlag_Type()
)
apStateLearningFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStateLearningFlag.setStatus("current")
_ApSupportExpiredFlag_Type = TruthValue
_ApSupportExpiredFlag_Object = MibScalar
apSupportExpiredFlag = _ApSupportExpiredFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 30),
    _ApSupportExpiredFlag_Type()
)
apSupportExpiredFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSupportExpiredFlag.setStatus("current")
_ApSevereLoadingFlag_Type = TruthValue
_ApSevereLoadingFlag_Object = MibScalar
apSevereLoadingFlag = _ApSevereLoadingFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 31),
    _ApSevereLoadingFlag_Type()
)
apSevereLoadingFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSevereLoadingFlag.setStatus("current")
_ApMacMisconfiguredFlag_Type = TruthValue
_ApMacMisconfiguredFlag_Object = MibScalar
apMacMisconfiguredFlag = _ApMacMisconfiguredFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 32),
    _ApMacMisconfiguredFlag_Type()
)
apMacMisconfiguredFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMacMisconfiguredFlag.setStatus("current")
_ApIfMisconfiguredFlag_Type = TruthValue
_ApIfMisconfiguredFlag_Object = MibScalar
apIfMisconfiguredFlag = _ApIfMisconfiguredFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 33),
    _ApIfMisconfiguredFlag_Type()
)
apIfMisconfiguredFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfMisconfiguredFlag.setStatus("current")
_ApInternetIfLinkDownFlag_Type = TruthValue
_ApInternetIfLinkDownFlag_Object = MibScalar
apInternetIfLinkDownFlag = _ApInternetIfLinkDownFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 34),
    _ApInternetIfLinkDownFlag_Type()
)
apInternetIfLinkDownFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInternetIfLinkDownFlag.setStatus("current")
_ApProtectedIfLinkDownFlag_Type = TruthValue
_ApProtectedIfLinkDownFlag_Object = MibScalar
apProtectedIfLinkDownFlag = _ApProtectedIfLinkDownFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 35),
    _ApProtectedIfLinkDownFlag_Type()
)
apProtectedIfLinkDownFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProtectedIfLinkDownFlag.setStatus("current")
_ApDatashareIfDisconnectedFlag_Type = TruthValue
_ApDatashareIfDisconnectedFlag_Object = MibScalar
apDatashareIfDisconnectedFlag = _ApDatashareIfDisconnectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 36),
    _ApDatashareIfDisconnectedFlag_Type()
)
apDatashareIfDisconnectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDatashareIfDisconnectedFlag.setStatus("current")
_ApDiskFailingFlag_Type = TruthValue
_ApDiskFailingFlag_Object = MibScalar
apDiskFailingFlag = _ApDiskFailingFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 37),
    _ApDiskFailingFlag_Type()
)
apDiskFailingFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiskFailingFlag.setStatus("current")
_ApPsuFailingFlag_Type = TruthValue
_ApPsuFailingFlag_Object = MibScalar
apPsuFailingFlag = _ApPsuFailingFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 38),
    _ApPsuFailingFlag_Type()
)
apPsuFailingFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPsuFailingFlag.setStatus("current")
_ApFanFailingFlag_Type = TruthValue
_ApFanFailingFlag_Object = MibScalar
apFanFailingFlag = _ApFanFailingFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 39),
    _ApFanFailingFlag_Type()
)
apFanFailingFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFanFailingFlag.setStatus("current")
_ApConfigXferFailFlag_Type = TruthValue
_ApConfigXferFailFlag_Object = MibScalar
apConfigXferFailFlag = _ApConfigXferFailFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 40),
    _ApConfigXferFailFlag_Type()
)
apConfigXferFailFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apConfigXferFailFlag.setStatus("current")
_ApMissingRequiredPartnerFlag_Type = TruthValue
_ApMissingRequiredPartnerFlag_Object = MibScalar
apMissingRequiredPartnerFlag = _ApMissingRequiredPartnerFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 41),
    _ApMissingRequiredPartnerFlag_Type()
)
apMissingRequiredPartnerFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMissingRequiredPartnerFlag.setStatus("current")
_ApBgpMisconfiguredIpFlag_Type = TruthValue
_ApBgpMisconfiguredIpFlag_Object = MibScalar
apBgpMisconfiguredIpFlag = _ApBgpMisconfiguredIpFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 2, 42),
    _ApBgpMisconfiguredIpFlag_Type()
)
apBgpMisconfiguredIpFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBgpMisconfiguredIpFlag.setStatus("current")
_ApStats_ObjectIdentity = ObjectIdentity
apStats = _ApStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3)
)
_ApSessionTallies_ObjectIdentity = ObjectIdentity
apSessionTallies = _ApSessionTallies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 1)
)
_ApInTcpConnTally_Type = Gauge32
_ApInTcpConnTally_Object = MibScalar
apInTcpConnTally = _ApInTcpConnTally_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 1, 1),
    _ApInTcpConnTally_Type()
)
apInTcpConnTally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInTcpConnTally.setStatus("current")
_ApOutTcpConnTally_Type = Gauge32
_ApOutTcpConnTally_Object = MibScalar
apOutTcpConnTally = _ApOutTcpConnTally_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 1, 2),
    _ApOutTcpConnTally_Type()
)
apOutTcpConnTally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutTcpConnTally.setStatus("current")
_ApInSynBacklogTally_Type = Gauge32
_ApInSynBacklogTally_Object = MibScalar
apInSynBacklogTally = _ApInSynBacklogTally_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 1, 3),
    _ApInSynBacklogTally_Type()
)
apInSynBacklogTally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInSynBacklogTally.setStatus("current")
_ApUdpSessionTally_Type = Gauge32
_ApUdpSessionTally_Object = MibScalar
apUdpSessionTally = _ApUdpSessionTally_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 1, 4),
    _ApUdpSessionTally_Type()
)
apUdpSessionTally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUdpSessionTally.setStatus("current")
_ApIcmpSessionTally_Type = Gauge32
_ApIcmpSessionTally_Object = MibScalar
apIcmpSessionTally = _ApIcmpSessionTally_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 1, 5),
    _ApIcmpSessionTally_Type()
)
apIcmpSessionTally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIcmpSessionTally.setStatus("current")
_ApOtherIpSessionTally_Type = Gauge32
_ApOtherIpSessionTally_Object = MibScalar
apOtherIpSessionTally = _ApOtherIpSessionTally_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 1, 6),
    _ApOtherIpSessionTally_Type()
)
apOtherIpSessionTally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOtherIpSessionTally.setStatus("current")
_ApSummaryBytes_ObjectIdentity = ObjectIdentity
apSummaryBytes = _ApSummaryBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 3)
)
_ApInTotalBytesCnt_Type = Counter64
_ApInTotalBytesCnt_Object = MibScalar
apInTotalBytesCnt = _ApInTotalBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 3, 1),
    _ApInTotalBytesCnt_Type()
)
apInTotalBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInTotalBytesCnt.setStatus("current")
_ApOutTotalBytesCnt_Type = Counter64
_ApOutTotalBytesCnt_Object = MibScalar
apOutTotalBytesCnt = _ApOutTotalBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 3, 2),
    _ApOutTotalBytesCnt_Type()
)
apOutTotalBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutTotalBytesCnt.setStatus("current")
_ApInDroppedBytesCnt_Type = Counter64
_ApInDroppedBytesCnt_Object = MibScalar
apInDroppedBytesCnt = _ApInDroppedBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 3, 3),
    _ApInDroppedBytesCnt_Type()
)
apInDroppedBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInDroppedBytesCnt.setStatus("current")
_ApOutDroppedBytesCnt_Type = Counter64
_ApOutDroppedBytesCnt_Object = MibScalar
apOutDroppedBytesCnt = _ApOutDroppedBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 3, 4),
    _ApOutDroppedBytesCnt_Type()
)
apOutDroppedBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutDroppedBytesCnt.setStatus("current")
_ApInCharmDroppedBytesCnt_Type = Counter64
_ApInCharmDroppedBytesCnt_Object = MibScalar
apInCharmDroppedBytesCnt = _ApInCharmDroppedBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 3, 5),
    _ApInCharmDroppedBytesCnt_Type()
)
apInCharmDroppedBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInCharmDroppedBytesCnt.setStatus("current")
_ApOutCharmDroppedBytesCnt_Type = Counter64
_ApOutCharmDroppedBytesCnt_Object = MibScalar
apOutCharmDroppedBytesCnt = _ApOutCharmDroppedBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 3, 6),
    _ApOutCharmDroppedBytesCnt_Type()
)
apOutCharmDroppedBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutCharmDroppedBytesCnt.setStatus("current")
_ApSummaryPpsRates_ObjectIdentity = ObjectIdentity
apSummaryPpsRates = _ApSummaryPpsRates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 4)
)
_ApInTotalPpsMax_Type = Gauge32
_ApInTotalPpsMax_Object = MibScalar
apInTotalPpsMax = _ApInTotalPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 4, 1),
    _ApInTotalPpsMax_Type()
)
apInTotalPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInTotalPpsMax.setStatus("current")
_ApOutTotalPpsMax_Type = Gauge32
_ApOutTotalPpsMax_Object = MibScalar
apOutTotalPpsMax = _ApOutTotalPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 4, 2),
    _ApOutTotalPpsMax_Type()
)
apOutTotalPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutTotalPpsMax.setStatus("current")
_ApInDroppedPpsMax_Type = Gauge32
_ApInDroppedPpsMax_Object = MibScalar
apInDroppedPpsMax = _ApInDroppedPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 4, 3),
    _ApInDroppedPpsMax_Type()
)
apInDroppedPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInDroppedPpsMax.setStatus("current")
_ApOutDroppedPpsMax_Type = Gauge32
_ApOutDroppedPpsMax_Object = MibScalar
apOutDroppedPpsMax = _ApOutDroppedPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 4, 4),
    _ApOutDroppedPpsMax_Type()
)
apOutDroppedPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutDroppedPpsMax.setStatus("current")
_ApSummaryBpsRates_ObjectIdentity = ObjectIdentity
apSummaryBpsRates = _ApSummaryBpsRates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 5)
)
_ApInTotalBpsMax_Type = Gauge32
_ApInTotalBpsMax_Object = MibScalar
apInTotalBpsMax = _ApInTotalBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 5, 1),
    _ApInTotalBpsMax_Type()
)
apInTotalBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInTotalBpsMax.setStatus("current")
_ApOutTotalBpsMax_Type = Gauge32
_ApOutTotalBpsMax_Object = MibScalar
apOutTotalBpsMax = _ApOutTotalBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 5, 2),
    _ApOutTotalBpsMax_Type()
)
apOutTotalBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutTotalBpsMax.setStatus("current")
_ApInDroppedBpsMax_Type = Gauge32
_ApInDroppedBpsMax_Object = MibScalar
apInDroppedBpsMax = _ApInDroppedBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 5, 3),
    _ApInDroppedBpsMax_Type()
)
apInDroppedBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInDroppedBpsMax.setStatus("current")
_ApOutDroppedBpsMax_Type = Gauge32
_ApOutDroppedBpsMax_Object = MibScalar
apOutDroppedBpsMax = _ApOutDroppedBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 5, 4),
    _ApOutDroppedBpsMax_Type()
)
apOutDroppedBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutDroppedBpsMax.setStatus("current")
_ApInCharmDroppedBpsMax_Type = Gauge32
_ApInCharmDroppedBpsMax_Object = MibScalar
apInCharmDroppedBpsMax = _ApInCharmDroppedBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 5, 5),
    _ApInCharmDroppedBpsMax_Type()
)
apInCharmDroppedBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInCharmDroppedBpsMax.setStatus("current")
_ApOutCharmDroppedBpsMax_Type = Gauge32
_ApOutCharmDroppedBpsMax_Object = MibScalar
apOutCharmDroppedBpsMax = _ApOutCharmDroppedBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 5, 6),
    _ApOutCharmDroppedBpsMax_Type()
)
apOutCharmDroppedBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutCharmDroppedBpsMax.setStatus("current")
_ApAttackPkts_ObjectIdentity = ObjectIdentity
apAttackPkts = _ApAttackPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6)
)
_ApInProtectBwthPktsCnt_Type = Counter32
_ApInProtectBwthPktsCnt_Object = MibScalar
apInProtectBwthPktsCnt = _ApInProtectBwthPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 1),
    _ApInProtectBwthPktsCnt_Type()
)
apInProtectBwthPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInProtectBwthPktsCnt.setStatus("current")
_ApOutProtectBwthPktsCnt_Type = Counter32
_ApOutProtectBwthPktsCnt_Object = MibScalar
apOutProtectBwthPktsCnt = _ApOutProtectBwthPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 2),
    _ApOutProtectBwthPktsCnt_Type()
)
apOutProtectBwthPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutProtectBwthPktsCnt.setStatus("current")
_ApInFloodPktsCnt_Type = Counter32
_ApInFloodPktsCnt_Object = MibScalar
apInFloodPktsCnt = _ApInFloodPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 3),
    _ApInFloodPktsCnt_Type()
)
apInFloodPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInFloodPktsCnt.setStatus("current")
_ApOutFloodPktsCnt_Type = Counter32
_ApOutFloodPktsCnt_Object = MibScalar
apOutFloodPktsCnt = _ApOutFloodPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 4),
    _ApOutFloodPktsCnt_Type()
)
apOutFloodPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutFloodPktsCnt.setStatus("current")
_ApInBlockedProtocolPktsCnt_Type = Counter32
_ApInBlockedProtocolPktsCnt_Object = MibScalar
apInBlockedProtocolPktsCnt = _ApInBlockedProtocolPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 5),
    _ApInBlockedProtocolPktsCnt_Type()
)
apInBlockedProtocolPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBlockedProtocolPktsCnt.setStatus("current")
_ApOutBlockedProtocolPktsCnt_Type = Counter32
_ApOutBlockedProtocolPktsCnt_Object = MibScalar
apOutBlockedProtocolPktsCnt = _ApOutBlockedProtocolPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 6),
    _ApOutBlockedProtocolPktsCnt_Type()
)
apOutBlockedProtocolPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBlockedProtocolPktsCnt.setStatus("current")
_ApInBlockedStatePktsCnt_Type = Counter32
_ApInBlockedStatePktsCnt_Object = MibScalar
apInBlockedStatePktsCnt = _ApInBlockedStatePktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 7),
    _ApInBlockedStatePktsCnt_Type()
)
apInBlockedStatePktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBlockedStatePktsCnt.setStatus("current")
_ApOutBlockedStatePktsCnt_Type = Counter32
_ApOutBlockedStatePktsCnt_Object = MibScalar
apOutBlockedStatePktsCnt = _ApOutBlockedStatePktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 8),
    _ApOutBlockedStatePktsCnt_Type()
)
apOutBlockedStatePktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBlockedStatePktsCnt.setStatus("current")
_ApInIpAttackPktsCnt_Type = Counter32
_ApInIpAttackPktsCnt_Object = MibScalar
apInIpAttackPktsCnt = _ApInIpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 9),
    _ApInIpAttackPktsCnt_Type()
)
apInIpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInIpAttackPktsCnt.setStatus("current")
_ApOutIpAttackPktsCnt_Type = Counter32
_ApOutIpAttackPktsCnt_Object = MibScalar
apOutIpAttackPktsCnt = _ApOutIpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 10),
    _ApOutIpAttackPktsCnt_Type()
)
apOutIpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutIpAttackPktsCnt.setStatus("current")
_ApInTcpAttackPktsCnt_Type = Counter32
_ApInTcpAttackPktsCnt_Object = MibScalar
apInTcpAttackPktsCnt = _ApInTcpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 11),
    _ApInTcpAttackPktsCnt_Type()
)
apInTcpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInTcpAttackPktsCnt.setStatus("current")
_ApOutTcpAttackPktsCnt_Type = Counter32
_ApOutTcpAttackPktsCnt_Object = MibScalar
apOutTcpAttackPktsCnt = _ApOutTcpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 12),
    _ApOutTcpAttackPktsCnt_Type()
)
apOutTcpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutTcpAttackPktsCnt.setStatus("current")
_ApInUdpAttackPktsCnt_Type = Counter32
_ApInUdpAttackPktsCnt_Object = MibScalar
apInUdpAttackPktsCnt = _ApInUdpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 13),
    _ApInUdpAttackPktsCnt_Type()
)
apInUdpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInUdpAttackPktsCnt.setStatus("current")
_ApOutUdpAttackPktsCnt_Type = Counter32
_ApOutUdpAttackPktsCnt_Object = MibScalar
apOutUdpAttackPktsCnt = _ApOutUdpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 14),
    _ApOutUdpAttackPktsCnt_Type()
)
apOutUdpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutUdpAttackPktsCnt.setStatus("current")
_ApInIcmpAttackPktsCnt_Type = Counter32
_ApInIcmpAttackPktsCnt_Object = MibScalar
apInIcmpAttackPktsCnt = _ApInIcmpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 15),
    _ApInIcmpAttackPktsCnt_Type()
)
apInIcmpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInIcmpAttackPktsCnt.setStatus("current")
_ApOutIcmpAttackPktsCnt_Type = Counter32
_ApOutIcmpAttackPktsCnt_Object = MibScalar
apOutIcmpAttackPktsCnt = _ApOutIcmpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 16),
    _ApOutIcmpAttackPktsCnt_Type()
)
apOutIcmpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutIcmpAttackPktsCnt.setStatus("current")
_ApInOtherIpAttackPktsCnt_Type = Counter32
_ApInOtherIpAttackPktsCnt_Object = MibScalar
apInOtherIpAttackPktsCnt = _ApInOtherIpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 17),
    _ApInOtherIpAttackPktsCnt_Type()
)
apInOtherIpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInOtherIpAttackPktsCnt.setStatus("current")
_ApOutOtherIpAttackPktsCnt_Type = Counter32
_ApOutOtherIpAttackPktsCnt_Object = MibScalar
apOutOtherIpAttackPktsCnt = _ApOutOtherIpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 18),
    _ApOutOtherIpAttackPktsCnt_Type()
)
apOutOtherIpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutOtherIpAttackPktsCnt.setStatus("current")
_ApInFragmentAttackPktsCnt_Type = Counter32
_ApInFragmentAttackPktsCnt_Object = MibScalar
apInFragmentAttackPktsCnt = _ApInFragmentAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 19),
    _ApInFragmentAttackPktsCnt_Type()
)
apInFragmentAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInFragmentAttackPktsCnt.setStatus("current")
_ApOutFragmentAttackPktsCnt_Type = Counter32
_ApOutFragmentAttackPktsCnt_Object = MibScalar
apOutFragmentAttackPktsCnt = _ApOutFragmentAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 20),
    _ApOutFragmentAttackPktsCnt_Type()
)
apOutFragmentAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutFragmentAttackPktsCnt.setStatus("current")
_ApInBadIpPktsCnt_Type = Counter32
_ApInBadIpPktsCnt_Object = MibScalar
apInBadIpPktsCnt = _ApInBadIpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 21),
    _ApInBadIpPktsCnt_Type()
)
apInBadIpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBadIpPktsCnt.setStatus("current")
_ApOutBadIpPktsCnt_Type = Counter32
_ApOutBadIpPktsCnt_Object = MibScalar
apOutBadIpPktsCnt = _ApOutBadIpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 22),
    _ApOutBadIpPktsCnt_Type()
)
apOutBadIpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBadIpPktsCnt.setStatus("current")
_ApInBadTcpPktsCnt_Type = Counter32
_ApInBadTcpPktsCnt_Object = MibScalar
apInBadTcpPktsCnt = _ApInBadTcpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 23),
    _ApInBadTcpPktsCnt_Type()
)
apInBadTcpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBadTcpPktsCnt.setStatus("current")
_ApOutBadTcpPktsCnt_Type = Counter32
_ApOutBadTcpPktsCnt_Object = MibScalar
apOutBadTcpPktsCnt = _ApOutBadTcpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 24),
    _ApOutBadTcpPktsCnt_Type()
)
apOutBadTcpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBadTcpPktsCnt.setStatus("current")
_ApInBadUdpPktsCnt_Type = Counter32
_ApInBadUdpPktsCnt_Object = MibScalar
apInBadUdpPktsCnt = _ApInBadUdpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 25),
    _ApInBadUdpPktsCnt_Type()
)
apInBadUdpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBadUdpPktsCnt.setStatus("current")
_ApOutBadUdpPktsCnt_Type = Counter32
_ApOutBadUdpPktsCnt_Object = MibScalar
apOutBadUdpPktsCnt = _ApOutBadUdpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 26),
    _ApOutBadUdpPktsCnt_Type()
)
apOutBadUdpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBadUdpPktsCnt.setStatus("current")
_ApInBadIcmpPktsCnt_Type = Counter32
_ApInBadIcmpPktsCnt_Object = MibScalar
apInBadIcmpPktsCnt = _ApInBadIcmpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 27),
    _ApInBadIcmpPktsCnt_Type()
)
apInBadIcmpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBadIcmpPktsCnt.setStatus("current")
_ApOutBadIcmpPktsCnt_Type = Counter32
_ApOutBadIcmpPktsCnt_Object = MibScalar
apOutBadIcmpPktsCnt = _ApOutBadIcmpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 28),
    _ApOutBadIcmpPktsCnt_Type()
)
apOutBadIcmpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBadIcmpPktsCnt.setStatus("current")
_ApInBadOtherIpPktsCnt_Type = Counter32
_ApInBadOtherIpPktsCnt_Object = MibScalar
apInBadOtherIpPktsCnt = _ApInBadOtherIpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 29),
    _ApInBadOtherIpPktsCnt_Type()
)
apInBadOtherIpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInBadOtherIpPktsCnt.setStatus("current")
_ApOutBadOtherIpPktsCnt_Type = Counter32
_ApOutBadOtherIpPktsCnt_Object = MibScalar
apOutBadOtherIpPktsCnt = _ApOutBadOtherIpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 30),
    _ApOutBadOtherIpPktsCnt_Type()
)
apOutBadOtherIpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutBadOtherIpPktsCnt.setStatus("current")
_ApInTotalPpsCnt_Type = Counter32
_ApInTotalPpsCnt_Object = MibScalar
apInTotalPpsCnt = _ApInTotalPpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 33),
    _ApInTotalPpsCnt_Type()
)
apInTotalPpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInTotalPpsCnt.setStatus("current")
_ApOutTotalPpsCnt_Type = Counter32
_ApOutTotalPpsCnt_Object = MibScalar
apOutTotalPpsCnt = _ApOutTotalPpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 34),
    _ApOutTotalPpsCnt_Type()
)
apOutTotalPpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutTotalPpsCnt.setStatus("current")
_ApInSmallPpsCnt_Type = Counter32
_ApInSmallPpsCnt_Object = MibScalar
apInSmallPpsCnt = _ApInSmallPpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 35),
    _ApInSmallPpsCnt_Type()
)
apInSmallPpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInSmallPpsCnt.setStatus("current")
_ApOutSmallPpsCnt_Type = Counter32
_ApOutSmallPpsCnt_Object = MibScalar
apOutSmallPpsCnt = _ApOutSmallPpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 36),
    _ApOutSmallPpsCnt_Type()
)
apOutSmallPpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutSmallPpsCnt.setStatus("current")
_ApInMediumPpsCnt_Type = Counter32
_ApInMediumPpsCnt_Object = MibScalar
apInMediumPpsCnt = _ApInMediumPpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 37),
    _ApInMediumPpsCnt_Type()
)
apInMediumPpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInMediumPpsCnt.setStatus("current")
_ApOutMediumPpsCnt_Type = Counter32
_ApOutMediumPpsCnt_Object = MibScalar
apOutMediumPpsCnt = _ApOutMediumPpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 38),
    _ApOutMediumPpsCnt_Type()
)
apOutMediumPpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutMediumPpsCnt.setStatus("current")
_ApInLargePpsCnt_Type = Counter32
_ApInLargePpsCnt_Object = MibScalar
apInLargePpsCnt = _ApInLargePpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 39),
    _ApInLargePpsCnt_Type()
)
apInLargePpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInLargePpsCnt.setStatus("current")
_ApOutLargePpsCnt_Type = Counter32
_ApOutLargePpsCnt_Object = MibScalar
apOutLargePpsCnt = _ApOutLargePpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 40),
    _ApOutLargePpsCnt_Type()
)
apOutLargePpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutLargePpsCnt.setStatus("current")
_ApInDroppedPpsCnt_Type = Counter32
_ApInDroppedPpsCnt_Object = MibScalar
apInDroppedPpsCnt = _ApInDroppedPpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 43),
    _ApInDroppedPpsCnt_Type()
)
apInDroppedPpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInDroppedPpsCnt.setStatus("current")
_ApOutDroppedPpsCnt_Type = Counter32
_ApOutDroppedPpsCnt_Object = MibScalar
apOutDroppedPpsCnt = _ApOutDroppedPpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 44),
    _ApOutDroppedPpsCnt_Type()
)
apOutDroppedPpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutDroppedPpsCnt.setStatus("current")
_ApInFilteredBwthPercentCnt_Type = Counter32
_ApInFilteredBwthPercentCnt_Object = MibScalar
apInFilteredBwthPercentCnt = _ApInFilteredBwthPercentCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 45),
    _ApInFilteredBwthPercentCnt_Type()
)
apInFilteredBwthPercentCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInFilteredBwthPercentCnt.setStatus("current")
_ApOutFilteredBwthPercentCnt_Type = Counter32
_ApOutFilteredBwthPercentCnt_Object = MibScalar
apOutFilteredBwthPercentCnt = _ApOutFilteredBwthPercentCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 46),
    _ApOutFilteredBwthPercentCnt_Type()
)
apOutFilteredBwthPercentCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutFilteredBwthPercentCnt.setStatus("current")
_ApInConnreqCnt_Type = Counter32
_ApInConnreqCnt_Object = MibScalar
apInConnreqCnt = _ApInConnreqCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 47),
    _ApInConnreqCnt_Type()
)
apInConnreqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInConnreqCnt.setStatus("current")
_ApOutConnreqCnt_Type = Counter32
_ApOutConnreqCnt_Object = MibScalar
apOutConnreqCnt = _ApOutConnreqCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 48),
    _ApOutConnreqCnt_Type()
)
apOutConnreqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutConnreqCnt.setStatus("current")
_ApInOverloadedCnt_Type = Counter32
_ApInOverloadedCnt_Object = MibScalar
apInOverloadedCnt = _ApInOverloadedCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 49),
    _ApInOverloadedCnt_Type()
)
apInOverloadedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInOverloadedCnt.setStatus("current")
_ApOutOverloadedCnt_Type = Counter32
_ApOutOverloadedCnt_Object = MibScalar
apOutOverloadedCnt = _ApOutOverloadedCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 6, 50),
    _ApOutOverloadedCnt_Type()
)
apOutOverloadedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutOverloadedCnt.setStatus("current")
_ApWorstOffenderTable_Object = MibTable
apWorstOffenderTable = _ApWorstOffenderTable_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 7)
)
if mibBuilder.loadTexts:
    apWorstOffenderTable.setStatus("current")
_ApWorstOffenderEntry_Object = MibTableRow
apWorstOffenderEntry = _ApWorstOffenderEntry_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 7, 1)
)
apWorstOffenderEntry.setIndexNames(
    (0, "DDOSSECURE4-MIB", "apWorstOffenderInetAddressType"),
    (0, "DDOSSECURE4-MIB", "apWorstOffenderInetAddress"),
    (0, "DDOSSECURE4-MIB", "apWorstOffenderReason"),
)
if mibBuilder.loadTexts:
    apWorstOffenderEntry.setStatus("current")
_ApWorstOffenderInetAddressType_Type = InetAddressType
_ApWorstOffenderInetAddressType_Object = MibTableColumn
apWorstOffenderInetAddressType = _ApWorstOffenderInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 7, 1, 1),
    _ApWorstOffenderInetAddressType_Type()
)
apWorstOffenderInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apWorstOffenderInetAddressType.setStatus("current")


class _ApWorstOffenderInetAddress_Type(InetAddress):
    """Custom type apWorstOffenderInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_ApWorstOffenderInetAddress_Type.__name__ = "InetAddress"
_ApWorstOffenderInetAddress_Object = MibTableColumn
apWorstOffenderInetAddress = _ApWorstOffenderInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 7, 1, 2),
    _ApWorstOffenderInetAddress_Type()
)
apWorstOffenderInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apWorstOffenderInetAddress.setStatus("current")
_ApWorstOffenderReason_Type = DefenseType
_ApWorstOffenderReason_Object = MibTableColumn
apWorstOffenderReason = _ApWorstOffenderReason_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 7, 1, 3),
    _ApWorstOffenderReason_Type()
)
apWorstOffenderReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apWorstOffenderReason.setStatus("current")
_ApWorstOffenderLastTime_Type = DateAndTime
_ApWorstOffenderLastTime_Object = MibTableColumn
apWorstOffenderLastTime = _ApWorstOffenderLastTime_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 7, 1, 4),
    _ApWorstOffenderLastTime_Type()
)
apWorstOffenderLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWorstOffenderLastTime.setStatus("current")
_ApWorstOffenderCount_Type = Counter32
_ApWorstOffenderCount_Object = MibTableColumn
apWorstOffenderCount = _ApWorstOffenderCount_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 3, 7, 1, 5),
    _ApWorstOffenderCount_Type()
)
apWorstOffenderCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWorstOffenderCount.setStatus("current")
_ApLogFileTable_Object = MibTable
apLogFileTable = _ApLogFileTable_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 4)
)
if mibBuilder.loadTexts:
    apLogFileTable.setStatus("current")
_ApLogFileEntry_Object = MibTableRow
apLogFileEntry = _ApLogFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 4, 1)
)
apLogFileEntry.setIndexNames(
    (0, "DDOSSECURE4-MIB", "apLogFileRecordNumber"),
)
if mibBuilder.loadTexts:
    apLogFileEntry.setStatus("current")
_ApLogFileRecordNumber_Type = LocalIndex
_ApLogFileRecordNumber_Object = MibTableColumn
apLogFileRecordNumber = _ApLogFileRecordNumber_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 4, 1, 1),
    _ApLogFileRecordNumber_Type()
)
apLogFileRecordNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apLogFileRecordNumber.setStatus("current")
_ApLogFileRecord_Type = DisplayString
_ApLogFileRecord_Object = MibTableColumn
apLogFileRecord = _ApLogFileRecord_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 4, 1, 2),
    _ApLogFileRecord_Type()
)
apLogFileRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLogFileRecord.setStatus("current")
_ApIncidentTable_Object = MibTable
apIncidentTable = _ApIncidentTable_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 5)
)
if mibBuilder.loadTexts:
    apIncidentTable.setStatus("current")
_ApIncidentEntry_Object = MibTableRow
apIncidentEntry = _ApIncidentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 5, 1)
)
apIncidentEntry.setIndexNames(
    (0, "DDOSSECURE4-MIB", "apIncidentYear"),
    (0, "DDOSSECURE4-MIB", "apIncidentMonth"),
    (0, "DDOSSECURE4-MIB", "apIncidentDay"),
    (0, "DDOSSECURE4-MIB", "apIncidentNumber"),
)
if mibBuilder.loadTexts:
    apIncidentEntry.setStatus("current")
_ApIncidentYear_Type = LocalIndex
_ApIncidentYear_Object = MibTableColumn
apIncidentYear = _ApIncidentYear_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 5, 1, 1),
    _ApIncidentYear_Type()
)
apIncidentYear.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apIncidentYear.setStatus("current")
_ApIncidentMonth_Type = LocalIndex
_ApIncidentMonth_Object = MibTableColumn
apIncidentMonth = _ApIncidentMonth_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 5, 1, 2),
    _ApIncidentMonth_Type()
)
apIncidentMonth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apIncidentMonth.setStatus("current")
_ApIncidentDay_Type = LocalIndex
_ApIncidentDay_Object = MibTableColumn
apIncidentDay = _ApIncidentDay_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 5, 1, 3),
    _ApIncidentDay_Type()
)
apIncidentDay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apIncidentDay.setStatus("current")
_ApIncidentNumber_Type = LocalIndex
_ApIncidentNumber_Object = MibTableColumn
apIncidentNumber = _ApIncidentNumber_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 5, 1, 4),
    _ApIncidentNumber_Type()
)
apIncidentNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apIncidentNumber.setStatus("current")
_ApIncidentStart_Type = DateAndTime
_ApIncidentStart_Object = MibTableColumn
apIncidentStart = _ApIncidentStart_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 5, 1, 5),
    _ApIncidentStart_Type()
)
apIncidentStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIncidentStart.setStatus("current")
_ApIncidentAddress_Type = DisplayString
_ApIncidentAddress_Object = MibTableColumn
apIncidentAddress = _ApIncidentAddress_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 5, 1, 6),
    _ApIncidentAddress_Type()
)
apIncidentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIncidentAddress.setStatus("current")
_ApIncidentType_Type = DisplayString
_ApIncidentType_Object = MibTableColumn
apIncidentType = _ApIncidentType_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 5, 1, 7),
    _ApIncidentType_Type()
)
apIncidentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIncidentType.setStatus("current")
_ApIncidentDirection_Type = Direction
_ApIncidentDirection_Object = MibTableColumn
apIncidentDirection = _ApIncidentDirection_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 5, 1, 8),
    _ApIncidentDirection_Type()
)
apIncidentDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIncidentDirection.setStatus("current")
_ApIncidentPeakRate_Type = Gauge32
_ApIncidentPeakRate_Object = MibTableColumn
apIncidentPeakRate = _ApIncidentPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 5, 1, 9),
    _ApIncidentPeakRate_Type()
)
apIncidentPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIncidentPeakRate.setStatus("current")
_ApIncidentDropped_Type = Gauge32
_ApIncidentDropped_Object = MibTableColumn
apIncidentDropped = _ApIncidentDropped_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 4, 5, 1, 10),
    _ApIncidentDropped_Type()
)
apIncidentDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIncidentDropped.setStatus("current")
_JddsPortal_ObjectIdentity = ObjectIdentity
jddsPortal = _JddsPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5)
)
_PoStatsTable_Object = MibTable
poStatsTable = _PoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3)
)
if mibBuilder.loadTexts:
    poStatsTable.setStatus("current")
_PoStatsEntry_Object = MibTableRow
poStatsEntry = _PoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1)
)
poStatsEntry.setIndexNames(
    (0, "DDOSSECURE4-MIB", "poStatsIndex"),
)
if mibBuilder.loadTexts:
    poStatsEntry.setStatus("current")
_PoStatsIndex_Type = LocalIndex
_PoStatsIndex_Object = MibTableColumn
poStatsIndex = _PoStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1),
    _PoStatsIndex_Type()
)
poStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    poStatsIndex.setStatus("current")
_PoPortalName_Type = DisplayString
_PoPortalName_Object = MibTableColumn
poPortalName = _PoPortalName_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 2),
    _PoPortalName_Type()
)
poPortalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poPortalName.setStatus("current")
_PoInTotalBpsAvg_Type = Gauge32
_PoInTotalBpsAvg_Object = MibTableColumn
poInTotalBpsAvg = _PoInTotalBpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 901),
    _PoInTotalBpsAvg_Type()
)
poInTotalBpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInTotalBpsAvg.setStatus("current")
_PoOutTotalBpsAvg_Type = Gauge32
_PoOutTotalBpsAvg_Object = MibTableColumn
poOutTotalBpsAvg = _PoOutTotalBpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 902),
    _PoOutTotalBpsAvg_Type()
)
poOutTotalBpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutTotalBpsAvg.setStatus("current")
_PoInTotalPpsAvg_Type = Gauge32
_PoInTotalPpsAvg_Object = MibTableColumn
poInTotalPpsAvg = _PoInTotalPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 903),
    _PoInTotalPpsAvg_Type()
)
poInTotalPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInTotalPpsAvg.setStatus("current")
_PoOutTotalPpsAvg_Type = Gauge32
_PoOutTotalPpsAvg_Object = MibTableColumn
poOutTotalPpsAvg = _PoOutTotalPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 904),
    _PoOutTotalPpsAvg_Type()
)
poOutTotalPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutTotalPpsAvg.setStatus("current")
_PoInSmallPpsAvg_Type = Gauge32
_PoInSmallPpsAvg_Object = MibTableColumn
poInSmallPpsAvg = _PoInSmallPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 905),
    _PoInSmallPpsAvg_Type()
)
poInSmallPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInSmallPpsAvg.setStatus("current")
_PoOutSmallPpsAvg_Type = Gauge32
_PoOutSmallPpsAvg_Object = MibTableColumn
poOutSmallPpsAvg = _PoOutSmallPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 906),
    _PoOutSmallPpsAvg_Type()
)
poOutSmallPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutSmallPpsAvg.setStatus("current")
_PoInMediumPpsAvg_Type = Gauge32
_PoInMediumPpsAvg_Object = MibTableColumn
poInMediumPpsAvg = _PoInMediumPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 907),
    _PoInMediumPpsAvg_Type()
)
poInMediumPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInMediumPpsAvg.setStatus("current")
_PoOutMediumPpsAvg_Type = Gauge32
_PoOutMediumPpsAvg_Object = MibTableColumn
poOutMediumPpsAvg = _PoOutMediumPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 908),
    _PoOutMediumPpsAvg_Type()
)
poOutMediumPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutMediumPpsAvg.setStatus("current")
_PoInLargePpsAvg_Type = Gauge32
_PoInLargePpsAvg_Object = MibTableColumn
poInLargePpsAvg = _PoInLargePpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 909),
    _PoInLargePpsAvg_Type()
)
poInLargePpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInLargePpsAvg.setStatus("current")
_PoOutLargePpsAvg_Type = Gauge32
_PoOutLargePpsAvg_Object = MibTableColumn
poOutLargePpsAvg = _PoOutLargePpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 910),
    _PoOutLargePpsAvg_Type()
)
poOutLargePpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutLargePpsAvg.setStatus("current")
_PoInDroppedBpsAvg_Type = Gauge32
_PoInDroppedBpsAvg_Object = MibTableColumn
poInDroppedBpsAvg = _PoInDroppedBpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 911),
    _PoInDroppedBpsAvg_Type()
)
poInDroppedBpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInDroppedBpsAvg.setStatus("current")
_PoOutDroppedBpsAvg_Type = Gauge32
_PoOutDroppedBpsAvg_Object = MibTableColumn
poOutDroppedBpsAvg = _PoOutDroppedBpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 912),
    _PoOutDroppedBpsAvg_Type()
)
poOutDroppedBpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutDroppedBpsAvg.setStatus("current")
_PoInDroppedPpsAvg_Type = Gauge32
_PoInDroppedPpsAvg_Object = MibTableColumn
poInDroppedPpsAvg = _PoInDroppedPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 913),
    _PoInDroppedPpsAvg_Type()
)
poInDroppedPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInDroppedPpsAvg.setStatus("current")
_PoOutDroppedPpsAvg_Type = Gauge32
_PoOutDroppedPpsAvg_Object = MibTableColumn
poOutDroppedPpsAvg = _PoOutDroppedPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 914),
    _PoOutDroppedPpsAvg_Type()
)
poOutDroppedPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutDroppedPpsAvg.setStatus("current")
_PoInCharmDroppedBpsAvg_Type = Gauge32
_PoInCharmDroppedBpsAvg_Object = MibTableColumn
poInCharmDroppedBpsAvg = _PoInCharmDroppedBpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 915),
    _PoInCharmDroppedBpsAvg_Type()
)
poInCharmDroppedBpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInCharmDroppedBpsAvg.setStatus("current")
_PoOutCharmDroppedBpsAvg_Type = Gauge32
_PoOutCharmDroppedBpsAvg_Object = MibTableColumn
poOutCharmDroppedBpsAvg = _PoOutCharmDroppedBpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 916),
    _PoOutCharmDroppedBpsAvg_Type()
)
poOutCharmDroppedBpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutCharmDroppedBpsAvg.setStatus("current")
_PoInFilteredBwthPercentAvg_Type = Gauge32
_PoInFilteredBwthPercentAvg_Object = MibTableColumn
poInFilteredBwthPercentAvg = _PoInFilteredBwthPercentAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 917),
    _PoInFilteredBwthPercentAvg_Type()
)
poInFilteredBwthPercentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInFilteredBwthPercentAvg.setStatus("current")
_PoOutFilteredBwthPercentAvg_Type = Gauge32
_PoOutFilteredBwthPercentAvg_Object = MibTableColumn
poOutFilteredBwthPercentAvg = _PoOutFilteredBwthPercentAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 918),
    _PoOutFilteredBwthPercentAvg_Type()
)
poOutFilteredBwthPercentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutFilteredBwthPercentAvg.setStatus("current")
_PoInSynbacklogtallyAvg_Type = Gauge32
_PoInSynbacklogtallyAvg_Object = MibTableColumn
poInSynbacklogtallyAvg = _PoInSynbacklogtallyAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 919),
    _PoInSynbacklogtallyAvg_Type()
)
poInSynbacklogtallyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInSynbacklogtallyAvg.setStatus("current")
_PoOutSynbacklogtallyAvg_Type = Gauge32
_PoOutSynbacklogtallyAvg_Object = MibTableColumn
poOutSynbacklogtallyAvg = _PoOutSynbacklogtallyAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 920),
    _PoOutSynbacklogtallyAvg_Type()
)
poOutSynbacklogtallyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutSynbacklogtallyAvg.setStatus("current")
_PoInConnectionAvg_Type = Gauge32
_PoInConnectionAvg_Object = MibTableColumn
poInConnectionAvg = _PoInConnectionAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 921),
    _PoInConnectionAvg_Type()
)
poInConnectionAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInConnectionAvg.setStatus("current")
_PoOutConnectionAvg_Type = Gauge32
_PoOutConnectionAvg_Object = MibTableColumn
poOutConnectionAvg = _PoOutConnectionAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 922),
    _PoOutConnectionAvg_Type()
)
poOutConnectionAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutConnectionAvg.setStatus("current")
_PoInConnreqAvg_Type = Gauge32
_PoInConnreqAvg_Object = MibTableColumn
poInConnreqAvg = _PoInConnreqAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 923),
    _PoInConnreqAvg_Type()
)
poInConnreqAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInConnreqAvg.setStatus("current")
_PoOutConnreqAvg_Type = Gauge32
_PoOutConnreqAvg_Object = MibTableColumn
poOutConnreqAvg = _PoOutConnreqAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 924),
    _PoOutConnreqAvg_Type()
)
poOutConnreqAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutConnreqAvg.setStatus("current")
_PoInActiveHttpGetsAvg_Type = Gauge32
_PoInActiveHttpGetsAvg_Object = MibTableColumn
poInActiveHttpGetsAvg = _PoInActiveHttpGetsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 925),
    _PoInActiveHttpGetsAvg_Type()
)
poInActiveHttpGetsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInActiveHttpGetsAvg.setStatus("current")
_PoOutActiveHttpGetsAvg_Type = Gauge32
_PoOutActiveHttpGetsAvg_Object = MibTableColumn
poOutActiveHttpGetsAvg = _PoOutActiveHttpGetsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 926),
    _PoOutActiveHttpGetsAvg_Type()
)
poOutActiveHttpGetsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutActiveHttpGetsAvg.setStatus("current")
_PoInProtectBwthPktsAvg_Type = Gauge32
_PoInProtectBwthPktsAvg_Object = MibTableColumn
poInProtectBwthPktsAvg = _PoInProtectBwthPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 927),
    _PoInProtectBwthPktsAvg_Type()
)
poInProtectBwthPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInProtectBwthPktsAvg.setStatus("current")
_PoOutProtectBwthPktsAvg_Type = Gauge32
_PoOutProtectBwthPktsAvg_Object = MibTableColumn
poOutProtectBwthPktsAvg = _PoOutProtectBwthPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 928),
    _PoOutProtectBwthPktsAvg_Type()
)
poOutProtectBwthPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutProtectBwthPktsAvg.setStatus("current")
_PoInFloodPktsAvg_Type = Gauge32
_PoInFloodPktsAvg_Object = MibTableColumn
poInFloodPktsAvg = _PoInFloodPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 929),
    _PoInFloodPktsAvg_Type()
)
poInFloodPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInFloodPktsAvg.setStatus("current")
_PoOutFloodPktsAvg_Type = Gauge32
_PoOutFloodPktsAvg_Object = MibTableColumn
poOutFloodPktsAvg = _PoOutFloodPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 930),
    _PoOutFloodPktsAvg_Type()
)
poOutFloodPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutFloodPktsAvg.setStatus("current")
_PoInBlockedProtocolPktsAvg_Type = Gauge32
_PoInBlockedProtocolPktsAvg_Object = MibTableColumn
poInBlockedProtocolPktsAvg = _PoInBlockedProtocolPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 931),
    _PoInBlockedProtocolPktsAvg_Type()
)
poInBlockedProtocolPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInBlockedProtocolPktsAvg.setStatus("current")
_PoOutBlockedProtocolPktsAvg_Type = Gauge32
_PoOutBlockedProtocolPktsAvg_Object = MibTableColumn
poOutBlockedProtocolPktsAvg = _PoOutBlockedProtocolPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 932),
    _PoOutBlockedProtocolPktsAvg_Type()
)
poOutBlockedProtocolPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutBlockedProtocolPktsAvg.setStatus("current")
_PoInBlockedStatePktsAvg_Type = Gauge32
_PoInBlockedStatePktsAvg_Object = MibTableColumn
poInBlockedStatePktsAvg = _PoInBlockedStatePktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 933),
    _PoInBlockedStatePktsAvg_Type()
)
poInBlockedStatePktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInBlockedStatePktsAvg.setStatus("current")
_PoOutBlockedStatePktsAvg_Type = Gauge32
_PoOutBlockedStatePktsAvg_Object = MibTableColumn
poOutBlockedStatePktsAvg = _PoOutBlockedStatePktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 934),
    _PoOutBlockedStatePktsAvg_Type()
)
poOutBlockedStatePktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutBlockedStatePktsAvg.setStatus("current")
_PoInIpAttackPktsAvg_Type = Gauge32
_PoInIpAttackPktsAvg_Object = MibTableColumn
poInIpAttackPktsAvg = _PoInIpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 935),
    _PoInIpAttackPktsAvg_Type()
)
poInIpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInIpAttackPktsAvg.setStatus("current")
_PoOutIpAttackPktsAvg_Type = Gauge32
_PoOutIpAttackPktsAvg_Object = MibTableColumn
poOutIpAttackPktsAvg = _PoOutIpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 936),
    _PoOutIpAttackPktsAvg_Type()
)
poOutIpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutIpAttackPktsAvg.setStatus("current")
_PoInTcpAttackPktsAvg_Type = Gauge32
_PoInTcpAttackPktsAvg_Object = MibTableColumn
poInTcpAttackPktsAvg = _PoInTcpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 937),
    _PoInTcpAttackPktsAvg_Type()
)
poInTcpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInTcpAttackPktsAvg.setStatus("current")
_PoOutTcpAttackPktsAvg_Type = Gauge32
_PoOutTcpAttackPktsAvg_Object = MibTableColumn
poOutTcpAttackPktsAvg = _PoOutTcpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 938),
    _PoOutTcpAttackPktsAvg_Type()
)
poOutTcpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutTcpAttackPktsAvg.setStatus("current")
_PoInUdpAttackPktsAvg_Type = Gauge32
_PoInUdpAttackPktsAvg_Object = MibTableColumn
poInUdpAttackPktsAvg = _PoInUdpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 939),
    _PoInUdpAttackPktsAvg_Type()
)
poInUdpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInUdpAttackPktsAvg.setStatus("current")
_PoOutUdpAttackPktsAvg_Type = Gauge32
_PoOutUdpAttackPktsAvg_Object = MibTableColumn
poOutUdpAttackPktsAvg = _PoOutUdpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 940),
    _PoOutUdpAttackPktsAvg_Type()
)
poOutUdpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutUdpAttackPktsAvg.setStatus("current")
_PoInIcmpAttackPktsAvg_Type = Gauge32
_PoInIcmpAttackPktsAvg_Object = MibTableColumn
poInIcmpAttackPktsAvg = _PoInIcmpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 941),
    _PoInIcmpAttackPktsAvg_Type()
)
poInIcmpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInIcmpAttackPktsAvg.setStatus("current")
_PoOutIcmpAttackPktsAvg_Type = Gauge32
_PoOutIcmpAttackPktsAvg_Object = MibTableColumn
poOutIcmpAttackPktsAvg = _PoOutIcmpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 942),
    _PoOutIcmpAttackPktsAvg_Type()
)
poOutIcmpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutIcmpAttackPktsAvg.setStatus("current")
_PoInOtherIpAttackPktsAvg_Type = Gauge32
_PoInOtherIpAttackPktsAvg_Object = MibTableColumn
poInOtherIpAttackPktsAvg = _PoInOtherIpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 943),
    _PoInOtherIpAttackPktsAvg_Type()
)
poInOtherIpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInOtherIpAttackPktsAvg.setStatus("current")
_PoOutOtherIpAttackPktsAvg_Type = Gauge32
_PoOutOtherIpAttackPktsAvg_Object = MibTableColumn
poOutOtherIpAttackPktsAvg = _PoOutOtherIpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 944),
    _PoOutOtherIpAttackPktsAvg_Type()
)
poOutOtherIpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutOtherIpAttackPktsAvg.setStatus("current")
_PoInFragmentAttackPktsAvg_Type = Gauge32
_PoInFragmentAttackPktsAvg_Object = MibTableColumn
poInFragmentAttackPktsAvg = _PoInFragmentAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 945),
    _PoInFragmentAttackPktsAvg_Type()
)
poInFragmentAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInFragmentAttackPktsAvg.setStatus("current")
_PoOutFragmentAttackPktsAvg_Type = Gauge32
_PoOutFragmentAttackPktsAvg_Object = MibTableColumn
poOutFragmentAttackPktsAvg = _PoOutFragmentAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 946),
    _PoOutFragmentAttackPktsAvg_Type()
)
poOutFragmentAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutFragmentAttackPktsAvg.setStatus("current")
_PoInBadipPktsAvg_Type = Gauge32
_PoInBadipPktsAvg_Object = MibTableColumn
poInBadipPktsAvg = _PoInBadipPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 947),
    _PoInBadipPktsAvg_Type()
)
poInBadipPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInBadipPktsAvg.setStatus("current")
_PoOutBadipPktsAvg_Type = Gauge32
_PoOutBadipPktsAvg_Object = MibTableColumn
poOutBadipPktsAvg = _PoOutBadipPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 948),
    _PoOutBadipPktsAvg_Type()
)
poOutBadipPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutBadipPktsAvg.setStatus("current")
_PoInBadTcpPktsAvg_Type = Gauge32
_PoInBadTcpPktsAvg_Object = MibTableColumn
poInBadTcpPktsAvg = _PoInBadTcpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 949),
    _PoInBadTcpPktsAvg_Type()
)
poInBadTcpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInBadTcpPktsAvg.setStatus("current")
_PoOutBadTcpPktsAvg_Type = Gauge32
_PoOutBadTcpPktsAvg_Object = MibTableColumn
poOutBadTcpPktsAvg = _PoOutBadTcpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 950),
    _PoOutBadTcpPktsAvg_Type()
)
poOutBadTcpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutBadTcpPktsAvg.setStatus("current")
_PoInBadUdpPktsAvg_Type = Gauge32
_PoInBadUdpPktsAvg_Object = MibTableColumn
poInBadUdpPktsAvg = _PoInBadUdpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 951),
    _PoInBadUdpPktsAvg_Type()
)
poInBadUdpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInBadUdpPktsAvg.setStatus("current")
_PoOutBadUdpPktsAvg_Type = Gauge32
_PoOutBadUdpPktsAvg_Object = MibTableColumn
poOutBadUdpPktsAvg = _PoOutBadUdpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 952),
    _PoOutBadUdpPktsAvg_Type()
)
poOutBadUdpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutBadUdpPktsAvg.setStatus("current")
_PoInBadIcmpPktsAvg_Type = Gauge32
_PoInBadIcmpPktsAvg_Object = MibTableColumn
poInBadIcmpPktsAvg = _PoInBadIcmpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 953),
    _PoInBadIcmpPktsAvg_Type()
)
poInBadIcmpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInBadIcmpPktsAvg.setStatus("current")
_PoOutBadIcmpPktsAvg_Type = Gauge32
_PoOutBadIcmpPktsAvg_Object = MibTableColumn
poOutBadIcmpPktsAvg = _PoOutBadIcmpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 954),
    _PoOutBadIcmpPktsAvg_Type()
)
poOutBadIcmpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutBadIcmpPktsAvg.setStatus("current")
_PoInBadOtherIpPktsAvg_Type = Gauge32
_PoInBadOtherIpPktsAvg_Object = MibTableColumn
poInBadOtherIpPktsAvg = _PoInBadOtherIpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 955),
    _PoInBadOtherIpPktsAvg_Type()
)
poInBadOtherIpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInBadOtherIpPktsAvg.setStatus("current")
_PoOutBadOtherIpPktsAvg_Type = Gauge32
_PoOutBadOtherIpPktsAvg_Object = MibTableColumn
poOutBadOtherIpPktsAvg = _PoOutBadOtherIpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 956),
    _PoOutBadOtherIpPktsAvg_Type()
)
poOutBadOtherIpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutBadOtherIpPktsAvg.setStatus("current")
_PoInOverloadedAvg_Type = Gauge32
_PoInOverloadedAvg_Object = MibTableColumn
poInOverloadedAvg = _PoInOverloadedAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 957),
    _PoInOverloadedAvg_Type()
)
poInOverloadedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInOverloadedAvg.setStatus("current")
_PoOutOverloadedAvg_Type = Gauge32
_PoOutOverloadedAvg_Object = MibTableColumn
poOutOverloadedAvg = _PoOutOverloadedAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 958),
    _PoOutOverloadedAvg_Type()
)
poOutOverloadedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutOverloadedAvg.setStatus("current")
_PoInLatencyAvg_Type = Gauge32
_PoInLatencyAvg_Object = MibTableColumn
poInLatencyAvg = _PoInLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 959),
    _PoInLatencyAvg_Type()
)
poInLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInLatencyAvg.setStatus("current")
_PoOutLatencyAvg_Type = Gauge32
_PoOutLatencyAvg_Object = MibTableColumn
poOutLatencyAvg = _PoOutLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 960),
    _PoOutLatencyAvg_Type()
)
poOutLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutLatencyAvg.setStatus("current")
_PoInTotalBpsMax_Type = Gauge32
_PoInTotalBpsMax_Object = MibTableColumn
poInTotalBpsMax = _PoInTotalBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1001),
    _PoInTotalBpsMax_Type()
)
poInTotalBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInTotalBpsMax.setStatus("current")
_PoOutTotalBpsMax_Type = Gauge32
_PoOutTotalBpsMax_Object = MibTableColumn
poOutTotalBpsMax = _PoOutTotalBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1002),
    _PoOutTotalBpsMax_Type()
)
poOutTotalBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutTotalBpsMax.setStatus("current")
_PoInTotalPpsMax_Type = Gauge32
_PoInTotalPpsMax_Object = MibTableColumn
poInTotalPpsMax = _PoInTotalPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1003),
    _PoInTotalPpsMax_Type()
)
poInTotalPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInTotalPpsMax.setStatus("current")
_PoOutTotalPpsMax_Type = Gauge32
_PoOutTotalPpsMax_Object = MibTableColumn
poOutTotalPpsMax = _PoOutTotalPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1004),
    _PoOutTotalPpsMax_Type()
)
poOutTotalPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutTotalPpsMax.setStatus("current")
_PoInSmallPpsMax_Type = Gauge32
_PoInSmallPpsMax_Object = MibTableColumn
poInSmallPpsMax = _PoInSmallPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1005),
    _PoInSmallPpsMax_Type()
)
poInSmallPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInSmallPpsMax.setStatus("current")
_PoOutSmallPpsMax_Type = Gauge32
_PoOutSmallPpsMax_Object = MibTableColumn
poOutSmallPpsMax = _PoOutSmallPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1006),
    _PoOutSmallPpsMax_Type()
)
poOutSmallPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutSmallPpsMax.setStatus("current")
_PoInMediumPpsMax_Type = Gauge32
_PoInMediumPpsMax_Object = MibTableColumn
poInMediumPpsMax = _PoInMediumPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1007),
    _PoInMediumPpsMax_Type()
)
poInMediumPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInMediumPpsMax.setStatus("current")
_PoOutMediumPpsMax_Type = Gauge32
_PoOutMediumPpsMax_Object = MibTableColumn
poOutMediumPpsMax = _PoOutMediumPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1008),
    _PoOutMediumPpsMax_Type()
)
poOutMediumPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutMediumPpsMax.setStatus("current")
_PoInLargePpsMax_Type = Gauge32
_PoInLargePpsMax_Object = MibTableColumn
poInLargePpsMax = _PoInLargePpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1009),
    _PoInLargePpsMax_Type()
)
poInLargePpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInLargePpsMax.setStatus("current")
_PoOutLargePpsMax_Type = Gauge32
_PoOutLargePpsMax_Object = MibTableColumn
poOutLargePpsMax = _PoOutLargePpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1010),
    _PoOutLargePpsMax_Type()
)
poOutLargePpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutLargePpsMax.setStatus("current")
_PoInDroppedBpsMax_Type = Gauge32
_PoInDroppedBpsMax_Object = MibTableColumn
poInDroppedBpsMax = _PoInDroppedBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1011),
    _PoInDroppedBpsMax_Type()
)
poInDroppedBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInDroppedBpsMax.setStatus("current")
_PoOutDroppedBpsMax_Type = Gauge32
_PoOutDroppedBpsMax_Object = MibTableColumn
poOutDroppedBpsMax = _PoOutDroppedBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1012),
    _PoOutDroppedBpsMax_Type()
)
poOutDroppedBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutDroppedBpsMax.setStatus("current")
_PoInDroppedPpsMax_Type = Gauge32
_PoInDroppedPpsMax_Object = MibTableColumn
poInDroppedPpsMax = _PoInDroppedPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1013),
    _PoInDroppedPpsMax_Type()
)
poInDroppedPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInDroppedPpsMax.setStatus("current")
_PoOutDroppedPpsMax_Type = Gauge32
_PoOutDroppedPpsMax_Object = MibTableColumn
poOutDroppedPpsMax = _PoOutDroppedPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1014),
    _PoOutDroppedPpsMax_Type()
)
poOutDroppedPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutDroppedPpsMax.setStatus("current")
_PoInCharmDroppedBpsMax_Type = Gauge32
_PoInCharmDroppedBpsMax_Object = MibTableColumn
poInCharmDroppedBpsMax = _PoInCharmDroppedBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1015),
    _PoInCharmDroppedBpsMax_Type()
)
poInCharmDroppedBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInCharmDroppedBpsMax.setStatus("current")
_PoOutCharmDroppedBpsMax_Type = Gauge32
_PoOutCharmDroppedBpsMax_Object = MibTableColumn
poOutCharmDroppedBpsMax = _PoOutCharmDroppedBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1016),
    _PoOutCharmDroppedBpsMax_Type()
)
poOutCharmDroppedBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutCharmDroppedBpsMax.setStatus("current")
_PoInFilteredBwthPercentMax_Type = Gauge32
_PoInFilteredBwthPercentMax_Object = MibTableColumn
poInFilteredBwthPercentMax = _PoInFilteredBwthPercentMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1017),
    _PoInFilteredBwthPercentMax_Type()
)
poInFilteredBwthPercentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInFilteredBwthPercentMax.setStatus("current")
_PoOutFilteredBwthPercentMax_Type = Gauge32
_PoOutFilteredBwthPercentMax_Object = MibTableColumn
poOutFilteredBwthPercentMax = _PoOutFilteredBwthPercentMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1018),
    _PoOutFilteredBwthPercentMax_Type()
)
poOutFilteredBwthPercentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutFilteredBwthPercentMax.setStatus("current")
_PoInSynbacklogtallyMax_Type = Gauge32
_PoInSynbacklogtallyMax_Object = MibTableColumn
poInSynbacklogtallyMax = _PoInSynbacklogtallyMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1019),
    _PoInSynbacklogtallyMax_Type()
)
poInSynbacklogtallyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInSynbacklogtallyMax.setStatus("current")
_PoOutSynbacklogtallyMax_Type = Gauge32
_PoOutSynbacklogtallyMax_Object = MibTableColumn
poOutSynbacklogtallyMax = _PoOutSynbacklogtallyMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1020),
    _PoOutSynbacklogtallyMax_Type()
)
poOutSynbacklogtallyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutSynbacklogtallyMax.setStatus("current")
_PoInConnectionMax_Type = Gauge32
_PoInConnectionMax_Object = MibTableColumn
poInConnectionMax = _PoInConnectionMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1021),
    _PoInConnectionMax_Type()
)
poInConnectionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInConnectionMax.setStatus("current")
_PoOutConnectionMax_Type = Gauge32
_PoOutConnectionMax_Object = MibTableColumn
poOutConnectionMax = _PoOutConnectionMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1022),
    _PoOutConnectionMax_Type()
)
poOutConnectionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutConnectionMax.setStatus("current")
_PoInConnreqMax_Type = Gauge32
_PoInConnreqMax_Object = MibTableColumn
poInConnreqMax = _PoInConnreqMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1023),
    _PoInConnreqMax_Type()
)
poInConnreqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInConnreqMax.setStatus("current")
_PoOutConnreqMax_Type = Gauge32
_PoOutConnreqMax_Object = MibTableColumn
poOutConnreqMax = _PoOutConnreqMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1024),
    _PoOutConnreqMax_Type()
)
poOutConnreqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutConnreqMax.setStatus("current")
_PoInActiveHttpGetsMax_Type = Gauge32
_PoInActiveHttpGetsMax_Object = MibTableColumn
poInActiveHttpGetsMax = _PoInActiveHttpGetsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1025),
    _PoInActiveHttpGetsMax_Type()
)
poInActiveHttpGetsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInActiveHttpGetsMax.setStatus("current")
_PoOutActiveHttpGetsMax_Type = Gauge32
_PoOutActiveHttpGetsMax_Object = MibTableColumn
poOutActiveHttpGetsMax = _PoOutActiveHttpGetsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1026),
    _PoOutActiveHttpGetsMax_Type()
)
poOutActiveHttpGetsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutActiveHttpGetsMax.setStatus("current")
_PoInProtectBwthPktsMax_Type = Gauge32
_PoInProtectBwthPktsMax_Object = MibTableColumn
poInProtectBwthPktsMax = _PoInProtectBwthPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1027),
    _PoInProtectBwthPktsMax_Type()
)
poInProtectBwthPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInProtectBwthPktsMax.setStatus("current")
_PoOutProtectBwthPktsMax_Type = Gauge32
_PoOutProtectBwthPktsMax_Object = MibTableColumn
poOutProtectBwthPktsMax = _PoOutProtectBwthPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1028),
    _PoOutProtectBwthPktsMax_Type()
)
poOutProtectBwthPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutProtectBwthPktsMax.setStatus("current")
_PoInFloodPktsMax_Type = Gauge32
_PoInFloodPktsMax_Object = MibTableColumn
poInFloodPktsMax = _PoInFloodPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1029),
    _PoInFloodPktsMax_Type()
)
poInFloodPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInFloodPktsMax.setStatus("current")
_PoOutFloodPktsMax_Type = Gauge32
_PoOutFloodPktsMax_Object = MibTableColumn
poOutFloodPktsMax = _PoOutFloodPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1030),
    _PoOutFloodPktsMax_Type()
)
poOutFloodPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutFloodPktsMax.setStatus("current")
_PoInBlockedProtocolPktsMax_Type = Gauge32
_PoInBlockedProtocolPktsMax_Object = MibTableColumn
poInBlockedProtocolPktsMax = _PoInBlockedProtocolPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1031),
    _PoInBlockedProtocolPktsMax_Type()
)
poInBlockedProtocolPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInBlockedProtocolPktsMax.setStatus("current")
_PoOutBlockedProtocolPktsMax_Type = Gauge32
_PoOutBlockedProtocolPktsMax_Object = MibTableColumn
poOutBlockedProtocolPktsMax = _PoOutBlockedProtocolPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1032),
    _PoOutBlockedProtocolPktsMax_Type()
)
poOutBlockedProtocolPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutBlockedProtocolPktsMax.setStatus("current")
_PoInBlockedStatePktsMax_Type = Gauge32
_PoInBlockedStatePktsMax_Object = MibTableColumn
poInBlockedStatePktsMax = _PoInBlockedStatePktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1033),
    _PoInBlockedStatePktsMax_Type()
)
poInBlockedStatePktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInBlockedStatePktsMax.setStatus("current")
_PoOutBlockedStatePktsMax_Type = Gauge32
_PoOutBlockedStatePktsMax_Object = MibTableColumn
poOutBlockedStatePktsMax = _PoOutBlockedStatePktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1034),
    _PoOutBlockedStatePktsMax_Type()
)
poOutBlockedStatePktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutBlockedStatePktsMax.setStatus("current")
_PoInIpAttackPktsMax_Type = Gauge32
_PoInIpAttackPktsMax_Object = MibTableColumn
poInIpAttackPktsMax = _PoInIpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1035),
    _PoInIpAttackPktsMax_Type()
)
poInIpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInIpAttackPktsMax.setStatus("current")
_PoOutIpAttackPktsMax_Type = Gauge32
_PoOutIpAttackPktsMax_Object = MibTableColumn
poOutIpAttackPktsMax = _PoOutIpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1036),
    _PoOutIpAttackPktsMax_Type()
)
poOutIpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutIpAttackPktsMax.setStatus("current")
_PoInTcpAttackPktsMax_Type = Gauge32
_PoInTcpAttackPktsMax_Object = MibTableColumn
poInTcpAttackPktsMax = _PoInTcpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1037),
    _PoInTcpAttackPktsMax_Type()
)
poInTcpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInTcpAttackPktsMax.setStatus("current")
_PoOutTcpAttackPktsMax_Type = Gauge32
_PoOutTcpAttackPktsMax_Object = MibTableColumn
poOutTcpAttackPktsMax = _PoOutTcpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1038),
    _PoOutTcpAttackPktsMax_Type()
)
poOutTcpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutTcpAttackPktsMax.setStatus("current")
_PoInUdpAttackPktsMax_Type = Gauge32
_PoInUdpAttackPktsMax_Object = MibTableColumn
poInUdpAttackPktsMax = _PoInUdpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1039),
    _PoInUdpAttackPktsMax_Type()
)
poInUdpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInUdpAttackPktsMax.setStatus("current")
_PoOutUdpAttackPktsMax_Type = Gauge32
_PoOutUdpAttackPktsMax_Object = MibTableColumn
poOutUdpAttackPktsMax = _PoOutUdpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1040),
    _PoOutUdpAttackPktsMax_Type()
)
poOutUdpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutUdpAttackPktsMax.setStatus("current")
_PoInIcmpAttackPktsMax_Type = Gauge32
_PoInIcmpAttackPktsMax_Object = MibTableColumn
poInIcmpAttackPktsMax = _PoInIcmpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1041),
    _PoInIcmpAttackPktsMax_Type()
)
poInIcmpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInIcmpAttackPktsMax.setStatus("current")
_PoOutIcmpAttackPktsMax_Type = Gauge32
_PoOutIcmpAttackPktsMax_Object = MibTableColumn
poOutIcmpAttackPktsMax = _PoOutIcmpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1042),
    _PoOutIcmpAttackPktsMax_Type()
)
poOutIcmpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutIcmpAttackPktsMax.setStatus("current")
_PoInOtherIpAttackPktsMax_Type = Gauge32
_PoInOtherIpAttackPktsMax_Object = MibTableColumn
poInOtherIpAttackPktsMax = _PoInOtherIpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1043),
    _PoInOtherIpAttackPktsMax_Type()
)
poInOtherIpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInOtherIpAttackPktsMax.setStatus("current")
_PoOutOtherIpAttackPktsMax_Type = Gauge32
_PoOutOtherIpAttackPktsMax_Object = MibTableColumn
poOutOtherIpAttackPktsMax = _PoOutOtherIpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1044),
    _PoOutOtherIpAttackPktsMax_Type()
)
poOutOtherIpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutOtherIpAttackPktsMax.setStatus("current")
_PoInFragmentAttackPktsMax_Type = Gauge32
_PoInFragmentAttackPktsMax_Object = MibTableColumn
poInFragmentAttackPktsMax = _PoInFragmentAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1045),
    _PoInFragmentAttackPktsMax_Type()
)
poInFragmentAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInFragmentAttackPktsMax.setStatus("current")
_PoOutFragmentAttackPktsMax_Type = Gauge32
_PoOutFragmentAttackPktsMax_Object = MibTableColumn
poOutFragmentAttackPktsMax = _PoOutFragmentAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1046),
    _PoOutFragmentAttackPktsMax_Type()
)
poOutFragmentAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutFragmentAttackPktsMax.setStatus("current")
_PoInBadipPktsMax_Type = Gauge32
_PoInBadipPktsMax_Object = MibTableColumn
poInBadipPktsMax = _PoInBadipPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1047),
    _PoInBadipPktsMax_Type()
)
poInBadipPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInBadipPktsMax.setStatus("current")
_PoOutBadipPktsMax_Type = Gauge32
_PoOutBadipPktsMax_Object = MibTableColumn
poOutBadipPktsMax = _PoOutBadipPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1048),
    _PoOutBadipPktsMax_Type()
)
poOutBadipPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutBadipPktsMax.setStatus("current")
_PoInBadTcpPktsMax_Type = Gauge32
_PoInBadTcpPktsMax_Object = MibTableColumn
poInBadTcpPktsMax = _PoInBadTcpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1049),
    _PoInBadTcpPktsMax_Type()
)
poInBadTcpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInBadTcpPktsMax.setStatus("current")
_PoOutBadTcpPktsMax_Type = Gauge32
_PoOutBadTcpPktsMax_Object = MibTableColumn
poOutBadTcpPktsMax = _PoOutBadTcpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1050),
    _PoOutBadTcpPktsMax_Type()
)
poOutBadTcpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutBadTcpPktsMax.setStatus("current")
_PoInBadUdpPktsMax_Type = Gauge32
_PoInBadUdpPktsMax_Object = MibTableColumn
poInBadUdpPktsMax = _PoInBadUdpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1051),
    _PoInBadUdpPktsMax_Type()
)
poInBadUdpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInBadUdpPktsMax.setStatus("current")
_PoOutBadUdpPktsMax_Type = Gauge32
_PoOutBadUdpPktsMax_Object = MibTableColumn
poOutBadUdpPktsMax = _PoOutBadUdpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1052),
    _PoOutBadUdpPktsMax_Type()
)
poOutBadUdpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutBadUdpPktsMax.setStatus("current")
_PoInBadIcmpPktsMax_Type = Gauge32
_PoInBadIcmpPktsMax_Object = MibTableColumn
poInBadIcmpPktsMax = _PoInBadIcmpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1053),
    _PoInBadIcmpPktsMax_Type()
)
poInBadIcmpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInBadIcmpPktsMax.setStatus("current")
_PoOutBadIcmpPktsMax_Type = Gauge32
_PoOutBadIcmpPktsMax_Object = MibTableColumn
poOutBadIcmpPktsMax = _PoOutBadIcmpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1054),
    _PoOutBadIcmpPktsMax_Type()
)
poOutBadIcmpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutBadIcmpPktsMax.setStatus("current")
_PoInBadOtherIpPktsMax_Type = Gauge32
_PoInBadOtherIpPktsMax_Object = MibTableColumn
poInBadOtherIpPktsMax = _PoInBadOtherIpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1055),
    _PoInBadOtherIpPktsMax_Type()
)
poInBadOtherIpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInBadOtherIpPktsMax.setStatus("current")
_PoOutBadOtherIpPktsMax_Type = Gauge32
_PoOutBadOtherIpPktsMax_Object = MibTableColumn
poOutBadOtherIpPktsMax = _PoOutBadOtherIpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1056),
    _PoOutBadOtherIpPktsMax_Type()
)
poOutBadOtherIpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutBadOtherIpPktsMax.setStatus("current")
_PoInOverloadedMax_Type = Gauge32
_PoInOverloadedMax_Object = MibTableColumn
poInOverloadedMax = _PoInOverloadedMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1057),
    _PoInOverloadedMax_Type()
)
poInOverloadedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInOverloadedMax.setStatus("current")
_PoOutOverloadedMax_Type = Gauge32
_PoOutOverloadedMax_Object = MibTableColumn
poOutOverloadedMax = _PoOutOverloadedMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1058),
    _PoOutOverloadedMax_Type()
)
poOutOverloadedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutOverloadedMax.setStatus("current")
_PoInLatencyMax_Type = Gauge32
_PoInLatencyMax_Object = MibTableColumn
poInLatencyMax = _PoInLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1059),
    _PoInLatencyMax_Type()
)
poInLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInLatencyMax.setStatus("current")
_PoOutLatencyMax_Type = Gauge32
_PoOutLatencyMax_Object = MibTableColumn
poOutLatencyMax = _PoOutLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1060),
    _PoOutLatencyMax_Type()
)
poOutLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutLatencyMax.setStatus("current")
_PoInTotalBytesCnt_Type = Counter64
_PoInTotalBytesCnt_Object = MibTableColumn
poInTotalBytesCnt = _PoInTotalBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1101),
    _PoInTotalBytesCnt_Type()
)
poInTotalBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInTotalBytesCnt.setStatus("current")
_PoOutTotalBytesCnt_Type = Counter64
_PoOutTotalBytesCnt_Object = MibTableColumn
poOutTotalBytesCnt = _PoOutTotalBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1102),
    _PoOutTotalBytesCnt_Type()
)
poOutTotalBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutTotalBytesCnt.setStatus("current")
_PoInDroppedBytesCnt_Type = Counter64
_PoInDroppedBytesCnt_Object = MibTableColumn
poInDroppedBytesCnt = _PoInDroppedBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1103),
    _PoInDroppedBytesCnt_Type()
)
poInDroppedBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInDroppedBytesCnt.setStatus("current")
_PoOutDroppedBytesCnt_Type = Counter64
_PoOutDroppedBytesCnt_Object = MibTableColumn
poOutDroppedBytesCnt = _PoOutDroppedBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1104),
    _PoOutDroppedBytesCnt_Type()
)
poOutDroppedBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutDroppedBytesCnt.setStatus("current")
_PoInCharmDroppedBytesCnt_Type = Counter64
_PoInCharmDroppedBytesCnt_Object = MibTableColumn
poInCharmDroppedBytesCnt = _PoInCharmDroppedBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1105),
    _PoInCharmDroppedBytesCnt_Type()
)
poInCharmDroppedBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInCharmDroppedBytesCnt.setStatus("current")
_PoOutCharmDroppedBytesCnt_Type = Counter64
_PoOutCharmDroppedBytesCnt_Object = MibTableColumn
poOutCharmDroppedBytesCnt = _PoOutCharmDroppedBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1106),
    _PoOutCharmDroppedBytesCnt_Type()
)
poOutCharmDroppedBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutCharmDroppedBytesCnt.setStatus("current")
_PoInTotalPpsCnt_Type = Counter32
_PoInTotalPpsCnt_Object = MibTableColumn
poInTotalPpsCnt = _PoInTotalPpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1109),
    _PoInTotalPpsCnt_Type()
)
poInTotalPpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInTotalPpsCnt.setStatus("current")
_PoOutTotalPpsCnt_Type = Counter32
_PoOutTotalPpsCnt_Object = MibTableColumn
poOutTotalPpsCnt = _PoOutTotalPpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1110),
    _PoOutTotalPpsCnt_Type()
)
poOutTotalPpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutTotalPpsCnt.setStatus("current")
_PoInSmallPpsCnt_Type = Counter32
_PoInSmallPpsCnt_Object = MibTableColumn
poInSmallPpsCnt = _PoInSmallPpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1111),
    _PoInSmallPpsCnt_Type()
)
poInSmallPpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInSmallPpsCnt.setStatus("current")
_PoOutSmallPpsCnt_Type = Counter32
_PoOutSmallPpsCnt_Object = MibTableColumn
poOutSmallPpsCnt = _PoOutSmallPpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1112),
    _PoOutSmallPpsCnt_Type()
)
poOutSmallPpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutSmallPpsCnt.setStatus("current")
_PoInMediumPpsCnt_Type = Counter32
_PoInMediumPpsCnt_Object = MibTableColumn
poInMediumPpsCnt = _PoInMediumPpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1113),
    _PoInMediumPpsCnt_Type()
)
poInMediumPpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInMediumPpsCnt.setStatus("current")
_PoOutMediumPpsCnt_Type = Counter32
_PoOutMediumPpsCnt_Object = MibTableColumn
poOutMediumPpsCnt = _PoOutMediumPpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1114),
    _PoOutMediumPpsCnt_Type()
)
poOutMediumPpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutMediumPpsCnt.setStatus("current")
_PoInLargePpsCnt_Type = Counter32
_PoInLargePpsCnt_Object = MibTableColumn
poInLargePpsCnt = _PoInLargePpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1115),
    _PoInLargePpsCnt_Type()
)
poInLargePpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInLargePpsCnt.setStatus("current")
_PoOutLargePpsCnt_Type = Counter32
_PoOutLargePpsCnt_Object = MibTableColumn
poOutLargePpsCnt = _PoOutLargePpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1116),
    _PoOutLargePpsCnt_Type()
)
poOutLargePpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutLargePpsCnt.setStatus("current")
_PoInDroppedPpsCnt_Type = Counter32
_PoInDroppedPpsCnt_Object = MibTableColumn
poInDroppedPpsCnt = _PoInDroppedPpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1119),
    _PoInDroppedPpsCnt_Type()
)
poInDroppedPpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInDroppedPpsCnt.setStatus("current")
_PoOutDroppedPpsCnt_Type = Counter32
_PoOutDroppedPpsCnt_Object = MibTableColumn
poOutDroppedPpsCnt = _PoOutDroppedPpsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1120),
    _PoOutDroppedPpsCnt_Type()
)
poOutDroppedPpsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutDroppedPpsCnt.setStatus("current")
_PoInFilteredBwthPercentCnt_Type = Counter32
_PoInFilteredBwthPercentCnt_Object = MibTableColumn
poInFilteredBwthPercentCnt = _PoInFilteredBwthPercentCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1121),
    _PoInFilteredBwthPercentCnt_Type()
)
poInFilteredBwthPercentCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInFilteredBwthPercentCnt.setStatus("current")
_PoOutFilteredBwthPercentCnt_Type = Counter32
_PoOutFilteredBwthPercentCnt_Object = MibTableColumn
poOutFilteredBwthPercentCnt = _PoOutFilteredBwthPercentCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1122),
    _PoOutFilteredBwthPercentCnt_Type()
)
poOutFilteredBwthPercentCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutFilteredBwthPercentCnt.setStatus("current")
_PoInConnreqCnt_Type = Counter32
_PoInConnreqCnt_Object = MibTableColumn
poInConnreqCnt = _PoInConnreqCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1123),
    _PoInConnreqCnt_Type()
)
poInConnreqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poInConnreqCnt.setStatus("current")
_PoOutConnreqCnt_Type = Counter32
_PoOutConnreqCnt_Object = MibTableColumn
poOutConnreqCnt = _PoOutConnreqCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 3, 1, 1124),
    _PoOutConnreqCnt_Type()
)
poOutConnreqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poOutConnreqCnt.setStatus("current")
_PoIncidentTable_Object = MibTable
poIncidentTable = _PoIncidentTable_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 5)
)
if mibBuilder.loadTexts:
    poIncidentTable.setStatus("current")
_PoIncidentEntry_Object = MibTableRow
poIncidentEntry = _PoIncidentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 5, 1)
)
poIncidentEntry.setIndexNames(
    (0, "DDOSSECURE4-MIB", "poIncidentYear"),
    (0, "DDOSSECURE4-MIB", "poIncidentMonth"),
    (0, "DDOSSECURE4-MIB", "poIncidentDay"),
    (0, "DDOSSECURE4-MIB", "poIncidentNumber"),
)
if mibBuilder.loadTexts:
    poIncidentEntry.setStatus("current")
_PoIncidentYear_Type = LocalIndex
_PoIncidentYear_Object = MibTableColumn
poIncidentYear = _PoIncidentYear_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 5, 1, 1),
    _PoIncidentYear_Type()
)
poIncidentYear.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    poIncidentYear.setStatus("current")
_PoIncidentMonth_Type = LocalIndex
_PoIncidentMonth_Object = MibTableColumn
poIncidentMonth = _PoIncidentMonth_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 5, 1, 2),
    _PoIncidentMonth_Type()
)
poIncidentMonth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    poIncidentMonth.setStatus("current")
_PoIncidentDay_Type = LocalIndex
_PoIncidentDay_Object = MibTableColumn
poIncidentDay = _PoIncidentDay_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 5, 1, 3),
    _PoIncidentDay_Type()
)
poIncidentDay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    poIncidentDay.setStatus("current")
_PoIncidentNumber_Type = LocalIndex
_PoIncidentNumber_Object = MibTableColumn
poIncidentNumber = _PoIncidentNumber_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 5, 1, 4),
    _PoIncidentNumber_Type()
)
poIncidentNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    poIncidentNumber.setStatus("current")
_PoIncidentPortalName_Type = DisplayString
_PoIncidentPortalName_Object = MibTableColumn
poIncidentPortalName = _PoIncidentPortalName_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 5, 1, 5),
    _PoIncidentPortalName_Type()
)
poIncidentPortalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poIncidentPortalName.setStatus("current")
_PoIncidentStart_Type = DateAndTime
_PoIncidentStart_Object = MibTableColumn
poIncidentStart = _PoIncidentStart_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 5, 1, 6),
    _PoIncidentStart_Type()
)
poIncidentStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poIncidentStart.setStatus("current")
_PoIncidentAddress_Type = DisplayString
_PoIncidentAddress_Object = MibTableColumn
poIncidentAddress = _PoIncidentAddress_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 5, 1, 7),
    _PoIncidentAddress_Type()
)
poIncidentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poIncidentAddress.setStatus("current")
_PoIncidentType_Type = DisplayString
_PoIncidentType_Object = MibTableColumn
poIncidentType = _PoIncidentType_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 5, 1, 8),
    _PoIncidentType_Type()
)
poIncidentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poIncidentType.setStatus("current")
_PoIncidentDirection_Type = Direction
_PoIncidentDirection_Object = MibTableColumn
poIncidentDirection = _PoIncidentDirection_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 5, 1, 9),
    _PoIncidentDirection_Type()
)
poIncidentDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poIncidentDirection.setStatus("current")
_PoIncidentPeakRate_Type = Gauge32
_PoIncidentPeakRate_Object = MibTableColumn
poIncidentPeakRate = _PoIncidentPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 5, 1, 10),
    _PoIncidentPeakRate_Type()
)
poIncidentPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poIncidentPeakRate.setStatus("current")
_PoIncidentDropped_Type = Gauge32
_PoIncidentDropped_Object = MibTableColumn
poIncidentDropped = _PoIncidentDropped_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 5, 1, 11),
    _PoIncidentDropped_Type()
)
poIncidentDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poIncidentDropped.setStatus("current")
_PoFiltersTable_Object = MibTable
poFiltersTable = _PoFiltersTable_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 6)
)
if mibBuilder.loadTexts:
    poFiltersTable.setStatus("current")
_PoFiltersEntry_Object = MibTableRow
poFiltersEntry = _PoFiltersEntry_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 6, 1)
)
poFiltersEntry.setIndexNames(
    (0, "DDOSSECURE4-MIB", "poFilterIndex"),
)
if mibBuilder.loadTexts:
    poFiltersEntry.setStatus("current")
_PoFilterIndex_Type = LocalIndex
_PoFilterIndex_Object = MibTableColumn
poFilterIndex = _PoFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 6, 1, 1),
    _PoFilterIndex_Type()
)
poFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    poFilterIndex.setStatus("current")
_PoFilterName_Type = DisplayString
_PoFilterName_Object = MibTableColumn
poFilterName = _PoFilterName_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 6, 1, 2),
    _PoFilterName_Type()
)
poFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poFilterName.setStatus("current")
_PoTcpPortsList_Type = DisplayString
_PoTcpPortsList_Object = MibTableColumn
poTcpPortsList = _PoTcpPortsList_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 6, 1, 3),
    _PoTcpPortsList_Type()
)
poTcpPortsList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poTcpPortsList.setStatus("current")
_PoUdpPortsList_Type = DisplayString
_PoUdpPortsList_Object = MibTableColumn
poUdpPortsList = _PoUdpPortsList_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 6, 1, 4),
    _PoUdpPortsList_Type()
)
poUdpPortsList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poUdpPortsList.setStatus("current")
_PoIcmpTypesList_Type = DisplayString
_PoIcmpTypesList_Object = MibTableColumn
poIcmpTypesList = _PoIcmpTypesList_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 6, 1, 5),
    _PoIcmpTypesList_Type()
)
poIcmpTypesList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poIcmpTypesList.setStatus("current")
_PoIpProtocolsList_Type = DisplayString
_PoIpProtocolsList_Object = MibTableColumn
poIpProtocolsList = _PoIpProtocolsList_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 5, 6, 1, 6),
    _PoIpProtocolsList_Type()
)
poIpProtocolsList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poIpProtocolsList.setStatus("current")
_JddsProtected_ObjectIdentity = ObjectIdentity
jddsProtected = _JddsProtected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6)
)
_PrConfigTable_Object = MibTable
prConfigTable = _PrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 1)
)
if mibBuilder.loadTexts:
    prConfigTable.setStatus("current")
_PrConfigEntry_Object = MibTableRow
prConfigEntry = _PrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 1, 1)
)
prConfigEntry.setIndexNames(
    (0, "DDOSSECURE4-MIB", "prConfigInetAddressType"),
    (0, "DDOSSECURE4-MIB", "prConfigInetAddress"),
)
if mibBuilder.loadTexts:
    prConfigEntry.setStatus("current")
_PrConfigInetAddressType_Type = InetAddressType
_PrConfigInetAddressType_Object = MibTableColumn
prConfigInetAddressType = _PrConfigInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 1, 1, 1),
    _PrConfigInetAddressType_Type()
)
prConfigInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prConfigInetAddressType.setStatus("current")


class _PrConfigInetAddress_Type(InetAddress):
    """Custom type prConfigInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_PrConfigInetAddress_Type.__name__ = "InetAddress"
_PrConfigInetAddress_Object = MibTableColumn
prConfigInetAddress = _PrConfigInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 1, 1, 2),
    _PrConfigInetAddress_Type()
)
prConfigInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prConfigInetAddress.setStatus("current")
_PrHostName_Type = DisplayString
_PrHostName_Object = MibTableColumn
prHostName = _PrHostName_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 1, 1, 3),
    _PrHostName_Type()
)
prHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prHostName.setStatus("current")
_PrTcpBacklog_Type = Gauge32
_PrTcpBacklog_Object = MibTableColumn
prTcpBacklog = _PrTcpBacklog_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 1, 1, 4),
    _PrTcpBacklog_Type()
)
prTcpBacklog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prTcpBacklog.setStatus("current")
_PrMaxConnections_Type = Gauge32
_PrMaxConnections_Object = MibTableColumn
prMaxConnections = _PrMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 1, 1, 5),
    _PrMaxConnections_Type()
)
prMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMaxConnections.setStatus("current")
_PrMaxConnectionRate_Type = Gauge32
_PrMaxConnectionRate_Object = MibTableColumn
prMaxConnectionRate = _PrMaxConnectionRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 1, 1, 6),
    _PrMaxConnectionRate_Type()
)
prMaxConnectionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMaxConnectionRate.setStatus("current")
_PrInFilterName_Type = DisplayString
_PrInFilterName_Object = MibTableColumn
prInFilterName = _PrInFilterName_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 1, 1, 7),
    _PrInFilterName_Type()
)
prInFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInFilterName.setStatus("current")
_PrOutFilterName_Type = DisplayString
_PrOutFilterName_Object = MibTableColumn
prOutFilterName = _PrOutFilterName_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 1, 1, 8),
    _PrOutFilterName_Type()
)
prOutFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutFilterName.setStatus("current")
_PrSendTcpRejects_Type = TruthValue
_PrSendTcpRejects_Object = MibTableColumn
prSendTcpRejects = _PrSendTcpRejects_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 1, 1, 9),
    _PrSendTcpRejects_Type()
)
prSendTcpRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prSendTcpRejects.setStatus("current")
_PrTrackSoap_Type = TruthValue
_PrTrackSoap_Object = MibTableColumn
prTrackSoap = _PrTrackSoap_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 1, 1, 10),
    _PrTrackSoap_Type()
)
prTrackSoap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prTrackSoap.setStatus("current")
_PrOperationMode_Type = DisplayString
_PrOperationMode_Object = MibTableColumn
prOperationMode = _PrOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 1, 1, 11),
    _PrOperationMode_Type()
)
prOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOperationMode.setStatus("current")
_PrMaxGets_Type = Gauge32
_PrMaxGets_Object = MibTableColumn
prMaxGets = _PrMaxGets_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 1, 1, 12),
    _PrMaxGets_Type()
)
prMaxGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMaxGets.setStatus("current")
_PrFragsDisabled_Type = TruthValue
_PrFragsDisabled_Object = MibTableColumn
prFragsDisabled = _PrFragsDisabled_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 1, 1, 13),
    _PrFragsDisabled_Type()
)
prFragsDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prFragsDisabled.setStatus("current")
_PrStatsTable_Object = MibTable
prStatsTable = _PrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3)
)
if mibBuilder.loadTexts:
    prStatsTable.setStatus("current")
_PrStatsEntry_Object = MibTableRow
prStatsEntry = _PrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1)
)
prStatsEntry.setIndexNames(
    (0, "DDOSSECURE4-MIB", "prInetAddressType"),
    (0, "DDOSSECURE4-MIB", "prInetAddress"),
)
if mibBuilder.loadTexts:
    prStatsEntry.setStatus("current")
_PrInetAddressType_Type = InetAddressType
_PrInetAddressType_Object = MibTableColumn
prInetAddressType = _PrInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1),
    _PrInetAddressType_Type()
)
prInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prInetAddressType.setStatus("current")


class _PrInetAddress_Type(InetAddress):
    """Custom type prInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_PrInetAddress_Type.__name__ = "InetAddress"
_PrInetAddress_Object = MibTableColumn
prInetAddress = _PrInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 2),
    _PrInetAddress_Type()
)
prInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prInetAddress.setStatus("current")
_PrBandwidth_Type = TruthValue
_PrBandwidth_Object = MibTableColumn
prBandwidth = _PrBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 101),
    _PrBandwidth_Type()
)
prBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prBandwidth.setStatus("current")
_PrFlood_Type = TruthValue
_PrFlood_Object = MibTableColumn
prFlood = _PrFlood_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 102),
    _PrFlood_Type()
)
prFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prFlood.setStatus("current")
_PrBlockedProtocol_Type = TruthValue
_PrBlockedProtocol_Object = MibTableColumn
prBlockedProtocol = _PrBlockedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 103),
    _PrBlockedProtocol_Type()
)
prBlockedProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prBlockedProtocol.setStatus("current")
_PrBlockedState_Type = TruthValue
_PrBlockedState_Object = MibTableColumn
prBlockedState = _PrBlockedState_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 104),
    _PrBlockedState_Type()
)
prBlockedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prBlockedState.setStatus("current")
_PrIpAttack_Type = TruthValue
_PrIpAttack_Object = MibTableColumn
prIpAttack = _PrIpAttack_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 105),
    _PrIpAttack_Type()
)
prIpAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prIpAttack.setStatus("current")
_PrTcpAttack_Type = TruthValue
_PrTcpAttack_Object = MibTableColumn
prTcpAttack = _PrTcpAttack_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 106),
    _PrTcpAttack_Type()
)
prTcpAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prTcpAttack.setStatus("current")
_PrUdpAttack_Type = TruthValue
_PrUdpAttack_Object = MibTableColumn
prUdpAttack = _PrUdpAttack_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 107),
    _PrUdpAttack_Type()
)
prUdpAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prUdpAttack.setStatus("current")
_PrIcmpAttack_Type = TruthValue
_PrIcmpAttack_Object = MibTableColumn
prIcmpAttack = _PrIcmpAttack_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 108),
    _PrIcmpAttack_Type()
)
prIcmpAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prIcmpAttack.setStatus("current")
_PrOtherIpAttack_Type = TruthValue
_PrOtherIpAttack_Object = MibTableColumn
prOtherIpAttack = _PrOtherIpAttack_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 109),
    _PrOtherIpAttack_Type()
)
prOtherIpAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOtherIpAttack.setStatus("current")
_PrFragAttack_Type = TruthValue
_PrFragAttack_Object = MibTableColumn
prFragAttack = _PrFragAttack_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 110),
    _PrFragAttack_Type()
)
prFragAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prFragAttack.setStatus("current")
_PrBadIp_Type = TruthValue
_PrBadIp_Object = MibTableColumn
prBadIp = _PrBadIp_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 111),
    _PrBadIp_Type()
)
prBadIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prBadIp.setStatus("current")
_PrBadTcp_Type = TruthValue
_PrBadTcp_Object = MibTableColumn
prBadTcp = _PrBadTcp_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 112),
    _PrBadTcp_Type()
)
prBadTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prBadTcp.setStatus("current")
_PrBadUdp_Type = TruthValue
_PrBadUdp_Object = MibTableColumn
prBadUdp = _PrBadUdp_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 113),
    _PrBadUdp_Type()
)
prBadUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prBadUdp.setStatus("current")
_PrBadIcmp_Type = TruthValue
_PrBadIcmp_Object = MibTableColumn
prBadIcmp = _PrBadIcmp_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 114),
    _PrBadIcmp_Type()
)
prBadIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prBadIcmp.setStatus("current")
_PrBadOtherIp_Type = TruthValue
_PrBadOtherIp_Object = MibTableColumn
prBadOtherIp = _PrBadOtherIp_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 115),
    _PrBadOtherIp_Type()
)
prBadOtherIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prBadOtherIp.setStatus("current")
_PrOverloaded_Type = TruthValue
_PrOverloaded_Object = MibTableColumn
prOverloaded = _PrOverloaded_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 116),
    _PrOverloaded_Type()
)
prOverloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOverloaded.setStatus("current")
_PrInSyn_Type = Gauge32
_PrInSyn_Object = MibTableColumn
prInSyn = _PrInSyn_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 201),
    _PrInSyn_Type()
)
prInSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInSyn.setStatus("current")
_PrOutSyn_Type = Gauge32
_PrOutSyn_Object = MibTableColumn
prOutSyn = _PrOutSyn_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 202),
    _PrOutSyn_Type()
)
prOutSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutSyn.setStatus("current")
_PrInSynAck_Type = Gauge32
_PrInSynAck_Object = MibTableColumn
prInSynAck = _PrInSynAck_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 203),
    _PrInSynAck_Type()
)
prInSynAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInSynAck.setStatus("current")
_PrOutSynAck_Type = Gauge32
_PrOutSynAck_Object = MibTableColumn
prOutSynAck = _PrOutSynAck_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 204),
    _PrOutSynAck_Type()
)
prOutSynAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutSynAck.setStatus("current")
_PrInSynSyn_Type = Gauge32
_PrInSynSyn_Object = MibTableColumn
prInSynSyn = _PrInSynSyn_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 205),
    _PrInSynSyn_Type()
)
prInSynSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInSynSyn.setStatus("current")
_PrOutSynSyn_Type = Gauge32
_PrOutSynSyn_Object = MibTableColumn
prOutSynSyn = _PrOutSynSyn_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 206),
    _PrOutSynSyn_Type()
)
prOutSynSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutSynSyn.setStatus("current")
_PrInAck_Type = Gauge32
_PrInAck_Object = MibTableColumn
prInAck = _PrInAck_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 207),
    _PrInAck_Type()
)
prInAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInAck.setStatus("current")
_PrOutAck_Type = Gauge32
_PrOutAck_Object = MibTableColumn
prOutAck = _PrOutAck_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 208),
    _PrOutAck_Type()
)
prOutAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutAck.setStatus("current")
_PrInPendAck_Type = Gauge32
_PrInPendAck_Object = MibTableColumn
prInPendAck = _PrInPendAck_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 209),
    _PrInPendAck_Type()
)
prInPendAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInPendAck.setStatus("current")
_PrOutPendAck_Type = Gauge32
_PrOutPendAck_Object = MibTableColumn
prOutPendAck = _PrOutPendAck_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 210),
    _PrOutPendAck_Type()
)
prOutPendAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutPendAck.setStatus("current")
_PrInGet_Type = Gauge32
_PrInGet_Object = MibTableColumn
prInGet = _PrInGet_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 211),
    _PrInGet_Type()
)
prInGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInGet.setStatus("current")
_PrOutGet_Type = Gauge32
_PrOutGet_Object = MibTableColumn
prOutGet = _PrOutGet_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 212),
    _PrOutGet_Type()
)
prOutGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutGet.setStatus("current")
_PrInEst_Type = Gauge32
_PrInEst_Object = MibTableColumn
prInEst = _PrInEst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 213),
    _PrInEst_Type()
)
prInEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInEst.setStatus("current")
_PrOutEst_Type = Gauge32
_PrOutEst_Object = MibTableColumn
prOutEst = _PrOutEst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 214),
    _PrOutEst_Type()
)
prOutEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutEst.setStatus("current")
_PrInFin1Src_Type = Gauge32
_PrInFin1Src_Object = MibTableColumn
prInFin1Src = _PrInFin1Src_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 215),
    _PrInFin1Src_Type()
)
prInFin1Src.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInFin1Src.setStatus("current")
_PrOutFin1Src_Type = Gauge32
_PrOutFin1Src_Object = MibTableColumn
prOutFin1Src = _PrOutFin1Src_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 216),
    _PrOutFin1Src_Type()
)
prOutFin1Src.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutFin1Src.setStatus("current")
_PrInFin2Src_Type = Gauge32
_PrInFin2Src_Object = MibTableColumn
prInFin2Src = _PrInFin2Src_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 217),
    _PrInFin2Src_Type()
)
prInFin2Src.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInFin2Src.setStatus("current")
_PrOutFin2Src_Type = Gauge32
_PrOutFin2Src_Object = MibTableColumn
prOutFin2Src = _PrOutFin2Src_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 218),
    _PrOutFin2Src_Type()
)
prOutFin2Src.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutFin2Src.setStatus("current")
_PrInFin3Src_Type = Gauge32
_PrInFin3Src_Object = MibTableColumn
prInFin3Src = _PrInFin3Src_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 219),
    _PrInFin3Src_Type()
)
prInFin3Src.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInFin3Src.setStatus("current")
_PrOutFin3Src_Type = Gauge32
_PrOutFin3Src_Object = MibTableColumn
prOutFin3Src = _PrOutFin3Src_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 220),
    _PrOutFin3Src_Type()
)
prOutFin3Src.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutFin3Src.setStatus("current")
_PrInFinFin_Type = Gauge32
_PrInFinFin_Object = MibTableColumn
prInFinFin = _PrInFinFin_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 221),
    _PrInFinFin_Type()
)
prInFinFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInFinFin.setStatus("current")
_PrOutFinFin_Type = Gauge32
_PrOutFinFin_Object = MibTableColumn
prOutFinFin = _PrOutFinFin_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 222),
    _PrOutFinFin_Type()
)
prOutFinFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutFinFin.setStatus("current")
_PrInFin1Dst_Type = Gauge32
_PrInFin1Dst_Object = MibTableColumn
prInFin1Dst = _PrInFin1Dst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 223),
    _PrInFin1Dst_Type()
)
prInFin1Dst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInFin1Dst.setStatus("current")
_PrOutFin1Dst_Type = Gauge32
_PrOutFin1Dst_Object = MibTableColumn
prOutFin1Dst = _PrOutFin1Dst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 224),
    _PrOutFin1Dst_Type()
)
prOutFin1Dst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutFin1Dst.setStatus("current")
_PrInFin2Dst_Type = Gauge32
_PrInFin2Dst_Object = MibTableColumn
prInFin2Dst = _PrInFin2Dst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 225),
    _PrInFin2Dst_Type()
)
prInFin2Dst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInFin2Dst.setStatus("current")
_PrOutFin2Dst_Type = Gauge32
_PrOutFin2Dst_Object = MibTableColumn
prOutFin2Dst = _PrOutFin2Dst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 226),
    _PrOutFin2Dst_Type()
)
prOutFin2Dst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutFin2Dst.setStatus("current")
_PrInFin3Dst_Type = Gauge32
_PrInFin3Dst_Object = MibTableColumn
prInFin3Dst = _PrInFin3Dst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 227),
    _PrInFin3Dst_Type()
)
prInFin3Dst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInFin3Dst.setStatus("current")
_PrOutFin3Dst_Type = Gauge32
_PrOutFin3Dst_Object = MibTableColumn
prOutFin3Dst = _PrOutFin3Dst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 228),
    _PrOutFin3Dst_Type()
)
prOutFin3Dst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutFin3Dst.setStatus("current")
_PrInCls_Type = Gauge32
_PrInCls_Object = MibTableColumn
prInCls = _PrInCls_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 229),
    _PrInCls_Type()
)
prInCls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInCls.setStatus("current")
_PrOutCls_Type = Gauge32
_PrOutCls_Object = MibTableColumn
prOutCls = _PrOutCls_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 230),
    _PrOutCls_Type()
)
prOutCls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutCls.setStatus("current")
_PrInRst_Type = Gauge32
_PrInRst_Object = MibTableColumn
prInRst = _PrInRst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 231),
    _PrInRst_Type()
)
prInRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInRst.setStatus("current")
_PrOutRst_Type = Gauge32
_PrOutRst_Object = MibTableColumn
prOutRst = _PrOutRst_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 232),
    _PrOutRst_Type()
)
prOutRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutRst.setStatus("current")
_PrInRstCls_Type = Gauge32
_PrInRstCls_Object = MibTableColumn
prInRstCls = _PrInRstCls_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 233),
    _PrInRstCls_Type()
)
prInRstCls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInRstCls.setStatus("current")
_PrOutRstCls_Type = Gauge32
_PrOutRstCls_Object = MibTableColumn
prOutRstCls = _PrOutRstCls_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 234),
    _PrOutRstCls_Type()
)
prOutRstCls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutRstCls.setStatus("current")
_PrInUnknown_Type = Gauge32
_PrInUnknown_Object = MibTableColumn
prInUnknown = _PrInUnknown_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 235),
    _PrInUnknown_Type()
)
prInUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInUnknown.setStatus("current")
_PrOutUnknown_Type = Gauge32
_PrOutUnknown_Object = MibTableColumn
prOutUnknown = _PrOutUnknown_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 236),
    _PrOutUnknown_Type()
)
prOutUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutUnknown.setStatus("current")
_PrInGets_Type = Gauge32
_PrInGets_Object = MibTableColumn
prInGets = _PrInGets_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 237),
    _PrInGets_Type()
)
prInGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInGets.setStatus("current")
_PrOutGets_Type = Gauge32
_PrOutGets_Object = MibTableColumn
prOutGets = _PrOutGets_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 238),
    _PrOutGets_Type()
)
prOutGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutGets.setStatus("current")
_PrOverloadedFlag_Type = TruthValue
_PrOverloadedFlag_Object = MibTableColumn
prOverloadedFlag = _PrOverloadedFlag_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 301),
    _PrOverloadedFlag_Type()
)
prOverloadedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOverloadedFlag.setStatus("current")
_PrInTcpConnTally_Type = Counter32
_PrInTcpConnTally_Object = MibTableColumn
prInTcpConnTally = _PrInTcpConnTally_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 401),
    _PrInTcpConnTally_Type()
)
prInTcpConnTally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInTcpConnTally.setStatus("current")
_PrOutTcpConnTally_Type = Counter32
_PrOutTcpConnTally_Object = MibTableColumn
prOutTcpConnTally = _PrOutTcpConnTally_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 402),
    _PrOutTcpConnTally_Type()
)
prOutTcpConnTally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutTcpConnTally.setStatus("current")
_PrInSynBacklogTally_Type = Counter32
_PrInSynBacklogTally_Object = MibTableColumn
prInSynBacklogTally = _PrInSynBacklogTally_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 403),
    _PrInSynBacklogTally_Type()
)
prInSynBacklogTally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInSynBacklogTally.setStatus("current")
_PrInTotalBytesCnt_Type = Counter64
_PrInTotalBytesCnt_Object = MibTableColumn
prInTotalBytesCnt = _PrInTotalBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 501),
    _PrInTotalBytesCnt_Type()
)
prInTotalBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInTotalBytesCnt.setStatus("current")
_PrOutTotalBytesCnt_Type = Counter64
_PrOutTotalBytesCnt_Object = MibTableColumn
prOutTotalBytesCnt = _PrOutTotalBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 502),
    _PrOutTotalBytesCnt_Type()
)
prOutTotalBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutTotalBytesCnt.setStatus("current")
_PrInDroppedBytesCnt_Type = Counter64
_PrInDroppedBytesCnt_Object = MibTableColumn
prInDroppedBytesCnt = _PrInDroppedBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 503),
    _PrInDroppedBytesCnt_Type()
)
prInDroppedBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInDroppedBytesCnt.setStatus("current")
_PrOutDroppedBytesCnt_Type = Counter64
_PrOutDroppedBytesCnt_Object = MibTableColumn
prOutDroppedBytesCnt = _PrOutDroppedBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 504),
    _PrOutDroppedBytesCnt_Type()
)
prOutDroppedBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutDroppedBytesCnt.setStatus("current")
_PrInCharmDroppedBytesCnt_Type = Counter64
_PrInCharmDroppedBytesCnt_Object = MibTableColumn
prInCharmDroppedBytesCnt = _PrInCharmDroppedBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 505),
    _PrInCharmDroppedBytesCnt_Type()
)
prInCharmDroppedBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInCharmDroppedBytesCnt.setStatus("current")
_PrOutCharmDroppedBytesCnt_Type = Counter64
_PrOutCharmDroppedBytesCnt_Object = MibTableColumn
prOutCharmDroppedBytesCnt = _PrOutCharmDroppedBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 506),
    _PrOutCharmDroppedBytesCnt_Type()
)
prOutCharmDroppedBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutCharmDroppedBytesCnt.setStatus("current")
_PrInTotalPpsMax_Type = Gauge32
_PrInTotalPpsMax_Object = MibTableColumn
prInTotalPpsMax = _PrInTotalPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 601),
    _PrInTotalPpsMax_Type()
)
prInTotalPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInTotalPpsMax.setStatus("current")
_PrOutTotalPpsMax_Type = Gauge32
_PrOutTotalPpsMax_Object = MibTableColumn
prOutTotalPpsMax = _PrOutTotalPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 602),
    _PrOutTotalPpsMax_Type()
)
prOutTotalPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutTotalPpsMax.setStatus("current")
_PrInDroppedPpsMax_Type = Gauge32
_PrInDroppedPpsMax_Object = MibTableColumn
prInDroppedPpsMax = _PrInDroppedPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 603),
    _PrInDroppedPpsMax_Type()
)
prInDroppedPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInDroppedPpsMax.setStatus("current")
_PrOutDroppedPpsMax_Type = Gauge32
_PrOutDroppedPpsMax_Object = MibTableColumn
prOutDroppedPpsMax = _PrOutDroppedPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 604),
    _PrOutDroppedPpsMax_Type()
)
prOutDroppedPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutDroppedPpsMax.setStatus("current")
_PrInTotalBpsMax_Type = Gauge32
_PrInTotalBpsMax_Object = MibTableColumn
prInTotalBpsMax = _PrInTotalBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 701),
    _PrInTotalBpsMax_Type()
)
prInTotalBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInTotalBpsMax.setStatus("current")
_PrOutTotalBpsMax_Type = Gauge32
_PrOutTotalBpsMax_Object = MibTableColumn
prOutTotalBpsMax = _PrOutTotalBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 702),
    _PrOutTotalBpsMax_Type()
)
prOutTotalBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutTotalBpsMax.setStatus("current")
_PrInDroppedBpsMax_Type = Gauge32
_PrInDroppedBpsMax_Object = MibTableColumn
prInDroppedBpsMax = _PrInDroppedBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 703),
    _PrInDroppedBpsMax_Type()
)
prInDroppedBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInDroppedBpsMax.setStatus("current")
_PrOutDroppedBpsMax_Type = Gauge32
_PrOutDroppedBpsMax_Object = MibTableColumn
prOutDroppedBpsMax = _PrOutDroppedBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 704),
    _PrOutDroppedBpsMax_Type()
)
prOutDroppedBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutDroppedBpsMax.setStatus("current")
_PrInCharmDroppedBpsMax_Type = Gauge32
_PrInCharmDroppedBpsMax_Object = MibTableColumn
prInCharmDroppedBpsMax = _PrInCharmDroppedBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 705),
    _PrInCharmDroppedBpsMax_Type()
)
prInCharmDroppedBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInCharmDroppedBpsMax.setStatus("current")
_PrOutCharmDroppedBpsMax_Type = Gauge32
_PrOutCharmDroppedBpsMax_Object = MibTableColumn
prOutCharmDroppedBpsMax = _PrOutCharmDroppedBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 706),
    _PrOutCharmDroppedBpsMax_Type()
)
prOutCharmDroppedBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutCharmDroppedBpsMax.setStatus("current")
_PrInProtectBwthPktsCnt_Type = Counter32
_PrInProtectBwthPktsCnt_Object = MibTableColumn
prInProtectBwthPktsCnt = _PrInProtectBwthPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 801),
    _PrInProtectBwthPktsCnt_Type()
)
prInProtectBwthPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInProtectBwthPktsCnt.setStatus("current")
_PrOutProtectBwthPktsCnt_Type = Counter32
_PrOutProtectBwthPktsCnt_Object = MibTableColumn
prOutProtectBwthPktsCnt = _PrOutProtectBwthPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 802),
    _PrOutProtectBwthPktsCnt_Type()
)
prOutProtectBwthPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutProtectBwthPktsCnt.setStatus("current")
_PrInFloodPktsCnt_Type = Counter32
_PrInFloodPktsCnt_Object = MibTableColumn
prInFloodPktsCnt = _PrInFloodPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 803),
    _PrInFloodPktsCnt_Type()
)
prInFloodPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInFloodPktsCnt.setStatus("current")
_PrOutFloodPktsCnt_Type = Counter32
_PrOutFloodPktsCnt_Object = MibTableColumn
prOutFloodPktsCnt = _PrOutFloodPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 804),
    _PrOutFloodPktsCnt_Type()
)
prOutFloodPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutFloodPktsCnt.setStatus("current")
_PrInBlockedProtocolPktsCnt_Type = Counter32
_PrInBlockedProtocolPktsCnt_Object = MibTableColumn
prInBlockedProtocolPktsCnt = _PrInBlockedProtocolPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 805),
    _PrInBlockedProtocolPktsCnt_Type()
)
prInBlockedProtocolPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBlockedProtocolPktsCnt.setStatus("current")
_PrOutBlockedProtocolPktsCnt_Type = Counter32
_PrOutBlockedProtocolPktsCnt_Object = MibTableColumn
prOutBlockedProtocolPktsCnt = _PrOutBlockedProtocolPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 806),
    _PrOutBlockedProtocolPktsCnt_Type()
)
prOutBlockedProtocolPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBlockedProtocolPktsCnt.setStatus("current")
_PrInBlockedStatePktsCnt_Type = Counter32
_PrInBlockedStatePktsCnt_Object = MibTableColumn
prInBlockedStatePktsCnt = _PrInBlockedStatePktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 807),
    _PrInBlockedStatePktsCnt_Type()
)
prInBlockedStatePktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBlockedStatePktsCnt.setStatus("current")
_PrOutBlockedStatePktsCnt_Type = Counter32
_PrOutBlockedStatePktsCnt_Object = MibTableColumn
prOutBlockedStatePktsCnt = _PrOutBlockedStatePktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 808),
    _PrOutBlockedStatePktsCnt_Type()
)
prOutBlockedStatePktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBlockedStatePktsCnt.setStatus("current")
_PrInIpAttackPktsCnt_Type = Counter32
_PrInIpAttackPktsCnt_Object = MibTableColumn
prInIpAttackPktsCnt = _PrInIpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 809),
    _PrInIpAttackPktsCnt_Type()
)
prInIpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInIpAttackPktsCnt.setStatus("current")
_PrOutIpAttackPktsCnt_Type = Counter32
_PrOutIpAttackPktsCnt_Object = MibTableColumn
prOutIpAttackPktsCnt = _PrOutIpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 810),
    _PrOutIpAttackPktsCnt_Type()
)
prOutIpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutIpAttackPktsCnt.setStatus("current")
_PrInTcpAttackPktsCnt_Type = Counter32
_PrInTcpAttackPktsCnt_Object = MibTableColumn
prInTcpAttackPktsCnt = _PrInTcpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 811),
    _PrInTcpAttackPktsCnt_Type()
)
prInTcpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInTcpAttackPktsCnt.setStatus("current")
_PrOutTcpAttackPktsCnt_Type = Counter32
_PrOutTcpAttackPktsCnt_Object = MibTableColumn
prOutTcpAttackPktsCnt = _PrOutTcpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 812),
    _PrOutTcpAttackPktsCnt_Type()
)
prOutTcpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutTcpAttackPktsCnt.setStatus("current")
_PrInUdpAttackPktsCnt_Type = Counter32
_PrInUdpAttackPktsCnt_Object = MibTableColumn
prInUdpAttackPktsCnt = _PrInUdpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 813),
    _PrInUdpAttackPktsCnt_Type()
)
prInUdpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInUdpAttackPktsCnt.setStatus("current")
_PrOutUdpAttackPktsCnt_Type = Counter32
_PrOutUdpAttackPktsCnt_Object = MibTableColumn
prOutUdpAttackPktsCnt = _PrOutUdpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 814),
    _PrOutUdpAttackPktsCnt_Type()
)
prOutUdpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutUdpAttackPktsCnt.setStatus("current")
_PrInIcmpAttackPktsCnt_Type = Counter32
_PrInIcmpAttackPktsCnt_Object = MibTableColumn
prInIcmpAttackPktsCnt = _PrInIcmpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 815),
    _PrInIcmpAttackPktsCnt_Type()
)
prInIcmpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInIcmpAttackPktsCnt.setStatus("current")
_PrOutIcmpAttackPktsCnt_Type = Counter32
_PrOutIcmpAttackPktsCnt_Object = MibTableColumn
prOutIcmpAttackPktsCnt = _PrOutIcmpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 816),
    _PrOutIcmpAttackPktsCnt_Type()
)
prOutIcmpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutIcmpAttackPktsCnt.setStatus("current")
_PrInOtherIpAttackPktsCnt_Type = Counter32
_PrInOtherIpAttackPktsCnt_Object = MibTableColumn
prInOtherIpAttackPktsCnt = _PrInOtherIpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 817),
    _PrInOtherIpAttackPktsCnt_Type()
)
prInOtherIpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInOtherIpAttackPktsCnt.setStatus("current")
_PrOutOtherIpAttackPktsCnt_Type = Counter32
_PrOutOtherIpAttackPktsCnt_Object = MibTableColumn
prOutOtherIpAttackPktsCnt = _PrOutOtherIpAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 818),
    _PrOutOtherIpAttackPktsCnt_Type()
)
prOutOtherIpAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutOtherIpAttackPktsCnt.setStatus("current")
_PrInFragmentAttackPktsCnt_Type = Counter32
_PrInFragmentAttackPktsCnt_Object = MibTableColumn
prInFragmentAttackPktsCnt = _PrInFragmentAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 819),
    _PrInFragmentAttackPktsCnt_Type()
)
prInFragmentAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInFragmentAttackPktsCnt.setStatus("current")
_PrOutFragmentAttackPktsCnt_Type = Counter32
_PrOutFragmentAttackPktsCnt_Object = MibTableColumn
prOutFragmentAttackPktsCnt = _PrOutFragmentAttackPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 820),
    _PrOutFragmentAttackPktsCnt_Type()
)
prOutFragmentAttackPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutFragmentAttackPktsCnt.setStatus("current")
_PrInBadIpPktsCnt_Type = Counter32
_PrInBadIpPktsCnt_Object = MibTableColumn
prInBadIpPktsCnt = _PrInBadIpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 821),
    _PrInBadIpPktsCnt_Type()
)
prInBadIpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBadIpPktsCnt.setStatus("current")
_PrOutBadIpPktsCnt_Type = Counter32
_PrOutBadIpPktsCnt_Object = MibTableColumn
prOutBadIpPktsCnt = _PrOutBadIpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 822),
    _PrOutBadIpPktsCnt_Type()
)
prOutBadIpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBadIpPktsCnt.setStatus("current")
_PrInBadTcpPktsCnt_Type = Counter32
_PrInBadTcpPktsCnt_Object = MibTableColumn
prInBadTcpPktsCnt = _PrInBadTcpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 823),
    _PrInBadTcpPktsCnt_Type()
)
prInBadTcpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBadTcpPktsCnt.setStatus("current")
_PrOutBadTcpPktsCnt_Type = Counter32
_PrOutBadTcpPktsCnt_Object = MibTableColumn
prOutBadTcpPktsCnt = _PrOutBadTcpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 824),
    _PrOutBadTcpPktsCnt_Type()
)
prOutBadTcpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBadTcpPktsCnt.setStatus("current")
_PrInBadUdpPktsCnt_Type = Counter32
_PrInBadUdpPktsCnt_Object = MibTableColumn
prInBadUdpPktsCnt = _PrInBadUdpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 825),
    _PrInBadUdpPktsCnt_Type()
)
prInBadUdpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBadUdpPktsCnt.setStatus("current")
_PrOutBadUdpPktsCnt_Type = Counter32
_PrOutBadUdpPktsCnt_Object = MibTableColumn
prOutBadUdpPktsCnt = _PrOutBadUdpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 826),
    _PrOutBadUdpPktsCnt_Type()
)
prOutBadUdpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBadUdpPktsCnt.setStatus("current")
_PrInBadIcmpPktsCnt_Type = Counter32
_PrInBadIcmpPktsCnt_Object = MibTableColumn
prInBadIcmpPktsCnt = _PrInBadIcmpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 827),
    _PrInBadIcmpPktsCnt_Type()
)
prInBadIcmpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBadIcmpPktsCnt.setStatus("current")
_PrOutBadIcmpPktsCnt_Type = Counter32
_PrOutBadIcmpPktsCnt_Object = MibTableColumn
prOutBadIcmpPktsCnt = _PrOutBadIcmpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 828),
    _PrOutBadIcmpPktsCnt_Type()
)
prOutBadIcmpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBadIcmpPktsCnt.setStatus("current")
_PrInBadOtherIpPktsCnt_Type = Counter32
_PrInBadOtherIpPktsCnt_Object = MibTableColumn
prInBadOtherIpPktsCnt = _PrInBadOtherIpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 829),
    _PrInBadOtherIpPktsCnt_Type()
)
prInBadOtherIpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBadOtherIpPktsCnt.setStatus("current")
_PrOutBadOtherIpPktsCnt_Type = Counter32
_PrOutBadOtherIpPktsCnt_Object = MibTableColumn
prOutBadOtherIpPktsCnt = _PrOutBadOtherIpPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 830),
    _PrOutBadOtherIpPktsCnt_Type()
)
prOutBadOtherIpPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBadOtherIpPktsCnt.setStatus("current")
_PrInTotalBpsAvg_Type = Gauge32
_PrInTotalBpsAvg_Object = MibTableColumn
prInTotalBpsAvg = _PrInTotalBpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 901),
    _PrInTotalBpsAvg_Type()
)
prInTotalBpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInTotalBpsAvg.setStatus("current")
_PrOutTotalBpsAvg_Type = Gauge32
_PrOutTotalBpsAvg_Object = MibTableColumn
prOutTotalBpsAvg = _PrOutTotalBpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 902),
    _PrOutTotalBpsAvg_Type()
)
prOutTotalBpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutTotalBpsAvg.setStatus("current")
_PrInTotalPpsAvg_Type = Gauge32
_PrInTotalPpsAvg_Object = MibTableColumn
prInTotalPpsAvg = _PrInTotalPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 903),
    _PrInTotalPpsAvg_Type()
)
prInTotalPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInTotalPpsAvg.setStatus("current")
_PrOutTotalPpsAvg_Type = Gauge32
_PrOutTotalPpsAvg_Object = MibTableColumn
prOutTotalPpsAvg = _PrOutTotalPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 904),
    _PrOutTotalPpsAvg_Type()
)
prOutTotalPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutTotalPpsAvg.setStatus("current")
_PrInSmallPpsAvg_Type = Gauge32
_PrInSmallPpsAvg_Object = MibTableColumn
prInSmallPpsAvg = _PrInSmallPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 905),
    _PrInSmallPpsAvg_Type()
)
prInSmallPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInSmallPpsAvg.setStatus("current")
_PrOutSmallPpsAvg_Type = Gauge32
_PrOutSmallPpsAvg_Object = MibTableColumn
prOutSmallPpsAvg = _PrOutSmallPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 906),
    _PrOutSmallPpsAvg_Type()
)
prOutSmallPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutSmallPpsAvg.setStatus("current")
_PrInMediumPpsAvg_Type = Gauge32
_PrInMediumPpsAvg_Object = MibTableColumn
prInMediumPpsAvg = _PrInMediumPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 907),
    _PrInMediumPpsAvg_Type()
)
prInMediumPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInMediumPpsAvg.setStatus("current")
_PrOutMediumPpsAvg_Type = Gauge32
_PrOutMediumPpsAvg_Object = MibTableColumn
prOutMediumPpsAvg = _PrOutMediumPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 908),
    _PrOutMediumPpsAvg_Type()
)
prOutMediumPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutMediumPpsAvg.setStatus("current")
_PrInLargePpsAvg_Type = Gauge32
_PrInLargePpsAvg_Object = MibTableColumn
prInLargePpsAvg = _PrInLargePpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 909),
    _PrInLargePpsAvg_Type()
)
prInLargePpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInLargePpsAvg.setStatus("current")
_PrOutLargePpsAvg_Type = Gauge32
_PrOutLargePpsAvg_Object = MibTableColumn
prOutLargePpsAvg = _PrOutLargePpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 910),
    _PrOutLargePpsAvg_Type()
)
prOutLargePpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutLargePpsAvg.setStatus("current")
_PrInDroppedBpsAvg_Type = Gauge32
_PrInDroppedBpsAvg_Object = MibTableColumn
prInDroppedBpsAvg = _PrInDroppedBpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 911),
    _PrInDroppedBpsAvg_Type()
)
prInDroppedBpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInDroppedBpsAvg.setStatus("current")
_PrOutDroppedBpsAvg_Type = Gauge32
_PrOutDroppedBpsAvg_Object = MibTableColumn
prOutDroppedBpsAvg = _PrOutDroppedBpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 912),
    _PrOutDroppedBpsAvg_Type()
)
prOutDroppedBpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutDroppedBpsAvg.setStatus("current")
_PrInDroppedPpsAvg_Type = Gauge32
_PrInDroppedPpsAvg_Object = MibTableColumn
prInDroppedPpsAvg = _PrInDroppedPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 913),
    _PrInDroppedPpsAvg_Type()
)
prInDroppedPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInDroppedPpsAvg.setStatus("current")
_PrOutDroppedPpsAvg_Type = Gauge32
_PrOutDroppedPpsAvg_Object = MibTableColumn
prOutDroppedPpsAvg = _PrOutDroppedPpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 914),
    _PrOutDroppedPpsAvg_Type()
)
prOutDroppedPpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutDroppedPpsAvg.setStatus("current")
_PrInCharmDroppedBpsAvg_Type = Gauge32
_PrInCharmDroppedBpsAvg_Object = MibTableColumn
prInCharmDroppedBpsAvg = _PrInCharmDroppedBpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 915),
    _PrInCharmDroppedBpsAvg_Type()
)
prInCharmDroppedBpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInCharmDroppedBpsAvg.setStatus("current")
_PrOutCharmDroppedBpsAvg_Type = Gauge32
_PrOutCharmDroppedBpsAvg_Object = MibTableColumn
prOutCharmDroppedBpsAvg = _PrOutCharmDroppedBpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 916),
    _PrOutCharmDroppedBpsAvg_Type()
)
prOutCharmDroppedBpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutCharmDroppedBpsAvg.setStatus("current")
_PrInFilteredBwthPercentAvg_Type = Gauge32
_PrInFilteredBwthPercentAvg_Object = MibTableColumn
prInFilteredBwthPercentAvg = _PrInFilteredBwthPercentAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 917),
    _PrInFilteredBwthPercentAvg_Type()
)
prInFilteredBwthPercentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInFilteredBwthPercentAvg.setStatus("current")
_PrOutFilteredBwthPercentAvg_Type = Gauge32
_PrOutFilteredBwthPercentAvg_Object = MibTableColumn
prOutFilteredBwthPercentAvg = _PrOutFilteredBwthPercentAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 918),
    _PrOutFilteredBwthPercentAvg_Type()
)
prOutFilteredBwthPercentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutFilteredBwthPercentAvg.setStatus("current")
_PrInSynbacklogtallyAvg_Type = Gauge32
_PrInSynbacklogtallyAvg_Object = MibTableColumn
prInSynbacklogtallyAvg = _PrInSynbacklogtallyAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 919),
    _PrInSynbacklogtallyAvg_Type()
)
prInSynbacklogtallyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInSynbacklogtallyAvg.setStatus("current")
_PrOutSynbacklogtallyAvg_Type = Gauge32
_PrOutSynbacklogtallyAvg_Object = MibTableColumn
prOutSynbacklogtallyAvg = _PrOutSynbacklogtallyAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 920),
    _PrOutSynbacklogtallyAvg_Type()
)
prOutSynbacklogtallyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutSynbacklogtallyAvg.setStatus("current")
_PrInConnectionAvg_Type = Gauge32
_PrInConnectionAvg_Object = MibTableColumn
prInConnectionAvg = _PrInConnectionAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 921),
    _PrInConnectionAvg_Type()
)
prInConnectionAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInConnectionAvg.setStatus("current")
_PrOutConnectionAvg_Type = Gauge32
_PrOutConnectionAvg_Object = MibTableColumn
prOutConnectionAvg = _PrOutConnectionAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 922),
    _PrOutConnectionAvg_Type()
)
prOutConnectionAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutConnectionAvg.setStatus("current")
_PrInConnreqAvg_Type = Gauge32
_PrInConnreqAvg_Object = MibTableColumn
prInConnreqAvg = _PrInConnreqAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 923),
    _PrInConnreqAvg_Type()
)
prInConnreqAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInConnreqAvg.setStatus("current")
_PrOutConnreqAvg_Type = Gauge32
_PrOutConnreqAvg_Object = MibTableColumn
prOutConnreqAvg = _PrOutConnreqAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 924),
    _PrOutConnreqAvg_Type()
)
prOutConnreqAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutConnreqAvg.setStatus("current")
_PrInActiveHttpGetsAvg_Type = Gauge32
_PrInActiveHttpGetsAvg_Object = MibTableColumn
prInActiveHttpGetsAvg = _PrInActiveHttpGetsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 925),
    _PrInActiveHttpGetsAvg_Type()
)
prInActiveHttpGetsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInActiveHttpGetsAvg.setStatus("current")
_PrOutActiveHttpGetsAvg_Type = Gauge32
_PrOutActiveHttpGetsAvg_Object = MibTableColumn
prOutActiveHttpGetsAvg = _PrOutActiveHttpGetsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 926),
    _PrOutActiveHttpGetsAvg_Type()
)
prOutActiveHttpGetsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutActiveHttpGetsAvg.setStatus("current")
_PrInProtectBwthPktsAvg_Type = Gauge32
_PrInProtectBwthPktsAvg_Object = MibTableColumn
prInProtectBwthPktsAvg = _PrInProtectBwthPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 927),
    _PrInProtectBwthPktsAvg_Type()
)
prInProtectBwthPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInProtectBwthPktsAvg.setStatus("current")
_PrOutProtectBwthPktsAvg_Type = Gauge32
_PrOutProtectBwthPktsAvg_Object = MibTableColumn
prOutProtectBwthPktsAvg = _PrOutProtectBwthPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 928),
    _PrOutProtectBwthPktsAvg_Type()
)
prOutProtectBwthPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutProtectBwthPktsAvg.setStatus("current")
_PrInFloodPktsAvg_Type = Gauge32
_PrInFloodPktsAvg_Object = MibTableColumn
prInFloodPktsAvg = _PrInFloodPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 929),
    _PrInFloodPktsAvg_Type()
)
prInFloodPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInFloodPktsAvg.setStatus("current")
_PrOutFloodPktsAvg_Type = Gauge32
_PrOutFloodPktsAvg_Object = MibTableColumn
prOutFloodPktsAvg = _PrOutFloodPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 930),
    _PrOutFloodPktsAvg_Type()
)
prOutFloodPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutFloodPktsAvg.setStatus("current")
_PrInBlockedProtocolPktsAvg_Type = Gauge32
_PrInBlockedProtocolPktsAvg_Object = MibTableColumn
prInBlockedProtocolPktsAvg = _PrInBlockedProtocolPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 931),
    _PrInBlockedProtocolPktsAvg_Type()
)
prInBlockedProtocolPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBlockedProtocolPktsAvg.setStatus("current")
_PrOutBlockedProtocolPktsAvg_Type = Gauge32
_PrOutBlockedProtocolPktsAvg_Object = MibTableColumn
prOutBlockedProtocolPktsAvg = _PrOutBlockedProtocolPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 932),
    _PrOutBlockedProtocolPktsAvg_Type()
)
prOutBlockedProtocolPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBlockedProtocolPktsAvg.setStatus("current")
_PrInBlockedStatePktsAvg_Type = Gauge32
_PrInBlockedStatePktsAvg_Object = MibTableColumn
prInBlockedStatePktsAvg = _PrInBlockedStatePktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 933),
    _PrInBlockedStatePktsAvg_Type()
)
prInBlockedStatePktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBlockedStatePktsAvg.setStatus("current")
_PrOutBlockedStatePktsAvg_Type = Gauge32
_PrOutBlockedStatePktsAvg_Object = MibTableColumn
prOutBlockedStatePktsAvg = _PrOutBlockedStatePktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 934),
    _PrOutBlockedStatePktsAvg_Type()
)
prOutBlockedStatePktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBlockedStatePktsAvg.setStatus("current")
_PrInIpAttackPktsAvg_Type = Gauge32
_PrInIpAttackPktsAvg_Object = MibTableColumn
prInIpAttackPktsAvg = _PrInIpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 935),
    _PrInIpAttackPktsAvg_Type()
)
prInIpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInIpAttackPktsAvg.setStatus("current")
_PrOutIpAttackPktsAvg_Type = Gauge32
_PrOutIpAttackPktsAvg_Object = MibTableColumn
prOutIpAttackPktsAvg = _PrOutIpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 936),
    _PrOutIpAttackPktsAvg_Type()
)
prOutIpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutIpAttackPktsAvg.setStatus("current")
_PrInTcpAttackPktsAvg_Type = Gauge32
_PrInTcpAttackPktsAvg_Object = MibTableColumn
prInTcpAttackPktsAvg = _PrInTcpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 937),
    _PrInTcpAttackPktsAvg_Type()
)
prInTcpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInTcpAttackPktsAvg.setStatus("current")
_PrOutTcpAttackPktsAvg_Type = Gauge32
_PrOutTcpAttackPktsAvg_Object = MibTableColumn
prOutTcpAttackPktsAvg = _PrOutTcpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 938),
    _PrOutTcpAttackPktsAvg_Type()
)
prOutTcpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutTcpAttackPktsAvg.setStatus("current")
_PrInUdpAttackPktsAvg_Type = Gauge32
_PrInUdpAttackPktsAvg_Object = MibTableColumn
prInUdpAttackPktsAvg = _PrInUdpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 939),
    _PrInUdpAttackPktsAvg_Type()
)
prInUdpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInUdpAttackPktsAvg.setStatus("current")
_PrOutUdpAttackPktsAvg_Type = Gauge32
_PrOutUdpAttackPktsAvg_Object = MibTableColumn
prOutUdpAttackPktsAvg = _PrOutUdpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 940),
    _PrOutUdpAttackPktsAvg_Type()
)
prOutUdpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutUdpAttackPktsAvg.setStatus("current")
_PrInIcmpAttackPktsAvg_Type = Gauge32
_PrInIcmpAttackPktsAvg_Object = MibTableColumn
prInIcmpAttackPktsAvg = _PrInIcmpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 941),
    _PrInIcmpAttackPktsAvg_Type()
)
prInIcmpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInIcmpAttackPktsAvg.setStatus("current")
_PrOutIcmpAttackPktsAvg_Type = Gauge32
_PrOutIcmpAttackPktsAvg_Object = MibTableColumn
prOutIcmpAttackPktsAvg = _PrOutIcmpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 942),
    _PrOutIcmpAttackPktsAvg_Type()
)
prOutIcmpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutIcmpAttackPktsAvg.setStatus("current")
_PrInOtherIpAttackPktsAvg_Type = Gauge32
_PrInOtherIpAttackPktsAvg_Object = MibTableColumn
prInOtherIpAttackPktsAvg = _PrInOtherIpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 943),
    _PrInOtherIpAttackPktsAvg_Type()
)
prInOtherIpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInOtherIpAttackPktsAvg.setStatus("current")
_PrOutOtherIpAttackPktsAvg_Type = Gauge32
_PrOutOtherIpAttackPktsAvg_Object = MibTableColumn
prOutOtherIpAttackPktsAvg = _PrOutOtherIpAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 944),
    _PrOutOtherIpAttackPktsAvg_Type()
)
prOutOtherIpAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutOtherIpAttackPktsAvg.setStatus("current")
_PrInFragmentAttackPktsAvg_Type = Gauge32
_PrInFragmentAttackPktsAvg_Object = MibTableColumn
prInFragmentAttackPktsAvg = _PrInFragmentAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 945),
    _PrInFragmentAttackPktsAvg_Type()
)
prInFragmentAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInFragmentAttackPktsAvg.setStatus("current")
_PrOutFragmentAttackPktsAvg_Type = Gauge32
_PrOutFragmentAttackPktsAvg_Object = MibTableColumn
prOutFragmentAttackPktsAvg = _PrOutFragmentAttackPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 946),
    _PrOutFragmentAttackPktsAvg_Type()
)
prOutFragmentAttackPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutFragmentAttackPktsAvg.setStatus("current")
_PrInBadipPktsAvg_Type = Gauge32
_PrInBadipPktsAvg_Object = MibTableColumn
prInBadipPktsAvg = _PrInBadipPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 947),
    _PrInBadipPktsAvg_Type()
)
prInBadipPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBadipPktsAvg.setStatus("current")
_PrOutBadipPktsAvg_Type = Gauge32
_PrOutBadipPktsAvg_Object = MibTableColumn
prOutBadipPktsAvg = _PrOutBadipPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 948),
    _PrOutBadipPktsAvg_Type()
)
prOutBadipPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBadipPktsAvg.setStatus("current")
_PrInBadTcpPktsAvg_Type = Gauge32
_PrInBadTcpPktsAvg_Object = MibTableColumn
prInBadTcpPktsAvg = _PrInBadTcpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 949),
    _PrInBadTcpPktsAvg_Type()
)
prInBadTcpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBadTcpPktsAvg.setStatus("current")
_PrOutBadTcpPktsAvg_Type = Gauge32
_PrOutBadTcpPktsAvg_Object = MibTableColumn
prOutBadTcpPktsAvg = _PrOutBadTcpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 950),
    _PrOutBadTcpPktsAvg_Type()
)
prOutBadTcpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBadTcpPktsAvg.setStatus("current")
_PrInBadUdpPktsAvg_Type = Gauge32
_PrInBadUdpPktsAvg_Object = MibTableColumn
prInBadUdpPktsAvg = _PrInBadUdpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 951),
    _PrInBadUdpPktsAvg_Type()
)
prInBadUdpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBadUdpPktsAvg.setStatus("current")
_PrOutBadUdpPktsAvg_Type = Gauge32
_PrOutBadUdpPktsAvg_Object = MibTableColumn
prOutBadUdpPktsAvg = _PrOutBadUdpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 952),
    _PrOutBadUdpPktsAvg_Type()
)
prOutBadUdpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBadUdpPktsAvg.setStatus("current")
_PrInBadIcmpPktsAvg_Type = Gauge32
_PrInBadIcmpPktsAvg_Object = MibTableColumn
prInBadIcmpPktsAvg = _PrInBadIcmpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 953),
    _PrInBadIcmpPktsAvg_Type()
)
prInBadIcmpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBadIcmpPktsAvg.setStatus("current")
_PrOutBadIcmpPktsAvg_Type = Gauge32
_PrOutBadIcmpPktsAvg_Object = MibTableColumn
prOutBadIcmpPktsAvg = _PrOutBadIcmpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 954),
    _PrOutBadIcmpPktsAvg_Type()
)
prOutBadIcmpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBadIcmpPktsAvg.setStatus("current")
_PrInBadOtherIpPktsAvg_Type = Gauge32
_PrInBadOtherIpPktsAvg_Object = MibTableColumn
prInBadOtherIpPktsAvg = _PrInBadOtherIpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 955),
    _PrInBadOtherIpPktsAvg_Type()
)
prInBadOtherIpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBadOtherIpPktsAvg.setStatus("current")
_PrOutBadOtherIpPktsAvg_Type = Gauge32
_PrOutBadOtherIpPktsAvg_Object = MibTableColumn
prOutBadOtherIpPktsAvg = _PrOutBadOtherIpPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 956),
    _PrOutBadOtherIpPktsAvg_Type()
)
prOutBadOtherIpPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBadOtherIpPktsAvg.setStatus("current")
_PrInOverloadedAvg_Type = Gauge32
_PrInOverloadedAvg_Object = MibTableColumn
prInOverloadedAvg = _PrInOverloadedAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 957),
    _PrInOverloadedAvg_Type()
)
prInOverloadedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInOverloadedAvg.setStatus("current")
_PrOutOverloadedAvg_Type = Gauge32
_PrOutOverloadedAvg_Object = MibTableColumn
prOutOverloadedAvg = _PrOutOverloadedAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 958),
    _PrOutOverloadedAvg_Type()
)
prOutOverloadedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutOverloadedAvg.setStatus("current")
_PrInLatencyAvg_Type = Gauge32
_PrInLatencyAvg_Object = MibTableColumn
prInLatencyAvg = _PrInLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 959),
    _PrInLatencyAvg_Type()
)
prInLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInLatencyAvg.setStatus("current")
_PrOutLatencyAvg_Type = Gauge32
_PrOutLatencyAvg_Object = MibTableColumn
prOutLatencyAvg = _PrOutLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 960),
    _PrOutLatencyAvg_Type()
)
prOutLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutLatencyAvg.setStatus("current")
_PrInSmallPpsMax_Type = Gauge32
_PrInSmallPpsMax_Object = MibTableColumn
prInSmallPpsMax = _PrInSmallPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1001),
    _PrInSmallPpsMax_Type()
)
prInSmallPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInSmallPpsMax.setStatus("current")
_PrOutSmallPpsMax_Type = Gauge32
_PrOutSmallPpsMax_Object = MibTableColumn
prOutSmallPpsMax = _PrOutSmallPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1002),
    _PrOutSmallPpsMax_Type()
)
prOutSmallPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutSmallPpsMax.setStatus("current")
_PrInMediumPpsMax_Type = Gauge32
_PrInMediumPpsMax_Object = MibTableColumn
prInMediumPpsMax = _PrInMediumPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1003),
    _PrInMediumPpsMax_Type()
)
prInMediumPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInMediumPpsMax.setStatus("current")
_PrOutMediumPpsMax_Type = Gauge32
_PrOutMediumPpsMax_Object = MibTableColumn
prOutMediumPpsMax = _PrOutMediumPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1004),
    _PrOutMediumPpsMax_Type()
)
prOutMediumPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutMediumPpsMax.setStatus("current")
_PrInLargePpsMax_Type = Gauge32
_PrInLargePpsMax_Object = MibTableColumn
prInLargePpsMax = _PrInLargePpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1005),
    _PrInLargePpsMax_Type()
)
prInLargePpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInLargePpsMax.setStatus("current")
_PrOutLargePpsMax_Type = Gauge32
_PrOutLargePpsMax_Object = MibTableColumn
prOutLargePpsMax = _PrOutLargePpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1006),
    _PrOutLargePpsMax_Type()
)
prOutLargePpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutLargePpsMax.setStatus("current")
_PrInFilteredBwthPercentMax_Type = Gauge32
_PrInFilteredBwthPercentMax_Object = MibTableColumn
prInFilteredBwthPercentMax = _PrInFilteredBwthPercentMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1007),
    _PrInFilteredBwthPercentMax_Type()
)
prInFilteredBwthPercentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInFilteredBwthPercentMax.setStatus("current")
_PrOutFilteredBwthPercentMax_Type = Gauge32
_PrOutFilteredBwthPercentMax_Object = MibTableColumn
prOutFilteredBwthPercentMax = _PrOutFilteredBwthPercentMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1008),
    _PrOutFilteredBwthPercentMax_Type()
)
prOutFilteredBwthPercentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutFilteredBwthPercentMax.setStatus("current")
_PrInSynbacklogtallyMax_Type = Gauge32
_PrInSynbacklogtallyMax_Object = MibTableColumn
prInSynbacklogtallyMax = _PrInSynbacklogtallyMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1009),
    _PrInSynbacklogtallyMax_Type()
)
prInSynbacklogtallyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInSynbacklogtallyMax.setStatus("current")
_PrOutSynbacklogtallyMax_Type = Gauge32
_PrOutSynbacklogtallyMax_Object = MibTableColumn
prOutSynbacklogtallyMax = _PrOutSynbacklogtallyMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1010),
    _PrOutSynbacklogtallyMax_Type()
)
prOutSynbacklogtallyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutSynbacklogtallyMax.setStatus("current")
_PrInConnectionMax_Type = Gauge32
_PrInConnectionMax_Object = MibTableColumn
prInConnectionMax = _PrInConnectionMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1011),
    _PrInConnectionMax_Type()
)
prInConnectionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInConnectionMax.setStatus("current")
_PrOutConnectionMax_Type = Gauge32
_PrOutConnectionMax_Object = MibTableColumn
prOutConnectionMax = _PrOutConnectionMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1012),
    _PrOutConnectionMax_Type()
)
prOutConnectionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutConnectionMax.setStatus("current")
_PrInConnreqMax_Type = Gauge32
_PrInConnreqMax_Object = MibTableColumn
prInConnreqMax = _PrInConnreqMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1013),
    _PrInConnreqMax_Type()
)
prInConnreqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInConnreqMax.setStatus("current")
_PrOutConnreqMax_Type = Gauge32
_PrOutConnreqMax_Object = MibTableColumn
prOutConnreqMax = _PrOutConnreqMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1014),
    _PrOutConnreqMax_Type()
)
prOutConnreqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutConnreqMax.setStatus("current")
_PrInActiveHttpGetsMax_Type = Gauge32
_PrInActiveHttpGetsMax_Object = MibTableColumn
prInActiveHttpGetsMax = _PrInActiveHttpGetsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1015),
    _PrInActiveHttpGetsMax_Type()
)
prInActiveHttpGetsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInActiveHttpGetsMax.setStatus("current")
_PrOutActiveHttpGetsMax_Type = Gauge32
_PrOutActiveHttpGetsMax_Object = MibTableColumn
prOutActiveHttpGetsMax = _PrOutActiveHttpGetsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1016),
    _PrOutActiveHttpGetsMax_Type()
)
prOutActiveHttpGetsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutActiveHttpGetsMax.setStatus("current")
_PrInProtectBwthPktsMax_Type = Gauge32
_PrInProtectBwthPktsMax_Object = MibTableColumn
prInProtectBwthPktsMax = _PrInProtectBwthPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1017),
    _PrInProtectBwthPktsMax_Type()
)
prInProtectBwthPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInProtectBwthPktsMax.setStatus("current")
_PrOutProtectBwthPktsMax_Type = Gauge32
_PrOutProtectBwthPktsMax_Object = MibTableColumn
prOutProtectBwthPktsMax = _PrOutProtectBwthPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1018),
    _PrOutProtectBwthPktsMax_Type()
)
prOutProtectBwthPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutProtectBwthPktsMax.setStatus("current")
_PrInFloodPktsMax_Type = Gauge32
_PrInFloodPktsMax_Object = MibTableColumn
prInFloodPktsMax = _PrInFloodPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1019),
    _PrInFloodPktsMax_Type()
)
prInFloodPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInFloodPktsMax.setStatus("current")
_PrOutFloodPktsMax_Type = Gauge32
_PrOutFloodPktsMax_Object = MibTableColumn
prOutFloodPktsMax = _PrOutFloodPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1020),
    _PrOutFloodPktsMax_Type()
)
prOutFloodPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutFloodPktsMax.setStatus("current")
_PrInBlockedProtocolPktsMax_Type = Gauge32
_PrInBlockedProtocolPktsMax_Object = MibTableColumn
prInBlockedProtocolPktsMax = _PrInBlockedProtocolPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1021),
    _PrInBlockedProtocolPktsMax_Type()
)
prInBlockedProtocolPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBlockedProtocolPktsMax.setStatus("current")
_PrOutBlockedProtocolPktsMax_Type = Gauge32
_PrOutBlockedProtocolPktsMax_Object = MibTableColumn
prOutBlockedProtocolPktsMax = _PrOutBlockedProtocolPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1022),
    _PrOutBlockedProtocolPktsMax_Type()
)
prOutBlockedProtocolPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBlockedProtocolPktsMax.setStatus("current")
_PrInBlockedStatePktsMax_Type = Gauge32
_PrInBlockedStatePktsMax_Object = MibTableColumn
prInBlockedStatePktsMax = _PrInBlockedStatePktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1023),
    _PrInBlockedStatePktsMax_Type()
)
prInBlockedStatePktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBlockedStatePktsMax.setStatus("current")
_PrOutBlockedStatePktsMax_Type = Gauge32
_PrOutBlockedStatePktsMax_Object = MibTableColumn
prOutBlockedStatePktsMax = _PrOutBlockedStatePktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1024),
    _PrOutBlockedStatePktsMax_Type()
)
prOutBlockedStatePktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBlockedStatePktsMax.setStatus("current")
_PrInIpAttackPktsMax_Type = Gauge32
_PrInIpAttackPktsMax_Object = MibTableColumn
prInIpAttackPktsMax = _PrInIpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1025),
    _PrInIpAttackPktsMax_Type()
)
prInIpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInIpAttackPktsMax.setStatus("current")
_PrOutIpAttackPktsMax_Type = Gauge32
_PrOutIpAttackPktsMax_Object = MibTableColumn
prOutIpAttackPktsMax = _PrOutIpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1026),
    _PrOutIpAttackPktsMax_Type()
)
prOutIpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutIpAttackPktsMax.setStatus("current")
_PrInTcpAttackPktsMax_Type = Gauge32
_PrInTcpAttackPktsMax_Object = MibTableColumn
prInTcpAttackPktsMax = _PrInTcpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1027),
    _PrInTcpAttackPktsMax_Type()
)
prInTcpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInTcpAttackPktsMax.setStatus("current")
_PrOutTcpAttackPktsMax_Type = Gauge32
_PrOutTcpAttackPktsMax_Object = MibTableColumn
prOutTcpAttackPktsMax = _PrOutTcpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1028),
    _PrOutTcpAttackPktsMax_Type()
)
prOutTcpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutTcpAttackPktsMax.setStatus("current")
_PrInUdpAttackPktsMax_Type = Gauge32
_PrInUdpAttackPktsMax_Object = MibTableColumn
prInUdpAttackPktsMax = _PrInUdpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1029),
    _PrInUdpAttackPktsMax_Type()
)
prInUdpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInUdpAttackPktsMax.setStatus("current")
_PrOutUdpAttackPktsMax_Type = Gauge32
_PrOutUdpAttackPktsMax_Object = MibTableColumn
prOutUdpAttackPktsMax = _PrOutUdpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1030),
    _PrOutUdpAttackPktsMax_Type()
)
prOutUdpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutUdpAttackPktsMax.setStatus("current")
_PrInIcmpAttackPktsMax_Type = Gauge32
_PrInIcmpAttackPktsMax_Object = MibTableColumn
prInIcmpAttackPktsMax = _PrInIcmpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1031),
    _PrInIcmpAttackPktsMax_Type()
)
prInIcmpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInIcmpAttackPktsMax.setStatus("current")
_PrOutIcmpAttackPktsMax_Type = Gauge32
_PrOutIcmpAttackPktsMax_Object = MibTableColumn
prOutIcmpAttackPktsMax = _PrOutIcmpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1032),
    _PrOutIcmpAttackPktsMax_Type()
)
prOutIcmpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutIcmpAttackPktsMax.setStatus("current")
_PrInOtherIpAttackPktsMax_Type = Gauge32
_PrInOtherIpAttackPktsMax_Object = MibTableColumn
prInOtherIpAttackPktsMax = _PrInOtherIpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1033),
    _PrInOtherIpAttackPktsMax_Type()
)
prInOtherIpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInOtherIpAttackPktsMax.setStatus("current")
_PrOutOtherIpAttackPktsMax_Type = Gauge32
_PrOutOtherIpAttackPktsMax_Object = MibTableColumn
prOutOtherIpAttackPktsMax = _PrOutOtherIpAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1034),
    _PrOutOtherIpAttackPktsMax_Type()
)
prOutOtherIpAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutOtherIpAttackPktsMax.setStatus("current")
_PrInFragmentAttackPktsMax_Type = Gauge32
_PrInFragmentAttackPktsMax_Object = MibTableColumn
prInFragmentAttackPktsMax = _PrInFragmentAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1035),
    _PrInFragmentAttackPktsMax_Type()
)
prInFragmentAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInFragmentAttackPktsMax.setStatus("current")
_PrOutFragmentAttackPktsMax_Type = Gauge32
_PrOutFragmentAttackPktsMax_Object = MibTableColumn
prOutFragmentAttackPktsMax = _PrOutFragmentAttackPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1036),
    _PrOutFragmentAttackPktsMax_Type()
)
prOutFragmentAttackPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutFragmentAttackPktsMax.setStatus("current")
_PrInBadipPktsMax_Type = Gauge32
_PrInBadipPktsMax_Object = MibTableColumn
prInBadipPktsMax = _PrInBadipPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1037),
    _PrInBadipPktsMax_Type()
)
prInBadipPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBadipPktsMax.setStatus("current")
_PrOutBadipPktsMax_Type = Gauge32
_PrOutBadipPktsMax_Object = MibTableColumn
prOutBadipPktsMax = _PrOutBadipPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1038),
    _PrOutBadipPktsMax_Type()
)
prOutBadipPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBadipPktsMax.setStatus("current")
_PrInBadTcpPktsMax_Type = Gauge32
_PrInBadTcpPktsMax_Object = MibTableColumn
prInBadTcpPktsMax = _PrInBadTcpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1039),
    _PrInBadTcpPktsMax_Type()
)
prInBadTcpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBadTcpPktsMax.setStatus("current")
_PrOutBadTcpPktsMax_Type = Gauge32
_PrOutBadTcpPktsMax_Object = MibTableColumn
prOutBadTcpPktsMax = _PrOutBadTcpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1040),
    _PrOutBadTcpPktsMax_Type()
)
prOutBadTcpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBadTcpPktsMax.setStatus("current")
_PrInBadUdpPktsMax_Type = Gauge32
_PrInBadUdpPktsMax_Object = MibTableColumn
prInBadUdpPktsMax = _PrInBadUdpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1041),
    _PrInBadUdpPktsMax_Type()
)
prInBadUdpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBadUdpPktsMax.setStatus("current")
_PrOutBadUdpPktsMax_Type = Gauge32
_PrOutBadUdpPktsMax_Object = MibTableColumn
prOutBadUdpPktsMax = _PrOutBadUdpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1042),
    _PrOutBadUdpPktsMax_Type()
)
prOutBadUdpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBadUdpPktsMax.setStatus("current")
_PrInBadIcmpPktsMax_Type = Gauge32
_PrInBadIcmpPktsMax_Object = MibTableColumn
prInBadIcmpPktsMax = _PrInBadIcmpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1043),
    _PrInBadIcmpPktsMax_Type()
)
prInBadIcmpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBadIcmpPktsMax.setStatus("current")
_PrOutBadIcmpPktsMax_Type = Gauge32
_PrOutBadIcmpPktsMax_Object = MibTableColumn
prOutBadIcmpPktsMax = _PrOutBadIcmpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1044),
    _PrOutBadIcmpPktsMax_Type()
)
prOutBadIcmpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBadIcmpPktsMax.setStatus("current")
_PrInBadOtherIpPktsMax_Type = Gauge32
_PrInBadOtherIpPktsMax_Object = MibTableColumn
prInBadOtherIpPktsMax = _PrInBadOtherIpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1045),
    _PrInBadOtherIpPktsMax_Type()
)
prInBadOtherIpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInBadOtherIpPktsMax.setStatus("current")
_PrOutBadOtherIpPktsMax_Type = Gauge32
_PrOutBadOtherIpPktsMax_Object = MibTableColumn
prOutBadOtherIpPktsMax = _PrOutBadOtherIpPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1046),
    _PrOutBadOtherIpPktsMax_Type()
)
prOutBadOtherIpPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutBadOtherIpPktsMax.setStatus("current")
_PrInOverloadedMax_Type = Gauge32
_PrInOverloadedMax_Object = MibTableColumn
prInOverloadedMax = _PrInOverloadedMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1047),
    _PrInOverloadedMax_Type()
)
prInOverloadedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInOverloadedMax.setStatus("current")
_PrOutOverloadedMax_Type = Gauge32
_PrOutOverloadedMax_Object = MibTableColumn
prOutOverloadedMax = _PrOutOverloadedMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1048),
    _PrOutOverloadedMax_Type()
)
prOutOverloadedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutOverloadedMax.setStatus("current")
_PrInLatencyMax_Type = Gauge32
_PrInLatencyMax_Object = MibTableColumn
prInLatencyMax = _PrInLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1049),
    _PrInLatencyMax_Type()
)
prInLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prInLatencyMax.setStatus("current")
_PrOutLatencyMax_Type = Gauge32
_PrOutLatencyMax_Object = MibTableColumn
prOutLatencyMax = _PrOutLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 3, 1, 1050),
    _PrOutLatencyMax_Type()
)
prOutLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prOutLatencyMax.setStatus("current")
_PrIncidentTable_Object = MibTable
prIncidentTable = _PrIncidentTable_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 5)
)
if mibBuilder.loadTexts:
    prIncidentTable.setStatus("current")
_PrIncidentEntry_Object = MibTableRow
prIncidentEntry = _PrIncidentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 5, 1)
)
prIncidentEntry.setIndexNames(
    (0, "DDOSSECURE4-MIB", "prIncidentYear"),
    (0, "DDOSSECURE4-MIB", "prIncidentMonth"),
    (0, "DDOSSECURE4-MIB", "prIncidentDay"),
    (0, "DDOSSECURE4-MIB", "prIncidentNumber"),
    (0, "DDOSSECURE4-MIB", "prIncidentInetAddressType"),
    (0, "DDOSSECURE4-MIB", "prIncidentInetAddress"),
)
if mibBuilder.loadTexts:
    prIncidentEntry.setStatus("current")
_PrIncidentYear_Type = LocalIndex
_PrIncidentYear_Object = MibTableColumn
prIncidentYear = _PrIncidentYear_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 5, 1, 1),
    _PrIncidentYear_Type()
)
prIncidentYear.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prIncidentYear.setStatus("current")
_PrIncidentMonth_Type = LocalIndex
_PrIncidentMonth_Object = MibTableColumn
prIncidentMonth = _PrIncidentMonth_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 5, 1, 2),
    _PrIncidentMonth_Type()
)
prIncidentMonth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prIncidentMonth.setStatus("current")
_PrIncidentDay_Type = LocalIndex
_PrIncidentDay_Object = MibTableColumn
prIncidentDay = _PrIncidentDay_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 5, 1, 3),
    _PrIncidentDay_Type()
)
prIncidentDay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prIncidentDay.setStatus("current")
_PrIncidentNumber_Type = LocalIndex
_PrIncidentNumber_Object = MibTableColumn
prIncidentNumber = _PrIncidentNumber_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 5, 1, 4),
    _PrIncidentNumber_Type()
)
prIncidentNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prIncidentNumber.setStatus("current")
_PrIncidentInetAddressType_Type = InetAddressType
_PrIncidentInetAddressType_Object = MibTableColumn
prIncidentInetAddressType = _PrIncidentInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 5, 1, 5),
    _PrIncidentInetAddressType_Type()
)
prIncidentInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prIncidentInetAddressType.setStatus("current")


class _PrIncidentInetAddress_Type(InetAddress):
    """Custom type prIncidentInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_PrIncidentInetAddress_Type.__name__ = "InetAddress"
_PrIncidentInetAddress_Object = MibTableColumn
prIncidentInetAddress = _PrIncidentInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 5, 1, 6),
    _PrIncidentInetAddress_Type()
)
prIncidentInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prIncidentInetAddress.setStatus("current")
_PrIncidentStart_Type = DateAndTime
_PrIncidentStart_Object = MibTableColumn
prIncidentStart = _PrIncidentStart_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 5, 1, 7),
    _PrIncidentStart_Type()
)
prIncidentStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prIncidentStart.setStatus("current")
_PrIncidentAddress_Type = DisplayString
_PrIncidentAddress_Object = MibTableColumn
prIncidentAddress = _PrIncidentAddress_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 5, 1, 8),
    _PrIncidentAddress_Type()
)
prIncidentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prIncidentAddress.setStatus("current")
_PrIncidentType_Type = DisplayString
_PrIncidentType_Object = MibTableColumn
prIncidentType = _PrIncidentType_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 5, 1, 9),
    _PrIncidentType_Type()
)
prIncidentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prIncidentType.setStatus("current")
_PrIncidentDirection_Type = Direction
_PrIncidentDirection_Object = MibTableColumn
prIncidentDirection = _PrIncidentDirection_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 5, 1, 10),
    _PrIncidentDirection_Type()
)
prIncidentDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prIncidentDirection.setStatus("current")
_PrIncidentPeakRate_Type = Gauge32
_PrIncidentPeakRate_Object = MibTableColumn
prIncidentPeakRate = _PrIncidentPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 5, 1, 11),
    _PrIncidentPeakRate_Type()
)
prIncidentPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prIncidentPeakRate.setStatus("current")
_PrIncidentDropped_Type = Gauge32
_PrIncidentDropped_Object = MibTableColumn
prIncidentDropped = _PrIncidentDropped_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 6, 5, 1, 12),
    _PrIncidentDropped_Type()
)
prIncidentDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prIncidentDropped.setStatus("current")
_JddsGatewayInternet_ObjectIdentity = ObjectIdentity
jddsGatewayInternet = _JddsGatewayInternet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7)
)
_GwInternetConfigTable_Object = MibTable
gwInternetConfigTable = _GwInternetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 1)
)
if mibBuilder.loadTexts:
    gwInternetConfigTable.setStatus("current")
_GwInternetConfigEntry_Object = MibTableRow
gwInternetConfigEntry = _GwInternetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 1, 1)
)
gwInternetConfigEntry.setIndexNames(
    (0, "DDOSSECURE4-MIB", "gwInternetConfigIndex"),
)
if mibBuilder.loadTexts:
    gwInternetConfigEntry.setStatus("current")
_GwInternetConfigIndex_Type = LocalIndex
_GwInternetConfigIndex_Object = MibTableColumn
gwInternetConfigIndex = _GwInternetConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 1, 1, 1),
    _GwInternetConfigIndex_Type()
)
gwInternetConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwInternetConfigIndex.setStatus("current")
_GwInternetConfigMacAddress_Type = DisplayString
_GwInternetConfigMacAddress_Object = MibTableColumn
gwInternetConfigMacAddress = _GwInternetConfigMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 1, 1, 2),
    _GwInternetConfigMacAddress_Type()
)
gwInternetConfigMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInternetConfigMacAddress.setStatus("current")
_GwInternetConfigToSpeedBps_Type = Gauge32
_GwInternetConfigToSpeedBps_Object = MibTableColumn
gwInternetConfigToSpeedBps = _GwInternetConfigToSpeedBps_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 1, 1, 3),
    _GwInternetConfigToSpeedBps_Type()
)
gwInternetConfigToSpeedBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInternetConfigToSpeedBps.setStatus("current")
_GwInternetConfigToRatePps_Type = Gauge32
_GwInternetConfigToRatePps_Object = MibTableColumn
gwInternetConfigToRatePps = _GwInternetConfigToRatePps_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 1, 1, 4),
    _GwInternetConfigToRatePps_Type()
)
gwInternetConfigToRatePps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInternetConfigToRatePps.setStatus("current")
_GwInternetStatsTable_Object = MibTable
gwInternetStatsTable = _GwInternetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 3)
)
if mibBuilder.loadTexts:
    gwInternetStatsTable.setStatus("current")
_GwInternetStatsEntry_Object = MibTableRow
gwInternetStatsEntry = _GwInternetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 3, 1)
)
gwInternetStatsEntry.setIndexNames(
    (0, "DDOSSECURE4-MIB", "gwInternetStatsIndex"),
)
if mibBuilder.loadTexts:
    gwInternetStatsEntry.setStatus("current")
_GwInternetStatsIndex_Type = LocalIndex
_GwInternetStatsIndex_Object = MibTableColumn
gwInternetStatsIndex = _GwInternetStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 3, 1, 1),
    _GwInternetStatsIndex_Type()
)
gwInternetStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwInternetStatsIndex.setStatus("current")
_GwInternetMacAddress_Type = DisplayString
_GwInternetMacAddress_Object = MibTableColumn
gwInternetMacAddress = _GwInternetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 3, 1, 2),
    _GwInternetMacAddress_Type()
)
gwInternetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInternetMacAddress.setStatus("current")
_GwInternetIpAddress_Type = DisplayString
_GwInternetIpAddress_Object = MibTableColumn
gwInternetIpAddress = _GwInternetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 3, 1, 3),
    _GwInternetIpAddress_Type()
)
gwInternetIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInternetIpAddress.setStatus("current")
_GwInternetInTotalBytesCnt_Type = Counter64
_GwInternetInTotalBytesCnt_Object = MibTableColumn
gwInternetInTotalBytesCnt = _GwInternetInTotalBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 3, 1, 101),
    _GwInternetInTotalBytesCnt_Type()
)
gwInternetInTotalBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInternetInTotalBytesCnt.setStatus("current")
_GwInternetOutTotalBytesCnt_Type = Counter64
_GwInternetOutTotalBytesCnt_Object = MibTableColumn
gwInternetOutTotalBytesCnt = _GwInternetOutTotalBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 3, 1, 102),
    _GwInternetOutTotalBytesCnt_Type()
)
gwInternetOutTotalBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInternetOutTotalBytesCnt.setStatus("current")
_GwInternetInDroppedBytesCnt_Type = Counter64
_GwInternetInDroppedBytesCnt_Object = MibTableColumn
gwInternetInDroppedBytesCnt = _GwInternetInDroppedBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 3, 1, 103),
    _GwInternetInDroppedBytesCnt_Type()
)
gwInternetInDroppedBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInternetInDroppedBytesCnt.setStatus("current")
_GwInternetOutDroppedBytesCnt_Type = Counter64
_GwInternetOutDroppedBytesCnt_Object = MibTableColumn
gwInternetOutDroppedBytesCnt = _GwInternetOutDroppedBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 3, 1, 104),
    _GwInternetOutDroppedBytesCnt_Type()
)
gwInternetOutDroppedBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInternetOutDroppedBytesCnt.setStatus("current")
_GwInternetInTotalPpsMax_Type = Gauge32
_GwInternetInTotalPpsMax_Object = MibTableColumn
gwInternetInTotalPpsMax = _GwInternetInTotalPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 3, 1, 201),
    _GwInternetInTotalPpsMax_Type()
)
gwInternetInTotalPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInternetInTotalPpsMax.setStatus("current")
_GwInternetOutTotalPpsMax_Type = Gauge32
_GwInternetOutTotalPpsMax_Object = MibTableColumn
gwInternetOutTotalPpsMax = _GwInternetOutTotalPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 3, 1, 202),
    _GwInternetOutTotalPpsMax_Type()
)
gwInternetOutTotalPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInternetOutTotalPpsMax.setStatus("current")
_GwInternetInDroppedPpsMax_Type = Gauge32
_GwInternetInDroppedPpsMax_Object = MibTableColumn
gwInternetInDroppedPpsMax = _GwInternetInDroppedPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 3, 1, 203),
    _GwInternetInDroppedPpsMax_Type()
)
gwInternetInDroppedPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInternetInDroppedPpsMax.setStatus("current")
_GwInternetOutDroppedPpsMax_Type = Gauge32
_GwInternetOutDroppedPpsMax_Object = MibTableColumn
gwInternetOutDroppedPpsMax = _GwInternetOutDroppedPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 3, 1, 204),
    _GwInternetOutDroppedPpsMax_Type()
)
gwInternetOutDroppedPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInternetOutDroppedPpsMax.setStatus("current")
_GwInternetInTotalBpsMax_Type = Gauge32
_GwInternetInTotalBpsMax_Object = MibTableColumn
gwInternetInTotalBpsMax = _GwInternetInTotalBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 3, 1, 301),
    _GwInternetInTotalBpsMax_Type()
)
gwInternetInTotalBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInternetInTotalBpsMax.setStatus("current")
_GwInternetOutTotalBpsMax_Type = Gauge32
_GwInternetOutTotalBpsMax_Object = MibTableColumn
gwInternetOutTotalBpsMax = _GwInternetOutTotalBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 3, 1, 302),
    _GwInternetOutTotalBpsMax_Type()
)
gwInternetOutTotalBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInternetOutTotalBpsMax.setStatus("current")
_GwInternetInDroppedBpsMax_Type = Gauge32
_GwInternetInDroppedBpsMax_Object = MibTableColumn
gwInternetInDroppedBpsMax = _GwInternetInDroppedBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 3, 1, 303),
    _GwInternetInDroppedBpsMax_Type()
)
gwInternetInDroppedBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInternetInDroppedBpsMax.setStatus("current")
_GwInternetOutDroppedBpsMax_Type = Gauge32
_GwInternetOutDroppedBpsMax_Object = MibTableColumn
gwInternetOutDroppedBpsMax = _GwInternetOutDroppedBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 7, 3, 1, 304),
    _GwInternetOutDroppedBpsMax_Type()
)
gwInternetOutDroppedBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInternetOutDroppedBpsMax.setStatus("current")
_JddsGatewayProtected_ObjectIdentity = ObjectIdentity
jddsGatewayProtected = _JddsGatewayProtected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8)
)
_GwProtectedConfigTable_Object = MibTable
gwProtectedConfigTable = _GwProtectedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 1)
)
if mibBuilder.loadTexts:
    gwProtectedConfigTable.setStatus("current")
_GwProtectedConfigEntry_Object = MibTableRow
gwProtectedConfigEntry = _GwProtectedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 1, 1)
)
gwProtectedConfigEntry.setIndexNames(
    (0, "DDOSSECURE4-MIB", "gwProtectedConfigIndex"),
)
if mibBuilder.loadTexts:
    gwProtectedConfigEntry.setStatus("current")
_GwProtectedConfigIndex_Type = LocalIndex
_GwProtectedConfigIndex_Object = MibTableColumn
gwProtectedConfigIndex = _GwProtectedConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 1, 1, 1),
    _GwProtectedConfigIndex_Type()
)
gwProtectedConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwProtectedConfigIndex.setStatus("current")
_GwProtectedConfigMacAddress_Type = DisplayString
_GwProtectedConfigMacAddress_Object = MibTableColumn
gwProtectedConfigMacAddress = _GwProtectedConfigMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 1, 1, 2),
    _GwProtectedConfigMacAddress_Type()
)
gwProtectedConfigMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwProtectedConfigMacAddress.setStatus("current")
_GwProtectedConfigToSpeedBps_Type = Gauge32
_GwProtectedConfigToSpeedBps_Object = MibTableColumn
gwProtectedConfigToSpeedBps = _GwProtectedConfigToSpeedBps_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 1, 1, 3),
    _GwProtectedConfigToSpeedBps_Type()
)
gwProtectedConfigToSpeedBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwProtectedConfigToSpeedBps.setStatus("current")
_GwProtectedConfigToRatePps_Type = Gauge32
_GwProtectedConfigToRatePps_Object = MibTableColumn
gwProtectedConfigToRatePps = _GwProtectedConfigToRatePps_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 1, 1, 4),
    _GwProtectedConfigToRatePps_Type()
)
gwProtectedConfigToRatePps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwProtectedConfigToRatePps.setStatus("current")
_GwProtectedStatsTable_Object = MibTable
gwProtectedStatsTable = _GwProtectedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 3)
)
if mibBuilder.loadTexts:
    gwProtectedStatsTable.setStatus("current")
_GwProtectedStatsEntry_Object = MibTableRow
gwProtectedStatsEntry = _GwProtectedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 3, 1)
)
gwProtectedStatsEntry.setIndexNames(
    (0, "DDOSSECURE4-MIB", "gwProtectedIndex"),
)
if mibBuilder.loadTexts:
    gwProtectedStatsEntry.setStatus("current")
_GwProtectedIndex_Type = LocalIndex
_GwProtectedIndex_Object = MibTableColumn
gwProtectedIndex = _GwProtectedIndex_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 3, 1, 1),
    _GwProtectedIndex_Type()
)
gwProtectedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwProtectedIndex.setStatus("current")
_GwProtectedMacAddress_Type = DisplayString
_GwProtectedMacAddress_Object = MibTableColumn
gwProtectedMacAddress = _GwProtectedMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 3, 1, 2),
    _GwProtectedMacAddress_Type()
)
gwProtectedMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwProtectedMacAddress.setStatus("current")
_GwProtectedIpAddress_Type = DisplayString
_GwProtectedIpAddress_Object = MibTableColumn
gwProtectedIpAddress = _GwProtectedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 3, 1, 3),
    _GwProtectedIpAddress_Type()
)
gwProtectedIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwProtectedIpAddress.setStatus("current")
_GwProtectedInTotalBytesCnt_Type = Counter64
_GwProtectedInTotalBytesCnt_Object = MibTableColumn
gwProtectedInTotalBytesCnt = _GwProtectedInTotalBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 3, 1, 101),
    _GwProtectedInTotalBytesCnt_Type()
)
gwProtectedInTotalBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwProtectedInTotalBytesCnt.setStatus("current")
_GwProtectedOutTotalBytesCnt_Type = Counter64
_GwProtectedOutTotalBytesCnt_Object = MibTableColumn
gwProtectedOutTotalBytesCnt = _GwProtectedOutTotalBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 3, 1, 102),
    _GwProtectedOutTotalBytesCnt_Type()
)
gwProtectedOutTotalBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwProtectedOutTotalBytesCnt.setStatus("current")
_GwProtectedInDroppedBytesCnt_Type = Counter64
_GwProtectedInDroppedBytesCnt_Object = MibTableColumn
gwProtectedInDroppedBytesCnt = _GwProtectedInDroppedBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 3, 1, 103),
    _GwProtectedInDroppedBytesCnt_Type()
)
gwProtectedInDroppedBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwProtectedInDroppedBytesCnt.setStatus("current")
_GwProtectedOutDroppedBytesCnt_Type = Counter64
_GwProtectedOutDroppedBytesCnt_Object = MibTableColumn
gwProtectedOutDroppedBytesCnt = _GwProtectedOutDroppedBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 3, 1, 104),
    _GwProtectedOutDroppedBytesCnt_Type()
)
gwProtectedOutDroppedBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwProtectedOutDroppedBytesCnt.setStatus("current")
_GwProtectedInTotalPpsMax_Type = Gauge32
_GwProtectedInTotalPpsMax_Object = MibTableColumn
gwProtectedInTotalPpsMax = _GwProtectedInTotalPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 3, 1, 201),
    _GwProtectedInTotalPpsMax_Type()
)
gwProtectedInTotalPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwProtectedInTotalPpsMax.setStatus("current")
_GwProtectedOutTotalPpsMax_Type = Gauge32
_GwProtectedOutTotalPpsMax_Object = MibTableColumn
gwProtectedOutTotalPpsMax = _GwProtectedOutTotalPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 3, 1, 202),
    _GwProtectedOutTotalPpsMax_Type()
)
gwProtectedOutTotalPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwProtectedOutTotalPpsMax.setStatus("current")
_GwProtectedInDroppedPpsMax_Type = Gauge32
_GwProtectedInDroppedPpsMax_Object = MibTableColumn
gwProtectedInDroppedPpsMax = _GwProtectedInDroppedPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 3, 1, 203),
    _GwProtectedInDroppedPpsMax_Type()
)
gwProtectedInDroppedPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwProtectedInDroppedPpsMax.setStatus("current")
_GwProtectedOutDroppedPpsMax_Type = Gauge32
_GwProtectedOutDroppedPpsMax_Object = MibTableColumn
gwProtectedOutDroppedPpsMax = _GwProtectedOutDroppedPpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 3, 1, 204),
    _GwProtectedOutDroppedPpsMax_Type()
)
gwProtectedOutDroppedPpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwProtectedOutDroppedPpsMax.setStatus("current")
_GwProtectedInTotalBpsMax_Type = Gauge32
_GwProtectedInTotalBpsMax_Object = MibTableColumn
gwProtectedInTotalBpsMax = _GwProtectedInTotalBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 3, 1, 301),
    _GwProtectedInTotalBpsMax_Type()
)
gwProtectedInTotalBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwProtectedInTotalBpsMax.setStatus("current")
_GwProtectedOutTotalBpsMax_Type = Gauge32
_GwProtectedOutTotalBpsMax_Object = MibTableColumn
gwProtectedOutTotalBpsMax = _GwProtectedOutTotalBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 3, 1, 302),
    _GwProtectedOutTotalBpsMax_Type()
)
gwProtectedOutTotalBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwProtectedOutTotalBpsMax.setStatus("current")
_GwProtectedInDroppedBpsMax_Type = Gauge32
_GwProtectedInDroppedBpsMax_Object = MibTableColumn
gwProtectedInDroppedBpsMax = _GwProtectedInDroppedBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 3, 1, 303),
    _GwProtectedInDroppedBpsMax_Type()
)
gwProtectedInDroppedBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwProtectedInDroppedBpsMax.setStatus("current")
_GwProtectedOutDroppedBpsMax_Type = Gauge32
_GwProtectedOutDroppedBpsMax_Object = MibTableColumn
gwProtectedOutDroppedBpsMax = _GwProtectedOutDroppedBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 8, 3, 1, 304),
    _GwProtectedOutDroppedBpsMax_Type()
)
gwProtectedOutDroppedBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwProtectedOutDroppedBpsMax.setStatus("current")
_Ddossecure4MIBConformance_ObjectIdentity = ObjectIdentity
ddossecure4MIBConformance = _Ddossecure4MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9)
)
_Ddossecure4MIBCompliances_ObjectIdentity = ObjectIdentity
ddossecure4MIBCompliances = _Ddossecure4MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 1)
)
_Ddossecure4MIBGroups_ObjectIdentity = ObjectIdentity
ddossecure4MIBGroups = _Ddossecure4MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 2)
)

# Managed Objects groups

apCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 2, 1)
)
apCfgGroup.setObjects(
      *(("DDOSSECURE4-MIB", "apMgmtIfIpAddress"),
        ("DDOSSECURE4-MIB", "apMgmtIfNetmask"),
        ("DDOSSECURE4-MIB", "apMgmtIfGwIpAddress"),
        ("DDOSSECURE4-MIB", "apMgmtIfLinkMode"),
        ("DDOSSECURE4-MIB", "apMgmtIfLinkFC"),
        ("DDOSSECURE4-MIB", "apMgmtIfName"),
        ("DDOSSECURE4-MIB", "apIntIfLinkMode"),
        ("DDOSSECURE4-MIB", "apIntIfLinkFC"),
        ("DDOSSECURE4-MIB", "apIntIfName"),
        ("DDOSSECURE4-MIB", "apProtIfLinkMode"),
        ("DDOSSECURE4-MIB", "apProtIfLinkFC"),
        ("DDOSSECURE4-MIB", "apProtIfName"),
        ("DDOSSECURE4-MIB", "apDataIfIpAddress"),
        ("DDOSSECURE4-MIB", "apDataIfNetmask"),
        ("DDOSSECURE4-MIB", "apDataIfLinkMode"),
        ("DDOSSECURE4-MIB", "apDataIfLinkFC"),
        ("DDOSSECURE4-MIB", "apDataIfName"),
        ("DDOSSECURE4-MIB", "apUserName"),
        ("DDOSSECURE4-MIB", "apUserPermissions"),
        ("DDOSSECURE4-MIB", "apSnmpRoCommunity"),
        ("DDOSSECURE4-MIB", "apSnmpTrapCommunity"),
        ("DDOSSECURE4-MIB", "apSnmpTrapIpAddressList"),
        ("DDOSSECURE4-MIB", "apSnmpAccessIpList"),
        ("DDOSSECURE4-MIB", "apHttpsAccessIpList"),
        ("DDOSSECURE4-MIB", "apSshAccessIpList"),
        ("DDOSSECURE4-MIB", "apSyslogServer"),
        ("DDOSSECURE4-MIB", "apSyslogFacility"),
        ("DDOSSECURE4-MIB", "apSyslogPriority"),
        ("DDOSSECURE4-MIB", "apWebtrendsServer"),
        ("DDOSSECURE4-MIB", "apWebtrendsFacility"),
        ("DDOSSECURE4-MIB", "apWebtrendsPriority"),
        ("DDOSSECURE4-MIB", "apMailServer"),
        ("DDOSSECURE4-MIB", "apMailFrom"),
        ("DDOSSECURE4-MIB", "apMailSubject"),
        ("DDOSSECURE4-MIB", "apMailToList"),
        ("DDOSSECURE4-MIB", "apMailDailyStats"),
        ("DDOSSECURE4-MIB", "apMailAlerts"),
        ("DDOSSECURE4-MIB", "apMailAlertInterval"),
        ("DDOSSECURE4-MIB", "apOperationMode"),
        ("DDOSSECURE4-MIB", "apNtpServerList"),
        ("DDOSSECURE4-MIB", "apTimeZone"),
        ("DDOSSECURE4-MIB", "apProtectedIpNetwork"),
        ("DDOSSECURE4-MIB", "apAutoblockEnable"),
        ("DDOSSECURE4-MIB", "apAutoblockRateT1"),
        ("DDOSSECURE4-MIB", "apProtectedIpAutodetect"),
        ("DDOSSECURE4-MIB", "apTrackIndeterminate"),
        ("DDOSSECURE4-MIB", "apAutoblockRateT2"))
)
if mibBuilder.loadTexts:
    apCfgGroup.setStatus("current")

gwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 2, 2)
)
gwGroup.setObjects(
      *(("DDOSSECURE4-MIB", "gwInternetMacAddress"),
        ("DDOSSECURE4-MIB", "gwInternetIpAddress"),
        ("DDOSSECURE4-MIB", "gwInternetInTotalBytesCnt"),
        ("DDOSSECURE4-MIB", "gwInternetOutTotalBytesCnt"),
        ("DDOSSECURE4-MIB", "gwInternetInDroppedBytesCnt"),
        ("DDOSSECURE4-MIB", "gwInternetOutDroppedBytesCnt"),
        ("DDOSSECURE4-MIB", "gwInternetInTotalPpsMax"),
        ("DDOSSECURE4-MIB", "gwInternetOutTotalPpsMax"),
        ("DDOSSECURE4-MIB", "gwInternetInDroppedPpsMax"),
        ("DDOSSECURE4-MIB", "gwInternetOutDroppedPpsMax"),
        ("DDOSSECURE4-MIB", "gwInternetInTotalBpsMax"),
        ("DDOSSECURE4-MIB", "gwInternetOutTotalBpsMax"),
        ("DDOSSECURE4-MIB", "gwInternetInDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "gwInternetOutDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "gwProtectedMacAddress"),
        ("DDOSSECURE4-MIB", "gwProtectedIpAddress"),
        ("DDOSSECURE4-MIB", "gwProtectedInTotalBytesCnt"),
        ("DDOSSECURE4-MIB", "gwProtectedOutTotalBytesCnt"),
        ("DDOSSECURE4-MIB", "gwProtectedInDroppedBytesCnt"),
        ("DDOSSECURE4-MIB", "gwProtectedOutDroppedBytesCnt"),
        ("DDOSSECURE4-MIB", "gwProtectedInTotalPpsMax"),
        ("DDOSSECURE4-MIB", "gwProtectedOutTotalPpsMax"),
        ("DDOSSECURE4-MIB", "gwProtectedInDroppedPpsMax"),
        ("DDOSSECURE4-MIB", "gwProtectedOutDroppedPpsMax"),
        ("DDOSSECURE4-MIB", "gwProtectedInTotalBpsMax"),
        ("DDOSSECURE4-MIB", "gwProtectedOutTotalBpsMax"),
        ("DDOSSECURE4-MIB", "gwProtectedInDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "gwProtectedOutDroppedBpsMax"))
)
if mibBuilder.loadTexts:
    gwGroup.setStatus("current")

apIncidentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 2, 3)
)
apIncidentGroup.setObjects(
      *(("DDOSSECURE4-MIB", "apBandwidthCreateThresh"),
        ("DDOSSECURE4-MIB", "apBandwidthCreateThreshRate"),
        ("DDOSSECURE4-MIB", "apFloodCreateThresh"),
        ("DDOSSECURE4-MIB", "apFloodCreateThreshRate"),
        ("DDOSSECURE4-MIB", "apBlockedProtoCreateThresh"),
        ("DDOSSECURE4-MIB", "apBlockedProtoCreateThreshRate"),
        ("DDOSSECURE4-MIB", "apBlockedStateCreateThresh"),
        ("DDOSSECURE4-MIB", "apBlockedStateCreateThreshRate"),
        ("DDOSSECURE4-MIB", "apIpAttackCreateThresh"),
        ("DDOSSECURE4-MIB", "apIpAttackCreateThreshRate"),
        ("DDOSSECURE4-MIB", "apTcpAttackCreateThresh"),
        ("DDOSSECURE4-MIB", "apTcpAttackCreateThreshRate"),
        ("DDOSSECURE4-MIB", "apUdpAttackCreateThresh"),
        ("DDOSSECURE4-MIB", "apUdpAttackCreateThreshRate"),
        ("DDOSSECURE4-MIB", "apIcmpAttackCreateThresh"),
        ("DDOSSECURE4-MIB", "apIcmpAttackCreateThreshRate"),
        ("DDOSSECURE4-MIB", "apOtherIpAttackCreateThresh"),
        ("DDOSSECURE4-MIB", "apOtherIpAttackCreateThreshRate"),
        ("DDOSSECURE4-MIB", "apFragAttackCreateThresh"),
        ("DDOSSECURE4-MIB", "apFragAttackCreateThreshRate"),
        ("DDOSSECURE4-MIB", "apBadIpCreateThresh"),
        ("DDOSSECURE4-MIB", "apBadIpCreateThreshRate"),
        ("DDOSSECURE4-MIB", "apBadTcpCreateThresh"),
        ("DDOSSECURE4-MIB", "apBadTcpCreateThreshRate"),
        ("DDOSSECURE4-MIB", "apBadUdpCreateThresh"),
        ("DDOSSECURE4-MIB", "apBadUdpCreateThreshRate"),
        ("DDOSSECURE4-MIB", "apBadIcmpCreateThresh"),
        ("DDOSSECURE4-MIB", "apBadIcmpCreateThreshRate"),
        ("DDOSSECURE4-MIB", "apBadOtherIpCreateThresh"),
        ("DDOSSECURE4-MIB", "apBadOtherIpCreateThreshRate"),
        ("DDOSSECURE4-MIB", "apOverloadedIpCreateThresh"),
        ("DDOSSECURE4-MIB", "apOverloadedIpCreateThreshRate"),
        ("DDOSSECURE4-MIB", "apBandwidthViewThresh"),
        ("DDOSSECURE4-MIB", "apBandwidthViewThreshRate"),
        ("DDOSSECURE4-MIB", "apFloodViewThresh"),
        ("DDOSSECURE4-MIB", "apFloodViewThreshRate"),
        ("DDOSSECURE4-MIB", "apBlockedProtoViewThresh"),
        ("DDOSSECURE4-MIB", "apBlockedProtoViewThreshRate"),
        ("DDOSSECURE4-MIB", "apBlockedStateViewThresh"),
        ("DDOSSECURE4-MIB", "apBlockedStateViewThreshRate"),
        ("DDOSSECURE4-MIB", "apIpAttackViewThresh"),
        ("DDOSSECURE4-MIB", "apIpAttackViewThreshRate"),
        ("DDOSSECURE4-MIB", "apTcpAttackViewThresh"),
        ("DDOSSECURE4-MIB", "apTcpAttackViewThreshRate"),
        ("DDOSSECURE4-MIB", "apUdpAttackViewThresh"),
        ("DDOSSECURE4-MIB", "apUdpAttackViewThreshRate"),
        ("DDOSSECURE4-MIB", "apIcmpAttackViewThresh"),
        ("DDOSSECURE4-MIB", "apIcmpAttackViewThreshRate"),
        ("DDOSSECURE4-MIB", "apOtherIpAttackViewThresh"),
        ("DDOSSECURE4-MIB", "apOtherIpAttackViewThreshRate"),
        ("DDOSSECURE4-MIB", "apFragAttackViewThresh"),
        ("DDOSSECURE4-MIB", "apFragAttackViewThreshRate"),
        ("DDOSSECURE4-MIB", "apBadIpViewThresh"),
        ("DDOSSECURE4-MIB", "apBadIpViewThreshRate"),
        ("DDOSSECURE4-MIB", "apBadTcpViewThresh"),
        ("DDOSSECURE4-MIB", "apBadTcpViewThreshRate"),
        ("DDOSSECURE4-MIB", "apBadUdpViewThresh"),
        ("DDOSSECURE4-MIB", "apBadUdpViewThreshRate"),
        ("DDOSSECURE4-MIB", "apBadIcmpViewThresh"),
        ("DDOSSECURE4-MIB", "apBadIcmpViewThreshRate"),
        ("DDOSSECURE4-MIB", "apBadOtherIpViewThresh"),
        ("DDOSSECURE4-MIB", "apBadOtherIpViewThreshRate"),
        ("DDOSSECURE4-MIB", "apOverloadedIpViewThresh"),
        ("DDOSSECURE4-MIB", "apOverloadedIpViewThreshRate"),
        ("DDOSSECURE4-MIB", "apBandwidthOffThresh"),
        ("DDOSSECURE4-MIB", "apBandwidthOffThreshRate"),
        ("DDOSSECURE4-MIB", "apFloodOffThresh"),
        ("DDOSSECURE4-MIB", "apFloodOffThreshRate"),
        ("DDOSSECURE4-MIB", "apBlockedProtoOffThresh"),
        ("DDOSSECURE4-MIB", "apBlockedProtoOffThreshRate"),
        ("DDOSSECURE4-MIB", "apBlockedStateOffThresh"),
        ("DDOSSECURE4-MIB", "apBlockedStateOffThreshRate"),
        ("DDOSSECURE4-MIB", "apIpAttackOffThresh"),
        ("DDOSSECURE4-MIB", "apIpAttackOffThreshRate"),
        ("DDOSSECURE4-MIB", "apTcpAttackOffThresh"),
        ("DDOSSECURE4-MIB", "apTcpAttackOffThreshRate"),
        ("DDOSSECURE4-MIB", "apUdpAttackOffThresh"),
        ("DDOSSECURE4-MIB", "apUdpAttackOffThreshRate"),
        ("DDOSSECURE4-MIB", "apIcmpAttackOffThresh"),
        ("DDOSSECURE4-MIB", "apIcmpAttackOffThreshRate"),
        ("DDOSSECURE4-MIB", "apOtherIpAttackOffThresh"),
        ("DDOSSECURE4-MIB", "apOtherIpAttackOffThreshRate"),
        ("DDOSSECURE4-MIB", "apFragAttackOffThresh"),
        ("DDOSSECURE4-MIB", "apFragAttackOffThreshRate"),
        ("DDOSSECURE4-MIB", "apBadIpOffThresh"),
        ("DDOSSECURE4-MIB", "apBadIpOffThreshRate"),
        ("DDOSSECURE4-MIB", "apBadTcpOffThresh"),
        ("DDOSSECURE4-MIB", "apBadTcpOffThreshRate"),
        ("DDOSSECURE4-MIB", "apBadUdpOffThresh"),
        ("DDOSSECURE4-MIB", "apBadUdpOffThreshRate"),
        ("DDOSSECURE4-MIB", "apBadIcmpOffThresh"),
        ("DDOSSECURE4-MIB", "apBadIcmpOffThreshRate"),
        ("DDOSSECURE4-MIB", "apBadOtherIpOffThresh"),
        ("DDOSSECURE4-MIB", "apBadOtherIpOffThreshRate"),
        ("DDOSSECURE4-MIB", "apOverloadedIpOffThresh"),
        ("DDOSSECURE4-MIB", "apOverloadedIpOffThreshRate"),
        ("DDOSSECURE4-MIB", "apBandwidthAlertThresh"),
        ("DDOSSECURE4-MIB", "apBandwidthAlertThreshRate"),
        ("DDOSSECURE4-MIB", "apFloodAlertThresh"),
        ("DDOSSECURE4-MIB", "apFloodAlertThreshRate"),
        ("DDOSSECURE4-MIB", "apBlockedProtoAlertThresh"),
        ("DDOSSECURE4-MIB", "apBlockedProtoAlertThreshRate"),
        ("DDOSSECURE4-MIB", "apBlockedStateAlertThresh"),
        ("DDOSSECURE4-MIB", "apBlockedStateAlertThreshRate"),
        ("DDOSSECURE4-MIB", "apIpAttackAlertThresh"),
        ("DDOSSECURE4-MIB", "apIpAttackAlertThreshRate"),
        ("DDOSSECURE4-MIB", "apTcpAttackAlertThresh"),
        ("DDOSSECURE4-MIB", "apTcpAttackAlertThreshRate"),
        ("DDOSSECURE4-MIB", "apUdpAttackAlertThresh"),
        ("DDOSSECURE4-MIB", "apUdpAttackAlertThreshRate"),
        ("DDOSSECURE4-MIB", "apIcmpAttackAlertThresh"),
        ("DDOSSECURE4-MIB", "apIcmpAttackAlertThreshRate"),
        ("DDOSSECURE4-MIB", "apOtherIpAttackAlertThresh"),
        ("DDOSSECURE4-MIB", "apOtherIpAttackAlertThreshRate"),
        ("DDOSSECURE4-MIB", "apFragAttackAlertThresh"),
        ("DDOSSECURE4-MIB", "apFragAttackAlertThreshRate"),
        ("DDOSSECURE4-MIB", "apBadIpAlertThresh"),
        ("DDOSSECURE4-MIB", "apBadIpAlertThreshRate"),
        ("DDOSSECURE4-MIB", "apBadTcpAlertThresh"),
        ("DDOSSECURE4-MIB", "apBadTcpAlertThreshRate"),
        ("DDOSSECURE4-MIB", "apBadUdpAlertThresh"),
        ("DDOSSECURE4-MIB", "apBadUdpAlertThreshRate"),
        ("DDOSSECURE4-MIB", "apBadIcmpAlertThresh"),
        ("DDOSSECURE4-MIB", "apBadIcmpAlertThreshRate"),
        ("DDOSSECURE4-MIB", "apBadOtherIpAlertThresh"),
        ("DDOSSECURE4-MIB", "apBadOtherIpAlertThreshRate"),
        ("DDOSSECURE4-MIB", "apOverloadedIpAlertThresh"),
        ("DDOSSECURE4-MIB", "apOverloadedIpAlertThreshRate"))
)
if mibBuilder.loadTexts:
    apIncidentGroup.setStatus("current")

apDebugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 2, 4)
)
apDebugGroup.setObjects(
      *(("DDOSSECURE4-MIB", "apDebugBandwidthFlag"),
        ("DDOSSECURE4-MIB", "apDebugFloodFlag"),
        ("DDOSSECURE4-MIB", "apDebugBlockedProtocolFlag"),
        ("DDOSSECURE4-MIB", "apDebugBlockedStateFlag"),
        ("DDOSSECURE4-MIB", "apDebugIpAttackFlag"),
        ("DDOSSECURE4-MIB", "apDebugTcpAttackFlag"),
        ("DDOSSECURE4-MIB", "apDebugUdpAttackFlag"),
        ("DDOSSECURE4-MIB", "apDebugIcmpAttackFlag"),
        ("DDOSSECURE4-MIB", "apDebugOtherIpAttackFlag"),
        ("DDOSSECURE4-MIB", "apDebugFragmentAttackFlag"),
        ("DDOSSECURE4-MIB", "apDebugBadIpPacketFlag"),
        ("DDOSSECURE4-MIB", "apDebugBadTcpPacketFlag"),
        ("DDOSSECURE4-MIB", "apDebugBadUdpPacketFlag"),
        ("DDOSSECURE4-MIB", "apDebugBadIcmpFlag"),
        ("DDOSSECURE4-MIB", "apDebugBadOtherIpFlag"),
        ("DDOSSECURE4-MIB", "apDebugOverloadProtectedIpFlag"))
)
if mibBuilder.loadTexts:
    apDebugGroup.setStatus("current")

apGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 2, 5)
)
apGroup.setObjects(
      *(("DDOSSECURE4-MIB", "apBandwidth"),
        ("DDOSSECURE4-MIB", "apFlood"),
        ("DDOSSECURE4-MIB", "apBlockedProtocol"),
        ("DDOSSECURE4-MIB", "apBlockedState"),
        ("DDOSSECURE4-MIB", "apIpAttack"),
        ("DDOSSECURE4-MIB", "apTcpAttack"),
        ("DDOSSECURE4-MIB", "apUdpAttack"),
        ("DDOSSECURE4-MIB", "apIcmpAttack"),
        ("DDOSSECURE4-MIB", "apOtherIpAttack"),
        ("DDOSSECURE4-MIB", "apFragAttack"),
        ("DDOSSECURE4-MIB", "apBadIp"),
        ("DDOSSECURE4-MIB", "apBadTcp"),
        ("DDOSSECURE4-MIB", "apBadUdp"),
        ("DDOSSECURE4-MIB", "apBadIcmp"),
        ("DDOSSECURE4-MIB", "apBadOtherIp"),
        ("DDOSSECURE4-MIB", "apOverloadedIp"),
        ("DDOSSECURE4-MIB", "apInSyn"),
        ("DDOSSECURE4-MIB", "apOutSyn"),
        ("DDOSSECURE4-MIB", "apInSynAck"),
        ("DDOSSECURE4-MIB", "apOutSynAck"),
        ("DDOSSECURE4-MIB", "apInSynSyn"),
        ("DDOSSECURE4-MIB", "apOutSynSyn"),
        ("DDOSSECURE4-MIB", "apInEst"),
        ("DDOSSECURE4-MIB", "apOutEst"),
        ("DDOSSECURE4-MIB", "apInFin1Src"),
        ("DDOSSECURE4-MIB", "apOutFin1Src"),
        ("DDOSSECURE4-MIB", "apInFin2Src"),
        ("DDOSSECURE4-MIB", "apOutFin2Src"),
        ("DDOSSECURE4-MIB", "apInFin3Src"),
        ("DDOSSECURE4-MIB", "apOutFin3Src"),
        ("DDOSSECURE4-MIB", "apInFinFin"),
        ("DDOSSECURE4-MIB", "apOutFinFin"),
        ("DDOSSECURE4-MIB", "apInFin1Dst"),
        ("DDOSSECURE4-MIB", "apOutFin1Dst"),
        ("DDOSSECURE4-MIB", "apInFin2Dst"),
        ("DDOSSECURE4-MIB", "apOutFin2Dst"),
        ("DDOSSECURE4-MIB", "apInFin3Dst"),
        ("DDOSSECURE4-MIB", "apOutFin3Dst"),
        ("DDOSSECURE4-MIB", "apInCls"),
        ("DDOSSECURE4-MIB", "apOutCls"),
        ("DDOSSECURE4-MIB", "apInRst"),
        ("DDOSSECURE4-MIB", "apOutRst"),
        ("DDOSSECURE4-MIB", "apInRstCls"),
        ("DDOSSECURE4-MIB", "apOutRstCls"),
        ("DDOSSECURE4-MIB", "apInUnknown"),
        ("DDOSSECURE4-MIB", "apOutUnknown"),
        ("DDOSSECURE4-MIB", "apInAck"),
        ("DDOSSECURE4-MIB", "apOutAck"),
        ("DDOSSECURE4-MIB", "apInPendAck"),
        ("DDOSSECURE4-MIB", "apOutPendAck"),
        ("DDOSSECURE4-MIB", "apInGet"),
        ("DDOSSECURE4-MIB", "apOutGet"),
        ("DDOSSECURE4-MIB", "apInGets"),
        ("DDOSSECURE4-MIB", "apOutGets"),
        ("DDOSSECURE4-MIB", "apInTotalBpsAvg"),
        ("DDOSSECURE4-MIB", "apOutTotalBpsAvg"),
        ("DDOSSECURE4-MIB", "apInTotalPpsAvg"),
        ("DDOSSECURE4-MIB", "apOutTotalPpsAvg"),
        ("DDOSSECURE4-MIB", "apInSmallPpsAvg"),
        ("DDOSSECURE4-MIB", "apOutSmallPpsAvg"),
        ("DDOSSECURE4-MIB", "apInMediumPpsAvg"),
        ("DDOSSECURE4-MIB", "apOutMediumPpsAvg"),
        ("DDOSSECURE4-MIB", "apInLargePpsAvg"),
        ("DDOSSECURE4-MIB", "apOutLargePpsAvg"),
        ("DDOSSECURE4-MIB", "apInDroppedBpsAvg"),
        ("DDOSSECURE4-MIB", "apOutDroppedBpsAvg"),
        ("DDOSSECURE4-MIB", "apInDroppedPpsAvg"),
        ("DDOSSECURE4-MIB", "apOutDroppedPpsAvg"),
        ("DDOSSECURE4-MIB", "apInCharmDroppedBpsAvg"),
        ("DDOSSECURE4-MIB", "apOutCharmDroppedBpsAvg"),
        ("DDOSSECURE4-MIB", "apInFilteredBwthPercentAvg"),
        ("DDOSSECURE4-MIB", "apOutFilteredBwthPercentAvg"),
        ("DDOSSECURE4-MIB", "apInSynbacklogtallyAvg"),
        ("DDOSSECURE4-MIB", "apOutSynbacklogtallyAvg"),
        ("DDOSSECURE4-MIB", "apInConnectionAvg"),
        ("DDOSSECURE4-MIB", "apOutConnectionAvg"),
        ("DDOSSECURE4-MIB", "apInConnreqAvg"),
        ("DDOSSECURE4-MIB", "apOutConnreqAvg"),
        ("DDOSSECURE4-MIB", "apInActiveHttpGetsAvg"),
        ("DDOSSECURE4-MIB", "apOutActiveHttpGetsAvg"),
        ("DDOSSECURE4-MIB", "apInProtectBwthPktsAvg"),
        ("DDOSSECURE4-MIB", "apOutProtectBwthPktsAvg"),
        ("DDOSSECURE4-MIB", "apInFloodPktsAvg"),
        ("DDOSSECURE4-MIB", "apOutFloodPktsAvg"),
        ("DDOSSECURE4-MIB", "apInBlockedProtocolPktsAvg"),
        ("DDOSSECURE4-MIB", "apOutBlockedProtocolPktsAvg"),
        ("DDOSSECURE4-MIB", "apInBlockedStatePktsAvg"),
        ("DDOSSECURE4-MIB", "apOutBlockedStatePktsAvg"),
        ("DDOSSECURE4-MIB", "apInIpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "apOutIpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "apInTcpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "apOutTcpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "apInUdpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "apOutUdpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "apInIcmpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "apOutIcmpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "apInOtherIpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "apOutOtherIpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "apInFragmentAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "apOutFragmentAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "apInBadipPktsAvg"),
        ("DDOSSECURE4-MIB", "apOutBadipPktsAvg"),
        ("DDOSSECURE4-MIB", "apInBadTcpPktsAvg"),
        ("DDOSSECURE4-MIB", "apOutBadTcpPktsAvg"),
        ("DDOSSECURE4-MIB", "apInBadUdpPktsAvg"),
        ("DDOSSECURE4-MIB", "apOutBadUdpPktsAvg"),
        ("DDOSSECURE4-MIB", "apInBadIcmpPktsAvg"),
        ("DDOSSECURE4-MIB", "apOutBadIcmpPktsAvg"),
        ("DDOSSECURE4-MIB", "apInBadOtherIpPktsAvg"),
        ("DDOSSECURE4-MIB", "apOutBadOtherIpPktsAvg"),
        ("DDOSSECURE4-MIB", "apInOverloadedAvg"),
        ("DDOSSECURE4-MIB", "apOutOverloadedAvg"),
        ("DDOSSECURE4-MIB", "apInLatencyAvg"),
        ("DDOSSECURE4-MIB", "apOutLatencyAvg"),
        ("DDOSSECURE4-MIB", "apInSmallPpsMax"),
        ("DDOSSECURE4-MIB", "apOutSmallPpsMax"),
        ("DDOSSECURE4-MIB", "apInMediumPpsMax"),
        ("DDOSSECURE4-MIB", "apOutMediumPpsMax"),
        ("DDOSSECURE4-MIB", "apInLargePpsMax"),
        ("DDOSSECURE4-MIB", "apOutLargePpsMax"),
        ("DDOSSECURE4-MIB", "apInCharmDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "apOutCharmDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "apInFilteredBwthPercentMax"),
        ("DDOSSECURE4-MIB", "apOutFilteredBwthPercentMax"),
        ("DDOSSECURE4-MIB", "apInSynbacklogtallyMax"),
        ("DDOSSECURE4-MIB", "apOutSynbacklogtallyMax"),
        ("DDOSSECURE4-MIB", "apInConnectionMax"),
        ("DDOSSECURE4-MIB", "apOutConnectionMax"),
        ("DDOSSECURE4-MIB", "apInConnreqMax"),
        ("DDOSSECURE4-MIB", "apOutConnreqMax"),
        ("DDOSSECURE4-MIB", "apInActiveHttpGetsMax"),
        ("DDOSSECURE4-MIB", "apOutActiveHttpGetsMax"),
        ("DDOSSECURE4-MIB", "apInProtectBwthPktsMax"),
        ("DDOSSECURE4-MIB", "apOutProtectBwthPktsMax"),
        ("DDOSSECURE4-MIB", "apInFloodPktsMax"),
        ("DDOSSECURE4-MIB", "apOutFloodPktsMax"),
        ("DDOSSECURE4-MIB", "apInBlockedProtocolPktsMax"),
        ("DDOSSECURE4-MIB", "apOutBlockedProtocolPktsMax"),
        ("DDOSSECURE4-MIB", "apInBlockedStatePktsMax"),
        ("DDOSSECURE4-MIB", "apOutBlockedStatePktsMax"),
        ("DDOSSECURE4-MIB", "apInIpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "apOutIpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "apInTcpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "apOutTcpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "apInUdpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "apOutUdpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "apInIcmpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "apOutIcmpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "apInOtherIpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "apOutOtherIpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "apInFragmentAttackPktsMax"),
        ("DDOSSECURE4-MIB", "apOutFragmentAttackPktsMax"),
        ("DDOSSECURE4-MIB", "apInBadipPktsMax"),
        ("DDOSSECURE4-MIB", "apOutBadipPktsMax"),
        ("DDOSSECURE4-MIB", "apInBadTcpPktsMax"),
        ("DDOSSECURE4-MIB", "apOutBadTcpPktsMax"),
        ("DDOSSECURE4-MIB", "apInBadUdpPktsMax"),
        ("DDOSSECURE4-MIB", "apOutBadUdpPktsMax"),
        ("DDOSSECURE4-MIB", "apInBadIcmpPktsMax"),
        ("DDOSSECURE4-MIB", "apOutBadIcmpPktsMax"),
        ("DDOSSECURE4-MIB", "apInBadOtherIpPktsMax"),
        ("DDOSSECURE4-MIB", "apOutBadOtherIpPktsMax"),
        ("DDOSSECURE4-MIB", "apInOverloadedMax"),
        ("DDOSSECURE4-MIB", "apOutOverloadedMax"),
        ("DDOSSECURE4-MIB", "apInLatencyMax"),
        ("DDOSSECURE4-MIB", "apOutLatencyMax"),
        ("DDOSSECURE4-MIB", "apStalledFlag"),
        ("DDOSSECURE4-MIB", "apOfflineFlag"),
        ("DDOSSECURE4-MIB", "apInTcpConnTally"),
        ("DDOSSECURE4-MIB", "apOutTcpConnTally"),
        ("DDOSSECURE4-MIB", "apInSynBacklogTally"),
        ("DDOSSECURE4-MIB", "apUdpSessionTally"),
        ("DDOSSECURE4-MIB", "apIcmpSessionTally"),
        ("DDOSSECURE4-MIB", "apOtherIpSessionTally"),
        ("DDOSSECURE4-MIB", "apIncidentStart"),
        ("DDOSSECURE4-MIB", "apIncidentAddress"),
        ("DDOSSECURE4-MIB", "apIncidentType"),
        ("DDOSSECURE4-MIB", "apIncidentDirection"),
        ("DDOSSECURE4-MIB", "apIncidentPeakRate"),
        ("DDOSSECURE4-MIB", "apIncidentDropped"))
)
if mibBuilder.loadTexts:
    apGroup.setStatus("current")

prGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 2, 6)
)
prGroup.setObjects(
      *(("DDOSSECURE4-MIB", "prBandwidth"),
        ("DDOSSECURE4-MIB", "prFlood"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"),
        ("DDOSSECURE4-MIB", "prBlockedState"),
        ("DDOSSECURE4-MIB", "prIpAttack"),
        ("DDOSSECURE4-MIB", "prTcpAttack"),
        ("DDOSSECURE4-MIB", "prUdpAttack"),
        ("DDOSSECURE4-MIB", "prIcmpAttack"),
        ("DDOSSECURE4-MIB", "prOtherIpAttack"),
        ("DDOSSECURE4-MIB", "prFragAttack"),
        ("DDOSSECURE4-MIB", "prBadIp"),
        ("DDOSSECURE4-MIB", "prBadTcp"),
        ("DDOSSECURE4-MIB", "prBadUdp"),
        ("DDOSSECURE4-MIB", "prBadIcmp"),
        ("DDOSSECURE4-MIB", "prBadOtherIp"),
        ("DDOSSECURE4-MIB", "prOverloaded"),
        ("DDOSSECURE4-MIB", "prInSyn"),
        ("DDOSSECURE4-MIB", "prOutSyn"),
        ("DDOSSECURE4-MIB", "prInSynAck"),
        ("DDOSSECURE4-MIB", "prOutSynAck"),
        ("DDOSSECURE4-MIB", "prInSynSyn"),
        ("DDOSSECURE4-MIB", "prOutSynSyn"),
        ("DDOSSECURE4-MIB", "prInEst"),
        ("DDOSSECURE4-MIB", "prOutEst"),
        ("DDOSSECURE4-MIB", "prInFin1Src"),
        ("DDOSSECURE4-MIB", "prOutFin1Src"),
        ("DDOSSECURE4-MIB", "prInFin2Src"),
        ("DDOSSECURE4-MIB", "prOutFin2Src"),
        ("DDOSSECURE4-MIB", "prInFin3Src"),
        ("DDOSSECURE4-MIB", "prOutFin3Src"),
        ("DDOSSECURE4-MIB", "prInFinFin"),
        ("DDOSSECURE4-MIB", "prOutFinFin"),
        ("DDOSSECURE4-MIB", "prInFin1Dst"),
        ("DDOSSECURE4-MIB", "prOutFin1Dst"),
        ("DDOSSECURE4-MIB", "prInFin2Dst"),
        ("DDOSSECURE4-MIB", "prOutFin2Dst"),
        ("DDOSSECURE4-MIB", "prInFin3Dst"),
        ("DDOSSECURE4-MIB", "prOutFin3Dst"),
        ("DDOSSECURE4-MIB", "prInCls"),
        ("DDOSSECURE4-MIB", "prOutCls"),
        ("DDOSSECURE4-MIB", "prInRst"),
        ("DDOSSECURE4-MIB", "prOutRst"),
        ("DDOSSECURE4-MIB", "prInRstCls"),
        ("DDOSSECURE4-MIB", "prOutRstCls"),
        ("DDOSSECURE4-MIB", "prInUnknown"),
        ("DDOSSECURE4-MIB", "prOutUnknown"),
        ("DDOSSECURE4-MIB", "prInAck"),
        ("DDOSSECURE4-MIB", "prOutAck"),
        ("DDOSSECURE4-MIB", "prInPendAck"),
        ("DDOSSECURE4-MIB", "prOutPendAck"),
        ("DDOSSECURE4-MIB", "prInGet"),
        ("DDOSSECURE4-MIB", "prOutGet"),
        ("DDOSSECURE4-MIB", "prInGets"),
        ("DDOSSECURE4-MIB", "prOutGets"),
        ("DDOSSECURE4-MIB", "prOverloadedFlag"),
        ("DDOSSECURE4-MIB", "prInTcpConnTally"),
        ("DDOSSECURE4-MIB", "prOutTcpConnTally"),
        ("DDOSSECURE4-MIB", "prInSynBacklogTally"),
        ("DDOSSECURE4-MIB", "prInTotalBytesCnt"),
        ("DDOSSECURE4-MIB", "prOutTotalBytesCnt"),
        ("DDOSSECURE4-MIB", "prInDroppedBytesCnt"),
        ("DDOSSECURE4-MIB", "prOutDroppedBytesCnt"),
        ("DDOSSECURE4-MIB", "prInCharmDroppedBytesCnt"),
        ("DDOSSECURE4-MIB", "prOutCharmDroppedBytesCnt"),
        ("DDOSSECURE4-MIB", "prInTotalPpsMax"),
        ("DDOSSECURE4-MIB", "prOutTotalPpsMax"),
        ("DDOSSECURE4-MIB", "prInDroppedPpsMax"),
        ("DDOSSECURE4-MIB", "prOutDroppedPpsMax"),
        ("DDOSSECURE4-MIB", "prInTotalBpsMax"),
        ("DDOSSECURE4-MIB", "prOutTotalBpsMax"),
        ("DDOSSECURE4-MIB", "prInDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "prOutDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "prInCharmDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "prOutCharmDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "prInProtectBwthPktsCnt"),
        ("DDOSSECURE4-MIB", "prOutProtectBwthPktsCnt"),
        ("DDOSSECURE4-MIB", "prInFloodPktsCnt"),
        ("DDOSSECURE4-MIB", "prOutFloodPktsCnt"),
        ("DDOSSECURE4-MIB", "prInBlockedProtocolPktsCnt"),
        ("DDOSSECURE4-MIB", "prOutBlockedProtocolPktsCnt"),
        ("DDOSSECURE4-MIB", "prInBlockedStatePktsCnt"),
        ("DDOSSECURE4-MIB", "prOutBlockedStatePktsCnt"),
        ("DDOSSECURE4-MIB", "prInIpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "prOutIpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "prInTcpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "prOutTcpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "prInUdpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "prOutUdpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "prInIcmpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "prOutIcmpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "prInOtherIpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "prOutOtherIpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "prInFragmentAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "prOutFragmentAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "prInBadIpPktsCnt"),
        ("DDOSSECURE4-MIB", "prOutBadIpPktsCnt"),
        ("DDOSSECURE4-MIB", "prInBadTcpPktsCnt"),
        ("DDOSSECURE4-MIB", "prOutBadTcpPktsCnt"),
        ("DDOSSECURE4-MIB", "prInBadUdpPktsCnt"),
        ("DDOSSECURE4-MIB", "prOutBadUdpPktsCnt"),
        ("DDOSSECURE4-MIB", "prInBadIcmpPktsCnt"),
        ("DDOSSECURE4-MIB", "prOutBadIcmpPktsCnt"),
        ("DDOSSECURE4-MIB", "prInBadOtherIpPktsCnt"),
        ("DDOSSECURE4-MIB", "prOutBadOtherIpPktsCnt"),
        ("DDOSSECURE4-MIB", "prInTotalBpsAvg"),
        ("DDOSSECURE4-MIB", "prOutTotalBpsAvg"),
        ("DDOSSECURE4-MIB", "prInTotalPpsAvg"),
        ("DDOSSECURE4-MIB", "prOutTotalPpsAvg"),
        ("DDOSSECURE4-MIB", "prInSmallPpsAvg"),
        ("DDOSSECURE4-MIB", "prOutSmallPpsAvg"),
        ("DDOSSECURE4-MIB", "prInMediumPpsAvg"),
        ("DDOSSECURE4-MIB", "prOutMediumPpsAvg"),
        ("DDOSSECURE4-MIB", "prInLargePpsAvg"),
        ("DDOSSECURE4-MIB", "prOutLargePpsAvg"),
        ("DDOSSECURE4-MIB", "prInDroppedBpsAvg"),
        ("DDOSSECURE4-MIB", "prOutDroppedBpsAvg"),
        ("DDOSSECURE4-MIB", "prInDroppedPpsAvg"),
        ("DDOSSECURE4-MIB", "prOutDroppedPpsAvg"),
        ("DDOSSECURE4-MIB", "prInCharmDroppedBpsAvg"),
        ("DDOSSECURE4-MIB", "prOutCharmDroppedBpsAvg"),
        ("DDOSSECURE4-MIB", "prInFilteredBwthPercentAvg"),
        ("DDOSSECURE4-MIB", "prOutFilteredBwthPercentAvg"),
        ("DDOSSECURE4-MIB", "prInSynbacklogtallyAvg"),
        ("DDOSSECURE4-MIB", "prOutSynbacklogtallyAvg"),
        ("DDOSSECURE4-MIB", "prInConnectionAvg"),
        ("DDOSSECURE4-MIB", "prOutConnectionAvg"),
        ("DDOSSECURE4-MIB", "prInConnreqAvg"),
        ("DDOSSECURE4-MIB", "prOutConnreqAvg"),
        ("DDOSSECURE4-MIB", "prInActiveHttpGetsAvg"),
        ("DDOSSECURE4-MIB", "prOutActiveHttpGetsAvg"),
        ("DDOSSECURE4-MIB", "prInProtectBwthPktsAvg"),
        ("DDOSSECURE4-MIB", "prOutProtectBwthPktsAvg"),
        ("DDOSSECURE4-MIB", "prInFloodPktsAvg"),
        ("DDOSSECURE4-MIB", "prOutFloodPktsAvg"),
        ("DDOSSECURE4-MIB", "prInBlockedProtocolPktsAvg"),
        ("DDOSSECURE4-MIB", "prOutBlockedProtocolPktsAvg"),
        ("DDOSSECURE4-MIB", "prInBlockedStatePktsAvg"),
        ("DDOSSECURE4-MIB", "prOutBlockedStatePktsAvg"),
        ("DDOSSECURE4-MIB", "prInIpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "prOutIpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "prInTcpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "prOutTcpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "prInUdpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "prOutUdpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "prInIcmpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "prOutIcmpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "prInOtherIpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "prOutOtherIpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "prInFragmentAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "prOutFragmentAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "prInBadipPktsAvg"),
        ("DDOSSECURE4-MIB", "prOutBadipPktsAvg"),
        ("DDOSSECURE4-MIB", "prInBadTcpPktsAvg"),
        ("DDOSSECURE4-MIB", "prOutBadTcpPktsAvg"),
        ("DDOSSECURE4-MIB", "prInBadUdpPktsAvg"),
        ("DDOSSECURE4-MIB", "prOutBadUdpPktsAvg"),
        ("DDOSSECURE4-MIB", "prInBadIcmpPktsAvg"),
        ("DDOSSECURE4-MIB", "prOutBadIcmpPktsAvg"),
        ("DDOSSECURE4-MIB", "prInBadOtherIpPktsAvg"),
        ("DDOSSECURE4-MIB", "prOutBadOtherIpPktsAvg"),
        ("DDOSSECURE4-MIB", "prInOverloadedAvg"),
        ("DDOSSECURE4-MIB", "prOutOverloadedAvg"),
        ("DDOSSECURE4-MIB", "prInLatencyAvg"),
        ("DDOSSECURE4-MIB", "prOutLatencyAvg"),
        ("DDOSSECURE4-MIB", "prInTotalBpsMax"),
        ("DDOSSECURE4-MIB", "prOutTotalBpsMax"),
        ("DDOSSECURE4-MIB", "prInTotalPpsMax"),
        ("DDOSSECURE4-MIB", "prOutTotalPpsMax"),
        ("DDOSSECURE4-MIB", "prInSmallPpsMax"),
        ("DDOSSECURE4-MIB", "prOutSmallPpsMax"),
        ("DDOSSECURE4-MIB", "prInMediumPpsMax"),
        ("DDOSSECURE4-MIB", "prOutMediumPpsMax"),
        ("DDOSSECURE4-MIB", "prInLargePpsMax"),
        ("DDOSSECURE4-MIB", "prOutLargePpsMax"),
        ("DDOSSECURE4-MIB", "prInDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "prOutDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "prInDroppedPpsMax"),
        ("DDOSSECURE4-MIB", "prOutDroppedPpsMax"),
        ("DDOSSECURE4-MIB", "prInCharmDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "prOutCharmDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "prInFilteredBwthPercentMax"),
        ("DDOSSECURE4-MIB", "prOutFilteredBwthPercentMax"),
        ("DDOSSECURE4-MIB", "prInSynbacklogtallyMax"),
        ("DDOSSECURE4-MIB", "prOutSynbacklogtallyMax"),
        ("DDOSSECURE4-MIB", "prInConnectionMax"),
        ("DDOSSECURE4-MIB", "prOutConnectionMax"),
        ("DDOSSECURE4-MIB", "prInConnreqMax"),
        ("DDOSSECURE4-MIB", "prOutConnreqMax"),
        ("DDOSSECURE4-MIB", "prInActiveHttpGetsMax"),
        ("DDOSSECURE4-MIB", "prOutActiveHttpGetsMax"),
        ("DDOSSECURE4-MIB", "prInProtectBwthPktsMax"),
        ("DDOSSECURE4-MIB", "prOutProtectBwthPktsMax"),
        ("DDOSSECURE4-MIB", "prInFloodPktsMax"),
        ("DDOSSECURE4-MIB", "prOutFloodPktsMax"),
        ("DDOSSECURE4-MIB", "prInBlockedProtocolPktsMax"),
        ("DDOSSECURE4-MIB", "prOutBlockedProtocolPktsMax"),
        ("DDOSSECURE4-MIB", "prInBlockedStatePktsMax"),
        ("DDOSSECURE4-MIB", "prOutBlockedStatePktsMax"),
        ("DDOSSECURE4-MIB", "prInIpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "prOutIpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "prInTcpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "prOutTcpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "prInUdpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "prOutUdpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "prInIcmpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "prOutIcmpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "prInOtherIpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "prOutOtherIpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "prInFragmentAttackPktsMax"),
        ("DDOSSECURE4-MIB", "prOutFragmentAttackPktsMax"),
        ("DDOSSECURE4-MIB", "prInBadipPktsMax"),
        ("DDOSSECURE4-MIB", "prOutBadipPktsMax"),
        ("DDOSSECURE4-MIB", "prInBadTcpPktsMax"),
        ("DDOSSECURE4-MIB", "prOutBadTcpPktsMax"),
        ("DDOSSECURE4-MIB", "prInBadUdpPktsMax"),
        ("DDOSSECURE4-MIB", "prOutBadUdpPktsMax"),
        ("DDOSSECURE4-MIB", "prInBadIcmpPktsMax"),
        ("DDOSSECURE4-MIB", "prOutBadIcmpPktsMax"),
        ("DDOSSECURE4-MIB", "prInBadOtherIpPktsMax"),
        ("DDOSSECURE4-MIB", "prOutBadOtherIpPktsMax"),
        ("DDOSSECURE4-MIB", "prInOverloadedMax"),
        ("DDOSSECURE4-MIB", "prOutOverloadedMax"),
        ("DDOSSECURE4-MIB", "prInLatencyMax"),
        ("DDOSSECURE4-MIB", "prOutLatencyMax"),
        ("DDOSSECURE4-MIB", "prIncidentStart"),
        ("DDOSSECURE4-MIB", "prIncidentAddress"),
        ("DDOSSECURE4-MIB", "prIncidentType"),
        ("DDOSSECURE4-MIB", "prIncidentDirection"),
        ("DDOSSECURE4-MIB", "prIncidentPeakRate"),
        ("DDOSSECURE4-MIB", "prIncidentDropped"))
)
if mibBuilder.loadTexts:
    prGroup.setStatus("current")

prCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 2, 7)
)
prCfgGroup.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpBacklog"),
        ("DDOSSECURE4-MIB", "prMaxConnections"),
        ("DDOSSECURE4-MIB", "prMaxConnectionRate"),
        ("DDOSSECURE4-MIB", "prInFilterName"),
        ("DDOSSECURE4-MIB", "prOutFilterName"),
        ("DDOSSECURE4-MIB", "prSendTcpRejects"),
        ("DDOSSECURE4-MIB", "prTrackSoap"),
        ("DDOSSECURE4-MIB", "prOperationMode"),
        ("DDOSSECURE4-MIB", "prMaxGets"),
        ("DDOSSECURE4-MIB", "prFragsDisabled"))
)
if mibBuilder.loadTexts:
    prCfgGroup.setStatus("current")

gwCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 2, 8)
)
gwCfgGroup.setObjects(
      *(("DDOSSECURE4-MIB", "gwInternetConfigMacAddress"),
        ("DDOSSECURE4-MIB", "gwInternetConfigToSpeedBps"),
        ("DDOSSECURE4-MIB", "gwInternetConfigToRatePps"),
        ("DDOSSECURE4-MIB", "gwProtectedConfigMacAddress"),
        ("DDOSSECURE4-MIB", "gwProtectedConfigToSpeedBps"),
        ("DDOSSECURE4-MIB", "gwProtectedConfigToRatePps"))
)
if mibBuilder.loadTexts:
    gwCfgGroup.setStatus("current")

apEventObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 2, 9)
)
apEventObjectGroup.setObjects(
      *(("DDOSSECURE4-MIB", "apOutputErrorIIFlag"),
        ("DDOSSECURE4-MIB", "apOutputErrorPIFlag"),
        ("DDOSSECURE4-MIB", "apOutputErrorMIFlag"),
        ("DDOSSECURE4-MIB", "apNewConfigFlag"),
        ("DDOSSECURE4-MIB", "apNotLicensedFlag"),
        ("DDOSSECURE4-MIB", "apMacTableFullFlag"),
        ("DDOSSECURE4-MIB", "apProtectedTableFullFlag"),
        ("DDOSSECURE4-MIB", "apIncidentTableFullFlag"),
        ("DDOSSECURE4-MIB", "apTcpTableFullFlag"),
        ("DDOSSECURE4-MIB", "apUdpTableFullFlag"),
        ("DDOSSECURE4-MIB", "apIcmpTableFullFlag"),
        ("DDOSSECURE4-MIB", "apOtherIpTableFullFlag"),
        ("DDOSSECURE4-MIB", "apFragTableFullFlag"),
        ("DDOSSECURE4-MIB", "apFtpTableFullFlag"),
        ("DDOSSECURE4-MIB", "apBlockedTableFullFlag"),
        ("DDOSSECURE4-MIB", "apShortCircuitFlag"),
        ("DDOSSECURE4-MIB", "apInternetIfDisconnectedFlag"),
        ("DDOSSECURE4-MIB", "apProtectedIfDisconnectedFlag"),
        ("DDOSSECURE4-MIB", "apMgmtIfDisconnectedFlag"),
        ("DDOSSECURE4-MIB", "apUpgradingFlag"),
        ("DDOSSECURE4-MIB", "apProtectedIfTrafficFlag"),
        ("DDOSSECURE4-MIB", "apRoutingLoopFlag"),
        ("DDOSSECURE4-MIB", "apStateLearningFlag"),
        ("DDOSSECURE4-MIB", "apSupportExpiredFlag"),
        ("DDOSSECURE4-MIB", "apSevereLoadingFlag"),
        ("DDOSSECURE4-MIB", "apMacMisconfiguredFlag"),
        ("DDOSSECURE4-MIB", "apIfMisconfiguredFlag"),
        ("DDOSSECURE4-MIB", "apInternetIfLinkDownFlag"),
        ("DDOSSECURE4-MIB", "apProtectedIfLinkDownFlag"),
        ("DDOSSECURE4-MIB", "apDatashareIfDisconnectedFlag"),
        ("DDOSSECURE4-MIB", "apDiskFailingFlag"),
        ("DDOSSECURE4-MIB", "apPsuFailingFlag"),
        ("DDOSSECURE4-MIB", "apFanFailingFlag"),
        ("DDOSSECURE4-MIB", "apConfigXferFailFlag"),
        ("DDOSSECURE4-MIB", "apMissingRequiredPartnerFlag"),
        ("DDOSSECURE4-MIB", "apBgpMisconfiguredIpFlag"))
)
if mibBuilder.loadTexts:
    apEventObjectGroup.setStatus("current")

apRatesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 2, 10)
)
apRatesGroup.setObjects(
      *(("DDOSSECURE4-MIB", "apInTotalBytesCnt"),
        ("DDOSSECURE4-MIB", "apOutTotalBytesCnt"),
        ("DDOSSECURE4-MIB", "apInDroppedBytesCnt"),
        ("DDOSSECURE4-MIB", "apOutDroppedBytesCnt"),
        ("DDOSSECURE4-MIB", "apInCharmDroppedBytesCnt"),
        ("DDOSSECURE4-MIB", "apOutCharmDroppedBytesCnt"),
        ("DDOSSECURE4-MIB", "apInTotalPpsMax"),
        ("DDOSSECURE4-MIB", "apOutTotalPpsMax"),
        ("DDOSSECURE4-MIB", "apInDroppedPpsMax"),
        ("DDOSSECURE4-MIB", "apOutDroppedPpsMax"),
        ("DDOSSECURE4-MIB", "apInTotalBpsMax"),
        ("DDOSSECURE4-MIB", "apOutTotalBpsMax"),
        ("DDOSSECURE4-MIB", "apInDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "apOutDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "apInCharmDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "apOutCharmDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "apInProtectBwthPktsCnt"),
        ("DDOSSECURE4-MIB", "apOutProtectBwthPktsCnt"),
        ("DDOSSECURE4-MIB", "apInFloodPktsCnt"),
        ("DDOSSECURE4-MIB", "apOutFloodPktsCnt"),
        ("DDOSSECURE4-MIB", "apInBlockedProtocolPktsCnt"),
        ("DDOSSECURE4-MIB", "apOutBlockedProtocolPktsCnt"),
        ("DDOSSECURE4-MIB", "apInBlockedStatePktsCnt"),
        ("DDOSSECURE4-MIB", "apOutBlockedStatePktsCnt"),
        ("DDOSSECURE4-MIB", "apInIpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "apOutIpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "apInTcpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "apOutTcpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "apInUdpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "apOutUdpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "apInIcmpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "apOutIcmpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "apInOtherIpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "apOutOtherIpAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "apInFragmentAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "apOutFragmentAttackPktsCnt"),
        ("DDOSSECURE4-MIB", "apInBadIpPktsCnt"),
        ("DDOSSECURE4-MIB", "apOutBadIpPktsCnt"),
        ("DDOSSECURE4-MIB", "apInBadTcpPktsCnt"),
        ("DDOSSECURE4-MIB", "apOutBadTcpPktsCnt"),
        ("DDOSSECURE4-MIB", "apInBadUdpPktsCnt"),
        ("DDOSSECURE4-MIB", "apOutBadUdpPktsCnt"),
        ("DDOSSECURE4-MIB", "apInBadIcmpPktsCnt"),
        ("DDOSSECURE4-MIB", "apOutBadIcmpPktsCnt"),
        ("DDOSSECURE4-MIB", "apInBadOtherIpPktsCnt"),
        ("DDOSSECURE4-MIB", "apOutBadOtherIpPktsCnt"),
        ("DDOSSECURE4-MIB", "apInTotalBytesCnt"),
        ("DDOSSECURE4-MIB", "apOutTotalBytesCnt"),
        ("DDOSSECURE4-MIB", "apInTotalPpsCnt"),
        ("DDOSSECURE4-MIB", "apOutTotalPpsCnt"),
        ("DDOSSECURE4-MIB", "apInSmallPpsCnt"),
        ("DDOSSECURE4-MIB", "apOutSmallPpsCnt"),
        ("DDOSSECURE4-MIB", "apInMediumPpsCnt"),
        ("DDOSSECURE4-MIB", "apOutMediumPpsCnt"),
        ("DDOSSECURE4-MIB", "apInLargePpsCnt"),
        ("DDOSSECURE4-MIB", "apOutLargePpsCnt"),
        ("DDOSSECURE4-MIB", "apInDroppedBytesCnt"),
        ("DDOSSECURE4-MIB", "apOutDroppedBytesCnt"),
        ("DDOSSECURE4-MIB", "apInDroppedPpsCnt"),
        ("DDOSSECURE4-MIB", "apOutDroppedPpsCnt"),
        ("DDOSSECURE4-MIB", "apInFilteredBwthPercentCnt"),
        ("DDOSSECURE4-MIB", "apOutFilteredBwthPercentCnt"),
        ("DDOSSECURE4-MIB", "apInConnreqCnt"),
        ("DDOSSECURE4-MIB", "apOutConnreqCnt"),
        ("DDOSSECURE4-MIB", "apInOverloadedCnt"),
        ("DDOSSECURE4-MIB", "apOutOverloadedCnt"))
)
if mibBuilder.loadTexts:
    apRatesGroup.setStatus("current")

poFilterCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 2, 11)
)
poFilterCfgGroup.setObjects(
      *(("DDOSSECURE4-MIB", "poFilterName"),
        ("DDOSSECURE4-MIB", "poTcpPortsList"),
        ("DDOSSECURE4-MIB", "poUdpPortsList"),
        ("DDOSSECURE4-MIB", "poIcmpTypesList"),
        ("DDOSSECURE4-MIB", "poIpProtocolsList"))
)
if mibBuilder.loadTexts:
    poFilterCfgGroup.setStatus("current")

apLinkStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 2, 12)
)
apLinkStatusGroup.setObjects(
      *(("DDOSSECURE4-MIB", "apMgmtIfLinkModeState"),
        ("DDOSSECURE4-MIB", "apIntIfLinkModeState"),
        ("DDOSSECURE4-MIB", "apMgmtIfLinkFCState"),
        ("DDOSSECURE4-MIB", "apIntIfLinkFCState"),
        ("DDOSSECURE4-MIB", "apProtIfLinkModeState"),
        ("DDOSSECURE4-MIB", "apProtIfLinkFCState"))
)
if mibBuilder.loadTexts:
    apLinkStatusGroup.setStatus("current")

apLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 2, 13)
)
apLogGroup.setObjects(
      *(("DDOSSECURE4-MIB", "apWorstOffenderLastTime"),
        ("DDOSSECURE4-MIB", "apWorstOffenderCount"),
        ("DDOSSECURE4-MIB", "apLogFileRecord"))
)
if mibBuilder.loadTexts:
    apLogGroup.setStatus("current")

apHaCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 2, 14)
)
apHaCfgGroup.setObjects(
      *(("DDOSSECURE4-MIB", "apHaState"),
        ("DDOSSECURE4-MIB", "apHaPartnerList"),
        ("DDOSSECURE4-MIB", "apHaPartnerTime"))
)
if mibBuilder.loadTexts:
    apHaCfgGroup.setStatus("current")

poGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 2, 15)
)
poGroup.setObjects(
      *(("DDOSSECURE4-MIB", "poPortalName"),
        ("DDOSSECURE4-MIB", "poInTotalBpsAvg"),
        ("DDOSSECURE4-MIB", "poOutTotalBpsAvg"),
        ("DDOSSECURE4-MIB", "poInTotalPpsAvg"),
        ("DDOSSECURE4-MIB", "poOutTotalPpsAvg"),
        ("DDOSSECURE4-MIB", "poInSmallPpsAvg"),
        ("DDOSSECURE4-MIB", "poOutSmallPpsAvg"),
        ("DDOSSECURE4-MIB", "poInMediumPpsAvg"),
        ("DDOSSECURE4-MIB", "poOutMediumPpsAvg"),
        ("DDOSSECURE4-MIB", "poInLargePpsAvg"),
        ("DDOSSECURE4-MIB", "poOutLargePpsAvg"),
        ("DDOSSECURE4-MIB", "poInDroppedBpsAvg"),
        ("DDOSSECURE4-MIB", "poOutDroppedBpsAvg"),
        ("DDOSSECURE4-MIB", "poInDroppedPpsAvg"),
        ("DDOSSECURE4-MIB", "poOutDroppedPpsAvg"),
        ("DDOSSECURE4-MIB", "poInCharmDroppedBpsAvg"),
        ("DDOSSECURE4-MIB", "poOutCharmDroppedBpsAvg"),
        ("DDOSSECURE4-MIB", "poInFilteredBwthPercentAvg"),
        ("DDOSSECURE4-MIB", "poOutFilteredBwthPercentAvg"),
        ("DDOSSECURE4-MIB", "poInSynbacklogtallyAvg"),
        ("DDOSSECURE4-MIB", "poOutSynbacklogtallyAvg"),
        ("DDOSSECURE4-MIB", "poInConnectionAvg"),
        ("DDOSSECURE4-MIB", "poOutConnectionAvg"),
        ("DDOSSECURE4-MIB", "poInConnreqAvg"),
        ("DDOSSECURE4-MIB", "poOutConnreqAvg"),
        ("DDOSSECURE4-MIB", "poInActiveHttpGetsAvg"),
        ("DDOSSECURE4-MIB", "poOutActiveHttpGetsAvg"),
        ("DDOSSECURE4-MIB", "poInProtectBwthPktsAvg"),
        ("DDOSSECURE4-MIB", "poOutProtectBwthPktsAvg"),
        ("DDOSSECURE4-MIB", "poInFloodPktsAvg"),
        ("DDOSSECURE4-MIB", "poOutFloodPktsAvg"),
        ("DDOSSECURE4-MIB", "poInBlockedProtocolPktsAvg"),
        ("DDOSSECURE4-MIB", "poOutBlockedProtocolPktsAvg"),
        ("DDOSSECURE4-MIB", "poInBlockedStatePktsAvg"),
        ("DDOSSECURE4-MIB", "poOutBlockedStatePktsAvg"),
        ("DDOSSECURE4-MIB", "poInIpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "poOutIpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "poInTcpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "poOutTcpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "poInUdpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "poOutUdpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "poInIcmpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "poOutIcmpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "poInOtherIpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "poOutOtherIpAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "poInFragmentAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "poOutFragmentAttackPktsAvg"),
        ("DDOSSECURE4-MIB", "poInBadipPktsAvg"),
        ("DDOSSECURE4-MIB", "poOutBadipPktsAvg"),
        ("DDOSSECURE4-MIB", "poInBadTcpPktsAvg"),
        ("DDOSSECURE4-MIB", "poOutBadTcpPktsAvg"),
        ("DDOSSECURE4-MIB", "poInBadUdpPktsAvg"),
        ("DDOSSECURE4-MIB", "poOutBadUdpPktsAvg"),
        ("DDOSSECURE4-MIB", "poInBadIcmpPktsAvg"),
        ("DDOSSECURE4-MIB", "poOutBadIcmpPktsAvg"),
        ("DDOSSECURE4-MIB", "poInBadOtherIpPktsAvg"),
        ("DDOSSECURE4-MIB", "poOutBadOtherIpPktsAvg"),
        ("DDOSSECURE4-MIB", "poInOverloadedAvg"),
        ("DDOSSECURE4-MIB", "poOutOverloadedAvg"),
        ("DDOSSECURE4-MIB", "poInLatencyAvg"),
        ("DDOSSECURE4-MIB", "poOutLatencyAvg"),
        ("DDOSSECURE4-MIB", "poInTotalBpsMax"),
        ("DDOSSECURE4-MIB", "poOutTotalBpsMax"),
        ("DDOSSECURE4-MIB", "poInTotalPpsMax"),
        ("DDOSSECURE4-MIB", "poOutTotalPpsMax"),
        ("DDOSSECURE4-MIB", "poInSmallPpsMax"),
        ("DDOSSECURE4-MIB", "poOutSmallPpsMax"),
        ("DDOSSECURE4-MIB", "poInMediumPpsMax"),
        ("DDOSSECURE4-MIB", "poOutMediumPpsMax"),
        ("DDOSSECURE4-MIB", "poInLargePpsMax"),
        ("DDOSSECURE4-MIB", "poOutLargePpsMax"),
        ("DDOSSECURE4-MIB", "poInDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "poOutDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "poInDroppedPpsMax"),
        ("DDOSSECURE4-MIB", "poOutDroppedPpsMax"),
        ("DDOSSECURE4-MIB", "poInCharmDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "poOutCharmDroppedBpsMax"),
        ("DDOSSECURE4-MIB", "poInFilteredBwthPercentMax"),
        ("DDOSSECURE4-MIB", "poOutFilteredBwthPercentMax"),
        ("DDOSSECURE4-MIB", "poInSynbacklogtallyMax"),
        ("DDOSSECURE4-MIB", "poOutSynbacklogtallyMax"),
        ("DDOSSECURE4-MIB", "poInConnectionMax"),
        ("DDOSSECURE4-MIB", "poOutConnectionMax"),
        ("DDOSSECURE4-MIB", "poInConnreqMax"),
        ("DDOSSECURE4-MIB", "poOutConnreqMax"),
        ("DDOSSECURE4-MIB", "poInActiveHttpGetsMax"),
        ("DDOSSECURE4-MIB", "poOutActiveHttpGetsMax"),
        ("DDOSSECURE4-MIB", "poInProtectBwthPktsMax"),
        ("DDOSSECURE4-MIB", "poOutProtectBwthPktsMax"),
        ("DDOSSECURE4-MIB", "poInFloodPktsMax"),
        ("DDOSSECURE4-MIB", "poOutFloodPktsMax"),
        ("DDOSSECURE4-MIB", "poInBlockedProtocolPktsMax"),
        ("DDOSSECURE4-MIB", "poOutBlockedProtocolPktsMax"),
        ("DDOSSECURE4-MIB", "poInBlockedStatePktsMax"),
        ("DDOSSECURE4-MIB", "poOutBlockedStatePktsMax"),
        ("DDOSSECURE4-MIB", "poInIpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "poOutIpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "poInTcpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "poOutTcpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "poInUdpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "poOutUdpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "poInIcmpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "poOutIcmpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "poInOtherIpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "poOutOtherIpAttackPktsMax"),
        ("DDOSSECURE4-MIB", "poInFragmentAttackPktsMax"),
        ("DDOSSECURE4-MIB", "poOutFragmentAttackPktsMax"),
        ("DDOSSECURE4-MIB", "poInBadipPktsMax"),
        ("DDOSSECURE4-MIB", "poOutBadipPktsMax"),
        ("DDOSSECURE4-MIB", "poInBadTcpPktsMax"),
        ("DDOSSECURE4-MIB", "poOutBadTcpPktsMax"),
        ("DDOSSECURE4-MIB", "poInBadUdpPktsMax"),
        ("DDOSSECURE4-MIB", "poOutBadUdpPktsMax"),
        ("DDOSSECURE4-MIB", "poInBadIcmpPktsMax"),
        ("DDOSSECURE4-MIB", "poOutBadIcmpPktsMax"),
        ("DDOSSECURE4-MIB", "poInBadOtherIpPktsMax"),
        ("DDOSSECURE4-MIB", "poOutBadOtherIpPktsMax"),
        ("DDOSSECURE4-MIB", "poInOverloadedMax"),
        ("DDOSSECURE4-MIB", "poOutOverloadedMax"),
        ("DDOSSECURE4-MIB", "poInLatencyMax"),
        ("DDOSSECURE4-MIB", "poOutLatencyMax"),
        ("DDOSSECURE4-MIB", "poInTotalBytesCnt"),
        ("DDOSSECURE4-MIB", "poOutTotalBytesCnt"),
        ("DDOSSECURE4-MIB", "poInDroppedBytesCnt"),
        ("DDOSSECURE4-MIB", "poOutDroppedBytesCnt"),
        ("DDOSSECURE4-MIB", "poInCharmDroppedBytesCnt"),
        ("DDOSSECURE4-MIB", "poOutCharmDroppedBytesCnt"),
        ("DDOSSECURE4-MIB", "poInTotalPpsCnt"),
        ("DDOSSECURE4-MIB", "poOutTotalPpsCnt"),
        ("DDOSSECURE4-MIB", "poInSmallPpsCnt"),
        ("DDOSSECURE4-MIB", "poOutSmallPpsCnt"),
        ("DDOSSECURE4-MIB", "poInMediumPpsCnt"),
        ("DDOSSECURE4-MIB", "poOutMediumPpsCnt"),
        ("DDOSSECURE4-MIB", "poInLargePpsCnt"),
        ("DDOSSECURE4-MIB", "poOutLargePpsCnt"),
        ("DDOSSECURE4-MIB", "poInDroppedPpsCnt"),
        ("DDOSSECURE4-MIB", "poOutDroppedPpsCnt"),
        ("DDOSSECURE4-MIB", "poInFilteredBwthPercentCnt"),
        ("DDOSSECURE4-MIB", "poOutFilteredBwthPercentCnt"),
        ("DDOSSECURE4-MIB", "poInConnreqCnt"),
        ("DDOSSECURE4-MIB", "poOutConnreqCnt"),
        ("DDOSSECURE4-MIB", "poIncidentPortalName"),
        ("DDOSSECURE4-MIB", "poIncidentStart"),
        ("DDOSSECURE4-MIB", "poIncidentAddress"),
        ("DDOSSECURE4-MIB", "poIncidentType"),
        ("DDOSSECURE4-MIB", "poIncidentDirection"),
        ("DDOSSECURE4-MIB", "poIncidentPeakRate"),
        ("DDOSSECURE4-MIB", "poIncidentDropped"))
)
if mibBuilder.loadTexts:
    poGroup.setStatus("current")


# Notification objects

apOutputErrorIIEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1)
)
apOutputErrorIIEvent.setObjects(
    ("DDOSSECURE4-MIB", "apOutputErrorIIFlag")
)
if mibBuilder.loadTexts:
    apOutputErrorIIEvent.setStatus(
        "deprecated"
    )

apOutputErrorPIEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2)
)
apOutputErrorPIEvent.setObjects(
    ("DDOSSECURE4-MIB", "apOutputErrorPIFlag")
)
if mibBuilder.loadTexts:
    apOutputErrorPIEvent.setStatus(
        "deprecated"
    )

apOutputErrorMIEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3)
)
apOutputErrorMIEvent.setObjects(
    ("DDOSSECURE4-MIB", "apOutputErrorMIFlag")
)
if mibBuilder.loadTexts:
    apOutputErrorMIEvent.setStatus(
        "deprecated"
    )

apNewConfigEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 4)
)
apNewConfigEvent.setObjects(
    ("DDOSSECURE4-MIB", "apNewConfigFlag")
)
if mibBuilder.loadTexts:
    apNewConfigEvent.setStatus(
        "deprecated"
    )

apNotLicensedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 5)
)
apNotLicensedEvent.setObjects(
    ("DDOSSECURE4-MIB", "apNotLicensedFlag")
)
if mibBuilder.loadTexts:
    apNotLicensedEvent.setStatus(
        "deprecated"
    )

apMacTableFullEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 6)
)
apMacTableFullEvent.setObjects(
    ("DDOSSECURE4-MIB", "apMacTableFullFlag")
)
if mibBuilder.loadTexts:
    apMacTableFullEvent.setStatus(
        "deprecated"
    )

apProtectedTableFullEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 7)
)
apProtectedTableFullEvent.setObjects(
    ("DDOSSECURE4-MIB", "apProtectedTableFullFlag")
)
if mibBuilder.loadTexts:
    apProtectedTableFullEvent.setStatus(
        "deprecated"
    )

apIncidentTableFullEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 8)
)
apIncidentTableFullEvent.setObjects(
    ("DDOSSECURE4-MIB", "apIncidentTableFullFlag")
)
if mibBuilder.loadTexts:
    apIncidentTableFullEvent.setStatus(
        "deprecated"
    )

apTcpTableFullEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 9)
)
apTcpTableFullEvent.setObjects(
    ("DDOSSECURE4-MIB", "apTcpTableFullFlag")
)
if mibBuilder.loadTexts:
    apTcpTableFullEvent.setStatus(
        "deprecated"
    )

apUdpTableFullEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 10)
)
apUdpTableFullEvent.setObjects(
    ("DDOSSECURE4-MIB", "apUdpTableFullFlag")
)
if mibBuilder.loadTexts:
    apUdpTableFullEvent.setStatus(
        "deprecated"
    )

apIcmpTableFullEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 11)
)
apIcmpTableFullEvent.setObjects(
    ("DDOSSECURE4-MIB", "apIcmpTableFullFlag")
)
if mibBuilder.loadTexts:
    apIcmpTableFullEvent.setStatus(
        "deprecated"
    )

apOtherIpTableFullEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 12)
)
apOtherIpTableFullEvent.setObjects(
    ("DDOSSECURE4-MIB", "apOtherIpTableFullFlag")
)
if mibBuilder.loadTexts:
    apOtherIpTableFullEvent.setStatus(
        "deprecated"
    )

apFragTableFullEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 13)
)
apFragTableFullEvent.setObjects(
    ("DDOSSECURE4-MIB", "apFragTableFullFlag")
)
if mibBuilder.loadTexts:
    apFragTableFullEvent.setStatus(
        "deprecated"
    )

apFtpTableFullEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 14)
)
apFtpTableFullEvent.setObjects(
    ("DDOSSECURE4-MIB", "apFtpTableFullFlag")
)
if mibBuilder.loadTexts:
    apFtpTableFullEvent.setStatus(
        "deprecated"
    )

apBlockedTableFullEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 15)
)
apBlockedTableFullEvent.setObjects(
    ("DDOSSECURE4-MIB", "apBlockedTableFullFlag")
)
if mibBuilder.loadTexts:
    apBlockedTableFullEvent.setStatus(
        "deprecated"
    )

apShortCircuitEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 16)
)
apShortCircuitEvent.setObjects(
    ("DDOSSECURE4-MIB", "apShortCircuitFlag")
)
if mibBuilder.loadTexts:
    apShortCircuitEvent.setStatus(
        "deprecated"
    )

apInternetIfDisconnectedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 17)
)
apInternetIfDisconnectedEvent.setObjects(
    ("DDOSSECURE4-MIB", "apInternetIfDisconnectedFlag")
)
if mibBuilder.loadTexts:
    apInternetIfDisconnectedEvent.setStatus(
        "deprecated"
    )

apProtectedIfDisconnectedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 18)
)
apProtectedIfDisconnectedEvent.setObjects(
    ("DDOSSECURE4-MIB", "apProtectedIfDisconnectedFlag")
)
if mibBuilder.loadTexts:
    apProtectedIfDisconnectedEvent.setStatus(
        "deprecated"
    )

apMgmtIfDisconnectedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 19)
)
apMgmtIfDisconnectedEvent.setObjects(
    ("DDOSSECURE4-MIB", "apMgmtIfDisconnectedFlag")
)
if mibBuilder.loadTexts:
    apMgmtIfDisconnectedEvent.setStatus(
        "deprecated"
    )

apUpgradingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 20)
)
apUpgradingEvent.setObjects(
    ("DDOSSECURE4-MIB", "apUpgradingFlag")
)
if mibBuilder.loadTexts:
    apUpgradingEvent.setStatus(
        "deprecated"
    )

apProtectedIfTrafficEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 21)
)
apProtectedIfTrafficEvent.setObjects(
    ("DDOSSECURE4-MIB", "apProtectedIfTrafficFlag")
)
if mibBuilder.loadTexts:
    apProtectedIfTrafficEvent.setStatus(
        "deprecated"
    )

apRoutingLoopEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 22)
)
apRoutingLoopEvent.setObjects(
    ("DDOSSECURE4-MIB", "apRoutingLoopFlag")
)
if mibBuilder.loadTexts:
    apRoutingLoopEvent.setStatus(
        "deprecated"
    )

apOfflineEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 23)
)
apOfflineEvent.setObjects(
    ("DDOSSECURE4-MIB", "apOfflineFlag")
)
if mibBuilder.loadTexts:
    apOfflineEvent.setStatus(
        "deprecated"
    )

apStateLearningEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 24)
)
apStateLearningEvent.setObjects(
    ("DDOSSECURE4-MIB", "apStateLearningFlag")
)
if mibBuilder.loadTexts:
    apStateLearningEvent.setStatus(
        "deprecated"
    )

apSupportExpiredEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 25)
)
apSupportExpiredEvent.setObjects(
    ("DDOSSECURE4-MIB", "apSupportExpiredFlag")
)
if mibBuilder.loadTexts:
    apSupportExpiredEvent.setStatus(
        "deprecated"
    )

apSevereLoadingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 26)
)
apSevereLoadingEvent.setObjects(
    ("DDOSSECURE4-MIB", "apSevereLoadingFlag")
)
if mibBuilder.loadTexts:
    apSevereLoadingEvent.setStatus(
        "deprecated"
    )

apMacMisconfiguredEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 27)
)
apMacMisconfiguredEvent.setObjects(
    ("DDOSSECURE4-MIB", "apMacMisconfiguredFlag")
)
if mibBuilder.loadTexts:
    apMacMisconfiguredEvent.setStatus(
        "deprecated"
    )

apIfMisconfiguredEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 28)
)
apIfMisconfiguredEvent.setObjects(
    ("DDOSSECURE4-MIB", "apIfMisconfiguredFlag")
)
if mibBuilder.loadTexts:
    apIfMisconfiguredEvent.setStatus(
        "deprecated"
    )

apInternetIfLinkDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 29)
)
apInternetIfLinkDownEvent.setObjects(
    ("DDOSSECURE4-MIB", "apInternetIfLinkDownFlag")
)
if mibBuilder.loadTexts:
    apInternetIfLinkDownEvent.setStatus(
        "deprecated"
    )

apProtectedIfLinkDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 30)
)
apProtectedIfLinkDownEvent.setObjects(
    ("DDOSSECURE4-MIB", "apProtectedIfLinkDownFlag")
)
if mibBuilder.loadTexts:
    apProtectedIfLinkDownEvent.setStatus(
        "deprecated"
    )

apDatashareIfDisconnectedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 31)
)
apDatashareIfDisconnectedEvent.setObjects(
    ("DDOSSECURE4-MIB", "apDatashareIfDisconnectedFlag")
)
if mibBuilder.loadTexts:
    apDatashareIfDisconnectedEvent.setStatus(
        "deprecated"
    )

apHaStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 35)
)
apHaStateEvent.setObjects(
    ("DDOSSECURE4-MIB", "apHaState")
)
if mibBuilder.loadTexts:
    apHaStateEvent.setStatus(
        "deprecated"
    )

prBandwidthEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 40)
)
prBandwidthEvent.setObjects(
    ("DDOSSECURE4-MIB", "prBandwidth")
)
if mibBuilder.loadTexts:
    prBandwidthEvent.setStatus(
        "deprecated"
    )

prFloodEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 41)
)
prFloodEvent.setObjects(
    ("DDOSSECURE4-MIB", "prFlood")
)
if mibBuilder.loadTexts:
    prFloodEvent.setStatus(
        "deprecated"
    )

prBlockedProtocolEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 42)
)
prBlockedProtocolEvent.setObjects(
    ("DDOSSECURE4-MIB", "prBlockedProtocol")
)
if mibBuilder.loadTexts:
    prBlockedProtocolEvent.setStatus(
        "deprecated"
    )

prBlockedStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 43)
)
prBlockedStateEvent.setObjects(
    ("DDOSSECURE4-MIB", "prBlockedState")
)
if mibBuilder.loadTexts:
    prBlockedStateEvent.setStatus(
        "deprecated"
    )

prIpAttackEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 44)
)
prIpAttackEvent.setObjects(
    ("DDOSSECURE4-MIB", "prIpAttack")
)
if mibBuilder.loadTexts:
    prIpAttackEvent.setStatus(
        "deprecated"
    )

prTcpAttackEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 45)
)
prTcpAttackEvent.setObjects(
    ("DDOSSECURE4-MIB", "prTcpAttack")
)
if mibBuilder.loadTexts:
    prTcpAttackEvent.setStatus(
        "deprecated"
    )

prUdpAttackEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 46)
)
prUdpAttackEvent.setObjects(
    ("DDOSSECURE4-MIB", "prUdpAttack")
)
if mibBuilder.loadTexts:
    prUdpAttackEvent.setStatus(
        "deprecated"
    )

prIcmpAttackEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 47)
)
prIcmpAttackEvent.setObjects(
    ("DDOSSECURE4-MIB", "prIcmpAttack")
)
if mibBuilder.loadTexts:
    prIcmpAttackEvent.setStatus(
        "deprecated"
    )

prOtherIpAttackEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 48)
)
prOtherIpAttackEvent.setObjects(
    ("DDOSSECURE4-MIB", "prOtherIpAttack")
)
if mibBuilder.loadTexts:
    prOtherIpAttackEvent.setStatus(
        "deprecated"
    )

prFragAttackEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 49)
)
prFragAttackEvent.setObjects(
    ("DDOSSECURE4-MIB", "prFragAttack")
)
if mibBuilder.loadTexts:
    prFragAttackEvent.setStatus(
        "deprecated"
    )

prBadIpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 50)
)
prBadIpEvent.setObjects(
    ("DDOSSECURE4-MIB", "prBadIp")
)
if mibBuilder.loadTexts:
    prBadIpEvent.setStatus(
        "deprecated"
    )

prBadTcpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 51)
)
prBadTcpEvent.setObjects(
    ("DDOSSECURE4-MIB", "prBadTcp")
)
if mibBuilder.loadTexts:
    prBadTcpEvent.setStatus(
        "deprecated"
    )

prBadUdpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 52)
)
prBadUdpEvent.setObjects(
    ("DDOSSECURE4-MIB", "prBadUdp")
)
if mibBuilder.loadTexts:
    prBadUdpEvent.setStatus(
        "deprecated"
    )

prBadIcmpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 53)
)
prBadIcmpEvent.setObjects(
    ("DDOSSECURE4-MIB", "prBadIcmp")
)
if mibBuilder.loadTexts:
    prBadIcmpEvent.setStatus(
        "deprecated"
    )

prBadOtherIpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 54)
)
prBadOtherIpEvent.setObjects(
    ("DDOSSECURE4-MIB", "prBadOtherIp")
)
if mibBuilder.loadTexts:
    prBadOtherIpEvent.setStatus(
        "deprecated"
    )

prOverloadedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 55)
)
prOverloadedEvent.setObjects(
    ("DDOSSECURE4-MIB", "prOverloaded")
)
if mibBuilder.loadTexts:
    prOverloadedEvent.setStatus(
        "deprecated"
    )

prBandwidthOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1011)
)
prBandwidthOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBandwidth"))
)
if mibBuilder.loadTexts:
    prBandwidthOn.setStatus(
        "current"
    )

prBandwidthOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1012)
)
prBandwidthOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBandwidth"))
)
if mibBuilder.loadTexts:
    prBandwidthOff.setStatus(
        "current"
    )

prFloodOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1021)
)
prFloodOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFlood"))
)
if mibBuilder.loadTexts:
    prFloodOn.setStatus(
        "current"
    )

prFloodOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1022)
)
prFloodOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFlood"))
)
if mibBuilder.loadTexts:
    prFloodOff.setStatus(
        "current"
    )

prBlockedProtocolOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1031)
)
prBlockedProtocolOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolOn.setStatus(
        "current"
    )

prBlockedProtocolOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1032)
)
prBlockedProtocolOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolOff.setStatus(
        "current"
    )

prBlockedStateOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1041)
)
prBlockedStateOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedState"))
)
if mibBuilder.loadTexts:
    prBlockedStateOn.setStatus(
        "current"
    )

prBlockedStateOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1042)
)
prBlockedStateOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedState"))
)
if mibBuilder.loadTexts:
    prBlockedStateOff.setStatus(
        "current"
    )

prIpAttackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1051)
)
prIpAttackOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prIpAttack"))
)
if mibBuilder.loadTexts:
    prIpAttackOn.setStatus(
        "current"
    )

prIpAttackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1052)
)
prIpAttackOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prIpAttack"))
)
if mibBuilder.loadTexts:
    prIpAttackOff.setStatus(
        "current"
    )

prTcpAttackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1061)
)
prTcpAttackOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackOn.setStatus(
        "current"
    )

prTcpAttackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1062)
)
prTcpAttackOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackOff.setStatus(
        "current"
    )

prUdpAttackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1071)
)
prUdpAttackOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prUdpAttack"))
)
if mibBuilder.loadTexts:
    prUdpAttackOn.setStatus(
        "current"
    )

prUdpAttackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1072)
)
prUdpAttackOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prUdpAttack"))
)
if mibBuilder.loadTexts:
    prUdpAttackOff.setStatus(
        "current"
    )

prIcmpAttackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1081)
)
prIcmpAttackOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prIcmpAttack"))
)
if mibBuilder.loadTexts:
    prIcmpAttackOn.setStatus(
        "current"
    )

prIcmpAttackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1082)
)
prIcmpAttackOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prIcmpAttack"))
)
if mibBuilder.loadTexts:
    prIcmpAttackOff.setStatus(
        "current"
    )

prOtherIpAttackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1091)
)
prOtherIpAttackOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prOtherIpAttack"))
)
if mibBuilder.loadTexts:
    prOtherIpAttackOn.setStatus(
        "current"
    )

prOtherIpAttackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1092)
)
prOtherIpAttackOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prOtherIpAttack"))
)
if mibBuilder.loadTexts:
    prOtherIpAttackOff.setStatus(
        "current"
    )

prFragAttackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1101)
)
prFragAttackOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFragAttack"))
)
if mibBuilder.loadTexts:
    prFragAttackOn.setStatus(
        "current"
    )

prFragAttackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1102)
)
prFragAttackOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFragAttack"))
)
if mibBuilder.loadTexts:
    prFragAttackOff.setStatus(
        "current"
    )

prBadIpOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1111)
)
prBadIpOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadIp"))
)
if mibBuilder.loadTexts:
    prBadIpOn.setStatus(
        "current"
    )

prBadIpOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1112)
)
prBadIpOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadIp"))
)
if mibBuilder.loadTexts:
    prBadIpOff.setStatus(
        "current"
    )

prBadTcpOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1121)
)
prBadTcpOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadTcp"))
)
if mibBuilder.loadTexts:
    prBadTcpOn.setStatus(
        "current"
    )

prBadTcpOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1122)
)
prBadTcpOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadTcp"))
)
if mibBuilder.loadTexts:
    prBadTcpOff.setStatus(
        "current"
    )

prBadUdpOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1131)
)
prBadUdpOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadUdp"))
)
if mibBuilder.loadTexts:
    prBadUdpOn.setStatus(
        "current"
    )

prBadUdpOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1132)
)
prBadUdpOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadUdp"))
)
if mibBuilder.loadTexts:
    prBadUdpOff.setStatus(
        "current"
    )

prBadIcmpOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1141)
)
prBadIcmpOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadIcmp"))
)
if mibBuilder.loadTexts:
    prBadIcmpOn.setStatus(
        "current"
    )

prBadIcmpOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1142)
)
prBadIcmpOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadIcmp"))
)
if mibBuilder.loadTexts:
    prBadIcmpOff.setStatus(
        "current"
    )

prBadOtherIpOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1151)
)
prBadOtherIpOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadOtherIp"))
)
if mibBuilder.loadTexts:
    prBadOtherIpOn.setStatus(
        "current"
    )

prBadOtherIpOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1152)
)
prBadOtherIpOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadOtherIp"))
)
if mibBuilder.loadTexts:
    prBadOtherIpOff.setStatus(
        "current"
    )

prOverloadedOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1161)
)
prOverloadedOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prOverloaded"))
)
if mibBuilder.loadTexts:
    prOverloadedOn.setStatus(
        "current"
    )

prOverloadedOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 1162)
)
prOverloadedOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prOverloaded"))
)
if mibBuilder.loadTexts:
    prOverloadedOff.setStatus(
        "current"
    )

apHaStateMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2000)
)
apHaStateMode.setObjects(
    ("DDOSSECURE4-MIB", "apHaState")
)
if mibBuilder.loadTexts:
    apHaStateMode.setStatus(
        "current"
    )

prBandwidthLimitOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2011)
)
prBandwidthLimitOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBandwidth"))
)
if mibBuilder.loadTexts:
    prBandwidthLimitOn.setStatus(
        "current"
    )

prBandwidthLimitOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2012)
)
prBandwidthLimitOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBandwidth"))
)
if mibBuilder.loadTexts:
    prBandwidthLimitOff.setStatus(
        "current"
    )

prPacketLimitOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2021)
)
prPacketLimitOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFlood"))
)
if mibBuilder.loadTexts:
    prPacketLimitOn.setStatus(
        "current"
    )

prPacketLimitOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2022)
)
prPacketLimitOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFlood"))
)
if mibBuilder.loadTexts:
    prPacketLimitOff.setStatus(
        "current"
    )

prBlockedProtocolBlackListIpOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2031)
)
prBlockedProtocolBlackListIpOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolBlackListIpOn.setStatus(
        "current"
    )

prBlockedProtocolBlackListIpOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2032)
)
prBlockedProtocolBlackListIpOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolBlackListIpOff.setStatus(
        "current"
    )

prBlockedProtocolIcmpTypeOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2041)
)
prBlockedProtocolIcmpTypeOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolIcmpTypeOn.setStatus(
        "current"
    )

prBlockedProtocolIcmpTypeOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2042)
)
prBlockedProtocolIcmpTypeOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolIcmpTypeOff.setStatus(
        "current"
    )

prBlockedProtocolPortOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2051)
)
prBlockedProtocolPortOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolPortOn.setStatus(
        "current"
    )

prBlockedProtocolPortOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2052)
)
prBlockedProtocolPortOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolPortOff.setStatus(
        "current"
    )

prBlockedProtocolOtherOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2061)
)
prBlockedProtocolOtherOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolOtherOn.setStatus(
        "current"
    )

prBlockedProtocolOtherOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2062)
)
prBlockedProtocolOtherOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolOtherOff.setStatus(
        "current"
    )

prUnknownSessionIcmpRespOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2081)
)
prUnknownSessionIcmpRespOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedState"))
)
if mibBuilder.loadTexts:
    prUnknownSessionIcmpRespOn.setStatus(
        "current"
    )

prUnknownSessionIcmpRespOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2082)
)
prUnknownSessionIcmpRespOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedState"))
)
if mibBuilder.loadTexts:
    prUnknownSessionIcmpRespOff.setStatus(
        "current"
    )

prUnknownSessionIcmpDiagRespOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2091)
)
prUnknownSessionIcmpDiagRespOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedState"))
)
if mibBuilder.loadTexts:
    prUnknownSessionIcmpDiagRespOn.setStatus(
        "current"
    )

prUnknownSessionIcmpDiagRespOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2092)
)
prUnknownSessionIcmpDiagRespOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedState"))
)
if mibBuilder.loadTexts:
    prUnknownSessionIcmpDiagRespOff.setStatus(
        "current"
    )

prUnknownSessionNoStateOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2101)
)
prUnknownSessionNoStateOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedState"))
)
if mibBuilder.loadTexts:
    prUnknownSessionNoStateOn.setStatus(
        "current"
    )

prUnknownSessionNoStateOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2102)
)
prUnknownSessionNoStateOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedState"))
)
if mibBuilder.loadTexts:
    prUnknownSessionNoStateOff.setStatus(
        "current"
    )

prUnknownSessionInvalidStateOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2111)
)
prUnknownSessionInvalidStateOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedState"))
)
if mibBuilder.loadTexts:
    prUnknownSessionInvalidStateOn.setStatus(
        "current"
    )

prUnknownSessionInvalidStateOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2112)
)
prUnknownSessionInvalidStateOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedState"))
)
if mibBuilder.loadTexts:
    prUnknownSessionInvalidStateOff.setStatus(
        "current"
    )

prTcpAttackRstOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2121)
)
prTcpAttackRstOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackRstOn.setStatus(
        "current"
    )

prTcpAttackRstOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2122)
)
prTcpAttackRstOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackRstOff.setStatus(
        "current"
    )

prIpAttackLandOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2131)
)
prIpAttackLandOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prIpAttack"))
)
if mibBuilder.loadTexts:
    prIpAttackLandOn.setStatus(
        "current"
    )

prIpAttackLandOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2132)
)
prIpAttackLandOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prIpAttack"))
)
if mibBuilder.loadTexts:
    prIpAttackLandOff.setStatus(
        "current"
    )

prTcpAttackSynAckToOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2141)
)
prTcpAttackSynAckToOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackSynAckToOn.setStatus(
        "current"
    )

prTcpAttackSynAckToOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2142)
)
prTcpAttackSynAckToOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackSynAckToOff.setStatus(
        "current"
    )

prBlockedProtocolCountryOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2151)
)
prBlockedProtocolCountryOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolCountryOn.setStatus(
        "current"
    )

prBlockedProtocolCountryOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2152)
)
prBlockedProtocolCountryOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolCountryOff.setStatus(
        "current"
    )

prTcpAttackSynFloodOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2161)
)
prTcpAttackSynFloodOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackSynFloodOn.setStatus(
        "current"
    )

prTcpAttackSynFloodOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2162)
)
prTcpAttackSynFloodOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackSynFloodOff.setStatus(
        "current"
    )

prTcpAttackConnFloodOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2171)
)
prTcpAttackConnFloodOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackConnFloodOn.setStatus(
        "current"
    )

prTcpAttackConnFloodOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2172)
)
prTcpAttackConnFloodOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackConnFloodOff.setStatus(
        "current"
    )

prTcpAttackTableFullOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2181)
)
prTcpAttackTableFullOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackTableFullOn.setStatus(
        "current"
    )

prTcpAttackTableFullOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2182)
)
prTcpAttackTableFullOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackTableFullOff.setStatus(
        "current"
    )

prBadTcpFastAckOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2191)
)
prBadTcpFastAckOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadTcp"))
)
if mibBuilder.loadTexts:
    prBadTcpFastAckOn.setStatus(
        "current"
    )

prBadTcpFastAckOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2192)
)
prBadTcpFastAckOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadTcp"))
)
if mibBuilder.loadTexts:
    prBadTcpFastAckOff.setStatus(
        "current"
    )

prTcpAttackHttpFloodOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2201)
)
prTcpAttackHttpFloodOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackHttpFloodOn.setStatus(
        "current"
    )

prTcpAttackHttpFloodOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2202)
)
prTcpAttackHttpFloodOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackHttpFloodOff.setStatus(
        "current"
    )

prUdpAttackTableFullOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2211)
)
prUdpAttackTableFullOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prUdpAttack"))
)
if mibBuilder.loadTexts:
    prUdpAttackTableFullOn.setStatus(
        "current"
    )

prUdpAttackTableFullOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2212)
)
prUdpAttackTableFullOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prUdpAttack"))
)
if mibBuilder.loadTexts:
    prUdpAttackTableFullOff.setStatus(
        "current"
    )

prTcpAttackHttpTimeoutOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2231)
)
prTcpAttackHttpTimeoutOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackHttpTimeoutOn.setStatus(
        "current"
    )

prTcpAttackHttpTimeoutOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2232)
)
prTcpAttackHttpTimeoutOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackHttpTimeoutOff.setStatus(
        "current"
    )

prIcmpAttackRepeatsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2241)
)
prIcmpAttackRepeatsOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prIcmpAttack"))
)
if mibBuilder.loadTexts:
    prIcmpAttackRepeatsOn.setStatus(
        "current"
    )

prIcmpAttackRepeatsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2242)
)
prIcmpAttackRepeatsOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prIcmpAttack"))
)
if mibBuilder.loadTexts:
    prIcmpAttackRepeatsOff.setStatus(
        "current"
    )

prIcmpAttackTableFullOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2251)
)
prIcmpAttackTableFullOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prIcmpAttack"))
)
if mibBuilder.loadTexts:
    prIcmpAttackTableFullOn.setStatus(
        "current"
    )

prIcmpAttackTableFullOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2252)
)
prIcmpAttackTableFullOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prIcmpAttack"))
)
if mibBuilder.loadTexts:
    prIcmpAttackTableFullOff.setStatus(
        "current"
    )

prOtherIpAttackTableFullOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2271)
)
prOtherIpAttackTableFullOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prOtherIpAttack"))
)
if mibBuilder.loadTexts:
    prOtherIpAttackTableFullOn.setStatus(
        "current"
    )

prOtherIpAttackTableFullOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2272)
)
prOtherIpAttackTableFullOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prOtherIpAttack"))
)
if mibBuilder.loadTexts:
    prOtherIpAttackTableFullOff.setStatus(
        "current"
    )

prFragAttackPingOfDeathOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2291)
)
prFragAttackPingOfDeathOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFragAttack"))
)
if mibBuilder.loadTexts:
    prFragAttackPingOfDeathOn.setStatus(
        "current"
    )

prFragAttackPingOfDeathOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2292)
)
prFragAttackPingOfDeathOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFragAttack"))
)
if mibBuilder.loadTexts:
    prFragAttackPingOfDeathOff.setStatus(
        "current"
    )

prFragAttackHeadOverlayOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2301)
)
prFragAttackHeadOverlayOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFragAttack"))
)
if mibBuilder.loadTexts:
    prFragAttackHeadOverlayOn.setStatus(
        "current"
    )

prFragAttackHeadOverlayOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2302)
)
prFragAttackHeadOverlayOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFragAttack"))
)
if mibBuilder.loadTexts:
    prFragAttackHeadOverlayOff.setStatus(
        "current"
    )

prFragAttackTableFullOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2311)
)
prFragAttackTableFullOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFragAttack"))
)
if mibBuilder.loadTexts:
    prFragAttackTableFullOn.setStatus(
        "current"
    )

prFragAttackTableFullOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2312)
)
prFragAttackTableFullOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFragAttack"))
)
if mibBuilder.loadTexts:
    prFragAttackTableFullOff.setStatus(
        "current"
    )

prFragAttackSmallSizeOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2321)
)
prFragAttackSmallSizeOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFragAttack"))
)
if mibBuilder.loadTexts:
    prFragAttackSmallSizeOn.setStatus(
        "current"
    )

prFragAttackSmallSizeOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2322)
)
prFragAttackSmallSizeOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFragAttack"))
)
if mibBuilder.loadTexts:
    prFragAttackSmallSizeOff.setStatus(
        "current"
    )

prFragAttackNoFragsAllowedOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2331)
)
prFragAttackNoFragsAllowedOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFragAttack"))
)
if mibBuilder.loadTexts:
    prFragAttackNoFragsAllowedOn.setStatus(
        "current"
    )

prFragAttackNoFragsAllowedOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2332)
)
prFragAttackNoFragsAllowedOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFragAttack"))
)
if mibBuilder.loadTexts:
    prFragAttackNoFragsAllowedOff.setStatus(
        "current"
    )

prBadIpSrcAddrOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2341)
)
prBadIpSrcAddrOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadIp"))
)
if mibBuilder.loadTexts:
    prBadIpSrcAddrOn.setStatus(
        "current"
    )

prBadIpSrcAddrOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2342)
)
prBadIpSrcAddrOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadIp"))
)
if mibBuilder.loadTexts:
    prBadIpSrcAddrOff.setStatus(
        "current"
    )

prBadIpHeaderOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2351)
)
prBadIpHeaderOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadIp"))
)
if mibBuilder.loadTexts:
    prBadIpHeaderOn.setStatus(
        "current"
    )

prBadIpHeaderOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2352)
)
prBadIpHeaderOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadIp"))
)
if mibBuilder.loadTexts:
    prBadIpHeaderOff.setStatus(
        "current"
    )

prBadIpOptionOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2361)
)
prBadIpOptionOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadIp"))
)
if mibBuilder.loadTexts:
    prBadIpOptionOn.setStatus(
        "current"
    )

prBadIpOptionOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2362)
)
prBadIpOptionOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadIp"))
)
if mibBuilder.loadTexts:
    prBadIpOptionOff.setStatus(
        "current"
    )

prBadIpSizeOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2371)
)
prBadIpSizeOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadIp"))
)
if mibBuilder.loadTexts:
    prBadIpSizeOn.setStatus(
        "current"
    )

prBadIpSizeOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2372)
)
prBadIpSizeOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadIp"))
)
if mibBuilder.loadTexts:
    prBadIpSizeOff.setStatus(
        "current"
    )

prBlockedProtocolTmpBlackListOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2381)
)
prBlockedProtocolTmpBlackListOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolTmpBlackListOn.setStatus(
        "current"
    )

prBlockedProtocolTmpBlackListOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2382)
)
prBlockedProtocolTmpBlackListOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolTmpBlackListOff.setStatus(
        "current"
    )

prBadTcpFlagsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2391)
)
prBadTcpFlagsOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadTcp"))
)
if mibBuilder.loadTexts:
    prBadTcpFlagsOn.setStatus(
        "current"
    )

prBadTcpFlagsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2392)
)
prBadTcpFlagsOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadTcp"))
)
if mibBuilder.loadTexts:
    prBadTcpFlagsOff.setStatus(
        "current"
    )

prBadTcpMalformedOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2401)
)
prBadTcpMalformedOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadTcp"))
)
if mibBuilder.loadTexts:
    prBadTcpMalformedOn.setStatus(
        "current"
    )

prBadTcpMalformedOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2402)
)
prBadTcpMalformedOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadTcp"))
)
if mibBuilder.loadTexts:
    prBadTcpMalformedOff.setStatus(
        "current"
    )

prBadTcpOptionOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2411)
)
prBadTcpOptionOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadTcp"))
)
if mibBuilder.loadTexts:
    prBadTcpOptionOn.setStatus(
        "current"
    )

prBadTcpOptionOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2412)
)
prBadTcpOptionOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadTcp"))
)
if mibBuilder.loadTexts:
    prBadTcpOptionOff.setStatus(
        "current"
    )

prBlockedProtocolDnsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2421)
)
prBlockedProtocolDnsOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolDnsOn.setStatus(
        "current"
    )

prBlockedProtocolDnsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2422)
)
prBlockedProtocolDnsOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolDnsOff.setStatus(
        "current"
    )

prBadUdpNoDataOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2431)
)
prBadUdpNoDataOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadUdp"))
)
if mibBuilder.loadTexts:
    prBadUdpNoDataOn.setStatus(
        "current"
    )

prBadUdpNoDataOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2432)
)
prBadUdpNoDataOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadUdp"))
)
if mibBuilder.loadTexts:
    prBadUdpNoDataOff.setStatus(
        "current"
    )

prBadUdpMalformedOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2441)
)
prBadUdpMalformedOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadUdp"))
)
if mibBuilder.loadTexts:
    prBadUdpMalformedOn.setStatus(
        "current"
    )

prBadUdpMalformedOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2442)
)
prBadUdpMalformedOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadUdp"))
)
if mibBuilder.loadTexts:
    prBadUdpMalformedOff.setStatus(
        "current"
    )

prBlockedProtocolAsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2451)
)
prBlockedProtocolAsOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolAsOn.setStatus(
        "current"
    )

prBlockedProtocolAsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2452)
)
prBlockedProtocolAsOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolAsOff.setStatus(
        "current"
    )

ptTcpAttackHttpRateFloodOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2461)
)
ptTcpAttackHttpRateFloodOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    ptTcpAttackHttpRateFloodOn.setStatus(
        "current"
    )

ptTcpAttackHttpRateFloodOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2462)
)
ptTcpAttackHttpRateFloodOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    ptTcpAttackHttpRateFloodOff.setStatus(
        "current"
    )

prBadIcmpMalformedOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2471)
)
prBadIcmpMalformedOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadIcmp"))
)
if mibBuilder.loadTexts:
    prBadIcmpMalformedOn.setStatus(
        "current"
    )

prBadIcmpMalformedOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2472)
)
prBadIcmpMalformedOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadIcmp"))
)
if mibBuilder.loadTexts:
    prBadIcmpMalformedOff.setStatus(
        "current"
    )

prBlockedProtocolUrlOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2481)
)
prBlockedProtocolUrlOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolUrlOn.setStatus(
        "current"
    )

prBlockedProtocolUrlOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2482)
)
prBlockedProtocolUrlOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolUrlOff.setStatus(
        "current"
    )

prBadOtherIpProtocolOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2501)
)
prBadOtherIpProtocolOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadOtherIp"))
)
if mibBuilder.loadTexts:
    prBadOtherIpProtocolOn.setStatus(
        "current"
    )

prBadOtherIpProtocolOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2502)
)
prBadOtherIpProtocolOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadOtherIp"))
)
if mibBuilder.loadTexts:
    prBadOtherIpProtocolOff.setStatus(
        "current"
    )

prBadOtherIpLengthOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2511)
)
prBadOtherIpLengthOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadOtherIp"))
)
if mibBuilder.loadTexts:
    prBadOtherIpLengthOn.setStatus(
        "current"
    )

prBadOtherIpLengthOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2512)
)
prBadOtherIpLengthOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadOtherIp"))
)
if mibBuilder.loadTexts:
    prBadOtherIpLengthOff.setStatus(
        "current"
    )

prTcpAttackHttpIncompleteOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2521)
)
prTcpAttackHttpIncompleteOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadOtherIp"))
)
if mibBuilder.loadTexts:
    prTcpAttackHttpIncompleteOn.setStatus(
        "current"
    )

prTcpAttackHttpIncompleteOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2522)
)
prTcpAttackHttpIncompleteOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadOtherIp"))
)
if mibBuilder.loadTexts:
    prTcpAttackHttpIncompleteOff.setStatus(
        "current"
    )

prOverloadedStallOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2531)
)
prOverloadedStallOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prOverloaded"))
)
if mibBuilder.loadTexts:
    prOverloadedStallOn.setStatus(
        "current"
    )

prOverloadedStallOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2532)
)
prOverloadedStallOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prOverloaded"))
)
if mibBuilder.loadTexts:
    prOverloadedStallOff.setStatus(
        "current"
    )

prFragAttackTimeOutOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2541)
)
prFragAttackTimeOutOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFragAttack"))
)
if mibBuilder.loadTexts:
    prFragAttackTimeOutOn.setStatus(
        "current"
    )

prFragAttackTimeOutOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2542)
)
prFragAttackTimeOutOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFragAttack"))
)
if mibBuilder.loadTexts:
    prFragAttackTimeOutOff.setStatus(
        "current"
    )

prFragAttackRepeatsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2551)
)
prFragAttackRepeatsOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFragAttack"))
)
if mibBuilder.loadTexts:
    prFragAttackRepeatsOn.setStatus(
        "current"
    )

prFragAttackRepeatsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2552)
)
prFragAttackRepeatsOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFragAttack"))
)
if mibBuilder.loadTexts:
    prFragAttackRepeatsOff.setStatus(
        "current"
    )

prFragAttackBadLengthOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2561)
)
prFragAttackBadLengthOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFragAttack"))
)
if mibBuilder.loadTexts:
    prFragAttackBadLengthOn.setStatus(
        "current"
    )

prFragAttackBadLengthOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2562)
)
prFragAttackBadLengthOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prFragAttack"))
)
if mibBuilder.loadTexts:
    prFragAttackBadLengthOff.setStatus(
        "current"
    )

prOverloadedBacklogOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2681)
)
prOverloadedBacklogOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prOverloaded"))
)
if mibBuilder.loadTexts:
    prOverloadedBacklogOn.setStatus(
        "current"
    )

prOverloadedBacklogOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2682)
)
prOverloadedBacklogOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prOverloaded"))
)
if mibBuilder.loadTexts:
    prOverloadedBacklogOff.setStatus(
        "current"
    )

prBlockedProtocolAddressOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2691)
)
prBlockedProtocolAddressOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolAddressOn.setStatus(
        "current"
    )

prBlockedProtocolAddressOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2692)
)
prBlockedProtocolAddressOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolAddressOff.setStatus(
        "current"
    )

prTcpAttackNoDataOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2701)
)
prTcpAttackNoDataOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackNoDataOn.setStatus(
        "current"
    )

prTcpAttackNoDataOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2702)
)
prTcpAttackNoDataOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackNoDataOff.setStatus(
        "current"
    )

prTcpAttackNoServerDataOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2711)
)
prTcpAttackNoServerDataOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackNoServerDataOn.setStatus(
        "current"
    )

prTcpAttackNoServerDataOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2712)
)
prTcpAttackNoServerDataOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackNoServerDataOff.setStatus(
        "current"
    )

prTcpAttackConnRateFloodOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2721)
)
prTcpAttackConnRateFloodOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackConnRateFloodOn.setStatus(
        "current"
    )

prTcpAttackConnRateFloodOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2722)
)
prTcpAttackConnRateFloodOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackConnRateFloodOff.setStatus(
        "current"
    )

prOverloadedThreadsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2731)
)
prOverloadedThreadsOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prOverloaded"))
)
if mibBuilder.loadTexts:
    prOverloadedThreadsOn.setStatus(
        "current"
    )

prOverloadedThreadsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2732)
)
prOverloadedThreadsOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prOverloaded"))
)
if mibBuilder.loadTexts:
    prOverloadedThreadsOff.setStatus(
        "current"
    )

prBadIpReflectedRouteOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2741)
)
prBadIpReflectedRouteOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadIp"))
)
if mibBuilder.loadTexts:
    prBadIpReflectedRouteOn.setStatus(
        "current"
    )

prBadIpReflectedRouteOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2742)
)
prBadIpReflectedRouteOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadIp"))
)
if mibBuilder.loadTexts:
    prBadIpReflectedRouteOff.setStatus(
        "current"
    )

prTcpAttackPortScanOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2771)
)
prTcpAttackPortScanOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackPortScanOn.setStatus(
        "current"
    )

prTcpAttackPortScanOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2772)
)
prTcpAttackPortScanOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackPortScanOff.setStatus(
        "current"
    )

prTcpAttackSmallWindowOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2781)
)
prTcpAttackSmallWindowOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackSmallWindowOn.setStatus(
        "current"
    )

prTcpAttackSmallWindowOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2782)
)
prTcpAttackSmallWindowOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackSmallWindowOff.setStatus(
        "current"
    )

prTcpAttackClientAbortOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2791)
)
prTcpAttackClientAbortOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackClientAbortOn.setStatus(
        "current"
    )

prTcpAttackClientAbortOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2792)
)
prTcpAttackClientAbortOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackClientAbortOff.setStatus(
        "current"
    )

prBlockedProtocolSipOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2811)
)
prBlockedProtocolSipOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolSipOn.setStatus(
        "current"
    )

prBlockedProtocolSipOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2812)
)
prBlockedProtocolSipOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedProtocol"))
)
if mibBuilder.loadTexts:
    prBlockedProtocolSipOff.setStatus(
        "current"
    )

prTcpAttackUrlRateLimitOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2821)
)
prTcpAttackUrlRateLimitOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackUrlRateLimitOn.setStatus(
        "current"
    )

prTcpAttackUrlRateLimitOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2822)
)
prTcpAttackUrlRateLimitOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackUrlRateLimitOff.setStatus(
        "current"
    )

prUdpAttackDnsRateLimitOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2831)
)
prUdpAttackDnsRateLimitOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prUdpAttack"))
)
if mibBuilder.loadTexts:
    prUdpAttackDnsRateLimitOn.setStatus(
        "current"
    )

prUdpAttackDnsRateLimitOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2832)
)
prUdpAttackDnsRateLimitOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prUdpAttack"))
)
if mibBuilder.loadTexts:
    prUdpAttackDnsRateLimitOff.setStatus(
        "current"
    )

prUdpAttackSipRateLimitOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2841)
)
prUdpAttackSipRateLimitOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prUdpAttack"))
)
if mibBuilder.loadTexts:
    prUdpAttackSipRateLimitOn.setStatus(
        "current"
    )

prUdpAttackSipRateLimitOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2842)
)
prUdpAttackSipRateLimitOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prUdpAttack"))
)
if mibBuilder.loadTexts:
    prUdpAttackSipRateLimitOff.setStatus(
        "current"
    )

prBadTcpChecksumOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2851)
)
prBadTcpChecksumOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadTcp"))
)
if mibBuilder.loadTexts:
    prBadTcpChecksumOn.setStatus(
        "current"
    )

prBadTcpChecksumOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2852)
)
prBadTcpChecksumOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadTcp"))
)
if mibBuilder.loadTexts:
    prBadTcpChecksumOff.setStatus(
        "current"
    )

prTcpAttackHttpFormatOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2861)
)
prTcpAttackHttpFormatOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prTcpAttack"))
)
if mibBuilder.loadTexts:
    prTcpAttackHttpFormatOn.setStatus(
        "current"
    )

prTcpAttackHttpFormatOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2862)
)
prTcpAttackHttpFormatOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBadTcp"))
)
if mibBuilder.loadTexts:
    prTcpAttackHttpFormatOff.setStatus(
        "current"
    )

prUnknownSessionReflectiveOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2871)
)
prUnknownSessionReflectiveOn.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedState"))
)
if mibBuilder.loadTexts:
    prUnknownSessionReflectiveOn.setStatus(
        "current"
    )

prUnknownSessionReflectiveOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 2872)
)
prUnknownSessionReflectiveOff.setObjects(
      *(("DDOSSECURE4-MIB", "prHostName"),
        ("DDOSSECURE4-MIB", "prBlockedState"))
)
if mibBuilder.loadTexts:
    prUnknownSessionReflectiveOff.setStatus(
        "current"
    )

apOutputErrorIIFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3011)
)
apOutputErrorIIFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apOutputErrorIIFlag")
)
if mibBuilder.loadTexts:
    apOutputErrorIIFlagOn.setStatus(
        "current"
    )

apOutputErrorIIFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3012)
)
apOutputErrorIIFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apOutputErrorIIFlag")
)
if mibBuilder.loadTexts:
    apOutputErrorIIFlagOff.setStatus(
        "current"
    )

apOutputErrorPIFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3021)
)
apOutputErrorPIFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apOutputErrorPIFlag")
)
if mibBuilder.loadTexts:
    apOutputErrorPIFlagOn.setStatus(
        "current"
    )

apOutputErrorPIFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3022)
)
apOutputErrorPIFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apOutputErrorPIFlag")
)
if mibBuilder.loadTexts:
    apOutputErrorPIFlagOff.setStatus(
        "current"
    )

apOutputErrorMIFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3031)
)
apOutputErrorMIFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apOutputErrorMIFlag")
)
if mibBuilder.loadTexts:
    apOutputErrorMIFlagOn.setStatus(
        "current"
    )

apOutputErrorMIFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3032)
)
apOutputErrorMIFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apOutputErrorMIFlag")
)
if mibBuilder.loadTexts:
    apOutputErrorMIFlagOff.setStatus(
        "current"
    )

apNewConfigFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3041)
)
apNewConfigFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apNewConfigFlag")
)
if mibBuilder.loadTexts:
    apNewConfigFlagOn.setStatus(
        "current"
    )

apNewConfigFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3042)
)
apNewConfigFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apNewConfigFlag")
)
if mibBuilder.loadTexts:
    apNewConfigFlagOff.setStatus(
        "current"
    )

apNotLicensedFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3051)
)
apNotLicensedFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apNotLicensedFlag")
)
if mibBuilder.loadTexts:
    apNotLicensedFlagOn.setStatus(
        "current"
    )

apNotLicensedFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3052)
)
apNotLicensedFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apNotLicensedFlag")
)
if mibBuilder.loadTexts:
    apNotLicensedFlagOff.setStatus(
        "current"
    )

apMacTableFullFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3061)
)
apMacTableFullFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apMacTableFullFlag")
)
if mibBuilder.loadTexts:
    apMacTableFullFlagOn.setStatus(
        "current"
    )

apMacTableFullFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3062)
)
apMacTableFullFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apMacTableFullFlag")
)
if mibBuilder.loadTexts:
    apMacTableFullFlagOff.setStatus(
        "current"
    )

apProtectedTableFullFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3071)
)
apProtectedTableFullFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apProtectedTableFullFlag")
)
if mibBuilder.loadTexts:
    apProtectedTableFullFlagOn.setStatus(
        "current"
    )

apProtectedTableFullFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3072)
)
apProtectedTableFullFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apProtectedTableFullFlag")
)
if mibBuilder.loadTexts:
    apProtectedTableFullFlagOff.setStatus(
        "current"
    )

apIncidentTableFullFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3081)
)
apIncidentTableFullFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apIncidentTableFullFlag")
)
if mibBuilder.loadTexts:
    apIncidentTableFullFlagOn.setStatus(
        "current"
    )

apIncidentTableFullFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3082)
)
apIncidentTableFullFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apIncidentTableFullFlag")
)
if mibBuilder.loadTexts:
    apIncidentTableFullFlagOff.setStatus(
        "current"
    )

apTcpTableFullFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3091)
)
apTcpTableFullFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apTcpTableFullFlag")
)
if mibBuilder.loadTexts:
    apTcpTableFullFlagOn.setStatus(
        "current"
    )

apTcpTableFullFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3092)
)
apTcpTableFullFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apTcpTableFullFlag")
)
if mibBuilder.loadTexts:
    apTcpTableFullFlagOff.setStatus(
        "current"
    )

apUdpTableFullFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3101)
)
apUdpTableFullFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apUdpTableFullFlag")
)
if mibBuilder.loadTexts:
    apUdpTableFullFlagOn.setStatus(
        "current"
    )

apUdpTableFullFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3102)
)
apUdpTableFullFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apUdpTableFullFlag")
)
if mibBuilder.loadTexts:
    apUdpTableFullFlagOff.setStatus(
        "current"
    )

apIcmpTableFullFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3111)
)
apIcmpTableFullFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apIcmpTableFullFlag")
)
if mibBuilder.loadTexts:
    apIcmpTableFullFlagOn.setStatus(
        "current"
    )

apIcmpTableFullFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3112)
)
apIcmpTableFullFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apIcmpTableFullFlag")
)
if mibBuilder.loadTexts:
    apIcmpTableFullFlagOff.setStatus(
        "current"
    )

apOtherIpTableFullFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3121)
)
apOtherIpTableFullFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apOtherIpTableFullFlag")
)
if mibBuilder.loadTexts:
    apOtherIpTableFullFlagOn.setStatus(
        "current"
    )

apOtherIpTableFullFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3122)
)
apOtherIpTableFullFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apOtherIpTableFullFlag")
)
if mibBuilder.loadTexts:
    apOtherIpTableFullFlagOff.setStatus(
        "current"
    )

apFragTableFullFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3131)
)
apFragTableFullFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apFragTableFullFlag")
)
if mibBuilder.loadTexts:
    apFragTableFullFlagOn.setStatus(
        "current"
    )

apFragTableFullFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3132)
)
apFragTableFullFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apFragTableFullFlag")
)
if mibBuilder.loadTexts:
    apFragTableFullFlagOff.setStatus(
        "current"
    )

apFtpTableFullFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3141)
)
apFtpTableFullFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apFtpTableFullFlag")
)
if mibBuilder.loadTexts:
    apFtpTableFullFlagOn.setStatus(
        "current"
    )

apFtpTableFullFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3142)
)
apFtpTableFullFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apFtpTableFullFlag")
)
if mibBuilder.loadTexts:
    apFtpTableFullFlagOff.setStatus(
        "current"
    )

apBlockedTableFullFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3151)
)
apBlockedTableFullFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apBlockedTableFullFlag")
)
if mibBuilder.loadTexts:
    apBlockedTableFullFlagOn.setStatus(
        "current"
    )

apBlockedTableFullFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3152)
)
apBlockedTableFullFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apBlockedTableFullFlag")
)
if mibBuilder.loadTexts:
    apBlockedTableFullFlagOff.setStatus(
        "current"
    )

apShortCircuitFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3161)
)
apShortCircuitFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apShortCircuitFlag")
)
if mibBuilder.loadTexts:
    apShortCircuitFlagOn.setStatus(
        "current"
    )

apShortCircuitFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3162)
)
apShortCircuitFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apShortCircuitFlag")
)
if mibBuilder.loadTexts:
    apShortCircuitFlagOff.setStatus(
        "current"
    )

apInternetIfDisconnectedFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3171)
)
apInternetIfDisconnectedFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apInternetIfDisconnectedFlag")
)
if mibBuilder.loadTexts:
    apInternetIfDisconnectedFlagOn.setStatus(
        "current"
    )

apInternetIfDisconnectedFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3172)
)
apInternetIfDisconnectedFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apInternetIfDisconnectedFlag")
)
if mibBuilder.loadTexts:
    apInternetIfDisconnectedFlagOff.setStatus(
        "current"
    )

apProtectedIfDisconnectedFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3181)
)
apProtectedIfDisconnectedFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apProtectedIfDisconnectedFlag")
)
if mibBuilder.loadTexts:
    apProtectedIfDisconnectedFlagOn.setStatus(
        "current"
    )

apProtectedIfDisconnectedFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3182)
)
apProtectedIfDisconnectedFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apProtectedIfDisconnectedFlag")
)
if mibBuilder.loadTexts:
    apProtectedIfDisconnectedFlagOff.setStatus(
        "current"
    )

apMgmtIfDisconnectedFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3191)
)
apMgmtIfDisconnectedFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apMgmtIfDisconnectedFlag")
)
if mibBuilder.loadTexts:
    apMgmtIfDisconnectedFlagOn.setStatus(
        "current"
    )

apMgmtIfDisconnectedFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3192)
)
apMgmtIfDisconnectedFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apMgmtIfDisconnectedFlag")
)
if mibBuilder.loadTexts:
    apMgmtIfDisconnectedFlagOff.setStatus(
        "current"
    )

apUpgradingFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3201)
)
apUpgradingFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apUpgradingFlag")
)
if mibBuilder.loadTexts:
    apUpgradingFlagOn.setStatus(
        "current"
    )

apUpgradingFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3202)
)
apUpgradingFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apUpgradingFlag")
)
if mibBuilder.loadTexts:
    apUpgradingFlagOff.setStatus(
        "current"
    )

apProtectedIfTrafficFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3211)
)
apProtectedIfTrafficFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apProtectedIfTrafficFlag")
)
if mibBuilder.loadTexts:
    apProtectedIfTrafficFlagOn.setStatus(
        "current"
    )

apProtectedIfTrafficFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3212)
)
apProtectedIfTrafficFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apProtectedIfTrafficFlag")
)
if mibBuilder.loadTexts:
    apProtectedIfTrafficFlagOff.setStatus(
        "current"
    )

apRoutingLoopFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3221)
)
apRoutingLoopFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apRoutingLoopFlag")
)
if mibBuilder.loadTexts:
    apRoutingLoopFlagOn.setStatus(
        "current"
    )

apRoutingLoopFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3222)
)
apRoutingLoopFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apRoutingLoopFlag")
)
if mibBuilder.loadTexts:
    apRoutingLoopFlagOff.setStatus(
        "current"
    )

apOfflineFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3231)
)
apOfflineFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apOfflineFlag")
)
if mibBuilder.loadTexts:
    apOfflineFlagOn.setStatus(
        "current"
    )

apOfflineFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3232)
)
apOfflineFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apOfflineFlag")
)
if mibBuilder.loadTexts:
    apOfflineFlagOff.setStatus(
        "current"
    )

apStateLearningFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3241)
)
apStateLearningFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apStateLearningFlag")
)
if mibBuilder.loadTexts:
    apStateLearningFlagOn.setStatus(
        "current"
    )

apStateLearningFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3242)
)
apStateLearningFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apStateLearningFlag")
)
if mibBuilder.loadTexts:
    apStateLearningFlagOff.setStatus(
        "current"
    )

apSupportExpiredFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3251)
)
apSupportExpiredFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apSupportExpiredFlag")
)
if mibBuilder.loadTexts:
    apSupportExpiredFlagOn.setStatus(
        "current"
    )

apSupportExpiredFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3252)
)
apSupportExpiredFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apSupportExpiredFlag")
)
if mibBuilder.loadTexts:
    apSupportExpiredFlagOff.setStatus(
        "current"
    )

apSevereLoadingFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3261)
)
apSevereLoadingFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apSevereLoadingFlag")
)
if mibBuilder.loadTexts:
    apSevereLoadingFlagOn.setStatus(
        "current"
    )

apSevereLoadingFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3262)
)
apSevereLoadingFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apSevereLoadingFlag")
)
if mibBuilder.loadTexts:
    apSevereLoadingFlagOff.setStatus(
        "current"
    )

apMacMisconfiguredFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3271)
)
apMacMisconfiguredFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apMacMisconfiguredFlag")
)
if mibBuilder.loadTexts:
    apMacMisconfiguredFlagOn.setStatus(
        "current"
    )

apMacMisconfiguredFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3272)
)
apMacMisconfiguredFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apMacMisconfiguredFlag")
)
if mibBuilder.loadTexts:
    apMacMisconfiguredFlagOff.setStatus(
        "current"
    )

apIfMisconfiguredFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3281)
)
apIfMisconfiguredFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apIfMisconfiguredFlag")
)
if mibBuilder.loadTexts:
    apIfMisconfiguredFlagOn.setStatus(
        "current"
    )

apIfMisconfiguredFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3282)
)
apIfMisconfiguredFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apIfMisconfiguredFlag")
)
if mibBuilder.loadTexts:
    apIfMisconfiguredFlagOff.setStatus(
        "current"
    )

apInternetIfLinkDownFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3291)
)
apInternetIfLinkDownFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apInternetIfLinkDownFlag")
)
if mibBuilder.loadTexts:
    apInternetIfLinkDownFlagOn.setStatus(
        "current"
    )

apInternetIfLinkDownFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3292)
)
apInternetIfLinkDownFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apInternetIfLinkDownFlag")
)
if mibBuilder.loadTexts:
    apInternetIfLinkDownFlagOff.setStatus(
        "current"
    )

apProtectedIfLinkDownFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3301)
)
apProtectedIfLinkDownFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apProtectedIfLinkDownFlag")
)
if mibBuilder.loadTexts:
    apProtectedIfLinkDownFlagOn.setStatus(
        "current"
    )

apProtectedIfLinkDownFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3302)
)
apProtectedIfLinkDownFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apProtectedIfLinkDownFlag")
)
if mibBuilder.loadTexts:
    apProtectedIfLinkDownFlagOff.setStatus(
        "current"
    )

apDatashareIfDisconnectedFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3311)
)
apDatashareIfDisconnectedFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apDatashareIfDisconnectedFlag")
)
if mibBuilder.loadTexts:
    apDatashareIfDisconnectedFlagOn.setStatus(
        "current"
    )

apDatashareIfDisconnectedFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3312)
)
apDatashareIfDisconnectedFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apDatashareIfDisconnectedFlag")
)
if mibBuilder.loadTexts:
    apDatashareIfDisconnectedFlagOff.setStatus(
        "current"
    )

apDiskFailingOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3321)
)
apDiskFailingOn.setObjects(
    ("DDOSSECURE4-MIB", "apDiskFailingFlag")
)
if mibBuilder.loadTexts:
    apDiskFailingOn.setStatus(
        "current"
    )

apDiskFailingOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3322)
)
apDiskFailingOff.setObjects(
    ("DDOSSECURE4-MIB", "apDiskFailingFlag")
)
if mibBuilder.loadTexts:
    apDiskFailingOff.setStatus(
        "current"
    )

apPsuFailingFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3331)
)
apPsuFailingFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apPsuFailingFlag")
)
if mibBuilder.loadTexts:
    apPsuFailingFlagOn.setStatus(
        "current"
    )

apPsuFailingFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3332)
)
apPsuFailingFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apPsuFailingFlag")
)
if mibBuilder.loadTexts:
    apPsuFailingFlagOff.setStatus(
        "current"
    )

apFanFailingFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3341)
)
apFanFailingFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apFanFailingFlag")
)
if mibBuilder.loadTexts:
    apFanFailingFlagOn.setStatus(
        "current"
    )

apFanFailingFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3342)
)
apFanFailingFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apFanFailingFlag")
)
if mibBuilder.loadTexts:
    apFanFailingFlagOff.setStatus(
        "current"
    )

apConfigXferFailFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3351)
)
apConfigXferFailFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apConfigXferFailFlag")
)
if mibBuilder.loadTexts:
    apConfigXferFailFlagOn.setStatus(
        "current"
    )

apConfigXferFailFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3352)
)
apConfigXferFailFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apConfigXferFailFlag")
)
if mibBuilder.loadTexts:
    apConfigXferFailFlagOff.setStatus(
        "current"
    )

apMissingRequiredPartnerFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3361)
)
apMissingRequiredPartnerFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apMissingRequiredPartnerFlag")
)
if mibBuilder.loadTexts:
    apMissingRequiredPartnerFlagOn.setStatus(
        "current"
    )

apMissingRequiredPartnerFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3362)
)
apMissingRequiredPartnerFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apMissingRequiredPartnerFlag")
)
if mibBuilder.loadTexts:
    apMissingRequiredPartnerFlagOff.setStatus(
        "current"
    )

apBgpMisconfiguredIpFlagOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3371)
)
apBgpMisconfiguredIpFlagOn.setObjects(
    ("DDOSSECURE4-MIB", "apBgpMisconfiguredIpFlag")
)
if mibBuilder.loadTexts:
    apBgpMisconfiguredIpFlagOn.setStatus(
        "current"
    )

apBgpMisconfiguredIpFlagOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 0, 3372)
)
apBgpMisconfiguredIpFlagOff.setObjects(
    ("DDOSSECURE4-MIB", "apBgpMisconfiguredIpFlag")
)
if mibBuilder.loadTexts:
    apBgpMisconfiguredIpFlagOff.setStatus(
        "current"
    )


# Notifications groups

prNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 2, 100)
)
prNotificationGroup.setObjects(
      *(("DDOSSECURE4-MIB", "prBandwidthOn"),
        ("DDOSSECURE4-MIB", "prBandwidthOff"),
        ("DDOSSECURE4-MIB", "prFloodOn"),
        ("DDOSSECURE4-MIB", "prFloodOff"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolOn"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolOff"),
        ("DDOSSECURE4-MIB", "prBlockedStateOn"),
        ("DDOSSECURE4-MIB", "prBlockedStateOff"),
        ("DDOSSECURE4-MIB", "prIpAttackOn"),
        ("DDOSSECURE4-MIB", "prIpAttackOff"),
        ("DDOSSECURE4-MIB", "prTcpAttackOn"),
        ("DDOSSECURE4-MIB", "prTcpAttackOff"),
        ("DDOSSECURE4-MIB", "prUdpAttackOn"),
        ("DDOSSECURE4-MIB", "prUdpAttackOff"),
        ("DDOSSECURE4-MIB", "prIcmpAttackOn"),
        ("DDOSSECURE4-MIB", "prIcmpAttackOff"),
        ("DDOSSECURE4-MIB", "prOtherIpAttackOn"),
        ("DDOSSECURE4-MIB", "prOtherIpAttackOff"),
        ("DDOSSECURE4-MIB", "prFragAttackOn"),
        ("DDOSSECURE4-MIB", "prFragAttackOff"),
        ("DDOSSECURE4-MIB", "prBadIpOn"),
        ("DDOSSECURE4-MIB", "prBadIpOff"),
        ("DDOSSECURE4-MIB", "prBadTcpOn"),
        ("DDOSSECURE4-MIB", "prBadTcpOff"),
        ("DDOSSECURE4-MIB", "prBadUdpOn"),
        ("DDOSSECURE4-MIB", "prBadUdpOff"),
        ("DDOSSECURE4-MIB", "prBadIcmpOn"),
        ("DDOSSECURE4-MIB", "prBadIcmpOff"),
        ("DDOSSECURE4-MIB", "prBadOtherIpOn"),
        ("DDOSSECURE4-MIB", "prBadOtherIpOff"),
        ("DDOSSECURE4-MIB", "prOverloadedOn"),
        ("DDOSSECURE4-MIB", "prOverloadedOff"),
        ("DDOSSECURE4-MIB", "apHaStateMode"),
        ("DDOSSECURE4-MIB", "apOutputErrorIIFlagOn"),
        ("DDOSSECURE4-MIB", "apOutputErrorIIFlagOff"),
        ("DDOSSECURE4-MIB", "apOutputErrorPIFlagOn"),
        ("DDOSSECURE4-MIB", "apOutputErrorPIFlagOff"),
        ("DDOSSECURE4-MIB", "apOutputErrorMIFlagOn"),
        ("DDOSSECURE4-MIB", "apOutputErrorMIFlagOff"),
        ("DDOSSECURE4-MIB", "apNewConfigFlagOn"),
        ("DDOSSECURE4-MIB", "apNewConfigFlagOff"),
        ("DDOSSECURE4-MIB", "apNotLicensedFlagOn"),
        ("DDOSSECURE4-MIB", "apNotLicensedFlagOff"),
        ("DDOSSECURE4-MIB", "apMacTableFullFlagOn"),
        ("DDOSSECURE4-MIB", "apMacTableFullFlagOff"),
        ("DDOSSECURE4-MIB", "apProtectedTableFullFlagOn"),
        ("DDOSSECURE4-MIB", "apProtectedTableFullFlagOff"),
        ("DDOSSECURE4-MIB", "apIncidentTableFullFlagOn"),
        ("DDOSSECURE4-MIB", "apIncidentTableFullFlagOff"),
        ("DDOSSECURE4-MIB", "apTcpTableFullFlagOn"),
        ("DDOSSECURE4-MIB", "apTcpTableFullFlagOff"),
        ("DDOSSECURE4-MIB", "apUdpTableFullFlagOn"),
        ("DDOSSECURE4-MIB", "apUdpTableFullFlagOff"),
        ("DDOSSECURE4-MIB", "apIcmpTableFullFlagOn"),
        ("DDOSSECURE4-MIB", "apIcmpTableFullFlagOff"),
        ("DDOSSECURE4-MIB", "apOtherIpTableFullFlagOn"),
        ("DDOSSECURE4-MIB", "apOtherIpTableFullFlagOff"),
        ("DDOSSECURE4-MIB", "apFragTableFullFlagOn"),
        ("DDOSSECURE4-MIB", "apFragTableFullFlagOff"),
        ("DDOSSECURE4-MIB", "apFtpTableFullFlagOn"),
        ("DDOSSECURE4-MIB", "apFtpTableFullFlagOff"),
        ("DDOSSECURE4-MIB", "apBlockedTableFullFlagOn"),
        ("DDOSSECURE4-MIB", "apBlockedTableFullFlagOff"),
        ("DDOSSECURE4-MIB", "apShortCircuitFlagOn"),
        ("DDOSSECURE4-MIB", "apShortCircuitFlagOff"),
        ("DDOSSECURE4-MIB", "apInternetIfDisconnectedFlagOn"),
        ("DDOSSECURE4-MIB", "apInternetIfDisconnectedFlagOff"),
        ("DDOSSECURE4-MIB", "apProtectedIfDisconnectedFlagOn"),
        ("DDOSSECURE4-MIB", "apProtectedIfDisconnectedFlagOff"),
        ("DDOSSECURE4-MIB", "apMgmtIfDisconnectedFlagOn"),
        ("DDOSSECURE4-MIB", "apMgmtIfDisconnectedFlagOff"),
        ("DDOSSECURE4-MIB", "apUpgradingFlagOn"),
        ("DDOSSECURE4-MIB", "apUpgradingFlagOff"),
        ("DDOSSECURE4-MIB", "apProtectedIfTrafficFlagOn"),
        ("DDOSSECURE4-MIB", "apProtectedIfTrafficFlagOff"),
        ("DDOSSECURE4-MIB", "apRoutingLoopFlagOn"),
        ("DDOSSECURE4-MIB", "apRoutingLoopFlagOff"),
        ("DDOSSECURE4-MIB", "apOfflineFlagOn"),
        ("DDOSSECURE4-MIB", "apOfflineFlagOff"),
        ("DDOSSECURE4-MIB", "apStateLearningFlagOn"),
        ("DDOSSECURE4-MIB", "apStateLearningFlagOff"),
        ("DDOSSECURE4-MIB", "apSupportExpiredFlagOn"),
        ("DDOSSECURE4-MIB", "apSupportExpiredFlagOff"),
        ("DDOSSECURE4-MIB", "apSevereLoadingFlagOn"),
        ("DDOSSECURE4-MIB", "apSevereLoadingFlagOff"),
        ("DDOSSECURE4-MIB", "apMacMisconfiguredFlagOn"),
        ("DDOSSECURE4-MIB", "apMacMisconfiguredFlagOff"),
        ("DDOSSECURE4-MIB", "apIfMisconfiguredFlagOn"),
        ("DDOSSECURE4-MIB", "apIfMisconfiguredFlagOff"),
        ("DDOSSECURE4-MIB", "apInternetIfLinkDownFlagOn"),
        ("DDOSSECURE4-MIB", "apInternetIfLinkDownFlagOff"),
        ("DDOSSECURE4-MIB", "apProtectedIfLinkDownFlagOn"),
        ("DDOSSECURE4-MIB", "apProtectedIfLinkDownFlagOff"),
        ("DDOSSECURE4-MIB", "apDatashareIfDisconnectedFlagOn"),
        ("DDOSSECURE4-MIB", "apDatashareIfDisconnectedFlagOff"),
        ("DDOSSECURE4-MIB", "apDiskFailingOn"),
        ("DDOSSECURE4-MIB", "apDiskFailingOff"),
        ("DDOSSECURE4-MIB", "apPsuFailingFlagOn"),
        ("DDOSSECURE4-MIB", "apPsuFailingFlagOff"),
        ("DDOSSECURE4-MIB", "apFanFailingFlagOn"),
        ("DDOSSECURE4-MIB", "apFanFailingFlagOff"),
        ("DDOSSECURE4-MIB", "apConfigXferFailFlagOn"),
        ("DDOSSECURE4-MIB", "apConfigXferFailFlagOff"),
        ("DDOSSECURE4-MIB", "apMissingRequiredPartnerFlagOn"),
        ("DDOSSECURE4-MIB", "apMissingRequiredPartnerFlagOff"),
        ("DDOSSECURE4-MIB", "apBgpMisconfiguredIpFlagOn"),
        ("DDOSSECURE4-MIB", "apBgpMisconfiguredIpFlagOff"),
        ("DDOSSECURE4-MIB", "prBandwidthLimitOn"),
        ("DDOSSECURE4-MIB", "prBandwidthLimitOff"),
        ("DDOSSECURE4-MIB", "prPacketLimitOn"),
        ("DDOSSECURE4-MIB", "prPacketLimitOff"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolBlackListIpOn"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolBlackListIpOff"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolIcmpTypeOn"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolIcmpTypeOff"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolPortOn"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolPortOff"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolOtherOn"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolOtherOff"),
        ("DDOSSECURE4-MIB", "prUnknownSessionIcmpRespOn"),
        ("DDOSSECURE4-MIB", "prUnknownSessionIcmpRespOff"),
        ("DDOSSECURE4-MIB", "prUnknownSessionIcmpDiagRespOn"),
        ("DDOSSECURE4-MIB", "prUnknownSessionIcmpDiagRespOff"),
        ("DDOSSECURE4-MIB", "prUnknownSessionNoStateOn"),
        ("DDOSSECURE4-MIB", "prUnknownSessionNoStateOff"),
        ("DDOSSECURE4-MIB", "prUnknownSessionInvalidStateOn"),
        ("DDOSSECURE4-MIB", "prUnknownSessionInvalidStateOff"),
        ("DDOSSECURE4-MIB", "prTcpAttackRstOn"),
        ("DDOSSECURE4-MIB", "prTcpAttackRstOff"),
        ("DDOSSECURE4-MIB", "prIpAttackLandOn"),
        ("DDOSSECURE4-MIB", "prIpAttackLandOff"),
        ("DDOSSECURE4-MIB", "prTcpAttackSynAckToOn"),
        ("DDOSSECURE4-MIB", "prTcpAttackSynAckToOff"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolCountryOn"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolCountryOff"),
        ("DDOSSECURE4-MIB", "prTcpAttackSynFloodOn"),
        ("DDOSSECURE4-MIB", "prTcpAttackSynFloodOff"),
        ("DDOSSECURE4-MIB", "prTcpAttackConnFloodOn"),
        ("DDOSSECURE4-MIB", "prTcpAttackConnFloodOff"),
        ("DDOSSECURE4-MIB", "prTcpAttackTableFullOn"),
        ("DDOSSECURE4-MIB", "prTcpAttackTableFullOff"),
        ("DDOSSECURE4-MIB", "prBadTcpFastAckOn"),
        ("DDOSSECURE4-MIB", "prBadTcpFastAckOff"),
        ("DDOSSECURE4-MIB", "prTcpAttackHttpFloodOn"),
        ("DDOSSECURE4-MIB", "prTcpAttackHttpFloodOff"),
        ("DDOSSECURE4-MIB", "prUdpAttackTableFullOn"),
        ("DDOSSECURE4-MIB", "prUdpAttackTableFullOff"),
        ("DDOSSECURE4-MIB", "prTcpAttackHttpTimeoutOn"),
        ("DDOSSECURE4-MIB", "prTcpAttackHttpTimeoutOff"),
        ("DDOSSECURE4-MIB", "prIcmpAttackRepeatsOn"),
        ("DDOSSECURE4-MIB", "prIcmpAttackRepeatsOff"),
        ("DDOSSECURE4-MIB", "prIcmpAttackTableFullOn"),
        ("DDOSSECURE4-MIB", "prIcmpAttackTableFullOff"),
        ("DDOSSECURE4-MIB", "prOtherIpAttackTableFullOn"),
        ("DDOSSECURE4-MIB", "prOtherIpAttackTableFullOff"),
        ("DDOSSECURE4-MIB", "prFragAttackPingOfDeathOn"),
        ("DDOSSECURE4-MIB", "prFragAttackPingOfDeathOff"),
        ("DDOSSECURE4-MIB", "prFragAttackHeadOverlayOn"),
        ("DDOSSECURE4-MIB", "prFragAttackHeadOverlayOff"),
        ("DDOSSECURE4-MIB", "prFragAttackTableFullOn"),
        ("DDOSSECURE4-MIB", "prFragAttackTableFullOff"),
        ("DDOSSECURE4-MIB", "prFragAttackSmallSizeOn"),
        ("DDOSSECURE4-MIB", "prFragAttackSmallSizeOff"),
        ("DDOSSECURE4-MIB", "prFragAttackNoFragsAllowedOn"),
        ("DDOSSECURE4-MIB", "prFragAttackNoFragsAllowedOff"),
        ("DDOSSECURE4-MIB", "prBadIpSrcAddrOn"),
        ("DDOSSECURE4-MIB", "prBadIpSrcAddrOff"),
        ("DDOSSECURE4-MIB", "prBadIpHeaderOn"),
        ("DDOSSECURE4-MIB", "prBadIpHeaderOff"),
        ("DDOSSECURE4-MIB", "prBadIpOptionOn"),
        ("DDOSSECURE4-MIB", "prBadIpOptionOff"),
        ("DDOSSECURE4-MIB", "prBadIpSizeOn"),
        ("DDOSSECURE4-MIB", "prBadIpSizeOff"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolTmpBlackListOn"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolTmpBlackListOff"),
        ("DDOSSECURE4-MIB", "prBadTcpFlagsOn"),
        ("DDOSSECURE4-MIB", "prBadTcpFlagsOff"),
        ("DDOSSECURE4-MIB", "prBadTcpMalformedOn"),
        ("DDOSSECURE4-MIB", "prBadTcpMalformedOff"),
        ("DDOSSECURE4-MIB", "prBadTcpOptionOn"),
        ("DDOSSECURE4-MIB", "prBadTcpOptionOff"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolDnsOn"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolDnsOff"),
        ("DDOSSECURE4-MIB", "prBadUdpNoDataOn"),
        ("DDOSSECURE4-MIB", "prBadUdpNoDataOff"),
        ("DDOSSECURE4-MIB", "prBadUdpMalformedOn"),
        ("DDOSSECURE4-MIB", "prBadUdpMalformedOff"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolAsOn"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolAsOff"),
        ("DDOSSECURE4-MIB", "ptTcpAttackHttpRateFloodOn"),
        ("DDOSSECURE4-MIB", "ptTcpAttackHttpRateFloodOff"),
        ("DDOSSECURE4-MIB", "prBadIcmpMalformedOn"),
        ("DDOSSECURE4-MIB", "prBadIcmpMalformedOff"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolUrlOn"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolUrlOff"),
        ("DDOSSECURE4-MIB", "prBadOtherIpProtocolOn"),
        ("DDOSSECURE4-MIB", "prBadOtherIpProtocolOff"),
        ("DDOSSECURE4-MIB", "prBadOtherIpLengthOn"),
        ("DDOSSECURE4-MIB", "prBadOtherIpLengthOff"),
        ("DDOSSECURE4-MIB", "prTcpAttackHttpIncompleteOn"),
        ("DDOSSECURE4-MIB", "prTcpAttackHttpIncompleteOff"),
        ("DDOSSECURE4-MIB", "prOverloadedStallOn"),
        ("DDOSSECURE4-MIB", "prOverloadedStallOff"),
        ("DDOSSECURE4-MIB", "prFragAttackTimeOutOn"),
        ("DDOSSECURE4-MIB", "prFragAttackTimeOutOff"),
        ("DDOSSECURE4-MIB", "prFragAttackRepeatsOn"),
        ("DDOSSECURE4-MIB", "prFragAttackRepeatsOff"),
        ("DDOSSECURE4-MIB", "prFragAttackBadLengthOn"),
        ("DDOSSECURE4-MIB", "prFragAttackBadLengthOff"),
        ("DDOSSECURE4-MIB", "prOverloadedBacklogOn"),
        ("DDOSSECURE4-MIB", "prOverloadedBacklogOff"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolAddressOn"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolAddressOff"),
        ("DDOSSECURE4-MIB", "prTcpAttackNoDataOn"),
        ("DDOSSECURE4-MIB", "prTcpAttackNoDataOff"),
        ("DDOSSECURE4-MIB", "prTcpAttackNoServerDataOn"),
        ("DDOSSECURE4-MIB", "prTcpAttackNoServerDataOff"),
        ("DDOSSECURE4-MIB", "prTcpAttackConnRateFloodOn"),
        ("DDOSSECURE4-MIB", "prTcpAttackConnRateFloodOff"),
        ("DDOSSECURE4-MIB", "prOverloadedThreadsOn"),
        ("DDOSSECURE4-MIB", "prOverloadedThreadsOff"),
        ("DDOSSECURE4-MIB", "prBadIpReflectedRouteOn"),
        ("DDOSSECURE4-MIB", "prBadIpReflectedRouteOff"),
        ("DDOSSECURE4-MIB", "prTcpAttackPortScanOn"),
        ("DDOSSECURE4-MIB", "prTcpAttackPortScanOff"),
        ("DDOSSECURE4-MIB", "prTcpAttackSmallWindowOn"),
        ("DDOSSECURE4-MIB", "prTcpAttackSmallWindowOff"),
        ("DDOSSECURE4-MIB", "prTcpAttackClientAbortOn"),
        ("DDOSSECURE4-MIB", "prTcpAttackClientAbortOff"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolSipOn"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolSipOff"),
        ("DDOSSECURE4-MIB", "prTcpAttackUrlRateLimitOn"),
        ("DDOSSECURE4-MIB", "prTcpAttackUrlRateLimitOff"),
        ("DDOSSECURE4-MIB", "prUdpAttackDnsRateLimitOn"),
        ("DDOSSECURE4-MIB", "prUdpAttackDnsRateLimitOff"),
        ("DDOSSECURE4-MIB", "prUdpAttackSipRateLimitOn"),
        ("DDOSSECURE4-MIB", "prUdpAttackSipRateLimitOff"),
        ("DDOSSECURE4-MIB", "prBadTcpChecksumOn"),
        ("DDOSSECURE4-MIB", "prBadTcpChecksumOff"),
        ("DDOSSECURE4-MIB", "prTcpAttackHttpFormatOn"),
        ("DDOSSECURE4-MIB", "prTcpAttackHttpFormatOff"),
        ("DDOSSECURE4-MIB", "prUnknownSessionReflectiveOn"),
        ("DDOSSECURE4-MIB", "prUnknownSessionReflectiveOff"))
)
if mibBuilder.loadTexts:
    prNotificationGroup.setStatus(
        "current"
    )

deprecatedNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 2, 101)
)
deprecatedNotificationGroup.setObjects(
      *(("DDOSSECURE4-MIB", "apOutputErrorIIEvent"),
        ("DDOSSECURE4-MIB", "apOutputErrorPIEvent"),
        ("DDOSSECURE4-MIB", "apOutputErrorMIEvent"),
        ("DDOSSECURE4-MIB", "apNewConfigEvent"),
        ("DDOSSECURE4-MIB", "apNotLicensedEvent"),
        ("DDOSSECURE4-MIB", "apMacTableFullEvent"),
        ("DDOSSECURE4-MIB", "apProtectedTableFullEvent"),
        ("DDOSSECURE4-MIB", "apIncidentTableFullEvent"),
        ("DDOSSECURE4-MIB", "apTcpTableFullEvent"),
        ("DDOSSECURE4-MIB", "apUdpTableFullEvent"),
        ("DDOSSECURE4-MIB", "apIcmpTableFullEvent"),
        ("DDOSSECURE4-MIB", "apOtherIpTableFullEvent"),
        ("DDOSSECURE4-MIB", "apFragTableFullEvent"),
        ("DDOSSECURE4-MIB", "apFtpTableFullEvent"),
        ("DDOSSECURE4-MIB", "apBlockedTableFullEvent"),
        ("DDOSSECURE4-MIB", "apShortCircuitEvent"),
        ("DDOSSECURE4-MIB", "apInternetIfDisconnectedEvent"),
        ("DDOSSECURE4-MIB", "apProtectedIfDisconnectedEvent"),
        ("DDOSSECURE4-MIB", "apMgmtIfDisconnectedEvent"),
        ("DDOSSECURE4-MIB", "apUpgradingEvent"),
        ("DDOSSECURE4-MIB", "apProtectedIfTrafficEvent"),
        ("DDOSSECURE4-MIB", "apRoutingLoopEvent"),
        ("DDOSSECURE4-MIB", "apOfflineEvent"),
        ("DDOSSECURE4-MIB", "apStateLearningEvent"),
        ("DDOSSECURE4-MIB", "apSupportExpiredEvent"),
        ("DDOSSECURE4-MIB", "apSevereLoadingEvent"),
        ("DDOSSECURE4-MIB", "apMacMisconfiguredEvent"),
        ("DDOSSECURE4-MIB", "apIfMisconfiguredEvent"),
        ("DDOSSECURE4-MIB", "apInternetIfLinkDownEvent"),
        ("DDOSSECURE4-MIB", "apProtectedIfLinkDownEvent"),
        ("DDOSSECURE4-MIB", "apDatashareIfDisconnectedEvent"),
        ("DDOSSECURE4-MIB", "apHaStateEvent"),
        ("DDOSSECURE4-MIB", "prBandwidthEvent"),
        ("DDOSSECURE4-MIB", "prFloodEvent"),
        ("DDOSSECURE4-MIB", "prBlockedProtocolEvent"),
        ("DDOSSECURE4-MIB", "prBlockedStateEvent"),
        ("DDOSSECURE4-MIB", "prIpAttackEvent"),
        ("DDOSSECURE4-MIB", "prTcpAttackEvent"),
        ("DDOSSECURE4-MIB", "prUdpAttackEvent"),
        ("DDOSSECURE4-MIB", "prIcmpAttackEvent"),
        ("DDOSSECURE4-MIB", "prOtherIpAttackEvent"),
        ("DDOSSECURE4-MIB", "prFragAttackEvent"),
        ("DDOSSECURE4-MIB", "prBadIpEvent"),
        ("DDOSSECURE4-MIB", "prBadTcpEvent"),
        ("DDOSSECURE4-MIB", "prBadUdpEvent"),
        ("DDOSSECURE4-MIB", "prBadIcmpEvent"),
        ("DDOSSECURE4-MIB", "prBadOtherIpEvent"),
        ("DDOSSECURE4-MIB", "prOverloadedEvent"))
)
if mibBuilder.loadTexts:
    deprecatedNotificationGroup.setStatus(
        "deprecated"
    )


# Agent capabilities


# Module compliance

ddossecure4MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 1, 1)
)
ddossecure4MIBCompliance.setObjects(
      *(("DDOSSECURE4-MIB", "apCfgGroup"),
        ("DDOSSECURE4-MIB", "gwGroup"),
        ("DDOSSECURE4-MIB", "apIncidentGroup"),
        ("DDOSSECURE4-MIB", "apDebugGroup"),
        ("DDOSSECURE4-MIB", "apGroup"),
        ("DDOSSECURE4-MIB", "poGroup"),
        ("DDOSSECURE4-MIB", "prGroup"),
        ("DDOSSECURE4-MIB", "prCfgGroup"),
        ("DDOSSECURE4-MIB", "gwCfgGroup"),
        ("DDOSSECURE4-MIB", "apEventObjectGroup"),
        ("DDOSSECURE4-MIB", "apRatesGroup"),
        ("DDOSSECURE4-MIB", "poFilterCfgGroup"),
        ("DDOSSECURE4-MIB", "apLinkStatusGroup"),
        ("DDOSSECURE4-MIB", "apLogGroup"),
        ("DDOSSECURE4-MIB", "apHaCfgGroup"),
        ("DDOSSECURE4-MIB", "prNotificationGroup"))
)
if mibBuilder.loadTexts:
    ddossecure4MIBCompliance.setStatus(
        "current"
    )

ddossecure4MIBComplianceDep = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11068, 1, 4, 9, 1, 2)
)
ddossecure4MIBComplianceDep.setObjects(
    ("DDOSSECURE4-MIB", "deprecatedNotificationGroup")
)
if mibBuilder.loadTexts:
    ddossecure4MIBComplianceDep.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DDOSSECURE4-MIB",
    **{"DefenseType": DefenseType,
       "Direction": Direction,
       "LocalIndex": LocalIndex,
       "ddossecure4MIB": ddossecure4MIB,
       "ddossecureEvents": ddossecureEvents,
       "apOutputErrorIIEvent": apOutputErrorIIEvent,
       "apOutputErrorPIEvent": apOutputErrorPIEvent,
       "apOutputErrorMIEvent": apOutputErrorMIEvent,
       "apNewConfigEvent": apNewConfigEvent,
       "apNotLicensedEvent": apNotLicensedEvent,
       "apMacTableFullEvent": apMacTableFullEvent,
       "apProtectedTableFullEvent": apProtectedTableFullEvent,
       "apIncidentTableFullEvent": apIncidentTableFullEvent,
       "apTcpTableFullEvent": apTcpTableFullEvent,
       "apUdpTableFullEvent": apUdpTableFullEvent,
       "apIcmpTableFullEvent": apIcmpTableFullEvent,
       "apOtherIpTableFullEvent": apOtherIpTableFullEvent,
       "apFragTableFullEvent": apFragTableFullEvent,
       "apFtpTableFullEvent": apFtpTableFullEvent,
       "apBlockedTableFullEvent": apBlockedTableFullEvent,
       "apShortCircuitEvent": apShortCircuitEvent,
       "apInternetIfDisconnectedEvent": apInternetIfDisconnectedEvent,
       "apProtectedIfDisconnectedEvent": apProtectedIfDisconnectedEvent,
       "apMgmtIfDisconnectedEvent": apMgmtIfDisconnectedEvent,
       "apUpgradingEvent": apUpgradingEvent,
       "apProtectedIfTrafficEvent": apProtectedIfTrafficEvent,
       "apRoutingLoopEvent": apRoutingLoopEvent,
       "apOfflineEvent": apOfflineEvent,
       "apStateLearningEvent": apStateLearningEvent,
       "apSupportExpiredEvent": apSupportExpiredEvent,
       "apSevereLoadingEvent": apSevereLoadingEvent,
       "apMacMisconfiguredEvent": apMacMisconfiguredEvent,
       "apIfMisconfiguredEvent": apIfMisconfiguredEvent,
       "apInternetIfLinkDownEvent": apInternetIfLinkDownEvent,
       "apProtectedIfLinkDownEvent": apProtectedIfLinkDownEvent,
       "apDatashareIfDisconnectedEvent": apDatashareIfDisconnectedEvent,
       "apHaStateEvent": apHaStateEvent,
       "prBandwidthEvent": prBandwidthEvent,
       "prFloodEvent": prFloodEvent,
       "prBlockedProtocolEvent": prBlockedProtocolEvent,
       "prBlockedStateEvent": prBlockedStateEvent,
       "prIpAttackEvent": prIpAttackEvent,
       "prTcpAttackEvent": prTcpAttackEvent,
       "prUdpAttackEvent": prUdpAttackEvent,
       "prIcmpAttackEvent": prIcmpAttackEvent,
       "prOtherIpAttackEvent": prOtherIpAttackEvent,
       "prFragAttackEvent": prFragAttackEvent,
       "prBadIpEvent": prBadIpEvent,
       "prBadTcpEvent": prBadTcpEvent,
       "prBadUdpEvent": prBadUdpEvent,
       "prBadIcmpEvent": prBadIcmpEvent,
       "prBadOtherIpEvent": prBadOtherIpEvent,
       "prOverloadedEvent": prOverloadedEvent,
       "prBandwidthOn": prBandwidthOn,
       "prBandwidthOff": prBandwidthOff,
       "prFloodOn": prFloodOn,
       "prFloodOff": prFloodOff,
       "prBlockedProtocolOn": prBlockedProtocolOn,
       "prBlockedProtocolOff": prBlockedProtocolOff,
       "prBlockedStateOn": prBlockedStateOn,
       "prBlockedStateOff": prBlockedStateOff,
       "prIpAttackOn": prIpAttackOn,
       "prIpAttackOff": prIpAttackOff,
       "prTcpAttackOn": prTcpAttackOn,
       "prTcpAttackOff": prTcpAttackOff,
       "prUdpAttackOn": prUdpAttackOn,
       "prUdpAttackOff": prUdpAttackOff,
       "prIcmpAttackOn": prIcmpAttackOn,
       "prIcmpAttackOff": prIcmpAttackOff,
       "prOtherIpAttackOn": prOtherIpAttackOn,
       "prOtherIpAttackOff": prOtherIpAttackOff,
       "prFragAttackOn": prFragAttackOn,
       "prFragAttackOff": prFragAttackOff,
       "prBadIpOn": prBadIpOn,
       "prBadIpOff": prBadIpOff,
       "prBadTcpOn": prBadTcpOn,
       "prBadTcpOff": prBadTcpOff,
       "prBadUdpOn": prBadUdpOn,
       "prBadUdpOff": prBadUdpOff,
       "prBadIcmpOn": prBadIcmpOn,
       "prBadIcmpOff": prBadIcmpOff,
       "prBadOtherIpOn": prBadOtherIpOn,
       "prBadOtherIpOff": prBadOtherIpOff,
       "prOverloadedOn": prOverloadedOn,
       "prOverloadedOff": prOverloadedOff,
       "apHaStateMode": apHaStateMode,
       "prBandwidthLimitOn": prBandwidthLimitOn,
       "prBandwidthLimitOff": prBandwidthLimitOff,
       "prPacketLimitOn": prPacketLimitOn,
       "prPacketLimitOff": prPacketLimitOff,
       "prBlockedProtocolBlackListIpOn": prBlockedProtocolBlackListIpOn,
       "prBlockedProtocolBlackListIpOff": prBlockedProtocolBlackListIpOff,
       "prBlockedProtocolIcmpTypeOn": prBlockedProtocolIcmpTypeOn,
       "prBlockedProtocolIcmpTypeOff": prBlockedProtocolIcmpTypeOff,
       "prBlockedProtocolPortOn": prBlockedProtocolPortOn,
       "prBlockedProtocolPortOff": prBlockedProtocolPortOff,
       "prBlockedProtocolOtherOn": prBlockedProtocolOtherOn,
       "prBlockedProtocolOtherOff": prBlockedProtocolOtherOff,
       "prUnknownSessionIcmpRespOn": prUnknownSessionIcmpRespOn,
       "prUnknownSessionIcmpRespOff": prUnknownSessionIcmpRespOff,
       "prUnknownSessionIcmpDiagRespOn": prUnknownSessionIcmpDiagRespOn,
       "prUnknownSessionIcmpDiagRespOff": prUnknownSessionIcmpDiagRespOff,
       "prUnknownSessionNoStateOn": prUnknownSessionNoStateOn,
       "prUnknownSessionNoStateOff": prUnknownSessionNoStateOff,
       "prUnknownSessionInvalidStateOn": prUnknownSessionInvalidStateOn,
       "prUnknownSessionInvalidStateOff": prUnknownSessionInvalidStateOff,
       "prTcpAttackRstOn": prTcpAttackRstOn,
       "prTcpAttackRstOff": prTcpAttackRstOff,
       "prIpAttackLandOn": prIpAttackLandOn,
       "prIpAttackLandOff": prIpAttackLandOff,
       "prTcpAttackSynAckToOn": prTcpAttackSynAckToOn,
       "prTcpAttackSynAckToOff": prTcpAttackSynAckToOff,
       "prBlockedProtocolCountryOn": prBlockedProtocolCountryOn,
       "prBlockedProtocolCountryOff": prBlockedProtocolCountryOff,
       "prTcpAttackSynFloodOn": prTcpAttackSynFloodOn,
       "prTcpAttackSynFloodOff": prTcpAttackSynFloodOff,
       "prTcpAttackConnFloodOn": prTcpAttackConnFloodOn,
       "prTcpAttackConnFloodOff": prTcpAttackConnFloodOff,
       "prTcpAttackTableFullOn": prTcpAttackTableFullOn,
       "prTcpAttackTableFullOff": prTcpAttackTableFullOff,
       "prBadTcpFastAckOn": prBadTcpFastAckOn,
       "prBadTcpFastAckOff": prBadTcpFastAckOff,
       "prTcpAttackHttpFloodOn": prTcpAttackHttpFloodOn,
       "prTcpAttackHttpFloodOff": prTcpAttackHttpFloodOff,
       "prUdpAttackTableFullOn": prUdpAttackTableFullOn,
       "prUdpAttackTableFullOff": prUdpAttackTableFullOff,
       "prTcpAttackHttpTimeoutOn": prTcpAttackHttpTimeoutOn,
       "prTcpAttackHttpTimeoutOff": prTcpAttackHttpTimeoutOff,
       "prIcmpAttackRepeatsOn": prIcmpAttackRepeatsOn,
       "prIcmpAttackRepeatsOff": prIcmpAttackRepeatsOff,
       "prIcmpAttackTableFullOn": prIcmpAttackTableFullOn,
       "prIcmpAttackTableFullOff": prIcmpAttackTableFullOff,
       "prOtherIpAttackTableFullOn": prOtherIpAttackTableFullOn,
       "prOtherIpAttackTableFullOff": prOtherIpAttackTableFullOff,
       "prFragAttackPingOfDeathOn": prFragAttackPingOfDeathOn,
       "prFragAttackPingOfDeathOff": prFragAttackPingOfDeathOff,
       "prFragAttackHeadOverlayOn": prFragAttackHeadOverlayOn,
       "prFragAttackHeadOverlayOff": prFragAttackHeadOverlayOff,
       "prFragAttackTableFullOn": prFragAttackTableFullOn,
       "prFragAttackTableFullOff": prFragAttackTableFullOff,
       "prFragAttackSmallSizeOn": prFragAttackSmallSizeOn,
       "prFragAttackSmallSizeOff": prFragAttackSmallSizeOff,
       "prFragAttackNoFragsAllowedOn": prFragAttackNoFragsAllowedOn,
       "prFragAttackNoFragsAllowedOff": prFragAttackNoFragsAllowedOff,
       "prBadIpSrcAddrOn": prBadIpSrcAddrOn,
       "prBadIpSrcAddrOff": prBadIpSrcAddrOff,
       "prBadIpHeaderOn": prBadIpHeaderOn,
       "prBadIpHeaderOff": prBadIpHeaderOff,
       "prBadIpOptionOn": prBadIpOptionOn,
       "prBadIpOptionOff": prBadIpOptionOff,
       "prBadIpSizeOn": prBadIpSizeOn,
       "prBadIpSizeOff": prBadIpSizeOff,
       "prBlockedProtocolTmpBlackListOn": prBlockedProtocolTmpBlackListOn,
       "prBlockedProtocolTmpBlackListOff": prBlockedProtocolTmpBlackListOff,
       "prBadTcpFlagsOn": prBadTcpFlagsOn,
       "prBadTcpFlagsOff": prBadTcpFlagsOff,
       "prBadTcpMalformedOn": prBadTcpMalformedOn,
       "prBadTcpMalformedOff": prBadTcpMalformedOff,
       "prBadTcpOptionOn": prBadTcpOptionOn,
       "prBadTcpOptionOff": prBadTcpOptionOff,
       "prBlockedProtocolDnsOn": prBlockedProtocolDnsOn,
       "prBlockedProtocolDnsOff": prBlockedProtocolDnsOff,
       "prBadUdpNoDataOn": prBadUdpNoDataOn,
       "prBadUdpNoDataOff": prBadUdpNoDataOff,
       "prBadUdpMalformedOn": prBadUdpMalformedOn,
       "prBadUdpMalformedOff": prBadUdpMalformedOff,
       "prBlockedProtocolAsOn": prBlockedProtocolAsOn,
       "prBlockedProtocolAsOff": prBlockedProtocolAsOff,
       "ptTcpAttackHttpRateFloodOn": ptTcpAttackHttpRateFloodOn,
       "ptTcpAttackHttpRateFloodOff": ptTcpAttackHttpRateFloodOff,
       "prBadIcmpMalformedOn": prBadIcmpMalformedOn,
       "prBadIcmpMalformedOff": prBadIcmpMalformedOff,
       "prBlockedProtocolUrlOn": prBlockedProtocolUrlOn,
       "prBlockedProtocolUrlOff": prBlockedProtocolUrlOff,
       "prBadOtherIpProtocolOn": prBadOtherIpProtocolOn,
       "prBadOtherIpProtocolOff": prBadOtherIpProtocolOff,
       "prBadOtherIpLengthOn": prBadOtherIpLengthOn,
       "prBadOtherIpLengthOff": prBadOtherIpLengthOff,
       "prTcpAttackHttpIncompleteOn": prTcpAttackHttpIncompleteOn,
       "prTcpAttackHttpIncompleteOff": prTcpAttackHttpIncompleteOff,
       "prOverloadedStallOn": prOverloadedStallOn,
       "prOverloadedStallOff": prOverloadedStallOff,
       "prFragAttackTimeOutOn": prFragAttackTimeOutOn,
       "prFragAttackTimeOutOff": prFragAttackTimeOutOff,
       "prFragAttackRepeatsOn": prFragAttackRepeatsOn,
       "prFragAttackRepeatsOff": prFragAttackRepeatsOff,
       "prFragAttackBadLengthOn": prFragAttackBadLengthOn,
       "prFragAttackBadLengthOff": prFragAttackBadLengthOff,
       "prOverloadedBacklogOn": prOverloadedBacklogOn,
       "prOverloadedBacklogOff": prOverloadedBacklogOff,
       "prBlockedProtocolAddressOn": prBlockedProtocolAddressOn,
       "prBlockedProtocolAddressOff": prBlockedProtocolAddressOff,
       "prTcpAttackNoDataOn": prTcpAttackNoDataOn,
       "prTcpAttackNoDataOff": prTcpAttackNoDataOff,
       "prTcpAttackNoServerDataOn": prTcpAttackNoServerDataOn,
       "prTcpAttackNoServerDataOff": prTcpAttackNoServerDataOff,
       "prTcpAttackConnRateFloodOn": prTcpAttackConnRateFloodOn,
       "prTcpAttackConnRateFloodOff": prTcpAttackConnRateFloodOff,
       "prOverloadedThreadsOn": prOverloadedThreadsOn,
       "prOverloadedThreadsOff": prOverloadedThreadsOff,
       "prBadIpReflectedRouteOn": prBadIpReflectedRouteOn,
       "prBadIpReflectedRouteOff": prBadIpReflectedRouteOff,
       "prTcpAttackPortScanOn": prTcpAttackPortScanOn,
       "prTcpAttackPortScanOff": prTcpAttackPortScanOff,
       "prTcpAttackSmallWindowOn": prTcpAttackSmallWindowOn,
       "prTcpAttackSmallWindowOff": prTcpAttackSmallWindowOff,
       "prTcpAttackClientAbortOn": prTcpAttackClientAbortOn,
       "prTcpAttackClientAbortOff": prTcpAttackClientAbortOff,
       "prBlockedProtocolSipOn": prBlockedProtocolSipOn,
       "prBlockedProtocolSipOff": prBlockedProtocolSipOff,
       "prTcpAttackUrlRateLimitOn": prTcpAttackUrlRateLimitOn,
       "prTcpAttackUrlRateLimitOff": prTcpAttackUrlRateLimitOff,
       "prUdpAttackDnsRateLimitOn": prUdpAttackDnsRateLimitOn,
       "prUdpAttackDnsRateLimitOff": prUdpAttackDnsRateLimitOff,
       "prUdpAttackSipRateLimitOn": prUdpAttackSipRateLimitOn,
       "prUdpAttackSipRateLimitOff": prUdpAttackSipRateLimitOff,
       "prBadTcpChecksumOn": prBadTcpChecksumOn,
       "prBadTcpChecksumOff": prBadTcpChecksumOff,
       "prTcpAttackHttpFormatOn": prTcpAttackHttpFormatOn,
       "prTcpAttackHttpFormatOff": prTcpAttackHttpFormatOff,
       "prUnknownSessionReflectiveOn": prUnknownSessionReflectiveOn,
       "prUnknownSessionReflectiveOff": prUnknownSessionReflectiveOff,
       "apOutputErrorIIFlagOn": apOutputErrorIIFlagOn,
       "apOutputErrorIIFlagOff": apOutputErrorIIFlagOff,
       "apOutputErrorPIFlagOn": apOutputErrorPIFlagOn,
       "apOutputErrorPIFlagOff": apOutputErrorPIFlagOff,
       "apOutputErrorMIFlagOn": apOutputErrorMIFlagOn,
       "apOutputErrorMIFlagOff": apOutputErrorMIFlagOff,
       "apNewConfigFlagOn": apNewConfigFlagOn,
       "apNewConfigFlagOff": apNewConfigFlagOff,
       "apNotLicensedFlagOn": apNotLicensedFlagOn,
       "apNotLicensedFlagOff": apNotLicensedFlagOff,
       "apMacTableFullFlagOn": apMacTableFullFlagOn,
       "apMacTableFullFlagOff": apMacTableFullFlagOff,
       "apProtectedTableFullFlagOn": apProtectedTableFullFlagOn,
       "apProtectedTableFullFlagOff": apProtectedTableFullFlagOff,
       "apIncidentTableFullFlagOn": apIncidentTableFullFlagOn,
       "apIncidentTableFullFlagOff": apIncidentTableFullFlagOff,
       "apTcpTableFullFlagOn": apTcpTableFullFlagOn,
       "apTcpTableFullFlagOff": apTcpTableFullFlagOff,
       "apUdpTableFullFlagOn": apUdpTableFullFlagOn,
       "apUdpTableFullFlagOff": apUdpTableFullFlagOff,
       "apIcmpTableFullFlagOn": apIcmpTableFullFlagOn,
       "apIcmpTableFullFlagOff": apIcmpTableFullFlagOff,
       "apOtherIpTableFullFlagOn": apOtherIpTableFullFlagOn,
       "apOtherIpTableFullFlagOff": apOtherIpTableFullFlagOff,
       "apFragTableFullFlagOn": apFragTableFullFlagOn,
       "apFragTableFullFlagOff": apFragTableFullFlagOff,
       "apFtpTableFullFlagOn": apFtpTableFullFlagOn,
       "apFtpTableFullFlagOff": apFtpTableFullFlagOff,
       "apBlockedTableFullFlagOn": apBlockedTableFullFlagOn,
       "apBlockedTableFullFlagOff": apBlockedTableFullFlagOff,
       "apShortCircuitFlagOn": apShortCircuitFlagOn,
       "apShortCircuitFlagOff": apShortCircuitFlagOff,
       "apInternetIfDisconnectedFlagOn": apInternetIfDisconnectedFlagOn,
       "apInternetIfDisconnectedFlagOff": apInternetIfDisconnectedFlagOff,
       "apProtectedIfDisconnectedFlagOn": apProtectedIfDisconnectedFlagOn,
       "apProtectedIfDisconnectedFlagOff": apProtectedIfDisconnectedFlagOff,
       "apMgmtIfDisconnectedFlagOn": apMgmtIfDisconnectedFlagOn,
       "apMgmtIfDisconnectedFlagOff": apMgmtIfDisconnectedFlagOff,
       "apUpgradingFlagOn": apUpgradingFlagOn,
       "apUpgradingFlagOff": apUpgradingFlagOff,
       "apProtectedIfTrafficFlagOn": apProtectedIfTrafficFlagOn,
       "apProtectedIfTrafficFlagOff": apProtectedIfTrafficFlagOff,
       "apRoutingLoopFlagOn": apRoutingLoopFlagOn,
       "apRoutingLoopFlagOff": apRoutingLoopFlagOff,
       "apOfflineFlagOn": apOfflineFlagOn,
       "apOfflineFlagOff": apOfflineFlagOff,
       "apStateLearningFlagOn": apStateLearningFlagOn,
       "apStateLearningFlagOff": apStateLearningFlagOff,
       "apSupportExpiredFlagOn": apSupportExpiredFlagOn,
       "apSupportExpiredFlagOff": apSupportExpiredFlagOff,
       "apSevereLoadingFlagOn": apSevereLoadingFlagOn,
       "apSevereLoadingFlagOff": apSevereLoadingFlagOff,
       "apMacMisconfiguredFlagOn": apMacMisconfiguredFlagOn,
       "apMacMisconfiguredFlagOff": apMacMisconfiguredFlagOff,
       "apIfMisconfiguredFlagOn": apIfMisconfiguredFlagOn,
       "apIfMisconfiguredFlagOff": apIfMisconfiguredFlagOff,
       "apInternetIfLinkDownFlagOn": apInternetIfLinkDownFlagOn,
       "apInternetIfLinkDownFlagOff": apInternetIfLinkDownFlagOff,
       "apProtectedIfLinkDownFlagOn": apProtectedIfLinkDownFlagOn,
       "apProtectedIfLinkDownFlagOff": apProtectedIfLinkDownFlagOff,
       "apDatashareIfDisconnectedFlagOn": apDatashareIfDisconnectedFlagOn,
       "apDatashareIfDisconnectedFlagOff": apDatashareIfDisconnectedFlagOff,
       "apDiskFailingOn": apDiskFailingOn,
       "apDiskFailingOff": apDiskFailingOff,
       "apPsuFailingFlagOn": apPsuFailingFlagOn,
       "apPsuFailingFlagOff": apPsuFailingFlagOff,
       "apFanFailingFlagOn": apFanFailingFlagOn,
       "apFanFailingFlagOff": apFanFailingFlagOff,
       "apConfigXferFailFlagOn": apConfigXferFailFlagOn,
       "apConfigXferFailFlagOff": apConfigXferFailFlagOff,
       "apMissingRequiredPartnerFlagOn": apMissingRequiredPartnerFlagOn,
       "apMissingRequiredPartnerFlagOff": apMissingRequiredPartnerFlagOff,
       "apBgpMisconfiguredIpFlagOn": apBgpMisconfiguredIpFlagOn,
       "apBgpMisconfiguredIpFlagOff": apBgpMisconfiguredIpFlagOff,
       "jddsAppliance": jddsAppliance,
       "apConfig": apConfig,
       "apInterfaces": apInterfaces,
       "apManagement": apManagement,
       "apMgmtIfIpAddress": apMgmtIfIpAddress,
       "apMgmtIfNetmask": apMgmtIfNetmask,
       "apMgmtIfGwIpAddress": apMgmtIfGwIpAddress,
       "apMgmtIfLinkMode": apMgmtIfLinkMode,
       "apMgmtIfLinkFC": apMgmtIfLinkFC,
       "apMgmtIfName": apMgmtIfName,
       "apInternet": apInternet,
       "apIntIfLinkMode": apIntIfLinkMode,
       "apIntIfLinkFC": apIntIfLinkFC,
       "apIntIfName": apIntIfName,
       "apProtectedInterface": apProtectedInterface,
       "apProtIfLinkMode": apProtIfLinkMode,
       "apProtIfLinkFC": apProtIfLinkFC,
       "apProtIfName": apProtIfName,
       "apDataShare": apDataShare,
       "apDataIfIpAddress": apDataIfIpAddress,
       "apDataIfNetmask": apDataIfNetmask,
       "apDataIfLinkMode": apDataIfLinkMode,
       "apDataIfLinkFC": apDataIfLinkFC,
       "apDataIfName": apDataIfName,
       "apAccess": apAccess,
       "apUserTable": apUserTable,
       "apUserEntry": apUserEntry,
       "apUserId": apUserId,
       "apUserName": apUserName,
       "apUserPermissions": apUserPermissions,
       "apSnmpAccessIpList": apSnmpAccessIpList,
       "apHttpsAccessIpList": apHttpsAccessIpList,
       "apSshAccessIpList": apSshAccessIpList,
       "apLogging": apLogging,
       "apSyslogServer": apSyslogServer,
       "apSyslogFacility": apSyslogFacility,
       "apSyslogPriority": apSyslogPriority,
       "apWebtrendsServer": apWebtrendsServer,
       "apWebtrendsFacility": apWebtrendsFacility,
       "apWebtrendsPriority": apWebtrendsPriority,
       "apCreateIncidentsThreshold": apCreateIncidentsThreshold,
       "apBandwidthCreateThresh": apBandwidthCreateThresh,
       "apBandwidthCreateThreshRate": apBandwidthCreateThreshRate,
       "apFloodCreateThresh": apFloodCreateThresh,
       "apFloodCreateThreshRate": apFloodCreateThreshRate,
       "apBlockedProtoCreateThresh": apBlockedProtoCreateThresh,
       "apBlockedProtoCreateThreshRate": apBlockedProtoCreateThreshRate,
       "apBlockedStateCreateThresh": apBlockedStateCreateThresh,
       "apBlockedStateCreateThreshRate": apBlockedStateCreateThreshRate,
       "apIpAttackCreateThresh": apIpAttackCreateThresh,
       "apIpAttackCreateThreshRate": apIpAttackCreateThreshRate,
       "apTcpAttackCreateThresh": apTcpAttackCreateThresh,
       "apTcpAttackCreateThreshRate": apTcpAttackCreateThreshRate,
       "apUdpAttackCreateThresh": apUdpAttackCreateThresh,
       "apUdpAttackCreateThreshRate": apUdpAttackCreateThreshRate,
       "apIcmpAttackCreateThresh": apIcmpAttackCreateThresh,
       "apIcmpAttackCreateThreshRate": apIcmpAttackCreateThreshRate,
       "apOtherIpAttackCreateThresh": apOtherIpAttackCreateThresh,
       "apOtherIpAttackCreateThreshRate": apOtherIpAttackCreateThreshRate,
       "apFragAttackCreateThresh": apFragAttackCreateThresh,
       "apFragAttackCreateThreshRate": apFragAttackCreateThreshRate,
       "apBadIpCreateThresh": apBadIpCreateThresh,
       "apBadIpCreateThreshRate": apBadIpCreateThreshRate,
       "apBadTcpCreateThresh": apBadTcpCreateThresh,
       "apBadTcpCreateThreshRate": apBadTcpCreateThreshRate,
       "apBadUdpCreateThresh": apBadUdpCreateThresh,
       "apBadUdpCreateThreshRate": apBadUdpCreateThreshRate,
       "apBadIcmpCreateThresh": apBadIcmpCreateThresh,
       "apBadIcmpCreateThreshRate": apBadIcmpCreateThreshRate,
       "apBadOtherIpCreateThresh": apBadOtherIpCreateThresh,
       "apBadOtherIpCreateThreshRate": apBadOtherIpCreateThreshRate,
       "apOverloadedIpCreateThresh": apOverloadedIpCreateThresh,
       "apOverloadedIpCreateThreshRate": apOverloadedIpCreateThreshRate,
       "apViewIncidentsThresholds": apViewIncidentsThresholds,
       "apBandwidthViewThresh": apBandwidthViewThresh,
       "apBandwidthViewThreshRate": apBandwidthViewThreshRate,
       "apFloodViewThresh": apFloodViewThresh,
       "apFloodViewThreshRate": apFloodViewThreshRate,
       "apBlockedProtoViewThresh": apBlockedProtoViewThresh,
       "apBlockedProtoViewThreshRate": apBlockedProtoViewThreshRate,
       "apBlockedStateViewThresh": apBlockedStateViewThresh,
       "apBlockedStateViewThreshRate": apBlockedStateViewThreshRate,
       "apIpAttackViewThresh": apIpAttackViewThresh,
       "apIpAttackViewThreshRate": apIpAttackViewThreshRate,
       "apTcpAttackViewThresh": apTcpAttackViewThresh,
       "apTcpAttackViewThreshRate": apTcpAttackViewThreshRate,
       "apUdpAttackViewThresh": apUdpAttackViewThresh,
       "apUdpAttackViewThreshRate": apUdpAttackViewThreshRate,
       "apIcmpAttackViewThresh": apIcmpAttackViewThresh,
       "apIcmpAttackViewThreshRate": apIcmpAttackViewThreshRate,
       "apOtherIpAttackViewThresh": apOtherIpAttackViewThresh,
       "apOtherIpAttackViewThreshRate": apOtherIpAttackViewThreshRate,
       "apFragAttackViewThresh": apFragAttackViewThresh,
       "apFragAttackViewThreshRate": apFragAttackViewThreshRate,
       "apBadIpViewThresh": apBadIpViewThresh,
       "apBadIpViewThreshRate": apBadIpViewThreshRate,
       "apBadTcpViewThresh": apBadTcpViewThresh,
       "apBadTcpViewThreshRate": apBadTcpViewThreshRate,
       "apBadUdpViewThresh": apBadUdpViewThresh,
       "apBadUdpViewThreshRate": apBadUdpViewThreshRate,
       "apBadIcmpViewThresh": apBadIcmpViewThresh,
       "apBadIcmpViewThreshRate": apBadIcmpViewThreshRate,
       "apBadOtherIpViewThresh": apBadOtherIpViewThresh,
       "apBadOtherIpViewThreshRate": apBadOtherIpViewThreshRate,
       "apOverloadedIpViewThresh": apOverloadedIpViewThresh,
       "apOverloadedIpViewThreshRate": apOverloadedIpViewThreshRate,
       "apWOffenderLogThreshold": apWOffenderLogThreshold,
       "apBandwidthOffThresh": apBandwidthOffThresh,
       "apBandwidthOffThreshRate": apBandwidthOffThreshRate,
       "apFloodOffThresh": apFloodOffThresh,
       "apFloodOffThreshRate": apFloodOffThreshRate,
       "apBlockedProtoOffThresh": apBlockedProtoOffThresh,
       "apBlockedProtoOffThreshRate": apBlockedProtoOffThreshRate,
       "apBlockedStateOffThresh": apBlockedStateOffThresh,
       "apBlockedStateOffThreshRate": apBlockedStateOffThreshRate,
       "apIpAttackOffThresh": apIpAttackOffThresh,
       "apIpAttackOffThreshRate": apIpAttackOffThreshRate,
       "apTcpAttackOffThresh": apTcpAttackOffThresh,
       "apTcpAttackOffThreshRate": apTcpAttackOffThreshRate,
       "apUdpAttackOffThresh": apUdpAttackOffThresh,
       "apUdpAttackOffThreshRate": apUdpAttackOffThreshRate,
       "apIcmpAttackOffThresh": apIcmpAttackOffThresh,
       "apIcmpAttackOffThreshRate": apIcmpAttackOffThreshRate,
       "apOtherIpAttackOffThresh": apOtherIpAttackOffThresh,
       "apOtherIpAttackOffThreshRate": apOtherIpAttackOffThreshRate,
       "apFragAttackOffThresh": apFragAttackOffThresh,
       "apFragAttackOffThreshRate": apFragAttackOffThreshRate,
       "apBadIpOffThresh": apBadIpOffThresh,
       "apBadIpOffThreshRate": apBadIpOffThreshRate,
       "apBadTcpOffThresh": apBadTcpOffThresh,
       "apBadTcpOffThreshRate": apBadTcpOffThreshRate,
       "apBadUdpOffThresh": apBadUdpOffThresh,
       "apBadUdpOffThreshRate": apBadUdpOffThreshRate,
       "apBadIcmpOffThresh": apBadIcmpOffThresh,
       "apBadIcmpOffThreshRate": apBadIcmpOffThreshRate,
       "apBadOtherIpOffThresh": apBadOtherIpOffThresh,
       "apBadOtherIpOffThreshRate": apBadOtherIpOffThreshRate,
       "apOverloadedIpOffThresh": apOverloadedIpOffThresh,
       "apOverloadedIpOffThreshRate": apOverloadedIpOffThreshRate,
       "apIncidentAlertThreshold": apIncidentAlertThreshold,
       "apBandwidthAlertThresh": apBandwidthAlertThresh,
       "apBandwidthAlertThreshRate": apBandwidthAlertThreshRate,
       "apFloodAlertThresh": apFloodAlertThresh,
       "apFloodAlertThreshRate": apFloodAlertThreshRate,
       "apBlockedProtoAlertThresh": apBlockedProtoAlertThresh,
       "apBlockedProtoAlertThreshRate": apBlockedProtoAlertThreshRate,
       "apBlockedStateAlertThresh": apBlockedStateAlertThresh,
       "apBlockedStateAlertThreshRate": apBlockedStateAlertThreshRate,
       "apIpAttackAlertThresh": apIpAttackAlertThresh,
       "apIpAttackAlertThreshRate": apIpAttackAlertThreshRate,
       "apTcpAttackAlertThresh": apTcpAttackAlertThresh,
       "apTcpAttackAlertThreshRate": apTcpAttackAlertThreshRate,
       "apUdpAttackAlertThresh": apUdpAttackAlertThresh,
       "apUdpAttackAlertThreshRate": apUdpAttackAlertThreshRate,
       "apIcmpAttackAlertThresh": apIcmpAttackAlertThresh,
       "apIcmpAttackAlertThreshRate": apIcmpAttackAlertThreshRate,
       "apOtherIpAttackAlertThresh": apOtherIpAttackAlertThresh,
       "apOtherIpAttackAlertThreshRate": apOtherIpAttackAlertThreshRate,
       "apFragAttackAlertThresh": apFragAttackAlertThresh,
       "apFragAttackAlertThreshRate": apFragAttackAlertThreshRate,
       "apBadIpAlertThresh": apBadIpAlertThresh,
       "apBadIpAlertThreshRate": apBadIpAlertThreshRate,
       "apBadTcpAlertThresh": apBadTcpAlertThresh,
       "apBadTcpAlertThreshRate": apBadTcpAlertThreshRate,
       "apBadUdpAlertThresh": apBadUdpAlertThresh,
       "apBadUdpAlertThreshRate": apBadUdpAlertThreshRate,
       "apBadIcmpAlertThresh": apBadIcmpAlertThresh,
       "apBadIcmpAlertThreshRate": apBadIcmpAlertThreshRate,
       "apBadOtherIpAlertThresh": apBadOtherIpAlertThresh,
       "apBadOtherIpAlertThreshRate": apBadOtherIpAlertThreshRate,
       "apOverloadedIpAlertThresh": apOverloadedIpAlertThresh,
       "apOverloadedIpAlertThreshRate": apOverloadedIpAlertThreshRate,
       "apMail": apMail,
       "apMailServer": apMailServer,
       "apMailFrom": apMailFrom,
       "apMailSubject": apMailSubject,
       "apMailToList": apMailToList,
       "apMailDailyStats": apMailDailyStats,
       "apMailAlerts": apMailAlerts,
       "apMailAlertInterval": apMailAlertInterval,
       "apDebugConfig": apDebugConfig,
       "apDebugBandwidthFlag": apDebugBandwidthFlag,
       "apDebugFloodFlag": apDebugFloodFlag,
       "apDebugBlockedProtocolFlag": apDebugBlockedProtocolFlag,
       "apDebugBlockedStateFlag": apDebugBlockedStateFlag,
       "apDebugIpAttackFlag": apDebugIpAttackFlag,
       "apDebugTcpAttackFlag": apDebugTcpAttackFlag,
       "apDebugUdpAttackFlag": apDebugUdpAttackFlag,
       "apDebugIcmpAttackFlag": apDebugIcmpAttackFlag,
       "apDebugOtherIpAttackFlag": apDebugOtherIpAttackFlag,
       "apDebugFragmentAttackFlag": apDebugFragmentAttackFlag,
       "apDebugBadIpPacketFlag": apDebugBadIpPacketFlag,
       "apDebugBadTcpPacketFlag": apDebugBadTcpPacketFlag,
       "apDebugBadUdpPacketFlag": apDebugBadUdpPacketFlag,
       "apDebugBadIcmpFlag": apDebugBadIcmpFlag,
       "apDebugBadOtherIpFlag": apDebugBadOtherIpFlag,
       "apDebugOverloadProtectedIpFlag": apDebugOverloadProtectedIpFlag,
       "apOperationMode": apOperationMode,
       "apNtpServerList": apNtpServerList,
       "apTimeZone": apTimeZone,
       "apProtectedIpNetwork": apProtectedIpNetwork,
       "apSnmp": apSnmp,
       "apSnmpRoCommunity": apSnmpRoCommunity,
       "apSnmpTrapCommunity": apSnmpTrapCommunity,
       "apSnmpTrapIpAddressList": apSnmpTrapIpAddressList,
       "apAutoBlackList": apAutoBlackList,
       "apAutoblockEnable": apAutoblockEnable,
       "apAutoblockRateT1": apAutoblockRateT1,
       "apAutoblockRateT2": apAutoblockRateT2,
       "apProtectedIpAutodetect": apProtectedIpAutodetect,
       "apTrackIndeterminate": apTrackIndeterminate,
       "apState": apState,
       "apDefenseFlags": apDefenseFlags,
       "apBandwidth": apBandwidth,
       "apFlood": apFlood,
       "apBlockedProtocol": apBlockedProtocol,
       "apBlockedState": apBlockedState,
       "apIpAttack": apIpAttack,
       "apTcpAttack": apTcpAttack,
       "apUdpAttack": apUdpAttack,
       "apIcmpAttack": apIcmpAttack,
       "apOtherIpAttack": apOtherIpAttack,
       "apFragAttack": apFragAttack,
       "apBadIp": apBadIp,
       "apBadTcp": apBadTcp,
       "apBadUdp": apBadUdp,
       "apBadIcmp": apBadIcmp,
       "apBadOtherIp": apBadOtherIp,
       "apOverloadedIp": apOverloadedIp,
       "apTcpStates": apTcpStates,
       "apInSyn": apInSyn,
       "apOutSyn": apOutSyn,
       "apInSynAck": apInSynAck,
       "apOutSynAck": apOutSynAck,
       "apInSynSyn": apInSynSyn,
       "apOutSynSyn": apOutSynSyn,
       "apInEst": apInEst,
       "apOutEst": apOutEst,
       "apInFin1Src": apInFin1Src,
       "apOutFin1Src": apOutFin1Src,
       "apInFin2Src": apInFin2Src,
       "apOutFin2Src": apOutFin2Src,
       "apInFin3Src": apInFin3Src,
       "apOutFin3Src": apOutFin3Src,
       "apInFinFin": apInFinFin,
       "apOutFinFin": apOutFinFin,
       "apInFin1Dst": apInFin1Dst,
       "apOutFin1Dst": apOutFin1Dst,
       "apInFin2Dst": apInFin2Dst,
       "apOutFin2Dst": apOutFin2Dst,
       "apInFin3Dst": apInFin3Dst,
       "apOutFin3Dst": apOutFin3Dst,
       "apInCls": apInCls,
       "apOutCls": apOutCls,
       "apInRst": apInRst,
       "apOutRst": apOutRst,
       "apInRstCls": apInRstCls,
       "apOutRstCls": apOutRstCls,
       "apInUnknown": apInUnknown,
       "apOutUnknown": apOutUnknown,
       "apInAck": apInAck,
       "apOutAck": apOutAck,
       "apInPendAck": apInPendAck,
       "apOutPendAck": apOutPendAck,
       "apInGet": apInGet,
       "apOutGet": apOutGet,
       "apInGets": apInGets,
       "apOutGets": apOutGets,
       "apInTotalBpsAvg": apInTotalBpsAvg,
       "apOutTotalBpsAvg": apOutTotalBpsAvg,
       "apInTotalPpsAvg": apInTotalPpsAvg,
       "apOutTotalPpsAvg": apOutTotalPpsAvg,
       "apInSmallPpsAvg": apInSmallPpsAvg,
       "apOutSmallPpsAvg": apOutSmallPpsAvg,
       "apInMediumPpsAvg": apInMediumPpsAvg,
       "apOutMediumPpsAvg": apOutMediumPpsAvg,
       "apInLargePpsAvg": apInLargePpsAvg,
       "apOutLargePpsAvg": apOutLargePpsAvg,
       "apInDroppedBpsAvg": apInDroppedBpsAvg,
       "apOutDroppedBpsAvg": apOutDroppedBpsAvg,
       "apInDroppedPpsAvg": apInDroppedPpsAvg,
       "apOutDroppedPpsAvg": apOutDroppedPpsAvg,
       "apInCharmDroppedBpsAvg": apInCharmDroppedBpsAvg,
       "apOutCharmDroppedBpsAvg": apOutCharmDroppedBpsAvg,
       "apInFilteredBwthPercentAvg": apInFilteredBwthPercentAvg,
       "apOutFilteredBwthPercentAvg": apOutFilteredBwthPercentAvg,
       "apInSynbacklogtallyAvg": apInSynbacklogtallyAvg,
       "apOutSynbacklogtallyAvg": apOutSynbacklogtallyAvg,
       "apInConnectionAvg": apInConnectionAvg,
       "apOutConnectionAvg": apOutConnectionAvg,
       "apInConnreqAvg": apInConnreqAvg,
       "apOutConnreqAvg": apOutConnreqAvg,
       "apInActiveHttpGetsAvg": apInActiveHttpGetsAvg,
       "apOutActiveHttpGetsAvg": apOutActiveHttpGetsAvg,
       "apInProtectBwthPktsAvg": apInProtectBwthPktsAvg,
       "apOutProtectBwthPktsAvg": apOutProtectBwthPktsAvg,
       "apInFloodPktsAvg": apInFloodPktsAvg,
       "apOutFloodPktsAvg": apOutFloodPktsAvg,
       "apInBlockedProtocolPktsAvg": apInBlockedProtocolPktsAvg,
       "apOutBlockedProtocolPktsAvg": apOutBlockedProtocolPktsAvg,
       "apInBlockedStatePktsAvg": apInBlockedStatePktsAvg,
       "apOutBlockedStatePktsAvg": apOutBlockedStatePktsAvg,
       "apInIpAttackPktsAvg": apInIpAttackPktsAvg,
       "apOutIpAttackPktsAvg": apOutIpAttackPktsAvg,
       "apInTcpAttackPktsAvg": apInTcpAttackPktsAvg,
       "apOutTcpAttackPktsAvg": apOutTcpAttackPktsAvg,
       "apInUdpAttackPktsAvg": apInUdpAttackPktsAvg,
       "apOutUdpAttackPktsAvg": apOutUdpAttackPktsAvg,
       "apInIcmpAttackPktsAvg": apInIcmpAttackPktsAvg,
       "apOutIcmpAttackPktsAvg": apOutIcmpAttackPktsAvg,
       "apInOtherIpAttackPktsAvg": apInOtherIpAttackPktsAvg,
       "apOutOtherIpAttackPktsAvg": apOutOtherIpAttackPktsAvg,
       "apInFragmentAttackPktsAvg": apInFragmentAttackPktsAvg,
       "apOutFragmentAttackPktsAvg": apOutFragmentAttackPktsAvg,
       "apInBadipPktsAvg": apInBadipPktsAvg,
       "apOutBadipPktsAvg": apOutBadipPktsAvg,
       "apInBadTcpPktsAvg": apInBadTcpPktsAvg,
       "apOutBadTcpPktsAvg": apOutBadTcpPktsAvg,
       "apInBadUdpPktsAvg": apInBadUdpPktsAvg,
       "apOutBadUdpPktsAvg": apOutBadUdpPktsAvg,
       "apInBadIcmpPktsAvg": apInBadIcmpPktsAvg,
       "apOutBadIcmpPktsAvg": apOutBadIcmpPktsAvg,
       "apInBadOtherIpPktsAvg": apInBadOtherIpPktsAvg,
       "apOutBadOtherIpPktsAvg": apOutBadOtherIpPktsAvg,
       "apInOverloadedAvg": apInOverloadedAvg,
       "apOutOverloadedAvg": apOutOverloadedAvg,
       "apInLatencyAvg": apInLatencyAvg,
       "apOutLatencyAvg": apOutLatencyAvg,
       "apInSmallPpsMax": apInSmallPpsMax,
       "apOutSmallPpsMax": apOutSmallPpsMax,
       "apInMediumPpsMax": apInMediumPpsMax,
       "apOutMediumPpsMax": apOutMediumPpsMax,
       "apInLargePpsMax": apInLargePpsMax,
       "apOutLargePpsMax": apOutLargePpsMax,
       "apInFilteredBwthPercentMax": apInFilteredBwthPercentMax,
       "apOutFilteredBwthPercentMax": apOutFilteredBwthPercentMax,
       "apInSynbacklogtallyMax": apInSynbacklogtallyMax,
       "apOutSynbacklogtallyMax": apOutSynbacklogtallyMax,
       "apInConnectionMax": apInConnectionMax,
       "apOutConnectionMax": apOutConnectionMax,
       "apInConnreqMax": apInConnreqMax,
       "apOutConnreqMax": apOutConnreqMax,
       "apInActiveHttpGetsMax": apInActiveHttpGetsMax,
       "apOutActiveHttpGetsMax": apOutActiveHttpGetsMax,
       "apInProtectBwthPktsMax": apInProtectBwthPktsMax,
       "apOutProtectBwthPktsMax": apOutProtectBwthPktsMax,
       "apInFloodPktsMax": apInFloodPktsMax,
       "apOutFloodPktsMax": apOutFloodPktsMax,
       "apInBlockedProtocolPktsMax": apInBlockedProtocolPktsMax,
       "apOutBlockedProtocolPktsMax": apOutBlockedProtocolPktsMax,
       "apInBlockedStatePktsMax": apInBlockedStatePktsMax,
       "apOutBlockedStatePktsMax": apOutBlockedStatePktsMax,
       "apInIpAttackPktsMax": apInIpAttackPktsMax,
       "apOutIpAttackPktsMax": apOutIpAttackPktsMax,
       "apInTcpAttackPktsMax": apInTcpAttackPktsMax,
       "apOutTcpAttackPktsMax": apOutTcpAttackPktsMax,
       "apInUdpAttackPktsMax": apInUdpAttackPktsMax,
       "apOutUdpAttackPktsMax": apOutUdpAttackPktsMax,
       "apInIcmpAttackPktsMax": apInIcmpAttackPktsMax,
       "apOutIcmpAttackPktsMax": apOutIcmpAttackPktsMax,
       "apInOtherIpAttackPktsMax": apInOtherIpAttackPktsMax,
       "apOutOtherIpAttackPktsMax": apOutOtherIpAttackPktsMax,
       "apInFragmentAttackPktsMax": apInFragmentAttackPktsMax,
       "apOutFragmentAttackPktsMax": apOutFragmentAttackPktsMax,
       "apInBadipPktsMax": apInBadipPktsMax,
       "apOutBadipPktsMax": apOutBadipPktsMax,
       "apInBadTcpPktsMax": apInBadTcpPktsMax,
       "apOutBadTcpPktsMax": apOutBadTcpPktsMax,
       "apInBadUdpPktsMax": apInBadUdpPktsMax,
       "apOutBadUdpPktsMax": apOutBadUdpPktsMax,
       "apInBadIcmpPktsMax": apInBadIcmpPktsMax,
       "apOutBadIcmpPktsMax": apOutBadIcmpPktsMax,
       "apInBadOtherIpPktsMax": apInBadOtherIpPktsMax,
       "apOutBadOtherIpPktsMax": apOutBadOtherIpPktsMax,
       "apInOverloadedMax": apInOverloadedMax,
       "apOutOverloadedMax": apOutOverloadedMax,
       "apInLatencyMax": apInLatencyMax,
       "apOutLatencyMax": apOutLatencyMax,
       "apIfStates": apIfStates,
       "apMgmtIfLinkModeState": apMgmtIfLinkModeState,
       "apIntIfLinkModeState": apIntIfLinkModeState,
       "apProtIfLinkModeState": apProtIfLinkModeState,
       "apMgmtIfLinkFCState": apMgmtIfLinkFCState,
       "apIntIfLinkFCState": apIntIfLinkFCState,
       "apProtIfLinkFCState": apProtIfLinkFCState,
       "apHighAvailabilityInfo": apHighAvailabilityInfo,
       "apHaState": apHaState,
       "apHaPartnerList": apHaPartnerList,
       "apHaPartnerTime": apHaPartnerTime,
       "apStalledFlag": apStalledFlag,
       "apOutputErrorIIFlag": apOutputErrorIIFlag,
       "apOutputErrorPIFlag": apOutputErrorPIFlag,
       "apOutputErrorMIFlag": apOutputErrorMIFlag,
       "apNewConfigFlag": apNewConfigFlag,
       "apNotLicensedFlag": apNotLicensedFlag,
       "apMacTableFullFlag": apMacTableFullFlag,
       "apProtectedTableFullFlag": apProtectedTableFullFlag,
       "apIncidentTableFullFlag": apIncidentTableFullFlag,
       "apTcpTableFullFlag": apTcpTableFullFlag,
       "apUdpTableFullFlag": apUdpTableFullFlag,
       "apIcmpTableFullFlag": apIcmpTableFullFlag,
       "apOtherIpTableFullFlag": apOtherIpTableFullFlag,
       "apFragTableFullFlag": apFragTableFullFlag,
       "apFtpTableFullFlag": apFtpTableFullFlag,
       "apBlockedTableFullFlag": apBlockedTableFullFlag,
       "apShortCircuitFlag": apShortCircuitFlag,
       "apInternetIfDisconnectedFlag": apInternetIfDisconnectedFlag,
       "apProtectedIfDisconnectedFlag": apProtectedIfDisconnectedFlag,
       "apMgmtIfDisconnectedFlag": apMgmtIfDisconnectedFlag,
       "apUpgradingFlag": apUpgradingFlag,
       "apProtectedIfTrafficFlag": apProtectedIfTrafficFlag,
       "apRoutingLoopFlag": apRoutingLoopFlag,
       "apOfflineFlag": apOfflineFlag,
       "apStateLearningFlag": apStateLearningFlag,
       "apSupportExpiredFlag": apSupportExpiredFlag,
       "apSevereLoadingFlag": apSevereLoadingFlag,
       "apMacMisconfiguredFlag": apMacMisconfiguredFlag,
       "apIfMisconfiguredFlag": apIfMisconfiguredFlag,
       "apInternetIfLinkDownFlag": apInternetIfLinkDownFlag,
       "apProtectedIfLinkDownFlag": apProtectedIfLinkDownFlag,
       "apDatashareIfDisconnectedFlag": apDatashareIfDisconnectedFlag,
       "apDiskFailingFlag": apDiskFailingFlag,
       "apPsuFailingFlag": apPsuFailingFlag,
       "apFanFailingFlag": apFanFailingFlag,
       "apConfigXferFailFlag": apConfigXferFailFlag,
       "apMissingRequiredPartnerFlag": apMissingRequiredPartnerFlag,
       "apBgpMisconfiguredIpFlag": apBgpMisconfiguredIpFlag,
       "apStats": apStats,
       "apSessionTallies": apSessionTallies,
       "apInTcpConnTally": apInTcpConnTally,
       "apOutTcpConnTally": apOutTcpConnTally,
       "apInSynBacklogTally": apInSynBacklogTally,
       "apUdpSessionTally": apUdpSessionTally,
       "apIcmpSessionTally": apIcmpSessionTally,
       "apOtherIpSessionTally": apOtherIpSessionTally,
       "apSummaryBytes": apSummaryBytes,
       "apInTotalBytesCnt": apInTotalBytesCnt,
       "apOutTotalBytesCnt": apOutTotalBytesCnt,
       "apInDroppedBytesCnt": apInDroppedBytesCnt,
       "apOutDroppedBytesCnt": apOutDroppedBytesCnt,
       "apInCharmDroppedBytesCnt": apInCharmDroppedBytesCnt,
       "apOutCharmDroppedBytesCnt": apOutCharmDroppedBytesCnt,
       "apSummaryPpsRates": apSummaryPpsRates,
       "apInTotalPpsMax": apInTotalPpsMax,
       "apOutTotalPpsMax": apOutTotalPpsMax,
       "apInDroppedPpsMax": apInDroppedPpsMax,
       "apOutDroppedPpsMax": apOutDroppedPpsMax,
       "apSummaryBpsRates": apSummaryBpsRates,
       "apInTotalBpsMax": apInTotalBpsMax,
       "apOutTotalBpsMax": apOutTotalBpsMax,
       "apInDroppedBpsMax": apInDroppedBpsMax,
       "apOutDroppedBpsMax": apOutDroppedBpsMax,
       "apInCharmDroppedBpsMax": apInCharmDroppedBpsMax,
       "apOutCharmDroppedBpsMax": apOutCharmDroppedBpsMax,
       "apAttackPkts": apAttackPkts,
       "apInProtectBwthPktsCnt": apInProtectBwthPktsCnt,
       "apOutProtectBwthPktsCnt": apOutProtectBwthPktsCnt,
       "apInFloodPktsCnt": apInFloodPktsCnt,
       "apOutFloodPktsCnt": apOutFloodPktsCnt,
       "apInBlockedProtocolPktsCnt": apInBlockedProtocolPktsCnt,
       "apOutBlockedProtocolPktsCnt": apOutBlockedProtocolPktsCnt,
       "apInBlockedStatePktsCnt": apInBlockedStatePktsCnt,
       "apOutBlockedStatePktsCnt": apOutBlockedStatePktsCnt,
       "apInIpAttackPktsCnt": apInIpAttackPktsCnt,
       "apOutIpAttackPktsCnt": apOutIpAttackPktsCnt,
       "apInTcpAttackPktsCnt": apInTcpAttackPktsCnt,
       "apOutTcpAttackPktsCnt": apOutTcpAttackPktsCnt,
       "apInUdpAttackPktsCnt": apInUdpAttackPktsCnt,
       "apOutUdpAttackPktsCnt": apOutUdpAttackPktsCnt,
       "apInIcmpAttackPktsCnt": apInIcmpAttackPktsCnt,
       "apOutIcmpAttackPktsCnt": apOutIcmpAttackPktsCnt,
       "apInOtherIpAttackPktsCnt": apInOtherIpAttackPktsCnt,
       "apOutOtherIpAttackPktsCnt": apOutOtherIpAttackPktsCnt,
       "apInFragmentAttackPktsCnt": apInFragmentAttackPktsCnt,
       "apOutFragmentAttackPktsCnt": apOutFragmentAttackPktsCnt,
       "apInBadIpPktsCnt": apInBadIpPktsCnt,
       "apOutBadIpPktsCnt": apOutBadIpPktsCnt,
       "apInBadTcpPktsCnt": apInBadTcpPktsCnt,
       "apOutBadTcpPktsCnt": apOutBadTcpPktsCnt,
       "apInBadUdpPktsCnt": apInBadUdpPktsCnt,
       "apOutBadUdpPktsCnt": apOutBadUdpPktsCnt,
       "apInBadIcmpPktsCnt": apInBadIcmpPktsCnt,
       "apOutBadIcmpPktsCnt": apOutBadIcmpPktsCnt,
       "apInBadOtherIpPktsCnt": apInBadOtherIpPktsCnt,
       "apOutBadOtherIpPktsCnt": apOutBadOtherIpPktsCnt,
       "apInTotalPpsCnt": apInTotalPpsCnt,
       "apOutTotalPpsCnt": apOutTotalPpsCnt,
       "apInSmallPpsCnt": apInSmallPpsCnt,
       "apOutSmallPpsCnt": apOutSmallPpsCnt,
       "apInMediumPpsCnt": apInMediumPpsCnt,
       "apOutMediumPpsCnt": apOutMediumPpsCnt,
       "apInLargePpsCnt": apInLargePpsCnt,
       "apOutLargePpsCnt": apOutLargePpsCnt,
       "apInDroppedPpsCnt": apInDroppedPpsCnt,
       "apOutDroppedPpsCnt": apOutDroppedPpsCnt,
       "apInFilteredBwthPercentCnt": apInFilteredBwthPercentCnt,
       "apOutFilteredBwthPercentCnt": apOutFilteredBwthPercentCnt,
       "apInConnreqCnt": apInConnreqCnt,
       "apOutConnreqCnt": apOutConnreqCnt,
       "apInOverloadedCnt": apInOverloadedCnt,
       "apOutOverloadedCnt": apOutOverloadedCnt,
       "apWorstOffenderTable": apWorstOffenderTable,
       "apWorstOffenderEntry": apWorstOffenderEntry,
       "apWorstOffenderInetAddressType": apWorstOffenderInetAddressType,
       "apWorstOffenderInetAddress": apWorstOffenderInetAddress,
       "apWorstOffenderReason": apWorstOffenderReason,
       "apWorstOffenderLastTime": apWorstOffenderLastTime,
       "apWorstOffenderCount": apWorstOffenderCount,
       "apLogFileTable": apLogFileTable,
       "apLogFileEntry": apLogFileEntry,
       "apLogFileRecordNumber": apLogFileRecordNumber,
       "apLogFileRecord": apLogFileRecord,
       "apIncidentTable": apIncidentTable,
       "apIncidentEntry": apIncidentEntry,
       "apIncidentYear": apIncidentYear,
       "apIncidentMonth": apIncidentMonth,
       "apIncidentDay": apIncidentDay,
       "apIncidentNumber": apIncidentNumber,
       "apIncidentStart": apIncidentStart,
       "apIncidentAddress": apIncidentAddress,
       "apIncidentType": apIncidentType,
       "apIncidentDirection": apIncidentDirection,
       "apIncidentPeakRate": apIncidentPeakRate,
       "apIncidentDropped": apIncidentDropped,
       "jddsPortal": jddsPortal,
       "poStatsTable": poStatsTable,
       "poStatsEntry": poStatsEntry,
       "poStatsIndex": poStatsIndex,
       "poPortalName": poPortalName,
       "poInTotalBpsAvg": poInTotalBpsAvg,
       "poOutTotalBpsAvg": poOutTotalBpsAvg,
       "poInTotalPpsAvg": poInTotalPpsAvg,
       "poOutTotalPpsAvg": poOutTotalPpsAvg,
       "poInSmallPpsAvg": poInSmallPpsAvg,
       "poOutSmallPpsAvg": poOutSmallPpsAvg,
       "poInMediumPpsAvg": poInMediumPpsAvg,
       "poOutMediumPpsAvg": poOutMediumPpsAvg,
       "poInLargePpsAvg": poInLargePpsAvg,
       "poOutLargePpsAvg": poOutLargePpsAvg,
       "poInDroppedBpsAvg": poInDroppedBpsAvg,
       "poOutDroppedBpsAvg": poOutDroppedBpsAvg,
       "poInDroppedPpsAvg": poInDroppedPpsAvg,
       "poOutDroppedPpsAvg": poOutDroppedPpsAvg,
       "poInCharmDroppedBpsAvg": poInCharmDroppedBpsAvg,
       "poOutCharmDroppedBpsAvg": poOutCharmDroppedBpsAvg,
       "poInFilteredBwthPercentAvg": poInFilteredBwthPercentAvg,
       "poOutFilteredBwthPercentAvg": poOutFilteredBwthPercentAvg,
       "poInSynbacklogtallyAvg": poInSynbacklogtallyAvg,
       "poOutSynbacklogtallyAvg": poOutSynbacklogtallyAvg,
       "poInConnectionAvg": poInConnectionAvg,
       "poOutConnectionAvg": poOutConnectionAvg,
       "poInConnreqAvg": poInConnreqAvg,
       "poOutConnreqAvg": poOutConnreqAvg,
       "poInActiveHttpGetsAvg": poInActiveHttpGetsAvg,
       "poOutActiveHttpGetsAvg": poOutActiveHttpGetsAvg,
       "poInProtectBwthPktsAvg": poInProtectBwthPktsAvg,
       "poOutProtectBwthPktsAvg": poOutProtectBwthPktsAvg,
       "poInFloodPktsAvg": poInFloodPktsAvg,
       "poOutFloodPktsAvg": poOutFloodPktsAvg,
       "poInBlockedProtocolPktsAvg": poInBlockedProtocolPktsAvg,
       "poOutBlockedProtocolPktsAvg": poOutBlockedProtocolPktsAvg,
       "poInBlockedStatePktsAvg": poInBlockedStatePktsAvg,
       "poOutBlockedStatePktsAvg": poOutBlockedStatePktsAvg,
       "poInIpAttackPktsAvg": poInIpAttackPktsAvg,
       "poOutIpAttackPktsAvg": poOutIpAttackPktsAvg,
       "poInTcpAttackPktsAvg": poInTcpAttackPktsAvg,
       "poOutTcpAttackPktsAvg": poOutTcpAttackPktsAvg,
       "poInUdpAttackPktsAvg": poInUdpAttackPktsAvg,
       "poOutUdpAttackPktsAvg": poOutUdpAttackPktsAvg,
       "poInIcmpAttackPktsAvg": poInIcmpAttackPktsAvg,
       "poOutIcmpAttackPktsAvg": poOutIcmpAttackPktsAvg,
       "poInOtherIpAttackPktsAvg": poInOtherIpAttackPktsAvg,
       "poOutOtherIpAttackPktsAvg": poOutOtherIpAttackPktsAvg,
       "poInFragmentAttackPktsAvg": poInFragmentAttackPktsAvg,
       "poOutFragmentAttackPktsAvg": poOutFragmentAttackPktsAvg,
       "poInBadipPktsAvg": poInBadipPktsAvg,
       "poOutBadipPktsAvg": poOutBadipPktsAvg,
       "poInBadTcpPktsAvg": poInBadTcpPktsAvg,
       "poOutBadTcpPktsAvg": poOutBadTcpPktsAvg,
       "poInBadUdpPktsAvg": poInBadUdpPktsAvg,
       "poOutBadUdpPktsAvg": poOutBadUdpPktsAvg,
       "poInBadIcmpPktsAvg": poInBadIcmpPktsAvg,
       "poOutBadIcmpPktsAvg": poOutBadIcmpPktsAvg,
       "poInBadOtherIpPktsAvg": poInBadOtherIpPktsAvg,
       "poOutBadOtherIpPktsAvg": poOutBadOtherIpPktsAvg,
       "poInOverloadedAvg": poInOverloadedAvg,
       "poOutOverloadedAvg": poOutOverloadedAvg,
       "poInLatencyAvg": poInLatencyAvg,
       "poOutLatencyAvg": poOutLatencyAvg,
       "poInTotalBpsMax": poInTotalBpsMax,
       "poOutTotalBpsMax": poOutTotalBpsMax,
       "poInTotalPpsMax": poInTotalPpsMax,
       "poOutTotalPpsMax": poOutTotalPpsMax,
       "poInSmallPpsMax": poInSmallPpsMax,
       "poOutSmallPpsMax": poOutSmallPpsMax,
       "poInMediumPpsMax": poInMediumPpsMax,
       "poOutMediumPpsMax": poOutMediumPpsMax,
       "poInLargePpsMax": poInLargePpsMax,
       "poOutLargePpsMax": poOutLargePpsMax,
       "poInDroppedBpsMax": poInDroppedBpsMax,
       "poOutDroppedBpsMax": poOutDroppedBpsMax,
       "poInDroppedPpsMax": poInDroppedPpsMax,
       "poOutDroppedPpsMax": poOutDroppedPpsMax,
       "poInCharmDroppedBpsMax": poInCharmDroppedBpsMax,
       "poOutCharmDroppedBpsMax": poOutCharmDroppedBpsMax,
       "poInFilteredBwthPercentMax": poInFilteredBwthPercentMax,
       "poOutFilteredBwthPercentMax": poOutFilteredBwthPercentMax,
       "poInSynbacklogtallyMax": poInSynbacklogtallyMax,
       "poOutSynbacklogtallyMax": poOutSynbacklogtallyMax,
       "poInConnectionMax": poInConnectionMax,
       "poOutConnectionMax": poOutConnectionMax,
       "poInConnreqMax": poInConnreqMax,
       "poOutConnreqMax": poOutConnreqMax,
       "poInActiveHttpGetsMax": poInActiveHttpGetsMax,
       "poOutActiveHttpGetsMax": poOutActiveHttpGetsMax,
       "poInProtectBwthPktsMax": poInProtectBwthPktsMax,
       "poOutProtectBwthPktsMax": poOutProtectBwthPktsMax,
       "poInFloodPktsMax": poInFloodPktsMax,
       "poOutFloodPktsMax": poOutFloodPktsMax,
       "poInBlockedProtocolPktsMax": poInBlockedProtocolPktsMax,
       "poOutBlockedProtocolPktsMax": poOutBlockedProtocolPktsMax,
       "poInBlockedStatePktsMax": poInBlockedStatePktsMax,
       "poOutBlockedStatePktsMax": poOutBlockedStatePktsMax,
       "poInIpAttackPktsMax": poInIpAttackPktsMax,
       "poOutIpAttackPktsMax": poOutIpAttackPktsMax,
       "poInTcpAttackPktsMax": poInTcpAttackPktsMax,
       "poOutTcpAttackPktsMax": poOutTcpAttackPktsMax,
       "poInUdpAttackPktsMax": poInUdpAttackPktsMax,
       "poOutUdpAttackPktsMax": poOutUdpAttackPktsMax,
       "poInIcmpAttackPktsMax": poInIcmpAttackPktsMax,
       "poOutIcmpAttackPktsMax": poOutIcmpAttackPktsMax,
       "poInOtherIpAttackPktsMax": poInOtherIpAttackPktsMax,
       "poOutOtherIpAttackPktsMax": poOutOtherIpAttackPktsMax,
       "poInFragmentAttackPktsMax": poInFragmentAttackPktsMax,
       "poOutFragmentAttackPktsMax": poOutFragmentAttackPktsMax,
       "poInBadipPktsMax": poInBadipPktsMax,
       "poOutBadipPktsMax": poOutBadipPktsMax,
       "poInBadTcpPktsMax": poInBadTcpPktsMax,
       "poOutBadTcpPktsMax": poOutBadTcpPktsMax,
       "poInBadUdpPktsMax": poInBadUdpPktsMax,
       "poOutBadUdpPktsMax": poOutBadUdpPktsMax,
       "poInBadIcmpPktsMax": poInBadIcmpPktsMax,
       "poOutBadIcmpPktsMax": poOutBadIcmpPktsMax,
       "poInBadOtherIpPktsMax": poInBadOtherIpPktsMax,
       "poOutBadOtherIpPktsMax": poOutBadOtherIpPktsMax,
       "poInOverloadedMax": poInOverloadedMax,
       "poOutOverloadedMax": poOutOverloadedMax,
       "poInLatencyMax": poInLatencyMax,
       "poOutLatencyMax": poOutLatencyMax,
       "poInTotalBytesCnt": poInTotalBytesCnt,
       "poOutTotalBytesCnt": poOutTotalBytesCnt,
       "poInDroppedBytesCnt": poInDroppedBytesCnt,
       "poOutDroppedBytesCnt": poOutDroppedBytesCnt,
       "poInCharmDroppedBytesCnt": poInCharmDroppedBytesCnt,
       "poOutCharmDroppedBytesCnt": poOutCharmDroppedBytesCnt,
       "poInTotalPpsCnt": poInTotalPpsCnt,
       "poOutTotalPpsCnt": poOutTotalPpsCnt,
       "poInSmallPpsCnt": poInSmallPpsCnt,
       "poOutSmallPpsCnt": poOutSmallPpsCnt,
       "poInMediumPpsCnt": poInMediumPpsCnt,
       "poOutMediumPpsCnt": poOutMediumPpsCnt,
       "poInLargePpsCnt": poInLargePpsCnt,
       "poOutLargePpsCnt": poOutLargePpsCnt,
       "poInDroppedPpsCnt": poInDroppedPpsCnt,
       "poOutDroppedPpsCnt": poOutDroppedPpsCnt,
       "poInFilteredBwthPercentCnt": poInFilteredBwthPercentCnt,
       "poOutFilteredBwthPercentCnt": poOutFilteredBwthPercentCnt,
       "poInConnreqCnt": poInConnreqCnt,
       "poOutConnreqCnt": poOutConnreqCnt,
       "poIncidentTable": poIncidentTable,
       "poIncidentEntry": poIncidentEntry,
       "poIncidentYear": poIncidentYear,
       "poIncidentMonth": poIncidentMonth,
       "poIncidentDay": poIncidentDay,
       "poIncidentNumber": poIncidentNumber,
       "poIncidentPortalName": poIncidentPortalName,
       "poIncidentStart": poIncidentStart,
       "poIncidentAddress": poIncidentAddress,
       "poIncidentType": poIncidentType,
       "poIncidentDirection": poIncidentDirection,
       "poIncidentPeakRate": poIncidentPeakRate,
       "poIncidentDropped": poIncidentDropped,
       "poFiltersTable": poFiltersTable,
       "poFiltersEntry": poFiltersEntry,
       "poFilterIndex": poFilterIndex,
       "poFilterName": poFilterName,
       "poTcpPortsList": poTcpPortsList,
       "poUdpPortsList": poUdpPortsList,
       "poIcmpTypesList": poIcmpTypesList,
       "poIpProtocolsList": poIpProtocolsList,
       "jddsProtected": jddsProtected,
       "prConfigTable": prConfigTable,
       "prConfigEntry": prConfigEntry,
       "prConfigInetAddressType": prConfigInetAddressType,
       "prConfigInetAddress": prConfigInetAddress,
       "prHostName": prHostName,
       "prTcpBacklog": prTcpBacklog,
       "prMaxConnections": prMaxConnections,
       "prMaxConnectionRate": prMaxConnectionRate,
       "prInFilterName": prInFilterName,
       "prOutFilterName": prOutFilterName,
       "prSendTcpRejects": prSendTcpRejects,
       "prTrackSoap": prTrackSoap,
       "prOperationMode": prOperationMode,
       "prMaxGets": prMaxGets,
       "prFragsDisabled": prFragsDisabled,
       "prStatsTable": prStatsTable,
       "prStatsEntry": prStatsEntry,
       "prInetAddressType": prInetAddressType,
       "prInetAddress": prInetAddress,
       "prBandwidth": prBandwidth,
       "prFlood": prFlood,
       "prBlockedProtocol": prBlockedProtocol,
       "prBlockedState": prBlockedState,
       "prIpAttack": prIpAttack,
       "prTcpAttack": prTcpAttack,
       "prUdpAttack": prUdpAttack,
       "prIcmpAttack": prIcmpAttack,
       "prOtherIpAttack": prOtherIpAttack,
       "prFragAttack": prFragAttack,
       "prBadIp": prBadIp,
       "prBadTcp": prBadTcp,
       "prBadUdp": prBadUdp,
       "prBadIcmp": prBadIcmp,
       "prBadOtherIp": prBadOtherIp,
       "prOverloaded": prOverloaded,
       "prInSyn": prInSyn,
       "prOutSyn": prOutSyn,
       "prInSynAck": prInSynAck,
       "prOutSynAck": prOutSynAck,
       "prInSynSyn": prInSynSyn,
       "prOutSynSyn": prOutSynSyn,
       "prInAck": prInAck,
       "prOutAck": prOutAck,
       "prInPendAck": prInPendAck,
       "prOutPendAck": prOutPendAck,
       "prInGet": prInGet,
       "prOutGet": prOutGet,
       "prInEst": prInEst,
       "prOutEst": prOutEst,
       "prInFin1Src": prInFin1Src,
       "prOutFin1Src": prOutFin1Src,
       "prInFin2Src": prInFin2Src,
       "prOutFin2Src": prOutFin2Src,
       "prInFin3Src": prInFin3Src,
       "prOutFin3Src": prOutFin3Src,
       "prInFinFin": prInFinFin,
       "prOutFinFin": prOutFinFin,
       "prInFin1Dst": prInFin1Dst,
       "prOutFin1Dst": prOutFin1Dst,
       "prInFin2Dst": prInFin2Dst,
       "prOutFin2Dst": prOutFin2Dst,
       "prInFin3Dst": prInFin3Dst,
       "prOutFin3Dst": prOutFin3Dst,
       "prInCls": prInCls,
       "prOutCls": prOutCls,
       "prInRst": prInRst,
       "prOutRst": prOutRst,
       "prInRstCls": prInRstCls,
       "prOutRstCls": prOutRstCls,
       "prInUnknown": prInUnknown,
       "prOutUnknown": prOutUnknown,
       "prInGets": prInGets,
       "prOutGets": prOutGets,
       "prOverloadedFlag": prOverloadedFlag,
       "prInTcpConnTally": prInTcpConnTally,
       "prOutTcpConnTally": prOutTcpConnTally,
       "prInSynBacklogTally": prInSynBacklogTally,
       "prInTotalBytesCnt": prInTotalBytesCnt,
       "prOutTotalBytesCnt": prOutTotalBytesCnt,
       "prInDroppedBytesCnt": prInDroppedBytesCnt,
       "prOutDroppedBytesCnt": prOutDroppedBytesCnt,
       "prInCharmDroppedBytesCnt": prInCharmDroppedBytesCnt,
       "prOutCharmDroppedBytesCnt": prOutCharmDroppedBytesCnt,
       "prInTotalPpsMax": prInTotalPpsMax,
       "prOutTotalPpsMax": prOutTotalPpsMax,
       "prInDroppedPpsMax": prInDroppedPpsMax,
       "prOutDroppedPpsMax": prOutDroppedPpsMax,
       "prInTotalBpsMax": prInTotalBpsMax,
       "prOutTotalBpsMax": prOutTotalBpsMax,
       "prInDroppedBpsMax": prInDroppedBpsMax,
       "prOutDroppedBpsMax": prOutDroppedBpsMax,
       "prInCharmDroppedBpsMax": prInCharmDroppedBpsMax,
       "prOutCharmDroppedBpsMax": prOutCharmDroppedBpsMax,
       "prInProtectBwthPktsCnt": prInProtectBwthPktsCnt,
       "prOutProtectBwthPktsCnt": prOutProtectBwthPktsCnt,
       "prInFloodPktsCnt": prInFloodPktsCnt,
       "prOutFloodPktsCnt": prOutFloodPktsCnt,
       "prInBlockedProtocolPktsCnt": prInBlockedProtocolPktsCnt,
       "prOutBlockedProtocolPktsCnt": prOutBlockedProtocolPktsCnt,
       "prInBlockedStatePktsCnt": prInBlockedStatePktsCnt,
       "prOutBlockedStatePktsCnt": prOutBlockedStatePktsCnt,
       "prInIpAttackPktsCnt": prInIpAttackPktsCnt,
       "prOutIpAttackPktsCnt": prOutIpAttackPktsCnt,
       "prInTcpAttackPktsCnt": prInTcpAttackPktsCnt,
       "prOutTcpAttackPktsCnt": prOutTcpAttackPktsCnt,
       "prInUdpAttackPktsCnt": prInUdpAttackPktsCnt,
       "prOutUdpAttackPktsCnt": prOutUdpAttackPktsCnt,
       "prInIcmpAttackPktsCnt": prInIcmpAttackPktsCnt,
       "prOutIcmpAttackPktsCnt": prOutIcmpAttackPktsCnt,
       "prInOtherIpAttackPktsCnt": prInOtherIpAttackPktsCnt,
       "prOutOtherIpAttackPktsCnt": prOutOtherIpAttackPktsCnt,
       "prInFragmentAttackPktsCnt": prInFragmentAttackPktsCnt,
       "prOutFragmentAttackPktsCnt": prOutFragmentAttackPktsCnt,
       "prInBadIpPktsCnt": prInBadIpPktsCnt,
       "prOutBadIpPktsCnt": prOutBadIpPktsCnt,
       "prInBadTcpPktsCnt": prInBadTcpPktsCnt,
       "prOutBadTcpPktsCnt": prOutBadTcpPktsCnt,
       "prInBadUdpPktsCnt": prInBadUdpPktsCnt,
       "prOutBadUdpPktsCnt": prOutBadUdpPktsCnt,
       "prInBadIcmpPktsCnt": prInBadIcmpPktsCnt,
       "prOutBadIcmpPktsCnt": prOutBadIcmpPktsCnt,
       "prInBadOtherIpPktsCnt": prInBadOtherIpPktsCnt,
       "prOutBadOtherIpPktsCnt": prOutBadOtherIpPktsCnt,
       "prInTotalBpsAvg": prInTotalBpsAvg,
       "prOutTotalBpsAvg": prOutTotalBpsAvg,
       "prInTotalPpsAvg": prInTotalPpsAvg,
       "prOutTotalPpsAvg": prOutTotalPpsAvg,
       "prInSmallPpsAvg": prInSmallPpsAvg,
       "prOutSmallPpsAvg": prOutSmallPpsAvg,
       "prInMediumPpsAvg": prInMediumPpsAvg,
       "prOutMediumPpsAvg": prOutMediumPpsAvg,
       "prInLargePpsAvg": prInLargePpsAvg,
       "prOutLargePpsAvg": prOutLargePpsAvg,
       "prInDroppedBpsAvg": prInDroppedBpsAvg,
       "prOutDroppedBpsAvg": prOutDroppedBpsAvg,
       "prInDroppedPpsAvg": prInDroppedPpsAvg,
       "prOutDroppedPpsAvg": prOutDroppedPpsAvg,
       "prInCharmDroppedBpsAvg": prInCharmDroppedBpsAvg,
       "prOutCharmDroppedBpsAvg": prOutCharmDroppedBpsAvg,
       "prInFilteredBwthPercentAvg": prInFilteredBwthPercentAvg,
       "prOutFilteredBwthPercentAvg": prOutFilteredBwthPercentAvg,
       "prInSynbacklogtallyAvg": prInSynbacklogtallyAvg,
       "prOutSynbacklogtallyAvg": prOutSynbacklogtallyAvg,
       "prInConnectionAvg": prInConnectionAvg,
       "prOutConnectionAvg": prOutConnectionAvg,
       "prInConnreqAvg": prInConnreqAvg,
       "prOutConnreqAvg": prOutConnreqAvg,
       "prInActiveHttpGetsAvg": prInActiveHttpGetsAvg,
       "prOutActiveHttpGetsAvg": prOutActiveHttpGetsAvg,
       "prInProtectBwthPktsAvg": prInProtectBwthPktsAvg,
       "prOutProtectBwthPktsAvg": prOutProtectBwthPktsAvg,
       "prInFloodPktsAvg": prInFloodPktsAvg,
       "prOutFloodPktsAvg": prOutFloodPktsAvg,
       "prInBlockedProtocolPktsAvg": prInBlockedProtocolPktsAvg,
       "prOutBlockedProtocolPktsAvg": prOutBlockedProtocolPktsAvg,
       "prInBlockedStatePktsAvg": prInBlockedStatePktsAvg,
       "prOutBlockedStatePktsAvg": prOutBlockedStatePktsAvg,
       "prInIpAttackPktsAvg": prInIpAttackPktsAvg,
       "prOutIpAttackPktsAvg": prOutIpAttackPktsAvg,
       "prInTcpAttackPktsAvg": prInTcpAttackPktsAvg,
       "prOutTcpAttackPktsAvg": prOutTcpAttackPktsAvg,
       "prInUdpAttackPktsAvg": prInUdpAttackPktsAvg,
       "prOutUdpAttackPktsAvg": prOutUdpAttackPktsAvg,
       "prInIcmpAttackPktsAvg": prInIcmpAttackPktsAvg,
       "prOutIcmpAttackPktsAvg": prOutIcmpAttackPktsAvg,
       "prInOtherIpAttackPktsAvg": prInOtherIpAttackPktsAvg,
       "prOutOtherIpAttackPktsAvg": prOutOtherIpAttackPktsAvg,
       "prInFragmentAttackPktsAvg": prInFragmentAttackPktsAvg,
       "prOutFragmentAttackPktsAvg": prOutFragmentAttackPktsAvg,
       "prInBadipPktsAvg": prInBadipPktsAvg,
       "prOutBadipPktsAvg": prOutBadipPktsAvg,
       "prInBadTcpPktsAvg": prInBadTcpPktsAvg,
       "prOutBadTcpPktsAvg": prOutBadTcpPktsAvg,
       "prInBadUdpPktsAvg": prInBadUdpPktsAvg,
       "prOutBadUdpPktsAvg": prOutBadUdpPktsAvg,
       "prInBadIcmpPktsAvg": prInBadIcmpPktsAvg,
       "prOutBadIcmpPktsAvg": prOutBadIcmpPktsAvg,
       "prInBadOtherIpPktsAvg": prInBadOtherIpPktsAvg,
       "prOutBadOtherIpPktsAvg": prOutBadOtherIpPktsAvg,
       "prInOverloadedAvg": prInOverloadedAvg,
       "prOutOverloadedAvg": prOutOverloadedAvg,
       "prInLatencyAvg": prInLatencyAvg,
       "prOutLatencyAvg": prOutLatencyAvg,
       "prInSmallPpsMax": prInSmallPpsMax,
       "prOutSmallPpsMax": prOutSmallPpsMax,
       "prInMediumPpsMax": prInMediumPpsMax,
       "prOutMediumPpsMax": prOutMediumPpsMax,
       "prInLargePpsMax": prInLargePpsMax,
       "prOutLargePpsMax": prOutLargePpsMax,
       "prInFilteredBwthPercentMax": prInFilteredBwthPercentMax,
       "prOutFilteredBwthPercentMax": prOutFilteredBwthPercentMax,
       "prInSynbacklogtallyMax": prInSynbacklogtallyMax,
       "prOutSynbacklogtallyMax": prOutSynbacklogtallyMax,
       "prInConnectionMax": prInConnectionMax,
       "prOutConnectionMax": prOutConnectionMax,
       "prInConnreqMax": prInConnreqMax,
       "prOutConnreqMax": prOutConnreqMax,
       "prInActiveHttpGetsMax": prInActiveHttpGetsMax,
       "prOutActiveHttpGetsMax": prOutActiveHttpGetsMax,
       "prInProtectBwthPktsMax": prInProtectBwthPktsMax,
       "prOutProtectBwthPktsMax": prOutProtectBwthPktsMax,
       "prInFloodPktsMax": prInFloodPktsMax,
       "prOutFloodPktsMax": prOutFloodPktsMax,
       "prInBlockedProtocolPktsMax": prInBlockedProtocolPktsMax,
       "prOutBlockedProtocolPktsMax": prOutBlockedProtocolPktsMax,
       "prInBlockedStatePktsMax": prInBlockedStatePktsMax,
       "prOutBlockedStatePktsMax": prOutBlockedStatePktsMax,
       "prInIpAttackPktsMax": prInIpAttackPktsMax,
       "prOutIpAttackPktsMax": prOutIpAttackPktsMax,
       "prInTcpAttackPktsMax": prInTcpAttackPktsMax,
       "prOutTcpAttackPktsMax": prOutTcpAttackPktsMax,
       "prInUdpAttackPktsMax": prInUdpAttackPktsMax,
       "prOutUdpAttackPktsMax": prOutUdpAttackPktsMax,
       "prInIcmpAttackPktsMax": prInIcmpAttackPktsMax,
       "prOutIcmpAttackPktsMax": prOutIcmpAttackPktsMax,
       "prInOtherIpAttackPktsMax": prInOtherIpAttackPktsMax,
       "prOutOtherIpAttackPktsMax": prOutOtherIpAttackPktsMax,
       "prInFragmentAttackPktsMax": prInFragmentAttackPktsMax,
       "prOutFragmentAttackPktsMax": prOutFragmentAttackPktsMax,
       "prInBadipPktsMax": prInBadipPktsMax,
       "prOutBadipPktsMax": prOutBadipPktsMax,
       "prInBadTcpPktsMax": prInBadTcpPktsMax,
       "prOutBadTcpPktsMax": prOutBadTcpPktsMax,
       "prInBadUdpPktsMax": prInBadUdpPktsMax,
       "prOutBadUdpPktsMax": prOutBadUdpPktsMax,
       "prInBadIcmpPktsMax": prInBadIcmpPktsMax,
       "prOutBadIcmpPktsMax": prOutBadIcmpPktsMax,
       "prInBadOtherIpPktsMax": prInBadOtherIpPktsMax,
       "prOutBadOtherIpPktsMax": prOutBadOtherIpPktsMax,
       "prInOverloadedMax": prInOverloadedMax,
       "prOutOverloadedMax": prOutOverloadedMax,
       "prInLatencyMax": prInLatencyMax,
       "prOutLatencyMax": prOutLatencyMax,
       "prIncidentTable": prIncidentTable,
       "prIncidentEntry": prIncidentEntry,
       "prIncidentYear": prIncidentYear,
       "prIncidentMonth": prIncidentMonth,
       "prIncidentDay": prIncidentDay,
       "prIncidentNumber": prIncidentNumber,
       "prIncidentInetAddressType": prIncidentInetAddressType,
       "prIncidentInetAddress": prIncidentInetAddress,
       "prIncidentStart": prIncidentStart,
       "prIncidentAddress": prIncidentAddress,
       "prIncidentType": prIncidentType,
       "prIncidentDirection": prIncidentDirection,
       "prIncidentPeakRate": prIncidentPeakRate,
       "prIncidentDropped": prIncidentDropped,
       "jddsGatewayInternet": jddsGatewayInternet,
       "gwInternetConfigTable": gwInternetConfigTable,
       "gwInternetConfigEntry": gwInternetConfigEntry,
       "gwInternetConfigIndex": gwInternetConfigIndex,
       "gwInternetConfigMacAddress": gwInternetConfigMacAddress,
       "gwInternetConfigToSpeedBps": gwInternetConfigToSpeedBps,
       "gwInternetConfigToRatePps": gwInternetConfigToRatePps,
       "gwInternetStatsTable": gwInternetStatsTable,
       "gwInternetStatsEntry": gwInternetStatsEntry,
       "gwInternetStatsIndex": gwInternetStatsIndex,
       "gwInternetMacAddress": gwInternetMacAddress,
       "gwInternetIpAddress": gwInternetIpAddress,
       "gwInternetInTotalBytesCnt": gwInternetInTotalBytesCnt,
       "gwInternetOutTotalBytesCnt": gwInternetOutTotalBytesCnt,
       "gwInternetInDroppedBytesCnt": gwInternetInDroppedBytesCnt,
       "gwInternetOutDroppedBytesCnt": gwInternetOutDroppedBytesCnt,
       "gwInternetInTotalPpsMax": gwInternetInTotalPpsMax,
       "gwInternetOutTotalPpsMax": gwInternetOutTotalPpsMax,
       "gwInternetInDroppedPpsMax": gwInternetInDroppedPpsMax,
       "gwInternetOutDroppedPpsMax": gwInternetOutDroppedPpsMax,
       "gwInternetInTotalBpsMax": gwInternetInTotalBpsMax,
       "gwInternetOutTotalBpsMax": gwInternetOutTotalBpsMax,
       "gwInternetInDroppedBpsMax": gwInternetInDroppedBpsMax,
       "gwInternetOutDroppedBpsMax": gwInternetOutDroppedBpsMax,
       "jddsGatewayProtected": jddsGatewayProtected,
       "gwProtectedConfigTable": gwProtectedConfigTable,
       "gwProtectedConfigEntry": gwProtectedConfigEntry,
       "gwProtectedConfigIndex": gwProtectedConfigIndex,
       "gwProtectedConfigMacAddress": gwProtectedConfigMacAddress,
       "gwProtectedConfigToSpeedBps": gwProtectedConfigToSpeedBps,
       "gwProtectedConfigToRatePps": gwProtectedConfigToRatePps,
       "gwProtectedStatsTable": gwProtectedStatsTable,
       "gwProtectedStatsEntry": gwProtectedStatsEntry,
       "gwProtectedIndex": gwProtectedIndex,
       "gwProtectedMacAddress": gwProtectedMacAddress,
       "gwProtectedIpAddress": gwProtectedIpAddress,
       "gwProtectedInTotalBytesCnt": gwProtectedInTotalBytesCnt,
       "gwProtectedOutTotalBytesCnt": gwProtectedOutTotalBytesCnt,
       "gwProtectedInDroppedBytesCnt": gwProtectedInDroppedBytesCnt,
       "gwProtectedOutDroppedBytesCnt": gwProtectedOutDroppedBytesCnt,
       "gwProtectedInTotalPpsMax": gwProtectedInTotalPpsMax,
       "gwProtectedOutTotalPpsMax": gwProtectedOutTotalPpsMax,
       "gwProtectedInDroppedPpsMax": gwProtectedInDroppedPpsMax,
       "gwProtectedOutDroppedPpsMax": gwProtectedOutDroppedPpsMax,
       "gwProtectedInTotalBpsMax": gwProtectedInTotalBpsMax,
       "gwProtectedOutTotalBpsMax": gwProtectedOutTotalBpsMax,
       "gwProtectedInDroppedBpsMax": gwProtectedInDroppedBpsMax,
       "gwProtectedOutDroppedBpsMax": gwProtectedOutDroppedBpsMax,
       "ddossecure4MIBConformance": ddossecure4MIBConformance,
       "ddossecure4MIBCompliances": ddossecure4MIBCompliances,
       "ddossecure4MIBCompliance": ddossecure4MIBCompliance,
       "ddossecure4MIBComplianceDep": ddossecure4MIBComplianceDep,
       "ddossecure4MIBGroups": ddossecure4MIBGroups,
       "apCfgGroup": apCfgGroup,
       "gwGroup": gwGroup,
       "apIncidentGroup": apIncidentGroup,
       "apDebugGroup": apDebugGroup,
       "apGroup": apGroup,
       "prGroup": prGroup,
       "prCfgGroup": prCfgGroup,
       "gwCfgGroup": gwCfgGroup,
       "apEventObjectGroup": apEventObjectGroup,
       "apRatesGroup": apRatesGroup,
       "poFilterCfgGroup": poFilterCfgGroup,
       "apLinkStatusGroup": apLinkStatusGroup,
       "apLogGroup": apLogGroup,
       "apHaCfgGroup": apHaCfgGroup,
       "poGroup": poGroup,
       "prNotificationGroup": prNotificationGroup,
       "deprecatedNotificationGroup": deprecatedNotificationGroup}
)
