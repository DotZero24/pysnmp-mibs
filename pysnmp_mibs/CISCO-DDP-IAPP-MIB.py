_Q='ciscoDdpIappNotificationGroup'
_P='ciscoDdpIappRogueApInfoGroup'
_O='ciscoDdpIappConfigGroup'
_N='cDdpIappLastRogueApNotif'
_M='cDdpIappRogueApNotifEnabled'
_L='cDdpIappPort'
_K='cDdpIappMcastIpAddr'
_J='cDdpIappMcastIpAddrType'
_I='read-only'
_H='TruthValue'
_G='MacAddress'
_F='InetAddress'
_E='CiscoPort'
_D='cDdpIappLastRogueApMacAddr'
_C='read-write'
_B='current'
_A='CISCO-DDP-IAPP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoPort,=mibBuilder.importSymbols('CISCO-TC',_E)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_F,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_G,'PhysAddress','TextualConvention',_H)
ciscoDdpIappMIB=ModuleIdentity((1,3,6,1,4,1,9,9,277))
if mibBuilder.loadTexts:ciscoDdpIappMIB.setRevisions(('2002-07-31 00:00','2002-07-17 00:00','2002-03-19 00:00','2002-03-07 00:00','2001-09-28 00:00'))
_CiscoDdpIappMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoDdpIappMIBNotifications=_CiscoDdpIappMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,277,0))
_CiscoDdpIappMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDdpIappMIBObjects=_CiscoDdpIappMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,277,1))
_CDdpIappGlobalConfig_ObjectIdentity=ObjectIdentity
cDdpIappGlobalConfig=_CDdpIappGlobalConfig_ObjectIdentity((1,3,6,1,4,1,9,9,277,1,1))
_CDdpIappMcastIpAddrType_Type=InetAddressType
_CDdpIappMcastIpAddrType_Object=MibScalar
cDdpIappMcastIpAddrType=_CDdpIappMcastIpAddrType_Object((1,3,6,1,4,1,9,9,277,1,1,1),_CDdpIappMcastIpAddrType_Type())
cDdpIappMcastIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cDdpIappMcastIpAddrType.setStatus(_B)
class _CDdpIappMcastIpAddr_Type(InetAddress):defaultHexValue='e0000128'
_CDdpIappMcastIpAddr_Type.__name__=_F
_CDdpIappMcastIpAddr_Object=MibScalar
cDdpIappMcastIpAddr=_CDdpIappMcastIpAddr_Object((1,3,6,1,4,1,9,9,277,1,1,2),_CDdpIappMcastIpAddr_Type())
cDdpIappMcastIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cDdpIappMcastIpAddr.setStatus(_B)
class _CDdpIappPort_Type(CiscoPort):defaultValue=2887
_CDdpIappPort_Type.__name__=_E
_CDdpIappPort_Object=MibScalar
cDdpIappPort=_CDdpIappPort_Object((1,3,6,1,4,1,9,9,277,1,1,3),_CDdpIappPort_Type())
cDdpIappPort.setMaxAccess(_I)
if mibBuilder.loadTexts:cDdpIappPort.setStatus(_B)
class _CDdpIappRogueApNotifEnabled_Type(TruthValue):defaultValue=2
_CDdpIappRogueApNotifEnabled_Type.__name__=_H
_CDdpIappRogueApNotifEnabled_Object=MibScalar
cDdpIappRogueApNotifEnabled=_CDdpIappRogueApNotifEnabled_Object((1,3,6,1,4,1,9,9,277,1,1,4),_CDdpIappRogueApNotifEnabled_Type())
cDdpIappRogueApNotifEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cDdpIappRogueApNotifEnabled.setStatus(_B)
_CDdpIappRogueApInfo_ObjectIdentity=ObjectIdentity
cDdpIappRogueApInfo=_CDdpIappRogueApInfo_ObjectIdentity((1,3,6,1,4,1,9,9,277,1,2))
class _CDdpIappLastRogueApMacAddr_Type(MacAddress):defaultHexValue='000000000000'
_CDdpIappLastRogueApMacAddr_Type.__name__=_G
_CDdpIappLastRogueApMacAddr_Object=MibScalar
cDdpIappLastRogueApMacAddr=_CDdpIappLastRogueApMacAddr_Object((1,3,6,1,4,1,9,9,277,1,2,1),_CDdpIappLastRogueApMacAddr_Type())
cDdpIappLastRogueApMacAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:cDdpIappLastRogueApMacAddr.setStatus(_B)
_CiscoDdpIappMIBConformance_ObjectIdentity=ObjectIdentity
ciscoDdpIappMIBConformance=_CiscoDdpIappMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,277,2))
_CiscoDdpIappMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDdpIappMIBCompliances=_CiscoDdpIappMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,277,2,1))
_CiscoDdpIappMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDdpIappMIBGroups=_CiscoDdpIappMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,277,2,2))
ciscoDdpIappConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,277,2,2,1))
ciscoDdpIappConfigGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:ciscoDdpIappConfigGroup.setStatus(_B)
ciscoDdpIappRogueApInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,277,2,2,2))
ciscoDdpIappRogueApInfoGroup.setObjects((_A,_D))
if mibBuilder.loadTexts:ciscoDdpIappRogueApInfoGroup.setStatus(_B)
cDdpIappLastRogueApNotif=NotificationType((1,3,6,1,4,1,9,9,277,0,1))
cDdpIappLastRogueApNotif.setObjects((_A,_D))
if mibBuilder.loadTexts:cDdpIappLastRogueApNotif.setStatus(_B)
ciscoDdpIappNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,277,2,2,3))
ciscoDdpIappNotificationGroup.setObjects((_A,_N))
if mibBuilder.loadTexts:ciscoDdpIappNotificationGroup.setStatus(_B)
ciscoDdpIappCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,277,2,1,1))
ciscoDdpIappCompliance.setObjects(*((_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciscoDdpIappCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoDdpIappMIB':ciscoDdpIappMIB,'ciscoDdpIappMIBNotifications':ciscoDdpIappMIBNotifications,_N:cDdpIappLastRogueApNotif,'ciscoDdpIappMIBObjects':ciscoDdpIappMIBObjects,'cDdpIappGlobalConfig':cDdpIappGlobalConfig,_J:cDdpIappMcastIpAddrType,_K:cDdpIappMcastIpAddr,_L:cDdpIappPort,_M:cDdpIappRogueApNotifEnabled,'cDdpIappRogueApInfo':cDdpIappRogueApInfo,_D:cDdpIappLastRogueApMacAddr,'ciscoDdpIappMIBConformance':ciscoDdpIappMIBConformance,'ciscoDdpIappMIBCompliances':ciscoDdpIappMIBCompliances,'ciscoDdpIappCompliance':ciscoDdpIappCompliance,'ciscoDdpIappMIBGroups':ciscoDdpIappMIBGroups,_O:ciscoDdpIappConfigGroup,_P:ciscoDdpIappRogueApInfoGroup,_Q:ciscoDdpIappNotificationGroup})