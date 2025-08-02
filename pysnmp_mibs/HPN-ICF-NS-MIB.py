_Q='hpnicfNSSlot'
_P='hpnicfNSDestSlot'
_O='hpnicfNSSourceIfIndex'
_N='hpnicfNSSourceSlot'
_M='hpnicfNSExportSlot'
_L='hpnicfNSExportType'
_K='disabled'
_J='enabled'
_I='hpnicfNSAggregationType'
_H='hpnicfNSProcessSlot'
_G='read-create'
_F='not-accessible'
_E='HPN-ICF-NS-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfNS=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,20))
if mibBuilder.loadTexts:hpnicfNS.setRevisions(('2004-09-21 14:15',))
_HpnicfNSMibObjects_ObjectIdentity=ObjectIdentity
hpnicfNSMibObjects=_HpnicfNSMibObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,20,1))
_HpnicfNSMibScalarObjects_ObjectIdentity=ObjectIdentity
hpnicfNSMibScalarObjects=_HpnicfNSMibScalarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,20,1,1))
class _HpnicfNSActiveTime_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_HpnicfNSActiveTime_Type.__name__=_B
_HpnicfNSActiveTime_Object=MibScalar
hpnicfNSActiveTime=_HpnicfNSActiveTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,1,1),_HpnicfNSActiveTime_Type())
hpnicfNSActiveTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNSActiveTime.setStatus(_A)
class _HpnicfNSInactiveTime_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_HpnicfNSInactiveTime_Type.__name__=_B
_HpnicfNSInactiveTime_Object=MibScalar
hpnicfNSInactiveTime=_HpnicfNSInactiveTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,1,2),_HpnicfNSInactiveTime_Type())
hpnicfNSInactiveTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNSInactiveTime.setStatus(_A)
class _HpnicfNSVersion_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,5),ValueRangeConstraint(9,9))
_HpnicfNSVersion_Type.__name__=_B
_HpnicfNSVersion_Object=MibScalar
hpnicfNSVersion=_HpnicfNSVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,1,3),_HpnicfNSVersion_Type())
hpnicfNSVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNSVersion.setStatus(_A)
class _HpnicfNSAsType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('peerAs',1),('originAs',2)))
_HpnicfNSAsType_Type.__name__=_B
_HpnicfNSAsType_Object=MibScalar
hpnicfNSAsType=_HpnicfNSAsType_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,1,4),_HpnicfNSAsType_Type())
hpnicfNSAsType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNSAsType.setStatus(_A)
class _HpnicfNSTemplateRefreshRate_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_HpnicfNSTemplateRefreshRate_Type.__name__=_B
_HpnicfNSTemplateRefreshRate_Object=MibScalar
hpnicfNSTemplateRefreshRate=_HpnicfNSTemplateRefreshRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,1,5),_HpnicfNSTemplateRefreshRate_Type())
hpnicfNSTemplateRefreshRate.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNSTemplateRefreshRate.setStatus(_A)
class _HpnicfNSTemplateTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_HpnicfNSTemplateTimeout_Type.__name__=_B
_HpnicfNSTemplateTimeout_Object=MibScalar
hpnicfNSTemplateTimeout=_HpnicfNSTemplateTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,1,6),_HpnicfNSTemplateTimeout_Type())
hpnicfNSTemplateTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNSTemplateTimeout.setStatus(_A)
class _HpnicfNSExportVlanOrIfIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlanId',1),('interfaceIndex',2)))
_HpnicfNSExportVlanOrIfIndex_Type.__name__=_B
_HpnicfNSExportVlanOrIfIndex_Object=MibScalar
hpnicfNSExportVlanOrIfIndex=_HpnicfNSExportVlanOrIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,1,7),_HpnicfNSExportVlanOrIfIndex_Type())
hpnicfNSExportVlanOrIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNSExportVlanOrIfIndex.setStatus(_A)
_HpnicfNSProcessSlotTable_Object=MibTable
hpnicfNSProcessSlotTable=_HpnicfNSProcessSlotTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,2))
if mibBuilder.loadTexts:hpnicfNSProcessSlotTable.setStatus(_A)
_HpnicfNSProcessSlotEntry_Object=MibTableRow
hpnicfNSProcessSlotEntry=_HpnicfNSProcessSlotEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,2,1))
hpnicfNSProcessSlotEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:hpnicfNSProcessSlotEntry.setStatus(_A)
_HpnicfNSProcessSlot_Type=Integer32
_HpnicfNSProcessSlot_Object=MibTableColumn
hpnicfNSProcessSlot=_HpnicfNSProcessSlot_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,2,1,1),_HpnicfNSProcessSlot_Type())
hpnicfNSProcessSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNSProcessSlot.setStatus(_A)
_HpnicfNSExportConfigTable_Object=MibTable
hpnicfNSExportConfigTable=_HpnicfNSExportConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,3))
if mibBuilder.loadTexts:hpnicfNSExportConfigTable.setStatus(_A)
_HpnicfNSExportConfigEntry_Object=MibTableRow
hpnicfNSExportConfigEntry=_HpnicfNSExportConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,3,1))
hpnicfNSExportConfigEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:hpnicfNSExportConfigEntry.setStatus(_A)
class _HpnicfNSAggregationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('v5Statistics',1),('as',2),('destinationPrefix',3),('sourcePrefix',4),('protocolPort',5),('prefix',6),('tosAs',7),('tosDestinationPrefix',8),('tosSourcePrefix',9),('tosProtocolPort',10),('tosPrefix',11),('prefixPort',12)))
_HpnicfNSAggregationType_Type.__name__=_B
_HpnicfNSAggregationType_Object=MibTableColumn
hpnicfNSAggregationType=_HpnicfNSAggregationType_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,3,1,1),_HpnicfNSAggregationType_Type())
hpnicfNSAggregationType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNSAggregationType.setStatus(_A)
_HpnicfNSHostIPAddr_Type=IpAddress
_HpnicfNSHostIPAddr_Object=MibTableColumn
hpnicfNSHostIPAddr=_HpnicfNSHostIPAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,3,1,2),_HpnicfNSHostIPAddr_Type())
hpnicfNSHostIPAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNSHostIPAddr.setStatus(_A)
class _HpnicfNSHostPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfNSHostPort_Type.__name__=_B
_HpnicfNSHostPort_Object=MibTableColumn
hpnicfNSHostPort=_HpnicfNSHostPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,3,1,3),_HpnicfNSHostPort_Type())
hpnicfNSHostPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNSHostPort.setStatus(_A)
_HpnicfNSSrcIpAddr_Type=IpAddress
_HpnicfNSSrcIpAddr_Object=MibTableColumn
hpnicfNSSrcIpAddr=_HpnicfNSSrcIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,3,1,4),_HpnicfNSSrcIpAddr_Type())
hpnicfNSSrcIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNSSrcIpAddr.setStatus(_A)
class _HpnicfNSState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpnicfNSState_Type.__name__=_B
_HpnicfNSState_Object=MibTableColumn
hpnicfNSState=_HpnicfNSState_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,3,1,5),_HpnicfNSState_Type())
hpnicfNSState.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNSState.setStatus(_A)
_HpnicfNSExportInformationTable_Object=MibTable
hpnicfNSExportInformationTable=_HpnicfNSExportInformationTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,4))
if mibBuilder.loadTexts:hpnicfNSExportInformationTable.setStatus(_A)
_HpnicfNSExportInformationEntry_Object=MibTableRow
hpnicfNSExportInformationEntry=_HpnicfNSExportInformationEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,4,1))
hpnicfNSExportInformationEntry.setIndexNames((0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:hpnicfNSExportInformationEntry.setStatus(_A)
class _HpnicfNSExportType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_HpnicfNSExportType_Type.__name__=_B
_HpnicfNSExportType_Object=MibTableColumn
hpnicfNSExportType=_HpnicfNSExportType_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,4,1,1),_HpnicfNSExportType_Type())
hpnicfNSExportType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNSExportType.setStatus(_A)
_HpnicfNSExportSlot_Type=Integer32
_HpnicfNSExportSlot_Object=MibTableColumn
hpnicfNSExportSlot=_HpnicfNSExportSlot_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,4,1,2),_HpnicfNSExportSlot_Type())
hpnicfNSExportSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNSExportSlot.setStatus(_A)
_HpnicfNSExportStream_Type=Counter32
_HpnicfNSExportStream_Object=MibTableColumn
hpnicfNSExportStream=_HpnicfNSExportStream_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,4,1,3),_HpnicfNSExportStream_Type())
hpnicfNSExportStream.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNSExportStream.setStatus(_A)
_HpnicfNSExportNum_Type=Counter32
_HpnicfNSExportNum_Object=MibTableColumn
hpnicfNSExportNum=_HpnicfNSExportNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,4,1,4),_HpnicfNSExportNum_Type())
hpnicfNSExportNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNSExportNum.setStatus(_A)
_HpnicfNSExportFail_Type=Counter32
_HpnicfNSExportFail_Object=MibTableColumn
hpnicfNSExportFail=_HpnicfNSExportFail_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,4,1,5),_HpnicfNSExportFail_Type())
hpnicfNSExportFail.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNSExportFail.setStatus(_A)
_HpnicfNSConfigTable_Object=MibTable
hpnicfNSConfigTable=_HpnicfNSConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,5))
if mibBuilder.loadTexts:hpnicfNSConfigTable.setStatus(_A)
_HpnicfNSConfigEntry_Object=MibTableRow
hpnicfNSConfigEntry=_HpnicfNSConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,5,1))
hpnicfNSConfigEntry.setIndexNames((0,_E,_N),(0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:hpnicfNSConfigEntry.setStatus(_A)
class _HpnicfNSSourceSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfNSSourceSlot_Type.__name__=_B
_HpnicfNSSourceSlot_Object=MibTableColumn
hpnicfNSSourceSlot=_HpnicfNSSourceSlot_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,5,1,1),_HpnicfNSSourceSlot_Type())
hpnicfNSSourceSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNSSourceSlot.setStatus(_A)
_HpnicfNSSourceIfIndex_Type=Integer32
_HpnicfNSSourceIfIndex_Object=MibTableColumn
hpnicfNSSourceIfIndex=_HpnicfNSSourceIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,5,1,2),_HpnicfNSSourceIfIndex_Type())
hpnicfNSSourceIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNSSourceIfIndex.setStatus(_A)
_HpnicfNSDestSlot_Type=Integer32
_HpnicfNSDestSlot_Object=MibTableColumn
hpnicfNSDestSlot=_HpnicfNSDestSlot_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,5,1,3),_HpnicfNSDestSlot_Type())
hpnicfNSDestSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNSDestSlot.setStatus(_A)
class _HpnicfNSDirect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inbound',1),('outbound',2)))
_HpnicfNSDirect_Type.__name__=_B
_HpnicfNSDirect_Object=MibTableColumn
hpnicfNSDirect=_HpnicfNSDirect_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,5,1,4),_HpnicfNSDirect_Type())
hpnicfNSDirect.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNSDirect.setStatus(_A)
class _HpnicfNSACLNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999))
_HpnicfNSACLNumber_Type.__name__=_B
_HpnicfNSACLNumber_Object=MibTableColumn
hpnicfNSACLNumber=_HpnicfNSACLNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,5,1,5),_HpnicfNSACLNumber_Type())
hpnicfNSACLNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNSACLNumber.setStatus(_A)
_HpnicfNSACLName_Type=OctetString
_HpnicfNSACLName_Object=MibTableColumn
hpnicfNSACLName=_HpnicfNSACLName_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,5,1,6),_HpnicfNSACLName_Type())
hpnicfNSACLName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNSACLName.setStatus(_A)
_HpnicfNSACLRule_Type=Integer32
_HpnicfNSACLRule_Object=MibTableColumn
hpnicfNSACLRule=_HpnicfNSACLRule_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,5,1,7),_HpnicfNSACLRule_Type())
hpnicfNSACLRule.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNSACLRule.setStatus(_A)
_HpnicfNSConfigRowStatus_Type=RowStatus
_HpnicfNSConfigRowStatus_Object=MibTableColumn
hpnicfNSConfigRowStatus=_HpnicfNSConfigRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,5,1,8),_HpnicfNSConfigRowStatus_Type())
hpnicfNSConfigRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNSConfigRowStatus.setStatus(_A)
_HpnicfNSStatusTable_Object=MibTable
hpnicfNSStatusTable=_HpnicfNSStatusTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,6))
if mibBuilder.loadTexts:hpnicfNSStatusTable.setStatus(_A)
_HpnicfNSStatusEntry_Object=MibTableRow
hpnicfNSStatusEntry=_HpnicfNSStatusEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,6,1))
hpnicfNSStatusEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:hpnicfNSStatusEntry.setStatus(_A)
_HpnicfNSSlot_Type=Integer32
_HpnicfNSSlot_Object=MibTableColumn
hpnicfNSSlot=_HpnicfNSSlot_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,6,1,1),_HpnicfNSSlot_Type())
hpnicfNSSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNSSlot.setStatus(_A)
_HpnicfNSActiveStreamNumber_Type=Counter32
_HpnicfNSActiveStreamNumber_Object=MibTableColumn
hpnicfNSActiveStreamNumber=_HpnicfNSActiveStreamNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,6,1,2),_HpnicfNSActiveStreamNumber_Type())
hpnicfNSActiveStreamNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNSActiveStreamNumber.setStatus(_A)
_HpnicfNSTotalStreamNumber_Type=Counter32
_HpnicfNSTotalStreamNumber_Object=MibTableColumn
hpnicfNSTotalStreamNumber=_HpnicfNSTotalStreamNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,6,1,3),_HpnicfNSTotalStreamNumber_Type())
hpnicfNSTotalStreamNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNSTotalStreamNumber.setStatus(_A)
_HpnicfNSTotalPacketNumber_Type=Counter32
_HpnicfNSTotalPacketNumber_Object=MibTableColumn
hpnicfNSTotalPacketNumber=_HpnicfNSTotalPacketNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,6,1,4),_HpnicfNSTotalPacketNumber_Type())
hpnicfNSTotalPacketNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNSTotalPacketNumber.setStatus(_A)
_HpnicfNSTotalOctetNumber_Type=Counter32
_HpnicfNSTotalOctetNumber_Object=MibTableColumn
hpnicfNSTotalOctetNumber=_HpnicfNSTotalOctetNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,6,1,5),_HpnicfNSTotalOctetNumber_Type())
hpnicfNSTotalOctetNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNSTotalOctetNumber.setStatus(_A)
_HpnicfNSMPLSActiveStreamNumber_Type=Counter32
_HpnicfNSMPLSActiveStreamNumber_Object=MibTableColumn
hpnicfNSMPLSActiveStreamNumber=_HpnicfNSMPLSActiveStreamNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,6,1,6),_HpnicfNSMPLSActiveStreamNumber_Type())
hpnicfNSMPLSActiveStreamNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNSMPLSActiveStreamNumber.setStatus(_A)
_HpnicfNSMPLSTotalStreamNumber_Type=Counter32
_HpnicfNSMPLSTotalStreamNumber_Object=MibTableColumn
hpnicfNSMPLSTotalStreamNumber=_HpnicfNSMPLSTotalStreamNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,6,1,7),_HpnicfNSMPLSTotalStreamNumber_Type())
hpnicfNSMPLSTotalStreamNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNSMPLSTotalStreamNumber.setStatus(_A)
_HpnicfNSMPLSTotalPacketNumber_Type=Counter32
_HpnicfNSMPLSTotalPacketNumber_Object=MibTableColumn
hpnicfNSMPLSTotalPacketNumber=_HpnicfNSMPLSTotalPacketNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,6,1,8),_HpnicfNSMPLSTotalPacketNumber_Type())
hpnicfNSMPLSTotalPacketNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNSMPLSTotalPacketNumber.setStatus(_A)
_HpnicfNSMPLSTotalOctetNumber_Type=Counter32
_HpnicfNSMPLSTotalOctetNumber_Object=MibTableColumn
hpnicfNSMPLSTotalOctetNumber=_HpnicfNSMPLSTotalOctetNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,6,1,9),_HpnicfNSMPLSTotalOctetNumber_Type())
hpnicfNSMPLSTotalOctetNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNSMPLSTotalOctetNumber.setStatus(_A)
class _HpnicfNSResetFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpnicfNSResetFlag_Type.__name__=_B
_HpnicfNSResetFlag_Object=MibTableColumn
hpnicfNSResetFlag=_HpnicfNSResetFlag_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,6,1,10),_HpnicfNSResetFlag_Type())
hpnicfNSResetFlag.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNSResetFlag.setStatus(_A)
_HpnicfNSResetTime_Type=TimeTicks
_HpnicfNSResetTime_Object=MibTableColumn
hpnicfNSResetTime=_HpnicfNSResetTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,20,1,6,1,11),_HpnicfNSResetTime_Type())
hpnicfNSResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNSResetTime.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hpnicfNS':hpnicfNS,'hpnicfNSMibObjects':hpnicfNSMibObjects,'hpnicfNSMibScalarObjects':hpnicfNSMibScalarObjects,'hpnicfNSActiveTime':hpnicfNSActiveTime,'hpnicfNSInactiveTime':hpnicfNSInactiveTime,'hpnicfNSVersion':hpnicfNSVersion,'hpnicfNSAsType':hpnicfNSAsType,'hpnicfNSTemplateRefreshRate':hpnicfNSTemplateRefreshRate,'hpnicfNSTemplateTimeout':hpnicfNSTemplateTimeout,'hpnicfNSExportVlanOrIfIndex':hpnicfNSExportVlanOrIfIndex,'hpnicfNSProcessSlotTable':hpnicfNSProcessSlotTable,'hpnicfNSProcessSlotEntry':hpnicfNSProcessSlotEntry,_H:hpnicfNSProcessSlot,'hpnicfNSExportConfigTable':hpnicfNSExportConfigTable,'hpnicfNSExportConfigEntry':hpnicfNSExportConfigEntry,_I:hpnicfNSAggregationType,'hpnicfNSHostIPAddr':hpnicfNSHostIPAddr,'hpnicfNSHostPort':hpnicfNSHostPort,'hpnicfNSSrcIpAddr':hpnicfNSSrcIpAddr,'hpnicfNSState':hpnicfNSState,'hpnicfNSExportInformationTable':hpnicfNSExportInformationTable,'hpnicfNSExportInformationEntry':hpnicfNSExportInformationEntry,_L:hpnicfNSExportType,_M:hpnicfNSExportSlot,'hpnicfNSExportStream':hpnicfNSExportStream,'hpnicfNSExportNum':hpnicfNSExportNum,'hpnicfNSExportFail':hpnicfNSExportFail,'hpnicfNSConfigTable':hpnicfNSConfigTable,'hpnicfNSConfigEntry':hpnicfNSConfigEntry,_N:hpnicfNSSourceSlot,_O:hpnicfNSSourceIfIndex,_P:hpnicfNSDestSlot,'hpnicfNSDirect':hpnicfNSDirect,'hpnicfNSACLNumber':hpnicfNSACLNumber,'hpnicfNSACLName':hpnicfNSACLName,'hpnicfNSACLRule':hpnicfNSACLRule,'hpnicfNSConfigRowStatus':hpnicfNSConfigRowStatus,'hpnicfNSStatusTable':hpnicfNSStatusTable,'hpnicfNSStatusEntry':hpnicfNSStatusEntry,_Q:hpnicfNSSlot,'hpnicfNSActiveStreamNumber':hpnicfNSActiveStreamNumber,'hpnicfNSTotalStreamNumber':hpnicfNSTotalStreamNumber,'hpnicfNSTotalPacketNumber':hpnicfNSTotalPacketNumber,'hpnicfNSTotalOctetNumber':hpnicfNSTotalOctetNumber,'hpnicfNSMPLSActiveStreamNumber':hpnicfNSMPLSActiveStreamNumber,'hpnicfNSMPLSTotalStreamNumber':hpnicfNSMPLSTotalStreamNumber,'hpnicfNSMPLSTotalPacketNumber':hpnicfNSMPLSTotalPacketNumber,'hpnicfNSMPLSTotalOctetNumber':hpnicfNSMPLSTotalOctetNumber,'hpnicfNSResetFlag':hpnicfNSResetFlag,'hpnicfNSResetTime':hpnicfNSResetTime})