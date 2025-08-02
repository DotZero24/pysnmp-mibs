_B1='pwPerformanceGeneralGroup'
_B0='pwDeleted'
_A_='pwRemoteIfString'
_Az='pwRemoteIfMtu'
_Ay='pwCwStatus'
_Ax='pwRemoteGroupID'
_Aw='pwLocalCapabAdvert'
_Av='pwLocalIfString'
_Au='pwLocalGroupID'
_At='pwNotifRate'
_As='pwDeletedNotifEnable'
_Ar='pwUpDownNotifEnable'
_Aq='pwPeerMappingPwIndex'
_Ap='pwIndexMappingPwIndex'
_Ao='pwPerfIntervalOutHCBytes'
_An='pwPerfIntervalOutHCPackets'
_Am='pwPerfIntervalInHCBytes'
_Al='pwPerfIntervalInHCPackets'
_Ak='pwPerfCurrentOutHCBytes'
_Aj='pwPerfCurrentOutHCPackets'
_Ai='pwPerfCurrentInHCBytes'
_Ah='pwPerfCurrentInHCPackets'
_Ag='pwPerfIntervalOutBytes'
_Af='pwPerfIntervalOutPackets'
_Ae='pwPerfIntervalInBytes'
_Ad='pwPerfIntervalInPackets'
_Ac='pwPerfCurrentOutBytes'
_Ab='pwPerfCurrentOutPackets'
_Aa='pwPerfCurrentInBytes'
_AZ='pwPerfCurrentInPackets'
_AY='pwPerfIntervalTimeElapsed'
_AX='pwPerfIntervalValidData'
_AW='pwValidIntervals'
_AV='pwTimeElapsed'
_AU='pwPerf1DayIntervalOutHCBytes'
_AT='pwPerf1DayIntervalOutHCPackets'
_AS='pwPerf1DayIntervalInHCBytes'
_AR='pwPerf1DayIntervalInHCPackets'
_AQ='pwPerf1DayIntervalTimeElapsed'
_AP='pwPerf1DayIntervalValidData'
_AO='pwPerfTotalErrorPackets'
_AN='pwAttachedPwIndex'
_AM='pwHoldingPriority'
_AL='pwSetUpPriority'
_AK='pwIndexNext'
_AJ='pwRemoteStatus'
_AI='pwRemoteStatusCapable'
_AH='pwRemoteCapabilities'
_AG='pwRmtFragCapability'
_AF='pwFragmentCfgSize'
_AE='pwFcsRetentionStatus'
_AD='pwFcsRetentionCfg'
_AC='pwPeerAttachmentID'
_AB='pwLocalAttachmentID'
_AA='pwGroupAttachmentID'
_A9='pwOamEnable'
_A8='pwStorageType'
_A7='pwRowStatus'
_A6='pwLocalStatus'
_A5='pwAdminStatus'
_A4='pwLastChange'
_A3='pwCreateTime'
_A2='pwInboundLabel'
_A1='pwOutboundLabel'
_A0='pwLocalIfMtu'
_z='pwCwPreference'
_y='pwIfIndex'
_x='pwPsnType'
_w='pwOwner'
_v='pwPeerMappingPwID'
_u='pwPeerMappingPwType'
_t='pwPeerMappingPeerAddr'
_s='pwPeerMappingPeerAddrType'
_r='pwIndexMappingPeerAddr'
_q='pwIndexMappingPeerAddrType'
_p='pwIndexMappingPwID'
_o='pwIndexMappingPwType'
_n='pwPerf1DayIntervalNumber'
_m='pwPerfIntervalNumber'
_l='StorageType'
_k='SnmpAdminString'
_j='PwIndexOrZeroType'
_i='PwFragSize'
_h='InetAddressType'
_g='InterfaceIndexOrZero'
_f='pwNotificationControlGroup'
_e='pwSignalingGroup'
_d='pwMappingTablesGroup'
_c='pwHCPeformanceIntervalGroup'
_b='pwPeformanceIntervalGroup'
_a='pwPerformanceIntervalGeneralGroup'
_Z='pwPeformance1DayIntervalGroup'
_Y='pwAttachmentGroup'
_X='pwPriorityGroup'
_W='pwGetNextGroup'
_V='pwPwStatusGroup'
_U='pwFragGroup'
_T='pwFcsGroup'
_S='pwGeneralizedFecGroup'
_R='pwPwIdGroup'
_Q='pwNotificationGroup'
_P='pwBasicGroup'
_O='pwPeerAddr'
_N='pwPeerAddrType'
_M='pwID'
_L='pwType'
_K='read-write'
_J='Unsigned32'
_I='pwIndex'
_H='pwOperStatus'
_G='TruthValue'
_F='Integer32'
_E='not-accessible'
_D='read-create'
_C='read-only'
_B='current'
_A='PW-STD-R-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HCPerfCurrentCount,HCPerfIntervalCount,HCPerfTimeElapsed,HCPerfValidIntervals=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfCurrentCount','HCPerfIntervalCount','HCPerfTimeElapsed','HCPerfValidIntervals')
IANAPwCapabilities,IANAPwPsnTypeTC,IANAPwTypeTC=mibBuilder.importSymbols('IANA-PWE3-R-MIB','IANAPwCapabilities','IANAPwPsnTypeTC','IANAPwTypeTC')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_g)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_h)
PwAttachmentIdentifierType,PwCwStatusTC,PwFragSize,PwFragStatus,PwGroupID,PwIDType,PwIndexOrZeroType,PwIndexType,PwOperStatusTC,PwStatus=mibBuilder.importSymbols('PW-TC-STD-R-MIB','PwAttachmentIdentifierType','PwCwStatusTC',_i,'PwFragStatus','PwGroupID','PwIDType',_j,'PwIndexType','PwOperStatusTC','PwStatus')
PerfCurrentCount,PerfIntervalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_k)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso','transmission')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_l,'TextualConvention','TimeStamp',_G)
pwStdMIBR=ModuleIdentity((1,3,6,1,4,1,164,20,10))
if mibBuilder.loadTexts:pwStdMIBR.setRevisions(('2007-02-04 12:00',))
_RadExperimental_ObjectIdentity=ObjectIdentity
radExperimental=_RadExperimental_ObjectIdentity((1,3,6,1,4,1,164,20))
_PwNotifications_ObjectIdentity=ObjectIdentity
pwNotifications=_PwNotifications_ObjectIdentity((1,3,6,1,4,1,164,20,10,0))
_PwObjects_ObjectIdentity=ObjectIdentity
pwObjects=_PwObjects_ObjectIdentity((1,3,6,1,4,1,164,20,10,1))
_PwIndexNext_Type=Unsigned32
_PwIndexNext_Object=MibScalar
pwIndexNext=_PwIndexNext_Object((1,3,6,1,4,1,164,20,10,1,1),_PwIndexNext_Type())
pwIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:pwIndexNext.setStatus(_B)
_PwTable_Object=MibTable
pwTable=_PwTable_Object((1,3,6,1,4,1,164,20,10,1,2))
if mibBuilder.loadTexts:pwTable.setStatus(_B)
_PwEntry_Object=MibTableRow
pwEntry=_PwEntry_Object((1,3,6,1,4,1,164,20,10,1,2,1))
pwEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:pwEntry.setStatus(_B)
_PwIndex_Type=PwIndexType
_PwIndex_Object=MibTableColumn
pwIndex=_PwIndex_Object((1,3,6,1,4,1,164,20,10,1,2,1,1),_PwIndex_Type())
pwIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pwIndex.setStatus(_B)
_PwType_Type=IANAPwTypeTC
_PwType_Object=MibTableColumn
pwType=_PwType_Object((1,3,6,1,4,1,164,20,10,1,2,1,2),_PwType_Type())
pwType.setMaxAccess(_D)
if mibBuilder.loadTexts:pwType.setStatus(_B)
class _PwOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('manual',1),('pwIdFecSignaling',2),('genFecSignaling',3),('l2tpControlProtocol',4),('other',5)))
_PwOwner_Type.__name__=_F
_PwOwner_Object=MibTableColumn
pwOwner=_PwOwner_Object((1,3,6,1,4,1,164,20,10,1,2,1,3),_PwOwner_Type())
pwOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:pwOwner.setStatus(_B)
_PwPsnType_Type=IANAPwPsnTypeTC
_PwPsnType_Object=MibTableColumn
pwPsnType=_PwPsnType_Object((1,3,6,1,4,1,164,20,10,1,2,1,4),_PwPsnType_Type())
pwPsnType.setMaxAccess(_D)
if mibBuilder.loadTexts:pwPsnType.setStatus(_B)
class _PwSetUpPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PwSetUpPriority_Type.__name__=_F
_PwSetUpPriority_Object=MibTableColumn
pwSetUpPriority=_PwSetUpPriority_Object((1,3,6,1,4,1,164,20,10,1,2,1,5),_PwSetUpPriority_Type())
pwSetUpPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:pwSetUpPriority.setStatus(_B)
class _PwHoldingPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PwHoldingPriority_Type.__name__=_F
_PwHoldingPriority_Object=MibTableColumn
pwHoldingPriority=_PwHoldingPriority_Object((1,3,6,1,4,1,164,20,10,1,2,1,6),_PwHoldingPriority_Type())
pwHoldingPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:pwHoldingPriority.setStatus(_B)
class _PwPeerAddrType_Type(InetAddressType):defaultValue=1
_PwPeerAddrType_Type.__name__=_h
_PwPeerAddrType_Object=MibTableColumn
pwPeerAddrType=_PwPeerAddrType_Object((1,3,6,1,4,1,164,20,10,1,2,1,8),_PwPeerAddrType_Type())
pwPeerAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:pwPeerAddrType.setStatus(_B)
_PwPeerAddr_Type=InetAddress
_PwPeerAddr_Object=MibTableColumn
pwPeerAddr=_PwPeerAddr_Object((1,3,6,1,4,1,164,20,10,1,2,1,9),_PwPeerAddr_Type())
pwPeerAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:pwPeerAddr.setStatus(_B)
class _PwAttachedPwIndex_Type(PwIndexOrZeroType):defaultValue=0
_PwAttachedPwIndex_Type.__name__=_j
_PwAttachedPwIndex_Object=MibTableColumn
pwAttachedPwIndex=_PwAttachedPwIndex_Object((1,3,6,1,4,1,164,20,10,1,2,1,10),_PwAttachedPwIndex_Type())
pwAttachedPwIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAttachedPwIndex.setStatus(_B)
class _PwIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_PwIfIndex_Type.__name__=_g
_PwIfIndex_Object=MibTableColumn
pwIfIndex=_PwIfIndex_Object((1,3,6,1,4,1,164,20,10,1,2,1,11),_PwIfIndex_Type())
pwIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:pwIfIndex.setStatus(_B)
_PwID_Type=PwIDType
_PwID_Object=MibTableColumn
pwID=_PwID_Object((1,3,6,1,4,1,164,20,10,1,2,1,12),_PwID_Type())
pwID.setMaxAccess(_D)
if mibBuilder.loadTexts:pwID.setStatus(_B)
_PwLocalGroupID_Type=PwGroupID
_PwLocalGroupID_Object=MibTableColumn
pwLocalGroupID=_PwLocalGroupID_Object((1,3,6,1,4,1,164,20,10,1,2,1,13),_PwLocalGroupID_Type())
pwLocalGroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:pwLocalGroupID.setStatus(_B)
_PwGroupAttachmentID_Type=PwAttachmentIdentifierType
_PwGroupAttachmentID_Object=MibTableColumn
pwGroupAttachmentID=_PwGroupAttachmentID_Object((1,3,6,1,4,1,164,20,10,1,2,1,14),_PwGroupAttachmentID_Type())
pwGroupAttachmentID.setMaxAccess(_D)
if mibBuilder.loadTexts:pwGroupAttachmentID.setStatus(_B)
_PwLocalAttachmentID_Type=PwAttachmentIdentifierType
_PwLocalAttachmentID_Object=MibTableColumn
pwLocalAttachmentID=_PwLocalAttachmentID_Object((1,3,6,1,4,1,164,20,10,1,2,1,15),_PwLocalAttachmentID_Type())
pwLocalAttachmentID.setMaxAccess(_D)
if mibBuilder.loadTexts:pwLocalAttachmentID.setStatus(_B)
_PwPeerAttachmentID_Type=PwAttachmentIdentifierType
_PwPeerAttachmentID_Object=MibTableColumn
pwPeerAttachmentID=_PwPeerAttachmentID_Object((1,3,6,1,4,1,164,20,10,1,2,1,16),_PwPeerAttachmentID_Type())
pwPeerAttachmentID.setMaxAccess(_D)
if mibBuilder.loadTexts:pwPeerAttachmentID.setStatus(_B)
class _PwCwPreference_Type(TruthValue):defaultValue=2
_PwCwPreference_Type.__name__=_G
_PwCwPreference_Object=MibTableColumn
pwCwPreference=_PwCwPreference_Object((1,3,6,1,4,1,164,20,10,1,2,1,17),_PwCwPreference_Type())
pwCwPreference.setMaxAccess(_D)
if mibBuilder.loadTexts:pwCwPreference.setStatus(_B)
class _PwLocalIfMtu_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PwLocalIfMtu_Type.__name__=_J
_PwLocalIfMtu_Object=MibTableColumn
pwLocalIfMtu=_PwLocalIfMtu_Object((1,3,6,1,4,1,164,20,10,1,2,1,18),_PwLocalIfMtu_Type())
pwLocalIfMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:pwLocalIfMtu.setStatus(_B)
class _PwLocalIfString_Type(TruthValue):defaultValue=2
_PwLocalIfString_Type.__name__=_G
_PwLocalIfString_Object=MibTableColumn
pwLocalIfString=_PwLocalIfString_Object((1,3,6,1,4,1,164,20,10,1,2,1,19),_PwLocalIfString_Type())
pwLocalIfString.setMaxAccess(_D)
if mibBuilder.loadTexts:pwLocalIfString.setStatus(_B)
_PwLocalCapabAdvert_Type=IANAPwCapabilities
_PwLocalCapabAdvert_Object=MibTableColumn
pwLocalCapabAdvert=_PwLocalCapabAdvert_Object((1,3,6,1,4,1,164,20,10,1,2,1,20),_PwLocalCapabAdvert_Type())
pwLocalCapabAdvert.setMaxAccess(_D)
if mibBuilder.loadTexts:pwLocalCapabAdvert.setStatus(_B)
_PwRemoteGroupID_Type=PwGroupID
_PwRemoteGroupID_Object=MibTableColumn
pwRemoteGroupID=_PwRemoteGroupID_Object((1,3,6,1,4,1,164,20,10,1,2,1,21),_PwRemoteGroupID_Type())
pwRemoteGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:pwRemoteGroupID.setStatus(_B)
_PwCwStatus_Type=PwCwStatusTC
_PwCwStatus_Object=MibTableColumn
pwCwStatus=_PwCwStatus_Object((1,3,6,1,4,1,164,20,10,1,2,1,22),_PwCwStatus_Type())
pwCwStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pwCwStatus.setStatus(_B)
_PwRemoteIfMtu_Type=Unsigned32
_PwRemoteIfMtu_Object=MibTableColumn
pwRemoteIfMtu=_PwRemoteIfMtu_Object((1,3,6,1,4,1,164,20,10,1,2,1,23),_PwRemoteIfMtu_Type())
pwRemoteIfMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:pwRemoteIfMtu.setStatus(_B)
class _PwRemoteIfString_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_PwRemoteIfString_Type.__name__=_k
_PwRemoteIfString_Object=MibTableColumn
pwRemoteIfString=_PwRemoteIfString_Object((1,3,6,1,4,1,164,20,10,1,2,1,24),_PwRemoteIfString_Type())
pwRemoteIfString.setMaxAccess(_C)
if mibBuilder.loadTexts:pwRemoteIfString.setStatus(_B)
_PwRemoteCapabilities_Type=IANAPwCapabilities
_PwRemoteCapabilities_Object=MibTableColumn
pwRemoteCapabilities=_PwRemoteCapabilities_Object((1,3,6,1,4,1,164,20,10,1,2,1,25),_PwRemoteCapabilities_Type())
pwRemoteCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:pwRemoteCapabilities.setStatus(_B)
class _PwFragmentCfgSize_Type(PwFragSize):defaultValue=0
_PwFragmentCfgSize_Type.__name__=_i
_PwFragmentCfgSize_Object=MibTableColumn
pwFragmentCfgSize=_PwFragmentCfgSize_Object((1,3,6,1,4,1,164,20,10,1,2,1,26),_PwFragmentCfgSize_Type())
pwFragmentCfgSize.setMaxAccess(_D)
if mibBuilder.loadTexts:pwFragmentCfgSize.setStatus(_B)
if mibBuilder.loadTexts:pwFragmentCfgSize.setUnits('bytes')
_PwRmtFragCapability_Type=PwFragStatus
_PwRmtFragCapability_Object=MibTableColumn
pwRmtFragCapability=_PwRmtFragCapability_Object((1,3,6,1,4,1,164,20,10,1,2,1,27),_PwRmtFragCapability_Type())
pwRmtFragCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:pwRmtFragCapability.setStatus(_B)
class _PwFcsRetentionCfg_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fcsRetentionDisable',1),('fcsRetentionEnable',2)))
_PwFcsRetentionCfg_Type.__name__=_F
_PwFcsRetentionCfg_Object=MibTableColumn
pwFcsRetentionCfg=_PwFcsRetentionCfg_Object((1,3,6,1,4,1,164,20,10,1,2,1,28),_PwFcsRetentionCfg_Type())
pwFcsRetentionCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:pwFcsRetentionCfg.setStatus(_B)
class _PwFcsRetentionStatus_Type(Bits):namedValues=NamedValues(*(('remoteIndicationUnknown',0),('remoteRequestFcsRetention',1),('fcsRetentionEnabled',2),('fcsRetentionDisabled',3),('localFcsRetentionCfgErr',4),('fcsRetentionFcsSizeMismatch',5)))
_PwFcsRetentionStatus_Type.__name__='Bits'
_PwFcsRetentionStatus_Object=MibTableColumn
pwFcsRetentionStatus=_PwFcsRetentionStatus_Object((1,3,6,1,4,1,164,20,10,1,2,1,29),_PwFcsRetentionStatus_Type())
pwFcsRetentionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pwFcsRetentionStatus.setStatus(_B)
_PwOutboundLabel_Type=Unsigned32
_PwOutboundLabel_Object=MibTableColumn
pwOutboundLabel=_PwOutboundLabel_Object((1,3,6,1,4,1,164,20,10,1,2,1,30),_PwOutboundLabel_Type())
pwOutboundLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:pwOutboundLabel.setStatus(_B)
_PwInboundLabel_Type=Unsigned32
_PwInboundLabel_Object=MibTableColumn
pwInboundLabel=_PwInboundLabel_Object((1,3,6,1,4,1,164,20,10,1,2,1,31),_PwInboundLabel_Type())
pwInboundLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:pwInboundLabel.setStatus(_B)
_PwName_Type=SnmpAdminString
_PwName_Object=MibTableColumn
pwName=_PwName_Object((1,3,6,1,4,1,164,20,10,1,2,1,32),_PwName_Type())
pwName.setMaxAccess(_D)
if mibBuilder.loadTexts:pwName.setStatus(_B)
_PwDescr_Type=SnmpAdminString
_PwDescr_Object=MibTableColumn
pwDescr=_PwDescr_Object((1,3,6,1,4,1,164,20,10,1,2,1,33),_PwDescr_Type())
pwDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:pwDescr.setStatus(_B)
_PwCreateTime_Type=TimeStamp
_PwCreateTime_Object=MibTableColumn
pwCreateTime=_PwCreateTime_Object((1,3,6,1,4,1,164,20,10,1,2,1,34),_PwCreateTime_Type())
pwCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pwCreateTime.setStatus(_B)
_PwUpTime_Type=TimeTicks
_PwUpTime_Object=MibTableColumn
pwUpTime=_PwUpTime_Object((1,3,6,1,4,1,164,20,10,1,2,1,35),_PwUpTime_Type())
pwUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pwUpTime.setStatus(_B)
_PwLastChange_Type=TimeTicks
_PwLastChange_Object=MibTableColumn
pwLastChange=_PwLastChange_Object((1,3,6,1,4,1,164,20,10,1,2,1,36),_PwLastChange_Type())
pwLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:pwLastChange.setStatus(_B)
class _PwAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_PwAdminStatus_Type.__name__=_F
_PwAdminStatus_Object=MibTableColumn
pwAdminStatus=_PwAdminStatus_Object((1,3,6,1,4,1,164,20,10,1,2,1,37),_PwAdminStatus_Type())
pwAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAdminStatus.setStatus(_B)
_PwOperStatus_Type=PwOperStatusTC
_PwOperStatus_Object=MibTableColumn
pwOperStatus=_PwOperStatus_Object((1,3,6,1,4,1,164,20,10,1,2,1,38),_PwOperStatus_Type())
pwOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pwOperStatus.setStatus(_B)
_PwLocalStatus_Type=PwStatus
_PwLocalStatus_Object=MibTableColumn
pwLocalStatus=_PwLocalStatus_Object((1,3,6,1,4,1,164,20,10,1,2,1,39),_PwLocalStatus_Type())
pwLocalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pwLocalStatus.setStatus(_B)
class _PwRemoteStatusCapable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notApplicable',1),('notYetKnown',2),('remoteCapable',3),('remoteNotCapable',4)))
_PwRemoteStatusCapable_Type.__name__=_F
_PwRemoteStatusCapable_Object=MibTableColumn
pwRemoteStatusCapable=_PwRemoteStatusCapable_Object((1,3,6,1,4,1,164,20,10,1,2,1,40),_PwRemoteStatusCapable_Type())
pwRemoteStatusCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:pwRemoteStatusCapable.setStatus(_B)
_PwRemoteStatus_Type=PwStatus
_PwRemoteStatus_Object=MibTableColumn
pwRemoteStatus=_PwRemoteStatus_Object((1,3,6,1,4,1,164,20,10,1,2,1,41),_PwRemoteStatus_Type())
pwRemoteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pwRemoteStatus.setStatus(_B)
_PwTimeElapsed_Type=HCPerfTimeElapsed
_PwTimeElapsed_Object=MibTableColumn
pwTimeElapsed=_PwTimeElapsed_Object((1,3,6,1,4,1,164,20,10,1,2,1,42),_PwTimeElapsed_Type())
pwTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTimeElapsed.setStatus(_B)
_PwValidIntervals_Type=HCPerfValidIntervals
_PwValidIntervals_Object=MibTableColumn
pwValidIntervals=_PwValidIntervals_Object((1,3,6,1,4,1,164,20,10,1,2,1,43),_PwValidIntervals_Type())
pwValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:pwValidIntervals.setStatus(_B)
_PwRowStatus_Type=RowStatus
_PwRowStatus_Object=MibTableColumn
pwRowStatus=_PwRowStatus_Object((1,3,6,1,4,1,164,20,10,1,2,1,44),_PwRowStatus_Type())
pwRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pwRowStatus.setStatus(_B)
class _PwStorageType_Type(StorageType):defaultValue=3
_PwStorageType_Type.__name__=_l
_PwStorageType_Object=MibTableColumn
pwStorageType=_PwStorageType_Object((1,3,6,1,4,1,164,20,10,1,2,1,45),_PwStorageType_Type())
pwStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:pwStorageType.setStatus(_B)
class _PwOamEnable_Type(TruthValue):defaultValue=1
_PwOamEnable_Type.__name__=_G
_PwOamEnable_Object=MibTableColumn
pwOamEnable=_PwOamEnable_Object((1,3,6,1,4,1,164,20,10,1,2,1,46),_PwOamEnable_Type())
pwOamEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:pwOamEnable.setStatus(_B)
_PwPerfCurrentTable_Object=MibTable
pwPerfCurrentTable=_PwPerfCurrentTable_Object((1,3,6,1,4,1,164,20,10,1,3))
if mibBuilder.loadTexts:pwPerfCurrentTable.setStatus(_B)
_PwPerfCurrentEntry_Object=MibTableRow
pwPerfCurrentEntry=_PwPerfCurrentEntry_Object((1,3,6,1,4,1,164,20,10,1,3,1))
pwPerfCurrentEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:pwPerfCurrentEntry.setStatus(_B)
_PwPerfCurrentInHCPackets_Type=HCPerfCurrentCount
_PwPerfCurrentInHCPackets_Object=MibTableColumn
pwPerfCurrentInHCPackets=_PwPerfCurrentInHCPackets_Object((1,3,6,1,4,1,164,20,10,1,3,1,1),_PwPerfCurrentInHCPackets_Type())
pwPerfCurrentInHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfCurrentInHCPackets.setStatus(_B)
_PwPerfCurrentInHCBytes_Type=HCPerfCurrentCount
_PwPerfCurrentInHCBytes_Object=MibTableColumn
pwPerfCurrentInHCBytes=_PwPerfCurrentInHCBytes_Object((1,3,6,1,4,1,164,20,10,1,3,1,2),_PwPerfCurrentInHCBytes_Type())
pwPerfCurrentInHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfCurrentInHCBytes.setStatus(_B)
_PwPerfCurrentOutHCPackets_Type=HCPerfCurrentCount
_PwPerfCurrentOutHCPackets_Object=MibTableColumn
pwPerfCurrentOutHCPackets=_PwPerfCurrentOutHCPackets_Object((1,3,6,1,4,1,164,20,10,1,3,1,3),_PwPerfCurrentOutHCPackets_Type())
pwPerfCurrentOutHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfCurrentOutHCPackets.setStatus(_B)
_PwPerfCurrentOutHCBytes_Type=HCPerfCurrentCount
_PwPerfCurrentOutHCBytes_Object=MibTableColumn
pwPerfCurrentOutHCBytes=_PwPerfCurrentOutHCBytes_Object((1,3,6,1,4,1,164,20,10,1,3,1,4),_PwPerfCurrentOutHCBytes_Type())
pwPerfCurrentOutHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfCurrentOutHCBytes.setStatus(_B)
_PwPerfCurrentInPackets_Type=PerfCurrentCount
_PwPerfCurrentInPackets_Object=MibTableColumn
pwPerfCurrentInPackets=_PwPerfCurrentInPackets_Object((1,3,6,1,4,1,164,20,10,1,3,1,5),_PwPerfCurrentInPackets_Type())
pwPerfCurrentInPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfCurrentInPackets.setStatus(_B)
_PwPerfCurrentInBytes_Type=PerfCurrentCount
_PwPerfCurrentInBytes_Object=MibTableColumn
pwPerfCurrentInBytes=_PwPerfCurrentInBytes_Object((1,3,6,1,4,1,164,20,10,1,3,1,6),_PwPerfCurrentInBytes_Type())
pwPerfCurrentInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfCurrentInBytes.setStatus(_B)
_PwPerfCurrentOutPackets_Type=PerfCurrentCount
_PwPerfCurrentOutPackets_Object=MibTableColumn
pwPerfCurrentOutPackets=_PwPerfCurrentOutPackets_Object((1,3,6,1,4,1,164,20,10,1,3,1,7),_PwPerfCurrentOutPackets_Type())
pwPerfCurrentOutPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfCurrentOutPackets.setStatus(_B)
_PwPerfCurrentOutBytes_Type=PerfCurrentCount
_PwPerfCurrentOutBytes_Object=MibTableColumn
pwPerfCurrentOutBytes=_PwPerfCurrentOutBytes_Object((1,3,6,1,4,1,164,20,10,1,3,1,8),_PwPerfCurrentOutBytes_Type())
pwPerfCurrentOutBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfCurrentOutBytes.setStatus(_B)
_PwPerfIntervalTable_Object=MibTable
pwPerfIntervalTable=_PwPerfIntervalTable_Object((1,3,6,1,4,1,164,20,10,1,4))
if mibBuilder.loadTexts:pwPerfIntervalTable.setStatus(_B)
_PwPerfIntervalEntry_Object=MibTableRow
pwPerfIntervalEntry=_PwPerfIntervalEntry_Object((1,3,6,1,4,1,164,20,10,1,4,1))
pwPerfIntervalEntry.setIndexNames((0,_A,_I),(0,_A,_m))
if mibBuilder.loadTexts:pwPerfIntervalEntry.setStatus(_B)
class _PwPerfIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_PwPerfIntervalNumber_Type.__name__=_F
_PwPerfIntervalNumber_Object=MibTableColumn
pwPerfIntervalNumber=_PwPerfIntervalNumber_Object((1,3,6,1,4,1,164,20,10,1,4,1,1),_PwPerfIntervalNumber_Type())
pwPerfIntervalNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:pwPerfIntervalNumber.setStatus(_B)
_PwPerfIntervalValidData_Type=TruthValue
_PwPerfIntervalValidData_Object=MibTableColumn
pwPerfIntervalValidData=_PwPerfIntervalValidData_Object((1,3,6,1,4,1,164,20,10,1,4,1,2),_PwPerfIntervalValidData_Type())
pwPerfIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalValidData.setStatus(_B)
_PwPerfIntervalTimeElapsed_Type=HCPerfTimeElapsed
_PwPerfIntervalTimeElapsed_Object=MibTableColumn
pwPerfIntervalTimeElapsed=_PwPerfIntervalTimeElapsed_Object((1,3,6,1,4,1,164,20,10,1,4,1,3),_PwPerfIntervalTimeElapsed_Type())
pwPerfIntervalTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalTimeElapsed.setStatus(_B)
_PwPerfIntervalInHCPackets_Type=HCPerfIntervalCount
_PwPerfIntervalInHCPackets_Object=MibTableColumn
pwPerfIntervalInHCPackets=_PwPerfIntervalInHCPackets_Object((1,3,6,1,4,1,164,20,10,1,4,1,4),_PwPerfIntervalInHCPackets_Type())
pwPerfIntervalInHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalInHCPackets.setStatus(_B)
_PwPerfIntervalInHCBytes_Type=HCPerfIntervalCount
_PwPerfIntervalInHCBytes_Object=MibTableColumn
pwPerfIntervalInHCBytes=_PwPerfIntervalInHCBytes_Object((1,3,6,1,4,1,164,20,10,1,4,1,5),_PwPerfIntervalInHCBytes_Type())
pwPerfIntervalInHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalInHCBytes.setStatus(_B)
_PwPerfIntervalOutHCPackets_Type=HCPerfIntervalCount
_PwPerfIntervalOutHCPackets_Object=MibTableColumn
pwPerfIntervalOutHCPackets=_PwPerfIntervalOutHCPackets_Object((1,3,6,1,4,1,164,20,10,1,4,1,6),_PwPerfIntervalOutHCPackets_Type())
pwPerfIntervalOutHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalOutHCPackets.setStatus(_B)
_PwPerfIntervalOutHCBytes_Type=HCPerfIntervalCount
_PwPerfIntervalOutHCBytes_Object=MibTableColumn
pwPerfIntervalOutHCBytes=_PwPerfIntervalOutHCBytes_Object((1,3,6,1,4,1,164,20,10,1,4,1,7),_PwPerfIntervalOutHCBytes_Type())
pwPerfIntervalOutHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalOutHCBytes.setStatus(_B)
_PwPerfIntervalInPackets_Type=PerfIntervalCount
_PwPerfIntervalInPackets_Object=MibTableColumn
pwPerfIntervalInPackets=_PwPerfIntervalInPackets_Object((1,3,6,1,4,1,164,20,10,1,4,1,8),_PwPerfIntervalInPackets_Type())
pwPerfIntervalInPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalInPackets.setStatus(_B)
_PwPerfIntervalInBytes_Type=PerfIntervalCount
_PwPerfIntervalInBytes_Object=MibTableColumn
pwPerfIntervalInBytes=_PwPerfIntervalInBytes_Object((1,3,6,1,4,1,164,20,10,1,4,1,9),_PwPerfIntervalInBytes_Type())
pwPerfIntervalInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalInBytes.setStatus(_B)
_PwPerfIntervalOutPackets_Type=PerfIntervalCount
_PwPerfIntervalOutPackets_Object=MibTableColumn
pwPerfIntervalOutPackets=_PwPerfIntervalOutPackets_Object((1,3,6,1,4,1,164,20,10,1,4,1,10),_PwPerfIntervalOutPackets_Type())
pwPerfIntervalOutPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalOutPackets.setStatus(_B)
_PwPerfIntervalOutBytes_Type=PerfIntervalCount
_PwPerfIntervalOutBytes_Object=MibTableColumn
pwPerfIntervalOutBytes=_PwPerfIntervalOutBytes_Object((1,3,6,1,4,1,164,20,10,1,4,1,11),_PwPerfIntervalOutBytes_Type())
pwPerfIntervalOutBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfIntervalOutBytes.setStatus(_B)
_PwPerf1DayIntervalTable_Object=MibTable
pwPerf1DayIntervalTable=_PwPerf1DayIntervalTable_Object((1,3,6,1,4,1,164,20,10,1,5))
if mibBuilder.loadTexts:pwPerf1DayIntervalTable.setStatus(_B)
_PwPerf1DayIntervalEntry_Object=MibTableRow
pwPerf1DayIntervalEntry=_PwPerf1DayIntervalEntry_Object((1,3,6,1,4,1,164,20,10,1,5,1))
pwPerf1DayIntervalEntry.setIndexNames((0,_A,_I),(0,_A,_n))
if mibBuilder.loadTexts:pwPerf1DayIntervalEntry.setStatus(_B)
class _PwPerf1DayIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_PwPerf1DayIntervalNumber_Type.__name__=_J
_PwPerf1DayIntervalNumber_Object=MibTableColumn
pwPerf1DayIntervalNumber=_PwPerf1DayIntervalNumber_Object((1,3,6,1,4,1,164,20,10,1,5,1,1),_PwPerf1DayIntervalNumber_Type())
pwPerf1DayIntervalNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:pwPerf1DayIntervalNumber.setStatus(_B)
_PwPerf1DayIntervalValidData_Type=TruthValue
_PwPerf1DayIntervalValidData_Object=MibTableColumn
pwPerf1DayIntervalValidData=_PwPerf1DayIntervalValidData_Object((1,3,6,1,4,1,164,20,10,1,5,1,2),_PwPerf1DayIntervalValidData_Type())
pwPerf1DayIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerf1DayIntervalValidData.setStatus(_B)
_PwPerf1DayIntervalTimeElapsed_Type=HCPerfTimeElapsed
_PwPerf1DayIntervalTimeElapsed_Object=MibTableColumn
pwPerf1DayIntervalTimeElapsed=_PwPerf1DayIntervalTimeElapsed_Object((1,3,6,1,4,1,164,20,10,1,5,1,3),_PwPerf1DayIntervalTimeElapsed_Type())
pwPerf1DayIntervalTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerf1DayIntervalTimeElapsed.setStatus(_B)
if mibBuilder.loadTexts:pwPerf1DayIntervalTimeElapsed.setUnits('seconds')
_PwPerf1DayIntervalInHCPackets_Type=Counter64
_PwPerf1DayIntervalInHCPackets_Object=MibTableColumn
pwPerf1DayIntervalInHCPackets=_PwPerf1DayIntervalInHCPackets_Object((1,3,6,1,4,1,164,20,10,1,5,1,4),_PwPerf1DayIntervalInHCPackets_Type())
pwPerf1DayIntervalInHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerf1DayIntervalInHCPackets.setStatus(_B)
_PwPerf1DayIntervalInHCBytes_Type=Counter64
_PwPerf1DayIntervalInHCBytes_Object=MibTableColumn
pwPerf1DayIntervalInHCBytes=_PwPerf1DayIntervalInHCBytes_Object((1,3,6,1,4,1,164,20,10,1,5,1,5),_PwPerf1DayIntervalInHCBytes_Type())
pwPerf1DayIntervalInHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerf1DayIntervalInHCBytes.setStatus(_B)
_PwPerf1DayIntervalOutHCPackets_Type=Counter64
_PwPerf1DayIntervalOutHCPackets_Object=MibTableColumn
pwPerf1DayIntervalOutHCPackets=_PwPerf1DayIntervalOutHCPackets_Object((1,3,6,1,4,1,164,20,10,1,5,1,6),_PwPerf1DayIntervalOutHCPackets_Type())
pwPerf1DayIntervalOutHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerf1DayIntervalOutHCPackets.setStatus(_B)
_PwPerf1DayIntervalOutHCBytes_Type=Counter64
_PwPerf1DayIntervalOutHCBytes_Object=MibTableColumn
pwPerf1DayIntervalOutHCBytes=_PwPerf1DayIntervalOutHCBytes_Object((1,3,6,1,4,1,164,20,10,1,5,1,7),_PwPerf1DayIntervalOutHCBytes_Type())
pwPerf1DayIntervalOutHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerf1DayIntervalOutHCBytes.setStatus(_B)
_PwPerfTotalErrorPackets_Type=Counter32
_PwPerfTotalErrorPackets_Object=MibScalar
pwPerfTotalErrorPackets=_PwPerfTotalErrorPackets_Object((1,3,6,1,4,1,164,20,10,1,6),_PwPerfTotalErrorPackets_Type())
pwPerfTotalErrorPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfTotalErrorPackets.setStatus(_B)
_PwIndexMappingTable_Object=MibTable
pwIndexMappingTable=_PwIndexMappingTable_Object((1,3,6,1,4,1,164,20,10,1,7))
if mibBuilder.loadTexts:pwIndexMappingTable.setStatus(_B)
_PwIndexMappingEntry_Object=MibTableRow
pwIndexMappingEntry=_PwIndexMappingEntry_Object((1,3,6,1,4,1,164,20,10,1,7,1))
pwIndexMappingEntry.setIndexNames((0,_A,_o),(0,_A,_p),(0,_A,_q),(0,_A,_r))
if mibBuilder.loadTexts:pwIndexMappingEntry.setStatus(_B)
_PwIndexMappingPwType_Type=IANAPwTypeTC
_PwIndexMappingPwType_Object=MibTableColumn
pwIndexMappingPwType=_PwIndexMappingPwType_Object((1,3,6,1,4,1,164,20,10,1,7,1,1),_PwIndexMappingPwType_Type())
pwIndexMappingPwType.setMaxAccess(_E)
if mibBuilder.loadTexts:pwIndexMappingPwType.setStatus(_B)
_PwIndexMappingPwID_Type=PwIDType
_PwIndexMappingPwID_Object=MibTableColumn
pwIndexMappingPwID=_PwIndexMappingPwID_Object((1,3,6,1,4,1,164,20,10,1,7,1,2),_PwIndexMappingPwID_Type())
pwIndexMappingPwID.setMaxAccess(_E)
if mibBuilder.loadTexts:pwIndexMappingPwID.setStatus(_B)
_PwIndexMappingPeerAddrType_Type=InetAddressType
_PwIndexMappingPeerAddrType_Object=MibTableColumn
pwIndexMappingPeerAddrType=_PwIndexMappingPeerAddrType_Object((1,3,6,1,4,1,164,20,10,1,7,1,3),_PwIndexMappingPeerAddrType_Type())
pwIndexMappingPeerAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:pwIndexMappingPeerAddrType.setStatus(_B)
_PwIndexMappingPeerAddr_Type=InetAddress
_PwIndexMappingPeerAddr_Object=MibTableColumn
pwIndexMappingPeerAddr=_PwIndexMappingPeerAddr_Object((1,3,6,1,4,1,164,20,10,1,7,1,4),_PwIndexMappingPeerAddr_Type())
pwIndexMappingPeerAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:pwIndexMappingPeerAddr.setStatus(_B)
_PwIndexMappingPwIndex_Type=PwIndexType
_PwIndexMappingPwIndex_Object=MibTableColumn
pwIndexMappingPwIndex=_PwIndexMappingPwIndex_Object((1,3,6,1,4,1,164,20,10,1,7,1,5),_PwIndexMappingPwIndex_Type())
pwIndexMappingPwIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pwIndexMappingPwIndex.setStatus(_B)
_PwPeerMappingTable_Object=MibTable
pwPeerMappingTable=_PwPeerMappingTable_Object((1,3,6,1,4,1,164,20,10,1,8))
if mibBuilder.loadTexts:pwPeerMappingTable.setStatus(_B)
_PwPeerMappingEntry_Object=MibTableRow
pwPeerMappingEntry=_PwPeerMappingEntry_Object((1,3,6,1,4,1,164,20,10,1,8,1))
pwPeerMappingEntry.setIndexNames((0,_A,_s),(0,_A,_t),(0,_A,_u),(0,_A,_v))
if mibBuilder.loadTexts:pwPeerMappingEntry.setStatus(_B)
_PwPeerMappingPeerAddrType_Type=InetAddressType
_PwPeerMappingPeerAddrType_Object=MibTableColumn
pwPeerMappingPeerAddrType=_PwPeerMappingPeerAddrType_Object((1,3,6,1,4,1,164,20,10,1,8,1,1),_PwPeerMappingPeerAddrType_Type())
pwPeerMappingPeerAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:pwPeerMappingPeerAddrType.setStatus(_B)
_PwPeerMappingPeerAddr_Type=InetAddress
_PwPeerMappingPeerAddr_Object=MibTableColumn
pwPeerMappingPeerAddr=_PwPeerMappingPeerAddr_Object((1,3,6,1,4,1,164,20,10,1,8,1,2),_PwPeerMappingPeerAddr_Type())
pwPeerMappingPeerAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:pwPeerMappingPeerAddr.setStatus(_B)
_PwPeerMappingPwType_Type=IANAPwTypeTC
_PwPeerMappingPwType_Object=MibTableColumn
pwPeerMappingPwType=_PwPeerMappingPwType_Object((1,3,6,1,4,1,164,20,10,1,8,1,3),_PwPeerMappingPwType_Type())
pwPeerMappingPwType.setMaxAccess(_E)
if mibBuilder.loadTexts:pwPeerMappingPwType.setStatus(_B)
_PwPeerMappingPwID_Type=PwIDType
_PwPeerMappingPwID_Object=MibTableColumn
pwPeerMappingPwID=_PwPeerMappingPwID_Object((1,3,6,1,4,1,164,20,10,1,8,1,4),_PwPeerMappingPwID_Type())
pwPeerMappingPwID.setMaxAccess(_E)
if mibBuilder.loadTexts:pwPeerMappingPwID.setStatus(_B)
_PwPeerMappingPwIndex_Type=PwIndexType
_PwPeerMappingPwIndex_Object=MibTableColumn
pwPeerMappingPwIndex=_PwPeerMappingPwIndex_Object((1,3,6,1,4,1,164,20,10,1,8,1,5),_PwPeerMappingPwIndex_Type())
pwPeerMappingPwIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPeerMappingPwIndex.setStatus(_B)
class _PwUpDownNotifEnable_Type(TruthValue):defaultValue=2
_PwUpDownNotifEnable_Type.__name__=_G
_PwUpDownNotifEnable_Object=MibScalar
pwUpDownNotifEnable=_PwUpDownNotifEnable_Object((1,3,6,1,4,1,164,20,10,1,9),_PwUpDownNotifEnable_Type())
pwUpDownNotifEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:pwUpDownNotifEnable.setStatus(_B)
class _PwDeletedNotifEnable_Type(TruthValue):defaultValue=2
_PwDeletedNotifEnable_Type.__name__=_G
_PwDeletedNotifEnable_Object=MibScalar
pwDeletedNotifEnable=_PwDeletedNotifEnable_Object((1,3,6,1,4,1,164,20,10,1,10),_PwDeletedNotifEnable_Type())
pwDeletedNotifEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:pwDeletedNotifEnable.setStatus(_B)
_PwNotifRate_Type=Unsigned32
_PwNotifRate_Object=MibScalar
pwNotifRate=_PwNotifRate_Object((1,3,6,1,4,1,164,20,10,1,11),_PwNotifRate_Type())
pwNotifRate.setMaxAccess(_K)
if mibBuilder.loadTexts:pwNotifRate.setStatus(_B)
_PwConformance_ObjectIdentity=ObjectIdentity
pwConformance=_PwConformance_ObjectIdentity((1,3,6,1,4,1,164,20,10,2))
_PwGroups_ObjectIdentity=ObjectIdentity
pwGroups=_PwGroups_ObjectIdentity((1,3,6,1,4,1,164,20,10,2,1))
_PwCompliances_ObjectIdentity=ObjectIdentity
pwCompliances=_PwCompliances_ObjectIdentity((1,3,6,1,4,1,164,20,10,2,2))
pwBasicGroup=ObjectGroup((1,3,6,1,4,1,164,20,10,2,1,1))
pwBasicGroup.setObjects(*((_A,_L),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,'pwName'),(_A,'pwDescr'),(_A,_A3),(_A,'pwUpTime'),(_A,_A4),(_A,_A5),(_A,_H),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:pwBasicGroup.setStatus(_B)
pwPwIdGroup=ObjectGroup((1,3,6,1,4,1,164,20,10,2,1,2))
pwPwIdGroup.setObjects((_A,_M))
if mibBuilder.loadTexts:pwPwIdGroup.setStatus(_B)
pwGeneralizedFecGroup=ObjectGroup((1,3,6,1,4,1,164,20,10,2,1,3))
pwGeneralizedFecGroup.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:pwGeneralizedFecGroup.setStatus(_B)
pwFcsGroup=ObjectGroup((1,3,6,1,4,1,164,20,10,2,1,4))
pwFcsGroup.setObjects(*((_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:pwFcsGroup.setStatus(_B)
pwFragGroup=ObjectGroup((1,3,6,1,4,1,164,20,10,2,1,5))
pwFragGroup.setObjects(*((_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:pwFragGroup.setStatus(_B)
pwPwStatusGroup=ObjectGroup((1,3,6,1,4,1,164,20,10,2,1,6))
pwPwStatusGroup.setObjects(*((_A,_AH),(_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:pwPwStatusGroup.setStatus(_B)
pwGetNextGroup=ObjectGroup((1,3,6,1,4,1,164,20,10,2,1,7))
pwGetNextGroup.setObjects((_A,_AK))
if mibBuilder.loadTexts:pwGetNextGroup.setStatus(_B)
pwPriorityGroup=ObjectGroup((1,3,6,1,4,1,164,20,10,2,1,8))
pwPriorityGroup.setObjects(*((_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:pwPriorityGroup.setStatus(_B)
pwAttachmentGroup=ObjectGroup((1,3,6,1,4,1,164,20,10,2,1,9))
pwAttachmentGroup.setObjects((_A,_AN))
if mibBuilder.loadTexts:pwAttachmentGroup.setStatus(_B)
pwPerformanceGeneralGroup=ObjectGroup((1,3,6,1,4,1,164,20,10,2,1,10))
pwPerformanceGeneralGroup.setObjects((_A,_AO))
if mibBuilder.loadTexts:pwPerformanceGeneralGroup.setStatus(_B)
pwPeformance1DayIntervalGroup=ObjectGroup((1,3,6,1,4,1,164,20,10,2,1,11))
pwPeformance1DayIntervalGroup.setObjects(*((_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU)))
if mibBuilder.loadTexts:pwPeformance1DayIntervalGroup.setStatus(_B)
pwPerformanceIntervalGeneralGroup=ObjectGroup((1,3,6,1,4,1,164,20,10,2,1,12))
pwPerformanceIntervalGeneralGroup.setObjects(*((_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:pwPerformanceIntervalGeneralGroup.setStatus(_B)
pwPeformanceIntervalGroup=ObjectGroup((1,3,6,1,4,1,164,20,10,2,1,13))
pwPeformanceIntervalGroup.setObjects(*((_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag)))
if mibBuilder.loadTexts:pwPeformanceIntervalGroup.setStatus(_B)
pwHCPeformanceIntervalGroup=ObjectGroup((1,3,6,1,4,1,164,20,10,2,1,14))
pwHCPeformanceIntervalGroup.setObjects(*((_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao)))
if mibBuilder.loadTexts:pwHCPeformanceIntervalGroup.setStatus(_B)
pwMappingTablesGroup=ObjectGroup((1,3,6,1,4,1,164,20,10,2,1,15))
pwMappingTablesGroup.setObjects(*((_A,_Ap),(_A,_Aq)))
if mibBuilder.loadTexts:pwMappingTablesGroup.setStatus(_B)
pwNotificationControlGroup=ObjectGroup((1,3,6,1,4,1,164,20,10,2,1,16))
pwNotificationControlGroup.setObjects(*((_A,_Ar),(_A,_As),(_A,_At)))
if mibBuilder.loadTexts:pwNotificationControlGroup.setStatus(_B)
pwSignalingGroup=ObjectGroup((1,3,6,1,4,1,164,20,10,2,1,18))
pwSignalingGroup.setObjects(*((_A,_N),(_A,_O),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_)))
if mibBuilder.loadTexts:pwSignalingGroup.setStatus(_B)
pwDown=NotificationType((1,3,6,1,4,1,164,20,10,0,1))
pwDown.setObjects(*((_A,_H),(_A,_H)))
if mibBuilder.loadTexts:pwDown.setStatus(_B)
pwUp=NotificationType((1,3,6,1,4,1,164,20,10,0,2))
pwUp.setObjects(*((_A,_H),(_A,_H)))
if mibBuilder.loadTexts:pwUp.setStatus(_B)
pwDeleted=NotificationType((1,3,6,1,4,1,164,20,10,0,3))
pwDeleted.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:pwDeleted.setStatus(_B)
pwNotificationGroup=NotificationGroup((1,3,6,1,4,1,164,20,10,2,1,17))
pwNotificationGroup.setObjects(*((_A,'pwUp'),(_A,'pwDown'),(_A,_B0)))
if mibBuilder.loadTexts:pwNotificationGroup.setStatus(_B)
pwModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,164,20,10,2,2,1))
pwModuleFullCompliance.setObjects(*((_A,_P),(_A,_B1),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:pwModuleFullCompliance.setStatus(_B)
pwModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,164,20,10,2,2,2))
pwModuleReadOnlyCompliance.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:pwModuleReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'radExperimental':radExperimental,'pwStdMIBR':pwStdMIBR,'pwNotifications':pwNotifications,'pwDown':pwDown,'pwUp':pwUp,_B0:pwDeleted,'pwObjects':pwObjects,_AK:pwIndexNext,'pwTable':pwTable,'pwEntry':pwEntry,_I:pwIndex,_L:pwType,_w:pwOwner,_x:pwPsnType,_AL:pwSetUpPriority,_AM:pwHoldingPriority,_N:pwPeerAddrType,_O:pwPeerAddr,_AN:pwAttachedPwIndex,_y:pwIfIndex,_M:pwID,_Au:pwLocalGroupID,_AA:pwGroupAttachmentID,_AB:pwLocalAttachmentID,_AC:pwPeerAttachmentID,_z:pwCwPreference,_A0:pwLocalIfMtu,_Av:pwLocalIfString,_Aw:pwLocalCapabAdvert,_Ax:pwRemoteGroupID,_Ay:pwCwStatus,_Az:pwRemoteIfMtu,_A_:pwRemoteIfString,_AH:pwRemoteCapabilities,_AF:pwFragmentCfgSize,_AG:pwRmtFragCapability,_AD:pwFcsRetentionCfg,_AE:pwFcsRetentionStatus,_A1:pwOutboundLabel,_A2:pwInboundLabel,'pwName':pwName,'pwDescr':pwDescr,_A3:pwCreateTime,'pwUpTime':pwUpTime,_A4:pwLastChange,_A5:pwAdminStatus,_H:pwOperStatus,_A6:pwLocalStatus,_AI:pwRemoteStatusCapable,_AJ:pwRemoteStatus,_AV:pwTimeElapsed,_AW:pwValidIntervals,_A7:pwRowStatus,_A8:pwStorageType,_A9:pwOamEnable,'pwPerfCurrentTable':pwPerfCurrentTable,'pwPerfCurrentEntry':pwPerfCurrentEntry,_Ah:pwPerfCurrentInHCPackets,_Ai:pwPerfCurrentInHCBytes,_Aj:pwPerfCurrentOutHCPackets,_Ak:pwPerfCurrentOutHCBytes,_AZ:pwPerfCurrentInPackets,_Aa:pwPerfCurrentInBytes,_Ab:pwPerfCurrentOutPackets,_Ac:pwPerfCurrentOutBytes,'pwPerfIntervalTable':pwPerfIntervalTable,'pwPerfIntervalEntry':pwPerfIntervalEntry,_m:pwPerfIntervalNumber,_AX:pwPerfIntervalValidData,_AY:pwPerfIntervalTimeElapsed,_Al:pwPerfIntervalInHCPackets,_Am:pwPerfIntervalInHCBytes,_An:pwPerfIntervalOutHCPackets,_Ao:pwPerfIntervalOutHCBytes,_Ad:pwPerfIntervalInPackets,_Ae:pwPerfIntervalInBytes,_Af:pwPerfIntervalOutPackets,_Ag:pwPerfIntervalOutBytes,'pwPerf1DayIntervalTable':pwPerf1DayIntervalTable,'pwPerf1DayIntervalEntry':pwPerf1DayIntervalEntry,_n:pwPerf1DayIntervalNumber,_AP:pwPerf1DayIntervalValidData,_AQ:pwPerf1DayIntervalTimeElapsed,_AR:pwPerf1DayIntervalInHCPackets,_AS:pwPerf1DayIntervalInHCBytes,_AT:pwPerf1DayIntervalOutHCPackets,_AU:pwPerf1DayIntervalOutHCBytes,_AO:pwPerfTotalErrorPackets,'pwIndexMappingTable':pwIndexMappingTable,'pwIndexMappingEntry':pwIndexMappingEntry,_o:pwIndexMappingPwType,_p:pwIndexMappingPwID,_q:pwIndexMappingPeerAddrType,_r:pwIndexMappingPeerAddr,_Ap:pwIndexMappingPwIndex,'pwPeerMappingTable':pwPeerMappingTable,'pwPeerMappingEntry':pwPeerMappingEntry,_s:pwPeerMappingPeerAddrType,_t:pwPeerMappingPeerAddr,_u:pwPeerMappingPwType,_v:pwPeerMappingPwID,_Aq:pwPeerMappingPwIndex,_Ar:pwUpDownNotifEnable,_As:pwDeletedNotifEnable,_At:pwNotifRate,'pwConformance':pwConformance,'pwGroups':pwGroups,_P:pwBasicGroup,_R:pwPwIdGroup,_S:pwGeneralizedFecGroup,_T:pwFcsGroup,_U:pwFragGroup,_V:pwPwStatusGroup,_W:pwGetNextGroup,_X:pwPriorityGroup,_Y:pwAttachmentGroup,_B1:pwPerformanceGeneralGroup,_Z:pwPeformance1DayIntervalGroup,_a:pwPerformanceIntervalGeneralGroup,_b:pwPeformanceIntervalGroup,_c:pwHCPeformanceIntervalGroup,_d:pwMappingTablesGroup,_f:pwNotificationControlGroup,_Q:pwNotificationGroup,_e:pwSignalingGroup,'pwCompliances':pwCompliances,'pwModuleFullCompliance':pwModuleFullCompliance,'pwModuleReadOnlyCompliance':pwModuleReadOnlyCompliance})