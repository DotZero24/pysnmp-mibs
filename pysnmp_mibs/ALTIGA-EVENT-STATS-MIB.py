_K='altigaEventStatsGroupRev1'
_J='altigaEventStatsGroup'
_I='alStatsEventNotificationId'
_H='deprecated'
_G='alEventStatsCount'
_F='Integer32'
_E='alEventStatsEventNumber'
_D='alEventStatsClass'
_C='read-only'
_B='current'
_A='ALTIGA-EVENT-STATS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alEventMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alEventMibModule')
alEventGroup,alStatsEvent=mibBuilder.importSymbols('ALTIGA-MIB','alEventGroup','alStatsEvent')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
altigaEventStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,8,2))
if mibBuilder.loadTexts:altigaEventStatsMibModule.setRevisions(('2003-01-13 00:00','2002-07-10 00:00'))
_AltigaEventStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaEventStatsMibConformance=_AltigaEventStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,8,2,1))
_AltigaEventStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaEventStatsMibCompliances=_AltigaEventStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,8,2,1,1))
_AlStatsEventGlobal_ObjectIdentity=ObjectIdentity
alStatsEventGlobal=_AlStatsEventGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,4,1))
_AlStatsEventNotificationId_Type=DisplayString
_AlStatsEventNotificationId_Object=MibScalar
alStatsEventNotificationId=_AlStatsEventNotificationId_Object((1,3,6,1,4,1,3076,2,1,2,4,1,1),_AlStatsEventNotificationId_Type())
alStatsEventNotificationId.setMaxAccess(_C)
if mibBuilder.loadTexts:alStatsEventNotificationId.setStatus(_B)
_AlEventStatsTable_Object=MibTable
alEventStatsTable=_AlEventStatsTable_Object((1,3,6,1,4,1,3076,2,1,2,4,2))
if mibBuilder.loadTexts:alEventStatsTable.setStatus(_B)
_AlEventStatsEntry_Object=MibTableRow
alEventStatsEntry=_AlEventStatsEntry_Object((1,3,6,1,4,1,3076,2,1,2,4,2,1))
alEventStatsEntry.setIndexNames((0,_A,_D),(0,_A,_E))
if mibBuilder.loadTexts:alEventStatsEntry.setStatus(_B)
class _AlEventStatsClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlEventStatsClass_Type.__name__=_F
_AlEventStatsClass_Object=MibTableColumn
alEventStatsClass=_AlEventStatsClass_Object((1,3,6,1,4,1,3076,2,1,2,4,2,1,1),_AlEventStatsClass_Type())
alEventStatsClass.setMaxAccess(_C)
if mibBuilder.loadTexts:alEventStatsClass.setStatus(_B)
class _AlEventStatsEventNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlEventStatsEventNumber_Type.__name__=_F
_AlEventStatsEventNumber_Object=MibTableColumn
alEventStatsEventNumber=_AlEventStatsEventNumber_Object((1,3,6,1,4,1,3076,2,1,2,4,2,1,2),_AlEventStatsEventNumber_Type())
alEventStatsEventNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alEventStatsEventNumber.setStatus(_B)
_AlEventStatsCount_Type=Counter32
_AlEventStatsCount_Object=MibTableColumn
alEventStatsCount=_AlEventStatsCount_Object((1,3,6,1,4,1,3076,2,1,2,4,2,1,3),_AlEventStatsCount_Type())
alEventStatsCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alEventStatsCount.setStatus(_B)
altigaEventStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,4,2))
altigaEventStatsGroup.setObjects(*((_A,_D),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:altigaEventStatsGroup.setStatus(_H)
altigaEventStatsGroupRev1=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,4,3))
altigaEventStatsGroupRev1.setObjects(*((_A,_D),(_A,_E),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:altigaEventStatsGroupRev1.setStatus(_B)
altigaEventStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,8,2,1,1,1))
altigaEventStatsMibCompliance.setObjects((_A,_J))
if mibBuilder.loadTexts:altigaEventStatsMibCompliance.setStatus(_H)
altigaEventStatsMibComplianceRev1=ModuleCompliance((1,3,6,1,4,1,3076,1,1,8,2,1,1,2))
altigaEventStatsMibComplianceRev1.setObjects((_A,_K))
if mibBuilder.loadTexts:altigaEventStatsMibComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'altigaEventStatsMibModule':altigaEventStatsMibModule,'altigaEventStatsMibConformance':altigaEventStatsMibConformance,'altigaEventStatsMibCompliances':altigaEventStatsMibCompliances,'altigaEventStatsMibCompliance':altigaEventStatsMibCompliance,'altigaEventStatsMibComplianceRev1':altigaEventStatsMibComplianceRev1,_J:altigaEventStatsGroup,_K:altigaEventStatsGroupRev1,'alStatsEventGlobal':alStatsEventGlobal,_I:alStatsEventNotificationId,'alEventStatsTable':alEventStatsTable,'alEventStatsEntry':alEventStatsEntry,_D:alEventStatsClass,_E:alEventStatsEventNumber,_G:alEventStatsCount})