#
# PySNMP MIB module SONICWALL-GMS-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/sonicwall/SONICWALL-GMS-TRAP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
snmpTrapCommunity, snmpTrapAddress = mibBuilder.importSymbols("SNMP-COMMUNITY-MIB", "snmpTrapCommunity", "snmpTrapAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
snmpTrapEnterprise, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTrapEnterprise")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, snmpModules, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "snmpModules", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
swTrapInfoTrapDescription, swTrapInfoTrapType = mibBuilder.importSymbols("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription", "swTrapInfoTrapType")
sonicwallGMS, = mibBuilder.importSymbols("SONICWALL-SMI", "sonicwallGMS")
sonicwallGMSTrapModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8741, 3, 1))
if mibBuilder.loadTexts: sonicwallGMSTrapModule.setLastUpdated('201308010000Z')
if mibBuilder.loadTexts: sonicwallGMSTrapModule.setOrganization('Dell SonicWall, Inc.')
class GmsTrapType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(100, 101, 102, 103, 104, 105, 106, 110, 120, 130, 200, 199))
    namedValues = NamedValues(("trapTypeStillAlive", 100), ("trapTypeLostContact", 101), ("trapTypeFirewallLostContact", 102), ("trapTypeNormalShutdown", 103), ("trapTypeStartup", 104), ("trapTypeStartContact", 105), ("trapTypeFirewallStartContact", 106), ("trapTypeFirewallMonDevicesUpDown", 110), ("trapTypeFirewallMonDevicesSNMPRTMAlert", 120), ("trapTypeFirewallEventMgmtAlert", 130), ("trapTypeUnspecified", 200), ("trapTypeStopSnmpManager", 199))

class GmsComponentType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 999))
    namedValues = NamedValues(("componentTypeGMSSNMPMgr", 0), ("componentTypeGMSConsole", 1), ("componentTypeGMSAgent", 2), ("componentTypeGateway", 3), ("componentTypeFirewall", 4), ("componentTypeViewpointScheduler", 5), ("componentTypeViewpointSummarizer", 6), ("componentTypeCLI", 7), ("componentTypeVisualTool", 8), ("componentTypeSyslogCollector", 9), ("componentTypeSGMSTool", 10), ("componentTypeSGMSMonitor", 11), ("componentTypeSGMSUpdater", 12), ("componentTypeSGMSJUnit", 13), ("componentTypeSGMSEventMgmt", 14), ("componentTypeSGMSWebServices", 15), ("componentTypeGMSUnknown", 999))

sonicwallGMSTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 8741, 3, 1, 1))
gmsTrapInfoTable = MibIdentifier((1, 3, 6, 1, 4, 1, 8741, 3, 1, 1, 1))
gmsTrapInfoTrapType = MibScalar((1, 3, 6, 1, 4, 1, 8741, 3, 1, 1, 1, 1), GmsTrapType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gmsTrapInfoTrapType.setStatus('current')
gmsTrapInfoTrapDescription = MibScalar((1, 3, 6, 1, 4, 1, 8741, 3, 1, 1, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gmsTrapInfoTrapDescription.setStatus('current')
gmsTrapInfoSerial = MibScalar((1, 3, 6, 1, 4, 1, 8741, 3, 1, 1, 1, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gmsTrapInfoSerial.setStatus('current')
gmsTrapInfoComponentType = MibScalar((1, 3, 6, 1, 4, 1, 8741, 3, 1, 1, 1, 4), GmsComponentType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gmsTrapInfoComponentType.setStatus('current')
sonicwallGMSTrapRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 8741, 3, 1, 2))
gmsFwTrapAttack = NotificationType((1, 3, 6, 1, 4, 1, 8741, 3, 1, 2, 0, 1)).setObjects(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"), ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"), ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoSerial"), ("SNMP-COMMUNITY-MIB", "snmpTrapAddress"), ("SNMP-COMMUNITY-MIB", "snmpTrapCommunity"), ("SNMPv2-MIB", "snmpTrapEnterprise"))
if mibBuilder.loadTexts: gmsFwTrapAttack.setStatus('current')
gmsFwTrapSysError = NotificationType((1, 3, 6, 1, 4, 1, 8741, 3, 1, 2, 0, 2)).setObjects(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"), ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"), ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoSerial"), ("SNMP-COMMUNITY-MIB", "snmpTrapAddress"), ("SNMP-COMMUNITY-MIB", "snmpTrapCommunity"), ("SNMPv2-MIB", "snmpTrapEnterprise"))
if mibBuilder.loadTexts: gmsFwTrapSysError.setStatus('current')
gmsFwTrapBlkWebSite = NotificationType((1, 3, 6, 1, 4, 1, 8741, 3, 1, 2, 0, 3)).setObjects(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"), ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"), ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoSerial"), ("SNMP-COMMUNITY-MIB", "snmpTrapAddress"), ("SNMP-COMMUNITY-MIB", "snmpTrapCommunity"), ("SNMPv2-MIB", "snmpTrapEnterprise"))
if mibBuilder.loadTexts: gmsFwTrapBlkWebSite.setStatus('current')
gmsFwTrapIpsecTunnel = NotificationType((1, 3, 6, 1, 4, 1, 8741, 3, 1, 2, 0, 4)).setObjects(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"), ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"), ("SONICWALL-GMS-TRAP-MIB", "swTrapInfoSaName"), ("SONICWALL-GMS-TRAP-MIB", "swTrapInfoFwSrlNumber"), ("SONICWALL-GMS-TRAP-MIB", "swTrapInfoSaStatus"), ("SONICWALL-GMS-TRAP-MIB", "swTrapInfoSrcAddrBegin"), ("SONICWALL-GMS-TRAP-MIB", "swTrapInfoSrcAddrEnd"), ("SONICWALL-GMS-TRAP-MIB", "swTrapInfoDstAddrBegin"), ("SONICWALL-GMS-TRAP-MIB", "swTrapInfoDstAddrEnd"), ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoSerial"), ("SNMP-COMMUNITY-MIB", "snmpTrapAddress"), ("SNMP-COMMUNITY-MIB", "snmpTrapCommunity"), ("SNMPv2-MIB", "snmpTrapEnterprise"))
if mibBuilder.loadTexts: gmsFwTrapIpsecTunnel.setStatus('current')
gmsTrapStatus = NotificationType((1, 3, 6, 1, 4, 1, 8741, 3, 1, 2, 0, 5)).setObjects(("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoTrapType"), ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoTrapDescription"), ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoSerial"), ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoComponentType"), ("SNMP-COMMUNITY-MIB", "snmpTrapAddress"), ("SNMP-COMMUNITY-MIB", "snmpTrapCommunity"), ("SNMPv2-MIB", "snmpTrapEnterprise"))
if mibBuilder.loadTexts: gmsTrapStatus.setStatus('current')
gmsTrapSysError = NotificationType((1, 3, 6, 1, 4, 1, 8741, 3, 1, 2, 0, 6)).setObjects(("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoTrapType"), ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoTrapDescription"), ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoSerial"), ("SONICWALL-GMS-TRAP-MIB", "gmsTrapInfoComponentType"), ("SNMP-COMMUNITY-MIB", "snmpTrapAddress"), ("SNMP-COMMUNITY-MIB", "snmpTrapCommunity"), ("SNMPv2-MIB", "snmpTrapEnterprise"))
if mibBuilder.loadTexts: gmsTrapSysError.setStatus('current')
mibBuilder.exportSymbols("SONICWALL-GMS-TRAP-MIB", gmsFwTrapBlkWebSite=gmsFwTrapBlkWebSite, gmsTrapInfoTable=gmsTrapInfoTable, sonicwallGMSTrapInfo=sonicwallGMSTrapInfo, sonicwallGMSTrapRoot=sonicwallGMSTrapRoot, GmsTrapType=GmsTrapType, gmsTrapSysError=gmsTrapSysError, GmsComponentType=GmsComponentType, gmsTrapInfoComponentType=gmsTrapInfoComponentType, gmsFwTrapAttack=gmsFwTrapAttack, PYSNMP_MODULE_ID=sonicwallGMSTrapModule, gmsTrapInfoSerial=gmsTrapInfoSerial, gmsFwTrapIpsecTunnel=gmsFwTrapIpsecTunnel, gmsTrapStatus=gmsTrapStatus, sonicwallGMSTrapModule=sonicwallGMSTrapModule, gmsTrapInfoTrapDescription=gmsTrapInfoTrapDescription, gmsFwTrapSysError=gmsFwTrapSysError, gmsTrapInfoTrapType=gmsTrapInfoTrapType)
