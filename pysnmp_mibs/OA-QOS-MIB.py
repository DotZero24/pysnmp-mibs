_R='oaQoSPermVPTServiceLevel'
_Q='oaQoSPermTOSServiceLevel'
_P='oaQoSPermQParamsQueueNumber'
_O='oaQoSVPTServiceLevel'
_N='oaQoSTOSServiceLevel'
_M='oaQoSQParamsQueueNumber'
_L='hybrid2sp2wrr'
_K='hybrid1sp3wrr'
_J='perOctets'
_I='perPackets'
_H='oaQoSModuleId'
_G='oaQoSSlotId'
_F='other'
_E='read-write'
_D='OA-QOS-MIB'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Oaccess_ObjectIdentity=ObjectIdentity
oaccess=_Oaccess_ObjectIdentity((1,3,6,1,4,1,6926))
_OaManagement_ObjectIdentity=ObjectIdentity
oaManagement=_OaManagement_ObjectIdentity((1,3,6,1,4,1,6926,1))
_OaClassification_ObjectIdentity=ObjectIdentity
oaClassification=_OaClassification_ObjectIdentity((1,3,6,1,4,1,6926,1,21))
_OaQoS_ObjectIdentity=ObjectIdentity
oaQoS=_OaQoS_ObjectIdentity((1,3,6,1,4,1,6926,1,21,2))
class _OaQoSSaveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('allQoSParams',2)))
_OaQoSSaveMode_Type.__name__=_B
_OaQoSSaveMode_Object=MibScalar
oaQoSSaveMode=_OaQoSSaveMode_Object((1,3,6,1,4,1,6926,1,21,2,1),_OaQoSSaveMode_Type())
oaQoSSaveMode.setMaxAccess(_E)
if mibBuilder.loadTexts:oaQoSSaveMode.setStatus(_A)
_OaQoSMaxPriorQueuesNumber_Type=Integer32
_OaQoSMaxPriorQueuesNumber_Object=MibScalar
oaQoSMaxPriorQueuesNumber=_OaQoSMaxPriorQueuesNumber_Object((1,3,6,1,4,1,6926,1,21,2,2),_OaQoSMaxPriorQueuesNumber_Type())
oaQoSMaxPriorQueuesNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:oaQoSMaxPriorQueuesNumber.setStatus(_A)
_OaQoSModuleStatusTable_Object=MibTable
oaQoSModuleStatusTable=_OaQoSModuleStatusTable_Object((1,3,6,1,4,1,6926,1,21,2,3))
if mibBuilder.loadTexts:oaQoSModuleStatusTable.setStatus(_A)
_OaQoSModuleStatusEntry_Object=MibTableRow
oaQoSModuleStatusEntry=_OaQoSModuleStatusEntry_Object((1,3,6,1,4,1,6926,1,21,2,3,1))
oaQoSModuleStatusEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:oaQoSModuleStatusEntry.setStatus(_A)
_OaQoSSlotId_Type=Integer32
_OaQoSSlotId_Object=MibTableColumn
oaQoSSlotId=_OaQoSSlotId_Object((1,3,6,1,4,1,6926,1,21,2,3,1,1),_OaQoSSlotId_Type())
oaQoSSlotId.setMaxAccess(_C)
if mibBuilder.loadTexts:oaQoSSlotId.setStatus(_A)
_OaQoSModuleId_Type=Integer32
_OaQoSModuleId_Object=MibTableColumn
oaQoSModuleId=_OaQoSModuleId_Object((1,3,6,1,4,1,6926,1,21,2,3,1,2),_OaQoSModuleId_Type())
oaQoSModuleId.setMaxAccess(_C)
if mibBuilder.loadTexts:oaQoSModuleId.setStatus(_A)
class _OaQoSModuleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('supported',2),('notSupported',3)))
_OaQoSModuleStatus_Type.__name__=_B
_OaQoSModuleStatus_Object=MibTableColumn
oaQoSModuleStatus=_OaQoSModuleStatus_Object((1,3,6,1,4,1,6926,1,21,2,3,1,3),_OaQoSModuleStatus_Type())
oaQoSModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oaQoSModuleStatus.setStatus(_A)
_OaQoSRun_ObjectIdentity=ObjectIdentity
oaQoSRun=_OaQoSRun_ObjectIdentity((1,3,6,1,4,1,6926,1,21,2,10))
class _OaQoSCounterMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3)))
_OaQoSCounterMode_Type.__name__=_B
_OaQoSCounterMode_Object=MibScalar
oaQoSCounterMode=_OaQoSCounterMode_Object((1,3,6,1,4,1,6926,1,21,2,10,1),_OaQoSCounterMode_Type())
oaQoSCounterMode.setMaxAccess(_E)
if mibBuilder.loadTexts:oaQoSCounterMode.setStatus(_A)
class _OaQoSTxSchedAlg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('wrr',2),(_K,3),(_L,4),('sp',5)))
_OaQoSTxSchedAlg_Type.__name__=_B
_OaQoSTxSchedAlg_Object=MibScalar
oaQoSTxSchedAlg=_OaQoSTxSchedAlg_Object((1,3,6,1,4,1,6926,1,21,2,10,2),_OaQoSTxSchedAlg_Type())
oaQoSTxSchedAlg.setMaxAccess(_E)
if mibBuilder.loadTexts:oaQoSTxSchedAlg.setStatus(_A)
_OaQoSQParamsTable_Object=MibTable
oaQoSQParamsTable=_OaQoSQParamsTable_Object((1,3,6,1,4,1,6926,1,21,2,10,6))
if mibBuilder.loadTexts:oaQoSQParamsTable.setStatus(_A)
_OaQoSQParamsEntry_Object=MibTableRow
oaQoSQParamsEntry=_OaQoSQParamsEntry_Object((1,3,6,1,4,1,6926,1,21,2,10,6,1))
oaQoSQParamsEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:oaQoSQParamsEntry.setStatus(_A)
_OaQoSQParamsQueueNumber_Type=Integer32
_OaQoSQParamsQueueNumber_Object=MibTableColumn
oaQoSQParamsQueueNumber=_OaQoSQParamsQueueNumber_Object((1,3,6,1,4,1,6926,1,21,2,10,6,1,1),_OaQoSQParamsQueueNumber_Type())
oaQoSQParamsQueueNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:oaQoSQParamsQueueNumber.setStatus(_A)
class _OaQoSQParamsQueueWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OaQoSQParamsQueueWeight_Type.__name__=_B
_OaQoSQParamsQueueWeight_Object=MibTableColumn
oaQoSQParamsQueueWeight=_OaQoSQParamsQueueWeight_Object((1,3,6,1,4,1,6926,1,21,2,10,6,1,2),_OaQoSQParamsQueueWeight_Type())
oaQoSQParamsQueueWeight.setMaxAccess(_E)
if mibBuilder.loadTexts:oaQoSQParamsQueueWeight.setStatus(_A)
_OaQoSTOSCfgTable_Object=MibTable
oaQoSTOSCfgTable=_OaQoSTOSCfgTable_Object((1,3,6,1,4,1,6926,1,21,2,10,9))
if mibBuilder.loadTexts:oaQoSTOSCfgTable.setStatus(_A)
_OaQoSTOSCfgEntry_Object=MibTableRow
oaQoSTOSCfgEntry=_OaQoSTOSCfgEntry_Object((1,3,6,1,4,1,6926,1,21,2,10,9,1))
oaQoSTOSCfgEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:oaQoSTOSCfgEntry.setStatus(_A)
class _OaQoSTOSServiceLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_OaQoSTOSServiceLevel_Type.__name__=_B
_OaQoSTOSServiceLevel_Object=MibTableColumn
oaQoSTOSServiceLevel=_OaQoSTOSServiceLevel_Object((1,3,6,1,4,1,6926,1,21,2,10,9,1,1),_OaQoSTOSServiceLevel_Type())
oaQoSTOSServiceLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oaQoSTOSServiceLevel.setStatus(_A)
class _OaQoSTOSvalue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_OaQoSTOSvalue_Type.__name__=_B
_OaQoSTOSvalue_Object=MibTableColumn
oaQoSTOSvalue=_OaQoSTOSvalue_Object((1,3,6,1,4,1,6926,1,21,2,10,9,1,2),_OaQoSTOSvalue_Type())
oaQoSTOSvalue.setMaxAccess(_E)
if mibBuilder.loadTexts:oaQoSTOSvalue.setStatus(_A)
class _OaQoSTOSvalueAfterReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_OaQoSTOSvalueAfterReset_Type.__name__=_B
_OaQoSTOSvalueAfterReset_Object=MibTableColumn
oaQoSTOSvalueAfterReset=_OaQoSTOSvalueAfterReset_Object((1,3,6,1,4,1,6926,1,21,2,10,9,1,3),_OaQoSTOSvalueAfterReset_Type())
oaQoSTOSvalueAfterReset.setMaxAccess(_E)
if mibBuilder.loadTexts:oaQoSTOSvalueAfterReset.setStatus(_A)
class _OaQoSTOSvalueDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_OaQoSTOSvalueDefault_Type.__name__=_B
_OaQoSTOSvalueDefault_Object=MibTableColumn
oaQoSTOSvalueDefault=_OaQoSTOSvalueDefault_Object((1,3,6,1,4,1,6926,1,21,2,10,9,1,4),_OaQoSTOSvalueDefault_Type())
oaQoSTOSvalueDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:oaQoSTOSvalueDefault.setStatus(_A)
_OaQoSVPTCfgTable_Object=MibTable
oaQoSVPTCfgTable=_OaQoSVPTCfgTable_Object((1,3,6,1,4,1,6926,1,21,2,10,10))
if mibBuilder.loadTexts:oaQoSVPTCfgTable.setStatus(_A)
_OaQoSVPTCfgEntry_Object=MibTableRow
oaQoSVPTCfgEntry=_OaQoSVPTCfgEntry_Object((1,3,6,1,4,1,6926,1,21,2,10,10,1))
oaQoSVPTCfgEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:oaQoSVPTCfgEntry.setStatus(_A)
class _OaQoSVPTServiceLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_OaQoSVPTServiceLevel_Type.__name__=_B
_OaQoSVPTServiceLevel_Object=MibTableColumn
oaQoSVPTServiceLevel=_OaQoSVPTServiceLevel_Object((1,3,6,1,4,1,6926,1,21,2,10,10,1,1),_OaQoSVPTServiceLevel_Type())
oaQoSVPTServiceLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oaQoSVPTServiceLevel.setStatus(_A)
class _OaQoSVPTvalue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_OaQoSVPTvalue_Type.__name__=_B
_OaQoSVPTvalue_Object=MibTableColumn
oaQoSVPTvalue=_OaQoSVPTvalue_Object((1,3,6,1,4,1,6926,1,21,2,10,10,1,2),_OaQoSVPTvalue_Type())
oaQoSVPTvalue.setMaxAccess(_E)
if mibBuilder.loadTexts:oaQoSVPTvalue.setStatus(_A)
class _OaQoSVPTvalueAfterReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_OaQoSVPTvalueAfterReset_Type.__name__=_B
_OaQoSVPTvalueAfterReset_Object=MibTableColumn
oaQoSVPTvalueAfterReset=_OaQoSVPTvalueAfterReset_Object((1,3,6,1,4,1,6926,1,21,2,10,10,1,3),_OaQoSVPTvalueAfterReset_Type())
oaQoSVPTvalueAfterReset.setMaxAccess(_E)
if mibBuilder.loadTexts:oaQoSVPTvalueAfterReset.setStatus(_A)
class _OaQoSVPTvalueDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_OaQoSVPTvalueDefault_Type.__name__=_B
_OaQoSVPTvalueDefault_Object=MibTableColumn
oaQoSVPTvalueDefault=_OaQoSVPTvalueDefault_Object((1,3,6,1,4,1,6926,1,21,2,10,10,1,4),_OaQoSVPTvalueDefault_Type())
oaQoSVPTvalueDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:oaQoSVPTvalueDefault.setStatus(_A)
_OaQoSPerm_ObjectIdentity=ObjectIdentity
oaQoSPerm=_OaQoSPerm_ObjectIdentity((1,3,6,1,4,1,6926,1,21,2,11))
class _OaQoSPermCounterMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3)))
_OaQoSPermCounterMode_Type.__name__=_B
_OaQoSPermCounterMode_Object=MibScalar
oaQoSPermCounterMode=_OaQoSPermCounterMode_Object((1,3,6,1,4,1,6926,1,21,2,11,1),_OaQoSPermCounterMode_Type())
oaQoSPermCounterMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oaQoSPermCounterMode.setStatus(_A)
class _OaQoSPermTxSchedAlg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('wrr',2),(_K,3),(_L,4),('sp',5)))
_OaQoSPermTxSchedAlg_Type.__name__=_B
_OaQoSPermTxSchedAlg_Object=MibScalar
oaQoSPermTxSchedAlg=_OaQoSPermTxSchedAlg_Object((1,3,6,1,4,1,6926,1,21,2,11,2),_OaQoSPermTxSchedAlg_Type())
oaQoSPermTxSchedAlg.setMaxAccess(_C)
if mibBuilder.loadTexts:oaQoSPermTxSchedAlg.setStatus(_A)
_OaQoSPermQParamsTable_Object=MibTable
oaQoSPermQParamsTable=_OaQoSPermQParamsTable_Object((1,3,6,1,4,1,6926,1,21,2,11,6))
if mibBuilder.loadTexts:oaQoSPermQParamsTable.setStatus(_A)
_OaQoSPermQParamsEntry_Object=MibTableRow
oaQoSPermQParamsEntry=_OaQoSPermQParamsEntry_Object((1,3,6,1,4,1,6926,1,21,2,11,6,1))
oaQoSPermQParamsEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:oaQoSPermQParamsEntry.setStatus(_A)
_OaQoSPermQParamsQueueNumber_Type=Integer32
_OaQoSPermQParamsQueueNumber_Object=MibTableColumn
oaQoSPermQParamsQueueNumber=_OaQoSPermQParamsQueueNumber_Object((1,3,6,1,4,1,6926,1,21,2,11,6,1,1),_OaQoSPermQParamsQueueNumber_Type())
oaQoSPermQParamsQueueNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:oaQoSPermQParamsQueueNumber.setStatus(_A)
class _OaQoSPermQParamsQueueWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OaQoSPermQParamsQueueWeight_Type.__name__=_B
_OaQoSPermQParamsQueueWeight_Object=MibTableColumn
oaQoSPermQParamsQueueWeight=_OaQoSPermQParamsQueueWeight_Object((1,3,6,1,4,1,6926,1,21,2,11,6,1,2),_OaQoSPermQParamsQueueWeight_Type())
oaQoSPermQParamsQueueWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:oaQoSPermQParamsQueueWeight.setStatus(_A)
_OaQoSPermTOSCfgTable_Object=MibTable
oaQoSPermTOSCfgTable=_OaQoSPermTOSCfgTable_Object((1,3,6,1,4,1,6926,1,21,2,11,9))
if mibBuilder.loadTexts:oaQoSPermTOSCfgTable.setStatus(_A)
_OaQoSPermTOSCfgEntry_Object=MibTableRow
oaQoSPermTOSCfgEntry=_OaQoSPermTOSCfgEntry_Object((1,3,6,1,4,1,6926,1,21,2,11,9,1))
oaQoSPermTOSCfgEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:oaQoSPermTOSCfgEntry.setStatus(_A)
class _OaQoSPermTOSServiceLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_OaQoSPermTOSServiceLevel_Type.__name__=_B
_OaQoSPermTOSServiceLevel_Object=MibTableColumn
oaQoSPermTOSServiceLevel=_OaQoSPermTOSServiceLevel_Object((1,3,6,1,4,1,6926,1,21,2,11,9,1,1),_OaQoSPermTOSServiceLevel_Type())
oaQoSPermTOSServiceLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oaQoSPermTOSServiceLevel.setStatus(_A)
class _OaQoSPermTOSvalue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_OaQoSPermTOSvalue_Type.__name__=_B
_OaQoSPermTOSvalue_Object=MibTableColumn
oaQoSPermTOSvalue=_OaQoSPermTOSvalue_Object((1,3,6,1,4,1,6926,1,21,2,11,9,1,2),_OaQoSPermTOSvalue_Type())
oaQoSPermTOSvalue.setMaxAccess(_C)
if mibBuilder.loadTexts:oaQoSPermTOSvalue.setStatus(_A)
_OaQoSPermVPTCfgTable_Object=MibTable
oaQoSPermVPTCfgTable=_OaQoSPermVPTCfgTable_Object((1,3,6,1,4,1,6926,1,21,2,11,10))
if mibBuilder.loadTexts:oaQoSPermVPTCfgTable.setStatus(_A)
_OaQoSPermVPTCfgEntry_Object=MibTableRow
oaQoSPermVPTCfgEntry=_OaQoSPermVPTCfgEntry_Object((1,3,6,1,4,1,6926,1,21,2,11,10,1))
oaQoSPermVPTCfgEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:oaQoSPermVPTCfgEntry.setStatus(_A)
class _OaQoSPermVPTServiceLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_OaQoSPermVPTServiceLevel_Type.__name__=_B
_OaQoSPermVPTServiceLevel_Object=MibTableColumn
oaQoSPermVPTServiceLevel=_OaQoSPermVPTServiceLevel_Object((1,3,6,1,4,1,6926,1,21,2,11,10,1,1),_OaQoSPermVPTServiceLevel_Type())
oaQoSPermVPTServiceLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oaQoSPermVPTServiceLevel.setStatus(_A)
class _OaQoSPermVPTvalue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_OaQoSPermVPTvalue_Type.__name__=_B
_OaQoSPermVPTvalue_Object=MibTableColumn
oaQoSPermVPTvalue=_OaQoSPermVPTvalue_Object((1,3,6,1,4,1,6926,1,21,2,11,10,1,2),_OaQoSPermVPTvalue_Type())
oaQoSPermVPTvalue.setMaxAccess(_C)
if mibBuilder.loadTexts:oaQoSPermVPTvalue.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'oaccess':oaccess,'oaManagement':oaManagement,'oaClassification':oaClassification,'oaQoS':oaQoS,'oaQoSSaveMode':oaQoSSaveMode,'oaQoSMaxPriorQueuesNumber':oaQoSMaxPriorQueuesNumber,'oaQoSModuleStatusTable':oaQoSModuleStatusTable,'oaQoSModuleStatusEntry':oaQoSModuleStatusEntry,_G:oaQoSSlotId,_H:oaQoSModuleId,'oaQoSModuleStatus':oaQoSModuleStatus,'oaQoSRun':oaQoSRun,'oaQoSCounterMode':oaQoSCounterMode,'oaQoSTxSchedAlg':oaQoSTxSchedAlg,'oaQoSQParamsTable':oaQoSQParamsTable,'oaQoSQParamsEntry':oaQoSQParamsEntry,_M:oaQoSQParamsQueueNumber,'oaQoSQParamsQueueWeight':oaQoSQParamsQueueWeight,'oaQoSTOSCfgTable':oaQoSTOSCfgTable,'oaQoSTOSCfgEntry':oaQoSTOSCfgEntry,_N:oaQoSTOSServiceLevel,'oaQoSTOSvalue':oaQoSTOSvalue,'oaQoSTOSvalueAfterReset':oaQoSTOSvalueAfterReset,'oaQoSTOSvalueDefault':oaQoSTOSvalueDefault,'oaQoSVPTCfgTable':oaQoSVPTCfgTable,'oaQoSVPTCfgEntry':oaQoSVPTCfgEntry,_O:oaQoSVPTServiceLevel,'oaQoSVPTvalue':oaQoSVPTvalue,'oaQoSVPTvalueAfterReset':oaQoSVPTvalueAfterReset,'oaQoSVPTvalueDefault':oaQoSVPTvalueDefault,'oaQoSPerm':oaQoSPerm,'oaQoSPermCounterMode':oaQoSPermCounterMode,'oaQoSPermTxSchedAlg':oaQoSPermTxSchedAlg,'oaQoSPermQParamsTable':oaQoSPermQParamsTable,'oaQoSPermQParamsEntry':oaQoSPermQParamsEntry,_P:oaQoSPermQParamsQueueNumber,'oaQoSPermQParamsQueueWeight':oaQoSPermQParamsQueueWeight,'oaQoSPermTOSCfgTable':oaQoSPermTOSCfgTable,'oaQoSPermTOSCfgEntry':oaQoSPermTOSCfgEntry,_Q:oaQoSPermTOSServiceLevel,'oaQoSPermTOSvalue':oaQoSPermTOSvalue,'oaQoSPermVPTCfgTable':oaQoSPermVPTCfgTable,'oaQoSPermVPTCfgEntry':oaQoSPermVPTCfgEntry,_R:oaQoSPermVPTServiceLevel,'oaQoSPermVPTvalue':oaQoSPermVPTvalue})