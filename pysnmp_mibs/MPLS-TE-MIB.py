_A_='mplsTunnelOptionalGroup'
_Az='mplsTunnelIsIntfcGroup'
_Ay='mplsTunnelIsNotIntfcGroup'
_Ax='mplsTunnelSignaledGroup'
_Aw='mplsTunnelManualGroup'
_Av='mplsTunnelScalarGroup'
_Au='mplsTunnelGroup'
_At='mplsTunnelRerouted'
_As='mplsTunnelDown'
_Ar='mplsTunnelUp'
_Aq='mplsTunnelCHopType'
_Ap='mplsTunnelCHopAsNumber'
_Ao='mplsTunnelCHopIpv6PrefixLen'
_An='mplsTunnelCHopIpv6Addr'
_Am='mplsTunnelCHopIpv4PrefixLen'
_Al='mplsTunnelCHopIpv4Addr'
_Ak='mplsTunnelCHopAddrType'
_Aj='mplsTunnelARHopType'
_Ai='mplsTunnelARHopAsNumber'
_Ah='mplsTunnelARHopIpv6PrefixLen'
_Ag='mplsTunnelARHopIpv6Addr'
_Af='mplsTunnelARHopIpv4PrefixLen'
_Ae='mplsTunnelARHopIpv4Addr'
_Ad='mplsTunnelARHopAddrType'
_Ac='mplsTunnelResourceStorageType'
_Ab='mplsTunnelResourceRowStatus'
_Aa='mplsTunnelResourceMaxBurstSize'
_AZ='mplsTunnelResourceMeanRate'
_AY='mplsTunnelResourceMaxRate'
_AX='mplsTunnelResourceIndexNext'
_AW='mplsTunnelMaxHops'
_AV='mplsTunnelTEDistProto'
_AU='mplsTunnelHopStorageType'
_AT='mplsTunnelHopRowStatus'
_AS='mplsTunnelHopType'
_AR='mplsTunnelHopLspId'
_AQ='mplsTunnelHopAsNumber'
_AP='mplsTunnelHopIpv6PrefixLen'
_AO='mplsTunnelHopIpv6Addr'
_AN='mplsTunnelHopIpv4PrefixLen'
_AM='mplsTunnelHopIpv4Addr'
_AL='mplsTunnelHopAddrType'
_AK='mplsTunnelHopListIndexNext'
_AJ='mplsTunnelSessionAttributes'
_AI='mplsTunnelLocalProtectInUse'
_AH='mplsTunnelHoldingPrio'
_AG='mplsTunnelSetupPrio'
_AF='mplsTunnelInstanceUpTime'
_AE='mplsTunnelTotalUpTime'
_AD='mplsTunnelRole'
_AC='mplsTunnelPathInUse'
_AB='mplsTunnelInstancePriority'
_AA='mplsTunnelResourcePointer'
_A9='mplsTunnelPerfHCBytes'
_A8='mplsTunnelPerfBytes'
_A7='mplsTunnelPerfErrors'
_A6='mplsTunnelPerfHCPackets'
_A5='mplsTunnelPerfPackets'
_A4='mplsTunnelExcludeAllAffinity'
_A3='mplsTunnelIncludeAllAffinity'
_A2='mplsTunnelIncludeAnyAffinity'
_A1='mplsTunnelStateTransitions'
_A0='mplsTunnelCreationTime'
_z='mplsTunnelLastPathChange'
_y='mplsTunnelPathChanges'
_x='mplsTunnelPrimaryTimeUp'
_w='mplsTunnelPrimaryInstance'
_v='mplsTunnelStorageType'
_u='mplsTunnelTrapEnable'
_t='mplsTunnelRowStatus'
_s='mplsTunnelCHopTableIndex'
_r='mplsTunnelARHopTableIndex'
_q='mplsTunnelHopTableIndex'
_p='mplsTunnelIfIndex'
_o='mplsTunnelXCPointer'
_n='mplsTunnelOwner'
_m='mplsTunnelDescr'
_l='mplsTunnelName'
_k='mplsTunnelIndexNext'
_j='mplsTunnelPerfEntry'
_i='mplsTunnelCHopIndex'
_h='mplsTunnelCHopListIndex'
_g='mplsTunnelARHopIndex'
_f='mplsTunnelARHopListIndex'
_e='bits per second'
_d='mplsTunnelResourceIndex'
_c='mplsTunnelHopIndex'
_b='mplsPathOptionIndex'
_a='mplsTunnelHopListIndex'
_Z='testing'
_Y='mplsTunnelIngressLSRId'
_X='mplsTunnelInstance'
_W='mplsTunnelIndex'
_V='mplsTunnelIsIf'
_U='mplsTunnelSignallingProto'
_T='mplsTunnelActive'
_S='mplsTunnelConfigured'
_R='loose'
_Q='strict'
_P='asNumber'
_O='ipV6'
_N='ipV4'
_M='mplsTunnelEgressLSRId'
_L='other'
_K='TruthValue'
_J='Bits'
_I='mplsTunnelOperStatus'
_H='mplsTunnelAdminStatus'
_G='not-accessible'
_F='Integer32'
_E='Unsigned32'
_D='read-only'
_C='read-create'
_B='MPLS-TE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
MplsBitRate,MplsBurstSize,MplsLSPID=mibBuilder.importSymbols('MPLS-LSR-MIB','MplsBitRate','MplsBurstSize','MplsLSPID')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI',_J,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'experimental','iso')
DisplayString,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','StorageType','TextualConvention','TimeStamp',_K)
mplsTeMIB=ModuleIdentity((1,3,6,1,3,95))
if mibBuilder.loadTexts:mplsTeMIB.setRevisions(('2000-11-21 12:00','2000-07-14 12:00','2000-05-26 12:00','2000-03-03 12:00','1999-07-16 12:00'))
class MplsTunnelIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class MplsTunnelInstanceIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class MplsLsrId(TextualConvention,Unsigned32):status=_A
class MplsPathIndex(TextualConvention,Unsigned32):status=_A
class MplsPathIndexOrZero(TextualConvention,Unsigned32):status=_A
_MplsTeScalars_ObjectIdentity=ObjectIdentity
mplsTeScalars=_MplsTeScalars_ObjectIdentity((1,3,6,1,3,95,1))
_MplsTunnelConfigured_Type=Unsigned32
_MplsTunnelConfigured_Object=MibScalar
mplsTunnelConfigured=_MplsTunnelConfigured_Object((1,3,6,1,3,95,1,1),_MplsTunnelConfigured_Type())
mplsTunnelConfigured.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelConfigured.setStatus(_A)
_MplsTunnelActive_Type=Unsigned32
_MplsTunnelActive_Object=MibScalar
mplsTunnelActive=_MplsTunnelActive_Object((1,3,6,1,3,95,1,2),_MplsTunnelActive_Type())
mplsTunnelActive.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelActive.setStatus(_A)
class _MplsTunnelTEDistProto_Type(Bits):namedValues=NamedValues(*((_L,0),('ospf',1),('isis',2)))
_MplsTunnelTEDistProto_Type.__name__=_J
_MplsTunnelTEDistProto_Object=MibScalar
mplsTunnelTEDistProto=_MplsTunnelTEDistProto_Object((1,3,6,1,3,95,1,3),_MplsTunnelTEDistProto_Type())
mplsTunnelTEDistProto.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelTEDistProto.setStatus(_A)
_MplsTunnelMaxHops_Type=Unsigned32
_MplsTunnelMaxHops_Object=MibScalar
mplsTunnelMaxHops=_MplsTunnelMaxHops_Object((1,3,6,1,3,95,1,4),_MplsTunnelMaxHops_Type())
mplsTunnelMaxHops.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelMaxHops.setStatus(_A)
_MplsTeObjects_ObjectIdentity=ObjectIdentity
mplsTeObjects=_MplsTeObjects_ObjectIdentity((1,3,6,1,3,95,2))
class _MplsTunnelIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MplsTunnelIndexNext_Type.__name__=_F
_MplsTunnelIndexNext_Object=MibScalar
mplsTunnelIndexNext=_MplsTunnelIndexNext_Object((1,3,6,1,3,95,2,1),_MplsTunnelIndexNext_Type())
mplsTunnelIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelIndexNext.setStatus(_A)
_MplsTunnelTable_Object=MibTable
mplsTunnelTable=_MplsTunnelTable_Object((1,3,6,1,3,95,2,2))
if mibBuilder.loadTexts:mplsTunnelTable.setStatus(_A)
_MplsTunnelEntry_Object=MibTableRow
mplsTunnelEntry=_MplsTunnelEntry_Object((1,3,6,1,3,95,2,2,1))
mplsTunnelEntry.setIndexNames((0,_B,_W),(0,_B,_X),(0,_B,_Y),(0,_B,_M))
if mibBuilder.loadTexts:mplsTunnelEntry.setStatus(_A)
_MplsTunnelIndex_Type=MplsTunnelIndex
_MplsTunnelIndex_Object=MibTableColumn
mplsTunnelIndex=_MplsTunnelIndex_Object((1,3,6,1,3,95,2,2,1,1),_MplsTunnelIndex_Type())
mplsTunnelIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mplsTunnelIndex.setStatus(_A)
_MplsTunnelInstance_Type=MplsTunnelInstanceIndex
_MplsTunnelInstance_Object=MibTableColumn
mplsTunnelInstance=_MplsTunnelInstance_Object((1,3,6,1,3,95,2,2,1,2),_MplsTunnelInstance_Type())
mplsTunnelInstance.setMaxAccess(_G)
if mibBuilder.loadTexts:mplsTunnelInstance.setStatus(_A)
_MplsTunnelIngressLSRId_Type=MplsLsrId
_MplsTunnelIngressLSRId_Object=MibTableColumn
mplsTunnelIngressLSRId=_MplsTunnelIngressLSRId_Object((1,3,6,1,3,95,2,2,1,3),_MplsTunnelIngressLSRId_Type())
mplsTunnelIngressLSRId.setMaxAccess(_G)
if mibBuilder.loadTexts:mplsTunnelIngressLSRId.setStatus(_A)
_MplsTunnelEgressLSRId_Type=MplsLsrId
_MplsTunnelEgressLSRId_Object=MibTableColumn
mplsTunnelEgressLSRId=_MplsTunnelEgressLSRId_Object((1,3,6,1,3,95,2,2,1,4),_MplsTunnelEgressLSRId_Type())
mplsTunnelEgressLSRId.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelEgressLSRId.setStatus(_A)
_MplsTunnelName_Type=DisplayString
_MplsTunnelName_Object=MibTableColumn
mplsTunnelName=_MplsTunnelName_Object((1,3,6,1,3,95,2,2,1,5),_MplsTunnelName_Type())
mplsTunnelName.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelName.setStatus(_A)
_MplsTunnelDescr_Type=DisplayString
_MplsTunnelDescr_Object=MibTableColumn
mplsTunnelDescr=_MplsTunnelDescr_Object((1,3,6,1,3,95,2,2,1,6),_MplsTunnelDescr_Type())
mplsTunnelDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelDescr.setStatus(_A)
class _MplsTunnelIsIf_Type(TruthValue):defaultValue=2
_MplsTunnelIsIf_Type.__name__=_K
_MplsTunnelIsIf_Object=MibTableColumn
mplsTunnelIsIf=_MplsTunnelIsIf_Object((1,3,6,1,3,95,2,2,1,7),_MplsTunnelIsIf_Type())
mplsTunnelIsIf.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelIsIf.setStatus(_A)
_MplsTunnelIfIndex_Type=InterfaceIndexOrZero
_MplsTunnelIfIndex_Object=MibTableColumn
mplsTunnelIfIndex=_MplsTunnelIfIndex_Object((1,3,6,1,3,95,2,2,1,8),_MplsTunnelIfIndex_Type())
mplsTunnelIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelIfIndex.setStatus(_A)
_MplsTunnelXCPointer_Type=RowPointer
_MplsTunnelXCPointer_Object=MibTableColumn
mplsTunnelXCPointer=_MplsTunnelXCPointer_Object((1,3,6,1,3,95,2,2,1,9),_MplsTunnelXCPointer_Type())
mplsTunnelXCPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelXCPointer.setStatus(_A)
class _MplsTunnelSignallingProto_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('rsvp',2),('crldp',3),(_L,4)))
_MplsTunnelSignallingProto_Type.__name__=_F
_MplsTunnelSignallingProto_Object=MibTableColumn
mplsTunnelSignallingProto=_MplsTunnelSignallingProto_Object((1,3,6,1,3,95,2,2,1,10),_MplsTunnelSignallingProto_Type())
mplsTunnelSignallingProto.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelSignallingProto.setStatus(_A)
class _MplsTunnelSetupPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MplsTunnelSetupPrio_Type.__name__=_F
_MplsTunnelSetupPrio_Object=MibTableColumn
mplsTunnelSetupPrio=_MplsTunnelSetupPrio_Object((1,3,6,1,3,95,2,2,1,11),_MplsTunnelSetupPrio_Type())
mplsTunnelSetupPrio.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelSetupPrio.setStatus(_A)
class _MplsTunnelHoldingPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MplsTunnelHoldingPrio_Type.__name__=_F
_MplsTunnelHoldingPrio_Object=MibTableColumn
mplsTunnelHoldingPrio=_MplsTunnelHoldingPrio_Object((1,3,6,1,3,95,2,2,1,12),_MplsTunnelHoldingPrio_Type())
mplsTunnelHoldingPrio.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelHoldingPrio.setStatus(_A)
class _MplsTunnelSessionAttributes_Type(Bits):namedValues=NamedValues(*(('fastReroute',0),('mergingPermitted',1),('isPersistent',2),('isPinned',3),('isComputed',4),('recordRoute',5)))
_MplsTunnelSessionAttributes_Type.__name__=_J
_MplsTunnelSessionAttributes_Object=MibTableColumn
mplsTunnelSessionAttributes=_MplsTunnelSessionAttributes_Object((1,3,6,1,3,95,2,2,1,13),_MplsTunnelSessionAttributes_Type())
mplsTunnelSessionAttributes.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelSessionAttributes.setStatus(_A)
class _MplsTunnelOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('admin',1),('rsvp',2),('crldp',3),('policyAgent',4),(_L,5)))
_MplsTunnelOwner_Type.__name__=_F
_MplsTunnelOwner_Object=MibTableColumn
mplsTunnelOwner=_MplsTunnelOwner_Object((1,3,6,1,3,95,2,2,1,14),_MplsTunnelOwner_Type())
mplsTunnelOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelOwner.setStatus(_A)
_MplsTunnelLocalProtectInUse_Type=TruthValue
_MplsTunnelLocalProtectInUse_Object=MibTableColumn
mplsTunnelLocalProtectInUse=_MplsTunnelLocalProtectInUse_Object((1,3,6,1,3,95,2,2,1,15),_MplsTunnelLocalProtectInUse_Type())
mplsTunnelLocalProtectInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelLocalProtectInUse.setStatus(_A)
_MplsTunnelResourcePointer_Type=RowPointer
_MplsTunnelResourcePointer_Object=MibTableColumn
mplsTunnelResourcePointer=_MplsTunnelResourcePointer_Object((1,3,6,1,3,95,2,2,1,16),_MplsTunnelResourcePointer_Type())
mplsTunnelResourcePointer.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelResourcePointer.setStatus(_A)
class _MplsTunnelInstancePriority_Type(Unsigned32):defaultValue=0
_MplsTunnelInstancePriority_Type.__name__=_E
_MplsTunnelInstancePriority_Object=MibTableColumn
mplsTunnelInstancePriority=_MplsTunnelInstancePriority_Object((1,3,6,1,3,95,2,2,1,17),_MplsTunnelInstancePriority_Type())
mplsTunnelInstancePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelInstancePriority.setStatus(_A)
_MplsTunnelHopTableIndex_Type=MplsPathIndexOrZero
_MplsTunnelHopTableIndex_Object=MibTableColumn
mplsTunnelHopTableIndex=_MplsTunnelHopTableIndex_Object((1,3,6,1,3,95,2,2,1,18),_MplsTunnelHopTableIndex_Type())
mplsTunnelHopTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelHopTableIndex.setStatus(_A)
_MplsTunnelARHopTableIndex_Type=MplsPathIndexOrZero
_MplsTunnelARHopTableIndex_Object=MibTableColumn
mplsTunnelARHopTableIndex=_MplsTunnelARHopTableIndex_Object((1,3,6,1,3,95,2,2,1,19),_MplsTunnelARHopTableIndex_Type())
mplsTunnelARHopTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelARHopTableIndex.setStatus(_A)
_MplsTunnelCHopTableIndex_Type=MplsPathIndexOrZero
_MplsTunnelCHopTableIndex_Object=MibTableColumn
mplsTunnelCHopTableIndex=_MplsTunnelCHopTableIndex_Object((1,3,6,1,3,95,2,2,1,20),_MplsTunnelCHopTableIndex_Type())
mplsTunnelCHopTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelCHopTableIndex.setStatus(_A)
_MplsTunnelPrimaryInstance_Type=MplsTunnelInstanceIndex
_MplsTunnelPrimaryInstance_Object=MibTableColumn
mplsTunnelPrimaryInstance=_MplsTunnelPrimaryInstance_Object((1,3,6,1,3,95,2,2,1,21),_MplsTunnelPrimaryInstance_Type())
mplsTunnelPrimaryInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelPrimaryInstance.setStatus(_A)
_MplsTunnelPrimaryTimeUp_Type=TimeTicks
_MplsTunnelPrimaryTimeUp_Object=MibTableColumn
mplsTunnelPrimaryTimeUp=_MplsTunnelPrimaryTimeUp_Object((1,3,6,1,3,95,2,2,1,22),_MplsTunnelPrimaryTimeUp_Type())
mplsTunnelPrimaryTimeUp.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelPrimaryTimeUp.setStatus(_A)
_MplsTunnelPathChanges_Type=Counter32
_MplsTunnelPathChanges_Object=MibTableColumn
mplsTunnelPathChanges=_MplsTunnelPathChanges_Object((1,3,6,1,3,95,2,2,1,23),_MplsTunnelPathChanges_Type())
mplsTunnelPathChanges.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelPathChanges.setStatus(_A)
_MplsTunnelLastPathChange_Type=TimeTicks
_MplsTunnelLastPathChange_Object=MibTableColumn
mplsTunnelLastPathChange=_MplsTunnelLastPathChange_Object((1,3,6,1,3,95,2,2,1,24),_MplsTunnelLastPathChange_Type())
mplsTunnelLastPathChange.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelLastPathChange.setStatus(_A)
_MplsTunnelCreationTime_Type=TimeStamp
_MplsTunnelCreationTime_Object=MibTableColumn
mplsTunnelCreationTime=_MplsTunnelCreationTime_Object((1,3,6,1,3,95,2,2,1,25),_MplsTunnelCreationTime_Type())
mplsTunnelCreationTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelCreationTime.setStatus(_A)
_MplsTunnelStateTransitions_Type=Counter32
_MplsTunnelStateTransitions_Object=MibTableColumn
mplsTunnelStateTransitions=_MplsTunnelStateTransitions_Object((1,3,6,1,3,95,2,2,1,26),_MplsTunnelStateTransitions_Type())
mplsTunnelStateTransitions.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelStateTransitions.setStatus(_A)
_MplsTunnelIncludeAnyAffinity_Type=Unsigned32
_MplsTunnelIncludeAnyAffinity_Object=MibTableColumn
mplsTunnelIncludeAnyAffinity=_MplsTunnelIncludeAnyAffinity_Object((1,3,6,1,3,95,2,2,1,27),_MplsTunnelIncludeAnyAffinity_Type())
mplsTunnelIncludeAnyAffinity.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelIncludeAnyAffinity.setStatus(_A)
_MplsTunnelIncludeAllAffinity_Type=Unsigned32
_MplsTunnelIncludeAllAffinity_Object=MibTableColumn
mplsTunnelIncludeAllAffinity=_MplsTunnelIncludeAllAffinity_Object((1,3,6,1,3,95,2,2,1,28),_MplsTunnelIncludeAllAffinity_Type())
mplsTunnelIncludeAllAffinity.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelIncludeAllAffinity.setStatus(_A)
_MplsTunnelExcludeAllAffinity_Type=Unsigned32
_MplsTunnelExcludeAllAffinity_Object=MibTableColumn
mplsTunnelExcludeAllAffinity=_MplsTunnelExcludeAllAffinity_Object((1,3,6,1,3,95,2,2,1,29),_MplsTunnelExcludeAllAffinity_Type())
mplsTunnelExcludeAllAffinity.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelExcludeAllAffinity.setStatus(_A)
_MplsTunnelPathInUse_Type=MplsPathIndexOrZero
_MplsTunnelPathInUse_Object=MibTableColumn
mplsTunnelPathInUse=_MplsTunnelPathInUse_Object((1,3,6,1,3,95,2,2,1,30),_MplsTunnelPathInUse_Type())
mplsTunnelPathInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelPathInUse.setStatus(_A)
class _MplsTunnelRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('head',1),('transit',2),('tail',3)))
_MplsTunnelRole_Type.__name__=_F
_MplsTunnelRole_Object=MibTableColumn
mplsTunnelRole=_MplsTunnelRole_Object((1,3,6,1,3,95,2,2,1,31),_MplsTunnelRole_Type())
mplsTunnelRole.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelRole.setStatus(_A)
_MplsTunnelTotalUpTime_Type=TimeTicks
_MplsTunnelTotalUpTime_Object=MibTableColumn
mplsTunnelTotalUpTime=_MplsTunnelTotalUpTime_Object((1,3,6,1,3,95,2,2,1,32),_MplsTunnelTotalUpTime_Type())
mplsTunnelTotalUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelTotalUpTime.setStatus(_A)
_MplsTunnelInstanceUpTime_Type=TimeTicks
_MplsTunnelInstanceUpTime_Object=MibTableColumn
mplsTunnelInstanceUpTime=_MplsTunnelInstanceUpTime_Object((1,3,6,1,3,95,2,2,1,33),_MplsTunnelInstanceUpTime_Type())
mplsTunnelInstanceUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelInstanceUpTime.setStatus(_A)
class _MplsTunnelAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_Z,3)))
_MplsTunnelAdminStatus_Type.__name__=_F
_MplsTunnelAdminStatus_Object=MibTableColumn
mplsTunnelAdminStatus=_MplsTunnelAdminStatus_Object((1,3,6,1,3,95,2,2,1,34),_MplsTunnelAdminStatus_Type())
mplsTunnelAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelAdminStatus.setStatus(_A)
class _MplsTunnelOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),('down',2),(_Z,3),('unknown',4),('dormant',5),('notPresent',6),('lowerLayerDown',7)))
_MplsTunnelOperStatus_Type.__name__=_F
_MplsTunnelOperStatus_Object=MibTableColumn
mplsTunnelOperStatus=_MplsTunnelOperStatus_Object((1,3,6,1,3,95,2,2,1,35),_MplsTunnelOperStatus_Type())
mplsTunnelOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelOperStatus.setStatus(_A)
_MplsTunnelRowStatus_Type=RowStatus
_MplsTunnelRowStatus_Object=MibTableColumn
mplsTunnelRowStatus=_MplsTunnelRowStatus_Object((1,3,6,1,3,95,2,2,1,36),_MplsTunnelRowStatus_Type())
mplsTunnelRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelRowStatus.setStatus(_A)
_MplsTunnelStorageType_Type=StorageType
_MplsTunnelStorageType_Object=MibTableColumn
mplsTunnelStorageType=_MplsTunnelStorageType_Object((1,3,6,1,3,95,2,2,1,37),_MplsTunnelStorageType_Type())
mplsTunnelStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelStorageType.setStatus(_A)
class _MplsTunnelHopListIndexNext_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsTunnelHopListIndexNext_Type.__name__=_E
_MplsTunnelHopListIndexNext_Object=MibScalar
mplsTunnelHopListIndexNext=_MplsTunnelHopListIndexNext_Object((1,3,6,1,3,95,2,3),_MplsTunnelHopListIndexNext_Type())
mplsTunnelHopListIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelHopListIndexNext.setStatus(_A)
_MplsTunnelHopTable_Object=MibTable
mplsTunnelHopTable=_MplsTunnelHopTable_Object((1,3,6,1,3,95,2,4))
if mibBuilder.loadTexts:mplsTunnelHopTable.setStatus(_A)
_MplsTunnelHopEntry_Object=MibTableRow
mplsTunnelHopEntry=_MplsTunnelHopEntry_Object((1,3,6,1,3,95,2,4,1))
mplsTunnelHopEntry.setIndexNames((0,_B,_a),(0,_B,_b),(0,_B,_c))
if mibBuilder.loadTexts:mplsTunnelHopEntry.setStatus(_A)
_MplsTunnelHopListIndex_Type=MplsPathIndex
_MplsTunnelHopListIndex_Object=MibTableColumn
mplsTunnelHopListIndex=_MplsTunnelHopListIndex_Object((1,3,6,1,3,95,2,4,1,1),_MplsTunnelHopListIndex_Type())
mplsTunnelHopListIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mplsTunnelHopListIndex.setStatus(_A)
_MplsPathOptionIndex_Type=MplsPathIndex
_MplsPathOptionIndex_Object=MibTableColumn
mplsPathOptionIndex=_MplsPathOptionIndex_Object((1,3,6,1,3,95,2,4,1,2),_MplsPathOptionIndex_Type())
mplsPathOptionIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mplsPathOptionIndex.setStatus(_A)
_MplsTunnelHopIndex_Type=MplsPathIndex
_MplsTunnelHopIndex_Object=MibTableColumn
mplsTunnelHopIndex=_MplsTunnelHopIndex_Object((1,3,6,1,3,95,2,4,1,3),_MplsTunnelHopIndex_Type())
mplsTunnelHopIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mplsTunnelHopIndex.setStatus(_A)
class _MplsTunnelHopAddrType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),('lspid',4)))
_MplsTunnelHopAddrType_Type.__name__=_F
_MplsTunnelHopAddrType_Object=MibTableColumn
mplsTunnelHopAddrType=_MplsTunnelHopAddrType_Object((1,3,6,1,3,95,2,4,1,4),_MplsTunnelHopAddrType_Type())
mplsTunnelHopAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelHopAddrType.setStatus(_A)
_MplsTunnelHopIpv4Addr_Type=InetAddressIPv4
_MplsTunnelHopIpv4Addr_Object=MibTableColumn
mplsTunnelHopIpv4Addr=_MplsTunnelHopIpv4Addr_Object((1,3,6,1,3,95,2,4,1,5),_MplsTunnelHopIpv4Addr_Type())
mplsTunnelHopIpv4Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelHopIpv4Addr.setStatus(_A)
class _MplsTunnelHopIpv4PrefixLen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_MplsTunnelHopIpv4PrefixLen_Type.__name__=_E
_MplsTunnelHopIpv4PrefixLen_Object=MibTableColumn
mplsTunnelHopIpv4PrefixLen=_MplsTunnelHopIpv4PrefixLen_Object((1,3,6,1,3,95,2,4,1,6),_MplsTunnelHopIpv4PrefixLen_Type())
mplsTunnelHopIpv4PrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelHopIpv4PrefixLen.setStatus(_A)
_MplsTunnelHopIpv6Addr_Type=InetAddressIPv6
_MplsTunnelHopIpv6Addr_Object=MibTableColumn
mplsTunnelHopIpv6Addr=_MplsTunnelHopIpv6Addr_Object((1,3,6,1,3,95,2,4,1,7),_MplsTunnelHopIpv6Addr_Type())
mplsTunnelHopIpv6Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelHopIpv6Addr.setStatus(_A)
class _MplsTunnelHopIpv6PrefixLen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_MplsTunnelHopIpv6PrefixLen_Type.__name__=_E
_MplsTunnelHopIpv6PrefixLen_Object=MibTableColumn
mplsTunnelHopIpv6PrefixLen=_MplsTunnelHopIpv6PrefixLen_Object((1,3,6,1,3,95,2,4,1,8),_MplsTunnelHopIpv6PrefixLen_Type())
mplsTunnelHopIpv6PrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelHopIpv6PrefixLen.setStatus(_A)
class _MplsTunnelHopAsNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MplsTunnelHopAsNumber_Type.__name__=_E
_MplsTunnelHopAsNumber_Object=MibTableColumn
mplsTunnelHopAsNumber=_MplsTunnelHopAsNumber_Object((1,3,6,1,3,95,2,4,1,9),_MplsTunnelHopAsNumber_Type())
mplsTunnelHopAsNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelHopAsNumber.setStatus(_A)
_MplsTunnelHopLspId_Type=MplsLSPID
_MplsTunnelHopLspId_Object=MibTableColumn
mplsTunnelHopLspId=_MplsTunnelHopLspId_Object((1,3,6,1,3,95,2,4,1,10),_MplsTunnelHopLspId_Type())
mplsTunnelHopLspId.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelHopLspId.setStatus(_A)
class _MplsTunnelHopType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_MplsTunnelHopType_Type.__name__=_F
_MplsTunnelHopType_Object=MibTableColumn
mplsTunnelHopType=_MplsTunnelHopType_Object((1,3,6,1,3,95,2,4,1,11),_MplsTunnelHopType_Type())
mplsTunnelHopType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelHopType.setStatus(_A)
_MplsTunnelHopRowStatus_Type=RowStatus
_MplsTunnelHopRowStatus_Object=MibTableColumn
mplsTunnelHopRowStatus=_MplsTunnelHopRowStatus_Object((1,3,6,1,3,95,2,4,1,12),_MplsTunnelHopRowStatus_Type())
mplsTunnelHopRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelHopRowStatus.setStatus(_A)
_MplsTunnelHopStorageType_Type=StorageType
_MplsTunnelHopStorageType_Object=MibTableColumn
mplsTunnelHopStorageType=_MplsTunnelHopStorageType_Object((1,3,6,1,3,95,2,4,1,13),_MplsTunnelHopStorageType_Type())
mplsTunnelHopStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelHopStorageType.setStatus(_A)
class _MplsTunnelResourceIndexNext_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsTunnelResourceIndexNext_Type.__name__=_E
_MplsTunnelResourceIndexNext_Object=MibScalar
mplsTunnelResourceIndexNext=_MplsTunnelResourceIndexNext_Object((1,3,6,1,3,95,2,5),_MplsTunnelResourceIndexNext_Type())
mplsTunnelResourceIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelResourceIndexNext.setStatus(_A)
_MplsTunnelResourceTable_Object=MibTable
mplsTunnelResourceTable=_MplsTunnelResourceTable_Object((1,3,6,1,3,95,2,6))
if mibBuilder.loadTexts:mplsTunnelResourceTable.setStatus(_A)
_MplsTunnelResourceEntry_Object=MibTableRow
mplsTunnelResourceEntry=_MplsTunnelResourceEntry_Object((1,3,6,1,3,95,2,6,1))
mplsTunnelResourceEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:mplsTunnelResourceEntry.setStatus(_A)
class _MplsTunnelResourceIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsTunnelResourceIndex_Type.__name__=_E
_MplsTunnelResourceIndex_Object=MibTableColumn
mplsTunnelResourceIndex=_MplsTunnelResourceIndex_Object((1,3,6,1,3,95,2,6,1,1),_MplsTunnelResourceIndex_Type())
mplsTunnelResourceIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mplsTunnelResourceIndex.setStatus(_A)
_MplsTunnelResourceMaxRate_Type=MplsBitRate
_MplsTunnelResourceMaxRate_Object=MibTableColumn
mplsTunnelResourceMaxRate=_MplsTunnelResourceMaxRate_Object((1,3,6,1,3,95,2,6,1,2),_MplsTunnelResourceMaxRate_Type())
mplsTunnelResourceMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelResourceMaxRate.setStatus(_A)
if mibBuilder.loadTexts:mplsTunnelResourceMaxRate.setUnits(_e)
_MplsTunnelResourceMeanRate_Type=MplsBitRate
_MplsTunnelResourceMeanRate_Object=MibTableColumn
mplsTunnelResourceMeanRate=_MplsTunnelResourceMeanRate_Object((1,3,6,1,3,95,2,6,1,3),_MplsTunnelResourceMeanRate_Type())
mplsTunnelResourceMeanRate.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelResourceMeanRate.setStatus(_A)
if mibBuilder.loadTexts:mplsTunnelResourceMeanRate.setUnits(_e)
_MplsTunnelResourceMaxBurstSize_Type=MplsBurstSize
_MplsTunnelResourceMaxBurstSize_Object=MibTableColumn
mplsTunnelResourceMaxBurstSize=_MplsTunnelResourceMaxBurstSize_Object((1,3,6,1,3,95,2,6,1,4),_MplsTunnelResourceMaxBurstSize_Type())
mplsTunnelResourceMaxBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelResourceMaxBurstSize.setStatus(_A)
if mibBuilder.loadTexts:mplsTunnelResourceMaxBurstSize.setUnits('bytes')
_MplsTunnelResourceRowStatus_Type=RowStatus
_MplsTunnelResourceRowStatus_Object=MibTableColumn
mplsTunnelResourceRowStatus=_MplsTunnelResourceRowStatus_Object((1,3,6,1,3,95,2,6,1,5),_MplsTunnelResourceRowStatus_Type())
mplsTunnelResourceRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelResourceRowStatus.setStatus(_A)
_MplsTunnelResourceStorageType_Type=StorageType
_MplsTunnelResourceStorageType_Object=MibTableColumn
mplsTunnelResourceStorageType=_MplsTunnelResourceStorageType_Object((1,3,6,1,3,95,2,6,1,6),_MplsTunnelResourceStorageType_Type())
mplsTunnelResourceStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelResourceStorageType.setStatus(_A)
_MplsTunnelARHopTable_Object=MibTable
mplsTunnelARHopTable=_MplsTunnelARHopTable_Object((1,3,6,1,3,95,2,7))
if mibBuilder.loadTexts:mplsTunnelARHopTable.setStatus(_A)
_MplsTunnelARHopEntry_Object=MibTableRow
mplsTunnelARHopEntry=_MplsTunnelARHopEntry_Object((1,3,6,1,3,95,2,7,1))
mplsTunnelARHopEntry.setIndexNames((0,_B,_f),(0,_B,_g))
if mibBuilder.loadTexts:mplsTunnelARHopEntry.setStatus(_A)
class _MplsTunnelARHopListIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsTunnelARHopListIndex_Type.__name__=_E
_MplsTunnelARHopListIndex_Object=MibTableColumn
mplsTunnelARHopListIndex=_MplsTunnelARHopListIndex_Object((1,3,6,1,3,95,2,7,1,1),_MplsTunnelARHopListIndex_Type())
mplsTunnelARHopListIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mplsTunnelARHopListIndex.setStatus(_A)
class _MplsTunnelARHopIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsTunnelARHopIndex_Type.__name__=_E
_MplsTunnelARHopIndex_Object=MibTableColumn
mplsTunnelARHopIndex=_MplsTunnelARHopIndex_Object((1,3,6,1,3,95,2,7,1,2),_MplsTunnelARHopIndex_Type())
mplsTunnelARHopIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mplsTunnelARHopIndex.setStatus(_A)
class _MplsTunnelARHopAddrType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_MplsTunnelARHopAddrType_Type.__name__=_F
_MplsTunnelARHopAddrType_Object=MibTableColumn
mplsTunnelARHopAddrType=_MplsTunnelARHopAddrType_Object((1,3,6,1,3,95,2,7,1,3),_MplsTunnelARHopAddrType_Type())
mplsTunnelARHopAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelARHopAddrType.setStatus(_A)
_MplsTunnelARHopIpv4Addr_Type=InetAddressIPv4
_MplsTunnelARHopIpv4Addr_Object=MibTableColumn
mplsTunnelARHopIpv4Addr=_MplsTunnelARHopIpv4Addr_Object((1,3,6,1,3,95,2,7,1,4),_MplsTunnelARHopIpv4Addr_Type())
mplsTunnelARHopIpv4Addr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelARHopIpv4Addr.setStatus(_A)
class _MplsTunnelARHopIpv4PrefixLen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_MplsTunnelARHopIpv4PrefixLen_Type.__name__=_E
_MplsTunnelARHopIpv4PrefixLen_Object=MibTableColumn
mplsTunnelARHopIpv4PrefixLen=_MplsTunnelARHopIpv4PrefixLen_Object((1,3,6,1,3,95,2,7,1,5),_MplsTunnelARHopIpv4PrefixLen_Type())
mplsTunnelARHopIpv4PrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelARHopIpv4PrefixLen.setStatus(_A)
_MplsTunnelARHopIpv6Addr_Type=InetAddressIPv6
_MplsTunnelARHopIpv6Addr_Object=MibTableColumn
mplsTunnelARHopIpv6Addr=_MplsTunnelARHopIpv6Addr_Object((1,3,6,1,3,95,2,7,1,6),_MplsTunnelARHopIpv6Addr_Type())
mplsTunnelARHopIpv6Addr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelARHopIpv6Addr.setStatus(_A)
class _MplsTunnelARHopIpv6PrefixLen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_MplsTunnelARHopIpv6PrefixLen_Type.__name__=_E
_MplsTunnelARHopIpv6PrefixLen_Object=MibTableColumn
mplsTunnelARHopIpv6PrefixLen=_MplsTunnelARHopIpv6PrefixLen_Object((1,3,6,1,3,95,2,7,1,7),_MplsTunnelARHopIpv6PrefixLen_Type())
mplsTunnelARHopIpv6PrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelARHopIpv6PrefixLen.setStatus(_A)
class _MplsTunnelARHopAsNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MplsTunnelARHopAsNumber_Type.__name__=_E
_MplsTunnelARHopAsNumber_Object=MibTableColumn
mplsTunnelARHopAsNumber=_MplsTunnelARHopAsNumber_Object((1,3,6,1,3,95,2,7,1,8),_MplsTunnelARHopAsNumber_Type())
mplsTunnelARHopAsNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelARHopAsNumber.setStatus(_A)
class _MplsTunnelARHopType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_MplsTunnelARHopType_Type.__name__=_F
_MplsTunnelARHopType_Object=MibTableColumn
mplsTunnelARHopType=_MplsTunnelARHopType_Object((1,3,6,1,3,95,2,7,1,9),_MplsTunnelARHopType_Type())
mplsTunnelARHopType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelARHopType.setStatus(_A)
_MplsTunnelCHopTable_Object=MibTable
mplsTunnelCHopTable=_MplsTunnelCHopTable_Object((1,3,6,1,3,95,2,8))
if mibBuilder.loadTexts:mplsTunnelCHopTable.setStatus(_A)
_MplsTunnelCHopEntry_Object=MibTableRow
mplsTunnelCHopEntry=_MplsTunnelCHopEntry_Object((1,3,6,1,3,95,2,8,1))
mplsTunnelCHopEntry.setIndexNames((0,_B,_h),(0,_B,_i))
if mibBuilder.loadTexts:mplsTunnelCHopEntry.setStatus(_A)
class _MplsTunnelCHopListIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsTunnelCHopListIndex_Type.__name__=_E
_MplsTunnelCHopListIndex_Object=MibTableColumn
mplsTunnelCHopListIndex=_MplsTunnelCHopListIndex_Object((1,3,6,1,3,95,2,8,1,1),_MplsTunnelCHopListIndex_Type())
mplsTunnelCHopListIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mplsTunnelCHopListIndex.setStatus(_A)
class _MplsTunnelCHopIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsTunnelCHopIndex_Type.__name__=_E
_MplsTunnelCHopIndex_Object=MibTableColumn
mplsTunnelCHopIndex=_MplsTunnelCHopIndex_Object((1,3,6,1,3,95,2,8,1,2),_MplsTunnelCHopIndex_Type())
mplsTunnelCHopIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mplsTunnelCHopIndex.setStatus(_A)
class _MplsTunnelCHopAddrType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_MplsTunnelCHopAddrType_Type.__name__=_F
_MplsTunnelCHopAddrType_Object=MibTableColumn
mplsTunnelCHopAddrType=_MplsTunnelCHopAddrType_Object((1,3,6,1,3,95,2,8,1,3),_MplsTunnelCHopAddrType_Type())
mplsTunnelCHopAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelCHopAddrType.setStatus(_A)
_MplsTunnelCHopIpv4Addr_Type=InetAddressIPv4
_MplsTunnelCHopIpv4Addr_Object=MibTableColumn
mplsTunnelCHopIpv4Addr=_MplsTunnelCHopIpv4Addr_Object((1,3,6,1,3,95,2,8,1,4),_MplsTunnelCHopIpv4Addr_Type())
mplsTunnelCHopIpv4Addr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelCHopIpv4Addr.setStatus(_A)
class _MplsTunnelCHopIpv4PrefixLen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_MplsTunnelCHopIpv4PrefixLen_Type.__name__=_E
_MplsTunnelCHopIpv4PrefixLen_Object=MibTableColumn
mplsTunnelCHopIpv4PrefixLen=_MplsTunnelCHopIpv4PrefixLen_Object((1,3,6,1,3,95,2,8,1,5),_MplsTunnelCHopIpv4PrefixLen_Type())
mplsTunnelCHopIpv4PrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelCHopIpv4PrefixLen.setStatus(_A)
_MplsTunnelCHopIpv6Addr_Type=InetAddressIPv6
_MplsTunnelCHopIpv6Addr_Object=MibTableColumn
mplsTunnelCHopIpv6Addr=_MplsTunnelCHopIpv6Addr_Object((1,3,6,1,3,95,2,8,1,6),_MplsTunnelCHopIpv6Addr_Type())
mplsTunnelCHopIpv6Addr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelCHopIpv6Addr.setStatus(_A)
class _MplsTunnelCHopIpv6PrefixLen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_MplsTunnelCHopIpv6PrefixLen_Type.__name__=_E
_MplsTunnelCHopIpv6PrefixLen_Object=MibTableColumn
mplsTunnelCHopIpv6PrefixLen=_MplsTunnelCHopIpv6PrefixLen_Object((1,3,6,1,3,95,2,8,1,7),_MplsTunnelCHopIpv6PrefixLen_Type())
mplsTunnelCHopIpv6PrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelCHopIpv6PrefixLen.setStatus(_A)
class _MplsTunnelCHopAsNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MplsTunnelCHopAsNumber_Type.__name__=_E
_MplsTunnelCHopAsNumber_Object=MibTableColumn
mplsTunnelCHopAsNumber=_MplsTunnelCHopAsNumber_Object((1,3,6,1,3,95,2,8,1,8),_MplsTunnelCHopAsNumber_Type())
mplsTunnelCHopAsNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelCHopAsNumber.setStatus(_A)
class _MplsTunnelCHopType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_MplsTunnelCHopType_Type.__name__=_F
_MplsTunnelCHopType_Object=MibTableColumn
mplsTunnelCHopType=_MplsTunnelCHopType_Object((1,3,6,1,3,95,2,8,1,9),_MplsTunnelCHopType_Type())
mplsTunnelCHopType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelCHopType.setStatus(_A)
_MplsTunnelPerfTable_Object=MibTable
mplsTunnelPerfTable=_MplsTunnelPerfTable_Object((1,3,6,1,3,95,2,9))
if mibBuilder.loadTexts:mplsTunnelPerfTable.setStatus(_A)
_MplsTunnelPerfEntry_Object=MibTableRow
mplsTunnelPerfEntry=_MplsTunnelPerfEntry_Object((1,3,6,1,3,95,2,9,1))
if mibBuilder.loadTexts:mplsTunnelPerfEntry.setStatus(_A)
_MplsTunnelPerfPackets_Type=Counter32
_MplsTunnelPerfPackets_Object=MibTableColumn
mplsTunnelPerfPackets=_MplsTunnelPerfPackets_Object((1,3,6,1,3,95,2,9,1,1),_MplsTunnelPerfPackets_Type())
mplsTunnelPerfPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelPerfPackets.setStatus(_A)
_MplsTunnelPerfHCPackets_Type=Counter64
_MplsTunnelPerfHCPackets_Object=MibTableColumn
mplsTunnelPerfHCPackets=_MplsTunnelPerfHCPackets_Object((1,3,6,1,3,95,2,9,1,2),_MplsTunnelPerfHCPackets_Type())
mplsTunnelPerfHCPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelPerfHCPackets.setStatus(_A)
_MplsTunnelPerfErrors_Type=Counter32
_MplsTunnelPerfErrors_Object=MibTableColumn
mplsTunnelPerfErrors=_MplsTunnelPerfErrors_Object((1,3,6,1,3,95,2,9,1,3),_MplsTunnelPerfErrors_Type())
mplsTunnelPerfErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelPerfErrors.setStatus(_A)
_MplsTunnelPerfBytes_Type=Counter32
_MplsTunnelPerfBytes_Object=MibTableColumn
mplsTunnelPerfBytes=_MplsTunnelPerfBytes_Object((1,3,6,1,3,95,2,9,1,4),_MplsTunnelPerfBytes_Type())
mplsTunnelPerfBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelPerfBytes.setStatus(_A)
_MplsTunnelPerfHCBytes_Type=Counter64
_MplsTunnelPerfHCBytes_Object=MibTableColumn
mplsTunnelPerfHCBytes=_MplsTunnelPerfHCBytes_Object((1,3,6,1,3,95,2,9,1,5),_MplsTunnelPerfHCBytes_Type())
mplsTunnelPerfHCBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelPerfHCBytes.setStatus(_A)
class _MplsTunnelTrapEnable_Type(TruthValue):defaultValue=2
_MplsTunnelTrapEnable_Type.__name__=_K
_MplsTunnelTrapEnable_Object=MibScalar
mplsTunnelTrapEnable=_MplsTunnelTrapEnable_Object((1,3,6,1,3,95,2,10),_MplsTunnelTrapEnable_Type())
mplsTunnelTrapEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:mplsTunnelTrapEnable.setStatus(_A)
_MplsTeNotifications_ObjectIdentity=ObjectIdentity
mplsTeNotifications=_MplsTeNotifications_ObjectIdentity((1,3,6,1,3,95,3))
_MplsTeNotifyPrefix_ObjectIdentity=ObjectIdentity
mplsTeNotifyPrefix=_MplsTeNotifyPrefix_ObjectIdentity((1,3,6,1,3,95,3,0))
_MplsTeConformance_ObjectIdentity=ObjectIdentity
mplsTeConformance=_MplsTeConformance_ObjectIdentity((1,3,6,1,3,95,4))
_MplsTeGroups_ObjectIdentity=ObjectIdentity
mplsTeGroups=_MplsTeGroups_ObjectIdentity((1,3,6,1,3,95,4,1))
_MplsTeCompliances_ObjectIdentity=ObjectIdentity
mplsTeCompliances=_MplsTeCompliances_ObjectIdentity((1,3,6,1,3,95,4,2))
mplsTunnelEntry.registerAugmentions((_B,_j))
mplsTunnelPerfEntry.setIndexNames(*mplsTunnelEntry.getIndexNames())
mplsTunnelGroup=ObjectGroup((1,3,6,1,3,95,4,1,1))
mplsTunnelGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_H),(_B,_I),(_B,_t),(_B,_u),(_B,_v),(_B,_S),(_B,_T),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_M),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:mplsTunnelGroup.setStatus(_A)
mplsTunnelManualGroup=ObjectGroup((1,3,6,1,3,95,4,1,2))
mplsTunnelManualGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:mplsTunnelManualGroup.setStatus(_A)
mplsTunnelSignaledGroup=ObjectGroup((1,3,6,1,3,95,4,1,3))
mplsTunnelSignaledGroup.setObjects(*((_B,_AG),(_B,_AH),(_B,_U),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU)))
if mibBuilder.loadTexts:mplsTunnelSignaledGroup.setStatus(_A)
mplsTunnelScalarGroup=ObjectGroup((1,3,6,1,3,95,4,1,4))
mplsTunnelScalarGroup.setObjects(*((_B,_S),(_B,_T),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:mplsTunnelScalarGroup.setStatus(_A)
mplsTunnelIsIntfcGroup=ObjectGroup((1,3,6,1,3,95,4,1,5))
mplsTunnelIsIntfcGroup.setObjects((_B,_V))
if mibBuilder.loadTexts:mplsTunnelIsIntfcGroup.setStatus(_A)
mplsTunnelIsNotIntfcGroup=ObjectGroup((1,3,6,1,3,95,4,1,6))
mplsTunnelIsNotIntfcGroup.setObjects((_B,_V))
if mibBuilder.loadTexts:mplsTunnelIsNotIntfcGroup.setStatus(_A)
mplsTunnelOptionalGroup=ObjectGroup((1,3,6,1,3,95,4,1,7))
mplsTunnelOptionalGroup.setObjects(*((_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq)))
if mibBuilder.loadTexts:mplsTunnelOptionalGroup.setStatus(_A)
mplsTunnelUp=NotificationType((1,3,6,1,3,95,3,0,1))
mplsTunnelUp.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:mplsTunnelUp.setStatus(_A)
mplsTunnelDown=NotificationType((1,3,6,1,3,95,3,0,2))
mplsTunnelDown.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:mplsTunnelDown.setStatus(_A)
mplsTunnelRerouted=NotificationType((1,3,6,1,3,95,3,0,3))
mplsTunnelRerouted.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:mplsTunnelRerouted.setStatus(_A)
mplsTeNotificationGroup=NotificationGroup((1,3,6,1,3,95,4,1,8))
mplsTeNotificationGroup.setObjects(*((_B,_Ar),(_B,_As),(_B,_At)))
if mibBuilder.loadTexts:mplsTeNotificationGroup.setStatus(_A)
mplsTeModuleCompliance=ModuleCompliance((1,3,6,1,3,95,4,2,1))
mplsTeModuleCompliance.setObjects(*((_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_)))
if mibBuilder.loadTexts:mplsTeModuleCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'MplsTunnelIndex':MplsTunnelIndex,'MplsTunnelInstanceIndex':MplsTunnelInstanceIndex,'MplsLsrId':MplsLsrId,'MplsPathIndex':MplsPathIndex,'MplsPathIndexOrZero':MplsPathIndexOrZero,'mplsTeMIB':mplsTeMIB,'mplsTeScalars':mplsTeScalars,_S:mplsTunnelConfigured,_T:mplsTunnelActive,_AV:mplsTunnelTEDistProto,_AW:mplsTunnelMaxHops,'mplsTeObjects':mplsTeObjects,_k:mplsTunnelIndexNext,'mplsTunnelTable':mplsTunnelTable,'mplsTunnelEntry':mplsTunnelEntry,_W:mplsTunnelIndex,_X:mplsTunnelInstance,_Y:mplsTunnelIngressLSRId,_M:mplsTunnelEgressLSRId,_l:mplsTunnelName,_m:mplsTunnelDescr,_V:mplsTunnelIsIf,_p:mplsTunnelIfIndex,_o:mplsTunnelXCPointer,_U:mplsTunnelSignallingProto,_AG:mplsTunnelSetupPrio,_AH:mplsTunnelHoldingPrio,_AJ:mplsTunnelSessionAttributes,_n:mplsTunnelOwner,_AI:mplsTunnelLocalProtectInUse,_AA:mplsTunnelResourcePointer,_AB:mplsTunnelInstancePriority,_q:mplsTunnelHopTableIndex,_r:mplsTunnelARHopTableIndex,_s:mplsTunnelCHopTableIndex,_w:mplsTunnelPrimaryInstance,_x:mplsTunnelPrimaryTimeUp,_y:mplsTunnelPathChanges,_z:mplsTunnelLastPathChange,_A0:mplsTunnelCreationTime,_A1:mplsTunnelStateTransitions,_A2:mplsTunnelIncludeAnyAffinity,_A3:mplsTunnelIncludeAllAffinity,_A4:mplsTunnelExcludeAllAffinity,_AC:mplsTunnelPathInUse,_AD:mplsTunnelRole,_AE:mplsTunnelTotalUpTime,_AF:mplsTunnelInstanceUpTime,_H:mplsTunnelAdminStatus,_I:mplsTunnelOperStatus,_t:mplsTunnelRowStatus,_v:mplsTunnelStorageType,_AK:mplsTunnelHopListIndexNext,'mplsTunnelHopTable':mplsTunnelHopTable,'mplsTunnelHopEntry':mplsTunnelHopEntry,_a:mplsTunnelHopListIndex,_b:mplsPathOptionIndex,_c:mplsTunnelHopIndex,_AL:mplsTunnelHopAddrType,_AM:mplsTunnelHopIpv4Addr,_AN:mplsTunnelHopIpv4PrefixLen,_AO:mplsTunnelHopIpv6Addr,_AP:mplsTunnelHopIpv6PrefixLen,_AQ:mplsTunnelHopAsNumber,_AR:mplsTunnelHopLspId,_AS:mplsTunnelHopType,_AT:mplsTunnelHopRowStatus,_AU:mplsTunnelHopStorageType,_AX:mplsTunnelResourceIndexNext,'mplsTunnelResourceTable':mplsTunnelResourceTable,'mplsTunnelResourceEntry':mplsTunnelResourceEntry,_d:mplsTunnelResourceIndex,_AY:mplsTunnelResourceMaxRate,_AZ:mplsTunnelResourceMeanRate,_Aa:mplsTunnelResourceMaxBurstSize,_Ab:mplsTunnelResourceRowStatus,_Ac:mplsTunnelResourceStorageType,'mplsTunnelARHopTable':mplsTunnelARHopTable,'mplsTunnelARHopEntry':mplsTunnelARHopEntry,_f:mplsTunnelARHopListIndex,_g:mplsTunnelARHopIndex,_Ad:mplsTunnelARHopAddrType,_Ae:mplsTunnelARHopIpv4Addr,_Af:mplsTunnelARHopIpv4PrefixLen,_Ag:mplsTunnelARHopIpv6Addr,_Ah:mplsTunnelARHopIpv6PrefixLen,_Ai:mplsTunnelARHopAsNumber,_Aj:mplsTunnelARHopType,'mplsTunnelCHopTable':mplsTunnelCHopTable,'mplsTunnelCHopEntry':mplsTunnelCHopEntry,_h:mplsTunnelCHopListIndex,_i:mplsTunnelCHopIndex,_Ak:mplsTunnelCHopAddrType,_Al:mplsTunnelCHopIpv4Addr,_Am:mplsTunnelCHopIpv4PrefixLen,_An:mplsTunnelCHopIpv6Addr,_Ao:mplsTunnelCHopIpv6PrefixLen,_Ap:mplsTunnelCHopAsNumber,_Aq:mplsTunnelCHopType,'mplsTunnelPerfTable':mplsTunnelPerfTable,_j:mplsTunnelPerfEntry,_A5:mplsTunnelPerfPackets,_A6:mplsTunnelPerfHCPackets,_A7:mplsTunnelPerfErrors,_A8:mplsTunnelPerfBytes,_A9:mplsTunnelPerfHCBytes,_u:mplsTunnelTrapEnable,'mplsTeNotifications':mplsTeNotifications,'mplsTeNotifyPrefix':mplsTeNotifyPrefix,_Ar:mplsTunnelUp,_As:mplsTunnelDown,_At:mplsTunnelRerouted,'mplsTeConformance':mplsTeConformance,'mplsTeGroups':mplsTeGroups,_Au:mplsTunnelGroup,_Aw:mplsTunnelManualGroup,_Ax:mplsTunnelSignaledGroup,_Av:mplsTunnelScalarGroup,_Az:mplsTunnelIsIntfcGroup,_Ay:mplsTunnelIsNotIntfcGroup,_A_:mplsTunnelOptionalGroup,'mplsTeNotificationGroup':mplsTeNotificationGroup,'mplsTeCompliances':mplsTeCompliances,'mplsTeModuleCompliance':mplsTeModuleCompliance})