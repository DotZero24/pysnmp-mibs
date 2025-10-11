# SNMP MIB module (XG-FIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/sophos/XG-FIREWALL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:31 2025
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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

sophos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21067)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HaModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("active-passive", 2),
          ("active-active", 3))
    )



class ServiceStatsType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("untouched", 1),
          ("stopped", 2),
          ("initializing", 3),
          ("running", 4),
          ("exiting", 5),
          ("dead", 6),
          ("unregistered", 7))
    )



class RegistrationStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("registered", 1),
          ("unregistered", 2))
    )



class SubscriptionStatusType(TextualConvention, Integer32):
    status = "current"
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
        *(("trial", 1),
          ("unsubscribed", 2),
          ("subscribed", 3),
          ("expired", 4))
    )



class SupportStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support8x5", 1),
          ("support24x7", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Xg_firewall_ObjectIdentity = ObjectIdentity
xg_firewall = _Xg_firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2)
)
if mibBuilder.loadTexts:
    xg_firewall.setStatus("current")
_SfosSystem_ObjectIdentity = ObjectIdentity
sfosSystem = _SfosSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1)
)
_SysInstall_ObjectIdentity = ObjectIdentity
sysInstall = _SysInstall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 1)
)


class _ApplianceKey_Type(DisplayString):
    """Custom type applianceKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ApplianceKey_Type.__name__ = "DisplayString"
_ApplianceKey_Object = MibScalar
applianceKey = _ApplianceKey_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 1, 1),
    _ApplianceKey_Type()
)
applianceKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applianceKey.setStatus("current")


class _ApplianceModel_Type(DisplayString):
    """Custom type applianceModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ApplianceModel_Type.__name__ = "DisplayString"
_ApplianceModel_Object = MibScalar
applianceModel = _ApplianceModel_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 1, 2),
    _ApplianceModel_Type()
)
applianceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applianceModel.setStatus("current")


class _Xg_firewallVersion_Type(DisplayString):
    """Custom type xg_firewallVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Xg_firewallVersion_Type.__name__ = "DisplayString"
_Xg_firewallVersion_Object = MibScalar
xg_firewallVersion = _Xg_firewallVersion_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 1, 3),
    _Xg_firewallVersion_Type()
)
xg_firewallVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xg_firewallVersion.setStatus("current")


class _WebcatVersion_Type(DisplayString):
    """Custom type webcatVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WebcatVersion_Type.__name__ = "DisplayString"
_WebcatVersion_Object = MibScalar
webcatVersion = _WebcatVersion_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 1, 4),
    _WebcatVersion_Type()
)
webcatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webcatVersion.setStatus("current")


class _AvVersion_Type(DisplayString):
    """Custom type avVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AvVersion_Type.__name__ = "DisplayString"
_AvVersion_Object = MibScalar
avVersion = _AvVersion_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 1, 5),
    _AvVersion_Type()
)
avVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avVersion.setStatus("current")


class _AsVersion_Type(DisplayString):
    """Custom type asVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AsVersion_Type.__name__ = "DisplayString"
_AsVersion_Object = MibScalar
asVersion = _AsVersion_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 1, 6),
    _AsVersion_Type()
)
asVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asVersion.setStatus("current")


