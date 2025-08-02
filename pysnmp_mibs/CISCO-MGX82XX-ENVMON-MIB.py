_Q='cmEnvmonGeneralGroup'
_P='cmEnvmonInfoGroup'
_O='asmShelfAlarmState'
_N='asmNumOfValidEntries'
_M='asmClrButton'
_L='asmPhysicalAlarmState'
_K='asmUnitMeasuredValue'
_J='asmUnitMeasurable'
_I='asmAlarmSeverity'
_H='asmAlarmThreshold'
_G='asmAlarmUnitNum'
_F='asmAlarmType'
_E='asmAlarmNum'
_D='read-only'
_C='Integer32'
_B='CISCO-MGX82XX-ENVMON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
basisAsm,=mibBuilder.importSymbols('BASIS-MIB','basisAsm')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoMgx82xxEnvmonMIB=ModuleIdentity((1,3,6,1,4,1,351,150,70))
if mibBuilder.loadTexts:ciscoMgx82xxEnvmonMIB.setRevisions(('2003-04-17 00:00',))
_AsmAlarmTable_Object=MibTable
asmAlarmTable=_AsmAlarmTable_Object((1,3,6,1,4,1,351,110,1,2,1))
if mibBuilder.loadTexts:asmAlarmTable.setStatus(_A)
_AsmAlarmEntry_Object=MibTableRow
asmAlarmEntry=_AsmAlarmEntry_Object((1,3,6,1,4,1,351,110,1,2,1,1))
asmAlarmEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:asmAlarmEntry.setStatus(_A)
class _AsmAlarmNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_AsmAlarmNum_Type.__name__=_C
_AsmAlarmNum_Object=MibTableColumn
asmAlarmNum=_AsmAlarmNum_Object((1,3,6,1,4,1,351,110,1,2,1,1,1),_AsmAlarmNum_Type())
asmAlarmNum.setMaxAccess(_D)
if mibBuilder.loadTexts:asmAlarmNum.setStatus(_A)
class _AsmAlarmType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('alarmOther',1),('alarmTemperature',2),('alarmPSU',3),('alarmDCLevel',4),('alarmFanUnit',5)))
_AsmAlarmType_Type.__name__=_C
_AsmAlarmType_Object=MibTableColumn
asmAlarmType=_AsmAlarmType_Object((1,3,6,1,4,1,351,110,1,2,1,1,2),_AsmAlarmType_Type())
asmAlarmType.setMaxAccess(_D)
if mibBuilder.loadTexts:asmAlarmType.setStatus(_A)
class _AsmAlarmUnitNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AsmAlarmUnitNum_Type.__name__=_C
_AsmAlarmUnitNum_Object=MibTableColumn
asmAlarmUnitNum=_AsmAlarmUnitNum_Object((1,3,6,1,4,1,351,110,1,2,1,1,3),_AsmAlarmUnitNum_Type())
asmAlarmUnitNum.setMaxAccess(_D)
if mibBuilder.loadTexts:asmAlarmUnitNum.setStatus(_A)
class _AsmAlarmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AsmAlarmThreshold_Type.__name__=_C
_AsmAlarmThreshold_Object=MibTableColumn
asmAlarmThreshold=_AsmAlarmThreshold_Object((1,3,6,1,4,1,351,110,1,2,1,1,4),_AsmAlarmThreshold_Type())
asmAlarmThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:asmAlarmThreshold.setStatus(_A)
class _AsmAlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('alarmMinor',1),('alarmMajor',2)))
_AsmAlarmSeverity_Type.__name__=_C
_AsmAlarmSeverity_Object=MibTableColumn
asmAlarmSeverity=_AsmAlarmSeverity_Object((1,3,6,1,4,1,351,110,1,2,1,1,5),_AsmAlarmSeverity_Type())
asmAlarmSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:asmAlarmSeverity.setStatus(_A)
class _AsmUnitMeasurable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_AsmUnitMeasurable_Type.__name__=_C
_AsmUnitMeasurable_Object=MibTableColumn
asmUnitMeasurable=_AsmUnitMeasurable_Object((1,3,6,1,4,1,351,110,1,2,1,1,6),_AsmUnitMeasurable_Type())
asmUnitMeasurable.setMaxAccess(_D)
if mibBuilder.loadTexts:asmUnitMeasurable.setStatus(_A)
class _AsmUnitMeasuredValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AsmUnitMeasuredValue_Type.__name__=_C
_AsmUnitMeasuredValue_Object=MibTableColumn
asmUnitMeasuredValue=_AsmUnitMeasuredValue_Object((1,3,6,1,4,1,351,110,1,2,1,1,7),_AsmUnitMeasuredValue_Type())
asmUnitMeasuredValue.setMaxAccess(_D)
if mibBuilder.loadTexts:asmUnitMeasuredValue.setStatus(_A)
class _AsmPhysicalAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AsmPhysicalAlarmState_Type.__name__=_C
_AsmPhysicalAlarmState_Object=MibTableColumn
asmPhysicalAlarmState=_AsmPhysicalAlarmState_Object((1,3,6,1,4,1,351,110,1,2,1,1,8),_AsmPhysicalAlarmState_Type())
asmPhysicalAlarmState.setMaxAccess(_D)
if mibBuilder.loadTexts:asmPhysicalAlarmState.setStatus(_A)
class _AsmClrButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('asmAlarmNoAction',1),('asmAlarmClear',2)))
_AsmClrButton_Type.__name__=_C
_AsmClrButton_Object=MibTableColumn
asmClrButton=_AsmClrButton_Object((1,3,6,1,4,1,351,110,1,2,1,1,9),_AsmClrButton_Type())
asmClrButton.setMaxAccess('read-write')
if mibBuilder.loadTexts:asmClrButton.setStatus(_A)
class _AsmNumOfValidEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AsmNumOfValidEntries_Type.__name__=_C
_AsmNumOfValidEntries_Object=MibScalar
asmNumOfValidEntries=_AsmNumOfValidEntries_Object((1,3,6,1,4,1,351,110,1,2,2),_AsmNumOfValidEntries_Type())
asmNumOfValidEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:asmNumOfValidEntries.setStatus(_A)
class _AsmShelfAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('alarmOff',1),('alarmOn',2)))
_AsmShelfAlarmState_Type.__name__=_C
_AsmShelfAlarmState_Object=MibScalar
asmShelfAlarmState=_AsmShelfAlarmState_Object((1,3,6,1,4,1,351,110,1,2,3),_AsmShelfAlarmState_Type())
asmShelfAlarmState.setMaxAccess(_D)
if mibBuilder.loadTexts:asmShelfAlarmState.setStatus(_A)
_CmEnvmonMIBConformance_ObjectIdentity=ObjectIdentity
cmEnvmonMIBConformance=_CmEnvmonMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,70,2))
_CmEnvmonMIBGroups_ObjectIdentity=ObjectIdentity
cmEnvmonMIBGroups=_CmEnvmonMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,70,2,1))
_CmEnvmonMIBCompliances_ObjectIdentity=ObjectIdentity
cmEnvmonMIBCompliances=_CmEnvmonMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,70,2,2))
cmEnvmonInfoGroup=ObjectGroup((1,3,6,1,4,1,351,150,70,2,1,1))
cmEnvmonInfoGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:cmEnvmonInfoGroup.setStatus(_A)
cmEnvmonGeneralGroup=ObjectGroup((1,3,6,1,4,1,351,150,70,2,1,2))
cmEnvmonGeneralGroup.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:cmEnvmonGeneralGroup.setStatus(_A)
cmEnvmonCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,70,2,2,1))
cmEnvmonCompliance.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:cmEnvmonCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'asmAlarmTable':asmAlarmTable,'asmAlarmEntry':asmAlarmEntry,_E:asmAlarmNum,_F:asmAlarmType,_G:asmAlarmUnitNum,_H:asmAlarmThreshold,_I:asmAlarmSeverity,_J:asmUnitMeasurable,_K:asmUnitMeasuredValue,_L:asmPhysicalAlarmState,_M:asmClrButton,_N:asmNumOfValidEntries,_O:asmShelfAlarmState,'ciscoMgx82xxEnvmonMIB':ciscoMgx82xxEnvmonMIB,'cmEnvmonMIBConformance':cmEnvmonMIBConformance,'cmEnvmonMIBGroups':cmEnvmonMIBGroups,_P:cmEnvmonInfoGroup,_Q:cmEnvmonGeneralGroup,'cmEnvmonMIBCompliances':cmEnvmonMIBCompliances,'cmEnvmonCompliance':cmEnvmonCompliance})