_T='gfpTpGroup'
_S='gfpTpHistStatsEnable'
_R='gfpTpGFPState'
_Q='gfpTpNetworkMap'
_P='gfpTpServiceModeQualifier'
_O='gfpTpServiceMode'
_N='gfpTpChannelId'
_M='gfpTpExtHeaderType'
_L='gfpTpPayloadFCS'
_K='Unsigned32'
_J='InfnServiceMode'
_I='InfnSMQ'
_H='InfnGfpExtHdrTyp'
_G='InfnGFPPayloadFCS'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='read-write'
_B='INFINERA-TP-GFPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnGFPPayloadFCS,InfnGFPState,InfnGfpExtHdrTyp,InfnNetworkMapping,InfnPmHistStatsControl,InfnSMQ,InfnServiceMode=mibBuilder.importSymbols('INFINERA-TC-MIB',_G,'InfnGFPState',_H,'InfnNetworkMapping','InfnPmHistStatsControl',_I,_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gfpTpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,80))
if mibBuilder.loadTexts:gfpTpMIB.setRevisions(('2011-04-20 00:00',))
_GfpTpTable_Object=MibTable
gfpTpTable=_GfpTpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,80,1))
if mibBuilder.loadTexts:gfpTpTable.setStatus(_A)
_GfpTpEntry_Object=MibTableRow
gfpTpEntry=_GfpTpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,80,1,1))
gfpTpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:gfpTpEntry.setStatus(_A)
class _GfpTpPayloadFCS_Type(InfnGFPPayloadFCS):defaultValue=2
_GfpTpPayloadFCS_Type.__name__=_G
_GfpTpPayloadFCS_Object=MibTableColumn
gfpTpPayloadFCS=_GfpTpPayloadFCS_Object((1,3,6,1,4,1,21296,2,2,2,2,80,1,1,1),_GfpTpPayloadFCS_Type())
gfpTpPayloadFCS.setMaxAccess(_C)
if mibBuilder.loadTexts:gfpTpPayloadFCS.setStatus(_A)
class _GfpTpExtHeaderType_Type(InfnGfpExtHdrTyp):defaultValue=1
_GfpTpExtHeaderType_Type.__name__=_H
_GfpTpExtHeaderType_Object=MibTableColumn
gfpTpExtHeaderType=_GfpTpExtHeaderType_Object((1,3,6,1,4,1,21296,2,2,2,2,80,1,1,2),_GfpTpExtHeaderType_Type())
gfpTpExtHeaderType.setMaxAccess(_C)
if mibBuilder.loadTexts:gfpTpExtHeaderType.setStatus(_A)
class _GfpTpChannelId_Type(Unsigned32):defaultValue=0
_GfpTpChannelId_Type.__name__=_K
_GfpTpChannelId_Object=MibTableColumn
gfpTpChannelId=_GfpTpChannelId_Object((1,3,6,1,4,1,21296,2,2,2,2,80,1,1,3),_GfpTpChannelId_Type())
gfpTpChannelId.setMaxAccess(_C)
if mibBuilder.loadTexts:gfpTpChannelId.setStatus(_A)
class _GfpTpServiceMode_Type(InfnServiceMode):defaultValue=1
_GfpTpServiceMode_Type.__name__=_J
_GfpTpServiceMode_Object=MibTableColumn
gfpTpServiceMode=_GfpTpServiceMode_Object((1,3,6,1,4,1,21296,2,2,2,2,80,1,1,4),_GfpTpServiceMode_Type())
gfpTpServiceMode.setMaxAccess(_D)
if mibBuilder.loadTexts:gfpTpServiceMode.setStatus(_A)
class _GfpTpServiceModeQualifier_Type(InfnSMQ):defaultValue=1
_GfpTpServiceModeQualifier_Type.__name__=_I
_GfpTpServiceModeQualifier_Object=MibTableColumn
gfpTpServiceModeQualifier=_GfpTpServiceModeQualifier_Object((1,3,6,1,4,1,21296,2,2,2,2,80,1,1,5),_GfpTpServiceModeQualifier_Type())
gfpTpServiceModeQualifier.setMaxAccess(_D)
if mibBuilder.loadTexts:gfpTpServiceModeQualifier.setStatus(_A)
_GfpTpNetworkMap_Type=InfnNetworkMapping
_GfpTpNetworkMap_Object=MibTableColumn
gfpTpNetworkMap=_GfpTpNetworkMap_Object((1,3,6,1,4,1,21296,2,2,2,2,80,1,1,6),_GfpTpNetworkMap_Type())
gfpTpNetworkMap.setMaxAccess(_D)
if mibBuilder.loadTexts:gfpTpNetworkMap.setStatus(_A)
_GfpTpGFPState_Type=InfnGFPState
_GfpTpGFPState_Object=MibTableColumn
gfpTpGFPState=_GfpTpGFPState_Object((1,3,6,1,4,1,21296,2,2,2,2,80,1,1,7),_GfpTpGFPState_Type())
gfpTpGFPState.setMaxAccess(_D)
if mibBuilder.loadTexts:gfpTpGFPState.setStatus(_A)
_GfpTpHistStatsEnable_Type=InfnPmHistStatsControl
_GfpTpHistStatsEnable_Object=MibTableColumn
gfpTpHistStatsEnable=_GfpTpHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,80,1,1,8),_GfpTpHistStatsEnable_Type())
gfpTpHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:gfpTpHistStatsEnable.setStatus(_A)
_GfpTpConformance_ObjectIdentity=ObjectIdentity
gfpTpConformance=_GfpTpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,80,3))
_GfpTpCompliances_ObjectIdentity=ObjectIdentity
gfpTpCompliances=_GfpTpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,80,3,1))
_GfpTpGroups_ObjectIdentity=ObjectIdentity
gfpTpGroups=_GfpTpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,80,3,2))
gfpTpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,80,3,2,1))
gfpTpGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:gfpTpGroup.setStatus(_A)
gfpTpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,80,3,1,1))
gfpTpCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:gfpTpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'gfpTpMIB':gfpTpMIB,'gfpTpTable':gfpTpTable,'gfpTpEntry':gfpTpEntry,_L:gfpTpPayloadFCS,_M:gfpTpExtHeaderType,_N:gfpTpChannelId,_O:gfpTpServiceMode,_P:gfpTpServiceModeQualifier,_Q:gfpTpNetworkMap,_R:gfpTpGFPState,_S:gfpTpHistStatsEnable,'gfpTpConformance':gfpTpConformance,'gfpTpCompliances':gfpTpCompliances,'gfpTpCompliance':gfpTpCompliance,'gfpTpGroups':gfpTpGroups,_T:gfpTpGroup})