_AJ='dot3adAggPortDebugGroup'
_AI='dot3adAggPortStatsGroup'
_AH='dot3adAggPortListGroup'
_AG='dot3adTablesLastChangedGroup'
_AF='dot3adAggPortGroup'
_AE='dot3adAggGroup'
_AD='dot3adTablesLastChanged'
_AC='dot3adAggPortDebugPartnerChangeCount'
_AB='dot3adAggPortDebugActorChangeCount'
_AA='dot3adAggPortDebugPartnerSyncTransitionCount'
_A9='dot3adAggPortDebugActorSyncTransitionCount'
_A8='dot3adAggPortDebugPartnerChurnCount'
_A7='dot3adAggPortDebugActorChurnCount'
_A6='dot3adAggPortDebugPartnerChurnState'
_A5='dot3adAggPortDebugActorChurnState'
_A4='dot3adAggPortDebugMuxReason'
_A3='dot3adAggPortDebugMuxState'
_A2='dot3adAggPortDebugLastRxTime'
_A1='dot3adAggPortDebugRxState'
_A0='dot3adAggPortStatsMarkerResponsePDUsTx'
_z='dot3adAggPortStatsMarkerPDUsTx'
_y='dot3adAggPortStatsLACPDUsTx'
_x='dot3adAggPortStatsIllegalRx'
_w='dot3adAggPortStatsUnknownRx'
_v='dot3adAggPortStatsMarkerResponsePDUsRx'
_u='dot3adAggPortStatsMarkerPDUsRx'
_t='dot3adAggPortStatsLACPDUsRx'
_s='dot3adAggPortAggregateOrIndividual'
_r='dot3adAggPortPartnerOperState'
_q='dot3adAggPortPartnerAdminState'
_p='dot3adAggPortActorOperState'
_o='dot3adAggPortActorAdminState'
_n='dot3adAggPortPartnerOperPortPriority'
_m='dot3adAggPortPartnerAdminPortPriority'
_l='dot3adAggPortPartnerOperPort'
_k='dot3adAggPortPartnerAdminPort'
_j='dot3adAggPortActorPortPriority'
_i='dot3adAggPortActorPort'
_h='dot3adAggPortAttachedAggID'
_g='dot3adAggPortSelectedAggID'
_f='dot3adAggPortPartnerOperKey'
_e='dot3adAggPortPartnerAdminKey'
_d='dot3adAggPortPartnerOperSystemID'
_c='dot3adAggPortPartnerAdminSystemID'
_b='dot3adAggPortPartnerOperSystemPriority'
_a='dot3adAggPortPartnerAdminSystemPriority'
_Z='dot3adAggPortActorOperKey'
_Y='dot3adAggPortActorAdminKey'
_X='dot3adAggPortActorSystemID'
_W='dot3adAggPortActorSystemPriority'
_V='dot3adAggPortListPorts'
_U='dot3adAggCollectorMaxDelay'
_T='dot3adAggPartnerOperKey'
_S='dot3adAggPartnerSystemPriority'
_R='dot3adAggPartnerSystemID'
_Q='dot3adAggActorOperKey'
_P='dot3adAggMACAddress'
_O='dot3adAggActorAdminKey'
_N='dot3adAggAggregateOrIndividual'
_M='dot3adAggActorSystemPriority'
_L='dot3adAggActorSystemID'
_K='expired'
_J='defaulted'
_I='distributing'
_H='collecting'
_G='dot3adAggIndex'
_F='dot3adAggPortIndex'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='LAG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
lagMIB=ModuleIdentity((1,2,840,10006,300,43))
if mibBuilder.loadTexts:lagMIB.setRevisions(('2003-06-18 01:00',))
class LacpKey(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class LacpState(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('lacpActivity',0),('lacpTimeout',1),('aggregation',2),('synchronisation',3),(_H,4),(_I,5),(_J,6),(_K,7)))
class ChurnState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noChurn',1),('churn',2),('churnMonitor',3)))
_LagMIBObjects_ObjectIdentity=ObjectIdentity
lagMIBObjects=_LagMIBObjects_ObjectIdentity((1,2,840,10006,300,43,1))
_Dot3adAgg_ObjectIdentity=ObjectIdentity
dot3adAgg=_Dot3adAgg_ObjectIdentity((1,2,840,10006,300,43,1,1))
_Dot3adAggTable_Object=MibTable
dot3adAggTable=_Dot3adAggTable_Object((1,2,840,10006,300,43,1,1,1))
if mibBuilder.loadTexts:dot3adAggTable.setStatus(_A)
_Dot3adAggEntry_Object=MibTableRow
dot3adAggEntry=_Dot3adAggEntry_Object((1,2,840,10006,300,43,1,1,1,1))
dot3adAggEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:dot3adAggEntry.setStatus(_A)
_Dot3adAggIndex_Type=InterfaceIndex
_Dot3adAggIndex_Object=MibTableColumn
dot3adAggIndex=_Dot3adAggIndex_Object((1,2,840,10006,300,43,1,1,1,1,1),_Dot3adAggIndex_Type())
dot3adAggIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggIndex.setStatus(_A)
_Dot3adAggMACAddress_Type=MacAddress
_Dot3adAggMACAddress_Object=MibTableColumn
dot3adAggMACAddress=_Dot3adAggMACAddress_Object((1,2,840,10006,300,43,1,1,1,1,2),_Dot3adAggMACAddress_Type())
dot3adAggMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggMACAddress.setStatus(_A)
class _Dot3adAggActorSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot3adAggActorSystemPriority_Type.__name__=_D
_Dot3adAggActorSystemPriority_Object=MibTableColumn
dot3adAggActorSystemPriority=_Dot3adAggActorSystemPriority_Object((1,2,840,10006,300,43,1,1,1,1,3),_Dot3adAggActorSystemPriority_Type())
dot3adAggActorSystemPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3adAggActorSystemPriority.setStatus(_A)
_Dot3adAggActorSystemID_Type=MacAddress
_Dot3adAggActorSystemID_Object=MibTableColumn
dot3adAggActorSystemID=_Dot3adAggActorSystemID_Object((1,2,840,10006,300,43,1,1,1,1,4),_Dot3adAggActorSystemID_Type())
dot3adAggActorSystemID.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggActorSystemID.setStatus(_A)
_Dot3adAggAggregateOrIndividual_Type=TruthValue
_Dot3adAggAggregateOrIndividual_Object=MibTableColumn
dot3adAggAggregateOrIndividual=_Dot3adAggAggregateOrIndividual_Object((1,2,840,10006,300,43,1,1,1,1,5),_Dot3adAggAggregateOrIndividual_Type())
dot3adAggAggregateOrIndividual.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggAggregateOrIndividual.setStatus(_A)
_Dot3adAggActorAdminKey_Type=LacpKey
_Dot3adAggActorAdminKey_Object=MibTableColumn
dot3adAggActorAdminKey=_Dot3adAggActorAdminKey_Object((1,2,840,10006,300,43,1,1,1,1,6),_Dot3adAggActorAdminKey_Type())
dot3adAggActorAdminKey.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3adAggActorAdminKey.setStatus(_A)
_Dot3adAggActorOperKey_Type=LacpKey
_Dot3adAggActorOperKey_Object=MibTableColumn
dot3adAggActorOperKey=_Dot3adAggActorOperKey_Object((1,2,840,10006,300,43,1,1,1,1,7),_Dot3adAggActorOperKey_Type())
dot3adAggActorOperKey.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggActorOperKey.setStatus(_A)
_Dot3adAggPartnerSystemID_Type=MacAddress
_Dot3adAggPartnerSystemID_Object=MibTableColumn
dot3adAggPartnerSystemID=_Dot3adAggPartnerSystemID_Object((1,2,840,10006,300,43,1,1,1,1,8),_Dot3adAggPartnerSystemID_Type())
dot3adAggPartnerSystemID.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPartnerSystemID.setStatus(_A)
class _Dot3adAggPartnerSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot3adAggPartnerSystemPriority_Type.__name__=_D
_Dot3adAggPartnerSystemPriority_Object=MibTableColumn
dot3adAggPartnerSystemPriority=_Dot3adAggPartnerSystemPriority_Object((1,2,840,10006,300,43,1,1,1,1,9),_Dot3adAggPartnerSystemPriority_Type())
dot3adAggPartnerSystemPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPartnerSystemPriority.setStatus(_A)
_Dot3adAggPartnerOperKey_Type=LacpKey
_Dot3adAggPartnerOperKey_Object=MibTableColumn
dot3adAggPartnerOperKey=_Dot3adAggPartnerOperKey_Object((1,2,840,10006,300,43,1,1,1,1,10),_Dot3adAggPartnerOperKey_Type())
dot3adAggPartnerOperKey.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPartnerOperKey.setStatus(_A)
class _Dot3adAggCollectorMaxDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot3adAggCollectorMaxDelay_Type.__name__=_D
_Dot3adAggCollectorMaxDelay_Object=MibTableColumn
dot3adAggCollectorMaxDelay=_Dot3adAggCollectorMaxDelay_Object((1,2,840,10006,300,43,1,1,1,1,11),_Dot3adAggCollectorMaxDelay_Type())
dot3adAggCollectorMaxDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3adAggCollectorMaxDelay.setStatus(_A)
_Dot3adAggPortListTable_Object=MibTable
dot3adAggPortListTable=_Dot3adAggPortListTable_Object((1,2,840,10006,300,43,1,1,2))
if mibBuilder.loadTexts:dot3adAggPortListTable.setStatus(_A)
_Dot3adAggPortListEntry_Object=MibTableRow
dot3adAggPortListEntry=_Dot3adAggPortListEntry_Object((1,2,840,10006,300,43,1,1,2,1))
dot3adAggPortListEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:dot3adAggPortListEntry.setStatus(_A)
_Dot3adAggPortListPorts_Type=PortList
_Dot3adAggPortListPorts_Object=MibTableColumn
dot3adAggPortListPorts=_Dot3adAggPortListPorts_Object((1,2,840,10006,300,43,1,1,2,1,1),_Dot3adAggPortListPorts_Type())
dot3adAggPortListPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortListPorts.setStatus(_A)
_Dot3adAggPort_ObjectIdentity=ObjectIdentity
dot3adAggPort=_Dot3adAggPort_ObjectIdentity((1,2,840,10006,300,43,1,2))
_Dot3adAggPortTable_Object=MibTable
dot3adAggPortTable=_Dot3adAggPortTable_Object((1,2,840,10006,300,43,1,2,1))
if mibBuilder.loadTexts:dot3adAggPortTable.setStatus(_A)
_Dot3adAggPortEntry_Object=MibTableRow
dot3adAggPortEntry=_Dot3adAggPortEntry_Object((1,2,840,10006,300,43,1,2,1,1))
dot3adAggPortEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:dot3adAggPortEntry.setStatus(_A)
_Dot3adAggPortIndex_Type=InterfaceIndex
_Dot3adAggPortIndex_Object=MibTableColumn
dot3adAggPortIndex=_Dot3adAggPortIndex_Object((1,2,840,10006,300,43,1,2,1,1,1),_Dot3adAggPortIndex_Type())
dot3adAggPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortIndex.setStatus(_A)
class _Dot3adAggPortActorSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot3adAggPortActorSystemPriority_Type.__name__=_D
_Dot3adAggPortActorSystemPriority_Object=MibTableColumn
dot3adAggPortActorSystemPriority=_Dot3adAggPortActorSystemPriority_Object((1,2,840,10006,300,43,1,2,1,1,2),_Dot3adAggPortActorSystemPriority_Type())
dot3adAggPortActorSystemPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3adAggPortActorSystemPriority.setStatus(_A)
_Dot3adAggPortActorSystemID_Type=MacAddress
_Dot3adAggPortActorSystemID_Object=MibTableColumn
dot3adAggPortActorSystemID=_Dot3adAggPortActorSystemID_Object((1,2,840,10006,300,43,1,2,1,1,3),_Dot3adAggPortActorSystemID_Type())
dot3adAggPortActorSystemID.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortActorSystemID.setStatus(_A)
_Dot3adAggPortActorAdminKey_Type=LacpKey
_Dot3adAggPortActorAdminKey_Object=MibTableColumn
dot3adAggPortActorAdminKey=_Dot3adAggPortActorAdminKey_Object((1,2,840,10006,300,43,1,2,1,1,4),_Dot3adAggPortActorAdminKey_Type())
dot3adAggPortActorAdminKey.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3adAggPortActorAdminKey.setStatus(_A)
_Dot3adAggPortActorOperKey_Type=LacpKey
_Dot3adAggPortActorOperKey_Object=MibTableColumn
dot3adAggPortActorOperKey=_Dot3adAggPortActorOperKey_Object((1,2,840,10006,300,43,1,2,1,1,5),_Dot3adAggPortActorOperKey_Type())
dot3adAggPortActorOperKey.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortActorOperKey.setStatus(_A)
class _Dot3adAggPortPartnerAdminSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot3adAggPortPartnerAdminSystemPriority_Type.__name__=_D
_Dot3adAggPortPartnerAdminSystemPriority_Object=MibTableColumn
dot3adAggPortPartnerAdminSystemPriority=_Dot3adAggPortPartnerAdminSystemPriority_Object((1,2,840,10006,300,43,1,2,1,1,6),_Dot3adAggPortPartnerAdminSystemPriority_Type())
dot3adAggPortPartnerAdminSystemPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3adAggPortPartnerAdminSystemPriority.setStatus(_A)
class _Dot3adAggPortPartnerOperSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot3adAggPortPartnerOperSystemPriority_Type.__name__=_D
_Dot3adAggPortPartnerOperSystemPriority_Object=MibTableColumn
dot3adAggPortPartnerOperSystemPriority=_Dot3adAggPortPartnerOperSystemPriority_Object((1,2,840,10006,300,43,1,2,1,1,7),_Dot3adAggPortPartnerOperSystemPriority_Type())
dot3adAggPortPartnerOperSystemPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortPartnerOperSystemPriority.setStatus(_A)
_Dot3adAggPortPartnerAdminSystemID_Type=MacAddress
_Dot3adAggPortPartnerAdminSystemID_Object=MibTableColumn
dot3adAggPortPartnerAdminSystemID=_Dot3adAggPortPartnerAdminSystemID_Object((1,2,840,10006,300,43,1,2,1,1,8),_Dot3adAggPortPartnerAdminSystemID_Type())
dot3adAggPortPartnerAdminSystemID.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3adAggPortPartnerAdminSystemID.setStatus(_A)
_Dot3adAggPortPartnerOperSystemID_Type=MacAddress
_Dot3adAggPortPartnerOperSystemID_Object=MibTableColumn
dot3adAggPortPartnerOperSystemID=_Dot3adAggPortPartnerOperSystemID_Object((1,2,840,10006,300,43,1,2,1,1,9),_Dot3adAggPortPartnerOperSystemID_Type())
dot3adAggPortPartnerOperSystemID.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortPartnerOperSystemID.setStatus(_A)
_Dot3adAggPortPartnerAdminKey_Type=LacpKey
_Dot3adAggPortPartnerAdminKey_Object=MibTableColumn
dot3adAggPortPartnerAdminKey=_Dot3adAggPortPartnerAdminKey_Object((1,2,840,10006,300,43,1,2,1,1,10),_Dot3adAggPortPartnerAdminKey_Type())
dot3adAggPortPartnerAdminKey.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3adAggPortPartnerAdminKey.setStatus(_A)
_Dot3adAggPortPartnerOperKey_Type=LacpKey
_Dot3adAggPortPartnerOperKey_Object=MibTableColumn
dot3adAggPortPartnerOperKey=_Dot3adAggPortPartnerOperKey_Object((1,2,840,10006,300,43,1,2,1,1,11),_Dot3adAggPortPartnerOperKey_Type())
dot3adAggPortPartnerOperKey.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortPartnerOperKey.setStatus(_A)
_Dot3adAggPortSelectedAggID_Type=InterfaceIndex
_Dot3adAggPortSelectedAggID_Object=MibTableColumn
dot3adAggPortSelectedAggID=_Dot3adAggPortSelectedAggID_Object((1,2,840,10006,300,43,1,2,1,1,12),_Dot3adAggPortSelectedAggID_Type())
dot3adAggPortSelectedAggID.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortSelectedAggID.setStatus(_A)
_Dot3adAggPortAttachedAggID_Type=InterfaceIndex
_Dot3adAggPortAttachedAggID_Object=MibTableColumn
dot3adAggPortAttachedAggID=_Dot3adAggPortAttachedAggID_Object((1,2,840,10006,300,43,1,2,1,1,13),_Dot3adAggPortAttachedAggID_Type())
dot3adAggPortAttachedAggID.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortAttachedAggID.setStatus(_A)
class _Dot3adAggPortActorPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot3adAggPortActorPort_Type.__name__=_D
_Dot3adAggPortActorPort_Object=MibTableColumn
dot3adAggPortActorPort=_Dot3adAggPortActorPort_Object((1,2,840,10006,300,43,1,2,1,1,14),_Dot3adAggPortActorPort_Type())
dot3adAggPortActorPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortActorPort.setStatus(_A)
class _Dot3adAggPortActorPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot3adAggPortActorPortPriority_Type.__name__=_D
_Dot3adAggPortActorPortPriority_Object=MibTableColumn
dot3adAggPortActorPortPriority=_Dot3adAggPortActorPortPriority_Object((1,2,840,10006,300,43,1,2,1,1,15),_Dot3adAggPortActorPortPriority_Type())
dot3adAggPortActorPortPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3adAggPortActorPortPriority.setStatus(_A)
class _Dot3adAggPortPartnerAdminPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot3adAggPortPartnerAdminPort_Type.__name__=_D
_Dot3adAggPortPartnerAdminPort_Object=MibTableColumn
dot3adAggPortPartnerAdminPort=_Dot3adAggPortPartnerAdminPort_Object((1,2,840,10006,300,43,1,2,1,1,16),_Dot3adAggPortPartnerAdminPort_Type())
dot3adAggPortPartnerAdminPort.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3adAggPortPartnerAdminPort.setStatus(_A)
class _Dot3adAggPortPartnerOperPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot3adAggPortPartnerOperPort_Type.__name__=_D
_Dot3adAggPortPartnerOperPort_Object=MibTableColumn
dot3adAggPortPartnerOperPort=_Dot3adAggPortPartnerOperPort_Object((1,2,840,10006,300,43,1,2,1,1,17),_Dot3adAggPortPartnerOperPort_Type())
dot3adAggPortPartnerOperPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortPartnerOperPort.setStatus(_A)
class _Dot3adAggPortPartnerAdminPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot3adAggPortPartnerAdminPortPriority_Type.__name__=_D
_Dot3adAggPortPartnerAdminPortPriority_Object=MibTableColumn
dot3adAggPortPartnerAdminPortPriority=_Dot3adAggPortPartnerAdminPortPriority_Object((1,2,840,10006,300,43,1,2,1,1,18),_Dot3adAggPortPartnerAdminPortPriority_Type())
dot3adAggPortPartnerAdminPortPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3adAggPortPartnerAdminPortPriority.setStatus(_A)
class _Dot3adAggPortPartnerOperPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot3adAggPortPartnerOperPortPriority_Type.__name__=_D
_Dot3adAggPortPartnerOperPortPriority_Object=MibTableColumn
dot3adAggPortPartnerOperPortPriority=_Dot3adAggPortPartnerOperPortPriority_Object((1,2,840,10006,300,43,1,2,1,1,19),_Dot3adAggPortPartnerOperPortPriority_Type())
dot3adAggPortPartnerOperPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortPartnerOperPortPriority.setStatus(_A)
_Dot3adAggPortActorAdminState_Type=LacpState
_Dot3adAggPortActorAdminState_Object=MibTableColumn
dot3adAggPortActorAdminState=_Dot3adAggPortActorAdminState_Object((1,2,840,10006,300,43,1,2,1,1,20),_Dot3adAggPortActorAdminState_Type())
dot3adAggPortActorAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3adAggPortActorAdminState.setStatus(_A)
_Dot3adAggPortActorOperState_Type=LacpState
_Dot3adAggPortActorOperState_Object=MibTableColumn
dot3adAggPortActorOperState=_Dot3adAggPortActorOperState_Object((1,2,840,10006,300,43,1,2,1,1,21),_Dot3adAggPortActorOperState_Type())
dot3adAggPortActorOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortActorOperState.setStatus(_A)
_Dot3adAggPortPartnerAdminState_Type=LacpState
_Dot3adAggPortPartnerAdminState_Object=MibTableColumn
dot3adAggPortPartnerAdminState=_Dot3adAggPortPartnerAdminState_Object((1,2,840,10006,300,43,1,2,1,1,22),_Dot3adAggPortPartnerAdminState_Type())
dot3adAggPortPartnerAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3adAggPortPartnerAdminState.setStatus(_A)
_Dot3adAggPortPartnerOperState_Type=LacpState
_Dot3adAggPortPartnerOperState_Object=MibTableColumn
dot3adAggPortPartnerOperState=_Dot3adAggPortPartnerOperState_Object((1,2,840,10006,300,43,1,2,1,1,23),_Dot3adAggPortPartnerOperState_Type())
dot3adAggPortPartnerOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortPartnerOperState.setStatus(_A)
_Dot3adAggPortAggregateOrIndividual_Type=TruthValue
_Dot3adAggPortAggregateOrIndividual_Object=MibTableColumn
dot3adAggPortAggregateOrIndividual=_Dot3adAggPortAggregateOrIndividual_Object((1,2,840,10006,300,43,1,2,1,1,24),_Dot3adAggPortAggregateOrIndividual_Type())
dot3adAggPortAggregateOrIndividual.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortAggregateOrIndividual.setStatus(_A)
_Dot3adAggPortStatsTable_Object=MibTable
dot3adAggPortStatsTable=_Dot3adAggPortStatsTable_Object((1,2,840,10006,300,43,1,2,2))
if mibBuilder.loadTexts:dot3adAggPortStatsTable.setStatus(_A)
_Dot3adAggPortStatsEntry_Object=MibTableRow
dot3adAggPortStatsEntry=_Dot3adAggPortStatsEntry_Object((1,2,840,10006,300,43,1,2,2,1))
dot3adAggPortStatsEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:dot3adAggPortStatsEntry.setStatus(_A)
_Dot3adAggPortStatsLACPDUsRx_Type=Counter32
_Dot3adAggPortStatsLACPDUsRx_Object=MibTableColumn
dot3adAggPortStatsLACPDUsRx=_Dot3adAggPortStatsLACPDUsRx_Object((1,2,840,10006,300,43,1,2,2,1,1),_Dot3adAggPortStatsLACPDUsRx_Type())
dot3adAggPortStatsLACPDUsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortStatsLACPDUsRx.setStatus(_A)
_Dot3adAggPortStatsMarkerPDUsRx_Type=Counter32
_Dot3adAggPortStatsMarkerPDUsRx_Object=MibTableColumn
dot3adAggPortStatsMarkerPDUsRx=_Dot3adAggPortStatsMarkerPDUsRx_Object((1,2,840,10006,300,43,1,2,2,1,2),_Dot3adAggPortStatsMarkerPDUsRx_Type())
dot3adAggPortStatsMarkerPDUsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortStatsMarkerPDUsRx.setStatus(_A)
_Dot3adAggPortStatsMarkerResponsePDUsRx_Type=Counter32
_Dot3adAggPortStatsMarkerResponsePDUsRx_Object=MibTableColumn
dot3adAggPortStatsMarkerResponsePDUsRx=_Dot3adAggPortStatsMarkerResponsePDUsRx_Object((1,2,840,10006,300,43,1,2,2,1,3),_Dot3adAggPortStatsMarkerResponsePDUsRx_Type())
dot3adAggPortStatsMarkerResponsePDUsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortStatsMarkerResponsePDUsRx.setStatus(_A)
_Dot3adAggPortStatsUnknownRx_Type=Counter32
_Dot3adAggPortStatsUnknownRx_Object=MibTableColumn
dot3adAggPortStatsUnknownRx=_Dot3adAggPortStatsUnknownRx_Object((1,2,840,10006,300,43,1,2,2,1,4),_Dot3adAggPortStatsUnknownRx_Type())
dot3adAggPortStatsUnknownRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortStatsUnknownRx.setStatus(_A)
_Dot3adAggPortStatsIllegalRx_Type=Counter32
_Dot3adAggPortStatsIllegalRx_Object=MibTableColumn
dot3adAggPortStatsIllegalRx=_Dot3adAggPortStatsIllegalRx_Object((1,2,840,10006,300,43,1,2,2,1,5),_Dot3adAggPortStatsIllegalRx_Type())
dot3adAggPortStatsIllegalRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortStatsIllegalRx.setStatus(_A)
_Dot3adAggPortStatsLACPDUsTx_Type=Counter32
_Dot3adAggPortStatsLACPDUsTx_Object=MibTableColumn
dot3adAggPortStatsLACPDUsTx=_Dot3adAggPortStatsLACPDUsTx_Object((1,2,840,10006,300,43,1,2,2,1,6),_Dot3adAggPortStatsLACPDUsTx_Type())
dot3adAggPortStatsLACPDUsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortStatsLACPDUsTx.setStatus(_A)
_Dot3adAggPortStatsMarkerPDUsTx_Type=Counter32
_Dot3adAggPortStatsMarkerPDUsTx_Object=MibTableColumn
dot3adAggPortStatsMarkerPDUsTx=_Dot3adAggPortStatsMarkerPDUsTx_Object((1,2,840,10006,300,43,1,2,2,1,7),_Dot3adAggPortStatsMarkerPDUsTx_Type())
dot3adAggPortStatsMarkerPDUsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortStatsMarkerPDUsTx.setStatus(_A)
_Dot3adAggPortStatsMarkerResponsePDUsTx_Type=Counter32
_Dot3adAggPortStatsMarkerResponsePDUsTx_Object=MibTableColumn
dot3adAggPortStatsMarkerResponsePDUsTx=_Dot3adAggPortStatsMarkerResponsePDUsTx_Object((1,2,840,10006,300,43,1,2,2,1,8),_Dot3adAggPortStatsMarkerResponsePDUsTx_Type())
dot3adAggPortStatsMarkerResponsePDUsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortStatsMarkerResponsePDUsTx.setStatus(_A)
_Dot3adAggPortDebugTable_Object=MibTable
dot3adAggPortDebugTable=_Dot3adAggPortDebugTable_Object((1,2,840,10006,300,43,1,2,3))
if mibBuilder.loadTexts:dot3adAggPortDebugTable.setStatus(_A)
_Dot3adAggPortDebugEntry_Object=MibTableRow
dot3adAggPortDebugEntry=_Dot3adAggPortDebugEntry_Object((1,2,840,10006,300,43,1,2,3,1))
dot3adAggPortDebugEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:dot3adAggPortDebugEntry.setStatus(_A)
class _Dot3adAggPortDebugRxState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_A,1),(_K,2),(_J,3),('initialize',4),('lacpDisabled',5),('portDisabled',6)))
_Dot3adAggPortDebugRxState_Type.__name__=_D
_Dot3adAggPortDebugRxState_Object=MibTableColumn
dot3adAggPortDebugRxState=_Dot3adAggPortDebugRxState_Object((1,2,840,10006,300,43,1,2,3,1,1),_Dot3adAggPortDebugRxState_Type())
dot3adAggPortDebugRxState.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortDebugRxState.setStatus(_A)
_Dot3adAggPortDebugLastRxTime_Type=TimeTicks
_Dot3adAggPortDebugLastRxTime_Object=MibTableColumn
dot3adAggPortDebugLastRxTime=_Dot3adAggPortDebugLastRxTime_Object((1,2,840,10006,300,43,1,2,3,1,2),_Dot3adAggPortDebugLastRxTime_Type())
dot3adAggPortDebugLastRxTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortDebugLastRxTime.setStatus(_A)
class _Dot3adAggPortDebugMuxState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('detached',1),('waiting',2),('attached',3),(_H,4),(_I,5),('collectingDistributing',6)))
_Dot3adAggPortDebugMuxState_Type.__name__=_D
_Dot3adAggPortDebugMuxState_Object=MibTableColumn
dot3adAggPortDebugMuxState=_Dot3adAggPortDebugMuxState_Object((1,2,840,10006,300,43,1,2,3,1,3),_Dot3adAggPortDebugMuxState_Type())
dot3adAggPortDebugMuxState.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortDebugMuxState.setStatus(_A)
_Dot3adAggPortDebugMuxReason_Type=DisplayString
_Dot3adAggPortDebugMuxReason_Object=MibTableColumn
dot3adAggPortDebugMuxReason=_Dot3adAggPortDebugMuxReason_Object((1,2,840,10006,300,43,1,2,3,1,4),_Dot3adAggPortDebugMuxReason_Type())
dot3adAggPortDebugMuxReason.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortDebugMuxReason.setStatus(_A)
_Dot3adAggPortDebugActorChurnState_Type=ChurnState
_Dot3adAggPortDebugActorChurnState_Object=MibTableColumn
dot3adAggPortDebugActorChurnState=_Dot3adAggPortDebugActorChurnState_Object((1,2,840,10006,300,43,1,2,3,1,5),_Dot3adAggPortDebugActorChurnState_Type())
dot3adAggPortDebugActorChurnState.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortDebugActorChurnState.setStatus(_A)
_Dot3adAggPortDebugPartnerChurnState_Type=ChurnState
_Dot3adAggPortDebugPartnerChurnState_Object=MibTableColumn
dot3adAggPortDebugPartnerChurnState=_Dot3adAggPortDebugPartnerChurnState_Object((1,2,840,10006,300,43,1,2,3,1,6),_Dot3adAggPortDebugPartnerChurnState_Type())
dot3adAggPortDebugPartnerChurnState.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortDebugPartnerChurnState.setStatus(_A)
_Dot3adAggPortDebugActorChurnCount_Type=Counter32
_Dot3adAggPortDebugActorChurnCount_Object=MibTableColumn
dot3adAggPortDebugActorChurnCount=_Dot3adAggPortDebugActorChurnCount_Object((1,2,840,10006,300,43,1,2,3,1,7),_Dot3adAggPortDebugActorChurnCount_Type())
dot3adAggPortDebugActorChurnCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortDebugActorChurnCount.setStatus(_A)
_Dot3adAggPortDebugPartnerChurnCount_Type=Counter32
_Dot3adAggPortDebugPartnerChurnCount_Object=MibTableColumn
dot3adAggPortDebugPartnerChurnCount=_Dot3adAggPortDebugPartnerChurnCount_Object((1,2,840,10006,300,43,1,2,3,1,8),_Dot3adAggPortDebugPartnerChurnCount_Type())
dot3adAggPortDebugPartnerChurnCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortDebugPartnerChurnCount.setStatus(_A)
_Dot3adAggPortDebugActorSyncTransitionCount_Type=Counter32
_Dot3adAggPortDebugActorSyncTransitionCount_Object=MibTableColumn
dot3adAggPortDebugActorSyncTransitionCount=_Dot3adAggPortDebugActorSyncTransitionCount_Object((1,2,840,10006,300,43,1,2,3,1,9),_Dot3adAggPortDebugActorSyncTransitionCount_Type())
dot3adAggPortDebugActorSyncTransitionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortDebugActorSyncTransitionCount.setStatus(_A)
_Dot3adAggPortDebugPartnerSyncTransitionCount_Type=Counter32
_Dot3adAggPortDebugPartnerSyncTransitionCount_Object=MibTableColumn
dot3adAggPortDebugPartnerSyncTransitionCount=_Dot3adAggPortDebugPartnerSyncTransitionCount_Object((1,2,840,10006,300,43,1,2,3,1,10),_Dot3adAggPortDebugPartnerSyncTransitionCount_Type())
dot3adAggPortDebugPartnerSyncTransitionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortDebugPartnerSyncTransitionCount.setStatus(_A)
_Dot3adAggPortDebugActorChangeCount_Type=Counter32
_Dot3adAggPortDebugActorChangeCount_Object=MibTableColumn
dot3adAggPortDebugActorChangeCount=_Dot3adAggPortDebugActorChangeCount_Object((1,2,840,10006,300,43,1,2,3,1,11),_Dot3adAggPortDebugActorChangeCount_Type())
dot3adAggPortDebugActorChangeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortDebugActorChangeCount.setStatus(_A)
_Dot3adAggPortDebugPartnerChangeCount_Type=Counter32
_Dot3adAggPortDebugPartnerChangeCount_Object=MibTableColumn
dot3adAggPortDebugPartnerChangeCount=_Dot3adAggPortDebugPartnerChangeCount_Object((1,2,840,10006,300,43,1,2,3,1,12),_Dot3adAggPortDebugPartnerChangeCount_Type())
dot3adAggPortDebugPartnerChangeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortDebugPartnerChangeCount.setStatus(_A)
_Dot3adTablesLastChanged_Type=TimeTicks
_Dot3adTablesLastChanged_Object=MibScalar
dot3adTablesLastChanged=_Dot3adTablesLastChanged_Object((1,2,840,10006,300,43,1,3),_Dot3adTablesLastChanged_Type())
dot3adTablesLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adTablesLastChanged.setStatus(_A)
_Dot3adAggConformance_ObjectIdentity=ObjectIdentity
dot3adAggConformance=_Dot3adAggConformance_ObjectIdentity((1,2,840,10006,300,43,2))
_Dot3adAggGroups_ObjectIdentity=ObjectIdentity
dot3adAggGroups=_Dot3adAggGroups_ObjectIdentity((1,2,840,10006,300,43,2,1))
_Dot3adAggCompliances_ObjectIdentity=ObjectIdentity
dot3adAggCompliances=_Dot3adAggCompliances_ObjectIdentity((1,2,840,10006,300,43,2,2))
dot3adAggGroup=ObjectGroup((1,2,840,10006,300,43,2,1,1))
dot3adAggGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:dot3adAggGroup.setStatus(_A)
dot3adAggPortListGroup=ObjectGroup((1,2,840,10006,300,43,2,1,2))
dot3adAggPortListGroup.setObjects((_B,_V))
if mibBuilder.loadTexts:dot3adAggPortListGroup.setStatus(_A)
dot3adAggPortGroup=ObjectGroup((1,2,840,10006,300,43,2,1,3))
dot3adAggPortGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:dot3adAggPortGroup.setStatus(_A)
dot3adAggPortStatsGroup=ObjectGroup((1,2,840,10006,300,43,2,1,4))
dot3adAggPortStatsGroup.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:dot3adAggPortStatsGroup.setStatus(_A)
dot3adAggPortDebugGroup=ObjectGroup((1,2,840,10006,300,43,2,1,5))
dot3adAggPortDebugGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:dot3adAggPortDebugGroup.setStatus(_A)
dot3adTablesLastChangedGroup=ObjectGroup((1,2,840,10006,300,43,2,1,6))
dot3adTablesLastChangedGroup.setObjects((_B,_AD))
if mibBuilder.loadTexts:dot3adTablesLastChangedGroup.setStatus(_A)
dot3adAggCompliance=ModuleCompliance((1,2,840,10006,300,43,2,2,1))
dot3adAggCompliance.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:dot3adAggCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'LacpKey':LacpKey,'LacpState':LacpState,'ChurnState':ChurnState,'lagMIB':lagMIB,'lagMIBObjects':lagMIBObjects,'dot3adAgg':dot3adAgg,'dot3adAggTable':dot3adAggTable,'dot3adAggEntry':dot3adAggEntry,_G:dot3adAggIndex,_P:dot3adAggMACAddress,_M:dot3adAggActorSystemPriority,_L:dot3adAggActorSystemID,_N:dot3adAggAggregateOrIndividual,_O:dot3adAggActorAdminKey,_Q:dot3adAggActorOperKey,_R:dot3adAggPartnerSystemID,_S:dot3adAggPartnerSystemPriority,_T:dot3adAggPartnerOperKey,_U:dot3adAggCollectorMaxDelay,'dot3adAggPortListTable':dot3adAggPortListTable,'dot3adAggPortListEntry':dot3adAggPortListEntry,_V:dot3adAggPortListPorts,'dot3adAggPort':dot3adAggPort,'dot3adAggPortTable':dot3adAggPortTable,'dot3adAggPortEntry':dot3adAggPortEntry,_F:dot3adAggPortIndex,_W:dot3adAggPortActorSystemPriority,_X:dot3adAggPortActorSystemID,_Y:dot3adAggPortActorAdminKey,_Z:dot3adAggPortActorOperKey,_a:dot3adAggPortPartnerAdminSystemPriority,_b:dot3adAggPortPartnerOperSystemPriority,_c:dot3adAggPortPartnerAdminSystemID,_d:dot3adAggPortPartnerOperSystemID,_e:dot3adAggPortPartnerAdminKey,_f:dot3adAggPortPartnerOperKey,_g:dot3adAggPortSelectedAggID,_h:dot3adAggPortAttachedAggID,_i:dot3adAggPortActorPort,_j:dot3adAggPortActorPortPriority,_k:dot3adAggPortPartnerAdminPort,_l:dot3adAggPortPartnerOperPort,_m:dot3adAggPortPartnerAdminPortPriority,_n:dot3adAggPortPartnerOperPortPriority,_o:dot3adAggPortActorAdminState,_p:dot3adAggPortActorOperState,_q:dot3adAggPortPartnerAdminState,_r:dot3adAggPortPartnerOperState,_s:dot3adAggPortAggregateOrIndividual,'dot3adAggPortStatsTable':dot3adAggPortStatsTable,'dot3adAggPortStatsEntry':dot3adAggPortStatsEntry,_t:dot3adAggPortStatsLACPDUsRx,_u:dot3adAggPortStatsMarkerPDUsRx,_v:dot3adAggPortStatsMarkerResponsePDUsRx,_w:dot3adAggPortStatsUnknownRx,_x:dot3adAggPortStatsIllegalRx,_y:dot3adAggPortStatsLACPDUsTx,_z:dot3adAggPortStatsMarkerPDUsTx,_A0:dot3adAggPortStatsMarkerResponsePDUsTx,'dot3adAggPortDebugTable':dot3adAggPortDebugTable,'dot3adAggPortDebugEntry':dot3adAggPortDebugEntry,_A1:dot3adAggPortDebugRxState,_A2:dot3adAggPortDebugLastRxTime,_A3:dot3adAggPortDebugMuxState,_A4:dot3adAggPortDebugMuxReason,_A5:dot3adAggPortDebugActorChurnState,_A6:dot3adAggPortDebugPartnerChurnState,_A7:dot3adAggPortDebugActorChurnCount,_A8:dot3adAggPortDebugPartnerChurnCount,_A9:dot3adAggPortDebugActorSyncTransitionCount,_AA:dot3adAggPortDebugPartnerSyncTransitionCount,_AB:dot3adAggPortDebugActorChangeCount,_AC:dot3adAggPortDebugPartnerChangeCount,_AD:dot3adTablesLastChanged,'dot3adAggConformance':dot3adAggConformance,'dot3adAggGroups':dot3adAggGroups,_AE:dot3adAggGroup,_AH:dot3adAggPortListGroup,_AF:dot3adAggPortGroup,_AI:dot3adAggPortStatsGroup,_AJ:dot3adAggPortDebugGroup,_AG:dot3adTablesLastChangedGroup,'dot3adAggCompliances':dot3adAggCompliances,'dot3adAggCompliance':dot3adAggCompliance})