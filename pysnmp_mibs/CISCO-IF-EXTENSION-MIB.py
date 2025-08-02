_B1='ciscoIfExtensionTableIntfGroup3SupR02'
_B0='cieIfIndexPersistenceGroup'
_A_='cieDelayedLinkUpDownNotif'
_Az='cieLinkUp'
_Ay='cieLinkDown'
_Ax='cieIfIgnoreInterruptThresholdConfig'
_Aw='cieIfIgnoreBitErrorsConfig'
_Av='cieIfFillPatternConfig'
_Au='cieIfTransceiverFrequencyConfig'
_At='cieLinkUpDownConfig'
_As='cieIfSpeedGroupConfig'
_Ar='cieIfSharedConfig'
_Aq='cieIfDropVlOutOctets'
_Ap='cieIfDropVlOutPkts'
_Ao='cieIfDropVlInOctets'
_An='cieIfDropVlInPkts'
_Am='cieIfNoDropVlOutOctets'
_Al='cieIfNoDropVlOutPkts'
_Ak='cieIfNoDropVlInOctets'
_Aj='cieIfNoDropVlInPkts'
_Ai='cieInterfaceOwnershipBitmap'
_Ah='cieIfOwner'
_Ag='cieIfIndexPersistenceControl'
_Af='cieIfIndexGlobalPersistence'
_Ae='cieDelayedLinkUpDownNotifDelay'
_Ad='cieDelayedLinkUpDownNotifEnable'
_Ac='cieIfIndexPersistenceEnabled'
_Ab='cieIfIndexPersistence'
_Aa='cieIfInterval'
_AZ='cieIfHighSpeedReceive'
_AY='cieIfSpeedReceive'
_AX='cieStandardLinkUpDownVarbinds'
_AW='cieLinkUpDownEnable'
_AV='cieInterfacesOperCause'
_AU='cieInterfacesOperMode'
_AT='cieInterfacesIndex'
_AS='cieIfIndex'
_AR='cieIfDot1dBaseMappingPort'
_AQ='cieIfOutOctetRate'
_AP='cieIfOutPktRate'
_AO='cieIfInOctetRate'
_AN='cieIfInPktRate'
_AM='cieIfDot1qCustomOperEtherType'
_AL='cieIfDot1qCustomAdminEtherType'
_AK='cieSystemMtu'
_AJ='cieIfInterfaceDiscontinuityTime'
_AI='cieIfCarrierTransitionCount'
_AH='cieIfStateChangeReason'
_AG='cieIfKeepAliveEnabled'
_AF='cieIfResetCount'
_AE='cieIfPacketDiscontinuityTime'
_AD='cieIfOutputQueueDrops'
_AC='cieIfInputQueueDrops'
_AB='cieIfInAbortErrs'
_AA='cieIfInIgnored'
_A9='cieIfInOverrunErrs'
_A8='cieIfInFramingErrs'
_A7='cieIfInGiantsErrs'
_A6='cieIfInRuntsErrs'
_A5='cieIfLastOutHangTime'
_A4='cieIfLastOutTime'
_A3='cieIfLastInTime'
_A2='cieIfName'
_A1='octets per second'
_A0='packets per second'
_z='standard'
_y='not-accessible'
_x='cieIfStatusListIndex'
_w='entPhysicalIndex'
_v='ENTITY-MIB'
_u='OctetString'
_t='cieLinkUpDownNotifConfigGroup'
_s='cieIfOperStatusCauseDescr'
_r='IfIndexPersistenceState'
_q='notApplicable'
_p='milliseconds'
_o='DisplayString'
_n='Bits'
_m='ciscoIfExtensionTableIntfGroup3SupR01'
_l='cieIfVlStatsGroup'
_k='ciscoIfExtensionTableIntfGroup1'
_j='cieIfOperStatusCause'
_i='cieIfContextName'
_h='cieIfMtu'
_g='cieIfDhcpMode'
_f='Unsigned32'
_e='ifType'
_d='ifOperStatus'
_c='ifName'
_b='ifAdminStatus'
_a='cieIfStatusListGroupSup1'
_Z='ciscoIfExtensionTableIntfGroup3'
_Y='cieIfIndexPersistenceControlGroup'
_X='TruthValue'
_W='cieDelayedLinkUpDownNotifNotifEnableGroup'
_V='cieDelayedLinkUpDownNotifNotifGroup'
_U='ciscoIfExtensionTableIntfGroup2'
_T='ciscoIfExtUtilIntervalGroup'
_S='cieLinkUpDownNotifEnableGroup'
_R='ifIndex'
_Q='ciscoIfExtensionAsymmetricalSpeedGroup'
_P='cieLinkUpDownNotifGroup'
_O='cieIfStatusListGroup'
_N='Integer32'
_M='ciscoIfExtIfNameMappingGroup'
_L='ciscoIfExtDot1dBaseMappingGroup'
_K='ciscoIfExtUtilizationGroup'
_J='ciscoIfExtDot1qEtherTypeGroup'
_I='ciscoIfExtensionSystemGroup'
_H='ciscoIfExtensionTableIntfGroup'
_G='ciscoIfExtensionTablePacketGroup'
_F='IF-MIB'
_E='deprecated'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-IF-EXTENSION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_u,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
IfOperStatusReason,=mibBuilder.importSymbols('CISCO-TC','IfOperStatusReason')
entPhysicalIndex,=mibBuilder.importSymbols(_v,_w)
InterfaceIndexOrZero,ifAdminStatus,ifIndex,ifName,ifOperStatus,ifType=mibBuilder.importSymbols(_F,'InterfaceIndexOrZero',_b,_R,_c,_d,_e)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_n,'Counter32','Counter64','Gauge32',_N,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_f,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_o,'PhysAddress','TextualConvention','TimeStamp',_X)
ciscoIfExtensionMIB=ModuleIdentity((1,3,6,1,4,1,9,9,276))
if mibBuilder.loadTexts:ciscoIfExtensionMIB.setRevisions(('2021-02-12 00:00','2020-11-03 00:00','2016-12-01 00:00','2013-03-13 00:00','2012-09-05 00:00','2011-06-27 00:00','2009-02-26 00:00','2008-12-09 00:00','2008-10-06 00:00','2008-07-31 00:00','2008-07-08 00:00','2008-06-23 00:00','2007-07-23 00:00','2006-11-01 00:00','2005-04-28 00:00','2005-01-25 00:00','2004-09-08 00:00','2003-11-14 00:00','2003-08-12 00:00','2003-07-17 00:00','2003-06-25 00:00','2002-10-12 00:00','2002-07-24 00:00'))
class InterfaceIndexList(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class InterfaceOperModeList(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
class InterfaceOperCauseList(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
class InterfaceOwnershipList(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
class IfIndexPersistenceState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disable',1),('enable',2),('global',3)))
_CiscoIfExtensionMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoIfExtensionMIBNotifications=_CiscoIfExtensionMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,276,0))
_CiscoIfExtensionMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIfExtensionMIBObjects=_CiscoIfExtensionMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,276,1))
_CiscoIfExtensionStats_ObjectIdentity=ObjectIdentity
ciscoIfExtensionStats=_CiscoIfExtensionStats_ObjectIdentity((1,3,6,1,4,1,9,9,276,1,1))
_CieIfPacketStatsTable_Object=MibTable
cieIfPacketStatsTable=_CieIfPacketStatsTable_Object((1,3,6,1,4,1,9,9,276,1,1,1))
if mibBuilder.loadTexts:cieIfPacketStatsTable.setStatus(_B)
_CieIfPacketStatsEntry_Object=MibTableRow
cieIfPacketStatsEntry=_CieIfPacketStatsEntry_Object((1,3,6,1,4,1,9,9,276,1,1,1,1))
cieIfPacketStatsEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:cieIfPacketStatsEntry.setStatus(_B)
_CieIfLastInTime_Type=Gauge32
_CieIfLastInTime_Object=MibTableColumn
cieIfLastInTime=_CieIfLastInTime_Object((1,3,6,1,4,1,9,9,276,1,1,1,1,1),_CieIfLastInTime_Type())
cieIfLastInTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfLastInTime.setStatus(_B)
if mibBuilder.loadTexts:cieIfLastInTime.setUnits(_p)
_CieIfLastOutTime_Type=Gauge32
_CieIfLastOutTime_Object=MibTableColumn
cieIfLastOutTime=_CieIfLastOutTime_Object((1,3,6,1,4,1,9,9,276,1,1,1,1,2),_CieIfLastOutTime_Type())
cieIfLastOutTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfLastOutTime.setStatus(_B)
if mibBuilder.loadTexts:cieIfLastOutTime.setUnits(_p)
_CieIfLastOutHangTime_Type=Gauge32
_CieIfLastOutHangTime_Object=MibTableColumn
cieIfLastOutHangTime=_CieIfLastOutHangTime_Object((1,3,6,1,4,1,9,9,276,1,1,1,1,3),_CieIfLastOutHangTime_Type())
cieIfLastOutHangTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfLastOutHangTime.setStatus(_B)
if mibBuilder.loadTexts:cieIfLastOutHangTime.setUnits(_p)
_CieIfInRuntsErrs_Type=Counter32
_CieIfInRuntsErrs_Object=MibTableColumn
cieIfInRuntsErrs=_CieIfInRuntsErrs_Object((1,3,6,1,4,1,9,9,276,1,1,1,1,4),_CieIfInRuntsErrs_Type())
cieIfInRuntsErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfInRuntsErrs.setStatus(_B)
_CieIfInGiantsErrs_Type=Counter32
_CieIfInGiantsErrs_Object=MibTableColumn
cieIfInGiantsErrs=_CieIfInGiantsErrs_Object((1,3,6,1,4,1,9,9,276,1,1,1,1,5),_CieIfInGiantsErrs_Type())
cieIfInGiantsErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfInGiantsErrs.setStatus(_B)
_CieIfInFramingErrs_Type=Counter32
_CieIfInFramingErrs_Object=MibTableColumn
cieIfInFramingErrs=_CieIfInFramingErrs_Object((1,3,6,1,4,1,9,9,276,1,1,1,1,6),_CieIfInFramingErrs_Type())
cieIfInFramingErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfInFramingErrs.setStatus(_B)
_CieIfInOverrunErrs_Type=Counter32
_CieIfInOverrunErrs_Object=MibTableColumn
cieIfInOverrunErrs=_CieIfInOverrunErrs_Object((1,3,6,1,4,1,9,9,276,1,1,1,1,7),_CieIfInOverrunErrs_Type())
cieIfInOverrunErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfInOverrunErrs.setStatus(_B)
_CieIfInIgnored_Type=Counter32
_CieIfInIgnored_Object=MibTableColumn
cieIfInIgnored=_CieIfInIgnored_Object((1,3,6,1,4,1,9,9,276,1,1,1,1,8),_CieIfInIgnored_Type())
cieIfInIgnored.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfInIgnored.setStatus(_B)
_CieIfInAbortErrs_Type=Counter32
_CieIfInAbortErrs_Object=MibTableColumn
cieIfInAbortErrs=_CieIfInAbortErrs_Object((1,3,6,1,4,1,9,9,276,1,1,1,1,9),_CieIfInAbortErrs_Type())
cieIfInAbortErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfInAbortErrs.setStatus(_B)
_CieIfInputQueueDrops_Type=Counter32
_CieIfInputQueueDrops_Object=MibTableColumn
cieIfInputQueueDrops=_CieIfInputQueueDrops_Object((1,3,6,1,4,1,9,9,276,1,1,1,1,10),_CieIfInputQueueDrops_Type())
cieIfInputQueueDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfInputQueueDrops.setStatus(_B)
_CieIfOutputQueueDrops_Type=Counter32
_CieIfOutputQueueDrops_Object=MibTableColumn
cieIfOutputQueueDrops=_CieIfOutputQueueDrops_Object((1,3,6,1,4,1,9,9,276,1,1,1,1,11),_CieIfOutputQueueDrops_Type())
cieIfOutputQueueDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfOutputQueueDrops.setStatus(_B)
_CieIfPacketDiscontinuityTime_Type=TimeStamp
_CieIfPacketDiscontinuityTime_Object=MibTableColumn
cieIfPacketDiscontinuityTime=_CieIfPacketDiscontinuityTime_Object((1,3,6,1,4,1,9,9,276,1,1,1,1,12),_CieIfPacketDiscontinuityTime_Type())
cieIfPacketDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfPacketDiscontinuityTime.setStatus(_B)
_CieIfInterfaceTable_Object=MibTable
cieIfInterfaceTable=_CieIfInterfaceTable_Object((1,3,6,1,4,1,9,9,276,1,1,2))
if mibBuilder.loadTexts:cieIfInterfaceTable.setStatus(_B)
_CieIfInterfaceEntry_Object=MibTableRow
cieIfInterfaceEntry=_CieIfInterfaceEntry_Object((1,3,6,1,4,1,9,9,276,1,1,2,1))
cieIfInterfaceEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:cieIfInterfaceEntry.setStatus(_B)
_CieIfResetCount_Type=Counter32
_CieIfResetCount_Object=MibTableColumn
cieIfResetCount=_CieIfResetCount_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,1),_CieIfResetCount_Type())
cieIfResetCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfResetCount.setStatus(_B)
_CieIfKeepAliveEnabled_Type=TruthValue
_CieIfKeepAliveEnabled_Object=MibTableColumn
cieIfKeepAliveEnabled=_CieIfKeepAliveEnabled_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,2),_CieIfKeepAliveEnabled_Type())
cieIfKeepAliveEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cieIfKeepAliveEnabled.setStatus(_B)
_CieIfStateChangeReason_Type=SnmpAdminString
_CieIfStateChangeReason_Object=MibTableColumn
cieIfStateChangeReason=_CieIfStateChangeReason_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,3),_CieIfStateChangeReason_Type())
cieIfStateChangeReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfStateChangeReason.setStatus(_B)
_CieIfCarrierTransitionCount_Type=Counter32
_CieIfCarrierTransitionCount_Object=MibTableColumn
cieIfCarrierTransitionCount=_CieIfCarrierTransitionCount_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,4),_CieIfCarrierTransitionCount_Type())
cieIfCarrierTransitionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfCarrierTransitionCount.setStatus(_B)
_CieIfInterfaceDiscontinuityTime_Type=TimeStamp
_CieIfInterfaceDiscontinuityTime_Object=MibTableColumn
cieIfInterfaceDiscontinuityTime=_CieIfInterfaceDiscontinuityTime_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,5),_CieIfInterfaceDiscontinuityTime_Type())
cieIfInterfaceDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfInterfaceDiscontinuityTime.setStatus(_B)
class _CieIfDhcpMode_Type(TruthValue):defaultValue=2
_CieIfDhcpMode_Type.__name__=_X
_CieIfDhcpMode_Object=MibTableColumn
cieIfDhcpMode=_CieIfDhcpMode_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,6),_CieIfDhcpMode_Type())
cieIfDhcpMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cieIfDhcpMode.setStatus(_B)
class _CieIfMtu_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(40,2147483647))
_CieIfMtu_Type.__name__=_N
_CieIfMtu_Object=MibTableColumn
cieIfMtu=_CieIfMtu_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,7),_CieIfMtu_Type())
cieIfMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:cieIfMtu.setStatus(_B)
class _CieIfContextName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CieIfContextName_Type.__name__=_u
_CieIfContextName_Object=MibTableColumn
cieIfContextName=_CieIfContextName_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,8),_CieIfContextName_Type())
cieIfContextName.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfContextName.setStatus(_B)
_CieIfOperStatusCause_Type=IfOperStatusReason
_CieIfOperStatusCause_Object=MibTableColumn
cieIfOperStatusCause=_CieIfOperStatusCause_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,9),_CieIfOperStatusCause_Type())
cieIfOperStatusCause.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfOperStatusCause.setStatus(_B)
_CieIfOperStatusCauseDescr_Type=SnmpAdminString
_CieIfOperStatusCauseDescr_Object=MibTableColumn
cieIfOperStatusCauseDescr=_CieIfOperStatusCauseDescr_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,10),_CieIfOperStatusCauseDescr_Type())
cieIfOperStatusCauseDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfOperStatusCauseDescr.setStatus(_B)
_CieIfSpeedReceive_Type=Gauge32
_CieIfSpeedReceive_Object=MibTableColumn
cieIfSpeedReceive=_CieIfSpeedReceive_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,11),_CieIfSpeedReceive_Type())
cieIfSpeedReceive.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfSpeedReceive.setStatus(_B)
_CieIfHighSpeedReceive_Type=Gauge32
_CieIfHighSpeedReceive_Object=MibTableColumn
cieIfHighSpeedReceive=_CieIfHighSpeedReceive_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,12),_CieIfHighSpeedReceive_Type())
cieIfHighSpeedReceive.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfHighSpeedReceive.setStatus(_B)
class _CieIfOwner_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CieIfOwner_Type.__name__=_o
_CieIfOwner_Object=MibTableColumn
cieIfOwner=_CieIfOwner_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,13),_CieIfOwner_Type())
cieIfOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:cieIfOwner.setStatus(_B)
class _CieIfSharedConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_q,1),('ownerDedicated',2),('ownerShared',3),('sharedOnly',4)))
_CieIfSharedConfig_Type.__name__=_N
_CieIfSharedConfig_Object=MibTableColumn
cieIfSharedConfig=_CieIfSharedConfig_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,14),_CieIfSharedConfig_Type())
cieIfSharedConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfSharedConfig.setStatus(_B)
class _CieIfSpeedGroupConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_q,1),('tenG',2),('oneTwoFourEightG',3),('twoFourEightSixteenG',4),('fourEightSixteenThirtyTwoG',5),('eightSixteenThirtyTwoSixtyFourG',6)))
_CieIfSpeedGroupConfig_Type.__name__=_N
_CieIfSpeedGroupConfig_Object=MibTableColumn
cieIfSpeedGroupConfig=_CieIfSpeedGroupConfig_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,15),_CieIfSpeedGroupConfig_Type())
cieIfSpeedGroupConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:cieIfSpeedGroupConfig.setStatus(_B)
class _CieIfTransceiverFrequencyConfig_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_q,1),('fibreChannel',2),('ethernet',3)))
_CieIfTransceiverFrequencyConfig_Type.__name__=_N
_CieIfTransceiverFrequencyConfig_Object=MibTableColumn
cieIfTransceiverFrequencyConfig=_CieIfTransceiverFrequencyConfig_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,16),_CieIfTransceiverFrequencyConfig_Type())
cieIfTransceiverFrequencyConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:cieIfTransceiverFrequencyConfig.setStatus(_B)
class _CieIfFillPatternConfig_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('arbff8G',1),('idle8G',2)))
_CieIfFillPatternConfig_Type.__name__=_N
_CieIfFillPatternConfig_Object=MibTableColumn
cieIfFillPatternConfig=_CieIfFillPatternConfig_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,17),_CieIfFillPatternConfig_Type())
cieIfFillPatternConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:cieIfFillPatternConfig.setStatus(_B)
class _CieIfIgnoreBitErrorsConfig_Type(TruthValue):defaultValue=1
_CieIfIgnoreBitErrorsConfig_Type.__name__=_X
_CieIfIgnoreBitErrorsConfig_Object=MibTableColumn
cieIfIgnoreBitErrorsConfig=_CieIfIgnoreBitErrorsConfig_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,18),_CieIfIgnoreBitErrorsConfig_Type())
cieIfIgnoreBitErrorsConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:cieIfIgnoreBitErrorsConfig.setStatus(_B)
class _CieIfIgnoreInterruptThresholdConfig_Type(TruthValue):defaultValue=1
_CieIfIgnoreInterruptThresholdConfig_Type.__name__=_X
_CieIfIgnoreInterruptThresholdConfig_Object=MibTableColumn
cieIfIgnoreInterruptThresholdConfig=_CieIfIgnoreInterruptThresholdConfig_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,19),_CieIfIgnoreInterruptThresholdConfig_Type())
cieIfIgnoreInterruptThresholdConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:cieIfIgnoreInterruptThresholdConfig.setStatus(_B)
class _CieIfDuplexCfgStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('full',0),('half',1),('auto',2),('unsupported',3)))
_CieIfDuplexCfgStatus_Type.__name__=_N
_CieIfDuplexCfgStatus_Object=MibTableColumn
cieIfDuplexCfgStatus=_CieIfDuplexCfgStatus_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,20),_CieIfDuplexCfgStatus_Type())
cieIfDuplexCfgStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cieIfDuplexCfgStatus.setStatus(_B)
class _CieIfDuplexDetectStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('full',0),('half',1),('auto',2),('unknown',3),('invalid',4)))
_CieIfDuplexDetectStatus_Type.__name__=_N
_CieIfDuplexDetectStatus_Object=MibTableColumn
cieIfDuplexDetectStatus=_CieIfDuplexDetectStatus_Object((1,3,6,1,4,1,9,9,276,1,1,2,1,21),_CieIfDuplexDetectStatus_Type())
cieIfDuplexDetectStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cieIfDuplexDetectStatus.setStatus(_B)
_CieIfStatusListTable_Object=MibTable
cieIfStatusListTable=_CieIfStatusListTable_Object((1,3,6,1,4,1,9,9,276,1,1,3))
if mibBuilder.loadTexts:cieIfStatusListTable.setStatus(_B)
_CieIfStatusListEntry_Object=MibTableRow
cieIfStatusListEntry=_CieIfStatusListEntry_Object((1,3,6,1,4,1,9,9,276,1,1,3,1))
cieIfStatusListEntry.setIndexNames((0,_v,_w),(0,_A,_x))
if mibBuilder.loadTexts:cieIfStatusListEntry.setStatus(_B)
class _CieIfStatusListIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,33554432))
_CieIfStatusListIndex_Type.__name__=_f
_CieIfStatusListIndex_Object=MibTableColumn
cieIfStatusListIndex=_CieIfStatusListIndex_Object((1,3,6,1,4,1,9,9,276,1,1,3,1,1),_CieIfStatusListIndex_Type())
cieIfStatusListIndex.setMaxAccess(_y)
if mibBuilder.loadTexts:cieIfStatusListIndex.setStatus(_B)
_CieInterfacesIndex_Type=InterfaceIndexList
_CieInterfacesIndex_Object=MibTableColumn
cieInterfacesIndex=_CieInterfacesIndex_Object((1,3,6,1,4,1,9,9,276,1,1,3,1,2),_CieInterfacesIndex_Type())
cieInterfacesIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cieInterfacesIndex.setStatus(_B)
_CieInterfacesOperMode_Type=InterfaceOperModeList
_CieInterfacesOperMode_Object=MibTableColumn
cieInterfacesOperMode=_CieInterfacesOperMode_Object((1,3,6,1,4,1,9,9,276,1,1,3,1,3),_CieInterfacesOperMode_Type())
cieInterfacesOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cieInterfacesOperMode.setStatus(_B)
_CieInterfacesOperCause_Type=InterfaceOperCauseList
_CieInterfacesOperCause_Object=MibTableColumn
cieInterfacesOperCause=_CieInterfacesOperCause_Object((1,3,6,1,4,1,9,9,276,1,1,3,1,4),_CieInterfacesOperCause_Type())
cieInterfacesOperCause.setMaxAccess(_C)
if mibBuilder.loadTexts:cieInterfacesOperCause.setStatus(_B)
_CieInterfaceOwnershipBitmap_Type=InterfaceOwnershipList
_CieInterfaceOwnershipBitmap_Object=MibTableColumn
cieInterfaceOwnershipBitmap=_CieInterfaceOwnershipBitmap_Object((1,3,6,1,4,1,9,9,276,1,1,3,1,5),_CieInterfaceOwnershipBitmap_Type())
cieInterfaceOwnershipBitmap.setMaxAccess(_C)
if mibBuilder.loadTexts:cieInterfaceOwnershipBitmap.setStatus(_B)
_CieIfVlStatsTable_Object=MibTable
cieIfVlStatsTable=_CieIfVlStatsTable_Object((1,3,6,1,4,1,9,9,276,1,1,4))
if mibBuilder.loadTexts:cieIfVlStatsTable.setStatus(_B)
_CieIfVlStatsEntry_Object=MibTableRow
cieIfVlStatsEntry=_CieIfVlStatsEntry_Object((1,3,6,1,4,1,9,9,276,1,1,4,1))
cieIfVlStatsEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:cieIfVlStatsEntry.setStatus(_B)
_CieIfNoDropVlInPkts_Type=Counter64
_CieIfNoDropVlInPkts_Object=MibTableColumn
cieIfNoDropVlInPkts=_CieIfNoDropVlInPkts_Object((1,3,6,1,4,1,9,9,276,1,1,4,1,1),_CieIfNoDropVlInPkts_Type())
cieIfNoDropVlInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfNoDropVlInPkts.setStatus(_B)
_CieIfNoDropVlInOctets_Type=Counter64
_CieIfNoDropVlInOctets_Object=MibTableColumn
cieIfNoDropVlInOctets=_CieIfNoDropVlInOctets_Object((1,3,6,1,4,1,9,9,276,1,1,4,1,2),_CieIfNoDropVlInOctets_Type())
cieIfNoDropVlInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfNoDropVlInOctets.setStatus(_B)
_CieIfNoDropVlOutPkts_Type=Counter64
_CieIfNoDropVlOutPkts_Object=MibTableColumn
cieIfNoDropVlOutPkts=_CieIfNoDropVlOutPkts_Object((1,3,6,1,4,1,9,9,276,1,1,4,1,3),_CieIfNoDropVlOutPkts_Type())
cieIfNoDropVlOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfNoDropVlOutPkts.setStatus(_B)
_CieIfNoDropVlOutOctets_Type=Counter64
_CieIfNoDropVlOutOctets_Object=MibTableColumn
cieIfNoDropVlOutOctets=_CieIfNoDropVlOutOctets_Object((1,3,6,1,4,1,9,9,276,1,1,4,1,4),_CieIfNoDropVlOutOctets_Type())
cieIfNoDropVlOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfNoDropVlOutOctets.setStatus(_B)
_CieIfDropVlInPkts_Type=Counter64
_CieIfDropVlInPkts_Object=MibTableColumn
cieIfDropVlInPkts=_CieIfDropVlInPkts_Object((1,3,6,1,4,1,9,9,276,1,1,4,1,5),_CieIfDropVlInPkts_Type())
cieIfDropVlInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfDropVlInPkts.setStatus(_B)
_CieIfDropVlInOctets_Type=Counter64
_CieIfDropVlInOctets_Object=MibTableColumn
cieIfDropVlInOctets=_CieIfDropVlInOctets_Object((1,3,6,1,4,1,9,9,276,1,1,4,1,6),_CieIfDropVlInOctets_Type())
cieIfDropVlInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfDropVlInOctets.setStatus(_B)
_CieIfDropVlOutPkts_Type=Counter64
_CieIfDropVlOutPkts_Object=MibTableColumn
cieIfDropVlOutPkts=_CieIfDropVlOutPkts_Object((1,3,6,1,4,1,9,9,276,1,1,4,1,7),_CieIfDropVlOutPkts_Type())
cieIfDropVlOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfDropVlOutPkts.setStatus(_B)
_CieIfDropVlOutOctets_Type=Counter64
_CieIfDropVlOutOctets_Object=MibTableColumn
cieIfDropVlOutOctets=_CieIfDropVlOutOctets_Object((1,3,6,1,4,1,9,9,276,1,1,4,1,8),_CieIfDropVlOutOctets_Type())
cieIfDropVlOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfDropVlOutOctets.setStatus(_B)
_CiscoIfExtSystemConfig_ObjectIdentity=ObjectIdentity
ciscoIfExtSystemConfig=_CiscoIfExtSystemConfig_ObjectIdentity((1,3,6,1,4,1,9,9,276,1,2))
class _CieSystemMtu_Type(Integer32):defaultValue=1500
_CieSystemMtu_Type.__name__=_N
_CieSystemMtu_Object=MibScalar
cieSystemMtu=_CieSystemMtu_Object((1,3,6,1,4,1,9,9,276,1,2,1),_CieSystemMtu_Type())
cieSystemMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:cieSystemMtu.setStatus(_B)
class _CieLinkUpDownEnable_Type(Bits):defaultBinValue='1';namedValues=NamedValues(*((_z,0),('cisco',1)))
_CieLinkUpDownEnable_Type.__name__=_n
_CieLinkUpDownEnable_Object=MibScalar
cieLinkUpDownEnable=_CieLinkUpDownEnable_Object((1,3,6,1,4,1,9,9,276,1,2,2),_CieLinkUpDownEnable_Type())
cieLinkUpDownEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cieLinkUpDownEnable.setStatus(_E)
class _CieStandardLinkUpDownVarbinds_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_z,1),('additional',2),('other',3)))
_CieStandardLinkUpDownVarbinds_Type.__name__=_N
_CieStandardLinkUpDownVarbinds_Object=MibScalar
cieStandardLinkUpDownVarbinds=_CieStandardLinkUpDownVarbinds_Object((1,3,6,1,4,1,9,9,276,1,2,3),_CieStandardLinkUpDownVarbinds_Type())
cieStandardLinkUpDownVarbinds.setMaxAccess(_D)
if mibBuilder.loadTexts:cieStandardLinkUpDownVarbinds.setStatus(_E)
class _CieIfIndexPersistence_Type(TruthValue):defaultValue=2
_CieIfIndexPersistence_Type.__name__=_X
_CieIfIndexPersistence_Object=MibScalar
cieIfIndexPersistence=_CieIfIndexPersistence_Object((1,3,6,1,4,1,9,9,276,1,2,4),_CieIfIndexPersistence_Type())
cieIfIndexPersistence.setMaxAccess(_D)
if mibBuilder.loadTexts:cieIfIndexPersistence.setStatus(_E)
_CieIfIndexPersistenceTable_Object=MibTable
cieIfIndexPersistenceTable=_CieIfIndexPersistenceTable_Object((1,3,6,1,4,1,9,9,276,1,2,5))
if mibBuilder.loadTexts:cieIfIndexPersistenceTable.setStatus(_B)
_CieIfIndexPersistenceEntry_Object=MibTableRow
cieIfIndexPersistenceEntry=_CieIfIndexPersistenceEntry_Object((1,3,6,1,4,1,9,9,276,1,2,5,1))
cieIfIndexPersistenceEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:cieIfIndexPersistenceEntry.setStatus(_B)
class _CieIfIndexPersistenceEnabled_Type(TruthValue):defaultValue=1
_CieIfIndexPersistenceEnabled_Type.__name__=_X
_CieIfIndexPersistenceEnabled_Object=MibTableColumn
cieIfIndexPersistenceEnabled=_CieIfIndexPersistenceEnabled_Object((1,3,6,1,4,1,9,9,276,1,2,5,1,1),_CieIfIndexPersistenceEnabled_Type())
cieIfIndexPersistenceEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cieIfIndexPersistenceEnabled.setStatus(_E)
class _CieIfIndexPersistenceControl_Type(IfIndexPersistenceState):defaultValue=3
_CieIfIndexPersistenceControl_Type.__name__=_r
_CieIfIndexPersistenceControl_Object=MibTableColumn
cieIfIndexPersistenceControl=_CieIfIndexPersistenceControl_Object((1,3,6,1,4,1,9,9,276,1,2,5,1,2),_CieIfIndexPersistenceControl_Type())
cieIfIndexPersistenceControl.setMaxAccess(_D)
if mibBuilder.loadTexts:cieIfIndexPersistenceControl.setStatus(_B)
class _CieDelayedLinkUpDownNotifEnable_Type(TruthValue):defaultValue=2
_CieDelayedLinkUpDownNotifEnable_Type.__name__=_X
_CieDelayedLinkUpDownNotifEnable_Object=MibScalar
cieDelayedLinkUpDownNotifEnable=_CieDelayedLinkUpDownNotifEnable_Object((1,3,6,1,4,1,9,9,276,1,2,6),_CieDelayedLinkUpDownNotifEnable_Type())
cieDelayedLinkUpDownNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cieDelayedLinkUpDownNotifEnable.setStatus(_B)
class _CieDelayedLinkUpDownNotifDelay_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CieDelayedLinkUpDownNotifDelay_Type.__name__=_f
_CieDelayedLinkUpDownNotifDelay_Object=MibScalar
cieDelayedLinkUpDownNotifDelay=_CieDelayedLinkUpDownNotifDelay_Object((1,3,6,1,4,1,9,9,276,1,2,7),_CieDelayedLinkUpDownNotifDelay_Type())
cieDelayedLinkUpDownNotifDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:cieDelayedLinkUpDownNotifDelay.setStatus(_B)
if mibBuilder.loadTexts:cieDelayedLinkUpDownNotifDelay.setUnits('minutes')
class _CieIfIndexGlobalPersistence_Type(IfIndexPersistenceState):defaultValue=1
_CieIfIndexGlobalPersistence_Type.__name__=_r
_CieIfIndexGlobalPersistence_Object=MibScalar
cieIfIndexGlobalPersistence=_CieIfIndexGlobalPersistence_Object((1,3,6,1,4,1,9,9,276,1,2,8),_CieIfIndexGlobalPersistence_Type())
cieIfIndexGlobalPersistence.setMaxAccess(_D)
if mibBuilder.loadTexts:cieIfIndexGlobalPersistence.setStatus(_B)
class _CieLinkUpDownConfig_Type(Bits):namedValues=NamedValues(*(('standardLinkUp',0),('standardLinkDown',1),('additionalLinkUp',2),('additionalLinkDown',3),('ciscoLinkUp',4),('ciscoLinkDown',5)))
_CieLinkUpDownConfig_Type.__name__=_n
_CieLinkUpDownConfig_Object=MibScalar
cieLinkUpDownConfig=_CieLinkUpDownConfig_Object((1,3,6,1,4,1,9,9,276,1,2,9),_CieLinkUpDownConfig_Type())
cieLinkUpDownConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:cieLinkUpDownConfig.setStatus(_B)
_CiscoIfExtDot1qCustomEtherType_ObjectIdentity=ObjectIdentity
ciscoIfExtDot1qCustomEtherType=_CiscoIfExtDot1qCustomEtherType_ObjectIdentity((1,3,6,1,4,1,9,9,276,1,3))
_CieIfDot1qCustomEtherTypeTable_Object=MibTable
cieIfDot1qCustomEtherTypeTable=_CieIfDot1qCustomEtherTypeTable_Object((1,3,6,1,4,1,9,9,276,1,3,1))
if mibBuilder.loadTexts:cieIfDot1qCustomEtherTypeTable.setStatus(_B)
_CieIfDot1qCustomEtherTypeEntry_Object=MibTableRow
cieIfDot1qCustomEtherTypeEntry=_CieIfDot1qCustomEtherTypeEntry_Object((1,3,6,1,4,1,9,9,276,1,3,1,1))
cieIfDot1qCustomEtherTypeEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:cieIfDot1qCustomEtherTypeEntry.setStatus(_B)
class _CieIfDot1qCustomAdminEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CieIfDot1qCustomAdminEtherType_Type.__name__=_N
_CieIfDot1qCustomAdminEtherType_Object=MibTableColumn
cieIfDot1qCustomAdminEtherType=_CieIfDot1qCustomAdminEtherType_Object((1,3,6,1,4,1,9,9,276,1,3,1,1,1),_CieIfDot1qCustomAdminEtherType_Type())
cieIfDot1qCustomAdminEtherType.setMaxAccess(_D)
if mibBuilder.loadTexts:cieIfDot1qCustomAdminEtherType.setStatus(_B)
class _CieIfDot1qCustomOperEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CieIfDot1qCustomOperEtherType_Type.__name__=_N
_CieIfDot1qCustomOperEtherType_Object=MibTableColumn
cieIfDot1qCustomOperEtherType=_CieIfDot1qCustomOperEtherType_Object((1,3,6,1,4,1,9,9,276,1,3,1,1,2),_CieIfDot1qCustomOperEtherType_Type())
cieIfDot1qCustomOperEtherType.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfDot1qCustomOperEtherType.setStatus(_B)
_CiscoIfExtUtilization_ObjectIdentity=ObjectIdentity
ciscoIfExtUtilization=_CiscoIfExtUtilization_ObjectIdentity((1,3,6,1,4,1,9,9,276,1,4))
_CieIfUtilTable_Object=MibTable
cieIfUtilTable=_CieIfUtilTable_Object((1,3,6,1,4,1,9,9,276,1,4,1))
if mibBuilder.loadTexts:cieIfUtilTable.setStatus(_B)
_CieIfUtilEntry_Object=MibTableRow
cieIfUtilEntry=_CieIfUtilEntry_Object((1,3,6,1,4,1,9,9,276,1,4,1,1))
cieIfUtilEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:cieIfUtilEntry.setStatus(_B)
_CieIfInPktRate_Type=Counter64
_CieIfInPktRate_Object=MibTableColumn
cieIfInPktRate=_CieIfInPktRate_Object((1,3,6,1,4,1,9,9,276,1,4,1,1,1),_CieIfInPktRate_Type())
cieIfInPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfInPktRate.setStatus(_B)
if mibBuilder.loadTexts:cieIfInPktRate.setUnits(_A0)
_CieIfInOctetRate_Type=Counter64
_CieIfInOctetRate_Object=MibTableColumn
cieIfInOctetRate=_CieIfInOctetRate_Object((1,3,6,1,4,1,9,9,276,1,4,1,1,2),_CieIfInOctetRate_Type())
cieIfInOctetRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfInOctetRate.setStatus(_B)
if mibBuilder.loadTexts:cieIfInOctetRate.setUnits(_A1)
_CieIfOutPktRate_Type=Counter64
_CieIfOutPktRate_Object=MibTableColumn
cieIfOutPktRate=_CieIfOutPktRate_Object((1,3,6,1,4,1,9,9,276,1,4,1,1,3),_CieIfOutPktRate_Type())
cieIfOutPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfOutPktRate.setStatus(_B)
if mibBuilder.loadTexts:cieIfOutPktRate.setUnits(_A0)
_CieIfOutOctetRate_Type=Counter64
_CieIfOutOctetRate_Object=MibTableColumn
cieIfOutOctetRate=_CieIfOutOctetRate_Object((1,3,6,1,4,1,9,9,276,1,4,1,1,4),_CieIfOutOctetRate_Type())
cieIfOutOctetRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfOutOctetRate.setStatus(_B)
if mibBuilder.loadTexts:cieIfOutOctetRate.setUnits(_A1)
class _CieIfInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CieIfInterval_Type.__name__=_f
_CieIfInterval_Object=MibTableColumn
cieIfInterval=_CieIfInterval_Object((1,3,6,1,4,1,9,9,276,1,4,1,1,5),_CieIfInterval_Type())
cieIfInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cieIfInterval.setStatus(_B)
if mibBuilder.loadTexts:cieIfInterval.setUnits('seconds')
_CiscoIfExtDot1dBaseMapping_ObjectIdentity=ObjectIdentity
ciscoIfExtDot1dBaseMapping=_CiscoIfExtDot1dBaseMapping_ObjectIdentity((1,3,6,1,4,1,9,9,276,1,5))
_CieIfDot1dBaseMappingTable_Object=MibTable
cieIfDot1dBaseMappingTable=_CieIfDot1dBaseMappingTable_Object((1,3,6,1,4,1,9,9,276,1,5,1))
if mibBuilder.loadTexts:cieIfDot1dBaseMappingTable.setStatus(_B)
_CieIfDot1dBaseMappingEntry_Object=MibTableRow
cieIfDot1dBaseMappingEntry=_CieIfDot1dBaseMappingEntry_Object((1,3,6,1,4,1,9,9,276,1,5,1,1))
cieIfDot1dBaseMappingEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:cieIfDot1dBaseMappingEntry.setStatus(_B)
class _CieIfDot1dBaseMappingPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CieIfDot1dBaseMappingPort_Type.__name__=_N
_CieIfDot1dBaseMappingPort_Object=MibTableColumn
cieIfDot1dBaseMappingPort=_CieIfDot1dBaseMappingPort_Object((1,3,6,1,4,1,9,9,276,1,5,1,1,1),_CieIfDot1dBaseMappingPort_Type())
cieIfDot1dBaseMappingPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfDot1dBaseMappingPort.setStatus(_B)
_CiscoIfExtIfNameMapping_ObjectIdentity=ObjectIdentity
ciscoIfExtIfNameMapping=_CiscoIfExtIfNameMapping_ObjectIdentity((1,3,6,1,4,1,9,9,276,1,6))
_CieIfNameMappingTable_Object=MibTable
cieIfNameMappingTable=_CieIfNameMappingTable_Object((1,3,6,1,4,1,9,9,276,1,6,1))
if mibBuilder.loadTexts:cieIfNameMappingTable.setStatus(_B)
_CieIfNameMappingEntry_Object=MibTableRow
cieIfNameMappingEntry=_CieIfNameMappingEntry_Object((1,3,6,1,4,1,9,9,276,1,6,1,1))
cieIfNameMappingEntry.setIndexNames((0,_A,_A2))
if mibBuilder.loadTexts:cieIfNameMappingEntry.setStatus(_B)
class _CieIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,112))
_CieIfName_Type.__name__=_o
_CieIfName_Object=MibTableColumn
cieIfName=_CieIfName_Object((1,3,6,1,4,1,9,9,276,1,6,1,1,1),_CieIfName_Type())
cieIfName.setMaxAccess(_y)
if mibBuilder.loadTexts:cieIfName.setStatus(_B)
_CieIfIndex_Type=InterfaceIndexOrZero
_CieIfIndex_Object=MibTableColumn
cieIfIndex=_CieIfIndex_Object((1,3,6,1,4,1,9,9,276,1,6,1,1,2),_CieIfIndex_Type())
cieIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cieIfIndex.setStatus(_B)
_CiscoIfExtensionMIBConformance_ObjectIdentity=ObjectIdentity
ciscoIfExtensionMIBConformance=_CiscoIfExtensionMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,276,2))
_CiscoIfExtensionMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIfExtensionMIBCompliances=_CiscoIfExtensionMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,276,2,1))
_CiscoIfExtensionMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIfExtensionMIBGroups=_CiscoIfExtensionMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,276,2,2))
ciscoIfExtensionTablePacketGroup=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,1))
ciscoIfExtensionTablePacketGroup.setObjects(*((_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:ciscoIfExtensionTablePacketGroup.setStatus(_B)
ciscoIfExtensionTableIntfGroup=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,2))
ciscoIfExtensionTableIntfGroup.setObjects(*((_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:ciscoIfExtensionTableIntfGroup.setStatus(_B)
ciscoIfExtensionTableIntfGroup1=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,3))
ciscoIfExtensionTableIntfGroup1.setObjects(*((_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:ciscoIfExtensionTableIntfGroup1.setStatus(_E)
ciscoIfExtensionSystemGroup=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,4))
ciscoIfExtensionSystemGroup.setObjects((_A,_AK))
if mibBuilder.loadTexts:ciscoIfExtensionSystemGroup.setStatus(_B)
ciscoIfExtDot1qEtherTypeGroup=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,5))
ciscoIfExtDot1qEtherTypeGroup.setObjects(*((_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:ciscoIfExtDot1qEtherTypeGroup.setStatus(_B)
ciscoIfExtUtilizationGroup=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,6))
ciscoIfExtUtilizationGroup.setObjects(*((_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ)))
if mibBuilder.loadTexts:ciscoIfExtUtilizationGroup.setStatus(_B)
ciscoIfExtDot1dBaseMappingGroup=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,7))
ciscoIfExtDot1dBaseMappingGroup.setObjects((_A,_AR))
if mibBuilder.loadTexts:ciscoIfExtDot1dBaseMappingGroup.setStatus(_B)
ciscoIfExtIfNameMappingGroup=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,8))
ciscoIfExtIfNameMappingGroup.setObjects((_A,_AS))
if mibBuilder.loadTexts:ciscoIfExtIfNameMappingGroup.setStatus(_B)
ciscoIfExtensionTableIntfGroup2=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,9))
ciscoIfExtensionTableIntfGroup2.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_s)))
if mibBuilder.loadTexts:ciscoIfExtensionTableIntfGroup2.setStatus(_E)
cieIfStatusListGroup=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,10))
cieIfStatusListGroup.setObjects(*((_A,_AT),(_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:cieIfStatusListGroup.setStatus(_B)
cieLinkUpDownNotifEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,11))
cieLinkUpDownNotifEnableGroup.setObjects(*((_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:cieLinkUpDownNotifEnableGroup.setStatus(_E)
ciscoIfExtensionAsymmetricalSpeedGroup=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,13))
ciscoIfExtensionAsymmetricalSpeedGroup.setObjects(*((_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:ciscoIfExtensionAsymmetricalSpeedGroup.setStatus(_B)
ciscoIfExtUtilIntervalGroup=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,14))
ciscoIfExtUtilIntervalGroup.setObjects((_A,_Aa))
if mibBuilder.loadTexts:ciscoIfExtUtilIntervalGroup.setStatus(_B)
cieIfIndexPersistenceGroup=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,15))
cieIfIndexPersistenceGroup.setObjects(*((_A,_Ab),(_A,_Ac)))
if mibBuilder.loadTexts:cieIfIndexPersistenceGroup.setStatus(_E)
cieDelayedLinkUpDownNotifNotifEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,16))
cieDelayedLinkUpDownNotifNotifEnableGroup.setObjects(*((_A,_Ad),(_A,_Ae)))
if mibBuilder.loadTexts:cieDelayedLinkUpDownNotifNotifEnableGroup.setStatus(_B)
cieIfIndexPersistenceControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,18))
cieIfIndexPersistenceControlGroup.setObjects(*((_A,_Af),(_A,_Ag)))
if mibBuilder.loadTexts:cieIfIndexPersistenceControlGroup.setStatus(_B)
ciscoIfExtensionTableIntfGroup3=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,19))
ciscoIfExtensionTableIntfGroup3.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_s),(_A,_Ah)))
if mibBuilder.loadTexts:ciscoIfExtensionTableIntfGroup3.setStatus(_B)
cieIfStatusListGroupSup1=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,20))
cieIfStatusListGroupSup1.setObjects((_A,_Ai))
if mibBuilder.loadTexts:cieIfStatusListGroupSup1.setStatus(_B)
cieIfVlStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,21))
cieIfVlStatsGroup.setObjects(*((_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq)))
if mibBuilder.loadTexts:cieIfVlStatsGroup.setStatus(_B)
ciscoIfExtensionTableIntfGroup3SupR01=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,22))
ciscoIfExtensionTableIntfGroup3SupR01.setObjects(*((_A,_Ar),(_A,_As)))
if mibBuilder.loadTexts:ciscoIfExtensionTableIntfGroup3SupR01.setStatus(_B)
cieLinkUpDownNotifConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,23))
cieLinkUpDownNotifConfigGroup.setObjects((_A,_At))
if mibBuilder.loadTexts:cieLinkUpDownNotifConfigGroup.setStatus(_B)
ciscoIfExtensionTableIntfGroup3SupR02=ObjectGroup((1,3,6,1,4,1,9,9,276,2,2,24))
ciscoIfExtensionTableIntfGroup3SupR02.setObjects(*((_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax)))
if mibBuilder.loadTexts:ciscoIfExtensionTableIntfGroup3SupR02.setStatus(_B)
cieLinkDown=NotificationType((1,3,6,1,4,1,9,9,276,0,1))
cieLinkDown.setObjects(*((_F,_R),(_F,_b),(_F,_d),(_F,_c),(_F,_e)))
if mibBuilder.loadTexts:cieLinkDown.setStatus(_B)
cieLinkUp=NotificationType((1,3,6,1,4,1,9,9,276,0,2))
cieLinkUp.setObjects(*((_F,_R),(_F,_b),(_F,_d),(_F,_c),(_F,_e)))
if mibBuilder.loadTexts:cieLinkUp.setStatus(_B)
cieDelayedLinkUpDownNotif=NotificationType((1,3,6,1,4,1,9,9,276,0,3))
cieDelayedLinkUpDownNotif.setObjects(*((_F,_b),(_F,_d),(_F,_c),(_F,_e),(_A,_j)))
if mibBuilder.loadTexts:cieDelayedLinkUpDownNotif.setStatus(_B)
cieLinkUpDownNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,276,2,2,12))
cieLinkUpDownNotifGroup.setObjects(*((_A,_Ay),(_A,_Az)))
if mibBuilder.loadTexts:cieLinkUpDownNotifGroup.setStatus(_B)
cieDelayedLinkUpDownNotifNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,276,2,2,17))
cieDelayedLinkUpDownNotifNotifGroup.setObjects((_A,_A_))
if mibBuilder.loadTexts:cieDelayedLinkUpDownNotifNotifGroup.setStatus(_B)
ciscoIfExtensionMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,276,2,1,1))
ciscoIfExtensionMIBCompliance.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ciscoIfExtensionMIBCompliance.setStatus(_E)
ciscoIfExtensionMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,276,2,1,2))
ciscoIfExtensionMIBCompliance1.setObjects(*((_A,_G),(_A,_H),(_A,_k),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:ciscoIfExtensionMIBCompliance1.setStatus(_E)
ciscoIfExtensionMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,276,2,1,3))
ciscoIfExtensionMIBCompliance2.setObjects(*((_A,_G),(_A,_H),(_A,_k),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoIfExtensionMIBCompliance2.setStatus(_E)
ciscoIfExtensionMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,276,2,1,4))
ciscoIfExtensionMIBCompliance3.setObjects(*((_A,_G),(_A,_H),(_A,_k),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:ciscoIfExtensionMIBCompliance3.setStatus(_E)
ciscoIfExtensionMIBCompliance4=ModuleCompliance((1,3,6,1,4,1,9,9,276,2,1,5))
ciscoIfExtensionMIBCompliance4.setObjects(*((_A,_G),(_A,_H),(_A,_U),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_O)))
if mibBuilder.loadTexts:ciscoIfExtensionMIBCompliance4.setStatus(_E)
ciscoIfExtensionMIBCompliance5=ModuleCompliance((1,3,6,1,4,1,9,9,276,2,1,6))
ciscoIfExtensionMIBCompliance5.setObjects(*((_A,_G),(_A,_H),(_A,_U),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_O),(_A,_S),(_A,_P)))
if mibBuilder.loadTexts:ciscoIfExtensionMIBCompliance5.setStatus(_E)
ciscoIfExtensionMIBCompliance6=ModuleCompliance((1,3,6,1,4,1,9,9,276,2,1,7))
ciscoIfExtensionMIBCompliance6.setObjects(*((_A,_G),(_A,_H),(_A,_U),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_O),(_A,_S),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciscoIfExtensionMIBCompliance6.setStatus(_E)
ciscoIfExtensionMIBCompliance7=ModuleCompliance((1,3,6,1,4,1,9,9,276,2,1,8))
ciscoIfExtensionMIBCompliance7.setObjects(*((_A,_G),(_A,_H),(_A,_U),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_O),(_A,_S),(_A,_P),(_A,_Q),(_A,_T)))
if mibBuilder.loadTexts:ciscoIfExtensionMIBCompliance7.setStatus(_E)
ciscoIfExtensionMIBCompliance8=ModuleCompliance((1,3,6,1,4,1,9,9,276,2,1,9))
ciscoIfExtensionMIBCompliance8.setObjects(*((_A,_G),(_A,_H),(_A,_U),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_O),(_A,_S),(_A,_P),(_A,_Q),(_A,_T),(_A,_B0)))
if mibBuilder.loadTexts:ciscoIfExtensionMIBCompliance8.setStatus(_E)
ciscoIfExtensionMIBCompliance9=ModuleCompliance((1,3,6,1,4,1,9,9,276,2,1,10))
ciscoIfExtensionMIBCompliance9.setObjects(*((_A,_G),(_A,_H),(_A,_U),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_O),(_A,_S),(_A,_P),(_A,_Q),(_A,_T),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:ciscoIfExtensionMIBCompliance9.setStatus(_E)
ciscoIfExtensionMIBCompliance10=ModuleCompliance((1,3,6,1,4,1,9,9,276,2,1,11))
ciscoIfExtensionMIBCompliance10.setObjects(*((_A,_G),(_A,_H),(_A,_U),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_O),(_A,_S),(_A,_P),(_A,_Q),(_A,_T),(_A,_V),(_A,_W),(_A,_Y)))
if mibBuilder.loadTexts:ciscoIfExtensionMIBCompliance10.setStatus(_E)
ciscoIfExtensionMIBCompliance11=ModuleCompliance((1,3,6,1,4,1,9,9,276,2,1,12))
ciscoIfExtensionMIBCompliance11.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_O),(_A,_S),(_A,_P),(_A,_Q),(_A,_T),(_A,_V),(_A,_W),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:ciscoIfExtensionMIBCompliance11.setStatus(_E)
ciscoIfExtensionMIBCompliance12=ModuleCompliance((1,3,6,1,4,1,9,9,276,2,1,13))
ciscoIfExtensionMIBCompliance12.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_S),(_A,_P),(_A,_Q),(_A,_T),(_A,_V),(_A,_W),(_A,_Y),(_A,_Z),(_A,_O),(_A,_a)))
if mibBuilder.loadTexts:ciscoIfExtensionMIBCompliance12.setStatus(_E)
ciscoIfExtensionMIBCompliance13=ModuleCompliance((1,3,6,1,4,1,9,9,276,2,1,14))
ciscoIfExtensionMIBCompliance13.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_S),(_A,_P),(_A,_Q),(_A,_T),(_A,_V),(_A,_W),(_A,_Y),(_A,_O),(_A,_a),(_A,_l),(_A,_Z),(_A,_m)))
if mibBuilder.loadTexts:ciscoIfExtensionMIBCompliance13.setStatus(_E)
ciscoIfExtensionMIBCompliance14=ModuleCompliance((1,3,6,1,4,1,9,9,276,2,1,15))
ciscoIfExtensionMIBCompliance14.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_P),(_A,_Q),(_A,_T),(_A,_V),(_A,_W),(_A,_Y),(_A,_O),(_A,_a),(_A,_l),(_A,_Z),(_A,_m),(_A,_t)))
if mibBuilder.loadTexts:ciscoIfExtensionMIBCompliance14.setStatus(_E)
ciscoIfExtensionMIBCompliance15=ModuleCompliance((1,3,6,1,4,1,9,9,276,2,1,16))
ciscoIfExtensionMIBCompliance15.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_P),(_A,_Q),(_A,_T),(_A,_V),(_A,_W),(_A,_Y),(_A,_O),(_A,_a),(_A,_l),(_A,_Z),(_A,_m),(_A,_B1),(_A,_t)))
if mibBuilder.loadTexts:ciscoIfExtensionMIBCompliance15.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'InterfaceIndexList':InterfaceIndexList,'InterfaceOperModeList':InterfaceOperModeList,'InterfaceOperCauseList':InterfaceOperCauseList,'InterfaceOwnershipList':InterfaceOwnershipList,_r:IfIndexPersistenceState,'ciscoIfExtensionMIB':ciscoIfExtensionMIB,'ciscoIfExtensionMIBNotifications':ciscoIfExtensionMIBNotifications,_Ay:cieLinkDown,_Az:cieLinkUp,_A_:cieDelayedLinkUpDownNotif,'ciscoIfExtensionMIBObjects':ciscoIfExtensionMIBObjects,'ciscoIfExtensionStats':ciscoIfExtensionStats,'cieIfPacketStatsTable':cieIfPacketStatsTable,'cieIfPacketStatsEntry':cieIfPacketStatsEntry,_A3:cieIfLastInTime,_A4:cieIfLastOutTime,_A5:cieIfLastOutHangTime,_A6:cieIfInRuntsErrs,_A7:cieIfInGiantsErrs,_A8:cieIfInFramingErrs,_A9:cieIfInOverrunErrs,_AA:cieIfInIgnored,_AB:cieIfInAbortErrs,_AC:cieIfInputQueueDrops,_AD:cieIfOutputQueueDrops,_AE:cieIfPacketDiscontinuityTime,'cieIfInterfaceTable':cieIfInterfaceTable,'cieIfInterfaceEntry':cieIfInterfaceEntry,_AF:cieIfResetCount,_AG:cieIfKeepAliveEnabled,_AH:cieIfStateChangeReason,_AI:cieIfCarrierTransitionCount,_AJ:cieIfInterfaceDiscontinuityTime,_g:cieIfDhcpMode,_h:cieIfMtu,_i:cieIfContextName,_j:cieIfOperStatusCause,_s:cieIfOperStatusCauseDescr,_AY:cieIfSpeedReceive,_AZ:cieIfHighSpeedReceive,_Ah:cieIfOwner,_Ar:cieIfSharedConfig,_As:cieIfSpeedGroupConfig,_Au:cieIfTransceiverFrequencyConfig,_Av:cieIfFillPatternConfig,_Aw:cieIfIgnoreBitErrorsConfig,_Ax:cieIfIgnoreInterruptThresholdConfig,'cieIfDuplexCfgStatus':cieIfDuplexCfgStatus,'cieIfDuplexDetectStatus':cieIfDuplexDetectStatus,'cieIfStatusListTable':cieIfStatusListTable,'cieIfStatusListEntry':cieIfStatusListEntry,_x:cieIfStatusListIndex,_AT:cieInterfacesIndex,_AU:cieInterfacesOperMode,_AV:cieInterfacesOperCause,_Ai:cieInterfaceOwnershipBitmap,'cieIfVlStatsTable':cieIfVlStatsTable,'cieIfVlStatsEntry':cieIfVlStatsEntry,_Aj:cieIfNoDropVlInPkts,_Ak:cieIfNoDropVlInOctets,_Al:cieIfNoDropVlOutPkts,_Am:cieIfNoDropVlOutOctets,_An:cieIfDropVlInPkts,_Ao:cieIfDropVlInOctets,_Ap:cieIfDropVlOutPkts,_Aq:cieIfDropVlOutOctets,'ciscoIfExtSystemConfig':ciscoIfExtSystemConfig,_AK:cieSystemMtu,_AW:cieLinkUpDownEnable,_AX:cieStandardLinkUpDownVarbinds,_Ab:cieIfIndexPersistence,'cieIfIndexPersistenceTable':cieIfIndexPersistenceTable,'cieIfIndexPersistenceEntry':cieIfIndexPersistenceEntry,_Ac:cieIfIndexPersistenceEnabled,_Ag:cieIfIndexPersistenceControl,_Ad:cieDelayedLinkUpDownNotifEnable,_Ae:cieDelayedLinkUpDownNotifDelay,_Af:cieIfIndexGlobalPersistence,_At:cieLinkUpDownConfig,'ciscoIfExtDot1qCustomEtherType':ciscoIfExtDot1qCustomEtherType,'cieIfDot1qCustomEtherTypeTable':cieIfDot1qCustomEtherTypeTable,'cieIfDot1qCustomEtherTypeEntry':cieIfDot1qCustomEtherTypeEntry,_AL:cieIfDot1qCustomAdminEtherType,_AM:cieIfDot1qCustomOperEtherType,'ciscoIfExtUtilization':ciscoIfExtUtilization,'cieIfUtilTable':cieIfUtilTable,'cieIfUtilEntry':cieIfUtilEntry,_AN:cieIfInPktRate,_AO:cieIfInOctetRate,_AP:cieIfOutPktRate,_AQ:cieIfOutOctetRate,_Aa:cieIfInterval,'ciscoIfExtDot1dBaseMapping':ciscoIfExtDot1dBaseMapping,'cieIfDot1dBaseMappingTable':cieIfDot1dBaseMappingTable,'cieIfDot1dBaseMappingEntry':cieIfDot1dBaseMappingEntry,_AR:cieIfDot1dBaseMappingPort,'ciscoIfExtIfNameMapping':ciscoIfExtIfNameMapping,'cieIfNameMappingTable':cieIfNameMappingTable,'cieIfNameMappingEntry':cieIfNameMappingEntry,_A2:cieIfName,_AS:cieIfIndex,'ciscoIfExtensionMIBConformance':ciscoIfExtensionMIBConformance,'ciscoIfExtensionMIBCompliances':ciscoIfExtensionMIBCompliances,'ciscoIfExtensionMIBCompliance':ciscoIfExtensionMIBCompliance,'ciscoIfExtensionMIBCompliance1':ciscoIfExtensionMIBCompliance1,'ciscoIfExtensionMIBCompliance2':ciscoIfExtensionMIBCompliance2,'ciscoIfExtensionMIBCompliance3':ciscoIfExtensionMIBCompliance3,'ciscoIfExtensionMIBCompliance4':ciscoIfExtensionMIBCompliance4,'ciscoIfExtensionMIBCompliance5':ciscoIfExtensionMIBCompliance5,'ciscoIfExtensionMIBCompliance6':ciscoIfExtensionMIBCompliance6,'ciscoIfExtensionMIBCompliance7':ciscoIfExtensionMIBCompliance7,'ciscoIfExtensionMIBCompliance8':ciscoIfExtensionMIBCompliance8,'ciscoIfExtensionMIBCompliance9':ciscoIfExtensionMIBCompliance9,'ciscoIfExtensionMIBCompliance10':ciscoIfExtensionMIBCompliance10,'ciscoIfExtensionMIBCompliance11':ciscoIfExtensionMIBCompliance11,'ciscoIfExtensionMIBCompliance12':ciscoIfExtensionMIBCompliance12,'ciscoIfExtensionMIBCompliance13':ciscoIfExtensionMIBCompliance13,'ciscoIfExtensionMIBCompliance14':ciscoIfExtensionMIBCompliance14,'ciscoIfExtensionMIBCompliance15':ciscoIfExtensionMIBCompliance15,'ciscoIfExtensionMIBGroups':ciscoIfExtensionMIBGroups,_G:ciscoIfExtensionTablePacketGroup,_H:ciscoIfExtensionTableIntfGroup,_k:ciscoIfExtensionTableIntfGroup1,_I:ciscoIfExtensionSystemGroup,_J:ciscoIfExtDot1qEtherTypeGroup,_K:ciscoIfExtUtilizationGroup,_L:ciscoIfExtDot1dBaseMappingGroup,_M:ciscoIfExtIfNameMappingGroup,_U:ciscoIfExtensionTableIntfGroup2,_O:cieIfStatusListGroup,_S:cieLinkUpDownNotifEnableGroup,_P:cieLinkUpDownNotifGroup,_Q:ciscoIfExtensionAsymmetricalSpeedGroup,_T:ciscoIfExtUtilIntervalGroup,_B0:cieIfIndexPersistenceGroup,_W:cieDelayedLinkUpDownNotifNotifEnableGroup,_V:cieDelayedLinkUpDownNotifNotifGroup,_Y:cieIfIndexPersistenceControlGroup,_Z:ciscoIfExtensionTableIntfGroup3,_a:cieIfStatusListGroupSup1,_l:cieIfVlStatsGroup,_m:ciscoIfExtensionTableIntfGroup3SupR01,_t:cieLinkUpDownNotifConfigGroup,_B1:ciscoIfExtensionTableIntfGroup3SupR02})