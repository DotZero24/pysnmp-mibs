_f='sFlowAgentGroup'
_e='sFlowCpInterval'
_d='sFlowCpReceiver'
_c='sFlowFsMaximumHeaderSize'
_b='sFlowFsPacketSamplingRate'
_a='sFlowFsReceiver'
_Z='sFlowRcvrDatagramVersion'
_Y='sFlowRcvrPort'
_X='sFlowRcvrAddress'
_W='sFlowRcvrAddressType'
_V='sFlowRcvrMaximumDatagramSize'
_U='sFlowRcvrTimeout'
_T='sFlowRcvrOwner'
_S='sFlowAgentAddress'
_R='sFlowAgentAddressType'
_Q='sFlowVersion'
_P='sFlowCpInstance'
_O='sFlowCpDataSource'
_N='sFlowFsInstance'
_M='sFlowFsDataSource'
_L='sFlowRcvrIndex'
_K='SnmpAdminString'
_J='OwnerString'
_I='InetAddressType'
_H='InetAddress'
_G='SFlowReceiver'
_F='read-only'
_E='not-accessible'
_D='Integer32'
_C='read-write'
_B='SFLOW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_H,_I)
OwnerString,=mibBuilder.importSymbols('RMON-MIB',_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sFlowMIB=ModuleIdentity((1,3,6,1,4,1,14706,1))
if mibBuilder.loadTexts:sFlowMIB.setRevisions(('2003-10-18 00:00','2003-09-24 00:00','2003-04-08 00:00','2002-09-17 00:00','2001-07-31 00:00','2001-05-01 00:00'))
class SFlowDataSource(TextualConvention,ObjectIdentifier):status=_A
class SFlowInstance(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class SFlowReceiver(TextualConvention,Integer32):status=_A
_SFlowAgent_ObjectIdentity=ObjectIdentity
sFlowAgent=_SFlowAgent_ObjectIdentity((1,3,6,1,4,1,14706,1,1))
class _SFlowVersion_Type(SnmpAdminString):defaultValue=OctetString('1.3;;')
_SFlowVersion_Type.__name__=_K
_SFlowVersion_Object=MibScalar
sFlowVersion=_SFlowVersion_Object((1,3,6,1,4,1,14706,1,1,1),_SFlowVersion_Type())
sFlowVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:sFlowVersion.setStatus(_A)
_SFlowAgentAddressType_Type=InetAddressType
_SFlowAgentAddressType_Object=MibScalar
sFlowAgentAddressType=_SFlowAgentAddressType_Object((1,3,6,1,4,1,14706,1,1,2),_SFlowAgentAddressType_Type())
sFlowAgentAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:sFlowAgentAddressType.setStatus(_A)
_SFlowAgentAddress_Type=InetAddress
_SFlowAgentAddress_Object=MibScalar
sFlowAgentAddress=_SFlowAgentAddress_Object((1,3,6,1,4,1,14706,1,1,3),_SFlowAgentAddress_Type())
sFlowAgentAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:sFlowAgentAddress.setStatus(_A)
_SFlowRcvrTable_Object=MibTable
sFlowRcvrTable=_SFlowRcvrTable_Object((1,3,6,1,4,1,14706,1,1,4))
if mibBuilder.loadTexts:sFlowRcvrTable.setStatus(_A)
_SFlowRcvrEntry_Object=MibTableRow
sFlowRcvrEntry=_SFlowRcvrEntry_Object((1,3,6,1,4,1,14706,1,1,4,1))
sFlowRcvrEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:sFlowRcvrEntry.setStatus(_A)
class _SFlowRcvrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SFlowRcvrIndex_Type.__name__=_D
_SFlowRcvrIndex_Object=MibTableColumn
sFlowRcvrIndex=_SFlowRcvrIndex_Object((1,3,6,1,4,1,14706,1,1,4,1,1),_SFlowRcvrIndex_Type())
sFlowRcvrIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:sFlowRcvrIndex.setStatus(_A)
class _SFlowRcvrOwner_Type(OwnerString):defaultValue=OctetString('')
_SFlowRcvrOwner_Type.__name__=_J
_SFlowRcvrOwner_Object=MibTableColumn
sFlowRcvrOwner=_SFlowRcvrOwner_Object((1,3,6,1,4,1,14706,1,1,4,1,2),_SFlowRcvrOwner_Type())
sFlowRcvrOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:sFlowRcvrOwner.setStatus(_A)
class _SFlowRcvrTimeout_Type(Integer32):defaultValue=0
_SFlowRcvrTimeout_Type.__name__=_D
_SFlowRcvrTimeout_Object=MibTableColumn
sFlowRcvrTimeout=_SFlowRcvrTimeout_Object((1,3,6,1,4,1,14706,1,1,4,1,3),_SFlowRcvrTimeout_Type())
sFlowRcvrTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:sFlowRcvrTimeout.setStatus(_A)
class _SFlowRcvrMaximumDatagramSize_Type(Integer32):defaultValue=1400
_SFlowRcvrMaximumDatagramSize_Type.__name__=_D
_SFlowRcvrMaximumDatagramSize_Object=MibTableColumn
sFlowRcvrMaximumDatagramSize=_SFlowRcvrMaximumDatagramSize_Object((1,3,6,1,4,1,14706,1,1,4,1,4),_SFlowRcvrMaximumDatagramSize_Type())
sFlowRcvrMaximumDatagramSize.setMaxAccess(_C)
if mibBuilder.loadTexts:sFlowRcvrMaximumDatagramSize.setStatus(_A)
class _SFlowRcvrAddressType_Type(InetAddressType):defaultValue=1
_SFlowRcvrAddressType_Type.__name__=_I
_SFlowRcvrAddressType_Object=MibTableColumn
sFlowRcvrAddressType=_SFlowRcvrAddressType_Object((1,3,6,1,4,1,14706,1,1,4,1,5),_SFlowRcvrAddressType_Type())
sFlowRcvrAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:sFlowRcvrAddressType.setStatus(_A)
class _SFlowRcvrAddress_Type(InetAddress):defaultHexValue='00000000'
_SFlowRcvrAddress_Type.__name__=_H
_SFlowRcvrAddress_Object=MibTableColumn
sFlowRcvrAddress=_SFlowRcvrAddress_Object((1,3,6,1,4,1,14706,1,1,4,1,6),_SFlowRcvrAddress_Type())
sFlowRcvrAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sFlowRcvrAddress.setStatus(_A)
class _SFlowRcvrPort_Type(Integer32):defaultValue=6343
_SFlowRcvrPort_Type.__name__=_D
_SFlowRcvrPort_Object=MibTableColumn
sFlowRcvrPort=_SFlowRcvrPort_Object((1,3,6,1,4,1,14706,1,1,4,1,7),_SFlowRcvrPort_Type())
sFlowRcvrPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sFlowRcvrPort.setStatus(_A)
class _SFlowRcvrDatagramVersion_Type(Integer32):defaultValue=5
_SFlowRcvrDatagramVersion_Type.__name__=_D
_SFlowRcvrDatagramVersion_Object=MibTableColumn
sFlowRcvrDatagramVersion=_SFlowRcvrDatagramVersion_Object((1,3,6,1,4,1,14706,1,1,4,1,8),_SFlowRcvrDatagramVersion_Type())
sFlowRcvrDatagramVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:sFlowRcvrDatagramVersion.setStatus(_A)
_SFlowFsTable_Object=MibTable
sFlowFsTable=_SFlowFsTable_Object((1,3,6,1,4,1,14706,1,1,5))
if mibBuilder.loadTexts:sFlowFsTable.setStatus(_A)
_SFlowFsEntry_Object=MibTableRow
sFlowFsEntry=_SFlowFsEntry_Object((1,3,6,1,4,1,14706,1,1,5,1))
sFlowFsEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:sFlowFsEntry.setStatus(_A)
_SFlowFsDataSource_Type=SFlowDataSource
_SFlowFsDataSource_Object=MibTableColumn
sFlowFsDataSource=_SFlowFsDataSource_Object((1,3,6,1,4,1,14706,1,1,5,1,1),_SFlowFsDataSource_Type())
sFlowFsDataSource.setMaxAccess(_E)
if mibBuilder.loadTexts:sFlowFsDataSource.setStatus(_A)
_SFlowFsInstance_Type=SFlowInstance
_SFlowFsInstance_Object=MibTableColumn
sFlowFsInstance=_SFlowFsInstance_Object((1,3,6,1,4,1,14706,1,1,5,1,2),_SFlowFsInstance_Type())
sFlowFsInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:sFlowFsInstance.setStatus(_A)
class _SFlowFsReceiver_Type(SFlowReceiver):defaultValue=0
_SFlowFsReceiver_Type.__name__=_G
_SFlowFsReceiver_Object=MibTableColumn
sFlowFsReceiver=_SFlowFsReceiver_Object((1,3,6,1,4,1,14706,1,1,5,1,3),_SFlowFsReceiver_Type())
sFlowFsReceiver.setMaxAccess(_C)
if mibBuilder.loadTexts:sFlowFsReceiver.setStatus(_A)
class _SFlowFsPacketSamplingRate_Type(Integer32):defaultValue=0
_SFlowFsPacketSamplingRate_Type.__name__=_D
_SFlowFsPacketSamplingRate_Object=MibTableColumn
sFlowFsPacketSamplingRate=_SFlowFsPacketSamplingRate_Object((1,3,6,1,4,1,14706,1,1,5,1,4),_SFlowFsPacketSamplingRate_Type())
sFlowFsPacketSamplingRate.setMaxAccess(_C)
if mibBuilder.loadTexts:sFlowFsPacketSamplingRate.setStatus(_A)
class _SFlowFsMaximumHeaderSize_Type(Integer32):defaultValue=128
_SFlowFsMaximumHeaderSize_Type.__name__=_D
_SFlowFsMaximumHeaderSize_Object=MibTableColumn
sFlowFsMaximumHeaderSize=_SFlowFsMaximumHeaderSize_Object((1,3,6,1,4,1,14706,1,1,5,1,5),_SFlowFsMaximumHeaderSize_Type())
sFlowFsMaximumHeaderSize.setMaxAccess(_C)
if mibBuilder.loadTexts:sFlowFsMaximumHeaderSize.setStatus(_A)
_SFlowCpTable_Object=MibTable
sFlowCpTable=_SFlowCpTable_Object((1,3,6,1,4,1,14706,1,1,6))
if mibBuilder.loadTexts:sFlowCpTable.setStatus(_A)
_SFlowCpEntry_Object=MibTableRow
sFlowCpEntry=_SFlowCpEntry_Object((1,3,6,1,4,1,14706,1,1,6,1))
sFlowCpEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:sFlowCpEntry.setStatus(_A)
_SFlowCpDataSource_Type=SFlowDataSource
_SFlowCpDataSource_Object=MibTableColumn
sFlowCpDataSource=_SFlowCpDataSource_Object((1,3,6,1,4,1,14706,1,1,6,1,1),_SFlowCpDataSource_Type())
sFlowCpDataSource.setMaxAccess(_E)
if mibBuilder.loadTexts:sFlowCpDataSource.setStatus(_A)
_SFlowCpInstance_Type=SFlowInstance
_SFlowCpInstance_Object=MibTableColumn
sFlowCpInstance=_SFlowCpInstance_Object((1,3,6,1,4,1,14706,1,1,6,1,2),_SFlowCpInstance_Type())
sFlowCpInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:sFlowCpInstance.setStatus(_A)
class _SFlowCpReceiver_Type(SFlowReceiver):defaultValue=0
_SFlowCpReceiver_Type.__name__=_G
_SFlowCpReceiver_Object=MibTableColumn
sFlowCpReceiver=_SFlowCpReceiver_Object((1,3,6,1,4,1,14706,1,1,6,1,3),_SFlowCpReceiver_Type())
sFlowCpReceiver.setMaxAccess(_C)
if mibBuilder.loadTexts:sFlowCpReceiver.setStatus(_A)
class _SFlowCpInterval_Type(Integer32):defaultValue=0
_SFlowCpInterval_Type.__name__=_D
_SFlowCpInterval_Object=MibTableColumn
sFlowCpInterval=_SFlowCpInterval_Object((1,3,6,1,4,1,14706,1,1,6,1,4),_SFlowCpInterval_Type())
sFlowCpInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:sFlowCpInterval.setStatus(_A)
_SFlowMIBConformance_ObjectIdentity=ObjectIdentity
sFlowMIBConformance=_SFlowMIBConformance_ObjectIdentity((1,3,6,1,4,1,14706,1,2))
_SFlowMIBGroups_ObjectIdentity=ObjectIdentity
sFlowMIBGroups=_SFlowMIBGroups_ObjectIdentity((1,3,6,1,4,1,14706,1,2,1))
_SFlowMIBCompliances_ObjectIdentity=ObjectIdentity
sFlowMIBCompliances=_SFlowMIBCompliances_ObjectIdentity((1,3,6,1,4,1,14706,1,2,2))
sFlowAgentGroup=ObjectGroup((1,3,6,1,4,1,14706,1,2,1,1))
sFlowAgentGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:sFlowAgentGroup.setStatus(_A)
sFlowCompliance=ModuleCompliance((1,3,6,1,4,1,14706,1,2,2,1))
sFlowCompliance.setObjects((_B,_f))
if mibBuilder.loadTexts:sFlowCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SFlowDataSource':SFlowDataSource,'SFlowInstance':SFlowInstance,_G:SFlowReceiver,'sFlowMIB':sFlowMIB,'sFlowAgent':sFlowAgent,_Q:sFlowVersion,_R:sFlowAgentAddressType,_S:sFlowAgentAddress,'sFlowRcvrTable':sFlowRcvrTable,'sFlowRcvrEntry':sFlowRcvrEntry,_L:sFlowRcvrIndex,_T:sFlowRcvrOwner,_U:sFlowRcvrTimeout,_V:sFlowRcvrMaximumDatagramSize,_W:sFlowRcvrAddressType,_X:sFlowRcvrAddress,_Y:sFlowRcvrPort,_Z:sFlowRcvrDatagramVersion,'sFlowFsTable':sFlowFsTable,'sFlowFsEntry':sFlowFsEntry,_M:sFlowFsDataSource,_N:sFlowFsInstance,_a:sFlowFsReceiver,_b:sFlowFsPacketSamplingRate,_c:sFlowFsMaximumHeaderSize,'sFlowCpTable':sFlowCpTable,'sFlowCpEntry':sFlowCpEntry,_O:sFlowCpDataSource,_P:sFlowCpInstance,_d:sFlowCpReceiver,_e:sFlowCpInterval,'sFlowMIBConformance':sFlowMIBConformance,'sFlowMIBGroups':sFlowMIBGroups,_f:sFlowAgentGroup,'sFlowMIBCompliances':sFlowMIBCompliances,'sFlowCompliance':sFlowCompliance})