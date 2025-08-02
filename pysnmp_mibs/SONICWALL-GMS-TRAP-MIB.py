_O='gmsTrapInfoComponentType'
_N='gmsTrapInfoTrapDescription'
_M='gmsTrapInfoTrapType'
_L='accessible-for-notify'
_K='swTrapInfoTrapType'
_J='swTrapInfoTrapDescription'
_I='gmsTrapInfoSerial'
_H='snmpTrapEnterprise'
_G='SNMPv2-MIB'
_F='snmpTrapCommunity'
_E='snmpTrapAddress'
_D='SONICWALL-FIREWALL-TRAP-MIB'
_C='current'
_B='SNMP-COMMUNITY-MIB'
_A='SONICWALL-GMS-TRAP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snmpTrapAddress,snmpTrapCommunity=mibBuilder.importSymbols(_B,_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
snmpTrapEnterprise,=mibBuilder.importSymbols(_G,_H)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','snmpModules')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
swTrapInfoTrapDescription,swTrapInfoTrapType=mibBuilder.importSymbols(_D,_J,_K)
sonicwallGMS,=mibBuilder.importSymbols('SONICWALL-SMI','sonicwallGMS')
sonicwallGMSTrapModule=ModuleIdentity((1,3,6,1,4,1,8741,3,1))
class GmsTrapType(TextualConvention,Integer32):status=_C;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,101,102,103,104,105,106,110,120,130,199,200)));namedValues=NamedValues(*(('trapTypeStillAlive',100),('trapTypeLostContact',101),('trapTypeFirewallLostContact',102),('trapTypeNormalShutdown',103),('trapTypeStartup',104),('trapTypeStartContact',105),('trapTypeFirewallStartContact',106),('trapTypeFirewallMonDevicesUpDown',110),('trapTypeFirewallMonDevicesSNMPRTMAlert',120),('trapTypeFirewallEventMgmtAlert',130),('trapTypeStopSnmpManager',199),('trapTypeUnspecified',200)))
class GmsComponentType(TextualConvention,Integer32):status=_C;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,999)));namedValues=NamedValues(*(('componentTypeGMSSNMPMgr',0),('componentTypeGMSConsole',1),('componentTypeGMSAgent',2),('componentTypeGateway',3),('componentTypeFirewall',4),('componentTypeViewpointScheduler',5),('componentTypeViewpointSummarizer',6),('componentTypeCLI',7),('componentTypeVisualTool',8),('componentTypeSyslogCollector',9),('componentTypeSGMSTool',10),('componentTypeSGMSMonitor',11),('componentTypeSGMSUpdater',12),('componentTypeSGMSJUnit',13),('componentTypeSGMSEventMgmt',14),('componentTypeSGMSWebServices',15),('componentTypeGMSUnknown',999)))
_SonicwallGMSTrapInfo_ObjectIdentity=ObjectIdentity
sonicwallGMSTrapInfo=_SonicwallGMSTrapInfo_ObjectIdentity((1,3,6,1,4,1,8741,3,1,1))
_GmsTrapInfoTable_ObjectIdentity=ObjectIdentity
gmsTrapInfoTable=_GmsTrapInfoTable_ObjectIdentity((1,3,6,1,4,1,8741,3,1,1,1))
_GmsTrapInfoTrapType_Type=GmsTrapType
_GmsTrapInfoTrapType_Object=MibScalar
gmsTrapInfoTrapType=_GmsTrapInfoTrapType_Object((1,3,6,1,4,1,8741,3,1,1,1,1),_GmsTrapInfoTrapType_Type())
gmsTrapInfoTrapType.setMaxAccess(_L)
if mibBuilder.loadTexts:gmsTrapInfoTrapType.setStatus(_C)
_GmsTrapInfoTrapDescription_Type=DisplayString
_GmsTrapInfoTrapDescription_Object=MibScalar
gmsTrapInfoTrapDescription=_GmsTrapInfoTrapDescription_Object((1,3,6,1,4,1,8741,3,1,1,1,2),_GmsTrapInfoTrapDescription_Type())
gmsTrapInfoTrapDescription.setMaxAccess(_L)
if mibBuilder.loadTexts:gmsTrapInfoTrapDescription.setStatus(_C)
_GmsTrapInfoSerial_Type=DisplayString
_GmsTrapInfoSerial_Object=MibScalar
gmsTrapInfoSerial=_GmsTrapInfoSerial_Object((1,3,6,1,4,1,8741,3,1,1,1,3),_GmsTrapInfoSerial_Type())
gmsTrapInfoSerial.setMaxAccess(_L)
if mibBuilder.loadTexts:gmsTrapInfoSerial.setStatus(_C)
_GmsTrapInfoComponentType_Type=GmsComponentType
_GmsTrapInfoComponentType_Object=MibScalar
gmsTrapInfoComponentType=_GmsTrapInfoComponentType_Object((1,3,6,1,4,1,8741,3,1,1,1,4),_GmsTrapInfoComponentType_Type())
gmsTrapInfoComponentType.setMaxAccess(_L)
if mibBuilder.loadTexts:gmsTrapInfoComponentType.setStatus(_C)
_SonicwallGMSTrapRoot_ObjectIdentity=ObjectIdentity
sonicwallGMSTrapRoot=_SonicwallGMSTrapRoot_ObjectIdentity((1,3,6,1,4,1,8741,3,1,2))
gmsFwTrapAttack=NotificationType((1,3,6,1,4,1,8741,3,1,2,0,1))
gmsFwTrapAttack.setObjects(*((_D,_K),(_D,_J),(_A,_I),(_B,_E),(_B,_F),(_G,_H)))
if mibBuilder.loadTexts:gmsFwTrapAttack.setStatus(_C)
gmsFwTrapSysError=NotificationType((1,3,6,1,4,1,8741,3,1,2,0,2))
gmsFwTrapSysError.setObjects(*((_D,_K),(_D,_J),(_A,_I),(_B,_E),(_B,_F),(_G,_H)))
if mibBuilder.loadTexts:gmsFwTrapSysError.setStatus(_C)
gmsFwTrapBlkWebSite=NotificationType((1,3,6,1,4,1,8741,3,1,2,0,3))
gmsFwTrapBlkWebSite.setObjects(*((_D,_K),(_D,_J),(_A,_I),(_B,_E),(_B,_F),(_G,_H)))
if mibBuilder.loadTexts:gmsFwTrapBlkWebSite.setStatus(_C)
gmsFwTrapIpsecTunnel=NotificationType((1,3,6,1,4,1,8741,3,1,2,0,4))
gmsFwTrapIpsecTunnel.setObjects(*((_D,_K),(_D,_J),(_A,'swTrapInfoSaName'),(_A,'swTrapInfoFwSrlNumber'),(_A,'swTrapInfoSaStatus'),(_A,'swTrapInfoSrcAddrBegin'),(_A,'swTrapInfoSrcAddrEnd'),(_A,'swTrapInfoDstAddrBegin'),(_A,'swTrapInfoDstAddrEnd'),(_A,_I),(_B,_E),(_B,_F),(_G,_H)))
if mibBuilder.loadTexts:gmsFwTrapIpsecTunnel.setStatus(_C)
gmsTrapStatus=NotificationType((1,3,6,1,4,1,8741,3,1,2,0,5))
gmsTrapStatus.setObjects(*((_A,_M),(_A,_N),(_A,_I),(_A,_O),(_B,_E),(_B,_F),(_G,_H)))
if mibBuilder.loadTexts:gmsTrapStatus.setStatus(_C)
gmsTrapSysError=NotificationType((1,3,6,1,4,1,8741,3,1,2,0,6))
gmsTrapSysError.setObjects(*((_A,_M),(_A,_N),(_A,_I),(_A,_O),(_B,_E),(_B,_F),(_G,_H)))
if mibBuilder.loadTexts:gmsTrapSysError.setStatus(_C)
mibBuilder.exportSymbols(_A,**{'GmsTrapType':GmsTrapType,'GmsComponentType':GmsComponentType,'sonicwallGMSTrapModule':sonicwallGMSTrapModule,'sonicwallGMSTrapInfo':sonicwallGMSTrapInfo,'gmsTrapInfoTable':gmsTrapInfoTable,_M:gmsTrapInfoTrapType,_N:gmsTrapInfoTrapDescription,_I:gmsTrapInfoSerial,_O:gmsTrapInfoComponentType,'sonicwallGMSTrapRoot':sonicwallGMSTrapRoot,'gmsFwTrapAttack':gmsFwTrapAttack,'gmsFwTrapSysError':gmsFwTrapSysError,'gmsFwTrapBlkWebSite':gmsFwTrapBlkWebSite,'gmsFwTrapIpsecTunnel':gmsFwTrapIpsecTunnel,'gmsTrapStatus':gmsTrapStatus,'gmsTrapSysError':gmsTrapSysError})