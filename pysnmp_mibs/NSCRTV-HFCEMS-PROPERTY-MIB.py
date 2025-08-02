_J='currentAlarmOID'
_I='discreteAlarmValue'
_H='discreteParameterOID'
_G='analogParameterOID'
_F='OctetString'
_E='NSCRTV-HFCEMS-PROPERTY-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
propertyIdent,=mibBuilder.importSymbols('NSCRTV-ROOT','propertyIdent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_AnalogPropertyTable_Object=MibTable
analogPropertyTable=_AnalogPropertyTable_Object((1,3,6,1,4,1,17409,1,1,1))
if mibBuilder.loadTexts:analogPropertyTable.setStatus(_A)
_AnalogPropertyEntry_Object=MibTableRow
analogPropertyEntry=_AnalogPropertyEntry_Object((1,3,6,1,4,1,17409,1,1,1,1))
analogPropertyEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:analogPropertyEntry.setStatus(_A)
_AnalogParameterOID_Type=ObjectIdentifier
_AnalogParameterOID_Object=MibTableColumn
analogParameterOID=_AnalogParameterOID_Object((1,3,6,1,4,1,17409,1,1,1,1,1),_AnalogParameterOID_Type())
analogParameterOID.setMaxAccess(_B)
if mibBuilder.loadTexts:analogParameterOID.setStatus(_A)
class _AlarmEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_AlarmEnable_Type.__name__=_F
_AlarmEnable_Object=MibTableColumn
alarmEnable=_AlarmEnable_Object((1,3,6,1,4,1,17409,1,1,1,1,2),_AlarmEnable_Type())
alarmEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmEnable.setStatus(_A)
class _AnalogAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('aasNominal',1),('aasHIHI',2),('aasHI',3),('aasLO',4),('aasLOLO',5)))
_AnalogAlarmState_Type.__name__=_D
_AnalogAlarmState_Object=MibTableColumn
analogAlarmState=_AnalogAlarmState_Object((1,3,6,1,4,1,17409,1,1,1,1,3),_AnalogAlarmState_Type())
analogAlarmState.setMaxAccess(_B)
if mibBuilder.loadTexts:analogAlarmState.setStatus(_A)
_AnalogAlarmHIHI_Type=Integer32
_AnalogAlarmHIHI_Object=MibTableColumn
analogAlarmHIHI=_AnalogAlarmHIHI_Object((1,3,6,1,4,1,17409,1,1,1,1,4),_AnalogAlarmHIHI_Type())
analogAlarmHIHI.setMaxAccess(_C)
if mibBuilder.loadTexts:analogAlarmHIHI.setStatus(_A)
_AnalogAlarmHI_Type=Integer32
_AnalogAlarmHI_Object=MibTableColumn
analogAlarmHI=_AnalogAlarmHI_Object((1,3,6,1,4,1,17409,1,1,1,1,5),_AnalogAlarmHI_Type())
analogAlarmHI.setMaxAccess(_C)
if mibBuilder.loadTexts:analogAlarmHI.setStatus(_A)
_AnalogAlarmLO_Type=Integer32
_AnalogAlarmLO_Object=MibTableColumn
analogAlarmLO=_AnalogAlarmLO_Object((1,3,6,1,4,1,17409,1,1,1,1,6),_AnalogAlarmLO_Type())
analogAlarmLO.setMaxAccess(_C)
if mibBuilder.loadTexts:analogAlarmLO.setStatus(_A)
_AnalogAlarmLOLO_Type=Integer32
_AnalogAlarmLOLO_Object=MibTableColumn
analogAlarmLOLO=_AnalogAlarmLOLO_Object((1,3,6,1,4,1,17409,1,1,1,1,7),_AnalogAlarmLOLO_Type())
analogAlarmLOLO.setMaxAccess(_C)
if mibBuilder.loadTexts:analogAlarmLOLO.setStatus(_A)
_AnalogAlarmDeadband_Type=Integer32
_AnalogAlarmDeadband_Object=MibTableColumn
analogAlarmDeadband=_AnalogAlarmDeadband_Object((1,3,6,1,4,1,17409,1,1,1,1,8),_AnalogAlarmDeadband_Type())
analogAlarmDeadband.setMaxAccess(_C)
if mibBuilder.loadTexts:analogAlarmDeadband.setStatus(_A)
_DiscretePropertyTable_Object=MibTable
discretePropertyTable=_DiscretePropertyTable_Object((1,3,6,1,4,1,17409,1,1,2))
if mibBuilder.loadTexts:discretePropertyTable.setStatus(_A)
_DiscretePropertyEntry_Object=MibTableRow
discretePropertyEntry=_DiscretePropertyEntry_Object((1,3,6,1,4,1,17409,1,1,2,1))
discretePropertyEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:discretePropertyEntry.setStatus(_A)
_DiscreteParameterOID_Type=ObjectIdentifier
_DiscreteParameterOID_Object=MibTableColumn
discreteParameterOID=_DiscreteParameterOID_Object((1,3,6,1,4,1,17409,1,1,2,1,1),_DiscreteParameterOID_Type())
discreteParameterOID.setMaxAccess(_B)
if mibBuilder.loadTexts:discreteParameterOID.setStatus(_A)
_DiscreteAlarmValue_Type=Integer32
_DiscreteAlarmValue_Object=MibTableColumn
discreteAlarmValue=_DiscreteAlarmValue_Object((1,3,6,1,4,1,17409,1,1,2,1,2),_DiscreteAlarmValue_Type())
discreteAlarmValue.setMaxAccess(_B)
if mibBuilder.loadTexts:discreteAlarmValue.setStatus(_A)
class _DiscreteAlarmEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disable',1),('enableMajor',2),('enableMinor',3)))
_DiscreteAlarmEnable_Type.__name__=_D
_DiscreteAlarmEnable_Object=MibTableColumn
discreteAlarmEnable=_DiscreteAlarmEnable_Object((1,3,6,1,4,1,17409,1,1,2,1,3),_DiscreteAlarmEnable_Type())
discreteAlarmEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:discreteAlarmEnable.setStatus(_A)
class _DiscreteAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6,7)));namedValues=NamedValues(*(('dasNominal',1),('dasDiscreteMajor',6),('dasDiscreteMinor',7)))
_DiscreteAlarmState_Type.__name__=_D
_DiscreteAlarmState_Object=MibTableColumn
discreteAlarmState=_DiscreteAlarmState_Object((1,3,6,1,4,1,17409,1,1,2,1,4),_DiscreteAlarmState_Type())
discreteAlarmState.setMaxAccess(_B)
if mibBuilder.loadTexts:discreteAlarmState.setStatus(_A)
_CurrentAlarmTable_Object=MibTable
currentAlarmTable=_CurrentAlarmTable_Object((1,3,6,1,4,1,17409,1,1,3))
if mibBuilder.loadTexts:currentAlarmTable.setStatus(_A)
_CurrentAlarmEntry_Object=MibTableRow
currentAlarmEntry=_CurrentAlarmEntry_Object((1,3,6,1,4,1,17409,1,1,3,1))
currentAlarmEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:currentAlarmEntry.setStatus(_A)
_CurrentAlarmOID_Type=ObjectIdentifier
_CurrentAlarmOID_Object=MibTableColumn
currentAlarmOID=_CurrentAlarmOID_Object((1,3,6,1,4,1,17409,1,1,3,1,1),_CurrentAlarmOID_Type())
currentAlarmOID.setMaxAccess(_B)
if mibBuilder.loadTexts:currentAlarmOID.setStatus(_A)
class _CurrentAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7)));namedValues=NamedValues(*(('caasHIHI',2),('caasHI',3),('caasLO',4),('caasLOLO',5),('caasDiscreteMajor',6),('caasDiscreteMinor',7)))
_CurrentAlarmState_Type.__name__=_D
_CurrentAlarmState_Object=MibTableColumn
currentAlarmState=_CurrentAlarmState_Object((1,3,6,1,4,1,17409,1,1,3,1,2),_CurrentAlarmState_Type())
currentAlarmState.setMaxAccess(_B)
if mibBuilder.loadTexts:currentAlarmState.setStatus(_A)
_CurrentAlarmValue_Type=Integer32
_CurrentAlarmValue_Object=MibTableColumn
currentAlarmValue=_CurrentAlarmValue_Object((1,3,6,1,4,1,17409,1,1,3,1,3),_CurrentAlarmValue_Type())
currentAlarmValue.setMaxAccess(_B)
if mibBuilder.loadTexts:currentAlarmValue.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'analogPropertyTable':analogPropertyTable,'analogPropertyEntry':analogPropertyEntry,_G:analogParameterOID,'alarmEnable':alarmEnable,'analogAlarmState':analogAlarmState,'analogAlarmHIHI':analogAlarmHIHI,'analogAlarmHI':analogAlarmHI,'analogAlarmLO':analogAlarmLO,'analogAlarmLOLO':analogAlarmLOLO,'analogAlarmDeadband':analogAlarmDeadband,'discretePropertyTable':discretePropertyTable,'discretePropertyEntry':discretePropertyEntry,_H:discreteParameterOID,_I:discreteAlarmValue,'discreteAlarmEnable':discreteAlarmEnable,'discreteAlarmState':discreteAlarmState,'currentAlarmTable':currentAlarmTable,'currentAlarmEntry':currentAlarmEntry,_J:currentAlarmOID,'currentAlarmState':currentAlarmState,'currentAlarmValue':currentAlarmValue})