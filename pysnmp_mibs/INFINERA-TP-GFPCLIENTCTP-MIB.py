_T='gfpclientCtpGroup'
_S='gfpclientCtpChannelId'
_R='gfpclientCtpExtHeaderType'
_Q='gfpclientCtpGFPState'
_P='gfpclientCtpPayloadFCS'
_O='gfpclientCtpConfigServiceType'
_N='gfpclientCtpServiceModeQualifier'
_M='gfpclientCtpServiceMode'
_L='Integer32'
_K='InfnServiceType'
_J='InfnServiceMode'
_I='InfnSMQ'
_H='InfnGfpExtHdrTyp'
_G='InfnGFPPayloadFCS'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='read-only'
_B='INFINERA-TP-GFPCLIENTCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnGFPPayloadFCS,InfnGFPState,InfnGfpExtHdrTyp,InfnSMQ,InfnServiceMode,InfnServiceType=mibBuilder.importSymbols('INFINERA-TC-MIB',_G,'InfnGFPState',_H,_I,_J,_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
gfpclientCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,32))
if mibBuilder.loadTexts:gfpclientCtpMIB.setRevisions(('2011-04-20 00:00',))
_GfpclientCtpTable_Object=MibTable
gfpclientCtpTable=_GfpclientCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,32,1))
if mibBuilder.loadTexts:gfpclientCtpTable.setStatus(_A)
_GfpclientCtpEntry_Object=MibTableRow
gfpclientCtpEntry=_GfpclientCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,32,1,1))
gfpclientCtpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:gfpclientCtpEntry.setStatus(_A)
class _GfpclientCtpServiceMode_Type(InfnServiceMode):defaultValue=1
_GfpclientCtpServiceMode_Type.__name__=_J
_GfpclientCtpServiceMode_Object=MibTableColumn
gfpclientCtpServiceMode=_GfpclientCtpServiceMode_Object((1,3,6,1,4,1,21296,2,2,2,2,32,1,1,1),_GfpclientCtpServiceMode_Type())
gfpclientCtpServiceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:gfpclientCtpServiceMode.setStatus(_A)
class _GfpclientCtpServiceModeQualifier_Type(InfnSMQ):defaultValue=1
_GfpclientCtpServiceModeQualifier_Type.__name__=_I
_GfpclientCtpServiceModeQualifier_Object=MibTableColumn
gfpclientCtpServiceModeQualifier=_GfpclientCtpServiceModeQualifier_Object((1,3,6,1,4,1,21296,2,2,2,2,32,1,1,2),_GfpclientCtpServiceModeQualifier_Type())
gfpclientCtpServiceModeQualifier.setMaxAccess(_C)
if mibBuilder.loadTexts:gfpclientCtpServiceModeQualifier.setStatus(_A)
class _GfpclientCtpConfigServiceType_Type(InfnServiceType):defaultValue=99
_GfpclientCtpConfigServiceType_Type.__name__=_K
_GfpclientCtpConfigServiceType_Object=MibTableColumn
gfpclientCtpConfigServiceType=_GfpclientCtpConfigServiceType_Object((1,3,6,1,4,1,21296,2,2,2,2,32,1,1,3),_GfpclientCtpConfigServiceType_Type())
gfpclientCtpConfigServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:gfpclientCtpConfigServiceType.setStatus(_A)
class _GfpclientCtpPayloadFCS_Type(InfnGFPPayloadFCS):defaultValue=2
_GfpclientCtpPayloadFCS_Type.__name__=_G
_GfpclientCtpPayloadFCS_Object=MibTableColumn
gfpclientCtpPayloadFCS=_GfpclientCtpPayloadFCS_Object((1,3,6,1,4,1,21296,2,2,2,2,32,1,1,4),_GfpclientCtpPayloadFCS_Type())
gfpclientCtpPayloadFCS.setMaxAccess(_D)
if mibBuilder.loadTexts:gfpclientCtpPayloadFCS.setStatus(_A)
_GfpclientCtpGFPState_Type=InfnGFPState
_GfpclientCtpGFPState_Object=MibTableColumn
gfpclientCtpGFPState=_GfpclientCtpGFPState_Object((1,3,6,1,4,1,21296,2,2,2,2,32,1,1,5),_GfpclientCtpGFPState_Type())
gfpclientCtpGFPState.setMaxAccess(_C)
if mibBuilder.loadTexts:gfpclientCtpGFPState.setStatus(_A)
class _GfpclientCtpExtHeaderType_Type(InfnGfpExtHdrTyp):defaultValue=1
_GfpclientCtpExtHeaderType_Type.__name__=_H
_GfpclientCtpExtHeaderType_Object=MibTableColumn
gfpclientCtpExtHeaderType=_GfpclientCtpExtHeaderType_Object((1,3,6,1,4,1,21296,2,2,2,2,32,1,1,6),_GfpclientCtpExtHeaderType_Type())
gfpclientCtpExtHeaderType.setMaxAccess(_D)
if mibBuilder.loadTexts:gfpclientCtpExtHeaderType.setStatus(_A)
class _GfpclientCtpChannelId_Type(Integer32):defaultValue=0
_GfpclientCtpChannelId_Type.__name__=_L
_GfpclientCtpChannelId_Object=MibTableColumn
gfpclientCtpChannelId=_GfpclientCtpChannelId_Object((1,3,6,1,4,1,21296,2,2,2,2,32,1,1,7),_GfpclientCtpChannelId_Type())
gfpclientCtpChannelId.setMaxAccess(_D)
if mibBuilder.loadTexts:gfpclientCtpChannelId.setStatus(_A)
_GfpclientCtpConformance_ObjectIdentity=ObjectIdentity
gfpclientCtpConformance=_GfpclientCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,32,3))
_GfpclientCtpCompliances_ObjectIdentity=ObjectIdentity
gfpclientCtpCompliances=_GfpclientCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,32,3,1))
_GfpclientCtpGroups_ObjectIdentity=ObjectIdentity
gfpclientCtpGroups=_GfpclientCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,32,3,2))
gfpclientCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,32,3,2,1))
gfpclientCtpGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:gfpclientCtpGroup.setStatus(_A)
gfpclientCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,32,3,1,1))
gfpclientCtpCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:gfpclientCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'gfpclientCtpMIB':gfpclientCtpMIB,'gfpclientCtpTable':gfpclientCtpTable,'gfpclientCtpEntry':gfpclientCtpEntry,_M:gfpclientCtpServiceMode,_N:gfpclientCtpServiceModeQualifier,_O:gfpclientCtpConfigServiceType,_P:gfpclientCtpPayloadFCS,_Q:gfpclientCtpGFPState,_R:gfpclientCtpExtHeaderType,_S:gfpclientCtpChannelId,'gfpclientCtpConformance':gfpclientCtpConformance,'gfpclientCtpCompliances':gfpclientCtpCompliances,'gfpclientCtpCompliance':gfpclientCtpCompliance,'gfpclientCtpGroups':gfpclientCtpGroups,_T:gfpclientCtpGroup})