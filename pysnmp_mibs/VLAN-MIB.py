_x='nbVlansRunPortMacLimitActionDescription'
_w='nbVlansRunPortMacLimitValue'
_v='nbVlansMacGetViewIndex'
_u='nbVlansPermPortMacLimitPortNumber'
_t='nbVlansPermVMANPortNumber'
_s='nbVlansPermSlotNumber'
_r='nbVlansPermPrior2VPTPriorNumber'
_q='nbVlansPermVPT2PriorVPTNumber'
_p='nbVlansPermIsvIndex'
_o='nbVlansPermPort'
_n='nbVlansPermSrvrPort'
_m='nbVlansPermMgmtTag'
_l='discardExceeded'
_k='portDisable'
_j='trapOnly'
_i='disable'
_h='enable'
_g='nbVlansRunVMANPortNumber'
_f='nbVlansRunSlotNumber'
_e='nbVlansRunPrior2VPTPriorNumber'
_d='nbVlansRunVPT2PriorVPTNumber'
_c='nbVlansRunIsvIndex'
_b='nonIsvp'
_a='tagAware'
_Z='access'
_Y='nbVlansRunPort'
_X='server'
_W='nonServer'
_V='nbVlansRunSrvrPort'
_U='nbVlansRunMgmtTag'
_T='isvpMode'
_S='vbcMode'
_R='noneVlan'
_Q='nbVlansRunPortMacLimitPortNumber'
_P='none'
_O='OctetString'
_N='enabled'
_M='disabled'
_L='perPort'
_K='perDeviceOnly'
_J='nonControl'
_I='other'
_H='invalid'
_G='valid'
_F='DisplayString'
_E='VLAN-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nbSwitchG1Il,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','nbSwitchG1Il')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class PortsBitmap(OctetString):0
_NbVlans_ObjectIdentity=ObjectIdentity
nbVlans=_NbVlans_ObjectIdentity((1,3,6,1,4,1,629,1,50,3))
_NbVlansRun_ObjectIdentity=ObjectIdentity
nbVlansRun=_NbVlansRun_ObjectIdentity((1,3,6,1,4,1,629,1,50,3,1))
class _NbVlansRunVlansMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3)))
_NbVlansRunVlansMode_Type.__name__=_C
_NbVlansRunVlansMode_Object=MibScalar
nbVlansRunVlansMode=_NbVlansRunVlansMode_Object((1,3,6,1,4,1,629,1,50,3,1,1),_NbVlansRunVlansMode_Type())
nbVlansRunVlansMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunVlansMode.setStatus(_A)
class _NbVlansRunIngressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_NbVlansRunIngressType_Type.__name__=_C
_NbVlansRunIngressType_Object=MibScalar
nbVlansRunIngressType=_NbVlansRunIngressType_Object((1,3,6,1,4,1,629,1,50,3,1,2),_NbVlansRunIngressType_Type())
nbVlansRunIngressType.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansRunIngressType.setStatus(_A)
class _NbVlansRunIngressMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_NbVlansRunIngressMode_Type.__name__=_C
_NbVlansRunIngressMode_Object=MibScalar
nbVlansRunIngressMode=_NbVlansRunIngressMode_Object((1,3,6,1,4,1,629,1,50,3,1,3),_NbVlansRunIngressMode_Type())
nbVlansRunIngressMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunIngressMode.setStatus(_A)
_NbVlansRunIngressPorts_Type=PortsBitmap
_NbVlansRunIngressPorts_Object=MibScalar
nbVlansRunIngressPorts=_NbVlansRunIngressPorts_Object((1,3,6,1,4,1,629,1,50,3,1,4),_NbVlansRunIngressPorts_Type())
nbVlansRunIngressPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunIngressPorts.setStatus(_A)
class _NbVlansRunEgressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_NbVlansRunEgressType_Type.__name__=_C
_NbVlansRunEgressType_Object=MibScalar
nbVlansRunEgressType=_NbVlansRunEgressType_Object((1,3,6,1,4,1,629,1,50,3,1,5),_NbVlansRunEgressType_Type())
nbVlansRunEgressType.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansRunEgressType.setStatus(_A)
class _NbVlansRunEgressMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_NbVlansRunEgressMode_Type.__name__=_C
_NbVlansRunEgressMode_Object=MibScalar
nbVlansRunEgressMode=_NbVlansRunEgressMode_Object((1,3,6,1,4,1,629,1,50,3,1,6),_NbVlansRunEgressMode_Type())
nbVlansRunEgressMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunEgressMode.setStatus(_A)
_NbVlansRunEgressPorts_Type=PortsBitmap
_NbVlansRunEgressPorts_Object=MibScalar
nbVlansRunEgressPorts=_NbVlansRunEgressPorts_Object((1,3,6,1,4,1,629,1,50,3,1,7),_NbVlansRunEgressPorts_Type())
nbVlansRunEgressPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunEgressPorts.setStatus(_A)
_NbVlansRunMgmtTable_Object=MibTable
nbVlansRunMgmtTable=_NbVlansRunMgmtTable_Object((1,3,6,1,4,1,629,1,50,3,1,8))
if mibBuilder.loadTexts:nbVlansRunMgmtTable.setStatus(_A)
_NbVlansRunMgmtEntry_Object=MibTableRow
nbVlansRunMgmtEntry=_NbVlansRunMgmtEntry_Object((1,3,6,1,4,1,629,1,50,3,1,8,1))
nbVlansRunMgmtEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:nbVlansRunMgmtEntry.setStatus(_A)
class _NbVlansRunMgmtTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4096))
_NbVlansRunMgmtTag_Type.__name__=_C
_NbVlansRunMgmtTag_Object=MibTableColumn
nbVlansRunMgmtTag=_NbVlansRunMgmtTag_Object((1,3,6,1,4,1,629,1,50,3,1,8,1,1),_NbVlansRunMgmtTag_Type())
nbVlansRunMgmtTag.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunMgmtTag.setStatus(_A)
_NbVlansRunMgmtList_Type=PortsBitmap
_NbVlansRunMgmtList_Object=MibTableColumn
nbVlansRunMgmtList=_NbVlansRunMgmtList_Object((1,3,6,1,4,1,629,1,50,3,1,8,1,2),_NbVlansRunMgmtList_Type())
nbVlansRunMgmtList.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunMgmtList.setStatus(_A)
class _NbVlansRunMgmtName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_NbVlansRunMgmtName_Type.__name__=_F
_NbVlansRunMgmtName_Object=MibTableColumn
nbVlansRunMgmtName=_NbVlansRunMgmtName_Object((1,3,6,1,4,1,629,1,50,3,1,8,1,3),_NbVlansRunMgmtName_Type())
nbVlansRunMgmtName.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunMgmtName.setStatus(_A)
class _NbVlansRunMgmtTagStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NbVlansRunMgmtTagStatus_Type.__name__=_C
_NbVlansRunMgmtTagStatus_Object=MibTableColumn
nbVlansRunMgmtTagStatus=_NbVlansRunMgmtTagStatus_Object((1,3,6,1,4,1,629,1,50,3,1,8,1,4),_NbVlansRunMgmtTagStatus_Type())
nbVlansRunMgmtTagStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunMgmtTagStatus.setStatus(_A)
_NbVlansRunSrvrTable_Object=MibTable
nbVlansRunSrvrTable=_NbVlansRunSrvrTable_Object((1,3,6,1,4,1,629,1,50,3,1,9))
if mibBuilder.loadTexts:nbVlansRunSrvrTable.setStatus(_A)
_NbVlansRunSrvrEntry_Object=MibTableRow
nbVlansRunSrvrEntry=_NbVlansRunSrvrEntry_Object((1,3,6,1,4,1,629,1,50,3,1,9,1))
nbVlansRunSrvrEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:nbVlansRunSrvrEntry.setStatus(_A)
_NbVlansRunSrvrPort_Type=Integer32
_NbVlansRunSrvrPort_Object=MibTableColumn
nbVlansRunSrvrPort=_NbVlansRunSrvrPort_Object((1,3,6,1,4,1,629,1,50,3,1,9,1,1),_NbVlansRunSrvrPort_Type())
nbVlansRunSrvrPort.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansRunSrvrPort.setStatus(_A)
class _NbVlansRunSrvrPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_NbVlansRunSrvrPortStatus_Type.__name__=_C
_NbVlansRunSrvrPortStatus_Object=MibTableColumn
nbVlansRunSrvrPortStatus=_NbVlansRunSrvrPortStatus_Object((1,3,6,1,4,1,629,1,50,3,1,9,1,2),_NbVlansRunSrvrPortStatus_Type())
nbVlansRunSrvrPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunSrvrPortStatus.setStatus(_A)
class _NbVlansRunSrvrPortTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4096))
_NbVlansRunSrvrPortTag_Type.__name__=_C
_NbVlansRunSrvrPortTag_Object=MibTableColumn
nbVlansRunSrvrPortTag=_NbVlansRunSrvrPortTag_Object((1,3,6,1,4,1,629,1,50,3,1,9,1,3),_NbVlansRunSrvrPortTag_Type())
nbVlansRunSrvrPortTag.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunSrvrPortTag.setStatus(_A)
_NbVlansRunPortsCfgTable_Object=MibTable
nbVlansRunPortsCfgTable=_NbVlansRunPortsCfgTable_Object((1,3,6,1,4,1,629,1,50,3,1,10))
if mibBuilder.loadTexts:nbVlansRunPortsCfgTable.setStatus(_A)
_NbVlansRunPortsCfgEntry_Object=MibTableRow
nbVlansRunPortsCfgEntry=_NbVlansRunPortsCfgEntry_Object((1,3,6,1,4,1,629,1,50,3,1,10,1))
nbVlansRunPortsCfgEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:nbVlansRunPortsCfgEntry.setStatus(_A)
_NbVlansRunPort_Type=Integer32
_NbVlansRunPort_Object=MibTableColumn
nbVlansRunPort=_NbVlansRunPort_Object((1,3,6,1,4,1,629,1,50,3,1,10,1,1),_NbVlansRunPort_Type())
nbVlansRunPort.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansRunPort.setStatus(_A)
class _NbVlansRunPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NbVlansRunPortPriority_Type.__name__=_C
_NbVlansRunPortPriority_Object=MibTableColumn
nbVlansRunPortPriority=_NbVlansRunPortPriority_Object((1,3,6,1,4,1,629,1,50,3,1,10,1,2),_NbVlansRunPortPriority_Type())
nbVlansRunPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunPortPriority.setStatus(_A)
class _NbVlansRunPortTagOutMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3)))
_NbVlansRunPortTagOutMode_Type.__name__=_C
_NbVlansRunPortTagOutMode_Object=MibTableColumn
nbVlansRunPortTagOutMode=_NbVlansRunPortTagOutMode_Object((1,3,6,1,4,1,629,1,50,3,1,10,1,3),_NbVlansRunPortTagOutMode_Type())
nbVlansRunPortTagOutMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunPortTagOutMode.setStatus(_A)
class _NbVlansRunPriorityPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_NbVlansRunPriorityPolicy_Type.__name__=_C
_NbVlansRunPriorityPolicy_Object=MibScalar
nbVlansRunPriorityPolicy=_NbVlansRunPriorityPolicy_Object((1,3,6,1,4,1,629,1,50,3,1,11),_NbVlansRunPriorityPolicy_Type())
nbVlansRunPriorityPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunPriorityPolicy.setStatus(_A)
_NbVlansRunIsvMaxNum_Type=Integer32
_NbVlansRunIsvMaxNum_Object=MibScalar
nbVlansRunIsvMaxNum=_NbVlansRunIsvMaxNum_Object((1,3,6,1,4,1,629,1,50,3,1,12),_NbVlansRunIsvMaxNum_Type())
nbVlansRunIsvMaxNum.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansRunIsvMaxNum.setStatus(_A)
_NbVlansRunIsvTable_Object=MibTable
nbVlansRunIsvTable=_NbVlansRunIsvTable_Object((1,3,6,1,4,1,629,1,50,3,1,13))
if mibBuilder.loadTexts:nbVlansRunIsvTable.setStatus(_A)
_NbVlansRunIsvEntry_Object=MibTableRow
nbVlansRunIsvEntry=_NbVlansRunIsvEntry_Object((1,3,6,1,4,1,629,1,50,3,1,13,1))
nbVlansRunIsvEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:nbVlansRunIsvEntry.setStatus(_A)
_NbVlansRunIsvIndex_Type=Integer32
_NbVlansRunIsvIndex_Object=MibTableColumn
nbVlansRunIsvIndex=_NbVlansRunIsvIndex_Object((1,3,6,1,4,1,629,1,50,3,1,13,1,1),_NbVlansRunIsvIndex_Type())
nbVlansRunIsvIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansRunIsvIndex.setStatus(_A)
class _NbVlansRunIsvStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),('mcast',3)))
_NbVlansRunIsvStatus_Type.__name__=_C
_NbVlansRunIsvStatus_Object=MibTableColumn
nbVlansRunIsvStatus=_NbVlansRunIsvStatus_Object((1,3,6,1,4,1,629,1,50,3,1,13,1,2),_NbVlansRunIsvStatus_Type())
nbVlansRunIsvStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunIsvStatus.setStatus(_A)
class _NbVlansRunIsvList_Type(OctetString):defaultHexValue='ffff'
_NbVlansRunIsvList_Type.__name__=_O
_NbVlansRunIsvList_Object=MibTableColumn
nbVlansRunIsvList=_NbVlansRunIsvList_Object((1,3,6,1,4,1,629,1,50,3,1,13,1,3),_NbVlansRunIsvList_Type())
nbVlansRunIsvList.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunIsvList.setStatus(_A)
class _NbVlansRunIsvName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_NbVlansRunIsvName_Type.__name__=_F
_NbVlansRunIsvName_Object=MibTableColumn
nbVlansRunIsvName=_NbVlansRunIsvName_Object((1,3,6,1,4,1,629,1,50,3,1,13,1,4),_NbVlansRunIsvName_Type())
nbVlansRunIsvName.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunIsvName.setStatus(_A)
class _NbVlansRunIsvTag_Type(Integer32):defaultValue=1
_NbVlansRunIsvTag_Type.__name__=_C
_NbVlansRunIsvTag_Object=MibTableColumn
nbVlansRunIsvTag=_NbVlansRunIsvTag_Object((1,3,6,1,4,1,629,1,50,3,1,13,1,5),_NbVlansRunIsvTag_Type())
nbVlansRunIsvTag.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunIsvTag.setStatus(_A)
_NbVlansRunIsvVlanIndex_Type=Integer32
_NbVlansRunIsvVlanIndex_Object=MibTableColumn
nbVlansRunIsvVlanIndex=_NbVlansRunIsvVlanIndex_Object((1,3,6,1,4,1,629,1,50,3,1,13,1,6),_NbVlansRunIsvVlanIndex_Type())
nbVlansRunIsvVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansRunIsvVlanIndex.setStatus(_A)
class _NbVlansRunIsvVlanPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NbVlansRunIsvVlanPriority_Type.__name__=_C
_NbVlansRunIsvVlanPriority_Object=MibTableColumn
nbVlansRunIsvVlanPriority=_NbVlansRunIsvVlanPriority_Object((1,3,6,1,4,1,629,1,50,3,1,13,1,7),_NbVlansRunIsvVlanPriority_Type())
nbVlansRunIsvVlanPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunIsvVlanPriority.setStatus(_A)
_NbVlansRunVPT2PriorityTable_Object=MibTable
nbVlansRunVPT2PriorityTable=_NbVlansRunVPT2PriorityTable_Object((1,3,6,1,4,1,629,1,50,3,1,15))
if mibBuilder.loadTexts:nbVlansRunVPT2PriorityTable.setStatus(_A)
_NbVlansRunVPT2PriorityEntry_Object=MibTableRow
nbVlansRunVPT2PriorityEntry=_NbVlansRunVPT2PriorityEntry_Object((1,3,6,1,4,1,629,1,50,3,1,15,1))
nbVlansRunVPT2PriorityEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:nbVlansRunVPT2PriorityEntry.setStatus(_A)
class _NbVlansRunVPT2PriorVPTNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_NbVlansRunVPT2PriorVPTNumber_Type.__name__=_C
_NbVlansRunVPT2PriorVPTNumber_Object=MibTableColumn
nbVlansRunVPT2PriorVPTNumber=_NbVlansRunVPT2PriorVPTNumber_Object((1,3,6,1,4,1,629,1,50,3,1,15,1,1),_NbVlansRunVPT2PriorVPTNumber_Type())
nbVlansRunVPT2PriorVPTNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansRunVPT2PriorVPTNumber.setStatus(_A)
class _NbVlansRunVPT2PriorPriorNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_NbVlansRunVPT2PriorPriorNumber_Type.__name__=_C
_NbVlansRunVPT2PriorPriorNumber_Object=MibTableColumn
nbVlansRunVPT2PriorPriorNumber=_NbVlansRunVPT2PriorPriorNumber_Object((1,3,6,1,4,1,629,1,50,3,1,15,1,2),_NbVlansRunVPT2PriorPriorNumber_Type())
nbVlansRunVPT2PriorPriorNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunVPT2PriorPriorNumber.setStatus(_A)
_NbVlansRunPriority2VPTTable_Object=MibTable
nbVlansRunPriority2VPTTable=_NbVlansRunPriority2VPTTable_Object((1,3,6,1,4,1,629,1,50,3,1,16))
if mibBuilder.loadTexts:nbVlansRunPriority2VPTTable.setStatus(_A)
_NbVlansRunPriority2VPTEntry_Object=MibTableRow
nbVlansRunPriority2VPTEntry=_NbVlansRunPriority2VPTEntry_Object((1,3,6,1,4,1,629,1,50,3,1,16,1))
nbVlansRunPriority2VPTEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:nbVlansRunPriority2VPTEntry.setStatus(_A)
class _NbVlansRunPrior2VPTPriorNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_NbVlansRunPrior2VPTPriorNumber_Type.__name__=_C
_NbVlansRunPrior2VPTPriorNumber_Object=MibTableColumn
nbVlansRunPrior2VPTPriorNumber=_NbVlansRunPrior2VPTPriorNumber_Object((1,3,6,1,4,1,629,1,50,3,1,16,1,1),_NbVlansRunPrior2VPTPriorNumber_Type())
nbVlansRunPrior2VPTPriorNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansRunPrior2VPTPriorNumber.setStatus(_A)
class _NbVlansRunPrior2VPTVPTNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_NbVlansRunPrior2VPTVPTNumber_Type.__name__=_C
_NbVlansRunPrior2VPTVPTNumber_Object=MibTableColumn
nbVlansRunPrior2VPTVPTNumber=_NbVlansRunPrior2VPTVPTNumber_Object((1,3,6,1,4,1,629,1,50,3,1,16,1,2),_NbVlansRunPrior2VPTVPTNumber_Type())
nbVlansRunPrior2VPTVPTNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunPrior2VPTVPTNumber.setStatus(_A)
_NbVlansRunSlotEtherTypeTable_Object=MibTable
nbVlansRunSlotEtherTypeTable=_NbVlansRunSlotEtherTypeTable_Object((1,3,6,1,4,1,629,1,50,3,1,20))
if mibBuilder.loadTexts:nbVlansRunSlotEtherTypeTable.setStatus(_A)
_NbVlansRunSlotEtherTypeEntry_Object=MibTableRow
nbVlansRunSlotEtherTypeEntry=_NbVlansRunSlotEtherTypeEntry_Object((1,3,6,1,4,1,629,1,50,3,1,20,1))
nbVlansRunSlotEtherTypeEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:nbVlansRunSlotEtherTypeEntry.setStatus(_A)
_NbVlansRunSlotNumber_Type=Integer32
_NbVlansRunSlotNumber_Object=MibTableColumn
nbVlansRunSlotNumber=_NbVlansRunSlotNumber_Object((1,3,6,1,4,1,629,1,50,3,1,20,1,1),_NbVlansRunSlotNumber_Type())
nbVlansRunSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansRunSlotNumber.setStatus(_A)
class _NbVlansRunSlotEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NbVlansRunSlotEtherType_Type.__name__=_C
_NbVlansRunSlotEtherType_Object=MibTableColumn
nbVlansRunSlotEtherType=_NbVlansRunSlotEtherType_Object((1,3,6,1,4,1,629,1,50,3,1,20,1,2),_NbVlansRunSlotEtherType_Type())
nbVlansRunSlotEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunSlotEtherType.setStatus(_A)
_NbVlansRunVMANPortTable_Object=MibTable
nbVlansRunVMANPortTable=_NbVlansRunVMANPortTable_Object((1,3,6,1,4,1,629,1,50,3,1,22))
if mibBuilder.loadTexts:nbVlansRunVMANPortTable.setStatus(_A)
_NbVlansRunVMANPortEntry_Object=MibTableRow
nbVlansRunVMANPortEntry=_NbVlansRunVMANPortEntry_Object((1,3,6,1,4,1,629,1,50,3,1,22,1))
nbVlansRunVMANPortEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:nbVlansRunVMANPortEntry.setStatus(_A)
_NbVlansRunVMANPortNumber_Type=Integer32
_NbVlansRunVMANPortNumber_Object=MibTableColumn
nbVlansRunVMANPortNumber=_NbVlansRunVMANPortNumber_Object((1,3,6,1,4,1,629,1,50,3,1,22,1,1),_NbVlansRunVMANPortNumber_Type())
nbVlansRunVMANPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansRunVMANPortNumber.setStatus(_A)
class _NbVlansRunVMANPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_h,2),(_i,3)))
_NbVlansRunVMANPortMode_Type.__name__=_C
_NbVlansRunVMANPortMode_Object=MibTableColumn
nbVlansRunVMANPortMode=_NbVlansRunVMANPortMode_Object((1,3,6,1,4,1,629,1,50,3,1,22,1,2),_NbVlansRunVMANPortMode_Type())
nbVlansRunVMANPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunVMANPortMode.setStatus(_A)
class _NbVlansRunCPUEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NbVlansRunCPUEtherType_Type.__name__=_C
_NbVlansRunCPUEtherType_Object=MibScalar
nbVlansRunCPUEtherType=_NbVlansRunCPUEtherType_Object((1,3,6,1,4,1,629,1,50,3,1,23),_NbVlansRunCPUEtherType_Type())
nbVlansRunCPUEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunCPUEtherType.setStatus(_A)
_NbVlansRunMacLimitGroup_ObjectIdentity=ObjectIdentity
nbVlansRunMacLimitGroup=_NbVlansRunMacLimitGroup_ObjectIdentity((1,3,6,1,4,1,629,1,50,3,1,24))
class _NbVlansRunPortMacLimitActionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),(_j,2),(_k,3),(_l,4)))
_NbVlansRunPortMacLimitActionMode_Type.__name__=_C
_NbVlansRunPortMacLimitActionMode_Object=MibScalar
nbVlansRunPortMacLimitActionMode=_NbVlansRunPortMacLimitActionMode_Object((1,3,6,1,4,1,629,1,50,3,1,24,1),_NbVlansRunPortMacLimitActionMode_Type())
nbVlansRunPortMacLimitActionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunPortMacLimitActionMode.setStatus(_A)
_NbVlansRunPortMacLimitActionDescription_Type=DisplayString
_NbVlansRunPortMacLimitActionDescription_Object=MibScalar
nbVlansRunPortMacLimitActionDescription=_NbVlansRunPortMacLimitActionDescription_Object((1,3,6,1,4,1,629,1,50,3,1,24,2),_NbVlansRunPortMacLimitActionDescription_Type())
nbVlansRunPortMacLimitActionDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansRunPortMacLimitActionDescription.setStatus(_A)
_NbVlansRunPortMacLimitTable_Object=MibTable
nbVlansRunPortMacLimitTable=_NbVlansRunPortMacLimitTable_Object((1,3,6,1,4,1,629,1,50,3,1,24,10))
if mibBuilder.loadTexts:nbVlansRunPortMacLimitTable.setStatus(_A)
_NbVlansRunPortMacLimitEntry_Object=MibTableRow
nbVlansRunPortMacLimitEntry=_NbVlansRunPortMacLimitEntry_Object((1,3,6,1,4,1,629,1,50,3,1,24,10,1))
nbVlansRunPortMacLimitEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:nbVlansRunPortMacLimitEntry.setStatus(_A)
_NbVlansRunPortMacLimitPortNumber_Type=Integer32
_NbVlansRunPortMacLimitPortNumber_Object=MibTableColumn
nbVlansRunPortMacLimitPortNumber=_NbVlansRunPortMacLimitPortNumber_Object((1,3,6,1,4,1,629,1,50,3,1,24,10,1,1),_NbVlansRunPortMacLimitPortNumber_Type())
nbVlansRunPortMacLimitPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansRunPortMacLimitPortNumber.setStatus(_A)
_NbVlansRunPortMacLimitValue_Type=Integer32
_NbVlansRunPortMacLimitValue_Object=MibTableColumn
nbVlansRunPortMacLimitValue=_NbVlansRunPortMacLimitValue_Object((1,3,6,1,4,1,629,1,50,3,1,24,10,1,2),_NbVlansRunPortMacLimitValue_Type())
nbVlansRunPortMacLimitValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansRunPortMacLimitValue.setStatus(_A)
_NbVlansPerm_ObjectIdentity=ObjectIdentity
nbVlansPerm=_NbVlansPerm_ObjectIdentity((1,3,6,1,4,1,629,1,50,3,2))
class _NbVlansPermVlansMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3)))
_NbVlansPermVlansMode_Type.__name__=_C
_NbVlansPermVlansMode_Object=MibScalar
nbVlansPermVlansMode=_NbVlansPermVlansMode_Object((1,3,6,1,4,1,629,1,50,3,2,1),_NbVlansPermVlansMode_Type())
nbVlansPermVlansMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermVlansMode.setStatus(_A)
class _NbVlansPermIngressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_NbVlansPermIngressType_Type.__name__=_C
_NbVlansPermIngressType_Object=MibScalar
nbVlansPermIngressType=_NbVlansPermIngressType_Object((1,3,6,1,4,1,629,1,50,3,2,2),_NbVlansPermIngressType_Type())
nbVlansPermIngressType.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansPermIngressType.setStatus(_A)
class _NbVlansPermIngressMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_NbVlansPermIngressMode_Type.__name__=_C
_NbVlansPermIngressMode_Object=MibScalar
nbVlansPermIngressMode=_NbVlansPermIngressMode_Object((1,3,6,1,4,1,629,1,50,3,2,3),_NbVlansPermIngressMode_Type())
nbVlansPermIngressMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermIngressMode.setStatus(_A)
_NbVlansPermIngressPorts_Type=PortsBitmap
_NbVlansPermIngressPorts_Object=MibScalar
nbVlansPermIngressPorts=_NbVlansPermIngressPorts_Object((1,3,6,1,4,1,629,1,50,3,2,4),_NbVlansPermIngressPorts_Type())
nbVlansPermIngressPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermIngressPorts.setStatus(_A)
class _NbVlansPermEgressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_NbVlansPermEgressType_Type.__name__=_C
_NbVlansPermEgressType_Object=MibScalar
nbVlansPermEgressType=_NbVlansPermEgressType_Object((1,3,6,1,4,1,629,1,50,3,2,5),_NbVlansPermEgressType_Type())
nbVlansPermEgressType.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansPermEgressType.setStatus(_A)
class _NbVlansPermEgressMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_NbVlansPermEgressMode_Type.__name__=_C
_NbVlansPermEgressMode_Object=MibScalar
nbVlansPermEgressMode=_NbVlansPermEgressMode_Object((1,3,6,1,4,1,629,1,50,3,2,6),_NbVlansPermEgressMode_Type())
nbVlansPermEgressMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermEgressMode.setStatus(_A)
_NbVlansPermEgressPorts_Type=PortsBitmap
_NbVlansPermEgressPorts_Object=MibScalar
nbVlansPermEgressPorts=_NbVlansPermEgressPorts_Object((1,3,6,1,4,1,629,1,50,3,2,7),_NbVlansPermEgressPorts_Type())
nbVlansPermEgressPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermEgressPorts.setStatus(_A)
_NbVlansPermMgmtTable_Object=MibTable
nbVlansPermMgmtTable=_NbVlansPermMgmtTable_Object((1,3,6,1,4,1,629,1,50,3,2,8))
if mibBuilder.loadTexts:nbVlansPermMgmtTable.setStatus(_A)
_NbVlansPermMgmtEntry_Object=MibTableRow
nbVlansPermMgmtEntry=_NbVlansPermMgmtEntry_Object((1,3,6,1,4,1,629,1,50,3,2,8,1))
nbVlansPermMgmtEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:nbVlansPermMgmtEntry.setStatus(_A)
class _NbVlansPermMgmtTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4096))
_NbVlansPermMgmtTag_Type.__name__=_C
_NbVlansPermMgmtTag_Object=MibTableColumn
nbVlansPermMgmtTag=_NbVlansPermMgmtTag_Object((1,3,6,1,4,1,629,1,50,3,2,8,1,1),_NbVlansPermMgmtTag_Type())
nbVlansPermMgmtTag.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermMgmtTag.setStatus(_A)
_NbVlansPermMgmtList_Type=PortsBitmap
_NbVlansPermMgmtList_Object=MibTableColumn
nbVlansPermMgmtList=_NbVlansPermMgmtList_Object((1,3,6,1,4,1,629,1,50,3,2,8,1,2),_NbVlansPermMgmtList_Type())
nbVlansPermMgmtList.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermMgmtList.setStatus(_A)
class _NbVlansPermMgmtName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_NbVlansPermMgmtName_Type.__name__=_F
_NbVlansPermMgmtName_Object=MibTableColumn
nbVlansPermMgmtName=_NbVlansPermMgmtName_Object((1,3,6,1,4,1,629,1,50,3,2,8,1,3),_NbVlansPermMgmtName_Type())
nbVlansPermMgmtName.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermMgmtName.setStatus(_A)
class _NbVlansPermMgmtTagStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NbVlansPermMgmtTagStatus_Type.__name__=_C
_NbVlansPermMgmtTagStatus_Object=MibTableColumn
nbVlansPermMgmtTagStatus=_NbVlansPermMgmtTagStatus_Object((1,3,6,1,4,1,629,1,50,3,2,8,1,4),_NbVlansPermMgmtTagStatus_Type())
nbVlansPermMgmtTagStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermMgmtTagStatus.setStatus(_A)
_NbVlansPermSrvrTable_Object=MibTable
nbVlansPermSrvrTable=_NbVlansPermSrvrTable_Object((1,3,6,1,4,1,629,1,50,3,2,9))
if mibBuilder.loadTexts:nbVlansPermSrvrTable.setStatus(_A)
_NbVlansPermSrvrEntry_Object=MibTableRow
nbVlansPermSrvrEntry=_NbVlansPermSrvrEntry_Object((1,3,6,1,4,1,629,1,50,3,2,9,1))
nbVlansPermSrvrEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:nbVlansPermSrvrEntry.setStatus(_A)
_NbVlansPermSrvrPort_Type=Integer32
_NbVlansPermSrvrPort_Object=MibTableColumn
nbVlansPermSrvrPort=_NbVlansPermSrvrPort_Object((1,3,6,1,4,1,629,1,50,3,2,9,1,1),_NbVlansPermSrvrPort_Type())
nbVlansPermSrvrPort.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansPermSrvrPort.setStatus(_A)
class _NbVlansPermSrvrPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_NbVlansPermSrvrPortStatus_Type.__name__=_C
_NbVlansPermSrvrPortStatus_Object=MibTableColumn
nbVlansPermSrvrPortStatus=_NbVlansPermSrvrPortStatus_Object((1,3,6,1,4,1,629,1,50,3,2,9,1,2),_NbVlansPermSrvrPortStatus_Type())
nbVlansPermSrvrPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermSrvrPortStatus.setStatus(_A)
class _NbVlansPermSrvrPortTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4096))
_NbVlansPermSrvrPortTag_Type.__name__=_C
_NbVlansPermSrvrPortTag_Object=MibTableColumn
nbVlansPermSrvrPortTag=_NbVlansPermSrvrPortTag_Object((1,3,6,1,4,1,629,1,50,3,2,9,1,3),_NbVlansPermSrvrPortTag_Type())
nbVlansPermSrvrPortTag.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermSrvrPortTag.setStatus(_A)
_NbVlansPermPortsCfgTable_Object=MibTable
nbVlansPermPortsCfgTable=_NbVlansPermPortsCfgTable_Object((1,3,6,1,4,1,629,1,50,3,2,10))
if mibBuilder.loadTexts:nbVlansPermPortsCfgTable.setStatus(_A)
_NbVlansPermPortsCfgEntry_Object=MibTableRow
nbVlansPermPortsCfgEntry=_NbVlansPermPortsCfgEntry_Object((1,3,6,1,4,1,629,1,50,3,2,10,1))
nbVlansPermPortsCfgEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:nbVlansPermPortsCfgEntry.setStatus(_A)
_NbVlansPermPort_Type=Integer32
_NbVlansPermPort_Object=MibTableColumn
nbVlansPermPort=_NbVlansPermPort_Object((1,3,6,1,4,1,629,1,50,3,2,10,1,1),_NbVlansPermPort_Type())
nbVlansPermPort.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansPermPort.setStatus(_A)
class _NbVlansPermPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NbVlansPermPortPriority_Type.__name__=_C
_NbVlansPermPortPriority_Object=MibTableColumn
nbVlansPermPortPriority=_NbVlansPermPortPriority_Object((1,3,6,1,4,1,629,1,50,3,2,10,1,2),_NbVlansPermPortPriority_Type())
nbVlansPermPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermPortPriority.setStatus(_A)
class _NbVlansPermPortTagOutMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3)))
_NbVlansPermPortTagOutMode_Type.__name__=_C
_NbVlansPermPortTagOutMode_Object=MibTableColumn
nbVlansPermPortTagOutMode=_NbVlansPermPortTagOutMode_Object((1,3,6,1,4,1,629,1,50,3,2,10,1,3),_NbVlansPermPortTagOutMode_Type())
nbVlansPermPortTagOutMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermPortTagOutMode.setStatus(_A)
class _NbVlansPermPriorityPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_NbVlansPermPriorityPolicy_Type.__name__=_C
_NbVlansPermPriorityPolicy_Object=MibScalar
nbVlansPermPriorityPolicy=_NbVlansPermPriorityPolicy_Object((1,3,6,1,4,1,629,1,50,3,2,11),_NbVlansPermPriorityPolicy_Type())
nbVlansPermPriorityPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermPriorityPolicy.setStatus(_A)
_NbVlansPermIsvMaxNum_Type=Integer32
_NbVlansPermIsvMaxNum_Object=MibScalar
nbVlansPermIsvMaxNum=_NbVlansPermIsvMaxNum_Object((1,3,6,1,4,1,629,1,50,3,2,12),_NbVlansPermIsvMaxNum_Type())
nbVlansPermIsvMaxNum.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansPermIsvMaxNum.setStatus(_A)
_NbVlansPermIsvTable_Object=MibTable
nbVlansPermIsvTable=_NbVlansPermIsvTable_Object((1,3,6,1,4,1,629,1,50,3,2,13))
if mibBuilder.loadTexts:nbVlansPermIsvTable.setStatus(_A)
_NbVlansPermIsvEntry_Object=MibTableRow
nbVlansPermIsvEntry=_NbVlansPermIsvEntry_Object((1,3,6,1,4,1,629,1,50,3,2,13,1))
nbVlansPermIsvEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:nbVlansPermIsvEntry.setStatus(_A)
_NbVlansPermIsvIndex_Type=Integer32
_NbVlansPermIsvIndex_Object=MibTableColumn
nbVlansPermIsvIndex=_NbVlansPermIsvIndex_Object((1,3,6,1,4,1,629,1,50,3,2,13,1,1),_NbVlansPermIsvIndex_Type())
nbVlansPermIsvIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansPermIsvIndex.setStatus(_A)
class _NbVlansPermIsvStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),('mcast',3)))
_NbVlansPermIsvStatus_Type.__name__=_C
_NbVlansPermIsvStatus_Object=MibTableColumn
nbVlansPermIsvStatus=_NbVlansPermIsvStatus_Object((1,3,6,1,4,1,629,1,50,3,2,13,1,2),_NbVlansPermIsvStatus_Type())
nbVlansPermIsvStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermIsvStatus.setStatus(_A)
class _NbVlansPermIsvList_Type(OctetString):defaultHexValue='ffff'
_NbVlansPermIsvList_Type.__name__=_O
_NbVlansPermIsvList_Object=MibTableColumn
nbVlansPermIsvList=_NbVlansPermIsvList_Object((1,3,6,1,4,1,629,1,50,3,2,13,1,3),_NbVlansPermIsvList_Type())
nbVlansPermIsvList.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermIsvList.setStatus(_A)
class _NbVlansPermIsvName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_NbVlansPermIsvName_Type.__name__=_F
_NbVlansPermIsvName_Object=MibTableColumn
nbVlansPermIsvName=_NbVlansPermIsvName_Object((1,3,6,1,4,1,629,1,50,3,2,13,1,4),_NbVlansPermIsvName_Type())
nbVlansPermIsvName.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermIsvName.setStatus(_A)
class _NbVlansPermIsvTag_Type(Integer32):defaultValue=1
_NbVlansPermIsvTag_Type.__name__=_C
_NbVlansPermIsvTag_Object=MibTableColumn
nbVlansPermIsvTag=_NbVlansPermIsvTag_Object((1,3,6,1,4,1,629,1,50,3,2,13,1,5),_NbVlansPermIsvTag_Type())
nbVlansPermIsvTag.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermIsvTag.setStatus(_A)
class _NbVlansPermIsvVlanPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NbVlansPermIsvVlanPriority_Type.__name__=_C
_NbVlansPermIsvVlanPriority_Object=MibTableColumn
nbVlansPermIsvVlanPriority=_NbVlansPermIsvVlanPriority_Object((1,3,6,1,4,1,629,1,50,3,2,13,1,6),_NbVlansPermIsvVlanPriority_Type())
nbVlansPermIsvVlanPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermIsvVlanPriority.setStatus(_A)
_NbVlansPermVPT2PriorityTable_Object=MibTable
nbVlansPermVPT2PriorityTable=_NbVlansPermVPT2PriorityTable_Object((1,3,6,1,4,1,629,1,50,3,2,15))
if mibBuilder.loadTexts:nbVlansPermVPT2PriorityTable.setStatus(_A)
_NbVlansPermVPT2PriorityEntry_Object=MibTableRow
nbVlansPermVPT2PriorityEntry=_NbVlansPermVPT2PriorityEntry_Object((1,3,6,1,4,1,629,1,50,3,2,15,1))
nbVlansPermVPT2PriorityEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:nbVlansPermVPT2PriorityEntry.setStatus(_A)
class _NbVlansPermVPT2PriorVPTNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_NbVlansPermVPT2PriorVPTNumber_Type.__name__=_C
_NbVlansPermVPT2PriorVPTNumber_Object=MibTableColumn
nbVlansPermVPT2PriorVPTNumber=_NbVlansPermVPT2PriorVPTNumber_Object((1,3,6,1,4,1,629,1,50,3,2,15,1,1),_NbVlansPermVPT2PriorVPTNumber_Type())
nbVlansPermVPT2PriorVPTNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansPermVPT2PriorVPTNumber.setStatus(_A)
class _NbVlansPermVPT2PriorPriorNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_NbVlansPermVPT2PriorPriorNumber_Type.__name__=_C
_NbVlansPermVPT2PriorPriorNumber_Object=MibTableColumn
nbVlansPermVPT2PriorPriorNumber=_NbVlansPermVPT2PriorPriorNumber_Object((1,3,6,1,4,1,629,1,50,3,2,15,1,2),_NbVlansPermVPT2PriorPriorNumber_Type())
nbVlansPermVPT2PriorPriorNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermVPT2PriorPriorNumber.setStatus(_A)
_NbVlansPermPriority2VPTTable_Object=MibTable
nbVlansPermPriority2VPTTable=_NbVlansPermPriority2VPTTable_Object((1,3,6,1,4,1,629,1,50,3,2,16))
if mibBuilder.loadTexts:nbVlansPermPriority2VPTTable.setStatus(_A)
_NbVlansPermPriority2VPTEntry_Object=MibTableRow
nbVlansPermPriority2VPTEntry=_NbVlansPermPriority2VPTEntry_Object((1,3,6,1,4,1,629,1,50,3,2,16,1))
nbVlansPermPriority2VPTEntry.setIndexNames((0,_E,_r))
if mibBuilder.loadTexts:nbVlansPermPriority2VPTEntry.setStatus(_A)
class _NbVlansPermPrior2VPTPriorNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_NbVlansPermPrior2VPTPriorNumber_Type.__name__=_C
_NbVlansPermPrior2VPTPriorNumber_Object=MibTableColumn
nbVlansPermPrior2VPTPriorNumber=_NbVlansPermPrior2VPTPriorNumber_Object((1,3,6,1,4,1,629,1,50,3,2,16,1,1),_NbVlansPermPrior2VPTPriorNumber_Type())
nbVlansPermPrior2VPTPriorNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansPermPrior2VPTPriorNumber.setStatus(_A)
class _NbVlansPermPrior2VPTVPTNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_NbVlansPermPrior2VPTVPTNumber_Type.__name__=_C
_NbVlansPermPrior2VPTVPTNumber_Object=MibTableColumn
nbVlansPermPrior2VPTVPTNumber=_NbVlansPermPrior2VPTVPTNumber_Object((1,3,6,1,4,1,629,1,50,3,2,16,1,2),_NbVlansPermPrior2VPTVPTNumber_Type())
nbVlansPermPrior2VPTVPTNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermPrior2VPTVPTNumber.setStatus(_A)
_NbVlansPermSlotEtherTypeTable_Object=MibTable
nbVlansPermSlotEtherTypeTable=_NbVlansPermSlotEtherTypeTable_Object((1,3,6,1,4,1,629,1,50,3,2,20))
if mibBuilder.loadTexts:nbVlansPermSlotEtherTypeTable.setStatus(_A)
_NbVlansPermSlotEtherTypeEntry_Object=MibTableRow
nbVlansPermSlotEtherTypeEntry=_NbVlansPermSlotEtherTypeEntry_Object((1,3,6,1,4,1,629,1,50,3,2,20,1))
nbVlansPermSlotEtherTypeEntry.setIndexNames((0,_E,_s))
if mibBuilder.loadTexts:nbVlansPermSlotEtherTypeEntry.setStatus(_A)
_NbVlansPermSlotNumber_Type=Integer32
_NbVlansPermSlotNumber_Object=MibTableColumn
nbVlansPermSlotNumber=_NbVlansPermSlotNumber_Object((1,3,6,1,4,1,629,1,50,3,2,20,1,1),_NbVlansPermSlotNumber_Type())
nbVlansPermSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansPermSlotNumber.setStatus(_A)
class _NbVlansPermSlotEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NbVlansPermSlotEtherType_Type.__name__=_C
_NbVlansPermSlotEtherType_Object=MibTableColumn
nbVlansPermSlotEtherType=_NbVlansPermSlotEtherType_Object((1,3,6,1,4,1,629,1,50,3,2,20,1,2),_NbVlansPermSlotEtherType_Type())
nbVlansPermSlotEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermSlotEtherType.setStatus(_A)
_NbVlansPermVMANPortTable_Object=MibTable
nbVlansPermVMANPortTable=_NbVlansPermVMANPortTable_Object((1,3,6,1,4,1,629,1,50,3,2,22))
if mibBuilder.loadTexts:nbVlansPermVMANPortTable.setStatus(_A)
_NbVlansPermVMANPortEntry_Object=MibTableRow
nbVlansPermVMANPortEntry=_NbVlansPermVMANPortEntry_Object((1,3,6,1,4,1,629,1,50,3,2,22,1))
nbVlansPermVMANPortEntry.setIndexNames((0,_E,_t))
if mibBuilder.loadTexts:nbVlansPermVMANPortEntry.setStatus(_A)
_NbVlansPermVMANPortNumber_Type=Integer32
_NbVlansPermVMANPortNumber_Object=MibTableColumn
nbVlansPermVMANPortNumber=_NbVlansPermVMANPortNumber_Object((1,3,6,1,4,1,629,1,50,3,2,22,1,1),_NbVlansPermVMANPortNumber_Type())
nbVlansPermVMANPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansPermVMANPortNumber.setStatus(_A)
class _NbVlansPermVMANPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_h,2),(_i,3)))
_NbVlansPermVMANPortMode_Type.__name__=_C
_NbVlansPermVMANPortMode_Object=MibTableColumn
nbVlansPermVMANPortMode=_NbVlansPermVMANPortMode_Object((1,3,6,1,4,1,629,1,50,3,2,22,1,2),_NbVlansPermVMANPortMode_Type())
nbVlansPermVMANPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermVMANPortMode.setStatus(_A)
class _NbVlansPermCPUEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NbVlansPermCPUEtherType_Type.__name__=_C
_NbVlansPermCPUEtherType_Object=MibScalar
nbVlansPermCPUEtherType=_NbVlansPermCPUEtherType_Object((1,3,6,1,4,1,629,1,50,3,2,23),_NbVlansPermCPUEtherType_Type())
nbVlansPermCPUEtherType.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansPermCPUEtherType.setStatus(_A)
_NbVlansPermMacLimitGroup_ObjectIdentity=ObjectIdentity
nbVlansPermMacLimitGroup=_NbVlansPermMacLimitGroup_ObjectIdentity((1,3,6,1,4,1,629,1,50,3,2,24))
class _NbVlansPermPortMacLimitActionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),(_j,2),(_k,3),(_l,4)))
_NbVlansPermPortMacLimitActionMode_Type.__name__=_C
_NbVlansPermPortMacLimitActionMode_Object=MibScalar
nbVlansPermPortMacLimitActionMode=_NbVlansPermPortMacLimitActionMode_Object((1,3,6,1,4,1,629,1,50,3,2,24,1),_NbVlansPermPortMacLimitActionMode_Type())
nbVlansPermPortMacLimitActionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermPortMacLimitActionMode.setStatus(_A)
_NbVlansPermPortMacLimitTable_Object=MibTable
nbVlansPermPortMacLimitTable=_NbVlansPermPortMacLimitTable_Object((1,3,6,1,4,1,629,1,50,3,2,24,10))
if mibBuilder.loadTexts:nbVlansPermPortMacLimitTable.setStatus(_A)
_NbVlansPermPortMacLimitEntry_Object=MibTableRow
nbVlansPermPortMacLimitEntry=_NbVlansPermPortMacLimitEntry_Object((1,3,6,1,4,1,629,1,50,3,2,24,10,1))
nbVlansPermPortMacLimitEntry.setIndexNames((0,_E,_u))
if mibBuilder.loadTexts:nbVlansPermPortMacLimitEntry.setStatus(_A)
_NbVlansPermPortMacLimitPortNumber_Type=Integer32
_NbVlansPermPortMacLimitPortNumber_Object=MibTableColumn
nbVlansPermPortMacLimitPortNumber=_NbVlansPermPortMacLimitPortNumber_Object((1,3,6,1,4,1,629,1,50,3,2,24,10,1,1),_NbVlansPermPortMacLimitPortNumber_Type())
nbVlansPermPortMacLimitPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansPermPortMacLimitPortNumber.setStatus(_A)
_NbVlansPermPortMacLimitValue_Type=Integer32
_NbVlansPermPortMacLimitValue_Object=MibTableColumn
nbVlansPermPortMacLimitValue=_NbVlansPermPortMacLimitValue_Object((1,3,6,1,4,1,629,1,50,3,2,24,10,1,2),_NbVlansPermPortMacLimitValue_Type())
nbVlansPermPortMacLimitValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansPermPortMacLimitValue.setStatus(_A)
_NbVlansMacTable_Object=MibTable
nbVlansMacTable=_NbVlansMacTable_Object((1,3,6,1,4,1,629,1,50,3,3))
if mibBuilder.loadTexts:nbVlansMacTable.setStatus(_A)
_NbVlansMacEntry_Object=MibTableRow
nbVlansMacEntry=_NbVlansMacEntry_Object((1,3,6,1,4,1,629,1,50,3,3,1))
nbVlansMacEntry.setIndexNames((0,_E,_v))
if mibBuilder.loadTexts:nbVlansMacEntry.setStatus(_A)
_NbVlansMacGetViewIndex_Type=Integer32
_NbVlansMacGetViewIndex_Object=MibTableColumn
nbVlansMacGetViewIndex=_NbVlansMacGetViewIndex_Object((1,3,6,1,4,1,629,1,50,3,3,1,1),_NbVlansMacGetViewIndex_Type())
nbVlansMacGetViewIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansMacGetViewIndex.setStatus(_A)
_NbVlansMac_Type=MacAddress
_NbVlansMac_Object=MibTableColumn
nbVlansMac=_NbVlansMac_Object((1,3,6,1,4,1,629,1,50,3,3,1,2),_NbVlansMac_Type())
nbVlansMac.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansMac.setStatus(_A)
class _NbVlansMacVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4096))
_NbVlansMacVid_Type.__name__=_C
_NbVlansMacVid_Object=MibTableColumn
nbVlansMacVid=_NbVlansMacVid_Object((1,3,6,1,4,1,629,1,50,3,3,1,3),_NbVlansMacVid_Type())
nbVlansMacVid.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansMacVid.setStatus(_A)
class _NbVlansMacVidx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4096))
_NbVlansMacVidx_Type.__name__=_C
_NbVlansMacVidx_Object=MibTableColumn
nbVlansMacVidx=_NbVlansMacVidx_Object((1,3,6,1,4,1,629,1,50,3,3,1,4),_NbVlansMacVidx_Type())
nbVlansMacVidx.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansMacVidx.setStatus(_A)
class _NbVlansMacPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NbVlansMacPort_Type.__name__=_C
_NbVlansMacPort_Object=MibTableColumn
nbVlansMacPort=_NbVlansMacPort_Object((1,3,6,1,4,1,629,1,50,3,3,1,5),_NbVlansMacPort_Type())
nbVlansMacPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansMacPort.setStatus(_A)
class _NbVlansMacStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('static',2)))
_NbVlansMacStatus_Type.__name__=_C
_NbVlansMacStatus_Object=MibTableColumn
nbVlansMacStatus=_NbVlansMacStatus_Object((1,3,6,1,4,1,629,1,50,3,3,1,6),_NbVlansMacStatus_Type())
nbVlansMacStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansMacStatus.setStatus(_A)
class _NbVlansMacTagged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_NbVlansMacTagged_Type.__name__=_C
_NbVlansMacTagged_Object=MibTableColumn
nbVlansMacTagged=_NbVlansMacTagged_Object((1,3,6,1,4,1,629,1,50,3,3,1,7),_NbVlansMacTagged_Type())
nbVlansMacTagged.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansMacTagged.setStatus(_A)
class _NbVlansMacState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NbVlansMacState_Type.__name__=_C
_NbVlansMacState_Object=MibTableColumn
nbVlansMacState=_NbVlansMacState_Object((1,3,6,1,4,1,629,1,50,3,3,1,8),_NbVlansMacState_Type())
nbVlansMacState.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansMacState.setStatus(_A)
class _NbVlansMacPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('low',0),('high',1)))
_NbVlansMacPriority_Type.__name__=_C
_NbVlansMacPriority_Object=MibTableColumn
nbVlansMacPriority=_NbVlansMacPriority_Object((1,3,6,1,4,1,629,1,50,3,3,1,9),_NbVlansMacPriority_Type())
nbVlansMacPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansMacPriority.setStatus(_A)
class _NbVlansMacFlags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),('route',1)))
_NbVlansMacFlags_Type.__name__=_C
_NbVlansMacFlags_Object=MibTableColumn
nbVlansMacFlags=_NbVlansMacFlags_Object((1,3,6,1,4,1,629,1,50,3,3,1,10),_NbVlansMacFlags_Type())
nbVlansMacFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansMacFlags.setStatus(_A)
_NbVlansMaxNumMgmtVlans_Type=Integer32
_NbVlansMaxNumMgmtVlans_Object=MibScalar
nbVlansMaxNumMgmtVlans=_NbVlansMaxNumMgmtVlans_Object((1,3,6,1,4,1,629,1,50,3,4),_NbVlansMaxNumMgmtVlans_Type())
nbVlansMaxNumMgmtVlans.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansMaxNumMgmtVlans.setStatus(_A)
class _NbVlansNewVlanIdMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),('enableAddVlanWithoutId',2)))
_NbVlansNewVlanIdMode_Type.__name__=_C
_NbVlansNewVlanIdMode_Object=MibScalar
nbVlansNewVlanIdMode=_NbVlansNewVlanIdMode_Object((1,3,6,1,4,1,629,1,50,3,5),_NbVlansNewVlanIdMode_Type())
nbVlansNewVlanIdMode.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansNewVlanIdMode.setStatus(_A)
class _NbVlansSaveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),('allVlansConfig',2)))
_NbVlansSaveMode_Type.__name__=_C
_NbVlansSaveMode_Object=MibScalar
nbVlansSaveMode=_NbVlansSaveMode_Object((1,3,6,1,4,1,629,1,50,3,6),_NbVlansSaveMode_Type())
nbVlansSaveMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansSaveMode.setStatus(_A)
class _NbVlansDevEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
_NbVlansDevEtherType_Type.__name__=_C
_NbVlansDevEtherType_Object=MibScalar
nbVlansDevEtherType=_NbVlansDevEtherType_Object((1,3,6,1,4,1,629,1,50,3,7),_NbVlansDevEtherType_Type())
nbVlansDevEtherType.setMaxAccess(_D)
if mibBuilder.loadTexts:nbVlansDevEtherType.setStatus(_A)
class _NbVlansMacLimitSaveCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),('allPortMacLimit',2)))
_NbVlansMacLimitSaveCfg_Type.__name__=_C
_NbVlansMacLimitSaveCfg_Object=MibScalar
nbVlansMacLimitSaveCfg=_NbVlansMacLimitSaveCfg_Object((1,3,6,1,4,1,629,1,50,3,8),_NbVlansMacLimitSaveCfg_Type())
nbVlansMacLimitSaveCfg.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVlansMacLimitSaveCfg.setStatus(_A)
portMacLimitExceeded=NotificationType((1,3,6,1,4,1,629,1,50,3,0,32))
portMacLimitExceeded.setObjects(*((_E,_Q),(_E,_w),(_E,_x)))
if mibBuilder.loadTexts:portMacLimitExceeded.setStatus('')
mibBuilder.exportSymbols(_E,**{'MacAddress':MacAddress,'PortsBitmap':PortsBitmap,'nbVlans':nbVlans,'portMacLimitExceeded':portMacLimitExceeded,'nbVlansRun':nbVlansRun,'nbVlansRunVlansMode':nbVlansRunVlansMode,'nbVlansRunIngressType':nbVlansRunIngressType,'nbVlansRunIngressMode':nbVlansRunIngressMode,'nbVlansRunIngressPorts':nbVlansRunIngressPorts,'nbVlansRunEgressType':nbVlansRunEgressType,'nbVlansRunEgressMode':nbVlansRunEgressMode,'nbVlansRunEgressPorts':nbVlansRunEgressPorts,'nbVlansRunMgmtTable':nbVlansRunMgmtTable,'nbVlansRunMgmtEntry':nbVlansRunMgmtEntry,_U:nbVlansRunMgmtTag,'nbVlansRunMgmtList':nbVlansRunMgmtList,'nbVlansRunMgmtName':nbVlansRunMgmtName,'nbVlansRunMgmtTagStatus':nbVlansRunMgmtTagStatus,'nbVlansRunSrvrTable':nbVlansRunSrvrTable,'nbVlansRunSrvrEntry':nbVlansRunSrvrEntry,_V:nbVlansRunSrvrPort,'nbVlansRunSrvrPortStatus':nbVlansRunSrvrPortStatus,'nbVlansRunSrvrPortTag':nbVlansRunSrvrPortTag,'nbVlansRunPortsCfgTable':nbVlansRunPortsCfgTable,'nbVlansRunPortsCfgEntry':nbVlansRunPortsCfgEntry,_Y:nbVlansRunPort,'nbVlansRunPortPriority':nbVlansRunPortPriority,'nbVlansRunPortTagOutMode':nbVlansRunPortTagOutMode,'nbVlansRunPriorityPolicy':nbVlansRunPriorityPolicy,'nbVlansRunIsvMaxNum':nbVlansRunIsvMaxNum,'nbVlansRunIsvTable':nbVlansRunIsvTable,'nbVlansRunIsvEntry':nbVlansRunIsvEntry,_c:nbVlansRunIsvIndex,'nbVlansRunIsvStatus':nbVlansRunIsvStatus,'nbVlansRunIsvList':nbVlansRunIsvList,'nbVlansRunIsvName':nbVlansRunIsvName,'nbVlansRunIsvTag':nbVlansRunIsvTag,'nbVlansRunIsvVlanIndex':nbVlansRunIsvVlanIndex,'nbVlansRunIsvVlanPriority':nbVlansRunIsvVlanPriority,'nbVlansRunVPT2PriorityTable':nbVlansRunVPT2PriorityTable,'nbVlansRunVPT2PriorityEntry':nbVlansRunVPT2PriorityEntry,_d:nbVlansRunVPT2PriorVPTNumber,'nbVlansRunVPT2PriorPriorNumber':nbVlansRunVPT2PriorPriorNumber,'nbVlansRunPriority2VPTTable':nbVlansRunPriority2VPTTable,'nbVlansRunPriority2VPTEntry':nbVlansRunPriority2VPTEntry,_e:nbVlansRunPrior2VPTPriorNumber,'nbVlansRunPrior2VPTVPTNumber':nbVlansRunPrior2VPTVPTNumber,'nbVlansRunSlotEtherTypeTable':nbVlansRunSlotEtherTypeTable,'nbVlansRunSlotEtherTypeEntry':nbVlansRunSlotEtherTypeEntry,_f:nbVlansRunSlotNumber,'nbVlansRunSlotEtherType':nbVlansRunSlotEtherType,'nbVlansRunVMANPortTable':nbVlansRunVMANPortTable,'nbVlansRunVMANPortEntry':nbVlansRunVMANPortEntry,_g:nbVlansRunVMANPortNumber,'nbVlansRunVMANPortMode':nbVlansRunVMANPortMode,'nbVlansRunCPUEtherType':nbVlansRunCPUEtherType,'nbVlansRunMacLimitGroup':nbVlansRunMacLimitGroup,'nbVlansRunPortMacLimitActionMode':nbVlansRunPortMacLimitActionMode,_x:nbVlansRunPortMacLimitActionDescription,'nbVlansRunPortMacLimitTable':nbVlansRunPortMacLimitTable,'nbVlansRunPortMacLimitEntry':nbVlansRunPortMacLimitEntry,_Q:nbVlansRunPortMacLimitPortNumber,_w:nbVlansRunPortMacLimitValue,'nbVlansPerm':nbVlansPerm,'nbVlansPermVlansMode':nbVlansPermVlansMode,'nbVlansPermIngressType':nbVlansPermIngressType,'nbVlansPermIngressMode':nbVlansPermIngressMode,'nbVlansPermIngressPorts':nbVlansPermIngressPorts,'nbVlansPermEgressType':nbVlansPermEgressType,'nbVlansPermEgressMode':nbVlansPermEgressMode,'nbVlansPermEgressPorts':nbVlansPermEgressPorts,'nbVlansPermMgmtTable':nbVlansPermMgmtTable,'nbVlansPermMgmtEntry':nbVlansPermMgmtEntry,_m:nbVlansPermMgmtTag,'nbVlansPermMgmtList':nbVlansPermMgmtList,'nbVlansPermMgmtName':nbVlansPermMgmtName,'nbVlansPermMgmtTagStatus':nbVlansPermMgmtTagStatus,'nbVlansPermSrvrTable':nbVlansPermSrvrTable,'nbVlansPermSrvrEntry':nbVlansPermSrvrEntry,_n:nbVlansPermSrvrPort,'nbVlansPermSrvrPortStatus':nbVlansPermSrvrPortStatus,'nbVlansPermSrvrPortTag':nbVlansPermSrvrPortTag,'nbVlansPermPortsCfgTable':nbVlansPermPortsCfgTable,'nbVlansPermPortsCfgEntry':nbVlansPermPortsCfgEntry,_o:nbVlansPermPort,'nbVlansPermPortPriority':nbVlansPermPortPriority,'nbVlansPermPortTagOutMode':nbVlansPermPortTagOutMode,'nbVlansPermPriorityPolicy':nbVlansPermPriorityPolicy,'nbVlansPermIsvMaxNum':nbVlansPermIsvMaxNum,'nbVlansPermIsvTable':nbVlansPermIsvTable,'nbVlansPermIsvEntry':nbVlansPermIsvEntry,_p:nbVlansPermIsvIndex,'nbVlansPermIsvStatus':nbVlansPermIsvStatus,'nbVlansPermIsvList':nbVlansPermIsvList,'nbVlansPermIsvName':nbVlansPermIsvName,'nbVlansPermIsvTag':nbVlansPermIsvTag,'nbVlansPermIsvVlanPriority':nbVlansPermIsvVlanPriority,'nbVlansPermVPT2PriorityTable':nbVlansPermVPT2PriorityTable,'nbVlansPermVPT2PriorityEntry':nbVlansPermVPT2PriorityEntry,_q:nbVlansPermVPT2PriorVPTNumber,'nbVlansPermVPT2PriorPriorNumber':nbVlansPermVPT2PriorPriorNumber,'nbVlansPermPriority2VPTTable':nbVlansPermPriority2VPTTable,'nbVlansPermPriority2VPTEntry':nbVlansPermPriority2VPTEntry,_r:nbVlansPermPrior2VPTPriorNumber,'nbVlansPermPrior2VPTVPTNumber':nbVlansPermPrior2VPTVPTNumber,'nbVlansPermSlotEtherTypeTable':nbVlansPermSlotEtherTypeTable,'nbVlansPermSlotEtherTypeEntry':nbVlansPermSlotEtherTypeEntry,_s:nbVlansPermSlotNumber,'nbVlansPermSlotEtherType':nbVlansPermSlotEtherType,'nbVlansPermVMANPortTable':nbVlansPermVMANPortTable,'nbVlansPermVMANPortEntry':nbVlansPermVMANPortEntry,_t:nbVlansPermVMANPortNumber,'nbVlansPermVMANPortMode':nbVlansPermVMANPortMode,'nbVlansPermCPUEtherType':nbVlansPermCPUEtherType,'nbVlansPermMacLimitGroup':nbVlansPermMacLimitGroup,'nbVlansPermPortMacLimitActionMode':nbVlansPermPortMacLimitActionMode,'nbVlansPermPortMacLimitTable':nbVlansPermPortMacLimitTable,'nbVlansPermPortMacLimitEntry':nbVlansPermPortMacLimitEntry,_u:nbVlansPermPortMacLimitPortNumber,'nbVlansPermPortMacLimitValue':nbVlansPermPortMacLimitValue,'nbVlansMacTable':nbVlansMacTable,'nbVlansMacEntry':nbVlansMacEntry,_v:nbVlansMacGetViewIndex,'nbVlansMac':nbVlansMac,'nbVlansMacVid':nbVlansMacVid,'nbVlansMacVidx':nbVlansMacVidx,'nbVlansMacPort':nbVlansMacPort,'nbVlansMacStatus':nbVlansMacStatus,'nbVlansMacTagged':nbVlansMacTagged,'nbVlansMacState':nbVlansMacState,'nbVlansMacPriority':nbVlansMacPriority,'nbVlansMacFlags':nbVlansMacFlags,'nbVlansMaxNumMgmtVlans':nbVlansMaxNumMgmtVlans,'nbVlansNewVlanIdMode':nbVlansNewVlanIdMode,'nbVlansSaveMode':nbVlansSaveMode,'nbVlansDevEtherType':nbVlansDevEtherType,'nbVlansMacLimitSaveCfg':nbVlansMacLimitSaveCfg})