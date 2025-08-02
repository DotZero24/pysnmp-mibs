_M='h3cVxlanStaticMacAddr'
_L='h3cVxlanMacAddr'
_K='read-write'
_J='Integer32'
_I='h3cVxlanVsiIndex'
_H='h3cVxlanTunnelID'
_G='h3cVxlanID'
_F='TruthValue'
_E='not-accessible'
_D='read-create'
_C='read-only'
_B='H3C-VXLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_F)
h3cVxlan=ModuleIdentity((1,3,6,1,4,1,2011,10,2,150))
if mibBuilder.loadTexts:h3cVxlan.setRevisions(('2015-02-11 09:00','2013-11-21 09:00'))
_H3cVxlanObjects_ObjectIdentity=ObjectIdentity
h3cVxlanObjects=_H3cVxlanObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,150,1))
_H3cVxlanScalarGroup_ObjectIdentity=ObjectIdentity
h3cVxlanScalarGroup=_H3cVxlanScalarGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,150,1,1))
class _H3cVxlanLocalMacNotify_Type(TruthValue):defaultValue=2
_H3cVxlanLocalMacNotify_Type.__name__=_F
_H3cVxlanLocalMacNotify_Object=MibScalar
h3cVxlanLocalMacNotify=_H3cVxlanLocalMacNotify_Object((1,3,6,1,4,1,2011,10,2,150,1,1,1),_H3cVxlanLocalMacNotify_Type())
h3cVxlanLocalMacNotify.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cVxlanLocalMacNotify.setStatus(_A)
class _H3cVxlanRemoteMacLearn_Type(TruthValue):defaultValue=1
_H3cVxlanRemoteMacLearn_Type.__name__=_F
_H3cVxlanRemoteMacLearn_Object=MibScalar
h3cVxlanRemoteMacLearn=_H3cVxlanRemoteMacLearn_Object((1,3,6,1,4,1,2011,10,2,150,1,1,2),_H3cVxlanRemoteMacLearn_Type())
h3cVxlanRemoteMacLearn.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cVxlanRemoteMacLearn.setStatus(_A)
_H3cVxlanNextVxlanID_Type=Unsigned32
_H3cVxlanNextVxlanID_Object=MibScalar
h3cVxlanNextVxlanID=_H3cVxlanNextVxlanID_Object((1,3,6,1,4,1,2011,10,2,150,1,1,3),_H3cVxlanNextVxlanID_Type())
h3cVxlanNextVxlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVxlanNextVxlanID.setStatus(_A)
_H3cVxlanConfigured_Type=Unsigned32
_H3cVxlanConfigured_Object=MibScalar
h3cVxlanConfigured=_H3cVxlanConfigured_Object((1,3,6,1,4,1,2011,10,2,150,1,1,4),_H3cVxlanConfigured_Type())
h3cVxlanConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVxlanConfigured.setStatus(_A)
_H3cVxlanTable_Object=MibTable
h3cVxlanTable=_H3cVxlanTable_Object((1,3,6,1,4,1,2011,10,2,150,1,2))
if mibBuilder.loadTexts:h3cVxlanTable.setStatus(_A)
_H3cVxlanEntry_Object=MibTableRow
h3cVxlanEntry=_H3cVxlanEntry_Object((1,3,6,1,4,1,2011,10,2,150,1,2,1))
h3cVxlanEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:h3cVxlanEntry.setStatus(_A)
_H3cVxlanID_Type=Unsigned32
_H3cVxlanID_Object=MibTableColumn
h3cVxlanID=_H3cVxlanID_Object((1,3,6,1,4,1,2011,10,2,150,1,2,1,1),_H3cVxlanID_Type())
h3cVxlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cVxlanID.setStatus(_A)
_H3cVxlanAddrType_Type=InetAddressType
_H3cVxlanAddrType_Object=MibTableColumn
h3cVxlanAddrType=_H3cVxlanAddrType_Object((1,3,6,1,4,1,2011,10,2,150,1,2,1,2),_H3cVxlanAddrType_Type())
h3cVxlanAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVxlanAddrType.setStatus(_A)
_H3cVxlanGroupAddr_Type=InetAddress
_H3cVxlanGroupAddr_Object=MibTableColumn
h3cVxlanGroupAddr=_H3cVxlanGroupAddr_Object((1,3,6,1,4,1,2011,10,2,150,1,2,1,3),_H3cVxlanGroupAddr_Type())
h3cVxlanGroupAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVxlanGroupAddr.setStatus(_A)
_H3cVxlanSourceAddr_Type=InetAddress
_H3cVxlanSourceAddr_Object=MibTableColumn
h3cVxlanSourceAddr=_H3cVxlanSourceAddr_Object((1,3,6,1,4,1,2011,10,2,150,1,2,1,4),_H3cVxlanSourceAddr_Type())
h3cVxlanSourceAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVxlanSourceAddr.setStatus(_A)
_H3cVxlanVsiIndex_Type=Unsigned32
_H3cVxlanVsiIndex_Object=MibTableColumn
h3cVxlanVsiIndex=_H3cVxlanVsiIndex_Object((1,3,6,1,4,1,2011,10,2,150,1,2,1,5),_H3cVxlanVsiIndex_Type())
h3cVxlanVsiIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVxlanVsiIndex.setStatus(_A)
_H3cVxlanRemoteMacCount_Type=Unsigned32
_H3cVxlanRemoteMacCount_Object=MibTableColumn
h3cVxlanRemoteMacCount=_H3cVxlanRemoteMacCount_Object((1,3,6,1,4,1,2011,10,2,150,1,2,1,6),_H3cVxlanRemoteMacCount_Type())
h3cVxlanRemoteMacCount.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVxlanRemoteMacCount.setStatus(_A)
_H3cVxlanRowStatus_Type=RowStatus
_H3cVxlanRowStatus_Object=MibTableColumn
h3cVxlanRowStatus=_H3cVxlanRowStatus_Object((1,3,6,1,4,1,2011,10,2,150,1,2,1,7),_H3cVxlanRowStatus_Type())
h3cVxlanRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVxlanRowStatus.setStatus(_A)
_H3cVxlanTunnelTable_Object=MibTable
h3cVxlanTunnelTable=_H3cVxlanTunnelTable_Object((1,3,6,1,4,1,2011,10,2,150,1,3))
if mibBuilder.loadTexts:h3cVxlanTunnelTable.setStatus(_A)
_H3cVxlanTunnelEntry_Object=MibTableRow
h3cVxlanTunnelEntry=_H3cVxlanTunnelEntry_Object((1,3,6,1,4,1,2011,10,2,150,1,3,1))
h3cVxlanTunnelEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:h3cVxlanTunnelEntry.setStatus(_A)
_H3cVxlanTunnelID_Type=Unsigned32
_H3cVxlanTunnelID_Object=MibTableColumn
h3cVxlanTunnelID=_H3cVxlanTunnelID_Object((1,3,6,1,4,1,2011,10,2,150,1,3,1,1),_H3cVxlanTunnelID_Type())
h3cVxlanTunnelID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cVxlanTunnelID.setStatus(_A)
_H3cVxlanTunnelRowStatus_Type=RowStatus
_H3cVxlanTunnelRowStatus_Object=MibTableColumn
h3cVxlanTunnelRowStatus=_H3cVxlanTunnelRowStatus_Object((1,3,6,1,4,1,2011,10,2,150,1,3,1,2),_H3cVxlanTunnelRowStatus_Type())
h3cVxlanTunnelRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVxlanTunnelRowStatus.setStatus(_A)
_H3cVxlanTunnelOctets_Type=Counter64
_H3cVxlanTunnelOctets_Object=MibTableColumn
h3cVxlanTunnelOctets=_H3cVxlanTunnelOctets_Object((1,3,6,1,4,1,2011,10,2,150,1,3,1,3),_H3cVxlanTunnelOctets_Type())
h3cVxlanTunnelOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVxlanTunnelOctets.setStatus(_A)
_H3cVxlanTunnelPackets_Type=Counter64
_H3cVxlanTunnelPackets_Object=MibTableColumn
h3cVxlanTunnelPackets=_H3cVxlanTunnelPackets_Object((1,3,6,1,4,1,2011,10,2,150,1,3,1,4),_H3cVxlanTunnelPackets_Type())
h3cVxlanTunnelPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVxlanTunnelPackets.setStatus(_A)
_H3cVxlanTunnelBoundTable_Object=MibTable
h3cVxlanTunnelBoundTable=_H3cVxlanTunnelBoundTable_Object((1,3,6,1,4,1,2011,10,2,150,1,4))
if mibBuilder.loadTexts:h3cVxlanTunnelBoundTable.setStatus(_A)
_H3cVxlanTunnelBoundEntry_Object=MibTableRow
h3cVxlanTunnelBoundEntry=_H3cVxlanTunnelBoundEntry_Object((1,3,6,1,4,1,2011,10,2,150,1,4,1))
h3cVxlanTunnelBoundEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:h3cVxlanTunnelBoundEntry.setStatus(_A)
_H3cVxlanTunnelBoundVxlanNum_Type=Unsigned32
_H3cVxlanTunnelBoundVxlanNum_Object=MibTableColumn
h3cVxlanTunnelBoundVxlanNum=_H3cVxlanTunnelBoundVxlanNum_Object((1,3,6,1,4,1,2011,10,2,150,1,4,1,1),_H3cVxlanTunnelBoundVxlanNum_Type())
h3cVxlanTunnelBoundVxlanNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVxlanTunnelBoundVxlanNum.setStatus(_A)
_H3cVxlanMacTable_Object=MibTable
h3cVxlanMacTable=_H3cVxlanMacTable_Object((1,3,6,1,4,1,2011,10,2,150,1,5))
if mibBuilder.loadTexts:h3cVxlanMacTable.setStatus(_A)
_H3cVxlanMacEntry_Object=MibTableRow
h3cVxlanMacEntry=_H3cVxlanMacEntry_Object((1,3,6,1,4,1,2011,10,2,150,1,5,1))
h3cVxlanMacEntry.setIndexNames((0,_B,_I),(0,_B,_L))
if mibBuilder.loadTexts:h3cVxlanMacEntry.setStatus(_A)
_H3cVxlanMacAddr_Type=MacAddress
_H3cVxlanMacAddr_Object=MibTableColumn
h3cVxlanMacAddr=_H3cVxlanMacAddr_Object((1,3,6,1,4,1,2011,10,2,150,1,5,1,1),_H3cVxlanMacAddr_Type())
h3cVxlanMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cVxlanMacAddr.setStatus(_A)
_H3cVxlanMacTunnelID_Type=Unsigned32
_H3cVxlanMacTunnelID_Object=MibTableColumn
h3cVxlanMacTunnelID=_H3cVxlanMacTunnelID_Object((1,3,6,1,4,1,2011,10,2,150,1,5,1,2),_H3cVxlanMacTunnelID_Type())
h3cVxlanMacTunnelID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVxlanMacTunnelID.setStatus(_A)
class _H3cVxlanMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('unknown',0),('selfLearned',1),('staticConfigured',2),('protocolLearned',3),('openflow',4),('ovsdb',5)))
_H3cVxlanMacType_Type.__name__=_J
_H3cVxlanMacType_Object=MibTableColumn
h3cVxlanMacType=_H3cVxlanMacType_Object((1,3,6,1,4,1,2011,10,2,150,1,5,1,3),_H3cVxlanMacType_Type())
h3cVxlanMacType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVxlanMacType.setStatus(_A)
_H3cVxlanStaticMacTable_Object=MibTable
h3cVxlanStaticMacTable=_H3cVxlanStaticMacTable_Object((1,3,6,1,4,1,2011,10,2,150,1,6))
if mibBuilder.loadTexts:h3cVxlanStaticMacTable.setStatus(_A)
_H3cVxlanStaticMacEntry_Object=MibTableRow
h3cVxlanStaticMacEntry=_H3cVxlanStaticMacEntry_Object((1,3,6,1,4,1,2011,10,2,150,1,6,1))
h3cVxlanStaticMacEntry.setIndexNames((0,_B,_I),(0,_B,_M))
if mibBuilder.loadTexts:h3cVxlanStaticMacEntry.setStatus(_A)
_H3cVxlanStaticMacAddr_Type=MacAddress
_H3cVxlanStaticMacAddr_Object=MibTableColumn
h3cVxlanStaticMacAddr=_H3cVxlanStaticMacAddr_Object((1,3,6,1,4,1,2011,10,2,150,1,6,1,1),_H3cVxlanStaticMacAddr_Type())
h3cVxlanStaticMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cVxlanStaticMacAddr.setStatus(_A)
_H3cVxlanStaticMacTunnelID_Type=Unsigned32
_H3cVxlanStaticMacTunnelID_Object=MibTableColumn
h3cVxlanStaticMacTunnelID=_H3cVxlanStaticMacTunnelID_Object((1,3,6,1,4,1,2011,10,2,150,1,6,1,2),_H3cVxlanStaticMacTunnelID_Type())
h3cVxlanStaticMacTunnelID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVxlanStaticMacTunnelID.setStatus(_A)
_H3cVxlanStaticMacRowStatus_Type=RowStatus
_H3cVxlanStaticMacRowStatus_Object=MibTableColumn
h3cVxlanStaticMacRowStatus=_H3cVxlanStaticMacRowStatus_Object((1,3,6,1,4,1,2011,10,2,150,1,6,1,3),_H3cVxlanStaticMacRowStatus_Type())
h3cVxlanStaticMacRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVxlanStaticMacRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cVxlan':h3cVxlan,'h3cVxlanObjects':h3cVxlanObjects,'h3cVxlanScalarGroup':h3cVxlanScalarGroup,'h3cVxlanLocalMacNotify':h3cVxlanLocalMacNotify,'h3cVxlanRemoteMacLearn':h3cVxlanRemoteMacLearn,'h3cVxlanNextVxlanID':h3cVxlanNextVxlanID,'h3cVxlanConfigured':h3cVxlanConfigured,'h3cVxlanTable':h3cVxlanTable,'h3cVxlanEntry':h3cVxlanEntry,_G:h3cVxlanID,'h3cVxlanAddrType':h3cVxlanAddrType,'h3cVxlanGroupAddr':h3cVxlanGroupAddr,'h3cVxlanSourceAddr':h3cVxlanSourceAddr,_I:h3cVxlanVsiIndex,'h3cVxlanRemoteMacCount':h3cVxlanRemoteMacCount,'h3cVxlanRowStatus':h3cVxlanRowStatus,'h3cVxlanTunnelTable':h3cVxlanTunnelTable,'h3cVxlanTunnelEntry':h3cVxlanTunnelEntry,_H:h3cVxlanTunnelID,'h3cVxlanTunnelRowStatus':h3cVxlanTunnelRowStatus,'h3cVxlanTunnelOctets':h3cVxlanTunnelOctets,'h3cVxlanTunnelPackets':h3cVxlanTunnelPackets,'h3cVxlanTunnelBoundTable':h3cVxlanTunnelBoundTable,'h3cVxlanTunnelBoundEntry':h3cVxlanTunnelBoundEntry,'h3cVxlanTunnelBoundVxlanNum':h3cVxlanTunnelBoundVxlanNum,'h3cVxlanMacTable':h3cVxlanMacTable,'h3cVxlanMacEntry':h3cVxlanMacEntry,_L:h3cVxlanMacAddr,'h3cVxlanMacTunnelID':h3cVxlanMacTunnelID,'h3cVxlanMacType':h3cVxlanMacType,'h3cVxlanStaticMacTable':h3cVxlanStaticMacTable,'h3cVxlanStaticMacEntry':h3cVxlanStaticMacEntry,_M:h3cVxlanStaticMacAddr,'h3cVxlanStaticMacTunnelID':h3cVxlanStaticMacTunnelID,'h3cVxlanStaticMacRowStatus':h3cVxlanStaticMacRowStatus})