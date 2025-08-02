_AZ='sipCommonStatsGroup'
_AY='sipCommonConfigGroup'
_AX='sipCommonStatusCodeThreshExceededOutNotif'
_AW='sipCommonStatusCodeThreshExceededInNotif'
_AV='sipCommonStatusCodeNotif'
_AU='sipCommonStatusCodeNotifInterval'
_AT='sipCommonStatusCodeNotifThresh'
_AS='sipCommonStatusCodeNotifEmitMode'
_AR='sipCommonStatusCodeNotifSend'
_AQ='sipCommonStatsRetryDisconTime'
_AP='sipCommonStatsRetryNonFinalResponses'
_AO='sipCommonStatsRetryFinalResponses'
_AN='sipCommonStatsRetries'
_AM='sipCommonOtherStatsDisconTime'
_AL='sipCommonOtherStatsOtherwiseDiscardedMsgs'
_AK='sipCommonOtherStatsNumUnsupportedMethods'
_AJ='sipCommonOtherStatsNumUnsupportedUris'
_AI='sipCommonTransCurrentactions'
_AH='sipCommonStatusCodeDisconTime'
_AG='sipCommonStatusCodeRowStatus'
_AF='sipCommonMethodStatsDisconTime'
_AE='sipCommonMethodStatsInbounds'
_AD='sipCommonMethodStatsOutbounds'
_AC='sipCommonSummaryDisconTime'
_AB='sipCommonSummaryTotalTransactions'
_AA='sipCommonSummaryOutResponses'
_A9='sipCommonSummaryInResponses'
_A8='sipCommonSummaryOutRequests'
_A7='sipCommonSummaryInRequests'
_A6='sipCommonCfgTimerT4'
_A5='sipCommonCfgTimerT2'
_A4='sipCommonCfgTimerT1'
_A3='sipCommonCfgTimerK'
_A2='sipCommonCfgTimerJ'
_A1='sipCommonCfgTimerI'
_A0='sipCommonCfgTimerH'
_z='sipCommonCfgTimerG'
_y='sipCommonCfgTimerF'
_x='sipCommonCfgTimerE'
_w='sipCommonCfgTimerD'
_v='sipCommonCfgTimerC'
_u='sipCommonCfgTimerB'
_t='sipCommonCfgTimerA'
_s='sipCommonCfgOrganization'
_r='sipCommonMethodSupportedName'
_q='sipCommonCfgEntityType'
_p='sipCommonCfgServiceNotifEnable'
_o='sipCommonCfgMaxTransactions'
_n='sipCommonOptionTagHeaderField'
_m='sipCommonOptionTag'
_l='sipCommonPortTransportRcv'
_k='sipCommonCfgProtocolVersion'
_j='sipCommonStatusCodeNotifEntry'
_i='sipCommonStatsRetryMethod'
_h='sipCommonStatusCodeValue'
_g='sipCommonStatusCodeMethod'
_f='sipCommonMethodStatsName'
_e='sipCommonMethodSupportedIndex'
_d='sipCommonOptionTagIndex'
_c='sipCommonPort'
_b='TruthValue'
_a='Gauge32'
_Z='InetPortNumber'
_Y='sipCommonStatusCodeNotifCSeq'
_X='sipCommonStatusCodeNotifCallId'
_W='sipCommonStatusCodeNotifFrom'
_V='sipCommonStatusCodeNotifTo'
_U='sipCommonCfgServiceStartTime'
_T='sipCommonCfgServiceOperStatus'
_S='sipCommonServiceStatusChanged'
_R='sipCommonServiceWarmStart'
_Q='sipCommonServiceColdStart'
_P='Integer32'
_O='sipCommonStatusCodeOuts'
_N='sipCommonStatusCodeIns'
_M='sipCommonCfgServiceLastChange'
_L='read-write'
_K='accessible-for-notify'
_J='not-accessible'
_I='sipCommonNotifSequenceNumber'
_H='sipCommonNotifApplIndex'
_G='applIndex'
_F='NETWORK-SERVICES-MIB'
_E='milliseconds'
_D='Unsigned32'
_C='read-only'
_B='SIP-COMMON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetPortNumber,=mibBuilder.importSymbols('INET-ADDRESS-MIB',_Z)
applIndex,=mibBuilder.importSymbols(_F,_G)
SipTCEntityRole,SipTCMethodName,SipTCOptionTagHeaders,SipTCTransportProtocol=mibBuilder.importSymbols('SIP-TC-MIB','SipTCEntityRole','SipTCMethodName','SipTCOptionTagHeaders','SipTCTransportProtocol')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_a,_P,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_b)
sipCommonMIB=ModuleIdentity((1,3,6,1,2,1,149))
if mibBuilder.loadTexts:sipCommonMIB.setRevisions(('2007-04-20 00:00',))
_SipCommonMIBNotifications_ObjectIdentity=ObjectIdentity
sipCommonMIBNotifications=_SipCommonMIBNotifications_ObjectIdentity((1,3,6,1,2,1,149,0))
_SipCommonMIBObjects_ObjectIdentity=ObjectIdentity
sipCommonMIBObjects=_SipCommonMIBObjects_ObjectIdentity((1,3,6,1,2,1,149,1))
_SipCommonCfgBase_ObjectIdentity=ObjectIdentity
sipCommonCfgBase=_SipCommonCfgBase_ObjectIdentity((1,3,6,1,2,1,149,1,1))
_SipCommonCfgTable_Object=MibTable
sipCommonCfgTable=_SipCommonCfgTable_Object((1,3,6,1,2,1,149,1,1,1))
if mibBuilder.loadTexts:sipCommonCfgTable.setStatus(_A)
_SipCommonCfgEntry_Object=MibTableRow
sipCommonCfgEntry=_SipCommonCfgEntry_Object((1,3,6,1,2,1,149,1,1,1,1))
sipCommonCfgEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:sipCommonCfgEntry.setStatus(_A)
_SipCommonCfgProtocolVersion_Type=SnmpAdminString
_SipCommonCfgProtocolVersion_Object=MibTableColumn
sipCommonCfgProtocolVersion=_SipCommonCfgProtocolVersion_Object((1,3,6,1,2,1,149,1,1,1,1,1),_SipCommonCfgProtocolVersion_Type())
sipCommonCfgProtocolVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgProtocolVersion.setStatus(_A)
class _SipCommonCfgServiceOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unknown',1),('up',2),('down',3),('congested',4),('restarting',5),('quiescing',6),('testing',7)))
_SipCommonCfgServiceOperStatus_Type.__name__=_P
_SipCommonCfgServiceOperStatus_Object=MibTableColumn
sipCommonCfgServiceOperStatus=_SipCommonCfgServiceOperStatus_Object((1,3,6,1,2,1,149,1,1,1,1,2),_SipCommonCfgServiceOperStatus_Type())
sipCommonCfgServiceOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgServiceOperStatus.setStatus(_A)
_SipCommonCfgServiceStartTime_Type=TimeTicks
_SipCommonCfgServiceStartTime_Object=MibTableColumn
sipCommonCfgServiceStartTime=_SipCommonCfgServiceStartTime_Object((1,3,6,1,2,1,149,1,1,1,1,3),_SipCommonCfgServiceStartTime_Type())
sipCommonCfgServiceStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgServiceStartTime.setStatus(_A)
_SipCommonCfgServiceLastChange_Type=TimeTicks
_SipCommonCfgServiceLastChange_Object=MibTableColumn
sipCommonCfgServiceLastChange=_SipCommonCfgServiceLastChange_Object((1,3,6,1,2,1,149,1,1,1,1,4),_SipCommonCfgServiceLastChange_Type())
sipCommonCfgServiceLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgServiceLastChange.setStatus(_A)
_SipCommonCfgOrganization_Type=SnmpAdminString
_SipCommonCfgOrganization_Object=MibTableColumn
sipCommonCfgOrganization=_SipCommonCfgOrganization_Object((1,3,6,1,2,1,149,1,1,1,1,5),_SipCommonCfgOrganization_Type())
sipCommonCfgOrganization.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgOrganization.setStatus(_A)
class _SipCommonCfgMaxTransactions_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_SipCommonCfgMaxTransactions_Type.__name__=_D
_SipCommonCfgMaxTransactions_Object=MibTableColumn
sipCommonCfgMaxTransactions=_SipCommonCfgMaxTransactions_Object((1,3,6,1,2,1,149,1,1,1,1,6),_SipCommonCfgMaxTransactions_Type())
sipCommonCfgMaxTransactions.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgMaxTransactions.setStatus(_A)
class _SipCommonCfgServiceNotifEnable_Type(Bits):defaultBinValue='11';namedValues=NamedValues(*((_Q,0),(_R,1),(_S,2)))
_SipCommonCfgServiceNotifEnable_Type.__name__='Bits'
_SipCommonCfgServiceNotifEnable_Object=MibTableColumn
sipCommonCfgServiceNotifEnable=_SipCommonCfgServiceNotifEnable_Object((1,3,6,1,2,1,149,1,1,1,1,7),_SipCommonCfgServiceNotifEnable_Type())
sipCommonCfgServiceNotifEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:sipCommonCfgServiceNotifEnable.setStatus(_A)
_SipCommonCfgEntityType_Type=SipTCEntityRole
_SipCommonCfgEntityType_Object=MibTableColumn
sipCommonCfgEntityType=_SipCommonCfgEntityType_Object((1,3,6,1,2,1,149,1,1,1,1,8),_SipCommonCfgEntityType_Type())
sipCommonCfgEntityType.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgEntityType.setStatus(_A)
_SipCommonPortTable_Object=MibTable
sipCommonPortTable=_SipCommonPortTable_Object((1,3,6,1,2,1,149,1,1,2))
if mibBuilder.loadTexts:sipCommonPortTable.setStatus(_A)
_SipCommonPortEntry_Object=MibTableRow
sipCommonPortEntry=_SipCommonPortEntry_Object((1,3,6,1,2,1,149,1,1,2,1))
sipCommonPortEntry.setIndexNames((0,_F,_G),(0,_B,_c))
if mibBuilder.loadTexts:sipCommonPortEntry.setStatus(_A)
class _SipCommonPort_Type(InetPortNumber):subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SipCommonPort_Type.__name__=_Z
_SipCommonPort_Object=MibTableColumn
sipCommonPort=_SipCommonPort_Object((1,3,6,1,2,1,149,1,1,2,1,1),_SipCommonPort_Type())
sipCommonPort.setMaxAccess(_J)
if mibBuilder.loadTexts:sipCommonPort.setStatus(_A)
_SipCommonPortTransportRcv_Type=SipTCTransportProtocol
_SipCommonPortTransportRcv_Object=MibTableColumn
sipCommonPortTransportRcv=_SipCommonPortTransportRcv_Object((1,3,6,1,2,1,149,1,1,2,1,2),_SipCommonPortTransportRcv_Type())
sipCommonPortTransportRcv.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonPortTransportRcv.setStatus(_A)
_SipCommonOptionTagTable_Object=MibTable
sipCommonOptionTagTable=_SipCommonOptionTagTable_Object((1,3,6,1,2,1,149,1,1,3))
if mibBuilder.loadTexts:sipCommonOptionTagTable.setStatus(_A)
_SipCommonOptionTagEntry_Object=MibTableRow
sipCommonOptionTagEntry=_SipCommonOptionTagEntry_Object((1,3,6,1,2,1,149,1,1,3,1))
sipCommonOptionTagEntry.setIndexNames((0,_F,_G),(0,_B,_d))
if mibBuilder.loadTexts:sipCommonOptionTagEntry.setStatus(_A)
class _SipCommonOptionTagIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_SipCommonOptionTagIndex_Type.__name__=_D
_SipCommonOptionTagIndex_Object=MibTableColumn
sipCommonOptionTagIndex=_SipCommonOptionTagIndex_Object((1,3,6,1,2,1,149,1,1,3,1,1),_SipCommonOptionTagIndex_Type())
sipCommonOptionTagIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:sipCommonOptionTagIndex.setStatus(_A)
_SipCommonOptionTag_Type=SnmpAdminString
_SipCommonOptionTag_Object=MibTableColumn
sipCommonOptionTag=_SipCommonOptionTag_Object((1,3,6,1,2,1,149,1,1,3,1,2),_SipCommonOptionTag_Type())
sipCommonOptionTag.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonOptionTag.setStatus(_A)
_SipCommonOptionTagHeaderField_Type=SipTCOptionTagHeaders
_SipCommonOptionTagHeaderField_Object=MibTableColumn
sipCommonOptionTagHeaderField=_SipCommonOptionTagHeaderField_Object((1,3,6,1,2,1,149,1,1,3,1,3),_SipCommonOptionTagHeaderField_Type())
sipCommonOptionTagHeaderField.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonOptionTagHeaderField.setStatus(_A)
_SipCommonMethodSupportedTable_Object=MibTable
sipCommonMethodSupportedTable=_SipCommonMethodSupportedTable_Object((1,3,6,1,2,1,149,1,1,4))
if mibBuilder.loadTexts:sipCommonMethodSupportedTable.setStatus(_A)
_SipCommonMethodSupportedEntry_Object=MibTableRow
sipCommonMethodSupportedEntry=_SipCommonMethodSupportedEntry_Object((1,3,6,1,2,1,149,1,1,4,1))
sipCommonMethodSupportedEntry.setIndexNames((0,_F,_G),(0,_B,_e))
if mibBuilder.loadTexts:sipCommonMethodSupportedEntry.setStatus(_A)
class _SipCommonMethodSupportedIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_SipCommonMethodSupportedIndex_Type.__name__=_D
_SipCommonMethodSupportedIndex_Object=MibTableColumn
sipCommonMethodSupportedIndex=_SipCommonMethodSupportedIndex_Object((1,3,6,1,2,1,149,1,1,4,1,1),_SipCommonMethodSupportedIndex_Type())
sipCommonMethodSupportedIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:sipCommonMethodSupportedIndex.setStatus(_A)
_SipCommonMethodSupportedName_Type=SipTCMethodName
_SipCommonMethodSupportedName_Object=MibTableColumn
sipCommonMethodSupportedName=_SipCommonMethodSupportedName_Object((1,3,6,1,2,1,149,1,1,4,1,2),_SipCommonMethodSupportedName_Type())
sipCommonMethodSupportedName.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonMethodSupportedName.setStatus(_A)
_SipCommonCfgTimer_ObjectIdentity=ObjectIdentity
sipCommonCfgTimer=_SipCommonCfgTimer_ObjectIdentity((1,3,6,1,2,1,149,1,2))
_SipCommonCfgTimerTable_Object=MibTable
sipCommonCfgTimerTable=_SipCommonCfgTimerTable_Object((1,3,6,1,2,1,149,1,2,1))
if mibBuilder.loadTexts:sipCommonCfgTimerTable.setStatus(_A)
_SipCommonCfgTimerEntry_Object=MibTableRow
sipCommonCfgTimerEntry=_SipCommonCfgTimerEntry_Object((1,3,6,1,2,1,149,1,2,1,1))
sipCommonCfgTimerEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:sipCommonCfgTimerEntry.setStatus(_A)
class _SipCommonCfgTimerA_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_SipCommonCfgTimerA_Type.__name__=_D
_SipCommonCfgTimerA_Object=MibTableColumn
sipCommonCfgTimerA=_SipCommonCfgTimerA_Object((1,3,6,1,2,1,149,1,2,1,1,1),_SipCommonCfgTimerA_Type())
sipCommonCfgTimerA.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgTimerA.setStatus(_A)
if mibBuilder.loadTexts:sipCommonCfgTimerA.setUnits(_E)
class _SipCommonCfgTimerB_Type(Unsigned32):defaultValue=32000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32000,300000))
_SipCommonCfgTimerB_Type.__name__=_D
_SipCommonCfgTimerB_Object=MibTableColumn
sipCommonCfgTimerB=_SipCommonCfgTimerB_Object((1,3,6,1,2,1,149,1,2,1,1,2),_SipCommonCfgTimerB_Type())
sipCommonCfgTimerB.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgTimerB.setStatus(_A)
if mibBuilder.loadTexts:sipCommonCfgTimerB.setUnits(_E)
class _SipCommonCfgTimerC_Type(Unsigned32):defaultValue=180000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(180000,300000))
_SipCommonCfgTimerC_Type.__name__=_D
_SipCommonCfgTimerC_Object=MibTableColumn
sipCommonCfgTimerC=_SipCommonCfgTimerC_Object((1,3,6,1,2,1,149,1,2,1,1,3),_SipCommonCfgTimerC_Type())
sipCommonCfgTimerC.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgTimerC.setStatus(_A)
if mibBuilder.loadTexts:sipCommonCfgTimerC.setUnits(_E)
class _SipCommonCfgTimerD_Type(Unsigned32):defaultValue=32000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300000))
_SipCommonCfgTimerD_Type.__name__=_D
_SipCommonCfgTimerD_Object=MibTableColumn
sipCommonCfgTimerD=_SipCommonCfgTimerD_Object((1,3,6,1,2,1,149,1,2,1,1,4),_SipCommonCfgTimerD_Type())
sipCommonCfgTimerD.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgTimerD.setStatus(_A)
if mibBuilder.loadTexts:sipCommonCfgTimerD.setUnits(_E)
class _SipCommonCfgTimerE_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_SipCommonCfgTimerE_Type.__name__=_D
_SipCommonCfgTimerE_Object=MibTableColumn
sipCommonCfgTimerE=_SipCommonCfgTimerE_Object((1,3,6,1,2,1,149,1,2,1,1,5),_SipCommonCfgTimerE_Type())
sipCommonCfgTimerE.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgTimerE.setStatus(_A)
if mibBuilder.loadTexts:sipCommonCfgTimerE.setUnits(_E)
class _SipCommonCfgTimerF_Type(Unsigned32):defaultValue=32000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32000,300000))
_SipCommonCfgTimerF_Type.__name__=_D
_SipCommonCfgTimerF_Object=MibTableColumn
sipCommonCfgTimerF=_SipCommonCfgTimerF_Object((1,3,6,1,2,1,149,1,2,1,1,6),_SipCommonCfgTimerF_Type())
sipCommonCfgTimerF.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgTimerF.setStatus(_A)
if mibBuilder.loadTexts:sipCommonCfgTimerF.setUnits(_E)
class _SipCommonCfgTimerG_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_SipCommonCfgTimerG_Type.__name__=_D
_SipCommonCfgTimerG_Object=MibTableColumn
sipCommonCfgTimerG=_SipCommonCfgTimerG_Object((1,3,6,1,2,1,149,1,2,1,1,7),_SipCommonCfgTimerG_Type())
sipCommonCfgTimerG.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgTimerG.setStatus(_A)
if mibBuilder.loadTexts:sipCommonCfgTimerG.setUnits(_E)
class _SipCommonCfgTimerH_Type(Unsigned32):defaultValue=32000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32000,300000))
_SipCommonCfgTimerH_Type.__name__=_D
_SipCommonCfgTimerH_Object=MibTableColumn
sipCommonCfgTimerH=_SipCommonCfgTimerH_Object((1,3,6,1,2,1,149,1,2,1,1,8),_SipCommonCfgTimerH_Type())
sipCommonCfgTimerH.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgTimerH.setStatus(_A)
if mibBuilder.loadTexts:sipCommonCfgTimerH.setUnits(_E)
class _SipCommonCfgTimerI_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_SipCommonCfgTimerI_Type.__name__=_D
_SipCommonCfgTimerI_Object=MibTableColumn
sipCommonCfgTimerI=_SipCommonCfgTimerI_Object((1,3,6,1,2,1,149,1,2,1,1,9),_SipCommonCfgTimerI_Type())
sipCommonCfgTimerI.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgTimerI.setStatus(_A)
if mibBuilder.loadTexts:sipCommonCfgTimerI.setUnits(_E)
class _SipCommonCfgTimerJ_Type(Unsigned32):defaultValue=32000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32000,300000))
_SipCommonCfgTimerJ_Type.__name__=_D
_SipCommonCfgTimerJ_Object=MibTableColumn
sipCommonCfgTimerJ=_SipCommonCfgTimerJ_Object((1,3,6,1,2,1,149,1,2,1,1,10),_SipCommonCfgTimerJ_Type())
sipCommonCfgTimerJ.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgTimerJ.setStatus(_A)
if mibBuilder.loadTexts:sipCommonCfgTimerJ.setUnits(_E)
class _SipCommonCfgTimerK_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_SipCommonCfgTimerK_Type.__name__=_D
_SipCommonCfgTimerK_Object=MibTableColumn
sipCommonCfgTimerK=_SipCommonCfgTimerK_Object((1,3,6,1,2,1,149,1,2,1,1,11),_SipCommonCfgTimerK_Type())
sipCommonCfgTimerK.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgTimerK.setStatus(_A)
if mibBuilder.loadTexts:sipCommonCfgTimerK.setUnits(_E)
class _SipCommonCfgTimerT1_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,10000))
_SipCommonCfgTimerT1_Type.__name__=_D
_SipCommonCfgTimerT1_Object=MibTableColumn
sipCommonCfgTimerT1=_SipCommonCfgTimerT1_Object((1,3,6,1,2,1,149,1,2,1,1,12),_SipCommonCfgTimerT1_Type())
sipCommonCfgTimerT1.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgTimerT1.setStatus(_A)
if mibBuilder.loadTexts:sipCommonCfgTimerT1.setUnits(_E)
class _SipCommonCfgTimerT2_Type(Unsigned32):defaultValue=4000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,10000))
_SipCommonCfgTimerT2_Type.__name__=_D
_SipCommonCfgTimerT2_Object=MibTableColumn
sipCommonCfgTimerT2=_SipCommonCfgTimerT2_Object((1,3,6,1,2,1,149,1,2,1,1,13),_SipCommonCfgTimerT2_Type())
sipCommonCfgTimerT2.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgTimerT2.setStatus(_A)
if mibBuilder.loadTexts:sipCommonCfgTimerT2.setUnits(_E)
class _SipCommonCfgTimerT4_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,10000))
_SipCommonCfgTimerT4_Type.__name__=_D
_SipCommonCfgTimerT4_Object=MibTableColumn
sipCommonCfgTimerT4=_SipCommonCfgTimerT4_Object((1,3,6,1,2,1,149,1,2,1,1,14),_SipCommonCfgTimerT4_Type())
sipCommonCfgTimerT4.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonCfgTimerT4.setStatus(_A)
if mibBuilder.loadTexts:sipCommonCfgTimerT4.setUnits(_E)
_SipCommonSummaryStats_ObjectIdentity=ObjectIdentity
sipCommonSummaryStats=_SipCommonSummaryStats_ObjectIdentity((1,3,6,1,2,1,149,1,3))
_SipCommonSummaryStatsTable_Object=MibTable
sipCommonSummaryStatsTable=_SipCommonSummaryStatsTable_Object((1,3,6,1,2,1,149,1,3,1))
if mibBuilder.loadTexts:sipCommonSummaryStatsTable.setStatus(_A)
_SipCommonSummaryStatsEntry_Object=MibTableRow
sipCommonSummaryStatsEntry=_SipCommonSummaryStatsEntry_Object((1,3,6,1,2,1,149,1,3,1,1))
sipCommonSummaryStatsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:sipCommonSummaryStatsEntry.setStatus(_A)
_SipCommonSummaryInRequests_Type=Counter32
_SipCommonSummaryInRequests_Object=MibTableColumn
sipCommonSummaryInRequests=_SipCommonSummaryInRequests_Object((1,3,6,1,2,1,149,1,3,1,1,1),_SipCommonSummaryInRequests_Type())
sipCommonSummaryInRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonSummaryInRequests.setStatus(_A)
_SipCommonSummaryOutRequests_Type=Counter32
_SipCommonSummaryOutRequests_Object=MibTableColumn
sipCommonSummaryOutRequests=_SipCommonSummaryOutRequests_Object((1,3,6,1,2,1,149,1,3,1,1,2),_SipCommonSummaryOutRequests_Type())
sipCommonSummaryOutRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonSummaryOutRequests.setStatus(_A)
_SipCommonSummaryInResponses_Type=Counter32
_SipCommonSummaryInResponses_Object=MibTableColumn
sipCommonSummaryInResponses=_SipCommonSummaryInResponses_Object((1,3,6,1,2,1,149,1,3,1,1,3),_SipCommonSummaryInResponses_Type())
sipCommonSummaryInResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonSummaryInResponses.setStatus(_A)
_SipCommonSummaryOutResponses_Type=Counter32
_SipCommonSummaryOutResponses_Object=MibTableColumn
sipCommonSummaryOutResponses=_SipCommonSummaryOutResponses_Object((1,3,6,1,2,1,149,1,3,1,1,4),_SipCommonSummaryOutResponses_Type())
sipCommonSummaryOutResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonSummaryOutResponses.setStatus(_A)
_SipCommonSummaryTotalTransactions_Type=Counter32
_SipCommonSummaryTotalTransactions_Object=MibTableColumn
sipCommonSummaryTotalTransactions=_SipCommonSummaryTotalTransactions_Object((1,3,6,1,2,1,149,1,3,1,1,5),_SipCommonSummaryTotalTransactions_Type())
sipCommonSummaryTotalTransactions.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonSummaryTotalTransactions.setStatus(_A)
_SipCommonSummaryDisconTime_Type=TimeStamp
_SipCommonSummaryDisconTime_Object=MibTableColumn
sipCommonSummaryDisconTime=_SipCommonSummaryDisconTime_Object((1,3,6,1,2,1,149,1,3,1,1,6),_SipCommonSummaryDisconTime_Type())
sipCommonSummaryDisconTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonSummaryDisconTime.setStatus(_A)
_SipCommonMethodStats_ObjectIdentity=ObjectIdentity
sipCommonMethodStats=_SipCommonMethodStats_ObjectIdentity((1,3,6,1,2,1,149,1,4))
_SipCommonMethodStatsTable_Object=MibTable
sipCommonMethodStatsTable=_SipCommonMethodStatsTable_Object((1,3,6,1,2,1,149,1,4,1))
if mibBuilder.loadTexts:sipCommonMethodStatsTable.setStatus(_A)
_SipCommonMethodStatsEntry_Object=MibTableRow
sipCommonMethodStatsEntry=_SipCommonMethodStatsEntry_Object((1,3,6,1,2,1,149,1,4,1,1))
sipCommonMethodStatsEntry.setIndexNames((0,_F,_G),(0,_B,_f))
if mibBuilder.loadTexts:sipCommonMethodStatsEntry.setStatus(_A)
_SipCommonMethodStatsName_Type=SipTCMethodName
_SipCommonMethodStatsName_Object=MibTableColumn
sipCommonMethodStatsName=_SipCommonMethodStatsName_Object((1,3,6,1,2,1,149,1,4,1,1,1),_SipCommonMethodStatsName_Type())
sipCommonMethodStatsName.setMaxAccess(_J)
if mibBuilder.loadTexts:sipCommonMethodStatsName.setStatus(_A)
_SipCommonMethodStatsOutbounds_Type=Counter32
_SipCommonMethodStatsOutbounds_Object=MibTableColumn
sipCommonMethodStatsOutbounds=_SipCommonMethodStatsOutbounds_Object((1,3,6,1,2,1,149,1,4,1,1,2),_SipCommonMethodStatsOutbounds_Type())
sipCommonMethodStatsOutbounds.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonMethodStatsOutbounds.setStatus(_A)
_SipCommonMethodStatsInbounds_Type=Counter32
_SipCommonMethodStatsInbounds_Object=MibTableColumn
sipCommonMethodStatsInbounds=_SipCommonMethodStatsInbounds_Object((1,3,6,1,2,1,149,1,4,1,1,3),_SipCommonMethodStatsInbounds_Type())
sipCommonMethodStatsInbounds.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonMethodStatsInbounds.setStatus(_A)
_SipCommonMethodStatsDisconTime_Type=TimeStamp
_SipCommonMethodStatsDisconTime_Object=MibTableColumn
sipCommonMethodStatsDisconTime=_SipCommonMethodStatsDisconTime_Object((1,3,6,1,2,1,149,1,4,1,1,4),_SipCommonMethodStatsDisconTime_Type())
sipCommonMethodStatsDisconTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonMethodStatsDisconTime.setStatus(_A)
_SipCommonStatusCode_ObjectIdentity=ObjectIdentity
sipCommonStatusCode=_SipCommonStatusCode_ObjectIdentity((1,3,6,1,2,1,149,1,5))
_SipCommonStatusCodeTable_Object=MibTable
sipCommonStatusCodeTable=_SipCommonStatusCodeTable_Object((1,3,6,1,2,1,149,1,5,1))
if mibBuilder.loadTexts:sipCommonStatusCodeTable.setStatus(_A)
_SipCommonStatusCodeEntry_Object=MibTableRow
sipCommonStatusCodeEntry=_SipCommonStatusCodeEntry_Object((1,3,6,1,2,1,149,1,5,1,1))
sipCommonStatusCodeEntry.setIndexNames((0,_F,_G),(0,_B,_g),(0,_B,_h))
if mibBuilder.loadTexts:sipCommonStatusCodeEntry.setStatus(_A)
_SipCommonStatusCodeMethod_Type=SipTCMethodName
_SipCommonStatusCodeMethod_Object=MibTableColumn
sipCommonStatusCodeMethod=_SipCommonStatusCodeMethod_Object((1,3,6,1,2,1,149,1,5,1,1,1),_SipCommonStatusCodeMethod_Type())
sipCommonStatusCodeMethod.setMaxAccess(_J)
if mibBuilder.loadTexts:sipCommonStatusCodeMethod.setStatus(_A)
class _SipCommonStatusCodeValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,999))
_SipCommonStatusCodeValue_Type.__name__=_D
_SipCommonStatusCodeValue_Object=MibTableColumn
sipCommonStatusCodeValue=_SipCommonStatusCodeValue_Object((1,3,6,1,2,1,149,1,5,1,1,2),_SipCommonStatusCodeValue_Type())
sipCommonStatusCodeValue.setMaxAccess(_J)
if mibBuilder.loadTexts:sipCommonStatusCodeValue.setStatus(_A)
_SipCommonStatusCodeIns_Type=Counter32
_SipCommonStatusCodeIns_Object=MibTableColumn
sipCommonStatusCodeIns=_SipCommonStatusCodeIns_Object((1,3,6,1,2,1,149,1,5,1,1,3),_SipCommonStatusCodeIns_Type())
sipCommonStatusCodeIns.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonStatusCodeIns.setStatus(_A)
_SipCommonStatusCodeOuts_Type=Counter32
_SipCommonStatusCodeOuts_Object=MibTableColumn
sipCommonStatusCodeOuts=_SipCommonStatusCodeOuts_Object((1,3,6,1,2,1,149,1,5,1,1,4),_SipCommonStatusCodeOuts_Type())
sipCommonStatusCodeOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonStatusCodeOuts.setStatus(_A)
_SipCommonStatusCodeRowStatus_Type=RowStatus
_SipCommonStatusCodeRowStatus_Object=MibTableColumn
sipCommonStatusCodeRowStatus=_SipCommonStatusCodeRowStatus_Object((1,3,6,1,2,1,149,1,5,1,1,5),_SipCommonStatusCodeRowStatus_Type())
sipCommonStatusCodeRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:sipCommonStatusCodeRowStatus.setStatus(_A)
_SipCommonStatusCodeDisconTime_Type=TimeStamp
_SipCommonStatusCodeDisconTime_Object=MibTableColumn
sipCommonStatusCodeDisconTime=_SipCommonStatusCodeDisconTime_Object((1,3,6,1,2,1,149,1,5,1,1,6),_SipCommonStatusCodeDisconTime_Type())
sipCommonStatusCodeDisconTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonStatusCodeDisconTime.setStatus(_A)
_SipCommonStatusCodeNotifTable_Object=MibTable
sipCommonStatusCodeNotifTable=_SipCommonStatusCodeNotifTable_Object((1,3,6,1,2,1,149,1,5,2))
if mibBuilder.loadTexts:sipCommonStatusCodeNotifTable.setStatus(_A)
_SipCommonStatusCodeNotifEntry_Object=MibTableRow
sipCommonStatusCodeNotifEntry=_SipCommonStatusCodeNotifEntry_Object((1,3,6,1,2,1,149,1,5,2,1))
if mibBuilder.loadTexts:sipCommonStatusCodeNotifEntry.setStatus(_A)
class _SipCommonStatusCodeNotifSend_Type(TruthValue):defaultValue=2
_SipCommonStatusCodeNotifSend_Type.__name__=_b
_SipCommonStatusCodeNotifSend_Object=MibTableColumn
sipCommonStatusCodeNotifSend=_SipCommonStatusCodeNotifSend_Object((1,3,6,1,2,1,149,1,5,2,1,1),_SipCommonStatusCodeNotifSend_Type())
sipCommonStatusCodeNotifSend.setMaxAccess(_L)
if mibBuilder.loadTexts:sipCommonStatusCodeNotifSend.setStatus(_A)
class _SipCommonStatusCodeNotifEmitMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('oneShot',2),('triggered',3)))
_SipCommonStatusCodeNotifEmitMode_Type.__name__=_P
_SipCommonStatusCodeNotifEmitMode_Object=MibTableColumn
sipCommonStatusCodeNotifEmitMode=_SipCommonStatusCodeNotifEmitMode_Object((1,3,6,1,2,1,149,1,5,2,1,2),_SipCommonStatusCodeNotifEmitMode_Type())
sipCommonStatusCodeNotifEmitMode.setMaxAccess(_L)
if mibBuilder.loadTexts:sipCommonStatusCodeNotifEmitMode.setStatus(_A)
class _SipCommonStatusCodeNotifThresh_Type(Unsigned32):defaultValue=500
_SipCommonStatusCodeNotifThresh_Type.__name__=_D
_SipCommonStatusCodeNotifThresh_Object=MibTableColumn
sipCommonStatusCodeNotifThresh=_SipCommonStatusCodeNotifThresh_Object((1,3,6,1,2,1,149,1,5,2,1,3),_SipCommonStatusCodeNotifThresh_Type())
sipCommonStatusCodeNotifThresh.setMaxAccess(_L)
if mibBuilder.loadTexts:sipCommonStatusCodeNotifThresh.setStatus(_A)
class _SipCommonStatusCodeNotifInterval_Type(Unsigned32):defaultValue=60
_SipCommonStatusCodeNotifInterval_Type.__name__=_D
_SipCommonStatusCodeNotifInterval_Object=MibTableColumn
sipCommonStatusCodeNotifInterval=_SipCommonStatusCodeNotifInterval_Object((1,3,6,1,2,1,149,1,5,2,1,4),_SipCommonStatusCodeNotifInterval_Type())
sipCommonStatusCodeNotifInterval.setMaxAccess(_L)
if mibBuilder.loadTexts:sipCommonStatusCodeNotifInterval.setStatus(_A)
if mibBuilder.loadTexts:sipCommonStatusCodeNotifInterval.setUnits('seconds')
_SipCommonStatsTrans_ObjectIdentity=ObjectIdentity
sipCommonStatsTrans=_SipCommonStatsTrans_ObjectIdentity((1,3,6,1,2,1,149,1,6))
_SipCommonTransCurrentTable_Object=MibTable
sipCommonTransCurrentTable=_SipCommonTransCurrentTable_Object((1,3,6,1,2,1,149,1,6,1))
if mibBuilder.loadTexts:sipCommonTransCurrentTable.setStatus(_A)
_SipCommonTransCurrentEntry_Object=MibTableRow
sipCommonTransCurrentEntry=_SipCommonTransCurrentEntry_Object((1,3,6,1,2,1,149,1,6,1,1))
sipCommonTransCurrentEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:sipCommonTransCurrentEntry.setStatus(_A)
class _SipCommonTransCurrentactions_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_SipCommonTransCurrentactions_Type.__name__=_a
_SipCommonTransCurrentactions_Object=MibTableColumn
sipCommonTransCurrentactions=_SipCommonTransCurrentactions_Object((1,3,6,1,2,1,149,1,6,1,1,1),_SipCommonTransCurrentactions_Type())
sipCommonTransCurrentactions.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonTransCurrentactions.setStatus(_A)
_SipCommonStatsRetry_ObjectIdentity=ObjectIdentity
sipCommonStatsRetry=_SipCommonStatsRetry_ObjectIdentity((1,3,6,1,2,1,149,1,7))
_SipCommonStatsRetryTable_Object=MibTable
sipCommonStatsRetryTable=_SipCommonStatsRetryTable_Object((1,3,6,1,2,1,149,1,7,1))
if mibBuilder.loadTexts:sipCommonStatsRetryTable.setStatus(_A)
_SipCommonStatsRetryEntry_Object=MibTableRow
sipCommonStatsRetryEntry=_SipCommonStatsRetryEntry_Object((1,3,6,1,2,1,149,1,7,1,1))
sipCommonStatsRetryEntry.setIndexNames((0,_F,_G),(0,_B,_i))
if mibBuilder.loadTexts:sipCommonStatsRetryEntry.setStatus(_A)
_SipCommonStatsRetryMethod_Type=SipTCMethodName
_SipCommonStatsRetryMethod_Object=MibTableColumn
sipCommonStatsRetryMethod=_SipCommonStatsRetryMethod_Object((1,3,6,1,2,1,149,1,7,1,1,1),_SipCommonStatsRetryMethod_Type())
sipCommonStatsRetryMethod.setMaxAccess(_J)
if mibBuilder.loadTexts:sipCommonStatsRetryMethod.setStatus(_A)
_SipCommonStatsRetries_Type=Counter32
_SipCommonStatsRetries_Object=MibTableColumn
sipCommonStatsRetries=_SipCommonStatsRetries_Object((1,3,6,1,2,1,149,1,7,1,1,2),_SipCommonStatsRetries_Type())
sipCommonStatsRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonStatsRetries.setStatus(_A)
_SipCommonStatsRetryFinalResponses_Type=Counter32
_SipCommonStatsRetryFinalResponses_Object=MibTableColumn
sipCommonStatsRetryFinalResponses=_SipCommonStatsRetryFinalResponses_Object((1,3,6,1,2,1,149,1,7,1,1,3),_SipCommonStatsRetryFinalResponses_Type())
sipCommonStatsRetryFinalResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonStatsRetryFinalResponses.setStatus(_A)
_SipCommonStatsRetryNonFinalResponses_Type=Counter32
_SipCommonStatsRetryNonFinalResponses_Object=MibTableColumn
sipCommonStatsRetryNonFinalResponses=_SipCommonStatsRetryNonFinalResponses_Object((1,3,6,1,2,1,149,1,7,1,1,4),_SipCommonStatsRetryNonFinalResponses_Type())
sipCommonStatsRetryNonFinalResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonStatsRetryNonFinalResponses.setStatus(_A)
_SipCommonStatsRetryDisconTime_Type=TimeStamp
_SipCommonStatsRetryDisconTime_Object=MibTableColumn
sipCommonStatsRetryDisconTime=_SipCommonStatsRetryDisconTime_Object((1,3,6,1,2,1,149,1,7,1,1,5),_SipCommonStatsRetryDisconTime_Type())
sipCommonStatsRetryDisconTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonStatsRetryDisconTime.setStatus(_A)
_SipCommonOtherStats_ObjectIdentity=ObjectIdentity
sipCommonOtherStats=_SipCommonOtherStats_ObjectIdentity((1,3,6,1,2,1,149,1,8))
_SipCommonOtherStatsTable_Object=MibTable
sipCommonOtherStatsTable=_SipCommonOtherStatsTable_Object((1,3,6,1,2,1,149,1,8,1))
if mibBuilder.loadTexts:sipCommonOtherStatsTable.setStatus(_A)
_SipCommonOtherStatsEntry_Object=MibTableRow
sipCommonOtherStatsEntry=_SipCommonOtherStatsEntry_Object((1,3,6,1,2,1,149,1,8,1,1))
sipCommonOtherStatsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:sipCommonOtherStatsEntry.setStatus(_A)
_SipCommonOtherStatsNumUnsupportedUris_Type=Counter32
_SipCommonOtherStatsNumUnsupportedUris_Object=MibTableColumn
sipCommonOtherStatsNumUnsupportedUris=_SipCommonOtherStatsNumUnsupportedUris_Object((1,3,6,1,2,1,149,1,8,1,1,1),_SipCommonOtherStatsNumUnsupportedUris_Type())
sipCommonOtherStatsNumUnsupportedUris.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonOtherStatsNumUnsupportedUris.setStatus(_A)
_SipCommonOtherStatsNumUnsupportedMethods_Type=Counter32
_SipCommonOtherStatsNumUnsupportedMethods_Object=MibTableColumn
sipCommonOtherStatsNumUnsupportedMethods=_SipCommonOtherStatsNumUnsupportedMethods_Object((1,3,6,1,2,1,149,1,8,1,1,2),_SipCommonOtherStatsNumUnsupportedMethods_Type())
sipCommonOtherStatsNumUnsupportedMethods.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonOtherStatsNumUnsupportedMethods.setStatus(_A)
_SipCommonOtherStatsOtherwiseDiscardedMsgs_Type=Counter32
_SipCommonOtherStatsOtherwiseDiscardedMsgs_Object=MibTableColumn
sipCommonOtherStatsOtherwiseDiscardedMsgs=_SipCommonOtherStatsOtherwiseDiscardedMsgs_Object((1,3,6,1,2,1,149,1,8,1,1,3),_SipCommonOtherStatsOtherwiseDiscardedMsgs_Type())
sipCommonOtherStatsOtherwiseDiscardedMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonOtherStatsOtherwiseDiscardedMsgs.setStatus(_A)
_SipCommonOtherStatsDisconTime_Type=TimeStamp
_SipCommonOtherStatsDisconTime_Object=MibTableColumn
sipCommonOtherStatsDisconTime=_SipCommonOtherStatsDisconTime_Object((1,3,6,1,2,1,149,1,8,1,1,4),_SipCommonOtherStatsDisconTime_Type())
sipCommonOtherStatsDisconTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCommonOtherStatsDisconTime.setStatus(_A)
_SipCommonNotifObjects_ObjectIdentity=ObjectIdentity
sipCommonNotifObjects=_SipCommonNotifObjects_ObjectIdentity((1,3,6,1,2,1,149,1,9))
_SipCommonStatusCodeNotifTo_Type=SnmpAdminString
_SipCommonStatusCodeNotifTo_Object=MibScalar
sipCommonStatusCodeNotifTo=_SipCommonStatusCodeNotifTo_Object((1,3,6,1,2,1,149,1,9,1),_SipCommonStatusCodeNotifTo_Type())
sipCommonStatusCodeNotifTo.setMaxAccess(_K)
if mibBuilder.loadTexts:sipCommonStatusCodeNotifTo.setStatus(_A)
_SipCommonStatusCodeNotifFrom_Type=SnmpAdminString
_SipCommonStatusCodeNotifFrom_Object=MibScalar
sipCommonStatusCodeNotifFrom=_SipCommonStatusCodeNotifFrom_Object((1,3,6,1,2,1,149,1,9,2),_SipCommonStatusCodeNotifFrom_Type())
sipCommonStatusCodeNotifFrom.setMaxAccess(_K)
if mibBuilder.loadTexts:sipCommonStatusCodeNotifFrom.setStatus(_A)
_SipCommonStatusCodeNotifCallId_Type=SnmpAdminString
_SipCommonStatusCodeNotifCallId_Object=MibScalar
sipCommonStatusCodeNotifCallId=_SipCommonStatusCodeNotifCallId_Object((1,3,6,1,2,1,149,1,9,3),_SipCommonStatusCodeNotifCallId_Type())
sipCommonStatusCodeNotifCallId.setMaxAccess(_K)
if mibBuilder.loadTexts:sipCommonStatusCodeNotifCallId.setStatus(_A)
_SipCommonStatusCodeNotifCSeq_Type=Unsigned32
_SipCommonStatusCodeNotifCSeq_Object=MibScalar
sipCommonStatusCodeNotifCSeq=_SipCommonStatusCodeNotifCSeq_Object((1,3,6,1,2,1,149,1,9,4),_SipCommonStatusCodeNotifCSeq_Type())
sipCommonStatusCodeNotifCSeq.setMaxAccess(_K)
if mibBuilder.loadTexts:sipCommonStatusCodeNotifCSeq.setStatus(_A)
class _SipCommonNotifApplIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SipCommonNotifApplIndex_Type.__name__=_D
_SipCommonNotifApplIndex_Object=MibScalar
sipCommonNotifApplIndex=_SipCommonNotifApplIndex_Object((1,3,6,1,2,1,149,1,9,5),_SipCommonNotifApplIndex_Type())
sipCommonNotifApplIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:sipCommonNotifApplIndex.setStatus(_A)
class _SipCommonNotifSequenceNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SipCommonNotifSequenceNumber_Type.__name__=_D
_SipCommonNotifSequenceNumber_Object=MibScalar
sipCommonNotifSequenceNumber=_SipCommonNotifSequenceNumber_Object((1,3,6,1,2,1,149,1,9,6),_SipCommonNotifSequenceNumber_Type())
sipCommonNotifSequenceNumber.setMaxAccess(_K)
if mibBuilder.loadTexts:sipCommonNotifSequenceNumber.setStatus(_A)
_SipCommonMIBConformance_ObjectIdentity=ObjectIdentity
sipCommonMIBConformance=_SipCommonMIBConformance_ObjectIdentity((1,3,6,1,2,1,149,2))
_SipCommonMIBCompliances_ObjectIdentity=ObjectIdentity
sipCommonMIBCompliances=_SipCommonMIBCompliances_ObjectIdentity((1,3,6,1,2,1,149,2,1))
_SipCommonMIBGroups_ObjectIdentity=ObjectIdentity
sipCommonMIBGroups=_SipCommonMIBGroups_ObjectIdentity((1,3,6,1,2,1,149,2,2))
sipCommonStatusCodeEntry.registerAugmentions((_B,_j))
sipCommonStatusCodeNotifEntry.setIndexNames(*sipCommonStatusCodeEntry.getIndexNames())
sipCommonConfigGroup=ObjectGroup((1,3,6,1,2,1,149,2,2,1))
sipCommonConfigGroup.setObjects(*((_B,_k),(_B,_T),(_B,_U),(_B,_M),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:sipCommonConfigGroup.setStatus(_A)
sipCommonInformationalGroup=ObjectGroup((1,3,6,1,2,1,149,2,2,2))
sipCommonInformationalGroup.setObjects((_B,_s))
if mibBuilder.loadTexts:sipCommonInformationalGroup.setStatus(_A)
sipCommonConfigTimerGroup=ObjectGroup((1,3,6,1,2,1,149,2,2,3))
sipCommonConfigTimerGroup.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:sipCommonConfigTimerGroup.setStatus(_A)
sipCommonStatsGroup=ObjectGroup((1,3,6,1,2,1,149,2,2,4))
sipCommonStatsGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_N),(_B,_O),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:sipCommonStatsGroup.setStatus(_A)
sipCommonStatsRetryGroup=ObjectGroup((1,3,6,1,2,1,149,2,2,5))
sipCommonStatsRetryGroup.setObjects(*((_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ)))
if mibBuilder.loadTexts:sipCommonStatsRetryGroup.setStatus(_A)
sipCommonStatusCodeNotifGroup=ObjectGroup((1,3,6,1,2,1,149,2,2,7))
sipCommonStatusCodeNotifGroup.setObjects(*((_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU)))
if mibBuilder.loadTexts:sipCommonStatusCodeNotifGroup.setStatus(_A)
sipCommonNotifObjectsGroup=ObjectGroup((1,3,6,1,2,1,149,2,2,8))
sipCommonNotifObjectsGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:sipCommonNotifObjectsGroup.setStatus(_A)
sipCommonStatusCodeNotif=NotificationType((1,3,6,1,2,1,149,0,1))
sipCommonStatusCodeNotif.setObjects(*((_B,_I),(_B,_H),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:sipCommonStatusCodeNotif.setStatus(_A)
sipCommonStatusCodeThreshExceededInNotif=NotificationType((1,3,6,1,2,1,149,0,2))
sipCommonStatusCodeThreshExceededInNotif.setObjects(*((_B,_I),(_B,_H),(_B,_N)))
if mibBuilder.loadTexts:sipCommonStatusCodeThreshExceededInNotif.setStatus(_A)
sipCommonStatusCodeThreshExceededOutNotif=NotificationType((1,3,6,1,2,1,149,0,3))
sipCommonStatusCodeThreshExceededOutNotif.setObjects(*((_B,_I),(_B,_H),(_B,_O)))
if mibBuilder.loadTexts:sipCommonStatusCodeThreshExceededOutNotif.setStatus(_A)
sipCommonServiceColdStart=NotificationType((1,3,6,1,2,1,149,0,4))
sipCommonServiceColdStart.setObjects(*((_B,_I),(_B,_H),(_B,_U)))
if mibBuilder.loadTexts:sipCommonServiceColdStart.setStatus(_A)
sipCommonServiceWarmStart=NotificationType((1,3,6,1,2,1,149,0,5))
sipCommonServiceWarmStart.setObjects(*((_B,_I),(_B,_H),(_B,_M)))
if mibBuilder.loadTexts:sipCommonServiceWarmStart.setStatus(_A)
sipCommonServiceStatusChanged=NotificationType((1,3,6,1,2,1,149,0,6))
sipCommonServiceStatusChanged.setObjects(*((_B,_I),(_B,_H),(_B,_M),(_B,_T)))
if mibBuilder.loadTexts:sipCommonServiceStatusChanged.setStatus(_A)
sipCommonNotifGroup=NotificationGroup((1,3,6,1,2,1,149,2,2,6))
sipCommonNotifGroup.setObjects(*((_B,_AV),(_B,_AW),(_B,_AX),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:sipCommonNotifGroup.setStatus(_A)
sipCommonCompliance=ModuleCompliance((1,3,6,1,2,1,149,2,1,1))
sipCommonCompliance.setObjects(*((_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:sipCommonCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'sipCommonMIB':sipCommonMIB,'sipCommonMIBNotifications':sipCommonMIBNotifications,_AV:sipCommonStatusCodeNotif,_AW:sipCommonStatusCodeThreshExceededInNotif,_AX:sipCommonStatusCodeThreshExceededOutNotif,_Q:sipCommonServiceColdStart,_R:sipCommonServiceWarmStart,_S:sipCommonServiceStatusChanged,'sipCommonMIBObjects':sipCommonMIBObjects,'sipCommonCfgBase':sipCommonCfgBase,'sipCommonCfgTable':sipCommonCfgTable,'sipCommonCfgEntry':sipCommonCfgEntry,_k:sipCommonCfgProtocolVersion,_T:sipCommonCfgServiceOperStatus,_U:sipCommonCfgServiceStartTime,_M:sipCommonCfgServiceLastChange,_s:sipCommonCfgOrganization,_o:sipCommonCfgMaxTransactions,_p:sipCommonCfgServiceNotifEnable,_q:sipCommonCfgEntityType,'sipCommonPortTable':sipCommonPortTable,'sipCommonPortEntry':sipCommonPortEntry,_c:sipCommonPort,_l:sipCommonPortTransportRcv,'sipCommonOptionTagTable':sipCommonOptionTagTable,'sipCommonOptionTagEntry':sipCommonOptionTagEntry,_d:sipCommonOptionTagIndex,_m:sipCommonOptionTag,_n:sipCommonOptionTagHeaderField,'sipCommonMethodSupportedTable':sipCommonMethodSupportedTable,'sipCommonMethodSupportedEntry':sipCommonMethodSupportedEntry,_e:sipCommonMethodSupportedIndex,_r:sipCommonMethodSupportedName,'sipCommonCfgTimer':sipCommonCfgTimer,'sipCommonCfgTimerTable':sipCommonCfgTimerTable,'sipCommonCfgTimerEntry':sipCommonCfgTimerEntry,_t:sipCommonCfgTimerA,_u:sipCommonCfgTimerB,_v:sipCommonCfgTimerC,_w:sipCommonCfgTimerD,_x:sipCommonCfgTimerE,_y:sipCommonCfgTimerF,_z:sipCommonCfgTimerG,_A0:sipCommonCfgTimerH,_A1:sipCommonCfgTimerI,_A2:sipCommonCfgTimerJ,_A3:sipCommonCfgTimerK,_A4:sipCommonCfgTimerT1,_A5:sipCommonCfgTimerT2,_A6:sipCommonCfgTimerT4,'sipCommonSummaryStats':sipCommonSummaryStats,'sipCommonSummaryStatsTable':sipCommonSummaryStatsTable,'sipCommonSummaryStatsEntry':sipCommonSummaryStatsEntry,_A7:sipCommonSummaryInRequests,_A8:sipCommonSummaryOutRequests,_A9:sipCommonSummaryInResponses,_AA:sipCommonSummaryOutResponses,_AB:sipCommonSummaryTotalTransactions,_AC:sipCommonSummaryDisconTime,'sipCommonMethodStats':sipCommonMethodStats,'sipCommonMethodStatsTable':sipCommonMethodStatsTable,'sipCommonMethodStatsEntry':sipCommonMethodStatsEntry,_f:sipCommonMethodStatsName,_AD:sipCommonMethodStatsOutbounds,_AE:sipCommonMethodStatsInbounds,_AF:sipCommonMethodStatsDisconTime,'sipCommonStatusCode':sipCommonStatusCode,'sipCommonStatusCodeTable':sipCommonStatusCodeTable,'sipCommonStatusCodeEntry':sipCommonStatusCodeEntry,_g:sipCommonStatusCodeMethod,_h:sipCommonStatusCodeValue,_N:sipCommonStatusCodeIns,_O:sipCommonStatusCodeOuts,_AG:sipCommonStatusCodeRowStatus,_AH:sipCommonStatusCodeDisconTime,'sipCommonStatusCodeNotifTable':sipCommonStatusCodeNotifTable,_j:sipCommonStatusCodeNotifEntry,_AR:sipCommonStatusCodeNotifSend,_AS:sipCommonStatusCodeNotifEmitMode,_AT:sipCommonStatusCodeNotifThresh,_AU:sipCommonStatusCodeNotifInterval,'sipCommonStatsTrans':sipCommonStatsTrans,'sipCommonTransCurrentTable':sipCommonTransCurrentTable,'sipCommonTransCurrentEntry':sipCommonTransCurrentEntry,_AI:sipCommonTransCurrentactions,'sipCommonStatsRetry':sipCommonStatsRetry,'sipCommonStatsRetryTable':sipCommonStatsRetryTable,'sipCommonStatsRetryEntry':sipCommonStatsRetryEntry,_i:sipCommonStatsRetryMethod,_AN:sipCommonStatsRetries,_AO:sipCommonStatsRetryFinalResponses,_AP:sipCommonStatsRetryNonFinalResponses,_AQ:sipCommonStatsRetryDisconTime,'sipCommonOtherStats':sipCommonOtherStats,'sipCommonOtherStatsTable':sipCommonOtherStatsTable,'sipCommonOtherStatsEntry':sipCommonOtherStatsEntry,_AJ:sipCommonOtherStatsNumUnsupportedUris,_AK:sipCommonOtherStatsNumUnsupportedMethods,_AL:sipCommonOtherStatsOtherwiseDiscardedMsgs,_AM:sipCommonOtherStatsDisconTime,'sipCommonNotifObjects':sipCommonNotifObjects,_V:sipCommonStatusCodeNotifTo,_W:sipCommonStatusCodeNotifFrom,_X:sipCommonStatusCodeNotifCallId,_Y:sipCommonStatusCodeNotifCSeq,_H:sipCommonNotifApplIndex,_I:sipCommonNotifSequenceNumber,'sipCommonMIBConformance':sipCommonMIBConformance,'sipCommonMIBCompliances':sipCommonMIBCompliances,'sipCommonCompliance':sipCommonCompliance,'sipCommonMIBGroups':sipCommonMIBGroups,_AY:sipCommonConfigGroup,'sipCommonInformationalGroup':sipCommonInformationalGroup,'sipCommonConfigTimerGroup':sipCommonConfigTimerGroup,_AZ:sipCommonStatsGroup,'sipCommonStatsRetryGroup':sipCommonStatsRetryGroup,'sipCommonNotifGroup':sipCommonNotifGroup,'sipCommonStatusCodeNotifGroup':sipCommonStatusCodeNotifGroup,'sipCommonNotifObjectsGroup':sipCommonNotifObjectsGroup})