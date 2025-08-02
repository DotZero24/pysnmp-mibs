_I='linfIndex'
_H='nodeIfConfIndex'
_G='testing'
_F='notInstalled'
_E='A100-R1-MIB'
_D='read-write'
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
_Nec_ObjectIdentity=ObjectIdentity
nec=_Nec_ObjectIdentity((1,3,6,1,4,1,119))
_Nec_mib_ObjectIdentity=ObjectIdentity
nec_mib=_Nec_mib_ObjectIdentity((1,3,6,1,4,1,119,2))
_NecProductDepend_ObjectIdentity=ObjectIdentity
necProductDepend=_NecProductDepend_ObjectIdentity((1,3,6,1,4,1,119,2,3))
_Atomis_mib_ObjectIdentity=ObjectIdentity
atomis_mib=_Atomis_mib_ObjectIdentity((1,3,6,1,4,1,119,2,3,14))
_M5core_mib_ObjectIdentity=ObjectIdentity
m5core_mib=_M5core_mib_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,3))
_Node_ObjectIdentity=ObjectIdentity
node=_Node_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,3,1))
class _NodeOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('down',1),('active',2),('off-line',3),(_G,4),('initializing',5)))
_NodeOperStatus_Type.__name__=_B
_NodeOperStatus_Object=MibScalar
nodeOperStatus=_NodeOperStatus_Object((1,3,6,1,4,1,119,2,3,14,3,1,1),_NodeOperStatus_Type())
nodeOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeOperStatus.setStatus(_A)
_NodeIfConfTable_Object=MibTable
nodeIfConfTable=_NodeIfConfTable_Object((1,3,6,1,4,1,119,2,3,14,3,1,2))
if mibBuilder.loadTexts:nodeIfConfTable.setStatus(_A)
_NodeIfConfEntry_Object=MibTableRow
nodeIfConfEntry=_NodeIfConfEntry_Object((1,3,6,1,4,1,119,2,3,14,3,1,2,1))
nodeIfConfEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:nodeIfConfEntry.setStatus(_A)
_NodeIfConfIndex_Type=Integer32
_NodeIfConfIndex_Object=MibTableColumn
nodeIfConfIndex=_NodeIfConfIndex_Object((1,3,6,1,4,1,119,2,3,14,3,1,2,1,1),_NodeIfConfIndex_Type())
nodeIfConfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeIfConfIndex.setStatus(_A)
class _NodeIfConfPhysType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,99)));namedValues=NamedValues(*(('other',1),('sar',2),('taxi100M',3),('oc3cSMF',4),('oc-3cMMF',5),('ds3-PLCP-SCRAMBLE',6),('ds3-PLCP-noScramble',7),('relay-6Mcel',8),(_F,99)))
_NodeIfConfPhysType_Type.__name__=_B
_NodeIfConfPhysType_Object=MibTableColumn
nodeIfConfPhysType=_NodeIfConfPhysType_Object((1,3,6,1,4,1,119,2,3,14,3,1,2,1,2),_NodeIfConfPhysType_Type())
nodeIfConfPhysType.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeIfConfPhysType.setStatus(_A)
_NodeIfConfRev_Type=DisplayString
_NodeIfConfRev_Object=MibTableColumn
nodeIfConfRev=_NodeIfConfRev_Object((1,3,6,1,4,1,119,2,3,14,3,1,2,1,3),_NodeIfConfRev_Type())
nodeIfConfRev.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeIfConfRev.setStatus(_A)
class _NodeIfConfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,99)));namedValues=NamedValues(*(('other',1),('inService',2),('outOfService',3),(_G,4),('localLoopBack',5),('remoteLoopBack',6),(_F,99)))
_NodeIfConfStatus_Type.__name__=_B
_NodeIfConfStatus_Object=MibTableColumn
nodeIfConfStatus=_NodeIfConfStatus_Object((1,3,6,1,4,1,119,2,3,14,3,1,2,1,4),_NodeIfConfStatus_Type())
nodeIfConfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeIfConfStatus.setStatus(_A)
class _NodeFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_NodeFanStatus_Type.__name__=_B
_NodeFanStatus_Object=MibScalar
nodeFanStatus=_NodeFanStatus_Object((1,3,6,1,4,1,119,2,3,14,3,1,3),_NodeFanStatus_Type())
nodeFanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeFanStatus.setStatus(_A)
class _NodeUpcWindowSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_NodeUpcWindowSize_Type.__name__=_B
_NodeUpcWindowSize_Object=MibScalar
nodeUpcWindowSize=_NodeUpcWindowSize_Object((1,3,6,1,4,1,119,2,3,14,3,1,4),_NodeUpcWindowSize_Type())
nodeUpcWindowSize.setMaxAccess(_D)
if mibBuilder.loadTexts:nodeUpcWindowSize.setStatus(_A)
class _NodeBestEffortBufferSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_NodeBestEffortBufferSize_Type.__name__=_B
_NodeBestEffortBufferSize_Object=MibScalar
nodeBestEffortBufferSize=_NodeBestEffortBufferSize_Object((1,3,6,1,4,1,119,2,3,14,3,1,5),_NodeBestEffortBufferSize_Type())
nodeBestEffortBufferSize.setMaxAccess(_D)
if mibBuilder.loadTexts:nodeBestEffortBufferSize.setStatus(_A)
class _NodeGuaranteedBufferSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_NodeGuaranteedBufferSize_Type.__name__=_B
_NodeGuaranteedBufferSize_Object=MibScalar
nodeGuaranteedBufferSize=_NodeGuaranteedBufferSize_Object((1,3,6,1,4,1,119,2,3,14,3,1,6),_NodeGuaranteedBufferSize_Type())
nodeGuaranteedBufferSize.setMaxAccess(_D)
if mibBuilder.loadTexts:nodeGuaranteedBufferSize.setStatus(_A)
class _NodeBestEffortBufferThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_NodeBestEffortBufferThreshold_Type.__name__=_B
_NodeBestEffortBufferThreshold_Object=MibScalar
nodeBestEffortBufferThreshold=_NodeBestEffortBufferThreshold_Object((1,3,6,1,4,1,119,2,3,14,3,1,7),_NodeBestEffortBufferThreshold_Type())
nodeBestEffortBufferThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:nodeBestEffortBufferThreshold.setStatus(_A)
class _NodeGuaranteedBufferThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_NodeGuaranteedBufferThreshold_Type.__name__=_B
_NodeGuaranteedBufferThreshold_Object=MibScalar
nodeGuaranteedBufferThreshold=_NodeGuaranteedBufferThreshold_Object((1,3,6,1,4,1,119,2,3,14,3,1,8),_NodeGuaranteedBufferThreshold_Type())
nodeGuaranteedBufferThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:nodeGuaranteedBufferThreshold.setStatus(_A)
class _NodeSaveConf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('save',1))
_NodeSaveConf_Type.__name__=_B
_NodeSaveConf_Object=MibScalar
nodeSaveConf=_NodeSaveConf_Object((1,3,6,1,4,1,119,2,3,14,3,1,9),_NodeSaveConf_Type())
nodeSaveConf.setMaxAccess('write-only')
if mibBuilder.loadTexts:nodeSaveConf.setStatus(_A)
class _NodeSaveResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('temporaryFailure',1),('notReady',2),('ready',3),('succeed',4),('nearend',5)))
_NodeSaveResult_Type.__name__=_B
_NodeSaveResult_Object=MibScalar
nodeSaveResult=_NodeSaveResult_Object((1,3,6,1,4,1,119,2,3,14,3,1,10),_NodeSaveResult_Type())
nodeSaveResult.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeSaveResult.setStatus(_A)
_Linf_ObjectIdentity=ObjectIdentity
linf=_Linf_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,3,2))
_LinfStatusTable_Object=MibTable
linfStatusTable=_LinfStatusTable_Object((1,3,6,1,4,1,119,2,3,14,3,2,1))
if mibBuilder.loadTexts:linfStatusTable.setStatus(_A)
_LinfStatusEntry_Object=MibTableRow
linfStatusEntry=_LinfStatusEntry_Object((1,3,6,1,4,1,119,2,3,14,3,2,1,1))
linfStatusEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:linfStatusEntry.setStatus(_A)
class _LinfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_LinfIndex_Type.__name__=_B
_LinfIndex_Object=MibTableColumn
linfIndex=_LinfIndex_Object((1,3,6,1,4,1,119,2,3,14,3,2,1,1,1),_LinfIndex_Type())
linfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:linfIndex.setStatus(_A)
class _LinfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,99)));namedValues=NamedValues(*(('normal',1),('los',2),('lof',3),('loc',4),('ais',5),('yellow-line',6),('yellow-path',7),('lop',8),(_F,99)))
_LinfStatus_Type.__name__=_B
_LinfStatus_Object=MibTableColumn
linfStatus=_LinfStatus_Object((1,3,6,1,4,1,119,2,3,14,3,2,1,1,2),_LinfStatus_Type())
linfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:linfStatus.setStatus(_A)
class _LinfConf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,99)));namedValues=NamedValues(*(('public-UNI',1),('private-UNI',2),('private-NNI',3),('others',99)))
_LinfConf_Type.__name__=_B
_LinfConf_Object=MibTableColumn
linfConf=_LinfConf_Object((1,3,6,1,4,1,119,2,3,14,3,2,1,1,3),_LinfConf_Type())
linfConf.setMaxAccess(_D)
if mibBuilder.loadTexts:linfConf.setStatus(_A)
_Conn_ObjectIdentity=ObjectIdentity
conn=_Conn_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,3,3))
_Perf_ObjectIdentity=ObjectIdentity
perf=_Perf_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,3,4))
mibBuilder.exportSymbols(_E,**{'nec':nec,'nec-mib':nec_mib,'necProductDepend':necProductDepend,'atomis-mib':atomis_mib,'m5core-mib':m5core_mib,'node':node,'nodeOperStatus':nodeOperStatus,'nodeIfConfTable':nodeIfConfTable,'nodeIfConfEntry':nodeIfConfEntry,_H:nodeIfConfIndex,'nodeIfConfPhysType':nodeIfConfPhysType,'nodeIfConfRev':nodeIfConfRev,'nodeIfConfStatus':nodeIfConfStatus,'nodeFanStatus':nodeFanStatus,'nodeUpcWindowSize':nodeUpcWindowSize,'nodeBestEffortBufferSize':nodeBestEffortBufferSize,'nodeGuaranteedBufferSize':nodeGuaranteedBufferSize,'nodeBestEffortBufferThreshold':nodeBestEffortBufferThreshold,'nodeGuaranteedBufferThreshold':nodeGuaranteedBufferThreshold,'nodeSaveConf':nodeSaveConf,'nodeSaveResult':nodeSaveResult,'linf':linf,'linfStatusTable':linfStatusTable,'linfStatusEntry':linfStatusEntry,_I:linfIndex,'linfStatus':linfStatus,'linfConf':linfConf,'conn':conn,'perf':perf})