_Ag='ciscoIetfPimExtNotifEnabledGroup'
_Af='ciscoIetfPimExtNotificationGroup'
_Ae='ciscoIetfPimExtRPMappingChange'
_Ad='ciscoIetfPimExtInterfaceDown'
_Ac='ciscoIetfPimExtInterfaceUp'
_Ab='cpimExtRPMappingChangeNotifEnabled'
_Aa='cpimExtInterfaceStateChangeNotifEnabled'
_AZ='cpimExtCRPBidir'
_AY='cpimExtMRouteBidirGroup'
_AX='cpimExtNbrBidirCapable'
_AW='cpimExtIfBidirCapable'
_AV='cpimExtBidirDFStateTimer'
_AU='cpimExtBidirDFState'
_AT='cpimExtBidirDFWinnerMetric'
_AS='cpimExtBidirDFWnrMtrcPref'
_AR='cpimExtBidirDFWinnerUptime'
_AQ='cpimExtBidirDFWinnerAddress'
_AP='cpimExtMRouteNextHopJoinPruneTmr'
_AO='cpimExtMRouteNextHopAsrtMtrcPref'
_AN='cpimExtMRouteNextHopAssertMetric'
_AM='cpimExtMRouteNextHopAssertTimer'
_AL='cpimExtMRouteNextHopAssertWinner'
_AK='cpimExtNbrSecMask'
_AJ='cpimExtNbrDRPriority'
_AI='cpimExtNbrDRPresent'
_AH='cpimExtNbrGenId'
_AG='cpimExtNbrSRCapable'
_AF='cpimExtNbrTBit'
_AE='cpimExtNbrOverrideInterval'
_AD='cpimExtNbrLANPruneDelay'
_AC='cpimExtStateRefreshTimeToLive'
_AB='cpimExtStateRefreshLimitInterval'
_AA='cpimExtStateRefreshInterval'
_A9='cpimExtSourceLifetime'
_A8='cpimExtRPSetRPActive'
_A7='cpimExtRPSetPriority'
_A6='cpimExtRPSetExpiryTime'
_A5='cpimExtMRouteOriginatorSRTTL'
_A4='cpimExtMRouteSourceTimer'
_A3='cpimExtMRouteRPFNeighbor'
_A2='cpimExtIfBSRBorder'
_A1='cpimExtIfDRPriority'
_A0='cpimExtIfSRCapable'
_z='cpimExtIfLanDelayEnabled'
_y='cpimExtIfSRTTLThreshold'
_x='cpimExtIfMaxGraftRetries'
_w='cpimExtIfGraftRetryInterval'
_v='cpimExtIfJoinPruneHoldtime'
_u='cpimExtIfGenerationID'
_t='cpimExtIfOverrideInterval'
_s='cpimExtIfPropagationDelay'
_r='cpimExtIfLanPruneDelay'
_q='cpimExtIfHelloHoldtime'
_p='cpimExtIfTrigHelloInterval'
_o='cpimExtCRPEntry'
_n='cpimExtMRouteNextHopEntry'
_m='cpimExtMRouteEntry'
_l='cpimExtNbrEntry'
_k='cpimExtIfEntry'
_j='cpimExtRPSetAddress'
_i='cpimExtRPSetProtocol'
_h='cpimExtRPSetType'
_g='cpimExtRPSetGroupMask'
_f='cpimExtRPSetGroupAddress'
_e='cpimExtRPSetAddrType'
_d='cpimExtRPSetComponent'
_c='cpimExtBidirDFIfIndex'
_b='cpimExtBidirDFRPAddress'
_a='cpimExtBidirDFRPAddressType'
_Z='TimeTicks'
_Y='cpimRPMappingChangeType'
_X='CISCO-PIM-MIB'
_W='cPimNbrIfIndex'
_V='cPimNbrAddressType'
_U='cPimNbrAddress'
_T='ciscoIetfPimExtBidirGroup'
_S='ciscoIetfPimExtNextHopGroup'
_R='ciscoIetfPimExtNbrGroup'
_Q='ciscoIetfPimExtGeneralGroup'
_P='cpimExtRPSetHoldTime'
_O='cpimExtNbrSecAddress'
_N='cPimIfStatus'
_M='Integer32'
_L='Bits'
_K='TruthValue'
_J='read-write'
_I='CISCO-IETF-PIM-MIB'
_H='seconds'
_G='InetAddress'
_F='not-accessible'
_E='read-create'
_D='Unsigned32'
_C='read-only'
_B='CISCO-IETF-PIM-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cPimCRPEntry,cPimIfEntry,cPimIfStatus,cPimInetMRouteEntry,cPimInetMRouteNextHopEntry,cPimNbrAddress,cPimNbrAddressType,cPimNbrEntry,cPimNbrIfIndex=mibBuilder.importSymbols(_I,'cPimCRPEntry','cPimIfEntry',_N,'cPimInetMRouteEntry','cPimInetMRouteNextHopEntry',_U,_V,'cPimNbrEntry',_W)
cpimRPMappingChangeType,=mibBuilder.importSymbols(_X,_Y)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
IANAipMRouteProtocol,=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipMRouteProtocol')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G,'InetAddressPrefixLength','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_L,'Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_Z,_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_K)
ciscoIetfPimExtMIB=ModuleIdentity((1,3,6,1,4,1,9,10,120))
if mibBuilder.loadTexts:ciscoIetfPimExtMIB.setRevisions(('2014-06-12 00:00','2006-08-25 00:00','2005-02-21 00:00'))
_CiscoIetfPimExtNotifs_ObjectIdentity=ObjectIdentity
ciscoIetfPimExtNotifs=_CiscoIetfPimExtNotifs_ObjectIdentity((1,3,6,1,4,1,9,10,120,0))
_CiscoIetfPimExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIetfPimExtMIBObjects=_CiscoIetfPimExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,120,1))
_CiscoPimExt_ObjectIdentity=ObjectIdentity
ciscoPimExt=_CiscoPimExt_ObjectIdentity((1,3,6,1,4,1,9,10,120,1,1))
_CpimExtIfTable_Object=MibTable
cpimExtIfTable=_CpimExtIfTable_Object((1,3,6,1,4,1,9,10,120,1,1,1))
if mibBuilder.loadTexts:cpimExtIfTable.setStatus(_A)
_CpimExtIfEntry_Object=MibTableRow
cpimExtIfEntry=_CpimExtIfEntry_Object((1,3,6,1,4,1,9,10,120,1,1,1,1))
if mibBuilder.loadTexts:cpimExtIfEntry.setStatus(_A)
class _CpimExtIfTrigHelloInterval_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpimExtIfTrigHelloInterval_Type.__name__=_D
_CpimExtIfTrigHelloInterval_Object=MibTableColumn
cpimExtIfTrigHelloInterval=_CpimExtIfTrigHelloInterval_Object((1,3,6,1,4,1,9,10,120,1,1,1,1,1),_CpimExtIfTrigHelloInterval_Type())
cpimExtIfTrigHelloInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cpimExtIfTrigHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:cpimExtIfTrigHelloInterval.setUnits(_H)
class _CpimExtIfHelloHoldtime_Type(Unsigned32):defaultValue=105;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpimExtIfHelloHoldtime_Type.__name__=_D
_CpimExtIfHelloHoldtime_Object=MibTableColumn
cpimExtIfHelloHoldtime=_CpimExtIfHelloHoldtime_Object((1,3,6,1,4,1,9,10,120,1,1,1,1,2),_CpimExtIfHelloHoldtime_Type())
cpimExtIfHelloHoldtime.setMaxAccess(_E)
if mibBuilder.loadTexts:cpimExtIfHelloHoldtime.setStatus(_A)
if mibBuilder.loadTexts:cpimExtIfHelloHoldtime.setUnits(_H)
class _CpimExtIfLanPruneDelay_Type(Bits):defaultBinValue='01';namedValues=NamedValues(*(('off',0),('on',1)))
_CpimExtIfLanPruneDelay_Type.__name__=_L
_CpimExtIfLanPruneDelay_Object=MibTableColumn
cpimExtIfLanPruneDelay=_CpimExtIfLanPruneDelay_Object((1,3,6,1,4,1,9,10,120,1,1,1,1,3),_CpimExtIfLanPruneDelay_Type())
cpimExtIfLanPruneDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:cpimExtIfLanPruneDelay.setStatus(_A)
class _CpimExtIfPropagationDelay_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_CpimExtIfPropagationDelay_Type.__name__=_D
_CpimExtIfPropagationDelay_Object=MibTableColumn
cpimExtIfPropagationDelay=_CpimExtIfPropagationDelay_Object((1,3,6,1,4,1,9,10,120,1,1,1,1,4),_CpimExtIfPropagationDelay_Type())
cpimExtIfPropagationDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:cpimExtIfPropagationDelay.setStatus(_A)
if mibBuilder.loadTexts:cpimExtIfPropagationDelay.setUnits('milliseconds')
class _CpimExtIfOverrideInterval_Type(Unsigned32):defaultValue=2500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpimExtIfOverrideInterval_Type.__name__=_D
_CpimExtIfOverrideInterval_Object=MibTableColumn
cpimExtIfOverrideInterval=_CpimExtIfOverrideInterval_Object((1,3,6,1,4,1,9,10,120,1,1,1,1,5),_CpimExtIfOverrideInterval_Type())
cpimExtIfOverrideInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cpimExtIfOverrideInterval.setStatus(_A)
class _CpimExtIfGenerationID_Type(Bits):defaultBinValue='1';namedValues=NamedValues(*(('off',0),('on',1)))
_CpimExtIfGenerationID_Type.__name__=_L
_CpimExtIfGenerationID_Object=MibTableColumn
cpimExtIfGenerationID=_CpimExtIfGenerationID_Object((1,3,6,1,4,1,9,10,120,1,1,1,1,6),_CpimExtIfGenerationID_Type())
cpimExtIfGenerationID.setMaxAccess(_E)
if mibBuilder.loadTexts:cpimExtIfGenerationID.setStatus(_A)
class _CpimExtIfJoinPruneHoldtime_Type(Unsigned32):defaultValue=210;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpimExtIfJoinPruneHoldtime_Type.__name__=_D
_CpimExtIfJoinPruneHoldtime_Object=MibTableColumn
cpimExtIfJoinPruneHoldtime=_CpimExtIfJoinPruneHoldtime_Object((1,3,6,1,4,1,9,10,120,1,1,1,1,7),_CpimExtIfJoinPruneHoldtime_Type())
cpimExtIfJoinPruneHoldtime.setMaxAccess(_E)
if mibBuilder.loadTexts:cpimExtIfJoinPruneHoldtime.setStatus(_A)
if mibBuilder.loadTexts:cpimExtIfJoinPruneHoldtime.setUnits(_H)
class _CpimExtIfGraftRetryInterval_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpimExtIfGraftRetryInterval_Type.__name__=_D
_CpimExtIfGraftRetryInterval_Object=MibTableColumn
cpimExtIfGraftRetryInterval=_CpimExtIfGraftRetryInterval_Object((1,3,6,1,4,1,9,10,120,1,1,1,1,8),_CpimExtIfGraftRetryInterval_Type())
cpimExtIfGraftRetryInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cpimExtIfGraftRetryInterval.setStatus(_A)
if mibBuilder.loadTexts:cpimExtIfGraftRetryInterval.setUnits(_H)
class _CpimExtIfMaxGraftRetries_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpimExtIfMaxGraftRetries_Type.__name__=_D
_CpimExtIfMaxGraftRetries_Object=MibTableColumn
cpimExtIfMaxGraftRetries=_CpimExtIfMaxGraftRetries_Object((1,3,6,1,4,1,9,10,120,1,1,1,1,9),_CpimExtIfMaxGraftRetries_Type())
cpimExtIfMaxGraftRetries.setMaxAccess(_E)
if mibBuilder.loadTexts:cpimExtIfMaxGraftRetries.setStatus(_A)
class _CpimExtIfSRTTLThreshold_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpimExtIfSRTTLThreshold_Type.__name__=_D
_CpimExtIfSRTTLThreshold_Object=MibTableColumn
cpimExtIfSRTTLThreshold=_CpimExtIfSRTTLThreshold_Object((1,3,6,1,4,1,9,10,120,1,1,1,1,10),_CpimExtIfSRTTLThreshold_Type())
cpimExtIfSRTTLThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cpimExtIfSRTTLThreshold.setStatus(_A)
_CpimExtIfLanDelayEnabled_Type=TruthValue
_CpimExtIfLanDelayEnabled_Object=MibTableColumn
cpimExtIfLanDelayEnabled=_CpimExtIfLanDelayEnabled_Object((1,3,6,1,4,1,9,10,120,1,1,1,1,11),_CpimExtIfLanDelayEnabled_Type())
cpimExtIfLanDelayEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtIfLanDelayEnabled.setStatus(_A)
_CpimExtIfSRCapable_Type=TruthValue
_CpimExtIfSRCapable_Object=MibTableColumn
cpimExtIfSRCapable=_CpimExtIfSRCapable_Object((1,3,6,1,4,1,9,10,120,1,1,1,1,12),_CpimExtIfSRCapable_Type())
cpimExtIfSRCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtIfSRCapable.setStatus(_A)
class _CpimExtIfDRPriority_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpimExtIfDRPriority_Type.__name__=_D
_CpimExtIfDRPriority_Object=MibTableColumn
cpimExtIfDRPriority=_CpimExtIfDRPriority_Object((1,3,6,1,4,1,9,10,120,1,1,1,1,13),_CpimExtIfDRPriority_Type())
cpimExtIfDRPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:cpimExtIfDRPriority.setStatus(_A)
_CpimExtIfBidirCapable_Type=TruthValue
_CpimExtIfBidirCapable_Object=MibTableColumn
cpimExtIfBidirCapable=_CpimExtIfBidirCapable_Object((1,3,6,1,4,1,9,10,120,1,1,1,1,14),_CpimExtIfBidirCapable_Type())
cpimExtIfBidirCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtIfBidirCapable.setStatus(_A)
class _CpimExtIfBSRBorder_Type(TruthValue):defaultValue=2
_CpimExtIfBSRBorder_Type.__name__=_K
_CpimExtIfBSRBorder_Object=MibTableColumn
cpimExtIfBSRBorder=_CpimExtIfBSRBorder_Object((1,3,6,1,4,1,9,10,120,1,1,1,1,15),_CpimExtIfBSRBorder_Type())
cpimExtIfBSRBorder.setMaxAccess(_E)
if mibBuilder.loadTexts:cpimExtIfBSRBorder.setStatus(_A)
_CpimExtNbrTable_Object=MibTable
cpimExtNbrTable=_CpimExtNbrTable_Object((1,3,6,1,4,1,9,10,120,1,1,2))
if mibBuilder.loadTexts:cpimExtNbrTable.setStatus(_A)
_CpimExtNbrEntry_Object=MibTableRow
cpimExtNbrEntry=_CpimExtNbrEntry_Object((1,3,6,1,4,1,9,10,120,1,1,2,1))
if mibBuilder.loadTexts:cpimExtNbrEntry.setStatus(_A)
class _CpimExtNbrLANPruneDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpimExtNbrLANPruneDelay_Type.__name__=_D
_CpimExtNbrLANPruneDelay_Object=MibTableColumn
cpimExtNbrLANPruneDelay=_CpimExtNbrLANPruneDelay_Object((1,3,6,1,4,1,9,10,120,1,1,2,1,1),_CpimExtNbrLANPruneDelay_Type())
cpimExtNbrLANPruneDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtNbrLANPruneDelay.setStatus(_A)
class _CpimExtNbrOverrideInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpimExtNbrOverrideInterval_Type.__name__=_D
_CpimExtNbrOverrideInterval_Object=MibTableColumn
cpimExtNbrOverrideInterval=_CpimExtNbrOverrideInterval_Object((1,3,6,1,4,1,9,10,120,1,1,2,1,2),_CpimExtNbrOverrideInterval_Type())
cpimExtNbrOverrideInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtNbrOverrideInterval.setStatus(_A)
class _CpimExtNbrTBit_Type(Bits):namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_CpimExtNbrTBit_Type.__name__=_L
_CpimExtNbrTBit_Object=MibTableColumn
cpimExtNbrTBit=_CpimExtNbrTBit_Object((1,3,6,1,4,1,9,10,120,1,1,2,1,3),_CpimExtNbrTBit_Type())
cpimExtNbrTBit.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtNbrTBit.setStatus(_A)
_CpimExtNbrSRCapable_Type=TruthValue
_CpimExtNbrSRCapable_Object=MibTableColumn
cpimExtNbrSRCapable=_CpimExtNbrSRCapable_Object((1,3,6,1,4,1,9,10,120,1,1,2,1,4),_CpimExtNbrSRCapable_Type())
cpimExtNbrSRCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtNbrSRCapable.setStatus(_A)
_CpimExtNbrGenId_Type=Unsigned32
_CpimExtNbrGenId_Object=MibTableColumn
cpimExtNbrGenId=_CpimExtNbrGenId_Object((1,3,6,1,4,1,9,10,120,1,1,2,1,5),_CpimExtNbrGenId_Type())
cpimExtNbrGenId.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtNbrGenId.setStatus(_A)
_CpimExtNbrBidirCapable_Type=TruthValue
_CpimExtNbrBidirCapable_Object=MibTableColumn
cpimExtNbrBidirCapable=_CpimExtNbrBidirCapable_Object((1,3,6,1,4,1,9,10,120,1,1,2,1,6),_CpimExtNbrBidirCapable_Type())
cpimExtNbrBidirCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtNbrBidirCapable.setStatus(_A)
_CpimExtNbrDRPresent_Type=TruthValue
_CpimExtNbrDRPresent_Object=MibTableColumn
cpimExtNbrDRPresent=_CpimExtNbrDRPresent_Object((1,3,6,1,4,1,9,10,120,1,1,2,1,7),_CpimExtNbrDRPresent_Type())
cpimExtNbrDRPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtNbrDRPresent.setStatus(_A)
class _CpimExtNbrDRPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpimExtNbrDRPriority_Type.__name__=_D
_CpimExtNbrDRPriority_Object=MibTableColumn
cpimExtNbrDRPriority=_CpimExtNbrDRPriority_Object((1,3,6,1,4,1,9,10,120,1,1,2,1,8),_CpimExtNbrDRPriority_Type())
cpimExtNbrDRPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtNbrDRPriority.setStatus(_A)
_CpimExtNbrSecAddressTable_Object=MibTable
cpimExtNbrSecAddressTable=_CpimExtNbrSecAddressTable_Object((1,3,6,1,4,1,9,10,120,1,1,3))
if mibBuilder.loadTexts:cpimExtNbrSecAddressTable.setStatus(_A)
_CpimExtNbrSecAddressEntry_Object=MibTableRow
cpimExtNbrSecAddressEntry=_CpimExtNbrSecAddressEntry_Object((1,3,6,1,4,1,9,10,120,1,1,3,1))
cpimExtNbrSecAddressEntry.setIndexNames((0,_I,_W),(0,_I,_V),(0,_I,_U),(0,_B,_O))
if mibBuilder.loadTexts:cpimExtNbrSecAddressEntry.setStatus(_A)
class _CpimExtNbrSecAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CpimExtNbrSecAddress_Type.__name__=_G
_CpimExtNbrSecAddress_Object=MibTableColumn
cpimExtNbrSecAddress=_CpimExtNbrSecAddress_Object((1,3,6,1,4,1,9,10,120,1,1,3,1,1),_CpimExtNbrSecAddress_Type())
cpimExtNbrSecAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtNbrSecAddress.setStatus(_A)
_CpimExtNbrSecMask_Type=InetAddressPrefixLength
_CpimExtNbrSecMask_Object=MibTableColumn
cpimExtNbrSecMask=_CpimExtNbrSecMask_Object((1,3,6,1,4,1,9,10,120,1,1,3,1,2),_CpimExtNbrSecMask_Type())
cpimExtNbrSecMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtNbrSecMask.setStatus(_A)
_CpimExtMRouteTable_Object=MibTable
cpimExtMRouteTable=_CpimExtMRouteTable_Object((1,3,6,1,4,1,9,10,120,1,1,4))
if mibBuilder.loadTexts:cpimExtMRouteTable.setStatus(_A)
_CpimExtMRouteEntry_Object=MibTableRow
cpimExtMRouteEntry=_CpimExtMRouteEntry_Object((1,3,6,1,4,1,9,10,120,1,1,4,1))
if mibBuilder.loadTexts:cpimExtMRouteEntry.setStatus(_A)
class _CpimExtMRouteRPFNeighbor_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CpimExtMRouteRPFNeighbor_Type.__name__=_G
_CpimExtMRouteRPFNeighbor_Object=MibTableColumn
cpimExtMRouteRPFNeighbor=_CpimExtMRouteRPFNeighbor_Object((1,3,6,1,4,1,9,10,120,1,1,4,1,1),_CpimExtMRouteRPFNeighbor_Type())
cpimExtMRouteRPFNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtMRouteRPFNeighbor.setStatus(_A)
_CpimExtMRouteSourceTimer_Type=TimeTicks
_CpimExtMRouteSourceTimer_Object=MibTableColumn
cpimExtMRouteSourceTimer=_CpimExtMRouteSourceTimer_Object((1,3,6,1,4,1,9,10,120,1,1,4,1,2),_CpimExtMRouteSourceTimer_Type())
cpimExtMRouteSourceTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtMRouteSourceTimer.setStatus(_A)
class _CpimExtMRouteOriginatorSRTTL_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CpimExtMRouteOriginatorSRTTL_Type.__name__=_D
_CpimExtMRouteOriginatorSRTTL_Object=MibTableColumn
cpimExtMRouteOriginatorSRTTL=_CpimExtMRouteOriginatorSRTTL_Object((1,3,6,1,4,1,9,10,120,1,1,4,1,3),_CpimExtMRouteOriginatorSRTTL_Type())
cpimExtMRouteOriginatorSRTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtMRouteOriginatorSRTTL.setStatus(_A)
_CpimExtMRouteBidirGroup_Type=TruthValue
_CpimExtMRouteBidirGroup_Object=MibTableColumn
cpimExtMRouteBidirGroup=_CpimExtMRouteBidirGroup_Object((1,3,6,1,4,1,9,10,120,1,1,4,1,4),_CpimExtMRouteBidirGroup_Type())
cpimExtMRouteBidirGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtMRouteBidirGroup.setStatus(_A)
_CpimExtMRouteNextHopTable_Object=MibTable
cpimExtMRouteNextHopTable=_CpimExtMRouteNextHopTable_Object((1,3,6,1,4,1,9,10,120,1,1,5))
if mibBuilder.loadTexts:cpimExtMRouteNextHopTable.setStatus(_A)
_CpimExtMRouteNextHopEntry_Object=MibTableRow
cpimExtMRouteNextHopEntry=_CpimExtMRouteNextHopEntry_Object((1,3,6,1,4,1,9,10,120,1,1,5,1))
if mibBuilder.loadTexts:cpimExtMRouteNextHopEntry.setStatus(_A)
class _CpimExtMRouteNextHopAssertWinner_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CpimExtMRouteNextHopAssertWinner_Type.__name__=_G
_CpimExtMRouteNextHopAssertWinner_Object=MibTableColumn
cpimExtMRouteNextHopAssertWinner=_CpimExtMRouteNextHopAssertWinner_Object((1,3,6,1,4,1,9,10,120,1,1,5,1,1),_CpimExtMRouteNextHopAssertWinner_Type())
cpimExtMRouteNextHopAssertWinner.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtMRouteNextHopAssertWinner.setStatus(_A)
_CpimExtMRouteNextHopAssertTimer_Type=TimeTicks
_CpimExtMRouteNextHopAssertTimer_Object=MibTableColumn
cpimExtMRouteNextHopAssertTimer=_CpimExtMRouteNextHopAssertTimer_Object((1,3,6,1,4,1,9,10,120,1,1,5,1,2),_CpimExtMRouteNextHopAssertTimer_Type())
cpimExtMRouteNextHopAssertTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtMRouteNextHopAssertTimer.setStatus(_A)
class _CpimExtMRouteNextHopAssertMetric_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpimExtMRouteNextHopAssertMetric_Type.__name__=_D
_CpimExtMRouteNextHopAssertMetric_Object=MibTableColumn
cpimExtMRouteNextHopAssertMetric=_CpimExtMRouteNextHopAssertMetric_Object((1,3,6,1,4,1,9,10,120,1,1,5,1,3),_CpimExtMRouteNextHopAssertMetric_Type())
cpimExtMRouteNextHopAssertMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtMRouteNextHopAssertMetric.setStatus(_A)
class _CpimExtMRouteNextHopAsrtMtrcPref_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpimExtMRouteNextHopAsrtMtrcPref_Type.__name__=_D
_CpimExtMRouteNextHopAsrtMtrcPref_Object=MibTableColumn
cpimExtMRouteNextHopAsrtMtrcPref=_CpimExtMRouteNextHopAsrtMtrcPref_Object((1,3,6,1,4,1,9,10,120,1,1,5,1,4),_CpimExtMRouteNextHopAsrtMtrcPref_Type())
cpimExtMRouteNextHopAsrtMtrcPref.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtMRouteNextHopAsrtMtrcPref.setStatus(_A)
_CpimExtMRouteNextHopJoinPruneTmr_Type=TimeTicks
_CpimExtMRouteNextHopJoinPruneTmr_Object=MibTableColumn
cpimExtMRouteNextHopJoinPruneTmr=_CpimExtMRouteNextHopJoinPruneTmr_Object((1,3,6,1,4,1,9,10,120,1,1,5,1,5),_CpimExtMRouteNextHopJoinPruneTmr_Type())
cpimExtMRouteNextHopJoinPruneTmr.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtMRouteNextHopJoinPruneTmr.setStatus(_A)
_CpimExtBidirDFTable_Object=MibTable
cpimExtBidirDFTable=_CpimExtBidirDFTable_Object((1,3,6,1,4,1,9,10,120,1,1,6))
if mibBuilder.loadTexts:cpimExtBidirDFTable.setStatus(_A)
_CpimExtBidirDFEntry_Object=MibTableRow
cpimExtBidirDFEntry=_CpimExtBidirDFEntry_Object((1,3,6,1,4,1,9,10,120,1,1,6,1))
cpimExtBidirDFEntry.setIndexNames((0,_B,_a),(0,_B,_b),(0,_B,_c))
if mibBuilder.loadTexts:cpimExtBidirDFEntry.setStatus(_A)
_CpimExtBidirDFIfIndex_Type=InterfaceIndex
_CpimExtBidirDFIfIndex_Object=MibTableColumn
cpimExtBidirDFIfIndex=_CpimExtBidirDFIfIndex_Object((1,3,6,1,4,1,9,10,120,1,1,6,1,1),_CpimExtBidirDFIfIndex_Type())
cpimExtBidirDFIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cpimExtBidirDFIfIndex.setStatus(_A)
_CpimExtBidirDFRPAddressType_Type=InetAddressType
_CpimExtBidirDFRPAddressType_Object=MibTableColumn
cpimExtBidirDFRPAddressType=_CpimExtBidirDFRPAddressType_Object((1,3,6,1,4,1,9,10,120,1,1,6,1,2),_CpimExtBidirDFRPAddressType_Type())
cpimExtBidirDFRPAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:cpimExtBidirDFRPAddressType.setStatus(_A)
class _CpimExtBidirDFRPAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CpimExtBidirDFRPAddress_Type.__name__=_G
_CpimExtBidirDFRPAddress_Object=MibTableColumn
cpimExtBidirDFRPAddress=_CpimExtBidirDFRPAddress_Object((1,3,6,1,4,1,9,10,120,1,1,6,1,3),_CpimExtBidirDFRPAddress_Type())
cpimExtBidirDFRPAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:cpimExtBidirDFRPAddress.setStatus(_A)
class _CpimExtBidirDFWinnerAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CpimExtBidirDFWinnerAddress_Type.__name__=_G
_CpimExtBidirDFWinnerAddress_Object=MibTableColumn
cpimExtBidirDFWinnerAddress=_CpimExtBidirDFWinnerAddress_Object((1,3,6,1,4,1,9,10,120,1,1,6,1,4),_CpimExtBidirDFWinnerAddress_Type())
cpimExtBidirDFWinnerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtBidirDFWinnerAddress.setStatus(_A)
_CpimExtBidirDFWinnerUptime_Type=TimeTicks
_CpimExtBidirDFWinnerUptime_Object=MibTableColumn
cpimExtBidirDFWinnerUptime=_CpimExtBidirDFWinnerUptime_Object((1,3,6,1,4,1,9,10,120,1,1,6,1,5),_CpimExtBidirDFWinnerUptime_Type())
cpimExtBidirDFWinnerUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtBidirDFWinnerUptime.setStatus(_A)
class _CpimExtBidirDFWnrMtrcPref_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpimExtBidirDFWnrMtrcPref_Type.__name__=_D
_CpimExtBidirDFWnrMtrcPref_Object=MibTableColumn
cpimExtBidirDFWnrMtrcPref=_CpimExtBidirDFWnrMtrcPref_Object((1,3,6,1,4,1,9,10,120,1,1,6,1,6),_CpimExtBidirDFWnrMtrcPref_Type())
cpimExtBidirDFWnrMtrcPref.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtBidirDFWnrMtrcPref.setStatus(_A)
class _CpimExtBidirDFWinnerMetric_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpimExtBidirDFWinnerMetric_Type.__name__=_D
_CpimExtBidirDFWinnerMetric_Object=MibTableColumn
cpimExtBidirDFWinnerMetric=_CpimExtBidirDFWinnerMetric_Object((1,3,6,1,4,1,9,10,120,1,1,6,1,7),_CpimExtBidirDFWinnerMetric_Type())
cpimExtBidirDFWinnerMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtBidirDFWinnerMetric.setStatus(_A)
class _CpimExtBidirDFState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('unknown',0),('dfOffer',1),('dfLose',2),('dfWinner',3),('dfBackoff',4)))
_CpimExtBidirDFState_Type.__name__=_M
_CpimExtBidirDFState_Object=MibTableColumn
cpimExtBidirDFState=_CpimExtBidirDFState_Object((1,3,6,1,4,1,9,10,120,1,1,6,1,8),_CpimExtBidirDFState_Type())
cpimExtBidirDFState.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtBidirDFState.setStatus(_A)
_CpimExtBidirDFStateTimer_Type=TimeTicks
_CpimExtBidirDFStateTimer_Object=MibTableColumn
cpimExtBidirDFStateTimer=_CpimExtBidirDFStateTimer_Object((1,3,6,1,4,1,9,10,120,1,1,6,1,9),_CpimExtBidirDFStateTimer_Type())
cpimExtBidirDFStateTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtBidirDFStateTimer.setStatus(_A)
_CpimExtRPSetTable_Object=MibTable
cpimExtRPSetTable=_CpimExtRPSetTable_Object((1,3,6,1,4,1,9,10,120,1,1,7))
if mibBuilder.loadTexts:cpimExtRPSetTable.setStatus(_A)
_CpimExtRPSetEntry_Object=MibTableRow
cpimExtRPSetEntry=_CpimExtRPSetEntry_Object((1,3,6,1,4,1,9,10,120,1,1,7,1))
cpimExtRPSetEntry.setIndexNames((0,_B,_d),(0,_B,_e),(0,_B,_f),(0,_B,_g),(0,_B,_h),(0,_B,_i),(0,_B,_j))
if mibBuilder.loadTexts:cpimExtRPSetEntry.setStatus(_A)
class _CpimExtRPSetComponent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CpimExtRPSetComponent_Type.__name__=_D
_CpimExtRPSetComponent_Object=MibTableColumn
cpimExtRPSetComponent=_CpimExtRPSetComponent_Object((1,3,6,1,4,1,9,10,120,1,1,7,1,1),_CpimExtRPSetComponent_Type())
cpimExtRPSetComponent.setMaxAccess(_F)
if mibBuilder.loadTexts:cpimExtRPSetComponent.setStatus(_A)
_CpimExtRPSetAddrType_Type=InetAddressType
_CpimExtRPSetAddrType_Object=MibTableColumn
cpimExtRPSetAddrType=_CpimExtRPSetAddrType_Object((1,3,6,1,4,1,9,10,120,1,1,7,1,2),_CpimExtRPSetAddrType_Type())
cpimExtRPSetAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:cpimExtRPSetAddrType.setStatus(_A)
class _CpimExtRPSetGroupAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CpimExtRPSetGroupAddress_Type.__name__=_G
_CpimExtRPSetGroupAddress_Object=MibTableColumn
cpimExtRPSetGroupAddress=_CpimExtRPSetGroupAddress_Object((1,3,6,1,4,1,9,10,120,1,1,7,1,3),_CpimExtRPSetGroupAddress_Type())
cpimExtRPSetGroupAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:cpimExtRPSetGroupAddress.setStatus(_A)
_CpimExtRPSetGroupMask_Type=InetAddressPrefixLength
_CpimExtRPSetGroupMask_Object=MibTableColumn
cpimExtRPSetGroupMask=_CpimExtRPSetGroupMask_Object((1,3,6,1,4,1,9,10,120,1,1,7,1,4),_CpimExtRPSetGroupMask_Type())
cpimExtRPSetGroupMask.setMaxAccess(_F)
if mibBuilder.loadTexts:cpimExtRPSetGroupMask.setStatus(_A)
class _CpimExtRPSetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('static',2),('bsr',3),('embedded',4),('autorp',5)))
_CpimExtRPSetType_Type.__name__=_M
_CpimExtRPSetType_Object=MibTableColumn
cpimExtRPSetType=_CpimExtRPSetType_Object((1,3,6,1,4,1,9,10,120,1,1,7,1,5),_CpimExtRPSetType_Type())
cpimExtRPSetType.setMaxAccess(_F)
if mibBuilder.loadTexts:cpimExtRPSetType.setStatus(_A)
_CpimExtRPSetProtocol_Type=IANAipMRouteProtocol
_CpimExtRPSetProtocol_Object=MibTableColumn
cpimExtRPSetProtocol=_CpimExtRPSetProtocol_Object((1,3,6,1,4,1,9,10,120,1,1,7,1,6),_CpimExtRPSetProtocol_Type())
cpimExtRPSetProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:cpimExtRPSetProtocol.setStatus(_A)
class _CpimExtRPSetAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CpimExtRPSetAddress_Type.__name__=_G
_CpimExtRPSetAddress_Object=MibTableColumn
cpimExtRPSetAddress=_CpimExtRPSetAddress_Object((1,3,6,1,4,1,9,10,120,1,1,7,1,7),_CpimExtRPSetAddress_Type())
cpimExtRPSetAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:cpimExtRPSetAddress.setStatus(_A)
class _CpimExtRPSetHoldTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpimExtRPSetHoldTime_Type.__name__=_D
_CpimExtRPSetHoldTime_Object=MibTableColumn
cpimExtRPSetHoldTime=_CpimExtRPSetHoldTime_Object((1,3,6,1,4,1,9,10,120,1,1,7,1,8),_CpimExtRPSetHoldTime_Type())
cpimExtRPSetHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtRPSetHoldTime.setStatus(_A)
if mibBuilder.loadTexts:cpimExtRPSetHoldTime.setUnits(_H)
class _CpimExtRPSetExpiryTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpimExtRPSetExpiryTime_Type.__name__=_D
_CpimExtRPSetExpiryTime_Object=MibTableColumn
cpimExtRPSetExpiryTime=_CpimExtRPSetExpiryTime_Object((1,3,6,1,4,1,9,10,120,1,1,7,1,9),_CpimExtRPSetExpiryTime_Type())
cpimExtRPSetExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtRPSetExpiryTime.setStatus(_A)
if mibBuilder.loadTexts:cpimExtRPSetExpiryTime.setUnits(_H)
class _CpimExtRPSetPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_CpimExtRPSetPriority_Type.__name__=_M
_CpimExtRPSetPriority_Object=MibTableColumn
cpimExtRPSetPriority=_CpimExtRPSetPriority_Object((1,3,6,1,4,1,9,10,120,1,1,7,1,10),_CpimExtRPSetPriority_Type())
cpimExtRPSetPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtRPSetPriority.setStatus(_A)
_CpimExtRPSetRPActive_Type=TruthValue
_CpimExtRPSetRPActive_Object=MibTableColumn
cpimExtRPSetRPActive=_CpimExtRPSetRPActive_Object((1,3,6,1,4,1,9,10,120,1,1,7,1,11),_CpimExtRPSetRPActive_Type())
cpimExtRPSetRPActive.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimExtRPSetRPActive.setStatus(_A)
_CpimExtCRPTable_Object=MibTable
cpimExtCRPTable=_CpimExtCRPTable_Object((1,3,6,1,4,1,9,10,120,1,1,8))
if mibBuilder.loadTexts:cpimExtCRPTable.setStatus(_A)
_CpimExtCRPEntry_Object=MibTableRow
cpimExtCRPEntry=_CpimExtCRPEntry_Object((1,3,6,1,4,1,9,10,120,1,1,8,1))
if mibBuilder.loadTexts:cpimExtCRPEntry.setStatus(_A)
class _CpimExtCRPBidir_Type(TruthValue):defaultValue=2
_CpimExtCRPBidir_Type.__name__=_K
_CpimExtCRPBidir_Object=MibTableColumn
cpimExtCRPBidir=_CpimExtCRPBidir_Object((1,3,6,1,4,1,9,10,120,1,1,8,1,1),_CpimExtCRPBidir_Type())
cpimExtCRPBidir.setMaxAccess(_E)
if mibBuilder.loadTexts:cpimExtCRPBidir.setStatus(_A)
class _CpimExtSourceLifetime_Type(Unsigned32):defaultValue=210;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpimExtSourceLifetime_Type.__name__=_D
_CpimExtSourceLifetime_Object=MibScalar
cpimExtSourceLifetime=_CpimExtSourceLifetime_Object((1,3,6,1,4,1,9,10,120,1,1,9),_CpimExtSourceLifetime_Type())
cpimExtSourceLifetime.setMaxAccess(_J)
if mibBuilder.loadTexts:cpimExtSourceLifetime.setStatus(_A)
if mibBuilder.loadTexts:cpimExtSourceLifetime.setUnits(_H)
class _CpimExtStateRefreshInterval_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CpimExtStateRefreshInterval_Type.__name__=_D
_CpimExtStateRefreshInterval_Object=MibScalar
cpimExtStateRefreshInterval=_CpimExtStateRefreshInterval_Object((1,3,6,1,4,1,9,10,120,1,1,10),_CpimExtStateRefreshInterval_Type())
cpimExtStateRefreshInterval.setMaxAccess(_J)
if mibBuilder.loadTexts:cpimExtStateRefreshInterval.setStatus(_A)
if mibBuilder.loadTexts:cpimExtStateRefreshInterval.setUnits(_H)
class _CpimExtStateRefreshLimitInterval_Type(TimeTicks):defaultValue=0
_CpimExtStateRefreshLimitInterval_Type.__name__=_Z
_CpimExtStateRefreshLimitInterval_Object=MibScalar
cpimExtStateRefreshLimitInterval=_CpimExtStateRefreshLimitInterval_Object((1,3,6,1,4,1,9,10,120,1,1,11),_CpimExtStateRefreshLimitInterval_Type())
cpimExtStateRefreshLimitInterval.setMaxAccess(_J)
if mibBuilder.loadTexts:cpimExtStateRefreshLimitInterval.setStatus(_A)
class _CpimExtStateRefreshTimeToLive_Type(Unsigned32):defaultValue=16;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CpimExtStateRefreshTimeToLive_Type.__name__=_D
_CpimExtStateRefreshTimeToLive_Object=MibScalar
cpimExtStateRefreshTimeToLive=_CpimExtStateRefreshTimeToLive_Object((1,3,6,1,4,1,9,10,120,1,1,12),_CpimExtStateRefreshTimeToLive_Type())
cpimExtStateRefreshTimeToLive.setMaxAccess(_J)
if mibBuilder.loadTexts:cpimExtStateRefreshTimeToLive.setStatus(_A)
class _CpimExtInterfaceStateChangeNotifEnabled_Type(TruthValue):defaultValue=2
_CpimExtInterfaceStateChangeNotifEnabled_Type.__name__=_K
_CpimExtInterfaceStateChangeNotifEnabled_Object=MibScalar
cpimExtInterfaceStateChangeNotifEnabled=_CpimExtInterfaceStateChangeNotifEnabled_Object((1,3,6,1,4,1,9,10,120,1,1,13),_CpimExtInterfaceStateChangeNotifEnabled_Type())
cpimExtInterfaceStateChangeNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:cpimExtInterfaceStateChangeNotifEnabled.setStatus(_A)
class _CpimExtRPMappingChangeNotifEnabled_Type(TruthValue):defaultValue=2
_CpimExtRPMappingChangeNotifEnabled_Type.__name__=_K
_CpimExtRPMappingChangeNotifEnabled_Object=MibScalar
cpimExtRPMappingChangeNotifEnabled=_CpimExtRPMappingChangeNotifEnabled_Object((1,3,6,1,4,1,9,10,120,1,1,14),_CpimExtRPMappingChangeNotifEnabled_Type())
cpimExtRPMappingChangeNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:cpimExtRPMappingChangeNotifEnabled.setStatus(_A)
_CiscoIetfPimExtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoIetfPimExtMIBConformance=_CiscoIetfPimExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,120,2))
_CiscoIetfPimExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIetfPimExtMIBCompliances=_CiscoIetfPimExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,120,2,1))
_CiscoIetfPimExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIetfPimExtMIBGroups=_CiscoIetfPimExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,120,2,2))
cPimIfEntry.registerAugmentions((_B,_k))
cpimExtIfEntry.setIndexNames(*cPimIfEntry.getIndexNames())
cPimNbrEntry.registerAugmentions((_B,_l))
cpimExtNbrEntry.setIndexNames(*cPimNbrEntry.getIndexNames())
cPimInetMRouteEntry.registerAugmentions((_B,_m))
cpimExtMRouteEntry.setIndexNames(*cPimInetMRouteEntry.getIndexNames())
cPimInetMRouteNextHopEntry.registerAugmentions((_B,_n))
cpimExtMRouteNextHopEntry.setIndexNames(*cPimInetMRouteNextHopEntry.getIndexNames())
cPimCRPEntry.registerAugmentions((_B,_o))
cpimExtCRPEntry.setIndexNames(*cPimCRPEntry.getIndexNames())
ciscoIetfPimExtGeneralGroup=ObjectGroup((1,3,6,1,4,1,9,10,120,2,2,1))
ciscoIetfPimExtGeneralGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_P),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:ciscoIetfPimExtGeneralGroup.setStatus(_A)
ciscoIetfPimExtNbrGroup=ObjectGroup((1,3,6,1,4,1,9,10,120,2,2,2))
ciscoIetfPimExtNbrGroup.setObjects(*((_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_O),(_B,_AK)))
if mibBuilder.loadTexts:ciscoIetfPimExtNbrGroup.setStatus(_A)
ciscoIetfPimExtNextHopGroup=ObjectGroup((1,3,6,1,4,1,9,10,120,2,2,3))
ciscoIetfPimExtNextHopGroup.setObjects(*((_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:ciscoIetfPimExtNextHopGroup.setStatus(_A)
ciscoIetfPimExtBidirGroup=ObjectGroup((1,3,6,1,4,1,9,10,120,2,2,4))
ciscoIetfPimExtBidirGroup.setObjects(*((_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:ciscoIetfPimExtBidirGroup.setStatus(_A)
ciscoIetfPimExtNotifEnabledGroup=ObjectGroup((1,3,6,1,4,1,9,10,120,2,2,6))
ciscoIetfPimExtNotifEnabledGroup.setObjects(*((_B,_Aa),(_B,_Ab)))
if mibBuilder.loadTexts:ciscoIetfPimExtNotifEnabledGroup.setStatus(_A)
ciscoIetfPimExtInterfaceUp=NotificationType((1,3,6,1,4,1,9,10,120,0,1))
ciscoIetfPimExtInterfaceUp.setObjects((_I,_N))
if mibBuilder.loadTexts:ciscoIetfPimExtInterfaceUp.setStatus(_A)
ciscoIetfPimExtInterfaceDown=NotificationType((1,3,6,1,4,1,9,10,120,0,2))
ciscoIetfPimExtInterfaceDown.setObjects((_I,_N))
if mibBuilder.loadTexts:ciscoIetfPimExtInterfaceDown.setStatus(_A)
ciscoIetfPimExtRPMappingChange=NotificationType((1,3,6,1,4,1,9,10,120,0,3))
ciscoIetfPimExtRPMappingChange.setObjects(*((_B,_P),(_X,_Y)))
if mibBuilder.loadTexts:ciscoIetfPimExtRPMappingChange.setStatus(_A)
ciscoIetfPimExtNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,10,120,2,2,5))
ciscoIetfPimExtNotificationGroup.setObjects(*((_B,_Ac),(_B,_Ad),(_B,_Ae)))
if mibBuilder.loadTexts:ciscoIetfPimExtNotificationGroup.setStatus(_A)
ciscoIetfPimExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,120,2,1,1))
ciscoIetfPimExtMIBCompliance.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ciscoIetfPimExtMIBCompliance.setStatus('deprecated')
ciscoIetfPimExtMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,10,120,2,1,2))
ciscoIetfPimExtMIBComplianceRev1.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_Af),(_B,_Ag)))
if mibBuilder.loadTexts:ciscoIetfPimExtMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIetfPimExtMIB':ciscoIetfPimExtMIB,'ciscoIetfPimExtNotifs':ciscoIetfPimExtNotifs,_Ac:ciscoIetfPimExtInterfaceUp,_Ad:ciscoIetfPimExtInterfaceDown,_Ae:ciscoIetfPimExtRPMappingChange,'ciscoIetfPimExtMIBObjects':ciscoIetfPimExtMIBObjects,'ciscoPimExt':ciscoPimExt,'cpimExtIfTable':cpimExtIfTable,_k:cpimExtIfEntry,_p:cpimExtIfTrigHelloInterval,_q:cpimExtIfHelloHoldtime,_r:cpimExtIfLanPruneDelay,_s:cpimExtIfPropagationDelay,_t:cpimExtIfOverrideInterval,_u:cpimExtIfGenerationID,_v:cpimExtIfJoinPruneHoldtime,_w:cpimExtIfGraftRetryInterval,_x:cpimExtIfMaxGraftRetries,_y:cpimExtIfSRTTLThreshold,_z:cpimExtIfLanDelayEnabled,_A0:cpimExtIfSRCapable,_A1:cpimExtIfDRPriority,_AW:cpimExtIfBidirCapable,_A2:cpimExtIfBSRBorder,'cpimExtNbrTable':cpimExtNbrTable,_l:cpimExtNbrEntry,_AD:cpimExtNbrLANPruneDelay,_AE:cpimExtNbrOverrideInterval,_AF:cpimExtNbrTBit,_AG:cpimExtNbrSRCapable,_AH:cpimExtNbrGenId,_AX:cpimExtNbrBidirCapable,_AI:cpimExtNbrDRPresent,_AJ:cpimExtNbrDRPriority,'cpimExtNbrSecAddressTable':cpimExtNbrSecAddressTable,'cpimExtNbrSecAddressEntry':cpimExtNbrSecAddressEntry,_O:cpimExtNbrSecAddress,_AK:cpimExtNbrSecMask,'cpimExtMRouteTable':cpimExtMRouteTable,_m:cpimExtMRouteEntry,_A3:cpimExtMRouteRPFNeighbor,_A4:cpimExtMRouteSourceTimer,_A5:cpimExtMRouteOriginatorSRTTL,_AY:cpimExtMRouteBidirGroup,'cpimExtMRouteNextHopTable':cpimExtMRouteNextHopTable,_n:cpimExtMRouteNextHopEntry,_AL:cpimExtMRouteNextHopAssertWinner,_AM:cpimExtMRouteNextHopAssertTimer,_AN:cpimExtMRouteNextHopAssertMetric,_AO:cpimExtMRouteNextHopAsrtMtrcPref,_AP:cpimExtMRouteNextHopJoinPruneTmr,'cpimExtBidirDFTable':cpimExtBidirDFTable,'cpimExtBidirDFEntry':cpimExtBidirDFEntry,_c:cpimExtBidirDFIfIndex,_a:cpimExtBidirDFRPAddressType,_b:cpimExtBidirDFRPAddress,_AQ:cpimExtBidirDFWinnerAddress,_AR:cpimExtBidirDFWinnerUptime,_AS:cpimExtBidirDFWnrMtrcPref,_AT:cpimExtBidirDFWinnerMetric,_AU:cpimExtBidirDFState,_AV:cpimExtBidirDFStateTimer,'cpimExtRPSetTable':cpimExtRPSetTable,'cpimExtRPSetEntry':cpimExtRPSetEntry,_d:cpimExtRPSetComponent,_e:cpimExtRPSetAddrType,_f:cpimExtRPSetGroupAddress,_g:cpimExtRPSetGroupMask,_h:cpimExtRPSetType,_i:cpimExtRPSetProtocol,_j:cpimExtRPSetAddress,_P:cpimExtRPSetHoldTime,_A6:cpimExtRPSetExpiryTime,_A7:cpimExtRPSetPriority,_A8:cpimExtRPSetRPActive,'cpimExtCRPTable':cpimExtCRPTable,_o:cpimExtCRPEntry,_AZ:cpimExtCRPBidir,_A9:cpimExtSourceLifetime,_AA:cpimExtStateRefreshInterval,_AB:cpimExtStateRefreshLimitInterval,_AC:cpimExtStateRefreshTimeToLive,_Aa:cpimExtInterfaceStateChangeNotifEnabled,_Ab:cpimExtRPMappingChangeNotifEnabled,'ciscoIetfPimExtMIBConformance':ciscoIetfPimExtMIBConformance,'ciscoIetfPimExtMIBCompliances':ciscoIetfPimExtMIBCompliances,'ciscoIetfPimExtMIBCompliance':ciscoIetfPimExtMIBCompliance,'ciscoIetfPimExtMIBComplianceRev1':ciscoIetfPimExtMIBComplianceRev1,'ciscoIetfPimExtMIBGroups':ciscoIetfPimExtMIBGroups,_Q:ciscoIetfPimExtGeneralGroup,_R:ciscoIetfPimExtNbrGroup,_S:ciscoIetfPimExtNextHopGroup,_T:ciscoIetfPimExtBidirGroup,_Af:ciscoIetfPimExtNotificationGroup,_Ag:ciscoIetfPimExtNotifEnabledGroup})