_U='rcHisNotifsAlarmIndex'
_T='not-accessible'
_S='rcCurNotifsAlarmIndex'
_R='rcNotifsPortAlarmInverseIfIndex'
_Q='rcNotifsPortAlarmInversePhysicalID'
_P='manual'
_O='rcNotifsPortAlarmFilterIfIndex'
_N='rcNotifsPortAlarmFilterPhysicalID'
_M='rcNotifsPortFilterIndex'
_L='rcNotifsFilterAlarmTrapOID'
_K='rcNotifsTrapIndex'
_J='disable'
_I='enable'
_H='TruthValue'
_G='read-create'
_F='RAISECOM-NOTIFICATION-MIB'
_E='OctetString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
optSysMgmt,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','optSysMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_H)
raisecomNotifisMib=ModuleIdentity((1,3,6,1,4,1,8886,15,1,3))
_RcNotifsConfObjects_ObjectIdentity=ObjectIdentity
rcNotifsConfObjects=_RcNotifsConfObjects_ObjectIdentity((1,3,6,1,4,1,8886,15,1,3,1))
class _RcNotifsTrapVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('snmpv1',1),('snmpv2c',2)))
_RcNotifsTrapVersion_Type.__name__=_D
_RcNotifsTrapVersion_Object=MibScalar
rcNotifsTrapVersion=_RcNotifsTrapVersion_Object((1,3,6,1,4,1,8886,15,1,3,1,1),_RcNotifsTrapVersion_Type())
rcNotifsTrapVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsTrapVersion.setStatus(_A)
class _RcNotifsTrapEnable_Type(TruthValue):defaultValue=1
_RcNotifsTrapEnable_Type.__name__=_H
_RcNotifsTrapEnable_Object=MibScalar
rcNotifsTrapEnable=_RcNotifsTrapEnable_Object((1,3,6,1,4,1,8886,15,1,3,1,3),_RcNotifsTrapEnable_Type())
rcNotifsTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsTrapEnable.setStatus(_A)
_RcNotifsTrapTotalNumber_Type=Integer32
_RcNotifsTrapTotalNumber_Object=MibScalar
rcNotifsTrapTotalNumber=_RcNotifsTrapTotalNumber_Object((1,3,6,1,4,1,8886,15,1,3,1,5),_RcNotifsTrapTotalNumber_Type())
rcNotifsTrapTotalNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsTrapTotalNumber.setStatus(_A)
_RcNotifsTrapLocation_Type=DisplayString
_RcNotifsTrapLocation_Object=MibScalar
rcNotifsTrapLocation=_RcNotifsTrapLocation_Object((1,3,6,1,4,1,8886,15,1,3,1,6),_RcNotifsTrapLocation_Type())
rcNotifsTrapLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsTrapLocation.setStatus(_A)
class _RcNotifsTrapFilterSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),('off',2),('locked_off',3)))
_RcNotifsTrapFilterSwitch_Type.__name__=_D
_RcNotifsTrapFilterSwitch_Object=MibScalar
rcNotifsTrapFilterSwitch=_RcNotifsTrapFilterSwitch_Object((1,3,6,1,4,1,8886,15,1,3,1,7),_RcNotifsTrapFilterSwitch_Type())
rcNotifsTrapFilterSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsTrapFilterSwitch.setStatus(_A)
_RcNotifsAlarmOutputGroup_Type=Integer32
_RcNotifsAlarmOutputGroup_Object=MibScalar
rcNotifsAlarmOutputGroup=_RcNotifsAlarmOutputGroup_Object((1,3,6,1,4,1,8886,15,1,3,1,8),_RcNotifsAlarmOutputGroup_Type())
rcNotifsAlarmOutputGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsAlarmOutputGroup.setStatus(_A)
_RcNotifsTrapSinkTable_Object=MibTable
rcNotifsTrapSinkTable=_RcNotifsTrapSinkTable_Object((1,3,6,1,4,1,8886,15,1,3,1,10))
if mibBuilder.loadTexts:rcNotifsTrapSinkTable.setStatus(_A)
_RcNotifsTrapSinkEntry_Object=MibTableRow
rcNotifsTrapSinkEntry=_RcNotifsTrapSinkEntry_Object((1,3,6,1,4,1,8886,15,1,3,1,10,1))
rcNotifsTrapSinkEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:rcNotifsTrapSinkEntry.setStatus(_A)
class _RcNotifsTrapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RcNotifsTrapIndex_Type.__name__=_D
_RcNotifsTrapIndex_Object=MibTableColumn
rcNotifsTrapIndex=_RcNotifsTrapIndex_Object((1,3,6,1,4,1,8886,15,1,3,1,10,1,1),_RcNotifsTrapIndex_Type())
rcNotifsTrapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsTrapIndex.setStatus(_A)
_RcNotifsTrapTarget_Type=IpAddress
_RcNotifsTrapTarget_Object=MibTableColumn
rcNotifsTrapTarget=_RcNotifsTrapTarget_Object((1,3,6,1,4,1,8886,15,1,3,1,10,1,2),_RcNotifsTrapTarget_Type())
rcNotifsTrapTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsTrapTarget.setStatus(_A)
class _RcNotifsTrapPort_Type(Integer32):defaultValue=162
_RcNotifsTrapPort_Type.__name__=_D
_RcNotifsTrapPort_Object=MibTableColumn
rcNotifsTrapPort=_RcNotifsTrapPort_Object((1,3,6,1,4,1,8886,15,1,3,1,10,1,3),_RcNotifsTrapPort_Type())
rcNotifsTrapPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsTrapPort.setStatus(_A)
_RcNotifsAlarmFilterTable_Object=MibTable
rcNotifsAlarmFilterTable=_RcNotifsAlarmFilterTable_Object((1,3,6,1,4,1,8886,15,1,3,1,11))
if mibBuilder.loadTexts:rcNotifsAlarmFilterTable.setStatus(_A)
_RcNotifsAlarmFilterEntry_Object=MibTableRow
rcNotifsAlarmFilterEntry=_RcNotifsAlarmFilterEntry_Object((1,3,6,1,4,1,8886,15,1,3,1,11,1))
rcNotifsAlarmFilterEntry.setIndexNames((1,_F,_L))
if mibBuilder.loadTexts:rcNotifsAlarmFilterEntry.setStatus(_A)
_RcNotifsFilterAlarmTrapOID_Type=ObjectIdentifier
_RcNotifsFilterAlarmTrapOID_Object=MibTableColumn
rcNotifsFilterAlarmTrapOID=_RcNotifsFilterAlarmTrapOID_Object((1,3,6,1,4,1,8886,15,1,3,1,11,1,1),_RcNotifsFilterAlarmTrapOID_Type())
rcNotifsFilterAlarmTrapOID.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsFilterAlarmTrapOID.setStatus(_A)
class _RcNotifsAlarmTrapEnable_Type(TruthValue):defaultValue=1
_RcNotifsAlarmTrapEnable_Type.__name__=_H
_RcNotifsAlarmTrapEnable_Object=MibTableColumn
rcNotifsAlarmTrapEnable=_RcNotifsAlarmTrapEnable_Object((1,3,6,1,4,1,8886,15,1,3,1,11,1,2),_RcNotifsAlarmTrapEnable_Type())
rcNotifsAlarmTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsAlarmTrapEnable.setStatus(_A)
class _RcNotifsAlarmTrapLogEnable_Type(TruthValue):defaultValue=1
_RcNotifsAlarmTrapLogEnable_Type.__name__=_H
_RcNotifsAlarmTrapLogEnable_Object=MibTableColumn
rcNotifsAlarmTrapLogEnable=_RcNotifsAlarmTrapLogEnable_Object((1,3,6,1,4,1,8886,15,1,3,1,11,1,3),_RcNotifsAlarmTrapLogEnable_Type())
rcNotifsAlarmTrapLogEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsAlarmTrapLogEnable.setStatus(_A)
class _RcNotifsAlarmFilterControl_Type(TruthValue):defaultValue=1
_RcNotifsAlarmFilterControl_Type.__name__=_H
_RcNotifsAlarmFilterControl_Object=MibTableColumn
rcNotifsAlarmFilterControl=_RcNotifsAlarmFilterControl_Object((1,3,6,1,4,1,8886,15,1,3,1,11,1,4),_RcNotifsAlarmFilterControl_Type())
rcNotifsAlarmFilterControl.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsAlarmFilterControl.setStatus(_A)
class _RcNotifsAlarmOutputEnable_Type(Integer32):defaultValue=0
_RcNotifsAlarmOutputEnable_Type.__name__=_D
_RcNotifsAlarmOutputEnable_Object=MibTableColumn
rcNotifsAlarmOutputEnable=_RcNotifsAlarmOutputEnable_Object((1,3,6,1,4,1,8886,15,1,3,1,11,1,5),_RcNotifsAlarmOutputEnable_Type())
rcNotifsAlarmOutputEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsAlarmOutputEnable.setStatus(_A)
class _RcNotifsAlarmMonitoringDisable_Type(TruthValue):defaultValue=2
_RcNotifsAlarmMonitoringDisable_Type.__name__=_H
_RcNotifsAlarmMonitoringDisable_Object=MibTableColumn
rcNotifsAlarmMonitoringDisable=_RcNotifsAlarmMonitoringDisable_Object((1,3,6,1,4,1,8886,15,1,3,1,11,1,6),_RcNotifsAlarmMonitoringDisable_Type())
rcNotifsAlarmMonitoringDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsAlarmMonitoringDisable.setStatus(_A)
_RcNotifsPortFilterConfig_ObjectIdentity=ObjectIdentity
rcNotifsPortFilterConfig=_RcNotifsPortFilterConfig_ObjectIdentity((1,3,6,1,4,1,8886,15,1,3,1,15))
_RcNotifsPortFilterIndexNext_Type=Integer32
_RcNotifsPortFilterIndexNext_Object=MibScalar
rcNotifsPortFilterIndexNext=_RcNotifsPortFilterIndexNext_Object((1,3,6,1,4,1,8886,15,1,3,1,15,1),_RcNotifsPortFilterIndexNext_Type())
rcNotifsPortFilterIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsPortFilterIndexNext.setStatus(_A)
_RcNotifsPortFilterTable_Object=MibTable
rcNotifsPortFilterTable=_RcNotifsPortFilterTable_Object((1,3,6,1,4,1,8886,15,1,3,1,15,2))
if mibBuilder.loadTexts:rcNotifsPortFilterTable.setStatus(_A)
_RcNotifsPortFilterEntry_Object=MibTableRow
rcNotifsPortFilterEntry=_RcNotifsPortFilterEntry_Object((1,3,6,1,4,1,8886,15,1,3,1,15,2,1))
rcNotifsPortFilterEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:rcNotifsPortFilterEntry.setStatus(_A)
_RcNotifsPortFilterIndex_Type=Integer32
_RcNotifsPortFilterIndex_Object=MibTableColumn
rcNotifsPortFilterIndex=_RcNotifsPortFilterIndex_Object((1,3,6,1,4,1,8886,15,1,3,1,15,2,1,1),_RcNotifsPortFilterIndex_Type())
rcNotifsPortFilterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsPortFilterIndex.setStatus(_A)
_RcNotifsPortIfIndex_Type=Integer32
_RcNotifsPortIfIndex_Object=MibTableColumn
rcNotifsPortIfIndex=_RcNotifsPortIfIndex_Object((1,3,6,1,4,1,8886,15,1,3,1,15,2,1,2),_RcNotifsPortIfIndex_Type())
rcNotifsPortIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rcNotifsPortIfIndex.setStatus(_A)
_RcNotifsPortFilterRowStatus_Type=RowStatus
_RcNotifsPortFilterRowStatus_Object=MibTableColumn
rcNotifsPortFilterRowStatus=_RcNotifsPortFilterRowStatus_Object((1,3,6,1,4,1,8886,15,1,3,1,15,2,1,3),_RcNotifsPortFilterRowStatus_Type())
rcNotifsPortFilterRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rcNotifsPortFilterRowStatus.setStatus(_A)
class _RcNotifsTrapPhysicalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_RcNotifsTrapPhysicalID_Type.__name__=_E
_RcNotifsTrapPhysicalID_Object=MibScalar
rcNotifsTrapPhysicalID=_RcNotifsTrapPhysicalID_Object((1,3,6,1,4,1,8886,15,1,3,1,20),_RcNotifsTrapPhysicalID_Type())
rcNotifsTrapPhysicalID.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsTrapPhysicalID.setStatus(_A)
_RcNotifsTrapIfIndex_Type=Integer32
_RcNotifsTrapIfIndex_Object=MibScalar
rcNotifsTrapIfIndex=_RcNotifsTrapIfIndex_Object((1,3,6,1,4,1,8886,15,1,3,1,21),_RcNotifsTrapIfIndex_Type())
rcNotifsTrapIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsTrapIfIndex.setStatus(_A)
_RcNotifsTrapBindVariable1_Type=Integer32
_RcNotifsTrapBindVariable1_Object=MibScalar
rcNotifsTrapBindVariable1=_RcNotifsTrapBindVariable1_Object((1,3,6,1,4,1,8886,15,1,3,1,22),_RcNotifsTrapBindVariable1_Type())
rcNotifsTrapBindVariable1.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsTrapBindVariable1.setStatus(_A)
_RcNotifsTrapBindVariable2_Type=Integer32
_RcNotifsTrapBindVariable2_Object=MibScalar
rcNotifsTrapBindVariable2=_RcNotifsTrapBindVariable2_Object((1,3,6,1,4,1,8886,15,1,3,1,23),_RcNotifsTrapBindVariable2_Type())
rcNotifsTrapBindVariable2.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsTrapBindVariable2.setStatus(_A)
_RcNotifsTrapBindVariable3_Type=Integer32
_RcNotifsTrapBindVariable3_Object=MibScalar
rcNotifsTrapBindVariable3=_RcNotifsTrapBindVariable3_Object((1,3,6,1,4,1,8886,15,1,3,1,24),_RcNotifsTrapBindVariable3_Type())
rcNotifsTrapBindVariable3.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsTrapBindVariable3.setStatus(_A)
_RcNotifsTrapBindIpAddress_Type=Integer32
_RcNotifsTrapBindIpAddress_Object=MibScalar
rcNotifsTrapBindIpAddress=_RcNotifsTrapBindIpAddress_Object((1,3,6,1,4,1,8886,15,1,3,1,25),_RcNotifsTrapBindIpAddress_Type())
rcNotifsTrapBindIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsTrapBindIpAddress.setStatus(_A)
class _RcNotifsTrapInhibitEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_RcNotifsTrapInhibitEnable_Type.__name__=_D
_RcNotifsTrapInhibitEnable_Object=MibScalar
rcNotifsTrapInhibitEnable=_RcNotifsTrapInhibitEnable_Object((1,3,6,1,4,1,8886,15,1,3,1,30),_RcNotifsTrapInhibitEnable_Type())
rcNotifsTrapInhibitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsTrapInhibitEnable.setStatus(_A)
class _RcNotifsTrapDelayEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_RcNotifsTrapDelayEnable_Type.__name__=_D
_RcNotifsTrapDelayEnable_Object=MibScalar
rcNotifsTrapDelayEnable=_RcNotifsTrapDelayEnable_Object((1,3,6,1,4,1,8886,15,1,3,1,40),_RcNotifsTrapDelayEnable_Type())
rcNotifsTrapDelayEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsTrapDelayEnable.setStatus(_A)
_RcNotifsTrapDelayStartingTime_Type=Integer32
_RcNotifsTrapDelayStartingTime_Object=MibScalar
rcNotifsTrapDelayStartingTime=_RcNotifsTrapDelayStartingTime_Object((1,3,6,1,4,1,8886,15,1,3,1,41),_RcNotifsTrapDelayStartingTime_Type())
rcNotifsTrapDelayStartingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsTrapDelayStartingTime.setStatus(_A)
_RcNotifsTrapDelayEndTime_Type=Integer32
_RcNotifsTrapDelayEndTime_Object=MibScalar
rcNotifsTrapDelayEndTime=_RcNotifsTrapDelayEndTime_Object((1,3,6,1,4,1,8886,15,1,3,1,42),_RcNotifsTrapDelayEndTime_Type())
rcNotifsTrapDelayEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsTrapDelayEndTime.setStatus(_A)
class _RcNotifsTrapAutoSaveEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_RcNotifsTrapAutoSaveEnable_Type.__name__=_D
_RcNotifsTrapAutoSaveEnable_Object=MibScalar
rcNotifsTrapAutoSaveEnable=_RcNotifsTrapAutoSaveEnable_Object((1,3,6,1,4,1,8886,15,1,3,1,45),_RcNotifsTrapAutoSaveEnable_Type())
rcNotifsTrapAutoSaveEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsTrapAutoSaveEnable.setStatus(_A)
_RcNotifsPortAlarmFilterConfig_ObjectIdentity=ObjectIdentity
rcNotifsPortAlarmFilterConfig=_RcNotifsPortAlarmFilterConfig_ObjectIdentity((1,3,6,1,4,1,8886,15,1,3,1,60))
_RcNotifsPortAlarmFilterTableSize_Type=Integer32
_RcNotifsPortAlarmFilterTableSize_Object=MibScalar
rcNotifsPortAlarmFilterTableSize=_RcNotifsPortAlarmFilterTableSize_Object((1,3,6,1,4,1,8886,15,1,3,1,60,10),_RcNotifsPortAlarmFilterTableSize_Type())
rcNotifsPortAlarmFilterTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsPortAlarmFilterTableSize.setStatus(_A)
_RcNotifsPortAlarmFilterTable_Object=MibTable
rcNotifsPortAlarmFilterTable=_RcNotifsPortAlarmFilterTable_Object((1,3,6,1,4,1,8886,15,1,3,1,60,11))
if mibBuilder.loadTexts:rcNotifsPortAlarmFilterTable.setStatus(_A)
_RcNotifsPortAlarmFilterEntry_Object=MibTableRow
rcNotifsPortAlarmFilterEntry=_RcNotifsPortAlarmFilterEntry_Object((1,3,6,1,4,1,8886,15,1,3,1,60,11,1))
rcNotifsPortAlarmFilterEntry.setIndexNames((0,_F,_N),(0,_F,_O))
if mibBuilder.loadTexts:rcNotifsPortAlarmFilterEntry.setStatus(_A)
class _RcNotifsPortAlarmFilterPhysicalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_RcNotifsPortAlarmFilterPhysicalID_Type.__name__=_E
_RcNotifsPortAlarmFilterPhysicalID_Object=MibTableColumn
rcNotifsPortAlarmFilterPhysicalID=_RcNotifsPortAlarmFilterPhysicalID_Object((1,3,6,1,4,1,8886,15,1,3,1,60,11,1,1),_RcNotifsPortAlarmFilterPhysicalID_Type())
rcNotifsPortAlarmFilterPhysicalID.setMaxAccess(_G)
if mibBuilder.loadTexts:rcNotifsPortAlarmFilterPhysicalID.setStatus(_A)
_RcNotifsPortAlarmFilterIfIndex_Type=Integer32
_RcNotifsPortAlarmFilterIfIndex_Object=MibTableColumn
rcNotifsPortAlarmFilterIfIndex=_RcNotifsPortAlarmFilterIfIndex_Object((1,3,6,1,4,1,8886,15,1,3,1,60,11,1,2),_RcNotifsPortAlarmFilterIfIndex_Type())
rcNotifsPortAlarmFilterIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rcNotifsPortAlarmFilterIfIndex.setStatus(_A)
class _RcNotifsPortAlarmFilterTrapEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,512))
_RcNotifsPortAlarmFilterTrapEnable_Type.__name__=_E
_RcNotifsPortAlarmFilterTrapEnable_Object=MibTableColumn
rcNotifsPortAlarmFilterTrapEnable=_RcNotifsPortAlarmFilterTrapEnable_Object((1,3,6,1,4,1,8886,15,1,3,1,60,11,1,10),_RcNotifsPortAlarmFilterTrapEnable_Type())
rcNotifsPortAlarmFilterTrapEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:rcNotifsPortAlarmFilterTrapEnable.setStatus(_A)
class _RcNotifsPortAlarmFilterMonitoringDisable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,512))
_RcNotifsPortAlarmFilterMonitoringDisable_Type.__name__=_E
_RcNotifsPortAlarmFilterMonitoringDisable_Object=MibTableColumn
rcNotifsPortAlarmFilterMonitoringDisable=_RcNotifsPortAlarmFilterMonitoringDisable_Object((1,3,6,1,4,1,8886,15,1,3,1,60,11,1,11),_RcNotifsPortAlarmFilterMonitoringDisable_Type())
rcNotifsPortAlarmFilterMonitoringDisable.setMaxAccess(_G)
if mibBuilder.loadTexts:rcNotifsPortAlarmFilterMonitoringDisable.setStatus(_A)
_RcNotifsPortAlarmFilterRowStatus_Type=RowStatus
_RcNotifsPortAlarmFilterRowStatus_Object=MibTableColumn
rcNotifsPortAlarmFilterRowStatus=_RcNotifsPortAlarmFilterRowStatus_Object((1,3,6,1,4,1,8886,15,1,3,1,60,11,1,30),_RcNotifsPortAlarmFilterRowStatus_Type())
rcNotifsPortAlarmFilterRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rcNotifsPortAlarmFilterRowStatus.setStatus(_A)
_RcNotifsPortAlarmInverseConfig_ObjectIdentity=ObjectIdentity
rcNotifsPortAlarmInverseConfig=_RcNotifsPortAlarmInverseConfig_ObjectIdentity((1,3,6,1,4,1,8886,15,1,3,1,61))
class _RcNotifsAlarmInverseMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('auto',2),(_P,3)))
_RcNotifsAlarmInverseMode_Type.__name__=_D
_RcNotifsAlarmInverseMode_Object=MibScalar
rcNotifsAlarmInverseMode=_RcNotifsAlarmInverseMode_Object((1,3,6,1,4,1,8886,15,1,3,1,61,9),_RcNotifsAlarmInverseMode_Type())
rcNotifsAlarmInverseMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsAlarmInverseMode.setStatus(_A)
_RcNotifsPortAlarmInverseTableSize_Type=Integer32
_RcNotifsPortAlarmInverseTableSize_Object=MibScalar
rcNotifsPortAlarmInverseTableSize=_RcNotifsPortAlarmInverseTableSize_Object((1,3,6,1,4,1,8886,15,1,3,1,61,10),_RcNotifsPortAlarmInverseTableSize_Type())
rcNotifsPortAlarmInverseTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsPortAlarmInverseTableSize.setStatus(_A)
_RcNotifsPortAlarmInverseTable_Object=MibTable
rcNotifsPortAlarmInverseTable=_RcNotifsPortAlarmInverseTable_Object((1,3,6,1,4,1,8886,15,1,3,1,61,11))
if mibBuilder.loadTexts:rcNotifsPortAlarmInverseTable.setStatus(_A)
_RcNotifsPortAlarmInverseEntry_Object=MibTableRow
rcNotifsPortAlarmInverseEntry=_RcNotifsPortAlarmInverseEntry_Object((1,3,6,1,4,1,8886,15,1,3,1,61,11,1))
rcNotifsPortAlarmInverseEntry.setIndexNames((0,_F,_Q),(0,_F,_R))
if mibBuilder.loadTexts:rcNotifsPortAlarmInverseEntry.setStatus(_A)
class _RcNotifsPortAlarmInversePhysicalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_RcNotifsPortAlarmInversePhysicalID_Type.__name__=_E
_RcNotifsPortAlarmInversePhysicalID_Object=MibTableColumn
rcNotifsPortAlarmInversePhysicalID=_RcNotifsPortAlarmInversePhysicalID_Object((1,3,6,1,4,1,8886,15,1,3,1,61,11,1,1),_RcNotifsPortAlarmInversePhysicalID_Type())
rcNotifsPortAlarmInversePhysicalID.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsPortAlarmInversePhysicalID.setStatus(_A)
_RcNotifsPortAlarmInverseIfIndex_Type=Integer32
_RcNotifsPortAlarmInverseIfIndex_Object=MibTableColumn
rcNotifsPortAlarmInverseIfIndex=_RcNotifsPortAlarmInverseIfIndex_Object((1,3,6,1,4,1,8886,15,1,3,1,61,11,1,2),_RcNotifsPortAlarmInverseIfIndex_Type())
rcNotifsPortAlarmInverseIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsPortAlarmInverseIfIndex.setStatus(_A)
class _RcNotifsPortAlarmInverseEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_RcNotifsPortAlarmInverseEnable_Type.__name__=_D
_RcNotifsPortAlarmInverseEnable_Object=MibTableColumn
rcNotifsPortAlarmInverseEnable=_RcNotifsPortAlarmInverseEnable_Object((1,3,6,1,4,1,8886,15,1,3,1,61,11,1,4),_RcNotifsPortAlarmInverseEnable_Type())
rcNotifsPortAlarmInverseEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsPortAlarmInverseEnable.setStatus(_A)
class _RcNotifsAlarmInverseBatchEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_RcNotifsAlarmInverseBatchEnable_Type.__name__=_E
_RcNotifsAlarmInverseBatchEnable_Object=MibScalar
rcNotifsAlarmInverseBatchEnable=_RcNotifsAlarmInverseBatchEnable_Object((1,3,6,1,4,1,8886,15,1,3,1,61,12),_RcNotifsAlarmInverseBatchEnable_Type())
rcNotifsAlarmInverseBatchEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsAlarmInverseBatchEnable.setStatus(_A)
class _RcNotifsTrapRepeatIndex_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RcNotifsTrapRepeatIndex_Type.__name__=_E
_RcNotifsTrapRepeatIndex_Object=MibScalar
rcNotifsTrapRepeatIndex=_RcNotifsTrapRepeatIndex_Object((1,3,6,1,4,1,8886,15,1,3,1,70),_RcNotifsTrapRepeatIndex_Type())
rcNotifsTrapRepeatIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsTrapRepeatIndex.setStatus(_A)
_RcNotifsTrapCurrentIndex_Type=Integer32
_RcNotifsTrapCurrentIndex_Object=MibScalar
rcNotifsTrapCurrentIndex=_RcNotifsTrapCurrentIndex_Object((1,3,6,1,4,1,8886,15,1,3,1,71),_RcNotifsTrapCurrentIndex_Type())
rcNotifsTrapCurrentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcNotifsTrapCurrentIndex.setStatus(_A)
class _RcNotifsTrapRelateEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_RcNotifsTrapRelateEnable_Type.__name__=_D
_RcNotifsTrapRelateEnable_Object=MibScalar
rcNotifsTrapRelateEnable=_RcNotifsTrapRelateEnable_Object((1,3,6,1,4,1,8886,15,1,3,1,72),_RcNotifsTrapRelateEnable_Type())
rcNotifsTrapRelateEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsTrapRelateEnable.setStatus(_A)
_RcNotifsTrapRelateDelayTimes_Type=Integer32
_RcNotifsTrapRelateDelayTimes_Object=MibScalar
rcNotifsTrapRelateDelayTimes=_RcNotifsTrapRelateDelayTimes_Object((1,3,6,1,4,1,8886,15,1,3,1,73),_RcNotifsTrapRelateDelayTimes_Type())
rcNotifsTrapRelateDelayTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:rcNotifsTrapRelateDelayTimes.setStatus(_A)
_RcNotifsObjects_ObjectIdentity=ObjectIdentity
rcNotifsObjects=_RcNotifsObjects_ObjectIdentity((1,3,6,1,4,1,8886,15,1,3,2))
_RcCurNotifsAlarmTableSize_Type=Integer32
_RcCurNotifsAlarmTableSize_Object=MibScalar
rcCurNotifsAlarmTableSize=_RcCurNotifsAlarmTableSize_Object((1,3,6,1,4,1,8886,15,1,3,2,1),_RcCurNotifsAlarmTableSize_Type())
rcCurNotifsAlarmTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCurNotifsAlarmTableSize.setStatus(_A)
_RcCurNotifsAlarmTable_Object=MibTable
rcCurNotifsAlarmTable=_RcCurNotifsAlarmTable_Object((1,3,6,1,4,1,8886,15,1,3,2,2))
if mibBuilder.loadTexts:rcCurNotifsAlarmTable.setStatus(_A)
_RcCurNotifsAlarmEntry_Object=MibTableRow
rcCurNotifsAlarmEntry=_RcCurNotifsAlarmEntry_Object((1,3,6,1,4,1,8886,15,1,3,2,2,1))
rcCurNotifsAlarmEntry.setIndexNames((0,_F,_S))
if mibBuilder.loadTexts:rcCurNotifsAlarmEntry.setStatus(_A)
_RcCurNotifsAlarmIndex_Type=Integer32
_RcCurNotifsAlarmIndex_Object=MibTableColumn
rcCurNotifsAlarmIndex=_RcCurNotifsAlarmIndex_Object((1,3,6,1,4,1,8886,15,1,3,2,2,1,1),_RcCurNotifsAlarmIndex_Type())
rcCurNotifsAlarmIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:rcCurNotifsAlarmIndex.setStatus(_A)
_RcCurNotifsAlarmType_Type=ObjectIdentifier
_RcCurNotifsAlarmType_Object=MibTableColumn
rcCurNotifsAlarmType=_RcCurNotifsAlarmType_Object((1,3,6,1,4,1,8886,15,1,3,2,2,1,2),_RcCurNotifsAlarmType_Type())
rcCurNotifsAlarmType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCurNotifsAlarmType.setStatus(_A)
_RcCurNotifsAlarmBindVarNum_Type=Integer32
_RcCurNotifsAlarmBindVarNum_Object=MibTableColumn
rcCurNotifsAlarmBindVarNum=_RcCurNotifsAlarmBindVarNum_Object((1,3,6,1,4,1,8886,15,1,3,2,2,1,3),_RcCurNotifsAlarmBindVarNum_Type())
rcCurNotifsAlarmBindVarNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCurNotifsAlarmBindVarNum.setStatus(_A)
_RcCurNotifsAlarmBindVar_Type=OctetString
_RcCurNotifsAlarmBindVar_Object=MibTableColumn
rcCurNotifsAlarmBindVar=_RcCurNotifsAlarmBindVar_Object((1,3,6,1,4,1,8886,15,1,3,2,2,1,4),_RcCurNotifsAlarmBindVar_Type())
rcCurNotifsAlarmBindVar.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCurNotifsAlarmBindVar.setStatus(_A)
_RcCurNotifsAlarmDeclareTime_Type=TimeStamp
_RcCurNotifsAlarmDeclareTime_Object=MibTableColumn
rcCurNotifsAlarmDeclareTime=_RcCurNotifsAlarmDeclareTime_Object((1,3,6,1,4,1,8886,15,1,3,2,2,1,5),_RcCurNotifsAlarmDeclareTime_Type())
rcCurNotifsAlarmDeclareTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCurNotifsAlarmDeclareTime.setStatus(_A)
_RcCurNotifsAlarmRelativeTime_Type=Counter64
_RcCurNotifsAlarmRelativeTime_Object=MibTableColumn
rcCurNotifsAlarmRelativeTime=_RcCurNotifsAlarmRelativeTime_Object((1,3,6,1,4,1,8886,15,1,3,2,2,1,6),_RcCurNotifsAlarmRelativeTime_Type())
rcCurNotifsAlarmRelativeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCurNotifsAlarmRelativeTime.setStatus(_A)
_RcHisNotifsAlarmTableSize_Type=Integer32
_RcHisNotifsAlarmTableSize_Object=MibScalar
rcHisNotifsAlarmTableSize=_RcHisNotifsAlarmTableSize_Object((1,3,6,1,4,1,8886,15,1,3,2,3),_RcHisNotifsAlarmTableSize_Type())
rcHisNotifsAlarmTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:rcHisNotifsAlarmTableSize.setStatus(_A)
_RcHisNotifsAlarmTable_Object=MibTable
rcHisNotifsAlarmTable=_RcHisNotifsAlarmTable_Object((1,3,6,1,4,1,8886,15,1,3,2,4))
if mibBuilder.loadTexts:rcHisNotifsAlarmTable.setStatus(_A)
_RcHisNotifsAlarmEntry_Object=MibTableRow
rcHisNotifsAlarmEntry=_RcHisNotifsAlarmEntry_Object((1,3,6,1,4,1,8886,15,1,3,2,4,1))
rcHisNotifsAlarmEntry.setIndexNames((0,_F,_U))
if mibBuilder.loadTexts:rcHisNotifsAlarmEntry.setStatus(_A)
_RcHisNotifsAlarmIndex_Type=Integer32
_RcHisNotifsAlarmIndex_Object=MibTableColumn
rcHisNotifsAlarmIndex=_RcHisNotifsAlarmIndex_Object((1,3,6,1,4,1,8886,15,1,3,2,4,1,1),_RcHisNotifsAlarmIndex_Type())
rcHisNotifsAlarmIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:rcHisNotifsAlarmIndex.setStatus(_A)
_RcHisNotifsAlarmType_Type=ObjectIdentifier
_RcHisNotifsAlarmType_Object=MibTableColumn
rcHisNotifsAlarmType=_RcHisNotifsAlarmType_Object((1,3,6,1,4,1,8886,15,1,3,2,4,1,2),_RcHisNotifsAlarmType_Type())
rcHisNotifsAlarmType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcHisNotifsAlarmType.setStatus(_A)
_RcHisNotifsAlarmBindVarNum_Type=Integer32
_RcHisNotifsAlarmBindVarNum_Object=MibTableColumn
rcHisNotifsAlarmBindVarNum=_RcHisNotifsAlarmBindVarNum_Object((1,3,6,1,4,1,8886,15,1,3,2,4,1,3),_RcHisNotifsAlarmBindVarNum_Type())
rcHisNotifsAlarmBindVarNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rcHisNotifsAlarmBindVarNum.setStatus(_A)
_RcHisNotifsAlarmBindVar_Type=OctetString
_RcHisNotifsAlarmBindVar_Object=MibTableColumn
rcHisNotifsAlarmBindVar=_RcHisNotifsAlarmBindVar_Object((1,3,6,1,4,1,8886,15,1,3,2,4,1,4),_RcHisNotifsAlarmBindVar_Type())
rcHisNotifsAlarmBindVar.setMaxAccess(_B)
if mibBuilder.loadTexts:rcHisNotifsAlarmBindVar.setStatus(_A)
_RcHisNotifsAlarmDeclareTime_Type=TimeStamp
_RcHisNotifsAlarmDeclareTime_Object=MibTableColumn
rcHisNotifsAlarmDeclareTime=_RcHisNotifsAlarmDeclareTime_Object((1,3,6,1,4,1,8886,15,1,3,2,4,1,5),_RcHisNotifsAlarmDeclareTime_Type())
rcHisNotifsAlarmDeclareTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcHisNotifsAlarmDeclareTime.setStatus(_A)
_RcHisNotifsAlarmClearTime_Type=TimeStamp
_RcHisNotifsAlarmClearTime_Object=MibTableColumn
rcHisNotifsAlarmClearTime=_RcHisNotifsAlarmClearTime_Object((1,3,6,1,4,1,8886,15,1,3,2,4,1,6),_RcHisNotifsAlarmClearTime_Type())
rcHisNotifsAlarmClearTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcHisNotifsAlarmClearTime.setStatus(_A)
class _RcHisNotifsAlarmCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),(_P,2)))
_RcHisNotifsAlarmCause_Type.__name__=_D
_RcHisNotifsAlarmCause_Object=MibTableColumn
rcHisNotifsAlarmCause=_RcHisNotifsAlarmCause_Object((1,3,6,1,4,1,8886,15,1,3,2,4,1,7),_RcHisNotifsAlarmCause_Type())
rcHisNotifsAlarmCause.setMaxAccess(_B)
if mibBuilder.loadTexts:rcHisNotifsAlarmCause.setStatus(_A)
class _RcCurNotifsAlarmTableCmd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,1024))
_RcCurNotifsAlarmTableCmd_Type.__name__=_E
_RcCurNotifsAlarmTableCmd_Object=MibScalar
rcCurNotifsAlarmTableCmd=_RcCurNotifsAlarmTableCmd_Object((1,3,6,1,4,1,8886,15,1,3,2,10),_RcCurNotifsAlarmTableCmd_Type())
rcCurNotifsAlarmTableCmd.setMaxAccess(_C)
if mibBuilder.loadTexts:rcCurNotifsAlarmTableCmd.setStatus(_A)
class _RcCurNotifsAlarmTableDeleteByAlarmOID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,1024))
_RcCurNotifsAlarmTableDeleteByAlarmOID_Type.__name__=_E
_RcCurNotifsAlarmTableDeleteByAlarmOID_Object=MibScalar
rcCurNotifsAlarmTableDeleteByAlarmOID=_RcCurNotifsAlarmTableDeleteByAlarmOID_Object((1,3,6,1,4,1,8886,15,1,3,2,11),_RcCurNotifsAlarmTableDeleteByAlarmOID_Type())
rcCurNotifsAlarmTableDeleteByAlarmOID.setMaxAccess(_C)
if mibBuilder.loadTexts:rcCurNotifsAlarmTableDeleteByAlarmOID.setStatus(_A)
class _RcCurNotifsAlarmTableMaxSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2000))
_RcCurNotifsAlarmTableMaxSize_Type.__name__=_D
_RcCurNotifsAlarmTableMaxSize_Object=MibScalar
rcCurNotifsAlarmTableMaxSize=_RcCurNotifsAlarmTableMaxSize_Object((1,3,6,1,4,1,8886,15,1,3,2,20),_RcCurNotifsAlarmTableMaxSize_Type())
rcCurNotifsAlarmTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCurNotifsAlarmTableMaxSize.setStatus(_A)
class _RcCurNotifsAlarmTableStorageMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loop',1),('stop',2)))
_RcCurNotifsAlarmTableStorageMode_Type.__name__=_D
_RcCurNotifsAlarmTableStorageMode_Object=MibScalar
rcCurNotifsAlarmTableStorageMode=_RcCurNotifsAlarmTableStorageMode_Object((1,3,6,1,4,1,8886,15,1,3,2,21),_RcCurNotifsAlarmTableStorageMode_Type())
rcCurNotifsAlarmTableStorageMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rcCurNotifsAlarmTableStorageMode.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'raisecomNotifisMib':raisecomNotifisMib,'rcNotifsConfObjects':rcNotifsConfObjects,'rcNotifsTrapVersion':rcNotifsTrapVersion,'rcNotifsTrapEnable':rcNotifsTrapEnable,'rcNotifsTrapTotalNumber':rcNotifsTrapTotalNumber,'rcNotifsTrapLocation':rcNotifsTrapLocation,'rcNotifsTrapFilterSwitch':rcNotifsTrapFilterSwitch,'rcNotifsAlarmOutputGroup':rcNotifsAlarmOutputGroup,'rcNotifsTrapSinkTable':rcNotifsTrapSinkTable,'rcNotifsTrapSinkEntry':rcNotifsTrapSinkEntry,_K:rcNotifsTrapIndex,'rcNotifsTrapTarget':rcNotifsTrapTarget,'rcNotifsTrapPort':rcNotifsTrapPort,'rcNotifsAlarmFilterTable':rcNotifsAlarmFilterTable,'rcNotifsAlarmFilterEntry':rcNotifsAlarmFilterEntry,_L:rcNotifsFilterAlarmTrapOID,'rcNotifsAlarmTrapEnable':rcNotifsAlarmTrapEnable,'rcNotifsAlarmTrapLogEnable':rcNotifsAlarmTrapLogEnable,'rcNotifsAlarmFilterControl':rcNotifsAlarmFilterControl,'rcNotifsAlarmOutputEnable':rcNotifsAlarmOutputEnable,'rcNotifsAlarmMonitoringDisable':rcNotifsAlarmMonitoringDisable,'rcNotifsPortFilterConfig':rcNotifsPortFilterConfig,'rcNotifsPortFilterIndexNext':rcNotifsPortFilterIndexNext,'rcNotifsPortFilterTable':rcNotifsPortFilterTable,'rcNotifsPortFilterEntry':rcNotifsPortFilterEntry,_M:rcNotifsPortFilterIndex,'rcNotifsPortIfIndex':rcNotifsPortIfIndex,'rcNotifsPortFilterRowStatus':rcNotifsPortFilterRowStatus,'rcNotifsTrapPhysicalID':rcNotifsTrapPhysicalID,'rcNotifsTrapIfIndex':rcNotifsTrapIfIndex,'rcNotifsTrapBindVariable1':rcNotifsTrapBindVariable1,'rcNotifsTrapBindVariable2':rcNotifsTrapBindVariable2,'rcNotifsTrapBindVariable3':rcNotifsTrapBindVariable3,'rcNotifsTrapBindIpAddress':rcNotifsTrapBindIpAddress,'rcNotifsTrapInhibitEnable':rcNotifsTrapInhibitEnable,'rcNotifsTrapDelayEnable':rcNotifsTrapDelayEnable,'rcNotifsTrapDelayStartingTime':rcNotifsTrapDelayStartingTime,'rcNotifsTrapDelayEndTime':rcNotifsTrapDelayEndTime,'rcNotifsTrapAutoSaveEnable':rcNotifsTrapAutoSaveEnable,'rcNotifsPortAlarmFilterConfig':rcNotifsPortAlarmFilterConfig,'rcNotifsPortAlarmFilterTableSize':rcNotifsPortAlarmFilterTableSize,'rcNotifsPortAlarmFilterTable':rcNotifsPortAlarmFilterTable,'rcNotifsPortAlarmFilterEntry':rcNotifsPortAlarmFilterEntry,_N:rcNotifsPortAlarmFilterPhysicalID,_O:rcNotifsPortAlarmFilterIfIndex,'rcNotifsPortAlarmFilterTrapEnable':rcNotifsPortAlarmFilterTrapEnable,'rcNotifsPortAlarmFilterMonitoringDisable':rcNotifsPortAlarmFilterMonitoringDisable,'rcNotifsPortAlarmFilterRowStatus':rcNotifsPortAlarmFilterRowStatus,'rcNotifsPortAlarmInverseConfig':rcNotifsPortAlarmInverseConfig,'rcNotifsAlarmInverseMode':rcNotifsAlarmInverseMode,'rcNotifsPortAlarmInverseTableSize':rcNotifsPortAlarmInverseTableSize,'rcNotifsPortAlarmInverseTable':rcNotifsPortAlarmInverseTable,'rcNotifsPortAlarmInverseEntry':rcNotifsPortAlarmInverseEntry,_Q:rcNotifsPortAlarmInversePhysicalID,_R:rcNotifsPortAlarmInverseIfIndex,'rcNotifsPortAlarmInverseEnable':rcNotifsPortAlarmInverseEnable,'rcNotifsAlarmInverseBatchEnable':rcNotifsAlarmInverseBatchEnable,'rcNotifsTrapRepeatIndex':rcNotifsTrapRepeatIndex,'rcNotifsTrapCurrentIndex':rcNotifsTrapCurrentIndex,'rcNotifsTrapRelateEnable':rcNotifsTrapRelateEnable,'rcNotifsTrapRelateDelayTimes':rcNotifsTrapRelateDelayTimes,'rcNotifsObjects':rcNotifsObjects,'rcCurNotifsAlarmTableSize':rcCurNotifsAlarmTableSize,'rcCurNotifsAlarmTable':rcCurNotifsAlarmTable,'rcCurNotifsAlarmEntry':rcCurNotifsAlarmEntry,_S:rcCurNotifsAlarmIndex,'rcCurNotifsAlarmType':rcCurNotifsAlarmType,'rcCurNotifsAlarmBindVarNum':rcCurNotifsAlarmBindVarNum,'rcCurNotifsAlarmBindVar':rcCurNotifsAlarmBindVar,'rcCurNotifsAlarmDeclareTime':rcCurNotifsAlarmDeclareTime,'rcCurNotifsAlarmRelativeTime':rcCurNotifsAlarmRelativeTime,'rcHisNotifsAlarmTableSize':rcHisNotifsAlarmTableSize,'rcHisNotifsAlarmTable':rcHisNotifsAlarmTable,'rcHisNotifsAlarmEntry':rcHisNotifsAlarmEntry,_U:rcHisNotifsAlarmIndex,'rcHisNotifsAlarmType':rcHisNotifsAlarmType,'rcHisNotifsAlarmBindVarNum':rcHisNotifsAlarmBindVarNum,'rcHisNotifsAlarmBindVar':rcHisNotifsAlarmBindVar,'rcHisNotifsAlarmDeclareTime':rcHisNotifsAlarmDeclareTime,'rcHisNotifsAlarmClearTime':rcHisNotifsAlarmClearTime,'rcHisNotifsAlarmCause':rcHisNotifsAlarmCause,'rcCurNotifsAlarmTableCmd':rcCurNotifsAlarmTableCmd,'rcCurNotifsAlarmTableDeleteByAlarmOID':rcCurNotifsAlarmTableDeleteByAlarmOID,'rcCurNotifsAlarmTableMaxSize':rcCurNotifsAlarmTableMaxSize,'rcCurNotifsAlarmTableStorageMode':rcCurNotifsAlarmTableStorageMode})