_R='osTmOptGroup'
_Q='osTmMandatoryGroup'
_P='osTmCountBytesDropped'
_O='osTmCountBytesPassed'
_N='osTmCountPacketsDropped'
_M='osTmCountPacketsPassed'
_L='osTmCountClear'
_K='osTmSupport'
_J='osTmCountSlQueue'
_I='osTmCountCNode'
_H='osTmCountBNode'
_G='osTmCountServNode'
_F='osTmCountPort'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='OS-TM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oaOptiSwitch,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','oaOptiSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
osTm=ModuleIdentity((1,3,6,1,4,1,6926,2,38))
if mibBuilder.loadTexts:osTm.setRevisions(('2016-11-06 00:00',))
class TmPortIndex(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class TmNodeId(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class TmSlQueueId(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_OsTmCapabilities_ObjectIdentity=ObjectIdentity
osTmCapabilities=_OsTmCapabilities_ObjectIdentity((1,3,6,1,4,1,6926,2,38,1))
class _OsTmSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
_OsTmSupport_Type.__name__=_E
_OsTmSupport_Object=MibScalar
osTmSupport=_OsTmSupport_Object((1,3,6,1,4,1,6926,2,38,1,1),_OsTmSupport_Type())
osTmSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:osTmSupport.setStatus(_A)
_OsTmCountTable_Object=MibTable
osTmCountTable=_OsTmCountTable_Object((1,3,6,1,4,1,6926,2,38,20))
if mibBuilder.loadTexts:osTmCountTable.setStatus(_A)
_OsTmCountEntry_Object=MibTableRow
osTmCountEntry=_OsTmCountEntry_Object((1,3,6,1,4,1,6926,2,38,20,1))
osTmCountEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:osTmCountEntry.setStatus(_A)
_OsTmCountPort_Type=TmPortIndex
_OsTmCountPort_Object=MibTableColumn
osTmCountPort=_OsTmCountPort_Object((1,3,6,1,4,1,6926,2,38,20,1,1),_OsTmCountPort_Type())
osTmCountPort.setMaxAccess(_D)
if mibBuilder.loadTexts:osTmCountPort.setStatus(_A)
_OsTmCountServNode_Type=TmNodeId
_OsTmCountServNode_Object=MibTableColumn
osTmCountServNode=_OsTmCountServNode_Object((1,3,6,1,4,1,6926,2,38,20,1,2),_OsTmCountServNode_Type())
osTmCountServNode.setMaxAccess(_D)
if mibBuilder.loadTexts:osTmCountServNode.setStatus(_A)
_OsTmCountBNode_Type=TmNodeId
_OsTmCountBNode_Object=MibTableColumn
osTmCountBNode=_OsTmCountBNode_Object((1,3,6,1,4,1,6926,2,38,20,1,3),_OsTmCountBNode_Type())
osTmCountBNode.setMaxAccess(_D)
if mibBuilder.loadTexts:osTmCountBNode.setStatus(_A)
_OsTmCountCNode_Type=TmNodeId
_OsTmCountCNode_Object=MibTableColumn
osTmCountCNode=_OsTmCountCNode_Object((1,3,6,1,4,1,6926,2,38,20,1,4),_OsTmCountCNode_Type())
osTmCountCNode.setMaxAccess(_D)
if mibBuilder.loadTexts:osTmCountCNode.setStatus(_A)
_OsTmCountSlQueue_Type=TmSlQueueId
_OsTmCountSlQueue_Object=MibTableColumn
osTmCountSlQueue=_OsTmCountSlQueue_Object((1,3,6,1,4,1,6926,2,38,20,1,5),_OsTmCountSlQueue_Type())
osTmCountSlQueue.setMaxAccess(_D)
if mibBuilder.loadTexts:osTmCountSlQueue.setStatus(_A)
_OsTmCountClear_Type=TruthValue
_OsTmCountClear_Object=MibTableColumn
osTmCountClear=_OsTmCountClear_Object((1,3,6,1,4,1,6926,2,38,20,1,6),_OsTmCountClear_Type())
osTmCountClear.setMaxAccess('read-write')
if mibBuilder.loadTexts:osTmCountClear.setStatus(_A)
_OsTmCountPacketsPassed_Type=Counter64
_OsTmCountPacketsPassed_Object=MibTableColumn
osTmCountPacketsPassed=_OsTmCountPacketsPassed_Object((1,3,6,1,4,1,6926,2,38,20,1,8),_OsTmCountPacketsPassed_Type())
osTmCountPacketsPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:osTmCountPacketsPassed.setStatus(_A)
_OsTmCountPacketsDropped_Type=Counter64
_OsTmCountPacketsDropped_Object=MibTableColumn
osTmCountPacketsDropped=_OsTmCountPacketsDropped_Object((1,3,6,1,4,1,6926,2,38,20,1,9),_OsTmCountPacketsDropped_Type())
osTmCountPacketsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:osTmCountPacketsDropped.setStatus(_A)
_OsTmCountBytesPassed_Type=Counter64
_OsTmCountBytesPassed_Object=MibTableColumn
osTmCountBytesPassed=_OsTmCountBytesPassed_Object((1,3,6,1,4,1,6926,2,38,20,1,10),_OsTmCountBytesPassed_Type())
osTmCountBytesPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:osTmCountBytesPassed.setStatus(_A)
_OsTmCountBytesDropped_Type=Counter64
_OsTmCountBytesDropped_Object=MibTableColumn
osTmCountBytesDropped=_OsTmCountBytesDropped_Object((1,3,6,1,4,1,6926,2,38,20,1,11),_OsTmCountBytesDropped_Type())
osTmCountBytesDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:osTmCountBytesDropped.setStatus(_A)
_OsTmConformance_ObjectIdentity=ObjectIdentity
osTmConformance=_OsTmConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,38,100))
_OsTmMIBCompliances_ObjectIdentity=ObjectIdentity
osTmMIBCompliances=_OsTmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,38,100,1))
_OsTmMIBGroups_ObjectIdentity=ObjectIdentity
osTmMIBGroups=_OsTmMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,38,100,2))
osTmMandatoryGroup=ObjectGroup((1,3,6,1,4,1,6926,2,38,100,2,1))
osTmMandatoryGroup.setObjects((_B,_K))
if mibBuilder.loadTexts:osTmMandatoryGroup.setStatus(_A)
osTmOptGroup=ObjectGroup((1,3,6,1,4,1,6926,2,38,100,2,2))
osTmOptGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:osTmOptGroup.setStatus(_A)
osTmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,38,100,1,1))
osTmMIBCompliance.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:osTmMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TmPortIndex':TmPortIndex,'TmNodeId':TmNodeId,'TmSlQueueId':TmSlQueueId,'osTm':osTm,'osTmCapabilities':osTmCapabilities,_K:osTmSupport,'osTmCountTable':osTmCountTable,'osTmCountEntry':osTmCountEntry,_F:osTmCountPort,_G:osTmCountServNode,_H:osTmCountBNode,_I:osTmCountCNode,_J:osTmCountSlQueue,_L:osTmCountClear,_M:osTmCountPacketsPassed,_N:osTmCountPacketsDropped,_O:osTmCountBytesPassed,_P:osTmCountBytesDropped,'osTmConformance':osTmConformance,'osTmMIBCompliances':osTmMIBCompliances,'osTmMIBCompliance':osTmMIBCompliance,'osTmMIBGroups':osTmMIBGroups,_Q:osTmMandatoryGroup,_R:osTmOptGroup})