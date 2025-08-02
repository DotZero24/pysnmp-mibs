_O='sysLocation'
_N='sysDescr'
_M='Integer32'
_L='dpsTEXTRTUAnalogvalue'
_K='dpsTEXTRTUv2AState'
_J='dpsTEXTRTUv2APntDesc'
_I='dpsTEXTRTUv2APoint'
_H='dpsTEXTRTUv2ADisplay'
_G='dpsTEXTRTUv2Phone'
_F='dpsTEXTRTUv2DeviceType'
_E='dpsTEXTRTUv2DateTime'
_D='read-write'
_C='read-only'
_B='current'
_A='DPS-TEXT-RTU-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dpsAlarmControl,=mibBuilder.importSymbols('DPS-MIB-V38','dpsAlarmControl')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class AnalogThresholds(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('noAlarms',0),('minorUnder',1),('minorOver',2),('majorUnder',3),('majorOver',4),('notDetected',5)))
class RTUCAction(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('latch',1),('release',2),('momentary',3),('syncStanding',4),('syncAnalogs',5)))
_DpsTEXTRTUv2_ObjectIdentity=ObjectIdentity
dpsTEXTRTUv2=_DpsTEXTRTUv2_ObjectIdentity((1,3,6,1,4,1,2682,1,5))
_DpsTEXTRTUv2Ident_ObjectIdentity=ObjectIdentity
dpsTEXTRTUv2Ident=_DpsTEXTRTUv2Ident_ObjectIdentity((1,3,6,1,4,1,2682,1,5,1))
_DpsTEXTRTUv2DateTime_Type=DisplayString
_DpsTEXTRTUv2DateTime_Object=MibScalar
dpsTEXTRTUv2DateTime=_DpsTEXTRTUv2DateTime_Object((1,3,6,1,4,1,2682,1,5,1,1),_DpsTEXTRTUv2DateTime_Type())
dpsTEXTRTUv2DateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dpsTEXTRTUv2DateTime.setStatus(_B)
_DpsTEXTRTUv2DeviceType_Type=DisplayString
_DpsTEXTRTUv2DeviceType_Object=MibScalar
dpsTEXTRTUv2DeviceType=_DpsTEXTRTUv2DeviceType_Object((1,3,6,1,4,1,2682,1,5,1,2),_DpsTEXTRTUv2DeviceType_Type())
dpsTEXTRTUv2DeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsTEXTRTUv2DeviceType.setStatus(_B)
_DpsTEXTRTUv2Phone_Type=DisplayString
_DpsTEXTRTUv2Phone_Object=MibScalar
dpsTEXTRTUv2Phone=_DpsTEXTRTUv2Phone_Object((1,3,6,1,4,1,2682,1,5,1,3),_DpsTEXTRTUv2Phone_Type())
dpsTEXTRTUv2Phone.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsTEXTRTUv2Phone.setStatus(_B)
_DpsTEXTRTUv2AlarmGrid_ObjectIdentity=ObjectIdentity
dpsTEXTRTUv2AlarmGrid=_DpsTEXTRTUv2AlarmGrid_ObjectIdentity((1,3,6,1,4,1,2682,1,5,2))
_DpsTEXTRTUv2ADisplay_Type=Integer32
_DpsTEXTRTUv2ADisplay_Object=MibScalar
dpsTEXTRTUv2ADisplay=_DpsTEXTRTUv2ADisplay_Object((1,3,6,1,4,1,2682,1,5,2,1),_DpsTEXTRTUv2ADisplay_Type())
dpsTEXTRTUv2ADisplay.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsTEXTRTUv2ADisplay.setStatus(_B)
_DpsTEXTRTUv2APoint_Type=Integer32
_DpsTEXTRTUv2APoint_Object=MibScalar
dpsTEXTRTUv2APoint=_DpsTEXTRTUv2APoint_Object((1,3,6,1,4,1,2682,1,5,2,2),_DpsTEXTRTUv2APoint_Type())
dpsTEXTRTUv2APoint.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsTEXTRTUv2APoint.setStatus(_B)
_DpsTEXTRTUv2APntDesc_Type=DisplayString
_DpsTEXTRTUv2APntDesc_Object=MibScalar
dpsTEXTRTUv2APntDesc=_DpsTEXTRTUv2APntDesc_Object((1,3,6,1,4,1,2682,1,5,2,3),_DpsTEXTRTUv2APntDesc_Type())
dpsTEXTRTUv2APntDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsTEXTRTUv2APntDesc.setStatus(_B)
_DpsTEXTRTUv2AState_Type=DisplayString
_DpsTEXTRTUv2AState_Object=MibScalar
dpsTEXTRTUv2AState=_DpsTEXTRTUv2AState_Object((1,3,6,1,4,1,2682,1,5,2,4),_DpsTEXTRTUv2AState_Type())
dpsTEXTRTUv2AState.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsTEXTRTUv2AState.setStatus(_B)
_DpsTEXTRTUAnalogvalue_Type=DisplayString
_DpsTEXTRTUAnalogvalue_Object=MibScalar
dpsTEXTRTUAnalogvalue=_DpsTEXTRTUAnalogvalue_Object((1,3,6,1,4,1,2682,1,5,2,5),_DpsTEXTRTUAnalogvalue_Type())
dpsTEXTRTUAnalogvalue.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsTEXTRTUAnalogvalue.setStatus(_B)
_DpsTEXTRTUAnalogthresholds_Type=AnalogThresholds
_DpsTEXTRTUAnalogthresholds_Object=MibScalar
dpsTEXTRTUAnalogthresholds=_DpsTEXTRTUAnalogthresholds_Object((1,3,6,1,4,1,2682,1,5,2,6),_DpsTEXTRTUAnalogthresholds_Type())
dpsTEXTRTUAnalogthresholds.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsTEXTRTUAnalogthresholds.setStatus(_B)
_DpsTEXTRTUv2ControlGrid_ObjectIdentity=ObjectIdentity
dpsTEXTRTUv2ControlGrid=_DpsTEXTRTUv2ControlGrid_ObjectIdentity((1,3,6,1,4,1,2682,1,5,3))
_DpsTEXTRTUv2CDisplay_Type=Integer32
_DpsTEXTRTUv2CDisplay_Object=MibScalar
dpsTEXTRTUv2CDisplay=_DpsTEXTRTUv2CDisplay_Object((1,3,6,1,4,1,2682,1,5,3,1),_DpsTEXTRTUv2CDisplay_Type())
dpsTEXTRTUv2CDisplay.setMaxAccess(_D)
if mibBuilder.loadTexts:dpsTEXTRTUv2CDisplay.setStatus(_B)
class _DpsTEXTRTUv2CPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_DpsTEXTRTUv2CPoint_Type.__name__=_M
_DpsTEXTRTUv2CPoint_Object=MibScalar
dpsTEXTRTUv2CPoint=_DpsTEXTRTUv2CPoint_Object((1,3,6,1,4,1,2682,1,5,3,2),_DpsTEXTRTUv2CPoint_Type())
dpsTEXTRTUv2CPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:dpsTEXTRTUv2CPoint.setStatus(_B)
_DpsTEXTRTUv2CMOMTime_Type=Integer32
_DpsTEXTRTUv2CMOMTime_Object=MibScalar
dpsTEXTRTUv2CMOMTime=_DpsTEXTRTUv2CMOMTime_Object((1,3,6,1,4,1,2682,1,5,3,3),_DpsTEXTRTUv2CMOMTime_Type())
dpsTEXTRTUv2CMOMTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dpsTEXTRTUv2CMOMTime.setStatus(_B)
_DpsTEXTRTUv2CAction_Type=RTUCAction
_DpsTEXTRTUv2CAction_Object=MibScalar
dpsTEXTRTUv2CAction=_DpsTEXTRTUv2CAction_Object((1,3,6,1,4,1,2682,1,5,3,4),_DpsTEXTRTUv2CAction_Type())
dpsTEXTRTUv2CAction.setMaxAccess(_D)
if mibBuilder.loadTexts:dpsTEXTRTUv2CAction.setStatus(_B)
dpsTEXTRTUv2AlarmSet=NotificationType((1,3,6,1,4,1,2682,1,5,100))
dpsTEXTRTUv2AlarmSet.setObjects(*((_A,_N),(_A,_O),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:dpsTEXTRTUv2AlarmSet.setStatus(_B)
dpsTEXTRTUv2AlarmClear=NotificationType((1,3,6,1,4,1,2682,1,5,200))
dpsTEXTRTUv2AlarmClear.setObjects(*((_A,_N),(_A,_O),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:dpsTEXTRTUv2AlarmClear.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'AnalogThresholds':AnalogThresholds,'RTUCAction':RTUCAction,'dpsTEXTRTUv2':dpsTEXTRTUv2,'dpsTEXTRTUv2Ident':dpsTEXTRTUv2Ident,_E:dpsTEXTRTUv2DateTime,_F:dpsTEXTRTUv2DeviceType,_G:dpsTEXTRTUv2Phone,'dpsTEXTRTUv2AlarmGrid':dpsTEXTRTUv2AlarmGrid,_H:dpsTEXTRTUv2ADisplay,_I:dpsTEXTRTUv2APoint,_J:dpsTEXTRTUv2APntDesc,_K:dpsTEXTRTUv2AState,_L:dpsTEXTRTUAnalogvalue,'dpsTEXTRTUAnalogthresholds':dpsTEXTRTUAnalogthresholds,'dpsTEXTRTUv2ControlGrid':dpsTEXTRTUv2ControlGrid,'dpsTEXTRTUv2CDisplay':dpsTEXTRTUv2CDisplay,'dpsTEXTRTUv2CPoint':dpsTEXTRTUv2CPoint,'dpsTEXTRTUv2CMOMTime':dpsTEXTRTUv2CMOMTime,'dpsTEXTRTUv2CAction':dpsTEXTRTUv2CAction,'dpsTEXTRTUv2AlarmSet':dpsTEXTRTUv2AlarmSet,'dpsTEXTRTUv2AlarmClear':dpsTEXTRTUv2AlarmClear})