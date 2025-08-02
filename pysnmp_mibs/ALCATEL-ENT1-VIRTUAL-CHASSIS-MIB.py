_Ad='virtualChassisVflMemberPortGroup'
_Ac='virtualChassisVflGroup'
_Ab='virtualChassisSlotRestStatusGroup'
_Aa='virtualChassisChassisResetListGroup'
_AZ='virtualChassisNeighborGroup'
_AY='virtualChassisGlobalGroup'
_AX='virtualChassisLocalInfoGroup'
_AW='virtualChassisVflSpeedTypeChange'
_AV='virtualChassisUpgradeComplete'
_AU='virtualChassisVflMemberPortJoinFailure'
_AT='virtualChassisVflMemberPortStatusChange'
_AS='virtualChassisVflStatusChange'
_AR='virtualChassisRoleChange'
_AQ='virtualChassisStatusChange'
_AP='virtualChassisAutoVflPortRowStatus'
_AO='virtualChassisAutoVflPortMemberStatus'
_AN='virtualChassisAutoVflIfindex'
_AM='virtualChassisVflMemberPortRowStatus'
_AL='virtualChassisVflMemberPortIsPrimay'
_AK='virtualChassisVflDirectNeighborChasId'
_AJ='virtualChassisVflRowStatus'
_AI='virtualChassisVflConfigPortNum'
_AH='virtualChassisVflActivePortNum'
_AG='virtualChassisVflPrimaryPort'
_AF='virtualChassisVflDefaultVlan'
_AE='virtualChassisSlotResetStatus'
_AD='virtualChassisChassisResetList'
_AC='virtualChassisNeighborIsDirect'
_AB='virtualChassisNeighborShortestPath'
_AA='virtualChassisVflMode'
_A9='virtualChassisNumOfDirectNeighbor'
_A8='virtualChassisNumOfNeighbor'
_A7='virtualChassisGlobalConsis'
_A6='virtualChassisLicenseConsis'
_A5='virtualChassisGroupConsis'
_A4='virtualChassisChassisTypeConsis'
_A3='virtualChassisConfigHelloIntervalConsis'
_A2='virtualChassisOperHelloIntervalConsis'
_A1='virtualChassisConfigControlVlanConsis'
_A0='virtualChassisOperControlVlanConsis'
_z='virtualChassisConfigChasIdConsis'
_y='virtualChassisOperChasIdConsis'
_x='virtualChassisLicense'
_w='virtualChassisType'
_v='virtualChassisConfigControlVlan'
_u='virtualChassisConfigHelloInterval'
_t='virtualChassisOperControlVlan'
_s='virtualChassisOperHelloInterval'
_r='virtualChassisSecCmm'
_q='virtualChassisPriCmm'
_p='virtualChassisDesigNI'
_o='virtualChassisUpTime'
_n='virtualChassisMac'
_m='virtualChassisGroup'
_l='virtualChassisConfigPriority'
_k='virtualChassisOperPriority'
_j='virtualChassisPreviousRole'
_i='virtualChassisConfigChassisId'
_h='virtualChassisLocalInfoChasId'
_g='virtualChassisAutoVflPortIfindex'
_f='virtualChassisSlotNum'
_e='virtualChassisNeighborChasId'
_d='VirtualChassisVflMode'
_c='VirtualChassisControlVlan'
_b='seconds'
_a='VirtualChassisGroup'
_Z='VirtualChassisPriority'
_Y='VirtualConfigChassisId'
_X='inconsistent'
_W='virtualChassisUpgradeCompleteStatus'
_V='virtualChassisDiagnostic'
_U='virtualChassisVflMemberPortOperStatus'
_T='virtualChassisVflSpeedType'
_S='virtualChassisVflOperStatus'
_R='virtualChassisStatus'
_Q='virtualChassisRole'
_P='down'
_O='VirtualChassisHelloInterval'
_N='unassigned'
_M='disabled'
_L='virtualChassisVflMemberPortIfindex'
_K='read-create'
_J='deprecated'
_I='SnmpAdminString'
_H='not-accessible'
_G='virtualChassisVflId'
_F='read-write'
_E='Integer32'
_D='virtualChassisOperChasId'
_C='read-only'
_B='ALCATEL-ENT1-VIRTUAL-CHASSIS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1VirtualChassisManager,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1VirtualChassisManager')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
alcatelIND1VirtualChassisMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,69,1))
if mibBuilder.loadTexts:alcatelIND1VirtualChassisMIB.setRevisions(('2011-05-25 00:00',))
class VirtualOperChassisId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class VirtualConfigChassisId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
class VirtualChassisHelloInterval(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class VirtualChassisControlVlan(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
class VirtualChassisCmmSlot(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,65,66)));namedValues=NamedValues(*(('notPresent',0),('cmmSlot1',65),('cmmSlot2',66)))
class VirtualChassisNiSlot(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
class VirtualChassisVflId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class VirtualChassisConsistency(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_X,0),('consistent',1),('na',2),(_M,3)))
class VirtualChassisRole(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_N,0),('master',1),('slave',2),(_X,3),('startuperror',4)))
class VirtualChassisStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('init',0),('running',1),('invalidChassisId',2),('helloDown',3),('duplicateChassisId',4),('mismatchImage',5),('mismatchChassisType',6),('mismatchHelloInterval',7),('mismatchControlVlan',8),('mismatchGroup',9),('mismatchLicenseConfig',10),('invalidLicense',11),('splitTopology',12),('commandShutdown',13),('failureShutdown',14)))
class VirtualChassisGroup(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class VirtualChassisPriority(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class VirtualChassisSlotResetStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('supported',0),('split',1)))
class VirtualChassisType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('invalid',0),('rushmore',1),('tor',2),('shasta',3),('medora',4),('everest',5)))
class VirtualChassisVflSpeedType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_N,0),('unknown',1),('mismatch',2),('tenGB',3),('fortyGB',4),('twentyOneGB',5)))
class VirtualChassisVflMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('auto',2)))
_AlcatelIND1VirtualChassisMIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1VirtualChassisMIBNotifications=_AlcatelIND1VirtualChassisMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,69,1,0))
if mibBuilder.loadTexts:alcatelIND1VirtualChassisMIBNotifications.setStatus(_A)
_AlcatelIND1VirtualChassisMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1VirtualChassisMIBObjects=_AlcatelIND1VirtualChassisMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,69,1,1))
if mibBuilder.loadTexts:alcatelIND1VirtualChassisMIBObjects.setStatus(_A)
_VirtualChassisLocalInfo_ObjectIdentity=ObjectIdentity
virtualChassisLocalInfo=_VirtualChassisLocalInfo_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,1))
_VirtualChassisLocalInfoChasId_Type=VirtualOperChassisId
_VirtualChassisLocalInfoChasId_Object=MibScalar
virtualChassisLocalInfoChasId=_VirtualChassisLocalInfoChasId_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,1,1),_VirtualChassisLocalInfoChasId_Type())
virtualChassisLocalInfoChasId.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisLocalInfoChasId.setStatus(_A)
_VirtualChassisGlobalTable_Object=MibTable
virtualChassisGlobalTable=_VirtualChassisGlobalTable_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2))
if mibBuilder.loadTexts:virtualChassisGlobalTable.setStatus(_A)
_VirtualChassisGlobalEntry_Object=MibTableRow
virtualChassisGlobalEntry=_VirtualChassisGlobalEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1))
virtualChassisGlobalEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:virtualChassisGlobalEntry.setStatus(_A)
_VirtualChassisOperChasId_Type=VirtualOperChassisId
_VirtualChassisOperChasId_Object=MibTableColumn
virtualChassisOperChasId=_VirtualChassisOperChasId_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,1),_VirtualChassisOperChasId_Type())
virtualChassisOperChasId.setMaxAccess(_H)
if mibBuilder.loadTexts:virtualChassisOperChasId.setStatus(_A)
class _VirtualChassisConfigChassisId_Type(VirtualConfigChassisId):defaultValue=0
_VirtualChassisConfigChassisId_Type.__name__=_Y
_VirtualChassisConfigChassisId_Object=MibTableColumn
virtualChassisConfigChassisId=_VirtualChassisConfigChassisId_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,2),_VirtualChassisConfigChassisId_Type())
virtualChassisConfigChassisId.setMaxAccess(_F)
if mibBuilder.loadTexts:virtualChassisConfigChassisId.setStatus(_A)
_VirtualChassisRole_Type=VirtualChassisRole
_VirtualChassisRole_Object=MibTableColumn
virtualChassisRole=_VirtualChassisRole_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,3),_VirtualChassisRole_Type())
virtualChassisRole.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisRole.setStatus(_A)
_VirtualChassisPreviousRole_Type=VirtualChassisRole
_VirtualChassisPreviousRole_Object=MibTableColumn
virtualChassisPreviousRole=_VirtualChassisPreviousRole_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,4),_VirtualChassisPreviousRole_Type())
virtualChassisPreviousRole.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisPreviousRole.setStatus(_A)
_VirtualChassisStatus_Type=VirtualChassisStatus
_VirtualChassisStatus_Object=MibTableColumn
virtualChassisStatus=_VirtualChassisStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,5),_VirtualChassisStatus_Type())
virtualChassisStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisStatus.setStatus(_A)
_VirtualChassisOperPriority_Type=VirtualChassisPriority
_VirtualChassisOperPriority_Object=MibTableColumn
virtualChassisOperPriority=_VirtualChassisOperPriority_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,6),_VirtualChassisOperPriority_Type())
virtualChassisOperPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisOperPriority.setStatus(_A)
class _VirtualChassisConfigPriority_Type(VirtualChassisPriority):defaultValue=100
_VirtualChassisConfigPriority_Type.__name__=_Z
_VirtualChassisConfigPriority_Object=MibTableColumn
virtualChassisConfigPriority=_VirtualChassisConfigPriority_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,7),_VirtualChassisConfigPriority_Type())
virtualChassisConfigPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:virtualChassisConfigPriority.setStatus(_A)
class _VirtualChassisGroup_Type(VirtualChassisGroup):defaultValue=0
_VirtualChassisGroup_Type.__name__=_a
_VirtualChassisGroup_Object=MibTableColumn
virtualChassisGroup=_VirtualChassisGroup_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,8),_VirtualChassisGroup_Type())
virtualChassisGroup.setMaxAccess(_F)
if mibBuilder.loadTexts:virtualChassisGroup.setStatus(_A)
_VirtualChassisMac_Type=MacAddress
_VirtualChassisMac_Object=MibTableColumn
virtualChassisMac=_VirtualChassisMac_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,9),_VirtualChassisMac_Type())
virtualChassisMac.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisMac.setStatus(_A)
_VirtualChassisUpTime_Type=TimeTicks
_VirtualChassisUpTime_Object=MibTableColumn
virtualChassisUpTime=_VirtualChassisUpTime_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,10),_VirtualChassisUpTime_Type())
virtualChassisUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisUpTime.setStatus(_A)
_VirtualChassisDesigNI_Type=VirtualChassisNiSlot
_VirtualChassisDesigNI_Object=MibTableColumn
virtualChassisDesigNI=_VirtualChassisDesigNI_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,11),_VirtualChassisDesigNI_Type())
virtualChassisDesigNI.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisDesigNI.setStatus(_A)
_VirtualChassisPriCmm_Type=VirtualChassisCmmSlot
_VirtualChassisPriCmm_Object=MibTableColumn
virtualChassisPriCmm=_VirtualChassisPriCmm_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,12),_VirtualChassisPriCmm_Type())
virtualChassisPriCmm.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisPriCmm.setStatus(_A)
_VirtualChassisSecCmm_Type=VirtualChassisCmmSlot
_VirtualChassisSecCmm_Object=MibTableColumn
virtualChassisSecCmm=_VirtualChassisSecCmm_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,13),_VirtualChassisSecCmm_Type())
virtualChassisSecCmm.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisSecCmm.setStatus(_A)
class _VirtualChassisOperHelloInterval_Type(VirtualChassisHelloInterval):defaultValue=10
_VirtualChassisOperHelloInterval_Type.__name__=_O
_VirtualChassisOperHelloInterval_Object=MibTableColumn
virtualChassisOperHelloInterval=_VirtualChassisOperHelloInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,14),_VirtualChassisOperHelloInterval_Type())
virtualChassisOperHelloInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:virtualChassisOperHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:virtualChassisOperHelloInterval.setUnits(_b)
_VirtualChassisOperControlVlan_Type=VirtualChassisControlVlan
_VirtualChassisOperControlVlan_Object=MibTableColumn
virtualChassisOperControlVlan=_VirtualChassisOperControlVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,15),_VirtualChassisOperControlVlan_Type())
virtualChassisOperControlVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisOperControlVlan.setStatus(_A)
class _VirtualChassisConfigHelloInterval_Type(VirtualChassisHelloInterval):defaultValue=2
_VirtualChassisConfigHelloInterval_Type.__name__=_O
_VirtualChassisConfigHelloInterval_Object=MibTableColumn
virtualChassisConfigHelloInterval=_VirtualChassisConfigHelloInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,16),_VirtualChassisConfigHelloInterval_Type())
virtualChassisConfigHelloInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:virtualChassisConfigHelloInterval.setStatus(_J)
if mibBuilder.loadTexts:virtualChassisConfigHelloInterval.setUnits(_b)
class _VirtualChassisConfigControlVlan_Type(VirtualChassisControlVlan):defaultValue=4094
_VirtualChassisConfigControlVlan_Type.__name__=_c
_VirtualChassisConfigControlVlan_Object=MibTableColumn
virtualChassisConfigControlVlan=_VirtualChassisConfigControlVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,17),_VirtualChassisConfigControlVlan_Type())
virtualChassisConfigControlVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:virtualChassisConfigControlVlan.setStatus(_A)
_VirtualChassisType_Type=VirtualChassisType
_VirtualChassisType_Object=MibTableColumn
virtualChassisType=_VirtualChassisType_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,18),_VirtualChassisType_Type())
virtualChassisType.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisType.setStatus(_A)
class _VirtualChassisLicense_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VirtualChassisLicense_Type.__name__=_I
_VirtualChassisLicense_Object=MibTableColumn
virtualChassisLicense=_VirtualChassisLicense_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,19),_VirtualChassisLicense_Type())
virtualChassisLicense.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisLicense.setStatus(_A)
_VirtualChassisOperChasIdConsis_Type=VirtualChassisConsistency
_VirtualChassisOperChasIdConsis_Object=MibTableColumn
virtualChassisOperChasIdConsis=_VirtualChassisOperChasIdConsis_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,20),_VirtualChassisOperChasIdConsis_Type())
virtualChassisOperChasIdConsis.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisOperChasIdConsis.setStatus(_A)
_VirtualChassisConfigChasIdConsis_Type=VirtualChassisConsistency
_VirtualChassisConfigChasIdConsis_Object=MibTableColumn
virtualChassisConfigChasIdConsis=_VirtualChassisConfigChasIdConsis_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,21),_VirtualChassisConfigChasIdConsis_Type())
virtualChassisConfigChasIdConsis.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisConfigChasIdConsis.setStatus(_A)
_VirtualChassisOperControlVlanConsis_Type=VirtualChassisConsistency
_VirtualChassisOperControlVlanConsis_Object=MibTableColumn
virtualChassisOperControlVlanConsis=_VirtualChassisOperControlVlanConsis_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,22),_VirtualChassisOperControlVlanConsis_Type())
virtualChassisOperControlVlanConsis.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisOperControlVlanConsis.setStatus(_A)
_VirtualChassisConfigControlVlanConsis_Type=VirtualChassisConsistency
_VirtualChassisConfigControlVlanConsis_Object=MibTableColumn
virtualChassisConfigControlVlanConsis=_VirtualChassisConfigControlVlanConsis_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,23),_VirtualChassisConfigControlVlanConsis_Type())
virtualChassisConfigControlVlanConsis.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisConfigControlVlanConsis.setStatus(_A)
_VirtualChassisOperHelloIntervalConsis_Type=VirtualChassisConsistency
_VirtualChassisOperHelloIntervalConsis_Object=MibTableColumn
virtualChassisOperHelloIntervalConsis=_VirtualChassisOperHelloIntervalConsis_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,24),_VirtualChassisOperHelloIntervalConsis_Type())
virtualChassisOperHelloIntervalConsis.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisOperHelloIntervalConsis.setStatus(_A)
_VirtualChassisConfigHelloIntervalConsis_Type=VirtualChassisConsistency
_VirtualChassisConfigHelloIntervalConsis_Object=MibTableColumn
virtualChassisConfigHelloIntervalConsis=_VirtualChassisConfigHelloIntervalConsis_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,25),_VirtualChassisConfigHelloIntervalConsis_Type())
virtualChassisConfigHelloIntervalConsis.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisConfigHelloIntervalConsis.setStatus(_J)
_VirtualChassisChassisTypeConsis_Type=VirtualChassisConsistency
_VirtualChassisChassisTypeConsis_Object=MibTableColumn
virtualChassisChassisTypeConsis=_VirtualChassisChassisTypeConsis_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,26),_VirtualChassisChassisTypeConsis_Type())
virtualChassisChassisTypeConsis.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisChassisTypeConsis.setStatus(_A)
_VirtualChassisGroupConsis_Type=VirtualChassisConsistency
_VirtualChassisGroupConsis_Object=MibTableColumn
virtualChassisGroupConsis=_VirtualChassisGroupConsis_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,27),_VirtualChassisGroupConsis_Type())
virtualChassisGroupConsis.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisGroupConsis.setStatus(_A)
_VirtualChassisLicenseConsis_Type=VirtualChassisConsistency
_VirtualChassisLicenseConsis_Object=MibTableColumn
virtualChassisLicenseConsis=_VirtualChassisLicenseConsis_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,28),_VirtualChassisLicenseConsis_Type())
virtualChassisLicenseConsis.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisLicenseConsis.setStatus(_A)
_VirtualChassisGlobalConsis_Type=VirtualChassisConsistency
_VirtualChassisGlobalConsis_Object=MibTableColumn
virtualChassisGlobalConsis=_VirtualChassisGlobalConsis_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,29),_VirtualChassisGlobalConsis_Type())
virtualChassisGlobalConsis.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisGlobalConsis.setStatus(_A)
class _VirtualChassisNumOfNeighbor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VirtualChassisNumOfNeighbor_Type.__name__=_E
_VirtualChassisNumOfNeighbor_Object=MibTableColumn
virtualChassisNumOfNeighbor=_VirtualChassisNumOfNeighbor_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,30),_VirtualChassisNumOfNeighbor_Type())
virtualChassisNumOfNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisNumOfNeighbor.setStatus(_A)
class _VirtualChassisNumOfDirectNeighbor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VirtualChassisNumOfDirectNeighbor_Type.__name__=_E
_VirtualChassisNumOfDirectNeighbor_Object=MibTableColumn
virtualChassisNumOfDirectNeighbor=_VirtualChassisNumOfDirectNeighbor_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,31),_VirtualChassisNumOfDirectNeighbor_Type())
virtualChassisNumOfDirectNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisNumOfDirectNeighbor.setStatus(_A)
class _VirtualChassisVflMode_Type(VirtualChassisVflMode):defaultValue=1
_VirtualChassisVflMode_Type.__name__=_d
_VirtualChassisVflMode_Object=MibTableColumn
virtualChassisVflMode=_VirtualChassisVflMode_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,2,1,32),_VirtualChassisVflMode_Type())
virtualChassisVflMode.setMaxAccess(_F)
if mibBuilder.loadTexts:virtualChassisVflMode.setStatus(_A)
_VirtualChassisNeighborTable_Object=MibTable
virtualChassisNeighborTable=_VirtualChassisNeighborTable_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,3))
if mibBuilder.loadTexts:virtualChassisNeighborTable.setStatus(_A)
_VirtualChassisNeighborEntry_Object=MibTableRow
virtualChassisNeighborEntry=_VirtualChassisNeighborEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,3,1))
virtualChassisNeighborEntry.setIndexNames((0,_B,_D),(0,_B,_e))
if mibBuilder.loadTexts:virtualChassisNeighborEntry.setStatus(_A)
_VirtualChassisNeighborChasId_Type=VirtualOperChassisId
_VirtualChassisNeighborChasId_Object=MibTableColumn
virtualChassisNeighborChasId=_VirtualChassisNeighborChasId_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,3,1,1),_VirtualChassisNeighborChasId_Type())
virtualChassisNeighborChasId.setMaxAccess(_H)
if mibBuilder.loadTexts:virtualChassisNeighborChasId.setStatus(_A)
class _VirtualChassisNeighborShortestPath_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VirtualChassisNeighborShortestPath_Type.__name__=_I
_VirtualChassisNeighborShortestPath_Object=MibTableColumn
virtualChassisNeighborShortestPath=_VirtualChassisNeighborShortestPath_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,3,1,2),_VirtualChassisNeighborShortestPath_Type())
virtualChassisNeighborShortestPath.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisNeighborShortestPath.setStatus(_A)
_VirtualChassisNeighborIsDirect_Type=TruthValue
_VirtualChassisNeighborIsDirect_Object=MibTableColumn
virtualChassisNeighborIsDirect=_VirtualChassisNeighborIsDirect_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,3,1,3),_VirtualChassisNeighborIsDirect_Type())
virtualChassisNeighborIsDirect.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisNeighborIsDirect.setStatus(_A)
_VirtualChassisChassisResetListTable_Object=MibTable
virtualChassisChassisResetListTable=_VirtualChassisChassisResetListTable_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,4))
if mibBuilder.loadTexts:virtualChassisChassisResetListTable.setStatus(_A)
_VirtualChassisChassisResetListEntry_Object=MibTableRow
virtualChassisChassisResetListEntry=_VirtualChassisChassisResetListEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,4,1))
virtualChassisChassisResetListEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:virtualChassisChassisResetListEntry.setStatus(_A)
class _VirtualChassisChassisResetList_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VirtualChassisChassisResetList_Type.__name__=_I
_VirtualChassisChassisResetList_Object=MibTableColumn
virtualChassisChassisResetList=_VirtualChassisChassisResetList_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,4,1,1),_VirtualChassisChassisResetList_Type())
virtualChassisChassisResetList.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisChassisResetList.setStatus(_A)
_VirtualChassisSlotResetStatusTable_Object=MibTable
virtualChassisSlotResetStatusTable=_VirtualChassisSlotResetStatusTable_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,5))
if mibBuilder.loadTexts:virtualChassisSlotResetStatusTable.setStatus(_A)
_VirtualChassisSlotResetStatusEntry_Object=MibTableRow
virtualChassisSlotResetStatusEntry=_VirtualChassisSlotResetStatusEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,5,1))
virtualChassisSlotResetStatusEntry.setIndexNames((0,_B,_D),(0,_B,_f))
if mibBuilder.loadTexts:virtualChassisSlotResetStatusEntry.setStatus(_A)
_VirtualChassisSlotNum_Type=VirtualChassisNiSlot
_VirtualChassisSlotNum_Object=MibTableColumn
virtualChassisSlotNum=_VirtualChassisSlotNum_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,5,1,1),_VirtualChassisSlotNum_Type())
virtualChassisSlotNum.setMaxAccess(_H)
if mibBuilder.loadTexts:virtualChassisSlotNum.setStatus(_A)
_VirtualChassisSlotResetStatus_Type=VirtualChassisSlotResetStatus
_VirtualChassisSlotResetStatus_Object=MibTableColumn
virtualChassisSlotResetStatus=_VirtualChassisSlotResetStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,5,1,2),_VirtualChassisSlotResetStatus_Type())
virtualChassisSlotResetStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisSlotResetStatus.setStatus(_A)
_VirtualChassisVflTable_Object=MibTable
virtualChassisVflTable=_VirtualChassisVflTable_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,6))
if mibBuilder.loadTexts:virtualChassisVflTable.setStatus(_A)
_VirtualChassisVflEntry_Object=MibTableRow
virtualChassisVflEntry=_VirtualChassisVflEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,6,1))
virtualChassisVflEntry.setIndexNames((0,_B,_D),(0,_B,_G))
if mibBuilder.loadTexts:virtualChassisVflEntry.setStatus(_A)
_VirtualChassisVflId_Type=VirtualChassisVflId
_VirtualChassisVflId_Object=MibTableColumn
virtualChassisVflId=_VirtualChassisVflId_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,6,1,1),_VirtualChassisVflId_Type())
virtualChassisVflId.setMaxAccess(_H)
if mibBuilder.loadTexts:virtualChassisVflId.setStatus(_A)
class _VirtualChassisVflDefaultVlan_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VirtualChassisVflDefaultVlan_Type.__name__=_E
_VirtualChassisVflDefaultVlan_Object=MibTableColumn
virtualChassisVflDefaultVlan=_VirtualChassisVflDefaultVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,6,1,2),_VirtualChassisVflDefaultVlan_Type())
virtualChassisVflDefaultVlan.setMaxAccess(_K)
if mibBuilder.loadTexts:virtualChassisVflDefaultVlan.setStatus(_J)
class _VirtualChassisVflOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),('up',1),(_P,2)))
_VirtualChassisVflOperStatus_Type.__name__=_E
_VirtualChassisVflOperStatus_Object=MibTableColumn
virtualChassisVflOperStatus=_VirtualChassisVflOperStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,6,1,3),_VirtualChassisVflOperStatus_Type())
virtualChassisVflOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisVflOperStatus.setStatus(_A)
_VirtualChassisVflPrimaryPort_Type=InterfaceIndexOrZero
_VirtualChassisVflPrimaryPort_Object=MibTableColumn
virtualChassisVflPrimaryPort=_VirtualChassisVflPrimaryPort_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,6,1,4),_VirtualChassisVflPrimaryPort_Type())
virtualChassisVflPrimaryPort.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisVflPrimaryPort.setStatus(_A)
class _VirtualChassisVflActivePortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_VirtualChassisVflActivePortNum_Type.__name__=_E
_VirtualChassisVflActivePortNum_Object=MibTableColumn
virtualChassisVflActivePortNum=_VirtualChassisVflActivePortNum_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,6,1,5),_VirtualChassisVflActivePortNum_Type())
virtualChassisVflActivePortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisVflActivePortNum.setStatus(_A)
class _VirtualChassisVflConfigPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_VirtualChassisVflConfigPortNum_Type.__name__=_E
_VirtualChassisVflConfigPortNum_Object=MibTableColumn
virtualChassisVflConfigPortNum=_VirtualChassisVflConfigPortNum_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,6,1,6),_VirtualChassisVflConfigPortNum_Type())
virtualChassisVflConfigPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisVflConfigPortNum.setStatus(_A)
_VirtualChassisVflRowStatus_Type=RowStatus
_VirtualChassisVflRowStatus_Object=MibTableColumn
virtualChassisVflRowStatus=_VirtualChassisVflRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,6,1,7),_VirtualChassisVflRowStatus_Type())
virtualChassisVflRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:virtualChassisVflRowStatus.setStatus(_A)
_VirtualChassisVflDirectNeighborChasId_Type=VirtualOperChassisId
_VirtualChassisVflDirectNeighborChasId_Object=MibTableColumn
virtualChassisVflDirectNeighborChasId=_VirtualChassisVflDirectNeighborChasId_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,6,1,8),_VirtualChassisVflDirectNeighborChasId_Type())
virtualChassisVflDirectNeighborChasId.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisVflDirectNeighborChasId.setStatus(_A)
_VirtualChassisVflSpeedType_Type=VirtualChassisVflSpeedType
_VirtualChassisVflSpeedType_Object=MibTableColumn
virtualChassisVflSpeedType=_VirtualChassisVflSpeedType_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,6,1,9),_VirtualChassisVflSpeedType_Type())
virtualChassisVflSpeedType.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisVflSpeedType.setStatus(_A)
_VirtualChassisVflMemberPortTable_Object=MibTable
virtualChassisVflMemberPortTable=_VirtualChassisVflMemberPortTable_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,7))
if mibBuilder.loadTexts:virtualChassisVflMemberPortTable.setStatus(_A)
_VirtualChassisVflMemberPortEntry_Object=MibTableRow
virtualChassisVflMemberPortEntry=_VirtualChassisVflMemberPortEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,7,1))
virtualChassisVflMemberPortEntry.setIndexNames((0,_B,_D),(0,_B,_G),(0,_B,_L))
if mibBuilder.loadTexts:virtualChassisVflMemberPortEntry.setStatus(_A)
_VirtualChassisVflMemberPortIfindex_Type=InterfaceIndex
_VirtualChassisVflMemberPortIfindex_Object=MibTableColumn
virtualChassisVflMemberPortIfindex=_VirtualChassisVflMemberPortIfindex_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,7,1,1),_VirtualChassisVflMemberPortIfindex_Type())
virtualChassisVflMemberPortIfindex.setMaxAccess(_H)
if mibBuilder.loadTexts:virtualChassisVflMemberPortIfindex.setStatus(_A)
_VirtualChassisVflMemberPortIsPrimay_Type=TruthValue
_VirtualChassisVflMemberPortIsPrimay_Object=MibTableColumn
virtualChassisVflMemberPortIsPrimay=_VirtualChassisVflMemberPortIsPrimay_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,7,1,2),_VirtualChassisVflMemberPortIsPrimay_Type())
virtualChassisVflMemberPortIsPrimay.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisVflMemberPortIsPrimay.setStatus(_A)
class _VirtualChassisVflMemberPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),('up',1),(_P,2)))
_VirtualChassisVflMemberPortOperStatus_Type.__name__=_E
_VirtualChassisVflMemberPortOperStatus_Object=MibTableColumn
virtualChassisVflMemberPortOperStatus=_VirtualChassisVflMemberPortOperStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,7,1,3),_VirtualChassisVflMemberPortOperStatus_Type())
virtualChassisVflMemberPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisVflMemberPortOperStatus.setStatus(_A)
_VirtualChassisVflMemberPortRowStatus_Type=RowStatus
_VirtualChassisVflMemberPortRowStatus_Object=MibTableColumn
virtualChassisVflMemberPortRowStatus=_VirtualChassisVflMemberPortRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,7,1,4),_VirtualChassisVflMemberPortRowStatus_Type())
virtualChassisVflMemberPortRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:virtualChassisVflMemberPortRowStatus.setStatus(_A)
_VirtualChassisTrapInfo_ObjectIdentity=ObjectIdentity
virtualChassisTrapInfo=_VirtualChassisTrapInfo_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,8))
class _VirtualChassisDiagnostic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('duplexMode',1),('speed',2)))
_VirtualChassisDiagnostic_Type.__name__=_E
_VirtualChassisDiagnostic_Object=MibScalar
virtualChassisDiagnostic=_VirtualChassisDiagnostic_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,8,1),_VirtualChassisDiagnostic_Type())
virtualChassisDiagnostic.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisDiagnostic.setStatus(_A)
class _VirtualChassisUpgradeCompleteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('success',1),('failure',2)))
_VirtualChassisUpgradeCompleteStatus_Type.__name__=_E
_VirtualChassisUpgradeCompleteStatus_Object=MibScalar
virtualChassisUpgradeCompleteStatus=_VirtualChassisUpgradeCompleteStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,8,2),_VirtualChassisUpgradeCompleteStatus_Type())
virtualChassisUpgradeCompleteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisUpgradeCompleteStatus.setStatus(_A)
_VirtualChassisAutoVflPortTable_Object=MibTable
virtualChassisAutoVflPortTable=_VirtualChassisAutoVflPortTable_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,9))
if mibBuilder.loadTexts:virtualChassisAutoVflPortTable.setStatus(_A)
_VirtualChassisAutoVflPortEntry_Object=MibTableRow
virtualChassisAutoVflPortEntry=_VirtualChassisAutoVflPortEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,9,1))
virtualChassisAutoVflPortEntry.setIndexNames((0,_B,_g))
if mibBuilder.loadTexts:virtualChassisAutoVflPortEntry.setStatus(_A)
_VirtualChassisAutoVflPortIfindex_Type=InterfaceIndex
_VirtualChassisAutoVflPortIfindex_Object=MibTableColumn
virtualChassisAutoVflPortIfindex=_VirtualChassisAutoVflPortIfindex_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,9,1,1),_VirtualChassisAutoVflPortIfindex_Type())
virtualChassisAutoVflPortIfindex.setMaxAccess(_H)
if mibBuilder.loadTexts:virtualChassisAutoVflPortIfindex.setStatus(_A)
_VirtualChassisAutoVflIfindex_Type=InterfaceIndexOrZero
_VirtualChassisAutoVflIfindex_Object=MibTableColumn
virtualChassisAutoVflIfindex=_VirtualChassisAutoVflIfindex_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,9,1,2),_VirtualChassisAutoVflIfindex_Type())
virtualChassisAutoVflIfindex.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisAutoVflIfindex.setStatus(_A)
class _VirtualChassisAutoVflPortMemberStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_P,2),(_N,3)))
_VirtualChassisAutoVflPortMemberStatus_Type.__name__=_E
_VirtualChassisAutoVflPortMemberStatus_Object=MibTableColumn
virtualChassisAutoVflPortMemberStatus=_VirtualChassisAutoVflPortMemberStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,9,1,3),_VirtualChassisAutoVflPortMemberStatus_Type())
virtualChassisAutoVflPortMemberStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualChassisAutoVflPortMemberStatus.setStatus(_A)
_VirtualChassisAutoVflPortRowStatus_Type=RowStatus
_VirtualChassisAutoVflPortRowStatus_Object=MibTableColumn
virtualChassisAutoVflPortRowStatus=_VirtualChassisAutoVflPortRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,1,9,1,4),_VirtualChassisAutoVflPortRowStatus_Type())
virtualChassisAutoVflPortRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:virtualChassisAutoVflPortRowStatus.setStatus(_A)
_AlcatelIND1VirtualChassisMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1VirtualChassisMIBConformance=_AlcatelIND1VirtualChassisMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,69,1,2))
if mibBuilder.loadTexts:alcatelIND1VirtualChassisMIBConformance.setStatus(_A)
_AlcatelIND1VirtualChassisMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1VirtualChassisMIBGroups=_AlcatelIND1VirtualChassisMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,69,1,2,1))
if mibBuilder.loadTexts:alcatelIND1VirtualChassisMIBGroups.setStatus(_A)
_AlcatelIND1VirtualChassisMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1VirtualChassisMIBCompliances=_AlcatelIND1VirtualChassisMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,69,1,2,2))
if mibBuilder.loadTexts:alcatelIND1VirtualChassisMIBCompliances.setStatus(_A)
_AlcatelIND1VirtualChassisMIBVCSP_ObjectIdentity=ObjectIdentity
alcatelIND1VirtualChassisMIBVCSP=_AlcatelIND1VirtualChassisMIBVCSP_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,69,1,3))
if mibBuilder.loadTexts:alcatelIND1VirtualChassisMIBVCSP.setStatus(_A)
virtualChassisLocalInfoGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,69,1,2,1,1))
virtualChassisLocalInfoGroup.setObjects((_B,_h))
if mibBuilder.loadTexts:virtualChassisLocalInfoGroup.setStatus(_A)
virtualChassisGlobalGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,69,1,2,1,2))
virtualChassisGlobalGroup.setObjects(*((_B,_i),(_B,_Q),(_B,_j),(_B,_R),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:virtualChassisGlobalGroup.setStatus(_A)
virtualChassisNeighborGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,69,1,2,1,3))
virtualChassisNeighborGroup.setObjects(*((_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:virtualChassisNeighborGroup.setStatus(_A)
virtualChassisChassisResetListGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,69,1,2,1,4))
virtualChassisChassisResetListGroup.setObjects((_B,_AD))
if mibBuilder.loadTexts:virtualChassisChassisResetListGroup.setStatus(_A)
virtualChassisSlotRestStatusGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,69,1,2,1,5))
virtualChassisSlotRestStatusGroup.setObjects((_B,_AE))
if mibBuilder.loadTexts:virtualChassisSlotRestStatusGroup.setStatus(_A)
virtualChassisVflGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,69,1,2,1,6))
virtualChassisVflGroup.setObjects(*((_B,_AF),(_B,_S),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_T)))
if mibBuilder.loadTexts:virtualChassisVflGroup.setStatus(_A)
virtualChassisVflMemberPortGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,69,1,2,1,7))
virtualChassisVflMemberPortGroup.setObjects(*((_B,_AL),(_B,_U),(_B,_AM)))
if mibBuilder.loadTexts:virtualChassisVflMemberPortGroup.setStatus(_A)
virtualChassisTrapInfoGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,69,1,2,1,8))
virtualChassisTrapInfoGroup.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:virtualChassisTrapInfoGroup.setStatus(_A)
virtualChassisAutoVflPortGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,69,1,2,1,10))
virtualChassisAutoVflPortGroup.setObjects(*((_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:virtualChassisAutoVflPortGroup.setStatus(_A)
virtualChassisStatusChange=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,69,1,0,1))
virtualChassisStatusChange.setObjects(*((_B,_D),(_B,_R)))
if mibBuilder.loadTexts:virtualChassisStatusChange.setStatus(_A)
virtualChassisRoleChange=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,69,1,0,2))
virtualChassisRoleChange.setObjects(*((_B,_D),(_B,_Q)))
if mibBuilder.loadTexts:virtualChassisRoleChange.setStatus(_A)
virtualChassisVflStatusChange=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,69,1,0,3))
virtualChassisVflStatusChange.setObjects(*((_B,_D),(_B,_G),(_B,_S)))
if mibBuilder.loadTexts:virtualChassisVflStatusChange.setStatus(_A)
virtualChassisVflMemberPortStatusChange=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,69,1,0,4))
virtualChassisVflMemberPortStatusChange.setObjects(*((_B,_D),(_B,_G),(_B,_L),(_B,_U)))
if mibBuilder.loadTexts:virtualChassisVflMemberPortStatusChange.setStatus(_J)
virtualChassisVflMemberPortJoinFailure=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,69,1,0,5))
virtualChassisVflMemberPortJoinFailure.setObjects(*((_B,_D),(_B,_G),(_B,_L),(_B,_V)))
if mibBuilder.loadTexts:virtualChassisVflMemberPortJoinFailure.setStatus(_A)
virtualChassisUpgradeComplete=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,69,1,0,6))
virtualChassisUpgradeComplete.setObjects((_B,_W))
if mibBuilder.loadTexts:virtualChassisUpgradeComplete.setStatus(_A)
virtualChassisVflSpeedTypeChange=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,69,1,0,7))
virtualChassisVflSpeedTypeChange.setObjects(*((_B,_D),(_B,_G),(_B,_T)))
if mibBuilder.loadTexts:virtualChassisVflSpeedTypeChange.setStatus(_A)
virtualChassisTrapOBJGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,69,1,2,1,9))
virtualChassisTrapOBJGroup.setObjects(*((_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:virtualChassisTrapOBJGroup.setStatus(_A)
alcatelIND1VirtualChassisMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,69,1,2,2,1))
alcatelIND1VirtualChassisMIBCompliance.setObjects(*((_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad)))
if mibBuilder.loadTexts:alcatelIND1VirtualChassisMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VirtualOperChassisId':VirtualOperChassisId,_Y:VirtualConfigChassisId,_O:VirtualChassisHelloInterval,_c:VirtualChassisControlVlan,'VirtualChassisCmmSlot':VirtualChassisCmmSlot,'VirtualChassisNiSlot':VirtualChassisNiSlot,'VirtualChassisVflId':VirtualChassisVflId,'VirtualChassisConsistency':VirtualChassisConsistency,'VirtualChassisRole':VirtualChassisRole,'VirtualChassisStatus':VirtualChassisStatus,_a:VirtualChassisGroup,_Z:VirtualChassisPriority,'VirtualChassisSlotResetStatus':VirtualChassisSlotResetStatus,'VirtualChassisType':VirtualChassisType,'VirtualChassisVflSpeedType':VirtualChassisVflSpeedType,_d:VirtualChassisVflMode,'alcatelIND1VirtualChassisMIB':alcatelIND1VirtualChassisMIB,'alcatelIND1VirtualChassisMIBNotifications':alcatelIND1VirtualChassisMIBNotifications,_AQ:virtualChassisStatusChange,_AR:virtualChassisRoleChange,_AS:virtualChassisVflStatusChange,_AT:virtualChassisVflMemberPortStatusChange,_AU:virtualChassisVflMemberPortJoinFailure,_AV:virtualChassisUpgradeComplete,_AW:virtualChassisVflSpeedTypeChange,'alcatelIND1VirtualChassisMIBObjects':alcatelIND1VirtualChassisMIBObjects,'virtualChassisLocalInfo':virtualChassisLocalInfo,_h:virtualChassisLocalInfoChasId,'virtualChassisGlobalTable':virtualChassisGlobalTable,'virtualChassisGlobalEntry':virtualChassisGlobalEntry,_D:virtualChassisOperChasId,_i:virtualChassisConfigChassisId,_Q:virtualChassisRole,_j:virtualChassisPreviousRole,_R:virtualChassisStatus,_k:virtualChassisOperPriority,_l:virtualChassisConfigPriority,_m:virtualChassisGroup,_n:virtualChassisMac,_o:virtualChassisUpTime,_p:virtualChassisDesigNI,_q:virtualChassisPriCmm,_r:virtualChassisSecCmm,_s:virtualChassisOperHelloInterval,_t:virtualChassisOperControlVlan,_u:virtualChassisConfigHelloInterval,_v:virtualChassisConfigControlVlan,_w:virtualChassisType,_x:virtualChassisLicense,_y:virtualChassisOperChasIdConsis,_z:virtualChassisConfigChasIdConsis,_A0:virtualChassisOperControlVlanConsis,_A1:virtualChassisConfigControlVlanConsis,_A2:virtualChassisOperHelloIntervalConsis,_A3:virtualChassisConfigHelloIntervalConsis,_A4:virtualChassisChassisTypeConsis,_A5:virtualChassisGroupConsis,_A6:virtualChassisLicenseConsis,_A7:virtualChassisGlobalConsis,_A8:virtualChassisNumOfNeighbor,_A9:virtualChassisNumOfDirectNeighbor,_AA:virtualChassisVflMode,'virtualChassisNeighborTable':virtualChassisNeighborTable,'virtualChassisNeighborEntry':virtualChassisNeighborEntry,_e:virtualChassisNeighborChasId,_AB:virtualChassisNeighborShortestPath,_AC:virtualChassisNeighborIsDirect,'virtualChassisChassisResetListTable':virtualChassisChassisResetListTable,'virtualChassisChassisResetListEntry':virtualChassisChassisResetListEntry,_AD:virtualChassisChassisResetList,'virtualChassisSlotResetStatusTable':virtualChassisSlotResetStatusTable,'virtualChassisSlotResetStatusEntry':virtualChassisSlotResetStatusEntry,_f:virtualChassisSlotNum,_AE:virtualChassisSlotResetStatus,'virtualChassisVflTable':virtualChassisVflTable,'virtualChassisVflEntry':virtualChassisVflEntry,_G:virtualChassisVflId,_AF:virtualChassisVflDefaultVlan,_S:virtualChassisVflOperStatus,_AG:virtualChassisVflPrimaryPort,_AH:virtualChassisVflActivePortNum,_AI:virtualChassisVflConfigPortNum,_AJ:virtualChassisVflRowStatus,_AK:virtualChassisVflDirectNeighborChasId,_T:virtualChassisVflSpeedType,'virtualChassisVflMemberPortTable':virtualChassisVflMemberPortTable,'virtualChassisVflMemberPortEntry':virtualChassisVflMemberPortEntry,_L:virtualChassisVflMemberPortIfindex,_AL:virtualChassisVflMemberPortIsPrimay,_U:virtualChassisVflMemberPortOperStatus,_AM:virtualChassisVflMemberPortRowStatus,'virtualChassisTrapInfo':virtualChassisTrapInfo,_V:virtualChassisDiagnostic,_W:virtualChassisUpgradeCompleteStatus,'virtualChassisAutoVflPortTable':virtualChassisAutoVflPortTable,'virtualChassisAutoVflPortEntry':virtualChassisAutoVflPortEntry,_g:virtualChassisAutoVflPortIfindex,_AN:virtualChassisAutoVflIfindex,_AO:virtualChassisAutoVflPortMemberStatus,_AP:virtualChassisAutoVflPortRowStatus,'alcatelIND1VirtualChassisMIBConformance':alcatelIND1VirtualChassisMIBConformance,'alcatelIND1VirtualChassisMIBGroups':alcatelIND1VirtualChassisMIBGroups,_AX:virtualChassisLocalInfoGroup,_AY:virtualChassisGlobalGroup,_AZ:virtualChassisNeighborGroup,_Aa:virtualChassisChassisResetListGroup,_Ab:virtualChassisSlotRestStatusGroup,_Ac:virtualChassisVflGroup,_Ad:virtualChassisVflMemberPortGroup,'virtualChassisTrapInfoGroup':virtualChassisTrapInfoGroup,'virtualChassisTrapOBJGroup':virtualChassisTrapOBJGroup,'virtualChassisAutoVflPortGroup':virtualChassisAutoVflPortGroup,'alcatelIND1VirtualChassisMIBCompliances':alcatelIND1VirtualChassisMIBCompliances,'alcatelIND1VirtualChassisMIBCompliance':alcatelIND1VirtualChassisMIBCompliance,'alcatelIND1VirtualChassisMIBVCSP':alcatelIND1VirtualChassisMIBVCSP})