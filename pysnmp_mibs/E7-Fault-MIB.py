_O='e7AlarmType'
_N='e7AlarmObjectInstance8'
_M='e7AlarmObjectInstance7'
_L='e7AlarmObjectInstance6'
_K='e7AlarmObjectInstance5'
_J='e7AlarmObjectInstance4'
_I='e7AlarmObjectInstance3'
_H='e7AlarmObjectInstance2'
_G='e7AlarmObjectInstance1'
_F='e7AlarmObjectClass'
_E='OctetString'
_D='Integer32'
_C='E7-Fault-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
e7,e7Modules=mibBuilder.importSymbols('CALIX-PRODUCT-MIB','e7','e7Modules')
E7AlarmType,E7ObjectClass=mibBuilder.importSymbols('E7-TC','E7AlarmType','E7ObjectClass')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
e7FaultModule=ModuleIdentity((1,3,6,1,4,1,6321,1,2,2,1,2))
_E7Fault_ObjectIdentity=ObjectIdentity
e7Fault=_E7Fault_ObjectIdentity((1,3,6,1,4,1,6321,1,2,2,3))
_E7Alarms_ObjectIdentity=ObjectIdentity
e7Alarms=_E7Alarms_ObjectIdentity((1,3,6,1,4,1,6321,1,2,2,3,1))
_E7AlarmTable_Object=MibTable
e7AlarmTable=_E7AlarmTable_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1))
if mibBuilder.loadTexts:e7AlarmTable.setStatus(_A)
_E7AlarmEntry_Object=MibTableRow
e7AlarmEntry=_E7AlarmEntry_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1))
e7AlarmEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_H),(0,_C,_I),(0,_C,_J),(0,_C,_K),(0,_C,_L),(0,_C,_M),(0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:e7AlarmEntry.setStatus(_A)
_E7AlarmObjectClass_Type=E7ObjectClass
_E7AlarmObjectClass_Object=MibTableColumn
e7AlarmObjectClass=_E7AlarmObjectClass_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,1),_E7AlarmObjectClass_Type())
e7AlarmObjectClass.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmObjectClass.setStatus(_A)
_E7AlarmObjectInstance1_Type=Integer32
_E7AlarmObjectInstance1_Object=MibTableColumn
e7AlarmObjectInstance1=_E7AlarmObjectInstance1_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,2),_E7AlarmObjectInstance1_Type())
e7AlarmObjectInstance1.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmObjectInstance1.setStatus(_A)
_E7AlarmObjectInstance2_Type=Integer32
_E7AlarmObjectInstance2_Object=MibTableColumn
e7AlarmObjectInstance2=_E7AlarmObjectInstance2_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,3),_E7AlarmObjectInstance2_Type())
e7AlarmObjectInstance2.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmObjectInstance2.setStatus(_A)
_E7AlarmObjectInstance3_Type=Integer32
_E7AlarmObjectInstance3_Object=MibTableColumn
e7AlarmObjectInstance3=_E7AlarmObjectInstance3_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,4),_E7AlarmObjectInstance3_Type())
e7AlarmObjectInstance3.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmObjectInstance3.setStatus(_A)
_E7AlarmObjectInstance4_Type=Integer32
_E7AlarmObjectInstance4_Object=MibTableColumn
e7AlarmObjectInstance4=_E7AlarmObjectInstance4_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,5),_E7AlarmObjectInstance4_Type())
e7AlarmObjectInstance4.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmObjectInstance4.setStatus(_A)
_E7AlarmObjectInstance5_Type=Integer32
_E7AlarmObjectInstance5_Object=MibTableColumn
e7AlarmObjectInstance5=_E7AlarmObjectInstance5_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,6),_E7AlarmObjectInstance5_Type())
e7AlarmObjectInstance5.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmObjectInstance5.setStatus(_A)
_E7AlarmObjectInstance6_Type=Integer32
_E7AlarmObjectInstance6_Object=MibTableColumn
e7AlarmObjectInstance6=_E7AlarmObjectInstance6_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,7),_E7AlarmObjectInstance6_Type())
e7AlarmObjectInstance6.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmObjectInstance6.setStatus(_A)
_E7AlarmObjectInstance7_Type=Integer32
_E7AlarmObjectInstance7_Object=MibTableColumn
e7AlarmObjectInstance7=_E7AlarmObjectInstance7_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,8),_E7AlarmObjectInstance7_Type())
e7AlarmObjectInstance7.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmObjectInstance7.setStatus(_A)
_E7AlarmObjectInstance8_Type=Integer32
_E7AlarmObjectInstance8_Object=MibTableColumn
e7AlarmObjectInstance8=_E7AlarmObjectInstance8_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,9),_E7AlarmObjectInstance8_Type())
e7AlarmObjectInstance8.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmObjectInstance8.setStatus(_A)
_E7AlarmType_Type=E7AlarmType
_E7AlarmType_Object=MibTableColumn
e7AlarmType=_E7AlarmType_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,10),_E7AlarmType_Type())
e7AlarmType.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmType.setStatus(_A)
class _E7AlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('critical',1),('major',2),('minor',3),('warning',4),('unknown',5)))
_E7AlarmSeverity_Type.__name__=_D
_E7AlarmSeverity_Object=MibTableColumn
e7AlarmSeverity=_E7AlarmSeverity_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,11),_E7AlarmSeverity_Type())
e7AlarmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmSeverity.setStatus(_A)
class _E7AlarmTimeStamp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_E7AlarmTimeStamp_Type.__name__=_E
_E7AlarmTimeStamp_Object=MibTableColumn
e7AlarmTimeStamp=_E7AlarmTimeStamp_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,12),_E7AlarmTimeStamp_Type())
e7AlarmTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmTimeStamp.setStatus(_A)
class _E7AlarmServiceAffecting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_E7AlarmServiceAffecting_Type.__name__=_D
_E7AlarmServiceAffecting_Object=MibTableColumn
e7AlarmServiceAffecting=_E7AlarmServiceAffecting_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,13),_E7AlarmServiceAffecting_Type())
e7AlarmServiceAffecting.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmServiceAffecting.setStatus(_A)
class _E7AlarmLocationInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('nearEnd',1))
_E7AlarmLocationInfo_Type.__name__=_D
_E7AlarmLocationInfo_Object=MibTableColumn
e7AlarmLocationInfo=_E7AlarmLocationInfo_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,14),_E7AlarmLocationInfo_Type())
e7AlarmLocationInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmLocationInfo.setStatus(_A)
_E7AlarmText_Type=OctetString
_E7AlarmText_Object=MibTableColumn
e7AlarmText=_E7AlarmText_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,15),_E7AlarmText_Type())
e7AlarmText.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmText.setStatus(_A)
_E7AlarmTime_Type=Integer32
_E7AlarmTime_Object=MibTableColumn
e7AlarmTime=_E7AlarmTime_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,16),_E7AlarmTime_Type())
e7AlarmTime.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmTime.setStatus(_A)
_E7AlarmCliObject_Type=OctetString
_E7AlarmCliObject_Object=MibTableColumn
e7AlarmCliObject=_E7AlarmCliObject_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,17),_E7AlarmCliObject_Type())
e7AlarmCliObject.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmCliObject.setStatus(_A)
_E7AlarmSecObjectClass_Type=E7ObjectClass
_E7AlarmSecObjectClass_Object=MibTableColumn
e7AlarmSecObjectClass=_E7AlarmSecObjectClass_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,18),_E7AlarmSecObjectClass_Type())
e7AlarmSecObjectClass.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmSecObjectClass.setStatus(_A)
_E7AlarmSecObjectInstance1_Type=Integer32
_E7AlarmSecObjectInstance1_Object=MibTableColumn
e7AlarmSecObjectInstance1=_E7AlarmSecObjectInstance1_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,19),_E7AlarmSecObjectInstance1_Type())
e7AlarmSecObjectInstance1.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmSecObjectInstance1.setStatus(_A)
_E7AlarmSecObjectInstance2_Type=Integer32
_E7AlarmSecObjectInstance2_Object=MibTableColumn
e7AlarmSecObjectInstance2=_E7AlarmSecObjectInstance2_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,20),_E7AlarmSecObjectInstance2_Type())
e7AlarmSecObjectInstance2.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmSecObjectInstance2.setStatus(_A)
_E7AlarmSecObjectInstance3_Type=Integer32
_E7AlarmSecObjectInstance3_Object=MibTableColumn
e7AlarmSecObjectInstance3=_E7AlarmSecObjectInstance3_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,21),_E7AlarmSecObjectInstance3_Type())
e7AlarmSecObjectInstance3.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmSecObjectInstance3.setStatus(_A)
_E7AlarmSecObjectInstance4_Type=Integer32
_E7AlarmSecObjectInstance4_Object=MibTableColumn
e7AlarmSecObjectInstance4=_E7AlarmSecObjectInstance4_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,22),_E7AlarmSecObjectInstance4_Type())
e7AlarmSecObjectInstance4.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmSecObjectInstance4.setStatus(_A)
_E7AlarmSecObjectInstance5_Type=Integer32
_E7AlarmSecObjectInstance5_Object=MibTableColumn
e7AlarmSecObjectInstance5=_E7AlarmSecObjectInstance5_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,23),_E7AlarmSecObjectInstance5_Type())
e7AlarmSecObjectInstance5.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmSecObjectInstance5.setStatus(_A)
_E7AlarmSecObjectInstance6_Type=Integer32
_E7AlarmSecObjectInstance6_Object=MibTableColumn
e7AlarmSecObjectInstance6=_E7AlarmSecObjectInstance6_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,24),_E7AlarmSecObjectInstance6_Type())
e7AlarmSecObjectInstance6.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmSecObjectInstance6.setStatus(_A)
_E7AlarmSecObjectInstance7_Type=Integer32
_E7AlarmSecObjectInstance7_Object=MibTableColumn
e7AlarmSecObjectInstance7=_E7AlarmSecObjectInstance7_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,25),_E7AlarmSecObjectInstance7_Type())
e7AlarmSecObjectInstance7.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmSecObjectInstance7.setStatus(_A)
_E7AlarmSecObjectInstance8_Type=Integer32
_E7AlarmSecObjectInstance8_Object=MibTableColumn
e7AlarmSecObjectInstance8=_E7AlarmSecObjectInstance8_Object((1,3,6,1,4,1,6321,1,2,2,3,1,1,1,26),_E7AlarmSecObjectInstance8_Type())
e7AlarmSecObjectInstance8.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmSecObjectInstance8.setStatus(_A)
_E7AlarmTableEnd_Type=Integer32
_E7AlarmTableEnd_Object=MibScalar
e7AlarmTableEnd=_E7AlarmTableEnd_Object((1,3,6,1,4,1,6321,1,2,2,3,1,2),_E7AlarmTableEnd_Type())
e7AlarmTableEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmTableEnd.setStatus(_A)
_E7AlarmCount_ObjectIdentity=ObjectIdentity
e7AlarmCount=_E7AlarmCount_ObjectIdentity((1,3,6,1,4,1,6321,1,2,2,3,2))
_E7AlarmCountCritical_Type=Integer32
_E7AlarmCountCritical_Object=MibScalar
e7AlarmCountCritical=_E7AlarmCountCritical_Object((1,3,6,1,4,1,6321,1,2,2,3,2,1),_E7AlarmCountCritical_Type())
e7AlarmCountCritical.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmCountCritical.setStatus(_A)
_E7AlarmCountMajor_Type=Integer32
_E7AlarmCountMajor_Object=MibScalar
e7AlarmCountMajor=_E7AlarmCountMajor_Object((1,3,6,1,4,1,6321,1,2,2,3,2,2),_E7AlarmCountMajor_Type())
e7AlarmCountMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmCountMajor.setStatus(_A)
_E7AlarmCountMinor_Type=Integer32
_E7AlarmCountMinor_Object=MibScalar
e7AlarmCountMinor=_E7AlarmCountMinor_Object((1,3,6,1,4,1,6321,1,2,2,3,2,3),_E7AlarmCountMinor_Type())
e7AlarmCountMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmCountMinor.setStatus(_A)
_E7AlarmCountWarning_Type=Integer32
_E7AlarmCountWarning_Object=MibScalar
e7AlarmCountWarning=_E7AlarmCountWarning_Object((1,3,6,1,4,1,6321,1,2,2,3,2,4),_E7AlarmCountWarning_Type())
e7AlarmCountWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmCountWarning.setStatus(_A)
_E7AlarmCountInfo_Type=Integer32
_E7AlarmCountInfo_Object=MibScalar
e7AlarmCountInfo=_E7AlarmCountInfo_Object((1,3,6,1,4,1,6321,1,2,2,3,2,5),_E7AlarmCountInfo_Type())
e7AlarmCountInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:e7AlarmCountInfo.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'e7FaultModule':e7FaultModule,'e7Fault':e7Fault,'e7Alarms':e7Alarms,'e7AlarmTable':e7AlarmTable,'e7AlarmEntry':e7AlarmEntry,_F:e7AlarmObjectClass,_G:e7AlarmObjectInstance1,_H:e7AlarmObjectInstance2,_I:e7AlarmObjectInstance3,_J:e7AlarmObjectInstance4,_K:e7AlarmObjectInstance5,_L:e7AlarmObjectInstance6,_M:e7AlarmObjectInstance7,_N:e7AlarmObjectInstance8,_O:e7AlarmType,'e7AlarmSeverity':e7AlarmSeverity,'e7AlarmTimeStamp':e7AlarmTimeStamp,'e7AlarmServiceAffecting':e7AlarmServiceAffecting,'e7AlarmLocationInfo':e7AlarmLocationInfo,'e7AlarmText':e7AlarmText,'e7AlarmTime':e7AlarmTime,'e7AlarmCliObject':e7AlarmCliObject,'e7AlarmSecObjectClass':e7AlarmSecObjectClass,'e7AlarmSecObjectInstance1':e7AlarmSecObjectInstance1,'e7AlarmSecObjectInstance2':e7AlarmSecObjectInstance2,'e7AlarmSecObjectInstance3':e7AlarmSecObjectInstance3,'e7AlarmSecObjectInstance4':e7AlarmSecObjectInstance4,'e7AlarmSecObjectInstance5':e7AlarmSecObjectInstance5,'e7AlarmSecObjectInstance6':e7AlarmSecObjectInstance6,'e7AlarmSecObjectInstance7':e7AlarmSecObjectInstance7,'e7AlarmSecObjectInstance8':e7AlarmSecObjectInstance8,'e7AlarmTableEnd':e7AlarmTableEnd,'e7AlarmCount':e7AlarmCount,'e7AlarmCountCritical':e7AlarmCountCritical,'e7AlarmCountMajor':e7AlarmCountMajor,'e7AlarmCountMinor':e7AlarmCountMinor,'e7AlarmCountWarning':e7AlarmCountWarning,'e7AlarmCountInfo':e7AlarmCountInfo})