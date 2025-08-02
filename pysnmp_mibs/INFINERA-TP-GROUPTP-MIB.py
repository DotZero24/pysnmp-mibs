_T='groupTpGroup'
_S='groupTpServiceAvailability'
_R='groupTpSupportingCircuitIdList'
_Q='groupTpConfigPayload'
_P='groupTpPmHistStatsEnable'
_O='groupTpCrossConnectType'
_N='groupTpDtpList'
_M='groupTpGtpType'
_L='groupTpSwReason'
_K='groupTpProtMod'
_J='groupTpCfgProtSt'
_I='InfnServiceType'
_H='ifIndex'
_G='IF-MIB'
_F='read-create'
_E='none'
_D='read-only'
_C='Integer32'
_B='INFINERA-TP-GROUPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatTenths,InfnServiceType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
groupTpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,10))
if mibBuilder.loadTexts:groupTpMIB.setRevisions(('2008-10-20 00:00',))
_GroupTpTable_Object=MibTable
groupTpTable=_GroupTpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,10,1))
if mibBuilder.loadTexts:groupTpTable.setStatus(_A)
_GroupTpEntry_Object=MibTableRow
groupTpEntry=_GroupTpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,10,1,1))
groupTpEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:groupTpEntry.setStatus(_A)
class _GroupTpCfgProtSt_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('wrk',2),('prot',3),('relb',4),('pu',5)))
_GroupTpCfgProtSt_Type.__name__=_C
_GroupTpCfgProtSt_Object=MibTableColumn
groupTpCfgProtSt=_GroupTpCfgProtSt_Object((1,3,6,1,4,1,21296,2,2,2,2,10,1,1,1),_GroupTpCfgProtSt_Type())
groupTpCfgProtSt.setMaxAccess(_D)
if mibBuilder.loadTexts:groupTpCfgProtSt.setStatus(_A)
class _GroupTpProtMod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('dtDSNCP',2),('stDSNCP',3)))
_GroupTpProtMod_Type.__name__=_C
_GroupTpProtMod_Object=MibTableColumn
groupTpProtMod=_GroupTpProtMod_Object((1,3,6,1,4,1,21296,2,2,2,2,10,1,1,2),_GroupTpProtMod_Type())
groupTpProtMod.setMaxAccess(_D)
if mibBuilder.loadTexts:groupTpProtMod.setStatus(_A)
class _GroupTpSwReason_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('mSwP',1),('mSwW',2),('wLck',3),('pLck',4),('auto',5),(_E,6),('revert',7),('admLck',8),('unProv',9),('eqFlt',10),('liFlt',11),('liSF',12),('clRxFlt',13),('clTxFlt',14),('sysLof',15)))
_GroupTpSwReason_Type.__name__=_C
_GroupTpSwReason_Object=MibTableColumn
groupTpSwReason=_GroupTpSwReason_Object((1,3,6,1,4,1,21296,2,2,2,2,10,1,1,3),_GroupTpSwReason_Type())
groupTpSwReason.setMaxAccess(_D)
if mibBuilder.loadTexts:groupTpSwReason.setStatus(_A)
class _GroupTpGtpType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('trib',1),('line',2),('hybrid',3)))
_GroupTpGtpType_Type.__name__=_C
_GroupTpGtpType_Object=MibTableColumn
groupTpGtpType=_GroupTpGtpType_Object((1,3,6,1,4,1,21296,2,2,2,2,10,1,1,4),_GroupTpGtpType_Type())
groupTpGtpType.setMaxAccess(_F)
if mibBuilder.loadTexts:groupTpGtpType.setStatus(_A)
_GroupTpDtpList_Type=DisplayString
_GroupTpDtpList_Object=MibTableColumn
groupTpDtpList=_GroupTpDtpList_Object((1,3,6,1,4,1,21296,2,2,2,2,10,1,1,5),_GroupTpDtpList_Type())
groupTpDtpList.setMaxAccess(_F)
if mibBuilder.loadTexts:groupTpDtpList.setStatus(_A)
class _GroupTpCrossConnectType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),('unidirectionFrom',2),('unidirectionTo',3),('unidirectionToAndFrom',4),('bidirection',5),('bidirectionUnidirectionFrom',6),('bidirectionUnidirectionTo',7),('bidirectionUnidirectionToAndFrom',8)))
_GroupTpCrossConnectType_Type.__name__=_C
_GroupTpCrossConnectType_Object=MibTableColumn
groupTpCrossConnectType=_GroupTpCrossConnectType_Object((1,3,6,1,4,1,21296,2,2,2,2,10,1,1,6),_GroupTpCrossConnectType_Type())
groupTpCrossConnectType.setMaxAccess(_D)
if mibBuilder.loadTexts:groupTpCrossConnectType.setStatus(_A)
class _GroupTpPmHistStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_GroupTpPmHistStatsEnable_Type.__name__=_C
_GroupTpPmHistStatsEnable_Object=MibTableColumn
groupTpPmHistStatsEnable=_GroupTpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,10,1,1,7),_GroupTpPmHistStatsEnable_Type())
groupTpPmHistStatsEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:groupTpPmHistStatsEnable.setStatus(_A)
class _GroupTpConfigPayload_Type(InfnServiceType):defaultValue=1
_GroupTpConfigPayload_Type.__name__=_I
_GroupTpConfigPayload_Object=MibTableColumn
groupTpConfigPayload=_GroupTpConfigPayload_Object((1,3,6,1,4,1,21296,2,2,2,2,10,1,1,8),_GroupTpConfigPayload_Type())
groupTpConfigPayload.setMaxAccess(_D)
if mibBuilder.loadTexts:groupTpConfigPayload.setStatus(_A)
_GroupTpSupportingCircuitIdList_Type=DisplayString
_GroupTpSupportingCircuitIdList_Object=MibTableColumn
groupTpSupportingCircuitIdList=_GroupTpSupportingCircuitIdList_Object((1,3,6,1,4,1,21296,2,2,2,2,10,1,1,9),_GroupTpSupportingCircuitIdList_Type())
groupTpSupportingCircuitIdList.setMaxAccess(_D)
if mibBuilder.loadTexts:groupTpSupportingCircuitIdList.setStatus(_A)
class _GroupTpServiceAvailability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('available',1),('notAvailable',2)))
_GroupTpServiceAvailability_Type.__name__=_C
_GroupTpServiceAvailability_Object=MibTableColumn
groupTpServiceAvailability=_GroupTpServiceAvailability_Object((1,3,6,1,4,1,21296,2,2,2,2,10,1,1,10),_GroupTpServiceAvailability_Type())
groupTpServiceAvailability.setMaxAccess(_D)
if mibBuilder.loadTexts:groupTpServiceAvailability.setStatus(_A)
_GroupTpConformance_ObjectIdentity=ObjectIdentity
groupTpConformance=_GroupTpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,10,3))
_GroupTpCompliances_ObjectIdentity=ObjectIdentity
groupTpCompliances=_GroupTpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,10,3,1))
_GroupTpGroups_ObjectIdentity=ObjectIdentity
groupTpGroups=_GroupTpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,10,3,2))
groupTpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,10,3,2,1))
groupTpGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:groupTpGroup.setStatus(_A)
groupTpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,10,3,1,1))
groupTpCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:groupTpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'groupTpMIB':groupTpMIB,'groupTpTable':groupTpTable,'groupTpEntry':groupTpEntry,_J:groupTpCfgProtSt,_K:groupTpProtMod,_L:groupTpSwReason,_M:groupTpGtpType,_N:groupTpDtpList,_O:groupTpCrossConnectType,_P:groupTpPmHistStatsEnable,_Q:groupTpConfigPayload,_R:groupTpSupportingCircuitIdList,_S:groupTpServiceAvailability,'groupTpConformance':groupTpConformance,'groupTpCompliances':groupTpCompliances,'groupTpCompliance':groupTpCompliance,'groupTpGroups':groupTpGroups,_T:groupTpGroup})