_AJ='cnpdSupportedProtocolsGroup'
_AI='cnpdMIBNotificationsConfigGroup'
_AH='cnpdMIBNotificationsGroup'
_AG='cnpdThresholdGroup'
_AF='cnpdTopNGroup'
_AE='cnpdStatsGroup'
_AD='cnpdThresholdFallingEvent'
_AC='cnpdThresholdRisingEvent'
_AB='cnpdSupportedProtocolsName'
_AA='cnpdNotificationsEnable'
_A9='cnpdThresholdHistoryStatsSelect'
_A8='cnpdThresholdHistoryProtocol'
_A7='cnpdThresholdHistoryType'
_A6='cnpdThresholdHistoryConfigIndex'
_A5='cnpdThresholdConfigStatus'
_A4='cnpdThresholdConfigStartup'
_A3='cnpdThresholdConfigProtocolAny'
_A2='cnpdThresholdConfigSampleType'
_A1='cnpdThresholdConfigInterval'
_A0='cnpdTopNStatsHCRate'
_z='cnpdTopNStatsRate'
_y='cnpdTopNStatsProtocolName'
_x='cnpdTopNConfigStatus'
_w='cnpdTopNConfigTime'
_v='cnpdTopNConfigGrantedSize'
_u='cnpdTopNConfigSampleTime'
_t='cnpdTopNConfigRequestedSize'
_s='cnpdTopNConfigStatsSelect'
_r='cnpdTopNConfigIfIndex'
_q='cnpdAllStatsOutBitRate'
_p='cnpdAllStatsInBitRate'
_o='cnpdAllStatsHCOutBytes'
_n='cnpdAllStatsHCInBytes'
_m='cnpdAllStatsHCOutPkts'
_l='cnpdAllStatsHCInPkts'
_k='cnpdAllStatsOutBytes'
_j='cnpdAllStatsInBytes'
_i='cnpdAllStatsOutPkts'
_h='cnpdAllStatsInPkts'
_g='cnpdAllStatsProtocolName'
_f='cnpdStatusLastUpdateTime'
_e='cnpdStatusPdEnable'
_d='cnpdSupportedProtocolsIndex'
_c='cnpdThresholdHistoryIndex'
_b='cnpdThresholdConfigIndex'
_a='cnpdTopNStatsIndex'
_Z='seconds'
_Y='kilo bits per second'
_X='cnpdAllStatsProtocolsIndex'
_W='read-write'
_V='cnpdThresholdConfigFalling'
_U='cnpdThresholdConfigRising'
_T='CiscoPdDataType'
_S='cnpdTopNConfigIndex'
_R='TruthValue'
_Q='ifIndex'
_P='IF-MIB'
_O='cnpdThresholdHistoryTime'
_N='cnpdThresholdHistoryValue'
_M='cnpdThresholdConfigStatsSelect'
_L='cnpdThresholdConfigProtocol'
_K='cnpdThresholdConfigIfIndex'
_J='bytes'
_I='packets'
_H='Integer32'
_G='CiscoPdProtocolIndex'
_F='not-accessible'
_E='read-create'
_D='Unsigned32'
_C='read-only'
_B='CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_P,'InterfaceIndex',_Q)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_R)
ciscoNbarProtocolDiscoveryMIB=ModuleIdentity((1,3,6,1,4,1,9,9,244))
if mibBuilder.loadTexts:ciscoNbarProtocolDiscoveryMIB.setRevisions(('2002-08-16 00:00','2001-12-28 00:00'))
class CiscoPdProtocolIndex(TextualConvention,Unsigned32):status=_A
class CiscoPdProtocolName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
class CiscoPdDataType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('bitRateIn',1),('bitRateOut',2),('bitRateSum',3),('byteCountIn',4),('byteCountOut',5),('byteCountSum',6),('packetCountIn',7),('packetCountOut',8),('packetCountSum',9)))
_CnpdMIBNotifications_ObjectIdentity=ObjectIdentity
cnpdMIBNotifications=_CnpdMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,244,0))
_CnpdMIBObjects_ObjectIdentity=ObjectIdentity
cnpdMIBObjects=_CnpdMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,244,1))
_CnpdStatus_ObjectIdentity=ObjectIdentity
cnpdStatus=_CnpdStatus_ObjectIdentity((1,3,6,1,4,1,9,9,244,1,1))
_CnpdStatusTable_Object=MibTable
cnpdStatusTable=_CnpdStatusTable_Object((1,3,6,1,4,1,9,9,244,1,1,1))
if mibBuilder.loadTexts:cnpdStatusTable.setStatus(_A)
_CnpdStatusEntry_Object=MibTableRow
cnpdStatusEntry=_CnpdStatusEntry_Object((1,3,6,1,4,1,9,9,244,1,1,1,1))
cnpdStatusEntry.setIndexNames((0,_P,_Q))
if mibBuilder.loadTexts:cnpdStatusEntry.setStatus(_A)
_CnpdStatusPdEnable_Type=TruthValue
_CnpdStatusPdEnable_Object=MibTableColumn
cnpdStatusPdEnable=_CnpdStatusPdEnable_Object((1,3,6,1,4,1,9,9,244,1,1,1,1,1),_CnpdStatusPdEnable_Type())
cnpdStatusPdEnable.setMaxAccess(_W)
if mibBuilder.loadTexts:cnpdStatusPdEnable.setStatus(_A)
_CnpdStatusLastUpdateTime_Type=TimeTicks
_CnpdStatusLastUpdateTime_Object=MibTableColumn
cnpdStatusLastUpdateTime=_CnpdStatusLastUpdateTime_Object((1,3,6,1,4,1,9,9,244,1,1,1,1,2),_CnpdStatusLastUpdateTime_Type())
cnpdStatusLastUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdStatusLastUpdateTime.setStatus(_A)
_CnpdAllStats_ObjectIdentity=ObjectIdentity
cnpdAllStats=_CnpdAllStats_ObjectIdentity((1,3,6,1,4,1,9,9,244,1,2))
_CnpdAllStatsTable_Object=MibTable
cnpdAllStatsTable=_CnpdAllStatsTable_Object((1,3,6,1,4,1,9,9,244,1,2,1))
if mibBuilder.loadTexts:cnpdAllStatsTable.setStatus(_A)
_CnpdAllStatsEntry_Object=MibTableRow
cnpdAllStatsEntry=_CnpdAllStatsEntry_Object((1,3,6,1,4,1,9,9,244,1,2,1,1))
cnpdAllStatsEntry.setIndexNames((0,_P,_Q),(0,_B,_X))
if mibBuilder.loadTexts:cnpdAllStatsEntry.setStatus(_A)
class _CnpdAllStatsProtocolsIndex_Type(CiscoPdProtocolIndex):subtypeSpec=CiscoPdProtocolIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CnpdAllStatsProtocolsIndex_Type.__name__=_G
_CnpdAllStatsProtocolsIndex_Object=MibTableColumn
cnpdAllStatsProtocolsIndex=_CnpdAllStatsProtocolsIndex_Object((1,3,6,1,4,1,9,9,244,1,2,1,1,1),_CnpdAllStatsProtocolsIndex_Type())
cnpdAllStatsProtocolsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cnpdAllStatsProtocolsIndex.setStatus(_A)
_CnpdAllStatsProtocolName_Type=CiscoPdProtocolName
_CnpdAllStatsProtocolName_Object=MibTableColumn
cnpdAllStatsProtocolName=_CnpdAllStatsProtocolName_Object((1,3,6,1,4,1,9,9,244,1,2,1,1,2),_CnpdAllStatsProtocolName_Type())
cnpdAllStatsProtocolName.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdAllStatsProtocolName.setStatus(_A)
_CnpdAllStatsInPkts_Type=Counter32
_CnpdAllStatsInPkts_Object=MibTableColumn
cnpdAllStatsInPkts=_CnpdAllStatsInPkts_Object((1,3,6,1,4,1,9,9,244,1,2,1,1,3),_CnpdAllStatsInPkts_Type())
cnpdAllStatsInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdAllStatsInPkts.setStatus(_A)
if mibBuilder.loadTexts:cnpdAllStatsInPkts.setUnits(_I)
_CnpdAllStatsOutPkts_Type=Counter32
_CnpdAllStatsOutPkts_Object=MibTableColumn
cnpdAllStatsOutPkts=_CnpdAllStatsOutPkts_Object((1,3,6,1,4,1,9,9,244,1,2,1,1,4),_CnpdAllStatsOutPkts_Type())
cnpdAllStatsOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdAllStatsOutPkts.setStatus(_A)
if mibBuilder.loadTexts:cnpdAllStatsOutPkts.setUnits(_I)
_CnpdAllStatsInBytes_Type=Counter32
_CnpdAllStatsInBytes_Object=MibTableColumn
cnpdAllStatsInBytes=_CnpdAllStatsInBytes_Object((1,3,6,1,4,1,9,9,244,1,2,1,1,5),_CnpdAllStatsInBytes_Type())
cnpdAllStatsInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdAllStatsInBytes.setStatus(_A)
if mibBuilder.loadTexts:cnpdAllStatsInBytes.setUnits(_J)
_CnpdAllStatsOutBytes_Type=Counter32
_CnpdAllStatsOutBytes_Object=MibTableColumn
cnpdAllStatsOutBytes=_CnpdAllStatsOutBytes_Object((1,3,6,1,4,1,9,9,244,1,2,1,1,6),_CnpdAllStatsOutBytes_Type())
cnpdAllStatsOutBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdAllStatsOutBytes.setStatus(_A)
if mibBuilder.loadTexts:cnpdAllStatsOutBytes.setUnits(_J)
_CnpdAllStatsHCInPkts_Type=Counter64
_CnpdAllStatsHCInPkts_Object=MibTableColumn
cnpdAllStatsHCInPkts=_CnpdAllStatsHCInPkts_Object((1,3,6,1,4,1,9,9,244,1,2,1,1,7),_CnpdAllStatsHCInPkts_Type())
cnpdAllStatsHCInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdAllStatsHCInPkts.setStatus(_A)
if mibBuilder.loadTexts:cnpdAllStatsHCInPkts.setUnits(_I)
_CnpdAllStatsHCOutPkts_Type=Counter64
_CnpdAllStatsHCOutPkts_Object=MibTableColumn
cnpdAllStatsHCOutPkts=_CnpdAllStatsHCOutPkts_Object((1,3,6,1,4,1,9,9,244,1,2,1,1,8),_CnpdAllStatsHCOutPkts_Type())
cnpdAllStatsHCOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdAllStatsHCOutPkts.setStatus(_A)
if mibBuilder.loadTexts:cnpdAllStatsHCOutPkts.setUnits(_I)
_CnpdAllStatsHCInBytes_Type=Counter64
_CnpdAllStatsHCInBytes_Object=MibTableColumn
cnpdAllStatsHCInBytes=_CnpdAllStatsHCInBytes_Object((1,3,6,1,4,1,9,9,244,1,2,1,1,9),_CnpdAllStatsHCInBytes_Type())
cnpdAllStatsHCInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdAllStatsHCInBytes.setStatus(_A)
if mibBuilder.loadTexts:cnpdAllStatsHCInBytes.setUnits(_J)
_CnpdAllStatsHCOutBytes_Type=Counter64
_CnpdAllStatsHCOutBytes_Object=MibTableColumn
cnpdAllStatsHCOutBytes=_CnpdAllStatsHCOutBytes_Object((1,3,6,1,4,1,9,9,244,1,2,1,1,10),_CnpdAllStatsHCOutBytes_Type())
cnpdAllStatsHCOutBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdAllStatsHCOutBytes.setStatus(_A)
if mibBuilder.loadTexts:cnpdAllStatsHCOutBytes.setUnits(_J)
class _CnpdAllStatsInBitRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CnpdAllStatsInBitRate_Type.__name__=_D
_CnpdAllStatsInBitRate_Object=MibTableColumn
cnpdAllStatsInBitRate=_CnpdAllStatsInBitRate_Object((1,3,6,1,4,1,9,9,244,1,2,1,1,11),_CnpdAllStatsInBitRate_Type())
cnpdAllStatsInBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdAllStatsInBitRate.setStatus(_A)
if mibBuilder.loadTexts:cnpdAllStatsInBitRate.setUnits(_Y)
class _CnpdAllStatsOutBitRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CnpdAllStatsOutBitRate_Type.__name__=_D
_CnpdAllStatsOutBitRate_Object=MibTableColumn
cnpdAllStatsOutBitRate=_CnpdAllStatsOutBitRate_Object((1,3,6,1,4,1,9,9,244,1,2,1,1,12),_CnpdAllStatsOutBitRate_Type())
cnpdAllStatsOutBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdAllStatsOutBitRate.setStatus(_A)
if mibBuilder.loadTexts:cnpdAllStatsOutBitRate.setUnits(_Y)
_CnpdTopNConfig_ObjectIdentity=ObjectIdentity
cnpdTopNConfig=_CnpdTopNConfig_ObjectIdentity((1,3,6,1,4,1,9,9,244,1,3))
_CnpdTopNConfigTable_Object=MibTable
cnpdTopNConfigTable=_CnpdTopNConfigTable_Object((1,3,6,1,4,1,9,9,244,1,3,1))
if mibBuilder.loadTexts:cnpdTopNConfigTable.setStatus(_A)
_CnpdTopNConfigEntry_Object=MibTableRow
cnpdTopNConfigEntry=_CnpdTopNConfigEntry_Object((1,3,6,1,4,1,9,9,244,1,3,1,1))
cnpdTopNConfigEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:cnpdTopNConfigEntry.setStatus(_A)
class _CnpdTopNConfigIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_CnpdTopNConfigIndex_Type.__name__=_D
_CnpdTopNConfigIndex_Object=MibTableColumn
cnpdTopNConfigIndex=_CnpdTopNConfigIndex_Object((1,3,6,1,4,1,9,9,244,1,3,1,1,1),_CnpdTopNConfigIndex_Type())
cnpdTopNConfigIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cnpdTopNConfigIndex.setStatus(_A)
_CnpdTopNConfigIfIndex_Type=InterfaceIndex
_CnpdTopNConfigIfIndex_Object=MibTableColumn
cnpdTopNConfigIfIndex=_CnpdTopNConfigIfIndex_Object((1,3,6,1,4,1,9,9,244,1,3,1,1,2),_CnpdTopNConfigIfIndex_Type())
cnpdTopNConfigIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cnpdTopNConfigIfIndex.setStatus(_A)
class _CnpdTopNConfigStatsSelect_Type(CiscoPdDataType):defaultValue=6
_CnpdTopNConfigStatsSelect_Type.__name__=_T
_CnpdTopNConfigStatsSelect_Object=MibTableColumn
cnpdTopNConfigStatsSelect=_CnpdTopNConfigStatsSelect_Object((1,3,6,1,4,1,9,9,244,1,3,1,1,3),_CnpdTopNConfigStatsSelect_Type())
cnpdTopNConfigStatsSelect.setMaxAccess(_E)
if mibBuilder.loadTexts:cnpdTopNConfigStatsSelect.setStatus(_A)
class _CnpdTopNConfigSampleTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_CnpdTopNConfigSampleTime_Type.__name__=_D
_CnpdTopNConfigSampleTime_Object=MibTableColumn
cnpdTopNConfigSampleTime=_CnpdTopNConfigSampleTime_Object((1,3,6,1,4,1,9,9,244,1,3,1,1,4),_CnpdTopNConfigSampleTime_Type())
cnpdTopNConfigSampleTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cnpdTopNConfigSampleTime.setStatus(_A)
if mibBuilder.loadTexts:cnpdTopNConfigSampleTime.setUnits(_Z)
class _CnpdTopNConfigRequestedSize_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_CnpdTopNConfigRequestedSize_Type.__name__=_D
_CnpdTopNConfigRequestedSize_Object=MibTableColumn
cnpdTopNConfigRequestedSize=_CnpdTopNConfigRequestedSize_Object((1,3,6,1,4,1,9,9,244,1,3,1,1,5),_CnpdTopNConfigRequestedSize_Type())
cnpdTopNConfigRequestedSize.setMaxAccess(_E)
if mibBuilder.loadTexts:cnpdTopNConfigRequestedSize.setStatus(_A)
class _CnpdTopNConfigGrantedSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_CnpdTopNConfigGrantedSize_Type.__name__=_D
_CnpdTopNConfigGrantedSize_Object=MibTableColumn
cnpdTopNConfigGrantedSize=_CnpdTopNConfigGrantedSize_Object((1,3,6,1,4,1,9,9,244,1,3,1,1,6),_CnpdTopNConfigGrantedSize_Type())
cnpdTopNConfigGrantedSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdTopNConfigGrantedSize.setStatus(_A)
_CnpdTopNConfigTime_Type=TimeTicks
_CnpdTopNConfigTime_Object=MibTableColumn
cnpdTopNConfigTime=_CnpdTopNConfigTime_Object((1,3,6,1,4,1,9,9,244,1,3,1,1,7),_CnpdTopNConfigTime_Type())
cnpdTopNConfigTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdTopNConfigTime.setStatus(_A)
_CnpdTopNConfigStatus_Type=RowStatus
_CnpdTopNConfigStatus_Object=MibTableColumn
cnpdTopNConfigStatus=_CnpdTopNConfigStatus_Object((1,3,6,1,4,1,9,9,244,1,3,1,1,8),_CnpdTopNConfigStatus_Type())
cnpdTopNConfigStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cnpdTopNConfigStatus.setStatus(_A)
_CnpdTopNStats_ObjectIdentity=ObjectIdentity
cnpdTopNStats=_CnpdTopNStats_ObjectIdentity((1,3,6,1,4,1,9,9,244,1,4))
_CnpdTopNStatsTable_Object=MibTable
cnpdTopNStatsTable=_CnpdTopNStatsTable_Object((1,3,6,1,4,1,9,9,244,1,4,1))
if mibBuilder.loadTexts:cnpdTopNStatsTable.setStatus(_A)
_CnpdTopNStatsEntry_Object=MibTableRow
cnpdTopNStatsEntry=_CnpdTopNStatsEntry_Object((1,3,6,1,4,1,9,9,244,1,4,1,1))
cnpdTopNStatsEntry.setIndexNames((0,_B,_S),(0,_B,_a))
if mibBuilder.loadTexts:cnpdTopNStatsEntry.setStatus(_A)
class _CnpdTopNStatsIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_CnpdTopNStatsIndex_Type.__name__=_D
_CnpdTopNStatsIndex_Object=MibTableColumn
cnpdTopNStatsIndex=_CnpdTopNStatsIndex_Object((1,3,6,1,4,1,9,9,244,1,4,1,1,1),_CnpdTopNStatsIndex_Type())
cnpdTopNStatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cnpdTopNStatsIndex.setStatus(_A)
_CnpdTopNStatsProtocolName_Type=CiscoPdProtocolName
_CnpdTopNStatsProtocolName_Object=MibTableColumn
cnpdTopNStatsProtocolName=_CnpdTopNStatsProtocolName_Object((1,3,6,1,4,1,9,9,244,1,4,1,1,2),_CnpdTopNStatsProtocolName_Type())
cnpdTopNStatsProtocolName.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdTopNStatsProtocolName.setStatus(_A)
_CnpdTopNStatsRate_Type=Counter32
_CnpdTopNStatsRate_Object=MibTableColumn
cnpdTopNStatsRate=_CnpdTopNStatsRate_Object((1,3,6,1,4,1,9,9,244,1,4,1,1,3),_CnpdTopNStatsRate_Type())
cnpdTopNStatsRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdTopNStatsRate.setStatus(_A)
_CnpdTopNStatsHCRate_Type=Counter64
_CnpdTopNStatsHCRate_Object=MibTableColumn
cnpdTopNStatsHCRate=_CnpdTopNStatsHCRate_Object((1,3,6,1,4,1,9,9,244,1,4,1,1,4),_CnpdTopNStatsHCRate_Type())
cnpdTopNStatsHCRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdTopNStatsHCRate.setStatus(_A)
_CnpdThresholdConfig_ObjectIdentity=ObjectIdentity
cnpdThresholdConfig=_CnpdThresholdConfig_ObjectIdentity((1,3,6,1,4,1,9,9,244,1,5))
_CnpdThresholdConfigTable_Object=MibTable
cnpdThresholdConfigTable=_CnpdThresholdConfigTable_Object((1,3,6,1,4,1,9,9,244,1,5,1))
if mibBuilder.loadTexts:cnpdThresholdConfigTable.setStatus(_A)
_CnpdThresholdConfigEntry_Object=MibTableRow
cnpdThresholdConfigEntry=_CnpdThresholdConfigEntry_Object((1,3,6,1,4,1,9,9,244,1,5,1,1))
cnpdThresholdConfigEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:cnpdThresholdConfigEntry.setStatus(_A)
class _CnpdThresholdConfigIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CnpdThresholdConfigIndex_Type.__name__=_D
_CnpdThresholdConfigIndex_Object=MibTableColumn
cnpdThresholdConfigIndex=_CnpdThresholdConfigIndex_Object((1,3,6,1,4,1,9,9,244,1,5,1,1,1),_CnpdThresholdConfigIndex_Type())
cnpdThresholdConfigIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cnpdThresholdConfigIndex.setStatus(_A)
_CnpdThresholdConfigIfIndex_Type=InterfaceIndex
_CnpdThresholdConfigIfIndex_Object=MibTableColumn
cnpdThresholdConfigIfIndex=_CnpdThresholdConfigIfIndex_Object((1,3,6,1,4,1,9,9,244,1,5,1,1,2),_CnpdThresholdConfigIfIndex_Type())
cnpdThresholdConfigIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cnpdThresholdConfigIfIndex.setStatus(_A)
class _CnpdThresholdConfigInterval_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_CnpdThresholdConfigInterval_Type.__name__=_D
_CnpdThresholdConfigInterval_Object=MibTableColumn
cnpdThresholdConfigInterval=_CnpdThresholdConfigInterval_Object((1,3,6,1,4,1,9,9,244,1,5,1,1,3),_CnpdThresholdConfigInterval_Type())
cnpdThresholdConfigInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cnpdThresholdConfigInterval.setStatus(_A)
if mibBuilder.loadTexts:cnpdThresholdConfigInterval.setUnits(_Z)
class _CnpdThresholdConfigSampleType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absoluteValue',1),('deltaValue',2)))
_CnpdThresholdConfigSampleType_Type.__name__=_H
_CnpdThresholdConfigSampleType_Object=MibTableColumn
cnpdThresholdConfigSampleType=_CnpdThresholdConfigSampleType_Object((1,3,6,1,4,1,9,9,244,1,5,1,1,4),_CnpdThresholdConfigSampleType_Type())
cnpdThresholdConfigSampleType.setMaxAccess(_E)
if mibBuilder.loadTexts:cnpdThresholdConfigSampleType.setStatus(_A)
class _CnpdThresholdConfigProtocol_Type(CiscoPdProtocolIndex):subtypeSpec=CiscoPdProtocolIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CnpdThresholdConfigProtocol_Type.__name__=_G
_CnpdThresholdConfigProtocol_Object=MibTableColumn
cnpdThresholdConfigProtocol=_CnpdThresholdConfigProtocol_Object((1,3,6,1,4,1,9,9,244,1,5,1,1,5),_CnpdThresholdConfigProtocol_Type())
cnpdThresholdConfigProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:cnpdThresholdConfigProtocol.setStatus(_A)
class _CnpdThresholdConfigProtocolAny_Type(TruthValue):defaultValue=1
_CnpdThresholdConfigProtocolAny_Type.__name__=_R
_CnpdThresholdConfigProtocolAny_Object=MibTableColumn
cnpdThresholdConfigProtocolAny=_CnpdThresholdConfigProtocolAny_Object((1,3,6,1,4,1,9,9,244,1,5,1,1,6),_CnpdThresholdConfigProtocolAny_Type())
cnpdThresholdConfigProtocolAny.setMaxAccess(_E)
if mibBuilder.loadTexts:cnpdThresholdConfigProtocolAny.setStatus(_A)
class _CnpdThresholdConfigStatsSelect_Type(CiscoPdDataType):defaultValue=3
_CnpdThresholdConfigStatsSelect_Type.__name__=_T
_CnpdThresholdConfigStatsSelect_Object=MibTableColumn
cnpdThresholdConfigStatsSelect=_CnpdThresholdConfigStatsSelect_Object((1,3,6,1,4,1,9,9,244,1,5,1,1,7),_CnpdThresholdConfigStatsSelect_Type())
cnpdThresholdConfigStatsSelect.setMaxAccess(_E)
if mibBuilder.loadTexts:cnpdThresholdConfigStatsSelect.setStatus(_A)
class _CnpdThresholdConfigStartup_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rising',1),('falling',2),('risingOrFalling',3)))
_CnpdThresholdConfigStartup_Type.__name__=_H
_CnpdThresholdConfigStartup_Object=MibTableColumn
cnpdThresholdConfigStartup=_CnpdThresholdConfigStartup_Object((1,3,6,1,4,1,9,9,244,1,5,1,1,8),_CnpdThresholdConfigStartup_Type())
cnpdThresholdConfigStartup.setMaxAccess(_E)
if mibBuilder.loadTexts:cnpdThresholdConfigStartup.setStatus(_A)
class _CnpdThresholdConfigRising_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CnpdThresholdConfigRising_Type.__name__=_D
_CnpdThresholdConfigRising_Object=MibTableColumn
cnpdThresholdConfigRising=_CnpdThresholdConfigRising_Object((1,3,6,1,4,1,9,9,244,1,5,1,1,9),_CnpdThresholdConfigRising_Type())
cnpdThresholdConfigRising.setMaxAccess(_E)
if mibBuilder.loadTexts:cnpdThresholdConfigRising.setStatus(_A)
class _CnpdThresholdConfigFalling_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CnpdThresholdConfigFalling_Type.__name__=_D
_CnpdThresholdConfigFalling_Object=MibTableColumn
cnpdThresholdConfigFalling=_CnpdThresholdConfigFalling_Object((1,3,6,1,4,1,9,9,244,1,5,1,1,10),_CnpdThresholdConfigFalling_Type())
cnpdThresholdConfigFalling.setMaxAccess(_E)
if mibBuilder.loadTexts:cnpdThresholdConfigFalling.setStatus(_A)
_CnpdThresholdConfigStatus_Type=RowStatus
_CnpdThresholdConfigStatus_Object=MibTableColumn
cnpdThresholdConfigStatus=_CnpdThresholdConfigStatus_Object((1,3,6,1,4,1,9,9,244,1,5,1,1,12),_CnpdThresholdConfigStatus_Type())
cnpdThresholdConfigStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cnpdThresholdConfigStatus.setStatus(_A)
_CnpdThresholdHistory_ObjectIdentity=ObjectIdentity
cnpdThresholdHistory=_CnpdThresholdHistory_ObjectIdentity((1,3,6,1,4,1,9,9,244,1,6))
_CnpdThresholdHistoryTable_Object=MibTable
cnpdThresholdHistoryTable=_CnpdThresholdHistoryTable_Object((1,3,6,1,4,1,9,9,244,1,6,1))
if mibBuilder.loadTexts:cnpdThresholdHistoryTable.setStatus(_A)
_CnpdThresholdHistoryEntry_Object=MibTableRow
cnpdThresholdHistoryEntry=_CnpdThresholdHistoryEntry_Object((1,3,6,1,4,1,9,9,244,1,6,1,1))
cnpdThresholdHistoryEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:cnpdThresholdHistoryEntry.setStatus(_A)
class _CnpdThresholdHistoryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CnpdThresholdHistoryIndex_Type.__name__=_D
_CnpdThresholdHistoryIndex_Object=MibTableColumn
cnpdThresholdHistoryIndex=_CnpdThresholdHistoryIndex_Object((1,3,6,1,4,1,9,9,244,1,6,1,1,1),_CnpdThresholdHistoryIndex_Type())
cnpdThresholdHistoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cnpdThresholdHistoryIndex.setStatus(_A)
class _CnpdThresholdHistoryConfigIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CnpdThresholdHistoryConfigIndex_Type.__name__=_D
_CnpdThresholdHistoryConfigIndex_Object=MibTableColumn
cnpdThresholdHistoryConfigIndex=_CnpdThresholdHistoryConfigIndex_Object((1,3,6,1,4,1,9,9,244,1,6,1,1,2),_CnpdThresholdHistoryConfigIndex_Type())
cnpdThresholdHistoryConfigIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdThresholdHistoryConfigIndex.setStatus(_A)
class _CnpdThresholdHistoryValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CnpdThresholdHistoryValue_Type.__name__=_D
_CnpdThresholdHistoryValue_Object=MibTableColumn
cnpdThresholdHistoryValue=_CnpdThresholdHistoryValue_Object((1,3,6,1,4,1,9,9,244,1,6,1,1,3),_CnpdThresholdHistoryValue_Type())
cnpdThresholdHistoryValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdThresholdHistoryValue.setStatus(_A)
class _CnpdThresholdHistoryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('risingBreach',1),('fallingBreach',2)))
_CnpdThresholdHistoryType_Type.__name__=_H
_CnpdThresholdHistoryType_Object=MibTableColumn
cnpdThresholdHistoryType=_CnpdThresholdHistoryType_Object((1,3,6,1,4,1,9,9,244,1,6,1,1,4),_CnpdThresholdHistoryType_Type())
cnpdThresholdHistoryType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdThresholdHistoryType.setStatus(_A)
_CnpdThresholdHistoryTime_Type=TimeTicks
_CnpdThresholdHistoryTime_Object=MibTableColumn
cnpdThresholdHistoryTime=_CnpdThresholdHistoryTime_Object((1,3,6,1,4,1,9,9,244,1,6,1,1,5),_CnpdThresholdHistoryTime_Type())
cnpdThresholdHistoryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdThresholdHistoryTime.setStatus(_A)
class _CnpdThresholdHistoryProtocol_Type(CiscoPdProtocolIndex):subtypeSpec=CiscoPdProtocolIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CnpdThresholdHistoryProtocol_Type.__name__=_G
_CnpdThresholdHistoryProtocol_Object=MibTableColumn
cnpdThresholdHistoryProtocol=_CnpdThresholdHistoryProtocol_Object((1,3,6,1,4,1,9,9,244,1,6,1,1,6),_CnpdThresholdHistoryProtocol_Type())
cnpdThresholdHistoryProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdThresholdHistoryProtocol.setStatus(_A)
_CnpdThresholdHistoryStatsSelect_Type=CiscoPdDataType
_CnpdThresholdHistoryStatsSelect_Object=MibTableColumn
cnpdThresholdHistoryStatsSelect=_CnpdThresholdHistoryStatsSelect_Object((1,3,6,1,4,1,9,9,244,1,6,1,1,7),_CnpdThresholdHistoryStatsSelect_Type())
cnpdThresholdHistoryStatsSelect.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdThresholdHistoryStatsSelect.setStatus(_A)
_CnpdNotificationsConfig_ObjectIdentity=ObjectIdentity
cnpdNotificationsConfig=_CnpdNotificationsConfig_ObjectIdentity((1,3,6,1,4,1,9,9,244,1,7))
class _CnpdNotificationsEnable_Type(TruthValue):defaultValue=2
_CnpdNotificationsEnable_Type.__name__=_R
_CnpdNotificationsEnable_Object=MibScalar
cnpdNotificationsEnable=_CnpdNotificationsEnable_Object((1,3,6,1,4,1,9,9,244,1,7,1),_CnpdNotificationsEnable_Type())
cnpdNotificationsEnable.setMaxAccess(_W)
if mibBuilder.loadTexts:cnpdNotificationsEnable.setStatus(_A)
_CnpdSupportedProtocols_ObjectIdentity=ObjectIdentity
cnpdSupportedProtocols=_CnpdSupportedProtocols_ObjectIdentity((1,3,6,1,4,1,9,9,244,1,8))
_CnpdSupportedProtocolsTable_Object=MibTable
cnpdSupportedProtocolsTable=_CnpdSupportedProtocolsTable_Object((1,3,6,1,4,1,9,9,244,1,8,1))
if mibBuilder.loadTexts:cnpdSupportedProtocolsTable.setStatus(_A)
_CnpdSupportedProtocolsEntry_Object=MibTableRow
cnpdSupportedProtocolsEntry=_CnpdSupportedProtocolsEntry_Object((1,3,6,1,4,1,9,9,244,1,8,1,1))
cnpdSupportedProtocolsEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:cnpdSupportedProtocolsEntry.setStatus(_A)
class _CnpdSupportedProtocolsIndex_Type(CiscoPdProtocolIndex):subtypeSpec=CiscoPdProtocolIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CnpdSupportedProtocolsIndex_Type.__name__=_G
_CnpdSupportedProtocolsIndex_Object=MibTableColumn
cnpdSupportedProtocolsIndex=_CnpdSupportedProtocolsIndex_Object((1,3,6,1,4,1,9,9,244,1,8,1,1,1),_CnpdSupportedProtocolsIndex_Type())
cnpdSupportedProtocolsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cnpdSupportedProtocolsIndex.setStatus(_A)
_CnpdSupportedProtocolsName_Type=CiscoPdProtocolName
_CnpdSupportedProtocolsName_Object=MibTableColumn
cnpdSupportedProtocolsName=_CnpdSupportedProtocolsName_Object((1,3,6,1,4,1,9,9,244,1,8,1,1,2),_CnpdSupportedProtocolsName_Type())
cnpdSupportedProtocolsName.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpdSupportedProtocolsName.setStatus(_A)
_CnpdMIBConformance_ObjectIdentity=ObjectIdentity
cnpdMIBConformance=_CnpdMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,244,2))
_CnpdMIBCompliances_ObjectIdentity=ObjectIdentity
cnpdMIBCompliances=_CnpdMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,244,2,1))
_CnpdMIBGroups_ObjectIdentity=ObjectIdentity
cnpdMIBGroups=_CnpdMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,244,2,2))
cnpdStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,244,2,2,1))
cnpdStatsGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:cnpdStatsGroup.setStatus(_A)
cnpdTopNGroup=ObjectGroup((1,3,6,1,4,1,9,9,244,2,2,2))
cnpdTopNGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:cnpdTopNGroup.setStatus(_A)
cnpdThresholdGroup=ObjectGroup((1,3,6,1,4,1,9,9,244,2,2,3))
cnpdThresholdGroup.setObjects(*((_B,_K),(_B,_A1),(_B,_A2),(_B,_L),(_B,_M),(_B,_A3),(_B,_A4),(_B,_U),(_B,_V),(_B,_A5),(_B,_A6),(_B,_N),(_B,_A7),(_B,_O),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:cnpdThresholdGroup.setStatus(_A)
cnpdMIBNotificationsConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,244,2,2,5))
cnpdMIBNotificationsConfigGroup.setObjects((_B,_AA))
if mibBuilder.loadTexts:cnpdMIBNotificationsConfigGroup.setStatus(_A)
cnpdSupportedProtocolsGroup=ObjectGroup((1,3,6,1,4,1,9,9,244,2,2,6))
cnpdSupportedProtocolsGroup.setObjects((_B,_AB))
if mibBuilder.loadTexts:cnpdSupportedProtocolsGroup.setStatus(_A)
cnpdThresholdRisingEvent=NotificationType((1,3,6,1,4,1,9,9,244,0,1))
cnpdThresholdRisingEvent.setObjects(*((_B,_K),(_B,_M),(_B,_N),(_B,_U),(_B,_L),(_B,_O)))
if mibBuilder.loadTexts:cnpdThresholdRisingEvent.setStatus(_A)
cnpdThresholdFallingEvent=NotificationType((1,3,6,1,4,1,9,9,244,0,2))
cnpdThresholdFallingEvent.setObjects(*((_B,_K),(_B,_M),(_B,_N),(_B,_V),(_B,_L),(_B,_O)))
if mibBuilder.loadTexts:cnpdThresholdFallingEvent.setStatus(_A)
cnpdMIBNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,244,2,2,4))
cnpdMIBNotificationsGroup.setObjects(*((_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:cnpdMIBNotificationsGroup.setStatus(_A)
cnpdMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,244,2,1,1))
cnpdMIBCompliance.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:cnpdMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_G:CiscoPdProtocolIndex,'CiscoPdProtocolName':CiscoPdProtocolName,_T:CiscoPdDataType,'ciscoNbarProtocolDiscoveryMIB':ciscoNbarProtocolDiscoveryMIB,'cnpdMIBNotifications':cnpdMIBNotifications,_AC:cnpdThresholdRisingEvent,_AD:cnpdThresholdFallingEvent,'cnpdMIBObjects':cnpdMIBObjects,'cnpdStatus':cnpdStatus,'cnpdStatusTable':cnpdStatusTable,'cnpdStatusEntry':cnpdStatusEntry,_e:cnpdStatusPdEnable,_f:cnpdStatusLastUpdateTime,'cnpdAllStats':cnpdAllStats,'cnpdAllStatsTable':cnpdAllStatsTable,'cnpdAllStatsEntry':cnpdAllStatsEntry,_X:cnpdAllStatsProtocolsIndex,_g:cnpdAllStatsProtocolName,_h:cnpdAllStatsInPkts,_i:cnpdAllStatsOutPkts,_j:cnpdAllStatsInBytes,_k:cnpdAllStatsOutBytes,_l:cnpdAllStatsHCInPkts,_m:cnpdAllStatsHCOutPkts,_n:cnpdAllStatsHCInBytes,_o:cnpdAllStatsHCOutBytes,_p:cnpdAllStatsInBitRate,_q:cnpdAllStatsOutBitRate,'cnpdTopNConfig':cnpdTopNConfig,'cnpdTopNConfigTable':cnpdTopNConfigTable,'cnpdTopNConfigEntry':cnpdTopNConfigEntry,_S:cnpdTopNConfigIndex,_r:cnpdTopNConfigIfIndex,_s:cnpdTopNConfigStatsSelect,_u:cnpdTopNConfigSampleTime,_t:cnpdTopNConfigRequestedSize,_v:cnpdTopNConfigGrantedSize,_w:cnpdTopNConfigTime,_x:cnpdTopNConfigStatus,'cnpdTopNStats':cnpdTopNStats,'cnpdTopNStatsTable':cnpdTopNStatsTable,'cnpdTopNStatsEntry':cnpdTopNStatsEntry,_a:cnpdTopNStatsIndex,_y:cnpdTopNStatsProtocolName,_z:cnpdTopNStatsRate,_A0:cnpdTopNStatsHCRate,'cnpdThresholdConfig':cnpdThresholdConfig,'cnpdThresholdConfigTable':cnpdThresholdConfigTable,'cnpdThresholdConfigEntry':cnpdThresholdConfigEntry,_b:cnpdThresholdConfigIndex,_K:cnpdThresholdConfigIfIndex,_A1:cnpdThresholdConfigInterval,_A2:cnpdThresholdConfigSampleType,_L:cnpdThresholdConfigProtocol,_A3:cnpdThresholdConfigProtocolAny,_M:cnpdThresholdConfigStatsSelect,_A4:cnpdThresholdConfigStartup,_U:cnpdThresholdConfigRising,_V:cnpdThresholdConfigFalling,_A5:cnpdThresholdConfigStatus,'cnpdThresholdHistory':cnpdThresholdHistory,'cnpdThresholdHistoryTable':cnpdThresholdHistoryTable,'cnpdThresholdHistoryEntry':cnpdThresholdHistoryEntry,_c:cnpdThresholdHistoryIndex,_A6:cnpdThresholdHistoryConfigIndex,_N:cnpdThresholdHistoryValue,_A7:cnpdThresholdHistoryType,_O:cnpdThresholdHistoryTime,_A8:cnpdThresholdHistoryProtocol,_A9:cnpdThresholdHistoryStatsSelect,'cnpdNotificationsConfig':cnpdNotificationsConfig,_AA:cnpdNotificationsEnable,'cnpdSupportedProtocols':cnpdSupportedProtocols,'cnpdSupportedProtocolsTable':cnpdSupportedProtocolsTable,'cnpdSupportedProtocolsEntry':cnpdSupportedProtocolsEntry,_d:cnpdSupportedProtocolsIndex,_AB:cnpdSupportedProtocolsName,'cnpdMIBConformance':cnpdMIBConformance,'cnpdMIBCompliances':cnpdMIBCompliances,'cnpdMIBCompliance':cnpdMIBCompliance,'cnpdMIBGroups':cnpdMIBGroups,_AE:cnpdStatsGroup,_AF:cnpdTopNGroup,_AG:cnpdThresholdGroup,_AH:cnpdMIBNotificationsGroup,_AI:cnpdMIBNotificationsConfigGroup,_AJ:cnpdSupportedProtocolsGroup})