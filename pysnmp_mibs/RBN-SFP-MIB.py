_R='rbnSfpMonMIBNotificationGroup'
_Q='rbnSfpMonMIBObjectGroup'
_P='rbnSfpAlarm'
_O='rbnSfpAlarmServiceAffecting'
_N='rbnSfpActiveAlarmIndex'
_M='Unsigned32'
_L='SnmpAdminString'
_K='rbnSfpAlarmSeverity'
_J='rbnSfpAlarmProbableCause'
_I='rbnSfpAlarmDescription'
_H='rbnSfpAlarmDateAndTime'
_G='rbnSfpAlarmType'
_F='rbnSfpAlarmId'
_E='rbnSfpAlarmPort'
_D='rbnSfpAlarmCardSlot'
_C='read-only'
_B='current'
_A='RBN-SFP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAItuEventType,IANAItuProbableCause=mibBuilder.importSymbols('IANA-ITU-ALARM-TC-MIB','IANAItuEventType','IANAItuProbableCause')
ItuPerceivedSeverity,=mibBuilder.importSymbols('ITU-ALARM-TC-MIB','ItuPerceivedSeverity')
RbnAlarmId,RbnAlarmServiceAffecting=mibBuilder.importSymbols('RBN-ALARM-TC','RbnAlarmId','RbnAlarmServiceAffecting')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
RbnPort,RbnSlot=mibBuilder.importSymbols('RBN-TC','RbnPort','RbnSlot')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
rbnSfpMonMIB=ModuleIdentity((1,3,6,1,4,1,2352,2,49))
if mibBuilder.loadTexts:rbnSfpMonMIB.setRevisions(('2008-08-20 00:00',))
_RbnSfpMonMIBNotifications_ObjectIdentity=ObjectIdentity
rbnSfpMonMIBNotifications=_RbnSfpMonMIBNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,49,0))
_RbnSfpMonMIBObjects_ObjectIdentity=ObjectIdentity
rbnSfpMonMIBObjects=_RbnSfpMonMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,49,1))
_RbnSfpAlarmActiveTable_Object=MibTable
rbnSfpAlarmActiveTable=_RbnSfpAlarmActiveTable_Object((1,3,6,1,4,1,2352,2,49,1,1))
if mibBuilder.loadTexts:rbnSfpAlarmActiveTable.setStatus(_B)
_RbnSfpAlarmActiveEntry_Object=MibTableRow
rbnSfpAlarmActiveEntry=_RbnSfpAlarmActiveEntry_Object((1,3,6,1,4,1,2352,2,49,1,1,1))
rbnSfpAlarmActiveEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:rbnSfpAlarmActiveEntry.setStatus(_B)
class _RbnSfpActiveAlarmIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RbnSfpActiveAlarmIndex_Type.__name__=_M
_RbnSfpActiveAlarmIndex_Object=MibTableColumn
rbnSfpActiveAlarmIndex=_RbnSfpActiveAlarmIndex_Object((1,3,6,1,4,1,2352,2,49,1,1,1,1),_RbnSfpActiveAlarmIndex_Type())
rbnSfpActiveAlarmIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rbnSfpActiveAlarmIndex.setStatus(_B)
_RbnSfpAlarmCardSlot_Type=RbnSlot
_RbnSfpAlarmCardSlot_Object=MibTableColumn
rbnSfpAlarmCardSlot=_RbnSfpAlarmCardSlot_Object((1,3,6,1,4,1,2352,2,49,1,1,1,2),_RbnSfpAlarmCardSlot_Type())
rbnSfpAlarmCardSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnSfpAlarmCardSlot.setStatus(_B)
_RbnSfpAlarmPort_Type=RbnPort
_RbnSfpAlarmPort_Object=MibTableColumn
rbnSfpAlarmPort=_RbnSfpAlarmPort_Object((1,3,6,1,4,1,2352,2,49,1,1,1,3),_RbnSfpAlarmPort_Type())
rbnSfpAlarmPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnSfpAlarmPort.setStatus(_B)
_RbnSfpAlarmId_Type=RbnAlarmId
_RbnSfpAlarmId_Object=MibTableColumn
rbnSfpAlarmId=_RbnSfpAlarmId_Object((1,3,6,1,4,1,2352,2,49,1,1,1,4),_RbnSfpAlarmId_Type())
rbnSfpAlarmId.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnSfpAlarmId.setStatus(_B)
_RbnSfpAlarmSeverity_Type=ItuPerceivedSeverity
_RbnSfpAlarmSeverity_Object=MibTableColumn
rbnSfpAlarmSeverity=_RbnSfpAlarmSeverity_Object((1,3,6,1,4,1,2352,2,49,1,1,1,5),_RbnSfpAlarmSeverity_Type())
rbnSfpAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnSfpAlarmSeverity.setStatus(_B)
_RbnSfpAlarmType_Type=IANAItuEventType
_RbnSfpAlarmType_Object=MibTableColumn
rbnSfpAlarmType=_RbnSfpAlarmType_Object((1,3,6,1,4,1,2352,2,49,1,1,1,6),_RbnSfpAlarmType_Type())
rbnSfpAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnSfpAlarmType.setStatus(_B)
_RbnSfpAlarmDateAndTime_Type=DateAndTime
_RbnSfpAlarmDateAndTime_Object=MibTableColumn
rbnSfpAlarmDateAndTime=_RbnSfpAlarmDateAndTime_Object((1,3,6,1,4,1,2352,2,49,1,1,1,7),_RbnSfpAlarmDateAndTime_Type())
rbnSfpAlarmDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnSfpAlarmDateAndTime.setStatus(_B)
class _RbnSfpAlarmDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_RbnSfpAlarmDescription_Type.__name__=_L
_RbnSfpAlarmDescription_Object=MibTableColumn
rbnSfpAlarmDescription=_RbnSfpAlarmDescription_Object((1,3,6,1,4,1,2352,2,49,1,1,1,8),_RbnSfpAlarmDescription_Type())
rbnSfpAlarmDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnSfpAlarmDescription.setStatus(_B)
_RbnSfpAlarmProbableCause_Type=IANAItuProbableCause
_RbnSfpAlarmProbableCause_Object=MibTableColumn
rbnSfpAlarmProbableCause=_RbnSfpAlarmProbableCause_Object((1,3,6,1,4,1,2352,2,49,1,1,1,9),_RbnSfpAlarmProbableCause_Type())
rbnSfpAlarmProbableCause.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnSfpAlarmProbableCause.setStatus(_B)
_RbnSfpAlarmServiceAffecting_Type=RbnAlarmServiceAffecting
_RbnSfpAlarmServiceAffecting_Object=MibTableColumn
rbnSfpAlarmServiceAffecting=_RbnSfpAlarmServiceAffecting_Object((1,3,6,1,4,1,2352,2,49,1,1,1,10),_RbnSfpAlarmServiceAffecting_Type())
rbnSfpAlarmServiceAffecting.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnSfpAlarmServiceAffecting.setStatus(_B)
_RbnSfpMonMIBConformance_ObjectIdentity=ObjectIdentity
rbnSfpMonMIBConformance=_RbnSfpMonMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,49,2))
_RbnSfpMonMIBGroups_ObjectIdentity=ObjectIdentity
rbnSfpMonMIBGroups=_RbnSfpMonMIBGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,49,2,1))
_RbnSfpMonMIBCompliances_ObjectIdentity=ObjectIdentity
rbnSfpMonMIBCompliances=_RbnSfpMonMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,49,2,2))
rbnSfpMonMIBObjectGroup=ObjectGroup((1,3,6,1,4,1,2352,2,49,2,1,1))
rbnSfpMonMIBObjectGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_O)))
if mibBuilder.loadTexts:rbnSfpMonMIBObjectGroup.setStatus(_B)
rbnSfpAlarm=NotificationType((1,3,6,1,4,1,2352,2,49,0,1))
rbnSfpAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_K),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:rbnSfpAlarm.setStatus(_B)
rbnSfpMonMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,2352,2,49,2,1,2))
rbnSfpMonMIBNotificationGroup.setObjects((_A,_P))
if mibBuilder.loadTexts:rbnSfpMonMIBNotificationGroup.setStatus(_B)
rbnSfpMonMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,49,2,2,1))
rbnSfpMonMIBCompliance.setObjects(*((_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:rbnSfpMonMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'rbnSfpMonMIB':rbnSfpMonMIB,'rbnSfpMonMIBNotifications':rbnSfpMonMIBNotifications,_P:rbnSfpAlarm,'rbnSfpMonMIBObjects':rbnSfpMonMIBObjects,'rbnSfpAlarmActiveTable':rbnSfpAlarmActiveTable,'rbnSfpAlarmActiveEntry':rbnSfpAlarmActiveEntry,_N:rbnSfpActiveAlarmIndex,_D:rbnSfpAlarmCardSlot,_E:rbnSfpAlarmPort,_F:rbnSfpAlarmId,_K:rbnSfpAlarmSeverity,_G:rbnSfpAlarmType,_H:rbnSfpAlarmDateAndTime,_I:rbnSfpAlarmDescription,_J:rbnSfpAlarmProbableCause,_O:rbnSfpAlarmServiceAffecting,'rbnSfpMonMIBConformance':rbnSfpMonMIBConformance,'rbnSfpMonMIBGroups':rbnSfpMonMIBGroups,_Q:rbnSfpMonMIBObjectGroup,_R:rbnSfpMonMIBNotificationGroup,'rbnSfpMonMIBCompliances':rbnSfpMonMIBCompliances,'rbnSfpMonMIBCompliance':rbnSfpMonMIBCompliance})