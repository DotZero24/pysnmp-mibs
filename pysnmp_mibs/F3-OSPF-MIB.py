_AC='f3OspfNbrExtGroup'
_AB='f3OspfIpMgmtTunnelExtGroup'
_AA='f3OspfIpInterfaceExtGroup'
_A9='f3OspfAreaGroup'
_A8='f3OspfRouterGroup'
_A7='f3OspfNbrExtRole'
_A6='f3OspfIpMgmtTunnelExtAuthKey'
_A5='f3OspfIpMgmtTunnelExtAuthType'
_A4='f3OspfIpMgmtTunnelExtCost'
_A3='f3OspfIpMgmtTunnelExtRtrPriority'
_A2='f3OspfIpMgmtTunnelExtRetransInterval'
_A1='f3OspfIpMgmtTunnelExtRtrDeadInterval'
_A0='f3OspfIpMgmtTunnelExtHelloInterval'
_z='f3OspfIpMgmtTunnelExtIfType'
_y='f3OspfIpMgmtTunnelExtAreaId'
_x='f3OspfIpMgmtTunnelExtStatus'
_w='f3OspfIpInterfaceExtAuthKey'
_v='f3OspfIpInterfaceExtAuthType'
_u='f3OspfIpInterfaceExtCost'
_t='f3OspfIpInterfaceExtRtrPriority'
_s='f3OspfIpInterfaceExtRetransInterval'
_r='f3OspfIpInterfaceExtRtrDeadInterval'
_q='f3OspfIpInterfaceExtHelloInterval'
_p='f3OspfIpInterfaceExtIfType'
_o='f3OspfIpInterfaceExtAreaId'
_n='f3OspfIpInterfaceExtStatus'
_m='f3OspfAreaRowStatus'
_l='f3OspfAreaStorageType'
_k='f3OspfAreaLsaCount'
_j='f3OspfAreaSpfRuns'
_i='f3OspfAreaDefaultCost'
_h='f3OspfAreaAuthType'
_g='f3OspfAreaType'
_f='f3OspfRouterRowStatus'
_e='f3OspfRouterStorageType'
_d='f3OspfRouterAreaBdrRtrStatus'
_c='f3OspfRouterNumAttachedAreas'
_b='f3OspfRouterRedistributionType'
_a='f3OspfRouterMetric'
_Z='f3OspfRouterMetricType'
_Y='f3OspfNbrExtEntry'
_X='f3OspfIpMgmtTunnelExtEntry'
_W='f3OspfIpInterfaceExtEntry'
_V='0000000000000000'
_U='pointToMultipoint'
_T='pointToPoint'
_S='broadcast'
_R='00000000'
_Q='f3OspfAreaId'
_P='not-accessible'
_O='f3OspfRouterIndex'
_N='Unsigned32'
_M='OspfState'
_L='OspfAuthenticationType'
_K='HelloRange'
_J='DesignatedRouterPriority'
_I='AreaID'
_H='OctetString'
_G='read-only'
_F='seconds'
_E='Integer32'
_D='read-create'
_C='read-write'
_B='F3-OSPF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsp150cm,=mibBuilder.importSymbols('ADVA-MIB','fsp150cm')
cmIpInterfaceEntry,ipManagementTunnelEntry=mibBuilder.importSymbols('CM-IP-MIB','cmIpInterfaceEntry','ipManagementTunnelEntry')
AreaID,DesignatedRouterPriority,HelloRange,OspfAuthenticationType,RouterID,ospfNbrEntry=mibBuilder.importSymbols('OSPF-MIB',_I,_J,_K,_L,'RouterID','ospfNbrEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TruthValue')
f3OspfMIB=ModuleIdentity((1,3,6,1,4,1,2544,1,12,35))
if mibBuilder.loadTexts:f3OspfMIB.setRevisions(('2014-10-06 00:00',))
class OspfMetricType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('e1',1),('e2',2)))
class OspfRedistributionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('rip',2)))
class OspfState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('disabled',2),('passive',3)))
class OspfAreaType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('stub',2)))
class OspfRole(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bdr',1),('dr',2),('drother',3)))
_F3OspfConfigObjects_ObjectIdentity=ObjectIdentity
f3OspfConfigObjects=_F3OspfConfigObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,35,1))
_F3OspfRouterTable_Object=MibTable
f3OspfRouterTable=_F3OspfRouterTable_Object((1,3,6,1,4,1,2544,1,12,35,1,1))
if mibBuilder.loadTexts:f3OspfRouterTable.setStatus(_A)
_F3OspfRouterEntry_Object=MibTableRow
f3OspfRouterEntry=_F3OspfRouterEntry_Object((1,3,6,1,4,1,2544,1,12,35,1,1,1))
f3OspfRouterEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:f3OspfRouterEntry.setStatus(_A)
_F3OspfRouterIndex_Type=RouterID
_F3OspfRouterIndex_Object=MibTableColumn
f3OspfRouterIndex=_F3OspfRouterIndex_Object((1,3,6,1,4,1,2544,1,12,35,1,1,1,1),_F3OspfRouterIndex_Type())
f3OspfRouterIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:f3OspfRouterIndex.setStatus(_A)
_F3OspfRouterMetricType_Type=OspfMetricType
_F3OspfRouterMetricType_Object=MibTableColumn
f3OspfRouterMetricType=_F3OspfRouterMetricType_Object((1,3,6,1,4,1,2544,1,12,35,1,1,1,2),_F3OspfRouterMetricType_Type())
f3OspfRouterMetricType.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OspfRouterMetricType.setStatus(_A)
class _F3OspfRouterMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777214))
_F3OspfRouterMetric_Type.__name__=_E
_F3OspfRouterMetric_Object=MibTableColumn
f3OspfRouterMetric=_F3OspfRouterMetric_Object((1,3,6,1,4,1,2544,1,12,35,1,1,1,3),_F3OspfRouterMetric_Type())
f3OspfRouterMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OspfRouterMetric.setStatus(_A)
_F3OspfRouterRedistributionType_Type=OspfRedistributionType
_F3OspfRouterRedistributionType_Object=MibTableColumn
f3OspfRouterRedistributionType=_F3OspfRouterRedistributionType_Object((1,3,6,1,4,1,2544,1,12,35,1,1,1,4),_F3OspfRouterRedistributionType_Type())
f3OspfRouterRedistributionType.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OspfRouterRedistributionType.setStatus(_A)
_F3OspfRouterNumAttachedAreas_Type=Unsigned32
_F3OspfRouterNumAttachedAreas_Object=MibTableColumn
f3OspfRouterNumAttachedAreas=_F3OspfRouterNumAttachedAreas_Object((1,3,6,1,4,1,2544,1,12,35,1,1,1,5),_F3OspfRouterNumAttachedAreas_Type())
f3OspfRouterNumAttachedAreas.setMaxAccess(_G)
if mibBuilder.loadTexts:f3OspfRouterNumAttachedAreas.setStatus(_A)
_F3OspfRouterAreaBdrRtrStatus_Type=TruthValue
_F3OspfRouterAreaBdrRtrStatus_Object=MibTableColumn
f3OspfRouterAreaBdrRtrStatus=_F3OspfRouterAreaBdrRtrStatus_Object((1,3,6,1,4,1,2544,1,12,35,1,1,1,6),_F3OspfRouterAreaBdrRtrStatus_Type())
f3OspfRouterAreaBdrRtrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OspfRouterAreaBdrRtrStatus.setStatus(_A)
_F3OspfRouterStorageType_Type=StorageType
_F3OspfRouterStorageType_Object=MibTableColumn
f3OspfRouterStorageType=_F3OspfRouterStorageType_Object((1,3,6,1,4,1,2544,1,12,35,1,1,1,7),_F3OspfRouterStorageType_Type())
f3OspfRouterStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OspfRouterStorageType.setStatus(_A)
_F3OspfRouterRowStatus_Type=RowStatus
_F3OspfRouterRowStatus_Object=MibTableColumn
f3OspfRouterRowStatus=_F3OspfRouterRowStatus_Object((1,3,6,1,4,1,2544,1,12,35,1,1,1,8),_F3OspfRouterRowStatus_Type())
f3OspfRouterRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OspfRouterRowStatus.setStatus(_A)
_F3OspfAreaTable_Object=MibTable
f3OspfAreaTable=_F3OspfAreaTable_Object((1,3,6,1,4,1,2544,1,12,35,1,2))
if mibBuilder.loadTexts:f3OspfAreaTable.setStatus(_A)
_F3OspfAreaEntry_Object=MibTableRow
f3OspfAreaEntry=_F3OspfAreaEntry_Object((1,3,6,1,4,1,2544,1,12,35,1,2,1))
f3OspfAreaEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:f3OspfAreaEntry.setStatus(_A)
_F3OspfAreaId_Type=AreaID
_F3OspfAreaId_Object=MibTableColumn
f3OspfAreaId=_F3OspfAreaId_Object((1,3,6,1,4,1,2544,1,12,35,1,2,1,1),_F3OspfAreaId_Type())
f3OspfAreaId.setMaxAccess(_P)
if mibBuilder.loadTexts:f3OspfAreaId.setStatus(_A)
_F3OspfAreaType_Type=OspfAreaType
_F3OspfAreaType_Object=MibTableColumn
f3OspfAreaType=_F3OspfAreaType_Object((1,3,6,1,4,1,2544,1,12,35,1,2,1,2),_F3OspfAreaType_Type())
f3OspfAreaType.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OspfAreaType.setStatus(_A)
_F3OspfAreaAuthType_Type=OspfAuthenticationType
_F3OspfAreaAuthType_Object=MibTableColumn
f3OspfAreaAuthType=_F3OspfAreaAuthType_Object((1,3,6,1,4,1,2544,1,12,35,1,2,1,3),_F3OspfAreaAuthType_Type())
f3OspfAreaAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OspfAreaAuthType.setStatus(_A)
class _F3OspfAreaDefaultCost_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_F3OspfAreaDefaultCost_Type.__name__=_N
_F3OspfAreaDefaultCost_Object=MibTableColumn
f3OspfAreaDefaultCost=_F3OspfAreaDefaultCost_Object((1,3,6,1,4,1,2544,1,12,35,1,2,1,4),_F3OspfAreaDefaultCost_Type())
f3OspfAreaDefaultCost.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OspfAreaDefaultCost.setStatus(_A)
_F3OspfAreaSpfRuns_Type=Counter32
_F3OspfAreaSpfRuns_Object=MibTableColumn
f3OspfAreaSpfRuns=_F3OspfAreaSpfRuns_Object((1,3,6,1,4,1,2544,1,12,35,1,2,1,5),_F3OspfAreaSpfRuns_Type())
f3OspfAreaSpfRuns.setMaxAccess(_G)
if mibBuilder.loadTexts:f3OspfAreaSpfRuns.setStatus(_A)
_F3OspfAreaLsaCount_Type=Gauge32
_F3OspfAreaLsaCount_Object=MibTableColumn
f3OspfAreaLsaCount=_F3OspfAreaLsaCount_Object((1,3,6,1,4,1,2544,1,12,35,1,2,1,6),_F3OspfAreaLsaCount_Type())
f3OspfAreaLsaCount.setMaxAccess(_G)
if mibBuilder.loadTexts:f3OspfAreaLsaCount.setStatus(_A)
_F3OspfAreaStorageType_Type=StorageType
_F3OspfAreaStorageType_Object=MibTableColumn
f3OspfAreaStorageType=_F3OspfAreaStorageType_Object((1,3,6,1,4,1,2544,1,12,35,1,2,1,7),_F3OspfAreaStorageType_Type())
f3OspfAreaStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OspfAreaStorageType.setStatus(_A)
_F3OspfAreaRowStatus_Type=RowStatus
_F3OspfAreaRowStatus_Object=MibTableColumn
f3OspfAreaRowStatus=_F3OspfAreaRowStatus_Object((1,3,6,1,4,1,2544,1,12,35,1,2,1,8),_F3OspfAreaRowStatus_Type())
f3OspfAreaRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:f3OspfAreaRowStatus.setStatus(_A)
_F3OspfIpInterfaceExtTable_Object=MibTable
f3OspfIpInterfaceExtTable=_F3OspfIpInterfaceExtTable_Object((1,3,6,1,4,1,2544,1,12,35,1,3))
if mibBuilder.loadTexts:f3OspfIpInterfaceExtTable.setStatus(_A)
_F3OspfIpInterfaceExtEntry_Object=MibTableRow
f3OspfIpInterfaceExtEntry=_F3OspfIpInterfaceExtEntry_Object((1,3,6,1,4,1,2544,1,12,35,1,3,1))
if mibBuilder.loadTexts:f3OspfIpInterfaceExtEntry.setStatus(_A)
class _F3OspfIpInterfaceExtStatus_Type(OspfState):defaultValue=1
_F3OspfIpInterfaceExtStatus_Type.__name__=_M
_F3OspfIpInterfaceExtStatus_Object=MibTableColumn
f3OspfIpInterfaceExtStatus=_F3OspfIpInterfaceExtStatus_Object((1,3,6,1,4,1,2544,1,12,35,1,3,1,1),_F3OspfIpInterfaceExtStatus_Type())
f3OspfIpInterfaceExtStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpInterfaceExtStatus.setStatus(_A)
class _F3OspfIpInterfaceExtAreaId_Type(AreaID):defaultHexValue=_R
_F3OspfIpInterfaceExtAreaId_Type.__name__=_I
_F3OspfIpInterfaceExtAreaId_Object=MibTableColumn
f3OspfIpInterfaceExtAreaId=_F3OspfIpInterfaceExtAreaId_Object((1,3,6,1,4,1,2544,1,12,35,1,3,1,2),_F3OspfIpInterfaceExtAreaId_Type())
f3OspfIpInterfaceExtAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpInterfaceExtAreaId.setStatus(_A)
class _F3OspfIpInterfaceExtIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5)));namedValues=NamedValues(*((_S,1),('nbma',2),(_T,3),(_U,5)))
_F3OspfIpInterfaceExtIfType_Type.__name__=_E
_F3OspfIpInterfaceExtIfType_Object=MibTableColumn
f3OspfIpInterfaceExtIfType=_F3OspfIpInterfaceExtIfType_Object((1,3,6,1,4,1,2544,1,12,35,1,3,1,3),_F3OspfIpInterfaceExtIfType_Type())
f3OspfIpInterfaceExtIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpInterfaceExtIfType.setStatus(_A)
class _F3OspfIpInterfaceExtHelloInterval_Type(HelloRange):defaultValue=10
_F3OspfIpInterfaceExtHelloInterval_Type.__name__=_K
_F3OspfIpInterfaceExtHelloInterval_Object=MibTableColumn
f3OspfIpInterfaceExtHelloInterval=_F3OspfIpInterfaceExtHelloInterval_Object((1,3,6,1,4,1,2544,1,12,35,1,3,1,4),_F3OspfIpInterfaceExtHelloInterval_Type())
f3OspfIpInterfaceExtHelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpInterfaceExtHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:f3OspfIpInterfaceExtHelloInterval.setUnits(_F)
class _F3OspfIpInterfaceExtRtrDeadInterval_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_F3OspfIpInterfaceExtRtrDeadInterval_Type.__name__=_E
_F3OspfIpInterfaceExtRtrDeadInterval_Object=MibTableColumn
f3OspfIpInterfaceExtRtrDeadInterval=_F3OspfIpInterfaceExtRtrDeadInterval_Object((1,3,6,1,4,1,2544,1,12,35,1,3,1,5),_F3OspfIpInterfaceExtRtrDeadInterval_Type())
f3OspfIpInterfaceExtRtrDeadInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpInterfaceExtRtrDeadInterval.setStatus(_A)
if mibBuilder.loadTexts:f3OspfIpInterfaceExtRtrDeadInterval.setUnits(_F)
class _F3OspfIpInterfaceExtRetransInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_F3OspfIpInterfaceExtRetransInterval_Type.__name__=_E
_F3OspfIpInterfaceExtRetransInterval_Object=MibTableColumn
f3OspfIpInterfaceExtRetransInterval=_F3OspfIpInterfaceExtRetransInterval_Object((1,3,6,1,4,1,2544,1,12,35,1,3,1,6),_F3OspfIpInterfaceExtRetransInterval_Type())
f3OspfIpInterfaceExtRetransInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpInterfaceExtRetransInterval.setStatus(_A)
if mibBuilder.loadTexts:f3OspfIpInterfaceExtRetransInterval.setUnits(_F)
class _F3OspfIpInterfaceExtRtrPriority_Type(DesignatedRouterPriority):defaultValue=1
_F3OspfIpInterfaceExtRtrPriority_Type.__name__=_J
_F3OspfIpInterfaceExtRtrPriority_Object=MibTableColumn
f3OspfIpInterfaceExtRtrPriority=_F3OspfIpInterfaceExtRtrPriority_Object((1,3,6,1,4,1,2544,1,12,35,1,3,1,7),_F3OspfIpInterfaceExtRtrPriority_Type())
f3OspfIpInterfaceExtRtrPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpInterfaceExtRtrPriority.setStatus(_A)
class _F3OspfIpInterfaceExtCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_F3OspfIpInterfaceExtCost_Type.__name__=_E
_F3OspfIpInterfaceExtCost_Object=MibTableColumn
f3OspfIpInterfaceExtCost=_F3OspfIpInterfaceExtCost_Object((1,3,6,1,4,1,2544,1,12,35,1,3,1,8),_F3OspfIpInterfaceExtCost_Type())
f3OspfIpInterfaceExtCost.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpInterfaceExtCost.setStatus(_A)
class _F3OspfIpInterfaceExtAuthType_Type(OspfAuthenticationType):defaultValue=0
_F3OspfIpInterfaceExtAuthType_Type.__name__=_L
_F3OspfIpInterfaceExtAuthType_Object=MibTableColumn
f3OspfIpInterfaceExtAuthType=_F3OspfIpInterfaceExtAuthType_Object((1,3,6,1,4,1,2544,1,12,35,1,3,1,9),_F3OspfIpInterfaceExtAuthType_Type())
f3OspfIpInterfaceExtAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpInterfaceExtAuthType.setStatus(_A)
class _F3OspfIpInterfaceExtAuthKey_Type(OctetString):defaultHexValue=_V;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_F3OspfIpInterfaceExtAuthKey_Type.__name__=_H
_F3OspfIpInterfaceExtAuthKey_Object=MibTableColumn
f3OspfIpInterfaceExtAuthKey=_F3OspfIpInterfaceExtAuthKey_Object((1,3,6,1,4,1,2544,1,12,35,1,3,1,10),_F3OspfIpInterfaceExtAuthKey_Type())
f3OspfIpInterfaceExtAuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpInterfaceExtAuthKey.setStatus(_A)
_F3OspfIpMgmtTunnelExtTable_Object=MibTable
f3OspfIpMgmtTunnelExtTable=_F3OspfIpMgmtTunnelExtTable_Object((1,3,6,1,4,1,2544,1,12,35,1,4))
if mibBuilder.loadTexts:f3OspfIpMgmtTunnelExtTable.setStatus(_A)
_F3OspfIpMgmtTunnelExtEntry_Object=MibTableRow
f3OspfIpMgmtTunnelExtEntry=_F3OspfIpMgmtTunnelExtEntry_Object((1,3,6,1,4,1,2544,1,12,35,1,4,1))
if mibBuilder.loadTexts:f3OspfIpMgmtTunnelExtEntry.setStatus(_A)
class _F3OspfIpMgmtTunnelExtStatus_Type(OspfState):defaultValue=1
_F3OspfIpMgmtTunnelExtStatus_Type.__name__=_M
_F3OspfIpMgmtTunnelExtStatus_Object=MibTableColumn
f3OspfIpMgmtTunnelExtStatus=_F3OspfIpMgmtTunnelExtStatus_Object((1,3,6,1,4,1,2544,1,12,35,1,4,1,1),_F3OspfIpMgmtTunnelExtStatus_Type())
f3OspfIpMgmtTunnelExtStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpMgmtTunnelExtStatus.setStatus(_A)
class _F3OspfIpMgmtTunnelExtAreaId_Type(AreaID):defaultHexValue=_R
_F3OspfIpMgmtTunnelExtAreaId_Type.__name__=_I
_F3OspfIpMgmtTunnelExtAreaId_Object=MibTableColumn
f3OspfIpMgmtTunnelExtAreaId=_F3OspfIpMgmtTunnelExtAreaId_Object((1,3,6,1,4,1,2544,1,12,35,1,4,1,2),_F3OspfIpMgmtTunnelExtAreaId_Type())
f3OspfIpMgmtTunnelExtAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpMgmtTunnelExtAreaId.setStatus(_A)
class _F3OspfIpMgmtTunnelExtIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5)));namedValues=NamedValues(*((_S,1),('nbma',2),(_T,3),(_U,5)))
_F3OspfIpMgmtTunnelExtIfType_Type.__name__=_E
_F3OspfIpMgmtTunnelExtIfType_Object=MibTableColumn
f3OspfIpMgmtTunnelExtIfType=_F3OspfIpMgmtTunnelExtIfType_Object((1,3,6,1,4,1,2544,1,12,35,1,4,1,3),_F3OspfIpMgmtTunnelExtIfType_Type())
f3OspfIpMgmtTunnelExtIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpMgmtTunnelExtIfType.setStatus(_A)
class _F3OspfIpMgmtTunnelExtHelloInterval_Type(HelloRange):defaultValue=10
_F3OspfIpMgmtTunnelExtHelloInterval_Type.__name__=_K
_F3OspfIpMgmtTunnelExtHelloInterval_Object=MibTableColumn
f3OspfIpMgmtTunnelExtHelloInterval=_F3OspfIpMgmtTunnelExtHelloInterval_Object((1,3,6,1,4,1,2544,1,12,35,1,4,1,4),_F3OspfIpMgmtTunnelExtHelloInterval_Type())
f3OspfIpMgmtTunnelExtHelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpMgmtTunnelExtHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:f3OspfIpMgmtTunnelExtHelloInterval.setUnits(_F)
class _F3OspfIpMgmtTunnelExtRtrDeadInterval_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_F3OspfIpMgmtTunnelExtRtrDeadInterval_Type.__name__=_E
_F3OspfIpMgmtTunnelExtRtrDeadInterval_Object=MibTableColumn
f3OspfIpMgmtTunnelExtRtrDeadInterval=_F3OspfIpMgmtTunnelExtRtrDeadInterval_Object((1,3,6,1,4,1,2544,1,12,35,1,4,1,5),_F3OspfIpMgmtTunnelExtRtrDeadInterval_Type())
f3OspfIpMgmtTunnelExtRtrDeadInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpMgmtTunnelExtRtrDeadInterval.setStatus(_A)
if mibBuilder.loadTexts:f3OspfIpMgmtTunnelExtRtrDeadInterval.setUnits(_F)
class _F3OspfIpMgmtTunnelExtRetransInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_F3OspfIpMgmtTunnelExtRetransInterval_Type.__name__=_E
_F3OspfIpMgmtTunnelExtRetransInterval_Object=MibTableColumn
f3OspfIpMgmtTunnelExtRetransInterval=_F3OspfIpMgmtTunnelExtRetransInterval_Object((1,3,6,1,4,1,2544,1,12,35,1,4,1,6),_F3OspfIpMgmtTunnelExtRetransInterval_Type())
f3OspfIpMgmtTunnelExtRetransInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpMgmtTunnelExtRetransInterval.setStatus(_A)
if mibBuilder.loadTexts:f3OspfIpMgmtTunnelExtRetransInterval.setUnits(_F)
class _F3OspfIpMgmtTunnelExtRtrPriority_Type(DesignatedRouterPriority):defaultValue=1
_F3OspfIpMgmtTunnelExtRtrPriority_Type.__name__=_J
_F3OspfIpMgmtTunnelExtRtrPriority_Object=MibTableColumn
f3OspfIpMgmtTunnelExtRtrPriority=_F3OspfIpMgmtTunnelExtRtrPriority_Object((1,3,6,1,4,1,2544,1,12,35,1,4,1,7),_F3OspfIpMgmtTunnelExtRtrPriority_Type())
f3OspfIpMgmtTunnelExtRtrPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpMgmtTunnelExtRtrPriority.setStatus(_A)
class _F3OspfIpMgmtTunnelExtCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_F3OspfIpMgmtTunnelExtCost_Type.__name__=_E
_F3OspfIpMgmtTunnelExtCost_Object=MibTableColumn
f3OspfIpMgmtTunnelExtCost=_F3OspfIpMgmtTunnelExtCost_Object((1,3,6,1,4,1,2544,1,12,35,1,4,1,8),_F3OspfIpMgmtTunnelExtCost_Type())
f3OspfIpMgmtTunnelExtCost.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpMgmtTunnelExtCost.setStatus(_A)
class _F3OspfIpMgmtTunnelExtAuthType_Type(OspfAuthenticationType):defaultValue=0
_F3OspfIpMgmtTunnelExtAuthType_Type.__name__=_L
_F3OspfIpMgmtTunnelExtAuthType_Object=MibTableColumn
f3OspfIpMgmtTunnelExtAuthType=_F3OspfIpMgmtTunnelExtAuthType_Object((1,3,6,1,4,1,2544,1,12,35,1,4,1,9),_F3OspfIpMgmtTunnelExtAuthType_Type())
f3OspfIpMgmtTunnelExtAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpMgmtTunnelExtAuthType.setStatus(_A)
class _F3OspfIpMgmtTunnelExtAuthKey_Type(OctetString):defaultHexValue=_V;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_F3OspfIpMgmtTunnelExtAuthKey_Type.__name__=_H
_F3OspfIpMgmtTunnelExtAuthKey_Object=MibTableColumn
f3OspfIpMgmtTunnelExtAuthKey=_F3OspfIpMgmtTunnelExtAuthKey_Object((1,3,6,1,4,1,2544,1,12,35,1,4,1,10),_F3OspfIpMgmtTunnelExtAuthKey_Type())
f3OspfIpMgmtTunnelExtAuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:f3OspfIpMgmtTunnelExtAuthKey.setStatus(_A)
_F3OspfNbrExtTable_Object=MibTable
f3OspfNbrExtTable=_F3OspfNbrExtTable_Object((1,3,6,1,4,1,2544,1,12,35,1,5))
if mibBuilder.loadTexts:f3OspfNbrExtTable.setStatus(_A)
_F3OspfNbrExtEntry_Object=MibTableRow
f3OspfNbrExtEntry=_F3OspfNbrExtEntry_Object((1,3,6,1,4,1,2544,1,12,35,1,5,1))
if mibBuilder.loadTexts:f3OspfNbrExtEntry.setStatus(_A)
_F3OspfNbrExtRole_Type=OspfRole
_F3OspfNbrExtRole_Object=MibTableColumn
f3OspfNbrExtRole=_F3OspfNbrExtRole_Object((1,3,6,1,4,1,2544,1,12,35,1,5,1,1),_F3OspfNbrExtRole_Type())
f3OspfNbrExtRole.setMaxAccess(_G)
if mibBuilder.loadTexts:f3OspfNbrExtRole.setStatus(_A)
_F3OspfConformance_ObjectIdentity=ObjectIdentity
f3OspfConformance=_F3OspfConformance_ObjectIdentity((1,3,6,1,4,1,2544,1,12,35,2))
_F3OspfCompliances_ObjectIdentity=ObjectIdentity
f3OspfCompliances=_F3OspfCompliances_ObjectIdentity((1,3,6,1,4,1,2544,1,12,35,2,1))
_F3OspfGroups_ObjectIdentity=ObjectIdentity
f3OspfGroups=_F3OspfGroups_ObjectIdentity((1,3,6,1,4,1,2544,1,12,35,2,2))
cmIpInterfaceEntry.registerAugmentions((_B,_W))
f3OspfIpInterfaceExtEntry.setIndexNames(*cmIpInterfaceEntry.getIndexNames())
ipManagementTunnelEntry.registerAugmentions((_B,_X))
f3OspfIpMgmtTunnelExtEntry.setIndexNames(*ipManagementTunnelEntry.getIndexNames())
ospfNbrEntry.registerAugmentions((_B,_Y))
f3OspfNbrExtEntry.setIndexNames(*ospfNbrEntry.getIndexNames())
f3OspfRouterGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,35,2,2,1))
f3OspfRouterGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:f3OspfRouterGroup.setStatus(_A)
f3OspfAreaGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,35,2,2,2))
f3OspfAreaGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:f3OspfAreaGroup.setStatus(_A)
f3OspfIpInterfaceExtGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,35,2,2,3))
f3OspfIpInterfaceExtGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:f3OspfIpInterfaceExtGroup.setStatus(_A)
f3OspfIpMgmtTunnelExtGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,35,2,2,4))
f3OspfIpMgmtTunnelExtGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:f3OspfIpMgmtTunnelExtGroup.setStatus(_A)
f3OspfNbrExtGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,35,2,2,5))
f3OspfNbrExtGroup.setObjects((_B,_A7))
if mibBuilder.loadTexts:f3OspfNbrExtGroup.setStatus(_A)
f3OspfCompliance=ModuleCompliance((1,3,6,1,4,1,2544,1,12,35,2,1,1))
f3OspfCompliance.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:f3OspfCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'OspfMetricType':OspfMetricType,'OspfRedistributionType':OspfRedistributionType,_M:OspfState,'OspfAreaType':OspfAreaType,'OspfRole':OspfRole,'f3OspfMIB':f3OspfMIB,'f3OspfConfigObjects':f3OspfConfigObjects,'f3OspfRouterTable':f3OspfRouterTable,'f3OspfRouterEntry':f3OspfRouterEntry,_O:f3OspfRouterIndex,_Z:f3OspfRouterMetricType,_a:f3OspfRouterMetric,_b:f3OspfRouterRedistributionType,_c:f3OspfRouterNumAttachedAreas,_d:f3OspfRouterAreaBdrRtrStatus,_e:f3OspfRouterStorageType,_f:f3OspfRouterRowStatus,'f3OspfAreaTable':f3OspfAreaTable,'f3OspfAreaEntry':f3OspfAreaEntry,_Q:f3OspfAreaId,_g:f3OspfAreaType,_h:f3OspfAreaAuthType,_i:f3OspfAreaDefaultCost,_j:f3OspfAreaSpfRuns,_k:f3OspfAreaLsaCount,_l:f3OspfAreaStorageType,_m:f3OspfAreaRowStatus,'f3OspfIpInterfaceExtTable':f3OspfIpInterfaceExtTable,_W:f3OspfIpInterfaceExtEntry,_n:f3OspfIpInterfaceExtStatus,_o:f3OspfIpInterfaceExtAreaId,_p:f3OspfIpInterfaceExtIfType,_q:f3OspfIpInterfaceExtHelloInterval,_r:f3OspfIpInterfaceExtRtrDeadInterval,_s:f3OspfIpInterfaceExtRetransInterval,_t:f3OspfIpInterfaceExtRtrPriority,_u:f3OspfIpInterfaceExtCost,_v:f3OspfIpInterfaceExtAuthType,_w:f3OspfIpInterfaceExtAuthKey,'f3OspfIpMgmtTunnelExtTable':f3OspfIpMgmtTunnelExtTable,_X:f3OspfIpMgmtTunnelExtEntry,_x:f3OspfIpMgmtTunnelExtStatus,_y:f3OspfIpMgmtTunnelExtAreaId,_z:f3OspfIpMgmtTunnelExtIfType,_A0:f3OspfIpMgmtTunnelExtHelloInterval,_A1:f3OspfIpMgmtTunnelExtRtrDeadInterval,_A2:f3OspfIpMgmtTunnelExtRetransInterval,_A3:f3OspfIpMgmtTunnelExtRtrPriority,_A4:f3OspfIpMgmtTunnelExtCost,_A5:f3OspfIpMgmtTunnelExtAuthType,_A6:f3OspfIpMgmtTunnelExtAuthKey,'f3OspfNbrExtTable':f3OspfNbrExtTable,_Y:f3OspfNbrExtEntry,_A7:f3OspfNbrExtRole,'f3OspfConformance':f3OspfConformance,'f3OspfCompliances':f3OspfCompliances,'f3OspfCompliance':f3OspfCompliance,'f3OspfGroups':f3OspfGroups,_A8:f3OspfRouterGroup,_A9:f3OspfAreaGroup,_AA:f3OspfIpInterfaceExtGroup,_AB:f3OspfIpMgmtTunnelExtGroup,_AC:f3OspfNbrExtGroup})