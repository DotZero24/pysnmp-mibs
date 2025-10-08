#
# PySNMP MIB module SONICWALL-GMS-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/sonicwall/SONICWALL-GMS-TRAP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:36 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
snmpTrapCommunity, snmpTrapAddress = mibBuilder.importSymbols("SNMP-COMMUNITY-MIB", "snmpTrapCommunity", "snmpTrapAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
snmpTrapEnterprise, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTrapEnterprise")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, snmpModules, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "snmpModules", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("SONICWALL-GMS-TRAP-MIB", GmsComponentType=GmsComponentType, gmsTrapSysError=gmsTrapSysError, gmsTrapInfoComponentType=gmsTrapInfoComponentType, gmsTrapInfoTrapType=gmsTrapInfoTrapType, GmsTrapType=GmsTrapType, sonicwallGMSTrapInfo=sonicwallGMSTrapInfo, PYSNMP_MODULE_ID=sonicwallGMSTrapModule, gmsTrapInfoTrapDescription=gmsTrapInfoTrapDescription, gmsFwTrapSysError=gmsFwTrapSysError, gmsFwTrapIpsecTunnel=gmsFwTrapIpsecTunnel, gmsTrapStatus=gmsTrapStatus, gmsTrapInfoSerial=gmsTrapInfoSerial, sonicwallGMSTrapModule=sonicwallGMSTrapModule, gmsFwTrapAttack=gmsFwTrapAttack, gmsFwTrapBlkWebSite=gmsFwTrapBlkWebSite, gmsTrapInfoTable=gmsTrapInfoTable, sonicwallGMSTrapRoot=sonicwallGMSTrapRoot)
