_j='ieee8021BridgePEGroup'
_i='ieee8021BridgePEETSBandwidth'
_h='ieee8021BridgePEETSTrafficSelectionAlgorthm'
_g='ieee8021BridgePERRPortMap'
_f='ieee8021BridgePEUtVLANsSupported'
_e='ieee8021BridgePETCsSupported'
_d='ieee8021BridgePERemoteRepEChannelsSupported'
_c='ieee8021BridgePEExtPortEChannelsSupported'
_b='ieee8021BridgePEPFC'
_a='ieee8021BridgePECN'
_Z='ieee8021BridgePEDEI'
_Y='ieee8021BridgePEROW'
_X='ieee8021BridgePEPCP'
_W='ieee8021BridgePEPortRxrspErrorsPE'
_V='ieee8021BridgePEPortRxrqErrorsPE'
_U='ieee8021BridgePEPortRxrspErrorsBridge'
_T='ieee8021BridgePEPortRxrqErrorsBridge'
_S='ieee8021BridgePECounterDiscontinuityTime'
_R='ieee8021BridgePEPortNumber'
_Q='ieee8021BridgePEPortEcid'
_P='ieee8021BridgePEPortUpstreamCSPAddress'
_O='read-write'
_N='ieee8021BridgePEETSTrafficClass'
_M='ieee8021BridgePERREcid'
_L='E-channels'
_K='octets'
_J='frames'
_I='ieee8021BridgePEPortType'
_H='Integer32'
_G='ieee8021BridgePEPort'
_F='ieee8021BridgePEPortComponentId'
_E='not-accessible'
_D='Unsigned32'
_C='read-only'
_B='IEEE8021-PE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IEEE8021BridgePortNumber,IEEE8021BridgePortNumberOrZero,IEEE8021PbbComponentIdentifier,ieee802dot1mibs=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021BridgePortNumber','IEEE8021BridgePortNumberOrZero','IEEE8021PbbComponentIdentifier','ieee802dot1mibs')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp','TruthValue')
ieee8021BridgePEMib=ModuleIdentity((1,3,111,2,802,1,1,25))
if mibBuilder.loadTexts:ieee8021BridgePEMib.setRevisions(('2012-01-22 00:00',))
class IEEE802BridgePEEChannelIDTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4194302))
class IEEE802BridgePETrafficClassValueTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class IEEE802BridgePETrafficSelectionAlgorithmTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,255)));namedValues=NamedValues(*(('tsaStrictPriority',0),('tsaCreditBasedShaper',1),('tsaEnhancedTransmission',2),('tsaVendorSpecific',255)))
class IEEE802BridgePETrafficClassBandwidthValue(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Ieee8021BridgePENotifications_ObjectIdentity=ObjectIdentity
ieee8021BridgePENotifications=_Ieee8021BridgePENotifications_ObjectIdentity((1,3,111,2,802,1,1,25,1))
_Ieee8021BridgePEObjects_ObjectIdentity=ObjectIdentity
ieee8021BridgePEObjects=_Ieee8021BridgePEObjects_ObjectIdentity((1,3,111,2,802,1,1,25,2))
_Ieee8021BridgePEPortTable_Object=MibTable
ieee8021BridgePEPortTable=_Ieee8021BridgePEPortTable_Object((1,3,111,2,802,1,1,25,2,1))
if mibBuilder.loadTexts:ieee8021BridgePEPortTable.setStatus(_A)
_Ieee8021BridgePEPortEntry_Object=MibTableRow
ieee8021BridgePEPortEntry=_Ieee8021BridgePEPortEntry_Object((1,3,111,2,802,1,1,25,2,1,1))
ieee8021BridgePEPortEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_I))
if mibBuilder.loadTexts:ieee8021BridgePEPortEntry.setStatus(_A)
_Ieee8021BridgePEPortComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021BridgePEPortComponentId_Object=MibTableColumn
ieee8021BridgePEPortComponentId=_Ieee8021BridgePEPortComponentId_Object((1,3,111,2,802,1,1,25,2,1,1,1),_Ieee8021BridgePEPortComponentId_Type())
ieee8021BridgePEPortComponentId.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021BridgePEPortComponentId.setStatus(_A)
_Ieee8021BridgePEPort_Type=IEEE8021BridgePortNumber
_Ieee8021BridgePEPort_Object=MibTableColumn
ieee8021BridgePEPort=_Ieee8021BridgePEPort_Object((1,3,111,2,802,1,1,25,2,1,1,2),_Ieee8021BridgePEPort_Type())
ieee8021BridgePEPort.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021BridgePEPort.setStatus(_A)
class _Ieee8021BridgePEPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pepCascade',1),('pepUpstream',2),('pepExtended',3)))
_Ieee8021BridgePEPortType_Type.__name__=_H
_Ieee8021BridgePEPortType_Object=MibTableColumn
ieee8021BridgePEPortType=_Ieee8021BridgePEPortType_Object((1,3,111,2,802,1,1,25,2,1,1,3),_Ieee8021BridgePEPortType_Type())
ieee8021BridgePEPortType.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021BridgePEPortType.setStatus(_A)
_Ieee8021BridgePEPortUpstreamCSPAddress_Type=MacAddress
_Ieee8021BridgePEPortUpstreamCSPAddress_Object=MibTableColumn
ieee8021BridgePEPortUpstreamCSPAddress=_Ieee8021BridgePEPortUpstreamCSPAddress_Object((1,3,111,2,802,1,1,25,2,1,1,4),_Ieee8021BridgePEPortUpstreamCSPAddress_Type())
ieee8021BridgePEPortUpstreamCSPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021BridgePEPortUpstreamCSPAddress.setStatus(_A)
_Ieee8021BridgePEPortEcid_Type=IEEE802BridgePEEChannelIDTC
_Ieee8021BridgePEPortEcid_Object=MibTableColumn
ieee8021BridgePEPortEcid=_Ieee8021BridgePEPortEcid_Object((1,3,111,2,802,1,1,25,2,1,1,5),_Ieee8021BridgePEPortEcid_Type())
ieee8021BridgePEPortEcid.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021BridgePEPortEcid.setStatus(_A)
_Ieee8021BridgePEPortNumber_Type=IEEE8021BridgePortNumberOrZero
_Ieee8021BridgePEPortNumber_Object=MibTableColumn
ieee8021BridgePEPortNumber=_Ieee8021BridgePEPortNumber_Object((1,3,111,2,802,1,1,25,2,1,1,6),_Ieee8021BridgePEPortNumber_Type())
ieee8021BridgePEPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021BridgePEPortNumber.setStatus(_A)
_Ieee8021BridgePECounterDiscontinuityTime_Type=TimeStamp
_Ieee8021BridgePECounterDiscontinuityTime_Object=MibTableColumn
ieee8021BridgePECounterDiscontinuityTime=_Ieee8021BridgePECounterDiscontinuityTime_Object((1,3,111,2,802,1,1,25,2,1,1,7),_Ieee8021BridgePECounterDiscontinuityTime_Type())
ieee8021BridgePECounterDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021BridgePECounterDiscontinuityTime.setStatus(_A)
_Ieee8021BridgePEPortRxrqErrorsBridge_Type=Counter64
_Ieee8021BridgePEPortRxrqErrorsBridge_Object=MibTableColumn
ieee8021BridgePEPortRxrqErrorsBridge=_Ieee8021BridgePEPortRxrqErrorsBridge_Object((1,3,111,2,802,1,1,25,2,1,1,8),_Ieee8021BridgePEPortRxrqErrorsBridge_Type())
ieee8021BridgePEPortRxrqErrorsBridge.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021BridgePEPortRxrqErrorsBridge.setStatus(_A)
if mibBuilder.loadTexts:ieee8021BridgePEPortRxrqErrorsBridge.setUnits(_J)
_Ieee8021BridgePEPortRxrspErrorsBridge_Type=Counter64
_Ieee8021BridgePEPortRxrspErrorsBridge_Object=MibTableColumn
ieee8021BridgePEPortRxrspErrorsBridge=_Ieee8021BridgePEPortRxrspErrorsBridge_Object((1,3,111,2,802,1,1,25,2,1,1,9),_Ieee8021BridgePEPortRxrspErrorsBridge_Type())
ieee8021BridgePEPortRxrspErrorsBridge.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021BridgePEPortRxrspErrorsBridge.setStatus(_A)
if mibBuilder.loadTexts:ieee8021BridgePEPortRxrspErrorsBridge.setUnits(_K)
_Ieee8021BridgePEPortRxrqErrorsPE_Type=Counter64
_Ieee8021BridgePEPortRxrqErrorsPE_Object=MibTableColumn
ieee8021BridgePEPortRxrqErrorsPE=_Ieee8021BridgePEPortRxrqErrorsPE_Object((1,3,111,2,802,1,1,25,2,1,1,10),_Ieee8021BridgePEPortRxrqErrorsPE_Type())
ieee8021BridgePEPortRxrqErrorsPE.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021BridgePEPortRxrqErrorsPE.setStatus(_A)
if mibBuilder.loadTexts:ieee8021BridgePEPortRxrqErrorsPE.setUnits(_J)
_Ieee8021BridgePEPortRxrspErrorsPE_Type=Counter64
_Ieee8021BridgePEPortRxrspErrorsPE_Object=MibTableColumn
ieee8021BridgePEPortRxrspErrorsPE=_Ieee8021BridgePEPortRxrspErrorsPE_Object((1,3,111,2,802,1,1,25,2,1,1,11),_Ieee8021BridgePEPortRxrspErrorsPE_Type())
ieee8021BridgePEPortRxrspErrorsPE.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021BridgePEPortRxrspErrorsPE.setStatus(_A)
if mibBuilder.loadTexts:ieee8021BridgePEPortRxrspErrorsPE.setUnits(_K)
_Ieee8021BridgePEPCP_Type=TruthValue
_Ieee8021BridgePEPCP_Object=MibTableColumn
ieee8021BridgePEPCP=_Ieee8021BridgePEPCP_Object((1,3,111,2,802,1,1,25,2,1,1,12),_Ieee8021BridgePEPCP_Type())
ieee8021BridgePEPCP.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021BridgePEPCP.setStatus(_A)
_Ieee8021BridgePEROW_Type=TruthValue
_Ieee8021BridgePEROW_Object=MibTableColumn
ieee8021BridgePEROW=_Ieee8021BridgePEROW_Object((1,3,111,2,802,1,1,25,2,1,1,13),_Ieee8021BridgePEROW_Type())
ieee8021BridgePEROW.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021BridgePEROW.setStatus(_A)
_Ieee8021BridgePEDEI_Type=TruthValue
_Ieee8021BridgePEDEI_Object=MibTableColumn
ieee8021BridgePEDEI=_Ieee8021BridgePEDEI_Object((1,3,111,2,802,1,1,25,2,1,1,14),_Ieee8021BridgePEDEI_Type())
ieee8021BridgePEDEI.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021BridgePEDEI.setStatus(_A)
_Ieee8021BridgePECN_Type=TruthValue
_Ieee8021BridgePECN_Object=MibTableColumn
ieee8021BridgePECN=_Ieee8021BridgePECN_Object((1,3,111,2,802,1,1,25,2,1,1,15),_Ieee8021BridgePECN_Type())
ieee8021BridgePECN.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021BridgePECN.setStatus(_A)
_Ieee8021BridgePEPFC_Type=TruthValue
_Ieee8021BridgePEPFC_Object=MibTableColumn
ieee8021BridgePEPFC=_Ieee8021BridgePEPFC_Object((1,3,111,2,802,1,1,25,2,1,1,16),_Ieee8021BridgePEPFC_Type())
ieee8021BridgePEPFC.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021BridgePEPFC.setStatus(_A)
class _Ieee8021BridgePEExtPortEChannelsSupported_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1048575))
_Ieee8021BridgePEExtPortEChannelsSupported_Type.__name__=_D
_Ieee8021BridgePEExtPortEChannelsSupported_Object=MibTableColumn
ieee8021BridgePEExtPortEChannelsSupported=_Ieee8021BridgePEExtPortEChannelsSupported_Object((1,3,111,2,802,1,1,25,2,1,1,17),_Ieee8021BridgePEExtPortEChannelsSupported_Type())
ieee8021BridgePEExtPortEChannelsSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021BridgePEExtPortEChannelsSupported.setStatus(_A)
if mibBuilder.loadTexts:ieee8021BridgePEExtPortEChannelsSupported.setUnits(_L)
class _Ieee8021BridgePERemoteRepEChannelsSupported_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3145727))
_Ieee8021BridgePERemoteRepEChannelsSupported_Type.__name__=_D
_Ieee8021BridgePERemoteRepEChannelsSupported_Object=MibTableColumn
ieee8021BridgePERemoteRepEChannelsSupported=_Ieee8021BridgePERemoteRepEChannelsSupported_Object((1,3,111,2,802,1,1,25,2,1,1,18),_Ieee8021BridgePERemoteRepEChannelsSupported_Type())
ieee8021BridgePERemoteRepEChannelsSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021BridgePERemoteRepEChannelsSupported.setStatus(_A)
if mibBuilder.loadTexts:ieee8021BridgePERemoteRepEChannelsSupported.setUnits(_L)
class _Ieee8021BridgePETCsSupported_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Ieee8021BridgePETCsSupported_Type.__name__=_D
_Ieee8021BridgePETCsSupported_Object=MibTableColumn
ieee8021BridgePETCsSupported=_Ieee8021BridgePETCsSupported_Object((1,3,111,2,802,1,1,25,2,1,1,19),_Ieee8021BridgePETCsSupported_Type())
ieee8021BridgePETCsSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021BridgePETCsSupported.setStatus(_A)
if mibBuilder.loadTexts:ieee8021BridgePETCsSupported.setUnits('traffic classes')
class _Ieee8021BridgePEUtVLANsSupported_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Ieee8021BridgePEUtVLANsSupported_Type.__name__=_D
_Ieee8021BridgePEUtVLANsSupported_Object=MibTableColumn
ieee8021BridgePEUtVLANsSupported=_Ieee8021BridgePEUtVLANsSupported_Object((1,3,111,2,802,1,1,25,2,1,1,20),_Ieee8021BridgePEUtVLANsSupported_Type())
ieee8021BridgePEUtVLANsSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021BridgePEUtVLANsSupported.setStatus(_A)
if mibBuilder.loadTexts:ieee8021BridgePEUtVLANsSupported.setUnits('VLANs')
_Ieee8021BridgePERemoteReplicationTable_Object=MibTable
ieee8021BridgePERemoteReplicationTable=_Ieee8021BridgePERemoteReplicationTable_Object((1,3,111,2,802,1,1,25,2,2))
if mibBuilder.loadTexts:ieee8021BridgePERemoteReplicationTable.setStatus(_A)
_Ieee8021BridgePERemoteReplicationEntry_Object=MibTableRow
ieee8021BridgePERemoteReplicationEntry=_Ieee8021BridgePERemoteReplicationEntry_Object((1,3,111,2,802,1,1,25,2,2,1))
ieee8021BridgePERemoteReplicationEntry.setIndexNames((0,_B,_F),(0,_B,_M))
if mibBuilder.loadTexts:ieee8021BridgePERemoteReplicationEntry.setStatus(_A)
_Ieee8021BridgePERREcid_Type=IEEE802BridgePEEChannelIDTC
_Ieee8021BridgePERREcid_Object=MibTableColumn
ieee8021BridgePERREcid=_Ieee8021BridgePERREcid_Object((1,3,111,2,802,1,1,25,2,2,1,1),_Ieee8021BridgePERREcid_Type())
ieee8021BridgePERREcid.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021BridgePERREcid.setStatus(_A)
_Ieee8021BridgePERRPortMap_Type=PortList
_Ieee8021BridgePERRPortMap_Object=MibTableColumn
ieee8021BridgePERRPortMap=_Ieee8021BridgePERRPortMap_Object((1,3,111,2,802,1,1,25,2,2,1,2),_Ieee8021BridgePERRPortMap_Type())
ieee8021BridgePERRPortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021BridgePERRPortMap.setStatus(_A)
_Ieee8021BridgePEETSTable_Object=MibTable
ieee8021BridgePEETSTable=_Ieee8021BridgePEETSTable_Object((1,3,111,2,802,1,1,25,2,3))
if mibBuilder.loadTexts:ieee8021BridgePEETSTable.setStatus(_A)
_Ieee8021BridgePEETSEntry_Object=MibTableRow
ieee8021BridgePEETSEntry=_Ieee8021BridgePEETSEntry_Object((1,3,111,2,802,1,1,25,2,3,1))
ieee8021BridgePEETSEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_N))
if mibBuilder.loadTexts:ieee8021BridgePEETSEntry.setStatus(_A)
_Ieee8021BridgePEETSTrafficClass_Type=IEEE802BridgePETrafficClassValueTC
_Ieee8021BridgePEETSTrafficClass_Object=MibTableColumn
ieee8021BridgePEETSTrafficClass=_Ieee8021BridgePEETSTrafficClass_Object((1,3,111,2,802,1,1,25,2,3,1,1),_Ieee8021BridgePEETSTrafficClass_Type())
ieee8021BridgePEETSTrafficClass.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021BridgePEETSTrafficClass.setStatus(_A)
_Ieee8021BridgePEETSTrafficSelectionAlgorthm_Type=IEEE802BridgePETrafficSelectionAlgorithmTC
_Ieee8021BridgePEETSTrafficSelectionAlgorthm_Object=MibTableColumn
ieee8021BridgePEETSTrafficSelectionAlgorthm=_Ieee8021BridgePEETSTrafficSelectionAlgorthm_Object((1,3,111,2,802,1,1,25,2,3,1,2),_Ieee8021BridgePEETSTrafficSelectionAlgorthm_Type())
ieee8021BridgePEETSTrafficSelectionAlgorthm.setMaxAccess(_O)
if mibBuilder.loadTexts:ieee8021BridgePEETSTrafficSelectionAlgorthm.setStatus(_A)
_Ieee8021BridgePEETSBandwidth_Type=IEEE802BridgePETrafficClassBandwidthValue
_Ieee8021BridgePEETSBandwidth_Object=MibTableColumn
ieee8021BridgePEETSBandwidth=_Ieee8021BridgePEETSBandwidth_Object((1,3,111,2,802,1,1,25,2,3,1,3),_Ieee8021BridgePEETSBandwidth_Type())
ieee8021BridgePEETSBandwidth.setMaxAccess(_O)
if mibBuilder.loadTexts:ieee8021BridgePEETSBandwidth.setStatus(_A)
_Ieee8021BridgePEConformance_ObjectIdentity=ObjectIdentity
ieee8021BridgePEConformance=_Ieee8021BridgePEConformance_ObjectIdentity((1,3,111,2,802,1,1,25,3))
_Ieee8021BridgePEGroups_ObjectIdentity=ObjectIdentity
ieee8021BridgePEGroups=_Ieee8021BridgePEGroups_ObjectIdentity((1,3,111,2,802,1,1,25,3,1))
_Ieee8021BridgePECompliances_ObjectIdentity=ObjectIdentity
ieee8021BridgePECompliances=_Ieee8021BridgePECompliances_ObjectIdentity((1,3,111,2,802,1,1,25,3,2))
ieee8021BridgePEGroup=ObjectGroup((1,3,111,2,802,1,1,25,3,1,1))
ieee8021BridgePEGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:ieee8021BridgePEGroup.setStatus(_A)
ieee8021BridgePECompliance=ModuleCompliance((1,3,111,2,802,1,1,25,3,2,1))
ieee8021BridgePECompliance.setObjects((_B,_j))
if mibBuilder.loadTexts:ieee8021BridgePECompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'IEEE802BridgePEEChannelIDTC':IEEE802BridgePEEChannelIDTC,'IEEE802BridgePETrafficClassValueTC':IEEE802BridgePETrafficClassValueTC,'IEEE802BridgePETrafficSelectionAlgorithmTC':IEEE802BridgePETrafficSelectionAlgorithmTC,'IEEE802BridgePETrafficClassBandwidthValue':IEEE802BridgePETrafficClassBandwidthValue,'ieee8021BridgePEMib':ieee8021BridgePEMib,'ieee8021BridgePENotifications':ieee8021BridgePENotifications,'ieee8021BridgePEObjects':ieee8021BridgePEObjects,'ieee8021BridgePEPortTable':ieee8021BridgePEPortTable,'ieee8021BridgePEPortEntry':ieee8021BridgePEPortEntry,_F:ieee8021BridgePEPortComponentId,_G:ieee8021BridgePEPort,_I:ieee8021BridgePEPortType,_P:ieee8021BridgePEPortUpstreamCSPAddress,_Q:ieee8021BridgePEPortEcid,_R:ieee8021BridgePEPortNumber,_S:ieee8021BridgePECounterDiscontinuityTime,_T:ieee8021BridgePEPortRxrqErrorsBridge,_U:ieee8021BridgePEPortRxrspErrorsBridge,_V:ieee8021BridgePEPortRxrqErrorsPE,_W:ieee8021BridgePEPortRxrspErrorsPE,_X:ieee8021BridgePEPCP,_Y:ieee8021BridgePEROW,_Z:ieee8021BridgePEDEI,_a:ieee8021BridgePECN,_b:ieee8021BridgePEPFC,_c:ieee8021BridgePEExtPortEChannelsSupported,_d:ieee8021BridgePERemoteRepEChannelsSupported,_e:ieee8021BridgePETCsSupported,_f:ieee8021BridgePEUtVLANsSupported,'ieee8021BridgePERemoteReplicationTable':ieee8021BridgePERemoteReplicationTable,'ieee8021BridgePERemoteReplicationEntry':ieee8021BridgePERemoteReplicationEntry,_M:ieee8021BridgePERREcid,_g:ieee8021BridgePERRPortMap,'ieee8021BridgePEETSTable':ieee8021BridgePEETSTable,'ieee8021BridgePEETSEntry':ieee8021BridgePEETSEntry,_N:ieee8021BridgePEETSTrafficClass,_h:ieee8021BridgePEETSTrafficSelectionAlgorthm,_i:ieee8021BridgePEETSBandwidth,'ieee8021BridgePEConformance':ieee8021BridgePEConformance,'ieee8021BridgePEGroups':ieee8021BridgePEGroups,_j:ieee8021BridgePEGroup,'ieee8021BridgePECompliances':ieee8021BridgePECompliances,'ieee8021BridgePECompliance':ieee8021BridgePECompliance})