class _IdpVersion_Type(DisplayString):
    """Custom type idpVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_IdpVersion_Type.__name__ = "DisplayString"
_IdpVersion_Object = MibScalar
idpVersion = _IdpVersion_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 1, 7),
    _IdpVersion_Type()
)
idpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idpVersion.setStatus("current")
_SysStatus_ObjectIdentity = ObjectIdentity
sysStatus = _SysStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2)
)
_SystemDate_Type = DateAndTime
_SystemDate_Object = MibScalar
systemDate = _SystemDate_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 1),
    _SystemDate_Type()
)
systemDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDate.setStatus("current")
_CpuStatus_ObjectIdentity = ObjectIdentity
cpuStatus = _CpuStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 2)
)
_CpuPercentUsage_Type = Integer32
_CpuPercentUsage_Object = MibScalar
cpuPercentUsage = _CpuPercentUsage_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 2, 1),
    _CpuPercentUsage_Type()
)
cpuPercentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPercentUsage.setStatus("current")
_DiskStatus_ObjectIdentity = ObjectIdentity
diskStatus = _DiskStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 3)
)
_DiskCapacity_Type = Gauge32
_DiskCapacity_Object = MibScalar
diskCapacity = _DiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 3, 1),
    _DiskCapacity_Type()
)
diskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskCapacity.setStatus("current")
_DiskPercentUsage_Type = Gauge32
_DiskPercentUsage_Object = MibScalar
diskPercentUsage = _DiskPercentUsage_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 3, 2),
    _DiskPercentUsage_Type()
)
diskPercentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPercentUsage.setStatus("current")
_MemoryStatus_ObjectIdentity = ObjectIdentity
memoryStatus = _MemoryStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 4)
)
_MemoryCapacity_Type = Gauge32
_MemoryCapacity_Object = MibScalar
memoryCapacity = _MemoryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 4, 1),
    _MemoryCapacity_Type()
)
memoryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryCapacity.setStatus("current")
_MemoryPercentUsage_Type = Gauge32
_MemoryPercentUsage_Object = MibScalar
memoryPercentUsage = _MemoryPercentUsage_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 4, 2),
    _MemoryPercentUsage_Type()
)
memoryPercentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPercentUsage.setStatus("current")
_SwapCapacity_Type = Gauge32
_SwapCapacity_Object = MibScalar
swapCapacity = _SwapCapacity_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 4, 3),
    _SwapCapacity_Type()
)
swapCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swapCapacity.setStatus("current")
_SwapPercentUsage_Type = Gauge32
_SwapPercentUsage_Object = MibScalar
swapPercentUsage = _SwapPercentUsage_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 4, 4),
    _SwapPercentUsage_Type()
)
swapPercentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swapPercentUsage.setStatus("current")
_HaMode_Type = HaModeType
_HaMode_Object = MibScalar
haMode = _HaMode_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 5),
    _HaMode_Type()
)
haMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haMode.setStatus("current")
_LiveUsers_Type = Gauge32
_LiveUsers_Object = MibScalar
liveUsers = _LiveUsers_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 6),
    _LiveUsers_Type()
)
liveUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveUsers.setStatus("current")
_HttpHits_Type = Counter64
_HttpHits_Object = MibScalar
httpHits = _HttpHits_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 7),
    _HttpHits_Type()
)
httpHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpHits.setStatus("current")
_FtpHits_Type = Counter64
_FtpHits_Object = MibScalar
ftpHits = _FtpHits_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 8),
    _FtpHits_Type()
)
ftpHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpHits.setStatus("current")
_MailHits_ObjectIdentity = ObjectIdentity
mailHits = _MailHits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 9)
)
_Pop3Hits_Type = Counter64
_Pop3Hits_Object = MibScalar
pop3Hits = _Pop3Hits_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 9, 1),
    _Pop3Hits_Type()
)
pop3Hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pop3Hits.setStatus("current")
_ImapHits_Type = Counter64
_ImapHits_Object = MibScalar
imapHits = _ImapHits_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 9, 2),
    _ImapHits_Type()
)
imapHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapHits.setStatus("current")
_SmtpHits_Type = Counter64
_SmtpHits_Object = MibScalar
smtpHits = _SmtpHits_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 9, 3),
    _SmtpHits_Type()
)
smtpHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpHits.setStatus("current")
_ServiceStats_ObjectIdentity = ObjectIdentity
serviceStats = _ServiceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10)
)
_Pop3Service_Type = ServiceStatsType
_Pop3Service_Object = MibScalar
pop3Service = _Pop3Service_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 1),
    _Pop3Service_Type()
)
pop3Service.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pop3Service.setStatus("current")
_Imap4Service_Type = ServiceStatsType
_Imap4Service_Object = MibScalar
imap4Service = _Imap4Service_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 2),
    _Imap4Service_Type()
)
imap4Service.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imap4Service.setStatus("current")
_SmtpService_Type = ServiceStatsType
_SmtpService_Object = MibScalar
smtpService = _SmtpService_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 3),
    _SmtpService_Type()
)
smtpService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpService.setStatus("current")
_FtpService_Type = ServiceStatsType
_FtpService_Object = MibScalar
ftpService = _FtpService_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 4),
    _FtpService_Type()
)
ftpService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpService.setStatus("current")
_HttpService_Type = ServiceStatsType
_HttpService_Object = MibScalar
httpService = _HttpService_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 5),
    _HttpService_Type()
)
httpService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpService.setStatus("current")
_AvService_Type = ServiceStatsType
_AvService_Object = MibScalar
avService = _AvService_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 6),
    _AvService_Type()
)
avService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avService.setStatus("current")
_AsService_Type = ServiceStatsType
_AsService_Object = MibScalar
asService = _AsService_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 7),
    _AsService_Type()
)
asService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asService.setStatus("current")
_DnsService_Type = ServiceStatsType
_DnsService_Object = MibScalar
dnsService = _DnsService_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 8),
    _DnsService_Type()
)
dnsService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsService.setStatus("current")
_HaService_Type = ServiceStatsType
_HaService_Object = MibScalar
haService = _HaService_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 9),
    _HaService_Type()
)
haService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haService.setStatus("current")
_IdpService_Type = ServiceStatsType
_IdpService_Object = MibScalar
idpService = _IdpService_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 10),
    _IdpService_Type()
)
idpService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idpService.setStatus("current")
_ApacheService_Type = ServiceStatsType
_ApacheService_Object = MibScalar
apacheService = _ApacheService_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 11),
    _ApacheService_Type()
)
apacheService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheService.setStatus("current")
_NtpService_Type = ServiceStatsType
_NtpService_Object = MibScalar
ntpService = _NtpService_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 12),
    _NtpService_Type()
)
ntpService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpService.setStatus("current")
_TomcatService_Type = ServiceStatsType
_TomcatService_Object = MibScalar
tomcatService = _TomcatService_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 13),
    _TomcatService_Type()
)
tomcatService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tomcatService.setStatus("current")
_SslvpnService_Type = ServiceStatsType
_SslvpnService_Object = MibScalar
sslvpnService = _SslvpnService_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 14),
    _SslvpnService_Type()
)
sslvpnService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslvpnService.setStatus("current")
_Databaseservice_Type = ServiceStatsType
_Databaseservice_Object = MibScalar
databaseservice = _Databaseservice_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 15),
    _Databaseservice_Type()
)
databaseservice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseservice.setStatus("current")
_NetworkService_Type = ServiceStatsType
_NetworkService_Object = MibScalar
networkService = _NetworkService_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 16),
    _NetworkService_Type()
)
networkService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkService.setStatus("current")
_GarnerService_Type = ServiceStatsType
_GarnerService_Object = MibScalar
garnerService = _GarnerService_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 17),
    _GarnerService_Type()
)
garnerService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    garnerService.setStatus("current")
_DroutingService_Type = ServiceStatsType
_DroutingService_Object = MibScalar
droutingService = _DroutingService_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 18),
    _DroutingService_Type()
)
droutingService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    droutingService.setStatus("current")
_SshdService_Type = ServiceStatsType
_SshdService_Object = MibScalar
sshdService = _SshdService_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 19),
    _SshdService_Type()
)
sshdService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshdService.setStatus("current")
_DgdService_Type = ServiceStatsType
_DgdService_Object = MibScalar
dgdService = _DgdService_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 2, 10, 20),
    _DgdService_Type()
)
dgdService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgdService.setStatus("current")
_SysLicense_ObjectIdentity = ObjectIdentity
sysLicense = _SysLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3)
)
_LiAppliance_ObjectIdentity = ObjectIdentity
liAppliance = _LiAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3, 1)
)
_AppRegStatus_Type = RegistrationStatusType
_AppRegStatus_Object = MibScalar
appRegStatus = _AppRegStatus_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3, 1, 1),
    _AppRegStatus_Type()
)
appRegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRegStatus.setStatus("current")
_AppExpiryDate_Type = DateAndTime
_AppExpiryDate_Object = MibScalar
appExpiryDate = _AppExpiryDate_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3, 1, 2),
    _AppExpiryDate_Type()
)
appExpiryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appExpiryDate.setStatus("current")
_LiSupport_ObjectIdentity = ObjectIdentity
liSupport = _LiSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3, 2)
)
_SupportSubStatus_Type = SupportStatusType
_SupportSubStatus_Object = MibScalar
supportSubStatus = _SupportSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3, 2, 1),
    _SupportSubStatus_Type()
)
supportSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supportSubStatus.setStatus("current")
_SupportExpiryDate_Type = DateAndTime
_SupportExpiryDate_Object = MibScalar
supportExpiryDate = _SupportExpiryDate_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3, 2, 2),
    _SupportExpiryDate_Type()
)
supportExpiryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supportExpiryDate.setStatus("current")
_LiAntivirus_ObjectIdentity = ObjectIdentity
liAntivirus = _LiAntivirus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3, 3)
)
_AvSubStatus_Type = SubscriptionStatusType
_AvSubStatus_Object = MibScalar
avSubStatus = _AvSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3, 3, 1),
    _AvSubStatus_Type()
)
avSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avSubStatus.setStatus("current")
_AvExpiryDate_Type = DateAndTime
_AvExpiryDate_Object = MibScalar
avExpiryDate = _AvExpiryDate_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3, 3, 2),
    _AvExpiryDate_Type()
)
avExpiryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avExpiryDate.setStatus("current")
_LiAntispam_ObjectIdentity = ObjectIdentity
liAntispam = _LiAntispam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3, 4)
)
_AsSubStatus_Type = SubscriptionStatusType
_AsSubStatus_Object = MibScalar
asSubStatus = _AsSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3, 4, 1),
    _AsSubStatus_Type()
)
asSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asSubStatus.setStatus("current")
_AsExpiryDate_Type = DateAndTime
_AsExpiryDate_Object = MibScalar
asExpiryDate = _AsExpiryDate_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3, 4, 2),
    _AsExpiryDate_Type()
)
asExpiryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asExpiryDate.setStatus("current")
_LiIdp_ObjectIdentity = ObjectIdentity
liIdp = _LiIdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3, 5)
)
_IdpSubStatus_Type = SubscriptionStatusType
_IdpSubStatus_Object = MibScalar
idpSubStatus = _IdpSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3, 5, 1),
    _IdpSubStatus_Type()
)
idpSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idpSubStatus.setStatus("current")
_IdpExpiryDate_Type = DateAndTime
_IdpExpiryDate_Object = MibScalar
idpExpiryDate = _IdpExpiryDate_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3, 5, 2),
    _IdpExpiryDate_Type()
)
idpExpiryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idpExpiryDate.setStatus("current")
_LiWebcat_ObjectIdentity = ObjectIdentity
liWebcat = _LiWebcat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3, 6)
)
_WebcatSubStatus_Type = SubscriptionStatusType
_WebcatSubStatus_Object = MibScalar
webcatSubStatus = _WebcatSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3, 6, 1),
    _WebcatSubStatus_Type()
)
webcatSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webcatSubStatus.setStatus("current")
_WebcatExpiryDate_Type = DateAndTime
_WebcatExpiryDate_Object = MibScalar
webcatExpiryDate = _WebcatExpiryDate_Object(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 3, 6, 2),
    _WebcatExpiryDate_Type()
)
webcatExpiryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webcatExpiryDate.setStatus("current")
_SysAlerts_ObjectIdentity = ObjectIdentity
sysAlerts = _SysAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4)
)
_HighDiskUsage_ObjectIdentity = ObjectIdentity
highDiskUsage = _HighDiskUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 2)
)
_HighMemUsage_ObjectIdentity = ObjectIdentity
highMemUsage = _HighMemUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 3)
)
_AvAlerts_ObjectIdentity = ObjectIdentity
avAlerts = _AvAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 4)
)
_DgdAlerts_ObjectIdentity = ObjectIdentity
dgdAlerts = _DgdAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 5)
)
_IdpAlerts_ObjectIdentity = ObjectIdentity
idpAlerts = _IdpAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 6)
)
_DosAlerts_ObjectIdentity = ObjectIdentity
dosAlerts = _DosAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 7)
)
_CscAlerts_ObjectIdentity = ObjectIdentity
cscAlerts = _CscAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 8)
)

# Managed Objects groups


# Notification objects

highCpuUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    highCpuUsage.setStatus(
        "current"
    )

highConfDiskUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    highConfDiskUsage.setStatus(
        "current"
    )

highSigDiskUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    highSigDiskUsage.setStatus(
        "current"
    )

highReportDiskUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    highReportDiskUsage.setStatus(
        "current"
    )

highPhyMemUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    highPhyMemUsage.setStatus(
        "current"
    )

highSwapMemUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    highSwapMemUsage.setStatus(
        "current"
    )

httpVirus = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    httpVirus.setStatus(
        "current"
    )

smtpVirus = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 4, 2)
)
if mibBuilder.loadTexts:
    smtpVirus.setStatus(
        "current"
    )

pop3Virus = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 4, 3)
)
if mibBuilder.loadTexts:
    pop3Virus.setStatus(
        "current"
    )

imap4Virus = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 4, 4)
)
if mibBuilder.loadTexts:
    imap4Virus.setStatus(
        "current"
    )

ftpVirus = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 4, 5)
)
if mibBuilder.loadTexts:
    ftpVirus.setStatus(
        "current"
    )

gwLiveDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 5, 1)
)
if mibBuilder.loadTexts:
    gwLiveDead.setStatus(
        "current"
    )

idpAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 6, 1)
)
if mibBuilder.loadTexts:
    idpAlert.setStatus(
        "current"
    )

synFlood = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 7, 1)
)
if mibBuilder.loadTexts:
    synFlood.setStatus(
        "current"
    )

tcpFlood = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 7, 2)
)
if mibBuilder.loadTexts:
    tcpFlood.setStatus(
        "current"
    )

udpFlood = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 7, 3)
)
if mibBuilder.loadTexts:
    udpFlood.setStatus(
        "current"
    )

icmpFlood = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 7, 4)
)
if mibBuilder.loadTexts:
    icmpFlood.setStatus(
        "current"
    )

opcodeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 8, 1)
)
if mibBuilder.loadTexts:
    opcodeFail.setStatus(
        "current"
    )

serviceFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 21067, 2, 1, 4, 8, 2)
)
if mibBuilder.loadTexts:
    serviceFail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XG-FIREWALL-MIB",
    **{"HaModeType": HaModeType,
       "ServiceStatsType": ServiceStatsType,
       "RegistrationStatusType": RegistrationStatusType,
       "SubscriptionStatusType": SubscriptionStatusType,
       "SupportStatusType": SupportStatusType,
       "sophos": sophos,
       "xg-firewall": xg_firewall,
       "sfosSystem": sfosSystem,
       "sysInstall": sysInstall,
       "applianceKey": applianceKey,
       "applianceModel": applianceModel,
       "xg-firewallVersion": xg_firewallVersion,
       "webcatVersion": webcatVersion,
       "avVersion": avVersion,
       "asVersion": asVersion,
       "idpVersion": idpVersion,
       "sysStatus": sysStatus,
       "systemDate": systemDate,
       "cpuStatus": cpuStatus,
       "cpuPercentUsage": cpuPercentUsage,
       "diskStatus": diskStatus,
       "diskCapacity": diskCapacity,
       "diskPercentUsage": diskPercentUsage,
       "memoryStatus": memoryStatus,
       "memoryCapacity": memoryCapacity,
       "memoryPercentUsage": memoryPercentUsage,
       "swapCapacity": swapCapacity,
       "swapPercentUsage": swapPercentUsage,
       "haMode": haMode,
       "liveUsers": liveUsers,
       "httpHits": httpHits,
       "ftpHits": ftpHits,
       "mailHits": mailHits,
       "pop3Hits": pop3Hits,
       "imapHits": imapHits,
       "smtpHits": smtpHits,
       "serviceStats": serviceStats,
       "pop3Service": pop3Service,
       "imap4Service": imap4Service,
       "smtpService": smtpService,
       "ftpService": ftpService,
       "httpService": httpService,
       "avService": avService,
       "asService": asService,
       "dnsService": dnsService,
       "haService": haService,
       "idpService": idpService,
       "apacheService": apacheService,
       "ntpService": ntpService,
       "tomcatService": tomcatService,
       "sslvpnService": sslvpnService,
       "databaseservice": databaseservice,
       "networkService": networkService,
       "garnerService": garnerService,
       "droutingService": droutingService,
       "sshdService": sshdService,
       "dgdService": dgdService,
       "sysLicense": sysLicense,
       "liAppliance": liAppliance,
       "appRegStatus": appRegStatus,
       "appExpiryDate": appExpiryDate,
       "liSupport": liSupport,
       "supportSubStatus": supportSubStatus,
       "supportExpiryDate": supportExpiryDate,
       "liAntivirus": liAntivirus,
       "avSubStatus": avSubStatus,
       "avExpiryDate": avExpiryDate,
       "liAntispam": liAntispam,
       "asSubStatus": asSubStatus,
       "asExpiryDate": asExpiryDate,
       "liIdp": liIdp,
       "idpSubStatus": idpSubStatus,
       "idpExpiryDate": idpExpiryDate,
       "liWebcat": liWebcat,
       "webcatSubStatus": webcatSubStatus,
       "webcatExpiryDate": webcatExpiryDate,
       "sysAlerts": sysAlerts,
       "highCpuUsage": highCpuUsage,
       "highDiskUsage": highDiskUsage,
       "highConfDiskUsage": highConfDiskUsage,
       "highSigDiskUsage": highSigDiskUsage,
       "highReportDiskUsage": highReportDiskUsage,
       "highMemUsage": highMemUsage,
       "highPhyMemUsage": highPhyMemUsage,
       "highSwapMemUsage": highSwapMemUsage,
       "avAlerts": avAlerts,
       "httpVirus": httpVirus,
       "smtpVirus": smtpVirus,
       "pop3Virus": pop3Virus,
       "imap4Virus": imap4Virus,
       "ftpVirus": ftpVirus,
       "dgdAlerts": dgdAlerts,
       "gwLiveDead": gwLiveDead,
       "idpAlerts": idpAlerts,
       "idpAlert": idpAlert,
       "dosAlerts": dosAlerts,
       "synFlood": synFlood,
       "tcpFlood": tcpFlood,
       "udpFlood": udpFlood,
       "icmpFlood": icmpFlood,
       "cscAlerts": cscAlerts,
       "opcodeFail": opcodeFail,
       "serviceFail": serviceFail}
)
