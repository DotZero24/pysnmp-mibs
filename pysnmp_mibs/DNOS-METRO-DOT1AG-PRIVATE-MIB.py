_O='agentDot1agRMepIdentifier'
_N='agentDot1agRMepMepIdIndex'
_M='agentDot1agRMepMaIndex'
_L='agentDot1agRMepMdIndex'
_K='agentDot1agMipIfIndex'
_J='agentDot1agMipMdIndex'
_I='disable'
_H='enable'
_G='read-create'
_F='Unsigned32'
_E='not-accessible'
_D='DNOS-METRO-DOT1AG-PRIVATE-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dnOS,=mibBuilder.importSymbols('DELL-REF-MIB','dnOS')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowPointer','RowStatus','StorageType','TextualConvention','TruthValue')
fastPathDot1agPrivateMIB=ModuleIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45))
if mibBuilder.loadTexts:fastPathDot1agPrivateMIB.setRevisions(('2011-01-26 00:00','2008-05-27 00:00'))
_Dot1agGlobalConfigGroup_ObjectIdentity=ObjectIdentity
dot1agGlobalConfigGroup=_Dot1agGlobalConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,1))
_AgentDot1agGlobalConfigGroup_ObjectIdentity=ObjectIdentity
agentDot1agGlobalConfigGroup=_AgentDot1agGlobalConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,1,1))
class _AgentDot1agCfmStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentDot1agCfmStatus_Type.__name__=_B
_AgentDot1agCfmStatus_Object=MibScalar
agentDot1agCfmStatus=_AgentDot1agCfmStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,1,1,1),_AgentDot1agCfmStatus_Type())
agentDot1agCfmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1agCfmStatus.setStatus(_A)
class _AgentDot1agCfmArchieveHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentDot1agCfmArchieveHoldTime_Type.__name__=_B
_AgentDot1agCfmArchieveHoldTime_Object=MibScalar
agentDot1agCfmArchieveHoldTime=_AgentDot1agCfmArchieveHoldTime_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,1,1,2),_AgentDot1agCfmArchieveHoldTime_Type())
agentDot1agCfmArchieveHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1agCfmArchieveHoldTime.setStatus(_A)
class _AgentDot1agCfmClearRemoteMEPs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AgentDot1agCfmClearRemoteMEPs_Type.__name__=_B
_AgentDot1agCfmClearRemoteMEPs_Object=MibScalar
agentDot1agCfmClearRemoteMEPs=_AgentDot1agCfmClearRemoteMEPs_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,1,1,3),_AgentDot1agCfmClearRemoteMEPs_Type())
agentDot1agCfmClearRemoteMEPs.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1agCfmClearRemoteMEPs.setStatus(_A)
class _AgentDot1agCfmClearTraceRouteCache_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AgentDot1agCfmClearTraceRouteCache_Type.__name__=_B
_AgentDot1agCfmClearTraceRouteCache_Object=MibScalar
agentDot1agCfmClearTraceRouteCache=_AgentDot1agCfmClearTraceRouteCache_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,1,1,4),_AgentDot1agCfmClearTraceRouteCache_Type())
agentDot1agCfmClearTraceRouteCache.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1agCfmClearTraceRouteCache.setStatus(_A)
class _AgentDot1agCfmClearStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AgentDot1agCfmClearStatistics_Type.__name__=_B
_AgentDot1agCfmClearStatistics_Object=MibScalar
agentDot1agCfmClearStatistics=_AgentDot1agCfmClearStatistics_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,1,1,5),_AgentDot1agCfmClearStatistics_Type())
agentDot1agCfmClearStatistics.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1agCfmClearStatistics.setStatus(_A)
_Dot1agMipConfigGroup_ObjectIdentity=ObjectIdentity
dot1agMipConfigGroup=_Dot1agMipConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,2))
_AgentDot1agMipConfigGroup_ObjectIdentity=ObjectIdentity
agentDot1agMipConfigGroup=_AgentDot1agMipConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,2,1))
_AgentDot1agMipTable_Object=MibTable
agentDot1agMipTable=_AgentDot1agMipTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,2,1,1))
if mibBuilder.loadTexts:agentDot1agMipTable.setStatus(_A)
_AgentDot1agMipEntry_Object=MibTableRow
agentDot1agMipEntry=_AgentDot1agMipEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,2,1,1,1))
agentDot1agMipEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:agentDot1agMipEntry.setStatus(_A)
class _AgentDot1agMipMdIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_AgentDot1agMipMdIndex_Type.__name__=_F
_AgentDot1agMipMdIndex_Object=MibTableColumn
agentDot1agMipMdIndex=_AgentDot1agMipMdIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,2,1,1,1,1),_AgentDot1agMipMdIndex_Type())
agentDot1agMipMdIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agentDot1agMipMdIndex.setStatus(_A)
_AgentDot1agMipIfIndex_Type=InterfaceIndex
_AgentDot1agMipIfIndex_Object=MibTableColumn
agentDot1agMipIfIndex=_AgentDot1agMipIfIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,2,1,1,1,2),_AgentDot1agMipIfIndex_Type())
agentDot1agMipIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agentDot1agMipIfIndex.setStatus(_A)
class _AgentDot1agMipMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentDot1agMipMode_Type.__name__=_B
_AgentDot1agMipMode_Object=MibTableColumn
agentDot1agMipMode=_AgentDot1agMipMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,2,1,1,1,3),_AgentDot1agMipMode_Type())
agentDot1agMipMode.setMaxAccess(_G)
if mibBuilder.loadTexts:agentDot1agMipMode.setStatus(_A)
_Dot1agRMepConfigGroup_ObjectIdentity=ObjectIdentity
dot1agRMepConfigGroup=_Dot1agRMepConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,3))
_AgentDot1agRMepConfigGroup_ObjectIdentity=ObjectIdentity
agentDot1agRMepConfigGroup=_AgentDot1agRMepConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,3,1))
_AgentDot1agRMepTable_Object=MibTable
agentDot1agRMepTable=_AgentDot1agRMepTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,3,1,1))
if mibBuilder.loadTexts:agentDot1agRMepTable.setStatus(_A)
_AgentDot1agRMepEntry_Object=MibTableRow
agentDot1agRMepEntry=_AgentDot1agRMepEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,3,1,1,1))
agentDot1agRMepEntry.setIndexNames((0,_D,_L),(0,_D,_M),(0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:agentDot1agRMepEntry.setStatus(_A)
_AgentDot1agRMepMdIndex_Type=Unsigned32
_AgentDot1agRMepMdIndex_Object=MibTableColumn
agentDot1agRMepMdIndex=_AgentDot1agRMepMdIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,3,1,1,1,1),_AgentDot1agRMepMdIndex_Type())
agentDot1agRMepMdIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agentDot1agRMepMdIndex.setStatus(_A)
_AgentDot1agRMepMaIndex_Type=Unsigned32
_AgentDot1agRMepMaIndex_Object=MibTableColumn
agentDot1agRMepMaIndex=_AgentDot1agRMepMaIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,3,1,1,1,2),_AgentDot1agRMepMaIndex_Type())
agentDot1agRMepMaIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agentDot1agRMepMaIndex.setStatus(_A)
class _AgentDot1agRMepMepIdIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,8191))
_AgentDot1agRMepMepIdIndex_Type.__name__=_F
_AgentDot1agRMepMepIdIndex_Object=MibTableColumn
agentDot1agRMepMepIdIndex=_AgentDot1agRMepMepIdIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,3,1,1,1,3),_AgentDot1agRMepMepIdIndex_Type())
agentDot1agRMepMepIdIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agentDot1agRMepMepIdIndex.setStatus(_A)
class _AgentDot1agRMepIdentifier_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,8191))
_AgentDot1agRMepIdentifier_Type.__name__=_F
_AgentDot1agRMepIdentifier_Object=MibTableColumn
agentDot1agRMepIdentifier=_AgentDot1agRMepIdentifier_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,3,1,1,1,4),_AgentDot1agRMepIdentifier_Type())
agentDot1agRMepIdentifier.setMaxAccess(_G)
if mibBuilder.loadTexts:agentDot1agRMepIdentifier.setStatus(_A)
_AgentDot1agRMepIfIndex_Type=InterfaceIndex
_AgentDot1agRMepIfIndex_Object=MibTableColumn
agentDot1agRMepIfIndex=_AgentDot1agRMepIfIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,3,1,1,1,5),_AgentDot1agRMepIfIndex_Type())
agentDot1agRMepIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1agRMepIfIndex.setStatus(_A)
_AgentDot1agRMepMacAddress_Type=MacAddress
_AgentDot1agRMepMacAddress_Object=MibTableColumn
agentDot1agRMepMacAddress=_AgentDot1agRMepMacAddress_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,3,1,1,1,6),_AgentDot1agRMepMacAddress_Type())
agentDot1agRMepMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1agRMepMacAddress.setStatus(_A)
_AgentDot1agRMepRowStatus_Type=RowStatus
_AgentDot1agRMepRowStatus_Object=MibTableColumn
agentDot1agRMepRowStatus=_AgentDot1agRMepRowStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,45,3,1,1,1,7),_AgentDot1agRMepRowStatus_Type())
agentDot1agRMepRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:agentDot1agRMepRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fastPathDot1agPrivateMIB':fastPathDot1agPrivateMIB,'dot1agGlobalConfigGroup':dot1agGlobalConfigGroup,'agentDot1agGlobalConfigGroup':agentDot1agGlobalConfigGroup,'agentDot1agCfmStatus':agentDot1agCfmStatus,'agentDot1agCfmArchieveHoldTime':agentDot1agCfmArchieveHoldTime,'agentDot1agCfmClearRemoteMEPs':agentDot1agCfmClearRemoteMEPs,'agentDot1agCfmClearTraceRouteCache':agentDot1agCfmClearTraceRouteCache,'agentDot1agCfmClearStatistics':agentDot1agCfmClearStatistics,'dot1agMipConfigGroup':dot1agMipConfigGroup,'agentDot1agMipConfigGroup':agentDot1agMipConfigGroup,'agentDot1agMipTable':agentDot1agMipTable,'agentDot1agMipEntry':agentDot1agMipEntry,_J:agentDot1agMipMdIndex,_K:agentDot1agMipIfIndex,'agentDot1agMipMode':agentDot1agMipMode,'dot1agRMepConfigGroup':dot1agRMepConfigGroup,'agentDot1agRMepConfigGroup':agentDot1agRMepConfigGroup,'agentDot1agRMepTable':agentDot1agRMepTable,'agentDot1agRMepEntry':agentDot1agRMepEntry,_L:agentDot1agRMepMdIndex,_M:agentDot1agRMepMaIndex,_N:agentDot1agRMepMepIdIndex,_O:agentDot1agRMepIdentifier,'agentDot1agRMepIfIndex':agentDot1agRMepIfIndex,'agentDot1agRMepMacAddress':agentDot1agRMepMacAddress,'agentDot1agRMepRowStatus':agentDot1agRMepRowStatus})