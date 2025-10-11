# SNMP MIB module (SONICWALL-GMS-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/sonicwall/SONICWALL-GMS-TRAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:36 2025
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

(snmpTrapAddress,
 snmpTrapCommunity) = mibBuilder.importSymbols(
    "SNMP-COMMUNITY-MIB",
    "snmpTrapAddress",
    "snmpTrapCommunity")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(snmpTrapEnterprise,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTrapEnterprise")

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
    "iso",
    "snmpModules")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(swTrapInfoTrapDescription,
 swTrapInfoTrapType) = mibBuilder.importSymbols(
    "SONICWALL-FIREWALL-TRAP-MIB",
    "swTrapInfoTrapDescription",
    "swTrapInfoTrapType")

(sonicwallGMS,) = mibBuilder.importSymbols(
    "SONICWALL-SMI",
    "sonicwallGMS")


# MODULE-IDENTITY

sonicwallGMSTrapModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class GmsTrapType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              101,
              102,
              103,
              104,
              105,
              106,
              110,
              120,
              130,
              199,
              200)
        )
    )
    namedValues = NamedValues(
        *(("trapTypeStillAlive", 100),
          ("trapTypeLostContact", 101),
          ("trapTypeFirewallLostContact", 102),
          ("trapTypeNormalShutdown", 103),
          ("trapTypeStartup", 104),
          ("trapTypeStartContact", 105),
          ("trapTypeFirewallStartContact", 106),
          ("trapTypeFirewallMonDevicesUpDown", 110),
          ("trapTypeFirewallMonDevicesSNMPRTMAlert", 120),
          ("trapTypeFirewallEventMgmtAlert", 130),
          ("trapTypeStopSnmpManager", 199),
          ("trapTypeUnspecified", 200))
    )



class GmsComponentType(TextualConvention, Integer32):
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
              11,
              12,
              13,
              14,
              15,
              999)
        )
    )
    namedValues = NamedValues(
        *(("componentTypeGMSSNMPMgr", 0),
          ("componentTypeGMSConsole", 1),
          ("componentTypeGMSAgent", 2),
          ("componentTypeGateway", 3),
          ("componentTypeFirewall", 4),
          ("componentTypeViewpointScheduler", 5),
          ("componentTypeViewpointSummarizer", 6),
          ("componentTypeCLI", 7),
          ("componentTypeVisualTool", 8),
          ("componentTypeSyslogCollector", 9),
          ("componentTypeSGMSTool", 10),
          ("componentTypeSGMSMonitor", 11),
          ("componentTypeSGMSUpdater", 12),
          ("componentTypeSGMSJUnit", 13),
          ("componentTypeSGMSEventMgmt", 14),
          ("componentTypeSGMSWebServices", 15),
          ("componentTypeGMSUnknown", 999))
    )



# MIB Managed Objects in the order of their OIDs

_SonicwallGMSTrapInfo_ObjectIdentity = ObjectIdentity
sonicwallGMSTrapInfo = _SonicwallGMSTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 3, 1, 1)
)
_GmsTrapInfoTable_ObjectIdentity = ObjectIdentity
gmsTrapInfoTable = _GmsTrapInfoTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 3, 1, 1, 1)
)
_GmsTrapInfoTrapType_Type = GmsTrapType
_GmsTrapInfoTrapType_Object = MibScalar
gmsTrapInfoTrapType = _GmsTrapInfoTrapType_Object(
    (1, 3, 6, 1, 4, 1, 8741, 3, 1, 1, 1, 1),
    _GmsTrapInfoTrapType_Type()
)
gmsTrapInfoTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmsTrapInfoTrapType.setStatus("current")
_GmsTrapInfoTrapDescription_Type = DisplayString
_GmsTrapInfoTrapDescription_Object = MibScalar
gmsTrapInfoTrapDescription = _GmsTrapInfoTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 8741, 3, 1, 1, 1, 2),
    _GmsTrapInfoTrapDescription_Type()
)
gmsTrapInfoTrapDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmsTrapInfoTrapDescription.setStatus("current")
_GmsTrapInfoSerial_Type = DisplayString
_GmsTrapInfoSerial_Object = MibScalar
gmsTrapInfoSerial = _GmsTrapInfoSerial_Object(
    (1, 3, 6, 1, 4, 1, 8741, 3, 1, 1, 1, 3),
    _GmsTrapInfoSerial_Type()
)
gmsTrapInfoSerial.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmsTrapInfoSerial.setStatus("current")
_GmsTrapInfoComponentType_Type = GmsComponentType
_GmsTrapInfoComponentType_Object = MibScalar
gmsTrapInfoComponentType = _GmsTrapInfoComponentType_Object(
    (1, 3, 6, 1, 4, 1, 8741, 3, 1, 1, 1, 4),
    _GmsTrapInfoComponentType_Type()
)
gmsTrapInfoComponentType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmsTrapInfoComponentType.setStatus("current")
_SonicwallGMSTrapRoot_ObjectIdentity = ObjectIdentity
sonicwallGMSTrapRoot = _SonicwallGMSTrapRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 3, 1, 2)
)

