_A_='apAuthFailReason'
_Az='apAuthMode'
_Ay='apCounterMeasureBssid'
_Ax='apCounterMeasureApMac'
_Aw='apSpectralInfoRssi'
_Av='apSpectralInfoFreq'
_Au='apSpectralInfoType'
_At='apSpectralInfoApMac'
_As='apAssocFailReason'
_Ar='apStaRSSI'
_Aq='apAssocAuthMode'
_Ap='apAPRadioType'
_Ao='apWlanSecurityModeAfterChg'
_An='apWlanSecurityModeBeforeChg'
_Am='apWlanSSID'
_Al='apAttackReason'
_Ak='apCPUUsage'
_Aj='apRevPackages'
_Ai='apSpeciousDeviceMac'
_Ah='apChanChangeMode'
_Ag='apChannelAfterChange'
_Af='apChannelBeforeChange'
_Ae='apCyperIndex'
_Ad='apSSIDKeyConflict'
_Ac='apSSIDKey'
_Ab='apSWVersionBeforeUpdate'
_Aa='updateFailReason'
_AZ='apWorkModeAfterChange'
_AY='apWorkModeBeforeChange'
_AX='apAntDetectCfgAPMac'
_AW='apAntDetectAntIndex'
_AV='apAntDetectAPMac'
_AU='apConfigInfoMac'
_AT='apBlackSSID'
_AS='neighborApMac'
_AR='apStaticAttackMac'
_AQ='apCounterVendor'
_AP='apCounterSSID'
_AO='apWidsPermitMac'
_AN='apCounterMac'
_AM='apIllegalApMac'
_AL='apBlackListDeviceMAC'
_AK='apBlackListIndex'
_AJ='apWhiteListIndex'
_AI='qtechRogueApMacAddr'
_AH='apSSIDStatisticsNewSSID'
_AG='apSSIDStatisticsNewRadioId'
_AF='apSSIDStatisticsNewAPMac'
_AE='apSSIDStatisticsWlanId'
_AD='apSSIDStatisticsRadioId'
_AC='apSSIDStatisticsAPMac'
_AB='apRGMIIIndex'
_AA='background'
_A9='bestEffort'
_A8='apWireQoSTrafficClassId'
_A7='apUserMacAddress'
_A6='apRefusedStaMAC'
_A5='1000 packets'
_A4='timepacket-Based'
_A3='packetBased'
_A2='timeBased'
_A1='wapicer-web'
_A0='sharedkey'
_z='opensystem'
_y='apSSIDRadioId'
_x='apSSIDAPMac'
_w='not-accessible'
_v='apIfLocalRGMIINum'
_u='associate'
_t='deassociate'
_s='apAssoStatusAPMac'
_r='ifIndex'
_q='IF-MIB'
_p='apTrapIllegalApSSID'
_o='apTrapIllegalApType'
_n='apTrapWorkingApBSSID'
_m='apTrapWorkingApMac'
_l='apTrapIllegalApRSSI'
_k='apTrapIllegalApChannel'
_j='apTrapIllegalApMac'
_i='apAPRadioId'
_h='apPermitAssoUser'
_g='apInterfStaMac'
_f='apInterfAPChannel'
_e='dot11b'
_d='dot11a'
_c='normal'
_b='qtechStaMacAddr'
_a='apAssoFailReason'
_Z='apInterruptReason'
_Y='second'
_X='up'
_W='admindown'
_V='apInterfAPBSSID'
_U='on'
_T='off'
_S='none'
_R='qtechApgWlanId'
_Q='apWorkingAPBSSID'
_P='apWorkingAPSSID'
_O='apWorkingAPChannel'
_N='OctetString'
_M='apStaMacAddr'
_L='DisplayString'
_K='Unsigned32'
_J='qtechApCfgRadioId'
_I='apWorkingAPRadioIfInfo'
_H='read-create'
_G='Integer32'
_F='qtechApMacAddr'
_E='QTECH-AC-MGMT-MIB'
_D='QTECH-WLAN-FIT-AP-CF-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
ifIndex,=mibBuilder.importSymbols(_q,_r)
qtechApApName,qtechApCfgRadioId,qtechApMacAddr,qtechApgWlanId,qtechStaMacAddr=mibBuilder.importSymbols(_E,'qtechApApName',_J,_F,_R,_b)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
qtechFitApMibModule=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,81))
if mibBuilder.loadTexts:qtechFitApMibModule.setRevisions(('2010-02-28 00:00',))
_ApQtechAlarmTraps_ObjectIdentity=ObjectIdentity
apQtechAlarmTraps=_ApQtechAlarmTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,0))
_ApSystemAlarmTraps_ObjectIdentity=ObjectIdentity
apSystemAlarmTraps=_ApSystemAlarmTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,0,1))
_ApWirelessAlarmTraps_ObjectIdentity=ObjectIdentity
apWirelessAlarmTraps=_ApWirelessAlarmTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,0,2))
_ApStaAnnounceTraps_ObjectIdentity=ObjectIdentity
apStaAnnounceTraps=_ApStaAnnounceTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,0,3))
_ApWAPISecurityAlarmTraps_ObjectIdentity=ObjectIdentity
apWAPISecurityAlarmTraps=_ApWAPISecurityAlarmTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,0,4))
_ApSystemInfoConfigObjects_ObjectIdentity=ObjectIdentity
apSystemInfoConfigObjects=_ApSystemInfoConfigObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,1))
_ApGeneralInfoConfigObjects_ObjectIdentity=ObjectIdentity
apGeneralInfoConfigObjects=_ApGeneralInfoConfigObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,1,1))
_ApGeneralInfoConfigTable_Object=MibTable
apGeneralInfoConfigTable=_ApGeneralInfoConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,1,1))
if mibBuilder.loadTexts:apGeneralInfoConfigTable.setStatus(_A)
_ApGeneralInfoConfigTableEntry_Object=MibTableRow
apGeneralInfoConfigTableEntry=_ApGeneralInfoConfigTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,1,1,1))
apGeneralInfoConfigTableEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:apGeneralInfoConfigTableEntry.setStatus(_A)
class _ApSysNEId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_ApSysNEId_Type.__name__=_L
_ApSysNEId_Object=MibTableColumn
apSysNEId=_ApSysNEId_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,1,1,1,1),_ApSysNEId_Type())
apSysNEId.setMaxAccess(_C)
if mibBuilder.loadTexts:apSysNEId.setStatus(_A)
class _ApSysName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_ApSysName_Type.__name__=_L
_ApSysName_Object=MibTableColumn
apSysName=_ApSysName_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,1,1,1,2),_ApSysName_Type())
apSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:apSysName.setStatus(_A)
_ApStatWindowTime_Type=TimeTicks
_ApStatWindowTime_Object=MibTableColumn
apStatWindowTime=_ApStatWindowTime_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,1,1,1,3),_ApStatWindowTime_Type())
apStatWindowTime.setMaxAccess(_C)
if mibBuilder.loadTexts:apStatWindowTime.setStatus(_A)
_ApSampleTime_Type=Counter32
_ApSampleTime_Object=MibTableColumn
apSampleTime=_ApSampleTime_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,1,1,1,4),_ApSampleTime_Type())
apSampleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:apSampleTime.setStatus(_A)
class _ApRtCollectOnoff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_ApRtCollectOnoff_Type.__name__=_G
_ApRtCollectOnoff_Object=MibTableColumn
apRtCollectOnoff=_ApRtCollectOnoff_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,1,1,1,5),_ApRtCollectOnoff_Type())
apRtCollectOnoff.setMaxAccess(_C)
if mibBuilder.loadTexts:apRtCollectOnoff.setStatus(_A)
class _ApSysRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_c,0),('restart',1)))
_ApSysRestart_Type.__name__=_G
_ApSysRestart_Object=MibTableColumn
apSysRestart=_ApSysRestart_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,1,1,1,6),_ApSysRestart_Type())
apSysRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:apSysRestart.setStatus(_A)
class _ApSysReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_c,0),('reset',1)))
_ApSysReset_Type.__name__=_G
_ApSysReset_Object=MibTableColumn
apSysReset=_ApSysReset_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,1,1,1,7),_ApSysReset_Type())
apSysReset.setMaxAccess(_C)
if mibBuilder.loadTexts:apSysReset.setStatus(_A)
_ApGeneralInfoReadObjects_ObjectIdentity=ObjectIdentity
apGeneralInfoReadObjects=_ApGeneralInfoReadObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,1,2))
_ApGeneralCfgInfoReadTable_Object=MibTable
apGeneralCfgInfoReadTable=_ApGeneralCfgInfoReadTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1))
if mibBuilder.loadTexts:apGeneralCfgInfoReadTable.setStatus(_A)
_ApGeneralCfgInfoReadTableEntry_Object=MibTableRow
apGeneralCfgInfoReadTableEntry=_ApGeneralCfgInfoReadTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1,1))
apGeneralCfgInfoReadTableEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:apGeneralCfgInfoReadTableEntry.setStatus(_A)
class _ApSysDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ApSysDescr_Type.__name__=_L
_ApSysDescr_Object=MibTableColumn
apSysDescr=_ApSysDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1,1,1),_ApSysDescr_Type())
apSysDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:apSysDescr.setStatus(_A)
class _ApSysManufacture_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ApSysManufacture_Type.__name__=_L
_ApSysManufacture_Object=MibTableColumn
apSysManufacture=_ApSysManufacture_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1,1,2),_ApSysManufacture_Type())
apSysManufacture.setMaxAccess(_B)
if mibBuilder.loadTexts:apSysManufacture.setStatus(_A)
class _ApSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ApSerialNumber_Type.__name__=_L
_ApSerialNumber_Object=MibTableColumn
apSerialNumber=_ApSerialNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1,1,3),_ApSerialNumber_Type())
apSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:apSerialNumber.setStatus(_A)
class _ApSysModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ApSysModel_Type.__name__=_L
_ApSysModel_Object=MibTableColumn
apSysModel=_ApSysModel_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1,1,4),_ApSysModel_Type())
apSysModel.setMaxAccess(_B)
if mibBuilder.loadTexts:apSysModel.setStatus(_A)
_ApSysUpTime_Type=Counter32
_ApSysUpTime_Object=MibTableColumn
apSysUpTime=_ApSysUpTime_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1,1,5),_ApSysUpTime_Type())
apSysUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:apSysUpTime.setStatus(_A)
_ApSysOnlineTime_Type=Counter32
_ApSysOnlineTime_Object=MibTableColumn
apSysOnlineTime=_ApSysOnlineTime_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1,1,6),_ApSysOnlineTime_Type())
apSysOnlineTime.setMaxAccess(_B)
if mibBuilder.loadTexts:apSysOnlineTime.setStatus(_A)
_ApSysIPAddress_Type=IpAddress
_ApSysIPAddress_Object=MibTableColumn
apSysIPAddress=_ApSysIPAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1,1,7),_ApSysIPAddress_Type())
apSysIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:apSysIPAddress.setStatus(_A)
_ApSysIPNetMask_Type=IpAddress
_ApSysIPNetMask_Object=MibTableColumn
apSysIPNetMask=_ApSysIPNetMask_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1,1,8),_ApSysIPNetMask_Type())
apSysIPNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:apSysIPNetMask.setStatus(_A)
_ApSysGateWayAddr_Type=IpAddress
_ApSysGateWayAddr_Object=MibTableColumn
apSysGateWayAddr=_ApSysGateWayAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1,1,9),_ApSysGateWayAddr_Type())
apSysGateWayAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:apSysGateWayAddr.setStatus(_A)
_ApSysMacAddrConnectToAC_Type=MacAddress
_ApSysMacAddrConnectToAC_Object=MibTableColumn
apSysMacAddrConnectToAC=_ApSysMacAddrConnectToAC_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1,1,10),_ApSysMacAddrConnectToAC_Type())
apSysMacAddrConnectToAC.setMaxAccess(_B)
if mibBuilder.loadTexts:apSysMacAddrConnectToAC.setStatus(_A)
_ApSoftwareName_Type=DisplayString
_ApSoftwareName_Object=MibTableColumn
apSoftwareName=_ApSoftwareName_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1,1,11),_ApSoftwareName_Type())
apSoftwareName.setMaxAccess(_B)
if mibBuilder.loadTexts:apSoftwareName.setStatus(_A)
_ApSoftwareVersion_Type=DisplayString
_ApSoftwareVersion_Object=MibTableColumn
apSoftwareVersion=_ApSoftwareVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1,1,12),_ApSoftwareVersion_Type())
apSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:apSoftwareVersion.setStatus(_A)
_ApSoftwareVendor_Type=DisplayString
_ApSoftwareVendor_Object=MibTableColumn
apSoftwareVendor=_ApSoftwareVendor_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1,1,13),_ApSoftwareVendor_Type())
apSoftwareVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:apSoftwareVendor.setStatus(_A)
_ApCPUType_Type=DisplayString
_ApCPUType_Object=MibTableColumn
apCPUType=_ApCPUType_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1,1,14),_ApCPUType_Type())
apCPUType.setMaxAccess(_B)
if mibBuilder.loadTexts:apCPUType.setStatus(_A)
_ApMemoryType_Type=DisplayString
_ApMemoryType_Object=MibTableColumn
apMemoryType=_ApMemoryType_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1,1,15),_ApMemoryType_Type())
apMemoryType.setMaxAccess(_B)
if mibBuilder.loadTexts:apMemoryType.setStatus(_A)
_ApMemorySize_Type=OctetString
_ApMemorySize_Object=MibTableColumn
apMemorySize=_ApMemorySize_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1,1,17),_ApMemorySize_Type())
apMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:apMemorySize.setStatus(_A)
_ApFlashSize_Type=OctetString
_ApFlashSize_Object=MibTableColumn
apFlashSize=_ApFlashSize_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,2,1,1,18),_ApFlashSize_Type())
apFlashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:apFlashSize.setStatus(_A)
_ApGeneralStatusCFGObjects_ObjectIdentity=ObjectIdentity
apGeneralStatusCFGObjects=_ApGeneralStatusCFGObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,1,3))
_ApGeneralStatusCFGTable_Object=MibTable
apGeneralStatusCFGTable=_ApGeneralStatusCFGTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,3,1))
if mibBuilder.loadTexts:apGeneralStatusCFGTable.setStatus(_A)
_ApGeneralStatusCFGTableEntry_Object=MibTableRow
apGeneralStatusCFGTableEntry=_ApGeneralStatusCFGTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,3,1,1))
apGeneralStatusCFGTableEntry.setIndexNames((0,_D,_s))
if mibBuilder.loadTexts:apGeneralStatusCFGTableEntry.setStatus(_A)
_ApAPName_Type=DisplayString
_ApAPName_Object=MibTableColumn
apAPName=_ApAPName_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,3,1,1,1),_ApAPName_Type())
apAPName.setMaxAccess(_B)
if mibBuilder.loadTexts:apAPName.setStatus(_A)
class _ApACAssociateStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_t,0),(_u,1)))
_ApACAssociateStatus_Type.__name__=_G
_ApACAssociateStatus_Object=MibTableColumn
apACAssociateStatus=_ApACAssociateStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,3,1,1,2),_ApACAssociateStatus_Type())
apACAssociateStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:apACAssociateStatus.setStatus(_A)
class _ApMonitorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_c,0),('monitor',1),('semiMonitor',2)))
_ApMonitorMode_Type.__name__=_G
_ApMonitorMode_Object=MibTableColumn
apMonitorMode=_ApMonitorMode_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,3,1,1,3),_ApMonitorMode_Type())
apMonitorMode.setMaxAccess(_C)
if mibBuilder.loadTexts:apMonitorMode.setStatus(_A)
_ApAssoStatusAPMac_Type=MacAddress
_ApAssoStatusAPMac_Object=MibTableColumn
apAssoStatusAPMac=_ApAssoStatusAPMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,3,1,1,4),_ApAssoStatusAPMac_Type())
apAssoStatusAPMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apAssoStatusAPMac.setStatus(_A)
class _ApACHbAssocStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_t,0),(_u,1)))
_ApACHbAssocStatus_Type.__name__=_G
_ApACHbAssocStatus_Object=MibTableColumn
apACHbAssocStatus=_ApACHbAssocStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,3,1,1,5),_ApACHbAssocStatus_Type())
apACHbAssocStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:apACHbAssocStatus.setStatus(_A)
_ApScanType_Type=Integer32
_ApScanType_Object=MibTableColumn
apScanType=_ApScanType_Object((1,3,6,1,4,1,27514,1,1,10,2,81,1,3,1,1,6),_ApScanType_Type())
apScanType.setMaxAccess(_C)
if mibBuilder.loadTexts:apScanType.setStatus(_A)
_ApInterfaceConfigObjects_ObjectIdentity=ObjectIdentity
apInterfaceConfigObjects=_ApInterfaceConfigObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,2))
_ApInterfaceNumberObjects_ObjectIdentity=ObjectIdentity
apInterfaceNumberObjects=_ApInterfaceNumberObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,2,1))
_ApInterfaceNumberTable_Object=MibTable
apInterfaceNumberTable=_ApInterfaceNumberTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,1,1))
if mibBuilder.loadTexts:apInterfaceNumberTable.setStatus(_A)
_ApInterfaceNumberTableEntry_Object=MibTableRow
apInterfaceNumberTableEntry=_ApInterfaceNumberTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,1,1,1))
apInterfaceNumberTableEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:apInterfaceNumberTableEntry.setStatus(_A)
class _ApIfNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ApIfNumber_Type.__name__=_G
_ApIfNumber_Object=MibTableColumn
apIfNumber=_ApIfNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,1,1,1,1),_ApIfNumber_Type())
apIfNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfNumber.setStatus(_A)
class _ApBSSIDNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ApBSSIDNum_Type.__name__=_G
_ApBSSIDNum_Object=MibTableColumn
apBSSIDNum=_ApBSSIDNum_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,1,1,1,2),_ApBSSIDNum_Type())
apBSSIDNum.setMaxAccess(_B)
if mibBuilder.loadTexts:apBSSIDNum.setStatus(_A)
_ApInterfaceRGMIIcfgObjects_ObjectIdentity=ObjectIdentity
apInterfaceRGMIIcfgObjects=_ApInterfaceRGMIIcfgObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,2,2))
_ApInterfaceRGMIIconfigTable_Object=MibTable
apInterfaceRGMIIconfigTable=_ApInterfaceRGMIIconfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,2,1))
if mibBuilder.loadTexts:apInterfaceRGMIIconfigTable.setStatus(_A)
_ApInterfaceRGMIIconfigTableEntry_Object=MibTableRow
apInterfaceRGMIIconfigTableEntry=_ApInterfaceRGMIIconfigTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,2,1,1))
apInterfaceRGMIIconfigTableEntry.setIndexNames((0,_E,_F),(0,_D,_v))
if mibBuilder.loadTexts:apInterfaceRGMIIconfigTableEntry.setStatus(_A)
_ApIfLocalRGMIINum_Type=Integer32
_ApIfLocalRGMIINum_Object=MibTableColumn
apIfLocalRGMIINum=_ApIfLocalRGMIINum_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,2,1,1,1),_ApIfLocalRGMIINum_Type())
apIfLocalRGMIINum.setMaxAccess(_w)
if mibBuilder.loadTexts:apIfLocalRGMIINum.setStatus(_A)
class _ApIfRGMIIDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ApIfRGMIIDescr_Type.__name__=_L
_ApIfRGMIIDescr_Object=MibTableColumn
apIfRGMIIDescr=_ApIfRGMIIDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,2,1,1,2),_ApIfRGMIIDescr_Type())
apIfRGMIIDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfRGMIIDescr.setStatus(_A)
_ApIfRGMIIType_Type=IANAifType
_ApIfRGMIIType_Object=MibTableColumn
apIfRGMIIType=_ApIfRGMIIType_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,2,1,1,3),_ApIfRGMIIType_Type())
apIfRGMIIType.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfRGMIIType.setStatus(_A)
_ApIfRGMIIMtu_Type=Integer32
_ApIfRGMIIMtu_Object=MibTableColumn
apIfRGMIIMtu=_ApIfRGMIIMtu_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,2,1,1,4),_ApIfRGMIIMtu_Type())
apIfRGMIIMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfRGMIIMtu.setStatus(_A)
_ApIfRGMIISpeed_Type=Integer32
_ApIfRGMIISpeed_Object=MibTableColumn
apIfRGMIISpeed=_ApIfRGMIISpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,2,1,1,5),_ApIfRGMIISpeed_Type())
apIfRGMIISpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfRGMIISpeed.setStatus(_A)
_ApIfRGMIIPhysAddress_Type=MacAddress
_ApIfRGMIIPhysAddress_Object=MibTableColumn
apIfRGMIIPhysAddress=_ApIfRGMIIPhysAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,2,1,1,6),_ApIfRGMIIPhysAddress_Type())
apIfRGMIIPhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfRGMIIPhysAddress.setStatus(_A)
class _ApIfRGMIIAdminStatusEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_X,1)))
_ApIfRGMIIAdminStatusEnable_Type.__name__=_G
_ApIfRGMIIAdminStatusEnable_Object=MibTableColumn
apIfRGMIIAdminStatusEnable=_ApIfRGMIIAdminStatusEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,2,1,1,7),_ApIfRGMIIAdminStatusEnable_Type())
apIfRGMIIAdminStatusEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfRGMIIAdminStatusEnable.setStatus(_A)
class _ApIfRGMIIOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('down',0),(_X,1),(_W,2)))
_ApIfRGMIIOperStatus_Type.__name__=_G
_ApIfRGMIIOperStatus_Object=MibTableColumn
apIfRGMIIOperStatus=_ApIfRGMIIOperStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,2,1,1,8),_ApIfRGMIIOperStatus_Type())
apIfRGMIIOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfRGMIIOperStatus.setStatus(_A)
_ApIfRGMIILastChange_Type=TimeTicks
_ApIfRGMIILastChange_Object=MibTableColumn
apIfRGMIILastChange=_ApIfRGMIILastChange_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,2,1,1,9),_ApIfRGMIILastChange_Type())
apIfRGMIILastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfRGMIILastChange.setStatus(_A)
_ApInterfaceWirelesscfgObjects_ObjectIdentity=ObjectIdentity
apInterfaceWirelesscfgObjects=_ApInterfaceWirelesscfgObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,2,3))
_ApInterfaceWirelessconfigTable_Object=MibTable
apInterfaceWirelessconfigTable=_ApInterfaceWirelessconfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1))
if mibBuilder.loadTexts:apInterfaceWirelessconfigTable.setStatus(_A)
_ApInterfaceWirelessconfigTableEntry_Object=MibTableRow
apInterfaceWirelessconfigTableEntry=_ApInterfaceWirelessconfigTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1))
apInterfaceWirelessconfigTableEntry.setIndexNames((0,_E,_F),(0,_E,_J))
if mibBuilder.loadTexts:apInterfaceWirelessconfigTableEntry.setStatus(_A)
class _ApIfWireDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ApIfWireDescr_Type.__name__=_L
_ApIfWireDescr_Object=MibTableColumn
apIfWireDescr=_ApIfWireDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,1),_ApIfWireDescr_Type())
apIfWireDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfWireDescr.setStatus(_A)
_ApIfWireType_Type=IANAifType
_ApIfWireType_Object=MibTableColumn
apIfWireType=_ApIfWireType_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,2),_ApIfWireType_Type())
apIfWireType.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfWireType.setStatus(_A)
_ApIfWireMtu_Type=Integer32
_ApIfWireMtu_Object=MibTableColumn
apIfWireMtu=_ApIfWireMtu_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,3),_ApIfWireMtu_Type())
apIfWireMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfWireMtu.setStatus(_A)
_ApIfWireSpeed_Type=Integer32
_ApIfWireSpeed_Object=MibTableColumn
apIfWireSpeed=_ApIfWireSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,4),_ApIfWireSpeed_Type())
apIfWireSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfWireSpeed.setStatus(_A)
_ApIfWirePhysAddress_Type=MacAddress
_ApIfWirePhysAddress_Object=MibTableColumn
apIfWirePhysAddress=_ApIfWirePhysAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,5),_ApIfWirePhysAddress_Type())
apIfWirePhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfWirePhysAddress.setStatus(_A)
class _ApIfWireAdminStatusEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_X,0),(_W,1)))
_ApIfWireAdminStatusEnable_Type.__name__=_G
_ApIfWireAdminStatusEnable_Object=MibTableColumn
apIfWireAdminStatusEnable=_ApIfWireAdminStatusEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,6),_ApIfWireAdminStatusEnable_Type())
apIfWireAdminStatusEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWireAdminStatusEnable.setStatus(_A)
class _ApIfWireOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_X,0),('down',1),(_W,2)))
_ApIfWireOperStatus_Type.__name__=_G
_ApIfWireOperStatus_Object=MibTableColumn
apIfWireOperStatus=_ApIfWireOperStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,7),_ApIfWireOperStatus_Type())
apIfWireOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfWireOperStatus.setStatus(_A)
_ApIfWireLastChange_Type=TimeTicks
_ApIfWireLastChange_Object=MibTableColumn
apIfWireLastChange=_ApIfWireLastChange_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,8),_ApIfWireLastChange_Type())
apIfWireLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfWireLastChange.setStatus(_A)
class _ApIfWireChannelAutoSelectEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_ApIfWireChannelAutoSelectEnable_Type.__name__=_G
_ApIfWireChannelAutoSelectEnable_Object=MibTableColumn
apIfWireChannelAutoSelectEnable=_ApIfWireChannelAutoSelectEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,9),_ApIfWireChannelAutoSelectEnable_Type())
apIfWireChannelAutoSelectEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWireChannelAutoSelectEnable.setStatus(_A)
_ApIfWireRadioChannelConfig_Type=Integer32
_ApIfWireRadioChannelConfig_Object=MibTableColumn
apIfWireRadioChannelConfig=_ApIfWireRadioChannelConfig_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,10),_ApIfWireRadioChannelConfig_Type())
apIfWireRadioChannelConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWireRadioChannelConfig.setStatus(_A)
_ApIfWireRadioChannelUsing_Type=Integer32
_ApIfWireRadioChannelUsing_Object=MibTableColumn
apIfWireRadioChannelUsing=_ApIfWireRadioChannelUsing_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,11),_ApIfWireRadioChannelUsing_Type())
apIfWireRadioChannelUsing.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfWireRadioChannelUsing.setStatus(_A)
_ApIfWireCurrRadioModeSupport_Type=Counter32
_ApIfWireCurrRadioModeSupport_Object=MibTableColumn
apIfWireCurrRadioModeSupport=_ApIfWireCurrRadioModeSupport_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,12),_ApIfWireCurrRadioModeSupport_Type())
apIfWireCurrRadioModeSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfWireCurrRadioModeSupport.setStatus(_A)
_ApIfWireRadioModeConfig_Type=Counter32
_ApIfWireRadioModeConfig_Object=MibTableColumn
apIfWireRadioModeConfig=_ApIfWireRadioModeConfig_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,13),_ApIfWireRadioModeConfig_Type())
apIfWireRadioModeConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWireRadioModeConfig.setStatus(_A)
class _ApIfWireTransmitSpeedConfig_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ApIfWireTransmitSpeedConfig_Type.__name__=_L
_ApIfWireTransmitSpeedConfig_Object=MibTableColumn
apIfWireTransmitSpeedConfig=_ApIfWireTransmitSpeedConfig_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,14),_ApIfWireTransmitSpeedConfig_Type())
apIfWireTransmitSpeedConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWireTransmitSpeedConfig.setStatus(_A)
class _ApIfWireMaxTxPwrLvl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ApIfWireMaxTxPwrLvl_Type.__name__=_L
_ApIfWireMaxTxPwrLvl_Object=MibTableColumn
apIfWireMaxTxPwrLvl=_ApIfWireMaxTxPwrLvl_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,15),_ApIfWireMaxTxPwrLvl_Type())
apIfWireMaxTxPwrLvl.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfWireMaxTxPwrLvl.setStatus(_A)
_ApIfWirePwrAttRange_Type=Integer32
_ApIfWirePwrAttRange_Object=MibTableColumn
apIfWirePwrAttRange=_ApIfWirePwrAttRange_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,16),_ApIfWirePwrAttRange_Type())
apIfWirePwrAttRange.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfWirePwrAttRange.setStatus(_A)
_ApIfWirePwrAttValue_Type=Integer32
_ApIfWirePwrAttValue_Object=MibTableColumn
apIfWirePwrAttValue=_ApIfWirePwrAttValue_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,17),_ApIfWirePwrAttValue_Type())
apIfWirePwrAttValue.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWirePwrAttValue.setStatus(_A)
_ApIfWireAntennaGain_Type=Integer32
_ApIfWireAntennaGain_Object=MibTableColumn
apIfWireAntennaGain=_ApIfWireAntennaGain_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,18),_ApIfWireAntennaGain_Type())
apIfWireAntennaGain.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfWireAntennaGain.setStatus(_A)
_ApIfWirePowerMgmtEnable_Type=TruthValue
_ApIfWirePowerMgmtEnable_Object=MibTableColumn
apIfWirePowerMgmtEnable=_ApIfWirePowerMgmtEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,19),_ApIfWirePowerMgmtEnable_Type())
apIfWirePowerMgmtEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWirePowerMgmtEnable.setStatus(_A)
_ApTxPwr_Type=Integer32
_ApTxPwr_Object=MibTableColumn
apTxPwr=_ApTxPwr_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,20),_ApTxPwr_Type())
apTxPwr.setMaxAccess(_C)
if mibBuilder.loadTexts:apTxPwr.setStatus(_A)
_ApIfWireMaxStationNumPermitted_Type=Counter32
_ApIfWireMaxStationNumPermitted_Object=MibTableColumn
apIfWireMaxStationNumPermitted=_ApIfWireMaxStationNumPermitted_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,21),_ApIfWireMaxStationNumPermitted_Type())
apIfWireMaxStationNumPermitted.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWireMaxStationNumPermitted.setStatus(_A)
class _ApIfWireAMPDUEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_ApIfWireAMPDUEnabled_Type.__name__=_G
_ApIfWireAMPDUEnabled_Object=MibTableColumn
apIfWireAMPDUEnabled=_ApIfWireAMPDUEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,22),_ApIfWireAMPDUEnabled_Type())
apIfWireAMPDUEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWireAMPDUEnabled.setStatus(_A)
class _ApIfWireBWMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_ApIfWireBWMode_Type.__name__=_G
_ApIfWireBWMode_Object=MibTableColumn
apIfWireBWMode=_ApIfWireBWMode_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,23),_ApIfWireBWMode_Type())
apIfWireBWMode.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWireBWMode.setStatus(_A)
class _ApIfWireShortGIEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_ApIfWireShortGIEnabled_Type.__name__=_G
_ApIfWireShortGIEnabled_Object=MibTableColumn
apIfWireShortGIEnabled=_ApIfWireShortGIEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,24),_ApIfWireShortGIEnabled_Type())
apIfWireShortGIEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWireShortGIEnabled.setStatus(_A)
_ApIfWireIs11nOnly_Type=TruthValue
_ApIfWireIs11nOnly_Object=MibTableColumn
apIfWireIs11nOnly=_ApIfWireIs11nOnly_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,25),_ApIfWireIs11nOnly_Type())
apIfWireIs11nOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWireIs11nOnly.setStatus(_A)
_ApIfWireBeaconIntvl_Type=Integer32
_ApIfWireBeaconIntvl_Object=MibTableColumn
apIfWireBeaconIntvl=_ApIfWireBeaconIntvl_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,26),_ApIfWireBeaconIntvl_Type())
apIfWireBeaconIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWireBeaconIntvl.setStatus(_A)
_ApIfWireDtimIntvl_Type=Integer32
_ApIfWireDtimIntvl_Object=MibTableColumn
apIfWireDtimIntvl=_ApIfWireDtimIntvl_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,27),_ApIfWireDtimIntvl_Type())
apIfWireDtimIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWireDtimIntvl.setStatus(_A)
_ApIfWireRtsThreshold_Type=Integer32
_ApIfWireRtsThreshold_Object=MibTableColumn
apIfWireRtsThreshold=_ApIfWireRtsThreshold_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,28),_ApIfWireRtsThreshold_Type())
apIfWireRtsThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWireRtsThreshold.setStatus(_A)
_ApIfWireFragThreshlod_Type=Integer32
_ApIfWireFragThreshlod_Object=MibTableColumn
apIfWireFragThreshlod=_ApIfWireFragThreshlod_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,29),_ApIfWireFragThreshlod_Type())
apIfWireFragThreshlod.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWireFragThreshlod.setStatus(_A)
class _ApIfWirePreambleLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('long',0),('short',1)))
_ApIfWirePreambleLen_Type.__name__=_G
_ApIfWirePreambleLen_Object=MibTableColumn
apIfWirePreambleLen=_ApIfWirePreambleLen_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,30),_ApIfWirePreambleLen_Type())
apIfWirePreambleLen.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWirePreambleLen.setStatus(_A)
_ApAntennaReceiveMask_Type=Integer32
_ApAntennaReceiveMask_Object=MibTableColumn
apAntennaReceiveMask=_ApAntennaReceiveMask_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,31),_ApAntennaReceiveMask_Type())
apAntennaReceiveMask.setMaxAccess(_C)
if mibBuilder.loadTexts:apAntennaReceiveMask.setStatus(_A)
_ApAntennaTransmitMask_Type=Integer32
_ApAntennaTransmitMask_Object=MibTableColumn
apAntennaTransmitMask=_ApAntennaTransmitMask_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,32),_ApAntennaTransmitMask_Type())
apAntennaTransmitMask.setMaxAccess(_C)
if mibBuilder.loadTexts:apAntennaTransmitMask.setStatus(_A)
_ApIfWireAMSDUEnabled_Type=Integer32
_ApIfWireAMSDUEnabled_Object=MibTableColumn
apIfWireAMSDUEnabled=_ApIfWireAMSDUEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,33),_ApIfWireAMSDUEnabled_Type())
apIfWireAMSDUEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWireAMSDUEnabled.setStatus(_A)
_ApIfwireMcsSuppIndex_Type=Integer32
_ApIfwireMcsSuppIndex_Object=MibTableColumn
apIfwireMcsSuppIndex=_ApIfwireMcsSuppIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,34),_ApIfwireMcsSuppIndex_Type())
apIfwireMcsSuppIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfwireMcsSuppIndex.setStatus(_A)
_ApIfwireMcsMandIndex_Type=Integer32
_ApIfwireMcsMandIndex_Object=MibTableColumn
apIfwireMcsMandIndex=_ApIfwireMcsMandIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,35),_ApIfwireMcsMandIndex_Type())
apIfwireMcsMandIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfwireMcsMandIndex.setStatus(_A)
_ApIfwire11nSuppEnable_Type=Integer32
_ApIfwire11nSuppEnable_Object=MibTableColumn
apIfwire11nSuppEnable=_ApIfwire11nSuppEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,36),_ApIfwire11nSuppEnable_Type())
apIfwire11nSuppEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfwire11nSuppEnable.setStatus(_A)
_ApShtRetryThld_Type=Integer32
_ApShtRetryThld_Object=MibTableColumn
apShtRetryThld=_ApShtRetryThld_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,37),_ApShtRetryThld_Type())
apShtRetryThld.setMaxAccess(_C)
if mibBuilder.loadTexts:apShtRetryThld.setStatus(_A)
_ApLongRetryThld_Type=Integer32
_ApLongRetryThld_Object=MibTableColumn
apLongRetryThld=_ApLongRetryThld_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,38),_ApLongRetryThld_Type())
apLongRetryThld.setMaxAccess(_C)
if mibBuilder.loadTexts:apLongRetryThld.setStatus(_A)
_ApIfWireResponseRssi_Type=Integer32
_ApIfWireResponseRssi_Object=MibTableColumn
apIfWireResponseRssi=_ApIfWireResponseRssi_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,39),_ApIfWireResponseRssi_Type())
apIfWireResponseRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWireResponseRssi.setStatus(_A)
_ApIfWireMaxStationLimit_Type=Integer32
_ApIfWireMaxStationLimit_Object=MibTableColumn
apIfWireMaxStationLimit=_ApIfWireMaxStationLimit_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,40),_ApIfWireMaxStationLimit_Type())
apIfWireMaxStationLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfWireMaxStationLimit.setStatus(_A)
_ApIfWireLinkscan_Type=Integer32
_ApIfWireLinkscan_Object=MibTableColumn
apIfWireLinkscan=_ApIfWireLinkscan_Object((1,3,6,1,4,1,27514,1,1,10,2,81,2,3,1,1,41),_ApIfWireLinkscan_Type())
apIfWireLinkscan.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfWireLinkscan.setStatus(_A)
_ApSSIDConfigObjects_ObjectIdentity=ObjectIdentity
apSSIDConfigObjects=_ApSSIDConfigObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,3))
_ApSSIDListCreateTable_Object=MibTable
apSSIDListCreateTable=_ApSSIDListCreateTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,1))
if mibBuilder.loadTexts:apSSIDListCreateTable.setStatus(_A)
_ApSSIDListCreateTableEntry_Object=MibTableRow
apSSIDListCreateTableEntry=_ApSSIDListCreateTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,1,1))
apSSIDListCreateTableEntry.setIndexNames((0,_D,_x),(0,_D,_y),(0,_E,_R))
if mibBuilder.loadTexts:apSSIDListCreateTableEntry.setStatus(_A)
_ApSSIDAPMac_Type=MacAddress
_ApSSIDAPMac_Object=MibTableColumn
apSSIDAPMac=_ApSSIDAPMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,1,1,1),_ApSSIDAPMac_Type())
apSSIDAPMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDAPMac.setStatus(_A)
_ApSSIDRadioId_Type=Integer32
_ApSSIDRadioId_Object=MibTableColumn
apSSIDRadioId=_ApSSIDRadioId_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,1,1,2),_ApSSIDRadioId_Type())
apSSIDRadioId.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDRadioId.setStatus(_A)
_ApSSIDListName_Type=DisplayString
_ApSSIDListName_Object=MibTableColumn
apSSIDListName=_ApSSIDListName_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,1,1,3),_ApSSIDListName_Type())
apSSIDListName.setMaxAccess(_H)
if mibBuilder.loadTexts:apSSIDListName.setStatus(_A)
_ApListBSSIDAddr_Type=MacAddress
_ApListBSSIDAddr_Object=MibTableColumn
apListBSSIDAddr=_ApListBSSIDAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,1,1,4),_ApListBSSIDAddr_Type())
apListBSSIDAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:apListBSSIDAddr.setStatus(_A)
_ApSSIDListStatus_Type=RowStatus
_ApSSIDListStatus_Object=MibTableColumn
apSSIDListStatus=_ApSSIDListStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,1,1,5),_ApSSIDListStatus_Type())
apSSIDListStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:apSSIDListStatus.setStatus(_A)
_ApSSIDConfigTable_Object=MibTable
apSSIDConfigTable=_ApSSIDConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,2))
if mibBuilder.loadTexts:apSSIDConfigTable.setStatus(_A)
_ApSSIDConfigTableEntry_Object=MibTableRow
apSSIDConfigTableEntry=_ApSSIDConfigTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,2,1))
apSSIDConfigTableEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:apSSIDConfigTableEntry.setStatus(_A)
class _ApSSIDName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ApSSIDName_Type.__name__=_L
_ApSSIDName_Object=MibTableColumn
apSSIDName=_ApSSIDName_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,2,1,1),_ApSSIDName_Type())
apSSIDName.setMaxAccess(_H)
if mibBuilder.loadTexts:apSSIDName.setStatus(_A)
_ApSSIDEnabled_Type=TruthValue
_ApSSIDEnabled_Object=MibTableColumn
apSSIDEnabled=_ApSSIDEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,2,1,2),_ApSSIDEnabled_Type())
apSSIDEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:apSSIDEnabled.setStatus(_A)
_ApSSIDHidden_Type=TruthValue
_ApSSIDHidden_Object=MibTableColumn
apSSIDHidden=_ApSSIDHidden_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,2,1,3),_ApSSIDHidden_Type())
apSSIDHidden.setMaxAccess(_H)
if mibBuilder.loadTexts:apSSIDHidden.setStatus(_A)
_ApStaIsolate_Type=TruthValue
_ApStaIsolate_Object=MibTableColumn
apStaIsolate=_ApStaIsolate_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,2,1,4),_ApStaIsolate_Type())
apStaIsolate.setMaxAccess(_H)
if mibBuilder.loadTexts:apStaIsolate.setStatus(_A)
class _ApDot11Auth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_z,0),(_A0,1)))
_ApDot11Auth_Type.__name__=_G
_ApDot11Auth_Object=MibTableColumn
apDot11Auth=_ApDot11Auth_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,2,1,5),_ApDot11Auth_Type())
apDot11Auth.setMaxAccess(_H)
if mibBuilder.loadTexts:apDot11Auth.setStatus(_A)
class _ApsecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_S,0),('wpa',1),('wpa2',2),('wapi',3)))
_ApsecurityMode_Type.__name__=_G
_ApsecurityMode_Object=MibTableColumn
apsecurityMode=_ApsecurityMode_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,2,1,6),_ApsecurityMode_Type())
apsecurityMode.setMaxAccess(_H)
if mibBuilder.loadTexts:apsecurityMode.setStatus(_A)
class _ApAuthenMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_S,0),('psk',1),('radius',2),('wapicer',3),('web',4),('psk-web',5),(_A1,6),('wapipsk',7)))
_ApAuthenMode_Type.__name__=_G
_ApAuthenMode_Object=MibTableColumn
apAuthenMode=_ApAuthenMode_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,2,1,7),_ApAuthenMode_Type())
apAuthenMode.setMaxAccess(_H)
if mibBuilder.loadTexts:apAuthenMode.setStatus(_A)
class _ApSecurityCiphers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_S,0),('wep40',1),('wep104',2),('tkip',3),('aesccmp',4),('wapisms4',5)))
_ApSecurityCiphers_Type.__name__=_G
_ApSecurityCiphers_Object=MibTableColumn
apSecurityCiphers=_ApSecurityCiphers_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,2,1,8),_ApSecurityCiphers_Type())
apSecurityCiphers.setMaxAccess(_H)
if mibBuilder.loadTexts:apSecurityCiphers.setStatus(_A)
_ApVlanId_Type=Integer32
_ApVlanId_Object=MibTableColumn
apVlanId=_ApVlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,2,1,9),_ApVlanId_Type())
apVlanId.setMaxAccess(_H)
if mibBuilder.loadTexts:apVlanId.setStatus(_A)
_ApVlanIpAddr_Type=IpAddress
_ApVlanIpAddr_Object=MibTableColumn
apVlanIpAddr=_ApVlanIpAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,2,1,10),_ApVlanIpAddr_Type())
apVlanIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:apVlanIpAddr.setStatus(_A)
_ApMaxSimultUsers_Type=Counter32
_ApMaxSimultUsers_Object=MibTableColumn
apMaxSimultUsers=_ApMaxSimultUsers_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,2,1,11),_ApMaxSimultUsers_Type())
apMaxSimultUsers.setMaxAccess(_H)
if mibBuilder.loadTexts:apMaxSimultUsers.setStatus(_A)
_ApStaUplinkMaxRate_Type=Counter32
_ApStaUplinkMaxRate_Object=MibTableColumn
apStaUplinkMaxRate=_ApStaUplinkMaxRate_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,2,1,12),_ApStaUplinkMaxRate_Type())
apStaUplinkMaxRate.setMaxAccess(_H)
if mibBuilder.loadTexts:apStaUplinkMaxRate.setStatus(_A)
_ApStaDwlinkMaxRate_Type=Counter32
_ApStaDwlinkMaxRate_Object=MibTableColumn
apStaDwlinkMaxRate=_ApStaDwlinkMaxRate_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,2,1,13),_ApStaDwlinkMaxRate_Type())
apStaDwlinkMaxRate.setMaxAccess(_H)
if mibBuilder.loadTexts:apStaDwlinkMaxRate.setStatus(_A)
_ApSSIDCfgStatus_Type=RowStatus
_ApSSIDCfgStatus_Object=MibTableColumn
apSSIDCfgStatus=_ApSSIDCfgStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,81,3,2,1,14),_ApSSIDCfgStatus_Type())
apSSIDCfgStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:apSSIDCfgStatus.setStatus(_A)
_ApSecurityConfigObjects_ObjectIdentity=ObjectIdentity
apSecurityConfigObjects=_ApSecurityConfigObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,4))
_ApSecurityConfigTable_Object=MibTable
apSecurityConfigTable=_ApSecurityConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,4,1))
if mibBuilder.loadTexts:apSecurityConfigTable.setStatus(_A)
_ApSecurityConfigTableEntry_Object=MibTableRow
apSecurityConfigTableEntry=_ApSecurityConfigTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,4,1,1))
apSecurityConfigTableEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:apSecurityConfigTableEntry.setStatus(_A)
_ApWEPCipherKeyIndex_Type=Integer32
_ApWEPCipherKeyIndex_Object=MibTableColumn
apWEPCipherKeyIndex=_ApWEPCipherKeyIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,81,4,1,1,1),_ApWEPCipherKeyIndex_Type())
apWEPCipherKeyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:apWEPCipherKeyIndex.setStatus(_A)
_ApWEPCipherKeyValue_Type=DisplayString
_ApWEPCipherKeyValue_Object=MibTableColumn
apWEPCipherKeyValue=_ApWEPCipherKeyValue_Object((1,3,6,1,4,1,27514,1,1,10,2,81,4,1,1,2),_ApWEPCipherKeyValue_Type())
apWEPCipherKeyValue.setMaxAccess(_C)
if mibBuilder.loadTexts:apWEPCipherKeyValue.setStatus(_A)
class _ApWEPCipherKeyCharType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('hex',0),('char',1)))
_ApWEPCipherKeyCharType_Type.__name__=_G
_ApWEPCipherKeyCharType_Object=MibTableColumn
apWEPCipherKeyCharType=_ApWEPCipherKeyCharType_Object((1,3,6,1,4,1,27514,1,1,10,2,81,4,1,1,3),_ApWEPCipherKeyCharType_Type())
apWEPCipherKeyCharType.setMaxAccess(_C)
if mibBuilder.loadTexts:apWEPCipherKeyCharType.setStatus(_A)
_ApPSKCipherKeyValue_Type=DisplayString
_ApPSKCipherKeyValue_Object=MibTableColumn
apPSKCipherKeyValue=_ApPSKCipherKeyValue_Object((1,3,6,1,4,1,27514,1,1,10,2,81,4,1,1,4),_ApPSKCipherKeyValue_Type())
apPSKCipherKeyValue.setMaxAccess(_C)
if mibBuilder.loadTexts:apPSKCipherKeyValue.setStatus(_A)
class _ApPSKCipherKeyCharType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('hex',0),('char',1)))
_ApPSKCipherKeyCharType_Type.__name__=_G
_ApPSKCipherKeyCharType_Object=MibTableColumn
apPSKCipherKeyCharType=_ApPSKCipherKeyCharType_Object((1,3,6,1,4,1,27514,1,1,10,2,81,4,1,1,5),_ApPSKCipherKeyCharType_Type())
apPSKCipherKeyCharType.setMaxAccess(_C)
if mibBuilder.loadTexts:apPSKCipherKeyCharType.setStatus(_A)
_ApWAPIAuthModeEnable_Type=TruthValue
_ApWAPIAuthModeEnable_Object=MibTableColumn
apWAPIAuthModeEnable=_ApWAPIAuthModeEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,4,1,1,6),_ApWAPIAuthModeEnable_Type())
apWAPIAuthModeEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIAuthModeEnable.setStatus(_A)
_ApWAPIASIPAddress_Type=IpAddress
_ApWAPIASIPAddress_Object=MibTableColumn
apWAPIASIPAddress=_ApWAPIASIPAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,81,4,1,1,7),_ApWAPIASIPAddress_Type())
apWAPIASIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIASIPAddress.setStatus(_A)
_ApWAPIIsInstalledCer_Type=TruthValue
_ApWAPIIsInstalledCer_Object=MibTableColumn
apWAPIIsInstalledCer=_ApWAPIIsInstalledCer_Object((1,3,6,1,4,1,27514,1,1,10,2,81,4,1,1,8),_ApWAPIIsInstalledCer_Type())
apWAPIIsInstalledCer.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIIsInstalledCer.setStatus(_A)
_ApWAPIExternInfoConfigObjects_ObjectIdentity=ObjectIdentity
apWAPIExternInfoConfigObjects=_ApWAPIExternInfoConfigObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,5))
_ApWAPIExternInfoConfigTable_Object=MibTable
apWAPIExternInfoConfigTable=_ApWAPIExternInfoConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1))
if mibBuilder.loadTexts:apWAPIExternInfoConfigTable.setStatus(_A)
_ApWAPIExternInfoConfigTableEntry_Object=MibTableRow
apWAPIExternInfoConfigTableEntry=_ApWAPIExternInfoConfigTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1))
apWAPIExternInfoConfigTableEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:apWAPIExternInfoConfigTableEntry.setStatus(_A)
_ApWAPIConfigVersion_Type=Integer32
_ApWAPIConfigVersion_Object=MibTableColumn
apWAPIConfigVersion=_ApWAPIConfigVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,1),_ApWAPIConfigVersion_Type())
apWAPIConfigVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIConfigVersion.setStatus(_A)
_ApWAPIControlledAuthControl_Type=TruthValue
_ApWAPIControlledAuthControl_Object=MibTableColumn
apWAPIControlledAuthControl=_ApWAPIControlledAuthControl_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,2),_ApWAPIControlledAuthControl_Type())
apWAPIControlledAuthControl.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIControlledAuthControl.setStatus(_A)
_ApWAPIControlledPortControl_Type=Integer32
_ApWAPIControlledPortControl_Object=MibTableColumn
apWAPIControlledPortControl=_ApWAPIControlledPortControl_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,3),_ApWAPIControlledPortControl_Type())
apWAPIControlledPortControl.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIControlledPortControl.setStatus(_A)
_ApWAPIOptionImplemented_Type=TruthValue
_ApWAPIOptionImplemented_Object=MibTableColumn
apWAPIOptionImplemented=_ApWAPIOptionImplemented_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,4),_ApWAPIOptionImplemented_Type())
apWAPIOptionImplemented.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIOptionImplemented.setStatus(_A)
_ApWAPIPreauthenticationImplemented_Type=TruthValue
_ApWAPIPreauthenticationImplemented_Object=MibTableColumn
apWAPIPreauthenticationImplemented=_ApWAPIPreauthenticationImplemented_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,5),_ApWAPIPreauthenticationImplemented_Type())
apWAPIPreauthenticationImplemented.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIPreauthenticationImplemented.setStatus(_A)
_ApWAPIEnabled_Type=TruthValue
_ApWAPIEnabled_Object=MibTableColumn
apWAPIEnabled=_ApWAPIEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,6),_ApWAPIEnabled_Type())
apWAPIEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIEnabled.setStatus(_A)
_ApWAPIPreauthEnabled_Type=TruthValue
_ApWAPIPreauthEnabled_Object=MibTableColumn
apWAPIPreauthEnabled=_ApWAPIPreauthEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,7),_ApWAPIPreauthEnabled_Type())
apWAPIPreauthEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIPreauthEnabled.setStatus(_A)
_ApWAPIUnicastKeysSupported_Type=Unsigned32
_ApWAPIUnicastKeysSupported_Object=MibTableColumn
apWAPIUnicastKeysSupported=_ApWAPIUnicastKeysSupported_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,8),_ApWAPIUnicastKeysSupported_Type())
apWAPIUnicastKeysSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIUnicastKeysSupported.setStatus(_A)
class _ApWAPIUnicastRekeyMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('disabled',0),(_A2,1),(_A3,2),(_A4,3)))
_ApWAPIUnicastRekeyMethod_Type.__name__=_G
_ApWAPIUnicastRekeyMethod_Object=MibTableColumn
apWAPIUnicastRekeyMethod=_ApWAPIUnicastRekeyMethod_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,9),_ApWAPIUnicastRekeyMethod_Type())
apWAPIUnicastRekeyMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIUnicastRekeyMethod.setStatus(_A)
class _ApWAPIUnicastRekeyTime_Type(Unsigned32):defaultValue=86400;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ApWAPIUnicastRekeyTime_Type.__name__=_K
_ApWAPIUnicastRekeyTime_Object=MibTableColumn
apWAPIUnicastRekeyTime=_ApWAPIUnicastRekeyTime_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,10),_ApWAPIUnicastRekeyTime_Type())
apWAPIUnicastRekeyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIUnicastRekeyTime.setStatus(_A)
if mibBuilder.loadTexts:apWAPIUnicastRekeyTime.setUnits(_Y)
class _ApWAPIUnicastRekeyPackets_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ApWAPIUnicastRekeyPackets_Type.__name__=_K
_ApWAPIUnicastRekeyPackets_Object=MibTableColumn
apWAPIUnicastRekeyPackets=_ApWAPIUnicastRekeyPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,11),_ApWAPIUnicastRekeyPackets_Type())
apWAPIUnicastRekeyPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIUnicastRekeyPackets.setStatus(_A)
if mibBuilder.loadTexts:apWAPIUnicastRekeyPackets.setUnits(_A5)
class _ApWAPIMulticastCipher_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ApWAPIMulticastCipher_Type.__name__=_N
_ApWAPIMulticastCipher_Object=MibTableColumn
apWAPIMulticastCipher=_ApWAPIMulticastCipher_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,12),_ApWAPIMulticastCipher_Type())
apWAPIMulticastCipher.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIMulticastCipher.setStatus(_A)
class _ApWAPIMulticastRekeyMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('disabled',0),(_A2,1),(_A3,2),(_A4,3)))
_ApWAPIMulticastRekeyMethod_Type.__name__=_G
_ApWAPIMulticastRekeyMethod_Object=MibTableColumn
apWAPIMulticastRekeyMethod=_ApWAPIMulticastRekeyMethod_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,13),_ApWAPIMulticastRekeyMethod_Type())
apWAPIMulticastRekeyMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIMulticastRekeyMethod.setStatus(_A)
class _ApWAPIMulticastRekeyTime_Type(Unsigned32):defaultValue=86400;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ApWAPIMulticastRekeyTime_Type.__name__=_K
_ApWAPIMulticastRekeyTime_Object=MibTableColumn
apWAPIMulticastRekeyTime=_ApWAPIMulticastRekeyTime_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,14),_ApWAPIMulticastRekeyTime_Type())
apWAPIMulticastRekeyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIMulticastRekeyTime.setStatus(_A)
if mibBuilder.loadTexts:apWAPIMulticastRekeyTime.setUnits(_Y)
class _ApWAPIMulticastRekeyPackets_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ApWAPIMulticastRekeyPackets_Type.__name__=_K
_ApWAPIMulticastRekeyPackets_Object=MibTableColumn
apWAPIMulticastRekeyPackets=_ApWAPIMulticastRekeyPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,15),_ApWAPIMulticastRekeyPackets_Type())
apWAPIMulticastRekeyPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIMulticastRekeyPackets.setStatus(_A)
if mibBuilder.loadTexts:apWAPIMulticastRekeyPackets.setUnits(_A5)
_ApWAPIMulticastRekeyStrict_Type=TruthValue
_ApWAPIMulticastRekeyStrict_Object=MibTableColumn
apWAPIMulticastRekeyStrict=_ApWAPIMulticastRekeyStrict_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,16),_ApWAPIMulticastRekeyStrict_Type())
apWAPIMulticastRekeyStrict.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIMulticastRekeyStrict.setStatus(_A)
class _ApWAPIPSKValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_ApWAPIPSKValue_Type.__name__=_N
_ApWAPIPSKValue_Object=MibTableColumn
apWAPIPSKValue=_ApWAPIPSKValue_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,17),_ApWAPIPSKValue_Type())
apWAPIPSKValue.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIPSKValue.setStatus(_A)
_ApWAPIPSKPassPhrase_Type=DisplayString
_ApWAPIPSKPassPhrase_Object=MibTableColumn
apWAPIPSKPassPhrase=_ApWAPIPSKPassPhrase_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,18),_ApWAPIPSKPassPhrase_Type())
apWAPIPSKPassPhrase.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIPSKPassPhrase.setStatus(_A)
class _ApWAPICertificateUpdateCount_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ApWAPICertificateUpdateCount_Type.__name__=_K
_ApWAPICertificateUpdateCount_Object=MibTableColumn
apWAPICertificateUpdateCount=_ApWAPICertificateUpdateCount_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,19),_ApWAPICertificateUpdateCount_Type())
apWAPICertificateUpdateCount.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPICertificateUpdateCount.setStatus(_A)
class _ApWAPIMulticastUpdateCount_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ApWAPIMulticastUpdateCount_Type.__name__=_K
_ApWAPIMulticastUpdateCount_Object=MibTableColumn
apWAPIMulticastUpdateCount=_ApWAPIMulticastUpdateCount_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,20),_ApWAPIMulticastUpdateCount_Type())
apWAPIMulticastUpdateCount.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIMulticastUpdateCount.setStatus(_A)
class _ApWAPIUnicastUpdateCount_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ApWAPIUnicastUpdateCount_Type.__name__=_K
_ApWAPIUnicastUpdateCount_Object=MibTableColumn
apWAPIUnicastUpdateCount=_ApWAPIUnicastUpdateCount_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,21),_ApWAPIUnicastUpdateCount_Type())
apWAPIUnicastUpdateCount.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIUnicastUpdateCount.setStatus(_A)
class _ApWAPIMulticastCipherSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ApWAPIMulticastCipherSize_Type.__name__=_K
_ApWAPIMulticastCipherSize_Object=MibTableColumn
apWAPIMulticastCipherSize=_ApWAPIMulticastCipherSize_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,22),_ApWAPIMulticastCipherSize_Type())
apWAPIMulticastCipherSize.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIMulticastCipherSize.setStatus(_A)
class _ApWAPIBKLifetime_Type(Unsigned32):defaultValue=43200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ApWAPIBKLifetime_Type.__name__=_K
_ApWAPIBKLifetime_Object=MibTableColumn
apWAPIBKLifetime=_ApWAPIBKLifetime_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,23),_ApWAPIBKLifetime_Type())
apWAPIBKLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIBKLifetime.setStatus(_A)
if mibBuilder.loadTexts:apWAPIBKLifetime.setUnits(_Y)
class _ApWAPIBKReauthThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ApWAPIBKReauthThreshold_Type.__name__=_K
_ApWAPIBKReauthThreshold_Object=MibTableColumn
apWAPIBKReauthThreshold=_ApWAPIBKReauthThreshold_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,24),_ApWAPIBKReauthThreshold_Type())
apWAPIBKReauthThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIBKReauthThreshold.setStatus(_A)
if mibBuilder.loadTexts:apWAPIBKReauthThreshold.setUnits('percentage')
class _ApWAPISATimeout_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ApWAPISATimeout_Type.__name__=_K
_ApWAPISATimeout_Object=MibTableColumn
apWAPISATimeout=_ApWAPISATimeout_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,25),_ApWAPISATimeout_Type())
apWAPISATimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPISATimeout.setStatus(_A)
if mibBuilder.loadTexts:apWAPISATimeout.setUnits(_Y)
class _ApWAPIAuthSuiteSelected_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ApWAPIAuthSuiteSelected_Type.__name__=_N
_ApWAPIAuthSuiteSelected_Object=MibTableColumn
apWAPIAuthSuiteSelected=_ApWAPIAuthSuiteSelected_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,26),_ApWAPIAuthSuiteSelected_Type())
apWAPIAuthSuiteSelected.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIAuthSuiteSelected.setStatus(_A)
class _ApWAPIUnicastCipherSelected_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ApWAPIUnicastCipherSelected_Type.__name__=_N
_ApWAPIUnicastCipherSelected_Object=MibTableColumn
apWAPIUnicastCipherSelected=_ApWAPIUnicastCipherSelected_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,27),_ApWAPIUnicastCipherSelected_Type())
apWAPIUnicastCipherSelected.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIUnicastCipherSelected.setStatus(_A)
class _ApWAPIMulticastCipherSelected_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ApWAPIMulticastCipherSelected_Type.__name__=_N
_ApWAPIMulticastCipherSelected_Object=MibTableColumn
apWAPIMulticastCipherSelected=_ApWAPIMulticastCipherSelected_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,28),_ApWAPIMulticastCipherSelected_Type())
apWAPIMulticastCipherSelected.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIMulticastCipherSelected.setStatus(_A)
class _ApWAPIBKIDUsed_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_ApWAPIBKIDUsed_Type.__name__=_N
_ApWAPIBKIDUsed_Object=MibTableColumn
apWAPIBKIDUsed=_ApWAPIBKIDUsed_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,29),_ApWAPIBKIDUsed_Type())
apWAPIBKIDUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIBKIDUsed.setStatus(_A)
class _ApWAPIAuthSuiteRequested_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ApWAPIAuthSuiteRequested_Type.__name__=_N
_ApWAPIAuthSuiteRequested_Object=MibTableColumn
apWAPIAuthSuiteRequested=_ApWAPIAuthSuiteRequested_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,30),_ApWAPIAuthSuiteRequested_Type())
apWAPIAuthSuiteRequested.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIAuthSuiteRequested.setStatus(_A)
class _ApWAPIUnicastCipherRequested_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ApWAPIUnicastCipherRequested_Type.__name__=_N
_ApWAPIUnicastCipherRequested_Object=MibTableColumn
apWAPIUnicastCipherRequested=_ApWAPIUnicastCipherRequested_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,31),_ApWAPIUnicastCipherRequested_Type())
apWAPIUnicastCipherRequested.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIUnicastCipherRequested.setStatus(_A)
class _ApWAPIMulticastCipherRequested_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ApWAPIMulticastCipherRequested_Type.__name__=_N
_ApWAPIMulticastCipherRequested_Object=MibTableColumn
apWAPIMulticastCipherRequested=_ApWAPIMulticastCipherRequested_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,32),_ApWAPIMulticastCipherRequested_Type())
apWAPIMulticastCipherRequested.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIMulticastCipherRequested.setStatus(_A)
_ApWAPIUnicastCipher_Type=OctetString
_ApWAPIUnicastCipher_Object=MibTableColumn
apWAPIUnicastCipher=_ApWAPIUnicastCipher_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,33),_ApWAPIUnicastCipher_Type())
apWAPIUnicastCipher.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIUnicastCipher.setStatus(_A)
_ApWAPIUnicastCipherEnabled_Type=TruthValue
_ApWAPIUnicastCipherEnabled_Object=MibTableColumn
apWAPIUnicastCipherEnabled=_ApWAPIUnicastCipherEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,34),_ApWAPIUnicastCipherEnabled_Type())
apWAPIUnicastCipherEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIUnicastCipherEnabled.setStatus(_A)
_ApWAPIUnicastCipherSize_Type=Unsigned32
_ApWAPIUnicastCipherSize_Object=MibTableColumn
apWAPIUnicastCipherSize=_ApWAPIUnicastCipherSize_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,35),_ApWAPIUnicastCipherSize_Type())
apWAPIUnicastCipherSize.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIUnicastCipherSize.setStatus(_A)
_ApWAPIAuthenticationSuite_Type=OctetString
_ApWAPIAuthenticationSuite_Object=MibTableColumn
apWAPIAuthenticationSuite=_ApWAPIAuthenticationSuite_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,36),_ApWAPIAuthenticationSuite_Type())
apWAPIAuthenticationSuite.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIAuthenticationSuite.setStatus(_A)
_ApWAPIAuthenticationSuiteEnabled_Type=TruthValue
_ApWAPIAuthenticationSuiteEnabled_Object=MibTableColumn
apWAPIAuthenticationSuiteEnabled=_ApWAPIAuthenticationSuiteEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,37),_ApWAPIAuthenticationSuiteEnabled_Type())
apWAPIAuthenticationSuiteEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIAuthenticationSuiteEnabled.setStatus(_A)
_ApWAPIAECertFile_Type=DisplayString
_ApWAPIAECertFile_Object=MibTableColumn
apWAPIAECertFile=_ApWAPIAECertFile_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,38),_ApWAPIAECertFile_Type())
apWAPIAECertFile.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIAECertFile.setStatus(_A)
_ApWAPICACertFile_Type=DisplayString
_ApWAPICACertFile_Object=MibTableColumn
apWAPICACertFile=_ApWAPICACertFile_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,39),_ApWAPICACertFile_Type())
apWAPICACertFile.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPICACertFile.setStatus(_A)
_ApWAPIASUCertFile_Type=DisplayString
_ApWAPIASUCertFile_Object=MibTableColumn
apWAPIASUCertFile=_ApWAPIASUCertFile_Object((1,3,6,1,4,1,27514,1,1,10,2,81,5,1,1,40),_ApWAPIASUCertFile_Type())
apWAPIASUCertFile.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIASUCertFile.setStatus(_A)
_ApStationInfoGetObjects_ObjectIdentity=ObjectIdentity
apStationInfoGetObjects=_ApStationInfoGetObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,6))
_ApStationInfoGetTable_Object=MibTable
apStationInfoGetTable=_ApStationInfoGetTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1))
if mibBuilder.loadTexts:apStationInfoGetTable.setStatus(_A)
_ApStationInfoGetTableEntry_Object=MibTableRow
apStationInfoGetTableEntry=_ApStationInfoGetTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1,1))
apStationInfoGetTableEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:apStationInfoGetTableEntry.setStatus(_A)
_ApStaMAC_Type=MacAddress
_ApStaMAC_Object=MibTableColumn
apStaMAC=_ApStaMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1,1,1),_ApStaMAC_Type())
apStaMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaMAC.setStatus(_A)
class _ApStaWMMAttr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('nonwmmsta',0),('wmmsta',1)))
_ApStaWMMAttr_Type.__name__=_G
_ApStaWMMAttr_Object=MibTableColumn
apStaWMMAttr=_ApStaWMMAttr_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1,1,2),_ApStaWMMAttr_Type())
apStaWMMAttr.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaWMMAttr.setStatus(_A)
_ApStaIPAddress_Type=IpAddress
_ApStaIPAddress_Object=MibTableColumn
apStaIPAddress=_ApStaIPAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1,1,3),_ApStaIPAddress_Type())
apStaIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaIPAddress.setStatus(_A)
class _ApStaRadioMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_d,0),(_e,1),('dot11g',2),('dot11n',3)))
_ApStaRadioMode_Type.__name__=_G
_ApStaRadioMode_Object=MibTableColumn
apStaRadioMode=_ApStaRadioMode_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1,1,4),_ApStaRadioMode_Type())
apStaRadioMode.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaRadioMode.setStatus(_A)
_ApStaRadioChannel_Type=Integer32
_ApStaRadioChannel_Object=MibTableColumn
apStaRadioChannel=_ApStaRadioChannel_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1,1,5),_ApStaRadioChannel_Type())
apStaRadioChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaRadioChannel.setStatus(_A)
_ApAPTxRates_Type=Integer32
_ApAPTxRates_Object=MibTableColumn
apAPTxRates=_ApAPTxRates_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1,1,6),_ApAPTxRates_Type())
apAPTxRates.setMaxAccess(_B)
if mibBuilder.loadTexts:apAPTxRates.setStatus(_A)
class _ApStaPowerSaveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('active',0),('powersave',1)))
_ApStaPowerSaveMode_Type.__name__=_G
_ApStaPowerSaveMode_Object=MibTableColumn
apStaPowerSaveMode=_ApStaPowerSaveMode_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1,1,7),_ApStaPowerSaveMode_Type())
apStaPowerSaveMode.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaPowerSaveMode.setStatus(_A)
_ApStaVlanId_Type=Counter32
_ApStaVlanId_Object=MibTableColumn
apStaVlanId=_ApStaVlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1,1,8),_ApStaVlanId_Type())
apStaVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaVlanId.setStatus(_A)
_ApStaSSIDName_Type=DisplayString
_ApStaSSIDName_Object=MibTableColumn
apStaSSIDName=_ApStaSSIDName_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1,1,9),_ApStaSSIDName_Type())
apStaSSIDName.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaSSIDName.setStatus(_A)
_ApAPId_Type=Integer32
_ApAPId_Object=MibTableColumn
apAPId=_ApAPId_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1,1,10),_ApAPId_Type())
apAPId.setMaxAccess(_B)
if mibBuilder.loadTexts:apAPId.setStatus(_A)
class _ApStaDot11Auth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_z,0),(_A0,1)))
_ApStaDot11Auth_Type.__name__=_G
_ApStaDot11Auth_Object=MibTableColumn
apStaDot11Auth=_ApStaDot11Auth_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1,1,11),_ApStaDot11Auth_Type())
apStaDot11Auth.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaDot11Auth.setStatus(_A)
class _Apsecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_S,0),('wpa',1),('wpa2',2),('wapi',3)))
_Apsecurity_Type.__name__=_G
_Apsecurity_Object=MibTableColumn
apsecurity=_Apsecurity_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1,1,12),_Apsecurity_Type())
apsecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:apsecurity.setStatus(_A)
class _ApStaAuthenMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_S,0),('psk',1),('radius',2),('wapicer',3),('web',4),('psk-web',5),(_A1,6),('wapipsk',7)))
_ApStaAuthenMode_Type.__name__=_G
_ApStaAuthenMode_Object=MibTableColumn
apStaAuthenMode=_ApStaAuthenMode_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1,1,13),_ApStaAuthenMode_Type())
apStaAuthenMode.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaAuthenMode.setStatus(_A)
class _ApStaSecurityCiphers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_S,0),('wep40',1),('wep104',2),('tkip',3),('aesccmp',4),('wpisms4',5)))
_ApStaSecurityCiphers_Type.__name__=_G
_ApStaSecurityCiphers_Object=MibTableColumn
apStaSecurityCiphers=_ApStaSecurityCiphers_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1,1,14),_ApStaSecurityCiphers_Type())
apStaSecurityCiphers.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaSecurityCiphers.setStatus(_A)
_ApAPIdMac_Type=MacAddress
_ApAPIdMac_Object=MibTableColumn
apAPIdMac=_ApAPIdMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1,1,15),_ApAPIdMac_Type())
apAPIdMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apAPIdMac.setStatus(_A)
class _ApStaMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16)));namedValues=NamedValues(*((_d,1),(_e,2),('dot11g',4),('dot11an',8),('dot11gn',16)))
_ApStaMode_Type.__name__=_G
_ApStaMode_Object=MibTableColumn
apStaMode=_ApStaMode_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1,1,16),_ApStaMode_Type())
apStaMode.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaMode.setStatus(_A)
_ApStaBand_Type=Integer32
_ApStaBand_Object=MibTableColumn
apStaBand=_ApStaBand_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,1,1,17),_ApStaBand_Type())
apStaBand.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaBand.setStatus(_A)
_ApStationRefusedAccessTable_Object=MibTable
apStationRefusedAccessTable=_ApStationRefusedAccessTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,2))
if mibBuilder.loadTexts:apStationRefusedAccessTable.setStatus(_A)
_ApStationRefusedAccessTableEntry_Object=MibTableRow
apStationRefusedAccessTableEntry=_ApStationRefusedAccessTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,2,1))
apStationRefusedAccessTableEntry.setIndexNames((0,_D,_A6))
if mibBuilder.loadTexts:apStationRefusedAccessTableEntry.setStatus(_A)
_ApRefusedStaMAC_Type=MacAddress
_ApRefusedStaMAC_Object=MibTableColumn
apRefusedStaMAC=_ApRefusedStaMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,2,1,1),_ApRefusedStaMAC_Type())
apRefusedStaMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:apRefusedStaMAC.setStatus(_A)
_ApFailReason_Type=Integer32
_ApFailReason_Object=MibTableColumn
apFailReason=_ApFailReason_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,2,1,2),_ApFailReason_Type())
apFailReason.setMaxAccess(_B)
if mibBuilder.loadTexts:apFailReason.setStatus(_A)
_ApRefusedTime_Type=DisplayString
_ApRefusedTime_Object=MibTableColumn
apRefusedTime=_ApRefusedTime_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,2,1,3),_ApRefusedTime_Type())
apRefusedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:apRefusedTime.setStatus(_A)
_ApRefusedAPMac_Type=MacAddress
_ApRefusedAPMac_Object=MibTableColumn
apRefusedAPMac=_ApRefusedAPMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,2,1,4),_ApRefusedAPMac_Type())
apRefusedAPMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apRefusedAPMac.setStatus(_A)
_ApStationRadiusInfoTable_Object=MibTable
apStationRadiusInfoTable=_ApStationRadiusInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,3))
if mibBuilder.loadTexts:apStationRadiusInfoTable.setStatus(_A)
_ApStationRadiusInfoTableEntry_Object=MibTableRow
apStationRadiusInfoTableEntry=_ApStationRadiusInfoTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,3,1))
apStationRadiusInfoTableEntry.setIndexNames((0,_E,_F),(0,_D,_A7))
if mibBuilder.loadTexts:apStationRadiusInfoTableEntry.setStatus(_A)
_ApUserMacAddress_Type=MacAddress
_ApUserMacAddress_Object=MibTableColumn
apUserMacAddress=_ApUserMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,3,1,1),_ApUserMacAddress_Type())
apUserMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:apUserMacAddress.setStatus(_A)
_ApUserIpAddress_Type=IpAddress
_ApUserIpAddress_Object=MibTableColumn
apUserIpAddress=_ApUserIpAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,3,1,2),_ApUserIpAddress_Type())
apUserIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:apUserIpAddress.setStatus(_A)
_ApUserLoginName_Type=OctetString
_ApUserLoginName_Object=MibTableColumn
apUserLoginName=_ApUserLoginName_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,3,1,3),_ApUserLoginName_Type())
apUserLoginName.setMaxAccess(_B)
if mibBuilder.loadTexts:apUserLoginName.setStatus(_A)
_ApUserLoginTime_Type=OctetString
_ApUserLoginTime_Object=MibTableColumn
apUserLoginTime=_ApUserLoginTime_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,3,1,4),_ApUserLoginTime_Type())
apUserLoginTime.setMaxAccess(_B)
if mibBuilder.loadTexts:apUserLoginTime.setStatus(_A)
_ApUserOnlineTime_Type=TimeTicks
_ApUserOnlineTime_Object=MibTableColumn
apUserOnlineTime=_ApUserOnlineTime_Object((1,3,6,1,4,1,27514,1,1,10,2,81,6,3,1,5),_ApUserOnlineTime_Type())
apUserOnlineTime.setMaxAccess(_B)
if mibBuilder.loadTexts:apUserOnlineTime.setStatus(_A)
_ApQOSInfoConfigObjects_ObjectIdentity=ObjectIdentity
apQOSInfoConfigObjects=_ApQOSInfoConfigObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,7))
_ApQOSWirelessConfigObjects_ObjectIdentity=ObjectIdentity
apQOSWirelessConfigObjects=_ApQOSWirelessConfigObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,7,1))
_ApQOSWirelessConfigTable_Object=MibTable
apQOSWirelessConfigTable=_ApQOSWirelessConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,1,1))
if mibBuilder.loadTexts:apQOSWirelessConfigTable.setStatus(_A)
_ApQOSWirelessConfigTableEntry_Object=MibTableRow
apQOSWirelessConfigTableEntry=_ApQOSWirelessConfigTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,1,1,1))
apQOSWirelessConfigTableEntry.setIndexNames((0,_E,_F),(0,_E,_J),(0,_D,_A8))
if mibBuilder.loadTexts:apQOSWirelessConfigTableEntry.setStatus(_A)
class _ApWireQoSTrafficClassId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_A9,0),(_AA,1),('video',2),('voice',3)))
_ApWireQoSTrafficClassId_Type.__name__=_G
_ApWireQoSTrafficClassId_Object=MibTableColumn
apWireQoSTrafficClassId=_ApWireQoSTrafficClassId_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,1,1,1,1),_ApWireQoSTrafficClassId_Type())
apWireQoSTrafficClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:apWireQoSTrafficClassId.setStatus(_A)
_ApWireQosAIFS_Type=Integer32
_ApWireQosAIFS_Object=MibTableColumn
apWireQosAIFS=_ApWireQosAIFS_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,1,1,1,2),_ApWireQosAIFS_Type())
apWireQosAIFS.setMaxAccess(_C)
if mibBuilder.loadTexts:apWireQosAIFS.setStatus(_A)
_ApWireQoSCWmin_Type=Integer32
_ApWireQoSCWmin_Object=MibTableColumn
apWireQoSCWmin=_ApWireQoSCWmin_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,1,1,1,3),_ApWireQoSCWmin_Type())
apWireQoSCWmin.setMaxAccess(_C)
if mibBuilder.loadTexts:apWireQoSCWmin.setStatus(_A)
_ApWireQoSCWmax_Type=Integer32
_ApWireQoSCWmax_Object=MibTableColumn
apWireQoSCWmax=_ApWireQoSCWmax_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,1,1,1,4),_ApWireQoSCWmax_Type())
apWireQoSCWmax.setMaxAccess(_C)
if mibBuilder.loadTexts:apWireQoSCWmax.setStatus(_A)
_ApWireQoSTXOPLim_Type=Integer32
_ApWireQoSTXOPLim_Object=MibTableColumn
apWireQoSTXOPLim=_ApWireQoSTXOPLim_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,1,1,1,5),_ApWireQoSTXOPLim_Type())
apWireQoSTXOPLim.setMaxAccess(_C)
if mibBuilder.loadTexts:apWireQoSTXOPLim.setStatus(_A)
_ApQOSBaseInfoConfigObjects_ObjectIdentity=ObjectIdentity
apQOSBaseInfoConfigObjects=_ApQOSBaseInfoConfigObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,7,2))
_ApQOSBaseInfoConfigTable_Object=MibTable
apQOSBaseInfoConfigTable=_ApQOSBaseInfoConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1))
if mibBuilder.loadTexts:apQOSBaseInfoConfigTable.setStatus(_A)
_ApQOSBaseInfoConfigTableEntry_Object=MibTableRow
apQOSBaseInfoConfigTableEntry=_ApQOSBaseInfoConfigTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1))
apQOSBaseInfoConfigTableEntry.setIndexNames((0,_E,_F),(0,_E,_J))
if mibBuilder.loadTexts:apQOSBaseInfoConfigTableEntry.setStatus(_A)
class _ApBaseQoSTrafficClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_AA,0),(_A9,1),('video',2),('voice',3)))
_ApBaseQoSTrafficClass_Type.__name__=_G
_ApBaseQoSTrafficClass_Object=MibTableColumn
apBaseQoSTrafficClass=_ApBaseQoSTrafficClass_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,1),_ApBaseQoSTrafficClass_Type())
apBaseQoSTrafficClass.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSTrafficClass.setStatus(_A)
_ApBaseQoSEnabled_Type=TruthValue
_ApBaseQoSEnabled_Object=MibTableColumn
apBaseQoSEnabled=_ApBaseQoSEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,2),_ApBaseQoSEnabled_Type())
apBaseQoSEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSEnabled.setStatus(_A)
_ApBaseQoSBW_Type=Integer32
_ApBaseQoSBW_Object=MibTableColumn
apBaseQoSBW=_ApBaseQoSBW_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,3),_ApBaseQoSBW_Type())
apBaseQoSBW.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSBW.setStatus(_A)
_ApBaseQoSResPercent_Type=Integer32
_ApBaseQoSResPercent_Object=MibTableColumn
apBaseQoSResPercent=_ApBaseQoSResPercent_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,4),_ApBaseQoSResPercent_Type())
apBaseQoSResPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSResPercent.setStatus(_A)
_ApBaseQoSsharedBW_Type=Integer32
_ApBaseQoSsharedBW_Object=MibTableColumn
apBaseQoSsharedBW=_ApBaseQoSsharedBW_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,5),_ApBaseQoSsharedBW_Type())
apBaseQoSsharedBW.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSsharedBW.setStatus(_A)
_ApBaseQoSsharedBWPercent_Type=Integer32
_ApBaseQoSsharedBWPercent_Object=MibTableColumn
apBaseQoSsharedBWPercent=_ApBaseQoSsharedBWPercent_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,6),_ApBaseQoSsharedBWPercent_Type())
apBaseQoSsharedBWPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSsharedBWPercent.setStatus(_A)
_ApBaseQoSSchedAlgName_Type=DisplayString
_ApBaseQoSSchedAlgName_Object=MibTableColumn
apBaseQoSSchedAlgName=_ApBaseQoSSchedAlgName_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,7),_ApBaseQoSSchedAlgName_Type())
apBaseQoSSchedAlgName.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSSchedAlgName.setStatus(_A)
_ApBaseQoSResPolicyEnabled_Type=TruthValue
_ApBaseQoSResPolicyEnabled_Object=MibTableColumn
apBaseQoSResPolicyEnabled=_ApBaseQoSResPolicyEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,8),_ApBaseQoSResPolicyEnabled_Type())
apBaseQoSResPolicyEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSResPolicyEnabled.setStatus(_A)
_ApBaseQoSResPolicyName_Type=DisplayString
_ApBaseQoSResPolicyName_Object=MibTableColumn
apBaseQoSResPolicyName=_ApBaseQoSResPolicyName_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,9),_ApBaseQoSResPolicyName_Type())
apBaseQoSResPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSResPolicyName.setStatus(_A)
_ApBaseQoSBackgroundSvcAvgSpeed_Type=Integer32
_ApBaseQoSBackgroundSvcAvgSpeed_Object=MibTableColumn
apBaseQoSBackgroundSvcAvgSpeed=_ApBaseQoSBackgroundSvcAvgSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,10),_ApBaseQoSBackgroundSvcAvgSpeed_Type())
apBaseQoSBackgroundSvcAvgSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSBackgroundSvcAvgSpeed.setStatus(_A)
_ApBaseQoSBackgroundSvcMaxBurst_Type=Integer32
_ApBaseQoSBackgroundSvcMaxBurst_Object=MibTableColumn
apBaseQoSBackgroundSvcMaxBurst=_ApBaseQoSBackgroundSvcMaxBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,11),_ApBaseQoSBackgroundSvcMaxBurst_Type())
apBaseQoSBackgroundSvcMaxBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSBackgroundSvcMaxBurst.setStatus(_A)
_ApBaseQoSBackgroundSvcPriority_Type=Integer32
_ApBaseQoSBackgroundSvcPriority_Object=MibTableColumn
apBaseQoSBackgroundSvcPriority=_ApBaseQoSBackgroundSvcPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,12),_ApBaseQoSBackgroundSvcPriority_Type())
apBaseQoSBackgroundSvcPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSBackgroundSvcPriority.setStatus(_A)
_ApBaseQoSBackgroundSvcResPriority_Type=Integer32
_ApBaseQoSBackgroundSvcResPriority_Object=MibTableColumn
apBaseQoSBackgroundSvcResPriority=_ApBaseQoSBackgroundSvcResPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,13),_ApBaseQoSBackgroundSvcResPriority_Type())
apBaseQoSBackgroundSvcResPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSBackgroundSvcResPriority.setStatus(_A)
_ApBaseQoSBestEffortSvcAvgSpeed_Type=Integer32
_ApBaseQoSBestEffortSvcAvgSpeed_Object=MibTableColumn
apBaseQoSBestEffortSvcAvgSpeed=_ApBaseQoSBestEffortSvcAvgSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,14),_ApBaseQoSBestEffortSvcAvgSpeed_Type())
apBaseQoSBestEffortSvcAvgSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSBestEffortSvcAvgSpeed.setStatus(_A)
_ApBaseQoSBestEffortSvcMaxBurst_Type=Integer32
_ApBaseQoSBestEffortSvcMaxBurst_Object=MibTableColumn
apBaseQoSBestEffortSvcMaxBurst=_ApBaseQoSBestEffortSvcMaxBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,15),_ApBaseQoSBestEffortSvcMaxBurst_Type())
apBaseQoSBestEffortSvcMaxBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSBestEffortSvcMaxBurst.setStatus(_A)
_ApBaseQoSBestEffortSvcPriority_Type=Integer32
_ApBaseQoSBestEffortSvcPriority_Object=MibTableColumn
apBaseQoSBestEffortSvcPriority=_ApBaseQoSBestEffortSvcPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,16),_ApBaseQoSBestEffortSvcPriority_Type())
apBaseQoSBestEffortSvcPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSBestEffortSvcPriority.setStatus(_A)
_ApBaseQoSBestEffortSvcResPriority_Type=Integer32
_ApBaseQoSBestEffortSvcResPriority_Object=MibTableColumn
apBaseQoSBestEffortSvcResPriority=_ApBaseQoSBestEffortSvcResPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,17),_ApBaseQoSBestEffortSvcResPriority_Type())
apBaseQoSBestEffortSvcResPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSBestEffortSvcResPriority.setStatus(_A)
_ApBaseQoSVoiceSvcAvgSpeed_Type=Integer32
_ApBaseQoSVoiceSvcAvgSpeed_Object=MibTableColumn
apBaseQoSVoiceSvcAvgSpeed=_ApBaseQoSVoiceSvcAvgSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,18),_ApBaseQoSVoiceSvcAvgSpeed_Type())
apBaseQoSVoiceSvcAvgSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSVoiceSvcAvgSpeed.setStatus(_A)
_ApBaseQoSVoiceSvcMaxBurst_Type=Integer32
_ApBaseQoSVoiceSvcMaxBurst_Object=MibTableColumn
apBaseQoSVoiceSvcMaxBurst=_ApBaseQoSVoiceSvcMaxBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,19),_ApBaseQoSVoiceSvcMaxBurst_Type())
apBaseQoSVoiceSvcMaxBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSVoiceSvcMaxBurst.setStatus(_A)
_ApBaseQoSVoiceSvcPriority_Type=Integer32
_ApBaseQoSVoiceSvcPriority_Object=MibTableColumn
apBaseQoSVoiceSvcPriority=_ApBaseQoSVoiceSvcPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,20),_ApBaseQoSVoiceSvcPriority_Type())
apBaseQoSVoiceSvcPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSVoiceSvcPriority.setStatus(_A)
_ApBaseQoSVoiceSvcResPriority_Type=Integer32
_ApBaseQoSVoiceSvcResPriority_Object=MibTableColumn
apBaseQoSVoiceSvcResPriority=_ApBaseQoSVoiceSvcResPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,21),_ApBaseQoSVoiceSvcResPriority_Type())
apBaseQoSVoiceSvcResPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSVoiceSvcResPriority.setStatus(_A)
_ApBaseQoSVideoSvcAvgSpeed_Type=Integer32
_ApBaseQoSVideoSvcAvgSpeed_Object=MibTableColumn
apBaseQoSVideoSvcAvgSpeed=_ApBaseQoSVideoSvcAvgSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,22),_ApBaseQoSVideoSvcAvgSpeed_Type())
apBaseQoSVideoSvcAvgSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSVideoSvcAvgSpeed.setStatus(_A)
_ApBaseQoSVideoSvcMaxBurst_Type=Integer32
_ApBaseQoSVideoSvcMaxBurst_Object=MibTableColumn
apBaseQoSVideoSvcMaxBurst=_ApBaseQoSVideoSvcMaxBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,23),_ApBaseQoSVideoSvcMaxBurst_Type())
apBaseQoSVideoSvcMaxBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSVideoSvcMaxBurst.setStatus(_A)
_ApBaseQoSVideoSvcPriority_Type=Integer32
_ApBaseQoSVideoSvcPriority_Object=MibTableColumn
apBaseQoSVideoSvcPriority=_ApBaseQoSVideoSvcPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,24),_ApBaseQoSVideoSvcPriority_Type())
apBaseQoSVideoSvcPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSVideoSvcPriority.setStatus(_A)
_ApBaseQoSVideoSvcResPriority_Type=Integer32
_ApBaseQoSVideoSvcResPriority_Object=MibTableColumn
apBaseQoSVideoSvcResPriority=_ApBaseQoSVideoSvcResPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,2,1,1,25),_ApBaseQoSVideoSvcResPriority_Type())
apBaseQoSVideoSvcResPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:apBaseQoSVideoSvcResPriority.setStatus(_A)
_ApQOSBackgroundCfgObjects_ObjectIdentity=ObjectIdentity
apQOSBackgroundCfgObjects=_ApQOSBackgroundCfgObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,7,3))
_ApQOSBackgroundCfgTable_Object=MibTable
apQOSBackgroundCfgTable=_ApQOSBackgroundCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,3,1))
if mibBuilder.loadTexts:apQOSBackgroundCfgTable.setStatus(_A)
_ApQOSBackgroundCfgTableEntry_Object=MibTableRow
apQOSBackgroundCfgTableEntry=_ApQOSBackgroundCfgTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,3,1,1))
apQOSBackgroundCfgTableEntry.setIndexNames((0,_E,_F),(0,_E,_J))
if mibBuilder.loadTexts:apQOSBackgroundCfgTableEntry.setStatus(_A)
_ApQOSBgMaxSvcCnt_Type=Integer32
_ApQOSBgMaxSvcCnt_Object=MibTableColumn
apQOSBgMaxSvcCnt=_ApQOSBgMaxSvcCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,3,1,1,1),_ApQOSBgMaxSvcCnt_Type())
apQOSBgMaxSvcCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSBgMaxSvcCnt.setStatus(_A)
_ApQOSBgSvcBW_Type=Integer32
_ApQOSBgSvcBW_Object=MibTableColumn
apQOSBgSvcBW=_ApQOSBgSvcBW_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,3,1,1,2),_ApQOSBgSvcBW_Type())
apQOSBgSvcBW.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSBgSvcBW.setStatus(_A)
_ApQOSBgSvcBWPercent_Type=Integer32
_ApQOSBgSvcBWPercent_Object=MibTableColumn
apQOSBgSvcBWPercent=_ApQOSBgSvcBWPercent_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,3,1,1,3),_ApQOSBgSvcBWPercent_Type())
apQOSBgSvcBWPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSBgSvcBWPercent.setStatus(_A)
_ApQOSBgIsUseWREDAlg_Type=TruthValue
_ApQOSBgIsUseWREDAlg_Object=MibTableColumn
apQOSBgIsUseWREDAlg=_ApQOSBgIsUseWREDAlg_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,3,1,1,4),_ApQOSBgIsUseWREDAlg_Type())
apQOSBgIsUseWREDAlg.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSBgIsUseWREDAlg.setStatus(_A)
_ApQOSBgIsUseTrafficShaping_Type=TruthValue
_ApQOSBgIsUseTrafficShaping_Object=MibTableColumn
apQOSBgIsUseTrafficShaping=_ApQOSBgIsUseTrafficShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,3,1,1,5),_ApQOSBgIsUseTrafficShaping_Type())
apQOSBgIsUseTrafficShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSBgIsUseTrafficShaping.setStatus(_A)
_ApQOSBestEffortCfgObjects_ObjectIdentity=ObjectIdentity
apQOSBestEffortCfgObjects=_ApQOSBestEffortCfgObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,7,4))
_ApQOSBestEffortCfgTable_Object=MibTable
apQOSBestEffortCfgTable=_ApQOSBestEffortCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,4,1))
if mibBuilder.loadTexts:apQOSBestEffortCfgTable.setStatus(_A)
_ApQOSBestEffortCfgTableEntry_Object=MibTableRow
apQOSBestEffortCfgTableEntry=_ApQOSBestEffortCfgTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,4,1,1))
apQOSBestEffortCfgTableEntry.setIndexNames((0,_E,_F),(0,_E,_J))
if mibBuilder.loadTexts:apQOSBestEffortCfgTableEntry.setStatus(_A)
_ApQOSBeMaxSvcCnt_Type=Integer32
_ApQOSBeMaxSvcCnt_Object=MibTableColumn
apQOSBeMaxSvcCnt=_ApQOSBeMaxSvcCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,4,1,1,1),_ApQOSBeMaxSvcCnt_Type())
apQOSBeMaxSvcCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSBeMaxSvcCnt.setStatus(_A)
_ApQOSBeSvcBW_Type=Integer32
_ApQOSBeSvcBW_Object=MibTableColumn
apQOSBeSvcBW=_ApQOSBeSvcBW_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,4,1,1,2),_ApQOSBeSvcBW_Type())
apQOSBeSvcBW.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSBeSvcBW.setStatus(_A)
_ApQOSBeSvcBWPercent_Type=Integer32
_ApQOSBeSvcBWPercent_Object=MibTableColumn
apQOSBeSvcBWPercent=_ApQOSBeSvcBWPercent_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,4,1,1,3),_ApQOSBeSvcBWPercent_Type())
apQOSBeSvcBWPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSBeSvcBWPercent.setStatus(_A)
_ApQOSBeIsUseWREDAlg_Type=TruthValue
_ApQOSBeIsUseWREDAlg_Object=MibTableColumn
apQOSBeIsUseWREDAlg=_ApQOSBeIsUseWREDAlg_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,4,1,1,4),_ApQOSBeIsUseWREDAlg_Type())
apQOSBeIsUseWREDAlg.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSBeIsUseWREDAlg.setStatus(_A)
_ApQOSBeIsUseTrafficShaping_Type=TruthValue
_ApQOSBeIsUseTrafficShaping_Object=MibTableColumn
apQOSBeIsUseTrafficShaping=_ApQOSBeIsUseTrafficShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,4,1,1,5),_ApQOSBeIsUseTrafficShaping_Type())
apQOSBeIsUseTrafficShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSBeIsUseTrafficShaping.setStatus(_A)
_ApQOSVoiceInfoCfgObjects_ObjectIdentity=ObjectIdentity
apQOSVoiceInfoCfgObjects=_ApQOSVoiceInfoCfgObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,7,5))
_ApQOSVoiceInfoCfgTable_Object=MibTable
apQOSVoiceInfoCfgTable=_ApQOSVoiceInfoCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,5,1))
if mibBuilder.loadTexts:apQOSVoiceInfoCfgTable.setStatus(_A)
_ApQOSVoiceInfoCfgTableEntry_Object=MibTableRow
apQOSVoiceInfoCfgTableEntry=_ApQOSVoiceInfoCfgTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,5,1,1))
apQOSVoiceInfoCfgTableEntry.setIndexNames((0,_E,_F),(0,_E,_J))
if mibBuilder.loadTexts:apQOSVoiceInfoCfgTableEntry.setStatus(_A)
_ApQOSVoiceMaxSvcCnt_Type=Integer32
_ApQOSVoiceMaxSvcCnt_Object=MibTableColumn
apQOSVoiceMaxSvcCnt=_ApQOSVoiceMaxSvcCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,5,1,1,1),_ApQOSVoiceMaxSvcCnt_Type())
apQOSVoiceMaxSvcCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSVoiceMaxSvcCnt.setStatus(_A)
_ApQOSVoiceSvcBW_Type=Integer32
_ApQOSVoiceSvcBW_Object=MibTableColumn
apQOSVoiceSvcBW=_ApQOSVoiceSvcBW_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,5,1,1,2),_ApQOSVoiceSvcBW_Type())
apQOSVoiceSvcBW.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSVoiceSvcBW.setStatus(_A)
_ApQOSVoiceSvcBWPercent_Type=Integer32
_ApQOSVoiceSvcBWPercent_Object=MibTableColumn
apQOSVoiceSvcBWPercent=_ApQOSVoiceSvcBWPercent_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,5,1,1,3),_ApQOSVoiceSvcBWPercent_Type())
apQOSVoiceSvcBWPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSVoiceSvcBWPercent.setStatus(_A)
_ApQOSVoiceIsUseStreamBasedQueue_Type=TruthValue
_ApQOSVoiceIsUseStreamBasedQueue_Object=MibTableColumn
apQOSVoiceIsUseStreamBasedQueue=_ApQOSVoiceIsUseStreamBasedQueue_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,5,1,1,4),_ApQOSVoiceIsUseStreamBasedQueue_Type())
apQOSVoiceIsUseStreamBasedQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSVoiceIsUseStreamBasedQueue.setStatus(_A)
_ApQOSVoiceStreamMaxQueueLen_Type=Integer32
_ApQOSVoiceStreamMaxQueueLen_Object=MibTableColumn
apQOSVoiceStreamMaxQueueLen=_ApQOSVoiceStreamMaxQueueLen_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,5,1,1,5),_ApQOSVoiceStreamMaxQueueLen_Type())
apQOSVoiceStreamMaxQueueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSVoiceStreamMaxQueueLen.setStatus(_A)
_ApQOSVoiceStreamAvgSpeed_Type=Integer32
_ApQOSVoiceStreamAvgSpeed_Object=MibTableColumn
apQOSVoiceStreamAvgSpeed=_ApQOSVoiceStreamAvgSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,5,1,1,6),_ApQOSVoiceStreamAvgSpeed_Type())
apQOSVoiceStreamAvgSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSVoiceStreamAvgSpeed.setStatus(_A)
_ApQOSVoiceStreamMaxBurst_Type=Integer32
_ApQOSVoiceStreamMaxBurst_Object=MibTableColumn
apQOSVoiceStreamMaxBurst=_ApQOSVoiceStreamMaxBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,5,1,1,7),_ApQOSVoiceStreamMaxBurst_Type())
apQOSVoiceStreamMaxBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSVoiceStreamMaxBurst.setStatus(_A)
_ApQOSVoiceIsUseWREDAlg_Type=TruthValue
_ApQOSVoiceIsUseWREDAlg_Object=MibTableColumn
apQOSVoiceIsUseWREDAlg=_ApQOSVoiceIsUseWREDAlg_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,5,1,1,8),_ApQOSVoiceIsUseWREDAlg_Type())
apQOSVoiceIsUseWREDAlg.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSVoiceIsUseWREDAlg.setStatus(_A)
_ApQOSVoiceIsUseTrafficShaping_Type=TruthValue
_ApQOSVoiceIsUseTrafficShaping_Object=MibTableColumn
apQOSVoiceIsUseTrafficShaping=_ApQOSVoiceIsUseTrafficShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,5,1,1,9),_ApQOSVoiceIsUseTrafficShaping_Type())
apQOSVoiceIsUseTrafficShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSVoiceIsUseTrafficShaping.setStatus(_A)
_ApQOSVideoInfoCfgObjects_ObjectIdentity=ObjectIdentity
apQOSVideoInfoCfgObjects=_ApQOSVideoInfoCfgObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,7,6))
_ApQOSVideoInfoCfgTable_Object=MibTable
apQOSVideoInfoCfgTable=_ApQOSVideoInfoCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,6,1))
if mibBuilder.loadTexts:apQOSVideoInfoCfgTable.setStatus(_A)
_ApQOSVideoInfoCfgTableEntry_Object=MibTableRow
apQOSVideoInfoCfgTableEntry=_ApQOSVideoInfoCfgTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,6,1,1))
apQOSVideoInfoCfgTableEntry.setIndexNames((0,_E,_F),(0,_E,_J))
if mibBuilder.loadTexts:apQOSVideoInfoCfgTableEntry.setStatus(_A)
_ApQOSVideoMaxSvcCnt_Type=Integer32
_ApQOSVideoMaxSvcCnt_Object=MibTableColumn
apQOSVideoMaxSvcCnt=_ApQOSVideoMaxSvcCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,6,1,1,1),_ApQOSVideoMaxSvcCnt_Type())
apQOSVideoMaxSvcCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSVideoMaxSvcCnt.setStatus(_A)
_ApQOSVideoSvcBW_Type=Integer32
_ApQOSVideoSvcBW_Object=MibTableColumn
apQOSVideoSvcBW=_ApQOSVideoSvcBW_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,6,1,1,2),_ApQOSVideoSvcBW_Type())
apQOSVideoSvcBW.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSVideoSvcBW.setStatus(_A)
_ApQOSVideoSvcBWPercent_Type=Integer32
_ApQOSVideoSvcBWPercent_Object=MibTableColumn
apQOSVideoSvcBWPercent=_ApQOSVideoSvcBWPercent_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,6,1,1,3),_ApQOSVideoSvcBWPercent_Type())
apQOSVideoSvcBWPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSVideoSvcBWPercent.setStatus(_A)
_ApQOSVideoIsUseStreamBasedQueue_Type=TruthValue
_ApQOSVideoIsUseStreamBasedQueue_Object=MibTableColumn
apQOSVideoIsUseStreamBasedQueue=_ApQOSVideoIsUseStreamBasedQueue_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,6,1,1,4),_ApQOSVideoIsUseStreamBasedQueue_Type())
apQOSVideoIsUseStreamBasedQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSVideoIsUseStreamBasedQueue.setStatus(_A)
_ApQOSVideoStreamMaxQueueLen_Type=Integer32
_ApQOSVideoStreamMaxQueueLen_Object=MibTableColumn
apQOSVideoStreamMaxQueueLen=_ApQOSVideoStreamMaxQueueLen_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,6,1,1,5),_ApQOSVideoStreamMaxQueueLen_Type())
apQOSVideoStreamMaxQueueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSVideoStreamMaxQueueLen.setStatus(_A)
_ApQOSVideoStreamAvgSpeed_Type=Integer32
_ApQOSVideoStreamAvgSpeed_Object=MibTableColumn
apQOSVideoStreamAvgSpeed=_ApQOSVideoStreamAvgSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,6,1,1,6),_ApQOSVideoStreamAvgSpeed_Type())
apQOSVideoStreamAvgSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSVideoStreamAvgSpeed.setStatus(_A)
_ApQOSVideoStreamMaxBurst_Type=Integer32
_ApQOSVideoStreamMaxBurst_Object=MibTableColumn
apQOSVideoStreamMaxBurst=_ApQOSVideoStreamMaxBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,6,1,1,7),_ApQOSVideoStreamMaxBurst_Type())
apQOSVideoStreamMaxBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSVideoStreamMaxBurst.setStatus(_A)
_ApQOSVideoIsUseWREDAlg_Type=TruthValue
_ApQOSVideoIsUseWREDAlg_Object=MibTableColumn
apQOSVideoIsUseWREDAlg=_ApQOSVideoIsUseWREDAlg_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,6,1,1,8),_ApQOSVideoIsUseWREDAlg_Type())
apQOSVideoIsUseWREDAlg.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSVideoIsUseWREDAlg.setStatus(_A)
_ApQOSVideoIsUseTrafficShaping_Type=TruthValue
_ApQOSVideoIsUseTrafficShaping_Object=MibTableColumn
apQOSVideoIsUseTrafficShaping=_ApQOSVideoIsUseTrafficShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,6,1,1,9),_ApQOSVideoIsUseTrafficShaping_Type())
apQOSVideoIsUseTrafficShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSVideoIsUseTrafficShaping.setStatus(_A)
_ApQOSWMMConfigObjects_ObjectIdentity=ObjectIdentity
apQOSWMMConfigObjects=_ApQOSWMMConfigObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,7,7))
_ApQOSWMMConfigTable_Object=MibTable
apQOSWMMConfigTable=_ApQOSWMMConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1))
if mibBuilder.loadTexts:apQOSWMMConfigTable.setStatus(_A)
_ApQOSWMMConfigTableEntry_Object=MibTableRow
apQOSWMMConfigTableEntry=_ApQOSWMMConfigTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1))
apQOSWMMConfigTableEntry.setIndexNames((0,_E,_F),(0,_E,_J))
if mibBuilder.loadTexts:apQOSWMMConfigTableEntry.setStatus(_A)
class _ApQOSMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_S,0),('wmm',1),('dot8011e',2),('wmm80211e',3)))
_ApQOSMode_Type.__name__=_G
_ApQOSMode_Object=MibTableColumn
apQOSMode=_ApQOSMode_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,1),_ApQOSMode_Type())
apQOSMode.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSMode.setStatus(_A)
_ApQOSUpdateSeq_Type=Integer32
_ApQOSUpdateSeq_Object=MibTableColumn
apQOSUpdateSeq=_ApQOSUpdateSeq_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,2),_ApQOSUpdateSeq_Type())
apQOSUpdateSeq.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSUpdateSeq.setStatus(_A)
_ApQOSSvpAcIndex_Type=Integer32
_ApQOSSvpAcIndex_Object=MibTableColumn
apQOSSvpAcIndex=_ApQOSSvpAcIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,3),_ApQOSSvpAcIndex_Type())
apQOSSvpAcIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSSvpAcIndex.setStatus(_A)
_ApQOSUapsd_Type=Integer32
_ApQOSUapsd_Object=MibTableColumn
apQOSUapsd=_ApQOSUapsd_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,4),_ApQOSUapsd_Type())
apQOSUapsd.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSUapsd.setStatus(_A)
_ApQOSAcIndx1_Type=Integer32
_ApQOSAcIndx1_Object=MibTableColumn
apQOSAcIndx1=_ApQOSAcIndx1_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,5),_ApQOSAcIndx1_Type())
apQOSAcIndx1.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSAcIndx1.setStatus(_A)
_ApQOSAcIndx2_Type=Integer32
_ApQOSAcIndx2_Object=MibTableColumn
apQOSAcIndx2=_ApQOSAcIndx2_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,6),_ApQOSAcIndx2_Type())
apQOSAcIndx2.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSAcIndx2.setStatus(_A)
_ApQOSAcIndx3_Type=Integer32
_ApQOSAcIndx3_Object=MibTableColumn
apQOSAcIndx3=_ApQOSAcIndx3_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,7),_ApQOSAcIndx3_Type())
apQOSAcIndx3.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSAcIndx3.setStatus(_A)
_ApQOSAcIndx4_Type=Integer32
_ApQOSAcIndx4_Object=MibTableColumn
apQOSAcIndx4=_ApQOSAcIndx4_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,8),_ApQOSAcIndx4_Type())
apQOSAcIndx4.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSAcIndx4.setStatus(_A)
_ApQOSAifsn1_Type=Integer32
_ApQOSAifsn1_Object=MibTableColumn
apQOSAifsn1=_ApQOSAifsn1_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,9),_ApQOSAifsn1_Type())
apQOSAifsn1.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSAifsn1.setStatus(_A)
_ApQOSAifsn2_Type=Integer32
_ApQOSAifsn2_Object=MibTableColumn
apQOSAifsn2=_ApQOSAifsn2_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,10),_ApQOSAifsn2_Type())
apQOSAifsn2.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSAifsn2.setStatus(_A)
_ApQOSAifsn3_Type=Integer32
_ApQOSAifsn3_Object=MibTableColumn
apQOSAifsn3=_ApQOSAifsn3_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,11),_ApQOSAifsn3_Type())
apQOSAifsn3.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSAifsn3.setStatus(_A)
_ApQOSAifsn4_Type=Integer32
_ApQOSAifsn4_Object=MibTableColumn
apQOSAifsn4=_ApQOSAifsn4_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,12),_ApQOSAifsn4_Type())
apQOSAifsn4.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSAifsn4.setStatus(_A)
_ApQOSEcwMin1_Type=Integer32
_ApQOSEcwMin1_Object=MibTableColumn
apQOSEcwMin1=_ApQOSEcwMin1_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,13),_ApQOSEcwMin1_Type())
apQOSEcwMin1.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSEcwMin1.setStatus(_A)
_ApQOSEcwMin2_Type=Integer32
_ApQOSEcwMin2_Object=MibTableColumn
apQOSEcwMin2=_ApQOSEcwMin2_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,14),_ApQOSEcwMin2_Type())
apQOSEcwMin2.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSEcwMin2.setStatus(_A)
_ApQOSEcwMin3_Type=Integer32
_ApQOSEcwMin3_Object=MibTableColumn
apQOSEcwMin3=_ApQOSEcwMin3_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,15),_ApQOSEcwMin3_Type())
apQOSEcwMin3.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSEcwMin3.setStatus(_A)
_ApQOSEcwMin4_Type=Integer32
_ApQOSEcwMin4_Object=MibTableColumn
apQOSEcwMin4=_ApQOSEcwMin4_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,16),_ApQOSEcwMin4_Type())
apQOSEcwMin4.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSEcwMin4.setStatus(_A)
_ApQOSEcwMax1_Type=Integer32
_ApQOSEcwMax1_Object=MibTableColumn
apQOSEcwMax1=_ApQOSEcwMax1_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,17),_ApQOSEcwMax1_Type())
apQOSEcwMax1.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSEcwMax1.setStatus(_A)
_ApQOSEcwMax2_Type=Integer32
_ApQOSEcwMax2_Object=MibTableColumn
apQOSEcwMax2=_ApQOSEcwMax2_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,18),_ApQOSEcwMax2_Type())
apQOSEcwMax2.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSEcwMax2.setStatus(_A)
_ApQOSEcwMax3_Type=Integer32
_ApQOSEcwMax3_Object=MibTableColumn
apQOSEcwMax3=_ApQOSEcwMax3_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,19),_ApQOSEcwMax3_Type())
apQOSEcwMax3.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSEcwMax3.setStatus(_A)
_ApQOSEcwMax4_Type=Integer32
_ApQOSEcwMax4_Object=MibTableColumn
apQOSEcwMax4=_ApQOSEcwMax4_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,20),_ApQOSEcwMax4_Type())
apQOSEcwMax4.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSEcwMax4.setStatus(_A)
_ApQOSTxopLmt1_Type=Integer32
_ApQOSTxopLmt1_Object=MibTableColumn
apQOSTxopLmt1=_ApQOSTxopLmt1_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,21),_ApQOSTxopLmt1_Type())
apQOSTxopLmt1.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSTxopLmt1.setStatus(_A)
_ApQOSTxopLmt2_Type=Integer32
_ApQOSTxopLmt2_Object=MibTableColumn
apQOSTxopLmt2=_ApQOSTxopLmt2_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,22),_ApQOSTxopLmt2_Type())
apQOSTxopLmt2.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSTxopLmt2.setStatus(_A)
_ApQOSTxopLmt3_Type=Integer32
_ApQOSTxopLmt3_Object=MibTableColumn
apQOSTxopLmt3=_ApQOSTxopLmt3_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,23),_ApQOSTxopLmt3_Type())
apQOSTxopLmt3.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSTxopLmt3.setStatus(_A)
_ApQOSTxopLmt4_Type=Integer32
_ApQOSTxopLmt4_Object=MibTableColumn
apQOSTxopLmt4=_ApQOSTxopLmt4_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,24),_ApQOSTxopLmt4_Type())
apQOSTxopLmt4.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSTxopLmt4.setStatus(_A)
_ApQOSAcmAndAck1_Type=Integer32
_ApQOSAcmAndAck1_Object=MibTableColumn
apQOSAcmAndAck1=_ApQOSAcmAndAck1_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,25),_ApQOSAcmAndAck1_Type())
apQOSAcmAndAck1.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSAcmAndAck1.setStatus(_A)
_ApQOSAcmAndAck2_Type=Integer32
_ApQOSAcmAndAck2_Object=MibTableColumn
apQOSAcmAndAck2=_ApQOSAcmAndAck2_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,26),_ApQOSAcmAndAck2_Type())
apQOSAcmAndAck2.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSAcmAndAck2.setStatus(_A)
_ApQOSAcmAndAck3_Type=Integer32
_ApQOSAcmAndAck3_Object=MibTableColumn
apQOSAcmAndAck3=_ApQOSAcmAndAck3_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,27),_ApQOSAcmAndAck3_Type())
apQOSAcmAndAck3.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSAcmAndAck3.setStatus(_A)
_ApQOSAcmAndAck4_Type=Integer32
_ApQOSAcmAndAck4_Object=MibTableColumn
apQOSAcmAndAck4=_ApQOSAcmAndAck4_Object((1,3,6,1,4,1,27514,1,1,10,2,81,7,7,1,1,28),_ApQOSAcmAndAck4_Type())
apQOSAcmAndAck4.setMaxAccess(_C)
if mibBuilder.loadTexts:apQOSAcmAndAck4.setStatus(_A)
_ApAlarmParamConfigEntry_ObjectIdentity=ObjectIdentity
apAlarmParamConfigEntry=_ApAlarmParamConfigEntry_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,8))
_ApStaInterfNumThreshhd_Type=Integer32
_ApStaInterfNumThreshhd_Object=MibScalar
apStaInterfNumThreshhd=_ApStaInterfNumThreshhd_Object((1,3,6,1,4,1,27514,1,1,10,2,81,8,1),_ApStaInterfNumThreshhd_Type())
apStaInterfNumThreshhd.setMaxAccess(_C)
if mibBuilder.loadTexts:apStaInterfNumThreshhd.setStatus(_A)
_ApAPCoInterfThreshhd_Type=Integer32
_ApAPCoInterfThreshhd_Object=MibScalar
apAPCoInterfThreshhd=_ApAPCoInterfThreshhd_Object((1,3,6,1,4,1,27514,1,1,10,2,81,8,2),_ApAPCoInterfThreshhd_Type())
apAPCoInterfThreshhd.setMaxAccess(_C)
if mibBuilder.loadTexts:apAPCoInterfThreshhd.setStatus(_A)
_ApAPNeiborInterfThreshhd_Type=Integer32
_ApAPNeiborInterfThreshhd_Object=MibScalar
apAPNeiborInterfThreshhd=_ApAPNeiborInterfThreshhd_Object((1,3,6,1,4,1,27514,1,1,10,2,81,8,3),_ApAPNeiborInterfThreshhd_Type())
apAPNeiborInterfThreshhd.setMaxAccess(_C)
if mibBuilder.loadTexts:apAPNeiborInterfThreshhd.setStatus(_A)
_ApCPUusageThreshhd_Type=Integer32
_ApCPUusageThreshhd_Object=MibScalar
apCPUusageThreshhd=_ApCPUusageThreshhd_Object((1,3,6,1,4,1,27514,1,1,10,2,81,8,4),_ApCPUusageThreshhd_Type())
apCPUusageThreshhd.setMaxAccess(_C)
if mibBuilder.loadTexts:apCPUusageThreshhd.setStatus(_A)
_ApMemUsageThreshhd_Type=Integer32
_ApMemUsageThreshhd_Object=MibScalar
apMemUsageThreshhd=_ApMemUsageThreshhd_Object((1,3,6,1,4,1,27514,1,1,10,2,81,8,5),_ApMemUsageThreshhd_Type())
apMemUsageThreshhd.setMaxAccess(_C)
if mibBuilder.loadTexts:apMemUsageThreshhd.setStatus(_A)
_AcUserExcepOfflineTimes_Type=Counter32
_AcUserExcepOfflineTimes_Object=MibScalar
acUserExcepOfflineTimes=_AcUserExcepOfflineTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,8,6),_AcUserExcepOfflineTimes_Type())
acUserExcepOfflineTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:acUserExcepOfflineTimes.setStatus(_A)
_AcAuthReqTimes_Type=Counter32
_AcAuthReqTimes_Object=MibScalar
acAuthReqTimes=_AcAuthReqTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,8,7),_AcAuthReqTimes_Type())
acAuthReqTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:acAuthReqTimes.setStatus(_A)
_AcAuthSuccessTimes_Type=Counter32
_AcAuthSuccessTimes_Object=MibScalar
acAuthSuccessTimes=_AcAuthSuccessTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,8,8),_AcAuthSuccessTimes_Type())
acAuthSuccessTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:acAuthSuccessTimes.setStatus(_A)
_AcAuthReqFailTimes_Type=Counter32
_AcAuthReqFailTimes_Object=MibScalar
acAuthReqFailTimes=_AcAuthReqFailTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,8,9),_AcAuthReqFailTimes_Type())
acAuthReqFailTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:acAuthReqFailTimes.setStatus(_A)
_AcDisconnectOnlineUsersCount_Type=Counter32
_AcDisconnectOnlineUsersCount_Object=MibScalar
acDisconnectOnlineUsersCount=_AcDisconnectOnlineUsersCount_Object((1,3,6,1,4,1,27514,1,1,10,2,81,8,10),_AcDisconnectOnlineUsersCount_Type())
acDisconnectOnlineUsersCount.setMaxAccess(_B)
if mibBuilder.loadTexts:acDisconnectOnlineUsersCount.setStatus(_A)
_AcOnlineUserNum_Type=Counter32
_AcOnlineUserNum_Object=MibScalar
acOnlineUserNum=_AcOnlineUserNum_Object((1,3,6,1,4,1,27514,1,1,10,2,81,8,11),_AcOnlineUserNum_Type())
acOnlineUserNum.setMaxAccess(_B)
if mibBuilder.loadTexts:acOnlineUserNum.setStatus(_A)
_ApVLANConfigObjects_ObjectIdentity=ObjectIdentity
apVLANConfigObjects=_ApVLANConfigObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,9))
_ApVLANConfigTable_Object=MibTable
apVLANConfigTable=_ApVLANConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,9,1))
if mibBuilder.loadTexts:apVLANConfigTable.setStatus(_A)
_ApVLANConfigTableEntry_Object=MibTableRow
apVLANConfigTableEntry=_ApVLANConfigTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,9,1,1))
apVLANConfigTableEntry.setIndexNames((0,_q,_r),(0,_E,_R))
if mibBuilder.loadTexts:apVLANConfigTableEntry.setStatus(_A)
_ApVLANID_Type=Integer32
_ApVLANID_Object=MibTableColumn
apVLANID=_ApVLANID_Object((1,3,6,1,4,1,27514,1,1,10,2,81,9,1,1,1),_ApVLANID_Type())
apVLANID.setMaxAccess(_H)
if mibBuilder.loadTexts:apVLANID.setStatus(_A)
_ApVlanCfgStatus_Type=RowStatus
_ApVlanCfgStatus_Object=MibTableColumn
apVlanCfgStatus=_ApVlanCfgStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,81,9,1,1,2),_ApVlanCfgStatus_Type())
apVlanCfgStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:apVlanCfgStatus.setStatus(_A)
_ApStatisticsInfoReadObjects_ObjectIdentity=ObjectIdentity
apStatisticsInfoReadObjects=_ApStatisticsInfoReadObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,10))
_ApSysCapabilityStatisticsObjects_ObjectIdentity=ObjectIdentity
apSysCapabilityStatisticsObjects=_ApSysCapabilityStatisticsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,10,1))
_ApSysCapabilityStatisticsTable_Object=MibTable
apSysCapabilityStatisticsTable=_ApSysCapabilityStatisticsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,1,1))
if mibBuilder.loadTexts:apSysCapabilityStatisticsTable.setStatus(_A)
_ApSysCapabilityStatisticsTableEntry_Object=MibTableRow
apSysCapabilityStatisticsTableEntry=_ApSysCapabilityStatisticsTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,1,1,1))
apSysCapabilityStatisticsTableEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:apSysCapabilityStatisticsTableEntry.setStatus(_A)
_ApCPURTUsage_Type=Integer32
_ApCPURTUsage_Object=MibTableColumn
apCPURTUsage=_ApCPURTUsage_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,1,1,1,1),_ApCPURTUsage_Type())
apCPURTUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:apCPURTUsage.setStatus(_A)
_ApCPUAvgUsage_Type=Integer32
_ApCPUAvgUsage_Object=MibTableColumn
apCPUAvgUsage=_ApCPUAvgUsage_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,1,1,1,2),_ApCPUAvgUsage_Type())
apCPUAvgUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:apCPUAvgUsage.setStatus(_A)
_ApMemRTUsage_Type=Integer32
_ApMemRTUsage_Object=MibTableColumn
apMemRTUsage=_ApMemRTUsage_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,1,1,1,3),_ApMemRTUsage_Type())
apMemRTUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:apMemRTUsage.setStatus(_A)
_ApMemAvgUsage_Type=Integer32
_ApMemAvgUsage_Object=MibTableColumn
apMemAvgUsage=_ApMemAvgUsage_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,1,1,1,4),_ApMemAvgUsage_Type())
apMemAvgUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:apMemAvgUsage.setStatus(_A)
_ApLinkStatisticsObjects_ObjectIdentity=ObjectIdentity
apLinkStatisticsObjects=_ApLinkStatisticsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,10,2))
_ApLinkStatisticsTable_Object=MibTable
apLinkStatisticsTable=_ApLinkStatisticsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1))
if mibBuilder.loadTexts:apLinkStatisticsTable.setStatus(_A)
_ApLinkStatisticsTableEntry_Object=MibTableRow
apLinkStatisticsTableEntry=_ApLinkStatisticsTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1))
apLinkStatisticsTableEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:apLinkStatisticsTableEntry.setStatus(_A)
_ApStationAssocSum_Type=Integer32
_ApStationAssocSum_Object=MibTableColumn
apStationAssocSum=_ApStationAssocSum_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,1),_ApStationAssocSum_Type())
apStationAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:apStationAssocSum.setStatus(_A)
_ApStationOnlineSum_Type=Integer32
_ApStationOnlineSum_Object=MibTableColumn
apStationOnlineSum=_ApStationOnlineSum_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,2),_ApStationOnlineSum_Type())
apStationOnlineSum.setMaxAccess(_B)
if mibBuilder.loadTexts:apStationOnlineSum.setStatus(_A)
_ApAssocTimes_Type=Counter32
_ApAssocTimes_Object=MibTableColumn
apAssocTimes=_ApAssocTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,3),_ApAssocTimes_Type())
apAssocTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apAssocTimes.setStatus(_A)
_ApAssocFailTimes_Type=Counter32
_ApAssocFailTimes_Object=MibTableColumn
apAssocFailTimes=_ApAssocFailTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,4),_ApAssocFailTimes_Type())
apAssocFailTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apAssocFailTimes.setStatus(_A)
_ApReassocTimes_Type=Counter32
_ApReassocTimes_Object=MibTableColumn
apReassocTimes=_ApReassocTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,5),_ApReassocTimes_Type())
apReassocTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apReassocTimes.setStatus(_A)
_ApPreAssCannotShiftDeassocFailSum_Type=Counter32
_ApPreAssCannotShiftDeassocFailSum_Object=MibTableColumn
apPreAssCannotShiftDeassocFailSum=_ApPreAssCannotShiftDeassocFailSum_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,6),_ApPreAssCannotShiftDeassocFailSum_Type())
apPreAssCannotShiftDeassocFailSum.setMaxAccess(_B)
if mibBuilder.loadTexts:apPreAssCannotShiftDeassocFailSum.setStatus(_A)
_ApApStatsDisassociated_Type=Counter32
_ApApStatsDisassociated_Object=MibTableColumn
apApStatsDisassociated=_ApApStatsDisassociated_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,7),_ApApStatsDisassociated_Type())
apApStatsDisassociated.setMaxAccess(_B)
if mibBuilder.loadTexts:apApStatsDisassociated.setStatus(_A)
_ApAssocRejectSum_Type=Counter32
_ApAssocRejectSum_Object=MibTableColumn
apAssocRejectSum=_ApAssocRejectSum_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,8),_ApAssocRejectSum_Type())
apAssocRejectSum.setMaxAccess(_B)
if mibBuilder.loadTexts:apAssocRejectSum.setStatus(_A)
_ApBSSNotSupportAssocFailSum_Type=Counter32
_ApBSSNotSupportAssocFailSum_Object=MibTableColumn
apBSSNotSupportAssocFailSum=_ApBSSNotSupportAssocFailSum_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,9),_ApBSSNotSupportAssocFailSum_Type())
apBSSNotSupportAssocFailSum.setMaxAccess(_B)
if mibBuilder.loadTexts:apBSSNotSupportAssocFailSum.setStatus(_A)
_ApApAuthReqTimes_Type=Counter32
_ApApAuthReqTimes_Object=MibTableColumn
apApAuthReqTimes=_ApApAuthReqTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,10),_ApApAuthReqTimes_Type())
apApAuthReqTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apApAuthReqTimes.setStatus(_A)
_ApApAuthSuccessTimes_Type=Counter32
_ApApAuthSuccessTimes_Object=MibTableColumn
apApAuthSuccessTimes=_ApApAuthSuccessTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,11),_ApApAuthSuccessTimes_Type())
apApAuthSuccessTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apApAuthSuccessTimes.setStatus(_A)
_AcApAuthReqFailTimes_Type=Counter32
_AcApAuthReqFailTimes_Object=MibTableColumn
acApAuthReqFailTimes=_AcApAuthReqFailTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,12),_AcApAuthReqFailTimes_Type())
acApAuthReqFailTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:acApAuthReqFailTimes.setStatus(_A)
_ApReassocFailTimes_Type=Counter32
_ApReassocFailTimes_Object=MibTableColumn
apReassocFailTimes=_ApReassocFailTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,13),_ApReassocFailTimes_Type())
apReassocFailTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apReassocFailTimes.setStatus(_A)
_ApRSSILowAssocFailSum_Type=Counter32
_ApRSSILowAssocFailSum_Object=MibTableColumn
apRSSILowAssocFailSum=_ApRSSILowAssocFailSum_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,14),_ApRSSILowAssocFailSum_Type())
apRSSILowAssocFailSum.setMaxAccess(_B)
if mibBuilder.loadTexts:apRSSILowAssocFailSum.setStatus(_A)
_ApUnknowReasonAssoFailSum_Type=Counter32
_ApUnknowReasonAssoFailSum_Object=MibTableColumn
apUnknowReasonAssoFailSum=_ApUnknowReasonAssoFailSum_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,15),_ApUnknowReasonAssoFailSum_Type())
apUnknowReasonAssoFailSum.setMaxAccess(_B)
if mibBuilder.loadTexts:apUnknowReasonAssoFailSum.setStatus(_A)
_ApOut80211StandardAssocFailSum_Type=Counter32
_ApOut80211StandardAssocFailSum_Object=MibTableColumn
apOut80211StandardAssocFailSum=_ApOut80211StandardAssocFailSum_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,16),_ApOut80211StandardAssocFailSum_Type())
apOut80211StandardAssocFailSum.setMaxAccess(_B)
if mibBuilder.loadTexts:apOut80211StandardAssocFailSum.setStatus(_A)
_ApAllStationsTotalUpTime_Type=Integer32
_ApAllStationsTotalUpTime_Object=MibTableColumn
apAllStationsTotalUpTime=_ApAllStationsTotalUpTime_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,17),_ApAllStationsTotalUpTime_Type())
apAllStationsTotalUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:apAllStationsTotalUpTime.setStatus(_A)
_ApAssocRespTimes_Type=Counter32
_ApAssocRespTimes_Object=MibTableColumn
apAssocRespTimes=_ApAssocRespTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,18),_ApAssocRespTimes_Type())
apAssocRespTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apAssocRespTimes.setStatus(_A)
_ApAssocSuccTimes_Type=Counter32
_ApAssocSuccTimes_Object=MibTableColumn
apAssocSuccTimes=_ApAssocSuccTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,19),_ApAssocSuccTimes_Type())
apAssocSuccTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apAssocSuccTimes.setStatus(_A)
_ApUserRadiusOnlineSum_Type=Integer32
_ApUserRadiusOnlineSum_Object=MibTableColumn
apUserRadiusOnlineSum=_ApUserRadiusOnlineSum_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,20),_ApUserRadiusOnlineSum_Type())
apUserRadiusOnlineSum.setMaxAccess(_B)
if mibBuilder.loadTexts:apUserRadiusOnlineSum.setStatus(_A)
_ApAllUserOnlineTime_Type=TimeTicks
_ApAllUserOnlineTime_Object=MibTableColumn
apAllUserOnlineTime=_ApAllUserOnlineTime_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,21),_ApAllUserOnlineTime_Type())
apAllUserOnlineTime.setMaxAccess(_B)
if mibBuilder.loadTexts:apAllUserOnlineTime.setStatus(_A)
_ApRadiusAuthTimes_Type=Counter32
_ApRadiusAuthTimes_Object=MibTableColumn
apRadiusAuthTimes=_ApRadiusAuthTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,22),_ApRadiusAuthTimes_Type())
apRadiusAuthTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apRadiusAuthTimes.setStatus(_A)
_ApRadiusAuthSuccTimes_Type=Counter32
_ApRadiusAuthSuccTimes_Object=MibTableColumn
apRadiusAuthSuccTimes=_ApRadiusAuthSuccTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,23),_ApRadiusAuthSuccTimes_Type())
apRadiusAuthSuccTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apRadiusAuthSuccTimes.setStatus(_A)
_ApRadiusAuthFailTimes_Type=Counter32
_ApRadiusAuthFailTimes_Object=MibTableColumn
apRadiusAuthFailTimes=_ApRadiusAuthFailTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,2,1,1,24),_ApRadiusAuthFailTimes_Type())
apRadiusAuthFailTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apRadiusAuthFailTimes.setStatus(_A)
_ApInterfaceRGMIIStatisticsObjects_ObjectIdentity=ObjectIdentity
apInterfaceRGMIIStatisticsObjects=_ApInterfaceRGMIIStatisticsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,10,3))
_ApInterfaceRGMIIStatisticsTable_Object=MibTable
apInterfaceRGMIIStatisticsTable=_ApInterfaceRGMIIStatisticsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,3,1))
if mibBuilder.loadTexts:apInterfaceRGMIIStatisticsTable.setStatus(_A)
_ApInterfaceRGMIIStatisticsTableEntry_Object=MibTableRow
apInterfaceRGMIIStatisticsTableEntry=_ApInterfaceRGMIIStatisticsTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,3,1,1))
apInterfaceRGMIIStatisticsTableEntry.setIndexNames((0,_E,_F),(0,_D,_AB))
if mibBuilder.loadTexts:apInterfaceRGMIIStatisticsTableEntry.setStatus(_A)
_ApRGMIIIndex_Type=Integer32
_ApRGMIIIndex_Object=MibTableColumn
apRGMIIIndex=_ApRGMIIIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,3,1,1,1),_ApRGMIIIndex_Type())
apRGMIIIndex.setMaxAccess(_w)
if mibBuilder.loadTexts:apRGMIIIndex.setStatus(_A)
_ApifInUcastPkts_Type=Counter32
_ApifInUcastPkts_Object=MibTableColumn
apifInUcastPkts=_ApifInUcastPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,3,1,1,2),_ApifInUcastPkts_Type())
apifInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apifInUcastPkts.setStatus(_A)
_ApifInNUcastPkts_Type=Counter32
_ApifInNUcastPkts_Object=MibTableColumn
apifInNUcastPkts=_ApifInNUcastPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,3,1,1,3),_ApifInNUcastPkts_Type())
apifInNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apifInNUcastPkts.setStatus(_A)
_ApifInOctets_Type=Counter32
_ApifInOctets_Object=MibTableColumn
apifInOctets=_ApifInOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,3,1,1,4),_ApifInOctets_Type())
apifInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:apifInOctets.setStatus(_A)
_ApifInDiscardPkts_Type=Counter32
_ApifInDiscardPkts_Object=MibTableColumn
apifInDiscardPkts=_ApifInDiscardPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,3,1,1,5),_ApifInDiscardPkts_Type())
apifInDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apifInDiscardPkts.setStatus(_A)
_ApifInErrors_Type=Counter32
_ApifInErrors_Object=MibTableColumn
apifInErrors=_ApifInErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,3,1,1,6),_ApifInErrors_Type())
apifInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:apifInErrors.setStatus(_A)
_ApifOutUcastPkts_Type=Counter32
_ApifOutUcastPkts_Object=MibTableColumn
apifOutUcastPkts=_ApifOutUcastPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,3,1,1,7),_ApifOutUcastPkts_Type())
apifOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apifOutUcastPkts.setStatus(_A)
_ApifOutNUcastPkts_Type=Counter32
_ApifOutNUcastPkts_Object=MibTableColumn
apifOutNUcastPkts=_ApifOutNUcastPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,3,1,1,8),_ApifOutNUcastPkts_Type())
apifOutNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apifOutNUcastPkts.setStatus(_A)
_ApifOutOctets_Type=Counter32
_ApifOutOctets_Object=MibTableColumn
apifOutOctets=_ApifOutOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,3,1,1,9),_ApifOutOctets_Type())
apifOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:apifOutOctets.setStatus(_A)
_ApifOutDiscardPkts_Type=Counter32
_ApifOutDiscardPkts_Object=MibTableColumn
apifOutDiscardPkts=_ApifOutDiscardPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,3,1,1,10),_ApifOutDiscardPkts_Type())
apifOutDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apifOutDiscardPkts.setStatus(_A)
_ApifOutErrors_Type=Counter32
_ApifOutErrors_Object=MibTableColumn
apifOutErrors=_ApifOutErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,3,1,1,11),_ApifOutErrors_Type())
apifOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:apifOutErrors.setStatus(_A)
_ApifUpDwnTimes_Type=Counter32
_ApifUpDwnTimes_Object=MibTableColumn
apifUpDwnTimes=_ApifUpDwnTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,3,1,1,12),_ApifUpDwnTimes_Type())
apifUpDwnTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apifUpDwnTimes.setStatus(_A)
_ApInterfaceWireStatisticsObjects_ObjectIdentity=ObjectIdentity
apInterfaceWireStatisticsObjects=_ApInterfaceWireStatisticsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,10,4))
_ApInterfaceWireStatisticsTable_Object=MibTable
apInterfaceWireStatisticsTable=_ApInterfaceWireStatisticsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1))
if mibBuilder.loadTexts:apInterfaceWireStatisticsTable.setStatus(_A)
_ApInterfaceWireStatisticsTableEntry_Object=MibTableRow
apInterfaceWireStatisticsTableEntry=_ApInterfaceWireStatisticsTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1))
apInterfaceWireStatisticsTableEntry.setIndexNames((0,_E,_F),(0,_E,_J))
if mibBuilder.loadTexts:apInterfaceWireStatisticsTableEntry.setStatus(_A)
_ApAvgRxSignalStrength_Type=DisplayString
_ApAvgRxSignalStrength_Object=MibTableColumn
apAvgRxSignalStrength=_ApAvgRxSignalStrength_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,1),_ApAvgRxSignalStrength_Type())
apAvgRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:apAvgRxSignalStrength.setStatus(_A)
_ApHighestRxSignalStrength_Type=DisplayString
_ApHighestRxSignalStrength_Object=MibTableColumn
apHighestRxSignalStrength=_ApHighestRxSignalStrength_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,2),_ApHighestRxSignalStrength_Type())
apHighestRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:apHighestRxSignalStrength.setStatus(_A)
_ApLowestRxSignalStrength_Type=DisplayString
_ApLowestRxSignalStrength_Object=MibTableColumn
apLowestRxSignalStrength=_ApLowestRxSignalStrength_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,3),_ApLowestRxSignalStrength_Type())
apLowestRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:apLowestRxSignalStrength.setStatus(_A)
_ApWirelessUpdownTimes_Type=Counter32
_ApWirelessUpdownTimes_Object=MibTableColumn
apWirelessUpdownTimes=_ApWirelessUpdownTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,4),_ApWirelessUpdownTimes_Type())
apWirelessUpdownTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apWirelessUpdownTimes.setStatus(_A)
_ApChStatsNumStations_Type=Counter32
_ApChStatsNumStations_Object=MibTableColumn
apChStatsNumStations=_ApChStatsNumStations_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,5),_ApChStatsNumStations_Type())
apChStatsNumStations.setMaxAccess(_B)
if mibBuilder.loadTexts:apChStatsNumStations.setStatus(_A)
_ApTxDataPkts_Type=Counter32
_ApTxDataPkts_Object=MibTableColumn
apTxDataPkts=_ApTxDataPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,6),_ApTxDataPkts_Type())
apTxDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apTxDataPkts.setStatus(_A)
_ApRxDataPkts_Type=Counter32
_ApRxDataPkts_Object=MibTableColumn
apRxDataPkts=_ApRxDataPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,7),_ApRxDataPkts_Type())
apRxDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apRxDataPkts.setStatus(_A)
_ApUplinkDataOctets_Type=Counter64
_ApUplinkDataOctets_Object=MibTableColumn
apUplinkDataOctets=_ApUplinkDataOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,8),_ApUplinkDataOctets_Type())
apUplinkDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:apUplinkDataOctets.setStatus(_A)
_ApDwlinkDataOctets_Type=Counter64
_ApDwlinkDataOctets_Object=MibTableColumn
apDwlinkDataOctets=_ApDwlinkDataOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,9),_ApDwlinkDataOctets_Type())
apDwlinkDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:apDwlinkDataOctets.setStatus(_A)
_ApChStatsDwlinkTotRetryPkts_Type=Counter32
_ApChStatsDwlinkTotRetryPkts_Object=MibTableColumn
apChStatsDwlinkTotRetryPkts=_ApChStatsDwlinkTotRetryPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,10),_ApChStatsDwlinkTotRetryPkts_Type())
apChStatsDwlinkTotRetryPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apChStatsDwlinkTotRetryPkts.setStatus(_A)
_ApChStatsPhyErrPkts_Type=Counter32
_ApChStatsPhyErrPkts_Object=MibTableColumn
apChStatsPhyErrPkts=_ApChStatsPhyErrPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,11),_ApChStatsPhyErrPkts_Type())
apChStatsPhyErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apChStatsPhyErrPkts.setStatus(_A)
_ApChStatsMacFcsErrPkts_Type=Counter32
_ApChStatsMacFcsErrPkts_Object=MibTableColumn
apChStatsMacFcsErrPkts=_ApChStatsMacFcsErrPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,12),_ApChStatsMacFcsErrPkts_Type())
apChStatsMacFcsErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apChStatsMacFcsErrPkts.setStatus(_A)
_ApChStatsMacMicErrPkts_Type=Counter32
_ApChStatsMacMicErrPkts_Object=MibTableColumn
apChStatsMacMicErrPkts=_ApChStatsMacMicErrPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,13),_ApChStatsMacMicErrPkts_Type())
apChStatsMacMicErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apChStatsMacMicErrPkts.setStatus(_A)
_ApChStatsMacDecryptErrPkts_Type=Counter32
_ApChStatsMacDecryptErrPkts_Object=MibTableColumn
apChStatsMacDecryptErrPkts=_ApChStatsMacDecryptErrPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,14),_ApChStatsMacDecryptErrPkts_Type())
apChStatsMacDecryptErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apChStatsMacDecryptErrPkts.setStatus(_A)
_ApChStatsTotalErrPkts_Type=Counter32
_ApChStatsTotalErrPkts_Object=MibTableColumn
apChStatsTotalErrPkts=_ApChStatsTotalErrPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,15),_ApChStatsTotalErrPkts_Type())
apChStatsTotalErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apChStatsTotalErrPkts.setStatus(_A)
_ApRxMgmtFrameCnt_Type=Counter32
_ApRxMgmtFrameCnt_Object=MibTableColumn
apRxMgmtFrameCnt=_ApRxMgmtFrameCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,16),_ApRxMgmtFrameCnt_Type())
apRxMgmtFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:apRxMgmtFrameCnt.setStatus(_A)
_ApRxCtrlFrameCnt_Type=Counter32
_ApRxCtrlFrameCnt_Object=MibTableColumn
apRxCtrlFrameCnt=_ApRxCtrlFrameCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,17),_ApRxCtrlFrameCnt_Type())
apRxCtrlFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:apRxCtrlFrameCnt.setStatus(_A)
_ApRxDataFrameCnt_Type=Counter32
_ApRxDataFrameCnt_Object=MibTableColumn
apRxDataFrameCnt=_ApRxDataFrameCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,18),_ApRxDataFrameCnt_Type())
apRxDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:apRxDataFrameCnt.setStatus(_A)
_ApTxMgmtFrameCnt_Type=Counter32
_ApTxMgmtFrameCnt_Object=MibTableColumn
apTxMgmtFrameCnt=_ApTxMgmtFrameCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,19),_ApTxMgmtFrameCnt_Type())
apTxMgmtFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:apTxMgmtFrameCnt.setStatus(_A)
_ApTxCtrlFrameCnt_Type=Counter32
_ApTxCtrlFrameCnt_Object=MibTableColumn
apTxCtrlFrameCnt=_ApTxCtrlFrameCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,20),_ApTxCtrlFrameCnt_Type())
apTxCtrlFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:apTxCtrlFrameCnt.setStatus(_A)
_ApTxDataFrameCnt_Type=Counter32
_ApTxDataFrameCnt_Object=MibTableColumn
apTxDataFrameCnt=_ApTxDataFrameCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,21),_ApTxDataFrameCnt_Type())
apTxDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:apTxDataFrameCnt.setStatus(_A)
_ApChStatsFrameErrorCnt_Type=Counter32
_ApChStatsFrameErrorCnt_Object=MibTableColumn
apChStatsFrameErrorCnt=_ApChStatsFrameErrorCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,22),_ApChStatsFrameErrorCnt_Type())
apChStatsFrameErrorCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:apChStatsFrameErrorCnt.setStatus(_A)
_ApRetryCnt_Type=Counter32
_ApRetryCnt_Object=MibTableColumn
apRetryCnt=_ApRetryCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,23),_ApRetryCnt_Type())
apRetryCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:apRetryCnt.setStatus(_A)
_ApCurTxPwr_Type=Integer32
_ApCurTxPwr_Object=MibTableColumn
apCurTxPwr=_ApCurTxPwr_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,24),_ApCurTxPwr_Type())
apCurTxPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:apCurTxPwr.setStatus(_A)
_ApAPNeighborSSIDList_Type=DisplayString
_ApAPNeighborSSIDList_Object=MibTableColumn
apAPNeighborSSIDList=_ApAPNeighborSSIDList_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,25),_ApAPNeighborSSIDList_Type())
apAPNeighborSSIDList.setMaxAccess(_B)
if mibBuilder.loadTexts:apAPNeighborSSIDList.setStatus(_A)
_ApChDownUnicastFrame_Type=Counter32
_ApChDownUnicastFrame_Object=MibTableColumn
apChDownUnicastFrame=_ApChDownUnicastFrame_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,26),_ApChDownUnicastFrame_Type())
apChDownUnicastFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:apChDownUnicastFrame.setStatus(_A)
_ApChDownNonUnicastFrame_Type=Counter32
_ApChDownNonUnicastFrame_Object=MibTableColumn
apChDownNonUnicastFrame=_ApChDownNonUnicastFrame_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,27),_ApChDownNonUnicastFrame_Type())
apChDownNonUnicastFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:apChDownNonUnicastFrame.setStatus(_A)
_ApChTxThroughput_Type=Counter32
_ApChTxThroughput_Object=MibTableColumn
apChTxThroughput=_ApChTxThroughput_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,28),_ApChTxThroughput_Type())
apChTxThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:apChTxThroughput.setStatus(_A)
_ApChRxThroughput_Type=Counter32
_ApChRxThroughput_Object=MibTableColumn
apChRxThroughput=_ApChRxThroughput_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,29),_ApChRxThroughput_Type())
apChRxThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:apChRxThroughput.setStatus(_A)
_ApChTxDropPkts_Type=Counter32
_ApChTxDropPkts_Object=MibTableColumn
apChTxDropPkts=_ApChTxDropPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,30),_ApChTxDropPkts_Type())
apChTxDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apChTxDropPkts.setStatus(_A)
_ApChRxDropPkts_Type=Counter32
_ApChRxDropPkts_Object=MibTableColumn
apChRxDropPkts=_ApChRxDropPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,31),_ApChRxDropPkts_Type())
apChRxDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apChRxDropPkts.setStatus(_A)
_ApChTxErrorPkts_Type=Counter32
_ApChTxErrorPkts_Object=MibTableColumn
apChTxErrorPkts=_ApChTxErrorPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,32),_ApChTxErrorPkts_Type())
apChTxErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apChTxErrorPkts.setStatus(_A)
_ApChRxErrorPkts_Type=Counter32
_ApChRxErrorPkts_Object=MibTableColumn
apChRxErrorPkts=_ApChRxErrorPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,33),_ApChRxErrorPkts_Type())
apChRxErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apChRxErrorPkts.setStatus(_A)
_ApRxBytes_Type=Counter32
_ApRxBytes_Object=MibTableColumn
apRxBytes=_ApRxBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,34),_ApRxBytes_Type())
apRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:apRxBytes.setStatus(_A)
_ApRxPkts_Type=Counter32
_ApRxPkts_Object=MibTableColumn
apRxPkts=_ApRxPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,35),_ApRxPkts_Type())
apRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apRxPkts.setStatus(_A)
_ApTxBytes_Type=Counter32
_ApTxBytes_Object=MibTableColumn
apTxBytes=_ApTxBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,36),_ApTxBytes_Type())
apTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:apTxBytes.setStatus(_A)
_ApTxPkts_Type=Counter32
_ApTxPkts_Object=MibTableColumn
apTxPkts=_ApTxPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,37),_ApTxPkts_Type())
apTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apTxPkts.setStatus(_A)
_ApDownNonUnicastPkts_Type=Counter32
_ApDownNonUnicastPkts_Object=MibTableColumn
apDownNonUnicastPkts=_ApDownNonUnicastPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,38),_ApDownNonUnicastPkts_Type())
apDownNonUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apDownNonUnicastPkts.setStatus(_A)
_ApDownUnicastPkts_Type=Counter32
_ApDownUnicastPkts_Object=MibTableColumn
apDownUnicastPkts=_ApDownUnicastPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,39),_ApDownUnicastPkts_Type())
apDownUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apDownUnicastPkts.setStatus(_A)
_ApUpNonUnicastPkts_Type=Counter32
_ApUpNonUnicastPkts_Object=MibTableColumn
apUpNonUnicastPkts=_ApUpNonUnicastPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,40),_ApUpNonUnicastPkts_Type())
apUpNonUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apUpNonUnicastPkts.setStatus(_A)
_ApUpUnicastPkts_Type=Counter32
_ApUpUnicastPkts_Object=MibTableColumn
apUpUnicastPkts=_ApUpUnicastPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,41),_ApUpUnicastPkts_Type())
apUpUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apUpUnicastPkts.setStatus(_A)
_ApAssoFailUnknowReason_Type=Counter32
_ApAssoFailUnknowReason_Object=MibTableColumn
apAssoFailUnknowReason=_ApAssoFailUnknowReason_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,42),_ApAssoFailUnknowReason_Type())
apAssoFailUnknowReason.setMaxAccess(_B)
if mibBuilder.loadTexts:apAssoFailUnknowReason.setStatus(_A)
_ApAssoFailOutofDot11_Type=Counter32
_ApAssoFailOutofDot11_Object=MibTableColumn
apAssoFailOutofDot11=_ApAssoFailOutofDot11_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,43),_ApAssoFailOutofDot11_Type())
apAssoFailOutofDot11.setMaxAccess(_B)
if mibBuilder.loadTexts:apAssoFailOutofDot11.setStatus(_A)
_ApAssoTotalTime_Type=Counter32
_ApAssoTotalTime_Object=MibTableColumn
apAssoTotalTime=_ApAssoTotalTime_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,44),_ApAssoTotalTime_Type())
apAssoTotalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:apAssoTotalTime.setStatus(_A)
_ApAuthReqFailTimes_Type=Counter32
_ApAuthReqFailTimes_Object=MibTableColumn
apAuthReqFailTimes=_ApAuthReqFailTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,45),_ApAuthReqFailTimes_Type())
apAuthReqFailTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apAuthReqFailTimes.setStatus(_A)
_ApAuthReqTimes_Type=Counter32
_ApAuthReqTimes_Object=MibTableColumn
apAuthReqTimes=_ApAuthReqTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,46),_ApAuthReqTimes_Type())
apAuthReqTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apAuthReqTimes.setStatus(_A)
_ApAuthSuccessTimes_Type=Counter32
_ApAuthSuccessTimes_Object=MibTableColumn
apAuthSuccessTimes=_ApAuthSuccessTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,47),_ApAuthSuccessTimes_Type())
apAuthSuccessTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apAuthSuccessTimes.setStatus(_A)
_ApReAssoFailTimes_Type=Counter32
_ApReAssoFailTimes_Object=MibTableColumn
apReAssoFailTimes=_ApReAssoFailTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,48),_ApReAssoFailTimes_Type())
apReAssoFailTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apReAssoFailTimes.setStatus(_A)
_ApMacTxCorrectFrameCnt_Type=Counter32
_ApMacTxCorrectFrameCnt_Object=MibTableColumn
apMacTxCorrectFrameCnt=_ApMacTxCorrectFrameCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,49),_ApMacTxCorrectFrameCnt_Type())
apMacTxCorrectFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:apMacTxCorrectFrameCnt.setStatus(_A)
_ApMacRxCorrectFrameCnt_Type=Counter32
_ApMacRxCorrectFrameCnt_Object=MibTableColumn
apMacRxCorrectFrameCnt=_ApMacRxCorrectFrameCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,50),_ApMacRxCorrectFrameCnt_Type())
apMacRxCorrectFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:apMacRxCorrectFrameCnt.setStatus(_A)
_ApPktErrRate_Type=Integer32
_ApPktErrRate_Object=MibTableColumn
apPktErrRate=_ApPktErrRate_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,51),_ApPktErrRate_Type())
apPktErrRate.setMaxAccess(_B)
if mibBuilder.loadTexts:apPktErrRate.setStatus(_A)
_ApTotalRxBytes_Type=Counter64
_ApTotalRxBytes_Object=MibTableColumn
apTotalRxBytes=_ApTotalRxBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,52),_ApTotalRxBytes_Type())
apTotalRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:apTotalRxBytes.setStatus(_A)
_ApTotalTxBytes_Type=Counter64
_ApTotalTxBytes_Object=MibTableColumn
apTotalTxBytes=_ApTotalTxBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,53),_ApTotalTxBytes_Type())
apTotalTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:apTotalTxBytes.setStatus(_A)
_ApTxErrorPkts_Type=Counter32
_ApTxErrorPkts_Object=MibTableColumn
apTxErrorPkts=_ApTxErrorPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,54),_ApTxErrorPkts_Type())
apTxErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apTxErrorPkts.setStatus(_A)
_ApTxDropPkts_Type=Counter32
_ApTxDropPkts_Object=MibTableColumn
apTxDropPkts=_ApTxDropPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,55),_ApTxDropPkts_Type())
apTxDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apTxDropPkts.setStatus(_A)
_ApIfRadiusOnlineUserNum_Type=Counter32
_ApIfRadiusOnlineUserNum_Object=MibTableColumn
apIfRadiusOnlineUserNum=_ApIfRadiusOnlineUserNum_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,4,1,1,56),_ApIfRadiusOnlineUserNum_Type())
apIfRadiusOnlineUserNum.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfRadiusOnlineUserNum.setStatus(_A)
_ApSSIDStatisticsObjects_ObjectIdentity=ObjectIdentity
apSSIDStatisticsObjects=_ApSSIDStatisticsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,10,5))
_ApSSIDStatisticsTable_Object=MibTable
apSSIDStatisticsTable=_ApSSIDStatisticsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,1))
if mibBuilder.loadTexts:apSSIDStatisticsTable.setStatus(_A)
_ApSSIDStatisticsTableEntry_Object=MibTableRow
apSSIDStatisticsTableEntry=_ApSSIDStatisticsTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,1,1))
apSSIDStatisticsTableEntry.setIndexNames((0,_D,_AC),(0,_D,_AD),(0,_D,_AE))
if mibBuilder.loadTexts:apSSIDStatisticsTableEntry.setStatus(_A)
_ApSSIDStatisticsAPMac_Type=MacAddress
_ApSSIDStatisticsAPMac_Object=MibTableColumn
apSSIDStatisticsAPMac=_ApSSIDStatisticsAPMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,1,1,1),_ApSSIDStatisticsAPMac_Type())
apSSIDStatisticsAPMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDStatisticsAPMac.setStatus(_A)
_ApSSIDStatisticsRadioId_Type=Integer32
_ApSSIDStatisticsRadioId_Object=MibTableColumn
apSSIDStatisticsRadioId=_ApSSIDStatisticsRadioId_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,1,1,2),_ApSSIDStatisticsRadioId_Type())
apSSIDStatisticsRadioId.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDStatisticsRadioId.setStatus(_A)
_ApSSIDStatisticsWlanId_Type=Integer32
_ApSSIDStatisticsWlanId_Object=MibTableColumn
apSSIDStatisticsWlanId=_ApSSIDStatisticsWlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,1,1,3),_ApSSIDStatisticsWlanId_Type())
apSSIDStatisticsWlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDStatisticsWlanId.setStatus(_A)
_ApSSIDTxDataPkts_Type=Counter32
_ApSSIDTxDataPkts_Object=MibTableColumn
apSSIDTxDataPkts=_ApSSIDTxDataPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,1,1,4),_ApSSIDTxDataPkts_Type())
apSSIDTxDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDTxDataPkts.setStatus(_A)
_ApSSIDRxDataPkts_Type=Counter32
_ApSSIDRxDataPkts_Object=MibTableColumn
apSSIDRxDataPkts=_ApSSIDRxDataPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,1,1,5),_ApSSIDRxDataPkts_Type())
apSSIDRxDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDRxDataPkts.setStatus(_A)
_ApSSIDUplinkDataOctets_Type=Counter64
_ApSSIDUplinkDataOctets_Object=MibTableColumn
apSSIDUplinkDataOctets=_ApSSIDUplinkDataOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,1,1,6),_ApSSIDUplinkDataOctets_Type())
apSSIDUplinkDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDUplinkDataOctets.setStatus(_A)
_ApSSIDDwlinkDataOctets_Type=Counter64
_ApSSIDDwlinkDataOctets_Object=MibTableColumn
apSSIDDwlinkDataOctets=_ApSSIDDwlinkDataOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,1,1,7),_ApSSIDDwlinkDataOctets_Type())
apSSIDDwlinkDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDDwlinkDataOctets.setStatus(_A)
_ApSSIDChStatsDwlinkTotRetryPkts_Type=Counter32
_ApSSIDChStatsDwlinkTotRetryPkts_Object=MibTableColumn
apSSIDChStatsDwlinkTotRetryPkts=_ApSSIDChStatsDwlinkTotRetryPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,1,1,8),_ApSSIDChStatsDwlinkTotRetryPkts_Type())
apSSIDChStatsDwlinkTotRetryPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDChStatsDwlinkTotRetryPkts.setStatus(_A)
_ApSSIDApChStatsNumStations_Type=Integer32
_ApSSIDApChStatsNumStations_Object=MibTableColumn
apSSIDApChStatsNumStations=_ApSSIDApChStatsNumStations_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,1,1,9),_ApSSIDApChStatsNumStations_Type())
apSSIDApChStatsNumStations.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDApChStatsNumStations.setStatus(_A)
_ApApChStatsOnlineSum_Type=Integer32
_ApApChStatsOnlineSum_Object=MibTableColumn
apApChStatsOnlineSum=_ApApChStatsOnlineSum_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,1,1,10),_ApApChStatsOnlineSum_Type())
apApChStatsOnlineSum.setMaxAccess(_B)
if mibBuilder.loadTexts:apApChStatsOnlineSum.setStatus(_A)
_ApSSIDStatisticsName_Type=DisplayString
_ApSSIDStatisticsName_Object=MibTableColumn
apSSIDStatisticsName=_ApSSIDStatisticsName_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,1,1,11),_ApSSIDStatisticsName_Type())
apSSIDStatisticsName.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDStatisticsName.setStatus(_A)
_ApSSIDMacTxPkts_Type=Counter32
_ApSSIDMacTxPkts_Object=MibTableColumn
apSSIDMacTxPkts=_ApSSIDMacTxPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,1,1,12),_ApSSIDMacTxPkts_Type())
apSSIDMacTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDMacTxPkts.setStatus(_A)
_ApSSIDMacRxPkts_Type=Counter32
_ApSSIDMacRxPkts_Object=MibTableColumn
apSSIDMacRxPkts=_ApSSIDMacRxPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,1,1,13),_ApSSIDMacRxPkts_Type())
apSSIDMacRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDMacRxPkts.setStatus(_A)
_ApSSIDStatisticsNewTable_Object=MibTable
apSSIDStatisticsNewTable=_ApSSIDStatisticsNewTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,2))
if mibBuilder.loadTexts:apSSIDStatisticsNewTable.setStatus(_A)
_ApSSIDStatisticsNewTableEntry_Object=MibTableRow
apSSIDStatisticsNewTableEntry=_ApSSIDStatisticsNewTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,2,1))
apSSIDStatisticsNewTableEntry.setIndexNames((0,_D,_AF),(0,_D,_AG),(0,_D,_AH))
if mibBuilder.loadTexts:apSSIDStatisticsNewTableEntry.setStatus(_A)
_ApSSIDStatisticsNewAPMac_Type=MacAddress
_ApSSIDStatisticsNewAPMac_Object=MibTableColumn
apSSIDStatisticsNewAPMac=_ApSSIDStatisticsNewAPMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,2,1,1),_ApSSIDStatisticsNewAPMac_Type())
apSSIDStatisticsNewAPMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDStatisticsNewAPMac.setStatus(_A)
_ApSSIDStatisticsNewRadioId_Type=Integer32
_ApSSIDStatisticsNewRadioId_Object=MibTableColumn
apSSIDStatisticsNewRadioId=_ApSSIDStatisticsNewRadioId_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,2,1,2),_ApSSIDStatisticsNewRadioId_Type())
apSSIDStatisticsNewRadioId.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDStatisticsNewRadioId.setStatus(_A)
_ApSSIDStatisticsNewSSID_Type=DisplayString
_ApSSIDStatisticsNewSSID_Object=MibTableColumn
apSSIDStatisticsNewSSID=_ApSSIDStatisticsNewSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,2,1,3),_ApSSIDStatisticsNewSSID_Type())
apSSIDStatisticsNewSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDStatisticsNewSSID.setStatus(_A)
_ApSSIDNewTxDataPkts_Type=Counter32
_ApSSIDNewTxDataPkts_Object=MibTableColumn
apSSIDNewTxDataPkts=_ApSSIDNewTxDataPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,2,1,4),_ApSSIDNewTxDataPkts_Type())
apSSIDNewTxDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDNewTxDataPkts.setStatus(_A)
_ApSSIDNewRxDataPkts_Type=Counter32
_ApSSIDNewRxDataPkts_Object=MibTableColumn
apSSIDNewRxDataPkts=_ApSSIDNewRxDataPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,2,1,5),_ApSSIDNewRxDataPkts_Type())
apSSIDNewRxDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDNewRxDataPkts.setStatus(_A)
_ApSSIDNewUplinkDataOctets_Type=Counter64
_ApSSIDNewUplinkDataOctets_Object=MibTableColumn
apSSIDNewUplinkDataOctets=_ApSSIDNewUplinkDataOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,2,1,6),_ApSSIDNewUplinkDataOctets_Type())
apSSIDNewUplinkDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDNewUplinkDataOctets.setStatus(_A)
_ApSSIDNewDwlinkDataOctets_Type=Counter64
_ApSSIDNewDwlinkDataOctets_Object=MibTableColumn
apSSIDNewDwlinkDataOctets=_ApSSIDNewDwlinkDataOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,2,1,7),_ApSSIDNewDwlinkDataOctets_Type())
apSSIDNewDwlinkDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDNewDwlinkDataOctets.setStatus(_A)
_ApSSIDNewChStatsDwlinkTotRetryPkts_Type=Counter32
_ApSSIDNewChStatsDwlinkTotRetryPkts_Object=MibTableColumn
apSSIDNewChStatsDwlinkTotRetryPkts=_ApSSIDNewChStatsDwlinkTotRetryPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,2,1,8),_ApSSIDNewChStatsDwlinkTotRetryPkts_Type())
apSSIDNewChStatsDwlinkTotRetryPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDNewChStatsDwlinkTotRetryPkts.setStatus(_A)
_ApSSIDNewApChStatsNumStations_Type=Integer32
_ApSSIDNewApChStatsNumStations_Object=MibTableColumn
apSSIDNewApChStatsNumStations=_ApSSIDNewApChStatsNumStations_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,2,1,9),_ApSSIDNewApChStatsNumStations_Type())
apSSIDNewApChStatsNumStations.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDNewApChStatsNumStations.setStatus(_A)
_ApApNewChStatsOnlineSum_Type=Integer32
_ApApNewChStatsOnlineSum_Object=MibTableColumn
apApNewChStatsOnlineSum=_ApApNewChStatsOnlineSum_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,2,1,10),_ApApNewChStatsOnlineSum_Type())
apApNewChStatsOnlineSum.setMaxAccess(_B)
if mibBuilder.loadTexts:apApNewChStatsOnlineSum.setStatus(_A)
_ApSSIDNewMacTxPkts_Type=Counter32
_ApSSIDNewMacTxPkts_Object=MibTableColumn
apSSIDNewMacTxPkts=_ApSSIDNewMacTxPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,2,1,11),_ApSSIDNewMacTxPkts_Type())
apSSIDNewMacTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDNewMacTxPkts.setStatus(_A)
_ApSSIDNewMacRxPkts_Type=Counter32
_ApSSIDNewMacRxPkts_Object=MibTableColumn
apSSIDNewMacRxPkts=_ApSSIDNewMacRxPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,5,2,1,12),_ApSSIDNewMacRxPkts_Type())
apSSIDNewMacRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDNewMacRxPkts.setStatus(_A)
_ApWAPIStatisticsObjects_ObjectIdentity=ObjectIdentity
apWAPIStatisticsObjects=_ApWAPIStatisticsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,10,6))
_ApWAPIStatisticsTable_Object=MibTable
apWAPIStatisticsTable=_ApWAPIStatisticsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,6,1))
if mibBuilder.loadTexts:apWAPIStatisticsTable.setStatus(_A)
_ApWAPIStatisticsTableEntry_Object=MibTableRow
apWAPIStatisticsTableEntry=_ApWAPIStatisticsTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,6,1,1))
apWAPIStatisticsTableEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:apWAPIStatisticsTableEntry.setStatus(_A)
_ApWAPIControlledPortStatus_Type=TruthValue
_ApWAPIControlledPortStatus_Object=MibTableColumn
apWAPIControlledPortStatus=_ApWAPIControlledPortStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,6,1,1,1),_ApWAPIControlledPortStatus_Type())
apWAPIControlledPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIControlledPortStatus.setStatus(_A)
_ApWAPISelectedUnicastCipher_Type=OctetString
_ApWAPISelectedUnicastCipher_Object=MibTableColumn
apWAPISelectedUnicastCipher=_ApWAPISelectedUnicastCipher_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,6,1,1,2),_ApWAPISelectedUnicastCipher_Type())
apWAPISelectedUnicastCipher.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPISelectedUnicastCipher.setStatus(_A)
_ApWPIReplayCounters_Type=Counter32
_ApWPIReplayCounters_Object=MibTableColumn
apWPIReplayCounters=_ApWPIReplayCounters_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,6,1,1,3),_ApWPIReplayCounters_Type())
apWPIReplayCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:apWPIReplayCounters.setStatus(_A)
_ApWPIDecryptableErrors_Type=Counter32
_ApWPIDecryptableErrors_Object=MibTableColumn
apWPIDecryptableErrors=_ApWPIDecryptableErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,6,1,1,4),_ApWPIDecryptableErrors_Type())
apWPIDecryptableErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:apWPIDecryptableErrors.setStatus(_A)
_ApWPIMICErrors_Type=Counter32
_ApWPIMICErrors_Object=MibTableColumn
apWPIMICErrors=_ApWPIMICErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,6,1,1,5),_ApWPIMICErrors_Type())
apWPIMICErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:apWPIMICErrors.setStatus(_A)
_ApWAISignatureErrors_Type=Counter32
_ApWAISignatureErrors_Object=MibTableColumn
apWAISignatureErrors=_ApWAISignatureErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,6,1,1,6),_ApWAISignatureErrors_Type())
apWAISignatureErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAISignatureErrors.setStatus(_A)
_ApWAIHMACErrors_Type=Counter32
_ApWAIHMACErrors_Object=MibTableColumn
apWAIHMACErrors=_ApWAIHMACErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,6,1,1,7),_ApWAIHMACErrors_Type())
apWAIHMACErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAIHMACErrors.setStatus(_A)
_ApWAIAuthResultFailures_Type=Counter32
_ApWAIAuthResultFailures_Object=MibTableColumn
apWAIAuthResultFailures=_ApWAIAuthResultFailures_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,6,1,1,8),_ApWAIAuthResultFailures_Type())
apWAIAuthResultFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAIAuthResultFailures.setStatus(_A)
_ApWAIDiscardCounters_Type=Counter32
_ApWAIDiscardCounters_Object=MibTableColumn
apWAIDiscardCounters=_ApWAIDiscardCounters_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,6,1,1,9),_ApWAIDiscardCounters_Type())
apWAIDiscardCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAIDiscardCounters.setStatus(_A)
_ApWAITimeoutCounters_Type=Counter32
_ApWAITimeoutCounters_Object=MibTableColumn
apWAITimeoutCounters=_ApWAITimeoutCounters_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,6,1,1,10),_ApWAITimeoutCounters_Type())
apWAITimeoutCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAITimeoutCounters.setStatus(_A)
_ApWAIFormatErrors_Type=Counter32
_ApWAIFormatErrors_Object=MibTableColumn
apWAIFormatErrors=_ApWAIFormatErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,6,1,1,11),_ApWAIFormatErrors_Type())
apWAIFormatErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAIFormatErrors.setStatus(_A)
_ApWAICertificateHandshakeFailures_Type=Counter32
_ApWAICertificateHandshakeFailures_Object=MibTableColumn
apWAICertificateHandshakeFailures=_ApWAICertificateHandshakeFailures_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,6,1,1,12),_ApWAICertificateHandshakeFailures_Type())
apWAICertificateHandshakeFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAICertificateHandshakeFailures.setStatus(_A)
_ApWAIUnicastHandshakeFailures_Type=Counter32
_ApWAIUnicastHandshakeFailures_Object=MibTableColumn
apWAIUnicastHandshakeFailures=_ApWAIUnicastHandshakeFailures_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,6,1,1,13),_ApWAIUnicastHandshakeFailures_Type())
apWAIUnicastHandshakeFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAIUnicastHandshakeFailures.setStatus(_A)
_ApWAIMulticastHandshakeFailures_Type=Counter32
_ApWAIMulticastHandshakeFailures_Object=MibTableColumn
apWAIMulticastHandshakeFailures=_ApWAIMulticastHandshakeFailures_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,6,1,1,14),_ApWAIMulticastHandshakeFailures_Type())
apWAIMulticastHandshakeFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAIMulticastHandshakeFailures.setStatus(_A)
_ApStationStatisticsObjects_ObjectIdentity=ObjectIdentity
apStationStatisticsObjects=_ApStationStatisticsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,10,7))
_ApStationStatisticsTable_Object=MibTable
apStationStatisticsTable=_ApStationStatisticsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,7,1))
if mibBuilder.loadTexts:apStationStatisticsTable.setStatus(_A)
_ApStationStatisticsTableEntry_Object=MibTableRow
apStationStatisticsTableEntry=_ApStationStatisticsTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,7,1,1))
apStationStatisticsTableEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:apStationStatisticsTableEntry.setStatus(_A)
_ApStaAddress_Type=MacAddress
_ApStaAddress_Object=MibTableColumn
apStaAddress=_ApStaAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,7,1,1,1),_ApStaAddress_Type())
apStaAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaAddress.setStatus(_A)
_ApStaUpTime_Type=TimeTicks
_ApStaUpTime_Object=MibTableColumn
apStaUpTime=_ApStaUpTime_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,7,1,1,2),_ApStaUpTime_Type())
apStaUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaUpTime.setStatus(_A)
_ApReceivedStaSignalStrength_Type=DisplayString
_ApReceivedStaSignalStrength_Object=MibTableColumn
apReceivedStaSignalStrength=_ApReceivedStaSignalStrength_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,7,1,1,3),_ApReceivedStaSignalStrength_Type())
apReceivedStaSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:apReceivedStaSignalStrength.setStatus(_A)
_ApAPReceiveStaSNR_Type=DisplayString
_ApAPReceiveStaSNR_Object=MibTableColumn
apAPReceiveStaSNR=_ApAPReceiveStaSNR_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,7,1,1,4),_ApAPReceiveStaSNR_Type())
apAPReceiveStaSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:apAPReceiveStaSNR.setStatus(_A)
_ApStaTxPkts_Type=Counter32
_ApStaTxPkts_Object=MibTableColumn
apStaTxPkts=_ApStaTxPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,7,1,1,5),_ApStaTxPkts_Type())
apStaTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaTxPkts.setStatus(_A)
_ApStaTxBytes_Type=Counter64
_ApStaTxBytes_Object=MibTableColumn
apStaTxBytes=_ApStaTxBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,7,1,1,6),_ApStaTxBytes_Type())
apStaTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaTxBytes.setStatus(_A)
_ApStaRxPkts_Type=Counter32
_ApStaRxPkts_Object=MibTableColumn
apStaRxPkts=_ApStaRxPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,7,1,1,7),_ApStaRxPkts_Type())
apStaRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaRxPkts.setStatus(_A)
_ApStaRxBytes_Type=Counter64
_ApStaRxBytes_Object=MibTableColumn
apStaRxBytes=_ApStaRxBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,7,1,1,8),_ApStaRxBytes_Type())
apStaRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaRxBytes.setStatus(_A)
_ApWAPISTAAddress_Type=MacAddress
_ApWAPISTAAddress_Object=MibTableColumn
apWAPISTAAddress=_ApWAPISTAAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,7,1,1,9),_ApWAPISTAAddress_Type())
apWAPISTAAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPISTAAddress.setStatus(_A)
_ApWAPIVersion_Type=Integer32
_ApWAPIVersion_Object=MibTableColumn
apWAPIVersion=_ApWAPIVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,7,1,1,10),_ApWAPIVersion_Type())
apWAPIVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIVersion.setStatus(_A)
_ApStaLinkSpeed_Type=Integer32
_ApStaLinkSpeed_Object=MibTableColumn
apStaLinkSpeed=_ApStaLinkSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,7,1,1,11),_ApStaLinkSpeed_Type())
apStaLinkSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaLinkSpeed.setStatus(_A)
_ApStaUpRate_Type=Integer32
_ApStaUpRate_Object=MibTableColumn
apStaUpRate=_ApStaUpRate_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,7,1,1,12),_ApStaUpRate_Type())
apStaUpRate.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaUpRate.setStatus(_A)
_ApStaDownRate_Type=Integer32
_ApStaDownRate_Object=MibTableColumn
apStaDownRate=_ApStaDownRate_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,7,1,1,13),_ApStaDownRate_Type())
apStaDownRate.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaDownRate.setStatus(_A)
_ApStaTxThroughput_Type=Counter32
_ApStaTxThroughput_Object=MibTableColumn
apStaTxThroughput=_ApStaTxThroughput_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,7,1,1,14),_ApStaTxThroughput_Type())
apStaTxThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaTxThroughput.setStatus(_A)
_ApStaRxThroughput_Type=Counter32
_ApStaRxThroughput_Object=MibTableColumn
apStaRxThroughput=_ApStaRxThroughput_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,7,1,1,15),_ApStaRxThroughput_Type())
apStaRxThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaRxThroughput.setStatus(_A)
_ApStaRxRetryBytes_Type=Counter64
_ApStaRxRetryBytes_Object=MibTableColumn
apStaRxRetryBytes=_ApStaRxRetryBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,7,1,1,16),_ApStaRxRetryBytes_Type())
apStaRxRetryBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaRxRetryBytes.setStatus(_A)
_ApQOSStatisticsObjects_ObjectIdentity=ObjectIdentity
apQOSStatisticsObjects=_ApQOSStatisticsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,10,8))
_ApQOSBaseStatisticsObjects_ObjectIdentity=ObjectIdentity
apQOSBaseStatisticsObjects=_ApQOSBaseStatisticsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,1))
_ApQOSBaseStatisticsTable_Object=MibTable
apQOSBaseStatisticsTable=_ApQOSBaseStatisticsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,1,1))
if mibBuilder.loadTexts:apQOSBaseStatisticsTable.setStatus(_A)
_ApQOSBaseStatisticsTableEntry_Object=MibTableRow
apQOSBaseStatisticsTableEntry=_ApQOSBaseStatisticsTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,1,1,1))
apQOSBaseStatisticsTableEntry.setIndexNames((0,_E,_F),(0,_E,_J))
if mibBuilder.loadTexts:apQOSBaseStatisticsTableEntry.setStatus(_A)
_ApBaseQoSSvcQueAvgLen_Type=Integer32
_ApBaseQoSSvcQueAvgLen_Object=MibTableColumn
apBaseQoSSvcQueAvgLen=_ApBaseQoSSvcQueAvgLen_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,1,1,1,1),_ApBaseQoSSvcQueAvgLen_Type())
apBaseQoSSvcQueAvgLen.setMaxAccess(_B)
if mibBuilder.loadTexts:apBaseQoSSvcQueAvgLen.setStatus(_A)
_ApBaseQoSSvcPktLossRatio_Type=Integer32
_ApBaseQoSSvcPktLossRatio_Object=MibTableColumn
apBaseQoSSvcPktLossRatio=_ApBaseQoSSvcPktLossRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,1,1,1,2),_ApBaseQoSSvcPktLossRatio_Type())
apBaseQoSSvcPktLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:apBaseQoSSvcPktLossRatio.setStatus(_A)
_ApBaseAvgTransSpeed_Type=Integer32
_ApBaseAvgTransSpeed_Object=MibTableColumn
apBaseAvgTransSpeed=_ApBaseAvgTransSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,1,1,1,3),_ApBaseAvgTransSpeed_Type())
apBaseAvgTransSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:apBaseAvgTransSpeed.setStatus(_A)
_ApQOSBackgroundStatisticsObjects_ObjectIdentity=ObjectIdentity
apQOSBackgroundStatisticsObjects=_ApQOSBackgroundStatisticsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,2))
_ApQOSBackgroundStatisticsTable_Object=MibTable
apQOSBackgroundStatisticsTable=_ApQOSBackgroundStatisticsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,2,1))
if mibBuilder.loadTexts:apQOSBackgroundStatisticsTable.setStatus(_A)
_ApQOSBackgroundStatisticsTableEntry_Object=MibTableRow
apQOSBackgroundStatisticsTableEntry=_ApQOSBackgroundStatisticsTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,2,1,1))
apQOSBackgroundStatisticsTableEntry.setIndexNames((0,_E,_F),(0,_E,_J))
if mibBuilder.loadTexts:apQOSBackgroundStatisticsTableEntry.setStatus(_A)
_ApQOSBgQueAvgLen_Type=Integer32
_ApQOSBgQueAvgLen_Object=MibTableColumn
apQOSBgQueAvgLen=_ApQOSBgQueAvgLen_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,2,1,1,1),_ApQOSBgQueAvgLen_Type())
apQOSBgQueAvgLen.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSBgQueAvgLen.setStatus(_A)
_ApQOSBgAvgBurst_Type=Integer32
_ApQOSBgAvgBurst_Object=MibTableColumn
apQOSBgAvgBurst=_ApQOSBgAvgBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,2,1,1,2),_ApQOSBgAvgBurst_Type())
apQOSBgAvgBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSBgAvgBurst.setStatus(_A)
_ApQOSBgPktLossRatio_Type=Integer32
_ApQOSBgPktLossRatio_Object=MibTableColumn
apQOSBgPktLossRatio=_ApQOSBgPktLossRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,2,1,1,3),_ApQOSBgPktLossRatio_Type())
apQOSBgPktLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSBgPktLossRatio.setStatus(_A)
_ApQOSBgAvgTransSpeed_Type=Integer32
_ApQOSBgAvgTransSpeed_Object=MibTableColumn
apQOSBgAvgTransSpeed=_ApQOSBgAvgTransSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,2,1,1,4),_ApQOSBgAvgTransSpeed_Type())
apQOSBgAvgTransSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSBgAvgTransSpeed.setStatus(_A)
_ApQOSBgSvcLoss_Type=Integer32
_ApQOSBgSvcLoss_Object=MibTableColumn
apQOSBgSvcLoss=_ApQOSBgSvcLoss_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,2,1,1,5),_ApQOSBgSvcLoss_Type())
apQOSBgSvcLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSBgSvcLoss.setStatus(_A)
_ApQOSBestEffortStatisticsObjects_ObjectIdentity=ObjectIdentity
apQOSBestEffortStatisticsObjects=_ApQOSBestEffortStatisticsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,3))
_ApQOSBestEffortStatisticsTable_Object=MibTable
apQOSBestEffortStatisticsTable=_ApQOSBestEffortStatisticsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,3,1))
if mibBuilder.loadTexts:apQOSBestEffortStatisticsTable.setStatus(_A)
_ApQOSBestEffortStatisticsTableEntry_Object=MibTableRow
apQOSBestEffortStatisticsTableEntry=_ApQOSBestEffortStatisticsTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,3,1,1))
apQOSBestEffortStatisticsTableEntry.setIndexNames((0,_E,_F),(0,_E,_J))
if mibBuilder.loadTexts:apQOSBestEffortStatisticsTableEntry.setStatus(_A)
_ApQOSBeQueAvgLen_Type=Integer32
_ApQOSBeQueAvgLen_Object=MibTableColumn
apQOSBeQueAvgLen=_ApQOSBeQueAvgLen_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,3,1,1,1),_ApQOSBeQueAvgLen_Type())
apQOSBeQueAvgLen.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSBeQueAvgLen.setStatus(_A)
_ApQOSBeAvgBurst_Type=Integer32
_ApQOSBeAvgBurst_Object=MibTableColumn
apQOSBeAvgBurst=_ApQOSBeAvgBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,3,1,1,2),_ApQOSBeAvgBurst_Type())
apQOSBeAvgBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSBeAvgBurst.setStatus(_A)
_ApQOSBePktLossRatio_Type=Integer32
_ApQOSBePktLossRatio_Object=MibTableColumn
apQOSBePktLossRatio=_ApQOSBePktLossRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,3,1,1,3),_ApQOSBePktLossRatio_Type())
apQOSBePktLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSBePktLossRatio.setStatus(_A)
_ApQOSBeAvgTransSpeed_Type=Integer32
_ApQOSBeAvgTransSpeed_Object=MibTableColumn
apQOSBeAvgTransSpeed=_ApQOSBeAvgTransSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,3,1,1,4),_ApQOSBeAvgTransSpeed_Type())
apQOSBeAvgTransSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSBeAvgTransSpeed.setStatus(_A)
_ApQOSBeSvcLoss_Type=Integer32
_ApQOSBeSvcLoss_Object=MibTableColumn
apQOSBeSvcLoss=_ApQOSBeSvcLoss_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,3,1,1,5),_ApQOSBeSvcLoss_Type())
apQOSBeSvcLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSBeSvcLoss.setStatus(_A)
_ApQOSVoiceStatisticsObjects_ObjectIdentity=ObjectIdentity
apQOSVoiceStatisticsObjects=_ApQOSVoiceStatisticsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,4))
_ApQOSVoiceStatisticsTable_Object=MibTable
apQOSVoiceStatisticsTable=_ApQOSVoiceStatisticsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,4,1))
if mibBuilder.loadTexts:apQOSVoiceStatisticsTable.setStatus(_A)
_ApQOSVoiceStatisticsTableEntry_Object=MibTableRow
apQOSVoiceStatisticsTableEntry=_ApQOSVoiceStatisticsTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,4,1,1))
apQOSVoiceStatisticsTableEntry.setIndexNames((0,_E,_F),(0,_E,_J))
if mibBuilder.loadTexts:apQOSVoiceStatisticsTableEntry.setStatus(_A)
_ApQOSVoiceQueAvgLen_Type=Integer32
_ApQOSVoiceQueAvgLen_Object=MibTableColumn
apQOSVoiceQueAvgLen=_ApQOSVoiceQueAvgLen_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,4,1,1,1),_ApQOSVoiceQueAvgLen_Type())
apQOSVoiceQueAvgLen.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSVoiceQueAvgLen.setStatus(_A)
_ApQOSVoiceAvgBurst_Type=Integer32
_ApQOSVoiceAvgBurst_Object=MibTableColumn
apQOSVoiceAvgBurst=_ApQOSVoiceAvgBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,4,1,1,2),_ApQOSVoiceAvgBurst_Type())
apQOSVoiceAvgBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSVoiceAvgBurst.setStatus(_A)
_ApQOSVoicePktLossRatio_Type=Integer32
_ApQOSVoicePktLossRatio_Object=MibTableColumn
apQOSVoicePktLossRatio=_ApQOSVoicePktLossRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,4,1,1,3),_ApQOSVoicePktLossRatio_Type())
apQOSVoicePktLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSVoicePktLossRatio.setStatus(_A)
_ApQOSVoiceAvgTransSpeed_Type=Integer32
_ApQOSVoiceAvgTransSpeed_Object=MibTableColumn
apQOSVoiceAvgTransSpeed=_ApQOSVoiceAvgTransSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,4,1,1,4),_ApQOSVoiceAvgTransSpeed_Type())
apQOSVoiceAvgTransSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSVoiceAvgTransSpeed.setStatus(_A)
_ApQOSVoicePutThroughRatio_Type=Integer32
_ApQOSVoicePutThroughRatio_Object=MibTableColumn
apQOSVoicePutThroughRatio=_ApQOSVoicePutThroughRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,4,1,1,5),_ApQOSVoicePutThroughRatio_Type())
apQOSVoicePutThroughRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSVoicePutThroughRatio.setStatus(_A)
_ApQOSVoiceDropRatio_Type=Integer32
_ApQOSVoiceDropRatio_Object=MibTableColumn
apQOSVoiceDropRatio=_ApQOSVoiceDropRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,4,1,1,6),_ApQOSVoiceDropRatio_Type())
apQOSVoiceDropRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSVoiceDropRatio.setStatus(_A)
_ApQOSVoiceSvcLoss_Type=Integer32
_ApQOSVoiceSvcLoss_Object=MibTableColumn
apQOSVoiceSvcLoss=_ApQOSVoiceSvcLoss_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,4,1,1,7),_ApQOSVoiceSvcLoss_Type())
apQOSVoiceSvcLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSVoiceSvcLoss.setStatus(_A)
_ApQOSVoiceExceedMaxUsersRequest_Type=Counter32
_ApQOSVoiceExceedMaxUsersRequest_Object=MibTableColumn
apQOSVoiceExceedMaxUsersRequest=_ApQOSVoiceExceedMaxUsersRequest_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,4,1,1,8),_ApQOSVoiceExceedMaxUsersRequest_Type())
apQOSVoiceExceedMaxUsersRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSVoiceExceedMaxUsersRequest.setStatus(_A)
_ApQOSVideoStatisticsObjects_ObjectIdentity=ObjectIdentity
apQOSVideoStatisticsObjects=_ApQOSVideoStatisticsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,5))
_ApQOSVideoStatisticsTable_Object=MibTable
apQOSVideoStatisticsTable=_ApQOSVideoStatisticsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,5,1))
if mibBuilder.loadTexts:apQOSVideoStatisticsTable.setStatus(_A)
_ApQOSVideoStatisticsTableEntry_Object=MibTableRow
apQOSVideoStatisticsTableEntry=_ApQOSVideoStatisticsTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,5,1,1))
apQOSVideoStatisticsTableEntry.setIndexNames((0,_E,_F),(0,_E,_J))
if mibBuilder.loadTexts:apQOSVideoStatisticsTableEntry.setStatus(_A)
_ApQOSVideoQueAvgLen_Type=Integer32
_ApQOSVideoQueAvgLen_Object=MibTableColumn
apQOSVideoQueAvgLen=_ApQOSVideoQueAvgLen_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,5,1,1,1),_ApQOSVideoQueAvgLen_Type())
apQOSVideoQueAvgLen.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSVideoQueAvgLen.setStatus(_A)
_ApQOSVideoAvgBurst_Type=Integer32
_ApQOSVideoAvgBurst_Object=MibTableColumn
apQOSVideoAvgBurst=_ApQOSVideoAvgBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,5,1,1,2),_ApQOSVideoAvgBurst_Type())
apQOSVideoAvgBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSVideoAvgBurst.setStatus(_A)
_ApQOSVideoPktLossRatio_Type=Integer32
_ApQOSVideoPktLossRatio_Object=MibTableColumn
apQOSVideoPktLossRatio=_ApQOSVideoPktLossRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,5,1,1,3),_ApQOSVideoPktLossRatio_Type())
apQOSVideoPktLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSVideoPktLossRatio.setStatus(_A)
_ApQOSVideoAvgTransSpeed_Type=Integer32
_ApQOSVideoAvgTransSpeed_Object=MibTableColumn
apQOSVideoAvgTransSpeed=_ApQOSVideoAvgTransSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,5,1,1,4),_ApQOSVideoAvgTransSpeed_Type())
apQOSVideoAvgTransSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSVideoAvgTransSpeed.setStatus(_A)
_ApQOSVideoPutThroughRatio_Type=Integer32
_ApQOSVideoPutThroughRatio_Object=MibTableColumn
apQOSVideoPutThroughRatio=_ApQOSVideoPutThroughRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,5,1,1,5),_ApQOSVideoPutThroughRatio_Type())
apQOSVideoPutThroughRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSVideoPutThroughRatio.setStatus(_A)
_ApQOSVideoDropRatio_Type=Integer32
_ApQOSVideoDropRatio_Object=MibTableColumn
apQOSVideoDropRatio=_ApQOSVideoDropRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,5,1,1,6),_ApQOSVideoDropRatio_Type())
apQOSVideoDropRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSVideoDropRatio.setStatus(_A)
_ApQOSVideoSvcLoss_Type=Integer32
_ApQOSVideoSvcLoss_Object=MibTableColumn
apQOSVideoSvcLoss=_ApQOSVideoSvcLoss_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,5,1,1,7),_ApQOSVideoSvcLoss_Type())
apQOSVideoSvcLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSVideoSvcLoss.setStatus(_A)
_ApQOSVideoExceedMaxUsersRequest_Type=Counter32
_ApQOSVideoExceedMaxUsersRequest_Object=MibTableColumn
apQOSVideoExceedMaxUsersRequest=_ApQOSVideoExceedMaxUsersRequest_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,8,5,1,1,8),_ApQOSVideoExceedMaxUsersRequest_Type())
apQOSVideoExceedMaxUsersRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:apQOSVideoExceedMaxUsersRequest.setStatus(_A)
_ApWIDSRogueApInfoObjects_ObjectIdentity=ObjectIdentity
apWIDSRogueApInfoObjects=_ApWIDSRogueApInfoObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,10,9))
_ApWIDSRogueApInfoTable_Object=MibTable
apWIDSRogueApInfoTable=_ApWIDSRogueApInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,9,1))
if mibBuilder.loadTexts:apWIDSRogueApInfoTable.setStatus(_A)
_ApWIDSRogueApInfoTableEntry_Object=MibTableRow
apWIDSRogueApInfoTableEntry=_ApWIDSRogueApInfoTableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,9,1,1))
apWIDSRogueApInfoTableEntry.setIndexNames((0,_D,_AI))
if mibBuilder.loadTexts:apWIDSRogueApInfoTableEntry.setStatus(_A)
_QtechRogueApMacAddr_Type=MacAddress
_QtechRogueApMacAddr_Object=MibTableColumn
qtechRogueApMacAddr=_QtechRogueApMacAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,9,1,1,1),_QtechRogueApMacAddr_Type())
qtechRogueApMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechRogueApMacAddr.setStatus(_A)
_QtechRogueApRSSI_Type=Integer32
_QtechRogueApRSSI_Object=MibTableColumn
qtechRogueApRSSI=_QtechRogueApRSSI_Object((1,3,6,1,4,1,27514,1,1,10,2,81,10,9,1,1,2),_QtechRogueApRSSI_Type())
qtechRogueApRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechRogueApRSSI.setStatus(_A)
_ApQtechAlarmTrapObjects_ObjectIdentity=ObjectIdentity
apQtechAlarmTrapObjects=_ApQtechAlarmTrapObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,11))
_ApAPMac_Type=MacAddress
_ApAPMac_Object=MibScalar
apAPMac=_ApAPMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,1),_ApAPMac_Type())
apAPMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apAPMac.setStatus(_A)
_ApWorkModeBeforeChange_Type=Integer32
_ApWorkModeBeforeChange_Object=MibScalar
apWorkModeBeforeChange=_ApWorkModeBeforeChange_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,2),_ApWorkModeBeforeChange_Type())
apWorkModeBeforeChange.setMaxAccess(_B)
if mibBuilder.loadTexts:apWorkModeBeforeChange.setStatus(_A)
_ApWorkModeAfterChange_Type=Integer32
_ApWorkModeAfterChange_Object=MibScalar
apWorkModeAfterChange=_ApWorkModeAfterChange_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,3),_ApWorkModeAfterChange_Type())
apWorkModeAfterChange.setMaxAccess(_B)
if mibBuilder.loadTexts:apWorkModeAfterChange.setStatus(_A)
_ApSSIDKey_Type=DisplayString
_ApSSIDKey_Object=MibScalar
apSSIDKey=_ApSSIDKey_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,4),_ApSSIDKey_Type())
apSSIDKey.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDKey.setStatus(_A)
_ApSSIDKeyConflict_Type=DisplayString
_ApSSIDKeyConflict_Object=MibScalar
apSSIDKeyConflict=_ApSSIDKeyConflict_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,5),_ApSSIDKeyConflict_Type())
apSSIDKeyConflict.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDKeyConflict.setStatus(_A)
_ApCyperIndex_Type=Integer32
_ApCyperIndex_Object=MibScalar
apCyperIndex=_ApCyperIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,6),_ApCyperIndex_Type())
apCyperIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:apCyperIndex.setStatus(_A)
_ApInterruptReason_Type=DisplayString
_ApInterruptReason_Object=MibScalar
apInterruptReason=_ApInterruptReason_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,7),_ApInterruptReason_Type())
apInterruptReason.setMaxAccess(_B)
if mibBuilder.loadTexts:apInterruptReason.setStatus(_A)
_ApWorkingAPRadioIfInfo_Type=MacAddress
_ApWorkingAPRadioIfInfo_Object=MibScalar
apWorkingAPRadioIfInfo=_ApWorkingAPRadioIfInfo_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,8),_ApWorkingAPRadioIfInfo_Type())
apWorkingAPRadioIfInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:apWorkingAPRadioIfInfo.setStatus(_A)
_ApWorkingAPChannel_Type=Integer32
_ApWorkingAPChannel_Object=MibScalar
apWorkingAPChannel=_ApWorkingAPChannel_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,9),_ApWorkingAPChannel_Type())
apWorkingAPChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:apWorkingAPChannel.setStatus(_A)
_ApInterfAPChannel_Type=Integer32
_ApInterfAPChannel_Object=MibScalar
apInterfAPChannel=_ApInterfAPChannel_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,10),_ApInterfAPChannel_Type())
apInterfAPChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:apInterfAPChannel.setStatus(_A)
_ApInterfAPBSSID_Type=MacAddress
_ApInterfAPBSSID_Object=MibScalar
apInterfAPBSSID=_ApInterfAPBSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,11),_ApInterfAPBSSID_Type())
apInterfAPBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:apInterfAPBSSID.setStatus(_A)
_ApInterfStaMac_Type=MacAddress
_ApInterfStaMac_Object=MibScalar
apInterfStaMac=_ApInterfStaMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,12),_ApInterfStaMac_Type())
apInterfStaMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apInterfStaMac.setStatus(_A)
_ApPermitAssoUser_Type=Integer32
_ApPermitAssoUser_Object=MibScalar
apPermitAssoUser=_ApPermitAssoUser_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,13),_ApPermitAssoUser_Type())
apPermitAssoUser.setMaxAccess(_B)
if mibBuilder.loadTexts:apPermitAssoUser.setStatus(_A)
_ApAssoFailReason_Type=DisplayString
_ApAssoFailReason_Object=MibScalar
apAssoFailReason=_ApAssoFailReason_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,14),_ApAssoFailReason_Type())
apAssoFailReason.setMaxAccess(_B)
if mibBuilder.loadTexts:apAssoFailReason.setStatus(_A)
_ApChannelBeforeChange_Type=Integer32
_ApChannelBeforeChange_Object=MibScalar
apChannelBeforeChange=_ApChannelBeforeChange_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,15),_ApChannelBeforeChange_Type())
apChannelBeforeChange.setMaxAccess(_B)
if mibBuilder.loadTexts:apChannelBeforeChange.setStatus(_A)
_ApChannelAfterChange_Type=Integer32
_ApChannelAfterChange_Object=MibScalar
apChannelAfterChange=_ApChannelAfterChange_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,16),_ApChannelAfterChange_Type())
apChannelAfterChange.setMaxAccess(_B)
if mibBuilder.loadTexts:apChannelAfterChange.setStatus(_A)
_ApChanChangeMode_Type=Integer32
_ApChanChangeMode_Object=MibScalar
apChanChangeMode=_ApChanChangeMode_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,17),_ApChanChangeMode_Type())
apChanChangeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:apChanChangeMode.setStatus(_A)
_ApWorkingAPBSSID_Type=MacAddress
_ApWorkingAPBSSID_Object=MibScalar
apWorkingAPBSSID=_ApWorkingAPBSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,18),_ApWorkingAPBSSID_Type())
apWorkingAPBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:apWorkingAPBSSID.setStatus(_A)
_ApWorkingAPSSID_Type=DisplayString
_ApWorkingAPSSID_Object=MibScalar
apWorkingAPSSID=_ApWorkingAPSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,19),_ApWorkingAPSSID_Type())
apWorkingAPSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:apWorkingAPSSID.setStatus(_A)
_ApStaMacAddr_Type=MacAddress
_ApStaMacAddr_Object=MibScalar
apStaMacAddr=_ApStaMacAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,20),_ApStaMacAddr_Type())
apStaMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaMacAddr.setStatus(_A)
_ApAuthMode_Type=Integer32
_ApAuthMode_Object=MibScalar
apAuthMode=_ApAuthMode_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,21),_ApAuthMode_Type())
apAuthMode.setMaxAccess(_B)
if mibBuilder.loadTexts:apAuthMode.setStatus(_A)
_ApAuthFailReason_Type=DisplayString
_ApAuthFailReason_Object=MibScalar
apAuthFailReason=_ApAuthFailReason_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,22),_ApAuthFailReason_Type())
apAuthFailReason.setMaxAccess(_B)
if mibBuilder.loadTexts:apAuthFailReason.setStatus(_A)
_UpdateFailReason_Type=DisplayString
_UpdateFailReason_Object=MibScalar
updateFailReason=_UpdateFailReason_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,23),_UpdateFailReason_Type())
updateFailReason.setMaxAccess(_B)
if mibBuilder.loadTexts:updateFailReason.setStatus(_A)
_ApSWVersionBeforeUpdate_Type=DisplayString
_ApSWVersionBeforeUpdate_Object=MibScalar
apSWVersionBeforeUpdate=_ApSWVersionBeforeUpdate_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,24),_ApSWVersionBeforeUpdate_Type())
apSWVersionBeforeUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:apSWVersionBeforeUpdate.setStatus(_A)
_ApAPRadioId_Type=Integer32
_ApAPRadioId_Object=MibScalar
apAPRadioId=_ApAPRadioId_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,25),_ApAPRadioId_Type())
apAPRadioId.setMaxAccess(_B)
if mibBuilder.loadTexts:apAPRadioId.setStatus(_A)
_ApRevPackages_Type=Integer32
_ApRevPackages_Object=MibScalar
apRevPackages=_ApRevPackages_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,26),_ApRevPackages_Type())
apRevPackages.setMaxAccess(_B)
if mibBuilder.loadTexts:apRevPackages.setStatus(_A)
_ApCPUUsage_Type=Integer32
_ApCPUUsage_Object=MibScalar
apCPUUsage=_ApCPUUsage_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,27),_ApCPUUsage_Type())
apCPUUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:apCPUUsage.setStatus(_A)
_ApSpeciousDeviceMac_Type=MacAddress
_ApSpeciousDeviceMac_Object=MibScalar
apSpeciousDeviceMac=_ApSpeciousDeviceMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,28),_ApSpeciousDeviceMac_Type())
apSpeciousDeviceMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apSpeciousDeviceMac.setStatus(_A)
_ApRSSI_Type=Integer32
_ApRSSI_Object=MibScalar
apRSSI=_ApRSSI_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,29),_ApRSSI_Type())
apRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:apRSSI.setStatus(_A)
_ApAttackReason_Type=DisplayString
_ApAttackReason_Object=MibScalar
apAttackReason=_ApAttackReason_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,30),_ApAttackReason_Type())
apAttackReason.setMaxAccess(_B)
if mibBuilder.loadTexts:apAttackReason.setStatus(_A)
_ApWlanId_Type=Integer32
_ApWlanId_Object=MibScalar
apWlanId=_ApWlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,31),_ApWlanId_Type())
apWlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:apWlanId.setStatus(_A)
_ApWlanSSID_Type=DisplayString
_ApWlanSSID_Object=MibScalar
apWlanSSID=_ApWlanSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,32),_ApWlanSSID_Type())
apWlanSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:apWlanSSID.setStatus(_A)
_ApWlanSecurityModeBeforeChg_Type=DisplayString
_ApWlanSecurityModeBeforeChg_Object=MibScalar
apWlanSecurityModeBeforeChg=_ApWlanSecurityModeBeforeChg_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,33),_ApWlanSecurityModeBeforeChg_Type())
apWlanSecurityModeBeforeChg.setMaxAccess(_B)
if mibBuilder.loadTexts:apWlanSecurityModeBeforeChg.setStatus(_A)
_ApWlanSecurityModeAfterChg_Type=DisplayString
_ApWlanSecurityModeAfterChg_Object=MibScalar
apWlanSecurityModeAfterChg=_ApWlanSecurityModeAfterChg_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,34),_ApWlanSecurityModeAfterChg_Type())
apWlanSecurityModeAfterChg.setMaxAccess(_B)
if mibBuilder.loadTexts:apWlanSecurityModeAfterChg.setStatus(_A)
_ApTrapIllegalApMac_Type=MacAddress
_ApTrapIllegalApMac_Object=MibScalar
apTrapIllegalApMac=_ApTrapIllegalApMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,35),_ApTrapIllegalApMac_Type())
apTrapIllegalApMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apTrapIllegalApMac.setStatus(_A)
_ApTrapIllegalApChannel_Type=Integer32
_ApTrapIllegalApChannel_Object=MibScalar
apTrapIllegalApChannel=_ApTrapIllegalApChannel_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,36),_ApTrapIllegalApChannel_Type())
apTrapIllegalApChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:apTrapIllegalApChannel.setStatus(_A)
_ApTrapIllegalApRSSI_Type=Integer32
_ApTrapIllegalApRSSI_Object=MibScalar
apTrapIllegalApRSSI=_ApTrapIllegalApRSSI_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,37),_ApTrapIllegalApRSSI_Type())
apTrapIllegalApRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:apTrapIllegalApRSSI.setStatus(_A)
_ApTrapWorkingApMac_Type=MacAddress
_ApTrapWorkingApMac_Object=MibScalar
apTrapWorkingApMac=_ApTrapWorkingApMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,38),_ApTrapWorkingApMac_Type())
apTrapWorkingApMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apTrapWorkingApMac.setStatus(_A)
_ApTrapWorkingApBSSID_Type=MacAddress
_ApTrapWorkingApBSSID_Object=MibScalar
apTrapWorkingApBSSID=_ApTrapWorkingApBSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,39),_ApTrapWorkingApBSSID_Type())
apTrapWorkingApBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:apTrapWorkingApBSSID.setStatus(_A)
_ApTrapIllegalApType_Type=Integer32
_ApTrapIllegalApType_Object=MibScalar
apTrapIllegalApType=_ApTrapIllegalApType_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,40),_ApTrapIllegalApType_Type())
apTrapIllegalApType.setMaxAccess(_B)
if mibBuilder.loadTexts:apTrapIllegalApType.setStatus(_A)
_ApTrapIllegalApSSID_Type=DisplayString
_ApTrapIllegalApSSID_Object=MibScalar
apTrapIllegalApSSID=_ApTrapIllegalApSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,41),_ApTrapIllegalApSSID_Type())
apTrapIllegalApSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:apTrapIllegalApSSID.setStatus(_A)
class _ApAPRadioType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_d,0),(_e,1)))
_ApAPRadioType_Type.__name__=_G
_ApAPRadioType_Object=MibScalar
apAPRadioType=_ApAPRadioType_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,42),_ApAPRadioType_Type())
apAPRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:apAPRadioType.setStatus(_A)
_ApAssocAuthMode_Type=Integer32
_ApAssocAuthMode_Object=MibScalar
apAssocAuthMode=_ApAssocAuthMode_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,43),_ApAssocAuthMode_Type())
apAssocAuthMode.setMaxAccess(_B)
if mibBuilder.loadTexts:apAssocAuthMode.setStatus(_A)
_ApStaRSSI_Type=DisplayString
_ApStaRSSI_Object=MibScalar
apStaRSSI=_ApStaRSSI_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,44),_ApStaRSSI_Type())
apStaRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaRSSI.setStatus(_A)
_ApAssocFailReason_Type=Integer32
_ApAssocFailReason_Object=MibScalar
apAssocFailReason=_ApAssocFailReason_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,45),_ApAssocFailReason_Type())
apAssocFailReason.setMaxAccess(_B)
if mibBuilder.loadTexts:apAssocFailReason.setStatus(_A)
_ApSpectralInfoApMac_Type=MacAddress
_ApSpectralInfoApMac_Object=MibScalar
apSpectralInfoApMac=_ApSpectralInfoApMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,46),_ApSpectralInfoApMac_Type())
apSpectralInfoApMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apSpectralInfoApMac.setStatus(_A)
_ApSpectralInfoType_Type=Integer32
_ApSpectralInfoType_Object=MibScalar
apSpectralInfoType=_ApSpectralInfoType_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,47),_ApSpectralInfoType_Type())
apSpectralInfoType.setMaxAccess(_B)
if mibBuilder.loadTexts:apSpectralInfoType.setStatus(_A)
_ApSpectralInfoFreq_Type=Integer32
_ApSpectralInfoFreq_Object=MibScalar
apSpectralInfoFreq=_ApSpectralInfoFreq_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,48),_ApSpectralInfoFreq_Type())
apSpectralInfoFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:apSpectralInfoFreq.setStatus(_A)
_ApSpectralInfoRssi_Type=Integer32
_ApSpectralInfoRssi_Object=MibScalar
apSpectralInfoRssi=_ApSpectralInfoRssi_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,49),_ApSpectralInfoRssi_Type())
apSpectralInfoRssi.setMaxAccess(_B)
if mibBuilder.loadTexts:apSpectralInfoRssi.setStatus(_A)
_ApCounterMeasureApMac_Type=MacAddress
_ApCounterMeasureApMac_Object=MibScalar
apCounterMeasureApMac=_ApCounterMeasureApMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,50),_ApCounterMeasureApMac_Type())
apCounterMeasureApMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apCounterMeasureApMac.setStatus(_A)
_ApCounterMeasureBssid_Type=MacAddress
_ApCounterMeasureBssid_Object=MibScalar
apCounterMeasureBssid=_ApCounterMeasureBssid_Object((1,3,6,1,4,1,27514,1,1,10,2,81,11,51),_ApCounterMeasureBssid_Type())
apCounterMeasureBssid.setMaxAccess(_B)
if mibBuilder.loadTexts:apCounterMeasureBssid.setStatus(_A)
_ApAccessControl_ObjectIdentity=ObjectIdentity
apAccessControl=_ApAccessControl_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,12))
_ApTerminalPermitTable_Object=MibTable
apTerminalPermitTable=_ApTerminalPermitTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,12,1))
if mibBuilder.loadTexts:apTerminalPermitTable.setStatus(_A)
_ApTerminalPermitEntry_Object=MibTableRow
apTerminalPermitEntry=_ApTerminalPermitEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,12,1,1))
apTerminalPermitEntry.setIndexNames((0,_D,_AJ))
if mibBuilder.loadTexts:apTerminalPermitEntry.setStatus(_A)
_ApWhiteListIndex_Type=Integer32
_ApWhiteListIndex_Object=MibTableColumn
apWhiteListIndex=_ApWhiteListIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,81,12,1,1,1),_ApWhiteListIndex_Type())
apWhiteListIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:apWhiteListIndex.setStatus(_A)
_ApPermitMAC_Type=MacAddress
_ApPermitMAC_Object=MibTableColumn
apPermitMAC=_ApPermitMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,81,12,1,1,2),_ApPermitMAC_Type())
apPermitMAC.setMaxAccess(_H)
if mibBuilder.loadTexts:apPermitMAC.setStatus(_A)
_ApWhiteListStatus_Type=RowStatus
_ApWhiteListStatus_Object=MibTableColumn
apWhiteListStatus=_ApWhiteListStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,81,12,1,1,3),_ApWhiteListStatus_Type())
apWhiteListStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:apWhiteListStatus.setStatus(_A)
_ApTerminalDeniedTable_Object=MibTable
apTerminalDeniedTable=_ApTerminalDeniedTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,12,2))
if mibBuilder.loadTexts:apTerminalDeniedTable.setStatus(_A)
_ApTerminalDeniedEntry_Object=MibTableRow
apTerminalDeniedEntry=_ApTerminalDeniedEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,12,2,1))
apTerminalDeniedEntry.setIndexNames((0,_D,_AK))
if mibBuilder.loadTexts:apTerminalDeniedEntry.setStatus(_A)
_ApBlackListIndex_Type=Integer32
_ApBlackListIndex_Object=MibTableColumn
apBlackListIndex=_ApBlackListIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,81,12,2,1,1),_ApBlackListIndex_Type())
apBlackListIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:apBlackListIndex.setStatus(_A)
_ApAttackDeviceMAC_Type=MacAddress
_ApAttackDeviceMAC_Object=MibTableColumn
apAttackDeviceMAC=_ApAttackDeviceMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,81,12,2,1,2),_ApAttackDeviceMAC_Type())
apAttackDeviceMAC.setMaxAccess(_H)
if mibBuilder.loadTexts:apAttackDeviceMAC.setStatus(_A)
_ApBlackListStatus_Type=RowStatus
_ApBlackListStatus_Object=MibTableColumn
apBlackListStatus=_ApBlackListStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,81,12,2,1,3),_ApBlackListStatus_Type())
apBlackListStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:apBlackListStatus.setStatus(_A)
_ApTerminalBlackListTable_Object=MibTable
apTerminalBlackListTable=_ApTerminalBlackListTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,12,3))
if mibBuilder.loadTexts:apTerminalBlackListTable.setStatus(_A)
_ApTerminalBlackListEntry_Object=MibTableRow
apTerminalBlackListEntry=_ApTerminalBlackListEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,12,3,1))
apTerminalBlackListEntry.setIndexNames((0,_D,_AL))
if mibBuilder.loadTexts:apTerminalBlackListEntry.setStatus(_A)
_ApBlackListDeviceMAC_Type=MacAddress
_ApBlackListDeviceMAC_Object=MibTableColumn
apBlackListDeviceMAC=_ApBlackListDeviceMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,81,12,3,1,1),_ApBlackListDeviceMAC_Type())
apBlackListDeviceMAC.setMaxAccess(_H)
if mibBuilder.loadTexts:apBlackListDeviceMAC.setStatus(_A)
_ApBlackListAddReason_Type=OctetString
_ApBlackListAddReason_Object=MibTableColumn
apBlackListAddReason=_ApBlackListAddReason_Object((1,3,6,1,4,1,27514,1,1,10,2,81,12,3,1,2),_ApBlackListAddReason_Type())
apBlackListAddReason.setMaxAccess(_B)
if mibBuilder.loadTexts:apBlackListAddReason.setStatus(_A)
_ApBlackListDuration_Type=TimeTicks
_ApBlackListDuration_Object=MibTableColumn
apBlackListDuration=_ApBlackListDuration_Object((1,3,6,1,4,1,27514,1,1,10,2,81,12,3,1,3),_ApBlackListDuration_Type())
apBlackListDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:apBlackListDuration.setStatus(_A)
_AcCapabilityStatistics_ObjectIdentity=ObjectIdentity
acCapabilityStatistics=_AcCapabilityStatistics_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,13))
_AcWirelessDownDropFrame_Type=Counter64
_AcWirelessDownDropFrame_Object=MibScalar
acWirelessDownDropFrame=_AcWirelessDownDropFrame_Object((1,3,6,1,4,1,27514,1,1,10,2,81,13,1),_AcWirelessDownDropFrame_Type())
acWirelessDownDropFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:acWirelessDownDropFrame.setStatus(_A)
_AcWirelessDownRetryFrame_Type=Counter64
_AcWirelessDownRetryFrame_Object=MibScalar
acWirelessDownRetryFrame=_AcWirelessDownRetryFrame_Object((1,3,6,1,4,1,27514,1,1,10,2,81,13,2),_AcWirelessDownRetryFrame_Type())
acWirelessDownRetryFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:acWirelessDownRetryFrame.setStatus(_A)
_AcWirelessDownFrame_Type=Counter64
_AcWirelessDownFrame_Object=MibScalar
acWirelessDownFrame=_AcWirelessDownFrame_Object((1,3,6,1,4,1,27514,1,1,10,2,81,13,3),_AcWirelessDownFrame_Type())
acWirelessDownFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:acWirelessDownFrame.setStatus(_A)
_AcWirelessDownErrorFrame_Type=Counter64
_AcWirelessDownErrorFrame_Object=MibScalar
acWirelessDownErrorFrame=_AcWirelessDownErrorFrame_Object((1,3,6,1,4,1,27514,1,1,10,2,81,13,4),_AcWirelessDownErrorFrame_Type())
acWirelessDownErrorFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:acWirelessDownErrorFrame.setStatus(_A)
_AcWirelessUpFrame_Type=Counter64
_AcWirelessUpFrame_Object=MibScalar
acWirelessUpFrame=_AcWirelessUpFrame_Object((1,3,6,1,4,1,27514,1,1,10,2,81,13,5),_AcWirelessUpFrame_Type())
acWirelessUpFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:acWirelessUpFrame.setStatus(_A)
_AcWirelessUpDropFrame_Type=Counter64
_AcWirelessUpDropFrame_Object=MibScalar
acWirelessUpDropFrame=_AcWirelessUpDropFrame_Object((1,3,6,1,4,1,27514,1,1,10,2,81,13,6),_AcWirelessUpDropFrame_Type())
acWirelessUpDropFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:acWirelessUpDropFrame.setStatus(_A)
_AcWirelessUpRetryFrame_Type=Counter64
_AcWirelessUpRetryFrame_Object=MibScalar
acWirelessUpRetryFrame=_AcWirelessUpRetryFrame_Object((1,3,6,1,4,1,27514,1,1,10,2,81,13,7),_AcWirelessUpRetryFrame_Type())
acWirelessUpRetryFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:acWirelessUpRetryFrame.setStatus(_A)
_AcWirelessUpRate_Type=Counter64
_AcWirelessUpRate_Object=MibScalar
acWirelessUpRate=_AcWirelessUpRate_Object((1,3,6,1,4,1,27514,1,1,10,2,81,13,8),_AcWirelessUpRate_Type())
acWirelessUpRate.setMaxAccess(_B)
if mibBuilder.loadTexts:acWirelessUpRate.setStatus(_A)
_AcWirelessDownRate_Type=Counter64
_AcWirelessDownRate_Object=MibScalar
acWirelessDownRate=_AcWirelessDownRate_Object((1,3,6,1,4,1,27514,1,1,10,2,81,13,9),_AcWirelessDownRate_Type())
acWirelessDownRate.setMaxAccess(_B)
if mibBuilder.loadTexts:acWirelessDownRate.setStatus(_A)
_ApWidsInfoObjects_ObjectIdentity=ObjectIdentity
apWidsInfoObjects=_ApWidsInfoObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,14))
_ApWidsIllegalApTable_Object=MibTable
apWidsIllegalApTable=_ApWidsIllegalApTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,1))
if mibBuilder.loadTexts:apWidsIllegalApTable.setStatus(_A)
_ApWidsIllegalApEntry_Object=MibTableRow
apWidsIllegalApEntry=_ApWidsIllegalApEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,1,1))
apWidsIllegalApEntry.setIndexNames((0,_D,_AM))
if mibBuilder.loadTexts:apWidsIllegalApEntry.setStatus(_A)
_ApIllegalApMac_Type=MacAddress
_ApIllegalApMac_Object=MibTableColumn
apIllegalApMac=_ApIllegalApMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,1,1,1),_ApIllegalApMac_Type())
apIllegalApMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apIllegalApMac.setStatus(_A)
_ApIllegalApChannel_Type=Integer32
_ApIllegalApChannel_Object=MibTableColumn
apIllegalApChannel=_ApIllegalApChannel_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,1,1,2),_ApIllegalApChannel_Type())
apIllegalApChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:apIllegalApChannel.setStatus(_A)
_ApIllegalApRSSI_Type=Integer32
_ApIllegalApRSSI_Object=MibTableColumn
apIllegalApRSSI=_ApIllegalApRSSI_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,1,1,3),_ApIllegalApRSSI_Type())
apIllegalApRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:apIllegalApRSSI.setStatus(_A)
_ApWorkingApMac_Type=MacAddress
_ApWorkingApMac_Object=MibTableColumn
apWorkingApMac=_ApWorkingApMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,1,1,4),_ApWorkingApMac_Type())
apWorkingApMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apWorkingApMac.setStatus(_A)
_ApDetectAPBSSID_Type=MacAddress
_ApDetectAPBSSID_Object=MibTableColumn
apDetectAPBSSID=_ApDetectAPBSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,1,1,5),_ApDetectAPBSSID_Type())
apDetectAPBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:apDetectAPBSSID.setStatus(_A)
_ApIllegalApType_Type=Integer32
_ApIllegalApType_Object=MibTableColumn
apIllegalApType=_ApIllegalApType_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,1,1,6),_ApIllegalApType_Type())
apIllegalApType.setMaxAccess(_B)
if mibBuilder.loadTexts:apIllegalApType.setStatus(_A)
_ApIllegalApSSID_Type=DisplayString
_ApIllegalApSSID_Object=MibTableColumn
apIllegalApSSID=_ApIllegalApSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,1,1,7),_ApIllegalApSSID_Type())
apIllegalApSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:apIllegalApSSID.setStatus(_A)
_ApWidsApCounterTable_Object=MibTable
apWidsApCounterTable=_ApWidsApCounterTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,2))
if mibBuilder.loadTexts:apWidsApCounterTable.setStatus(_A)
_ApWidsApCounterEntry_Object=MibTableRow
apWidsApCounterEntry=_ApWidsApCounterEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,2,1))
apWidsApCounterEntry.setIndexNames((0,_D,_AN))
if mibBuilder.loadTexts:apWidsApCounterEntry.setStatus(_A)
_ApCounterMac_Type=MacAddress
_ApCounterMac_Object=MibTableColumn
apCounterMac=_ApCounterMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,2,1,1),_ApCounterMac_Type())
apCounterMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apCounterMac.setStatus(_A)
_ApCounter_Type=Integer32
_ApCounter_Object=MibTableColumn
apCounter=_ApCounter_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,2,1,2),_ApCounter_Type())
apCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:apCounter.setStatus(_A)
_ApCounterMode_Type=Integer32
_ApCounterMode_Object=MibTableColumn
apCounterMode=_ApCounterMode_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,2,1,3),_ApCounterMode_Type())
apCounterMode.setMaxAccess(_C)
if mibBuilder.loadTexts:apCounterMode.setStatus(_A)
_ApCounterRssiThreshold_Type=Integer32
_ApCounterRssiThreshold_Object=MibTableColumn
apCounterRssiThreshold=_ApCounterRssiThreshold_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,2,1,4),_ApCounterRssiThreshold_Type())
apCounterRssiThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:apCounterRssiThreshold.setStatus(_A)
_ApWidsDeviceMode_Type=Integer32
_ApWidsDeviceMode_Object=MibScalar
apWidsDeviceMode=_ApWidsDeviceMode_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,3),_ApWidsDeviceMode_Type())
apWidsDeviceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:apWidsDeviceMode.setStatus(_A)
_ApWidsCounterIllegalAp_Type=Integer32
_ApWidsCounterIllegalAp_Object=MibScalar
apWidsCounterIllegalAp=_ApWidsCounterIllegalAp_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,4),_ApWidsCounterIllegalAp_Type())
apWidsCounterIllegalAp.setMaxAccess(_C)
if mibBuilder.loadTexts:apWidsCounterIllegalAp.setStatus(_A)
_ApWidsCounterModeIllegalAp_Type=Integer32
_ApWidsCounterModeIllegalAp_Object=MibScalar
apWidsCounterModeIllegalAp=_ApWidsCounterModeIllegalAp_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,5),_ApWidsCounterModeIllegalAp_Type())
apWidsCounterModeIllegalAp.setMaxAccess(_C)
if mibBuilder.loadTexts:apWidsCounterModeIllegalAp.setStatus(_A)
_ApWidsDeviceModeFlag_Type=Integer32
_ApWidsDeviceModeFlag_Object=MibScalar
apWidsDeviceModeFlag=_ApWidsDeviceModeFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,6),_ApWidsDeviceModeFlag_Type())
apWidsDeviceModeFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:apWidsDeviceModeFlag.setStatus(_A)
_ApWidsCounterIllegalApFlag_Type=Integer32
_ApWidsCounterIllegalApFlag_Object=MibScalar
apWidsCounterIllegalApFlag=_ApWidsCounterIllegalApFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,7),_ApWidsCounterIllegalApFlag_Type())
apWidsCounterIllegalApFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:apWidsCounterIllegalApFlag.setStatus(_A)
_ApWidsCounterModeIllegalApFlag_Type=Integer32
_ApWidsCounterModeIllegalApFlag_Object=MibScalar
apWidsCounterModeIllegalApFlag=_ApWidsCounterModeIllegalApFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,8),_ApWidsCounterModeIllegalApFlag_Type())
apWidsCounterModeIllegalApFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:apWidsCounterModeIllegalApFlag.setStatus(_A)
_ApWidsPermitMacTable_Object=MibTable
apWidsPermitMacTable=_ApWidsPermitMacTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,9))
if mibBuilder.loadTexts:apWidsPermitMacTable.setStatus(_A)
_ApWidsPermitMacEntry_Object=MibTableRow
apWidsPermitMacEntry=_ApWidsPermitMacEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,9,1))
apWidsPermitMacEntry.setIndexNames((0,_D,_AO))
if mibBuilder.loadTexts:apWidsPermitMacEntry.setStatus(_A)
_ApWidsPermitMac_Type=MacAddress
_ApWidsPermitMac_Object=MibTableColumn
apWidsPermitMac=_ApWidsPermitMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,9,1,1),_ApWidsPermitMac_Type())
apWidsPermitMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apWidsPermitMac.setStatus(_A)
_ApPermitMacrowstatus_Type=RowStatus
_ApPermitMacrowstatus_Object=MibTableColumn
apPermitMacrowstatus=_ApPermitMacrowstatus_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,9,1,2),_ApPermitMacrowstatus_Type())
apPermitMacrowstatus.setMaxAccess(_H)
if mibBuilder.loadTexts:apPermitMacrowstatus.setStatus(_A)
_ApWidsPermitSSIDTable_Object=MibTable
apWidsPermitSSIDTable=_ApWidsPermitSSIDTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,10))
if mibBuilder.loadTexts:apWidsPermitSSIDTable.setStatus(_A)
_ApWidsPermitSSIDEntry_Object=MibTableRow
apWidsPermitSSIDEntry=_ApWidsPermitSSIDEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,10,1))
apWidsPermitSSIDEntry.setIndexNames((0,_D,_AP))
if mibBuilder.loadTexts:apWidsPermitSSIDEntry.setStatus(_A)
_ApCounterSSID_Type=DisplayString
_ApCounterSSID_Object=MibTableColumn
apCounterSSID=_ApCounterSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,10,1,1),_ApCounterSSID_Type())
apCounterSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:apCounterSSID.setStatus(_A)
_ApPermitSSIDrowstatus_Type=RowStatus
_ApPermitSSIDrowstatus_Object=MibTableColumn
apPermitSSIDrowstatus=_ApPermitSSIDrowstatus_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,10,1,2),_ApPermitSSIDrowstatus_Type())
apPermitSSIDrowstatus.setMaxAccess(_H)
if mibBuilder.loadTexts:apPermitSSIDrowstatus.setStatus(_A)
_ApWidsPermitVendorTable_Object=MibTable
apWidsPermitVendorTable=_ApWidsPermitVendorTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,11))
if mibBuilder.loadTexts:apWidsPermitVendorTable.setStatus(_A)
_ApWidsPermitVendorEntry_Object=MibTableRow
apWidsPermitVendorEntry=_ApWidsPermitVendorEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,11,1))
apWidsPermitVendorEntry.setIndexNames((0,_D,_AQ))
if mibBuilder.loadTexts:apWidsPermitVendorEntry.setStatus(_A)
_ApCounterVendor_Type=MacAddress
_ApCounterVendor_Object=MibTableColumn
apCounterVendor=_ApCounterVendor_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,11,1,1),_ApCounterVendor_Type())
apCounterVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:apCounterVendor.setStatus(_A)
_ApPermitVendorrowstatus_Type=RowStatus
_ApPermitVendorrowstatus_Object=MibTableColumn
apPermitVendorrowstatus=_ApPermitVendorrowstatus_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,11,1,2),_ApPermitVendorrowstatus_Type())
apPermitVendorrowstatus.setMaxAccess(_H)
if mibBuilder.loadTexts:apPermitVendorrowstatus.setStatus(_A)
_ApWidsStaticAttackTable_Object=MibTable
apWidsStaticAttackTable=_ApWidsStaticAttackTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,12))
if mibBuilder.loadTexts:apWidsStaticAttackTable.setStatus(_A)
_ApWidsStaticAttackEntry_Object=MibTableRow
apWidsStaticAttackEntry=_ApWidsStaticAttackEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,12,1))
apWidsStaticAttackEntry.setIndexNames((0,_D,_AR))
if mibBuilder.loadTexts:apWidsStaticAttackEntry.setStatus(_A)
_ApStaticAttackMac_Type=MacAddress
_ApStaticAttackMac_Object=MibTableColumn
apStaticAttackMac=_ApStaticAttackMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,12,1,1),_ApStaticAttackMac_Type())
apStaticAttackMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaticAttackMac.setStatus(_A)
_ApStaticAttackrowstatus_Type=RowStatus
_ApStaticAttackrowstatus_Object=MibTableColumn
apStaticAttackrowstatus=_ApStaticAttackrowstatus_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,12,1,2),_ApStaticAttackrowstatus_Type())
apStaticAttackrowstatus.setMaxAccess(_H)
if mibBuilder.loadTexts:apStaticAttackrowstatus.setStatus(_A)
_ApWidsNeighborApInfoTable_Object=MibTable
apWidsNeighborApInfoTable=_ApWidsNeighborApInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,13))
if mibBuilder.loadTexts:apWidsNeighborApInfoTable.setStatus(_A)
_ApWidsNeighborApInfoEntry_Object=MibTableRow
apWidsNeighborApInfoEntry=_ApWidsNeighborApInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,13,1))
apWidsNeighborApInfoEntry.setIndexNames((0,_D,_AS))
if mibBuilder.loadTexts:apWidsNeighborApInfoEntry.setStatus(_A)
_NeighborApMac_Type=MacAddress
_NeighborApMac_Object=MibTableColumn
neighborApMac=_NeighborApMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,13,1,1),_NeighborApMac_Type())
neighborApMac.setMaxAccess(_B)
if mibBuilder.loadTexts:neighborApMac.setStatus(_A)
_NeighborApSSID_Type=DisplayString
_NeighborApSSID_Object=MibTableColumn
neighborApSSID=_NeighborApSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,13,1,2),_NeighborApSSID_Type())
neighborApSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:neighborApSSID.setStatus(_A)
_NeighborApRSSI_Type=Integer32
_NeighborApRSSI_Object=MibTableColumn
neighborApRSSI=_NeighborApRSSI_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,13,1,3),_NeighborApRSSI_Type())
neighborApRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:neighborApRSSI.setStatus(_A)
_NeighborApChannel_Type=Integer32
_NeighborApChannel_Object=MibTableColumn
neighborApChannel=_NeighborApChannel_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,13,1,4),_NeighborApChannel_Type())
neighborApChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:neighborApChannel.setStatus(_A)
_NeighborApInControl_Type=Integer32
_NeighborApInControl_Object=MibTableColumn
neighborApInControl=_NeighborApInControl_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,13,1,5),_NeighborApInControl_Type())
neighborApInControl.setMaxAccess(_B)
if mibBuilder.loadTexts:neighborApInControl.setStatus(_A)
_ApWidsClearIlleglApListFlag_Type=TruthValue
_ApWidsClearIlleglApListFlag_Object=MibScalar
apWidsClearIlleglApListFlag=_ApWidsClearIlleglApListFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,14),_ApWidsClearIlleglApListFlag_Type())
apWidsClearIlleglApListFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:apWidsClearIlleglApListFlag.setStatus(_A)
_ApWidsFloodInterval_Type=Unsigned32
_ApWidsFloodInterval_Object=MibScalar
apWidsFloodInterval=_ApWidsFloodInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,15),_ApWidsFloodInterval_Type())
apWidsFloodInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:apWidsFloodInterval.setStatus(_A)
_ApWidsBlackListThreshold_Type=Unsigned32
_ApWidsBlackListThreshold_Object=MibScalar
apWidsBlackListThreshold=_ApWidsBlackListThreshold_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,16),_ApWidsBlackListThreshold_Type())
apWidsBlackListThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:apWidsBlackListThreshold.setStatus(_A)
_ApWidsBlackListDuration_Type=Unsigned32
_ApWidsBlackListDuration_Object=MibScalar
apWidsBlackListDuration=_ApWidsBlackListDuration_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,17),_ApWidsBlackListDuration_Type())
apWidsBlackListDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:apWidsBlackListDuration.setStatus(_A)
_ApWidsFloodDetectOnOff_Type=Integer32
_ApWidsFloodDetectOnOff_Object=MibScalar
apWidsFloodDetectOnOff=_ApWidsFloodDetectOnOff_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,18),_ApWidsFloodDetectOnOff_Type())
apWidsFloodDetectOnOff.setMaxAccess(_C)
if mibBuilder.loadTexts:apWidsFloodDetectOnOff.setStatus(_A)
_ApWidsCounterRssiThreshold_Type=Integer32
_ApWidsCounterRssiThreshold_Object=MibScalar
apWidsCounterRssiThreshold=_ApWidsCounterRssiThreshold_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,19),_ApWidsCounterRssiThreshold_Type())
apWidsCounterRssiThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:apWidsCounterRssiThreshold.setStatus(_A)
_ApWidsBlackSSIDTable_Object=MibTable
apWidsBlackSSIDTable=_ApWidsBlackSSIDTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,20))
if mibBuilder.loadTexts:apWidsBlackSSIDTable.setStatus(_A)
_ApWidsBlackSSIDEntry_Object=MibTableRow
apWidsBlackSSIDEntry=_ApWidsBlackSSIDEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,20,1))
apWidsBlackSSIDEntry.setIndexNames((0,_D,_AT))
if mibBuilder.loadTexts:apWidsBlackSSIDEntry.setStatus(_A)
_ApBlackSSID_Type=DisplayString
_ApBlackSSID_Object=MibTableColumn
apBlackSSID=_ApBlackSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,20,1,1),_ApBlackSSID_Type())
apBlackSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:apBlackSSID.setStatus(_A)
_ApBlackSSIDrowstatus_Type=RowStatus
_ApBlackSSIDrowstatus_Object=MibTableColumn
apBlackSSIDrowstatus=_ApBlackSSIDrowstatus_Object((1,3,6,1,4,1,27514,1,1,10,2,81,14,20,1,2),_ApBlackSSIDrowstatus_Type())
apBlackSSIDrowstatus.setMaxAccess(_H)
if mibBuilder.loadTexts:apBlackSSIDrowstatus.setStatus(_A)
_ApConfigInfoObjects_ObjectIdentity=ObjectIdentity
apConfigInfoObjects=_ApConfigInfoObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,15))
_ApConfigInfoTable_Object=MibTable
apConfigInfoTable=_ApConfigInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,15,1))
if mibBuilder.loadTexts:apConfigInfoTable.setStatus(_A)
_ApConfigInfoEntry_Object=MibTableRow
apConfigInfoEntry=_ApConfigInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,15,1,1))
apConfigInfoEntry.setIndexNames((0,_D,_AU))
if mibBuilder.loadTexts:apConfigInfoEntry.setStatus(_A)
_ApConfigInfoMac_Type=MacAddress
_ApConfigInfoMac_Object=MibTableColumn
apConfigInfoMac=_ApConfigInfoMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,15,1,1,1),_ApConfigInfoMac_Type())
apConfigInfoMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apConfigInfoMac.setStatus(_A)
_ApSpectralSwitch_Type=Integer32
_ApSpectralSwitch_Object=MibTableColumn
apSpectralSwitch=_ApSpectralSwitch_Object((1,3,6,1,4,1,27514,1,1,10,2,81,15,1,1,2),_ApSpectralSwitch_Type())
apSpectralSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:apSpectralSwitch.setStatus(_A)
_ApSpectralSupport_Type=Integer32
_ApSpectralSupport_Object=MibTableColumn
apSpectralSupport=_ApSpectralSupport_Object((1,3,6,1,4,1,27514,1,1,10,2,81,15,1,1,3),_ApSpectralSupport_Type())
apSpectralSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:apSpectralSupport.setStatus(_A)
_ApSmartAntSupport_Type=Integer32
_ApSmartAntSupport_Object=MibTableColumn
apSmartAntSupport=_ApSmartAntSupport_Object((1,3,6,1,4,1,27514,1,1,10,2,81,15,1,1,4),_ApSmartAntSupport_Type())
apSmartAntSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:apSmartAntSupport.setStatus(_A)
_ApSmartDisSupport_Type=Integer32
_ApSmartDisSupport_Object=MibTableColumn
apSmartDisSupport=_ApSmartDisSupport_Object((1,3,6,1,4,1,27514,1,1,10,2,81,15,1,1,5),_ApSmartDisSupport_Type())
apSmartDisSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:apSmartDisSupport.setStatus(_A)
_ApAntdetectSupport_Type=Integer32
_ApAntdetectSupport_Object=MibTableColumn
apAntdetectSupport=_ApAntdetectSupport_Object((1,3,6,1,4,1,27514,1,1,10,2,81,15,1,1,6),_ApAntdetectSupport_Type())
apAntdetectSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:apAntdetectSupport.setStatus(_A)
_ApAntdetectEnable_Type=Integer32
_ApAntdetectEnable_Object=MibTableColumn
apAntdetectEnable=_ApAntdetectEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,15,1,1,7),_ApAntdetectEnable_Type())
apAntdetectEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:apAntdetectEnable.setStatus(_A)
_ApAntdetectInterval_Type=Integer32
_ApAntdetectInterval_Object=MibTableColumn
apAntdetectInterval=_ApAntdetectInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,81,15,1,1,8),_ApAntdetectInterval_Type())
apAntdetectInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:apAntdetectInterval.setStatus(_A)
_ApAntdetectState_Type=Integer32
_ApAntdetectState_Object=MibTableColumn
apAntdetectState=_ApAntdetectState_Object((1,3,6,1,4,1,27514,1,1,10,2,81,15,1,1,9),_ApAntdetectState_Type())
apAntdetectState.setMaxAccess(_B)
if mibBuilder.loadTexts:apAntdetectState.setStatus(_A)
_ApAntDetectObjects_ObjectIdentity=ObjectIdentity
apAntDetectObjects=_ApAntDetectObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,81,16))
_ApAntDetectTable_Object=MibTable
apAntDetectTable=_ApAntDetectTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,16,1))
if mibBuilder.loadTexts:apAntDetectTable.setStatus(_A)
_ApAntDetectEntry_Object=MibTableRow
apAntDetectEntry=_ApAntDetectEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,16,1,1))
apAntDetectEntry.setIndexNames((0,_D,_AV),(0,_D,_AW))
if mibBuilder.loadTexts:apAntDetectEntry.setStatus(_A)
_ApAntDetectAPMac_Type=MacAddress
_ApAntDetectAPMac_Object=MibTableColumn
apAntDetectAPMac=_ApAntDetectAPMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,16,1,1,1),_ApAntDetectAPMac_Type())
apAntDetectAPMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apAntDetectAPMac.setStatus(_A)
_ApAntDetectAntIndex_Type=Integer32
_ApAntDetectAntIndex_Object=MibTableColumn
apAntDetectAntIndex=_ApAntDetectAntIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,81,16,1,1,2),_ApAntDetectAntIndex_Type())
apAntDetectAntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:apAntDetectAntIndex.setStatus(_A)
_ApAntDetectDesc_Type=DisplayString
_ApAntDetectDesc_Object=MibTableColumn
apAntDetectDesc=_ApAntDetectDesc_Object((1,3,6,1,4,1,27514,1,1,10,2,81,16,1,1,3),_ApAntDetectDesc_Type())
apAntDetectDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:apAntDetectDesc.setStatus(_A)
_ApAntDetectRadioId_Type=DisplayString
_ApAntDetectRadioId_Object=MibTableColumn
apAntDetectRadioId=_ApAntDetectRadioId_Object((1,3,6,1,4,1,27514,1,1,10,2,81,16,1,1,4),_ApAntDetectRadioId_Type())
apAntDetectRadioId.setMaxAccess(_B)
if mibBuilder.loadTexts:apAntDetectRadioId.setStatus(_A)
_ApAntDetectStatus_Type=Integer32
_ApAntDetectStatus_Object=MibTableColumn
apAntDetectStatus=_ApAntDetectStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,81,16,1,1,5),_ApAntDetectStatus_Type())
apAntDetectStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:apAntDetectStatus.setStatus(_A)
_ApAntDetectCfgTable_Object=MibTable
apAntDetectCfgTable=_ApAntDetectCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,81,16,2))
if mibBuilder.loadTexts:apAntDetectCfgTable.setStatus(_A)
_ApAntDetectCfgEntry_Object=MibTableRow
apAntDetectCfgEntry=_ApAntDetectCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,81,16,2,1))
apAntDetectCfgEntry.setIndexNames((0,_D,_AX))
if mibBuilder.loadTexts:apAntDetectCfgEntry.setStatus(_A)
_ApAntDetectCfgAPMac_Type=MacAddress
_ApAntDetectCfgAPMac_Object=MibTableColumn
apAntDetectCfgAPMac=_ApAntDetectCfgAPMac_Object((1,3,6,1,4,1,27514,1,1,10,2,81,16,2,1,1),_ApAntDetectCfgAPMac_Type())
apAntDetectCfgAPMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apAntDetectCfgAPMac.setStatus(_A)
_ApAntDetectCfgSupport_Type=Integer32
_ApAntDetectCfgSupport_Object=MibTableColumn
apAntDetectCfgSupport=_ApAntDetectCfgSupport_Object((1,3,6,1,4,1,27514,1,1,10,2,81,16,2,1,2),_ApAntDetectCfgSupport_Type())
apAntDetectCfgSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:apAntDetectCfgSupport.setStatus(_A)
_ApAntDetectCfgSwitch_Type=Integer32
_ApAntDetectCfgSwitch_Object=MibTableColumn
apAntDetectCfgSwitch=_ApAntDetectCfgSwitch_Object((1,3,6,1,4,1,27514,1,1,10,2,81,16,2,1,3),_ApAntDetectCfgSwitch_Type())
apAntDetectCfgSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:apAntDetectCfgSwitch.setStatus(_A)
apCPUusageTooHighTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,1,1))
if mibBuilder.loadTexts:apCPUusageTooHighTrap.setStatus(_A)
apCPUusageTooHighRecovTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,1,2))
if mibBuilder.loadTexts:apCPUusageTooHighRecovTrap.setStatus(_A)
apMemUsageTooHighTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,1,3))
if mibBuilder.loadTexts:apMemUsageTooHighTrap.setStatus(_A)
apMemUsageTooHighRecovTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,1,4))
if mibBuilder.loadTexts:apMemUsageTooHighRecovTrap.setStatus(_A)
aPOfflineTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,1,5))
if mibBuilder.loadTexts:aPOfflineTrap.setStatus(_A)
aPOnlineTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,1,6))
if mibBuilder.loadTexts:aPOnlineTrap.setStatus(_A)
aPMtWorkModeChgTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,1,7))
aPMtWorkModeChgTrap.setObjects(*((_D,'apAPMac'),(_D,_AY),(_D,_AZ)))
if mibBuilder.loadTexts:aPMtWorkModeChgTrap.setStatus(_A)
apSoftwareUpdateFailTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,1,8))
apSoftwareUpdateFailTrap.setObjects(*((_D,_Aa),(_D,_Ab)))
if mibBuilder.loadTexts:apSoftwareUpdateFailTrap.setStatus(_A)
apSSIDCyperConflictTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,1,9))
apSSIDCyperConflictTrap.setObjects(*((_E,_F),(_D,_I),(_D,_Ac),(_D,_Ad),(_D,_Ae)))
if mibBuilder.loadTexts:apSSIDCyperConflictTrap.setStatus(_A)
aPCoInterfDetectedTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,1))
aPCoInterfDetectedTrap.setObjects(*((_E,_F),(_D,_I),(_D,_O),(_D,_V)))
if mibBuilder.loadTexts:aPCoInterfDetectedTrap.setStatus(_A)
aPCoInterfClearTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,2))
aPCoInterfClearTrap.setObjects(*((_E,_F),(_D,_I),(_D,_O),(_D,_V)))
if mibBuilder.loadTexts:aPCoInterfClearTrap.setStatus(_A)
aPNerborInterfDetectedTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,3))
aPNerborInterfDetectedTrap.setObjects(*((_E,_F),(_D,_I),(_D,_O),(_D,_V),(_D,_f)))
if mibBuilder.loadTexts:aPNerborInterfDetectedTrap.setStatus(_A)
aPNeiborInterfClearTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,4))
aPNeiborInterfClearTrap.setObjects(*((_E,_F),(_D,_I),(_D,_O),(_D,_V),(_D,_f)))
if mibBuilder.loadTexts:aPNeiborInterfClearTrap.setStatus(_A)
staInterfDetectedTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,5))
staInterfDetectedTrap.setObjects(*((_E,_F),(_D,_I),(_D,_O),(_D,_g)))
if mibBuilder.loadTexts:staInterfDetectedTrap.setStatus(_A)
staInterfClearTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,6))
staInterfClearTrap.setObjects(*((_E,_F),(_D,_I),(_D,_O),(_D,_g)))
if mibBuilder.loadTexts:staInterfClearTrap.setStatus(_A)
otherDeviceInterfDetectedTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,7))
otherDeviceInterfDetectedTrap.setObjects(*((_E,_F),(_D,_I),(_D,_O)))
if mibBuilder.loadTexts:otherDeviceInterfDetectedTrap.setStatus(_A)
otherDevInterfClearTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,8))
otherDevInterfClearTrap.setObjects(*((_E,_F),(_D,_I),(_D,_O)))
if mibBuilder.loadTexts:otherDevInterfClearTrap.setStatus(_A)
apRadioDownTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,9))
apRadioDownTrap.setObjects(*((_E,_F),(_D,_I),(_D,_Z)))
if mibBuilder.loadTexts:apRadioDownTrap.setStatus(_A)
apRadioDownRecovTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,10))
apRadioDownRecovTrap.setObjects(*((_E,_F),(_D,_I),(_D,_Z)))
if mibBuilder.loadTexts:apRadioDownRecovTrap.setStatus(_A)
aPStaFullTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,11))
aPStaFullTrap.setObjects(*((_E,_F),(_D,_h),(_D,_a)))
if mibBuilder.loadTexts:aPStaFullTrap.setStatus(_A)
aPStaFullRecoverTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,12))
aPStaFullRecoverTrap.setObjects(*((_E,_F),(_D,_h),(_D,_a)))
if mibBuilder.loadTexts:aPStaFullRecoverTrap.setStatus(_A)
aPMtRdoChanlChgTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,13))
aPMtRdoChanlChgTrap.setObjects(*((_E,_F),(_D,_Af),(_D,_Ag),(_D,_Ah)))
if mibBuilder.loadTexts:aPMtRdoChanlChgTrap.setStatus(_A)
apSpeciusDeviceDetectTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,14))
apSpeciusDeviceDetectTrap.setObjects(*((_E,_F),(_D,_Ai)))
if mibBuilder.loadTexts:apSpeciusDeviceDetectTrap.setStatus(_A)
apRadioRxPackagesTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,15))
apRadioRxPackagesTrap.setObjects(*((_E,_F),(_D,_i),(_D,_Aj)))
if mibBuilder.loadTexts:apRadioRxPackagesTrap.setStatus(_A)
apCPUUsageTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,16))
apCPUUsageTrap.setObjects(*((_E,_F),(_D,_Ak)))
if mibBuilder.loadTexts:apCPUUsageTrap.setStatus(_A)
apSTARefusedRSSITrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,17))
apSTARefusedRSSITrap.setObjects(*((_E,_F),(_D,_M),(_D,'apRSSI')))
if mibBuilder.loadTexts:apSTARefusedRSSITrap.setStatus(_A)
apSTARefusedRatesetTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,18))
apSTARefusedRatesetTrap.setObjects(*((_E,_F),(_D,_M)))
if mibBuilder.loadTexts:apSTARefusedRatesetTrap.setStatus(_A)
apFindAttackTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,19))
apFindAttackTrap.setObjects(*((_E,_F),(_D,_Al)))
if mibBuilder.loadTexts:apFindAttackTrap.setStatus(_A)
wlanSecurityChgTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,20))
wlanSecurityChgTrap.setObjects(*((_D,'apWlanId'),(_D,_Am),(_D,_An),(_D,_Ao)))
if mibBuilder.loadTexts:wlanSecurityChgTrap.setStatus(_A)
apRadioFailureTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,21))
apRadioFailureTrap.setObjects(*((_E,_F),(_D,_I),(_D,_Z)))
if mibBuilder.loadTexts:apRadioFailureTrap.setStatus(_A)
apIllegalApTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,22))
apIllegalApTrap.setObjects(*((_D,_j),(_D,_k),(_D,_l),(_D,_m),(_D,_n),(_D,_o),(_D,_p)))
if mibBuilder.loadTexts:apIllegalApTrap.setStatus(_A)
apIllegalApRecoverTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,23))
apIllegalApRecoverTrap.setObjects(*((_D,_j),(_D,_k),(_D,_l),(_D,_m),(_D,_n),(_D,_o),(_D,_p)))
if mibBuilder.loadTexts:apIllegalApRecoverTrap.setStatus(_A)
apStaAssocFailTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,24))
apStaAssocFailTrap.setObjects(*((_E,_F),(_D,_M),(_D,_i),(_D,_Ap),(_D,_Aq),(_D,_Ar),(_D,_P),(_D,_As),(_D,_O)))
if mibBuilder.loadTexts:apStaAssocFailTrap.setStatus(_A)
apSpectralInfoTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,25))
apSpectralInfoTrap.setObjects(*((_D,_At),(_D,_Au),(_D,_Av),(_D,_Aw)))
if mibBuilder.loadTexts:apSpectralInfoTrap.setStatus(_A)
apCounterMeasureTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,2,26))
apCounterMeasureTrap.setObjects(*((_D,_Ax),(_D,_Ay)))
if mibBuilder.loadTexts:apCounterMeasureTrap.setStatus(_A)
apStaAuthErrorTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,3,1))
apStaAuthErrorTrap.setObjects(*((_E,_F),(_D,_I),(_D,_Q),(_D,_P),(_D,_M),(_D,_Az),(_D,_A_)))
if mibBuilder.loadTexts:apStaAuthErrorTrap.setStatus(_A)
apStAssociationFailTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,3,2))
apStAssociationFailTrap.setObjects(*((_E,_F),(_D,_I),(_D,_Q),(_D,_P),(_D,_M),(_D,_a)))
if mibBuilder.loadTexts:apStAssociationFailTrap.setStatus(_A)
userwithInvalidCerficationInbreakNetwork=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,4,1))
userwithInvalidCerficationInbreakNetwork.setObjects(*((_E,_F),(_D,_I),(_D,_Q),(_D,_P),(_D,_M)))
if mibBuilder.loadTexts:userwithInvalidCerficationInbreakNetwork.setStatus(_A)
stationRepititiveAttack=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,4,2))
stationRepititiveAttack.setObjects(*((_E,_F),(_D,_I),(_D,_Q),(_D,_P),(_D,_M)))
if mibBuilder.loadTexts:stationRepititiveAttack.setStatus(_A)
tamperAttack=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,4,3))
tamperAttack.setObjects(*((_E,_F),(_D,_I),(_D,_Q),(_D,_P),(_D,_M)))
if mibBuilder.loadTexts:tamperAttack.setStatus(_A)
lowSafeLevelAttack=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,4,4))
lowSafeLevelAttack.setObjects(*((_E,_F),(_D,_I),(_D,_Q),(_D,_P),(_D,_M)))
if mibBuilder.loadTexts:lowSafeLevelAttack.setStatus(_A)
addressRedirectionAttack=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,81,0,4,5))
addressRedirectionAttack.setObjects(*((_E,_F),(_D,_I),(_D,_Q),(_D,_P),(_D,_M)))
if mibBuilder.loadTexts:addressRedirectionAttack.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'qtechFitApMibModule':qtechFitApMibModule,'apQtechAlarmTraps':apQtechAlarmTraps,'apSystemAlarmTraps':apSystemAlarmTraps,'apCPUusageTooHighTrap':apCPUusageTooHighTrap,'apCPUusageTooHighRecovTrap':apCPUusageTooHighRecovTrap,'apMemUsageTooHighTrap':apMemUsageTooHighTrap,'apMemUsageTooHighRecovTrap':apMemUsageTooHighRecovTrap,'aPOfflineTrap':aPOfflineTrap,'aPOnlineTrap':aPOnlineTrap,'aPMtWorkModeChgTrap':aPMtWorkModeChgTrap,'apSoftwareUpdateFailTrap':apSoftwareUpdateFailTrap,'apSSIDCyperConflictTrap':apSSIDCyperConflictTrap,'apWirelessAlarmTraps':apWirelessAlarmTraps,'aPCoInterfDetectedTrap':aPCoInterfDetectedTrap,'aPCoInterfClearTrap':aPCoInterfClearTrap,'aPNerborInterfDetectedTrap':aPNerborInterfDetectedTrap,'aPNeiborInterfClearTrap':aPNeiborInterfClearTrap,'staInterfDetectedTrap':staInterfDetectedTrap,'staInterfClearTrap':staInterfClearTrap,'otherDeviceInterfDetectedTrap':otherDeviceInterfDetectedTrap,'otherDevInterfClearTrap':otherDevInterfClearTrap,'apRadioDownTrap':apRadioDownTrap,'apRadioDownRecovTrap':apRadioDownRecovTrap,'aPStaFullTrap':aPStaFullTrap,'aPStaFullRecoverTrap':aPStaFullRecoverTrap,'aPMtRdoChanlChgTrap':aPMtRdoChanlChgTrap,'apSpeciusDeviceDetectTrap':apSpeciusDeviceDetectTrap,'apRadioRxPackagesTrap':apRadioRxPackagesTrap,'apCPUUsageTrap':apCPUUsageTrap,'apSTARefusedRSSITrap':apSTARefusedRSSITrap,'apSTARefusedRatesetTrap':apSTARefusedRatesetTrap,'apFindAttackTrap':apFindAttackTrap,'wlanSecurityChgTrap':wlanSecurityChgTrap,'apRadioFailureTrap':apRadioFailureTrap,'apIllegalApTrap':apIllegalApTrap,'apIllegalApRecoverTrap':apIllegalApRecoverTrap,'apStaAssocFailTrap':apStaAssocFailTrap,'apSpectralInfoTrap':apSpectralInfoTrap,'apCounterMeasureTrap':apCounterMeasureTrap,'apStaAnnounceTraps':apStaAnnounceTraps,'apStaAuthErrorTrap':apStaAuthErrorTrap,'apStAssociationFailTrap':apStAssociationFailTrap,'apWAPISecurityAlarmTraps':apWAPISecurityAlarmTraps,'userwithInvalidCerficationInbreakNetwork':userwithInvalidCerficationInbreakNetwork,'stationRepititiveAttack':stationRepititiveAttack,'tamperAttack':tamperAttack,'lowSafeLevelAttack':lowSafeLevelAttack,'addressRedirectionAttack':addressRedirectionAttack,'apSystemInfoConfigObjects':apSystemInfoConfigObjects,'apGeneralInfoConfigObjects':apGeneralInfoConfigObjects,'apGeneralInfoConfigTable':apGeneralInfoConfigTable,'apGeneralInfoConfigTableEntry':apGeneralInfoConfigTableEntry,'apSysNEId':apSysNEId,'apSysName':apSysName,'apStatWindowTime':apStatWindowTime,'apSampleTime':apSampleTime,'apRtCollectOnoff':apRtCollectOnoff,'apSysRestart':apSysRestart,'apSysReset':apSysReset,'apGeneralInfoReadObjects':apGeneralInfoReadObjects,'apGeneralCfgInfoReadTable':apGeneralCfgInfoReadTable,'apGeneralCfgInfoReadTableEntry':apGeneralCfgInfoReadTableEntry,'apSysDescr':apSysDescr,'apSysManufacture':apSysManufacture,'apSerialNumber':apSerialNumber,'apSysModel':apSysModel,'apSysUpTime':apSysUpTime,'apSysOnlineTime':apSysOnlineTime,'apSysIPAddress':apSysIPAddress,'apSysIPNetMask':apSysIPNetMask,'apSysGateWayAddr':apSysGateWayAddr,'apSysMacAddrConnectToAC':apSysMacAddrConnectToAC,'apSoftwareName':apSoftwareName,'apSoftwareVersion':apSoftwareVersion,'apSoftwareVendor':apSoftwareVendor,'apCPUType':apCPUType,'apMemoryType':apMemoryType,'apMemorySize':apMemorySize,'apFlashSize':apFlashSize,'apGeneralStatusCFGObjects':apGeneralStatusCFGObjects,'apGeneralStatusCFGTable':apGeneralStatusCFGTable,'apGeneralStatusCFGTableEntry':apGeneralStatusCFGTableEntry,'apAPName':apAPName,'apACAssociateStatus':apACAssociateStatus,'apMonitorMode':apMonitorMode,_s:apAssoStatusAPMac,'apACHbAssocStatus':apACHbAssocStatus,'apScanType':apScanType,'apInterfaceConfigObjects':apInterfaceConfigObjects,'apInterfaceNumberObjects':apInterfaceNumberObjects,'apInterfaceNumberTable':apInterfaceNumberTable,'apInterfaceNumberTableEntry':apInterfaceNumberTableEntry,'apIfNumber':apIfNumber,'apBSSIDNum':apBSSIDNum,'apInterfaceRGMIIcfgObjects':apInterfaceRGMIIcfgObjects,'apInterfaceRGMIIconfigTable':apInterfaceRGMIIconfigTable,'apInterfaceRGMIIconfigTableEntry':apInterfaceRGMIIconfigTableEntry,_v:apIfLocalRGMIINum,'apIfRGMIIDescr':apIfRGMIIDescr,'apIfRGMIIType':apIfRGMIIType,'apIfRGMIIMtu':apIfRGMIIMtu,'apIfRGMIISpeed':apIfRGMIISpeed,'apIfRGMIIPhysAddress':apIfRGMIIPhysAddress,'apIfRGMIIAdminStatusEnable':apIfRGMIIAdminStatusEnable,'apIfRGMIIOperStatus':apIfRGMIIOperStatus,'apIfRGMIILastChange':apIfRGMIILastChange,'apInterfaceWirelesscfgObjects':apInterfaceWirelesscfgObjects,'apInterfaceWirelessconfigTable':apInterfaceWirelessconfigTable,'apInterfaceWirelessconfigTableEntry':apInterfaceWirelessconfigTableEntry,'apIfWireDescr':apIfWireDescr,'apIfWireType':apIfWireType,'apIfWireMtu':apIfWireMtu,'apIfWireSpeed':apIfWireSpeed,'apIfWirePhysAddress':apIfWirePhysAddress,'apIfWireAdminStatusEnable':apIfWireAdminStatusEnable,'apIfWireOperStatus':apIfWireOperStatus,'apIfWireLastChange':apIfWireLastChange,'apIfWireChannelAutoSelectEnable':apIfWireChannelAutoSelectEnable,'apIfWireRadioChannelConfig':apIfWireRadioChannelConfig,'apIfWireRadioChannelUsing':apIfWireRadioChannelUsing,'apIfWireCurrRadioModeSupport':apIfWireCurrRadioModeSupport,'apIfWireRadioModeConfig':apIfWireRadioModeConfig,'apIfWireTransmitSpeedConfig':apIfWireTransmitSpeedConfig,'apIfWireMaxTxPwrLvl':apIfWireMaxTxPwrLvl,'apIfWirePwrAttRange':apIfWirePwrAttRange,'apIfWirePwrAttValue':apIfWirePwrAttValue,'apIfWireAntennaGain':apIfWireAntennaGain,'apIfWirePowerMgmtEnable':apIfWirePowerMgmtEnable,'apTxPwr':apTxPwr,'apIfWireMaxStationNumPermitted':apIfWireMaxStationNumPermitted,'apIfWireAMPDUEnabled':apIfWireAMPDUEnabled,'apIfWireBWMode':apIfWireBWMode,'apIfWireShortGIEnabled':apIfWireShortGIEnabled,'apIfWireIs11nOnly':apIfWireIs11nOnly,'apIfWireBeaconIntvl':apIfWireBeaconIntvl,'apIfWireDtimIntvl':apIfWireDtimIntvl,'apIfWireRtsThreshold':apIfWireRtsThreshold,'apIfWireFragThreshlod':apIfWireFragThreshlod,'apIfWirePreambleLen':apIfWirePreambleLen,'apAntennaReceiveMask':apAntennaReceiveMask,'apAntennaTransmitMask':apAntennaTransmitMask,'apIfWireAMSDUEnabled':apIfWireAMSDUEnabled,'apIfwireMcsSuppIndex':apIfwireMcsSuppIndex,'apIfwireMcsMandIndex':apIfwireMcsMandIndex,'apIfwire11nSuppEnable':apIfwire11nSuppEnable,'apShtRetryThld':apShtRetryThld,'apLongRetryThld':apLongRetryThld,'apIfWireResponseRssi':apIfWireResponseRssi,'apIfWireMaxStationLimit':apIfWireMaxStationLimit,'apIfWireLinkscan':apIfWireLinkscan,'apSSIDConfigObjects':apSSIDConfigObjects,'apSSIDListCreateTable':apSSIDListCreateTable,'apSSIDListCreateTableEntry':apSSIDListCreateTableEntry,_x:apSSIDAPMac,_y:apSSIDRadioId,'apSSIDListName':apSSIDListName,'apListBSSIDAddr':apListBSSIDAddr,'apSSIDListStatus':apSSIDListStatus,'apSSIDConfigTable':apSSIDConfigTable,'apSSIDConfigTableEntry':apSSIDConfigTableEntry,'apSSIDName':apSSIDName,'apSSIDEnabled':apSSIDEnabled,'apSSIDHidden':apSSIDHidden,'apStaIsolate':apStaIsolate,'apDot11Auth':apDot11Auth,'apsecurityMode':apsecurityMode,'apAuthenMode':apAuthenMode,'apSecurityCiphers':apSecurityCiphers,'apVlanId':apVlanId,'apVlanIpAddr':apVlanIpAddr,'apMaxSimultUsers':apMaxSimultUsers,'apStaUplinkMaxRate':apStaUplinkMaxRate,'apStaDwlinkMaxRate':apStaDwlinkMaxRate,'apSSIDCfgStatus':apSSIDCfgStatus,'apSecurityConfigObjects':apSecurityConfigObjects,'apSecurityConfigTable':apSecurityConfigTable,'apSecurityConfigTableEntry':apSecurityConfigTableEntry,'apWEPCipherKeyIndex':apWEPCipherKeyIndex,'apWEPCipherKeyValue':apWEPCipherKeyValue,'apWEPCipherKeyCharType':apWEPCipherKeyCharType,'apPSKCipherKeyValue':apPSKCipherKeyValue,'apPSKCipherKeyCharType':apPSKCipherKeyCharType,'apWAPIAuthModeEnable':apWAPIAuthModeEnable,'apWAPIASIPAddress':apWAPIASIPAddress,'apWAPIIsInstalledCer':apWAPIIsInstalledCer,'apWAPIExternInfoConfigObjects':apWAPIExternInfoConfigObjects,'apWAPIExternInfoConfigTable':apWAPIExternInfoConfigTable,'apWAPIExternInfoConfigTableEntry':apWAPIExternInfoConfigTableEntry,'apWAPIConfigVersion':apWAPIConfigVersion,'apWAPIControlledAuthControl':apWAPIControlledAuthControl,'apWAPIControlledPortControl':apWAPIControlledPortControl,'apWAPIOptionImplemented':apWAPIOptionImplemented,'apWAPIPreauthenticationImplemented':apWAPIPreauthenticationImplemented,'apWAPIEnabled':apWAPIEnabled,'apWAPIPreauthEnabled':apWAPIPreauthEnabled,'apWAPIUnicastKeysSupported':apWAPIUnicastKeysSupported,'apWAPIUnicastRekeyMethod':apWAPIUnicastRekeyMethod,'apWAPIUnicastRekeyTime':apWAPIUnicastRekeyTime,'apWAPIUnicastRekeyPackets':apWAPIUnicastRekeyPackets,'apWAPIMulticastCipher':apWAPIMulticastCipher,'apWAPIMulticastRekeyMethod':apWAPIMulticastRekeyMethod,'apWAPIMulticastRekeyTime':apWAPIMulticastRekeyTime,'apWAPIMulticastRekeyPackets':apWAPIMulticastRekeyPackets,'apWAPIMulticastRekeyStrict':apWAPIMulticastRekeyStrict,'apWAPIPSKValue':apWAPIPSKValue,'apWAPIPSKPassPhrase':apWAPIPSKPassPhrase,'apWAPICertificateUpdateCount':apWAPICertificateUpdateCount,'apWAPIMulticastUpdateCount':apWAPIMulticastUpdateCount,'apWAPIUnicastUpdateCount':apWAPIUnicastUpdateCount,'apWAPIMulticastCipherSize':apWAPIMulticastCipherSize,'apWAPIBKLifetime':apWAPIBKLifetime,'apWAPIBKReauthThreshold':apWAPIBKReauthThreshold,'apWAPISATimeout':apWAPISATimeout,'apWAPIAuthSuiteSelected':apWAPIAuthSuiteSelected,'apWAPIUnicastCipherSelected':apWAPIUnicastCipherSelected,'apWAPIMulticastCipherSelected':apWAPIMulticastCipherSelected,'apWAPIBKIDUsed':apWAPIBKIDUsed,'apWAPIAuthSuiteRequested':apWAPIAuthSuiteRequested,'apWAPIUnicastCipherRequested':apWAPIUnicastCipherRequested,'apWAPIMulticastCipherRequested':apWAPIMulticastCipherRequested,'apWAPIUnicastCipher':apWAPIUnicastCipher,'apWAPIUnicastCipherEnabled':apWAPIUnicastCipherEnabled,'apWAPIUnicastCipherSize':apWAPIUnicastCipherSize,'apWAPIAuthenticationSuite':apWAPIAuthenticationSuite,'apWAPIAuthenticationSuiteEnabled':apWAPIAuthenticationSuiteEnabled,'apWAPIAECertFile':apWAPIAECertFile,'apWAPICACertFile':apWAPICACertFile,'apWAPIASUCertFile':apWAPIASUCertFile,'apStationInfoGetObjects':apStationInfoGetObjects,'apStationInfoGetTable':apStationInfoGetTable,'apStationInfoGetTableEntry':apStationInfoGetTableEntry,'apStaMAC':apStaMAC,'apStaWMMAttr':apStaWMMAttr,'apStaIPAddress':apStaIPAddress,'apStaRadioMode':apStaRadioMode,'apStaRadioChannel':apStaRadioChannel,'apAPTxRates':apAPTxRates,'apStaPowerSaveMode':apStaPowerSaveMode,'apStaVlanId':apStaVlanId,'apStaSSIDName':apStaSSIDName,'apAPId':apAPId,'apStaDot11Auth':apStaDot11Auth,'apsecurity':apsecurity,'apStaAuthenMode':apStaAuthenMode,'apStaSecurityCiphers':apStaSecurityCiphers,'apAPIdMac':apAPIdMac,'apStaMode':apStaMode,'apStaBand':apStaBand,'apStationRefusedAccessTable':apStationRefusedAccessTable,'apStationRefusedAccessTableEntry':apStationRefusedAccessTableEntry,_A6:apRefusedStaMAC,'apFailReason':apFailReason,'apRefusedTime':apRefusedTime,'apRefusedAPMac':apRefusedAPMac,'apStationRadiusInfoTable':apStationRadiusInfoTable,'apStationRadiusInfoTableEntry':apStationRadiusInfoTableEntry,_A7:apUserMacAddress,'apUserIpAddress':apUserIpAddress,'apUserLoginName':apUserLoginName,'apUserLoginTime':apUserLoginTime,'apUserOnlineTime':apUserOnlineTime,'apQOSInfoConfigObjects':apQOSInfoConfigObjects,'apQOSWirelessConfigObjects':apQOSWirelessConfigObjects,'apQOSWirelessConfigTable':apQOSWirelessConfigTable,'apQOSWirelessConfigTableEntry':apQOSWirelessConfigTableEntry,_A8:apWireQoSTrafficClassId,'apWireQosAIFS':apWireQosAIFS,'apWireQoSCWmin':apWireQoSCWmin,'apWireQoSCWmax':apWireQoSCWmax,'apWireQoSTXOPLim':apWireQoSTXOPLim,'apQOSBaseInfoConfigObjects':apQOSBaseInfoConfigObjects,'apQOSBaseInfoConfigTable':apQOSBaseInfoConfigTable,'apQOSBaseInfoConfigTableEntry':apQOSBaseInfoConfigTableEntry,'apBaseQoSTrafficClass':apBaseQoSTrafficClass,'apBaseQoSEnabled':apBaseQoSEnabled,'apBaseQoSBW':apBaseQoSBW,'apBaseQoSResPercent':apBaseQoSResPercent,'apBaseQoSsharedBW':apBaseQoSsharedBW,'apBaseQoSsharedBWPercent':apBaseQoSsharedBWPercent,'apBaseQoSSchedAlgName':apBaseQoSSchedAlgName,'apBaseQoSResPolicyEnabled':apBaseQoSResPolicyEnabled,'apBaseQoSResPolicyName':apBaseQoSResPolicyName,'apBaseQoSBackgroundSvcAvgSpeed':apBaseQoSBackgroundSvcAvgSpeed,'apBaseQoSBackgroundSvcMaxBurst':apBaseQoSBackgroundSvcMaxBurst,'apBaseQoSBackgroundSvcPriority':apBaseQoSBackgroundSvcPriority,'apBaseQoSBackgroundSvcResPriority':apBaseQoSBackgroundSvcResPriority,'apBaseQoSBestEffortSvcAvgSpeed':apBaseQoSBestEffortSvcAvgSpeed,'apBaseQoSBestEffortSvcMaxBurst':apBaseQoSBestEffortSvcMaxBurst,'apBaseQoSBestEffortSvcPriority':apBaseQoSBestEffortSvcPriority,'apBaseQoSBestEffortSvcResPriority':apBaseQoSBestEffortSvcResPriority,'apBaseQoSVoiceSvcAvgSpeed':apBaseQoSVoiceSvcAvgSpeed,'apBaseQoSVoiceSvcMaxBurst':apBaseQoSVoiceSvcMaxBurst,'apBaseQoSVoiceSvcPriority':apBaseQoSVoiceSvcPriority,'apBaseQoSVoiceSvcResPriority':apBaseQoSVoiceSvcResPriority,'apBaseQoSVideoSvcAvgSpeed':apBaseQoSVideoSvcAvgSpeed,'apBaseQoSVideoSvcMaxBurst':apBaseQoSVideoSvcMaxBurst,'apBaseQoSVideoSvcPriority':apBaseQoSVideoSvcPriority,'apBaseQoSVideoSvcResPriority':apBaseQoSVideoSvcResPriority,'apQOSBackgroundCfgObjects':apQOSBackgroundCfgObjects,'apQOSBackgroundCfgTable':apQOSBackgroundCfgTable,'apQOSBackgroundCfgTableEntry':apQOSBackgroundCfgTableEntry,'apQOSBgMaxSvcCnt':apQOSBgMaxSvcCnt,'apQOSBgSvcBW':apQOSBgSvcBW,'apQOSBgSvcBWPercent':apQOSBgSvcBWPercent,'apQOSBgIsUseWREDAlg':apQOSBgIsUseWREDAlg,'apQOSBgIsUseTrafficShaping':apQOSBgIsUseTrafficShaping,'apQOSBestEffortCfgObjects':apQOSBestEffortCfgObjects,'apQOSBestEffortCfgTable':apQOSBestEffortCfgTable,'apQOSBestEffortCfgTableEntry':apQOSBestEffortCfgTableEntry,'apQOSBeMaxSvcCnt':apQOSBeMaxSvcCnt,'apQOSBeSvcBW':apQOSBeSvcBW,'apQOSBeSvcBWPercent':apQOSBeSvcBWPercent,'apQOSBeIsUseWREDAlg':apQOSBeIsUseWREDAlg,'apQOSBeIsUseTrafficShaping':apQOSBeIsUseTrafficShaping,'apQOSVoiceInfoCfgObjects':apQOSVoiceInfoCfgObjects,'apQOSVoiceInfoCfgTable':apQOSVoiceInfoCfgTable,'apQOSVoiceInfoCfgTableEntry':apQOSVoiceInfoCfgTableEntry,'apQOSVoiceMaxSvcCnt':apQOSVoiceMaxSvcCnt,'apQOSVoiceSvcBW':apQOSVoiceSvcBW,'apQOSVoiceSvcBWPercent':apQOSVoiceSvcBWPercent,'apQOSVoiceIsUseStreamBasedQueue':apQOSVoiceIsUseStreamBasedQueue,'apQOSVoiceStreamMaxQueueLen':apQOSVoiceStreamMaxQueueLen,'apQOSVoiceStreamAvgSpeed':apQOSVoiceStreamAvgSpeed,'apQOSVoiceStreamMaxBurst':apQOSVoiceStreamMaxBurst,'apQOSVoiceIsUseWREDAlg':apQOSVoiceIsUseWREDAlg,'apQOSVoiceIsUseTrafficShaping':apQOSVoiceIsUseTrafficShaping,'apQOSVideoInfoCfgObjects':apQOSVideoInfoCfgObjects,'apQOSVideoInfoCfgTable':apQOSVideoInfoCfgTable,'apQOSVideoInfoCfgTableEntry':apQOSVideoInfoCfgTableEntry,'apQOSVideoMaxSvcCnt':apQOSVideoMaxSvcCnt,'apQOSVideoSvcBW':apQOSVideoSvcBW,'apQOSVideoSvcBWPercent':apQOSVideoSvcBWPercent,'apQOSVideoIsUseStreamBasedQueue':apQOSVideoIsUseStreamBasedQueue,'apQOSVideoStreamMaxQueueLen':apQOSVideoStreamMaxQueueLen,'apQOSVideoStreamAvgSpeed':apQOSVideoStreamAvgSpeed,'apQOSVideoStreamMaxBurst':apQOSVideoStreamMaxBurst,'apQOSVideoIsUseWREDAlg':apQOSVideoIsUseWREDAlg,'apQOSVideoIsUseTrafficShaping':apQOSVideoIsUseTrafficShaping,'apQOSWMMConfigObjects':apQOSWMMConfigObjects,'apQOSWMMConfigTable':apQOSWMMConfigTable,'apQOSWMMConfigTableEntry':apQOSWMMConfigTableEntry,'apQOSMode':apQOSMode,'apQOSUpdateSeq':apQOSUpdateSeq,'apQOSSvpAcIndex':apQOSSvpAcIndex,'apQOSUapsd':apQOSUapsd,'apQOSAcIndx1':apQOSAcIndx1,'apQOSAcIndx2':apQOSAcIndx2,'apQOSAcIndx3':apQOSAcIndx3,'apQOSAcIndx4':apQOSAcIndx4,'apQOSAifsn1':apQOSAifsn1,'apQOSAifsn2':apQOSAifsn2,'apQOSAifsn3':apQOSAifsn3,'apQOSAifsn4':apQOSAifsn4,'apQOSEcwMin1':apQOSEcwMin1,'apQOSEcwMin2':apQOSEcwMin2,'apQOSEcwMin3':apQOSEcwMin3,'apQOSEcwMin4':apQOSEcwMin4,'apQOSEcwMax1':apQOSEcwMax1,'apQOSEcwMax2':apQOSEcwMax2,'apQOSEcwMax3':apQOSEcwMax3,'apQOSEcwMax4':apQOSEcwMax4,'apQOSTxopLmt1':apQOSTxopLmt1,'apQOSTxopLmt2':apQOSTxopLmt2,'apQOSTxopLmt3':apQOSTxopLmt3,'apQOSTxopLmt4':apQOSTxopLmt4,'apQOSAcmAndAck1':apQOSAcmAndAck1,'apQOSAcmAndAck2':apQOSAcmAndAck2,'apQOSAcmAndAck3':apQOSAcmAndAck3,'apQOSAcmAndAck4':apQOSAcmAndAck4,'apAlarmParamConfigEntry':apAlarmParamConfigEntry,'apStaInterfNumThreshhd':apStaInterfNumThreshhd,'apAPCoInterfThreshhd':apAPCoInterfThreshhd,'apAPNeiborInterfThreshhd':apAPNeiborInterfThreshhd,'apCPUusageThreshhd':apCPUusageThreshhd,'apMemUsageThreshhd':apMemUsageThreshhd,'acUserExcepOfflineTimes':acUserExcepOfflineTimes,'acAuthReqTimes':acAuthReqTimes,'acAuthSuccessTimes':acAuthSuccessTimes,'acAuthReqFailTimes':acAuthReqFailTimes,'acDisconnectOnlineUsersCount':acDisconnectOnlineUsersCount,'acOnlineUserNum':acOnlineUserNum,'apVLANConfigObjects':apVLANConfigObjects,'apVLANConfigTable':apVLANConfigTable,'apVLANConfigTableEntry':apVLANConfigTableEntry,'apVLANID':apVLANID,'apVlanCfgStatus':apVlanCfgStatus,'apStatisticsInfoReadObjects':apStatisticsInfoReadObjects,'apSysCapabilityStatisticsObjects':apSysCapabilityStatisticsObjects,'apSysCapabilityStatisticsTable':apSysCapabilityStatisticsTable,'apSysCapabilityStatisticsTableEntry':apSysCapabilityStatisticsTableEntry,'apCPURTUsage':apCPURTUsage,'apCPUAvgUsage':apCPUAvgUsage,'apMemRTUsage':apMemRTUsage,'apMemAvgUsage':apMemAvgUsage,'apLinkStatisticsObjects':apLinkStatisticsObjects,'apLinkStatisticsTable':apLinkStatisticsTable,'apLinkStatisticsTableEntry':apLinkStatisticsTableEntry,'apStationAssocSum':apStationAssocSum,'apStationOnlineSum':apStationOnlineSum,'apAssocTimes':apAssocTimes,'apAssocFailTimes':apAssocFailTimes,'apReassocTimes':apReassocTimes,'apPreAssCannotShiftDeassocFailSum':apPreAssCannotShiftDeassocFailSum,'apApStatsDisassociated':apApStatsDisassociated,'apAssocRejectSum':apAssocRejectSum,'apBSSNotSupportAssocFailSum':apBSSNotSupportAssocFailSum,'apApAuthReqTimes':apApAuthReqTimes,'apApAuthSuccessTimes':apApAuthSuccessTimes,'acApAuthReqFailTimes':acApAuthReqFailTimes,'apReassocFailTimes':apReassocFailTimes,'apRSSILowAssocFailSum':apRSSILowAssocFailSum,'apUnknowReasonAssoFailSum':apUnknowReasonAssoFailSum,'apOut80211StandardAssocFailSum':apOut80211StandardAssocFailSum,'apAllStationsTotalUpTime':apAllStationsTotalUpTime,'apAssocRespTimes':apAssocRespTimes,'apAssocSuccTimes':apAssocSuccTimes,'apUserRadiusOnlineSum':apUserRadiusOnlineSum,'apAllUserOnlineTime':apAllUserOnlineTime,'apRadiusAuthTimes':apRadiusAuthTimes,'apRadiusAuthSuccTimes':apRadiusAuthSuccTimes,'apRadiusAuthFailTimes':apRadiusAuthFailTimes,'apInterfaceRGMIIStatisticsObjects':apInterfaceRGMIIStatisticsObjects,'apInterfaceRGMIIStatisticsTable':apInterfaceRGMIIStatisticsTable,'apInterfaceRGMIIStatisticsTableEntry':apInterfaceRGMIIStatisticsTableEntry,_AB:apRGMIIIndex,'apifInUcastPkts':apifInUcastPkts,'apifInNUcastPkts':apifInNUcastPkts,'apifInOctets':apifInOctets,'apifInDiscardPkts':apifInDiscardPkts,'apifInErrors':apifInErrors,'apifOutUcastPkts':apifOutUcastPkts,'apifOutNUcastPkts':apifOutNUcastPkts,'apifOutOctets':apifOutOctets,'apifOutDiscardPkts':apifOutDiscardPkts,'apifOutErrors':apifOutErrors,'apifUpDwnTimes':apifUpDwnTimes,'apInterfaceWireStatisticsObjects':apInterfaceWireStatisticsObjects,'apInterfaceWireStatisticsTable':apInterfaceWireStatisticsTable,'apInterfaceWireStatisticsTableEntry':apInterfaceWireStatisticsTableEntry,'apAvgRxSignalStrength':apAvgRxSignalStrength,'apHighestRxSignalStrength':apHighestRxSignalStrength,'apLowestRxSignalStrength':apLowestRxSignalStrength,'apWirelessUpdownTimes':apWirelessUpdownTimes,'apChStatsNumStations':apChStatsNumStations,'apTxDataPkts':apTxDataPkts,'apRxDataPkts':apRxDataPkts,'apUplinkDataOctets':apUplinkDataOctets,'apDwlinkDataOctets':apDwlinkDataOctets,'apChStatsDwlinkTotRetryPkts':apChStatsDwlinkTotRetryPkts,'apChStatsPhyErrPkts':apChStatsPhyErrPkts,'apChStatsMacFcsErrPkts':apChStatsMacFcsErrPkts,'apChStatsMacMicErrPkts':apChStatsMacMicErrPkts,'apChStatsMacDecryptErrPkts':apChStatsMacDecryptErrPkts,'apChStatsTotalErrPkts':apChStatsTotalErrPkts,'apRxMgmtFrameCnt':apRxMgmtFrameCnt,'apRxCtrlFrameCnt':apRxCtrlFrameCnt,'apRxDataFrameCnt':apRxDataFrameCnt,'apTxMgmtFrameCnt':apTxMgmtFrameCnt,'apTxCtrlFrameCnt':apTxCtrlFrameCnt,'apTxDataFrameCnt':apTxDataFrameCnt,'apChStatsFrameErrorCnt':apChStatsFrameErrorCnt,'apRetryCnt':apRetryCnt,'apCurTxPwr':apCurTxPwr,'apAPNeighborSSIDList':apAPNeighborSSIDList,'apChDownUnicastFrame':apChDownUnicastFrame,'apChDownNonUnicastFrame':apChDownNonUnicastFrame,'apChTxThroughput':apChTxThroughput,'apChRxThroughput':apChRxThroughput,'apChTxDropPkts':apChTxDropPkts,'apChRxDropPkts':apChRxDropPkts,'apChTxErrorPkts':apChTxErrorPkts,'apChRxErrorPkts':apChRxErrorPkts,'apRxBytes':apRxBytes,'apRxPkts':apRxPkts,'apTxBytes':apTxBytes,'apTxPkts':apTxPkts,'apDownNonUnicastPkts':apDownNonUnicastPkts,'apDownUnicastPkts':apDownUnicastPkts,'apUpNonUnicastPkts':apUpNonUnicastPkts,'apUpUnicastPkts':apUpUnicastPkts,'apAssoFailUnknowReason':apAssoFailUnknowReason,'apAssoFailOutofDot11':apAssoFailOutofDot11,'apAssoTotalTime':apAssoTotalTime,'apAuthReqFailTimes':apAuthReqFailTimes,'apAuthReqTimes':apAuthReqTimes,'apAuthSuccessTimes':apAuthSuccessTimes,'apReAssoFailTimes':apReAssoFailTimes,'apMacTxCorrectFrameCnt':apMacTxCorrectFrameCnt,'apMacRxCorrectFrameCnt':apMacRxCorrectFrameCnt,'apPktErrRate':apPktErrRate,'apTotalRxBytes':apTotalRxBytes,'apTotalTxBytes':apTotalTxBytes,'apTxErrorPkts':apTxErrorPkts,'apTxDropPkts':apTxDropPkts,'apIfRadiusOnlineUserNum':apIfRadiusOnlineUserNum,'apSSIDStatisticsObjects':apSSIDStatisticsObjects,'apSSIDStatisticsTable':apSSIDStatisticsTable,'apSSIDStatisticsTableEntry':apSSIDStatisticsTableEntry,_AC:apSSIDStatisticsAPMac,_AD:apSSIDStatisticsRadioId,_AE:apSSIDStatisticsWlanId,'apSSIDTxDataPkts':apSSIDTxDataPkts,'apSSIDRxDataPkts':apSSIDRxDataPkts,'apSSIDUplinkDataOctets':apSSIDUplinkDataOctets,'apSSIDDwlinkDataOctets':apSSIDDwlinkDataOctets,'apSSIDChStatsDwlinkTotRetryPkts':apSSIDChStatsDwlinkTotRetryPkts,'apSSIDApChStatsNumStations':apSSIDApChStatsNumStations,'apApChStatsOnlineSum':apApChStatsOnlineSum,'apSSIDStatisticsName':apSSIDStatisticsName,'apSSIDMacTxPkts':apSSIDMacTxPkts,'apSSIDMacRxPkts':apSSIDMacRxPkts,'apSSIDStatisticsNewTable':apSSIDStatisticsNewTable,'apSSIDStatisticsNewTableEntry':apSSIDStatisticsNewTableEntry,_AF:apSSIDStatisticsNewAPMac,_AG:apSSIDStatisticsNewRadioId,_AH:apSSIDStatisticsNewSSID,'apSSIDNewTxDataPkts':apSSIDNewTxDataPkts,'apSSIDNewRxDataPkts':apSSIDNewRxDataPkts,'apSSIDNewUplinkDataOctets':apSSIDNewUplinkDataOctets,'apSSIDNewDwlinkDataOctets':apSSIDNewDwlinkDataOctets,'apSSIDNewChStatsDwlinkTotRetryPkts':apSSIDNewChStatsDwlinkTotRetryPkts,'apSSIDNewApChStatsNumStations':apSSIDNewApChStatsNumStations,'apApNewChStatsOnlineSum':apApNewChStatsOnlineSum,'apSSIDNewMacTxPkts':apSSIDNewMacTxPkts,'apSSIDNewMacRxPkts':apSSIDNewMacRxPkts,'apWAPIStatisticsObjects':apWAPIStatisticsObjects,'apWAPIStatisticsTable':apWAPIStatisticsTable,'apWAPIStatisticsTableEntry':apWAPIStatisticsTableEntry,'apWAPIControlledPortStatus':apWAPIControlledPortStatus,'apWAPISelectedUnicastCipher':apWAPISelectedUnicastCipher,'apWPIReplayCounters':apWPIReplayCounters,'apWPIDecryptableErrors':apWPIDecryptableErrors,'apWPIMICErrors':apWPIMICErrors,'apWAISignatureErrors':apWAISignatureErrors,'apWAIHMACErrors':apWAIHMACErrors,'apWAIAuthResultFailures':apWAIAuthResultFailures,'apWAIDiscardCounters':apWAIDiscardCounters,'apWAITimeoutCounters':apWAITimeoutCounters,'apWAIFormatErrors':apWAIFormatErrors,'apWAICertificateHandshakeFailures':apWAICertificateHandshakeFailures,'apWAIUnicastHandshakeFailures':apWAIUnicastHandshakeFailures,'apWAIMulticastHandshakeFailures':apWAIMulticastHandshakeFailures,'apStationStatisticsObjects':apStationStatisticsObjects,'apStationStatisticsTable':apStationStatisticsTable,'apStationStatisticsTableEntry':apStationStatisticsTableEntry,'apStaAddress':apStaAddress,'apStaUpTime':apStaUpTime,'apReceivedStaSignalStrength':apReceivedStaSignalStrength,'apAPReceiveStaSNR':apAPReceiveStaSNR,'apStaTxPkts':apStaTxPkts,'apStaTxBytes':apStaTxBytes,'apStaRxPkts':apStaRxPkts,'apStaRxBytes':apStaRxBytes,'apWAPISTAAddress':apWAPISTAAddress,'apWAPIVersion':apWAPIVersion,'apStaLinkSpeed':apStaLinkSpeed,'apStaUpRate':apStaUpRate,'apStaDownRate':apStaDownRate,'apStaTxThroughput':apStaTxThroughput,'apStaRxThroughput':apStaRxThroughput,'apStaRxRetryBytes':apStaRxRetryBytes,'apQOSStatisticsObjects':apQOSStatisticsObjects,'apQOSBaseStatisticsObjects':apQOSBaseStatisticsObjects,'apQOSBaseStatisticsTable':apQOSBaseStatisticsTable,'apQOSBaseStatisticsTableEntry':apQOSBaseStatisticsTableEntry,'apBaseQoSSvcQueAvgLen':apBaseQoSSvcQueAvgLen,'apBaseQoSSvcPktLossRatio':apBaseQoSSvcPktLossRatio,'apBaseAvgTransSpeed':apBaseAvgTransSpeed,'apQOSBackgroundStatisticsObjects':apQOSBackgroundStatisticsObjects,'apQOSBackgroundStatisticsTable':apQOSBackgroundStatisticsTable,'apQOSBackgroundStatisticsTableEntry':apQOSBackgroundStatisticsTableEntry,'apQOSBgQueAvgLen':apQOSBgQueAvgLen,'apQOSBgAvgBurst':apQOSBgAvgBurst,'apQOSBgPktLossRatio':apQOSBgPktLossRatio,'apQOSBgAvgTransSpeed':apQOSBgAvgTransSpeed,'apQOSBgSvcLoss':apQOSBgSvcLoss,'apQOSBestEffortStatisticsObjects':apQOSBestEffortStatisticsObjects,'apQOSBestEffortStatisticsTable':apQOSBestEffortStatisticsTable,'apQOSBestEffortStatisticsTableEntry':apQOSBestEffortStatisticsTableEntry,'apQOSBeQueAvgLen':apQOSBeQueAvgLen,'apQOSBeAvgBurst':apQOSBeAvgBurst,'apQOSBePktLossRatio':apQOSBePktLossRatio,'apQOSBeAvgTransSpeed':apQOSBeAvgTransSpeed,'apQOSBeSvcLoss':apQOSBeSvcLoss,'apQOSVoiceStatisticsObjects':apQOSVoiceStatisticsObjects,'apQOSVoiceStatisticsTable':apQOSVoiceStatisticsTable,'apQOSVoiceStatisticsTableEntry':apQOSVoiceStatisticsTableEntry,'apQOSVoiceQueAvgLen':apQOSVoiceQueAvgLen,'apQOSVoiceAvgBurst':apQOSVoiceAvgBurst,'apQOSVoicePktLossRatio':apQOSVoicePktLossRatio,'apQOSVoiceAvgTransSpeed':apQOSVoiceAvgTransSpeed,'apQOSVoicePutThroughRatio':apQOSVoicePutThroughRatio,'apQOSVoiceDropRatio':apQOSVoiceDropRatio,'apQOSVoiceSvcLoss':apQOSVoiceSvcLoss,'apQOSVoiceExceedMaxUsersRequest':apQOSVoiceExceedMaxUsersRequest,'apQOSVideoStatisticsObjects':apQOSVideoStatisticsObjects,'apQOSVideoStatisticsTable':apQOSVideoStatisticsTable,'apQOSVideoStatisticsTableEntry':apQOSVideoStatisticsTableEntry,'apQOSVideoQueAvgLen':apQOSVideoQueAvgLen,'apQOSVideoAvgBurst':apQOSVideoAvgBurst,'apQOSVideoPktLossRatio':apQOSVideoPktLossRatio,'apQOSVideoAvgTransSpeed':apQOSVideoAvgTransSpeed,'apQOSVideoPutThroughRatio':apQOSVideoPutThroughRatio,'apQOSVideoDropRatio':apQOSVideoDropRatio,'apQOSVideoSvcLoss':apQOSVideoSvcLoss,'apQOSVideoExceedMaxUsersRequest':apQOSVideoExceedMaxUsersRequest,'apWIDSRogueApInfoObjects':apWIDSRogueApInfoObjects,'apWIDSRogueApInfoTable':apWIDSRogueApInfoTable,'apWIDSRogueApInfoTableEntry':apWIDSRogueApInfoTableEntry,_AI:qtechRogueApMacAddr,'qtechRogueApRSSI':qtechRogueApRSSI,'apQtechAlarmTrapObjects':apQtechAlarmTrapObjects,'apAPMac':apAPMac,_AY:apWorkModeBeforeChange,_AZ:apWorkModeAfterChange,_Ac:apSSIDKey,_Ad:apSSIDKeyConflict,_Ae:apCyperIndex,_Z:apInterruptReason,_I:apWorkingAPRadioIfInfo,_O:apWorkingAPChannel,_f:apInterfAPChannel,_V:apInterfAPBSSID,_g:apInterfStaMac,_h:apPermitAssoUser,_a:apAssoFailReason,_Af:apChannelBeforeChange,_Ag:apChannelAfterChange,_Ah:apChanChangeMode,_Q:apWorkingAPBSSID,_P:apWorkingAPSSID,_M:apStaMacAddr,_Az:apAuthMode,_A_:apAuthFailReason,_Aa:updateFailReason,_Ab:apSWVersionBeforeUpdate,_i:apAPRadioId,_Aj:apRevPackages,_Ak:apCPUUsage,_Ai:apSpeciousDeviceMac,'apRSSI':apRSSI,_Al:apAttackReason,'apWlanId':apWlanId,_Am:apWlanSSID,_An:apWlanSecurityModeBeforeChg,_Ao:apWlanSecurityModeAfterChg,_j:apTrapIllegalApMac,_k:apTrapIllegalApChannel,_l:apTrapIllegalApRSSI,_m:apTrapWorkingApMac,_n:apTrapWorkingApBSSID,_o:apTrapIllegalApType,_p:apTrapIllegalApSSID,_Ap:apAPRadioType,_Aq:apAssocAuthMode,_Ar:apStaRSSI,_As:apAssocFailReason,_At:apSpectralInfoApMac,_Au:apSpectralInfoType,_Av:apSpectralInfoFreq,_Aw:apSpectralInfoRssi,_Ax:apCounterMeasureApMac,_Ay:apCounterMeasureBssid,'apAccessControl':apAccessControl,'apTerminalPermitTable':apTerminalPermitTable,'apTerminalPermitEntry':apTerminalPermitEntry,_AJ:apWhiteListIndex,'apPermitMAC':apPermitMAC,'apWhiteListStatus':apWhiteListStatus,'apTerminalDeniedTable':apTerminalDeniedTable,'apTerminalDeniedEntry':apTerminalDeniedEntry,_AK:apBlackListIndex,'apAttackDeviceMAC':apAttackDeviceMAC,'apBlackListStatus':apBlackListStatus,'apTerminalBlackListTable':apTerminalBlackListTable,'apTerminalBlackListEntry':apTerminalBlackListEntry,_AL:apBlackListDeviceMAC,'apBlackListAddReason':apBlackListAddReason,'apBlackListDuration':apBlackListDuration,'acCapabilityStatistics':acCapabilityStatistics,'acWirelessDownDropFrame':acWirelessDownDropFrame,'acWirelessDownRetryFrame':acWirelessDownRetryFrame,'acWirelessDownFrame':acWirelessDownFrame,'acWirelessDownErrorFrame':acWirelessDownErrorFrame,'acWirelessUpFrame':acWirelessUpFrame,'acWirelessUpDropFrame':acWirelessUpDropFrame,'acWirelessUpRetryFrame':acWirelessUpRetryFrame,'acWirelessUpRate':acWirelessUpRate,'acWirelessDownRate':acWirelessDownRate,'apWidsInfoObjects':apWidsInfoObjects,'apWidsIllegalApTable':apWidsIllegalApTable,'apWidsIllegalApEntry':apWidsIllegalApEntry,_AM:apIllegalApMac,'apIllegalApChannel':apIllegalApChannel,'apIllegalApRSSI':apIllegalApRSSI,'apWorkingApMac':apWorkingApMac,'apDetectAPBSSID':apDetectAPBSSID,'apIllegalApType':apIllegalApType,'apIllegalApSSID':apIllegalApSSID,'apWidsApCounterTable':apWidsApCounterTable,'apWidsApCounterEntry':apWidsApCounterEntry,_AN:apCounterMac,'apCounter':apCounter,'apCounterMode':apCounterMode,'apCounterRssiThreshold':apCounterRssiThreshold,'apWidsDeviceMode':apWidsDeviceMode,'apWidsCounterIllegalAp':apWidsCounterIllegalAp,'apWidsCounterModeIllegalAp':apWidsCounterModeIllegalAp,'apWidsDeviceModeFlag':apWidsDeviceModeFlag,'apWidsCounterIllegalApFlag':apWidsCounterIllegalApFlag,'apWidsCounterModeIllegalApFlag':apWidsCounterModeIllegalApFlag,'apWidsPermitMacTable':apWidsPermitMacTable,'apWidsPermitMacEntry':apWidsPermitMacEntry,_AO:apWidsPermitMac,'apPermitMacrowstatus':apPermitMacrowstatus,'apWidsPermitSSIDTable':apWidsPermitSSIDTable,'apWidsPermitSSIDEntry':apWidsPermitSSIDEntry,_AP:apCounterSSID,'apPermitSSIDrowstatus':apPermitSSIDrowstatus,'apWidsPermitVendorTable':apWidsPermitVendorTable,'apWidsPermitVendorEntry':apWidsPermitVendorEntry,_AQ:apCounterVendor,'apPermitVendorrowstatus':apPermitVendorrowstatus,'apWidsStaticAttackTable':apWidsStaticAttackTable,'apWidsStaticAttackEntry':apWidsStaticAttackEntry,_AR:apStaticAttackMac,'apStaticAttackrowstatus':apStaticAttackrowstatus,'apWidsNeighborApInfoTable':apWidsNeighborApInfoTable,'apWidsNeighborApInfoEntry':apWidsNeighborApInfoEntry,_AS:neighborApMac,'neighborApSSID':neighborApSSID,'neighborApRSSI':neighborApRSSI,'neighborApChannel':neighborApChannel,'neighborApInControl':neighborApInControl,'apWidsClearIlleglApListFlag':apWidsClearIlleglApListFlag,'apWidsFloodInterval':apWidsFloodInterval,'apWidsBlackListThreshold':apWidsBlackListThreshold,'apWidsBlackListDuration':apWidsBlackListDuration,'apWidsFloodDetectOnOff':apWidsFloodDetectOnOff,'apWidsCounterRssiThreshold':apWidsCounterRssiThreshold,'apWidsBlackSSIDTable':apWidsBlackSSIDTable,'apWidsBlackSSIDEntry':apWidsBlackSSIDEntry,_AT:apBlackSSID,'apBlackSSIDrowstatus':apBlackSSIDrowstatus,'apConfigInfoObjects':apConfigInfoObjects,'apConfigInfoTable':apConfigInfoTable,'apConfigInfoEntry':apConfigInfoEntry,_AU:apConfigInfoMac,'apSpectralSwitch':apSpectralSwitch,'apSpectralSupport':apSpectralSupport,'apSmartAntSupport':apSmartAntSupport,'apSmartDisSupport':apSmartDisSupport,'apAntdetectSupport':apAntdetectSupport,'apAntdetectEnable':apAntdetectEnable,'apAntdetectInterval':apAntdetectInterval,'apAntdetectState':apAntdetectState,'apAntDetectObjects':apAntDetectObjects,'apAntDetectTable':apAntDetectTable,'apAntDetectEntry':apAntDetectEntry,_AV:apAntDetectAPMac,_AW:apAntDetectAntIndex,'apAntDetectDesc':apAntDetectDesc,'apAntDetectRadioId':apAntDetectRadioId,'apAntDetectStatus':apAntDetectStatus,'apAntDetectCfgTable':apAntDetectCfgTable,'apAntDetectCfgEntry':apAntDetectCfgEntry,_AX:apAntDetectCfgAPMac,'apAntDetectCfgSupport':apAntDetectCfgSupport,'apAntDetectCfgSwitch':apAntDetectCfgSwitch})