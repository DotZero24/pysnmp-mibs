_N='oacSnmpTrapConfigisEnabled'
_M='oacSnmpTrapConfigType'
_L='oacSnmpRemoteEngineId'
_K='oacSnmpCommunityAccessType'
_J='oacSnmpCommunityString'
_I='TruthValue'
_H='IpAddress'
_G='not-accessible'
_F='ONEACCESS-SNMP-CONFIG-MIB'
_E='Integer32'
_D='read-write'
_C='OctetString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oacExpIMIpAcl,oacExpIMManagement,oacMIBModules=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMIpAcl','oacExpIMManagement','oacMIBModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,_H,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
oacSnmpConfigMIB=ModuleIdentity((1,3,6,1,4,1,13191,1,100,2002))
if mibBuilder.loadTexts:oacSnmpConfigMIB.setRevisions(('2011-07-29 00:00','2011-07-26 00:00','2011-06-15 00:00','2010-07-08 00:01'))
_OacSnmpConfig_ObjectIdentity=ObjectIdentity
oacSnmpConfig=_OacSnmpConfig_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,20))
_OacSnmpConfigObjects_ObjectIdentity=ObjectIdentity
oacSnmpConfigObjects=_OacSnmpConfigObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,20,1))
class _OacSnmpSource_Type(OctetString):defaultValue=OctetString('any');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_OacSnmpSource_Type.__name__=_C
_OacSnmpSource_Object=MibScalar
oacSnmpSource=_OacSnmpSource_Object((1,3,6,1,4,1,13191,10,3,4,20,1,1),_OacSnmpSource_Type())
oacSnmpSource.setMaxAccess(_D)
if mibBuilder.loadTexts:oacSnmpSource.setStatus(_A)
class _OacSnmpTrapSource_Type(OctetString):defaultValue=OctetString('any');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_OacSnmpTrapSource_Type.__name__=_C
_OacSnmpTrapSource_Object=MibScalar
oacSnmpTrapSource=_OacSnmpTrapSource_Object((1,3,6,1,4,1,13191,10,3,4,20,1,2),_OacSnmpTrapSource_Type())
oacSnmpTrapSource.setMaxAccess(_D)
if mibBuilder.loadTexts:oacSnmpTrapSource.setStatus(_A)
class _OacSnmpMibIfDescrShort_Type(TruthValue):defaultValue=2
_OacSnmpMibIfDescrShort_Type.__name__=_I
_OacSnmpMibIfDescrShort_Object=MibScalar
oacSnmpMibIfDescrShort=_OacSnmpMibIfDescrShort_Object((1,3,6,1,4,1,13191,10,3,4,20,1,3),_OacSnmpMibIfDescrShort_Type())
oacSnmpMibIfDescrShort.setMaxAccess(_D)
if mibBuilder.loadTexts:oacSnmpMibIfDescrShort.setStatus(_A)
class _OacSnmpChassisId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OacSnmpChassisId_Type.__name__=_C
_OacSnmpChassisId_Object=MibScalar
oacSnmpChassisId=_OacSnmpChassisId_Object((1,3,6,1,4,1,13191,10,3,4,20,1,4),_OacSnmpChassisId_Type())
oacSnmpChassisId.setMaxAccess(_D)
if mibBuilder.loadTexts:oacSnmpChassisId.setStatus(_A)
class _OacSnmpMaxMsgSize_Type(Integer32):defaultValue=8192
_OacSnmpMaxMsgSize_Type.__name__=_E
_OacSnmpMaxMsgSize_Object=MibScalar
oacSnmpMaxMsgSize=_OacSnmpMaxMsgSize_Object((1,3,6,1,4,1,13191,10,3,4,20,1,5),_OacSnmpMaxMsgSize_Type())
oacSnmpMaxMsgSize.setMaxAccess(_D)
if mibBuilder.loadTexts:oacSnmpMaxMsgSize.setStatus(_A)
_OacSnmpCommunityConfigTable_Object=MibTable
oacSnmpCommunityConfigTable=_OacSnmpCommunityConfigTable_Object((1,3,6,1,4,1,13191,10,3,4,20,1,6))
if mibBuilder.loadTexts:oacSnmpCommunityConfigTable.setStatus(_A)
_OacSnmpCommunityConfigEntry_Object=MibTableRow
oacSnmpCommunityConfigEntry=_OacSnmpCommunityConfigEntry_Object((1,3,6,1,4,1,13191,10,3,4,20,1,6,1))
oacSnmpCommunityConfigEntry.setIndexNames((0,_F,_J),(0,_F,_K))
if mibBuilder.loadTexts:oacSnmpCommunityConfigEntry.setStatus(_A)
class _OacSnmpCommunityString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_OacSnmpCommunityString_Type.__name__=_C
_OacSnmpCommunityString_Object=MibTableColumn
oacSnmpCommunityString=_OacSnmpCommunityString_Object((1,3,6,1,4,1,13191,10,3,4,20,1,6,1,1),_OacSnmpCommunityString_Type())
oacSnmpCommunityString.setMaxAccess(_G)
if mibBuilder.loadTexts:oacSnmpCommunityString.setStatus(_A)
class _OacSnmpCommunityAccessType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('set-read-community',1),('set-write-community',2)))
_OacSnmpCommunityAccessType_Type.__name__=_E
_OacSnmpCommunityAccessType_Object=MibTableColumn
oacSnmpCommunityAccessType=_OacSnmpCommunityAccessType_Object((1,3,6,1,4,1,13191,10,3,4,20,1,6,1,2),_OacSnmpCommunityAccessType_Type())
oacSnmpCommunityAccessType.setMaxAccess(_G)
if mibBuilder.loadTexts:oacSnmpCommunityAccessType.setStatus(_A)
class _OacSnmpCommunityAclType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_OacSnmpCommunityAclType_Type.__name__=_E
_OacSnmpCommunityAclType_Object=MibTableColumn
oacSnmpCommunityAclType=_OacSnmpCommunityAclType_Object((1,3,6,1,4,1,13191,10,3,4,20,1,6,1,3),_OacSnmpCommunityAclType_Type())
oacSnmpCommunityAclType.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSnmpCommunityAclType.setStatus(_A)
class _OacSnmpCommunityAclName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OacSnmpCommunityAclName_Type.__name__=_C
_OacSnmpCommunityAclName_Object=MibTableColumn
oacSnmpCommunityAclName=_OacSnmpCommunityAclName_Object((1,3,6,1,4,1,13191,10,3,4,20,1,6,1,4),_OacSnmpCommunityAclName_Type())
oacSnmpCommunityAclName.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSnmpCommunityAclName.setStatus(_A)
class _OacSnmpCommunityV2GroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OacSnmpCommunityV2GroupName_Type.__name__=_C
_OacSnmpCommunityV2GroupName_Object=MibTableColumn
oacSnmpCommunityV2GroupName=_OacSnmpCommunityV2GroupName_Object((1,3,6,1,4,1,13191,10,3,4,20,1,6,1,5),_OacSnmpCommunityV2GroupName_Type())
oacSnmpCommunityV2GroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSnmpCommunityV2GroupName.setStatus(_A)
_OacSnmpCommunityisEncrypted_Type=TruthValue
_OacSnmpCommunityisEncrypted_Object=MibTableColumn
oacSnmpCommunityisEncrypted=_OacSnmpCommunityisEncrypted_Object((1,3,6,1,4,1,13191,10,3,4,20,1,6,1,6),_OacSnmpCommunityisEncrypted_Type())
oacSnmpCommunityisEncrypted.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSnmpCommunityisEncrypted.setStatus(_A)
_OacSnmpCommunityRowStatus_Type=RowStatus
_OacSnmpCommunityRowStatus_Object=MibTableColumn
oacSnmpCommunityRowStatus=_OacSnmpCommunityRowStatus_Object((1,3,6,1,4,1,13191,10,3,4,20,1,6,1,7),_OacSnmpCommunityRowStatus_Type())
oacSnmpCommunityRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSnmpCommunityRowStatus.setStatus(_A)
class _OacSnmpEngineId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_OacSnmpEngineId_Type.__name__=_C
_OacSnmpEngineId_Object=MibScalar
oacSnmpEngineId=_OacSnmpEngineId_Object((1,3,6,1,4,1,13191,10,3,4,20,1,7),_OacSnmpEngineId_Type())
oacSnmpEngineId.setMaxAccess(_D)
if mibBuilder.loadTexts:oacSnmpEngineId.setStatus(_A)
class _OacSnmpRemoteAgentIpAddr_Type(IpAddress):defaultHexValue='00000000'
_OacSnmpRemoteAgentIpAddr_Type.__name__=_H
_OacSnmpRemoteAgentIpAddr_Object=MibScalar
oacSnmpRemoteAgentIpAddr=_OacSnmpRemoteAgentIpAddr_Object((1,3,6,1,4,1,13191,10,3,4,20,1,8),_OacSnmpRemoteAgentIpAddr_Type())
oacSnmpRemoteAgentIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:oacSnmpRemoteAgentIpAddr.setStatus(_A)
_OacSnmpRemoteEngineIdConfigTable_Object=MibTable
oacSnmpRemoteEngineIdConfigTable=_OacSnmpRemoteEngineIdConfigTable_Object((1,3,6,1,4,1,13191,10,3,4,20,1,9))
if mibBuilder.loadTexts:oacSnmpRemoteEngineIdConfigTable.setStatus(_A)
_OacSnmpRemoteEngineIdConfigEntry_Object=MibTableRow
oacSnmpRemoteEngineIdConfigEntry=_OacSnmpRemoteEngineIdConfigEntry_Object((1,3,6,1,4,1,13191,10,3,4,20,1,9,1))
oacSnmpRemoteEngineIdConfigEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:oacSnmpRemoteEngineIdConfigEntry.setStatus(_A)
class _OacSnmpRemoteEngineId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_OacSnmpRemoteEngineId_Type.__name__=_C
_OacSnmpRemoteEngineId_Object=MibTableColumn
oacSnmpRemoteEngineId=_OacSnmpRemoteEngineId_Object((1,3,6,1,4,1,13191,10,3,4,20,1,9,1,1),_OacSnmpRemoteEngineId_Type())
oacSnmpRemoteEngineId.setMaxAccess(_G)
if mibBuilder.loadTexts:oacSnmpRemoteEngineId.setStatus(_A)
_OacSnmpRemoteEngineIpAddr_Type=IpAddress
_OacSnmpRemoteEngineIpAddr_Object=MibTableColumn
oacSnmpRemoteEngineIpAddr=_OacSnmpRemoteEngineIpAddr_Object((1,3,6,1,4,1,13191,10,3,4,20,1,9,1,2),_OacSnmpRemoteEngineIpAddr_Type())
oacSnmpRemoteEngineIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSnmpRemoteEngineIpAddr.setStatus(_A)
class _OacSnmpRemoteEngineMaxMsgSize_Type(Integer32):defaultValue=8192;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(484,8192))
_OacSnmpRemoteEngineMaxMsgSize_Type.__name__=_E
_OacSnmpRemoteEngineMaxMsgSize_Object=MibTableColumn
oacSnmpRemoteEngineMaxMsgSize=_OacSnmpRemoteEngineMaxMsgSize_Object((1,3,6,1,4,1,13191,10,3,4,20,1,9,1,3),_OacSnmpRemoteEngineMaxMsgSize_Type())
oacSnmpRemoteEngineMaxMsgSize.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSnmpRemoteEngineMaxMsgSize.setStatus(_A)
_OacSnmpRemoteEngineRowstatus_Type=RowStatus
_OacSnmpRemoteEngineRowstatus_Object=MibTableColumn
oacSnmpRemoteEngineRowstatus=_OacSnmpRemoteEngineRowstatus_Object((1,3,6,1,4,1,13191,10,3,4,20,1,9,1,4),_OacSnmpRemoteEngineRowstatus_Type())
oacSnmpRemoteEngineRowstatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSnmpRemoteEngineRowstatus.setStatus(_A)
_OacSnmpTrapConfigTable_Object=MibTable
oacSnmpTrapConfigTable=_OacSnmpTrapConfigTable_Object((1,3,6,1,4,1,13191,10,3,4,20,1,10))
if mibBuilder.loadTexts:oacSnmpTrapConfigTable.setStatus(_A)
_OacSnmpTrapConfigEntry_Object=MibTableRow
oacSnmpTrapConfigEntry=_OacSnmpTrapConfigEntry_Object((1,3,6,1,4,1,13191,10,3,4,20,1,10,1))
oacSnmpTrapConfigEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:oacSnmpTrapConfigEntry.setStatus(_A)
class _OacSnmpTrapConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('standard',1),('acl',2),('bgp',3),('ipsec',4),('isakmp',5),('isdn',6),('nat',7),('pstn',8),('vrrp',9)))
_OacSnmpTrapConfigType_Type.__name__=_E
_OacSnmpTrapConfigType_Object=MibTableColumn
oacSnmpTrapConfigType=_OacSnmpTrapConfigType_Object((1,3,6,1,4,1,13191,10,3,4,20,1,10,1,1),_OacSnmpTrapConfigType_Type())
oacSnmpTrapConfigType.setMaxAccess(_G)
if mibBuilder.loadTexts:oacSnmpTrapConfigType.setStatus(_A)
_OacSnmpTrapConfigisEnabled_Type=TruthValue
_OacSnmpTrapConfigisEnabled_Object=MibTableColumn
oacSnmpTrapConfigisEnabled=_OacSnmpTrapConfigisEnabled_Object((1,3,6,1,4,1,13191,10,3,4,20,1,10,1,2),_OacSnmpTrapConfigisEnabled_Type())
oacSnmpTrapConfigisEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSnmpTrapConfigisEnabled.setStatus(_A)
_OacSnmpTrapConfigRowStatus_Type=RowStatus
_OacSnmpTrapConfigRowStatus_Object=MibTableColumn
oacSnmpTrapConfigRowStatus=_OacSnmpTrapConfigRowStatus_Object((1,3,6,1,4,1,13191,10,3,4,20,1,10,1,3),_OacSnmpTrapConfigRowStatus_Type())
oacSnmpTrapConfigRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSnmpTrapConfigRowStatus.setStatus(_A)
_OacSnmpConfigConformance_ObjectIdentity=ObjectIdentity
oacSnmpConfigConformance=_OacSnmpConfigConformance_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,20,2))
_OacSnmpConfigGroups_ObjectIdentity=ObjectIdentity
oacSnmpConfigGroups=_OacSnmpConfigGroups_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,20,2,1))
_OacSnmpCompls_ObjectIdentity=ObjectIdentity
oacSnmpCompls=_OacSnmpCompls_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,20,2,2))
oacSnmpConfigGroup=ObjectGroup((1,3,6,1,4,1,13191,10,3,4,20,2,1,1))
oacSnmpConfigGroup.setObjects((_F,_N))
if mibBuilder.loadTexts:oacSnmpConfigGroup.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'oacSnmpConfigMIB':oacSnmpConfigMIB,'oacSnmpConfig':oacSnmpConfig,'oacSnmpConfigObjects':oacSnmpConfigObjects,'oacSnmpSource':oacSnmpSource,'oacSnmpTrapSource':oacSnmpTrapSource,'oacSnmpMibIfDescrShort':oacSnmpMibIfDescrShort,'oacSnmpChassisId':oacSnmpChassisId,'oacSnmpMaxMsgSize':oacSnmpMaxMsgSize,'oacSnmpCommunityConfigTable':oacSnmpCommunityConfigTable,'oacSnmpCommunityConfigEntry':oacSnmpCommunityConfigEntry,_J:oacSnmpCommunityString,_K:oacSnmpCommunityAccessType,'oacSnmpCommunityAclType':oacSnmpCommunityAclType,'oacSnmpCommunityAclName':oacSnmpCommunityAclName,'oacSnmpCommunityV2GroupName':oacSnmpCommunityV2GroupName,'oacSnmpCommunityisEncrypted':oacSnmpCommunityisEncrypted,'oacSnmpCommunityRowStatus':oacSnmpCommunityRowStatus,'oacSnmpEngineId':oacSnmpEngineId,'oacSnmpRemoteAgentIpAddr':oacSnmpRemoteAgentIpAddr,'oacSnmpRemoteEngineIdConfigTable':oacSnmpRemoteEngineIdConfigTable,'oacSnmpRemoteEngineIdConfigEntry':oacSnmpRemoteEngineIdConfigEntry,_L:oacSnmpRemoteEngineId,'oacSnmpRemoteEngineIpAddr':oacSnmpRemoteEngineIpAddr,'oacSnmpRemoteEngineMaxMsgSize':oacSnmpRemoteEngineMaxMsgSize,'oacSnmpRemoteEngineRowstatus':oacSnmpRemoteEngineRowstatus,'oacSnmpTrapConfigTable':oacSnmpTrapConfigTable,'oacSnmpTrapConfigEntry':oacSnmpTrapConfigEntry,_M:oacSnmpTrapConfigType,_N:oacSnmpTrapConfigisEnabled,'oacSnmpTrapConfigRowStatus':oacSnmpTrapConfigRowStatus,'oacSnmpConfigConformance':oacSnmpConfigConformance,'oacSnmpConfigGroups':oacSnmpConfigGroups,'oacSnmpConfigGroup':oacSnmpConfigGroup,'oacSnmpCompls':oacSnmpCompls})