# Managed Objects groups


# Notification objects

gmsFwTrapAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 3, 1, 2, 0, 1)
)
gmsFwTrapAttack.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"),
        ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoSerial"),
        ("SNMP-COMMUNITY-MIB", "snmpTrapAddress"),
        ("SNMP-COMMUNITY-MIB", "snmpTrapCommunity"),
        ("SNMPv2-MIB", "snmpTrapEnterprise"))
)
if mibBuilder.loadTexts:
    gmsFwTrapAttack.setStatus(
        "current"
    )

gmsFwTrapSysError = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 3, 1, 2, 0, 2)
)
gmsFwTrapSysError.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"),
        ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoSerial"),
        ("SNMP-COMMUNITY-MIB", "snmpTrapAddress"),
        ("SNMP-COMMUNITY-MIB", "snmpTrapCommunity"),
        ("SNMPv2-MIB", "snmpTrapEnterprise"))
)
if mibBuilder.loadTexts:
    gmsFwTrapSysError.setStatus(
        "current"
    )

gmsFwTrapBlkWebSite = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 3, 1, 2, 0, 3)
)
gmsFwTrapBlkWebSite.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"),
        ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoSerial"),
        ("SNMP-COMMUNITY-MIB", "snmpTrapAddress"),
        ("SNMP-COMMUNITY-MIB", "snmpTrapCommunity"),
        ("SNMPv2-MIB", "snmpTrapEnterprise"))
)
if mibBuilder.loadTexts:
    gmsFwTrapBlkWebSite.setStatus(
        "current"
    )

gmsFwTrapIpsecTunnel = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 3, 1, 2, 0, 4)
)
gmsFwTrapIpsecTunnel.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"),
        ("SONICWALL-GMS-TRAP-MIB", "swTrapInfoSaName"),
        ("SONICWALL-GMS-TRAP-MIB", "swTrapInfoFwSrlNumber"),
        ("SONICWALL-GMS-TRAP-MIB", "swTrapInfoSaStatus"),
        ("SONICWALL-GMS-TRAP-MIB", "swTrapInfoSrcAddrBegin"),
        ("SONICWALL-GMS-TRAP-MIB", "swTrapInfoSrcAddrEnd"),
        ("SONICWALL-GMS-TRAP-MIB", "swTrapInfoDstAddrBegin"),
        ("SONICWALL-GMS-TRAP-MIB", "swTrapInfoDstAddrEnd"),
        ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoSerial"),
        ("SNMP-COMMUNITY-MIB", "snmpTrapAddress"),
        ("SNMP-COMMUNITY-MIB", "snmpTrapCommunity"),
        ("SNMPv2-MIB", "snmpTrapEnterprise"))
)
if mibBuilder.loadTexts:
    gmsFwTrapIpsecTunnel.setStatus(
        "current"
    )

gmsTrapStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 3, 1, 2, 0, 5)
)
gmsTrapStatus.setObjects(
      *(("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoTrapType"),
        ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoTrapDescription"),
        ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoSerial"),
        ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoComponentType"),
        ("SNMP-COMMUNITY-MIB", "snmpTrapAddress"),
        ("SNMP-COMMUNITY-MIB", "snmpTrapCommunity"),
        ("SNMPv2-MIB", "snmpTrapEnterprise"))
)
if mibBuilder.loadTexts:
    gmsTrapStatus.setStatus(
        "current"
    )

gmsTrapSysError = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 3, 1, 2, 0, 6)
)
gmsTrapSysError.setObjects(
      *(("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoTrapType"),
        ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoTrapDescription"),
        ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoSerial"),
        ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoComponentType"),
        ("SNMP-COMMUNITY-MIB", "snmpTrapAddress"),
        ("SNMP-COMMUNITY-MIB", "snmpTrapCommunity"),
        ("SNMPv2-MIB", "snmpTrapEnterprise"))
)
if mibBuilder.loadTexts:
    gmsTrapSysError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONICWALL-GMS-TRAP-MIB",
    **{"GmsTrapType": GmsTrapType,
       "GmsComponentType": GmsComponentType,
       "sonicwallGMSTrapModule": sonicwallGMSTrapModule,
       "sonicwallGMSTrapInfo": sonicwallGMSTrapInfo,
       "gmsTrapInfoTable": gmsTrapInfoTable,
       "gmsTrapInfoTrapType": gmsTrapInfoTrapType,
       "gmsTrapInfoTrapDescription": gmsTrapInfoTrapDescription,
       "gmsTrapInfoSerial": gmsTrapInfoSerial,
       "gmsTrapInfoComponentType": gmsTrapInfoComponentType,
       "sonicwallGMSTrapRoot": sonicwallGMSTrapRoot,
       "gmsFwTrapAttack": gmsFwTrapAttack,
       "gmsFwTrapSysError": gmsFwTrapSysError,
       "gmsFwTrapBlkWebSite": gmsFwTrapBlkWebSite,
       "gmsFwTrapIpsecTunnel": gmsFwTrapIpsecTunnel,
       "gmsTrapStatus": gmsTrapStatus,
       "gmsTrapSysError": gmsTrapSysError}
)
