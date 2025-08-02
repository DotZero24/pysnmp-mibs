_Ad='ogOmBasicGroup'
_Ac='ogOmTempSensorValue'
_Ab='ogOmTempSensorDevice'
_Aa='ogOmTempSensorName'
_AZ='ogOmPowerSupplyOutputPower'
_AY='ogOmPowerSupplyOutputCurrent'
_AX='ogOmPowerSupplyInputVoltage'
_AW='ogOmPowerSupplyDevice'
_AV='ogOmPowerSupplyName'
_AU='ogOmEnrollmentStatus'
_AT='ogOmEnrollmentBundle'
_AS='ogOmEnrollmentPort'
_AR='ogOmEnrollmentAddress'
_AQ='ogOmCellUimRoamingOperatorName'
_AP='ogOmCellUimLastActiveTime'
_AO='ogOmCellUimLastUpdateTime'
_AN='ogOmCellUimSignalHealth'
_AM='ogOmCellUimConnectivityHealth'
_AL='ogOmCellUimRssi'
_AK='ogOmCellUimSignalQuality'
_AJ='ogOmCellUimApn'
_AI='ogOmCellUimOperatorName'
_AH='ogOmCellUimImsi'
_AG='ogOmCellUimIccid'
_AF='ogOmCellUimCardState'
_AE='ogOmCellUimSlotState'
_AD='ogOmCellUimPhysicalSlot'
_AC='ogOmCellularUimFailoverState'
_AB='ogOmCellularActiveUim'
_AA='ogOmCellularAccessTechnology'
_A9='ogOmCellularState'
_A8='ogOmCellularFirmware'
_A7='ogOmCellularEquipmentId'
_A6='ogOmCellularModel'
_A5='ogOmCellularVendor'
_A4='ogOmWebUserSourcePort'
_A3='ogOmWebUserSourceAddress'
_A2='ogOmWebUserName'
_A1='ogOmWebUserStartTime'
_A0='ogOmSerialUserName'
_z='ogOmSerialUserPortLabel'
_y='ogOmSerialUserPortNumber'
_x='ogOmSerialUserStartTime'
_w='ogOmSerialPortRTS'
_v='ogOmSerialPortCTS'
_u='ogOmSerialPortDSR'
_t='ogOmSerialPortDTR'
_s='ogOmSerialPortDCD'
_r='ogOmSerialPortBreaks'
_q='ogOmSerialPortOverrunErrors'
_p='ogOmSerialPortParityErrors'
_o='ogOmSerialPortFramingErrors'
_n='ogOmSerialPortTxBytes'
_m='ogOmSerialPortRxBytes'
_l='ogOmSerialPortLogLevel'
_k='ogOmSerialPortPinout'
_j='ogOmSerialPortMode'
_i='ogOmSerialPortFlowControl'
_h='ogOmSerialPortStopBits'
_g='ogOmSerialPortParity'
_f='ogOmSerialPortDataBits'
_e='ogOmSerialPortSpeed'
_d='ogOmSerialPortLabel'
_c='ogOmSerialPortCount'
_b='ogOmSystemModel'
_a='ogOmSystemVendor'
_Z='ogOmSystemFirmwareVersion'
_Y='ogOmSystemSerialNumber'
_X='ogOmSystemHostName'
_W='ogOmTempSensorIndex'
_V='ogOmPowerSupplyIndex'
_U='ogOmEnrollmentIndex'
_T='ogOmCellUimIndex'
_S='connected'
_R='registered'
_Q='enabled'
_P='failed'
_O='ogOmCellularIndex'
_N='ogOmWebUserIndex'
_M='ogOmSerialUserIndex'
_L='ogOmSerialPortIndex'
_K='disabled'
_J='off'
_I='on'
_H='unavailable'
_G='unknown'
_F='not-accessible'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='OG-OMTELEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ogMgmt,=mibBuilder.importSymbols('OG-SMI-MIB','ogMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'PhysAddress','TextualConvention')
ogOmTelem=ModuleIdentity((1,3,6,1,4,1,25049,10,19))
if mibBuilder.loadTexts:ogOmTelem.setRevisions(('2023-11-13 09:34','2021-03-12 14:54','2020-08-04 14:54'))
_OgOmSystem_ObjectIdentity=ObjectIdentity
ogOmSystem=_OgOmSystem_ObjectIdentity((1,3,6,1,4,1,25049,10,19,1))
class _OgOmSystemHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_OgOmSystemHostName_Type.__name__=_E
_OgOmSystemHostName_Object=MibScalar
ogOmSystemHostName=_OgOmSystemHostName_Object((1,3,6,1,4,1,25049,10,19,1,1),_OgOmSystemHostName_Type())
ogOmSystemHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSystemHostName.setStatus(_A)
class _OgOmSystemSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_OgOmSystemSerialNumber_Type.__name__=_E
_OgOmSystemSerialNumber_Object=MibScalar
ogOmSystemSerialNumber=_OgOmSystemSerialNumber_Object((1,3,6,1,4,1,25049,10,19,1,2),_OgOmSystemSerialNumber_Type())
ogOmSystemSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSystemSerialNumber.setStatus(_A)
class _OgOmSystemFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_OgOmSystemFirmwareVersion_Type.__name__=_E
_OgOmSystemFirmwareVersion_Object=MibScalar
ogOmSystemFirmwareVersion=_OgOmSystemFirmwareVersion_Object((1,3,6,1,4,1,25049,10,19,1,3),_OgOmSystemFirmwareVersion_Type())
ogOmSystemFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSystemFirmwareVersion.setStatus(_A)
class _OgOmSystemVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_OgOmSystemVendor_Type.__name__=_E
_OgOmSystemVendor_Object=MibScalar
ogOmSystemVendor=_OgOmSystemVendor_Object((1,3,6,1,4,1,25049,10,19,1,4),_OgOmSystemVendor_Type())
ogOmSystemVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSystemVendor.setStatus(_A)
class _OgOmSystemModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_OgOmSystemModel_Type.__name__=_E
_OgOmSystemModel_Object=MibScalar
ogOmSystemModel=_OgOmSystemModel_Object((1,3,6,1,4,1,25049,10,19,1,5),_OgOmSystemModel_Type())
ogOmSystemModel.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSystemModel.setStatus(_A)
_OgOmSerialPort_ObjectIdentity=ObjectIdentity
ogOmSerialPort=_OgOmSerialPort_ObjectIdentity((1,3,6,1,4,1,25049,10,19,2))
class _OgOmSerialPortCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgOmSerialPortCount_Type.__name__=_D
_OgOmSerialPortCount_Object=MibScalar
ogOmSerialPortCount=_OgOmSerialPortCount_Object((1,3,6,1,4,1,25049,10,19,2,1),_OgOmSerialPortCount_Type())
ogOmSerialPortCount.setMaxAccess('read-write')
if mibBuilder.loadTexts:ogOmSerialPortCount.setStatus(_A)
_OgOmSerialPortTable_Object=MibTable
ogOmSerialPortTable=_OgOmSerialPortTable_Object((1,3,6,1,4,1,25049,10,19,2,2))
if mibBuilder.loadTexts:ogOmSerialPortTable.setStatus(_A)
_OgOmSerialPortEntry_Object=MibTableRow
ogOmSerialPortEntry=_OgOmSerialPortEntry_Object((1,3,6,1,4,1,25049,10,19,2,2,1))
ogOmSerialPortEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:ogOmSerialPortEntry.setStatus(_A)
class _OgOmSerialPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgOmSerialPortIndex_Type.__name__=_D
_OgOmSerialPortIndex_Object=MibTableColumn
ogOmSerialPortIndex=_OgOmSerialPortIndex_Object((1,3,6,1,4,1,25049,10,19,2,2,1,1),_OgOmSerialPortIndex_Type())
ogOmSerialPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ogOmSerialPortIndex.setStatus(_A)
class _OgOmSerialPortLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_OgOmSerialPortLabel_Type.__name__=_E
_OgOmSerialPortLabel_Object=MibTableColumn
ogOmSerialPortLabel=_OgOmSerialPortLabel_Object((1,3,6,1,4,1,25049,10,19,2,2,1,2),_OgOmSerialPortLabel_Type())
ogOmSerialPortLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortLabel.setStatus(_A)
_OgOmSerialPortSpeed_Type=Integer32
_OgOmSerialPortSpeed_Object=MibTableColumn
ogOmSerialPortSpeed=_OgOmSerialPortSpeed_Object((1,3,6,1,4,1,25049,10,19,2,2,1,3),_OgOmSerialPortSpeed_Type())
ogOmSerialPortSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortSpeed.setStatus(_A)
_OgOmSerialPortDataBits_Type=Integer32
_OgOmSerialPortDataBits_Object=MibTableColumn
ogOmSerialPortDataBits=_OgOmSerialPortDataBits_Object((1,3,6,1,4,1,25049,10,19,2,2,1,4),_OgOmSerialPortDataBits_Type())
ogOmSerialPortDataBits.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortDataBits.setStatus(_A)
class _OgOmSerialPortParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('odd',2),('even',3),('mark',4),('space',5)))
_OgOmSerialPortParity_Type.__name__=_D
_OgOmSerialPortParity_Object=MibTableColumn
ogOmSerialPortParity=_OgOmSerialPortParity_Object((1,3,6,1,4,1,25049,10,19,2,2,1,5),_OgOmSerialPortParity_Type())
ogOmSerialPortParity.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortParity.setStatus(_A)
class _OgOmSerialPortStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('one',1),('two',2),('oneAndAHalf',3)))
_OgOmSerialPortStopBits_Type.__name__=_D
_OgOmSerialPortStopBits_Object=MibTableColumn
ogOmSerialPortStopBits=_OgOmSerialPortStopBits_Object((1,3,6,1,4,1,25049,10,19,2,2,1,6),_OgOmSerialPortStopBits_Type())
ogOmSerialPortStopBits.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortStopBits.setStatus(_A)
class _OgOmSerialPortFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('hardware',2),('software',3)))
_OgOmSerialPortFlowControl_Type.__name__=_D
_OgOmSerialPortFlowControl_Object=MibTableColumn
ogOmSerialPortFlowControl=_OgOmSerialPortFlowControl_Object((1,3,6,1,4,1,25049,10,19,2,2,1,7),_OgOmSerialPortFlowControl_Type())
ogOmSerialPortFlowControl.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortFlowControl.setStatus(_A)
class _OgOmSerialPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_K,1),('localConsole',2),('consoleServer',3),('bridge',4),('terminalServer',5),('reserved',6),('pduDevice',7),(_G,8)))
_OgOmSerialPortMode_Type.__name__=_D
_OgOmSerialPortMode_Object=MibTableColumn
ogOmSerialPortMode=_OgOmSerialPortMode_Object((1,3,6,1,4,1,25049,10,19,2,2,1,8),_OgOmSerialPortMode_Type())
ogOmSerialPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortMode.setStatus(_A)
class _OgOmSerialPortPinout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('x1',1),('x2',2),('usb',3)))
_OgOmSerialPortPinout_Type.__name__=_D
_OgOmSerialPortPinout_Object=MibTableColumn
ogOmSerialPortPinout=_OgOmSerialPortPinout_Object((1,3,6,1,4,1,25049,10,19,2,2,1,9),_OgOmSerialPortPinout_Type())
ogOmSerialPortPinout.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortPinout.setStatus(_A)
class _OgOmSerialPortLogLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('connect',2),('inputAndOutput',3),('inputOnly',4)))
_OgOmSerialPortLogLevel_Type.__name__=_D
_OgOmSerialPortLogLevel_Object=MibTableColumn
ogOmSerialPortLogLevel=_OgOmSerialPortLogLevel_Object((1,3,6,1,4,1,25049,10,19,2,2,1,10),_OgOmSerialPortLogLevel_Type())
ogOmSerialPortLogLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortLogLevel.setStatus(_A)
_OgOmSerialPortRxBytes_Type=Counter64
_OgOmSerialPortRxBytes_Object=MibTableColumn
ogOmSerialPortRxBytes=_OgOmSerialPortRxBytes_Object((1,3,6,1,4,1,25049,10,19,2,2,1,11),_OgOmSerialPortRxBytes_Type())
ogOmSerialPortRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortRxBytes.setStatus(_A)
_OgOmSerialPortTxBytes_Type=Counter64
_OgOmSerialPortTxBytes_Object=MibTableColumn
ogOmSerialPortTxBytes=_OgOmSerialPortTxBytes_Object((1,3,6,1,4,1,25049,10,19,2,2,1,12),_OgOmSerialPortTxBytes_Type())
ogOmSerialPortTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortTxBytes.setStatus(_A)
_OgOmSerialPortFramingErrors_Type=Counter64
_OgOmSerialPortFramingErrors_Object=MibTableColumn
ogOmSerialPortFramingErrors=_OgOmSerialPortFramingErrors_Object((1,3,6,1,4,1,25049,10,19,2,2,1,13),_OgOmSerialPortFramingErrors_Type())
ogOmSerialPortFramingErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortFramingErrors.setStatus(_A)
_OgOmSerialPortParityErrors_Type=Counter64
_OgOmSerialPortParityErrors_Object=MibTableColumn
ogOmSerialPortParityErrors=_OgOmSerialPortParityErrors_Object((1,3,6,1,4,1,25049,10,19,2,2,1,14),_OgOmSerialPortParityErrors_Type())
ogOmSerialPortParityErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortParityErrors.setStatus(_A)
_OgOmSerialPortOverrunErrors_Type=Counter64
_OgOmSerialPortOverrunErrors_Object=MibTableColumn
ogOmSerialPortOverrunErrors=_OgOmSerialPortOverrunErrors_Object((1,3,6,1,4,1,25049,10,19,2,2,1,15),_OgOmSerialPortOverrunErrors_Type())
ogOmSerialPortOverrunErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortOverrunErrors.setStatus(_A)
_OgOmSerialPortBreaks_Type=Counter64
_OgOmSerialPortBreaks_Object=MibTableColumn
ogOmSerialPortBreaks=_OgOmSerialPortBreaks_Object((1,3,6,1,4,1,25049,10,19,2,2,1,16),_OgOmSerialPortBreaks_Type())
ogOmSerialPortBreaks.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortBreaks.setStatus(_A)
class _OgOmSerialPortDCD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_I,1),(_J,2)))
_OgOmSerialPortDCD_Type.__name__=_D
_OgOmSerialPortDCD_Object=MibTableColumn
ogOmSerialPortDCD=_OgOmSerialPortDCD_Object((1,3,6,1,4,1,25049,10,19,2,2,1,17),_OgOmSerialPortDCD_Type())
ogOmSerialPortDCD.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortDCD.setStatus(_A)
class _OgOmSerialPortDTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_I,1),(_J,2)))
_OgOmSerialPortDTR_Type.__name__=_D
_OgOmSerialPortDTR_Object=MibTableColumn
ogOmSerialPortDTR=_OgOmSerialPortDTR_Object((1,3,6,1,4,1,25049,10,19,2,2,1,18),_OgOmSerialPortDTR_Type())
ogOmSerialPortDTR.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortDTR.setStatus(_A)
class _OgOmSerialPortDSR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_I,1),(_J,2)))
_OgOmSerialPortDSR_Type.__name__=_D
_OgOmSerialPortDSR_Object=MibTableColumn
ogOmSerialPortDSR=_OgOmSerialPortDSR_Object((1,3,6,1,4,1,25049,10,19,2,2,1,19),_OgOmSerialPortDSR_Type())
ogOmSerialPortDSR.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortDSR.setStatus(_A)
class _OgOmSerialPortCTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_I,1),(_J,2)))
_OgOmSerialPortCTS_Type.__name__=_D
_OgOmSerialPortCTS_Object=MibTableColumn
ogOmSerialPortCTS=_OgOmSerialPortCTS_Object((1,3,6,1,4,1,25049,10,19,2,2,1,20),_OgOmSerialPortCTS_Type())
ogOmSerialPortCTS.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortCTS.setStatus(_A)
class _OgOmSerialPortRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_I,1),(_J,2)))
_OgOmSerialPortRTS_Type.__name__=_D
_OgOmSerialPortRTS_Object=MibTableColumn
ogOmSerialPortRTS=_OgOmSerialPortRTS_Object((1,3,6,1,4,1,25049,10,19,2,2,1,21),_OgOmSerialPortRTS_Type())
ogOmSerialPortRTS.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialPortRTS.setStatus(_A)
_OgOmSerialUser_ObjectIdentity=ObjectIdentity
ogOmSerialUser=_OgOmSerialUser_ObjectIdentity((1,3,6,1,4,1,25049,10,19,3))
_OgOmSerialUserTable_Object=MibTable
ogOmSerialUserTable=_OgOmSerialUserTable_Object((1,3,6,1,4,1,25049,10,19,3,1))
if mibBuilder.loadTexts:ogOmSerialUserTable.setStatus(_A)
_OgOmSerialUserEntry_Object=MibTableRow
ogOmSerialUserEntry=_OgOmSerialUserEntry_Object((1,3,6,1,4,1,25049,10,19,3,1,1))
ogOmSerialUserEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:ogOmSerialUserEntry.setStatus(_A)
class _OgOmSerialUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgOmSerialUserIndex_Type.__name__=_D
_OgOmSerialUserIndex_Object=MibTableColumn
ogOmSerialUserIndex=_OgOmSerialUserIndex_Object((1,3,6,1,4,1,25049,10,19,3,1,1,1),_OgOmSerialUserIndex_Type())
ogOmSerialUserIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ogOmSerialUserIndex.setStatus(_A)
_OgOmSerialUserStartTime_Type=DateAndTime
_OgOmSerialUserStartTime_Object=MibTableColumn
ogOmSerialUserStartTime=_OgOmSerialUserStartTime_Object((1,3,6,1,4,1,25049,10,19,3,1,1,2),_OgOmSerialUserStartTime_Type())
ogOmSerialUserStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialUserStartTime.setStatus(_A)
_OgOmSerialUserPortNumber_Type=Integer32
_OgOmSerialUserPortNumber_Object=MibTableColumn
ogOmSerialUserPortNumber=_OgOmSerialUserPortNumber_Object((1,3,6,1,4,1,25049,10,19,3,1,1,3),_OgOmSerialUserPortNumber_Type())
ogOmSerialUserPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialUserPortNumber.setStatus(_A)
class _OgOmSerialUserPortLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_OgOmSerialUserPortLabel_Type.__name__=_E
_OgOmSerialUserPortLabel_Object=MibTableColumn
ogOmSerialUserPortLabel=_OgOmSerialUserPortLabel_Object((1,3,6,1,4,1,25049,10,19,3,1,1,4),_OgOmSerialUserPortLabel_Type())
ogOmSerialUserPortLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialUserPortLabel.setStatus(_A)
class _OgOmSerialUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_OgOmSerialUserName_Type.__name__=_E
_OgOmSerialUserName_Object=MibTableColumn
ogOmSerialUserName=_OgOmSerialUserName_Object((1,3,6,1,4,1,25049,10,19,3,1,1,5),_OgOmSerialUserName_Type())
ogOmSerialUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmSerialUserName.setStatus(_A)
_OgOmWebUser_ObjectIdentity=ObjectIdentity
ogOmWebUser=_OgOmWebUser_ObjectIdentity((1,3,6,1,4,1,25049,10,19,4))
_OgOmWebUserTable_Object=MibTable
ogOmWebUserTable=_OgOmWebUserTable_Object((1,3,6,1,4,1,25049,10,19,4,1))
if mibBuilder.loadTexts:ogOmWebUserTable.setStatus(_A)
_OgOmWebUserEntry_Object=MibTableRow
ogOmWebUserEntry=_OgOmWebUserEntry_Object((1,3,6,1,4,1,25049,10,19,4,1,1))
ogOmWebUserEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:ogOmWebUserEntry.setStatus(_A)
class _OgOmWebUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgOmWebUserIndex_Type.__name__=_D
_OgOmWebUserIndex_Object=MibTableColumn
ogOmWebUserIndex=_OgOmWebUserIndex_Object((1,3,6,1,4,1,25049,10,19,4,1,1,1),_OgOmWebUserIndex_Type())
ogOmWebUserIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ogOmWebUserIndex.setStatus(_A)
_OgOmWebUserStartTime_Type=DateAndTime
_OgOmWebUserStartTime_Object=MibTableColumn
ogOmWebUserStartTime=_OgOmWebUserStartTime_Object((1,3,6,1,4,1,25049,10,19,4,1,1,2),_OgOmWebUserStartTime_Type())
ogOmWebUserStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmWebUserStartTime.setStatus(_A)
class _OgOmWebUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_OgOmWebUserName_Type.__name__=_E
_OgOmWebUserName_Object=MibTableColumn
ogOmWebUserName=_OgOmWebUserName_Object((1,3,6,1,4,1,25049,10,19,4,1,1,3),_OgOmWebUserName_Type())
ogOmWebUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmWebUserName.setStatus(_A)
class _OgOmWebUserSourceAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_OgOmWebUserSourceAddress_Type.__name__=_E
_OgOmWebUserSourceAddress_Object=MibTableColumn
ogOmWebUserSourceAddress=_OgOmWebUserSourceAddress_Object((1,3,6,1,4,1,25049,10,19,4,1,1,4),_OgOmWebUserSourceAddress_Type())
ogOmWebUserSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmWebUserSourceAddress.setStatus(_A)
class _OgOmWebUserSourcePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgOmWebUserSourcePort_Type.__name__=_D
_OgOmWebUserSourcePort_Object=MibTableColumn
ogOmWebUserSourcePort=_OgOmWebUserSourcePort_Object((1,3,6,1,4,1,25049,10,19,4,1,1,5),_OgOmWebUserSourcePort_Type())
ogOmWebUserSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmWebUserSourcePort.setStatus(_A)
_OgOmCellular_ObjectIdentity=ObjectIdentity
ogOmCellular=_OgOmCellular_ObjectIdentity((1,3,6,1,4,1,25049,10,19,5))
_OgOmCellularTable_Object=MibTable
ogOmCellularTable=_OgOmCellularTable_Object((1,3,6,1,4,1,25049,10,19,5,1))
if mibBuilder.loadTexts:ogOmCellularTable.setStatus(_A)
_OgOmCellularEntry_Object=MibTableRow
ogOmCellularEntry=_OgOmCellularEntry_Object((1,3,6,1,4,1,25049,10,19,5,1,1))
ogOmCellularEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:ogOmCellularEntry.setStatus(_A)
class _OgOmCellularIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgOmCellularIndex_Type.__name__=_D
_OgOmCellularIndex_Object=MibTableColumn
ogOmCellularIndex=_OgOmCellularIndex_Object((1,3,6,1,4,1,25049,10,19,5,1,1,1),_OgOmCellularIndex_Type())
ogOmCellularIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ogOmCellularIndex.setStatus(_A)
class _OgOmCellularVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OgOmCellularVendor_Type.__name__=_E
_OgOmCellularVendor_Object=MibTableColumn
ogOmCellularVendor=_OgOmCellularVendor_Object((1,3,6,1,4,1,25049,10,19,5,1,1,2),_OgOmCellularVendor_Type())
ogOmCellularVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellularVendor.setStatus(_A)
class _OgOmCellularModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OgOmCellularModel_Type.__name__=_E
_OgOmCellularModel_Object=MibTableColumn
ogOmCellularModel=_OgOmCellularModel_Object((1,3,6,1,4,1,25049,10,19,5,1,1,3),_OgOmCellularModel_Type())
ogOmCellularModel.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellularModel.setStatus(_A)
class _OgOmCellularEquipmentId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OgOmCellularEquipmentId_Type.__name__=_E
_OgOmCellularEquipmentId_Object=MibTableColumn
ogOmCellularEquipmentId=_OgOmCellularEquipmentId_Object((1,3,6,1,4,1,25049,10,19,5,1,1,4),_OgOmCellularEquipmentId_Type())
ogOmCellularEquipmentId.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellularEquipmentId.setStatus(_A)
class _OgOmCellularFirmware_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OgOmCellularFirmware_Type.__name__=_E
_OgOmCellularFirmware_Object=MibTableColumn
ogOmCellularFirmware=_OgOmCellularFirmware_Object((1,3,6,1,4,1,25049,10,19,5,1,1,5),_OgOmCellularFirmware_Type())
ogOmCellularFirmware.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellularFirmware.setStatus(_A)
class _OgOmCellularState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_P,1),(_G,2),('initializing',3),('locked',4),(_K,5),('disabling',6),('enabling',7),(_Q,8),('searching',9),(_R,10),('disconnecting',11),('connecting',12),(_S,13)))
_OgOmCellularState_Type.__name__=_D
_OgOmCellularState_Object=MibTableColumn
ogOmCellularState=_OgOmCellularState_Object((1,3,6,1,4,1,25049,10,19,5,1,1,6),_OgOmCellularState_Type())
ogOmCellularState.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellularState.setStatus(_A)
class _OgOmCellularAccessTechnology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_H,1),('cdma',2),('evdo',3),('gsm',4),('umts',5),('lte',6),('gsmUmts',7),('gsmUmtsLte',8),('cdmaEvdo',9),('cdmaEvdoLte',10),('lteNr5g',11),('nr5g',12)))
_OgOmCellularAccessTechnology_Type.__name__=_D
_OgOmCellularAccessTechnology_Object=MibTableColumn
ogOmCellularAccessTechnology=_OgOmCellularAccessTechnology_Object((1,3,6,1,4,1,25049,10,19,5,1,1,7),_OgOmCellularAccessTechnology_Type())
ogOmCellularAccessTechnology.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellularAccessTechnology.setStatus(_A)
_OgOmCellularActiveUim_Type=Counter32
_OgOmCellularActiveUim_Object=MibTableColumn
ogOmCellularActiveUim=_OgOmCellularActiveUim_Object((1,3,6,1,4,1,25049,10,19,5,1,1,8),_OgOmCellularActiveUim_Type())
ogOmCellularActiveUim.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellularActiveUim.setStatus(_A)
class _OgOmCellularUimFailoverState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),(_K,2),(_Q,3),('failingOver',4),('failedOver',5),('failingBack',6)))
_OgOmCellularUimFailoverState_Type.__name__=_D
_OgOmCellularUimFailoverState_Object=MibTableColumn
ogOmCellularUimFailoverState=_OgOmCellularUimFailoverState_Object((1,3,6,1,4,1,25049,10,19,5,1,1,9),_OgOmCellularUimFailoverState_Type())
ogOmCellularUimFailoverState.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellularUimFailoverState.setStatus(_A)
_OgOmCellUim_ObjectIdentity=ObjectIdentity
ogOmCellUim=_OgOmCellUim_ObjectIdentity((1,3,6,1,4,1,25049,10,19,6))
_OgOmCellUimTable_Object=MibTable
ogOmCellUimTable=_OgOmCellUimTable_Object((1,3,6,1,4,1,25049,10,19,6,1))
if mibBuilder.loadTexts:ogOmCellUimTable.setStatus(_A)
_OgOmCellUimEntry_Object=MibTableRow
ogOmCellUimEntry=_OgOmCellUimEntry_Object((1,3,6,1,4,1,25049,10,19,6,1,1))
ogOmCellUimEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:ogOmCellUimEntry.setStatus(_A)
class _OgOmCellUimIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgOmCellUimIndex_Type.__name__=_D
_OgOmCellUimIndex_Object=MibTableColumn
ogOmCellUimIndex=_OgOmCellUimIndex_Object((1,3,6,1,4,1,25049,10,19,6,1,1,1),_OgOmCellUimIndex_Type())
ogOmCellUimIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ogOmCellUimIndex.setStatus(_A)
_OgOmCellUimPhysicalSlot_Type=Counter32
_OgOmCellUimPhysicalSlot_Object=MibTableColumn
ogOmCellUimPhysicalSlot=_OgOmCellUimPhysicalSlot_Object((1,3,6,1,4,1,25049,10,19,6,1,1,2),_OgOmCellUimPhysicalSlot_Type())
ogOmCellUimPhysicalSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellUimPhysicalSlot.setStatus(_A)
class _OgOmCellUimSlotState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('inactive',2),('active',3)))
_OgOmCellUimSlotState_Type.__name__=_D
_OgOmCellUimSlotState_Object=MibTableColumn
ogOmCellUimSlotState=_OgOmCellUimSlotState_Object((1,3,6,1,4,1,25049,10,19,6,1,1,3),_OgOmCellUimSlotState_Type())
ogOmCellUimSlotState.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellUimSlotState.setStatus(_A)
class _OgOmCellUimCardState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('absent',2),('present',3)))
_OgOmCellUimCardState_Type.__name__=_D
_OgOmCellUimCardState_Object=MibTableColumn
ogOmCellUimCardState=_OgOmCellUimCardState_Object((1,3,6,1,4,1,25049,10,19,6,1,1,4),_OgOmCellUimCardState_Type())
ogOmCellUimCardState.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellUimCardState.setStatus(_A)
class _OgOmCellUimIccid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OgOmCellUimIccid_Type.__name__=_E
_OgOmCellUimIccid_Object=MibTableColumn
ogOmCellUimIccid=_OgOmCellUimIccid_Object((1,3,6,1,4,1,25049,10,19,6,1,1,5),_OgOmCellUimIccid_Type())
ogOmCellUimIccid.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellUimIccid.setStatus(_A)
class _OgOmCellUimImsi_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OgOmCellUimImsi_Type.__name__=_E
_OgOmCellUimImsi_Object=MibTableColumn
ogOmCellUimImsi=_OgOmCellUimImsi_Object((1,3,6,1,4,1,25049,10,19,6,1,1,6),_OgOmCellUimImsi_Type())
ogOmCellUimImsi.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellUimImsi.setStatus(_A)
class _OgOmCellUimOperatorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OgOmCellUimOperatorName_Type.__name__=_E
_OgOmCellUimOperatorName_Object=MibTableColumn
ogOmCellUimOperatorName=_OgOmCellUimOperatorName_Object((1,3,6,1,4,1,25049,10,19,6,1,1,7),_OgOmCellUimOperatorName_Type())
ogOmCellUimOperatorName.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellUimOperatorName.setStatus(_A)
class _OgOmCellUimApn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OgOmCellUimApn_Type.__name__=_E
_OgOmCellUimApn_Object=MibTableColumn
ogOmCellUimApn=_OgOmCellUimApn_Object((1,3,6,1,4,1,25049,10,19,6,1,1,8),_OgOmCellUimApn_Type())
ogOmCellUimApn.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellUimApn.setStatus(_A)
class _OgOmCellUimSignalQuality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_OgOmCellUimSignalQuality_Type.__name__=_D
_OgOmCellUimSignalQuality_Object=MibTableColumn
ogOmCellUimSignalQuality=_OgOmCellUimSignalQuality_Object((1,3,6,1,4,1,25049,10,19,6,1,1,9),_OgOmCellUimSignalQuality_Type())
ogOmCellUimSignalQuality.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellUimSignalQuality.setStatus(_A)
class _OgOmCellUimRssi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-99,99))
_OgOmCellUimRssi_Type.__name__=_D
_OgOmCellUimRssi_Object=MibTableColumn
ogOmCellUimRssi=_OgOmCellUimRssi_Object((1,3,6,1,4,1,25049,10,19,6,1,1,10),_OgOmCellUimRssi_Type())
ogOmCellUimRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellUimRssi.setStatus(_A)
class _OgOmCellUimConnectivityHealth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('bad',2),('good',3)))
_OgOmCellUimConnectivityHealth_Type.__name__=_D
_OgOmCellUimConnectivityHealth_Object=MibTableColumn
ogOmCellUimConnectivityHealth=_OgOmCellUimConnectivityHealth_Object((1,3,6,1,4,1,25049,10,19,6,1,1,11),_OgOmCellUimConnectivityHealth_Type())
ogOmCellUimConnectivityHealth.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellUimConnectivityHealth.setStatus(_A)
class _OgOmCellUimSignalHealth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('bad',2),('moderate',3),('good',4)))
_OgOmCellUimSignalHealth_Type.__name__=_D
_OgOmCellUimSignalHealth_Object=MibTableColumn
ogOmCellUimSignalHealth=_OgOmCellUimSignalHealth_Object((1,3,6,1,4,1,25049,10,19,6,1,1,12),_OgOmCellUimSignalHealth_Type())
ogOmCellUimSignalHealth.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellUimSignalHealth.setStatus(_A)
_OgOmCellUimLastUpdateTime_Type=DateAndTime
_OgOmCellUimLastUpdateTime_Object=MibTableColumn
ogOmCellUimLastUpdateTime=_OgOmCellUimLastUpdateTime_Object((1,3,6,1,4,1,25049,10,19,6,1,1,13),_OgOmCellUimLastUpdateTime_Type())
ogOmCellUimLastUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellUimLastUpdateTime.setStatus(_A)
_OgOmCellUimLastActiveTime_Type=DateAndTime
_OgOmCellUimLastActiveTime_Object=MibTableColumn
ogOmCellUimLastActiveTime=_OgOmCellUimLastActiveTime_Object((1,3,6,1,4,1,25049,10,19,6,1,1,14),_OgOmCellUimLastActiveTime_Type())
ogOmCellUimLastActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellUimLastActiveTime.setStatus(_A)
class _OgOmCellUimRoamingOperatorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OgOmCellUimRoamingOperatorName_Type.__name__=_E
_OgOmCellUimRoamingOperatorName_Object=MibTableColumn
ogOmCellUimRoamingOperatorName=_OgOmCellUimRoamingOperatorName_Object((1,3,6,1,4,1,25049,10,19,6,1,1,15),_OgOmCellUimRoamingOperatorName_Type())
ogOmCellUimRoamingOperatorName.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmCellUimRoamingOperatorName.setStatus(_A)
_OgOmEnrollment_ObjectIdentity=ObjectIdentity
ogOmEnrollment=_OgOmEnrollment_ObjectIdentity((1,3,6,1,4,1,25049,10,19,7))
_OgOmEnrollmentTable_Object=MibTable
ogOmEnrollmentTable=_OgOmEnrollmentTable_Object((1,3,6,1,4,1,25049,10,19,7,1))
if mibBuilder.loadTexts:ogOmEnrollmentTable.setStatus(_A)
_OgOmEnrollmentEntry_Object=MibTableRow
ogOmEnrollmentEntry=_OgOmEnrollmentEntry_Object((1,3,6,1,4,1,25049,10,19,7,1,1))
ogOmEnrollmentEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:ogOmEnrollmentEntry.setStatus(_A)
class _OgOmEnrollmentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgOmEnrollmentIndex_Type.__name__=_D
_OgOmEnrollmentIndex_Object=MibTableColumn
ogOmEnrollmentIndex=_OgOmEnrollmentIndex_Object((1,3,6,1,4,1,25049,10,19,7,1,1,1),_OgOmEnrollmentIndex_Type())
ogOmEnrollmentIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ogOmEnrollmentIndex.setStatus(_A)
class _OgOmEnrollmentAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_OgOmEnrollmentAddress_Type.__name__=_E
_OgOmEnrollmentAddress_Object=MibTableColumn
ogOmEnrollmentAddress=_OgOmEnrollmentAddress_Object((1,3,6,1,4,1,25049,10,19,7,1,1,2),_OgOmEnrollmentAddress_Type())
ogOmEnrollmentAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmEnrollmentAddress.setStatus(_A)
class _OgOmEnrollmentPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgOmEnrollmentPort_Type.__name__=_D
_OgOmEnrollmentPort_Object=MibTableColumn
ogOmEnrollmentPort=_OgOmEnrollmentPort_Object((1,3,6,1,4,1,25049,10,19,7,1,1,3),_OgOmEnrollmentPort_Type())
ogOmEnrollmentPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmEnrollmentPort.setStatus(_A)
class _OgOmEnrollmentBundle_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_OgOmEnrollmentBundle_Type.__name__=_E
_OgOmEnrollmentBundle_Object=MibTableColumn
ogOmEnrollmentBundle=_OgOmEnrollmentBundle_Object((1,3,6,1,4,1,25049,10,19,7,1,1,4),_OgOmEnrollmentBundle_Type())
ogOmEnrollmentBundle.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmEnrollmentBundle.setStatus(_A)
class _OgOmEnrollmentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('enrolling',2),(_S,3),('disconnected',4),(_R,5),(_P,6)))
_OgOmEnrollmentStatus_Type.__name__=_D
_OgOmEnrollmentStatus_Object=MibTableColumn
ogOmEnrollmentStatus=_OgOmEnrollmentStatus_Object((1,3,6,1,4,1,25049,10,19,7,1,1,5),_OgOmEnrollmentStatus_Type())
ogOmEnrollmentStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmEnrollmentStatus.setStatus(_A)
_OgOmPowerSupply_ObjectIdentity=ObjectIdentity
ogOmPowerSupply=_OgOmPowerSupply_ObjectIdentity((1,3,6,1,4,1,25049,10,19,8))
_OgOmPowerSupplyTable_Object=MibTable
ogOmPowerSupplyTable=_OgOmPowerSupplyTable_Object((1,3,6,1,4,1,25049,10,19,8,1))
if mibBuilder.loadTexts:ogOmPowerSupplyTable.setStatus(_A)
_OgOmPowerSupplyEntry_Object=MibTableRow
ogOmPowerSupplyEntry=_OgOmPowerSupplyEntry_Object((1,3,6,1,4,1,25049,10,19,8,1,1))
ogOmPowerSupplyEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:ogOmPowerSupplyEntry.setStatus(_A)
class _OgOmPowerSupplyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgOmPowerSupplyIndex_Type.__name__=_D
_OgOmPowerSupplyIndex_Object=MibTableColumn
ogOmPowerSupplyIndex=_OgOmPowerSupplyIndex_Object((1,3,6,1,4,1,25049,10,19,8,1,1,1),_OgOmPowerSupplyIndex_Type())
ogOmPowerSupplyIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ogOmPowerSupplyIndex.setStatus(_A)
class _OgOmPowerSupplyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OgOmPowerSupplyName_Type.__name__=_E
_OgOmPowerSupplyName_Object=MibTableColumn
ogOmPowerSupplyName=_OgOmPowerSupplyName_Object((1,3,6,1,4,1,25049,10,19,8,1,1,2),_OgOmPowerSupplyName_Type())
ogOmPowerSupplyName.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmPowerSupplyName.setStatus(_A)
class _OgOmPowerSupplyDevice_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OgOmPowerSupplyDevice_Type.__name__=_E
_OgOmPowerSupplyDevice_Object=MibTableColumn
ogOmPowerSupplyDevice=_OgOmPowerSupplyDevice_Object((1,3,6,1,4,1,25049,10,19,8,1,1,3),_OgOmPowerSupplyDevice_Type())
ogOmPowerSupplyDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmPowerSupplyDevice.setStatus(_A)
_OgOmPowerSupplyInputVoltage_Type=Integer32
_OgOmPowerSupplyInputVoltage_Object=MibTableColumn
ogOmPowerSupplyInputVoltage=_OgOmPowerSupplyInputVoltage_Object((1,3,6,1,4,1,25049,10,19,8,1,1,4),_OgOmPowerSupplyInputVoltage_Type())
ogOmPowerSupplyInputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmPowerSupplyInputVoltage.setStatus(_A)
if mibBuilder.loadTexts:ogOmPowerSupplyInputVoltage.setUnits('0.001 volts')
_OgOmPowerSupplyOutputCurrent_Type=Integer32
_OgOmPowerSupplyOutputCurrent_Object=MibTableColumn
ogOmPowerSupplyOutputCurrent=_OgOmPowerSupplyOutputCurrent_Object((1,3,6,1,4,1,25049,10,19,8,1,1,5),_OgOmPowerSupplyOutputCurrent_Type())
ogOmPowerSupplyOutputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmPowerSupplyOutputCurrent.setStatus(_A)
if mibBuilder.loadTexts:ogOmPowerSupplyOutputCurrent.setUnits('0.001 Amps')
_OgOmPowerSupplyOutputPower_Type=Integer32
_OgOmPowerSupplyOutputPower_Object=MibTableColumn
ogOmPowerSupplyOutputPower=_OgOmPowerSupplyOutputPower_Object((1,3,6,1,4,1,25049,10,19,8,1,1,6),_OgOmPowerSupplyOutputPower_Type())
ogOmPowerSupplyOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmPowerSupplyOutputPower.setStatus(_A)
if mibBuilder.loadTexts:ogOmPowerSupplyOutputPower.setUnits('Watts')
_OgOmTempSensor_ObjectIdentity=ObjectIdentity
ogOmTempSensor=_OgOmTempSensor_ObjectIdentity((1,3,6,1,4,1,25049,10,19,9))
_OgOmTempSensorTable_Object=MibTable
ogOmTempSensorTable=_OgOmTempSensorTable_Object((1,3,6,1,4,1,25049,10,19,9,1))
if mibBuilder.loadTexts:ogOmTempSensorTable.setStatus(_A)
_OgOmTempSensorEntry_Object=MibTableRow
ogOmTempSensorEntry=_OgOmTempSensorEntry_Object((1,3,6,1,4,1,25049,10,19,9,1,1))
ogOmTempSensorEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:ogOmTempSensorEntry.setStatus(_A)
class _OgOmTempSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgOmTempSensorIndex_Type.__name__=_D
_OgOmTempSensorIndex_Object=MibTableColumn
ogOmTempSensorIndex=_OgOmTempSensorIndex_Object((1,3,6,1,4,1,25049,10,19,9,1,1,1),_OgOmTempSensorIndex_Type())
ogOmTempSensorIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ogOmTempSensorIndex.setStatus(_A)
class _OgOmTempSensorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OgOmTempSensorName_Type.__name__=_E
_OgOmTempSensorName_Object=MibTableColumn
ogOmTempSensorName=_OgOmTempSensorName_Object((1,3,6,1,4,1,25049,10,19,9,1,1,2),_OgOmTempSensorName_Type())
ogOmTempSensorName.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmTempSensorName.setStatus(_A)
class _OgOmTempSensorDevice_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OgOmTempSensorDevice_Type.__name__=_E
_OgOmTempSensorDevice_Object=MibTableColumn
ogOmTempSensorDevice=_OgOmTempSensorDevice_Object((1,3,6,1,4,1,25049,10,19,9,1,1,3),_OgOmTempSensorDevice_Type())
ogOmTempSensorDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmTempSensorDevice.setStatus(_A)
_OgOmTempSensorValue_Type=Integer32
_OgOmTempSensorValue_Object=MibTableColumn
ogOmTempSensorValue=_OgOmTempSensorValue_Object((1,3,6,1,4,1,25049,10,19,9,1,1,4),_OgOmTempSensorValue_Type())
ogOmTempSensorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOmTempSensorValue.setStatus(_A)
if mibBuilder.loadTexts:ogOmTempSensorValue.setUnits('millidegrees Celsius')
_OgOmConformance_ObjectIdentity=ObjectIdentity
ogOmConformance=_OgOmConformance_ObjectIdentity((1,3,6,1,4,1,25049,10,19,65535))
_OgOmCompliances_ObjectIdentity=ObjectIdentity
ogOmCompliances=_OgOmCompliances_ObjectIdentity((1,3,6,1,4,1,25049,10,19,65535,1))
_OgOmGroups_ObjectIdentity=ObjectIdentity
ogOmGroups=_OgOmGroups_ObjectIdentity((1,3,6,1,4,1,25049,10,19,65535,2))
ogOmBasicGroup=ObjectGroup((1,3,6,1,4,1,25049,10,19,65535,2,1))
ogOmBasicGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac)))
if mibBuilder.loadTexts:ogOmBasicGroup.setStatus(_A)
ogOmCompliance=ModuleCompliance((1,3,6,1,4,1,25049,10,19,65535,1,1))
ogOmCompliance.setObjects((_B,_Ad))
if mibBuilder.loadTexts:ogOmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ogOmTelem':ogOmTelem,'ogOmSystem':ogOmSystem,_X:ogOmSystemHostName,_Y:ogOmSystemSerialNumber,_Z:ogOmSystemFirmwareVersion,_a:ogOmSystemVendor,_b:ogOmSystemModel,'ogOmSerialPort':ogOmSerialPort,_c:ogOmSerialPortCount,'ogOmSerialPortTable':ogOmSerialPortTable,'ogOmSerialPortEntry':ogOmSerialPortEntry,_L:ogOmSerialPortIndex,_d:ogOmSerialPortLabel,_e:ogOmSerialPortSpeed,_f:ogOmSerialPortDataBits,_g:ogOmSerialPortParity,_h:ogOmSerialPortStopBits,_i:ogOmSerialPortFlowControl,_j:ogOmSerialPortMode,_k:ogOmSerialPortPinout,_l:ogOmSerialPortLogLevel,_m:ogOmSerialPortRxBytes,_n:ogOmSerialPortTxBytes,_o:ogOmSerialPortFramingErrors,_p:ogOmSerialPortParityErrors,_q:ogOmSerialPortOverrunErrors,_r:ogOmSerialPortBreaks,_s:ogOmSerialPortDCD,_t:ogOmSerialPortDTR,_u:ogOmSerialPortDSR,_v:ogOmSerialPortCTS,_w:ogOmSerialPortRTS,'ogOmSerialUser':ogOmSerialUser,'ogOmSerialUserTable':ogOmSerialUserTable,'ogOmSerialUserEntry':ogOmSerialUserEntry,_M:ogOmSerialUserIndex,_x:ogOmSerialUserStartTime,_y:ogOmSerialUserPortNumber,_z:ogOmSerialUserPortLabel,_A0:ogOmSerialUserName,'ogOmWebUser':ogOmWebUser,'ogOmWebUserTable':ogOmWebUserTable,'ogOmWebUserEntry':ogOmWebUserEntry,_N:ogOmWebUserIndex,_A1:ogOmWebUserStartTime,_A2:ogOmWebUserName,_A3:ogOmWebUserSourceAddress,_A4:ogOmWebUserSourcePort,'ogOmCellular':ogOmCellular,'ogOmCellularTable':ogOmCellularTable,'ogOmCellularEntry':ogOmCellularEntry,_O:ogOmCellularIndex,_A5:ogOmCellularVendor,_A6:ogOmCellularModel,_A7:ogOmCellularEquipmentId,_A8:ogOmCellularFirmware,_A9:ogOmCellularState,_AA:ogOmCellularAccessTechnology,_AB:ogOmCellularActiveUim,_AC:ogOmCellularUimFailoverState,'ogOmCellUim':ogOmCellUim,'ogOmCellUimTable':ogOmCellUimTable,'ogOmCellUimEntry':ogOmCellUimEntry,_T:ogOmCellUimIndex,_AD:ogOmCellUimPhysicalSlot,_AE:ogOmCellUimSlotState,_AF:ogOmCellUimCardState,_AG:ogOmCellUimIccid,_AH:ogOmCellUimImsi,_AI:ogOmCellUimOperatorName,_AJ:ogOmCellUimApn,_AK:ogOmCellUimSignalQuality,_AL:ogOmCellUimRssi,_AM:ogOmCellUimConnectivityHealth,_AN:ogOmCellUimSignalHealth,_AO:ogOmCellUimLastUpdateTime,_AP:ogOmCellUimLastActiveTime,_AQ:ogOmCellUimRoamingOperatorName,'ogOmEnrollment':ogOmEnrollment,'ogOmEnrollmentTable':ogOmEnrollmentTable,'ogOmEnrollmentEntry':ogOmEnrollmentEntry,_U:ogOmEnrollmentIndex,_AR:ogOmEnrollmentAddress,_AS:ogOmEnrollmentPort,_AT:ogOmEnrollmentBundle,_AU:ogOmEnrollmentStatus,'ogOmPowerSupply':ogOmPowerSupply,'ogOmPowerSupplyTable':ogOmPowerSupplyTable,'ogOmPowerSupplyEntry':ogOmPowerSupplyEntry,_V:ogOmPowerSupplyIndex,_AV:ogOmPowerSupplyName,_AW:ogOmPowerSupplyDevice,_AX:ogOmPowerSupplyInputVoltage,_AY:ogOmPowerSupplyOutputCurrent,_AZ:ogOmPowerSupplyOutputPower,'ogOmTempSensor':ogOmTempSensor,'ogOmTempSensorTable':ogOmTempSensorTable,'ogOmTempSensorEntry':ogOmTempSensorEntry,_W:ogOmTempSensorIndex,_Aa:ogOmTempSensorName,_Ab:ogOmTempSensorDevice,_Ac:ogOmTempSensorValue,'ogOmConformance':ogOmConformance,'ogOmCompliances':ogOmCompliances,'ogOmCompliance':ogOmCompliance,'ogOmGroups':ogOmGroups,_Ad:ogOmBasicGroup})