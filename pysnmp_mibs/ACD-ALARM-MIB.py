_m='acdAlarmTidGroup'
_l='acdAlarmNotificationsGroup'
_k='acdAlarmStatusGroup'
_j='acdAlarmCfgGroup'
_i='acdAlarmGenGroup'
_h='acdAlarmClearState'
_g='acdAlarmActiveState'
_f='acdAlarmStatusTableLastChangeTid'
_e='acdAlarmCfgTableLastChangeTid'
_d='acdAlarmStatusMsg'
_c='acdAlarmStatusOn'
_b='acdAlarmStatusNumber'
_a='acdAlarmCfgEnable'
_Z='acdAlarmGen8023AHEnable'
_Y='acdAlarmGenSNMPEnable'
_X='acdAlarmGenSyslogEnable'
_W='acdAlarmGenLedEnable'
_V='acdAlarmGenThreshOff'
_U='acdAlarmGenThreshOn'
_T='milliseconds'
_S='Integer32'
_R='acdAlarmStatusID'
_Q='Unsigned32'
_P='sysName'
_O='SNMPv2-MIB'
_N='acdAlarmStatusLastChange'
_M='acdAlarmCfgAMOType'
_L='acdAlarmCfgConditionType'
_K='acdAlarmCfgExtNumber'
_J='acdAlarmCfgServiceAffecting'
_I='acdAlarmCfgSeverity'
_H='acdAlarmCfgDesc'
_G='acdAlarmCfgNumber'
_F='acdAlarmCfgID'
_E='DisplayString'
_D='read-write'
_C='read-only'
_B='current'
_A='ACD-ALARM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acdMibs,=mibBuilder.importSymbols('ACCEDIAN-SMI','acdMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_O,_P)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_S,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Q,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'PhysAddress','TextualConvention','TruthValue')
acdAlarm=ModuleIdentity((1,3,6,1,4,1,22420,2,1))
if mibBuilder.loadTexts:acdAlarm.setRevisions(('2011-10-10 01:00','2010-11-10 01:00','2009-02-04 01:00','2008-02-01 01:00','2007-05-22 01:00','2006-12-19 01:00','2006-08-06 01:00'))
class _AcdAlarmGenThreshOn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,50000))
_AcdAlarmGenThreshOn_Type.__name__=_Q
_AcdAlarmGenThreshOn_Object=MibScalar
acdAlarmGenThreshOn=_AcdAlarmGenThreshOn_Object((1,3,6,1,4,1,22420,2,1,1),_AcdAlarmGenThreshOn_Type())
acdAlarmGenThreshOn.setMaxAccess(_D)
if mibBuilder.loadTexts:acdAlarmGenThreshOn.setStatus(_B)
if mibBuilder.loadTexts:acdAlarmGenThreshOn.setUnits(_T)
class _AcdAlarmGenThreshOff_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,50000))
_AcdAlarmGenThreshOff_Type.__name__=_Q
_AcdAlarmGenThreshOff_Object=MibScalar
acdAlarmGenThreshOff=_AcdAlarmGenThreshOff_Object((1,3,6,1,4,1,22420,2,1,2),_AcdAlarmGenThreshOff_Type())
acdAlarmGenThreshOff.setMaxAccess(_D)
if mibBuilder.loadTexts:acdAlarmGenThreshOff.setStatus(_B)
if mibBuilder.loadTexts:acdAlarmGenThreshOff.setUnits(_T)
_AcdAlarmGenLedEnable_Type=TruthValue
_AcdAlarmGenLedEnable_Object=MibScalar
acdAlarmGenLedEnable=_AcdAlarmGenLedEnable_Object((1,3,6,1,4,1,22420,2,1,3),_AcdAlarmGenLedEnable_Type())
acdAlarmGenLedEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:acdAlarmGenLedEnable.setStatus(_B)
_AcdAlarmGenSyslogEnable_Type=TruthValue
_AcdAlarmGenSyslogEnable_Object=MibScalar
acdAlarmGenSyslogEnable=_AcdAlarmGenSyslogEnable_Object((1,3,6,1,4,1,22420,2,1,4),_AcdAlarmGenSyslogEnable_Type())
acdAlarmGenSyslogEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:acdAlarmGenSyslogEnable.setStatus(_B)
_AcdAlarmGenSNMPEnable_Type=TruthValue
_AcdAlarmGenSNMPEnable_Object=MibScalar
acdAlarmGenSNMPEnable=_AcdAlarmGenSNMPEnable_Object((1,3,6,1,4,1,22420,2,1,5),_AcdAlarmGenSNMPEnable_Type())
acdAlarmGenSNMPEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:acdAlarmGenSNMPEnable.setStatus(_B)
_AcdAlarmGen8023AHEnable_Type=TruthValue
_AcdAlarmGen8023AHEnable_Object=MibScalar
acdAlarmGen8023AHEnable=_AcdAlarmGen8023AHEnable_Object((1,3,6,1,4,1,22420,2,1,6),_AcdAlarmGen8023AHEnable_Type())
acdAlarmGen8023AHEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:acdAlarmGen8023AHEnable.setStatus(_B)
_AcdAlarmCfgTable_Object=MibTable
acdAlarmCfgTable=_AcdAlarmCfgTable_Object((1,3,6,1,4,1,22420,2,1,10))
if mibBuilder.loadTexts:acdAlarmCfgTable.setStatus(_B)
_AcdAlarmCfgEntry_Object=MibTableRow
acdAlarmCfgEntry=_AcdAlarmCfgEntry_Object((1,3,6,1,4,1,22420,2,1,10,1))
acdAlarmCfgEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:acdAlarmCfgEntry.setStatus(_B)
_AcdAlarmCfgID_Type=Unsigned32
_AcdAlarmCfgID_Object=MibTableColumn
acdAlarmCfgID=_AcdAlarmCfgID_Object((1,3,6,1,4,1,22420,2,1,10,1,1),_AcdAlarmCfgID_Type())
acdAlarmCfgID.setMaxAccess(_C)
if mibBuilder.loadTexts:acdAlarmCfgID.setStatus(_B)
_AcdAlarmCfgNumber_Type=Unsigned32
_AcdAlarmCfgNumber_Object=MibTableColumn
acdAlarmCfgNumber=_AcdAlarmCfgNumber_Object((1,3,6,1,4,1,22420,2,1,10,1,2),_AcdAlarmCfgNumber_Type())
acdAlarmCfgNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:acdAlarmCfgNumber.setStatus(_B)
class _AcdAlarmCfgDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AcdAlarmCfgDesc_Type.__name__=_E
_AcdAlarmCfgDesc_Object=MibTableColumn
acdAlarmCfgDesc=_AcdAlarmCfgDesc_Object((1,3,6,1,4,1,22420,2,1,10,1,3),_AcdAlarmCfgDesc_Type())
acdAlarmCfgDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:acdAlarmCfgDesc.setStatus(_B)
_AcdAlarmCfgEnable_Type=TruthValue
_AcdAlarmCfgEnable_Object=MibTableColumn
acdAlarmCfgEnable=_AcdAlarmCfgEnable_Object((1,3,6,1,4,1,22420,2,1,10,1,4),_AcdAlarmCfgEnable_Type())
acdAlarmCfgEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:acdAlarmCfgEnable.setStatus(_B)
class _AcdAlarmCfgSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('info',0),('minor',1),('major',2),('critical',3)))
_AcdAlarmCfgSeverity_Type.__name__=_S
_AcdAlarmCfgSeverity_Object=MibTableColumn
acdAlarmCfgSeverity=_AcdAlarmCfgSeverity_Object((1,3,6,1,4,1,22420,2,1,10,1,5),_AcdAlarmCfgSeverity_Type())
acdAlarmCfgSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:acdAlarmCfgSeverity.setStatus(_B)
_AcdAlarmCfgServiceAffecting_Type=TruthValue
_AcdAlarmCfgServiceAffecting_Object=MibTableColumn
acdAlarmCfgServiceAffecting=_AcdAlarmCfgServiceAffecting_Object((1,3,6,1,4,1,22420,2,1,10,1,6),_AcdAlarmCfgServiceAffecting_Type())
acdAlarmCfgServiceAffecting.setMaxAccess(_D)
if mibBuilder.loadTexts:acdAlarmCfgServiceAffecting.setStatus(_B)
class _AcdAlarmCfgExtNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AcdAlarmCfgExtNumber_Type.__name__=_E
_AcdAlarmCfgExtNumber_Object=MibTableColumn
acdAlarmCfgExtNumber=_AcdAlarmCfgExtNumber_Object((1,3,6,1,4,1,22420,2,1,10,1,7),_AcdAlarmCfgExtNumber_Type())
acdAlarmCfgExtNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:acdAlarmCfgExtNumber.setStatus(_B)
class _AcdAlarmCfgConditionType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AcdAlarmCfgConditionType_Type.__name__=_E
_AcdAlarmCfgConditionType_Object=MibTableColumn
acdAlarmCfgConditionType=_AcdAlarmCfgConditionType_Object((1,3,6,1,4,1,22420,2,1,10,1,8),_AcdAlarmCfgConditionType_Type())
acdAlarmCfgConditionType.setMaxAccess(_C)
if mibBuilder.loadTexts:acdAlarmCfgConditionType.setStatus(_B)
class _AcdAlarmCfgAMOType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AcdAlarmCfgAMOType_Type.__name__=_E
_AcdAlarmCfgAMOType_Object=MibTableColumn
acdAlarmCfgAMOType=_AcdAlarmCfgAMOType_Object((1,3,6,1,4,1,22420,2,1,10,1,9),_AcdAlarmCfgAMOType_Type())
acdAlarmCfgAMOType.setMaxAccess(_C)
if mibBuilder.loadTexts:acdAlarmCfgAMOType.setStatus(_B)
_AcdAlarmStatusTable_Object=MibTable
acdAlarmStatusTable=_AcdAlarmStatusTable_Object((1,3,6,1,4,1,22420,2,1,11))
if mibBuilder.loadTexts:acdAlarmStatusTable.setStatus(_B)
_AcdAlarmStatusEntry_Object=MibTableRow
acdAlarmStatusEntry=_AcdAlarmStatusEntry_Object((1,3,6,1,4,1,22420,2,1,11,1))
acdAlarmStatusEntry.setIndexNames((0,_A,_R))
if mibBuilder.loadTexts:acdAlarmStatusEntry.setStatus(_B)
_AcdAlarmStatusID_Type=Unsigned32
_AcdAlarmStatusID_Object=MibTableColumn
acdAlarmStatusID=_AcdAlarmStatusID_Object((1,3,6,1,4,1,22420,2,1,11,1,1),_AcdAlarmStatusID_Type())
acdAlarmStatusID.setMaxAccess(_C)
if mibBuilder.loadTexts:acdAlarmStatusID.setStatus(_B)
_AcdAlarmStatusNumber_Type=Unsigned32
_AcdAlarmStatusNumber_Object=MibTableColumn
acdAlarmStatusNumber=_AcdAlarmStatusNumber_Object((1,3,6,1,4,1,22420,2,1,11,1,2),_AcdAlarmStatusNumber_Type())
acdAlarmStatusNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:acdAlarmStatusNumber.setStatus(_B)
_AcdAlarmStatusOn_Type=TruthValue
_AcdAlarmStatusOn_Object=MibTableColumn
acdAlarmStatusOn=_AcdAlarmStatusOn_Object((1,3,6,1,4,1,22420,2,1,11,1,3),_AcdAlarmStatusOn_Type())
acdAlarmStatusOn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdAlarmStatusOn.setStatus(_B)
_AcdAlarmStatusLastChange_Type=DateAndTime
_AcdAlarmStatusLastChange_Object=MibTableColumn
acdAlarmStatusLastChange=_AcdAlarmStatusLastChange_Object((1,3,6,1,4,1,22420,2,1,11,1,4),_AcdAlarmStatusLastChange_Type())
acdAlarmStatusLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:acdAlarmStatusLastChange.setStatus(_B)
class _AcdAlarmStatusMsg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AcdAlarmStatusMsg_Type.__name__=_E
_AcdAlarmStatusMsg_Object=MibTableColumn
acdAlarmStatusMsg=_AcdAlarmStatusMsg_Object((1,3,6,1,4,1,22420,2,1,11,1,5),_AcdAlarmStatusMsg_Type())
acdAlarmStatusMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:acdAlarmStatusMsg.setStatus(_B)
_AcdAlarmV2_ObjectIdentity=ObjectIdentity
acdAlarmV2=_AcdAlarmV2_ObjectIdentity((1,3,6,1,4,1,22420,2,1,12))
_AcdAlarmMIBObjects_ObjectIdentity=ObjectIdentity
acdAlarmMIBObjects=_AcdAlarmMIBObjects_ObjectIdentity((1,3,6,1,4,1,22420,2,1,15))
_AcdAlarmConfig_ObjectIdentity=ObjectIdentity
acdAlarmConfig=_AcdAlarmConfig_ObjectIdentity((1,3,6,1,4,1,22420,2,1,15,1))
_AcdAlarmStatus_ObjectIdentity=ObjectIdentity
acdAlarmStatus=_AcdAlarmStatus_ObjectIdentity((1,3,6,1,4,1,22420,2,1,15,2))
_AcdAlarmConformance_ObjectIdentity=ObjectIdentity
acdAlarmConformance=_AcdAlarmConformance_ObjectIdentity((1,3,6,1,4,1,22420,2,1,15,3))
_AcdAlarmCompliances_ObjectIdentity=ObjectIdentity
acdAlarmCompliances=_AcdAlarmCompliances_ObjectIdentity((1,3,6,1,4,1,22420,2,1,15,3,1))
_AcdAlarmGroups_ObjectIdentity=ObjectIdentity
acdAlarmGroups=_AcdAlarmGroups_ObjectIdentity((1,3,6,1,4,1,22420,2,1,15,3,2))
_AcdAlarmTableTid_ObjectIdentity=ObjectIdentity
acdAlarmTableTid=_AcdAlarmTableTid_ObjectIdentity((1,3,6,1,4,1,22420,2,1,15,4))
_AcdAlarmCfgTableLastChangeTid_Type=Unsigned32
_AcdAlarmCfgTableLastChangeTid_Object=MibScalar
acdAlarmCfgTableLastChangeTid=_AcdAlarmCfgTableLastChangeTid_Object((1,3,6,1,4,1,22420,2,1,15,4,1),_AcdAlarmCfgTableLastChangeTid_Type())
acdAlarmCfgTableLastChangeTid.setMaxAccess(_C)
if mibBuilder.loadTexts:acdAlarmCfgTableLastChangeTid.setStatus(_B)
_AcdAlarmStatusTableLastChangeTid_Type=Unsigned32
_AcdAlarmStatusTableLastChangeTid_Object=MibScalar
acdAlarmStatusTableLastChangeTid=_AcdAlarmStatusTableLastChangeTid_Object((1,3,6,1,4,1,22420,2,1,15,4,2),_AcdAlarmStatusTableLastChangeTid_Type())
acdAlarmStatusTableLastChangeTid.setMaxAccess(_C)
if mibBuilder.loadTexts:acdAlarmStatusTableLastChangeTid.setStatus(_B)
acdAlarmGenGroup=ObjectGroup((1,3,6,1,4,1,22420,2,1,15,3,2,1))
acdAlarmGenGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:acdAlarmGenGroup.setStatus(_B)
acdAlarmCfgGroup=ObjectGroup((1,3,6,1,4,1,22420,2,1,15,3,2,2))
acdAlarmCfgGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_a),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:acdAlarmCfgGroup.setStatus(_B)
acdAlarmStatusGroup=ObjectGroup((1,3,6,1,4,1,22420,2,1,15,3,2,3))
acdAlarmStatusGroup.setObjects(*((_A,_R),(_A,_b),(_A,_c),(_A,_N),(_A,_d)))
if mibBuilder.loadTexts:acdAlarmStatusGroup.setStatus(_B)
acdAlarmTidGroup=ObjectGroup((1,3,6,1,4,1,22420,2,1,15,3,2,5))
acdAlarmTidGroup.setObjects(*((_A,_e),(_A,_f)))
if mibBuilder.loadTexts:acdAlarmTidGroup.setStatus(_B)
acdAlarmActiveState=NotificationType((1,3,6,1,4,1,22420,2,1,12,1))
acdAlarmActiveState.setObjects(*((_A,_F),(_A,_G),(_A,_I),(_A,_J),(_A,_H),(_A,_N),(_A,_K),(_A,_L),(_A,_M),(_O,_P)))
if mibBuilder.loadTexts:acdAlarmActiveState.setStatus(_B)
acdAlarmClearState=NotificationType((1,3,6,1,4,1,22420,2,1,12,2))
acdAlarmClearState.setObjects(*((_A,_F),(_A,_G),(_A,_I),(_A,_J),(_A,_H),(_A,_N),(_A,_K),(_A,_L),(_A,_M),(_O,_P)))
if mibBuilder.loadTexts:acdAlarmClearState.setStatus(_B)
acdAlarmNotificationsGroup=NotificationGroup((1,3,6,1,4,1,22420,2,1,15,3,2,4))
acdAlarmNotificationsGroup.setObjects(*((_A,_g),(_A,_h)))
if mibBuilder.loadTexts:acdAlarmNotificationsGroup.setStatus(_B)
acdAlarmCompliance=ModuleCompliance((1,3,6,1,4,1,22420,2,1,15,3,1,1))
acdAlarmCompliance.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:acdAlarmCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'acdAlarm':acdAlarm,_U:acdAlarmGenThreshOn,_V:acdAlarmGenThreshOff,_W:acdAlarmGenLedEnable,_X:acdAlarmGenSyslogEnable,_Y:acdAlarmGenSNMPEnable,_Z:acdAlarmGen8023AHEnable,'acdAlarmCfgTable':acdAlarmCfgTable,'acdAlarmCfgEntry':acdAlarmCfgEntry,_F:acdAlarmCfgID,_G:acdAlarmCfgNumber,_H:acdAlarmCfgDesc,_a:acdAlarmCfgEnable,_I:acdAlarmCfgSeverity,_J:acdAlarmCfgServiceAffecting,_K:acdAlarmCfgExtNumber,_L:acdAlarmCfgConditionType,_M:acdAlarmCfgAMOType,'acdAlarmStatusTable':acdAlarmStatusTable,'acdAlarmStatusEntry':acdAlarmStatusEntry,_R:acdAlarmStatusID,_b:acdAlarmStatusNumber,_c:acdAlarmStatusOn,_N:acdAlarmStatusLastChange,_d:acdAlarmStatusMsg,'acdAlarmV2':acdAlarmV2,_g:acdAlarmActiveState,_h:acdAlarmClearState,'acdAlarmMIBObjects':acdAlarmMIBObjects,'acdAlarmConfig':acdAlarmConfig,'acdAlarmStatus':acdAlarmStatus,'acdAlarmConformance':acdAlarmConformance,'acdAlarmCompliances':acdAlarmCompliances,'acdAlarmCompliance':acdAlarmCompliance,'acdAlarmGroups':acdAlarmGroups,_i:acdAlarmGenGroup,_j:acdAlarmCfgGroup,_k:acdAlarmStatusGroup,_l:acdAlarmNotificationsGroup,_m:acdAlarmTidGroup,'acdAlarmTableTid':acdAlarmTableTid,_e:acdAlarmCfgTableLastChangeTid,_f:acdAlarmStatusTableLastChangeTid})