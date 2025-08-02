_G='read-create'
_F='toIfIndex'
_E='fromIfIndex'
_D='read-write'
_C='NORTEL-OME40G-CNXN-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
nnOme40G,=mibBuilder.importSymbols('NORTEL-OME40G-MIB','nnOme40G')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
nnOme40GConnections=ModuleIdentity((1,3,6,1,4,1,562,68,11,3,2))
if mibBuilder.loadTexts:nnOme40GConnections.setRevisions(('2007-02-02 00:00','2008-02-07 00:00'))
_NnCrossConnects_ObjectIdentity=ObjectIdentity
nnCrossConnects=_NnCrossConnects_ObjectIdentity((1,3,6,1,4,1,562,68,11,3,2,1))
_NnCrossConnectsTable_Object=MibTable
nnCrossConnectsTable=_NnCrossConnectsTable_Object((1,3,6,1,4,1,562,68,11,3,2,1,1))
if mibBuilder.loadTexts:nnCrossConnectsTable.setStatus(_A)
_NnCrossConnectsEntry_Object=MibTableRow
nnCrossConnectsEntry=_NnCrossConnectsEntry_Object((1,3,6,1,4,1,562,68,11,3,2,1,1,1))
nnCrossConnectsEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:nnCrossConnectsEntry.setStatus(_A)
_FromIfIndex_Type=InterfaceIndex
_FromIfIndex_Object=MibTableColumn
fromIfIndex=_FromIfIndex_Object((1,3,6,1,4,1,562,68,11,3,2,1,1,1,1),_FromIfIndex_Type())
fromIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fromIfIndex.setStatus(_A)
_ToIfIndex_Type=InterfaceIndex
_ToIfIndex_Object=MibTableColumn
toIfIndex=_ToIfIndex_Object((1,3,6,1,4,1,562,68,11,3,2,1,1,1,2),_ToIfIndex_Type())
toIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:toIfIndex.setStatus(_A)
class _PayloadIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_PayloadIndex_Type.__name__=_B
_PayloadIndex_Object=MibTableColumn
payloadIndex=_PayloadIndex_Object((1,3,6,1,4,1,562,68,11,3,2,1,1,1,3),_PayloadIndex_Type())
payloadIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:payloadIndex.setStatus(_A)
_XcRowStatus_Type=RowStatus
_XcRowStatus_Object=MibTableColumn
xcRowStatus=_XcRowStatus_Object((1,3,6,1,4,1,562,68,11,3,2,1,1,1,4),_XcRowStatus_Type())
xcRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:xcRowStatus.setStatus(_A)
class _CrossConnectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('one-way',1),('two-way',2)))
_CrossConnectType_Type.__name__=_B
_CrossConnectType_Object=MibTableColumn
crossConnectType=_CrossConnectType_Object((1,3,6,1,4,1,562,68,11,3,2,1,1,1,5),_CrossConnectType_Type())
crossConnectType.setMaxAccess(_D)
if mibBuilder.loadTexts:crossConnectType.setStatus(_A)
_CrossConnectName_Type=DisplayString
_CrossConnectName_Object=MibTableColumn
crossConnectName=_CrossConnectName_Object((1,3,6,1,4,1,562,68,11,3,2,1,1,1,6),_CrossConnectName_Type())
crossConnectName.setMaxAccess(_D)
if mibBuilder.loadTexts:crossConnectName.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'nnOme40GConnections':nnOme40GConnections,'nnCrossConnects':nnCrossConnects,'nnCrossConnectsTable':nnCrossConnectsTable,'nnCrossConnectsEntry':nnCrossConnectsEntry,_E:fromIfIndex,_F:toIfIndex,'payloadIndex':payloadIndex,'xcRowStatus':xcRowStatus,'crossConnectType':crossConnectType,'crossConnectName':crossConnectName})