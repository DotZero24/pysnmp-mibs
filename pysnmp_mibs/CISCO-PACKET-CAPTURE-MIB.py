_AK='cpcSessionDescrGroup'
_AJ='cpcSessionPacketRateLimitGroup'
_AI='cpcMaxIpFilterConfigGroup'
_AH='cpcMaxMacFilterConfigGroup'
_AG='cpcSessionStatsGroup'
_AF='cpcScheduleConfigGroup'
_AE='cpcBufferConfigGroup'
_AD='cpcAccessGroupFilterConfigGroup'
_AC='cpcVlanFilterConfigGroup'
_AB='cpcEthertypeFilterConfigGroup'
_AA='cpcPacketLengthFilterConfigGroup'
_A9='cpcSessionDescr'
_A8='cpcSessionPacketRateLimit'
_A7='cpcMaxIpFilterAllowed'
_A6='cpcMaxMacFilterAllowed'
_A5='cpcSessionPacketsDropped'
_A4='cpcSessionPacketsCaptured'
_A3='cpcSessionPacketsReceived'
_A2='cpcScheduleCapturePeriod'
_A1='cpcScheduleStartTime'
_A0='cpcBufferOperStatus'
_z='cpcBufferAction'
_y='cpcBufferSize'
_x='cpcBufferType'
_w='cpcAccessGroupFilterStatus'
_v='cpcMaxAccessGroupFilterAllowed'
_u='cpcVlanFilterRowStatus'
_t='cpcMaxVlanFilterAllowed'
_s='cpcEthertypeFilterStatus'
_r='cpcMaxEthertypeFilterAllowed'
_q='cpcPacketLengthFilterMax'
_p='cpcPacketLengthFilterMin'
_o='cpcSessionDestFileName'
_n='cpcIpFilterRowStatus'
_m='cpcIpFilterMask'
_l='cpcMacFilterRowStatus'
_k='cpcMaxFilterAllowed'
_j='cpcCaptureSourceIfStatus'
_i='cpcCaptureSourceIfDirection'
_h='cpcSessionConfigStatus'
_g='cpcSessionAction'
_f='cpcSessionPacketLimits'
_e='cpcSessionPacketLength'
_d='cpcSessionMaxSources'
_c='cpcSessionOperStatus'
_b='cpcMaxSessionAllowed'
_a='cpcAccessGroupFilterName'
_Z='cpcAccessGroupFilterType'
_Y='cpcVlanFilterVlanIndex'
_X='cpcEthertypeFilterValue'
_W='cpcIpFilterCriteria'
_V='cpcIpFilterAddress'
_U='cpcIpFilterAddressType'
_T='cpcMacFilterCriteria'
_S='cpcMacFilterMacAddress'
_R='InetAddress'
_Q='ifIndex'
_P='IF-MIB'
_O='cpcDestFileNameConfigGroup'
_N='cpcIpFilterConfigGroup'
_M='cpcMacFilterConfigGroup'
_L='cpcFilterConfigGroup'
_K='cpcGenericConfigGroup'
_J='SnmpAdminString'
_I='Unsigned32'
_H='read-write'
_G='Integer32'
_F='not-accessible'
_E='cpcSessionId'
_D='read-only'
_C='read-create'
_B='CISCO-PACKET-CAPTURE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
VlanIndex,=mibBuilder.importSymbols('CISCO-VTP-MIB','VlanIndex')
ifIndex,=mibBuilder.importSymbols(_P,_Q)
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_R,'InetAddressPrefixLength','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
ciscoPacketCaptureMIB=ModuleIdentity((1,3,6,1,4,1,9,9,602))
if mibBuilder.loadTexts:ciscoPacketCaptureMIB.setRevisions(('2008-07-07 00:00','2007-01-03 00:00'))
class CiscoPacketCaptureFilterCriteria(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('source',1),('dest',2)))
_CpcMIBNotification_ObjectIdentity=ObjectIdentity
cpcMIBNotification=_CpcMIBNotification_ObjectIdentity((1,3,6,1,4,1,9,9,602,0))
_CpcMIBObjects_ObjectIdentity=ObjectIdentity
cpcMIBObjects=_CpcMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,602,1))
_CpcGenericConfig_ObjectIdentity=ObjectIdentity
cpcGenericConfig=_CpcGenericConfig_ObjectIdentity((1,3,6,1,4,1,9,9,602,1,1))
_CpcMaxSessionAllowed_Type=Unsigned32
_CpcMaxSessionAllowed_Object=MibScalar
cpcMaxSessionAllowed=_CpcMaxSessionAllowed_Object((1,3,6,1,4,1,9,9,602,1,1,1),_CpcMaxSessionAllowed_Type())
cpcMaxSessionAllowed.setMaxAccess(_D)
if mibBuilder.loadTexts:cpcMaxSessionAllowed.setStatus(_A)
_CpcSessionConfigTable_Object=MibTable
cpcSessionConfigTable=_CpcSessionConfigTable_Object((1,3,6,1,4,1,9,9,602,1,1,2))
if mibBuilder.loadTexts:cpcSessionConfigTable.setStatus(_A)
_CpcSessionConfigEntry_Object=MibTableRow
cpcSessionConfigEntry=_CpcSessionConfigEntry_Object((1,3,6,1,4,1,9,9,602,1,1,2,1))
cpcSessionConfigEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cpcSessionConfigEntry.setStatus(_A)
class _CpcSessionId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CpcSessionId_Type.__name__=_I
_CpcSessionId_Object=MibTableColumn
cpcSessionId=_CpcSessionId_Object((1,3,6,1,4,1,9,9,602,1,1,2,1,1),_CpcSessionId_Type())
cpcSessionId.setMaxAccess(_F)
if mibBuilder.loadTexts:cpcSessionId.setStatus(_A)
class _CpcSessionOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('inProgress',2),('completed',3),('stopped',4),('storageFull',5),('bufferFull',6)))
_CpcSessionOperStatus_Type.__name__=_G
_CpcSessionOperStatus_Object=MibTableColumn
cpcSessionOperStatus=_CpcSessionOperStatus_Object((1,3,6,1,4,1,9,9,602,1,1,2,1,2),_CpcSessionOperStatus_Type())
cpcSessionOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cpcSessionOperStatus.setStatus(_A)
_CpcSessionDestFileName_Type=SnmpAdminString
_CpcSessionDestFileName_Object=MibTableColumn
cpcSessionDestFileName=_CpcSessionDestFileName_Object((1,3,6,1,4,1,9,9,602,1,1,2,1,3),_CpcSessionDestFileName_Type())
cpcSessionDestFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpcSessionDestFileName.setStatus(_A)
class _CpcSessionPacketLength_Type(Unsigned32):defaultValue=0
_CpcSessionPacketLength_Type.__name__=_I
_CpcSessionPacketLength_Object=MibTableColumn
cpcSessionPacketLength=_CpcSessionPacketLength_Object((1,3,6,1,4,1,9,9,602,1,1,2,1,4),_CpcSessionPacketLength_Type())
cpcSessionPacketLength.setMaxAccess(_C)
if mibBuilder.loadTexts:cpcSessionPacketLength.setStatus(_A)
if mibBuilder.loadTexts:cpcSessionPacketLength.setUnits('octets')
class _CpcSessionPacketLimits_Type(Unsigned32):defaultValue=0
_CpcSessionPacketLimits_Type.__name__=_I
_CpcSessionPacketLimits_Object=MibTableColumn
cpcSessionPacketLimits=_CpcSessionPacketLimits_Object((1,3,6,1,4,1,9,9,602,1,1,2,1,5),_CpcSessionPacketLimits_Type())
cpcSessionPacketLimits.setMaxAccess(_C)
if mibBuilder.loadTexts:cpcSessionPacketLimits.setStatus(_A)
if mibBuilder.loadTexts:cpcSessionPacketLimits.setUnits('packets')
class _CpcSessionAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_CpcSessionAction_Type.__name__=_G
_CpcSessionAction_Object=MibTableColumn
cpcSessionAction=_CpcSessionAction_Object((1,3,6,1,4,1,9,9,602,1,1,2,1,6),_CpcSessionAction_Type())
cpcSessionAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cpcSessionAction.setStatus(_A)
_CpcSessionConfigStatus_Type=RowStatus
_CpcSessionConfigStatus_Object=MibTableColumn
cpcSessionConfigStatus=_CpcSessionConfigStatus_Object((1,3,6,1,4,1,9,9,602,1,1,2,1,7),_CpcSessionConfigStatus_Type())
cpcSessionConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpcSessionConfigStatus.setStatus(_A)
class _CpcSessionPacketRateLimit_Type(Unsigned32):defaultValue=10000
_CpcSessionPacketRateLimit_Type.__name__=_I
_CpcSessionPacketRateLimit_Object=MibTableColumn
cpcSessionPacketRateLimit=_CpcSessionPacketRateLimit_Object((1,3,6,1,4,1,9,9,602,1,1,2,1,8),_CpcSessionPacketRateLimit_Type())
cpcSessionPacketRateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cpcSessionPacketRateLimit.setStatus(_A)
if mibBuilder.loadTexts:cpcSessionPacketRateLimit.setUnits('packets per second')
class _CpcSessionDescr_Type(SnmpAdminString):defaultValue=OctetString('')
_CpcSessionDescr_Type.__name__=_J
_CpcSessionDescr_Object=MibTableColumn
cpcSessionDescr=_CpcSessionDescr_Object((1,3,6,1,4,1,9,9,602,1,1,2,1,9),_CpcSessionDescr_Type())
cpcSessionDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cpcSessionDescr.setStatus(_A)
_CpcSessionMaxSources_Type=Unsigned32
_CpcSessionMaxSources_Object=MibScalar
cpcSessionMaxSources=_CpcSessionMaxSources_Object((1,3,6,1,4,1,9,9,602,1,1,3),_CpcSessionMaxSources_Type())
cpcSessionMaxSources.setMaxAccess(_D)
if mibBuilder.loadTexts:cpcSessionMaxSources.setStatus(_A)
_CpcCaptureSourceIfTable_Object=MibTable
cpcCaptureSourceIfTable=_CpcCaptureSourceIfTable_Object((1,3,6,1,4,1,9,9,602,1,1,4))
if mibBuilder.loadTexts:cpcCaptureSourceIfTable.setStatus(_A)
_CpcCaptureSourceIfEntry_Object=MibTableRow
cpcCaptureSourceIfEntry=_CpcCaptureSourceIfEntry_Object((1,3,6,1,4,1,9,9,602,1,1,4,1))
cpcCaptureSourceIfEntry.setIndexNames((0,_B,_E),(0,_P,_Q))
if mibBuilder.loadTexts:cpcCaptureSourceIfEntry.setStatus(_A)
class _CpcCaptureSourceIfDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rx',1),('tx',2),('both',3)))
_CpcCaptureSourceIfDirection_Type.__name__=_G
_CpcCaptureSourceIfDirection_Object=MibTableColumn
cpcCaptureSourceIfDirection=_CpcCaptureSourceIfDirection_Object((1,3,6,1,4,1,9,9,602,1,1,4,1,1),_CpcCaptureSourceIfDirection_Type())
cpcCaptureSourceIfDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:cpcCaptureSourceIfDirection.setStatus(_A)
_CpcCaptureSourceIfStatus_Type=RowStatus
_CpcCaptureSourceIfStatus_Object=MibTableColumn
cpcCaptureSourceIfStatus=_CpcCaptureSourceIfStatus_Object((1,3,6,1,4,1,9,9,602,1,1,4,1,2),_CpcCaptureSourceIfStatus_Type())
cpcCaptureSourceIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpcCaptureSourceIfStatus.setStatus(_A)
_CpcFilterConfig_ObjectIdentity=ObjectIdentity
cpcFilterConfig=_CpcFilterConfig_ObjectIdentity((1,3,6,1,4,1,9,9,602,1,2))
_CpcMaxFilterAllowed_Type=Unsigned32
_CpcMaxFilterAllowed_Object=MibScalar
cpcMaxFilterAllowed=_CpcMaxFilterAllowed_Object((1,3,6,1,4,1,9,9,602,1,2,1),_CpcMaxFilterAllowed_Type())
cpcMaxFilterAllowed.setMaxAccess(_D)
if mibBuilder.loadTexts:cpcMaxFilterAllowed.setStatus(_A)
_CpcMacFilterTable_Object=MibTable
cpcMacFilterTable=_CpcMacFilterTable_Object((1,3,6,1,4,1,9,9,602,1,2,2))
if mibBuilder.loadTexts:cpcMacFilterTable.setStatus(_A)
_CpcMacFilterEntry_Object=MibTableRow
cpcMacFilterEntry=_CpcMacFilterEntry_Object((1,3,6,1,4,1,9,9,602,1,2,2,1))
cpcMacFilterEntry.setIndexNames((0,_B,_E),(0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:cpcMacFilterEntry.setStatus(_A)
_CpcMacFilterMacAddress_Type=MacAddress
_CpcMacFilterMacAddress_Object=MibTableColumn
cpcMacFilterMacAddress=_CpcMacFilterMacAddress_Object((1,3,6,1,4,1,9,9,602,1,2,2,1,1),_CpcMacFilterMacAddress_Type())
cpcMacFilterMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:cpcMacFilterMacAddress.setStatus(_A)
_CpcMacFilterCriteria_Type=CiscoPacketCaptureFilterCriteria
_CpcMacFilterCriteria_Object=MibTableColumn
cpcMacFilterCriteria=_CpcMacFilterCriteria_Object((1,3,6,1,4,1,9,9,602,1,2,2,1,2),_CpcMacFilterCriteria_Type())
cpcMacFilterCriteria.setMaxAccess(_F)
if mibBuilder.loadTexts:cpcMacFilterCriteria.setStatus(_A)
_CpcMacFilterRowStatus_Type=RowStatus
_CpcMacFilterRowStatus_Object=MibTableColumn
cpcMacFilterRowStatus=_CpcMacFilterRowStatus_Object((1,3,6,1,4,1,9,9,602,1,2,2,1,3),_CpcMacFilterRowStatus_Type())
cpcMacFilterRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpcMacFilterRowStatus.setStatus(_A)
_CpcIpFilterTable_Object=MibTable
cpcIpFilterTable=_CpcIpFilterTable_Object((1,3,6,1,4,1,9,9,602,1,2,3))
if mibBuilder.loadTexts:cpcIpFilterTable.setStatus(_A)
_CpcIpFilterEntry_Object=MibTableRow
cpcIpFilterEntry=_CpcIpFilterEntry_Object((1,3,6,1,4,1,9,9,602,1,2,3,1))
cpcIpFilterEntry.setIndexNames((0,_B,_E),(0,_B,_U),(0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:cpcIpFilterEntry.setStatus(_A)
_CpcIpFilterAddressType_Type=InetAddressType
_CpcIpFilterAddressType_Object=MibTableColumn
cpcIpFilterAddressType=_CpcIpFilterAddressType_Object((1,3,6,1,4,1,9,9,602,1,2,3,1,1),_CpcIpFilterAddressType_Type())
cpcIpFilterAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:cpcIpFilterAddressType.setStatus(_A)
class _CpcIpFilterAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CpcIpFilterAddress_Type.__name__=_R
_CpcIpFilterAddress_Object=MibTableColumn
cpcIpFilterAddress=_CpcIpFilterAddress_Object((1,3,6,1,4,1,9,9,602,1,2,3,1,2),_CpcIpFilterAddress_Type())
cpcIpFilterAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:cpcIpFilterAddress.setStatus(_A)
_CpcIpFilterCriteria_Type=CiscoPacketCaptureFilterCriteria
_CpcIpFilterCriteria_Object=MibTableColumn
cpcIpFilterCriteria=_CpcIpFilterCriteria_Object((1,3,6,1,4,1,9,9,602,1,2,3,1,3),_CpcIpFilterCriteria_Type())
cpcIpFilterCriteria.setMaxAccess(_F)
if mibBuilder.loadTexts:cpcIpFilterCriteria.setStatus(_A)
_CpcIpFilterMask_Type=InetAddressPrefixLength
_CpcIpFilterMask_Object=MibTableColumn
cpcIpFilterMask=_CpcIpFilterMask_Object((1,3,6,1,4,1,9,9,602,1,2,3,1,4),_CpcIpFilterMask_Type())
cpcIpFilterMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cpcIpFilterMask.setStatus(_A)
_CpcIpFilterRowStatus_Type=RowStatus
_CpcIpFilterRowStatus_Object=MibTableColumn
cpcIpFilterRowStatus=_CpcIpFilterRowStatus_Object((1,3,6,1,4,1,9,9,602,1,2,3,1,5),_CpcIpFilterRowStatus_Type())
cpcIpFilterRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpcIpFilterRowStatus.setStatus(_A)
_CpcMaxMacFilterAllowed_Type=Unsigned32
_CpcMaxMacFilterAllowed_Object=MibScalar
cpcMaxMacFilterAllowed=_CpcMaxMacFilterAllowed_Object((1,3,6,1,4,1,9,9,602,1,2,4),_CpcMaxMacFilterAllowed_Type())
cpcMaxMacFilterAllowed.setMaxAccess(_D)
if mibBuilder.loadTexts:cpcMaxMacFilterAllowed.setStatus(_A)
_CpcMaxIpFilterAllowed_Type=Unsigned32
_CpcMaxIpFilterAllowed_Object=MibScalar
cpcMaxIpFilterAllowed=_CpcMaxIpFilterAllowed_Object((1,3,6,1,4,1,9,9,602,1,2,5),_CpcMaxIpFilterAllowed_Type())
cpcMaxIpFilterAllowed.setMaxAccess(_D)
if mibBuilder.loadTexts:cpcMaxIpFilterAllowed.setStatus(_A)
_CpcPacketLengthFilterTable_Object=MibTable
cpcPacketLengthFilterTable=_CpcPacketLengthFilterTable_Object((1,3,6,1,4,1,9,9,602,1,2,6))
if mibBuilder.loadTexts:cpcPacketLengthFilterTable.setStatus(_A)
_CpcPacketLengthFilterEntry_Object=MibTableRow
cpcPacketLengthFilterEntry=_CpcPacketLengthFilterEntry_Object((1,3,6,1,4,1,9,9,602,1,2,6,1))
cpcPacketLengthFilterEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cpcPacketLengthFilterEntry.setStatus(_A)
_CpcPacketLengthFilterMin_Type=Unsigned32
_CpcPacketLengthFilterMin_Object=MibTableColumn
cpcPacketLengthFilterMin=_CpcPacketLengthFilterMin_Object((1,3,6,1,4,1,9,9,602,1,2,6,1,1),_CpcPacketLengthFilterMin_Type())
cpcPacketLengthFilterMin.setMaxAccess(_H)
if mibBuilder.loadTexts:cpcPacketLengthFilterMin.setStatus(_A)
if mibBuilder.loadTexts:cpcPacketLengthFilterMin.setUnits('bytes')
_CpcPacketLengthFilterMax_Type=Unsigned32
_CpcPacketLengthFilterMax_Object=MibTableColumn
cpcPacketLengthFilterMax=_CpcPacketLengthFilterMax_Object((1,3,6,1,4,1,9,9,602,1,2,6,1,2),_CpcPacketLengthFilterMax_Type())
cpcPacketLengthFilterMax.setMaxAccess(_H)
if mibBuilder.loadTexts:cpcPacketLengthFilterMax.setStatus(_A)
if mibBuilder.loadTexts:cpcPacketLengthFilterMax.setUnits('bytes')
_CpcMaxEthertypeFilterAllowed_Type=Unsigned32
_CpcMaxEthertypeFilterAllowed_Object=MibScalar
cpcMaxEthertypeFilterAllowed=_CpcMaxEthertypeFilterAllowed_Object((1,3,6,1,4,1,9,9,602,1,2,7),_CpcMaxEthertypeFilterAllowed_Type())
cpcMaxEthertypeFilterAllowed.setMaxAccess(_D)
if mibBuilder.loadTexts:cpcMaxEthertypeFilterAllowed.setStatus(_A)
_CpcEthertypeFilterTable_Object=MibTable
cpcEthertypeFilterTable=_CpcEthertypeFilterTable_Object((1,3,6,1,4,1,9,9,602,1,2,8))
if mibBuilder.loadTexts:cpcEthertypeFilterTable.setStatus(_A)
_CpcEthertypeFilterEntry_Object=MibTableRow
cpcEthertypeFilterEntry=_CpcEthertypeFilterEntry_Object((1,3,6,1,4,1,9,9,602,1,2,8,1))
cpcEthertypeFilterEntry.setIndexNames((0,_B,_E),(0,_B,_X))
if mibBuilder.loadTexts:cpcEthertypeFilterEntry.setStatus(_A)
class _CpcEthertypeFilterValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpcEthertypeFilterValue_Type.__name__=_G
_CpcEthertypeFilterValue_Object=MibTableColumn
cpcEthertypeFilterValue=_CpcEthertypeFilterValue_Object((1,3,6,1,4,1,9,9,602,1,2,8,1,1),_CpcEthertypeFilterValue_Type())
cpcEthertypeFilterValue.setMaxAccess(_F)
if mibBuilder.loadTexts:cpcEthertypeFilterValue.setStatus(_A)
_CpcEthertypeFilterStatus_Type=RowStatus
_CpcEthertypeFilterStatus_Object=MibTableColumn
cpcEthertypeFilterStatus=_CpcEthertypeFilterStatus_Object((1,3,6,1,4,1,9,9,602,1,2,8,1,2),_CpcEthertypeFilterStatus_Type())
cpcEthertypeFilterStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpcEthertypeFilterStatus.setStatus(_A)
_CpcMaxVlanFilterAllowed_Type=Unsigned32
_CpcMaxVlanFilterAllowed_Object=MibScalar
cpcMaxVlanFilterAllowed=_CpcMaxVlanFilterAllowed_Object((1,3,6,1,4,1,9,9,602,1,2,9),_CpcMaxVlanFilterAllowed_Type())
cpcMaxVlanFilterAllowed.setMaxAccess(_D)
if mibBuilder.loadTexts:cpcMaxVlanFilterAllowed.setStatus(_A)
_CpcVlanFilterTable_Object=MibTable
cpcVlanFilterTable=_CpcVlanFilterTable_Object((1,3,6,1,4,1,9,9,602,1,2,10))
if mibBuilder.loadTexts:cpcVlanFilterTable.setStatus(_A)
_CpcVlanFilterEntry_Object=MibTableRow
cpcVlanFilterEntry=_CpcVlanFilterEntry_Object((1,3,6,1,4,1,9,9,602,1,2,10,1))
cpcVlanFilterEntry.setIndexNames((0,_B,_E),(0,_B,_Y))
if mibBuilder.loadTexts:cpcVlanFilterEntry.setStatus(_A)
_CpcVlanFilterVlanIndex_Type=VlanIndex
_CpcVlanFilterVlanIndex_Object=MibTableColumn
cpcVlanFilterVlanIndex=_CpcVlanFilterVlanIndex_Object((1,3,6,1,4,1,9,9,602,1,2,10,1,1),_CpcVlanFilterVlanIndex_Type())
cpcVlanFilterVlanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cpcVlanFilterVlanIndex.setStatus(_A)
_CpcVlanFilterRowStatus_Type=RowStatus
_CpcVlanFilterRowStatus_Object=MibTableColumn
cpcVlanFilterRowStatus=_CpcVlanFilterRowStatus_Object((1,3,6,1,4,1,9,9,602,1,2,10,1,2),_CpcVlanFilterRowStatus_Type())
cpcVlanFilterRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpcVlanFilterRowStatus.setStatus(_A)
_CpcMaxAccessGroupFilterAllowed_Type=Unsigned32
_CpcMaxAccessGroupFilterAllowed_Object=MibScalar
cpcMaxAccessGroupFilterAllowed=_CpcMaxAccessGroupFilterAllowed_Object((1,3,6,1,4,1,9,9,602,1,2,11),_CpcMaxAccessGroupFilterAllowed_Type())
cpcMaxAccessGroupFilterAllowed.setMaxAccess(_D)
if mibBuilder.loadTexts:cpcMaxAccessGroupFilterAllowed.setStatus(_A)
_CpcAccessGroupFilterTable_Object=MibTable
cpcAccessGroupFilterTable=_CpcAccessGroupFilterTable_Object((1,3,6,1,4,1,9,9,602,1,2,12))
if mibBuilder.loadTexts:cpcAccessGroupFilterTable.setStatus(_A)
_CpcAccessGroupFilterEntry_Object=MibTableRow
cpcAccessGroupFilterEntry=_CpcAccessGroupFilterEntry_Object((1,3,6,1,4,1,9,9,602,1,2,12,1))
cpcAccessGroupFilterEntry.setIndexNames((0,_B,_E),(0,_B,_Z),(1,_B,_a))
if mibBuilder.loadTexts:cpcAccessGroupFilterEntry.setStatus(_A)
class _CpcAccessGroupFilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hardware',1),('software',2)))
_CpcAccessGroupFilterType_Type.__name__=_G
_CpcAccessGroupFilterType_Object=MibTableColumn
cpcAccessGroupFilterType=_CpcAccessGroupFilterType_Object((1,3,6,1,4,1,9,9,602,1,2,12,1,1),_CpcAccessGroupFilterType_Type())
cpcAccessGroupFilterType.setMaxAccess(_F)
if mibBuilder.loadTexts:cpcAccessGroupFilterType.setStatus(_A)
class _CpcAccessGroupFilterName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,99))
_CpcAccessGroupFilterName_Type.__name__=_J
_CpcAccessGroupFilterName_Object=MibTableColumn
cpcAccessGroupFilterName=_CpcAccessGroupFilterName_Object((1,3,6,1,4,1,9,9,602,1,2,12,1,2),_CpcAccessGroupFilterName_Type())
cpcAccessGroupFilterName.setMaxAccess(_F)
if mibBuilder.loadTexts:cpcAccessGroupFilterName.setStatus(_A)
_CpcAccessGroupFilterStatus_Type=RowStatus
_CpcAccessGroupFilterStatus_Object=MibTableColumn
cpcAccessGroupFilterStatus=_CpcAccessGroupFilterStatus_Object((1,3,6,1,4,1,9,9,602,1,2,12,1,3),_CpcAccessGroupFilterStatus_Type())
cpcAccessGroupFilterStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpcAccessGroupFilterStatus.setStatus(_A)
_CpcBufferConfig_ObjectIdentity=ObjectIdentity
cpcBufferConfig=_CpcBufferConfig_ObjectIdentity((1,3,6,1,4,1,9,9,602,1,3))
_CpcBufferConfigTable_Object=MibTable
cpcBufferConfigTable=_CpcBufferConfigTable_Object((1,3,6,1,4,1,9,9,602,1,3,1))
if mibBuilder.loadTexts:cpcBufferConfigTable.setStatus(_A)
_CpcBufferConfigEntry_Object=MibTableRow
cpcBufferConfigEntry=_CpcBufferConfigEntry_Object((1,3,6,1,4,1,9,9,602,1,3,1,1))
cpcBufferConfigEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cpcBufferConfigEntry.setStatus(_A)
class _CpcBufferType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('linear',1),('circular',2)))
_CpcBufferType_Type.__name__=_G
_CpcBufferType_Object=MibTableColumn
cpcBufferType=_CpcBufferType_Object((1,3,6,1,4,1,9,9,602,1,3,1,1,1),_CpcBufferType_Type())
cpcBufferType.setMaxAccess(_H)
if mibBuilder.loadTexts:cpcBufferType.setStatus(_A)
_CpcBufferSize_Type=Unsigned32
_CpcBufferSize_Object=MibTableColumn
cpcBufferSize=_CpcBufferSize_Object((1,3,6,1,4,1,9,9,602,1,3,1,1,2),_CpcBufferSize_Type())
cpcBufferSize.setMaxAccess(_H)
if mibBuilder.loadTexts:cpcBufferSize.setStatus(_A)
if mibBuilder.loadTexts:cpcBufferSize.setUnits('Kilo-bytes')
class _CpcBufferAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAction',1),('clear',2),('export',3)))
_CpcBufferAction_Type.__name__=_G
_CpcBufferAction_Object=MibTableColumn
cpcBufferAction=_CpcBufferAction_Object((1,3,6,1,4,1,9,9,602,1,3,1,1,3),_CpcBufferAction_Type())
cpcBufferAction.setMaxAccess(_H)
if mibBuilder.loadTexts:cpcBufferAction.setStatus(_A)
class _CpcBufferOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('exporting',2)))
_CpcBufferOperStatus_Type.__name__=_G
_CpcBufferOperStatus_Object=MibTableColumn
cpcBufferOperStatus=_CpcBufferOperStatus_Object((1,3,6,1,4,1,9,9,602,1,3,1,1,4),_CpcBufferOperStatus_Type())
cpcBufferOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cpcBufferOperStatus.setStatus(_A)
_CpcScheduleConfig_ObjectIdentity=ObjectIdentity
cpcScheduleConfig=_CpcScheduleConfig_ObjectIdentity((1,3,6,1,4,1,9,9,602,1,4))
_CpcScheduleConfigTable_Object=MibTable
cpcScheduleConfigTable=_CpcScheduleConfigTable_Object((1,3,6,1,4,1,9,9,602,1,4,1))
if mibBuilder.loadTexts:cpcScheduleConfigTable.setStatus(_A)
_CpcScheduleConfigEntry_Object=MibTableRow
cpcScheduleConfigEntry=_CpcScheduleConfigEntry_Object((1,3,6,1,4,1,9,9,602,1,4,1,1))
cpcScheduleConfigEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cpcScheduleConfigEntry.setStatus(_A)
_CpcScheduleStartTime_Type=DateAndTime
_CpcScheduleStartTime_Object=MibTableColumn
cpcScheduleStartTime=_CpcScheduleStartTime_Object((1,3,6,1,4,1,9,9,602,1,4,1,1,1),_CpcScheduleStartTime_Type())
cpcScheduleStartTime.setMaxAccess(_H)
if mibBuilder.loadTexts:cpcScheduleStartTime.setStatus(_A)
_CpcScheduleCapturePeriod_Type=Unsigned32
_CpcScheduleCapturePeriod_Object=MibTableColumn
cpcScheduleCapturePeriod=_CpcScheduleCapturePeriod_Object((1,3,6,1,4,1,9,9,602,1,4,1,1,2),_CpcScheduleCapturePeriod_Type())
cpcScheduleCapturePeriod.setMaxAccess(_H)
if mibBuilder.loadTexts:cpcScheduleCapturePeriod.setStatus(_A)
if mibBuilder.loadTexts:cpcScheduleCapturePeriod.setUnits('seconds')
_CpcSessionStats_ObjectIdentity=ObjectIdentity
cpcSessionStats=_CpcSessionStats_ObjectIdentity((1,3,6,1,4,1,9,9,602,1,5))
_CpcSessionStatsTable_Object=MibTable
cpcSessionStatsTable=_CpcSessionStatsTable_Object((1,3,6,1,4,1,9,9,602,1,5,1))
if mibBuilder.loadTexts:cpcSessionStatsTable.setStatus(_A)
_CpcSessionStatsEntry_Object=MibTableRow
cpcSessionStatsEntry=_CpcSessionStatsEntry_Object((1,3,6,1,4,1,9,9,602,1,5,1,1))
cpcSessionStatsEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cpcSessionStatsEntry.setStatus(_A)
_CpcSessionPacketsReceived_Type=Unsigned32
_CpcSessionPacketsReceived_Object=MibTableColumn
cpcSessionPacketsReceived=_CpcSessionPacketsReceived_Object((1,3,6,1,4,1,9,9,602,1,5,1,1,1),_CpcSessionPacketsReceived_Type())
cpcSessionPacketsReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:cpcSessionPacketsReceived.setStatus(_A)
_CpcSessionPacketsCaptured_Type=Unsigned32
_CpcSessionPacketsCaptured_Object=MibTableColumn
cpcSessionPacketsCaptured=_CpcSessionPacketsCaptured_Object((1,3,6,1,4,1,9,9,602,1,5,1,1,2),_CpcSessionPacketsCaptured_Type())
cpcSessionPacketsCaptured.setMaxAccess(_D)
if mibBuilder.loadTexts:cpcSessionPacketsCaptured.setStatus(_A)
_CpcSessionPacketsDropped_Type=Unsigned32
_CpcSessionPacketsDropped_Object=MibTableColumn
cpcSessionPacketsDropped=_CpcSessionPacketsDropped_Object((1,3,6,1,4,1,9,9,602,1,5,1,1,3),_CpcSessionPacketsDropped_Type())
cpcSessionPacketsDropped.setMaxAccess(_D)
if mibBuilder.loadTexts:cpcSessionPacketsDropped.setStatus(_A)
_CpcMIBConformance_ObjectIdentity=ObjectIdentity
cpcMIBConformance=_CpcMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,602,2))
_CpcMIBCompliances_ObjectIdentity=ObjectIdentity
cpcMIBCompliances=_CpcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,602,2,1))
_CpcMIBGroups_ObjectIdentity=ObjectIdentity
cpcMIBGroups=_CpcMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,602,2,2))
cpcGenericConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,602,2,2,1))
cpcGenericConfigGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:cpcGenericConfigGroup.setStatus(_A)
cpcFilterConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,602,2,2,2))
cpcFilterConfigGroup.setObjects((_B,_k))
if mibBuilder.loadTexts:cpcFilterConfigGroup.setStatus(_A)
cpcMacFilterConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,602,2,2,3))
cpcMacFilterConfigGroup.setObjects((_B,_l))
if mibBuilder.loadTexts:cpcMacFilterConfigGroup.setStatus(_A)
cpcIpFilterConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,602,2,2,4))
cpcIpFilterConfigGroup.setObjects(*((_B,_m),(_B,_n)))
if mibBuilder.loadTexts:cpcIpFilterConfigGroup.setStatus(_A)
cpcDestFileNameConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,602,2,2,5))
cpcDestFileNameConfigGroup.setObjects((_B,_o))
if mibBuilder.loadTexts:cpcDestFileNameConfigGroup.setStatus(_A)
cpcPacketLengthFilterConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,602,2,2,6))
cpcPacketLengthFilterConfigGroup.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:cpcPacketLengthFilterConfigGroup.setStatus(_A)
cpcEthertypeFilterConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,602,2,2,7))
cpcEthertypeFilterConfigGroup.setObjects(*((_B,_r),(_B,_s)))
if mibBuilder.loadTexts:cpcEthertypeFilterConfigGroup.setStatus(_A)
cpcVlanFilterConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,602,2,2,8))
cpcVlanFilterConfigGroup.setObjects(*((_B,_t),(_B,_u)))
if mibBuilder.loadTexts:cpcVlanFilterConfigGroup.setStatus(_A)
cpcAccessGroupFilterConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,602,2,2,9))
cpcAccessGroupFilterConfigGroup.setObjects(*((_B,_v),(_B,_w)))
if mibBuilder.loadTexts:cpcAccessGroupFilterConfigGroup.setStatus(_A)
cpcBufferConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,602,2,2,10))
cpcBufferConfigGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:cpcBufferConfigGroup.setStatus(_A)
cpcScheduleConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,602,2,2,11))
cpcScheduleConfigGroup.setObjects(*((_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:cpcScheduleConfigGroup.setStatus(_A)
cpcSessionStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,602,2,2,12))
cpcSessionStatsGroup.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:cpcSessionStatsGroup.setStatus(_A)
cpcMaxMacFilterConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,602,2,2,13))
cpcMaxMacFilterConfigGroup.setObjects((_B,_A6))
if mibBuilder.loadTexts:cpcMaxMacFilterConfigGroup.setStatus(_A)
cpcMaxIpFilterConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,602,2,2,14))
cpcMaxIpFilterConfigGroup.setObjects((_B,_A7))
if mibBuilder.loadTexts:cpcMaxIpFilterConfigGroup.setStatus(_A)
cpcSessionPacketRateLimitGroup=ObjectGroup((1,3,6,1,4,1,9,9,602,2,2,15))
cpcSessionPacketRateLimitGroup.setObjects((_B,_A8))
if mibBuilder.loadTexts:cpcSessionPacketRateLimitGroup.setStatus(_A)
cpcSessionDescrGroup=ObjectGroup((1,3,6,1,4,1,9,9,602,2,2,16))
cpcSessionDescrGroup.setObjects((_B,_A9))
if mibBuilder.loadTexts:cpcSessionDescrGroup.setStatus(_A)
cpcCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,602,2,1,1))
cpcCompliance.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:cpcCompliance.setStatus('deprecated')
cpcComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,602,2,1,2))
cpcComplianceRev1.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:cpcComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CiscoPacketCaptureFilterCriteria':CiscoPacketCaptureFilterCriteria,'ciscoPacketCaptureMIB':ciscoPacketCaptureMIB,'cpcMIBNotification':cpcMIBNotification,'cpcMIBObjects':cpcMIBObjects,'cpcGenericConfig':cpcGenericConfig,_b:cpcMaxSessionAllowed,'cpcSessionConfigTable':cpcSessionConfigTable,'cpcSessionConfigEntry':cpcSessionConfigEntry,_E:cpcSessionId,_c:cpcSessionOperStatus,_o:cpcSessionDestFileName,_e:cpcSessionPacketLength,_f:cpcSessionPacketLimits,_g:cpcSessionAction,_h:cpcSessionConfigStatus,_A8:cpcSessionPacketRateLimit,_A9:cpcSessionDescr,_d:cpcSessionMaxSources,'cpcCaptureSourceIfTable':cpcCaptureSourceIfTable,'cpcCaptureSourceIfEntry':cpcCaptureSourceIfEntry,_i:cpcCaptureSourceIfDirection,_j:cpcCaptureSourceIfStatus,'cpcFilterConfig':cpcFilterConfig,_k:cpcMaxFilterAllowed,'cpcMacFilterTable':cpcMacFilterTable,'cpcMacFilterEntry':cpcMacFilterEntry,_S:cpcMacFilterMacAddress,_T:cpcMacFilterCriteria,_l:cpcMacFilterRowStatus,'cpcIpFilterTable':cpcIpFilterTable,'cpcIpFilterEntry':cpcIpFilterEntry,_U:cpcIpFilterAddressType,_V:cpcIpFilterAddress,_W:cpcIpFilterCriteria,_m:cpcIpFilterMask,_n:cpcIpFilterRowStatus,_A6:cpcMaxMacFilterAllowed,_A7:cpcMaxIpFilterAllowed,'cpcPacketLengthFilterTable':cpcPacketLengthFilterTable,'cpcPacketLengthFilterEntry':cpcPacketLengthFilterEntry,_p:cpcPacketLengthFilterMin,_q:cpcPacketLengthFilterMax,_r:cpcMaxEthertypeFilterAllowed,'cpcEthertypeFilterTable':cpcEthertypeFilterTable,'cpcEthertypeFilterEntry':cpcEthertypeFilterEntry,_X:cpcEthertypeFilterValue,_s:cpcEthertypeFilterStatus,_t:cpcMaxVlanFilterAllowed,'cpcVlanFilterTable':cpcVlanFilterTable,'cpcVlanFilterEntry':cpcVlanFilterEntry,_Y:cpcVlanFilterVlanIndex,_u:cpcVlanFilterRowStatus,_v:cpcMaxAccessGroupFilterAllowed,'cpcAccessGroupFilterTable':cpcAccessGroupFilterTable,'cpcAccessGroupFilterEntry':cpcAccessGroupFilterEntry,_Z:cpcAccessGroupFilterType,_a:cpcAccessGroupFilterName,_w:cpcAccessGroupFilterStatus,'cpcBufferConfig':cpcBufferConfig,'cpcBufferConfigTable':cpcBufferConfigTable,'cpcBufferConfigEntry':cpcBufferConfigEntry,_x:cpcBufferType,_y:cpcBufferSize,_z:cpcBufferAction,_A0:cpcBufferOperStatus,'cpcScheduleConfig':cpcScheduleConfig,'cpcScheduleConfigTable':cpcScheduleConfigTable,'cpcScheduleConfigEntry':cpcScheduleConfigEntry,_A1:cpcScheduleStartTime,_A2:cpcScheduleCapturePeriod,'cpcSessionStats':cpcSessionStats,'cpcSessionStatsTable':cpcSessionStatsTable,'cpcSessionStatsEntry':cpcSessionStatsEntry,_A3:cpcSessionPacketsReceived,_A4:cpcSessionPacketsCaptured,_A5:cpcSessionPacketsDropped,'cpcMIBConformance':cpcMIBConformance,'cpcMIBCompliances':cpcMIBCompliances,'cpcCompliance':cpcCompliance,'cpcComplianceRev1':cpcComplianceRev1,'cpcMIBGroups':cpcMIBGroups,_K:cpcGenericConfigGroup,_L:cpcFilterConfigGroup,_M:cpcMacFilterConfigGroup,_N:cpcIpFilterConfigGroup,_O:cpcDestFileNameConfigGroup,_AA:cpcPacketLengthFilterConfigGroup,_AB:cpcEthertypeFilterConfigGroup,_AC:cpcVlanFilterConfigGroup,_AD:cpcAccessGroupFilterConfigGroup,_AE:cpcBufferConfigGroup,_AF:cpcScheduleConfigGroup,_AG:cpcSessionStatsGroup,_AH:cpcMaxMacFilterConfigGroup,_AI:cpcMaxIpFilterConfigGroup,_AJ:cpcSessionPacketRateLimitGroup,_AK:cpcSessionDescrGroup})