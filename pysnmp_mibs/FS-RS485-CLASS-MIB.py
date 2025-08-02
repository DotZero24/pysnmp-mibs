_AB='fsClassScheduleTableUpdateStatus'
_AA='fsRs485Mac'
_A9='fsRs485IpAddress'
_A8='fsClassOldDeviceIP'
_A7='fsClassChannel'
_A6='fsClassAPPUpdateReq'
_A5='fsClassCommand'
_A4='fsClassCMDType'
_A3='fsClassDeviceSwitch'
_A2='fsRs485HeartbeatStatus'
_A1='fsLabelStolenWarningStatus'
_A0='fsLabelPowerStatus'
_z='fsLabelActiveStatus'
_y='fsRs485TelnetIp'
_x='fsRs485SerialPower4'
_w='fsRs485SerialPower3'
_v='fsRs485SerialPower2'
_u='fsRs485SerialPower1'
_t='fsRs485State'
_s='scc_remote_no_exist_error'
_r='delete'
_q='unused'
_p='smart-switch'
_o='app-pad'
_n='screen'
_m='projector'
_l='record'
_k='air-con'
_j='videoandaudio'
_i='disable'
_h='fsSSIfIndex'
_g='unnormal'
_f='fsRs485SerialPort'
_e='fsClassCardID'
_d='fsClassDeviceState'
_c='fsClassDateTime'
_b='fsClassAPPPassword'
_a='fsClassAPPUsername'
_Z='fsLabelUnregStatus'
_Y='scc_update_file_too_big_error'
_X='scc_update_tftp_timeout_error'
_W='scc_update_product_id_error'
_V='scc_update_crc_error'
_U='scc_update_success'
_T='scc_update_start'
_S='init'
_R='fsClassOperAll'
_Q='start'
_P='fsClassDeviceID'
_O='fsClassDeviceType'
_N='default'
_M='enable'
_L='short'
_K='break'
_J='fsLabelID'
_I='fsLabelType'
_H='normal'
_G='unknown'
_F='OctetString'
_E='read-only'
_D='Integer32'
_C='FS-RS485-CLASS-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsRs485MIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,149))
if mibBuilder.loadTexts:fsRs485MIB.setRevisions(('2007-03-20 00:00',))
_FsRs485MIBObjects_ObjectIdentity=ObjectIdentity
fsRs485MIBObjects=_FsRs485MIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,149,1))
_FsRs485IpAddress_Type=IpAddress
_FsRs485IpAddress_Object=MibScalar
fsRs485IpAddress=_FsRs485IpAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,1),_FsRs485IpAddress_Type())
fsRs485IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRs485IpAddress.setStatus(_A)
_FsRs485IpAddressMask_Type=IpAddress
_FsRs485IpAddressMask_Object=MibScalar
fsRs485IpAddressMask=_FsRs485IpAddressMask_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,2),_FsRs485IpAddressMask_Type())
fsRs485IpAddressMask.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRs485IpAddressMask.setStatus(_A)
_FsRs485Gateway_Type=IpAddress
_FsRs485Gateway_Object=MibScalar
fsRs485Gateway=_FsRs485Gateway_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,3),_FsRs485Gateway_Type())
fsRs485Gateway.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRs485Gateway.setStatus(_A)
_FsRs485Mac_Type=PhysAddress
_FsRs485Mac_Object=MibScalar
fsRs485Mac=_FsRs485Mac_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,4),_FsRs485Mac_Type())
fsRs485Mac.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRs485Mac.setStatus(_A)
class _FsRs485ServerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('client',0),('server',1)))
_FsRs485ServerMode_Type.__name__=_D
_FsRs485ServerMode_Object=MibScalar
fsRs485ServerMode=_FsRs485ServerMode_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,5),_FsRs485ServerMode_Type())
fsRs485ServerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRs485ServerMode.setStatus(_A)
class _FsRs485SerialNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_FsRs485SerialNum_Type.__name__=_D
_FsRs485SerialNum_Object=MibScalar
fsRs485SerialNum=_FsRs485SerialNum_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,6),_FsRs485SerialNum_Type())
fsRs485SerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRs485SerialNum.setStatus(_A)
_FsRs485TelnetIp_Type=IpAddress
_FsRs485TelnetIp_Object=MibScalar
fsRs485TelnetIp=_FsRs485TelnetIp_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,7),_FsRs485TelnetIp_Type())
fsRs485TelnetIp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRs485TelnetIp.setStatus(_A)
_FsRs485State_Type=Integer32
_FsRs485State_Object=MibScalar
fsRs485State=_FsRs485State_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,8),_FsRs485State_Type())
fsRs485State.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRs485State.setStatus(_A)
class _FsRs485SerialPower1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_H,1),(_L,2),(_K,3)))
_FsRs485SerialPower1_Type.__name__=_D
_FsRs485SerialPower1_Object=MibScalar
fsRs485SerialPower1=_FsRs485SerialPower1_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,9),_FsRs485SerialPower1_Type())
fsRs485SerialPower1.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRs485SerialPower1.setStatus(_A)
class _FsRs485SerialPower2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_H,1),(_L,2),(_K,3)))
_FsRs485SerialPower2_Type.__name__=_D
_FsRs485SerialPower2_Object=MibScalar
fsRs485SerialPower2=_FsRs485SerialPower2_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,10),_FsRs485SerialPower2_Type())
fsRs485SerialPower2.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRs485SerialPower2.setStatus(_A)
class _FsRs485SerialPower3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_H,1),(_L,2),(_K,3)))
_FsRs485SerialPower3_Type.__name__=_D
_FsRs485SerialPower3_Object=MibScalar
fsRs485SerialPower3=_FsRs485SerialPower3_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,11),_FsRs485SerialPower3_Type())
fsRs485SerialPower3.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRs485SerialPower3.setStatus(_A)
class _FsRs485SerialPower4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_H,1),(_L,2),(_K,3)))
_FsRs485SerialPower4_Type.__name__=_D
_FsRs485SerialPower4_Object=MibScalar
fsRs485SerialPower4=_FsRs485SerialPower4_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,12),_FsRs485SerialPower4_Type())
fsRs485SerialPower4.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRs485SerialPower4.setStatus(_A)
_FsRs485VlanTable_Object=MibTable
fsRs485VlanTable=_FsRs485VlanTable_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,13))
if mibBuilder.loadTexts:fsRs485VlanTable.setStatus(_A)
_FsRs485VlanEntry_Object=MibTableRow
fsRs485VlanEntry=_FsRs485VlanEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,13,1))
fsRs485VlanEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:fsRs485VlanEntry.setStatus(_A)
_FsRs485SerialPort_Type=Counter32
_FsRs485SerialPort_Object=MibTableColumn
fsRs485SerialPort=_FsRs485SerialPort_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,13,1,1),_FsRs485SerialPort_Type())
fsRs485SerialPort.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRs485SerialPort.setStatus(_A)
class _FsRs485VLANID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_FsRs485VLANID_Type.__name__=_D
_FsRs485VLANID_Object=MibTableColumn
fsRs485VLANID=_FsRs485VLANID_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,13,1,2),_FsRs485VLANID_Type())
fsRs485VLANID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRs485VLANID.setStatus(_A)
class _FsRs485Baudrate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,999999))
_FsRs485Baudrate_Type.__name__=_D
_FsRs485Baudrate_Object=MibTableColumn
fsRs485Baudrate=_FsRs485Baudrate_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,13,1,3),_FsRs485Baudrate_Type())
fsRs485Baudrate.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRs485Baudrate.setStatus(_A)
class _FsRs485Parity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('odd',2),('even',3),('mark',4),('space',5)))
_FsRs485Parity_Type.__name__=_D
_FsRs485Parity_Object=MibTableColumn
fsRs485Parity=_FsRs485Parity_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,13,1,4),_FsRs485Parity_Type())
fsRs485Parity.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRs485Parity.setStatus(_A)
class _FsClassSerialType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('rs485',0),('rs232',1)))
_FsClassSerialType_Type.__name__=_D
_FsClassSerialType_Object=MibTableColumn
fsClassSerialType=_FsClassSerialType_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,13,1,5),_FsClassSerialType_Type())
fsClassSerialType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsClassSerialType.setStatus(_A)
class _FsClassStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_g,1)))
_FsClassStatus_Type.__name__=_D
_FsClassStatus_Object=MibTableColumn
fsClassStatus=_FsClassStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,13,1,6),_FsClassStatus_Type())
fsClassStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsClassStatus.setStatus(_A)
class _FsClassIsTeleControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_FsClassIsTeleControl_Type.__name__=_D
_FsClassIsTeleControl_Object=MibTableColumn
fsClassIsTeleControl=_FsClassIsTeleControl_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,13,1,7),_FsClassIsTeleControl_Type())
fsClassIsTeleControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassIsTeleControl.setStatus(_A)
_FsSSIfTable_Object=MibTable
fsSSIfTable=_FsSSIfTable_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,14))
if mibBuilder.loadTexts:fsSSIfTable.setStatus(_A)
_FsSSIfEntry_Object=MibTableRow
fsSSIfEntry=_FsSSIfEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,14,1))
fsSSIfEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:fsSSIfEntry.setStatus(_A)
_FsSSIfIndex_Type=Counter32
_FsSSIfIndex_Object=MibTableColumn
fsSSIfIndex=_FsSSIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,14,1,1),_FsSSIfIndex_Type())
fsSSIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSSIfIndex.setStatus(_A)
class _FsSSIfAccessVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsSSIfAccessVlan_Type.__name__=_D
_FsSSIfAccessVlan_Object=MibTableColumn
fsSSIfAccessVlan=_FsSSIfAccessVlan_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,14,1,2),_FsSSIfAccessVlan_Type())
fsSSIfAccessVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSSIfAccessVlan.setStatus(_A)
class _FsSSIfNativeVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsSSIfNativeVlan_Type.__name__=_D
_FsSSIfNativeVlan_Object=MibTableColumn
fsSSIfNativeVlan=_FsSSIfNativeVlan_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,14,1,3),_FsSSIfNativeVlan_Type())
fsSSIfNativeVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSSIfNativeVlan.setStatus(_A)
class _FsSSIfTrunk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_i,0),(_M,1)))
_FsSSIfTrunk_Type.__name__=_D
_FsSSIfTrunk_Object=MibTableColumn
fsSSIfTrunk=_FsSSIfTrunk_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,14,1,4),_FsSSIfTrunk_Type())
fsSSIfTrunk.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSSIfTrunk.setStatus(_A)
class _FsSSIfSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('speed_10M',0),('speed_100M',1),('speed_1000M',2)))
_FsSSIfSpeed_Type.__name__=_D
_FsSSIfSpeed_Object=MibTableColumn
fsSSIfSpeed=_FsSSIfSpeed_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,14,1,5),_FsSSIfSpeed_Type())
fsSSIfSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSSIfSpeed.setStatus(_A)
class _FsSSIfDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('half',0),('full',1)))
_FsSSIfDuplex_Type.__name__=_D
_FsSSIfDuplex_Object=MibTableColumn
fsSSIfDuplex=_FsSSIfDuplex_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,14,1,6),_FsSSIfDuplex_Type())
fsSSIfDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSSIfDuplex.setStatus(_A)
class _FsSSIfNegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_i,0),(_M,1)))
_FsSSIfNegotiation_Type.__name__=_D
_FsSSIfNegotiation_Object=MibTableColumn
fsSSIfNegotiation=_FsSSIfNegotiation_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,14,1,7),_FsSSIfNegotiation_Type())
fsSSIfNegotiation.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSSIfNegotiation.setStatus(_A)
class _FsRs485IpSetStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_M,1),('dhcp',2)))
_FsRs485IpSetStatus_Type.__name__=_D
_FsRs485IpSetStatus_Object=MibScalar
fsRs485IpSetStatus=_FsRs485IpSetStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,15),_FsRs485IpSetStatus_Type())
fsRs485IpSetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRs485IpSetStatus.setStatus(_A)
_FsLabelIDReg_Type=PhysAddress
_FsLabelIDReg_Object=MibScalar
fsLabelIDReg=_FsLabelIDReg_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,16),_FsLabelIDReg_Type())
fsLabelIDReg.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLabelIDReg.setStatus(_A)
class _FsLabelTypeReg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_N,0),('rfid',1),('ble',2),('zibgee',3)))
_FsLabelTypeReg_Type.__name__=_D
_FsLabelTypeReg_Object=MibScalar
fsLabelTypeReg=_FsLabelTypeReg_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,17),_FsLabelTypeReg_Type())
fsLabelTypeReg.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLabelTypeReg.setStatus(_A)
class _FsLabelRegStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_M,1)))
_FsLabelRegStatus_Type.__name__=_D
_FsLabelRegStatus_Object=MibScalar
fsLabelRegStatus=_FsLabelRegStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,18),_FsLabelRegStatus_Type())
fsLabelRegStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLabelRegStatus.setStatus(_A)
_FsLabelInfoTable_Object=MibTable
fsLabelInfoTable=_FsLabelInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,19))
if mibBuilder.loadTexts:fsLabelInfoTable.setStatus(_A)
_FsLabelInfoEntry_Object=MibTableRow
fsLabelInfoEntry=_FsLabelInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,19,1))
fsLabelInfoEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:fsLabelInfoEntry.setStatus(_A)
class _FsLabelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),('rfid',1),('ble',2),('zigbee',3)))
_FsLabelType_Type.__name__=_D
_FsLabelType_Object=MibTableColumn
fsLabelType=_FsLabelType_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,19,1,1),_FsLabelType_Type())
fsLabelType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsLabelType.setStatus(_A)
_FsLabelID_Type=PhysAddress
_FsLabelID_Object=MibTableColumn
fsLabelID=_FsLabelID_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,19,1,2),_FsLabelID_Type())
fsLabelID.setMaxAccess(_E)
if mibBuilder.loadTexts:fsLabelID.setStatus(_A)
class _FsLabelActiveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_G,0),('active',1),('deactive',2),('active-success-ack',3),('active-fail-ack',4),('deactive-success-ack',5),('deactive-fail-ack',6)))
_FsLabelActiveStatus_Type.__name__=_D
_FsLabelActiveStatus_Object=MibTableColumn
fsLabelActiveStatus=_FsLabelActiveStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,19,1,3),_FsLabelActiveStatus_Type())
fsLabelActiveStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLabelActiveStatus.setStatus(_A)
class _FsLabelPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsLabelPowerStatus_Type.__name__=_D
_FsLabelPowerStatus_Object=MibTableColumn
fsLabelPowerStatus=_FsLabelPowerStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,19,1,4),_FsLabelPowerStatus_Type())
fsLabelPowerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsLabelPowerStatus.setStatus(_A)
class _FsLabelWarningCancel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),('cancel-stolen',1),('cancel-power',2),('cancel-unnormal',3)))
_FsLabelWarningCancel_Type.__name__=_D
_FsLabelWarningCancel_Object=MibTableColumn
fsLabelWarningCancel=_FsLabelWarningCancel_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,19,1,5),_FsLabelWarningCancel_Type())
fsLabelWarningCancel.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLabelWarningCancel.setStatus(_A)
class _FsLabelUnregStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_G,0),('apply-unreg',1),('unreg',2),('allow-unreg',3),('not-allow-unreg',4),('reg-success',5),('reg-failed',6)))
_FsLabelUnregStatus_Type.__name__=_D
_FsLabelUnregStatus_Object=MibTableColumn
fsLabelUnregStatus=_FsLabelUnregStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,19,1,6),_FsLabelUnregStatus_Type())
fsLabelUnregStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLabelUnregStatus.setStatus(_A)
class _FsLabelStolenWarningStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_H,1),('stolen',2),(_g,3)))
_FsLabelStolenWarningStatus_Type.__name__=_D
_FsLabelStolenWarningStatus_Object=MibTableColumn
fsLabelStolenWarningStatus=_FsLabelStolenWarningStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,19,1,7),_FsLabelStolenWarningStatus_Type())
fsLabelStolenWarningStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsLabelStolenWarningStatus.setStatus(_A)
_FsRs485TrapIp_Type=IpAddress
_FsRs485TrapIp_Object=MibScalar
fsRs485TrapIp=_FsRs485TrapIp_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,20),_FsRs485TrapIp_Type())
fsRs485TrapIp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRs485TrapIp.setStatus(_A)
class _FsRs485HeartbeatStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_FsRs485HeartbeatStatus_Type.__name__=_D
_FsRs485HeartbeatStatus_Object=MibScalar
fsRs485HeartbeatStatus=_FsRs485HeartbeatStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,21),_FsRs485HeartbeatStatus_Type())
fsRs485HeartbeatStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRs485HeartbeatStatus.setStatus(_A)
class _FsClassPDUPower1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_K,1),(_H,2)))
_FsClassPDUPower1_Type.__name__=_D
_FsClassPDUPower1_Object=MibScalar
fsClassPDUPower1=_FsClassPDUPower1_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,22),_FsClassPDUPower1_Type())
fsClassPDUPower1.setMaxAccess(_E)
if mibBuilder.loadTexts:fsClassPDUPower1.setStatus(_A)
class _FsClassPDUPower2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_K,1),(_H,2)))
_FsClassPDUPower2_Type.__name__=_D
_FsClassPDUPower2_Object=MibScalar
fsClassPDUPower2=_FsClassPDUPower2_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,23),_FsClassPDUPower2_Type())
fsClassPDUPower2.setMaxAccess(_E)
if mibBuilder.loadTexts:fsClassPDUPower2.setStatus(_A)
class _FsClassDeviceAddType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_G,0),('video',1),('audio',2),(_j,3),('light',4),(_k,5),(_l,6),(_m,7),(_n,8),(_o,9),(_p,10)))
_FsClassDeviceAddType_Type.__name__=_D
_FsClassDeviceAddType_Object=MibScalar
fsClassDeviceAddType=_FsClassDeviceAddType_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,24),_FsClassDeviceAddType_Type())
fsClassDeviceAddType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeviceAddType.setStatus(_A)
_FsClassDeviceAddID_Type=Integer32
_FsClassDeviceAddID_Object=MibScalar
fsClassDeviceAddID=_FsClassDeviceAddID_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,25),_FsClassDeviceAddID_Type())
fsClassDeviceAddID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeviceAddID.setStatus(_A)
class _FsClassDeviceAddStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('add',1))
_FsClassDeviceAddStatus_Type.__name__=_D
_FsClassDeviceAddStatus_Object=MibScalar
fsClassDeviceAddStatus=_FsClassDeviceAddStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,26),_FsClassDeviceAddStatus_Type())
fsClassDeviceAddStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeviceAddStatus.setStatus(_A)
_FsClassDeviceInfoTable_Object=MibTable
fsClassDeviceInfoTable=_FsClassDeviceInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27))
if mibBuilder.loadTexts:fsClassDeviceInfoTable.setStatus(_A)
_FsClassDeviceInfoEntry_Object=MibTableRow
fsClassDeviceInfoEntry=_FsClassDeviceInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1))
fsClassDeviceInfoEntry.setIndexNames((0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:fsClassDeviceInfoEntry.setStatus(_A)
class _FsClassDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_G,0),('video',1),('audio',2),(_j,3),('light',4),(_k,5),(_l,6),(_m,7),(_n,8),(_o,9),(_p,10)))
_FsClassDeviceType_Type.__name__=_D
_FsClassDeviceType_Object=MibTableColumn
fsClassDeviceType=_FsClassDeviceType_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,1),_FsClassDeviceType_Type())
fsClassDeviceType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsClassDeviceType.setStatus(_A)
_FsClassDeviceID_Type=Integer32
_FsClassDeviceID_Object=MibTableColumn
fsClassDeviceID=_FsClassDeviceID_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,2),_FsClassDeviceID_Type())
fsClassDeviceID.setMaxAccess(_E)
if mibBuilder.loadTexts:fsClassDeviceID.setStatus(_A)
_FsClassDeviceIconType_Type=Integer32
_FsClassDeviceIconType_Object=MibTableColumn
fsClassDeviceIconType=_FsClassDeviceIconType_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,3),_FsClassDeviceIconType_Type())
fsClassDeviceIconType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeviceIconType.setStatus(_A)
class _FsClassDeviceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_FsClassDeviceName_Type.__name__=_F
_FsClassDeviceName_Object=MibTableColumn
fsClassDeviceName=_FsClassDeviceName_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,4),_FsClassDeviceName_Type())
fsClassDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeviceName.setStatus(_A)
_FsClassDeviceModelID_Type=Integer32
_FsClassDeviceModelID_Object=MibTableColumn
fsClassDeviceModelID=_FsClassDeviceModelID_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,5),_FsClassDeviceModelID_Type())
fsClassDeviceModelID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeviceModelID.setStatus(_A)
class _FsClassDeviceControlSerial_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_FsClassDeviceControlSerial_Type.__name__=_D
_FsClassDeviceControlSerial_Object=MibTableColumn
fsClassDeviceControlSerial=_FsClassDeviceControlSerial_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,6),_FsClassDeviceControlSerial_Type())
fsClassDeviceControlSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeviceControlSerial.setStatus(_A)
class _FsClassDeviceTeleControlPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_FsClassDeviceTeleControlPort_Type.__name__=_D
_FsClassDeviceTeleControlPort_Object=MibTableColumn
fsClassDeviceTeleControlPort=_FsClassDeviceTeleControlPort_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,7),_FsClassDeviceTeleControlPort_Type())
fsClassDeviceTeleControlPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeviceTeleControlPort.setStatus(_A)
class _FsClassDeviceIOType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('input',0),('output',1),('other',2)))
_FsClassDeviceIOType_Type.__name__=_D
_FsClassDeviceIOType_Object=MibTableColumn
fsClassDeviceIOType=_FsClassDeviceIOType_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,8),_FsClassDeviceIOType_Type())
fsClassDeviceIOType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeviceIOType.setStatus(_A)
class _FsClassDeviceVideoPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_FsClassDeviceVideoPort_Type.__name__=_D
_FsClassDeviceVideoPort_Object=MibTableColumn
fsClassDeviceVideoPort=_FsClassDeviceVideoPort_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,9),_FsClassDeviceVideoPort_Type())
fsClassDeviceVideoPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeviceVideoPort.setStatus(_A)
class _FsClassDeviceAudioPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_FsClassDeviceAudioPort_Type.__name__=_D
_FsClassDeviceAudioPort_Object=MibTableColumn
fsClassDeviceAudioPort=_FsClassDeviceAudioPort_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,10),_FsClassDeviceAudioPort_Type())
fsClassDeviceAudioPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeviceAudioPort.setStatus(_A)
class _FsClassDeviceVideoUsedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_q,0),('used',1)))
_FsClassDeviceVideoUsedStatus_Type.__name__=_D
_FsClassDeviceVideoUsedStatus_Object=MibTableColumn
fsClassDeviceVideoUsedStatus=_FsClassDeviceVideoUsedStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,11),_FsClassDeviceVideoUsedStatus_Type())
fsClassDeviceVideoUsedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeviceVideoUsedStatus.setStatus(_A)
class _FsClassDeviceAudioUsedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_q,0),('used',1)))
_FsClassDeviceAudioUsedStatus_Type.__name__=_D
_FsClassDeviceAudioUsedStatus_Object=MibTableColumn
fsClassDeviceAudioUsedStatus=_FsClassDeviceAudioUsedStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,12),_FsClassDeviceAudioUsedStatus_Type())
fsClassDeviceAudioUsedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeviceAudioUsedStatus.setStatus(_A)
_FsClassDeviceSwitch_Type=Integer32
_FsClassDeviceSwitch_Object=MibTableColumn
fsClassDeviceSwitch=_FsClassDeviceSwitch_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,13),_FsClassDeviceSwitch_Type())
fsClassDeviceSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeviceSwitch.setStatus(_A)
class _FsClassDeviceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_H,1),('no-ack',2)))
_FsClassDeviceState_Type.__name__=_D
_FsClassDeviceState_Object=MibTableColumn
fsClassDeviceState=_FsClassDeviceState_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,14),_FsClassDeviceState_Type())
fsClassDeviceState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeviceState.setStatus(_A)
_FsClassDeviceZigbeeID_Type=Integer32
_FsClassDeviceZigbeeID_Object=MibTableColumn
fsClassDeviceZigbeeID=_FsClassDeviceZigbeeID_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,15),_FsClassDeviceZigbeeID_Type())
fsClassDeviceZigbeeID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeviceZigbeeID.setStatus(_A)
class _FsClassDeviceSetStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unset',0),('set',1),(_r,2),('update',3)))
_FsClassDeviceSetStatus_Type.__name__=_D
_FsClassDeviceSetStatus_Object=MibTableColumn
fsClassDeviceSetStatus=_FsClassDeviceSetStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,16),_FsClassDeviceSetStatus_Type())
fsClassDeviceSetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeviceSetStatus.setStatus(_A)
_FsClassDeviceIP_Type=IpAddress
_FsClassDeviceIP_Object=MibTableColumn
fsClassDeviceIP=_FsClassDeviceIP_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,17),_FsClassDeviceIP_Type())
fsClassDeviceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeviceIP.setStatus(_A)
_FsClassBindDeviceID_Type=Integer32
_FsClassBindDeviceID_Object=MibTableColumn
fsClassBindDeviceID=_FsClassBindDeviceID_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,18),_FsClassBindDeviceID_Type())
fsClassBindDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassBindDeviceID.setStatus(_A)
_FsClassBatchSupport_Type=Integer32
_FsClassBatchSupport_Object=MibTableColumn
fsClassBatchSupport=_FsClassBatchSupport_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,27,1,19),_FsClassBatchSupport_Type())
fsClassBatchSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassBatchSupport.setStatus(_A)
class _FsClassAPPUsername_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_FsClassAPPUsername_Type.__name__=_F
_FsClassAPPUsername_Object=MibScalar
fsClassAPPUsername=_FsClassAPPUsername_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,28),_FsClassAPPUsername_Type())
fsClassAPPUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassAPPUsername.setStatus(_A)
class _FsClassAPPPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_FsClassAPPPassword_Type.__name__=_F
_FsClassAPPPassword_Object=MibScalar
fsClassAPPPassword=_FsClassAPPPassword_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,29),_FsClassAPPPassword_Type())
fsClassAPPPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassAPPPassword.setStatus(_A)
class _FsClassAPPAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('success',0),('failed',1),('success-update',2),('card-success',3),('card-failed',4),('user-info',5)))
_FsClassAPPAuth_Type.__name__=_D
_FsClassAPPAuth_Object=MibScalar
fsClassAPPAuth=_FsClassAPPAuth_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,30),_FsClassAPPAuth_Type())
fsClassAPPAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassAPPAuth.setStatus(_A)
_FsClassCMDDeviceModelID_Type=Integer32
_FsClassCMDDeviceModelID_Object=MibScalar
fsClassCMDDeviceModelID=_FsClassCMDDeviceModelID_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,31),_FsClassCMDDeviceModelID_Type())
fsClassCMDDeviceModelID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassCMDDeviceModelID.setStatus(_A)
_FsClassCMDType_Type=Integer32
_FsClassCMDType_Object=MibScalar
fsClassCMDType=_FsClassCMDType_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,32),_FsClassCMDType_Type())
fsClassCMDType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassCMDType.setStatus(_A)
class _FsClassCommand_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_FsClassCommand_Type.__name__=_F
_FsClassCommand_Object=MibScalar
fsClassCommand=_FsClassCommand_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,33),_FsClassCommand_Type())
fsClassCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassCommand.setStatus(_A)
class _FsClassCommandSetStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto-get',1),('set',2),(_r,3)))
_FsClassCommandSetStatus_Type.__name__=_D
_FsClassCommandSetStatus_Object=MibScalar
fsClassCommandSetStatus=_FsClassCommandSetStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,34),_FsClassCommandSetStatus_Type())
fsClassCommandSetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassCommandSetStatus.setStatus(_A)
class _FsClassOperAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('open-all',1),('close-all',2)))
_FsClassOperAll_Type.__name__=_D
_FsClassOperAll_Object=MibScalar
fsClassOperAll=_FsClassOperAll_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,35),_FsClassOperAll_Type())
fsClassOperAll.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassOperAll.setStatus(_A)
class _FsClassCardID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_FsClassCardID_Type.__name__=_F
_FsClassCardID_Object=MibScalar
fsClassCardID=_FsClassCardID_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,36),_FsClassCardID_Type())
fsClassCardID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassCardID.setStatus(_A)
_FsClassDateTime_Type=Integer32
_FsClassDateTime_Object=MibScalar
fsClassDateTime=_FsClassDateTime_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,37),_FsClassDateTime_Type())
fsClassDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDateTime.setStatus(_A)
class _FsClassAPPUpdateReq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('device_req',1),('user_auth_req',2)))
_FsClassAPPUpdateReq_Type.__name__=_D
_FsClassAPPUpdateReq_Object=MibScalar
fsClassAPPUpdateReq=_FsClassAPPUpdateReq_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,38),_FsClassAPPUpdateReq_Type())
fsClassAPPUpdateReq.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassAPPUpdateReq.setStatus(_A)
class _FsClassUpdateFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FsClassUpdateFileName_Type.__name__=_F
_FsClassUpdateFileName_Object=MibScalar
fsClassUpdateFileName=_FsClassUpdateFileName_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,39),_FsClassUpdateFileName_Type())
fsClassUpdateFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassUpdateFileName.setStatus(_A)
class _FsClassUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_Q,1))
_FsClassUpdate_Type.__name__=_D
_FsClassUpdate_Object=MibScalar
fsClassUpdate=_FsClassUpdate_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,40),_FsClassUpdate_Type())
fsClassUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassUpdate.setStatus(_A)
class _FsClassSoftVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FsClassSoftVersion_Type.__name__=_F
_FsClassSoftVersion_Object=MibScalar
fsClassSoftVersion=_FsClassSoftVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,41),_FsClassSoftVersion_Type())
fsClassSoftVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassSoftVersion.setStatus(_A)
class _FsClassChannel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FsClassChannel_Type.__name__=_F
_FsClassChannel_Object=MibScalar
fsClassChannel=_FsClassChannel_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,42),_FsClassChannel_Type())
fsClassChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassChannel.setStatus(_A)
_FsClassOldDeviceIP_Type=IpAddress
_FsClassOldDeviceIP_Object=MibScalar
fsClassOldDeviceIP=_FsClassOldDeviceIP_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,43),_FsClassOldDeviceIP_Type())
fsClassOldDeviceIP.setMaxAccess(_E)
if mibBuilder.loadTexts:fsClassOldDeviceIP.setStatus(_A)
class _FsClassCommunity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsClassCommunity_Type.__name__=_F
_FsClassCommunity_Object=MibScalar
fsClassCommunity=_FsClassCommunity_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,44),_FsClassCommunity_Type())
fsClassCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassCommunity.setStatus(_A)
class _FsClassUpdateStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_S,0),(_T,1),(_U,2),(_V,3),(_W,4),(_X,5),('remote_device_update_no_existerror',6),(_Y,7)))
_FsClassUpdateStatus_Type.__name__=_D
_FsClassUpdateStatus_Object=MibScalar
fsClassUpdateStatus=_FsClassUpdateStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,45),_FsClassUpdateStatus_Type())
fsClassUpdateStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassUpdateStatus.setStatus(_A)
class _FsClassScheduleTableName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FsClassScheduleTableName_Type.__name__=_F
_FsClassScheduleTableName_Object=MibScalar
fsClassScheduleTableName=_FsClassScheduleTableName_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,46),_FsClassScheduleTableName_Type())
fsClassScheduleTableName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassScheduleTableName.setStatus(_A)
class _FsClassUpdateScheduleTable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_Q,1))
_FsClassUpdateScheduleTable_Type.__name__=_D
_FsClassUpdateScheduleTable_Object=MibScalar
fsClassUpdateScheduleTable=_FsClassUpdateScheduleTable_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,47),_FsClassUpdateScheduleTable_Type())
fsClassUpdateScheduleTable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassUpdateScheduleTable.setStatus(_A)
class _FsClassScheduleTableUpdateStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_S,0),(_T,1),(_U,2),(_V,3),(_W,4),(_X,5),(_s,6),(_Y,7),('scc_update_redo',8)))
_FsClassScheduleTableUpdateStatus_Type.__name__=_D
_FsClassScheduleTableUpdateStatus_Object=MibScalar
fsClassScheduleTableUpdateStatus=_FsClassScheduleTableUpdateStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,48),_FsClassScheduleTableUpdateStatus_Type())
fsClassScheduleTableUpdateStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsClassScheduleTableUpdateStatus.setStatus(_A)
class _FsClassCheckTableName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FsClassCheckTableName_Type.__name__=_F
_FsClassCheckTableName_Object=MibScalar
fsClassCheckTableName=_FsClassCheckTableName_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,49),_FsClassCheckTableName_Type())
fsClassCheckTableName.setMaxAccess(_E)
if mibBuilder.loadTexts:fsClassCheckTableName.setStatus(_A)
class _FsClassReadCheckTable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_Q,1))
_FsClassReadCheckTable_Type.__name__=_D
_FsClassReadCheckTable_Object=MibScalar
fsClassReadCheckTable=_FsClassReadCheckTable_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,50),_FsClassReadCheckTable_Type())
fsClassReadCheckTable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassReadCheckTable.setStatus(_A)
class _FsClassReadCheckTable1UploadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_S,0),(_T,1),(_U,2),(_V,3),(_W,4),(_X,5),(_s,6),(_Y,7)))
_FsClassReadCheckTable1UploadStatus_Type.__name__=_D
_FsClassReadCheckTable1UploadStatus_Object=MibScalar
fsClassReadCheckTable1UploadStatus=_FsClassReadCheckTable1UploadStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,51),_FsClassReadCheckTable1UploadStatus_Type())
fsClassReadCheckTable1UploadStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsClassReadCheckTable1UploadStatus.setStatus(_A)
_FsClassLampTimeClass_Type=Integer32
_FsClassLampTimeClass_Object=MibScalar
fsClassLampTimeClass=_FsClassLampTimeClass_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,52),_FsClassLampTimeClass_Type())
fsClassLampTimeClass.setMaxAccess(_E)
if mibBuilder.loadTexts:fsClassLampTimeClass.setStatus(_A)
class _FsClassDeleteRecordTable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_Q,1))
_FsClassDeleteRecordTable_Type.__name__=_D
_FsClassDeleteRecordTable_Object=MibScalar
fsClassDeleteRecordTable=_FsClassDeleteRecordTable_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,53),_FsClassDeleteRecordTable_Type())
fsClassDeleteRecordTable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassDeleteRecordTable.setStatus(_A)
_FsClassSystemTime_Type=Counter32
_FsClassSystemTime_Object=MibScalar
fsClassSystemTime=_FsClassSystemTime_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,54),_FsClassSystemTime_Type())
fsClassSystemTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClassSystemTime.setStatus(_A)
class _FsClassProjectorFact_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsClassProjectorFact_Type.__name__=_F
_FsClassProjectorFact_Object=MibScalar
fsClassProjectorFact=_FsClassProjectorFact_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,55),_FsClassProjectorFact_Type())
fsClassProjectorFact.setMaxAccess(_E)
if mibBuilder.loadTexts:fsClassProjectorFact.setStatus(_A)
class _FsClassProjectorModel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FsClassProjectorModel_Type.__name__=_F
_FsClassProjectorModel_Object=MibScalar
fsClassProjectorModel=_FsClassProjectorModel_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,56),_FsClassProjectorModel_Type())
fsClassProjectorModel.setMaxAccess(_E)
if mibBuilder.loadTexts:fsClassProjectorModel.setStatus(_A)
class _FsClassAIOFact_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsClassAIOFact_Type.__name__=_F
_FsClassAIOFact_Object=MibScalar
fsClassAIOFact=_FsClassAIOFact_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,57),_FsClassAIOFact_Type())
fsClassAIOFact.setMaxAccess(_E)
if mibBuilder.loadTexts:fsClassAIOFact.setStatus(_A)
class _FsClassAIOModel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FsClassAIOModel_Type.__name__=_F
_FsClassAIOModel_Object=MibScalar
fsClassAIOModel=_FsClassAIOModel_Object((1,3,6,1,4,1,52642,1,1,10,2,149,1,58),_FsClassAIOModel_Type())
fsClassAIOModel.setMaxAccess(_E)
if mibBuilder.loadTexts:fsClassAIOModel.setStatus(_A)
_FsRs485MIBTrap_ObjectIdentity=ObjectIdentity
fsRs485MIBTrap=_FsRs485MIBTrap_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,149,2))
fsRs485StateChange=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,0))
fsRs485StateChange.setObjects((_C,_t))
if mibBuilder.loadTexts:fsRs485StateChange.setStatus(_A)
fsRs485Power1Change=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,1))
fsRs485Power1Change.setObjects((_C,_u))
if mibBuilder.loadTexts:fsRs485Power1Change.setStatus(_A)
fsRs485Power2Change=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,2))
fsRs485Power2Change.setObjects((_C,_v))
if mibBuilder.loadTexts:fsRs485Power2Change.setStatus(_A)
fsRs485Power3Change=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,3))
fsRs485Power3Change.setObjects((_C,_w))
if mibBuilder.loadTexts:fsRs485Power3Change.setStatus(_A)
fsRs485Power4Change=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,4))
fsRs485Power4Change.setObjects((_C,_x))
if mibBuilder.loadTexts:fsRs485Power4Change.setStatus(_A)
fsRs485TelnetFail=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,5))
fsRs485TelnetFail.setObjects((_C,_y))
if mibBuilder.loadTexts:fsRs485TelnetFail.setStatus(_A)
fsLabelActiveACK=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,6))
fsLabelActiveACK.setObjects(*((_C,_I),(_C,_J),(_C,_z)))
if mibBuilder.loadTexts:fsLabelActiveACK.setStatus(_A)
fsLabelLowPower=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,7))
fsLabelLowPower.setObjects(*((_C,_I),(_C,_J),(_C,_A0)))
if mibBuilder.loadTexts:fsLabelLowPower.setStatus(_A)
fsLabelStolen=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,8))
fsLabelStolen.setObjects(*((_C,_I),(_C,_J),(_C,_A1)))
if mibBuilder.loadTexts:fsLabelStolen.setStatus(_A)
fsLabelUnregACK=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,9))
fsLabelUnregACK.setObjects(*((_C,_I),(_C,_J),(_C,_Z)))
if mibBuilder.loadTexts:fsLabelUnregACK.setStatus(_A)
fsRs485Heartbeat=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,10))
fsRs485Heartbeat.setObjects((_C,_A2))
if mibBuilder.loadTexts:fsRs485Heartbeat.setStatus(_A)
fsLabelRegACK=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,11))
fsLabelRegACK.setObjects(*((_C,_I),(_C,_J),(_C,_Z)))
if mibBuilder.loadTexts:fsLabelRegACK.setStatus(_A)
fsClassAPPLoginREQ=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,12))
fsClassAPPLoginREQ.setObjects(*((_C,_a),(_C,_b),(_C,_c)))
if mibBuilder.loadTexts:fsClassAPPLoginREQ.setStatus(_A)
fsClassAPPOperation=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,13))
fsClassAPPOperation.setObjects(*((_C,_O),(_C,_P),(_C,_A3),(_C,_d)))
if mibBuilder.loadTexts:fsClassAPPOperation.setStatus(_A)
fsClassTelecommand=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,14))
fsClassTelecommand.setObjects(*((_C,_O),(_C,_A4),(_C,_A5)))
if mibBuilder.loadTexts:fsClassTelecommand.setStatus(_A)
fsClassSwipeCard=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,15))
fsClassSwipeCard.setObjects((_C,_e))
if mibBuilder.loadTexts:fsClassSwipeCard.setStatus(_A)
fsClassUpdateReq=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,16))
fsClassUpdateReq.setObjects(*((_C,_A6),(_C,_c)))
if mibBuilder.loadTexts:fsClassUpdateReq.setStatus(_A)
fsClassOperationAll=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,17))
fsClassOperationAll.setObjects((_C,_R))
if mibBuilder.loadTexts:fsClassOperationAll.setStatus(_A)
fsClassChannelToServer=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,18))
fsClassChannelToServer.setObjects((_C,_A7))
if mibBuilder.loadTexts:fsClassChannelToServer.setStatus(_A)
fsClassDevIPChange=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,19))
fsClassDevIPChange.setObjects(*((_C,_A8),(_C,_A9),(_C,_AA)))
if mibBuilder.loadTexts:fsClassDevIPChange.setStatus(_A)
fsClassCardOperationAll=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,20))
fsClassCardOperationAll.setObjects(*((_C,_e),(_C,_R)))
if mibBuilder.loadTexts:fsClassCardOperationAll.setStatus(_A)
fsClassAccountOperationAll=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,21))
fsClassAccountOperationAll.setObjects(*((_C,_a),(_C,_b),(_C,_R)))
if mibBuilder.loadTexts:fsClassAccountOperationAll.setStatus(_A)
fsClassTableRedo=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,22))
fsClassTableRedo.setObjects((_C,_AB))
if mibBuilder.loadTexts:fsClassTableRedo.setStatus(_A)
fsClassDeviceStateChange=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,149,2,23))
fsClassDeviceStateChange.setObjects(*((_C,_P),(_C,_d)))
if mibBuilder.loadTexts:fsClassDeviceStateChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fsRs485MIB':fsRs485MIB,'fsRs485MIBObjects':fsRs485MIBObjects,_A9:fsRs485IpAddress,'fsRs485IpAddressMask':fsRs485IpAddressMask,'fsRs485Gateway':fsRs485Gateway,_AA:fsRs485Mac,'fsRs485ServerMode':fsRs485ServerMode,'fsRs485SerialNum':fsRs485SerialNum,_y:fsRs485TelnetIp,_t:fsRs485State,_u:fsRs485SerialPower1,_v:fsRs485SerialPower2,_w:fsRs485SerialPower3,_x:fsRs485SerialPower4,'fsRs485VlanTable':fsRs485VlanTable,'fsRs485VlanEntry':fsRs485VlanEntry,_f:fsRs485SerialPort,'fsRs485VLANID':fsRs485VLANID,'fsRs485Baudrate':fsRs485Baudrate,'fsRs485Parity':fsRs485Parity,'fsClassSerialType':fsClassSerialType,'fsClassStatus':fsClassStatus,'fsClassIsTeleControl':fsClassIsTeleControl,'fsSSIfTable':fsSSIfTable,'fsSSIfEntry':fsSSIfEntry,_h:fsSSIfIndex,'fsSSIfAccessVlan':fsSSIfAccessVlan,'fsSSIfNativeVlan':fsSSIfNativeVlan,'fsSSIfTrunk':fsSSIfTrunk,'fsSSIfSpeed':fsSSIfSpeed,'fsSSIfDuplex':fsSSIfDuplex,'fsSSIfNegotiation':fsSSIfNegotiation,'fsRs485IpSetStatus':fsRs485IpSetStatus,'fsLabelIDReg':fsLabelIDReg,'fsLabelTypeReg':fsLabelTypeReg,'fsLabelRegStatus':fsLabelRegStatus,'fsLabelInfoTable':fsLabelInfoTable,'fsLabelInfoEntry':fsLabelInfoEntry,_I:fsLabelType,_J:fsLabelID,_z:fsLabelActiveStatus,_A0:fsLabelPowerStatus,'fsLabelWarningCancel':fsLabelWarningCancel,_Z:fsLabelUnregStatus,_A1:fsLabelStolenWarningStatus,'fsRs485TrapIp':fsRs485TrapIp,_A2:fsRs485HeartbeatStatus,'fsClassPDUPower1':fsClassPDUPower1,'fsClassPDUPower2':fsClassPDUPower2,'fsClassDeviceAddType':fsClassDeviceAddType,'fsClassDeviceAddID':fsClassDeviceAddID,'fsClassDeviceAddStatus':fsClassDeviceAddStatus,'fsClassDeviceInfoTable':fsClassDeviceInfoTable,'fsClassDeviceInfoEntry':fsClassDeviceInfoEntry,_O:fsClassDeviceType,_P:fsClassDeviceID,'fsClassDeviceIconType':fsClassDeviceIconType,'fsClassDeviceName':fsClassDeviceName,'fsClassDeviceModelID':fsClassDeviceModelID,'fsClassDeviceControlSerial':fsClassDeviceControlSerial,'fsClassDeviceTeleControlPort':fsClassDeviceTeleControlPort,'fsClassDeviceIOType':fsClassDeviceIOType,'fsClassDeviceVideoPort':fsClassDeviceVideoPort,'fsClassDeviceAudioPort':fsClassDeviceAudioPort,'fsClassDeviceVideoUsedStatus':fsClassDeviceVideoUsedStatus,'fsClassDeviceAudioUsedStatus':fsClassDeviceAudioUsedStatus,_A3:fsClassDeviceSwitch,_d:fsClassDeviceState,'fsClassDeviceZigbeeID':fsClassDeviceZigbeeID,'fsClassDeviceSetStatus':fsClassDeviceSetStatus,'fsClassDeviceIP':fsClassDeviceIP,'fsClassBindDeviceID':fsClassBindDeviceID,'fsClassBatchSupport':fsClassBatchSupport,_a:fsClassAPPUsername,_b:fsClassAPPPassword,'fsClassAPPAuth':fsClassAPPAuth,'fsClassCMDDeviceModelID':fsClassCMDDeviceModelID,_A4:fsClassCMDType,_A5:fsClassCommand,'fsClassCommandSetStatus':fsClassCommandSetStatus,_R:fsClassOperAll,_e:fsClassCardID,_c:fsClassDateTime,_A6:fsClassAPPUpdateReq,'fsClassUpdateFileName':fsClassUpdateFileName,'fsClassUpdate':fsClassUpdate,'fsClassSoftVersion':fsClassSoftVersion,_A7:fsClassChannel,_A8:fsClassOldDeviceIP,'fsClassCommunity':fsClassCommunity,'fsClassUpdateStatus':fsClassUpdateStatus,'fsClassScheduleTableName':fsClassScheduleTableName,'fsClassUpdateScheduleTable':fsClassUpdateScheduleTable,_AB:fsClassScheduleTableUpdateStatus,'fsClassCheckTableName':fsClassCheckTableName,'fsClassReadCheckTable':fsClassReadCheckTable,'fsClassReadCheckTable1UploadStatus':fsClassReadCheckTable1UploadStatus,'fsClassLampTimeClass':fsClassLampTimeClass,'fsClassDeleteRecordTable':fsClassDeleteRecordTable,'fsClassSystemTime':fsClassSystemTime,'fsClassProjectorFact':fsClassProjectorFact,'fsClassProjectorModel':fsClassProjectorModel,'fsClassAIOFact':fsClassAIOFact,'fsClassAIOModel':fsClassAIOModel,'fsRs485MIBTrap':fsRs485MIBTrap,'fsRs485StateChange':fsRs485StateChange,'fsRs485Power1Change':fsRs485Power1Change,'fsRs485Power2Change':fsRs485Power2Change,'fsRs485Power3Change':fsRs485Power3Change,'fsRs485Power4Change':fsRs485Power4Change,'fsRs485TelnetFail':fsRs485TelnetFail,'fsLabelActiveACK':fsLabelActiveACK,'fsLabelLowPower':fsLabelLowPower,'fsLabelStolen':fsLabelStolen,'fsLabelUnregACK':fsLabelUnregACK,'fsRs485Heartbeat':fsRs485Heartbeat,'fsLabelRegACK':fsLabelRegACK,'fsClassAPPLoginREQ':fsClassAPPLoginREQ,'fsClassAPPOperation':fsClassAPPOperation,'fsClassTelecommand':fsClassTelecommand,'fsClassSwipeCard':fsClassSwipeCard,'fsClassUpdateReq':fsClassUpdateReq,'fsClassOperationAll':fsClassOperationAll,'fsClassChannelToServer':fsClassChannelToServer,'fsClassDevIPChange':fsClassDevIPChange,'fsClassCardOperationAll':fsClassCardOperationAll,'fsClassAccountOperationAll':fsClassAccountOperationAll,'fsClassTableRedo':fsClassTableRedo,'fsClassDeviceStateChange':fsClassDeviceStateChange})