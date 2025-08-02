_K='remEthAlarm'
_J='locEthAlarm'
_I='rateLimit'
_H='rateType'
_G='rateConfig'
_F='function'
_E='DisplayString'
_D='read-only'
_C='ETHERNET-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
interface,locEthAlarms,remEthAlarms=mibBuilder.importSymbols('ExaltComProducts','interface','locEthAlarms','remEthAlarms')
AlarmLevelT,EnableStatusT,EthernetMgmtTypeT=mibBuilder.importSymbols('ExaltComm','AlarmLevelT','EnableStatusT','EthernetMgmtTypeT')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
class EthernetFunctionT(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('traffic',0),('mgmt',1),('trafficmgmt',2)))
class EthernetModeT(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('full1000',0),('half1000',1),('full100',2),('half100',3),('full10',4),('half10',5),('auto',6)))
class EthRateLimitTypeT(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('kbps',0),('mbps',1)))
class EthRateLimitValueT(TextualConvention,Integer32):status=_A
_Ethernet_ObjectIdentity=ObjectIdentity
ethernet=_Ethernet_ObjectIdentity((1,3,6,1,4,1,25651,1,2,3,2,1))
if mibBuilder.loadTexts:ethernet.setStatus(_A)
_EthernetNumChannels_Type=Gauge32
_EthernetNumChannels_Object=MibScalar
ethernetNumChannels=_EthernetNumChannels_Object((1,3,6,1,4,1,25651,1,2,3,2,1,3),_EthernetNumChannels_Type())
ethernetNumChannels.setMaxAccess(_D)
if mibBuilder.loadTexts:ethernetNumChannels.setStatus(_A)
if mibBuilder.loadTexts:ethernetNumChannels.setUnits('channels')
_EthernetInterfaces_Object=MibTable
ethernetInterfaces=_EthernetInterfaces_Object((1,3,6,1,4,1,25651,1,2,3,2,1,4))
if mibBuilder.loadTexts:ethernetInterfaces.setStatus(_A)
_EthernetInterface_Object=MibTableRow
ethernetInterface=_EthernetInterface_Object((1,3,6,1,4,1,25651,1,2,3,2,1,4,1))
ethernetInterface.setIndexNames((0,_C,_F),(0,_C,'mode'),(0,_C,'alarm'),(0,_C,'mute'),(0,_C,'dhcp'),(0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:ethernetInterface.setStatus(_A)
_Function_Type=EthernetFunctionT
_Function_Object=MibTableColumn
function=_Function_Object((1,3,6,1,4,1,25651,1,2,3,2,1,4,1,1),_Function_Type())
function.setMaxAccess(_B)
if mibBuilder.loadTexts:function.setStatus(_A)
_Mode_Type=EthernetModeT
_Mode_Object=MibTableColumn
mode=_Mode_Object((1,3,6,1,4,1,25651,1,2,3,2,1,4,1,2),_Mode_Type())
mode.setMaxAccess(_B)
if mibBuilder.loadTexts:mode.setStatus(_A)
_Alarm_Type=EnableStatusT
_Alarm_Object=MibTableColumn
alarm=_Alarm_Object((1,3,6,1,4,1,25651,1,2,3,2,1,4,1,3),_Alarm_Type())
alarm.setMaxAccess(_B)
if mibBuilder.loadTexts:alarm.setStatus(_A)
_Mute_Type=EnableStatusT
_Mute_Object=MibTableColumn
mute=_Mute_Object((1,3,6,1,4,1,25651,1,2,3,2,1,4,1,4),_Mute_Type())
mute.setMaxAccess(_B)
if mibBuilder.loadTexts:mute.setStatus(_A)
_RateConfig_Type=EnableStatusT
_RateConfig_Object=MibTableColumn
rateConfig=_RateConfig_Object((1,3,6,1,4,1,25651,1,2,3,2,1,4,1,5),_RateConfig_Type())
rateConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:rateConfig.setStatus(_A)
_RateType_Type=EthRateLimitTypeT
_RateType_Object=MibTableColumn
rateType=_RateType_Object((1,3,6,1,4,1,25651,1,2,3,2,1,4,1,6),_RateType_Type())
rateType.setMaxAccess(_B)
if mibBuilder.loadTexts:rateType.setStatus(_A)
_RateLimit_Type=EthRateLimitValueT
_RateLimit_Object=MibTableColumn
rateLimit=_RateLimit_Object((1,3,6,1,4,1,25651,1,2,3,2,1,4,1,7),_RateLimit_Type())
rateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:rateLimit.setStatus(_A)
_Dhcp_Type=EnableStatusT
_Dhcp_Object=MibTableColumn
dhcp=_Dhcp_Object((1,3,6,1,4,1,25651,1,2,3,2,1,4,1,8),_Dhcp_Type())
dhcp.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcp.setStatus(_A)
_EthernetLearning_Type=EnableStatusT
_EthernetLearning_Object=MibScalar
ethernetLearning=_EthernetLearning_Object((1,3,6,1,4,1,25651,1,2,3,2,1,5),_EthernetLearning_Type())
ethernetLearning.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetLearning.setStatus(_A)
_EthernetMgmt_Type=EthernetMgmtTypeT
_EthernetMgmt_Object=MibScalar
ethernetMgmt=_EthernetMgmt_Object((1,3,6,1,4,1,25651,1,2,3,2,1,6),_EthernetMgmt_Type())
ethernetMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetMgmt.setStatus(_A)
_EthernetFlowControl_Type=EnableStatusT
_EthernetFlowControl_Object=MibScalar
ethernetFlowControl=_EthernetFlowControl_Object((1,3,6,1,4,1,25651,1,2,3,2,1,7),_EthernetFlowControl_Type())
ethernetFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetFlowControl.setStatus(_A)
class _CommitEthernetSettings_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,200))
_CommitEthernetSettings_Type.__name__=_E
_CommitEthernetSettings_Object=MibScalar
commitEthernetSettings=_CommitEthernetSettings_Object((1,3,6,1,4,1,25651,1,2,3,2,1,1000),_CommitEthernetSettings_Type())
commitEthernetSettings.setMaxAccess(_B)
if mibBuilder.loadTexts:commitEthernetSettings.setStatus(_A)
_LocETHAlarms_Object=MibTable
locETHAlarms=_LocETHAlarms_Object((1,3,6,1,4,1,25651,1,2,4,2,3,2,1))
if mibBuilder.loadTexts:locETHAlarms.setStatus(_A)
_LocEthAlarmsEntry_Object=MibTableRow
locEthAlarmsEntry=_LocEthAlarmsEntry_Object((1,3,6,1,4,1,25651,1,2,4,2,3,2,1,1))
locEthAlarmsEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:locEthAlarmsEntry.setStatus(_A)
_LocEthAlarm_Type=AlarmLevelT
_LocEthAlarm_Object=MibTableColumn
locEthAlarm=_LocEthAlarm_Object((1,3,6,1,4,1,25651,1,2,4,2,3,2,1,1,1),_LocEthAlarm_Type())
locEthAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:locEthAlarm.setStatus(_A)
_RemETHAlarms_Object=MibTable
remETHAlarms=_RemETHAlarms_Object((1,3,6,1,4,1,25651,1,2,4,2,4,2,1))
if mibBuilder.loadTexts:remETHAlarms.setStatus(_A)
_RemEthAlarmsEntry_Object=MibTableRow
remEthAlarmsEntry=_RemEthAlarmsEntry_Object((1,3,6,1,4,1,25651,1,2,4,2,4,2,1,1))
remEthAlarmsEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:remEthAlarmsEntry.setStatus(_A)
_RemEthAlarm_Type=AlarmLevelT
_RemEthAlarm_Object=MibTableColumn
remEthAlarm=_RemEthAlarm_Object((1,3,6,1,4,1,25651,1,2,4,2,4,2,1,1,1),_RemEthAlarm_Type())
remEthAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:remEthAlarm.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'EthernetFunctionT':EthernetFunctionT,'EthernetModeT':EthernetModeT,'EthRateLimitTypeT':EthRateLimitTypeT,'EthRateLimitValueT':EthRateLimitValueT,'ethernet':ethernet,'ethernetNumChannels':ethernetNumChannels,'ethernetInterfaces':ethernetInterfaces,'ethernetInterface':ethernetInterface,_F:function,'mode':mode,'alarm':alarm,'mute':mute,_G:rateConfig,_H:rateType,_I:rateLimit,'dhcp':dhcp,'ethernetLearning':ethernetLearning,'ethernetMgmt':ethernetMgmt,'ethernetFlowControl':ethernetFlowControl,'commitEthernetSettings':commitEthernetSettings,'locETHAlarms':locETHAlarms,'locEthAlarmsEntry':locEthAlarmsEntry,_J:locEthAlarm,'remETHAlarms':remETHAlarms,'remEthAlarmsEntry':remEthAlarmsEntry,_K:remEthAlarm})