_Q='rlIscsiSnoopConnectionInitiatorPort'
_P='rlIscsiSnoopConnectionInitiatorAddr'
_O='rlIscsiSnoopConnectionTargetPort'
_N='rlIscsiSnoopConnectionTargetAddr'
_M='rlIscsiSnoopTargetConfigAddr'
_L='rlIscsiSnoopTargetConfigTcpPort'
_K='rlIscsiSnoopQosKey'
_J='rlIscsiSnoopSessionISID'
_I='rlIscsiSnoopInitiatorNameId'
_H='rlIscsiSnoopTargetNameId'
_G='Integer32'
_F='DisplayString'
_E='not-accessible'
_D='read-write'
_C='read-only'
_B='NETGEAR-RADLAN-iscsi-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
class QosType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('vpt',0),('dscp',1)))
_RlIscsiSnoop_ObjectIdentity=ObjectIdentity
rlIscsiSnoop=_RlIscsiSnoop_ObjectIdentity((1,3,6,1,4,1,4526,17,126))
_RlIscsiSnoopEnable_Type=TruthValue
_RlIscsiSnoopEnable_Object=MibScalar
rlIscsiSnoopEnable=_RlIscsiSnoopEnable_Object((1,3,6,1,4,1,4526,17,126,1),_RlIscsiSnoopEnable_Type())
rlIscsiSnoopEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rlIscsiSnoopEnable.setStatus(_A)
class _RlIscsiSnoopAgingTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,2592000))
_RlIscsiSnoopAgingTimeOut_Type.__name__=_G
_RlIscsiSnoopAgingTimeOut_Object=MibScalar
rlIscsiSnoopAgingTimeOut=_RlIscsiSnoopAgingTimeOut_Object((1,3,6,1,4,1,4526,17,126,2),_RlIscsiSnoopAgingTimeOut_Type())
rlIscsiSnoopAgingTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:rlIscsiSnoopAgingTimeOut.setStatus(_A)
_RlIscsiSnoopQosTable_Object=MibTable
rlIscsiSnoopQosTable=_RlIscsiSnoopQosTable_Object((1,3,6,1,4,1,4526,17,126,3))
if mibBuilder.loadTexts:rlIscsiSnoopQosTable.setStatus(_A)
_RlIscsiSnoopQosEntry_Object=MibTableRow
rlIscsiSnoopQosEntry=_RlIscsiSnoopQosEntry_Object((1,3,6,1,4,1,4526,17,126,3,1))
rlIscsiSnoopQosEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:rlIscsiSnoopQosEntry.setStatus(_A)
class _RlIscsiSnoopQosKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_RlIscsiSnoopQosKey_Type.__name__=_G
_RlIscsiSnoopQosKey_Object=MibTableColumn
rlIscsiSnoopQosKey=_RlIscsiSnoopQosKey_Object((1,3,6,1,4,1,4526,17,126,3,1,1),_RlIscsiSnoopQosKey_Type())
rlIscsiSnoopQosKey.setMaxAccess(_E)
if mibBuilder.loadTexts:rlIscsiSnoopQosKey.setStatus(_A)
_RlIscsiSnoopQosType_Type=QosType
_RlIscsiSnoopQosType_Object=MibTableColumn
rlIscsiSnoopQosType=_RlIscsiSnoopQosType_Object((1,3,6,1,4,1,4526,17,126,3,1,2),_RlIscsiSnoopQosType_Type())
rlIscsiSnoopQosType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlIscsiSnoopQosType.setStatus(_A)
class _RlIscsiSnoopQosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RlIscsiSnoopQosValue_Type.__name__=_G
_RlIscsiSnoopQosValue_Object=MibTableColumn
rlIscsiSnoopQosValue=_RlIscsiSnoopQosValue_Object((1,3,6,1,4,1,4526,17,126,3,1,4),_RlIscsiSnoopQosValue_Type())
rlIscsiSnoopQosValue.setMaxAccess(_D)
if mibBuilder.loadTexts:rlIscsiSnoopQosValue.setStatus(_A)
_RlIscsiSnoopQosRemark_Type=TruthValue
_RlIscsiSnoopQosRemark_Object=MibTableColumn
rlIscsiSnoopQosRemark=_RlIscsiSnoopQosRemark_Object((1,3,6,1,4,1,4526,17,126,3,1,5),_RlIscsiSnoopQosRemark_Type())
rlIscsiSnoopQosRemark.setMaxAccess(_D)
if mibBuilder.loadTexts:rlIscsiSnoopQosRemark.setStatus(_A)
_RlIscsiSnoopTargetConfigTable_Object=MibTable
rlIscsiSnoopTargetConfigTable=_RlIscsiSnoopTargetConfigTable_Object((1,3,6,1,4,1,4526,17,126,4))
if mibBuilder.loadTexts:rlIscsiSnoopTargetConfigTable.setStatus(_A)
_RlIscsiSnoopTargetConfigEntry_Object=MibTableRow
rlIscsiSnoopTargetConfigEntry=_RlIscsiSnoopTargetConfigEntry_Object((1,3,6,1,4,1,4526,17,126,4,1))
rlIscsiSnoopTargetConfigEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:rlIscsiSnoopTargetConfigEntry.setStatus(_A)
_RlIscsiSnoopTargetConfigTcpPort_Type=Integer32
_RlIscsiSnoopTargetConfigTcpPort_Object=MibTableColumn
rlIscsiSnoopTargetConfigTcpPort=_RlIscsiSnoopTargetConfigTcpPort_Object((1,3,6,1,4,1,4526,17,126,4,1,1),_RlIscsiSnoopTargetConfigTcpPort_Type())
rlIscsiSnoopTargetConfigTcpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:rlIscsiSnoopTargetConfigTcpPort.setStatus(_A)
_RlIscsiSnoopTargetConfigAddr_Type=IpAddress
_RlIscsiSnoopTargetConfigAddr_Object=MibTableColumn
rlIscsiSnoopTargetConfigAddr=_RlIscsiSnoopTargetConfigAddr_Object((1,3,6,1,4,1,4526,17,126,4,1,3),_RlIscsiSnoopTargetConfigAddr_Type())
rlIscsiSnoopTargetConfigAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:rlIscsiSnoopTargetConfigAddr.setStatus(_A)
class _RlIscsiSnoopTargetConfigName1_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_RlIscsiSnoopTargetConfigName1_Type.__name__=_F
_RlIscsiSnoopTargetConfigName1_Object=MibTableColumn
rlIscsiSnoopTargetConfigName1=_RlIscsiSnoopTargetConfigName1_Object((1,3,6,1,4,1,4526,17,126,4,1,4),_RlIscsiSnoopTargetConfigName1_Type())
rlIscsiSnoopTargetConfigName1.setMaxAccess(_D)
if mibBuilder.loadTexts:rlIscsiSnoopTargetConfigName1.setStatus(_A)
class _RlIscsiSnoopTargetConfigName2_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_RlIscsiSnoopTargetConfigName2_Type.__name__=_F
_RlIscsiSnoopTargetConfigName2_Object=MibTableColumn
rlIscsiSnoopTargetConfigName2=_RlIscsiSnoopTargetConfigName2_Object((1,3,6,1,4,1,4526,17,126,4,1,5),_RlIscsiSnoopTargetConfigName2_Type())
rlIscsiSnoopTargetConfigName2.setMaxAccess(_D)
if mibBuilder.loadTexts:rlIscsiSnoopTargetConfigName2.setStatus(_A)
_RlIscsiSnoopTargetConfigStatus_Type=RowStatus
_RlIscsiSnoopTargetConfigStatus_Object=MibTableColumn
rlIscsiSnoopTargetConfigStatus=_RlIscsiSnoopTargetConfigStatus_Object((1,3,6,1,4,1,4526,17,126,4,1,6),_RlIscsiSnoopTargetConfigStatus_Type())
rlIscsiSnoopTargetConfigStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:rlIscsiSnoopTargetConfigStatus.setStatus(_A)
_RlIscsiSnoopTargetNameTable_Object=MibTable
rlIscsiSnoopTargetNameTable=_RlIscsiSnoopTargetNameTable_Object((1,3,6,1,4,1,4526,17,126,5))
if mibBuilder.loadTexts:rlIscsiSnoopTargetNameTable.setStatus(_A)
_RlIscsiSnoopTargetNameEntry_Object=MibTableRow
rlIscsiSnoopTargetNameEntry=_RlIscsiSnoopTargetNameEntry_Object((1,3,6,1,4,1,4526,17,126,5,1))
rlIscsiSnoopTargetNameEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:rlIscsiSnoopTargetNameEntry.setStatus(_A)
_RlIscsiSnoopTargetNameId_Type=Integer32
_RlIscsiSnoopTargetNameId_Object=MibTableColumn
rlIscsiSnoopTargetNameId=_RlIscsiSnoopTargetNameId_Object((1,3,6,1,4,1,4526,17,126,5,1,1),_RlIscsiSnoopTargetNameId_Type())
rlIscsiSnoopTargetNameId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlIscsiSnoopTargetNameId.setStatus(_A)
class _RlIscsiSnoopTargetName1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_RlIscsiSnoopTargetName1_Type.__name__=_F
_RlIscsiSnoopTargetName1_Object=MibTableColumn
rlIscsiSnoopTargetName1=_RlIscsiSnoopTargetName1_Object((1,3,6,1,4,1,4526,17,126,5,1,2),_RlIscsiSnoopTargetName1_Type())
rlIscsiSnoopTargetName1.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiSnoopTargetName1.setStatus(_A)
class _RlIscsiSnoopTargetName2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_RlIscsiSnoopTargetName2_Type.__name__=_F
_RlIscsiSnoopTargetName2_Object=MibTableColumn
rlIscsiSnoopTargetName2=_RlIscsiSnoopTargetName2_Object((1,3,6,1,4,1,4526,17,126,5,1,3),_RlIscsiSnoopTargetName2_Type())
rlIscsiSnoopTargetName2.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiSnoopTargetName2.setStatus(_A)
_RlIscsiSnoopInitiatorNameTable_Object=MibTable
rlIscsiSnoopInitiatorNameTable=_RlIscsiSnoopInitiatorNameTable_Object((1,3,6,1,4,1,4526,17,126,6))
if mibBuilder.loadTexts:rlIscsiSnoopInitiatorNameTable.setStatus(_A)
_RlIscsiSnoopInitiatorNameEntry_Object=MibTableRow
rlIscsiSnoopInitiatorNameEntry=_RlIscsiSnoopInitiatorNameEntry_Object((1,3,6,1,4,1,4526,17,126,6,1))
rlIscsiSnoopInitiatorNameEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:rlIscsiSnoopInitiatorNameEntry.setStatus(_A)
_RlIscsiSnoopInitiatorNameId_Type=Integer32
_RlIscsiSnoopInitiatorNameId_Object=MibTableColumn
rlIscsiSnoopInitiatorNameId=_RlIscsiSnoopInitiatorNameId_Object((1,3,6,1,4,1,4526,17,126,6,1,1),_RlIscsiSnoopInitiatorNameId_Type())
rlIscsiSnoopInitiatorNameId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlIscsiSnoopInitiatorNameId.setStatus(_A)
class _RlIscsiSnoopInitiatorName1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_RlIscsiSnoopInitiatorName1_Type.__name__=_F
_RlIscsiSnoopInitiatorName1_Object=MibTableColumn
rlIscsiSnoopInitiatorName1=_RlIscsiSnoopInitiatorName1_Object((1,3,6,1,4,1,4526,17,126,6,1,2),_RlIscsiSnoopInitiatorName1_Type())
rlIscsiSnoopInitiatorName1.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiSnoopInitiatorName1.setStatus(_A)
class _RlIscsiSnoopInitiatorName2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_RlIscsiSnoopInitiatorName2_Type.__name__=_F
_RlIscsiSnoopInitiatorName2_Object=MibTableColumn
rlIscsiSnoopInitiatorName2=_RlIscsiSnoopInitiatorName2_Object((1,3,6,1,4,1,4526,17,126,6,1,3),_RlIscsiSnoopInitiatorName2_Type())
rlIscsiSnoopInitiatorName2.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiSnoopInitiatorName2.setStatus(_A)
_RlIscsiSnoopSessionTable_Object=MibTable
rlIscsiSnoopSessionTable=_RlIscsiSnoopSessionTable_Object((1,3,6,1,4,1,4526,17,126,7))
if mibBuilder.loadTexts:rlIscsiSnoopSessionTable.setStatus(_A)
_RlIscsiSnoopSessionEntry_Object=MibTableRow
rlIscsiSnoopSessionEntry=_RlIscsiSnoopSessionEntry_Object((1,3,6,1,4,1,4526,17,126,7,1))
rlIscsiSnoopSessionEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:rlIscsiSnoopSessionEntry.setStatus(_A)
_RlIscsiSnoopSessionISID_Type=OctetString
_RlIscsiSnoopSessionISID_Object=MibTableColumn
rlIscsiSnoopSessionISID=_RlIscsiSnoopSessionISID_Object((1,3,6,1,4,1,4526,17,126,7,1,1),_RlIscsiSnoopSessionISID_Type())
rlIscsiSnoopSessionISID.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiSnoopSessionISID.setStatus(_A)
_RlIscsiSnoopSessAgingTime_Type=Integer32
_RlIscsiSnoopSessAgingTime_Object=MibTableColumn
rlIscsiSnoopSessAgingTime=_RlIscsiSnoopSessAgingTime_Object((1,3,6,1,4,1,4526,17,126,7,1,2),_RlIscsiSnoopSessAgingTime_Type())
rlIscsiSnoopSessAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiSnoopSessAgingTime.setStatus(_A)
_RlIscsiSnoopSessionUpTime_Type=Integer32
_RlIscsiSnoopSessionUpTime_Object=MibTableColumn
rlIscsiSnoopSessionUpTime=_RlIscsiSnoopSessionUpTime_Object((1,3,6,1,4,1,4526,17,126,7,1,3),_RlIscsiSnoopSessionUpTime_Type())
rlIscsiSnoopSessionUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiSnoopSessionUpTime.setStatus(_A)
_RlIscsiSnoopConnectionTable_Object=MibTable
rlIscsiSnoopConnectionTable=_RlIscsiSnoopConnectionTable_Object((1,3,6,1,4,1,4526,17,126,8))
if mibBuilder.loadTexts:rlIscsiSnoopConnectionTable.setStatus(_A)
_RlIscsiSnoopConnectionEntry_Object=MibTableRow
rlIscsiSnoopConnectionEntry=_RlIscsiSnoopConnectionEntry_Object((1,3,6,1,4,1,4526,17,126,8,1))
rlIscsiSnoopConnectionEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_N),(0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:rlIscsiSnoopConnectionEntry.setStatus(_A)
_RlIscsiSnoopConnectionTargetAddr_Type=IpAddress
_RlIscsiSnoopConnectionTargetAddr_Object=MibTableColumn
rlIscsiSnoopConnectionTargetAddr=_RlIscsiSnoopConnectionTargetAddr_Object((1,3,6,1,4,1,4526,17,126,8,1,2),_RlIscsiSnoopConnectionTargetAddr_Type())
rlIscsiSnoopConnectionTargetAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:rlIscsiSnoopConnectionTargetAddr.setStatus(_A)
_RlIscsiSnoopConnectionTargetPort_Type=Integer32
_RlIscsiSnoopConnectionTargetPort_Object=MibTableColumn
rlIscsiSnoopConnectionTargetPort=_RlIscsiSnoopConnectionTargetPort_Object((1,3,6,1,4,1,4526,17,126,8,1,3),_RlIscsiSnoopConnectionTargetPort_Type())
rlIscsiSnoopConnectionTargetPort.setMaxAccess(_E)
if mibBuilder.loadTexts:rlIscsiSnoopConnectionTargetPort.setStatus(_A)
_RlIscsiSnoopConnectionInitiatorAddr_Type=IpAddress
_RlIscsiSnoopConnectionInitiatorAddr_Object=MibTableColumn
rlIscsiSnoopConnectionInitiatorAddr=_RlIscsiSnoopConnectionInitiatorAddr_Object((1,3,6,1,4,1,4526,17,126,8,1,5),_RlIscsiSnoopConnectionInitiatorAddr_Type())
rlIscsiSnoopConnectionInitiatorAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:rlIscsiSnoopConnectionInitiatorAddr.setStatus(_A)
_RlIscsiSnoopConnectionInitiatorPort_Type=Integer32
_RlIscsiSnoopConnectionInitiatorPort_Object=MibTableColumn
rlIscsiSnoopConnectionInitiatorPort=_RlIscsiSnoopConnectionInitiatorPort_Object((1,3,6,1,4,1,4526,17,126,8,1,6),_RlIscsiSnoopConnectionInitiatorPort_Type())
rlIscsiSnoopConnectionInitiatorPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiSnoopConnectionInitiatorPort.setStatus(_A)
_RlIscsiSnoopConnectionCreationTime_Type=TimeStamp
_RlIscsiSnoopConnectionCreationTime_Object=MibTableColumn
rlIscsiSnoopConnectionCreationTime=_RlIscsiSnoopConnectionCreationTime_Object((1,3,6,1,4,1,4526,17,126,8,1,7),_RlIscsiSnoopConnectionCreationTime_Type())
rlIscsiSnoopConnectionCreationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiSnoopConnectionCreationTime.setStatus(_A)
_RlIscsiSnoopConnectionLastActTime_Type=TimeStamp
_RlIscsiSnoopConnectionLastActTime_Object=MibTableColumn
rlIscsiSnoopConnectionLastActTime=_RlIscsiSnoopConnectionLastActTime_Object((1,3,6,1,4,1,4526,17,126,8,1,8),_RlIscsiSnoopConnectionLastActTime_Type())
rlIscsiSnoopConnectionLastActTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiSnoopConnectionLastActTime.setStatus(_A)
_RlIscsiSnoopConnectionLastPollTime_Type=TimeStamp
_RlIscsiSnoopConnectionLastPollTime_Object=MibTableColumn
rlIscsiSnoopConnectionLastPollTime=_RlIscsiSnoopConnectionLastPollTime_Object((1,3,6,1,4,1,4526,17,126,8,1,9),_RlIscsiSnoopConnectionLastPollTime_Type())
rlIscsiSnoopConnectionLastPollTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiSnoopConnectionLastPollTime.setStatus(_A)
_RlIscsiSnoopConnectionExpiryTime_Type=TimeStamp
_RlIscsiSnoopConnectionExpiryTime_Object=MibTableColumn
rlIscsiSnoopConnectionExpiryTime=_RlIscsiSnoopConnectionExpiryTime_Object((1,3,6,1,4,1,4526,17,126,8,1,10),_RlIscsiSnoopConnectionExpiryTime_Type())
rlIscsiSnoopConnectionExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiSnoopConnectionExpiryTime.setStatus(_A)
_RlIscsiSnoopConnectionCounterIndex_Type=Unsigned32
_RlIscsiSnoopConnectionCounterIndex_Object=MibTableColumn
rlIscsiSnoopConnectionCounterIndex=_RlIscsiSnoopConnectionCounterIndex_Object((1,3,6,1,4,1,4526,17,126,8,1,11),_RlIscsiSnoopConnectionCounterIndex_Type())
rlIscsiSnoopConnectionCounterIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiSnoopConnectionCounterIndex.setStatus(_A)
_RlIscsiSnoopCosEnable_Type=TruthValue
_RlIscsiSnoopCosEnable_Object=MibScalar
rlIscsiSnoopCosEnable=_RlIscsiSnoopCosEnable_Object((1,3,6,1,4,1,4526,17,126,9),_RlIscsiSnoopCosEnable_Type())
rlIscsiSnoopCosEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rlIscsiSnoopCosEnable.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'QosType':QosType,'rlIscsiSnoop':rlIscsiSnoop,'rlIscsiSnoopEnable':rlIscsiSnoopEnable,'rlIscsiSnoopAgingTimeOut':rlIscsiSnoopAgingTimeOut,'rlIscsiSnoopQosTable':rlIscsiSnoopQosTable,'rlIscsiSnoopQosEntry':rlIscsiSnoopQosEntry,_K:rlIscsiSnoopQosKey,'rlIscsiSnoopQosType':rlIscsiSnoopQosType,'rlIscsiSnoopQosValue':rlIscsiSnoopQosValue,'rlIscsiSnoopQosRemark':rlIscsiSnoopQosRemark,'rlIscsiSnoopTargetConfigTable':rlIscsiSnoopTargetConfigTable,'rlIscsiSnoopTargetConfigEntry':rlIscsiSnoopTargetConfigEntry,_L:rlIscsiSnoopTargetConfigTcpPort,_M:rlIscsiSnoopTargetConfigAddr,'rlIscsiSnoopTargetConfigName1':rlIscsiSnoopTargetConfigName1,'rlIscsiSnoopTargetConfigName2':rlIscsiSnoopTargetConfigName2,'rlIscsiSnoopTargetConfigStatus':rlIscsiSnoopTargetConfigStatus,'rlIscsiSnoopTargetNameTable':rlIscsiSnoopTargetNameTable,'rlIscsiSnoopTargetNameEntry':rlIscsiSnoopTargetNameEntry,_H:rlIscsiSnoopTargetNameId,'rlIscsiSnoopTargetName1':rlIscsiSnoopTargetName1,'rlIscsiSnoopTargetName2':rlIscsiSnoopTargetName2,'rlIscsiSnoopInitiatorNameTable':rlIscsiSnoopInitiatorNameTable,'rlIscsiSnoopInitiatorNameEntry':rlIscsiSnoopInitiatorNameEntry,_I:rlIscsiSnoopInitiatorNameId,'rlIscsiSnoopInitiatorName1':rlIscsiSnoopInitiatorName1,'rlIscsiSnoopInitiatorName2':rlIscsiSnoopInitiatorName2,'rlIscsiSnoopSessionTable':rlIscsiSnoopSessionTable,'rlIscsiSnoopSessionEntry':rlIscsiSnoopSessionEntry,_J:rlIscsiSnoopSessionISID,'rlIscsiSnoopSessAgingTime':rlIscsiSnoopSessAgingTime,'rlIscsiSnoopSessionUpTime':rlIscsiSnoopSessionUpTime,'rlIscsiSnoopConnectionTable':rlIscsiSnoopConnectionTable,'rlIscsiSnoopConnectionEntry':rlIscsiSnoopConnectionEntry,_N:rlIscsiSnoopConnectionTargetAddr,_O:rlIscsiSnoopConnectionTargetPort,_P:rlIscsiSnoopConnectionInitiatorAddr,_Q:rlIscsiSnoopConnectionInitiatorPort,'rlIscsiSnoopConnectionCreationTime':rlIscsiSnoopConnectionCreationTime,'rlIscsiSnoopConnectionLastActTime':rlIscsiSnoopConnectionLastActTime,'rlIscsiSnoopConnectionLastPollTime':rlIscsiSnoopConnectionLastPollTime,'rlIscsiSnoopConnectionExpiryTime':rlIscsiSnoopConnectionExpiryTime,'rlIscsiSnoopConnectionCounterIndex':rlIscsiSnoopConnectionCounterIndex,'rlIscsiSnoopCosEnable':rlIscsiSnoopCosEnable})