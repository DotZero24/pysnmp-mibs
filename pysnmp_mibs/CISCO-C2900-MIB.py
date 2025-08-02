_Ax='c2900PortStatsGroupRev1'
_Aw='c2900NotificationsGroup'
_Av='c2900PortGroupWC4'
_Au='c2900PortGroupWC2'
_At='c2900PortGroupSA7'
_As='c2900PortStatsGroupSA3'
_Ar='c2900PortGroupSA3'
_Aq='c2900PortGroupSA5'
_Ap='c2900PortGroup'
_Ao='c2900SysConfigGroup'
_An='c2900RpsFailed'
_Am='c2900BroadcastStorm'
_Al='c2900AddressViolation'
_Ak='c2900PortAddrSecureAgingStatic'
_Aj='c2900PortAddrSecureAgingType'
_Ai='c2900PortAddrSecureAgingTime'
_Ah='c2900BandwidthUsageCurrentPeakEntry'
_Ag='c2900BandwidthUsagePeakTime'
_Af='c2900BandwidthUsagePeak'
_Ae='c2900BandwidthUsageStartTime'
_Ad='c2900BandwidthUsagePeakRestart'
_Ac='c2900BandwidthUsagePeakInterval'
_Ab='c2900BandwidthUsageMaxPeakEntries'
_Aa='c2900BandwidthUsageCurrent'
_AZ='c2900PortRxSuppressBcastFrames'
_AY='c2900PortBufferCongestionControl'
_AX='c2900ModuleSwVersion'
_AW='c2900ModuleHwVersion'
_AV='c2900ModuleType'
_AU='c2900ModuleStatus'
_AT='c2900ConfigBroadcastStormAlarm'
_AS='c2900ConfigAddressViolationAction'
_AR='c2900InfoBoardIdentifier'
_AQ='c2900InfoRedunantPowerSupplyInfo'
_AP='c2900InfoVisualIndicatorMode'
_AO='c2900InfoUtilDisplay'
_AN='c2900InfoSelfTestFailed'
_AM='c2900InfoRestrictedStaticAddrCapacity'
_AL='c2900InfoAddrCapacity'
_AK='c2900InfoTotalBufferDepth'
_AJ='c2900InfoPeakBuffersUsed'
_AI='c2900InfoBoardRevision'
_AH='megabits per second'
_AG='halfduplex'
_AF='fullduplex'
_AE='c2900ModuleIndex'
_AD='disablePortAndNotify'
_AC='sendNotify'
_AB='doNothing'
_AA='SNMPv2-MIB'
_A9='InterfaceIndex'
_A8='c2900PortVoiceVlanId'
_A7='c2900PortMayLearnAddress'
_A6='c2900BandwidthUsagePeakIndex'
_A5='c2900PortIndex'
_A4='c2900PortModuleIndex'
_A3='not-accessible'
_A2='disablePort'
_A1='DisplayString'
_A0='Gauge32'
_z='OctetString'
_y='c2900PortSpantreeFastStart'
_x='c2900PortTxBroadcastFrames'
_w='c2900PortTxMulticastFrames'
_v='c2900PortCollFragFrames'
_u='c2900PortRxFcsErrFrames'
_t='c2900PortRxNoDestMultiFrames'
_s='c2900PortRxNoDestUniFrames'
_r='c2900PortRxNoBufferFrames'
_q='c2900PortRxNoBwFrames'
_p='c2900Portdot1dBasePort'
_o='c2900ModuleGroup'
_n='TruthValue'
_m='c2900BandwidthUsageGroup'
_l='c2900SysInfoGroup'
_k='c2900PortNoMonitorDestinationPort'
_j='c2900PortAdminSpeed'
_i='c2900PortDuplexStatus'
_h='c2900PortDuplexState'
_g='c2900PortMonitoredPortMap'
_f='c2900PortSwitchPortIndex'
_e='c2900PortMonitorDestinationPort'
_d='c2900PortBroadcastStormAlarm'
_c='c2900PortAddressViolationAction'
_b='c2900PortVisualIndicator'
_a='c2900PortTestResult'
_Z='c2900PortStatus'
_Y='c2900PortBroadcastFallingThreshold'
_X='c2900PortBroadcastStormAction'
_W='c2900PortLinkbeatStatus'
_V='c2900PortFloodUnknownUnicasts'
_U='c2900PortFloodUnknownMulticasts'
_T='c2900PortClearAddresses'
_S='c2900PortNumberOfDroppedAddresses'
_R='c2900PortNumberOfLearnedAddresses'
_Q='c2900PortAddrSecureAddrViolations'
_P='c2900PortAddrSecureCurrentAddresses'
_O='c2900PortAddrSecureMaxAddresses'
_N='c2900PortFrameAge'
_M='c2900PortBufferCongestionThreshholdPercent'
_L='c2900PortMayForwardFrames'
_K='c2900PortGroupIndex'
_J='c2900PortUsageApplication'
_I='c2900PortIfIndex'
_H='c2900PortBroadcastRisingThreshold'
_G='frames'
_F='deprecated'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-C2900-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_z,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB',_A9)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_AA,'sysName')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_A0,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_A1,'PhysAddress','TextualConvention',_n)
ciscoC2900MIB=ModuleIdentity((1,3,6,1,4,1,9,9,87))
if mibBuilder.loadTexts:ciscoC2900MIB.setRevisions(('2002-05-30 00:00','2001-07-25 13:45','1999-09-24 00:00','1999-08-24 00:00','1999-05-20 00:00','1998-06-08 00:00','1998-04-30 00:00'))
_C2900MIBObjects_ObjectIdentity=ObjectIdentity
c2900MIBObjects=_C2900MIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,87,1))
_C2900SysInfo_ObjectIdentity=ObjectIdentity
c2900SysInfo=_C2900SysInfo_ObjectIdentity((1,3,6,1,4,1,9,9,87,1,1))
_C2900InfoBoardRevision_Type=Gauge32
_C2900InfoBoardRevision_Object=MibScalar
c2900InfoBoardRevision=_C2900InfoBoardRevision_Object((1,3,6,1,4,1,9,9,87,1,1,1),_C2900InfoBoardRevision_Type())
c2900InfoBoardRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900InfoBoardRevision.setStatus(_B)
_C2900InfoPeakBuffersUsed_Type=Gauge32
_C2900InfoPeakBuffersUsed_Object=MibScalar
c2900InfoPeakBuffersUsed=_C2900InfoPeakBuffersUsed_Object((1,3,6,1,4,1,9,9,87,1,1,2),_C2900InfoPeakBuffersUsed_Type())
c2900InfoPeakBuffersUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900InfoPeakBuffersUsed.setStatus(_B)
if mibBuilder.loadTexts:c2900InfoPeakBuffersUsed.setUnits('buffers')
_C2900InfoTotalBufferDepth_Type=Gauge32
_C2900InfoTotalBufferDepth_Object=MibScalar
c2900InfoTotalBufferDepth=_C2900InfoTotalBufferDepth_Object((1,3,6,1,4,1,9,9,87,1,1,3),_C2900InfoTotalBufferDepth_Type())
c2900InfoTotalBufferDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900InfoTotalBufferDepth.setStatus(_B)
if mibBuilder.loadTexts:c2900InfoTotalBufferDepth.setUnits('buffers')
_C2900InfoAddrCapacity_Type=Gauge32
_C2900InfoAddrCapacity_Object=MibScalar
c2900InfoAddrCapacity=_C2900InfoAddrCapacity_Object((1,3,6,1,4,1,9,9,87,1,1,4),_C2900InfoAddrCapacity_Type())
c2900InfoAddrCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900InfoAddrCapacity.setStatus(_B)
_C2900InfoRestrictedStaticAddrCapacity_Type=Gauge32
_C2900InfoRestrictedStaticAddrCapacity_Object=MibScalar
c2900InfoRestrictedStaticAddrCapacity=_C2900InfoRestrictedStaticAddrCapacity_Object((1,3,6,1,4,1,9,9,87,1,1,5),_C2900InfoRestrictedStaticAddrCapacity_Type())
c2900InfoRestrictedStaticAddrCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900InfoRestrictedStaticAddrCapacity.setStatus(_B)
class _C2900InfoSelfTestFailed_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_C2900InfoSelfTestFailed_Type.__name__=_z
_C2900InfoSelfTestFailed_Object=MibScalar
c2900InfoSelfTestFailed=_C2900InfoSelfTestFailed_Object((1,3,6,1,4,1,9,9,87,1,1,6),_C2900InfoSelfTestFailed_Type())
c2900InfoSelfTestFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900InfoSelfTestFailed.setStatus(_B)
_C2900InfoUtilDisplay_Type=Gauge32
_C2900InfoUtilDisplay_Object=MibScalar
c2900InfoUtilDisplay=_C2900InfoUtilDisplay_Object((1,3,6,1,4,1,9,9,87,1,1,7),_C2900InfoUtilDisplay_Type())
c2900InfoUtilDisplay.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900InfoUtilDisplay.setStatus(_B)
class _C2900InfoVisualIndicatorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('portStatus',1),('fullDuplex',2),('linkRate',3),('utilization',4)))
_C2900InfoVisualIndicatorMode_Type.__name__=_D
_C2900InfoVisualIndicatorMode_Object=MibScalar
c2900InfoVisualIndicatorMode=_C2900InfoVisualIndicatorMode_Object((1,3,6,1,4,1,9,9,87,1,1,8),_C2900InfoVisualIndicatorMode_Type())
c2900InfoVisualIndicatorMode.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900InfoVisualIndicatorMode.setStatus(_B)
class _C2900InfoRedunantPowerSupplyInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('absent',1),('connectedFunctional',2),('connectedNotFunctional',3),('functionalPrimaryFailed',4)))
_C2900InfoRedunantPowerSupplyInfo_Type.__name__=_D
_C2900InfoRedunantPowerSupplyInfo_Object=MibScalar
c2900InfoRedunantPowerSupplyInfo=_C2900InfoRedunantPowerSupplyInfo_Object((1,3,6,1,4,1,9,9,87,1,1,9),_C2900InfoRedunantPowerSupplyInfo_Type())
c2900InfoRedunantPowerSupplyInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900InfoRedunantPowerSupplyInfo.setStatus(_B)
_C2900InfoBoardIdentifier_Type=Gauge32
_C2900InfoBoardIdentifier_Object=MibScalar
c2900InfoBoardIdentifier=_C2900InfoBoardIdentifier_Object((1,3,6,1,4,1,9,9,87,1,1,10),_C2900InfoBoardIdentifier_Type())
c2900InfoBoardIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900InfoBoardIdentifier.setStatus(_B)
_C2900SysConfig_ObjectIdentity=ObjectIdentity
c2900SysConfig=_C2900SysConfig_ObjectIdentity((1,3,6,1,4,1,9,9,87,1,2))
class _C2900ConfigAddressViolationAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_AB,1),(_A2,2),(_AC,3),(_AD,4)))
_C2900ConfigAddressViolationAction_Type.__name__=_D
_C2900ConfigAddressViolationAction_Object=MibScalar
c2900ConfigAddressViolationAction=_C2900ConfigAddressViolationAction_Object((1,3,6,1,4,1,9,9,87,1,2,1),_C2900ConfigAddressViolationAction_Type())
c2900ConfigAddressViolationAction.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900ConfigAddressViolationAction.setStatus(_F)
_C2900ConfigBroadcastStormAlarm_Type=TruthValue
_C2900ConfigBroadcastStormAlarm_Object=MibScalar
c2900ConfigBroadcastStormAlarm=_C2900ConfigBroadcastStormAlarm_Object((1,3,6,1,4,1,9,9,87,1,2,2),_C2900ConfigBroadcastStormAlarm_Type())
c2900ConfigBroadcastStormAlarm.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900ConfigBroadcastStormAlarm.setStatus(_F)
_C2900ModuleTable_Object=MibTable
c2900ModuleTable=_C2900ModuleTable_Object((1,3,6,1,4,1,9,9,87,1,3))
if mibBuilder.loadTexts:c2900ModuleTable.setStatus(_B)
_C2900ModuleEntry_Object=MibTableRow
c2900ModuleEntry=_C2900ModuleEntry_Object((1,3,6,1,4,1,9,9,87,1,3,1))
c2900ModuleEntry.setIndexNames((0,_A,_AE))
if mibBuilder.loadTexts:c2900ModuleEntry.setStatus(_B)
class _C2900ModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_C2900ModuleIndex_Type.__name__=_D
_C2900ModuleIndex_Object=MibTableColumn
c2900ModuleIndex=_C2900ModuleIndex_Object((1,3,6,1,4,1,9,9,87,1,3,1,1),_C2900ModuleIndex_Type())
c2900ModuleIndex.setMaxAccess(_A3)
if mibBuilder.loadTexts:c2900ModuleIndex.setStatus(_B)
class _C2900ModuleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('moduleNotInstalled',1),('moduleInTest',2),('moduleHealthy',3),('moduleFaulty',4)))
_C2900ModuleStatus_Type.__name__=_D
_C2900ModuleStatus_Object=MibTableColumn
c2900ModuleStatus=_C2900ModuleStatus_Object((1,3,6,1,4,1,9,9,87,1,3,1,2),_C2900ModuleStatus_Type())
c2900ModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900ModuleStatus.setStatus(_B)
class _C2900ModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('other',1),('empty',2),('wsx2914xl',3),('wsx2922xl',4),('atm155SMLRFiber',5),('atm155SMMRFiber',6),('atm155MMFiber',7),('atm155UTP',8),('wsx2914xlv',9),('wsx2922xlv',10),('wsx2924xlv',11),('wsx2931xl',12),('wsx2932xl',13)))
_C2900ModuleType_Type.__name__=_D
_C2900ModuleType_Object=MibTableColumn
c2900ModuleType=_C2900ModuleType_Object((1,3,6,1,4,1,9,9,87,1,3,1,3),_C2900ModuleType_Type())
c2900ModuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900ModuleType.setStatus(_B)
class _C2900ModuleHwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_C2900ModuleHwVersion_Type.__name__=_A1
_C2900ModuleHwVersion_Object=MibTableColumn
c2900ModuleHwVersion=_C2900ModuleHwVersion_Object((1,3,6,1,4,1,9,9,87,1,3,1,4),_C2900ModuleHwVersion_Type())
c2900ModuleHwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900ModuleHwVersion.setStatus(_B)
class _C2900ModuleSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_C2900ModuleSwVersion_Type.__name__=_A1
_C2900ModuleSwVersion_Object=MibTableColumn
c2900ModuleSwVersion=_C2900ModuleSwVersion_Object((1,3,6,1,4,1,9,9,87,1,3,1,5),_C2900ModuleSwVersion_Type())
c2900ModuleSwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900ModuleSwVersion.setStatus(_B)
_C2900Port_ObjectIdentity=ObjectIdentity
c2900Port=_C2900Port_ObjectIdentity((1,3,6,1,4,1,9,9,87,1,4))
_C2900PortTable_Object=MibTable
c2900PortTable=_C2900PortTable_Object((1,3,6,1,4,1,9,9,87,1,4,1))
if mibBuilder.loadTexts:c2900PortTable.setStatus(_B)
_C2900PortEntry_Object=MibTableRow
c2900PortEntry=_C2900PortEntry_Object((1,3,6,1,4,1,9,9,87,1,4,1,1))
c2900PortEntry.setIndexNames((0,_A,_A4),(0,_A,_A5))
if mibBuilder.loadTexts:c2900PortEntry.setStatus(_B)
class _C2900PortModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_C2900PortModuleIndex_Type.__name__=_D
_C2900PortModuleIndex_Object=MibTableColumn
c2900PortModuleIndex=_C2900PortModuleIndex_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,1),_C2900PortModuleIndex_Type())
c2900PortModuleIndex.setMaxAccess(_A3)
if mibBuilder.loadTexts:c2900PortModuleIndex.setStatus(_B)
class _C2900PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_C2900PortIndex_Type.__name__=_D
_C2900PortIndex_Object=MibTableColumn
c2900PortIndex=_C2900PortIndex_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,2),_C2900PortIndex_Type())
c2900PortIndex.setMaxAccess(_A3)
if mibBuilder.loadTexts:c2900PortIndex.setStatus(_B)
class _C2900PortUsageApplication_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('standard',1),('security',2),('monitor',3),('portGrouping',4),('network',5),('networkGroup',6),('portGroupDest',7),('protected',8)))
_C2900PortUsageApplication_Type.__name__=_D
_C2900PortUsageApplication_Object=MibTableColumn
c2900PortUsageApplication=_C2900PortUsageApplication_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,3),_C2900PortUsageApplication_Type())
c2900PortUsageApplication.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortUsageApplication.setStatus(_B)
class _C2900PortGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_C2900PortGroupIndex_Type.__name__=_D
_C2900PortGroupIndex_Object=MibTableColumn
c2900PortGroupIndex=_C2900PortGroupIndex_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,4),_C2900PortGroupIndex_Type())
c2900PortGroupIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortGroupIndex.setStatus(_B)
class _C2900PortMayLearnAddress_Type(TruthValue):defaultValue=1
_C2900PortMayLearnAddress_Type.__name__=_n
_C2900PortMayLearnAddress_Object=MibTableColumn
c2900PortMayLearnAddress=_C2900PortMayLearnAddress_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,5),_C2900PortMayLearnAddress_Type())
c2900PortMayLearnAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortMayLearnAddress.setStatus(_F)
class _C2900PortMayForwardFrames_Type(TruthValue):defaultValue=1
_C2900PortMayForwardFrames_Type.__name__=_n
_C2900PortMayForwardFrames_Object=MibTableColumn
c2900PortMayForwardFrames=_C2900PortMayForwardFrames_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,6),_C2900PortMayForwardFrames_Type())
c2900PortMayForwardFrames.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortMayForwardFrames.setStatus(_B)
_C2900PortBufferCongestionControl_Type=TruthValue
_C2900PortBufferCongestionControl_Object=MibTableColumn
c2900PortBufferCongestionControl=_C2900PortBufferCongestionControl_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,7),_C2900PortBufferCongestionControl_Type())
c2900PortBufferCongestionControl.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortBufferCongestionControl.setStatus(_F)
class _C2900PortBufferCongestionThreshholdPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_C2900PortBufferCongestionThreshholdPercent_Type.__name__=_D
_C2900PortBufferCongestionThreshholdPercent_Object=MibTableColumn
c2900PortBufferCongestionThreshholdPercent=_C2900PortBufferCongestionThreshholdPercent_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,8),_C2900PortBufferCongestionThreshholdPercent_Type())
c2900PortBufferCongestionThreshholdPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortBufferCongestionThreshholdPercent.setStatus(_B)
class _C2900PortFrameAge_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,4000))
_C2900PortFrameAge_Type.__name__=_D
_C2900PortFrameAge_Object=MibTableColumn
c2900PortFrameAge=_C2900PortFrameAge_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,9),_C2900PortFrameAge_Type())
c2900PortFrameAge.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortFrameAge.setStatus(_B)
if mibBuilder.loadTexts:c2900PortFrameAge.setUnits('milliseconds')
class _C2900PortAddrSecureMaxAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,132))
_C2900PortAddrSecureMaxAddresses_Type.__name__=_D
_C2900PortAddrSecureMaxAddresses_Object=MibTableColumn
c2900PortAddrSecureMaxAddresses=_C2900PortAddrSecureMaxAddresses_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,10),_C2900PortAddrSecureMaxAddresses_Type())
c2900PortAddrSecureMaxAddresses.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortAddrSecureMaxAddresses.setStatus(_B)
_C2900PortAddrSecureCurrentAddresses_Type=Gauge32
_C2900PortAddrSecureCurrentAddresses_Object=MibTableColumn
c2900PortAddrSecureCurrentAddresses=_C2900PortAddrSecureCurrentAddresses_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,11),_C2900PortAddrSecureCurrentAddresses_Type())
c2900PortAddrSecureCurrentAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortAddrSecureCurrentAddresses.setStatus(_B)
_C2900PortAddrSecureAddrViolations_Type=Counter32
_C2900PortAddrSecureAddrViolations_Object=MibTableColumn
c2900PortAddrSecureAddrViolations=_C2900PortAddrSecureAddrViolations_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,12),_C2900PortAddrSecureAddrViolations_Type())
c2900PortAddrSecureAddrViolations.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortAddrSecureAddrViolations.setStatus(_B)
_C2900PortNumberOfLearnedAddresses_Type=Counter32
_C2900PortNumberOfLearnedAddresses_Object=MibTableColumn
c2900PortNumberOfLearnedAddresses=_C2900PortNumberOfLearnedAddresses_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,13),_C2900PortNumberOfLearnedAddresses_Type())
c2900PortNumberOfLearnedAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortNumberOfLearnedAddresses.setStatus(_B)
_C2900PortNumberOfDroppedAddresses_Type=Counter32
_C2900PortNumberOfDroppedAddresses_Object=MibTableColumn
c2900PortNumberOfDroppedAddresses=_C2900PortNumberOfDroppedAddresses_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,14),_C2900PortNumberOfDroppedAddresses_Type())
c2900PortNumberOfDroppedAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortNumberOfDroppedAddresses.setStatus(_B)
_C2900PortClearAddresses_Type=TruthValue
_C2900PortClearAddresses_Object=MibTableColumn
c2900PortClearAddresses=_C2900PortClearAddresses_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,15),_C2900PortClearAddresses_Type())
c2900PortClearAddresses.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortClearAddresses.setStatus(_B)
class _C2900PortFloodUnknownMulticasts_Type(TruthValue):defaultValue=1
_C2900PortFloodUnknownMulticasts_Type.__name__=_n
_C2900PortFloodUnknownMulticasts_Object=MibTableColumn
c2900PortFloodUnknownMulticasts=_C2900PortFloodUnknownMulticasts_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,16),_C2900PortFloodUnknownMulticasts_Type())
c2900PortFloodUnknownMulticasts.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortFloodUnknownMulticasts.setStatus(_B)
_C2900PortFloodUnknownUnicasts_Type=TruthValue
_C2900PortFloodUnknownUnicasts_Object=MibTableColumn
c2900PortFloodUnknownUnicasts=_C2900PortFloodUnknownUnicasts_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,17),_C2900PortFloodUnknownUnicasts_Type())
c2900PortFloodUnknownUnicasts.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortFloodUnknownUnicasts.setStatus(_B)
class _C2900PortLinkbeatStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('linkbeat',2),('nolinkbeat',3)))
_C2900PortLinkbeatStatus_Type.__name__=_D
_C2900PortLinkbeatStatus_Object=MibTableColumn
c2900PortLinkbeatStatus=_C2900PortLinkbeatStatus_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,18),_C2900PortLinkbeatStatus_Type())
c2900PortLinkbeatStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortLinkbeatStatus.setStatus(_B)
class _C2900PortBroadcastStormAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stopBroadcastForwarding',1),('forwardBroadcast',2),(_A2,3)))
_C2900PortBroadcastStormAction_Type.__name__=_D
_C2900PortBroadcastStormAction_Object=MibTableColumn
c2900PortBroadcastStormAction=_C2900PortBroadcastStormAction_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,19),_C2900PortBroadcastStormAction_Type())
c2900PortBroadcastStormAction.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortBroadcastStormAction.setStatus(_B)
class _C2900PortBroadcastRisingThreshold_Type(Gauge32):defaultValue=500
_C2900PortBroadcastRisingThreshold_Type.__name__=_A0
_C2900PortBroadcastRisingThreshold_Object=MibTableColumn
c2900PortBroadcastRisingThreshold=_C2900PortBroadcastRisingThreshold_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,20),_C2900PortBroadcastRisingThreshold_Type())
c2900PortBroadcastRisingThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortBroadcastRisingThreshold.setStatus(_B)
class _C2900PortBroadcastFallingThreshold_Type(Gauge32):defaultValue=250
_C2900PortBroadcastFallingThreshold_Type.__name__=_A0
_C2900PortBroadcastFallingThreshold_Object=MibTableColumn
c2900PortBroadcastFallingThreshold=_C2900PortBroadcastFallingThreshold_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,21),_C2900PortBroadcastFallingThreshold_Type())
c2900PortBroadcastFallingThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortBroadcastFallingThreshold.setStatus(_B)
class _C2900PortStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('other',1),('disabled',2),('blocking',3),('listening',4),('learning',5),('preforwarding',6),('forwarding',7),('secureforwarding',8),('suspended',9),('broken',10)))
_C2900PortStatus_Type.__name__=_D
_C2900PortStatus_Object=MibTableColumn
c2900PortStatus=_C2900PortStatus_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,22),_C2900PortStatus_Type())
c2900PortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortStatus.setStatus(_B)
_C2900PortTestResult_Type=TruthValue
_C2900PortTestResult_Object=MibTableColumn
c2900PortTestResult=_C2900PortTestResult_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,23),_C2900PortTestResult_Type())
c2900PortTestResult.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortTestResult.setStatus(_B)
class _C2900PortVisualIndicator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notused',1),('black',2),('amber',3),('green',4)))
_C2900PortVisualIndicator_Type.__name__=_D
_C2900PortVisualIndicator_Object=MibTableColumn
c2900PortVisualIndicator=_C2900PortVisualIndicator_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,24),_C2900PortVisualIndicator_Type())
c2900PortVisualIndicator.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortVisualIndicator.setStatus(_B)
class _C2900PortIfIndex_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_C2900PortIfIndex_Type.__name__=_A9
_C2900PortIfIndex_Object=MibTableColumn
c2900PortIfIndex=_C2900PortIfIndex_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,25),_C2900PortIfIndex_Type())
c2900PortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortIfIndex.setStatus(_B)
class _C2900PortAddressViolationAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_AB,1),(_A2,2),(_AC,3),(_AD,4)))
_C2900PortAddressViolationAction_Type.__name__=_D
_C2900PortAddressViolationAction_Object=MibTableColumn
c2900PortAddressViolationAction=_C2900PortAddressViolationAction_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,26),_C2900PortAddressViolationAction_Type())
c2900PortAddressViolationAction.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortAddressViolationAction.setStatus(_B)
class _C2900PortBroadcastStormAlarm_Type(TruthValue):defaultValue=2
_C2900PortBroadcastStormAlarm_Type.__name__=_n
_C2900PortBroadcastStormAlarm_Object=MibTableColumn
c2900PortBroadcastStormAlarm=_C2900PortBroadcastStormAlarm_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,27),_C2900PortBroadcastStormAlarm_Type())
c2900PortBroadcastStormAlarm.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortBroadcastStormAlarm.setStatus(_B)
class _C2900PortMonitorDestinationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_C2900PortMonitorDestinationPort_Type.__name__=_D
_C2900PortMonitorDestinationPort_Object=MibTableColumn
c2900PortMonitorDestinationPort=_C2900PortMonitorDestinationPort_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,28),_C2900PortMonitorDestinationPort_Type())
c2900PortMonitorDestinationPort.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortMonitorDestinationPort.setStatus(_B)
class _C2900PortSwitchPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_C2900PortSwitchPortIndex_Type.__name__=_D
_C2900PortSwitchPortIndex_Object=MibTableColumn
c2900PortSwitchPortIndex=_C2900PortSwitchPortIndex_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,29),_C2900PortSwitchPortIndex_Type())
c2900PortSwitchPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortSwitchPortIndex.setStatus(_B)
class _C2900PortMonitoredPortMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_C2900PortMonitoredPortMap_Type.__name__=_z
_C2900PortMonitoredPortMap_Object=MibTableColumn
c2900PortMonitoredPortMap=_C2900PortMonitoredPortMap_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,30),_C2900PortMonitoredPortMap_Type())
c2900PortMonitoredPortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortMonitoredPortMap.setStatus(_B)
class _C2900PortDuplexState_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AF,1),(_AG,2),('autoNegotiate',3)))
_C2900PortDuplexState_Type.__name__=_D
_C2900PortDuplexState_Object=MibTableColumn
c2900PortDuplexState=_C2900PortDuplexState_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,31),_C2900PortDuplexState_Type())
c2900PortDuplexState.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortDuplexState.setStatus(_B)
class _C2900PortDuplexStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AF,1),(_AG,2)))
_C2900PortDuplexStatus_Type.__name__=_D
_C2900PortDuplexStatus_Object=MibTableColumn
c2900PortDuplexStatus=_C2900PortDuplexStatus_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,32),_C2900PortDuplexStatus_Type())
c2900PortDuplexStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortDuplexStatus.setStatus(_B)
class _C2900PortAdminSpeed_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10000000,100000000,155520000)));namedValues=NamedValues(*(('autoDetect',1),('s10000000',10000000),('s100000000',100000000),('s155520000',155520000)))
_C2900PortAdminSpeed_Type.__name__=_D
_C2900PortAdminSpeed_Object=MibTableColumn
c2900PortAdminSpeed=_C2900PortAdminSpeed_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,33),_C2900PortAdminSpeed_Type())
c2900PortAdminSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortAdminSpeed.setStatus(_B)
class _C2900PortNoMonitorDestinationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_C2900PortNoMonitorDestinationPort_Type.__name__=_D
_C2900PortNoMonitorDestinationPort_Object=MibTableColumn
c2900PortNoMonitorDestinationPort=_C2900PortNoMonitorDestinationPort_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,34),_C2900PortNoMonitorDestinationPort_Type())
c2900PortNoMonitorDestinationPort.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortNoMonitorDestinationPort.setStatus(_B)
class _C2900Portdot1dBasePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_C2900Portdot1dBasePort_Type.__name__=_D
_C2900Portdot1dBasePort_Object=MibTableColumn
c2900Portdot1dBasePort=_C2900Portdot1dBasePort_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,35),_C2900Portdot1dBasePort_Type())
c2900Portdot1dBasePort.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900Portdot1dBasePort.setStatus(_B)
class _C2900PortSpantreeFastStart_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_C2900PortSpantreeFastStart_Type.__name__=_D
_C2900PortSpantreeFastStart_Object=MibTableColumn
c2900PortSpantreeFastStart=_C2900PortSpantreeFastStart_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,36),_C2900PortSpantreeFastStart_Type())
c2900PortSpantreeFastStart.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortSpantreeFastStart.setStatus(_B)
class _C2900PortVoiceVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1000),ValueRangeConstraint(4095,4095),ValueRangeConstraint(4096,4096))
_C2900PortVoiceVlanId_Type.__name__=_D
_C2900PortVoiceVlanId_Object=MibTableColumn
c2900PortVoiceVlanId=_C2900PortVoiceVlanId_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,37),_C2900PortVoiceVlanId_Type())
c2900PortVoiceVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortVoiceVlanId.setStatus(_B)
class _C2900PortAddrSecureAgingTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_C2900PortAddrSecureAgingTime_Type.__name__=_D
_C2900PortAddrSecureAgingTime_Object=MibTableColumn
c2900PortAddrSecureAgingTime=_C2900PortAddrSecureAgingTime_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,38),_C2900PortAddrSecureAgingTime_Type())
c2900PortAddrSecureAgingTime.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortAddrSecureAgingTime.setStatus(_B)
if mibBuilder.loadTexts:c2900PortAddrSecureAgingTime.setUnits('minutes')
class _C2900PortAddrSecureAgingType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absolute',1),('inactivity',2)))
_C2900PortAddrSecureAgingType_Type.__name__=_D
_C2900PortAddrSecureAgingType_Object=MibTableColumn
c2900PortAddrSecureAgingType=_C2900PortAddrSecureAgingType_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,39),_C2900PortAddrSecureAgingType_Type())
c2900PortAddrSecureAgingType.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortAddrSecureAgingType.setStatus(_B)
class _C2900PortAddrSecureAgingStatic_Type(TruthValue):defaultValue=2
_C2900PortAddrSecureAgingStatic_Type.__name__=_n
_C2900PortAddrSecureAgingStatic_Object=MibTableColumn
c2900PortAddrSecureAgingStatic=_C2900PortAddrSecureAgingStatic_Object((1,3,6,1,4,1,9,9,87,1,4,1,1,40),_C2900PortAddrSecureAgingStatic_Type())
c2900PortAddrSecureAgingStatic.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900PortAddrSecureAgingStatic.setStatus(_B)
_C2900PortStatsTable_Object=MibTable
c2900PortStatsTable=_C2900PortStatsTable_Object((1,3,6,1,4,1,9,9,87,1,4,2))
if mibBuilder.loadTexts:c2900PortStatsTable.setStatus(_B)
_C2900PortStatsEntry_Object=MibTableRow
c2900PortStatsEntry=_C2900PortStatsEntry_Object((1,3,6,1,4,1,9,9,87,1,4,2,1))
c2900PortStatsEntry.setIndexNames((0,_A,_A4),(0,_A,_A5))
if mibBuilder.loadTexts:c2900PortStatsEntry.setStatus(_B)
_C2900PortRxNoBwFrames_Type=Counter32
_C2900PortRxNoBwFrames_Object=MibTableColumn
c2900PortRxNoBwFrames=_C2900PortRxNoBwFrames_Object((1,3,6,1,4,1,9,9,87,1,4,2,1,1),_C2900PortRxNoBwFrames_Type())
c2900PortRxNoBwFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortRxNoBwFrames.setStatus(_B)
if mibBuilder.loadTexts:c2900PortRxNoBwFrames.setUnits(_G)
_C2900PortRxNoBufferFrames_Type=Counter32
_C2900PortRxNoBufferFrames_Object=MibTableColumn
c2900PortRxNoBufferFrames=_C2900PortRxNoBufferFrames_Object((1,3,6,1,4,1,9,9,87,1,4,2,1,2),_C2900PortRxNoBufferFrames_Type())
c2900PortRxNoBufferFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortRxNoBufferFrames.setStatus(_B)
if mibBuilder.loadTexts:c2900PortRxNoBufferFrames.setUnits(_G)
_C2900PortRxNoDestUniFrames_Type=Counter32
_C2900PortRxNoDestUniFrames_Object=MibTableColumn
c2900PortRxNoDestUniFrames=_C2900PortRxNoDestUniFrames_Object((1,3,6,1,4,1,9,9,87,1,4,2,1,3),_C2900PortRxNoDestUniFrames_Type())
c2900PortRxNoDestUniFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortRxNoDestUniFrames.setStatus(_B)
if mibBuilder.loadTexts:c2900PortRxNoDestUniFrames.setUnits(_G)
_C2900PortRxNoDestMultiFrames_Type=Counter32
_C2900PortRxNoDestMultiFrames_Object=MibTableColumn
c2900PortRxNoDestMultiFrames=_C2900PortRxNoDestMultiFrames_Object((1,3,6,1,4,1,9,9,87,1,4,2,1,4),_C2900PortRxNoDestMultiFrames_Type())
c2900PortRxNoDestMultiFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortRxNoDestMultiFrames.setStatus(_B)
if mibBuilder.loadTexts:c2900PortRxNoDestMultiFrames.setUnits(_G)
_C2900PortRxSuppressBcastFrames_Type=Counter32
_C2900PortRxSuppressBcastFrames_Object=MibTableColumn
c2900PortRxSuppressBcastFrames=_C2900PortRxSuppressBcastFrames_Object((1,3,6,1,4,1,9,9,87,1,4,2,1,5),_C2900PortRxSuppressBcastFrames_Type())
c2900PortRxSuppressBcastFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortRxSuppressBcastFrames.setStatus(_F)
if mibBuilder.loadTexts:c2900PortRxSuppressBcastFrames.setUnits(_G)
_C2900PortRxFcsErrFrames_Type=Counter32
_C2900PortRxFcsErrFrames_Object=MibTableColumn
c2900PortRxFcsErrFrames=_C2900PortRxFcsErrFrames_Object((1,3,6,1,4,1,9,9,87,1,4,2,1,6),_C2900PortRxFcsErrFrames_Type())
c2900PortRxFcsErrFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortRxFcsErrFrames.setStatus(_B)
if mibBuilder.loadTexts:c2900PortRxFcsErrFrames.setUnits(_G)
_C2900PortCollFragFrames_Type=Counter32
_C2900PortCollFragFrames_Object=MibTableColumn
c2900PortCollFragFrames=_C2900PortCollFragFrames_Object((1,3,6,1,4,1,9,9,87,1,4,2,1,7),_C2900PortCollFragFrames_Type())
c2900PortCollFragFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortCollFragFrames.setStatus(_B)
if mibBuilder.loadTexts:c2900PortCollFragFrames.setUnits(_G)
_C2900PortTxMulticastFrames_Type=Counter32
_C2900PortTxMulticastFrames_Object=MibTableColumn
c2900PortTxMulticastFrames=_C2900PortTxMulticastFrames_Object((1,3,6,1,4,1,9,9,87,1,4,2,1,8),_C2900PortTxMulticastFrames_Type())
c2900PortTxMulticastFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortTxMulticastFrames.setStatus(_B)
if mibBuilder.loadTexts:c2900PortTxMulticastFrames.setUnits(_G)
_C2900PortTxBroadcastFrames_Type=Counter32
_C2900PortTxBroadcastFrames_Object=MibTableColumn
c2900PortTxBroadcastFrames=_C2900PortTxBroadcastFrames_Object((1,3,6,1,4,1,9,9,87,1,4,2,1,9),_C2900PortTxBroadcastFrames_Type())
c2900PortTxBroadcastFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900PortTxBroadcastFrames.setStatus(_B)
if mibBuilder.loadTexts:c2900PortTxBroadcastFrames.setUnits(_G)
_C2900BandwidthUsage_ObjectIdentity=ObjectIdentity
c2900BandwidthUsage=_C2900BandwidthUsage_ObjectIdentity((1,3,6,1,4,1,9,9,87,1,5))
_C2900BandwidthUsageCurrent_Type=Gauge32
_C2900BandwidthUsageCurrent_Object=MibScalar
c2900BandwidthUsageCurrent=_C2900BandwidthUsageCurrent_Object((1,3,6,1,4,1,9,9,87,1,5,1),_C2900BandwidthUsageCurrent_Type())
c2900BandwidthUsageCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900BandwidthUsageCurrent.setStatus(_B)
if mibBuilder.loadTexts:c2900BandwidthUsageCurrent.setUnits(_AH)
_C2900BandwidthUsageMaxPeakEntries_Type=Gauge32
_C2900BandwidthUsageMaxPeakEntries_Object=MibScalar
c2900BandwidthUsageMaxPeakEntries=_C2900BandwidthUsageMaxPeakEntries_Object((1,3,6,1,4,1,9,9,87,1,5,2),_C2900BandwidthUsageMaxPeakEntries_Type())
c2900BandwidthUsageMaxPeakEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900BandwidthUsageMaxPeakEntries.setStatus(_B)
class _C2900BandwidthUsagePeakInterval_Type(Integer32):defaultValue=24;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,6,12,24,48,72,96,120,144,168)));namedValues=NamedValues(*(('onehour',1),('threehours',3),('sixhours',6),('twelvehours',12),('oneday',24),('twodays',48),('threedays',72),('fourdays',96),('fivedays',120),('sixdays',144),('oneweek',168)))
_C2900BandwidthUsagePeakInterval_Type.__name__=_D
_C2900BandwidthUsagePeakInterval_Object=MibScalar
c2900BandwidthUsagePeakInterval=_C2900BandwidthUsagePeakInterval_Object((1,3,6,1,4,1,9,9,87,1,5,3),_C2900BandwidthUsagePeakInterval_Type())
c2900BandwidthUsagePeakInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900BandwidthUsagePeakInterval.setStatus(_B)
_C2900BandwidthUsagePeakRestart_Type=TruthValue
_C2900BandwidthUsagePeakRestart_Object=MibScalar
c2900BandwidthUsagePeakRestart=_C2900BandwidthUsagePeakRestart_Object((1,3,6,1,4,1,9,9,87,1,5,4),_C2900BandwidthUsagePeakRestart_Type())
c2900BandwidthUsagePeakRestart.setMaxAccess(_E)
if mibBuilder.loadTexts:c2900BandwidthUsagePeakRestart.setStatus(_B)
_C2900BandwidthUsageCurrentPeakEntry_Type=Gauge32
_C2900BandwidthUsageCurrentPeakEntry_Object=MibScalar
c2900BandwidthUsageCurrentPeakEntry=_C2900BandwidthUsageCurrentPeakEntry_Object((1,3,6,1,4,1,9,9,87,1,5,5),_C2900BandwidthUsageCurrentPeakEntry_Type())
c2900BandwidthUsageCurrentPeakEntry.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900BandwidthUsageCurrentPeakEntry.setStatus(_B)
_C2900BandwidthUsagePeakTable_Object=MibTable
c2900BandwidthUsagePeakTable=_C2900BandwidthUsagePeakTable_Object((1,3,6,1,4,1,9,9,87,1,5,6))
if mibBuilder.loadTexts:c2900BandwidthUsagePeakTable.setStatus(_B)
_C2900BandwidthUsagePeakEntry_Object=MibTableRow
c2900BandwidthUsagePeakEntry=_C2900BandwidthUsagePeakEntry_Object((1,3,6,1,4,1,9,9,87,1,5,6,1))
c2900BandwidthUsagePeakEntry.setIndexNames((0,_A,_A6))
if mibBuilder.loadTexts:c2900BandwidthUsagePeakEntry.setStatus(_B)
class _C2900BandwidthUsagePeakIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_C2900BandwidthUsagePeakIndex_Type.__name__=_D
_C2900BandwidthUsagePeakIndex_Object=MibTableColumn
c2900BandwidthUsagePeakIndex=_C2900BandwidthUsagePeakIndex_Object((1,3,6,1,4,1,9,9,87,1,5,6,1,1),_C2900BandwidthUsagePeakIndex_Type())
c2900BandwidthUsagePeakIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900BandwidthUsagePeakIndex.setStatus(_B)
_C2900BandwidthUsageStartTime_Type=DateAndTime
_C2900BandwidthUsageStartTime_Object=MibTableColumn
c2900BandwidthUsageStartTime=_C2900BandwidthUsageStartTime_Object((1,3,6,1,4,1,9,9,87,1,5,6,1,2),_C2900BandwidthUsageStartTime_Type())
c2900BandwidthUsageStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900BandwidthUsageStartTime.setStatus(_B)
_C2900BandwidthUsagePeak_Type=Gauge32
_C2900BandwidthUsagePeak_Object=MibTableColumn
c2900BandwidthUsagePeak=_C2900BandwidthUsagePeak_Object((1,3,6,1,4,1,9,9,87,1,5,6,1,3),_C2900BandwidthUsagePeak_Type())
c2900BandwidthUsagePeak.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900BandwidthUsagePeak.setStatus(_B)
if mibBuilder.loadTexts:c2900BandwidthUsagePeak.setUnits(_AH)
_C2900BandwidthUsagePeakTime_Type=DateAndTime
_C2900BandwidthUsagePeakTime_Object=MibTableColumn
c2900BandwidthUsagePeakTime=_C2900BandwidthUsagePeakTime_Object((1,3,6,1,4,1,9,9,87,1,5,6,1,4),_C2900BandwidthUsagePeakTime_Type())
c2900BandwidthUsagePeakTime.setMaxAccess(_C)
if mibBuilder.loadTexts:c2900BandwidthUsagePeakTime.setStatus(_B)
_C2900MibNotifications_ObjectIdentity=ObjectIdentity
c2900MibNotifications=_C2900MibNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,87,2))
_C2900MibNotificationsPrefix_ObjectIdentity=ObjectIdentity
c2900MibNotificationsPrefix=_C2900MibNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,87,2,0))
_C2900MIBConformance_ObjectIdentity=ObjectIdentity
c2900MIBConformance=_C2900MIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,87,3))
_C2900MIBCompliances_ObjectIdentity=ObjectIdentity
c2900MIBCompliances=_C2900MIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,87,3,1))
_C2900MIBGroups_ObjectIdentity=ObjectIdentity
c2900MIBGroups=_C2900MIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,87,3,2))
c2900SysInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,87,3,2,1))
c2900SysInfoGroup.setObjects(*((_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:c2900SysInfoGroup.setStatus(_B)
c2900SysConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,87,3,2,2))
c2900SysConfigGroup.setObjects(*((_A,_AS),(_A,_AT)))
if mibBuilder.loadTexts:c2900SysConfigGroup.setStatus(_F)
c2900ModuleGroup=ObjectGroup((1,3,6,1,4,1,9,9,87,3,2,3))
c2900ModuleGroup.setObjects(*((_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:c2900ModuleGroup.setStatus(_B)
c2900PortGroup=ObjectGroup((1,3,6,1,4,1,9,9,87,3,2,4))
c2900PortGroup.setObjects(*((_A,_J),(_A,_K),(_A,_A7),(_A,_L),(_A,_AY),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_H),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_I),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:c2900PortGroup.setStatus(_F)
c2900PortStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,87,3,2,5))
c2900PortStatsGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_AZ),(_A,_u),(_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:c2900PortStatsGroup.setStatus(_F)
c2900BandwidthUsageGroup=ObjectGroup((1,3,6,1,4,1,9,9,87,3,2,6))
c2900BandwidthUsageGroup.setObjects(*((_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_A6),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:c2900BandwidthUsageGroup.setStatus(_B)
c2900PortGroupSA3=ObjectGroup((1,3,6,1,4,1,9,9,87,3,2,7))
c2900PortGroupSA3.setObjects(*((_A,_J),(_A,_K),(_A,_A7),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_H),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_I),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:c2900PortGroupSA3.setStatus(_F)
c2900PortStatsGroupSA3=ObjectGroup((1,3,6,1,4,1,9,9,87,3,2,8))
c2900PortStatsGroupSA3.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:c2900PortStatsGroupSA3.setStatus(_F)
c2900PortGroupSA5=ObjectGroup((1,3,6,1,4,1,9,9,87,3,2,9))
c2900PortGroupSA5.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_H),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_I),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_p)))
if mibBuilder.loadTexts:c2900PortGroupSA5.setStatus(_F)
c2900PortGroupSA7=ObjectGroup((1,3,6,1,4,1,9,9,87,3,2,10))
c2900PortGroupSA7.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_H),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_I),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_p),(_A,_y)))
if mibBuilder.loadTexts:c2900PortGroupSA7.setStatus(_F)
c2900PortGroupWC2=ObjectGroup((1,3,6,1,4,1,9,9,87,3,2,11))
c2900PortGroupWC2.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_H),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_I),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_p),(_A,_y),(_A,_A8)))
if mibBuilder.loadTexts:c2900PortGroupWC2.setStatus(_F)
c2900PortGroupWC4=ObjectGroup((1,3,6,1,4,1,9,9,87,3,2,12))
c2900PortGroupWC4.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_H),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_I),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_p),(_A,_y),(_A,_A8),(_A,_Ai),(_A,_Aj),(_A,_Ak)))
if mibBuilder.loadTexts:c2900PortGroupWC4.setStatus(_B)
c2900PortStatsGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,87,3,2,14))
c2900PortStatsGroupRev1.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:c2900PortStatsGroupRev1.setStatus(_B)
c2900AddressViolation=NotificationType((1,3,6,1,4,1,9,9,87,2,0,1))
c2900AddressViolation.setObjects((_A,_I))
if mibBuilder.loadTexts:c2900AddressViolation.setStatus(_B)
c2900BroadcastStorm=NotificationType((1,3,6,1,4,1,9,9,87,2,0,2))
c2900BroadcastStorm.setObjects((_A,_H))
if mibBuilder.loadTexts:c2900BroadcastStorm.setStatus(_B)
c2900RpsFailed=NotificationType((1,3,6,1,4,1,9,9,87,2,0,3))
c2900RpsFailed.setObjects((_AA,'sysName'))
if mibBuilder.loadTexts:c2900RpsFailed.setStatus(_B)
c2900NotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,87,3,2,13))
c2900NotificationsGroup.setObjects(*((_A,_Al),(_A,_Am),(_A,_An)))
if mibBuilder.loadTexts:c2900NotificationsGroup.setStatus(_B)
c2900MIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,87,3,1,1))
c2900MIBCompliance.setObjects(*((_A,_l),(_A,_Ao),(_A,_Ap),(_A,_m)))
if mibBuilder.loadTexts:c2900MIBCompliance.setStatus(_F)
c2900MIBComplianceSA5=ModuleCompliance((1,3,6,1,4,1,9,9,87,3,1,2))
c2900MIBComplianceSA5.setObjects(*((_A,_l),(_A,_o),(_A,_m),(_A,_Aq)))
if mibBuilder.loadTexts:c2900MIBComplianceSA5.setStatus(_F)
c2900MIBComplianceSA3=ModuleCompliance((1,3,6,1,4,1,9,9,87,3,1,3))
c2900MIBComplianceSA3.setObjects(*((_A,_l),(_A,_o),(_A,_m),(_A,_Ar),(_A,_As)))
if mibBuilder.loadTexts:c2900MIBComplianceSA3.setStatus(_F)
c2900MIBComplianceSA7=ModuleCompliance((1,3,6,1,4,1,9,9,87,3,1,4))
c2900MIBComplianceSA7.setObjects(*((_A,_l),(_A,_o),(_A,_m),(_A,_At)))
if mibBuilder.loadTexts:c2900MIBComplianceSA7.setStatus(_F)
c2900MIBComplianceWC2=ModuleCompliance((1,3,6,1,4,1,9,9,87,3,1,5))
c2900MIBComplianceWC2.setObjects(*((_A,_l),(_A,_o),(_A,_m),(_A,_Au)))
if mibBuilder.loadTexts:c2900MIBComplianceWC2.setStatus(_F)
c2900MIBComplianceWC4=ModuleCompliance((1,3,6,1,4,1,9,9,87,3,1,6))
c2900MIBComplianceWC4.setObjects(*((_A,_l),(_A,_o),(_A,_m),(_A,_Av),(_A,_Aw),(_A,_Ax)))
if mibBuilder.loadTexts:c2900MIBComplianceWC4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoC2900MIB':ciscoC2900MIB,'c2900MIBObjects':c2900MIBObjects,'c2900SysInfo':c2900SysInfo,_AI:c2900InfoBoardRevision,_AJ:c2900InfoPeakBuffersUsed,_AK:c2900InfoTotalBufferDepth,_AL:c2900InfoAddrCapacity,_AM:c2900InfoRestrictedStaticAddrCapacity,_AN:c2900InfoSelfTestFailed,_AO:c2900InfoUtilDisplay,_AP:c2900InfoVisualIndicatorMode,_AQ:c2900InfoRedunantPowerSupplyInfo,_AR:c2900InfoBoardIdentifier,'c2900SysConfig':c2900SysConfig,_AS:c2900ConfigAddressViolationAction,_AT:c2900ConfigBroadcastStormAlarm,'c2900ModuleTable':c2900ModuleTable,'c2900ModuleEntry':c2900ModuleEntry,_AE:c2900ModuleIndex,_AU:c2900ModuleStatus,_AV:c2900ModuleType,_AW:c2900ModuleHwVersion,_AX:c2900ModuleSwVersion,'c2900Port':c2900Port,'c2900PortTable':c2900PortTable,'c2900PortEntry':c2900PortEntry,_A4:c2900PortModuleIndex,_A5:c2900PortIndex,_J:c2900PortUsageApplication,_K:c2900PortGroupIndex,_A7:c2900PortMayLearnAddress,_L:c2900PortMayForwardFrames,_AY:c2900PortBufferCongestionControl,_M:c2900PortBufferCongestionThreshholdPercent,_N:c2900PortFrameAge,_O:c2900PortAddrSecureMaxAddresses,_P:c2900PortAddrSecureCurrentAddresses,_Q:c2900PortAddrSecureAddrViolations,_R:c2900PortNumberOfLearnedAddresses,_S:c2900PortNumberOfDroppedAddresses,_T:c2900PortClearAddresses,_U:c2900PortFloodUnknownMulticasts,_V:c2900PortFloodUnknownUnicasts,_W:c2900PortLinkbeatStatus,_X:c2900PortBroadcastStormAction,_H:c2900PortBroadcastRisingThreshold,_Y:c2900PortBroadcastFallingThreshold,_Z:c2900PortStatus,_a:c2900PortTestResult,_b:c2900PortVisualIndicator,_I:c2900PortIfIndex,_c:c2900PortAddressViolationAction,_d:c2900PortBroadcastStormAlarm,_e:c2900PortMonitorDestinationPort,_f:c2900PortSwitchPortIndex,_g:c2900PortMonitoredPortMap,_h:c2900PortDuplexState,_i:c2900PortDuplexStatus,_j:c2900PortAdminSpeed,_k:c2900PortNoMonitorDestinationPort,_p:c2900Portdot1dBasePort,_y:c2900PortSpantreeFastStart,_A8:c2900PortVoiceVlanId,_Ai:c2900PortAddrSecureAgingTime,_Aj:c2900PortAddrSecureAgingType,_Ak:c2900PortAddrSecureAgingStatic,'c2900PortStatsTable':c2900PortStatsTable,'c2900PortStatsEntry':c2900PortStatsEntry,_q:c2900PortRxNoBwFrames,_r:c2900PortRxNoBufferFrames,_s:c2900PortRxNoDestUniFrames,_t:c2900PortRxNoDestMultiFrames,_AZ:c2900PortRxSuppressBcastFrames,_u:c2900PortRxFcsErrFrames,_v:c2900PortCollFragFrames,_w:c2900PortTxMulticastFrames,_x:c2900PortTxBroadcastFrames,'c2900BandwidthUsage':c2900BandwidthUsage,_Aa:c2900BandwidthUsageCurrent,_Ab:c2900BandwidthUsageMaxPeakEntries,_Ac:c2900BandwidthUsagePeakInterval,_Ad:c2900BandwidthUsagePeakRestart,_Ah:c2900BandwidthUsageCurrentPeakEntry,'c2900BandwidthUsagePeakTable':c2900BandwidthUsagePeakTable,'c2900BandwidthUsagePeakEntry':c2900BandwidthUsagePeakEntry,_A6:c2900BandwidthUsagePeakIndex,_Ae:c2900BandwidthUsageStartTime,_Af:c2900BandwidthUsagePeak,_Ag:c2900BandwidthUsagePeakTime,'c2900MibNotifications':c2900MibNotifications,'c2900MibNotificationsPrefix':c2900MibNotificationsPrefix,_Al:c2900AddressViolation,_Am:c2900BroadcastStorm,_An:c2900RpsFailed,'c2900MIBConformance':c2900MIBConformance,'c2900MIBCompliances':c2900MIBCompliances,'c2900MIBCompliance':c2900MIBCompliance,'c2900MIBComplianceSA5':c2900MIBComplianceSA5,'c2900MIBComplianceSA3':c2900MIBComplianceSA3,'c2900MIBComplianceSA7':c2900MIBComplianceSA7,'c2900MIBComplianceWC2':c2900MIBComplianceWC2,'c2900MIBComplianceWC4':c2900MIBComplianceWC4,'c2900MIBGroups':c2900MIBGroups,_l:c2900SysInfoGroup,_Ao:c2900SysConfigGroup,_o:c2900ModuleGroup,_Ap:c2900PortGroup,'c2900PortStatsGroup':c2900PortStatsGroup,_m:c2900BandwidthUsageGroup,_Ar:c2900PortGroupSA3,_As:c2900PortStatsGroupSA3,_Aq:c2900PortGroupSA5,_At:c2900PortGroupSA7,_Au:c2900PortGroupWC2,_Av:c2900PortGroupWC4,_Aw:c2900NotificationsGroup,_Ax:c2900PortStatsGroupRev1})