_I='slSonetAlarmServiceAffect'
_H='slSonetAlarmSeverity'
_G='slSonetAlarmStatus'
_F='Integer32'
_E='slSonetAlarmType'
_D='slSonetAlarmIfIndex'
_C='read-only'
_B='SL-SONET-ALARM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
slSonetMib,=mibBuilder.importSymbols('SL-SONET-MIB','slSonetMib')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
slSonetAlarmMib=ModuleIdentity((1,3,6,1,4,1,4515,1,6,4))
class SonetAlarmType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('losSonetAlarm',1),('lofSonetAlarm',2),('lopSonetAlarm',3),('aisSonetAlarm',4),('rfiSonetAlarm',5),('uneqSonetAlarm',6),('tim',7),('slm',8),('sd',9),('sf',10),('hwfail',11)))
_SlSonetAlarmConfig_ObjectIdentity=ObjectIdentity
slSonetAlarmConfig=_SlSonetAlarmConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,6,4,1))
_SlSonetAlarmConfigTable_Object=MibTable
slSonetAlarmConfigTable=_SlSonetAlarmConfigTable_Object((1,3,6,1,4,1,4515,1,6,4,1,1))
if mibBuilder.loadTexts:slSonetAlarmConfigTable.setStatus(_A)
_SlSonetAlarmConfigEntry_Object=MibTableRow
slSonetAlarmConfigEntry=_SlSonetAlarmConfigEntry_Object((1,3,6,1,4,1,4515,1,6,4,1,1,1))
slSonetAlarmConfigEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:slSonetAlarmConfigEntry.setStatus(_A)
_SlSonetAlarmIfIndex_Type=InterfaceIndex
_SlSonetAlarmIfIndex_Object=MibTableColumn
slSonetAlarmIfIndex=_SlSonetAlarmIfIndex_Object((1,3,6,1,4,1,4515,1,6,4,1,1,1,1),_SlSonetAlarmIfIndex_Type())
slSonetAlarmIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:slSonetAlarmIfIndex.setStatus(_A)
_SlSonetAlarmType_Type=SonetAlarmType
_SlSonetAlarmType_Object=MibTableColumn
slSonetAlarmType=_SlSonetAlarmType_Object((1,3,6,1,4,1,4515,1,6,4,1,1,1,2),_SlSonetAlarmType_Type())
slSonetAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:slSonetAlarmType.setStatus(_A)
_SlSonetAlarmMask_Type=TruthValue
_SlSonetAlarmMask_Object=MibTableColumn
slSonetAlarmMask=_SlSonetAlarmMask_Object((1,3,6,1,4,1,4515,1,6,4,1,1,1,3),_SlSonetAlarmMask_Type())
slSonetAlarmMask.setMaxAccess('read-write')
if mibBuilder.loadTexts:slSonetAlarmMask.setStatus(_A)
_SlSonetAlarmStatus_Type=TruthValue
_SlSonetAlarmStatus_Object=MibTableColumn
slSonetAlarmStatus=_SlSonetAlarmStatus_Object((1,3,6,1,4,1,4515,1,6,4,1,1,1,4),_SlSonetAlarmStatus_Type())
slSonetAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:slSonetAlarmStatus.setStatus(_A)
_SlSonetAlarmTraps_ObjectIdentity=ObjectIdentity
slSonetAlarmTraps=_SlSonetAlarmTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,6,4,2))
class _SlSonetAlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noAlarm',0),('critical',1),('major',2),('minor',3)))
_SlSonetAlarmSeverity_Type.__name__=_F
_SlSonetAlarmSeverity_Object=MibScalar
slSonetAlarmSeverity=_SlSonetAlarmSeverity_Object((1,3,6,1,4,1,4515,1,6,4,2,1),_SlSonetAlarmSeverity_Type())
slSonetAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:slSonetAlarmSeverity.setStatus(_A)
_SlSonetAlarmServiceAffect_Type=TruthValue
_SlSonetAlarmServiceAffect_Object=MibScalar
slSonetAlarmServiceAffect=_SlSonetAlarmServiceAffect_Object((1,3,6,1,4,1,4515,1,6,4,2,2),_SlSonetAlarmServiceAffect_Type())
slSonetAlarmServiceAffect.setMaxAccess(_C)
if mibBuilder.loadTexts:slSonetAlarmServiceAffect.setStatus(_A)
slSonetAlarmTrap=NotificationType((1,3,6,1,4,1,4515,1,6,4,2,3))
slSonetAlarmTrap.setObjects(*((_B,_D),(_B,_E),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:slSonetAlarmTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SonetAlarmType':SonetAlarmType,'slSonetAlarmMib':slSonetAlarmMib,'slSonetAlarmConfig':slSonetAlarmConfig,'slSonetAlarmConfigTable':slSonetAlarmConfigTable,'slSonetAlarmConfigEntry':slSonetAlarmConfigEntry,_D:slSonetAlarmIfIndex,_E:slSonetAlarmType,'slSonetAlarmMask':slSonetAlarmMask,_G:slSonetAlarmStatus,'slSonetAlarmTraps':slSonetAlarmTraps,_H:slSonetAlarmSeverity,_I:slSonetAlarmServiceAffect,'slSonetAlarmTrap':slSonetAlarmTrap})