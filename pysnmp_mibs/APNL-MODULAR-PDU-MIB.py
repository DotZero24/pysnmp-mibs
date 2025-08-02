_i='beeperLo'
_h='beeperHi'
_g='trapLo'
_f='trapHi'
_e='sensorIndex'
_d='trapVoltLo'
_c='trapVoltHi'
_b='trapCurrLo'
_a='trapCurrHi'
_Z='not-accessible'
_Y='nodeIndex'
_X='by type'
_W='Unsigned32'
_V='on'
_U='off'
_T='unknown'
_S='Volts'
_R='switchOff'
_Q='switchOn'
_P='trapThreshHold'
_O='trapThreshHoldType'
_N='accessible-for-notify'
_M='KiloWattHours'
_L='kiloWattHours'
_K='trapTableIndex'
_J='trapType'
_I='IPv4 Addr'
_H='Bits'
_G='DisplayString'
_F='DeciAmpers'
_E='Integer32'
_D='APNL-MODULAR-PDU-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_H,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_W,'enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_G,'PhysAddress','TextualConvention')
apNederland=ModuleIdentity((1,3,6,1,4,1,29640))
if mibBuilder.loadTexts:apNederland.setRevisions(('2013-01-24 13:05',))
_ApnlDirectory_ObjectIdentity=ObjectIdentity
apnlDirectory=_ApnlDirectory_ObjectIdentity((1,3,6,1,4,1,29640,1))
_ApnlMib_ObjectIdentity=ObjectIdentity
apnlMib=_ApnlMib_ObjectIdentity((1,3,6,1,4,1,29640,2))
_ApnlTmp_ObjectIdentity=ObjectIdentity
apnlTmp=_ApnlTmp_ObjectIdentity((1,3,6,1,4,1,29640,3))
_ApnlModules_ObjectIdentity=ObjectIdentity
apnlModules=_ApnlModules_ObjectIdentity((1,3,6,1,4,1,29640,4))
_Cm_ObjectIdentity=ObjectIdentity
cm=_Cm_ObjectIdentity((1,3,6,1,4,1,29640,4,1))
_CmTraps_ObjectIdentity=ObjectIdentity
cmTraps=_CmTraps_ObjectIdentity((1,3,6,1,4,1,29640,4,2))
_Pdu_ObjectIdentity=ObjectIdentity
pdu=_Pdu_ObjectIdentity((1,3,6,1,4,1,29640,4,3))
class _PduType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('pduModular',0),('pduGateway1',1),('pduGateway2',2)))
_PduType_Type.__name__=_E
_PduType_Object=MibScalar
pduType=_PduType_Object((1,3,6,1,4,1,29640,4,3,1),_PduType_Type())
pduType.setMaxAccess(_B)
if mibBuilder.loadTexts:pduType.setStatus(_A)
_PduProductIdentifier_Type=Integer32
_PduProductIdentifier_Object=MibScalar
pduProductIdentifier=_PduProductIdentifier_Object((1,3,6,1,4,1,29640,4,3,2),_PduProductIdentifier_Type())
pduProductIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:pduProductIdentifier.setStatus(_A)
class _PduSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_PduSerialNumber_Type.__name__=_G
_PduSerialNumber_Object=MibScalar
pduSerialNumber=_PduSerialNumber_Object((1,3,6,1,4,1,29640,4,3,3),_PduSerialNumber_Type())
pduSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pduSerialNumber.setStatus(_A)
class _PduStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('pduBusy',0),('pduReady1',1),('pduAlarm',2),('pduError',3)))
_PduStatus_Type.__name__=_E
_PduStatus_Object=MibScalar
pduStatus=_PduStatus_Object((1,3,6,1,4,1,29640,4,3,4),_PduStatus_Type())
pduStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pduStatus.setStatus(_A)
_PduPower_Type=Unsigned32
_PduPower_Object=MibScalar
pduPower=_PduPower_Object((1,3,6,1,4,1,29640,4,3,5),_PduPower_Type())
pduPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pduPower.setStatus(_A)
if mibBuilder.loadTexts:pduPower.setUnits(_L)
_PduPowerL1_Type=Unsigned32
_PduPowerL1_Object=MibScalar
pduPowerL1=_PduPowerL1_Object((1,3,6,1,4,1,29640,4,3,6),_PduPowerL1_Type())
pduPowerL1.setMaxAccess(_B)
if mibBuilder.loadTexts:pduPowerL1.setStatus(_A)
if mibBuilder.loadTexts:pduPowerL1.setUnits(_L)
_PduPowerL2_Type=Unsigned32
_PduPowerL2_Object=MibScalar
pduPowerL2=_PduPowerL2_Object((1,3,6,1,4,1,29640,4,3,7),_PduPowerL2_Type())
pduPowerL2.setMaxAccess(_B)
if mibBuilder.loadTexts:pduPowerL2.setStatus(_A)
if mibBuilder.loadTexts:pduPowerL2.setUnits(_L)
_PduPowerL3_Type=Unsigned32
_PduPowerL3_Object=MibScalar
pduPowerL3=_PduPowerL3_Object((1,3,6,1,4,1,29640,4,3,8),_PduPowerL3_Type())
pduPowerL3.setMaxAccess(_B)
if mibBuilder.loadTexts:pduPowerL3.setStatus(_A)
if mibBuilder.loadTexts:pduPowerL3.setUnits(_L)
_PduKvar_Type=Unsigned32
_PduKvar_Object=MibScalar
pduKvar=_PduKvar_Object((1,3,6,1,4,1,29640,4,3,9),_PduKvar_Type())
pduKvar.setMaxAccess(_B)
if mibBuilder.loadTexts:pduKvar.setStatus(_A)
if mibBuilder.loadTexts:pduKvar.setUnits(_M)
_PduKvarL1_Type=Unsigned32
_PduKvarL1_Object=MibScalar
pduKvarL1=_PduKvarL1_Object((1,3,6,1,4,1,29640,4,3,10),_PduKvarL1_Type())
pduKvarL1.setMaxAccess(_B)
if mibBuilder.loadTexts:pduKvarL1.setStatus(_A)
if mibBuilder.loadTexts:pduKvarL1.setUnits(_M)
_PduKvarL2_Type=Unsigned32
_PduKvarL2_Object=MibScalar
pduKvarL2=_PduKvarL2_Object((1,3,6,1,4,1,29640,4,3,11),_PduKvarL2_Type())
pduKvarL2.setMaxAccess(_B)
if mibBuilder.loadTexts:pduKvarL2.setStatus(_A)
if mibBuilder.loadTexts:pduKvarL2.setUnits(_M)
_PduKvarL3_Type=Unsigned32
_PduKvarL3_Object=MibScalar
pduKvarL3=_PduKvarL3_Object((1,3,6,1,4,1,29640,4,3,12),_PduKvarL3_Type())
pduKvarL3.setMaxAccess(_B)
if mibBuilder.loadTexts:pduKvarL3.setStatus(_A)
if mibBuilder.loadTexts:pduKvarL3.setUnits(_M)
_PdulAcurrent_Type=Unsigned32
_PdulAcurrent_Object=MibScalar
pdulAcurrent=_PdulAcurrent_Object((1,3,6,1,4,1,29640,4,3,13),_PdulAcurrent_Type())
pdulAcurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:pdulAcurrent.setStatus(_A)
if mibBuilder.loadTexts:pdulAcurrent.setUnits(_F)
_PduAcurrentL1_Type=Unsigned32
_PduAcurrentL1_Object=MibScalar
pduAcurrentL1=_PduAcurrentL1_Object((1,3,6,1,4,1,29640,4,3,14),_PduAcurrentL1_Type())
pduAcurrentL1.setMaxAccess(_B)
if mibBuilder.loadTexts:pduAcurrentL1.setStatus(_A)
if mibBuilder.loadTexts:pduAcurrentL1.setUnits(_F)
_PduAcurrentL2_Type=Unsigned32
_PduAcurrentL2_Object=MibScalar
pduAcurrentL2=_PduAcurrentL2_Object((1,3,6,1,4,1,29640,4,3,15),_PduAcurrentL2_Type())
pduAcurrentL2.setMaxAccess(_B)
if mibBuilder.loadTexts:pduAcurrentL2.setStatus(_A)
if mibBuilder.loadTexts:pduAcurrentL2.setUnits(_F)
_PduAcurrentL3_Type=Unsigned32
_PduAcurrentL3_Object=MibScalar
pduAcurrentL3=_PduAcurrentL3_Object((1,3,6,1,4,1,29640,4,3,16),_PduAcurrentL3_Type())
pduAcurrentL3.setMaxAccess(_B)
if mibBuilder.loadTexts:pduAcurrentL3.setStatus(_A)
if mibBuilder.loadTexts:pduAcurrentL3.setUnits(_F)
_PduCurIpAddress_Type=IpAddress
_PduCurIpAddress_Object=MibScalar
pduCurIpAddress=_PduCurIpAddress_Object((1,3,6,1,4,1,29640,4,3,17),_PduCurIpAddress_Type())
pduCurIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:pduCurIpAddress.setStatus(_A)
if mibBuilder.loadTexts:pduCurIpAddress.setUnits(_I)
_PduCurSubNetMask_Type=IpAddress
_PduCurSubNetMask_Object=MibScalar
pduCurSubNetMask=_PduCurSubNetMask_Object((1,3,6,1,4,1,29640,4,3,18),_PduCurSubNetMask_Type())
pduCurSubNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:pduCurSubNetMask.setStatus(_A)
if mibBuilder.loadTexts:pduCurSubNetMask.setUnits(_I)
_PduCurDefGwAddress_Type=IpAddress
_PduCurDefGwAddress_Object=MibScalar
pduCurDefGwAddress=_PduCurDefGwAddress_Object((1,3,6,1,4,1,29640,4,3,19),_PduCurDefGwAddress_Type())
pduCurDefGwAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:pduCurDefGwAddress.setStatus(_A)
if mibBuilder.loadTexts:pduCurDefGwAddress.setUnits(_I)
_PduNumberOfNodes_Type=Integer32
_PduNumberOfNodes_Object=MibScalar
pduNumberOfNodes=_PduNumberOfNodes_Object((1,3,6,1,4,1,29640,4,3,20),_PduNumberOfNodes_Type())
pduNumberOfNodes.setMaxAccess(_B)
if mibBuilder.loadTexts:pduNumberOfNodes.setStatus(_A)
_PduNumberOfSensors_Type=Integer32
_PduNumberOfSensors_Object=MibScalar
pduNumberOfSensors=_PduNumberOfSensors_Object((1,3,6,1,4,1,29640,4,3,21),_PduNumberOfSensors_Type())
pduNumberOfSensors.setMaxAccess(_B)
if mibBuilder.loadTexts:pduNumberOfSensors.setStatus(_A)
class _PduSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_PduSoftwareVersion_Type.__name__=_G
_PduSoftwareVersion_Object=MibScalar
pduSoftwareVersion=_PduSoftwareVersion_Object((1,3,6,1,4,1,29640,4,3,22),_PduSoftwareVersion_Type())
pduSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:pduSoftwareVersion.setStatus(_A)
class _PduFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_PduFirmwareVersion_Type.__name__=_G
_PduFirmwareVersion_Object=MibScalar
pduFirmwareVersion=_PduFirmwareVersion_Object((1,3,6,1,4,1,29640,4,3,23),_PduFirmwareVersion_Type())
pduFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:pduFirmwareVersion.setStatus(_A)
class _PduBusProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('apbus',0),('modbus',1)))
_PduBusProtocol_Type.__name__=_E
_PduBusProtocol_Object=MibScalar
pduBusProtocol=_PduBusProtocol_Object((1,3,6,1,4,1,29640,4,3,24),_PduBusProtocol_Type())
pduBusProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:pduBusProtocol.setStatus(_A)
class _PduAdminCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('noOp',0),('rebootPdu',1),('rediscover',2),('updateSofware',3),('resetConfig',4),('resetSNMPv3Config',5),('resetNetworkSetting',6),('readDataFromBusPdu',7),('writeDataToBusPdu',8)))
_PduAdminCommand_Type.__name__=_E
_PduAdminCommand_Object=MibScalar
pduAdminCommand=_PduAdminCommand_Object((1,3,6,1,4,1,29640,4,3,25),_PduAdminCommand_Type())
pduAdminCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:pduAdminCommand.setStatus(_A)
_PduStartupIpAddress_Type=IpAddress
_PduStartupIpAddress_Object=MibScalar
pduStartupIpAddress=_PduStartupIpAddress_Object((1,3,6,1,4,1,29640,4,3,26),_PduStartupIpAddress_Type())
pduStartupIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pduStartupIpAddress.setStatus(_A)
if mibBuilder.loadTexts:pduStartupIpAddress.setUnits(_I)
_PduStartupSubNetMask_Type=IpAddress
_PduStartupSubNetMask_Object=MibScalar
pduStartupSubNetMask=_PduStartupSubNetMask_Object((1,3,6,1,4,1,29640,4,3,27),_PduStartupSubNetMask_Type())
pduStartupSubNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:pduStartupSubNetMask.setStatus(_A)
if mibBuilder.loadTexts:pduStartupSubNetMask.setUnits(_I)
_PduStartupDefGwAddress_Type=IpAddress
_PduStartupDefGwAddress_Object=MibScalar
pduStartupDefGwAddress=_PduStartupDefGwAddress_Object((1,3,6,1,4,1,29640,4,3,28),_PduStartupDefGwAddress_Type())
pduStartupDefGwAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pduStartupDefGwAddress.setStatus(_A)
if mibBuilder.loadTexts:pduStartupDefGwAddress.setUnits(_I)
_PduRealTimeClock_Type=DateAndTime
_PduRealTimeClock_Object=MibScalar
pduRealTimeClock=_PduRealTimeClock_Object((1,3,6,1,4,1,29640,4,3,29),_PduRealTimeClock_Type())
pduRealTimeClock.setMaxAccess(_C)
if mibBuilder.loadTexts:pduRealTimeClock.setStatus(_A)
class _PduEnableFeatures_Type(Bits):namedValues=NamedValues(*(('globalWebEnabled',0),('globalUsbEnabled',1),('globalSwitchEnabled',2),('displaySwitchEnabled',3),('webSwitchEnabled',4)))
_PduEnableFeatures_Type.__name__=_H
_PduEnableFeatures_Object=MibScalar
pduEnableFeatures=_PduEnableFeatures_Object((1,3,6,1,4,1,29640,4,3,30),_PduEnableFeatures_Type())
pduEnableFeatures.setMaxAccess(_C)
if mibBuilder.loadTexts:pduEnableFeatures.setStatus(_A)
_PduBusAddress_Type=Integer32
_PduBusAddress_Object=MibScalar
pduBusAddress=_PduBusAddress_Object((1,3,6,1,4,1,29640,4,3,31),_PduBusAddress_Type())
pduBusAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pduBusAddress.setStatus(_A)
class _PduName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_PduName_Type.__name__=_G
_PduName_Object=MibScalar
pduName=_PduName_Object((1,3,6,1,4,1,29640,4,3,32),_PduName_Type())
pduName.setMaxAccess(_C)
if mibBuilder.loadTexts:pduName.setStatus(_A)
_NodeTable_Object=MibTable
nodeTable=_NodeTable_Object((1,3,6,1,4,1,29640,4,3,33))
if mibBuilder.loadTexts:nodeTable.setStatus(_A)
_NodeEntry_Object=MibTableRow
nodeEntry=_NodeEntry_Object((1,3,6,1,4,1,29640,4,3,33,1))
nodeEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:nodeEntry.setStatus(_A)
class _NodeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_NodeIndex_Type.__name__=_W
_NodeIndex_Object=MibTableColumn
nodeIndex=_NodeIndex_Object((1,3,6,1,4,1,29640,4,3,33,1,1),_NodeIndex_Type())
nodeIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:nodeIndex.setStatus(_A)
class _NodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('typeUnknown',0),('typePresModChar',1),('typePresModMono',2),('typePresModGraph',3),('typePowerMeter',4),('typePowerMeterSwitch',5),('typeSwitch',6)))
_NodeType_Type.__name__=_E
_NodeType_Object=MibTableColumn
nodeType=_NodeType_Object((1,3,6,1,4,1,29640,4,3,33,1,2),_NodeType_Type())
nodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeType.setStatus(_A)
_NodeOutlet_Type=Unsigned32
_NodeOutlet_Object=MibTableColumn
nodeOutlet=_NodeOutlet_Object((1,3,6,1,4,1,29640,4,3,33,1,3),_NodeOutlet_Type())
nodeOutlet.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeOutlet.setStatus(_A)
class _NodeAlarmStatus_Type(Bits):namedValues=NamedValues(*((_a,0),(_b,1),(_c,2),(_d,3),(_Q,4),(_R,5)))
_NodeAlarmStatus_Type.__name__=_H
_NodeAlarmStatus_Object=MibTableColumn
nodeAlarmStatus=_NodeAlarmStatus_Object((1,3,6,1,4,1,29640,4,3,33,1,4),_NodeAlarmStatus_Type())
nodeAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeAlarmStatus.setStatus(_A)
_NodePower_Type=Unsigned32
_NodePower_Object=MibTableColumn
nodePower=_NodePower_Object((1,3,6,1,4,1,29640,4,3,33,1,5),_NodePower_Type())
nodePower.setMaxAccess(_B)
if mibBuilder.loadTexts:nodePower.setStatus(_A)
if mibBuilder.loadTexts:nodePower.setUnits(_L)
_NodeAcurrent_Type=Unsigned32
_NodeAcurrent_Object=MibTableColumn
nodeAcurrent=_NodeAcurrent_Object((1,3,6,1,4,1,29640,4,3,33,1,6),_NodeAcurrent_Type())
nodeAcurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeAcurrent.setStatus(_A)
if mibBuilder.loadTexts:nodeAcurrent.setUnits(_F)
_NodePeakCurrent_Type=Unsigned32
_NodePeakCurrent_Object=MibTableColumn
nodePeakCurrent=_NodePeakCurrent_Object((1,3,6,1,4,1,29640,4,3,33,1,7),_NodePeakCurrent_Type())
nodePeakCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:nodePeakCurrent.setStatus(_A)
if mibBuilder.loadTexts:nodePeakCurrent.setUnits(_F)
_NodeVoltage_Type=Unsigned32
_NodeVoltage_Object=MibTableColumn
nodeVoltage=_NodeVoltage_Object((1,3,6,1,4,1,29640,4,3,33,1,8),_NodeVoltage_Type())
nodeVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeVoltage.setStatus(_A)
if mibBuilder.loadTexts:nodeVoltage.setUnits(_S)
_NodeMinVoltage_Type=Unsigned32
_NodeMinVoltage_Object=MibTableColumn
nodeMinVoltage=_NodeMinVoltage_Object((1,3,6,1,4,1,29640,4,3,33,1,9),_NodeMinVoltage_Type())
nodeMinVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeMinVoltage.setStatus(_A)
if mibBuilder.loadTexts:nodeMinVoltage.setUnits(_S)
_NodeKvar_Type=Unsigned32
_NodeKvar_Object=MibTableColumn
nodeKvar=_NodeKvar_Object((1,3,6,1,4,1,29640,4,3,33,1,10),_NodeKvar_Type())
nodeKvar.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeKvar.setStatus(_A)
if mibBuilder.loadTexts:nodeKvar.setUnits(_M)
_NodeFrequency_Type=Unsigned32
_NodeFrequency_Object=MibTableColumn
nodeFrequency=_NodeFrequency_Object((1,3,6,1,4,1,29640,4,3,33,1,11),_NodeFrequency_Type())
nodeFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeFrequency.setStatus(_A)
if mibBuilder.loadTexts:nodeFrequency.setUnits('Hertz')
_NodePowerFactor_Type=Unsigned32
_NodePowerFactor_Object=MibTableColumn
nodePowerFactor=_NodePowerFactor_Object((1,3,6,1,4,1,29640,4,3,33,1,12),_NodePowerFactor_Type())
nodePowerFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:nodePowerFactor.setStatus(_A)
if mibBuilder.loadTexts:nodePowerFactor.setUnits('Percent')
class _NodeSwitchOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_T,0),(_U,1),(_V,2)))
_NodeSwitchOperStatus_Type.__name__=_E
_NodeSwitchOperStatus_Object=MibTableColumn
nodeSwitchOperStatus=_NodeSwitchOperStatus_Object((1,3,6,1,4,1,29640,4,3,33,1,13),_NodeSwitchOperStatus_Type())
nodeSwitchOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeSwitchOperStatus.setStatus(_A)
class _NodeSwitchAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_T,0),(_U,1),(_V,2)))
_NodeSwitchAdminStatus_Type.__name__=_E
_NodeSwitchAdminStatus_Object=MibTableColumn
nodeSwitchAdminStatus=_NodeSwitchAdminStatus_Object((1,3,6,1,4,1,29640,4,3,33,1,14),_NodeSwitchAdminStatus_Type())
nodeSwitchAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeSwitchAdminStatus.setStatus(_A)
_NodeCurrHiThresh_Type=Unsigned32
_NodeCurrHiThresh_Object=MibTableColumn
nodeCurrHiThresh=_NodeCurrHiThresh_Object((1,3,6,1,4,1,29640,4,3,33,1,15),_NodeCurrHiThresh_Type())
nodeCurrHiThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeCurrHiThresh.setStatus(_A)
if mibBuilder.loadTexts:nodeCurrHiThresh.setUnits(_F)
_NodeCurrLoThresh_Type=Unsigned32
_NodeCurrLoThresh_Object=MibTableColumn
nodeCurrLoThresh=_NodeCurrLoThresh_Object((1,3,6,1,4,1,29640,4,3,33,1,16),_NodeCurrLoThresh_Type())
nodeCurrLoThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeCurrLoThresh.setStatus(_A)
if mibBuilder.loadTexts:nodeCurrLoThresh.setUnits(_F)
_NodeVoltHiThresh_Type=Unsigned32
_NodeVoltHiThresh_Object=MibTableColumn
nodeVoltHiThresh=_NodeVoltHiThresh_Object((1,3,6,1,4,1,29640,4,3,33,1,17),_NodeVoltHiThresh_Type())
nodeVoltHiThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeVoltHiThresh.setStatus(_A)
if mibBuilder.loadTexts:nodeVoltHiThresh.setUnits(_S)
_NodeVoltLoThresh_Type=Unsigned32
_NodeVoltLoThresh_Object=MibTableColumn
nodeVoltLoThresh=_NodeVoltLoThresh_Object((1,3,6,1,4,1,29640,4,3,33,1,18),_NodeVoltLoThresh_Type())
nodeVoltLoThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeVoltLoThresh.setStatus(_A)
if mibBuilder.loadTexts:nodeVoltLoThresh.setUnits(_S)
class _NodeAlarmSelector_Type(Bits):namedValues=NamedValues(*((_a,0),(_b,1),(_c,2),(_d,3),(_Q,4),(_R,5)))
_NodeAlarmSelector_Type.__name__=_H
_NodeAlarmSelector_Object=MibTableColumn
nodeAlarmSelector=_NodeAlarmSelector_Object((1,3,6,1,4,1,29640,4,3,33,1,19),_NodeAlarmSelector_Type())
nodeAlarmSelector.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeAlarmSelector.setStatus(_A)
class _NodeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,14))
_NodeName_Type.__name__=_G
_NodeName_Object=MibTableColumn
nodeName=_NodeName_Object((1,3,6,1,4,1,29640,4,3,33,1,20),_NodeName_Type())
nodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeName.setStatus(_A)
class _NodePhase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('phaseUnknown',0),('phaseL1',1),('phaseL2',2),('phaseL3',3)))
_NodePhase_Type.__name__=_E
_NodePhase_Object=MibTableColumn
nodePhase=_NodePhase_Object((1,3,6,1,4,1,29640,4,3,33,1,21),_NodePhase_Type())
nodePhase.setMaxAccess(_C)
if mibBuilder.loadTexts:nodePhase.setStatus(_A)
_SensorTable_Object=MibTable
sensorTable=_SensorTable_Object((1,3,6,1,4,1,29640,4,3,34))
if mibBuilder.loadTexts:sensorTable.setStatus(_A)
_SensorEntry_Object=MibTableRow
sensorEntry=_SensorEntry_Object((1,3,6,1,4,1,29640,4,3,34,1))
sensorEntry.setIndexNames((0,_D,_e))
if mibBuilder.loadTexts:sensorEntry.setStatus(_A)
class _SensorIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_SensorIndex_Type.__name__=_W
_SensorIndex_Object=MibTableColumn
sensorIndex=_SensorIndex_Object((1,3,6,1,4,1,29640,4,3,34,1,1),_SensorIndex_Type())
sensorIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:sensorIndex.setStatus(_A)
class _SensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('other',0),('temperature',1),('humidity',2),('smoke',3),('co1',4),('vibration',5),('doorStatus',6)))
_SensorType_Type.__name__=_E
_SensorType_Object=MibTableColumn
sensorType=_SensorType_Object((1,3,6,1,4,1,29640,4,3,34,1,2),_SensorType_Type())
sensorType.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorType.setStatus(_A)
class _SensorAlarmStatus_Type(Bits):namedValues=NamedValues(*((_f,0),(_g,1),(_Q,2),(_R,3),(_h,4),(_i,5)))
_SensorAlarmStatus_Type.__name__=_H
_SensorAlarmStatus_Object=MibTableColumn
sensorAlarmStatus=_SensorAlarmStatus_Object((1,3,6,1,4,1,29640,4,3,34,1,3),_SensorAlarmStatus_Type())
sensorAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorAlarmStatus.setStatus(_A)
_SensorValue_Type=Integer32
_SensorValue_Object=MibTableColumn
sensorValue=_SensorValue_Object((1,3,6,1,4,1,29640,4,3,34,1,4),_SensorValue_Type())
sensorValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorValue.setStatus(_A)
if mibBuilder.loadTexts:sensorValue.setUnits(_X)
class _SensorSwitchOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_T,0),(_U,1),(_V,2)))
_SensorSwitchOperStatus_Type.__name__=_E
_SensorSwitchOperStatus_Object=MibTableColumn
sensorSwitchOperStatus=_SensorSwitchOperStatus_Object((1,3,6,1,4,1,29640,4,3,34,1,5),_SensorSwitchOperStatus_Type())
sensorSwitchOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorSwitchOperStatus.setStatus(_A)
class _SensorSwitchAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_T,0),(_U,1),(_V,2)))
_SensorSwitchAdminStatus_Type.__name__=_E
_SensorSwitchAdminStatus_Object=MibTableColumn
sensorSwitchAdminStatus=_SensorSwitchAdminStatus_Object((1,3,6,1,4,1,29640,4,3,34,1,6),_SensorSwitchAdminStatus_Type())
sensorSwitchAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorSwitchAdminStatus.setStatus(_A)
_SensorHiThresh_Type=Integer32
_SensorHiThresh_Object=MibTableColumn
sensorHiThresh=_SensorHiThresh_Object((1,3,6,1,4,1,29640,4,3,34,1,7),_SensorHiThresh_Type())
sensorHiThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorHiThresh.setStatus(_A)
if mibBuilder.loadTexts:sensorHiThresh.setUnits(_X)
_SensorLoThresh_Type=Integer32
_SensorLoThresh_Object=MibTableColumn
sensorLoThresh=_SensorLoThresh_Object((1,3,6,1,4,1,29640,4,3,34,1,8),_SensorLoThresh_Type())
sensorLoThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorLoThresh.setStatus(_A)
if mibBuilder.loadTexts:sensorLoThresh.setUnits(_X)
class _SensorAlarmSelector_Type(Bits):namedValues=NamedValues(*((_f,0),(_g,1),(_Q,2),(_R,3),(_h,4),(_i,5)))
_SensorAlarmSelector_Type.__name__=_H
_SensorAlarmSelector_Object=MibTableColumn
sensorAlarmSelector=_SensorAlarmSelector_Object((1,3,6,1,4,1,29640,4,3,34,1,9),_SensorAlarmSelector_Type())
sensorAlarmSelector.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorAlarmSelector.setStatus(_A)
class _SensorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SensorName_Type.__name__=_G
_SensorName_Object=MibTableColumn
sensorName=_SensorName_Object((1,3,6,1,4,1,29640,4,3,34,1,10),_SensorName_Type())
sensorName.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorName.setStatus(_A)
_PduTraps_ObjectIdentity=ObjectIdentity
pduTraps=_PduTraps_ObjectIdentity((1,3,6,1,4,1,29640,4,4))
class _TrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('voltageHiAlarm',0),('voltageLoAlarm',1),('currentHiAlarm',2),('currentLoAlarm',3),('tempHiAlarm',4),('tempLoAlarm',5),('humidityHiAlarm',6),('humidityLoAlarm',7),('switchOnAlarm',8),('switchOffAlarm',9),('powerHiAlarm',10),('blackBoxColdTrap',11)))
_TrapType_Type.__name__=_E
_TrapType_Object=MibScalar
trapType=_TrapType_Object((1,3,6,1,4,1,29640,4,4,1),_TrapType_Type())
trapType.setMaxAccess(_N)
if mibBuilder.loadTexts:trapType.setStatus(_A)
class _PduTableType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('pduNodeTable',0),('pduSensorTable',1)))
_PduTableType_Type.__name__=_E
_PduTableType_Object=MibScalar
pduTableType=_PduTableType_Object((1,3,6,1,4,1,29640,4,4,2),_PduTableType_Type())
pduTableType.setMaxAccess(_N)
if mibBuilder.loadTexts:pduTableType.setStatus(_A)
_TrapTableIndex_Type=Integer32
_TrapTableIndex_Object=MibScalar
trapTableIndex=_TrapTableIndex_Object((1,3,6,1,4,1,29640,4,4,3),_TrapTableIndex_Type())
trapTableIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:trapTableIndex.setStatus(_A)
class _TrapThreshHoldType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('trapThresholdOther',0),('trapThresholdHi',1),('trapThresholdLo',2)))
_TrapThreshHoldType_Type.__name__=_E
_TrapThreshHoldType_Object=MibScalar
trapThreshHoldType=_TrapThreshHoldType_Object((1,3,6,1,4,1,29640,4,4,4),_TrapThreshHoldType_Type())
trapThreshHoldType.setMaxAccess(_N)
if mibBuilder.loadTexts:trapThreshHoldType.setStatus(_A)
_TrapThreshHold_Type=Integer32
_TrapThreshHold_Object=MibScalar
trapThreshHold=_TrapThreshHold_Object((1,3,6,1,4,1,29640,4,4,5),_TrapThreshHold_Type())
trapThreshHold.setMaxAccess(_N)
if mibBuilder.loadTexts:trapThreshHold.setStatus(_A)
_ApnlTest_ObjectIdentity=ObjectIdentity
apnlTest=_ApnlTest_ObjectIdentity((1,3,6,1,4,1,29640,5))
_ApnlDemo_ObjectIdentity=ObjectIdentity
apnlDemo=_ApnlDemo_ObjectIdentity((1,3,6,1,4,1,29640,6))
_ApnlMIBConformance_ObjectIdentity=ObjectIdentity
apnlMIBConformance=_ApnlMIBConformance_ObjectIdentity((1,3,6,1,4,1,29640,7))
pduVoltageAlarm=NotificationType((1,3,6,1,4,1,29640,4,4,6))
pduVoltageAlarm.setObjects(*((_D,_J),(_D,_K),(_D,_O),(_D,_P)))
if mibBuilder.loadTexts:pduVoltageAlarm.setStatus(_A)
pduCurrentAlarm=NotificationType((1,3,6,1,4,1,29640,4,4,7))
pduCurrentAlarm.setObjects(*((_D,_J),(_D,_K),(_D,_O),(_D,_P)))
if mibBuilder.loadTexts:pduCurrentAlarm.setStatus(_A)
pduPowerAlarm=NotificationType((1,3,6,1,4,1,29640,4,4,8))
pduPowerAlarm.setObjects(*((_D,_J),(_D,_K),(_D,_O),(_D,_P)))
if mibBuilder.loadTexts:pduPowerAlarm.setStatus(_A)
sensorAlarm=NotificationType((1,3,6,1,4,1,29640,4,4,9))
sensorAlarm.setObjects(*((_D,_J),(_D,_K),(_D,_O),(_D,_P)))
if mibBuilder.loadTexts:sensorAlarm.setStatus(_A)
pduSwitchAlarm=NotificationType((1,3,6,1,4,1,29640,4,4,10))
pduSwitchAlarm.setObjects(*((_D,_J),(_D,_K)))
if mibBuilder.loadTexts:pduSwitchAlarm.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'apNederland':apNederland,'apnlDirectory':apnlDirectory,'apnlMib':apnlMib,'apnlTmp':apnlTmp,'apnlModules':apnlModules,'cm':cm,'cmTraps':cmTraps,'pdu':pdu,'pduType':pduType,'pduProductIdentifier':pduProductIdentifier,'pduSerialNumber':pduSerialNumber,'pduStatus':pduStatus,'pduPower':pduPower,'pduPowerL1':pduPowerL1,'pduPowerL2':pduPowerL2,'pduPowerL3':pduPowerL3,'pduKvar':pduKvar,'pduKvarL1':pduKvarL1,'pduKvarL2':pduKvarL2,'pduKvarL3':pduKvarL3,'pdulAcurrent':pdulAcurrent,'pduAcurrentL1':pduAcurrentL1,'pduAcurrentL2':pduAcurrentL2,'pduAcurrentL3':pduAcurrentL3,'pduCurIpAddress':pduCurIpAddress,'pduCurSubNetMask':pduCurSubNetMask,'pduCurDefGwAddress':pduCurDefGwAddress,'pduNumberOfNodes':pduNumberOfNodes,'pduNumberOfSensors':pduNumberOfSensors,'pduSoftwareVersion':pduSoftwareVersion,'pduFirmwareVersion':pduFirmwareVersion,'pduBusProtocol':pduBusProtocol,'pduAdminCommand':pduAdminCommand,'pduStartupIpAddress':pduStartupIpAddress,'pduStartupSubNetMask':pduStartupSubNetMask,'pduStartupDefGwAddress':pduStartupDefGwAddress,'pduRealTimeClock':pduRealTimeClock,'pduEnableFeatures':pduEnableFeatures,'pduBusAddress':pduBusAddress,'pduName':pduName,'nodeTable':nodeTable,'nodeEntry':nodeEntry,_Y:nodeIndex,'nodeType':nodeType,'nodeOutlet':nodeOutlet,'nodeAlarmStatus':nodeAlarmStatus,'nodePower':nodePower,'nodeAcurrent':nodeAcurrent,'nodePeakCurrent':nodePeakCurrent,'nodeVoltage':nodeVoltage,'nodeMinVoltage':nodeMinVoltage,'nodeKvar':nodeKvar,'nodeFrequency':nodeFrequency,'nodePowerFactor':nodePowerFactor,'nodeSwitchOperStatus':nodeSwitchOperStatus,'nodeSwitchAdminStatus':nodeSwitchAdminStatus,'nodeCurrHiThresh':nodeCurrHiThresh,'nodeCurrLoThresh':nodeCurrLoThresh,'nodeVoltHiThresh':nodeVoltHiThresh,'nodeVoltLoThresh':nodeVoltLoThresh,'nodeAlarmSelector':nodeAlarmSelector,'nodeName':nodeName,'nodePhase':nodePhase,'sensorTable':sensorTable,'sensorEntry':sensorEntry,_e:sensorIndex,'sensorType':sensorType,'sensorAlarmStatus':sensorAlarmStatus,'sensorValue':sensorValue,'sensorSwitchOperStatus':sensorSwitchOperStatus,'sensorSwitchAdminStatus':sensorSwitchAdminStatus,'sensorHiThresh':sensorHiThresh,'sensorLoThresh':sensorLoThresh,'sensorAlarmSelector':sensorAlarmSelector,'sensorName':sensorName,'pduTraps':pduTraps,_J:trapType,'pduTableType':pduTableType,_K:trapTableIndex,_O:trapThreshHoldType,_P:trapThreshHold,'pduVoltageAlarm':pduVoltageAlarm,'pduCurrentAlarm':pduCurrentAlarm,'pduPowerAlarm':pduPowerAlarm,'sensorAlarm':sensorAlarm,'pduSwitchAlarm':pduSwitchAlarm,'apnlTest':apnlTest,'apnlDemo':apnlDemo,'apnlMIBConformance':apnlMIBConformance})