_I='swL2PTProtocolIndex'
_H='mac-01-00-0C-CC-CC-CD'
_G='mac-01-00-0C-CC-CC-CC'
_F='not-accessible'
_E='swL2PTPortIndex'
_D='L2PROTOCOL-TUNNEL-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
swL2ProtocolTunnelMIB=ModuleIdentity((1,3,6,1,4,1,171,12,93))
_SwL2PTMIBObjects_ObjectIdentity=ObjectIdentity
swL2PTMIBObjects=_SwL2PTMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,12,93,1))
class _SwL2PTState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_SwL2PTState_Type.__name__=_B
_SwL2PTState_Object=MibScalar
swL2PTState=_SwL2PTState_Object((1,3,6,1,4,1,171,12,93,1,1),_SwL2PTState_Type())
swL2PTState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PTState.setStatus(_A)
_SwL2PTPortTable_Object=MibTable
swL2PTPortTable=_SwL2PTPortTable_Object((1,3,6,1,4,1,171,12,93,1,2))
if mibBuilder.loadTexts:swL2PTPortTable.setStatus(_A)
_SwL2PTPortEntry_Object=MibTableRow
swL2PTPortEntry=_SwL2PTPortEntry_Object((1,3,6,1,4,1,171,12,93,1,2,1))
swL2PTPortEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:swL2PTPortEntry.setStatus(_A)
_SwL2PTPortIndex_Type=Integer32
_SwL2PTPortIndex_Object=MibTableColumn
swL2PTPortIndex=_SwL2PTPortIndex_Object((1,3,6,1,4,1,171,12,93,1,2,1,1),_SwL2PTPortIndex_Type())
swL2PTPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:swL2PTPortIndex.setStatus(_A)
class _SwL2PTPortType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('uni',2),('nni',3)))
_SwL2PTPortType_Type.__name__=_B
_SwL2PTPortType_Object=MibTableColumn
swL2PTPortType=_SwL2PTPortType_Object((1,3,6,1,4,1,171,12,93,1,2,1,2),_SwL2PTPortType_Type())
swL2PTPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PTPortType.setStatus(_A)
class _SwL2PTProtocol_Type(Bits):namedValues=NamedValues(*(('stp',0),('gvrp',1),(_G,2),(_H,3)))
_SwL2PTProtocol_Type.__name__='Bits'
_SwL2PTProtocol_Object=MibTableColumn
swL2PTProtocol=_SwL2PTProtocol_Object((1,3,6,1,4,1,171,12,93,1,2,1,3),_SwL2PTProtocol_Type())
swL2PTProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PTProtocol.setStatus(_A)
_SwL2PTThresholdTable_Object=MibTable
swL2PTThresholdTable=_SwL2PTThresholdTable_Object((1,3,6,1,4,1,171,12,93,1,3))
if mibBuilder.loadTexts:swL2PTThresholdTable.setStatus(_A)
_SwL2PTThresholdEntry_Object=MibTableRow
swL2PTThresholdEntry=_SwL2PTThresholdEntry_Object((1,3,6,1,4,1,171,12,93,1,3,1))
swL2PTThresholdEntry.setIndexNames((0,_D,_E),(0,_D,_I))
if mibBuilder.loadTexts:swL2PTThresholdEntry.setStatus(_A)
class _SwL2PTProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('stp',1),('gvrp',2),(_G,3),(_H,4)))
_SwL2PTProtocolIndex_Type.__name__=_B
_SwL2PTProtocolIndex_Object=MibTableColumn
swL2PTProtocolIndex=_SwL2PTProtocolIndex_Object((1,3,6,1,4,1,171,12,93,1,3,1,1),_SwL2PTProtocolIndex_Type())
swL2PTProtocolIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:swL2PTProtocolIndex.setStatus(_A)
class _SwL2PTDropThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PTDropThreshold_Type.__name__=_B
_SwL2PTDropThreshold_Object=MibTableColumn
swL2PTDropThreshold=_SwL2PTDropThreshold_Object((1,3,6,1,4,1,171,12,93,1,3,1,2),_SwL2PTDropThreshold_Type())
swL2PTDropThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PTDropThreshold.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'swL2ProtocolTunnelMIB':swL2ProtocolTunnelMIB,'swL2PTMIBObjects':swL2PTMIBObjects,'swL2PTState':swL2PTState,'swL2PTPortTable':swL2PTPortTable,'swL2PTPortEntry':swL2PTPortEntry,_E:swL2PTPortIndex,'swL2PTPortType':swL2PTPortType,'swL2PTProtocol':swL2PTProtocol,'swL2PTThresholdTable':swL2PTThresholdTable,'swL2PTThresholdEntry':swL2PTThresholdEntry,_I:swL2PTProtocolIndex,'swL2PTDropThreshold':swL2PTDropThreshold})