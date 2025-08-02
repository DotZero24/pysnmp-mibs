_P='linkUp'
_O='Unsigned32'
_N='ifSpeed-1000M'
_M='ifSpeed-100M'
_L='ifSpeed-10M'
_K='chassisIfStatusIndex'
_J='PLANET-MC1610MR-MIB'
_I='full'
_H='half'
_G='linkDown'
_F='enable'
_E='disable'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_O,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
planet=ModuleIdentity((1,3,6,1,4,1,10456))
if mibBuilder.loadTexts:planet.setRevisions(('2021-05-19 00:00','2008-11-20 00:00'))
_MediaConverter_ObjectIdentity=ObjectIdentity
mediaConverter=_MediaConverter_ObjectIdentity((1,3,6,1,4,1,10456,2))
_Chassis_ObjectIdentity=ObjectIdentity
chassis=_Chassis_ObjectIdentity((1,3,6,1,4,1,10456,2,625))
_ChassisIfNumber_Type=Integer32
_ChassisIfNumber_Object=MibScalar
chassisIfNumber=_ChassisIfNumber_Object((1,3,6,1,4,1,10456,2,625,1),_ChassisIfNumber_Type())
chassisIfNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisIfNumber.setStatus(_A)
_ChassisIfInfo_ObjectIdentity=ObjectIdentity
chassisIfInfo=_ChassisIfInfo_ObjectIdentity((1,3,6,1,4,1,10456,2,625,2))
_ChassisIfStatusTable_Object=MibTable
chassisIfStatusTable=_ChassisIfStatusTable_Object((1,3,6,1,4,1,10456,2,625,2,1))
if mibBuilder.loadTexts:chassisIfStatusTable.setStatus(_A)
_ChassisIfStatusEntry_Object=MibTableRow
chassisIfStatusEntry=_ChassisIfStatusEntry_Object((1,3,6,1,4,1,10456,2,625,2,1,1))
chassisIfStatusEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:chassisIfStatusEntry.setStatus(_A)
class _ChassisIfStatusIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_ChassisIfStatusIndex_Type.__name__=_O
_ChassisIfStatusIndex_Object=MibTableColumn
chassisIfStatusIndex=_ChassisIfStatusIndex_Object((1,3,6,1,4,1,10456,2,625,2,1,1,1),_ChassisIfStatusIndex_Type())
chassisIfStatusIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisIfStatusIndex.setStatus(_A)
_ChassisIfStatusName_Type=OctetString
_ChassisIfStatusName_Object=MibTableColumn
chassisIfStatusName=_ChassisIfStatusName_Object((1,3,6,1,4,1,10456,2,625,2,1,1,2),_ChassisIfStatusName_Type())
chassisIfStatusName.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisIfStatusName.setStatus(_A)
class _ChassisIfStatusTPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_P,1)))
_ChassisIfStatusTPStatus_Type.__name__=_B
_ChassisIfStatusTPStatus_Object=MibTableColumn
chassisIfStatusTPStatus=_ChassisIfStatusTPStatus_Object((1,3,6,1,4,1,10456,2,625,2,1,1,3),_ChassisIfStatusTPStatus_Type())
chassisIfStatusTPStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisIfStatusTPStatus.setStatus(_A)
class _ChassisIfStatusTPSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_L,1),(_M,2),(_N,3)))
_ChassisIfStatusTPSpeed_Type.__name__=_B
_ChassisIfStatusTPSpeed_Object=MibTableColumn
chassisIfStatusTPSpeed=_ChassisIfStatusTPSpeed_Object((1,3,6,1,4,1,10456,2,625,2,1,1,4),_ChassisIfStatusTPSpeed_Type())
chassisIfStatusTPSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisIfStatusTPSpeed.setStatus(_A)
class _ChassisIfStatusTPDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2)))
_ChassisIfStatusTPDuplex_Type.__name__=_B
_ChassisIfStatusTPDuplex_Object=MibTableColumn
chassisIfStatusTPDuplex=_ChassisIfStatusTPDuplex_Object((1,3,6,1,4,1,10456,2,625,2,1,1,5),_ChassisIfStatusTPDuplex_Type())
chassisIfStatusTPDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisIfStatusTPDuplex.setStatus(_A)
class _ChassisIfStatusFXStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_P,1)))
_ChassisIfStatusFXStatus_Type.__name__=_B
_ChassisIfStatusFXStatus_Object=MibTableColumn
chassisIfStatusFXStatus=_ChassisIfStatusFXStatus_Object((1,3,6,1,4,1,10456,2,625,2,1,1,6),_ChassisIfStatusFXStatus_Type())
chassisIfStatusFXStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisIfStatusFXStatus.setStatus(_A)
class _ChassisIfStatusFXSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_L,1),(_M,2),(_N,3)))
_ChassisIfStatusFXSpeed_Type.__name__=_B
_ChassisIfStatusFXSpeed_Object=MibTableColumn
chassisIfStatusFXSpeed=_ChassisIfStatusFXSpeed_Object((1,3,6,1,4,1,10456,2,625,2,1,1,7),_ChassisIfStatusFXSpeed_Type())
chassisIfStatusFXSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisIfStatusFXSpeed.setStatus(_A)
class _ChassisIfStatusFXDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2)))
_ChassisIfStatusFXDuplex_Type.__name__=_B
_ChassisIfStatusFXDuplex_Object=MibTableColumn
chassisIfStatusFXDuplex=_ChassisIfStatusFXDuplex_Object((1,3,6,1,4,1,10456,2,625,2,1,1,8),_ChassisIfStatusFXDuplex_Type())
chassisIfStatusFXDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisIfStatusFXDuplex.setStatus(_A)
_ChassisIfConfTable_Object=MibTable
chassisIfConfTable=_ChassisIfConfTable_Object((1,3,6,1,4,1,10456,2,625,2,2))
if mibBuilder.loadTexts:chassisIfConfTable.setStatus(_A)
_ChassisIfConfEntry_Object=MibTableRow
chassisIfConfEntry=_ChassisIfConfEntry_Object((1,3,6,1,4,1,10456,2,625,2,2,1))
chassisIfConfEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:chassisIfConfEntry.setStatus(_A)
class _ChassisIfConfAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ChassisIfConfAdmin_Type.__name__=_B
_ChassisIfConfAdmin_Object=MibTableColumn
chassisIfConfAdmin=_ChassisIfConfAdmin_Object((1,3,6,1,4,1,10456,2,625,2,2,1,1),_ChassisIfConfAdmin_Type())
chassisIfConfAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisIfConfAdmin.setStatus(_A)
class _ChassisIfConfTPANmode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_ChassisIfConfTPANmode_Type.__name__=_B
_ChassisIfConfTPANmode_Object=MibTableColumn
chassisIfConfTPANmode=_ChassisIfConfTPANmode_Object((1,3,6,1,4,1,10456,2,625,2,2,1,2),_ChassisIfConfTPANmode_Type())
chassisIfConfTPANmode.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisIfConfTPANmode.setStatus(_A)
class _ChassisIfConfTPSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_M,1),(_N,2)))
_ChassisIfConfTPSpeed_Type.__name__=_B
_ChassisIfConfTPSpeed_Object=MibTableColumn
chassisIfConfTPSpeed=_ChassisIfConfTPSpeed_Object((1,3,6,1,4,1,10456,2,625,2,2,1,3),_ChassisIfConfTPSpeed_Type())
chassisIfConfTPSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisIfConfTPSpeed.setStatus(_A)
class _ChassisIfConfTPDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_ChassisIfConfTPDuplex_Type.__name__=_B
_ChassisIfConfTPDuplex_Object=MibTableColumn
chassisIfConfTPDuplex=_ChassisIfConfTPDuplex_Object((1,3,6,1,4,1,10456,2,625,2,2,1,4),_ChassisIfConfTPDuplex_Type())
chassisIfConfTPDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisIfConfTPDuplex.setStatus(_A)
class _ChassisIfConfTPFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_ChassisIfConfTPFlowControl_Type.__name__=_B
_ChassisIfConfTPFlowControl_Object=MibTableColumn
chassisIfConfTPFlowControl=_ChassisIfConfTPFlowControl_Object((1,3,6,1,4,1,10456,2,625,2,2,1,5),_ChassisIfConfTPFlowControl_Type())
chassisIfConfTPFlowControl.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisIfConfTPFlowControl.setStatus(_A)
class _ChassisIfConfLLCF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_ChassisIfConfLLCF_Type.__name__=_B
_ChassisIfConfLLCF_Object=MibTableColumn
chassisIfConfLLCF=_ChassisIfConfLLCF_Object((1,3,6,1,4,1,10456,2,625,2,2,1,6),_ChassisIfConfLLCF_Type())
chassisIfConfLLCF.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisIfConfLLCF.setStatus(_A)
class _ChassisIfConfFXDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_ChassisIfConfFXDuplex_Type.__name__=_B
_ChassisIfConfFXDuplex_Object=MibTableColumn
chassisIfConfFXDuplex=_ChassisIfConfFXDuplex_Object((1,3,6,1,4,1,10456,2,625,2,2,1,7),_ChassisIfConfFXDuplex_Type())
chassisIfConfFXDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisIfConfFXDuplex.setStatus(_A)
class _ChassisIfConfFXLLR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ChassisIfConfFXLLR_Type.__name__=_B
_ChassisIfConfFXLLR_Object=MibTableColumn
chassisIfConfFXLLR=_ChassisIfConfFXLLR_Object((1,3,6,1,4,1,10456,2,625,2,2,1,8),_ChassisIfConfFXLLR_Type())
chassisIfConfFXLLR.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisIfConfFXLLR.setStatus(_A)
class _ChassisIfConfFXANbyPass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ChassisIfConfFXANbyPass_Type.__name__=_B
_ChassisIfConfFXANbyPass_Object=MibTableColumn
chassisIfConfFXANbyPass=_ChassisIfConfFXANbyPass_Object((1,3,6,1,4,1,10456,2,625,2,2,1,9),_ChassisIfConfFXANbyPass_Type())
chassisIfConfFXANbyPass.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisIfConfFXANbyPass.setStatus(_A)
_ChassisTemperature_Type=OctetString
_ChassisTemperature_Object=MibScalar
chassisTemperature=_ChassisTemperature_Object((1,3,6,1,4,1,10456,2,625,3),_ChassisTemperature_Type())
chassisTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisTemperature.setStatus(_A)
class _ChassisPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),('on',1),('fail',2)))
_ChassisPowerStatus_Type.__name__=_B
_ChassisPowerStatus_Object=MibScalar
chassisPowerStatus=_ChassisPowerStatus_Object((1,3,6,1,4,1,10456,2,625,4),_ChassisPowerStatus_Type())
chassisPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisPowerStatus.setStatus(_A)
class _ChassisFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),('on',1),('fail',2)))
_ChassisFanStatus_Type.__name__=_B
_ChassisFanStatus_Object=MibScalar
chassisFanStatus=_ChassisFanStatus_Object((1,3,6,1,4,1,10456,2,625,5),_ChassisFanStatus_Type())
chassisFanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisFanStatus.setStatus(_A)
class _ChassisRedundant_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ChassisRedundant_Type.__name__=_B
_ChassisRedundant_Object=MibScalar
chassisRedundant=_ChassisRedundant_Object((1,3,6,1,4,1,10456,2,625,6),_ChassisRedundant_Type())
chassisRedundant.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisRedundant.setStatus(_A)
_ChassisSlotLocation_Type=OctetString
_ChassisSlotLocation_Object=MibScalar
chassisSlotLocation=_ChassisSlotLocation_Object((1,3,6,1,4,1,10456,2,625,7),_ChassisSlotLocation_Type())
chassisSlotLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisSlotLocation.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'planet':planet,'mediaConverter':mediaConverter,'chassis':chassis,'chassisIfNumber':chassisIfNumber,'chassisIfInfo':chassisIfInfo,'chassisIfStatusTable':chassisIfStatusTable,'chassisIfStatusEntry':chassisIfStatusEntry,_K:chassisIfStatusIndex,'chassisIfStatusName':chassisIfStatusName,'chassisIfStatusTPStatus':chassisIfStatusTPStatus,'chassisIfStatusTPSpeed':chassisIfStatusTPSpeed,'chassisIfStatusTPDuplex':chassisIfStatusTPDuplex,'chassisIfStatusFXStatus':chassisIfStatusFXStatus,'chassisIfStatusFXSpeed':chassisIfStatusFXSpeed,'chassisIfStatusFXDuplex':chassisIfStatusFXDuplex,'chassisIfConfTable':chassisIfConfTable,'chassisIfConfEntry':chassisIfConfEntry,'chassisIfConfAdmin':chassisIfConfAdmin,'chassisIfConfTPANmode':chassisIfConfTPANmode,'chassisIfConfTPSpeed':chassisIfConfTPSpeed,'chassisIfConfTPDuplex':chassisIfConfTPDuplex,'chassisIfConfTPFlowControl':chassisIfConfTPFlowControl,'chassisIfConfLLCF':chassisIfConfLLCF,'chassisIfConfFXDuplex':chassisIfConfFXDuplex,'chassisIfConfFXLLR':chassisIfConfFXLLR,'chassisIfConfFXANbyPass':chassisIfConfFXANbyPass,'chassisTemperature':chassisTemperature,'chassisPowerStatus':chassisPowerStatus,'chassisFanStatus':chassisFanStatus,'chassisRedundant':chassisRedundant,'chassisSlotLocation':chassisSlotLocation})