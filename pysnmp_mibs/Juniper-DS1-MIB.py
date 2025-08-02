_w='juniDs1Group5'
_v='juniDs1Group4'
_u='juniDs1Group3'
_t='juniDs1Group2'
_s='juniDs1Group'
_r='juniDsx1FarEndCarrier'
_q='juniDsx1FarEndGeneratorNumber'
_p='juniDsx1FarEndPortNumber'
_o='juniDsx1FarEndFacilityIDCode'
_n='juniDsx1FarEndUnitCode'
_m='juniDsx1FarEndFrameIDCode'
_l='juniDsx1FarEndLocationIDCode'
_k='juniDsx1FarEndEquipCode'
_j='juniDsx1FdlTransmit'
_i='juniDsx1FarEndLineIndex'
_h='notSupported'
_g='ifIndex'
_f='IF-MIB'
_e='juniDsx1FdlGenerator'
_d='juniDsx1FdlPort'
_c='juniDsx1FdlPfi'
_b='juniDsx1FdlUnit'
_a='juniDsx1FdlFic'
_Z='juniDsx1FdlLic'
_Y='juniDsx1FdlEic'
_X='juniDsx1FdlCarrier'
_W='juniDsx1RemoteLoopback'
_V='juniDsx1YellowAlarm'
_U='juniDsx1SendCode'
_T='enabled'
_S='disabled'
_R='juniDs1NextIfIndex'
_Q='juniDsx1RowStatus'
_P='juniDsx1LowerIfIndex'
_O='juniDsx1LineLength'
_N='juniDsx1LineAttenuation'
_M='juniDsx1LineBuildOutType'
_L='juniDsx1LineBuildOutCapabilities'
_K='juniDsx1Mode'
_J='juniDsx1Capabilities'
_I='juniDsx1Ds1ChannelNumber'
_H='juniDsx1TimeSlotMap'
_G='obsolete'
_F='read-only'
_E='Integer32'
_D='DisplayString'
_C='read-create'
_B='current'
_A='Juniper-DS1-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_f,'InterfaceIndexOrZero',_g)
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniNextIfIndex,JuniTimeSlotMap=mibBuilder.importSymbols('Juniper-TC','JuniNextIfIndex','JuniTimeSlotMap')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
juniDs1MIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,5))
if mibBuilder.loadTexts:juniDs1MIB.setRevisions(('2003-02-10 15:07','2002-09-12 16:59','2002-05-13 16:01','2001-07-31 18:25','2001-04-04 18:05','1999-06-17 00:00','1998-11-13 00:00'))
_JuniDs1Objects_ObjectIdentity=ObjectIdentity
juniDs1Objects=_JuniDs1Objects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,5,1))
_JuniDsx1ConfigTable_Object=MibTable
juniDsx1ConfigTable=_JuniDsx1ConfigTable_Object((1,3,6,1,4,1,4874,2,2,5,1,1))
if mibBuilder.loadTexts:juniDsx1ConfigTable.setStatus(_B)
_JuniDsx1ConfigEntry_Object=MibTableRow
juniDsx1ConfigEntry=_JuniDsx1ConfigEntry_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1))
juniDsx1ConfigEntry.setIndexNames((0,_f,_g))
if mibBuilder.loadTexts:juniDsx1ConfigEntry.setStatus(_B)
_JuniDsx1TimeSlotMap_Type=JuniTimeSlotMap
_JuniDsx1TimeSlotMap_Object=MibTableColumn
juniDsx1TimeSlotMap=_JuniDsx1TimeSlotMap_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,1),_JuniDsx1TimeSlotMap_Type())
juniDsx1TimeSlotMap.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDsx1TimeSlotMap.setStatus(_B)
class _JuniDsx1Ds1ChannelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,28))
_JuniDsx1Ds1ChannelNumber_Type.__name__=_E
_JuniDsx1Ds1ChannelNumber_Object=MibTableColumn
juniDsx1Ds1ChannelNumber=_JuniDsx1Ds1ChannelNumber_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,2),_JuniDsx1Ds1ChannelNumber_Type())
juniDsx1Ds1ChannelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1Ds1ChannelNumber.setStatus(_B)
class _JuniDsx1Capabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_JuniDsx1Capabilities_Type.__name__=_E
_JuniDsx1Capabilities_Object=MibTableColumn
juniDsx1Capabilities=_JuniDsx1Capabilities_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,3),_JuniDsx1Capabilities_Type())
juniDsx1Capabilities.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDsx1Capabilities.setStatus(_B)
class _JuniDsx1Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t1',1),('e1',2),('j1',3)))
_JuniDsx1Mode_Type.__name__=_E
_JuniDsx1Mode_Object=MibTableColumn
juniDsx1Mode=_JuniDsx1Mode_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,4),_JuniDsx1Mode_Type())
juniDsx1Mode.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1Mode.setStatus(_B)
class _JuniDsx1LineBuildOutCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_JuniDsx1LineBuildOutCapabilities_Type.__name__=_E
_JuniDsx1LineBuildOutCapabilities_Object=MibTableColumn
juniDsx1LineBuildOutCapabilities=_JuniDsx1LineBuildOutCapabilities_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,5),_JuniDsx1LineBuildOutCapabilities_Type())
juniDsx1LineBuildOutCapabilities.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDsx1LineBuildOutCapabilities.setStatus(_B)
class _JuniDsx1LineBuildOutType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('shortHaul',1),('longHaul',2),(_h,3)))
_JuniDsx1LineBuildOutType_Type.__name__=_E
_JuniDsx1LineBuildOutType_Object=MibTableColumn
juniDsx1LineBuildOutType=_JuniDsx1LineBuildOutType_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,6),_JuniDsx1LineBuildOutType_Type())
juniDsx1LineBuildOutType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1LineBuildOutType.setStatus(_B)
class _JuniDsx1LineAttenuation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('db0',1),('dbMinus7Point5',2),('dbMinus15',3),('dbMinus22Point5',4),(_h,5)))
_JuniDsx1LineAttenuation_Type.__name__=_E
_JuniDsx1LineAttenuation_Object=MibTableColumn
juniDsx1LineAttenuation=_JuniDsx1LineAttenuation_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,7),_JuniDsx1LineAttenuation_Type())
juniDsx1LineAttenuation.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1LineAttenuation.setStatus(_B)
class _JuniDsx1LineLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64000))
_JuniDsx1LineLength_Type.__name__=_E
_JuniDsx1LineLength_Object=MibTableColumn
juniDsx1LineLength=_JuniDsx1LineLength_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,8),_JuniDsx1LineLength_Type())
juniDsx1LineLength.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1LineLength.setStatus(_B)
if mibBuilder.loadTexts:juniDsx1LineLength.setUnits('meters')
_JuniDsx1LowerIfIndex_Type=InterfaceIndexOrZero
_JuniDsx1LowerIfIndex_Object=MibTableColumn
juniDsx1LowerIfIndex=_JuniDsx1LowerIfIndex_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,9),_JuniDsx1LowerIfIndex_Type())
juniDsx1LowerIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1LowerIfIndex.setStatus(_B)
_JuniDsx1RowStatus_Type=RowStatus
_JuniDsx1RowStatus_Object=MibTableColumn
juniDsx1RowStatus=_JuniDsx1RowStatus_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,10),_JuniDsx1RowStatus_Type())
juniDsx1RowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1RowStatus.setStatus(_B)
class _JuniDsx1SendCode_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*(('sendInbandLineCode',1),('sendBellcoreLineCode',2),('sendBellcoreInbandLineCode',3),('sendQRSPattern',4),('sendAllZerosPattern',5),('sendAllOnesPattern',6),('sendAltZeroOnePattern',7),('sendTwo11Pattern',8),('sendTwo15Pattern',9),('sendTwo20Pattern',10),('sendTwo23Pattern',11),('sendUnfrQRSPattern',12),('sendUnfrAllZerosPattern',13),('sendUnfrAllOnesPattern',14),('sendUnfrAltZeroOnePattern',15),('sendUnfrTwo11Pattern',16),('sendUnfrTwo15Pattern',17),('sendUnfrTwo20Pattern',18),('sendUnfrTwo23Pattern',19),('otherPattern',20)))
_JuniDsx1SendCode_Type.__name__=_E
_JuniDsx1SendCode_Object=MibTableColumn
juniDsx1SendCode=_JuniDsx1SendCode_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,11),_JuniDsx1SendCode_Type())
juniDsx1SendCode.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1SendCode.setStatus(_B)
class _JuniDsx1YellowAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('generate',1),('detect',2),('generateAndDetect',3),('none',4)))
_JuniDsx1YellowAlarm_Type.__name__=_E
_JuniDsx1YellowAlarm_Object=MibTableColumn
juniDsx1YellowAlarm=_JuniDsx1YellowAlarm_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,12),_JuniDsx1YellowAlarm_Type())
juniDsx1YellowAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1YellowAlarm.setStatus(_B)
class _JuniDsx1RemoteLoopback_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_JuniDsx1RemoteLoopback_Type.__name__=_E
_JuniDsx1RemoteLoopback_Object=MibTableColumn
juniDsx1RemoteLoopback=_JuniDsx1RemoteLoopback_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,13),_JuniDsx1RemoteLoopback_Type())
juniDsx1RemoteLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1RemoteLoopback.setStatus(_B)
class _JuniDsx1FdlCarrier_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_JuniDsx1FdlCarrier_Type.__name__=_E
_JuniDsx1FdlCarrier_Object=MibTableColumn
juniDsx1FdlCarrier=_JuniDsx1FdlCarrier_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,14),_JuniDsx1FdlCarrier_Type())
juniDsx1FdlCarrier.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1FdlCarrier.setStatus(_B)
class _JuniDsx1FdlEic_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_JuniDsx1FdlEic_Type.__name__=_D
_JuniDsx1FdlEic_Object=MibTableColumn
juniDsx1FdlEic=_JuniDsx1FdlEic_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,15),_JuniDsx1FdlEic_Type())
juniDsx1FdlEic.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1FdlEic.setStatus(_B)
class _JuniDsx1FdlLic_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_JuniDsx1FdlLic_Type.__name__=_D
_JuniDsx1FdlLic_Object=MibTableColumn
juniDsx1FdlLic=_JuniDsx1FdlLic_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,16),_JuniDsx1FdlLic_Type())
juniDsx1FdlLic.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1FdlLic.setStatus(_B)
class _JuniDsx1FdlFic_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_JuniDsx1FdlFic_Type.__name__=_D
_JuniDsx1FdlFic_Object=MibTableColumn
juniDsx1FdlFic=_JuniDsx1FdlFic_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,17),_JuniDsx1FdlFic_Type())
juniDsx1FdlFic.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1FdlFic.setStatus(_B)
class _JuniDsx1FdlUnit_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_JuniDsx1FdlUnit_Type.__name__=_D
_JuniDsx1FdlUnit_Object=MibTableColumn
juniDsx1FdlUnit=_JuniDsx1FdlUnit_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,18),_JuniDsx1FdlUnit_Type())
juniDsx1FdlUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1FdlUnit.setStatus(_B)
class _JuniDsx1FdlPfi_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_JuniDsx1FdlPfi_Type.__name__=_D
_JuniDsx1FdlPfi_Object=MibTableColumn
juniDsx1FdlPfi=_JuniDsx1FdlPfi_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,19),_JuniDsx1FdlPfi_Type())
juniDsx1FdlPfi.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1FdlPfi.setStatus(_B)
class _JuniDsx1FdlPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_JuniDsx1FdlPort_Type.__name__=_D
_JuniDsx1FdlPort_Object=MibTableColumn
juniDsx1FdlPort=_JuniDsx1FdlPort_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,20),_JuniDsx1FdlPort_Type())
juniDsx1FdlPort.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1FdlPort.setStatus(_B)
class _JuniDsx1FdlGenerator_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_JuniDsx1FdlGenerator_Type.__name__=_D
_JuniDsx1FdlGenerator_Object=MibTableColumn
juniDsx1FdlGenerator=_JuniDsx1FdlGenerator_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,21),_JuniDsx1FdlGenerator_Type())
juniDsx1FdlGenerator.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1FdlGenerator.setStatus(_B)
class _JuniDsx1FdlTransmit_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('path',0),('idlesignal',1),('testsignal',2)))
_JuniDsx1FdlTransmit_Type.__name__='Bits'
_JuniDsx1FdlTransmit_Object=MibTableColumn
juniDsx1FdlTransmit=_JuniDsx1FdlTransmit_Object((1,3,6,1,4,1,4874,2,2,5,1,1,1,22),_JuniDsx1FdlTransmit_Type())
juniDsx1FdlTransmit.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx1FdlTransmit.setStatus(_B)
_JuniDs1NextIfIndex_Type=JuniNextIfIndex
_JuniDs1NextIfIndex_Object=MibScalar
juniDs1NextIfIndex=_JuniDs1NextIfIndex_Object((1,3,6,1,4,1,4874,2,2,5,1,2),_JuniDs1NextIfIndex_Type())
juniDs1NextIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDs1NextIfIndex.setStatus(_B)
_JuniDsx1FarEndConfigTable_Object=MibTable
juniDsx1FarEndConfigTable=_JuniDsx1FarEndConfigTable_Object((1,3,6,1,4,1,4874,2,2,5,1,3))
if mibBuilder.loadTexts:juniDsx1FarEndConfigTable.setStatus(_B)
_JuniDsx1FarEndConfigEntry_Object=MibTableRow
juniDsx1FarEndConfigEntry=_JuniDsx1FarEndConfigEntry_Object((1,3,6,1,4,1,4874,2,2,5,1,3,1))
juniDsx1FarEndConfigEntry.setIndexNames((0,_A,_i))
if mibBuilder.loadTexts:juniDsx1FarEndConfigEntry.setStatus(_B)
class _JuniDsx1FarEndLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_JuniDsx1FarEndLineIndex_Type.__name__=_E
_JuniDsx1FarEndLineIndex_Object=MibTableColumn
juniDsx1FarEndLineIndex=_JuniDsx1FarEndLineIndex_Object((1,3,6,1,4,1,4874,2,2,5,1,3,1,1),_JuniDsx1FarEndLineIndex_Type())
juniDsx1FarEndLineIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:juniDsx1FarEndLineIndex.setStatus(_B)
class _JuniDsx1FarEndEquipCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_JuniDsx1FarEndEquipCode_Type.__name__=_D
_JuniDsx1FarEndEquipCode_Object=MibTableColumn
juniDsx1FarEndEquipCode=_JuniDsx1FarEndEquipCode_Object((1,3,6,1,4,1,4874,2,2,5,1,3,1,2),_JuniDsx1FarEndEquipCode_Type())
juniDsx1FarEndEquipCode.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDsx1FarEndEquipCode.setStatus(_B)
class _JuniDsx1FarEndLocationIDCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_JuniDsx1FarEndLocationIDCode_Type.__name__=_D
_JuniDsx1FarEndLocationIDCode_Object=MibTableColumn
juniDsx1FarEndLocationIDCode=_JuniDsx1FarEndLocationIDCode_Object((1,3,6,1,4,1,4874,2,2,5,1,3,1,3),_JuniDsx1FarEndLocationIDCode_Type())
juniDsx1FarEndLocationIDCode.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDsx1FarEndLocationIDCode.setStatus(_B)
class _JuniDsx1FarEndFrameIDCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_JuniDsx1FarEndFrameIDCode_Type.__name__=_D
_JuniDsx1FarEndFrameIDCode_Object=MibTableColumn
juniDsx1FarEndFrameIDCode=_JuniDsx1FarEndFrameIDCode_Object((1,3,6,1,4,1,4874,2,2,5,1,3,1,4),_JuniDsx1FarEndFrameIDCode_Type())
juniDsx1FarEndFrameIDCode.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDsx1FarEndFrameIDCode.setStatus(_B)
class _JuniDsx1FarEndUnitCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_JuniDsx1FarEndUnitCode_Type.__name__=_D
_JuniDsx1FarEndUnitCode_Object=MibTableColumn
juniDsx1FarEndUnitCode=_JuniDsx1FarEndUnitCode_Object((1,3,6,1,4,1,4874,2,2,5,1,3,1,5),_JuniDsx1FarEndUnitCode_Type())
juniDsx1FarEndUnitCode.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDsx1FarEndUnitCode.setStatus(_B)
class _JuniDsx1FarEndFacilityIDCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_JuniDsx1FarEndFacilityIDCode_Type.__name__=_D
_JuniDsx1FarEndFacilityIDCode_Object=MibTableColumn
juniDsx1FarEndFacilityIDCode=_JuniDsx1FarEndFacilityIDCode_Object((1,3,6,1,4,1,4874,2,2,5,1,3,1,6),_JuniDsx1FarEndFacilityIDCode_Type())
juniDsx1FarEndFacilityIDCode.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDsx1FarEndFacilityIDCode.setStatus(_B)
class _JuniDsx1FarEndPortNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_JuniDsx1FarEndPortNumber_Type.__name__=_D
_JuniDsx1FarEndPortNumber_Object=MibTableColumn
juniDsx1FarEndPortNumber=_JuniDsx1FarEndPortNumber_Object((1,3,6,1,4,1,4874,2,2,5,1,3,1,7),_JuniDsx1FarEndPortNumber_Type())
juniDsx1FarEndPortNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDsx1FarEndPortNumber.setStatus(_B)
class _JuniDsx1FarEndGeneratorNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_JuniDsx1FarEndGeneratorNumber_Type.__name__=_D
_JuniDsx1FarEndGeneratorNumber_Object=MibTableColumn
juniDsx1FarEndGeneratorNumber=_JuniDsx1FarEndGeneratorNumber_Object((1,3,6,1,4,1,4874,2,2,5,1,3,1,8),_JuniDsx1FarEndGeneratorNumber_Type())
juniDsx1FarEndGeneratorNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDsx1FarEndGeneratorNumber.setStatus(_B)
class _JuniDsx1FarEndCarrier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_JuniDsx1FarEndCarrier_Type.__name__=_E
_JuniDsx1FarEndCarrier_Object=MibTableColumn
juniDsx1FarEndCarrier=_JuniDsx1FarEndCarrier_Object((1,3,6,1,4,1,4874,2,2,5,1,3,1,9),_JuniDsx1FarEndCarrier_Type())
juniDsx1FarEndCarrier.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDsx1FarEndCarrier.setStatus(_B)
_JuniDs1Conformance_ObjectIdentity=ObjectIdentity
juniDs1Conformance=_JuniDs1Conformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,5,4))
_JuniDs1Compliances_ObjectIdentity=ObjectIdentity
juniDs1Compliances=_JuniDs1Compliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,5,4,1))
_JuniDs1Groups_ObjectIdentity=ObjectIdentity
juniDs1Groups=_JuniDs1Groups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,5,4,2))
juniDs1Group=ObjectGroup((1,3,6,1,4,1,4874,2,2,5,4,2,1))
juniDs1Group.setObjects(*((_A,_H),(_A,_I)))
if mibBuilder.loadTexts:juniDs1Group.setStatus(_G)
juniDs1Group2=ObjectGroup((1,3,6,1,4,1,4874,2,2,5,4,2,2))
juniDs1Group2.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:juniDs1Group2.setStatus(_G)
juniDs1Group3=ObjectGroup((1,3,6,1,4,1,4874,2,2,5,4,2,3))
juniDs1Group3.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:juniDs1Group3.setStatus(_G)
juniDs1Group4=ObjectGroup((1,3,6,1,4,1,4874,2,2,5,4,2,4))
juniDs1Group4.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_R)))
if mibBuilder.loadTexts:juniDs1Group4.setStatus(_G)
juniDs1Group5=ObjectGroup((1,3,6,1,4,1,4874,2,2,5,4,2,5))
juniDs1Group5.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_R)))
if mibBuilder.loadTexts:juniDs1Group5.setStatus(_B)
juniDs1Compliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,5,4,1,1))
juniDs1Compliance.setObjects((_A,_s))
if mibBuilder.loadTexts:juniDs1Compliance.setStatus(_G)
juniDs1Compliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,5,4,1,2))
juniDs1Compliance2.setObjects((_A,_t))
if mibBuilder.loadTexts:juniDs1Compliance2.setStatus(_G)
juniDs1Compliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,5,4,1,3))
juniDs1Compliance3.setObjects((_A,_u))
if mibBuilder.loadTexts:juniDs1Compliance3.setStatus(_G)
juniDs1Compliance4=ModuleCompliance((1,3,6,1,4,1,4874,2,2,5,4,1,4))
juniDs1Compliance4.setObjects((_A,_v))
if mibBuilder.loadTexts:juniDs1Compliance4.setStatus(_G)
juniDs1Compliance5=ModuleCompliance((1,3,6,1,4,1,4874,2,2,5,4,1,5))
juniDs1Compliance5.setObjects((_A,_w))
if mibBuilder.loadTexts:juniDs1Compliance5.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniDs1MIB':juniDs1MIB,'juniDs1Objects':juniDs1Objects,'juniDsx1ConfigTable':juniDsx1ConfigTable,'juniDsx1ConfigEntry':juniDsx1ConfigEntry,_H:juniDsx1TimeSlotMap,_I:juniDsx1Ds1ChannelNumber,_J:juniDsx1Capabilities,_K:juniDsx1Mode,_L:juniDsx1LineBuildOutCapabilities,_M:juniDsx1LineBuildOutType,_N:juniDsx1LineAttenuation,_O:juniDsx1LineLength,_P:juniDsx1LowerIfIndex,_Q:juniDsx1RowStatus,_U:juniDsx1SendCode,_V:juniDsx1YellowAlarm,_W:juniDsx1RemoteLoopback,_X:juniDsx1FdlCarrier,_Y:juniDsx1FdlEic,_Z:juniDsx1FdlLic,_a:juniDsx1FdlFic,_b:juniDsx1FdlUnit,_c:juniDsx1FdlPfi,_d:juniDsx1FdlPort,_e:juniDsx1FdlGenerator,_j:juniDsx1FdlTransmit,_R:juniDs1NextIfIndex,'juniDsx1FarEndConfigTable':juniDsx1FarEndConfigTable,'juniDsx1FarEndConfigEntry':juniDsx1FarEndConfigEntry,_i:juniDsx1FarEndLineIndex,_k:juniDsx1FarEndEquipCode,_l:juniDsx1FarEndLocationIDCode,_m:juniDsx1FarEndFrameIDCode,_n:juniDsx1FarEndUnitCode,_o:juniDsx1FarEndFacilityIDCode,_p:juniDsx1FarEndPortNumber,_q:juniDsx1FarEndGeneratorNumber,_r:juniDsx1FarEndCarrier,'juniDs1Conformance':juniDs1Conformance,'juniDs1Compliances':juniDs1Compliances,'juniDs1Compliance':juniDs1Compliance,'juniDs1Compliance2':juniDs1Compliance2,'juniDs1Compliance3':juniDs1Compliance3,'juniDs1Compliance4':juniDs1Compliance4,'juniDs1Compliance5':juniDs1Compliance5,'juniDs1Groups':juniDs1Groups,_s:juniDs1Group,_t:juniDs1Group2,_u:juniDs1Group3,_v:juniDs1Group4,_w:juniDs1Group5})