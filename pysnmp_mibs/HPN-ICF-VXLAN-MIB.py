_M='hpnicfVxlanStaticMacAddr'
_L='hpnicfVxlanMacAddr'
_K='read-write'
_J='Integer32'
_I='hpnicfVxlanVsiIndex'
_H='hpnicfVxlanTunnelID'
_G='hpnicfVxlanID'
_F='TruthValue'
_E='not-accessible'
_D='read-create'
_C='read-only'
_B='HPN-ICF-VXLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_F)
hpnicfVxlan=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,150))
if mibBuilder.loadTexts:hpnicfVxlan.setRevisions(('2013-11-21 09:00',))
_HpnicfVxlanObjects_ObjectIdentity=ObjectIdentity
hpnicfVxlanObjects=_HpnicfVxlanObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,150,1))
_HpnicfVxlanScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfVxlanScalarGroup=_HpnicfVxlanScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,150,1,1))
class _HpnicfVxlanLocalMacNotify_Type(TruthValue):defaultValue=2
_HpnicfVxlanLocalMacNotify_Type.__name__=_F
_HpnicfVxlanLocalMacNotify_Object=MibScalar
hpnicfVxlanLocalMacNotify=_HpnicfVxlanLocalMacNotify_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,1,1),_HpnicfVxlanLocalMacNotify_Type())
hpnicfVxlanLocalMacNotify.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfVxlanLocalMacNotify.setStatus(_A)
class _HpnicfVxlanRemoteMacLearn_Type(TruthValue):defaultValue=1
_HpnicfVxlanRemoteMacLearn_Type.__name__=_F
_HpnicfVxlanRemoteMacLearn_Object=MibScalar
hpnicfVxlanRemoteMacLearn=_HpnicfVxlanRemoteMacLearn_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,1,2),_HpnicfVxlanRemoteMacLearn_Type())
hpnicfVxlanRemoteMacLearn.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfVxlanRemoteMacLearn.setStatus(_A)
_HpnicfVxlanNextVxlanID_Type=Unsigned32
_HpnicfVxlanNextVxlanID_Object=MibScalar
hpnicfVxlanNextVxlanID=_HpnicfVxlanNextVxlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,1,3),_HpnicfVxlanNextVxlanID_Type())
hpnicfVxlanNextVxlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVxlanNextVxlanID.setStatus(_A)
_HpnicfVxlanConfigured_Type=Unsigned32
_HpnicfVxlanConfigured_Object=MibScalar
hpnicfVxlanConfigured=_HpnicfVxlanConfigured_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,1,4),_HpnicfVxlanConfigured_Type())
hpnicfVxlanConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVxlanConfigured.setStatus(_A)
_HpnicfVxlanTable_Object=MibTable
hpnicfVxlanTable=_HpnicfVxlanTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,2))
if mibBuilder.loadTexts:hpnicfVxlanTable.setStatus(_A)
_HpnicfVxlanEntry_Object=MibTableRow
hpnicfVxlanEntry=_HpnicfVxlanEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,2,1))
hpnicfVxlanEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hpnicfVxlanEntry.setStatus(_A)
_HpnicfVxlanID_Type=Unsigned32
_HpnicfVxlanID_Object=MibTableColumn
hpnicfVxlanID=_HpnicfVxlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,2,1,1),_HpnicfVxlanID_Type())
hpnicfVxlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfVxlanID.setStatus(_A)
_HpnicfVxlanAddrType_Type=InetAddressType
_HpnicfVxlanAddrType_Object=MibTableColumn
hpnicfVxlanAddrType=_HpnicfVxlanAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,2,1,2),_HpnicfVxlanAddrType_Type())
hpnicfVxlanAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVxlanAddrType.setStatus(_A)
_HpnicfVxlanGroupAddr_Type=InetAddress
_HpnicfVxlanGroupAddr_Object=MibTableColumn
hpnicfVxlanGroupAddr=_HpnicfVxlanGroupAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,2,1,3),_HpnicfVxlanGroupAddr_Type())
hpnicfVxlanGroupAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVxlanGroupAddr.setStatus(_A)
_HpnicfVxlanSourceAddr_Type=InetAddress
_HpnicfVxlanSourceAddr_Object=MibTableColumn
hpnicfVxlanSourceAddr=_HpnicfVxlanSourceAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,2,1,4),_HpnicfVxlanSourceAddr_Type())
hpnicfVxlanSourceAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVxlanSourceAddr.setStatus(_A)
_HpnicfVxlanVsiIndex_Type=Unsigned32
_HpnicfVxlanVsiIndex_Object=MibTableColumn
hpnicfVxlanVsiIndex=_HpnicfVxlanVsiIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,2,1,5),_HpnicfVxlanVsiIndex_Type())
hpnicfVxlanVsiIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVxlanVsiIndex.setStatus(_A)
_HpnicfVxlanRemoteMacCount_Type=Unsigned32
_HpnicfVxlanRemoteMacCount_Object=MibTableColumn
hpnicfVxlanRemoteMacCount=_HpnicfVxlanRemoteMacCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,2,1,6),_HpnicfVxlanRemoteMacCount_Type())
hpnicfVxlanRemoteMacCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVxlanRemoteMacCount.setStatus(_A)
_HpnicfVxlanRowStatus_Type=RowStatus
_HpnicfVxlanRowStatus_Object=MibTableColumn
hpnicfVxlanRowStatus=_HpnicfVxlanRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,2,1,7),_HpnicfVxlanRowStatus_Type())
hpnicfVxlanRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVxlanRowStatus.setStatus(_A)
_HpnicfVxlanTunnelTable_Object=MibTable
hpnicfVxlanTunnelTable=_HpnicfVxlanTunnelTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,3))
if mibBuilder.loadTexts:hpnicfVxlanTunnelTable.setStatus(_A)
_HpnicfVxlanTunnelEntry_Object=MibTableRow
hpnicfVxlanTunnelEntry=_HpnicfVxlanTunnelEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,3,1))
hpnicfVxlanTunnelEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:hpnicfVxlanTunnelEntry.setStatus(_A)
_HpnicfVxlanTunnelID_Type=Unsigned32
_HpnicfVxlanTunnelID_Object=MibTableColumn
hpnicfVxlanTunnelID=_HpnicfVxlanTunnelID_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,3,1,1),_HpnicfVxlanTunnelID_Type())
hpnicfVxlanTunnelID.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfVxlanTunnelID.setStatus(_A)
_HpnicfVxlanTunnelRowStatus_Type=RowStatus
_HpnicfVxlanTunnelRowStatus_Object=MibTableColumn
hpnicfVxlanTunnelRowStatus=_HpnicfVxlanTunnelRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,3,1,2),_HpnicfVxlanTunnelRowStatus_Type())
hpnicfVxlanTunnelRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVxlanTunnelRowStatus.setStatus(_A)
_HpnicfVxlanTunnelOctets_Type=Counter64
_HpnicfVxlanTunnelOctets_Object=MibTableColumn
hpnicfVxlanTunnelOctets=_HpnicfVxlanTunnelOctets_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,3,1,3),_HpnicfVxlanTunnelOctets_Type())
hpnicfVxlanTunnelOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVxlanTunnelOctets.setStatus(_A)
_HpnicfVxlanTunnelPackets_Type=Counter64
_HpnicfVxlanTunnelPackets_Object=MibTableColumn
hpnicfVxlanTunnelPackets=_HpnicfVxlanTunnelPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,3,1,4),_HpnicfVxlanTunnelPackets_Type())
hpnicfVxlanTunnelPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVxlanTunnelPackets.setStatus(_A)
_HpnicfVxlanTunnelBoundTable_Object=MibTable
hpnicfVxlanTunnelBoundTable=_HpnicfVxlanTunnelBoundTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,4))
if mibBuilder.loadTexts:hpnicfVxlanTunnelBoundTable.setStatus(_A)
_HpnicfVxlanTunnelBoundEntry_Object=MibTableRow
hpnicfVxlanTunnelBoundEntry=_HpnicfVxlanTunnelBoundEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,4,1))
hpnicfVxlanTunnelBoundEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfVxlanTunnelBoundEntry.setStatus(_A)
_HpnicfVxlanTunnelBoundVxlanNum_Type=Unsigned32
_HpnicfVxlanTunnelBoundVxlanNum_Object=MibTableColumn
hpnicfVxlanTunnelBoundVxlanNum=_HpnicfVxlanTunnelBoundVxlanNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,4,1,1),_HpnicfVxlanTunnelBoundVxlanNum_Type())
hpnicfVxlanTunnelBoundVxlanNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVxlanTunnelBoundVxlanNum.setStatus(_A)
_HpnicfVxlanMacTable_Object=MibTable
hpnicfVxlanMacTable=_HpnicfVxlanMacTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,5))
if mibBuilder.loadTexts:hpnicfVxlanMacTable.setStatus(_A)
_HpnicfVxlanMacEntry_Object=MibTableRow
hpnicfVxlanMacEntry=_HpnicfVxlanMacEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,5,1))
hpnicfVxlanMacEntry.setIndexNames((0,_B,_I),(0,_B,_L))
if mibBuilder.loadTexts:hpnicfVxlanMacEntry.setStatus(_A)
_HpnicfVxlanMacAddr_Type=MacAddress
_HpnicfVxlanMacAddr_Object=MibTableColumn
hpnicfVxlanMacAddr=_HpnicfVxlanMacAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,5,1,1),_HpnicfVxlanMacAddr_Type())
hpnicfVxlanMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfVxlanMacAddr.setStatus(_A)
_HpnicfVxlanMacTunnelID_Type=Unsigned32
_HpnicfVxlanMacTunnelID_Object=MibTableColumn
hpnicfVxlanMacTunnelID=_HpnicfVxlanMacTunnelID_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,5,1,2),_HpnicfVxlanMacTunnelID_Type())
hpnicfVxlanMacTunnelID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVxlanMacTunnelID.setStatus(_A)
class _HpnicfVxlanMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('selfLearned',1),('staticConfigured',2),('protocolLearned',3)))
_HpnicfVxlanMacType_Type.__name__=_J
_HpnicfVxlanMacType_Object=MibTableColumn
hpnicfVxlanMacType=_HpnicfVxlanMacType_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,5,1,3),_HpnicfVxlanMacType_Type())
hpnicfVxlanMacType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVxlanMacType.setStatus(_A)
_HpnicfVxlanStaticMacTable_Object=MibTable
hpnicfVxlanStaticMacTable=_HpnicfVxlanStaticMacTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,6))
if mibBuilder.loadTexts:hpnicfVxlanStaticMacTable.setStatus(_A)
_HpnicfVxlanStaticMacEntry_Object=MibTableRow
hpnicfVxlanStaticMacEntry=_HpnicfVxlanStaticMacEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,6,1))
hpnicfVxlanStaticMacEntry.setIndexNames((0,_B,_I),(0,_B,_M))
if mibBuilder.loadTexts:hpnicfVxlanStaticMacEntry.setStatus(_A)
_HpnicfVxlanStaticMacAddr_Type=MacAddress
_HpnicfVxlanStaticMacAddr_Object=MibTableColumn
hpnicfVxlanStaticMacAddr=_HpnicfVxlanStaticMacAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,6,1,1),_HpnicfVxlanStaticMacAddr_Type())
hpnicfVxlanStaticMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfVxlanStaticMacAddr.setStatus(_A)
_HpnicfVxlanStaticMacTunnelID_Type=Unsigned32
_HpnicfVxlanStaticMacTunnelID_Object=MibTableColumn
hpnicfVxlanStaticMacTunnelID=_HpnicfVxlanStaticMacTunnelID_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,6,1,2),_HpnicfVxlanStaticMacTunnelID_Type())
hpnicfVxlanStaticMacTunnelID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVxlanStaticMacTunnelID.setStatus(_A)
_HpnicfVxlanStaticMacRowStatus_Type=RowStatus
_HpnicfVxlanStaticMacRowStatus_Object=MibTableColumn
hpnicfVxlanStaticMacRowStatus=_HpnicfVxlanStaticMacRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,150,1,6,1,3),_HpnicfVxlanStaticMacRowStatus_Type())
hpnicfVxlanStaticMacRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfVxlanStaticMacRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfVxlan':hpnicfVxlan,'hpnicfVxlanObjects':hpnicfVxlanObjects,'hpnicfVxlanScalarGroup':hpnicfVxlanScalarGroup,'hpnicfVxlanLocalMacNotify':hpnicfVxlanLocalMacNotify,'hpnicfVxlanRemoteMacLearn':hpnicfVxlanRemoteMacLearn,'hpnicfVxlanNextVxlanID':hpnicfVxlanNextVxlanID,'hpnicfVxlanConfigured':hpnicfVxlanConfigured,'hpnicfVxlanTable':hpnicfVxlanTable,'hpnicfVxlanEntry':hpnicfVxlanEntry,_G:hpnicfVxlanID,'hpnicfVxlanAddrType':hpnicfVxlanAddrType,'hpnicfVxlanGroupAddr':hpnicfVxlanGroupAddr,'hpnicfVxlanSourceAddr':hpnicfVxlanSourceAddr,_I:hpnicfVxlanVsiIndex,'hpnicfVxlanRemoteMacCount':hpnicfVxlanRemoteMacCount,'hpnicfVxlanRowStatus':hpnicfVxlanRowStatus,'hpnicfVxlanTunnelTable':hpnicfVxlanTunnelTable,'hpnicfVxlanTunnelEntry':hpnicfVxlanTunnelEntry,_H:hpnicfVxlanTunnelID,'hpnicfVxlanTunnelRowStatus':hpnicfVxlanTunnelRowStatus,'hpnicfVxlanTunnelOctets':hpnicfVxlanTunnelOctets,'hpnicfVxlanTunnelPackets':hpnicfVxlanTunnelPackets,'hpnicfVxlanTunnelBoundTable':hpnicfVxlanTunnelBoundTable,'hpnicfVxlanTunnelBoundEntry':hpnicfVxlanTunnelBoundEntry,'hpnicfVxlanTunnelBoundVxlanNum':hpnicfVxlanTunnelBoundVxlanNum,'hpnicfVxlanMacTable':hpnicfVxlanMacTable,'hpnicfVxlanMacEntry':hpnicfVxlanMacEntry,_L:hpnicfVxlanMacAddr,'hpnicfVxlanMacTunnelID':hpnicfVxlanMacTunnelID,'hpnicfVxlanMacType':hpnicfVxlanMacType,'hpnicfVxlanStaticMacTable':hpnicfVxlanStaticMacTable,'hpnicfVxlanStaticMacEntry':hpnicfVxlanStaticMacEntry,_M:hpnicfVxlanStaticMacAddr,'hpnicfVxlanStaticMacTunnelID':hpnicfVxlanStaticMacTunnelID,'hpnicfVxlanStaticMacRowStatus':hpnicfVxlanStaticMacRowStatus})