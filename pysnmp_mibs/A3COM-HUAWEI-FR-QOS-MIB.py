_O='hwRTPFrClassApplyFrClassIndex'
_N='hwIfApplyFrClassIfIndex'
_M='hwCirFrClassIndex'
_L='hwCirAllowDirection'
_K='hwCirAllowFrClassIndex'
_J='hwFrClassIndex'
_I='OctetString'
_H='hwPvcApplyFrClassDlciNum'
_G='hwPvcApplyFrClassIfIndex'
_F='read-only'
_E='not-accessible'
_D='Integer32'
_C='A3COM-HUAWEI-FR-QOS-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hwQoS,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','hwQoS')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hwFrQoSMib=ModuleIdentity((1,3,6,1,4,1,43,45,1,5,25,32,3))
class CirAllowDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inbound',1),('outbound',2),('inboundAndOutbound',3)))
_HwFrQoSObjects_ObjectIdentity=ObjectIdentity
hwFrQoSObjects=_HwFrQoSObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,32,3,1))
_HwFrClassObjects_ObjectIdentity=ObjectIdentity
hwFrClassObjects=_HwFrClassObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1))
_HwFrClassIndexNext_Type=Integer32
_HwFrClassIndexNext_Object=MibScalar
hwFrClassIndexNext=_HwFrClassIndexNext_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,1),_HwFrClassIndexNext_Type())
hwFrClassIndexNext.setMaxAccess(_F)
if mibBuilder.loadTexts:hwFrClassIndexNext.setStatus(_A)
_HwFrClassCfgInfoTable_Object=MibTable
hwFrClassCfgInfoTable=_HwFrClassCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,2))
if mibBuilder.loadTexts:hwFrClassCfgInfoTable.setStatus(_A)
_HwFrClassCfgInfoEntry_Object=MibTableRow
hwFrClassCfgInfoEntry=_HwFrClassCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,2,1))
hwFrClassCfgInfoEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:hwFrClassCfgInfoEntry.setStatus(_A)
_HwFrClassIndex_Type=Integer32
_HwFrClassIndex_Object=MibTableColumn
hwFrClassIndex=_HwFrClassIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,2,1,1),_HwFrClassIndex_Type())
hwFrClassIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwFrClassIndex.setStatus(_A)
class _HwFrClassName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwFrClassName_Type.__name__=_I
_HwFrClassName_Object=MibTableColumn
hwFrClassName=_HwFrClassName_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,2,1,2),_HwFrClassName_Type())
hwFrClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:hwFrClassName.setStatus(_A)
_HwFrClassRowStatus_Type=RowStatus
_HwFrClassRowStatus_Object=MibTableColumn
hwFrClassRowStatus=_HwFrClassRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,2,1,3),_HwFrClassRowStatus_Type())
hwFrClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwFrClassRowStatus.setStatus(_A)
_HwCirAllowCfgInfoTable_Object=MibTable
hwCirAllowCfgInfoTable=_HwCirAllowCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,3))
if mibBuilder.loadTexts:hwCirAllowCfgInfoTable.setStatus(_A)
_HwCirAllowCfgInfoEntry_Object=MibTableRow
hwCirAllowCfgInfoEntry=_HwCirAllowCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,3,1))
hwCirAllowCfgInfoEntry.setIndexNames((0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:hwCirAllowCfgInfoEntry.setStatus(_A)
_HwCirAllowFrClassIndex_Type=Integer32
_HwCirAllowFrClassIndex_Object=MibTableColumn
hwCirAllowFrClassIndex=_HwCirAllowFrClassIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,3,1,1),_HwCirAllowFrClassIndex_Type())
hwCirAllowFrClassIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwCirAllowFrClassIndex.setStatus(_A)
_HwCirAllowDirection_Type=CirAllowDirection
_HwCirAllowDirection_Object=MibTableColumn
hwCirAllowDirection=_HwCirAllowDirection_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,3,1,2),_HwCirAllowDirection_Type())
hwCirAllowDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:hwCirAllowDirection.setStatus(_A)
class _HwCirAllowValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,45000000))
_HwCirAllowValue_Type.__name__=_D
_HwCirAllowValue_Object=MibTableColumn
hwCirAllowValue=_HwCirAllowValue_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,3,1,3),_HwCirAllowValue_Type())
hwCirAllowValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hwCirAllowValue.setStatus(_A)
_HwCirAllowRowStatus_Type=RowStatus
_HwCirAllowRowStatus_Object=MibTableColumn
hwCirAllowRowStatus=_HwCirAllowRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,3,1,4),_HwCirAllowRowStatus_Type())
hwCirAllowRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwCirAllowRowStatus.setStatus(_A)
_HwCirCfgInfoTable_Object=MibTable
hwCirCfgInfoTable=_HwCirCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,4))
if mibBuilder.loadTexts:hwCirCfgInfoTable.setStatus(_A)
_HwCirCfgInfoEntry_Object=MibTableRow
hwCirCfgInfoEntry=_HwCirCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,4,1))
hwCirCfgInfoEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:hwCirCfgInfoEntry.setStatus(_A)
_HwCirFrClassIndex_Type=Integer32
_HwCirFrClassIndex_Object=MibTableColumn
hwCirFrClassIndex=_HwCirFrClassIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,4,1,1),_HwCirFrClassIndex_Type())
hwCirFrClassIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwCirFrClassIndex.setStatus(_A)
class _HwCirValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,45000000))
_HwCirValue_Type.__name__=_D
_HwCirValue_Object=MibTableColumn
hwCirValue=_HwCirValue_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,4,1,2),_HwCirValue_Type())
hwCirValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hwCirValue.setStatus(_A)
_HwCirRowStatus_Type=RowStatus
_HwCirRowStatus_Object=MibTableColumn
hwCirRowStatus=_HwCirRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,4,1,3),_HwCirRowStatus_Type())
hwCirRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwCirRowStatus.setStatus(_A)
_HwIfApplyFrClassTable_Object=MibTable
hwIfApplyFrClassTable=_HwIfApplyFrClassTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,5))
if mibBuilder.loadTexts:hwIfApplyFrClassTable.setStatus(_A)
_HwIfApplyFrClassEntry_Object=MibTableRow
hwIfApplyFrClassEntry=_HwIfApplyFrClassEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,5,1))
hwIfApplyFrClassEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:hwIfApplyFrClassEntry.setStatus(_A)
_HwIfApplyFrClassIfIndex_Type=Integer32
_HwIfApplyFrClassIfIndex_Object=MibTableColumn
hwIfApplyFrClassIfIndex=_HwIfApplyFrClassIfIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,5,1,1),_HwIfApplyFrClassIfIndex_Type())
hwIfApplyFrClassIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwIfApplyFrClassIfIndex.setStatus(_A)
_HwIfApplyFrClassIndex_Type=Integer32
_HwIfApplyFrClassIndex_Object=MibTableColumn
hwIfApplyFrClassIndex=_HwIfApplyFrClassIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,5,1,2),_HwIfApplyFrClassIndex_Type())
hwIfApplyFrClassIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hwIfApplyFrClassIndex.setStatus(_A)
_HwIfApplyFrClassRowStatus_Type=RowStatus
_HwIfApplyFrClassRowStatus_Object=MibTableColumn
hwIfApplyFrClassRowStatus=_HwIfApplyFrClassRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,5,1,3),_HwIfApplyFrClassRowStatus_Type())
hwIfApplyFrClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwIfApplyFrClassRowStatus.setStatus(_A)
_HwPvcApplyFrClassTable_Object=MibTable
hwPvcApplyFrClassTable=_HwPvcApplyFrClassTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,6))
if mibBuilder.loadTexts:hwPvcApplyFrClassTable.setStatus(_A)
_HwPvcApplyFrClassEntry_Object=MibTableRow
hwPvcApplyFrClassEntry=_HwPvcApplyFrClassEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,6,1))
hwPvcApplyFrClassEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:hwPvcApplyFrClassEntry.setStatus(_A)
_HwPvcApplyFrClassIfIndex_Type=Integer32
_HwPvcApplyFrClassIfIndex_Object=MibTableColumn
hwPvcApplyFrClassIfIndex=_HwPvcApplyFrClassIfIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,6,1,1),_HwPvcApplyFrClassIfIndex_Type())
hwPvcApplyFrClassIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwPvcApplyFrClassIfIndex.setStatus(_A)
class _HwPvcApplyFrClassDlciNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1007))
_HwPvcApplyFrClassDlciNum_Type.__name__=_D
_HwPvcApplyFrClassDlciNum_Object=MibTableColumn
hwPvcApplyFrClassDlciNum=_HwPvcApplyFrClassDlciNum_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,6,1,2),_HwPvcApplyFrClassDlciNum_Type())
hwPvcApplyFrClassDlciNum.setMaxAccess(_E)
if mibBuilder.loadTexts:hwPvcApplyFrClassDlciNum.setStatus(_A)
_HwPvcApplyFrClassIndex_Type=Integer32
_HwPvcApplyFrClassIndex_Object=MibTableColumn
hwPvcApplyFrClassIndex=_HwPvcApplyFrClassIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,6,1,3),_HwPvcApplyFrClassIndex_Type())
hwPvcApplyFrClassIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPvcApplyFrClassIndex.setStatus(_A)
_HwPvcApplyFrClassRowStatus_Type=RowStatus
_HwPvcApplyFrClassRowStatus_Object=MibTableColumn
hwPvcApplyFrClassRowStatus=_HwPvcApplyFrClassRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,6,1,4),_HwPvcApplyFrClassRowStatus_Type())
hwPvcApplyFrClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPvcApplyFrClassRowStatus.setStatus(_A)
_HwFrPvcBandwidthTable_Object=MibTable
hwFrPvcBandwidthTable=_HwFrPvcBandwidthTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,7))
if mibBuilder.loadTexts:hwFrPvcBandwidthTable.setStatus(_A)
_HwFrPvcBandwidthEntry_Object=MibTableRow
hwFrPvcBandwidthEntry=_HwFrPvcBandwidthEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,7,1))
hwFrPvcBandwidthEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:hwFrPvcBandwidthEntry.setStatus(_A)
_HwFrPvcBandwidthMaxReservedBW_Type=Integer32
_HwFrPvcBandwidthMaxReservedBW_Object=MibTableColumn
hwFrPvcBandwidthMaxReservedBW=_HwFrPvcBandwidthMaxReservedBW_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,7,1,1),_HwFrPvcBandwidthMaxReservedBW_Type())
hwFrPvcBandwidthMaxReservedBW.setMaxAccess(_F)
if mibBuilder.loadTexts:hwFrPvcBandwidthMaxReservedBW.setStatus(_A)
_HwFrPvcBandwidthAvailable_Type=Integer32
_HwFrPvcBandwidthAvailable_Object=MibTableColumn
hwFrPvcBandwidthAvailable=_HwFrPvcBandwidthAvailable_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,1,7,1,2),_HwFrPvcBandwidthAvailable_Type())
hwFrPvcBandwidthAvailable.setMaxAccess(_F)
if mibBuilder.loadTexts:hwFrPvcBandwidthAvailable.setStatus(_A)
_HwRTPQoSObjects_ObjectIdentity=ObjectIdentity
hwRTPQoSObjects=_HwRTPQoSObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,32,3,1,2))
_HwRTPFrClassApplyTable_Object=MibTable
hwRTPFrClassApplyTable=_HwRTPFrClassApplyTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,2,1))
if mibBuilder.loadTexts:hwRTPFrClassApplyTable.setStatus(_A)
_HwRTPFrClassApplyEntry_Object=MibTableRow
hwRTPFrClassApplyEntry=_HwRTPFrClassApplyEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,2,1,1))
hwRTPFrClassApplyEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:hwRTPFrClassApplyEntry.setStatus(_A)
_HwRTPFrClassApplyFrClassIndex_Type=Integer32
_HwRTPFrClassApplyFrClassIndex_Object=MibTableColumn
hwRTPFrClassApplyFrClassIndex=_HwRTPFrClassApplyFrClassIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,2,1,1,1),_HwRTPFrClassApplyFrClassIndex_Type())
hwRTPFrClassApplyFrClassIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwRTPFrClassApplyFrClassIndex.setStatus(_A)
class _HwRTPFrClassApplyStartPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,65535))
_HwRTPFrClassApplyStartPort_Type.__name__=_D
_HwRTPFrClassApplyStartPort_Object=MibTableColumn
hwRTPFrClassApplyStartPort=_HwRTPFrClassApplyStartPort_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,2,1,1,2),_HwRTPFrClassApplyStartPort_Type())
hwRTPFrClassApplyStartPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hwRTPFrClassApplyStartPort.setStatus(_A)
class _HwRTPFrClassApplyEndPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,65535))
_HwRTPFrClassApplyEndPort_Type.__name__=_D
_HwRTPFrClassApplyEndPort_Object=MibTableColumn
hwRTPFrClassApplyEndPort=_HwRTPFrClassApplyEndPort_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,2,1,1,3),_HwRTPFrClassApplyEndPort_Type())
hwRTPFrClassApplyEndPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hwRTPFrClassApplyEndPort.setStatus(_A)
class _HwRTPFrClassApplyBandWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,1000000))
_HwRTPFrClassApplyBandWidth_Type.__name__=_D
_HwRTPFrClassApplyBandWidth_Object=MibTableColumn
hwRTPFrClassApplyBandWidth=_HwRTPFrClassApplyBandWidth_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,2,1,1,4),_HwRTPFrClassApplyBandWidth_Type())
hwRTPFrClassApplyBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:hwRTPFrClassApplyBandWidth.setStatus(_A)
class _HwRTPFrClassApplyCbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1500,2000000))
_HwRTPFrClassApplyCbs_Type.__name__=_D
_HwRTPFrClassApplyCbs_Object=MibTableColumn
hwRTPFrClassApplyCbs=_HwRTPFrClassApplyCbs_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,2,1,1,5),_HwRTPFrClassApplyCbs_Type())
hwRTPFrClassApplyCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:hwRTPFrClassApplyCbs.setStatus(_A)
_HwRTPFrClassApplyRowStatus_Type=RowStatus
_HwRTPFrClassApplyRowStatus_Object=MibTableColumn
hwRTPFrClassApplyRowStatus=_HwRTPFrClassApplyRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,2,1,1,6),_HwRTPFrClassApplyRowStatus_Type())
hwRTPFrClassApplyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwRTPFrClassApplyRowStatus.setStatus(_A)
_HwRTPFrPvcQueueRunInfoTable_Object=MibTable
hwRTPFrPvcQueueRunInfoTable=_HwRTPFrPvcQueueRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,2,2))
if mibBuilder.loadTexts:hwRTPFrPvcQueueRunInfoTable.setStatus(_A)
_HwRTPFrPvcQueueRunInfoEntry_Object=MibTableRow
hwRTPFrPvcQueueRunInfoEntry=_HwRTPFrPvcQueueRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,2,2,1))
hwRTPFrPvcQueueRunInfoEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:hwRTPFrPvcQueueRunInfoEntry.setStatus(_A)
_HwRTPFrPvcQueueSize_Type=Integer32
_HwRTPFrPvcQueueSize_Object=MibTableColumn
hwRTPFrPvcQueueSize=_HwRTPFrPvcQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,2,2,1,1),_HwRTPFrPvcQueueSize_Type())
hwRTPFrPvcQueueSize.setMaxAccess(_F)
if mibBuilder.loadTexts:hwRTPFrPvcQueueSize.setStatus(_A)
_HwRTPFrPvcQueueMaxSize_Type=Integer32
_HwRTPFrPvcQueueMaxSize_Object=MibTableColumn
hwRTPFrPvcQueueMaxSize=_HwRTPFrPvcQueueMaxSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,2,2,1,2),_HwRTPFrPvcQueueMaxSize_Type())
hwRTPFrPvcQueueMaxSize.setMaxAccess(_F)
if mibBuilder.loadTexts:hwRTPFrPvcQueueMaxSize.setStatus(_A)
_HwRTPFrPvcQueueOutputs_Type=Counter32
_HwRTPFrPvcQueueOutputs_Object=MibTableColumn
hwRTPFrPvcQueueOutputs=_HwRTPFrPvcQueueOutputs_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,2,2,1,3),_HwRTPFrPvcQueueOutputs_Type())
hwRTPFrPvcQueueOutputs.setMaxAccess(_F)
if mibBuilder.loadTexts:hwRTPFrPvcQueueOutputs.setStatus(_A)
_HwRTPFrPvcQueueDiscards_Type=Counter32
_HwRTPFrPvcQueueDiscards_Object=MibTableColumn
hwRTPFrPvcQueueDiscards=_HwRTPFrPvcQueueDiscards_Object((1,3,6,1,4,1,43,45,1,5,25,32,3,1,2,2,1,4),_HwRTPFrPvcQueueDiscards_Type())
hwRTPFrPvcQueueDiscards.setMaxAccess(_F)
if mibBuilder.loadTexts:hwRTPFrPvcQueueDiscards.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'CirAllowDirection':CirAllowDirection,'hwFrQoSMib':hwFrQoSMib,'hwFrQoSObjects':hwFrQoSObjects,'hwFrClassObjects':hwFrClassObjects,'hwFrClassIndexNext':hwFrClassIndexNext,'hwFrClassCfgInfoTable':hwFrClassCfgInfoTable,'hwFrClassCfgInfoEntry':hwFrClassCfgInfoEntry,_J:hwFrClassIndex,'hwFrClassName':hwFrClassName,'hwFrClassRowStatus':hwFrClassRowStatus,'hwCirAllowCfgInfoTable':hwCirAllowCfgInfoTable,'hwCirAllowCfgInfoEntry':hwCirAllowCfgInfoEntry,_K:hwCirAllowFrClassIndex,_L:hwCirAllowDirection,'hwCirAllowValue':hwCirAllowValue,'hwCirAllowRowStatus':hwCirAllowRowStatus,'hwCirCfgInfoTable':hwCirCfgInfoTable,'hwCirCfgInfoEntry':hwCirCfgInfoEntry,_M:hwCirFrClassIndex,'hwCirValue':hwCirValue,'hwCirRowStatus':hwCirRowStatus,'hwIfApplyFrClassTable':hwIfApplyFrClassTable,'hwIfApplyFrClassEntry':hwIfApplyFrClassEntry,_N:hwIfApplyFrClassIfIndex,'hwIfApplyFrClassIndex':hwIfApplyFrClassIndex,'hwIfApplyFrClassRowStatus':hwIfApplyFrClassRowStatus,'hwPvcApplyFrClassTable':hwPvcApplyFrClassTable,'hwPvcApplyFrClassEntry':hwPvcApplyFrClassEntry,_G:hwPvcApplyFrClassIfIndex,_H:hwPvcApplyFrClassDlciNum,'hwPvcApplyFrClassIndex':hwPvcApplyFrClassIndex,'hwPvcApplyFrClassRowStatus':hwPvcApplyFrClassRowStatus,'hwFrPvcBandwidthTable':hwFrPvcBandwidthTable,'hwFrPvcBandwidthEntry':hwFrPvcBandwidthEntry,'hwFrPvcBandwidthMaxReservedBW':hwFrPvcBandwidthMaxReservedBW,'hwFrPvcBandwidthAvailable':hwFrPvcBandwidthAvailable,'hwRTPQoSObjects':hwRTPQoSObjects,'hwRTPFrClassApplyTable':hwRTPFrClassApplyTable,'hwRTPFrClassApplyEntry':hwRTPFrClassApplyEntry,_O:hwRTPFrClassApplyFrClassIndex,'hwRTPFrClassApplyStartPort':hwRTPFrClassApplyStartPort,'hwRTPFrClassApplyEndPort':hwRTPFrClassApplyEndPort,'hwRTPFrClassApplyBandWidth':hwRTPFrClassApplyBandWidth,'hwRTPFrClassApplyCbs':hwRTPFrClassApplyCbs,'hwRTPFrClassApplyRowStatus':hwRTPFrClassApplyRowStatus,'hwRTPFrPvcQueueRunInfoTable':hwRTPFrPvcQueueRunInfoTable,'hwRTPFrPvcQueueRunInfoEntry':hwRTPFrPvcQueueRunInfoEntry,'hwRTPFrPvcQueueSize':hwRTPFrPvcQueueSize,'hwRTPFrPvcQueueMaxSize':hwRTPFrPvcQueueMaxSize,'hwRTPFrPvcQueueOutputs':hwRTPFrPvcQueueOutputs,'hwRTPFrPvcQueueDiscards':hwRTPFrPvcQueueDiscards})