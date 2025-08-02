_q='tnPortTestEntry'
_p='tnObjectAppPool'
_o='tnObjectAppType'
_n='tnObjectId'
_m='tnObjectType'
_l='tnMMACID'
_k='tnPMACID'
_j='tnEMACID'
_i='TmnxPortEtherReportStatus'
_h='mega-bits per second'
_g='halfDuplex'
_f='fullDuplex'
_e='default'
_d='TmnxPortAdminStatus'
_c='diagnose'
_b='oduflex'
_a='failed'
_Z='outOfService'
_Y='inService'
_X='TmnxEnabledDisabled'
_W='TmnxActionType'
_V='TNamedItem'
_U='TItemLongDescription'
_T='MacAddress'
_S='Packets'
_R='seconds'
_Q='none'
_P='Bits'
_O='OctetString'
_N='tnPortPortID'
_M='tnSysSwitchId'
_L='TROPIC-SYSTEM-MIB'
_K='TNamedItemOrEmpty'
_J='not-accessible'
_I='unknown'
_H='notApplicable'
_G='TruthValue'
_F='TN-PORT-MIB'
_E='Unsigned32'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_P,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString',_T,'PhysAddress','RowPointer','RowStatus','TextualConvention','TimeStamp',_G)
TItemLongDescription,TNamedItem,TNamedItemOrEmpty,TmnxActionType,TmnxEnabledDisabled,TmnxPortID=mibBuilder.importSymbols('TN-TC-MIB',_U,_V,_K,_W,_X,'TmnxPortID')
tnSRMIBModules,tnSRNotifyPrefix,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRNotifyPrefix','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_L,_M)
tnPortMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,25))
if mibBuilder.loadTexts:tnPortMIBModule.setRevisions(('2020-05-01 00:00','2020-01-10 00:00','2019-11-15 00:00','2019-10-25 00:00','2019-06-07 00:00','2019-03-08 00:00','2019-03-01 00:00','2019-02-15 00:00','2019-01-25 00:00','2018-12-28 00:00','2018-12-14 00:00','2018-01-05 00:00','2017-08-02 00:00','2017-05-31 00:00','2017-03-10 00:00','2016-10-19 00:00','2015-09-02 00:00','2015-01-22 00:00','2013-08-22 00:00','2012-12-05 00:00','2012-11-06 00:00','2012-10-12 00:00','2009-02-28 00:00','2008-07-01 00:00','2008-01-01 00:00','2007-01-01 00:00','2006-03-16 00:00','2005-08-31 00:00','2005-01-24 00:00','2004-03-01 00:00'))
class TmnxPortOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),(_Y,2),(_Z,3),('diagnosing',4),(_a,5)))
class TmnxPortEtherReportStatus(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('notUsed',0),('signalFailure',1),('remoteFault',2),('localFault',3),('noFrameLock',4),('highBer',5),('noBlockLock',6),('noAmLock',7),('duplicateLane',8)))
class TmnxPortClass(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*((_Q,1),('faste',2),('gige',3),('xgige',4),('sonet',5),('vport',6),('unused',7),('xcme',8),('tdm',9),('xlgige',10),('cgige',11),('xcmbar',12),(_b,13),('vsme',14),('tfgige',15),('cpri3',16),('cpri5',17),('cpri6',18),('cpri7',19),('cpri8',20),('cpri10',21),('obsai8',22),('obsai4',23),('cpri4',24)))
class TmnxPortConnectorType(TextualConvention,Unsigned32):status=_A
class TmnxPortState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Q,1),('ghost',2),('linkDown',3),('linkUp',4),('up',5),(_c,6)))
class TmnxPortType(TextualConvention,Unsigned32):status=_A
class TmnxAlarmState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),('alarmActive',1),('alarmCleared',2)))
class TmnxPortAdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noop',1),(_Y,2),(_Z,3),(_c,4)))
_TnHwObjs_ObjectIdentity=ObjectIdentity
tnHwObjs=_TnHwObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,2))
_TnPortObjs_ObjectIdentity=ObjectIdentity
tnPortObjs=_TnPortObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,2,4))
_TnPortTableLastChange_Type=TimeStamp
_TnPortTableLastChange_Object=MibScalar
tnPortTableLastChange=_TnPortTableLastChange_Object((1,3,6,1,4,1,7483,6,1,2,2,4,1),_TnPortTableLastChange_Type())
tnPortTableLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortTableLastChange.setStatus(_A)
_TnPortTable_Object=MibTable
tnPortTable=_TnPortTable_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2))
if mibBuilder.loadTexts:tnPortTable.setStatus(_A)
_TnPortEntry_Object=MibTableRow
tnPortEntry=_TnPortEntry_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1))
tnPortEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:tnPortEntry.setStatus(_A)
_TnPortPortID_Type=TmnxPortID
_TnPortPortID_Object=MibTableColumn
tnPortPortID=_TnPortPortID_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,1),_TnPortPortID_Type())
tnPortPortID.setMaxAccess(_J)
if mibBuilder.loadTexts:tnPortPortID.setStatus(_A)
_TnPortLastChangeTime_Type=TimeStamp
_TnPortLastChangeTime_Object=MibTableColumn
tnPortLastChangeTime=_TnPortLastChangeTime_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,2),_TnPortLastChangeTime_Type())
tnPortLastChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortLastChangeTime.setStatus(_A)
_TnPortType_Type=TmnxPortType
_TnPortType_Object=MibTableColumn
tnPortType=_TnPortType_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,3),_TnPortType_Type())
tnPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortType.setStatus(_A)
_TnPortClass_Type=TmnxPortClass
_TnPortClass_Object=MibTableColumn
tnPortClass=_TnPortClass_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,4),_TnPortClass_Type())
tnPortClass.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortClass.setStatus(_A)
class _TnPortDescription_Type(TItemLongDescription):defaultHexValue=''
_TnPortDescription_Type.__name__=_U
_TnPortDescription_Object=MibTableColumn
tnPortDescription=_TnPortDescription_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,5),_TnPortDescription_Type())
tnPortDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortDescription.setStatus(_A)
_TnPortName_Type=TNamedItemOrEmpty
_TnPortName_Object=MibTableColumn
tnPortName=_TnPortName_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,6),_TnPortName_Type())
tnPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortName.setStatus(_A)
class _TnPortAlias_Type(TNamedItemOrEmpty):defaultHexValue=''
_TnPortAlias_Type.__name__=_K
_TnPortAlias_Object=MibTableColumn
tnPortAlias=_TnPortAlias_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,7),_TnPortAlias_Type())
tnPortAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortAlias.setStatus(_A)
class _TnPortUserAssignedMac_Type(TruthValue):defaultValue=2
_TnPortUserAssignedMac_Type.__name__=_G
_TnPortUserAssignedMac_Object=MibTableColumn
tnPortUserAssignedMac=_TnPortUserAssignedMac_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,8),_TnPortUserAssignedMac_Type())
tnPortUserAssignedMac.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortUserAssignedMac.setStatus(_A)
class _TnPortMacAddress_Type(MacAddress):defaultHexValue='000000000000'
_TnPortMacAddress_Type.__name__=_T
_TnPortMacAddress_Object=MibTableColumn
tnPortMacAddress=_TnPortMacAddress_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,9),_TnPortMacAddress_Type())
tnPortMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortMacAddress.setStatus(_A)
_TnPortHwMacAddress_Type=MacAddress
_TnPortHwMacAddress_Object=MibTableColumn
tnPortHwMacAddress=_TnPortHwMacAddress_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,10),_TnPortHwMacAddress_Type())
tnPortHwMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortHwMacAddress.setStatus(_A)
class _TnPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('undefined',0),('access',1),('network',2)))
_TnPortMode_Type.__name__=_D
_TnPortMode_Object=MibTableColumn
tnPortMode=_TnPortMode_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,11),_TnPortMode_Type())
tnPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortMode.setStatus(_A)
class _TnPortEncapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_I,0),('nullEncap',1),('qEncap',2),('mplsEncap',3),('bcpNullEncap',4),('bcpDot1qEncap',5),('ipcpEncap',6),('frEncap',7),('pppAutoEncap',8),('atmEncap',9),('qinqEncap',10),('wanMirrorEncap',11),('ciscoHDLCEncap',12),('cemEncap',13)))
_TnPortEncapType_Type.__name__=_D
_TnPortEncapType_Object=MibTableColumn
tnPortEncapType=_TnPortEncapType_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,12),_TnPortEncapType_Type())
tnPortEncapType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEncapType.setStatus(_A)
class _TnPortLagId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_TnPortLagId_Type.__name__=_E
_TnPortLagId_Object=MibTableColumn
tnPortLagId=_TnPortLagId_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,13),_TnPortLagId_Type())
tnPortLagId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortLagId.setStatus(_A)
class _TnPortHoldTimeUp_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90000))
_TnPortHoldTimeUp_Type.__name__=_E
_TnPortHoldTimeUp_Object=MibTableColumn
tnPortHoldTimeUp=_TnPortHoldTimeUp_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,14),_TnPortHoldTimeUp_Type())
tnPortHoldTimeUp.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortHoldTimeUp.setStatus(_A)
class _TnPortHoldTimeDown_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90000))
_TnPortHoldTimeDown_Type.__name__=_E
_TnPortHoldTimeDown_Object=MibTableColumn
tnPortHoldTimeDown=_TnPortHoldTimeDown_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,15),_TnPortHoldTimeDown_Type())
tnPortHoldTimeDown.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortHoldTimeDown.setStatus(_A)
class _TnPortUpProtocols_Type(Bits):namedValues=NamedValues(*(('portUpIpv4',0),('portUpMpls',1),('portUpBcp',2),('portUpIso',3),('portUpFr',4),('portUpAtm',5),('portUpChdlc',6),('portUpIma',7),('portUpIpv6',8)))
_TnPortUpProtocols_Type.__name__=_P
_TnPortUpProtocols_Object=MibTableColumn
tnPortUpProtocols=_TnPortUpProtocols_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,16),_TnPortUpProtocols_Type())
tnPortUpProtocols.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortUpProtocols.setStatus(_A)
_TnPortConnectorType_Type=TmnxPortConnectorType
_TnPortConnectorType_Object=MibTableColumn
tnPortConnectorType=_TnPortConnectorType_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,17),_TnPortConnectorType_Type())
tnPortConnectorType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortConnectorType.setStatus(_A)
class _TnPortTransceiverType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,130)));namedValues=NamedValues(*((_I,0),('gbic',1),('moduleConnectorSolderedToMotherboard',2),('sfpTransceiver',3),('xbiTransceiver',4),('xenpakTransceiver',5),('xfpTransceiver',6),('xffTransceiver',7),('xfpeTransceiver',8),('xpakTransceiver',9),('x2Transceiver',10),('dwdmSfpTransceiver',11),('qsfpTransceiver',12),('qsfpPlusTransceiver',13),('cfpTransceiver',14),('shieldedMiniMultilaneHd4x',15),('shieldedMiniMultilaneHd8x',16),('qsfp28Transceiver',17),('cfp4Transceiver',18),('cdfpStyle1or2Transceiver',19),('shieldedMiniMultilaneHd4xFc',20),('shieldedMiniMultilaneHd8xFc',21),('cdfpStyle3Transceiver',22),('microQsfpTransceiver',23),('qsfpDd8xTransceiver',24),('osfp8xTransceiver',25),('sfpDd2xTransceiver',26),('tsopSmartSfpTransceiver',130)))
_TnPortTransceiverType_Type.__name__=_D
_TnPortTransceiverType_Object=MibTableColumn
tnPortTransceiverType=_TnPortTransceiverType_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,25),_TnPortTransceiverType_Type())
tnPortTransceiverType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortTransceiverType.setStatus(_A)
_TnPortTransceiverLaserWaveLen_Type=Unsigned32
_TnPortTransceiverLaserWaveLen_Object=MibTableColumn
tnPortTransceiverLaserWaveLen=_TnPortTransceiverLaserWaveLen_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,27),_TnPortTransceiverLaserWaveLen_Type())
tnPortTransceiverLaserWaveLen.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortTransceiverLaserWaveLen.setStatus(_A)
class _TnPortTransceiverDiagCapable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('true',1),('false',2)))
_TnPortTransceiverDiagCapable_Type.__name__=_D
_TnPortTransceiverDiagCapable_Object=MibTableColumn
tnPortTransceiverDiagCapable=_TnPortTransceiverDiagCapable_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,28),_TnPortTransceiverDiagCapable_Type())
tnPortTransceiverDiagCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortTransceiverDiagCapable.setStatus(_A)
_TnPortTransceiverModelNumber_Type=TNamedItemOrEmpty
_TnPortTransceiverModelNumber_Object=MibTableColumn
tnPortTransceiverModelNumber=_TnPortTransceiverModelNumber_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,29),_TnPortTransceiverModelNumber_Type())
tnPortTransceiverModelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortTransceiverModelNumber.setStatus(_A)
class _TnPortSFPConnectorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,32,33,34,35,36,37,38,128)));namedValues=NamedValues(*((_I,0),('sc',1),('fiberChannel-Style1-CopperConnector',2),('fiberChannel-Style2-CopperConnector',3),('bncortnc',4),('fiberChannelCoaxialHeaders',5),('fiberJack',6),('lc',7),('mt-rj',8),('mu',9),('sg',10),('opticalPigtail',11),('mpo1x12',12),('mpo2x16',13),('hssdcII',32),('copperPigtail',33),('rj45',34),('noSeparableConnector',35),('mxc2x16',36),('csOptical',37),('miniCsOptical',38),('copperGigE',128)))
_TnPortSFPConnectorCode_Type.__name__=_D
_TnPortSFPConnectorCode_Object=MibTableColumn
tnPortSFPConnectorCode=_TnPortSFPConnectorCode_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,30),_TnPortSFPConnectorCode_Type())
tnPortSFPConnectorCode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortSFPConnectorCode.setStatus(_A)
_TnPortSFPVendorOUI_Type=Unsigned32
_TnPortSFPVendorOUI_Object=MibTableColumn
tnPortSFPVendorOUI=_TnPortSFPVendorOUI_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,31),_TnPortSFPVendorOUI_Type())
tnPortSFPVendorOUI.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortSFPVendorOUI.setStatus(_A)
_TnPortSFPVendorManufactureDate_Type=DateAndTime
_TnPortSFPVendorManufactureDate_Object=MibTableColumn
tnPortSFPVendorManufactureDate=_TnPortSFPVendorManufactureDate_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,32),_TnPortSFPVendorManufactureDate_Type())
tnPortSFPVendorManufactureDate.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortSFPVendorManufactureDate.setStatus(_A)
class _TnPortSFPMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('ethernet',1),('sonetsdh',2)))
_TnPortSFPMedia_Type.__name__=_D
_TnPortSFPMedia_Object=MibTableColumn
tnPortSFPMedia=_TnPortSFPMedia_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,33),_TnPortSFPMedia_Type())
tnPortSFPMedia.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortSFPMedia.setStatus(_A)
_TnPortSFPEquipped_Type=TruthValue
_TnPortSFPEquipped_Object=MibTableColumn
tnPortSFPEquipped=_TnPortSFPEquipped_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,34),_TnPortSFPEquipped_Type())
tnPortSFPEquipped.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortSFPEquipped.setStatus(_A)
_TnPortEquipped_Type=TruthValue
_TnPortEquipped_Object=MibTableColumn
tnPortEquipped=_TnPortEquipped_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,35),_TnPortEquipped_Type())
tnPortEquipped.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortEquipped.setStatus(_A)
_TnPortLinkStatus_Type=TruthValue
_TnPortLinkStatus_Object=MibTableColumn
tnPortLinkStatus=_TnPortLinkStatus_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,36),_TnPortLinkStatus_Type())
tnPortLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortLinkStatus.setStatus(_A)
class _TnPortAdminStatus_Type(TmnxPortAdminStatus):defaultValue=2
_TnPortAdminStatus_Type.__name__=_d
_TnPortAdminStatus_Object=MibTableColumn
tnPortAdminStatus=_TnPortAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,37),_TnPortAdminStatus_Type())
tnPortAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortAdminStatus.setStatus(_A)
_TnPortOperStatus_Type=TmnxPortOperStatus
_TnPortOperStatus_Object=MibTableColumn
tnPortOperStatus=_TnPortOperStatus_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,38),_TnPortOperStatus_Type())
tnPortOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortOperStatus.setStatus(_A)
_TnPortState_Type=TmnxPortState
_TnPortState_Object=MibTableColumn
tnPortState=_TnPortState_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,39),_TnPortState_Type())
tnPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortState.setStatus(_A)
_TnPortPrevState_Type=TmnxPortState
_TnPortPrevState_Object=MibTableColumn
tnPortPrevState=_TnPortPrevState_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,40),_TnPortPrevState_Type())
tnPortPrevState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortPrevState.setStatus(_A)
_TnPortNumAlarms_Type=Unsigned32
_TnPortNumAlarms_Object=MibTableColumn
tnPortNumAlarms=_TnPortNumAlarms_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,41),_TnPortNumAlarms_Type())
tnPortNumAlarms.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortNumAlarms.setStatus(_A)
_TnPortAlarmState_Type=TmnxAlarmState
_TnPortAlarmState_Object=MibTableColumn
tnPortAlarmState=_TnPortAlarmState_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,42),_TnPortAlarmState_Type())
tnPortAlarmState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortAlarmState.setStatus(_A)
_TnPortLastAlarmEvent_Type=RowPointer
_TnPortLastAlarmEvent_Object=MibTableColumn
tnPortLastAlarmEvent=_TnPortLastAlarmEvent_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,43),_TnPortLastAlarmEvent_Type())
tnPortLastAlarmEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortLastAlarmEvent.setStatus(_A)
class _TnPortClearAlarms_Type(TmnxActionType):defaultValue=2
_TnPortClearAlarms_Type.__name__=_W
_TnPortClearAlarms_Object=MibTableColumn
tnPortClearAlarms=_TnPortClearAlarms_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,44),_TnPortClearAlarms_Type())
tnPortClearAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortClearAlarms.setStatus(_A)
_TnPortSFPVendorSerialNum_Type=TNamedItemOrEmpty
_TnPortSFPVendorSerialNum_Object=MibTableColumn
tnPortSFPVendorSerialNum=_TnPortSFPVendorSerialNum_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,45),_TnPortSFPVendorSerialNum_Type())
tnPortSFPVendorSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortSFPVendorSerialNum.setStatus(_A)
_TnPortSFPVendorPartNum_Type=TNamedItemOrEmpty
_TnPortSFPVendorPartNum_Object=MibTableColumn
tnPortSFPVendorPartNum=_TnPortSFPVendorPartNum_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,46),_TnPortSFPVendorPartNum_Type())
tnPortSFPVendorPartNum.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortSFPVendorPartNum.setStatus(_A)
_TnPortLastStateChanged_Type=TimeStamp
_TnPortLastStateChanged_Object=MibTableColumn
tnPortLastStateChanged=_TnPortLastStateChanged_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,48),_TnPortLastStateChanged_Type())
tnPortLastStateChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortLastStateChanged.setStatus(_A)
_TnPortNumChannels_Type=Unsigned32
_TnPortNumChannels_Object=MibTableColumn
tnPortNumChannels=_TnPortNumChannels_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,49),_TnPortNumChannels_Type())
tnPortNumChannels.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortNumChannels.setStatus(_A)
_TnPortNetworkEgrQueues_Type=TNamedItemOrEmpty
_TnPortNetworkEgrQueues_Object=MibTableColumn
tnPortNetworkEgrQueues=_TnPortNetworkEgrQueues_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,50),_TnPortNetworkEgrQueues_Type())
tnPortNetworkEgrQueues.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortNetworkEgrQueues.setStatus(_A)
class _TnPortBundleNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_TnPortBundleNumber_Type.__name__=_D
_TnPortBundleNumber_Object=MibTableColumn
tnPortBundleNumber=_TnPortBundleNumber_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,51),_TnPortBundleNumber_Type())
tnPortBundleNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortBundleNumber.setStatus(_A)
_TnPortIsLeaf_Type=TruthValue
_TnPortIsLeaf_Object=MibTableColumn
tnPortIsLeaf=_TnPortIsLeaf_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,52),_TnPortIsLeaf_Type())
tnPortIsLeaf.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortIsLeaf.setStatus(_A)
_TnPortParentPortID_Type=TmnxPortID
_TnPortParentPortID_Object=MibTableColumn
tnPortParentPortID=_TnPortParentPortID_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,54),_TnPortParentPortID_Type())
tnPortParentPortID.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortParentPortID.setStatus(_A)
class _TnPortOpticalCompliance_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_TnPortOpticalCompliance_Type.__name__=_O
_TnPortOpticalCompliance_Object=MibTableColumn
tnPortOpticalCompliance=_TnPortOpticalCompliance_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,55),_TnPortOpticalCompliance_Type())
tnPortOpticalCompliance.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortOpticalCompliance.setStatus(_A)
class _TnPortLoadBalanceAlgorithm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),(_e,1),('includeL4',2),('excludeL4',3)))
_TnPortLoadBalanceAlgorithm_Type.__name__=_D
_TnPortLoadBalanceAlgorithm_Object=MibTableColumn
tnPortLoadBalanceAlgorithm=_TnPortLoadBalanceAlgorithm_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,56),_TnPortLoadBalanceAlgorithm_Type())
tnPortLoadBalanceAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortLoadBalanceAlgorithm.setStatus(_A)
class _TnPortEgrPortSchedPlcy_Type(TNamedItemOrEmpty):defaultValue=OctetString('')
_TnPortEgrPortSchedPlcy_Type.__name__=_K
_TnPortEgrPortSchedPlcy_Object=MibTableColumn
tnPortEgrPortSchedPlcy=_TnPortEgrPortSchedPlcy_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,57),_TnPortEgrPortSchedPlcy_Type())
tnPortEgrPortSchedPlcy.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEgrPortSchedPlcy.setStatus(_A)
_TnPortLastClearedTime_Type=TimeStamp
_TnPortLastClearedTime_Object=MibTableColumn
tnPortLastClearedTime=_TnPortLastClearedTime_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,58),_TnPortLastClearedTime_Type())
tnPortLastClearedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortLastClearedTime.setStatus(_A)
class _TnPortEgrHsmdaSchedPlcy_Type(TNamedItemOrEmpty):defaultValue=OctetString('')
_TnPortEgrHsmdaSchedPlcy_Type.__name__=_K
_TnPortEgrHsmdaSchedPlcy_Object=MibTableColumn
tnPortEgrHsmdaSchedPlcy=_TnPortEgrHsmdaSchedPlcy_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,59),_TnPortEgrHsmdaSchedPlcy_Type())
tnPortEgrHsmdaSchedPlcy.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEgrHsmdaSchedPlcy.setStatus(_A)
class _TnPortIngNamedPoolPlcy_Type(TNamedItemOrEmpty):defaultHexValue=''
_TnPortIngNamedPoolPlcy_Type.__name__=_K
_TnPortIngNamedPoolPlcy_Object=MibTableColumn
tnPortIngNamedPoolPlcy=_TnPortIngNamedPoolPlcy_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,60),_TnPortIngNamedPoolPlcy_Type())
tnPortIngNamedPoolPlcy.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortIngNamedPoolPlcy.setStatus(_A)
class _TnPortEgrNamedPoolPlcy_Type(TNamedItemOrEmpty):defaultHexValue=''
_TnPortEgrNamedPoolPlcy_Type.__name__=_K
_TnPortEgrNamedPoolPlcy_Object=MibTableColumn
tnPortEgrNamedPoolPlcy=_TnPortEgrNamedPoolPlcy_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,61),_TnPortEgrNamedPoolPlcy_Type())
tnPortEgrNamedPoolPlcy.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEgrNamedPoolPlcy.setStatus(_A)
class _TnPortIngPoolPercentRate_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_TnPortIngPoolPercentRate_Type.__name__=_E
_TnPortIngPoolPercentRate_Object=MibTableColumn
tnPortIngPoolPercentRate=_TnPortIngPoolPercentRate_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,62),_TnPortIngPoolPercentRate_Type())
tnPortIngPoolPercentRate.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortIngPoolPercentRate.setStatus(_A)
class _TnPortEgrPoolPercentRate_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_TnPortEgrPoolPercentRate_Type.__name__=_E
_TnPortEgrPoolPercentRate_Object=MibTableColumn
tnPortEgrPoolPercentRate=_TnPortEgrPoolPercentRate_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,63),_TnPortEgrPoolPercentRate_Type())
tnPortEgrPoolPercentRate.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEgrPoolPercentRate.setStatus(_A)
class _TnPortDDMEventSuppression_Type(TruthValue):defaultValue=2
_TnPortDDMEventSuppression_Type.__name__=_G
_TnPortDDMEventSuppression_Object=MibTableColumn
tnPortDDMEventSuppression=_TnPortDDMEventSuppression_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,64),_TnPortDDMEventSuppression_Type())
tnPortDDMEventSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortDDMEventSuppression.setStatus(_A)
class _TnPortSFPStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('not-equipped',0),('operational',1),('read-error',2),('data-corrupt',3),('ddm-corrupt',4),('unsupported',5)))
_TnPortSFPStatus_Type.__name__=_D
_TnPortSFPStatus_Object=MibTableColumn
tnPortSFPStatus=_TnPortSFPStatus_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,65),_TnPortSFPStatus_Type())
tnPortSFPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortSFPStatus.setStatus(_A)
class _TnPortReasonDownFlags_Type(Bits):namedValues=NamedValues(*((_I,0),('linklossFwd',1),('lagMemberPortStandby',2),('ethCfmFault',3),('opticalTuning',4),('channelOutOfRange',5),('channelNotConfigured',6),('crcError',7),('internalMacTxError',8),('noServicePort',9)))
_TnPortReasonDownFlags_Type.__name__=_P
_TnPortReasonDownFlags_Object=MibTableColumn
tnPortReasonDownFlags=_TnPortReasonDownFlags_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,66),_TnPortReasonDownFlags_Type())
tnPortReasonDownFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortReasonDownFlags.setStatus(_A)
class _TnPortSSMRxQualityLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*((_I,0),('prs',1),('stu',2),('st2',3),('tnc',4),('st3e',5),('st3',6),('smc',7),('st4',8),('dus',9),('prc',10),('ssua',11),('ssub',12),('sec',13),('dnu',14),('inv',15),('pno',16),('eec1',17),('eec2',18),(_a,19)))
_TnPortSSMRxQualityLevel_Type.__name__=_D
_TnPortSSMRxQualityLevel_Object=MibTableColumn
tnPortSSMRxQualityLevel=_TnPortSSMRxQualityLevel_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,67),_TnPortSSMRxQualityLevel_Type())
tnPortSSMRxQualityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortSSMRxQualityLevel.setStatus(_A)
class _TnPortDwdmLaserChannel_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(17,61),ValueRangeConstraint(170,610))
_TnPortDwdmLaserChannel_Type.__name__=_E
_TnPortDwdmLaserChannel_Object=MibTableColumn
tnPortDwdmLaserChannel=_TnPortDwdmLaserChannel_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,68),_TnPortDwdmLaserChannel_Type())
tnPortDwdmLaserChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortDwdmLaserChannel.setStatus(_A)
_TnPortOtuCapable_Type=TruthValue
_TnPortOtuCapable_Object=MibTableColumn
tnPortOtuCapable=_TnPortOtuCapable_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,69),_TnPortOtuCapable_Type())
tnPortOtuCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortOtuCapable.setStatus(_A)
class _TnPortHoldTimeUnits_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_R,0),('centiseconds',1)))
_TnPortHoldTimeUnits_Type.__name__=_D
_TnPortHoldTimeUnits_Object=MibTableColumn
tnPortHoldTimeUnits=_TnPortHoldTimeUnits_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,70),_TnPortHoldTimeUnits_Type())
tnPortHoldTimeUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortHoldTimeUnits.setStatus(_A)
class _TnPortLinkLengthInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TnPortLinkLengthInfo_Type.__name__=_O
_TnPortLinkLengthInfo_Object=MibTableColumn
tnPortLinkLengthInfo=_TnPortLinkLengthInfo_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,71),_TnPortLinkLengthInfo_Type())
tnPortLinkLengthInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortLinkLengthInfo.setStatus(_A)
_TnPortSFPNumLanes_Type=Unsigned32
_TnPortSFPNumLanes_Object=MibTableColumn
tnPortSFPNumLanes=_TnPortSFPNumLanes_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,72),_TnPortSFPNumLanes_Type())
tnPortSFPNumLanes.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortSFPNumLanes.setStatus(_A)
_TnPortPhysStateChangeCount_Type=Counter32
_TnPortPhysStateChangeCount_Object=MibTableColumn
tnPortPhysStateChangeCount=_TnPortPhysStateChangeCount_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,73),_TnPortPhysStateChangeCount_Type())
tnPortPhysStateChangeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortPhysStateChangeCount.setStatus(_A)
_TnPortPacketSwitchId_Type=Unsigned32
_TnPortPacketSwitchId_Object=MibTableColumn
tnPortPacketSwitchId=_TnPortPacketSwitchId_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,74),_TnPortPacketSwitchId_Type())
tnPortPacketSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortPacketSwitchId.setStatus(_A)
class _TnPortOtnSignalDegrade_Type(TmnxEnabledDisabled):defaultValue=2
_TnPortOtnSignalDegrade_Type.__name__=_X
_TnPortOtnSignalDegrade_Object=MibTableColumn
tnPortOtnSignalDegrade=_TnPortOtnSignalDegrade_Object((1,3,6,1,4,1,7483,6,1,2,2,4,2,1,75),_TnPortOtnSignalDegrade_Type())
tnPortOtnSignalDegrade.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortOtnSignalDegrade.setStatus(_A)
_TnPortTestTable_Object=MibTable
tnPortTestTable=_TnPortTestTable_Object((1,3,6,1,4,1,7483,6,1,2,2,4,3))
if mibBuilder.loadTexts:tnPortTestTable.setStatus(_A)
_TnPortTestEntry_Object=MibTableRow
tnPortTestEntry=_TnPortTestEntry_Object((1,3,6,1,4,1,7483,6,1,2,2,4,3,1))
if mibBuilder.loadTexts:tnPortTestEntry.setStatus(_A)
class _TnPortTestState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notInTest',1),('inTest',2)))
_TnPortTestState_Type.__name__=_D
_TnPortTestState_Object=MibTableColumn
tnPortTestState=_TnPortTestState_Object((1,3,6,1,4,1,7483,6,1,2,2,4,3,1,1),_TnPortTestState_Type())
tnPortTestState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortTestState.setStatus(_A)
class _TnPortTestMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),('loopback1',1),('loopback2',2),('loopback3',3),('singalInsertion',4)))
_TnPortTestMode_Type.__name__=_D
_TnPortTestMode_Object=MibTableColumn
tnPortTestMode=_TnPortTestMode_Object((1,3,6,1,4,1,7483,6,1,2,2,4,3,1,2),_TnPortTestMode_Type())
tnPortTestMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortTestMode.setStatus(_A)
_TnPortTestParameter_Type=Unsigned32
_TnPortTestParameter_Object=MibTableColumn
tnPortTestParameter=_TnPortTestParameter_Object((1,3,6,1,4,1,7483,6,1,2,2,4,3,1,3),_TnPortTestParameter_Type())
tnPortTestParameter.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortTestParameter.setStatus(_A)
class _TnPortTestLastResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),('success',1),('failure',2),('timeout',3)))
_TnPortTestLastResult_Type.__name__=_D
_TnPortTestLastResult_Object=MibTableColumn
tnPortTestLastResult=_TnPortTestLastResult_Object((1,3,6,1,4,1,7483,6,1,2,2,4,3,1,4),_TnPortTestLastResult_Type())
tnPortTestLastResult.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortTestLastResult.setStatus(_A)
_TnPortTestStartTime_Type=DateAndTime
_TnPortTestStartTime_Object=MibTableColumn
tnPortTestStartTime=_TnPortTestStartTime_Object((1,3,6,1,4,1,7483,6,1,2,2,4,3,1,5),_TnPortTestStartTime_Type())
tnPortTestStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortTestStartTime.setStatus(_A)
_TnPortTestEndTime_Type=DateAndTime
_TnPortTestEndTime_Object=MibTableColumn
tnPortTestEndTime=_TnPortTestEndTime_Object((1,3,6,1,4,1,7483,6,1,2,2,4,3,1,6),_TnPortTestEndTime_Type())
tnPortTestEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortTestEndTime.setStatus(_A)
class _TnPortTestDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_TnPortTestDuration_Type.__name__=_D
_TnPortTestDuration_Object=MibTableColumn
tnPortTestDuration=_TnPortTestDuration_Object((1,3,6,1,4,1,7483,6,1,2,2,4,3,1,7),_TnPortTestDuration_Type())
tnPortTestDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortTestDuration.setStatus(_A)
class _TnPortTestAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),('startTest',2),('stopTest',3)))
_TnPortTestAction_Type.__name__=_D
_TnPortTestAction_Object=MibTableColumn
tnPortTestAction=_TnPortTestAction_Object((1,3,6,1,4,1,7483,6,1,2,2,4,3,1,8),_TnPortTestAction_Type())
tnPortTestAction.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortTestAction.setStatus(_A)
_TnPortEtherTable_Object=MibTable
tnPortEtherTable=_TnPortEtherTable_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4))
if mibBuilder.loadTexts:tnPortEtherTable.setStatus(_A)
_TnPortEtherEntry_Object=MibTableRow
tnPortEtherEntry=_TnPortEtherEntry_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1))
tnPortEtherEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:tnPortEtherEntry.setStatus(_A)
class _TnPortEtherMTU_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(512,9612))
_TnPortEtherMTU_Type.__name__=_E
_TnPortEtherMTU_Object=MibTableColumn
tnPortEtherMTU=_TnPortEtherMTU_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,1),_TnPortEtherMTU_Type())
tnPortEtherMTU.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherMTU.setStatus(_A)
if mibBuilder.loadTexts:tnPortEtherMTU.setUnits('bytes')
class _TnPortEtherDuplex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_f,1),(_g,2)))
_TnPortEtherDuplex_Type.__name__=_D
_TnPortEtherDuplex_Object=MibTableColumn
tnPortEtherDuplex=_TnPortEtherDuplex_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,2),_TnPortEtherDuplex_Type())
tnPortEtherDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherDuplex.setStatus(_A)
class _TnPortEtherSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_H,0),('speed10',1),('speed100',2),('speed1000',3),('speed10000',4),('speed40000',5),('speed100000',6),(_b,7),('speed2457',8),('speed4915',9),('spped6114',10),('speed9830',11),('speed10137',12),('speed24330',13),('speed3072',14),('speed25000',15)))
_TnPortEtherSpeed_Type.__name__=_D
_TnPortEtherSpeed_Object=MibTableColumn
tnPortEtherSpeed=_TnPortEtherSpeed_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,3),_TnPortEtherSpeed_Type())
tnPortEtherSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherSpeed.setStatus(_A)
class _TnPortEtherAutoNegotiate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),('true',1),('false',2),('limited',3)))
_TnPortEtherAutoNegotiate_Type.__name__=_D
_TnPortEtherAutoNegotiate_Object=MibTableColumn
tnPortEtherAutoNegotiate=_TnPortEtherAutoNegotiate_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,4),_TnPortEtherAutoNegotiate_Type())
tnPortEtherAutoNegotiate.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherAutoNegotiate.setStatus(_A)
class _TnPortEtherOperDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_f,1),(_g,2)))
_TnPortEtherOperDuplex_Type.__name__=_D
_TnPortEtherOperDuplex_Object=MibTableColumn
tnPortEtherOperDuplex=_TnPortEtherOperDuplex_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,5),_TnPortEtherOperDuplex_Type())
tnPortEtherOperDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortEtherOperDuplex.setStatus(_A)
_TnPortEtherOperSpeed_Type=Unsigned32
_TnPortEtherOperSpeed_Object=MibTableColumn
tnPortEtherOperSpeed=_TnPortEtherOperSpeed_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,6),_TnPortEtherOperSpeed_Type())
tnPortEtherOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortEtherOperSpeed.setStatus(_A)
if mibBuilder.loadTexts:tnPortEtherOperSpeed.setUnits(_h)
class _TnPortEtherAcctPolicyId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_TnPortEtherAcctPolicyId_Type.__name__=_E
_TnPortEtherAcctPolicyId_Object=MibTableColumn
tnPortEtherAcctPolicyId=_TnPortEtherAcctPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,7),_TnPortEtherAcctPolicyId_Type())
tnPortEtherAcctPolicyId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherAcctPolicyId.setStatus(_A)
class _TnPortEtherCollectStats_Type(TruthValue):defaultValue=1
_TnPortEtherCollectStats_Type.__name__=_G
_TnPortEtherCollectStats_Object=MibTableColumn
tnPortEtherCollectStats=_TnPortEtherCollectStats_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,8),_TnPortEtherCollectStats_Type())
tnPortEtherCollectStats.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherCollectStats.setStatus(_A)
class _TnPortEtherMDIMDIX_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),('mdi',1),('mdix',2)))
_TnPortEtherMDIMDIX_Type.__name__=_D
_TnPortEtherMDIMDIX_Object=MibTableColumn
tnPortEtherMDIMDIX=_TnPortEtherMDIMDIX_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,9),_TnPortEtherMDIMDIX_Type())
tnPortEtherMDIMDIX.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortEtherMDIMDIX.setStatus(_A)
class _TnPortEtherXGigMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('lan',1),('wan',2)))
_TnPortEtherXGigMode_Type.__name__=_D
_TnPortEtherXGigMode_Object=MibTableColumn
tnPortEtherXGigMode=_TnPortEtherXGigMode_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,10),_TnPortEtherXGigMode_Type())
tnPortEtherXGigMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherXGigMode.setStatus(_A)
class _TnPortEtherEgressRate_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,100000000))
_TnPortEtherEgressRate_Type.__name__=_D
_TnPortEtherEgressRate_Object=MibTableColumn
tnPortEtherEgressRate=_TnPortEtherEgressRate_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,11),_TnPortEtherEgressRate_Type())
tnPortEtherEgressRate.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherEgressRate.setStatus(_A)
class _TnPortEtherDot1qEtype_Type(Unsigned32):defaultValue=33024;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1536,65535))
_TnPortEtherDot1qEtype_Type.__name__=_E
_TnPortEtherDot1qEtype_Object=MibTableColumn
tnPortEtherDot1qEtype=_TnPortEtherDot1qEtype_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,12),_TnPortEtherDot1qEtype_Type())
tnPortEtherDot1qEtype.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherDot1qEtype.setStatus(_A)
class _TnPortEtherQinqEtype_Type(Unsigned32):defaultValue=33024;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1536,65535))
_TnPortEtherQinqEtype_Type.__name__=_E
_TnPortEtherQinqEtype_Object=MibTableColumn
tnPortEtherQinqEtype=_TnPortEtherQinqEtype_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,13),_TnPortEtherQinqEtype_Type())
tnPortEtherQinqEtype.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherQinqEtype.setStatus(_A)
class _TnPortEtherIngressRate_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,10000))
_TnPortEtherIngressRate_Type.__name__=_D
_TnPortEtherIngressRate_Object=MibTableColumn
tnPortEtherIngressRate=_TnPortEtherIngressRate_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,14),_TnPortEtherIngressRate_Type())
tnPortEtherIngressRate.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherIngressRate.setStatus(_A)
if mibBuilder.loadTexts:tnPortEtherIngressRate.setUnits(_h)
class _TnPortEtherReportAlarm_Type(TmnxPortEtherReportStatus):defaultBinValue='0011'
_TnPortEtherReportAlarm_Type.__name__=_i
_TnPortEtherReportAlarm_Object=MibTableColumn
tnPortEtherReportAlarm=_TnPortEtherReportAlarm_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,15),_TnPortEtherReportAlarm_Type())
tnPortEtherReportAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherReportAlarm.setStatus(_A)
_TnPortEtherReportAlarmStatus_Type=TmnxPortEtherReportStatus
_TnPortEtherReportAlarmStatus_Object=MibTableColumn
tnPortEtherReportAlarmStatus=_TnPortEtherReportAlarmStatus_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,16),_TnPortEtherReportAlarmStatus_Type())
tnPortEtherReportAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortEtherReportAlarmStatus.setStatus(_A)
_TnPortEtherPkts1519toMax_Type=Counter32
_TnPortEtherPkts1519toMax_Object=MibTableColumn
tnPortEtherPkts1519toMax=_TnPortEtherPkts1519toMax_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,17),_TnPortEtherPkts1519toMax_Type())
tnPortEtherPkts1519toMax.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortEtherPkts1519toMax.setStatus(_A)
if mibBuilder.loadTexts:tnPortEtherPkts1519toMax.setUnits(_S)
_TnPortEtherHCOverPkts1519toMax_Type=Counter32
_TnPortEtherHCOverPkts1519toMax_Object=MibTableColumn
tnPortEtherHCOverPkts1519toMax=_TnPortEtherHCOverPkts1519toMax_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,18),_TnPortEtherHCOverPkts1519toMax_Type())
tnPortEtherHCOverPkts1519toMax.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortEtherHCOverPkts1519toMax.setStatus(_A)
if mibBuilder.loadTexts:tnPortEtherHCOverPkts1519toMax.setUnits(_S)
_TnPortEtherHCPkts1519toMax_Type=Counter64
_TnPortEtherHCPkts1519toMax_Object=MibTableColumn
tnPortEtherHCPkts1519toMax=_TnPortEtherHCPkts1519toMax_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,19),_TnPortEtherHCPkts1519toMax_Type())
tnPortEtherHCPkts1519toMax.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortEtherHCPkts1519toMax.setStatus(_A)
if mibBuilder.loadTexts:tnPortEtherHCPkts1519toMax.setUnits(_S)
class _TnPortEtherLacpTunnel_Type(TruthValue):defaultValue=2
_TnPortEtherLacpTunnel_Type.__name__=_G
_TnPortEtherLacpTunnel_Object=MibTableColumn
tnPortEtherLacpTunnel=_TnPortEtherLacpTunnel_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,20),_TnPortEtherLacpTunnel_Type())
tnPortEtherLacpTunnel.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherLacpTunnel.setStatus(_A)
class _TnPortEtherDownWhenLoopedEnabled_Type(TruthValue):defaultValue=2
_TnPortEtherDownWhenLoopedEnabled_Type.__name__=_G
_TnPortEtherDownWhenLoopedEnabled_Object=MibTableColumn
tnPortEtherDownWhenLoopedEnabled=_TnPortEtherDownWhenLoopedEnabled_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,21),_TnPortEtherDownWhenLoopedEnabled_Type())
tnPortEtherDownWhenLoopedEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherDownWhenLoopedEnabled.setStatus(_A)
class _TnPortEtherDownWhenLoopedKeepAlive_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_TnPortEtherDownWhenLoopedKeepAlive_Type.__name__=_E
_TnPortEtherDownWhenLoopedKeepAlive_Object=MibTableColumn
tnPortEtherDownWhenLoopedKeepAlive=_TnPortEtherDownWhenLoopedKeepAlive_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,22),_TnPortEtherDownWhenLoopedKeepAlive_Type())
tnPortEtherDownWhenLoopedKeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherDownWhenLoopedKeepAlive.setStatus(_A)
if mibBuilder.loadTexts:tnPortEtherDownWhenLoopedKeepAlive.setUnits(_R)
class _TnPortEtherDownWhenLoopedRetry_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,160))
_TnPortEtherDownWhenLoopedRetry_Type.__name__=_E
_TnPortEtherDownWhenLoopedRetry_Object=MibTableColumn
tnPortEtherDownWhenLoopedRetry=_TnPortEtherDownWhenLoopedRetry_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,23),_TnPortEtherDownWhenLoopedRetry_Type())
tnPortEtherDownWhenLoopedRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherDownWhenLoopedRetry.setStatus(_A)
if mibBuilder.loadTexts:tnPortEtherDownWhenLoopedRetry.setUnits(_R)
class _TnPortEtherDownWhenLoopedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noLoopDetected',1),('loopDetected',2)))
_TnPortEtherDownWhenLoopedState_Type.__name__=_D
_TnPortEtherDownWhenLoopedState_Object=MibTableColumn
tnPortEtherDownWhenLoopedState=_TnPortEtherDownWhenLoopedState_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,24),_TnPortEtherDownWhenLoopedState_Type())
tnPortEtherDownWhenLoopedState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortEtherDownWhenLoopedState.setStatus(_A)
class _TnPortEtherPBBEtype_Type(Unsigned32):defaultValue=35047;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1536,65535))
_TnPortEtherPBBEtype_Type.__name__=_E
_TnPortEtherPBBEtype_Object=MibTableColumn
tnPortEtherPBBEtype=_TnPortEtherPBBEtype_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,25),_TnPortEtherPBBEtype_Type())
tnPortEtherPBBEtype.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherPBBEtype.setStatus(_A)
class _TnPortEtherSingleFiber_Type(TruthValue):defaultValue=2
_TnPortEtherSingleFiber_Type.__name__=_G
_TnPortEtherSingleFiber_Object=MibTableColumn
tnPortEtherSingleFiber=_TnPortEtherSingleFiber_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,27),_TnPortEtherSingleFiber_Type())
tnPortEtherSingleFiber.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherSingleFiber.setStatus(_A)
class _TnPortEtherSSM_Type(TruthValue):defaultValue=2
_TnPortEtherSSM_Type.__name__=_G
_TnPortEtherSSM_Object=MibTableColumn
tnPortEtherSSM=_TnPortEtherSSM_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,28),_TnPortEtherSSM_Type())
tnPortEtherSSM.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherSSM.setStatus(_A)
class _TnPortEtherDWLUseBroadcastAddr_Type(TruthValue):defaultValue=2
_TnPortEtherDWLUseBroadcastAddr_Type.__name__=_G
_TnPortEtherDWLUseBroadcastAddr_Object=MibTableColumn
tnPortEtherDWLUseBroadcastAddr=_TnPortEtherDWLUseBroadcastAddr_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,29),_TnPortEtherDWLUseBroadcastAddr_Type())
tnPortEtherDWLUseBroadcastAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherDWLUseBroadcastAddr.setStatus(_A)
class _TnPortEtherSSMCodeType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('sonet',2),('sdh',3)))
_TnPortEtherSSMCodeType_Type.__name__=_D
_TnPortEtherSSMCodeType_Object=MibTableColumn
tnPortEtherSSMCodeType=_TnPortEtherSSMCodeType_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,30),_TnPortEtherSSMCodeType_Type())
tnPortEtherSSMCodeType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherSSMCodeType.setStatus(_A)
class _TnPortEtherSSMTxDus_Type(TruthValue):defaultValue=2
_TnPortEtherSSMTxDus_Type.__name__=_G
_TnPortEtherSSMTxDus_Object=MibTableColumn
tnPortEtherSSMTxDus=_TnPortEtherSSMTxDus_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,31),_TnPortEtherSSMTxDus_Type())
tnPortEtherSSMTxDus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherSSMTxDus.setStatus(_A)
class _TnPortEtherSSMRxEsmc_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TnPortEtherSSMRxEsmc_Type.__name__=_E
_TnPortEtherSSMRxEsmc_Object=MibTableColumn
tnPortEtherSSMRxEsmc=_TnPortEtherSSMRxEsmc_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,32),_TnPortEtherSSMRxEsmc_Type())
tnPortEtherSSMRxEsmc.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortEtherSSMRxEsmc.setStatus(_A)
class _TnPortEtherSSMTxQualityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*(('reserved0',0),('prs',1),('stu',2),('st2',3),('tnc',4),('st3e',5),('reserved6',6),('smc',7),('reserved8',8),('dus',9),('prc',10),('ssua',11),('ssub',12),('reserved13',13),('dnu',14),('reserved15',15),('pno',16),('eec1',17),('eec2',18),('reserved19',19)))
_TnPortEtherSSMTxQualityLevel_Type.__name__=_D
_TnPortEtherSSMTxQualityLevel_Object=MibTableColumn
tnPortEtherSSMTxQualityLevel=_TnPortEtherSSMTxQualityLevel_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,33),_TnPortEtherSSMTxQualityLevel_Type())
tnPortEtherSSMTxQualityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortEtherSSMTxQualityLevel.setStatus(_A)
_TnPortEtherQinqEtypelink_Type=Unsigned32
_TnPortEtherQinqEtypelink_Object=MibTableColumn
tnPortEtherQinqEtypelink=_TnPortEtherQinqEtypelink_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,34),_TnPortEtherQinqEtypelink_Type())
tnPortEtherQinqEtypelink.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPortEtherQinqEtypelink.setStatus(_A)
class _TnPortEtherOperEgressRate_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,100000000))
_TnPortEtherOperEgressRate_Type.__name__=_D
_TnPortEtherOperEgressRate_Object=MibTableColumn
tnPortEtherOperEgressRate=_TnPortEtherOperEgressRate_Object((1,3,6,1,4,1,7483,6,1,2,2,4,4,1,35),_TnPortEtherOperEgressRate_Type())
tnPortEtherOperEgressRate.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortEtherOperEgressRate.setStatus(_A)
_TnPortScalarObjs_ObjectIdentity=ObjectIdentity
tnPortScalarObjs=_TnPortScalarObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,2,4,19))
_TnPortScalar1_Type=Unsigned32
_TnPortScalar1_Object=MibScalar
tnPortScalar1=_TnPortScalar1_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,11),_TnPortScalar1_Type())
tnPortScalar1.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar1.setStatus(_A)
_TnPortScalar2_Type=Unsigned32
_TnPortScalar2_Object=MibScalar
tnPortScalar2=_TnPortScalar2_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,12),_TnPortScalar2_Type())
tnPortScalar2.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar2.setStatus(_A)
_TnPortScalar3_Type=Unsigned32
_TnPortScalar3_Object=MibScalar
tnPortScalar3=_TnPortScalar3_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,13),_TnPortScalar3_Type())
tnPortScalar3.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar3.setStatus(_A)
_TnPortScalar4_Type=Unsigned32
_TnPortScalar4_Object=MibScalar
tnPortScalar4=_TnPortScalar4_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,14),_TnPortScalar4_Type())
tnPortScalar4.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar4.setStatus(_A)
_TnPortScalar5_Type=Unsigned32
_TnPortScalar5_Object=MibScalar
tnPortScalar5=_TnPortScalar5_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,15),_TnPortScalar5_Type())
tnPortScalar5.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar5.setStatus(_A)
_TnPortScalar6_Type=Unsigned32
_TnPortScalar6_Object=MibScalar
tnPortScalar6=_TnPortScalar6_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,16),_TnPortScalar6_Type())
tnPortScalar6.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar6.setStatus(_A)
_TnPortScalar7_Type=Unsigned32
_TnPortScalar7_Object=MibScalar
tnPortScalar7=_TnPortScalar7_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,17),_TnPortScalar7_Type())
tnPortScalar7.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar7.setStatus(_A)
_TnPortScalar8_Type=Unsigned32
_TnPortScalar8_Object=MibScalar
tnPortScalar8=_TnPortScalar8_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,18),_TnPortScalar8_Type())
tnPortScalar8.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar8.setStatus(_A)
_TnPortScalar9_Type=Unsigned32
_TnPortScalar9_Object=MibScalar
tnPortScalar9=_TnPortScalar9_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,19),_TnPortScalar9_Type())
tnPortScalar9.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar9.setStatus(_A)
_TnPortScalar10_Type=Unsigned32
_TnPortScalar10_Object=MibScalar
tnPortScalar10=_TnPortScalar10_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,20),_TnPortScalar10_Type())
tnPortScalar10.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar10.setStatus(_A)
_TnPortScalar11_Type=Unsigned32
_TnPortScalar11_Object=MibScalar
tnPortScalar11=_TnPortScalar11_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,21),_TnPortScalar11_Type())
tnPortScalar11.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar11.setStatus(_A)
_TnPortScalar12_Type=Unsigned32
_TnPortScalar12_Object=MibScalar
tnPortScalar12=_TnPortScalar12_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,22),_TnPortScalar12_Type())
tnPortScalar12.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar12.setStatus(_A)
_TnPortScalar13_Type=Unsigned32
_TnPortScalar13_Object=MibScalar
tnPortScalar13=_TnPortScalar13_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,23),_TnPortScalar13_Type())
tnPortScalar13.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar13.setStatus(_A)
_TnPortScalar14_Type=Unsigned32
_TnPortScalar14_Object=MibScalar
tnPortScalar14=_TnPortScalar14_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,24),_TnPortScalar14_Type())
tnPortScalar14.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar14.setStatus(_A)
_TnPortScalar15_Type=Unsigned32
_TnPortScalar15_Object=MibScalar
tnPortScalar15=_TnPortScalar15_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,25),_TnPortScalar15_Type())
tnPortScalar15.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar15.setStatus(_A)
_TnPortScalar16_Type=Unsigned32
_TnPortScalar16_Object=MibScalar
tnPortScalar16=_TnPortScalar16_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,26),_TnPortScalar16_Type())
tnPortScalar16.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar16.setStatus(_A)
_TnPortScalar17_Type=Unsigned32
_TnPortScalar17_Object=MibScalar
tnPortScalar17=_TnPortScalar17_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,27),_TnPortScalar17_Type())
tnPortScalar17.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar17.setStatus(_A)
_TnPortScalar18_Type=Unsigned32
_TnPortScalar18_Object=MibScalar
tnPortScalar18=_TnPortScalar18_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,28),_TnPortScalar18_Type())
tnPortScalar18.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar18.setStatus(_A)
_TnPortScalar19_Type=Unsigned32
_TnPortScalar19_Object=MibScalar
tnPortScalar19=_TnPortScalar19_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,29),_TnPortScalar19_Type())
tnPortScalar19.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar19.setStatus(_A)
_TnPortScalar20_Type=Unsigned32
_TnPortScalar20_Object=MibScalar
tnPortScalar20=_TnPortScalar20_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,30),_TnPortScalar20_Type())
tnPortScalar20.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar20.setStatus(_A)
_TnPortScalar21_Type=Unsigned32
_TnPortScalar21_Object=MibScalar
tnPortScalar21=_TnPortScalar21_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,31),_TnPortScalar21_Type())
tnPortScalar21.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar21.setStatus(_A)
_TnPortScalar22_Type=Unsigned32
_TnPortScalar22_Object=MibScalar
tnPortScalar22=_TnPortScalar22_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,32),_TnPortScalar22_Type())
tnPortScalar22.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar22.setStatus(_A)
_TnPortScalar23_Type=Unsigned32
_TnPortScalar23_Object=MibScalar
tnPortScalar23=_TnPortScalar23_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,33),_TnPortScalar23_Type())
tnPortScalar23.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar23.setStatus(_A)
_TnPortScalar24_Type=Unsigned32
_TnPortScalar24_Object=MibScalar
tnPortScalar24=_TnPortScalar24_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,34),_TnPortScalar24_Type())
tnPortScalar24.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar24.setStatus(_A)
_TnPortScalar25_Type=Unsigned32
_TnPortScalar25_Object=MibScalar
tnPortScalar25=_TnPortScalar25_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,35),_TnPortScalar25_Type())
tnPortScalar25.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar25.setStatus(_A)
_TnPortScalar26_Type=Unsigned32
_TnPortScalar26_Object=MibScalar
tnPortScalar26=_TnPortScalar26_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,36),_TnPortScalar26_Type())
tnPortScalar26.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar26.setStatus(_A)
_TnPortScalar27_Type=Unsigned32
_TnPortScalar27_Object=MibScalar
tnPortScalar27=_TnPortScalar27_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,37),_TnPortScalar27_Type())
tnPortScalar27.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar27.setStatus(_A)
_TnPortScalar28_Type=Unsigned32
_TnPortScalar28_Object=MibScalar
tnPortScalar28=_TnPortScalar28_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,38),_TnPortScalar28_Type())
tnPortScalar28.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar28.setStatus(_A)
_TnPortScalar29_Type=Unsigned32
_TnPortScalar29_Object=MibScalar
tnPortScalar29=_TnPortScalar29_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,39),_TnPortScalar29_Type())
tnPortScalar29.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar29.setStatus(_A)
_TnPortScalar30_Type=Unsigned32
_TnPortScalar30_Object=MibScalar
tnPortScalar30=_TnPortScalar30_Object((1,3,6,1,4,1,7483,6,1,2,2,4,19,40),_TnPortScalar30_Type())
tnPortScalar30.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPortScalar30.setStatus(_A)
_TnPacketSwitchPortTable_Object=MibTable
tnPacketSwitchPortTable=_TnPacketSwitchPortTable_Object((1,3,6,1,4,1,7483,6,1,2,2,4,99))
if mibBuilder.loadTexts:tnPacketSwitchPortTable.setStatus(_A)
_TnPacketSwitchPortEntry_Object=MibTableRow
tnPacketSwitchPortEntry=_TnPacketSwitchPortEntry_Object((1,3,6,1,4,1,7483,6,1,2,2,4,99,1))
tnPacketSwitchPortEntry.setIndexNames((0,_L,_M),(0,_F,_N))
if mibBuilder.loadTexts:tnPacketSwitchPortEntry.setStatus(_A)
_TnPacketSwitchPortName_Type=TNamedItemOrEmpty
_TnPacketSwitchPortName_Object=MibTableColumn
tnPacketSwitchPortName=_TnPacketSwitchPortName_Object((1,3,6,1,4,1,7483,6,1,2,2,4,99,1,1),_TnPacketSwitchPortName_Type())
tnPacketSwitchPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketSwitchPortName.setStatus(_A)
_TnEMACTable_Object=MibTable
tnEMACTable=_TnEMACTable_Object((1,3,6,1,4,1,7483,6,1,2,2,4,100))
if mibBuilder.loadTexts:tnEMACTable.setStatus(_A)
_TnEMACEntry_Object=MibTableRow
tnEMACEntry=_TnEMACEntry_Object((1,3,6,1,4,1,7483,6,1,2,2,4,100,1))
tnEMACEntry.setIndexNames((0,_L,_M),(0,_F,_j))
if mibBuilder.loadTexts:tnEMACEntry.setStatus(_A)
_TnEMACID_Type=TmnxPortID
_TnEMACID_Object=MibTableColumn
tnEMACID=_TnEMACID_Object((1,3,6,1,4,1,7483,6,1,2,2,4,100,1,1),_TnEMACID_Type())
tnEMACID.setMaxAccess(_J)
if mibBuilder.loadTexts:tnEMACID.setStatus(_A)
class _TnEMACAcctPolicyId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_TnEMACAcctPolicyId_Type.__name__=_E
_TnEMACAcctPolicyId_Object=MibTableColumn
tnEMACAcctPolicyId=_TnEMACAcctPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,2,4,100,1,2),_TnEMACAcctPolicyId_Type())
tnEMACAcctPolicyId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEMACAcctPolicyId.setStatus(_A)
_TnPMACTable_Object=MibTable
tnPMACTable=_TnPMACTable_Object((1,3,6,1,4,1,7483,6,1,2,2,4,101))
if mibBuilder.loadTexts:tnPMACTable.setStatus(_A)
_TnPMACEntry_Object=MibTableRow
tnPMACEntry=_TnPMACEntry_Object((1,3,6,1,4,1,7483,6,1,2,2,4,101,1))
tnPMACEntry.setIndexNames((0,_L,_M),(0,_F,_k))
if mibBuilder.loadTexts:tnPMACEntry.setStatus(_A)
_TnPMACID_Type=TmnxPortID
_TnPMACID_Object=MibTableColumn
tnPMACID=_TnPMACID_Object((1,3,6,1,4,1,7483,6,1,2,2,4,101,1,1),_TnPMACID_Type())
tnPMACID.setMaxAccess(_J)
if mibBuilder.loadTexts:tnPMACID.setStatus(_A)
class _TnPMACAcctPolicyId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_TnPMACAcctPolicyId_Type.__name__=_E
_TnPMACAcctPolicyId_Object=MibTableColumn
tnPMACAcctPolicyId=_TnPMACAcctPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,2,4,101,1,2),_TnPMACAcctPolicyId_Type())
tnPMACAcctPolicyId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnPMACAcctPolicyId.setStatus(_A)
_TnMMACTable_Object=MibTable
tnMMACTable=_TnMMACTable_Object((1,3,6,1,4,1,7483,6,1,2,2,4,102))
if mibBuilder.loadTexts:tnMMACTable.setStatus(_A)
_TnMMACEntry_Object=MibTableRow
tnMMACEntry=_TnMMACEntry_Object((1,3,6,1,4,1,7483,6,1,2,2,4,102,1))
tnMMACEntry.setIndexNames((0,_L,_M),(0,_F,_l))
if mibBuilder.loadTexts:tnMMACEntry.setStatus(_A)
_TnMMACID_Type=TmnxPortID
_TnMMACID_Object=MibTableColumn
tnMMACID=_TnMMACID_Object((1,3,6,1,4,1,7483,6,1,2,2,4,102,1,1),_TnMMACID_Type())
tnMMACID.setMaxAccess(_J)
if mibBuilder.loadTexts:tnMMACID.setStatus(_A)
class _TnMMACAcctPolicyId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_TnMMACAcctPolicyId_Type.__name__=_E
_TnMMACAcctPolicyId_Object=MibTableColumn
tnMMACAcctPolicyId=_TnMMACAcctPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,2,4,102,1,2),_TnMMACAcctPolicyId_Type())
tnMMACAcctPolicyId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnMMACAcctPolicyId.setStatus(_A)
_TnQosAppObjs_ObjectIdentity=ObjectIdentity
tnQosAppObjs=_TnQosAppObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,2,10))
_TnQosPoolAppTable_Object=MibTable
tnQosPoolAppTable=_TnQosPoolAppTable_Object((1,3,6,1,4,1,7483,6,1,2,2,10,2))
if mibBuilder.loadTexts:tnQosPoolAppTable.setStatus(_A)
_TnQosPoolAppEntry_Object=MibTableRow
tnQosPoolAppEntry=_TnQosPoolAppEntry_Object((1,3,6,1,4,1,7483,6,1,2,2,10,2,1))
tnQosPoolAppEntry.setIndexNames((0,_F,_m),(0,_F,_n),(0,_F,_o),(0,_F,_p))
if mibBuilder.loadTexts:tnQosPoolAppEntry.setStatus(_A)
class _TnObjectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,51)));namedValues=NamedValues(*(('mda',1),('port',2),('channel',3),('bundle',4),('mpointQueues',51)))
_TnObjectType_Type.__name__=_D
_TnObjectType_Object=MibTableColumn
tnObjectType=_TnObjectType_Object((1,3,6,1,4,1,7483,6,1,2,2,10,2,1,1),_TnObjectType_Type())
tnObjectType.setMaxAccess(_J)
if mibBuilder.loadTexts:tnObjectType.setStatus(_A)
_TnObjectId_Type=TmnxPortID
_TnObjectId_Object=MibTableColumn
tnObjectId=_TnObjectId_Object((1,3,6,1,4,1,7483,6,1,2,2,10,2,1,2),_TnObjectId_Type())
tnObjectId.setMaxAccess(_J)
if mibBuilder.loadTexts:tnObjectId.setStatus(_A)
class _TnObjectAppType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,51)));namedValues=NamedValues(*(('accessIngress',1),('accessEgress',2),('networkIngress',3),('networkEgress',4),('system',51)))
_TnObjectAppType_Type.__name__=_D
_TnObjectAppType_Object=MibTableColumn
tnObjectAppType=_TnObjectAppType_Object((1,3,6,1,4,1,7483,6,1,2,2,10,2,1,3),_TnObjectAppType_Type())
tnObjectAppType.setMaxAccess(_J)
if mibBuilder.loadTexts:tnObjectAppType.setStatus(_A)
_TnObjectAppPool_Type=TNamedItem
_TnObjectAppPool_Object=MibTableColumn
tnObjectAppPool=_TnObjectAppPool_Object((1,3,6,1,4,1,7483,6,1,2,2,10,2,1,4),_TnObjectAppPool_Type())
tnObjectAppPool.setMaxAccess(_J)
if mibBuilder.loadTexts:tnObjectAppPool.setStatus(_A)
_TnObjectAppPoolRowStatus_Type=RowStatus
_TnObjectAppPoolRowStatus_Object=MibTableColumn
tnObjectAppPoolRowStatus=_TnObjectAppPoolRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,2,10,2,1,5),_TnObjectAppPoolRowStatus_Type())
tnObjectAppPoolRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnObjectAppPoolRowStatus.setStatus(_A)
class _TnObjectAppResvCbs_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,100))
_TnObjectAppResvCbs_Type.__name__=_D
_TnObjectAppResvCbs_Object=MibTableColumn
tnObjectAppResvCbs=_TnObjectAppResvCbs_Object((1,3,6,1,4,1,7483,6,1,2,2,10,2,1,6),_TnObjectAppResvCbs_Type())
tnObjectAppResvCbs.setMaxAccess(_C)
if mibBuilder.loadTexts:tnObjectAppResvCbs.setStatus(_A)
class _TnObjectAppSlopePolicy_Type(TNamedItem):defaultValue=OctetString(_e)
_TnObjectAppSlopePolicy_Type.__name__=_V
_TnObjectAppSlopePolicy_Object=MibTableColumn
tnObjectAppSlopePolicy=_TnObjectAppSlopePolicy_Object((1,3,6,1,4,1,7483,6,1,2,2,10,2,1,7),_TnObjectAppSlopePolicy_Type())
tnObjectAppSlopePolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:tnObjectAppSlopePolicy.setStatus(_A)
class _TnObjectAppPoolSize_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,100))
_TnObjectAppPoolSize_Type.__name__=_D
_TnObjectAppPoolSize_Object=MibTableColumn
tnObjectAppPoolSize=_TnObjectAppPoolSize_Object((1,3,6,1,4,1,7483,6,1,2,2,10,2,1,8),_TnObjectAppPoolSize_Type())
tnObjectAppPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:tnObjectAppPoolSize.setStatus(_A)
_TnHwNotification_ObjectIdentity=ObjectIdentity
tnHwNotification=_TnHwNotification_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,2))
_TnPortNotifyPrefix_ObjectIdentity=ObjectIdentity
tnPortNotifyPrefix=_TnPortNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,2,2))
_TnPortNotification_ObjectIdentity=ObjectIdentity
tnPortNotification=_TnPortNotification_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,2,2,0))
tnPortEntry.registerAugmentions((_F,_q))
tnPortTestEntry.setIndexNames(*tnPortEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'TmnxPortOperStatus':TmnxPortOperStatus,_i:TmnxPortEtherReportStatus,'TmnxPortClass':TmnxPortClass,'TmnxPortConnectorType':TmnxPortConnectorType,'TmnxPortState':TmnxPortState,'TmnxPortType':TmnxPortType,'TmnxAlarmState':TmnxAlarmState,_d:TmnxPortAdminStatus,'tnPortMIBModule':tnPortMIBModule,'tnHwObjs':tnHwObjs,'tnPortObjs':tnPortObjs,'tnPortTableLastChange':tnPortTableLastChange,'tnPortTable':tnPortTable,'tnPortEntry':tnPortEntry,_N:tnPortPortID,'tnPortLastChangeTime':tnPortLastChangeTime,'tnPortType':tnPortType,'tnPortClass':tnPortClass,'tnPortDescription':tnPortDescription,'tnPortName':tnPortName,'tnPortAlias':tnPortAlias,'tnPortUserAssignedMac':tnPortUserAssignedMac,'tnPortMacAddress':tnPortMacAddress,'tnPortHwMacAddress':tnPortHwMacAddress,'tnPortMode':tnPortMode,'tnPortEncapType':tnPortEncapType,'tnPortLagId':tnPortLagId,'tnPortHoldTimeUp':tnPortHoldTimeUp,'tnPortHoldTimeDown':tnPortHoldTimeDown,'tnPortUpProtocols':tnPortUpProtocols,'tnPortConnectorType':tnPortConnectorType,'tnPortTransceiverType':tnPortTransceiverType,'tnPortTransceiverLaserWaveLen':tnPortTransceiverLaserWaveLen,'tnPortTransceiverDiagCapable':tnPortTransceiverDiagCapable,'tnPortTransceiverModelNumber':tnPortTransceiverModelNumber,'tnPortSFPConnectorCode':tnPortSFPConnectorCode,'tnPortSFPVendorOUI':tnPortSFPVendorOUI,'tnPortSFPVendorManufactureDate':tnPortSFPVendorManufactureDate,'tnPortSFPMedia':tnPortSFPMedia,'tnPortSFPEquipped':tnPortSFPEquipped,'tnPortEquipped':tnPortEquipped,'tnPortLinkStatus':tnPortLinkStatus,'tnPortAdminStatus':tnPortAdminStatus,'tnPortOperStatus':tnPortOperStatus,'tnPortState':tnPortState,'tnPortPrevState':tnPortPrevState,'tnPortNumAlarms':tnPortNumAlarms,'tnPortAlarmState':tnPortAlarmState,'tnPortLastAlarmEvent':tnPortLastAlarmEvent,'tnPortClearAlarms':tnPortClearAlarms,'tnPortSFPVendorSerialNum':tnPortSFPVendorSerialNum,'tnPortSFPVendorPartNum':tnPortSFPVendorPartNum,'tnPortLastStateChanged':tnPortLastStateChanged,'tnPortNumChannels':tnPortNumChannels,'tnPortNetworkEgrQueues':tnPortNetworkEgrQueues,'tnPortBundleNumber':tnPortBundleNumber,'tnPortIsLeaf':tnPortIsLeaf,'tnPortParentPortID':tnPortParentPortID,'tnPortOpticalCompliance':tnPortOpticalCompliance,'tnPortLoadBalanceAlgorithm':tnPortLoadBalanceAlgorithm,'tnPortEgrPortSchedPlcy':tnPortEgrPortSchedPlcy,'tnPortLastClearedTime':tnPortLastClearedTime,'tnPortEgrHsmdaSchedPlcy':tnPortEgrHsmdaSchedPlcy,'tnPortIngNamedPoolPlcy':tnPortIngNamedPoolPlcy,'tnPortEgrNamedPoolPlcy':tnPortEgrNamedPoolPlcy,'tnPortIngPoolPercentRate':tnPortIngPoolPercentRate,'tnPortEgrPoolPercentRate':tnPortEgrPoolPercentRate,'tnPortDDMEventSuppression':tnPortDDMEventSuppression,'tnPortSFPStatus':tnPortSFPStatus,'tnPortReasonDownFlags':tnPortReasonDownFlags,'tnPortSSMRxQualityLevel':tnPortSSMRxQualityLevel,'tnPortDwdmLaserChannel':tnPortDwdmLaserChannel,'tnPortOtuCapable':tnPortOtuCapable,'tnPortHoldTimeUnits':tnPortHoldTimeUnits,'tnPortLinkLengthInfo':tnPortLinkLengthInfo,'tnPortSFPNumLanes':tnPortSFPNumLanes,'tnPortPhysStateChangeCount':tnPortPhysStateChangeCount,'tnPortPacketSwitchId':tnPortPacketSwitchId,'tnPortOtnSignalDegrade':tnPortOtnSignalDegrade,'tnPortTestTable':tnPortTestTable,_q:tnPortTestEntry,'tnPortTestState':tnPortTestState,'tnPortTestMode':tnPortTestMode,'tnPortTestParameter':tnPortTestParameter,'tnPortTestLastResult':tnPortTestLastResult,'tnPortTestStartTime':tnPortTestStartTime,'tnPortTestEndTime':tnPortTestEndTime,'tnPortTestDuration':tnPortTestDuration,'tnPortTestAction':tnPortTestAction,'tnPortEtherTable':tnPortEtherTable,'tnPortEtherEntry':tnPortEtherEntry,'tnPortEtherMTU':tnPortEtherMTU,'tnPortEtherDuplex':tnPortEtherDuplex,'tnPortEtherSpeed':tnPortEtherSpeed,'tnPortEtherAutoNegotiate':tnPortEtherAutoNegotiate,'tnPortEtherOperDuplex':tnPortEtherOperDuplex,'tnPortEtherOperSpeed':tnPortEtherOperSpeed,'tnPortEtherAcctPolicyId':tnPortEtherAcctPolicyId,'tnPortEtherCollectStats':tnPortEtherCollectStats,'tnPortEtherMDIMDIX':tnPortEtherMDIMDIX,'tnPortEtherXGigMode':tnPortEtherXGigMode,'tnPortEtherEgressRate':tnPortEtherEgressRate,'tnPortEtherDot1qEtype':tnPortEtherDot1qEtype,'tnPortEtherQinqEtype':tnPortEtherQinqEtype,'tnPortEtherIngressRate':tnPortEtherIngressRate,'tnPortEtherReportAlarm':tnPortEtherReportAlarm,'tnPortEtherReportAlarmStatus':tnPortEtherReportAlarmStatus,'tnPortEtherPkts1519toMax':tnPortEtherPkts1519toMax,'tnPortEtherHCOverPkts1519toMax':tnPortEtherHCOverPkts1519toMax,'tnPortEtherHCPkts1519toMax':tnPortEtherHCPkts1519toMax,'tnPortEtherLacpTunnel':tnPortEtherLacpTunnel,'tnPortEtherDownWhenLoopedEnabled':tnPortEtherDownWhenLoopedEnabled,'tnPortEtherDownWhenLoopedKeepAlive':tnPortEtherDownWhenLoopedKeepAlive,'tnPortEtherDownWhenLoopedRetry':tnPortEtherDownWhenLoopedRetry,'tnPortEtherDownWhenLoopedState':tnPortEtherDownWhenLoopedState,'tnPortEtherPBBEtype':tnPortEtherPBBEtype,'tnPortEtherSingleFiber':tnPortEtherSingleFiber,'tnPortEtherSSM':tnPortEtherSSM,'tnPortEtherDWLUseBroadcastAddr':tnPortEtherDWLUseBroadcastAddr,'tnPortEtherSSMCodeType':tnPortEtherSSMCodeType,'tnPortEtherSSMTxDus':tnPortEtherSSMTxDus,'tnPortEtherSSMRxEsmc':tnPortEtherSSMRxEsmc,'tnPortEtherSSMTxQualityLevel':tnPortEtherSSMTxQualityLevel,'tnPortEtherQinqEtypelink':tnPortEtherQinqEtypelink,'tnPortEtherOperEgressRate':tnPortEtherOperEgressRate,'tnPortScalarObjs':tnPortScalarObjs,'tnPortScalar1':tnPortScalar1,'tnPortScalar2':tnPortScalar2,'tnPortScalar3':tnPortScalar3,'tnPortScalar4':tnPortScalar4,'tnPortScalar5':tnPortScalar5,'tnPortScalar6':tnPortScalar6,'tnPortScalar7':tnPortScalar7,'tnPortScalar8':tnPortScalar8,'tnPortScalar9':tnPortScalar9,'tnPortScalar10':tnPortScalar10,'tnPortScalar11':tnPortScalar11,'tnPortScalar12':tnPortScalar12,'tnPortScalar13':tnPortScalar13,'tnPortScalar14':tnPortScalar14,'tnPortScalar15':tnPortScalar15,'tnPortScalar16':tnPortScalar16,'tnPortScalar17':tnPortScalar17,'tnPortScalar18':tnPortScalar18,'tnPortScalar19':tnPortScalar19,'tnPortScalar20':tnPortScalar20,'tnPortScalar21':tnPortScalar21,'tnPortScalar22':tnPortScalar22,'tnPortScalar23':tnPortScalar23,'tnPortScalar24':tnPortScalar24,'tnPortScalar25':tnPortScalar25,'tnPortScalar26':tnPortScalar26,'tnPortScalar27':tnPortScalar27,'tnPortScalar28':tnPortScalar28,'tnPortScalar29':tnPortScalar29,'tnPortScalar30':tnPortScalar30,'tnPacketSwitchPortTable':tnPacketSwitchPortTable,'tnPacketSwitchPortEntry':tnPacketSwitchPortEntry,'tnPacketSwitchPortName':tnPacketSwitchPortName,'tnEMACTable':tnEMACTable,'tnEMACEntry':tnEMACEntry,_j:tnEMACID,'tnEMACAcctPolicyId':tnEMACAcctPolicyId,'tnPMACTable':tnPMACTable,'tnPMACEntry':tnPMACEntry,_k:tnPMACID,'tnPMACAcctPolicyId':tnPMACAcctPolicyId,'tnMMACTable':tnMMACTable,'tnMMACEntry':tnMMACEntry,_l:tnMMACID,'tnMMACAcctPolicyId':tnMMACAcctPolicyId,'tnQosAppObjs':tnQosAppObjs,'tnQosPoolAppTable':tnQosPoolAppTable,'tnQosPoolAppEntry':tnQosPoolAppEntry,_m:tnObjectType,_n:tnObjectId,_o:tnObjectAppType,_p:tnObjectAppPool,'tnObjectAppPoolRowStatus':tnObjectAppPoolRowStatus,'tnObjectAppResvCbs':tnObjectAppResvCbs,'tnObjectAppSlopePolicy':tnObjectAppSlopePolicy,'tnObjectAppPoolSize':tnObjectAppPoolSize,'tnHwNotification':tnHwNotification,'tnPortNotifyPrefix':tnPortNotifyPrefix,'tnPortNotification':tnPortNotification})