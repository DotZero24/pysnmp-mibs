_B9='ciscoTelePresenceExchangeSystemMIBStatsGroup'
_B8='ciscoTelepresenceExchangeSystemMIBErrorHistoryGroup'
_B7='ciscoTelepresenceExchangeSystemMIBNotifyGroup'
_B6='ciscoTelepresenceExchangeSystemMIBNotfyObjectsGroup'
_B5='ciscoTelepresenceExchangeSystemMIBConfigGroup'
_B4='ciscoTelepresenceExchangeSystemMIBStatusGroup'
_B3='ciscoCTXSysResourceUp'
_B2='ciscoCTXSysClusterNodeUp'
_B1='ciscoCTXSysResourceAllocFailure'
_B0='ciscoCTXSysCallAbnormalDisconnect'
_A_='ciscoCTXSysErrorHistoryEvent'
_Az='ciscoCTXSysCallSetupFailure'
_Ay='ciscoCTXSysResourceDown'
_Ax='ciscoCTXSysClusterNodeDown'
_Aw='ciscoCTXSysUserAuthFailure'
_Av='ciscoCTXSysLicenseFailure'
_Au='ciscoCTXSysSystemBackupStatusChg'
_At='ciscoCTXSysSystemConfigStatusChg'
_As='ciscoCTXSysResourceStatusChg'
_Ar='ciscoCTXSysCallEnginesStatusChg'
_Aq='ciscoCTXSysDatabaseServersStatusChg'
_Ap='ciscoCTXSysAdminServersStatusChg'
_Ao='ctxErrorTimeStamp'
_An='ctxErrorHistoryLastIndex'
_Am='ctxErrorHistoryMaxSeverity'
_Al='ctxErrorHistoryTableSize'
_Ak='ctxErrorHistoryEventNotifyEnable'
_Aj='ctxCallFailureNotifyEnable'
_Ai='ctxResourceAlarmNotifyEnable'
_Ah='ctxClusterNodeAlarmNotifyEnable'
_Ag='ctxAuthFailureNotifyEnable'
_Af='ctxLicenseAlarmNotifyEnable'
_Ae='ctxStatusChangeNotifyEnable'
_Ad='ctxPeakHistAllocPoolPorts'
_Ac='ctxPeakHistAllocPoolTS'
_Ab='ctxPeakHistAllocPorts'
_Aa='ctxPeakHistAllocTS'
_AZ='ctxPeakHistIntTime'
_AY='ctxPeakHistMaxIntervals'
_AX='ctxResourceUnavailDuration'
_AW='ctxResourceOperState'
_AV='ctxAllocPoolAllocOutOfPorts'
_AU='ctxAllocOutOfPorts'
_AT='ctxRegionCallSetupFailures'
_AS='ctxResourceCallSetupFailures'
_AR='ctxAllocPoolAllocFailures'
_AQ='ctxAllocFailures'
_AP='ctxAllocPoolAvailPorts'
_AO='ctxAllocPoolActivePorts'
_AN='ctxAllocAvailPorts'
_AM='ctxAllocActivePorts'
_AL='ctxResourceUnavailTrans'
_AK='ctxMeetingConfigInterOpMaxId'
_AJ='ctxMeetingConfigInterOpMinId'
_AI='ctxMeetingConfigStaticMaxId'
_AH='ctxMeetingConfigStaticMinId'
_AG='ctxClusterNodeKey'
_AF='ctxClusterNodeOperState'
_AE='ctxResourceRegionKeyRef1'
_AD='ctxResourceKey'
_AC='ctxOrganizationServiceProviderKeyRef1'
_AB='ctxOrganizationKey'
_AA='ctxRegionServiceProviderKeyRef1'
_A9='ctxServiceProviderKey'
_A8='ctxClusterNodeClusterName'
_A7='ctxClusterNodeIPAddr'
_A6='ctxClusterNodeIPType'
_A5='ctxClusterNodeHostName'
_A4='ctxMediaCapacityLargeMeeting'
_A3='ctxMediaCapacityMaxPorts'
_A2='ctxSipTransportProto'
_A1='ctxSipPort'
_A0='ctxSipIpAddr'
_z='ctxSipIpType'
_y='ctxResourceMgmtIPAddr'
_x='ctxResourceMgmtIPType'
_w='ctxResourceDescr'
_v='ctxOrganizationDirectDial'
_u='ctxOrganizationMaxPorts'
_t='ctxOrganizationDescr'
_s='ctxOrganizationName'
_r='ctxRegionDescr'
_q='ctxServiceProviderHDNumber'
_p='ctxServiceProviderDescr'
_o='ctxServiceProviderName'
_n='ctxErrorIndex'
_m='ctxPeakHistAllocPoolIntIndex'
_l='ctxPeakHistAllocIntIndex'
_k='ctxClusterNodeIndex'
_j='ctxOrganizationIndex'
_i='ctxServiceProviderIndex'
_h='SyslogSeverity'
_g='ctxErrorAttrValStr'
_f='ctxErrorAlarmId'
_e='ctxErrorAppName'
_d='ctxErrorMessage'
_c='ctxErrorSeverity'
_b='ctxErrorKey'
_a='ctxRegionKey'
_Z='ctxSystemBackupStatus'
_Y='ctxSystemConfigStatus'
_X='ctxResourceStatus'
_W='ctxDatabaseServersStatus'
_V='ctxCallEnginesStatus'
_U='ctxAdminServersStatus'
_T='failures'
_S='Integer32'
_R='ctxClusterNodeType'
_Q='ctxClusterNodeName'
_P='ctxRegionName'
_O='occurrences'
_N='ctxRegionIndex'
_M='Unsigned32'
_L='OctetString'
_K='ctxResourceDeviceType'
_J='ctxResourceName'
_I='ctxResourceIndex'
_H='not-accessible'
_G='TruthValue'
_F='read-write'
_E='DisplayString'
_D='ctxNotifyMessage'
_C='read-only'
_B='current'
_A='CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SyslogSeverity,=mibBuilder.importSymbols('CISCO-SYSLOG-MIB',_h)
CiscoPort,=mibBuilder.importSymbols('CISCO-TC','CiscoPort')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_S,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention','TimeStamp',_G)
ciscoTelepresenceExchangeSystemMIB=ModuleIdentity((1,3,6,1,4,1,9,9,758))
if mibBuilder.loadTexts:ciscoTelepresenceExchangeSystemMIB.setRevisions(('2011-01-13 00:00',))
class CtxKeyId(TextualConvention,OctetString):status=_B;displayHint='4x-';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class CtxIndex(TextualConvention,Unsigned32):status=_B;displayHint='d'
class CtxPorts(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class CtxClusterNodeTypes(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('admin',1),('engine',2),('db',3)))
class CtxHealthStates(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('warning',2),('error',3)))
class CtxResourceOperState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('operational',1),('disabled',2),('failed',3),('maintenance',4),('pending',5),('standby',6),('unreachable',7)))
class CtxSIPProtocolType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tcp',1),('udp',2),('tls',3)))
class CtxResourceType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('ctms',1),('ivr',2),('sbc',3),('sip',4),('ctsmanager',5),('mseTps',6),('mseMedia2',7),('isdn',8),('cuvcm',9),('cucm',10),('vcs',11),('tms',12)))
_CiscoTelepresenceExchangeSystemMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoTelepresenceExchangeSystemMIBNotifs=_CiscoTelepresenceExchangeSystemMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,758,0))
_CiscoTelepresenceExchangeSystemMIBObjects_ObjectIdentity=ObjectIdentity
ciscoTelepresenceExchangeSystemMIBObjects=_CiscoTelepresenceExchangeSystemMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,758,1))
_CtxConfigObjects_ObjectIdentity=ObjectIdentity
ctxConfigObjects=_CtxConfigObjects_ObjectIdentity((1,3,6,1,4,1,9,9,758,1,1))
_CtxServiceProviderTable_Object=MibTable
ctxServiceProviderTable=_CtxServiceProviderTable_Object((1,3,6,1,4,1,9,9,758,1,1,1))
if mibBuilder.loadTexts:ctxServiceProviderTable.setStatus(_B)
_CtxServiceProviderEntry_Object=MibTableRow
ctxServiceProviderEntry=_CtxServiceProviderEntry_Object((1,3,6,1,4,1,9,9,758,1,1,1,1))
ctxServiceProviderEntry.setIndexNames((0,_A,_i))
if mibBuilder.loadTexts:ctxServiceProviderEntry.setStatus(_B)
_CtxServiceProviderIndex_Type=CtxIndex
_CtxServiceProviderIndex_Object=MibTableColumn
ctxServiceProviderIndex=_CtxServiceProviderIndex_Object((1,3,6,1,4,1,9,9,758,1,1,1,1,1),_CtxServiceProviderIndex_Type())
ctxServiceProviderIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ctxServiceProviderIndex.setStatus(_B)
_CtxServiceProviderKey_Type=CtxKeyId
_CtxServiceProviderKey_Object=MibTableColumn
ctxServiceProviderKey=_CtxServiceProviderKey_Object((1,3,6,1,4,1,9,9,758,1,1,1,1,2),_CtxServiceProviderKey_Type())
ctxServiceProviderKey.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxServiceProviderKey.setStatus(_B)
class _CtxServiceProviderName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CtxServiceProviderName_Type.__name__=_E
_CtxServiceProviderName_Object=MibTableColumn
ctxServiceProviderName=_CtxServiceProviderName_Object((1,3,6,1,4,1,9,9,758,1,1,1,1,3),_CtxServiceProviderName_Type())
ctxServiceProviderName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxServiceProviderName.setStatus(_B)
class _CtxServiceProviderDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CtxServiceProviderDescr_Type.__name__=_L
_CtxServiceProviderDescr_Object=MibTableColumn
ctxServiceProviderDescr=_CtxServiceProviderDescr_Object((1,3,6,1,4,1,9,9,758,1,1,1,1,4),_CtxServiceProviderDescr_Type())
ctxServiceProviderDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxServiceProviderDescr.setStatus(_B)
_CtxServiceProviderHDNumber_Type=DisplayString
_CtxServiceProviderHDNumber_Object=MibTableColumn
ctxServiceProviderHDNumber=_CtxServiceProviderHDNumber_Object((1,3,6,1,4,1,9,9,758,1,1,1,1,5),_CtxServiceProviderHDNumber_Type())
ctxServiceProviderHDNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxServiceProviderHDNumber.setStatus(_B)
_CtxRegionTable_Object=MibTable
ctxRegionTable=_CtxRegionTable_Object((1,3,6,1,4,1,9,9,758,1,1,2))
if mibBuilder.loadTexts:ctxRegionTable.setStatus(_B)
_CtxRegionEntry_Object=MibTableRow
ctxRegionEntry=_CtxRegionEntry_Object((1,3,6,1,4,1,9,9,758,1,1,2,1))
ctxRegionEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:ctxRegionEntry.setStatus(_B)
_CtxRegionIndex_Type=CtxIndex
_CtxRegionIndex_Object=MibTableColumn
ctxRegionIndex=_CtxRegionIndex_Object((1,3,6,1,4,1,9,9,758,1,1,2,1,1),_CtxRegionIndex_Type())
ctxRegionIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ctxRegionIndex.setStatus(_B)
_CtxRegionKey_Type=CtxKeyId
_CtxRegionKey_Object=MibTableColumn
ctxRegionKey=_CtxRegionKey_Object((1,3,6,1,4,1,9,9,758,1,1,2,1,2),_CtxRegionKey_Type())
ctxRegionKey.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxRegionKey.setStatus(_B)
class _CtxRegionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CtxRegionName_Type.__name__=_E
_CtxRegionName_Object=MibTableColumn
ctxRegionName=_CtxRegionName_Object((1,3,6,1,4,1,9,9,758,1,1,2,1,3),_CtxRegionName_Type())
ctxRegionName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxRegionName.setStatus(_B)
class _CtxRegionDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CtxRegionDescr_Type.__name__=_L
_CtxRegionDescr_Object=MibTableColumn
ctxRegionDescr=_CtxRegionDescr_Object((1,3,6,1,4,1,9,9,758,1,1,2,1,4),_CtxRegionDescr_Type())
ctxRegionDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxRegionDescr.setStatus(_B)
_CtxRegionServiceProviderKeyRef1_Type=CtxKeyId
_CtxRegionServiceProviderKeyRef1_Object=MibTableColumn
ctxRegionServiceProviderKeyRef1=_CtxRegionServiceProviderKeyRef1_Object((1,3,6,1,4,1,9,9,758,1,1,2,1,5),_CtxRegionServiceProviderKeyRef1_Type())
ctxRegionServiceProviderKeyRef1.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxRegionServiceProviderKeyRef1.setStatus(_B)
_CtxOrganizationTable_Object=MibTable
ctxOrganizationTable=_CtxOrganizationTable_Object((1,3,6,1,4,1,9,9,758,1,1,3))
if mibBuilder.loadTexts:ctxOrganizationTable.setStatus(_B)
_CtxOrganizationEntry_Object=MibTableRow
ctxOrganizationEntry=_CtxOrganizationEntry_Object((1,3,6,1,4,1,9,9,758,1,1,3,1))
ctxOrganizationEntry.setIndexNames((0,_A,_j))
if mibBuilder.loadTexts:ctxOrganizationEntry.setStatus(_B)
_CtxOrganizationIndex_Type=CtxIndex
_CtxOrganizationIndex_Object=MibTableColumn
ctxOrganizationIndex=_CtxOrganizationIndex_Object((1,3,6,1,4,1,9,9,758,1,1,3,1,1),_CtxOrganizationIndex_Type())
ctxOrganizationIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ctxOrganizationIndex.setStatus(_B)
_CtxOrganizationKey_Type=CtxKeyId
_CtxOrganizationKey_Object=MibTableColumn
ctxOrganizationKey=_CtxOrganizationKey_Object((1,3,6,1,4,1,9,9,758,1,1,3,1,2),_CtxOrganizationKey_Type())
ctxOrganizationKey.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxOrganizationKey.setStatus(_B)
class _CtxOrganizationName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CtxOrganizationName_Type.__name__=_E
_CtxOrganizationName_Object=MibTableColumn
ctxOrganizationName=_CtxOrganizationName_Object((1,3,6,1,4,1,9,9,758,1,1,3,1,3),_CtxOrganizationName_Type())
ctxOrganizationName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxOrganizationName.setStatus(_B)
class _CtxOrganizationDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CtxOrganizationDescr_Type.__name__=_L
_CtxOrganizationDescr_Object=MibTableColumn
ctxOrganizationDescr=_CtxOrganizationDescr_Object((1,3,6,1,4,1,9,9,758,1,1,3,1,4),_CtxOrganizationDescr_Type())
ctxOrganizationDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxOrganizationDescr.setStatus(_B)
_CtxOrganizationMaxPorts_Type=CtxPorts
_CtxOrganizationMaxPorts_Object=MibTableColumn
ctxOrganizationMaxPorts=_CtxOrganizationMaxPorts_Object((1,3,6,1,4,1,9,9,758,1,1,3,1,5),_CtxOrganizationMaxPorts_Type())
ctxOrganizationMaxPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxOrganizationMaxPorts.setStatus(_B)
_CtxOrganizationDirectDial_Type=TruthValue
_CtxOrganizationDirectDial_Object=MibTableColumn
ctxOrganizationDirectDial=_CtxOrganizationDirectDial_Object((1,3,6,1,4,1,9,9,758,1,1,3,1,6),_CtxOrganizationDirectDial_Type())
ctxOrganizationDirectDial.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxOrganizationDirectDial.setStatus(_B)
_CtxOrganizationServiceProviderKeyRef1_Type=CtxKeyId
_CtxOrganizationServiceProviderKeyRef1_Object=MibTableColumn
ctxOrganizationServiceProviderKeyRef1=_CtxOrganizationServiceProviderKeyRef1_Object((1,3,6,1,4,1,9,9,758,1,1,3,1,7),_CtxOrganizationServiceProviderKeyRef1_Type())
ctxOrganizationServiceProviderKeyRef1.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxOrganizationServiceProviderKeyRef1.setStatus(_B)
_CtxResourceObjects_ObjectIdentity=ObjectIdentity
ctxResourceObjects=_CtxResourceObjects_ObjectIdentity((1,3,6,1,4,1,9,9,758,1,1,4))
_CtxResourceTable_Object=MibTable
ctxResourceTable=_CtxResourceTable_Object((1,3,6,1,4,1,9,9,758,1,1,4,1))
if mibBuilder.loadTexts:ctxResourceTable.setStatus(_B)
_CtxResourceEntry_Object=MibTableRow
ctxResourceEntry=_CtxResourceEntry_Object((1,3,6,1,4,1,9,9,758,1,1,4,1,1))
ctxResourceEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:ctxResourceEntry.setStatus(_B)
_CtxResourceIndex_Type=CtxIndex
_CtxResourceIndex_Object=MibTableColumn
ctxResourceIndex=_CtxResourceIndex_Object((1,3,6,1,4,1,9,9,758,1,1,4,1,1,1),_CtxResourceIndex_Type())
ctxResourceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ctxResourceIndex.setStatus(_B)
_CtxResourceKey_Type=CtxKeyId
_CtxResourceKey_Object=MibTableColumn
ctxResourceKey=_CtxResourceKey_Object((1,3,6,1,4,1,9,9,758,1,1,4,1,1,2),_CtxResourceKey_Type())
ctxResourceKey.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxResourceKey.setStatus(_B)
class _CtxResourceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CtxResourceName_Type.__name__=_E
_CtxResourceName_Object=MibTableColumn
ctxResourceName=_CtxResourceName_Object((1,3,6,1,4,1,9,9,758,1,1,4,1,1,3),_CtxResourceName_Type())
ctxResourceName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxResourceName.setStatus(_B)
class _CtxResourceDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CtxResourceDescr_Type.__name__=_L
_CtxResourceDescr_Object=MibTableColumn
ctxResourceDescr=_CtxResourceDescr_Object((1,3,6,1,4,1,9,9,758,1,1,4,1,1,4),_CtxResourceDescr_Type())
ctxResourceDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxResourceDescr.setStatus(_B)
_CtxResourceMgmtIPType_Type=InetAddressType
_CtxResourceMgmtIPType_Object=MibTableColumn
ctxResourceMgmtIPType=_CtxResourceMgmtIPType_Object((1,3,6,1,4,1,9,9,758,1,1,4,1,1,5),_CtxResourceMgmtIPType_Type())
ctxResourceMgmtIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxResourceMgmtIPType.setStatus(_B)
_CtxResourceMgmtIPAddr_Type=InetAddress
_CtxResourceMgmtIPAddr_Object=MibTableColumn
ctxResourceMgmtIPAddr=_CtxResourceMgmtIPAddr_Object((1,3,6,1,4,1,9,9,758,1,1,4,1,1,6),_CtxResourceMgmtIPAddr_Type())
ctxResourceMgmtIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxResourceMgmtIPAddr.setStatus(_B)
_CtxResourceDeviceType_Type=CtxResourceType
_CtxResourceDeviceType_Object=MibTableColumn
ctxResourceDeviceType=_CtxResourceDeviceType_Object((1,3,6,1,4,1,9,9,758,1,1,4,1,1,7),_CtxResourceDeviceType_Type())
ctxResourceDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxResourceDeviceType.setStatus(_B)
_CtxResourceRegionKeyRef1_Type=CtxKeyId
_CtxResourceRegionKeyRef1_Object=MibTableColumn
ctxResourceRegionKeyRef1=_CtxResourceRegionKeyRef1_Object((1,3,6,1,4,1,9,9,758,1,1,4,1,1,8),_CtxResourceRegionKeyRef1_Type())
ctxResourceRegionKeyRef1.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxResourceRegionKeyRef1.setStatus(_B)
_CtxSipConfigTable_Object=MibTable
ctxSipConfigTable=_CtxSipConfigTable_Object((1,3,6,1,4,1,9,9,758,1,1,4,2))
if mibBuilder.loadTexts:ctxSipConfigTable.setStatus(_B)
_CtxSipConfigEntry_Object=MibTableRow
ctxSipConfigEntry=_CtxSipConfigEntry_Object((1,3,6,1,4,1,9,9,758,1,1,4,2,1))
ctxSipConfigEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:ctxSipConfigEntry.setStatus(_B)
_CtxSipIpType_Type=InetAddressType
_CtxSipIpType_Object=MibTableColumn
ctxSipIpType=_CtxSipIpType_Object((1,3,6,1,4,1,9,9,758,1,1,4,2,1,1),_CtxSipIpType_Type())
ctxSipIpType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxSipIpType.setStatus(_B)
_CtxSipIpAddr_Type=InetAddress
_CtxSipIpAddr_Object=MibTableColumn
ctxSipIpAddr=_CtxSipIpAddr_Object((1,3,6,1,4,1,9,9,758,1,1,4,2,1,2),_CtxSipIpAddr_Type())
ctxSipIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxSipIpAddr.setStatus(_B)
_CtxSipPort_Type=CiscoPort
_CtxSipPort_Object=MibTableColumn
ctxSipPort=_CtxSipPort_Object((1,3,6,1,4,1,9,9,758,1,1,4,2,1,3),_CtxSipPort_Type())
ctxSipPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxSipPort.setStatus(_B)
_CtxSipTransportProto_Type=CtxSIPProtocolType
_CtxSipTransportProto_Object=MibTableColumn
ctxSipTransportProto=_CtxSipTransportProto_Object((1,3,6,1,4,1,9,9,758,1,1,4,2,1,4),_CtxSipTransportProto_Type())
ctxSipTransportProto.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxSipTransportProto.setStatus(_B)
_CtxMediaCapacityConfigTable_Object=MibTable
ctxMediaCapacityConfigTable=_CtxMediaCapacityConfigTable_Object((1,3,6,1,4,1,9,9,758,1,1,4,3))
if mibBuilder.loadTexts:ctxMediaCapacityConfigTable.setStatus(_B)
_CtxMediaCapacityConfigEntry_Object=MibTableRow
ctxMediaCapacityConfigEntry=_CtxMediaCapacityConfigEntry_Object((1,3,6,1,4,1,9,9,758,1,1,4,3,1))
ctxMediaCapacityConfigEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:ctxMediaCapacityConfigEntry.setStatus(_B)
_CtxMediaCapacityMaxPorts_Type=CtxPorts
_CtxMediaCapacityMaxPorts_Object=MibTableColumn
ctxMediaCapacityMaxPorts=_CtxMediaCapacityMaxPorts_Object((1,3,6,1,4,1,9,9,758,1,1,4,3,1,1),_CtxMediaCapacityMaxPorts_Type())
ctxMediaCapacityMaxPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxMediaCapacityMaxPorts.setStatus(_B)
_CtxMediaCapacityLargeMeeting_Type=TruthValue
_CtxMediaCapacityLargeMeeting_Object=MibTableColumn
ctxMediaCapacityLargeMeeting=_CtxMediaCapacityLargeMeeting_Object((1,3,6,1,4,1,9,9,758,1,1,4,3,1,2),_CtxMediaCapacityLargeMeeting_Type())
ctxMediaCapacityLargeMeeting.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxMediaCapacityLargeMeeting.setStatus(_B)
_CtxMeetingConfigTable_Object=MibTable
ctxMeetingConfigTable=_CtxMeetingConfigTable_Object((1,3,6,1,4,1,9,9,758,1,1,4,4))
if mibBuilder.loadTexts:ctxMeetingConfigTable.setStatus(_B)
_CtxMeetingConfigEntry_Object=MibTableRow
ctxMeetingConfigEntry=_CtxMeetingConfigEntry_Object((1,3,6,1,4,1,9,9,758,1,1,4,4,1))
ctxMeetingConfigEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:ctxMeetingConfigEntry.setStatus(_B)
class _CtxMeetingConfigStaticMinId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_CtxMeetingConfigStaticMinId_Type.__name__=_E
_CtxMeetingConfigStaticMinId_Object=MibTableColumn
ctxMeetingConfigStaticMinId=_CtxMeetingConfigStaticMinId_Object((1,3,6,1,4,1,9,9,758,1,1,4,4,1,1),_CtxMeetingConfigStaticMinId_Type())
ctxMeetingConfigStaticMinId.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxMeetingConfigStaticMinId.setStatus(_B)
class _CtxMeetingConfigStaticMaxId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_CtxMeetingConfigStaticMaxId_Type.__name__=_E
_CtxMeetingConfigStaticMaxId_Object=MibTableColumn
ctxMeetingConfigStaticMaxId=_CtxMeetingConfigStaticMaxId_Object((1,3,6,1,4,1,9,9,758,1,1,4,4,1,2),_CtxMeetingConfigStaticMaxId_Type())
ctxMeetingConfigStaticMaxId.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxMeetingConfigStaticMaxId.setStatus(_B)
class _CtxMeetingConfigInterOpMinId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_CtxMeetingConfigInterOpMinId_Type.__name__=_E
_CtxMeetingConfigInterOpMinId_Object=MibTableColumn
ctxMeetingConfigInterOpMinId=_CtxMeetingConfigInterOpMinId_Object((1,3,6,1,4,1,9,9,758,1,1,4,4,1,3),_CtxMeetingConfigInterOpMinId_Type())
ctxMeetingConfigInterOpMinId.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxMeetingConfigInterOpMinId.setStatus(_B)
class _CtxMeetingConfigInterOpMaxId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_CtxMeetingConfigInterOpMaxId_Type.__name__=_E
_CtxMeetingConfigInterOpMaxId_Object=MibTableColumn
ctxMeetingConfigInterOpMaxId=_CtxMeetingConfigInterOpMaxId_Object((1,3,6,1,4,1,9,9,758,1,1,4,4,1,4),_CtxMeetingConfigInterOpMaxId_Type())
ctxMeetingConfigInterOpMaxId.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxMeetingConfigInterOpMaxId.setStatus(_B)
_CtxClusterNodeTable_Object=MibTable
ctxClusterNodeTable=_CtxClusterNodeTable_Object((1,3,6,1,4,1,9,9,758,1,1,5))
if mibBuilder.loadTexts:ctxClusterNodeTable.setStatus(_B)
_CtxClusterNodeEntry_Object=MibTableRow
ctxClusterNodeEntry=_CtxClusterNodeEntry_Object((1,3,6,1,4,1,9,9,758,1,1,5,1))
ctxClusterNodeEntry.setIndexNames((0,_A,_k))
if mibBuilder.loadTexts:ctxClusterNodeEntry.setStatus(_B)
_CtxClusterNodeIndex_Type=CtxIndex
_CtxClusterNodeIndex_Object=MibTableColumn
ctxClusterNodeIndex=_CtxClusterNodeIndex_Object((1,3,6,1,4,1,9,9,758,1,1,5,1,1),_CtxClusterNodeIndex_Type())
ctxClusterNodeIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ctxClusterNodeIndex.setStatus(_B)
_CtxClusterNodeKey_Type=CtxKeyId
_CtxClusterNodeKey_Object=MibTableColumn
ctxClusterNodeKey=_CtxClusterNodeKey_Object((1,3,6,1,4,1,9,9,758,1,1,5,1,2),_CtxClusterNodeKey_Type())
ctxClusterNodeKey.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxClusterNodeKey.setStatus(_B)
class _CtxClusterNodeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CtxClusterNodeName_Type.__name__=_E
_CtxClusterNodeName_Object=MibTableColumn
ctxClusterNodeName=_CtxClusterNodeName_Object((1,3,6,1,4,1,9,9,758,1,1,5,1,3),_CtxClusterNodeName_Type())
ctxClusterNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxClusterNodeName.setStatus(_B)
_CtxClusterNodeHostName_Type=DisplayString
_CtxClusterNodeHostName_Object=MibTableColumn
ctxClusterNodeHostName=_CtxClusterNodeHostName_Object((1,3,6,1,4,1,9,9,758,1,1,5,1,4),_CtxClusterNodeHostName_Type())
ctxClusterNodeHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxClusterNodeHostName.setStatus(_B)
_CtxClusterNodeIPType_Type=InetAddressType
_CtxClusterNodeIPType_Object=MibTableColumn
ctxClusterNodeIPType=_CtxClusterNodeIPType_Object((1,3,6,1,4,1,9,9,758,1,1,5,1,5),_CtxClusterNodeIPType_Type())
ctxClusterNodeIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxClusterNodeIPType.setStatus(_B)
_CtxClusterNodeIPAddr_Type=InetAddress
_CtxClusterNodeIPAddr_Object=MibTableColumn
ctxClusterNodeIPAddr=_CtxClusterNodeIPAddr_Object((1,3,6,1,4,1,9,9,758,1,1,5,1,6),_CtxClusterNodeIPAddr_Type())
ctxClusterNodeIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxClusterNodeIPAddr.setStatus(_B)
class _CtxClusterNodeClusterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CtxClusterNodeClusterName_Type.__name__=_E
_CtxClusterNodeClusterName_Object=MibTableColumn
ctxClusterNodeClusterName=_CtxClusterNodeClusterName_Object((1,3,6,1,4,1,9,9,758,1,1,5,1,7),_CtxClusterNodeClusterName_Type())
ctxClusterNodeClusterName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxClusterNodeClusterName.setStatus(_B)
_CtxClusterNodeType_Type=CtxClusterNodeTypes
_CtxClusterNodeType_Object=MibTableColumn
ctxClusterNodeType=_CtxClusterNodeType_Object((1,3,6,1,4,1,9,9,758,1,1,5,1,8),_CtxClusterNodeType_Type())
ctxClusterNodeType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxClusterNodeType.setStatus(_B)
_CtxClusterNodeOperState_Type=CtxResourceOperState
_CtxClusterNodeOperState_Object=MibTableColumn
ctxClusterNodeOperState=_CtxClusterNodeOperState_Object((1,3,6,1,4,1,9,9,758,1,1,5,1,9),_CtxClusterNodeOperState_Type())
ctxClusterNodeOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxClusterNodeOperState.setStatus(_B)
_CtxSystemStatusObjects_ObjectIdentity=ObjectIdentity
ctxSystemStatusObjects=_CtxSystemStatusObjects_ObjectIdentity((1,3,6,1,4,1,9,9,758,1,2))
_CtxAdminServersStatus_Type=CtxHealthStates
_CtxAdminServersStatus_Object=MibScalar
ctxAdminServersStatus=_CtxAdminServersStatus_Object((1,3,6,1,4,1,9,9,758,1,2,1),_CtxAdminServersStatus_Type())
ctxAdminServersStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxAdminServersStatus.setStatus(_B)
_CtxCallEnginesStatus_Type=CtxHealthStates
_CtxCallEnginesStatus_Object=MibScalar
ctxCallEnginesStatus=_CtxCallEnginesStatus_Object((1,3,6,1,4,1,9,9,758,1,2,2),_CtxCallEnginesStatus_Type())
ctxCallEnginesStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxCallEnginesStatus.setStatus(_B)
_CtxDatabaseServersStatus_Type=CtxHealthStates
_CtxDatabaseServersStatus_Object=MibScalar
ctxDatabaseServersStatus=_CtxDatabaseServersStatus_Object((1,3,6,1,4,1,9,9,758,1,2,3),_CtxDatabaseServersStatus_Type())
ctxDatabaseServersStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxDatabaseServersStatus.setStatus(_B)
_CtxResourceStatus_Type=CtxHealthStates
_CtxResourceStatus_Object=MibScalar
ctxResourceStatus=_CtxResourceStatus_Object((1,3,6,1,4,1,9,9,758,1,2,4),_CtxResourceStatus_Type())
ctxResourceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxResourceStatus.setStatus(_B)
_CtxSystemConfigStatus_Type=CtxHealthStates
_CtxSystemConfigStatus_Object=MibScalar
ctxSystemConfigStatus=_CtxSystemConfigStatus_Object((1,3,6,1,4,1,9,9,758,1,2,5),_CtxSystemConfigStatus_Type())
ctxSystemConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxSystemConfigStatus.setStatus(_B)
_CtxSystemBackupStatus_Type=CtxHealthStates
_CtxSystemBackupStatus_Object=MibScalar
ctxSystemBackupStatus=_CtxSystemBackupStatus_Object((1,3,6,1,4,1,9,9,758,1,2,6),_CtxSystemBackupStatus_Type())
ctxSystemBackupStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxSystemBackupStatus.setStatus(_B)
_CtxStatisticsObjects_ObjectIdentity=ObjectIdentity
ctxStatisticsObjects=_CtxStatisticsObjects_ObjectIdentity((1,3,6,1,4,1,9,9,758,1,3))
_CtxResourceStatsTable_Object=MibTable
ctxResourceStatsTable=_CtxResourceStatsTable_Object((1,3,6,1,4,1,9,9,758,1,3,1))
if mibBuilder.loadTexts:ctxResourceStatsTable.setStatus(_B)
_CtxResourceStatsEntry_Object=MibTableRow
ctxResourceStatsEntry=_CtxResourceStatsEntry_Object((1,3,6,1,4,1,9,9,758,1,3,1,1))
ctxResourceStatsEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:ctxResourceStatsEntry.setStatus(_B)
_CtxResourceOperState_Type=CtxResourceOperState
_CtxResourceOperState_Object=MibTableColumn
ctxResourceOperState=_CtxResourceOperState_Object((1,3,6,1,4,1,9,9,758,1,3,1,1,1),_CtxResourceOperState_Type())
ctxResourceOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxResourceOperState.setStatus(_B)
_CtxResourceUnavailTrans_Type=Counter32
_CtxResourceUnavailTrans_Object=MibTableColumn
ctxResourceUnavailTrans=_CtxResourceUnavailTrans_Object((1,3,6,1,4,1,9,9,758,1,3,1,1,2),_CtxResourceUnavailTrans_Type())
ctxResourceUnavailTrans.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxResourceUnavailTrans.setStatus(_B)
if mibBuilder.loadTexts:ctxResourceUnavailTrans.setUnits(_O)
_CtxResourceUnavailDuration_Type=Counter32
_CtxResourceUnavailDuration_Object=MibTableColumn
ctxResourceUnavailDuration=_CtxResourceUnavailDuration_Object((1,3,6,1,4,1,9,9,758,1,3,1,1,3),_CtxResourceUnavailDuration_Type())
ctxResourceUnavailDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxResourceUnavailDuration.setStatus(_B)
if mibBuilder.loadTexts:ctxResourceUnavailDuration.setUnits('seconds')
_CtxResourceCallSetupFailures_Type=Counter32
_CtxResourceCallSetupFailures_Object=MibTableColumn
ctxResourceCallSetupFailures=_CtxResourceCallSetupFailures_Object((1,3,6,1,4,1,9,9,758,1,3,1,1,4),_CtxResourceCallSetupFailures_Type())
ctxResourceCallSetupFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxResourceCallSetupFailures.setStatus(_B)
if mibBuilder.loadTexts:ctxResourceCallSetupFailures.setUnits(_O)
_CtxAllocStatsTable_Object=MibTable
ctxAllocStatsTable=_CtxAllocStatsTable_Object((1,3,6,1,4,1,9,9,758,1,3,2))
if mibBuilder.loadTexts:ctxAllocStatsTable.setStatus(_B)
_CtxAllocStatsEntry_Object=MibTableRow
ctxAllocStatsEntry=_CtxAllocStatsEntry_Object((1,3,6,1,4,1,9,9,758,1,3,2,1))
ctxAllocStatsEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:ctxAllocStatsEntry.setStatus(_B)
_CtxAllocActivePorts_Type=CtxPorts
_CtxAllocActivePorts_Object=MibTableColumn
ctxAllocActivePorts=_CtxAllocActivePorts_Object((1,3,6,1,4,1,9,9,758,1,3,2,1,1),_CtxAllocActivePorts_Type())
ctxAllocActivePorts.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxAllocActivePorts.setStatus(_B)
_CtxAllocAvailPorts_Type=CtxPorts
_CtxAllocAvailPorts_Object=MibTableColumn
ctxAllocAvailPorts=_CtxAllocAvailPorts_Object((1,3,6,1,4,1,9,9,758,1,3,2,1,2),_CtxAllocAvailPorts_Type())
ctxAllocAvailPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxAllocAvailPorts.setStatus(_B)
_CtxAllocFailures_Type=Counter32
_CtxAllocFailures_Object=MibTableColumn
ctxAllocFailures=_CtxAllocFailures_Object((1,3,6,1,4,1,9,9,758,1,3,2,1,3),_CtxAllocFailures_Type())
ctxAllocFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxAllocFailures.setStatus(_B)
if mibBuilder.loadTexts:ctxAllocFailures.setUnits(_T)
_CtxAllocOutOfPorts_Type=Counter32
_CtxAllocOutOfPorts_Object=MibTableColumn
ctxAllocOutOfPorts=_CtxAllocOutOfPorts_Object((1,3,6,1,4,1,9,9,758,1,3,2,1,4),_CtxAllocOutOfPorts_Type())
ctxAllocOutOfPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxAllocOutOfPorts.setStatus(_B)
if mibBuilder.loadTexts:ctxAllocOutOfPorts.setUnits(_O)
_CtxRegionStatsTable_Object=MibTable
ctxRegionStatsTable=_CtxRegionStatsTable_Object((1,3,6,1,4,1,9,9,758,1,3,3))
if mibBuilder.loadTexts:ctxRegionStatsTable.setStatus(_B)
_CtxRegionStatsEntry_Object=MibTableRow
ctxRegionStatsEntry=_CtxRegionStatsEntry_Object((1,3,6,1,4,1,9,9,758,1,3,3,1))
ctxRegionStatsEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:ctxRegionStatsEntry.setStatus(_B)
_CtxRegionCallSetupFailures_Type=Counter32
_CtxRegionCallSetupFailures_Object=MibTableColumn
ctxRegionCallSetupFailures=_CtxRegionCallSetupFailures_Object((1,3,6,1,4,1,9,9,758,1,3,3,1,1),_CtxRegionCallSetupFailures_Type())
ctxRegionCallSetupFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxRegionCallSetupFailures.setStatus(_B)
if mibBuilder.loadTexts:ctxRegionCallSetupFailures.setUnits(_T)
_CtxAllocPoolActivePorts_Type=CtxPorts
_CtxAllocPoolActivePorts_Object=MibTableColumn
ctxAllocPoolActivePorts=_CtxAllocPoolActivePorts_Object((1,3,6,1,4,1,9,9,758,1,3,3,1,2),_CtxAllocPoolActivePorts_Type())
ctxAllocPoolActivePorts.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxAllocPoolActivePorts.setStatus(_B)
_CtxAllocPoolAvailPorts_Type=CtxPorts
_CtxAllocPoolAvailPorts_Object=MibTableColumn
ctxAllocPoolAvailPorts=_CtxAllocPoolAvailPorts_Object((1,3,6,1,4,1,9,9,758,1,3,3,1,3),_CtxAllocPoolAvailPorts_Type())
ctxAllocPoolAvailPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxAllocPoolAvailPorts.setStatus(_B)
_CtxAllocPoolAllocFailures_Type=Counter32
_CtxAllocPoolAllocFailures_Object=MibTableColumn
ctxAllocPoolAllocFailures=_CtxAllocPoolAllocFailures_Object((1,3,6,1,4,1,9,9,758,1,3,3,1,4),_CtxAllocPoolAllocFailures_Type())
ctxAllocPoolAllocFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxAllocPoolAllocFailures.setStatus(_B)
if mibBuilder.loadTexts:ctxAllocPoolAllocFailures.setUnits(_T)
_CtxAllocPoolAllocOutOfPorts_Type=Counter32
_CtxAllocPoolAllocOutOfPorts_Object=MibTableColumn
ctxAllocPoolAllocOutOfPorts=_CtxAllocPoolAllocOutOfPorts_Object((1,3,6,1,4,1,9,9,758,1,3,3,1,5),_CtxAllocPoolAllocOutOfPorts_Type())
ctxAllocPoolAllocOutOfPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxAllocPoolAllocOutOfPorts.setStatus(_B)
if mibBuilder.loadTexts:ctxAllocPoolAllocOutOfPorts.setUnits(_O)
_CtxAllocPeakHistory_ObjectIdentity=ObjectIdentity
ctxAllocPeakHistory=_CtxAllocPeakHistory_ObjectIdentity((1,3,6,1,4,1,9,9,758,1,3,4))
class _CtxPeakHistMaxIntervals_Type(Unsigned32):defaultValue=96;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,1440))
_CtxPeakHistMaxIntervals_Type.__name__=_M
_CtxPeakHistMaxIntervals_Object=MibScalar
ctxPeakHistMaxIntervals=_CtxPeakHistMaxIntervals_Object((1,3,6,1,4,1,9,9,758,1,3,4,1),_CtxPeakHistMaxIntervals_Type())
ctxPeakHistMaxIntervals.setMaxAccess(_F)
if mibBuilder.loadTexts:ctxPeakHistMaxIntervals.setStatus(_B)
if mibBuilder.loadTexts:ctxPeakHistMaxIntervals.setUnits('intervals')
class _CtxPeakHistIntTime_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_CtxPeakHistIntTime_Type.__name__=_M
_CtxPeakHistIntTime_Object=MibScalar
ctxPeakHistIntTime=_CtxPeakHistIntTime_Object((1,3,6,1,4,1,9,9,758,1,3,4,2),_CtxPeakHistIntTime_Type())
ctxPeakHistIntTime.setMaxAccess(_F)
if mibBuilder.loadTexts:ctxPeakHistIntTime.setStatus(_B)
if mibBuilder.loadTexts:ctxPeakHistIntTime.setUnits('minutes')
_CtxPeakHistAllocTable_Object=MibTable
ctxPeakHistAllocTable=_CtxPeakHistAllocTable_Object((1,3,6,1,4,1,9,9,758,1,3,4,3))
if mibBuilder.loadTexts:ctxPeakHistAllocTable.setStatus(_B)
_CtxPeakHistAllocEntry_Object=MibTableRow
ctxPeakHistAllocEntry=_CtxPeakHistAllocEntry_Object((1,3,6,1,4,1,9,9,758,1,3,4,3,1))
ctxPeakHistAllocEntry.setIndexNames((0,_A,_I),(0,_A,_l))
if mibBuilder.loadTexts:ctxPeakHistAllocEntry.setStatus(_B)
class _CtxPeakHistAllocIntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CtxPeakHistAllocIntIndex_Type.__name__=_S
_CtxPeakHistAllocIntIndex_Object=MibTableColumn
ctxPeakHistAllocIntIndex=_CtxPeakHistAllocIntIndex_Object((1,3,6,1,4,1,9,9,758,1,3,4,3,1,1),_CtxPeakHistAllocIntIndex_Type())
ctxPeakHistAllocIntIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ctxPeakHistAllocIntIndex.setStatus(_B)
_CtxPeakHistAllocTS_Type=TimeStamp
_CtxPeakHistAllocTS_Object=MibTableColumn
ctxPeakHistAllocTS=_CtxPeakHistAllocTS_Object((1,3,6,1,4,1,9,9,758,1,3,4,3,1,2),_CtxPeakHistAllocTS_Type())
ctxPeakHistAllocTS.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxPeakHistAllocTS.setStatus(_B)
_CtxPeakHistAllocPorts_Type=CtxPorts
_CtxPeakHistAllocPorts_Object=MibTableColumn
ctxPeakHistAllocPorts=_CtxPeakHistAllocPorts_Object((1,3,6,1,4,1,9,9,758,1,3,4,3,1,3),_CtxPeakHistAllocPorts_Type())
ctxPeakHistAllocPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxPeakHistAllocPorts.setStatus(_B)
if mibBuilder.loadTexts:ctxPeakHistAllocPorts.setUnits('ports')
_CtxPeakHistAllocPoolTable_Object=MibTable
ctxPeakHistAllocPoolTable=_CtxPeakHistAllocPoolTable_Object((1,3,6,1,4,1,9,9,758,1,3,4,4))
if mibBuilder.loadTexts:ctxPeakHistAllocPoolTable.setStatus(_B)
_CtxPeakHistAllocPoolEntry_Object=MibTableRow
ctxPeakHistAllocPoolEntry=_CtxPeakHistAllocPoolEntry_Object((1,3,6,1,4,1,9,9,758,1,3,4,4,1))
ctxPeakHistAllocPoolEntry.setIndexNames((0,_A,_N),(0,_A,_m))
if mibBuilder.loadTexts:ctxPeakHistAllocPoolEntry.setStatus(_B)
class _CtxPeakHistAllocPoolIntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CtxPeakHistAllocPoolIntIndex_Type.__name__=_S
_CtxPeakHistAllocPoolIntIndex_Object=MibTableColumn
ctxPeakHistAllocPoolIntIndex=_CtxPeakHistAllocPoolIntIndex_Object((1,3,6,1,4,1,9,9,758,1,3,4,4,1,1),_CtxPeakHistAllocPoolIntIndex_Type())
ctxPeakHistAllocPoolIntIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ctxPeakHistAllocPoolIntIndex.setStatus(_B)
_CtxPeakHistAllocPoolTS_Type=TimeStamp
_CtxPeakHistAllocPoolTS_Object=MibTableColumn
ctxPeakHistAllocPoolTS=_CtxPeakHistAllocPoolTS_Object((1,3,6,1,4,1,9,9,758,1,3,4,4,1,2),_CtxPeakHistAllocPoolTS_Type())
ctxPeakHistAllocPoolTS.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxPeakHistAllocPoolTS.setStatus(_B)
_CtxPeakHistAllocPoolPorts_Type=CtxPorts
_CtxPeakHistAllocPoolPorts_Object=MibTableColumn
ctxPeakHistAllocPoolPorts=_CtxPeakHistAllocPoolPorts_Object((1,3,6,1,4,1,9,9,758,1,3,4,4,1,3),_CtxPeakHistAllocPoolPorts_Type())
ctxPeakHistAllocPoolPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxPeakHistAllocPoolPorts.setStatus(_B)
if mibBuilder.loadTexts:ctxPeakHistAllocPoolPorts.setUnits('ports')
_CtxEventHistory_ObjectIdentity=ObjectIdentity
ctxEventHistory=_CtxEventHistory_ObjectIdentity((1,3,6,1,4,1,9,9,758,1,4))
class _CtxErrorHistoryTableSize_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(25,2500))
_CtxErrorHistoryTableSize_Type.__name__=_M
_CtxErrorHistoryTableSize_Object=MibScalar
ctxErrorHistoryTableSize=_CtxErrorHistoryTableSize_Object((1,3,6,1,4,1,9,9,758,1,4,1),_CtxErrorHistoryTableSize_Type())
ctxErrorHistoryTableSize.setMaxAccess(_F)
if mibBuilder.loadTexts:ctxErrorHistoryTableSize.setStatus(_B)
class _CtxErrorHistoryMaxSeverity_Type(SyslogSeverity):defaultValue=6
_CtxErrorHistoryMaxSeverity_Type.__name__=_h
_CtxErrorHistoryMaxSeverity_Object=MibScalar
ctxErrorHistoryMaxSeverity=_CtxErrorHistoryMaxSeverity_Object((1,3,6,1,4,1,9,9,758,1,4,2),_CtxErrorHistoryMaxSeverity_Type())
ctxErrorHistoryMaxSeverity.setMaxAccess(_F)
if mibBuilder.loadTexts:ctxErrorHistoryMaxSeverity.setStatus(_B)
_CtxErrorHistoryLastIndex_Type=CtxIndex
_CtxErrorHistoryLastIndex_Object=MibScalar
ctxErrorHistoryLastIndex=_CtxErrorHistoryLastIndex_Object((1,3,6,1,4,1,9,9,758,1,4,3),_CtxErrorHistoryLastIndex_Type())
ctxErrorHistoryLastIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxErrorHistoryLastIndex.setStatus(_B)
_CtxErrorHistoryTable_Object=MibTable
ctxErrorHistoryTable=_CtxErrorHistoryTable_Object((1,3,6,1,4,1,9,9,758,1,4,4))
if mibBuilder.loadTexts:ctxErrorHistoryTable.setStatus(_B)
_CtxErrorHistoryEntry_Object=MibTableRow
ctxErrorHistoryEntry=_CtxErrorHistoryEntry_Object((1,3,6,1,4,1,9,9,758,1,4,4,1))
ctxErrorHistoryEntry.setIndexNames((0,_A,_n))
if mibBuilder.loadTexts:ctxErrorHistoryEntry.setStatus(_B)
_CtxErrorIndex_Type=CtxIndex
_CtxErrorIndex_Object=MibTableColumn
ctxErrorIndex=_CtxErrorIndex_Object((1,3,6,1,4,1,9,9,758,1,4,4,1,1),_CtxErrorIndex_Type())
ctxErrorIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ctxErrorIndex.setStatus(_B)
_CtxErrorKey_Type=CtxKeyId
_CtxErrorKey_Object=MibTableColumn
ctxErrorKey=_CtxErrorKey_Object((1,3,6,1,4,1,9,9,758,1,4,4,1,2),_CtxErrorKey_Type())
ctxErrorKey.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxErrorKey.setStatus(_B)
_CtxErrorTimeStamp_Type=TimeStamp
_CtxErrorTimeStamp_Object=MibTableColumn
ctxErrorTimeStamp=_CtxErrorTimeStamp_Object((1,3,6,1,4,1,9,9,758,1,4,4,1,3),_CtxErrorTimeStamp_Type())
ctxErrorTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxErrorTimeStamp.setStatus(_B)
_CtxErrorSeverity_Type=SyslogSeverity
_CtxErrorSeverity_Object=MibTableColumn
ctxErrorSeverity=_CtxErrorSeverity_Object((1,3,6,1,4,1,9,9,758,1,4,4,1,4),_CtxErrorSeverity_Type())
ctxErrorSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxErrorSeverity.setStatus(_B)
class _CtxErrorAppName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_CtxErrorAppName_Type.__name__=_E
_CtxErrorAppName_Object=MibTableColumn
ctxErrorAppName=_CtxErrorAppName_Object((1,3,6,1,4,1,9,9,758,1,4,4,1,5),_CtxErrorAppName_Type())
ctxErrorAppName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxErrorAppName.setStatus(_B)
class _CtxErrorAlarmId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CtxErrorAlarmId_Type.__name__=_E
_CtxErrorAlarmId_Object=MibTableColumn
ctxErrorAlarmId=_CtxErrorAlarmId_Object((1,3,6,1,4,1,9,9,758,1,4,4,1,6),_CtxErrorAlarmId_Type())
ctxErrorAlarmId.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxErrorAlarmId.setStatus(_B)
_CtxErrorAttrValStr_Type=DisplayString
_CtxErrorAttrValStr_Object=MibTableColumn
ctxErrorAttrValStr=_CtxErrorAttrValStr_Object((1,3,6,1,4,1,9,9,758,1,4,4,1,7),_CtxErrorAttrValStr_Type())
ctxErrorAttrValStr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxErrorAttrValStr.setStatus(_B)
_CtxErrorMessage_Type=DisplayString
_CtxErrorMessage_Object=MibTableColumn
ctxErrorMessage=_CtxErrorMessage_Object((1,3,6,1,4,1,9,9,758,1,4,4,1,8),_CtxErrorMessage_Type())
ctxErrorMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:ctxErrorMessage.setStatus(_B)
_CtxNotifyObjects_ObjectIdentity=ObjectIdentity
ctxNotifyObjects=_CtxNotifyObjects_ObjectIdentity((1,3,6,1,4,1,9,9,758,1,5))
_CtxNotifyMessage_Type=DisplayString
_CtxNotifyMessage_Object=MibScalar
ctxNotifyMessage=_CtxNotifyMessage_Object((1,3,6,1,4,1,9,9,758,1,5,1),_CtxNotifyMessage_Type())
ctxNotifyMessage.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:ctxNotifyMessage.setStatus(_B)
_CtxNotifyConfigObjects_ObjectIdentity=ObjectIdentity
ctxNotifyConfigObjects=_CtxNotifyConfigObjects_ObjectIdentity((1,3,6,1,4,1,9,9,758,1,5,2))
class _CtxStatusChangeNotifyEnable_Type(TruthValue):defaultValue=1
_CtxStatusChangeNotifyEnable_Type.__name__=_G
_CtxStatusChangeNotifyEnable_Object=MibScalar
ctxStatusChangeNotifyEnable=_CtxStatusChangeNotifyEnable_Object((1,3,6,1,4,1,9,9,758,1,5,2,1),_CtxStatusChangeNotifyEnable_Type())
ctxStatusChangeNotifyEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:ctxStatusChangeNotifyEnable.setStatus(_B)
class _CtxLicenseAlarmNotifyEnable_Type(TruthValue):defaultValue=1
_CtxLicenseAlarmNotifyEnable_Type.__name__=_G
_CtxLicenseAlarmNotifyEnable_Object=MibScalar
ctxLicenseAlarmNotifyEnable=_CtxLicenseAlarmNotifyEnable_Object((1,3,6,1,4,1,9,9,758,1,5,2,2),_CtxLicenseAlarmNotifyEnable_Type())
ctxLicenseAlarmNotifyEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:ctxLicenseAlarmNotifyEnable.setStatus(_B)
class _CtxAuthFailureNotifyEnable_Type(TruthValue):defaultValue=2
_CtxAuthFailureNotifyEnable_Type.__name__=_G
_CtxAuthFailureNotifyEnable_Object=MibScalar
ctxAuthFailureNotifyEnable=_CtxAuthFailureNotifyEnable_Object((1,3,6,1,4,1,9,9,758,1,5,2,3),_CtxAuthFailureNotifyEnable_Type())
ctxAuthFailureNotifyEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:ctxAuthFailureNotifyEnable.setStatus(_B)
class _CtxClusterNodeAlarmNotifyEnable_Type(TruthValue):defaultValue=1
_CtxClusterNodeAlarmNotifyEnable_Type.__name__=_G
_CtxClusterNodeAlarmNotifyEnable_Object=MibScalar
ctxClusterNodeAlarmNotifyEnable=_CtxClusterNodeAlarmNotifyEnable_Object((1,3,6,1,4,1,9,9,758,1,5,2,4),_CtxClusterNodeAlarmNotifyEnable_Type())
ctxClusterNodeAlarmNotifyEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:ctxClusterNodeAlarmNotifyEnable.setStatus(_B)
class _CtxResourceAlarmNotifyEnable_Type(TruthValue):defaultValue=1
_CtxResourceAlarmNotifyEnable_Type.__name__=_G
_CtxResourceAlarmNotifyEnable_Object=MibScalar
ctxResourceAlarmNotifyEnable=_CtxResourceAlarmNotifyEnable_Object((1,3,6,1,4,1,9,9,758,1,5,2,5),_CtxResourceAlarmNotifyEnable_Type())
ctxResourceAlarmNotifyEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:ctxResourceAlarmNotifyEnable.setStatus(_B)
class _CtxCallFailureNotifyEnable_Type(TruthValue):defaultValue=1
_CtxCallFailureNotifyEnable_Type.__name__=_G
_CtxCallFailureNotifyEnable_Object=MibScalar
ctxCallFailureNotifyEnable=_CtxCallFailureNotifyEnable_Object((1,3,6,1,4,1,9,9,758,1,5,2,6),_CtxCallFailureNotifyEnable_Type())
ctxCallFailureNotifyEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:ctxCallFailureNotifyEnable.setStatus(_B)
class _CtxErrorHistoryEventNotifyEnable_Type(TruthValue):defaultValue=2
_CtxErrorHistoryEventNotifyEnable_Type.__name__=_G
_CtxErrorHistoryEventNotifyEnable_Object=MibScalar
ctxErrorHistoryEventNotifyEnable=_CtxErrorHistoryEventNotifyEnable_Object((1,3,6,1,4,1,9,9,758,1,5,2,7),_CtxErrorHistoryEventNotifyEnable_Type())
ctxErrorHistoryEventNotifyEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:ctxErrorHistoryEventNotifyEnable.setStatus(_B)
_CiscoTelepresenceExchangeSystemMIBConform_ObjectIdentity=ObjectIdentity
ciscoTelepresenceExchangeSystemMIBConform=_CiscoTelepresenceExchangeSystemMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,758,7))
_CiscoTelepresenceExchangeSystemMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoTelepresenceExchangeSystemMIBCompliances=_CiscoTelepresenceExchangeSystemMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,758,7,1))
_CiscoTelepresenceExchangeSystemMIBGroups_ObjectIdentity=ObjectIdentity
ciscoTelepresenceExchangeSystemMIBGroups=_CiscoTelepresenceExchangeSystemMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,758,7,2))
ciscoTelepresenceExchangeSystemMIBStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,758,7,2,1))
ciscoTelepresenceExchangeSystemMIBStatusGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:ciscoTelepresenceExchangeSystemMIBStatusGroup.setStatus(_B)
ciscoTelepresenceExchangeSystemMIBConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,758,7,2,2))
ciscoTelepresenceExchangeSystemMIBConfigGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_P),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_J),(_A,_w),(_A,_x),(_A,_y),(_A,_K),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_Q),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_R),(_A,_A9),(_A,_a),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:ciscoTelepresenceExchangeSystemMIBConfigGroup.setStatus(_B)
ciscoTelePresenceExchangeSystemMIBStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,758,7,2,3))
ciscoTelePresenceExchangeSystemMIBStatsGroup.setObjects(*((_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad)))
if mibBuilder.loadTexts:ciscoTelePresenceExchangeSystemMIBStatsGroup.setStatus(_B)
ciscoTelepresenceExchangeSystemMIBNotfyObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,758,7,2,4))
ciscoTelepresenceExchangeSystemMIBNotfyObjectsGroup.setObjects(*((_A,_D),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak)))
if mibBuilder.loadTexts:ciscoTelepresenceExchangeSystemMIBNotfyObjectsGroup.setStatus(_B)
ciscoTelepresenceExchangeSystemMIBErrorHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,9,758,7,2,5))
ciscoTelepresenceExchangeSystemMIBErrorHistoryGroup.setObjects(*((_A,_Al),(_A,_Am),(_A,_An),(_A,_b),(_A,_Ao),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:ciscoTelepresenceExchangeSystemMIBErrorHistoryGroup.setStatus(_B)
ciscoCTXSysAdminServersStatusChg=NotificationType((1,3,6,1,4,1,9,9,758,0,1))
ciscoCTXSysAdminServersStatusChg.setObjects(*((_A,_U),(_A,_D)))
if mibBuilder.loadTexts:ciscoCTXSysAdminServersStatusChg.setStatus(_B)
ciscoCTXSysDatabaseServersStatusChg=NotificationType((1,3,6,1,4,1,9,9,758,0,2))
ciscoCTXSysDatabaseServersStatusChg.setObjects(*((_A,_W),(_A,_D)))
if mibBuilder.loadTexts:ciscoCTXSysDatabaseServersStatusChg.setStatus(_B)
ciscoCTXSysCallEnginesStatusChg=NotificationType((1,3,6,1,4,1,9,9,758,0,3))
ciscoCTXSysCallEnginesStatusChg.setObjects(*((_A,_V),(_A,_D)))
if mibBuilder.loadTexts:ciscoCTXSysCallEnginesStatusChg.setStatus(_B)
ciscoCTXSysResourceStatusChg=NotificationType((1,3,6,1,4,1,9,9,758,0,4))
ciscoCTXSysResourceStatusChg.setObjects(*((_A,_X),(_A,_D)))
if mibBuilder.loadTexts:ciscoCTXSysResourceStatusChg.setStatus(_B)
ciscoCTXSysSystemConfigStatusChg=NotificationType((1,3,6,1,4,1,9,9,758,0,5))
ciscoCTXSysSystemConfigStatusChg.setObjects(*((_A,_Y),(_A,_D)))
if mibBuilder.loadTexts:ciscoCTXSysSystemConfigStatusChg.setStatus(_B)
ciscoCTXSysSystemBackupStatusChg=NotificationType((1,3,6,1,4,1,9,9,758,0,6))
ciscoCTXSysSystemBackupStatusChg.setObjects(*((_A,_Z),(_A,_D)))
if mibBuilder.loadTexts:ciscoCTXSysSystemBackupStatusChg.setStatus(_B)
ciscoCTXSysLicenseFailure=NotificationType((1,3,6,1,4,1,9,9,758,0,7))
ciscoCTXSysLicenseFailure.setObjects((_A,_D))
if mibBuilder.loadTexts:ciscoCTXSysLicenseFailure.setStatus(_B)
ciscoCTXSysUserAuthFailure=NotificationType((1,3,6,1,4,1,9,9,758,0,8))
ciscoCTXSysUserAuthFailure.setObjects((_A,_D))
if mibBuilder.loadTexts:ciscoCTXSysUserAuthFailure.setStatus(_B)
ciscoCTXSysClusterNodeDown=NotificationType((1,3,6,1,4,1,9,9,758,0,9))
ciscoCTXSysClusterNodeDown.setObjects(*((_A,_R),(_A,_Q),(_A,_D)))
if mibBuilder.loadTexts:ciscoCTXSysClusterNodeDown.setStatus(_B)
ciscoCTXSysClusterNodeUp=NotificationType((1,3,6,1,4,1,9,9,758,0,10))
ciscoCTXSysClusterNodeUp.setObjects(*((_A,_R),(_A,_Q),(_A,_D)))
if mibBuilder.loadTexts:ciscoCTXSysClusterNodeUp.setStatus(_B)
ciscoCTXSysResourceDown=NotificationType((1,3,6,1,4,1,9,9,758,0,11))
ciscoCTXSysResourceDown.setObjects(*((_A,_J),(_A,_K),(_A,_P),(_A,_D)))
if mibBuilder.loadTexts:ciscoCTXSysResourceDown.setStatus(_B)
ciscoCTXSysResourceUp=NotificationType((1,3,6,1,4,1,9,9,758,0,12))
ciscoCTXSysResourceUp.setObjects(*((_A,_J),(_A,_K),(_A,_P),(_A,_D)))
if mibBuilder.loadTexts:ciscoCTXSysResourceUp.setStatus(_B)
ciscoCTXSysResourceAllocFailure=NotificationType((1,3,6,1,4,1,9,9,758,0,13))
ciscoCTXSysResourceAllocFailure.setObjects(*((_A,_J),(_A,_K),(_A,_a),(_A,_D)))
if mibBuilder.loadTexts:ciscoCTXSysResourceAllocFailure.setStatus(_B)
ciscoCTXSysCallSetupFailure=NotificationType((1,3,6,1,4,1,9,9,758,0,14))
ciscoCTXSysCallSetupFailure.setObjects(*((_A,_J),(_A,_K),(_A,_D)))
if mibBuilder.loadTexts:ciscoCTXSysCallSetupFailure.setStatus(_B)
ciscoCTXSysCallAbnormalDisconnect=NotificationType((1,3,6,1,4,1,9,9,758,0,15))
ciscoCTXSysCallAbnormalDisconnect.setObjects(*((_A,_J),(_A,_K),(_A,_D)))
if mibBuilder.loadTexts:ciscoCTXSysCallAbnormalDisconnect.setStatus(_B)
ciscoCTXSysErrorHistoryEvent=NotificationType((1,3,6,1,4,1,9,9,758,0,16))
ciscoCTXSysErrorHistoryEvent.setObjects(*((_A,_b),(_A,_c),(_A,_e),(_A,_f),(_A,_g),(_A,_d)))
if mibBuilder.loadTexts:ciscoCTXSysErrorHistoryEvent.setStatus(_B)
ciscoTelepresenceExchangeSystemMIBNotifyGroup=NotificationGroup((1,3,6,1,4,1,9,9,758,7,2,6))
ciscoTelepresenceExchangeSystemMIBNotifyGroup.setObjects(*((_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3)))
if mibBuilder.loadTexts:ciscoTelepresenceExchangeSystemMIBNotifyGroup.setStatus(_B)
ciscoTelepresenceExchangeSystemMIBModuleCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,758,7,1,1))
ciscoTelepresenceExchangeSystemMIBModuleCompliance.setObjects(*((_A,_B4),(_A,_B5),(_A,_B6),(_A,_B7),(_A,_B8),(_A,_B9)))
if mibBuilder.loadTexts:ciscoTelepresenceExchangeSystemMIBModuleCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CtxKeyId':CtxKeyId,'CtxIndex':CtxIndex,'CtxPorts':CtxPorts,'CtxClusterNodeTypes':CtxClusterNodeTypes,'CtxHealthStates':CtxHealthStates,'CtxResourceOperState':CtxResourceOperState,'CtxSIPProtocolType':CtxSIPProtocolType,'CtxResourceType':CtxResourceType,'ciscoTelepresenceExchangeSystemMIB':ciscoTelepresenceExchangeSystemMIB,'ciscoTelepresenceExchangeSystemMIBNotifs':ciscoTelepresenceExchangeSystemMIBNotifs,_Ap:ciscoCTXSysAdminServersStatusChg,_Aq:ciscoCTXSysDatabaseServersStatusChg,_Ar:ciscoCTXSysCallEnginesStatusChg,_As:ciscoCTXSysResourceStatusChg,_At:ciscoCTXSysSystemConfigStatusChg,_Au:ciscoCTXSysSystemBackupStatusChg,_Av:ciscoCTXSysLicenseFailure,_Aw:ciscoCTXSysUserAuthFailure,_Ax:ciscoCTXSysClusterNodeDown,_B2:ciscoCTXSysClusterNodeUp,_Ay:ciscoCTXSysResourceDown,_B3:ciscoCTXSysResourceUp,_B1:ciscoCTXSysResourceAllocFailure,_Az:ciscoCTXSysCallSetupFailure,_B0:ciscoCTXSysCallAbnormalDisconnect,_A_:ciscoCTXSysErrorHistoryEvent,'ciscoTelepresenceExchangeSystemMIBObjects':ciscoTelepresenceExchangeSystemMIBObjects,'ctxConfigObjects':ctxConfigObjects,'ctxServiceProviderTable':ctxServiceProviderTable,'ctxServiceProviderEntry':ctxServiceProviderEntry,_i:ctxServiceProviderIndex,_A9:ctxServiceProviderKey,_o:ctxServiceProviderName,_p:ctxServiceProviderDescr,_q:ctxServiceProviderHDNumber,'ctxRegionTable':ctxRegionTable,'ctxRegionEntry':ctxRegionEntry,_N:ctxRegionIndex,_a:ctxRegionKey,_P:ctxRegionName,_r:ctxRegionDescr,_AA:ctxRegionServiceProviderKeyRef1,'ctxOrganizationTable':ctxOrganizationTable,'ctxOrganizationEntry':ctxOrganizationEntry,_j:ctxOrganizationIndex,_AB:ctxOrganizationKey,_s:ctxOrganizationName,_t:ctxOrganizationDescr,_u:ctxOrganizationMaxPorts,_v:ctxOrganizationDirectDial,_AC:ctxOrganizationServiceProviderKeyRef1,'ctxResourceObjects':ctxResourceObjects,'ctxResourceTable':ctxResourceTable,'ctxResourceEntry':ctxResourceEntry,_I:ctxResourceIndex,_AD:ctxResourceKey,_J:ctxResourceName,_w:ctxResourceDescr,_x:ctxResourceMgmtIPType,_y:ctxResourceMgmtIPAddr,_K:ctxResourceDeviceType,_AE:ctxResourceRegionKeyRef1,'ctxSipConfigTable':ctxSipConfigTable,'ctxSipConfigEntry':ctxSipConfigEntry,_z:ctxSipIpType,_A0:ctxSipIpAddr,_A1:ctxSipPort,_A2:ctxSipTransportProto,'ctxMediaCapacityConfigTable':ctxMediaCapacityConfigTable,'ctxMediaCapacityConfigEntry':ctxMediaCapacityConfigEntry,_A3:ctxMediaCapacityMaxPorts,_A4:ctxMediaCapacityLargeMeeting,'ctxMeetingConfigTable':ctxMeetingConfigTable,'ctxMeetingConfigEntry':ctxMeetingConfigEntry,_AH:ctxMeetingConfigStaticMinId,_AI:ctxMeetingConfigStaticMaxId,_AJ:ctxMeetingConfigInterOpMinId,_AK:ctxMeetingConfigInterOpMaxId,'ctxClusterNodeTable':ctxClusterNodeTable,'ctxClusterNodeEntry':ctxClusterNodeEntry,_k:ctxClusterNodeIndex,_AG:ctxClusterNodeKey,_Q:ctxClusterNodeName,_A5:ctxClusterNodeHostName,_A6:ctxClusterNodeIPType,_A7:ctxClusterNodeIPAddr,_A8:ctxClusterNodeClusterName,_R:ctxClusterNodeType,_AF:ctxClusterNodeOperState,'ctxSystemStatusObjects':ctxSystemStatusObjects,_U:ctxAdminServersStatus,_V:ctxCallEnginesStatus,_W:ctxDatabaseServersStatus,_X:ctxResourceStatus,_Y:ctxSystemConfigStatus,_Z:ctxSystemBackupStatus,'ctxStatisticsObjects':ctxStatisticsObjects,'ctxResourceStatsTable':ctxResourceStatsTable,'ctxResourceStatsEntry':ctxResourceStatsEntry,_AW:ctxResourceOperState,_AL:ctxResourceUnavailTrans,_AX:ctxResourceUnavailDuration,_AS:ctxResourceCallSetupFailures,'ctxAllocStatsTable':ctxAllocStatsTable,'ctxAllocStatsEntry':ctxAllocStatsEntry,_AM:ctxAllocActivePorts,_AN:ctxAllocAvailPorts,_AQ:ctxAllocFailures,_AU:ctxAllocOutOfPorts,'ctxRegionStatsTable':ctxRegionStatsTable,'ctxRegionStatsEntry':ctxRegionStatsEntry,_AT:ctxRegionCallSetupFailures,_AO:ctxAllocPoolActivePorts,_AP:ctxAllocPoolAvailPorts,_AR:ctxAllocPoolAllocFailures,_AV:ctxAllocPoolAllocOutOfPorts,'ctxAllocPeakHistory':ctxAllocPeakHistory,_AY:ctxPeakHistMaxIntervals,_AZ:ctxPeakHistIntTime,'ctxPeakHistAllocTable':ctxPeakHistAllocTable,'ctxPeakHistAllocEntry':ctxPeakHistAllocEntry,_l:ctxPeakHistAllocIntIndex,_Aa:ctxPeakHistAllocTS,_Ab:ctxPeakHistAllocPorts,'ctxPeakHistAllocPoolTable':ctxPeakHistAllocPoolTable,'ctxPeakHistAllocPoolEntry':ctxPeakHistAllocPoolEntry,_m:ctxPeakHistAllocPoolIntIndex,_Ac:ctxPeakHistAllocPoolTS,_Ad:ctxPeakHistAllocPoolPorts,'ctxEventHistory':ctxEventHistory,_Al:ctxErrorHistoryTableSize,_Am:ctxErrorHistoryMaxSeverity,_An:ctxErrorHistoryLastIndex,'ctxErrorHistoryTable':ctxErrorHistoryTable,'ctxErrorHistoryEntry':ctxErrorHistoryEntry,_n:ctxErrorIndex,_b:ctxErrorKey,_Ao:ctxErrorTimeStamp,_c:ctxErrorSeverity,_e:ctxErrorAppName,_f:ctxErrorAlarmId,_g:ctxErrorAttrValStr,_d:ctxErrorMessage,'ctxNotifyObjects':ctxNotifyObjects,_D:ctxNotifyMessage,'ctxNotifyConfigObjects':ctxNotifyConfigObjects,_Ae:ctxStatusChangeNotifyEnable,_Af:ctxLicenseAlarmNotifyEnable,_Ag:ctxAuthFailureNotifyEnable,_Ah:ctxClusterNodeAlarmNotifyEnable,_Ai:ctxResourceAlarmNotifyEnable,_Aj:ctxCallFailureNotifyEnable,_Ak:ctxErrorHistoryEventNotifyEnable,'ciscoTelepresenceExchangeSystemMIBConform':ciscoTelepresenceExchangeSystemMIBConform,'ciscoTelepresenceExchangeSystemMIBCompliances':ciscoTelepresenceExchangeSystemMIBCompliances,'ciscoTelepresenceExchangeSystemMIBModuleCompliance':ciscoTelepresenceExchangeSystemMIBModuleCompliance,'ciscoTelepresenceExchangeSystemMIBGroups':ciscoTelepresenceExchangeSystemMIBGroups,_B4:ciscoTelepresenceExchangeSystemMIBStatusGroup,_B5:ciscoTelepresenceExchangeSystemMIBConfigGroup,_B9:ciscoTelePresenceExchangeSystemMIBStatsGroup,_B6:ciscoTelepresenceExchangeSystemMIBNotfyObjectsGroup,_B8:ciscoTelepresenceExchangeSystemMIBErrorHistoryGroup,_B7:ciscoTelepresenceExchangeSystemMIBNotifyGroup})