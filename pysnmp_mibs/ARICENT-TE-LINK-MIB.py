_M='fsTeLinkEntry'
_L='fsTeLinkBwThresholdIndex'
_K='disable'
_J='enable'
_I='TruthValue'
_H='DisplayString'
_G='ifIndex'
_F='IF-MIB'
_E='ARICENT-TE-LINK-MIB'
_D='read-create'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention',_I)
TeLinkBandwidth,teLinkEntry=mibBuilder.importSymbols('TE-LINK-STD-MIB','TeLinkBandwidth','teLinkEntry')
fstlm=ModuleIdentity((1,3,6,1,4,1,29601,2,67))
if mibBuilder.loadTexts:fstlm.setRevisions(('2012-09-17 00:00',))
_FsTlmSystem_ObjectIdentity=ObjectIdentity
fsTlmSystem=_FsTlmSystem_ObjectIdentity((1,3,6,1,4,1,29601,2,67,1))
class _FsTeLinkTraceOption_Type(Integer32):defaultValue=1
_FsTeLinkTraceOption_Type.__name__=_B
_FsTeLinkTraceOption_Object=MibScalar
fsTeLinkTraceOption=_FsTeLinkTraceOption_Object((1,3,6,1,4,1,29601,2,67,1,1),_FsTeLinkTraceOption_Type())
fsTeLinkTraceOption.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkTraceOption.setStatus(_A)
class _FsTeLinkModuleStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsTeLinkModuleStatus_Type.__name__=_B
_FsTeLinkModuleStatus_Object=MibScalar
fsTeLinkModuleStatus=_FsTeLinkModuleStatus_Object((1,3,6,1,4,1,29601,2,67,1,2),_FsTeLinkModuleStatus_Type())
fsTeLinkModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkModuleStatus.setStatus(_A)
_FsTeLinkConfigObjects_ObjectIdentity=ObjectIdentity
fsTeLinkConfigObjects=_FsTeLinkConfigObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,67,2))
_FsTeLinkTable_Object=MibTable
fsTeLinkTable=_FsTeLinkTable_Object((1,3,6,1,4,1,29601,2,67,2,1))
if mibBuilder.loadTexts:fsTeLinkTable.setStatus(_A)
_FsTeLinkEntry_Object=MibTableRow
fsTeLinkEntry=_FsTeLinkEntry_Object((1,3,6,1,4,1,29601,2,67,2,1,1))
if mibBuilder.loadTexts:fsTeLinkEntry.setStatus(_A)
class _FsTeLinkName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_FsTeLinkName_Type.__name__=_H
_FsTeLinkName_Object=MibTableColumn
fsTeLinkName=_FsTeLinkName_Object((1,3,6,1,4,1,29601,2,67,2,1,1,1),_FsTeLinkName_Type())
fsTeLinkName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTeLinkName.setStatus(_A)
_FsTeLinkRemoteRtrId_Type=IpAddress
_FsTeLinkRemoteRtrId_Object=MibTableColumn
fsTeLinkRemoteRtrId=_FsTeLinkRemoteRtrId_Object((1,3,6,1,4,1,29601,2,67,2,1,1,2),_FsTeLinkRemoteRtrId_Type())
fsTeLinkRemoteRtrId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTeLinkRemoteRtrId.setStatus(_A)
_FsTeLinkMaximumBandwidth_Type=TeLinkBandwidth
_FsTeLinkMaximumBandwidth_Object=MibTableColumn
fsTeLinkMaximumBandwidth=_FsTeLinkMaximumBandwidth_Object((1,3,6,1,4,1,29601,2,67,2,1,1,3),_FsTeLinkMaximumBandwidth_Type())
fsTeLinkMaximumBandwidth.setMaxAccess('read-only')
if mibBuilder.loadTexts:fsTeLinkMaximumBandwidth.setStatus(_A)
if mibBuilder.loadTexts:fsTeLinkMaximumBandwidth.setUnits('bps')
class _FsTeLinkType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unbundle',0),('bundle',1)))
_FsTeLinkType_Type.__name__=_B
_FsTeLinkType_Object=MibTableColumn
fsTeLinkType=_FsTeLinkType_Object((1,3,6,1,4,1,29601,2,67,2,1,1,4),_FsTeLinkType_Type())
fsTeLinkType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTeLinkType.setStatus(_A)
class _FsTeLinkInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forwardingAdjacenyChannel',0),('dataChannel',1),('dataAndControlChannel',2)))
_FsTeLinkInfoType_Type.__name__=_B
_FsTeLinkInfoType_Object=MibTableColumn
fsTeLinkInfoType=_FsTeLinkInfoType_Object((1,3,6,1,4,1,29601,2,67,2,1,1,5),_FsTeLinkInfoType_Type())
fsTeLinkInfoType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTeLinkInfoType.setStatus(_A)
class _FsTeLinkIfType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pointToPoint',1),('multiAccess',2)))
_FsTeLinkIfType_Type.__name__=_B
_FsTeLinkIfType_Object=MibTableColumn
fsTeLinkIfType=_FsTeLinkIfType_Object((1,3,6,1,4,1,29601,2,67,2,1,1,6),_FsTeLinkIfType_Type())
fsTeLinkIfType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTeLinkIfType.setStatus(_A)
class _FsTeLinkIsAdvertise_Type(TruthValue):defaultValue=1
_FsTeLinkIsAdvertise_Type.__name__=_I
_FsTeLinkIsAdvertise_Object=MibTableColumn
fsTeLinkIsAdvertise=_FsTeLinkIsAdvertise_Object((1,3,6,1,4,1,29601,2,67,2,1,1,7),_FsTeLinkIsAdvertise_Type())
fsTeLinkIsAdvertise.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTeLinkIsAdvertise.setStatus(_A)
_FsTeLinkBwThresholdTable_Object=MibTable
fsTeLinkBwThresholdTable=_FsTeLinkBwThresholdTable_Object((1,3,6,1,4,1,29601,2,67,2,2))
if mibBuilder.loadTexts:fsTeLinkBwThresholdTable.setStatus(_A)
_FsTeLinkBwThresholdEntry_Object=MibTableRow
fsTeLinkBwThresholdEntry=_FsTeLinkBwThresholdEntry_Object((1,3,6,1,4,1,29601,2,67,2,2,1))
fsTeLinkBwThresholdEntry.setIndexNames((0,_F,_G),(0,_E,_L))
if mibBuilder.loadTexts:fsTeLinkBwThresholdEntry.setStatus(_A)
class _FsTeLinkBwThresholdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_FsTeLinkBwThresholdIndex_Type.__name__=_B
_FsTeLinkBwThresholdIndex_Object=MibTableColumn
fsTeLinkBwThresholdIndex=_FsTeLinkBwThresholdIndex_Object((1,3,6,1,4,1,29601,2,67,2,2,1,1),_FsTeLinkBwThresholdIndex_Type())
fsTeLinkBwThresholdIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsTeLinkBwThresholdIndex.setStatus(_A)
class _FsTeLinkBwThreshold0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsTeLinkBwThreshold0_Type.__name__=_B
_FsTeLinkBwThreshold0_Object=MibTableColumn
fsTeLinkBwThreshold0=_FsTeLinkBwThreshold0_Object((1,3,6,1,4,1,29601,2,67,2,2,1,2),_FsTeLinkBwThreshold0_Type())
fsTeLinkBwThreshold0.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkBwThreshold0.setStatus(_A)
class _FsTeLinkBwThreshold1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsTeLinkBwThreshold1_Type.__name__=_B
_FsTeLinkBwThreshold1_Object=MibTableColumn
fsTeLinkBwThreshold1=_FsTeLinkBwThreshold1_Object((1,3,6,1,4,1,29601,2,67,2,2,1,3),_FsTeLinkBwThreshold1_Type())
fsTeLinkBwThreshold1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkBwThreshold1.setStatus(_A)
class _FsTeLinkBwThreshold2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsTeLinkBwThreshold2_Type.__name__=_B
_FsTeLinkBwThreshold2_Object=MibTableColumn
fsTeLinkBwThreshold2=_FsTeLinkBwThreshold2_Object((1,3,6,1,4,1,29601,2,67,2,2,1,4),_FsTeLinkBwThreshold2_Type())
fsTeLinkBwThreshold2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkBwThreshold2.setStatus(_A)
class _FsTeLinkBwThreshold3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsTeLinkBwThreshold3_Type.__name__=_B
_FsTeLinkBwThreshold3_Object=MibTableColumn
fsTeLinkBwThreshold3=_FsTeLinkBwThreshold3_Object((1,3,6,1,4,1,29601,2,67,2,2,1,5),_FsTeLinkBwThreshold3_Type())
fsTeLinkBwThreshold3.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkBwThreshold3.setStatus(_A)
class _FsTeLinkBwThreshold4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsTeLinkBwThreshold4_Type.__name__=_B
_FsTeLinkBwThreshold4_Object=MibTableColumn
fsTeLinkBwThreshold4=_FsTeLinkBwThreshold4_Object((1,3,6,1,4,1,29601,2,67,2,2,1,6),_FsTeLinkBwThreshold4_Type())
fsTeLinkBwThreshold4.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkBwThreshold4.setStatus(_A)
class _FsTeLinkBwThreshold5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsTeLinkBwThreshold5_Type.__name__=_B
_FsTeLinkBwThreshold5_Object=MibTableColumn
fsTeLinkBwThreshold5=_FsTeLinkBwThreshold5_Object((1,3,6,1,4,1,29601,2,67,2,2,1,7),_FsTeLinkBwThreshold5_Type())
fsTeLinkBwThreshold5.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkBwThreshold5.setStatus(_A)
class _FsTeLinkBwThreshold6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsTeLinkBwThreshold6_Type.__name__=_B
_FsTeLinkBwThreshold6_Object=MibTableColumn
fsTeLinkBwThreshold6=_FsTeLinkBwThreshold6_Object((1,3,6,1,4,1,29601,2,67,2,2,1,8),_FsTeLinkBwThreshold6_Type())
fsTeLinkBwThreshold6.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkBwThreshold6.setStatus(_A)
class _FsTeLinkBwThreshold7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsTeLinkBwThreshold7_Type.__name__=_B
_FsTeLinkBwThreshold7_Object=MibTableColumn
fsTeLinkBwThreshold7=_FsTeLinkBwThreshold7_Object((1,3,6,1,4,1,29601,2,67,2,2,1,9),_FsTeLinkBwThreshold7_Type())
fsTeLinkBwThreshold7.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkBwThreshold7.setStatus(_A)
class _FsTeLinkBwThreshold8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsTeLinkBwThreshold8_Type.__name__=_B
_FsTeLinkBwThreshold8_Object=MibTableColumn
fsTeLinkBwThreshold8=_FsTeLinkBwThreshold8_Object((1,3,6,1,4,1,29601,2,67,2,2,1,10),_FsTeLinkBwThreshold8_Type())
fsTeLinkBwThreshold8.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkBwThreshold8.setStatus(_A)
class _FsTeLinkBwThreshold9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsTeLinkBwThreshold9_Type.__name__=_B
_FsTeLinkBwThreshold9_Object=MibTableColumn
fsTeLinkBwThreshold9=_FsTeLinkBwThreshold9_Object((1,3,6,1,4,1,29601,2,67,2,2,1,11),_FsTeLinkBwThreshold9_Type())
fsTeLinkBwThreshold9.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkBwThreshold9.setStatus(_A)
class _FsTeLinkBwThreshold10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsTeLinkBwThreshold10_Type.__name__=_B
_FsTeLinkBwThreshold10_Object=MibTableColumn
fsTeLinkBwThreshold10=_FsTeLinkBwThreshold10_Object((1,3,6,1,4,1,29601,2,67,2,2,1,12),_FsTeLinkBwThreshold10_Type())
fsTeLinkBwThreshold10.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkBwThreshold10.setStatus(_A)
class _FsTeLinkBwThreshold11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsTeLinkBwThreshold11_Type.__name__=_B
_FsTeLinkBwThreshold11_Object=MibTableColumn
fsTeLinkBwThreshold11=_FsTeLinkBwThreshold11_Object((1,3,6,1,4,1,29601,2,67,2,2,1,13),_FsTeLinkBwThreshold11_Type())
fsTeLinkBwThreshold11.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkBwThreshold11.setStatus(_A)
class _FsTeLinkBwThreshold12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsTeLinkBwThreshold12_Type.__name__=_B
_FsTeLinkBwThreshold12_Object=MibTableColumn
fsTeLinkBwThreshold12=_FsTeLinkBwThreshold12_Object((1,3,6,1,4,1,29601,2,67,2,2,1,14),_FsTeLinkBwThreshold12_Type())
fsTeLinkBwThreshold12.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkBwThreshold12.setStatus(_A)
class _FsTeLinkBwThreshold13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsTeLinkBwThreshold13_Type.__name__=_B
_FsTeLinkBwThreshold13_Object=MibTableColumn
fsTeLinkBwThreshold13=_FsTeLinkBwThreshold13_Object((1,3,6,1,4,1,29601,2,67,2,2,1,15),_FsTeLinkBwThreshold13_Type())
fsTeLinkBwThreshold13.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkBwThreshold13.setStatus(_A)
class _FsTeLinkBwThreshold14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsTeLinkBwThreshold14_Type.__name__=_B
_FsTeLinkBwThreshold14_Object=MibTableColumn
fsTeLinkBwThreshold14=_FsTeLinkBwThreshold14_Object((1,3,6,1,4,1,29601,2,67,2,2,1,16),_FsTeLinkBwThreshold14_Type())
fsTeLinkBwThreshold14.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkBwThreshold14.setStatus(_A)
class _FsTeLinkBwThreshold15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsTeLinkBwThreshold15_Type.__name__=_B
_FsTeLinkBwThreshold15_Object=MibTableColumn
fsTeLinkBwThreshold15=_FsTeLinkBwThreshold15_Object((1,3,6,1,4,1,29601,2,67,2,2,1,17),_FsTeLinkBwThreshold15_Type())
fsTeLinkBwThreshold15.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkBwThreshold15.setStatus(_A)
_FsTeLinkBwThresholdRowStatus_Type=RowStatus
_FsTeLinkBwThresholdRowStatus_Object=MibTableColumn
fsTeLinkBwThresholdRowStatus=_FsTeLinkBwThresholdRowStatus_Object((1,3,6,1,4,1,29601,2,67,2,2,1,18),_FsTeLinkBwThresholdRowStatus_Type())
fsTeLinkBwThresholdRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTeLinkBwThresholdRowStatus.setStatus(_A)
class _FsTeLinkBwThresholdForceOption_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsTeLinkBwThresholdForceOption_Type.__name__=_B
_FsTeLinkBwThresholdForceOption_Object=MibScalar
fsTeLinkBwThresholdForceOption=_FsTeLinkBwThresholdForceOption_Object((1,3,6,1,4,1,29601,2,67,2,3),_FsTeLinkBwThresholdForceOption_Type())
fsTeLinkBwThresholdForceOption.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTeLinkBwThresholdForceOption.setStatus(_A)
teLinkEntry.registerAugmentions((_E,_M))
fsTeLinkEntry.setIndexNames(*teLinkEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'fstlm':fstlm,'fsTlmSystem':fsTlmSystem,'fsTeLinkTraceOption':fsTeLinkTraceOption,'fsTeLinkModuleStatus':fsTeLinkModuleStatus,'fsTeLinkConfigObjects':fsTeLinkConfigObjects,'fsTeLinkTable':fsTeLinkTable,_M:fsTeLinkEntry,'fsTeLinkName':fsTeLinkName,'fsTeLinkRemoteRtrId':fsTeLinkRemoteRtrId,'fsTeLinkMaximumBandwidth':fsTeLinkMaximumBandwidth,'fsTeLinkType':fsTeLinkType,'fsTeLinkInfoType':fsTeLinkInfoType,'fsTeLinkIfType':fsTeLinkIfType,'fsTeLinkIsAdvertise':fsTeLinkIsAdvertise,'fsTeLinkBwThresholdTable':fsTeLinkBwThresholdTable,'fsTeLinkBwThresholdEntry':fsTeLinkBwThresholdEntry,_L:fsTeLinkBwThresholdIndex,'fsTeLinkBwThreshold0':fsTeLinkBwThreshold0,'fsTeLinkBwThreshold1':fsTeLinkBwThreshold1,'fsTeLinkBwThreshold2':fsTeLinkBwThreshold2,'fsTeLinkBwThreshold3':fsTeLinkBwThreshold3,'fsTeLinkBwThreshold4':fsTeLinkBwThreshold4,'fsTeLinkBwThreshold5':fsTeLinkBwThreshold5,'fsTeLinkBwThreshold6':fsTeLinkBwThreshold6,'fsTeLinkBwThreshold7':fsTeLinkBwThreshold7,'fsTeLinkBwThreshold8':fsTeLinkBwThreshold8,'fsTeLinkBwThreshold9':fsTeLinkBwThreshold9,'fsTeLinkBwThreshold10':fsTeLinkBwThreshold10,'fsTeLinkBwThreshold11':fsTeLinkBwThreshold11,'fsTeLinkBwThreshold12':fsTeLinkBwThreshold12,'fsTeLinkBwThreshold13':fsTeLinkBwThreshold13,'fsTeLinkBwThreshold14':fsTeLinkBwThreshold14,'fsTeLinkBwThreshold15':fsTeLinkBwThreshold15,'fsTeLinkBwThresholdRowStatus':fsTeLinkBwThresholdRowStatus,'fsTeLinkBwThresholdForceOption':fsTeLinkBwThresholdForceOption})