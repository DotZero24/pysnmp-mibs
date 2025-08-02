_AC='hpicfPsModel'
_AB='hpicfXpsZoneRecordVersion'
_AA='hpicfXpsZonePowerShareForce'
_A9='hpicfXpsPSUModule'
_A8='hpicfXpsPSURev'
_A7='hpicfXpsZoneWattage'
_A6='hpicfXpsZoneVoltage'
_A5='hpicfXpsZonePowerShareMap'
_A4='hpicfXpsZoneState'
_A3='hpicfXpsZoneNo'
_A2='hpicfXpsSwitchModType'
_A1='hpicfXpsSupportedZoneVersion'
_A0='hpicfXpsSupportedCableVersion'
_z='hpicfXpsResetReqStatus'
_y='hpicfXpsPowerShareReqStatus'
_x='hpicfXpsModuleName'
_w='hpicfXpsSerialNum'
_v='hpicfXpsType'
_u='hpicfXpsReset'
_t='hpicfXpsAllowPortsSupported'
_s='hpicfXpsSwitchAutoRecovery'
_r='hpicfXpsSwitchAdminStatus'
_q='hpicfXpsPower'
_p='hpicfXpsSwitchIpsWattage'
_o='hpicfXpsSwitchIpsVoltage'
_n='hpicfXpsSwitchOSVersion'
_m='hpicfXpsMACAddress'
_l='hpicfXpsSysName'
_k='hpicfXpsConnectionState'
_j='hpicfXpsSwitchSerialNo'
_i='hpicfXpsPortOperStatus'
_h='deprecated'
_g='failed'
_f='success'
_e='inProgress'
_d='disable'
_c='enable'
_b='hpicfXpsConnectingPort'
_a='not-accessible'
_Z='hpicfPsBayNum'
_Y='notReady'
_X='notConnected'
_W='DisplayString'
_V='SnmpAdminString'
_U='hpicfPsGroup1'
_T='hpicfXpsZoneGroup'
_S='hpicfXpsGroup'
_R='hpicfPsGroup'
_Q='hpicfPsLastCall'
_P='hpicfPsWattageMax'
_O='hpicfPsWattageCur'
_N='hpicfPsVoltageInfo'
_M='hpicfPsTemp'
_L='hpicfPsFailures'
_K='hpicfPsState'
_J='Watts'
_I='Unsigned32'
_H='OctetString'
_G='entPhysicalIndex'
_F='ENTITY-MIB'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='POWERSUPPLY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_F,_G)
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_V)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_W,'MacAddress','PhysAddress','TextualConvention','TruthValue')
hpicfPsMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,55))
if mibBuilder.loadTexts:hpicfPsMIB.setRevisions(('2013-08-20 00:00','2013-06-13 00:00','2013-03-07 10:00','2008-08-27 10:00'))
class HpicfDcPsIndex(TextualConvention,Unsigned32):status=_A;displayHint='d'
class HpicfDcPsState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('psNotPresent',1),('psNotPlugged',2),('psPowered',3),('psFailed',4),('psPermFailure',5),('psMax',6),('psAuxFailure',7),('psNotPowered',8),('psAuxNotPowered',9)))
class HpicfXpsConnectionStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_X,0),('unavailable',1),('available',2),('active',3),('mismatch',4),(_Y,5),('overCurrent',6),('cannotPower',7),('autoDisabled',8)))
class HpicfXpsZoneStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_X,1),(_Y,2),('faulted',3),('powered',4),('inReset',5)))
_HpicfEntityPs_ObjectIdentity=ObjectIdentity
hpicfEntityPs=_HpicfEntityPs_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,55,1))
_HpicfPsTable_Object=MibTable
hpicfPsTable=_HpicfPsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,1))
if mibBuilder.loadTexts:hpicfPsTable.setStatus(_A)
_HpicfPsEntry_Object=MibTableRow
hpicfPsEntry=_HpicfPsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,1,1))
hpicfPsEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:hpicfPsEntry.setStatus(_A)
_HpicfPsBayNum_Type=HpicfDcPsIndex
_HpicfPsBayNum_Object=MibTableColumn
hpicfPsBayNum=_HpicfPsBayNum_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,1,1,1),_HpicfPsBayNum_Type())
hpicfPsBayNum.setMaxAccess(_a)
if mibBuilder.loadTexts:hpicfPsBayNum.setStatus(_A)
_HpicfPsState_Type=HpicfDcPsState
_HpicfPsState_Object=MibTableColumn
hpicfPsState=_HpicfPsState_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,1,1,2),_HpicfPsState_Type())
hpicfPsState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfPsState.setStatus(_A)
_HpicfPsFailures_Type=Counter32
_HpicfPsFailures_Object=MibTableColumn
hpicfPsFailures=_HpicfPsFailures_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,1,1,3),_HpicfPsFailures_Type())
hpicfPsFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfPsFailures.setStatus(_A)
_HpicfPsTemp_Type=Integer32
_HpicfPsTemp_Object=MibTableColumn
hpicfPsTemp=_HpicfPsTemp_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,1,1,4),_HpicfPsTemp_Type())
hpicfPsTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfPsTemp.setStatus(_A)
class _HpicfPsVoltageInfo_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpicfPsVoltageInfo_Type.__name__=_V
_HpicfPsVoltageInfo_Object=MibTableColumn
hpicfPsVoltageInfo=_HpicfPsVoltageInfo_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,1,1,5),_HpicfPsVoltageInfo_Type())
hpicfPsVoltageInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfPsVoltageInfo.setStatus(_A)
_HpicfPsWattageCur_Type=Integer32
_HpicfPsWattageCur_Object=MibTableColumn
hpicfPsWattageCur=_HpicfPsWattageCur_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,1,1,6),_HpicfPsWattageCur_Type())
hpicfPsWattageCur.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfPsWattageCur.setStatus(_A)
_HpicfPsWattageMax_Type=Integer32
_HpicfPsWattageMax_Object=MibTableColumn
hpicfPsWattageMax=_HpicfPsWattageMax_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,1,1,7),_HpicfPsWattageMax_Type())
hpicfPsWattageMax.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfPsWattageMax.setStatus(_A)
_HpicfPsLastCall_Type=Counter32
_HpicfPsLastCall_Object=MibTableColumn
hpicfPsLastCall=_HpicfPsLastCall_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,1,1,8),_HpicfPsLastCall_Type())
hpicfPsLastCall.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfPsLastCall.setStatus(_A)
class _HpicfPsModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpicfPsModel_Type.__name__=_W
_HpicfPsModel_Object=MibTableColumn
hpicfPsModel=_HpicfPsModel_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,1,1,9),_HpicfPsModel_Type())
hpicfPsModel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfPsModel.setStatus(_A)
_HpicfXpsTable_Object=MibTable
hpicfXpsTable=_HpicfXpsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,2))
if mibBuilder.loadTexts:hpicfXpsTable.setStatus(_A)
_HpicfXpsEntry_Object=MibTableRow
hpicfXpsEntry=_HpicfXpsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,2,1))
hpicfXpsEntry.setIndexNames((0,_F,_G),(0,_B,_b))
if mibBuilder.loadTexts:hpicfXpsEntry.setStatus(_A)
_HpicfXpsConnectingPort_Type=Unsigned32
_HpicfXpsConnectingPort_Object=MibTableColumn
hpicfXpsConnectingPort=_HpicfXpsConnectingPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,2,1,1),_HpicfXpsConnectingPort_Type())
hpicfXpsConnectingPort.setMaxAccess(_a)
if mibBuilder.loadTexts:hpicfXpsConnectingPort.setStatus(_A)
class _HpicfXpsPortOperStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_HpicfXpsPortOperStatus_Type.__name__=_D
_HpicfXpsPortOperStatus_Object=MibTableColumn
hpicfXpsPortOperStatus=_HpicfXpsPortOperStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,2,1,2),_HpicfXpsPortOperStatus_Type())
hpicfXpsPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsPortOperStatus.setStatus(_A)
_HpicfXpsSwitchSerialNo_Type=DisplayString
_HpicfXpsSwitchSerialNo_Object=MibTableColumn
hpicfXpsSwitchSerialNo=_HpicfXpsSwitchSerialNo_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,2,1,3),_HpicfXpsSwitchSerialNo_Type())
hpicfXpsSwitchSerialNo.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsSwitchSerialNo.setStatus(_A)
_HpicfXpsConnectionState_Type=HpicfXpsConnectionStatus
_HpicfXpsConnectionState_Object=MibTableColumn
hpicfXpsConnectionState=_HpicfXpsConnectionState_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,2,1,4),_HpicfXpsConnectionState_Type())
hpicfXpsConnectionState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsConnectionState.setStatus(_A)
_HpicfXpsSysName_Type=DisplayString
_HpicfXpsSysName_Object=MibTableColumn
hpicfXpsSysName=_HpicfXpsSysName_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,2,1,5),_HpicfXpsSysName_Type())
hpicfXpsSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsSysName.setStatus(_A)
_HpicfXpsMACAddress_Type=MacAddress
_HpicfXpsMACAddress_Object=MibTableColumn
hpicfXpsMACAddress=_HpicfXpsMACAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,2,1,6),_HpicfXpsMACAddress_Type())
hpicfXpsMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsMACAddress.setStatus(_A)
_HpicfXpsSwitchOSVersion_Type=DisplayString
_HpicfXpsSwitchOSVersion_Object=MibTableColumn
hpicfXpsSwitchOSVersion=_HpicfXpsSwitchOSVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,2,1,7),_HpicfXpsSwitchOSVersion_Type())
hpicfXpsSwitchOSVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsSwitchOSVersion.setStatus(_A)
_HpicfXpsSwitchIpsVoltage_Type=Unsigned32
_HpicfXpsSwitchIpsVoltage_Object=MibTableColumn
hpicfXpsSwitchIpsVoltage=_HpicfXpsSwitchIpsVoltage_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,2,1,8),_HpicfXpsSwitchIpsVoltage_Type())
hpicfXpsSwitchIpsVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsSwitchIpsVoltage.setStatus(_A)
if mibBuilder.loadTexts:hpicfXpsSwitchIpsVoltage.setUnits('Volts')
_HpicfXpsSwitchIpsWattage_Type=Unsigned32
_HpicfXpsSwitchIpsWattage_Object=MibTableColumn
hpicfXpsSwitchIpsWattage=_HpicfXpsSwitchIpsWattage_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,2,1,9),_HpicfXpsSwitchIpsWattage_Type())
hpicfXpsSwitchIpsWattage.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsSwitchIpsWattage.setStatus(_A)
if mibBuilder.loadTexts:hpicfXpsSwitchIpsWattage.setUnits(_J)
_HpicfXpsPower_Type=Unsigned32
_HpicfXpsPower_Object=MibTableColumn
hpicfXpsPower=_HpicfXpsPower_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,2,1,10),_HpicfXpsPower_Type())
hpicfXpsPower.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsPower.setStatus(_A)
if mibBuilder.loadTexts:hpicfXpsPower.setUnits(_J)
_HpicfXpsSupportedCableVersion_Type=Unsigned32
_HpicfXpsSupportedCableVersion_Object=MibTableColumn
hpicfXpsSupportedCableVersion=_HpicfXpsSupportedCableVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,2,1,11),_HpicfXpsSupportedCableVersion_Type())
hpicfXpsSupportedCableVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsSupportedCableVersion.setStatus(_A)
_HpicfXpsSupportedZoneVersion_Type=Unsigned32
_HpicfXpsSupportedZoneVersion_Object=MibTableColumn
hpicfXpsSupportedZoneVersion=_HpicfXpsSupportedZoneVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,2,1,12),_HpicfXpsSupportedZoneVersion_Type())
hpicfXpsSupportedZoneVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsSupportedZoneVersion.setStatus(_A)
_HpicfXpsSwitchModType_Type=DisplayString
_HpicfXpsSwitchModType_Object=MibTableColumn
hpicfXpsSwitchModType=_HpicfXpsSwitchModType_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,2,1,13),_HpicfXpsSwitchModType_Type())
hpicfXpsSwitchModType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsSwitchModType.setStatus(_A)
_HpicfXpsSwitchConfigTable_Object=MibTable
hpicfXpsSwitchConfigTable=_HpicfXpsSwitchConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,3))
if mibBuilder.loadTexts:hpicfXpsSwitchConfigTable.setStatus(_A)
_HpicfXpsSwitchConfigEntry_Object=MibTableRow
hpicfXpsSwitchConfigEntry=_HpicfXpsSwitchConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,3,1))
hpicfXpsSwitchConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpicfXpsSwitchConfigEntry.setStatus(_A)
class _HpicfXpsSwitchAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_HpicfXpsSwitchAdminStatus_Type.__name__=_D
_HpicfXpsSwitchAdminStatus_Object=MibTableColumn
hpicfXpsSwitchAdminStatus=_HpicfXpsSwitchAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,3,1,1),_HpicfXpsSwitchAdminStatus_Type())
hpicfXpsSwitchAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfXpsSwitchAdminStatus.setStatus(_A)
class _HpicfXpsSwitchAutoRecovery_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_HpicfXpsSwitchAutoRecovery_Type.__name__=_D
_HpicfXpsSwitchAutoRecovery_Object=MibTableColumn
hpicfXpsSwitchAutoRecovery=_HpicfXpsSwitchAutoRecovery_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,3,1,2),_HpicfXpsSwitchAutoRecovery_Type())
hpicfXpsSwitchAutoRecovery.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfXpsSwitchAutoRecovery.setStatus(_A)
class _HpicfXpsAllowPortsSupported_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4))
_HpicfXpsAllowPortsSupported_Type.__name__=_I
_HpicfXpsAllowPortsSupported_Object=MibTableColumn
hpicfXpsAllowPortsSupported=_HpicfXpsAllowPortsSupported_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,3,1,3),_HpicfXpsAllowPortsSupported_Type())
hpicfXpsAllowPortsSupported.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfXpsAllowPortsSupported.setStatus(_A)
class _HpicfXpsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noReset',1),('factoryReset',2)))
_HpicfXpsReset_Type.__name__=_D
_HpicfXpsReset_Object=MibTableColumn
hpicfXpsReset=_HpicfXpsReset_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,3,1,4),_HpicfXpsReset_Type())
hpicfXpsReset.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfXpsReset.setStatus(_A)
class _HpicfXpsType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpicfXpsType_Type.__name__=_H
_HpicfXpsType_Object=MibTableColumn
hpicfXpsType=_HpicfXpsType_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,3,1,5),_HpicfXpsType_Type())
hpicfXpsType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsType.setStatus(_A)
_HpicfXpsSerialNum_Type=SnmpAdminString
_HpicfXpsSerialNum_Object=MibTableColumn
hpicfXpsSerialNum=_HpicfXpsSerialNum_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,3,1,6),_HpicfXpsSerialNum_Type())
hpicfXpsSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsSerialNum.setStatus(_A)
_HpicfXpsModuleName_Type=SnmpAdminString
_HpicfXpsModuleName_Object=MibTableColumn
hpicfXpsModuleName=_HpicfXpsModuleName_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,3,1,7),_HpicfXpsModuleName_Type())
hpicfXpsModuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsModuleName.setStatus(_A)
class _HpicfXpsPowerShareReqStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),(_e,2),(_f,3),(_g,4)))
_HpicfXpsPowerShareReqStatus_Type.__name__=_D
_HpicfXpsPowerShareReqStatus_Object=MibTableColumn
hpicfXpsPowerShareReqStatus=_HpicfXpsPowerShareReqStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,3,1,8),_HpicfXpsPowerShareReqStatus_Type())
hpicfXpsPowerShareReqStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsPowerShareReqStatus.setStatus(_A)
class _HpicfXpsResetReqStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),(_e,2),(_f,3),(_g,4)))
_HpicfXpsResetReqStatus_Type.__name__=_D
_HpicfXpsResetReqStatus_Object=MibTableColumn
hpicfXpsResetReqStatus=_HpicfXpsResetReqStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,3,1,9),_HpicfXpsResetReqStatus_Type())
hpicfXpsResetReqStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsResetReqStatus.setStatus(_A)
_HpicfXpsZoneTable_Object=MibTable
hpicfXpsZoneTable=_HpicfXpsZoneTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,4))
if mibBuilder.loadTexts:hpicfXpsZoneTable.setStatus(_A)
_HpicfXpsZoneEntry_Object=MibTableRow
hpicfXpsZoneEntry=_HpicfXpsZoneEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,4,1))
hpicfXpsZoneEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpicfXpsZoneEntry.setStatus(_A)
class _HpicfXpsZoneNo_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_HpicfXpsZoneNo_Type.__name__=_I
_HpicfXpsZoneNo_Object=MibTableColumn
hpicfXpsZoneNo=_HpicfXpsZoneNo_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,4,1,1),_HpicfXpsZoneNo_Type())
hpicfXpsZoneNo.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsZoneNo.setStatus(_A)
_HpicfXpsZoneState_Type=HpicfXpsZoneStatus
_HpicfXpsZoneState_Object=MibTableColumn
hpicfXpsZoneState=_HpicfXpsZoneState_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,4,1,2),_HpicfXpsZoneState_Type())
hpicfXpsZoneState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsZoneState.setStatus(_A)
class _HpicfXpsZonePowerShareMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpicfXpsZonePowerShareMap_Type.__name__=_H
_HpicfXpsZonePowerShareMap_Object=MibTableColumn
hpicfXpsZonePowerShareMap=_HpicfXpsZonePowerShareMap_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,4,1,3),_HpicfXpsZonePowerShareMap_Type())
hpicfXpsZonePowerShareMap.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfXpsZonePowerShareMap.setStatus(_A)
_HpicfXpsZoneVoltage_Type=Unsigned32
_HpicfXpsZoneVoltage_Object=MibTableColumn
hpicfXpsZoneVoltage=_HpicfXpsZoneVoltage_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,4,1,4),_HpicfXpsZoneVoltage_Type())
hpicfXpsZoneVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsZoneVoltage.setStatus(_A)
if mibBuilder.loadTexts:hpicfXpsZoneVoltage.setUnits('Volts')
_HpicfXpsZoneWattage_Type=Unsigned32
_HpicfXpsZoneWattage_Object=MibTableColumn
hpicfXpsZoneWattage=_HpicfXpsZoneWattage_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,4,1,5),_HpicfXpsZoneWattage_Type())
hpicfXpsZoneWattage.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsZoneWattage.setStatus(_A)
if mibBuilder.loadTexts:hpicfXpsZoneWattage.setUnits(_J)
_HpicfXpsPSURev_Type=Unsigned32
_HpicfXpsPSURev_Object=MibTableColumn
hpicfXpsPSURev=_HpicfXpsPSURev_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,4,1,6),_HpicfXpsPSURev_Type())
hpicfXpsPSURev.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsPSURev.setStatus(_A)
_HpicfXpsPSUModule_Type=SnmpAdminString
_HpicfXpsPSUModule_Object=MibTableColumn
hpicfXpsPSUModule=_HpicfXpsPSUModule_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,4,1,7),_HpicfXpsPSUModule_Type())
hpicfXpsPSUModule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsPSUModule.setStatus(_A)
_HpicfXpsZonePowerShareForce_Type=TruthValue
_HpicfXpsZonePowerShareForce_Object=MibTableColumn
hpicfXpsZonePowerShareForce=_HpicfXpsZonePowerShareForce_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,4,1,8),_HpicfXpsZonePowerShareForce_Type())
hpicfXpsZonePowerShareForce.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfXpsZonePowerShareForce.setStatus(_A)
_HpicfXpsZoneRecordVersion_Type=Unsigned32
_HpicfXpsZoneRecordVersion_Object=MibTableColumn
hpicfXpsZoneRecordVersion=_HpicfXpsZoneRecordVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,55,1,4,1,9),_HpicfXpsZoneRecordVersion_Type())
hpicfXpsZoneRecordVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXpsZoneRecordVersion.setStatus(_A)
_HpicfPsConformance_ObjectIdentity=ObjectIdentity
hpicfPsConformance=_HpicfPsConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,55,2))
_HpicfPsCompliance_ObjectIdentity=ObjectIdentity
hpicfPsCompliance=_HpicfPsCompliance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,55,2,1))
_HpicfPsGroups_ObjectIdentity=ObjectIdentity
hpicfPsGroups=_HpicfPsGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,55,2,2))
hpicfPsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,55,2,2,1))
hpicfPsGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:hpicfPsGroup.setStatus(_h)
hpicfXpsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,55,2,2,2))
hpicfXpsGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:hpicfXpsGroup.setStatus(_A)
hpicfXpsZoneGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,55,2,2,3))
hpicfXpsZoneGroup.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:hpicfXpsZoneGroup.setStatus(_A)
hpicfPsGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,55,2,2,4))
hpicfPsGroup1.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_AC)))
if mibBuilder.loadTexts:hpicfPsGroup1.setStatus(_A)
hpicfDcPsCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,55,2,1,1))
hpicfDcPsCompliance.setObjects(*((_B,_R),(_B,_R)))
if mibBuilder.loadTexts:hpicfDcPsCompliance.setStatus(_h)
hpicfXpsCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,55,2,1,2))
hpicfXpsCompliance.setObjects(*((_B,_S),(_B,_S)))
if mibBuilder.loadTexts:hpicfXpsCompliance.setStatus(_A)
hpicfXpsZoneCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,55,2,1,3))
hpicfXpsZoneCompliance.setObjects(*((_B,_T),(_B,_T)))
if mibBuilder.loadTexts:hpicfXpsZoneCompliance.setStatus(_A)
hpicfDcPsCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,55,2,1,4))
hpicfDcPsCompliance1.setObjects(*((_B,_U),(_B,_U)))
if mibBuilder.loadTexts:hpicfDcPsCompliance1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HpicfDcPsIndex':HpicfDcPsIndex,'HpicfDcPsState':HpicfDcPsState,'HpicfXpsConnectionStatus':HpicfXpsConnectionStatus,'HpicfXpsZoneStatus':HpicfXpsZoneStatus,'hpicfPsMIB':hpicfPsMIB,'hpicfEntityPs':hpicfEntityPs,'hpicfPsTable':hpicfPsTable,'hpicfPsEntry':hpicfPsEntry,_Z:hpicfPsBayNum,_K:hpicfPsState,_L:hpicfPsFailures,_M:hpicfPsTemp,_N:hpicfPsVoltageInfo,_O:hpicfPsWattageCur,_P:hpicfPsWattageMax,_Q:hpicfPsLastCall,_AC:hpicfPsModel,'hpicfXpsTable':hpicfXpsTable,'hpicfXpsEntry':hpicfXpsEntry,_b:hpicfXpsConnectingPort,_i:hpicfXpsPortOperStatus,_j:hpicfXpsSwitchSerialNo,_k:hpicfXpsConnectionState,_l:hpicfXpsSysName,_m:hpicfXpsMACAddress,_n:hpicfXpsSwitchOSVersion,_o:hpicfXpsSwitchIpsVoltage,_p:hpicfXpsSwitchIpsWattage,_q:hpicfXpsPower,_A0:hpicfXpsSupportedCableVersion,_A1:hpicfXpsSupportedZoneVersion,_A2:hpicfXpsSwitchModType,'hpicfXpsSwitchConfigTable':hpicfXpsSwitchConfigTable,'hpicfXpsSwitchConfigEntry':hpicfXpsSwitchConfigEntry,_r:hpicfXpsSwitchAdminStatus,_s:hpicfXpsSwitchAutoRecovery,_t:hpicfXpsAllowPortsSupported,_u:hpicfXpsReset,_v:hpicfXpsType,_w:hpicfXpsSerialNum,_x:hpicfXpsModuleName,_y:hpicfXpsPowerShareReqStatus,_z:hpicfXpsResetReqStatus,'hpicfXpsZoneTable':hpicfXpsZoneTable,'hpicfXpsZoneEntry':hpicfXpsZoneEntry,_A3:hpicfXpsZoneNo,_A4:hpicfXpsZoneState,_A5:hpicfXpsZonePowerShareMap,_A6:hpicfXpsZoneVoltage,_A7:hpicfXpsZoneWattage,_A8:hpicfXpsPSURev,_A9:hpicfXpsPSUModule,_AA:hpicfXpsZonePowerShareForce,_AB:hpicfXpsZoneRecordVersion,'hpicfPsConformance':hpicfPsConformance,'hpicfPsCompliance':hpicfPsCompliance,'hpicfDcPsCompliance':hpicfDcPsCompliance,'hpicfXpsCompliance':hpicfXpsCompliance,'hpicfXpsZoneCompliance':hpicfXpsZoneCompliance,'hpicfDcPsCompliance1':hpicfDcPsCompliance1,'hpicfPsGroups':hpicfPsGroups,_R:hpicfPsGroup,_S:hpicfXpsGroup,_T:hpicfXpsZoneGroup,_U:hpicfPsGroup1})