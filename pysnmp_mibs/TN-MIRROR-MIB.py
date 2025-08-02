_b='tnMirrorSourceSapEncapValue'
_a='tnMirrorSourceSapPortId'
_Z='tnMirrorSourcePortIndex'
_Y='tnMirrorSourceMacFilterParams'
_X='tnMirrorSourceMacFilter'
_W='000000000000'
_V='TmnxMirrorEncapType'
_U='TMplsLabel'
_T='tnMirrorDestinationIndex'
_S='TmnxPortID'
_R='TmnxEncapVal'
_Q='TPolicyID'
_P='TMACFilterID'
_O='TItemDescription'
_N='TFCName'
_M='Unsigned32'
_L='not-accessible'
_K='ServiceAdminStatus'
_J='MacAddress'
_I='accessible-for-notify'
_H='tnMirrorSourceIndex'
_G='tnSysSwitchId'
_F='TROPIC-SYSTEM-MIB'
_E='TruthValue'
_D='read-only'
_C='TN-MIRROR-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_J,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_E)
TEntryId,=mibBuilder.importSymbols('TN-FILTER-MIB','TEntryId')
SdpId,=mibBuilder.importSymbols('TN-SERV-MIB','SdpId')
ServiceAdminStatus,ServiceOperStatus,TFCName,TItemDescription,TMACFilterID,TPolicyID,TmnxEncapVal,TmnxPortID,TmnxServId=mibBuilder.importSymbols('TN-TC-MIB',_K,'ServiceOperStatus',_N,_O,_P,_Q,_R,_S,'TmnxServId')
tnSRMIBModules,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_F,_G)
tnMirrorMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,18))
if mibBuilder.loadTexts:tnMirrorMIBModule.setRevisions(('2020-08-14 00:00','2019-10-25 00:00','2017-02-10 00:00','2015-03-10 00:00','2012-12-05 00:00','2012-09-01 00:00','2008-01-01 00:00','2007-01-01 00:00','2005-01-24 00:00','2004-01-15 00:00','2003-08-15 00:00','2003-01-20 00:00','2002-03-14 00:00'))
class TMplsLabel(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048575))
class TmnxMirrorEncapType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('ether',1),('frameRelay',2),('ppp',3),('atmSdu',4),('satopE1',5),('satopT1',6),('satopE3',7),('satopT3',8),('cesopsn',9),('cesopsnCas',10),('ipOnly',11)))
_TnMirrorObjects_ObjectIdentity=ObjectIdentity
tnMirrorObjects=_TnMirrorObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,18))
_TnMirrorDestinationObjects_ObjectIdentity=ObjectIdentity
tnMirrorDestinationObjects=_TnMirrorDestinationObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,18,1))
_TnMirrorDestinationTable_Object=MibTable
tnMirrorDestinationTable=_TnMirrorDestinationTable_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1))
if mibBuilder.loadTexts:tnMirrorDestinationTable.setStatus(_A)
_TnMirrorDestinationEntry_Object=MibTableRow
tnMirrorDestinationEntry=_TnMirrorDestinationEntry_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1))
tnMirrorDestinationEntry.setIndexNames((0,_F,_G),(0,_C,_T))
if mibBuilder.loadTexts:tnMirrorDestinationEntry.setStatus(_A)
_TnMirrorDestinationIndex_Type=TmnxServId
_TnMirrorDestinationIndex_Object=MibTableColumn
tnMirrorDestinationIndex=_TnMirrorDestinationIndex_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,1),_TnMirrorDestinationIndex_Type())
tnMirrorDestinationIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:tnMirrorDestinationIndex.setStatus(_A)
_TnMirrorDestinationRowStatus_Type=RowStatus
_TnMirrorDestinationRowStatus_Object=MibTableColumn
tnMirrorDestinationRowStatus=_TnMirrorDestinationRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,2),_TnMirrorDestinationRowStatus_Type())
tnMirrorDestinationRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorDestinationRowStatus.setStatus(_A)
class _TnMirrorDestinationDescription_Type(TItemDescription):defaultHexValue=''
_TnMirrorDestinationDescription_Type.__name__=_O
_TnMirrorDestinationDescription_Object=MibTableColumn
tnMirrorDestinationDescription=_TnMirrorDestinationDescription_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,3),_TnMirrorDestinationDescription_Type())
tnMirrorDestinationDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorDestinationDescription.setStatus(_A)
class _TnMirrorDestinationFC_Type(TFCName):defaultHexValue='be'
_TnMirrorDestinationFC_Type.__name__=_N
_TnMirrorDestinationFC_Object=MibTableColumn
tnMirrorDestinationFC=_TnMirrorDestinationFC_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,4),_TnMirrorDestinationFC_Type())
tnMirrorDestinationFC.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorDestinationFC.setStatus(_A)
class _TnMirrorDestinationRemoteSource_Type(TruthValue):defaultValue=2
_TnMirrorDestinationRemoteSource_Type.__name__=_E
_TnMirrorDestinationRemoteSource_Object=MibTableColumn
tnMirrorDestinationRemoteSource=_TnMirrorDestinationRemoteSource_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,5),_TnMirrorDestinationRemoteSource_Type())
tnMirrorDestinationRemoteSource.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorDestinationRemoteSource.setStatus(_A)
class _TnMirrorDestinationSapPortId_Type(TmnxPortID):defaultValue=503316480
_TnMirrorDestinationSapPortId_Type.__name__=_S
_TnMirrorDestinationSapPortId_Object=MibTableColumn
tnMirrorDestinationSapPortId=_TnMirrorDestinationSapPortId_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,6),_TnMirrorDestinationSapPortId_Type())
tnMirrorDestinationSapPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorDestinationSapPortId.setStatus(_A)
class _TnMirrorDestinationSapEncapValue_Type(TmnxEncapVal):defaultValue=0
_TnMirrorDestinationSapEncapValue_Type.__name__=_R
_TnMirrorDestinationSapEncapValue_Object=MibTableColumn
tnMirrorDestinationSapEncapValue=_TnMirrorDestinationSapEncapValue_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,7),_TnMirrorDestinationSapEncapValue_Type())
tnMirrorDestinationSapEncapValue.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorDestinationSapEncapValue.setStatus(_A)
class _TnMirrorDestinationSdpNumber_Type(SdpId):defaultValue=0
_TnMirrorDestinationSdpNumber_Type.__name__='SdpId'
_TnMirrorDestinationSdpNumber_Object=MibTableColumn
tnMirrorDestinationSdpNumber=_TnMirrorDestinationSdpNumber_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,8),_TnMirrorDestinationSdpNumber_Type())
tnMirrorDestinationSdpNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorDestinationSdpNumber.setStatus(_A)
class _TnMirrorDestinationAdminStatus_Type(ServiceAdminStatus):defaultValue=2
_TnMirrorDestinationAdminStatus_Type.__name__=_K
_TnMirrorDestinationAdminStatus_Object=MibTableColumn
tnMirrorDestinationAdminStatus=_TnMirrorDestinationAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,10),_TnMirrorDestinationAdminStatus_Type())
tnMirrorDestinationAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorDestinationAdminStatus.setStatus(_A)
_TnMirrorDestinationOperStatus_Type=ServiceOperStatus
_TnMirrorDestinationOperStatus_Object=MibTableColumn
tnMirrorDestinationOperStatus=_TnMirrorDestinationOperStatus_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,11),_TnMirrorDestinationOperStatus_Type())
tnMirrorDestinationOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMirrorDestinationOperStatus.setStatus(_A)
class _TnMirrorDestinationSliceSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(128,9216))
_TnMirrorDestinationSliceSize_Type.__name__=_M
_TnMirrorDestinationSliceSize_Object=MibTableColumn
tnMirrorDestinationSliceSize=_TnMirrorDestinationSliceSize_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,13),_TnMirrorDestinationSliceSize_Type())
tnMirrorDestinationSliceSize.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorDestinationSliceSize.setStatus(_A)
class _TnMirrorDestinationSdpEgrSvcLabel_Type(TMplsLabel):defaultValue=0;subtypeSpec=TMplsLabel.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(16,1048575))
_TnMirrorDestinationSdpEgrSvcLabel_Type.__name__=_U
_TnMirrorDestinationSdpEgrSvcLabel_Object=MibTableColumn
tnMirrorDestinationSdpEgrSvcLabel=_TnMirrorDestinationSdpEgrSvcLabel_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,18),_TnMirrorDestinationSdpEgrSvcLabel_Type())
tnMirrorDestinationSdpEgrSvcLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorDestinationSdpEgrSvcLabel.setStatus(_A)
class _TnMirrorDestinationSapEgressQosPolicyId_Type(TPolicyID):defaultValue=1
_TnMirrorDestinationSapEgressQosPolicyId_Type.__name__=_Q
_TnMirrorDestinationSapEgressQosPolicyId_Object=MibTableColumn
tnMirrorDestinationSapEgressQosPolicyId=_TnMirrorDestinationSapEgressQosPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,19),_TnMirrorDestinationSapEgressQosPolicyId_Type())
tnMirrorDestinationSapEgressQosPolicyId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorDestinationSapEgressQosPolicyId.setStatus(_A)
class _TnMirrorDestinationEncapsulation_Type(TmnxMirrorEncapType):defaultValue=1
_TnMirrorDestinationEncapsulation_Type.__name__=_V
_TnMirrorDestinationEncapsulation_Object=MibTableColumn
tnMirrorDestinationEncapsulation=_TnMirrorDestinationEncapsulation_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,20),_TnMirrorDestinationEncapsulation_Type())
tnMirrorDestinationEncapsulation.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorDestinationEncapsulation.setStatus(_A)
_TnMirrorDestinationSdpOperEgrSvcLabel_Type=TMplsLabel
_TnMirrorDestinationSdpOperEgrSvcLabel_Object=MibTableColumn
tnMirrorDestinationSdpOperEgrSvcLabel=_TnMirrorDestinationSdpOperEgrSvcLabel_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,21),_TnMirrorDestinationSdpOperEgrSvcLabel_Type())
tnMirrorDestinationSdpOperEgrSvcLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMirrorDestinationSdpOperEgrSvcLabel.setStatus(_A)
class _TnMirrorDestinationEnablePortId_Type(TruthValue):defaultValue=2
_TnMirrorDestinationEnablePortId_Type.__name__=_E
_TnMirrorDestinationEnablePortId_Object=MibTableColumn
tnMirrorDestinationEnablePortId=_TnMirrorDestinationEnablePortId_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,22),_TnMirrorDestinationEnablePortId_Type())
tnMirrorDestinationEnablePortId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorDestinationEnablePortId.setStatus(_A)
class _TnMirrorDestSapEgrIpMirrorSA_Type(MacAddress):defaultHexValue=_W
_TnMirrorDestSapEgrIpMirrorSA_Type.__name__=_J
_TnMirrorDestSapEgrIpMirrorSA_Object=MibTableColumn
tnMirrorDestSapEgrIpMirrorSA=_TnMirrorDestSapEgrIpMirrorSA_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,23),_TnMirrorDestSapEgrIpMirrorSA_Type())
tnMirrorDestSapEgrIpMirrorSA.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorDestSapEgrIpMirrorSA.setStatus(_A)
class _TnMirrorDestSapEgrIpMirrorDA_Type(MacAddress):defaultHexValue=_W
_TnMirrorDestSapEgrIpMirrorDA_Type.__name__=_J
_TnMirrorDestSapEgrIpMirrorDA_Object=MibTableColumn
tnMirrorDestSapEgrIpMirrorDA=_TnMirrorDestSapEgrIpMirrorDA_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,24),_TnMirrorDestSapEgrIpMirrorDA_Type())
tnMirrorDestSapEgrIpMirrorDA.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorDestSapEgrIpMirrorDA.setStatus(_A)
_TnMirrorDestLastChanged_Type=TimeStamp
_TnMirrorDestLastChanged_Object=MibTableColumn
tnMirrorDestLastChanged=_TnMirrorDestLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,25),_TnMirrorDestLastChanged_Type())
tnMirrorDestLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMirrorDestLastChanged.setStatus(_A)
class _TnMirrorDestSapStatsCounterEnable_Type(TruthValue):defaultValue=1
_TnMirrorDestSapStatsCounterEnable_Type.__name__=_E
_TnMirrorDestSapStatsCounterEnable_Object=MibTableColumn
tnMirrorDestSapStatsCounterEnable=_TnMirrorDestSapStatsCounterEnable_Object((1,3,6,1,4,1,7483,6,1,2,18,1,1,1,26),_TnMirrorDestSapStatsCounterEnable_Type())
tnMirrorDestSapStatsCounterEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorDestSapStatsCounterEnable.setStatus('deprecated')
_TnMirrorDestinationScalar1_Type=Unsigned32
_TnMirrorDestinationScalar1_Object=MibScalar
tnMirrorDestinationScalar1=_TnMirrorDestinationScalar1_Object((1,3,6,1,4,1,7483,6,1,2,18,1,101),_TnMirrorDestinationScalar1_Type())
tnMirrorDestinationScalar1.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMirrorDestinationScalar1.setStatus(_A)
_TnMirrorDestinationScalar2_Type=Unsigned32
_TnMirrorDestinationScalar2_Object=MibScalar
tnMirrorDestinationScalar2=_TnMirrorDestinationScalar2_Object((1,3,6,1,4,1,7483,6,1,2,18,1,102),_TnMirrorDestinationScalar2_Type())
tnMirrorDestinationScalar2.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMirrorDestinationScalar2.setStatus(_A)
_TnMirrorSourceObjects_ObjectIdentity=ObjectIdentity
tnMirrorSourceObjects=_TnMirrorSourceObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,18,2))
_TnMirrorSourceTable_Object=MibTable
tnMirrorSourceTable=_TnMirrorSourceTable_Object((1,3,6,1,4,1,7483,6,1,2,18,2,1))
if mibBuilder.loadTexts:tnMirrorSourceTable.setStatus(_A)
_TnMirrorSourceEntry_Object=MibTableRow
tnMirrorSourceEntry=_TnMirrorSourceEntry_Object((1,3,6,1,4,1,7483,6,1,2,18,2,1,1))
tnMirrorSourceEntry.setIndexNames((0,_F,_G),(0,_C,_H))
if mibBuilder.loadTexts:tnMirrorSourceEntry.setStatus(_A)
_TnMirrorSourceIndex_Type=TmnxServId
_TnMirrorSourceIndex_Object=MibTableColumn
tnMirrorSourceIndex=_TnMirrorSourceIndex_Object((1,3,6,1,4,1,7483,6,1,2,18,2,1,1,1),_TnMirrorSourceIndex_Type())
tnMirrorSourceIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:tnMirrorSourceIndex.setStatus(_A)
class _TnMirrorSourceAdminStatus_Type(ServiceAdminStatus):defaultValue=1
_TnMirrorSourceAdminStatus_Type.__name__=_K
_TnMirrorSourceAdminStatus_Object=MibTableColumn
tnMirrorSourceAdminStatus=_TnMirrorSourceAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,18,2,1,1,2),_TnMirrorSourceAdminStatus_Type())
tnMirrorSourceAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorSourceAdminStatus.setStatus(_A)
_TnMirrorSourceRowStatus_Type=RowStatus
_TnMirrorSourceRowStatus_Object=MibTableColumn
tnMirrorSourceRowStatus=_TnMirrorSourceRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,18,2,1,1,3),_TnMirrorSourceRowStatus_Type())
tnMirrorSourceRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorSourceRowStatus.setStatus(_A)
_TnMirrorSourceLastChgd_Type=TimeStamp
_TnMirrorSourceLastChgd_Object=MibTableColumn
tnMirrorSourceLastChgd=_TnMirrorSourceLastChgd_Object((1,3,6,1,4,1,7483,6,1,2,18,2,1,1,4),_TnMirrorSourceLastChgd_Type())
tnMirrorSourceLastChgd.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMirrorSourceLastChgd.setStatus(_A)
_TnMirrorSourceMacFilterTable_Object=MibTable
tnMirrorSourceMacFilterTable=_TnMirrorSourceMacFilterTable_Object((1,3,6,1,4,1,7483,6,1,2,18,2,3))
if mibBuilder.loadTexts:tnMirrorSourceMacFilterTable.setStatus(_A)
_TnMirrorSourceMacFilterEntry_Object=MibTableRow
tnMirrorSourceMacFilterEntry=_TnMirrorSourceMacFilterEntry_Object((1,3,6,1,4,1,7483,6,1,2,18,2,3,1))
tnMirrorSourceMacFilterEntry.setIndexNames((0,_F,_G),(0,_C,_H),(0,_C,_X),(0,_C,_Y))
if mibBuilder.loadTexts:tnMirrorSourceMacFilterEntry.setStatus(_A)
class _TnMirrorSourceMacFilter_Type(TMACFilterID):subtypeSpec=TMACFilterID.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TnMirrorSourceMacFilter_Type.__name__=_P
_TnMirrorSourceMacFilter_Object=MibTableColumn
tnMirrorSourceMacFilter=_TnMirrorSourceMacFilter_Object((1,3,6,1,4,1,7483,6,1,2,18,2,3,1,1),_TnMirrorSourceMacFilter_Type())
tnMirrorSourceMacFilter.setMaxAccess(_L)
if mibBuilder.loadTexts:tnMirrorSourceMacFilter.setStatus(_A)
_TnMirrorSourceMacFilterParams_Type=TEntryId
_TnMirrorSourceMacFilterParams_Object=MibTableColumn
tnMirrorSourceMacFilterParams=_TnMirrorSourceMacFilterParams_Object((1,3,6,1,4,1,7483,6,1,2,18,2,3,1,2),_TnMirrorSourceMacFilterParams_Type())
tnMirrorSourceMacFilterParams.setMaxAccess(_L)
if mibBuilder.loadTexts:tnMirrorSourceMacFilterParams.setStatus(_A)
_TnMirrorSourceMacFilterRowStatus_Type=RowStatus
_TnMirrorSourceMacFilterRowStatus_Object=MibTableColumn
tnMirrorSourceMacFilterRowStatus=_TnMirrorSourceMacFilterRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,18,2,3,1,3),_TnMirrorSourceMacFilterRowStatus_Type())
tnMirrorSourceMacFilterRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorSourceMacFilterRowStatus.setStatus(_A)
_TnMirrorSourceMacFilterLastChgd_Type=TimeStamp
_TnMirrorSourceMacFilterLastChgd_Object=MibTableColumn
tnMirrorSourceMacFilterLastChgd=_TnMirrorSourceMacFilterLastChgd_Object((1,3,6,1,4,1,7483,6,1,2,18,2,3,1,4),_TnMirrorSourceMacFilterLastChgd_Type())
tnMirrorSourceMacFilterLastChgd.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMirrorSourceMacFilterLastChgd.setStatus(_A)
_TnMirrorSourcePortTable_Object=MibTable
tnMirrorSourcePortTable=_TnMirrorSourcePortTable_Object((1,3,6,1,4,1,7483,6,1,2,18,2,5))
if mibBuilder.loadTexts:tnMirrorSourcePortTable.setStatus(_A)
_TnMirrorSourcePortEntry_Object=MibTableRow
tnMirrorSourcePortEntry=_TnMirrorSourcePortEntry_Object((1,3,6,1,4,1,7483,6,1,2,18,2,5,1))
tnMirrorSourcePortEntry.setIndexNames((0,_F,_G),(0,_C,_H),(0,_C,_Z))
if mibBuilder.loadTexts:tnMirrorSourcePortEntry.setStatus(_A)
_TnMirrorSourcePortIndex_Type=TmnxPortID
_TnMirrorSourcePortIndex_Object=MibTableColumn
tnMirrorSourcePortIndex=_TnMirrorSourcePortIndex_Object((1,3,6,1,4,1,7483,6,1,2,18,2,5,1,1),_TnMirrorSourcePortIndex_Type())
tnMirrorSourcePortIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:tnMirrorSourcePortIndex.setStatus(_A)
_TnMirrorSourcePortRowStatus_Type=RowStatus
_TnMirrorSourcePortRowStatus_Object=MibTableColumn
tnMirrorSourcePortRowStatus=_TnMirrorSourcePortRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,18,2,5,1,2),_TnMirrorSourcePortRowStatus_Type())
tnMirrorSourcePortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorSourcePortRowStatus.setStatus(_A)
class _TnMirrorSourcePortEgressEnabled_Type(TruthValue):defaultValue=2
_TnMirrorSourcePortEgressEnabled_Type.__name__=_E
_TnMirrorSourcePortEgressEnabled_Object=MibTableColumn
tnMirrorSourcePortEgressEnabled=_TnMirrorSourcePortEgressEnabled_Object((1,3,6,1,4,1,7483,6,1,2,18,2,5,1,3),_TnMirrorSourcePortEgressEnabled_Type())
tnMirrorSourcePortEgressEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorSourcePortEgressEnabled.setStatus(_A)
class _TnMirrorSourcePortIngressEnabled_Type(TruthValue):defaultValue=2
_TnMirrorSourcePortIngressEnabled_Type.__name__=_E
_TnMirrorSourcePortIngressEnabled_Object=MibTableColumn
tnMirrorSourcePortIngressEnabled=_TnMirrorSourcePortIngressEnabled_Object((1,3,6,1,4,1,7483,6,1,2,18,2,5,1,4),_TnMirrorSourcePortIngressEnabled_Type())
tnMirrorSourcePortIngressEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorSourcePortIngressEnabled.setStatus(_A)
_TnMirrorSourcePortLastChgd_Type=TimeStamp
_TnMirrorSourcePortLastChgd_Object=MibTableColumn
tnMirrorSourcePortLastChgd=_TnMirrorSourcePortLastChgd_Object((1,3,6,1,4,1,7483,6,1,2,18,2,5,1,5),_TnMirrorSourcePortLastChgd_Type())
tnMirrorSourcePortLastChgd.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMirrorSourcePortLastChgd.setStatus(_A)
_TnMirrorSourceSapTable_Object=MibTable
tnMirrorSourceSapTable=_TnMirrorSourceSapTable_Object((1,3,6,1,4,1,7483,6,1,2,18,2,6))
if mibBuilder.loadTexts:tnMirrorSourceSapTable.setStatus(_A)
_TnMirrorSourceSapEntry_Object=MibTableRow
tnMirrorSourceSapEntry=_TnMirrorSourceSapEntry_Object((1,3,6,1,4,1,7483,6,1,2,18,2,6,1))
tnMirrorSourceSapEntry.setIndexNames((0,_F,_G),(0,_C,_H),(0,_C,_a),(0,_C,_b))
if mibBuilder.loadTexts:tnMirrorSourceSapEntry.setStatus(_A)
_TnMirrorSourceSapPortId_Type=TmnxPortID
_TnMirrorSourceSapPortId_Object=MibTableColumn
tnMirrorSourceSapPortId=_TnMirrorSourceSapPortId_Object((1,3,6,1,4,1,7483,6,1,2,18,2,6,1,2),_TnMirrorSourceSapPortId_Type())
tnMirrorSourceSapPortId.setMaxAccess(_I)
if mibBuilder.loadTexts:tnMirrorSourceSapPortId.setStatus(_A)
_TnMirrorSourceSapEncapValue_Type=TmnxEncapVal
_TnMirrorSourceSapEncapValue_Object=MibTableColumn
tnMirrorSourceSapEncapValue=_TnMirrorSourceSapEncapValue_Object((1,3,6,1,4,1,7483,6,1,2,18,2,6,1,3),_TnMirrorSourceSapEncapValue_Type())
tnMirrorSourceSapEncapValue.setMaxAccess(_I)
if mibBuilder.loadTexts:tnMirrorSourceSapEncapValue.setStatus(_A)
_TnMirrorSourceSapRowStatus_Type=RowStatus
_TnMirrorSourceSapRowStatus_Object=MibTableColumn
tnMirrorSourceSapRowStatus=_TnMirrorSourceSapRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,18,2,6,1,4),_TnMirrorSourceSapRowStatus_Type())
tnMirrorSourceSapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorSourceSapRowStatus.setStatus(_A)
class _TnMirrorSourceSapEgressEnabled_Type(TruthValue):defaultValue=2
_TnMirrorSourceSapEgressEnabled_Type.__name__=_E
_TnMirrorSourceSapEgressEnabled_Object=MibTableColumn
tnMirrorSourceSapEgressEnabled=_TnMirrorSourceSapEgressEnabled_Object((1,3,6,1,4,1,7483,6,1,2,18,2,6,1,5),_TnMirrorSourceSapEgressEnabled_Type())
tnMirrorSourceSapEgressEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorSourceSapEgressEnabled.setStatus(_A)
class _TnMirrorSourceSapIngressEnabled_Type(TruthValue):defaultValue=2
_TnMirrorSourceSapIngressEnabled_Type.__name__=_E
_TnMirrorSourceSapIngressEnabled_Object=MibTableColumn
tnMirrorSourceSapIngressEnabled=_TnMirrorSourceSapIngressEnabled_Object((1,3,6,1,4,1,7483,6,1,2,18,2,6,1,6),_TnMirrorSourceSapIngressEnabled_Type())
tnMirrorSourceSapIngressEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMirrorSourceSapIngressEnabled.setStatus(_A)
_TnMirrorSourceSapLastChgd_Type=TimeStamp
_TnMirrorSourceSapLastChgd_Object=MibTableColumn
tnMirrorSourceSapLastChgd=_TnMirrorSourceSapLastChgd_Object((1,3,6,1,4,1,7483,6,1,2,18,2,6,1,7),_TnMirrorSourceSapLastChgd_Type())
tnMirrorSourceSapLastChgd.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMirrorSourceSapLastChgd.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_U:TMplsLabel,_V:TmnxMirrorEncapType,'tnMirrorMIBModule':tnMirrorMIBModule,'tnMirrorObjects':tnMirrorObjects,'tnMirrorDestinationObjects':tnMirrorDestinationObjects,'tnMirrorDestinationTable':tnMirrorDestinationTable,'tnMirrorDestinationEntry':tnMirrorDestinationEntry,_T:tnMirrorDestinationIndex,'tnMirrorDestinationRowStatus':tnMirrorDestinationRowStatus,'tnMirrorDestinationDescription':tnMirrorDestinationDescription,'tnMirrorDestinationFC':tnMirrorDestinationFC,'tnMirrorDestinationRemoteSource':tnMirrorDestinationRemoteSource,'tnMirrorDestinationSapPortId':tnMirrorDestinationSapPortId,'tnMirrorDestinationSapEncapValue':tnMirrorDestinationSapEncapValue,'tnMirrorDestinationSdpNumber':tnMirrorDestinationSdpNumber,'tnMirrorDestinationAdminStatus':tnMirrorDestinationAdminStatus,'tnMirrorDestinationOperStatus':tnMirrorDestinationOperStatus,'tnMirrorDestinationSliceSize':tnMirrorDestinationSliceSize,'tnMirrorDestinationSdpEgrSvcLabel':tnMirrorDestinationSdpEgrSvcLabel,'tnMirrorDestinationSapEgressQosPolicyId':tnMirrorDestinationSapEgressQosPolicyId,'tnMirrorDestinationEncapsulation':tnMirrorDestinationEncapsulation,'tnMirrorDestinationSdpOperEgrSvcLabel':tnMirrorDestinationSdpOperEgrSvcLabel,'tnMirrorDestinationEnablePortId':tnMirrorDestinationEnablePortId,'tnMirrorDestSapEgrIpMirrorSA':tnMirrorDestSapEgrIpMirrorSA,'tnMirrorDestSapEgrIpMirrorDA':tnMirrorDestSapEgrIpMirrorDA,'tnMirrorDestLastChanged':tnMirrorDestLastChanged,'tnMirrorDestSapStatsCounterEnable':tnMirrorDestSapStatsCounterEnable,'tnMirrorDestinationScalar1':tnMirrorDestinationScalar1,'tnMirrorDestinationScalar2':tnMirrorDestinationScalar2,'tnMirrorSourceObjects':tnMirrorSourceObjects,'tnMirrorSourceTable':tnMirrorSourceTable,'tnMirrorSourceEntry':tnMirrorSourceEntry,_H:tnMirrorSourceIndex,'tnMirrorSourceAdminStatus':tnMirrorSourceAdminStatus,'tnMirrorSourceRowStatus':tnMirrorSourceRowStatus,'tnMirrorSourceLastChgd':tnMirrorSourceLastChgd,'tnMirrorSourceMacFilterTable':tnMirrorSourceMacFilterTable,'tnMirrorSourceMacFilterEntry':tnMirrorSourceMacFilterEntry,_X:tnMirrorSourceMacFilter,_Y:tnMirrorSourceMacFilterParams,'tnMirrorSourceMacFilterRowStatus':tnMirrorSourceMacFilterRowStatus,'tnMirrorSourceMacFilterLastChgd':tnMirrorSourceMacFilterLastChgd,'tnMirrorSourcePortTable':tnMirrorSourcePortTable,'tnMirrorSourcePortEntry':tnMirrorSourcePortEntry,_Z:tnMirrorSourcePortIndex,'tnMirrorSourcePortRowStatus':tnMirrorSourcePortRowStatus,'tnMirrorSourcePortEgressEnabled':tnMirrorSourcePortEgressEnabled,'tnMirrorSourcePortIngressEnabled':tnMirrorSourcePortIngressEnabled,'tnMirrorSourcePortLastChgd':tnMirrorSourcePortLastChgd,'tnMirrorSourceSapTable':tnMirrorSourceSapTable,'tnMirrorSourceSapEntry':tnMirrorSourceSapEntry,_a:tnMirrorSourceSapPortId,_b:tnMirrorSourceSapEncapValue,'tnMirrorSourceSapRowStatus':tnMirrorSourceSapRowStatus,'tnMirrorSourceSapEgressEnabled':tnMirrorSourceSapEgressEnabled,'tnMirrorSourceSapIngressEnabled':tnMirrorSourceSapIngressEnabled,'tnMirrorSourceSapLastChgd':tnMirrorSourceSapLastChgd})