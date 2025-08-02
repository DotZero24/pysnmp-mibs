_Aa='ipoaLisTableGroup'
_AZ='ipoaLisNotificationsGroup'
_AY='ipoaSrvrNotificationsGroup'
_AX='ipoaSrvrGroup'
_AW='ipoaClientGroup'
_AV='ipoaBasicNotificationsGroup'
_AU='ipoaGeneralGroup'
_AT='ipoaLisDelete'
_AS='ipoaLisCreate'
_AR='ipoaDuplicateIpAddress'
_AQ='ipoaMtuExceeded'
_AP='ipoaArpRemoteSrvrOperStatus'
_AO='ipoaArpRemoteSrvrAdminStatus'
_AN='ipoaArpRemoteSrvrIpAddr'
_AM='ipoaArpRemoteSrvrRowStatus'
_AL='ipoaLisIfMappingRowStatus'
_AK='ipoaLisRowStatus'
_AJ='ipoaLisActiveVcs'
_AI='ipoaLisDefaultPeakCellRate'
_AH='ipoaLisTimeout'
_AG='ipoaLisRetries'
_AF='ipoaLisCacheEntryAge'
_AE='ipoaLisMaxCalls'
_AD='ipoaLisQDepth'
_AC='ipoaLisMinHoldingTime'
_AB='ipoaLisInactivityTimer'
_AA='ipoaLisDefaultEncapsType'
_A9='ipoaLisDefaultMtu'
_A8='ipoaLisTrapEnable'
_A7='ipoaArpSrvrRowStatus'
_A6='ipoaArpSrvrArpUnknownOps'
_A5='ipoaArpSrvrArpDupIpAddrs'
_A4='ipoaArpSrvrArpOutNaks'
_A3='ipoaArpSrvrArpOutReplies'
_A2='ipoaArpSrvrArpInReqs'
_A1='ipoaArpSrvrInArpInvalidOutReqs'
_A0='ipoaArpSrvrInArpInvalidInReqs'
_z='ipoaArpSrvrInArpOutReplies'
_y='ipoaArpSrvrInArpInReplies'
_x='ipoaArpSrvrInArpOutReqs'
_w='ipoaArpSrvrInArpInReqs'
_v='ipoaArpSrvrLis'
_u='ipoaArpClientRowStatus'
_t='ipoaArpClientArpNoSrvrResps'
_s='ipoaArpClientArpUnknownOps'
_r='ipoaArpClientArpOutNaks'
_q='ipoaArpClientArpInNaks'
_p='ipoaArpClientArpOutReplies'
_o='ipoaArpClientArpInReplies'
_n='ipoaArpClientArpOutReqs'
_m='ipoaArpClientArpInReqs'
_l='ipoaArpClientInArpInvalidOutReqs'
_k='ipoaArpClientInArpInvalidInReqs'
_j='ipoaArpClientInArpOutReplies'
_i='ipoaArpClientInArpInReplies'
_h='ipoaArpClientInArpOutReqs'
_g='ipoaArpClientInArpInReqs'
_f='ipoaArpClientSrvrInUse'
_e='ipoaArpClientAtmAddr'
_d='ipoaConfigPvcRowStatus'
_c='ipoaConfigPvcDefaultMtu'
_b='ipoaVcNegotiatedEncapsType'
_a='ipoaVcType'
_Z='ipoaConfigPvcVci'
_Y='ipoaConfigPvcVpi'
_X='ipoaConfigPvcIfIndex'
_W='ipoaVcVci'
_V='ipoaVcVpi'
_U='ipoaArpRemoteSrvrIfIndex'
_T='ipoaArpRemoteSrvrAtmAddr'
_S='ipoaArpSrvrAddr'
_R='IpoaAtmAddr'
_Q='ipoaLisIfMappingIfIndex'
_P='IpoaEncapsType'
_O='IpAddress'
_N='ipoaVcNegotiatedMtu'
_M='ipNetToMediaPhysAddress'
_L='ipNetToMediaNetAddress'
_K='ipNetToMediaIfIndex'
_J='ipAdEntAddr'
_I='seconds'
_H='ipoaLisSubnetAddr'
_G='not-accessible'
_F='IP-MIB'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='IPOA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
ipAdEntAddr,ipNetToMediaIfIndex,ipNetToMediaNetAddress,ipNetToMediaPhysAddress=mibBuilder.importSymbols(_F,_J,_K,_L,_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,_O,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ipoaMIB=ModuleIdentity((1,3,6,1,2,1,10,46))
class IpoaEncapsType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('llcSnap',1),('vcMuxed',2),('other',3)))
class IpoaVpiInteger(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class IpoaVciInteger(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class IpoaAtmAddr(TextualConvention,OctetString):status=_A;displayHint='1x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
class IpoaAtmConnKind(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('pvc',1),('svcIncoming',2),('svcOutgoing',3),('spvcInitiator',4),('spvcTarget',5)))
_IpoaObjects_ObjectIdentity=ObjectIdentity
ipoaObjects=_IpoaObjects_ObjectIdentity((1,3,6,1,2,1,10,46,1))
class _IpoaLisTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_IpoaLisTrapEnable_Type.__name__=_E
_IpoaLisTrapEnable_Object=MibScalar
ipoaLisTrapEnable=_IpoaLisTrapEnable_Object((1,3,6,1,2,1,10,46,1,1),_IpoaLisTrapEnable_Type())
ipoaLisTrapEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:ipoaLisTrapEnable.setStatus(_A)
_IpoaLisTable_Object=MibTable
ipoaLisTable=_IpoaLisTable_Object((1,3,6,1,2,1,10,46,1,2))
if mibBuilder.loadTexts:ipoaLisTable.setStatus(_A)
_IpoaLisEntry_Object=MibTableRow
ipoaLisEntry=_IpoaLisEntry_Object((1,3,6,1,2,1,10,46,1,2,1))
ipoaLisEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:ipoaLisEntry.setStatus(_A)
_IpoaLisSubnetAddr_Type=IpAddress
_IpoaLisSubnetAddr_Object=MibTableColumn
ipoaLisSubnetAddr=_IpoaLisSubnetAddr_Object((1,3,6,1,2,1,10,46,1,2,1,1),_IpoaLisSubnetAddr_Type())
ipoaLisSubnetAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaLisSubnetAddr.setStatus(_A)
class _IpoaLisDefaultMtu_Type(Integer32):defaultValue=9180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpoaLisDefaultMtu_Type.__name__=_E
_IpoaLisDefaultMtu_Object=MibTableColumn
ipoaLisDefaultMtu=_IpoaLisDefaultMtu_Object((1,3,6,1,2,1,10,46,1,2,1,2),_IpoaLisDefaultMtu_Type())
ipoaLisDefaultMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaLisDefaultMtu.setStatus(_A)
class _IpoaLisDefaultEncapsType_Type(IpoaEncapsType):defaultValue=1
_IpoaLisDefaultEncapsType_Type.__name__=_P
_IpoaLisDefaultEncapsType_Object=MibTableColumn
ipoaLisDefaultEncapsType=_IpoaLisDefaultEncapsType_Object((1,3,6,1,2,1,10,46,1,2,1,3),_IpoaLisDefaultEncapsType_Type())
ipoaLisDefaultEncapsType.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaLisDefaultEncapsType.setStatus(_A)
class _IpoaLisInactivityTimer_Type(Integer32):defaultValue=1200
_IpoaLisInactivityTimer_Type.__name__=_E
_IpoaLisInactivityTimer_Object=MibTableColumn
ipoaLisInactivityTimer=_IpoaLisInactivityTimer_Object((1,3,6,1,2,1,10,46,1,2,1,4),_IpoaLisInactivityTimer_Type())
ipoaLisInactivityTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaLisInactivityTimer.setStatus(_A)
if mibBuilder.loadTexts:ipoaLisInactivityTimer.setUnits(_I)
class _IpoaLisMinHoldingTime_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpoaLisMinHoldingTime_Type.__name__=_E
_IpoaLisMinHoldingTime_Object=MibTableColumn
ipoaLisMinHoldingTime=_IpoaLisMinHoldingTime_Object((1,3,6,1,2,1,10,46,1,2,1,5),_IpoaLisMinHoldingTime_Type())
ipoaLisMinHoldingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaLisMinHoldingTime.setStatus(_A)
if mibBuilder.loadTexts:ipoaLisMinHoldingTime.setUnits(_I)
class _IpoaLisQDepth_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpoaLisQDepth_Type.__name__=_E
_IpoaLisQDepth_Object=MibTableColumn
ipoaLisQDepth=_IpoaLisQDepth_Object((1,3,6,1,2,1,10,46,1,2,1,6),_IpoaLisQDepth_Type())
ipoaLisQDepth.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaLisQDepth.setStatus(_A)
if mibBuilder.loadTexts:ipoaLisQDepth.setUnits('packets')
class _IpoaLisMaxCalls_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpoaLisMaxCalls_Type.__name__=_E
_IpoaLisMaxCalls_Object=MibTableColumn
ipoaLisMaxCalls=_IpoaLisMaxCalls_Object((1,3,6,1,2,1,10,46,1,2,1,7),_IpoaLisMaxCalls_Type())
ipoaLisMaxCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaLisMaxCalls.setStatus(_A)
class _IpoaLisCacheEntryAge_Type(Integer32):defaultValue=900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,1200))
_IpoaLisCacheEntryAge_Type.__name__=_E
_IpoaLisCacheEntryAge_Object=MibTableColumn
ipoaLisCacheEntryAge=_IpoaLisCacheEntryAge_Object((1,3,6,1,2,1,10,46,1,2,1,8),_IpoaLisCacheEntryAge_Type())
ipoaLisCacheEntryAge.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaLisCacheEntryAge.setStatus(_A)
if mibBuilder.loadTexts:ipoaLisCacheEntryAge.setUnits(_I)
class _IpoaLisRetries_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_IpoaLisRetries_Type.__name__=_E
_IpoaLisRetries_Object=MibTableColumn
ipoaLisRetries=_IpoaLisRetries_Object((1,3,6,1,2,1,10,46,1,2,1,9),_IpoaLisRetries_Type())
ipoaLisRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaLisRetries.setStatus(_A)
class _IpoaLisTimeout_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_IpoaLisTimeout_Type.__name__=_E
_IpoaLisTimeout_Object=MibTableColumn
ipoaLisTimeout=_IpoaLisTimeout_Object((1,3,6,1,2,1,10,46,1,2,1,10),_IpoaLisTimeout_Type())
ipoaLisTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaLisTimeout.setStatus(_A)
if mibBuilder.loadTexts:ipoaLisTimeout.setUnits(_I)
_IpoaLisDefaultPeakCellRate_Type=Integer32
_IpoaLisDefaultPeakCellRate_Object=MibTableColumn
ipoaLisDefaultPeakCellRate=_IpoaLisDefaultPeakCellRate_Object((1,3,6,1,2,1,10,46,1,2,1,11),_IpoaLisDefaultPeakCellRate_Type())
ipoaLisDefaultPeakCellRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaLisDefaultPeakCellRate.setStatus(_A)
_IpoaLisActiveVcs_Type=Gauge32
_IpoaLisActiveVcs_Object=MibTableColumn
ipoaLisActiveVcs=_IpoaLisActiveVcs_Object((1,3,6,1,2,1,10,46,1,2,1,12),_IpoaLisActiveVcs_Type())
ipoaLisActiveVcs.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaLisActiveVcs.setStatus(_A)
_IpoaLisRowStatus_Type=RowStatus
_IpoaLisRowStatus_Object=MibTableColumn
ipoaLisRowStatus=_IpoaLisRowStatus_Object((1,3,6,1,2,1,10,46,1,2,1,13),_IpoaLisRowStatus_Type())
ipoaLisRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaLisRowStatus.setStatus(_A)
_IpoaLisIfMappingTable_Object=MibTable
ipoaLisIfMappingTable=_IpoaLisIfMappingTable_Object((1,3,6,1,2,1,10,46,1,3))
if mibBuilder.loadTexts:ipoaLisIfMappingTable.setStatus(_A)
_IpoaLisIfMappingEntry_Object=MibTableRow
ipoaLisIfMappingEntry=_IpoaLisIfMappingEntry_Object((1,3,6,1,2,1,10,46,1,3,1))
ipoaLisIfMappingEntry.setIndexNames((0,_B,_H),(0,_B,_Q))
if mibBuilder.loadTexts:ipoaLisIfMappingEntry.setStatus(_A)
_IpoaLisIfMappingIfIndex_Type=InterfaceIndex
_IpoaLisIfMappingIfIndex_Object=MibTableColumn
ipoaLisIfMappingIfIndex=_IpoaLisIfMappingIfIndex_Object((1,3,6,1,2,1,10,46,1,3,1,1),_IpoaLisIfMappingIfIndex_Type())
ipoaLisIfMappingIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ipoaLisIfMappingIfIndex.setStatus(_A)
_IpoaLisIfMappingRowStatus_Type=RowStatus
_IpoaLisIfMappingRowStatus_Object=MibTableColumn
ipoaLisIfMappingRowStatus=_IpoaLisIfMappingRowStatus_Object((1,3,6,1,2,1,10,46,1,3,1,2),_IpoaLisIfMappingRowStatus_Type())
ipoaLisIfMappingRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaLisIfMappingRowStatus.setStatus(_A)
_IpoaArpClientTable_Object=MibTable
ipoaArpClientTable=_IpoaArpClientTable_Object((1,3,6,1,2,1,10,46,1,4))
if mibBuilder.loadTexts:ipoaArpClientTable.setStatus(_A)
_IpoaArpClientEntry_Object=MibTableRow
ipoaArpClientEntry=_IpoaArpClientEntry_Object((1,3,6,1,2,1,10,46,1,4,1))
ipoaArpClientEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:ipoaArpClientEntry.setStatus(_A)
_IpoaArpClientAtmAddr_Type=IpoaAtmAddr
_IpoaArpClientAtmAddr_Object=MibTableColumn
ipoaArpClientAtmAddr=_IpoaArpClientAtmAddr_Object((1,3,6,1,2,1,10,46,1,4,1,1),_IpoaArpClientAtmAddr_Type())
ipoaArpClientAtmAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaArpClientAtmAddr.setStatus(_A)
class _IpoaArpClientSrvrInUse_Type(IpoaAtmAddr):defaultHexValue=''
_IpoaArpClientSrvrInUse_Type.__name__=_R
_IpoaArpClientSrvrInUse_Object=MibTableColumn
ipoaArpClientSrvrInUse=_IpoaArpClientSrvrInUse_Object((1,3,6,1,2,1,10,46,1,4,1,2),_IpoaArpClientSrvrInUse_Type())
ipoaArpClientSrvrInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpClientSrvrInUse.setStatus(_A)
_IpoaArpClientInArpInReqs_Type=Counter32
_IpoaArpClientInArpInReqs_Object=MibTableColumn
ipoaArpClientInArpInReqs=_IpoaArpClientInArpInReqs_Object((1,3,6,1,2,1,10,46,1,4,1,3),_IpoaArpClientInArpInReqs_Type())
ipoaArpClientInArpInReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpClientInArpInReqs.setStatus(_A)
_IpoaArpClientInArpOutReqs_Type=Counter32
_IpoaArpClientInArpOutReqs_Object=MibTableColumn
ipoaArpClientInArpOutReqs=_IpoaArpClientInArpOutReqs_Object((1,3,6,1,2,1,10,46,1,4,1,4),_IpoaArpClientInArpOutReqs_Type())
ipoaArpClientInArpOutReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpClientInArpOutReqs.setStatus(_A)
_IpoaArpClientInArpInReplies_Type=Counter32
_IpoaArpClientInArpInReplies_Object=MibTableColumn
ipoaArpClientInArpInReplies=_IpoaArpClientInArpInReplies_Object((1,3,6,1,2,1,10,46,1,4,1,5),_IpoaArpClientInArpInReplies_Type())
ipoaArpClientInArpInReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpClientInArpInReplies.setStatus(_A)
_IpoaArpClientInArpOutReplies_Type=Counter32
_IpoaArpClientInArpOutReplies_Object=MibTableColumn
ipoaArpClientInArpOutReplies=_IpoaArpClientInArpOutReplies_Object((1,3,6,1,2,1,10,46,1,4,1,6),_IpoaArpClientInArpOutReplies_Type())
ipoaArpClientInArpOutReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpClientInArpOutReplies.setStatus(_A)
_IpoaArpClientInArpInvalidInReqs_Type=Counter32
_IpoaArpClientInArpInvalidInReqs_Object=MibTableColumn
ipoaArpClientInArpInvalidInReqs=_IpoaArpClientInArpInvalidInReqs_Object((1,3,6,1,2,1,10,46,1,4,1,7),_IpoaArpClientInArpInvalidInReqs_Type())
ipoaArpClientInArpInvalidInReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpClientInArpInvalidInReqs.setStatus(_A)
_IpoaArpClientInArpInvalidOutReqs_Type=Counter32
_IpoaArpClientInArpInvalidOutReqs_Object=MibTableColumn
ipoaArpClientInArpInvalidOutReqs=_IpoaArpClientInArpInvalidOutReqs_Object((1,3,6,1,2,1,10,46,1,4,1,8),_IpoaArpClientInArpInvalidOutReqs_Type())
ipoaArpClientInArpInvalidOutReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpClientInArpInvalidOutReqs.setStatus(_A)
_IpoaArpClientArpInReqs_Type=Counter32
_IpoaArpClientArpInReqs_Object=MibTableColumn
ipoaArpClientArpInReqs=_IpoaArpClientArpInReqs_Object((1,3,6,1,2,1,10,46,1,4,1,9),_IpoaArpClientArpInReqs_Type())
ipoaArpClientArpInReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpClientArpInReqs.setStatus(_A)
_IpoaArpClientArpOutReqs_Type=Counter32
_IpoaArpClientArpOutReqs_Object=MibTableColumn
ipoaArpClientArpOutReqs=_IpoaArpClientArpOutReqs_Object((1,3,6,1,2,1,10,46,1,4,1,10),_IpoaArpClientArpOutReqs_Type())
ipoaArpClientArpOutReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpClientArpOutReqs.setStatus(_A)
_IpoaArpClientArpInReplies_Type=Counter32
_IpoaArpClientArpInReplies_Object=MibTableColumn
ipoaArpClientArpInReplies=_IpoaArpClientArpInReplies_Object((1,3,6,1,2,1,10,46,1,4,1,11),_IpoaArpClientArpInReplies_Type())
ipoaArpClientArpInReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpClientArpInReplies.setStatus(_A)
_IpoaArpClientArpOutReplies_Type=Counter32
_IpoaArpClientArpOutReplies_Object=MibTableColumn
ipoaArpClientArpOutReplies=_IpoaArpClientArpOutReplies_Object((1,3,6,1,2,1,10,46,1,4,1,12),_IpoaArpClientArpOutReplies_Type())
ipoaArpClientArpOutReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpClientArpOutReplies.setStatus(_A)
_IpoaArpClientArpInNaks_Type=Counter32
_IpoaArpClientArpInNaks_Object=MibTableColumn
ipoaArpClientArpInNaks=_IpoaArpClientArpInNaks_Object((1,3,6,1,2,1,10,46,1,4,1,13),_IpoaArpClientArpInNaks_Type())
ipoaArpClientArpInNaks.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpClientArpInNaks.setStatus(_A)
_IpoaArpClientArpOutNaks_Type=Counter32
_IpoaArpClientArpOutNaks_Object=MibTableColumn
ipoaArpClientArpOutNaks=_IpoaArpClientArpOutNaks_Object((1,3,6,1,2,1,10,46,1,4,1,14),_IpoaArpClientArpOutNaks_Type())
ipoaArpClientArpOutNaks.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpClientArpOutNaks.setStatus(_A)
_IpoaArpClientArpUnknownOps_Type=Counter32
_IpoaArpClientArpUnknownOps_Object=MibTableColumn
ipoaArpClientArpUnknownOps=_IpoaArpClientArpUnknownOps_Object((1,3,6,1,2,1,10,46,1,4,1,15),_IpoaArpClientArpUnknownOps_Type())
ipoaArpClientArpUnknownOps.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpClientArpUnknownOps.setStatus(_A)
_IpoaArpClientArpNoSrvrResps_Type=Counter32
_IpoaArpClientArpNoSrvrResps_Object=MibTableColumn
ipoaArpClientArpNoSrvrResps=_IpoaArpClientArpNoSrvrResps_Object((1,3,6,1,2,1,10,46,1,4,1,16),_IpoaArpClientArpNoSrvrResps_Type())
ipoaArpClientArpNoSrvrResps.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpClientArpNoSrvrResps.setStatus(_A)
_IpoaArpClientRowStatus_Type=RowStatus
_IpoaArpClientRowStatus_Object=MibTableColumn
ipoaArpClientRowStatus=_IpoaArpClientRowStatus_Object((1,3,6,1,2,1,10,46,1,4,1,17),_IpoaArpClientRowStatus_Type())
ipoaArpClientRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaArpClientRowStatus.setStatus(_A)
_IpoaArpSrvrTable_Object=MibTable
ipoaArpSrvrTable=_IpoaArpSrvrTable_Object((1,3,6,1,2,1,10,46,1,5))
if mibBuilder.loadTexts:ipoaArpSrvrTable.setStatus(_A)
_IpoaArpSrvrEntry_Object=MibTableRow
ipoaArpSrvrEntry=_IpoaArpSrvrEntry_Object((1,3,6,1,2,1,10,46,1,5,1))
ipoaArpSrvrEntry.setIndexNames((0,_F,_J),(0,_B,_S))
if mibBuilder.loadTexts:ipoaArpSrvrEntry.setStatus(_A)
_IpoaArpSrvrAddr_Type=IpoaAtmAddr
_IpoaArpSrvrAddr_Object=MibTableColumn
ipoaArpSrvrAddr=_IpoaArpSrvrAddr_Object((1,3,6,1,2,1,10,46,1,5,1,1),_IpoaArpSrvrAddr_Type())
ipoaArpSrvrAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:ipoaArpSrvrAddr.setStatus(_A)
_IpoaArpSrvrLis_Type=IpAddress
_IpoaArpSrvrLis_Object=MibTableColumn
ipoaArpSrvrLis=_IpoaArpSrvrLis_Object((1,3,6,1,2,1,10,46,1,5,1,2),_IpoaArpSrvrLis_Type())
ipoaArpSrvrLis.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaArpSrvrLis.setStatus(_A)
_IpoaArpSrvrInArpInReqs_Type=Counter32
_IpoaArpSrvrInArpInReqs_Object=MibTableColumn
ipoaArpSrvrInArpInReqs=_IpoaArpSrvrInArpInReqs_Object((1,3,6,1,2,1,10,46,1,5,1,3),_IpoaArpSrvrInArpInReqs_Type())
ipoaArpSrvrInArpInReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpSrvrInArpInReqs.setStatus(_A)
_IpoaArpSrvrInArpOutReqs_Type=Counter32
_IpoaArpSrvrInArpOutReqs_Object=MibTableColumn
ipoaArpSrvrInArpOutReqs=_IpoaArpSrvrInArpOutReqs_Object((1,3,6,1,2,1,10,46,1,5,1,4),_IpoaArpSrvrInArpOutReqs_Type())
ipoaArpSrvrInArpOutReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpSrvrInArpOutReqs.setStatus(_A)
_IpoaArpSrvrInArpInReplies_Type=Counter32
_IpoaArpSrvrInArpInReplies_Object=MibTableColumn
ipoaArpSrvrInArpInReplies=_IpoaArpSrvrInArpInReplies_Object((1,3,6,1,2,1,10,46,1,5,1,5),_IpoaArpSrvrInArpInReplies_Type())
ipoaArpSrvrInArpInReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpSrvrInArpInReplies.setStatus(_A)
_IpoaArpSrvrInArpOutReplies_Type=Counter32
_IpoaArpSrvrInArpOutReplies_Object=MibTableColumn
ipoaArpSrvrInArpOutReplies=_IpoaArpSrvrInArpOutReplies_Object((1,3,6,1,2,1,10,46,1,5,1,6),_IpoaArpSrvrInArpOutReplies_Type())
ipoaArpSrvrInArpOutReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpSrvrInArpOutReplies.setStatus(_A)
_IpoaArpSrvrInArpInvalidInReqs_Type=Counter32
_IpoaArpSrvrInArpInvalidInReqs_Object=MibTableColumn
ipoaArpSrvrInArpInvalidInReqs=_IpoaArpSrvrInArpInvalidInReqs_Object((1,3,6,1,2,1,10,46,1,5,1,7),_IpoaArpSrvrInArpInvalidInReqs_Type())
ipoaArpSrvrInArpInvalidInReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpSrvrInArpInvalidInReqs.setStatus(_A)
_IpoaArpSrvrInArpInvalidOutReqs_Type=Counter32
_IpoaArpSrvrInArpInvalidOutReqs_Object=MibTableColumn
ipoaArpSrvrInArpInvalidOutReqs=_IpoaArpSrvrInArpInvalidOutReqs_Object((1,3,6,1,2,1,10,46,1,5,1,8),_IpoaArpSrvrInArpInvalidOutReqs_Type())
ipoaArpSrvrInArpInvalidOutReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpSrvrInArpInvalidOutReqs.setStatus(_A)
_IpoaArpSrvrArpInReqs_Type=Counter32
_IpoaArpSrvrArpInReqs_Object=MibTableColumn
ipoaArpSrvrArpInReqs=_IpoaArpSrvrArpInReqs_Object((1,3,6,1,2,1,10,46,1,5,1,9),_IpoaArpSrvrArpInReqs_Type())
ipoaArpSrvrArpInReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpSrvrArpInReqs.setStatus(_A)
_IpoaArpSrvrArpOutReplies_Type=Counter32
_IpoaArpSrvrArpOutReplies_Object=MibTableColumn
ipoaArpSrvrArpOutReplies=_IpoaArpSrvrArpOutReplies_Object((1,3,6,1,2,1,10,46,1,5,1,10),_IpoaArpSrvrArpOutReplies_Type())
ipoaArpSrvrArpOutReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpSrvrArpOutReplies.setStatus(_A)
_IpoaArpSrvrArpOutNaks_Type=Counter32
_IpoaArpSrvrArpOutNaks_Object=MibTableColumn
ipoaArpSrvrArpOutNaks=_IpoaArpSrvrArpOutNaks_Object((1,3,6,1,2,1,10,46,1,5,1,11),_IpoaArpSrvrArpOutNaks_Type())
ipoaArpSrvrArpOutNaks.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpSrvrArpOutNaks.setStatus(_A)
_IpoaArpSrvrArpDupIpAddrs_Type=Counter32
_IpoaArpSrvrArpDupIpAddrs_Object=MibTableColumn
ipoaArpSrvrArpDupIpAddrs=_IpoaArpSrvrArpDupIpAddrs_Object((1,3,6,1,2,1,10,46,1,5,1,12),_IpoaArpSrvrArpDupIpAddrs_Type())
ipoaArpSrvrArpDupIpAddrs.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpSrvrArpDupIpAddrs.setStatus(_A)
_IpoaArpSrvrArpUnknownOps_Type=Counter32
_IpoaArpSrvrArpUnknownOps_Object=MibTableColumn
ipoaArpSrvrArpUnknownOps=_IpoaArpSrvrArpUnknownOps_Object((1,3,6,1,2,1,10,46,1,5,1,13),_IpoaArpSrvrArpUnknownOps_Type())
ipoaArpSrvrArpUnknownOps.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpSrvrArpUnknownOps.setStatus(_A)
_IpoaArpSrvrRowStatus_Type=RowStatus
_IpoaArpSrvrRowStatus_Object=MibTableColumn
ipoaArpSrvrRowStatus=_IpoaArpSrvrRowStatus_Object((1,3,6,1,2,1,10,46,1,5,1,14),_IpoaArpSrvrRowStatus_Type())
ipoaArpSrvrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaArpSrvrRowStatus.setStatus(_A)
_IpoaArpRemoteSrvrTable_Object=MibTable
ipoaArpRemoteSrvrTable=_IpoaArpRemoteSrvrTable_Object((1,3,6,1,2,1,10,46,1,6))
if mibBuilder.loadTexts:ipoaArpRemoteSrvrTable.setStatus(_A)
_IpoaArpRemoteSrvrEntry_Object=MibTableRow
ipoaArpRemoteSrvrEntry=_IpoaArpRemoteSrvrEntry_Object((1,3,6,1,2,1,10,46,1,6,1))
ipoaArpRemoteSrvrEntry.setIndexNames((0,_B,_H),(0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:ipoaArpRemoteSrvrEntry.setStatus(_A)
_IpoaArpRemoteSrvrAtmAddr_Type=IpoaAtmAddr
_IpoaArpRemoteSrvrAtmAddr_Object=MibTableColumn
ipoaArpRemoteSrvrAtmAddr=_IpoaArpRemoteSrvrAtmAddr_Object((1,3,6,1,2,1,10,46,1,6,1,1),_IpoaArpRemoteSrvrAtmAddr_Type())
ipoaArpRemoteSrvrAtmAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:ipoaArpRemoteSrvrAtmAddr.setStatus(_A)
_IpoaArpRemoteSrvrRowStatus_Type=RowStatus
_IpoaArpRemoteSrvrRowStatus_Object=MibTableColumn
ipoaArpRemoteSrvrRowStatus=_IpoaArpRemoteSrvrRowStatus_Object((1,3,6,1,2,1,10,46,1,6,1,2),_IpoaArpRemoteSrvrRowStatus_Type())
ipoaArpRemoteSrvrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaArpRemoteSrvrRowStatus.setStatus(_A)
_IpoaArpRemoteSrvrIfIndex_Type=InterfaceIndexOrZero
_IpoaArpRemoteSrvrIfIndex_Object=MibTableColumn
ipoaArpRemoteSrvrIfIndex=_IpoaArpRemoteSrvrIfIndex_Object((1,3,6,1,2,1,10,46,1,6,1,3),_IpoaArpRemoteSrvrIfIndex_Type())
ipoaArpRemoteSrvrIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ipoaArpRemoteSrvrIfIndex.setStatus(_A)
class _IpoaArpRemoteSrvrIpAddr_Type(IpAddress):defaultHexValue='00000000'
_IpoaArpRemoteSrvrIpAddr_Type.__name__=_O
_IpoaArpRemoteSrvrIpAddr_Object=MibTableColumn
ipoaArpRemoteSrvrIpAddr=_IpoaArpRemoteSrvrIpAddr_Object((1,3,6,1,2,1,10,46,1,6,1,4),_IpoaArpRemoteSrvrIpAddr_Type())
ipoaArpRemoteSrvrIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpRemoteSrvrIpAddr.setStatus(_A)
class _IpoaArpRemoteSrvrAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_IpoaArpRemoteSrvrAdminStatus_Type.__name__=_E
_IpoaArpRemoteSrvrAdminStatus_Object=MibTableColumn
ipoaArpRemoteSrvrAdminStatus=_IpoaArpRemoteSrvrAdminStatus_Object((1,3,6,1,2,1,10,46,1,6,1,5),_IpoaArpRemoteSrvrAdminStatus_Type())
ipoaArpRemoteSrvrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaArpRemoteSrvrAdminStatus.setStatus(_A)
class _IpoaArpRemoteSrvrOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_IpoaArpRemoteSrvrOperStatus_Type.__name__=_E
_IpoaArpRemoteSrvrOperStatus_Object=MibTableColumn
ipoaArpRemoteSrvrOperStatus=_IpoaArpRemoteSrvrOperStatus_Object((1,3,6,1,2,1,10,46,1,6,1,6),_IpoaArpRemoteSrvrOperStatus_Type())
ipoaArpRemoteSrvrOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaArpRemoteSrvrOperStatus.setStatus(_A)
_IpoaVcTable_Object=MibTable
ipoaVcTable=_IpoaVcTable_Object((1,3,6,1,2,1,10,46,1,7))
if mibBuilder.loadTexts:ipoaVcTable.setStatus(_A)
_IpoaVcEntry_Object=MibTableRow
ipoaVcEntry=_IpoaVcEntry_Object((1,3,6,1,2,1,10,46,1,7,1))
ipoaVcEntry.setIndexNames((0,_F,_K),(0,_F,_L),(0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:ipoaVcEntry.setStatus(_A)
_IpoaVcVpi_Type=IpoaVpiInteger
_IpoaVcVpi_Object=MibTableColumn
ipoaVcVpi=_IpoaVcVpi_Object((1,3,6,1,2,1,10,46,1,7,1,1),_IpoaVcVpi_Type())
ipoaVcVpi.setMaxAccess(_G)
if mibBuilder.loadTexts:ipoaVcVpi.setStatus(_A)
_IpoaVcVci_Type=IpoaVciInteger
_IpoaVcVci_Object=MibTableColumn
ipoaVcVci=_IpoaVcVci_Object((1,3,6,1,2,1,10,46,1,7,1,2),_IpoaVcVci_Type())
ipoaVcVci.setMaxAccess(_G)
if mibBuilder.loadTexts:ipoaVcVci.setStatus(_A)
_IpoaVcType_Type=IpoaAtmConnKind
_IpoaVcType_Object=MibTableColumn
ipoaVcType=_IpoaVcType_Object((1,3,6,1,2,1,10,46,1,7,1,3),_IpoaVcType_Type())
ipoaVcType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaVcType.setStatus(_A)
_IpoaVcNegotiatedEncapsType_Type=IpoaEncapsType
_IpoaVcNegotiatedEncapsType_Object=MibTableColumn
ipoaVcNegotiatedEncapsType=_IpoaVcNegotiatedEncapsType_Object((1,3,6,1,2,1,10,46,1,7,1,4),_IpoaVcNegotiatedEncapsType_Type())
ipoaVcNegotiatedEncapsType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaVcNegotiatedEncapsType.setStatus(_A)
class _IpoaVcNegotiatedMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpoaVcNegotiatedMtu_Type.__name__=_E
_IpoaVcNegotiatedMtu_Object=MibTableColumn
ipoaVcNegotiatedMtu=_IpoaVcNegotiatedMtu_Object((1,3,6,1,2,1,10,46,1,7,1,5),_IpoaVcNegotiatedMtu_Type())
ipoaVcNegotiatedMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:ipoaVcNegotiatedMtu.setStatus(_A)
_IpoaConfigPvcTable_Object=MibTable
ipoaConfigPvcTable=_IpoaConfigPvcTable_Object((1,3,6,1,2,1,10,46,1,8))
if mibBuilder.loadTexts:ipoaConfigPvcTable.setStatus(_A)
_IpoaConfigPvcEntry_Object=MibTableRow
ipoaConfigPvcEntry=_IpoaConfigPvcEntry_Object((1,3,6,1,2,1,10,46,1,8,1))
ipoaConfigPvcEntry.setIndexNames((0,_B,_X),(0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:ipoaConfigPvcEntry.setStatus(_A)
_IpoaConfigPvcIfIndex_Type=InterfaceIndex
_IpoaConfigPvcIfIndex_Object=MibTableColumn
ipoaConfigPvcIfIndex=_IpoaConfigPvcIfIndex_Object((1,3,6,1,2,1,10,46,1,8,1,1),_IpoaConfigPvcIfIndex_Type())
ipoaConfigPvcIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ipoaConfigPvcIfIndex.setStatus(_A)
_IpoaConfigPvcVpi_Type=IpoaVpiInteger
_IpoaConfigPvcVpi_Object=MibTableColumn
ipoaConfigPvcVpi=_IpoaConfigPvcVpi_Object((1,3,6,1,2,1,10,46,1,8,1,2),_IpoaConfigPvcVpi_Type())
ipoaConfigPvcVpi.setMaxAccess(_G)
if mibBuilder.loadTexts:ipoaConfigPvcVpi.setStatus(_A)
_IpoaConfigPvcVci_Type=IpoaVciInteger
_IpoaConfigPvcVci_Object=MibTableColumn
ipoaConfigPvcVci=_IpoaConfigPvcVci_Object((1,3,6,1,2,1,10,46,1,8,1,3),_IpoaConfigPvcVci_Type())
ipoaConfigPvcVci.setMaxAccess(_G)
if mibBuilder.loadTexts:ipoaConfigPvcVci.setStatus(_A)
class _IpoaConfigPvcDefaultMtu_Type(Integer32):defaultValue=9180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpoaConfigPvcDefaultMtu_Type.__name__=_E
_IpoaConfigPvcDefaultMtu_Object=MibTableColumn
ipoaConfigPvcDefaultMtu=_IpoaConfigPvcDefaultMtu_Object((1,3,6,1,2,1,10,46,1,8,1,4),_IpoaConfigPvcDefaultMtu_Type())
ipoaConfigPvcDefaultMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaConfigPvcDefaultMtu.setStatus(_A)
_IpoaConfigPvcRowStatus_Type=RowStatus
_IpoaConfigPvcRowStatus_Object=MibTableColumn
ipoaConfigPvcRowStatus=_IpoaConfigPvcRowStatus_Object((1,3,6,1,2,1,10,46,1,8,1,5),_IpoaConfigPvcRowStatus_Type())
ipoaConfigPvcRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ipoaConfigPvcRowStatus.setStatus(_A)
_IpoaNotifications_ObjectIdentity=ObjectIdentity
ipoaNotifications=_IpoaNotifications_ObjectIdentity((1,3,6,1,2,1,10,46,2))
_IpoaTrapPrefix_ObjectIdentity=ObjectIdentity
ipoaTrapPrefix=_IpoaTrapPrefix_ObjectIdentity((1,3,6,1,2,1,10,46,2,0))
_IpoaConformance_ObjectIdentity=ObjectIdentity
ipoaConformance=_IpoaConformance_ObjectIdentity((1,3,6,1,2,1,10,46,3))
_IpoaGroups_ObjectIdentity=ObjectIdentity
ipoaGroups=_IpoaGroups_ObjectIdentity((1,3,6,1,2,1,10,46,3,1))
_IpoaCompliances_ObjectIdentity=ObjectIdentity
ipoaCompliances=_IpoaCompliances_ObjectIdentity((1,3,6,1,2,1,10,46,3,2))
ipoaGeneralGroup=ObjectGroup((1,3,6,1,2,1,10,46,3,1,1))
ipoaGeneralGroup.setObjects(*((_B,_a),(_B,_b),(_B,_N),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:ipoaGeneralGroup.setStatus(_A)
ipoaClientGroup=ObjectGroup((1,3,6,1,2,1,10,46,3,1,2))
ipoaClientGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:ipoaClientGroup.setStatus(_A)
ipoaSrvrGroup=ObjectGroup((1,3,6,1,2,1,10,46,3,1,3))
ipoaSrvrGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:ipoaSrvrGroup.setStatus(_A)
ipoaLisTableGroup=ObjectGroup((1,3,6,1,2,1,10,46,3,1,7))
ipoaLisTableGroup.setObjects(*((_B,_A8),(_B,_H),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:ipoaLisTableGroup.setStatus(_A)
ipoaMtuExceeded=NotificationType((1,3,6,1,2,1,10,46,2,0,1))
ipoaMtuExceeded.setObjects((_B,_N))
if mibBuilder.loadTexts:ipoaMtuExceeded.setStatus(_A)
ipoaDuplicateIpAddress=NotificationType((1,3,6,1,2,1,10,46,2,0,2))
ipoaDuplicateIpAddress.setObjects(*((_F,_K),(_F,_L),(_F,_M),(_F,_M)))
if mibBuilder.loadTexts:ipoaDuplicateIpAddress.setStatus(_A)
ipoaLisCreate=NotificationType((1,3,6,1,2,1,10,46,2,0,3))
ipoaLisCreate.setObjects((_B,_H))
if mibBuilder.loadTexts:ipoaLisCreate.setStatus(_A)
ipoaLisDelete=NotificationType((1,3,6,1,2,1,10,46,2,0,4))
ipoaLisDelete.setObjects((_B,_H))
if mibBuilder.loadTexts:ipoaLisDelete.setStatus(_A)
ipoaBasicNotificationsGroup=NotificationGroup((1,3,6,1,2,1,10,46,3,1,4))
ipoaBasicNotificationsGroup.setObjects((_B,_AQ))
if mibBuilder.loadTexts:ipoaBasicNotificationsGroup.setStatus(_A)
ipoaSrvrNotificationsGroup=NotificationGroup((1,3,6,1,2,1,10,46,3,1,5))
ipoaSrvrNotificationsGroup.setObjects((_B,_AR))
if mibBuilder.loadTexts:ipoaSrvrNotificationsGroup.setStatus(_A)
ipoaLisNotificationsGroup=NotificationGroup((1,3,6,1,2,1,10,46,3,1,6))
ipoaLisNotificationsGroup.setObjects(*((_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:ipoaLisNotificationsGroup.setStatus(_A)
ipoaCompliance=ModuleCompliance((1,3,6,1,2,1,10,46,3,2,1))
ipoaCompliance.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:ipoaCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_P:IpoaEncapsType,'IpoaVpiInteger':IpoaVpiInteger,'IpoaVciInteger':IpoaVciInteger,_R:IpoaAtmAddr,'IpoaAtmConnKind':IpoaAtmConnKind,'ipoaMIB':ipoaMIB,'ipoaObjects':ipoaObjects,_A8:ipoaLisTrapEnable,'ipoaLisTable':ipoaLisTable,'ipoaLisEntry':ipoaLisEntry,_H:ipoaLisSubnetAddr,_A9:ipoaLisDefaultMtu,_AA:ipoaLisDefaultEncapsType,_AB:ipoaLisInactivityTimer,_AC:ipoaLisMinHoldingTime,_AD:ipoaLisQDepth,_AE:ipoaLisMaxCalls,_AF:ipoaLisCacheEntryAge,_AG:ipoaLisRetries,_AH:ipoaLisTimeout,_AI:ipoaLisDefaultPeakCellRate,_AJ:ipoaLisActiveVcs,_AK:ipoaLisRowStatus,'ipoaLisIfMappingTable':ipoaLisIfMappingTable,'ipoaLisIfMappingEntry':ipoaLisIfMappingEntry,_Q:ipoaLisIfMappingIfIndex,_AL:ipoaLisIfMappingRowStatus,'ipoaArpClientTable':ipoaArpClientTable,'ipoaArpClientEntry':ipoaArpClientEntry,_e:ipoaArpClientAtmAddr,_f:ipoaArpClientSrvrInUse,_g:ipoaArpClientInArpInReqs,_h:ipoaArpClientInArpOutReqs,_i:ipoaArpClientInArpInReplies,_j:ipoaArpClientInArpOutReplies,_k:ipoaArpClientInArpInvalidInReqs,_l:ipoaArpClientInArpInvalidOutReqs,_m:ipoaArpClientArpInReqs,_n:ipoaArpClientArpOutReqs,_o:ipoaArpClientArpInReplies,_p:ipoaArpClientArpOutReplies,_q:ipoaArpClientArpInNaks,_r:ipoaArpClientArpOutNaks,_s:ipoaArpClientArpUnknownOps,_t:ipoaArpClientArpNoSrvrResps,_u:ipoaArpClientRowStatus,'ipoaArpSrvrTable':ipoaArpSrvrTable,'ipoaArpSrvrEntry':ipoaArpSrvrEntry,_S:ipoaArpSrvrAddr,_v:ipoaArpSrvrLis,_w:ipoaArpSrvrInArpInReqs,_x:ipoaArpSrvrInArpOutReqs,_y:ipoaArpSrvrInArpInReplies,_z:ipoaArpSrvrInArpOutReplies,_A0:ipoaArpSrvrInArpInvalidInReqs,_A1:ipoaArpSrvrInArpInvalidOutReqs,_A2:ipoaArpSrvrArpInReqs,_A3:ipoaArpSrvrArpOutReplies,_A4:ipoaArpSrvrArpOutNaks,_A5:ipoaArpSrvrArpDupIpAddrs,_A6:ipoaArpSrvrArpUnknownOps,_A7:ipoaArpSrvrRowStatus,'ipoaArpRemoteSrvrTable':ipoaArpRemoteSrvrTable,'ipoaArpRemoteSrvrEntry':ipoaArpRemoteSrvrEntry,_T:ipoaArpRemoteSrvrAtmAddr,_AM:ipoaArpRemoteSrvrRowStatus,_U:ipoaArpRemoteSrvrIfIndex,_AN:ipoaArpRemoteSrvrIpAddr,_AO:ipoaArpRemoteSrvrAdminStatus,_AP:ipoaArpRemoteSrvrOperStatus,'ipoaVcTable':ipoaVcTable,'ipoaVcEntry':ipoaVcEntry,_V:ipoaVcVpi,_W:ipoaVcVci,_a:ipoaVcType,_b:ipoaVcNegotiatedEncapsType,_N:ipoaVcNegotiatedMtu,'ipoaConfigPvcTable':ipoaConfigPvcTable,'ipoaConfigPvcEntry':ipoaConfigPvcEntry,_X:ipoaConfigPvcIfIndex,_Y:ipoaConfigPvcVpi,_Z:ipoaConfigPvcVci,_c:ipoaConfigPvcDefaultMtu,_d:ipoaConfigPvcRowStatus,'ipoaNotifications':ipoaNotifications,'ipoaTrapPrefix':ipoaTrapPrefix,_AQ:ipoaMtuExceeded,_AR:ipoaDuplicateIpAddress,_AS:ipoaLisCreate,_AT:ipoaLisDelete,'ipoaConformance':ipoaConformance,'ipoaGroups':ipoaGroups,_AU:ipoaGeneralGroup,_AW:ipoaClientGroup,_AX:ipoaSrvrGroup,_AV:ipoaBasicNotificationsGroup,_AY:ipoaSrvrNotificationsGroup,_AZ:ipoaLisNotificationsGroup,_Aa:ipoaLisTableGroup,'ipoaCompliances':ipoaCompliances,'ipoaCompliance':ipoaCompliance})