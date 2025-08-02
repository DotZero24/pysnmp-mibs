_F='read-only'
_E='agentFeatureKeyingIndex'
_D='NETGEAR-KEYING-PRIVATE-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ng7000managedswitch,=mibBuilder.importSymbols('NETGEAR-REF-MIB','ng7000managedswitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','TextualConvention')
fastPathKeyingPrivate=ModuleIdentity((1,3,6,1,4,1,4526,10,24))
if mibBuilder.loadTexts:fastPathKeyingPrivate.setRevisions(('2011-01-26 00:00','2007-05-23 00:00'))
_AgentFeatureKeyingGroup_ObjectIdentity=ObjectIdentity
agentFeatureKeyingGroup=_AgentFeatureKeyingGroup_ObjectIdentity((1,3,6,1,4,1,4526,10,24,1))
_AgentFeatureKeyingEnableKey_Type=DisplayString
_AgentFeatureKeyingEnableKey_Object=MibScalar
agentFeatureKeyingEnableKey=_AgentFeatureKeyingEnableKey_Object((1,3,6,1,4,1,4526,10,24,1,1),_AgentFeatureKeyingEnableKey_Type())
agentFeatureKeyingEnableKey.setMaxAccess(_C)
if mibBuilder.loadTexts:agentFeatureKeyingEnableKey.setStatus(_A)
_AgentFeatureKeyingDisableKey_Type=DisplayString
_AgentFeatureKeyingDisableKey_Object=MibScalar
agentFeatureKeyingDisableKey=_AgentFeatureKeyingDisableKey_Object((1,3,6,1,4,1,4526,10,24,1,2),_AgentFeatureKeyingDisableKey_Type())
agentFeatureKeyingDisableKey.setMaxAccess(_C)
if mibBuilder.loadTexts:agentFeatureKeyingDisableKey.setStatus(_A)
_AgentFeatureKeyingTable_Object=MibTable
agentFeatureKeyingTable=_AgentFeatureKeyingTable_Object((1,3,6,1,4,1,4526,10,24,1,3))
if mibBuilder.loadTexts:agentFeatureKeyingTable.setStatus(_A)
_AgentFeatureKeyingEntry_Object=MibTableRow
agentFeatureKeyingEntry=_AgentFeatureKeyingEntry_Object((1,3,6,1,4,1,4526,10,24,1,3,1))
agentFeatureKeyingEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:agentFeatureKeyingEntry.setStatus(_A)
_AgentFeatureKeyingIndex_Type=Unsigned32
_AgentFeatureKeyingIndex_Object=MibTableColumn
agentFeatureKeyingIndex=_AgentFeatureKeyingIndex_Object((1,3,6,1,4,1,4526,10,24,1,3,1,1),_AgentFeatureKeyingIndex_Type())
agentFeatureKeyingIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:agentFeatureKeyingIndex.setStatus(_A)
_AgentFeatureKeyingName_Type=DisplayString
_AgentFeatureKeyingName_Object=MibTableColumn
agentFeatureKeyingName=_AgentFeatureKeyingName_Object((1,3,6,1,4,1,4526,10,24,1,3,1,2),_AgentFeatureKeyingName_Type())
agentFeatureKeyingName.setMaxAccess(_F)
if mibBuilder.loadTexts:agentFeatureKeyingName.setStatus(_A)
class _AgentFeatureKeyingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AgentFeatureKeyingStatus_Type.__name__=_B
_AgentFeatureKeyingStatus_Object=MibTableColumn
agentFeatureKeyingStatus=_AgentFeatureKeyingStatus_Object((1,3,6,1,4,1,4526,10,24,1,3,1,3),_AgentFeatureKeyingStatus_Type())
agentFeatureKeyingStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:agentFeatureKeyingStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fastPathKeyingPrivate':fastPathKeyingPrivate,'agentFeatureKeyingGroup':agentFeatureKeyingGroup,'agentFeatureKeyingEnableKey':agentFeatureKeyingEnableKey,'agentFeatureKeyingDisableKey':agentFeatureKeyingDisableKey,'agentFeatureKeyingTable':agentFeatureKeyingTable,'agentFeatureKeyingEntry':agentFeatureKeyingEntry,_E:agentFeatureKeyingIndex,'agentFeatureKeyingName':agentFeatureKeyingName,'agentFeatureKeyingStatus':agentFeatureKeyingStatus})