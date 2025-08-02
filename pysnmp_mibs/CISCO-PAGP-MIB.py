_u='ciscoPagpRateAndTimeOutGroup'
_t='ciscoPagpEthcGroupV1R1'
_s='pagpInPacketTimeout'
_r='pagpRate'
_q='pagpDistributionAddress'
_p='pagpDistributionProtocol'
_o='pagpInErrors'
_n='pagpOutFlushes'
_m='pagpReturnedFlushes'
_l='pagpInFlushes'
_k='pagpOutPackets'
_j='pagpInPackets'
_i='pagpPartnerAgportMACAddress'
_h='pagpPartnerPortName'
_g='pagpPartnerDeviceName'
_f='pagpPartnerGroupIfIndex'
_e='pagpPartnerGroupCapability'
_d='pagpPartnerIfIndex'
_c='pagpPartnerPortPriority'
_b='pagpPartnerLearnMethod'
_a='pagpPartnerDeviceId'
_Z='pagpPartnerCount'
_Y='pagpDistributionAlgorithm'
_X='pagpHelloFrequency'
_W='pagpLastStateChange'
_V='pagpPortState'
_U='pagpOperationMode'
_T='obsolete'
_S='Unsigned32'
_R='ciscoPagpEthcGroupV2R2'
_Q='pagpGroupIfIndex'
_P='pagpLearnMethod'
_O='pagpPortPriority'
_N='pagpAdminGroupCapability'
_M='pagpOperGroupCapability'
_L='pagpPhysGroupCapability'
_K='pagpDeviceId'
_J='pagpEthcOperationMode'
_I='ciscoPagpPagpGroupV1R1'
_H='ifIndex'
_G='IF-MIB'
_F='packets'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-PAGP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('CISCO-TC','InterfaceIndexOrZero')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_S,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp')
ciscoPagpMIB=ModuleIdentity((1,3,6,1,4,1,9,9,98))
if mibBuilder.loadTexts:ciscoPagpMIB.setRevisions(('2010-10-20 00:00','2008-02-01 00:00','2002-12-13 00:00','2002-01-02 00:00','1999-03-04 00:00','1998-04-09 00:00'))
class PagpGroupCapability(TextualConvention,Integer32):status=_B
class PagpEthcOperationMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('manual',2),('pagpOn',3)))
class PagpPortPriority(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class PagpOperationMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('desirable',1),('desirableSilent',2),('automatic',3),('automaticSilent',4)))
class PagpLearnMethod(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('physPort',1),('agPort',2),('undefined',3)))
_CiscoPagpMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPagpMIBObjects=_CiscoPagpMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,98,1))
_PagpGroupCapabilityConfiguration_ObjectIdentity=ObjectIdentity
pagpGroupCapabilityConfiguration=_PagpGroupCapabilityConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,98,1,1))
_PagpEtherChannelTable_Object=MibTable
pagpEtherChannelTable=_PagpEtherChannelTable_Object((1,3,6,1,4,1,9,9,98,1,1,1))
if mibBuilder.loadTexts:pagpEtherChannelTable.setStatus(_B)
_PagpEtherChannelEntry_Object=MibTableRow
pagpEtherChannelEntry=_PagpEtherChannelEntry_Object((1,3,6,1,4,1,9,9,98,1,1,1,1))
pagpEtherChannelEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:pagpEtherChannelEntry.setStatus(_B)
_PagpEthcOperationMode_Type=PagpEthcOperationMode
_PagpEthcOperationMode_Object=MibTableColumn
pagpEthcOperationMode=_PagpEthcOperationMode_Object((1,3,6,1,4,1,9,9,98,1,1,1,1,1),_PagpEthcOperationMode_Type())
pagpEthcOperationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pagpEthcOperationMode.setStatus(_B)
_PagpDeviceId_Type=MacAddress
_PagpDeviceId_Object=MibTableColumn
pagpDeviceId=_PagpDeviceId_Object((1,3,6,1,4,1,9,9,98,1,1,1,1,2),_PagpDeviceId_Type())
pagpDeviceId.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpDeviceId.setStatus(_B)
_PagpPhysGroupCapability_Type=PagpGroupCapability
_PagpPhysGroupCapability_Object=MibTableColumn
pagpPhysGroupCapability=_PagpPhysGroupCapability_Object((1,3,6,1,4,1,9,9,98,1,1,1,1,3),_PagpPhysGroupCapability_Type())
pagpPhysGroupCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpPhysGroupCapability.setStatus(_B)
_PagpOperGroupCapability_Type=PagpGroupCapability
_PagpOperGroupCapability_Object=MibTableColumn
pagpOperGroupCapability=_PagpOperGroupCapability_Object((1,3,6,1,4,1,9,9,98,1,1,1,1,4),_PagpOperGroupCapability_Type())
pagpOperGroupCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpOperGroupCapability.setStatus(_B)
_PagpAdminGroupCapability_Type=PagpGroupCapability
_PagpAdminGroupCapability_Object=MibTableColumn
pagpAdminGroupCapability=_PagpAdminGroupCapability_Object((1,3,6,1,4,1,9,9,98,1,1,1,1,5),_PagpAdminGroupCapability_Type())
pagpAdminGroupCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:pagpAdminGroupCapability.setStatus(_B)
_PagpPortPriority_Type=PagpPortPriority
_PagpPortPriority_Object=MibTableColumn
pagpPortPriority=_PagpPortPriority_Object((1,3,6,1,4,1,9,9,98,1,1,1,1,6),_PagpPortPriority_Type())
pagpPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:pagpPortPriority.setStatus(_B)
_PagpLearnMethod_Type=PagpLearnMethod
_PagpLearnMethod_Object=MibTableColumn
pagpLearnMethod=_PagpLearnMethod_Object((1,3,6,1,4,1,9,9,98,1,1,1,1,7),_PagpLearnMethod_Type())
pagpLearnMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:pagpLearnMethod.setStatus(_B)
_PagpGroupIfIndex_Type=InterfaceIndexOrZero
_PagpGroupIfIndex_Object=MibTableColumn
pagpGroupIfIndex=_PagpGroupIfIndex_Object((1,3,6,1,4,1,9,9,98,1,1,1,1,8),_PagpGroupIfIndex_Type())
pagpGroupIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpGroupIfIndex.setStatus(_B)
class _PagpDistributionProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ip',1),('mac',2),('port',3),('vlanIpPort',4),('vlanIp',5),('ipPort',6)))
_PagpDistributionProtocol_Type.__name__=_E
_PagpDistributionProtocol_Object=MibTableColumn
pagpDistributionProtocol=_PagpDistributionProtocol_Object((1,3,6,1,4,1,9,9,98,1,1,1,1,9),_PagpDistributionProtocol_Type())
pagpDistributionProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:pagpDistributionProtocol.setStatus(_B)
class _PagpDistributionAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('source',1),('destination',2),('both',3)))
_PagpDistributionAddress_Type.__name__=_E
_PagpDistributionAddress_Object=MibTableColumn
pagpDistributionAddress=_PagpDistributionAddress_Object((1,3,6,1,4,1,9,9,98,1,1,1,1,10),_PagpDistributionAddress_Type())
pagpDistributionAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:pagpDistributionAddress.setStatus(_B)
class _PagpRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fast',1),('normal',2)))
_PagpRate_Type.__name__=_E
_PagpRate_Object=MibTableColumn
pagpRate=_PagpRate_Object((1,3,6,1,4,1,9,9,98,1,1,1,1,11),_PagpRate_Type())
pagpRate.setMaxAccess(_D)
if mibBuilder.loadTexts:pagpRate.setStatus(_B)
class _PagpInPacketTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_PagpInPacketTimeout_Type.__name__=_S
_PagpInPacketTimeout_Object=MibTableColumn
pagpInPacketTimeout=_PagpInPacketTimeout_Object((1,3,6,1,4,1,9,9,98,1,1,1,1,12),_PagpInPacketTimeout_Type())
pagpInPacketTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:pagpInPacketTimeout.setStatus(_B)
if mibBuilder.loadTexts:pagpInPacketTimeout.setUnits('Seconds')
_PagpProtocol_ObjectIdentity=ObjectIdentity
pagpProtocol=_PagpProtocol_ObjectIdentity((1,3,6,1,4,1,9,9,98,1,2))
_PagpProtocolConfigTable_Object=MibTable
pagpProtocolConfigTable=_PagpProtocolConfigTable_Object((1,3,6,1,4,1,9,9,98,1,2,1))
if mibBuilder.loadTexts:pagpProtocolConfigTable.setStatus(_B)
_PagpProtocolConfigEntry_Object=MibTableRow
pagpProtocolConfigEntry=_PagpProtocolConfigEntry_Object((1,3,6,1,4,1,9,9,98,1,2,1,1))
pagpProtocolConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:pagpProtocolConfigEntry.setStatus(_B)
_PagpOperationMode_Type=PagpOperationMode
_PagpOperationMode_Object=MibTableColumn
pagpOperationMode=_PagpOperationMode_Object((1,3,6,1,4,1,9,9,98,1,2,1,1,1),_PagpOperationMode_Type())
pagpOperationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pagpOperationMode.setStatus(_B)
class _PagpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('portDown',1),('portUp',2),('dataReceived',3),('upData',4),('pagpReceived',5),('biDirectional',6),('upPagp',7),('upMult',8)))
_PagpPortState_Type.__name__=_E
_PagpPortState_Object=MibTableColumn
pagpPortState=_PagpPortState_Object((1,3,6,1,4,1,9,9,98,1,2,1,1,2),_PagpPortState_Type())
pagpPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpPortState.setStatus(_B)
_PagpLastStateChange_Type=TimeStamp
_PagpLastStateChange_Object=MibTableColumn
pagpLastStateChange=_PagpLastStateChange_Object((1,3,6,1,4,1,9,9,98,1,2,1,1,3),_PagpLastStateChange_Type())
pagpLastStateChange.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpLastStateChange.setStatus(_B)
class _PagpHelloFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fast',1),('slow',2)))
_PagpHelloFrequency_Type.__name__=_E
_PagpHelloFrequency_Object=MibTableColumn
pagpHelloFrequency=_PagpHelloFrequency_Object((1,3,6,1,4,1,9,9,98,1,2,1,1,4),_PagpHelloFrequency_Type())
pagpHelloFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpHelloFrequency.setStatus(_B)
_PagpDistributionAlgorithm_Type=DisplayString
_PagpDistributionAlgorithm_Object=MibTableColumn
pagpDistributionAlgorithm=_PagpDistributionAlgorithm_Object((1,3,6,1,4,1,9,9,98,1,2,1,1,5),_PagpDistributionAlgorithm_Type())
pagpDistributionAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpDistributionAlgorithm.setStatus(_B)
class _PagpPartnerCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('one',2),('many',3)))
_PagpPartnerCount_Type.__name__=_E
_PagpPartnerCount_Object=MibTableColumn
pagpPartnerCount=_PagpPartnerCount_Object((1,3,6,1,4,1,9,9,98,1,2,1,1,6),_PagpPartnerCount_Type())
pagpPartnerCount.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpPartnerCount.setStatus(_B)
_PagpPartnerDeviceId_Type=MacAddress
_PagpPartnerDeviceId_Object=MibTableColumn
pagpPartnerDeviceId=_PagpPartnerDeviceId_Object((1,3,6,1,4,1,9,9,98,1,2,1,1,7),_PagpPartnerDeviceId_Type())
pagpPartnerDeviceId.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpPartnerDeviceId.setStatus(_B)
_PagpPartnerLearnMethod_Type=PagpLearnMethod
_PagpPartnerLearnMethod_Object=MibTableColumn
pagpPartnerLearnMethod=_PagpPartnerLearnMethod_Object((1,3,6,1,4,1,9,9,98,1,2,1,1,8),_PagpPartnerLearnMethod_Type())
pagpPartnerLearnMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpPartnerLearnMethod.setStatus(_B)
_PagpPartnerPortPriority_Type=PagpPortPriority
_PagpPartnerPortPriority_Object=MibTableColumn
pagpPartnerPortPriority=_PagpPartnerPortPriority_Object((1,3,6,1,4,1,9,9,98,1,2,1,1,9),_PagpPartnerPortPriority_Type())
pagpPartnerPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpPartnerPortPriority.setStatus(_B)
_PagpPartnerIfIndex_Type=InterfaceIndexOrZero
_PagpPartnerIfIndex_Object=MibTableColumn
pagpPartnerIfIndex=_PagpPartnerIfIndex_Object((1,3,6,1,4,1,9,9,98,1,2,1,1,10),_PagpPartnerIfIndex_Type())
pagpPartnerIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpPartnerIfIndex.setStatus(_B)
_PagpPartnerGroupCapability_Type=PagpGroupCapability
_PagpPartnerGroupCapability_Object=MibTableColumn
pagpPartnerGroupCapability=_PagpPartnerGroupCapability_Object((1,3,6,1,4,1,9,9,98,1,2,1,1,11),_PagpPartnerGroupCapability_Type())
pagpPartnerGroupCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpPartnerGroupCapability.setStatus(_B)
_PagpPartnerGroupIfIndex_Type=InterfaceIndexOrZero
_PagpPartnerGroupIfIndex_Object=MibTableColumn
pagpPartnerGroupIfIndex=_PagpPartnerGroupIfIndex_Object((1,3,6,1,4,1,9,9,98,1,2,1,1,12),_PagpPartnerGroupIfIndex_Type())
pagpPartnerGroupIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpPartnerGroupIfIndex.setStatus(_B)
_PagpPartnerDeviceName_Type=DisplayString
_PagpPartnerDeviceName_Object=MibTableColumn
pagpPartnerDeviceName=_PagpPartnerDeviceName_Object((1,3,6,1,4,1,9,9,98,1,2,1,1,13),_PagpPartnerDeviceName_Type())
pagpPartnerDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpPartnerDeviceName.setStatus(_B)
_PagpPartnerPortName_Type=DisplayString
_PagpPartnerPortName_Object=MibTableColumn
pagpPartnerPortName=_PagpPartnerPortName_Object((1,3,6,1,4,1,9,9,98,1,2,1,1,14),_PagpPartnerPortName_Type())
pagpPartnerPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpPartnerPortName.setStatus(_B)
_PagpPartnerAgportMACAddress_Type=MacAddress
_PagpPartnerAgportMACAddress_Object=MibTableColumn
pagpPartnerAgportMACAddress=_PagpPartnerAgportMACAddress_Object((1,3,6,1,4,1,9,9,98,1,2,1,1,15),_PagpPartnerAgportMACAddress_Type())
pagpPartnerAgportMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpPartnerAgportMACAddress.setStatus(_B)
_PagpProtocolStatsTable_Object=MibTable
pagpProtocolStatsTable=_PagpProtocolStatsTable_Object((1,3,6,1,4,1,9,9,98,1,2,2))
if mibBuilder.loadTexts:pagpProtocolStatsTable.setStatus(_B)
_PagpProtocolStatsEntry_Object=MibTableRow
pagpProtocolStatsEntry=_PagpProtocolStatsEntry_Object((1,3,6,1,4,1,9,9,98,1,2,2,1))
pagpProtocolStatsEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:pagpProtocolStatsEntry.setStatus(_B)
_PagpInPackets_Type=Counter32
_PagpInPackets_Object=MibTableColumn
pagpInPackets=_PagpInPackets_Object((1,3,6,1,4,1,9,9,98,1,2,2,1,3),_PagpInPackets_Type())
pagpInPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpInPackets.setStatus(_B)
if mibBuilder.loadTexts:pagpInPackets.setUnits(_F)
_PagpOutPackets_Type=Counter32
_PagpOutPackets_Object=MibTableColumn
pagpOutPackets=_PagpOutPackets_Object((1,3,6,1,4,1,9,9,98,1,2,2,1,4),_PagpOutPackets_Type())
pagpOutPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpOutPackets.setStatus(_B)
if mibBuilder.loadTexts:pagpOutPackets.setUnits(_F)
_PagpInFlushes_Type=Counter32
_PagpInFlushes_Object=MibTableColumn
pagpInFlushes=_PagpInFlushes_Object((1,3,6,1,4,1,9,9,98,1,2,2,1,5),_PagpInFlushes_Type())
pagpInFlushes.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpInFlushes.setStatus(_B)
if mibBuilder.loadTexts:pagpInFlushes.setUnits(_F)
_PagpReturnedFlushes_Type=Counter32
_PagpReturnedFlushes_Object=MibTableColumn
pagpReturnedFlushes=_PagpReturnedFlushes_Object((1,3,6,1,4,1,9,9,98,1,2,2,1,6),_PagpReturnedFlushes_Type())
pagpReturnedFlushes.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpReturnedFlushes.setStatus(_B)
if mibBuilder.loadTexts:pagpReturnedFlushes.setUnits(_F)
_PagpOutFlushes_Type=Counter32
_PagpOutFlushes_Object=MibTableColumn
pagpOutFlushes=_PagpOutFlushes_Object((1,3,6,1,4,1,9,9,98,1,2,2,1,7),_PagpOutFlushes_Type())
pagpOutFlushes.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpOutFlushes.setStatus(_B)
if mibBuilder.loadTexts:pagpOutFlushes.setUnits(_F)
_PagpInErrors_Type=Counter32
_PagpInErrors_Object=MibTableColumn
pagpInErrors=_PagpInErrors_Object((1,3,6,1,4,1,9,9,98,1,2,2,1,8),_PagpInErrors_Type())
pagpInErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:pagpInErrors.setStatus(_B)
if mibBuilder.loadTexts:pagpInErrors.setUnits(_F)
_CiscoPagpMIBConformance_ObjectIdentity=ObjectIdentity
ciscoPagpMIBConformance=_CiscoPagpMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,98,3))
_CiscoPagpMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoPagpMIBCompliances=_CiscoPagpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,98,3,1))
_CiscoPagpMIBGroups_ObjectIdentity=ObjectIdentity
ciscoPagpMIBGroups=_CiscoPagpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,98,3,2))
ciscoPagpEthcGroupV1R1=ObjectGroup((1,3,6,1,4,1,9,9,98,3,2,1))
ciscoPagpEthcGroupV1R1.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciscoPagpEthcGroupV1R1.setStatus(_T)
ciscoPagpPagpGroupV1R1=ObjectGroup((1,3,6,1,4,1,9,9,98,3,2,2))
ciscoPagpPagpGroupV1R1.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:ciscoPagpPagpGroupV1R1.setStatus(_B)
ciscoPagpEthcGroupV2R2=ObjectGroup((1,3,6,1,4,1,9,9,98,3,2,3))
ciscoPagpEthcGroupV2R2.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:ciscoPagpEthcGroupV2R2.setStatus(_B)
ciscoPagpRateAndTimeOutGroup=ObjectGroup((1,3,6,1,4,1,9,9,98,3,2,4))
ciscoPagpRateAndTimeOutGroup.setObjects(*((_A,_r),(_A,_s)))
if mibBuilder.loadTexts:ciscoPagpRateAndTimeOutGroup.setStatus(_B)
ciscoPagpMIBComplianceV1R1=ModuleCompliance((1,3,6,1,4,1,9,9,98,3,1,1))
ciscoPagpMIBComplianceV1R1.setObjects(*((_A,_t),(_A,_I)))
if mibBuilder.loadTexts:ciscoPagpMIBComplianceV1R1.setStatus(_T)
ciscoPagpMIBComplianceV2R2=ModuleCompliance((1,3,6,1,4,1,9,9,98,3,1,2))
ciscoPagpMIBComplianceV2R2.setObjects(*((_A,_R),(_A,_I)))
if mibBuilder.loadTexts:ciscoPagpMIBComplianceV2R2.setStatus('deprecated')
ciscoPagpMIBComplianceV3R3=ModuleCompliance((1,3,6,1,4,1,9,9,98,3,1,3))
ciscoPagpMIBComplianceV3R3.setObjects(*((_A,_R),(_A,_I),(_A,_u)))
if mibBuilder.loadTexts:ciscoPagpMIBComplianceV3R3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'PagpGroupCapability':PagpGroupCapability,'PagpEthcOperationMode':PagpEthcOperationMode,'PagpPortPriority':PagpPortPriority,'PagpOperationMode':PagpOperationMode,'PagpLearnMethod':PagpLearnMethod,'ciscoPagpMIB':ciscoPagpMIB,'ciscoPagpMIBObjects':ciscoPagpMIBObjects,'pagpGroupCapabilityConfiguration':pagpGroupCapabilityConfiguration,'pagpEtherChannelTable':pagpEtherChannelTable,'pagpEtherChannelEntry':pagpEtherChannelEntry,_J:pagpEthcOperationMode,_K:pagpDeviceId,_L:pagpPhysGroupCapability,_M:pagpOperGroupCapability,_N:pagpAdminGroupCapability,_O:pagpPortPriority,_P:pagpLearnMethod,_Q:pagpGroupIfIndex,_p:pagpDistributionProtocol,_q:pagpDistributionAddress,_r:pagpRate,_s:pagpInPacketTimeout,'pagpProtocol':pagpProtocol,'pagpProtocolConfigTable':pagpProtocolConfigTable,'pagpProtocolConfigEntry':pagpProtocolConfigEntry,_U:pagpOperationMode,_V:pagpPortState,_W:pagpLastStateChange,_X:pagpHelloFrequency,_Y:pagpDistributionAlgorithm,_Z:pagpPartnerCount,_a:pagpPartnerDeviceId,_b:pagpPartnerLearnMethod,_c:pagpPartnerPortPriority,_d:pagpPartnerIfIndex,_e:pagpPartnerGroupCapability,_f:pagpPartnerGroupIfIndex,_g:pagpPartnerDeviceName,_h:pagpPartnerPortName,_i:pagpPartnerAgportMACAddress,'pagpProtocolStatsTable':pagpProtocolStatsTable,'pagpProtocolStatsEntry':pagpProtocolStatsEntry,_j:pagpInPackets,_k:pagpOutPackets,_l:pagpInFlushes,_m:pagpReturnedFlushes,_n:pagpOutFlushes,_o:pagpInErrors,'ciscoPagpMIBConformance':ciscoPagpMIBConformance,'ciscoPagpMIBCompliances':ciscoPagpMIBCompliances,'ciscoPagpMIBComplianceV1R1':ciscoPagpMIBComplianceV1R1,'ciscoPagpMIBComplianceV2R2':ciscoPagpMIBComplianceV2R2,'ciscoPagpMIBComplianceV3R3':ciscoPagpMIBComplianceV3R3,'ciscoPagpMIBGroups':ciscoPagpMIBGroups,_t:ciscoPagpEthcGroupV1R1,_I:ciscoPagpPagpGroupV1R1,_R:ciscoPagpEthcGroupV2R2,_u:ciscoPagpRateAndTimeOutGroup})