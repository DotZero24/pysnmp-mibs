_AR='infoLastPortStateChangeSource'
_AQ='portAdminState'
_AP='infoLastConfigChangeSource'
_AO='infoTotalConfigChanges'
_AN='infoLastFuncInputAlarmNumber'
_AM='infoLastFuncInputAlarmName'
_AL='infoLastFuncInputAlarmState'
_AK='infoLastInternalMgmtWarning'
_AJ='infoLastSfpEventMessage'
_AI='infoLastTftpMessage'
_AH='infoPowerVoltage3300'
_AG='infoPowerVoltage2500'
_AF='adminAlarmNameM2'
_AE='infoAlarmStateM2'
_AD='adminAlarmNameM1'
_AC='infoAlarmStateM1'
_AB='portPoePower'
_AA='infoPoeInputPower'
_A9='infoPoeInputVoltage'
_A8='portErrorCounter'
_A7='infoNewMacAddr'
_A6='portLinkState'
_A5='infoTemperature'
_A4='sfpPortIndex'
_A3='vlanIndex'
_A2='limit256M'
_A1='limit128M'
_A0='limit512k'
_z='limit256k'
_y='limit128k'
_x='allwaysOn'
_w='allwaysOff'
_v='allwaysEnable'
_u='alarmForceContactOpenShorted'
_t='alarmForceContactOpen'
_s='alarmForceContactShorted'
_r='alarmLocalAlarmDestination'
_q='alarmRemoteAlarmDestination'
_p='alarmRemoteFunctionInput'
_o='alarmLocalFunctionInputOpen'
_n='alarmLocalFunctionInputShorted'
_m='alarmPowerSupply1or2Failure'
_l='alarmPowerSupply2Failure'
_k='alarmPowerSupply1Failure'
_j='alarmLinkDown'
_i='alarmContactForcedOpen'
_h='alarmContactForcedShorted'
_g='alarmOnLocalAlarmDestTable'
_f='alarmOnRemoteAlarmDestTable'
_e='alarmOnRemoteFunctionInput'
_d='alarmOnFunctionInputOpen'
_c='alarmOnFunctionInputShorted'
_b='alarmOnPowerSupplyS1orS2'
_a='alarmOnPowerSupplyS2'
_Z='alarmOnPowerSupplyS1'
_Y='alarmOnLinkDown'
_X='alarmOn'
_W='alarmOff'
_V='dot1dStpPortState'
_U='BRIDGE-MIB'
_T='infoUnauthIpAddr'
_S='infoSecurityFailMacAddr'
_R='alarmOffForced'
_Q='alarmOnForced'
_P='enable'
_O='functionInputOpen'
_N='functionInputShorted'
_M='not defined'
_L='accessible-for-notify'
_K='disable'
_J='portName'
_I='portDescr'
_H='portIndex'
_G='notSupported'
_F='DisplayString'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='NEXANS-BM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dStpPortState,=mibBuilder.importSymbols(_U,_V)
nexansANS,=mibBuilder.importSymbols('NEXANS-MIB','nexansANS')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','TextualConvention')
bmSwitchMIB=ModuleIdentity((1,3,6,1,4,1,266,20))
if mibBuilder.loadTexts:bmSwitchMIB.setRevisions(('2017-01-24 00:00',))
_BmTraps_ObjectIdentity=ObjectIdentity
bmTraps=_BmTraps_ObjectIdentity((1,3,6,1,4,1,266,20,0))
_BmSwitchInfo_ObjectIdentity=ObjectIdentity
bmSwitchInfo=_BmSwitchInfo_ObjectIdentity((1,3,6,1,4,1,266,20,1))
class _InfoDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_InfoDescr_Type.__name__=_F
_InfoDescr_Object=MibScalar
infoDescr=_InfoDescr_Object((1,3,6,1,4,1,266,20,1,1),_InfoDescr_Type())
infoDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:infoDescr.setStatus(_A)
_InfoType_Type=Integer32
_InfoType_Object=MibScalar
infoType=_InfoType_Object((1,3,6,1,4,1,266,20,1,2),_InfoType_Type())
infoType.setMaxAccess(_C)
if mibBuilder.loadTexts:infoType.setStatus(_A)
class _InfoProductNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_InfoProductNo_Type.__name__=_F
_InfoProductNo_Object=MibScalar
infoProductNo=_InfoProductNo_Object((1,3,6,1,4,1,266,20,1,3),_InfoProductNo_Type())
infoProductNo.setMaxAccess(_C)
if mibBuilder.loadTexts:infoProductNo.setStatus(_A)
class _InfoSerie_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
_InfoSerie_Type.__name__=_F
_InfoSerie_Object=MibScalar
infoSerie=_InfoSerie_Object((1,3,6,1,4,1,266,20,1,4),_InfoSerie_Type())
infoSerie.setMaxAccess(_C)
if mibBuilder.loadTexts:infoSerie.setStatus(_A)
class _InfoSeriesNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
_InfoSeriesNo_Type.__name__=_F
_InfoSeriesNo_Object=MibScalar
infoSeriesNo=_InfoSeriesNo_Object((1,3,6,1,4,1,266,20,1,5),_InfoSeriesNo_Type())
infoSeriesNo.setMaxAccess(_C)
if mibBuilder.loadTexts:infoSeriesNo.setStatus(_A)
class _InfoManufactureDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_InfoManufactureDate_Type.__name__=_F
_InfoManufactureDate_Object=MibScalar
infoManufactureDate=_InfoManufactureDate_Object((1,3,6,1,4,1,266,20,1,6),_InfoManufactureDate_Type())
infoManufactureDate.setMaxAccess(_C)
if mibBuilder.loadTexts:infoManufactureDate.setStatus(_A)
class _InfoSwitchHardwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
_InfoSwitchHardwareVersion_Type.__name__=_F
_InfoSwitchHardwareVersion_Object=MibScalar
infoSwitchHardwareVersion=_InfoSwitchHardwareVersion_Object((1,3,6,1,4,1,266,20,1,7),_InfoSwitchHardwareVersion_Type())
infoSwitchHardwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:infoSwitchHardwareVersion.setStatus(_A)
class _InfoMgmtHardwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
_InfoMgmtHardwareVersion_Type.__name__=_F
_InfoMgmtHardwareVersion_Object=MibScalar
infoMgmtHardwareVersion=_InfoMgmtHardwareVersion_Object((1,3,6,1,4,1,266,20,1,8),_InfoMgmtHardwareVersion_Type())
infoMgmtHardwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:infoMgmtHardwareVersion.setStatus(_A)
class _InfoMgmtFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_InfoMgmtFirmwareVersion_Type.__name__=_F
_InfoMgmtFirmwareVersion_Object=MibScalar
infoMgmtFirmwareVersion=_InfoMgmtFirmwareVersion_Object((1,3,6,1,4,1,266,20,1,9),_InfoMgmtFirmwareVersion_Type())
infoMgmtFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:infoMgmtFirmwareVersion.setStatus(_A)
_InfoNoOfPorts_Type=Integer32
_InfoNoOfPorts_Object=MibScalar
infoNoOfPorts=_InfoNoOfPorts_Object((1,3,6,1,4,1,266,20,1,10),_InfoNoOfPorts_Type())
infoNoOfPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:infoNoOfPorts.setStatus(_A)
_InfoNoOfReboots_Type=Counter32
_InfoNoOfReboots_Object=MibScalar
infoNoOfReboots=_InfoNoOfReboots_Object((1,3,6,1,4,1,266,20,1,11),_InfoNoOfReboots_Type())
infoNoOfReboots.setMaxAccess(_C)
if mibBuilder.loadTexts:infoNoOfReboots.setStatus(_A)
_InfoTemperature_Type=Integer32
_InfoTemperature_Object=MibScalar
infoTemperature=_InfoTemperature_Object((1,3,6,1,4,1,266,20,1,12),_InfoTemperature_Type())
infoTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:infoTemperature.setStatus(_A)
_InfoTemperatureMaxAllowed_Type=Integer32
_InfoTemperatureMaxAllowed_Object=MibScalar
infoTemperatureMaxAllowed=_InfoTemperatureMaxAllowed_Object((1,3,6,1,4,1,266,20,1,13),_InfoTemperatureMaxAllowed_Type())
infoTemperatureMaxAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:infoTemperatureMaxAllowed.setStatus(_A)
_InfoPowerVoltage2500_Type=Integer32
_InfoPowerVoltage2500_Object=MibScalar
infoPowerVoltage2500=_InfoPowerVoltage2500_Object((1,3,6,1,4,1,266,20,1,14),_InfoPowerVoltage2500_Type())
infoPowerVoltage2500.setMaxAccess(_C)
if mibBuilder.loadTexts:infoPowerVoltage2500.setStatus(_A)
_InfoPowerVoltage3300_Type=Integer32
_InfoPowerVoltage3300_Object=MibScalar
infoPowerVoltage3300=_InfoPowerVoltage3300_Object((1,3,6,1,4,1,266,20,1,15),_InfoPowerVoltage3300_Type())
infoPowerVoltage3300.setMaxAccess(_C)
if mibBuilder.loadTexts:infoPowerVoltage3300.setStatus(_A)
_InfoUnauthIpAddr_Type=IpAddress
_InfoUnauthIpAddr_Object=MibScalar
infoUnauthIpAddr=_InfoUnauthIpAddr_Object((1,3,6,1,4,1,266,20,1,16),_InfoUnauthIpAddr_Type())
infoUnauthIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:infoUnauthIpAddr.setStatus(_A)
class _InfoSecurityFailMacAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_InfoSecurityFailMacAddr_Type.__name__=_F
_InfoSecurityFailMacAddr_Object=MibScalar
infoSecurityFailMacAddr=_InfoSecurityFailMacAddr_Object((1,3,6,1,4,1,266,20,1,17),_InfoSecurityFailMacAddr_Type())
infoSecurityFailMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:infoSecurityFailMacAddr.setStatus(_A)
class _InfoNewMacAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_InfoNewMacAddr_Type.__name__=_F
_InfoNewMacAddr_Object=MibScalar
infoNewMacAddr=_InfoNewMacAddr_Object((1,3,6,1,4,1,266,20,1,18),_InfoNewMacAddr_Type())
infoNewMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:infoNewMacAddr.setStatus(_A)
_InfoPoeInputVoltage_Type=Integer32
_InfoPoeInputVoltage_Object=MibScalar
infoPoeInputVoltage=_InfoPoeInputVoltage_Object((1,3,6,1,4,1,266,20,1,19),_InfoPoeInputVoltage_Type())
infoPoeInputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:infoPoeInputVoltage.setStatus(_A)
_InfoPoeInputPower_Type=Integer32
_InfoPoeInputPower_Object=MibScalar
infoPoeInputPower=_InfoPoeInputPower_Object((1,3,6,1,4,1,266,20,1,20),_InfoPoeInputPower_Type())
infoPoeInputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:infoPoeInputPower.setStatus(_A)
class _InfoAlarmStateM1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_G,1),(_W,2),(_X,3),(_Y,4),(_Q,5),(_R,6),(_Z,7),(_a,8),(_b,9),(_c,10),(_d,11),(_e,12),(_f,13),(_g,14),(_h,15),(_i,16)))
_InfoAlarmStateM1_Type.__name__=_E
_InfoAlarmStateM1_Object=MibScalar
infoAlarmStateM1=_InfoAlarmStateM1_Object((1,3,6,1,4,1,266,20,1,21),_InfoAlarmStateM1_Type())
infoAlarmStateM1.setMaxAccess(_C)
if mibBuilder.loadTexts:infoAlarmStateM1.setStatus(_A)
class _InfoAlarmStateM2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_G,1),(_W,2),(_X,3),(_Y,4),(_Q,5),(_R,6),(_Z,7),(_a,8),(_b,9),(_c,10),(_d,11),(_e,12),(_f,13),(_g,14),(_h,15),(_i,16)))
_InfoAlarmStateM2_Type.__name__=_E
_InfoAlarmStateM2_Object=MibScalar
infoAlarmStateM2=_InfoAlarmStateM2_Object((1,3,6,1,4,1,266,20,1,22),_InfoAlarmStateM2_Type())
infoAlarmStateM2.setMaxAccess(_C)
if mibBuilder.loadTexts:infoAlarmStateM2.setStatus(_A)
class _InfoLastTftpMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_InfoLastTftpMessage_Type.__name__=_F
_InfoLastTftpMessage_Object=MibScalar
infoLastTftpMessage=_InfoLastTftpMessage_Object((1,3,6,1,4,1,266,20,1,23),_InfoLastTftpMessage_Type())
infoLastTftpMessage.setMaxAccess(_L)
if mibBuilder.loadTexts:infoLastTftpMessage.setStatus(_A)
class _InfoLastSfpEventMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_InfoLastSfpEventMessage_Type.__name__=_F
_InfoLastSfpEventMessage_Object=MibScalar
infoLastSfpEventMessage=_InfoLastSfpEventMessage_Object((1,3,6,1,4,1,266,20,1,24),_InfoLastSfpEventMessage_Type())
infoLastSfpEventMessage.setMaxAccess(_L)
if mibBuilder.loadTexts:infoLastSfpEventMessage.setStatus(_A)
class _InfoLastInternalMgmtWarning_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_InfoLastInternalMgmtWarning_Type.__name__=_F
_InfoLastInternalMgmtWarning_Object=MibScalar
infoLastInternalMgmtWarning=_InfoLastInternalMgmtWarning_Object((1,3,6,1,4,1,266,20,1,25),_InfoLastInternalMgmtWarning_Type())
infoLastInternalMgmtWarning.setMaxAccess(_L)
if mibBuilder.loadTexts:infoLastInternalMgmtWarning.setStatus(_A)
class _InfoFunctionInputStateF1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_N,2),(_O,3)))
_InfoFunctionInputStateF1_Type.__name__=_E
_InfoFunctionInputStateF1_Object=MibScalar
infoFunctionInputStateF1=_InfoFunctionInputStateF1_Object((1,3,6,1,4,1,266,20,1,26),_InfoFunctionInputStateF1_Type())
infoFunctionInputStateF1.setMaxAccess(_C)
if mibBuilder.loadTexts:infoFunctionInputStateF1.setStatus(_A)
_InfoTotalConfigChanges_Type=Counter32
_InfoTotalConfigChanges_Object=MibScalar
infoTotalConfigChanges=_InfoTotalConfigChanges_Object((1,3,6,1,4,1,266,20,1,27),_InfoTotalConfigChanges_Type())
infoTotalConfigChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:infoTotalConfigChanges.setStatus(_A)
class _InfoLastConfigChangeSource_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_InfoLastConfigChangeSource_Type.__name__=_F
_InfoLastConfigChangeSource_Object=MibScalar
infoLastConfigChangeSource=_InfoLastConfigChangeSource_Object((1,3,6,1,4,1,266,20,1,28),_InfoLastConfigChangeSource_Type())
infoLastConfigChangeSource.setMaxAccess(_L)
if mibBuilder.loadTexts:infoLastConfigChangeSource.setStatus(_A)
class _InfoLastPortStateChangeSource_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_InfoLastPortStateChangeSource_Type.__name__=_F
_InfoLastPortStateChangeSource_Object=MibScalar
infoLastPortStateChangeSource=_InfoLastPortStateChangeSource_Object((1,3,6,1,4,1,266,20,1,29),_InfoLastPortStateChangeSource_Type())
infoLastPortStateChangeSource.setMaxAccess(_L)
if mibBuilder.loadTexts:infoLastPortStateChangeSource.setStatus(_A)
class _InfoFunctionInputStateF2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_N,2),(_O,3)))
_InfoFunctionInputStateF2_Type.__name__=_E
_InfoFunctionInputStateF2_Object=MibScalar
infoFunctionInputStateF2=_InfoFunctionInputStateF2_Object((1,3,6,1,4,1,266,20,1,30),_InfoFunctionInputStateF2_Type())
infoFunctionInputStateF2.setMaxAccess(_C)
if mibBuilder.loadTexts:infoFunctionInputStateF2.setStatus(_A)
class _InfoFunctionInputStateF3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_N,2),(_O,3)))
_InfoFunctionInputStateF3_Type.__name__=_E
_InfoFunctionInputStateF3_Object=MibScalar
infoFunctionInputStateF3=_InfoFunctionInputStateF3_Object((1,3,6,1,4,1,266,20,1,31),_InfoFunctionInputStateF3_Type())
infoFunctionInputStateF3.setMaxAccess(_C)
if mibBuilder.loadTexts:infoFunctionInputStateF3.setStatus(_A)
class _InfoFunctionInputStateF4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_N,2),(_O,3)))
_InfoFunctionInputStateF4_Type.__name__=_E
_InfoFunctionInputStateF4_Object=MibScalar
infoFunctionInputStateF4=_InfoFunctionInputStateF4_Object((1,3,6,1,4,1,266,20,1,32),_InfoFunctionInputStateF4_Type())
infoFunctionInputStateF4.setMaxAccess(_C)
if mibBuilder.loadTexts:infoFunctionInputStateF4.setStatus(_A)
class _InfoLastFuncInputAlarmNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_InfoLastFuncInputAlarmNumber_Type.__name__=_E
_InfoLastFuncInputAlarmNumber_Object=MibScalar
infoLastFuncInputAlarmNumber=_InfoLastFuncInputAlarmNumber_Object((1,3,6,1,4,1,266,20,1,33),_InfoLastFuncInputAlarmNumber_Type())
infoLastFuncInputAlarmNumber.setMaxAccess(_L)
if mibBuilder.loadTexts:infoLastFuncInputAlarmNumber.setStatus(_A)
class _InfoLastFuncInputAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_N,2),(_O,3)))
_InfoLastFuncInputAlarmState_Type.__name__=_E
_InfoLastFuncInputAlarmState_Object=MibScalar
infoLastFuncInputAlarmState=_InfoLastFuncInputAlarmState_Object((1,3,6,1,4,1,266,20,1,34),_InfoLastFuncInputAlarmState_Type())
infoLastFuncInputAlarmState.setMaxAccess(_L)
if mibBuilder.loadTexts:infoLastFuncInputAlarmState.setStatus(_A)
class _InfoLastFuncInputAlarmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_InfoLastFuncInputAlarmName_Type.__name__=_F
_InfoLastFuncInputAlarmName_Object=MibScalar
infoLastFuncInputAlarmName=_InfoLastFuncInputAlarmName_Object((1,3,6,1,4,1,266,20,1,35),_InfoLastFuncInputAlarmName_Type())
infoLastFuncInputAlarmName.setMaxAccess(_L)
if mibBuilder.loadTexts:infoLastFuncInputAlarmName.setStatus(_A)
_BmSwitchAdmin_ObjectIdentity=ObjectIdentity
bmSwitchAdmin=_BmSwitchAdmin_ObjectIdentity((1,3,6,1,4,1,266,20,2))
class _AdminReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('resetIdle',1),('resetCounters',2),('rebootSwitch',3),('rebootToFactoryDefaults',4),('renewIpAndVlanParameter',5)))
_AdminReset_Type.__name__=_E
_AdminReset_Object=MibScalar
adminReset=_AdminReset_Object((1,3,6,1,4,1,266,20,2,1),_AdminReset_Type())
adminReset.setMaxAccess(_D)
if mibBuilder.loadTexts:adminReset.setStatus(_A)
class _AdminAgentDhcp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_K,2)))
_AdminAgentDhcp_Type.__name__=_E
_AdminAgentDhcp_Object=MibScalar
adminAgentDhcp=_AdminAgentDhcp_Object((1,3,6,1,4,1,266,20,2,2),_AdminAgentDhcp_Type())
adminAgentDhcp.setMaxAccess(_D)
if mibBuilder.loadTexts:adminAgentDhcp.setStatus(_A)
_AdminAgentIpAddress_Type=IpAddress
_AdminAgentIpAddress_Object=MibScalar
adminAgentIpAddress=_AdminAgentIpAddress_Object((1,3,6,1,4,1,266,20,2,3),_AdminAgentIpAddress_Type())
adminAgentIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:adminAgentIpAddress.setStatus(_A)
_AdminAgentPhysAddress_Type=MacAddress
_AdminAgentPhysAddress_Object=MibScalar
adminAgentPhysAddress=_AdminAgentPhysAddress_Object((1,3,6,1,4,1,266,20,2,4),_AdminAgentPhysAddress_Type())
adminAgentPhysAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adminAgentPhysAddress.setStatus(_A)
_AdminAgentDefRouterIpAddress_Type=IpAddress
_AdminAgentDefRouterIpAddress_Object=MibScalar
adminAgentDefRouterIpAddress=_AdminAgentDefRouterIpAddress_Object((1,3,6,1,4,1,266,20,2,5),_AdminAgentDefRouterIpAddress_Type())
adminAgentDefRouterIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:adminAgentDefRouterIpAddress.setStatus(_A)
_AdminAgentNetmask_Type=IpAddress
_AdminAgentNetmask_Object=MibScalar
adminAgentNetmask=_AdminAgentNetmask_Object((1,3,6,1,4,1,266,20,2,6),_AdminAgentNetmask_Type())
adminAgentNetmask.setMaxAccess(_D)
if mibBuilder.loadTexts:adminAgentNetmask.setStatus(_A)
_AdminAgentDhcpServerIpAddress_Type=IpAddress
_AdminAgentDhcpServerIpAddress_Object=MibScalar
adminAgentDhcpServerIpAddress=_AdminAgentDhcpServerIpAddress_Object((1,3,6,1,4,1,266,20,2,7),_AdminAgentDhcpServerIpAddress_Type())
adminAgentDhcpServerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adminAgentDhcpServerIpAddress.setStatus(_A)
class _AdminAgentVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_AdminAgentVlanId_Type.__name__=_E
_AdminAgentVlanId_Object=MibScalar
adminAgentVlanId=_AdminAgentVlanId_Object((1,3,6,1,4,1,266,20,2,8),_AdminAgentVlanId_Type())
adminAgentVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:adminAgentVlanId.setStatus(_A)
class _AdminAgentPrioValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdminAgentPrioValue_Type.__name__=_E
_AdminAgentPrioValue_Object=MibScalar
adminAgentPrioValue=_AdminAgentPrioValue_Object((1,3,6,1,4,1,266,20,2,9),_AdminAgentPrioValue_Type())
adminAgentPrioValue.setMaxAccess(_D)
if mibBuilder.loadTexts:adminAgentPrioValue.setStatus(_A)
class _AdminAddrAgingTimeMinutes_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,68))
_AdminAddrAgingTimeMinutes_Type.__name__=_E
_AdminAddrAgingTimeMinutes_Object=MibScalar
adminAddrAgingTimeMinutes=_AdminAddrAgingTimeMinutes_Object((1,3,6,1,4,1,266,20,2,10),_AdminAddrAgingTimeMinutes_Type())
adminAddrAgingTimeMinutes.setMaxAccess(_D)
if mibBuilder.loadTexts:adminAddrAgingTimeMinutes.setStatus(_A)
class _AdminSwitchPortMirror_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_K,2)))
_AdminSwitchPortMirror_Type.__name__=_E
_AdminSwitchPortMirror_Object=MibScalar
adminSwitchPortMirror=_AdminSwitchPortMirror_Object((1,3,6,1,4,1,266,20,2,11),_AdminSwitchPortMirror_Type())
adminSwitchPortMirror.setMaxAccess(_D)
if mibBuilder.loadTexts:adminSwitchPortMirror.setStatus(_A)
class _AdminMgmtAccessList_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('enableForNexManAccess',2),('enableForAllAccess',3),('enableForSnmpAccess',4)))
_AdminMgmtAccessList_Type.__name__=_E
_AdminMgmtAccessList_Object=MibScalar
adminMgmtAccessList=_AdminMgmtAccessList_Object((1,3,6,1,4,1,266,20,2,12),_AdminMgmtAccessList_Type())
adminMgmtAccessList.setMaxAccess(_D)
if mibBuilder.loadTexts:adminMgmtAccessList.setStatus(_A)
_AdminSwitchPoEPowerLimit_Type=Integer32
_AdminSwitchPoEPowerLimit_Object=MibScalar
adminSwitchPoEPowerLimit=_AdminSwitchPoEPowerLimit_Object((1,3,6,1,4,1,266,20,2,13),_AdminSwitchPoEPowerLimit_Type())
adminSwitchPoEPowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:adminSwitchPoEPowerLimit.setStatus(_A)
class _AdminSwitchVlanTableMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('staticMode',1),('dynamicMode',2),('staticModeVlans64',3),('staticModePortBased',4)))
_AdminSwitchVlanTableMode_Type.__name__=_E
_AdminSwitchVlanTableMode_Object=MibScalar
adminSwitchVlanTableMode=_AdminSwitchVlanTableMode_Object((1,3,6,1,4,1,266,20,2,14),_AdminSwitchVlanTableMode_Type())
adminSwitchVlanTableMode.setMaxAccess(_D)
if mibBuilder.loadTexts:adminSwitchVlanTableMode.setStatus(_A)
class _AdminUnsecureVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_AdminUnsecureVlanId_Type.__name__=_E
_AdminUnsecureVlanId_Object=MibScalar
adminUnsecureVlanId=_AdminUnsecureVlanId_Object((1,3,6,1,4,1,266,20,2,15),_AdminUnsecureVlanId_Type())
adminUnsecureVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:adminUnsecureVlanId.setStatus(_A)
class _AdminDot1xAuthFailureVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AdminDot1xAuthFailureVlanId_Type.__name__=_E
_AdminDot1xAuthFailureVlanId_Object=MibScalar
adminDot1xAuthFailureVlanId=_AdminDot1xAuthFailureVlanId_Object((1,3,6,1,4,1,266,20,2,16),_AdminDot1xAuthFailureVlanId_Type())
adminDot1xAuthFailureVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:adminDot1xAuthFailureVlanId.setStatus(_A)
class _AdminTftpAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tftpAccessDisable',1),('tftpAccessReadOnly',2),('tftpAccessReadWrite',3)))
_AdminTftpAccess_Type.__name__=_E
_AdminTftpAccess_Object=MibScalar
adminTftpAccess=_AdminTftpAccess_Object((1,3,6,1,4,1,266,20,2,17),_AdminTftpAccess_Type())
adminTftpAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:adminTftpAccess.setStatus(_A)
class _AdminSnmpMacTableMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('listAllPorts',1),('listUserPortsOnly',2)))
_AdminSnmpMacTableMode_Type.__name__=_E
_AdminSnmpMacTableMode_Object=MibScalar
adminSnmpMacTableMode=_AdminSnmpMacTableMode_Object((1,3,6,1,4,1,266,20,2,18),_AdminSnmpMacTableMode_Type())
adminSnmpMacTableMode.setMaxAccess(_D)
if mibBuilder.loadTexts:adminSnmpMacTableMode.setStatus(_A)
class _AdminAlarmM1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_G,1),(_j,2),(_Q,3),(_R,4),(_k,5),(_l,6),(_m,7),(_n,8),(_o,9),(_p,10),(_q,11),(_r,12),(_s,13),(_t,14),(_u,15)))
_AdminAlarmM1_Type.__name__=_E
_AdminAlarmM1_Object=MibScalar
adminAlarmM1=_AdminAlarmM1_Object((1,3,6,1,4,1,266,20,2,19),_AdminAlarmM1_Type())
adminAlarmM1.setMaxAccess(_D)
if mibBuilder.loadTexts:adminAlarmM1.setStatus(_A)
class _AdminAlarmM2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_G,1),(_j,2),(_Q,3),(_R,4),(_k,5),(_l,6),(_m,7),(_n,8),(_o,9),(_p,10),(_q,11),(_r,12),(_s,13),(_t,14),(_u,15)))
_AdminAlarmM2_Type.__name__=_E
_AdminAlarmM2_Object=MibScalar
adminAlarmM2=_AdminAlarmM2_Object((1,3,6,1,4,1,266,20,2,20),_AdminAlarmM2_Type())
adminAlarmM2.setMaxAccess(_D)
if mibBuilder.loadTexts:adminAlarmM2.setStatus(_A)
class _AdminMemoryCardMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('mcEnabled',2),('mcDisabled',3),('mcPermanentDisabled',4),('mcEnabledWithAes256',5),('mcEnabledWithAes256AndFw',6)))
_AdminMemoryCardMode_Type.__name__=_E
_AdminMemoryCardMode_Object=MibScalar
adminMemoryCardMode=_AdminMemoryCardMode_Object((1,3,6,1,4,1,266,20,2,21),_AdminMemoryCardMode_Type())
adminMemoryCardMode.setMaxAccess(_D)
if mibBuilder.loadTexts:adminMemoryCardMode.setStatus(_A)
class _AdminAlarmNameM1_Type(DisplayString):defaultValue=OctetString(_M);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AdminAlarmNameM1_Type.__name__=_F
_AdminAlarmNameM1_Object=MibScalar
adminAlarmNameM1=_AdminAlarmNameM1_Object((1,3,6,1,4,1,266,20,2,22),_AdminAlarmNameM1_Type())
adminAlarmNameM1.setMaxAccess(_D)
if mibBuilder.loadTexts:adminAlarmNameM1.setStatus(_A)
class _AdminAlarmNameM2_Type(DisplayString):defaultValue=OctetString(_M);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AdminAlarmNameM2_Type.__name__=_F
_AdminAlarmNameM2_Object=MibScalar
adminAlarmNameM2=_AdminAlarmNameM2_Object((1,3,6,1,4,1,266,20,2,23),_AdminAlarmNameM2_Type())
adminAlarmNameM2.setMaxAccess(_D)
if mibBuilder.loadTexts:adminAlarmNameM2.setStatus(_A)
class _AdminFunctionInputNameF1_Type(DisplayString):defaultValue=OctetString(_M);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AdminFunctionInputNameF1_Type.__name__=_F
_AdminFunctionInputNameF1_Object=MibScalar
adminFunctionInputNameF1=_AdminFunctionInputNameF1_Object((1,3,6,1,4,1,266,20,2,24),_AdminFunctionInputNameF1_Type())
adminFunctionInputNameF1.setMaxAccess(_D)
if mibBuilder.loadTexts:adminFunctionInputNameF1.setStatus(_A)
class _AdminLedGlobalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ledGlobalModeNotSupported',1),('ledGlobalModeStandard',2),('ledGlobalModeAllOff',3),('ledGlobalModeAllOn',4),('ledGlobalModeMgmtOnly',5),('ledGlobalModeGreenBlink',6),('ledGlobalModeRedBlueBlink',7)))
_AdminLedGlobalMode_Type.__name__=_E
_AdminLedGlobalMode_Object=MibScalar
adminLedGlobalMode=_AdminLedGlobalMode_Object((1,3,6,1,4,1,266,20,2,25),_AdminLedGlobalMode_Type())
adminLedGlobalMode.setMaxAccess(_D)
if mibBuilder.loadTexts:adminLedGlobalMode.setStatus(_A)
class _AdminFunctionInputNameF2_Type(DisplayString):defaultValue=OctetString(_M);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AdminFunctionInputNameF2_Type.__name__=_F
_AdminFunctionInputNameF2_Object=MibScalar
adminFunctionInputNameF2=_AdminFunctionInputNameF2_Object((1,3,6,1,4,1,266,20,2,26),_AdminFunctionInputNameF2_Type())
adminFunctionInputNameF2.setMaxAccess(_D)
if mibBuilder.loadTexts:adminFunctionInputNameF2.setStatus(_A)
class _AdminFunctionInputNameF3_Type(DisplayString):defaultValue=OctetString(_M);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AdminFunctionInputNameF3_Type.__name__=_F
_AdminFunctionInputNameF3_Object=MibScalar
adminFunctionInputNameF3=_AdminFunctionInputNameF3_Object((1,3,6,1,4,1,266,20,2,27),_AdminFunctionInputNameF3_Type())
adminFunctionInputNameF3.setMaxAccess(_D)
if mibBuilder.loadTexts:adminFunctionInputNameF3.setStatus(_A)
class _AdminFunctionInputNameF4_Type(DisplayString):defaultValue=OctetString(_M);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AdminFunctionInputNameF4_Type.__name__=_F
_AdminFunctionInputNameF4_Object=MibScalar
adminFunctionInputNameF4=_AdminFunctionInputNameF4_Object((1,3,6,1,4,1,266,20,2,28),_AdminFunctionInputNameF4_Type())
adminFunctionInputNameF4.setMaxAccess(_D)
if mibBuilder.loadTexts:adminFunctionInputNameF4.setStatus(_A)
_BmSwitchPort_ObjectIdentity=ObjectIdentity
bmSwitchPort=_BmSwitchPort_ObjectIdentity((1,3,6,1,4,1,266,20,3))
_BmSwitchPortTable_Object=MibTable
bmSwitchPortTable=_BmSwitchPortTable_Object((1,3,6,1,4,1,266,20,3,1))
if mibBuilder.loadTexts:bmSwitchPortTable.setStatus(_A)
_BmSwitchPortEntry_Object=MibTableRow
bmSwitchPortEntry=_BmSwitchPortEntry_Object((1,3,6,1,4,1,266,20,3,1,1))
bmSwitchPortEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:bmSwitchPortEntry.setStatus(_A)
class _PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PortIndex_Type.__name__=_E
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,266,20,3,1,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PortDescr_Type.__name__=_F
_PortDescr_Object=MibTableColumn
portDescr=_PortDescr_Object((1,3,6,1,4,1,266,20,3,1,1,2),_PortDescr_Type())
portDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:portDescr.setStatus(_A)
class _PortName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_PortName_Type.__name__=_F
_PortName_Object=MibTableColumn
portName=_PortName_Object((1,3,6,1,4,1,266,20,3,1,1,3),_PortName_Type())
portName.setMaxAccess(_D)
if mibBuilder.loadTexts:portName.setStatus(_A)
class _PortAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_v,1),(_P,2),('adminDisable',3),('securityDisable',4),('loopDisable',5),('bpduDisable',6),('udldDisable',7),('linkFlapDisable',8),('errorCountDisable',9),('sfpErrorDisable',10),('redundanyLoopDisable',11),('dhcpSnoopingDisable',12)))
_PortAdminState_Type.__name__=_E
_PortAdminState_Object=MibTableColumn
portAdminState=_PortAdminState_Object((1,3,6,1,4,1,266,20,3,1,1,4),_PortAdminState_Type())
portAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:portAdminState.setStatus(_A)
class _PortSpeedDuplexSetup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,8,9,10,11,12)));namedValues=NamedValues(*(('autoneg',1),('fix10Hdx',2),('fix10Fdx',3),('fix100Hdx',4),('fix100Fdx',5),('fix1000Hdx',7),('fix1000Fdx',8),('eco',9),('ecoOverTemp',10),('ecoPowerSave',11),('fix1000fdxNoAutoneg',12)))
_PortSpeedDuplexSetup_Type.__name__=_E
_PortSpeedDuplexSetup_Object=MibTableColumn
portSpeedDuplexSetup=_PortSpeedDuplexSetup_Object((1,3,6,1,4,1,266,20,3,1,1,5),_PortSpeedDuplexSetup_Type())
portSpeedDuplexSetup.setMaxAccess(_D)
if mibBuilder.loadTexts:portSpeedDuplexSetup.setStatus(_A)
class _PortLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('down',1),('up10Hdx',2),('up10Fdx',3),('up100Hdx',4),('up100Fdx',5),('up1000Hdx',6),('up1000Fdx',7)))
_PortLinkState_Type.__name__=_E
_PortLinkState_Object=MibTableColumn
portLinkState=_PortLinkState_Object((1,3,6,1,4,1,266,20,3,1,1,6),_PortLinkState_Type())
portLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:portLinkState.setStatus(_A)
_PortErrorCounter_Type=Counter32
_PortErrorCounter_Object=MibTableColumn
portErrorCounter=_PortErrorCounter_Object((1,3,6,1,4,1,266,20,3,1,1,7),_PortErrorCounter_Type())
portErrorCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:portErrorCounter.setStatus(_A)
class _PortRemoteFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_P,2),(_K,3)))
_PortRemoteFault_Type.__name__=_E
_PortRemoteFault_Object=MibTableColumn
portRemoteFault=_PortRemoteFault_Object((1,3,6,1,4,1,266,20,3,1,1,8),_PortRemoteFault_Type())
portRemoteFault.setMaxAccess(_D)
if mibBuilder.loadTexts:portRemoteFault.setStatus(_A)
class _PortDefaultVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_PortDefaultVlanId_Type.__name__=_E
_PortDefaultVlanId_Object=MibTableColumn
portDefaultVlanId=_PortDefaultVlanId_Object((1,3,6,1,4,1,266,20,3,1,1,9),_PortDefaultVlanId_Type())
portDefaultVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:portDefaultVlanId.setStatus(_A)
class _PortTrunkingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dot1qTagging',1),(_K,2),('enableWithoutTagging',3)))
_PortTrunkingMode_Type.__name__=_E
_PortTrunkingMode_Object=MibTableColumn
portTrunkingMode=_PortTrunkingMode_Object((1,3,6,1,4,1,266,20,3,1,1,10),_PortTrunkingMode_Type())
portTrunkingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:portTrunkingMode.setStatus(_A)
class _PortDot1qDefaultPrioValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PortDot1qDefaultPrioValue_Type.__name__=_E
_PortDot1qDefaultPrioValue_Object=MibTableColumn
portDot1qDefaultPrioValue=_PortDot1qDefaultPrioValue_Object((1,3,6,1,4,1,266,20,3,1,1,11),_PortDot1qDefaultPrioValue_Type())
portDot1qDefaultPrioValue.setMaxAccess(_D)
if mibBuilder.loadTexts:portDot1qDefaultPrioValue.setStatus(_A)
class _PortDefaultPrioQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_PortDefaultPrioQueue_Type.__name__=_E
_PortDefaultPrioQueue_Object=MibTableColumn
portDefaultPrioQueue=_PortDefaultPrioQueue_Object((1,3,6,1,4,1,266,20,3,1,1,12),_PortDefaultPrioQueue_Type())
portDefaultPrioQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:portDefaultPrioQueue.setStatus(_A)
class _PortLEDGreen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('showLinkState',2),('blink',3),(_w,4),(_x,5),('showLinkSpeedDuplex',6)))
_PortLEDGreen_Type.__name__=_E
_PortLEDGreen_Object=MibTableColumn
portLEDGreen=_PortLEDGreen_Object((1,3,6,1,4,1,266,20,3,1,1,13),_PortLEDGreen_Type())
portLEDGreen.setMaxAccess(_D)
if mibBuilder.loadTexts:portLEDGreen.setStatus(_A)
class _PortLEDYellow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),('showDuplexState',2),('blink',3),(_w,4),(_x,5),('showPoeEnabled',6),('showSpeed',7)))
_PortLEDYellow_Type.__name__=_E
_PortLEDYellow_Object=MibTableColumn
portLEDYellow=_PortLEDYellow_Object((1,3,6,1,4,1,266,20,3,1,1,14),_PortLEDYellow_Type())
portLEDYellow.setMaxAccess(_D)
if mibBuilder.loadTexts:portLEDYellow.setStatus(_A)
class _PortBandwidthLimitRxd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_G,1),(_K,2),(_y,3),(_z,4),(_A0,5),('limit1M',6),('limit2M',7),('limit4M',8),('limit8M',9),('limit16M',10),('limit32M',11),('limit64M',12),(_A1,13),(_A2,14)))
_PortBandwidthLimitRxd_Type.__name__=_E
_PortBandwidthLimitRxd_Object=MibTableColumn
portBandwidthLimitRxd=_PortBandwidthLimitRxd_Object((1,3,6,1,4,1,266,20,3,1,1,15),_PortBandwidthLimitRxd_Type())
portBandwidthLimitRxd.setMaxAccess(_D)
if mibBuilder.loadTexts:portBandwidthLimitRxd.setStatus(_A)
class _PortBandwidthLimitTxd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_G,1),(_K,2),(_y,3),(_z,4),(_A0,5),('limit1M',6),('limit2M',7),('limit4M',8),('limit8M',9),('limit16M',10),('limit32M',11),('limit64M',12),(_A1,13),(_A2,14)))
_PortBandwidthLimitTxd_Type.__name__=_E
_PortBandwidthLimitTxd_Object=MibTableColumn
portBandwidthLimitTxd=_PortBandwidthLimitTxd_Object((1,3,6,1,4,1,266,20,3,1,1,16),_PortBandwidthLimitTxd_Type())
portBandwidthLimitTxd.setMaxAccess(_D)
if mibBuilder.loadTexts:portBandwidthLimitTxd.setStatus(_A)
class _PortSecurityAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_G,1),(_K,2),('manualSettingMacAddr',3),('autoAllowOneMacAddr',4),('autoAllowTwoMacAddr',5),('autoAllowThreeMacAddr',6),('radiusAllowOneMacAddr',7),('radiusAllowTwoMacAddr',8),('radiusAllowThreeMacAddr',9),('renew',10),('ieee802AllowOneMacAddr',11),('vendorSettingMacAddr',12),('ieee802AllowMultiMacAddr',13),('ieee802OrRadiusOneMac',14),('ieee802AndRadiusTwoMac',15),('learnOneMacAddr',16),('learnTwoMacAddr',17)))
_PortSecurityAdminState_Type.__name__=_E
_PortSecurityAdminState_Object=MibTableColumn
portSecurityAdminState=_PortSecurityAdminState_Object((1,3,6,1,4,1,266,20,3,1,1,17),_PortSecurityAdminState_Type())
portSecurityAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:portSecurityAdminState.setStatus(_A)
_PortSecurityMacAddr1_Type=MacAddress
_PortSecurityMacAddr1_Object=MibTableColumn
portSecurityMacAddr1=_PortSecurityMacAddr1_Object((1,3,6,1,4,1,266,20,3,1,1,18),_PortSecurityMacAddr1_Type())
portSecurityMacAddr1.setMaxAccess(_D)
if mibBuilder.loadTexts:portSecurityMacAddr1.setStatus(_A)
_PortSecurityMacAddr2_Type=MacAddress
_PortSecurityMacAddr2_Object=MibTableColumn
portSecurityMacAddr2=_PortSecurityMacAddr2_Object((1,3,6,1,4,1,266,20,3,1,1,19),_PortSecurityMacAddr2_Type())
portSecurityMacAddr2.setMaxAccess(_D)
if mibBuilder.loadTexts:portSecurityMacAddr2.setStatus(_A)
_PortSecurityMacAddr3_Type=MacAddress
_PortSecurityMacAddr3_Object=MibTableColumn
portSecurityMacAddr3=_PortSecurityMacAddr3_Object((1,3,6,1,4,1,266,20,3,1,1,20),_PortSecurityMacAddr3_Type())
portSecurityMacAddr3.setMaxAccess(_D)
if mibBuilder.loadTexts:portSecurityMacAddr3.setStatus(_A)
class _PortPoeAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,1),('off',2),('forcedOn',3),('autoOn',4),('overloadFail',5),('reset',6),('afHighPower',7),('atHighPower',8)))
_PortPoeAdminState_Type.__name__=_E
_PortPoeAdminState_Object=MibTableColumn
portPoeAdminState=_PortPoeAdminState_Object((1,3,6,1,4,1,266,20,3,1,1,21),_PortPoeAdminState_Type())
portPoeAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:portPoeAdminState.setStatus(_A)
_PortPoeVoltage_Type=Integer32
_PortPoeVoltage_Object=MibTableColumn
portPoeVoltage=_PortPoeVoltage_Object((1,3,6,1,4,1,266,20,3,1,1,22),_PortPoeVoltage_Type())
portPoeVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:portPoeVoltage.setStatus(_A)
_PortPoeCurrent_Type=Integer32
_PortPoeCurrent_Object=MibTableColumn
portPoeCurrent=_PortPoeCurrent_Object((1,3,6,1,4,1,266,20,3,1,1,23),_PortPoeCurrent_Type())
portPoeCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:portPoeCurrent.setStatus(_A)
_PortPoePower_Type=Integer32
_PortPoePower_Object=MibTableColumn
portPoePower=_PortPoePower_Object((1,3,6,1,4,1,266,20,3,1,1,24),_PortPoePower_Type())
portPoePower.setMaxAccess(_C)
if mibBuilder.loadTexts:portPoePower.setStatus(_A)
class _PortSecurityForwardingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*((_G,1),('portAdminDisabled',2),('waitingForLink',3),('unsecureVLAN',4),('portAuthenticated',5),('portSecurityDisabled',6),('portLoopDisabled',7),('authFailureVLAN',8),('securityWarning',9),('authenticatingClients',10),('waitingForMacAddress',11),('allRadiusServersDown',12),('portBpduDisabled',13),('portUdldDisabled',14),('portLinkFlapDisabled',15),('portErrorCountDisabled',16),('portSfpErrorDisabled',17),('portRedundanyLoopDisable',18),('portDhcpSnoopingDisable',19)))
_PortSecurityForwardingState_Type.__name__=_E
_PortSecurityForwardingState_Object=MibTableColumn
portSecurityForwardingState=_PortSecurityForwardingState_Object((1,3,6,1,4,1,266,20,3,1,1,25),_PortSecurityForwardingState_Type())
portSecurityForwardingState.setMaxAccess(_C)
if mibBuilder.loadTexts:portSecurityForwardingState.setStatus(_A)
_PortPoePowerLimit_Type=Integer32
_PortPoePowerLimit_Object=MibTableColumn
portPoePowerLimit=_PortPoePowerLimit_Object((1,3,6,1,4,1,266,20,3,1,1,26),_PortPoePowerLimit_Type())
portPoePowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:portPoePowerLimit.setStatus(_A)
class _PortLimiterPacketType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('limitAllPackets',2),('limitLoopBcastPackets',3),('limitAllPacketsBurstsAllowed',4)))
_PortLimiterPacketType_Type.__name__=_E
_PortLimiterPacketType_Object=MibTableColumn
portLimiterPacketType=_PortLimiterPacketType_Object((1,3,6,1,4,1,266,20,3,1,1,27),_PortLimiterPacketType_Type())
portLimiterPacketType.setMaxAccess(_D)
if mibBuilder.loadTexts:portLimiterPacketType.setStatus(_A)
class _PortAcApSetup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_v,2),(_P,3),(_K,4)))
_PortAcApSetup_Type.__name__=_E
_PortAcApSetup_Object=MibTableColumn
portAcApSetup=_PortAcApSetup_Object((1,3,6,1,4,1,266,20,3,1,1,28),_PortAcApSetup_Type())
portAcApSetup.setMaxAccess(_D)
if mibBuilder.loadTexts:portAcApSetup.setStatus(_A)
class _PortLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('user',1),('userWithLoopProtection',2),('upDownlink',3)))
_PortLinkType_Type.__name__=_E
_PortLinkType_Object=MibTableColumn
portLinkType=_PortLinkType_Object((1,3,6,1,4,1,266,20,3,1,1,29),_PortLinkType_Type())
portLinkType.setMaxAccess(_D)
if mibBuilder.loadTexts:portLinkType.setStatus(_A)
class _PortVoiceVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_PortVoiceVlanId_Type.__name__=_E
_PortVoiceVlanId_Object=MibTableColumn
portVoiceVlanId=_PortVoiceVlanId_Object((1,3,6,1,4,1,266,20,3,1,1,30),_PortVoiceVlanId_Type())
portVoiceVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceVlanId.setStatus(_A)
class _PortPrioDot1p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('prioDot1pDisabled',1),('prioDot1pEnabled',2)))
_PortPrioDot1p_Type.__name__=_E
_PortPrioDot1p_Object=MibTableColumn
portPrioDot1p=_PortPrioDot1p_Object((1,3,6,1,4,1,266,20,3,1,1,31),_PortPrioDot1p_Type())
portPrioDot1p.setMaxAccess(_D)
if mibBuilder.loadTexts:portPrioDot1p.setStatus(_A)
class _PortPrioIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('prioIpDisabled',1),('prioIpEnabled',2)))
_PortPrioIp_Type.__name__=_E
_PortPrioIp_Object=MibTableColumn
portPrioIp=_PortPrioIp_Object((1,3,6,1,4,1,266,20,3,1,1,32),_PortPrioIp_Type())
portPrioIp.setMaxAccess(_D)
if mibBuilder.loadTexts:portPrioIp.setStatus(_A)
class _PortActiveDefaultVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_PortActiveDefaultVlanId_Type.__name__=_E
_PortActiveDefaultVlanId_Object=MibTableColumn
portActiveDefaultVlanId=_PortActiveDefaultVlanId_Object((1,3,6,1,4,1,266,20,3,1,1,33),_PortActiveDefaultVlanId_Type())
portActiveDefaultVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:portActiveDefaultVlanId.setStatus(_A)
class _PortActiveVoiceVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_PortActiveVoiceVlanId_Type.__name__=_E
_PortActiveVoiceVlanId_Object=MibTableColumn
portActiveVoiceVlanId=_PortActiveVoiceVlanId_Object((1,3,6,1,4,1,266,20,3,1,1,34),_PortActiveVoiceVlanId_Type())
portActiveVoiceVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:portActiveVoiceVlanId.setStatus(_A)
_BmSwitchVlan_ObjectIdentity=ObjectIdentity
bmSwitchVlan=_BmSwitchVlan_ObjectIdentity((1,3,6,1,4,1,266,20,4))
_BmSwitchVlanTable_Object=MibTable
bmSwitchVlanTable=_BmSwitchVlanTable_Object((1,3,6,1,4,1,266,20,4,1))
if mibBuilder.loadTexts:bmSwitchVlanTable.setStatus(_A)
_BmSwitchVlanEntry_Object=MibTableRow
bmSwitchVlanEntry=_BmSwitchVlanEntry_Object((1,3,6,1,4,1,266,20,4,1,1))
bmSwitchVlanEntry.setIndexNames((0,_B,_A3))
if mibBuilder.loadTexts:bmSwitchVlanEntry.setStatus(_A)
class _VlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_VlanIndex_Type.__name__=_E
_VlanIndex_Object=MibTableColumn
vlanIndex=_VlanIndex_Object((1,3,6,1,4,1,266,20,4,1,1,1),_VlanIndex_Type())
vlanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanIndex.setStatus(_A)
class _VlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_VlanId_Type.__name__=_E
_VlanId_Object=MibTableColumn
vlanId=_VlanId_Object((1,3,6,1,4,1,266,20,4,1,1,2),_VlanId_Type())
vlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanId.setStatus(_A)
class _VlanDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_VlanDescr_Type.__name__=_F
_VlanDescr_Object=MibTableColumn
vlanDescr=_VlanDescr_Object((1,3,6,1,4,1,266,20,4,1,1,3),_VlanDescr_Type())
vlanDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanDescr.setStatus(_A)
_BmSwitchSfp_ObjectIdentity=ObjectIdentity
bmSwitchSfp=_BmSwitchSfp_ObjectIdentity((1,3,6,1,4,1,266,20,5))
_BmSwitchSfpTable_Object=MibTable
bmSwitchSfpTable=_BmSwitchSfpTable_Object((1,3,6,1,4,1,266,20,5,1))
if mibBuilder.loadTexts:bmSwitchSfpTable.setStatus(_A)
_BmSwitchSfpEntry_Object=MibTableRow
bmSwitchSfpEntry=_BmSwitchSfpEntry_Object((1,3,6,1,4,1,266,20,5,1,1))
bmSwitchSfpEntry.setIndexNames((0,_B,_A4))
if mibBuilder.loadTexts:bmSwitchSfpEntry.setStatus(_A)
class _SfpPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_SfpPortIndex_Type.__name__=_E
_SfpPortIndex_Object=MibTableColumn
sfpPortIndex=_SfpPortIndex_Object((1,3,6,1,4,1,266,20,5,1,1,1),_SfpPortIndex_Type())
sfpPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpPortIndex.setStatus(_A)
class _SfpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('noSfpInserted',2),('validSfpNoDiagnostic',3),('validSfpWithDiagnostic',4)))
_SfpState_Type.__name__=_E
_SfpState_Object=MibTableColumn
sfpState=_SfpState_Object((1,3,6,1,4,1,266,20,5,1,1,2),_SfpState_Type())
sfpState.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpState.setStatus(_A)
class _SfpInfoVendorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_SfpInfoVendorName_Type.__name__=_F
_SfpInfoVendorName_Object=MibTableColumn
sfpInfoVendorName=_SfpInfoVendorName_Object((1,3,6,1,4,1,266,20,5,1,1,3),_SfpInfoVendorName_Type())
sfpInfoVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpInfoVendorName.setStatus(_A)
class _SfpInfoPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_SfpInfoPartNumber_Type.__name__=_F
_SfpInfoPartNumber_Object=MibTableColumn
sfpInfoPartNumber=_SfpInfoPartNumber_Object((1,3,6,1,4,1,266,20,5,1,1,4),_SfpInfoPartNumber_Type())
sfpInfoPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpInfoPartNumber.setStatus(_A)
class _SfpInfoRevisionNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_SfpInfoRevisionNumber_Type.__name__=_F
_SfpInfoRevisionNumber_Object=MibTableColumn
sfpInfoRevisionNumber=_SfpInfoRevisionNumber_Object((1,3,6,1,4,1,266,20,5,1,1,5),_SfpInfoRevisionNumber_Type())
sfpInfoRevisionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpInfoRevisionNumber.setStatus(_A)
class _SfpInfoSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_SfpInfoSerialNumber_Type.__name__=_F
_SfpInfoSerialNumber_Object=MibTableColumn
sfpInfoSerialNumber=_SfpInfoSerialNumber_Object((1,3,6,1,4,1,266,20,5,1,1,6),_SfpInfoSerialNumber_Type())
sfpInfoSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpInfoSerialNumber.setStatus(_A)
class _SfpInfoDateCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_SfpInfoDateCode_Type.__name__=_F
_SfpInfoDateCode_Object=MibTableColumn
sfpInfoDateCode=_SfpInfoDateCode_Object((1,3,6,1,4,1,266,20,5,1,1,7),_SfpInfoDateCode_Type())
sfpInfoDateCode.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpInfoDateCode.setStatus(_A)
class _SfpInfoBitRate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_SfpInfoBitRate_Type.__name__=_F
_SfpInfoBitRate_Object=MibTableColumn
sfpInfoBitRate=_SfpInfoBitRate_Object((1,3,6,1,4,1,266,20,5,1,1,8),_SfpInfoBitRate_Type())
sfpInfoBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpInfoBitRate.setStatus(_A)
class _SfpInfoWavelength_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_SfpInfoWavelength_Type.__name__=_F
_SfpInfoWavelength_Object=MibTableColumn
sfpInfoWavelength=_SfpInfoWavelength_Object((1,3,6,1,4,1,266,20,5,1,1,9),_SfpInfoWavelength_Type())
sfpInfoWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpInfoWavelength.setStatus(_A)
class _SfpInfoLength9um_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_SfpInfoLength9um_Type.__name__=_F
_SfpInfoLength9um_Object=MibTableColumn
sfpInfoLength9um=_SfpInfoLength9um_Object((1,3,6,1,4,1,266,20,5,1,1,10),_SfpInfoLength9um_Type())
sfpInfoLength9um.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpInfoLength9um.setStatus(_A)
class _SfpInfoLength50um_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_SfpInfoLength50um_Type.__name__=_F
_SfpInfoLength50um_Object=MibTableColumn
sfpInfoLength50um=_SfpInfoLength50um_Object((1,3,6,1,4,1,266,20,5,1,1,11),_SfpInfoLength50um_Type())
sfpInfoLength50um.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpInfoLength50um.setStatus(_A)
class _SfpInfoLength62um_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_SfpInfoLength62um_Type.__name__=_F
_SfpInfoLength62um_Object=MibTableColumn
sfpInfoLength62um=_SfpInfoLength62um_Object((1,3,6,1,4,1,266,20,5,1,1,12),_SfpInfoLength62um_Type())
sfpInfoLength62um.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpInfoLength62um.setStatus(_A)
class _SfpInfoConnectorDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_SfpInfoConnectorDescr_Type.__name__=_F
_SfpInfoConnectorDescr_Object=MibTableColumn
sfpInfoConnectorDescr=_SfpInfoConnectorDescr_Object((1,3,6,1,4,1,266,20,5,1,1,13),_SfpInfoConnectorDescr_Type())
sfpInfoConnectorDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpInfoConnectorDescr.setStatus(_A)
_SfpDiagTemperature_Type=Integer32
_SfpDiagTemperature_Object=MibTableColumn
sfpDiagTemperature=_SfpDiagTemperature_Object((1,3,6,1,4,1,266,20,5,1,1,14),_SfpDiagTemperature_Type())
sfpDiagTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagTemperature.setStatus(_A)
_SfpDiagSupplyVoltage_Type=Integer32
_SfpDiagSupplyVoltage_Object=MibTableColumn
sfpDiagSupplyVoltage=_SfpDiagSupplyVoltage_Object((1,3,6,1,4,1,266,20,5,1,1,15),_SfpDiagSupplyVoltage_Type())
sfpDiagSupplyVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagSupplyVoltage.setStatus(_A)
_SfpDiagTxBiasCurrent_Type=Integer32
_SfpDiagTxBiasCurrent_Object=MibTableColumn
sfpDiagTxBiasCurrent=_SfpDiagTxBiasCurrent_Object((1,3,6,1,4,1,266,20,5,1,1,16),_SfpDiagTxBiasCurrent_Type())
sfpDiagTxBiasCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagTxBiasCurrent.setStatus(_A)
_SfpDiagTxOutputPower_Type=Integer32
_SfpDiagTxOutputPower_Object=MibTableColumn
sfpDiagTxOutputPower=_SfpDiagTxOutputPower_Object((1,3,6,1,4,1,266,20,5,1,1,17),_SfpDiagTxOutputPower_Type())
sfpDiagTxOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagTxOutputPower.setStatus(_A)
_SfpDiagTxOutputPowerDbm_Type=Integer32
_SfpDiagTxOutputPowerDbm_Object=MibTableColumn
sfpDiagTxOutputPowerDbm=_SfpDiagTxOutputPowerDbm_Object((1,3,6,1,4,1,266,20,5,1,1,18),_SfpDiagTxOutputPowerDbm_Type())
sfpDiagTxOutputPowerDbm.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagTxOutputPowerDbm.setStatus(_A)
_SfpDiagRxIntputPower_Type=Integer32
_SfpDiagRxIntputPower_Object=MibTableColumn
sfpDiagRxIntputPower=_SfpDiagRxIntputPower_Object((1,3,6,1,4,1,266,20,5,1,1,19),_SfpDiagRxIntputPower_Type())
sfpDiagRxIntputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagRxIntputPower.setStatus(_A)
_SfpDiagRxInputPowerDbm_Type=Integer32
_SfpDiagRxInputPowerDbm_Object=MibTableColumn
sfpDiagRxInputPowerDbm=_SfpDiagRxInputPowerDbm_Object((1,3,6,1,4,1,266,20,5,1,1,20),_SfpDiagRxInputPowerDbm_Type())
sfpDiagRxInputPowerDbm.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagRxInputPowerDbm.setStatus(_A)
_SfpAlarmTxBiasCurrentUpperLimit_Type=Integer32
_SfpAlarmTxBiasCurrentUpperLimit_Object=MibTableColumn
sfpAlarmTxBiasCurrentUpperLimit=_SfpAlarmTxBiasCurrentUpperLimit_Object((1,3,6,1,4,1,266,20,5,1,1,21),_SfpAlarmTxBiasCurrentUpperLimit_Type())
sfpAlarmTxBiasCurrentUpperLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpAlarmTxBiasCurrentUpperLimit.setStatus(_A)
_SfpAlarmTxOutputPowerLowerLimit_Type=Integer32
_SfpAlarmTxOutputPowerLowerLimit_Object=MibTableColumn
sfpAlarmTxOutputPowerLowerLimit=_SfpAlarmTxOutputPowerLowerLimit_Object((1,3,6,1,4,1,266,20,5,1,1,22),_SfpAlarmTxOutputPowerLowerLimit_Type())
sfpAlarmTxOutputPowerLowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpAlarmTxOutputPowerLowerLimit.setStatus(_A)
_SfpAlarmRxInputPowerLowerLimit_Type=Integer32
_SfpAlarmRxInputPowerLowerLimit_Object=MibTableColumn
sfpAlarmRxInputPowerLowerLimit=_SfpAlarmRxInputPowerLowerLimit_Object((1,3,6,1,4,1,266,20,5,1,1,23),_SfpAlarmRxInputPowerLowerLimit_Type())
sfpAlarmRxInputPowerLowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpAlarmRxInputPowerLowerLimit.setStatus(_A)
switchTemperatureFailure=NotificationType((1,3,6,1,4,1,266,20,0,1))
switchTemperatureFailure.setObjects((_B,_A5))
if mibBuilder.loadTexts:switchTemperatureFailure.setStatus(_A)
portLinkChange=NotificationType((1,3,6,1,4,1,266,20,0,2))
portLinkChange.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_A6)))
if mibBuilder.loadTexts:portLinkChange.setStatus(_A)
portNewMacAddress=NotificationType((1,3,6,1,4,1,266,20,0,3))
portNewMacAddress.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_A7)))
if mibBuilder.loadTexts:portNewMacAddress.setStatus(_A)
portSecurityFailure=NotificationType((1,3,6,1,4,1,266,20,0,4))
portSecurityFailure.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_S)))
if mibBuilder.loadTexts:portSecurityFailure.setStatus(_A)
portErrorCountFailure=NotificationType((1,3,6,1,4,1,266,20,0,5))
portErrorCountFailure.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_A8)))
if mibBuilder.loadTexts:portErrorCountFailure.setStatus(_A)
switchMgmtAuthFailure=NotificationType((1,3,6,1,4,1,266,20,0,6))
switchMgmtAuthFailure.setObjects((_B,_T))
if mibBuilder.loadTexts:switchMgmtAuthFailure.setStatus(_A)
radiusMgmtAuthReject=NotificationType((1,3,6,1,4,1,266,20,0,7))
radiusMgmtAuthReject.setObjects((_B,_T))
if mibBuilder.loadTexts:radiusMgmtAuthReject.setStatus(_A)
radiusPortSecurityReject=NotificationType((1,3,6,1,4,1,266,20,0,8))
radiusPortSecurityReject.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_S)))
if mibBuilder.loadTexts:radiusPortSecurityReject.setStatus(_A)
portLoopBcastFailure=NotificationType((1,3,6,1,4,1,266,20,0,9))
portLoopBcastFailure.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:portLoopBcastFailure.setStatus(_A)
switchPoeVoltageFailure=NotificationType((1,3,6,1,4,1,266,20,0,10))
switchPoeVoltageFailure.setObjects((_B,_A9))
if mibBuilder.loadTexts:switchPoeVoltageFailure.setStatus(_A)
switchPoeOverloadFailure=NotificationType((1,3,6,1,4,1,266,20,0,11))
switchPoeOverloadFailure.setObjects((_B,_AA))
if mibBuilder.loadTexts:switchPoeOverloadFailure.setStatus(_A)
portPoeOverloadFailure=NotificationType((1,3,6,1,4,1,266,20,0,12))
portPoeOverloadFailure.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_AB)))
if mibBuilder.loadTexts:portPoeOverloadFailure.setStatus(_A)
portActiveLoopDetectionFailure=NotificationType((1,3,6,1,4,1,266,20,0,13))
portActiveLoopDetectionFailure.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:portActiveLoopDetectionFailure.setStatus(_A)
switchIndustrialAlarmM1=NotificationType((1,3,6,1,4,1,266,20,0,14))
switchIndustrialAlarmM1.setObjects(*((_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:switchIndustrialAlarmM1.setStatus(_A)
switchIndustrialAlarmM2=NotificationType((1,3,6,1,4,1,266,20,0,15))
switchIndustrialAlarmM2.setObjects(*((_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:switchIndustrialAlarmM2.setStatus(_A)
switchInternalVoltageFailure=NotificationType((1,3,6,1,4,1,266,20,0,16))
switchInternalVoltageFailure.setObjects(*((_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:switchInternalVoltageFailure.setStatus(_A)
tftpMessage=NotificationType((1,3,6,1,4,1,266,20,0,17))
tftpMessage.setObjects((_B,_AI))
if mibBuilder.loadTexts:tftpMessage.setStatus(_A)
sfpEvent=NotificationType((1,3,6,1,4,1,266,20,0,18))
sfpEvent.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_AJ)))
if mibBuilder.loadTexts:sfpEvent.setStatus(_A)
clientRemoved=NotificationType((1,3,6,1,4,1,266,20,0,19))
clientRemoved.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:clientRemoved.setStatus(_A)
internalMgmtWarning=NotificationType((1,3,6,1,4,1,266,20,0,20))
internalMgmtWarning.setObjects((_B,_AK))
if mibBuilder.loadTexts:internalMgmtWarning.setStatus(_A)
switchFunctionInputAlarm=NotificationType((1,3,6,1,4,1,266,20,0,21))
switchFunctionInputAlarm.setObjects(*((_B,_AL),(_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:switchFunctionInputAlarm.setStatus(_A)
switchConfigurationChanged=NotificationType((1,3,6,1,4,1,266,20,0,22))
switchConfigurationChanged.setObjects(*((_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:switchConfigurationChanged.setStatus(_A)
portErrorDisabled=NotificationType((1,3,6,1,4,1,266,20,0,23))
portErrorDisabled.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_AQ)))
if mibBuilder.loadTexts:portErrorDisabled.setStatus(_A)
portStateChanged=NotificationType((1,3,6,1,4,1,266,20,0,24))
portStateChanged.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_U,_V),(_B,_AR)))
if mibBuilder.loadTexts:portStateChanged.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bmSwitchMIB':bmSwitchMIB,'bmTraps':bmTraps,'switchTemperatureFailure':switchTemperatureFailure,'portLinkChange':portLinkChange,'portNewMacAddress':portNewMacAddress,'portSecurityFailure':portSecurityFailure,'portErrorCountFailure':portErrorCountFailure,'switchMgmtAuthFailure':switchMgmtAuthFailure,'radiusMgmtAuthReject':radiusMgmtAuthReject,'radiusPortSecurityReject':radiusPortSecurityReject,'portLoopBcastFailure':portLoopBcastFailure,'switchPoeVoltageFailure':switchPoeVoltageFailure,'switchPoeOverloadFailure':switchPoeOverloadFailure,'portPoeOverloadFailure':portPoeOverloadFailure,'portActiveLoopDetectionFailure':portActiveLoopDetectionFailure,'switchIndustrialAlarmM1':switchIndustrialAlarmM1,'switchIndustrialAlarmM2':switchIndustrialAlarmM2,'switchInternalVoltageFailure':switchInternalVoltageFailure,'tftpMessage':tftpMessage,'sfpEvent':sfpEvent,'clientRemoved':clientRemoved,'internalMgmtWarning':internalMgmtWarning,'switchFunctionInputAlarm':switchFunctionInputAlarm,'switchConfigurationChanged':switchConfigurationChanged,'portErrorDisabled':portErrorDisabled,'portStateChanged':portStateChanged,'bmSwitchInfo':bmSwitchInfo,'infoDescr':infoDescr,'infoType':infoType,'infoProductNo':infoProductNo,'infoSerie':infoSerie,'infoSeriesNo':infoSeriesNo,'infoManufactureDate':infoManufactureDate,'infoSwitchHardwareVersion':infoSwitchHardwareVersion,'infoMgmtHardwareVersion':infoMgmtHardwareVersion,'infoMgmtFirmwareVersion':infoMgmtFirmwareVersion,'infoNoOfPorts':infoNoOfPorts,'infoNoOfReboots':infoNoOfReboots,_A5:infoTemperature,'infoTemperatureMaxAllowed':infoTemperatureMaxAllowed,_AG:infoPowerVoltage2500,_AH:infoPowerVoltage3300,_T:infoUnauthIpAddr,_S:infoSecurityFailMacAddr,_A7:infoNewMacAddr,_A9:infoPoeInputVoltage,_AA:infoPoeInputPower,_AC:infoAlarmStateM1,_AE:infoAlarmStateM2,_AI:infoLastTftpMessage,_AJ:infoLastSfpEventMessage,_AK:infoLastInternalMgmtWarning,'infoFunctionInputStateF1':infoFunctionInputStateF1,_AO:infoTotalConfigChanges,_AP:infoLastConfigChangeSource,_AR:infoLastPortStateChangeSource,'infoFunctionInputStateF2':infoFunctionInputStateF2,'infoFunctionInputStateF3':infoFunctionInputStateF3,'infoFunctionInputStateF4':infoFunctionInputStateF4,_AN:infoLastFuncInputAlarmNumber,_AL:infoLastFuncInputAlarmState,_AM:infoLastFuncInputAlarmName,'bmSwitchAdmin':bmSwitchAdmin,'adminReset':adminReset,'adminAgentDhcp':adminAgentDhcp,'adminAgentIpAddress':adminAgentIpAddress,'adminAgentPhysAddress':adminAgentPhysAddress,'adminAgentDefRouterIpAddress':adminAgentDefRouterIpAddress,'adminAgentNetmask':adminAgentNetmask,'adminAgentDhcpServerIpAddress':adminAgentDhcpServerIpAddress,'adminAgentVlanId':adminAgentVlanId,'adminAgentPrioValue':adminAgentPrioValue,'adminAddrAgingTimeMinutes':adminAddrAgingTimeMinutes,'adminSwitchPortMirror':adminSwitchPortMirror,'adminMgmtAccessList':adminMgmtAccessList,'adminSwitchPoEPowerLimit':adminSwitchPoEPowerLimit,'adminSwitchVlanTableMode':adminSwitchVlanTableMode,'adminUnsecureVlanId':adminUnsecureVlanId,'adminDot1xAuthFailureVlanId':adminDot1xAuthFailureVlanId,'adminTftpAccess':adminTftpAccess,'adminSnmpMacTableMode':adminSnmpMacTableMode,'adminAlarmM1':adminAlarmM1,'adminAlarmM2':adminAlarmM2,'adminMemoryCardMode':adminMemoryCardMode,_AD:adminAlarmNameM1,_AF:adminAlarmNameM2,'adminFunctionInputNameF1':adminFunctionInputNameF1,'adminLedGlobalMode':adminLedGlobalMode,'adminFunctionInputNameF2':adminFunctionInputNameF2,'adminFunctionInputNameF3':adminFunctionInputNameF3,'adminFunctionInputNameF4':adminFunctionInputNameF4,'bmSwitchPort':bmSwitchPort,'bmSwitchPortTable':bmSwitchPortTable,'bmSwitchPortEntry':bmSwitchPortEntry,_H:portIndex,_I:portDescr,_J:portName,_AQ:portAdminState,'portSpeedDuplexSetup':portSpeedDuplexSetup,_A6:portLinkState,_A8:portErrorCounter,'portRemoteFault':portRemoteFault,'portDefaultVlanId':portDefaultVlanId,'portTrunkingMode':portTrunkingMode,'portDot1qDefaultPrioValue':portDot1qDefaultPrioValue,'portDefaultPrioQueue':portDefaultPrioQueue,'portLEDGreen':portLEDGreen,'portLEDYellow':portLEDYellow,'portBandwidthLimitRxd':portBandwidthLimitRxd,'portBandwidthLimitTxd':portBandwidthLimitTxd,'portSecurityAdminState':portSecurityAdminState,'portSecurityMacAddr1':portSecurityMacAddr1,'portSecurityMacAddr2':portSecurityMacAddr2,'portSecurityMacAddr3':portSecurityMacAddr3,'portPoeAdminState':portPoeAdminState,'portPoeVoltage':portPoeVoltage,'portPoeCurrent':portPoeCurrent,_AB:portPoePower,'portSecurityForwardingState':portSecurityForwardingState,'portPoePowerLimit':portPoePowerLimit,'portLimiterPacketType':portLimiterPacketType,'portAcApSetup':portAcApSetup,'portLinkType':portLinkType,'portVoiceVlanId':portVoiceVlanId,'portPrioDot1p':portPrioDot1p,'portPrioIp':portPrioIp,'portActiveDefaultVlanId':portActiveDefaultVlanId,'portActiveVoiceVlanId':portActiveVoiceVlanId,'bmSwitchVlan':bmSwitchVlan,'bmSwitchVlanTable':bmSwitchVlanTable,'bmSwitchVlanEntry':bmSwitchVlanEntry,_A3:vlanIndex,'vlanId':vlanId,'vlanDescr':vlanDescr,'bmSwitchSfp':bmSwitchSfp,'bmSwitchSfpTable':bmSwitchSfpTable,'bmSwitchSfpEntry':bmSwitchSfpEntry,_A4:sfpPortIndex,'sfpState':sfpState,'sfpInfoVendorName':sfpInfoVendorName,'sfpInfoPartNumber':sfpInfoPartNumber,'sfpInfoRevisionNumber':sfpInfoRevisionNumber,'sfpInfoSerialNumber':sfpInfoSerialNumber,'sfpInfoDateCode':sfpInfoDateCode,'sfpInfoBitRate':sfpInfoBitRate,'sfpInfoWavelength':sfpInfoWavelength,'sfpInfoLength9um':sfpInfoLength9um,'sfpInfoLength50um':sfpInfoLength50um,'sfpInfoLength62um':sfpInfoLength62um,'sfpInfoConnectorDescr':sfpInfoConnectorDescr,'sfpDiagTemperature':sfpDiagTemperature,'sfpDiagSupplyVoltage':sfpDiagSupplyVoltage,'sfpDiagTxBiasCurrent':sfpDiagTxBiasCurrent,'sfpDiagTxOutputPower':sfpDiagTxOutputPower,'sfpDiagTxOutputPowerDbm':sfpDiagTxOutputPowerDbm,'sfpDiagRxIntputPower':sfpDiagRxIntputPower,'sfpDiagRxInputPowerDbm':sfpDiagRxInputPowerDbm,'sfpAlarmTxBiasCurrentUpperLimit':sfpAlarmTxBiasCurrentUpperLimit,'sfpAlarmTxOutputPowerLowerLimit':sfpAlarmTxOutputPowerLowerLimit,'sfpAlarmRxInputPowerLowerLimit':sfpAlarmRxInputPowerLowerLimit})