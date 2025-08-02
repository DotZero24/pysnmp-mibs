_k='atEnvMonv2TemperatureCurrent'
_j='atEnvMonv2FaultLedStackMemberId'
_i='atEnvMonv2PsbHostSlotIndex'
_h='atEnvMonv2PsbHostBoardIndex'
_g='atEnvMonv2PsbHostStackMemberId'
_f='inRange'
_e='outOfRange'
_d='failed'
_c='atEnvMonv2PsbSensorDescription'
_b='atEnvMonv2PsbSensorType'
_a='atEnvMonv2TemperatureUpperThreshold'
_Z='atEnvMonv2TemperatureDescription'
_Y='atEnvMonv2VoltageCurrent'
_X='atEnvMonv2VoltageLowerThreshold'
_W='atEnvMonv2VoltageUpperThreshold'
_V='atEnvMonv2VoltageDescription'
_U='atEnvMonv2FanCurrentSpeed'
_T='atEnvMonv2FanLowerThreshold'
_S='atEnvMonv2FanDescription'
_R='atEnvMonv2PsbSensorIndex'
_Q='atEnvMonv2PsbSensorBoardIndex'
_P='atEnvMonv2PsbSensorStackMemberId'
_O='atEnvMonv2TemperatureIndex'
_N='atEnvMonv2TemperatureBoardIndex'
_M='atEnvMonv2TemperatureStackMemberId'
_L='atEnvMonv2VoltageIndex'
_K='atEnvMonv2VoltageBoardIndex'
_J='atEnvMonv2VoltageStackMemberId'
_I='atEnvMonv2FanIndex'
_H='atEnvMonv2FanBoardIndex'
_G='atEnvMonv2FanStackMemberId'
_F='noFault'
_E='DisplayStringUnsized'
_D='Integer32'
_C='read-only'
_B='current'
_A='AT-ENVMONv2-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,=mibBuilder.importSymbols('AT-SMI-MIB',_E)
sysinfo,=mibBuilder.importSymbols('AT-SYSINFO-MIB','sysinfo')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
atEnvMonv2=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,3,12))
if mibBuilder.loadTexts:atEnvMonv2.setRevisions(('2008-11-26 00:00','2008-09-24 00:00','2008-02-07 00:00'))
class AtEnvMonv2PsbSensorType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('psbSensorTypeInvalid',0),('fanSpeedDiscrete',1),('temperatureDiscrete',2),('voltageDiscrete',3)))
_AtEnvMonv2FanTable_Object=MibTable
atEnvMonv2FanTable=_AtEnvMonv2FanTable_Object((1,3,6,1,4,1,207,8,4,4,3,12,1))
if mibBuilder.loadTexts:atEnvMonv2FanTable.setStatus(_B)
_AtEnvMonv2FanEntry_Object=MibTableRow
atEnvMonv2FanEntry=_AtEnvMonv2FanEntry_Object((1,3,6,1,4,1,207,8,4,4,3,12,1,1))
atEnvMonv2FanEntry.setIndexNames((0,_A,_G),(0,_A,_H),(0,_A,_I))
if mibBuilder.loadTexts:atEnvMonv2FanEntry.setStatus(_B)
_AtEnvMonv2FanStackMemberId_Type=Unsigned32
_AtEnvMonv2FanStackMemberId_Object=MibTableColumn
atEnvMonv2FanStackMemberId=_AtEnvMonv2FanStackMemberId_Object((1,3,6,1,4,1,207,8,4,4,3,12,1,1,1),_AtEnvMonv2FanStackMemberId_Type())
atEnvMonv2FanStackMemberId.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2FanStackMemberId.setStatus(_B)
_AtEnvMonv2FanBoardIndex_Type=Unsigned32
_AtEnvMonv2FanBoardIndex_Object=MibTableColumn
atEnvMonv2FanBoardIndex=_AtEnvMonv2FanBoardIndex_Object((1,3,6,1,4,1,207,8,4,4,3,12,1,1,2),_AtEnvMonv2FanBoardIndex_Type())
atEnvMonv2FanBoardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2FanBoardIndex.setStatus(_B)
_AtEnvMonv2FanIndex_Type=Unsigned32
_AtEnvMonv2FanIndex_Object=MibTableColumn
atEnvMonv2FanIndex=_AtEnvMonv2FanIndex_Object((1,3,6,1,4,1,207,8,4,4,3,12,1,1,3),_AtEnvMonv2FanIndex_Type())
atEnvMonv2FanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2FanIndex.setStatus(_B)
class _AtEnvMonv2FanDescription_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_AtEnvMonv2FanDescription_Type.__name__=_E
_AtEnvMonv2FanDescription_Object=MibTableColumn
atEnvMonv2FanDescription=_AtEnvMonv2FanDescription_Object((1,3,6,1,4,1,207,8,4,4,3,12,1,1,4),_AtEnvMonv2FanDescription_Type())
atEnvMonv2FanDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2FanDescription.setStatus(_B)
_AtEnvMonv2FanCurrentSpeed_Type=Unsigned32
_AtEnvMonv2FanCurrentSpeed_Object=MibTableColumn
atEnvMonv2FanCurrentSpeed=_AtEnvMonv2FanCurrentSpeed_Object((1,3,6,1,4,1,207,8,4,4,3,12,1,1,5),_AtEnvMonv2FanCurrentSpeed_Type())
atEnvMonv2FanCurrentSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2FanCurrentSpeed.setStatus(_B)
_AtEnvMonv2FanLowerThreshold_Type=Unsigned32
_AtEnvMonv2FanLowerThreshold_Object=MibTableColumn
atEnvMonv2FanLowerThreshold=_AtEnvMonv2FanLowerThreshold_Object((1,3,6,1,4,1,207,8,4,4,3,12,1,1,6),_AtEnvMonv2FanLowerThreshold_Type())
atEnvMonv2FanLowerThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2FanLowerThreshold.setStatus(_B)
class _AtEnvMonv2FanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_d,1),('good',2)))
_AtEnvMonv2FanStatus_Type.__name__=_D
_AtEnvMonv2FanStatus_Object=MibTableColumn
atEnvMonv2FanStatus=_AtEnvMonv2FanStatus_Object((1,3,6,1,4,1,207,8,4,4,3,12,1,1,7),_AtEnvMonv2FanStatus_Type())
atEnvMonv2FanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2FanStatus.setStatus(_B)
_AtEnvMonv2VoltageTable_Object=MibTable
atEnvMonv2VoltageTable=_AtEnvMonv2VoltageTable_Object((1,3,6,1,4,1,207,8,4,4,3,12,2))
if mibBuilder.loadTexts:atEnvMonv2VoltageTable.setStatus(_B)
_AtEnvMonv2VoltageEntry_Object=MibTableRow
atEnvMonv2VoltageEntry=_AtEnvMonv2VoltageEntry_Object((1,3,6,1,4,1,207,8,4,4,3,12,2,1))
atEnvMonv2VoltageEntry.setIndexNames((0,_A,_J),(0,_A,_K),(0,_A,_L))
if mibBuilder.loadTexts:atEnvMonv2VoltageEntry.setStatus(_B)
_AtEnvMonv2VoltageStackMemberId_Type=Unsigned32
_AtEnvMonv2VoltageStackMemberId_Object=MibTableColumn
atEnvMonv2VoltageStackMemberId=_AtEnvMonv2VoltageStackMemberId_Object((1,3,6,1,4,1,207,8,4,4,3,12,2,1,1),_AtEnvMonv2VoltageStackMemberId_Type())
atEnvMonv2VoltageStackMemberId.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2VoltageStackMemberId.setStatus(_B)
_AtEnvMonv2VoltageBoardIndex_Type=Unsigned32
_AtEnvMonv2VoltageBoardIndex_Object=MibTableColumn
atEnvMonv2VoltageBoardIndex=_AtEnvMonv2VoltageBoardIndex_Object((1,3,6,1,4,1,207,8,4,4,3,12,2,1,2),_AtEnvMonv2VoltageBoardIndex_Type())
atEnvMonv2VoltageBoardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2VoltageBoardIndex.setStatus(_B)
_AtEnvMonv2VoltageIndex_Type=Unsigned32
_AtEnvMonv2VoltageIndex_Object=MibTableColumn
atEnvMonv2VoltageIndex=_AtEnvMonv2VoltageIndex_Object((1,3,6,1,4,1,207,8,4,4,3,12,2,1,3),_AtEnvMonv2VoltageIndex_Type())
atEnvMonv2VoltageIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2VoltageIndex.setStatus(_B)
class _AtEnvMonv2VoltageDescription_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_AtEnvMonv2VoltageDescription_Type.__name__=_E
_AtEnvMonv2VoltageDescription_Object=MibTableColumn
atEnvMonv2VoltageDescription=_AtEnvMonv2VoltageDescription_Object((1,3,6,1,4,1,207,8,4,4,3,12,2,1,4),_AtEnvMonv2VoltageDescription_Type())
atEnvMonv2VoltageDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2VoltageDescription.setStatus(_B)
_AtEnvMonv2VoltageCurrent_Type=Integer32
_AtEnvMonv2VoltageCurrent_Object=MibTableColumn
atEnvMonv2VoltageCurrent=_AtEnvMonv2VoltageCurrent_Object((1,3,6,1,4,1,207,8,4,4,3,12,2,1,5),_AtEnvMonv2VoltageCurrent_Type())
atEnvMonv2VoltageCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2VoltageCurrent.setStatus(_B)
_AtEnvMonv2VoltageUpperThreshold_Type=Integer32
_AtEnvMonv2VoltageUpperThreshold_Object=MibTableColumn
atEnvMonv2VoltageUpperThreshold=_AtEnvMonv2VoltageUpperThreshold_Object((1,3,6,1,4,1,207,8,4,4,3,12,2,1,6),_AtEnvMonv2VoltageUpperThreshold_Type())
atEnvMonv2VoltageUpperThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2VoltageUpperThreshold.setStatus(_B)
_AtEnvMonv2VoltageLowerThreshold_Type=Integer32
_AtEnvMonv2VoltageLowerThreshold_Object=MibTableColumn
atEnvMonv2VoltageLowerThreshold=_AtEnvMonv2VoltageLowerThreshold_Object((1,3,6,1,4,1,207,8,4,4,3,12,2,1,7),_AtEnvMonv2VoltageLowerThreshold_Type())
atEnvMonv2VoltageLowerThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2VoltageLowerThreshold.setStatus(_B)
class _AtEnvMonv2VoltageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_AtEnvMonv2VoltageStatus_Type.__name__=_D
_AtEnvMonv2VoltageStatus_Object=MibTableColumn
atEnvMonv2VoltageStatus=_AtEnvMonv2VoltageStatus_Object((1,3,6,1,4,1,207,8,4,4,3,12,2,1,8),_AtEnvMonv2VoltageStatus_Type())
atEnvMonv2VoltageStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2VoltageStatus.setStatus(_B)
_AtEnvMonv2TemperatureTable_Object=MibTable
atEnvMonv2TemperatureTable=_AtEnvMonv2TemperatureTable_Object((1,3,6,1,4,1,207,8,4,4,3,12,3))
if mibBuilder.loadTexts:atEnvMonv2TemperatureTable.setStatus(_B)
_AtEnvMonv2TemperatureEntry_Object=MibTableRow
atEnvMonv2TemperatureEntry=_AtEnvMonv2TemperatureEntry_Object((1,3,6,1,4,1,207,8,4,4,3,12,3,1))
atEnvMonv2TemperatureEntry.setIndexNames((0,_A,_M),(0,_A,_N),(0,_A,_O))
if mibBuilder.loadTexts:atEnvMonv2TemperatureEntry.setStatus(_B)
_AtEnvMonv2TemperatureStackMemberId_Type=Unsigned32
_AtEnvMonv2TemperatureStackMemberId_Object=MibTableColumn
atEnvMonv2TemperatureStackMemberId=_AtEnvMonv2TemperatureStackMemberId_Object((1,3,6,1,4,1,207,8,4,4,3,12,3,1,1),_AtEnvMonv2TemperatureStackMemberId_Type())
atEnvMonv2TemperatureStackMemberId.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2TemperatureStackMemberId.setStatus(_B)
_AtEnvMonv2TemperatureBoardIndex_Type=Unsigned32
_AtEnvMonv2TemperatureBoardIndex_Object=MibTableColumn
atEnvMonv2TemperatureBoardIndex=_AtEnvMonv2TemperatureBoardIndex_Object((1,3,6,1,4,1,207,8,4,4,3,12,3,1,2),_AtEnvMonv2TemperatureBoardIndex_Type())
atEnvMonv2TemperatureBoardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2TemperatureBoardIndex.setStatus(_B)
_AtEnvMonv2TemperatureIndex_Type=Unsigned32
_AtEnvMonv2TemperatureIndex_Object=MibTableColumn
atEnvMonv2TemperatureIndex=_AtEnvMonv2TemperatureIndex_Object((1,3,6,1,4,1,207,8,4,4,3,12,3,1,3),_AtEnvMonv2TemperatureIndex_Type())
atEnvMonv2TemperatureIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2TemperatureIndex.setStatus(_B)
class _AtEnvMonv2TemperatureDescription_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_AtEnvMonv2TemperatureDescription_Type.__name__=_E
_AtEnvMonv2TemperatureDescription_Object=MibTableColumn
atEnvMonv2TemperatureDescription=_AtEnvMonv2TemperatureDescription_Object((1,3,6,1,4,1,207,8,4,4,3,12,3,1,4),_AtEnvMonv2TemperatureDescription_Type())
atEnvMonv2TemperatureDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2TemperatureDescription.setStatus(_B)
_AtEnvMonv2TemperatureCurrent_Type=Integer32
_AtEnvMonv2TemperatureCurrent_Object=MibTableColumn
atEnvMonv2TemperatureCurrent=_AtEnvMonv2TemperatureCurrent_Object((1,3,6,1,4,1,207,8,4,4,3,12,3,1,5),_AtEnvMonv2TemperatureCurrent_Type())
atEnvMonv2TemperatureCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2TemperatureCurrent.setStatus(_B)
_AtEnvMonv2TemperatureUpperThreshold_Type=Integer32
_AtEnvMonv2TemperatureUpperThreshold_Object=MibTableColumn
atEnvMonv2TemperatureUpperThreshold=_AtEnvMonv2TemperatureUpperThreshold_Object((1,3,6,1,4,1,207,8,4,4,3,12,3,1,6),_AtEnvMonv2TemperatureUpperThreshold_Type())
atEnvMonv2TemperatureUpperThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2TemperatureUpperThreshold.setStatus(_B)
class _AtEnvMonv2TemperatureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_AtEnvMonv2TemperatureStatus_Type.__name__=_D
_AtEnvMonv2TemperatureStatus_Object=MibTableColumn
atEnvMonv2TemperatureStatus=_AtEnvMonv2TemperatureStatus_Object((1,3,6,1,4,1,207,8,4,4,3,12,3,1,7),_AtEnvMonv2TemperatureStatus_Type())
atEnvMonv2TemperatureStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2TemperatureStatus.setStatus(_B)
_AtEnvMonv2PsbObjects_ObjectIdentity=ObjectIdentity
atEnvMonv2PsbObjects=_AtEnvMonv2PsbObjects_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,12,4))
_AtEnvMonv2PsbTable_Object=MibTable
atEnvMonv2PsbTable=_AtEnvMonv2PsbTable_Object((1,3,6,1,4,1,207,8,4,4,3,12,4,1))
if mibBuilder.loadTexts:atEnvMonv2PsbTable.setStatus(_B)
_AtEnvMonv2PsbEntry_Object=MibTableRow
atEnvMonv2PsbEntry=_AtEnvMonv2PsbEntry_Object((1,3,6,1,4,1,207,8,4,4,3,12,4,1,1))
atEnvMonv2PsbEntry.setIndexNames((0,_A,_g),(0,_A,_h),(0,_A,_i))
if mibBuilder.loadTexts:atEnvMonv2PsbEntry.setStatus(_B)
_AtEnvMonv2PsbHostStackMemberId_Type=Unsigned32
_AtEnvMonv2PsbHostStackMemberId_Object=MibTableColumn
atEnvMonv2PsbHostStackMemberId=_AtEnvMonv2PsbHostStackMemberId_Object((1,3,6,1,4,1,207,8,4,4,3,12,4,1,1,1),_AtEnvMonv2PsbHostStackMemberId_Type())
atEnvMonv2PsbHostStackMemberId.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2PsbHostStackMemberId.setStatus(_B)
_AtEnvMonv2PsbHostBoardIndex_Type=Unsigned32
_AtEnvMonv2PsbHostBoardIndex_Object=MibTableColumn
atEnvMonv2PsbHostBoardIndex=_AtEnvMonv2PsbHostBoardIndex_Object((1,3,6,1,4,1,207,8,4,4,3,12,4,1,1,2),_AtEnvMonv2PsbHostBoardIndex_Type())
atEnvMonv2PsbHostBoardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2PsbHostBoardIndex.setStatus(_B)
_AtEnvMonv2PsbHostSlotIndex_Type=Unsigned32
_AtEnvMonv2PsbHostSlotIndex_Object=MibTableColumn
atEnvMonv2PsbHostSlotIndex=_AtEnvMonv2PsbHostSlotIndex_Object((1,3,6,1,4,1,207,8,4,4,3,12,4,1,1,3),_AtEnvMonv2PsbHostSlotIndex_Type())
atEnvMonv2PsbHostSlotIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2PsbHostSlotIndex.setStatus(_B)
_AtEnvMonv2PsbHeldBoardIndex_Type=Unsigned32
_AtEnvMonv2PsbHeldBoardIndex_Object=MibTableColumn
atEnvMonv2PsbHeldBoardIndex=_AtEnvMonv2PsbHeldBoardIndex_Object((1,3,6,1,4,1,207,8,4,4,3,12,4,1,1,4),_AtEnvMonv2PsbHeldBoardIndex_Type())
atEnvMonv2PsbHeldBoardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2PsbHeldBoardIndex.setStatus(_B)
_AtEnvMonv2PsbHeldBoardId_Type=ObjectIdentifier
_AtEnvMonv2PsbHeldBoardId_Object=MibTableColumn
atEnvMonv2PsbHeldBoardId=_AtEnvMonv2PsbHeldBoardId_Object((1,3,6,1,4,1,207,8,4,4,3,12,4,1,1,5),_AtEnvMonv2PsbHeldBoardId_Type())
atEnvMonv2PsbHeldBoardId.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2PsbHeldBoardId.setStatus(_B)
class _AtEnvMonv2PsbDescription_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_AtEnvMonv2PsbDescription_Type.__name__=_E
_AtEnvMonv2PsbDescription_Object=MibTableColumn
atEnvMonv2PsbDescription=_AtEnvMonv2PsbDescription_Object((1,3,6,1,4,1,207,8,4,4,3,12,4,1,1,6),_AtEnvMonv2PsbDescription_Type())
atEnvMonv2PsbDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2PsbDescription.setStatus(_B)
_AtEnvMonv2PsbSensorTable_Object=MibTable
atEnvMonv2PsbSensorTable=_AtEnvMonv2PsbSensorTable_Object((1,3,6,1,4,1,207,8,4,4,3,12,4,2))
if mibBuilder.loadTexts:atEnvMonv2PsbSensorTable.setStatus(_B)
_AtEnvMonv2PsbSensorEntry_Object=MibTableRow
atEnvMonv2PsbSensorEntry=_AtEnvMonv2PsbSensorEntry_Object((1,3,6,1,4,1,207,8,4,4,3,12,4,2,1))
atEnvMonv2PsbSensorEntry.setIndexNames((0,_A,_P),(0,_A,_Q),(0,_A,_R))
if mibBuilder.loadTexts:atEnvMonv2PsbSensorEntry.setStatus(_B)
_AtEnvMonv2PsbSensorStackMemberId_Type=Unsigned32
_AtEnvMonv2PsbSensorStackMemberId_Object=MibTableColumn
atEnvMonv2PsbSensorStackMemberId=_AtEnvMonv2PsbSensorStackMemberId_Object((1,3,6,1,4,1,207,8,4,4,3,12,4,2,1,1),_AtEnvMonv2PsbSensorStackMemberId_Type())
atEnvMonv2PsbSensorStackMemberId.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2PsbSensorStackMemberId.setStatus(_B)
_AtEnvMonv2PsbSensorBoardIndex_Type=Unsigned32
_AtEnvMonv2PsbSensorBoardIndex_Object=MibTableColumn
atEnvMonv2PsbSensorBoardIndex=_AtEnvMonv2PsbSensorBoardIndex_Object((1,3,6,1,4,1,207,8,4,4,3,12,4,2,1,2),_AtEnvMonv2PsbSensorBoardIndex_Type())
atEnvMonv2PsbSensorBoardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2PsbSensorBoardIndex.setStatus(_B)
_AtEnvMonv2PsbSensorIndex_Type=Unsigned32
_AtEnvMonv2PsbSensorIndex_Object=MibTableColumn
atEnvMonv2PsbSensorIndex=_AtEnvMonv2PsbSensorIndex_Object((1,3,6,1,4,1,207,8,4,4,3,12,4,2,1,3),_AtEnvMonv2PsbSensorIndex_Type())
atEnvMonv2PsbSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2PsbSensorIndex.setStatus(_B)
_AtEnvMonv2PsbSensorType_Type=AtEnvMonv2PsbSensorType
_AtEnvMonv2PsbSensorType_Object=MibTableColumn
atEnvMonv2PsbSensorType=_AtEnvMonv2PsbSensorType_Object((1,3,6,1,4,1,207,8,4,4,3,12,4,2,1,4),_AtEnvMonv2PsbSensorType_Type())
atEnvMonv2PsbSensorType.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2PsbSensorType.setStatus(_B)
class _AtEnvMonv2PsbSensorDescription_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_AtEnvMonv2PsbSensorDescription_Type.__name__=_E
_AtEnvMonv2PsbSensorDescription_Object=MibTableColumn
atEnvMonv2PsbSensorDescription=_AtEnvMonv2PsbSensorDescription_Object((1,3,6,1,4,1,207,8,4,4,3,12,4,2,1,5),_AtEnvMonv2PsbSensorDescription_Type())
atEnvMonv2PsbSensorDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2PsbSensorDescription.setStatus(_B)
class _AtEnvMonv2PsbSensorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_d,1),('good',2),('notPowered',3)))
_AtEnvMonv2PsbSensorStatus_Type.__name__=_D
_AtEnvMonv2PsbSensorStatus_Object=MibTableColumn
atEnvMonv2PsbSensorStatus=_AtEnvMonv2PsbSensorStatus_Object((1,3,6,1,4,1,207,8,4,4,3,12,4,2,1,6),_AtEnvMonv2PsbSensorStatus_Type())
atEnvMonv2PsbSensorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2PsbSensorStatus.setStatus(_B)
_AtEnvMonv2Traps_ObjectIdentity=ObjectIdentity
atEnvMonv2Traps=_AtEnvMonv2Traps_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,12,5))
_AtEnvMonv2FaultLedTable_Object=MibTable
atEnvMonv2FaultLedTable=_AtEnvMonv2FaultLedTable_Object((1,3,6,1,4,1,207,8,4,4,3,12,6))
if mibBuilder.loadTexts:atEnvMonv2FaultLedTable.setStatus(_B)
_AtEnvMonv2FaultLedEntry_Object=MibTableRow
atEnvMonv2FaultLedEntry=_AtEnvMonv2FaultLedEntry_Object((1,3,6,1,4,1,207,8,4,4,3,12,6,1))
atEnvMonv2FaultLedEntry.setIndexNames((0,_A,_j))
if mibBuilder.loadTexts:atEnvMonv2FaultLedEntry.setStatus(_B)
_AtEnvMonv2FaultLedStackMemberId_Type=Unsigned32
_AtEnvMonv2FaultLedStackMemberId_Object=MibTableColumn
atEnvMonv2FaultLedStackMemberId=_AtEnvMonv2FaultLedStackMemberId_Object((1,3,6,1,4,1,207,8,4,4,3,12,6,1,1),_AtEnvMonv2FaultLedStackMemberId_Type())
atEnvMonv2FaultLedStackMemberId.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2FaultLedStackMemberId.setStatus(_B)
class _AtEnvMonv2FaultLed1Flash_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('heatsinkFanFailure',1),(_F,2)))
_AtEnvMonv2FaultLed1Flash_Type.__name__=_D
_AtEnvMonv2FaultLed1Flash_Object=MibTableColumn
atEnvMonv2FaultLed1Flash=_AtEnvMonv2FaultLed1Flash_Object((1,3,6,1,4,1,207,8,4,4,3,12,6,1,2),_AtEnvMonv2FaultLed1Flash_Type())
atEnvMonv2FaultLed1Flash.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2FaultLed1Flash.setStatus(_B)
class _AtEnvMonv2FaultLed2Flashes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('chassisFanFailure',1),(_F,2)))
_AtEnvMonv2FaultLed2Flashes_Type.__name__=_D
_AtEnvMonv2FaultLed2Flashes_Object=MibTableColumn
atEnvMonv2FaultLed2Flashes=_AtEnvMonv2FaultLed2Flashes_Object((1,3,6,1,4,1,207,8,4,4,3,12,6,1,3),_AtEnvMonv2FaultLed2Flashes_Type())
atEnvMonv2FaultLed2Flashes.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2FaultLed2Flashes.setStatus(_B)
class _AtEnvMonv2FaultLed3Flashes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sensorFailure',1),(_F,2)))
_AtEnvMonv2FaultLed3Flashes_Type.__name__=_D
_AtEnvMonv2FaultLed3Flashes_Object=MibTableColumn
atEnvMonv2FaultLed3Flashes=_AtEnvMonv2FaultLed3Flashes_Object((1,3,6,1,4,1,207,8,4,4,3,12,6,1,4),_AtEnvMonv2FaultLed3Flashes_Type())
atEnvMonv2FaultLed3Flashes.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2FaultLed3Flashes.setStatus(_B)
class _AtEnvMonv2FaultLed4Flashes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('xemInitialisationFailure',1),(_F,2)))
_AtEnvMonv2FaultLed4Flashes_Type.__name__=_D
_AtEnvMonv2FaultLed4Flashes_Object=MibTableColumn
atEnvMonv2FaultLed4Flashes=_AtEnvMonv2FaultLed4Flashes_Object((1,3,6,1,4,1,207,8,4,4,3,12,6,1,5),_AtEnvMonv2FaultLed4Flashes_Type())
atEnvMonv2FaultLed4Flashes.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2FaultLed4Flashes.setStatus(_B)
class _AtEnvMonv2FaultLed5Flashes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues((_F,2))
_AtEnvMonv2FaultLed5Flashes_Type.__name__=_D
_AtEnvMonv2FaultLed5Flashes_Object=MibTableColumn
atEnvMonv2FaultLed5Flashes=_AtEnvMonv2FaultLed5Flashes_Object((1,3,6,1,4,1,207,8,4,4,3,12,6,1,6),_AtEnvMonv2FaultLed5Flashes_Type())
atEnvMonv2FaultLed5Flashes.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2FaultLed5Flashes.setStatus(_B)
class _AtEnvMonv2FaultLed6Flashes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('temperatureFailure',1),(_F,2)))
_AtEnvMonv2FaultLed6Flashes_Type.__name__=_D
_AtEnvMonv2FaultLed6Flashes_Object=MibTableColumn
atEnvMonv2FaultLed6Flashes=_AtEnvMonv2FaultLed6Flashes_Object((1,3,6,1,4,1,207,8,4,4,3,12,6,1,7),_AtEnvMonv2FaultLed6Flashes_Type())
atEnvMonv2FaultLed6Flashes.setMaxAccess(_C)
if mibBuilder.loadTexts:atEnvMonv2FaultLed6Flashes.setStatus(_B)
atEnvMonv2FanAlarmSetEvent=NotificationType((1,3,6,1,4,1,207,8,4,4,3,12,5,1))
atEnvMonv2FanAlarmSetEvent.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:atEnvMonv2FanAlarmSetEvent.setStatus(_B)
atEnvMonv2FanAlarmClearedEvent=NotificationType((1,3,6,1,4,1,207,8,4,4,3,12,5,2))
atEnvMonv2FanAlarmClearedEvent.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:atEnvMonv2FanAlarmClearedEvent.setStatus(_B)
atEnvMonv2VoltAlarmSetEvent=NotificationType((1,3,6,1,4,1,207,8,4,4,3,12,5,3))
atEnvMonv2VoltAlarmSetEvent.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:atEnvMonv2VoltAlarmSetEvent.setStatus(_B)
atEnvMonv2VoltAlarmClearedEvent=NotificationType((1,3,6,1,4,1,207,8,4,4,3,12,5,4))
atEnvMonv2VoltAlarmClearedEvent.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:atEnvMonv2VoltAlarmClearedEvent.setStatus(_B)
atEnvMonv2TempAlarmSetEvent=NotificationType((1,3,6,1,4,1,207,8,4,4,3,12,5,5))
atEnvMonv2TempAlarmSetEvent.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_Z),(_A,_a),(_A,_k)))
if mibBuilder.loadTexts:atEnvMonv2TempAlarmSetEvent.setStatus(_B)
atEnvMonv2TempAlarmClearedEvent=NotificationType((1,3,6,1,4,1,207,8,4,4,3,12,5,6))
atEnvMonv2TempAlarmClearedEvent.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:atEnvMonv2TempAlarmClearedEvent.setStatus(_B)
atEnvMonv2PsbAlarmSetEvent=NotificationType((1,3,6,1,4,1,207,8,4,4,3,12,5,7))
atEnvMonv2PsbAlarmSetEvent.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:atEnvMonv2PsbAlarmSetEvent.setStatus(_B)
atEnvMonv2PsbAlarmClearedEvent=NotificationType((1,3,6,1,4,1,207,8,4,4,3,12,5,8))
atEnvMonv2PsbAlarmClearedEvent.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:atEnvMonv2PsbAlarmClearedEvent.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'AtEnvMonv2PsbSensorType':AtEnvMonv2PsbSensorType,'atEnvMonv2':atEnvMonv2,'atEnvMonv2FanTable':atEnvMonv2FanTable,'atEnvMonv2FanEntry':atEnvMonv2FanEntry,_G:atEnvMonv2FanStackMemberId,_H:atEnvMonv2FanBoardIndex,_I:atEnvMonv2FanIndex,_S:atEnvMonv2FanDescription,_U:atEnvMonv2FanCurrentSpeed,_T:atEnvMonv2FanLowerThreshold,'atEnvMonv2FanStatus':atEnvMonv2FanStatus,'atEnvMonv2VoltageTable':atEnvMonv2VoltageTable,'atEnvMonv2VoltageEntry':atEnvMonv2VoltageEntry,_J:atEnvMonv2VoltageStackMemberId,_K:atEnvMonv2VoltageBoardIndex,_L:atEnvMonv2VoltageIndex,_V:atEnvMonv2VoltageDescription,_Y:atEnvMonv2VoltageCurrent,_W:atEnvMonv2VoltageUpperThreshold,_X:atEnvMonv2VoltageLowerThreshold,'atEnvMonv2VoltageStatus':atEnvMonv2VoltageStatus,'atEnvMonv2TemperatureTable':atEnvMonv2TemperatureTable,'atEnvMonv2TemperatureEntry':atEnvMonv2TemperatureEntry,_M:atEnvMonv2TemperatureStackMemberId,_N:atEnvMonv2TemperatureBoardIndex,_O:atEnvMonv2TemperatureIndex,_Z:atEnvMonv2TemperatureDescription,_k:atEnvMonv2TemperatureCurrent,_a:atEnvMonv2TemperatureUpperThreshold,'atEnvMonv2TemperatureStatus':atEnvMonv2TemperatureStatus,'atEnvMonv2PsbObjects':atEnvMonv2PsbObjects,'atEnvMonv2PsbTable':atEnvMonv2PsbTable,'atEnvMonv2PsbEntry':atEnvMonv2PsbEntry,_g:atEnvMonv2PsbHostStackMemberId,_h:atEnvMonv2PsbHostBoardIndex,_i:atEnvMonv2PsbHostSlotIndex,'atEnvMonv2PsbHeldBoardIndex':atEnvMonv2PsbHeldBoardIndex,'atEnvMonv2PsbHeldBoardId':atEnvMonv2PsbHeldBoardId,'atEnvMonv2PsbDescription':atEnvMonv2PsbDescription,'atEnvMonv2PsbSensorTable':atEnvMonv2PsbSensorTable,'atEnvMonv2PsbSensorEntry':atEnvMonv2PsbSensorEntry,_P:atEnvMonv2PsbSensorStackMemberId,_Q:atEnvMonv2PsbSensorBoardIndex,_R:atEnvMonv2PsbSensorIndex,_b:atEnvMonv2PsbSensorType,_c:atEnvMonv2PsbSensorDescription,'atEnvMonv2PsbSensorStatus':atEnvMonv2PsbSensorStatus,'atEnvMonv2Traps':atEnvMonv2Traps,'atEnvMonv2FanAlarmSetEvent':atEnvMonv2FanAlarmSetEvent,'atEnvMonv2FanAlarmClearedEvent':atEnvMonv2FanAlarmClearedEvent,'atEnvMonv2VoltAlarmSetEvent':atEnvMonv2VoltAlarmSetEvent,'atEnvMonv2VoltAlarmClearedEvent':atEnvMonv2VoltAlarmClearedEvent,'atEnvMonv2TempAlarmSetEvent':atEnvMonv2TempAlarmSetEvent,'atEnvMonv2TempAlarmClearedEvent':atEnvMonv2TempAlarmClearedEvent,'atEnvMonv2PsbAlarmSetEvent':atEnvMonv2PsbAlarmSetEvent,'atEnvMonv2PsbAlarmClearedEvent':atEnvMonv2PsbAlarmClearedEvent,'atEnvMonv2FaultLedTable':atEnvMonv2FaultLedTable,'atEnvMonv2FaultLedEntry':atEnvMonv2FaultLedEntry,_j:atEnvMonv2FaultLedStackMemberId,'atEnvMonv2FaultLed1Flash':atEnvMonv2FaultLed1Flash,'atEnvMonv2FaultLed2Flashes':atEnvMonv2FaultLed2Flashes,'atEnvMonv2FaultLed3Flashes':atEnvMonv2FaultLed3Flashes,'atEnvMonv2FaultLed4Flashes':atEnvMonv2FaultLed4Flashes,'atEnvMonv2FaultLed5Flashes':atEnvMonv2FaultLed5Flashes,'atEnvMonv2FaultLed6Flashes':atEnvMonv2FaultLed6Flashes})