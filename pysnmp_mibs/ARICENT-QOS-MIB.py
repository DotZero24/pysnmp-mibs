_w='fsQosHwCpuQId'
_v='fsQoSCoSQId'
_u='SchedulerPriority'
_t='fsQoSHierarchyLevel'
_s='fsQoSQId'
_r='fsQoSQMapRegenPriority'
_q='fsQoSQMapRegenPriType'
_p='fsQoSQMapCLASS'
_o='fsQoSShapeTemplateId'
_n='fsQoSRandomDetectCfgDP'
_m='setFlagConfInnerVlanDE'
_l='setFlagConfInnerVlanPrio'
_k='fsQoSPolicyMapId'
_j='MeterColorMode'
_i='fsQoSPcpPacketType'
_h='fsQoSVlanMapID'
_g='fsQoSClassToPriorityCLASS'
_f='fsQoSClassMapId'
_e='vlanDEI'
_d='fsQoSPriorityMapID'
_c='TruthValue'
_b='fsQoSSchedulerId'
_a='EnableStatus'
_Z='fsQoSQTemplateId'
_Y='fsQoSMeterId'
_X='yellow'
_W='green'
_V='mplsExp'
_U='ipDscp'
_T='ipTos'
_S='vlanPri'
_R='enabled'
_Q='disabled'
_P='Bytes'
_O='red'
_N='dot1P'
_M='none'
_L='Bits'
_K='DisplayString'
_J='ifIndex'
_I='IF-MIB'
_H='read-create'
_G='not-accessible'
_F='read-only'
_E='ARICENT-QOS-MIB'
_D='Integer32'
_C='Unsigned32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_L,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention',_c)
fsQoSMib=ModuleIdentity((1,3,6,1,4,1,29601,2,6))
if mibBuilder.loadTexts:fsQoSMib.setRevisions(('2012-09-05 00:00',))
class Dscp(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
class MeterColorMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('colorAware',1),('colorBlind',2)))
class MeterType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('simpleTokenBucket',1),('avgRate',2),('srTCM',3),('trTCM',4),('tswTCM',5),('mefDecoupledMeter',6),('mefCoupledMeter',7)))
class EnableStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
class SchedulerPriority(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
class IndexInteger(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSMIBObjects_ObjectIdentity=ObjectIdentity
fsQoSMIBObjects=_FsQoSMIBObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,6,1))
_FsQoSSystem_ObjectIdentity=ObjectIdentity
fsQoSSystem=_FsQoSSystem_ObjectIdentity((1,3,6,1,4,1,29601,2,6,1,1))
class _FsQoSSystemControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('shutdown',0),('start',1)))
_FsQoSSystemControl_Type.__name__=_D
_FsQoSSystemControl_Object=MibScalar
fsQoSSystemControl=_FsQoSSystemControl_Object((1,3,6,1,4,1,29601,2,6,1,1,1),_FsQoSSystemControl_Type())
fsQoSSystemControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSSystemControl.setStatus(_A)
class _FsQoSStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_FsQoSStatus_Type.__name__=_D
_FsQoSStatus_Object=MibScalar
fsQoSStatus=_FsQoSStatus_Object((1,3,6,1,4,1,29601,2,6,1,1,2),_FsQoSStatus_Type())
fsQoSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSStatus.setStatus(_A)
class _FsQoSTrcFlag_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsQoSTrcFlag_Type.__name__=_C
_FsQoSTrcFlag_Object=MibScalar
fsQoSTrcFlag=_FsQoSTrcFlag_Object((1,3,6,1,4,1,29601,2,6,1,1,3),_FsQoSTrcFlag_Type())
fsQoSTrcFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSTrcFlag.setStatus(_A)
class _FsQoSRateUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bps',1),('kbps',2),('mbps',3),('gbps',4)))
_FsQoSRateUnit_Type.__name__=_D
_FsQoSRateUnit_Object=MibScalar
fsQoSRateUnit=_FsQoSRateUnit_Object((1,3,6,1,4,1,29601,2,6,1,1,4),_FsQoSRateUnit_Type())
fsQoSRateUnit.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQoSRateUnit.setStatus(_A)
_FsQoSRateGranularity_Type=Unsigned32
_FsQoSRateGranularity_Object=MibScalar
fsQoSRateGranularity=_FsQoSRateGranularity_Object((1,3,6,1,4,1,29601,2,6,1,1,5),_FsQoSRateGranularity_Type())
fsQoSRateGranularity.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQoSRateGranularity.setStatus(_A)
class _FsQoSVlanQueueingStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_FsQoSVlanQueueingStatus_Type.__name__=_D
_FsQoSVlanQueueingStatus_Object=MibScalar
fsQoSVlanQueueingStatus=_FsQoSVlanQueueingStatus_Object((1,3,6,1,4,1,29601,2,6,1,1,6),_FsQoSVlanQueueingStatus_Type())
fsQoSVlanQueueingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSVlanQueueingStatus.setStatus(_A)
_FsQoSClass_ObjectIdentity=ObjectIdentity
fsQoSClass=_FsQoSClass_ObjectIdentity((1,3,6,1,4,1,29601,2,6,1,2))
_FsQoSPriorityMapTable_Object=MibTable
fsQoSPriorityMapTable=_FsQoSPriorityMapTable_Object((1,3,6,1,4,1,29601,2,6,1,2,1))
if mibBuilder.loadTexts:fsQoSPriorityMapTable.setStatus(_A)
_FsQoSPriorityMapEntry_Object=MibTableRow
fsQoSPriorityMapEntry=_FsQoSPriorityMapEntry_Object((1,3,6,1,4,1,29601,2,6,1,2,1,1))
fsQoSPriorityMapEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:fsQoSPriorityMapEntry.setStatus(_A)
_FsQoSPriorityMapID_Type=IndexInteger
_FsQoSPriorityMapID_Object=MibTableColumn
fsQoSPriorityMapID=_FsQoSPriorityMapID_Object((1,3,6,1,4,1,29601,2,6,1,2,1,1,1),_FsQoSPriorityMapID_Type())
fsQoSPriorityMapID.setMaxAccess(_G)
if mibBuilder.loadTexts:fsQoSPriorityMapID.setStatus(_A)
class _FsQoSPriorityMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_FsQoSPriorityMapName_Type.__name__=_K
_FsQoSPriorityMapName_Object=MibTableColumn
fsQoSPriorityMapName=_FsQoSPriorityMapName_Object((1,3,6,1,4,1,29601,2,6,1,2,1,1,2),_FsQoSPriorityMapName_Type())
fsQoSPriorityMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPriorityMapName.setStatus(_A)
class _FsQoSPriorityMapIfIndex_Type(Unsigned32):defaultValue=0
_FsQoSPriorityMapIfIndex_Type.__name__=_C
_FsQoSPriorityMapIfIndex_Object=MibTableColumn
fsQoSPriorityMapIfIndex=_FsQoSPriorityMapIfIndex_Object((1,3,6,1,4,1,29601,2,6,1,2,1,1,3),_FsQoSPriorityMapIfIndex_Type())
fsQoSPriorityMapIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPriorityMapIfIndex.setStatus(_A)
class _FsQoSPriorityMapVlanId_Type(Unsigned32):defaultValue=0
_FsQoSPriorityMapVlanId_Type.__name__=_C
_FsQoSPriorityMapVlanId_Object=MibTableColumn
fsQoSPriorityMapVlanId=_FsQoSPriorityMapVlanId_Object((1,3,6,1,4,1,29601,2,6,1,2,1,1,4),_FsQoSPriorityMapVlanId_Type())
fsQoSPriorityMapVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPriorityMapVlanId.setStatus(_A)
class _FsQoSPriorityMapInPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_FsQoSPriorityMapInPriority_Type.__name__=_D
_FsQoSPriorityMapInPriority_Object=MibTableColumn
fsQoSPriorityMapInPriority=_FsQoSPriorityMapInPriority_Object((1,3,6,1,4,1,29601,2,6,1,2,1,1,5),_FsQoSPriorityMapInPriority_Type())
fsQoSPriorityMapInPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPriorityMapInPriority.setStatus(_A)
class _FsQoSPriorityMapInPriType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_S,0),(_T,1),(_U,2),(_V,3),(_e,4),(_N,5)))
_FsQoSPriorityMapInPriType_Type.__name__=_D
_FsQoSPriorityMapInPriType_Object=MibTableColumn
fsQoSPriorityMapInPriType=_FsQoSPriorityMapInPriType_Object((1,3,6,1,4,1,29601,2,6,1,2,1,1,6),_FsQoSPriorityMapInPriType_Type())
fsQoSPriorityMapInPriType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPriorityMapInPriType.setStatus(_A)
class _FsQoSPriorityMapRegenPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_FsQoSPriorityMapRegenPriority_Type.__name__=_C
_FsQoSPriorityMapRegenPriority_Object=MibTableColumn
fsQoSPriorityMapRegenPriority=_FsQoSPriorityMapRegenPriority_Object((1,3,6,1,4,1,29601,2,6,1,2,1,1,7),_FsQoSPriorityMapRegenPriority_Type())
fsQoSPriorityMapRegenPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPriorityMapRegenPriority.setStatus(_A)
class _FsQoSPriorityMapRegenInnerPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_FsQoSPriorityMapRegenInnerPriority_Type.__name__=_C
_FsQoSPriorityMapRegenInnerPriority_Object=MibTableColumn
fsQoSPriorityMapRegenInnerPriority=_FsQoSPriorityMapRegenInnerPriority_Object((1,3,6,1,4,1,29601,2,6,1,2,1,1,8),_FsQoSPriorityMapRegenInnerPriority_Type())
fsQoSPriorityMapRegenInnerPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPriorityMapRegenInnerPriority.setStatus(_A)
class _FsQoSPriorityMapConfigStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sysdefault',1),('management',2)))
_FsQoSPriorityMapConfigStatus_Type.__name__=_D
_FsQoSPriorityMapConfigStatus_Object=MibTableColumn
fsQoSPriorityMapConfigStatus=_FsQoSPriorityMapConfigStatus_Object((1,3,6,1,4,1,29601,2,6,1,2,1,1,9),_FsQoSPriorityMapConfigStatus_Type())
fsQoSPriorityMapConfigStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQoSPriorityMapConfigStatus.setStatus(_A)
_FsQoSPriorityMapStatus_Type=RowStatus
_FsQoSPriorityMapStatus_Object=MibTableColumn
fsQoSPriorityMapStatus=_FsQoSPriorityMapStatus_Object((1,3,6,1,4,1,29601,2,6,1,2,1,1,10),_FsQoSPriorityMapStatus_Type())
fsQoSPriorityMapStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsQoSPriorityMapStatus.setStatus(_A)
class _FsQoSPriorityMapInDEI_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_FsQoSPriorityMapInDEI_Type.__name__=_D
_FsQoSPriorityMapInDEI_Object=MibTableColumn
fsQoSPriorityMapInDEI=_FsQoSPriorityMapInDEI_Object((1,3,6,1,4,1,29601,2,6,1,2,1,1,11),_FsQoSPriorityMapInDEI_Type())
fsQoSPriorityMapInDEI.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPriorityMapInDEI.setStatus(_A)
class _FsQoSPriorityMapRegenColor_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_W,0),(_X,1),(_O,2)))
_FsQoSPriorityMapRegenColor_Type.__name__=_D
_FsQoSPriorityMapRegenColor_Object=MibTableColumn
fsQoSPriorityMapRegenColor=_FsQoSPriorityMapRegenColor_Object((1,3,6,1,4,1,29601,2,6,1,2,1,1,12),_FsQoSPriorityMapRegenColor_Type())
fsQoSPriorityMapRegenColor.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPriorityMapRegenColor.setStatus(_A)
_FsQoSClassMapTable_Object=MibTable
fsQoSClassMapTable=_FsQoSClassMapTable_Object((1,3,6,1,4,1,29601,2,6,1,2,2))
if mibBuilder.loadTexts:fsQoSClassMapTable.setStatus(_A)
_FsQoSClassMapEntry_Object=MibTableRow
fsQoSClassMapEntry=_FsQoSClassMapEntry_Object((1,3,6,1,4,1,29601,2,6,1,2,2,1))
fsQoSClassMapEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:fsQoSClassMapEntry.setStatus(_A)
_FsQoSClassMapId_Type=IndexInteger
_FsQoSClassMapId_Object=MibTableColumn
fsQoSClassMapId=_FsQoSClassMapId_Object((1,3,6,1,4,1,29601,2,6,1,2,2,1,1),_FsQoSClassMapId_Type())
fsQoSClassMapId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsQoSClassMapId.setStatus(_A)
class _FsQoSClassMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_FsQoSClassMapName_Type.__name__=_K
_FsQoSClassMapName_Object=MibTableColumn
fsQoSClassMapName=_FsQoSClassMapName_Object((1,3,6,1,4,1,29601,2,6,1,2,2,1,2),_FsQoSClassMapName_Type())
fsQoSClassMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSClassMapName.setStatus(_A)
class _FsQoSClassMapL2FilterId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSClassMapL2FilterId_Type.__name__=_C
_FsQoSClassMapL2FilterId_Object=MibTableColumn
fsQoSClassMapL2FilterId=_FsQoSClassMapL2FilterId_Object((1,3,6,1,4,1,29601,2,6,1,2,2,1,3),_FsQoSClassMapL2FilterId_Type())
fsQoSClassMapL2FilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSClassMapL2FilterId.setStatus(_A)
class _FsQoSClassMapL3FilterId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSClassMapL3FilterId_Type.__name__=_C
_FsQoSClassMapL3FilterId_Object=MibTableColumn
fsQoSClassMapL3FilterId=_FsQoSClassMapL3FilterId_Object((1,3,6,1,4,1,29601,2,6,1,2,2,1,4),_FsQoSClassMapL3FilterId_Type())
fsQoSClassMapL3FilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSClassMapL3FilterId.setStatus(_A)
class _FsQoSClassMapPriorityMapId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSClassMapPriorityMapId_Type.__name__=_C
_FsQoSClassMapPriorityMapId_Object=MibTableColumn
fsQoSClassMapPriorityMapId=_FsQoSClassMapPriorityMapId_Object((1,3,6,1,4,1,29601,2,6,1,2,2,1,5),_FsQoSClassMapPriorityMapId_Type())
fsQoSClassMapPriorityMapId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSClassMapPriorityMapId.setStatus(_A)
class _FsQoSClassMapCLASS_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSClassMapCLASS_Type.__name__=_C
_FsQoSClassMapCLASS_Object=MibTableColumn
fsQoSClassMapCLASS=_FsQoSClassMapCLASS_Object((1,3,6,1,4,1,29601,2,6,1,2,2,1,6),_FsQoSClassMapCLASS_Type())
fsQoSClassMapCLASS.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSClassMapCLASS.setStatus(_A)
class _FsQoSClassMapClfrId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSClassMapClfrId_Type.__name__=_C
_FsQoSClassMapClfrId_Object=MibTableColumn
fsQoSClassMapClfrId=_FsQoSClassMapClfrId_Object((1,3,6,1,4,1,29601,2,6,1,2,2,1,7),_FsQoSClassMapClfrId_Type())
fsQoSClassMapClfrId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSClassMapClfrId.setStatus(_A)
class _FsQoSClassMapPreColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_M,0),(_W,1),(_X,2),(_O,3)))
_FsQoSClassMapPreColor_Type.__name__=_D
_FsQoSClassMapPreColor_Object=MibTableColumn
fsQoSClassMapPreColor=_FsQoSClassMapPreColor_Object((1,3,6,1,4,1,29601,2,6,1,2,2,1,8),_FsQoSClassMapPreColor_Type())
fsQoSClassMapPreColor.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSClassMapPreColor.setStatus(_A)
class _FsQoSClassMapVlanMapId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSClassMapVlanMapId_Type.__name__=_C
_FsQoSClassMapVlanMapId_Object=MibTableColumn
fsQoSClassMapVlanMapId=_FsQoSClassMapVlanMapId_Object((1,3,6,1,4,1,29601,2,6,1,2,2,1,9),_FsQoSClassMapVlanMapId_Type())
fsQoSClassMapVlanMapId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSClassMapVlanMapId.setStatus(_A)
_FsQoSClassMapStatus_Type=RowStatus
_FsQoSClassMapStatus_Object=MibTableColumn
fsQoSClassMapStatus=_FsQoSClassMapStatus_Object((1,3,6,1,4,1,29601,2,6,1,2,2,1,10),_FsQoSClassMapStatus_Type())
fsQoSClassMapStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsQoSClassMapStatus.setStatus(_A)
_FsQoSClassToPriorityTable_Object=MibTable
fsQoSClassToPriorityTable=_FsQoSClassToPriorityTable_Object((1,3,6,1,4,1,29601,2,6,1,2,3))
if mibBuilder.loadTexts:fsQoSClassToPriorityTable.setStatus(_A)
_FsQoSClassToPriorityEntry_Object=MibTableRow
fsQoSClassToPriorityEntry=_FsQoSClassToPriorityEntry_Object((1,3,6,1,4,1,29601,2,6,1,2,3,1))
fsQoSClassToPriorityEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:fsQoSClassToPriorityEntry.setStatus(_A)
_FsQoSClassToPriorityCLASS_Type=IndexInteger
_FsQoSClassToPriorityCLASS_Object=MibTableColumn
fsQoSClassToPriorityCLASS=_FsQoSClassToPriorityCLASS_Object((1,3,6,1,4,1,29601,2,6,1,2,3,1,1),_FsQoSClassToPriorityCLASS_Type())
fsQoSClassToPriorityCLASS.setMaxAccess(_G)
if mibBuilder.loadTexts:fsQoSClassToPriorityCLASS.setStatus(_A)
class _FsQoSClassToPriorityRegenPri_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsQoSClassToPriorityRegenPri_Type.__name__=_C
_FsQoSClassToPriorityRegenPri_Object=MibTableColumn
fsQoSClassToPriorityRegenPri=_FsQoSClassToPriorityRegenPri_Object((1,3,6,1,4,1,29601,2,6,1,2,3,1,2),_FsQoSClassToPriorityRegenPri_Type())
fsQoSClassToPriorityRegenPri.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSClassToPriorityRegenPri.setStatus(_A)
class _FsQoSClassToPriorityGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_FsQoSClassToPriorityGroupName_Type.__name__=_K
_FsQoSClassToPriorityGroupName_Object=MibTableColumn
fsQoSClassToPriorityGroupName=_FsQoSClassToPriorityGroupName_Object((1,3,6,1,4,1,29601,2,6,1,2,3,1,3),_FsQoSClassToPriorityGroupName_Type())
fsQoSClassToPriorityGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSClassToPriorityGroupName.setStatus(_A)
_FsQoSClassToPriorityStatus_Type=RowStatus
_FsQoSClassToPriorityStatus_Object=MibTableColumn
fsQoSClassToPriorityStatus=_FsQoSClassToPriorityStatus_Object((1,3,6,1,4,1,29601,2,6,1,2,3,1,4),_FsQoSClassToPriorityStatus_Type())
fsQoSClassToPriorityStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsQoSClassToPriorityStatus.setStatus(_A)
_FsQoSVlanMapTable_Object=MibTable
fsQoSVlanMapTable=_FsQoSVlanMapTable_Object((1,3,6,1,4,1,29601,2,6,1,2,4))
if mibBuilder.loadTexts:fsQoSVlanMapTable.setStatus(_A)
_FsQoSVlanMapEntry_Object=MibTableRow
fsQoSVlanMapEntry=_FsQoSVlanMapEntry_Object((1,3,6,1,4,1,29601,2,6,1,2,4,1))
fsQoSVlanMapEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:fsQoSVlanMapEntry.setStatus(_A)
_FsQoSVlanMapID_Type=IndexInteger
_FsQoSVlanMapID_Object=MibTableColumn
fsQoSVlanMapID=_FsQoSVlanMapID_Object((1,3,6,1,4,1,29601,2,6,1,2,4,1,1),_FsQoSVlanMapID_Type())
fsQoSVlanMapID.setMaxAccess(_G)
if mibBuilder.loadTexts:fsQoSVlanMapID.setStatus(_A)
_FsQoSVlanMapIfIndex_Type=Unsigned32
_FsQoSVlanMapIfIndex_Object=MibTableColumn
fsQoSVlanMapIfIndex=_FsQoSVlanMapIfIndex_Object((1,3,6,1,4,1,29601,2,6,1,2,4,1,2),_FsQoSVlanMapIfIndex_Type())
fsQoSVlanMapIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSVlanMapIfIndex.setStatus(_A)
_FsQoSVlanMapVlanId_Type=Unsigned32
_FsQoSVlanMapVlanId_Object=MibTableColumn
fsQoSVlanMapVlanId=_FsQoSVlanMapVlanId_Object((1,3,6,1,4,1,29601,2,6,1,2,4,1,3),_FsQoSVlanMapVlanId_Type())
fsQoSVlanMapVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSVlanMapVlanId.setStatus(_A)
_FsQoSVlanMapStatus_Type=RowStatus
_FsQoSVlanMapStatus_Object=MibTableColumn
fsQoSVlanMapStatus=_FsQoSVlanMapStatus_Object((1,3,6,1,4,1,29601,2,6,1,2,4,1,4),_FsQoSVlanMapStatus_Type())
fsQoSVlanMapStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsQoSVlanMapStatus.setStatus(_A)
_FsQoSPortTable_Object=MibTable
fsQoSPortTable=_FsQoSPortTable_Object((1,3,6,1,4,1,29601,2,6,1,2,5))
if mibBuilder.loadTexts:fsQoSPortTable.setStatus(_A)
_FsQoSPortEntry_Object=MibTableRow
fsQoSPortEntry=_FsQoSPortEntry_Object((1,3,6,1,4,1,29601,2,6,1,2,5,1))
fsQoSPortEntry.setIndexNames((0,_I,_J),(0,_E,_i))
if mibBuilder.loadTexts:fsQoSPortEntry.setStatus(_A)
class _FsQoSPcpPacketType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*((_N,0),('ip',1),('mpls',3)))
_FsQoSPcpPacketType_Type.__name__=_D
_FsQoSPcpPacketType_Object=MibTableColumn
fsQoSPcpPacketType=_FsQoSPcpPacketType_Object((1,3,6,1,4,1,29601,2,6,1,2,5,1,1),_FsQoSPcpPacketType_Type())
fsQoSPcpPacketType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsQoSPcpPacketType.setStatus(_A)
class _FsQoSPcpSelRow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('codePoint8P0D',1),('codePoint7P1D',2),('codePoint6P2D',3),('codePoint5P3D',4)))
_FsQoSPcpSelRow_Type.__name__=_D
_FsQoSPcpSelRow_Object=MibTableColumn
fsQoSPcpSelRow=_FsQoSPcpSelRow_Object((1,3,6,1,4,1,29601,2,6,1,2,5,1,2),_FsQoSPcpSelRow_Type())
fsQoSPcpSelRow.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPcpSelRow.setStatus(_A)
_FsQoSPcpRowStatus_Type=RowStatus
_FsQoSPcpRowStatus_Object=MibTableColumn
fsQoSPcpRowStatus=_FsQoSPcpRowStatus_Object((1,3,6,1,4,1,29601,2,6,1,2,5,1,3),_FsQoSPcpRowStatus_Type())
fsQoSPcpRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsQoSPcpRowStatus.setStatus(_A)
_FsQoSPolicy_ObjectIdentity=ObjectIdentity
fsQoSPolicy=_FsQoSPolicy_ObjectIdentity((1,3,6,1,4,1,29601,2,6,1,3))
_FsQoSMeterTable_Object=MibTable
fsQoSMeterTable=_FsQoSMeterTable_Object((1,3,6,1,4,1,29601,2,6,1,3,1))
if mibBuilder.loadTexts:fsQoSMeterTable.setStatus(_A)
_FsQoSMeterEntry_Object=MibTableRow
fsQoSMeterEntry=_FsQoSMeterEntry_Object((1,3,6,1,4,1,29601,2,6,1,3,1,1))
fsQoSMeterEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:fsQoSMeterEntry.setStatus(_A)
_FsQoSMeterId_Type=IndexInteger
_FsQoSMeterId_Object=MibTableColumn
fsQoSMeterId=_FsQoSMeterId_Object((1,3,6,1,4,1,29601,2,6,1,3,1,1,1),_FsQoSMeterId_Type())
fsQoSMeterId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsQoSMeterId.setStatus(_A)
class _FsQoSMeterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_FsQoSMeterName_Type.__name__=_K
_FsQoSMeterName_Object=MibTableColumn
fsQoSMeterName=_FsQoSMeterName_Object((1,3,6,1,4,1,29601,2,6,1,3,1,1,2),_FsQoSMeterName_Type())
fsQoSMeterName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSMeterName.setStatus(_A)
_FsQoSMeterType_Type=MeterType
_FsQoSMeterType_Object=MibTableColumn
fsQoSMeterType=_FsQoSMeterType_Object((1,3,6,1,4,1,29601,2,6,1,3,1,1,3),_FsQoSMeterType_Type())
fsQoSMeterType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSMeterType.setStatus(_A)
class _FsQoSMeterInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_FsQoSMeterInterval_Type.__name__=_C
_FsQoSMeterInterval_Object=MibTableColumn
fsQoSMeterInterval=_FsQoSMeterInterval_Object((1,3,6,1,4,1,29601,2,6,1,3,1,1,4),_FsQoSMeterInterval_Type())
fsQoSMeterInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSMeterInterval.setStatus(_A)
if mibBuilder.loadTexts:fsQoSMeterInterval.setUnits('microseconds')
class _FsQoSMeterColorMode_Type(MeterColorMode):defaultValue=2
_FsQoSMeterColorMode_Type.__name__=_j
_FsQoSMeterColorMode_Object=MibTableColumn
fsQoSMeterColorMode=_FsQoSMeterColorMode_Object((1,3,6,1,4,1,29601,2,6,1,3,1,1,5),_FsQoSMeterColorMode_Type())
fsQoSMeterColorMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSMeterColorMode.setStatus(_A)
class _FsQoSMeterCIR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSMeterCIR_Type.__name__=_C
_FsQoSMeterCIR_Object=MibTableColumn
fsQoSMeterCIR=_FsQoSMeterCIR_Object((1,3,6,1,4,1,29601,2,6,1,3,1,1,6),_FsQoSMeterCIR_Type())
fsQoSMeterCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSMeterCIR.setStatus(_A)
class _FsQoSMeterCBS_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSMeterCBS_Type.__name__=_C
_FsQoSMeterCBS_Object=MibTableColumn
fsQoSMeterCBS=_FsQoSMeterCBS_Object((1,3,6,1,4,1,29601,2,6,1,3,1,1,7),_FsQoSMeterCBS_Type())
fsQoSMeterCBS.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSMeterCBS.setStatus(_A)
if mibBuilder.loadTexts:fsQoSMeterCBS.setUnits(_P)
class _FsQoSMeterEIR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSMeterEIR_Type.__name__=_C
_FsQoSMeterEIR_Object=MibTableColumn
fsQoSMeterEIR=_FsQoSMeterEIR_Object((1,3,6,1,4,1,29601,2,6,1,3,1,1,8),_FsQoSMeterEIR_Type())
fsQoSMeterEIR.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSMeterEIR.setStatus(_A)
class _FsQoSMeterEBS_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSMeterEBS_Type.__name__=_C
_FsQoSMeterEBS_Object=MibTableColumn
fsQoSMeterEBS=_FsQoSMeterEBS_Object((1,3,6,1,4,1,29601,2,6,1,3,1,1,9),_FsQoSMeterEBS_Type())
fsQoSMeterEBS.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSMeterEBS.setStatus(_A)
if mibBuilder.loadTexts:fsQoSMeterEBS.setUnits(_P)
class _FsQoSMeterNext_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSMeterNext_Type.__name__=_C
_FsQoSMeterNext_Object=MibTableColumn
fsQoSMeterNext=_FsQoSMeterNext_Object((1,3,6,1,4,1,29601,2,6,1,3,1,1,10),_FsQoSMeterNext_Type())
fsQoSMeterNext.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSMeterNext.setStatus(_A)
_FsQoSMeterStatus_Type=RowStatus
_FsQoSMeterStatus_Object=MibTableColumn
fsQoSMeterStatus=_FsQoSMeterStatus_Object((1,3,6,1,4,1,29601,2,6,1,3,1,1,11),_FsQoSMeterStatus_Type())
fsQoSMeterStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsQoSMeterStatus.setStatus(_A)
_FsQoSPolicyMapTable_Object=MibTable
fsQoSPolicyMapTable=_FsQoSPolicyMapTable_Object((1,3,6,1,4,1,29601,2,6,1,3,2))
if mibBuilder.loadTexts:fsQoSPolicyMapTable.setStatus(_A)
_FsQoSPolicyMapEntry_Object=MibTableRow
fsQoSPolicyMapEntry=_FsQoSPolicyMapEntry_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1))
fsQoSPolicyMapEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:fsQoSPolicyMapEntry.setStatus(_A)
_FsQoSPolicyMapId_Type=IndexInteger
_FsQoSPolicyMapId_Object=MibTableColumn
fsQoSPolicyMapId=_FsQoSPolicyMapId_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,1),_FsQoSPolicyMapId_Type())
fsQoSPolicyMapId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsQoSPolicyMapId.setStatus(_A)
class _FsQoSPolicyMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_FsQoSPolicyMapName_Type.__name__=_K
_FsQoSPolicyMapName_Object=MibTableColumn
fsQoSPolicyMapName=_FsQoSPolicyMapName_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,2),_FsQoSPolicyMapName_Type())
fsQoSPolicyMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapName.setStatus(_A)
class _FsQoSPolicyMapIfIndex_Type(Unsigned32):defaultValue=0
_FsQoSPolicyMapIfIndex_Type.__name__=_C
_FsQoSPolicyMapIfIndex_Object=MibTableColumn
fsQoSPolicyMapIfIndex=_FsQoSPolicyMapIfIndex_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,3),_FsQoSPolicyMapIfIndex_Type())
fsQoSPolicyMapIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapIfIndex.setStatus(_A)
class _FsQoSPolicyMapCLASS_Type(Unsigned32):defaultValue=0
_FsQoSPolicyMapCLASS_Type.__name__=_C
_FsQoSPolicyMapCLASS_Object=MibTableColumn
fsQoSPolicyMapCLASS=_FsQoSPolicyMapCLASS_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,4),_FsQoSPolicyMapCLASS_Type())
fsQoSPolicyMapCLASS.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapCLASS.setStatus(_A)
class _FsQoSPolicyMapPHBType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_M,0),(_S,1),(_T,2),(_U,3),(_V,4),(_N,5)))
_FsQoSPolicyMapPHBType_Type.__name__=_D
_FsQoSPolicyMapPHBType_Object=MibTableColumn
fsQoSPolicyMapPHBType=_FsQoSPolicyMapPHBType_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,5),_FsQoSPolicyMapPHBType_Type())
fsQoSPolicyMapPHBType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapPHBType.setStatus(_A)
class _FsQoSPolicyMapDefaultPHB_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_FsQoSPolicyMapDefaultPHB_Type.__name__=_C
_FsQoSPolicyMapDefaultPHB_Object=MibTableColumn
fsQoSPolicyMapDefaultPHB=_FsQoSPolicyMapDefaultPHB_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,6),_FsQoSPolicyMapDefaultPHB_Type())
fsQoSPolicyMapDefaultPHB.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapDefaultPHB.setStatus(_A)
class _FsQoSPolicyMapMeterTableId_Type(Unsigned32):defaultValue=0
_FsQoSPolicyMapMeterTableId_Type.__name__=_C
_FsQoSPolicyMapMeterTableId_Object=MibTableColumn
fsQoSPolicyMapMeterTableId=_FsQoSPolicyMapMeterTableId_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,7),_FsQoSPolicyMapMeterTableId_Type())
fsQoSPolicyMapMeterTableId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapMeterTableId.setStatus(_A)
class _FsQoSPolicyMapFailMeterTableId_Type(Unsigned32):defaultValue=0
_FsQoSPolicyMapFailMeterTableId_Type.__name__=_C
_FsQoSPolicyMapFailMeterTableId_Object=MibTableColumn
fsQoSPolicyMapFailMeterTableId=_FsQoSPolicyMapFailMeterTableId_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,8),_FsQoSPolicyMapFailMeterTableId_Type())
fsQoSPolicyMapFailMeterTableId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapFailMeterTableId.setStatus(_A)
class _FsQoSPolicyMapInProfileConformActionFlag_Type(Bits):namedValues=NamedValues(*((_M,0),('setFlagPort',1),('setFlagConfTos',2),('setFlagConfDscp',3),('setFlagConfVlanPrio',4),('setFlagConfVlanDE',5),(_l,6),('setFlagConfMplsExp',7),(_m,8)))
_FsQoSPolicyMapInProfileConformActionFlag_Type.__name__=_L
_FsQoSPolicyMapInProfileConformActionFlag_Object=MibTableColumn
fsQoSPolicyMapInProfileConformActionFlag=_FsQoSPolicyMapInProfileConformActionFlag_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,9),_FsQoSPolicyMapInProfileConformActionFlag_Type())
fsQoSPolicyMapInProfileConformActionFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapInProfileConformActionFlag.setStatus(_A)
class _FsQoSPolicyMapInProfileConformActionId_Type(Unsigned32):defaultValue=0
_FsQoSPolicyMapInProfileConformActionId_Type.__name__=_C
_FsQoSPolicyMapInProfileConformActionId_Object=MibTableColumn
fsQoSPolicyMapInProfileConformActionId=_FsQoSPolicyMapInProfileConformActionId_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,10),_FsQoSPolicyMapInProfileConformActionId_Type())
fsQoSPolicyMapInProfileConformActionId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapInProfileConformActionId.setStatus(_A)
_FsQoSPolicyMapInProfileActionSetPort_Type=Unsigned32
_FsQoSPolicyMapInProfileActionSetPort_Object=MibTableColumn
fsQoSPolicyMapInProfileActionSetPort=_FsQoSPolicyMapInProfileActionSetPort_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,11),_FsQoSPolicyMapInProfileActionSetPort_Type())
fsQoSPolicyMapInProfileActionSetPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapInProfileActionSetPort.setStatus(_A)
_FsQoSPolicyMapConformActionSetIpTOS_Type=Unsigned32
_FsQoSPolicyMapConformActionSetIpTOS_Object=MibTableColumn
fsQoSPolicyMapConformActionSetIpTOS=_FsQoSPolicyMapConformActionSetIpTOS_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,12),_FsQoSPolicyMapConformActionSetIpTOS_Type())
fsQoSPolicyMapConformActionSetIpTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapConformActionSetIpTOS.setStatus(_A)
_FsQoSPolicyMapConformActionSetDscp_Type=Dscp
_FsQoSPolicyMapConformActionSetDscp_Object=MibTableColumn
fsQoSPolicyMapConformActionSetDscp=_FsQoSPolicyMapConformActionSetDscp_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,13),_FsQoSPolicyMapConformActionSetDscp_Type())
fsQoSPolicyMapConformActionSetDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapConformActionSetDscp.setStatus(_A)
class _FsQoSPolicyMapConformActionSetVlanPrio_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsQoSPolicyMapConformActionSetVlanPrio_Type.__name__=_C
_FsQoSPolicyMapConformActionSetVlanPrio_Object=MibTableColumn
fsQoSPolicyMapConformActionSetVlanPrio=_FsQoSPolicyMapConformActionSetVlanPrio_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,14),_FsQoSPolicyMapConformActionSetVlanPrio_Type())
fsQoSPolicyMapConformActionSetVlanPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapConformActionSetVlanPrio.setStatus(_A)
class _FsQoSPolicyMapConformActionSetVlanDE_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsQoSPolicyMapConformActionSetVlanDE_Type.__name__=_C
_FsQoSPolicyMapConformActionSetVlanDE_Object=MibTableColumn
fsQoSPolicyMapConformActionSetVlanDE=_FsQoSPolicyMapConformActionSetVlanDE_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,15),_FsQoSPolicyMapConformActionSetVlanDE_Type())
fsQoSPolicyMapConformActionSetVlanDE.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapConformActionSetVlanDE.setStatus(_A)
class _FsQoSPolicyMapConformActionSetInnerVlanPrio_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsQoSPolicyMapConformActionSetInnerVlanPrio_Type.__name__=_C
_FsQoSPolicyMapConformActionSetInnerVlanPrio_Object=MibTableColumn
fsQoSPolicyMapConformActionSetInnerVlanPrio=_FsQoSPolicyMapConformActionSetInnerVlanPrio_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,16),_FsQoSPolicyMapConformActionSetInnerVlanPrio_Type())
fsQoSPolicyMapConformActionSetInnerVlanPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapConformActionSetInnerVlanPrio.setStatus(_A)
class _FsQoSPolicyMapConformActionSetMplsExp_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsQoSPolicyMapConformActionSetMplsExp_Type.__name__=_C
_FsQoSPolicyMapConformActionSetMplsExp_Object=MibTableColumn
fsQoSPolicyMapConformActionSetMplsExp=_FsQoSPolicyMapConformActionSetMplsExp_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,17),_FsQoSPolicyMapConformActionSetMplsExp_Type())
fsQoSPolicyMapConformActionSetMplsExp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapConformActionSetMplsExp.setStatus(_A)
_FsQoSPolicyMapConformActionSetNewCLASS_Type=Unsigned32
_FsQoSPolicyMapConformActionSetNewCLASS_Object=MibTableColumn
fsQoSPolicyMapConformActionSetNewCLASS=_FsQoSPolicyMapConformActionSetNewCLASS_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,18),_FsQoSPolicyMapConformActionSetNewCLASS_Type())
fsQoSPolicyMapConformActionSetNewCLASS.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapConformActionSetNewCLASS.setStatus(_A)
class _FsQoSPolicyMapInProfileExceedActionFlag_Type(Bits):namedValues=NamedValues(*(('setFlagExcDrop',0),('setFlagExcTos',1),('setFlagExcDscp',2),('setFlagExcVlanPrio',3),('setFlagExcVlanDE',4),('setFlagExcInnerVlanPrio',5),('setFlagExcMplsExp',6),('setFlagExcInnerVlanDE',7)))
_FsQoSPolicyMapInProfileExceedActionFlag_Type.__name__=_L
_FsQoSPolicyMapInProfileExceedActionFlag_Object=MibTableColumn
fsQoSPolicyMapInProfileExceedActionFlag=_FsQoSPolicyMapInProfileExceedActionFlag_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,19),_FsQoSPolicyMapInProfileExceedActionFlag_Type())
fsQoSPolicyMapInProfileExceedActionFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapInProfileExceedActionFlag.setStatus(_A)
class _FsQoSPolicyMapInProfileExceedActionId_Type(Unsigned32):defaultValue=0
_FsQoSPolicyMapInProfileExceedActionId_Type.__name__=_C
_FsQoSPolicyMapInProfileExceedActionId_Object=MibTableColumn
fsQoSPolicyMapInProfileExceedActionId=_FsQoSPolicyMapInProfileExceedActionId_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,20),_FsQoSPolicyMapInProfileExceedActionId_Type())
fsQoSPolicyMapInProfileExceedActionId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapInProfileExceedActionId.setStatus(_A)
_FsQoSPolicyMapExceedActionSetIpTOS_Type=Unsigned32
_FsQoSPolicyMapExceedActionSetIpTOS_Object=MibTableColumn
fsQoSPolicyMapExceedActionSetIpTOS=_FsQoSPolicyMapExceedActionSetIpTOS_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,21),_FsQoSPolicyMapExceedActionSetIpTOS_Type())
fsQoSPolicyMapExceedActionSetIpTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapExceedActionSetIpTOS.setStatus(_A)
_FsQoSPolicyMapExceedActionSetDscp_Type=Dscp
_FsQoSPolicyMapExceedActionSetDscp_Object=MibTableColumn
fsQoSPolicyMapExceedActionSetDscp=_FsQoSPolicyMapExceedActionSetDscp_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,22),_FsQoSPolicyMapExceedActionSetDscp_Type())
fsQoSPolicyMapExceedActionSetDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapExceedActionSetDscp.setStatus(_A)
class _FsQoSPolicyMapExceedActionSetInnerVlanPrio_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsQoSPolicyMapExceedActionSetInnerVlanPrio_Type.__name__=_C
_FsQoSPolicyMapExceedActionSetInnerVlanPrio_Object=MibTableColumn
fsQoSPolicyMapExceedActionSetInnerVlanPrio=_FsQoSPolicyMapExceedActionSetInnerVlanPrio_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,23),_FsQoSPolicyMapExceedActionSetInnerVlanPrio_Type())
fsQoSPolicyMapExceedActionSetInnerVlanPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapExceedActionSetInnerVlanPrio.setStatus(_A)
class _FsQoSPolicyMapExceedActionSetVlanPrio_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsQoSPolicyMapExceedActionSetVlanPrio_Type.__name__=_C
_FsQoSPolicyMapExceedActionSetVlanPrio_Object=MibTableColumn
fsQoSPolicyMapExceedActionSetVlanPrio=_FsQoSPolicyMapExceedActionSetVlanPrio_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,24),_FsQoSPolicyMapExceedActionSetVlanPrio_Type())
fsQoSPolicyMapExceedActionSetVlanPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapExceedActionSetVlanPrio.setStatus(_A)
class _FsQoSPolicyMapExceedActionSetVlanDE_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsQoSPolicyMapExceedActionSetVlanDE_Type.__name__=_C
_FsQoSPolicyMapExceedActionSetVlanDE_Object=MibTableColumn
fsQoSPolicyMapExceedActionSetVlanDE=_FsQoSPolicyMapExceedActionSetVlanDE_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,25),_FsQoSPolicyMapExceedActionSetVlanDE_Type())
fsQoSPolicyMapExceedActionSetVlanDE.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapExceedActionSetVlanDE.setStatus(_A)
class _FsQoSPolicyMapExceedActionSetMplsExp_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsQoSPolicyMapExceedActionSetMplsExp_Type.__name__=_C
_FsQoSPolicyMapExceedActionSetMplsExp_Object=MibTableColumn
fsQoSPolicyMapExceedActionSetMplsExp=_FsQoSPolicyMapExceedActionSetMplsExp_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,26),_FsQoSPolicyMapExceedActionSetMplsExp_Type())
fsQoSPolicyMapExceedActionSetMplsExp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapExceedActionSetMplsExp.setStatus(_A)
_FsQoSPolicyMapExceedActionSetNewCLASS_Type=Unsigned32
_FsQoSPolicyMapExceedActionSetNewCLASS_Object=MibTableColumn
fsQoSPolicyMapExceedActionSetNewCLASS=_FsQoSPolicyMapExceedActionSetNewCLASS_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,27),_FsQoSPolicyMapExceedActionSetNewCLASS_Type())
fsQoSPolicyMapExceedActionSetNewCLASS.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapExceedActionSetNewCLASS.setStatus(_A)
class _FsQoSPolicyMapOutProfileActionFlag_Type(Bits):namedValues=NamedValues(*(('setFlagDrop',0),('setFlagTos',1),('setFlagDscp',2),('setFlagVlanPrio',3),('setFlagVlanDE',4),(_l,5),('setFlagMplsExp',6),(_m,7)))
_FsQoSPolicyMapOutProfileActionFlag_Type.__name__=_L
_FsQoSPolicyMapOutProfileActionFlag_Object=MibTableColumn
fsQoSPolicyMapOutProfileActionFlag=_FsQoSPolicyMapOutProfileActionFlag_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,28),_FsQoSPolicyMapOutProfileActionFlag_Type())
fsQoSPolicyMapOutProfileActionFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapOutProfileActionFlag.setStatus(_A)
class _FsQoSPolicyMapOutProfileActionId_Type(Unsigned32):defaultValue=0
_FsQoSPolicyMapOutProfileActionId_Type.__name__=_C
_FsQoSPolicyMapOutProfileActionId_Object=MibTableColumn
fsQoSPolicyMapOutProfileActionId=_FsQoSPolicyMapOutProfileActionId_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,29),_FsQoSPolicyMapOutProfileActionId_Type())
fsQoSPolicyMapOutProfileActionId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapOutProfileActionId.setStatus(_A)
_FsQoSPolicyMapOutProfileActionSetIPTOS_Type=Unsigned32
_FsQoSPolicyMapOutProfileActionSetIPTOS_Object=MibTableColumn
fsQoSPolicyMapOutProfileActionSetIPTOS=_FsQoSPolicyMapOutProfileActionSetIPTOS_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,30),_FsQoSPolicyMapOutProfileActionSetIPTOS_Type())
fsQoSPolicyMapOutProfileActionSetIPTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapOutProfileActionSetIPTOS.setStatus(_A)
_FsQoSPolicyMapOutProfileActionSetDscp_Type=Dscp
_FsQoSPolicyMapOutProfileActionSetDscp_Object=MibTableColumn
fsQoSPolicyMapOutProfileActionSetDscp=_FsQoSPolicyMapOutProfileActionSetDscp_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,31),_FsQoSPolicyMapOutProfileActionSetDscp_Type())
fsQoSPolicyMapOutProfileActionSetDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapOutProfileActionSetDscp.setStatus(_A)
class _FsQoSPolicyMapOutProfileActionSetInnerVlanPrio_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsQoSPolicyMapOutProfileActionSetInnerVlanPrio_Type.__name__=_C
_FsQoSPolicyMapOutProfileActionSetInnerVlanPrio_Object=MibTableColumn
fsQoSPolicyMapOutProfileActionSetInnerVlanPrio=_FsQoSPolicyMapOutProfileActionSetInnerVlanPrio_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,32),_FsQoSPolicyMapOutProfileActionSetInnerVlanPrio_Type())
fsQoSPolicyMapOutProfileActionSetInnerVlanPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapOutProfileActionSetInnerVlanPrio.setStatus(_A)
class _FsQoSPolicyMapOutProfileActionSetVlanPrio_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsQoSPolicyMapOutProfileActionSetVlanPrio_Type.__name__=_C
_FsQoSPolicyMapOutProfileActionSetVlanPrio_Object=MibTableColumn
fsQoSPolicyMapOutProfileActionSetVlanPrio=_FsQoSPolicyMapOutProfileActionSetVlanPrio_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,33),_FsQoSPolicyMapOutProfileActionSetVlanPrio_Type())
fsQoSPolicyMapOutProfileActionSetVlanPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapOutProfileActionSetVlanPrio.setStatus(_A)
class _FsQoSPolicyMapOutProfileActionSetVlanDE_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsQoSPolicyMapOutProfileActionSetVlanDE_Type.__name__=_C
_FsQoSPolicyMapOutProfileActionSetVlanDE_Object=MibTableColumn
fsQoSPolicyMapOutProfileActionSetVlanDE=_FsQoSPolicyMapOutProfileActionSetVlanDE_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,34),_FsQoSPolicyMapOutProfileActionSetVlanDE_Type())
fsQoSPolicyMapOutProfileActionSetVlanDE.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapOutProfileActionSetVlanDE.setStatus(_A)
class _FsQoSPolicyMapOutProfileActionSetMplsExp_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsQoSPolicyMapOutProfileActionSetMplsExp_Type.__name__=_C
_FsQoSPolicyMapOutProfileActionSetMplsExp_Object=MibTableColumn
fsQoSPolicyMapOutProfileActionSetMplsExp=_FsQoSPolicyMapOutProfileActionSetMplsExp_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,35),_FsQoSPolicyMapOutProfileActionSetMplsExp_Type())
fsQoSPolicyMapOutProfileActionSetMplsExp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapOutProfileActionSetMplsExp.setStatus(_A)
_FsQoSPolicyMapOutProfileActionSetNewCLASS_Type=Unsigned32
_FsQoSPolicyMapOutProfileActionSetNewCLASS_Object=MibTableColumn
fsQoSPolicyMapOutProfileActionSetNewCLASS=_FsQoSPolicyMapOutProfileActionSetNewCLASS_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,36),_FsQoSPolicyMapOutProfileActionSetNewCLASS_Type())
fsQoSPolicyMapOutProfileActionSetNewCLASS.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapOutProfileActionSetNewCLASS.setStatus(_A)
_FsQoSPolicyMapStatus_Type=RowStatus
_FsQoSPolicyMapStatus_Object=MibTableColumn
fsQoSPolicyMapStatus=_FsQoSPolicyMapStatus_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,37),_FsQoSPolicyMapStatus_Type())
fsQoSPolicyMapStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsQoSPolicyMapStatus.setStatus(_A)
class _FsQoSPolicyMapConformActionSetInnerVlanDE_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsQoSPolicyMapConformActionSetInnerVlanDE_Type.__name__=_C
_FsQoSPolicyMapConformActionSetInnerVlanDE_Object=MibTableColumn
fsQoSPolicyMapConformActionSetInnerVlanDE=_FsQoSPolicyMapConformActionSetInnerVlanDE_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,38),_FsQoSPolicyMapConformActionSetInnerVlanDE_Type())
fsQoSPolicyMapConformActionSetInnerVlanDE.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapConformActionSetInnerVlanDE.setStatus(_A)
class _FsQoSPolicyMapExceedActionSetInnerVlanDE_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsQoSPolicyMapExceedActionSetInnerVlanDE_Type.__name__=_C
_FsQoSPolicyMapExceedActionSetInnerVlanDE_Object=MibTableColumn
fsQoSPolicyMapExceedActionSetInnerVlanDE=_FsQoSPolicyMapExceedActionSetInnerVlanDE_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,39),_FsQoSPolicyMapExceedActionSetInnerVlanDE_Type())
fsQoSPolicyMapExceedActionSetInnerVlanDE.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapExceedActionSetInnerVlanDE.setStatus(_A)
class _FsQoSPolicyMapOutProfileActionSetInnerVlanDE_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsQoSPolicyMapOutProfileActionSetInnerVlanDE_Type.__name__=_C
_FsQoSPolicyMapOutProfileActionSetInnerVlanDE_Object=MibTableColumn
fsQoSPolicyMapOutProfileActionSetInnerVlanDE=_FsQoSPolicyMapOutProfileActionSetInnerVlanDE_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,40),_FsQoSPolicyMapOutProfileActionSetInnerVlanDE_Type())
fsQoSPolicyMapOutProfileActionSetInnerVlanDE.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyMapOutProfileActionSetInnerVlanDE.setStatus(_A)
class _FsQoSPolicyDefaultVlanDE_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsQoSPolicyDefaultVlanDE_Type.__name__=_D
_FsQoSPolicyDefaultVlanDE_Object=MibTableColumn
fsQoSPolicyDefaultVlanDE=_FsQoSPolicyDefaultVlanDE_Object((1,3,6,1,4,1,29601,2,6,1,3,2,1,41),_FsQoSPolicyDefaultVlanDE_Type())
fsQoSPolicyDefaultVlanDE.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicyDefaultVlanDE.setStatus(_A)
_FsQoSTrafficMgmt_ObjectIdentity=ObjectIdentity
fsQoSTrafficMgmt=_FsQoSTrafficMgmt_ObjectIdentity((1,3,6,1,4,1,29601,2,6,1,4))
_FsQoSQTemplateTable_Object=MibTable
fsQoSQTemplateTable=_FsQoSQTemplateTable_Object((1,3,6,1,4,1,29601,2,6,1,4,1))
if mibBuilder.loadTexts:fsQoSQTemplateTable.setStatus(_A)
_FsQoSQTemplateEntry_Object=MibTableRow
fsQoSQTemplateEntry=_FsQoSQTemplateEntry_Object((1,3,6,1,4,1,29601,2,6,1,4,1,1))
fsQoSQTemplateEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:fsQoSQTemplateEntry.setStatus(_A)
_FsQoSQTemplateId_Type=IndexInteger
_FsQoSQTemplateId_Object=MibTableColumn
fsQoSQTemplateId=_FsQoSQTemplateId_Object((1,3,6,1,4,1,29601,2,6,1,4,1,1,1),_FsQoSQTemplateId_Type())
fsQoSQTemplateId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsQoSQTemplateId.setStatus(_A)
class _FsQoSQTemplateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_FsQoSQTemplateName_Type.__name__=_K
_FsQoSQTemplateName_Object=MibTableColumn
fsQoSQTemplateName=_FsQoSQTemplateName_Object((1,3,6,1,4,1,29601,2,6,1,4,1,1,2),_FsQoSQTemplateName_Type())
fsQoSQTemplateName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSQTemplateName.setStatus(_A)
class _FsQoSQTemplateDropType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('tailDrop',2),('headDrop',3),(_O,4),('alwaysDrop',5),('wred',6)))
_FsQoSQTemplateDropType_Type.__name__=_D
_FsQoSQTemplateDropType_Object=MibTableColumn
fsQoSQTemplateDropType=_FsQoSQTemplateDropType_Object((1,3,6,1,4,1,29601,2,6,1,4,1,1,3),_FsQoSQTemplateDropType_Type())
fsQoSQTemplateDropType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSQTemplateDropType.setStatus(_A)
class _FsQoSQTemplateDropAlgoEnableFlag_Type(EnableStatus):defaultValue=2
_FsQoSQTemplateDropAlgoEnableFlag_Type.__name__=_a
_FsQoSQTemplateDropAlgoEnableFlag_Object=MibTableColumn
fsQoSQTemplateDropAlgoEnableFlag=_FsQoSQTemplateDropAlgoEnableFlag_Object((1,3,6,1,4,1,29601,2,6,1,4,1,1,4),_FsQoSQTemplateDropAlgoEnableFlag_Type())
fsQoSQTemplateDropAlgoEnableFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSQTemplateDropAlgoEnableFlag.setStatus(_A)
class _FsQoSQTemplateSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSQTemplateSize_Type.__name__=_C
_FsQoSQTemplateSize_Object=MibTableColumn
fsQoSQTemplateSize=_FsQoSQTemplateSize_Object((1,3,6,1,4,1,29601,2,6,1,4,1,1,5),_FsQoSQTemplateSize_Type())
fsQoSQTemplateSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSQTemplateSize.setStatus(_A)
if mibBuilder.loadTexts:fsQoSQTemplateSize.setUnits('bytes')
_FsQoSQTemplateStatus_Type=RowStatus
_FsQoSQTemplateStatus_Object=MibTableColumn
fsQoSQTemplateStatus=_FsQoSQTemplateStatus_Object((1,3,6,1,4,1,29601,2,6,1,4,1,1,6),_FsQoSQTemplateStatus_Type())
fsQoSQTemplateStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsQoSQTemplateStatus.setStatus(_A)
_FsQoSRandomDetectCfgTable_Object=MibTable
fsQoSRandomDetectCfgTable=_FsQoSRandomDetectCfgTable_Object((1,3,6,1,4,1,29601,2,6,1,4,2))
if mibBuilder.loadTexts:fsQoSRandomDetectCfgTable.setStatus(_A)
_FsQoSRandomDetectCfgEntry_Object=MibTableRow
fsQoSRandomDetectCfgEntry=_FsQoSRandomDetectCfgEntry_Object((1,3,6,1,4,1,29601,2,6,1,4,2,1))
fsQoSRandomDetectCfgEntry.setIndexNames((0,_E,_Z),(0,_E,_n))
if mibBuilder.loadTexts:fsQoSRandomDetectCfgEntry.setStatus(_A)
class _FsQoSRandomDetectCfgDP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_FsQoSRandomDetectCfgDP_Type.__name__=_D
_FsQoSRandomDetectCfgDP_Object=MibTableColumn
fsQoSRandomDetectCfgDP=_FsQoSRandomDetectCfgDP_Object((1,3,6,1,4,1,29601,2,6,1,4,2,1,1),_FsQoSRandomDetectCfgDP_Type())
fsQoSRandomDetectCfgDP.setMaxAccess(_G)
if mibBuilder.loadTexts:fsQoSRandomDetectCfgDP.setStatus(_A)
class _FsQoSRandomDetectCfgMinAvgThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsQoSRandomDetectCfgMinAvgThresh_Type.__name__=_C
_FsQoSRandomDetectCfgMinAvgThresh_Object=MibTableColumn
fsQoSRandomDetectCfgMinAvgThresh=_FsQoSRandomDetectCfgMinAvgThresh_Object((1,3,6,1,4,1,29601,2,6,1,4,2,1,2),_FsQoSRandomDetectCfgMinAvgThresh_Type())
fsQoSRandomDetectCfgMinAvgThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSRandomDetectCfgMinAvgThresh.setStatus(_A)
class _FsQoSRandomDetectCfgMaxAvgThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsQoSRandomDetectCfgMaxAvgThresh_Type.__name__=_C
_FsQoSRandomDetectCfgMaxAvgThresh_Object=MibTableColumn
fsQoSRandomDetectCfgMaxAvgThresh=_FsQoSRandomDetectCfgMaxAvgThresh_Object((1,3,6,1,4,1,29601,2,6,1,4,2,1,3),_FsQoSRandomDetectCfgMaxAvgThresh_Type())
fsQoSRandomDetectCfgMaxAvgThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSRandomDetectCfgMaxAvgThresh.setStatus(_A)
class _FsQoSRandomDetectCfgMaxPktSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsQoSRandomDetectCfgMaxPktSize_Type.__name__=_C
_FsQoSRandomDetectCfgMaxPktSize_Object=MibTableColumn
fsQoSRandomDetectCfgMaxPktSize=_FsQoSRandomDetectCfgMaxPktSize_Object((1,3,6,1,4,1,29601,2,6,1,4,2,1,4),_FsQoSRandomDetectCfgMaxPktSize_Type())
fsQoSRandomDetectCfgMaxPktSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSRandomDetectCfgMaxPktSize.setStatus(_A)
class _FsQoSRandomDetectCfgMaxProb_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_FsQoSRandomDetectCfgMaxProb_Type.__name__=_C
_FsQoSRandomDetectCfgMaxProb_Object=MibTableColumn
fsQoSRandomDetectCfgMaxProb=_FsQoSRandomDetectCfgMaxProb_Object((1,3,6,1,4,1,29601,2,6,1,4,2,1,5),_FsQoSRandomDetectCfgMaxProb_Type())
fsQoSRandomDetectCfgMaxProb.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSRandomDetectCfgMaxProb.setStatus(_A)
class _FsQoSRandomDetectCfgExpWeight_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_FsQoSRandomDetectCfgExpWeight_Type.__name__=_C
_FsQoSRandomDetectCfgExpWeight_Object=MibTableColumn
fsQoSRandomDetectCfgExpWeight=_FsQoSRandomDetectCfgExpWeight_Object((1,3,6,1,4,1,29601,2,6,1,4,2,1,6),_FsQoSRandomDetectCfgExpWeight_Type())
fsQoSRandomDetectCfgExpWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSRandomDetectCfgExpWeight.setStatus(_A)
_FsQoSRandomDetectCfgStatus_Type=RowStatus
_FsQoSRandomDetectCfgStatus_Object=MibTableColumn
fsQoSRandomDetectCfgStatus=_FsQoSRandomDetectCfgStatus_Object((1,3,6,1,4,1,29601,2,6,1,4,2,1,7),_FsQoSRandomDetectCfgStatus_Type())
fsQoSRandomDetectCfgStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsQoSRandomDetectCfgStatus.setStatus(_A)
class _FsQoSRandomDetectCfgGain_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsQoSRandomDetectCfgGain_Type.__name__=_C
_FsQoSRandomDetectCfgGain_Object=MibTableColumn
fsQoSRandomDetectCfgGain=_FsQoSRandomDetectCfgGain_Object((1,3,6,1,4,1,29601,2,6,1,4,2,1,8),_FsQoSRandomDetectCfgGain_Type())
fsQoSRandomDetectCfgGain.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSRandomDetectCfgGain.setStatus(_A)
class _FsQoSRandomDetectCfgDropThreshType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('discardpackets',1),('discardbytes',2)))
_FsQoSRandomDetectCfgDropThreshType_Type.__name__=_D
_FsQoSRandomDetectCfgDropThreshType_Object=MibTableColumn
fsQoSRandomDetectCfgDropThreshType=_FsQoSRandomDetectCfgDropThreshType_Object((1,3,6,1,4,1,29601,2,6,1,4,2,1,9),_FsQoSRandomDetectCfgDropThreshType_Type())
fsQoSRandomDetectCfgDropThreshType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSRandomDetectCfgDropThreshType.setStatus(_A)
class _FsQoSRandomDetectCfgECNThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSRandomDetectCfgECNThresh_Type.__name__=_C
_FsQoSRandomDetectCfgECNThresh_Object=MibTableColumn
fsQoSRandomDetectCfgECNThresh=_FsQoSRandomDetectCfgECNThresh_Object((1,3,6,1,4,1,29601,2,6,1,4,2,1,10),_FsQoSRandomDetectCfgECNThresh_Type())
fsQoSRandomDetectCfgECNThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSRandomDetectCfgECNThresh.setStatus(_A)
class _FsQoSRandomDetectCfgActionFlag_Type(Bits):defaultHexValue='';namedValues=NamedValues(*((_M,0),('capavg',1),('markcongestion',2)))
_FsQoSRandomDetectCfgActionFlag_Type.__name__=_L
_FsQoSRandomDetectCfgActionFlag_Object=MibTableColumn
fsQoSRandomDetectCfgActionFlag=_FsQoSRandomDetectCfgActionFlag_Object((1,3,6,1,4,1,29601,2,6,1,4,2,1,11),_FsQoSRandomDetectCfgActionFlag_Type())
fsQoSRandomDetectCfgActionFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSRandomDetectCfgActionFlag.setStatus(_A)
_FsQoSShapeTemplateTable_Object=MibTable
fsQoSShapeTemplateTable=_FsQoSShapeTemplateTable_Object((1,3,6,1,4,1,29601,2,6,1,4,3))
if mibBuilder.loadTexts:fsQoSShapeTemplateTable.setStatus(_A)
_FsQoSShapeTemplateEntry_Object=MibTableRow
fsQoSShapeTemplateEntry=_FsQoSShapeTemplateEntry_Object((1,3,6,1,4,1,29601,2,6,1,4,3,1))
fsQoSShapeTemplateEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:fsQoSShapeTemplateEntry.setStatus(_A)
_FsQoSShapeTemplateId_Type=IndexInteger
_FsQoSShapeTemplateId_Object=MibTableColumn
fsQoSShapeTemplateId=_FsQoSShapeTemplateId_Object((1,3,6,1,4,1,29601,2,6,1,4,3,1,1),_FsQoSShapeTemplateId_Type())
fsQoSShapeTemplateId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsQoSShapeTemplateId.setStatus(_A)
class _FsQoSShapeTemplateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_FsQoSShapeTemplateName_Type.__name__=_K
_FsQoSShapeTemplateName_Object=MibTableColumn
fsQoSShapeTemplateName=_FsQoSShapeTemplateName_Object((1,3,6,1,4,1,29601,2,6,1,4,3,1,2),_FsQoSShapeTemplateName_Type())
fsQoSShapeTemplateName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSShapeTemplateName.setStatus(_A)
class _FsQoSShapeTemplateCIR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsQoSShapeTemplateCIR_Type.__name__=_C
_FsQoSShapeTemplateCIR_Object=MibTableColumn
fsQoSShapeTemplateCIR=_FsQoSShapeTemplateCIR_Object((1,3,6,1,4,1,29601,2,6,1,4,3,1,3),_FsQoSShapeTemplateCIR_Type())
fsQoSShapeTemplateCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSShapeTemplateCIR.setStatus(_A)
class _FsQoSShapeTemplateCBS_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSShapeTemplateCBS_Type.__name__=_C
_FsQoSShapeTemplateCBS_Object=MibTableColumn
fsQoSShapeTemplateCBS=_FsQoSShapeTemplateCBS_Object((1,3,6,1,4,1,29601,2,6,1,4,3,1,4),_FsQoSShapeTemplateCBS_Type())
fsQoSShapeTemplateCBS.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSShapeTemplateCBS.setStatus(_A)
if mibBuilder.loadTexts:fsQoSShapeTemplateCBS.setUnits(_P)
class _FsQoSShapeTemplateEIR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSShapeTemplateEIR_Type.__name__=_C
_FsQoSShapeTemplateEIR_Object=MibTableColumn
fsQoSShapeTemplateEIR=_FsQoSShapeTemplateEIR_Object((1,3,6,1,4,1,29601,2,6,1,4,3,1,5),_FsQoSShapeTemplateEIR_Type())
fsQoSShapeTemplateEIR.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSShapeTemplateEIR.setStatus(_A)
class _FsQoSShapeTemplateEBS_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSShapeTemplateEBS_Type.__name__=_C
_FsQoSShapeTemplateEBS_Object=MibTableColumn
fsQoSShapeTemplateEBS=_FsQoSShapeTemplateEBS_Object((1,3,6,1,4,1,29601,2,6,1,4,3,1,6),_FsQoSShapeTemplateEBS_Type())
fsQoSShapeTemplateEBS.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSShapeTemplateEBS.setStatus(_A)
if mibBuilder.loadTexts:fsQoSShapeTemplateEBS.setUnits(_P)
_FsQoSShapeTemplateStatus_Type=RowStatus
_FsQoSShapeTemplateStatus_Object=MibTableColumn
fsQoSShapeTemplateStatus=_FsQoSShapeTemplateStatus_Object((1,3,6,1,4,1,29601,2,6,1,4,3,1,7),_FsQoSShapeTemplateStatus_Type())
fsQoSShapeTemplateStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsQoSShapeTemplateStatus.setStatus(_A)
_FsQoSQMapTable_Object=MibTable
fsQoSQMapTable=_FsQoSQMapTable_Object((1,3,6,1,4,1,29601,2,6,1,4,4))
if mibBuilder.loadTexts:fsQoSQMapTable.setStatus(_A)
_FsQoSQMapEntry_Object=MibTableRow
fsQoSQMapEntry=_FsQoSQMapEntry_Object((1,3,6,1,4,1,29601,2,6,1,4,4,1))
fsQoSQMapEntry.setIndexNames((0,_I,_J),(0,_E,_p),(0,_E,_q),(0,_E,_r))
if mibBuilder.loadTexts:fsQoSQMapEntry.setStatus(_A)
class _FsQoSQMapCLASS_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSQMapCLASS_Type.__name__=_C
_FsQoSQMapCLASS_Object=MibTableColumn
fsQoSQMapCLASS=_FsQoSQMapCLASS_Object((1,3,6,1,4,1,29601,2,6,1,4,4,1,1),_FsQoSQMapCLASS_Type())
fsQoSQMapCLASS.setMaxAccess(_G)
if mibBuilder.loadTexts:fsQoSQMapCLASS.setStatus(_A)
class _FsQoSQMapRegenPriType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_M,0),(_S,1),(_T,2),(_U,3),(_V,4),(_e,5),('internalPrio',6),(_N,7)))
_FsQoSQMapRegenPriType_Type.__name__=_D
_FsQoSQMapRegenPriType_Object=MibTableColumn
fsQoSQMapRegenPriType=_FsQoSQMapRegenPriType_Object((1,3,6,1,4,1,29601,2,6,1,4,4,1,2),_FsQoSQMapRegenPriType_Type())
fsQoSQMapRegenPriType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsQoSQMapRegenPriType.setStatus(_A)
class _FsQoSQMapRegenPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_FsQoSQMapRegenPriority_Type.__name__=_C
_FsQoSQMapRegenPriority_Object=MibTableColumn
fsQoSQMapRegenPriority=_FsQoSQMapRegenPriority_Object((1,3,6,1,4,1,29601,2,6,1,4,4,1,3),_FsQoSQMapRegenPriority_Type())
fsQoSQMapRegenPriority.setMaxAccess(_G)
if mibBuilder.loadTexts:fsQoSQMapRegenPriority.setStatus(_A)
class _FsQoSQMapQId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsQoSQMapQId_Type.__name__=_C
_FsQoSQMapQId_Object=MibTableColumn
fsQoSQMapQId=_FsQoSQMapQId_Object((1,3,6,1,4,1,29601,2,6,1,4,4,1,4),_FsQoSQMapQId_Type())
fsQoSQMapQId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSQMapQId.setStatus(_A)
_FsQoSQMapStatus_Type=RowStatus
_FsQoSQMapStatus_Object=MibTableColumn
fsQoSQMapStatus=_FsQoSQMapStatus_Object((1,3,6,1,4,1,29601,2,6,1,4,4,1,5),_FsQoSQMapStatus_Type())
fsQoSQMapStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsQoSQMapStatus.setStatus(_A)
class _FsQoSQMapRegenDEI_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_FsQoSQMapRegenDEI_Type.__name__=_D
_FsQoSQMapRegenDEI_Object=MibTableColumn
fsQoSQMapRegenDEI=_FsQoSQMapRegenDEI_Object((1,3,6,1,4,1,29601,2,6,1,4,4,1,6),_FsQoSQMapRegenDEI_Type())
fsQoSQMapRegenDEI.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSQMapRegenDEI.setStatus(_A)
class _FsQoSQMapRegenColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_W,0),(_X,1),(_O,2)))
_FsQoSQMapRegenColor_Type.__name__=_D
_FsQoSQMapRegenColor_Object=MibTableColumn
fsQoSQMapRegenColor=_FsQoSQMapRegenColor_Object((1,3,6,1,4,1,29601,2,6,1,4,4,1,7),_FsQoSQMapRegenColor_Type())
fsQoSQMapRegenColor.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQoSQMapRegenColor.setStatus(_A)
_FsQoSQTable_Object=MibTable
fsQoSQTable=_FsQoSQTable_Object((1,3,6,1,4,1,29601,2,6,1,4,5))
if mibBuilder.loadTexts:fsQoSQTable.setStatus(_A)
_FsQoSQEntry_Object=MibTableRow
fsQoSQEntry=_FsQoSQEntry_Object((1,3,6,1,4,1,29601,2,6,1,4,5,1))
fsQoSQEntry.setIndexNames((0,_I,_J),(0,_E,_s))
if mibBuilder.loadTexts:fsQoSQEntry.setStatus(_A)
class _FsQoSQId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsQoSQId_Type.__name__=_C
_FsQoSQId_Object=MibTableColumn
fsQoSQId=_FsQoSQId_Object((1,3,6,1,4,1,29601,2,6,1,4,5,1,1),_FsQoSQId_Type())
fsQoSQId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsQoSQId.setStatus(_A)
class _FsQoSQCfgTemplateId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsQoSQCfgTemplateId_Type.__name__=_C
_FsQoSQCfgTemplateId_Object=MibTableColumn
fsQoSQCfgTemplateId=_FsQoSQCfgTemplateId_Object((1,3,6,1,4,1,29601,2,6,1,4,5,1,2),_FsQoSQCfgTemplateId_Type())
fsQoSQCfgTemplateId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSQCfgTemplateId.setStatus(_A)
class _FsQoSQSchedulerId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsQoSQSchedulerId_Type.__name__=_C
_FsQoSQSchedulerId_Object=MibTableColumn
fsQoSQSchedulerId=_FsQoSQSchedulerId_Object((1,3,6,1,4,1,29601,2,6,1,4,5,1,3),_FsQoSQSchedulerId_Type())
fsQoSQSchedulerId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSQSchedulerId.setStatus(_A)
class _FsQoSQWeight_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_FsQoSQWeight_Type.__name__=_C
_FsQoSQWeight_Object=MibTableColumn
fsQoSQWeight=_FsQoSQWeight_Object((1,3,6,1,4,1,29601,2,6,1,4,5,1,4),_FsQoSQWeight_Type())
fsQoSQWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSQWeight.setStatus(_A)
class _FsQoSQPriority_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsQoSQPriority_Type.__name__=_C
_FsQoSQPriority_Object=MibTableColumn
fsQoSQPriority=_FsQoSQPriority_Object((1,3,6,1,4,1,29601,2,6,1,4,5,1,5),_FsQoSQPriority_Type())
fsQoSQPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSQPriority.setStatus(_A)
class _FsQoSQShapeId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSQShapeId_Type.__name__=_C
_FsQoSQShapeId_Object=MibTableColumn
fsQoSQShapeId=_FsQoSQShapeId_Object((1,3,6,1,4,1,29601,2,6,1,4,5,1,6),_FsQoSQShapeId_Type())
fsQoSQShapeId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSQShapeId.setStatus(_A)
_FsQoSQStatus_Type=RowStatus
_FsQoSQStatus_Object=MibTableColumn
fsQoSQStatus=_FsQoSQStatus_Object((1,3,6,1,4,1,29601,2,6,1,4,5,1,7),_FsQoSQStatus_Type())
fsQoSQStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsQoSQStatus.setStatus(_A)
class _FsQoSQType_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_FsQoSQType_Type.__name__=_C
_FsQoSQType_Object=MibTableColumn
fsQoSQType=_FsQoSQType_Object((1,3,6,1,4,1,29601,2,6,1,4,5,1,8),_FsQoSQType_Type())
fsQoSQType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSQType.setStatus(_A)
_FsQoSSchedulerTable_Object=MibTable
fsQoSSchedulerTable=_FsQoSSchedulerTable_Object((1,3,6,1,4,1,29601,2,6,1,4,6))
if mibBuilder.loadTexts:fsQoSSchedulerTable.setStatus(_A)
_FsQoSSchedulerEntry_Object=MibTableRow
fsQoSSchedulerEntry=_FsQoSSchedulerEntry_Object((1,3,6,1,4,1,29601,2,6,1,4,6,1))
fsQoSSchedulerEntry.setIndexNames((0,_I,_J),(0,_E,_b))
if mibBuilder.loadTexts:fsQoSSchedulerEntry.setStatus(_A)
class _FsQoSSchedulerId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSSchedulerId_Type.__name__=_C
_FsQoSSchedulerId_Object=MibTableColumn
fsQoSSchedulerId=_FsQoSSchedulerId_Object((1,3,6,1,4,1,29601,2,6,1,4,6,1,1),_FsQoSSchedulerId_Type())
fsQoSSchedulerId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsQoSSchedulerId.setStatus(_A)
class _FsQoSSchedulerSchedAlgorithm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('strictPriority',1),('roundRobin',2),('weightedRoundRobin',3),('weightedFairQueing',4),('strictRoundRobin',5),('strictWeightedRoundRobin',6),('strictWeightedFairQueing',7),('deficitRoundRobin',8)))
_FsQoSSchedulerSchedAlgorithm_Type.__name__=_D
_FsQoSSchedulerSchedAlgorithm_Object=MibTableColumn
fsQoSSchedulerSchedAlgorithm=_FsQoSSchedulerSchedAlgorithm_Object((1,3,6,1,4,1,29601,2,6,1,4,6,1,2),_FsQoSSchedulerSchedAlgorithm_Type())
fsQoSSchedulerSchedAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSSchedulerSchedAlgorithm.setStatus(_A)
class _FsQoSSchedulerShapeId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSSchedulerShapeId_Type.__name__=_C
_FsQoSSchedulerShapeId_Object=MibTableColumn
fsQoSSchedulerShapeId=_FsQoSSchedulerShapeId_Object((1,3,6,1,4,1,29601,2,6,1,4,6,1,3),_FsQoSSchedulerShapeId_Type())
fsQoSSchedulerShapeId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSSchedulerShapeId.setStatus(_A)
class _FsQoSSchedulerHierarchyLevel_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_FsQoSSchedulerHierarchyLevel_Type.__name__=_C
_FsQoSSchedulerHierarchyLevel_Object=MibTableColumn
fsQoSSchedulerHierarchyLevel=_FsQoSSchedulerHierarchyLevel_Object((1,3,6,1,4,1,29601,2,6,1,4,6,1,4),_FsQoSSchedulerHierarchyLevel_Type())
fsQoSSchedulerHierarchyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSSchedulerHierarchyLevel.setStatus(_A)
class _FsQoSSchedulerGlobalId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSSchedulerGlobalId_Type.__name__=_C
_FsQoSSchedulerGlobalId_Object=MibTableColumn
fsQoSSchedulerGlobalId=_FsQoSSchedulerGlobalId_Object((1,3,6,1,4,1,29601,2,6,1,4,6,1,5),_FsQoSSchedulerGlobalId_Type())
fsQoSSchedulerGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSSchedulerGlobalId.setStatus(_A)
_FsQoSSchedulerStatus_Type=RowStatus
_FsQoSSchedulerStatus_Object=MibTableColumn
fsQoSSchedulerStatus=_FsQoSSchedulerStatus_Object((1,3,6,1,4,1,29601,2,6,1,4,6,1,6),_FsQoSSchedulerStatus_Type())
fsQoSSchedulerStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsQoSSchedulerStatus.setStatus(_A)
_FsQoSHierarchyTable_Object=MibTable
fsQoSHierarchyTable=_FsQoSHierarchyTable_Object((1,3,6,1,4,1,29601,2,6,1,4,7))
if mibBuilder.loadTexts:fsQoSHierarchyTable.setStatus(_A)
_FsQoSHierarchyEntry_Object=MibTableRow
fsQoSHierarchyEntry=_FsQoSHierarchyEntry_Object((1,3,6,1,4,1,29601,2,6,1,4,7,1))
fsQoSHierarchyEntry.setIndexNames((0,_I,_J),(0,_E,_t),(0,_E,_b))
if mibBuilder.loadTexts:fsQoSHierarchyEntry.setStatus(_A)
class _FsQoSHierarchyLevel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_FsQoSHierarchyLevel_Type.__name__=_C
_FsQoSHierarchyLevel_Object=MibTableColumn
fsQoSHierarchyLevel=_FsQoSHierarchyLevel_Object((1,3,6,1,4,1,29601,2,6,1,4,7,1,1),_FsQoSHierarchyLevel_Type())
fsQoSHierarchyLevel.setMaxAccess(_G)
if mibBuilder.loadTexts:fsQoSHierarchyLevel.setStatus(_A)
class _FsQoSHierarchyQNext_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSHierarchyQNext_Type.__name__=_C
_FsQoSHierarchyQNext_Object=MibTableColumn
fsQoSHierarchyQNext=_FsQoSHierarchyQNext_Object((1,3,6,1,4,1,29601,2,6,1,4,7,1,2),_FsQoSHierarchyQNext_Type())
fsQoSHierarchyQNext.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSHierarchyQNext.setStatus(_A)
class _FsQoSHierarchySchedNext_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsQoSHierarchySchedNext_Type.__name__=_C
_FsQoSHierarchySchedNext_Object=MibTableColumn
fsQoSHierarchySchedNext=_FsQoSHierarchySchedNext_Object((1,3,6,1,4,1,29601,2,6,1,4,7,1,3),_FsQoSHierarchySchedNext_Type())
fsQoSHierarchySchedNext.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSHierarchySchedNext.setStatus(_A)
class _FsQoSHierarchyWeight_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_FsQoSHierarchyWeight_Type.__name__=_C
_FsQoSHierarchyWeight_Object=MibTableColumn
fsQoSHierarchyWeight=_FsQoSHierarchyWeight_Object((1,3,6,1,4,1,29601,2,6,1,4,7,1,4),_FsQoSHierarchyWeight_Type())
fsQoSHierarchyWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSHierarchyWeight.setStatus(_A)
if mibBuilder.loadTexts:fsQoSHierarchyWeight.setUnits('Percentage')
class _FsQoSHierarchyPriority_Type(SchedulerPriority):defaultValue=0
_FsQoSHierarchyPriority_Type.__name__=_u
_FsQoSHierarchyPriority_Object=MibTableColumn
fsQoSHierarchyPriority=_FsQoSHierarchyPriority_Object((1,3,6,1,4,1,29601,2,6,1,4,7,1,5),_FsQoSHierarchyPriority_Type())
fsQoSHierarchyPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSHierarchyPriority.setStatus(_A)
_FsQoSHierarchyStatus_Type=RowStatus
_FsQoSHierarchyStatus_Object=MibTableColumn
fsQoSHierarchyStatus=_FsQoSHierarchyStatus_Object((1,3,6,1,4,1,29601,2,6,1,4,7,1,6),_FsQoSHierarchyStatus_Type())
fsQoSHierarchyStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsQoSHierarchyStatus.setStatus(_A)
_FsQoSDefUserPriorityTable_Object=MibTable
fsQoSDefUserPriorityTable=_FsQoSDefUserPriorityTable_Object((1,3,6,1,4,1,29601,2,6,1,4,8))
if mibBuilder.loadTexts:fsQoSDefUserPriorityTable.setStatus(_A)
_FsQoSDefUserPriorityEntry_Object=MibTableRow
fsQoSDefUserPriorityEntry=_FsQoSDefUserPriorityEntry_Object((1,3,6,1,4,1,29601,2,6,1,4,8,1))
fsQoSDefUserPriorityEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:fsQoSDefUserPriorityEntry.setStatus(_A)
class _FsQoSPortDefaultUserPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsQoSPortDefaultUserPriority_Type.__name__=_D
_FsQoSPortDefaultUserPriority_Object=MibTableColumn
fsQoSPortDefaultUserPriority=_FsQoSPortDefaultUserPriority_Object((1,3,6,1,4,1,29601,2,6,1,4,8,1,1),_FsQoSPortDefaultUserPriority_Type())
fsQoSPortDefaultUserPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPortDefaultUserPriority.setStatus(_A)
class _FsQoSPortPbitPrefOverDscp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_Q,2)))
_FsQoSPortPbitPrefOverDscp_Type.__name__=_D
_FsQoSPortPbitPrefOverDscp_Object=MibTableColumn
fsQoSPortPbitPrefOverDscp=_FsQoSPortPbitPrefOverDscp_Object((1,3,6,1,4,1,29601,2,6,1,4,8,1,2),_FsQoSPortPbitPrefOverDscp_Type())
fsQoSPortPbitPrefOverDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPortPbitPrefOverDscp.setStatus(_A)
_FsQoSStats_ObjectIdentity=ObjectIdentity
fsQoSStats=_FsQoSStats_ObjectIdentity((1,3,6,1,4,1,29601,2,6,1,5))
_FsQoSPolicerStatsTable_Object=MibTable
fsQoSPolicerStatsTable=_FsQoSPolicerStatsTable_Object((1,3,6,1,4,1,29601,2,6,1,5,1))
if mibBuilder.loadTexts:fsQoSPolicerStatsTable.setStatus(_A)
_FsQoSPolicerStatsEntry_Object=MibTableRow
fsQoSPolicerStatsEntry=_FsQoSPolicerStatsEntry_Object((1,3,6,1,4,1,29601,2,6,1,5,1,1))
fsQoSPolicerStatsEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:fsQoSPolicerStatsEntry.setStatus(_A)
_FsQoSPolicerStatsConformPkts_Type=Counter64
_FsQoSPolicerStatsConformPkts_Object=MibTableColumn
fsQoSPolicerStatsConformPkts=_FsQoSPolicerStatsConformPkts_Object((1,3,6,1,4,1,29601,2,6,1,5,1,1,1),_FsQoSPolicerStatsConformPkts_Type())
fsQoSPolicerStatsConformPkts.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQoSPolicerStatsConformPkts.setStatus(_A)
_FsQoSPolicerStatsConformOctets_Type=Counter64
_FsQoSPolicerStatsConformOctets_Object=MibTableColumn
fsQoSPolicerStatsConformOctets=_FsQoSPolicerStatsConformOctets_Object((1,3,6,1,4,1,29601,2,6,1,5,1,1,2),_FsQoSPolicerStatsConformOctets_Type())
fsQoSPolicerStatsConformOctets.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQoSPolicerStatsConformOctets.setStatus(_A)
_FsQoSPolicerStatsExceedPkts_Type=Counter64
_FsQoSPolicerStatsExceedPkts_Object=MibTableColumn
fsQoSPolicerStatsExceedPkts=_FsQoSPolicerStatsExceedPkts_Object((1,3,6,1,4,1,29601,2,6,1,5,1,1,3),_FsQoSPolicerStatsExceedPkts_Type())
fsQoSPolicerStatsExceedPkts.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQoSPolicerStatsExceedPkts.setStatus(_A)
_FsQoSPolicerStatsExceedOctets_Type=Counter64
_FsQoSPolicerStatsExceedOctets_Object=MibTableColumn
fsQoSPolicerStatsExceedOctets=_FsQoSPolicerStatsExceedOctets_Object((1,3,6,1,4,1,29601,2,6,1,5,1,1,4),_FsQoSPolicerStatsExceedOctets_Type())
fsQoSPolicerStatsExceedOctets.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQoSPolicerStatsExceedOctets.setStatus(_A)
_FsQoSPolicerStatsViolatePkts_Type=Counter64
_FsQoSPolicerStatsViolatePkts_Object=MibTableColumn
fsQoSPolicerStatsViolatePkts=_FsQoSPolicerStatsViolatePkts_Object((1,3,6,1,4,1,29601,2,6,1,5,1,1,5),_FsQoSPolicerStatsViolatePkts_Type())
fsQoSPolicerStatsViolatePkts.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQoSPolicerStatsViolatePkts.setStatus(_A)
_FsQoSPolicerStatsViolateOctets_Type=Counter64
_FsQoSPolicerStatsViolateOctets_Object=MibTableColumn
fsQoSPolicerStatsViolateOctets=_FsQoSPolicerStatsViolateOctets_Object((1,3,6,1,4,1,29601,2,6,1,5,1,1,6),_FsQoSPolicerStatsViolateOctets_Type())
fsQoSPolicerStatsViolateOctets.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQoSPolicerStatsViolateOctets.setStatus(_A)
class _FsQoSPolicerStatsStatus_Type(EnableStatus):defaultValue=2
_FsQoSPolicerStatsStatus_Type.__name__=_a
_FsQoSPolicerStatsStatus_Object=MibTableColumn
fsQoSPolicerStatsStatus=_FsQoSPolicerStatsStatus_Object((1,3,6,1,4,1,29601,2,6,1,5,1,1,7),_FsQoSPolicerStatsStatus_Type())
fsQoSPolicerStatsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicerStatsStatus.setStatus(_A)
class _FsQoSPolicerStatsClearCounter_Type(TruthValue):defaultValue=2
_FsQoSPolicerStatsClearCounter_Type.__name__=_c
_FsQoSPolicerStatsClearCounter_Object=MibTableColumn
fsQoSPolicerStatsClearCounter=_FsQoSPolicerStatsClearCounter_Object((1,3,6,1,4,1,29601,2,6,1,5,1,1,8),_FsQoSPolicerStatsClearCounter_Type())
fsQoSPolicerStatsClearCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQoSPolicerStatsClearCounter.setStatus(_A)
_FsQoSCoSQStatsTable_Object=MibTable
fsQoSCoSQStatsTable=_FsQoSCoSQStatsTable_Object((1,3,6,1,4,1,29601,2,6,1,5,2))
if mibBuilder.loadTexts:fsQoSCoSQStatsTable.setStatus(_A)
_FsQoSCoSQStatsEntry_Object=MibTableRow
fsQoSCoSQStatsEntry=_FsQoSCoSQStatsEntry_Object((1,3,6,1,4,1,29601,2,6,1,5,2,1))
fsQoSCoSQStatsEntry.setIndexNames((0,_I,_J),(0,_E,_v))
if mibBuilder.loadTexts:fsQoSCoSQStatsEntry.setStatus(_A)
class _FsQoSCoSQId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsQoSCoSQId_Type.__name__=_C
_FsQoSCoSQId_Object=MibTableColumn
fsQoSCoSQId=_FsQoSCoSQId_Object((1,3,6,1,4,1,29601,2,6,1,5,2,1,1),_FsQoSCoSQId_Type())
fsQoSCoSQId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsQoSCoSQId.setStatus(_A)
_FsQoSCoSQStatsEnQPkts_Type=Counter64
_FsQoSCoSQStatsEnQPkts_Object=MibTableColumn
fsQoSCoSQStatsEnQPkts=_FsQoSCoSQStatsEnQPkts_Object((1,3,6,1,4,1,29601,2,6,1,5,2,1,2),_FsQoSCoSQStatsEnQPkts_Type())
fsQoSCoSQStatsEnQPkts.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQoSCoSQStatsEnQPkts.setStatus(_A)
_FsQoSCoSQStatsEnQBytes_Type=Counter64
_FsQoSCoSQStatsEnQBytes_Object=MibTableColumn
fsQoSCoSQStatsEnQBytes=_FsQoSCoSQStatsEnQBytes_Object((1,3,6,1,4,1,29601,2,6,1,5,2,1,3),_FsQoSCoSQStatsEnQBytes_Type())
fsQoSCoSQStatsEnQBytes.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQoSCoSQStatsEnQBytes.setStatus(_A)
_FsQoSCoSQStatsDeQPkts_Type=Counter64
_FsQoSCoSQStatsDeQPkts_Object=MibTableColumn
fsQoSCoSQStatsDeQPkts=_FsQoSCoSQStatsDeQPkts_Object((1,3,6,1,4,1,29601,2,6,1,5,2,1,4),_FsQoSCoSQStatsDeQPkts_Type())
fsQoSCoSQStatsDeQPkts.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQoSCoSQStatsDeQPkts.setStatus(_A)
_FsQoSCoSQStatsDeQBytes_Type=Counter64
_FsQoSCoSQStatsDeQBytes_Object=MibTableColumn
fsQoSCoSQStatsDeQBytes=_FsQoSCoSQStatsDeQBytes_Object((1,3,6,1,4,1,29601,2,6,1,5,2,1,5),_FsQoSCoSQStatsDeQBytes_Type())
fsQoSCoSQStatsDeQBytes.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQoSCoSQStatsDeQBytes.setStatus(_A)
_FsQoSCoSQStatsDiscardPkts_Type=Counter64
_FsQoSCoSQStatsDiscardPkts_Object=MibTableColumn
fsQoSCoSQStatsDiscardPkts=_FsQoSCoSQStatsDiscardPkts_Object((1,3,6,1,4,1,29601,2,6,1,5,2,1,6),_FsQoSCoSQStatsDiscardPkts_Type())
fsQoSCoSQStatsDiscardPkts.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQoSCoSQStatsDiscardPkts.setStatus(_A)
_FsQoSCoSQStatsDiscardBytes_Type=Counter64
_FsQoSCoSQStatsDiscardBytes_Object=MibTableColumn
fsQoSCoSQStatsDiscardBytes=_FsQoSCoSQStatsDiscardBytes_Object((1,3,6,1,4,1,29601,2,6,1,5,2,1,7),_FsQoSCoSQStatsDiscardBytes_Type())
fsQoSCoSQStatsDiscardBytes.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQoSCoSQStatsDiscardBytes.setStatus(_A)
_FsQoSCoSQStatsOccupancy_Type=Counter64
_FsQoSCoSQStatsOccupancy_Object=MibTableColumn
fsQoSCoSQStatsOccupancy=_FsQoSCoSQStatsOccupancy_Object((1,3,6,1,4,1,29601,2,6,1,5,2,1,8),_FsQoSCoSQStatsOccupancy_Type())
fsQoSCoSQStatsOccupancy.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQoSCoSQStatsOccupancy.setStatus(_A)
_FsQoSCoSQStatsCongMgntAlgoDrop_Type=Counter64
_FsQoSCoSQStatsCongMgntAlgoDrop_Object=MibTableColumn
fsQoSCoSQStatsCongMgntAlgoDrop=_FsQoSCoSQStatsCongMgntAlgoDrop_Object((1,3,6,1,4,1,29601,2,6,1,5,2,1,9),_FsQoSCoSQStatsCongMgntAlgoDrop_Type())
fsQoSCoSQStatsCongMgntAlgoDrop.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQoSCoSQStatsCongMgntAlgoDrop.setStatus(_A)
_FsQosHwCpuRateControl_ObjectIdentity=ObjectIdentity
fsQosHwCpuRateControl=_FsQosHwCpuRateControl_ObjectIdentity((1,3,6,1,4,1,29601,2,6,1,6))
_FsQosHwCpuRateLimitTable_Object=MibTable
fsQosHwCpuRateLimitTable=_FsQosHwCpuRateLimitTable_Object((1,3,6,1,4,1,29601,2,6,1,6,1))
if mibBuilder.loadTexts:fsQosHwCpuRateLimitTable.setStatus(_A)
_FsQosHwCpuRateLimitEntry_Object=MibTableRow
fsQosHwCpuRateLimitEntry=_FsQosHwCpuRateLimitEntry_Object((1,3,6,1,4,1,29601,2,6,1,6,1,1))
fsQosHwCpuRateLimitEntry.setIndexNames((0,_E,_w))
if mibBuilder.loadTexts:fsQosHwCpuRateLimitEntry.setStatus(_A)
class _FsQosHwCpuQId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsQosHwCpuQId_Type.__name__=_C
_FsQosHwCpuQId_Object=MibTableColumn
fsQosHwCpuQId=_FsQosHwCpuQId_Object((1,3,6,1,4,1,29601,2,6,1,6,1,1,1),_FsQosHwCpuQId_Type())
fsQosHwCpuQId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsQosHwCpuQId.setStatus(_A)
class _FsQosHwCpuMinRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsQosHwCpuMinRate_Type.__name__=_C
_FsQosHwCpuMinRate_Object=MibTableColumn
fsQosHwCpuMinRate=_FsQosHwCpuMinRate_Object((1,3,6,1,4,1,29601,2,6,1,6,1,1,2),_FsQosHwCpuMinRate_Type())
fsQosHwCpuMinRate.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQosHwCpuMinRate.setStatus(_A)
class _FsQosHwCpuMaxRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsQosHwCpuMaxRate_Type.__name__=_C
_FsQosHwCpuMaxRate_Object=MibTableColumn
fsQosHwCpuMaxRate=_FsQosHwCpuMaxRate_Object((1,3,6,1,4,1,29601,2,6,1,6,1,1,3),_FsQosHwCpuMaxRate_Type())
fsQosHwCpuMaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:fsQosHwCpuMaxRate.setStatus(_A)
_FsQosHwCpuRowStatus_Type=RowStatus
_FsQosHwCpuRowStatus_Object=MibTableColumn
fsQosHwCpuRowStatus=_FsQosHwCpuRowStatus_Object((1,3,6,1,4,1,29601,2,6,1,6,1,1,4),_FsQosHwCpuRowStatus_Type())
fsQosHwCpuRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsQosHwCpuRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'Dscp':Dscp,_j:MeterColorMode,'MeterType':MeterType,_a:EnableStatus,_u:SchedulerPriority,'IndexInteger':IndexInteger,'fsQoSMib':fsQoSMib,'fsQoSMIBObjects':fsQoSMIBObjects,'fsQoSSystem':fsQoSSystem,'fsQoSSystemControl':fsQoSSystemControl,'fsQoSStatus':fsQoSStatus,'fsQoSTrcFlag':fsQoSTrcFlag,'fsQoSRateUnit':fsQoSRateUnit,'fsQoSRateGranularity':fsQoSRateGranularity,'fsQoSVlanQueueingStatus':fsQoSVlanQueueingStatus,'fsQoSClass':fsQoSClass,'fsQoSPriorityMapTable':fsQoSPriorityMapTable,'fsQoSPriorityMapEntry':fsQoSPriorityMapEntry,_d:fsQoSPriorityMapID,'fsQoSPriorityMapName':fsQoSPriorityMapName,'fsQoSPriorityMapIfIndex':fsQoSPriorityMapIfIndex,'fsQoSPriorityMapVlanId':fsQoSPriorityMapVlanId,'fsQoSPriorityMapInPriority':fsQoSPriorityMapInPriority,'fsQoSPriorityMapInPriType':fsQoSPriorityMapInPriType,'fsQoSPriorityMapRegenPriority':fsQoSPriorityMapRegenPriority,'fsQoSPriorityMapRegenInnerPriority':fsQoSPriorityMapRegenInnerPriority,'fsQoSPriorityMapConfigStatus':fsQoSPriorityMapConfigStatus,'fsQoSPriorityMapStatus':fsQoSPriorityMapStatus,'fsQoSPriorityMapInDEI':fsQoSPriorityMapInDEI,'fsQoSPriorityMapRegenColor':fsQoSPriorityMapRegenColor,'fsQoSClassMapTable':fsQoSClassMapTable,'fsQoSClassMapEntry':fsQoSClassMapEntry,_f:fsQoSClassMapId,'fsQoSClassMapName':fsQoSClassMapName,'fsQoSClassMapL2FilterId':fsQoSClassMapL2FilterId,'fsQoSClassMapL3FilterId':fsQoSClassMapL3FilterId,'fsQoSClassMapPriorityMapId':fsQoSClassMapPriorityMapId,'fsQoSClassMapCLASS':fsQoSClassMapCLASS,'fsQoSClassMapClfrId':fsQoSClassMapClfrId,'fsQoSClassMapPreColor':fsQoSClassMapPreColor,'fsQoSClassMapVlanMapId':fsQoSClassMapVlanMapId,'fsQoSClassMapStatus':fsQoSClassMapStatus,'fsQoSClassToPriorityTable':fsQoSClassToPriorityTable,'fsQoSClassToPriorityEntry':fsQoSClassToPriorityEntry,_g:fsQoSClassToPriorityCLASS,'fsQoSClassToPriorityRegenPri':fsQoSClassToPriorityRegenPri,'fsQoSClassToPriorityGroupName':fsQoSClassToPriorityGroupName,'fsQoSClassToPriorityStatus':fsQoSClassToPriorityStatus,'fsQoSVlanMapTable':fsQoSVlanMapTable,'fsQoSVlanMapEntry':fsQoSVlanMapEntry,_h:fsQoSVlanMapID,'fsQoSVlanMapIfIndex':fsQoSVlanMapIfIndex,'fsQoSVlanMapVlanId':fsQoSVlanMapVlanId,'fsQoSVlanMapStatus':fsQoSVlanMapStatus,'fsQoSPortTable':fsQoSPortTable,'fsQoSPortEntry':fsQoSPortEntry,_i:fsQoSPcpPacketType,'fsQoSPcpSelRow':fsQoSPcpSelRow,'fsQoSPcpRowStatus':fsQoSPcpRowStatus,'fsQoSPolicy':fsQoSPolicy,'fsQoSMeterTable':fsQoSMeterTable,'fsQoSMeterEntry':fsQoSMeterEntry,_Y:fsQoSMeterId,'fsQoSMeterName':fsQoSMeterName,'fsQoSMeterType':fsQoSMeterType,'fsQoSMeterInterval':fsQoSMeterInterval,'fsQoSMeterColorMode':fsQoSMeterColorMode,'fsQoSMeterCIR':fsQoSMeterCIR,'fsQoSMeterCBS':fsQoSMeterCBS,'fsQoSMeterEIR':fsQoSMeterEIR,'fsQoSMeterEBS':fsQoSMeterEBS,'fsQoSMeterNext':fsQoSMeterNext,'fsQoSMeterStatus':fsQoSMeterStatus,'fsQoSPolicyMapTable':fsQoSPolicyMapTable,'fsQoSPolicyMapEntry':fsQoSPolicyMapEntry,_k:fsQoSPolicyMapId,'fsQoSPolicyMapName':fsQoSPolicyMapName,'fsQoSPolicyMapIfIndex':fsQoSPolicyMapIfIndex,'fsQoSPolicyMapCLASS':fsQoSPolicyMapCLASS,'fsQoSPolicyMapPHBType':fsQoSPolicyMapPHBType,'fsQoSPolicyMapDefaultPHB':fsQoSPolicyMapDefaultPHB,'fsQoSPolicyMapMeterTableId':fsQoSPolicyMapMeterTableId,'fsQoSPolicyMapFailMeterTableId':fsQoSPolicyMapFailMeterTableId,'fsQoSPolicyMapInProfileConformActionFlag':fsQoSPolicyMapInProfileConformActionFlag,'fsQoSPolicyMapInProfileConformActionId':fsQoSPolicyMapInProfileConformActionId,'fsQoSPolicyMapInProfileActionSetPort':fsQoSPolicyMapInProfileActionSetPort,'fsQoSPolicyMapConformActionSetIpTOS':fsQoSPolicyMapConformActionSetIpTOS,'fsQoSPolicyMapConformActionSetDscp':fsQoSPolicyMapConformActionSetDscp,'fsQoSPolicyMapConformActionSetVlanPrio':fsQoSPolicyMapConformActionSetVlanPrio,'fsQoSPolicyMapConformActionSetVlanDE':fsQoSPolicyMapConformActionSetVlanDE,'fsQoSPolicyMapConformActionSetInnerVlanPrio':fsQoSPolicyMapConformActionSetInnerVlanPrio,'fsQoSPolicyMapConformActionSetMplsExp':fsQoSPolicyMapConformActionSetMplsExp,'fsQoSPolicyMapConformActionSetNewCLASS':fsQoSPolicyMapConformActionSetNewCLASS,'fsQoSPolicyMapInProfileExceedActionFlag':fsQoSPolicyMapInProfileExceedActionFlag,'fsQoSPolicyMapInProfileExceedActionId':fsQoSPolicyMapInProfileExceedActionId,'fsQoSPolicyMapExceedActionSetIpTOS':fsQoSPolicyMapExceedActionSetIpTOS,'fsQoSPolicyMapExceedActionSetDscp':fsQoSPolicyMapExceedActionSetDscp,'fsQoSPolicyMapExceedActionSetInnerVlanPrio':fsQoSPolicyMapExceedActionSetInnerVlanPrio,'fsQoSPolicyMapExceedActionSetVlanPrio':fsQoSPolicyMapExceedActionSetVlanPrio,'fsQoSPolicyMapExceedActionSetVlanDE':fsQoSPolicyMapExceedActionSetVlanDE,'fsQoSPolicyMapExceedActionSetMplsExp':fsQoSPolicyMapExceedActionSetMplsExp,'fsQoSPolicyMapExceedActionSetNewCLASS':fsQoSPolicyMapExceedActionSetNewCLASS,'fsQoSPolicyMapOutProfileActionFlag':fsQoSPolicyMapOutProfileActionFlag,'fsQoSPolicyMapOutProfileActionId':fsQoSPolicyMapOutProfileActionId,'fsQoSPolicyMapOutProfileActionSetIPTOS':fsQoSPolicyMapOutProfileActionSetIPTOS,'fsQoSPolicyMapOutProfileActionSetDscp':fsQoSPolicyMapOutProfileActionSetDscp,'fsQoSPolicyMapOutProfileActionSetInnerVlanPrio':fsQoSPolicyMapOutProfileActionSetInnerVlanPrio,'fsQoSPolicyMapOutProfileActionSetVlanPrio':fsQoSPolicyMapOutProfileActionSetVlanPrio,'fsQoSPolicyMapOutProfileActionSetVlanDE':fsQoSPolicyMapOutProfileActionSetVlanDE,'fsQoSPolicyMapOutProfileActionSetMplsExp':fsQoSPolicyMapOutProfileActionSetMplsExp,'fsQoSPolicyMapOutProfileActionSetNewCLASS':fsQoSPolicyMapOutProfileActionSetNewCLASS,'fsQoSPolicyMapStatus':fsQoSPolicyMapStatus,'fsQoSPolicyMapConformActionSetInnerVlanDE':fsQoSPolicyMapConformActionSetInnerVlanDE,'fsQoSPolicyMapExceedActionSetInnerVlanDE':fsQoSPolicyMapExceedActionSetInnerVlanDE,'fsQoSPolicyMapOutProfileActionSetInnerVlanDE':fsQoSPolicyMapOutProfileActionSetInnerVlanDE,'fsQoSPolicyDefaultVlanDE':fsQoSPolicyDefaultVlanDE,'fsQoSTrafficMgmt':fsQoSTrafficMgmt,'fsQoSQTemplateTable':fsQoSQTemplateTable,'fsQoSQTemplateEntry':fsQoSQTemplateEntry,_Z:fsQoSQTemplateId,'fsQoSQTemplateName':fsQoSQTemplateName,'fsQoSQTemplateDropType':fsQoSQTemplateDropType,'fsQoSQTemplateDropAlgoEnableFlag':fsQoSQTemplateDropAlgoEnableFlag,'fsQoSQTemplateSize':fsQoSQTemplateSize,'fsQoSQTemplateStatus':fsQoSQTemplateStatus,'fsQoSRandomDetectCfgTable':fsQoSRandomDetectCfgTable,'fsQoSRandomDetectCfgEntry':fsQoSRandomDetectCfgEntry,_n:fsQoSRandomDetectCfgDP,'fsQoSRandomDetectCfgMinAvgThresh':fsQoSRandomDetectCfgMinAvgThresh,'fsQoSRandomDetectCfgMaxAvgThresh':fsQoSRandomDetectCfgMaxAvgThresh,'fsQoSRandomDetectCfgMaxPktSize':fsQoSRandomDetectCfgMaxPktSize,'fsQoSRandomDetectCfgMaxProb':fsQoSRandomDetectCfgMaxProb,'fsQoSRandomDetectCfgExpWeight':fsQoSRandomDetectCfgExpWeight,'fsQoSRandomDetectCfgStatus':fsQoSRandomDetectCfgStatus,'fsQoSRandomDetectCfgGain':fsQoSRandomDetectCfgGain,'fsQoSRandomDetectCfgDropThreshType':fsQoSRandomDetectCfgDropThreshType,'fsQoSRandomDetectCfgECNThresh':fsQoSRandomDetectCfgECNThresh,'fsQoSRandomDetectCfgActionFlag':fsQoSRandomDetectCfgActionFlag,'fsQoSShapeTemplateTable':fsQoSShapeTemplateTable,'fsQoSShapeTemplateEntry':fsQoSShapeTemplateEntry,_o:fsQoSShapeTemplateId,'fsQoSShapeTemplateName':fsQoSShapeTemplateName,'fsQoSShapeTemplateCIR':fsQoSShapeTemplateCIR,'fsQoSShapeTemplateCBS':fsQoSShapeTemplateCBS,'fsQoSShapeTemplateEIR':fsQoSShapeTemplateEIR,'fsQoSShapeTemplateEBS':fsQoSShapeTemplateEBS,'fsQoSShapeTemplateStatus':fsQoSShapeTemplateStatus,'fsQoSQMapTable':fsQoSQMapTable,'fsQoSQMapEntry':fsQoSQMapEntry,_p:fsQoSQMapCLASS,_q:fsQoSQMapRegenPriType,_r:fsQoSQMapRegenPriority,'fsQoSQMapQId':fsQoSQMapQId,'fsQoSQMapStatus':fsQoSQMapStatus,'fsQoSQMapRegenDEI':fsQoSQMapRegenDEI,'fsQoSQMapRegenColor':fsQoSQMapRegenColor,'fsQoSQTable':fsQoSQTable,'fsQoSQEntry':fsQoSQEntry,_s:fsQoSQId,'fsQoSQCfgTemplateId':fsQoSQCfgTemplateId,'fsQoSQSchedulerId':fsQoSQSchedulerId,'fsQoSQWeight':fsQoSQWeight,'fsQoSQPriority':fsQoSQPriority,'fsQoSQShapeId':fsQoSQShapeId,'fsQoSQStatus':fsQoSQStatus,'fsQoSQType':fsQoSQType,'fsQoSSchedulerTable':fsQoSSchedulerTable,'fsQoSSchedulerEntry':fsQoSSchedulerEntry,_b:fsQoSSchedulerId,'fsQoSSchedulerSchedAlgorithm':fsQoSSchedulerSchedAlgorithm,'fsQoSSchedulerShapeId':fsQoSSchedulerShapeId,'fsQoSSchedulerHierarchyLevel':fsQoSSchedulerHierarchyLevel,'fsQoSSchedulerGlobalId':fsQoSSchedulerGlobalId,'fsQoSSchedulerStatus':fsQoSSchedulerStatus,'fsQoSHierarchyTable':fsQoSHierarchyTable,'fsQoSHierarchyEntry':fsQoSHierarchyEntry,_t:fsQoSHierarchyLevel,'fsQoSHierarchyQNext':fsQoSHierarchyQNext,'fsQoSHierarchySchedNext':fsQoSHierarchySchedNext,'fsQoSHierarchyWeight':fsQoSHierarchyWeight,'fsQoSHierarchyPriority':fsQoSHierarchyPriority,'fsQoSHierarchyStatus':fsQoSHierarchyStatus,'fsQoSDefUserPriorityTable':fsQoSDefUserPriorityTable,'fsQoSDefUserPriorityEntry':fsQoSDefUserPriorityEntry,'fsQoSPortDefaultUserPriority':fsQoSPortDefaultUserPriority,'fsQoSPortPbitPrefOverDscp':fsQoSPortPbitPrefOverDscp,'fsQoSStats':fsQoSStats,'fsQoSPolicerStatsTable':fsQoSPolicerStatsTable,'fsQoSPolicerStatsEntry':fsQoSPolicerStatsEntry,'fsQoSPolicerStatsConformPkts':fsQoSPolicerStatsConformPkts,'fsQoSPolicerStatsConformOctets':fsQoSPolicerStatsConformOctets,'fsQoSPolicerStatsExceedPkts':fsQoSPolicerStatsExceedPkts,'fsQoSPolicerStatsExceedOctets':fsQoSPolicerStatsExceedOctets,'fsQoSPolicerStatsViolatePkts':fsQoSPolicerStatsViolatePkts,'fsQoSPolicerStatsViolateOctets':fsQoSPolicerStatsViolateOctets,'fsQoSPolicerStatsStatus':fsQoSPolicerStatsStatus,'fsQoSPolicerStatsClearCounter':fsQoSPolicerStatsClearCounter,'fsQoSCoSQStatsTable':fsQoSCoSQStatsTable,'fsQoSCoSQStatsEntry':fsQoSCoSQStatsEntry,_v:fsQoSCoSQId,'fsQoSCoSQStatsEnQPkts':fsQoSCoSQStatsEnQPkts,'fsQoSCoSQStatsEnQBytes':fsQoSCoSQStatsEnQBytes,'fsQoSCoSQStatsDeQPkts':fsQoSCoSQStatsDeQPkts,'fsQoSCoSQStatsDeQBytes':fsQoSCoSQStatsDeQBytes,'fsQoSCoSQStatsDiscardPkts':fsQoSCoSQStatsDiscardPkts,'fsQoSCoSQStatsDiscardBytes':fsQoSCoSQStatsDiscardBytes,'fsQoSCoSQStatsOccupancy':fsQoSCoSQStatsOccupancy,'fsQoSCoSQStatsCongMgntAlgoDrop':fsQoSCoSQStatsCongMgntAlgoDrop,'fsQosHwCpuRateControl':fsQosHwCpuRateControl,'fsQosHwCpuRateLimitTable':fsQosHwCpuRateLimitTable,'fsQosHwCpuRateLimitEntry':fsQosHwCpuRateLimitEntry,_w:fsQosHwCpuQId,'fsQosHwCpuMinRate':fsQosHwCpuMinRate,'fsQosHwCpuMaxRate':fsQosHwCpuMaxRate,'fsQosHwCpuRowStatus':fsQosHwCpuRowStatus})