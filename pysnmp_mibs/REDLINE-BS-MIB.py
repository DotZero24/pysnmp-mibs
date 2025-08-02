_AH='redlineBsNotificationGroup'
_AG='redlineBsPowerSupplyAndCoolingGroup'
_AF='redlineBsSmcGroup'
_AE='redlineBsVlanGroup'
_AD='redlineBsEthGroup'
_AC='redlineBsPhyGroup'
_AB='redlineBsRfGroup'
_AA='redlineBsSystemGroup'
_A9='redlineBsConfigSaveGroup'
_A8='redlineBsSntpGroup'
_A7='redlineBsDhcpGroup'
_A6='redlineBsTempThresholdTrap'
_A5='redlineBsPowerSupplyStatusTrap'
_A4='redlineBsTrapTempThresholdIndex'
_A3='redlineBsTrapUnitIndex'
_A2='redlineBsTrapPowerSupplyIndex'
_A1='redlineBsFanStatus'
_A0='redlineBsFanName'
_z='redlineBsTempThresholdName'
_y='redlineBsTempTrapClrThreshold'
_x='redlineBsTempTrapThreshold'
_w='redlineBsUnitType'
_v='redlineBsUnitName'
_u='redlineBsPowerSupplyType'
_t='redlineBsPowerSupplyName'
_s='redlineBsSmcCurrentOperMode'
_r='redlineBsVlanId'
_q='redlineBsVlanTrafficTagging'
_p='redlineBsDataPortSettings'
_o='redlineBsManagementAccess'
_n='redlineBsChannelSize'
_m='redlineBsUplinkChanFreq'
_l='redlineBsDownlinkChanFreq'
_k='redlineBsRadioType'
_j='redlineBsSfConfigSave'
_i='redlineBsSnmpConfigSave'
_h='redlineBsTimezoneMin'
_g='redlineBsTimeServerIpAddress'
_f='redlineBsTimeServerIpAddressType'
_e='redlineBsTimezone'
_d='redlineBsDayLightSaving'
_c='redlineBsRefreshTime'
_b='redlineBsDhcpPacketsRelay'
_a='redlineBsIpAddressSource'
_Z='redlineBsFanIndex'
_Y='redlineBsTempThresholdIndex'
_X='redlineBsPowerSupplyIndex'
_W='halfDuplex10'
_V='halfDuplex100'
_U='fullDuplex10'
_T='fullDuplex100'
_S='autoDetect'
_R='InetAddressType'
_Q='OctetString'
_P='redlineBsTrapType'
_O='redlineBsTemperatureTrapTrigger'
_N='redlineBsCurrTemperature'
_M='redlineBsPowerSupplyStatus'
_L='degrees Celsius'
_K='redlineBsUnitIndex'
_J='off'
_I='noop'
_H='accessible-for-notify'
_G='not-accessible'
_F='DisplayString'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='REDLINE-BS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Q,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_R,'InetPortNumber')
redlineSystem,=mibBuilder.importSymbols('REDLINE-MIB','redlineSystem')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'PhysAddress','RowStatus','TextualConvention')
redlineBsMib=ModuleIdentity((1,3,6,1,4,1,10728,2,1,2))
if mibBuilder.loadTexts:redlineBsMib.setRevisions(('2005-10-28 15:43',))
_RedlineBsDhcpObjects_ObjectIdentity=ObjectIdentity
redlineBsDhcpObjects=_RedlineBsDhcpObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,2,1))
class _RedlineBsIpAddressSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dhcp',1),('static',2)))
_RedlineBsIpAddressSource_Type.__name__=_C
_RedlineBsIpAddressSource_Object=MibScalar
redlineBsIpAddressSource=_RedlineBsIpAddressSource_Object((1,3,6,1,4,1,10728,2,1,2,1,1),_RedlineBsIpAddressSource_Type())
redlineBsIpAddressSource.setMaxAccess(_E)
if mibBuilder.loadTexts:redlineBsIpAddressSource.setStatus(_A)
class _RedlineBsDhcpPacketsRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('relay',1),('notRelay',2)))
_RedlineBsDhcpPacketsRelay_Type.__name__=_C
_RedlineBsDhcpPacketsRelay_Object=MibScalar
redlineBsDhcpPacketsRelay=_RedlineBsDhcpPacketsRelay_Object((1,3,6,1,4,1,10728,2,1,2,1,2),_RedlineBsDhcpPacketsRelay_Type())
redlineBsDhcpPacketsRelay.setMaxAccess(_E)
if mibBuilder.loadTexts:redlineBsDhcpPacketsRelay.setStatus(_A)
_RedlineBsSntpObjects_ObjectIdentity=ObjectIdentity
redlineBsSntpObjects=_RedlineBsSntpObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,2,2))
class _RedlineBsRefreshTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),('refresh',2)))
_RedlineBsRefreshTime_Type.__name__=_C
_RedlineBsRefreshTime_Object=MibScalar
redlineBsRefreshTime=_RedlineBsRefreshTime_Object((1,3,6,1,4,1,10728,2,1,2,2,1),_RedlineBsRefreshTime_Type())
redlineBsRefreshTime.setMaxAccess(_E)
if mibBuilder.loadTexts:redlineBsRefreshTime.setStatus(_A)
class _RedlineBsDayLightSaving_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_J,2)))
_RedlineBsDayLightSaving_Type.__name__=_C
_RedlineBsDayLightSaving_Object=MibScalar
redlineBsDayLightSaving=_RedlineBsDayLightSaving_Object((1,3,6,1,4,1,10728,2,1,2,2,2),_RedlineBsDayLightSaving_Type())
redlineBsDayLightSaving.setMaxAccess(_E)
if mibBuilder.loadTexts:redlineBsDayLightSaving.setStatus(_A)
_RedlineBsTimezone_Type=Integer32
_RedlineBsTimezone_Object=MibScalar
redlineBsTimezone=_RedlineBsTimezone_Object((1,3,6,1,4,1,10728,2,1,2,2,3),_RedlineBsTimezone_Type())
redlineBsTimezone.setMaxAccess(_E)
if mibBuilder.loadTexts:redlineBsTimezone.setStatus(_A)
class _RedlineBsTimeServerIpAddressType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('ipv4',1))
_RedlineBsTimeServerIpAddressType_Type.__name__=_R
_RedlineBsTimeServerIpAddressType_Object=MibScalar
redlineBsTimeServerIpAddressType=_RedlineBsTimeServerIpAddressType_Object((1,3,6,1,4,1,10728,2,1,2,2,4),_RedlineBsTimeServerIpAddressType_Type())
redlineBsTimeServerIpAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:redlineBsTimeServerIpAddressType.setStatus(_A)
_RedlineBsTimeServerIpAddress_Type=InetAddress
_RedlineBsTimeServerIpAddress_Object=MibScalar
redlineBsTimeServerIpAddress=_RedlineBsTimeServerIpAddress_Object((1,3,6,1,4,1,10728,2,1,2,2,5),_RedlineBsTimeServerIpAddress_Type())
redlineBsTimeServerIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:redlineBsTimeServerIpAddress.setStatus(_A)
_RedlineBsTimezoneMin_Type=Integer32
_RedlineBsTimezoneMin_Object=MibScalar
redlineBsTimezoneMin=_RedlineBsTimezoneMin_Object((1,3,6,1,4,1,10728,2,1,2,2,6),_RedlineBsTimezoneMin_Type())
redlineBsTimezoneMin.setMaxAccess(_E)
if mibBuilder.loadTexts:redlineBsTimezoneMin.setStatus(_A)
_RedlineBsConfigSaveObjects_ObjectIdentity=ObjectIdentity
redlineBsConfigSaveObjects=_RedlineBsConfigSaveObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,2,3))
class _RedlineBsSnmpConfigSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),('save',2)))
_RedlineBsSnmpConfigSave_Type.__name__=_C
_RedlineBsSnmpConfigSave_Object=MibScalar
redlineBsSnmpConfigSave=_RedlineBsSnmpConfigSave_Object((1,3,6,1,4,1,10728,2,1,2,3,1),_RedlineBsSnmpConfigSave_Type())
redlineBsSnmpConfigSave.setMaxAccess(_E)
if mibBuilder.loadTexts:redlineBsSnmpConfigSave.setStatus(_A)
class _RedlineBsSfConfigSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),('save',2)))
_RedlineBsSfConfigSave_Type.__name__=_C
_RedlineBsSfConfigSave_Object=MibScalar
redlineBsSfConfigSave=_RedlineBsSfConfigSave_Object((1,3,6,1,4,1,10728,2,1,2,3,2),_RedlineBsSfConfigSave_Type())
redlineBsSfConfigSave.setMaxAccess(_E)
if mibBuilder.loadTexts:redlineBsSfConfigSave.setStatus(_A)
_RedlineBsSystemObjects_ObjectIdentity=ObjectIdentity
redlineBsSystemObjects=_RedlineBsSystemObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,2,4))
class _RedlineBsRadioType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RedlineBsRadioType_Type.__name__=_Q
_RedlineBsRadioType_Object=MibScalar
redlineBsRadioType=_RedlineBsRadioType_Object((1,3,6,1,4,1,10728,2,1,2,4,1),_RedlineBsRadioType_Type())
redlineBsRadioType.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsRadioType.setStatus(_A)
_RedlineBsRfObjects_ObjectIdentity=ObjectIdentity
redlineBsRfObjects=_RedlineBsRfObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,2,5))
_RedlineBsDownlinkChanFreq_Type=Unsigned32
_RedlineBsDownlinkChanFreq_Object=MibScalar
redlineBsDownlinkChanFreq=_RedlineBsDownlinkChanFreq_Object((1,3,6,1,4,1,10728,2,1,2,5,1),_RedlineBsDownlinkChanFreq_Type())
redlineBsDownlinkChanFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsDownlinkChanFreq.setStatus(_A)
if mibBuilder.loadTexts:redlineBsDownlinkChanFreq.setUnits('kHz')
_RedlineBsUplinkChanFreq_Type=Unsigned32
_RedlineBsUplinkChanFreq_Object=MibScalar
redlineBsUplinkChanFreq=_RedlineBsUplinkChanFreq_Object((1,3,6,1,4,1,10728,2,1,2,5,2),_RedlineBsUplinkChanFreq_Type())
redlineBsUplinkChanFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsUplinkChanFreq.setStatus(_A)
if mibBuilder.loadTexts:redlineBsUplinkChanFreq.setUnits('kHz')
_RedlineBsPhyObjects_ObjectIdentity=ObjectIdentity
redlineBsPhyObjects=_RedlineBsPhyObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,2,6))
_RedlineBsChannelSize_Type=Unsigned32
_RedlineBsChannelSize_Object=MibScalar
redlineBsChannelSize=_RedlineBsChannelSize_Object((1,3,6,1,4,1,10728,2,1,2,6,1),_RedlineBsChannelSize_Type())
redlineBsChannelSize.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsChannelSize.setStatus(_A)
if mibBuilder.loadTexts:redlineBsChannelSize.setUnits('KHz')
_RedlineBsEthObjects_ObjectIdentity=ObjectIdentity
redlineBsEthObjects=_RedlineBsEthObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,2,7))
class _RedlineBsManagementAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dataPort',1),('mgtPort',2)))
_RedlineBsManagementAccess_Type.__name__=_C
_RedlineBsManagementAccess_Object=MibScalar
redlineBsManagementAccess=_RedlineBsManagementAccess_Object((1,3,6,1,4,1,10728,2,1,2,7,1),_RedlineBsManagementAccess_Type())
redlineBsManagementAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsManagementAccess.setStatus(_A)
class _RedlineBsDataPortSettings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3),(_V,4),(_W,5)))
_RedlineBsDataPortSettings_Type.__name__=_C
_RedlineBsDataPortSettings_Object=MibScalar
redlineBsDataPortSettings=_RedlineBsDataPortSettings_Object((1,3,6,1,4,1,10728,2,1,2,7,2),_RedlineBsDataPortSettings_Type())
redlineBsDataPortSettings.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsDataPortSettings.setStatus(_A)
class _RedlineBsMgtPortSettings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3),(_V,4),(_W,5)))
_RedlineBsMgtPortSettings_Type.__name__=_C
_RedlineBsMgtPortSettings_Object=MibScalar
redlineBsMgtPortSettings=_RedlineBsMgtPortSettings_Object((1,3,6,1,4,1,10728,2,1,2,7,3),_RedlineBsMgtPortSettings_Type())
redlineBsMgtPortSettings.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsMgtPortSettings.setStatus(_A)
_RedlineBsVlanObjects_ObjectIdentity=ObjectIdentity
redlineBsVlanObjects=_RedlineBsVlanObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,2,8))
class _RedlineBsVlanTrafficTagging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_RedlineBsVlanTrafficTagging_Type.__name__=_C
_RedlineBsVlanTrafficTagging_Object=MibScalar
redlineBsVlanTrafficTagging=_RedlineBsVlanTrafficTagging_Object((1,3,6,1,4,1,10728,2,1,2,8,1),_RedlineBsVlanTrafficTagging_Type())
redlineBsVlanTrafficTagging.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsVlanTrafficTagging.setStatus(_A)
_RedlineBsVlanId_Type=Unsigned32
_RedlineBsVlanId_Object=MibScalar
redlineBsVlanId=_RedlineBsVlanId_Object((1,3,6,1,4,1,10728,2,1,2,8,2),_RedlineBsVlanId_Type())
redlineBsVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsVlanId.setStatus(_A)
_RedlineBsSmcObjects_ObjectIdentity=ObjectIdentity
redlineBsSmcObjects=_RedlineBsSmcObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,2,9))
class _RedlineBsSmcCurrentOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('maintenance',2)))
_RedlineBsSmcCurrentOperMode_Type.__name__=_C
_RedlineBsSmcCurrentOperMode_Object=MibScalar
redlineBsSmcCurrentOperMode=_RedlineBsSmcCurrentOperMode_Object((1,3,6,1,4,1,10728,2,1,2,9,1),_RedlineBsSmcCurrentOperMode_Type())
redlineBsSmcCurrentOperMode.setMaxAccess(_E)
if mibBuilder.loadTexts:redlineBsSmcCurrentOperMode.setStatus(_A)
_RedlineBsPowerSupplyAndCoolingObjects_ObjectIdentity=ObjectIdentity
redlineBsPowerSupplyAndCoolingObjects=_RedlineBsPowerSupplyAndCoolingObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,2,10))
_RedlineBsPowerSupplyTable_Object=MibTable
redlineBsPowerSupplyTable=_RedlineBsPowerSupplyTable_Object((1,3,6,1,4,1,10728,2,1,2,10,1))
if mibBuilder.loadTexts:redlineBsPowerSupplyTable.setStatus(_A)
_RedlineBsPowerSupplyEntry_Object=MibTableRow
redlineBsPowerSupplyEntry=_RedlineBsPowerSupplyEntry_Object((1,3,6,1,4,1,10728,2,1,2,10,1,1))
redlineBsPowerSupplyEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:redlineBsPowerSupplyEntry.setStatus(_A)
_RedlineBsPowerSupplyIndex_Type=Integer32
_RedlineBsPowerSupplyIndex_Object=MibTableColumn
redlineBsPowerSupplyIndex=_RedlineBsPowerSupplyIndex_Object((1,3,6,1,4,1,10728,2,1,2,10,1,1,1),_RedlineBsPowerSupplyIndex_Type())
redlineBsPowerSupplyIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:redlineBsPowerSupplyIndex.setStatus(_A)
class _RedlineBsPowerSupplyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RedlineBsPowerSupplyName_Type.__name__=_F
_RedlineBsPowerSupplyName_Object=MibTableColumn
redlineBsPowerSupplyName=_RedlineBsPowerSupplyName_Object((1,3,6,1,4,1,10728,2,1,2,10,1,1,2),_RedlineBsPowerSupplyName_Type())
redlineBsPowerSupplyName.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsPowerSupplyName.setStatus(_A)
class _RedlineBsPowerSupplyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('internal',1),('external',2),('externalShared',3)))
_RedlineBsPowerSupplyType_Type.__name__=_C
_RedlineBsPowerSupplyType_Object=MibTableColumn
redlineBsPowerSupplyType=_RedlineBsPowerSupplyType_Object((1,3,6,1,4,1,10728,2,1,2,10,1,1,3),_RedlineBsPowerSupplyType_Type())
redlineBsPowerSupplyType.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsPowerSupplyType.setStatus(_A)
class _RedlineBsPowerSupplyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_J,2)))
_RedlineBsPowerSupplyStatus_Type.__name__=_C
_RedlineBsPowerSupplyStatus_Object=MibTableColumn
redlineBsPowerSupplyStatus=_RedlineBsPowerSupplyStatus_Object((1,3,6,1,4,1,10728,2,1,2,10,1,1,4),_RedlineBsPowerSupplyStatus_Type())
redlineBsPowerSupplyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsPowerSupplyStatus.setStatus(_A)
_RedlineBsTemperatureTable_Object=MibTable
redlineBsTemperatureTable=_RedlineBsTemperatureTable_Object((1,3,6,1,4,1,10728,2,1,2,10,2))
if mibBuilder.loadTexts:redlineBsTemperatureTable.setStatus(_A)
_RedlineBsTemperatureEntry_Object=MibTableRow
redlineBsTemperatureEntry=_RedlineBsTemperatureEntry_Object((1,3,6,1,4,1,10728,2,1,2,10,2,1))
redlineBsTemperatureEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:redlineBsTemperatureEntry.setStatus(_A)
_RedlineBsUnitIndex_Type=Integer32
_RedlineBsUnitIndex_Object=MibTableColumn
redlineBsUnitIndex=_RedlineBsUnitIndex_Object((1,3,6,1,4,1,10728,2,1,2,10,2,1,1),_RedlineBsUnitIndex_Type())
redlineBsUnitIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:redlineBsUnitIndex.setStatus(_A)
class _RedlineBsUnitName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RedlineBsUnitName_Type.__name__=_F
_RedlineBsUnitName_Object=MibTableColumn
redlineBsUnitName=_RedlineBsUnitName_Object((1,3,6,1,4,1,10728,2,1,2,10,2,1,2),_RedlineBsUnitName_Type())
redlineBsUnitName.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsUnitName.setStatus(_A)
class _RedlineBsUnitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('indoor',1),('outdoor',2)))
_RedlineBsUnitType_Type.__name__=_C
_RedlineBsUnitType_Object=MibTableColumn
redlineBsUnitType=_RedlineBsUnitType_Object((1,3,6,1,4,1,10728,2,1,2,10,2,1,3),_RedlineBsUnitType_Type())
redlineBsUnitType.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsUnitType.setStatus(_A)
class _RedlineBsCurrTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,100))
_RedlineBsCurrTemperature_Type.__name__=_C
_RedlineBsCurrTemperature_Object=MibTableColumn
redlineBsCurrTemperature=_RedlineBsCurrTemperature_Object((1,3,6,1,4,1,10728,2,1,2,10,2,1,4),_RedlineBsCurrTemperature_Type())
redlineBsCurrTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsCurrTemperature.setStatus(_A)
if mibBuilder.loadTexts:redlineBsCurrTemperature.setUnits(_L)
_RedlineBsTempThresholdTable_Object=MibTable
redlineBsTempThresholdTable=_RedlineBsTempThresholdTable_Object((1,3,6,1,4,1,10728,2,1,2,10,3))
if mibBuilder.loadTexts:redlineBsTempThresholdTable.setStatus(_A)
_RedlineBsTempThresholdEntry_Object=MibTableRow
redlineBsTempThresholdEntry=_RedlineBsTempThresholdEntry_Object((1,3,6,1,4,1,10728,2,1,2,10,3,1))
redlineBsTempThresholdEntry.setIndexNames((0,_B,_K),(0,_B,_Y))
if mibBuilder.loadTexts:redlineBsTempThresholdEntry.setStatus(_A)
_RedlineBsTempThresholdIndex_Type=Integer32
_RedlineBsTempThresholdIndex_Object=MibTableColumn
redlineBsTempThresholdIndex=_RedlineBsTempThresholdIndex_Object((1,3,6,1,4,1,10728,2,1,2,10,3,1,1),_RedlineBsTempThresholdIndex_Type())
redlineBsTempThresholdIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:redlineBsTempThresholdIndex.setStatus(_A)
class _RedlineBsTempTrapThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,100))
_RedlineBsTempTrapThreshold_Type.__name__=_C
_RedlineBsTempTrapThreshold_Object=MibTableColumn
redlineBsTempTrapThreshold=_RedlineBsTempTrapThreshold_Object((1,3,6,1,4,1,10728,2,1,2,10,3,1,2),_RedlineBsTempTrapThreshold_Type())
redlineBsTempTrapThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsTempTrapThreshold.setStatus(_A)
if mibBuilder.loadTexts:redlineBsTempTrapThreshold.setUnits(_L)
class _RedlineBsTempTrapClrThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,100))
_RedlineBsTempTrapClrThreshold_Type.__name__=_C
_RedlineBsTempTrapClrThreshold_Object=MibTableColumn
redlineBsTempTrapClrThreshold=_RedlineBsTempTrapClrThreshold_Object((1,3,6,1,4,1,10728,2,1,2,10,3,1,3),_RedlineBsTempTrapClrThreshold_Type())
redlineBsTempTrapClrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsTempTrapClrThreshold.setStatus(_A)
if mibBuilder.loadTexts:redlineBsTempTrapClrThreshold.setUnits(_L)
class _RedlineBsTempThresholdName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RedlineBsTempThresholdName_Type.__name__=_F
_RedlineBsTempThresholdName_Object=MibTableColumn
redlineBsTempThresholdName=_RedlineBsTempThresholdName_Object((1,3,6,1,4,1,10728,2,1,2,10,3,1,4),_RedlineBsTempThresholdName_Type())
redlineBsTempThresholdName.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsTempThresholdName.setStatus(_A)
class _RedlineBsTemperatureTrapTrigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('temperatureRising',1),('temperatureFalling',2)))
_RedlineBsTemperatureTrapTrigger_Type.__name__=_C
_RedlineBsTemperatureTrapTrigger_Object=MibTableColumn
redlineBsTemperatureTrapTrigger=_RedlineBsTemperatureTrapTrigger_Object((1,3,6,1,4,1,10728,2,1,2,10,3,1,5),_RedlineBsTemperatureTrapTrigger_Type())
redlineBsTemperatureTrapTrigger.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsTemperatureTrapTrigger.setStatus(_A)
_RedlineBsFanTable_Object=MibTable
redlineBsFanTable=_RedlineBsFanTable_Object((1,3,6,1,4,1,10728,2,1,2,10,4))
if mibBuilder.loadTexts:redlineBsFanTable.setStatus(_A)
_RedlineBsFanEntry_Object=MibTableRow
redlineBsFanEntry=_RedlineBsFanEntry_Object((1,3,6,1,4,1,10728,2,1,2,10,4,1))
redlineBsFanEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:redlineBsFanEntry.setStatus(_A)
_RedlineBsFanIndex_Type=Integer32
_RedlineBsFanIndex_Object=MibTableColumn
redlineBsFanIndex=_RedlineBsFanIndex_Object((1,3,6,1,4,1,10728,2,1,2,10,4,1,1),_RedlineBsFanIndex_Type())
redlineBsFanIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:redlineBsFanIndex.setStatus(_A)
class _RedlineBsFanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RedlineBsFanName_Type.__name__=_F
_RedlineBsFanName_Object=MibTableColumn
redlineBsFanName=_RedlineBsFanName_Object((1,3,6,1,4,1,10728,2,1,2,10,4,1,2),_RedlineBsFanName_Type())
redlineBsFanName.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsFanName.setStatus(_A)
class _RedlineBsFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_J,2)))
_RedlineBsFanStatus_Type.__name__=_C
_RedlineBsFanStatus_Object=MibTableColumn
redlineBsFanStatus=_RedlineBsFanStatus_Object((1,3,6,1,4,1,10728,2,1,2,10,4,1,3),_RedlineBsFanStatus_Type())
redlineBsFanStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:redlineBsFanStatus.setStatus(_A)
_RedlineBsNotificationObjects_ObjectIdentity=ObjectIdentity
redlineBsNotificationObjects=_RedlineBsNotificationObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,2,11))
_RedlineBsTrapDefinitions_ObjectIdentity=ObjectIdentity
redlineBsTrapDefinitions=_RedlineBsTrapDefinitions_ObjectIdentity((1,3,6,1,4,1,10728,2,1,2,11,0))
_RedlineBsTrapMibObjects_ObjectIdentity=ObjectIdentity
redlineBsTrapMibObjects=_RedlineBsTrapMibObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,2,11,1))
class _RedlineBsTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trapSet',1),('trapClr',2)))
_RedlineBsTrapType_Type.__name__=_C
_RedlineBsTrapType_Object=MibScalar
redlineBsTrapType=_RedlineBsTrapType_Object((1,3,6,1,4,1,10728,2,1,2,11,1,1),_RedlineBsTrapType_Type())
redlineBsTrapType.setMaxAccess(_H)
if mibBuilder.loadTexts:redlineBsTrapType.setStatus(_A)
_RedlineBsTrapPowerSupplyIndex_Type=Integer32
_RedlineBsTrapPowerSupplyIndex_Object=MibScalar
redlineBsTrapPowerSupplyIndex=_RedlineBsTrapPowerSupplyIndex_Object((1,3,6,1,4,1,10728,2,1,2,11,1,2),_RedlineBsTrapPowerSupplyIndex_Type())
redlineBsTrapPowerSupplyIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:redlineBsTrapPowerSupplyIndex.setStatus(_A)
_RedlineBsTrapUnitIndex_Type=Integer32
_RedlineBsTrapUnitIndex_Object=MibScalar
redlineBsTrapUnitIndex=_RedlineBsTrapUnitIndex_Object((1,3,6,1,4,1,10728,2,1,2,11,1,3),_RedlineBsTrapUnitIndex_Type())
redlineBsTrapUnitIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:redlineBsTrapUnitIndex.setStatus(_A)
_RedlineBsTrapTempThresholdIndex_Type=Integer32
_RedlineBsTrapTempThresholdIndex_Object=MibScalar
redlineBsTrapTempThresholdIndex=_RedlineBsTrapTempThresholdIndex_Object((1,3,6,1,4,1,10728,2,1,2,11,1,4),_RedlineBsTrapTempThresholdIndex_Type())
redlineBsTrapTempThresholdIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:redlineBsTrapTempThresholdIndex.setStatus(_A)
_RedlineBsConformance_ObjectIdentity=ObjectIdentity
redlineBsConformance=_RedlineBsConformance_ObjectIdentity((1,3,6,1,4,1,10728,2,1,2,12))
_RedlineBsGroups_ObjectIdentity=ObjectIdentity
redlineBsGroups=_RedlineBsGroups_ObjectIdentity((1,3,6,1,4,1,10728,2,1,2,12,1))
_RedlineBsCompls_ObjectIdentity=ObjectIdentity
redlineBsCompls=_RedlineBsCompls_ObjectIdentity((1,3,6,1,4,1,10728,2,1,2,12,2))
redlineBsDhcpGroup=ObjectGroup((1,3,6,1,4,1,10728,2,1,2,12,1,1))
redlineBsDhcpGroup.setObjects(*((_B,_a),(_B,_b)))
if mibBuilder.loadTexts:redlineBsDhcpGroup.setStatus(_A)
redlineBsSntpGroup=ObjectGroup((1,3,6,1,4,1,10728,2,1,2,12,1,2))
redlineBsSntpGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:redlineBsSntpGroup.setStatus(_A)
redlineBsConfigSaveGroup=ObjectGroup((1,3,6,1,4,1,10728,2,1,2,12,1,3))
redlineBsConfigSaveGroup.setObjects(*((_B,_i),(_B,_j)))
if mibBuilder.loadTexts:redlineBsConfigSaveGroup.setStatus(_A)
redlineBsSystemGroup=ObjectGroup((1,3,6,1,4,1,10728,2,1,2,12,1,4))
redlineBsSystemGroup.setObjects((_B,_k))
if mibBuilder.loadTexts:redlineBsSystemGroup.setStatus(_A)
redlineBsRfGroup=ObjectGroup((1,3,6,1,4,1,10728,2,1,2,12,1,5))
redlineBsRfGroup.setObjects(*((_B,_l),(_B,_m)))
if mibBuilder.loadTexts:redlineBsRfGroup.setStatus(_A)
redlineBsPhyGroup=ObjectGroup((1,3,6,1,4,1,10728,2,1,2,12,1,6))
redlineBsPhyGroup.setObjects((_B,_n))
if mibBuilder.loadTexts:redlineBsPhyGroup.setStatus(_A)
redlineBsEthGroup=ObjectGroup((1,3,6,1,4,1,10728,2,1,2,12,1,7))
redlineBsEthGroup.setObjects(*((_B,_o),(_B,_p)))
if mibBuilder.loadTexts:redlineBsEthGroup.setStatus(_A)
redlineBsVlanGroup=ObjectGroup((1,3,6,1,4,1,10728,2,1,2,12,1,8))
redlineBsVlanGroup.setObjects(*((_B,_q),(_B,_r)))
if mibBuilder.loadTexts:redlineBsVlanGroup.setStatus(_A)
redlineBsSmcGroup=ObjectGroup((1,3,6,1,4,1,10728,2,1,2,12,1,9))
redlineBsSmcGroup.setObjects((_B,_s))
if mibBuilder.loadTexts:redlineBsSmcGroup.setStatus(_A)
redlineBsPowerSupplyAndCoolingGroup=ObjectGroup((1,3,6,1,4,1,10728,2,1,2,12,1,10))
redlineBsPowerSupplyAndCoolingGroup.setObjects(*((_B,_t),(_B,_u),(_B,_M),(_B,_v),(_B,_w),(_B,_N),(_B,_x),(_B,_y),(_B,_z),(_B,_O),(_B,_A0),(_B,_A1),(_B,_P)))
if mibBuilder.loadTexts:redlineBsPowerSupplyAndCoolingGroup.setStatus(_A)
redlineBsPowerSupplyStatusTrap=NotificationType((1,3,6,1,4,1,10728,2,1,2,11,0,1))
redlineBsPowerSupplyStatusTrap.setObjects(*((_B,_A2),(_B,_M)))
if mibBuilder.loadTexts:redlineBsPowerSupplyStatusTrap.setStatus(_A)
redlineBsTempThresholdTrap=NotificationType((1,3,6,1,4,1,10728,2,1,2,11,0,2))
redlineBsTempThresholdTrap.setObjects(*((_B,_A3),(_B,_A4),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:redlineBsTempThresholdTrap.setStatus(_A)
redlineBsNotificationGroup=NotificationGroup((1,3,6,1,4,1,10728,2,1,2,12,1,11))
redlineBsNotificationGroup.setObjects(*((_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:redlineBsNotificationGroup.setStatus(_A)
redlineBsCompliance=ModuleCompliance((1,3,6,1,4,1,10728,2,1,2,12,2,1))
redlineBsCompliance.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:redlineBsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'redlineBsMib':redlineBsMib,'redlineBsDhcpObjects':redlineBsDhcpObjects,_a:redlineBsIpAddressSource,_b:redlineBsDhcpPacketsRelay,'redlineBsSntpObjects':redlineBsSntpObjects,_c:redlineBsRefreshTime,_d:redlineBsDayLightSaving,_e:redlineBsTimezone,_f:redlineBsTimeServerIpAddressType,_g:redlineBsTimeServerIpAddress,_h:redlineBsTimezoneMin,'redlineBsConfigSaveObjects':redlineBsConfigSaveObjects,_i:redlineBsSnmpConfigSave,_j:redlineBsSfConfigSave,'redlineBsSystemObjects':redlineBsSystemObjects,_k:redlineBsRadioType,'redlineBsRfObjects':redlineBsRfObjects,_l:redlineBsDownlinkChanFreq,_m:redlineBsUplinkChanFreq,'redlineBsPhyObjects':redlineBsPhyObjects,_n:redlineBsChannelSize,'redlineBsEthObjects':redlineBsEthObjects,_o:redlineBsManagementAccess,_p:redlineBsDataPortSettings,'redlineBsMgtPortSettings':redlineBsMgtPortSettings,'redlineBsVlanObjects':redlineBsVlanObjects,_q:redlineBsVlanTrafficTagging,_r:redlineBsVlanId,'redlineBsSmcObjects':redlineBsSmcObjects,_s:redlineBsSmcCurrentOperMode,'redlineBsPowerSupplyAndCoolingObjects':redlineBsPowerSupplyAndCoolingObjects,'redlineBsPowerSupplyTable':redlineBsPowerSupplyTable,'redlineBsPowerSupplyEntry':redlineBsPowerSupplyEntry,_X:redlineBsPowerSupplyIndex,_t:redlineBsPowerSupplyName,_u:redlineBsPowerSupplyType,_M:redlineBsPowerSupplyStatus,'redlineBsTemperatureTable':redlineBsTemperatureTable,'redlineBsTemperatureEntry':redlineBsTemperatureEntry,_K:redlineBsUnitIndex,_v:redlineBsUnitName,_w:redlineBsUnitType,_N:redlineBsCurrTemperature,'redlineBsTempThresholdTable':redlineBsTempThresholdTable,'redlineBsTempThresholdEntry':redlineBsTempThresholdEntry,_Y:redlineBsTempThresholdIndex,_x:redlineBsTempTrapThreshold,_y:redlineBsTempTrapClrThreshold,_z:redlineBsTempThresholdName,_O:redlineBsTemperatureTrapTrigger,'redlineBsFanTable':redlineBsFanTable,'redlineBsFanEntry':redlineBsFanEntry,_Z:redlineBsFanIndex,_A0:redlineBsFanName,_A1:redlineBsFanStatus,'redlineBsNotificationObjects':redlineBsNotificationObjects,'redlineBsTrapDefinitions':redlineBsTrapDefinitions,_A5:redlineBsPowerSupplyStatusTrap,_A6:redlineBsTempThresholdTrap,'redlineBsTrapMibObjects':redlineBsTrapMibObjects,_P:redlineBsTrapType,_A2:redlineBsTrapPowerSupplyIndex,_A3:redlineBsTrapUnitIndex,_A4:redlineBsTrapTempThresholdIndex,'redlineBsConformance':redlineBsConformance,'redlineBsGroups':redlineBsGroups,_A7:redlineBsDhcpGroup,_A8:redlineBsSntpGroup,_A9:redlineBsConfigSaveGroup,_AA:redlineBsSystemGroup,_AB:redlineBsRfGroup,_AC:redlineBsPhyGroup,_AD:redlineBsEthGroup,_AE:redlineBsVlanGroup,_AF:redlineBsSmcGroup,_AG:redlineBsPowerSupplyAndCoolingGroup,_AH:redlineBsNotificationGroup,'redlineBsCompls':redlineBsCompls,'redlineBsCompliance':redlineBsCompliance})