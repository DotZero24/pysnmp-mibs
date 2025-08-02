_AN='ipfixExporterStatsGroup'
_AM='ipfixExporterGroup'
_AL='ipfixSelectionProcessStatsDiscontinuityTime'
_AK='ipfixSelectionProcessStatsPacketsDropped'
_AJ='ipfixSelectionProcessStatsPacketsObserved'
_AI='ipfixMeteringProcessCacheDiscontinuityTime'
_AH='ipfixMeteringProcessCacheDataRecords'
_AG='ipfixMeteringProcessCacheUnusedCacheEntries'
_AF='ipfixMeteringProcessCacheActiveFlows'
_AE='ipfixSelectionProcessSelectorFunction'
_AD='ipfixObservationPointPhysicalEntityDirection'
_AC='ipfixObservationPointPhysicalInterface'
_AB='ipfixObservationPointPhysicalEntity'
_AA='ipfixObservationPointObservationDomainId'
_A9='ipfixMeteringProcessCacheIdleTimeout'
_A8='ipfixMeteringProcessCacheActiveTimeout'
_A7='ipfixMeteringProcessObservationPointGroupRef'
_A6='ipfixExportMemberType'
_A5='ipfixTemplateDiscontinuityTime'
_A4='ipfixTemplateDataRecords'
_A3='ipfixTransportSessionDiscontinuityTime'
_A2='ipfixTransportSessionOptionsTemplates'
_A1='ipfixTransportSessionTemplates'
_A0='ipfixTransportSessionRecords'
_z='ipfixTransportSessionDiscardedMessages'
_y='ipfixTransportSessionMessages'
_x='ipfixTransportSessionBytes'
_w='ipfixTransportSessionPackets'
_v='ipfixTransportSessionRate'
_u='ipfixTemplateDefinitionFlags'
_t='ipfixTemplateDefinitionEnterpriseNumber'
_s='ipfixTemplateDefinitionIeLength'
_r='ipfixTemplateDefinitionIeId'
_q='ipfixTemplateAccessTime'
_p='ipfixTemplateSetId'
_o='ipfixTransportSessionStatus'
_n='ipfixTransportSessionIpfixVersion'
_m='ipfixTransportSessionOptionsTemplateRefreshPacket'
_l='ipfixTransportSessionTemplateRefreshPacket'
_k='ipfixTransportSessionOptionsTemplateRefreshTimeout'
_j='ipfixTransportSessionTemplateRefreshTimeout'
_i='ipfixTransportSessionDeviceMode'
_h='ipfixTransportSessionSctpAssocId'
_g='ipfixTransportSessionDestinationPort'
_f='ipfixTransportSessionSourcePort'
_e='ipfixTransportSessionDestinationAddress'
_d='ipfixTransportSessionDestinationAddressType'
_c='ipfixTransportSessionSourceAddress'
_b='ipfixTransportSessionSourceAddressType'
_a='ipfixTransportSessionProtocol'
_Z='ipfixSelectionProcessStatsEntry'
_Y='ipfixMeteringProcessStatsEntry'
_X='ipfixTemplateStatsEntry'
_W='ipfixTransportSessionStatsEntry'
_V='ipfixSelectionProcessSelectorIndex'
_U='ipfixSelectionProcessIndex'
_T='ipfixObservationPointIndex'
_S='ipfixObservationPointGroupId'
_R='ipfixExportIndex'
_Q='ipfixTemplateDefinitionIndex'
_P='ipfixCommonStatsGroup'
_O='ipfixCommonGroup'
_N='ipfixTemplateId'
_M='ipfixTemplateObservationDomainId'
_L='packets'
_K='InetAddressType'
_J='ipfixMeteringProcessCacheId'
_I='seconds'
_H='unknown'
_G='ipfixTransportSessionIndex'
_F='Integer32'
_E='not-accessible'
_D='Unsigned32'
_C='read-only'
_B='IPFIX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalIndexOrZero,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndexOrZero')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_K,'InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso','mib-2')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ipfixMIB=ModuleIdentity((1,3,6,1,2,1,193))
if mibBuilder.loadTexts:ipfixMIB.setRevisions(('2012-06-11 00:00','2010-04-19 00:00'))
_IpfixObjects_ObjectIdentity=ObjectIdentity
ipfixObjects=_IpfixObjects_ObjectIdentity((1,3,6,1,2,1,193,1))
_IpfixMainObjects_ObjectIdentity=ObjectIdentity
ipfixMainObjects=_IpfixMainObjects_ObjectIdentity((1,3,6,1,2,1,193,1,1))
_IpfixTransportSessionTable_Object=MibTable
ipfixTransportSessionTable=_IpfixTransportSessionTable_Object((1,3,6,1,2,1,193,1,1,1))
if mibBuilder.loadTexts:ipfixTransportSessionTable.setStatus(_A)
_IpfixTransportSessionEntry_Object=MibTableRow
ipfixTransportSessionEntry=_IpfixTransportSessionEntry_Object((1,3,6,1,2,1,193,1,1,1,1))
ipfixTransportSessionEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:ipfixTransportSessionEntry.setStatus(_A)
class _IpfixTransportSessionIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_IpfixTransportSessionIndex_Type.__name__=_D
_IpfixTransportSessionIndex_Object=MibTableColumn
ipfixTransportSessionIndex=_IpfixTransportSessionIndex_Object((1,3,6,1,2,1,193,1,1,1,1,1),_IpfixTransportSessionIndex_Type())
ipfixTransportSessionIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ipfixTransportSessionIndex.setStatus(_A)
class _IpfixTransportSessionProtocol_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_IpfixTransportSessionProtocol_Type.__name__=_D
_IpfixTransportSessionProtocol_Object=MibTableColumn
ipfixTransportSessionProtocol=_IpfixTransportSessionProtocol_Object((1,3,6,1,2,1,193,1,1,1,1,2),_IpfixTransportSessionProtocol_Type())
ipfixTransportSessionProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionProtocol.setStatus(_A)
class _IpfixTransportSessionSourceAddressType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('ipv4',1),('ipv6',2)))
_IpfixTransportSessionSourceAddressType_Type.__name__=_K
_IpfixTransportSessionSourceAddressType_Object=MibTableColumn
ipfixTransportSessionSourceAddressType=_IpfixTransportSessionSourceAddressType_Object((1,3,6,1,2,1,193,1,1,1,1,3),_IpfixTransportSessionSourceAddressType_Type())
ipfixTransportSessionSourceAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionSourceAddressType.setStatus(_A)
_IpfixTransportSessionSourceAddress_Type=InetAddress
_IpfixTransportSessionSourceAddress_Object=MibTableColumn
ipfixTransportSessionSourceAddress=_IpfixTransportSessionSourceAddress_Object((1,3,6,1,2,1,193,1,1,1,1,4),_IpfixTransportSessionSourceAddress_Type())
ipfixTransportSessionSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionSourceAddress.setStatus(_A)
class _IpfixTransportSessionDestinationAddressType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('ipv4',1),('ipv6',2)))
_IpfixTransportSessionDestinationAddressType_Type.__name__=_K
_IpfixTransportSessionDestinationAddressType_Object=MibTableColumn
ipfixTransportSessionDestinationAddressType=_IpfixTransportSessionDestinationAddressType_Object((1,3,6,1,2,1,193,1,1,1,1,5),_IpfixTransportSessionDestinationAddressType_Type())
ipfixTransportSessionDestinationAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionDestinationAddressType.setStatus(_A)
_IpfixTransportSessionDestinationAddress_Type=InetAddress
_IpfixTransportSessionDestinationAddress_Object=MibTableColumn
ipfixTransportSessionDestinationAddress=_IpfixTransportSessionDestinationAddress_Object((1,3,6,1,2,1,193,1,1,1,1,6),_IpfixTransportSessionDestinationAddress_Type())
ipfixTransportSessionDestinationAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionDestinationAddress.setStatus(_A)
_IpfixTransportSessionSourcePort_Type=InetPortNumber
_IpfixTransportSessionSourcePort_Object=MibTableColumn
ipfixTransportSessionSourcePort=_IpfixTransportSessionSourcePort_Object((1,3,6,1,2,1,193,1,1,1,1,7),_IpfixTransportSessionSourcePort_Type())
ipfixTransportSessionSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionSourcePort.setStatus(_A)
_IpfixTransportSessionDestinationPort_Type=InetPortNumber
_IpfixTransportSessionDestinationPort_Object=MibTableColumn
ipfixTransportSessionDestinationPort=_IpfixTransportSessionDestinationPort_Object((1,3,6,1,2,1,193,1,1,1,1,8),_IpfixTransportSessionDestinationPort_Type())
ipfixTransportSessionDestinationPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionDestinationPort.setStatus(_A)
_IpfixTransportSessionSctpAssocId_Type=Unsigned32
_IpfixTransportSessionSctpAssocId_Object=MibTableColumn
ipfixTransportSessionSctpAssocId=_IpfixTransportSessionSctpAssocId_Object((1,3,6,1,2,1,193,1,1,1,1,9),_IpfixTransportSessionSctpAssocId_Type())
ipfixTransportSessionSctpAssocId.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionSctpAssocId.setStatus(_A)
class _IpfixTransportSessionDeviceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('exporting',1),('collecting',2)))
_IpfixTransportSessionDeviceMode_Type.__name__=_F
_IpfixTransportSessionDeviceMode_Object=MibTableColumn
ipfixTransportSessionDeviceMode=_IpfixTransportSessionDeviceMode_Object((1,3,6,1,2,1,193,1,1,1,1,10),_IpfixTransportSessionDeviceMode_Type())
ipfixTransportSessionDeviceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionDeviceMode.setStatus(_A)
_IpfixTransportSessionTemplateRefreshTimeout_Type=Unsigned32
_IpfixTransportSessionTemplateRefreshTimeout_Object=MibTableColumn
ipfixTransportSessionTemplateRefreshTimeout=_IpfixTransportSessionTemplateRefreshTimeout_Object((1,3,6,1,2,1,193,1,1,1,1,11),_IpfixTransportSessionTemplateRefreshTimeout_Type())
ipfixTransportSessionTemplateRefreshTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionTemplateRefreshTimeout.setStatus(_A)
if mibBuilder.loadTexts:ipfixTransportSessionTemplateRefreshTimeout.setUnits(_I)
_IpfixTransportSessionOptionsTemplateRefreshTimeout_Type=Unsigned32
_IpfixTransportSessionOptionsTemplateRefreshTimeout_Object=MibTableColumn
ipfixTransportSessionOptionsTemplateRefreshTimeout=_IpfixTransportSessionOptionsTemplateRefreshTimeout_Object((1,3,6,1,2,1,193,1,1,1,1,12),_IpfixTransportSessionOptionsTemplateRefreshTimeout_Type())
ipfixTransportSessionOptionsTemplateRefreshTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionOptionsTemplateRefreshTimeout.setStatus(_A)
if mibBuilder.loadTexts:ipfixTransportSessionOptionsTemplateRefreshTimeout.setUnits(_I)
_IpfixTransportSessionTemplateRefreshPacket_Type=Unsigned32
_IpfixTransportSessionTemplateRefreshPacket_Object=MibTableColumn
ipfixTransportSessionTemplateRefreshPacket=_IpfixTransportSessionTemplateRefreshPacket_Object((1,3,6,1,2,1,193,1,1,1,1,13),_IpfixTransportSessionTemplateRefreshPacket_Type())
ipfixTransportSessionTemplateRefreshPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionTemplateRefreshPacket.setStatus(_A)
if mibBuilder.loadTexts:ipfixTransportSessionTemplateRefreshPacket.setUnits(_L)
_IpfixTransportSessionOptionsTemplateRefreshPacket_Type=Unsigned32
_IpfixTransportSessionOptionsTemplateRefreshPacket_Object=MibTableColumn
ipfixTransportSessionOptionsTemplateRefreshPacket=_IpfixTransportSessionOptionsTemplateRefreshPacket_Object((1,3,6,1,2,1,193,1,1,1,1,14),_IpfixTransportSessionOptionsTemplateRefreshPacket_Type())
ipfixTransportSessionOptionsTemplateRefreshPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionOptionsTemplateRefreshPacket.setStatus(_A)
if mibBuilder.loadTexts:ipfixTransportSessionOptionsTemplateRefreshPacket.setUnits(_L)
class _IpfixTransportSessionIpfixVersion_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpfixTransportSessionIpfixVersion_Type.__name__=_D
_IpfixTransportSessionIpfixVersion_Object=MibTableColumn
ipfixTransportSessionIpfixVersion=_IpfixTransportSessionIpfixVersion_Object((1,3,6,1,2,1,193,1,1,1,1,15),_IpfixTransportSessionIpfixVersion_Type())
ipfixTransportSessionIpfixVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionIpfixVersion.setStatus(_A)
class _IpfixTransportSessionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('inactive',1),('active',2)))
_IpfixTransportSessionStatus_Type.__name__=_F
_IpfixTransportSessionStatus_Object=MibTableColumn
ipfixTransportSessionStatus=_IpfixTransportSessionStatus_Object((1,3,6,1,2,1,193,1,1,1,1,16),_IpfixTransportSessionStatus_Type())
ipfixTransportSessionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionStatus.setStatus(_A)
_IpfixTemplateTable_Object=MibTable
ipfixTemplateTable=_IpfixTemplateTable_Object((1,3,6,1,2,1,193,1,1,2))
if mibBuilder.loadTexts:ipfixTemplateTable.setStatus(_A)
_IpfixTemplateEntry_Object=MibTableRow
ipfixTemplateEntry=_IpfixTemplateEntry_Object((1,3,6,1,2,1,193,1,1,2,1))
ipfixTemplateEntry.setIndexNames((0,_B,_G),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:ipfixTemplateEntry.setStatus(_A)
class _IpfixTemplateObservationDomainId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_IpfixTemplateObservationDomainId_Type.__name__=_D
_IpfixTemplateObservationDomainId_Object=MibTableColumn
ipfixTemplateObservationDomainId=_IpfixTemplateObservationDomainId_Object((1,3,6,1,2,1,193,1,1,2,1,1),_IpfixTemplateObservationDomainId_Type())
ipfixTemplateObservationDomainId.setMaxAccess(_E)
if mibBuilder.loadTexts:ipfixTemplateObservationDomainId.setStatus(_A)
class _IpfixTemplateId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,65535))
_IpfixTemplateId_Type.__name__=_D
_IpfixTemplateId_Object=MibTableColumn
ipfixTemplateId=_IpfixTemplateId_Object((1,3,6,1,2,1,193,1,1,2,1,2),_IpfixTemplateId_Type())
ipfixTemplateId.setMaxAccess(_E)
if mibBuilder.loadTexts:ipfixTemplateId.setStatus(_A)
class _IpfixTemplateSetId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpfixTemplateSetId_Type.__name__=_D
_IpfixTemplateSetId_Object=MibTableColumn
ipfixTemplateSetId=_IpfixTemplateSetId_Object((1,3,6,1,2,1,193,1,1,2,1,3),_IpfixTemplateSetId_Type())
ipfixTemplateSetId.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTemplateSetId.setStatus(_A)
_IpfixTemplateAccessTime_Type=DateAndTime
_IpfixTemplateAccessTime_Object=MibTableColumn
ipfixTemplateAccessTime=_IpfixTemplateAccessTime_Object((1,3,6,1,2,1,193,1,1,2,1,4),_IpfixTemplateAccessTime_Type())
ipfixTemplateAccessTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTemplateAccessTime.setStatus(_A)
_IpfixTemplateDefinitionTable_Object=MibTable
ipfixTemplateDefinitionTable=_IpfixTemplateDefinitionTable_Object((1,3,6,1,2,1,193,1,1,3))
if mibBuilder.loadTexts:ipfixTemplateDefinitionTable.setStatus(_A)
_IpfixTemplateDefinitionEntry_Object=MibTableRow
ipfixTemplateDefinitionEntry=_IpfixTemplateDefinitionEntry_Object((1,3,6,1,2,1,193,1,1,3,1))
ipfixTemplateDefinitionEntry.setIndexNames((0,_B,_G),(0,_B,_M),(0,_B,_N),(0,_B,_Q))
if mibBuilder.loadTexts:ipfixTemplateDefinitionEntry.setStatus(_A)
class _IpfixTemplateDefinitionIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpfixTemplateDefinitionIndex_Type.__name__=_D
_IpfixTemplateDefinitionIndex_Object=MibTableColumn
ipfixTemplateDefinitionIndex=_IpfixTemplateDefinitionIndex_Object((1,3,6,1,2,1,193,1,1,3,1,1),_IpfixTemplateDefinitionIndex_Type())
ipfixTemplateDefinitionIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ipfixTemplateDefinitionIndex.setStatus(_A)
class _IpfixTemplateDefinitionIeId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpfixTemplateDefinitionIeId_Type.__name__=_D
_IpfixTemplateDefinitionIeId_Object=MibTableColumn
ipfixTemplateDefinitionIeId=_IpfixTemplateDefinitionIeId_Object((1,3,6,1,2,1,193,1,1,3,1,2),_IpfixTemplateDefinitionIeId_Type())
ipfixTemplateDefinitionIeId.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTemplateDefinitionIeId.setStatus(_A)
class _IpfixTemplateDefinitionIeLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpfixTemplateDefinitionIeLength_Type.__name__=_D
_IpfixTemplateDefinitionIeLength_Object=MibTableColumn
ipfixTemplateDefinitionIeLength=_IpfixTemplateDefinitionIeLength_Object((1,3,6,1,2,1,193,1,1,3,1,3),_IpfixTemplateDefinitionIeLength_Type())
ipfixTemplateDefinitionIeLength.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTemplateDefinitionIeLength.setStatus(_A)
_IpfixTemplateDefinitionEnterpriseNumber_Type=Unsigned32
_IpfixTemplateDefinitionEnterpriseNumber_Object=MibTableColumn
ipfixTemplateDefinitionEnterpriseNumber=_IpfixTemplateDefinitionEnterpriseNumber_Object((1,3,6,1,2,1,193,1,1,3,1,4),_IpfixTemplateDefinitionEnterpriseNumber_Type())
ipfixTemplateDefinitionEnterpriseNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTemplateDefinitionEnterpriseNumber.setStatus(_A)
class _IpfixTemplateDefinitionFlags_Type(Bits):namedValues=NamedValues(*(('scope',0),('flowKey',1)))
_IpfixTemplateDefinitionFlags_Type.__name__='Bits'
_IpfixTemplateDefinitionFlags_Object=MibTableColumn
ipfixTemplateDefinitionFlags=_IpfixTemplateDefinitionFlags_Object((1,3,6,1,2,1,193,1,1,3,1,5),_IpfixTemplateDefinitionFlags_Type())
ipfixTemplateDefinitionFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTemplateDefinitionFlags.setStatus(_A)
_IpfixExportTable_Object=MibTable
ipfixExportTable=_IpfixExportTable_Object((1,3,6,1,2,1,193,1,1,4))
if mibBuilder.loadTexts:ipfixExportTable.setStatus(_A)
_IpfixExportEntry_Object=MibTableRow
ipfixExportEntry=_IpfixExportEntry_Object((1,3,6,1,2,1,193,1,1,4,1))
ipfixExportEntry.setIndexNames((0,_B,_R),(0,_B,_J),(0,_B,_G))
if mibBuilder.loadTexts:ipfixExportEntry.setStatus(_A)
class _IpfixExportIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_IpfixExportIndex_Type.__name__=_D
_IpfixExportIndex_Object=MibTableColumn
ipfixExportIndex=_IpfixExportIndex_Object((1,3,6,1,2,1,193,1,1,4,1,1),_IpfixExportIndex_Type())
ipfixExportIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ipfixExportIndex.setStatus(_A)
class _IpfixExportMemberType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),('primary',1),('secondary',2),('parallel',3),('loadBalancing',4)))
_IpfixExportMemberType_Type.__name__=_F
_IpfixExportMemberType_Object=MibTableColumn
ipfixExportMemberType=_IpfixExportMemberType_Object((1,3,6,1,2,1,193,1,1,4,1,2),_IpfixExportMemberType_Type())
ipfixExportMemberType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixExportMemberType.setStatus(_A)
_IpfixMeteringProcessTable_Object=MibTable
ipfixMeteringProcessTable=_IpfixMeteringProcessTable_Object((1,3,6,1,2,1,193,1,1,5))
if mibBuilder.loadTexts:ipfixMeteringProcessTable.setStatus(_A)
_IpfixMeteringProcessEntry_Object=MibTableRow
ipfixMeteringProcessEntry=_IpfixMeteringProcessEntry_Object((1,3,6,1,2,1,193,1,1,5,1))
ipfixMeteringProcessEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:ipfixMeteringProcessEntry.setStatus(_A)
class _IpfixMeteringProcessCacheId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_IpfixMeteringProcessCacheId_Type.__name__=_D
_IpfixMeteringProcessCacheId_Object=MibTableColumn
ipfixMeteringProcessCacheId=_IpfixMeteringProcessCacheId_Object((1,3,6,1,2,1,193,1,1,5,1,1),_IpfixMeteringProcessCacheId_Type())
ipfixMeteringProcessCacheId.setMaxAccess(_E)
if mibBuilder.loadTexts:ipfixMeteringProcessCacheId.setStatus(_A)
_IpfixMeteringProcessObservationPointGroupRef_Type=Unsigned32
_IpfixMeteringProcessObservationPointGroupRef_Object=MibTableColumn
ipfixMeteringProcessObservationPointGroupRef=_IpfixMeteringProcessObservationPointGroupRef_Object((1,3,6,1,2,1,193,1,1,5,1,2),_IpfixMeteringProcessObservationPointGroupRef_Type())
ipfixMeteringProcessObservationPointGroupRef.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixMeteringProcessObservationPointGroupRef.setStatus(_A)
_IpfixMeteringProcessCacheActiveTimeout_Type=Unsigned32
_IpfixMeteringProcessCacheActiveTimeout_Object=MibTableColumn
ipfixMeteringProcessCacheActiveTimeout=_IpfixMeteringProcessCacheActiveTimeout_Object((1,3,6,1,2,1,193,1,1,5,1,3),_IpfixMeteringProcessCacheActiveTimeout_Type())
ipfixMeteringProcessCacheActiveTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixMeteringProcessCacheActiveTimeout.setStatus(_A)
if mibBuilder.loadTexts:ipfixMeteringProcessCacheActiveTimeout.setUnits(_I)
_IpfixMeteringProcessCacheIdleTimeout_Type=Unsigned32
_IpfixMeteringProcessCacheIdleTimeout_Object=MibTableColumn
ipfixMeteringProcessCacheIdleTimeout=_IpfixMeteringProcessCacheIdleTimeout_Object((1,3,6,1,2,1,193,1,1,5,1,4),_IpfixMeteringProcessCacheIdleTimeout_Type())
ipfixMeteringProcessCacheIdleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixMeteringProcessCacheIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:ipfixMeteringProcessCacheIdleTimeout.setUnits(_I)
_IpfixObservationPointTable_Object=MibTable
ipfixObservationPointTable=_IpfixObservationPointTable_Object((1,3,6,1,2,1,193,1,1,6))
if mibBuilder.loadTexts:ipfixObservationPointTable.setStatus(_A)
_IpfixObservationPointEntry_Object=MibTableRow
ipfixObservationPointEntry=_IpfixObservationPointEntry_Object((1,3,6,1,2,1,193,1,1,6,1))
ipfixObservationPointEntry.setIndexNames((0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:ipfixObservationPointEntry.setStatus(_A)
class _IpfixObservationPointGroupId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_IpfixObservationPointGroupId_Type.__name__=_D
_IpfixObservationPointGroupId_Object=MibTableColumn
ipfixObservationPointGroupId=_IpfixObservationPointGroupId_Object((1,3,6,1,2,1,193,1,1,6,1,1),_IpfixObservationPointGroupId_Type())
ipfixObservationPointGroupId.setMaxAccess(_E)
if mibBuilder.loadTexts:ipfixObservationPointGroupId.setStatus(_A)
class _IpfixObservationPointIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_IpfixObservationPointIndex_Type.__name__=_D
_IpfixObservationPointIndex_Object=MibTableColumn
ipfixObservationPointIndex=_IpfixObservationPointIndex_Object((1,3,6,1,2,1,193,1,1,6,1,2),_IpfixObservationPointIndex_Type())
ipfixObservationPointIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ipfixObservationPointIndex.setStatus(_A)
_IpfixObservationPointObservationDomainId_Type=Unsigned32
_IpfixObservationPointObservationDomainId_Object=MibTableColumn
ipfixObservationPointObservationDomainId=_IpfixObservationPointObservationDomainId_Object((1,3,6,1,2,1,193,1,1,6,1,3),_IpfixObservationPointObservationDomainId_Type())
ipfixObservationPointObservationDomainId.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixObservationPointObservationDomainId.setStatus(_A)
_IpfixObservationPointPhysicalEntity_Type=PhysicalIndexOrZero
_IpfixObservationPointPhysicalEntity_Object=MibTableColumn
ipfixObservationPointPhysicalEntity=_IpfixObservationPointPhysicalEntity_Object((1,3,6,1,2,1,193,1,1,6,1,4),_IpfixObservationPointPhysicalEntity_Type())
ipfixObservationPointPhysicalEntity.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixObservationPointPhysicalEntity.setStatus(_A)
_IpfixObservationPointPhysicalInterface_Type=InterfaceIndexOrZero
_IpfixObservationPointPhysicalInterface_Object=MibTableColumn
ipfixObservationPointPhysicalInterface=_IpfixObservationPointPhysicalInterface_Object((1,3,6,1,2,1,193,1,1,6,1,5),_IpfixObservationPointPhysicalInterface_Type())
ipfixObservationPointPhysicalInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixObservationPointPhysicalInterface.setStatus(_A)
class _IpfixObservationPointPhysicalEntityDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),('ingress',1),('egress',2),('both',3)))
_IpfixObservationPointPhysicalEntityDirection_Type.__name__=_F
_IpfixObservationPointPhysicalEntityDirection_Object=MibTableColumn
ipfixObservationPointPhysicalEntityDirection=_IpfixObservationPointPhysicalEntityDirection_Object((1,3,6,1,2,1,193,1,1,6,1,6),_IpfixObservationPointPhysicalEntityDirection_Type())
ipfixObservationPointPhysicalEntityDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixObservationPointPhysicalEntityDirection.setStatus(_A)
_IpfixSelectionProcessTable_Object=MibTable
ipfixSelectionProcessTable=_IpfixSelectionProcessTable_Object((1,3,6,1,2,1,193,1,1,7))
if mibBuilder.loadTexts:ipfixSelectionProcessTable.setStatus(_A)
_IpfixSelectionProcessEntry_Object=MibTableRow
ipfixSelectionProcessEntry=_IpfixSelectionProcessEntry_Object((1,3,6,1,2,1,193,1,1,7,1))
ipfixSelectionProcessEntry.setIndexNames((0,_B,_J),(0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:ipfixSelectionProcessEntry.setStatus(_A)
class _IpfixSelectionProcessIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_IpfixSelectionProcessIndex_Type.__name__=_D
_IpfixSelectionProcessIndex_Object=MibTableColumn
ipfixSelectionProcessIndex=_IpfixSelectionProcessIndex_Object((1,3,6,1,2,1,193,1,1,7,1,1),_IpfixSelectionProcessIndex_Type())
ipfixSelectionProcessIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ipfixSelectionProcessIndex.setStatus(_A)
class _IpfixSelectionProcessSelectorIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_IpfixSelectionProcessSelectorIndex_Type.__name__=_D
_IpfixSelectionProcessSelectorIndex_Object=MibTableColumn
ipfixSelectionProcessSelectorIndex=_IpfixSelectionProcessSelectorIndex_Object((1,3,6,1,2,1,193,1,1,7,1,2),_IpfixSelectionProcessSelectorIndex_Type())
ipfixSelectionProcessSelectorIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ipfixSelectionProcessSelectorIndex.setStatus(_A)
_IpfixSelectionProcessSelectorFunction_Type=ObjectIdentifier
_IpfixSelectionProcessSelectorFunction_Object=MibTableColumn
ipfixSelectionProcessSelectorFunction=_IpfixSelectionProcessSelectorFunction_Object((1,3,6,1,2,1,193,1,1,7,1,3),_IpfixSelectionProcessSelectorFunction_Type())
ipfixSelectionProcessSelectorFunction.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixSelectionProcessSelectorFunction.setStatus(_A)
_IpfixStatistics_ObjectIdentity=ObjectIdentity
ipfixStatistics=_IpfixStatistics_ObjectIdentity((1,3,6,1,2,1,193,1,2))
_IpfixTransportSessionStatsTable_Object=MibTable
ipfixTransportSessionStatsTable=_IpfixTransportSessionStatsTable_Object((1,3,6,1,2,1,193,1,2,1))
if mibBuilder.loadTexts:ipfixTransportSessionStatsTable.setStatus(_A)
_IpfixTransportSessionStatsEntry_Object=MibTableRow
ipfixTransportSessionStatsEntry=_IpfixTransportSessionStatsEntry_Object((1,3,6,1,2,1,193,1,2,1,1))
if mibBuilder.loadTexts:ipfixTransportSessionStatsEntry.setStatus(_A)
_IpfixTransportSessionRate_Type=Gauge32
_IpfixTransportSessionRate_Object=MibTableColumn
ipfixTransportSessionRate=_IpfixTransportSessionRate_Object((1,3,6,1,2,1,193,1,2,1,1,1),_IpfixTransportSessionRate_Type())
ipfixTransportSessionRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionRate.setStatus(_A)
if mibBuilder.loadTexts:ipfixTransportSessionRate.setUnits('bytes/second')
_IpfixTransportSessionPackets_Type=Counter64
_IpfixTransportSessionPackets_Object=MibTableColumn
ipfixTransportSessionPackets=_IpfixTransportSessionPackets_Object((1,3,6,1,2,1,193,1,2,1,1,2),_IpfixTransportSessionPackets_Type())
ipfixTransportSessionPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionPackets.setStatus(_A)
if mibBuilder.loadTexts:ipfixTransportSessionPackets.setUnits(_L)
_IpfixTransportSessionBytes_Type=Counter64
_IpfixTransportSessionBytes_Object=MibTableColumn
ipfixTransportSessionBytes=_IpfixTransportSessionBytes_Object((1,3,6,1,2,1,193,1,2,1,1,3),_IpfixTransportSessionBytes_Type())
ipfixTransportSessionBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionBytes.setStatus(_A)
if mibBuilder.loadTexts:ipfixTransportSessionBytes.setUnits('bytes')
_IpfixTransportSessionMessages_Type=Counter64
_IpfixTransportSessionMessages_Object=MibTableColumn
ipfixTransportSessionMessages=_IpfixTransportSessionMessages_Object((1,3,6,1,2,1,193,1,2,1,1,4),_IpfixTransportSessionMessages_Type())
ipfixTransportSessionMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionMessages.setStatus(_A)
_IpfixTransportSessionDiscardedMessages_Type=Counter64
_IpfixTransportSessionDiscardedMessages_Object=MibTableColumn
ipfixTransportSessionDiscardedMessages=_IpfixTransportSessionDiscardedMessages_Object((1,3,6,1,2,1,193,1,2,1,1,5),_IpfixTransportSessionDiscardedMessages_Type())
ipfixTransportSessionDiscardedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionDiscardedMessages.setStatus(_A)
_IpfixTransportSessionRecords_Type=Counter64
_IpfixTransportSessionRecords_Object=MibTableColumn
ipfixTransportSessionRecords=_IpfixTransportSessionRecords_Object((1,3,6,1,2,1,193,1,2,1,1,6),_IpfixTransportSessionRecords_Type())
ipfixTransportSessionRecords.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionRecords.setStatus(_A)
_IpfixTransportSessionTemplates_Type=Counter64
_IpfixTransportSessionTemplates_Object=MibTableColumn
ipfixTransportSessionTemplates=_IpfixTransportSessionTemplates_Object((1,3,6,1,2,1,193,1,2,1,1,7),_IpfixTransportSessionTemplates_Type())
ipfixTransportSessionTemplates.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionTemplates.setStatus(_A)
_IpfixTransportSessionOptionsTemplates_Type=Counter64
_IpfixTransportSessionOptionsTemplates_Object=MibTableColumn
ipfixTransportSessionOptionsTemplates=_IpfixTransportSessionOptionsTemplates_Object((1,3,6,1,2,1,193,1,2,1,1,8),_IpfixTransportSessionOptionsTemplates_Type())
ipfixTransportSessionOptionsTemplates.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionOptionsTemplates.setStatus(_A)
_IpfixTransportSessionDiscontinuityTime_Type=TimeStamp
_IpfixTransportSessionDiscontinuityTime_Object=MibTableColumn
ipfixTransportSessionDiscontinuityTime=_IpfixTransportSessionDiscontinuityTime_Object((1,3,6,1,2,1,193,1,2,1,1,9),_IpfixTransportSessionDiscontinuityTime_Type())
ipfixTransportSessionDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTransportSessionDiscontinuityTime.setStatus(_A)
_IpfixTemplateStatsTable_Object=MibTable
ipfixTemplateStatsTable=_IpfixTemplateStatsTable_Object((1,3,6,1,2,1,193,1,2,2))
if mibBuilder.loadTexts:ipfixTemplateStatsTable.setStatus(_A)
_IpfixTemplateStatsEntry_Object=MibTableRow
ipfixTemplateStatsEntry=_IpfixTemplateStatsEntry_Object((1,3,6,1,2,1,193,1,2,2,1))
if mibBuilder.loadTexts:ipfixTemplateStatsEntry.setStatus(_A)
_IpfixTemplateDataRecords_Type=Counter64
_IpfixTemplateDataRecords_Object=MibTableColumn
ipfixTemplateDataRecords=_IpfixTemplateDataRecords_Object((1,3,6,1,2,1,193,1,2,2,1,1),_IpfixTemplateDataRecords_Type())
ipfixTemplateDataRecords.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTemplateDataRecords.setStatus(_A)
_IpfixTemplateDiscontinuityTime_Type=TimeStamp
_IpfixTemplateDiscontinuityTime_Object=MibTableColumn
ipfixTemplateDiscontinuityTime=_IpfixTemplateDiscontinuityTime_Object((1,3,6,1,2,1,193,1,2,2,1,2),_IpfixTemplateDiscontinuityTime_Type())
ipfixTemplateDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixTemplateDiscontinuityTime.setStatus(_A)
_IpfixMeteringProcessStatsTable_Object=MibTable
ipfixMeteringProcessStatsTable=_IpfixMeteringProcessStatsTable_Object((1,3,6,1,2,1,193,1,2,3))
if mibBuilder.loadTexts:ipfixMeteringProcessStatsTable.setStatus(_A)
_IpfixMeteringProcessStatsEntry_Object=MibTableRow
ipfixMeteringProcessStatsEntry=_IpfixMeteringProcessStatsEntry_Object((1,3,6,1,2,1,193,1,2,3,1))
if mibBuilder.loadTexts:ipfixMeteringProcessStatsEntry.setStatus(_A)
_IpfixMeteringProcessCacheActiveFlows_Type=Gauge32
_IpfixMeteringProcessCacheActiveFlows_Object=MibTableColumn
ipfixMeteringProcessCacheActiveFlows=_IpfixMeteringProcessCacheActiveFlows_Object((1,3,6,1,2,1,193,1,2,3,1,1),_IpfixMeteringProcessCacheActiveFlows_Type())
ipfixMeteringProcessCacheActiveFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixMeteringProcessCacheActiveFlows.setStatus(_A)
_IpfixMeteringProcessCacheUnusedCacheEntries_Type=Gauge32
_IpfixMeteringProcessCacheUnusedCacheEntries_Object=MibTableColumn
ipfixMeteringProcessCacheUnusedCacheEntries=_IpfixMeteringProcessCacheUnusedCacheEntries_Object((1,3,6,1,2,1,193,1,2,3,1,2),_IpfixMeteringProcessCacheUnusedCacheEntries_Type())
ipfixMeteringProcessCacheUnusedCacheEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixMeteringProcessCacheUnusedCacheEntries.setStatus(_A)
_IpfixMeteringProcessCacheDataRecords_Type=Counter64
_IpfixMeteringProcessCacheDataRecords_Object=MibTableColumn
ipfixMeteringProcessCacheDataRecords=_IpfixMeteringProcessCacheDataRecords_Object((1,3,6,1,2,1,193,1,2,3,1,3),_IpfixMeteringProcessCacheDataRecords_Type())
ipfixMeteringProcessCacheDataRecords.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixMeteringProcessCacheDataRecords.setStatus(_A)
_IpfixMeteringProcessCacheDiscontinuityTime_Type=TimeStamp
_IpfixMeteringProcessCacheDiscontinuityTime_Object=MibTableColumn
ipfixMeteringProcessCacheDiscontinuityTime=_IpfixMeteringProcessCacheDiscontinuityTime_Object((1,3,6,1,2,1,193,1,2,3,1,4),_IpfixMeteringProcessCacheDiscontinuityTime_Type())
ipfixMeteringProcessCacheDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixMeteringProcessCacheDiscontinuityTime.setStatus(_A)
_IpfixSelectionProcessStatsTable_Object=MibTable
ipfixSelectionProcessStatsTable=_IpfixSelectionProcessStatsTable_Object((1,3,6,1,2,1,193,1,2,4))
if mibBuilder.loadTexts:ipfixSelectionProcessStatsTable.setStatus(_A)
_IpfixSelectionProcessStatsEntry_Object=MibTableRow
ipfixSelectionProcessStatsEntry=_IpfixSelectionProcessStatsEntry_Object((1,3,6,1,2,1,193,1,2,4,1))
if mibBuilder.loadTexts:ipfixSelectionProcessStatsEntry.setStatus(_A)
_IpfixSelectionProcessStatsPacketsObserved_Type=Counter64
_IpfixSelectionProcessStatsPacketsObserved_Object=MibTableColumn
ipfixSelectionProcessStatsPacketsObserved=_IpfixSelectionProcessStatsPacketsObserved_Object((1,3,6,1,2,1,193,1,2,4,1,1),_IpfixSelectionProcessStatsPacketsObserved_Type())
ipfixSelectionProcessStatsPacketsObserved.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixSelectionProcessStatsPacketsObserved.setStatus(_A)
_IpfixSelectionProcessStatsPacketsDropped_Type=Counter64
_IpfixSelectionProcessStatsPacketsDropped_Object=MibTableColumn
ipfixSelectionProcessStatsPacketsDropped=_IpfixSelectionProcessStatsPacketsDropped_Object((1,3,6,1,2,1,193,1,2,4,1,2),_IpfixSelectionProcessStatsPacketsDropped_Type())
ipfixSelectionProcessStatsPacketsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixSelectionProcessStatsPacketsDropped.setStatus(_A)
_IpfixSelectionProcessStatsDiscontinuityTime_Type=TimeStamp
_IpfixSelectionProcessStatsDiscontinuityTime_Object=MibTableColumn
ipfixSelectionProcessStatsDiscontinuityTime=_IpfixSelectionProcessStatsDiscontinuityTime_Object((1,3,6,1,2,1,193,1,2,4,1,3),_IpfixSelectionProcessStatsDiscontinuityTime_Type())
ipfixSelectionProcessStatsDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipfixSelectionProcessStatsDiscontinuityTime.setStatus(_A)
_IpfixConformance_ObjectIdentity=ObjectIdentity
ipfixConformance=_IpfixConformance_ObjectIdentity((1,3,6,1,2,1,193,2))
_IpfixCompliances_ObjectIdentity=ObjectIdentity
ipfixCompliances=_IpfixCompliances_ObjectIdentity((1,3,6,1,2,1,193,2,1))
_IpfixGroups_ObjectIdentity=ObjectIdentity
ipfixGroups=_IpfixGroups_ObjectIdentity((1,3,6,1,2,1,193,2,2))
ipfixTransportSessionEntry.registerAugmentions((_B,_W))
ipfixTransportSessionStatsEntry.setIndexNames(*ipfixTransportSessionEntry.getIndexNames())
ipfixTemplateEntry.registerAugmentions((_B,_X))
ipfixTemplateStatsEntry.setIndexNames(*ipfixTemplateEntry.getIndexNames())
ipfixMeteringProcessEntry.registerAugmentions((_B,_Y))
ipfixMeteringProcessStatsEntry.setIndexNames(*ipfixMeteringProcessEntry.getIndexNames())
ipfixSelectionProcessEntry.registerAugmentions((_B,_Z))
ipfixSelectionProcessStatsEntry.setIndexNames(*ipfixSelectionProcessEntry.getIndexNames())
ipfixCommonGroup=ObjectGroup((1,3,6,1,2,1,193,2,2,1))
ipfixCommonGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:ipfixCommonGroup.setStatus(_A)
ipfixCommonStatsGroup=ObjectGroup((1,3,6,1,2,1,193,2,2,2))
ipfixCommonStatsGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:ipfixCommonStatsGroup.setStatus(_A)
ipfixExporterGroup=ObjectGroup((1,3,6,1,2,1,193,2,2,3))
ipfixExporterGroup.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:ipfixExporterGroup.setStatus(_A)
ipfixExporterStatsGroup=ObjectGroup((1,3,6,1,2,1,193,2,2,4))
ipfixExporterStatsGroup.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:ipfixExporterStatsGroup.setStatus(_A)
ipfixCollectorCompliance=ModuleCompliance((1,3,6,1,2,1,193,2,1,1))
ipfixCollectorCompliance.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ipfixCollectorCompliance.setStatus(_A)
ipfixExporterCompliance=ModuleCompliance((1,3,6,1,2,1,193,2,1,2))
ipfixExporterCompliance.setObjects(*((_B,_O),(_B,_AM),(_B,_P),(_B,_AN)))
if mibBuilder.loadTexts:ipfixExporterCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ipfixMIB':ipfixMIB,'ipfixObjects':ipfixObjects,'ipfixMainObjects':ipfixMainObjects,'ipfixTransportSessionTable':ipfixTransportSessionTable,'ipfixTransportSessionEntry':ipfixTransportSessionEntry,_G:ipfixTransportSessionIndex,_a:ipfixTransportSessionProtocol,_b:ipfixTransportSessionSourceAddressType,_c:ipfixTransportSessionSourceAddress,_d:ipfixTransportSessionDestinationAddressType,_e:ipfixTransportSessionDestinationAddress,_f:ipfixTransportSessionSourcePort,_g:ipfixTransportSessionDestinationPort,_h:ipfixTransportSessionSctpAssocId,_i:ipfixTransportSessionDeviceMode,_j:ipfixTransportSessionTemplateRefreshTimeout,_k:ipfixTransportSessionOptionsTemplateRefreshTimeout,_l:ipfixTransportSessionTemplateRefreshPacket,_m:ipfixTransportSessionOptionsTemplateRefreshPacket,_n:ipfixTransportSessionIpfixVersion,_o:ipfixTransportSessionStatus,'ipfixTemplateTable':ipfixTemplateTable,'ipfixTemplateEntry':ipfixTemplateEntry,_M:ipfixTemplateObservationDomainId,_N:ipfixTemplateId,_p:ipfixTemplateSetId,_q:ipfixTemplateAccessTime,'ipfixTemplateDefinitionTable':ipfixTemplateDefinitionTable,'ipfixTemplateDefinitionEntry':ipfixTemplateDefinitionEntry,_Q:ipfixTemplateDefinitionIndex,_r:ipfixTemplateDefinitionIeId,_s:ipfixTemplateDefinitionIeLength,_t:ipfixTemplateDefinitionEnterpriseNumber,_u:ipfixTemplateDefinitionFlags,'ipfixExportTable':ipfixExportTable,'ipfixExportEntry':ipfixExportEntry,_R:ipfixExportIndex,_A6:ipfixExportMemberType,'ipfixMeteringProcessTable':ipfixMeteringProcessTable,'ipfixMeteringProcessEntry':ipfixMeteringProcessEntry,_J:ipfixMeteringProcessCacheId,_A7:ipfixMeteringProcessObservationPointGroupRef,_A8:ipfixMeteringProcessCacheActiveTimeout,_A9:ipfixMeteringProcessCacheIdleTimeout,'ipfixObservationPointTable':ipfixObservationPointTable,'ipfixObservationPointEntry':ipfixObservationPointEntry,_S:ipfixObservationPointGroupId,_T:ipfixObservationPointIndex,_AA:ipfixObservationPointObservationDomainId,_AB:ipfixObservationPointPhysicalEntity,_AC:ipfixObservationPointPhysicalInterface,_AD:ipfixObservationPointPhysicalEntityDirection,'ipfixSelectionProcessTable':ipfixSelectionProcessTable,'ipfixSelectionProcessEntry':ipfixSelectionProcessEntry,_U:ipfixSelectionProcessIndex,_V:ipfixSelectionProcessSelectorIndex,_AE:ipfixSelectionProcessSelectorFunction,'ipfixStatistics':ipfixStatistics,'ipfixTransportSessionStatsTable':ipfixTransportSessionStatsTable,_W:ipfixTransportSessionStatsEntry,_v:ipfixTransportSessionRate,_w:ipfixTransportSessionPackets,_x:ipfixTransportSessionBytes,_y:ipfixTransportSessionMessages,_z:ipfixTransportSessionDiscardedMessages,_A0:ipfixTransportSessionRecords,_A1:ipfixTransportSessionTemplates,_A2:ipfixTransportSessionOptionsTemplates,_A3:ipfixTransportSessionDiscontinuityTime,'ipfixTemplateStatsTable':ipfixTemplateStatsTable,_X:ipfixTemplateStatsEntry,_A4:ipfixTemplateDataRecords,_A5:ipfixTemplateDiscontinuityTime,'ipfixMeteringProcessStatsTable':ipfixMeteringProcessStatsTable,_Y:ipfixMeteringProcessStatsEntry,_AF:ipfixMeteringProcessCacheActiveFlows,_AG:ipfixMeteringProcessCacheUnusedCacheEntries,_AH:ipfixMeteringProcessCacheDataRecords,_AI:ipfixMeteringProcessCacheDiscontinuityTime,'ipfixSelectionProcessStatsTable':ipfixSelectionProcessStatsTable,_Z:ipfixSelectionProcessStatsEntry,_AJ:ipfixSelectionProcessStatsPacketsObserved,_AK:ipfixSelectionProcessStatsPacketsDropped,_AL:ipfixSelectionProcessStatsDiscontinuityTime,'ipfixConformance':ipfixConformance,'ipfixCompliances':ipfixCompliances,'ipfixCollectorCompliance':ipfixCollectorCompliance,'ipfixExporterCompliance':ipfixExporterCompliance,'ipfixGroups':ipfixGroups,_O:ipfixCommonGroup,_P:ipfixCommonStatsGroup,_AM:ipfixExporterGroup,_AN:ipfixExporterStatsGroup})