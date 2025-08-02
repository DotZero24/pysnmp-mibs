_AD='isdnMibDirectoryGroup'
_AC='isdnMibEndpointGroup'
_AB='isdnMibBasicRateGroup'
_AA='isdnMibNotificationsGroup'
_A9='isdnMibBearerGroup'
_A8='isdnMibSignalingGroup'
_A7='isdnMibCallInformation'
_A6='isdnDirectoryStatus'
_A5='isdnDirectorySigIndex'
_A4='isdnDirectoryNumber'
_A3='isdnEndpointStatus'
_A2='isdnEndpointSpid'
_A1='isdnEndpointTeiValue'
_A0='isdnEndpointTeiType'
_z='isdnEndpointIfType'
_y='isdnEndpointIfIndex'
_x='isdnEndpointGetIndex'
_w='isdnLapdRecvdFrmr'
_v='isdnLapdPeerSabme'
_u='isdnLapdOperStatus'
_t='isdnLapdPrimaryChannel'
_s='isdnSigStatsChargedUnits'
_r='isdnSigStatsOutConnected'
_q='isdnSigStatsOutCalls'
_p='isdnSigStatsInConnected'
_o='isdnSigStatsInCalls'
_n='isdnSignalingStatus'
_m='isdnSignalingInfoTrapEnable'
_l='isdnSignalingBchannelCount'
_k='isdnSignalingSubAddress'
_j='isdnSignalingCallingAddress'
_i='isdnSignalingProtocol'
_h='isdnSignalingIfIndex'
_g='isdnSignalingGetIndex'
_f='isdnBearerChargedUnits'
_e='isdnBearerCallConnectTime'
_d='isdnBearerMultirate'
_c='isdnBearerChannelNumber'
_b='isdnBearerChannelType'
_a='isdnBasicRateSignalMode'
_Z='isdnBasicRateIfMode'
_Y='isdnBasicRateLineTopology'
_X='isdnBasicRateIfType'
_W='isdnSignalingStatsEntry'
_V='isdnDirectoryIndex'
_U='isdnEndpointIndex'
_T='isdnSignalingIndex'
_S='unknown'
_R='inactive'
_Q='active'
_P='isdnBearerCallSetupTime'
_O='isdnBearerInfoType'
_N='isdnBearerCallOrigin'
_M='isdnBearerPeerSubAddress'
_L='isdnBearerPeerAddress'
_K='isdnBearerOperStatus'
_J='not-accessible'
_I='DisplayString'
_H='ifIndex'
_G='IF-MIB'
_F='read-write'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='ISDN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_G,'InterfaceIndex',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention','TestAndIncr','TimeStamp','TruthValue')
isdnMib=ModuleIdentity((1,3,6,1,2,1,10,20))
class IsdnSignalingProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)));namedValues=NamedValues(*(('other',1),('dss1',2),('etsi',3),('dass2',4),('ess4',5),('ess5',6),('dms100',7),('dms250',8),('ni1',9),('ni2',10),('ni3',11),('vn2',12),('vn3',13),('vn4',14),('vn6',15),('kdd',16),('ins64',17),('ins1500',18),('itr6',19),('cornet',20),('ts013',21),('ts014',22),('qsig',23),('swissnet2',24),('swissnet3',25)))
_IsdnMibObjects_ObjectIdentity=ObjectIdentity
isdnMibObjects=_IsdnMibObjects_ObjectIdentity((1,3,6,1,2,1,10,20,1))
_IsdnBasicRateGroup_ObjectIdentity=ObjectIdentity
isdnBasicRateGroup=_IsdnBasicRateGroup_ObjectIdentity((1,3,6,1,2,1,10,20,1,1))
_IsdnBasicRateTable_Object=MibTable
isdnBasicRateTable=_IsdnBasicRateTable_Object((1,3,6,1,2,1,10,20,1,1,1))
if mibBuilder.loadTexts:isdnBasicRateTable.setStatus(_A)
_IsdnBasicRateEntry_Object=MibTableRow
isdnBasicRateEntry=_IsdnBasicRateEntry_Object((1,3,6,1,2,1,10,20,1,1,1,1))
isdnBasicRateEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:isdnBasicRateEntry.setStatus(_A)
class _IsdnBasicRateIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(75,76)));namedValues=NamedValues(*(('isdns',75),('isdnu',76)))
_IsdnBasicRateIfType_Type.__name__=_D
_IsdnBasicRateIfType_Object=MibTableColumn
isdnBasicRateIfType=_IsdnBasicRateIfType_Object((1,3,6,1,2,1,10,20,1,1,1,1,1),_IsdnBasicRateIfType_Type())
isdnBasicRateIfType.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnBasicRateIfType.setStatus(_A)
class _IsdnBasicRateLineTopology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pointToPoint',1),('pointToMultipoint',2)))
_IsdnBasicRateLineTopology_Type.__name__=_D
_IsdnBasicRateLineTopology_Object=MibTableColumn
isdnBasicRateLineTopology=_IsdnBasicRateLineTopology_Object((1,3,6,1,2,1,10,20,1,1,1,1,2),_IsdnBasicRateLineTopology_Type())
isdnBasicRateLineTopology.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnBasicRateLineTopology.setStatus(_A)
class _IsdnBasicRateIfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('te',1),('nt',2)))
_IsdnBasicRateIfMode_Type.__name__=_D
_IsdnBasicRateIfMode_Object=MibTableColumn
isdnBasicRateIfMode=_IsdnBasicRateIfMode_Object((1,3,6,1,2,1,10,20,1,1,1,1,3),_IsdnBasicRateIfMode_Type())
isdnBasicRateIfMode.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnBasicRateIfMode.setStatus(_A)
class _IsdnBasicRateSignalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_IsdnBasicRateSignalMode_Type.__name__=_D
_IsdnBasicRateSignalMode_Object=MibTableColumn
isdnBasicRateSignalMode=_IsdnBasicRateSignalMode_Object((1,3,6,1,2,1,10,20,1,1,1,1,4),_IsdnBasicRateSignalMode_Type())
isdnBasicRateSignalMode.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnBasicRateSignalMode.setStatus(_A)
_IsdnBearerGroup_ObjectIdentity=ObjectIdentity
isdnBearerGroup=_IsdnBearerGroup_ObjectIdentity((1,3,6,1,2,1,10,20,1,2))
_IsdnBearerTable_Object=MibTable
isdnBearerTable=_IsdnBearerTable_Object((1,3,6,1,2,1,10,20,1,2,1))
if mibBuilder.loadTexts:isdnBearerTable.setStatus(_A)
_IsdnBearerEntry_Object=MibTableRow
isdnBearerEntry=_IsdnBearerEntry_Object((1,3,6,1,2,1,10,20,1,2,1,1))
isdnBearerEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:isdnBearerEntry.setStatus(_A)
class _IsdnBearerChannelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dialup',1),('leased',2)))
_IsdnBearerChannelType_Type.__name__=_D
_IsdnBearerChannelType_Object=MibTableColumn
isdnBearerChannelType=_IsdnBearerChannelType_Object((1,3,6,1,2,1,10,20,1,2,1,1,1),_IsdnBearerChannelType_Type())
isdnBearerChannelType.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnBearerChannelType.setStatus(_A)
class _IsdnBearerOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),('connecting',2),('connected',3),(_Q,4)))
_IsdnBearerOperStatus_Type.__name__=_D
_IsdnBearerOperStatus_Object=MibTableColumn
isdnBearerOperStatus=_IsdnBearerOperStatus_Object((1,3,6,1,2,1,10,20,1,2,1,1,2),_IsdnBearerOperStatus_Type())
isdnBearerOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnBearerOperStatus.setStatus(_A)
class _IsdnBearerChannelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_IsdnBearerChannelNumber_Type.__name__=_D
_IsdnBearerChannelNumber_Object=MibTableColumn
isdnBearerChannelNumber=_IsdnBearerChannelNumber_Object((1,3,6,1,2,1,10,20,1,2,1,1,3),_IsdnBearerChannelNumber_Type())
isdnBearerChannelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnBearerChannelNumber.setStatus(_A)
_IsdnBearerPeerAddress_Type=DisplayString
_IsdnBearerPeerAddress_Object=MibTableColumn
isdnBearerPeerAddress=_IsdnBearerPeerAddress_Object((1,3,6,1,2,1,10,20,1,2,1,1,4),_IsdnBearerPeerAddress_Type())
isdnBearerPeerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnBearerPeerAddress.setStatus(_A)
_IsdnBearerPeerSubAddress_Type=DisplayString
_IsdnBearerPeerSubAddress_Object=MibTableColumn
isdnBearerPeerSubAddress=_IsdnBearerPeerSubAddress_Object((1,3,6,1,2,1,10,20,1,2,1,1,5),_IsdnBearerPeerSubAddress_Type())
isdnBearerPeerSubAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnBearerPeerSubAddress.setStatus(_A)
class _IsdnBearerCallOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),('originate',2),('answer',3),('callback',4)))
_IsdnBearerCallOrigin_Type.__name__=_D
_IsdnBearerCallOrigin_Object=MibTableColumn
isdnBearerCallOrigin=_IsdnBearerCallOrigin_Object((1,3,6,1,2,1,10,20,1,2,1,1,6),_IsdnBearerCallOrigin_Type())
isdnBearerCallOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnBearerCallOrigin.setStatus(_A)
class _IsdnBearerInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_S,1),('speech',2),('unrestrictedDigital',3),('unrestrictedDigital56',4),('restrictedDigital',5),('audio31',6),('audio7',7),('video',8),('packetSwitched',9)))
_IsdnBearerInfoType_Type.__name__=_D
_IsdnBearerInfoType_Object=MibTableColumn
isdnBearerInfoType=_IsdnBearerInfoType_Object((1,3,6,1,2,1,10,20,1,2,1,1,7),_IsdnBearerInfoType_Type())
isdnBearerInfoType.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnBearerInfoType.setStatus(_A)
_IsdnBearerMultirate_Type=TruthValue
_IsdnBearerMultirate_Object=MibTableColumn
isdnBearerMultirate=_IsdnBearerMultirate_Object((1,3,6,1,2,1,10,20,1,2,1,1,8),_IsdnBearerMultirate_Type())
isdnBearerMultirate.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnBearerMultirate.setStatus(_A)
_IsdnBearerCallSetupTime_Type=TimeStamp
_IsdnBearerCallSetupTime_Object=MibTableColumn
isdnBearerCallSetupTime=_IsdnBearerCallSetupTime_Object((1,3,6,1,2,1,10,20,1,2,1,1,9),_IsdnBearerCallSetupTime_Type())
isdnBearerCallSetupTime.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnBearerCallSetupTime.setStatus(_A)
_IsdnBearerCallConnectTime_Type=TimeStamp
_IsdnBearerCallConnectTime_Object=MibTableColumn
isdnBearerCallConnectTime=_IsdnBearerCallConnectTime_Object((1,3,6,1,2,1,10,20,1,2,1,1,10),_IsdnBearerCallConnectTime_Type())
isdnBearerCallConnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnBearerCallConnectTime.setStatus(_A)
_IsdnBearerChargedUnits_Type=Gauge32
_IsdnBearerChargedUnits_Object=MibTableColumn
isdnBearerChargedUnits=_IsdnBearerChargedUnits_Object((1,3,6,1,2,1,10,20,1,2,1,1,11),_IsdnBearerChargedUnits_Type())
isdnBearerChargedUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnBearerChargedUnits.setStatus(_A)
_IsdnSignalingGroup_ObjectIdentity=ObjectIdentity
isdnSignalingGroup=_IsdnSignalingGroup_ObjectIdentity((1,3,6,1,2,1,10,20,1,3))
_IsdnSignalingGetIndex_Type=TestAndIncr
_IsdnSignalingGetIndex_Object=MibScalar
isdnSignalingGetIndex=_IsdnSignalingGetIndex_Object((1,3,6,1,2,1,10,20,1,3,1),_IsdnSignalingGetIndex_Type())
isdnSignalingGetIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnSignalingGetIndex.setStatus(_A)
_IsdnSignalingTable_Object=MibTable
isdnSignalingTable=_IsdnSignalingTable_Object((1,3,6,1,2,1,10,20,1,3,2))
if mibBuilder.loadTexts:isdnSignalingTable.setStatus(_A)
_IsdnSignalingEntry_Object=MibTableRow
isdnSignalingEntry=_IsdnSignalingEntry_Object((1,3,6,1,2,1,10,20,1,3,2,1))
isdnSignalingEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:isdnSignalingEntry.setStatus(_A)
class _IsdnSignalingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IsdnSignalingIndex_Type.__name__=_D
_IsdnSignalingIndex_Object=MibTableColumn
isdnSignalingIndex=_IsdnSignalingIndex_Object((1,3,6,1,2,1,10,20,1,3,2,1,1),_IsdnSignalingIndex_Type())
isdnSignalingIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:isdnSignalingIndex.setStatus(_A)
_IsdnSignalingIfIndex_Type=InterfaceIndex
_IsdnSignalingIfIndex_Object=MibTableColumn
isdnSignalingIfIndex=_IsdnSignalingIfIndex_Object((1,3,6,1,2,1,10,20,1,3,2,1,2),_IsdnSignalingIfIndex_Type())
isdnSignalingIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnSignalingIfIndex.setStatus(_A)
_IsdnSignalingProtocol_Type=IsdnSignalingProtocol
_IsdnSignalingProtocol_Object=MibTableColumn
isdnSignalingProtocol=_IsdnSignalingProtocol_Object((1,3,6,1,2,1,10,20,1,3,2,1,3),_IsdnSignalingProtocol_Type())
isdnSignalingProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnSignalingProtocol.setStatus(_A)
class _IsdnSignalingCallingAddress_Type(DisplayString):defaultValue=OctetString('')
_IsdnSignalingCallingAddress_Type.__name__=_I
_IsdnSignalingCallingAddress_Object=MibTableColumn
isdnSignalingCallingAddress=_IsdnSignalingCallingAddress_Object((1,3,6,1,2,1,10,20,1,3,2,1,4),_IsdnSignalingCallingAddress_Type())
isdnSignalingCallingAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnSignalingCallingAddress.setStatus(_A)
class _IsdnSignalingSubAddress_Type(DisplayString):defaultValue=OctetString('')
_IsdnSignalingSubAddress_Type.__name__=_I
_IsdnSignalingSubAddress_Object=MibTableColumn
isdnSignalingSubAddress=_IsdnSignalingSubAddress_Object((1,3,6,1,2,1,10,20,1,3,2,1,5),_IsdnSignalingSubAddress_Type())
isdnSignalingSubAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnSignalingSubAddress.setStatus(_A)
class _IsdnSignalingBchannelCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IsdnSignalingBchannelCount_Type.__name__=_D
_IsdnSignalingBchannelCount_Object=MibTableColumn
isdnSignalingBchannelCount=_IsdnSignalingBchannelCount_Object((1,3,6,1,2,1,10,20,1,3,2,1,6),_IsdnSignalingBchannelCount_Type())
isdnSignalingBchannelCount.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnSignalingBchannelCount.setStatus(_A)
class _IsdnSignalingInfoTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_IsdnSignalingInfoTrapEnable_Type.__name__=_D
_IsdnSignalingInfoTrapEnable_Object=MibTableColumn
isdnSignalingInfoTrapEnable=_IsdnSignalingInfoTrapEnable_Object((1,3,6,1,2,1,10,20,1,3,2,1,7),_IsdnSignalingInfoTrapEnable_Type())
isdnSignalingInfoTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnSignalingInfoTrapEnable.setStatus(_A)
_IsdnSignalingStatus_Type=RowStatus
_IsdnSignalingStatus_Object=MibTableColumn
isdnSignalingStatus=_IsdnSignalingStatus_Object((1,3,6,1,2,1,10,20,1,3,2,1,8),_IsdnSignalingStatus_Type())
isdnSignalingStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnSignalingStatus.setStatus(_A)
_IsdnSignalingStatsTable_Object=MibTable
isdnSignalingStatsTable=_IsdnSignalingStatsTable_Object((1,3,6,1,2,1,10,20,1,3,3))
if mibBuilder.loadTexts:isdnSignalingStatsTable.setStatus(_A)
_IsdnSignalingStatsEntry_Object=MibTableRow
isdnSignalingStatsEntry=_IsdnSignalingStatsEntry_Object((1,3,6,1,2,1,10,20,1,3,3,1))
if mibBuilder.loadTexts:isdnSignalingStatsEntry.setStatus(_A)
_IsdnSigStatsInCalls_Type=Counter32
_IsdnSigStatsInCalls_Object=MibTableColumn
isdnSigStatsInCalls=_IsdnSigStatsInCalls_Object((1,3,6,1,2,1,10,20,1,3,3,1,1),_IsdnSigStatsInCalls_Type())
isdnSigStatsInCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnSigStatsInCalls.setStatus(_A)
_IsdnSigStatsInConnected_Type=Counter32
_IsdnSigStatsInConnected_Object=MibTableColumn
isdnSigStatsInConnected=_IsdnSigStatsInConnected_Object((1,3,6,1,2,1,10,20,1,3,3,1,2),_IsdnSigStatsInConnected_Type())
isdnSigStatsInConnected.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnSigStatsInConnected.setStatus(_A)
_IsdnSigStatsOutCalls_Type=Counter32
_IsdnSigStatsOutCalls_Object=MibTableColumn
isdnSigStatsOutCalls=_IsdnSigStatsOutCalls_Object((1,3,6,1,2,1,10,20,1,3,3,1,3),_IsdnSigStatsOutCalls_Type())
isdnSigStatsOutCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnSigStatsOutCalls.setStatus(_A)
_IsdnSigStatsOutConnected_Type=Counter32
_IsdnSigStatsOutConnected_Object=MibTableColumn
isdnSigStatsOutConnected=_IsdnSigStatsOutConnected_Object((1,3,6,1,2,1,10,20,1,3,3,1,4),_IsdnSigStatsOutConnected_Type())
isdnSigStatsOutConnected.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnSigStatsOutConnected.setStatus(_A)
_IsdnSigStatsChargedUnits_Type=Counter32
_IsdnSigStatsChargedUnits_Object=MibTableColumn
isdnSigStatsChargedUnits=_IsdnSigStatsChargedUnits_Object((1,3,6,1,2,1,10,20,1,3,3,1,5),_IsdnSigStatsChargedUnits_Type())
isdnSigStatsChargedUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnSigStatsChargedUnits.setStatus(_A)
_IsdnLapdTable_Object=MibTable
isdnLapdTable=_IsdnLapdTable_Object((1,3,6,1,2,1,10,20,1,3,4))
if mibBuilder.loadTexts:isdnLapdTable.setStatus(_A)
_IsdnLapdEntry_Object=MibTableRow
isdnLapdEntry=_IsdnLapdEntry_Object((1,3,6,1,2,1,10,20,1,3,4,1))
isdnLapdEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:isdnLapdEntry.setStatus(_A)
_IsdnLapdPrimaryChannel_Type=TruthValue
_IsdnLapdPrimaryChannel_Object=MibTableColumn
isdnLapdPrimaryChannel=_IsdnLapdPrimaryChannel_Object((1,3,6,1,2,1,10,20,1,3,4,1,1),_IsdnLapdPrimaryChannel_Type())
isdnLapdPrimaryChannel.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnLapdPrimaryChannel.setStatus(_A)
class _IsdnLapdOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('l1Active',2),('l2Active',3)))
_IsdnLapdOperStatus_Type.__name__=_D
_IsdnLapdOperStatus_Object=MibTableColumn
isdnLapdOperStatus=_IsdnLapdOperStatus_Object((1,3,6,1,2,1,10,20,1,3,4,1,2),_IsdnLapdOperStatus_Type())
isdnLapdOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnLapdOperStatus.setStatus(_A)
_IsdnLapdPeerSabme_Type=Counter32
_IsdnLapdPeerSabme_Object=MibTableColumn
isdnLapdPeerSabme=_IsdnLapdPeerSabme_Object((1,3,6,1,2,1,10,20,1,3,4,1,3),_IsdnLapdPeerSabme_Type())
isdnLapdPeerSabme.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnLapdPeerSabme.setStatus(_A)
_IsdnLapdRecvdFrmr_Type=Counter32
_IsdnLapdRecvdFrmr_Object=MibTableColumn
isdnLapdRecvdFrmr=_IsdnLapdRecvdFrmr_Object((1,3,6,1,2,1,10,20,1,3,4,1,4),_IsdnLapdRecvdFrmr_Type())
isdnLapdRecvdFrmr.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnLapdRecvdFrmr.setStatus(_A)
_IsdnEndpointGroup_ObjectIdentity=ObjectIdentity
isdnEndpointGroup=_IsdnEndpointGroup_ObjectIdentity((1,3,6,1,2,1,10,20,1,4))
_IsdnEndpointGetIndex_Type=TestAndIncr
_IsdnEndpointGetIndex_Object=MibScalar
isdnEndpointGetIndex=_IsdnEndpointGetIndex_Object((1,3,6,1,2,1,10,20,1,4,1),_IsdnEndpointGetIndex_Type())
isdnEndpointGetIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnEndpointGetIndex.setStatus(_A)
_IsdnEndpointTable_Object=MibTable
isdnEndpointTable=_IsdnEndpointTable_Object((1,3,6,1,2,1,10,20,1,4,2))
if mibBuilder.loadTexts:isdnEndpointTable.setStatus(_A)
_IsdnEndpointEntry_Object=MibTableRow
isdnEndpointEntry=_IsdnEndpointEntry_Object((1,3,6,1,2,1,10,20,1,4,2,1))
isdnEndpointEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:isdnEndpointEntry.setStatus(_A)
class _IsdnEndpointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IsdnEndpointIndex_Type.__name__=_D
_IsdnEndpointIndex_Object=MibTableColumn
isdnEndpointIndex=_IsdnEndpointIndex_Object((1,3,6,1,2,1,10,20,1,4,2,1,1),_IsdnEndpointIndex_Type())
isdnEndpointIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:isdnEndpointIndex.setStatus(_A)
_IsdnEndpointIfIndex_Type=InterfaceIndex
_IsdnEndpointIfIndex_Object=MibTableColumn
isdnEndpointIfIndex=_IsdnEndpointIfIndex_Object((1,3,6,1,2,1,10,20,1,4,2,1,2),_IsdnEndpointIfIndex_Type())
isdnEndpointIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnEndpointIfIndex.setStatus(_A)
_IsdnEndpointIfType_Type=IANAifType
_IsdnEndpointIfType_Object=MibTableColumn
isdnEndpointIfType=_IsdnEndpointIfType_Object((1,3,6,1,2,1,10,20,1,4,2,1,3),_IsdnEndpointIfType_Type())
isdnEndpointIfType.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnEndpointIfType.setStatus(_A)
class _IsdnEndpointTeiType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('static',2)))
_IsdnEndpointTeiType_Type.__name__=_D
_IsdnEndpointTeiType_Object=MibTableColumn
isdnEndpointTeiType=_IsdnEndpointTeiType_Object((1,3,6,1,2,1,10,20,1,4,2,1,4),_IsdnEndpointTeiType_Type())
isdnEndpointTeiType.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnEndpointTeiType.setStatus(_A)
class _IsdnEndpointTeiValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IsdnEndpointTeiValue_Type.__name__=_D
_IsdnEndpointTeiValue_Object=MibTableColumn
isdnEndpointTeiValue=_IsdnEndpointTeiValue_Object((1,3,6,1,2,1,10,20,1,4,2,1,5),_IsdnEndpointTeiValue_Type())
isdnEndpointTeiValue.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnEndpointTeiValue.setStatus(_A)
class _IsdnEndpointSpid_Type(DisplayString):defaultValue=OctetString('')
_IsdnEndpointSpid_Type.__name__=_I
_IsdnEndpointSpid_Object=MibTableColumn
isdnEndpointSpid=_IsdnEndpointSpid_Object((1,3,6,1,2,1,10,20,1,4,2,1,6),_IsdnEndpointSpid_Type())
isdnEndpointSpid.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnEndpointSpid.setStatus(_A)
_IsdnEndpointStatus_Type=RowStatus
_IsdnEndpointStatus_Object=MibTableColumn
isdnEndpointStatus=_IsdnEndpointStatus_Object((1,3,6,1,2,1,10,20,1,4,2,1,7),_IsdnEndpointStatus_Type())
isdnEndpointStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnEndpointStatus.setStatus(_A)
_IsdnDirectoryGroup_ObjectIdentity=ObjectIdentity
isdnDirectoryGroup=_IsdnDirectoryGroup_ObjectIdentity((1,3,6,1,2,1,10,20,1,5))
_IsdnDirectoryTable_Object=MibTable
isdnDirectoryTable=_IsdnDirectoryTable_Object((1,3,6,1,2,1,10,20,1,5,1))
if mibBuilder.loadTexts:isdnDirectoryTable.setStatus(_A)
_IsdnDirectoryEntry_Object=MibTableRow
isdnDirectoryEntry=_IsdnDirectoryEntry_Object((1,3,6,1,2,1,10,20,1,5,1,1))
isdnDirectoryEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:isdnDirectoryEntry.setStatus(_A)
class _IsdnDirectoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IsdnDirectoryIndex_Type.__name__=_D
_IsdnDirectoryIndex_Object=MibTableColumn
isdnDirectoryIndex=_IsdnDirectoryIndex_Object((1,3,6,1,2,1,10,20,1,5,1,1,1),_IsdnDirectoryIndex_Type())
isdnDirectoryIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:isdnDirectoryIndex.setStatus(_A)
_IsdnDirectoryNumber_Type=DisplayString
_IsdnDirectoryNumber_Object=MibTableColumn
isdnDirectoryNumber=_IsdnDirectoryNumber_Object((1,3,6,1,2,1,10,20,1,5,1,1,2),_IsdnDirectoryNumber_Type())
isdnDirectoryNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnDirectoryNumber.setStatus(_A)
class _IsdnDirectorySigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IsdnDirectorySigIndex_Type.__name__=_D
_IsdnDirectorySigIndex_Object=MibTableColumn
isdnDirectorySigIndex=_IsdnDirectorySigIndex_Object((1,3,6,1,2,1,10,20,1,5,1,1,3),_IsdnDirectorySigIndex_Type())
isdnDirectorySigIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnDirectorySigIndex.setStatus(_A)
_IsdnDirectoryStatus_Type=RowStatus
_IsdnDirectoryStatus_Object=MibTableColumn
isdnDirectoryStatus=_IsdnDirectoryStatus_Object((1,3,6,1,2,1,10,20,1,5,1,1,4),_IsdnDirectoryStatus_Type())
isdnDirectoryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:isdnDirectoryStatus.setStatus(_A)
_IsdnMibTrapPrefix_ObjectIdentity=ObjectIdentity
isdnMibTrapPrefix=_IsdnMibTrapPrefix_ObjectIdentity((1,3,6,1,2,1,10,20,2))
_IsdnMibConformance_ObjectIdentity=ObjectIdentity
isdnMibConformance=_IsdnMibConformance_ObjectIdentity((1,3,6,1,2,1,10,20,2))
_IsdnMibTraps_ObjectIdentity=ObjectIdentity
isdnMibTraps=_IsdnMibTraps_ObjectIdentity((1,3,6,1,2,1,10,20,2,0))
_IsdnMibCompliances_ObjectIdentity=ObjectIdentity
isdnMibCompliances=_IsdnMibCompliances_ObjectIdentity((1,3,6,1,2,1,10,20,2,1))
_IsdnMibGroups_ObjectIdentity=ObjectIdentity
isdnMibGroups=_IsdnMibGroups_ObjectIdentity((1,3,6,1,2,1,10,20,2,2))
isdnSignalingEntry.registerAugmentions((_B,_W))
isdnSignalingStatsEntry.setIndexNames(*isdnSignalingEntry.getIndexNames())
isdnMibBasicRateGroup=ObjectGroup((1,3,6,1,2,1,10,20,2,2,1))
isdnMibBasicRateGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:isdnMibBasicRateGroup.setStatus(_A)
isdnMibBearerGroup=ObjectGroup((1,3,6,1,2,1,10,20,2,2,2))
isdnMibBearerGroup.setObjects(*((_B,_b),(_B,_K),(_B,_c),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_d),(_B,_P),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:isdnMibBearerGroup.setStatus(_A)
isdnMibSignalingGroup=ObjectGroup((1,3,6,1,2,1,10,20,2,2,3))
isdnMibSignalingGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:isdnMibSignalingGroup.setStatus(_A)
isdnMibEndpointGroup=ObjectGroup((1,3,6,1,2,1,10,20,2,2,4))
isdnMibEndpointGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:isdnMibEndpointGroup.setStatus(_A)
isdnMibDirectoryGroup=ObjectGroup((1,3,6,1,2,1,10,20,2,2,5))
isdnMibDirectoryGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:isdnMibDirectoryGroup.setStatus(_A)
isdnMibCallInformation=NotificationType((1,3,6,1,2,1,10,20,2,0,1))
isdnMibCallInformation.setObjects(*((_G,_H),(_B,_K),(_B,_L),(_B,_M),(_B,_P),(_B,_O),(_B,_N)))
if mibBuilder.loadTexts:isdnMibCallInformation.setStatus(_A)
isdnMibNotificationsGroup=NotificationGroup((1,3,6,1,2,1,10,20,2,2,6))
isdnMibNotificationsGroup.setObjects((_B,_A7))
if mibBuilder.loadTexts:isdnMibNotificationsGroup.setStatus(_A)
isdnMibCompliance=ModuleCompliance((1,3,6,1,2,1,10,20,2,1,1))
isdnMibCompliance.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:isdnMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'IsdnSignalingProtocol':IsdnSignalingProtocol,'isdnMib':isdnMib,'isdnMibObjects':isdnMibObjects,'isdnBasicRateGroup':isdnBasicRateGroup,'isdnBasicRateTable':isdnBasicRateTable,'isdnBasicRateEntry':isdnBasicRateEntry,_X:isdnBasicRateIfType,_Y:isdnBasicRateLineTopology,_Z:isdnBasicRateIfMode,_a:isdnBasicRateSignalMode,'isdnBearerGroup':isdnBearerGroup,'isdnBearerTable':isdnBearerTable,'isdnBearerEntry':isdnBearerEntry,_b:isdnBearerChannelType,_K:isdnBearerOperStatus,_c:isdnBearerChannelNumber,_L:isdnBearerPeerAddress,_M:isdnBearerPeerSubAddress,_N:isdnBearerCallOrigin,_O:isdnBearerInfoType,_d:isdnBearerMultirate,_P:isdnBearerCallSetupTime,_e:isdnBearerCallConnectTime,_f:isdnBearerChargedUnits,'isdnSignalingGroup':isdnSignalingGroup,_g:isdnSignalingGetIndex,'isdnSignalingTable':isdnSignalingTable,'isdnSignalingEntry':isdnSignalingEntry,_T:isdnSignalingIndex,_h:isdnSignalingIfIndex,_i:isdnSignalingProtocol,_j:isdnSignalingCallingAddress,_k:isdnSignalingSubAddress,_l:isdnSignalingBchannelCount,_m:isdnSignalingInfoTrapEnable,_n:isdnSignalingStatus,'isdnSignalingStatsTable':isdnSignalingStatsTable,_W:isdnSignalingStatsEntry,_o:isdnSigStatsInCalls,_p:isdnSigStatsInConnected,_q:isdnSigStatsOutCalls,_r:isdnSigStatsOutConnected,_s:isdnSigStatsChargedUnits,'isdnLapdTable':isdnLapdTable,'isdnLapdEntry':isdnLapdEntry,_t:isdnLapdPrimaryChannel,_u:isdnLapdOperStatus,_v:isdnLapdPeerSabme,_w:isdnLapdRecvdFrmr,'isdnEndpointGroup':isdnEndpointGroup,_x:isdnEndpointGetIndex,'isdnEndpointTable':isdnEndpointTable,'isdnEndpointEntry':isdnEndpointEntry,_U:isdnEndpointIndex,_y:isdnEndpointIfIndex,_z:isdnEndpointIfType,_A0:isdnEndpointTeiType,_A1:isdnEndpointTeiValue,_A2:isdnEndpointSpid,_A3:isdnEndpointStatus,'isdnDirectoryGroup':isdnDirectoryGroup,'isdnDirectoryTable':isdnDirectoryTable,'isdnDirectoryEntry':isdnDirectoryEntry,_V:isdnDirectoryIndex,_A4:isdnDirectoryNumber,_A5:isdnDirectorySigIndex,_A6:isdnDirectoryStatus,'isdnMibTrapPrefix':isdnMibTrapPrefix,'isdnMibConformance':isdnMibConformance,'isdnMibTraps':isdnMibTraps,_A7:isdnMibCallInformation,'isdnMibCompliances':isdnMibCompliances,'isdnMibCompliance':isdnMibCompliance,'isdnMibGroups':isdnMibGroups,_AB:isdnMibBasicRateGroup,_A9:isdnMibBearerGroup,_A8:isdnMibSignalingGroup,_AC:isdnMibEndpointGroup,_AD:isdnMibDirectoryGroup,_AA:isdnMibNotificationsGroup})