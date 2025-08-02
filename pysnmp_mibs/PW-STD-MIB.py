_BB='pwPerformanceGeneralGroup'
_BA='pwDeleted'
_B9='pwRemoteIfString'
_B8='pwRemoteIfMtu'
_B7='pwCwStatus'
_B6='pwRemoteGroupID'
_B5='pwLocalCapabAdvert'
_B4='pwLocalIfString'
_B3='pwLocalGroupID'
_B2='pwNotifRate'
_B1='pwDeletedNotifEnable'
_B0='pwUpDownNotifEnable'
_A_='pwGenFecIndexMappingPwIndex'
_Az='pwPeerMappingPwIndex'
_Ay='pwIndexMappingPwIndex'
_Ax='pwPerfIntervalOutHCBytes'
_Aw='pwPerfIntervalOutHCPackets'
_Av='pwPerfIntervalInHCBytes'
_Au='pwPerfIntervalInHCPackets'
_At='pwPerfCurrentOutHCBytes'
_As='pwPerfCurrentOutHCPackets'
_Ar='pwPerfCurrentInHCBytes'
_Aq='pwPerfCurrentInHCPackets'
_Ap='pwPerfIntervalOutBytes'
_Ao='pwPerfIntervalOutPackets'
_An='pwPerfIntervalInBytes'
_Am='pwPerfIntervalInPackets'
_Al='pwPerfCurrentOutBytes'
_Ak='pwPerfCurrentOutPackets'
_Aj='pwPerfCurrentInBytes'
_Ai='pwPerfCurrentInPackets'
_Ah='pwPerfIntervalTimeElapsed'
_Ag='pwPerfIntervalValidData'
_Af='pwValidIntervals'
_Ae='pwTimeElapsed'
_Ad='pwPerf1DayIntervalOutHCBytes'
_Ac='pwPerf1DayIntervalOutHCPackets'
_Ab='pwPerf1DayIntervalInHCBytes'
_Aa='pwPerf1DayIntervalInHCPackets'
_AZ='pwPerf1DayIntervalTimeElapsed'
_AY='pwPerf1DayIntervalValidData'
_AX='pwPerfTotalErrorPackets'
_AW='pwAttachedPwIndex'
_AV='pwHoldingPriority'
_AU='pwSetUpPriority'
_AT='pwIndexNext'
_AS='pwRemoteStatus'
_AR='pwRemoteStatusCapable'
_AQ='pwRemoteCapabilities'
_AP='pwRmtFragCapability'
_AO='pwFragmentCfgSize'
_AN='pwFcsRetentionStatus'
_AM='pwFcsRetentionCfg'
_AL='pwGenRemoteAIIType'
_AK='pwGenLocalAIIType'
_AJ='pwGenAGIType'
_AI='pwRemoteAttachmentID'
_AH='pwLocalAttachmentID'
_AG='pwGroupAttachmentID'
_AF='pwOamEnable'
_AE='pwStorageType'
_AD='pwRowStatus'
_AC='pwLocalStatus'
_AB='pwAdminStatus'
_AA='pwLastChange'
_A9='pwCreateTime'
_A8='pwInboundLabel'
_A7='pwOutboundLabel'
_A6='pwLocalIfMtu'
_A5='pwCwPreference'
_A4='pwIfIndex'
_A3='pwPsnType'
_A2='pwGenFecIndexMappingRemoteAII'
_A1='pwGenFecIndexMappingRemoteAIIType'
_A0='pwGenFecIndexMappingLocalAII'
_z='pwGenFecIndexMappingLocalAIIType'
_y='pwGenFecIndexMappingAGI'
_x='pwGenFecIndexMappingAGIType'
_w='pwPeerMappingPwID'
_v='pwPeerMappingPwType'
_u='pwPeerMappingPeerAddr'
_t='pwPeerMappingPeerAddrType'
_s='pwIndexMappingPeerAddr'
_r='pwIndexMappingPeerAddrType'
_q='pwIndexMappingPwID'
_p='pwIndexMappingPwType'
_o='pwPerf1DayIntervalNumber'
_n='pwPerfIntervalNumber'
_m='StorageType'
_l='SnmpAdminString'
_k='PwIndexOrZeroType'
_j='PwFragSize'
_i='InetAddressType'
_h='InterfaceIndexOrZero'
_g='pwNotificationControlGroup'
_f='pwSignalingGroup'
_e='pwMappingTablesGroup'
_d='pwHCPeformanceIntervalGroup'
_c='pwPeformanceIntervalGroup'
_b='pwPerformanceIntervalGeneralGroup'
_a='pwPeformance1DayIntervalGroup'
_Z='pwAttachmentGroup'
_Y='pwPriorityGroup'
_X='pwGetNextGroup'
_W='pwPwStatusGroup'
_V='pwFragGroup'
_U='pwFcsGroup'
_T='pwGeneralizedFecGroup'
_S='pwPwIdGroup'
_R='pwNotificationGroup'
_Q='pwBasicGroup'
_P='pwPeerAddr'
_O='pwPeerAddrType'
_N='pwID'
_M='pwType'
_L='read-write'
_K='Unsigned32'
_J='PwGenIdType'
_I='pwIndex'
_H='pwOperStatus'
_G='TruthValue'
_F='Integer32'
_E='not-accessible'
_D='read-create'
_C='read-only'
_B='current'
_A='PW-STD-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HCPerfCurrentCount,HCPerfIntervalCount,HCPerfTimeElapsed,HCPerfValidIntervals=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfCurrentCount','HCPerfIntervalCount','HCPerfTimeElapsed','HCPerfValidIntervals')
IANAPwCapabilities,IANAPwPsnTypeTC,IANAPwTypeTC=mibBuilder.importSymbols('IANA-PWE3-MIB','IANAPwCapabilities','IANAPwPsnTypeTC','IANAPwTypeTC')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_h)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_i)
PwAttachmentIdentifierType,PwCwStatusTC,PwFragSize,PwFragStatus,PwGenIdType,PwGroupID,PwIDType,PwIndexOrZeroType,PwIndexType,PwOperStatusTC,PwStatus=mibBuilder.importSymbols('PW-TC-STD-MIB','PwAttachmentIdentifierType','PwCwStatusTC',_j,'PwFragStatus',_J,'PwGroupID','PwIDType',_k,'PwIndexType','PwOperStatusTC','PwStatus')
PerfCurrentCount,PerfIntervalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_l)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso','transmission')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_m,'TextualConvention','TimeStamp',_G)
pwStdMIB=ModuleIdentity((1,3,6,1,2,1,10,246))
if mibBuilder.loadTexts:pwStdMIB.setRevisions(('2009-06-11 00:00',))
_PwNotifications_ObjectIdentity=ObjectIdentity
pwNotifications=_PwNotifications_ObjectIdentity((1,3,6,1,2,1,10,246,0))
_PwObjects_ObjectIdentity=ObjectIdentity
pwObjects=_PwObjects_ObjectIdentity((1,3,6,1,2,1,10,246,1))
_PwIndexNext_Type=Unsigned32
_PwIndexNext_Object=MibScalar
pwIndexNext=_PwIndexNext_Object((1,3,6,1,2,1,10,246,1,1),_PwIndexNext_Type())
pwIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:pwIndexNext.setStatus(_B)
_PwTable_Object=MibTable
pwTable=_PwTable_Object((1,3,6,1,2,1,10,246,1,2))
if mibBuilder.loadTexts:pwTable.setStatus(_B)
_PwEntry_Object=MibTableRow
pwEntry=_PwEntry_Object((1,3,6,1,2,1,10,246,1,2,1))
pwEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:pwEntry.setStatus(_B)
_PwIndex_Type=PwIndexType
_PwIndex_Object=MibTableColumn
pwIndex=_PwIndex_Object((1,3,6,1,2,1,10,246,1,2,1,1),_PwIndex_Type())
pwIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pwIndex.setStatus(_B)
_PwType_Type=IANAPwTypeTC
_PwType_Object=MibTableColumn
pwType=_PwType_Object((1,3,6,1,2,1,10,246,1,2,1,2),_PwType_Type())
pwType.setMaxAccess(_D)
if mibBuilder.loadTexts:pwType.setStatus(_B)
class _PwOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('manual',1),('pwIdFecSignaling',2),('genFecSignaling',3),('l2tpControlProtocol',4),('other',5)))
_PwOwner_Type.__name__=_F
_PwOwner_Object=MibTableColumn
pwOwner=_PwOwner_Object((1,3,6,1,2,1,10,246,1,2,1,3),_PwOwner_Type())
pwOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:pwOwner.setStatus(_B)
_PwPsnType_Type=IANAPwPsnTypeTC
_PwPsnType_Object=MibTableColumn
pwPsnType=_PwPsnType_Object((1,3,6,1,2,1,10,246,1,2,1,4),_PwPsnType_Type())
pwPsnType.setMaxAccess(_D)
if mibBuilder.loadTexts:pwPsnType.setStatus(_B)
class _PwSetUpPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PwSetUpPriority_Type.__name__=_F
_PwSetUpPriority_Object=MibTableColumn
pwSetUpPriority=_PwSetUpPriority_Object((1,3,6,1,2,1,10,246,1,2,1,5),_PwSetUpPriority_Type())
pwSetUpPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:pwSetUpPriority.setStatus(_B)
class _PwHoldingPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PwHoldingPriority_Type.__name__=_F
_PwHoldingPriority_Object=MibTableColumn
pwHoldingPriority=_PwHoldingPriority_Object((1,3,6,1,2,1,10,246,1,2,1,6),_PwHoldingPriority_Type())
pwHoldingPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:pwHoldingPriority.setStatus(_B)
class _PwPeerAddrType_Type(InetAddressType):defaultValue=1
_PwPeerAddrType_Type.__name__=_i
_PwPeerAddrType_Object=MibTableColumn
pwPeerAddrType=_PwPeerAddrType_Object((1,3,6,1,2,1,10,246,1,2,1,8),_PwPeerAddrType_Type())
pwPeerAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:pwPeerAddrType.setStatus(_B)
_PwPeerAddr_Type=InetAddress
_PwPeerAddr_Object=MibTableColumn
pwPeerAddr=_PwPeerAddr_Object((1,3,6,1,2,1,10,246,1,2,1,9),_PwPeerAddr_Type())
pwPeerAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:pwPeerAddr.setStatus(_B)
class _PwAttachedPwIndex_Type(PwIndexOrZeroType):defaultValue=0
_PwAttachedPwIndex_Type.__name__=_k
_PwAttachedPwIndex_Object=MibTableColumn
pwAttachedPwIndex=_PwAttachedPwIndex_Object((1,3,6,1,2,1,10,246,1,2,1,10),_PwAttachedPwIndex_Type())
pwAttachedPwIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAttachedPwIndex.setStatus(_B)
class _PwIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_PwIfIndex_Type.__name__=_h
_PwIfIndex_Object=MibTableColumn
pwIfIndex=_PwIfIndex_Object((1,3,6,1,2,1,10,246,1,2,1,11),_PwIfIndex_Type())
pwIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:pwIfIndex.setStatus(_B)
_PwID_Type=PwIDType
_PwID_Object=MibTableColumn
pwID=_PwID_Object((1,3,6,1,2,1,10,246,1,2,1,12),_PwID_Type())
pwID.setMaxAccess(_D)
if mibBuilder.loadTexts:pwID.setStatus(_B)
_PwLocalGroupID_Type=PwGroupID
_PwLocalGroupID_Object=MibTableColumn
pwLocalGroupID=_PwLocalGroupID_Object((1,3,6,1,2,1,10,246,1,2,1,13),_PwLocalGroupID_Type())
pwLocalGroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:pwLocalGroupID.setStatus(_B)
_PwGroupAttachmentID_Type=PwAttachmentIdentifierType
_PwGroupAttachmentID_Object=MibTableColumn
pwGroupAttachmentID=_PwGroupAttachmentID_Object((1,3,6,1,2,1,10,246,1,2,1,14),_PwGroupAttachmentID_Type())
pwGroupAttachmentID.setMaxAccess(_D)
if mibBuilder.loadTexts:pwGroupAttachmentID.setStatus(_B)
_PwLocalAttachmentID_Type=PwAttachmentIdentifierType
_PwLocalAttachmentID_Object=MibTableColumn
pwLocalAttachmentID=_PwLocalAttachmentID_Object((1,3,6,1,2,1,10,246,1,2,1,15),_PwLocalAttachmentID_Type())
pwLocalAttachmentID.setMaxAccess(_D)
if mibBuilder.loadTexts:pwLocalAttachmentID.setStatus(_B)
_PwRemoteAttachmentID_Type=PwAttachmentIdentifierType
_PwRemoteAttachmentID_Object=MibTableColumn
pwRemoteAttachmentID=_PwRemoteAttachmentID_Object((1,3,6,1,2,1,10,246,1,2,1,16),_PwRemoteAttachmentID_Type())
pwRemoteAttachmentID.setMaxAccess(_D)
if mibBuilder.loadTexts:pwRemoteAttachmentID.setStatus(_B)
class _PwCwPreference_Type(TruthValue):defaultValue=2
_PwCwPreference_Type.__name__=_G
_PwCwPreference_Object=MibTableColumn
pwCwPreference=_PwCwPreference_Object((1,3,6,1,2,1,10,246,1,2,1,17),_PwCwPreference_Type())
pwCwPreference.setMaxAccess(_D)
if mibBuilder.loadTexts:pwCwPreference.setStatus(_B)
class _PwLocalIfMtu_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PwLocalIfMtu_Type.__name__=_K
_PwLocalIfMtu_Object=MibTableColumn
pwLocalIfMtu=_PwLocalIfMtu_Object((1,3,6,1,2,1,10,246,1,2,1,18),_PwLocalIfMtu_Type())
pwLocalIfMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:pwLocalIfMtu.setStatus(_B)
class _PwLocalIfString_Type(TruthValue):defaultValue=2
_PwLocalIfString_Type.__name__=_G
_PwLocalIfString_Object=MibTableColumn
pwLocalIfString=_PwLocalIfString_Object((1,3,6,1,2,1,10,246,1,2,1,19),_PwLocalIfString_Type())
pwLocalIfString.setMaxAccess(_D)
if mibBuilder.loadTexts:pwLocalIfString.setStatus(_B)
_PwLocalCapabAdvert_Type=IANAPwCapabilities
_PwLocalCapabAdvert_Object=MibTableColumn
pwLocalCapabAdvert=_PwLocalCapabAdvert_Object((1,3,6,1,2,1,10,246,1,2,1,20),_PwLocalCapabAdvert_Type())
pwLocalCapabAdvert.setMaxAccess(_D)
if mibBuilder.loadTexts:pwLocalCapabAdvert.setStatus(_B)
_PwRemoteGroupID_Type=PwGroupID
_PwRemoteGroupID_Object=MibTableColumn
pwRemoteGroupID=_PwRemoteGroupID_Object((1,3,6,1,2,1,10,246,1,2,1,21),_PwRemoteGroupID_Type())
pwRemoteGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:pwRemoteGroupID.setStatus(_B)
_PwCwStatus_Type=PwCwStatusTC
_PwCwStatus_Object=MibTableColumn
pwCwStatus=_PwCwStatus_Object((1,3,6,1,2,1,10,246,1,2,1,22),_PwCwStatus_Type())
pwCwStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pwCwStatus.setStatus(_B)
_PwRemoteIfMtu_Type=Unsigned32
_PwRemoteIfMtu_Object=MibTableColumn
pwRemoteIfMtu=_PwRemoteIfMtu_Object((1,3,6,1,2,1,10,246,1,2,1,23),_PwRemoteIfMtu_Type())
pwRemoteIfMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:pwRemoteIfMtu.setStatus(_B)
class _PwRemoteIfString_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_PwRemoteIfString_Type.__name__=_l
_PwRemoteIfString_Object=MibTableColumn
pwRemoteIfString=_PwRemoteIfString_Object((1,3,6,1,2,1,10,246,1,2,1,24),_PwRemoteIfString_Type())
pwRemoteIfString.setMaxAccess(_C)
if mibBuilder.loadTexts:pwRemoteIfString.setStatus(_B)
_PwRemoteCapabilities_Type=IANAPwCapabilities
_PwRemoteCapabilities_Object=MibTableColumn
pwRemoteCapabilities=_PwRemoteCapabilities_Object((1,3,6,1,2,1,10,246,1,2,1,25),_PwRemoteCapabilities_Type())
pwRemoteCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:pwRemoteCapabilities.setStatus(_B)
class _PwFragmentCfgSize_Type(PwFragSize):defaultValue=0
_PwFragmentCfgSize_Type.__name__=_j
_PwFragmentCfgSize_Object=MibTableColumn
pwFragmentCfgSize=_PwFragmentCfgSize_Object((1,3,6,1,2,1,10,246,1,2,1,26),_PwFragmentCfgSize_Type())
pwFragmentCfgSize.setMaxAccess(_D)
if mibBuilder.loadTexts:pwFragmentCfgSize.setStatus(_B)
if mibBuilder.loadTexts:pwFragmentCfgSize.setUnits('bytes')
_PwRmtFragCapability_Type=PwFragStatus
_PwRmtFragCapability_Object=MibTableColumn
pwRmtFragCapability=_PwRmtFragCapability_Object((1,3,6,1,2,1,10,246,1,2,1,27),_PwRmtFragCapability_Type())
pwRmtFragCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:pwRmtFragCapability.setStatus(_B)
class _PwFcsRetentionCfg_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fcsRetentionDisable',1),('fcsRetentionEnable',2)))
_PwFcsRetentionCfg_Type.__name__=_F
_PwFcsRetentionCfg_Object=MibTableColumn
pwFcsRetentionCfg=_PwFcsRetentionCfg_Object((1,3,6,1,2,1,10,246,1,2,1,28),_PwFcsRetentionCfg_Type())
pwFcsRetentionCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:pwFcsRetentionCfg.setStatus(_B)
class _PwFcsRetentionStatus_Type(Bits):namedValues=NamedValues(*(('remoteIndicationUnknown',0),('remoteRequestFcsRetention',1),('fcsRetentionEnabled',2),('fcsRetentionDisabled',3),('localFcsRetentionCfgErr',4),('fcsRetentionFcsSizeMismatch',5)))
_PwFcsRetentionStatus_Type.__name__='Bits'
_PwFcsRetentionStatus_Object=MibTableColumn
pwFcsRetentionStatus=_PwFcsRetentionStatus_Object((1,3,6,1,2,1,10,246,1,2,1,29),_PwFcsRetentionStatus_Type())
pwFcsRetentionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pwFcsRetentionStatus.setStatus(_B)
_PwOutboundLabel_Type=Unsigned32
_PwOutboundLabel_Object=MibTableColumn
pwOutboundLabel=_PwOutboundLabel_Object((1,3,6,1,2,1,10,246,1,2,1,30),_PwOutboundLabel_Type())
pwOutboundLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:pwOutboundLabel.setStatus(_B)
_PwInboundLabel_Type=Unsigned32
_PwInboundLabel_Object=MibTableColumn
pwInboundLabel=_PwInboundLabel_Object((1,3,6,1,2,1,10,246,1,2,1,31),_PwInboundLabel_Type())
pwInboundLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:pwInboundLabel.setStatus(_B)
_PwName_Type=SnmpAdminString
_PwName_Object=MibTableColumn
pwName=_PwName_Object((1,3,6,1,2,1,10,246,1,2,1,32),_PwName_Type())
pwName.setMaxAccess(_D)
if mibBuilder.loadTexts:pwName.setStatus(_B)
_PwDescr_Type=SnmpAdminString
_PwDescr_Object=MibTableColumn
pwDescr=_PwDescr_Object((1,3,6,1,2,1,10,246,1,2,1,33),_PwDescr_Type())
pwDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:pwDescr.setStatus(_B)
_PwCreateTime_Type=TimeStamp
_PwCreateTime_Object=MibTableColumn
pwCreateTime=_PwCreateTime_Object((1,3,6,1,2,1,10,246,1,2,1,34),_PwCreateTime_Type())
pwCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pwCreateTime.setStatus(_B)
_PwUpTime_Type=TimeTicks
_PwUpTime_Object=MibTableColumn
pwUpTime=_PwUpTime_Object((1,3,6,1,2,1,10,246,1,2,1,35),_PwUpTime_Type())
pwUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pwUpTime.setStatus(_B)
_PwLastChange_Type=TimeTicks
_PwLastChange_Object=MibTableColumn
pwLastChange=_PwLastChange_Object((1,3,6,1,2,1,10,246,1,2,1,36),_PwLastChange_Type())
pwLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:pwLastChange.setStatus(_B)
class _PwAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_PwAdminStatus_Type.__name__=_F
_PwAdminStatus_Object=MibTableColumn
pwAdminStatus=_PwAdminStatus_Object((1,3,6,1,2,1,10,246,1,2,1,37),_PwAdminStatus_Type())
pwAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAdminStatus.setStatus(_B)
_PwOperStatus_Type=PwOperStatusTC
_PwOperStatus_Object=MibTableColumn
pwOperStatus=_PwOperStatus_Object((1,3,6,1,2,1,10,246,1,2,1,38),_PwOperStatus_Type())
pwOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pwOperStatus.setStatus(_B)
_PwLocalStatus_Type=PwStatus
_PwLocalStatus_Object=MibTableColumn
pwLocalStatus=_PwLocalStatus_Object((1,3,6,1,2,1,10,246,1,2,1,39),_PwLocalStatus_Type())
pwLocalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pwLocalStatus.setStatus(_B)
class _PwRemoteStatusCapable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notApplicable',1),('notYetKnown',2),('remoteCapable',3),('remoteNotCapable',4)))
_PwRemoteStatusCapable_Type.__name__=_F
_PwRemoteStatusCapable_Object=MibTableColumn
pwRemoteStatusCapable=_PwRemoteStatusCapable_Object((1,3,6,1,2,1,10,246,1,2,1,40),_PwRemoteStatusCapable_Type())
pwRemoteStatusCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:pwRemoteStatusCapable.setStatus(_B)
_PwRemoteStatus_Type=PwStatus
_PwRemoteStatus_Object=MibTableColumn
pwRemoteStatus=_PwRemoteStatus_Object((1,3,6,1,2,1,10,246,1,2,1,41),_PwRemoteStatus_Type())
pwRemoteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pwRemoteStatus.setStatus(_B)
_PwTimeElapsed_Type=HCPerfTimeElapsed
_PwTimeElapsed_Object=MibTableColumn
pwTimeElapsed=_PwTimeElapsed_Object((1,3,6,1,2,1,10,246,1,2,1,42),_PwTimeElapsed_Type())
pwTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTimeElapsed.setStatus(_B)
_PwValidIntervals_Type=HCPerfValidIntervals
_PwValidIntervals_Object=MibTableColumn
pwValidIntervals=_PwValidIntervals_Object((1,3,6,1,2,1,10,246,1,2,1,43),_PwValidIntervals_Type())
pwValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:pwValidIntervals.setStatus(_B)
_PwRowStatus_Type=RowStatus
_PwRowStatus_Object=MibTableColumn
pwRowStatus=_PwRowStatus_Object((1,3,6,1,2,1,10,246,1,2,1,44),_PwRowStatus_Type())
pwRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pwRowStatus.setStatus(_B)
class _PwStorageType_Type(StorageType):defaultValue=3
_PwStorageType_Type.__name__=_m
_PwStorageType_Object=MibTableColumn
pwStorageType=_PwStorageType_Object((1,3,6,1,2,1,10,246,1,2,1,45),_PwStorageType_Type())
pwStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:pwStorageType.setStatus(_B)
class _PwOamEnable_Type(TruthValue):defaultValue=1
_PwOamEnable_Type.__name__=_G
_PwOamEnable_Object=MibTableColumn
pwOamEnable=_PwOamEnable_Object((1,3,6,1,2,1,10,246,1,2,1,46),_PwOamEnable_Type())
pwOamEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:pwOamEnable.setStatus(_B)
class _PwGenAGIType_Type(PwGenIdType):defaultValue=0
_PwGenAGIType_Type.__name__=_J
_PwGenAGIType_Object=MibTableColumn
pwGenAGIType=_PwGenAGIType_Object((1,3,6,1,2,1,10,246,1,2,1,47),_PwGenAGIType_Type())
pwGenAGIType.setMaxAccess(_D)
if mibBuilder.loadTexts:pwGenAGIType.setStatus(_B)
class _PwGenLocalAIIType_Type(PwGenIdType):defaultValue=0
_PwGenLocalAIIType_Type.__name__=_J
_PwGenLocalAIIType_Object=MibTableColumn
pwGenLocalAIIType=_PwGenLocalAIIType_Object((1,3,6,1,2,1,10,246,1,2,1,48),_PwGenLocalAIIType_Type())
pwGenLocalAIIType.setMaxAccess(_D)
if mibBuilder.loadTexts:pwGenLocalAIIType.setStatus(_B)
class _PwGenRemoteAIIType_Type(PwGenIdType):defaultValue=0
_PwGenRemoteAIIType_Type.__name__=_J
_PwGenRemoteAIIType_Object=MibTableColumn
pwGenRemoteAIIType=_PwGenRemoteAIIType_Object((1,3,6,1,2,1,10,246,1,2,1,49),_PwGenRemoteAIIType_Type())
pwGenRemoteAIIType.setMaxAccess(_D)
if mibBuilder.loadTexts:pwGenRemoteAIIType.setStatus(_B)
_PwPerfCurrentTable_Object=MibTable
pwPerfCurrentTable=_PwPerfCurrentTable_Object((1,3,6,1,2,1,10,246,1,3))
if mibBuilder.loadTexts:pwPerfCurrentTable.setStatus(_B)
_PwPerfCurrentEntry_Object=MibTableRow
pwPerfCurrentEntry=_PwPerfCurrentEntry_Object((1,3,6,1,2,1,10,246,1,3,1))
pwPerfCurrentEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:pwPerfCurrentEntry.setStatus(_B)
_PwPerfCurrentInHCPackets_Type=HCPerfCurrentCount
_PwPerfCurrentInHCPackets_Object=MibTableColumn
pwPerfCurrentInHCPackets=_PwPerfCurrentInHCPackets_Object((1,3,6,1,2,1,10,246,1,3,1,1),_PwPerfCurrentInHCPackets_Type())
pwPerfCurrentInHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfCurrentInHCPackets.setStatus(_B)
_PwPerfCurrentInHCBytes_Type=HCPerfCurrentCount
_PwPerfCurrentInHCBytes_Object=MibTableColumn
pwPerfCurrentInHCBytes=_PwPerfCurrentInHCBytes_Object((1,3,6,1,2,1,10,246,1,3,1,2),_PwPerfCurrentInHCBytes_Type())
pwPerfCurrentInHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfCurrentInHCBytes.setStatus(_B)
_PwPerfCurrentOutHCPackets_Type=HCPerfCurrentCount
_PwPerfCurrentOutHCPackets_Object=MibTableColumn
pwPerfCurrentOutHCPackets=_PwPerfCurrentOutHCPackets_Object((1,3,6,1,2,1,10,246,1,3,1,3),_PwPerfCurrentOutHCPackets_Type())
pwPerfCurrentOutHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfCurrentOutHCPackets.setStatus(_B)
_PwPerfCurrentOutHCBytes_Type=HCPerfCurrentCount
_PwPerfCurrentOutHCBytes_Object=MibTableColumn
pwPerfCurrentOutHCBytes=_PwPerfCurrentOutHCBytes_Object((1,3,6,1,2,1,10,246,1,3,1,4),_PwPerfCurrentOutHCBytes_Type())
pwPerfCurrentOutHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfCurrentOutHCBytes.setStatus(_B)
_PwPerfCurrentInPackets_Type=PerfCurrentCount
_PwPerfCurrentInPackets_Object=MibTableColumn
pwPerfCurrentInPackets=_PwPerfCurrentInPackets_Object((1,3,6,1,2,1,10,246,1,3,1,5),_PwPerfCurrentInPackets_Type())
pwPerfCurrentInPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfCurrentInPackets.setStatus(_B)
_PwPerfCurrentInBytes_Type=PerfCurrentCount
_PwPerfCurrentInBytes_Object=MibTableColumn
pwPerfCurrentInBytes=_PwPerfCurrentInBytes_Object((1,3,6,1,2,1,10,246,1,3,1,6),_PwPerfCurrentInBytes_Type())
pwPerfCurrentInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfCurrentInBytes.setStatus(_B)
_PwPerfCurrentOutPackets_Type=PerfCurrentCount
_PwPerfCurrentOutPackets_Object=MibTableColumn
pwPerfCurrentOutPackets=_PwPerfCurrentOutPackets_Object((1,3,6,1,2,1,10,246,1,3,1,7),_PwPerfCurrentOutPackets_Type())
pwPerfCurrentOutPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfCurrentOutPackets.setStatus(_B)
_PwPerfCurrentOutBytes_Type=PerfCurrentCount
_PwPerfCurrentOutBytes_Object=MibTableColumn
pwPerfCurrentOutBytes=_PwPerfCurrentOutBytes_Object((1,3,6,1,2,1,10,246,1,3,1,8),_PwPerfCurrentOutBytes_Type())
pwPerfCurrentOutBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfCurrentOutBytes.setStatus(_B)
_PwPerfIntervalTable_Object=MibTable
pwPerfIntervalTable=_PwPerfIntervalTable_Object((1,3,6,1,2,1,10,246,1,4))
if mibBuilder.loadTexts:pwPerfIntervalTable.setStatus(_B)
_PwPerfIntervalEntry_Object=MibTableRow
pwPerfIntervalEntry=_PwPerfIntervalEntry_Object((1,3,6,1,2,1,10,246,1,4,1))
pwPerfIntervalEntry.setIndexNames((0,_A,_I),(0,_A,_n))
if mibBuilder.loadTexts:pwPerfIntervalEntry.setStatus(_B)
class _PwPerfIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_PwPerfIntervalNumber_Type.__name__=_F
_PwPerfIntervalNumber_Object=MibTableColumn
pwPerfIntervalNumber=_PwPerfIntervalNumber_Object((1,3,6,1,2,1,10,246,1,4,1,1),_PwPerfIntervalNumber_Type())
pwPerfIntervalNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:pwPerfIntervalNumber.setStatus(_B)
_PwPerfIntervalValidData_Type=TruthValue
_PwPerfIntervalValidData_Object=MibTableColumn
pwPerfIntervalValidData=_PwPerfIntervalValidData_Object((1,3,6,1,2,1,10,246,1,4,1,2),_PwPerfIntervalValidData_Type())
pwPerfIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalValidData.setStatus(_B)
_PwPerfIntervalTimeElapsed_Type=HCPerfTimeElapsed
_PwPerfIntervalTimeElapsed_Object=MibTableColumn
pwPerfIntervalTimeElapsed=_PwPerfIntervalTimeElapsed_Object((1,3,6,1,2,1,10,246,1,4,1,3),_PwPerfIntervalTimeElapsed_Type())
pwPerfIntervalTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalTimeElapsed.setStatus(_B)
_PwPerfIntervalInHCPackets_Type=HCPerfIntervalCount
_PwPerfIntervalInHCPackets_Object=MibTableColumn
pwPerfIntervalInHCPackets=_PwPerfIntervalInHCPackets_Object((1,3,6,1,2,1,10,246,1,4,1,4),_PwPerfIntervalInHCPackets_Type())
pwPerfIntervalInHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalInHCPackets.setStatus(_B)
_PwPerfIntervalInHCBytes_Type=HCPerfIntervalCount
_PwPerfIntervalInHCBytes_Object=MibTableColumn
pwPerfIntervalInHCBytes=_PwPerfIntervalInHCBytes_Object((1,3,6,1,2,1,10,246,1,4,1,5),_PwPerfIntervalInHCBytes_Type())
pwPerfIntervalInHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalInHCBytes.setStatus(_B)
_PwPerfIntervalOutHCPackets_Type=HCPerfIntervalCount
_PwPerfIntervalOutHCPackets_Object=MibTableColumn
pwPerfIntervalOutHCPackets=_PwPerfIntervalOutHCPackets_Object((1,3,6,1,2,1,10,246,1,4,1,6),_PwPerfIntervalOutHCPackets_Type())
pwPerfIntervalOutHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalOutHCPackets.setStatus(_B)
_PwPerfIntervalOutHCBytes_Type=HCPerfIntervalCount
_PwPerfIntervalOutHCBytes_Object=MibTableColumn
pwPerfIntervalOutHCBytes=_PwPerfIntervalOutHCBytes_Object((1,3,6,1,2,1,10,246,1,4,1,7),_PwPerfIntervalOutHCBytes_Type())
pwPerfIntervalOutHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalOutHCBytes.setStatus(_B)
_PwPerfIntervalInPackets_Type=PerfIntervalCount
_PwPerfIntervalInPackets_Object=MibTableColumn
pwPerfIntervalInPackets=_PwPerfIntervalInPackets_Object((1,3,6,1,2,1,10,246,1,4,1,8),_PwPerfIntervalInPackets_Type())
pwPerfIntervalInPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalInPackets.setStatus(_B)
_PwPerfIntervalInBytes_Type=PerfIntervalCount
_PwPerfIntervalInBytes_Object=MibTableColumn
pwPerfIntervalInBytes=_PwPerfIntervalInBytes_Object((1,3,6,1,2,1,10,246,1,4,1,9),_PwPerfIntervalInBytes_Type())
pwPerfIntervalInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalInBytes.setStatus(_B)
_PwPerfIntervalOutPackets_Type=PerfIntervalCount
_PwPerfIntervalOutPackets_Object=MibTableColumn
pwPerfIntervalOutPackets=_PwPerfIntervalOutPackets_Object((1,3,6,1,2,1,10,246,1,4,1,10),_PwPerfIntervalOutPackets_Type())
pwPerfIntervalOutPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalOutPackets.setStatus(_B)
_PwPerfIntervalOutBytes_Type=PerfIntervalCount
_PwPerfIntervalOutBytes_Object=MibTableColumn
pwPerfIntervalOutBytes=_PwPerfIntervalOutBytes_Object((1,3,6,1,2,1,10,246,1,4,1,11),_PwPerfIntervalOutBytes_Type())
pwPerfIntervalOutBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalOutBytes.setStatus(_B)
_PwPerf1DayIntervalTable_Object=MibTable
pwPerf1DayIntervalTable=_PwPerf1DayIntervalTable_Object((1,3,6,1,2,1,10,246,1,5))
if mibBuilder.loadTexts:pwPerf1DayIntervalTable.setStatus(_B)
_PwPerf1DayIntervalEntry_Object=MibTableRow
pwPerf1DayIntervalEntry=_PwPerf1DayIntervalEntry_Object((1,3,6,1,2,1,10,246,1,5,1))
pwPerf1DayIntervalEntry.setIndexNames((0,_A,_I),(0,_A,_o))
if mibBuilder.loadTexts:pwPerf1DayIntervalEntry.setStatus(_B)
class _PwPerf1DayIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_PwPerf1DayIntervalNumber_Type.__name__=_K
_PwPerf1DayIntervalNumber_Object=MibTableColumn
pwPerf1DayIntervalNumber=_PwPerf1DayIntervalNumber_Object((1,3,6,1,2,1,10,246,1,5,1,1),_PwPerf1DayIntervalNumber_Type())
pwPerf1DayIntervalNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:pwPerf1DayIntervalNumber.setStatus(_B)
_PwPerf1DayIntervalValidData_Type=TruthValue
_PwPerf1DayIntervalValidData_Object=MibTableColumn
pwPerf1DayIntervalValidData=_PwPerf1DayIntervalValidData_Object((1,3,6,1,2,1,10,246,1,5,1,2),_PwPerf1DayIntervalValidData_Type())
pwPerf1DayIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerf1DayIntervalValidData.setStatus(_B)
_PwPerf1DayIntervalTimeElapsed_Type=HCPerfTimeElapsed
_PwPerf1DayIntervalTimeElapsed_Object=MibTableColumn
pwPerf1DayIntervalTimeElapsed=_PwPerf1DayIntervalTimeElapsed_Object((1,3,6,1,2,1,10,246,1,5,1,3),_PwPerf1DayIntervalTimeElapsed_Type())
pwPerf1DayIntervalTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerf1DayIntervalTimeElapsed.setStatus(_B)
if mibBuilder.loadTexts:pwPerf1DayIntervalTimeElapsed.setUnits('seconds')
_PwPerf1DayIntervalInHCPackets_Type=Counter64
_PwPerf1DayIntervalInHCPackets_Object=MibTableColumn
pwPerf1DayIntervalInHCPackets=_PwPerf1DayIntervalInHCPackets_Object((1,3,6,1,2,1,10,246,1,5,1,4),_PwPerf1DayIntervalInHCPackets_Type())
pwPerf1DayIntervalInHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerf1DayIntervalInHCPackets.setStatus(_B)
_PwPerf1DayIntervalInHCBytes_Type=Counter64
_PwPerf1DayIntervalInHCBytes_Object=MibTableColumn
pwPerf1DayIntervalInHCBytes=_PwPerf1DayIntervalInHCBytes_Object((1,3,6,1,2,1,10,246,1,5,1,5),_PwPerf1DayIntervalInHCBytes_Type())
pwPerf1DayIntervalInHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerf1DayIntervalInHCBytes.setStatus(_B)
_PwPerf1DayIntervalOutHCPackets_Type=Counter64
_PwPerf1DayIntervalOutHCPackets_Object=MibTableColumn
pwPerf1DayIntervalOutHCPackets=_PwPerf1DayIntervalOutHCPackets_Object((1,3,6,1,2,1,10,246,1,5,1,6),_PwPerf1DayIntervalOutHCPackets_Type())
pwPerf1DayIntervalOutHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerf1DayIntervalOutHCPackets.setStatus(_B)
_PwPerf1DayIntervalOutHCBytes_Type=Counter64
_PwPerf1DayIntervalOutHCBytes_Object=MibTableColumn
pwPerf1DayIntervalOutHCBytes=_PwPerf1DayIntervalOutHCBytes_Object((1,3,6,1,2,1,10,246,1,5,1,7),_PwPerf1DayIntervalOutHCBytes_Type())
pwPerf1DayIntervalOutHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerf1DayIntervalOutHCBytes.setStatus(_B)
_PwPerfTotalErrorPackets_Type=Counter32
_PwPerfTotalErrorPackets_Object=MibScalar
pwPerfTotalErrorPackets=_PwPerfTotalErrorPackets_Object((1,3,6,1,2,1,10,246,1,6),_PwPerfTotalErrorPackets_Type())
pwPerfTotalErrorPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfTotalErrorPackets.setStatus(_B)
_PwIndexMappingTable_Object=MibTable
pwIndexMappingTable=_PwIndexMappingTable_Object((1,3,6,1,2,1,10,246,1,7))
if mibBuilder.loadTexts:pwIndexMappingTable.setStatus(_B)
_PwIndexMappingEntry_Object=MibTableRow
pwIndexMappingEntry=_PwIndexMappingEntry_Object((1,3,6,1,2,1,10,246,1,7,1))
pwIndexMappingEntry.setIndexNames((0,_A,_p),(0,_A,_q),(0,_A,_r),(0,_A,_s))
if mibBuilder.loadTexts:pwIndexMappingEntry.setStatus(_B)
_PwIndexMappingPwType_Type=IANAPwTypeTC
_PwIndexMappingPwType_Object=MibTableColumn
pwIndexMappingPwType=_PwIndexMappingPwType_Object((1,3,6,1,2,1,10,246,1,7,1,1),_PwIndexMappingPwType_Type())
pwIndexMappingPwType.setMaxAccess(_E)
if mibBuilder.loadTexts:pwIndexMappingPwType.setStatus(_B)
_PwIndexMappingPwID_Type=PwIDType
_PwIndexMappingPwID_Object=MibTableColumn
pwIndexMappingPwID=_PwIndexMappingPwID_Object((1,3,6,1,2,1,10,246,1,7,1,2),_PwIndexMappingPwID_Type())
pwIndexMappingPwID.setMaxAccess(_E)
if mibBuilder.loadTexts:pwIndexMappingPwID.setStatus(_B)
_PwIndexMappingPeerAddrType_Type=InetAddressType
_PwIndexMappingPeerAddrType_Object=MibTableColumn
pwIndexMappingPeerAddrType=_PwIndexMappingPeerAddrType_Object((1,3,6,1,2,1,10,246,1,7,1,3),_PwIndexMappingPeerAddrType_Type())
pwIndexMappingPeerAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:pwIndexMappingPeerAddrType.setStatus(_B)
_PwIndexMappingPeerAddr_Type=InetAddress
_PwIndexMappingPeerAddr_Object=MibTableColumn
pwIndexMappingPeerAddr=_PwIndexMappingPeerAddr_Object((1,3,6,1,2,1,10,246,1,7,1,4),_PwIndexMappingPeerAddr_Type())
pwIndexMappingPeerAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:pwIndexMappingPeerAddr.setStatus(_B)
_PwIndexMappingPwIndex_Type=PwIndexType
_PwIndexMappingPwIndex_Object=MibTableColumn
pwIndexMappingPwIndex=_PwIndexMappingPwIndex_Object((1,3,6,1,2,1,10,246,1,7,1,5),_PwIndexMappingPwIndex_Type())
pwIndexMappingPwIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pwIndexMappingPwIndex.setStatus(_B)
_PwPeerMappingTable_Object=MibTable
pwPeerMappingTable=_PwPeerMappingTable_Object((1,3,6,1,2,1,10,246,1,8))
if mibBuilder.loadTexts:pwPeerMappingTable.setStatus(_B)
_PwPeerMappingEntry_Object=MibTableRow
pwPeerMappingEntry=_PwPeerMappingEntry_Object((1,3,6,1,2,1,10,246,1,8,1))
pwPeerMappingEntry.setIndexNames((0,_A,_t),(0,_A,_u),(0,_A,_v),(0,_A,_w))
if mibBuilder.loadTexts:pwPeerMappingEntry.setStatus(_B)
_PwPeerMappingPeerAddrType_Type=InetAddressType
_PwPeerMappingPeerAddrType_Object=MibTableColumn
pwPeerMappingPeerAddrType=_PwPeerMappingPeerAddrType_Object((1,3,6,1,2,1,10,246,1,8,1,1),_PwPeerMappingPeerAddrType_Type())
pwPeerMappingPeerAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:pwPeerMappingPeerAddrType.setStatus(_B)
_PwPeerMappingPeerAddr_Type=InetAddress
_PwPeerMappingPeerAddr_Object=MibTableColumn
pwPeerMappingPeerAddr=_PwPeerMappingPeerAddr_Object((1,3,6,1,2,1,10,246,1,8,1,2),_PwPeerMappingPeerAddr_Type())
pwPeerMappingPeerAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:pwPeerMappingPeerAddr.setStatus(_B)
_PwPeerMappingPwType_Type=IANAPwTypeTC
_PwPeerMappingPwType_Object=MibTableColumn
pwPeerMappingPwType=_PwPeerMappingPwType_Object((1,3,6,1,2,1,10,246,1,8,1,3),_PwPeerMappingPwType_Type())
pwPeerMappingPwType.setMaxAccess(_E)
if mibBuilder.loadTexts:pwPeerMappingPwType.setStatus(_B)
_PwPeerMappingPwID_Type=PwIDType
_PwPeerMappingPwID_Object=MibTableColumn
pwPeerMappingPwID=_PwPeerMappingPwID_Object((1,3,6,1,2,1,10,246,1,8,1,4),_PwPeerMappingPwID_Type())
pwPeerMappingPwID.setMaxAccess(_E)
if mibBuilder.loadTexts:pwPeerMappingPwID.setStatus(_B)
_PwPeerMappingPwIndex_Type=PwIndexType
_PwPeerMappingPwIndex_Object=MibTableColumn
pwPeerMappingPwIndex=_PwPeerMappingPwIndex_Object((1,3,6,1,2,1,10,246,1,8,1,5),_PwPeerMappingPwIndex_Type())
pwPeerMappingPwIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPeerMappingPwIndex.setStatus(_B)
class _PwUpDownNotifEnable_Type(TruthValue):defaultValue=2
_PwUpDownNotifEnable_Type.__name__=_G
_PwUpDownNotifEnable_Object=MibScalar
pwUpDownNotifEnable=_PwUpDownNotifEnable_Object((1,3,6,1,2,1,10,246,1,9),_PwUpDownNotifEnable_Type())
pwUpDownNotifEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:pwUpDownNotifEnable.setStatus(_B)
class _PwDeletedNotifEnable_Type(TruthValue):defaultValue=2
_PwDeletedNotifEnable_Type.__name__=_G
_PwDeletedNotifEnable_Object=MibScalar
pwDeletedNotifEnable=_PwDeletedNotifEnable_Object((1,3,6,1,2,1,10,246,1,10),_PwDeletedNotifEnable_Type())
pwDeletedNotifEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:pwDeletedNotifEnable.setStatus(_B)
_PwNotifRate_Type=Unsigned32
_PwNotifRate_Object=MibScalar
pwNotifRate=_PwNotifRate_Object((1,3,6,1,2,1,10,246,1,11),_PwNotifRate_Type())
pwNotifRate.setMaxAccess(_L)
if mibBuilder.loadTexts:pwNotifRate.setStatus(_B)
_PwGenFecIndexMappingTable_Object=MibTable
pwGenFecIndexMappingTable=_PwGenFecIndexMappingTable_Object((1,3,6,1,2,1,10,246,1,12))
if mibBuilder.loadTexts:pwGenFecIndexMappingTable.setStatus(_B)
_PwGenFecIndexMappingEntry_Object=MibTableRow
pwGenFecIndexMappingEntry=_PwGenFecIndexMappingEntry_Object((1,3,6,1,2,1,10,246,1,12,1))
pwGenFecIndexMappingEntry.setIndexNames((0,_A,_x),(0,_A,_y),(0,_A,_z),(0,_A,_A0),(0,_A,_A1),(0,_A,_A2))
if mibBuilder.loadTexts:pwGenFecIndexMappingEntry.setStatus(_B)
_PwGenFecIndexMappingAGIType_Type=PwGenIdType
_PwGenFecIndexMappingAGIType_Object=MibTableColumn
pwGenFecIndexMappingAGIType=_PwGenFecIndexMappingAGIType_Object((1,3,6,1,2,1,10,246,1,12,1,1),_PwGenFecIndexMappingAGIType_Type())
pwGenFecIndexMappingAGIType.setMaxAccess(_E)
if mibBuilder.loadTexts:pwGenFecIndexMappingAGIType.setStatus(_B)
_PwGenFecIndexMappingAGI_Type=PwAttachmentIdentifierType
_PwGenFecIndexMappingAGI_Object=MibTableColumn
pwGenFecIndexMappingAGI=_PwGenFecIndexMappingAGI_Object((1,3,6,1,2,1,10,246,1,12,1,2),_PwGenFecIndexMappingAGI_Type())
pwGenFecIndexMappingAGI.setMaxAccess(_E)
if mibBuilder.loadTexts:pwGenFecIndexMappingAGI.setStatus(_B)
_PwGenFecIndexMappingLocalAIIType_Type=PwGenIdType
_PwGenFecIndexMappingLocalAIIType_Object=MibTableColumn
pwGenFecIndexMappingLocalAIIType=_PwGenFecIndexMappingLocalAIIType_Object((1,3,6,1,2,1,10,246,1,12,1,3),_PwGenFecIndexMappingLocalAIIType_Type())
pwGenFecIndexMappingLocalAIIType.setMaxAccess(_E)
if mibBuilder.loadTexts:pwGenFecIndexMappingLocalAIIType.setStatus(_B)
_PwGenFecIndexMappingLocalAII_Type=PwAttachmentIdentifierType
_PwGenFecIndexMappingLocalAII_Object=MibTableColumn
pwGenFecIndexMappingLocalAII=_PwGenFecIndexMappingLocalAII_Object((1,3,6,1,2,1,10,246,1,12,1,4),_PwGenFecIndexMappingLocalAII_Type())
pwGenFecIndexMappingLocalAII.setMaxAccess(_E)
if mibBuilder.loadTexts:pwGenFecIndexMappingLocalAII.setStatus(_B)
_PwGenFecIndexMappingRemoteAIIType_Type=PwGenIdType
_PwGenFecIndexMappingRemoteAIIType_Object=MibTableColumn
pwGenFecIndexMappingRemoteAIIType=_PwGenFecIndexMappingRemoteAIIType_Object((1,3,6,1,2,1,10,246,1,12,1,5),_PwGenFecIndexMappingRemoteAIIType_Type())
pwGenFecIndexMappingRemoteAIIType.setMaxAccess(_E)
if mibBuilder.loadTexts:pwGenFecIndexMappingRemoteAIIType.setStatus(_B)
_PwGenFecIndexMappingRemoteAII_Type=PwAttachmentIdentifierType
_PwGenFecIndexMappingRemoteAII_Object=MibTableColumn
pwGenFecIndexMappingRemoteAII=_PwGenFecIndexMappingRemoteAII_Object((1,3,6,1,2,1,10,246,1,12,1,6),_PwGenFecIndexMappingRemoteAII_Type())
pwGenFecIndexMappingRemoteAII.setMaxAccess(_E)
if mibBuilder.loadTexts:pwGenFecIndexMappingRemoteAII.setStatus(_B)
_PwGenFecIndexMappingPwIndex_Type=PwIndexType
_PwGenFecIndexMappingPwIndex_Object=MibTableColumn
pwGenFecIndexMappingPwIndex=_PwGenFecIndexMappingPwIndex_Object((1,3,6,1,2,1,10,246,1,12,1,7),_PwGenFecIndexMappingPwIndex_Type())
pwGenFecIndexMappingPwIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pwGenFecIndexMappingPwIndex.setStatus(_B)
_PwConformance_ObjectIdentity=ObjectIdentity
pwConformance=_PwConformance_ObjectIdentity((1,3,6,1,2,1,10,246,2))
_PwGroups_ObjectIdentity=ObjectIdentity
pwGroups=_PwGroups_ObjectIdentity((1,3,6,1,2,1,10,246,2,1))
_PwCompliances_ObjectIdentity=ObjectIdentity
pwCompliances=_PwCompliances_ObjectIdentity((1,3,6,1,2,1,10,246,2,2))
pwBasicGroup=ObjectGroup((1,3,6,1,2,1,10,246,2,1,1))
pwBasicGroup.setObjects(*((_A,_M),(_A,'pwOwner'),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,'pwName'),(_A,'pwDescr'),(_A,_A9),(_A,'pwUpTime'),(_A,_AA),(_A,_AB),(_A,_H),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:pwBasicGroup.setStatus(_B)
pwPwIdGroup=ObjectGroup((1,3,6,1,2,1,10,246,2,1,2))
pwPwIdGroup.setObjects((_A,_N))
if mibBuilder.loadTexts:pwPwIdGroup.setStatus(_B)
pwGeneralizedFecGroup=ObjectGroup((1,3,6,1,2,1,10,246,2,1,3))
pwGeneralizedFecGroup.setObjects(*((_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:pwGeneralizedFecGroup.setStatus(_B)
pwFcsGroup=ObjectGroup((1,3,6,1,2,1,10,246,2,1,4))
pwFcsGroup.setObjects(*((_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:pwFcsGroup.setStatus(_B)
pwFragGroup=ObjectGroup((1,3,6,1,2,1,10,246,2,1,5))
pwFragGroup.setObjects(*((_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:pwFragGroup.setStatus(_B)
pwPwStatusGroup=ObjectGroup((1,3,6,1,2,1,10,246,2,1,6))
pwPwStatusGroup.setObjects(*((_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:pwPwStatusGroup.setStatus(_B)
pwGetNextGroup=ObjectGroup((1,3,6,1,2,1,10,246,2,1,7))
pwGetNextGroup.setObjects((_A,_AT))
if mibBuilder.loadTexts:pwGetNextGroup.setStatus(_B)
pwPriorityGroup=ObjectGroup((1,3,6,1,2,1,10,246,2,1,8))
pwPriorityGroup.setObjects(*((_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:pwPriorityGroup.setStatus(_B)
pwAttachmentGroup=ObjectGroup((1,3,6,1,2,1,10,246,2,1,9))
pwAttachmentGroup.setObjects((_A,_AW))
if mibBuilder.loadTexts:pwAttachmentGroup.setStatus(_B)
pwPerformanceGeneralGroup=ObjectGroup((1,3,6,1,2,1,10,246,2,1,10))
pwPerformanceGeneralGroup.setObjects((_A,_AX))
if mibBuilder.loadTexts:pwPerformanceGeneralGroup.setStatus(_B)
pwPeformance1DayIntervalGroup=ObjectGroup((1,3,6,1,2,1,10,246,2,1,11))
pwPeformance1DayIntervalGroup.setObjects(*((_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad)))
if mibBuilder.loadTexts:pwPeformance1DayIntervalGroup.setStatus(_B)
pwPerformanceIntervalGeneralGroup=ObjectGroup((1,3,6,1,2,1,10,246,2,1,12))
pwPerformanceIntervalGeneralGroup.setObjects(*((_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:pwPerformanceIntervalGeneralGroup.setStatus(_B)
pwPeformanceIntervalGroup=ObjectGroup((1,3,6,1,2,1,10,246,2,1,13))
pwPeformanceIntervalGroup.setObjects(*((_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap)))
if mibBuilder.loadTexts:pwPeformanceIntervalGroup.setStatus(_B)
pwHCPeformanceIntervalGroup=ObjectGroup((1,3,6,1,2,1,10,246,2,1,14))
pwHCPeformanceIntervalGroup.setObjects(*((_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax)))
if mibBuilder.loadTexts:pwHCPeformanceIntervalGroup.setStatus(_B)
pwMappingTablesGroup=ObjectGroup((1,3,6,1,2,1,10,246,2,1,15))
pwMappingTablesGroup.setObjects(*((_A,_Ay),(_A,_Az),(_A,_A_)))
if mibBuilder.loadTexts:pwMappingTablesGroup.setStatus(_B)
pwNotificationControlGroup=ObjectGroup((1,3,6,1,2,1,10,246,2,1,16))
pwNotificationControlGroup.setObjects(*((_A,_B0),(_A,_B1),(_A,_B2)))
if mibBuilder.loadTexts:pwNotificationControlGroup.setStatus(_B)
pwSignalingGroup=ObjectGroup((1,3,6,1,2,1,10,246,2,1,18))
pwSignalingGroup.setObjects(*((_A,_O),(_A,_P),(_A,_B3),(_A,_B4),(_A,_B5),(_A,_B6),(_A,_B7),(_A,_B8),(_A,_B9)))
if mibBuilder.loadTexts:pwSignalingGroup.setStatus(_B)
pwDown=NotificationType((1,3,6,1,2,1,10,246,0,1))
pwDown.setObjects(*((_A,_H),(_A,_H)))
if mibBuilder.loadTexts:pwDown.setStatus(_B)
pwUp=NotificationType((1,3,6,1,2,1,10,246,0,2))
pwUp.setObjects(*((_A,_H),(_A,_H)))
if mibBuilder.loadTexts:pwUp.setStatus(_B)
pwDeleted=NotificationType((1,3,6,1,2,1,10,246,0,3))
pwDeleted.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:pwDeleted.setStatus(_B)
pwNotificationGroup=NotificationGroup((1,3,6,1,2,1,10,246,2,1,17))
pwNotificationGroup.setObjects(*((_A,'pwUp'),(_A,'pwDown'),(_A,_BA)))
if mibBuilder.loadTexts:pwNotificationGroup.setStatus(_B)
pwModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,10,246,2,2,1))
pwModuleFullCompliance.setObjects(*((_A,_Q),(_A,_BB),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:pwModuleFullCompliance.setStatus(_B)
pwModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,10,246,2,2,2))
pwModuleReadOnlyCompliance.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:pwModuleReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'pwStdMIB':pwStdMIB,'pwNotifications':pwNotifications,'pwDown':pwDown,'pwUp':pwUp,_BA:pwDeleted,'pwObjects':pwObjects,_AT:pwIndexNext,'pwTable':pwTable,'pwEntry':pwEntry,_I:pwIndex,_M:pwType,'pwOwner':pwOwner,_A3:pwPsnType,_AU:pwSetUpPriority,_AV:pwHoldingPriority,_O:pwPeerAddrType,_P:pwPeerAddr,_AW:pwAttachedPwIndex,_A4:pwIfIndex,_N:pwID,_B3:pwLocalGroupID,_AG:pwGroupAttachmentID,_AH:pwLocalAttachmentID,_AI:pwRemoteAttachmentID,_A5:pwCwPreference,_A6:pwLocalIfMtu,_B4:pwLocalIfString,_B5:pwLocalCapabAdvert,_B6:pwRemoteGroupID,_B7:pwCwStatus,_B8:pwRemoteIfMtu,_B9:pwRemoteIfString,_AQ:pwRemoteCapabilities,_AO:pwFragmentCfgSize,_AP:pwRmtFragCapability,_AM:pwFcsRetentionCfg,_AN:pwFcsRetentionStatus,_A7:pwOutboundLabel,_A8:pwInboundLabel,'pwName':pwName,'pwDescr':pwDescr,_A9:pwCreateTime,'pwUpTime':pwUpTime,_AA:pwLastChange,_AB:pwAdminStatus,_H:pwOperStatus,_AC:pwLocalStatus,_AR:pwRemoteStatusCapable,_AS:pwRemoteStatus,_Ae:pwTimeElapsed,_Af:pwValidIntervals,_AD:pwRowStatus,_AE:pwStorageType,_AF:pwOamEnable,_AJ:pwGenAGIType,_AK:pwGenLocalAIIType,_AL:pwGenRemoteAIIType,'pwPerfCurrentTable':pwPerfCurrentTable,'pwPerfCurrentEntry':pwPerfCurrentEntry,_Aq:pwPerfCurrentInHCPackets,_Ar:pwPerfCurrentInHCBytes,_As:pwPerfCurrentOutHCPackets,_At:pwPerfCurrentOutHCBytes,_Ai:pwPerfCurrentInPackets,_Aj:pwPerfCurrentInBytes,_Ak:pwPerfCurrentOutPackets,_Al:pwPerfCurrentOutBytes,'pwPerfIntervalTable':pwPerfIntervalTable,'pwPerfIntervalEntry':pwPerfIntervalEntry,_n:pwPerfIntervalNumber,_Ag:pwPerfIntervalValidData,_Ah:pwPerfIntervalTimeElapsed,_Au:pwPerfIntervalInHCPackets,_Av:pwPerfIntervalInHCBytes,_Aw:pwPerfIntervalOutHCPackets,_Ax:pwPerfIntervalOutHCBytes,_Am:pwPerfIntervalInPackets,_An:pwPerfIntervalInBytes,_Ao:pwPerfIntervalOutPackets,_Ap:pwPerfIntervalOutBytes,'pwPerf1DayIntervalTable':pwPerf1DayIntervalTable,'pwPerf1DayIntervalEntry':pwPerf1DayIntervalEntry,_o:pwPerf1DayIntervalNumber,_AY:pwPerf1DayIntervalValidData,_AZ:pwPerf1DayIntervalTimeElapsed,_Aa:pwPerf1DayIntervalInHCPackets,_Ab:pwPerf1DayIntervalInHCBytes,_Ac:pwPerf1DayIntervalOutHCPackets,_Ad:pwPerf1DayIntervalOutHCBytes,_AX:pwPerfTotalErrorPackets,'pwIndexMappingTable':pwIndexMappingTable,'pwIndexMappingEntry':pwIndexMappingEntry,_p:pwIndexMappingPwType,_q:pwIndexMappingPwID,_r:pwIndexMappingPeerAddrType,_s:pwIndexMappingPeerAddr,_Ay:pwIndexMappingPwIndex,'pwPeerMappingTable':pwPeerMappingTable,'pwPeerMappingEntry':pwPeerMappingEntry,_t:pwPeerMappingPeerAddrType,_u:pwPeerMappingPeerAddr,_v:pwPeerMappingPwType,_w:pwPeerMappingPwID,_Az:pwPeerMappingPwIndex,_B0:pwUpDownNotifEnable,_B1:pwDeletedNotifEnable,_B2:pwNotifRate,'pwGenFecIndexMappingTable':pwGenFecIndexMappingTable,'pwGenFecIndexMappingEntry':pwGenFecIndexMappingEntry,_x:pwGenFecIndexMappingAGIType,_y:pwGenFecIndexMappingAGI,_z:pwGenFecIndexMappingLocalAIIType,_A0:pwGenFecIndexMappingLocalAII,_A1:pwGenFecIndexMappingRemoteAIIType,_A2:pwGenFecIndexMappingRemoteAII,_A_:pwGenFecIndexMappingPwIndex,'pwConformance':pwConformance,'pwGroups':pwGroups,_Q:pwBasicGroup,_S:pwPwIdGroup,_T:pwGeneralizedFecGroup,_U:pwFcsGroup,_V:pwFragGroup,_W:pwPwStatusGroup,_X:pwGetNextGroup,_Y:pwPriorityGroup,_Z:pwAttachmentGroup,_BB:pwPerformanceGeneralGroup,_a:pwPeformance1DayIntervalGroup,_b:pwPerformanceIntervalGeneralGroup,_c:pwPeformanceIntervalGroup,_d:pwHCPeformanceIntervalGroup,_e:pwMappingTablesGroup,_g:pwNotificationControlGroup,_R:pwNotificationGroup,_f:pwSignalingGroup,'pwCompliances':pwCompliances,'pwModuleFullCompliance':pwModuleFullCompliance,'pwModuleReadOnlyCompliance':pwModuleReadOnlyCompliance})