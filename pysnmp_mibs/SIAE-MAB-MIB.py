_K='MabPduCompliance'
_J='mabPduSenderIndex'
_I='MabBwCalculationMethod'
_H='not-accessible'
_G='MacAddress'
_F='mabSensorIndex'
_E='read-only'
_D='SIAE-MAB-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_G,'PhysAddress','RowStatus','TextualConvention')
mabMib=ModuleIdentity((1,3,6,1,4,1,3373,1103,93))
if mibBuilder.loadTexts:mabMib.setRevisions(('2015-02-17 00:00',))
class MabBwCalculationMethod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('average',1),('min',2),('max',3)))
class MabPduCompliance(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stdMcmCompliant',1),('extMcmCompliant',2),('ituG8013Compliant',3)))
class MabSenderOption(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('enableAlways',0),('enableSignalFail',1)))
_MabMibVersion_Type=Integer32
_MabMibVersion_Object=MibScalar
mabMibVersion=_MabMibVersion_Object((1,3,6,1,4,1,3373,1103,93,1),_MabMibVersion_Type())
mabMibVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:mabMibVersion.setStatus(_A)
_MabSensorTable_Object=MibTable
mabSensorTable=_MabSensorTable_Object((1,3,6,1,4,1,3373,1103,93,2))
if mibBuilder.loadTexts:mabSensorTable.setStatus(_A)
_MabSensorEntry_Object=MibTableRow
mabSensorEntry=_MabSensorEntry_Object((1,3,6,1,4,1,3373,1103,93,2,1))
mabSensorEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:mabSensorEntry.setStatus(_A)
_MabSensorIndex_Type=Integer32
_MabSensorIndex_Object=MibTableColumn
mabSensorIndex=_MabSensorIndex_Object((1,3,6,1,4,1,3373,1103,93,2,1,1),_MabSensorIndex_Type())
mabSensorIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:mabSensorIndex.setStatus(_A)
_MabSensorRowStatus_Type=RowStatus
_MabSensorRowStatus_Object=MibTableColumn
mabSensorRowStatus=_MabSensorRowStatus_Object((1,3,6,1,4,1,3373,1103,93,2,1,2),_MabSensorRowStatus_Type())
mabSensorRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mabSensorRowStatus.setStatus(_A)
class _MabSensorAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_MabSensorAdminStatus_Type.__name__=_C
_MabSensorAdminStatus_Object=MibTableColumn
mabSensorAdminStatus=_MabSensorAdminStatus_Object((1,3,6,1,4,1,3373,1103,93,2,1,3),_MabSensorAdminStatus_Type())
mabSensorAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mabSensorAdminStatus.setStatus(_A)
_MabSensorIfIndex_Type=InterfaceIndex
_MabSensorIfIndex_Object=MibTableColumn
mabSensorIfIndex=_MabSensorIfIndex_Object((1,3,6,1,4,1,3373,1103,93,2,1,4),_MabSensorIfIndex_Type())
mabSensorIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mabSensorIfIndex.setStatus(_A)
_MabSensorLinkId_Type=Integer32
_MabSensorLinkId_Object=MibTableColumn
mabSensorLinkId=_MabSensorLinkId_Object((1,3,6,1,4,1,3373,1103,93,2,1,5),_MabSensorLinkId_Type())
mabSensorLinkId.setMaxAccess(_B)
if mibBuilder.loadTexts:mabSensorLinkId.setStatus(_A)
class _MabSensorBwMode_Type(MabBwCalculationMethod):defaultValue=1
_MabSensorBwMode_Type.__name__=_I
_MabSensorBwMode_Object=MibTableColumn
mabSensorBwMode=_MabSensorBwMode_Object((1,3,6,1,4,1,3373,1103,93,2,1,6),_MabSensorBwMode_Type())
mabSensorBwMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mabSensorBwMode.setStatus(_A)
class _MabSensorHoldoffTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,60))
_MabSensorHoldoffTime_Type.__name__=_C
_MabSensorHoldoffTime_Object=MibTableColumn
mabSensorHoldoffTime=_MabSensorHoldoffTime_Object((1,3,6,1,4,1,3373,1103,93,2,1,7),_MabSensorHoldoffTime_Type())
mabSensorHoldoffTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mabSensorHoldoffTime.setStatus(_A)
class _MabSensorObservationTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(10,10),ValueRangeConstraint(60,60))
_MabSensorObservationTime_Type.__name__=_C
_MabSensorObservationTime_Object=MibTableColumn
mabSensorObservationTime=_MabSensorObservationTime_Object((1,3,6,1,4,1,3373,1103,93,2,1,8),_MabSensorObservationTime_Type())
mabSensorObservationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mabSensorObservationTime.setStatus(_A)
class _MabSensorFastTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,59))
_MabSensorFastTime_Type.__name__=_C
_MabSensorFastTime_Object=MibTableColumn
mabSensorFastTime=_MabSensorFastTime_Object((1,3,6,1,4,1,3373,1103,93,2,1,9),_MabSensorFastTime_Type())
mabSensorFastTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mabSensorFastTime.setStatus(_A)
class _MabSensorFastCount_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_MabSensorFastCount_Type.__name__=_C
_MabSensorFastCount_Object=MibTableColumn
mabSensorFastCount=_MabSensorFastCount_Object((1,3,6,1,4,1,3373,1103,93,2,1,10),_MabSensorFastCount_Type())
mabSensorFastCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mabSensorFastCount.setStatus(_A)
_MabSensorStatusTable_Object=MibTable
mabSensorStatusTable=_MabSensorStatusTable_Object((1,3,6,1,4,1,3373,1103,93,3))
if mibBuilder.loadTexts:mabSensorStatusTable.setStatus(_A)
_MabSensorStatusEntry_Object=MibTableRow
mabSensorStatusEntry=_MabSensorStatusEntry_Object((1,3,6,1,4,1,3373,1103,93,3,1))
mabSensorStatusEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:mabSensorStatusEntry.setStatus(_A)
_MabSensorNominalBw_Type=Integer32
_MabSensorNominalBw_Object=MibTableColumn
mabSensorNominalBw=_MabSensorNominalBw_Object((1,3,6,1,4,1,3373,1103,93,3,1,1),_MabSensorNominalBw_Type())
mabSensorNominalBw.setMaxAccess(_E)
if mibBuilder.loadTexts:mabSensorNominalBw.setStatus(_A)
_MabSensorCurrentBw_Type=Integer32
_MabSensorCurrentBw_Object=MibTableColumn
mabSensorCurrentBw=_MabSensorCurrentBw_Object((1,3,6,1,4,1,3373,1103,93,3,1,2),_MabSensorCurrentBw_Type())
mabSensorCurrentBw.setMaxAccess(_E)
if mibBuilder.loadTexts:mabSensorCurrentBw.setStatus(_A)
_MabPduSenderTable_Object=MibTable
mabPduSenderTable=_MabPduSenderTable_Object((1,3,6,1,4,1,3373,1103,93,4))
if mibBuilder.loadTexts:mabPduSenderTable.setStatus(_A)
_MabPduSenderEntry_Object=MibTableRow
mabPduSenderEntry=_MabPduSenderEntry_Object((1,3,6,1,4,1,3373,1103,93,4,1))
mabPduSenderEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:mabPduSenderEntry.setStatus(_A)
_MabPduSenderIndex_Type=Integer32
_MabPduSenderIndex_Object=MibTableColumn
mabPduSenderIndex=_MabPduSenderIndex_Object((1,3,6,1,4,1,3373,1103,93,4,1,1),_MabPduSenderIndex_Type())
mabPduSenderIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:mabPduSenderIndex.setStatus(_A)
_MabPduSenderRowStatus_Type=RowStatus
_MabPduSenderRowStatus_Object=MibTableColumn
mabPduSenderRowStatus=_MabPduSenderRowStatus_Object((1,3,6,1,4,1,3373,1103,93,4,1,2),_MabPduSenderRowStatus_Type())
mabPduSenderRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mabPduSenderRowStatus.setStatus(_A)
class _MabPduSenderAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_MabPduSenderAdminStatus_Type.__name__=_C
_MabPduSenderAdminStatus_Object=MibTableColumn
mabPduSenderAdminStatus=_MabPduSenderAdminStatus_Object((1,3,6,1,4,1,3373,1103,93,4,1,3),_MabPduSenderAdminStatus_Type())
mabPduSenderAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mabPduSenderAdminStatus.setStatus(_A)
_MabPduSenderIfIndex_Type=InterfaceIndex
_MabPduSenderIfIndex_Object=MibTableColumn
mabPduSenderIfIndex=_MabPduSenderIfIndex_Object((1,3,6,1,4,1,3373,1103,93,4,1,4),_MabPduSenderIfIndex_Type())
mabPduSenderIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mabPduSenderIfIndex.setStatus(_A)
_MabPduSenderSensorIndex_Type=Integer32
_MabPduSenderSensorIndex_Object=MibTableColumn
mabPduSenderSensorIndex=_MabPduSenderSensorIndex_Object((1,3,6,1,4,1,3373,1103,93,4,1,5),_MabPduSenderSensorIndex_Type())
mabPduSenderSensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mabPduSenderSensorIndex.setStatus(_A)
class _MabPduSenderVlanId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094))
_MabPduSenderVlanId_Type.__name__=_C
_MabPduSenderVlanId_Object=MibTableColumn
mabPduSenderVlanId=_MabPduSenderVlanId_Object((1,3,6,1,4,1,3373,1103,93,4,1,6),_MabPduSenderVlanId_Type())
mabPduSenderVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:mabPduSenderVlanId.setStatus(_A)
class _MabPduSenderPcp_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MabPduSenderPcp_Type.__name__=_C
_MabPduSenderPcp_Object=MibTableColumn
mabPduSenderPcp=_MabPduSenderPcp_Object((1,3,6,1,4,1,3373,1103,93,4,1,7),_MabPduSenderPcp_Type())
mabPduSenderPcp.setMaxAccess(_B)
if mibBuilder.loadTexts:mabPduSenderPcp.setStatus(_A)
class _MabPduSenderOamMaintLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MabPduSenderOamMaintLevel_Type.__name__=_C
_MabPduSenderOamMaintLevel_Object=MibTableColumn
mabPduSenderOamMaintLevel=_MabPduSenderOamMaintLevel_Object((1,3,6,1,4,1,3373,1103,93,4,1,8),_MabPduSenderOamMaintLevel_Type())
mabPduSenderOamMaintLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:mabPduSenderOamMaintLevel.setStatus(_A)
class _MabPduSenderDAType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('multicastDA',1),('unicastDA',2)))
_MabPduSenderDAType_Type.__name__=_C
_MabPduSenderDAType_Object=MibTableColumn
mabPduSenderDAType=_MabPduSenderDAType_Object((1,3,6,1,4,1,3373,1103,93,4,1,9),_MabPduSenderDAType_Type())
mabPduSenderDAType.setMaxAccess(_B)
if mibBuilder.loadTexts:mabPduSenderDAType.setStatus(_A)
class _MabPduSenderUnicastDA_Type(MacAddress):defaultHexValue='000000000000'
_MabPduSenderUnicastDA_Type.__name__=_G
_MabPduSenderUnicastDA_Object=MibTableColumn
mabPduSenderUnicastDA=_MabPduSenderUnicastDA_Object((1,3,6,1,4,1,3373,1103,93,4,1,10),_MabPduSenderUnicastDA_Type())
mabPduSenderUnicastDA.setMaxAccess(_B)
if mibBuilder.loadTexts:mabPduSenderUnicastDA.setStatus(_A)
_MabPduSenderOption_Type=MabSenderOption
_MabPduSenderOption_Object=MibTableColumn
mabPduSenderOption=_MabPduSenderOption_Object((1,3,6,1,4,1,3373,1103,93,4,1,11),_MabPduSenderOption_Type())
mabPduSenderOption.setMaxAccess(_B)
if mibBuilder.loadTexts:mabPduSenderOption.setStatus(_A)
class _MabPduSenderPduCompliance_Type(MabPduCompliance):defaultValue=1
_MabPduSenderPduCompliance_Type.__name__=_K
_MabPduSenderPduCompliance_Object=MibTableColumn
mabPduSenderPduCompliance=_MabPduSenderPduCompliance_Object((1,3,6,1,4,1,3373,1103,93,4,1,12),_MabPduSenderPduCompliance_Type())
mabPduSenderPduCompliance.setMaxAccess(_B)
if mibBuilder.loadTexts:mabPduSenderPduCompliance.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_I:MabBwCalculationMethod,_K:MabPduCompliance,'MabSenderOption':MabSenderOption,'mabMib':mabMib,'mabMibVersion':mabMibVersion,'mabSensorTable':mabSensorTable,'mabSensorEntry':mabSensorEntry,_F:mabSensorIndex,'mabSensorRowStatus':mabSensorRowStatus,'mabSensorAdminStatus':mabSensorAdminStatus,'mabSensorIfIndex':mabSensorIfIndex,'mabSensorLinkId':mabSensorLinkId,'mabSensorBwMode':mabSensorBwMode,'mabSensorHoldoffTime':mabSensorHoldoffTime,'mabSensorObservationTime':mabSensorObservationTime,'mabSensorFastTime':mabSensorFastTime,'mabSensorFastCount':mabSensorFastCount,'mabSensorStatusTable':mabSensorStatusTable,'mabSensorStatusEntry':mabSensorStatusEntry,'mabSensorNominalBw':mabSensorNominalBw,'mabSensorCurrentBw':mabSensorCurrentBw,'mabPduSenderTable':mabPduSenderTable,'mabPduSenderEntry':mabPduSenderEntry,_J:mabPduSenderIndex,'mabPduSenderRowStatus':mabPduSenderRowStatus,'mabPduSenderAdminStatus':mabPduSenderAdminStatus,'mabPduSenderIfIndex':mabPduSenderIfIndex,'mabPduSenderSensorIndex':mabPduSenderSensorIndex,'mabPduSenderVlanId':mabPduSenderVlanId,'mabPduSenderPcp':mabPduSenderPcp,'mabPduSenderOamMaintLevel':mabPduSenderOamMaintLevel,'mabPduSenderDAType':mabPduSenderDAType,'mabPduSenderUnicastDA':mabPduSenderUnicastDA,'mabPduSenderOption':mabPduSenderOption,'mabPduSenderPduCompliance':mabPduSenderPduCompliance})