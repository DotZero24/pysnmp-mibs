_M='a3ComTrunkPeersMacAddress'
_L='a3ComTrunkPeerMacIndex'
_K='a3ComTrunkPeerTrunkIfIndex'
_J='read-only'
_I='a3ComTrunkMacIndex'
_H='a3ComTrunkMacTrunkIfIndex'
_G='a3ComTrunkIfIndex'
_F='DisplayString'
_E='read-write'
_D='Integer32'
_C='not-accessible'
_B='GENERIC-3COM-TRUNK-MIB'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
class RowStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('active',1),('notInService',2),('notReady',3),('createAndGo',4),('createAndWait',5),('destroy',6)))
_A3Com_ObjectIdentity=ObjectIdentity
a3Com=_A3Com_ObjectIdentity((1,3,6,1,4,1,43))
_Generic_ObjectIdentity=ObjectIdentity
generic=_Generic_ObjectIdentity((1,3,6,1,4,1,43,10))
_GenExperimental_ObjectIdentity=ObjectIdentity
genExperimental=_GenExperimental_ObjectIdentity((1,3,6,1,4,1,43,10,1))
_GenTrunk_ObjectIdentity=ObjectIdentity
genTrunk=_GenTrunk_ObjectIdentity((1,3,6,1,4,1,43,10,1,15))
_A3ComTrunkGroup_ObjectIdentity=ObjectIdentity
a3ComTrunkGroup=_A3ComTrunkGroup_ObjectIdentity((1,3,6,1,4,1,43,10,1,15,1))
_A3ComTrunkIfTable_Object=MibTable
a3ComTrunkIfTable=_A3ComTrunkIfTable_Object((1,3,6,1,4,1,43,10,1,15,1,1))
if mibBuilder.loadTexts:a3ComTrunkIfTable.setStatus(_A)
_A3ComTrunkIfEntry_Object=MibTableRow
a3ComTrunkIfEntry=_A3ComTrunkIfEntry_Object((1,3,6,1,4,1,43,10,1,15,1,1,1))
a3ComTrunkIfEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:a3ComTrunkIfEntry.setStatus(_A)
_A3ComTrunkIfIndex_Type=Integer32
_A3ComTrunkIfIndex_Object=MibTableColumn
a3ComTrunkIfIndex=_A3ComTrunkIfIndex_Object((1,3,6,1,4,1,43,10,1,15,1,1,1,1),_A3ComTrunkIfIndex_Type())
a3ComTrunkIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComTrunkIfIndex.setStatus(_A)
class _A3ComTrunkIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_A3ComTrunkIfName_Type.__name__=_F
_A3ComTrunkIfName_Object=MibTableColumn
a3ComTrunkIfName=_A3ComTrunkIfName_Object((1,3,6,1,4,1,43,10,1,15,1,1,1,2),_A3ComTrunkIfName_Type())
a3ComTrunkIfName.setMaxAccess(_E)
if mibBuilder.loadTexts:a3ComTrunkIfName.setStatus(_A)
class _A3ComTrunkTcmpEnable_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notAvailable',1),('tcmpDisable',2),('tcmpEnable',3)))
_A3ComTrunkTcmpEnable_Type.__name__=_D
_A3ComTrunkTcmpEnable_Object=MibTableColumn
a3ComTrunkTcmpEnable=_A3ComTrunkTcmpEnable_Object((1,3,6,1,4,1,43,10,1,15,1,1,1,3),_A3ComTrunkTcmpEnable_Type())
a3ComTrunkTcmpEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:a3ComTrunkTcmpEnable.setStatus(_A)
class _A3ComTrunkMacMode_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('half10',1),('full10',2),('half100',3),('full100',4),('half1000',5),('full1000',6)))
_A3ComTrunkMacMode_Type.__name__=_D
_A3ComTrunkMacMode_Object=MibTableColumn
a3ComTrunkMacMode=_A3ComTrunkMacMode_Object((1,3,6,1,4,1,43,10,1,15,1,1,1,4),_A3ComTrunkMacMode_Type())
a3ComTrunkMacMode.setMaxAccess(_E)
if mibBuilder.loadTexts:a3ComTrunkMacMode.setStatus(_A)
_A3ComTrunkIfStatus_Type=RowStatus
_A3ComTrunkIfStatus_Object=MibTableColumn
a3ComTrunkIfStatus=_A3ComTrunkIfStatus_Object((1,3,6,1,4,1,43,10,1,15,1,1,1,5),_A3ComTrunkIfStatus_Type())
a3ComTrunkIfStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:a3ComTrunkIfStatus.setStatus(_A)
_A3ComTrunkMacTable_Object=MibTable
a3ComTrunkMacTable=_A3ComTrunkMacTable_Object((1,3,6,1,4,1,43,10,1,15,1,2))
if mibBuilder.loadTexts:a3ComTrunkMacTable.setStatus(_A)
_A3ComTrunkMacEntry_Object=MibTableRow
a3ComTrunkMacEntry=_A3ComTrunkMacEntry_Object((1,3,6,1,4,1,43,10,1,15,1,2,1))
a3ComTrunkMacEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:a3ComTrunkMacEntry.setStatus(_A)
_A3ComTrunkMacTrunkIfIndex_Type=Integer32
_A3ComTrunkMacTrunkIfIndex_Object=MibTableColumn
a3ComTrunkMacTrunkIfIndex=_A3ComTrunkMacTrunkIfIndex_Object((1,3,6,1,4,1,43,10,1,15,1,2,1,1),_A3ComTrunkMacTrunkIfIndex_Type())
a3ComTrunkMacTrunkIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComTrunkMacTrunkIfIndex.setStatus(_A)
_A3ComTrunkMacIndex_Type=Integer32
_A3ComTrunkMacIndex_Object=MibTableColumn
a3ComTrunkMacIndex=_A3ComTrunkMacIndex_Object((1,3,6,1,4,1,43,10,1,15,1,2,1,2),_A3ComTrunkMacIndex_Type())
a3ComTrunkMacIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComTrunkMacIndex.setStatus(_A)
class _A3ComTrunkTcmpMacState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('notInUse',1),('selected',2),('inUse',3),('undefined',4),('down',5),('up',6),('configured',7)))
_A3ComTrunkTcmpMacState_Type.__name__=_D
_A3ComTrunkTcmpMacState_Object=MibTableColumn
a3ComTrunkTcmpMacState=_A3ComTrunkTcmpMacState_Object((1,3,6,1,4,1,43,10,1,15,1,2,1,3),_A3ComTrunkTcmpMacState_Type())
a3ComTrunkTcmpMacState.setMaxAccess(_J)
if mibBuilder.loadTexts:a3ComTrunkTcmpMacState.setStatus(_A)
_A3ComTrunkTcmpPeersTable_Object=MibTable
a3ComTrunkTcmpPeersTable=_A3ComTrunkTcmpPeersTable_Object((1,3,6,1,4,1,43,10,1,15,1,3))
if mibBuilder.loadTexts:a3ComTrunkTcmpPeersTable.setStatus(_A)
_A3ComTrunkTcmpPeersEntry_Object=MibTableRow
a3ComTrunkTcmpPeersEntry=_A3ComTrunkTcmpPeersEntry_Object((1,3,6,1,4,1,43,10,1,15,1,3,1))
a3ComTrunkTcmpPeersEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:a3ComTrunkTcmpPeersEntry.setStatus(_A)
_A3ComTrunkPeerTrunkIfIndex_Type=Integer32
_A3ComTrunkPeerTrunkIfIndex_Object=MibTableColumn
a3ComTrunkPeerTrunkIfIndex=_A3ComTrunkPeerTrunkIfIndex_Object((1,3,6,1,4,1,43,10,1,15,1,3,1,1),_A3ComTrunkPeerTrunkIfIndex_Type())
a3ComTrunkPeerTrunkIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComTrunkPeerTrunkIfIndex.setStatus(_A)
_A3ComTrunkPeerMacIndex_Type=Integer32
_A3ComTrunkPeerMacIndex_Object=MibTableColumn
a3ComTrunkPeerMacIndex=_A3ComTrunkPeerMacIndex_Object((1,3,6,1,4,1,43,10,1,15,1,3,1,2),_A3ComTrunkPeerMacIndex_Type())
a3ComTrunkPeerMacIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComTrunkPeerMacIndex.setStatus(_A)
_A3ComTrunkPeersMacAddress_Type=PhysAddress
_A3ComTrunkPeersMacAddress_Object=MibTableColumn
a3ComTrunkPeersMacAddress=_A3ComTrunkPeersMacAddress_Object((1,3,6,1,4,1,43,10,1,15,1,3,1,3),_A3ComTrunkPeersMacAddress_Type())
a3ComTrunkPeersMacAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:a3ComTrunkPeersMacAddress.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'RowStatus':RowStatus,'a3Com':a3Com,'generic':generic,'genExperimental':genExperimental,'genTrunk':genTrunk,'a3ComTrunkGroup':a3ComTrunkGroup,'a3ComTrunkIfTable':a3ComTrunkIfTable,'a3ComTrunkIfEntry':a3ComTrunkIfEntry,_G:a3ComTrunkIfIndex,'a3ComTrunkIfName':a3ComTrunkIfName,'a3ComTrunkTcmpEnable':a3ComTrunkTcmpEnable,'a3ComTrunkMacMode':a3ComTrunkMacMode,'a3ComTrunkIfStatus':a3ComTrunkIfStatus,'a3ComTrunkMacTable':a3ComTrunkMacTable,'a3ComTrunkMacEntry':a3ComTrunkMacEntry,_H:a3ComTrunkMacTrunkIfIndex,_I:a3ComTrunkMacIndex,'a3ComTrunkTcmpMacState':a3ComTrunkTcmpMacState,'a3ComTrunkTcmpPeersTable':a3ComTrunkTcmpPeersTable,'a3ComTrunkTcmpPeersEntry':a3ComTrunkTcmpPeersEntry,_K:a3ComTrunkPeerTrunkIfIndex,_L:a3ComTrunkPeerMacIndex,_M:a3ComTrunkPeersMacAddress})