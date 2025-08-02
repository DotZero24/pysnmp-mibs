_r='ceAlarmFilterProfileGroup'
_q='ceAlarmFilterGroup'
_p='ceAlarmHistGroup'
_o='ceAlarmGroup'
_n='ceAlarmDescriptionGroup'
_m='ceAlarmFilterSyslogEnabled'
_l='ceAlarmFilterNotifiesEnabled'
_k='ceAlarmFilterAlarmsEnabled'
_j='ceAlarmFilterAlias'
_i='ceAlarmFilterStatus'
_h='ceAlarmFilterProfileIndexNext'
_g='ceAlarmSyslogEnable'
_f='ceAlarmNotifiesEnable'
_e='ceAlarmHistType'
_d='ceAlarmHistLastIndex'
_c='ceAlarmHistTableSize'
_b='ceAlarmList'
_a='ceAlarmSeverity'
_Z='ceAlarmFilterProfile'
_Y='ceAlarmCutOff'
_X='ceAlarmMinorCount'
_W='ceAlarmMajorCount'
_V='ceAlarmCriticalCount'
_U='ceAlarmDescrText'
_T='ceAlarmDescrSeverity'
_S='ceAlarmDescrVendorType'
_R='ceAlarmFilterIndex'
_Q='ceAlarmHistIndex'
_P='ceAlarmDescrAlarmType'
_O='entPhysicalIndex'
_N='ENTITY-MIB'
_M='Unsigned32'
_L='ceAlarmDescrIndex'
_K='Integer32'
_J='ceAlarmHistTimeStamp'
_I='ceAlarmHistSeverity'
_H='ceAlarmHistAlarmType'
_G='ceAlarmHistEntPhysicalIndex'
_F='not-accessible'
_E='read-create'
_D='read-write'
_C='read-only'
_B='CISCO-ENTITY-ALARM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
Unsigned32,=mibBuilder.importSymbols('CISCO-TC',_M)
PhysicalIndex,entPhysicalIndex=mibBuilder.importSymbols(_N,'PhysicalIndex',_O)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
AutonomousType,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
ciscoEntityAlarmMIB=ModuleIdentity((1,3,6,1,4,1,9,9,138))
class AlarmType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class AlarmSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('critical',1),('major',2),('minor',3),('info',4)))
class AlarmSeverityOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
class AlarmList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class AlarmFilterProfileType(TextualConvention,Unsigned32):status=_A
_CiscoEntityAlarmMIBObjects_ObjectIdentity=ObjectIdentity
ciscoEntityAlarmMIBObjects=_CiscoEntityAlarmMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,138,1))
_CeAlarmDescription_ObjectIdentity=ObjectIdentity
ceAlarmDescription=_CeAlarmDescription_ObjectIdentity((1,3,6,1,4,1,9,9,138,1,1))
_CeAlarmDescrMapTable_Object=MibTable
ceAlarmDescrMapTable=_CeAlarmDescrMapTable_Object((1,3,6,1,4,1,9,9,138,1,1,1))
if mibBuilder.loadTexts:ceAlarmDescrMapTable.setStatus(_A)
_CeAlarmDescrMapEntry_Object=MibTableRow
ceAlarmDescrMapEntry=_CeAlarmDescrMapEntry_Object((1,3,6,1,4,1,9,9,138,1,1,1,1))
ceAlarmDescrMapEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:ceAlarmDescrMapEntry.setStatus(_A)
_CeAlarmDescrIndex_Type=Unsigned32
_CeAlarmDescrIndex_Object=MibTableColumn
ceAlarmDescrIndex=_CeAlarmDescrIndex_Object((1,3,6,1,4,1,9,9,138,1,1,1,1,1),_CeAlarmDescrIndex_Type())
ceAlarmDescrIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ceAlarmDescrIndex.setStatus(_A)
_CeAlarmDescrVendorType_Type=AutonomousType
_CeAlarmDescrVendorType_Object=MibTableColumn
ceAlarmDescrVendorType=_CeAlarmDescrVendorType_Object((1,3,6,1,4,1,9,9,138,1,1,1,1,2),_CeAlarmDescrVendorType_Type())
ceAlarmDescrVendorType.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAlarmDescrVendorType.setStatus(_A)
_CeAlarmDescrTable_Object=MibTable
ceAlarmDescrTable=_CeAlarmDescrTable_Object((1,3,6,1,4,1,9,9,138,1,1,2))
if mibBuilder.loadTexts:ceAlarmDescrTable.setStatus(_A)
_CeAlarmDescrEntry_Object=MibTableRow
ceAlarmDescrEntry=_CeAlarmDescrEntry_Object((1,3,6,1,4,1,9,9,138,1,1,2,1))
ceAlarmDescrEntry.setIndexNames((0,_B,_L),(0,_B,_P))
if mibBuilder.loadTexts:ceAlarmDescrEntry.setStatus(_A)
_CeAlarmDescrAlarmType_Type=AlarmType
_CeAlarmDescrAlarmType_Object=MibTableColumn
ceAlarmDescrAlarmType=_CeAlarmDescrAlarmType_Object((1,3,6,1,4,1,9,9,138,1,1,2,1,1),_CeAlarmDescrAlarmType_Type())
ceAlarmDescrAlarmType.setMaxAccess(_F)
if mibBuilder.loadTexts:ceAlarmDescrAlarmType.setStatus(_A)
_CeAlarmDescrSeverity_Type=AlarmSeverityOrZero
_CeAlarmDescrSeverity_Object=MibTableColumn
ceAlarmDescrSeverity=_CeAlarmDescrSeverity_Object((1,3,6,1,4,1,9,9,138,1,1,2,1,2),_CeAlarmDescrSeverity_Type())
ceAlarmDescrSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:ceAlarmDescrSeverity.setStatus(_A)
_CeAlarmDescrText_Type=SnmpAdminString
_CeAlarmDescrText_Object=MibTableColumn
ceAlarmDescrText=_CeAlarmDescrText_Object((1,3,6,1,4,1,9,9,138,1,1,2,1,3),_CeAlarmDescrText_Type())
ceAlarmDescrText.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAlarmDescrText.setStatus(_A)
_CeAlarmMonitoring_ObjectIdentity=ObjectIdentity
ceAlarmMonitoring=_CeAlarmMonitoring_ObjectIdentity((1,3,6,1,4,1,9,9,138,1,2))
_CeAlarmCriticalCount_Type=Gauge32
_CeAlarmCriticalCount_Object=MibScalar
ceAlarmCriticalCount=_CeAlarmCriticalCount_Object((1,3,6,1,4,1,9,9,138,1,2,1),_CeAlarmCriticalCount_Type())
ceAlarmCriticalCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAlarmCriticalCount.setStatus(_A)
_CeAlarmMajorCount_Type=Gauge32
_CeAlarmMajorCount_Object=MibScalar
ceAlarmMajorCount=_CeAlarmMajorCount_Object((1,3,6,1,4,1,9,9,138,1,2,2),_CeAlarmMajorCount_Type())
ceAlarmMajorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAlarmMajorCount.setStatus(_A)
_CeAlarmMinorCount_Type=Gauge32
_CeAlarmMinorCount_Object=MibScalar
ceAlarmMinorCount=_CeAlarmMinorCount_Object((1,3,6,1,4,1,9,9,138,1,2,3),_CeAlarmMinorCount_Type())
ceAlarmMinorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAlarmMinorCount.setStatus(_A)
_CeAlarmCutOff_Type=TruthValue
_CeAlarmCutOff_Object=MibScalar
ceAlarmCutOff=_CeAlarmCutOff_Object((1,3,6,1,4,1,9,9,138,1,2,4),_CeAlarmCutOff_Type())
ceAlarmCutOff.setMaxAccess(_D)
if mibBuilder.loadTexts:ceAlarmCutOff.setStatus(_A)
_CeAlarmTable_Object=MibTable
ceAlarmTable=_CeAlarmTable_Object((1,3,6,1,4,1,9,9,138,1,2,5))
if mibBuilder.loadTexts:ceAlarmTable.setStatus(_A)
_CeAlarmEntry_Object=MibTableRow
ceAlarmEntry=_CeAlarmEntry_Object((1,3,6,1,4,1,9,9,138,1,2,5,1))
ceAlarmEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:ceAlarmEntry.setStatus(_A)
_CeAlarmFilterProfile_Type=AlarmFilterProfileType
_CeAlarmFilterProfile_Object=MibTableColumn
ceAlarmFilterProfile=_CeAlarmFilterProfile_Object((1,3,6,1,4,1,9,9,138,1,2,5,1,1),_CeAlarmFilterProfile_Type())
ceAlarmFilterProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:ceAlarmFilterProfile.setStatus(_A)
_CeAlarmSeverity_Type=AlarmSeverityOrZero
_CeAlarmSeverity_Object=MibTableColumn
ceAlarmSeverity=_CeAlarmSeverity_Object((1,3,6,1,4,1,9,9,138,1,2,5,1,2),_CeAlarmSeverity_Type())
ceAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAlarmSeverity.setStatus(_A)
_CeAlarmList_Type=AlarmList
_CeAlarmList_Object=MibTableColumn
ceAlarmList=_CeAlarmList_Object((1,3,6,1,4,1,9,9,138,1,2,5,1,3),_CeAlarmList_Type())
ceAlarmList.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAlarmList.setStatus(_A)
_CeAlarmHistory_ObjectIdentity=ObjectIdentity
ceAlarmHistory=_CeAlarmHistory_ObjectIdentity((1,3,6,1,4,1,9,9,138,1,3))
class _CeAlarmHistTableSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CeAlarmHistTableSize_Type.__name__=_K
_CeAlarmHistTableSize_Object=MibScalar
ceAlarmHistTableSize=_CeAlarmHistTableSize_Object((1,3,6,1,4,1,9,9,138,1,3,1),_CeAlarmHistTableSize_Type())
ceAlarmHistTableSize.setMaxAccess(_D)
if mibBuilder.loadTexts:ceAlarmHistTableSize.setStatus(_A)
_CeAlarmHistLastIndex_Type=Unsigned32
_CeAlarmHistLastIndex_Object=MibScalar
ceAlarmHistLastIndex=_CeAlarmHistLastIndex_Object((1,3,6,1,4,1,9,9,138,1,3,2),_CeAlarmHistLastIndex_Type())
ceAlarmHistLastIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAlarmHistLastIndex.setStatus(_A)
_CeAlarmHistTable_Object=MibTable
ceAlarmHistTable=_CeAlarmHistTable_Object((1,3,6,1,4,1,9,9,138,1,3,3))
if mibBuilder.loadTexts:ceAlarmHistTable.setStatus(_A)
_CeAlarmHistEntry_Object=MibTableRow
ceAlarmHistEntry=_CeAlarmHistEntry_Object((1,3,6,1,4,1,9,9,138,1,3,3,1))
ceAlarmHistEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:ceAlarmHistEntry.setStatus(_A)
_CeAlarmHistIndex_Type=Unsigned32
_CeAlarmHistIndex_Object=MibTableColumn
ceAlarmHistIndex=_CeAlarmHistIndex_Object((1,3,6,1,4,1,9,9,138,1,3,3,1,1),_CeAlarmHistIndex_Type())
ceAlarmHistIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ceAlarmHistIndex.setStatus(_A)
class _CeAlarmHistType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('asserted',1),('cleared',2)))
_CeAlarmHistType_Type.__name__=_K
_CeAlarmHistType_Object=MibTableColumn
ceAlarmHistType=_CeAlarmHistType_Object((1,3,6,1,4,1,9,9,138,1,3,3,1,2),_CeAlarmHistType_Type())
ceAlarmHistType.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAlarmHistType.setStatus(_A)
_CeAlarmHistEntPhysicalIndex_Type=PhysicalIndex
_CeAlarmHistEntPhysicalIndex_Object=MibTableColumn
ceAlarmHistEntPhysicalIndex=_CeAlarmHistEntPhysicalIndex_Object((1,3,6,1,4,1,9,9,138,1,3,3,1,3),_CeAlarmHistEntPhysicalIndex_Type())
ceAlarmHistEntPhysicalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAlarmHistEntPhysicalIndex.setStatus(_A)
_CeAlarmHistAlarmType_Type=AlarmType
_CeAlarmHistAlarmType_Object=MibTableColumn
ceAlarmHistAlarmType=_CeAlarmHistAlarmType_Object((1,3,6,1,4,1,9,9,138,1,3,3,1,4),_CeAlarmHistAlarmType_Type())
ceAlarmHistAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAlarmHistAlarmType.setStatus(_A)
_CeAlarmHistSeverity_Type=AlarmSeverity
_CeAlarmHistSeverity_Object=MibTableColumn
ceAlarmHistSeverity=_CeAlarmHistSeverity_Object((1,3,6,1,4,1,9,9,138,1,3,3,1,5),_CeAlarmHistSeverity_Type())
ceAlarmHistSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAlarmHistSeverity.setStatus(_A)
_CeAlarmHistTimeStamp_Type=TimeStamp
_CeAlarmHistTimeStamp_Object=MibTableColumn
ceAlarmHistTimeStamp=_CeAlarmHistTimeStamp_Object((1,3,6,1,4,1,9,9,138,1,3,3,1,6),_CeAlarmHistTimeStamp_Type())
ceAlarmHistTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAlarmHistTimeStamp.setStatus(_A)
_CeAlarmFiltering_ObjectIdentity=ObjectIdentity
ceAlarmFiltering=_CeAlarmFiltering_ObjectIdentity((1,3,6,1,4,1,9,9,138,1,4))
_CeAlarmNotifiesEnable_Type=AlarmSeverityOrZero
_CeAlarmNotifiesEnable_Object=MibScalar
ceAlarmNotifiesEnable=_CeAlarmNotifiesEnable_Object((1,3,6,1,4,1,9,9,138,1,4,1),_CeAlarmNotifiesEnable_Type())
ceAlarmNotifiesEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ceAlarmNotifiesEnable.setStatus(_A)
_CeAlarmSyslogEnable_Type=AlarmSeverityOrZero
_CeAlarmSyslogEnable_Object=MibScalar
ceAlarmSyslogEnable=_CeAlarmSyslogEnable_Object((1,3,6,1,4,1,9,9,138,1,4,2),_CeAlarmSyslogEnable_Type())
ceAlarmSyslogEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ceAlarmSyslogEnable.setStatus(_A)
_CeAlarmFilterProfileIndexNext_Type=AlarmFilterProfileType
_CeAlarmFilterProfileIndexNext_Object=MibScalar
ceAlarmFilterProfileIndexNext=_CeAlarmFilterProfileIndexNext_Object((1,3,6,1,4,1,9,9,138,1,4,3),_CeAlarmFilterProfileIndexNext_Type())
ceAlarmFilterProfileIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:ceAlarmFilterProfileIndexNext.setStatus(_A)
_CeAlarmFilterProfileTable_Object=MibTable
ceAlarmFilterProfileTable=_CeAlarmFilterProfileTable_Object((1,3,6,1,4,1,9,9,138,1,4,4))
if mibBuilder.loadTexts:ceAlarmFilterProfileTable.setStatus(_A)
_CeAlarmFilterProfileEntry_Object=MibTableRow
ceAlarmFilterProfileEntry=_CeAlarmFilterProfileEntry_Object((1,3,6,1,4,1,9,9,138,1,4,4,1))
ceAlarmFilterProfileEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:ceAlarmFilterProfileEntry.setStatus(_A)
_CeAlarmFilterIndex_Type=AlarmFilterProfileType
_CeAlarmFilterIndex_Object=MibTableColumn
ceAlarmFilterIndex=_CeAlarmFilterIndex_Object((1,3,6,1,4,1,9,9,138,1,4,4,1,1),_CeAlarmFilterIndex_Type())
ceAlarmFilterIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ceAlarmFilterIndex.setStatus(_A)
_CeAlarmFilterStatus_Type=RowStatus
_CeAlarmFilterStatus_Object=MibTableColumn
ceAlarmFilterStatus=_CeAlarmFilterStatus_Object((1,3,6,1,4,1,9,9,138,1,4,4,1,2),_CeAlarmFilterStatus_Type())
ceAlarmFilterStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ceAlarmFilterStatus.setStatus(_A)
_CeAlarmFilterAlias_Type=DisplayString
_CeAlarmFilterAlias_Object=MibTableColumn
ceAlarmFilterAlias=_CeAlarmFilterAlias_Object((1,3,6,1,4,1,9,9,138,1,4,4,1,3),_CeAlarmFilterAlias_Type())
ceAlarmFilterAlias.setMaxAccess(_E)
if mibBuilder.loadTexts:ceAlarmFilterAlias.setStatus(_A)
_CeAlarmFilterAlarmsEnabled_Type=AlarmList
_CeAlarmFilterAlarmsEnabled_Object=MibTableColumn
ceAlarmFilterAlarmsEnabled=_CeAlarmFilterAlarmsEnabled_Object((1,3,6,1,4,1,9,9,138,1,4,4,1,4),_CeAlarmFilterAlarmsEnabled_Type())
ceAlarmFilterAlarmsEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:ceAlarmFilterAlarmsEnabled.setStatus(_A)
_CeAlarmFilterNotifiesEnabled_Type=AlarmList
_CeAlarmFilterNotifiesEnabled_Object=MibTableColumn
ceAlarmFilterNotifiesEnabled=_CeAlarmFilterNotifiesEnabled_Object((1,3,6,1,4,1,9,9,138,1,4,4,1,5),_CeAlarmFilterNotifiesEnabled_Type())
ceAlarmFilterNotifiesEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:ceAlarmFilterNotifiesEnabled.setStatus(_A)
_CeAlarmFilterSyslogEnabled_Type=AlarmList
_CeAlarmFilterSyslogEnabled_Object=MibTableColumn
ceAlarmFilterSyslogEnabled=_CeAlarmFilterSyslogEnabled_Object((1,3,6,1,4,1,9,9,138,1,4,4,1,6),_CeAlarmFilterSyslogEnabled_Type())
ceAlarmFilterSyslogEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:ceAlarmFilterSyslogEnabled.setStatus(_A)
_CiscoEntityAlarmMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
ciscoEntityAlarmMIBNotificationsPrefix=_CiscoEntityAlarmMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,138,2))
_CiscoEntityAlarmMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoEntityAlarmMIBNotifications=_CiscoEntityAlarmMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,138,2,0))
_CiscoEntityAlarmMIBConformance_ObjectIdentity=ObjectIdentity
ciscoEntityAlarmMIBConformance=_CiscoEntityAlarmMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,138,3))
_CiscoEntityAlarmMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoEntityAlarmMIBCompliances=_CiscoEntityAlarmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,138,3,1))
_CiscoEntityAlarmMIBGroups_ObjectIdentity=ObjectIdentity
ciscoEntityAlarmMIBGroups=_CiscoEntityAlarmMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,138,3,2))
ceAlarmDescriptionGroup=ObjectGroup((1,3,6,1,4,1,9,9,138,3,2,1))
ceAlarmDescriptionGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ceAlarmDescriptionGroup.setStatus(_A)
ceAlarmGroup=ObjectGroup((1,3,6,1,4,1,9,9,138,3,2,2))
ceAlarmGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:ceAlarmGroup.setStatus(_A)
ceAlarmHistGroup=ObjectGroup((1,3,6,1,4,1,9,9,138,3,2,3))
ceAlarmHistGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:ceAlarmHistGroup.setStatus(_A)
ceAlarmFilterGroup=ObjectGroup((1,3,6,1,4,1,9,9,138,3,2,4))
ceAlarmFilterGroup.setObjects(*((_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ceAlarmFilterGroup.setStatus(_A)
ceAlarmFilterProfileGroup=ObjectGroup((1,3,6,1,4,1,9,9,138,3,2,5))
ceAlarmFilterProfileGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:ceAlarmFilterProfileGroup.setStatus(_A)
ceAlarmAsserted=NotificationType((1,3,6,1,4,1,9,9,138,2,0,1))
ceAlarmAsserted.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:ceAlarmAsserted.setStatus(_A)
ceAlarmCleared=NotificationType((1,3,6,1,4,1,9,9,138,2,0,2))
ceAlarmCleared.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:ceAlarmCleared.setStatus(_A)
ceAlarmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,138,3,1,1))
ceAlarmMIBCompliance.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:ceAlarmMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AlarmType':AlarmType,'AlarmSeverity':AlarmSeverity,'AlarmSeverityOrZero':AlarmSeverityOrZero,'AlarmList':AlarmList,'AlarmFilterProfileType':AlarmFilterProfileType,'ciscoEntityAlarmMIB':ciscoEntityAlarmMIB,'ciscoEntityAlarmMIBObjects':ciscoEntityAlarmMIBObjects,'ceAlarmDescription':ceAlarmDescription,'ceAlarmDescrMapTable':ceAlarmDescrMapTable,'ceAlarmDescrMapEntry':ceAlarmDescrMapEntry,_L:ceAlarmDescrIndex,_S:ceAlarmDescrVendorType,'ceAlarmDescrTable':ceAlarmDescrTable,'ceAlarmDescrEntry':ceAlarmDescrEntry,_P:ceAlarmDescrAlarmType,_T:ceAlarmDescrSeverity,_U:ceAlarmDescrText,'ceAlarmMonitoring':ceAlarmMonitoring,_V:ceAlarmCriticalCount,_W:ceAlarmMajorCount,_X:ceAlarmMinorCount,_Y:ceAlarmCutOff,'ceAlarmTable':ceAlarmTable,'ceAlarmEntry':ceAlarmEntry,_Z:ceAlarmFilterProfile,_a:ceAlarmSeverity,_b:ceAlarmList,'ceAlarmHistory':ceAlarmHistory,_c:ceAlarmHistTableSize,_d:ceAlarmHistLastIndex,'ceAlarmHistTable':ceAlarmHistTable,'ceAlarmHistEntry':ceAlarmHistEntry,_Q:ceAlarmHistIndex,_e:ceAlarmHistType,_G:ceAlarmHistEntPhysicalIndex,_H:ceAlarmHistAlarmType,_I:ceAlarmHistSeverity,_J:ceAlarmHistTimeStamp,'ceAlarmFiltering':ceAlarmFiltering,_f:ceAlarmNotifiesEnable,_g:ceAlarmSyslogEnable,_h:ceAlarmFilterProfileIndexNext,'ceAlarmFilterProfileTable':ceAlarmFilterProfileTable,'ceAlarmFilterProfileEntry':ceAlarmFilterProfileEntry,_R:ceAlarmFilterIndex,_i:ceAlarmFilterStatus,_j:ceAlarmFilterAlias,_k:ceAlarmFilterAlarmsEnabled,_l:ceAlarmFilterNotifiesEnabled,_m:ceAlarmFilterSyslogEnabled,'ciscoEntityAlarmMIBNotificationsPrefix':ciscoEntityAlarmMIBNotificationsPrefix,'ciscoEntityAlarmMIBNotifications':ciscoEntityAlarmMIBNotifications,'ceAlarmAsserted':ceAlarmAsserted,'ceAlarmCleared':ceAlarmCleared,'ciscoEntityAlarmMIBConformance':ciscoEntityAlarmMIBConformance,'ciscoEntityAlarmMIBCompliances':ciscoEntityAlarmMIBCompliances,'ceAlarmMIBCompliance':ceAlarmMIBCompliance,'ciscoEntityAlarmMIBGroups':ciscoEntityAlarmMIBGroups,_n:ceAlarmDescriptionGroup,_o:ceAlarmGroup,_p:ceAlarmHistGroup,_q:ceAlarmFilterGroup,_r:ceAlarmFilterProfileGroup})