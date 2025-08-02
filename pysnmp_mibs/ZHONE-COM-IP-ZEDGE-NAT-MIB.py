_P='zhoneNATExcludeIndex'
_O='zhonePATBindIndex'
_N='natBindingPublicPort'
_M='natBindingPublicAddr'
_L='natBindingLocalPort'
_K='natBindingLocalAddr'
_J='natBindingsIfIndex'
_I='seconds'
_H='read-write'
_G='Unsigned32'
_F='not-accessible'
_E='Integer32'
_D='ZHONE-COM-IP-ZEDGE-NAT-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
zhoneIp,zhoneModules=mibBuilder.importSymbols('Zhone','zhoneIp','zhoneModules')
ZhoneRowStatus,=mibBuilder.importSymbols('Zhone-TC','ZhoneRowStatus')
comIpZEdgeNat=ModuleIdentity((1,3,6,1,4,1,5504,6,66))
if mibBuilder.loadTexts:comIpZEdgeNat.setRevisions(('2010-10-20 05:52','2008-07-22 07:28','2003-12-11 02:58','2003-03-19 09:02','2000-10-04 15:30'))
_ZedgeNat_ObjectIdentity=ObjectIdentity
zedgeNat=_ZedgeNat_ObjectIdentity((1,3,6,1,4,1,5504,4,1,16))
if mibBuilder.loadTexts:zedgeNat.setStatus(_A)
_NatConfigGroup_ObjectIdentity=ObjectIdentity
natConfigGroup=_NatConfigGroup_ObjectIdentity((1,3,6,1,4,1,5504,4,1,16,1))
if mibBuilder.loadTexts:natConfigGroup.setStatus(_A)
class _NatTcpTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800))
_NatTcpTimeout_Type.__name__=_G
_NatTcpTimeout_Object=MibScalar
natTcpTimeout=_NatTcpTimeout_Object((1,3,6,1,4,1,5504,4,1,16,1,1),_NatTcpTimeout_Type())
natTcpTimeout.setMaxAccess(_H)
if mibBuilder.loadTexts:natTcpTimeout.setStatus(_A)
if mibBuilder.loadTexts:natTcpTimeout.setUnits(_I)
class _NatUdpTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800))
_NatUdpTimeout_Type.__name__=_G
_NatUdpTimeout_Object=MibScalar
natUdpTimeout=_NatUdpTimeout_Object((1,3,6,1,4,1,5504,4,1,16,1,2),_NatUdpTimeout_Type())
natUdpTimeout.setMaxAccess(_H)
if mibBuilder.loadTexts:natUdpTimeout.setStatus(_A)
if mibBuilder.loadTexts:natUdpTimeout.setUnits(_I)
_NatClearBindings_Type=TruthValue
_NatClearBindings_Object=MibScalar
natClearBindings=_NatClearBindings_Object((1,3,6,1,4,1,5504,4,1,16,1,3),_NatClearBindings_Type())
natClearBindings.setMaxAccess(_H)
if mibBuilder.loadTexts:natClearBindings.setStatus(_A)
_NatStatsGroup_ObjectIdentity=ObjectIdentity
natStatsGroup=_NatStatsGroup_ObjectIdentity((1,3,6,1,4,1,5504,4,1,16,2))
if mibBuilder.loadTexts:natStatsGroup.setStatus(_A)
_NatNumCurrentBindings_Type=Gauge32
_NatNumCurrentBindings_Object=MibScalar
natNumCurrentBindings=_NatNumCurrentBindings_Object((1,3,6,1,4,1,5504,4,1,16,2,1),_NatNumCurrentBindings_Type())
natNumCurrentBindings.setMaxAccess(_C)
if mibBuilder.loadTexts:natNumCurrentBindings.setStatus(_A)
_NatNumExpiredBindings_Type=Gauge32
_NatNumExpiredBindings_Object=MibScalar
natNumExpiredBindings=_NatNumExpiredBindings_Object((1,3,6,1,4,1,5504,4,1,16,2,2),_NatNumExpiredBindings_Type())
natNumExpiredBindings.setMaxAccess(_C)
if mibBuilder.loadTexts:natNumExpiredBindings.setStatus(_A)
_NatTotalPkts_Type=Counter32
_NatTotalPkts_Object=MibScalar
natTotalPkts=_NatTotalPkts_Object((1,3,6,1,4,1,5504,4,1,16,2,3),_NatTotalPkts_Type())
natTotalPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:natTotalPkts.setStatus(_A)
_NatDroppedPkts_Type=Counter32
_NatDroppedPkts_Object=MibScalar
natDroppedPkts=_NatDroppedPkts_Object((1,3,6,1,4,1,5504,4,1,16,2,4),_NatDroppedPkts_Type())
natDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:natDroppedPkts.setStatus(_A)
_NatBindingsTable_Object=MibTable
natBindingsTable=_NatBindingsTable_Object((1,3,6,1,4,1,5504,4,1,16,3))
if mibBuilder.loadTexts:natBindingsTable.setStatus(_A)
_NatBindingsEntry_Object=MibTableRow
natBindingsEntry=_NatBindingsEntry_Object((1,3,6,1,4,1,5504,4,1,16,3,1))
natBindingsEntry.setIndexNames((0,_D,_J),(0,_D,_K),(0,_D,_L),(0,_D,_M),(0,_D,_N))
if mibBuilder.loadTexts:natBindingsEntry.setStatus(_A)
_NatBindingsIfIndex_Type=InterfaceIndex
_NatBindingsIfIndex_Object=MibTableColumn
natBindingsIfIndex=_NatBindingsIfIndex_Object((1,3,6,1,4,1,5504,4,1,16,3,1,1),_NatBindingsIfIndex_Type())
natBindingsIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:natBindingsIfIndex.setStatus(_A)
_NatBindingLocalAddr_Type=IpAddress
_NatBindingLocalAddr_Object=MibTableColumn
natBindingLocalAddr=_NatBindingLocalAddr_Object((1,3,6,1,4,1,5504,4,1,16,3,1,2),_NatBindingLocalAddr_Type())
natBindingLocalAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:natBindingLocalAddr.setStatus(_A)
_NatBindingLocalPort_Type=Unsigned32
_NatBindingLocalPort_Object=MibTableColumn
natBindingLocalPort=_NatBindingLocalPort_Object((1,3,6,1,4,1,5504,4,1,16,3,1,3),_NatBindingLocalPort_Type())
natBindingLocalPort.setMaxAccess(_F)
if mibBuilder.loadTexts:natBindingLocalPort.setStatus(_A)
_NatBindingPublicAddr_Type=IpAddress
_NatBindingPublicAddr_Object=MibTableColumn
natBindingPublicAddr=_NatBindingPublicAddr_Object((1,3,6,1,4,1,5504,4,1,16,3,1,4),_NatBindingPublicAddr_Type())
natBindingPublicAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:natBindingPublicAddr.setStatus(_A)
_NatBindingPublicPort_Type=Unsigned32
_NatBindingPublicPort_Object=MibTableColumn
natBindingPublicPort=_NatBindingPublicPort_Object((1,3,6,1,4,1,5504,4,1,16,3,1,5),_NatBindingPublicPort_Type())
natBindingPublicPort.setMaxAccess(_C)
if mibBuilder.loadTexts:natBindingPublicPort.setStatus(_A)
_ZhonePATBindings_ObjectIdentity=ObjectIdentity
zhonePATBindings=_ZhonePATBindings_ObjectIdentity((1,3,6,1,4,1,5504,4,1,16,4))
_PatBindNextIndex_Type=Integer32
_PatBindNextIndex_Object=MibScalar
patBindNextIndex=_PatBindNextIndex_Object((1,3,6,1,4,1,5504,4,1,16,4,1),_PatBindNextIndex_Type())
patBindNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:patBindNextIndex.setStatus(_A)
_PatTable_Object=MibTable
patTable=_PatTable_Object((1,3,6,1,4,1,5504,4,1,16,4,2))
if mibBuilder.loadTexts:patTable.setStatus(_A)
_PatEntry_Object=MibTableRow
patEntry=_PatEntry_Object((1,3,6,1,4,1,5504,4,1,16,4,2,1))
patEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:patEntry.setStatus(_A)
class _ZhonePATBindIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4320))
_ZhonePATBindIndex_Type.__name__=_E
_ZhonePATBindIndex_Object=MibTableColumn
zhonePATBindIndex=_ZhonePATBindIndex_Object((1,3,6,1,4,1,5504,4,1,16,4,2,1,1),_ZhonePATBindIndex_Type())
zhonePATBindIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhonePATBindIndex.setStatus(_A)
_ZhonePATBindRowStatus_Type=ZhoneRowStatus
_ZhonePATBindRowStatus_Object=MibTableColumn
zhonePATBindRowStatus=_ZhonePATBindRowStatus_Object((1,3,6,1,4,1,5504,4,1,16,4,2,1,2),_ZhonePATBindRowStatus_Type())
zhonePATBindRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zhonePATBindRowStatus.setStatus(_A)
_PublicAddr_Type=IpAddress
_PublicAddr_Object=MibTableColumn
publicAddr=_PublicAddr_Object((1,3,6,1,4,1,5504,4,1,16,4,2,1,3),_PublicAddr_Type())
publicAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:publicAddr.setStatus(_A)
class _PublicPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(51921,56250))
_PublicPort_Type.__name__=_E
_PublicPort_Object=MibTableColumn
publicPort=_PublicPort_Object((1,3,6,1,4,1,5504,4,1,16,4,2,1,4),_PublicPort_Type())
publicPort.setMaxAccess(_B)
if mibBuilder.loadTexts:publicPort.setStatus(_A)
_LocalAddr_Type=IpAddress
_LocalAddr_Object=MibTableColumn
localAddr=_LocalAddr_Object((1,3,6,1,4,1,5504,4,1,16,4,2,1,5),_LocalAddr_Type())
localAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:localAddr.setStatus(_A)
class _LocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,49151))
_LocalPort_Type.__name__=_E
_LocalPort_Object=MibTableColumn
localPort=_LocalPort_Object((1,3,6,1,4,1,5504,4,1,16,4,2,1,6),_LocalPort_Type())
localPort.setMaxAccess(_B)
if mibBuilder.loadTexts:localPort.setStatus(_A)
class _PortType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tcp',1),('udp',2),('cpemgr',3),('cpemgrsecure',4)))
_PortType_Type.__name__=_E
_PortType_Object=MibTableColumn
portType=_PortType_Object((1,3,6,1,4,1,5504,4,1,16,4,2,1,7),_PortType_Type())
portType.setMaxAccess(_B)
if mibBuilder.loadTexts:portType.setStatus(_A)
_ZhoneNATExclusion_ObjectIdentity=ObjectIdentity
zhoneNATExclusion=_ZhoneNATExclusion_ObjectIdentity((1,3,6,1,4,1,5504,4,1,16,5))
_NatExcludeNextIndex_Type=Integer32
_NatExcludeNextIndex_Object=MibScalar
natExcludeNextIndex=_NatExcludeNextIndex_Object((1,3,6,1,4,1,5504,4,1,16,5,1),_NatExcludeNextIndex_Type())
natExcludeNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:natExcludeNextIndex.setStatus(_A)
_NatExcludeTable_Object=MibTable
natExcludeTable=_NatExcludeTable_Object((1,3,6,1,4,1,5504,4,1,16,5,2))
if mibBuilder.loadTexts:natExcludeTable.setStatus(_A)
_NatExcludeEntry_Object=MibTableRow
natExcludeEntry=_NatExcludeEntry_Object((1,3,6,1,4,1,5504,4,1,16,5,2,1))
natExcludeEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:natExcludeEntry.setStatus(_A)
class _ZhoneNATExcludeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_ZhoneNATExcludeIndex_Type.__name__=_E
_ZhoneNATExcludeIndex_Object=MibTableColumn
zhoneNATExcludeIndex=_ZhoneNATExcludeIndex_Object((1,3,6,1,4,1,5504,4,1,16,5,2,1,1),_ZhoneNATExcludeIndex_Type())
zhoneNATExcludeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneNATExcludeIndex.setStatus(_A)
_ZhoneNATExcludeRowStatus_Type=ZhoneRowStatus
_ZhoneNATExcludeRowStatus_Object=MibTableColumn
zhoneNATExcludeRowStatus=_ZhoneNATExcludeRowStatus_Object((1,3,6,1,4,1,5504,4,1,16,5,2,1,2),_ZhoneNATExcludeRowStatus_Type())
zhoneNATExcludeRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneNATExcludeRowStatus.setStatus(_A)
_IpStartAddr_Type=IpAddress
_IpStartAddr_Object=MibTableColumn
ipStartAddr=_IpStartAddr_Object((1,3,6,1,4,1,5504,4,1,16,5,2,1,3),_IpStartAddr_Type())
ipStartAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipStartAddr.setStatus(_A)
_IpEndAddr_Type=IpAddress
_IpEndAddr_Object=MibTableColumn
ipEndAddr=_IpEndAddr_Object((1,3,6,1,4,1,5504,4,1,16,5,2,1,4),_IpEndAddr_Type())
ipEndAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipEndAddr.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zedgeNat':zedgeNat,'natConfigGroup':natConfigGroup,'natTcpTimeout':natTcpTimeout,'natUdpTimeout':natUdpTimeout,'natClearBindings':natClearBindings,'natStatsGroup':natStatsGroup,'natNumCurrentBindings':natNumCurrentBindings,'natNumExpiredBindings':natNumExpiredBindings,'natTotalPkts':natTotalPkts,'natDroppedPkts':natDroppedPkts,'natBindingsTable':natBindingsTable,'natBindingsEntry':natBindingsEntry,_J:natBindingsIfIndex,_K:natBindingLocalAddr,_L:natBindingLocalPort,_M:natBindingPublicAddr,_N:natBindingPublicPort,'zhonePATBindings':zhonePATBindings,'patBindNextIndex':patBindNextIndex,'patTable':patTable,'patEntry':patEntry,_O:zhonePATBindIndex,'zhonePATBindRowStatus':zhonePATBindRowStatus,'publicAddr':publicAddr,'publicPort':publicPort,'localAddr':localAddr,'localPort':localPort,'portType':portType,'zhoneNATExclusion':zhoneNATExclusion,'natExcludeNextIndex':natExcludeNextIndex,'natExcludeTable':natExcludeTable,'natExcludeEntry':natExcludeEntry,_P:zhoneNATExcludeIndex,'zhoneNATExcludeRowStatus':zhoneNATExcludeRowStatus,'ipStartAddr':ipStartAddr,'ipEndAddr':ipEndAddr,'comIpZEdgeNat':comIpZEdgeNat})