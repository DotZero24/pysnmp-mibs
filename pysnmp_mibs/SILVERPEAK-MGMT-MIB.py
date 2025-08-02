_X='silverpeakMgmtNotifyGroup'
_W='silverpeakMgmtGroup'
_V='spsNotifyAlarm'
_U='spsActiveAlarmServiceAffect'
_T='spsActiveAlarmLogTime'
_S='spsActiveAlarmClearable'
_R='spsActiveAlarmActive'
_Q='spsActiveAlarmAcked'
_P='spsActiveAlarmType'
_O='spsActiveAlarmName'
_N='spsActiveAlarmSeqNum'
_M='spsOperStatus'
_L='spsProductModel'
_K='spsSystemVersion'
_J='spsActiveAlarmIndex'
_I='OctetString'
_H='spsActiveAlarmSource'
_G='spsActiveAlarmDescr'
_F='spsActiveAlarmSeverity'
_E='Integer32'
_D='DisplayString'
_C='read-only'
_B='SILVERPEAK-MGMT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
silverpeakMgmt,silverpeakNotifications=mibBuilder.importSymbols('SILVERPEAK-SMI','silverpeakMgmt','silverpeakNotifications')
SilverpeakAlarmSeverity,SilverpeakSeqNum,SilverpeakYesNo=mibBuilder.importSymbols('SILVERPEAK-TC','SilverpeakAlarmSeverity','SilverpeakSeqNum','SilverpeakYesNo')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
silverpeakMgmtMIB=ModuleIdentity((1,3,6,1,4,1,23867,3,1))
_SilverpeakMgmtMIBObjects_ObjectIdentity=ObjectIdentity
silverpeakMgmtMIBObjects=_SilverpeakMgmtMIBObjects_ObjectIdentity((1,3,6,1,4,1,23867,3,1,1))
_SilverpeakMgmtMIBScalars_ObjectIdentity=ObjectIdentity
silverpeakMgmtMIBScalars=_SilverpeakMgmtMIBScalars_ObjectIdentity((1,3,6,1,4,1,23867,3,1,1,1))
_SpsSystemVersion_Type=DisplayString
_SpsSystemVersion_Object=MibScalar
spsSystemVersion=_SpsSystemVersion_Object((1,3,6,1,4,1,23867,3,1,1,1,1),_SpsSystemVersion_Type())
spsSystemVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:spsSystemVersion.setStatus(_A)
_SpsProductModel_Type=DisplayString
_SpsProductModel_Object=MibScalar
spsProductModel=_SpsProductModel_Object((1,3,6,1,4,1,23867,3,1,1,1,2),_SpsProductModel_Type())
spsProductModel.setMaxAccess(_C)
if mibBuilder.loadTexts:spsProductModel.setStatus(_A)
_SpsOperStatus_Type=DisplayString
_SpsOperStatus_Object=MibScalar
spsOperStatus=_SpsOperStatus_Object((1,3,6,1,4,1,23867,3,1,1,1,3),_SpsOperStatus_Type())
spsOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:spsOperStatus.setStatus(_A)
class _SpsActiveAlarmCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SpsActiveAlarmCount_Type.__name__=_E
_SpsActiveAlarmCount_Object=MibScalar
spsActiveAlarmCount=_SpsActiveAlarmCount_Object((1,3,6,1,4,1,23867,3,1,1,1,4),_SpsActiveAlarmCount_Type())
spsActiveAlarmCount.setMaxAccess(_C)
if mibBuilder.loadTexts:spsActiveAlarmCount.setStatus(_A)
_SpsSystemUptime_Type=TimeTicks
_SpsSystemUptime_Object=MibScalar
spsSystemUptime=_SpsSystemUptime_Object((1,3,6,1,4,1,23867,3,1,1,1,5),_SpsSystemUptime_Type())
spsSystemUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:spsSystemUptime.setStatus(_A)
_SpsSystemSerial_Type=DisplayString
_SpsSystemSerial_Object=MibScalar
spsSystemSerial=_SpsSystemSerial_Object((1,3,6,1,4,1,23867,3,1,1,1,6),_SpsSystemSerial_Type())
spsSystemSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:spsSystemSerial.setStatus(_A)
_SilverpeakMgmtMIBTables_ObjectIdentity=ObjectIdentity
silverpeakMgmtMIBTables=_SilverpeakMgmtMIBTables_ObjectIdentity((1,3,6,1,4,1,23867,3,1,1,2))
_SpsActiveAlarmTable_Object=MibTable
spsActiveAlarmTable=_SpsActiveAlarmTable_Object((1,3,6,1,4,1,23867,3,1,1,2,1))
if mibBuilder.loadTexts:spsActiveAlarmTable.setStatus(_A)
_ActiveAlarmEntry_Object=MibTableRow
activeAlarmEntry=_ActiveAlarmEntry_Object((1,3,6,1,4,1,23867,3,1,1,2,1,1))
activeAlarmEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:activeAlarmEntry.setStatus(_A)
class _SpsActiveAlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SpsActiveAlarmIndex_Type.__name__=_E
_SpsActiveAlarmIndex_Object=MibTableColumn
spsActiveAlarmIndex=_SpsActiveAlarmIndex_Object((1,3,6,1,4,1,23867,3,1,1,2,1,1,1),_SpsActiveAlarmIndex_Type())
spsActiveAlarmIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:spsActiveAlarmIndex.setStatus(_A)
_SpsActiveAlarmSeqNum_Type=SilverpeakSeqNum
_SpsActiveAlarmSeqNum_Object=MibTableColumn
spsActiveAlarmSeqNum=_SpsActiveAlarmSeqNum_Object((1,3,6,1,4,1,23867,3,1,1,2,1,1,2),_SpsActiveAlarmSeqNum_Type())
spsActiveAlarmSeqNum.setMaxAccess(_C)
if mibBuilder.loadTexts:spsActiveAlarmSeqNum.setStatus(_A)
_SpsActiveAlarmSeverity_Type=SilverpeakAlarmSeverity
_SpsActiveAlarmSeverity_Object=MibTableColumn
spsActiveAlarmSeverity=_SpsActiveAlarmSeverity_Object((1,3,6,1,4,1,23867,3,1,1,2,1,1,3),_SpsActiveAlarmSeverity_Type())
spsActiveAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:spsActiveAlarmSeverity.setStatus(_A)
class _SpsActiveAlarmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SpsActiveAlarmName_Type.__name__=_D
_SpsActiveAlarmName_Object=MibTableColumn
spsActiveAlarmName=_SpsActiveAlarmName_Object((1,3,6,1,4,1,23867,3,1,1,2,1,1,4),_SpsActiveAlarmName_Type())
spsActiveAlarmName.setMaxAccess(_C)
if mibBuilder.loadTexts:spsActiveAlarmName.setStatus(_A)
class _SpsActiveAlarmDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SpsActiveAlarmDescr_Type.__name__=_D
_SpsActiveAlarmDescr_Object=MibTableColumn
spsActiveAlarmDescr=_SpsActiveAlarmDescr_Object((1,3,6,1,4,1,23867,3,1,1,2,1,1,5),_SpsActiveAlarmDescr_Type())
spsActiveAlarmDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:spsActiveAlarmDescr.setStatus(_A)
class _SpsActiveAlarmSource_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SpsActiveAlarmSource_Type.__name__=_D
_SpsActiveAlarmSource_Object=MibTableColumn
spsActiveAlarmSource=_SpsActiveAlarmSource_Object((1,3,6,1,4,1,23867,3,1,1,2,1,1,6),_SpsActiveAlarmSource_Type())
spsActiveAlarmSource.setMaxAccess(_C)
if mibBuilder.loadTexts:spsActiveAlarmSource.setStatus(_A)
class _SpsActiveAlarmType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SpsActiveAlarmType_Type.__name__=_D
_SpsActiveAlarmType_Object=MibTableColumn
spsActiveAlarmType=_SpsActiveAlarmType_Object((1,3,6,1,4,1,23867,3,1,1,2,1,1,7),_SpsActiveAlarmType_Type())
spsActiveAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:spsActiveAlarmType.setStatus(_A)
_SpsActiveAlarmAcked_Type=SilverpeakYesNo
_SpsActiveAlarmAcked_Object=MibTableColumn
spsActiveAlarmAcked=_SpsActiveAlarmAcked_Object((1,3,6,1,4,1,23867,3,1,1,2,1,1,8),_SpsActiveAlarmAcked_Type())
spsActiveAlarmAcked.setMaxAccess(_C)
if mibBuilder.loadTexts:spsActiveAlarmAcked.setStatus(_A)
_SpsActiveAlarmActive_Type=SilverpeakYesNo
_SpsActiveAlarmActive_Object=MibTableColumn
spsActiveAlarmActive=_SpsActiveAlarmActive_Object((1,3,6,1,4,1,23867,3,1,1,2,1,1,9),_SpsActiveAlarmActive_Type())
spsActiveAlarmActive.setMaxAccess(_C)
if mibBuilder.loadTexts:spsActiveAlarmActive.setStatus(_A)
_SpsActiveAlarmClearable_Type=SilverpeakYesNo
_SpsActiveAlarmClearable_Object=MibTableColumn
spsActiveAlarmClearable=_SpsActiveAlarmClearable_Object((1,3,6,1,4,1,23867,3,1,1,2,1,1,10),_SpsActiveAlarmClearable_Type())
spsActiveAlarmClearable.setMaxAccess(_C)
if mibBuilder.loadTexts:spsActiveAlarmClearable.setStatus(_A)
class _SpsActiveAlarmLogTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SpsActiveAlarmLogTime_Type.__name__=_I
_SpsActiveAlarmLogTime_Object=MibTableColumn
spsActiveAlarmLogTime=_SpsActiveAlarmLogTime_Object((1,3,6,1,4,1,23867,3,1,1,2,1,1,11),_SpsActiveAlarmLogTime_Type())
spsActiveAlarmLogTime.setMaxAccess(_C)
if mibBuilder.loadTexts:spsActiveAlarmLogTime.setStatus(_A)
_SpsActiveAlarmServiceAffect_Type=SilverpeakYesNo
_SpsActiveAlarmServiceAffect_Object=MibTableColumn
spsActiveAlarmServiceAffect=_SpsActiveAlarmServiceAffect_Object((1,3,6,1,4,1,23867,3,1,1,2,1,1,12),_SpsActiveAlarmServiceAffect_Type())
spsActiveAlarmServiceAffect.setMaxAccess(_C)
if mibBuilder.loadTexts:spsActiveAlarmServiceAffect.setStatus(_A)
_SpsActiveAlarmTypeId_Type=Integer32
_SpsActiveAlarmTypeId_Object=MibTableColumn
spsActiveAlarmTypeId=_SpsActiveAlarmTypeId_Object((1,3,6,1,4,1,23867,3,1,1,2,1,1,13),_SpsActiveAlarmTypeId_Type())
spsActiveAlarmTypeId.setMaxAccess(_C)
if mibBuilder.loadTexts:spsActiveAlarmTypeId.setStatus(_A)
_SilverpeakMgmtMIBConformance_ObjectIdentity=ObjectIdentity
silverpeakMgmtMIBConformance=_SilverpeakMgmtMIBConformance_ObjectIdentity((1,3,6,1,4,1,23867,3,1,2))
_SilverpeakMgmtMIBCompliances_ObjectIdentity=ObjectIdentity
silverpeakMgmtMIBCompliances=_SilverpeakMgmtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,23867,3,1,2,1))
_SilverpeakMgmtMIBGroups_ObjectIdentity=ObjectIdentity
silverpeakMgmtMIBGroups=_SilverpeakMgmtMIBGroups_ObjectIdentity((1,3,6,1,4,1,23867,3,1,2,2))
_SilverpeakMgmtMIBNotifications_ObjectIdentity=ObjectIdentity
silverpeakMgmtMIBNotifications=_SilverpeakMgmtMIBNotifications_ObjectIdentity((1,3,6,1,4,1,23867,4,1))
silverpeakMgmtGroup=ObjectGroup((1,3,6,1,4,1,23867,3,1,2,2,1))
silverpeakMgmtGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_F),(_B,_O),(_B,_G),(_B,_H),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:silverpeakMgmtGroup.setStatus(_A)
spsNotifyAlarm=NotificationType((1,3,6,1,4,1,23867,4,1,1))
spsNotifyAlarm.setObjects(*((_B,_H),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:spsNotifyAlarm.setStatus(_A)
silverpeakMgmtNotifyGroup=NotificationGroup((1,3,6,1,4,1,23867,3,1,2,2,3))
silverpeakMgmtNotifyGroup.setObjects((_B,_V))
if mibBuilder.loadTexts:silverpeakMgmtNotifyGroup.setStatus(_A)
silverpeakMgmtCompliance=ModuleCompliance((1,3,6,1,4,1,23867,3,1,2,1,1))
silverpeakMgmtCompliance.setObjects(*((_B,_W),(_B,_X)))
if mibBuilder.loadTexts:silverpeakMgmtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'silverpeakMgmtMIB':silverpeakMgmtMIB,'silverpeakMgmtMIBObjects':silverpeakMgmtMIBObjects,'silverpeakMgmtMIBScalars':silverpeakMgmtMIBScalars,_K:spsSystemVersion,_L:spsProductModel,_M:spsOperStatus,'spsActiveAlarmCount':spsActiveAlarmCount,'spsSystemUptime':spsSystemUptime,'spsSystemSerial':spsSystemSerial,'silverpeakMgmtMIBTables':silverpeakMgmtMIBTables,'spsActiveAlarmTable':spsActiveAlarmTable,'activeAlarmEntry':activeAlarmEntry,_J:spsActiveAlarmIndex,_N:spsActiveAlarmSeqNum,_F:spsActiveAlarmSeverity,_O:spsActiveAlarmName,_G:spsActiveAlarmDescr,_H:spsActiveAlarmSource,_P:spsActiveAlarmType,_Q:spsActiveAlarmAcked,_R:spsActiveAlarmActive,_S:spsActiveAlarmClearable,_T:spsActiveAlarmLogTime,_U:spsActiveAlarmServiceAffect,'spsActiveAlarmTypeId':spsActiveAlarmTypeId,'silverpeakMgmtMIBConformance':silverpeakMgmtMIBConformance,'silverpeakMgmtMIBCompliances':silverpeakMgmtMIBCompliances,'silverpeakMgmtCompliance':silverpeakMgmtCompliance,'silverpeakMgmtMIBGroups':silverpeakMgmtMIBGroups,_W:silverpeakMgmtGroup,_X:silverpeakMgmtNotifyGroup,'silverpeakMgmtMIBNotifications':silverpeakMgmtMIBNotifications,_V:spsNotifyAlarm})