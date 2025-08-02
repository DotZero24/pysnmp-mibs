_a='osSFlowMandatoryGroup'
_Z='osSFlowCpOperStatus'
_Y='osSFlowCpAdminStatus'
_X='osSflowCpSampleCount'
_W='osSflowCpActiveTime'
_V='osSflowCpPorts'
_U='osSflowCpRate'
_T='osSflowCpRcvrIndex'
_S='osSFlowRcvrOperStatus'
_R='osSFlowRcvrAdminStatus'
_Q='osSFlowRcvrPort'
_P='osSFlowRcvrAddress'
_O='osSFlowRcvrOwner'
_N='osSFlowSamplesDroppedByRateLimit'
_M='osSFlowSamplesRateLimit'
_L='osSFlowDefaultTruncateSize'
_K='osSFlowAgentAddress'
_J='osSFlowCpName'
_I='not-accessible'
_H='osSFlowRcvrIndex'
_G='Seconds'
_F='read-only'
_E='OctetString'
_D='Integer32'
_C='read-write'
_B='OS-SFLOW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EntryValidator,PortList,oaOptiSwitch=mibBuilder.importSymbols('OS-COMMON-TC-MIB','EntryValidator','PortList','oaOptiSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
osSFlow=ModuleIdentity((1,3,6,1,4,1,6926,2,25))
if mibBuilder.loadTexts:osSFlow.setRevisions(('2013-05-08 00:00',))
class OsRcvrOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('notReady',2),('ready',3)))
_OsSFlowAgent_ObjectIdentity=ObjectIdentity
osSFlowAgent=_OsSFlowAgent_ObjectIdentity((1,3,6,1,4,1,6926,2,25,1))
class _OsSFlowAgentAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_OsSFlowAgentAddress_Type.__name__=_E
_OsSFlowAgentAddress_Object=MibScalar
osSFlowAgentAddress=_OsSFlowAgentAddress_Object((1,3,6,1,4,1,6926,2,25,1,1),_OsSFlowAgentAddress_Type())
osSFlowAgentAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:osSFlowAgentAddress.setStatus(_A)
class _OsSFlowDefaultTruncateSize_Type(Integer32):defaultValue=65536;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(128,65536))
_OsSFlowDefaultTruncateSize_Type.__name__=_D
_OsSFlowDefaultTruncateSize_Object=MibScalar
osSFlowDefaultTruncateSize=_OsSFlowDefaultTruncateSize_Object((1,3,6,1,4,1,6926,2,25,1,2),_OsSFlowDefaultTruncateSize_Type())
osSFlowDefaultTruncateSize.setMaxAccess(_C)
if mibBuilder.loadTexts:osSFlowDefaultTruncateSize.setStatus(_A)
class _OsSFlowSamplesRateLimit_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,200))
_OsSFlowSamplesRateLimit_Type.__name__=_D
_OsSFlowSamplesRateLimit_Object=MibScalar
osSFlowSamplesRateLimit=_OsSFlowSamplesRateLimit_Object((1,3,6,1,4,1,6926,2,25,1,3),_OsSFlowSamplesRateLimit_Type())
osSFlowSamplesRateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:osSFlowSamplesRateLimit.setStatus(_A)
if mibBuilder.loadTexts:osSFlowSamplesRateLimit.setUnits('Samples per Second')
_OsSFlowSamplesDroppedByRateLimit_Type=Integer32
_OsSFlowSamplesDroppedByRateLimit_Object=MibScalar
osSFlowSamplesDroppedByRateLimit=_OsSFlowSamplesDroppedByRateLimit_Object((1,3,6,1,4,1,6926,2,25,1,4),_OsSFlowSamplesDroppedByRateLimit_Type())
osSFlowSamplesDroppedByRateLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:osSFlowSamplesDroppedByRateLimit.setStatus(_A)
_OsSFlowRcvrTable_Object=MibTable
osSFlowRcvrTable=_OsSFlowRcvrTable_Object((1,3,6,1,4,1,6926,2,25,2))
if mibBuilder.loadTexts:osSFlowRcvrTable.setStatus(_A)
_OsSFlowRcvrEntry_Object=MibTableRow
osSFlowRcvrEntry=_OsSFlowRcvrEntry_Object((1,3,6,1,4,1,6926,2,25,2,1))
osSFlowRcvrEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:osSFlowRcvrEntry.setStatus(_A)
class _OsSFlowRcvrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9999))
_OsSFlowRcvrIndex_Type.__name__=_D
_OsSFlowRcvrIndex_Object=MibTableColumn
osSFlowRcvrIndex=_OsSFlowRcvrIndex_Object((1,3,6,1,4,1,6926,2,25,2,1,1),_OsSFlowRcvrIndex_Type())
osSFlowRcvrIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:osSFlowRcvrIndex.setStatus(_A)
class _OsSFlowRcvrOwner_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_OsSFlowRcvrOwner_Type.__name__=_E
_OsSFlowRcvrOwner_Object=MibTableColumn
osSFlowRcvrOwner=_OsSFlowRcvrOwner_Object((1,3,6,1,4,1,6926,2,25,2,1,2),_OsSFlowRcvrOwner_Type())
osSFlowRcvrOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:osSFlowRcvrOwner.setStatus(_A)
class _OsSFlowRcvrAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_OsSFlowRcvrAddress_Type.__name__=_E
_OsSFlowRcvrAddress_Object=MibTableColumn
osSFlowRcvrAddress=_OsSFlowRcvrAddress_Object((1,3,6,1,4,1,6926,2,25,2,1,6),_OsSFlowRcvrAddress_Type())
osSFlowRcvrAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:osSFlowRcvrAddress.setStatus(_A)
class _OsSFlowRcvrPort_Type(Integer32):defaultValue=6343
_OsSFlowRcvrPort_Type.__name__=_D
_OsSFlowRcvrPort_Object=MibTableColumn
osSFlowRcvrPort=_OsSFlowRcvrPort_Object((1,3,6,1,4,1,6926,2,25,2,1,7),_OsSFlowRcvrPort_Type())
osSFlowRcvrPort.setMaxAccess(_C)
if mibBuilder.loadTexts:osSFlowRcvrPort.setStatus(_A)
_OsSFlowRcvrAdminStatus_Type=EntryValidator
_OsSFlowRcvrAdminStatus_Object=MibTableColumn
osSFlowRcvrAdminStatus=_OsSFlowRcvrAdminStatus_Object((1,3,6,1,4,1,6926,2,25,2,1,98),_OsSFlowRcvrAdminStatus_Type())
osSFlowRcvrAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:osSFlowRcvrAdminStatus.setStatus(_A)
_OsSFlowRcvrOperStatus_Type=OsRcvrOperStatus
_OsSFlowRcvrOperStatus_Object=MibTableColumn
osSFlowRcvrOperStatus=_OsSFlowRcvrOperStatus_Object((1,3,6,1,4,1,6926,2,25,2,1,99),_OsSFlowRcvrOperStatus_Type())
osSFlowRcvrOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:osSFlowRcvrOperStatus.setStatus(_A)
_OsSFlowCpTable_Object=MibTable
osSFlowCpTable=_OsSFlowCpTable_Object((1,3,6,1,4,1,6926,2,25,3))
if mibBuilder.loadTexts:osSFlowCpTable.setStatus(_A)
_OsSFlowCpEntry_Object=MibTableRow
osSFlowCpEntry=_OsSFlowCpEntry_Object((1,3,6,1,4,1,6926,2,25,3,1))
osSFlowCpEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:osSFlowCpEntry.setStatus(_A)
class _OsSFlowCpName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_OsSFlowCpName_Type.__name__=_E
_OsSFlowCpName_Object=MibTableColumn
osSFlowCpName=_OsSFlowCpName_Object((1,3,6,1,4,1,6926,2,25,3,1,1),_OsSFlowCpName_Type())
osSFlowCpName.setMaxAccess(_I)
if mibBuilder.loadTexts:osSFlowCpName.setStatus(_A)
class _OsSflowCpRcvrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,9999))
_OsSflowCpRcvrIndex_Type.__name__=_D
_OsSflowCpRcvrIndex_Object=MibTableColumn
osSflowCpRcvrIndex=_OsSflowCpRcvrIndex_Object((1,3,6,1,4,1,6926,2,25,3,1,2),_OsSflowCpRcvrIndex_Type())
osSflowCpRcvrIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:osSflowCpRcvrIndex.setStatus(_A)
class _OsSflowCpRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,3600))
_OsSflowCpRate_Type.__name__=_D
_OsSflowCpRate_Object=MibTableColumn
osSflowCpRate=_OsSflowCpRate_Object((1,3,6,1,4,1,6926,2,25,3,1,3),_OsSflowCpRate_Type())
osSflowCpRate.setMaxAccess(_C)
if mibBuilder.loadTexts:osSflowCpRate.setStatus(_A)
if mibBuilder.loadTexts:osSflowCpRate.setUnits(_G)
_OsSflowCpPorts_Type=PortList
_OsSflowCpPorts_Object=MibTableColumn
osSflowCpPorts=_OsSflowCpPorts_Object((1,3,6,1,4,1,6926,2,25,3,1,4),_OsSflowCpPorts_Type())
osSflowCpPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:osSflowCpPorts.setStatus(_A)
_OsSflowCpActiveTime_Type=Unsigned32
_OsSflowCpActiveTime_Object=MibTableColumn
osSflowCpActiveTime=_OsSflowCpActiveTime_Object((1,3,6,1,4,1,6926,2,25,3,1,5),_OsSflowCpActiveTime_Type())
osSflowCpActiveTime.setMaxAccess(_F)
if mibBuilder.loadTexts:osSflowCpActiveTime.setStatus(_A)
if mibBuilder.loadTexts:osSflowCpActiveTime.setUnits(_G)
_OsSflowCpSampleCount_Type=Counter64
_OsSflowCpSampleCount_Object=MibTableColumn
osSflowCpSampleCount=_OsSflowCpSampleCount_Object((1,3,6,1,4,1,6926,2,25,3,1,6),_OsSflowCpSampleCount_Type())
osSflowCpSampleCount.setMaxAccess(_F)
if mibBuilder.loadTexts:osSflowCpSampleCount.setStatus(_A)
if mibBuilder.loadTexts:osSflowCpSampleCount.setUnits(_G)
_OsSFlowCpAdminStatus_Type=EntryValidator
_OsSFlowCpAdminStatus_Object=MibTableColumn
osSFlowCpAdminStatus=_OsSFlowCpAdminStatus_Object((1,3,6,1,4,1,6926,2,25,3,1,98),_OsSFlowCpAdminStatus_Type())
osSFlowCpAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:osSFlowCpAdminStatus.setStatus(_A)
class _OsSFlowCpOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notActive',1),('active',2)))
_OsSFlowCpOperStatus_Type.__name__=_D
_OsSFlowCpOperStatus_Object=MibTableColumn
osSFlowCpOperStatus=_OsSFlowCpOperStatus_Object((1,3,6,1,4,1,6926,2,25,3,1,99),_OsSFlowCpOperStatus_Type())
osSFlowCpOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:osSFlowCpOperStatus.setStatus(_A)
_OsSFlowConformance_ObjectIdentity=ObjectIdentity
osSFlowConformance=_OsSFlowConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,25,100))
_OsSFlowMIBCompliances_ObjectIdentity=ObjectIdentity
osSFlowMIBCompliances=_OsSFlowMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,25,100,1))
_OsSFlowMIBGroups_ObjectIdentity=ObjectIdentity
osSFlowMIBGroups=_OsSFlowMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,25,100,2))
osSFlowMandatoryGroup=ObjectGroup((1,3,6,1,4,1,6926,2,25,100,2,1))
osSFlowMandatoryGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:osSFlowMandatoryGroup.setStatus(_A)
osSFlowMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,25,100,1,1))
osSFlowMIBCompliance.setObjects((_B,_a))
if mibBuilder.loadTexts:osSFlowMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'OsRcvrOperStatus':OsRcvrOperStatus,'osSFlow':osSFlow,'osSFlowAgent':osSFlowAgent,_K:osSFlowAgentAddress,_L:osSFlowDefaultTruncateSize,_M:osSFlowSamplesRateLimit,_N:osSFlowSamplesDroppedByRateLimit,'osSFlowRcvrTable':osSFlowRcvrTable,'osSFlowRcvrEntry':osSFlowRcvrEntry,_H:osSFlowRcvrIndex,_O:osSFlowRcvrOwner,_P:osSFlowRcvrAddress,_Q:osSFlowRcvrPort,_R:osSFlowRcvrAdminStatus,_S:osSFlowRcvrOperStatus,'osSFlowCpTable':osSFlowCpTable,'osSFlowCpEntry':osSFlowCpEntry,_J:osSFlowCpName,_T:osSflowCpRcvrIndex,_U:osSflowCpRate,_V:osSflowCpPorts,_W:osSflowCpActiveTime,_X:osSflowCpSampleCount,_Y:osSFlowCpAdminStatus,_Z:osSFlowCpOperStatus,'osSFlowConformance':osSFlowConformance,'osSFlowMIBCompliances':osSFlowMIBCompliances,'osSFlowMIBCompliance':osSFlowMIBCompliance,'osSFlowMIBGroups':osSFlowMIBGroups,_a:osSFlowMandatoryGroup})