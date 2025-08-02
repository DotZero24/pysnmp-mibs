_P='fsRstpPortGroup'
_O='fsRstpBridgeGroup'
_N='fsDot1dStpPortOperPointToPoint'
_M='fsDot1dStpPortAdminPointToPoint'
_L='fsDot1dStpPortOperEdgePort'
_K='fsDot1dStpPortAdminEdgePort'
_J='fsDot1dStpPortProtocolMigration'
_I='fsDot1dStpTxHoldCount'
_H='fsDot1dStpVersion'
_G='fsDot1dStpExtPortEntry'
_F='fsDot1dStpExtEntry'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='ARICENT-MIStdRSTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,Timeout,fsDot1dBridge,fsDot1dStp,fsDot1dStpEntry,fsDot1dStpPortEntry=mibBuilder.importSymbols('ARICENT-MIStdBRIDGE-MIB','BridgeId','Timeout','fsDot1dBridge','fsDot1dStp','fsDot1dStpEntry','fsDot1dStpPortEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
fsRstpMIB=ModuleIdentity((1,3,6,1,4,1,2076,116,11))
if mibBuilder.loadTexts:fsRstpMIB.setRevisions(('2012-09-05 00:00',))
_FsDot1dStpExtTable_Object=MibTable
fsDot1dStpExtTable=_FsDot1dStpExtTable_Object((1,3,6,1,4,1,2076,116,2,3))
if mibBuilder.loadTexts:fsDot1dStpExtTable.setStatus(_A)
_FsDot1dStpExtEntry_Object=MibTableRow
fsDot1dStpExtEntry=_FsDot1dStpExtEntry_Object((1,3,6,1,4,1,2076,116,2,3,1))
if mibBuilder.loadTexts:fsDot1dStpExtEntry.setStatus(_A)
class _FsDot1dStpVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*(('stpCompatible',0),('rstp',2)))
_FsDot1dStpVersion_Type.__name__=_D
_FsDot1dStpVersion_Object=MibTableColumn
fsDot1dStpVersion=_FsDot1dStpVersion_Object((1,3,6,1,4,1,2076,116,2,3,1,1),_FsDot1dStpVersion_Type())
fsDot1dStpVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1dStpVersion.setStatus(_A)
class _FsDot1dStpTxHoldCount_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FsDot1dStpTxHoldCount_Type.__name__=_D
_FsDot1dStpTxHoldCount_Object=MibTableColumn
fsDot1dStpTxHoldCount=_FsDot1dStpTxHoldCount_Object((1,3,6,1,4,1,2076,116,2,3,1,2),_FsDot1dStpTxHoldCount_Type())
fsDot1dStpTxHoldCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1dStpTxHoldCount.setStatus(_A)
class _FsDot1dStpPathCostDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stp8021d1998',1),('stp8021t2001',2)))
_FsDot1dStpPathCostDefault_Type.__name__=_D
_FsDot1dStpPathCostDefault_Object=MibTableColumn
fsDot1dStpPathCostDefault=_FsDot1dStpPathCostDefault_Object((1,3,6,1,4,1,2076,116,2,3,1,3),_FsDot1dStpPathCostDefault_Type())
fsDot1dStpPathCostDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1dStpPathCostDefault.setStatus('obsolete')
_FsDot1dStpExtPortTable_Object=MibTable
fsDot1dStpExtPortTable=_FsDot1dStpExtPortTable_Object((1,3,6,1,4,1,2076,116,2,4))
if mibBuilder.loadTexts:fsDot1dStpExtPortTable.setStatus(_A)
_FsDot1dStpExtPortEntry_Object=MibTableRow
fsDot1dStpExtPortEntry=_FsDot1dStpExtPortEntry_Object((1,3,6,1,4,1,2076,116,2,4,1))
if mibBuilder.loadTexts:fsDot1dStpExtPortEntry.setStatus(_A)
_FsDot1dStpPortProtocolMigration_Type=TruthValue
_FsDot1dStpPortProtocolMigration_Object=MibTableColumn
fsDot1dStpPortProtocolMigration=_FsDot1dStpPortProtocolMigration_Object((1,3,6,1,4,1,2076,116,2,4,1,1),_FsDot1dStpPortProtocolMigration_Type())
fsDot1dStpPortProtocolMigration.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1dStpPortProtocolMigration.setStatus(_A)
_FsDot1dStpPortAdminEdgePort_Type=TruthValue
_FsDot1dStpPortAdminEdgePort_Object=MibTableColumn
fsDot1dStpPortAdminEdgePort=_FsDot1dStpPortAdminEdgePort_Object((1,3,6,1,4,1,2076,116,2,4,1,2),_FsDot1dStpPortAdminEdgePort_Type())
fsDot1dStpPortAdminEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1dStpPortAdminEdgePort.setStatus(_A)
_FsDot1dStpPortOperEdgePort_Type=TruthValue
_FsDot1dStpPortOperEdgePort_Object=MibTableColumn
fsDot1dStpPortOperEdgePort=_FsDot1dStpPortOperEdgePort_Object((1,3,6,1,4,1,2076,116,2,4,1,3),_FsDot1dStpPortOperEdgePort_Type())
fsDot1dStpPortOperEdgePort.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot1dStpPortOperEdgePort.setStatus(_A)
class _FsDot1dStpPortAdminPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_FsDot1dStpPortAdminPointToPoint_Type.__name__=_D
_FsDot1dStpPortAdminPointToPoint_Object=MibTableColumn
fsDot1dStpPortAdminPointToPoint=_FsDot1dStpPortAdminPointToPoint_Object((1,3,6,1,4,1,2076,116,2,4,1,4),_FsDot1dStpPortAdminPointToPoint_Type())
fsDot1dStpPortAdminPointToPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1dStpPortAdminPointToPoint.setStatus(_A)
_FsDot1dStpPortOperPointToPoint_Type=TruthValue
_FsDot1dStpPortOperPointToPoint_Object=MibTableColumn
fsDot1dStpPortOperPointToPoint=_FsDot1dStpPortOperPointToPoint_Object((1,3,6,1,4,1,2076,116,2,4,1,5),_FsDot1dStpPortOperPointToPoint_Type())
fsDot1dStpPortOperPointToPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot1dStpPortOperPointToPoint.setStatus(_A)
class _FsDot1dStpPortAdminPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_FsDot1dStpPortAdminPathCost_Type.__name__=_D
_FsDot1dStpPortAdminPathCost_Object=MibTableColumn
fsDot1dStpPortAdminPathCost=_FsDot1dStpPortAdminPathCost_Object((1,3,6,1,4,1,2076,116,2,4,1,6),_FsDot1dStpPortAdminPathCost_Type())
fsDot1dStpPortAdminPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1dStpPortAdminPathCost.setStatus(_A)
_FsRstpMIBObjects_ObjectIdentity=ObjectIdentity
fsRstpMIBObjects=_FsRstpMIBObjects_ObjectIdentity((1,3,6,1,4,1,2076,116,11,1))
_FsRstpConformance_ObjectIdentity=ObjectIdentity
fsRstpConformance=_FsRstpConformance_ObjectIdentity((1,3,6,1,4,1,2076,116,11,2))
_FsRstpGroups_ObjectIdentity=ObjectIdentity
fsRstpGroups=_FsRstpGroups_ObjectIdentity((1,3,6,1,4,1,2076,116,11,2,1))
_FsRstpCompliances_ObjectIdentity=ObjectIdentity
fsRstpCompliances=_FsRstpCompliances_ObjectIdentity((1,3,6,1,4,1,2076,116,11,2,2))
fsDot1dStpEntry.registerAugmentions((_B,_F))
fsDot1dStpExtEntry.setIndexNames(*fsDot1dStpEntry.getIndexNames())
fsDot1dStpPortEntry.registerAugmentions((_B,_G))
fsDot1dStpExtPortEntry.setIndexNames(*fsDot1dStpPortEntry.getIndexNames())
fsRstpBridgeGroup=ObjectGroup((1,3,6,1,4,1,2076,116,11,2,1,1))
fsRstpBridgeGroup.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:fsRstpBridgeGroup.setStatus(_A)
fsRstpPortGroup=ObjectGroup((1,3,6,1,4,1,2076,116,11,2,1,2))
fsRstpPortGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:fsRstpPortGroup.setStatus(_A)
fsRstpCompliance=ModuleCompliance((1,3,6,1,4,1,2076,116,11,2,2,1))
fsRstpCompliance.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:fsRstpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsDot1dStpExtTable':fsDot1dStpExtTable,_F:fsDot1dStpExtEntry,_H:fsDot1dStpVersion,_I:fsDot1dStpTxHoldCount,'fsDot1dStpPathCostDefault':fsDot1dStpPathCostDefault,'fsDot1dStpExtPortTable':fsDot1dStpExtPortTable,_G:fsDot1dStpExtPortEntry,_J:fsDot1dStpPortProtocolMigration,_K:fsDot1dStpPortAdminEdgePort,_L:fsDot1dStpPortOperEdgePort,_M:fsDot1dStpPortAdminPointToPoint,_N:fsDot1dStpPortOperPointToPoint,'fsDot1dStpPortAdminPathCost':fsDot1dStpPortAdminPathCost,'fsRstpMIB':fsRstpMIB,'fsRstpMIBObjects':fsRstpMIBObjects,'fsRstpConformance':fsRstpConformance,'fsRstpGroups':fsRstpGroups,_O:fsRstpBridgeGroup,_P:fsRstpPortGroup,'fsRstpCompliances':fsRstpCompliances,'fsRstpCompliance':fsRstpCompliance})