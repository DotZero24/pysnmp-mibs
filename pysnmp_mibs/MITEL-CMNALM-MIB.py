_M='mitelAlmActiveTblThresholdValue'
_L='mitelAlmActiveTblThresholdType'
_K='mitelAlmActiveTblSeverity'
_J='mitelAlmActiveTblTypeName'
_I='mitelAlmActiveTblType'
_H='mitelAlmActiveTblClass'
_G='mitelAlmSysSeverityDetectTime'
_F='mitelAlmSysSeverity'
_E='indeterminate'
_D='mitelAlmActiveTblIndex'
_C='MITEL-CMNALM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mitelConfCompliances,mitelConfGroups,mitelIdentification,mitelPropCommon=mibBuilder.importSymbols('MITEL-MIB','mitelConfCompliances','mitelConfGroups','mitelIdentification','mitelPropCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
mitelCmnAlarms=ModuleIdentity((1,3,6,1,4,1,1027,4,9,1))
if mibBuilder.loadTexts:mitelCmnAlarms.setRevisions(('2014-02-11 12:00','2005-02-21 21:34','2004-02-23 00:00'))
class ItuPerceivedSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('cleared',1),(_E,2),('critical',3),('major',4),('minor',5),('warning',6)))
class MitelCmnAlarmThresholdType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('percentage',1),('absoluteValue',2),(_E,3)))
_MitelCmnAlmObjects_ObjectIdentity=ObjectIdentity
mitelCmnAlmObjects=_MitelCmnAlmObjects_ObjectIdentity((1,3,6,1,4,1,1027,4,9,1,1))
if mibBuilder.loadTexts:mitelCmnAlmObjects.setStatus(_A)
_MitelAlmSystem_ObjectIdentity=ObjectIdentity
mitelAlmSystem=_MitelAlmSystem_ObjectIdentity((1,3,6,1,4,1,1027,4,9,1,1,1))
if mibBuilder.loadTexts:mitelAlmSystem.setStatus(_A)
_MitelAlmSysSeverity_Type=ItuPerceivedSeverity
_MitelAlmSysSeverity_Object=MibScalar
mitelAlmSysSeverity=_MitelAlmSysSeverity_Object((1,3,6,1,4,1,1027,4,9,1,1,1,1),_MitelAlmSysSeverity_Type())
mitelAlmSysSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAlmSysSeverity.setStatus(_A)
_MitelAlmSysSeverityDetectTime_Type=DateAndTime
_MitelAlmSysSeverityDetectTime_Object=MibScalar
mitelAlmSysSeverityDetectTime=_MitelAlmSysSeverityDetectTime_Object((1,3,6,1,4,1,1027,4,9,1,1,1,2),_MitelAlmSysSeverityDetectTime_Type())
mitelAlmSysSeverityDetectTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAlmSysSeverityDetectTime.setStatus(_A)
_MitelAlmSysSeverityDescr_Type=DisplayString
_MitelAlmSysSeverityDescr_Object=MibScalar
mitelAlmSysSeverityDescr=_MitelAlmSysSeverityDescr_Object((1,3,6,1,4,1,1027,4,9,1,1,1,3),_MitelAlmSysSeverityDescr_Type())
mitelAlmSysSeverityDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAlmSysSeverityDescr.setStatus(_A)
_MitelAlmActiveTable_Object=MibTable
mitelAlmActiveTable=_MitelAlmActiveTable_Object((1,3,6,1,4,1,1027,4,9,1,1,2))
if mibBuilder.loadTexts:mitelAlmActiveTable.setStatus(_A)
_MitelAlmActiveTableEntry_Object=MibTableRow
mitelAlmActiveTableEntry=_MitelAlmActiveTableEntry_Object((1,3,6,1,4,1,1027,4,9,1,1,2,1))
mitelAlmActiveTableEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:mitelAlmActiveTableEntry.setStatus(_A)
_MitelAlmActiveTblIndex_Type=ObjectIdentifier
_MitelAlmActiveTblIndex_Object=MibTableColumn
mitelAlmActiveTblIndex=_MitelAlmActiveTblIndex_Object((1,3,6,1,4,1,1027,4,9,1,1,2,1,1),_MitelAlmActiveTblIndex_Type())
mitelAlmActiveTblIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAlmActiveTblIndex.setStatus(_A)
_MitelAlmActiveTblClass_Type=DisplayString
_MitelAlmActiveTblClass_Object=MibTableColumn
mitelAlmActiveTblClass=_MitelAlmActiveTblClass_Object((1,3,6,1,4,1,1027,4,9,1,1,2,1,2),_MitelAlmActiveTblClass_Type())
mitelAlmActiveTblClass.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAlmActiveTblClass.setStatus(_A)
_MitelAlmActiveTblType_Type=DisplayString
_MitelAlmActiveTblType_Object=MibTableColumn
mitelAlmActiveTblType=_MitelAlmActiveTblType_Object((1,3,6,1,4,1,1027,4,9,1,1,2,1,3),_MitelAlmActiveTblType_Type())
mitelAlmActiveTblType.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAlmActiveTblType.setStatus(_A)
_MitelAlmActiveTblTypeName_Type=DisplayString
_MitelAlmActiveTblTypeName_Object=MibTableColumn
mitelAlmActiveTblTypeName=_MitelAlmActiveTblTypeName_Object((1,3,6,1,4,1,1027,4,9,1,1,2,1,4),_MitelAlmActiveTblTypeName_Type())
mitelAlmActiveTblTypeName.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAlmActiveTblTypeName.setStatus(_A)
_MitelAlmActiveTblSeverity_Type=ItuPerceivedSeverity
_MitelAlmActiveTblSeverity_Object=MibTableColumn
mitelAlmActiveTblSeverity=_MitelAlmActiveTblSeverity_Object((1,3,6,1,4,1,1027,4,9,1,1,2,1,5),_MitelAlmActiveTblSeverity_Type())
mitelAlmActiveTblSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAlmActiveTblSeverity.setStatus(_A)
_MitelAlmActiveTblSeverityDetectTime_Type=DateAndTime
_MitelAlmActiveTblSeverityDetectTime_Object=MibTableColumn
mitelAlmActiveTblSeverityDetectTime=_MitelAlmActiveTblSeverityDetectTime_Object((1,3,6,1,4,1,1027,4,9,1,1,2,1,6),_MitelAlmActiveTblSeverityDetectTime_Type())
mitelAlmActiveTblSeverityDetectTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAlmActiveTblSeverityDetectTime.setStatus(_A)
_MitelAlmActiveTblThresholdType_Type=MitelCmnAlarmThresholdType
_MitelAlmActiveTblThresholdType_Object=MibTableColumn
mitelAlmActiveTblThresholdType=_MitelAlmActiveTblThresholdType_Object((1,3,6,1,4,1,1027,4,9,1,1,2,1,7),_MitelAlmActiveTblThresholdType_Type())
mitelAlmActiveTblThresholdType.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAlmActiveTblThresholdType.setStatus(_A)
_MitelAlmActiveTblThresholdValue_Type=Integer32
_MitelAlmActiveTblThresholdValue_Object=MibTableColumn
mitelAlmActiveTblThresholdValue=_MitelAlmActiveTblThresholdValue_Object((1,3,6,1,4,1,1027,4,9,1,1,2,1,8),_MitelAlmActiveTblThresholdValue_Type())
mitelAlmActiveTblThresholdValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAlmActiveTblThresholdValue.setStatus(_A)
_MitelAlmActiveTblDescr_Type=DisplayString
_MitelAlmActiveTblDescr_Object=MibTableColumn
mitelAlmActiveTblDescr=_MitelAlmActiveTblDescr_Object((1,3,6,1,4,1,1027,4,9,1,1,2,1,9),_MitelAlmActiveTblDescr_Type())
mitelAlmActiveTblDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAlmActiveTblDescr.setStatus(_A)
_MitelCmnAlmNotifications_ObjectIdentity=ObjectIdentity
mitelCmnAlmNotifications=_MitelCmnAlmNotifications_ObjectIdentity((1,3,6,1,4,1,1027,4,9,1,2))
if mibBuilder.loadTexts:mitelCmnAlmNotifications.setStatus(_A)
_MitelCmnAlmConformance_ObjectIdentity=ObjectIdentity
mitelCmnAlmConformance=_MitelCmnAlmConformance_ObjectIdentity((1,3,6,1,4,1,1027,4,9,1,3))
if mibBuilder.loadTexts:mitelCmnAlmConformance.setStatus(_A)
mitelNotifActiveAlarm=NotificationType((1,3,6,1,4,1,1027,4,9,1,2,1))
mitelNotifActiveAlarm.setObjects(*((_C,_F),(_C,_G),(_C,_D),(_C,_H),(_C,_I),(_C,_J),(_C,_K),(_C,_L),(_C,_M)))
if mibBuilder.loadTexts:mitelNotifActiveAlarm.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ItuPerceivedSeverity':ItuPerceivedSeverity,'MitelCmnAlarmThresholdType':MitelCmnAlarmThresholdType,'mitelCmnAlarms':mitelCmnAlarms,'mitelCmnAlmObjects':mitelCmnAlmObjects,'mitelAlmSystem':mitelAlmSystem,_F:mitelAlmSysSeverity,_G:mitelAlmSysSeverityDetectTime,'mitelAlmSysSeverityDescr':mitelAlmSysSeverityDescr,'mitelAlmActiveTable':mitelAlmActiveTable,'mitelAlmActiveTableEntry':mitelAlmActiveTableEntry,_D:mitelAlmActiveTblIndex,_H:mitelAlmActiveTblClass,_I:mitelAlmActiveTblType,_J:mitelAlmActiveTblTypeName,_K:mitelAlmActiveTblSeverity,'mitelAlmActiveTblSeverityDetectTime':mitelAlmActiveTblSeverityDetectTime,_L:mitelAlmActiveTblThresholdType,_M:mitelAlmActiveTblThresholdValue,'mitelAlmActiveTblDescr':mitelAlmActiveTblDescr,'mitelCmnAlmNotifications':mitelCmnAlmNotifications,'mitelNotifActiveAlarm':mitelNotifActiveAlarm,'mitelCmnAlmConformance':mitelCmnAlmConformance})