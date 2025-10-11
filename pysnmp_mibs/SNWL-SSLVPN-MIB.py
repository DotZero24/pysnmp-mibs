# SNMP MIB module (SNWL-SSLVPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/sonicwall/SNWL-SSLVPN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:29 2025
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

(sonicwall,
 sonicwallSSLVPN) = mibBuilder.importSymbols(
    "SONICWALL-SMI",
    "sonicwall",
    "sonicwallSSLVPN")


# MODULE-IDENTITY

sonicwallSSLVPN = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 6)
)
if mibBuilder.loadTexts:
    sonicwallSSLVPN.setRevisions(
        ("2009-10-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SslvpnSystemModule_ObjectIdentity = ObjectIdentity
sslvpnSystemModule = _SslvpnSystemModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 6, 2)
)
_SslvpnSys_ObjectIdentity = ObjectIdentity
sslvpnSys = _SslvpnSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 6, 2, 1)
)
_SslvpnAuthCode_Type = DisplayString
_SslvpnAuthCode_Object = MibScalar
sslvpnAuthCode = _SslvpnAuthCode_Object(
    (1, 3, 6, 1, 4, 1, 8741, 6, 2, 1, 1),
    _SslvpnAuthCode_Type()
)
sslvpnAuthCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslvpnAuthCode.setStatus("current")
_CpuType_Type = DisplayString
_CpuType_Object = MibScalar
cpuType = _CpuType_Object(
    (1, 3, 6, 1, 4, 1, 8741, 6, 2, 1, 2),
    _CpuType_Type()
)
cpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuType.setStatus("current")
_CpuUtilization_Type = Integer32
_CpuUtilization_Object = MibScalar
cpuUtilization = _CpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8741, 6, 2, 1, 3),
    _CpuUtilization_Type()
)
cpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilization.setStatus("current")
_MemoryTotal_Type = DisplayString
_MemoryTotal_Object = MibScalar
memoryTotal = _MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 8741, 6, 2, 1, 4),
    _MemoryTotal_Type()
)
memoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryTotal.setStatus("current")
_MemoryUtilization_Type = Integer32
_MemoryUtilization_Object = MibScalar
memoryUtilization = _MemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8741, 6, 2, 1, 5),
    _MemoryUtilization_Type()
)
memoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryUtilization.setStatus("current")
_SystemTime_Type = DisplayString
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 8741, 6, 2, 1, 6),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTime.setStatus("current")
_SystemUptime_Type = DisplayString
_SystemUptime_Object = MibScalar
systemUptime = _SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 8741, 6, 2, 1, 7),
    _SystemUptime_Type()
)
systemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUptime.setStatus("current")
_ActiveUsers_Type = Integer32
_ActiveUsers_Object = MibScalar
activeUsers = _ActiveUsers_Object(
    (1, 3, 6, 1, 4, 1, 8741, 6, 2, 1, 8),
    _ActiveUsers_Type()
)
activeUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeUsers.setStatus("current")
_ActiveUserLicense_Type = Integer32
_ActiveUserLicense_Object = MibScalar
activeUserLicense = _ActiveUserLicense_Object(
    (1, 3, 6, 1, 4, 1, 8741, 6, 2, 1, 9),
    _ActiveUserLicense_Type()
)
activeUserLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeUserLicense.setStatus("current")
_ActiveNetExtenderConnections_Type = Integer32
_ActiveNetExtenderConnections_Object = MibScalar
activeNetExtenderConnections = _ActiveNetExtenderConnections_Object(
    (1, 3, 6, 1, 4, 1, 8741, 6, 2, 1, 10),
    _ActiveNetExtenderConnections_Type()
)
activeNetExtenderConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeNetExtenderConnections.setStatus("current")
_ActiveVirtualAssistTechnicians_Type = Integer32
_ActiveVirtualAssistTechnicians_Object = MibScalar
activeVirtualAssistTechnicians = _ActiveVirtualAssistTechnicians_Object(
    (1, 3, 6, 1, 4, 1, 8741, 6, 2, 1, 11),
    _ActiveVirtualAssistTechnicians_Type()
)
activeVirtualAssistTechnicians.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeVirtualAssistTechnicians.setStatus("current")
_SslvpnLicenseModule_ObjectIdentity = ObjectIdentity
sslvpnLicenseModule = _SslvpnLicenseModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 6, 3)
)
_SslvpnLicense_ObjectIdentity = ObjectIdentity
sslvpnLicense = _SslvpnLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 6, 3, 1)
)
_UserLicense_Type = DisplayString
_UserLicense_Object = MibScalar
userLicense = _UserLicense_Object(
    (1, 3, 6, 1, 4, 1, 8741, 6, 3, 1, 1),
    _UserLicense_Type()
)
userLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userLicense.setStatus("current")
_ViewPointLicense_Type = DisplayString
_ViewPointLicense_Object = MibScalar
viewPointLicense = _ViewPointLicense_Object(
    (1, 3, 6, 1, 4, 1, 8741, 6, 3, 1, 2),
    _ViewPointLicense_Type()
)
viewPointLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viewPointLicense.setStatus("current")
_VirtualAssistLicense_Type = DisplayString
_VirtualAssistLicense_Object = MibScalar
virtualAssistLicense = _VirtualAssistLicense_Object(
    (1, 3, 6, 1, 4, 1, 8741, 6, 3, 1, 3),
    _VirtualAssistLicense_Type()
)
virtualAssistLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAssistLicense.setStatus("current")
_WafLicense_Type = DisplayString
_WafLicense_Object = MibScalar
wafLicense = _WafLicense_Object(
    (1, 3, 6, 1, 4, 1, 8741, 6, 3, 1, 4),
    _WafLicense_Type()
)
wafLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wafLicense.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNWL-SSLVPN-MIB",
    **{"sonicwallSSLVPN": sonicwallSSLVPN,
       "sslvpnSystemModule": sslvpnSystemModule,
       "sslvpnSys": sslvpnSys,
       "sslvpnAuthCode": sslvpnAuthCode,
       "cpuType": cpuType,
       "cpuUtilization": cpuUtilization,
       "memoryTotal": memoryTotal,
       "memoryUtilization": memoryUtilization,
       "systemTime": systemTime,
       "systemUptime": systemUptime,
       "activeUsers": activeUsers,
       "activeUserLicense": activeUserLicense,
       "activeNetExtenderConnections": activeNetExtenderConnections,
       "activeVirtualAssistTechnicians": activeVirtualAssistTechnicians,
       "sslvpnLicenseModule": sslvpnLicenseModule,
       "sslvpnLicense": sslvpnLicense,
       "userLicense": userLicense,
       "viewPointLicense": viewPointLicense,
       "virtualAssistLicense": virtualAssistLicense,
       "wafLicense": wafLicense}
)
