_O='hpnicfRTPFrClassApplyFrClassIndex'
_N='hpnicfIfApplyFrClassIfIndex'
_M='hpnicfCirFrClassIndex'
_L='hpnicfCirAllowDirection'
_K='hpnicfCirAllowFrClassIndex'
_J='hpnicfFrClassIndex'
_I='OctetString'
_H='hpnicfPvcApplyFrClassDlciNum'
_G='hpnicfPvcApplyFrClassIfIndex'
_F='read-only'
_E='not-accessible'
_D='Integer32'
_C='HPN-ICF-FR-QOS-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfQoS,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfQoS')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfFrQoSMib=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,32,3))
class HpnicfCirAllowDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inbound',1),('outbound',2),('inboundAndOutbound',3)))
_HpnicfFrQoSObjects_ObjectIdentity=ObjectIdentity
hpnicfFrQoSObjects=_HpnicfFrQoSObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1))
_HpnicfFrClassObjects_ObjectIdentity=ObjectIdentity
hpnicfFrClassObjects=_HpnicfFrClassObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1))
_HpnicfFrClassIndexNext_Type=Integer32
_HpnicfFrClassIndexNext_Object=MibScalar
hpnicfFrClassIndexNext=_HpnicfFrClassIndexNext_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,1),_HpnicfFrClassIndexNext_Type())
hpnicfFrClassIndexNext.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfFrClassIndexNext.setStatus(_A)
_HpnicfFrClassCfgInfoTable_Object=MibTable
hpnicfFrClassCfgInfoTable=_HpnicfFrClassCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,2))
if mibBuilder.loadTexts:hpnicfFrClassCfgInfoTable.setStatus(_A)
_HpnicfFrClassCfgInfoEntry_Object=MibTableRow
hpnicfFrClassCfgInfoEntry=_HpnicfFrClassCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,2,1))
hpnicfFrClassCfgInfoEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:hpnicfFrClassCfgInfoEntry.setStatus(_A)
_HpnicfFrClassIndex_Type=Integer32
_HpnicfFrClassIndex_Object=MibTableColumn
hpnicfFrClassIndex=_HpnicfFrClassIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,2,1,1),_HpnicfFrClassIndex_Type())
hpnicfFrClassIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFrClassIndex.setStatus(_A)
class _HpnicfFrClassName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfFrClassName_Type.__name__=_I
_HpnicfFrClassName_Object=MibTableColumn
hpnicfFrClassName=_HpnicfFrClassName_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,2,1,2),_HpnicfFrClassName_Type())
hpnicfFrClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFrClassName.setStatus(_A)
_HpnicfFrClassRowStatus_Type=RowStatus
_HpnicfFrClassRowStatus_Object=MibTableColumn
hpnicfFrClassRowStatus=_HpnicfFrClassRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,2,1,3),_HpnicfFrClassRowStatus_Type())
hpnicfFrClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFrClassRowStatus.setStatus(_A)
_HpnicfCirAllowCfgInfoTable_Object=MibTable
hpnicfCirAllowCfgInfoTable=_HpnicfCirAllowCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,3))
if mibBuilder.loadTexts:hpnicfCirAllowCfgInfoTable.setStatus(_A)
_HpnicfCirAllowCfgInfoEntry_Object=MibTableRow
hpnicfCirAllowCfgInfoEntry=_HpnicfCirAllowCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,3,1))
hpnicfCirAllowCfgInfoEntry.setIndexNames((0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:hpnicfCirAllowCfgInfoEntry.setStatus(_A)
_HpnicfCirAllowFrClassIndex_Type=Integer32
_HpnicfCirAllowFrClassIndex_Object=MibTableColumn
hpnicfCirAllowFrClassIndex=_HpnicfCirAllowFrClassIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,3,1,1),_HpnicfCirAllowFrClassIndex_Type())
hpnicfCirAllowFrClassIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCirAllowFrClassIndex.setStatus(_A)
_HpnicfCirAllowDirection_Type=HpnicfCirAllowDirection
_HpnicfCirAllowDirection_Object=MibTableColumn
hpnicfCirAllowDirection=_HpnicfCirAllowDirection_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,3,1,2),_HpnicfCirAllowDirection_Type())
hpnicfCirAllowDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCirAllowDirection.setStatus(_A)
class _HpnicfCirAllowValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,45000000))
_HpnicfCirAllowValue_Type.__name__=_D
_HpnicfCirAllowValue_Object=MibTableColumn
hpnicfCirAllowValue=_HpnicfCirAllowValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,3,1,3),_HpnicfCirAllowValue_Type())
hpnicfCirAllowValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCirAllowValue.setStatus(_A)
_HpnicfCirAllowRowStatus_Type=RowStatus
_HpnicfCirAllowRowStatus_Object=MibTableColumn
hpnicfCirAllowRowStatus=_HpnicfCirAllowRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,3,1,4),_HpnicfCirAllowRowStatus_Type())
hpnicfCirAllowRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCirAllowRowStatus.setStatus(_A)
_HpnicfCirCfgInfoTable_Object=MibTable
hpnicfCirCfgInfoTable=_HpnicfCirCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,4))
if mibBuilder.loadTexts:hpnicfCirCfgInfoTable.setStatus(_A)
_HpnicfCirCfgInfoEntry_Object=MibTableRow
hpnicfCirCfgInfoEntry=_HpnicfCirCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,4,1))
hpnicfCirCfgInfoEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:hpnicfCirCfgInfoEntry.setStatus(_A)
_HpnicfCirFrClassIndex_Type=Integer32
_HpnicfCirFrClassIndex_Object=MibTableColumn
hpnicfCirFrClassIndex=_HpnicfCirFrClassIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,4,1,1),_HpnicfCirFrClassIndex_Type())
hpnicfCirFrClassIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCirFrClassIndex.setStatus(_A)
class _HpnicfCirValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,45000000))
_HpnicfCirValue_Type.__name__=_D
_HpnicfCirValue_Object=MibTableColumn
hpnicfCirValue=_HpnicfCirValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,4,1,2),_HpnicfCirValue_Type())
hpnicfCirValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCirValue.setStatus(_A)
_HpnicfCirRowStatus_Type=RowStatus
_HpnicfCirRowStatus_Object=MibTableColumn
hpnicfCirRowStatus=_HpnicfCirRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,4,1,3),_HpnicfCirRowStatus_Type())
hpnicfCirRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCirRowStatus.setStatus(_A)
_HpnicfIfApplyFrClassTable_Object=MibTable
hpnicfIfApplyFrClassTable=_HpnicfIfApplyFrClassTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,5))
if mibBuilder.loadTexts:hpnicfIfApplyFrClassTable.setStatus(_A)
_HpnicfIfApplyFrClassEntry_Object=MibTableRow
hpnicfIfApplyFrClassEntry=_HpnicfIfApplyFrClassEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,5,1))
hpnicfIfApplyFrClassEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:hpnicfIfApplyFrClassEntry.setStatus(_A)
_HpnicfIfApplyFrClassIfIndex_Type=Integer32
_HpnicfIfApplyFrClassIfIndex_Object=MibTableColumn
hpnicfIfApplyFrClassIfIndex=_HpnicfIfApplyFrClassIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,5,1,1),_HpnicfIfApplyFrClassIfIndex_Type())
hpnicfIfApplyFrClassIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIfApplyFrClassIfIndex.setStatus(_A)
_HpnicfIfApplyFrClassIndex_Type=Integer32
_HpnicfIfApplyFrClassIndex_Object=MibTableColumn
hpnicfIfApplyFrClassIndex=_HpnicfIfApplyFrClassIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,5,1,2),_HpnicfIfApplyFrClassIndex_Type())
hpnicfIfApplyFrClassIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfApplyFrClassIndex.setStatus(_A)
_HpnicfIfApplyFrClassRowStatus_Type=RowStatus
_HpnicfIfApplyFrClassRowStatus_Object=MibTableColumn
hpnicfIfApplyFrClassRowStatus=_HpnicfIfApplyFrClassRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,5,1,3),_HpnicfIfApplyFrClassRowStatus_Type())
hpnicfIfApplyFrClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfApplyFrClassRowStatus.setStatus(_A)
_HpnicfPvcApplyFrClassTable_Object=MibTable
hpnicfPvcApplyFrClassTable=_HpnicfPvcApplyFrClassTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,6))
if mibBuilder.loadTexts:hpnicfPvcApplyFrClassTable.setStatus(_A)
_HpnicfPvcApplyFrClassEntry_Object=MibTableRow
hpnicfPvcApplyFrClassEntry=_HpnicfPvcApplyFrClassEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,6,1))
hpnicfPvcApplyFrClassEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:hpnicfPvcApplyFrClassEntry.setStatus(_A)
_HpnicfPvcApplyFrClassIfIndex_Type=Integer32
_HpnicfPvcApplyFrClassIfIndex_Object=MibTableColumn
hpnicfPvcApplyFrClassIfIndex=_HpnicfPvcApplyFrClassIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,6,1,1),_HpnicfPvcApplyFrClassIfIndex_Type())
hpnicfPvcApplyFrClassIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPvcApplyFrClassIfIndex.setStatus(_A)
class _HpnicfPvcApplyFrClassDlciNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1007))
_HpnicfPvcApplyFrClassDlciNum_Type.__name__=_D
_HpnicfPvcApplyFrClassDlciNum_Object=MibTableColumn
hpnicfPvcApplyFrClassDlciNum=_HpnicfPvcApplyFrClassDlciNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,6,1,2),_HpnicfPvcApplyFrClassDlciNum_Type())
hpnicfPvcApplyFrClassDlciNum.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPvcApplyFrClassDlciNum.setStatus(_A)
_HpnicfPvcApplyFrClassIndex_Type=Integer32
_HpnicfPvcApplyFrClassIndex_Object=MibTableColumn
hpnicfPvcApplyFrClassIndex=_HpnicfPvcApplyFrClassIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,6,1,3),_HpnicfPvcApplyFrClassIndex_Type())
hpnicfPvcApplyFrClassIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPvcApplyFrClassIndex.setStatus(_A)
_HpnicfPvcApplyFrClassRowStatus_Type=RowStatus
_HpnicfPvcApplyFrClassRowStatus_Object=MibTableColumn
hpnicfPvcApplyFrClassRowStatus=_HpnicfPvcApplyFrClassRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,6,1,4),_HpnicfPvcApplyFrClassRowStatus_Type())
hpnicfPvcApplyFrClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPvcApplyFrClassRowStatus.setStatus(_A)
_HpnicfFrPvcBandwidthTable_Object=MibTable
hpnicfFrPvcBandwidthTable=_HpnicfFrPvcBandwidthTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,7))
if mibBuilder.loadTexts:hpnicfFrPvcBandwidthTable.setStatus(_A)
_HpnicfFrPvcBandwidthEntry_Object=MibTableRow
hpnicfFrPvcBandwidthEntry=_HpnicfFrPvcBandwidthEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,7,1))
hpnicfFrPvcBandwidthEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:hpnicfFrPvcBandwidthEntry.setStatus(_A)
_HpnicfFrPvcBandwidthMaxReservedBW_Type=Integer32
_HpnicfFrPvcBandwidthMaxReservedBW_Object=MibTableColumn
hpnicfFrPvcBandwidthMaxReservedBW=_HpnicfFrPvcBandwidthMaxReservedBW_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,7,1,1),_HpnicfFrPvcBandwidthMaxReservedBW_Type())
hpnicfFrPvcBandwidthMaxReservedBW.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfFrPvcBandwidthMaxReservedBW.setStatus(_A)
_HpnicfFrPvcBandwidthAvailable_Type=Integer32
_HpnicfFrPvcBandwidthAvailable_Object=MibTableColumn
hpnicfFrPvcBandwidthAvailable=_HpnicfFrPvcBandwidthAvailable_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,1,7,1,2),_HpnicfFrPvcBandwidthAvailable_Type())
hpnicfFrPvcBandwidthAvailable.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfFrPvcBandwidthAvailable.setStatus(_A)
_HpnicfRTPQoSObjects_ObjectIdentity=ObjectIdentity
hpnicfRTPQoSObjects=_HpnicfRTPQoSObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,2))
_HpnicfRTPFrClassApplyTable_Object=MibTable
hpnicfRTPFrClassApplyTable=_HpnicfRTPFrClassApplyTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,2,1))
if mibBuilder.loadTexts:hpnicfRTPFrClassApplyTable.setStatus(_A)
_HpnicfRTPFrClassApplyEntry_Object=MibTableRow
hpnicfRTPFrClassApplyEntry=_HpnicfRTPFrClassApplyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,2,1,1))
hpnicfRTPFrClassApplyEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:hpnicfRTPFrClassApplyEntry.setStatus(_A)
_HpnicfRTPFrClassApplyFrClassIndex_Type=Integer32
_HpnicfRTPFrClassApplyFrClassIndex_Object=MibTableColumn
hpnicfRTPFrClassApplyFrClassIndex=_HpnicfRTPFrClassApplyFrClassIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,2,1,1,1),_HpnicfRTPFrClassApplyFrClassIndex_Type())
hpnicfRTPFrClassApplyFrClassIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRTPFrClassApplyFrClassIndex.setStatus(_A)
class _HpnicfRTPFrClassApplyStartPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,65535))
_HpnicfRTPFrClassApplyStartPort_Type.__name__=_D
_HpnicfRTPFrClassApplyStartPort_Object=MibTableColumn
hpnicfRTPFrClassApplyStartPort=_HpnicfRTPFrClassApplyStartPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,2,1,1,2),_HpnicfRTPFrClassApplyStartPort_Type())
hpnicfRTPFrClassApplyStartPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRTPFrClassApplyStartPort.setStatus(_A)
class _HpnicfRTPFrClassApplyEndPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,65535))
_HpnicfRTPFrClassApplyEndPort_Type.__name__=_D
_HpnicfRTPFrClassApplyEndPort_Object=MibTableColumn
hpnicfRTPFrClassApplyEndPort=_HpnicfRTPFrClassApplyEndPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,2,1,1,3),_HpnicfRTPFrClassApplyEndPort_Type())
hpnicfRTPFrClassApplyEndPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRTPFrClassApplyEndPort.setStatus(_A)
class _HpnicfRTPFrClassApplyBandWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,1000000))
_HpnicfRTPFrClassApplyBandWidth_Type.__name__=_D
_HpnicfRTPFrClassApplyBandWidth_Object=MibTableColumn
hpnicfRTPFrClassApplyBandWidth=_HpnicfRTPFrClassApplyBandWidth_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,2,1,1,4),_HpnicfRTPFrClassApplyBandWidth_Type())
hpnicfRTPFrClassApplyBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRTPFrClassApplyBandWidth.setStatus(_A)
class _HpnicfRTPFrClassApplyCbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1500,2000000))
_HpnicfRTPFrClassApplyCbs_Type.__name__=_D
_HpnicfRTPFrClassApplyCbs_Object=MibTableColumn
hpnicfRTPFrClassApplyCbs=_HpnicfRTPFrClassApplyCbs_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,2,1,1,5),_HpnicfRTPFrClassApplyCbs_Type())
hpnicfRTPFrClassApplyCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRTPFrClassApplyCbs.setStatus(_A)
_HpnicfRTPFrClassApplyRowStatus_Type=RowStatus
_HpnicfRTPFrClassApplyRowStatus_Object=MibTableColumn
hpnicfRTPFrClassApplyRowStatus=_HpnicfRTPFrClassApplyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,2,1,1,6),_HpnicfRTPFrClassApplyRowStatus_Type())
hpnicfRTPFrClassApplyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRTPFrClassApplyRowStatus.setStatus(_A)
_HpnicfRTPFrPvcQueueRunInfoTable_Object=MibTable
hpnicfRTPFrPvcQueueRunInfoTable=_HpnicfRTPFrPvcQueueRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,2,2))
if mibBuilder.loadTexts:hpnicfRTPFrPvcQueueRunInfoTable.setStatus(_A)
_HpnicfRTPFrPvcQueueRunInfoEntry_Object=MibTableRow
hpnicfRTPFrPvcQueueRunInfoEntry=_HpnicfRTPFrPvcQueueRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,2,2,1))
hpnicfRTPFrPvcQueueRunInfoEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:hpnicfRTPFrPvcQueueRunInfoEntry.setStatus(_A)
_HpnicfRTPFrPvcQueueSize_Type=Integer32
_HpnicfRTPFrPvcQueueSize_Object=MibTableColumn
hpnicfRTPFrPvcQueueSize=_HpnicfRTPFrPvcQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,2,2,1,1),_HpnicfRTPFrPvcQueueSize_Type())
hpnicfRTPFrPvcQueueSize.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRTPFrPvcQueueSize.setStatus(_A)
_HpnicfRTPFrPvcQueueMaxSize_Type=Integer32
_HpnicfRTPFrPvcQueueMaxSize_Object=MibTableColumn
hpnicfRTPFrPvcQueueMaxSize=_HpnicfRTPFrPvcQueueMaxSize_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,2,2,1,2),_HpnicfRTPFrPvcQueueMaxSize_Type())
hpnicfRTPFrPvcQueueMaxSize.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRTPFrPvcQueueMaxSize.setStatus(_A)
_HpnicfRTPFrPvcQueueOutputs_Type=Counter32
_HpnicfRTPFrPvcQueueOutputs_Object=MibTableColumn
hpnicfRTPFrPvcQueueOutputs=_HpnicfRTPFrPvcQueueOutputs_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,2,2,1,3),_HpnicfRTPFrPvcQueueOutputs_Type())
hpnicfRTPFrPvcQueueOutputs.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRTPFrPvcQueueOutputs.setStatus(_A)
_HpnicfRTPFrPvcQueueDiscards_Type=Counter32
_HpnicfRTPFrPvcQueueDiscards_Object=MibTableColumn
hpnicfRTPFrPvcQueueDiscards=_HpnicfRTPFrPvcQueueDiscards_Object((1,3,6,1,4,1,11,2,14,11,15,8,32,3,1,2,2,1,4),_HpnicfRTPFrPvcQueueDiscards_Type())
hpnicfRTPFrPvcQueueDiscards.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRTPFrPvcQueueDiscards.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'HpnicfCirAllowDirection':HpnicfCirAllowDirection,'hpnicfFrQoSMib':hpnicfFrQoSMib,'hpnicfFrQoSObjects':hpnicfFrQoSObjects,'hpnicfFrClassObjects':hpnicfFrClassObjects,'hpnicfFrClassIndexNext':hpnicfFrClassIndexNext,'hpnicfFrClassCfgInfoTable':hpnicfFrClassCfgInfoTable,'hpnicfFrClassCfgInfoEntry':hpnicfFrClassCfgInfoEntry,_J:hpnicfFrClassIndex,'hpnicfFrClassName':hpnicfFrClassName,'hpnicfFrClassRowStatus':hpnicfFrClassRowStatus,'hpnicfCirAllowCfgInfoTable':hpnicfCirAllowCfgInfoTable,'hpnicfCirAllowCfgInfoEntry':hpnicfCirAllowCfgInfoEntry,_K:hpnicfCirAllowFrClassIndex,_L:hpnicfCirAllowDirection,'hpnicfCirAllowValue':hpnicfCirAllowValue,'hpnicfCirAllowRowStatus':hpnicfCirAllowRowStatus,'hpnicfCirCfgInfoTable':hpnicfCirCfgInfoTable,'hpnicfCirCfgInfoEntry':hpnicfCirCfgInfoEntry,_M:hpnicfCirFrClassIndex,'hpnicfCirValue':hpnicfCirValue,'hpnicfCirRowStatus':hpnicfCirRowStatus,'hpnicfIfApplyFrClassTable':hpnicfIfApplyFrClassTable,'hpnicfIfApplyFrClassEntry':hpnicfIfApplyFrClassEntry,_N:hpnicfIfApplyFrClassIfIndex,'hpnicfIfApplyFrClassIndex':hpnicfIfApplyFrClassIndex,'hpnicfIfApplyFrClassRowStatus':hpnicfIfApplyFrClassRowStatus,'hpnicfPvcApplyFrClassTable':hpnicfPvcApplyFrClassTable,'hpnicfPvcApplyFrClassEntry':hpnicfPvcApplyFrClassEntry,_G:hpnicfPvcApplyFrClassIfIndex,_H:hpnicfPvcApplyFrClassDlciNum,'hpnicfPvcApplyFrClassIndex':hpnicfPvcApplyFrClassIndex,'hpnicfPvcApplyFrClassRowStatus':hpnicfPvcApplyFrClassRowStatus,'hpnicfFrPvcBandwidthTable':hpnicfFrPvcBandwidthTable,'hpnicfFrPvcBandwidthEntry':hpnicfFrPvcBandwidthEntry,'hpnicfFrPvcBandwidthMaxReservedBW':hpnicfFrPvcBandwidthMaxReservedBW,'hpnicfFrPvcBandwidthAvailable':hpnicfFrPvcBandwidthAvailable,'hpnicfRTPQoSObjects':hpnicfRTPQoSObjects,'hpnicfRTPFrClassApplyTable':hpnicfRTPFrClassApplyTable,'hpnicfRTPFrClassApplyEntry':hpnicfRTPFrClassApplyEntry,_O:hpnicfRTPFrClassApplyFrClassIndex,'hpnicfRTPFrClassApplyStartPort':hpnicfRTPFrClassApplyStartPort,'hpnicfRTPFrClassApplyEndPort':hpnicfRTPFrClassApplyEndPort,'hpnicfRTPFrClassApplyBandWidth':hpnicfRTPFrClassApplyBandWidth,'hpnicfRTPFrClassApplyCbs':hpnicfRTPFrClassApplyCbs,'hpnicfRTPFrClassApplyRowStatus':hpnicfRTPFrClassApplyRowStatus,'hpnicfRTPFrPvcQueueRunInfoTable':hpnicfRTPFrPvcQueueRunInfoTable,'hpnicfRTPFrPvcQueueRunInfoEntry':hpnicfRTPFrPvcQueueRunInfoEntry,'hpnicfRTPFrPvcQueueSize':hpnicfRTPFrPvcQueueSize,'hpnicfRTPFrPvcQueueMaxSize':hpnicfRTPFrPvcQueueMaxSize,'hpnicfRTPFrPvcQueueOutputs':hpnicfRTPFrPvcQueueOutputs,'hpnicfRTPFrPvcQueueDiscards':hpnicfRTPFrPvcQueueDiscards})