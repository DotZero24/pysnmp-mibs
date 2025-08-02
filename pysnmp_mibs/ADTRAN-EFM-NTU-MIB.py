_AZ='adGenEfmNtuAutoDiscover'
_AY='adGenEfmNtuCustIfDownAct'
_AX='adGenEfmNtuCustIfDownClr'
_AW='adGenEfmNtuMACTableExhaust'
_AV='adGenEfmNtuCorruptConfiguration'
_AU='adGenEfmNtuSwDownloadFail'
_AT='adGenEfmNtuCraftLoginFail'
_AS='adGenEfmNtuCraftLoginSuccess'
_AR='adGenEfmNtuPerfCustIfRxDiscardedFrames'
_AQ='adGenEfmNtuPerfCustIfRxErroredFrames'
_AP='adGenEfmNtuPerfCustIfRxFrames'
_AO='adGenEfmNtuPerfCustIfRxOctets'
_AN='adGenEfmNtuPerfCustIfTxFrames'
_AM='adGenEfmNtuPerfCustIfTxOctets'
_AL='adGenEfmNtuStatCustIf'
_AK='adGenEfmNtuStatLinkStateAware'
_AJ='adGenEfmNtuStatUpTime'
_AI='adGenEfmNtuProvMgmtAutoConfigHostIpv6'
_AH='adGenEfmNtuProvMgmtAutoConfigHostIpv4'
_AG='adGenEfmNtuProvMgmtAutoConfigGroupName'
_AF='adGenEfmNtuProvMgmtAutoConfigFilename'
_AE='adGenEfmNtuProvMgmtAutoConfigMode'
_AD='adGenEfmNtuProvMgmtIpv6AddressLinkLocal'
_AC='adGenEfmNtuProvMgmtIpv6Address'
_AB='adGenEfmNtuProvMgmtIpv6AddressEui64'
_AA='adGenEfmNtuProvMgmtIpv6AddressPrefixLength'
_A9='adGenEfmNtuProvMgmtEzProvEnabled'
_A8='adGenEfmNtuProvMgmtEzProvHostTwoTrapVersion'
_A7='adGenEfmNtuProvMgmtEzProvHostTwoIpAddress'
_A6='adGenEfmNtuProvMgmtEzProvHostOneTrapVersion'
_A5='adGenEfmNtuProvMgmtEzProvHostOneIpAddress'
_A4='adGenEfmNtuProvMgmtSnmpSysLocation'
_A3='adGenEfmNtuProvMgmtPriority'
_A2='adGenEfmNtuProvMgmtSnmpReadCommunity'
_A1='adGenEfmNtuProvMgmtSnmpWriteCommunity'
_A0='adGenEfmNtuProvMgmtFarEndSysName'
_z='adGenEfmNtuProvMgmtFarEndIpAddress'
_y='adGenEfmNtuProvMgmtFarEndIfIndex'
_x='adGenEfmNtuProvMgmtSysName'
_w='adGenEfmNtuProvMgmtTftpServer'
_v='adGenEfmNtuProvMgmtIpVlan'
_u='adGenEfmNtuProvMgmtIpGateway'
_t='adGenEfmNtuProvMgmtIpSubnetMask'
_s='adGenEfmNtuProvMgmtIpAddress'
_r='adGenEfmNtuProvCfmMepEntryStatus'
_q='adGenEfmNtuProvCfmMepId'
_p='adGenEfmNtuProvCfmMepTableNextIndex'
_o='adGenEfmNtuProvCfmCcmInterval'
_n='adGenEfmNtuProvCfmVlanId'
_m='adGenEfmNtuProvCfmMdLevel'
_l='adGenEfmNtuProvCfmLocalMepId'
_k='adGenEfmNtuProvCfmMaName'
_j='adGenEfmNtuProvCfmMdName'
_i='adGenEfmNtuAutoDiscoverAck'
_h='adGenEfmNtuAutoDiscoverMode'
_g='adGenEfmNtuProvLinkStateAware'
_f='adGenEfmNtuProvMacAging'
_e='adGenEfmNtuProvMacTableSize'
_d='adGenEfmNtuProvEnablePassword'
_c='adGenEfmNtuProvCustIfFlowControl'
_b='adGenEfmNtuProvCustIfDuplex'
_a='adGenEfmNtuProvCustIfSpeed'
_Z='adGenEfmNtuProvCustIfAutoNeg'
_Y='adGenEfmNtuProvSwDownloadFilename'
_X='adGenEfmNtuProvSwDownloadStart'
_W='adGenEfmNtuProvReset'
_V='adGenEfmNtuProvRestoreDefaults'
_U='ifDescr'
_T='adGenEfmNtuProvSwDownloadStatus'
_S='adGenEfmNtuProvCfmMepIndex'
_R='disable'
_Q='enable'
_P='DisplayString'
_O='TruthValue'
_N='ifIndex'
_M='adGenEfmNtuProvCustId'
_L='sysName'
_K='SNMPv2-MIB'
_J='IF-MIB'
_I='adTrapInformSeqNum'
_H='ADTRAN-GENTRAPINFORM-MIB'
_G='adGenSlotInfoIndex'
_F='ADTRAN-GENSLOT-MIB'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='ADTRAN-EFM-NTU-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPortTrapIdentifier,=mibBuilder.importSymbols('ADTRAN-GENPORT-MIB','adGenPortTrapIdentifier')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_F,_G)
adTrapInformSeqNum,=mibBuilder.importSymbols(_H,_I)
AdGenTrapVersion,=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-TC-MIB','AdGenTrapVersion')
adGenEfmNtu,adGenEfmNtuID=mibBuilder.importSymbols('ADTRAN-SHARED-EFM-MIB','adGenEfmNtu','adGenEfmNtuID')
EntryStatus,=mibBuilder.importSymbols('ADTRAN-TC','EntryStatus')
InterfaceIndex,ifDescr,ifIndex=mibBuilder.importSymbols(_J,'InterfaceIndex',_U,_N)
InetAddressIPv4,InetAddressIPv6,InetAddressPrefixLength=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6','InetAddressPrefixLength')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_K,_L)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_P,'PhysAddress','TextualConvention',_O)
adGenEfmNtuMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,66,2,1))
if mibBuilder.loadTexts:adGenEfmNtuMIB.setRevisions(('2014-09-22 00:00','2014-05-16 00:00','2007-08-31 00:00'))
_AdGenEfmNtuConfiguration_ObjectIdentity=ObjectIdentity
adGenEfmNtuConfiguration=_AdGenEfmNtuConfiguration_ObjectIdentity((1,3,6,1,4,1,664,5,66,2,1))
_AdGenEfmNtuProvisioning_ObjectIdentity=ObjectIdentity
adGenEfmNtuProvisioning=_AdGenEfmNtuProvisioning_ObjectIdentity((1,3,6,1,4,1,664,5,66,2,2))
_AdGenEfmNtuProvTable_Object=MibTable
adGenEfmNtuProvTable=_AdGenEfmNtuProvTable_Object((1,3,6,1,4,1,664,5,66,2,2,1))
if mibBuilder.loadTexts:adGenEfmNtuProvTable.setStatus(_A)
_AdGenEfmNtuProvEntry_Object=MibTableRow
adGenEfmNtuProvEntry=_AdGenEfmNtuProvEntry_Object((1,3,6,1,4,1,664,5,66,2,2,1,1))
adGenEfmNtuProvEntry.setIndexNames((0,_J,_N))
if mibBuilder.loadTexts:adGenEfmNtuProvEntry.setStatus(_A)
class _AdGenEfmNtuProvRestoreDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('restoreDefaults',1))
_AdGenEfmNtuProvRestoreDefaults_Type.__name__=_E
_AdGenEfmNtuProvRestoreDefaults_Object=MibTableColumn
adGenEfmNtuProvRestoreDefaults=_AdGenEfmNtuProvRestoreDefaults_Object((1,3,6,1,4,1,664,5,66,2,2,1,1,1),_AdGenEfmNtuProvRestoreDefaults_Type())
adGenEfmNtuProvRestoreDefaults.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvRestoreDefaults.setStatus(_A)
class _AdGenEfmNtuProvReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_AdGenEfmNtuProvReset_Type.__name__=_E
_AdGenEfmNtuProvReset_Object=MibTableColumn
adGenEfmNtuProvReset=_AdGenEfmNtuProvReset_Object((1,3,6,1,4,1,664,5,66,2,2,1,1,2),_AdGenEfmNtuProvReset_Type())
adGenEfmNtuProvReset.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvReset.setStatus(_A)
class _AdGenEfmNtuProvSwDownloadStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('start',1))
_AdGenEfmNtuProvSwDownloadStart_Type.__name__=_E
_AdGenEfmNtuProvSwDownloadStart_Object=MibTableColumn
adGenEfmNtuProvSwDownloadStart=_AdGenEfmNtuProvSwDownloadStart_Object((1,3,6,1,4,1,664,5,66,2,2,1,1,3),_AdGenEfmNtuProvSwDownloadStart_Type())
adGenEfmNtuProvSwDownloadStart.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvSwDownloadStart.setStatus(_A)
_AdGenEfmNtuProvSwDownloadFilename_Type=OctetString
_AdGenEfmNtuProvSwDownloadFilename_Object=MibTableColumn
adGenEfmNtuProvSwDownloadFilename=_AdGenEfmNtuProvSwDownloadFilename_Object((1,3,6,1,4,1,664,5,66,2,2,1,1,4),_AdGenEfmNtuProvSwDownloadFilename_Type())
adGenEfmNtuProvSwDownloadFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvSwDownloadFilename.setStatus(_A)
_AdGenEfmNtuProvSwDownloadStatus_Type=OctetString
_AdGenEfmNtuProvSwDownloadStatus_Object=MibTableColumn
adGenEfmNtuProvSwDownloadStatus=_AdGenEfmNtuProvSwDownloadStatus_Object((1,3,6,1,4,1,664,5,66,2,2,1,1,5),_AdGenEfmNtuProvSwDownloadStatus_Type())
adGenEfmNtuProvSwDownloadStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEfmNtuProvSwDownloadStatus.setStatus(_A)
_AdGenEfmNtuProvCustId_Type=OctetString
_AdGenEfmNtuProvCustId_Object=MibTableColumn
adGenEfmNtuProvCustId=_AdGenEfmNtuProvCustId_Object((1,3,6,1,4,1,664,5,66,2,2,1,1,6),_AdGenEfmNtuProvCustId_Type())
adGenEfmNtuProvCustId.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvCustId.setStatus(_A)
class _AdGenEfmNtuProvCustIfAutoNeg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_AdGenEfmNtuProvCustIfAutoNeg_Type.__name__=_E
_AdGenEfmNtuProvCustIfAutoNeg_Object=MibTableColumn
adGenEfmNtuProvCustIfAutoNeg=_AdGenEfmNtuProvCustIfAutoNeg_Object((1,3,6,1,4,1,664,5,66,2,2,1,1,7),_AdGenEfmNtuProvCustIfAutoNeg_Type())
adGenEfmNtuProvCustIfAutoNeg.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvCustIfAutoNeg.setStatus(_A)
class _AdGenEfmNtuProvCustIfSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tenBaseT',1),('hundredBaseT',2)))
_AdGenEfmNtuProvCustIfSpeed_Type.__name__=_E
_AdGenEfmNtuProvCustIfSpeed_Object=MibTableColumn
adGenEfmNtuProvCustIfSpeed=_AdGenEfmNtuProvCustIfSpeed_Object((1,3,6,1,4,1,664,5,66,2,2,1,1,8),_AdGenEfmNtuProvCustIfSpeed_Type())
adGenEfmNtuProvCustIfSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvCustIfSpeed.setStatus(_A)
class _AdGenEfmNtuProvCustIfDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('halfDuplex',1),('fullDuplex',2)))
_AdGenEfmNtuProvCustIfDuplex_Type.__name__=_E
_AdGenEfmNtuProvCustIfDuplex_Object=MibTableColumn
adGenEfmNtuProvCustIfDuplex=_AdGenEfmNtuProvCustIfDuplex_Object((1,3,6,1,4,1,664,5,66,2,2,1,1,9),_AdGenEfmNtuProvCustIfDuplex_Type())
adGenEfmNtuProvCustIfDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvCustIfDuplex.setStatus(_A)
class _AdGenEfmNtuProvCustIfFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_AdGenEfmNtuProvCustIfFlowControl_Type.__name__=_E
_AdGenEfmNtuProvCustIfFlowControl_Object=MibTableColumn
adGenEfmNtuProvCustIfFlowControl=_AdGenEfmNtuProvCustIfFlowControl_Object((1,3,6,1,4,1,664,5,66,2,2,1,1,10),_AdGenEfmNtuProvCustIfFlowControl_Type())
adGenEfmNtuProvCustIfFlowControl.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvCustIfFlowControl.setStatus(_A)
_AdGenEfmNtuProvEnablePassword_Type=OctetString
_AdGenEfmNtuProvEnablePassword_Object=MibTableColumn
adGenEfmNtuProvEnablePassword=_AdGenEfmNtuProvEnablePassword_Object((1,3,6,1,4,1,664,5,66,2,2,1,1,11),_AdGenEfmNtuProvEnablePassword_Type())
adGenEfmNtuProvEnablePassword.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvEnablePassword.setStatus(_A)
_AdGenEfmNtuProvMacTableSize_Type=Integer32
_AdGenEfmNtuProvMacTableSize_Object=MibTableColumn
adGenEfmNtuProvMacTableSize=_AdGenEfmNtuProvMacTableSize_Object((1,3,6,1,4,1,664,5,66,2,2,1,1,12),_AdGenEfmNtuProvMacTableSize_Type())
adGenEfmNtuProvMacTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMacTableSize.setStatus(_A)
_AdGenEfmNtuProvMacAging_Type=Integer32
_AdGenEfmNtuProvMacAging_Object=MibTableColumn
adGenEfmNtuProvMacAging=_AdGenEfmNtuProvMacAging_Object((1,3,6,1,4,1,664,5,66,2,2,1,1,13),_AdGenEfmNtuProvMacAging_Type())
adGenEfmNtuProvMacAging.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMacAging.setStatus(_A)
class _AdGenEfmNtuProvLinkStateAware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_AdGenEfmNtuProvLinkStateAware_Type.__name__=_E
_AdGenEfmNtuProvLinkStateAware_Object=MibTableColumn
adGenEfmNtuProvLinkStateAware=_AdGenEfmNtuProvLinkStateAware_Object((1,3,6,1,4,1,664,5,66,2,2,1,1,14),_AdGenEfmNtuProvLinkStateAware_Type())
adGenEfmNtuProvLinkStateAware.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvLinkStateAware.setStatus(_A)
class _AdGenEfmNtuAutoDiscoverMode_Type(TruthValue):defaultValue=2
_AdGenEfmNtuAutoDiscoverMode_Type.__name__=_O
_AdGenEfmNtuAutoDiscoverMode_Object=MibTableColumn
adGenEfmNtuAutoDiscoverMode=_AdGenEfmNtuAutoDiscoverMode_Object((1,3,6,1,4,1,664,5,66,2,2,1,1,15),_AdGenEfmNtuAutoDiscoverMode_Type())
adGenEfmNtuAutoDiscoverMode.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuAutoDiscoverMode.setStatus(_A)
class _AdGenEfmNtuAutoDiscoverAck_Type(TruthValue):defaultValue=2
_AdGenEfmNtuAutoDiscoverAck_Type.__name__=_O
_AdGenEfmNtuAutoDiscoverAck_Object=MibTableColumn
adGenEfmNtuAutoDiscoverAck=_AdGenEfmNtuAutoDiscoverAck_Object((1,3,6,1,4,1,664,5,66,2,2,1,1,16),_AdGenEfmNtuAutoDiscoverAck_Type())
adGenEfmNtuAutoDiscoverAck.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuAutoDiscoverAck.setStatus(_A)
_AdGenEfmNtuProvCfmTable_Object=MibTable
adGenEfmNtuProvCfmTable=_AdGenEfmNtuProvCfmTable_Object((1,3,6,1,4,1,664,5,66,2,2,2))
if mibBuilder.loadTexts:adGenEfmNtuProvCfmTable.setStatus(_A)
_AdGenEfmNtuProvCfmEntry_Object=MibTableRow
adGenEfmNtuProvCfmEntry=_AdGenEfmNtuProvCfmEntry_Object((1,3,6,1,4,1,664,5,66,2,2,2,1))
adGenEfmNtuProvCfmEntry.setIndexNames((0,_J,_N))
if mibBuilder.loadTexts:adGenEfmNtuProvCfmEntry.setStatus(_A)
_AdGenEfmNtuProvCfmMdName_Type=OctetString
_AdGenEfmNtuProvCfmMdName_Object=MibTableColumn
adGenEfmNtuProvCfmMdName=_AdGenEfmNtuProvCfmMdName_Object((1,3,6,1,4,1,664,5,66,2,2,2,1,1),_AdGenEfmNtuProvCfmMdName_Type())
adGenEfmNtuProvCfmMdName.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvCfmMdName.setStatus(_A)
_AdGenEfmNtuProvCfmMaName_Type=OctetString
_AdGenEfmNtuProvCfmMaName_Object=MibTableColumn
adGenEfmNtuProvCfmMaName=_AdGenEfmNtuProvCfmMaName_Object((1,3,6,1,4,1,664,5,66,2,2,2,1,2),_AdGenEfmNtuProvCfmMaName_Type())
adGenEfmNtuProvCfmMaName.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvCfmMaName.setStatus(_A)
_AdGenEfmNtuProvCfmLocalMepId_Type=Integer32
_AdGenEfmNtuProvCfmLocalMepId_Object=MibTableColumn
adGenEfmNtuProvCfmLocalMepId=_AdGenEfmNtuProvCfmLocalMepId_Object((1,3,6,1,4,1,664,5,66,2,2,2,1,3),_AdGenEfmNtuProvCfmLocalMepId_Type())
adGenEfmNtuProvCfmLocalMepId.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvCfmLocalMepId.setStatus(_A)
_AdGenEfmNtuProvCfmMdLevel_Type=Integer32
_AdGenEfmNtuProvCfmMdLevel_Object=MibTableColumn
adGenEfmNtuProvCfmMdLevel=_AdGenEfmNtuProvCfmMdLevel_Object((1,3,6,1,4,1,664,5,66,2,2,2,1,4),_AdGenEfmNtuProvCfmMdLevel_Type())
adGenEfmNtuProvCfmMdLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvCfmMdLevel.setStatus(_A)
_AdGenEfmNtuProvCfmVlanId_Type=Integer32
_AdGenEfmNtuProvCfmVlanId_Object=MibTableColumn
adGenEfmNtuProvCfmVlanId=_AdGenEfmNtuProvCfmVlanId_Object((1,3,6,1,4,1,664,5,66,2,2,2,1,5),_AdGenEfmNtuProvCfmVlanId_Type())
adGenEfmNtuProvCfmVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvCfmVlanId.setStatus(_A)
_AdGenEfmNtuProvCfmCcmInterval_Type=Integer32
_AdGenEfmNtuProvCfmCcmInterval_Object=MibTableColumn
adGenEfmNtuProvCfmCcmInterval=_AdGenEfmNtuProvCfmCcmInterval_Object((1,3,6,1,4,1,664,5,66,2,2,2,1,6),_AdGenEfmNtuProvCfmCcmInterval_Type())
adGenEfmNtuProvCfmCcmInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvCfmCcmInterval.setStatus(_A)
_AdGenEfmNtuProvCfmMepTableNextIndex_Type=Integer32
_AdGenEfmNtuProvCfmMepTableNextIndex_Object=MibTableColumn
adGenEfmNtuProvCfmMepTableNextIndex=_AdGenEfmNtuProvCfmMepTableNextIndex_Object((1,3,6,1,4,1,664,5,66,2,2,2,1,7),_AdGenEfmNtuProvCfmMepTableNextIndex_Type())
adGenEfmNtuProvCfmMepTableNextIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEfmNtuProvCfmMepTableNextIndex.setStatus(_A)
_AdGenEfmNtuProvCfmMepTable_Object=MibTable
adGenEfmNtuProvCfmMepTable=_AdGenEfmNtuProvCfmMepTable_Object((1,3,6,1,4,1,664,5,66,2,2,3))
if mibBuilder.loadTexts:adGenEfmNtuProvCfmMepTable.setStatus(_A)
_AdGenEfmNtuProvCfmMepEntry_Object=MibTableRow
adGenEfmNtuProvCfmMepEntry=_AdGenEfmNtuProvCfmMepEntry_Object((1,3,6,1,4,1,664,5,66,2,2,3,1))
adGenEfmNtuProvCfmMepEntry.setIndexNames((0,_J,_N),(0,_B,_S))
if mibBuilder.loadTexts:adGenEfmNtuProvCfmMepEntry.setStatus(_A)
_AdGenEfmNtuProvCfmMepIndex_Type=Integer32
_AdGenEfmNtuProvCfmMepIndex_Object=MibTableColumn
adGenEfmNtuProvCfmMepIndex=_AdGenEfmNtuProvCfmMepIndex_Object((1,3,6,1,4,1,664,5,66,2,2,3,1,1),_AdGenEfmNtuProvCfmMepIndex_Type())
adGenEfmNtuProvCfmMepIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEfmNtuProvCfmMepIndex.setStatus(_A)
_AdGenEfmNtuProvCfmMepId_Type=Integer32
_AdGenEfmNtuProvCfmMepId_Object=MibTableColumn
adGenEfmNtuProvCfmMepId=_AdGenEfmNtuProvCfmMepId_Object((1,3,6,1,4,1,664,5,66,2,2,3,1,2),_AdGenEfmNtuProvCfmMepId_Type())
adGenEfmNtuProvCfmMepId.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvCfmMepId.setStatus(_A)
_AdGenEfmNtuProvCfmMepEntryStatus_Type=EntryStatus
_AdGenEfmNtuProvCfmMepEntryStatus_Object=MibTableColumn
adGenEfmNtuProvCfmMepEntryStatus=_AdGenEfmNtuProvCfmMepEntryStatus_Object((1,3,6,1,4,1,664,5,66,2,2,3,1,3),_AdGenEfmNtuProvCfmMepEntryStatus_Type())
adGenEfmNtuProvCfmMepEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvCfmMepEntryStatus.setStatus(_A)
_AdGenEfmNtuProvMgmtIpTable_Object=MibTable
adGenEfmNtuProvMgmtIpTable=_AdGenEfmNtuProvMgmtIpTable_Object((1,3,6,1,4,1,664,5,66,2,2,4))
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtIpTable.setStatus(_A)
_AdGenEfmNtuProvMgmtIpEntry_Object=MibTableRow
adGenEfmNtuProvMgmtIpEntry=_AdGenEfmNtuProvMgmtIpEntry_Object((1,3,6,1,4,1,664,5,66,2,2,4,1))
adGenEfmNtuProvMgmtIpEntry.setIndexNames((0,_J,_N))
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtIpEntry.setStatus(_A)
_AdGenEfmNtuProvMgmtIpAddress_Type=IpAddress
_AdGenEfmNtuProvMgmtIpAddress_Object=MibTableColumn
adGenEfmNtuProvMgmtIpAddress=_AdGenEfmNtuProvMgmtIpAddress_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,1),_AdGenEfmNtuProvMgmtIpAddress_Type())
adGenEfmNtuProvMgmtIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtIpAddress.setStatus(_A)
_AdGenEfmNtuProvMgmtIpSubnetMask_Type=IpAddress
_AdGenEfmNtuProvMgmtIpSubnetMask_Object=MibTableColumn
adGenEfmNtuProvMgmtIpSubnetMask=_AdGenEfmNtuProvMgmtIpSubnetMask_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,2),_AdGenEfmNtuProvMgmtIpSubnetMask_Type())
adGenEfmNtuProvMgmtIpSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtIpSubnetMask.setStatus(_A)
_AdGenEfmNtuProvMgmtIpGateway_Type=IpAddress
_AdGenEfmNtuProvMgmtIpGateway_Object=MibTableColumn
adGenEfmNtuProvMgmtIpGateway=_AdGenEfmNtuProvMgmtIpGateway_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,3),_AdGenEfmNtuProvMgmtIpGateway_Type())
adGenEfmNtuProvMgmtIpGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtIpGateway.setStatus(_A)
_AdGenEfmNtuProvMgmtIpVlan_Type=Integer32
_AdGenEfmNtuProvMgmtIpVlan_Object=MibTableColumn
adGenEfmNtuProvMgmtIpVlan=_AdGenEfmNtuProvMgmtIpVlan_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,4),_AdGenEfmNtuProvMgmtIpVlan_Type())
adGenEfmNtuProvMgmtIpVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtIpVlan.setStatus(_A)
_AdGenEfmNtuProvMgmtTftpServer_Type=IpAddress
_AdGenEfmNtuProvMgmtTftpServer_Object=MibTableColumn
adGenEfmNtuProvMgmtTftpServer=_AdGenEfmNtuProvMgmtTftpServer_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,5),_AdGenEfmNtuProvMgmtTftpServer_Type())
adGenEfmNtuProvMgmtTftpServer.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtTftpServer.setStatus(_A)
_AdGenEfmNtuProvMgmtSnmpWriteCommunity_Type=DisplayString
_AdGenEfmNtuProvMgmtSnmpWriteCommunity_Object=MibTableColumn
adGenEfmNtuProvMgmtSnmpWriteCommunity=_AdGenEfmNtuProvMgmtSnmpWriteCommunity_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,6),_AdGenEfmNtuProvMgmtSnmpWriteCommunity_Type())
adGenEfmNtuProvMgmtSnmpWriteCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtSnmpWriteCommunity.setStatus(_A)
_AdGenEfmNtuProvMgmtSnmpReadCommunity_Type=DisplayString
_AdGenEfmNtuProvMgmtSnmpReadCommunity_Object=MibTableColumn
adGenEfmNtuProvMgmtSnmpReadCommunity=_AdGenEfmNtuProvMgmtSnmpReadCommunity_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,7),_AdGenEfmNtuProvMgmtSnmpReadCommunity_Type())
adGenEfmNtuProvMgmtSnmpReadCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtSnmpReadCommunity.setStatus(_A)
_AdGenEfmNtuProvMgmtSysName_Type=DisplayString
_AdGenEfmNtuProvMgmtSysName_Object=MibTableColumn
adGenEfmNtuProvMgmtSysName=_AdGenEfmNtuProvMgmtSysName_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,8),_AdGenEfmNtuProvMgmtSysName_Type())
adGenEfmNtuProvMgmtSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtSysName.setStatus(_A)
_AdGenEfmNtuProvMgmtFarEndIfIndex_Type=InterfaceIndex
_AdGenEfmNtuProvMgmtFarEndIfIndex_Object=MibTableColumn
adGenEfmNtuProvMgmtFarEndIfIndex=_AdGenEfmNtuProvMgmtFarEndIfIndex_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,9),_AdGenEfmNtuProvMgmtFarEndIfIndex_Type())
adGenEfmNtuProvMgmtFarEndIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtFarEndIfIndex.setStatus(_A)
_AdGenEfmNtuProvMgmtFarEndIpAddress_Type=IpAddress
_AdGenEfmNtuProvMgmtFarEndIpAddress_Object=MibTableColumn
adGenEfmNtuProvMgmtFarEndIpAddress=_AdGenEfmNtuProvMgmtFarEndIpAddress_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,10),_AdGenEfmNtuProvMgmtFarEndIpAddress_Type())
adGenEfmNtuProvMgmtFarEndIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtFarEndIpAddress.setStatus(_A)
_AdGenEfmNtuProvMgmtFarEndSysName_Type=DisplayString
_AdGenEfmNtuProvMgmtFarEndSysName_Object=MibTableColumn
adGenEfmNtuProvMgmtFarEndSysName=_AdGenEfmNtuProvMgmtFarEndSysName_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,11),_AdGenEfmNtuProvMgmtFarEndSysName_Type())
adGenEfmNtuProvMgmtFarEndSysName.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtFarEndSysName.setStatus(_A)
_AdGenEfmNtuProvMgmtPriority_Type=Integer32
_AdGenEfmNtuProvMgmtPriority_Object=MibTableColumn
adGenEfmNtuProvMgmtPriority=_AdGenEfmNtuProvMgmtPriority_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,12),_AdGenEfmNtuProvMgmtPriority_Type())
adGenEfmNtuProvMgmtPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtPriority.setStatus(_A)
_AdGenEfmNtuProvMgmtSnmpSysLocation_Type=DisplayString
_AdGenEfmNtuProvMgmtSnmpSysLocation_Object=MibTableColumn
adGenEfmNtuProvMgmtSnmpSysLocation=_AdGenEfmNtuProvMgmtSnmpSysLocation_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,13),_AdGenEfmNtuProvMgmtSnmpSysLocation_Type())
adGenEfmNtuProvMgmtSnmpSysLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtSnmpSysLocation.setStatus(_A)
_AdGenEfmNtuProvMgmtEzProvHostOneIpAddress_Type=IpAddress
_AdGenEfmNtuProvMgmtEzProvHostOneIpAddress_Object=MibTableColumn
adGenEfmNtuProvMgmtEzProvHostOneIpAddress=_AdGenEfmNtuProvMgmtEzProvHostOneIpAddress_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,14),_AdGenEfmNtuProvMgmtEzProvHostOneIpAddress_Type())
adGenEfmNtuProvMgmtEzProvHostOneIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtEzProvHostOneIpAddress.setStatus(_A)
_AdGenEfmNtuProvMgmtEzProvHostOneTrapVersion_Type=AdGenTrapVersion
_AdGenEfmNtuProvMgmtEzProvHostOneTrapVersion_Object=MibTableColumn
adGenEfmNtuProvMgmtEzProvHostOneTrapVersion=_AdGenEfmNtuProvMgmtEzProvHostOneTrapVersion_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,15),_AdGenEfmNtuProvMgmtEzProvHostOneTrapVersion_Type())
adGenEfmNtuProvMgmtEzProvHostOneTrapVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtEzProvHostOneTrapVersion.setStatus(_A)
_AdGenEfmNtuProvMgmtEzProvHostTwoIpAddress_Type=IpAddress
_AdGenEfmNtuProvMgmtEzProvHostTwoIpAddress_Object=MibTableColumn
adGenEfmNtuProvMgmtEzProvHostTwoIpAddress=_AdGenEfmNtuProvMgmtEzProvHostTwoIpAddress_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,16),_AdGenEfmNtuProvMgmtEzProvHostTwoIpAddress_Type())
adGenEfmNtuProvMgmtEzProvHostTwoIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtEzProvHostTwoIpAddress.setStatus(_A)
_AdGenEfmNtuProvMgmtEzProvHostTwoTrapVersion_Type=AdGenTrapVersion
_AdGenEfmNtuProvMgmtEzProvHostTwoTrapVersion_Object=MibTableColumn
adGenEfmNtuProvMgmtEzProvHostTwoTrapVersion=_AdGenEfmNtuProvMgmtEzProvHostTwoTrapVersion_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,17),_AdGenEfmNtuProvMgmtEzProvHostTwoTrapVersion_Type())
adGenEfmNtuProvMgmtEzProvHostTwoTrapVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtEzProvHostTwoTrapVersion.setStatus(_A)
_AdGenEfmNtuProvMgmtEzProvEnabled_Type=TruthValue
_AdGenEfmNtuProvMgmtEzProvEnabled_Object=MibTableColumn
adGenEfmNtuProvMgmtEzProvEnabled=_AdGenEfmNtuProvMgmtEzProvEnabled_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,18),_AdGenEfmNtuProvMgmtEzProvEnabled_Type())
adGenEfmNtuProvMgmtEzProvEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtEzProvEnabled.setStatus(_A)
_AdGenEfmNtuProvMgmtIpv6AddressPrefixLength_Type=InetAddressPrefixLength
_AdGenEfmNtuProvMgmtIpv6AddressPrefixLength_Object=MibTableColumn
adGenEfmNtuProvMgmtIpv6AddressPrefixLength=_AdGenEfmNtuProvMgmtIpv6AddressPrefixLength_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,19),_AdGenEfmNtuProvMgmtIpv6AddressPrefixLength_Type())
adGenEfmNtuProvMgmtIpv6AddressPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtIpv6AddressPrefixLength.setStatus(_A)
_AdGenEfmNtuProvMgmtIpv6AddressEui64_Type=TruthValue
_AdGenEfmNtuProvMgmtIpv6AddressEui64_Object=MibTableColumn
adGenEfmNtuProvMgmtIpv6AddressEui64=_AdGenEfmNtuProvMgmtIpv6AddressEui64_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,20),_AdGenEfmNtuProvMgmtIpv6AddressEui64_Type())
adGenEfmNtuProvMgmtIpv6AddressEui64.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtIpv6AddressEui64.setStatus(_A)
_AdGenEfmNtuProvMgmtIpv6Address_Type=InetAddressIPv6
_AdGenEfmNtuProvMgmtIpv6Address_Object=MibTableColumn
adGenEfmNtuProvMgmtIpv6Address=_AdGenEfmNtuProvMgmtIpv6Address_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,21),_AdGenEfmNtuProvMgmtIpv6Address_Type())
adGenEfmNtuProvMgmtIpv6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtIpv6Address.setStatus(_A)
_AdGenEfmNtuProvMgmtIpv6AddressLinkLocal_Type=InetAddressIPv6
_AdGenEfmNtuProvMgmtIpv6AddressLinkLocal_Object=MibTableColumn
adGenEfmNtuProvMgmtIpv6AddressLinkLocal=_AdGenEfmNtuProvMgmtIpv6AddressLinkLocal_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,22),_AdGenEfmNtuProvMgmtIpv6AddressLinkLocal_Type())
adGenEfmNtuProvMgmtIpv6AddressLinkLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtIpv6AddressLinkLocal.setStatus(_A)
class _AdGenEfmNtuProvMgmtAutoConfigMode_Type(TruthValue):defaultValue=2
_AdGenEfmNtuProvMgmtAutoConfigMode_Type.__name__=_O
_AdGenEfmNtuProvMgmtAutoConfigMode_Object=MibTableColumn
adGenEfmNtuProvMgmtAutoConfigMode=_AdGenEfmNtuProvMgmtAutoConfigMode_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,23),_AdGenEfmNtuProvMgmtAutoConfigMode_Type())
adGenEfmNtuProvMgmtAutoConfigMode.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtAutoConfigMode.setStatus(_A)
class _AdGenEfmNtuProvMgmtAutoConfigFilename_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AdGenEfmNtuProvMgmtAutoConfigFilename_Type.__name__=_P
_AdGenEfmNtuProvMgmtAutoConfigFilename_Object=MibTableColumn
adGenEfmNtuProvMgmtAutoConfigFilename=_AdGenEfmNtuProvMgmtAutoConfigFilename_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,24),_AdGenEfmNtuProvMgmtAutoConfigFilename_Type())
adGenEfmNtuProvMgmtAutoConfigFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtAutoConfigFilename.setStatus(_A)
class _AdGenEfmNtuProvMgmtAutoConfigGroupName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AdGenEfmNtuProvMgmtAutoConfigGroupName_Type.__name__=_P
_AdGenEfmNtuProvMgmtAutoConfigGroupName_Object=MibTableColumn
adGenEfmNtuProvMgmtAutoConfigGroupName=_AdGenEfmNtuProvMgmtAutoConfigGroupName_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,25),_AdGenEfmNtuProvMgmtAutoConfigGroupName_Type())
adGenEfmNtuProvMgmtAutoConfigGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtAutoConfigGroupName.setStatus(_A)
_AdGenEfmNtuProvMgmtAutoConfigHostIpv4_Type=InetAddressIPv4
_AdGenEfmNtuProvMgmtAutoConfigHostIpv4_Object=MibTableColumn
adGenEfmNtuProvMgmtAutoConfigHostIpv4=_AdGenEfmNtuProvMgmtAutoConfigHostIpv4_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,26),_AdGenEfmNtuProvMgmtAutoConfigHostIpv4_Type())
adGenEfmNtuProvMgmtAutoConfigHostIpv4.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtAutoConfigHostIpv4.setStatus(_A)
_AdGenEfmNtuProvMgmtAutoConfigHostIpv6_Type=InetAddressIPv6
_AdGenEfmNtuProvMgmtAutoConfigHostIpv6_Object=MibTableColumn
adGenEfmNtuProvMgmtAutoConfigHostIpv6=_AdGenEfmNtuProvMgmtAutoConfigHostIpv6_Object((1,3,6,1,4,1,664,5,66,2,2,4,1,27),_AdGenEfmNtuProvMgmtAutoConfigHostIpv6_Type())
adGenEfmNtuProvMgmtAutoConfigHostIpv6.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtAutoConfigHostIpv6.setStatus(_A)
_AdGenEfmNtuStatus_ObjectIdentity=ObjectIdentity
adGenEfmNtuStatus=_AdGenEfmNtuStatus_ObjectIdentity((1,3,6,1,4,1,664,5,66,2,3))
_AdGenEfmNtuStatTable_Object=MibTable
adGenEfmNtuStatTable=_AdGenEfmNtuStatTable_Object((1,3,6,1,4,1,664,5,66,2,3,1))
if mibBuilder.loadTexts:adGenEfmNtuStatTable.setStatus(_A)
_AdGenEfmNtuStatEntry_Object=MibTableRow
adGenEfmNtuStatEntry=_AdGenEfmNtuStatEntry_Object((1,3,6,1,4,1,664,5,66,2,3,1,1))
adGenEfmNtuStatEntry.setIndexNames((0,_J,_N))
if mibBuilder.loadTexts:adGenEfmNtuStatEntry.setStatus(_A)
_AdGenEfmNtuStatUpTime_Type=TimeTicks
_AdGenEfmNtuStatUpTime_Object=MibTableColumn
adGenEfmNtuStatUpTime=_AdGenEfmNtuStatUpTime_Object((1,3,6,1,4,1,664,5,66,2,3,1,1,1),_AdGenEfmNtuStatUpTime_Type())
adGenEfmNtuStatUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEfmNtuStatUpTime.setStatus(_A)
class _AdGenEfmNtuStatLinkStateAware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_AdGenEfmNtuStatLinkStateAware_Type.__name__=_E
_AdGenEfmNtuStatLinkStateAware_Object=MibTableColumn
adGenEfmNtuStatLinkStateAware=_AdGenEfmNtuStatLinkStateAware_Object((1,3,6,1,4,1,664,5,66,2,3,1,1,2),_AdGenEfmNtuStatLinkStateAware_Type())
adGenEfmNtuStatLinkStateAware.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEfmNtuStatLinkStateAware.setStatus(_A)
class _AdGenEfmNtuStatCustIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_AdGenEfmNtuStatCustIf_Type.__name__=_E
_AdGenEfmNtuStatCustIf_Object=MibTableColumn
adGenEfmNtuStatCustIf=_AdGenEfmNtuStatCustIf_Object((1,3,6,1,4,1,664,5,66,2,3,1,1,3),_AdGenEfmNtuStatCustIf_Type())
adGenEfmNtuStatCustIf.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEfmNtuStatCustIf.setStatus(_A)
_AdGenEfmNtuTest_ObjectIdentity=ObjectIdentity
adGenEfmNtuTest=_AdGenEfmNtuTest_ObjectIdentity((1,3,6,1,4,1,664,5,66,2,4))
_AdGenEfmNtuPerformance_ObjectIdentity=ObjectIdentity
adGenEfmNtuPerformance=_AdGenEfmNtuPerformance_ObjectIdentity((1,3,6,1,4,1,664,5,66,2,5))
_AdGenEfmNtuPerfTable_Object=MibTable
adGenEfmNtuPerfTable=_AdGenEfmNtuPerfTable_Object((1,3,6,1,4,1,664,5,66,2,5,1))
if mibBuilder.loadTexts:adGenEfmNtuPerfTable.setStatus(_A)
_AdGenEfmNtuPerfEntry_Object=MibTableRow
adGenEfmNtuPerfEntry=_AdGenEfmNtuPerfEntry_Object((1,3,6,1,4,1,664,5,66,2,5,1,1))
adGenEfmNtuPerfEntry.setIndexNames((0,_J,_N))
if mibBuilder.loadTexts:adGenEfmNtuPerfEntry.setStatus(_A)
_AdGenEfmNtuPerfCustIfTxOctets_Type=Gauge32
_AdGenEfmNtuPerfCustIfTxOctets_Object=MibTableColumn
adGenEfmNtuPerfCustIfTxOctets=_AdGenEfmNtuPerfCustIfTxOctets_Object((1,3,6,1,4,1,664,5,66,2,5,1,1,1),_AdGenEfmNtuPerfCustIfTxOctets_Type())
adGenEfmNtuPerfCustIfTxOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEfmNtuPerfCustIfTxOctets.setStatus(_A)
_AdGenEfmNtuPerfCustIfTxFrames_Type=Gauge32
_AdGenEfmNtuPerfCustIfTxFrames_Object=MibTableColumn
adGenEfmNtuPerfCustIfTxFrames=_AdGenEfmNtuPerfCustIfTxFrames_Object((1,3,6,1,4,1,664,5,66,2,5,1,1,2),_AdGenEfmNtuPerfCustIfTxFrames_Type())
adGenEfmNtuPerfCustIfTxFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEfmNtuPerfCustIfTxFrames.setStatus(_A)
_AdGenEfmNtuPerfCustIfRxOctets_Type=Gauge32
_AdGenEfmNtuPerfCustIfRxOctets_Object=MibTableColumn
adGenEfmNtuPerfCustIfRxOctets=_AdGenEfmNtuPerfCustIfRxOctets_Object((1,3,6,1,4,1,664,5,66,2,5,1,1,3),_AdGenEfmNtuPerfCustIfRxOctets_Type())
adGenEfmNtuPerfCustIfRxOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEfmNtuPerfCustIfRxOctets.setStatus(_A)
_AdGenEfmNtuPerfCustIfRxFrames_Type=Gauge32
_AdGenEfmNtuPerfCustIfRxFrames_Object=MibTableColumn
adGenEfmNtuPerfCustIfRxFrames=_AdGenEfmNtuPerfCustIfRxFrames_Object((1,3,6,1,4,1,664,5,66,2,5,1,1,4),_AdGenEfmNtuPerfCustIfRxFrames_Type())
adGenEfmNtuPerfCustIfRxFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEfmNtuPerfCustIfRxFrames.setStatus(_A)
_AdGenEfmNtuPerfCustIfRxErroredFrames_Type=Gauge32
_AdGenEfmNtuPerfCustIfRxErroredFrames_Object=MibTableColumn
adGenEfmNtuPerfCustIfRxErroredFrames=_AdGenEfmNtuPerfCustIfRxErroredFrames_Object((1,3,6,1,4,1,664,5,66,2,5,1,1,5),_AdGenEfmNtuPerfCustIfRxErroredFrames_Type())
adGenEfmNtuPerfCustIfRxErroredFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEfmNtuPerfCustIfRxErroredFrames.setStatus(_A)
_AdGenEfmNtuPerfCustIfRxDiscardedFrames_Type=Gauge32
_AdGenEfmNtuPerfCustIfRxDiscardedFrames_Object=MibTableColumn
adGenEfmNtuPerfCustIfRxDiscardedFrames=_AdGenEfmNtuPerfCustIfRxDiscardedFrames_Object((1,3,6,1,4,1,664,5,66,2,5,1,1,6),_AdGenEfmNtuPerfCustIfRxDiscardedFrames_Type())
adGenEfmNtuPerfCustIfRxDiscardedFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEfmNtuPerfCustIfRxDiscardedFrames.setStatus(_A)
_AdGenEfmNtuMibConformance_ObjectIdentity=ObjectIdentity
adGenEfmNtuMibConformance=_AdGenEfmNtuMibConformance_ObjectIdentity((1,3,6,1,4,1,664,5,66,2,7))
_AdGenEfmNtuMibGroups_ObjectIdentity=ObjectIdentity
adGenEfmNtuMibGroups=_AdGenEfmNtuMibGroups_ObjectIdentity((1,3,6,1,4,1,664,5,66,2,7,1))
_AdGenEfmNtuAlarmsPrefix_ObjectIdentity=ObjectIdentity
adGenEfmNtuAlarmsPrefix=_AdGenEfmNtuAlarmsPrefix_ObjectIdentity((1,3,6,1,4,1,664,5,66,2,10))
_AdGenEfmNtuAlarms_ObjectIdentity=ObjectIdentity
adGenEfmNtuAlarms=_AdGenEfmNtuAlarms_ObjectIdentity((1,3,6,1,4,1,664,5,66,2,10,0))
adGenEfmNtuProvGroup=ObjectGroup((1,3,6,1,4,1,664,5,66,2,7,1,1))
adGenEfmNtuProvGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_T),(_B,_M),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:adGenEfmNtuProvGroup.setStatus(_A)
adGenEfmNtuProvCfmGroup=ObjectGroup((1,3,6,1,4,1,664,5,66,2,7,1,2))
adGenEfmNtuProvCfmGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:adGenEfmNtuProvCfmGroup.setStatus(_A)
adGenEfmNtuProvCfmMepGroup=ObjectGroup((1,3,6,1,4,1,664,5,66,2,7,1,3))
adGenEfmNtuProvCfmMepGroup.setObjects(*((_B,_S),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:adGenEfmNtuProvCfmMepGroup.setStatus(_A)
adGenEfmNtuProvMgmtGroup=ObjectGroup((1,3,6,1,4,1,664,5,66,2,7,1,4))
adGenEfmNtuProvMgmtGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI)))
if mibBuilder.loadTexts:adGenEfmNtuProvMgmtGroup.setStatus(_A)
adGenEfmNtuStatGroup=ObjectGroup((1,3,6,1,4,1,664,5,66,2,7,1,5))
adGenEfmNtuStatGroup.setObjects(*((_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:adGenEfmNtuStatGroup.setStatus(_A)
adGenEfmNtuPerfGroup=ObjectGroup((1,3,6,1,4,1,664,5,66,2,7,1,6))
adGenEfmNtuPerfGroup.setObjects(*((_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:adGenEfmNtuPerfGroup.setStatus(_A)
adGenEfmNtuCraftLoginSuccess=NotificationType((1,3,6,1,4,1,664,5,66,2,10,0,1))
adGenEfmNtuCraftLoginSuccess.setObjects(*((_H,_I),(_K,_L),(_F,_G),(_B,_M)))
if mibBuilder.loadTexts:adGenEfmNtuCraftLoginSuccess.setStatus(_A)
adGenEfmNtuCraftLoginFail=NotificationType((1,3,6,1,4,1,664,5,66,2,10,0,2))
adGenEfmNtuCraftLoginFail.setObjects(*((_H,_I),(_K,_L),(_F,_G),(_B,_M)))
if mibBuilder.loadTexts:adGenEfmNtuCraftLoginFail.setStatus(_A)
adGenEfmNtuSwDownloadFail=NotificationType((1,3,6,1,4,1,664,5,66,2,10,0,3))
adGenEfmNtuSwDownloadFail.setObjects(*((_H,_I),(_K,_L),(_F,_G),(_B,_M),(_B,_T)))
if mibBuilder.loadTexts:adGenEfmNtuSwDownloadFail.setStatus(_A)
adGenEfmNtuCorruptConfiguration=NotificationType((1,3,6,1,4,1,664,5,66,2,10,0,4))
adGenEfmNtuCorruptConfiguration.setObjects(*((_H,_I),(_K,_L),(_F,_G),(_B,_M)))
if mibBuilder.loadTexts:adGenEfmNtuCorruptConfiguration.setStatus(_A)
adGenEfmNtuMACTableExhaust=NotificationType((1,3,6,1,4,1,664,5,66,2,10,0,5))
adGenEfmNtuMACTableExhaust.setObjects(*((_H,_I),(_K,_L),(_F,_G),(_B,_M)))
if mibBuilder.loadTexts:adGenEfmNtuMACTableExhaust.setStatus(_A)
adGenEfmNtuCustIfDownClr=NotificationType((1,3,6,1,4,1,664,5,66,2,10,0,10))
adGenEfmNtuCustIfDownClr.setObjects(*((_H,_I),(_K,_L),(_F,_G),(_B,_M)))
if mibBuilder.loadTexts:adGenEfmNtuCustIfDownClr.setStatus(_A)
adGenEfmNtuCustIfDownAct=NotificationType((1,3,6,1,4,1,664,5,66,2,10,0,11))
adGenEfmNtuCustIfDownAct.setObjects(*((_H,_I),(_K,_L),(_F,_G),(_B,_M)))
if mibBuilder.loadTexts:adGenEfmNtuCustIfDownAct.setStatus(_A)
adGenEfmNtuAutoDiscover=NotificationType((1,3,6,1,4,1,664,5,66,2,10,0,12))
adGenEfmNtuAutoDiscover.setObjects(*((_H,_I),(_K,_L),(_F,_G),(_J,_U),(_J,_N)))
if mibBuilder.loadTexts:adGenEfmNtuAutoDiscover.setStatus(_A)
adGenEfmNtuEventGroup=NotificationGroup((1,3,6,1,4,1,664,5,66,2,7,1,7))
adGenEfmNtuEventGroup.setObjects(*((_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:adGenEfmNtuEventGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenEfmNtuConfiguration':adGenEfmNtuConfiguration,'adGenEfmNtuProvisioning':adGenEfmNtuProvisioning,'adGenEfmNtuProvTable':adGenEfmNtuProvTable,'adGenEfmNtuProvEntry':adGenEfmNtuProvEntry,_V:adGenEfmNtuProvRestoreDefaults,_W:adGenEfmNtuProvReset,_X:adGenEfmNtuProvSwDownloadStart,_Y:adGenEfmNtuProvSwDownloadFilename,_T:adGenEfmNtuProvSwDownloadStatus,_M:adGenEfmNtuProvCustId,_Z:adGenEfmNtuProvCustIfAutoNeg,_a:adGenEfmNtuProvCustIfSpeed,_b:adGenEfmNtuProvCustIfDuplex,_c:adGenEfmNtuProvCustIfFlowControl,_d:adGenEfmNtuProvEnablePassword,_e:adGenEfmNtuProvMacTableSize,_f:adGenEfmNtuProvMacAging,_g:adGenEfmNtuProvLinkStateAware,_h:adGenEfmNtuAutoDiscoverMode,_i:adGenEfmNtuAutoDiscoverAck,'adGenEfmNtuProvCfmTable':adGenEfmNtuProvCfmTable,'adGenEfmNtuProvCfmEntry':adGenEfmNtuProvCfmEntry,_j:adGenEfmNtuProvCfmMdName,_k:adGenEfmNtuProvCfmMaName,_l:adGenEfmNtuProvCfmLocalMepId,_m:adGenEfmNtuProvCfmMdLevel,_n:adGenEfmNtuProvCfmVlanId,_o:adGenEfmNtuProvCfmCcmInterval,_p:adGenEfmNtuProvCfmMepTableNextIndex,'adGenEfmNtuProvCfmMepTable':adGenEfmNtuProvCfmMepTable,'adGenEfmNtuProvCfmMepEntry':adGenEfmNtuProvCfmMepEntry,_S:adGenEfmNtuProvCfmMepIndex,_q:adGenEfmNtuProvCfmMepId,_r:adGenEfmNtuProvCfmMepEntryStatus,'adGenEfmNtuProvMgmtIpTable':adGenEfmNtuProvMgmtIpTable,'adGenEfmNtuProvMgmtIpEntry':adGenEfmNtuProvMgmtIpEntry,_s:adGenEfmNtuProvMgmtIpAddress,_t:adGenEfmNtuProvMgmtIpSubnetMask,_u:adGenEfmNtuProvMgmtIpGateway,_v:adGenEfmNtuProvMgmtIpVlan,_w:adGenEfmNtuProvMgmtTftpServer,_A1:adGenEfmNtuProvMgmtSnmpWriteCommunity,_A2:adGenEfmNtuProvMgmtSnmpReadCommunity,_x:adGenEfmNtuProvMgmtSysName,_y:adGenEfmNtuProvMgmtFarEndIfIndex,_z:adGenEfmNtuProvMgmtFarEndIpAddress,_A0:adGenEfmNtuProvMgmtFarEndSysName,_A3:adGenEfmNtuProvMgmtPriority,_A4:adGenEfmNtuProvMgmtSnmpSysLocation,_A5:adGenEfmNtuProvMgmtEzProvHostOneIpAddress,_A6:adGenEfmNtuProvMgmtEzProvHostOneTrapVersion,_A7:adGenEfmNtuProvMgmtEzProvHostTwoIpAddress,_A8:adGenEfmNtuProvMgmtEzProvHostTwoTrapVersion,_A9:adGenEfmNtuProvMgmtEzProvEnabled,_AA:adGenEfmNtuProvMgmtIpv6AddressPrefixLength,_AB:adGenEfmNtuProvMgmtIpv6AddressEui64,_AC:adGenEfmNtuProvMgmtIpv6Address,_AD:adGenEfmNtuProvMgmtIpv6AddressLinkLocal,_AE:adGenEfmNtuProvMgmtAutoConfigMode,_AF:adGenEfmNtuProvMgmtAutoConfigFilename,_AG:adGenEfmNtuProvMgmtAutoConfigGroupName,_AH:adGenEfmNtuProvMgmtAutoConfigHostIpv4,_AI:adGenEfmNtuProvMgmtAutoConfigHostIpv6,'adGenEfmNtuStatus':adGenEfmNtuStatus,'adGenEfmNtuStatTable':adGenEfmNtuStatTable,'adGenEfmNtuStatEntry':adGenEfmNtuStatEntry,_AJ:adGenEfmNtuStatUpTime,_AK:adGenEfmNtuStatLinkStateAware,_AL:adGenEfmNtuStatCustIf,'adGenEfmNtuTest':adGenEfmNtuTest,'adGenEfmNtuPerformance':adGenEfmNtuPerformance,'adGenEfmNtuPerfTable':adGenEfmNtuPerfTable,'adGenEfmNtuPerfEntry':adGenEfmNtuPerfEntry,_AM:adGenEfmNtuPerfCustIfTxOctets,_AN:adGenEfmNtuPerfCustIfTxFrames,_AO:adGenEfmNtuPerfCustIfRxOctets,_AP:adGenEfmNtuPerfCustIfRxFrames,_AQ:adGenEfmNtuPerfCustIfRxErroredFrames,_AR:adGenEfmNtuPerfCustIfRxDiscardedFrames,'adGenEfmNtuMibConformance':adGenEfmNtuMibConformance,'adGenEfmNtuMibGroups':adGenEfmNtuMibGroups,'adGenEfmNtuProvGroup':adGenEfmNtuProvGroup,'adGenEfmNtuProvCfmGroup':adGenEfmNtuProvCfmGroup,'adGenEfmNtuProvCfmMepGroup':adGenEfmNtuProvCfmMepGroup,'adGenEfmNtuProvMgmtGroup':adGenEfmNtuProvMgmtGroup,'adGenEfmNtuStatGroup':adGenEfmNtuStatGroup,'adGenEfmNtuPerfGroup':adGenEfmNtuPerfGroup,'adGenEfmNtuEventGroup':adGenEfmNtuEventGroup,'adGenEfmNtuAlarmsPrefix':adGenEfmNtuAlarmsPrefix,'adGenEfmNtuAlarms':adGenEfmNtuAlarms,_AS:adGenEfmNtuCraftLoginSuccess,_AT:adGenEfmNtuCraftLoginFail,_AU:adGenEfmNtuSwDownloadFail,_AV:adGenEfmNtuCorruptConfiguration,_AW:adGenEfmNtuMACTableExhaust,_AX:adGenEfmNtuCustIfDownClr,_AY:adGenEfmNtuCustIfDownAct,_AZ:adGenEfmNtuAutoDiscover,'adGenEfmNtuMIB':adGenEfmNtuMIB})