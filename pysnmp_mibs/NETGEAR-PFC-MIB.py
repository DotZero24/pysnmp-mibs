_N='unwilling'
_M='willing'
_L='read-write'
_K='not-accessible'
_J='Unsigned32'
_I='agentPfcPriority'
_H='nodrop'
_G='drop'
_F='agentPfcIntfIndex'
_E='absent'
_D='NETGEAR-PFC-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ng7000managedswitch,=mibBuilder.importSymbols('NETGEAR-REF-MIB','ng7000managedswitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fastPathPFC=ModuleIdentity((1,3,6,1,4,1,4526,10,47))
if mibBuilder.loadTexts:fastPathPFC.setRevisions(('2011-01-26 00:00','2009-05-22 00:00'))
_AgentPfcCfgGroup_ObjectIdentity=ObjectIdentity
agentPfcCfgGroup=_AgentPfcCfgGroup_ObjectIdentity((1,3,6,1,4,1,4526,10,47,1))
_AgentPfcTable_Object=MibTable
agentPfcTable=_AgentPfcTable_Object((1,3,6,1,4,1,4526,10,47,1,1))
if mibBuilder.loadTexts:agentPfcTable.setStatus(_A)
_AgentPfcEntry_Object=MibTableRow
agentPfcEntry=_AgentPfcEntry_Object((1,3,6,1,4,1,4526,10,47,1,1,1))
agentPfcEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:agentPfcEntry.setStatus(_A)
_AgentPfcIntfIndex_Type=InterfaceIndex
_AgentPfcIntfIndex_Object=MibTableColumn
agentPfcIntfIndex=_AgentPfcIntfIndex_Object((1,3,6,1,4,1,4526,10,47,1,1,1,1),_AgentPfcIntfIndex_Type())
agentPfcIntfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:agentPfcIntfIndex.setStatus(_A)
class _AgentPfcIntfAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AgentPfcIntfAdminMode_Type.__name__=_C
_AgentPfcIntfAdminMode_Object=MibTableColumn
agentPfcIntfAdminMode=_AgentPfcIntfAdminMode_Object((1,3,6,1,4,1,4526,10,47,1,1,1,2),_AgentPfcIntfAdminMode_Type())
agentPfcIntfAdminMode.setMaxAccess(_L)
if mibBuilder.loadTexts:agentPfcIntfAdminMode.setStatus(_A)
class _AgentPfcIntfPfcStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_AgentPfcIntfPfcStatus_Type.__name__=_C
_AgentPfcIntfPfcStatus_Object=MibTableColumn
agentPfcIntfPfcStatus=_AgentPfcIntfPfcStatus_Object((1,3,6,1,4,1,4526,10,47,1,1,1,3),_AgentPfcIntfPfcStatus_Type())
agentPfcIntfPfcStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPfcIntfPfcStatus.setStatus(_A)
_AgentPfcTotalIntfPfcFramesRx_Type=Unsigned32
_AgentPfcTotalIntfPfcFramesRx_Object=MibTableColumn
agentPfcTotalIntfPfcFramesRx=_AgentPfcTotalIntfPfcFramesRx_Object((1,3,6,1,4,1,4526,10,47,1,1,1,4),_AgentPfcTotalIntfPfcFramesRx_Type())
agentPfcTotalIntfPfcFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPfcTotalIntfPfcFramesRx.setStatus(_A)
_AgentPfcTotalIntfPfcFramesTx_Type=Unsigned32
_AgentPfcTotalIntfPfcFramesTx_Object=MibTableColumn
agentPfcTotalIntfPfcFramesTx=_AgentPfcTotalIntfPfcFramesTx_Object((1,3,6,1,4,1,4526,10,47,1,1,1,5),_AgentPfcTotalIntfPfcFramesTx_Type())
agentPfcTotalIntfPfcFramesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPfcTotalIntfPfcFramesTx.setStatus(_A)
_AgentPfcIntfLinkDelayAllowance_Type=Unsigned32
_AgentPfcIntfLinkDelayAllowance_Object=MibTableColumn
agentPfcIntfLinkDelayAllowance=_AgentPfcIntfLinkDelayAllowance_Object((1,3,6,1,4,1,4526,10,47,1,1,1,6),_AgentPfcIntfLinkDelayAllowance_Type())
agentPfcIntfLinkDelayAllowance.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPfcIntfLinkDelayAllowance.setStatus(_A)
class _AgentPfcIntfAdvWilling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_AgentPfcIntfAdvWilling_Type.__name__=_C
_AgentPfcIntfAdvWilling_Object=MibTableColumn
agentPfcIntfAdvWilling=_AgentPfcIntfAdvWilling_Object((1,3,6,1,4,1,4526,10,47,1,1,1,7),_AgentPfcIntfAdvWilling_Type())
agentPfcIntfAdvWilling.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPfcIntfAdvWilling.setStatus(_A)
class _AgentPfcIntfPeerDetected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('detected',1),(_E,2)))
_AgentPfcIntfPeerDetected_Type.__name__=_C
_AgentPfcIntfPeerDetected_Object=MibTableColumn
agentPfcIntfPeerDetected=_AgentPfcIntfPeerDetected_Object((1,3,6,1,4,1,4526,10,47,1,1,1,8),_AgentPfcIntfPeerDetected_Type())
agentPfcIntfPeerDetected.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPfcIntfPeerDetected.setStatus(_A)
_AgentPfcIntfPeerMacAddr_Type=MacAddress
_AgentPfcIntfPeerMacAddr_Object=MibTableColumn
agentPfcIntfPeerMacAddr=_AgentPfcIntfPeerMacAddr_Object((1,3,6,1,4,1,4526,10,47,1,1,1,9),_AgentPfcIntfPeerMacAddr_Type())
agentPfcIntfPeerMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPfcIntfPeerMacAddr.setStatus(_A)
class _AgentPfcIntfPeerWilling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_M,2),(_N,3)))
_AgentPfcIntfPeerWilling_Type.__name__=_C
_AgentPfcIntfPeerWilling_Object=MibTableColumn
agentPfcIntfPeerWilling=_AgentPfcIntfPeerWilling_Object((1,3,6,1,4,1,4526,10,47,1,1,1,10),_AgentPfcIntfPeerWilling_Type())
agentPfcIntfPeerWilling.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPfcIntfPeerWilling.setStatus(_A)
class _AgentPfcIntfPeerMBCStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('true',2),('false',3)))
_AgentPfcIntfPeerMBCStatus_Type.__name__=_C
_AgentPfcIntfPeerMBCStatus_Object=MibTableColumn
agentPfcIntfPeerMBCStatus=_AgentPfcIntfPeerMBCStatus_Object((1,3,6,1,4,1,4526,10,47,1,1,1,11),_AgentPfcIntfPeerMBCStatus_Type())
agentPfcIntfPeerMBCStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPfcIntfPeerMBCStatus.setStatus(_A)
_AgentPfcIntfPeerCapability_Type=Unsigned32
_AgentPfcIntfPeerCapability_Object=MibTableColumn
agentPfcIntfPeerCapability=_AgentPfcIntfPeerCapability_Object((1,3,6,1,4,1,4526,10,47,1,1,1,12),_AgentPfcIntfPeerCapability_Type())
agentPfcIntfPeerCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPfcIntfPeerCapability.setStatus(_A)
class _AgentPfcIntfPeerCfgCompatible_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('true',2),('false',3)))
_AgentPfcIntfPeerCfgCompatible_Type.__name__=_C
_AgentPfcIntfPeerCfgCompatible_Object=MibTableColumn
agentPfcIntfPeerCfgCompatible=_AgentPfcIntfPeerCfgCompatible_Object((1,3,6,1,4,1,4526,10,47,1,1,1,13),_AgentPfcIntfPeerCfgCompatible_Type())
agentPfcIntfPeerCfgCompatible.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPfcIntfPeerCfgCompatible.setStatus(_A)
_AgentPfcIntfPeerCompatibleCfgCount_Type=Unsigned32
_AgentPfcIntfPeerCompatibleCfgCount_Object=MibTableColumn
agentPfcIntfPeerCompatibleCfgCount=_AgentPfcIntfPeerCompatibleCfgCount_Object((1,3,6,1,4,1,4526,10,47,1,1,1,14),_AgentPfcIntfPeerCompatibleCfgCount_Type())
agentPfcIntfPeerCompatibleCfgCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPfcIntfPeerCompatibleCfgCount.setStatus(_A)
_AgentPfcIntfPeerIncompatibleCfgCount_Type=Unsigned32
_AgentPfcIntfPeerIncompatibleCfgCount_Object=MibTableColumn
agentPfcIntfPeerIncompatibleCfgCount=_AgentPfcIntfPeerIncompatibleCfgCount_Object((1,3,6,1,4,1,4526,10,47,1,1,1,15),_AgentPfcIntfPeerIncompatibleCfgCount_Type())
agentPfcIntfPeerIncompatibleCfgCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPfcIntfPeerIncompatibleCfgCount.setStatus(_A)
_AgentPfcActionTable_Object=MibTable
agentPfcActionTable=_AgentPfcActionTable_Object((1,3,6,1,4,1,4526,10,47,1,2))
if mibBuilder.loadTexts:agentPfcActionTable.setStatus(_A)
_AgentPfcActionEntry_Object=MibTableRow
agentPfcActionEntry=_AgentPfcActionEntry_Object((1,3,6,1,4,1,4526,10,47,1,2,1))
agentPfcActionEntry.setIndexNames((0,_D,_F),(0,_D,_I))
if mibBuilder.loadTexts:agentPfcActionEntry.setStatus(_A)
class _AgentPfcPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AgentPfcPriority_Type.__name__=_J
_AgentPfcPriority_Object=MibTableColumn
agentPfcPriority=_AgentPfcPriority_Object((1,3,6,1,4,1,4526,10,47,1,2,1,1),_AgentPfcPriority_Type())
agentPfcPriority.setMaxAccess(_K)
if mibBuilder.loadTexts:agentPfcPriority.setStatus(_A)
class _AgentPfcAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentPfcAction_Type.__name__=_C
_AgentPfcAction_Object=MibTableColumn
agentPfcAction=_AgentPfcAction_Object((1,3,6,1,4,1,4526,10,47,1,2,1,2),_AgentPfcAction_Type())
agentPfcAction.setMaxAccess(_L)
if mibBuilder.loadTexts:agentPfcAction.setStatus(_A)
class _AgentPfcOperAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentPfcOperAction_Type.__name__=_C
_AgentPfcOperAction_Object=MibTableColumn
agentPfcOperAction=_AgentPfcOperAction_Object((1,3,6,1,4,1,4526,10,47,1,2,1,3),_AgentPfcOperAction_Type())
agentPfcOperAction.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPfcOperAction.setStatus(_A)
class _AgentPfcAdvAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentPfcAdvAction_Type.__name__=_C
_AgentPfcAdvAction_Object=MibTableColumn
agentPfcAdvAction=_AgentPfcAdvAction_Object((1,3,6,1,4,1,4526,10,47,1,2,1,4),_AgentPfcAdvAction_Type())
agentPfcAdvAction.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPfcAdvAction.setStatus(_A)
class _AgentPfcPeerAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_AgentPfcPeerAction_Type.__name__=_C
_AgentPfcPeerAction_Object=MibTableColumn
agentPfcPeerAction=_AgentPfcPeerAction_Object((1,3,6,1,4,1,4526,10,47,1,2,1,5),_AgentPfcPeerAction_Type())
agentPfcPeerAction.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPfcPeerAction.setStatus(_A)
_AgentPfcIntfStatsPerPriorityTable_Object=MibTable
agentPfcIntfStatsPerPriorityTable=_AgentPfcIntfStatsPerPriorityTable_Object((1,3,6,1,4,1,4526,10,47,1,3))
if mibBuilder.loadTexts:agentPfcIntfStatsPerPriorityTable.setStatus(_A)
_AgentPfcIntfStatsPerPriorityEntry_Object=MibTableRow
agentPfcIntfStatsPerPriorityEntry=_AgentPfcIntfStatsPerPriorityEntry_Object((1,3,6,1,4,1,4526,10,47,1,3,1))
agentPfcIntfStatsPerPriorityEntry.setIndexNames((0,_D,_F),(0,_D,_I))
if mibBuilder.loadTexts:agentPfcIntfStatsPerPriorityEntry.setStatus(_A)
_AgentPfcIntfPfcPriorityFramesRx_Type=Unsigned32
_AgentPfcIntfPfcPriorityFramesRx_Object=MibTableColumn
agentPfcIntfPfcPriorityFramesRx=_AgentPfcIntfPfcPriorityFramesRx_Object((1,3,6,1,4,1,4526,10,47,1,3,1,1),_AgentPfcIntfPfcPriorityFramesRx_Type())
agentPfcIntfPfcPriorityFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPfcIntfPfcPriorityFramesRx.setStatus(_A)
_AgentPfcIntfPfcPriorityFramesTx_Type=Unsigned32
_AgentPfcIntfPfcPriorityFramesTx_Object=MibTableColumn
agentPfcIntfPfcPriorityFramesTx=_AgentPfcIntfPfcPriorityFramesTx_Object((1,3,6,1,4,1,4526,10,47,1,3,1,2),_AgentPfcIntfPfcPriorityFramesTx_Type())
agentPfcIntfPfcPriorityFramesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPfcIntfPfcPriorityFramesTx.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fastPathPFC':fastPathPFC,'agentPfcCfgGroup':agentPfcCfgGroup,'agentPfcTable':agentPfcTable,'agentPfcEntry':agentPfcEntry,_F:agentPfcIntfIndex,'agentPfcIntfAdminMode':agentPfcIntfAdminMode,'agentPfcIntfPfcStatus':agentPfcIntfPfcStatus,'agentPfcTotalIntfPfcFramesRx':agentPfcTotalIntfPfcFramesRx,'agentPfcTotalIntfPfcFramesTx':agentPfcTotalIntfPfcFramesTx,'agentPfcIntfLinkDelayAllowance':agentPfcIntfLinkDelayAllowance,'agentPfcIntfAdvWilling':agentPfcIntfAdvWilling,'agentPfcIntfPeerDetected':agentPfcIntfPeerDetected,'agentPfcIntfPeerMacAddr':agentPfcIntfPeerMacAddr,'agentPfcIntfPeerWilling':agentPfcIntfPeerWilling,'agentPfcIntfPeerMBCStatus':agentPfcIntfPeerMBCStatus,'agentPfcIntfPeerCapability':agentPfcIntfPeerCapability,'agentPfcIntfPeerCfgCompatible':agentPfcIntfPeerCfgCompatible,'agentPfcIntfPeerCompatibleCfgCount':agentPfcIntfPeerCompatibleCfgCount,'agentPfcIntfPeerIncompatibleCfgCount':agentPfcIntfPeerIncompatibleCfgCount,'agentPfcActionTable':agentPfcActionTable,'agentPfcActionEntry':agentPfcActionEntry,_I:agentPfcPriority,'agentPfcAction':agentPfcAction,'agentPfcOperAction':agentPfcOperAction,'agentPfcAdvAction':agentPfcAdvAction,'agentPfcPeerAction':agentPfcPeerAction,'agentPfcIntfStatsPerPriorityTable':agentPfcIntfStatsPerPriorityTable,'agentPfcIntfStatsPerPriorityEntry':agentPfcIntfStatsPerPriorityEntry,'agentPfcIntfPfcPriorityFramesRx':agentPfcIntfPfcPriorityFramesRx,'agentPfcIntfPfcPriorityFramesTx':agentPfcIntfPfcPriorityFramesTx})