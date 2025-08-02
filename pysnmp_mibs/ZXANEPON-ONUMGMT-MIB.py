_B1='zxAnEponOltIfIndex'
_B0='zxAnEponOnuTkIgmpIpAddr'
_A_='zxAnEponOnuTkIgmpVlanId'
_Az='zxAnPtpIfIndex'
_Ay='zxAnEponRmEthHisIntervalNo'
_Ax='zxAnEponOnuDbaQueueSetIndex'
_Aw='auto-negotiate'
_Av='zx-ISO-ETHERNET'
_Au='zx-REM-FAULT2'
_At='zx-REM-FAULT1'
_As='zx-1000BASE-TFD'
_Ar='zx-1000BASE-T'
_Aq='zx-1000BASE-XFD'
_Ap='zx-1000BASE-X'
_Ao='zx-100BASE-T2FD'
_An='zx-100BASE-T2'
_Am='zx-FDX-BPAUSE'
_Al='zx-FDX-SPAUSE'
_Ak='zx-FDX-APAUSE'
_Aj='zx-FDX-PAUSE'
_Ai='zx-100BASE-TXFD'
_Ah='zx-100BASE-TX'
_Ag='zx-100BASE-T4'
_Af='zx-10BASE-TFD'
_Ae='zx-10BASE-T'
_Ad='zx-UNKNOWN'
_Ac='zx-GLOBAL'
_Ab='Milliseconds'
_Aa='zxAnEponRmOnuWanPortId'
_AZ='zxAnEponRmWanPrfName'
_AY='zxAnEponOnuUniMacSequenceNo'
_AX='zxAnEponOnuUniVlanId'
_AW='zxAnEponOnuVersionImageIndex'
_AV='downloading'
_AU='zxAnEponOnuUniAlarmCode'
_AT='zxAnEponOnuPonAlarmCode'
_AS='zxAnEponOnuLvlAlarmCode'
_AR='zxAnEponOnuSlaServiceIdx'
_AQ='zxAnEponOnuLlid'
_AP='zxAnEponOnuIptvUserVlan'
_AO='zxAnEponOnuMVlan'
_AN='zxEponMduSnmpTrapHostIndex'
_AM='zxAnEponOnuInterfaceType'
_AL='notSupport'
_AK='notInService'
_AJ='rebooting'
_AI='registering'
_AH='zxAnEponRmVoipH248MgcpUserTidGroupIdx'
_AG='secondary'
_AF='zxAnEponRmVoipFaxProfileIdx'
_AE='zxAnEponRmVoipSipProfileIdx'
_AD='zxAnEponRmVoipMgcpProfileIdx'
_AC='deviceName'
_AB='domainName'
_AA='zxAnEponRmVoipH248ProfileIdx'
_A9='zxAnEponRmVoipVlanProfileIdx'
_A8='zxAnEponRmVoipIpProfileIdx'
_A7='uniProfileIndex'
_A6='zxAnEponOnuVioceCardIndex'
_A5='zxEponStaticVlan'
_A4='zxAnEponOnuStaticMAC'
_A3='zxEponBindVlan'
_A2='zxAnEponOnuBindMAC'
_A1='zxEponFilterVlan'
_A0='zxAnEponOnuFilterMAC'
_z='zxAnEponOnuMcstCtrlEntryIndex'
_y='delete'
_x='filter'
_w='zxAnEponOnuClassMarkingRulePrecedence'
_v='zxAnEponOnuClassMarkingRuleId'
_u='zxAnEponOnuClassMarkingConditionId'
_t='zxAnEponOnuVlanAggGrpId'
_s='zxAnEponOnuVlanTransModeEntryId'
_r='onuOffLine'
_q='zxAnEponOnuVersionId'
_p='zxAnEponOnuSlaProfileIndex'
_o='unsupported'
_n='supported'
_m='kbps'
_l='reset'
_k='other'
_j='deregister'
_i='h248'
_h='sip'
_g='pap'
_f='chap'
_e='auto'
_d='pppoe'
_c='dhcp'
_b='transparent'
_a='zxAnEponRmPerfOnuPortType'
_Z='mgcp'
_Y='none'
_X='active'
_W='Seconds'
_V='static'
_U='deactive'
_T='Unsigned32'
_S='disabled'
_R='enabled'
_Q='kt-oam'
_P='tk-oam'
_O='Bits'
_N='OctetString'
_M='zxAnEponOnuCardIndex'
_L='DisplayString'
_K='enable'
_J='disable'
_I='not-accessible'
_H='zxAnEponOnuPortId'
_G='read-create'
_F='zxAnEponOnuIfIndex'
_E='ZXANEPON-ONUMGMT-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_O,'Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_T,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
zxAnEponMib,=mibBuilder.importSymbols('ZTE-MASTER-MIB','zxAnEponMib')
zxAnEponOnuRemoteMgmt=ModuleIdentity((1,3,6,1,4,1,3902,1015,1010,1,1))
_ZxAnEponOnuExtendedAttrMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuExtendedAttrMgmt=_ZxAnEponOnuExtendedAttrMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,1))
_ZxAnEponOnuSnTable_Object=MibTable
zxAnEponOnuSnTable=_ZxAnEponOnuSnTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,1))
if mibBuilder.loadTexts:zxAnEponOnuSnTable.setStatus(_A)
_ZxAnEponOnuSnEntry_Object=MibTableRow
zxAnEponOnuSnEntry=_ZxAnEponOnuSnEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,1,1))
zxAnEponOnuSnEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuSnEntry.setStatus(_A)
_ZxAnEponOnuIfIndex_Type=Integer32
_ZxAnEponOnuIfIndex_Object=MibTableColumn
zxAnEponOnuIfIndex=_ZxAnEponOnuIfIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,1,1,1),_ZxAnEponOnuIfIndex_Type())
zxAnEponOnuIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuIfIndex.setStatus(_A)
class _ZxAnEponOnuVendorId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ZxAnEponOnuVendorId_Type.__name__=_N
_ZxAnEponOnuVendorId_Object=MibTableColumn
zxAnEponOnuVendorId=_ZxAnEponOnuVendorId_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,1,1,2),_ZxAnEponOnuVendorId_Type())
zxAnEponOnuVendorId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVendorId.setStatus(_A)
class _ZxAnEponOnuModel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ZxAnEponOnuModel_Type.__name__=_N
_ZxAnEponOnuModel_Object=MibTableColumn
zxAnEponOnuModel=_ZxAnEponOnuModel_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,1,1,3),_ZxAnEponOnuModel_Type())
zxAnEponOnuModel.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuModel.setStatus(_A)
_ZxAnEponOnuMacAddr_Type=MacAddress
_ZxAnEponOnuMacAddr_Object=MibTableColumn
zxAnEponOnuMacAddr=_ZxAnEponOnuMacAddr_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,1,1,4),_ZxAnEponOnuMacAddr_Type())
zxAnEponOnuMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuMacAddr.setStatus(_A)
class _ZxAnEponOnuHardwareVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxAnEponOnuHardwareVersion_Type.__name__=_N
_ZxAnEponOnuHardwareVersion_Object=MibTableColumn
zxAnEponOnuHardwareVersion=_ZxAnEponOnuHardwareVersion_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,1,1,5),_ZxAnEponOnuHardwareVersion_Type())
zxAnEponOnuHardwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuHardwareVersion.setStatus(_A)
class _ZxAnEponOnuSoftwareVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_ZxAnEponOnuSoftwareVersion_Type.__name__=_N
_ZxAnEponOnuSoftwareVersion_Object=MibTableColumn
zxAnEponOnuSoftwareVersion=_ZxAnEponOnuSoftwareVersion_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,1,1,6),_ZxAnEponOnuSoftwareVersion_Type())
zxAnEponOnuSoftwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuSoftwareVersion.setStatus(_A)
class _ZxAnEponOnuExtendedModel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_ZxAnEponOnuExtendedModel_Type.__name__=_N
_ZxAnEponOnuExtendedModel_Object=MibTableColumn
zxAnEponOnuExtendedModel=_ZxAnEponOnuExtendedModel_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,1,1,7),_ZxAnEponOnuExtendedModel_Type())
zxAnEponOnuExtendedModel.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuExtendedModel.setStatus(_A)
_ZxAnEponOnuFirmwareVerTable_Object=MibTable
zxAnEponOnuFirmwareVerTable=_ZxAnEponOnuFirmwareVerTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,2))
if mibBuilder.loadTexts:zxAnEponOnuFirmwareVerTable.setStatus(_A)
_ZxAnEponOnuFirmwareVerEntry_Object=MibTableRow
zxAnEponOnuFirmwareVerEntry=_ZxAnEponOnuFirmwareVerEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,2,1))
zxAnEponOnuFirmwareVerEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuFirmwareVerEntry.setStatus(_A)
class _ZxAnEponOnuFirmwareVer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_ZxAnEponOnuFirmwareVer_Type.__name__=_N
_ZxAnEponOnuFirmwareVer_Object=MibTableColumn
zxAnEponOnuFirmwareVer=_ZxAnEponOnuFirmwareVer_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,2,1,1),_ZxAnEponOnuFirmwareVer_Type())
zxAnEponOnuFirmwareVer.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuFirmwareVer.setStatus(_A)
_ZxAnEponOnuChipsetIdTable_Object=MibTable
zxAnEponOnuChipsetIdTable=_ZxAnEponOnuChipsetIdTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,3))
if mibBuilder.loadTexts:zxAnEponOnuChipsetIdTable.setStatus(_A)
_ZxAnEponOnuChipsetIdEntry_Object=MibTableRow
zxAnEponOnuChipsetIdEntry=_ZxAnEponOnuChipsetIdEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,3,1))
zxAnEponOnuChipsetIdEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuChipsetIdEntry.setStatus(_A)
class _ZxAnEponOnuChipVendorId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_ZxAnEponOnuChipVendorId_Type.__name__=_N
_ZxAnEponOnuChipVendorId_Object=MibTableColumn
zxAnEponOnuChipVendorId=_ZxAnEponOnuChipVendorId_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,3,1,1),_ZxAnEponOnuChipVendorId_Type())
zxAnEponOnuChipVendorId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuChipVendorId.setStatus(_A)
class _ZxAnEponOnuChipModel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_ZxAnEponOnuChipModel_Type.__name__=_N
_ZxAnEponOnuChipModel_Object=MibTableColumn
zxAnEponOnuChipModel=_ZxAnEponOnuChipModel_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,3,1,2),_ZxAnEponOnuChipModel_Type())
zxAnEponOnuChipModel.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuChipModel.setStatus(_A)
_ZxAnEponOnuChipRevision_Type=Integer32
_ZxAnEponOnuChipRevision_Object=MibTableColumn
zxAnEponOnuChipRevision=_ZxAnEponOnuChipRevision_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,3,1,3),_ZxAnEponOnuChipRevision_Type())
zxAnEponOnuChipRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuChipRevision.setStatus(_A)
class _ZxAnEponOnuChipDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_ZxAnEponOnuChipDate_Type.__name__=_N
_ZxAnEponOnuChipDate_Object=MibTableColumn
zxAnEponOnuChipDate=_ZxAnEponOnuChipDate_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,3,1,4),_ZxAnEponOnuChipDate_Type())
zxAnEponOnuChipDate.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuChipDate.setStatus(_A)
_ZxAnEponOnuCapabilityTable_Object=MibTable
zxAnEponOnuCapabilityTable=_ZxAnEponOnuCapabilityTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,4))
if mibBuilder.loadTexts:zxAnEponOnuCapabilityTable.setStatus(_A)
_ZxAnEponOnuCapabilityEntry_Object=MibTableRow
zxAnEponOnuCapabilityEntry=_ZxAnEponOnuCapabilityEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,4,1))
zxAnEponOnuCapabilityEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuCapabilityEntry.setStatus(_A)
class _ZxAnEponOnuServiceSupported_Type(Bits):namedValues=NamedValues(*(('gePortSupport',0),('fePortSupport',1),('voipSupport',2),('e1Support',3),(_r,4)))
_ZxAnEponOnuServiceSupported_Type.__name__=_O
_ZxAnEponOnuServiceSupported_Object=MibTableColumn
zxAnEponOnuServiceSupported=_ZxAnEponOnuServiceSupported_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,4,1,1),_ZxAnEponOnuServiceSupported_Type())
zxAnEponOnuServiceSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuServiceSupported.setStatus(_A)
class _ZxAnEponOnuGePortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnEponOnuGePortNumber_Type.__name__=_B
_ZxAnEponOnuGePortNumber_Object=MibTableColumn
zxAnEponOnuGePortNumber=_ZxAnEponOnuGePortNumber_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,4,1,2),_ZxAnEponOnuGePortNumber_Type())
zxAnEponOnuGePortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuGePortNumber.setStatus(_A)
class _ZxAnEponOnuGePortBitmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxAnEponOnuGePortBitmap_Type.__name__=_N
_ZxAnEponOnuGePortBitmap_Object=MibTableColumn
zxAnEponOnuGePortBitmap=_ZxAnEponOnuGePortBitmap_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,4,1,3),_ZxAnEponOnuGePortBitmap_Type())
zxAnEponOnuGePortBitmap.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuGePortBitmap.setStatus(_A)
class _ZxAnEponOnuFePortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnEponOnuFePortNumber_Type.__name__=_B
_ZxAnEponOnuFePortNumber_Object=MibTableColumn
zxAnEponOnuFePortNumber=_ZxAnEponOnuFePortNumber_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,4,1,4),_ZxAnEponOnuFePortNumber_Type())
zxAnEponOnuFePortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuFePortNumber.setStatus(_A)
class _ZxAnEponOnuFePortBitmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxAnEponOnuFePortBitmap_Type.__name__=_N
_ZxAnEponOnuFePortBitmap_Object=MibTableColumn
zxAnEponOnuFePortBitmap=_ZxAnEponOnuFePortBitmap_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,4,1,5),_ZxAnEponOnuFePortBitmap_Type())
zxAnEponOnuFePortBitmap.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuFePortBitmap.setStatus(_A)
class _ZxAnEponOnuPotsPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnEponOnuPotsPortNumber_Type.__name__=_B
_ZxAnEponOnuPotsPortNumber_Object=MibTableColumn
zxAnEponOnuPotsPortNumber=_ZxAnEponOnuPotsPortNumber_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,4,1,6),_ZxAnEponOnuPotsPortNumber_Type())
zxAnEponOnuPotsPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuPotsPortNumber.setStatus(_A)
class _ZxAnEponOnuE1PortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnEponOnuE1PortNumber_Type.__name__=_B
_ZxAnEponOnuE1PortNumber_Object=MibTableColumn
zxAnEponOnuE1PortNumber=_ZxAnEponOnuE1PortNumber_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,4,1,7),_ZxAnEponOnuE1PortNumber_Type())
zxAnEponOnuE1PortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuE1PortNumber.setStatus(_A)
class _ZxAnEponOnuUsQueueNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnEponOnuUsQueueNumber_Type.__name__=_B
_ZxAnEponOnuUsQueueNumber_Object=MibTableColumn
zxAnEponOnuUsQueueNumber=_ZxAnEponOnuUsQueueNumber_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,4,1,8),_ZxAnEponOnuUsQueueNumber_Type())
zxAnEponOnuUsQueueNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuUsQueueNumber.setStatus(_A)
class _ZxAnEponOnuUsPortMaxQueueNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnEponOnuUsPortMaxQueueNumber_Type.__name__=_B
_ZxAnEponOnuUsPortMaxQueueNumber_Object=MibTableColumn
zxAnEponOnuUsPortMaxQueueNumber=_ZxAnEponOnuUsPortMaxQueueNumber_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,4,1,9),_ZxAnEponOnuUsPortMaxQueueNumber_Type())
zxAnEponOnuUsPortMaxQueueNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuUsPortMaxQueueNumber.setStatus(_A)
class _ZxAnEponOnuDsQueueNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnEponOnuDsQueueNumber_Type.__name__=_B
_ZxAnEponOnuDsQueueNumber_Object=MibTableColumn
zxAnEponOnuDsQueueNumber=_ZxAnEponOnuDsQueueNumber_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,4,1,10),_ZxAnEponOnuDsQueueNumber_Type())
zxAnEponOnuDsQueueNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuDsQueueNumber.setStatus(_A)
class _ZxAnEponOnuDsPortMaxQueueNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnEponOnuDsPortMaxQueueNumber_Type.__name__=_B
_ZxAnEponOnuDsPortMaxQueueNumber_Object=MibTableColumn
zxAnEponOnuDsPortMaxQueueNumber=_ZxAnEponOnuDsPortMaxQueueNumber_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,4,1,11),_ZxAnEponOnuDsPortMaxQueueNumber_Type())
zxAnEponOnuDsPortMaxQueueNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuDsPortMaxQueueNumber.setStatus(_A)
_ZxAnEponOnuBatteryBackup_Type=TruthValue
_ZxAnEponOnuBatteryBackup_Object=MibTableColumn
zxAnEponOnuBatteryBackup=_ZxAnEponOnuBatteryBackup_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,4,1,12),_ZxAnEponOnuBatteryBackup_Type())
zxAnEponOnuBatteryBackup.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuBatteryBackup.setStatus(_A)
_ZxAnEponOnuEthLinkStateTable_Object=MibTable
zxAnEponOnuEthLinkStateTable=_ZxAnEponOnuEthLinkStateTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,5))
if mibBuilder.loadTexts:zxAnEponOnuEthLinkStateTable.setStatus(_A)
_ZxAnEponOnuEthLinkStateEntry_Object=MibTableRow
zxAnEponOnuEthLinkStateEntry=_ZxAnEponOnuEthLinkStateEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,5,1))
zxAnEponOnuEthLinkStateEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuEthLinkStateEntry.setStatus(_A)
_ZxAnEponOnuPortId_Type=Integer32
_ZxAnEponOnuPortId_Object=MibTableColumn
zxAnEponOnuPortId=_ZxAnEponOnuPortId_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,5,1,1),_ZxAnEponOnuPortId_Type())
zxAnEponOnuPortId.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuPortId.setStatus(_A)
class _ZxAnEponOnuEthPortLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_ZxAnEponOnuEthPortLinkState_Type.__name__=_B
_ZxAnEponOnuEthPortLinkState_Object=MibTableColumn
zxAnEponOnuEthPortLinkState=_ZxAnEponOnuEthPortLinkState_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,5,1,2),_ZxAnEponOnuEthPortLinkState_Type())
zxAnEponOnuEthPortLinkState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuEthPortLinkState.setStatus(_A)
_ZxAnEponOnuEthPortPauseTable_Object=MibTable
zxAnEponOnuEthPortPauseTable=_ZxAnEponOnuEthPortPauseTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,6))
if mibBuilder.loadTexts:zxAnEponOnuEthPortPauseTable.setStatus(_A)
_ZxAnEponOnuEthPortPauseEntry_Object=MibTableRow
zxAnEponOnuEthPortPauseEntry=_ZxAnEponOnuEthPortPauseEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,6,1))
zxAnEponOnuEthPortPauseEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuEthPortPauseEntry.setStatus(_A)
class _ZxAnEponOnuPortBackPressure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_X,2)))
_ZxAnEponOnuPortBackPressure_Type.__name__=_B
_ZxAnEponOnuPortBackPressure_Object=MibTableColumn
zxAnEponOnuPortBackPressure=_ZxAnEponOnuPortBackPressure_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,6,1,1),_ZxAnEponOnuPortBackPressure_Type())
zxAnEponOnuPortBackPressure.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPortBackPressure.setStatus(_A)
_ZxAnEponOnuEthPortPolicingTable_Object=MibTable
zxAnEponOnuEthPortPolicingTable=_ZxAnEponOnuEthPortPolicingTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,7))
if mibBuilder.loadTexts:zxAnEponOnuEthPortPolicingTable.setStatus(_A)
_ZxAnEponOnuEthPortPolicingEntry_Object=MibTableRow
zxAnEponOnuEthPortPolicingEntry=_ZxAnEponOnuEthPortPolicingEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,7,1))
zxAnEponOnuEthPortPolicingEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuEthPortPolicingEntry.setStatus(_A)
class _ZxAnEponOnuPortPolicing_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_X,2)))
_ZxAnEponOnuPortPolicing_Type.__name__=_B
_ZxAnEponOnuPortPolicing_Object=MibTableColumn
zxAnEponOnuPortPolicing=_ZxAnEponOnuPortPolicing_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,7,1,1),_ZxAnEponOnuPortPolicing_Type())
zxAnEponOnuPortPolicing.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPortPolicing.setStatus(_A)
class _ZxAnEponOnuPortPolicingCir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_ZxAnEponOnuPortPolicingCir_Type.__name__=_B
_ZxAnEponOnuPortPolicingCir_Object=MibTableColumn
zxAnEponOnuPortPolicingCir=_ZxAnEponOnuPortPolicingCir_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,7,1,2),_ZxAnEponOnuPortPolicingCir_Type())
zxAnEponOnuPortPolicingCir.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPortPolicingCir.setStatus(_A)
class _ZxAnEponOnuPortPolicingBucketDepth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1522,16777215))
_ZxAnEponOnuPortPolicingBucketDepth_Type.__name__=_B
_ZxAnEponOnuPortPolicingBucketDepth_Object=MibTableColumn
zxAnEponOnuPortPolicingBucketDepth=_ZxAnEponOnuPortPolicingBucketDepth_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,7,1,3),_ZxAnEponOnuPortPolicingBucketDepth_Type())
zxAnEponOnuPortPolicingBucketDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPortPolicingBucketDepth.setStatus(_A)
class _ZxAnEponOnuPortPolicingExtraBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1522))
_ZxAnEponOnuPortPolicingExtraBurstSize_Type.__name__=_B
_ZxAnEponOnuPortPolicingExtraBurstSize_Object=MibTableColumn
zxAnEponOnuPortPolicingExtraBurstSize=_ZxAnEponOnuPortPolicingExtraBurstSize_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,7,1,4),_ZxAnEponOnuPortPolicingExtraBurstSize_Type())
zxAnEponOnuPortPolicingExtraBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPortPolicingExtraBurstSize.setStatus(_A)
class _ZxAnEponOnuPortPolicingDownStream_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notavailable',0),(_U,1),(_X,2)))
_ZxAnEponOnuPortPolicingDownStream_Type.__name__=_B
_ZxAnEponOnuPortPolicingDownStream_Object=MibTableColumn
zxAnEponOnuPortPolicingDownStream=_ZxAnEponOnuPortPolicingDownStream_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,7,1,5),_ZxAnEponOnuPortPolicingDownStream_Type())
zxAnEponOnuPortPolicingDownStream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPortPolicingDownStream.setStatus(_A)
class _ZxAnEponOnuPortPolicingCirDownStream_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_ZxAnEponOnuPortPolicingCirDownStream_Type.__name__=_B
_ZxAnEponOnuPortPolicingCirDownStream_Object=MibTableColumn
zxAnEponOnuPortPolicingCirDownStream=_ZxAnEponOnuPortPolicingCirDownStream_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,7,1,6),_ZxAnEponOnuPortPolicingCirDownStream_Type())
zxAnEponOnuPortPolicingCirDownStream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPortPolicingCirDownStream.setStatus(_A)
class _ZxAnEponOnuPortPolicingBucketDepthDownStream_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1522,16777215))
_ZxAnEponOnuPortPolicingBucketDepthDownStream_Type.__name__=_B
_ZxAnEponOnuPortPolicingBucketDepthDownStream_Object=MibTableColumn
zxAnEponOnuPortPolicingBucketDepthDownStream=_ZxAnEponOnuPortPolicingBucketDepthDownStream_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,7,1,7),_ZxAnEponOnuPortPolicingBucketDepthDownStream_Type())
zxAnEponOnuPortPolicingBucketDepthDownStream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPortPolicingBucketDepthDownStream.setStatus(_A)
class _ZxAnEponOnuPortPolicingExtraBurstSizeDownStream_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1522))
_ZxAnEponOnuPortPolicingExtraBurstSizeDownStream_Type.__name__=_B
_ZxAnEponOnuPortPolicingExtraBurstSizeDownStream_Object=MibTableColumn
zxAnEponOnuPortPolicingExtraBurstSizeDownStream=_ZxAnEponOnuPortPolicingExtraBurstSizeDownStream_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,7,1,8),_ZxAnEponOnuPortPolicingExtraBurstSizeDownStream_Type())
zxAnEponOnuPortPolicingExtraBurstSizeDownStream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPortPolicingExtraBurstSizeDownStream.setStatus(_A)
_ZxAnEponOnuVoipPortTable_Object=MibTable
zxAnEponOnuVoipPortTable=_ZxAnEponOnuVoipPortTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,8))
if mibBuilder.loadTexts:zxAnEponOnuVoipPortTable.setStatus(_A)
_ZxAnEponOnuVoipPortEntry_Object=MibTableRow
zxAnEponOnuVoipPortEntry=_ZxAnEponOnuVoipPortEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,8,1))
zxAnEponOnuVoipPortEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuVoipPortEntry.setStatus(_A)
class _ZxAnEponOnuVoipPortEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZxAnEponOnuVoipPortEnable_Type.__name__=_B
_ZxAnEponOnuVoipPortEnable_Object=MibTableColumn
zxAnEponOnuVoipPortEnable=_ZxAnEponOnuVoipPortEnable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,8,1,1),_ZxAnEponOnuVoipPortEnable_Type())
zxAnEponOnuVoipPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoipPortEnable.setStatus(_A)
_ZxAnEponOnuE1PortTable_Object=MibTable
zxAnEponOnuE1PortTable=_ZxAnEponOnuE1PortTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,9))
if mibBuilder.loadTexts:zxAnEponOnuE1PortTable.setStatus(_A)
_ZxAnEponOnuE1PortEntry_Object=MibTableRow
zxAnEponOnuE1PortEntry=_ZxAnEponOnuE1PortEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,9,1))
zxAnEponOnuE1PortEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuE1PortEntry.setStatus(_A)
class _ZxAnEponOnuE1PortEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZxAnEponOnuE1PortEnable_Type.__name__=_B
_ZxAnEponOnuE1PortEnable_Object=MibTableColumn
zxAnEponOnuE1PortEnable=_ZxAnEponOnuE1PortEnable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,9,1,1),_ZxAnEponOnuE1PortEnable_Type())
zxAnEponOnuE1PortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuE1PortEnable.setStatus(_A)
_ZxAnEponOnuVlanCfgMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuVlanCfgMgmt=_ZxAnEponOnuVlanCfgMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,1,10))
_ZxAnEponOnuVlanCfgTable_Object=MibTable
zxAnEponOnuVlanCfgTable=_ZxAnEponOnuVlanCfgTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,1))
if mibBuilder.loadTexts:zxAnEponOnuVlanCfgTable.setStatus(_A)
_ZxAnEponOnuVlanCfgEntry_Object=MibTableRow
zxAnEponOnuVlanCfgEntry=_ZxAnEponOnuVlanCfgEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,1,1))
zxAnEponOnuVlanCfgEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuVlanCfgEntry.setStatus(_A)
class _ZxAnEponOnuVlanMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_b,1),('tag',2),('translation',3),('trunk',4),('hybrid',5),('aggregation',6)))
_ZxAnEponOnuVlanMode_Type.__name__=_B
_ZxAnEponOnuVlanMode_Object=MibTableColumn
zxAnEponOnuVlanMode=_ZxAnEponOnuVlanMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,1,1,1),_ZxAnEponOnuVlanMode_Type())
zxAnEponOnuVlanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVlanMode.setStatus(_A)
class _ZxAnEponOnuVlanCfgState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('not-finish',1),('finish',2)))
_ZxAnEponOnuVlanCfgState_Type.__name__=_B
_ZxAnEponOnuVlanCfgState_Object=MibTableColumn
zxAnEponOnuVlanCfgState=_ZxAnEponOnuVlanCfgState_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,1,1,2),_ZxAnEponOnuVlanCfgState_Type())
zxAnEponOnuVlanCfgState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVlanCfgState.setStatus(_A)
_ZxAnEponOnuVlanTagTable_Object=MibTable
zxAnEponOnuVlanTagTable=_ZxAnEponOnuVlanTagTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,2))
if mibBuilder.loadTexts:zxAnEponOnuVlanTagTable.setStatus(_A)
_ZxAnEponOnuVlanTagEntry_Object=MibTableRow
zxAnEponOnuVlanTagEntry=_ZxAnEponOnuVlanTagEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,2,1))
zxAnEponOnuVlanTagEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuVlanTagEntry.setStatus(_A)
class _ZxAnEponOnuVlanTagVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxAnEponOnuVlanTagVid_Type.__name__=_B
_ZxAnEponOnuVlanTagVid_Object=MibTableColumn
zxAnEponOnuVlanTagVid=_ZxAnEponOnuVlanTagVid_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,2,1,1),_ZxAnEponOnuVlanTagVid_Type())
zxAnEponOnuVlanTagVid.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVlanTagVid.setStatus(_A)
_ZxAnEponOnuVlanTagTpid_Type=Integer32
_ZxAnEponOnuVlanTagTpid_Object=MibTableColumn
zxAnEponOnuVlanTagTpid=_ZxAnEponOnuVlanTagTpid_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,2,1,2),_ZxAnEponOnuVlanTagTpid_Type())
zxAnEponOnuVlanTagTpid.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVlanTagTpid.setStatus(_A)
class _ZxAnEponOnuVlanTagCfi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ZxAnEponOnuVlanTagCfi_Type.__name__=_B
_ZxAnEponOnuVlanTagCfi_Object=MibTableColumn
zxAnEponOnuVlanTagCfi=_ZxAnEponOnuVlanTagCfi_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,2,1,3),_ZxAnEponOnuVlanTagCfi_Type())
zxAnEponOnuVlanTagCfi.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVlanTagCfi.setStatus(_A)
class _ZxAnEponOnuVlanPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnEponOnuVlanPriority_Type.__name__=_B
_ZxAnEponOnuVlanPriority_Object=MibTableColumn
zxAnEponOnuVlanPriority=_ZxAnEponOnuVlanPriority_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,2,1,4),_ZxAnEponOnuVlanPriority_Type())
zxAnEponOnuVlanPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVlanPriority.setStatus(_A)
_ZxAnEponOnuVlanTranslationTable_Object=MibTable
zxAnEponOnuVlanTranslationTable=_ZxAnEponOnuVlanTranslationTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,3))
if mibBuilder.loadTexts:zxAnEponOnuVlanTranslationTable.setStatus(_A)
_ZxAnEponOnuVlanTranslationEntry_Object=MibTableRow
zxAnEponOnuVlanTranslationEntry=_ZxAnEponOnuVlanTranslationEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,3,1))
zxAnEponOnuVlanTranslationEntry.setIndexNames((0,_E,_F),(0,_E,_H),(0,_E,_s))
if mibBuilder.loadTexts:zxAnEponOnuVlanTranslationEntry.setStatus(_A)
_ZxAnEponOnuVlanTransModeEntryId_Type=Integer32
_ZxAnEponOnuVlanTransModeEntryId_Object=MibTableColumn
zxAnEponOnuVlanTransModeEntryId=_ZxAnEponOnuVlanTransModeEntryId_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,3,1,1),_ZxAnEponOnuVlanTransModeEntryId_Type())
zxAnEponOnuVlanTransModeEntryId.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuVlanTransModeEntryId.setStatus(_A)
_ZxAnEponOnuVlanTransOriginalTag_Type=Unsigned32
_ZxAnEponOnuVlanTransOriginalTag_Object=MibTableColumn
zxAnEponOnuVlanTransOriginalTag=_ZxAnEponOnuVlanTransOriginalTag_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,3,1,2),_ZxAnEponOnuVlanTransOriginalTag_Type())
zxAnEponOnuVlanTransOriginalTag.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVlanTransOriginalTag.setStatus(_A)
_ZxAnEponOnuVlanTransNewTag_Type=Unsigned32
_ZxAnEponOnuVlanTransNewTag_Object=MibTableColumn
zxAnEponOnuVlanTransNewTag=_ZxAnEponOnuVlanTransNewTag_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,3,1,3),_ZxAnEponOnuVlanTransNewTag_Type())
zxAnEponOnuVlanTransNewTag.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVlanTransNewTag.setStatus(_A)
_ZxAnEponOnuVlanTransModeRowStatus_Type=RowStatus
_ZxAnEponOnuVlanTransModeRowStatus_Object=MibTableColumn
zxAnEponOnuVlanTransModeRowStatus=_ZxAnEponOnuVlanTransModeRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,3,1,4),_ZxAnEponOnuVlanTransModeRowStatus_Type())
zxAnEponOnuVlanTransModeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVlanTransModeRowStatus.setStatus(_A)
_ZxAnEponOnuVlanTrunkTable_Object=MibTable
zxAnEponOnuVlanTrunkTable=_ZxAnEponOnuVlanTrunkTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,4))
if mibBuilder.loadTexts:zxAnEponOnuVlanTrunkTable.setStatus(_A)
_ZxAnEponOnuVlanTrunkEntry_Object=MibTableRow
zxAnEponOnuVlanTrunkEntry=_ZxAnEponOnuVlanTrunkEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,4,1))
zxAnEponOnuVlanTrunkEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuVlanTrunkEntry.setStatus(_A)
_ZxAnEponOnuVlanTrunkModeVlan_Type=OctetString
_ZxAnEponOnuVlanTrunkModeVlan_Object=MibTableColumn
zxAnEponOnuVlanTrunkModeVlan=_ZxAnEponOnuVlanTrunkModeVlan_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,4,1,1),_ZxAnEponOnuVlanTrunkModeVlan_Type())
zxAnEponOnuVlanTrunkModeVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVlanTrunkModeVlan.setStatus(_A)
_ZxAnEponOnuVlanAggregationTable_Object=MibTable
zxAnEponOnuVlanAggregationTable=_ZxAnEponOnuVlanAggregationTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,5))
if mibBuilder.loadTexts:zxAnEponOnuVlanAggregationTable.setStatus(_A)
_ZxAnEponOnuVlanAggregationEntry_Object=MibTableRow
zxAnEponOnuVlanAggregationEntry=_ZxAnEponOnuVlanAggregationEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,5,1))
zxAnEponOnuVlanAggregationEntry.setIndexNames((0,_E,_F),(0,_E,_H),(0,_E,_t))
if mibBuilder.loadTexts:zxAnEponOnuVlanAggregationEntry.setStatus(_A)
class _ZxAnEponOnuVlanAggGrpId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ZxAnEponOnuVlanAggGrpId_Type.__name__=_B
_ZxAnEponOnuVlanAggGrpId_Object=MibTableColumn
zxAnEponOnuVlanAggGrpId=_ZxAnEponOnuVlanAggGrpId_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,5,1,1),_ZxAnEponOnuVlanAggGrpId_Type())
zxAnEponOnuVlanAggGrpId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuVlanAggGrpId.setStatus(_A)
_ZxAnEponOnuVlamAggSrcVlanList_Type=DisplayString
_ZxAnEponOnuVlamAggSrcVlanList_Object=MibTableColumn
zxAnEponOnuVlamAggSrcVlanList=_ZxAnEponOnuVlamAggSrcVlanList_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,5,1,2),_ZxAnEponOnuVlamAggSrcVlanList_Type())
zxAnEponOnuVlamAggSrcVlanList.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuVlamAggSrcVlanList.setStatus(_A)
class _ZxAnEponOnuVlanAggDestVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnEponOnuVlanAggDestVlan_Type.__name__=_B
_ZxAnEponOnuVlanAggDestVlan_Object=MibTableColumn
zxAnEponOnuVlanAggDestVlan=_ZxAnEponOnuVlanAggDestVlan_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,5,1,3),_ZxAnEponOnuVlanAggDestVlan_Type())
zxAnEponOnuVlanAggDestVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuVlanAggDestVlan.setStatus(_A)
_ZxAnEponOnuVlanAggRowStatus_Type=RowStatus
_ZxAnEponOnuVlanAggRowStatus_Object=MibTableColumn
zxAnEponOnuVlanAggRowStatus=_ZxAnEponOnuVlanAggRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,10,5,1,10),_ZxAnEponOnuVlanAggRowStatus_Type())
zxAnEponOnuVlanAggRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuVlanAggRowStatus.setStatus(_A)
_ZxAnEponOnuClassMarkingAttrMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuClassMarkingAttrMgmt=_ZxAnEponOnuClassMarkingAttrMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,1,11))
_ZxAnEponOnuClassMarkingConditionTable_Object=MibTable
zxAnEponOnuClassMarkingConditionTable=_ZxAnEponOnuClassMarkingConditionTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,1))
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingConditionTable.setStatus(_A)
_ZxAnEponOnuClassMarkingConditionEntry_Object=MibTableRow
zxAnEponOnuClassMarkingConditionEntry=_ZxAnEponOnuClassMarkingConditionEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,1,1))
zxAnEponOnuClassMarkingConditionEntry.setIndexNames((0,_E,_F),(0,_E,_u))
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingConditionEntry.setStatus(_A)
_ZxAnEponOnuClassMarkingConditionId_Type=Integer32
_ZxAnEponOnuClassMarkingConditionId_Object=MibTableColumn
zxAnEponOnuClassMarkingConditionId=_ZxAnEponOnuClassMarkingConditionId_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,1,1,1),_ZxAnEponOnuClassMarkingConditionId_Type())
zxAnEponOnuClassMarkingConditionId.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingConditionId.setStatus(_A)
class _ZxAnEponOnuClassMarkingConditionName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnEponOnuClassMarkingConditionName_Type.__name__=_N
_ZxAnEponOnuClassMarkingConditionName_Object=MibTableColumn
zxAnEponOnuClassMarkingConditionName=_ZxAnEponOnuClassMarkingConditionName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,1,1,2),_ZxAnEponOnuClassMarkingConditionName_Type())
zxAnEponOnuClassMarkingConditionName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingConditionName.setStatus(_A)
class _ZxAnEponOnuClassMarkingField_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('da',1),('sa',2),('priority',3),('vlan',4),('ethType',5),('destIp',6),('srcIp',7),('ipProtType',8),('ipV4',9),('ipV6',10),('l4SrcPort',11),('l4DestPort',12),('linkIndex',13),('ipPrecedence',14)))
_ZxAnEponOnuClassMarkingField_Type.__name__=_B
_ZxAnEponOnuClassMarkingField_Object=MibTableColumn
zxAnEponOnuClassMarkingField=_ZxAnEponOnuClassMarkingField_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,1,1,3),_ZxAnEponOnuClassMarkingField_Type())
zxAnEponOnuClassMarkingField.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingField.setStatus(_A)
class _ZxAnEponOnuClassMarkingMatchValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_ZxAnEponOnuClassMarkingMatchValue_Type.__name__=_N
_ZxAnEponOnuClassMarkingMatchValue_Object=MibTableColumn
zxAnEponOnuClassMarkingMatchValue=_ZxAnEponOnuClassMarkingMatchValue_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,1,1,4),_ZxAnEponOnuClassMarkingMatchValue_Type())
zxAnEponOnuClassMarkingMatchValue.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingMatchValue.setStatus(_A)
class _ZxAnEponOnuClassMarkingOperator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('never-match',1),('equal',2),('not-equal',3),('less-and-equal',4),('greater-and-equal',5),('exist',6),('not-exist',7),('always-match',8)))
_ZxAnEponOnuClassMarkingOperator_Type.__name__=_B
_ZxAnEponOnuClassMarkingOperator_Object=MibTableColumn
zxAnEponOnuClassMarkingOperator=_ZxAnEponOnuClassMarkingOperator_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,1,1,5),_ZxAnEponOnuClassMarkingOperator_Type())
zxAnEponOnuClassMarkingOperator.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingOperator.setStatus(_A)
_ZxAnEponOnuClassMarkingConditionRefCnt_Type=Integer32
_ZxAnEponOnuClassMarkingConditionRefCnt_Object=MibTableColumn
zxAnEponOnuClassMarkingConditionRefCnt=_ZxAnEponOnuClassMarkingConditionRefCnt_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,1,1,6),_ZxAnEponOnuClassMarkingConditionRefCnt_Type())
zxAnEponOnuClassMarkingConditionRefCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingConditionRefCnt.setStatus(_A)
_ZxAnEponOnuClassMarkingConditionRowStatus_Type=RowStatus
_ZxAnEponOnuClassMarkingConditionRowStatus_Object=MibTableColumn
zxAnEponOnuClassMarkingConditionRowStatus=_ZxAnEponOnuClassMarkingConditionRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,1,1,7),_ZxAnEponOnuClassMarkingConditionRowStatus_Type())
zxAnEponOnuClassMarkingConditionRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingConditionRowStatus.setStatus(_A)
_ZxAnEponOnuClassMarkingRuleTable_Object=MibTable
zxAnEponOnuClassMarkingRuleTable=_ZxAnEponOnuClassMarkingRuleTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,2))
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingRuleTable.setStatus(_A)
_ZxAnEponOnuClassMarkingRuleEntry_Object=MibTableRow
zxAnEponOnuClassMarkingRuleEntry=_ZxAnEponOnuClassMarkingRuleEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,2,1))
zxAnEponOnuClassMarkingRuleEntry.setIndexNames((0,_E,_F),(0,_E,_v))
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingRuleEntry.setStatus(_A)
_ZxAnEponOnuClassMarkingRuleId_Type=Integer32
_ZxAnEponOnuClassMarkingRuleId_Object=MibTableColumn
zxAnEponOnuClassMarkingRuleId=_ZxAnEponOnuClassMarkingRuleId_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,2,1,1),_ZxAnEponOnuClassMarkingRuleId_Type())
zxAnEponOnuClassMarkingRuleId.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingRuleId.setStatus(_A)
class _ZxAnEponOnuClassMarkingRuleName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnEponOnuClassMarkingRuleName_Type.__name__=_N
_ZxAnEponOnuClassMarkingRuleName_Object=MibTableColumn
zxAnEponOnuClassMarkingRuleName=_ZxAnEponOnuClassMarkingRuleName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,2,1,2),_ZxAnEponOnuClassMarkingRuleName_Type())
zxAnEponOnuClassMarkingRuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingRuleName.setStatus(_A)
_ZxAnEponOnuClassMarkingQueue_Type=Integer32
_ZxAnEponOnuClassMarkingQueue_Object=MibTableColumn
zxAnEponOnuClassMarkingQueue=_ZxAnEponOnuClassMarkingQueue_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,2,1,3),_ZxAnEponOnuClassMarkingQueue_Type())
zxAnEponOnuClassMarkingQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingQueue.setStatus(_A)
class _ZxAnEponOnuClassMarkingPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnEponOnuClassMarkingPriority_Type.__name__=_B
_ZxAnEponOnuClassMarkingPriority_Object=MibTableColumn
zxAnEponOnuClassMarkingPriority=_ZxAnEponOnuClassMarkingPriority_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,2,1,4),_ZxAnEponOnuClassMarkingPriority_Type())
zxAnEponOnuClassMarkingPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingPriority.setStatus(_A)
_ZxAnEponOnuClassMarkingRuleRefCnt_Type=Integer32
_ZxAnEponOnuClassMarkingRuleRefCnt_Object=MibTableColumn
zxAnEponOnuClassMarkingRuleRefCnt=_ZxAnEponOnuClassMarkingRuleRefCnt_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,2,1,5),_ZxAnEponOnuClassMarkingRuleRefCnt_Type())
zxAnEponOnuClassMarkingRuleRefCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingRuleRefCnt.setStatus(_A)
_ZxAnEponOnuClassMarkingRuleRowStatus_Type=RowStatus
_ZxAnEponOnuClassMarkingRuleRowStatus_Object=MibTableColumn
zxAnEponOnuClassMarkingRuleRowStatus=_ZxAnEponOnuClassMarkingRuleRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,2,1,6),_ZxAnEponOnuClassMarkingRuleRowStatus_Type())
zxAnEponOnuClassMarkingRuleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingRuleRowStatus.setStatus(_A)
_ZxAnEponOnuClassMarkingTable_Object=MibTable
zxAnEponOnuClassMarkingTable=_ZxAnEponOnuClassMarkingTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,3))
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingTable.setStatus(_A)
_ZxAnEponOnuClassMarkingEntry_Object=MibTableRow
zxAnEponOnuClassMarkingEntry=_ZxAnEponOnuClassMarkingEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,3,1))
zxAnEponOnuClassMarkingEntry.setIndexNames((0,_E,_F),(0,_E,_H),(0,_E,_w))
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingEntry.setStatus(_A)
_ZxAnEponOnuClassMarkingRulePrecedence_Type=Integer32
_ZxAnEponOnuClassMarkingRulePrecedence_Object=MibTableColumn
zxAnEponOnuClassMarkingRulePrecedence=_ZxAnEponOnuClassMarkingRulePrecedence_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,3,1,1),_ZxAnEponOnuClassMarkingRulePrecedence_Type())
zxAnEponOnuClassMarkingRulePrecedence.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingRulePrecedence.setStatus(_A)
_ZxAnEponOnuClassMarkingRuleIndex_Type=Integer32
_ZxAnEponOnuClassMarkingRuleIndex_Object=MibTableColumn
zxAnEponOnuClassMarkingRuleIndex=_ZxAnEponOnuClassMarkingRuleIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,3,1,2),_ZxAnEponOnuClassMarkingRuleIndex_Type())
zxAnEponOnuClassMarkingRuleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingRuleIndex.setStatus(_A)
_ZxAnEponOnuClassMarkingRuleConditionList_Type=OctetString
_ZxAnEponOnuClassMarkingRuleConditionList_Object=MibTableColumn
zxAnEponOnuClassMarkingRuleConditionList=_ZxAnEponOnuClassMarkingRuleConditionList_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,3,1,3),_ZxAnEponOnuClassMarkingRuleConditionList_Type())
zxAnEponOnuClassMarkingRuleConditionList.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingRuleConditionList.setStatus(_A)
_ZxAnEponOnuClassMarkingRowStatus_Type=RowStatus
_ZxAnEponOnuClassMarkingRowStatus_Object=MibTableColumn
zxAnEponOnuClassMarkingRowStatus=_ZxAnEponOnuClassMarkingRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,3,1,4),_ZxAnEponOnuClassMarkingRowStatus_Type())
zxAnEponOnuClassMarkingRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingRowStatus.setStatus(_A)
_ZxAnEponOnuClassMarkingRulePriority_Type=Integer32
_ZxAnEponOnuClassMarkingRulePriority_Object=MibTableColumn
zxAnEponOnuClassMarkingRulePriority=_ZxAnEponOnuClassMarkingRulePriority_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,3,1,5),_ZxAnEponOnuClassMarkingRulePriority_Type())
zxAnEponOnuClassMarkingRulePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingRulePriority.setStatus(_A)
class _ZxAnEponOnuClassMarkingRuleDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('downstream',1),('upstream',2)))
_ZxAnEponOnuClassMarkingRuleDirection_Type.__name__=_B
_ZxAnEponOnuClassMarkingRuleDirection_Object=MibTableColumn
zxAnEponOnuClassMarkingRuleDirection=_ZxAnEponOnuClassMarkingRuleDirection_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,3,1,6),_ZxAnEponOnuClassMarkingRuleDirection_Type())
zxAnEponOnuClassMarkingRuleDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingRuleDirection.setStatus(_A)
class _ZxAnEponOnuClassMarkingRuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('classification',1),(_x,2)))
_ZxAnEponOnuClassMarkingRuleType_Type.__name__=_B
_ZxAnEponOnuClassMarkingRuleType_Object=MibTableColumn
zxAnEponOnuClassMarkingRuleType=_ZxAnEponOnuClassMarkingRuleType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,3,1,7),_ZxAnEponOnuClassMarkingRuleType_Type())
zxAnEponOnuClassMarkingRuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingRuleType.setStatus(_A)
_ZxAnEponOnuClassMarkingClearTable_Object=MibTable
zxAnEponOnuClassMarkingClearTable=_ZxAnEponOnuClassMarkingClearTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,4))
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingClearTable.setStatus(_A)
_ZxAnEponOnuClassMarkingClearEntry_Object=MibTableRow
zxAnEponOnuClassMarkingClearEntry=_ZxAnEponOnuClassMarkingClearEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,4,1))
zxAnEponOnuClassMarkingClearEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingClearEntry.setStatus(_A)
_ZxAnEponOnuClassMarkingClear_Type=Integer32
_ZxAnEponOnuClassMarkingClear_Object=MibTableColumn
zxAnEponOnuClassMarkingClear=_ZxAnEponOnuClassMarkingClear_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,4,1,1),_ZxAnEponOnuClassMarkingClear_Type())
zxAnEponOnuClassMarkingClear.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingClear.setStatus(_A)
_ZxAnEponOnuClassMarkingCompatibilityTable_Object=MibTable
zxAnEponOnuClassMarkingCompatibilityTable=_ZxAnEponOnuClassMarkingCompatibilityTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,101))
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingCompatibilityTable.setStatus(_A)
_ZxAnEponOnuClassMarkingCompatibilityEntry_Object=MibTableRow
zxAnEponOnuClassMarkingCompatibilityEntry=_ZxAnEponOnuClassMarkingCompatibilityEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,101,1))
zxAnEponOnuClassMarkingCompatibilityEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingCompatibilityEntry.setStatus(_A)
class _ZxAnEponOnuClassMarkingRulePriorityFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuClassMarkingRulePriorityFlag_Type.__name__=_B
_ZxAnEponOnuClassMarkingRulePriorityFlag_Object=MibTableColumn
zxAnEponOnuClassMarkingRulePriorityFlag=_ZxAnEponOnuClassMarkingRulePriorityFlag_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,101,1,1),_ZxAnEponOnuClassMarkingRulePriorityFlag_Type())
zxAnEponOnuClassMarkingRulePriorityFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingRulePriorityFlag.setStatus(_A)
class _ZxAnEponOnuClassMarkingRuleDirectionFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuClassMarkingRuleDirectionFlag_Type.__name__=_B
_ZxAnEponOnuClassMarkingRuleDirectionFlag_Object=MibTableColumn
zxAnEponOnuClassMarkingRuleDirectionFlag=_ZxAnEponOnuClassMarkingRuleDirectionFlag_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,101,1,2),_ZxAnEponOnuClassMarkingRuleDirectionFlag_Type())
zxAnEponOnuClassMarkingRuleDirectionFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingRuleDirectionFlag.setStatus(_A)
class _ZxAnEponOnuClassMarkingRuleTypeFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuClassMarkingRuleTypeFlag_Type.__name__=_B
_ZxAnEponOnuClassMarkingRuleTypeFlag_Object=MibTableColumn
zxAnEponOnuClassMarkingRuleTypeFlag=_ZxAnEponOnuClassMarkingRuleTypeFlag_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,11,101,1,3),_ZxAnEponOnuClassMarkingRuleTypeFlag_Type())
zxAnEponOnuClassMarkingRuleTypeFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingRuleTypeFlag.setStatus(_A)
_ZxAnEponOnuMulticastVlanTable_Object=MibTable
zxAnEponOnuMulticastVlanTable=_ZxAnEponOnuMulticastVlanTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,12))
if mibBuilder.loadTexts:zxAnEponOnuMulticastVlanTable.setStatus(_A)
_ZxAnEponOnuMulticastVlanEntry_Object=MibTableRow
zxAnEponOnuMulticastVlanEntry=_ZxAnEponOnuMulticastVlanEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,12,1))
zxAnEponOnuMulticastVlanEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuMulticastVlanEntry.setStatus(_A)
class _ZxAnEponOnuMulticastVlanAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_y,0),('add',1),('clear',2)))
_ZxAnEponOnuMulticastVlanAction_Type.__name__=_B
_ZxAnEponOnuMulticastVlanAction_Object=MibTableColumn
zxAnEponOnuMulticastVlanAction=_ZxAnEponOnuMulticastVlanAction_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,12,1,1),_ZxAnEponOnuMulticastVlanAction_Type())
zxAnEponOnuMulticastVlanAction.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuMulticastVlanAction.setStatus(_A)
_ZxAnEponOnuMulticastVlanList_Type=OctetString
_ZxAnEponOnuMulticastVlanList_Object=MibTableColumn
zxAnEponOnuMulticastVlanList=_ZxAnEponOnuMulticastVlanList_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,12,1,2),_ZxAnEponOnuMulticastVlanList_Type())
zxAnEponOnuMulticastVlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuMulticastVlanList.setStatus(_A)
_ZxAnEponOnuMulticastTagCfgTable_Object=MibTable
zxAnEponOnuMulticastTagCfgTable=_ZxAnEponOnuMulticastTagCfgTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,13))
if mibBuilder.loadTexts:zxAnEponOnuMulticastTagCfgTable.setStatus(_A)
_ZxAnEponOnuMulticastTagCfgEntry_Object=MibTableRow
zxAnEponOnuMulticastTagCfgEntry=_ZxAnEponOnuMulticastTagCfgEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,13,1))
zxAnEponOnuMulticastTagCfgEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuMulticastTagCfgEntry.setStatus(_A)
class _ZxAnEponOnuMulticastTagStripe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('not-striped',1),('striped',2),('tagSwitch',3)))
_ZxAnEponOnuMulticastTagStripe_Type.__name__=_B
_ZxAnEponOnuMulticastTagStripe_Object=MibTableColumn
zxAnEponOnuMulticastTagStripe=_ZxAnEponOnuMulticastTagStripe_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,13,1,1),_ZxAnEponOnuMulticastTagStripe_Type())
zxAnEponOnuMulticastTagStripe.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuMulticastTagStripe.setStatus(_A)
_ZxAnEponOnuMulticastSwitchTable_Object=MibTable
zxAnEponOnuMulticastSwitchTable=_ZxAnEponOnuMulticastSwitchTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,14))
if mibBuilder.loadTexts:zxAnEponOnuMulticastSwitchTable.setStatus(_A)
_ZxAnEponOnuMulticastSwitchEntry_Object=MibTableRow
zxAnEponOnuMulticastSwitchEntry=_ZxAnEponOnuMulticastSwitchEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,14,1))
zxAnEponOnuMulticastSwitchEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuMulticastSwitchEntry.setStatus(_A)
class _ZxAnEponOnuMulticastSwitchAttr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('igmpsnooping',1),('ctrl-multicast',2)))
_ZxAnEponOnuMulticastSwitchAttr_Type.__name__=_B
_ZxAnEponOnuMulticastSwitchAttr_Object=MibTableColumn
zxAnEponOnuMulticastSwitchAttr=_ZxAnEponOnuMulticastSwitchAttr_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,14,1,1),_ZxAnEponOnuMulticastSwitchAttr_Type())
zxAnEponOnuMulticastSwitchAttr.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuMulticastSwitchAttr.setStatus(_A)
_ZxAnEponOnuMulticastControlMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuMulticastControlMgmt=_ZxAnEponOnuMulticastControlMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,1,15))
_ZxAnEponOnuMulticastControlClearTable_Object=MibTable
zxAnEponOnuMulticastControlClearTable=_ZxAnEponOnuMulticastControlClearTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,15,1))
if mibBuilder.loadTexts:zxAnEponOnuMulticastControlClearTable.setStatus(_A)
_ZxAnEponOnuMulticastControlClearEntry_Object=MibTableRow
zxAnEponOnuMulticastControlClearEntry=_ZxAnEponOnuMulticastControlClearEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,15,1,1))
zxAnEponOnuMulticastControlClearEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuMulticastControlClearEntry.setStatus(_A)
_ZxAnEponOnuMcstCtrlClear_Type=Integer32
_ZxAnEponOnuMcstCtrlClear_Object=MibTableColumn
zxAnEponOnuMcstCtrlClear=_ZxAnEponOnuMcstCtrlClear_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,15,1,1,1),_ZxAnEponOnuMcstCtrlClear_Type())
zxAnEponOnuMcstCtrlClear.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuMcstCtrlClear.setStatus(_A)
_ZxAnEponOnuMulticastControlTable_Object=MibTable
zxAnEponOnuMulticastControlTable=_ZxAnEponOnuMulticastControlTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,15,2))
if mibBuilder.loadTexts:zxAnEponOnuMulticastControlTable.setStatus(_A)
_ZxAnEponOnuMulticastControlEntry_Object=MibTableRow
zxAnEponOnuMulticastControlEntry=_ZxAnEponOnuMulticastControlEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,15,2,1))
zxAnEponOnuMulticastControlEntry.setIndexNames((0,_E,_F),(0,_E,_z))
if mibBuilder.loadTexts:zxAnEponOnuMulticastControlEntry.setStatus(_A)
_ZxAnEponOnuMcstCtrlEntryIndex_Type=Integer32
_ZxAnEponOnuMcstCtrlEntryIndex_Object=MibTableColumn
zxAnEponOnuMcstCtrlEntryIndex=_ZxAnEponOnuMcstCtrlEntryIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,15,2,1,1),_ZxAnEponOnuMcstCtrlEntryIndex_Type())
zxAnEponOnuMcstCtrlEntryIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuMcstCtrlEntryIndex.setStatus(_A)
class _ZxAnEponOnuMcstCtrlAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_y,1),('add',2)))
_ZxAnEponOnuMcstCtrlAction_Type.__name__=_B
_ZxAnEponOnuMcstCtrlAction_Object=MibTableColumn
zxAnEponOnuMcstCtrlAction=_ZxAnEponOnuMcstCtrlAction_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,15,2,1,2),_ZxAnEponOnuMcstCtrlAction_Type())
zxAnEponOnuMcstCtrlAction.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuMcstCtrlAction.setStatus(_A)
class _ZxAnEponOnuMcstCtrlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('gda',1),('gda-and-vlan',2),('gda-and-sa',3),('gip-and-vlan',4)))
_ZxAnEponOnuMcstCtrlType_Type.__name__=_B
_ZxAnEponOnuMcstCtrlType_Object=MibTableColumn
zxAnEponOnuMcstCtrlType=_ZxAnEponOnuMcstCtrlType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,15,2,1,3),_ZxAnEponOnuMcstCtrlType_Type())
zxAnEponOnuMcstCtrlType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuMcstCtrlType.setStatus(_A)
class _ZxAnEponOnuMcstCtrlUserId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnEponOnuMcstCtrlUserId_Type.__name__=_B
_ZxAnEponOnuMcstCtrlUserId_Object=MibTableColumn
zxAnEponOnuMcstCtrlUserId=_ZxAnEponOnuMcstCtrlUserId_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,15,2,1,4),_ZxAnEponOnuMcstCtrlUserId_Type())
zxAnEponOnuMcstCtrlUserId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuMcstCtrlUserId.setStatus(_A)
_ZxAnEponOnuMcstCtrlGda_Type=MacAddress
_ZxAnEponOnuMcstCtrlGda_Object=MibTableColumn
zxAnEponOnuMcstCtrlGda=_ZxAnEponOnuMcstCtrlGda_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,15,2,1,5),_ZxAnEponOnuMcstCtrlGda_Type())
zxAnEponOnuMcstCtrlGda.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuMcstCtrlGda.setStatus(_A)
class _ZxAnEponOnuMcstCtrlMvlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnEponOnuMcstCtrlMvlan_Type.__name__=_B
_ZxAnEponOnuMcstCtrlMvlan_Object=MibTableColumn
zxAnEponOnuMcstCtrlMvlan=_ZxAnEponOnuMcstCtrlMvlan_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,15,2,1,6),_ZxAnEponOnuMcstCtrlMvlan_Type())
zxAnEponOnuMcstCtrlMvlan.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuMcstCtrlMvlan.setStatus(_A)
_ZxAnEponOnuMcstCtrlGdaIp_Type=IpAddress
_ZxAnEponOnuMcstCtrlGdaIp_Object=MibTableColumn
zxAnEponOnuMcstCtrlGdaIp=_ZxAnEponOnuMcstCtrlGdaIp_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,15,2,1,7),_ZxAnEponOnuMcstCtrlGdaIp_Type())
zxAnEponOnuMcstCtrlGdaIp.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuMcstCtrlGdaIp.setStatus(_A)
_ZxAnEponOnuMaxGroupNumTable_Object=MibTable
zxAnEponOnuMaxGroupNumTable=_ZxAnEponOnuMaxGroupNumTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,16))
if mibBuilder.loadTexts:zxAnEponOnuMaxGroupNumTable.setStatus(_A)
_ZxAnEponOnuMaxGroupNumEntry_Object=MibTableRow
zxAnEponOnuMaxGroupNumEntry=_ZxAnEponOnuMaxGroupNumEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,16,1))
zxAnEponOnuMaxGroupNumEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuMaxGroupNumEntry.setStatus(_A)
class _ZxAnEponOnuMaxGroupNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnEponOnuMaxGroupNum_Type.__name__=_B
_ZxAnEponOnuMaxGroupNum_Object=MibTableColumn
zxAnEponOnuMaxGroupNum=_ZxAnEponOnuMaxGroupNum_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,16,1,1),_ZxAnEponOnuMaxGroupNum_Type())
zxAnEponOnuMaxGroupNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuMaxGroupNum.setStatus(_A)
_ZxAnEponOnuAlarmCtrlTable_Object=MibTable
zxAnEponOnuAlarmCtrlTable=_ZxAnEponOnuAlarmCtrlTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,17))
if mibBuilder.loadTexts:zxAnEponOnuAlarmCtrlTable.setStatus(_A)
_ZxAnEponOnuAlarmCtrlEntry_Object=MibTableRow
zxAnEponOnuAlarmCtrlEntry=_ZxAnEponOnuAlarmCtrlEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,17,1))
zxAnEponOnuAlarmCtrlEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuAlarmCtrlEntry.setStatus(_A)
class _ZxAnEponOnuAlarmCtr_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZxAnEponOnuAlarmCtr_Type.__name__=_B
_ZxAnEponOnuAlarmCtr_Object=MibTableColumn
zxAnEponOnuAlarmCtr=_ZxAnEponOnuAlarmCtr_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,17,1,1),_ZxAnEponOnuAlarmCtr_Type())
zxAnEponOnuAlarmCtr.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuAlarmCtr.setStatus(_A)
_ZxAnEponOnuMACNumTable_Object=MibTable
zxAnEponOnuMACNumTable=_ZxAnEponOnuMACNumTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,18))
if mibBuilder.loadTexts:zxAnEponOnuMACNumTable.setStatus(_A)
_ZxAnEponOnuMACNumEntry_Object=MibTableRow
zxAnEponOnuMACNumEntry=_ZxAnEponOnuMACNumEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,18,1))
zxAnEponOnuMACNumEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuMACNumEntry.setStatus(_A)
class _ZxAnEponOnuMACNum_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnEponOnuMACNum_Type.__name__=_B
_ZxAnEponOnuMACNum_Object=MibTableColumn
zxAnEponOnuMACNum=_ZxAnEponOnuMACNum_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,18,1,1),_ZxAnEponOnuMACNum_Type())
zxAnEponOnuMACNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuMACNum.setStatus(_A)
class _ZxAnEponOnuUniLearnedMacs_Type(Integer32):defaultValue=0
_ZxAnEponOnuUniLearnedMacs_Type.__name__=_B
_ZxAnEponOnuUniLearnedMacs_Object=MibTableColumn
zxAnEponOnuUniLearnedMacs=_ZxAnEponOnuUniLearnedMacs_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,18,1,2),_ZxAnEponOnuUniLearnedMacs_Type())
zxAnEponOnuUniLearnedMacs.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuUniLearnedMacs.setStatus(_A)
_ZxAnEponOnuMACAgingTimeTable_Object=MibTable
zxAnEponOnuMACAgingTimeTable=_ZxAnEponOnuMACAgingTimeTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,19))
if mibBuilder.loadTexts:zxAnEponOnuMACAgingTimeTable.setStatus(_A)
_ZxAnEponOnuMACAgingTimeEntry_Object=MibTableRow
zxAnEponOnuMACAgingTimeEntry=_ZxAnEponOnuMACAgingTimeEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,19,1))
zxAnEponOnuMACAgingTimeEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuMACAgingTimeEntry.setStatus(_A)
class _ZxAnEponOnuMACAgingTimeAttr_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,86400))
_ZxAnEponOnuMACAgingTimeAttr_Type.__name__=_B
_ZxAnEponOnuMACAgingTimeAttr_Object=MibTableColumn
zxAnEponOnuMACAgingTimeAttr=_ZxAnEponOnuMACAgingTimeAttr_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,19,1,1),_ZxAnEponOnuMACAgingTimeAttr_Type())
zxAnEponOnuMACAgingTimeAttr.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuMACAgingTimeAttr.setStatus(_A)
_ZxAnEponOnuFilterMACTable_Object=MibTable
zxAnEponOnuFilterMACTable=_ZxAnEponOnuFilterMACTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,20))
if mibBuilder.loadTexts:zxAnEponOnuFilterMACTable.setStatus(_A)
_ZxAnEponOnuFilterMACEntry_Object=MibTableRow
zxAnEponOnuFilterMACEntry=_ZxAnEponOnuFilterMACEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,20,1))
zxAnEponOnuFilterMACEntry.setIndexNames((0,_E,_F),(0,_E,_H),(0,_E,_A0),(0,_E,_A1))
if mibBuilder.loadTexts:zxAnEponOnuFilterMACEntry.setStatus(_A)
_ZxAnEponOnuFilterMAC_Type=MacAddress
_ZxAnEponOnuFilterMAC_Object=MibTableColumn
zxAnEponOnuFilterMAC=_ZxAnEponOnuFilterMAC_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,20,1,1),_ZxAnEponOnuFilterMAC_Type())
zxAnEponOnuFilterMAC.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuFilterMAC.setStatus(_A)
class _ZxEponFilterVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxEponFilterVlan_Type.__name__=_B
_ZxEponFilterVlan_Object=MibTableColumn
zxEponFilterVlan=_ZxEponFilterVlan_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,20,1,2),_ZxEponFilterVlan_Type())
zxEponFilterVlan.setMaxAccess(_I)
if mibBuilder.loadTexts:zxEponFilterVlan.setStatus(_A)
_ZxAnEponOnuFilterMACEntryStatus_Type=RowStatus
_ZxAnEponOnuFilterMACEntryStatus_Object=MibTableColumn
zxAnEponOnuFilterMACEntryStatus=_ZxAnEponOnuFilterMACEntryStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,20,1,3),_ZxAnEponOnuFilterMACEntryStatus_Type())
zxAnEponOnuFilterMACEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuFilterMACEntryStatus.setStatus(_A)
_ZxAnEponOnuBindMACTable_Object=MibTable
zxAnEponOnuBindMACTable=_ZxAnEponOnuBindMACTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,21))
if mibBuilder.loadTexts:zxAnEponOnuBindMACTable.setStatus(_A)
_ZxAnEponOnuBindMACEntry_Object=MibTableRow
zxAnEponOnuBindMACEntry=_ZxAnEponOnuBindMACEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,21,1))
zxAnEponOnuBindMACEntry.setIndexNames((0,_E,_F),(0,_E,_H),(0,_E,_A2),(0,_E,_A3))
if mibBuilder.loadTexts:zxAnEponOnuBindMACEntry.setStatus(_A)
_ZxAnEponOnuBindMAC_Type=MacAddress
_ZxAnEponOnuBindMAC_Object=MibTableColumn
zxAnEponOnuBindMAC=_ZxAnEponOnuBindMAC_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,21,1,1),_ZxAnEponOnuBindMAC_Type())
zxAnEponOnuBindMAC.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuBindMAC.setStatus(_A)
class _ZxEponBindVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxEponBindVlan_Type.__name__=_B
_ZxEponBindVlan_Object=MibTableColumn
zxEponBindVlan=_ZxEponBindVlan_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,21,1,2),_ZxEponBindVlan_Type())
zxEponBindVlan.setMaxAccess(_I)
if mibBuilder.loadTexts:zxEponBindVlan.setStatus(_A)
_ZxAnEponOnuBindMACEntryStatus_Type=RowStatus
_ZxAnEponOnuBindMACEntryStatus_Object=MibTableColumn
zxAnEponOnuBindMACEntryStatus=_ZxAnEponOnuBindMACEntryStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,21,1,3),_ZxAnEponOnuBindMACEntryStatus_Type())
zxAnEponOnuBindMACEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuBindMACEntryStatus.setStatus(_A)
_ZxAnEponOnuStaticMACTable_Object=MibTable
zxAnEponOnuStaticMACTable=_ZxAnEponOnuStaticMACTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,22))
if mibBuilder.loadTexts:zxAnEponOnuStaticMACTable.setStatus(_A)
_ZxAnEponOnuStaticMACEntry_Object=MibTableRow
zxAnEponOnuStaticMACEntry=_ZxAnEponOnuStaticMACEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,22,1))
zxAnEponOnuStaticMACEntry.setIndexNames((0,_E,_F),(0,_E,_H),(0,_E,_A4),(0,_E,_A5))
if mibBuilder.loadTexts:zxAnEponOnuStaticMACEntry.setStatus(_A)
_ZxAnEponOnuStaticMAC_Type=MacAddress
_ZxAnEponOnuStaticMAC_Object=MibTableColumn
zxAnEponOnuStaticMAC=_ZxAnEponOnuStaticMAC_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,22,1,1),_ZxAnEponOnuStaticMAC_Type())
zxAnEponOnuStaticMAC.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuStaticMAC.setStatus(_A)
class _ZxEponStaticVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxEponStaticVlan_Type.__name__=_B
_ZxEponStaticVlan_Object=MibTableColumn
zxEponStaticVlan=_ZxEponStaticVlan_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,22,1,2),_ZxEponStaticVlan_Type())
zxEponStaticVlan.setMaxAccess(_I)
if mibBuilder.loadTexts:zxEponStaticVlan.setStatus(_A)
_ZxAnEponOnuStaicMACEntryStatus_Type=RowStatus
_ZxAnEponOnuStaicMACEntryStatus_Object=MibTableColumn
zxAnEponOnuStaicMACEntryStatus=_ZxAnEponOnuStaicMACEntryStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,22,1,3),_ZxAnEponOnuStaicMACEntryStatus_Type())
zxAnEponOnuStaicMACEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuStaicMACEntryStatus.setStatus(_A)
_ZxAnEponOnuMACAddressClearTable_Object=MibTable
zxAnEponOnuMACAddressClearTable=_ZxAnEponOnuMACAddressClearTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,23))
if mibBuilder.loadTexts:zxAnEponOnuMACAddressClearTable.setStatus(_A)
_ZxAnEponOnuMACAddressClearEntry_Object=MibTableRow
zxAnEponOnuMACAddressClearEntry=_ZxAnEponOnuMACAddressClearEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,23,1))
zxAnEponOnuMACAddressClearEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuMACAddressClearEntry.setStatus(_A)
class _ZxAnEponOnuMACAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_x,1),('bind',2),(_V,3)))
_ZxAnEponOnuMACAddressType_Type.__name__=_B
_ZxAnEponOnuMACAddressType_Object=MibTableColumn
zxAnEponOnuMACAddressType=_ZxAnEponOnuMACAddressType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,23,1,1),_ZxAnEponOnuMACAddressType_Type())
zxAnEponOnuMACAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuMACAddressType.setStatus(_A)
_ZxAnEponOnuManagerIPTable_Object=MibTable
zxAnEponOnuManagerIPTable=_ZxAnEponOnuManagerIPTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,24))
if mibBuilder.loadTexts:zxAnEponOnuManagerIPTable.setStatus(_A)
_ZxAnEponOnuManagerIPTableEntry_Object=MibTableRow
zxAnEponOnuManagerIPTableEntry=_ZxAnEponOnuManagerIPTableEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,24,1))
zxAnEponOnuManagerIPTableEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuManagerIPTableEntry.setStatus(_A)
_ZxEponOnuIPAddress_Type=IpAddress
_ZxEponOnuIPAddress_Object=MibTableColumn
zxEponOnuIPAddress=_ZxEponOnuIPAddress_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,24,1,1),_ZxEponOnuIPAddress_Type())
zxEponOnuIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponOnuIPAddress.setStatus(_A)
_ZxEponOnuIPMask_Type=IpAddress
_ZxEponOnuIPMask_Object=MibTableColumn
zxEponOnuIPMask=_ZxEponOnuIPMask_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,24,1,2),_ZxEponOnuIPMask_Type())
zxEponOnuIPMask.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponOnuIPMask.setStatus(_A)
class _ZxEponMangementPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxEponMangementPriority_Type.__name__=_B
_ZxEponMangementPriority_Object=MibTableColumn
zxEponMangementPriority=_ZxEponMangementPriority_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,24,1,3),_ZxEponMangementPriority_Type())
zxEponMangementPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponMangementPriority.setStatus(_A)
class _ZxEponMangementVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxEponMangementVlan_Type.__name__=_B
_ZxEponMangementVlan_Object=MibTableColumn
zxEponMangementVlan=_ZxEponMangementVlan_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,24,1,4),_ZxEponMangementVlan_Type())
zxEponMangementVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponMangementVlan.setStatus(_A)
_ZxEponManagementHostIP_Type=IpAddress
_ZxEponManagementHostIP_Object=MibTableColumn
zxEponManagementHostIP=_ZxEponManagementHostIP_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,24,1,5),_ZxEponManagementHostIP_Type())
zxEponManagementHostIP.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponManagementHostIP.setStatus(_A)
_ZxEponManagementHostMask_Type=IpAddress
_ZxEponManagementHostMask_Object=MibTableColumn
zxEponManagementHostMask=_ZxEponManagementHostMask_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,24,1,6),_ZxEponManagementHostMask_Type())
zxEponManagementHostMask.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponManagementHostMask.setStatus(_A)
_ZxEponManagementGateway_Type=IpAddress
_ZxEponManagementGateway_Object=MibTableColumn
zxEponManagementGateway=_ZxEponManagementGateway_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,24,1,7),_ZxEponManagementGateway_Type())
zxEponManagementGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponManagementGateway.setStatus(_A)
class _ZxEponOnuIPConfigureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZxEponOnuIPConfigureStatus_Type.__name__=_B
_ZxEponOnuIPConfigureStatus_Object=MibTableColumn
zxEponOnuIPConfigureStatus=_ZxEponOnuIPConfigureStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,24,1,8),_ZxEponOnuIPConfigureStatus_Type())
zxEponOnuIPConfigureStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponOnuIPConfigureStatus.setStatus(_A)
class _ZxEponMangementSVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxEponMangementSVlan_Type.__name__=_B
_ZxEponMangementSVlan_Object=MibTableColumn
zxEponMangementSVlan=_ZxEponMangementSVlan_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,24,1,9),_ZxEponMangementSVlan_Type())
zxEponMangementSVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponMangementSVlan.setStatus(_A)
_ZxAnEponOnuIsolationCtrlTable_Object=MibTable
zxAnEponOnuIsolationCtrlTable=_ZxAnEponOnuIsolationCtrlTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,25))
if mibBuilder.loadTexts:zxAnEponOnuIsolationCtrlTable.setStatus(_A)
_ZxAnEponOnuIsolationCtrlEntry_Object=MibTableRow
zxAnEponOnuIsolationCtrlEntry=_ZxAnEponOnuIsolationCtrlEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,25,1))
zxAnEponOnuIsolationCtrlEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuIsolationCtrlEntry.setStatus(_A)
class _ZxAnEponOnuIsolationCtr_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZxAnEponOnuIsolationCtr_Type.__name__=_B
_ZxAnEponOnuIsolationCtr_Object=MibTableColumn
zxAnEponOnuIsolationCtr=_ZxAnEponOnuIsolationCtr_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,25,1,1),_ZxAnEponOnuIsolationCtr_Type())
zxAnEponOnuIsolationCtr.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuIsolationCtr.setStatus(_A)
_ZxAnEponRmFastLeaveAbiTable_Object=MibTable
zxAnEponRmFastLeaveAbiTable=_ZxAnEponRmFastLeaveAbiTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,26))
if mibBuilder.loadTexts:zxAnEponRmFastLeaveAbiTable.setStatus(_A)
_ZxAnEponRmFastLeaveAbiEntry_Object=MibTableRow
zxAnEponRmFastLeaveAbiEntry=_ZxAnEponRmFastLeaveAbiEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,26,1))
zxAnEponRmFastLeaveAbiEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponRmFastLeaveAbiEntry.setStatus(_A)
_Fastleaveabi_Type=Integer32
_Fastleaveabi_Object=MibTableColumn
fastleaveabi=_Fastleaveabi_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,26,1,1),_Fastleaveabi_Type())
fastleaveabi.setMaxAccess(_D)
if mibBuilder.loadTexts:fastleaveabi.setStatus(_A)
_EponRmFastLeaveAdminStateTable_Object=MibTable
eponRmFastLeaveAdminStateTable=_EponRmFastLeaveAdminStateTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,27))
if mibBuilder.loadTexts:eponRmFastLeaveAdminStateTable.setStatus(_A)
_EponRmFastLeaveAdminStateEntry_Object=MibTableRow
eponRmFastLeaveAdminStateEntry=_EponRmFastLeaveAdminStateEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,27,1))
eponRmFastLeaveAdminStateEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:eponRmFastLeaveAdminStateEntry.setStatus(_A)
class _GetState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noResult',0),(_J,1),(_K,2)))
_GetState_Type.__name__=_B
_GetState_Object=MibTableColumn
getState=_GetState_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,27,1,1),_GetState_Type())
getState.setMaxAccess(_C)
if mibBuilder.loadTexts:getState.setStatus(_A)
_EponIpGlobalTable_Object=MibTable
eponIpGlobalTable=_EponIpGlobalTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,28))
if mibBuilder.loadTexts:eponIpGlobalTable.setStatus(_A)
_EponIpGlobalEntry_Object=MibTableRow
eponIpGlobalEntry=_EponIpGlobalEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,28,1))
eponIpGlobalEntry.setIndexNames((0,_E,_F),(0,_E,_A6))
if mibBuilder.loadTexts:eponIpGlobalEntry.setStatus(_A)
_ZxAnEponOnuVioceCardIndex_Type=Integer32
_ZxAnEponOnuVioceCardIndex_Object=MibTableColumn
zxAnEponOnuVioceCardIndex=_ZxAnEponOnuVioceCardIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,28,1,1),_ZxAnEponOnuVioceCardIndex_Type())
zxAnEponOnuVioceCardIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuVioceCardIndex.setStatus(_A)
class _ZxAnEponOnuVoiceIpMngIpRelation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('standalone',1),('useVOIPIP',2)))
_ZxAnEponOnuVoiceIpMngIpRelation_Type.__name__=_B
_ZxAnEponOnuVoiceIpMngIpRelation_Object=MibTableColumn
zxAnEponOnuVoiceIpMngIpRelation=_ZxAnEponOnuVoiceIpMngIpRelation_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,28,1,2),_ZxAnEponOnuVoiceIpMngIpRelation_Type())
zxAnEponOnuVoiceIpMngIpRelation.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoiceIpMngIpRelation.setStatus(_A)
class _ZxAnEponOnuVoiceIpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_V,1),(_c,2),(_d,3)))
_ZxAnEponOnuVoiceIpMode_Type.__name__=_B
_ZxAnEponOnuVoiceIpMode_Object=MibTableColumn
zxAnEponOnuVoiceIpMode=_ZxAnEponOnuVoiceIpMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,28,1,3),_ZxAnEponOnuVoiceIpMode_Type())
zxAnEponOnuVoiceIpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoiceIpMode.setStatus(_A)
_ZxAnEponOnuVoiceIpAddress_Type=IpAddress
_ZxAnEponOnuVoiceIpAddress_Object=MibTableColumn
zxAnEponOnuVoiceIpAddress=_ZxAnEponOnuVoiceIpAddress_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,28,1,4),_ZxAnEponOnuVoiceIpAddress_Type())
zxAnEponOnuVoiceIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoiceIpAddress.setStatus(_A)
_ZxAnEponOnuVoiceDnsServer_Type=IpAddress
_ZxAnEponOnuVoiceDnsServer_Object=MibTableColumn
zxAnEponOnuVoiceDnsServer=_ZxAnEponOnuVoiceDnsServer_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,28,1,5),_ZxAnEponOnuVoiceDnsServer_Type())
zxAnEponOnuVoiceDnsServer.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoiceDnsServer.setStatus(_A)
_ZxAnEponOnuVoiceIpMask_Type=IpAddress
_ZxAnEponOnuVoiceIpMask_Object=MibTableColumn
zxAnEponOnuVoiceIpMask=_ZxAnEponOnuVoiceIpMask_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,28,1,6),_ZxAnEponOnuVoiceIpMask_Type())
zxAnEponOnuVoiceIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoiceIpMask.setStatus(_A)
_ZxAnEponOnuVoiceGateway_Type=IpAddress
_ZxAnEponOnuVoiceGateway_Object=MibTableColumn
zxAnEponOnuVoiceGateway=_ZxAnEponOnuVoiceGateway_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,28,1,7),_ZxAnEponOnuVoiceGateway_Type())
zxAnEponOnuVoiceGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoiceGateway.setStatus(_A)
class _ZxAnEponOnuVoicePPPoEMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_e,1),(_f,2),(_g,3)))
_ZxAnEponOnuVoicePPPoEMode_Type.__name__=_B
_ZxAnEponOnuVoicePPPoEMode_Object=MibTableColumn
zxAnEponOnuVoicePPPoEMode=_ZxAnEponOnuVoicePPPoEMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,28,1,8),_ZxAnEponOnuVoicePPPoEMode_Type())
zxAnEponOnuVoicePPPoEMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoicePPPoEMode.setStatus(_A)
_ZxAnEponOnuVoicePPPoEUserName_Type=DisplayString
_ZxAnEponOnuVoicePPPoEUserName_Object=MibTableColumn
zxAnEponOnuVoicePPPoEUserName=_ZxAnEponOnuVoicePPPoEUserName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,28,1,9),_ZxAnEponOnuVoicePPPoEUserName_Type())
zxAnEponOnuVoicePPPoEUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoicePPPoEUserName.setStatus(_A)
_ZxAnEponOnuVoicePPPoEPassword_Type=DisplayString
_ZxAnEponOnuVoicePPPoEPassword_Object=MibTableColumn
zxAnEponOnuVoicePPPoEPassword=_ZxAnEponOnuVoicePPPoEPassword_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,28,1,10),_ZxAnEponOnuVoicePPPoEPassword_Type())
zxAnEponOnuVoicePPPoEPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoicePPPoEPassword.setStatus(_A)
class _ZxAnEponOnuVoiceTaggedFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuVoiceTaggedFlag_Type.__name__=_B
_ZxAnEponOnuVoiceTaggedFlag_Object=MibTableColumn
zxAnEponOnuVoiceTaggedFlag=_ZxAnEponOnuVoiceTaggedFlag_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,28,1,11),_ZxAnEponOnuVoiceTaggedFlag_Type())
zxAnEponOnuVoiceTaggedFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoiceTaggedFlag.setStatus(_A)
_ZxAnEponOnuVoiceDataVlan_Type=Integer32
_ZxAnEponOnuVoiceDataVlan_Object=MibTableColumn
zxAnEponOnuVoiceDataVlan=_ZxAnEponOnuVoiceDataVlan_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,28,1,12),_ZxAnEponOnuVoiceDataVlan_Type())
zxAnEponOnuVoiceDataVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoiceDataVlan.setStatus(_A)
class _ZxAnEponOnuVoiceDataPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('pri0',1),('pri1',2),('pri2',3),('pri3',4),('pri4',5),('pri5',6),('pri6',7),('pri7',8)))
_ZxAnEponOnuVoiceDataPriority_Type.__name__=_B
_ZxAnEponOnuVoiceDataPriority_Object=MibTableColumn
zxAnEponOnuVoiceDataPriority=_ZxAnEponOnuVoiceDataPriority_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,28,1,13),_ZxAnEponOnuVoiceDataPriority_Type())
zxAnEponOnuVoiceDataPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoiceDataPriority.setStatus(_A)
_ZxAnEponOnuVoiceDhcpLeaseTime_Type=Integer32
_ZxAnEponOnuVoiceDhcpLeaseTime_Object=MibTableColumn
zxAnEponOnuVoiceDhcpLeaseTime=_ZxAnEponOnuVoiceDhcpLeaseTime_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,28,1,14),_ZxAnEponOnuVoiceDhcpLeaseTime_Type())
zxAnEponOnuVoiceDhcpLeaseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVoiceDhcpLeaseTime.setStatus(_A)
class _ZxAnEponOnuVoicePPPoEStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dhcping',1),('dhcpfinish',2),('pppoeing',3),('pppoefinish',4)))
_ZxAnEponOnuVoicePPPoEStatus_Type.__name__=_B
_ZxAnEponOnuVoicePPPoEStatus_Object=MibTableColumn
zxAnEponOnuVoicePPPoEStatus=_ZxAnEponOnuVoicePPPoEStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,28,1,15),_ZxAnEponOnuVoicePPPoEStatus_Type())
zxAnEponOnuVoicePPPoEStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVoicePPPoEStatus.setStatus(_A)
_Epon0pticalTransceiverDiagnosisTable_Object=MibTable
epon0pticalTransceiverDiagnosisTable=_Epon0pticalTransceiverDiagnosisTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,29))
if mibBuilder.loadTexts:epon0pticalTransceiverDiagnosisTable.setStatus(_A)
_Epon0pticalTransceiverDiagnosisEntry_Object=MibTableRow
epon0pticalTransceiverDiagnosisEntry=_Epon0pticalTransceiverDiagnosisEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,29,1))
epon0pticalTransceiverDiagnosisEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:epon0pticalTransceiverDiagnosisEntry.setStatus(_A)
_ZxAnEponOnuTransTemperature_Type=DisplayString
_ZxAnEponOnuTransTemperature_Object=MibTableColumn
zxAnEponOnuTransTemperature=_ZxAnEponOnuTransTemperature_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,29,1,1),_ZxAnEponOnuTransTemperature_Type())
zxAnEponOnuTransTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTransTemperature.setStatus(_A)
_ZxAnEponOnuSupplyVoltage_Type=DisplayString
_ZxAnEponOnuSupplyVoltage_Object=MibTableColumn
zxAnEponOnuSupplyVoltage=_ZxAnEponOnuSupplyVoltage_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,29,1,2),_ZxAnEponOnuSupplyVoltage_Type())
zxAnEponOnuSupplyVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuSupplyVoltage.setStatus(_A)
_ZxAnEponOnuTxBiasCurrent_Type=DisplayString
_ZxAnEponOnuTxBiasCurrent_Object=MibTableColumn
zxAnEponOnuTxBiasCurrent=_ZxAnEponOnuTxBiasCurrent_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,29,1,3),_ZxAnEponOnuTxBiasCurrent_Type())
zxAnEponOnuTxBiasCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTxBiasCurrent.setStatus(_A)
_ZxAnEponOnuTxPower_Type=DisplayString
_ZxAnEponOnuTxPower_Object=MibTableColumn
zxAnEponOnuTxPower=_ZxAnEponOnuTxPower_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,29,1,4),_ZxAnEponOnuTxPower_Type())
zxAnEponOnuTxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTxPower.setStatus(_A)
_ZxAnEponOnuRxPower_Type=DisplayString
_ZxAnEponOnuRxPower_Object=MibTableColumn
zxAnEponOnuRxPower=_ZxAnEponOnuRxPower_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,29,1,5),_ZxAnEponOnuRxPower_Type())
zxAnEponOnuRxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuRxPower.setStatus(_A)
_EponRmOnuTransAlarmCfgTable_Object=MibTable
eponRmOnuTransAlarmCfgTable=_EponRmOnuTransAlarmCfgTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,30))
if mibBuilder.loadTexts:eponRmOnuTransAlarmCfgTable.setStatus(_A)
_EponRmOnuTransAlarmCfgTableEntry_Object=MibTableRow
eponRmOnuTransAlarmCfgTableEntry=_EponRmOnuTransAlarmCfgTableEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,30,1))
eponRmOnuTransAlarmCfgTableEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:eponRmOnuTransAlarmCfgTableEntry.setStatus(_A)
class _ZxAnEponOnuTrans_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZxAnEponOnuTrans_Type.__name__=_B
_ZxAnEponOnuTrans_Object=MibTableColumn
zxAnEponOnuTrans=_ZxAnEponOnuTrans_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,30,1,1),_ZxAnEponOnuTrans_Type())
zxAnEponOnuTrans.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTrans.setStatus(_A)
_EponRmOnuTransAlarmThresholdTable_Object=MibTable
eponRmOnuTransAlarmThresholdTable=_EponRmOnuTransAlarmThresholdTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31))
if mibBuilder.loadTexts:eponRmOnuTransAlarmThresholdTable.setStatus(_A)
_EponRmOnuTransAlarmThresholdEntry_Object=MibTableRow
eponRmOnuTransAlarmThresholdEntry=_EponRmOnuTransAlarmThresholdEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1))
eponRmOnuTransAlarmThresholdEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:eponRmOnuTransAlarmThresholdEntry.setStatus(_A)
_ZxAnEponOnuTempHighAlarm_Type=DisplayString
_ZxAnEponOnuTempHighAlarm_Object=MibTableColumn
zxAnEponOnuTempHighAlarm=_ZxAnEponOnuTempHighAlarm_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,1),_ZxAnEponOnuTempHighAlarm_Type())
zxAnEponOnuTempHighAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTempHighAlarm.setStatus(_A)
_ZxAnEponOnuTempLowAlarm_Type=DisplayString
_ZxAnEponOnuTempLowAlarm_Object=MibTableColumn
zxAnEponOnuTempLowAlarm=_ZxAnEponOnuTempLowAlarm_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,2),_ZxAnEponOnuTempLowAlarm_Type())
zxAnEponOnuTempLowAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTempLowAlarm.setStatus(_A)
_ZxAnEponOnuTempHighWarning_Type=DisplayString
_ZxAnEponOnuTempHighWarning_Object=MibTableColumn
zxAnEponOnuTempHighWarning=_ZxAnEponOnuTempHighWarning_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,3),_ZxAnEponOnuTempHighWarning_Type())
zxAnEponOnuTempHighWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTempHighWarning.setStatus(_A)
_ZxAnEponOnuTempLowwarning_Type=DisplayString
_ZxAnEponOnuTempLowwarning_Object=MibTableColumn
zxAnEponOnuTempLowwarning=_ZxAnEponOnuTempLowwarning_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,4),_ZxAnEponOnuTempLowwarning_Type())
zxAnEponOnuTempLowwarning.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTempLowwarning.setStatus(_A)
_ZxAnEponOnuVoltageHighAlarm_Type=DisplayString
_ZxAnEponOnuVoltageHighAlarm_Object=MibTableColumn
zxAnEponOnuVoltageHighAlarm=_ZxAnEponOnuVoltageHighAlarm_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,5),_ZxAnEponOnuVoltageHighAlarm_Type())
zxAnEponOnuVoltageHighAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoltageHighAlarm.setStatus(_A)
_ZxAnEponOnuVoltageLowAlarm_Type=DisplayString
_ZxAnEponOnuVoltageLowAlarm_Object=MibTableColumn
zxAnEponOnuVoltageLowAlarm=_ZxAnEponOnuVoltageLowAlarm_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,6),_ZxAnEponOnuVoltageLowAlarm_Type())
zxAnEponOnuVoltageLowAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoltageLowAlarm.setStatus(_A)
_ZxAnEponOnuVoltageHighWarning_Type=DisplayString
_ZxAnEponOnuVoltageHighWarning_Object=MibTableColumn
zxAnEponOnuVoltageHighWarning=_ZxAnEponOnuVoltageHighWarning_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,7),_ZxAnEponOnuVoltageHighWarning_Type())
zxAnEponOnuVoltageHighWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoltageHighWarning.setStatus(_A)
_ZxAnEponOnuVoltageLowWarning_Type=DisplayString
_ZxAnEponOnuVoltageLowWarning_Object=MibTableColumn
zxAnEponOnuVoltageLowWarning=_ZxAnEponOnuVoltageLowWarning_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,8),_ZxAnEponOnuVoltageLowWarning_Type())
zxAnEponOnuVoltageLowWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoltageLowWarning.setStatus(_A)
_ZxAnEponOnuBiasHighAlarm_Type=DisplayString
_ZxAnEponOnuBiasHighAlarm_Object=MibTableColumn
zxAnEponOnuBiasHighAlarm=_ZxAnEponOnuBiasHighAlarm_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,9),_ZxAnEponOnuBiasHighAlarm_Type())
zxAnEponOnuBiasHighAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuBiasHighAlarm.setStatus(_A)
_ZxAnEponOnuBiasLowAlarm_Type=DisplayString
_ZxAnEponOnuBiasLowAlarm_Object=MibTableColumn
zxAnEponOnuBiasLowAlarm=_ZxAnEponOnuBiasLowAlarm_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,10),_ZxAnEponOnuBiasLowAlarm_Type())
zxAnEponOnuBiasLowAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuBiasLowAlarm.setStatus(_A)
_ZxAnEponOnuBiasHighWarning_Type=DisplayString
_ZxAnEponOnuBiasHighWarning_Object=MibTableColumn
zxAnEponOnuBiasHighWarning=_ZxAnEponOnuBiasHighWarning_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,11),_ZxAnEponOnuBiasHighWarning_Type())
zxAnEponOnuBiasHighWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuBiasHighWarning.setStatus(_A)
_ZxAnEponOnuBiasLowWarning_Type=DisplayString
_ZxAnEponOnuBiasLowWarning_Object=MibTableColumn
zxAnEponOnuBiasLowWarning=_ZxAnEponOnuBiasLowWarning_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,12),_ZxAnEponOnuBiasLowWarning_Type())
zxAnEponOnuBiasLowWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuBiasLowWarning.setStatus(_A)
_ZxAnEponOnuTxPowerHighAlarm_Type=DisplayString
_ZxAnEponOnuTxPowerHighAlarm_Object=MibTableColumn
zxAnEponOnuTxPowerHighAlarm=_ZxAnEponOnuTxPowerHighAlarm_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,13),_ZxAnEponOnuTxPowerHighAlarm_Type())
zxAnEponOnuTxPowerHighAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTxPowerHighAlarm.setStatus(_A)
_ZxAnEponOnuTxPowerLowAlarm_Type=DisplayString
_ZxAnEponOnuTxPowerLowAlarm_Object=MibTableColumn
zxAnEponOnuTxPowerLowAlarm=_ZxAnEponOnuTxPowerLowAlarm_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,14),_ZxAnEponOnuTxPowerLowAlarm_Type())
zxAnEponOnuTxPowerLowAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTxPowerLowAlarm.setStatus(_A)
_ZxAnEponOnuTxPowerHighWarning_Type=DisplayString
_ZxAnEponOnuTxPowerHighWarning_Object=MibTableColumn
zxAnEponOnuTxPowerHighWarning=_ZxAnEponOnuTxPowerHighWarning_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,15),_ZxAnEponOnuTxPowerHighWarning_Type())
zxAnEponOnuTxPowerHighWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTxPowerHighWarning.setStatus(_A)
_ZxAnEponOnuTxPowerLowWarning_Type=DisplayString
_ZxAnEponOnuTxPowerLowWarning_Object=MibTableColumn
zxAnEponOnuTxPowerLowWarning=_ZxAnEponOnuTxPowerLowWarning_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,16),_ZxAnEponOnuTxPowerLowWarning_Type())
zxAnEponOnuTxPowerLowWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTxPowerLowWarning.setStatus(_A)
_ZxAnEponOnuRxPowerHighAlarm_Type=DisplayString
_ZxAnEponOnuRxPowerHighAlarm_Object=MibTableColumn
zxAnEponOnuRxPowerHighAlarm=_ZxAnEponOnuRxPowerHighAlarm_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,17),_ZxAnEponOnuRxPowerHighAlarm_Type())
zxAnEponOnuRxPowerHighAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuRxPowerHighAlarm.setStatus(_A)
_ZxAnEponOnuRxPowerLowAlarm_Type=DisplayString
_ZxAnEponOnuRxPowerLowAlarm_Object=MibTableColumn
zxAnEponOnuRxPowerLowAlarm=_ZxAnEponOnuRxPowerLowAlarm_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,18),_ZxAnEponOnuRxPowerLowAlarm_Type())
zxAnEponOnuRxPowerLowAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuRxPowerLowAlarm.setStatus(_A)
_ZxAnEponOnuRxPowerHighWarning_Type=DisplayString
_ZxAnEponOnuRxPowerHighWarning_Object=MibTableColumn
zxAnEponOnuRxPowerHighWarning=_ZxAnEponOnuRxPowerHighWarning_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,19),_ZxAnEponOnuRxPowerHighWarning_Type())
zxAnEponOnuRxPowerHighWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuRxPowerHighWarning.setStatus(_A)
_ZxAnEponOnuRxPowerLowWarning_Type=DisplayString
_ZxAnEponOnuRxPowerLowWarning_Object=MibTableColumn
zxAnEponOnuRxPowerLowWarning=_ZxAnEponOnuRxPowerLowWarning_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,31,1,20),_ZxAnEponOnuRxPowerLowWarning_Type())
zxAnEponOnuRxPowerLowWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuRxPowerLowWarning.setStatus(_A)
_ZxEponUniProfileAdmin_ObjectIdentity=ObjectIdentity
zxEponUniProfileAdmin=_ZxEponUniProfileAdmin_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,1,32))
_ZxEponUniProfileTable_Object=MibTable
zxEponUniProfileTable=_ZxEponUniProfileTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,32,1))
if mibBuilder.loadTexts:zxEponUniProfileTable.setStatus(_A)
_ZxEponUniProfileEntry_Object=MibTableRow
zxEponUniProfileEntry=_ZxEponUniProfileEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,32,1,1))
zxEponUniProfileEntry.setIndexNames((0,_E,_A7))
if mibBuilder.loadTexts:zxEponUniProfileEntry.setStatus(_A)
_UniProfileIndex_Type=Integer32
_UniProfileIndex_Object=MibTableColumn
uniProfileIndex=_UniProfileIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,32,1,1,1),_UniProfileIndex_Type())
uniProfileIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:uniProfileIndex.setStatus(_A)
class _UniProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_UniProfileName_Type.__name__=_L
_UniProfileName_Object=MibTableColumn
uniProfileName=_UniProfileName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,32,1,1,2),_UniProfileName_Type())
uniProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:uniProfileName.setStatus(_A)
class _UniProfileUpCir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_UniProfileUpCir_Type.__name__=_B
_UniProfileUpCir_Object=MibTableColumn
uniProfileUpCir=_UniProfileUpCir_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,32,1,1,3),_UniProfileUpCir_Type())
uniProfileUpCir.setMaxAccess(_C)
if mibBuilder.loadTexts:uniProfileUpCir.setStatus(_A)
class _UniProfileUpCbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1522,16777215))
_UniProfileUpCbs_Type.__name__=_B
_UniProfileUpCbs_Object=MibTableColumn
uniProfileUpCbs=_UniProfileUpCbs_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,32,1,1,4),_UniProfileUpCbs_Type())
uniProfileUpCbs.setMaxAccess(_C)
if mibBuilder.loadTexts:uniProfileUpCbs.setStatus(_A)
class _UniProfileUpEbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1522))
_UniProfileUpEbs_Type.__name__=_B
_UniProfileUpEbs_Object=MibTableColumn
uniProfileUpEbs=_UniProfileUpEbs_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,32,1,1,5),_UniProfileUpEbs_Type())
uniProfileUpEbs.setMaxAccess(_C)
if mibBuilder.loadTexts:uniProfileUpEbs.setStatus(_A)
class _UniProfileDownCir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_UniProfileDownCir_Type.__name__=_B
_UniProfileDownCir_Object=MibTableColumn
uniProfileDownCir=_UniProfileDownCir_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,32,1,1,6),_UniProfileDownCir_Type())
uniProfileDownCir.setMaxAccess(_C)
if mibBuilder.loadTexts:uniProfileDownCir.setStatus(_A)
class _UniProfileDownCbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1522,16777215))
_UniProfileDownCbs_Type.__name__=_B
_UniProfileDownCbs_Object=MibTableColumn
uniProfileDownCbs=_UniProfileDownCbs_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,32,1,1,7),_UniProfileDownCbs_Type())
uniProfileDownCbs.setMaxAccess(_C)
if mibBuilder.loadTexts:uniProfileDownCbs.setStatus(_A)
class _UniProfileDownEbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1522))
_UniProfileDownEbs_Type.__name__=_B
_UniProfileDownEbs_Object=MibTableColumn
uniProfileDownEbs=_UniProfileDownEbs_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,32,1,1,8),_UniProfileDownEbs_Type())
uniProfileDownEbs.setMaxAccess(_C)
if mibBuilder.loadTexts:uniProfileDownEbs.setStatus(_A)
_UniProfileRowStatus_Type=RowStatus
_UniProfileRowStatus_Object=MibTableColumn
uniProfileRowStatus=_UniProfileRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,32,1,1,9),_UniProfileRowStatus_Type())
uniProfileRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:uniProfileRowStatus.setStatus(_A)
_UniProfileNextIndex_Type=Integer32
_UniProfileNextIndex_Object=MibScalar
uniProfileNextIndex=_UniProfileNextIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,32,2),_UniProfileNextIndex_Type())
uniProfileNextIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:uniProfileNextIndex.setStatus(_A)
_ZxEponUniLimitCfgTable_Object=MibTable
zxEponUniLimitCfgTable=_ZxEponUniLimitCfgTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,34))
if mibBuilder.loadTexts:zxEponUniLimitCfgTable.setStatus(_A)
_ZxEponUniLimitCfgEntry_Object=MibTableRow
zxEponUniLimitCfgEntry=_ZxEponUniLimitCfgEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,34,1))
zxEponUniLimitCfgEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxEponUniLimitCfgEntry.setStatus(_A)
class _UniCfgLimitProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_UniCfgLimitProfileIndex_Type.__name__=_B
_UniCfgLimitProfileIndex_Object=MibTableColumn
uniCfgLimitProfileIndex=_UniCfgLimitProfileIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,34,1,1),_UniCfgLimitProfileIndex_Type())
uniCfgLimitProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:uniCfgLimitProfileIndex.setStatus(_A)
_ZxAnEponRmVoipProfileMgmt_ObjectIdentity=ObjectIdentity
zxAnEponRmVoipProfileMgmt=_ZxAnEponRmVoipProfileMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,1,35))
_ZxAnEponRmVoipIpProfileIdxNext_Type=Integer32
_ZxAnEponRmVoipIpProfileIdxNext_Object=MibScalar
zxAnEponRmVoipIpProfileIdxNext=_ZxAnEponRmVoipIpProfileIdxNext_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,1),_ZxAnEponRmVoipIpProfileIdxNext_Type())
zxAnEponRmVoipIpProfileIdxNext.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipIpProfileIdxNext.setStatus(_A)
_ZxAnEponRmVoipIpProfileTable_Object=MibTable
zxAnEponRmVoipIpProfileTable=_ZxAnEponRmVoipIpProfileTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,2))
if mibBuilder.loadTexts:zxAnEponRmVoipIpProfileTable.setStatus(_A)
_ZxAnEponRmVoipIpProfileEntry_Object=MibTableRow
zxAnEponRmVoipIpProfileEntry=_ZxAnEponRmVoipIpProfileEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,2,1))
zxAnEponRmVoipIpProfileEntry.setIndexNames((0,_E,_A8))
if mibBuilder.loadTexts:zxAnEponRmVoipIpProfileEntry.setStatus(_A)
_ZxAnEponRmVoipIpProfileIdx_Type=Integer32
_ZxAnEponRmVoipIpProfileIdx_Object=MibTableColumn
zxAnEponRmVoipIpProfileIdx=_ZxAnEponRmVoipIpProfileIdx_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,2,1,1),_ZxAnEponRmVoipIpProfileIdx_Type())
zxAnEponRmVoipIpProfileIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponRmVoipIpProfileIdx.setStatus(_A)
class _ZxAnEponRmVoipIpProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnEponRmVoipIpProfileName_Type.__name__=_L
_ZxAnEponRmVoipIpProfileName_Object=MibTableColumn
zxAnEponRmVoipIpProfileName=_ZxAnEponRmVoipIpProfileName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,2,1,2),_ZxAnEponRmVoipIpProfileName_Type())
zxAnEponRmVoipIpProfileName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipIpProfileName.setStatus(_A)
class _ZxAnEponRmVoipIpMngIpRelation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('independent',1),('shared',2)))
_ZxAnEponRmVoipIpMngIpRelation_Type.__name__=_B
_ZxAnEponRmVoipIpMngIpRelation_Object=MibTableColumn
zxAnEponRmVoipIpMngIpRelation=_ZxAnEponRmVoipIpMngIpRelation_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,2,1,3),_ZxAnEponRmVoipIpMngIpRelation_Type())
zxAnEponRmVoipIpMngIpRelation.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipIpMngIpRelation.setStatus(_A)
class _ZxAnEponRmVoipIpMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_V,1),(_c,2),(_d,3)))
_ZxAnEponRmVoipIpMode_Type.__name__=_B
_ZxAnEponRmVoipIpMode_Object=MibTableColumn
zxAnEponRmVoipIpMode=_ZxAnEponRmVoipIpMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,2,1,4),_ZxAnEponRmVoipIpMode_Type())
zxAnEponRmVoipIpMode.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipIpMode.setStatus(_A)
_ZxAnEponRmVoipIpDefaultGateWay_Type=IpAddress
_ZxAnEponRmVoipIpDefaultGateWay_Object=MibTableColumn
zxAnEponRmVoipIpDefaultGateWay=_ZxAnEponRmVoipIpDefaultGateWay_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,2,1,5),_ZxAnEponRmVoipIpDefaultGateWay_Type())
zxAnEponRmVoipIpDefaultGateWay.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipIpDefaultGateWay.setStatus(_A)
_ZxAnEponRmVoipIpPrimaryDNSServerIp_Type=IpAddress
_ZxAnEponRmVoipIpPrimaryDNSServerIp_Object=MibTableColumn
zxAnEponRmVoipIpPrimaryDNSServerIp=_ZxAnEponRmVoipIpPrimaryDNSServerIp_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,2,1,6),_ZxAnEponRmVoipIpPrimaryDNSServerIp_Type())
zxAnEponRmVoipIpPrimaryDNSServerIp.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipIpPrimaryDNSServerIp.setStatus(_A)
class _ZxAnEponRmVoipIpPPPoEMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_e,1),(_f,2),(_g,3)))
_ZxAnEponRmVoipIpPPPoEMode_Type.__name__=_B
_ZxAnEponRmVoipIpPPPoEMode_Object=MibTableColumn
zxAnEponRmVoipIpPPPoEMode=_ZxAnEponRmVoipIpPPPoEMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,2,1,7),_ZxAnEponRmVoipIpPPPoEMode_Type())
zxAnEponRmVoipIpPPPoEMode.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipIpPPPoEMode.setStatus(_A)
_ZxAnEponRmVoipIpRowStatus_Type=RowStatus
_ZxAnEponRmVoipIpRowStatus_Object=MibTableColumn
zxAnEponRmVoipIpRowStatus=_ZxAnEponRmVoipIpRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,2,1,30),_ZxAnEponRmVoipIpRowStatus_Type())
zxAnEponRmVoipIpRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipIpRowStatus.setStatus(_A)
_ZxAnEponRmVoipVlanProfileIdxNext_Type=Integer32
_ZxAnEponRmVoipVlanProfileIdxNext_Object=MibScalar
zxAnEponRmVoipVlanProfileIdxNext=_ZxAnEponRmVoipVlanProfileIdxNext_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,3),_ZxAnEponRmVoipVlanProfileIdxNext_Type())
zxAnEponRmVoipVlanProfileIdxNext.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipVlanProfileIdxNext.setStatus(_A)
_ZxAnEponRmVoipVlanProfileTable_Object=MibTable
zxAnEponRmVoipVlanProfileTable=_ZxAnEponRmVoipVlanProfileTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,4))
if mibBuilder.loadTexts:zxAnEponRmVoipVlanProfileTable.setStatus(_A)
_ZxAnEponRmVoipVlanProfileEntry_Object=MibTableRow
zxAnEponRmVoipVlanProfileEntry=_ZxAnEponRmVoipVlanProfileEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,4,1))
zxAnEponRmVoipVlanProfileEntry.setIndexNames((0,_E,_A9))
if mibBuilder.loadTexts:zxAnEponRmVoipVlanProfileEntry.setStatus(_A)
_ZxAnEponRmVoipVlanProfileIdx_Type=Integer32
_ZxAnEponRmVoipVlanProfileIdx_Object=MibTableColumn
zxAnEponRmVoipVlanProfileIdx=_ZxAnEponRmVoipVlanProfileIdx_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,4,1,1),_ZxAnEponRmVoipVlanProfileIdx_Type())
zxAnEponRmVoipVlanProfileIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponRmVoipVlanProfileIdx.setStatus(_A)
class _ZxAnEponRmVoipVlanProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnEponRmVoipVlanProfileName_Type.__name__=_L
_ZxAnEponRmVoipVlanProfileName_Object=MibTableColumn
zxAnEponRmVoipVlanProfileName=_ZxAnEponRmVoipVlanProfileName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,4,1,2),_ZxAnEponRmVoipVlanProfileName_Type())
zxAnEponRmVoipVlanProfileName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipVlanProfileName.setStatus(_A)
class _ZxAnEponRmVoipVlanTagMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_b,1),('tag',2),('vlanStacking',3)))
_ZxAnEponRmVoipVlanTagMode_Type.__name__=_B
_ZxAnEponRmVoipVlanTagMode_Object=MibTableColumn
zxAnEponRmVoipVlanTagMode=_ZxAnEponRmVoipVlanTagMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,4,1,3),_ZxAnEponRmVoipVlanTagMode_Type())
zxAnEponRmVoipVlanTagMode.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipVlanTagMode.setStatus(_A)
class _ZxAnEponRmVoipVlanTagCVlan_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnEponRmVoipVlanTagCVlan_Type.__name__=_B
_ZxAnEponRmVoipVlanTagCVlan_Object=MibTableColumn
zxAnEponRmVoipVlanTagCVlan=_ZxAnEponRmVoipVlanTagCVlan_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,4,1,4),_ZxAnEponRmVoipVlanTagCVlan_Type())
zxAnEponRmVoipVlanTagCVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipVlanTagCVlan.setStatus(_A)
class _ZxAnEponRmVoipVlanTagPriority_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnEponRmVoipVlanTagPriority_Type.__name__=_B
_ZxAnEponRmVoipVlanTagPriority_Object=MibTableColumn
zxAnEponRmVoipVlanTagPriority=_ZxAnEponRmVoipVlanTagPriority_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,4,1,5),_ZxAnEponRmVoipVlanTagPriority_Type())
zxAnEponRmVoipVlanTagPriority.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipVlanTagPriority.setStatus(_A)
class _ZxAnEponRmVoipVlanTagSVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnEponRmVoipVlanTagSVlan_Type.__name__=_B
_ZxAnEponRmVoipVlanTagSVlan_Object=MibTableColumn
zxAnEponRmVoipVlanTagSVlan=_ZxAnEponRmVoipVlanTagSVlan_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,4,1,6),_ZxAnEponRmVoipVlanTagSVlan_Type())
zxAnEponRmVoipVlanTagSVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipVlanTagSVlan.setStatus(_A)
_ZxAnEponRmVoipVlanRowStatus_Type=RowStatus
_ZxAnEponRmVoipVlanRowStatus_Object=MibTableColumn
zxAnEponRmVoipVlanRowStatus=_ZxAnEponRmVoipVlanRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,4,1,30),_ZxAnEponRmVoipVlanRowStatus_Type())
zxAnEponRmVoipVlanRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipVlanRowStatus.setStatus(_A)
_ZxAnEponRmVoipH248ProfileIdxNext_Type=Integer32
_ZxAnEponRmVoipH248ProfileIdxNext_Object=MibScalar
zxAnEponRmVoipH248ProfileIdxNext=_ZxAnEponRmVoipH248ProfileIdxNext_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,5),_ZxAnEponRmVoipH248ProfileIdxNext_Type())
zxAnEponRmVoipH248ProfileIdxNext.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipH248ProfileIdxNext.setStatus(_A)
_ZxAnEponRmVoipH248ProfileTable_Object=MibTable
zxAnEponRmVoipH248ProfileTable=_ZxAnEponRmVoipH248ProfileTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,6))
if mibBuilder.loadTexts:zxAnEponRmVoipH248ProfileTable.setStatus(_A)
_ZxAnEponRmVoipH248ProfileEntry_Object=MibTableRow
zxAnEponRmVoipH248ProfileEntry=_ZxAnEponRmVoipH248ProfileEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,6,1))
zxAnEponRmVoipH248ProfileEntry.setIndexNames((0,_E,_AA))
if mibBuilder.loadTexts:zxAnEponRmVoipH248ProfileEntry.setStatus(_A)
_ZxAnEponRmVoipH248ProfileIdx_Type=Integer32
_ZxAnEponRmVoipH248ProfileIdx_Object=MibTableColumn
zxAnEponRmVoipH248ProfileIdx=_ZxAnEponRmVoipH248ProfileIdx_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,6,1,1),_ZxAnEponRmVoipH248ProfileIdx_Type())
zxAnEponRmVoipH248ProfileIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponRmVoipH248ProfileIdx.setStatus(_A)
class _ZxAnEponRmVoipH248ProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnEponRmVoipH248ProfileName_Type.__name__=_L
_ZxAnEponRmVoipH248ProfileName_Object=MibTableColumn
zxAnEponRmVoipH248ProfileName=_ZxAnEponRmVoipH248ProfileName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,6,1,2),_ZxAnEponRmVoipH248ProfileName_Type())
zxAnEponRmVoipH248ProfileName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248ProfileName.setStatus(_A)
_ZxAnEponRmVoipH248RegServerIp_Type=IpAddress
_ZxAnEponRmVoipH248RegServerIp_Object=MibTableColumn
zxAnEponRmVoipH248RegServerIp=_ZxAnEponRmVoipH248RegServerIp_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,6,1,3),_ZxAnEponRmVoipH248RegServerIp_Type())
zxAnEponRmVoipH248RegServerIp.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248RegServerIp.setStatus(_A)
class _ZxAnEponRmVoipH248RegServerPort_Type(Integer32):defaultValue=2944;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1001,65535))
_ZxAnEponRmVoipH248RegServerPort_Type.__name__=_B
_ZxAnEponRmVoipH248RegServerPort_Object=MibTableColumn
zxAnEponRmVoipH248RegServerPort=_ZxAnEponRmVoipH248RegServerPort_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,6,1,4),_ZxAnEponRmVoipH248RegServerPort_Type())
zxAnEponRmVoipH248RegServerPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248RegServerPort.setStatus(_A)
_ZxAnEponRmVoipH248BackRegServerIp_Type=IpAddress
_ZxAnEponRmVoipH248BackRegServerIp_Object=MibTableColumn
zxAnEponRmVoipH248BackRegServerIp=_ZxAnEponRmVoipH248BackRegServerIp_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,6,1,5),_ZxAnEponRmVoipH248BackRegServerIp_Type())
zxAnEponRmVoipH248BackRegServerIp.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248BackRegServerIp.setStatus(_A)
class _ZxAnEponRmVoipH248BackRegServerPort_Type(Integer32):defaultValue=2944;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1001,65535))
_ZxAnEponRmVoipH248BackRegServerPort_Type.__name__=_B
_ZxAnEponRmVoipH248BackRegServerPort_Object=MibTableColumn
zxAnEponRmVoipH248BackRegServerPort=_ZxAnEponRmVoipH248BackRegServerPort_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,6,1,6),_ZxAnEponRmVoipH248BackRegServerPort_Type())
zxAnEponRmVoipH248BackRegServerPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248BackRegServerPort.setStatus(_A)
class _ZxAnEponRmVoipH248RtpLinkKeptFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_ZxAnEponRmVoipH248RtpLinkKeptFlag_Type.__name__=_B
_ZxAnEponRmVoipH248RtpLinkKeptFlag_Object=MibTableColumn
zxAnEponRmVoipH248RtpLinkKeptFlag=_ZxAnEponRmVoipH248RtpLinkKeptFlag_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,6,1,7),_ZxAnEponRmVoipH248RtpLinkKeptFlag_Type())
zxAnEponRmVoipH248RtpLinkKeptFlag.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248RtpLinkKeptFlag.setStatus(_A)
class _ZxAnEponRmVoipH248OnuHeartbeatMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),('h248ServiceChange',2),('h248Ctc',3)))
_ZxAnEponRmVoipH248OnuHeartbeatMode_Type.__name__=_B
_ZxAnEponRmVoipH248OnuHeartbeatMode_Object=MibTableColumn
zxAnEponRmVoipH248OnuHeartbeatMode=_ZxAnEponRmVoipH248OnuHeartbeatMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,6,1,8),_ZxAnEponRmVoipH248OnuHeartbeatMode_Type())
zxAnEponRmVoipH248OnuHeartbeatMode.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248OnuHeartbeatMode.setStatus(_A)
class _ZxAnEponRmVoipH248OnuHeartbeatCycle_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,65535))
_ZxAnEponRmVoipH248OnuHeartbeatCycle_Type.__name__=_B
_ZxAnEponRmVoipH248OnuHeartbeatCycle_Object=MibTableColumn
zxAnEponRmVoipH248OnuHeartbeatCycle=_ZxAnEponRmVoipH248OnuHeartbeatCycle_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,6,1,9),_ZxAnEponRmVoipH248OnuHeartbeatCycle_Type())
zxAnEponRmVoipH248OnuHeartbeatCycle.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248OnuHeartbeatCycle.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponRmVoipH248OnuHeartbeatCycle.setUnits(_W)
class _ZxAnEponRmVoipH248OnuHeartbeatCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ZxAnEponRmVoipH248OnuHeartbeatCount_Type.__name__=_B
_ZxAnEponRmVoipH248OnuHeartbeatCount_Object=MibTableColumn
zxAnEponRmVoipH248OnuHeartbeatCount=_ZxAnEponRmVoipH248OnuHeartbeatCount_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,6,1,10),_ZxAnEponRmVoipH248OnuHeartbeatCount_Type())
zxAnEponRmVoipH248OnuHeartbeatCount.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248OnuHeartbeatCount.setStatus(_A)
class _ZxAnEponRmVoipH248MgRegMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AB,1),('ip',2),(_AC,3)))
_ZxAnEponRmVoipH248MgRegMode_Type.__name__=_B
_ZxAnEponRmVoipH248MgRegMode_Object=MibTableColumn
zxAnEponRmVoipH248MgRegMode=_ZxAnEponRmVoipH248MgRegMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,6,1,11),_ZxAnEponRmVoipH248MgRegMode_Type())
zxAnEponRmVoipH248MgRegMode.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgRegMode.setStatus(_A)
class _ZxAnEponRmVoipH248MgPort_Type(Integer32):defaultValue=2944;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1001,65535))
_ZxAnEponRmVoipH248MgPort_Type.__name__=_B
_ZxAnEponRmVoipH248MgPort_Object=MibTableColumn
zxAnEponRmVoipH248MgPort=_ZxAnEponRmVoipH248MgPort_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,6,1,12),_ZxAnEponRmVoipH248MgPort_Type())
zxAnEponRmVoipH248MgPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgPort.setStatus(_A)
_ZxAnEponRmVoipH248RowStatus_Type=RowStatus
_ZxAnEponRmVoipH248RowStatus_Object=MibTableColumn
zxAnEponRmVoipH248RowStatus=_ZxAnEponRmVoipH248RowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,6,1,30),_ZxAnEponRmVoipH248RowStatus_Type())
zxAnEponRmVoipH248RowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248RowStatus.setStatus(_A)
_ZxAnEponRmVoipMgcpProfileIdxNext_Type=Integer32
_ZxAnEponRmVoipMgcpProfileIdxNext_Object=MibScalar
zxAnEponRmVoipMgcpProfileIdxNext=_ZxAnEponRmVoipMgcpProfileIdxNext_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,7),_ZxAnEponRmVoipMgcpProfileIdxNext_Type())
zxAnEponRmVoipMgcpProfileIdxNext.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipMgcpProfileIdxNext.setStatus(_A)
_ZxAnEponRmVoipMgcpProfileTable_Object=MibTable
zxAnEponRmVoipMgcpProfileTable=_ZxAnEponRmVoipMgcpProfileTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,8))
if mibBuilder.loadTexts:zxAnEponRmVoipMgcpProfileTable.setStatus(_A)
_ZxAnEponRmVoipMgcpProfileEntry_Object=MibTableRow
zxAnEponRmVoipMgcpProfileEntry=_ZxAnEponRmVoipMgcpProfileEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,8,1))
zxAnEponRmVoipMgcpProfileEntry.setIndexNames((0,_E,_AD))
if mibBuilder.loadTexts:zxAnEponRmVoipMgcpProfileEntry.setStatus(_A)
_ZxAnEponRmVoipMgcpProfileIdx_Type=Integer32
_ZxAnEponRmVoipMgcpProfileIdx_Object=MibTableColumn
zxAnEponRmVoipMgcpProfileIdx=_ZxAnEponRmVoipMgcpProfileIdx_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,8,1,1),_ZxAnEponRmVoipMgcpProfileIdx_Type())
zxAnEponRmVoipMgcpProfileIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponRmVoipMgcpProfileIdx.setStatus(_A)
class _ZxAnEponRmVoipMgcpProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnEponRmVoipMgcpProfileName_Type.__name__=_L
_ZxAnEponRmVoipMgcpProfileName_Object=MibTableColumn
zxAnEponRmVoipMgcpProfileName=_ZxAnEponRmVoipMgcpProfileName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,8,1,2),_ZxAnEponRmVoipMgcpProfileName_Type())
zxAnEponRmVoipMgcpProfileName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipMgcpProfileName.setStatus(_A)
_ZxAnEponRmVoipMgcpRegServerIp_Type=IpAddress
_ZxAnEponRmVoipMgcpRegServerIp_Object=MibTableColumn
zxAnEponRmVoipMgcpRegServerIp=_ZxAnEponRmVoipMgcpRegServerIp_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,8,1,3),_ZxAnEponRmVoipMgcpRegServerIp_Type())
zxAnEponRmVoipMgcpRegServerIp.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipMgcpRegServerIp.setStatus(_A)
class _ZxAnEponRmVoipMgcpRegServerPort_Type(Integer32):defaultValue=2727;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1001,65535))
_ZxAnEponRmVoipMgcpRegServerPort_Type.__name__=_B
_ZxAnEponRmVoipMgcpRegServerPort_Object=MibTableColumn
zxAnEponRmVoipMgcpRegServerPort=_ZxAnEponRmVoipMgcpRegServerPort_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,8,1,4),_ZxAnEponRmVoipMgcpRegServerPort_Type())
zxAnEponRmVoipMgcpRegServerPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipMgcpRegServerPort.setStatus(_A)
_ZxAnEponRmVoipMgcpBackRegServerIp_Type=IpAddress
_ZxAnEponRmVoipMgcpBackRegServerIp_Object=MibTableColumn
zxAnEponRmVoipMgcpBackRegServerIp=_ZxAnEponRmVoipMgcpBackRegServerIp_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,8,1,5),_ZxAnEponRmVoipMgcpBackRegServerIp_Type())
zxAnEponRmVoipMgcpBackRegServerIp.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipMgcpBackRegServerIp.setStatus(_A)
class _ZxAnEponRmVoipMgcpBackRegServerPort_Type(Integer32):defaultValue=2727;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1001,65535))
_ZxAnEponRmVoipMgcpBackRegServerPort_Type.__name__=_B
_ZxAnEponRmVoipMgcpBackRegServerPort_Object=MibTableColumn
zxAnEponRmVoipMgcpBackRegServerPort=_ZxAnEponRmVoipMgcpBackRegServerPort_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,8,1,6),_ZxAnEponRmVoipMgcpBackRegServerPort_Type())
zxAnEponRmVoipMgcpBackRegServerPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipMgcpBackRegServerPort.setStatus(_A)
class _ZxAnEponRmVoipMgcpOnuHeartbeatMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_ZxAnEponRmVoipMgcpOnuHeartbeatMode_Type.__name__=_B
_ZxAnEponRmVoipMgcpOnuHeartbeatMode_Object=MibTableColumn
zxAnEponRmVoipMgcpOnuHeartbeatMode=_ZxAnEponRmVoipMgcpOnuHeartbeatMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,8,1,7),_ZxAnEponRmVoipMgcpOnuHeartbeatMode_Type())
zxAnEponRmVoipMgcpOnuHeartbeatMode.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipMgcpOnuHeartbeatMode.setStatus(_A)
class _ZxAnEponRmVoipMgcpOnuHeartbeatCycle_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_ZxAnEponRmVoipMgcpOnuHeartbeatCycle_Type.__name__=_B
_ZxAnEponRmVoipMgcpOnuHeartbeatCycle_Object=MibTableColumn
zxAnEponRmVoipMgcpOnuHeartbeatCycle=_ZxAnEponRmVoipMgcpOnuHeartbeatCycle_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,8,1,8),_ZxAnEponRmVoipMgcpOnuHeartbeatCycle_Type())
zxAnEponRmVoipMgcpOnuHeartbeatCycle.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipMgcpOnuHeartbeatCycle.setStatus(_A)
class _ZxAnEponRmVoipMgcpOnuHeartbeatCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ZxAnEponRmVoipMgcpOnuHeartbeatCount_Type.__name__=_B
_ZxAnEponRmVoipMgcpOnuHeartbeatCount_Object=MibTableColumn
zxAnEponRmVoipMgcpOnuHeartbeatCount=_ZxAnEponRmVoipMgcpOnuHeartbeatCount_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,8,1,9),_ZxAnEponRmVoipMgcpOnuHeartbeatCount_Type())
zxAnEponRmVoipMgcpOnuHeartbeatCount.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipMgcpOnuHeartbeatCount.setStatus(_A)
class _ZxAnEponRmVoipMgcpMgRegMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AB,1),('ip',2),(_AC,3)))
_ZxAnEponRmVoipMgcpMgRegMode_Type.__name__=_B
_ZxAnEponRmVoipMgcpMgRegMode_Object=MibTableColumn
zxAnEponRmVoipMgcpMgRegMode=_ZxAnEponRmVoipMgcpMgRegMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,8,1,10),_ZxAnEponRmVoipMgcpMgRegMode_Type())
zxAnEponRmVoipMgcpMgRegMode.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipMgcpMgRegMode.setStatus(_A)
class _ZxAnEponRmVoipMgcpMgPort_Type(Integer32):defaultValue=2427;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1001,65535))
_ZxAnEponRmVoipMgcpMgPort_Type.__name__=_B
_ZxAnEponRmVoipMgcpMgPort_Object=MibTableColumn
zxAnEponRmVoipMgcpMgPort=_ZxAnEponRmVoipMgcpMgPort_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,8,1,11),_ZxAnEponRmVoipMgcpMgPort_Type())
zxAnEponRmVoipMgcpMgPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipMgcpMgPort.setStatus(_A)
_ZxAnEponRmVoipMgcpRowStatus_Type=RowStatus
_ZxAnEponRmVoipMgcpRowStatus_Object=MibTableColumn
zxAnEponRmVoipMgcpRowStatus=_ZxAnEponRmVoipMgcpRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,8,1,30),_ZxAnEponRmVoipMgcpRowStatus_Type())
zxAnEponRmVoipMgcpRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipMgcpRowStatus.setStatus(_A)
_ZxAnEponRmVoipSipProfileIdxNext_Type=Integer32
_ZxAnEponRmVoipSipProfileIdxNext_Object=MibScalar
zxAnEponRmVoipSipProfileIdxNext=_ZxAnEponRmVoipSipProfileIdxNext_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,9),_ZxAnEponRmVoipSipProfileIdxNext_Type())
zxAnEponRmVoipSipProfileIdxNext.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipSipProfileIdxNext.setStatus(_A)
_ZxAnEponRmVoipSipProfileTable_Object=MibTable
zxAnEponRmVoipSipProfileTable=_ZxAnEponRmVoipSipProfileTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10))
if mibBuilder.loadTexts:zxAnEponRmVoipSipProfileTable.setStatus(_A)
_ZxAnEponRmVoipSipProfileEntry_Object=MibTableRow
zxAnEponRmVoipSipProfileEntry=_ZxAnEponRmVoipSipProfileEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1))
zxAnEponRmVoipSipProfileEntry.setIndexNames((0,_E,_AE))
if mibBuilder.loadTexts:zxAnEponRmVoipSipProfileEntry.setStatus(_A)
_ZxAnEponRmVoipSipProfileIdx_Type=Integer32
_ZxAnEponRmVoipSipProfileIdx_Object=MibTableColumn
zxAnEponRmVoipSipProfileIdx=_ZxAnEponRmVoipSipProfileIdx_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1,1),_ZxAnEponRmVoipSipProfileIdx_Type())
zxAnEponRmVoipSipProfileIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponRmVoipSipProfileIdx.setStatus(_A)
class _ZxAnEponRmVoipSipProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnEponRmVoipSipProfileName_Type.__name__=_L
_ZxAnEponRmVoipSipProfileName_Object=MibTableColumn
zxAnEponRmVoipSipProfileName=_ZxAnEponRmVoipSipProfileName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1,2),_ZxAnEponRmVoipSipProfileName_Type())
zxAnEponRmVoipSipProfileName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipSipProfileName.setStatus(_A)
class _ZxAnEponRmVoipSipMgPort_Type(Integer32):defaultValue=5060;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1001,65535))
_ZxAnEponRmVoipSipMgPort_Type.__name__=_B
_ZxAnEponRmVoipSipMgPort_Object=MibTableColumn
zxAnEponRmVoipSipMgPort=_ZxAnEponRmVoipSipMgPort_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1,3),_ZxAnEponRmVoipSipMgPort_Type())
zxAnEponRmVoipSipMgPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipSipMgPort.setStatus(_A)
_ZxAnEponRmVoipSipRegServerIp_Type=IpAddress
_ZxAnEponRmVoipSipRegServerIp_Object=MibTableColumn
zxAnEponRmVoipSipRegServerIp=_ZxAnEponRmVoipSipRegServerIp_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1,4),_ZxAnEponRmVoipSipRegServerIp_Type())
zxAnEponRmVoipSipRegServerIp.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipSipRegServerIp.setStatus(_A)
class _ZxAnEponRmVoipSipRegServerPort_Type(Integer32):defaultValue=5060;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1001,65535))
_ZxAnEponRmVoipSipRegServerPort_Type.__name__=_B
_ZxAnEponRmVoipSipRegServerPort_Object=MibTableColumn
zxAnEponRmVoipSipRegServerPort=_ZxAnEponRmVoipSipRegServerPort_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1,5),_ZxAnEponRmVoipSipRegServerPort_Type())
zxAnEponRmVoipSipRegServerPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipSipRegServerPort.setStatus(_A)
_ZxAnEponRmVoipSipBackRegServerIp_Type=IpAddress
_ZxAnEponRmVoipSipBackRegServerIp_Object=MibTableColumn
zxAnEponRmVoipSipBackRegServerIp=_ZxAnEponRmVoipSipBackRegServerIp_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1,6),_ZxAnEponRmVoipSipBackRegServerIp_Type())
zxAnEponRmVoipSipBackRegServerIp.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipSipBackRegServerIp.setStatus(_A)
class _ZxAnEponRmVoipSipBackRegServerPort_Type(Integer32):defaultValue=5060;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1001,65535))
_ZxAnEponRmVoipSipBackRegServerPort_Type.__name__=_B
_ZxAnEponRmVoipSipBackRegServerPort_Object=MibTableColumn
zxAnEponRmVoipSipBackRegServerPort=_ZxAnEponRmVoipSipBackRegServerPort_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1,7),_ZxAnEponRmVoipSipBackRegServerPort_Type())
zxAnEponRmVoipSipBackRegServerPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipSipBackRegServerPort.setStatus(_A)
_ZxAnEponRmVoipSipProxyServerIp_Type=IpAddress
_ZxAnEponRmVoipSipProxyServerIp_Object=MibTableColumn
zxAnEponRmVoipSipProxyServerIp=_ZxAnEponRmVoipSipProxyServerIp_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1,8),_ZxAnEponRmVoipSipProxyServerIp_Type())
zxAnEponRmVoipSipProxyServerIp.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipSipProxyServerIp.setStatus(_A)
class _ZxAnEponRmVoipSipProxyServerPort_Type(Integer32):defaultValue=5060;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1001,65535))
_ZxAnEponRmVoipSipProxyServerPort_Type.__name__=_B
_ZxAnEponRmVoipSipProxyServerPort_Object=MibTableColumn
zxAnEponRmVoipSipProxyServerPort=_ZxAnEponRmVoipSipProxyServerPort_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1,9),_ZxAnEponRmVoipSipProxyServerPort_Type())
zxAnEponRmVoipSipProxyServerPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipSipProxyServerPort.setStatus(_A)
_ZxAnEponRmVoipSipBackProxyServerIp_Type=IpAddress
_ZxAnEponRmVoipSipBackProxyServerIp_Object=MibTableColumn
zxAnEponRmVoipSipBackProxyServerIp=_ZxAnEponRmVoipSipBackProxyServerIp_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1,10),_ZxAnEponRmVoipSipBackProxyServerIp_Type())
zxAnEponRmVoipSipBackProxyServerIp.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipSipBackProxyServerIp.setStatus(_A)
class _ZxAnEponRmVoipSipBackProxyServerPort_Type(Integer32):defaultValue=5060;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1001,65535))
_ZxAnEponRmVoipSipBackProxyServerPort_Type.__name__=_B
_ZxAnEponRmVoipSipBackProxyServerPort_Object=MibTableColumn
zxAnEponRmVoipSipBackProxyServerPort=_ZxAnEponRmVoipSipBackProxyServerPort_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1,11),_ZxAnEponRmVoipSipBackProxyServerPort_Type())
zxAnEponRmVoipSipBackProxyServerPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipSipBackProxyServerPort.setStatus(_A)
_ZxAnEponRmVoipSipOutBoundServerIp_Type=IpAddress
_ZxAnEponRmVoipSipOutBoundServerIp_Object=MibTableColumn
zxAnEponRmVoipSipOutBoundServerIp=_ZxAnEponRmVoipSipOutBoundServerIp_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1,12),_ZxAnEponRmVoipSipOutBoundServerIp_Type())
zxAnEponRmVoipSipOutBoundServerIp.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipSipOutBoundServerIp.setStatus(_A)
class _ZxAnEponRmVoipSipOutBoundServerPort_Type(Integer32):defaultValue=5060;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1001,65535))
_ZxAnEponRmVoipSipOutBoundServerPort_Type.__name__=_B
_ZxAnEponRmVoipSipOutBoundServerPort_Object=MibTableColumn
zxAnEponRmVoipSipOutBoundServerPort=_ZxAnEponRmVoipSipOutBoundServerPort_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1,13),_ZxAnEponRmVoipSipOutBoundServerPort_Type())
zxAnEponRmVoipSipOutBoundServerPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipSipOutBoundServerPort.setStatus(_A)
class _ZxAnEponRmVoipSipRegInterval_Type(Integer32):defaultValue=3600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnEponRmVoipSipRegInterval_Type.__name__=_B
_ZxAnEponRmVoipSipRegInterval_Object=MibTableColumn
zxAnEponRmVoipSipRegInterval=_ZxAnEponRmVoipSipRegInterval_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1,14),_ZxAnEponRmVoipSipRegInterval_Type())
zxAnEponRmVoipSipRegInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipSipRegInterval.setStatus(_A)
class _ZxAnEponRmVoipSipHeartbeatSwitch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_ZxAnEponRmVoipSipHeartbeatSwitch_Type.__name__=_B
_ZxAnEponRmVoipSipHeartbeatSwitch_Object=MibTableColumn
zxAnEponRmVoipSipHeartbeatSwitch=_ZxAnEponRmVoipSipHeartbeatSwitch_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1,15),_ZxAnEponRmVoipSipHeartbeatSwitch_Type())
zxAnEponRmVoipSipHeartbeatSwitch.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipSipHeartbeatSwitch.setStatus(_A)
class _ZxAnEponRmVoipSipHeartbeatCycle_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnEponRmVoipSipHeartbeatCycle_Type.__name__=_B
_ZxAnEponRmVoipSipHeartbeatCycle_Object=MibTableColumn
zxAnEponRmVoipSipHeartbeatCycle=_ZxAnEponRmVoipSipHeartbeatCycle_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1,16),_ZxAnEponRmVoipSipHeartbeatCycle_Type())
zxAnEponRmVoipSipHeartbeatCycle.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipSipHeartbeatCycle.setStatus(_A)
class _ZxAnEponRmVoipSipHeartbeatCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ZxAnEponRmVoipSipHeartbeatCount_Type.__name__=_B
_ZxAnEponRmVoipSipHeartbeatCount_Object=MibTableColumn
zxAnEponRmVoipSipHeartbeatCount=_ZxAnEponRmVoipSipHeartbeatCount_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1,17),_ZxAnEponRmVoipSipHeartbeatCount_Type())
zxAnEponRmVoipSipHeartbeatCount.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipSipHeartbeatCount.setStatus(_A)
_ZxAnEponRmVoipSipRowStatus_Type=RowStatus
_ZxAnEponRmVoipSipRowStatus_Object=MibTableColumn
zxAnEponRmVoipSipRowStatus=_ZxAnEponRmVoipSipRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,10,1,30),_ZxAnEponRmVoipSipRowStatus_Type())
zxAnEponRmVoipSipRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipSipRowStatus.setStatus(_A)
_ZxAnEponRmVoipFaxProfileIdxNext_Type=Integer32
_ZxAnEponRmVoipFaxProfileIdxNext_Object=MibScalar
zxAnEponRmVoipFaxProfileIdxNext=_ZxAnEponRmVoipFaxProfileIdxNext_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,11),_ZxAnEponRmVoipFaxProfileIdxNext_Type())
zxAnEponRmVoipFaxProfileIdxNext.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipFaxProfileIdxNext.setStatus(_A)
_ZxAnEponRmVoipFaxProfileTable_Object=MibTable
zxAnEponRmVoipFaxProfileTable=_ZxAnEponRmVoipFaxProfileTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,12))
if mibBuilder.loadTexts:zxAnEponRmVoipFaxProfileTable.setStatus(_A)
_ZxAnEponRmVoipFaxProfileEntry_Object=MibTableRow
zxAnEponRmVoipFaxProfileEntry=_ZxAnEponRmVoipFaxProfileEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,12,1))
zxAnEponRmVoipFaxProfileEntry.setIndexNames((0,_E,_AF))
if mibBuilder.loadTexts:zxAnEponRmVoipFaxProfileEntry.setStatus(_A)
_ZxAnEponRmVoipFaxProfileIdx_Type=Integer32
_ZxAnEponRmVoipFaxProfileIdx_Object=MibTableColumn
zxAnEponRmVoipFaxProfileIdx=_ZxAnEponRmVoipFaxProfileIdx_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,12,1,1),_ZxAnEponRmVoipFaxProfileIdx_Type())
zxAnEponRmVoipFaxProfileIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponRmVoipFaxProfileIdx.setStatus(_A)
class _ZxAnEponRmVoipFaxProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnEponRmVoipFaxProfileName_Type.__name__=_L
_ZxAnEponRmVoipFaxProfileName_Object=MibTableColumn
zxAnEponRmVoipFaxProfileName=_ZxAnEponRmVoipFaxProfileName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,12,1,2),_ZxAnEponRmVoipFaxProfileName_Type())
zxAnEponRmVoipFaxProfileName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipFaxProfileName.setStatus(_A)
class _ZxAnEponRmVoipFaxMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('t30',1),('t38',2)))
_ZxAnEponRmVoipFaxMode_Type.__name__=_B
_ZxAnEponRmVoipFaxMode_Object=MibTableColumn
zxAnEponRmVoipFaxMode=_ZxAnEponRmVoipFaxMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,12,1,3),_ZxAnEponRmVoipFaxMode_Type())
zxAnEponRmVoipFaxMode.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipFaxMode.setStatus(_A)
class _ZxAnEponRmVoipFaxControlMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Y,1),('rtcp',2),('ss',3),('autoVbd',4)))
_ZxAnEponRmVoipFaxControlMode_Type.__name__=_B
_ZxAnEponRmVoipFaxControlMode_Object=MibTableColumn
zxAnEponRmVoipFaxControlMode=_ZxAnEponRmVoipFaxControlMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,12,1,4),_ZxAnEponRmVoipFaxControlMode_Type())
zxAnEponRmVoipFaxControlMode.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipFaxControlMode.setStatus(_A)
_ZxAnEponRmVoipFaxRowStatus_Type=RowStatus
_ZxAnEponRmVoipFaxRowStatus_Object=MibTableColumn
zxAnEponRmVoipFaxRowStatus=_ZxAnEponRmVoipFaxRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,35,12,1,30),_ZxAnEponRmVoipFaxRowStatus_Type())
zxAnEponRmVoipFaxRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipFaxRowStatus.setStatus(_A)
_ZxAnEponRmVoipMgmt_ObjectIdentity=ObjectIdentity
zxAnEponRmVoipMgmt=_ZxAnEponRmVoipMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,1,36))
_ZxAnEponRmVoipIpInfoTable_Object=MibTable
zxAnEponRmVoipIpInfoTable=_ZxAnEponRmVoipIpInfoTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,1))
if mibBuilder.loadTexts:zxAnEponRmVoipIpInfoTable.setStatus(_A)
_ZxAnEponRmVoipIpInfoEntry_Object=MibTableRow
zxAnEponRmVoipIpInfoEntry=_ZxAnEponRmVoipIpInfoEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,1,1))
zxAnEponRmVoipIpInfoEntry.setIndexNames((0,_E,_F),(0,_E,_M))
if mibBuilder.loadTexts:zxAnEponRmVoipIpInfoEntry.setStatus(_A)
_ZxAnEponOnuCardIndex_Type=Integer32
_ZxAnEponOnuCardIndex_Object=MibTableColumn
zxAnEponOnuCardIndex=_ZxAnEponOnuCardIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,1,1,1),_ZxAnEponOnuCardIndex_Type())
zxAnEponOnuCardIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuCardIndex.setStatus(_A)
_ZxAnEponRmVoipIpAddress_Type=IpAddress
_ZxAnEponRmVoipIpAddress_Object=MibTableColumn
zxAnEponRmVoipIpAddress=_ZxAnEponRmVoipIpAddress_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,1,1,2),_ZxAnEponRmVoipIpAddress_Type())
zxAnEponRmVoipIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipIpAddress.setStatus(_A)
_ZxAnEponRmVoipIpNetMask_Type=IpAddress
_ZxAnEponRmVoipIpNetMask_Object=MibTableColumn
zxAnEponRmVoipIpNetMask=_ZxAnEponRmVoipIpNetMask_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,1,1,3),_ZxAnEponRmVoipIpNetMask_Type())
zxAnEponRmVoipIpNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipIpNetMask.setStatus(_A)
_ZxAnEponRmVoipPppoeInfoTable_Object=MibTable
zxAnEponRmVoipPppoeInfoTable=_ZxAnEponRmVoipPppoeInfoTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,2))
if mibBuilder.loadTexts:zxAnEponRmVoipPppoeInfoTable.setStatus(_A)
_ZxAnEponRmVoipPppoeInfoEntry_Object=MibTableRow
zxAnEponRmVoipPppoeInfoEntry=_ZxAnEponRmVoipPppoeInfoEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,2,1))
zxAnEponRmVoipPppoeInfoEntry.setIndexNames((0,_E,_F),(0,_E,_M))
if mibBuilder.loadTexts:zxAnEponRmVoipPppoeInfoEntry.setStatus(_A)
class _ZxAnEponRmVoipPppoeUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnEponRmVoipPppoeUserName_Type.__name__=_L
_ZxAnEponRmVoipPppoeUserName_Object=MibTableColumn
zxAnEponRmVoipPppoeUserName=_ZxAnEponRmVoipPppoeUserName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,2,1,1),_ZxAnEponRmVoipPppoeUserName_Type())
zxAnEponRmVoipPppoeUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipPppoeUserName.setStatus(_A)
class _ZxAnEponRmVoipPppoePassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnEponRmVoipPppoePassword_Type.__name__=_L
_ZxAnEponRmVoipPppoePassword_Object=MibTableColumn
zxAnEponRmVoipPppoePassword=_ZxAnEponRmVoipPppoePassword_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,2,1,2),_ZxAnEponRmVoipPppoePassword_Type())
zxAnEponRmVoipPppoePassword.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipPppoePassword.setStatus(_A)
_ZxAnEponRmVoipH248MgcpAttrTable_Object=MibTable
zxAnEponRmVoipH248MgcpAttrTable=_ZxAnEponRmVoipH248MgcpAttrTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,3))
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpAttrTable.setStatus(_A)
_ZxAnEponRmVoipH248MgcpAttrEntry_Object=MibTableRow
zxAnEponRmVoipH248MgcpAttrEntry=_ZxAnEponRmVoipH248MgcpAttrEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,3,1))
zxAnEponRmVoipH248MgcpAttrEntry.setIndexNames((0,_E,_F),(0,_E,_M))
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpAttrEntry.setStatus(_A)
class _ZxAnEponRmVoipH248MgcpMID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ZxAnEponRmVoipH248MgcpMID_Type.__name__=_L
_ZxAnEponRmVoipH248MgcpMID_Object=MibTableColumn
zxAnEponRmVoipH248MgcpMID=_ZxAnEponRmVoipH248MgcpMID_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,3,1,1),_ZxAnEponRmVoipH248MgcpMID_Type())
zxAnEponRmVoipH248MgcpMID.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpMID.setStatus(_A)
class _ZxAnEponRmVoipH248MgcpActiveMgc_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AG,1),('primary',2)))
_ZxAnEponRmVoipH248MgcpActiveMgc_Type.__name__=_B
_ZxAnEponRmVoipH248MgcpActiveMgc_Object=MibTableColumn
zxAnEponRmVoipH248MgcpActiveMgc=_ZxAnEponRmVoipH248MgcpActiveMgc_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,3,1,2),_ZxAnEponRmVoipH248MgcpActiveMgc_Type())
zxAnEponRmVoipH248MgcpActiveMgc.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpActiveMgc.setStatus(_A)
_ZxAnEponRmVoipH248MgcpUserTidCfgTable_Object=MibTable
zxAnEponRmVoipH248MgcpUserTidCfgTable=_ZxAnEponRmVoipH248MgcpUserTidCfgTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,4))
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpUserTidCfgTable.setStatus(_A)
_ZxAnEponRmVoipH248MgcpUserTidCfgEntry_Object=MibTableRow
zxAnEponRmVoipH248MgcpUserTidCfgEntry=_ZxAnEponRmVoipH248MgcpUserTidCfgEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,4,1))
zxAnEponRmVoipH248MgcpUserTidCfgEntry.setIndexNames((0,_E,_F),(0,_E,_M),(0,_E,_AH))
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpUserTidCfgEntry.setStatus(_A)
_ZxAnEponRmVoipH248MgcpUserTidGroupIdx_Type=Integer32
_ZxAnEponRmVoipH248MgcpUserTidGroupIdx_Object=MibTableColumn
zxAnEponRmVoipH248MgcpUserTidGroupIdx=_ZxAnEponRmVoipH248MgcpUserTidGroupIdx_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,4,1,1),_ZxAnEponRmVoipH248MgcpUserTidGroupIdx_Type())
zxAnEponRmVoipH248MgcpUserTidGroupIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpUserTidGroupIdx.setStatus(_A)
class _ZxAnEponRmVoipH248MgcpUserTidBeginIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ZxAnEponRmVoipH248MgcpUserTidBeginIdx_Type.__name__=_B
_ZxAnEponRmVoipH248MgcpUserTidBeginIdx_Object=MibTableColumn
zxAnEponRmVoipH248MgcpUserTidBeginIdx=_ZxAnEponRmVoipH248MgcpUserTidBeginIdx_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,4,1,2),_ZxAnEponRmVoipH248MgcpUserTidBeginIdx_Type())
zxAnEponRmVoipH248MgcpUserTidBeginIdx.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpUserTidBeginIdx.setStatus(_A)
class _ZxAnEponRmVoipH248MgcpUserTidNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ZxAnEponRmVoipH248MgcpUserTidNumber_Type.__name__=_B
_ZxAnEponRmVoipH248MgcpUserTidNumber_Object=MibTableColumn
zxAnEponRmVoipH248MgcpUserTidNumber=_ZxAnEponRmVoipH248MgcpUserTidNumber_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,4,1,3),_ZxAnEponRmVoipH248MgcpUserTidNumber_Type())
zxAnEponRmVoipH248MgcpUserTidNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpUserTidNumber.setStatus(_A)
class _ZxAnEponRmVoipH248MgcpUserTidPrefix_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_ZxAnEponRmVoipH248MgcpUserTidPrefix_Type.__name__=_L
_ZxAnEponRmVoipH248MgcpUserTidPrefix_Object=MibTableColumn
zxAnEponRmVoipH248MgcpUserTidPrefix=_ZxAnEponRmVoipH248MgcpUserTidPrefix_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,4,1,4),_ZxAnEponRmVoipH248MgcpUserTidPrefix_Type())
zxAnEponRmVoipH248MgcpUserTidPrefix.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpUserTidPrefix.setStatus(_A)
class _ZxAnEponRmVoipH248MgcpUserTidBeginDigit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_ZxAnEponRmVoipH248MgcpUserTidBeginDigit_Type.__name__=_L
_ZxAnEponRmVoipH248MgcpUserTidBeginDigit_Object=MibTableColumn
zxAnEponRmVoipH248MgcpUserTidBeginDigit=_ZxAnEponRmVoipH248MgcpUserTidBeginDigit_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,4,1,5),_ZxAnEponRmVoipH248MgcpUserTidBeginDigit_Type())
zxAnEponRmVoipH248MgcpUserTidBeginDigit.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpUserTidBeginDigit.setStatus(_A)
class _ZxAnEponRmVoipH248MgcpUserTidDigitAlignMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('align',1),('noAlign',2)))
_ZxAnEponRmVoipH248MgcpUserTidDigitAlignMode_Type.__name__=_B
_ZxAnEponRmVoipH248MgcpUserTidDigitAlignMode_Object=MibTableColumn
zxAnEponRmVoipH248MgcpUserTidDigitAlignMode=_ZxAnEponRmVoipH248MgcpUserTidDigitAlignMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,4,1,6),_ZxAnEponRmVoipH248MgcpUserTidDigitAlignMode_Type())
zxAnEponRmVoipH248MgcpUserTidDigitAlignMode.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpUserTidDigitAlignMode.setStatus(_A)
class _ZxAnEponRmVoipH248MgcpUserTidDigitLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_ZxAnEponRmVoipH248MgcpUserTidDigitLength_Type.__name__=_B
_ZxAnEponRmVoipH248MgcpUserTidDigitLength_Object=MibTableColumn
zxAnEponRmVoipH248MgcpUserTidDigitLength=_ZxAnEponRmVoipH248MgcpUserTidDigitLength_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,4,1,7),_ZxAnEponRmVoipH248MgcpUserTidDigitLength_Type())
zxAnEponRmVoipH248MgcpUserTidDigitLength.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpUserTidDigitLength.setStatus(_A)
_ZxAnEponRmVoipH248MgcpUserTidRowStatus_Type=RowStatus
_ZxAnEponRmVoipH248MgcpUserTidRowStatus_Object=MibTableColumn
zxAnEponRmVoipH248MgcpUserTidRowStatus=_ZxAnEponRmVoipH248MgcpUserTidRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,4,1,30),_ZxAnEponRmVoipH248MgcpUserTidRowStatus_Type())
zxAnEponRmVoipH248MgcpUserTidRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpUserTidRowStatus.setStatus(_A)
_ZxAnEponRmVoipH248MgcpRtpTidCfgTable_Object=MibTable
zxAnEponRmVoipH248MgcpRtpTidCfgTable=_ZxAnEponRmVoipH248MgcpRtpTidCfgTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,5))
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpRtpTidCfgTable.setStatus(_A)
_ZxAnEponRmVoipH248MgcpRtpTidCfgEntry_Object=MibTableRow
zxAnEponRmVoipH248MgcpRtpTidCfgEntry=_ZxAnEponRmVoipH248MgcpRtpTidCfgEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,5,1))
zxAnEponRmVoipH248MgcpRtpTidCfgEntry.setIndexNames((0,_E,_F),(0,_E,_M))
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpRtpTidCfgEntry.setStatus(_A)
class _ZxAnEponRmVoipH248MgcpRtpTidPrefix_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_ZxAnEponRmVoipH248MgcpRtpTidPrefix_Type.__name__=_L
_ZxAnEponRmVoipH248MgcpRtpTidPrefix_Object=MibTableColumn
zxAnEponRmVoipH248MgcpRtpTidPrefix=_ZxAnEponRmVoipH248MgcpRtpTidPrefix_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,5,1,1),_ZxAnEponRmVoipH248MgcpRtpTidPrefix_Type())
zxAnEponRmVoipH248MgcpRtpTidPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpRtpTidPrefix.setStatus(_A)
class _ZxAnEponRmVoipH248MgcpRtpTidBeginDigit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_ZxAnEponRmVoipH248MgcpRtpTidBeginDigit_Type.__name__=_L
_ZxAnEponRmVoipH248MgcpRtpTidBeginDigit_Object=MibTableColumn
zxAnEponRmVoipH248MgcpRtpTidBeginDigit=_ZxAnEponRmVoipH248MgcpRtpTidBeginDigit_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,5,1,2),_ZxAnEponRmVoipH248MgcpRtpTidBeginDigit_Type())
zxAnEponRmVoipH248MgcpRtpTidBeginDigit.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpRtpTidBeginDigit.setStatus(_A)
class _ZxAnEponRmVoipH248MgcpRtpTidDigitAlignMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('align',1),('noAlign',2)))
_ZxAnEponRmVoipH248MgcpRtpTidDigitAlignMode_Type.__name__=_B
_ZxAnEponRmVoipH248MgcpRtpTidDigitAlignMode_Object=MibTableColumn
zxAnEponRmVoipH248MgcpRtpTidDigitAlignMode=_ZxAnEponRmVoipH248MgcpRtpTidDigitAlignMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,5,1,3),_ZxAnEponRmVoipH248MgcpRtpTidDigitAlignMode_Type())
zxAnEponRmVoipH248MgcpRtpTidDigitAlignMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpRtpTidDigitAlignMode.setStatus(_A)
class _ZxAnEponRmVoipH248MgcpRtpTidDigitLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_ZxAnEponRmVoipH248MgcpRtpTidDigitLength_Type.__name__=_B
_ZxAnEponRmVoipH248MgcpRtpTidDigitLength_Object=MibTableColumn
zxAnEponRmVoipH248MgcpRtpTidDigitLength=_ZxAnEponRmVoipH248MgcpRtpTidDigitLength_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,5,1,4),_ZxAnEponRmVoipH248MgcpRtpTidDigitLength_Type())
zxAnEponRmVoipH248MgcpRtpTidDigitLength.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpRtpTidDigitLength.setStatus(_A)
class _ZxAnEponRmVoipH248MgcpRtpTidNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ZxAnEponRmVoipH248MgcpRtpTidNum_Type.__name__=_B
_ZxAnEponRmVoipH248MgcpRtpTidNum_Object=MibTableColumn
zxAnEponRmVoipH248MgcpRtpTidNum=_ZxAnEponRmVoipH248MgcpRtpTidNum_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,5,1,5),_ZxAnEponRmVoipH248MgcpRtpTidNum_Type())
zxAnEponRmVoipH248MgcpRtpTidNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpRtpTidNum.setStatus(_A)
_ZxAnEponRmVoipSipUserCfgTable_Object=MibTable
zxAnEponRmVoipSipUserCfgTable=_ZxAnEponRmVoipSipUserCfgTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,6))
if mibBuilder.loadTexts:zxAnEponRmVoipSipUserCfgTable.setStatus(_A)
_ZxAnEponRmVoipSipUserCfgEntry_Object=MibTableRow
zxAnEponRmVoipSipUserCfgEntry=_ZxAnEponRmVoipSipUserCfgEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,6,1))
zxAnEponRmVoipSipUserCfgEntry.setIndexNames((0,_E,_F),(0,_E,_M),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponRmVoipSipUserCfgEntry.setStatus(_A)
class _ZxAnEponRmVoipSipUserAccount_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_ZxAnEponRmVoipSipUserAccount_Type.__name__=_L
_ZxAnEponRmVoipSipUserAccount_Object=MibTableColumn
zxAnEponRmVoipSipUserAccount=_ZxAnEponRmVoipSipUserAccount_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,6,1,1),_ZxAnEponRmVoipSipUserAccount_Type())
zxAnEponRmVoipSipUserAccount.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipSipUserAccount.setStatus(_A)
class _ZxAnEponRmVoipSipUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnEponRmVoipSipUserName_Type.__name__=_L
_ZxAnEponRmVoipSipUserName_Object=MibTableColumn
zxAnEponRmVoipSipUserName=_ZxAnEponRmVoipSipUserName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,6,1,2),_ZxAnEponRmVoipSipUserName_Type())
zxAnEponRmVoipSipUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipSipUserName.setStatus(_A)
class _ZxAnEponRmVoipSipUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_ZxAnEponRmVoipSipUserPassword_Type.__name__=_L
_ZxAnEponRmVoipSipUserPassword_Object=MibTableColumn
zxAnEponRmVoipSipUserPassword=_ZxAnEponRmVoipSipUserPassword_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,6,1,3),_ZxAnEponRmVoipSipUserPassword_Type())
zxAnEponRmVoipSipUserPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipSipUserPassword.setStatus(_A)
_ZxAnEponRmVoipBaseInfoTable_Object=MibTable
zxAnEponRmVoipBaseInfoTable=_ZxAnEponRmVoipBaseInfoTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,7))
if mibBuilder.loadTexts:zxAnEponRmVoipBaseInfoTable.setStatus(_A)
_ZxAnEponRmVoipBaseInfoEntry_Object=MibTableRow
zxAnEponRmVoipBaseInfoEntry=_ZxAnEponRmVoipBaseInfoEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,7,1))
zxAnEponRmVoipBaseInfoEntry.setIndexNames((0,_E,_F),(0,_E,_M))
if mibBuilder.loadTexts:zxAnEponRmVoipBaseInfoEntry.setStatus(_A)
_ZxAnEponRmVoipMacAddress_Type=MacAddress
_ZxAnEponRmVoipMacAddress_Object=MibTableColumn
zxAnEponRmVoipMacAddress=_ZxAnEponRmVoipMacAddress_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,7,1,1),_ZxAnEponRmVoipMacAddress_Type())
zxAnEponRmVoipMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipMacAddress.setStatus(_A)
class _ZxAnEponRmVoipProtocolSupported_Type(Bits):namedValues=NamedValues(*((_h,0),(_i,1),(_Z,2)))
_ZxAnEponRmVoipProtocolSupported_Type.__name__=_O
_ZxAnEponRmVoipProtocolSupported_Object=MibTableColumn
zxAnEponRmVoipProtocolSupported=_ZxAnEponRmVoipProtocolSupported_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,7,1,2),_ZxAnEponRmVoipProtocolSupported_Type())
zxAnEponRmVoipProtocolSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipProtocolSupported.setStatus(_A)
class _ZxAnEponRmVoipSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnEponRmVoipSoftwareVersion_Type.__name__=_L
_ZxAnEponRmVoipSoftwareVersion_Object=MibTableColumn
zxAnEponRmVoipSoftwareVersion=_ZxAnEponRmVoipSoftwareVersion_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,7,1,3),_ZxAnEponRmVoipSoftwareVersion_Type())
zxAnEponRmVoipSoftwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipSoftwareVersion.setStatus(_A)
class _ZxAnEponRmVoipSoftwareVersionTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnEponRmVoipSoftwareVersionTime_Type.__name__=_L
_ZxAnEponRmVoipSoftwareVersionTime_Object=MibTableColumn
zxAnEponRmVoipSoftwareVersionTime=_ZxAnEponRmVoipSoftwareVersionTime_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,7,1,4),_ZxAnEponRmVoipSoftwareVersionTime_Type())
zxAnEponRmVoipSoftwareVersionTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipSoftwareVersionTime.setStatus(_A)
_ZxAnEponRmVoipUserCount_Type=Integer32
_ZxAnEponRmVoipUserCount_Object=MibTableColumn
zxAnEponRmVoipUserCount=_ZxAnEponRmVoipUserCount_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,7,1,5),_ZxAnEponRmVoipUserCount_Type())
zxAnEponRmVoipUserCount.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipUserCount.setStatus(_A)
class _ZxAnEponRmVoipProtocolUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_h,1),(_i,2),(_Z,3)))
_ZxAnEponRmVoipProtocolUsed_Type.__name__=_B
_ZxAnEponRmVoipProtocolUsed_Object=MibTableColumn
zxAnEponRmVoipProtocolUsed=_ZxAnEponRmVoipProtocolUsed_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,7,1,6),_ZxAnEponRmVoipProtocolUsed_Type())
zxAnEponRmVoipProtocolUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipProtocolUsed.setStatus(_A)
_ZxAnEponRmVoipH248MgcpUserTidInfoTable_Object=MibTable
zxAnEponRmVoipH248MgcpUserTidInfoTable=_ZxAnEponRmVoipH248MgcpUserTidInfoTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,8))
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpUserTidInfoTable.setStatus(_A)
_ZxAnEponRmVoipH248MgcpUserTidInfoEntry_Object=MibTableRow
zxAnEponRmVoipH248MgcpUserTidInfoEntry=_ZxAnEponRmVoipH248MgcpUserTidInfoEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,8,1))
zxAnEponRmVoipH248MgcpUserTidInfoEntry.setIndexNames((0,_E,_F),(0,_E,_M),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpUserTidInfoEntry.setStatus(_A)
class _ZxAnEponRmVoipH248MgcpUserTidName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnEponRmVoipH248MgcpUserTidName_Type.__name__=_L
_ZxAnEponRmVoipH248MgcpUserTidName_Object=MibTableColumn
zxAnEponRmVoipH248MgcpUserTidName=_ZxAnEponRmVoipH248MgcpUserTidName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,8,1,1),_ZxAnEponRmVoipH248MgcpUserTidName_Type())
zxAnEponRmVoipH248MgcpUserTidName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpUserTidName.setStatus(_A)
_ZxAnEponRmVoipH248MgcpRtpTidInfoTable_Object=MibTable
zxAnEponRmVoipH248MgcpRtpTidInfoTable=_ZxAnEponRmVoipH248MgcpRtpTidInfoTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,9))
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpRtpTidInfoTable.setStatus(_A)
_ZxAnEponRmVoipH248MgcpRtpTidInfoEntry_Object=MibTableRow
zxAnEponRmVoipH248MgcpRtpTidInfoEntry=_ZxAnEponRmVoipH248MgcpRtpTidInfoEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,9,1))
zxAnEponRmVoipH248MgcpRtpTidInfoEntry.setIndexNames((0,_E,_F),(0,_E,_M))
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpRtpTidInfoEntry.setStatus(_A)
_ZxAnEponRmVoipH248MgcpRtpTidNumber_Type=Integer32
_ZxAnEponRmVoipH248MgcpRtpTidNumber_Object=MibTableColumn
zxAnEponRmVoipH248MgcpRtpTidNumber=_ZxAnEponRmVoipH248MgcpRtpTidNumber_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,9,1,1),_ZxAnEponRmVoipH248MgcpRtpTidNumber_Type())
zxAnEponRmVoipH248MgcpRtpTidNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpRtpTidNumber.setStatus(_A)
class _ZxAnEponRmVoipH248MgcpRtpTidFirstName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnEponRmVoipH248MgcpRtpTidFirstName_Type.__name__=_L
_ZxAnEponRmVoipH248MgcpRtpTidFirstName_Object=MibTableColumn
zxAnEponRmVoipH248MgcpRtpTidFirstName=_ZxAnEponRmVoipH248MgcpRtpTidFirstName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,9,1,2),_ZxAnEponRmVoipH248MgcpRtpTidFirstName_Type())
zxAnEponRmVoipH248MgcpRtpTidFirstName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipH248MgcpRtpTidFirstName.setStatus(_A)
_ZxAnEponRmVoipModuleStatusTable_Object=MibTable
zxAnEponRmVoipModuleStatusTable=_ZxAnEponRmVoipModuleStatusTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,10))
if mibBuilder.loadTexts:zxAnEponRmVoipModuleStatusTable.setStatus(_A)
_ZxAnEponRmVoipModuleStatusEntry_Object=MibTableRow
zxAnEponRmVoipModuleStatusEntry=_ZxAnEponRmVoipModuleStatusEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,10,1))
zxAnEponRmVoipModuleStatusEntry.setIndexNames((0,_E,_F),(0,_E,_M))
if mibBuilder.loadTexts:zxAnEponRmVoipModuleStatusEntry.setStatus(_A)
class _ZxAnEponRmVoipModuleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,255)));namedValues=NamedValues(*((_AI,1),('registerSuccess',2),('fault',3),(_j,4),(_AJ,5),(_k,255)))
_ZxAnEponRmVoipModuleStatus_Type.__name__=_B
_ZxAnEponRmVoipModuleStatus_Object=MibTableColumn
zxAnEponRmVoipModuleStatus=_ZxAnEponRmVoipModuleStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,10,1,1),_ZxAnEponRmVoipModuleStatus_Type())
zxAnEponRmVoipModuleStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipModuleStatus.setStatus(_A)
class _ZxAnEponRmVoipModuleAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('register',1),(_j,2),(_l,3),('restore',4)))
_ZxAnEponRmVoipModuleAction_Type.__name__=_B
_ZxAnEponRmVoipModuleAction_Object=MibTableColumn
zxAnEponRmVoipModuleAction=_ZxAnEponRmVoipModuleAction_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,10,1,2),_ZxAnEponRmVoipModuleAction_Type())
zxAnEponRmVoipModuleAction.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipModuleAction.setStatus(_A)
_ZxAnEponRmVoipUserIfStatusTable_Object=MibTable
zxAnEponRmVoipUserIfStatusTable=_ZxAnEponRmVoipUserIfStatusTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,11))
if mibBuilder.loadTexts:zxAnEponRmVoipUserIfStatusTable.setStatus(_A)
_ZxAnEponRmVoipUserIfStatusEntry_Object=MibTableRow
zxAnEponRmVoipUserIfStatusEntry=_ZxAnEponRmVoipUserIfStatusEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,11,1))
zxAnEponRmVoipUserIfStatusEntry.setIndexNames((0,_E,_F),(0,_E,_M),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponRmVoipUserIfStatusEntry.setStatus(_A)
class _ZxAnEponRmVoipPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_AI,1),('idle',2),('hold',3),('dialing',4),('ringing',5),('ringingBack',6),('connecting',7),('connected',8),('releasing',9),('busy',10),('registerFail',11),(_U,12)))
_ZxAnEponRmVoipPortOperStatus_Type.__name__=_B
_ZxAnEponRmVoipPortOperStatus_Object=MibTableColumn
zxAnEponRmVoipPortOperStatus=_ZxAnEponRmVoipPortOperStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,11,1,1),_ZxAnEponRmVoipPortOperStatus_Type())
zxAnEponRmVoipPortOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipPortOperStatus.setStatus(_A)
class _ZxAnEponRmVoipPortServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('normal',1),('innerSpc',2),('ipSpc',3),(_AK,4),(_AL,5)))
_ZxAnEponRmVoipPortServiceType_Type.__name__=_B
_ZxAnEponRmVoipPortServiceType_Object=MibTableColumn
zxAnEponRmVoipPortServiceType=_ZxAnEponRmVoipPortServiceType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,11,1,2),_ZxAnEponRmVoipPortServiceType_Type())
zxAnEponRmVoipPortServiceType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipPortServiceType.setStatus(_A)
class _ZxAnEponRmVoipPortServiceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('endLocal',1),('endRemote',2),('endAuto',3),('normalState',4)))
_ZxAnEponRmVoipPortServiceState_Type.__name__=_B
_ZxAnEponRmVoipPortServiceState_Object=MibTableColumn
zxAnEponRmVoipPortServiceState=_ZxAnEponRmVoipPortServiceState_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,11,1,3),_ZxAnEponRmVoipPortServiceState_Type())
zxAnEponRmVoipPortServiceState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipPortServiceState.setStatus(_A)
class _ZxAnEponRmVoipPortCodecMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('g711U',1),('g711A',2),('g723',3),('g729',4),('g726',5),('t38',6),('connectionless',7),(_k,8)))
_ZxAnEponRmVoipPortCodecMode_Type.__name__=_B
_ZxAnEponRmVoipPortCodecMode_Object=MibTableColumn
zxAnEponRmVoipPortCodecMode=_ZxAnEponRmVoipPortCodecMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,11,1,4),_ZxAnEponRmVoipPortCodecMode_Type())
zxAnEponRmVoipPortCodecMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipPortCodecMode.setStatus(_A)
class _ZxAnEponRmVoipPortAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('register',1),(_j,2)))
_ZxAnEponRmVoipPortAction_Type.__name__=_B
_ZxAnEponRmVoipPortAction_Object=MibTableColumn
zxAnEponRmVoipPortAction=_ZxAnEponRmVoipPortAction_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,11,1,5),_ZxAnEponRmVoipPortAction_Type())
zxAnEponRmVoipPortAction.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipPortAction.setStatus(_A)
class _ZxAnEponRmVoipPortReversalCtrl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponRmVoipPortReversalCtrl_Type.__name__=_B
_ZxAnEponRmVoipPortReversalCtrl_Object=MibTableColumn
zxAnEponRmVoipPortReversalCtrl=_ZxAnEponRmVoipPortReversalCtrl_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,11,1,6),_ZxAnEponRmVoipPortReversalCtrl_Type())
zxAnEponRmVoipPortReversalCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipPortReversalCtrl.setStatus(_A)
_ZxAnEponRmVoipPortPcmToPktGain_Type=Integer32
_ZxAnEponRmVoipPortPcmToPktGain_Object=MibTableColumn
zxAnEponRmVoipPortPcmToPktGain=_ZxAnEponRmVoipPortPcmToPktGain_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,11,1,7),_ZxAnEponRmVoipPortPcmToPktGain_Type())
zxAnEponRmVoipPortPcmToPktGain.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipPortPcmToPktGain.setStatus(_A)
_ZxAnEponRmVoipPortPktToPcmGain_Type=Integer32
_ZxAnEponRmVoipPortPktToPcmGain_Object=MibTableColumn
zxAnEponRmVoipPortPktToPcmGain=_ZxAnEponRmVoipPortPktToPcmGain_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,11,1,8),_ZxAnEponRmVoipPortPktToPcmGain_Type())
zxAnEponRmVoipPortPktToPcmGain.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipPortPktToPcmGain.setStatus(_A)
_ZxAnEponRmVoipProfileApplyTable_Object=MibTable
zxAnEponRmVoipProfileApplyTable=_ZxAnEponRmVoipProfileApplyTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,12))
if mibBuilder.loadTexts:zxAnEponRmVoipProfileApplyTable.setStatus(_A)
_ZxAnEponRmVoipProfileApplyEntry_Object=MibTableRow
zxAnEponRmVoipProfileApplyEntry=_ZxAnEponRmVoipProfileApplyEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,12,1))
zxAnEponRmVoipProfileApplyEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponRmVoipProfileApplyEntry.setStatus(_A)
_ZxAnEponRmVoipCurrIpProfileIdx_Type=Integer32
_ZxAnEponRmVoipCurrIpProfileIdx_Object=MibTableColumn
zxAnEponRmVoipCurrIpProfileIdx=_ZxAnEponRmVoipCurrIpProfileIdx_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,12,1,1),_ZxAnEponRmVoipCurrIpProfileIdx_Type())
zxAnEponRmVoipCurrIpProfileIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipCurrIpProfileIdx.setStatus(_A)
_ZxAnEponRmVoipCurrVlanProfileIdx_Type=Integer32
_ZxAnEponRmVoipCurrVlanProfileIdx_Object=MibTableColumn
zxAnEponRmVoipCurrVlanProfileIdx=_ZxAnEponRmVoipCurrVlanProfileIdx_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,12,1,2),_ZxAnEponRmVoipCurrVlanProfileIdx_Type())
zxAnEponRmVoipCurrVlanProfileIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipCurrVlanProfileIdx.setStatus(_A)
class _ZxAnEponRmVoipCurrProtocolProfileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_h,1),(_i,2),(_Z,3)))
_ZxAnEponRmVoipCurrProtocolProfileType_Type.__name__=_B
_ZxAnEponRmVoipCurrProtocolProfileType_Object=MibTableColumn
zxAnEponRmVoipCurrProtocolProfileType=_ZxAnEponRmVoipCurrProtocolProfileType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,12,1,3),_ZxAnEponRmVoipCurrProtocolProfileType_Type())
zxAnEponRmVoipCurrProtocolProfileType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipCurrProtocolProfileType.setStatus(_A)
_ZxAnEponRmVoipCurrProtocolProfileIdx_Type=Integer32
_ZxAnEponRmVoipCurrProtocolProfileIdx_Object=MibTableColumn
zxAnEponRmVoipCurrProtocolProfileIdx=_ZxAnEponRmVoipCurrProtocolProfileIdx_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,12,1,4),_ZxAnEponRmVoipCurrProtocolProfileIdx_Type())
zxAnEponRmVoipCurrProtocolProfileIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipCurrProtocolProfileIdx.setStatus(_A)
_ZxAnEponRmVoipCurrFaxProfileIdx_Type=Integer32
_ZxAnEponRmVoipCurrFaxProfileIdx_Object=MibTableColumn
zxAnEponRmVoipCurrFaxProfileIdx=_ZxAnEponRmVoipCurrFaxProfileIdx_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,12,1,5),_ZxAnEponRmVoipCurrFaxProfileIdx_Type())
zxAnEponRmVoipCurrFaxProfileIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmVoipCurrFaxProfileIdx.setStatus(_A)
_ZxAnEponRmVoipSipAttrTable_Object=MibTable
zxAnEponRmVoipSipAttrTable=_ZxAnEponRmVoipSipAttrTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,13))
if mibBuilder.loadTexts:zxAnEponRmVoipSipAttrTable.setStatus(_A)
_ZxAnEponRmVoipSipAttrEntry_Object=MibTableRow
zxAnEponRmVoipSipAttrEntry=_ZxAnEponRmVoipSipAttrEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,13,1))
zxAnEponRmVoipSipAttrEntry.setIndexNames((0,_E,_F),(0,_E,_M))
if mibBuilder.loadTexts:zxAnEponRmVoipSipAttrEntry.setStatus(_A)
class _ZxAnEponRmVoipSipActiveProxyServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AG,1),('primary',2)))
_ZxAnEponRmVoipSipActiveProxyServer_Type.__name__=_B
_ZxAnEponRmVoipSipActiveProxyServer_Object=MibTableColumn
zxAnEponRmVoipSipActiveProxyServer=_ZxAnEponRmVoipSipActiveProxyServer_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,13,1,1),_ZxAnEponRmVoipSipActiveProxyServer_Type())
zxAnEponRmVoipSipActiveProxyServer.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmVoipSipActiveProxyServer.setStatus(_A)
_ZxAnEponRmVoipSipDigitMapTable_Object=MibTable
zxAnEponRmVoipSipDigitMapTable=_ZxAnEponRmVoipSipDigitMapTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,14))
if mibBuilder.loadTexts:zxAnEponRmVoipSipDigitMapTable.setStatus(_A)
_ZxAnEponRmVoipSipDigitMapEntry_Object=MibTableRow
zxAnEponRmVoipSipDigitMapEntry=_ZxAnEponRmVoipSipDigitMapEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,14,1))
zxAnEponRmVoipSipDigitMapEntry.setIndexNames((0,_E,_F),(0,_E,_M))
if mibBuilder.loadTexts:zxAnEponRmVoipSipDigitMapEntry.setStatus(_A)
class _ZxEponRmVoipSipDigitMap_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1024))
_ZxEponRmVoipSipDigitMap_Type.__name__=_L
_ZxEponRmVoipSipDigitMap_Object=MibTableColumn
zxEponRmVoipSipDigitMap=_ZxEponRmVoipSipDigitMap_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,14,1,1),_ZxEponRmVoipSipDigitMap_Type())
zxEponRmVoipSipDigitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponRmVoipSipDigitMap.setStatus(_A)
_ZxAnEponOnuVoipPresentingTable_Object=MibTable
zxAnEponOnuVoipPresentingTable=_ZxAnEponOnuVoipPresentingTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,15))
if mibBuilder.loadTexts:zxAnEponOnuVoipPresentingTable.setStatus(_A)
_ZxAnEponOnuVoipPresentingEntry_Object=MibTableRow
zxAnEponOnuVoipPresentingEntry=_ZxAnEponOnuVoipPresentingEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,15,1))
zxAnEponOnuVoipPresentingEntry.setIndexNames((0,_E,_F),(0,_E,_M),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuVoipPresentingEntry.setStatus(_A)
class _ZxAnEponOnuVoipPresentingCallNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZxAnEponOnuVoipPresentingCallNbrState_Type.__name__=_B
_ZxAnEponOnuVoipPresentingCallNbrState_Object=MibTableColumn
zxAnEponOnuVoipPresentingCallNbrState=_ZxAnEponOnuVoipPresentingCallNbrState_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,15,1,1),_ZxAnEponOnuVoipPresentingCallNbrState_Type())
zxAnEponOnuVoipPresentingCallNbrState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoipPresentingCallNbrState.setStatus(_A)
class _ZxAnEponOnuVoipPresentingCallNbrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fsk',1),('dtmf',2)))
_ZxAnEponOnuVoipPresentingCallNbrType_Type.__name__=_B
_ZxAnEponOnuVoipPresentingCallNbrType_Object=MibTableColumn
zxAnEponOnuVoipPresentingCallNbrType=_ZxAnEponOnuVoipPresentingCallNbrType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,15,1,2),_ZxAnEponOnuVoipPresentingCallNbrType_Type())
zxAnEponOnuVoipPresentingCallNbrType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoipPresentingCallNbrType.setStatus(_A)
_ZxAnEponOnuVoipTimerConfigTable_Object=MibTable
zxAnEponOnuVoipTimerConfigTable=_ZxAnEponOnuVoipTimerConfigTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,16))
if mibBuilder.loadTexts:zxAnEponOnuVoipTimerConfigTable.setStatus(_A)
_ZxAnEponOnuVoipTimerConfigEntry_Object=MibTableRow
zxAnEponOnuVoipTimerConfigEntry=_ZxAnEponOnuVoipTimerConfigEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,16,1))
zxAnEponOnuVoipTimerConfigEntry.setIndexNames((0,_E,_F),(0,_E,_M))
if mibBuilder.loadTexts:zxAnEponOnuVoipTimerConfigEntry.setStatus(_A)
class _ZxAnEponOnuVoipTimerConfigDml_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_ZxAnEponOnuVoipTimerConfigDml_Type.__name__=_B
_ZxAnEponOnuVoipTimerConfigDml_Object=MibTableColumn
zxAnEponOnuVoipTimerConfigDml=_ZxAnEponOnuVoipTimerConfigDml_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,16,1,1),_ZxAnEponOnuVoipTimerConfigDml_Type())
zxAnEponOnuVoipTimerConfigDml.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoipTimerConfigDml.setStatus(_A)
class _ZxAnEponOnuVoipTimerConfigDms_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_ZxAnEponOnuVoipTimerConfigDms_Type.__name__=_B
_ZxAnEponOnuVoipTimerConfigDms_Object=MibTableColumn
zxAnEponOnuVoipTimerConfigDms=_ZxAnEponOnuVoipTimerConfigDms_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,16,1,2),_ZxAnEponOnuVoipTimerConfigDms_Type())
zxAnEponOnuVoipTimerConfigDms.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoipTimerConfigDms.setStatus(_A)
_ZxAnEponOnuVoipStatsTable_Object=MibTable
zxAnEponOnuVoipStatsTable=_ZxAnEponOnuVoipStatsTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,17))
if mibBuilder.loadTexts:zxAnEponOnuVoipStatsTable.setStatus(_A)
_ZxAnEponOnuVoipStatsEntry_Object=MibTableRow
zxAnEponOnuVoipStatsEntry=_ZxAnEponOnuVoipStatsEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,17,1))
zxAnEponOnuVoipStatsEntry.setIndexNames((0,_E,_F),(0,_E,_M),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuVoipStatsEntry.setStatus(_A)
_ZxAnEponOnuVoipRxPkts_Type=Counter64
_ZxAnEponOnuVoipRxPkts_Object=MibTableColumn
zxAnEponOnuVoipRxPkts=_ZxAnEponOnuVoipRxPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,17,1,1),_ZxAnEponOnuVoipRxPkts_Type())
zxAnEponOnuVoipRxPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVoipRxPkts.setStatus(_A)
_ZxAnEponOnuVoipTxPkts_Type=Counter64
_ZxAnEponOnuVoipTxPkts_Object=MibTableColumn
zxAnEponOnuVoipTxPkts=_ZxAnEponOnuVoipTxPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,17,1,2),_ZxAnEponOnuVoipTxPkts_Type())
zxAnEponOnuVoipTxPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVoipTxPkts.setStatus(_A)
class _ZxAnEponOnuVoipAverageDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnEponOnuVoipAverageDelay_Type.__name__=_B
_ZxAnEponOnuVoipAverageDelay_Object=MibTableColumn
zxAnEponOnuVoipAverageDelay=_ZxAnEponOnuVoipAverageDelay_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,17,1,3),_ZxAnEponOnuVoipAverageDelay_Type())
zxAnEponOnuVoipAverageDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVoipAverageDelay.setStatus(_A)
class _ZxAnEponOnuVoipAverageJitter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnEponOnuVoipAverageJitter_Type.__name__=_B
_ZxAnEponOnuVoipAverageJitter_Object=MibTableColumn
zxAnEponOnuVoipAverageJitter=_ZxAnEponOnuVoipAverageJitter_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,17,1,4),_ZxAnEponOnuVoipAverageJitter_Type())
zxAnEponOnuVoipAverageJitter.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVoipAverageJitter.setStatus(_A)
class _ZxAnEponOnuVoipLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnEponOnuVoipLoss_Type.__name__=_B
_ZxAnEponOnuVoipLoss_Object=MibTableColumn
zxAnEponOnuVoipLoss=_ZxAnEponOnuVoipLoss_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,17,1,5),_ZxAnEponOnuVoipLoss_Type())
zxAnEponOnuVoipLoss.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVoipLoss.setStatus(_A)
_ZxAnEponRmUniVoipRxMediaDataRate_Type=Gauge32
_ZxAnEponRmUniVoipRxMediaDataRate_Object=MibTableColumn
zxAnEponRmUniVoipRxMediaDataRate=_ZxAnEponRmUniVoipRxMediaDataRate_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,17,1,6),_ZxAnEponRmUniVoipRxMediaDataRate_Type())
zxAnEponRmUniVoipRxMediaDataRate.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmUniVoipRxMediaDataRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponRmUniVoipRxMediaDataRate.setUnits(_m)
_ZxAnEponRmUniVoipTxMediaDataRate_Type=Gauge32
_ZxAnEponRmUniVoipTxMediaDataRate_Object=MibTableColumn
zxAnEponRmUniVoipTxMediaDataRate=_ZxAnEponRmUniVoipTxMediaDataRate_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,17,1,7),_ZxAnEponRmUniVoipTxMediaDataRate_Type())
zxAnEponRmUniVoipTxMediaDataRate.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmUniVoipTxMediaDataRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponRmUniVoipTxMediaDataRate.setUnits(_m)
_ZxAnEponRmUniVoipCurCallDuration_Type=Unsigned32
_ZxAnEponRmUniVoipCurCallDuration_Object=MibTableColumn
zxAnEponRmUniVoipCurCallDuration=_ZxAnEponRmUniVoipCurCallDuration_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,17,1,8),_ZxAnEponRmUniVoipCurCallDuration_Type())
zxAnEponRmUniVoipCurCallDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmUniVoipCurCallDuration.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponRmUniVoipCurCallDuration.setUnits(_W)
_ZxAnEponRmUniVoipTotCallDuration_Type=Unsigned32
_ZxAnEponRmUniVoipTotCallDuration_Object=MibTableColumn
zxAnEponRmUniVoipTotCallDuration=_ZxAnEponRmUniVoipTotCallDuration_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,17,1,9),_ZxAnEponRmUniVoipTotCallDuration_Type())
zxAnEponRmUniVoipTotCallDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmUniVoipTotCallDuration.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponRmUniVoipTotCallDuration.setUnits(_W)
_ZxAnEponRmUniVoipCallTimes_Type=Unsigned32
_ZxAnEponRmUniVoipCallTimes_Object=MibTableColumn
zxAnEponRmUniVoipCallTimes=_ZxAnEponRmUniVoipCallTimes_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,17,1,10),_ZxAnEponRmUniVoipCallTimes_Type())
zxAnEponRmUniVoipCallTimes.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmUniVoipCallTimes.setStatus(_A)
_ZxAnEponOnuVoipOtherConfigTable_Object=MibTable
zxAnEponOnuVoipOtherConfigTable=_ZxAnEponOnuVoipOtherConfigTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,18))
if mibBuilder.loadTexts:zxAnEponOnuVoipOtherConfigTable.setStatus(_A)
_ZxAnEponOnuVoipOtherConfigEntry_Object=MibTableRow
zxAnEponOnuVoipOtherConfigEntry=_ZxAnEponOnuVoipOtherConfigEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,18,1))
zxAnEponOnuVoipOtherConfigEntry.setIndexNames((0,_E,_F),(0,_E,_M))
if mibBuilder.loadTexts:zxAnEponOnuVoipOtherConfigEntry.setStatus(_A)
class _ZxAnEponOnuVoipComfortableNoise_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuVoipComfortableNoise_Type.__name__=_B
_ZxAnEponOnuVoipComfortableNoise_Object=MibTableColumn
zxAnEponOnuVoipComfortableNoise=_ZxAnEponOnuVoipComfortableNoise_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,18,1,1),_ZxAnEponOnuVoipComfortableNoise_Type())
zxAnEponOnuVoipComfortableNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoipComfortableNoise.setStatus(_A)
class _ZxAnEponOnuVoipSilenceDetection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuVoipSilenceDetection_Type.__name__=_B
_ZxAnEponOnuVoipSilenceDetection_Object=MibTableColumn
zxAnEponOnuVoipSilenceDetection=_ZxAnEponOnuVoipSilenceDetection_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,18,1,2),_ZxAnEponOnuVoipSilenceDetection_Type())
zxAnEponOnuVoipSilenceDetection.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoipSilenceDetection.setStatus(_A)
class _ZxAnEponOnuVoipEchoCanceller_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuVoipEchoCanceller_Type.__name__=_B
_ZxAnEponOnuVoipEchoCanceller_Object=MibTableColumn
zxAnEponOnuVoipEchoCanceller=_ZxAnEponOnuVoipEchoCanceller_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,18,1,3),_ZxAnEponOnuVoipEchoCanceller_Type())
zxAnEponOnuVoipEchoCanceller.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoipEchoCanceller.setStatus(_A)
class _ZxAnEponOnuVoipDtmpTransferMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('voiceCoding',1),('nredRfc2833',2),('redRfc2833',3),('aal2OrIetf',4),('noForwarding',5)))
_ZxAnEponOnuVoipDtmpTransferMode_Type.__name__=_B
_ZxAnEponOnuVoipDtmpTransferMode_Object=MibTableColumn
zxAnEponOnuVoipDtmpTransferMode=_ZxAnEponOnuVoipDtmpTransferMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,18,1,4),_ZxAnEponOnuVoipDtmpTransferMode_Type())
zxAnEponOnuVoipDtmpTransferMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVoipDtmpTransferMode.setStatus(_A)
_ZxAnEponRmOnuVoipSrvPerfTable_Object=MibTable
zxAnEponRmOnuVoipSrvPerfTable=_ZxAnEponRmOnuVoipSrvPerfTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,19))
if mibBuilder.loadTexts:zxAnEponRmOnuVoipSrvPerfTable.setStatus(_A)
_ZxAnEponRmOnuVoipSrvPerfEntry_Object=MibTableRow
zxAnEponRmOnuVoipSrvPerfEntry=_ZxAnEponRmOnuVoipSrvPerfEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,19,1))
zxAnEponRmOnuVoipSrvPerfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponRmOnuVoipSrvPerfEntry.setStatus(_A)
_ZxAnEponRmOnuVoipRxSignalMsg_Type=Counter64
_ZxAnEponRmOnuVoipRxSignalMsg_Object=MibTableColumn
zxAnEponRmOnuVoipRxSignalMsg=_ZxAnEponRmOnuVoipRxSignalMsg_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,19,1,1),_ZxAnEponRmOnuVoipRxSignalMsg_Type())
zxAnEponRmOnuVoipRxSignalMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmOnuVoipRxSignalMsg.setStatus(_A)
_ZxAnEponRmOnuVoipTxSignalMsg_Type=Counter64
_ZxAnEponRmOnuVoipTxSignalMsg_Object=MibTableColumn
zxAnEponRmOnuVoipTxSignalMsg=_ZxAnEponRmOnuVoipTxSignalMsg_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,19,1,2),_ZxAnEponRmOnuVoipTxSignalMsg_Type())
zxAnEponRmOnuVoipTxSignalMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmOnuVoipTxSignalMsg.setStatus(_A)
_ZxAnEponRmOnuVoipLossSignalMsg_Type=Counter32
_ZxAnEponRmOnuVoipLossSignalMsg_Object=MibTableColumn
zxAnEponRmOnuVoipLossSignalMsg=_ZxAnEponRmOnuVoipLossSignalMsg_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,19,1,3),_ZxAnEponRmOnuVoipLossSignalMsg_Type())
zxAnEponRmOnuVoipLossSignalMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmOnuVoipLossSignalMsg.setStatus(_A)
_ZxAnEponRmOnuVoipReTxSignalMsg_Type=Counter32
_ZxAnEponRmOnuVoipReTxSignalMsg_Object=MibTableColumn
zxAnEponRmOnuVoipReTxSignalMsg=_ZxAnEponRmOnuVoipReTxSignalMsg_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,19,1,4),_ZxAnEponRmOnuVoipReTxSignalMsg_Type())
zxAnEponRmOnuVoipReTxSignalMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmOnuVoipReTxSignalMsg.setStatus(_A)
_ZxAnEponRmOnuVoipErrSignalMsg_Type=Counter32
_ZxAnEponRmOnuVoipErrSignalMsg_Object=MibTableColumn
zxAnEponRmOnuVoipErrSignalMsg=_ZxAnEponRmOnuVoipErrSignalMsg_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,19,1,5),_ZxAnEponRmOnuVoipErrSignalMsg_Type())
zxAnEponRmOnuVoipErrSignalMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmOnuVoipErrSignalMsg.setStatus(_A)
_ZxAnEponRmOnuVoipUnknowSignalMsg_Type=Counter32
_ZxAnEponRmOnuVoipUnknowSignalMsg_Object=MibTableColumn
zxAnEponRmOnuVoipUnknowSignalMsg=_ZxAnEponRmOnuVoipUnknowSignalMsg_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,36,19,1,6),_ZxAnEponRmOnuVoipUnknowSignalMsg_Type())
zxAnEponRmOnuVoipUnknowSignalMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmOnuVoipUnknowSignalMsg.setStatus(_A)
_ZxAnEponOnuCapabilityExtTable_Object=MibTable
zxAnEponOnuCapabilityExtTable=_ZxAnEponOnuCapabilityExtTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,37))
if mibBuilder.loadTexts:zxAnEponOnuCapabilityExtTable.setStatus(_A)
_ZxAnEponOnuCapabilityExtEntry_Object=MibTableRow
zxAnEponOnuCapabilityExtEntry=_ZxAnEponOnuCapabilityExtEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,37,1))
zxAnEponOnuCapabilityExtEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuCapabilityExtEntry.setStatus(_A)
class _ZxAnEponOnuType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('sfu',1),('hgu',2),('sbu',3),('ethMduCompactBox',4),('ethMduCards',5),('dslMduCardsCompactBox',6),('dslMduCardsRack',7),('bybridMduCards',8),('mtu',9)))
_ZxAnEponOnuType_Type.__name__=_B
_ZxAnEponOnuType_Object=MibTableColumn
zxAnEponOnuType=_ZxAnEponOnuType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,37,1,1),_ZxAnEponOnuType_Type())
zxAnEponOnuType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuType.setStatus(_A)
class _ZxAnEponOnuMultiLlid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_ZxAnEponOnuMultiLlid_Type.__name__=_B
_ZxAnEponOnuMultiLlid_Object=MibTableColumn
zxAnEponOnuMultiLlid=_ZxAnEponOnuMultiLlid_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,37,1,2),_ZxAnEponOnuMultiLlid_Type())
zxAnEponOnuMultiLlid.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuMultiLlid.setStatus(_A)
class _ZxAnEponOnuProtection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AL,1),('typeC',2),('typeD',3)))
_ZxAnEponOnuProtection_Type.__name__=_B
_ZxAnEponOnuProtection_Object=MibTableColumn
zxAnEponOnuProtection=_ZxAnEponOnuProtection_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,37,1,3),_ZxAnEponOnuProtection_Type())
zxAnEponOnuProtection.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuProtection.setStatus(_A)
_ZxAnEponOnuPonPorts_Type=Integer32
_ZxAnEponOnuPonPorts_Object=MibTableColumn
zxAnEponOnuPonPorts=_ZxAnEponOnuPonPorts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,37,1,4),_ZxAnEponOnuPonPorts_Type())
zxAnEponOnuPonPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuPonPorts.setStatus(_A)
_ZxAnEponOnuSlots_Type=Integer32
_ZxAnEponOnuSlots_Object=MibTableColumn
zxAnEponOnuSlots=_ZxAnEponOnuSlots_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,37,1,5),_ZxAnEponOnuSlots_Type())
zxAnEponOnuSlots.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuSlots.setStatus(_A)
class _ZxAnEponOnuBatteryBackupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noBatteryBackup',1),('batteryBackup',2)))
_ZxAnEponOnuBatteryBackupStatus_Type.__name__=_B
_ZxAnEponOnuBatteryBackupStatus_Object=MibTableColumn
zxAnEponOnuBatteryBackupStatus=_ZxAnEponOnuBatteryBackupStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,37,1,6),_ZxAnEponOnuBatteryBackupStatus_Type())
zxAnEponOnuBatteryBackupStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuBatteryBackupStatus.setStatus(_A)
class _ZxAnEponOnuIsSupportIpv6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_n,1),(_o,2)))
_ZxAnEponOnuIsSupportIpv6_Type.__name__=_B
_ZxAnEponOnuIsSupportIpv6_Object=MibTableColumn
zxAnEponOnuIsSupportIpv6=_ZxAnEponOnuIsSupportIpv6_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,37,1,7),_ZxAnEponOnuIsSupportIpv6_Type())
zxAnEponOnuIsSupportIpv6.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuIsSupportIpv6.setStatus(_A)
class _ZxAnEponOnuPwrSdSupportMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_o,1),('supportTx',2),('supportTrx',3)))
_ZxAnEponOnuPwrSdSupportMode_Type.__name__=_B
_ZxAnEponOnuPwrSdSupportMode_Object=MibTableColumn
zxAnEponOnuPwrSdSupportMode=_ZxAnEponOnuPwrSdSupportMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,37,1,8),_ZxAnEponOnuPwrSdSupportMode_Type())
zxAnEponOnuPwrSdSupportMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuPwrSdSupportMode.setStatus(_A)
class _ZxAnEponOnuSlaNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZxAnEponOnuSlaNumber_Type.__name__=_B
_ZxAnEponOnuSlaNumber_Object=MibTableColumn
zxAnEponOnuSlaNumber=_ZxAnEponOnuSlaNumber_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,37,1,9),_ZxAnEponOnuSlaNumber_Type())
zxAnEponOnuSlaNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuSlaNumber.setStatus(_A)
_ZxAnEponOnuInterfaceTable_Object=MibTable
zxAnEponOnuInterfaceTable=_ZxAnEponOnuInterfaceTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,38))
if mibBuilder.loadTexts:zxAnEponOnuInterfaceTable.setStatus(_A)
_ZxAnEponOnuInterfaceEntry_Object=MibTableRow
zxAnEponOnuInterfaceEntry=_ZxAnEponOnuInterfaceEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,38,1))
zxAnEponOnuInterfaceEntry.setIndexNames((0,_E,_F),(0,_E,_AM))
if mibBuilder.loadTexts:zxAnEponOnuInterfaceEntry.setStatus(_A)
class _ZxAnEponOnuInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('ge',1),('fe',2),('voip',3),('tdm',4),('adsl2Plus',5),('vdsl2',6),('wlan',7),('usb',8),('catvRf',9)))
_ZxAnEponOnuInterfaceType_Type.__name__=_B
_ZxAnEponOnuInterfaceType_Object=MibTableColumn
zxAnEponOnuInterfaceType=_ZxAnEponOnuInterfaceType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,38,1,1),_ZxAnEponOnuInterfaceType_Type())
zxAnEponOnuInterfaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuInterfaceType.setStatus(_A)
_ZxAnEponOnuInterfaceNum_Type=Integer32
_ZxAnEponOnuInterfaceNum_Object=MibTableColumn
zxAnEponOnuInterfaceNum=_ZxAnEponOnuInterfaceNum_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,38,1,2),_ZxAnEponOnuInterfaceNum_Type())
zxAnEponOnuInterfaceNum.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuInterfaceNum.setStatus(_A)
_ZxAnEponMduCardTable_Object=MibTable
zxAnEponMduCardTable=_ZxAnEponMduCardTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,39))
if mibBuilder.loadTexts:zxAnEponMduCardTable.setStatus(_A)
_ZxAnEponMduCardEntry_Object=MibTableRow
zxAnEponMduCardEntry=_ZxAnEponMduCardEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,39,1))
zxAnEponMduCardEntry.setIndexNames((0,_E,_F),(0,_E,_M))
if mibBuilder.loadTexts:zxAnEponMduCardEntry.setStatus(_A)
class _ZxAnEponMduCardOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('inService',1),(_AK,2),('hwOnline',3),('hwOffline',4),('configuring',5),('configFailed',6),('typeMismatch',7),('deactived',8),('faulty',9),('invalid',10)))
_ZxAnEponMduCardOperStatus_Type.__name__=_B
_ZxAnEponMduCardOperStatus_Object=MibTableColumn
zxAnEponMduCardOperStatus=_ZxAnEponMduCardOperStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,39,1,1),_ZxAnEponMduCardOperStatus_Type())
zxAnEponMduCardOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponMduCardOperStatus.setStatus(_A)
class _ZxAnEponMduCardAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_l,1),('switch',2),('stopService',3),(_X,4),(_U,5)))
_ZxAnEponMduCardAdminStatus_Type.__name__=_B
_ZxAnEponMduCardAdminStatus_Object=MibTableColumn
zxAnEponMduCardAdminStatus=_ZxAnEponMduCardAdminStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,39,1,2),_ZxAnEponMduCardAdminStatus_Type())
zxAnEponMduCardAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponMduCardAdminStatus.setStatus(_A)
_ZxAnEponMduSnmpParamMgmt_ObjectIdentity=ObjectIdentity
zxAnEponMduSnmpParamMgmt=_ZxAnEponMduSnmpParamMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,1,40))
_ZxAnEponMduSnmpParamTable_Object=MibTable
zxAnEponMduSnmpParamTable=_ZxAnEponMduSnmpParamTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,40,1))
if mibBuilder.loadTexts:zxAnEponMduSnmpParamTable.setStatus(_A)
_ZxAnEponMduSnmpParamEntry_Object=MibTableRow
zxAnEponMduSnmpParamEntry=_ZxAnEponMduSnmpParamEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,40,1,1))
zxAnEponMduSnmpParamEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponMduSnmpParamEntry.setStatus(_A)
class _ZxEponMduSnmpVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('snmpV1',1),('snmpV2c',2),('snmpV3',3)))
_ZxEponMduSnmpVersion_Type.__name__=_B
_ZxEponMduSnmpVersion_Object=MibTableColumn
zxEponMduSnmpVersion=_ZxEponMduSnmpVersion_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,40,1,1,1),_ZxEponMduSnmpVersion_Type())
zxEponMduSnmpVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponMduSnmpVersion.setStatus(_A)
class _ZxEponMduSnmpServicePort_Type(Integer32):defaultValue=161;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZxEponMduSnmpServicePort_Type.__name__=_B
_ZxEponMduSnmpServicePort_Object=MibTableColumn
zxEponMduSnmpServicePort=_ZxEponMduSnmpServicePort_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,40,1,1,2),_ZxEponMduSnmpServicePort_Type())
zxEponMduSnmpServicePort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponMduSnmpServicePort.setStatus(_A)
class _ZxEponMduSnmpTrapPort_Type(Integer32):defaultValue=162;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZxEponMduSnmpTrapPort_Type.__name__=_B
_ZxEponMduSnmpTrapPort_Object=MibTableColumn
zxEponMduSnmpTrapPort=_ZxEponMduSnmpTrapPort_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,40,1,1,3),_ZxEponMduSnmpTrapPort_Type())
zxEponMduSnmpTrapPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponMduSnmpTrapPort.setStatus(_A)
class _ZxEponMduSnmpReadCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxEponMduSnmpReadCommunity_Type.__name__=_L
_ZxEponMduSnmpReadCommunity_Object=MibTableColumn
zxEponMduSnmpReadCommunity=_ZxEponMduSnmpReadCommunity_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,40,1,1,4),_ZxEponMduSnmpReadCommunity_Type())
zxEponMduSnmpReadCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponMduSnmpReadCommunity.setStatus(_A)
class _ZxEponMduSnmpWriteCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxEponMduSnmpWriteCommunity_Type.__name__=_L
_ZxEponMduSnmpWriteCommunity_Object=MibTableColumn
zxEponMduSnmpWriteCommunity=_ZxEponMduSnmpWriteCommunity_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,40,1,1,5),_ZxEponMduSnmpWriteCommunity_Type())
zxEponMduSnmpWriteCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponMduSnmpWriteCommunity.setStatus(_A)
_ZxEponMduSnmpTrapHostTable_Object=MibTable
zxEponMduSnmpTrapHostTable=_ZxEponMduSnmpTrapHostTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,40,2))
if mibBuilder.loadTexts:zxEponMduSnmpTrapHostTable.setStatus(_A)
_ZxEponMduSnmpTrapHostEntry_Object=MibTableRow
zxEponMduSnmpTrapHostEntry=_ZxEponMduSnmpTrapHostEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,40,2,1))
zxEponMduSnmpTrapHostEntry.setIndexNames((0,_E,_F),(0,_E,_AN))
if mibBuilder.loadTexts:zxEponMduSnmpTrapHostEntry.setStatus(_A)
class _ZxEponMduSnmpTrapHostIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZxEponMduSnmpTrapHostIndex_Type.__name__=_B
_ZxEponMduSnmpTrapHostIndex_Object=MibTableColumn
zxEponMduSnmpTrapHostIndex=_ZxEponMduSnmpTrapHostIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,40,2,1,1),_ZxEponMduSnmpTrapHostIndex_Type())
zxEponMduSnmpTrapHostIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:zxEponMduSnmpTrapHostIndex.setStatus(_A)
_ZxEponMduSnmpTrapHostIpAddr_Type=IpAddress
_ZxEponMduSnmpTrapHostIpAddr_Object=MibTableColumn
zxEponMduSnmpTrapHostIpAddr=_ZxEponMduSnmpTrapHostIpAddr_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,40,2,1,2),_ZxEponMduSnmpTrapHostIpAddr_Type())
zxEponMduSnmpTrapHostIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponMduSnmpTrapHostIpAddr.setStatus(_A)
class _ZxEponMduSnmpTrapHostSnmpVer_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('snmpV1',1),('snmpV2c',2),('snmpV3',3)))
_ZxEponMduSnmpTrapHostSnmpVer_Type.__name__=_B
_ZxEponMduSnmpTrapHostSnmpVer_Object=MibTableColumn
zxEponMduSnmpTrapHostSnmpVer=_ZxEponMduSnmpTrapHostSnmpVer_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,40,2,1,3),_ZxEponMduSnmpTrapHostSnmpVer_Type())
zxEponMduSnmpTrapHostSnmpVer.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponMduSnmpTrapHostSnmpVer.setStatus(_A)
class _ZxEponMduSnmpTrapHostCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxEponMduSnmpTrapHostCommunity_Type.__name__=_L
_ZxEponMduSnmpTrapHostCommunity_Object=MibTableColumn
zxEponMduSnmpTrapHostCommunity=_ZxEponMduSnmpTrapHostCommunity_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,40,2,1,4),_ZxEponMduSnmpTrapHostCommunity_Type())
zxEponMduSnmpTrapHostCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponMduSnmpTrapHostCommunity.setStatus(_A)
class _ZxEponMduSnmpTrapHostMinEventLevel_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('critical',0),('major',1),('minor',2),('warning',3),('indeterminate',4),('cleared',5),('notification',6)))
_ZxEponMduSnmpTrapHostMinEventLevel_Type.__name__=_B
_ZxEponMduSnmpTrapHostMinEventLevel_Object=MibTableColumn
zxEponMduSnmpTrapHostMinEventLevel=_ZxEponMduSnmpTrapHostMinEventLevel_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,40,2,1,5),_ZxEponMduSnmpTrapHostMinEventLevel_Type())
zxEponMduSnmpTrapHostMinEventLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponMduSnmpTrapHostMinEventLevel.setStatus(_A)
class _ZxEponMduSnmpTrapHostEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxEponMduSnmpTrapHostEnable_Type.__name__=_B
_ZxEponMduSnmpTrapHostEnable_Object=MibTableColumn
zxEponMduSnmpTrapHostEnable=_ZxEponMduSnmpTrapHostEnable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,40,2,1,6),_ZxEponMduSnmpTrapHostEnable_Type())
zxEponMduSnmpTrapHostEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponMduSnmpTrapHostEnable.setStatus(_A)
_ZxEponMduSnmpTrapHostRowStatus_Type=RowStatus
_ZxEponMduSnmpTrapHostRowStatus_Object=MibTableColumn
zxEponMduSnmpTrapHostRowStatus=_ZxEponMduSnmpTrapHostRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,40,2,1,7),_ZxEponMduSnmpTrapHostRowStatus_Type())
zxEponMduSnmpTrapHostRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponMduSnmpTrapHostRowStatus.setStatus(_A)
_ZxAnEponOnuMVlanSwitchTable_Object=MibTable
zxAnEponOnuMVlanSwitchTable=_ZxAnEponOnuMVlanSwitchTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,41))
if mibBuilder.loadTexts:zxAnEponOnuMVlanSwitchTable.setStatus(_A)
_ZxAnEponOnuMVlanSwitchEntry_Object=MibTableRow
zxAnEponOnuMVlanSwitchEntry=_ZxAnEponOnuMVlanSwitchEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,41,1))
zxAnEponOnuMVlanSwitchEntry.setIndexNames((0,_E,_F),(0,_E,_H),(0,_E,_AO),(0,_E,_AP))
if mibBuilder.loadTexts:zxAnEponOnuMVlanSwitchEntry.setStatus(_A)
class _ZxAnEponOnuMVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnEponOnuMVlan_Type.__name__=_B
_ZxAnEponOnuMVlan_Object=MibTableColumn
zxAnEponOnuMVlan=_ZxAnEponOnuMVlan_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,41,1,1),_ZxAnEponOnuMVlan_Type())
zxAnEponOnuMVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuMVlan.setStatus(_A)
class _ZxAnEponOnuIptvUserVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnEponOnuIptvUserVlan_Type.__name__=_B
_ZxAnEponOnuIptvUserVlan_Object=MibTableColumn
zxAnEponOnuIptvUserVlan=_ZxAnEponOnuIptvUserVlan_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,41,1,2),_ZxAnEponOnuIptvUserVlan_Type())
zxAnEponOnuIptvUserVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuIptvUserVlan.setStatus(_A)
_ZxAnEponOnuMVlanSwitchRowStatus_Type=RowStatus
_ZxAnEponOnuMVlanSwitchRowStatus_Object=MibTableColumn
zxAnEponOnuMVlanSwitchRowStatus=_ZxAnEponOnuMVlanSwitchRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,41,1,10),_ZxAnEponOnuMVlanSwitchRowStatus_Type())
zxAnEponOnuMVlanSwitchRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuMVlanSwitchRowStatus.setStatus(_A)
_ZxAnEponOnuPortTable_Object=MibTable
zxAnEponOnuPortTable=_ZxAnEponOnuPortTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,42))
if mibBuilder.loadTexts:zxAnEponOnuPortTable.setStatus(_A)
_ZxAnEponOnuPortEntry_Object=MibTableRow
zxAnEponOnuPortEntry=_ZxAnEponOnuPortEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,42,1))
zxAnEponOnuPortEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuPortEntry.setStatus(_A)
class _ZxAnEponOnuPortLoopbackDetectStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZxAnEponOnuPortLoopbackDetectStatus_Type.__name__=_B
_ZxAnEponOnuPortLoopbackDetectStatus_Object=MibTableColumn
zxAnEponOnuPortLoopbackDetectStatus=_ZxAnEponOnuPortLoopbackDetectStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,42,1,1),_ZxAnEponOnuPortLoopbackDetectStatus_Type())
zxAnEponOnuPortLoopbackDetectStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPortLoopbackDetectStatus.setStatus(_A)
class _ZxAnEponOnuPortLoopbackAutoSdEn_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_ZxAnEponOnuPortLoopbackAutoSdEn_Type.__name__=_B
_ZxAnEponOnuPortLoopbackAutoSdEn_Object=MibTableColumn
zxAnEponOnuPortLoopbackAutoSdEn=_ZxAnEponOnuPortLoopbackAutoSdEn_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,42,1,2),_ZxAnEponOnuPortLoopbackAutoSdEn_Type())
zxAnEponOnuPortLoopbackAutoSdEn.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPortLoopbackAutoSdEn.setStatus(_A)
_ZxAnEponOnuLlidQueueTable_Object=MibTable
zxAnEponOnuLlidQueueTable=_ZxAnEponOnuLlidQueueTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,43))
if mibBuilder.loadTexts:zxAnEponOnuLlidQueueTable.setStatus(_A)
_ZxAnEponOnuLlidQueueEntry_Object=MibTableRow
zxAnEponOnuLlidQueueEntry=_ZxAnEponOnuLlidQueueEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,43,1))
zxAnEponOnuLlidQueueEntry.setIndexNames((0,_E,_F),(0,_E,_AQ))
if mibBuilder.loadTexts:zxAnEponOnuLlidQueueEntry.setStatus(_A)
_ZxAnEponOnuLlid_Type=Integer32
_ZxAnEponOnuLlid_Object=MibTableColumn
zxAnEponOnuLlid=_ZxAnEponOnuLlid_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,43,1,1),_ZxAnEponOnuLlid_Type())
zxAnEponOnuLlid.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuLlid.setStatus(_A)
class _ZxAnEponOnuLlidQueue1WrrWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnEponOnuLlidQueue1WrrWeight_Type.__name__=_B
_ZxAnEponOnuLlidQueue1WrrWeight_Object=MibTableColumn
zxAnEponOnuLlidQueue1WrrWeight=_ZxAnEponOnuLlidQueue1WrrWeight_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,43,1,2),_ZxAnEponOnuLlidQueue1WrrWeight_Type())
zxAnEponOnuLlidQueue1WrrWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuLlidQueue1WrrWeight.setStatus(_A)
class _ZxAnEponOnuLlidQueue2WrrWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnEponOnuLlidQueue2WrrWeight_Type.__name__=_B
_ZxAnEponOnuLlidQueue2WrrWeight_Object=MibTableColumn
zxAnEponOnuLlidQueue2WrrWeight=_ZxAnEponOnuLlidQueue2WrrWeight_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,43,1,3),_ZxAnEponOnuLlidQueue2WrrWeight_Type())
zxAnEponOnuLlidQueue2WrrWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuLlidQueue2WrrWeight.setStatus(_A)
class _ZxAnEponOnuLlidQueue3WrrWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnEponOnuLlidQueue3WrrWeight_Type.__name__=_B
_ZxAnEponOnuLlidQueue3WrrWeight_Object=MibTableColumn
zxAnEponOnuLlidQueue3WrrWeight=_ZxAnEponOnuLlidQueue3WrrWeight_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,43,1,4),_ZxAnEponOnuLlidQueue3WrrWeight_Type())
zxAnEponOnuLlidQueue3WrrWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuLlidQueue3WrrWeight.setStatus(_A)
class _ZxAnEponOnuLlidQueue4WrrWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnEponOnuLlidQueue4WrrWeight_Type.__name__=_B
_ZxAnEponOnuLlidQueue4WrrWeight_Object=MibTableColumn
zxAnEponOnuLlidQueue4WrrWeight=_ZxAnEponOnuLlidQueue4WrrWeight_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,43,1,5),_ZxAnEponOnuLlidQueue4WrrWeight_Type())
zxAnEponOnuLlidQueue4WrrWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuLlidQueue4WrrWeight.setStatus(_A)
class _ZxAnEponOnuLlidQueue5WrrWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnEponOnuLlidQueue5WrrWeight_Type.__name__=_B
_ZxAnEponOnuLlidQueue5WrrWeight_Object=MibTableColumn
zxAnEponOnuLlidQueue5WrrWeight=_ZxAnEponOnuLlidQueue5WrrWeight_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,43,1,6),_ZxAnEponOnuLlidQueue5WrrWeight_Type())
zxAnEponOnuLlidQueue5WrrWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuLlidQueue5WrrWeight.setStatus(_A)
class _ZxAnEponOnuLlidQueue6WrrWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnEponOnuLlidQueue6WrrWeight_Type.__name__=_B
_ZxAnEponOnuLlidQueue6WrrWeight_Object=MibTableColumn
zxAnEponOnuLlidQueue6WrrWeight=_ZxAnEponOnuLlidQueue6WrrWeight_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,43,1,7),_ZxAnEponOnuLlidQueue6WrrWeight_Type())
zxAnEponOnuLlidQueue6WrrWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuLlidQueue6WrrWeight.setStatus(_A)
class _ZxAnEponOnuLlidQueue7WrrWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnEponOnuLlidQueue7WrrWeight_Type.__name__=_B
_ZxAnEponOnuLlidQueue7WrrWeight_Object=MibTableColumn
zxAnEponOnuLlidQueue7WrrWeight=_ZxAnEponOnuLlidQueue7WrrWeight_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,43,1,8),_ZxAnEponOnuLlidQueue7WrrWeight_Type())
zxAnEponOnuLlidQueue7WrrWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuLlidQueue7WrrWeight.setStatus(_A)
class _ZxAnEponOnuLlidQueue8WrrWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnEponOnuLlidQueue8WrrWeight_Type.__name__=_B
_ZxAnEponOnuLlidQueue8WrrWeight_Object=MibTableColumn
zxAnEponOnuLlidQueue8WrrWeight=_ZxAnEponOnuLlidQueue8WrrWeight_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,43,1,9),_ZxAnEponOnuLlidQueue8WrrWeight_Type())
zxAnEponOnuLlidQueue8WrrWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuLlidQueue8WrrWeight.setStatus(_A)
_ZxAnEponOnuPonIfTable_Object=MibTable
zxAnEponOnuPonIfTable=_ZxAnEponOnuPonIfTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,44))
if mibBuilder.loadTexts:zxAnEponOnuPonIfTable.setStatus(_A)
_ZxAnEponOnuPonIfEntry_Object=MibTableRow
zxAnEponOnuPonIfEntry=_ZxAnEponOnuPonIfEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,44,1))
zxAnEponOnuPonIfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuPonIfEntry.setStatus(_A)
class _ZxAnEponOnuActivePonIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_ZxAnEponOnuActivePonIf_Type.__name__=_B
_ZxAnEponOnuActivePonIf_Object=MibTableColumn
zxAnEponOnuActivePonIf=_ZxAnEponOnuActivePonIf_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,44,1,1),_ZxAnEponOnuActivePonIf_Type())
zxAnEponOnuActivePonIf.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuActivePonIf.setStatus(_A)
_ZxAnEponOnuSlaMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuSlaMgmt=_ZxAnEponOnuSlaMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,1,45))
_ZxAnEponOnuSlaProfileIdxNext_Type=Integer32
_ZxAnEponOnuSlaProfileIdxNext_Object=MibScalar
zxAnEponOnuSlaProfileIdxNext=_ZxAnEponOnuSlaProfileIdxNext_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,1),_ZxAnEponOnuSlaProfileIdxNext_Type())
zxAnEponOnuSlaProfileIdxNext.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuSlaProfileIdxNext.setStatus(_A)
_ZxAnEponOnuSlaProfileTable_Object=MibTable
zxAnEponOnuSlaProfileTable=_ZxAnEponOnuSlaProfileTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,2))
if mibBuilder.loadTexts:zxAnEponOnuSlaProfileTable.setStatus(_A)
_ZxAnEponOnuSlaProfileEntry_Object=MibTableRow
zxAnEponOnuSlaProfileEntry=_ZxAnEponOnuSlaProfileEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,2,1))
zxAnEponOnuSlaProfileEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:zxAnEponOnuSlaProfileEntry.setStatus(_A)
_ZxAnEponOnuSlaProfileIndex_Type=Integer32
_ZxAnEponOnuSlaProfileIndex_Object=MibTableColumn
zxAnEponOnuSlaProfileIndex=_ZxAnEponOnuSlaProfileIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,2,1,1),_ZxAnEponOnuSlaProfileIndex_Type())
zxAnEponOnuSlaProfileIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuSlaProfileIndex.setStatus(_A)
class _ZxAnEponOnuSlaProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnEponOnuSlaProfileName_Type.__name__=_L
_ZxAnEponOnuSlaProfileName_Object=MibTableColumn
zxAnEponOnuSlaProfileName=_ZxAnEponOnuSlaProfileName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,2,1,2),_ZxAnEponOnuSlaProfileName_Type())
zxAnEponOnuSlaProfileName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuSlaProfileName.setStatus(_A)
class _ZxAnEponOnuServiceDbaEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZxAnEponOnuServiceDbaEnable_Type.__name__=_B
_ZxAnEponOnuServiceDbaEnable_Object=MibTableColumn
zxAnEponOnuServiceDbaEnable=_ZxAnEponOnuServiceDbaEnable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,2,1,3),_ZxAnEponOnuServiceDbaEnable_Type())
zxAnEponOnuServiceDbaEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuServiceDbaEnable.setStatus(_A)
class _ZxAnEponOnuBestEffortSchedulingScheme_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sp',1),('wrr',2),('spWrr',3)))
_ZxAnEponOnuBestEffortSchedulingScheme_Type.__name__=_B
_ZxAnEponOnuBestEffortSchedulingScheme_Object=MibTableColumn
zxAnEponOnuBestEffortSchedulingScheme=_ZxAnEponOnuBestEffortSchedulingScheme_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,2,1,4),_ZxAnEponOnuBestEffortSchedulingScheme_Type())
zxAnEponOnuBestEffortSchedulingScheme.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuBestEffortSchedulingScheme.setStatus(_A)
class _ZxAnEponOnuHighPriorityBoundary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnEponOnuHighPriorityBoundary_Type.__name__=_B
_ZxAnEponOnuHighPriorityBoundary_Object=MibTableColumn
zxAnEponOnuHighPriorityBoundary=_ZxAnEponOnuHighPriorityBoundary_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,2,1,5),_ZxAnEponOnuHighPriorityBoundary_Type())
zxAnEponOnuHighPriorityBoundary.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuHighPriorityBoundary.setStatus(_A)
_ZxAnEponOnuServiceDbaCycleLength_Type=Integer32
_ZxAnEponOnuServiceDbaCycleLength_Object=MibTableColumn
zxAnEponOnuServiceDbaCycleLength=_ZxAnEponOnuServiceDbaCycleLength_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,2,1,6),_ZxAnEponOnuServiceDbaCycleLength_Type())
zxAnEponOnuServiceDbaCycleLength.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuServiceDbaCycleLength.setStatus(_A)
_ZxAnEponOnuSlaServiceIdxNext_Type=Integer32
_ZxAnEponOnuSlaServiceIdxNext_Object=MibTableColumn
zxAnEponOnuSlaServiceIdxNext=_ZxAnEponOnuSlaServiceIdxNext_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,2,1,29),_ZxAnEponOnuSlaServiceIdxNext_Type())
zxAnEponOnuSlaServiceIdxNext.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuSlaServiceIdxNext.setStatus(_A)
_ZxAnEponOnuSlaProfileRowStatus_Type=RowStatus
_ZxAnEponOnuSlaProfileRowStatus_Object=MibTableColumn
zxAnEponOnuSlaProfileRowStatus=_ZxAnEponOnuSlaProfileRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,2,1,30),_ZxAnEponOnuSlaProfileRowStatus_Type())
zxAnEponOnuSlaProfileRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuSlaProfileRowStatus.setStatus(_A)
_ZxAnEponOnuServiceQueueTable_Object=MibTable
zxAnEponOnuServiceQueueTable=_ZxAnEponOnuServiceQueueTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,3))
if mibBuilder.loadTexts:zxAnEponOnuServiceQueueTable.setStatus(_A)
_ZxAnEponOnuServiceQueueEntry_Object=MibTableRow
zxAnEponOnuServiceQueueEntry=_ZxAnEponOnuServiceQueueEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,3,1))
zxAnEponOnuServiceQueueEntry.setIndexNames((0,_E,_p),(0,_E,_AR))
if mibBuilder.loadTexts:zxAnEponOnuServiceQueueEntry.setStatus(_A)
class _ZxAnEponOnuSlaServiceIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZxAnEponOnuSlaServiceIdx_Type.__name__=_B
_ZxAnEponOnuSlaServiceIdx_Object=MibTableColumn
zxAnEponOnuSlaServiceIdx=_ZxAnEponOnuSlaServiceIdx_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,3,1,1),_ZxAnEponOnuSlaServiceIdx_Type())
zxAnEponOnuSlaServiceIdx.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuSlaServiceIdx.setStatus(_A)
_ZxAnEponOnuServiceName_Type=DisplayString
_ZxAnEponOnuServiceName_Object=MibTableColumn
zxAnEponOnuServiceName=_ZxAnEponOnuServiceName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,3,1,2),_ZxAnEponOnuServiceName_Type())
zxAnEponOnuServiceName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuServiceName.setStatus(_A)
_ZxAnEponOnuQueueId_Type=Integer32
_ZxAnEponOnuQueueId_Object=MibTableColumn
zxAnEponOnuQueueId=_ZxAnEponOnuQueueId_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,3,1,3),_ZxAnEponOnuQueueId_Type())
zxAnEponOnuQueueId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuQueueId.setStatus(_A)
_ZxAnEponOnuServiceFixedPktSize_Type=Integer32
_ZxAnEponOnuServiceFixedPktSize_Object=MibTableColumn
zxAnEponOnuServiceFixedPktSize=_ZxAnEponOnuServiceFixedPktSize_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,3,1,4),_ZxAnEponOnuServiceFixedPktSize_Type())
zxAnEponOnuServiceFixedPktSize.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuServiceFixedPktSize.setStatus(_A)
_ZxAnEponOnuServiceFixedBandwidth_Type=Integer32
_ZxAnEponOnuServiceFixedBandwidth_Object=MibTableColumn
zxAnEponOnuServiceFixedBandwidth=_ZxAnEponOnuServiceFixedBandwidth_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,3,1,5),_ZxAnEponOnuServiceFixedBandwidth_Type())
zxAnEponOnuServiceFixedBandwidth.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuServiceFixedBandwidth.setStatus(_A)
_ZxAnEponOnuServiceAssuredBandwidth_Type=Integer32
_ZxAnEponOnuServiceAssuredBandwidth_Object=MibTableColumn
zxAnEponOnuServiceAssuredBandwidth=_ZxAnEponOnuServiceAssuredBandwidth_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,3,1,6),_ZxAnEponOnuServiceAssuredBandwidth_Type())
zxAnEponOnuServiceAssuredBandwidth.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuServiceAssuredBandwidth.setStatus(_A)
_ZxAnEponOnuServiceBestEffortBandwidth_Type=Integer32
_ZxAnEponOnuServiceBestEffortBandwidth_Object=MibTableColumn
zxAnEponOnuServiceBestEffortBandwidth=_ZxAnEponOnuServiceBestEffortBandwidth_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,3,1,7),_ZxAnEponOnuServiceBestEffortBandwidth_Type())
zxAnEponOnuServiceBestEffortBandwidth.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuServiceBestEffortBandwidth.setStatus(_A)
class _ZxAnEponOnuServiceWrrWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnEponOnuServiceWrrWeight_Type.__name__=_B
_ZxAnEponOnuServiceWrrWeight_Object=MibTableColumn
zxAnEponOnuServiceWrrWeight=_ZxAnEponOnuServiceWrrWeight_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,3,1,8),_ZxAnEponOnuServiceWrrWeight_Type())
zxAnEponOnuServiceWrrWeight.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuServiceWrrWeight.setStatus(_A)
_ZxAnEponOnuServiceRowStatus_Type=RowStatus
_ZxAnEponOnuServiceRowStatus_Object=MibTableColumn
zxAnEponOnuServiceRowStatus=_ZxAnEponOnuServiceRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,3,1,30),_ZxAnEponOnuServiceRowStatus_Type())
zxAnEponOnuServiceRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponOnuServiceRowStatus.setStatus(_A)
_ZxAnEponOnuSlaProfileApplyTable_Object=MibTable
zxAnEponOnuSlaProfileApplyTable=_ZxAnEponOnuSlaProfileApplyTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,4))
if mibBuilder.loadTexts:zxAnEponOnuSlaProfileApplyTable.setStatus(_A)
_ZxAnEponOnuSlaProfileApplyEntry_Object=MibTableRow
zxAnEponOnuSlaProfileApplyEntry=_ZxAnEponOnuSlaProfileApplyEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,4,1))
zxAnEponOnuSlaProfileApplyEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuSlaProfileApplyEntry.setStatus(_A)
_ZxAnEponOnuCurrSlaProfileIdx_Type=Integer32
_ZxAnEponOnuCurrSlaProfileIdx_Object=MibTableColumn
zxAnEponOnuCurrSlaProfileIdx=_ZxAnEponOnuCurrSlaProfileIdx_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,45,4,1,1),_ZxAnEponOnuCurrSlaProfileIdx_Type())
zxAnEponOnuCurrSlaProfileIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuCurrSlaProfileIdx.setStatus(_A)
_ZxAnEponOnuHoldoverTable_Object=MibTable
zxAnEponOnuHoldoverTable=_ZxAnEponOnuHoldoverTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,46))
if mibBuilder.loadTexts:zxAnEponOnuHoldoverTable.setStatus(_A)
_ZxAnEponOnuHoldoverEntry_Object=MibTableRow
zxAnEponOnuHoldoverEntry=_ZxAnEponOnuHoldoverEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,46,1))
zxAnEponOnuHoldoverEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuHoldoverEntry.setStatus(_A)
class _ZxAnEponOnuHoldoverState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZxAnEponOnuHoldoverState_Type.__name__=_B
_ZxAnEponOnuHoldoverState_Object=MibTableColumn
zxAnEponOnuHoldoverState=_ZxAnEponOnuHoldoverState_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,46,1,1),_ZxAnEponOnuHoldoverState_Type())
zxAnEponOnuHoldoverState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuHoldoverState.setStatus(_A)
class _ZxAnEponOnuHoldoverTime_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,1000))
_ZxAnEponOnuHoldoverTime_Type.__name__=_B
_ZxAnEponOnuHoldoverTime_Object=MibTableColumn
zxAnEponOnuHoldoverTime=_ZxAnEponOnuHoldoverTime_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,46,1,2),_ZxAnEponOnuHoldoverTime_Type())
zxAnEponOnuHoldoverTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuHoldoverTime.setStatus(_A)
_ZxAnEponOnuAlarmMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuAlarmMgmt=_ZxAnEponOnuAlarmMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,1,48))
_ZxAnEponOnuLvlAlarmCtrlTable_Object=MibTable
zxAnEponOnuLvlAlarmCtrlTable=_ZxAnEponOnuLvlAlarmCtrlTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,48,1))
if mibBuilder.loadTexts:zxAnEponOnuLvlAlarmCtrlTable.setStatus(_A)
_ZxAnEponOnuLvlAlarmCtrlEntry_Object=MibTableRow
zxAnEponOnuLvlAlarmCtrlEntry=_ZxAnEponOnuLvlAlarmCtrlEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,48,1,1))
zxAnEponOnuLvlAlarmCtrlEntry.setIndexNames((0,_E,_F),(0,_E,_AS))
if mibBuilder.loadTexts:zxAnEponOnuLvlAlarmCtrlEntry.setStatus(_A)
_ZxAnEponOnuLvlAlarmCode_Type=Integer32
_ZxAnEponOnuLvlAlarmCode_Object=MibTableColumn
zxAnEponOnuLvlAlarmCode=_ZxAnEponOnuLvlAlarmCode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,48,1,1,1),_ZxAnEponOnuLvlAlarmCode_Type())
zxAnEponOnuLvlAlarmCode.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuLvlAlarmCode.setStatus(_A)
class _ZxAnEponOnuLvlAlarmEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZxAnEponOnuLvlAlarmEnable_Type.__name__=_B
_ZxAnEponOnuLvlAlarmEnable_Object=MibTableColumn
zxAnEponOnuLvlAlarmEnable=_ZxAnEponOnuLvlAlarmEnable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,48,1,1,2),_ZxAnEponOnuLvlAlarmEnable_Type())
zxAnEponOnuLvlAlarmEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuLvlAlarmEnable.setStatus(_A)
_ZxAnEponOnuLvlAlarmThreshold_Type=Integer32
_ZxAnEponOnuLvlAlarmThreshold_Object=MibTableColumn
zxAnEponOnuLvlAlarmThreshold=_ZxAnEponOnuLvlAlarmThreshold_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,48,1,1,3),_ZxAnEponOnuLvlAlarmThreshold_Type())
zxAnEponOnuLvlAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuLvlAlarmThreshold.setStatus(_A)
_ZxAnEponOnuLvlAlarmRestoreThreshold_Type=Integer32
_ZxAnEponOnuLvlAlarmRestoreThreshold_Object=MibTableColumn
zxAnEponOnuLvlAlarmRestoreThreshold=_ZxAnEponOnuLvlAlarmRestoreThreshold_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,48,1,1,4),_ZxAnEponOnuLvlAlarmRestoreThreshold_Type())
zxAnEponOnuLvlAlarmRestoreThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuLvlAlarmRestoreThreshold.setStatus(_A)
_ZxAnEponOnuPonAlarmCtrlTable_Object=MibTable
zxAnEponOnuPonAlarmCtrlTable=_ZxAnEponOnuPonAlarmCtrlTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,48,2))
if mibBuilder.loadTexts:zxAnEponOnuPonAlarmCtrlTable.setStatus(_A)
_ZxAnEponOnuPonAlarmCtrlEntry_Object=MibTableRow
zxAnEponOnuPonAlarmCtrlEntry=_ZxAnEponOnuPonAlarmCtrlEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,48,2,1))
zxAnEponOnuPonAlarmCtrlEntry.setIndexNames((0,_E,_F),(0,_E,_H),(0,_E,_AT))
if mibBuilder.loadTexts:zxAnEponOnuPonAlarmCtrlEntry.setStatus(_A)
_ZxAnEponOnuPonAlarmCode_Type=Integer32
_ZxAnEponOnuPonAlarmCode_Object=MibTableColumn
zxAnEponOnuPonAlarmCode=_ZxAnEponOnuPonAlarmCode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,48,2,1,1),_ZxAnEponOnuPonAlarmCode_Type())
zxAnEponOnuPonAlarmCode.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuPonAlarmCode.setStatus(_A)
class _ZxAnEponOnuPonAlarmEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZxAnEponOnuPonAlarmEnable_Type.__name__=_B
_ZxAnEponOnuPonAlarmEnable_Object=MibTableColumn
zxAnEponOnuPonAlarmEnable=_ZxAnEponOnuPonAlarmEnable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,48,2,1,2),_ZxAnEponOnuPonAlarmEnable_Type())
zxAnEponOnuPonAlarmEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPonAlarmEnable.setStatus(_A)
_ZxAnEponOnuPonAlarmThreshold_Type=Integer32
_ZxAnEponOnuPonAlarmThreshold_Object=MibTableColumn
zxAnEponOnuPonAlarmThreshold=_ZxAnEponOnuPonAlarmThreshold_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,48,2,1,3),_ZxAnEponOnuPonAlarmThreshold_Type())
zxAnEponOnuPonAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPonAlarmThreshold.setStatus(_A)
_ZxAnEponOnuPonAlarmRestoreThreshold_Type=Integer32
_ZxAnEponOnuPonAlarmRestoreThreshold_Object=MibTableColumn
zxAnEponOnuPonAlarmRestoreThreshold=_ZxAnEponOnuPonAlarmRestoreThreshold_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,48,2,1,4),_ZxAnEponOnuPonAlarmRestoreThreshold_Type())
zxAnEponOnuPonAlarmRestoreThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPonAlarmRestoreThreshold.setStatus(_A)
_ZxAnEponOnuUniAlarmCtrlTable_Object=MibTable
zxAnEponOnuUniAlarmCtrlTable=_ZxAnEponOnuUniAlarmCtrlTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,48,3))
if mibBuilder.loadTexts:zxAnEponOnuUniAlarmCtrlTable.setStatus(_A)
_ZxAnEponOnuUniAlarmCtrlEntry_Object=MibTableRow
zxAnEponOnuUniAlarmCtrlEntry=_ZxAnEponOnuUniAlarmCtrlEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,48,3,1))
zxAnEponOnuUniAlarmCtrlEntry.setIndexNames((0,_E,_F),(0,_E,_H),(0,_E,_AU))
if mibBuilder.loadTexts:zxAnEponOnuUniAlarmCtrlEntry.setStatus(_A)
_ZxAnEponOnuUniAlarmCode_Type=Integer32
_ZxAnEponOnuUniAlarmCode_Object=MibTableColumn
zxAnEponOnuUniAlarmCode=_ZxAnEponOnuUniAlarmCode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,48,3,1,1),_ZxAnEponOnuUniAlarmCode_Type())
zxAnEponOnuUniAlarmCode.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuUniAlarmCode.setStatus(_A)
class _ZxAnEponOnuUniAlarmEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZxAnEponOnuUniAlarmEnable_Type.__name__=_B
_ZxAnEponOnuUniAlarmEnable_Object=MibTableColumn
zxAnEponOnuUniAlarmEnable=_ZxAnEponOnuUniAlarmEnable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,48,3,1,2),_ZxAnEponOnuUniAlarmEnable_Type())
zxAnEponOnuUniAlarmEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuUniAlarmEnable.setStatus(_A)
class _ZxAnEponOnuUniAlarmThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ZxAnEponOnuUniAlarmThreshold_Type.__name__=_T
_ZxAnEponOnuUniAlarmThreshold_Object=MibTableColumn
zxAnEponOnuUniAlarmThreshold=_ZxAnEponOnuUniAlarmThreshold_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,48,3,1,3),_ZxAnEponOnuUniAlarmThreshold_Type())
zxAnEponOnuUniAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuUniAlarmThreshold.setStatus(_A)
class _ZxAnEponOnuUniAlarmRestoreThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ZxAnEponOnuUniAlarmRestoreThresh_Type.__name__=_T
_ZxAnEponOnuUniAlarmRestoreThresh_Object=MibTableColumn
zxAnEponOnuUniAlarmRestoreThresh=_ZxAnEponOnuUniAlarmRestoreThresh_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,48,3,1,4),_ZxAnEponOnuUniAlarmRestoreThresh_Type())
zxAnEponOnuUniAlarmRestoreThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuUniAlarmRestoreThresh.setStatus(_A)
_ZxAnEponOnuVersionMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuVersionMgmt=_ZxAnEponOnuVersionMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,1,49))
_ZxAnEponOnuVersionTable_Object=MibTable
zxAnEponOnuVersionTable=_ZxAnEponOnuVersionTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,1))
if mibBuilder.loadTexts:zxAnEponOnuVersionTable.setStatus(_A)
_ZxAnEponOnuVersionEntry_Object=MibTableRow
zxAnEponOnuVersionEntry=_ZxAnEponOnuVersionEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,1,1))
zxAnEponOnuVersionEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:zxAnEponOnuVersionEntry.setStatus(_A)
_ZxAnEponOnuVersionId_Type=Integer32
_ZxAnEponOnuVersionId_Object=MibTableColumn
zxAnEponOnuVersionId=_ZxAnEponOnuVersionId_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,1,1,1),_ZxAnEponOnuVersionId_Type())
zxAnEponOnuVersionId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVersionId.setStatus(_A)
_ZxAnEponOnuVersionFileName_Type=DisplayString
_ZxAnEponOnuVersionFileName_Object=MibTableColumn
zxAnEponOnuVersionFileName=_ZxAnEponOnuVersionFileName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,1,1,2),_ZxAnEponOnuVersionFileName_Type())
zxAnEponOnuVersionFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVersionFileName.setStatus(_A)
_ZxAnEponOnuVersionType_Type=DisplayString
_ZxAnEponOnuVersionType_Object=MibTableColumn
zxAnEponOnuVersionType=_ZxAnEponOnuVersionType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,1,1,3),_ZxAnEponOnuVersionType_Type())
zxAnEponOnuVersionType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVersionType.setStatus(_A)
_ZxAnEponOnuVersionTag_Type=DisplayString
_ZxAnEponOnuVersionTag_Object=MibTableColumn
zxAnEponOnuVersionTag=_ZxAnEponOnuVersionTag_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,1,1,4),_ZxAnEponOnuVersionTag_Type())
zxAnEponOnuVersionTag.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVersionTag.setStatus(_A)
_ZxAnEponOnuVersionBuildTime_Type=DisplayString
_ZxAnEponOnuVersionBuildTime_Object=MibTableColumn
zxAnEponOnuVersionBuildTime=_ZxAnEponOnuVersionBuildTime_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,1,1,5),_ZxAnEponOnuVersionBuildTime_Type())
zxAnEponOnuVersionBuildTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVersionBuildTime.setStatus(_A)
_ZxAnEponOnuVersionUpdateTable_Object=MibTable
zxAnEponOnuVersionUpdateTable=_ZxAnEponOnuVersionUpdateTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,2))
if mibBuilder.loadTexts:zxAnEponOnuVersionUpdateTable.setStatus(_A)
_ZxAnEponOnuVersionUpdateEntry_Object=MibTableRow
zxAnEponOnuVersionUpdateEntry=_ZxAnEponOnuVersionUpdateEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,2,1))
zxAnEponOnuVersionUpdateEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:zxAnEponOnuVersionUpdateEntry.setStatus(_A)
_ZxAnEponOnuVersionUpdateOnuType_Type=DisplayString
_ZxAnEponOnuVersionUpdateOnuType_Object=MibTableColumn
zxAnEponOnuVersionUpdateOnuType=_ZxAnEponOnuVersionUpdateOnuType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,2,1,1),_ZxAnEponOnuVersionUpdateOnuType_Type())
zxAnEponOnuVersionUpdateOnuType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVersionUpdateOnuType.setStatus(_A)
class _ZxAnEponOnuVersionUpdateLocType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('slot',1),('olt',2),('onuList',3)))
_ZxAnEponOnuVersionUpdateLocType_Type.__name__=_B
_ZxAnEponOnuVersionUpdateLocType_Object=MibTableColumn
zxAnEponOnuVersionUpdateLocType=_ZxAnEponOnuVersionUpdateLocType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,2,1,2),_ZxAnEponOnuVersionUpdateLocType_Type())
zxAnEponOnuVersionUpdateLocType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVersionUpdateLocType.setStatus(_A)
_ZxAnEponOnuVersionUpdateSlotId_Type=Integer32
_ZxAnEponOnuVersionUpdateSlotId_Object=MibTableColumn
zxAnEponOnuVersionUpdateSlotId=_ZxAnEponOnuVersionUpdateSlotId_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,2,1,3),_ZxAnEponOnuVersionUpdateSlotId_Type())
zxAnEponOnuVersionUpdateSlotId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVersionUpdateSlotId.setStatus(_A)
_ZxAnEponOnuVersionUpdateOltId_Type=Integer32
_ZxAnEponOnuVersionUpdateOltId_Object=MibTableColumn
zxAnEponOnuVersionUpdateOltId=_ZxAnEponOnuVersionUpdateOltId_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,2,1,4),_ZxAnEponOnuVersionUpdateOltId_Type())
zxAnEponOnuVersionUpdateOltId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVersionUpdateOltId.setStatus(_A)
_ZxAnEponOnuVersionUpdateOnuList_Type=DisplayString
_ZxAnEponOnuVersionUpdateOnuList_Object=MibTableColumn
zxAnEponOnuVersionUpdateOnuList=_ZxAnEponOnuVersionUpdateOnuList_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,2,1,5),_ZxAnEponOnuVersionUpdateOnuList_Type())
zxAnEponOnuVersionUpdateOnuList.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVersionUpdateOnuList.setStatus(_A)
class _ZxAnEponOnuVersionUpdateAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,99)));namedValues=NamedValues(*(('download',1),('downloadAndActivate',2),('downloadAndCommit',3),('activate',4),('commit',5),('abort',99)))
_ZxAnEponOnuVersionUpdateAction_Type.__name__=_B
_ZxAnEponOnuVersionUpdateAction_Object=MibTableColumn
zxAnEponOnuVersionUpdateAction=_ZxAnEponOnuVersionUpdateAction_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,2,1,6),_ZxAnEponOnuVersionUpdateAction_Type())
zxAnEponOnuVersionUpdateAction.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVersionUpdateAction.setStatus(_A)
_ZxAnEponOnuVersionUpdateStatusTable_Object=MibTable
zxAnEponOnuVersionUpdateStatusTable=_ZxAnEponOnuVersionUpdateStatusTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,3))
if mibBuilder.loadTexts:zxAnEponOnuVersionUpdateStatusTable.setStatus(_A)
_ZxAnEponOnuVersionUpdateStatusEntry_Object=MibTableRow
zxAnEponOnuVersionUpdateStatusEntry=_ZxAnEponOnuVersionUpdateStatusEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,3,1))
zxAnEponOnuVersionUpdateStatusEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuVersionUpdateStatusEntry.setStatus(_A)
class _ZxAnEponOnuVersionUpdateState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notStart',1),('updateFailed',2),(_AV,3),('waitEndResponse',4),('finished',5)))
_ZxAnEponOnuVersionUpdateState_Type.__name__=_B
_ZxAnEponOnuVersionUpdateState_Object=MibTableColumn
zxAnEponOnuVersionUpdateState=_ZxAnEponOnuVersionUpdateState_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,3,1,1),_ZxAnEponOnuVersionUpdateState_Type())
zxAnEponOnuVersionUpdateState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVersionUpdateState.setStatus(_A)
class _ZxAnEponOnuVersionUpdateAbortReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_Y,1),('downloadError',2),('downloadTimeout',3),('onuReturnError',4),('endDownloadCheckError',5),('userAbort',6),(_r,7)))
_ZxAnEponOnuVersionUpdateAbortReason_Type.__name__=_B
_ZxAnEponOnuVersionUpdateAbortReason_Object=MibTableColumn
zxAnEponOnuVersionUpdateAbortReason=_ZxAnEponOnuVersionUpdateAbortReason_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,3,1,2),_ZxAnEponOnuVersionUpdateAbortReason_Type())
zxAnEponOnuVersionUpdateAbortReason.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVersionUpdateAbortReason.setStatus(_A)
_ZxAnEponOnuVersionUpdateErrCode_Type=Integer32
_ZxAnEponOnuVersionUpdateErrCode_Object=MibTableColumn
zxAnEponOnuVersionUpdateErrCode=_ZxAnEponOnuVersionUpdateErrCode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,3,1,3),_ZxAnEponOnuVersionUpdateErrCode_Type())
zxAnEponOnuVersionUpdateErrCode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVersionUpdateErrCode.setStatus(_A)
class _ZxAnEponOnuVersionUpdateErrMsg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_ZxAnEponOnuVersionUpdateErrMsg_Type.__name__=_L
_ZxAnEponOnuVersionUpdateErrMsg_Object=MibTableColumn
zxAnEponOnuVersionUpdateErrMsg=_ZxAnEponOnuVersionUpdateErrMsg_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,3,1,4),_ZxAnEponOnuVersionUpdateErrMsg_Type())
zxAnEponOnuVersionUpdateErrMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVersionUpdateErrMsg.setStatus(_A)
class _ZxAnEponOnuVersionUpdateProgress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ZxAnEponOnuVersionUpdateProgress_Type.__name__=_B
_ZxAnEponOnuVersionUpdateProgress_Object=MibTableColumn
zxAnEponOnuVersionUpdateProgress=_ZxAnEponOnuVersionUpdateProgress_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,3,1,5),_ZxAnEponOnuVersionUpdateProgress_Type())
zxAnEponOnuVersionUpdateProgress.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVersionUpdateProgress.setStatus(_A)
_ZxAnEponOnuCurrentUsedVersionName_Type=DisplayString
_ZxAnEponOnuCurrentUsedVersionName_Object=MibTableColumn
zxAnEponOnuCurrentUsedVersionName=_ZxAnEponOnuCurrentUsedVersionName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,3,1,6),_ZxAnEponOnuCurrentUsedVersionName_Type())
zxAnEponOnuCurrentUsedVersionName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuCurrentUsedVersionName.setStatus(_A)
_ZxAnEponOnuCurrentUsedVersionTime_Type=DisplayString
_ZxAnEponOnuCurrentUsedVersionTime_Object=MibTableColumn
zxAnEponOnuCurrentUsedVersionTime=_ZxAnEponOnuCurrentUsedVersionTime_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,3,1,7),_ZxAnEponOnuCurrentUsedVersionTime_Type())
zxAnEponOnuCurrentUsedVersionTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuCurrentUsedVersionTime.setStatus(_A)
_ZxAnEponOnuUpdatingVersionName_Type=DisplayString
_ZxAnEponOnuUpdatingVersionName_Object=MibTableColumn
zxAnEponOnuUpdatingVersionName=_ZxAnEponOnuUpdatingVersionName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,3,1,8),_ZxAnEponOnuUpdatingVersionName_Type())
zxAnEponOnuUpdatingVersionName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuUpdatingVersionName.setStatus(_A)
_ZxAnEponOnuUpdatingVersionTime_Type=DisplayString
_ZxAnEponOnuUpdatingVersionTime_Object=MibTableColumn
zxAnEponOnuUpdatingVersionTime=_ZxAnEponOnuUpdatingVersionTime_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,3,1,9),_ZxAnEponOnuUpdatingVersionTime_Type())
zxAnEponOnuUpdatingVersionTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuUpdatingVersionTime.setStatus(_A)
_ZxAnEponOnuVersionActionTable_Object=MibTable
zxAnEponOnuVersionActionTable=_ZxAnEponOnuVersionActionTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,4))
if mibBuilder.loadTexts:zxAnEponOnuVersionActionTable.setStatus(_A)
_ZxAnEponOnuVersionActionEntry_Object=MibTableRow
zxAnEponOnuVersionActionEntry=_ZxAnEponOnuVersionActionEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,4,1))
zxAnEponOnuVersionActionEntry.setIndexNames((0,_E,_F),(0,_E,_AW))
if mibBuilder.loadTexts:zxAnEponOnuVersionActionEntry.setStatus(_A)
_ZxAnEponOnuVersionImageIndex_Type=Integer32
_ZxAnEponOnuVersionImageIndex_Object=MibTableColumn
zxAnEponOnuVersionImageIndex=_ZxAnEponOnuVersionImageIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,4,1,1),_ZxAnEponOnuVersionImageIndex_Type())
zxAnEponOnuVersionImageIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuVersionImageIndex.setStatus(_A)
class _ZxAnEponOnuVersionImageAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('activate',1),('commit',2)))
_ZxAnEponOnuVersionImageAction_Type.__name__=_B
_ZxAnEponOnuVersionImageAction_Object=MibTableColumn
zxAnEponOnuVersionImageAction=_ZxAnEponOnuVersionImageAction_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,4,1,2),_ZxAnEponOnuVersionImageAction_Type())
zxAnEponOnuVersionImageAction.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuVersionImageAction.setStatus(_A)
class _ZxAnEponOnuVersionImageCommitState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('committed',1),('notCommitted',2)))
_ZxAnEponOnuVersionImageCommitState_Type.__name__=_B
_ZxAnEponOnuVersionImageCommitState_Object=MibTableColumn
zxAnEponOnuVersionImageCommitState=_ZxAnEponOnuVersionImageCommitState_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,4,1,3),_ZxAnEponOnuVersionImageCommitState_Type())
zxAnEponOnuVersionImageCommitState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVersionImageCommitState.setStatus(_A)
class _ZxAnEponOnuVersionImageActiveState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('actived',1),('notActived',2)))
_ZxAnEponOnuVersionImageActiveState_Type.__name__=_B
_ZxAnEponOnuVersionImageActiveState_Object=MibTableColumn
zxAnEponOnuVersionImageActiveState=_ZxAnEponOnuVersionImageActiveState_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,4,1,4),_ZxAnEponOnuVersionImageActiveState_Type())
zxAnEponOnuVersionImageActiveState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVersionImageActiveState.setStatus(_A)
class _ZxAnEponOnuVersionImageValidState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('notValid',2)))
_ZxAnEponOnuVersionImageValidState_Type.__name__=_B
_ZxAnEponOnuVersionImageValidState_Object=MibTableColumn
zxAnEponOnuVersionImageValidState=_ZxAnEponOnuVersionImageValidState_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,49,4,1,5),_ZxAnEponOnuVersionImageValidState_Type())
zxAnEponOnuVersionImageValidState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVersionImageValidState.setStatus(_A)
_ZxAnEponOnuPonMacShapingMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuPonMacShapingMgmt=_ZxAnEponOnuPonMacShapingMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,1,50))
_ZxAnEponOnuPonMacShapingTable_Object=MibTable
zxAnEponOnuPonMacShapingTable=_ZxAnEponOnuPonMacShapingTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,1))
if mibBuilder.loadTexts:zxAnEponOnuPonMacShapingTable.setStatus(_A)
_ZxAnEponOnuPonMacShapingEntry_Object=MibTableRow
zxAnEponOnuPonMacShapingEntry=_ZxAnEponOnuPonMacShapingEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,1,1))
zxAnEponOnuPonMacShapingEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuPonMacShapingEntry.setStatus(_A)
class _ZxAnEponOnuShappingAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuShappingAdminStatus_Type.__name__=_B
_ZxAnEponOnuShappingAdminStatus_Object=MibTableColumn
zxAnEponOnuShappingAdminStatus=_ZxAnEponOnuShappingAdminStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,1,1,1),_ZxAnEponOnuShappingAdminStatus_Type())
zxAnEponOnuShappingAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuShappingAdminStatus.setStatus(_A)
class _ZxAnEponOnuShappingCir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_ZxAnEponOnuShappingCir_Type.__name__=_B
_ZxAnEponOnuShappingCir_Object=MibTableColumn
zxAnEponOnuShappingCir=_ZxAnEponOnuShappingCir_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,1,1,2),_ZxAnEponOnuShappingCir_Type())
zxAnEponOnuShappingCir.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuShappingCir.setStatus(_A)
class _ZxAnEponOnuShappingCbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1522,16777215))
_ZxAnEponOnuShappingCbs_Type.__name__=_B
_ZxAnEponOnuShappingCbs_Object=MibTableColumn
zxAnEponOnuShappingCbs=_ZxAnEponOnuShappingCbs_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,1,1,3),_ZxAnEponOnuShappingCbs_Type())
zxAnEponOnuShappingCbs.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuShappingCbs.setStatus(_A)
_ZxAnEponOnuPonMacBufferTable_Object=MibTable
zxAnEponOnuPonMacBufferTable=_ZxAnEponOnuPonMacBufferTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,2))
if mibBuilder.loadTexts:zxAnEponOnuPonMacBufferTable.setStatus(_A)
_ZxAnEponOnuPonMacBufferEntry_Object=MibTableRow
zxAnEponOnuPonMacBufferEntry=_ZxAnEponOnuPonMacBufferEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,2,1))
zxAnEponOnuPonMacBufferEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuPonMacBufferEntry.setStatus(_A)
class _ZxAnEponOnuPonMacDsBufferAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuPonMacDsBufferAdminStatus_Type.__name__=_B
_ZxAnEponOnuPonMacDsBufferAdminStatus_Object=MibTableColumn
zxAnEponOnuPonMacDsBufferAdminStatus=_ZxAnEponOnuPonMacDsBufferAdminStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,2,1,1),_ZxAnEponOnuPonMacDsBufferAdminStatus_Type())
zxAnEponOnuPonMacDsBufferAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPonMacDsBufferAdminStatus.setStatus(_A)
class _ZxAnEponOnuPonMacDsBufferOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuPonMacDsBufferOperStatus_Type.__name__=_B
_ZxAnEponOnuPonMacDsBufferOperStatus_Object=MibTableColumn
zxAnEponOnuPonMacDsBufferOperStatus=_ZxAnEponOnuPonMacDsBufferOperStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,2,1,2),_ZxAnEponOnuPonMacDsBufferOperStatus_Type())
zxAnEponOnuPonMacDsBufferOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuPonMacDsBufferOperStatus.setStatus(_A)
_ZxAnEponOnuPonMacDsConfBufferSize_Type=Integer32
_ZxAnEponOnuPonMacDsConfBufferSize_Object=MibTableColumn
zxAnEponOnuPonMacDsConfBufferSize=_ZxAnEponOnuPonMacDsConfBufferSize_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,2,1,3),_ZxAnEponOnuPonMacDsConfBufferSize_Type())
zxAnEponOnuPonMacDsConfBufferSize.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPonMacDsConfBufferSize.setStatus(_A)
_ZxAnEponOnuPonMacDsActBufferSize_Type=Integer32
_ZxAnEponOnuPonMacDsActBufferSize_Object=MibTableColumn
zxAnEponOnuPonMacDsActBufferSize=_ZxAnEponOnuPonMacDsActBufferSize_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,2,1,4),_ZxAnEponOnuPonMacDsActBufferSize_Type())
zxAnEponOnuPonMacDsActBufferSize.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuPonMacDsActBufferSize.setStatus(_A)
class _ZxAnEponOnuPonMacUsBufferAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuPonMacUsBufferAdminStatus_Type.__name__=_B
_ZxAnEponOnuPonMacUsBufferAdminStatus_Object=MibTableColumn
zxAnEponOnuPonMacUsBufferAdminStatus=_ZxAnEponOnuPonMacUsBufferAdminStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,2,1,5),_ZxAnEponOnuPonMacUsBufferAdminStatus_Type())
zxAnEponOnuPonMacUsBufferAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPonMacUsBufferAdminStatus.setStatus(_A)
class _ZxAnEponOnuPonMacUsBufferOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuPonMacUsBufferOperStatus_Type.__name__=_B
_ZxAnEponOnuPonMacUsBufferOperStatus_Object=MibTableColumn
zxAnEponOnuPonMacUsBufferOperStatus=_ZxAnEponOnuPonMacUsBufferOperStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,2,1,6),_ZxAnEponOnuPonMacUsBufferOperStatus_Type())
zxAnEponOnuPonMacUsBufferOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuPonMacUsBufferOperStatus.setStatus(_A)
_ZxAnEponOnuPonMacUsConfBufferSize_Type=Integer32
_ZxAnEponOnuPonMacUsConfBufferSize_Object=MibTableColumn
zxAnEponOnuPonMacUsConfBufferSize=_ZxAnEponOnuPonMacUsConfBufferSize_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,2,1,7),_ZxAnEponOnuPonMacUsConfBufferSize_Type())
zxAnEponOnuPonMacUsConfBufferSize.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPonMacUsConfBufferSize.setStatus(_A)
_ZxAnEponOnuPonMacUsActBufferSize_Type=Integer32
_ZxAnEponOnuPonMacUsActBufferSize_Object=MibTableColumn
zxAnEponOnuPonMacUsActBufferSize=_ZxAnEponOnuPonMacUsActBufferSize_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,2,1,8),_ZxAnEponOnuPonMacUsActBufferSize_Type())
zxAnEponOnuPonMacUsActBufferSize.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuPonMacUsActBufferSize.setStatus(_A)
_ZxAnEponOnuPonMacBufferCapabilityTable_Object=MibTable
zxAnEponOnuPonMacBufferCapabilityTable=_ZxAnEponOnuPonMacBufferCapabilityTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,3))
if mibBuilder.loadTexts:zxAnEponOnuPonMacBufferCapabilityTable.setStatus(_A)
_ZxAnEponOnuPonMacBufferCapabilityEntry_Object=MibTableRow
zxAnEponOnuPonMacBufferCapabilityEntry=_ZxAnEponOnuPonMacBufferCapabilityEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,3,1))
zxAnEponOnuPonMacBufferCapabilityEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuPonMacBufferCapabilityEntry.setStatus(_A)
class _ZxAnEponOnuPonMacBufferCapability_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuPonMacBufferCapability_Type.__name__=_B
_ZxAnEponOnuPonMacBufferCapability_Object=MibTableColumn
zxAnEponOnuPonMacBufferCapability=_ZxAnEponOnuPonMacBufferCapability_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,3,1,1),_ZxAnEponOnuPonMacBufferCapability_Type())
zxAnEponOnuPonMacBufferCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuPonMacBufferCapability.setStatus(_A)
_ZxAnEponOnuPonMacMinDsBufferSize_Type=Integer32
_ZxAnEponOnuPonMacMinDsBufferSize_Object=MibTableColumn
zxAnEponOnuPonMacMinDsBufferSize=_ZxAnEponOnuPonMacMinDsBufferSize_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,3,1,2),_ZxAnEponOnuPonMacMinDsBufferSize_Type())
zxAnEponOnuPonMacMinDsBufferSize.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuPonMacMinDsBufferSize.setStatus(_A)
_ZxAnEponOnuPonMacMaxDsBufferSize_Type=Integer32
_ZxAnEponOnuPonMacMaxDsBufferSize_Object=MibTableColumn
zxAnEponOnuPonMacMaxDsBufferSize=_ZxAnEponOnuPonMacMaxDsBufferSize_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,3,1,3),_ZxAnEponOnuPonMacMaxDsBufferSize_Type())
zxAnEponOnuPonMacMaxDsBufferSize.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuPonMacMaxDsBufferSize.setStatus(_A)
_ZxAnEponOnuPonMacMinUsBufferSize_Type=Integer32
_ZxAnEponOnuPonMacMinUsBufferSize_Object=MibTableColumn
zxAnEponOnuPonMacMinUsBufferSize=_ZxAnEponOnuPonMacMinUsBufferSize_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,3,1,4),_ZxAnEponOnuPonMacMinUsBufferSize_Type())
zxAnEponOnuPonMacMinUsBufferSize.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuPonMacMinUsBufferSize.setStatus(_A)
_ZxAnEponOnuPonMacMaxUsBufferSize_Type=Integer32
_ZxAnEponOnuPonMacMaxUsBufferSize_Object=MibTableColumn
zxAnEponOnuPonMacMaxUsBufferSize=_ZxAnEponOnuPonMacMaxUsBufferSize_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,50,3,1,5),_ZxAnEponOnuPonMacMaxUsBufferSize_Type())
zxAnEponOnuPonMacMaxUsBufferSize.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuPonMacMaxUsBufferSize.setStatus(_A)
_ZxAnEponOnuUniMacTable_Object=MibTable
zxAnEponOnuUniMacTable=_ZxAnEponOnuUniMacTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,51))
if mibBuilder.loadTexts:zxAnEponOnuUniMacTable.setStatus(_A)
_ZxAnEponOnuUniMacEntry_Object=MibTableRow
zxAnEponOnuUniMacEntry=_ZxAnEponOnuUniMacEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,51,1))
zxAnEponOnuUniMacEntry.setIndexNames((0,_E,_F),(0,_E,_H),(0,_E,_AX),(0,_E,_AY))
if mibBuilder.loadTexts:zxAnEponOnuUniMacEntry.setStatus(_A)
class _ZxAnEponOnuUniVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnEponOnuUniVlanId_Type.__name__=_B
_ZxAnEponOnuUniVlanId_Object=MibTableColumn
zxAnEponOnuUniVlanId=_ZxAnEponOnuUniVlanId_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,51,1,1),_ZxAnEponOnuUniVlanId_Type())
zxAnEponOnuUniVlanId.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuUniVlanId.setStatus(_A)
_ZxAnEponOnuUniMacSequenceNo_Type=Integer32
_ZxAnEponOnuUniMacSequenceNo_Object=MibTableColumn
zxAnEponOnuUniMacSequenceNo=_ZxAnEponOnuUniMacSequenceNo_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,51,1,2),_ZxAnEponOnuUniMacSequenceNo_Type())
zxAnEponOnuUniMacSequenceNo.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuUniMacSequenceNo.setStatus(_A)
class _ZxAnEponOnuUniMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),(_V,2)))
_ZxAnEponOnuUniMacType_Type.__name__=_B
_ZxAnEponOnuUniMacType_Object=MibTableColumn
zxAnEponOnuUniMacType=_ZxAnEponOnuUniMacType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,51,1,3),_ZxAnEponOnuUniMacType_Type())
zxAnEponOnuUniMacType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuUniMacType.setStatus(_A)
_ZxAnEponOnuUniMacAddress_Type=MacAddress
_ZxAnEponOnuUniMacAddress_Object=MibTableColumn
zxAnEponOnuUniMacAddress=_ZxAnEponOnuUniMacAddress_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,51,1,4),_ZxAnEponOnuUniMacAddress_Type())
zxAnEponOnuUniMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuUniMacAddress.setStatus(_A)
_ZxAnEponOnuMgmtIpDHCPCfgTable_Object=MibTable
zxAnEponOnuMgmtIpDHCPCfgTable=_ZxAnEponOnuMgmtIpDHCPCfgTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,52))
if mibBuilder.loadTexts:zxAnEponOnuMgmtIpDHCPCfgTable.setStatus(_A)
_ZxAnEponOnuMgmtIpDHCPCfgEntry_Object=MibTableRow
zxAnEponOnuMgmtIpDHCPCfgEntry=_ZxAnEponOnuMgmtIpDHCPCfgEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,52,1))
zxAnEponOnuMgmtIpDHCPCfgEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuMgmtIpDHCPCfgEntry.setStatus(_A)
class _ZxAnEponOnuMgmtIpDHCPCfgVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnEponOnuMgmtIpDHCPCfgVlan_Type.__name__=_B
_ZxAnEponOnuMgmtIpDHCPCfgVlan_Object=MibTableColumn
zxAnEponOnuMgmtIpDHCPCfgVlan=_ZxAnEponOnuMgmtIpDHCPCfgVlan_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,52,1,1),_ZxAnEponOnuMgmtIpDHCPCfgVlan_Type())
zxAnEponOnuMgmtIpDHCPCfgVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuMgmtIpDHCPCfgVlan.setStatus(_A)
class _ZxAnEponOnuMgmtIpDHCPCfgPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnEponOnuMgmtIpDHCPCfgPriority_Type.__name__=_B
_ZxAnEponOnuMgmtIpDHCPCfgPriority_Object=MibTableColumn
zxAnEponOnuMgmtIpDHCPCfgPriority=_ZxAnEponOnuMgmtIpDHCPCfgPriority_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,52,1,2),_ZxAnEponOnuMgmtIpDHCPCfgPriority_Type())
zxAnEponOnuMgmtIpDHCPCfgPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuMgmtIpDHCPCfgPriority.setStatus(_A)
class _ZxAnEponOnuMgmtIpDHCPCfgEnableState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuMgmtIpDHCPCfgEnableState_Type.__name__=_B
_ZxAnEponOnuMgmtIpDHCPCfgEnableState_Object=MibTableColumn
zxAnEponOnuMgmtIpDHCPCfgEnableState=_ZxAnEponOnuMgmtIpDHCPCfgEnableState_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,52,1,3),_ZxAnEponOnuMgmtIpDHCPCfgEnableState_Type())
zxAnEponOnuMgmtIpDHCPCfgEnableState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuMgmtIpDHCPCfgEnableState.setStatus(_A)
class _ZxAnEponOnuMgmtIpDHCPCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('init',0),('selecting',1),('requesting',2),('init-reboot',3),(_AJ,4),('bound',5),('renewing',6),('rebinding',7)))
_ZxAnEponOnuMgmtIpDHCPCfgState_Type.__name__=_B
_ZxAnEponOnuMgmtIpDHCPCfgState_Object=MibTableColumn
zxAnEponOnuMgmtIpDHCPCfgState=_ZxAnEponOnuMgmtIpDHCPCfgState_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,52,1,4),_ZxAnEponOnuMgmtIpDHCPCfgState_Type())
zxAnEponOnuMgmtIpDHCPCfgState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuMgmtIpDHCPCfgState.setStatus(_A)
_ZxAnEponRmOnuWanMgmt_ObjectIdentity=ObjectIdentity
zxAnEponRmOnuWanMgmt=_ZxAnEponRmOnuWanMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,1,53))
_ZxAnEponRmWanPrfTable_Object=MibTable
zxAnEponRmWanPrfTable=_ZxAnEponRmWanPrfTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,2))
if mibBuilder.loadTexts:zxAnEponRmWanPrfTable.setStatus(_A)
_ZxAnEponRmWanPrfEntry_Object=MibTableRow
zxAnEponRmWanPrfEntry=_ZxAnEponRmWanPrfEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,2,1))
zxAnEponRmWanPrfEntry.setIndexNames((0,_E,_AZ))
if mibBuilder.loadTexts:zxAnEponRmWanPrfEntry.setStatus(_A)
class _ZxAnEponRmWanPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnEponRmWanPrfName_Type.__name__=_L
_ZxAnEponRmWanPrfName_Object=MibTableColumn
zxAnEponRmWanPrfName=_ZxAnEponRmWanPrfName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,2,1,1),_ZxAnEponRmWanPrfName_Type())
zxAnEponRmWanPrfName.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponRmWanPrfName.setStatus(_A)
class _ZxAnEponRmWanPrfWorkMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bridge',1),('route',2)))
_ZxAnEponRmWanPrfWorkMode_Type.__name__=_B
_ZxAnEponRmWanPrfWorkMode_Object=MibTableColumn
zxAnEponRmWanPrfWorkMode=_ZxAnEponRmWanPrfWorkMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,2,1,2),_ZxAnEponRmWanPrfWorkMode_Type())
zxAnEponRmWanPrfWorkMode.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmWanPrfWorkMode.setStatus(_A)
class _ZxAnEponRmWanPrfSrvType_Type(Bits):namedValues=NamedValues(*(('internet',0),('tr069',1),('voip',2),(_k,3)))
_ZxAnEponRmWanPrfSrvType_Type.__name__=_O
_ZxAnEponRmWanPrfSrvType_Object=MibTableColumn
zxAnEponRmWanPrfSrvType=_ZxAnEponRmWanPrfSrvType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,2,1,3),_ZxAnEponRmWanPrfSrvType_Type())
zxAnEponRmWanPrfSrvType.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmWanPrfSrvType.setStatus(_A)
class _ZxAnEponRmWanPrfIpStackMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2),('ipv4AndIpv6',3)))
_ZxAnEponRmWanPrfIpStackMode_Type.__name__=_B
_ZxAnEponRmWanPrfIpStackMode_Object=MibTableColumn
zxAnEponRmWanPrfIpStackMode=_ZxAnEponRmWanPrfIpStackMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,2,1,4),_ZxAnEponRmWanPrfIpStackMode_Type())
zxAnEponRmWanPrfIpStackMode.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmWanPrfIpStackMode.setStatus(_A)
class _ZxAnEponRmWanPrfNatNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnEponRmWanPrfNatNum_Type.__name__=_B
_ZxAnEponRmWanPrfNatNum_Object=MibTableColumn
zxAnEponRmWanPrfNatNum=_ZxAnEponRmWanPrfNatNum_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,2,1,5),_ZxAnEponRmWanPrfNatNum_Type())
zxAnEponRmWanPrfNatNum.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmWanPrfNatNum.setStatus(_A)
class _ZxAnEponRmWanPrfTransTagMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_b,1),('tagged',2),('untagged',3)))
_ZxAnEponRmWanPrfTransTagMode_Type.__name__=_B
_ZxAnEponRmWanPrfTransTagMode_Object=MibTableColumn
zxAnEponRmWanPrfTransTagMode=_ZxAnEponRmWanPrfTransTagMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,2,1,6),_ZxAnEponRmWanPrfTransTagMode_Type())
zxAnEponRmWanPrfTransTagMode.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmWanPrfTransTagMode.setStatus(_A)
class _ZxAnEponRmWanPrfTagTpid_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZxAnEponRmWanPrfTagTpid_Type.__name__=_B
_ZxAnEponRmWanPrfTagTpid_Object=MibTableColumn
zxAnEponRmWanPrfTagTpid=_ZxAnEponRmWanPrfTagTpid_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,2,1,7),_ZxAnEponRmWanPrfTagTpid_Type())
zxAnEponRmWanPrfTagTpid.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmWanPrfTagTpid.setStatus(_A)
class _ZxAnEponRmWanPrfTagVid_Type(Integer32):defaultValue=4092;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnEponRmWanPrfTagVid_Type.__name__=_B
_ZxAnEponRmWanPrfTagVid_Object=MibTableColumn
zxAnEponRmWanPrfTagVid=_ZxAnEponRmWanPrfTagVid_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,2,1,8),_ZxAnEponRmWanPrfTagVid_Type())
zxAnEponRmWanPrfTagVid.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmWanPrfTagVid.setStatus(_A)
class _ZxAnEponRmWanPrfTagPrior_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnEponRmWanPrfTagPrior_Type.__name__=_B
_ZxAnEponRmWanPrfTagPrior_Object=MibTableColumn
zxAnEponRmWanPrfTagPrior=_ZxAnEponRmWanPrfTagPrior_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,2,1,9),_ZxAnEponRmWanPrfTagPrior_Type())
zxAnEponRmWanPrfTagPrior.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmWanPrfTagPrior.setStatus(_A)
class _ZxAnEponRmWanPrfMaxTransUnit_Type(Integer32):defaultValue=1522;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_ZxAnEponRmWanPrfMaxTransUnit_Type.__name__=_B
_ZxAnEponRmWanPrfMaxTransUnit_Object=MibTableColumn
zxAnEponRmWanPrfMaxTransUnit=_ZxAnEponRmWanPrfMaxTransUnit_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,2,1,10),_ZxAnEponRmWanPrfMaxTransUnit_Type())
zxAnEponRmWanPrfMaxTransUnit.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmWanPrfMaxTransUnit.setStatus(_A)
class _ZxAnEponRmWanPrfMVid_Type(Integer32):defaultValue=4096;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094),ValueRangeConstraint(4096,4096))
_ZxAnEponRmWanPrfMVid_Type.__name__=_B
_ZxAnEponRmWanPrfMVid_Object=MibTableColumn
zxAnEponRmWanPrfMVid=_ZxAnEponRmWanPrfMVid_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,2,1,11),_ZxAnEponRmWanPrfMVid_Type())
zxAnEponRmWanPrfMVid.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmWanPrfMVid.setStatus(_A)
class _ZxAnEponRmWanPrfBindLanPortList_Type(Bits):namedValues=NamedValues(*(('lan1',0),('lan2',1),('lan3',2),('lan4',3),('lan5',4),('lan6',5),('lan7',6),('lan8',7),('lan9',8),('lan10',9),('lan11',10),('lan12',11),('lan13',12),('lan14',13),('lan15',14),('lan16',15)))
_ZxAnEponRmWanPrfBindLanPortList_Type.__name__=_O
_ZxAnEponRmWanPrfBindLanPortList_Object=MibTableColumn
zxAnEponRmWanPrfBindLanPortList=_ZxAnEponRmWanPrfBindLanPortList_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,2,1,12),_ZxAnEponRmWanPrfBindLanPortList_Type())
zxAnEponRmWanPrfBindLanPortList.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmWanPrfBindLanPortList.setStatus(_A)
class _ZxAnEponRmWanPrfBindSsidList_Type(Bits):namedValues=NamedValues(*(('ssid1',0),('ssid2',1),('ssid3',2),('ssid4',3),('ssid5',4),('ssid6',5),('ssid7',6),('ssid8',7),('ssid9',8),('ssid10',9),('ssid11',10),('ssid12',11),('ssid13',12),('ssid14',13),('ssid15',14),('ssid16',15)))
_ZxAnEponRmWanPrfBindSsidList_Type.__name__=_O
_ZxAnEponRmWanPrfBindSsidList_Object=MibTableColumn
zxAnEponRmWanPrfBindSsidList=_ZxAnEponRmWanPrfBindSsidList_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,2,1,13),_ZxAnEponRmWanPrfBindSsidList_Type())
zxAnEponRmWanPrfBindSsidList.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmWanPrfBindSsidList.setStatus(_A)
_ZxAnEponRmWanPrfRowStatus_Type=RowStatus
_ZxAnEponRmWanPrfRowStatus_Object=MibTableColumn
zxAnEponRmWanPrfRowStatus=_ZxAnEponRmWanPrfRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,2,1,50),_ZxAnEponRmWanPrfRowStatus_Type())
zxAnEponRmWanPrfRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmWanPrfRowStatus.setStatus(_A)
_ZxAnEponRmOnuWanConfTable_Object=MibTable
zxAnEponRmOnuWanConfTable=_ZxAnEponRmOnuWanConfTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,3))
if mibBuilder.loadTexts:zxAnEponRmOnuWanConfTable.setStatus(_A)
_ZxAnEponRmOnuWanConfEntry_Object=MibTableRow
zxAnEponRmOnuWanConfEntry=_ZxAnEponRmOnuWanConfEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,3,1))
zxAnEponRmOnuWanConfEntry.setIndexNames((0,_E,_F),(0,_E,_Aa))
if mibBuilder.loadTexts:zxAnEponRmOnuWanConfEntry.setStatus(_A)
class _ZxAnEponRmOnuWanPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZxAnEponRmOnuWanPortId_Type.__name__=_B
_ZxAnEponRmOnuWanPortId_Object=MibTableColumn
zxAnEponRmOnuWanPortId=_ZxAnEponRmOnuWanPortId_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,3,1,1),_ZxAnEponRmOnuWanPortId_Type())
zxAnEponRmOnuWanPortId.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponRmOnuWanPortId.setStatus(_A)
class _ZxAnEponRmOnuWanPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnEponRmOnuWanPrfName_Type.__name__=_L
_ZxAnEponRmOnuWanPrfName_Object=MibTableColumn
zxAnEponRmOnuWanPrfName=_ZxAnEponRmOnuWanPrfName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,3,1,2),_ZxAnEponRmOnuWanPrfName_Type())
zxAnEponRmOnuWanPrfName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmOnuWanPrfName.setStatus(_A)
class _ZxAnEponRmOnuWanIpAllocationMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_V,1),(_c,2),(_d,3)))
_ZxAnEponRmOnuWanIpAllocationMode_Type.__name__=_B
_ZxAnEponRmOnuWanIpAllocationMode_Object=MibTableColumn
zxAnEponRmOnuWanIpAllocationMode=_ZxAnEponRmOnuWanIpAllocationMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,3,1,3),_ZxAnEponRmOnuWanIpAllocationMode_Type())
zxAnEponRmOnuWanIpAllocationMode.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmOnuWanIpAllocationMode.setStatus(_A)
_ZxAnEponRmOnuWanIpAddr_Type=IpAddress
_ZxAnEponRmOnuWanIpAddr_Object=MibTableColumn
zxAnEponRmOnuWanIpAddr=_ZxAnEponRmOnuWanIpAddr_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,3,1,4),_ZxAnEponRmOnuWanIpAddr_Type())
zxAnEponRmOnuWanIpAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmOnuWanIpAddr.setStatus(_A)
_ZxAnEponRmOnuWanIpMask_Type=IpAddress
_ZxAnEponRmOnuWanIpMask_Object=MibTableColumn
zxAnEponRmOnuWanIpMask=_ZxAnEponRmOnuWanIpMask_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,3,1,5),_ZxAnEponRmOnuWanIpMask_Type())
zxAnEponRmOnuWanIpMask.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmOnuWanIpMask.setStatus(_A)
_ZxAnEponRmOnuWanIpGateway_Type=IpAddress
_ZxAnEponRmOnuWanIpGateway_Object=MibTableColumn
zxAnEponRmOnuWanIpGateway=_ZxAnEponRmOnuWanIpGateway_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,3,1,6),_ZxAnEponRmOnuWanIpGateway_Type())
zxAnEponRmOnuWanIpGateway.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmOnuWanIpGateway.setStatus(_A)
_ZxAnEponRmOnuWanPriDnsSvrIp_Type=IpAddress
_ZxAnEponRmOnuWanPriDnsSvrIp_Object=MibTableColumn
zxAnEponRmOnuWanPriDnsSvrIp=_ZxAnEponRmOnuWanPriDnsSvrIp_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,3,1,7),_ZxAnEponRmOnuWanPriDnsSvrIp_Type())
zxAnEponRmOnuWanPriDnsSvrIp.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmOnuWanPriDnsSvrIp.setStatus(_A)
_ZxAnEponRmOnuWanSecDnsSvrIp_Type=IpAddress
_ZxAnEponRmOnuWanSecDnsSvrIp_Object=MibTableColumn
zxAnEponRmOnuWanSecDnsSvrIp=_ZxAnEponRmOnuWanSecDnsSvrIp_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,3,1,8),_ZxAnEponRmOnuWanSecDnsSvrIp_Type())
zxAnEponRmOnuWanSecDnsSvrIp.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmOnuWanSecDnsSvrIp.setStatus(_A)
class _ZxAnEponRmOnuWanPppoeAuthMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_e,1),(_f,2),(_g,3)))
_ZxAnEponRmOnuWanPppoeAuthMode_Type.__name__=_B
_ZxAnEponRmOnuWanPppoeAuthMode_Object=MibTableColumn
zxAnEponRmOnuWanPppoeAuthMode=_ZxAnEponRmOnuWanPppoeAuthMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,3,1,9),_ZxAnEponRmOnuWanPppoeAuthMode_Type())
zxAnEponRmOnuWanPppoeAuthMode.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmOnuWanPppoeAuthMode.setStatus(_A)
class _ZxAnEponRmOnuWanPppoeUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnEponRmOnuWanPppoeUserName_Type.__name__=_L
_ZxAnEponRmOnuWanPppoeUserName_Object=MibTableColumn
zxAnEponRmOnuWanPppoeUserName=_ZxAnEponRmOnuWanPppoeUserName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,3,1,10),_ZxAnEponRmOnuWanPppoeUserName_Type())
zxAnEponRmOnuWanPppoeUserName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmOnuWanPppoeUserName.setStatus(_A)
class _ZxAnEponRmOnuWanPppoePassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnEponRmOnuWanPppoePassword_Type.__name__=_L
_ZxAnEponRmOnuWanPppoePassword_Object=MibTableColumn
zxAnEponRmOnuWanPppoePassword=_ZxAnEponRmOnuWanPppoePassword_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,3,1,11),_ZxAnEponRmOnuWanPppoePassword_Type())
zxAnEponRmOnuWanPppoePassword.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmOnuWanPppoePassword.setStatus(_A)
class _ZxAnEponRmOnuWanPppoePrxyNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnEponRmOnuWanPppoePrxyNum_Type.__name__=_B
_ZxAnEponRmOnuWanPppoePrxyNum_Object=MibTableColumn
zxAnEponRmOnuWanPppoePrxyNum=_ZxAnEponRmOnuWanPppoePrxyNum_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,3,1,12),_ZxAnEponRmOnuWanPppoePrxyNum_Type())
zxAnEponRmOnuWanPppoePrxyNum.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmOnuWanPppoePrxyNum.setStatus(_A)
class _ZxAnEponRmOnuWanPppoePrxyUserNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnEponRmOnuWanPppoePrxyUserNum_Type.__name__=_B
_ZxAnEponRmOnuWanPppoePrxyUserNum_Object=MibTableColumn
zxAnEponRmOnuWanPppoePrxyUserNum=_ZxAnEponRmOnuWanPppoePrxyUserNum_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,3,1,13),_ZxAnEponRmOnuWanPppoePrxyUserNum_Type())
zxAnEponRmOnuWanPppoePrxyUserNum.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmOnuWanPppoePrxyUserNum.setStatus(_A)
class _ZxAnEponRmOnuWanPortUpTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ZxAnEponRmOnuWanPortUpTime_Type.__name__=_T
_ZxAnEponRmOnuWanPortUpTime_Object=MibTableColumn
zxAnEponRmOnuWanPortUpTime=_ZxAnEponRmOnuWanPortUpTime_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,3,1,14),_ZxAnEponRmOnuWanPortUpTime_Type())
zxAnEponRmOnuWanPortUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmOnuWanPortUpTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponRmOnuWanPortUpTime.setUnits(_W)
_ZxAnEponRmOnuWanConfRowStatus_Type=RowStatus
_ZxAnEponRmOnuWanConfRowStatus_Object=MibTableColumn
zxAnEponRmOnuWanConfRowStatus=_ZxAnEponRmOnuWanConfRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,3,1,50),_ZxAnEponRmOnuWanConfRowStatus_Type())
zxAnEponRmOnuWanConfRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmOnuWanConfRowStatus.setStatus(_A)
_ZxAnEponRmOnuWanGlobalConfTable_Object=MibTable
zxAnEponRmOnuWanGlobalConfTable=_ZxAnEponRmOnuWanGlobalConfTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,4))
if mibBuilder.loadTexts:zxAnEponRmOnuWanGlobalConfTable.setStatus(_A)
_ZxAnEponRmOnuWanGlobalConfEntry_Object=MibTableRow
zxAnEponRmOnuWanGlobalConfEntry=_ZxAnEponRmOnuWanGlobalConfEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,4,1))
zxAnEponRmOnuWanGlobalConfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponRmOnuWanGlobalConfEntry.setStatus(_A)
class _ZxAnEponRmOnuWanGlbMaxUserNum_Type(Integer32):defaultValue=254;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnEponRmOnuWanGlbMaxUserNum_Type.__name__=_B
_ZxAnEponRmOnuWanGlbMaxUserNum_Object=MibTableColumn
zxAnEponRmOnuWanGlbMaxUserNum=_ZxAnEponRmOnuWanGlbMaxUserNum_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,53,4,1,1),_ZxAnEponRmOnuWanGlbMaxUserNum_Type())
zxAnEponRmOnuWanGlbMaxUserNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponRmOnuWanGlbMaxUserNum.setStatus(_A)
_ZxAnEponOnuPowerSavingMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuPowerSavingMgmt=_ZxAnEponOnuPowerSavingMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,1,55))
_ZxAnEponOnuPowerSavingTable_Object=MibTable
zxAnEponOnuPowerSavingTable=_ZxAnEponOnuPowerSavingTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,55,2))
if mibBuilder.loadTexts:zxAnEponOnuPowerSavingTable.setStatus(_A)
_ZxAnEponOnuPowerSavingEntry_Object=MibTableRow
zxAnEponOnuPowerSavingEntry=_ZxAnEponOnuPowerSavingEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,55,2,1))
zxAnEponOnuPowerSavingEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuPowerSavingEntry.setStatus(_A)
class _ZxAnEponOnuPwrSaveEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_ZxAnEponOnuPwrSaveEnable_Type.__name__=_B
_ZxAnEponOnuPwrSaveEnable_Object=MibTableColumn
zxAnEponOnuPwrSaveEnable=_ZxAnEponOnuPwrSaveEnable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,55,2,1,1),_ZxAnEponOnuPwrSaveEnable_Type())
zxAnEponOnuPwrSaveEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPwrSaveEnable.setStatus(_A)
class _ZxAnEponOnuPwrSaveSleepMode_Type(Bits):namedValues=NamedValues(*(('tx',0),('trx',1)))
_ZxAnEponOnuPwrSaveSleepMode_Type.__name__=_O
_ZxAnEponOnuPwrSaveSleepMode_Object=MibTableColumn
zxAnEponOnuPwrSaveSleepMode=_ZxAnEponOnuPwrSaveSleepMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,55,2,1,2),_ZxAnEponOnuPwrSaveSleepMode_Type())
zxAnEponOnuPwrSaveSleepMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuPwrSaveSleepMode.setStatus(_A)
class _ZxAnEponOnuPwrSaveSleepConfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tx',1),('trx',2)))
_ZxAnEponOnuPwrSaveSleepConfMode_Type.__name__=_B
_ZxAnEponOnuPwrSaveSleepConfMode_Object=MibTableColumn
zxAnEponOnuPwrSaveSleepConfMode=_ZxAnEponOnuPwrSaveSleepConfMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,55,2,1,3),_ZxAnEponOnuPwrSaveSleepConfMode_Type())
zxAnEponOnuPwrSaveSleepConfMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPwrSaveSleepConfMode.setStatus(_A)
class _ZxAnEponOnuPwrSaveEarlyWakeUp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_n,1),(_o,2)))
_ZxAnEponOnuPwrSaveEarlyWakeUp_Type.__name__=_B
_ZxAnEponOnuPwrSaveEarlyWakeUp_Object=MibTableColumn
zxAnEponOnuPwrSaveEarlyWakeUp=_ZxAnEponOnuPwrSaveEarlyWakeUp_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,55,2,1,4),_ZxAnEponOnuPwrSaveEarlyWakeUp_Type())
zxAnEponOnuPwrSaveEarlyWakeUp.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuPwrSaveEarlyWakeUp.setStatus(_A)
class _ZxAnEponOnuPwrSaveEarlyWakeUpEn_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_ZxAnEponOnuPwrSaveEarlyWakeUpEn_Type.__name__=_B
_ZxAnEponOnuPwrSaveEarlyWakeUpEn_Object=MibTableColumn
zxAnEponOnuPwrSaveEarlyWakeUpEn=_ZxAnEponOnuPwrSaveEarlyWakeUpEn_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,55,2,1,5),_ZxAnEponOnuPwrSaveEarlyWakeUpEn_Type())
zxAnEponOnuPwrSaveEarlyWakeUpEn.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPwrSaveEarlyWakeUpEn.setStatus(_A)
class _ZxAnEponOnuPwrSaveSleepDuration_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,62500000))
_ZxAnEponOnuPwrSaveSleepDuration_Type.__name__=_B
_ZxAnEponOnuPwrSaveSleepDuration_Object=MibTableColumn
zxAnEponOnuPwrSaveSleepDuration=_ZxAnEponOnuPwrSaveSleepDuration_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,55,2,1,6),_ZxAnEponOnuPwrSaveSleepDuration_Type())
zxAnEponOnuPwrSaveSleepDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPwrSaveSleepDuration.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponOnuPwrSaveSleepDuration.setUnits('TQ')
class _ZxAnEponOnuPwrSaveWakeUpDuration_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,62500000))
_ZxAnEponOnuPwrSaveWakeUpDuration_Type.__name__=_B
_ZxAnEponOnuPwrSaveWakeUpDuration_Object=MibTableColumn
zxAnEponOnuPwrSaveWakeUpDuration=_ZxAnEponOnuPwrSaveWakeUpDuration_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,55,2,1,7),_ZxAnEponOnuPwrSaveWakeUpDuration_Type())
zxAnEponOnuPwrSaveWakeUpDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPwrSaveWakeUpDuration.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponOnuPwrSaveWakeUpDuration.setUnits('TQ')
class _ZxAnEponOnuPwrSaveMaxRefreshTime_Type(Unsigned32):defaultValue=8000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ZxAnEponOnuPwrSaveMaxRefreshTime_Type.__name__=_T
_ZxAnEponOnuPwrSaveMaxRefreshTime_Object=MibTableColumn
zxAnEponOnuPwrSaveMaxRefreshTime=_ZxAnEponOnuPwrSaveMaxRefreshTime_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,55,2,1,8),_ZxAnEponOnuPwrSaveMaxRefreshTime_Type())
zxAnEponOnuPwrSaveMaxRefreshTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPwrSaveMaxRefreshTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponOnuPwrSaveMaxRefreshTime.setUnits('125Microseconds')
_ZxAnEponOnuProtectMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuProtectMgmt=_ZxAnEponOnuProtectMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,1,56))
_ZxAnOnuProtectConfTable_Object=MibTable
zxAnOnuProtectConfTable=_ZxAnOnuProtectConfTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,56,56))
if mibBuilder.loadTexts:zxAnOnuProtectConfTable.setStatus(_A)
_ZxAnOnuProtectConfEntry_Object=MibTableRow
zxAnOnuProtectConfEntry=_ZxAnOnuProtectConfEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,56,56,1))
zxAnOnuProtectConfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnOnuProtectConfEntry.setStatus(_A)
class _ZxAnOnuProtectLosTimeByOptSignal_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZxAnOnuProtectLosTimeByOptSignal_Type.__name__=_B
_ZxAnOnuProtectLosTimeByOptSignal_Object=MibTableColumn
zxAnOnuProtectLosTimeByOptSignal=_ZxAnOnuProtectLosTimeByOptSignal_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,56,56,1,1),_ZxAnOnuProtectLosTimeByOptSignal_Type())
zxAnOnuProtectLosTimeByOptSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnOnuProtectLosTimeByOptSignal.setStatus(_A)
if mibBuilder.loadTexts:zxAnOnuProtectLosTimeByOptSignal.setUnits(_Ab)
class _ZxAnOnuProtectLosTimeByMpcp_Type(Integer32):defaultValue=55;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZxAnOnuProtectLosTimeByMpcp_Type.__name__=_B
_ZxAnOnuProtectLosTimeByMpcp_Object=MibTableColumn
zxAnOnuProtectLosTimeByMpcp=_ZxAnOnuProtectLosTimeByMpcp_Object((1,3,6,1,4,1,3902,1015,1010,1,1,1,56,56,1,2),_ZxAnOnuProtectLosTimeByMpcp_Type())
zxAnOnuProtectLosTimeByMpcp.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnOnuProtectLosTimeByMpcp.setStatus(_A)
if mibBuilder.loadTexts:zxAnOnuProtectLosTimeByMpcp.setUnits(_Ab)
_ZxAnEponOnuExtendedActionMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuExtendedActionMgmt=_ZxAnEponOnuExtendedActionMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,2))
_ZxAnEponOnuActionTable_Object=MibTable
zxAnEponOnuActionTable=_ZxAnEponOnuActionTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,2,1))
if mibBuilder.loadTexts:zxAnEponOnuActionTable.setStatus(_A)
_ZxAnEponOnuActionEntry_Object=MibTableRow
zxAnEponOnuActionEntry=_ZxAnEponOnuActionEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,2,1,1))
zxAnEponOnuActionEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuActionEntry.setStatus(_A)
class _ZxAnEponOnuAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_l,1))
_ZxAnEponOnuAction_Type.__name__=_B
_ZxAnEponOnuAction_Object=MibTableColumn
zxAnEponOnuAction=_ZxAnEponOnuAction_Object((1,3,6,1,4,1,3902,1015,1010,1,1,2,1,1,1),_ZxAnEponOnuAction_Type())
zxAnEponOnuAction.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuAction.setStatus(_A)
_ZxAnEponOnuSaveActionTable_Object=MibTable
zxAnEponOnuSaveActionTable=_ZxAnEponOnuSaveActionTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,2,2))
if mibBuilder.loadTexts:zxAnEponOnuSaveActionTable.setStatus(_A)
_ZxAnEponOnuSaveActionEntry_Object=MibTableRow
zxAnEponOnuSaveActionEntry=_ZxAnEponOnuSaveActionEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,2,2,1))
zxAnEponOnuSaveActionEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuSaveActionEntry.setStatus(_A)
class _ZxAnEponOnuSaveAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('save',1),('clear',2),('restoreFactory',3)))
_ZxAnEponOnuSaveAction_Type.__name__=_B
_ZxAnEponOnuSaveAction_Object=MibTableColumn
zxAnEponOnuSaveAction=_ZxAnEponOnuSaveAction_Object((1,3,6,1,4,1,3902,1015,1010,1,1,2,2,1,1),_ZxAnEponOnuSaveAction_Type())
zxAnEponOnuSaveAction.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuSaveAction.setStatus(_A)
_ZxAnEponOnuSetHGMACCodeTable_Object=MibTable
zxAnEponOnuSetHGMACCodeTable=_ZxAnEponOnuSetHGMACCodeTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,2,3))
if mibBuilder.loadTexts:zxAnEponOnuSetHGMACCodeTable.setStatus(_A)
_ZxAnEponOnuSetHGMACCodeEntry_Object=MibTableRow
zxAnEponOnuSetHGMACCodeEntry=_ZxAnEponOnuSetHGMACCodeEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,2,3,1))
zxAnEponOnuSetHGMACCodeEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuSetHGMACCodeEntry.setStatus(_A)
_ZxAnEponOnuHGMACCode_Type=OctetString
_ZxAnEponOnuHGMACCode_Object=MibTableColumn
zxAnEponOnuHGMACCode=_ZxAnEponOnuHGMACCode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,2,3,1,1),_ZxAnEponOnuHGMACCode_Type())
zxAnEponOnuHGMACCode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuHGMACCode.setStatus(_A)
_ZxAnEponOnuHGMACVlanTable_Object=MibTable
zxAnEponOnuHGMACVlanTable=_ZxAnEponOnuHGMACVlanTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,2,4))
if mibBuilder.loadTexts:zxAnEponOnuHGMACVlanTable.setStatus(_A)
_ZxAnEponOnuHGMACVlanEntry_Object=MibTableRow
zxAnEponOnuHGMACVlanEntry=_ZxAnEponOnuHGMACVlanEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,2,4,1))
zxAnEponOnuHGMACVlanEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuHGMACVlanEntry.setStatus(_A)
class _ZxAnEponOnuHGVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnEponOnuHGVlan_Type.__name__=_B
_ZxAnEponOnuHGVlan_Object=MibTableColumn
zxAnEponOnuHGVlan=_ZxAnEponOnuHGVlan_Object((1,3,6,1,4,1,3902,1015,1010,1,1,2,4,1,1),_ZxAnEponOnuHGVlan_Type())
zxAnEponOnuHGVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuHGVlan.setStatus(_A)
_ZxAnEponOnuHGStateTable_Object=MibTable
zxAnEponOnuHGStateTable=_ZxAnEponOnuHGStateTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,2,5))
if mibBuilder.loadTexts:zxAnEponOnuHGStateTable.setStatus(_A)
_ZxAnEponOnuHGStateEntry_Object=MibTableRow
zxAnEponOnuHGStateEntry=_ZxAnEponOnuHGStateEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,2,5,1))
zxAnEponOnuHGStateEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuHGStateEntry.setStatus(_A)
_ZxAnEponOnuHGMAC_Type=MacAddress
_ZxAnEponOnuHGMAC_Object=MibTableColumn
zxAnEponOnuHGMAC=_ZxAnEponOnuHGMAC_Object((1,3,6,1,4,1,3902,1015,1010,1,1,2,5,1,1),_ZxAnEponOnuHGMAC_Type())
zxAnEponOnuHGMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuHGMAC.setStatus(_A)
class _ZxEponOnuHGState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ZxEponOnuHGState_Type.__name__=_B
_ZxEponOnuHGState_Object=MibTableColumn
zxEponOnuHGState=_ZxEponOnuHGState_Object((1,3,6,1,4,1,3902,1015,1010,1,1,2,5,1,2),_ZxEponOnuHGState_Type())
zxEponOnuHGState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxEponOnuHGState.setStatus(_A)
_ZxAnEponOnuStdAttrMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuStdAttrMgmt=_ZxAnEponOnuStdAttrMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,3))
_ZxAnEponOnuPhyMgmtTable_Object=MibTable
zxAnEponOnuPhyMgmtTable=_ZxAnEponOnuPhyMgmtTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,3,1))
if mibBuilder.loadTexts:zxAnEponOnuPhyMgmtTable.setStatus(_A)
_ZxAnEponOnuPhyMgmtEntry_Object=MibTableRow
zxAnEponOnuPhyMgmtEntry=_ZxAnEponOnuPhyMgmtEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,3,1,1))
zxAnEponOnuPhyMgmtEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuPhyMgmtEntry.setStatus(_A)
class _ZxAnEponOnuPhyAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_R,2)))
_ZxAnEponOnuPhyAdminState_Type.__name__=_B
_ZxAnEponOnuPhyAdminState_Object=MibTableColumn
zxAnEponOnuPhyAdminState=_ZxAnEponOnuPhyAdminState_Object((1,3,6,1,4,1,3902,1015,1010,1,1,3,1,1,1),_ZxAnEponOnuPhyAdminState_Type())
zxAnEponOnuPhyAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuPhyAdminState.setStatus(_A)
_ZxAnEponOnuAutoNegAttrTable_Object=MibTable
zxAnEponOnuAutoNegAttrTable=_ZxAnEponOnuAutoNegAttrTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,3,2))
if mibBuilder.loadTexts:zxAnEponOnuAutoNegAttrTable.setStatus(_A)
_ZxAnEponOnuAutoNegAttrEntry_Object=MibTableRow
zxAnEponOnuAutoNegAttrEntry=_ZxAnEponOnuAutoNegAttrEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,3,2,1))
zxAnEponOnuAutoNegAttrEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuAutoNegAttrEntry.setStatus(_A)
class _ZxAnEponOnuAutoNegAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_R,2)))
_ZxAnEponOnuAutoNegAdminState_Type.__name__=_B
_ZxAnEponOnuAutoNegAdminState_Object=MibTableColumn
zxAnEponOnuAutoNegAdminState=_ZxAnEponOnuAutoNegAdminState_Object((1,3,6,1,4,1,3902,1015,1010,1,1,3,2,1,1),_ZxAnEponOnuAutoNegAdminState_Type())
zxAnEponOnuAutoNegAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuAutoNegAdminState.setStatus(_A)
class _ZxAnEponOnuAutoNegCapability_Type(Bits):namedValues=NamedValues(*((_Ac,0),('zx-OTHER',1),(_Ad,2),(_Ae,3),(_Af,4),(_Ag,5),(_Ah,6),(_Ai,7),(_Aj,8),(_Ak,9),(_Al,10),(_Am,11),(_An,12),(_Ao,13),(_Ap,14),(_Aq,15),(_Ar,16),(_As,17),(_At,18),(_Au,19),(_Av,20)))
_ZxAnEponOnuAutoNegCapability_Type.__name__=_O
_ZxAnEponOnuAutoNegCapability_Object=MibTableColumn
zxAnEponOnuAutoNegCapability=_ZxAnEponOnuAutoNegCapability_Object((1,3,6,1,4,1,3902,1015,1010,1,1,3,2,1,2),_ZxAnEponOnuAutoNegCapability_Type())
zxAnEponOnuAutoNegCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuAutoNegCapability.setStatus(_A)
class _ZxAnEponOnuAutoNegCapAdvertised_Type(Bits):namedValues=NamedValues(*((_Ac,0),('zx-OTHER',1),(_Ad,2),(_Ae,3),(_Af,4),(_Ag,5),(_Ah,6),(_Ai,7),(_Aj,8),(_Ak,9),(_Al,10),(_Am,11),(_An,12),(_Ao,13),(_Ap,14),(_Aq,15),(_Ar,16),(_As,17),(_At,18),(_Au,19),(_Av,20)))
_ZxAnEponOnuAutoNegCapAdvertised_Type.__name__=_O
_ZxAnEponOnuAutoNegCapAdvertised_Object=MibTableColumn
zxAnEponOnuAutoNegCapAdvertised=_ZxAnEponOnuAutoNegCapAdvertised_Object((1,3,6,1,4,1,3902,1015,1010,1,1,3,2,1,3),_ZxAnEponOnuAutoNegCapAdvertised_Type())
zxAnEponOnuAutoNegCapAdvertised.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuAutoNegCapAdvertised.setStatus(_A)
class _ZxAnEponOnuEthIfConfDuplexSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,99)));namedValues=NamedValues(*((_Aw,1),('half-10',2),('full-10',3),('half-100',4),('full-100',5),('full-1000',6),('full-10000',7),('illegal',99)))
_ZxAnEponOnuEthIfConfDuplexSpeed_Type.__name__=_B
_ZxAnEponOnuEthIfConfDuplexSpeed_Object=MibTableColumn
zxAnEponOnuEthIfConfDuplexSpeed=_ZxAnEponOnuEthIfConfDuplexSpeed_Object((1,3,6,1,4,1,3902,1015,1010,1,1,3,2,1,4),_ZxAnEponOnuEthIfConfDuplexSpeed_Type())
zxAnEponOnuEthIfConfDuplexSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuEthIfConfDuplexSpeed.setStatus(_A)
class _ZxAnEponOnuEthIfActualDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Aw,1),('half',2),('full',3)))
_ZxAnEponOnuEthIfActualDuplex_Type.__name__=_B
_ZxAnEponOnuEthIfActualDuplex_Object=MibTableColumn
zxAnEponOnuEthIfActualDuplex=_ZxAnEponOnuEthIfActualDuplex_Object((1,3,6,1,4,1,3902,1015,1010,1,1,3,2,1,5),_ZxAnEponOnuEthIfActualDuplex_Type())
zxAnEponOnuEthIfActualDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuEthIfActualDuplex.setStatus(_A)
class _ZxAnEponOnuEthIfActualSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('speed-10',1),('speed-100',2),('speed-1000',3),('speed-10000',4),('auto-speed',5)))
_ZxAnEponOnuEthIfActualSpeed_Type.__name__=_B
_ZxAnEponOnuEthIfActualSpeed_Object=MibTableColumn
zxAnEponOnuEthIfActualSpeed=_ZxAnEponOnuEthIfActualSpeed_Object((1,3,6,1,4,1,3902,1015,1010,1,1,3,2,1,6),_ZxAnEponOnuEthIfActualSpeed_Type())
zxAnEponOnuEthIfActualSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuEthIfActualSpeed.setStatus(_A)
_ZxAnEponOnuFecMgmtTable_Object=MibTable
zxAnEponOnuFecMgmtTable=_ZxAnEponOnuFecMgmtTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,3,3))
if mibBuilder.loadTexts:zxAnEponOnuFecMgmtTable.setStatus(_A)
_ZxAnEponOnuFecMgmtEntry_Object=MibTableRow
zxAnEponOnuFecMgmtEntry=_ZxAnEponOnuFecMgmtEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,3,3,1))
zxAnEponOnuFecMgmtEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuFecMgmtEntry.setStatus(_A)
class _ZxAnEponOnuFecAbility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),(_n,2),('notsupported',3)))
_ZxAnEponOnuFecAbility_Type.__name__=_B
_ZxAnEponOnuFecAbility_Object=MibTableColumn
zxAnEponOnuFecAbility=_ZxAnEponOnuFecAbility_Object((1,3,6,1,4,1,3902,1015,1010,1,1,3,3,1,1),_ZxAnEponOnuFecAbility_Type())
zxAnEponOnuFecAbility.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuFecAbility.setStatus(_A)
class _ZxAnEponOnuFecMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),(_R,2),(_S,3)))
_ZxAnEponOnuFecMode_Type.__name__=_B
_ZxAnEponOnuFecMode_Object=MibTableColumn
zxAnEponOnuFecMode=_ZxAnEponOnuFecMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,3,3,1,2),_ZxAnEponOnuFecMode_Type())
zxAnEponOnuFecMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuFecMode.setStatus(_A)
_ZxAnEponOnuStdActionMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuStdActionMgmt=_ZxAnEponOnuStdActionMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,4))
_ZxAnEponOnuAutoNegActionTable_Object=MibTable
zxAnEponOnuAutoNegActionTable=_ZxAnEponOnuAutoNegActionTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,4,1))
if mibBuilder.loadTexts:zxAnEponOnuAutoNegActionTable.setStatus(_A)
_ZxAnEponOnuAutoNegActionEntry_Object=MibTableRow
zxAnEponOnuAutoNegActionEntry=_ZxAnEponOnuAutoNegActionEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,4,1,1))
zxAnEponOnuAutoNegActionEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuAutoNegActionEntry.setStatus(_A)
class _ZxAnEponOnuAutoNegAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('restart',1))
_ZxAnEponOnuAutoNegAction_Type.__name__=_B
_ZxAnEponOnuAutoNegAction_Object=MibTableColumn
zxAnEponOnuAutoNegAction=_ZxAnEponOnuAutoNegAction_Object((1,3,6,1,4,1,3902,1015,1010,1,1,4,1,1,1),_ZxAnEponOnuAutoNegAction_Type())
zxAnEponOnuAutoNegAction.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuAutoNegAction.setStatus(_A)
_ZxAnEponOnuDbaAttrMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuDbaAttrMgmt=_ZxAnEponOnuDbaAttrMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,5))
_ZxAnEponOnuDbaQueueThresholdsTable_Object=MibTable
zxAnEponOnuDbaQueueThresholdsTable=_ZxAnEponOnuDbaQueueThresholdsTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,5,1))
if mibBuilder.loadTexts:zxAnEponOnuDbaQueueThresholdsTable.setStatus(_A)
_ZxAnEponOnuDbaQueueThresholdsEntry_Object=MibTableRow
zxAnEponOnuDbaQueueThresholdsEntry=_ZxAnEponOnuDbaQueueThresholdsEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,5,1,1))
zxAnEponOnuDbaQueueThresholdsEntry.setIndexNames((0,_E,_F),(0,_E,_Ax))
if mibBuilder.loadTexts:zxAnEponOnuDbaQueueThresholdsEntry.setStatus(_A)
class _ZxAnEponOnuDbaQueueSetIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ZxAnEponOnuDbaQueueSetIndex_Type.__name__=_B
_ZxAnEponOnuDbaQueueSetIndex_Object=MibTableColumn
zxAnEponOnuDbaQueueSetIndex=_ZxAnEponOnuDbaQueueSetIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,1,5,1,1,1),_ZxAnEponOnuDbaQueueSetIndex_Type())
zxAnEponOnuDbaQueueSetIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuDbaQueueSetIndex.setStatus(_A)
_ZxAnEponOnuDbaQueueThresholds1_Type=Integer32
_ZxAnEponOnuDbaQueueThresholds1_Object=MibTableColumn
zxAnEponOnuDbaQueueThresholds1=_ZxAnEponOnuDbaQueueThresholds1_Object((1,3,6,1,4,1,3902,1015,1010,1,1,5,1,1,2),_ZxAnEponOnuDbaQueueThresholds1_Type())
zxAnEponOnuDbaQueueThresholds1.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuDbaQueueThresholds1.setStatus(_A)
_ZxAnEponOnuDbaQueueThresholds2_Type=Integer32
_ZxAnEponOnuDbaQueueThresholds2_Object=MibTableColumn
zxAnEponOnuDbaQueueThresholds2=_ZxAnEponOnuDbaQueueThresholds2_Object((1,3,6,1,4,1,3902,1015,1010,1,1,5,1,1,3),_ZxAnEponOnuDbaQueueThresholds2_Type())
zxAnEponOnuDbaQueueThresholds2.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuDbaQueueThresholds2.setStatus(_A)
_ZxAnEponOnuDbaQueueThresholds3_Type=Integer32
_ZxAnEponOnuDbaQueueThresholds3_Object=MibTableColumn
zxAnEponOnuDbaQueueThresholds3=_ZxAnEponOnuDbaQueueThresholds3_Object((1,3,6,1,4,1,3902,1015,1010,1,1,5,1,1,4),_ZxAnEponOnuDbaQueueThresholds3_Type())
zxAnEponOnuDbaQueueThresholds3.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuDbaQueueThresholds3.setStatus(_A)
_ZxAnEponOnuDbaQueueThresholds4_Type=Integer32
_ZxAnEponOnuDbaQueueThresholds4_Object=MibTableColumn
zxAnEponOnuDbaQueueThresholds4=_ZxAnEponOnuDbaQueueThresholds4_Object((1,3,6,1,4,1,3902,1015,1010,1,1,5,1,1,5),_ZxAnEponOnuDbaQueueThresholds4_Type())
zxAnEponOnuDbaQueueThresholds4.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuDbaQueueThresholds4.setStatus(_A)
_ZxAnEponOnuDbaQueueThresholds5_Type=Integer32
_ZxAnEponOnuDbaQueueThresholds5_Object=MibTableColumn
zxAnEponOnuDbaQueueThresholds5=_ZxAnEponOnuDbaQueueThresholds5_Object((1,3,6,1,4,1,3902,1015,1010,1,1,5,1,1,6),_ZxAnEponOnuDbaQueueThresholds5_Type())
zxAnEponOnuDbaQueueThresholds5.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuDbaQueueThresholds5.setStatus(_A)
_ZxAnEponOnuDbaQueueThresholds6_Type=Integer32
_ZxAnEponOnuDbaQueueThresholds6_Object=MibTableColumn
zxAnEponOnuDbaQueueThresholds6=_ZxAnEponOnuDbaQueueThresholds6_Object((1,3,6,1,4,1,3902,1015,1010,1,1,5,1,1,7),_ZxAnEponOnuDbaQueueThresholds6_Type())
zxAnEponOnuDbaQueueThresholds6.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuDbaQueueThresholds6.setStatus(_A)
_ZxAnEponOnuDbaQueueThresholds7_Type=Integer32
_ZxAnEponOnuDbaQueueThresholds7_Object=MibTableColumn
zxAnEponOnuDbaQueueThresholds7=_ZxAnEponOnuDbaQueueThresholds7_Object((1,3,6,1,4,1,3902,1015,1010,1,1,5,1,1,8),_ZxAnEponOnuDbaQueueThresholds7_Type())
zxAnEponOnuDbaQueueThresholds7.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuDbaQueueThresholds7.setStatus(_A)
_ZxAnEponOnuDbaQueueThresholds8_Type=Integer32
_ZxAnEponOnuDbaQueueThresholds8_Object=MibTableColumn
zxAnEponOnuDbaQueueThresholds8=_ZxAnEponOnuDbaQueueThresholds8_Object((1,3,6,1,4,1,3902,1015,1010,1,1,5,1,1,9),_ZxAnEponOnuDbaQueueThresholds8_Type())
zxAnEponOnuDbaQueueThresholds8.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuDbaQueueThresholds8.setStatus(_A)
_ZxAnEponOnuDbaQueueSetActiveTable_Object=MibTable
zxAnEponOnuDbaQueueSetActiveTable=_ZxAnEponOnuDbaQueueSetActiveTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,5,2))
if mibBuilder.loadTexts:zxAnEponOnuDbaQueueSetActiveTable.setStatus(_A)
_ZxAnEponOnuDbaQueueSetActiveEntry_Object=MibTableRow
zxAnEponOnuDbaQueueSetActiveEntry=_ZxAnEponOnuDbaQueueSetActiveEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,5,2,1))
zxAnEponOnuDbaQueueSetActiveEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuDbaQueueSetActiveEntry.setStatus(_A)
_ZxAnEponOnuDbaQueueSetList_Type=OctetString
_ZxAnEponOnuDbaQueueSetList_Object=MibTableColumn
zxAnEponOnuDbaQueueSetList=_ZxAnEponOnuDbaQueueSetList_Object((1,3,6,1,4,1,3902,1015,1010,1,1,5,2,1,1),_ZxAnEponOnuDbaQueueSetList_Type())
zxAnEponOnuDbaQueueSetList.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuDbaQueueSetList.setStatus(_A)
_ZxAnEponOnuProfileMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuProfileMgmt=_ZxAnEponOnuProfileMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,6))
_ZxAnEponOnuProfileIndexNextTable_Object=MibTable
zxAnEponOnuProfileIndexNextTable=_ZxAnEponOnuProfileIndexNextTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,6,1))
if mibBuilder.loadTexts:zxAnEponOnuProfileIndexNextTable.setStatus(_A)
_ZxAnEponOnuProfileIndexNextEntry_Object=MibTableRow
zxAnEponOnuProfileIndexNextEntry=_ZxAnEponOnuProfileIndexNextEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,6,1,1))
zxAnEponOnuProfileIndexNextEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuProfileIndexNextEntry.setStatus(_A)
_ZxAnEponOnuClassMarkingConditionIdNext_Type=Integer32
_ZxAnEponOnuClassMarkingConditionIdNext_Object=MibTableColumn
zxAnEponOnuClassMarkingConditionIdNext=_ZxAnEponOnuClassMarkingConditionIdNext_Object((1,3,6,1,4,1,3902,1015,1010,1,1,6,1,1,1),_ZxAnEponOnuClassMarkingConditionIdNext_Type())
zxAnEponOnuClassMarkingConditionIdNext.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingConditionIdNext.setStatus(_A)
_ZxAnEponOnuClassMarkingRuleIdNext_Type=Integer32
_ZxAnEponOnuClassMarkingRuleIdNext_Object=MibTableColumn
zxAnEponOnuClassMarkingRuleIdNext=_ZxAnEponOnuClassMarkingRuleIdNext_Object((1,3,6,1,4,1,3902,1015,1010,1,1,6,1,1,2),_ZxAnEponOnuClassMarkingRuleIdNext_Type())
zxAnEponOnuClassMarkingRuleIdNext.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuClassMarkingRuleIdNext.setStatus(_A)
_ZxAnEponOnuPfmncStatis_ObjectIdentity=ObjectIdentity
zxAnEponOnuPfmncStatis=_ZxAnEponOnuPfmncStatis_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,7))
_ZxAnEponOnuPfmncStatisTable_Object=MibTable
zxAnEponOnuPfmncStatisTable=_ZxAnEponOnuPfmncStatisTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,1))
if mibBuilder.loadTexts:zxAnEponOnuPfmncStatisTable.setStatus(_A)
_ZxAnEponOnuPfmncStatisEntry_Object=MibTableRow
zxAnEponOnuPfmncStatisEntry=_ZxAnEponOnuPfmncStatisEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,1,1))
zxAnEponOnuPfmncStatisEntry.setIndexNames((0,_E,_F),(0,_E,_H),(0,_E,'portType'))
if mibBuilder.loadTexts:zxAnEponOnuPfmncStatisEntry.setStatus(_A)
class _PortType_Type(Integer32):defaultValue=0
_PortType_Type.__name__=_B
_PortType_Object=MibTableColumn
portType=_PortType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,1,1,1),_PortType_Type())
portType.setMaxAccess(_I)
if mibBuilder.loadTexts:portType.setStatus(_A)
_Parameter1_Type=Counter64
_Parameter1_Object=MibTableColumn
parameter1=_Parameter1_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,1,1,2),_Parameter1_Type())
parameter1.setMaxAccess(_D)
if mibBuilder.loadTexts:parameter1.setStatus(_A)
_Parameter2_Type=Counter64
_Parameter2_Object=MibTableColumn
parameter2=_Parameter2_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,1,1,3),_Parameter2_Type())
parameter2.setMaxAccess(_D)
if mibBuilder.loadTexts:parameter2.setStatus(_A)
_Parameter3_Type=Counter64
_Parameter3_Object=MibTableColumn
parameter3=_Parameter3_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,1,1,4),_Parameter3_Type())
parameter3.setMaxAccess(_D)
if mibBuilder.loadTexts:parameter3.setStatus(_A)
_Parameter4_Type=Counter64
_Parameter4_Object=MibTableColumn
parameter4=_Parameter4_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,1,1,5),_Parameter4_Type())
parameter4.setMaxAccess(_D)
if mibBuilder.loadTexts:parameter4.setStatus(_A)
_Parameter5_Type=Counter64
_Parameter5_Object=MibTableColumn
parameter5=_Parameter5_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,1,1,6),_Parameter5_Type())
parameter5.setMaxAccess(_D)
if mibBuilder.loadTexts:parameter5.setStatus(_A)
_Parameter6_Type=Counter64
_Parameter6_Object=MibTableColumn
parameter6=_Parameter6_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,1,1,7),_Parameter6_Type())
parameter6.setMaxAccess(_D)
if mibBuilder.loadTexts:parameter6.setStatus(_A)
_Parameter7_Type=Counter64
_Parameter7_Object=MibTableColumn
parameter7=_Parameter7_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,1,1,8),_Parameter7_Type())
parameter7.setMaxAccess(_D)
if mibBuilder.loadTexts:parameter7.setStatus(_A)
_Parameter8_Type=Counter64
_Parameter8_Object=MibTableColumn
parameter8=_Parameter8_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,1,1,9),_Parameter8_Type())
parameter8.setMaxAccess(_D)
if mibBuilder.loadTexts:parameter8.setStatus(_A)
_Parameter9_Type=Counter64
_Parameter9_Object=MibTableColumn
parameter9=_Parameter9_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,1,1,10),_Parameter9_Type())
parameter9.setMaxAccess(_D)
if mibBuilder.loadTexts:parameter9.setStatus(_A)
_Parameter10_Type=Counter64
_Parameter10_Object=MibTableColumn
parameter10=_Parameter10_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,1,1,11),_Parameter10_Type())
parameter10.setMaxAccess(_D)
if mibBuilder.loadTexts:parameter10.setStatus(_A)
_Parameter11_Type=Counter64
_Parameter11_Object=MibTableColumn
parameter11=_Parameter11_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,1,1,12),_Parameter11_Type())
parameter11.setMaxAccess(_D)
if mibBuilder.loadTexts:parameter11.setStatus(_A)
_Parameter12_Type=Counter64
_Parameter12_Object=MibTableColumn
parameter12=_Parameter12_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,1,1,13),_Parameter12_Type())
parameter12.setMaxAccess(_D)
if mibBuilder.loadTexts:parameter12.setStatus(_A)
_Parameter13_Type=Counter64
_Parameter13_Object=MibTableColumn
parameter13=_Parameter13_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,1,1,14),_Parameter13_Type())
parameter13.setMaxAccess(_D)
if mibBuilder.loadTexts:parameter13.setStatus(_A)
_ZxAnEponRmPerfConfTable_Object=MibTable
zxAnEponRmPerfConfTable=_ZxAnEponRmPerfConfTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,2))
if mibBuilder.loadTexts:zxAnEponRmPerfConfTable.setStatus(_A)
_ZxAnEponRmPerfConfEntry_Object=MibTableRow
zxAnEponRmPerfConfEntry=_ZxAnEponRmPerfConfEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,2,1))
zxAnEponRmPerfConfEntry.setIndexNames((0,_E,_F),(0,_E,_a),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponRmPerfConfEntry.setStatus(_A)
class _ZxAnEponRmPerfOnuPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ponPort',1),('ethPort',2)))
_ZxAnEponRmPerfOnuPortType_Type.__name__=_B
_ZxAnEponRmPerfOnuPortType_Object=MibTableColumn
zxAnEponRmPerfOnuPortType=_ZxAnEponRmPerfOnuPortType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,2,1,1),_ZxAnEponRmPerfOnuPortType_Type())
zxAnEponRmPerfOnuPortType.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponRmPerfOnuPortType.setStatus(_A)
class _ZxAnEponRmPerfOnuHisStatInterval_Type(Integer32):defaultValue=900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ZxAnEponRmPerfOnuHisStatInterval_Type.__name__=_B
_ZxAnEponRmPerfOnuHisStatInterval_Object=MibTableColumn
zxAnEponRmPerfOnuHisStatInterval=_ZxAnEponRmPerfOnuHisStatInterval_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,2,1,2),_ZxAnEponRmPerfOnuHisStatInterval_Type())
zxAnEponRmPerfOnuHisStatInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmPerfOnuHisStatInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponRmPerfOnuHisStatInterval.setUnits(_W)
_ZxAnEponRmPerfConfRowStatus_Type=RowStatus
_ZxAnEponRmPerfConfRowStatus_Object=MibTableColumn
zxAnEponRmPerfConfRowStatus=_ZxAnEponRmPerfConfRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,2,1,50),_ZxAnEponRmPerfConfRowStatus_Type())
zxAnEponRmPerfConfRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnEponRmPerfConfRowStatus.setStatus(_A)
_ZxAnEponRmEthCurPerfTable_Object=MibTable
zxAnEponRmEthCurPerfTable=_ZxAnEponRmEthCurPerfTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3))
if mibBuilder.loadTexts:zxAnEponRmEthCurPerfTable.setStatus(_A)
_ZxAnEponRmEthCurPerfEntry_Object=MibTableRow
zxAnEponRmEthCurPerfEntry=_ZxAnEponRmEthCurPerfEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1))
zxAnEponRmEthCurPerfEntry.setIndexNames((0,_E,_F),(0,_E,_a),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponRmEthCurPerfEntry.setStatus(_A)
_ZxAnEponRmCurDsDropEvents_Type=Counter64
_ZxAnEponRmCurDsDropEvents_Object=MibTableColumn
zxAnEponRmCurDsDropEvents=_ZxAnEponRmCurDsDropEvents_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,1),_ZxAnEponRmCurDsDropEvents_Type())
zxAnEponRmCurDsDropEvents.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurDsDropEvents.setStatus(_A)
_ZxAnEponRmCurDsOctets_Type=Counter64
_ZxAnEponRmCurDsOctets_Object=MibTableColumn
zxAnEponRmCurDsOctets=_ZxAnEponRmCurDsOctets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,2),_ZxAnEponRmCurDsOctets_Type())
zxAnEponRmCurDsOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurDsOctets.setStatus(_A)
_ZxAnEponRmCurDsPkts_Type=Counter64
_ZxAnEponRmCurDsPkts_Object=MibTableColumn
zxAnEponRmCurDsPkts=_ZxAnEponRmCurDsPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,3),_ZxAnEponRmCurDsPkts_Type())
zxAnEponRmCurDsPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurDsPkts.setStatus(_A)
_ZxAnEponRmCurDsBcastPkts_Type=Counter64
_ZxAnEponRmCurDsBcastPkts_Object=MibTableColumn
zxAnEponRmCurDsBcastPkts=_ZxAnEponRmCurDsBcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,4),_ZxAnEponRmCurDsBcastPkts_Type())
zxAnEponRmCurDsBcastPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurDsBcastPkts.setStatus(_A)
_ZxAnEponRmCurDsMcastPkts_Type=Counter64
_ZxAnEponRmCurDsMcastPkts_Object=MibTableColumn
zxAnEponRmCurDsMcastPkts=_ZxAnEponRmCurDsMcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,5),_ZxAnEponRmCurDsMcastPkts_Type())
zxAnEponRmCurDsMcastPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurDsMcastPkts.setStatus(_A)
_ZxAnEponRmCurDsCrcErrPkts_Type=Counter64
_ZxAnEponRmCurDsCrcErrPkts_Object=MibTableColumn
zxAnEponRmCurDsCrcErrPkts=_ZxAnEponRmCurDsCrcErrPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,6),_ZxAnEponRmCurDsCrcErrPkts_Type())
zxAnEponRmCurDsCrcErrPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurDsCrcErrPkts.setStatus(_A)
_ZxAnEponRmCurDsUndersizePkts_Type=Counter64
_ZxAnEponRmCurDsUndersizePkts_Object=MibTableColumn
zxAnEponRmCurDsUndersizePkts=_ZxAnEponRmCurDsUndersizePkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,7),_ZxAnEponRmCurDsUndersizePkts_Type())
zxAnEponRmCurDsUndersizePkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurDsUndersizePkts.setStatus(_A)
_ZxAnEponRmCurDsOversizePkts_Type=Counter64
_ZxAnEponRmCurDsOversizePkts_Object=MibTableColumn
zxAnEponRmCurDsOversizePkts=_ZxAnEponRmCurDsOversizePkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,8),_ZxAnEponRmCurDsOversizePkts_Type())
zxAnEponRmCurDsOversizePkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurDsOversizePkts.setStatus(_A)
_ZxAnEponRmCurDsFragments_Type=Counter64
_ZxAnEponRmCurDsFragments_Object=MibTableColumn
zxAnEponRmCurDsFragments=_ZxAnEponRmCurDsFragments_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,9),_ZxAnEponRmCurDsFragments_Type())
zxAnEponRmCurDsFragments.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurDsFragments.setStatus(_A)
_ZxAnEponRmCurDsJabbers_Type=Counter64
_ZxAnEponRmCurDsJabbers_Object=MibTableColumn
zxAnEponRmCurDsJabbers=_ZxAnEponRmCurDsJabbers_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,10),_ZxAnEponRmCurDsJabbers_Type())
zxAnEponRmCurDsJabbers.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurDsJabbers.setStatus(_A)
_ZxAnEponRmCurDsPkts64Octets_Type=Counter64
_ZxAnEponRmCurDsPkts64Octets_Object=MibTableColumn
zxAnEponRmCurDsPkts64Octets=_ZxAnEponRmCurDsPkts64Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,11),_ZxAnEponRmCurDsPkts64Octets_Type())
zxAnEponRmCurDsPkts64Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurDsPkts64Octets.setStatus(_A)
_ZxAnEponRmCurDs65To127Octets_Type=Counter64
_ZxAnEponRmCurDs65To127Octets_Object=MibTableColumn
zxAnEponRmCurDs65To127Octets=_ZxAnEponRmCurDs65To127Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,12),_ZxAnEponRmCurDs65To127Octets_Type())
zxAnEponRmCurDs65To127Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurDs65To127Octets.setStatus(_A)
_ZxAnEponRmCurDs128To255Octets_Type=Counter64
_ZxAnEponRmCurDs128To255Octets_Object=MibTableColumn
zxAnEponRmCurDs128To255Octets=_ZxAnEponRmCurDs128To255Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,13),_ZxAnEponRmCurDs128To255Octets_Type())
zxAnEponRmCurDs128To255Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurDs128To255Octets.setStatus(_A)
_ZxAnEponRmCurDs256To511Octets_Type=Counter64
_ZxAnEponRmCurDs256To511Octets_Object=MibTableColumn
zxAnEponRmCurDs256To511Octets=_ZxAnEponRmCurDs256To511Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,14),_ZxAnEponRmCurDs256To511Octets_Type())
zxAnEponRmCurDs256To511Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurDs256To511Octets.setStatus(_A)
_ZxAnEponRmCurDs512To1023Octets_Type=Counter64
_ZxAnEponRmCurDs512To1023Octets_Object=MibTableColumn
zxAnEponRmCurDs512To1023Octets=_ZxAnEponRmCurDs512To1023Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,15),_ZxAnEponRmCurDs512To1023Octets_Type())
zxAnEponRmCurDs512To1023Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurDs512To1023Octets.setStatus(_A)
_ZxAnEponRmCurDs1024To1518Octets_Type=Counter64
_ZxAnEponRmCurDs1024To1518Octets_Object=MibTableColumn
zxAnEponRmCurDs1024To1518Octets=_ZxAnEponRmCurDs1024To1518Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,16),_ZxAnEponRmCurDs1024To1518Octets_Type())
zxAnEponRmCurDs1024To1518Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurDs1024To1518Octets.setStatus(_A)
_ZxAnEponRmCurDsDiscards_Type=Counter64
_ZxAnEponRmCurDsDiscards_Object=MibTableColumn
zxAnEponRmCurDsDiscards=_ZxAnEponRmCurDsDiscards_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,17),_ZxAnEponRmCurDsDiscards_Type())
zxAnEponRmCurDsDiscards.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurDsDiscards.setStatus(_A)
_ZxAnEponRmCurDsErrors_Type=Counter64
_ZxAnEponRmCurDsErrors_Object=MibTableColumn
zxAnEponRmCurDsErrors=_ZxAnEponRmCurDsErrors_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,18),_ZxAnEponRmCurDsErrors_Type())
zxAnEponRmCurDsErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurDsErrors.setStatus(_A)
_ZxAnEponRmCurUsDropEvents_Type=Counter64
_ZxAnEponRmCurUsDropEvents_Object=MibTableColumn
zxAnEponRmCurUsDropEvents=_ZxAnEponRmCurUsDropEvents_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,19),_ZxAnEponRmCurUsDropEvents_Type())
zxAnEponRmCurUsDropEvents.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurUsDropEvents.setStatus(_A)
_ZxAnEponRmCurUsOctets_Type=Counter64
_ZxAnEponRmCurUsOctets_Object=MibTableColumn
zxAnEponRmCurUsOctets=_ZxAnEponRmCurUsOctets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,20),_ZxAnEponRmCurUsOctets_Type())
zxAnEponRmCurUsOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurUsOctets.setStatus(_A)
_ZxAnEponRmCurUsPkts_Type=Counter64
_ZxAnEponRmCurUsPkts_Object=MibTableColumn
zxAnEponRmCurUsPkts=_ZxAnEponRmCurUsPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,21),_ZxAnEponRmCurUsPkts_Type())
zxAnEponRmCurUsPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurUsPkts.setStatus(_A)
_ZxAnEponRmCurUsBcastPkts_Type=Counter64
_ZxAnEponRmCurUsBcastPkts_Object=MibTableColumn
zxAnEponRmCurUsBcastPkts=_ZxAnEponRmCurUsBcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,22),_ZxAnEponRmCurUsBcastPkts_Type())
zxAnEponRmCurUsBcastPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurUsBcastPkts.setStatus(_A)
_ZxAnEponRmCurUsMcastPkts_Type=Counter64
_ZxAnEponRmCurUsMcastPkts_Object=MibTableColumn
zxAnEponRmCurUsMcastPkts=_ZxAnEponRmCurUsMcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,23),_ZxAnEponRmCurUsMcastPkts_Type())
zxAnEponRmCurUsMcastPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurUsMcastPkts.setStatus(_A)
_ZxAnEponRmCurUsCrcErrPkts_Type=Counter64
_ZxAnEponRmCurUsCrcErrPkts_Object=MibTableColumn
zxAnEponRmCurUsCrcErrPkts=_ZxAnEponRmCurUsCrcErrPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,24),_ZxAnEponRmCurUsCrcErrPkts_Type())
zxAnEponRmCurUsCrcErrPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurUsCrcErrPkts.setStatus(_A)
_ZxAnEponRmCurUsUndersizePkts_Type=Counter64
_ZxAnEponRmCurUsUndersizePkts_Object=MibTableColumn
zxAnEponRmCurUsUndersizePkts=_ZxAnEponRmCurUsUndersizePkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,25),_ZxAnEponRmCurUsUndersizePkts_Type())
zxAnEponRmCurUsUndersizePkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurUsUndersizePkts.setStatus(_A)
_ZxAnEponRmCurUsOversizePkts_Type=Counter64
_ZxAnEponRmCurUsOversizePkts_Object=MibTableColumn
zxAnEponRmCurUsOversizePkts=_ZxAnEponRmCurUsOversizePkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,26),_ZxAnEponRmCurUsOversizePkts_Type())
zxAnEponRmCurUsOversizePkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurUsOversizePkts.setStatus(_A)
_ZxAnEponRmCurUsFragments_Type=Counter64
_ZxAnEponRmCurUsFragments_Object=MibTableColumn
zxAnEponRmCurUsFragments=_ZxAnEponRmCurUsFragments_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,27),_ZxAnEponRmCurUsFragments_Type())
zxAnEponRmCurUsFragments.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurUsFragments.setStatus(_A)
_ZxAnEponRmCurUsJabbers_Type=Counter64
_ZxAnEponRmCurUsJabbers_Object=MibTableColumn
zxAnEponRmCurUsJabbers=_ZxAnEponRmCurUsJabbers_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,28),_ZxAnEponRmCurUsJabbers_Type())
zxAnEponRmCurUsJabbers.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurUsJabbers.setStatus(_A)
_ZxAnEponRmCurUsPkts64Octets_Type=Counter64
_ZxAnEponRmCurUsPkts64Octets_Object=MibTableColumn
zxAnEponRmCurUsPkts64Octets=_ZxAnEponRmCurUsPkts64Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,29),_ZxAnEponRmCurUsPkts64Octets_Type())
zxAnEponRmCurUsPkts64Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurUsPkts64Octets.setStatus(_A)
_ZxAnEponRmCurUs65To127Octets_Type=Counter64
_ZxAnEponRmCurUs65To127Octets_Object=MibTableColumn
zxAnEponRmCurUs65To127Octets=_ZxAnEponRmCurUs65To127Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,30),_ZxAnEponRmCurUs65To127Octets_Type())
zxAnEponRmCurUs65To127Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurUs65To127Octets.setStatus(_A)
_ZxAnEponRmCurUs128To255Octets_Type=Counter64
_ZxAnEponRmCurUs128To255Octets_Object=MibTableColumn
zxAnEponRmCurUs128To255Octets=_ZxAnEponRmCurUs128To255Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,31),_ZxAnEponRmCurUs128To255Octets_Type())
zxAnEponRmCurUs128To255Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurUs128To255Octets.setStatus(_A)
_ZxAnEponRmCurUs256To511Octets_Type=Counter64
_ZxAnEponRmCurUs256To511Octets_Object=MibTableColumn
zxAnEponRmCurUs256To511Octets=_ZxAnEponRmCurUs256To511Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,32),_ZxAnEponRmCurUs256To511Octets_Type())
zxAnEponRmCurUs256To511Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurUs256To511Octets.setStatus(_A)
_ZxAnEponRmCurUs512To1023Octets_Type=Counter64
_ZxAnEponRmCurUs512To1023Octets_Object=MibTableColumn
zxAnEponRmCurUs512To1023Octets=_ZxAnEponRmCurUs512To1023Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,33),_ZxAnEponRmCurUs512To1023Octets_Type())
zxAnEponRmCurUs512To1023Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurUs512To1023Octets.setStatus(_A)
_ZxAnEponRmCurUs1024To1518Octets_Type=Counter64
_ZxAnEponRmCurUs1024To1518Octets_Object=MibTableColumn
zxAnEponRmCurUs1024To1518Octets=_ZxAnEponRmCurUs1024To1518Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,34),_ZxAnEponRmCurUs1024To1518Octets_Type())
zxAnEponRmCurUs1024To1518Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurUs1024To1518Octets.setStatus(_A)
_ZxAnEponRmCurUsDiscards_Type=Counter64
_ZxAnEponRmCurUsDiscards_Object=MibTableColumn
zxAnEponRmCurUsDiscards=_ZxAnEponRmCurUsDiscards_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,35),_ZxAnEponRmCurUsDiscards_Type())
zxAnEponRmCurUsDiscards.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurUsDiscards.setStatus(_A)
_ZxAnEponRmCurUsErrors_Type=Counter64
_ZxAnEponRmCurUsErrors_Object=MibTableColumn
zxAnEponRmCurUsErrors=_ZxAnEponRmCurUsErrors_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,36),_ZxAnEponRmCurUsErrors_Type())
zxAnEponRmCurUsErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurUsErrors.setStatus(_A)
_ZxAnEponRmCurPortStatusChanges_Type=Counter64
_ZxAnEponRmCurPortStatusChanges_Object=MibTableColumn
zxAnEponRmCurPortStatusChanges=_ZxAnEponRmCurPortStatusChanges_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,3,1,37),_ZxAnEponRmCurPortStatusChanges_Type())
zxAnEponRmCurPortStatusChanges.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmCurPortStatusChanges.setStatus(_A)
_ZxAnEponRmEthHisPerfTable_Object=MibTable
zxAnEponRmEthHisPerfTable=_ZxAnEponRmEthHisPerfTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4))
if mibBuilder.loadTexts:zxAnEponRmEthHisPerfTable.setStatus(_A)
_ZxAnEponRmEthHisPerfEntry_Object=MibTableRow
zxAnEponRmEthHisPerfEntry=_ZxAnEponRmEthHisPerfEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1))
zxAnEponRmEthHisPerfEntry.setIndexNames((0,_E,_F),(0,_E,_a),(0,_E,_H),(0,_E,_Ay))
if mibBuilder.loadTexts:zxAnEponRmEthHisPerfEntry.setStatus(_A)
class _ZxAnEponRmEthHisIntervalNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_ZxAnEponRmEthHisIntervalNo_Type.__name__=_B
_ZxAnEponRmEthHisIntervalNo_Object=MibTableColumn
zxAnEponRmEthHisIntervalNo=_ZxAnEponRmEthHisIntervalNo_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,1),_ZxAnEponRmEthHisIntervalNo_Type())
zxAnEponRmEthHisIntervalNo.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponRmEthHisIntervalNo.setStatus(_A)
_ZxAnEponRmHisDsDropEvents_Type=Counter64
_ZxAnEponRmHisDsDropEvents_Object=MibTableColumn
zxAnEponRmHisDsDropEvents=_ZxAnEponRmHisDsDropEvents_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,2),_ZxAnEponRmHisDsDropEvents_Type())
zxAnEponRmHisDsDropEvents.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisDsDropEvents.setStatus(_A)
_ZxAnEponRmHisDsOctets_Type=Counter64
_ZxAnEponRmHisDsOctets_Object=MibTableColumn
zxAnEponRmHisDsOctets=_ZxAnEponRmHisDsOctets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,3),_ZxAnEponRmHisDsOctets_Type())
zxAnEponRmHisDsOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisDsOctets.setStatus(_A)
_ZxAnEponRmHisDsPkts_Type=Counter64
_ZxAnEponRmHisDsPkts_Object=MibTableColumn
zxAnEponRmHisDsPkts=_ZxAnEponRmHisDsPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,4),_ZxAnEponRmHisDsPkts_Type())
zxAnEponRmHisDsPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisDsPkts.setStatus(_A)
_ZxAnEponRmHisDsBcastPkts_Type=Counter64
_ZxAnEponRmHisDsBcastPkts_Object=MibTableColumn
zxAnEponRmHisDsBcastPkts=_ZxAnEponRmHisDsBcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,5),_ZxAnEponRmHisDsBcastPkts_Type())
zxAnEponRmHisDsBcastPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisDsBcastPkts.setStatus(_A)
_ZxAnEponRmHisDsMcastPkts_Type=Counter64
_ZxAnEponRmHisDsMcastPkts_Object=MibTableColumn
zxAnEponRmHisDsMcastPkts=_ZxAnEponRmHisDsMcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,6),_ZxAnEponRmHisDsMcastPkts_Type())
zxAnEponRmHisDsMcastPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisDsMcastPkts.setStatus(_A)
_ZxAnEponRmHisDsCrcErrPkts_Type=Counter64
_ZxAnEponRmHisDsCrcErrPkts_Object=MibTableColumn
zxAnEponRmHisDsCrcErrPkts=_ZxAnEponRmHisDsCrcErrPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,7),_ZxAnEponRmHisDsCrcErrPkts_Type())
zxAnEponRmHisDsCrcErrPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisDsCrcErrPkts.setStatus(_A)
_ZxAnEponRmHisDsUndersizePkts_Type=Counter64
_ZxAnEponRmHisDsUndersizePkts_Object=MibTableColumn
zxAnEponRmHisDsUndersizePkts=_ZxAnEponRmHisDsUndersizePkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,8),_ZxAnEponRmHisDsUndersizePkts_Type())
zxAnEponRmHisDsUndersizePkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisDsUndersizePkts.setStatus(_A)
_ZxAnEponRmHisDsOversizePkts_Type=Counter64
_ZxAnEponRmHisDsOversizePkts_Object=MibTableColumn
zxAnEponRmHisDsOversizePkts=_ZxAnEponRmHisDsOversizePkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,9),_ZxAnEponRmHisDsOversizePkts_Type())
zxAnEponRmHisDsOversizePkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisDsOversizePkts.setStatus(_A)
_ZxAnEponRmHisDsFragments_Type=Counter64
_ZxAnEponRmHisDsFragments_Object=MibTableColumn
zxAnEponRmHisDsFragments=_ZxAnEponRmHisDsFragments_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,10),_ZxAnEponRmHisDsFragments_Type())
zxAnEponRmHisDsFragments.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisDsFragments.setStatus(_A)
_ZxAnEponRmHisDsJabbers_Type=Counter64
_ZxAnEponRmHisDsJabbers_Object=MibTableColumn
zxAnEponRmHisDsJabbers=_ZxAnEponRmHisDsJabbers_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,11),_ZxAnEponRmHisDsJabbers_Type())
zxAnEponRmHisDsJabbers.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisDsJabbers.setStatus(_A)
_ZxAnEponRmHisDsPkts64Octets_Type=Counter64
_ZxAnEponRmHisDsPkts64Octets_Object=MibTableColumn
zxAnEponRmHisDsPkts64Octets=_ZxAnEponRmHisDsPkts64Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,12),_ZxAnEponRmHisDsPkts64Octets_Type())
zxAnEponRmHisDsPkts64Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisDsPkts64Octets.setStatus(_A)
_ZxAnEponRmHisDs65To127Octets_Type=Counter64
_ZxAnEponRmHisDs65To127Octets_Object=MibTableColumn
zxAnEponRmHisDs65To127Octets=_ZxAnEponRmHisDs65To127Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,13),_ZxAnEponRmHisDs65To127Octets_Type())
zxAnEponRmHisDs65To127Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisDs65To127Octets.setStatus(_A)
_ZxAnEponRmHisDs128To255Octets_Type=Counter64
_ZxAnEponRmHisDs128To255Octets_Object=MibTableColumn
zxAnEponRmHisDs128To255Octets=_ZxAnEponRmHisDs128To255Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,14),_ZxAnEponRmHisDs128To255Octets_Type())
zxAnEponRmHisDs128To255Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisDs128To255Octets.setStatus(_A)
_ZxAnEponRmHisDs256To511Octets_Type=Counter64
_ZxAnEponRmHisDs256To511Octets_Object=MibTableColumn
zxAnEponRmHisDs256To511Octets=_ZxAnEponRmHisDs256To511Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,15),_ZxAnEponRmHisDs256To511Octets_Type())
zxAnEponRmHisDs256To511Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisDs256To511Octets.setStatus(_A)
_ZxAnEponRmHisDs512To1023Octets_Type=Counter64
_ZxAnEponRmHisDs512To1023Octets_Object=MibTableColumn
zxAnEponRmHisDs512To1023Octets=_ZxAnEponRmHisDs512To1023Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,16),_ZxAnEponRmHisDs512To1023Octets_Type())
zxAnEponRmHisDs512To1023Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisDs512To1023Octets.setStatus(_A)
_ZxAnEponRmHisDs1024To1518Octets_Type=Counter64
_ZxAnEponRmHisDs1024To1518Octets_Object=MibTableColumn
zxAnEponRmHisDs1024To1518Octets=_ZxAnEponRmHisDs1024To1518Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,17),_ZxAnEponRmHisDs1024To1518Octets_Type())
zxAnEponRmHisDs1024To1518Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisDs1024To1518Octets.setStatus(_A)
_ZxAnEponRmHisDsDiscards_Type=Counter64
_ZxAnEponRmHisDsDiscards_Object=MibTableColumn
zxAnEponRmHisDsDiscards=_ZxAnEponRmHisDsDiscards_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,18),_ZxAnEponRmHisDsDiscards_Type())
zxAnEponRmHisDsDiscards.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisDsDiscards.setStatus(_A)
_ZxAnEponRmHisDsErrors_Type=Counter64
_ZxAnEponRmHisDsErrors_Object=MibTableColumn
zxAnEponRmHisDsErrors=_ZxAnEponRmHisDsErrors_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,19),_ZxAnEponRmHisDsErrors_Type())
zxAnEponRmHisDsErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisDsErrors.setStatus(_A)
_ZxAnEponRmHisUsDropEvents_Type=Counter64
_ZxAnEponRmHisUsDropEvents_Object=MibTableColumn
zxAnEponRmHisUsDropEvents=_ZxAnEponRmHisUsDropEvents_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,20),_ZxAnEponRmHisUsDropEvents_Type())
zxAnEponRmHisUsDropEvents.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisUsDropEvents.setStatus(_A)
_ZxAnEponRmHisUsOctets_Type=Counter64
_ZxAnEponRmHisUsOctets_Object=MibTableColumn
zxAnEponRmHisUsOctets=_ZxAnEponRmHisUsOctets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,21),_ZxAnEponRmHisUsOctets_Type())
zxAnEponRmHisUsOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisUsOctets.setStatus(_A)
_ZxAnEponRmHisUsPkts_Type=Counter64
_ZxAnEponRmHisUsPkts_Object=MibTableColumn
zxAnEponRmHisUsPkts=_ZxAnEponRmHisUsPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,22),_ZxAnEponRmHisUsPkts_Type())
zxAnEponRmHisUsPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisUsPkts.setStatus(_A)
_ZxAnEponRmHisUsBcastPkts_Type=Counter64
_ZxAnEponRmHisUsBcastPkts_Object=MibTableColumn
zxAnEponRmHisUsBcastPkts=_ZxAnEponRmHisUsBcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,23),_ZxAnEponRmHisUsBcastPkts_Type())
zxAnEponRmHisUsBcastPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisUsBcastPkts.setStatus(_A)
_ZxAnEponRmHisUsMcastPkts_Type=Counter64
_ZxAnEponRmHisUsMcastPkts_Object=MibTableColumn
zxAnEponRmHisUsMcastPkts=_ZxAnEponRmHisUsMcastPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,24),_ZxAnEponRmHisUsMcastPkts_Type())
zxAnEponRmHisUsMcastPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisUsMcastPkts.setStatus(_A)
_ZxAnEponRmHisUsCrcErrPkts_Type=Counter64
_ZxAnEponRmHisUsCrcErrPkts_Object=MibTableColumn
zxAnEponRmHisUsCrcErrPkts=_ZxAnEponRmHisUsCrcErrPkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,25),_ZxAnEponRmHisUsCrcErrPkts_Type())
zxAnEponRmHisUsCrcErrPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisUsCrcErrPkts.setStatus(_A)
_ZxAnEponRmHisUsUndersizePkts_Type=Counter64
_ZxAnEponRmHisUsUndersizePkts_Object=MibTableColumn
zxAnEponRmHisUsUndersizePkts=_ZxAnEponRmHisUsUndersizePkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,26),_ZxAnEponRmHisUsUndersizePkts_Type())
zxAnEponRmHisUsUndersizePkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisUsUndersizePkts.setStatus(_A)
_ZxAnEponRmHisUsOversizePkts_Type=Counter64
_ZxAnEponRmHisUsOversizePkts_Object=MibTableColumn
zxAnEponRmHisUsOversizePkts=_ZxAnEponRmHisUsOversizePkts_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,27),_ZxAnEponRmHisUsOversizePkts_Type())
zxAnEponRmHisUsOversizePkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisUsOversizePkts.setStatus(_A)
_ZxAnEponRmHisUsFragments_Type=Counter64
_ZxAnEponRmHisUsFragments_Object=MibTableColumn
zxAnEponRmHisUsFragments=_ZxAnEponRmHisUsFragments_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,28),_ZxAnEponRmHisUsFragments_Type())
zxAnEponRmHisUsFragments.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisUsFragments.setStatus(_A)
_ZxAnEponRmHisUsJabbers_Type=Counter64
_ZxAnEponRmHisUsJabbers_Object=MibTableColumn
zxAnEponRmHisUsJabbers=_ZxAnEponRmHisUsJabbers_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,29),_ZxAnEponRmHisUsJabbers_Type())
zxAnEponRmHisUsJabbers.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisUsJabbers.setStatus(_A)
_ZxAnEponRmHisUsPkts64Octets_Type=Counter64
_ZxAnEponRmHisUsPkts64Octets_Object=MibTableColumn
zxAnEponRmHisUsPkts64Octets=_ZxAnEponRmHisUsPkts64Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,30),_ZxAnEponRmHisUsPkts64Octets_Type())
zxAnEponRmHisUsPkts64Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisUsPkts64Octets.setStatus(_A)
_ZxAnEponRmHisUs65To127Octets_Type=Counter64
_ZxAnEponRmHisUs65To127Octets_Object=MibTableColumn
zxAnEponRmHisUs65To127Octets=_ZxAnEponRmHisUs65To127Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,31),_ZxAnEponRmHisUs65To127Octets_Type())
zxAnEponRmHisUs65To127Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisUs65To127Octets.setStatus(_A)
_ZxAnEponRmHisUs128To255Octets_Type=Counter64
_ZxAnEponRmHisUs128To255Octets_Object=MibTableColumn
zxAnEponRmHisUs128To255Octets=_ZxAnEponRmHisUs128To255Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,32),_ZxAnEponRmHisUs128To255Octets_Type())
zxAnEponRmHisUs128To255Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisUs128To255Octets.setStatus(_A)
_ZxAnEponRmHisUs256To511Octets_Type=Counter64
_ZxAnEponRmHisUs256To511Octets_Object=MibTableColumn
zxAnEponRmHisUs256To511Octets=_ZxAnEponRmHisUs256To511Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,33),_ZxAnEponRmHisUs256To511Octets_Type())
zxAnEponRmHisUs256To511Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisUs256To511Octets.setStatus(_A)
_ZxAnEponRmHisUs512To1023Octets_Type=Counter64
_ZxAnEponRmHisUs512To1023Octets_Object=MibTableColumn
zxAnEponRmHisUs512To1023Octets=_ZxAnEponRmHisUs512To1023Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,34),_ZxAnEponRmHisUs512To1023Octets_Type())
zxAnEponRmHisUs512To1023Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisUs512To1023Octets.setStatus(_A)
_ZxAnEponRmHisUs1024To1518Octets_Type=Counter64
_ZxAnEponRmHisUs1024To1518Octets_Object=MibTableColumn
zxAnEponRmHisUs1024To1518Octets=_ZxAnEponRmHisUs1024To1518Octets_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,35),_ZxAnEponRmHisUs1024To1518Octets_Type())
zxAnEponRmHisUs1024To1518Octets.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisUs1024To1518Octets.setStatus(_A)
_ZxAnEponRmHisUsDiscards_Type=Counter64
_ZxAnEponRmHisUsDiscards_Object=MibTableColumn
zxAnEponRmHisUsDiscards=_ZxAnEponRmHisUsDiscards_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,36),_ZxAnEponRmHisUsDiscards_Type())
zxAnEponRmHisUsDiscards.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisUsDiscards.setStatus(_A)
_ZxAnEponRmHisUsErrors_Type=Counter64
_ZxAnEponRmHisUsErrors_Object=MibTableColumn
zxAnEponRmHisUsErrors=_ZxAnEponRmHisUsErrors_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,37),_ZxAnEponRmHisUsErrors_Type())
zxAnEponRmHisUsErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisUsErrors.setStatus(_A)
_ZxAnEponRmHisPortStatusChanges_Type=Counter64
_ZxAnEponRmHisPortStatusChanges_Object=MibTableColumn
zxAnEponRmHisPortStatusChanges=_ZxAnEponRmHisPortStatusChanges_Object((1,3,6,1,4,1,3902,1015,1010,1,1,7,4,1,38),_ZxAnEponRmHisPortStatusChanges_Type())
zxAnEponRmHisPortStatusChanges.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponRmHisPortStatusChanges.setStatus(_A)
_ZxAnPtpExtOamMgmt_ObjectIdentity=ObjectIdentity
zxAnPtpExtOamMgmt=_ZxAnPtpExtOamMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,8))
_ZxAnPtpExtOamTable_Object=MibTable
zxAnPtpExtOamTable=_ZxAnPtpExtOamTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,8,2))
if mibBuilder.loadTexts:zxAnPtpExtOamTable.setStatus(_A)
_ZxAnPtpExtOamEntry_Object=MibTableRow
zxAnPtpExtOamEntry=_ZxAnPtpExtOamEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,8,2,1))
zxAnPtpExtOamEntry.setIndexNames((0,_E,_Az))
if mibBuilder.loadTexts:zxAnPtpExtOamEntry.setStatus(_A)
_ZxAnPtpIfIndex_Type=Integer32
_ZxAnPtpIfIndex_Object=MibTableColumn
zxAnPtpIfIndex=_ZxAnPtpIfIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,1,8,2,1,1),_ZxAnPtpIfIndex_Type())
zxAnPtpIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnPtpIfIndex.setStatus(_A)
class _ZxAnPtpExtOamAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_ZxAnPtpExtOamAdminStatus_Type.__name__=_B
_ZxAnPtpExtOamAdminStatus_Object=MibTableColumn
zxAnPtpExtOamAdminStatus=_ZxAnPtpExtOamAdminStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,8,2,1,2),_ZxAnPtpExtOamAdminStatus_Type())
zxAnPtpExtOamAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPtpExtOamAdminStatus.setStatus(_A)
_ZxAnEponOnuCustomMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuCustomMgmt=_ZxAnEponOnuCustomMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,101))
_ZxAnEponOnuTkMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuTkMgmt=_ZxAnEponOnuTkMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,101,31))
_ZxAnEponOnuTkAttrMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuTkAttrMgmt=_ZxAnEponOnuTkAttrMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31))
_ZxAnEponOnuTkGlobalTable_Object=MibTable
zxAnEponOnuTkGlobalTable=_ZxAnEponOnuTkGlobalTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,31))
if mibBuilder.loadTexts:zxAnEponOnuTkGlobalTable.setStatus(_A)
_ZxAnEponOnuTkGlobalEntry_Object=MibTableRow
zxAnEponOnuTkGlobalEntry=_ZxAnEponOnuTkGlobalEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,31,1))
zxAnEponOnuTkGlobalEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuTkGlobalEntry.setStatus(_A)
_ZxAnEponOnuTkFirmwareVer_Type=DisplayString
_ZxAnEponOnuTkFirmwareVer_Object=MibTableColumn
zxAnEponOnuTkFirmwareVer=_ZxAnEponOnuTkFirmwareVer_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,31,1,1),_ZxAnEponOnuTkFirmwareVer_Type())
zxAnEponOnuTkFirmwareVer.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkFirmwareVer.setStatus(_A)
_ZxAnEponOnuTkModeName_Type=DisplayString
_ZxAnEponOnuTkModeName_Object=MibTableColumn
zxAnEponOnuTkModeName=_ZxAnEponOnuTkModeName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,31,1,2),_ZxAnEponOnuTkModeName_Type())
zxAnEponOnuTkModeName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkModeName.setStatus(_A)
_ZxAnEponOnuTkPortTable_Object=MibTable
zxAnEponOnuTkPortTable=_ZxAnEponOnuTkPortTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,32))
if mibBuilder.loadTexts:zxAnEponOnuTkPortTable.setStatus(_A)
_ZxAnEponOnuTkPortEntry_Object=MibTableRow
zxAnEponOnuTkPortEntry=_ZxAnEponOnuTkPortEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,32,1))
zxAnEponOnuTkPortEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuTkPortEntry.setStatus(_A)
class _ZxAnEponOnuTkPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuTkPortOperStatus_Type.__name__=_B
_ZxAnEponOnuTkPortOperStatus_Object=MibTableColumn
zxAnEponOnuTkPortOperStatus=_ZxAnEponOnuTkPortOperStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,32,1,1),_ZxAnEponOnuTkPortOperStatus_Type())
zxAnEponOnuTkPortOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkPortOperStatus.setStatus(_A)
class _ZxAnEponOnuTkPortAutoNegStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuTkPortAutoNegStatus_Type.__name__=_B
_ZxAnEponOnuTkPortAutoNegStatus_Object=MibTableColumn
zxAnEponOnuTkPortAutoNegStatus=_ZxAnEponOnuTkPortAutoNegStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,32,1,2),_ZxAnEponOnuTkPortAutoNegStatus_Type())
zxAnEponOnuTkPortAutoNegStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkPortAutoNegStatus.setStatus(_A)
class _ZxAnEponOnuTkPortFlowCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuTkPortFlowCtrlStatus_Type.__name__=_B
_ZxAnEponOnuTkPortFlowCtrlStatus_Object=MibTableColumn
zxAnEponOnuTkPortFlowCtrlStatus=_ZxAnEponOnuTkPortFlowCtrlStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,32,1,3),_ZxAnEponOnuTkPortFlowCtrlStatus_Type())
zxAnEponOnuTkPortFlowCtrlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkPortFlowCtrlStatus.setStatus(_A)
class _ZxAnEponOnuTkPortDuplexMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('half',1),('full',2)))
_ZxAnEponOnuTkPortDuplexMode_Type.__name__=_B
_ZxAnEponOnuTkPortDuplexMode_Object=MibTableColumn
zxAnEponOnuTkPortDuplexMode=_ZxAnEponOnuTkPortDuplexMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,32,1,4),_ZxAnEponOnuTkPortDuplexMode_Type())
zxAnEponOnuTkPortDuplexMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkPortDuplexMode.setStatus(_A)
class _ZxAnEponOnuTkPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuTkPortAdminStatus_Type.__name__=_B
_ZxAnEponOnuTkPortAdminStatus_Object=MibTableColumn
zxAnEponOnuTkPortAdminStatus=_ZxAnEponOnuTkPortAdminStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,32,1,5),_ZxAnEponOnuTkPortAdminStatus_Type())
zxAnEponOnuTkPortAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkPortAdminStatus.setStatus(_A)
_ZxAnEponOnuTkLoopbackTable_Object=MibTable
zxAnEponOnuTkLoopbackTable=_ZxAnEponOnuTkLoopbackTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,33))
if mibBuilder.loadTexts:zxAnEponOnuTkLoopbackTable.setStatus(_A)
_ZxAnEponOnuTkLoopbackEntry_Object=MibTableRow
zxAnEponOnuTkLoopbackEntry=_ZxAnEponOnuTkLoopbackEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,33,1))
zxAnEponOnuTkLoopbackEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuTkLoopbackEntry.setStatus(_A)
class _ZxAnEponOnuTkLoopbackAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuTkLoopbackAdminStatus_Type.__name__=_B
_ZxAnEponOnuTkLoopbackAdminStatus_Object=MibTableColumn
zxAnEponOnuTkLoopbackAdminStatus=_ZxAnEponOnuTkLoopbackAdminStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,33,1,1),_ZxAnEponOnuTkLoopbackAdminStatus_Type())
zxAnEponOnuTkLoopbackAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkLoopbackAdminStatus.setStatus(_A)
_ZxAnEponOnuTkLinkBlockTable_Object=MibTable
zxAnEponOnuTkLinkBlockTable=_ZxAnEponOnuTkLinkBlockTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,34))
if mibBuilder.loadTexts:zxAnEponOnuTkLinkBlockTable.setStatus(_A)
_ZxAnEponOnuTkLinkBlockEntry_Object=MibTableRow
zxAnEponOnuTkLinkBlockEntry=_ZxAnEponOnuTkLinkBlockEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,34,1))
zxAnEponOnuTkLinkBlockEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuTkLinkBlockEntry.setStatus(_A)
class _ZxAnEponOnuTkLinkBlockAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuTkLinkBlockAdminStatus_Type.__name__=_B
_ZxAnEponOnuTkLinkBlockAdminStatus_Object=MibTableColumn
zxAnEponOnuTkLinkBlockAdminStatus=_ZxAnEponOnuTkLinkBlockAdminStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,34,1,1),_ZxAnEponOnuTkLinkBlockAdminStatus_Type())
zxAnEponOnuTkLinkBlockAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkLinkBlockAdminStatus.setStatus(_A)
class _ZxAnEponOnuTkLinkBlockOamType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_ZxAnEponOnuTkLinkBlockOamType_Type.__name__=_B
_ZxAnEponOnuTkLinkBlockOamType_Object=MibTableColumn
zxAnEponOnuTkLinkBlockOamType=_ZxAnEponOnuTkLinkBlockOamType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,34,1,2),_ZxAnEponOnuTkLinkBlockOamType_Type())
zxAnEponOnuTkLinkBlockOamType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkLinkBlockOamType.setStatus(_A)
_ZxAnEponOnuTkOpticalCtrlTable_Object=MibTable
zxAnEponOnuTkOpticalCtrlTable=_ZxAnEponOnuTkOpticalCtrlTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,35))
if mibBuilder.loadTexts:zxAnEponOnuTkOpticalCtrlTable.setStatus(_A)
_ZxAnEponOnuTkOpticalCtrlEntry_Object=MibTableRow
zxAnEponOnuTkOpticalCtrlEntry=_ZxAnEponOnuTkOpticalCtrlEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,35,1))
zxAnEponOnuTkOpticalCtrlEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuTkOpticalCtrlEntry.setStatus(_A)
class _ZxAnEponOnuTkOpticalBlockStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuTkOpticalBlockStatus_Type.__name__=_B
_ZxAnEponOnuTkOpticalBlockStatus_Object=MibTableColumn
zxAnEponOnuTkOpticalBlockStatus=_ZxAnEponOnuTkOpticalBlockStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,35,1,1),_ZxAnEponOnuTkOpticalBlockStatus_Type())
zxAnEponOnuTkOpticalBlockStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkOpticalBlockStatus.setStatus(_A)
class _ZxAnEponOnuTkOpticalBlockDurationTime_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ZxAnEponOnuTkOpticalBlockDurationTime_Type.__name__=_B
_ZxAnEponOnuTkOpticalBlockDurationTime_Object=MibTableColumn
zxAnEponOnuTkOpticalBlockDurationTime=_ZxAnEponOnuTkOpticalBlockDurationTime_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,35,1,2),_ZxAnEponOnuTkOpticalBlockDurationTime_Type())
zxAnEponOnuTkOpticalBlockDurationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkOpticalBlockDurationTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponOnuTkOpticalBlockDurationTime.setUnits('second')
class _ZxAnEponOnuTkOpticalBlockOamType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_ZxAnEponOnuTkOpticalBlockOamType_Type.__name__=_B
_ZxAnEponOnuTkOpticalBlockOamType_Object=MibTableColumn
zxAnEponOnuTkOpticalBlockOamType=_ZxAnEponOnuTkOpticalBlockOamType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,35,1,3),_ZxAnEponOnuTkOpticalBlockOamType_Type())
zxAnEponOnuTkOpticalBlockOamType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkOpticalBlockOamType.setStatus(_A)
_ZxAnEponOnuTkRstpCtrlTable_Object=MibTable
zxAnEponOnuTkRstpCtrlTable=_ZxAnEponOnuTkRstpCtrlTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,36))
if mibBuilder.loadTexts:zxAnEponOnuTkRstpCtrlTable.setStatus(_A)
_ZxAnEponOnuTkRstpCtrlEntry_Object=MibTableRow
zxAnEponOnuTkRstpCtrlEntry=_ZxAnEponOnuTkRstpCtrlEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,36,1))
zxAnEponOnuTkRstpCtrlEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuTkRstpCtrlEntry.setStatus(_A)
class _ZxAnEponOnuTkRstpAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_J,2),('passthrough',3)))
_ZxAnEponOnuTkRstpAdminStatus_Type.__name__=_B
_ZxAnEponOnuTkRstpAdminStatus_Object=MibTableColumn
zxAnEponOnuTkRstpAdminStatus=_ZxAnEponOnuTkRstpAdminStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,36,1,1),_ZxAnEponOnuTkRstpAdminStatus_Type())
zxAnEponOnuTkRstpAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkRstpAdminStatus.setStatus(_A)
_ZxAnEponOnuTkMacLearningTable_Object=MibTable
zxAnEponOnuTkMacLearningTable=_ZxAnEponOnuTkMacLearningTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,37))
if mibBuilder.loadTexts:zxAnEponOnuTkMacLearningTable.setStatus(_A)
_ZxAnEponOnuTkMacLearningEntry_Object=MibTableRow
zxAnEponOnuTkMacLearningEntry=_ZxAnEponOnuTkMacLearningEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,37,1))
zxAnEponOnuTkMacLearningEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuTkMacLearningEntry.setStatus(_A)
class _ZxAnEponOnuTkMacLearningMaxNum_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_ZxAnEponOnuTkMacLearningMaxNum_Type.__name__=_B
_ZxAnEponOnuTkMacLearningMaxNum_Object=MibTableColumn
zxAnEponOnuTkMacLearningMaxNum=_ZxAnEponOnuTkMacLearningMaxNum_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,37,1,1),_ZxAnEponOnuTkMacLearningMaxNum_Type())
zxAnEponOnuTkMacLearningMaxNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkMacLearningMaxNum.setStatus(_A)
class _ZxAnEponOnuTkMacLearningOamType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_ZxAnEponOnuTkMacLearningOamType_Type.__name__=_B
_ZxAnEponOnuTkMacLearningOamType_Object=MibTableColumn
zxAnEponOnuTkMacLearningOamType=_ZxAnEponOnuTkMacLearningOamType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,37,1,2),_ZxAnEponOnuTkMacLearningOamType_Type())
zxAnEponOnuTkMacLearningOamType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkMacLearningOamType.setStatus(_A)
_ZxAnEponOnuTkSnoopingTable_Object=MibTable
zxAnEponOnuTkSnoopingTable=_ZxAnEponOnuTkSnoopingTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,38))
if mibBuilder.loadTexts:zxAnEponOnuTkSnoopingTable.setStatus(_A)
_ZxAnEponOnuTkSnoopingEntry_Object=MibTableRow
zxAnEponOnuTkSnoopingEntry=_ZxAnEponOnuTkSnoopingEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,38,1))
zxAnEponOnuTkSnoopingEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuTkSnoopingEntry.setStatus(_A)
class _ZxAnEponOnuTkSnoopingCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuTkSnoopingCtrl_Type.__name__=_B
_ZxAnEponOnuTkSnoopingCtrl_Object=MibTableColumn
zxAnEponOnuTkSnoopingCtrl=_ZxAnEponOnuTkSnoopingCtrl_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,38,1,1),_ZxAnEponOnuTkSnoopingCtrl_Type())
zxAnEponOnuTkSnoopingCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkSnoopingCtrl.setStatus(_A)
class _ZxAnEponOnuTkSnoopingRobustCnt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_ZxAnEponOnuTkSnoopingRobustCnt_Type.__name__=_B
_ZxAnEponOnuTkSnoopingRobustCnt_Object=MibTableColumn
zxAnEponOnuTkSnoopingRobustCnt=_ZxAnEponOnuTkSnoopingRobustCnt_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,38,1,2),_ZxAnEponOnuTkSnoopingRobustCnt_Type())
zxAnEponOnuTkSnoopingRobustCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkSnoopingRobustCnt.setStatus(_A)
class _ZxAnEponOnuTkSnoopingLsmq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_ZxAnEponOnuTkSnoopingLsmq_Type.__name__=_B
_ZxAnEponOnuTkSnoopingLsmq_Object=MibTableColumn
zxAnEponOnuTkSnoopingLsmq=_ZxAnEponOnuTkSnoopingLsmq_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,38,1,3),_ZxAnEponOnuTkSnoopingLsmq_Type())
zxAnEponOnuTkSnoopingLsmq.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkSnoopingLsmq.setStatus(_A)
class _ZxAnEponOnuTkSnoopingMaxGroupNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_ZxAnEponOnuTkSnoopingMaxGroupNum_Type.__name__=_B
_ZxAnEponOnuTkSnoopingMaxGroupNum_Object=MibTableColumn
zxAnEponOnuTkSnoopingMaxGroupNum=_ZxAnEponOnuTkSnoopingMaxGroupNum_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,38,1,4),_ZxAnEponOnuTkSnoopingMaxGroupNum_Type())
zxAnEponOnuTkSnoopingMaxGroupNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkSnoopingMaxGroupNum.setStatus(_A)
_ZxAnEponOnuTkIgmpTable_Object=MibTable
zxAnEponOnuTkIgmpTable=_ZxAnEponOnuTkIgmpTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,39))
if mibBuilder.loadTexts:zxAnEponOnuTkIgmpTable.setStatus(_A)
_ZxAnEponOnuTkIgmpEntry_Object=MibTableRow
zxAnEponOnuTkIgmpEntry=_ZxAnEponOnuTkIgmpEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,39,1))
zxAnEponOnuTkIgmpEntry.setIndexNames((0,_E,_F),(0,_E,_A_),(0,_E,_B0))
if mibBuilder.loadTexts:zxAnEponOnuTkIgmpEntry.setStatus(_A)
class _ZxAnEponOnuTkIgmpVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnEponOnuTkIgmpVlanId_Type.__name__=_B
_ZxAnEponOnuTkIgmpVlanId_Object=MibTableColumn
zxAnEponOnuTkIgmpVlanId=_ZxAnEponOnuTkIgmpVlanId_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,39,1,1),_ZxAnEponOnuTkIgmpVlanId_Type())
zxAnEponOnuTkIgmpVlanId.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuTkIgmpVlanId.setStatus(_A)
_ZxAnEponOnuTkIgmpIpAddr_Type=IpAddress
_ZxAnEponOnuTkIgmpIpAddr_Object=MibTableColumn
zxAnEponOnuTkIgmpIpAddr=_ZxAnEponOnuTkIgmpIpAddr_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,39,1,2),_ZxAnEponOnuTkIgmpIpAddr_Type())
zxAnEponOnuTkIgmpIpAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOnuTkIgmpIpAddr.setStatus(_A)
_ZxAnEponOnuTkIgmpPortList_Type=OctetString
_ZxAnEponOnuTkIgmpPortList_Object=MibTableColumn
zxAnEponOnuTkIgmpPortList=_ZxAnEponOnuTkIgmpPortList_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,39,1,3),_ZxAnEponOnuTkIgmpPortList_Type())
zxAnEponOnuTkIgmpPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkIgmpPortList.setStatus(_A)
_ZxAnEponOnuTkLoopDetectTable_Object=MibTable
zxAnEponOnuTkLoopDetectTable=_ZxAnEponOnuTkLoopDetectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,40))
if mibBuilder.loadTexts:zxAnEponOnuTkLoopDetectTable.setStatus(_A)
_ZxAnEponOnuTkLoopDetectEntry_Object=MibTableRow
zxAnEponOnuTkLoopDetectEntry=_ZxAnEponOnuTkLoopDetectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,40,1))
zxAnEponOnuTkLoopDetectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuTkLoopDetectEntry.setStatus(_A)
class _ZxAnEponOnuTkLoopDetectAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuTkLoopDetectAdminStatus_Type.__name__=_B
_ZxAnEponOnuTkLoopDetectAdminStatus_Object=MibTableColumn
zxAnEponOnuTkLoopDetectAdminStatus=_ZxAnEponOnuTkLoopDetectAdminStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,40,1,1),_ZxAnEponOnuTkLoopDetectAdminStatus_Type())
zxAnEponOnuTkLoopDetectAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkLoopDetectAdminStatus.setStatus(_A)
class _ZxAnEponOnuTkLoopDetectInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ZxAnEponOnuTkLoopDetectInterval_Type.__name__=_B
_ZxAnEponOnuTkLoopDetectInterval_Object=MibTableColumn
zxAnEponOnuTkLoopDetectInterval=_ZxAnEponOnuTkLoopDetectInterval_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,40,1,2),_ZxAnEponOnuTkLoopDetectInterval_Type())
zxAnEponOnuTkLoopDetectInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkLoopDetectInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponOnuTkLoopDetectInterval.setUnits('second')
class _ZxAnEponOnuTkLoopDetectOamType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_ZxAnEponOnuTkLoopDetectOamType_Type.__name__=_B
_ZxAnEponOnuTkLoopDetectOamType_Object=MibTableColumn
zxAnEponOnuTkLoopDetectOamType=_ZxAnEponOnuTkLoopDetectOamType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,40,1,3),_ZxAnEponOnuTkLoopDetectOamType_Type())
zxAnEponOnuTkLoopDetectOamType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkLoopDetectOamType.setStatus(_A)
_ZxAnEponOnuTkPortShapingTable_Object=MibTable
zxAnEponOnuTkPortShapingTable=_ZxAnEponOnuTkPortShapingTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,41))
if mibBuilder.loadTexts:zxAnEponOnuTkPortShapingTable.setStatus(_A)
_ZxAnEponOnuTkPortShapingEntry_Object=MibTableRow
zxAnEponOnuTkPortShapingEntry=_ZxAnEponOnuTkPortShapingEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,41,1))
zxAnEponOnuTkPortShapingEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuTkPortShapingEntry.setStatus(_A)
class _ZxAnEponOnuTkPortDsShapingAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuTkPortDsShapingAdminStatus_Type.__name__=_B
_ZxAnEponOnuTkPortDsShapingAdminStatus_Object=MibTableColumn
zxAnEponOnuTkPortDsShapingAdminStatus=_ZxAnEponOnuTkPortDsShapingAdminStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,41,1,1),_ZxAnEponOnuTkPortDsShapingAdminStatus_Type())
zxAnEponOnuTkPortDsShapingAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkPortDsShapingAdminStatus.setStatus(_A)
_ZxAnEponOnuTkPortDsShapingRate_Type=Integer32
_ZxAnEponOnuTkPortDsShapingRate_Object=MibTableColumn
zxAnEponOnuTkPortDsShapingRate=_ZxAnEponOnuTkPortDsShapingRate_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,41,1,2),_ZxAnEponOnuTkPortDsShapingRate_Type())
zxAnEponOnuTkPortDsShapingRate.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkPortDsShapingRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponOnuTkPortDsShapingRate.setUnits(_m)
class _ZxAnEponOnuTkPortDsShapingOamType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_ZxAnEponOnuTkPortDsShapingOamType_Type.__name__=_B
_ZxAnEponOnuTkPortDsShapingOamType_Object=MibTableColumn
zxAnEponOnuTkPortDsShapingOamType=_ZxAnEponOnuTkPortDsShapingOamType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,31,41,1,3),_ZxAnEponOnuTkPortDsShapingOamType_Type())
zxAnEponOnuTkPortDsShapingOamType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkPortDsShapingOamType.setStatus(_A)
_ZxAnEponOnuTkActionMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuTkActionMgmt=_ZxAnEponOnuTkActionMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32))
_ZxAnEponOnuTkRestoreActionTable_Object=MibTable
zxAnEponOnuTkRestoreActionTable=_ZxAnEponOnuTkRestoreActionTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32,31))
if mibBuilder.loadTexts:zxAnEponOnuTkRestoreActionTable.setStatus(_A)
_ZxAnEponOnuTkRestoreActionEntry_Object=MibTableRow
zxAnEponOnuTkRestoreActionEntry=_ZxAnEponOnuTkRestoreActionEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32,31,1))
zxAnEponOnuTkRestoreActionEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuTkRestoreActionEntry.setStatus(_A)
class _ZxAnEponOnuTkRestoreFactorySettings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('restore',1))
_ZxAnEponOnuTkRestoreFactorySettings_Type.__name__=_B
_ZxAnEponOnuTkRestoreFactorySettings_Object=MibTableColumn
zxAnEponOnuTkRestoreFactorySettings=_ZxAnEponOnuTkRestoreFactorySettings_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32,31,1,1),_ZxAnEponOnuTkRestoreFactorySettings_Type())
zxAnEponOnuTkRestoreFactorySettings.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkRestoreFactorySettings.setStatus(_A)
class _ZxAnEponOnuTkRestoreOamType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_ZxAnEponOnuTkRestoreOamType_Type.__name__=_B
_ZxAnEponOnuTkRestoreOamType_Object=MibTableColumn
zxAnEponOnuTkRestoreOamType=_ZxAnEponOnuTkRestoreOamType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32,31,1,2),_ZxAnEponOnuTkRestoreOamType_Type())
zxAnEponOnuTkRestoreOamType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkRestoreOamType.setStatus(_A)
_ZxAnEponOnuTkUpdateVerTable_Object=MibTable
zxAnEponOnuTkUpdateVerTable=_ZxAnEponOnuTkUpdateVerTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32,32))
if mibBuilder.loadTexts:zxAnEponOnuTkUpdateVerTable.setStatus(_A)
_ZxAnEponOnuTkUpdateVerEntry_Object=MibTableRow
zxAnEponOnuTkUpdateVerEntry=_ZxAnEponOnuTkUpdateVerEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32,32,1))
zxAnEponOnuTkUpdateVerEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuTkUpdateVerEntry.setStatus(_A)
class _ZxAnEponOnuTkVerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('boot',1),('application',2),('personality',3),('diagnostic',4),('dsan',5)))
_ZxAnEponOnuTkVerType_Type.__name__=_B
_ZxAnEponOnuTkVerType_Object=MibTableColumn
zxAnEponOnuTkVerType=_ZxAnEponOnuTkVerType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32,32,1,1),_ZxAnEponOnuTkVerType_Type())
zxAnEponOnuTkVerType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkVerType.setStatus(_A)
_ZxAnEponOnuTkVerName_Type=DisplayString
_ZxAnEponOnuTkVerName_Object=MibTableColumn
zxAnEponOnuTkVerName=_ZxAnEponOnuTkVerName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32,32,1,2),_ZxAnEponOnuTkVerName_Type())
zxAnEponOnuTkVerName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkVerName.setStatus(_A)
class _ZxAnEponOnuTkUpdateStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noStart',1),('failed',2),(_AV,3),('writtingImage',4),('finished',5)))
_ZxAnEponOnuTkUpdateStatus_Type.__name__=_B
_ZxAnEponOnuTkUpdateStatus_Object=MibTableColumn
zxAnEponOnuTkUpdateStatus=_ZxAnEponOnuTkUpdateStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32,32,1,3),_ZxAnEponOnuTkUpdateStatus_Type())
zxAnEponOnuTkUpdateStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkUpdateStatus.setStatus(_A)
class _ZxAnEponOnuTkUpdateProgress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnEponOnuTkUpdateProgress_Type.__name__=_B
_ZxAnEponOnuTkUpdateProgress_Object=MibTableColumn
zxAnEponOnuTkUpdateProgress=_ZxAnEponOnuTkUpdateProgress_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32,32,1,4),_ZxAnEponOnuTkUpdateProgress_Type())
zxAnEponOnuTkUpdateProgress.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkUpdateProgress.setStatus(_A)
if mibBuilder.loadTexts:zxAnEponOnuTkUpdateProgress.setUnits('percent')
_ZxAnEponOnuTkOnuAckCode_Type=Integer32
_ZxAnEponOnuTkOnuAckCode_Object=MibTableColumn
zxAnEponOnuTkOnuAckCode=_ZxAnEponOnuTkOnuAckCode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32,32,1,5),_ZxAnEponOnuTkOnuAckCode_Type())
zxAnEponOnuTkOnuAckCode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkOnuAckCode.setStatus(_A)
_ZxAnEponOnuTkErrorCode_Type=Integer32
_ZxAnEponOnuTkErrorCode_Object=MibTableColumn
zxAnEponOnuTkErrorCode=_ZxAnEponOnuTkErrorCode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32,32,1,6),_ZxAnEponOnuTkErrorCode_Type())
zxAnEponOnuTkErrorCode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkErrorCode.setStatus(_A)
_ZxAnEponOnuTkUpdattingVerName_Type=DisplayString
_ZxAnEponOnuTkUpdattingVerName_Object=MibTableColumn
zxAnEponOnuTkUpdattingVerName=_ZxAnEponOnuTkUpdattingVerName_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32,32,1,7),_ZxAnEponOnuTkUpdattingVerName_Type())
zxAnEponOnuTkUpdattingVerName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkUpdattingVerName.setStatus(_A)
_ZxAnEponOnuTkAutoUpdateVerTable_Object=MibTable
zxAnEponOnuTkAutoUpdateVerTable=_ZxAnEponOnuTkAutoUpdateVerTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32,33))
if mibBuilder.loadTexts:zxAnEponOnuTkAutoUpdateVerTable.setStatus(_A)
_ZxAnEponOnuTkAutoUpdateVerEntry_Object=MibTableRow
zxAnEponOnuTkAutoUpdateVerEntry=_ZxAnEponOnuTkAutoUpdateVerEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32,33,1))
zxAnEponOnuTkAutoUpdateVerEntry.setIndexNames((0,_E,_B1))
if mibBuilder.loadTexts:zxAnEponOnuTkAutoUpdateVerEntry.setStatus(_A)
_ZxAnEponOltIfIndex_Type=Integer32
_ZxAnEponOltIfIndex_Object=MibTableColumn
zxAnEponOltIfIndex=_ZxAnEponOltIfIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32,33,1,1),_ZxAnEponOltIfIndex_Type())
zxAnEponOltIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEponOltIfIndex.setStatus(_A)
class _ZxAnEponOnuTkAutoUpdateAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxAnEponOnuTkAutoUpdateAdminStatus_Type.__name__=_B
_ZxAnEponOnuTkAutoUpdateAdminStatus_Object=MibTableColumn
zxAnEponOnuTkAutoUpdateAdminStatus=_ZxAnEponOnuTkAutoUpdateAdminStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32,33,1,2),_ZxAnEponOnuTkAutoUpdateAdminStatus_Type())
zxAnEponOnuTkAutoUpdateAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkAutoUpdateAdminStatus.setStatus(_A)
class _ZxAnEponOnuTkVerActiveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('immediately',1),('next',2)))
_ZxAnEponOnuTkVerActiveMode_Type.__name__=_B
_ZxAnEponOnuTkVerActiveMode_Object=MibTableColumn
zxAnEponOnuTkVerActiveMode=_ZxAnEponOnuTkVerActiveMode_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,32,33,1,3),_ZxAnEponOnuTkVerActiveMode_Type())
zxAnEponOnuTkVerActiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkVerActiveMode.setStatus(_A)
_ZxAnEponOnuTkStatisticMgmt_ObjectIdentity=ObjectIdentity
zxAnEponOnuTkStatisticMgmt=_ZxAnEponOnuTkStatisticMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33))
_ZxAnEponOnuTkGlobalStatTable_Object=MibTable
zxAnEponOnuTkGlobalStatTable=_ZxAnEponOnuTkGlobalStatTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,31))
if mibBuilder.loadTexts:zxAnEponOnuTkGlobalStatTable.setStatus(_A)
_ZxAnEponOnuTkGlobalStatEntry_Object=MibTableRow
zxAnEponOnuTkGlobalStatEntry=_ZxAnEponOnuTkGlobalStatEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,31,1))
zxAnEponOnuTkGlobalStatEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuTkGlobalStatEntry.setStatus(_A)
_ZxAnEponOnuTkGlobalStatResetCounter_Type=Integer32
_ZxAnEponOnuTkGlobalStatResetCounter_Object=MibTableColumn
zxAnEponOnuTkGlobalStatResetCounter=_ZxAnEponOnuTkGlobalStatResetCounter_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,31,1,1),_ZxAnEponOnuTkGlobalStatResetCounter_Type())
zxAnEponOnuTkGlobalStatResetCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkGlobalStatResetCounter.setStatus(_A)
class _ZxAnEponOnuTkGlobalStatOamType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_ZxAnEponOnuTkGlobalStatOamType_Type.__name__=_B
_ZxAnEponOnuTkGlobalStatOamType_Object=MibTableColumn
zxAnEponOnuTkGlobalStatOamType=_ZxAnEponOnuTkGlobalStatOamType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,31,1,2),_ZxAnEponOnuTkGlobalStatOamType_Type())
zxAnEponOnuTkGlobalStatOamType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkGlobalStatOamType.setStatus(_A)
_ZxAnEponOnuTkGlobalStatTxRegReq_Type=Counter64
_ZxAnEponOnuTkGlobalStatTxRegReq_Object=MibTableColumn
zxAnEponOnuTkGlobalStatTxRegReq=_ZxAnEponOnuTkGlobalStatTxRegReq_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,31,1,32),_ZxAnEponOnuTkGlobalStatTxRegReq_Type())
zxAnEponOnuTkGlobalStatTxRegReq.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkGlobalStatTxRegReq.setStatus(_A)
_ZxAnEponOnuTkGlobalStatRxReg_Type=Counter64
_ZxAnEponOnuTkGlobalStatRxReg_Object=MibTableColumn
zxAnEponOnuTkGlobalStatRxReg=_ZxAnEponOnuTkGlobalStatRxReg_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,31,1,33),_ZxAnEponOnuTkGlobalStatRxReg_Type())
zxAnEponOnuTkGlobalStatRxReg.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkGlobalStatRxReg.setStatus(_A)
_ZxAnEponOnuTkGlobalStatTxRegAck_Type=Counter64
_ZxAnEponOnuTkGlobalStatTxRegAck_Object=MibTableColumn
zxAnEponOnuTkGlobalStatTxRegAck=_ZxAnEponOnuTkGlobalStatTxRegAck_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,31,1,34),_ZxAnEponOnuTkGlobalStatTxRegAck_Type())
zxAnEponOnuTkGlobalStatTxRegAck.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkGlobalStatTxRegAck.setStatus(_A)
_ZxAnEponOnuTkGlobalStatRxGateFrames_Type=Counter64
_ZxAnEponOnuTkGlobalStatRxGateFrames_Object=MibTableColumn
zxAnEponOnuTkGlobalStatRxGateFrames=_ZxAnEponOnuTkGlobalStatRxGateFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,31,1,35),_ZxAnEponOnuTkGlobalStatRxGateFrames_Type())
zxAnEponOnuTkGlobalStatRxGateFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkGlobalStatRxGateFrames.setStatus(_A)
_ZxAnEponOnuTkGlobalStatTxReportFrames_Type=Counter64
_ZxAnEponOnuTkGlobalStatTxReportFrames_Object=MibTableColumn
zxAnEponOnuTkGlobalStatTxReportFrames=_ZxAnEponOnuTkGlobalStatTxReportFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,31,1,36),_ZxAnEponOnuTkGlobalStatTxReportFrames_Type())
zxAnEponOnuTkGlobalStatTxReportFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkGlobalStatTxReportFrames.setStatus(_A)
_ZxAnEponOnuTkPortStatTable_Object=MibTable
zxAnEponOnuTkPortStatTable=_ZxAnEponOnuTkPortStatTable_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,32))
if mibBuilder.loadTexts:zxAnEponOnuTkPortStatTable.setStatus(_A)
_ZxAnEponOnuTkPortStatEntry_Object=MibTableRow
zxAnEponOnuTkPortStatEntry=_ZxAnEponOnuTkPortStatEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,32,1))
zxAnEponOnuTkPortStatEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:zxAnEponOnuTkPortStatEntry.setStatus(_A)
_ZxAnEponOnuTkPortStatResetCounter_Type=Integer32
_ZxAnEponOnuTkPortStatResetCounter_Object=MibTableColumn
zxAnEponOnuTkPortStatResetCounter=_ZxAnEponOnuTkPortStatResetCounter_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,32,1,1),_ZxAnEponOnuTkPortStatResetCounter_Type())
zxAnEponOnuTkPortStatResetCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkPortStatResetCounter.setStatus(_A)
class _ZxAnEponOnuTkPortStatOamType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_ZxAnEponOnuTkPortStatOamType_Type.__name__=_B
_ZxAnEponOnuTkPortStatOamType_Object=MibTableColumn
zxAnEponOnuTkPortStatOamType=_ZxAnEponOnuTkPortStatOamType_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,32,1,2),_ZxAnEponOnuTkPortStatOamType_Type())
zxAnEponOnuTkPortStatOamType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEponOnuTkPortStatOamType.setStatus(_A)
_ZxAnEponOnuTkPortStatTxFrames_Type=Counter64
_ZxAnEponOnuTkPortStatTxFrames_Object=MibTableColumn
zxAnEponOnuTkPortStatTxFrames=_ZxAnEponOnuTkPortStatTxFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,32,1,31),_ZxAnEponOnuTkPortStatTxFrames_Type())
zxAnEponOnuTkPortStatTxFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkPortStatTxFrames.setStatus(_A)
_ZxAnEponOnuTkPortStatTxBytes_Type=Counter64
_ZxAnEponOnuTkPortStatTxBytes_Object=MibTableColumn
zxAnEponOnuTkPortStatTxBytes=_ZxAnEponOnuTkPortStatTxBytes_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,32,1,32),_ZxAnEponOnuTkPortStatTxBytes_Type())
zxAnEponOnuTkPortStatTxBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkPortStatTxBytes.setStatus(_A)
_ZxAnEponOnuTkPortStatTxMulticast_Type=Counter64
_ZxAnEponOnuTkPortStatTxMulticast_Object=MibTableColumn
zxAnEponOnuTkPortStatTxMulticast=_ZxAnEponOnuTkPortStatTxMulticast_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,32,1,33),_ZxAnEponOnuTkPortStatTxMulticast_Type())
zxAnEponOnuTkPortStatTxMulticast.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkPortStatTxMulticast.setStatus(_A)
_ZxAnEponOnuTkPortStatTxBroadcast_Type=Counter64
_ZxAnEponOnuTkPortStatTxBroadcast_Object=MibTableColumn
zxAnEponOnuTkPortStatTxBroadcast=_ZxAnEponOnuTkPortStatTxBroadcast_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,32,1,34),_ZxAnEponOnuTkPortStatTxBroadcast_Type())
zxAnEponOnuTkPortStatTxBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkPortStatTxBroadcast.setStatus(_A)
_ZxAnEponOnuTkPortStatTxDropedFrames_Type=Counter64
_ZxAnEponOnuTkPortStatTxDropedFrames_Object=MibTableColumn
zxAnEponOnuTkPortStatTxDropedFrames=_ZxAnEponOnuTkPortStatTxDropedFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,32,1,35),_ZxAnEponOnuTkPortStatTxDropedFrames_Type())
zxAnEponOnuTkPortStatTxDropedFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkPortStatTxDropedFrames.setStatus(_A)
_ZxAnEponOnuTkPortStatRxFrames_Type=Counter64
_ZxAnEponOnuTkPortStatRxFrames_Object=MibTableColumn
zxAnEponOnuTkPortStatRxFrames=_ZxAnEponOnuTkPortStatRxFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,32,1,36),_ZxAnEponOnuTkPortStatRxFrames_Type())
zxAnEponOnuTkPortStatRxFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkPortStatRxFrames.setStatus(_A)
_ZxAnEponOnuTkPortStatRxBytes_Type=Counter64
_ZxAnEponOnuTkPortStatRxBytes_Object=MibTableColumn
zxAnEponOnuTkPortStatRxBytes=_ZxAnEponOnuTkPortStatRxBytes_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,32,1,37),_ZxAnEponOnuTkPortStatRxBytes_Type())
zxAnEponOnuTkPortStatRxBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkPortStatRxBytes.setStatus(_A)
_ZxAnEponOnuTkPortStatRxMulticast_Type=Counter64
_ZxAnEponOnuTkPortStatRxMulticast_Object=MibTableColumn
zxAnEponOnuTkPortStatRxMulticast=_ZxAnEponOnuTkPortStatRxMulticast_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,32,1,38),_ZxAnEponOnuTkPortStatRxMulticast_Type())
zxAnEponOnuTkPortStatRxMulticast.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkPortStatRxMulticast.setStatus(_A)
_ZxAnEponOnuTkPortStatRxBroadcast_Type=Counter64
_ZxAnEponOnuTkPortStatRxBroadcast_Object=MibTableColumn
zxAnEponOnuTkPortStatRxBroadcast=_ZxAnEponOnuTkPortStatRxBroadcast_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,32,1,39),_ZxAnEponOnuTkPortStatRxBroadcast_Type())
zxAnEponOnuTkPortStatRxBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkPortStatRxBroadcast.setStatus(_A)
_ZxAnEponOnuTkPortStatRxOversizeFrames_Type=Counter64
_ZxAnEponOnuTkPortStatRxOversizeFrames_Object=MibTableColumn
zxAnEponOnuTkPortStatRxOversizeFrames=_ZxAnEponOnuTkPortStatRxOversizeFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,32,1,40),_ZxAnEponOnuTkPortStatRxOversizeFrames_Type())
zxAnEponOnuTkPortStatRxOversizeFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkPortStatRxOversizeFrames.setStatus(_A)
_ZxAnEponOnuTkPortStatRxUnderSizeFrames_Type=Counter64
_ZxAnEponOnuTkPortStatRxUnderSizeFrames_Object=MibTableColumn
zxAnEponOnuTkPortStatRxUnderSizeFrames=_ZxAnEponOnuTkPortStatRxUnderSizeFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,32,1,41),_ZxAnEponOnuTkPortStatRxUnderSizeFrames_Type())
zxAnEponOnuTkPortStatRxUnderSizeFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkPortStatRxUnderSizeFrames.setStatus(_A)
_ZxAnEponOnuTkPortStatRxCrcFrames_Type=Counter64
_ZxAnEponOnuTkPortStatRxCrcFrames_Object=MibTableColumn
zxAnEponOnuTkPortStatRxCrcFrames=_ZxAnEponOnuTkPortStatRxCrcFrames_Object((1,3,6,1,4,1,3902,1015,1010,1,1,101,31,33,32,1,42),_ZxAnEponOnuTkPortStatRxCrcFrames_Type())
zxAnEponOnuTkPortStatRxCrcFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuTkPortStatRxCrcFrames.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zxAnEponOnuRemoteMgmt':zxAnEponOnuRemoteMgmt,'zxAnEponOnuExtendedAttrMgmt':zxAnEponOnuExtendedAttrMgmt,'zxAnEponOnuSnTable':zxAnEponOnuSnTable,'zxAnEponOnuSnEntry':zxAnEponOnuSnEntry,_F:zxAnEponOnuIfIndex,'zxAnEponOnuVendorId':zxAnEponOnuVendorId,'zxAnEponOnuModel':zxAnEponOnuModel,'zxAnEponOnuMacAddr':zxAnEponOnuMacAddr,'zxAnEponOnuHardwareVersion':zxAnEponOnuHardwareVersion,'zxAnEponOnuSoftwareVersion':zxAnEponOnuSoftwareVersion,'zxAnEponOnuExtendedModel':zxAnEponOnuExtendedModel,'zxAnEponOnuFirmwareVerTable':zxAnEponOnuFirmwareVerTable,'zxAnEponOnuFirmwareVerEntry':zxAnEponOnuFirmwareVerEntry,'zxAnEponOnuFirmwareVer':zxAnEponOnuFirmwareVer,'zxAnEponOnuChipsetIdTable':zxAnEponOnuChipsetIdTable,'zxAnEponOnuChipsetIdEntry':zxAnEponOnuChipsetIdEntry,'zxAnEponOnuChipVendorId':zxAnEponOnuChipVendorId,'zxAnEponOnuChipModel':zxAnEponOnuChipModel,'zxAnEponOnuChipRevision':zxAnEponOnuChipRevision,'zxAnEponOnuChipDate':zxAnEponOnuChipDate,'zxAnEponOnuCapabilityTable':zxAnEponOnuCapabilityTable,'zxAnEponOnuCapabilityEntry':zxAnEponOnuCapabilityEntry,'zxAnEponOnuServiceSupported':zxAnEponOnuServiceSupported,'zxAnEponOnuGePortNumber':zxAnEponOnuGePortNumber,'zxAnEponOnuGePortBitmap':zxAnEponOnuGePortBitmap,'zxAnEponOnuFePortNumber':zxAnEponOnuFePortNumber,'zxAnEponOnuFePortBitmap':zxAnEponOnuFePortBitmap,'zxAnEponOnuPotsPortNumber':zxAnEponOnuPotsPortNumber,'zxAnEponOnuE1PortNumber':zxAnEponOnuE1PortNumber,'zxAnEponOnuUsQueueNumber':zxAnEponOnuUsQueueNumber,'zxAnEponOnuUsPortMaxQueueNumber':zxAnEponOnuUsPortMaxQueueNumber,'zxAnEponOnuDsQueueNumber':zxAnEponOnuDsQueueNumber,'zxAnEponOnuDsPortMaxQueueNumber':zxAnEponOnuDsPortMaxQueueNumber,'zxAnEponOnuBatteryBackup':zxAnEponOnuBatteryBackup,'zxAnEponOnuEthLinkStateTable':zxAnEponOnuEthLinkStateTable,'zxAnEponOnuEthLinkStateEntry':zxAnEponOnuEthLinkStateEntry,_H:zxAnEponOnuPortId,'zxAnEponOnuEthPortLinkState':zxAnEponOnuEthPortLinkState,'zxAnEponOnuEthPortPauseTable':zxAnEponOnuEthPortPauseTable,'zxAnEponOnuEthPortPauseEntry':zxAnEponOnuEthPortPauseEntry,'zxAnEponOnuPortBackPressure':zxAnEponOnuPortBackPressure,'zxAnEponOnuEthPortPolicingTable':zxAnEponOnuEthPortPolicingTable,'zxAnEponOnuEthPortPolicingEntry':zxAnEponOnuEthPortPolicingEntry,'zxAnEponOnuPortPolicing':zxAnEponOnuPortPolicing,'zxAnEponOnuPortPolicingCir':zxAnEponOnuPortPolicingCir,'zxAnEponOnuPortPolicingBucketDepth':zxAnEponOnuPortPolicingBucketDepth,'zxAnEponOnuPortPolicingExtraBurstSize':zxAnEponOnuPortPolicingExtraBurstSize,'zxAnEponOnuPortPolicingDownStream':zxAnEponOnuPortPolicingDownStream,'zxAnEponOnuPortPolicingCirDownStream':zxAnEponOnuPortPolicingCirDownStream,'zxAnEponOnuPortPolicingBucketDepthDownStream':zxAnEponOnuPortPolicingBucketDepthDownStream,'zxAnEponOnuPortPolicingExtraBurstSizeDownStream':zxAnEponOnuPortPolicingExtraBurstSizeDownStream,'zxAnEponOnuVoipPortTable':zxAnEponOnuVoipPortTable,'zxAnEponOnuVoipPortEntry':zxAnEponOnuVoipPortEntry,'zxAnEponOnuVoipPortEnable':zxAnEponOnuVoipPortEnable,'zxAnEponOnuE1PortTable':zxAnEponOnuE1PortTable,'zxAnEponOnuE1PortEntry':zxAnEponOnuE1PortEntry,'zxAnEponOnuE1PortEnable':zxAnEponOnuE1PortEnable,'zxAnEponOnuVlanCfgMgmt':zxAnEponOnuVlanCfgMgmt,'zxAnEponOnuVlanCfgTable':zxAnEponOnuVlanCfgTable,'zxAnEponOnuVlanCfgEntry':zxAnEponOnuVlanCfgEntry,'zxAnEponOnuVlanMode':zxAnEponOnuVlanMode,'zxAnEponOnuVlanCfgState':zxAnEponOnuVlanCfgState,'zxAnEponOnuVlanTagTable':zxAnEponOnuVlanTagTable,'zxAnEponOnuVlanTagEntry':zxAnEponOnuVlanTagEntry,'zxAnEponOnuVlanTagVid':zxAnEponOnuVlanTagVid,'zxAnEponOnuVlanTagTpid':zxAnEponOnuVlanTagTpid,'zxAnEponOnuVlanTagCfi':zxAnEponOnuVlanTagCfi,'zxAnEponOnuVlanPriority':zxAnEponOnuVlanPriority,'zxAnEponOnuVlanTranslationTable':zxAnEponOnuVlanTranslationTable,'zxAnEponOnuVlanTranslationEntry':zxAnEponOnuVlanTranslationEntry,_s:zxAnEponOnuVlanTransModeEntryId,'zxAnEponOnuVlanTransOriginalTag':zxAnEponOnuVlanTransOriginalTag,'zxAnEponOnuVlanTransNewTag':zxAnEponOnuVlanTransNewTag,'zxAnEponOnuVlanTransModeRowStatus':zxAnEponOnuVlanTransModeRowStatus,'zxAnEponOnuVlanTrunkTable':zxAnEponOnuVlanTrunkTable,'zxAnEponOnuVlanTrunkEntry':zxAnEponOnuVlanTrunkEntry,'zxAnEponOnuVlanTrunkModeVlan':zxAnEponOnuVlanTrunkModeVlan,'zxAnEponOnuVlanAggregationTable':zxAnEponOnuVlanAggregationTable,'zxAnEponOnuVlanAggregationEntry':zxAnEponOnuVlanAggregationEntry,_t:zxAnEponOnuVlanAggGrpId,'zxAnEponOnuVlamAggSrcVlanList':zxAnEponOnuVlamAggSrcVlanList,'zxAnEponOnuVlanAggDestVlan':zxAnEponOnuVlanAggDestVlan,'zxAnEponOnuVlanAggRowStatus':zxAnEponOnuVlanAggRowStatus,'zxAnEponOnuClassMarkingAttrMgmt':zxAnEponOnuClassMarkingAttrMgmt,'zxAnEponOnuClassMarkingConditionTable':zxAnEponOnuClassMarkingConditionTable,'zxAnEponOnuClassMarkingConditionEntry':zxAnEponOnuClassMarkingConditionEntry,_u:zxAnEponOnuClassMarkingConditionId,'zxAnEponOnuClassMarkingConditionName':zxAnEponOnuClassMarkingConditionName,'zxAnEponOnuClassMarkingField':zxAnEponOnuClassMarkingField,'zxAnEponOnuClassMarkingMatchValue':zxAnEponOnuClassMarkingMatchValue,'zxAnEponOnuClassMarkingOperator':zxAnEponOnuClassMarkingOperator,'zxAnEponOnuClassMarkingConditionRefCnt':zxAnEponOnuClassMarkingConditionRefCnt,'zxAnEponOnuClassMarkingConditionRowStatus':zxAnEponOnuClassMarkingConditionRowStatus,'zxAnEponOnuClassMarkingRuleTable':zxAnEponOnuClassMarkingRuleTable,'zxAnEponOnuClassMarkingRuleEntry':zxAnEponOnuClassMarkingRuleEntry,_v:zxAnEponOnuClassMarkingRuleId,'zxAnEponOnuClassMarkingRuleName':zxAnEponOnuClassMarkingRuleName,'zxAnEponOnuClassMarkingQueue':zxAnEponOnuClassMarkingQueue,'zxAnEponOnuClassMarkingPriority':zxAnEponOnuClassMarkingPriority,'zxAnEponOnuClassMarkingRuleRefCnt':zxAnEponOnuClassMarkingRuleRefCnt,'zxAnEponOnuClassMarkingRuleRowStatus':zxAnEponOnuClassMarkingRuleRowStatus,'zxAnEponOnuClassMarkingTable':zxAnEponOnuClassMarkingTable,'zxAnEponOnuClassMarkingEntry':zxAnEponOnuClassMarkingEntry,_w:zxAnEponOnuClassMarkingRulePrecedence,'zxAnEponOnuClassMarkingRuleIndex':zxAnEponOnuClassMarkingRuleIndex,'zxAnEponOnuClassMarkingRuleConditionList':zxAnEponOnuClassMarkingRuleConditionList,'zxAnEponOnuClassMarkingRowStatus':zxAnEponOnuClassMarkingRowStatus,'zxAnEponOnuClassMarkingRulePriority':zxAnEponOnuClassMarkingRulePriority,'zxAnEponOnuClassMarkingRuleDirection':zxAnEponOnuClassMarkingRuleDirection,'zxAnEponOnuClassMarkingRuleType':zxAnEponOnuClassMarkingRuleType,'zxAnEponOnuClassMarkingClearTable':zxAnEponOnuClassMarkingClearTable,'zxAnEponOnuClassMarkingClearEntry':zxAnEponOnuClassMarkingClearEntry,'zxAnEponOnuClassMarkingClear':zxAnEponOnuClassMarkingClear,'zxAnEponOnuClassMarkingCompatibilityTable':zxAnEponOnuClassMarkingCompatibilityTable,'zxAnEponOnuClassMarkingCompatibilityEntry':zxAnEponOnuClassMarkingCompatibilityEntry,'zxAnEponOnuClassMarkingRulePriorityFlag':zxAnEponOnuClassMarkingRulePriorityFlag,'zxAnEponOnuClassMarkingRuleDirectionFlag':zxAnEponOnuClassMarkingRuleDirectionFlag,'zxAnEponOnuClassMarkingRuleTypeFlag':zxAnEponOnuClassMarkingRuleTypeFlag,'zxAnEponOnuMulticastVlanTable':zxAnEponOnuMulticastVlanTable,'zxAnEponOnuMulticastVlanEntry':zxAnEponOnuMulticastVlanEntry,'zxAnEponOnuMulticastVlanAction':zxAnEponOnuMulticastVlanAction,'zxAnEponOnuMulticastVlanList':zxAnEponOnuMulticastVlanList,'zxAnEponOnuMulticastTagCfgTable':zxAnEponOnuMulticastTagCfgTable,'zxAnEponOnuMulticastTagCfgEntry':zxAnEponOnuMulticastTagCfgEntry,'zxAnEponOnuMulticastTagStripe':zxAnEponOnuMulticastTagStripe,'zxAnEponOnuMulticastSwitchTable':zxAnEponOnuMulticastSwitchTable,'zxAnEponOnuMulticastSwitchEntry':zxAnEponOnuMulticastSwitchEntry,'zxAnEponOnuMulticastSwitchAttr':zxAnEponOnuMulticastSwitchAttr,'zxAnEponOnuMulticastControlMgmt':zxAnEponOnuMulticastControlMgmt,'zxAnEponOnuMulticastControlClearTable':zxAnEponOnuMulticastControlClearTable,'zxAnEponOnuMulticastControlClearEntry':zxAnEponOnuMulticastControlClearEntry,'zxAnEponOnuMcstCtrlClear':zxAnEponOnuMcstCtrlClear,'zxAnEponOnuMulticastControlTable':zxAnEponOnuMulticastControlTable,'zxAnEponOnuMulticastControlEntry':zxAnEponOnuMulticastControlEntry,_z:zxAnEponOnuMcstCtrlEntryIndex,'zxAnEponOnuMcstCtrlAction':zxAnEponOnuMcstCtrlAction,'zxAnEponOnuMcstCtrlType':zxAnEponOnuMcstCtrlType,'zxAnEponOnuMcstCtrlUserId':zxAnEponOnuMcstCtrlUserId,'zxAnEponOnuMcstCtrlGda':zxAnEponOnuMcstCtrlGda,'zxAnEponOnuMcstCtrlMvlan':zxAnEponOnuMcstCtrlMvlan,'zxAnEponOnuMcstCtrlGdaIp':zxAnEponOnuMcstCtrlGdaIp,'zxAnEponOnuMaxGroupNumTable':zxAnEponOnuMaxGroupNumTable,'zxAnEponOnuMaxGroupNumEntry':zxAnEponOnuMaxGroupNumEntry,'zxAnEponOnuMaxGroupNum':zxAnEponOnuMaxGroupNum,'zxAnEponOnuAlarmCtrlTable':zxAnEponOnuAlarmCtrlTable,'zxAnEponOnuAlarmCtrlEntry':zxAnEponOnuAlarmCtrlEntry,'zxAnEponOnuAlarmCtr':zxAnEponOnuAlarmCtr,'zxAnEponOnuMACNumTable':zxAnEponOnuMACNumTable,'zxAnEponOnuMACNumEntry':zxAnEponOnuMACNumEntry,'zxAnEponOnuMACNum':zxAnEponOnuMACNum,'zxAnEponOnuUniLearnedMacs':zxAnEponOnuUniLearnedMacs,'zxAnEponOnuMACAgingTimeTable':zxAnEponOnuMACAgingTimeTable,'zxAnEponOnuMACAgingTimeEntry':zxAnEponOnuMACAgingTimeEntry,'zxAnEponOnuMACAgingTimeAttr':zxAnEponOnuMACAgingTimeAttr,'zxAnEponOnuFilterMACTable':zxAnEponOnuFilterMACTable,'zxAnEponOnuFilterMACEntry':zxAnEponOnuFilterMACEntry,_A0:zxAnEponOnuFilterMAC,_A1:zxEponFilterVlan,'zxAnEponOnuFilterMACEntryStatus':zxAnEponOnuFilterMACEntryStatus,'zxAnEponOnuBindMACTable':zxAnEponOnuBindMACTable,'zxAnEponOnuBindMACEntry':zxAnEponOnuBindMACEntry,_A2:zxAnEponOnuBindMAC,_A3:zxEponBindVlan,'zxAnEponOnuBindMACEntryStatus':zxAnEponOnuBindMACEntryStatus,'zxAnEponOnuStaticMACTable':zxAnEponOnuStaticMACTable,'zxAnEponOnuStaticMACEntry':zxAnEponOnuStaticMACEntry,_A4:zxAnEponOnuStaticMAC,_A5:zxEponStaticVlan,'zxAnEponOnuStaicMACEntryStatus':zxAnEponOnuStaicMACEntryStatus,'zxAnEponOnuMACAddressClearTable':zxAnEponOnuMACAddressClearTable,'zxAnEponOnuMACAddressClearEntry':zxAnEponOnuMACAddressClearEntry,'zxAnEponOnuMACAddressType':zxAnEponOnuMACAddressType,'zxAnEponOnuManagerIPTable':zxAnEponOnuManagerIPTable,'zxAnEponOnuManagerIPTableEntry':zxAnEponOnuManagerIPTableEntry,'zxEponOnuIPAddress':zxEponOnuIPAddress,'zxEponOnuIPMask':zxEponOnuIPMask,'zxEponMangementPriority':zxEponMangementPriority,'zxEponMangementVlan':zxEponMangementVlan,'zxEponManagementHostIP':zxEponManagementHostIP,'zxEponManagementHostMask':zxEponManagementHostMask,'zxEponManagementGateway':zxEponManagementGateway,'zxEponOnuIPConfigureStatus':zxEponOnuIPConfigureStatus,'zxEponMangementSVlan':zxEponMangementSVlan,'zxAnEponOnuIsolationCtrlTable':zxAnEponOnuIsolationCtrlTable,'zxAnEponOnuIsolationCtrlEntry':zxAnEponOnuIsolationCtrlEntry,'zxAnEponOnuIsolationCtr':zxAnEponOnuIsolationCtr,'zxAnEponRmFastLeaveAbiTable':zxAnEponRmFastLeaveAbiTable,'zxAnEponRmFastLeaveAbiEntry':zxAnEponRmFastLeaveAbiEntry,'fastleaveabi':fastleaveabi,'eponRmFastLeaveAdminStateTable':eponRmFastLeaveAdminStateTable,'eponRmFastLeaveAdminStateEntry':eponRmFastLeaveAdminStateEntry,'getState':getState,'eponIpGlobalTable':eponIpGlobalTable,'eponIpGlobalEntry':eponIpGlobalEntry,_A6:zxAnEponOnuVioceCardIndex,'zxAnEponOnuVoiceIpMngIpRelation':zxAnEponOnuVoiceIpMngIpRelation,'zxAnEponOnuVoiceIpMode':zxAnEponOnuVoiceIpMode,'zxAnEponOnuVoiceIpAddress':zxAnEponOnuVoiceIpAddress,'zxAnEponOnuVoiceDnsServer':zxAnEponOnuVoiceDnsServer,'zxAnEponOnuVoiceIpMask':zxAnEponOnuVoiceIpMask,'zxAnEponOnuVoiceGateway':zxAnEponOnuVoiceGateway,'zxAnEponOnuVoicePPPoEMode':zxAnEponOnuVoicePPPoEMode,'zxAnEponOnuVoicePPPoEUserName':zxAnEponOnuVoicePPPoEUserName,'zxAnEponOnuVoicePPPoEPassword':zxAnEponOnuVoicePPPoEPassword,'zxAnEponOnuVoiceTaggedFlag':zxAnEponOnuVoiceTaggedFlag,'zxAnEponOnuVoiceDataVlan':zxAnEponOnuVoiceDataVlan,'zxAnEponOnuVoiceDataPriority':zxAnEponOnuVoiceDataPriority,'zxAnEponOnuVoiceDhcpLeaseTime':zxAnEponOnuVoiceDhcpLeaseTime,'zxAnEponOnuVoicePPPoEStatus':zxAnEponOnuVoicePPPoEStatus,'epon0pticalTransceiverDiagnosisTable':epon0pticalTransceiverDiagnosisTable,'epon0pticalTransceiverDiagnosisEntry':epon0pticalTransceiverDiagnosisEntry,'zxAnEponOnuTransTemperature':zxAnEponOnuTransTemperature,'zxAnEponOnuSupplyVoltage':zxAnEponOnuSupplyVoltage,'zxAnEponOnuTxBiasCurrent':zxAnEponOnuTxBiasCurrent,'zxAnEponOnuTxPower':zxAnEponOnuTxPower,'zxAnEponOnuRxPower':zxAnEponOnuRxPower,'eponRmOnuTransAlarmCfgTable':eponRmOnuTransAlarmCfgTable,'eponRmOnuTransAlarmCfgTableEntry':eponRmOnuTransAlarmCfgTableEntry,'zxAnEponOnuTrans':zxAnEponOnuTrans,'eponRmOnuTransAlarmThresholdTable':eponRmOnuTransAlarmThresholdTable,'eponRmOnuTransAlarmThresholdEntry':eponRmOnuTransAlarmThresholdEntry,'zxAnEponOnuTempHighAlarm':zxAnEponOnuTempHighAlarm,'zxAnEponOnuTempLowAlarm':zxAnEponOnuTempLowAlarm,'zxAnEponOnuTempHighWarning':zxAnEponOnuTempHighWarning,'zxAnEponOnuTempLowwarning':zxAnEponOnuTempLowwarning,'zxAnEponOnuVoltageHighAlarm':zxAnEponOnuVoltageHighAlarm,'zxAnEponOnuVoltageLowAlarm':zxAnEponOnuVoltageLowAlarm,'zxAnEponOnuVoltageHighWarning':zxAnEponOnuVoltageHighWarning,'zxAnEponOnuVoltageLowWarning':zxAnEponOnuVoltageLowWarning,'zxAnEponOnuBiasHighAlarm':zxAnEponOnuBiasHighAlarm,'zxAnEponOnuBiasLowAlarm':zxAnEponOnuBiasLowAlarm,'zxAnEponOnuBiasHighWarning':zxAnEponOnuBiasHighWarning,'zxAnEponOnuBiasLowWarning':zxAnEponOnuBiasLowWarning,'zxAnEponOnuTxPowerHighAlarm':zxAnEponOnuTxPowerHighAlarm,'zxAnEponOnuTxPowerLowAlarm':zxAnEponOnuTxPowerLowAlarm,'zxAnEponOnuTxPowerHighWarning':zxAnEponOnuTxPowerHighWarning,'zxAnEponOnuTxPowerLowWarning':zxAnEponOnuTxPowerLowWarning,'zxAnEponOnuRxPowerHighAlarm':zxAnEponOnuRxPowerHighAlarm,'zxAnEponOnuRxPowerLowAlarm':zxAnEponOnuRxPowerLowAlarm,'zxAnEponOnuRxPowerHighWarning':zxAnEponOnuRxPowerHighWarning,'zxAnEponOnuRxPowerLowWarning':zxAnEponOnuRxPowerLowWarning,'zxEponUniProfileAdmin':zxEponUniProfileAdmin,'zxEponUniProfileTable':zxEponUniProfileTable,'zxEponUniProfileEntry':zxEponUniProfileEntry,_A7:uniProfileIndex,'uniProfileName':uniProfileName,'uniProfileUpCir':uniProfileUpCir,'uniProfileUpCbs':uniProfileUpCbs,'uniProfileUpEbs':uniProfileUpEbs,'uniProfileDownCir':uniProfileDownCir,'uniProfileDownCbs':uniProfileDownCbs,'uniProfileDownEbs':uniProfileDownEbs,'uniProfileRowStatus':uniProfileRowStatus,'uniProfileNextIndex':uniProfileNextIndex,'zxEponUniLimitCfgTable':zxEponUniLimitCfgTable,'zxEponUniLimitCfgEntry':zxEponUniLimitCfgEntry,'uniCfgLimitProfileIndex':uniCfgLimitProfileIndex,'zxAnEponRmVoipProfileMgmt':zxAnEponRmVoipProfileMgmt,'zxAnEponRmVoipIpProfileIdxNext':zxAnEponRmVoipIpProfileIdxNext,'zxAnEponRmVoipIpProfileTable':zxAnEponRmVoipIpProfileTable,'zxAnEponRmVoipIpProfileEntry':zxAnEponRmVoipIpProfileEntry,_A8:zxAnEponRmVoipIpProfileIdx,'zxAnEponRmVoipIpProfileName':zxAnEponRmVoipIpProfileName,'zxAnEponRmVoipIpMngIpRelation':zxAnEponRmVoipIpMngIpRelation,'zxAnEponRmVoipIpMode':zxAnEponRmVoipIpMode,'zxAnEponRmVoipIpDefaultGateWay':zxAnEponRmVoipIpDefaultGateWay,'zxAnEponRmVoipIpPrimaryDNSServerIp':zxAnEponRmVoipIpPrimaryDNSServerIp,'zxAnEponRmVoipIpPPPoEMode':zxAnEponRmVoipIpPPPoEMode,'zxAnEponRmVoipIpRowStatus':zxAnEponRmVoipIpRowStatus,'zxAnEponRmVoipVlanProfileIdxNext':zxAnEponRmVoipVlanProfileIdxNext,'zxAnEponRmVoipVlanProfileTable':zxAnEponRmVoipVlanProfileTable,'zxAnEponRmVoipVlanProfileEntry':zxAnEponRmVoipVlanProfileEntry,_A9:zxAnEponRmVoipVlanProfileIdx,'zxAnEponRmVoipVlanProfileName':zxAnEponRmVoipVlanProfileName,'zxAnEponRmVoipVlanTagMode':zxAnEponRmVoipVlanTagMode,'zxAnEponRmVoipVlanTagCVlan':zxAnEponRmVoipVlanTagCVlan,'zxAnEponRmVoipVlanTagPriority':zxAnEponRmVoipVlanTagPriority,'zxAnEponRmVoipVlanTagSVlan':zxAnEponRmVoipVlanTagSVlan,'zxAnEponRmVoipVlanRowStatus':zxAnEponRmVoipVlanRowStatus,'zxAnEponRmVoipH248ProfileIdxNext':zxAnEponRmVoipH248ProfileIdxNext,'zxAnEponRmVoipH248ProfileTable':zxAnEponRmVoipH248ProfileTable,'zxAnEponRmVoipH248ProfileEntry':zxAnEponRmVoipH248ProfileEntry,_AA:zxAnEponRmVoipH248ProfileIdx,'zxAnEponRmVoipH248ProfileName':zxAnEponRmVoipH248ProfileName,'zxAnEponRmVoipH248RegServerIp':zxAnEponRmVoipH248RegServerIp,'zxAnEponRmVoipH248RegServerPort':zxAnEponRmVoipH248RegServerPort,'zxAnEponRmVoipH248BackRegServerIp':zxAnEponRmVoipH248BackRegServerIp,'zxAnEponRmVoipH248BackRegServerPort':zxAnEponRmVoipH248BackRegServerPort,'zxAnEponRmVoipH248RtpLinkKeptFlag':zxAnEponRmVoipH248RtpLinkKeptFlag,'zxAnEponRmVoipH248OnuHeartbeatMode':zxAnEponRmVoipH248OnuHeartbeatMode,'zxAnEponRmVoipH248OnuHeartbeatCycle':zxAnEponRmVoipH248OnuHeartbeatCycle,'zxAnEponRmVoipH248OnuHeartbeatCount':zxAnEponRmVoipH248OnuHeartbeatCount,'zxAnEponRmVoipH248MgRegMode':zxAnEponRmVoipH248MgRegMode,'zxAnEponRmVoipH248MgPort':zxAnEponRmVoipH248MgPort,'zxAnEponRmVoipH248RowStatus':zxAnEponRmVoipH248RowStatus,'zxAnEponRmVoipMgcpProfileIdxNext':zxAnEponRmVoipMgcpProfileIdxNext,'zxAnEponRmVoipMgcpProfileTable':zxAnEponRmVoipMgcpProfileTable,'zxAnEponRmVoipMgcpProfileEntry':zxAnEponRmVoipMgcpProfileEntry,_AD:zxAnEponRmVoipMgcpProfileIdx,'zxAnEponRmVoipMgcpProfileName':zxAnEponRmVoipMgcpProfileName,'zxAnEponRmVoipMgcpRegServerIp':zxAnEponRmVoipMgcpRegServerIp,'zxAnEponRmVoipMgcpRegServerPort':zxAnEponRmVoipMgcpRegServerPort,'zxAnEponRmVoipMgcpBackRegServerIp':zxAnEponRmVoipMgcpBackRegServerIp,'zxAnEponRmVoipMgcpBackRegServerPort':zxAnEponRmVoipMgcpBackRegServerPort,'zxAnEponRmVoipMgcpOnuHeartbeatMode':zxAnEponRmVoipMgcpOnuHeartbeatMode,'zxAnEponRmVoipMgcpOnuHeartbeatCycle':zxAnEponRmVoipMgcpOnuHeartbeatCycle,'zxAnEponRmVoipMgcpOnuHeartbeatCount':zxAnEponRmVoipMgcpOnuHeartbeatCount,'zxAnEponRmVoipMgcpMgRegMode':zxAnEponRmVoipMgcpMgRegMode,'zxAnEponRmVoipMgcpMgPort':zxAnEponRmVoipMgcpMgPort,'zxAnEponRmVoipMgcpRowStatus':zxAnEponRmVoipMgcpRowStatus,'zxAnEponRmVoipSipProfileIdxNext':zxAnEponRmVoipSipProfileIdxNext,'zxAnEponRmVoipSipProfileTable':zxAnEponRmVoipSipProfileTable,'zxAnEponRmVoipSipProfileEntry':zxAnEponRmVoipSipProfileEntry,_AE:zxAnEponRmVoipSipProfileIdx,'zxAnEponRmVoipSipProfileName':zxAnEponRmVoipSipProfileName,'zxAnEponRmVoipSipMgPort':zxAnEponRmVoipSipMgPort,'zxAnEponRmVoipSipRegServerIp':zxAnEponRmVoipSipRegServerIp,'zxAnEponRmVoipSipRegServerPort':zxAnEponRmVoipSipRegServerPort,'zxAnEponRmVoipSipBackRegServerIp':zxAnEponRmVoipSipBackRegServerIp,'zxAnEponRmVoipSipBackRegServerPort':zxAnEponRmVoipSipBackRegServerPort,'zxAnEponRmVoipSipProxyServerIp':zxAnEponRmVoipSipProxyServerIp,'zxAnEponRmVoipSipProxyServerPort':zxAnEponRmVoipSipProxyServerPort,'zxAnEponRmVoipSipBackProxyServerIp':zxAnEponRmVoipSipBackProxyServerIp,'zxAnEponRmVoipSipBackProxyServerPort':zxAnEponRmVoipSipBackProxyServerPort,'zxAnEponRmVoipSipOutBoundServerIp':zxAnEponRmVoipSipOutBoundServerIp,'zxAnEponRmVoipSipOutBoundServerPort':zxAnEponRmVoipSipOutBoundServerPort,'zxAnEponRmVoipSipRegInterval':zxAnEponRmVoipSipRegInterval,'zxAnEponRmVoipSipHeartbeatSwitch':zxAnEponRmVoipSipHeartbeatSwitch,'zxAnEponRmVoipSipHeartbeatCycle':zxAnEponRmVoipSipHeartbeatCycle,'zxAnEponRmVoipSipHeartbeatCount':zxAnEponRmVoipSipHeartbeatCount,'zxAnEponRmVoipSipRowStatus':zxAnEponRmVoipSipRowStatus,'zxAnEponRmVoipFaxProfileIdxNext':zxAnEponRmVoipFaxProfileIdxNext,'zxAnEponRmVoipFaxProfileTable':zxAnEponRmVoipFaxProfileTable,'zxAnEponRmVoipFaxProfileEntry':zxAnEponRmVoipFaxProfileEntry,_AF:zxAnEponRmVoipFaxProfileIdx,'zxAnEponRmVoipFaxProfileName':zxAnEponRmVoipFaxProfileName,'zxAnEponRmVoipFaxMode':zxAnEponRmVoipFaxMode,'zxAnEponRmVoipFaxControlMode':zxAnEponRmVoipFaxControlMode,'zxAnEponRmVoipFaxRowStatus':zxAnEponRmVoipFaxRowStatus,'zxAnEponRmVoipMgmt':zxAnEponRmVoipMgmt,'zxAnEponRmVoipIpInfoTable':zxAnEponRmVoipIpInfoTable,'zxAnEponRmVoipIpInfoEntry':zxAnEponRmVoipIpInfoEntry,_M:zxAnEponOnuCardIndex,'zxAnEponRmVoipIpAddress':zxAnEponRmVoipIpAddress,'zxAnEponRmVoipIpNetMask':zxAnEponRmVoipIpNetMask,'zxAnEponRmVoipPppoeInfoTable':zxAnEponRmVoipPppoeInfoTable,'zxAnEponRmVoipPppoeInfoEntry':zxAnEponRmVoipPppoeInfoEntry,'zxAnEponRmVoipPppoeUserName':zxAnEponRmVoipPppoeUserName,'zxAnEponRmVoipPppoePassword':zxAnEponRmVoipPppoePassword,'zxAnEponRmVoipH248MgcpAttrTable':zxAnEponRmVoipH248MgcpAttrTable,'zxAnEponRmVoipH248MgcpAttrEntry':zxAnEponRmVoipH248MgcpAttrEntry,'zxAnEponRmVoipH248MgcpMID':zxAnEponRmVoipH248MgcpMID,'zxAnEponRmVoipH248MgcpActiveMgc':zxAnEponRmVoipH248MgcpActiveMgc,'zxAnEponRmVoipH248MgcpUserTidCfgTable':zxAnEponRmVoipH248MgcpUserTidCfgTable,'zxAnEponRmVoipH248MgcpUserTidCfgEntry':zxAnEponRmVoipH248MgcpUserTidCfgEntry,_AH:zxAnEponRmVoipH248MgcpUserTidGroupIdx,'zxAnEponRmVoipH248MgcpUserTidBeginIdx':zxAnEponRmVoipH248MgcpUserTidBeginIdx,'zxAnEponRmVoipH248MgcpUserTidNumber':zxAnEponRmVoipH248MgcpUserTidNumber,'zxAnEponRmVoipH248MgcpUserTidPrefix':zxAnEponRmVoipH248MgcpUserTidPrefix,'zxAnEponRmVoipH248MgcpUserTidBeginDigit':zxAnEponRmVoipH248MgcpUserTidBeginDigit,'zxAnEponRmVoipH248MgcpUserTidDigitAlignMode':zxAnEponRmVoipH248MgcpUserTidDigitAlignMode,'zxAnEponRmVoipH248MgcpUserTidDigitLength':zxAnEponRmVoipH248MgcpUserTidDigitLength,'zxAnEponRmVoipH248MgcpUserTidRowStatus':zxAnEponRmVoipH248MgcpUserTidRowStatus,'zxAnEponRmVoipH248MgcpRtpTidCfgTable':zxAnEponRmVoipH248MgcpRtpTidCfgTable,'zxAnEponRmVoipH248MgcpRtpTidCfgEntry':zxAnEponRmVoipH248MgcpRtpTidCfgEntry,'zxAnEponRmVoipH248MgcpRtpTidPrefix':zxAnEponRmVoipH248MgcpRtpTidPrefix,'zxAnEponRmVoipH248MgcpRtpTidBeginDigit':zxAnEponRmVoipH248MgcpRtpTidBeginDigit,'zxAnEponRmVoipH248MgcpRtpTidDigitAlignMode':zxAnEponRmVoipH248MgcpRtpTidDigitAlignMode,'zxAnEponRmVoipH248MgcpRtpTidDigitLength':zxAnEponRmVoipH248MgcpRtpTidDigitLength,'zxAnEponRmVoipH248MgcpRtpTidNum':zxAnEponRmVoipH248MgcpRtpTidNum,'zxAnEponRmVoipSipUserCfgTable':zxAnEponRmVoipSipUserCfgTable,'zxAnEponRmVoipSipUserCfgEntry':zxAnEponRmVoipSipUserCfgEntry,'zxAnEponRmVoipSipUserAccount':zxAnEponRmVoipSipUserAccount,'zxAnEponRmVoipSipUserName':zxAnEponRmVoipSipUserName,'zxAnEponRmVoipSipUserPassword':zxAnEponRmVoipSipUserPassword,'zxAnEponRmVoipBaseInfoTable':zxAnEponRmVoipBaseInfoTable,'zxAnEponRmVoipBaseInfoEntry':zxAnEponRmVoipBaseInfoEntry,'zxAnEponRmVoipMacAddress':zxAnEponRmVoipMacAddress,'zxAnEponRmVoipProtocolSupported':zxAnEponRmVoipProtocolSupported,'zxAnEponRmVoipSoftwareVersion':zxAnEponRmVoipSoftwareVersion,'zxAnEponRmVoipSoftwareVersionTime':zxAnEponRmVoipSoftwareVersionTime,'zxAnEponRmVoipUserCount':zxAnEponRmVoipUserCount,'zxAnEponRmVoipProtocolUsed':zxAnEponRmVoipProtocolUsed,'zxAnEponRmVoipH248MgcpUserTidInfoTable':zxAnEponRmVoipH248MgcpUserTidInfoTable,'zxAnEponRmVoipH248MgcpUserTidInfoEntry':zxAnEponRmVoipH248MgcpUserTidInfoEntry,'zxAnEponRmVoipH248MgcpUserTidName':zxAnEponRmVoipH248MgcpUserTidName,'zxAnEponRmVoipH248MgcpRtpTidInfoTable':zxAnEponRmVoipH248MgcpRtpTidInfoTable,'zxAnEponRmVoipH248MgcpRtpTidInfoEntry':zxAnEponRmVoipH248MgcpRtpTidInfoEntry,'zxAnEponRmVoipH248MgcpRtpTidNumber':zxAnEponRmVoipH248MgcpRtpTidNumber,'zxAnEponRmVoipH248MgcpRtpTidFirstName':zxAnEponRmVoipH248MgcpRtpTidFirstName,'zxAnEponRmVoipModuleStatusTable':zxAnEponRmVoipModuleStatusTable,'zxAnEponRmVoipModuleStatusEntry':zxAnEponRmVoipModuleStatusEntry,'zxAnEponRmVoipModuleStatus':zxAnEponRmVoipModuleStatus,'zxAnEponRmVoipModuleAction':zxAnEponRmVoipModuleAction,'zxAnEponRmVoipUserIfStatusTable':zxAnEponRmVoipUserIfStatusTable,'zxAnEponRmVoipUserIfStatusEntry':zxAnEponRmVoipUserIfStatusEntry,'zxAnEponRmVoipPortOperStatus':zxAnEponRmVoipPortOperStatus,'zxAnEponRmVoipPortServiceType':zxAnEponRmVoipPortServiceType,'zxAnEponRmVoipPortServiceState':zxAnEponRmVoipPortServiceState,'zxAnEponRmVoipPortCodecMode':zxAnEponRmVoipPortCodecMode,'zxAnEponRmVoipPortAction':zxAnEponRmVoipPortAction,'zxAnEponRmVoipPortReversalCtrl':zxAnEponRmVoipPortReversalCtrl,'zxAnEponRmVoipPortPcmToPktGain':zxAnEponRmVoipPortPcmToPktGain,'zxAnEponRmVoipPortPktToPcmGain':zxAnEponRmVoipPortPktToPcmGain,'zxAnEponRmVoipProfileApplyTable':zxAnEponRmVoipProfileApplyTable,'zxAnEponRmVoipProfileApplyEntry':zxAnEponRmVoipProfileApplyEntry,'zxAnEponRmVoipCurrIpProfileIdx':zxAnEponRmVoipCurrIpProfileIdx,'zxAnEponRmVoipCurrVlanProfileIdx':zxAnEponRmVoipCurrVlanProfileIdx,'zxAnEponRmVoipCurrProtocolProfileType':zxAnEponRmVoipCurrProtocolProfileType,'zxAnEponRmVoipCurrProtocolProfileIdx':zxAnEponRmVoipCurrProtocolProfileIdx,'zxAnEponRmVoipCurrFaxProfileIdx':zxAnEponRmVoipCurrFaxProfileIdx,'zxAnEponRmVoipSipAttrTable':zxAnEponRmVoipSipAttrTable,'zxAnEponRmVoipSipAttrEntry':zxAnEponRmVoipSipAttrEntry,'zxAnEponRmVoipSipActiveProxyServer':zxAnEponRmVoipSipActiveProxyServer,'zxAnEponRmVoipSipDigitMapTable':zxAnEponRmVoipSipDigitMapTable,'zxAnEponRmVoipSipDigitMapEntry':zxAnEponRmVoipSipDigitMapEntry,'zxEponRmVoipSipDigitMap':zxEponRmVoipSipDigitMap,'zxAnEponOnuVoipPresentingTable':zxAnEponOnuVoipPresentingTable,'zxAnEponOnuVoipPresentingEntry':zxAnEponOnuVoipPresentingEntry,'zxAnEponOnuVoipPresentingCallNbrState':zxAnEponOnuVoipPresentingCallNbrState,'zxAnEponOnuVoipPresentingCallNbrType':zxAnEponOnuVoipPresentingCallNbrType,'zxAnEponOnuVoipTimerConfigTable':zxAnEponOnuVoipTimerConfigTable,'zxAnEponOnuVoipTimerConfigEntry':zxAnEponOnuVoipTimerConfigEntry,'zxAnEponOnuVoipTimerConfigDml':zxAnEponOnuVoipTimerConfigDml,'zxAnEponOnuVoipTimerConfigDms':zxAnEponOnuVoipTimerConfigDms,'zxAnEponOnuVoipStatsTable':zxAnEponOnuVoipStatsTable,'zxAnEponOnuVoipStatsEntry':zxAnEponOnuVoipStatsEntry,'zxAnEponOnuVoipRxPkts':zxAnEponOnuVoipRxPkts,'zxAnEponOnuVoipTxPkts':zxAnEponOnuVoipTxPkts,'zxAnEponOnuVoipAverageDelay':zxAnEponOnuVoipAverageDelay,'zxAnEponOnuVoipAverageJitter':zxAnEponOnuVoipAverageJitter,'zxAnEponOnuVoipLoss':zxAnEponOnuVoipLoss,'zxAnEponRmUniVoipRxMediaDataRate':zxAnEponRmUniVoipRxMediaDataRate,'zxAnEponRmUniVoipTxMediaDataRate':zxAnEponRmUniVoipTxMediaDataRate,'zxAnEponRmUniVoipCurCallDuration':zxAnEponRmUniVoipCurCallDuration,'zxAnEponRmUniVoipTotCallDuration':zxAnEponRmUniVoipTotCallDuration,'zxAnEponRmUniVoipCallTimes':zxAnEponRmUniVoipCallTimes,'zxAnEponOnuVoipOtherConfigTable':zxAnEponOnuVoipOtherConfigTable,'zxAnEponOnuVoipOtherConfigEntry':zxAnEponOnuVoipOtherConfigEntry,'zxAnEponOnuVoipComfortableNoise':zxAnEponOnuVoipComfortableNoise,'zxAnEponOnuVoipSilenceDetection':zxAnEponOnuVoipSilenceDetection,'zxAnEponOnuVoipEchoCanceller':zxAnEponOnuVoipEchoCanceller,'zxAnEponOnuVoipDtmpTransferMode':zxAnEponOnuVoipDtmpTransferMode,'zxAnEponRmOnuVoipSrvPerfTable':zxAnEponRmOnuVoipSrvPerfTable,'zxAnEponRmOnuVoipSrvPerfEntry':zxAnEponRmOnuVoipSrvPerfEntry,'zxAnEponRmOnuVoipRxSignalMsg':zxAnEponRmOnuVoipRxSignalMsg,'zxAnEponRmOnuVoipTxSignalMsg':zxAnEponRmOnuVoipTxSignalMsg,'zxAnEponRmOnuVoipLossSignalMsg':zxAnEponRmOnuVoipLossSignalMsg,'zxAnEponRmOnuVoipReTxSignalMsg':zxAnEponRmOnuVoipReTxSignalMsg,'zxAnEponRmOnuVoipErrSignalMsg':zxAnEponRmOnuVoipErrSignalMsg,'zxAnEponRmOnuVoipUnknowSignalMsg':zxAnEponRmOnuVoipUnknowSignalMsg,'zxAnEponOnuCapabilityExtTable':zxAnEponOnuCapabilityExtTable,'zxAnEponOnuCapabilityExtEntry':zxAnEponOnuCapabilityExtEntry,'zxAnEponOnuType':zxAnEponOnuType,'zxAnEponOnuMultiLlid':zxAnEponOnuMultiLlid,'zxAnEponOnuProtection':zxAnEponOnuProtection,'zxAnEponOnuPonPorts':zxAnEponOnuPonPorts,'zxAnEponOnuSlots':zxAnEponOnuSlots,'zxAnEponOnuBatteryBackupStatus':zxAnEponOnuBatteryBackupStatus,'zxAnEponOnuIsSupportIpv6':zxAnEponOnuIsSupportIpv6,'zxAnEponOnuPwrSdSupportMode':zxAnEponOnuPwrSdSupportMode,'zxAnEponOnuSlaNumber':zxAnEponOnuSlaNumber,'zxAnEponOnuInterfaceTable':zxAnEponOnuInterfaceTable,'zxAnEponOnuInterfaceEntry':zxAnEponOnuInterfaceEntry,_AM:zxAnEponOnuInterfaceType,'zxAnEponOnuInterfaceNum':zxAnEponOnuInterfaceNum,'zxAnEponMduCardTable':zxAnEponMduCardTable,'zxAnEponMduCardEntry':zxAnEponMduCardEntry,'zxAnEponMduCardOperStatus':zxAnEponMduCardOperStatus,'zxAnEponMduCardAdminStatus':zxAnEponMduCardAdminStatus,'zxAnEponMduSnmpParamMgmt':zxAnEponMduSnmpParamMgmt,'zxAnEponMduSnmpParamTable':zxAnEponMduSnmpParamTable,'zxAnEponMduSnmpParamEntry':zxAnEponMduSnmpParamEntry,'zxEponMduSnmpVersion':zxEponMduSnmpVersion,'zxEponMduSnmpServicePort':zxEponMduSnmpServicePort,'zxEponMduSnmpTrapPort':zxEponMduSnmpTrapPort,'zxEponMduSnmpReadCommunity':zxEponMduSnmpReadCommunity,'zxEponMduSnmpWriteCommunity':zxEponMduSnmpWriteCommunity,'zxEponMduSnmpTrapHostTable':zxEponMduSnmpTrapHostTable,'zxEponMduSnmpTrapHostEntry':zxEponMduSnmpTrapHostEntry,_AN:zxEponMduSnmpTrapHostIndex,'zxEponMduSnmpTrapHostIpAddr':zxEponMduSnmpTrapHostIpAddr,'zxEponMduSnmpTrapHostSnmpVer':zxEponMduSnmpTrapHostSnmpVer,'zxEponMduSnmpTrapHostCommunity':zxEponMduSnmpTrapHostCommunity,'zxEponMduSnmpTrapHostMinEventLevel':zxEponMduSnmpTrapHostMinEventLevel,'zxEponMduSnmpTrapHostEnable':zxEponMduSnmpTrapHostEnable,'zxEponMduSnmpTrapHostRowStatus':zxEponMduSnmpTrapHostRowStatus,'zxAnEponOnuMVlanSwitchTable':zxAnEponOnuMVlanSwitchTable,'zxAnEponOnuMVlanSwitchEntry':zxAnEponOnuMVlanSwitchEntry,_AO:zxAnEponOnuMVlan,_AP:zxAnEponOnuIptvUserVlan,'zxAnEponOnuMVlanSwitchRowStatus':zxAnEponOnuMVlanSwitchRowStatus,'zxAnEponOnuPortTable':zxAnEponOnuPortTable,'zxAnEponOnuPortEntry':zxAnEponOnuPortEntry,'zxAnEponOnuPortLoopbackDetectStatus':zxAnEponOnuPortLoopbackDetectStatus,'zxAnEponOnuPortLoopbackAutoSdEn':zxAnEponOnuPortLoopbackAutoSdEn,'zxAnEponOnuLlidQueueTable':zxAnEponOnuLlidQueueTable,'zxAnEponOnuLlidQueueEntry':zxAnEponOnuLlidQueueEntry,_AQ:zxAnEponOnuLlid,'zxAnEponOnuLlidQueue1WrrWeight':zxAnEponOnuLlidQueue1WrrWeight,'zxAnEponOnuLlidQueue2WrrWeight':zxAnEponOnuLlidQueue2WrrWeight,'zxAnEponOnuLlidQueue3WrrWeight':zxAnEponOnuLlidQueue3WrrWeight,'zxAnEponOnuLlidQueue4WrrWeight':zxAnEponOnuLlidQueue4WrrWeight,'zxAnEponOnuLlidQueue5WrrWeight':zxAnEponOnuLlidQueue5WrrWeight,'zxAnEponOnuLlidQueue6WrrWeight':zxAnEponOnuLlidQueue6WrrWeight,'zxAnEponOnuLlidQueue7WrrWeight':zxAnEponOnuLlidQueue7WrrWeight,'zxAnEponOnuLlidQueue8WrrWeight':zxAnEponOnuLlidQueue8WrrWeight,'zxAnEponOnuPonIfTable':zxAnEponOnuPonIfTable,'zxAnEponOnuPonIfEntry':zxAnEponOnuPonIfEntry,'zxAnEponOnuActivePonIf':zxAnEponOnuActivePonIf,'zxAnEponOnuSlaMgmt':zxAnEponOnuSlaMgmt,'zxAnEponOnuSlaProfileIdxNext':zxAnEponOnuSlaProfileIdxNext,'zxAnEponOnuSlaProfileTable':zxAnEponOnuSlaProfileTable,'zxAnEponOnuSlaProfileEntry':zxAnEponOnuSlaProfileEntry,_p:zxAnEponOnuSlaProfileIndex,'zxAnEponOnuSlaProfileName':zxAnEponOnuSlaProfileName,'zxAnEponOnuServiceDbaEnable':zxAnEponOnuServiceDbaEnable,'zxAnEponOnuBestEffortSchedulingScheme':zxAnEponOnuBestEffortSchedulingScheme,'zxAnEponOnuHighPriorityBoundary':zxAnEponOnuHighPriorityBoundary,'zxAnEponOnuServiceDbaCycleLength':zxAnEponOnuServiceDbaCycleLength,'zxAnEponOnuSlaServiceIdxNext':zxAnEponOnuSlaServiceIdxNext,'zxAnEponOnuSlaProfileRowStatus':zxAnEponOnuSlaProfileRowStatus,'zxAnEponOnuServiceQueueTable':zxAnEponOnuServiceQueueTable,'zxAnEponOnuServiceQueueEntry':zxAnEponOnuServiceQueueEntry,_AR:zxAnEponOnuSlaServiceIdx,'zxAnEponOnuServiceName':zxAnEponOnuServiceName,'zxAnEponOnuQueueId':zxAnEponOnuQueueId,'zxAnEponOnuServiceFixedPktSize':zxAnEponOnuServiceFixedPktSize,'zxAnEponOnuServiceFixedBandwidth':zxAnEponOnuServiceFixedBandwidth,'zxAnEponOnuServiceAssuredBandwidth':zxAnEponOnuServiceAssuredBandwidth,'zxAnEponOnuServiceBestEffortBandwidth':zxAnEponOnuServiceBestEffortBandwidth,'zxAnEponOnuServiceWrrWeight':zxAnEponOnuServiceWrrWeight,'zxAnEponOnuServiceRowStatus':zxAnEponOnuServiceRowStatus,'zxAnEponOnuSlaProfileApplyTable':zxAnEponOnuSlaProfileApplyTable,'zxAnEponOnuSlaProfileApplyEntry':zxAnEponOnuSlaProfileApplyEntry,'zxAnEponOnuCurrSlaProfileIdx':zxAnEponOnuCurrSlaProfileIdx,'zxAnEponOnuHoldoverTable':zxAnEponOnuHoldoverTable,'zxAnEponOnuHoldoverEntry':zxAnEponOnuHoldoverEntry,'zxAnEponOnuHoldoverState':zxAnEponOnuHoldoverState,'zxAnEponOnuHoldoverTime':zxAnEponOnuHoldoverTime,'zxAnEponOnuAlarmMgmt':zxAnEponOnuAlarmMgmt,'zxAnEponOnuLvlAlarmCtrlTable':zxAnEponOnuLvlAlarmCtrlTable,'zxAnEponOnuLvlAlarmCtrlEntry':zxAnEponOnuLvlAlarmCtrlEntry,_AS:zxAnEponOnuLvlAlarmCode,'zxAnEponOnuLvlAlarmEnable':zxAnEponOnuLvlAlarmEnable,'zxAnEponOnuLvlAlarmThreshold':zxAnEponOnuLvlAlarmThreshold,'zxAnEponOnuLvlAlarmRestoreThreshold':zxAnEponOnuLvlAlarmRestoreThreshold,'zxAnEponOnuPonAlarmCtrlTable':zxAnEponOnuPonAlarmCtrlTable,'zxAnEponOnuPonAlarmCtrlEntry':zxAnEponOnuPonAlarmCtrlEntry,_AT:zxAnEponOnuPonAlarmCode,'zxAnEponOnuPonAlarmEnable':zxAnEponOnuPonAlarmEnable,'zxAnEponOnuPonAlarmThreshold':zxAnEponOnuPonAlarmThreshold,'zxAnEponOnuPonAlarmRestoreThreshold':zxAnEponOnuPonAlarmRestoreThreshold,'zxAnEponOnuUniAlarmCtrlTable':zxAnEponOnuUniAlarmCtrlTable,'zxAnEponOnuUniAlarmCtrlEntry':zxAnEponOnuUniAlarmCtrlEntry,_AU:zxAnEponOnuUniAlarmCode,'zxAnEponOnuUniAlarmEnable':zxAnEponOnuUniAlarmEnable,'zxAnEponOnuUniAlarmThreshold':zxAnEponOnuUniAlarmThreshold,'zxAnEponOnuUniAlarmRestoreThresh':zxAnEponOnuUniAlarmRestoreThresh,'zxAnEponOnuVersionMgmt':zxAnEponOnuVersionMgmt,'zxAnEponOnuVersionTable':zxAnEponOnuVersionTable,'zxAnEponOnuVersionEntry':zxAnEponOnuVersionEntry,_q:zxAnEponOnuVersionId,'zxAnEponOnuVersionFileName':zxAnEponOnuVersionFileName,'zxAnEponOnuVersionType':zxAnEponOnuVersionType,'zxAnEponOnuVersionTag':zxAnEponOnuVersionTag,'zxAnEponOnuVersionBuildTime':zxAnEponOnuVersionBuildTime,'zxAnEponOnuVersionUpdateTable':zxAnEponOnuVersionUpdateTable,'zxAnEponOnuVersionUpdateEntry':zxAnEponOnuVersionUpdateEntry,'zxAnEponOnuVersionUpdateOnuType':zxAnEponOnuVersionUpdateOnuType,'zxAnEponOnuVersionUpdateLocType':zxAnEponOnuVersionUpdateLocType,'zxAnEponOnuVersionUpdateSlotId':zxAnEponOnuVersionUpdateSlotId,'zxAnEponOnuVersionUpdateOltId':zxAnEponOnuVersionUpdateOltId,'zxAnEponOnuVersionUpdateOnuList':zxAnEponOnuVersionUpdateOnuList,'zxAnEponOnuVersionUpdateAction':zxAnEponOnuVersionUpdateAction,'zxAnEponOnuVersionUpdateStatusTable':zxAnEponOnuVersionUpdateStatusTable,'zxAnEponOnuVersionUpdateStatusEntry':zxAnEponOnuVersionUpdateStatusEntry,'zxAnEponOnuVersionUpdateState':zxAnEponOnuVersionUpdateState,'zxAnEponOnuVersionUpdateAbortReason':zxAnEponOnuVersionUpdateAbortReason,'zxAnEponOnuVersionUpdateErrCode':zxAnEponOnuVersionUpdateErrCode,'zxAnEponOnuVersionUpdateErrMsg':zxAnEponOnuVersionUpdateErrMsg,'zxAnEponOnuVersionUpdateProgress':zxAnEponOnuVersionUpdateProgress,'zxAnEponOnuCurrentUsedVersionName':zxAnEponOnuCurrentUsedVersionName,'zxAnEponOnuCurrentUsedVersionTime':zxAnEponOnuCurrentUsedVersionTime,'zxAnEponOnuUpdatingVersionName':zxAnEponOnuUpdatingVersionName,'zxAnEponOnuUpdatingVersionTime':zxAnEponOnuUpdatingVersionTime,'zxAnEponOnuVersionActionTable':zxAnEponOnuVersionActionTable,'zxAnEponOnuVersionActionEntry':zxAnEponOnuVersionActionEntry,_AW:zxAnEponOnuVersionImageIndex,'zxAnEponOnuVersionImageAction':zxAnEponOnuVersionImageAction,'zxAnEponOnuVersionImageCommitState':zxAnEponOnuVersionImageCommitState,'zxAnEponOnuVersionImageActiveState':zxAnEponOnuVersionImageActiveState,'zxAnEponOnuVersionImageValidState':zxAnEponOnuVersionImageValidState,'zxAnEponOnuPonMacShapingMgmt':zxAnEponOnuPonMacShapingMgmt,'zxAnEponOnuPonMacShapingTable':zxAnEponOnuPonMacShapingTable,'zxAnEponOnuPonMacShapingEntry':zxAnEponOnuPonMacShapingEntry,'zxAnEponOnuShappingAdminStatus':zxAnEponOnuShappingAdminStatus,'zxAnEponOnuShappingCir':zxAnEponOnuShappingCir,'zxAnEponOnuShappingCbs':zxAnEponOnuShappingCbs,'zxAnEponOnuPonMacBufferTable':zxAnEponOnuPonMacBufferTable,'zxAnEponOnuPonMacBufferEntry':zxAnEponOnuPonMacBufferEntry,'zxAnEponOnuPonMacDsBufferAdminStatus':zxAnEponOnuPonMacDsBufferAdminStatus,'zxAnEponOnuPonMacDsBufferOperStatus':zxAnEponOnuPonMacDsBufferOperStatus,'zxAnEponOnuPonMacDsConfBufferSize':zxAnEponOnuPonMacDsConfBufferSize,'zxAnEponOnuPonMacDsActBufferSize':zxAnEponOnuPonMacDsActBufferSize,'zxAnEponOnuPonMacUsBufferAdminStatus':zxAnEponOnuPonMacUsBufferAdminStatus,'zxAnEponOnuPonMacUsBufferOperStatus':zxAnEponOnuPonMacUsBufferOperStatus,'zxAnEponOnuPonMacUsConfBufferSize':zxAnEponOnuPonMacUsConfBufferSize,'zxAnEponOnuPonMacUsActBufferSize':zxAnEponOnuPonMacUsActBufferSize,'zxAnEponOnuPonMacBufferCapabilityTable':zxAnEponOnuPonMacBufferCapabilityTable,'zxAnEponOnuPonMacBufferCapabilityEntry':zxAnEponOnuPonMacBufferCapabilityEntry,'zxAnEponOnuPonMacBufferCapability':zxAnEponOnuPonMacBufferCapability,'zxAnEponOnuPonMacMinDsBufferSize':zxAnEponOnuPonMacMinDsBufferSize,'zxAnEponOnuPonMacMaxDsBufferSize':zxAnEponOnuPonMacMaxDsBufferSize,'zxAnEponOnuPonMacMinUsBufferSize':zxAnEponOnuPonMacMinUsBufferSize,'zxAnEponOnuPonMacMaxUsBufferSize':zxAnEponOnuPonMacMaxUsBufferSize,'zxAnEponOnuUniMacTable':zxAnEponOnuUniMacTable,'zxAnEponOnuUniMacEntry':zxAnEponOnuUniMacEntry,_AX:zxAnEponOnuUniVlanId,_AY:zxAnEponOnuUniMacSequenceNo,'zxAnEponOnuUniMacType':zxAnEponOnuUniMacType,'zxAnEponOnuUniMacAddress':zxAnEponOnuUniMacAddress,'zxAnEponOnuMgmtIpDHCPCfgTable':zxAnEponOnuMgmtIpDHCPCfgTable,'zxAnEponOnuMgmtIpDHCPCfgEntry':zxAnEponOnuMgmtIpDHCPCfgEntry,'zxAnEponOnuMgmtIpDHCPCfgVlan':zxAnEponOnuMgmtIpDHCPCfgVlan,'zxAnEponOnuMgmtIpDHCPCfgPriority':zxAnEponOnuMgmtIpDHCPCfgPriority,'zxAnEponOnuMgmtIpDHCPCfgEnableState':zxAnEponOnuMgmtIpDHCPCfgEnableState,'zxAnEponOnuMgmtIpDHCPCfgState':zxAnEponOnuMgmtIpDHCPCfgState,'zxAnEponRmOnuWanMgmt':zxAnEponRmOnuWanMgmt,'zxAnEponRmWanPrfTable':zxAnEponRmWanPrfTable,'zxAnEponRmWanPrfEntry':zxAnEponRmWanPrfEntry,_AZ:zxAnEponRmWanPrfName,'zxAnEponRmWanPrfWorkMode':zxAnEponRmWanPrfWorkMode,'zxAnEponRmWanPrfSrvType':zxAnEponRmWanPrfSrvType,'zxAnEponRmWanPrfIpStackMode':zxAnEponRmWanPrfIpStackMode,'zxAnEponRmWanPrfNatNum':zxAnEponRmWanPrfNatNum,'zxAnEponRmWanPrfTransTagMode':zxAnEponRmWanPrfTransTagMode,'zxAnEponRmWanPrfTagTpid':zxAnEponRmWanPrfTagTpid,'zxAnEponRmWanPrfTagVid':zxAnEponRmWanPrfTagVid,'zxAnEponRmWanPrfTagPrior':zxAnEponRmWanPrfTagPrior,'zxAnEponRmWanPrfMaxTransUnit':zxAnEponRmWanPrfMaxTransUnit,'zxAnEponRmWanPrfMVid':zxAnEponRmWanPrfMVid,'zxAnEponRmWanPrfBindLanPortList':zxAnEponRmWanPrfBindLanPortList,'zxAnEponRmWanPrfBindSsidList':zxAnEponRmWanPrfBindSsidList,'zxAnEponRmWanPrfRowStatus':zxAnEponRmWanPrfRowStatus,'zxAnEponRmOnuWanConfTable':zxAnEponRmOnuWanConfTable,'zxAnEponRmOnuWanConfEntry':zxAnEponRmOnuWanConfEntry,_Aa:zxAnEponRmOnuWanPortId,'zxAnEponRmOnuWanPrfName':zxAnEponRmOnuWanPrfName,'zxAnEponRmOnuWanIpAllocationMode':zxAnEponRmOnuWanIpAllocationMode,'zxAnEponRmOnuWanIpAddr':zxAnEponRmOnuWanIpAddr,'zxAnEponRmOnuWanIpMask':zxAnEponRmOnuWanIpMask,'zxAnEponRmOnuWanIpGateway':zxAnEponRmOnuWanIpGateway,'zxAnEponRmOnuWanPriDnsSvrIp':zxAnEponRmOnuWanPriDnsSvrIp,'zxAnEponRmOnuWanSecDnsSvrIp':zxAnEponRmOnuWanSecDnsSvrIp,'zxAnEponRmOnuWanPppoeAuthMode':zxAnEponRmOnuWanPppoeAuthMode,'zxAnEponRmOnuWanPppoeUserName':zxAnEponRmOnuWanPppoeUserName,'zxAnEponRmOnuWanPppoePassword':zxAnEponRmOnuWanPppoePassword,'zxAnEponRmOnuWanPppoePrxyNum':zxAnEponRmOnuWanPppoePrxyNum,'zxAnEponRmOnuWanPppoePrxyUserNum':zxAnEponRmOnuWanPppoePrxyUserNum,'zxAnEponRmOnuWanPortUpTime':zxAnEponRmOnuWanPortUpTime,'zxAnEponRmOnuWanConfRowStatus':zxAnEponRmOnuWanConfRowStatus,'zxAnEponRmOnuWanGlobalConfTable':zxAnEponRmOnuWanGlobalConfTable,'zxAnEponRmOnuWanGlobalConfEntry':zxAnEponRmOnuWanGlobalConfEntry,'zxAnEponRmOnuWanGlbMaxUserNum':zxAnEponRmOnuWanGlbMaxUserNum,'zxAnEponOnuPowerSavingMgmt':zxAnEponOnuPowerSavingMgmt,'zxAnEponOnuPowerSavingTable':zxAnEponOnuPowerSavingTable,'zxAnEponOnuPowerSavingEntry':zxAnEponOnuPowerSavingEntry,'zxAnEponOnuPwrSaveEnable':zxAnEponOnuPwrSaveEnable,'zxAnEponOnuPwrSaveSleepMode':zxAnEponOnuPwrSaveSleepMode,'zxAnEponOnuPwrSaveSleepConfMode':zxAnEponOnuPwrSaveSleepConfMode,'zxAnEponOnuPwrSaveEarlyWakeUp':zxAnEponOnuPwrSaveEarlyWakeUp,'zxAnEponOnuPwrSaveEarlyWakeUpEn':zxAnEponOnuPwrSaveEarlyWakeUpEn,'zxAnEponOnuPwrSaveSleepDuration':zxAnEponOnuPwrSaveSleepDuration,'zxAnEponOnuPwrSaveWakeUpDuration':zxAnEponOnuPwrSaveWakeUpDuration,'zxAnEponOnuPwrSaveMaxRefreshTime':zxAnEponOnuPwrSaveMaxRefreshTime,'zxAnEponOnuProtectMgmt':zxAnEponOnuProtectMgmt,'zxAnOnuProtectConfTable':zxAnOnuProtectConfTable,'zxAnOnuProtectConfEntry':zxAnOnuProtectConfEntry,'zxAnOnuProtectLosTimeByOptSignal':zxAnOnuProtectLosTimeByOptSignal,'zxAnOnuProtectLosTimeByMpcp':zxAnOnuProtectLosTimeByMpcp,'zxAnEponOnuExtendedActionMgmt':zxAnEponOnuExtendedActionMgmt,'zxAnEponOnuActionTable':zxAnEponOnuActionTable,'zxAnEponOnuActionEntry':zxAnEponOnuActionEntry,'zxAnEponOnuAction':zxAnEponOnuAction,'zxAnEponOnuSaveActionTable':zxAnEponOnuSaveActionTable,'zxAnEponOnuSaveActionEntry':zxAnEponOnuSaveActionEntry,'zxAnEponOnuSaveAction':zxAnEponOnuSaveAction,'zxAnEponOnuSetHGMACCodeTable':zxAnEponOnuSetHGMACCodeTable,'zxAnEponOnuSetHGMACCodeEntry':zxAnEponOnuSetHGMACCodeEntry,'zxAnEponOnuHGMACCode':zxAnEponOnuHGMACCode,'zxAnEponOnuHGMACVlanTable':zxAnEponOnuHGMACVlanTable,'zxAnEponOnuHGMACVlanEntry':zxAnEponOnuHGMACVlanEntry,'zxAnEponOnuHGVlan':zxAnEponOnuHGVlan,'zxAnEponOnuHGStateTable':zxAnEponOnuHGStateTable,'zxAnEponOnuHGStateEntry':zxAnEponOnuHGStateEntry,'zxAnEponOnuHGMAC':zxAnEponOnuHGMAC,'zxEponOnuHGState':zxEponOnuHGState,'zxAnEponOnuStdAttrMgmt':zxAnEponOnuStdAttrMgmt,'zxAnEponOnuPhyMgmtTable':zxAnEponOnuPhyMgmtTable,'zxAnEponOnuPhyMgmtEntry':zxAnEponOnuPhyMgmtEntry,'zxAnEponOnuPhyAdminState':zxAnEponOnuPhyAdminState,'zxAnEponOnuAutoNegAttrTable':zxAnEponOnuAutoNegAttrTable,'zxAnEponOnuAutoNegAttrEntry':zxAnEponOnuAutoNegAttrEntry,'zxAnEponOnuAutoNegAdminState':zxAnEponOnuAutoNegAdminState,'zxAnEponOnuAutoNegCapability':zxAnEponOnuAutoNegCapability,'zxAnEponOnuAutoNegCapAdvertised':zxAnEponOnuAutoNegCapAdvertised,'zxAnEponOnuEthIfConfDuplexSpeed':zxAnEponOnuEthIfConfDuplexSpeed,'zxAnEponOnuEthIfActualDuplex':zxAnEponOnuEthIfActualDuplex,'zxAnEponOnuEthIfActualSpeed':zxAnEponOnuEthIfActualSpeed,'zxAnEponOnuFecMgmtTable':zxAnEponOnuFecMgmtTable,'zxAnEponOnuFecMgmtEntry':zxAnEponOnuFecMgmtEntry,'zxAnEponOnuFecAbility':zxAnEponOnuFecAbility,'zxAnEponOnuFecMode':zxAnEponOnuFecMode,'zxAnEponOnuStdActionMgmt':zxAnEponOnuStdActionMgmt,'zxAnEponOnuAutoNegActionTable':zxAnEponOnuAutoNegActionTable,'zxAnEponOnuAutoNegActionEntry':zxAnEponOnuAutoNegActionEntry,'zxAnEponOnuAutoNegAction':zxAnEponOnuAutoNegAction,'zxAnEponOnuDbaAttrMgmt':zxAnEponOnuDbaAttrMgmt,'zxAnEponOnuDbaQueueThresholdsTable':zxAnEponOnuDbaQueueThresholdsTable,'zxAnEponOnuDbaQueueThresholdsEntry':zxAnEponOnuDbaQueueThresholdsEntry,_Ax:zxAnEponOnuDbaQueueSetIndex,'zxAnEponOnuDbaQueueThresholds1':zxAnEponOnuDbaQueueThresholds1,'zxAnEponOnuDbaQueueThresholds2':zxAnEponOnuDbaQueueThresholds2,'zxAnEponOnuDbaQueueThresholds3':zxAnEponOnuDbaQueueThresholds3,'zxAnEponOnuDbaQueueThresholds4':zxAnEponOnuDbaQueueThresholds4,'zxAnEponOnuDbaQueueThresholds5':zxAnEponOnuDbaQueueThresholds5,'zxAnEponOnuDbaQueueThresholds6':zxAnEponOnuDbaQueueThresholds6,'zxAnEponOnuDbaQueueThresholds7':zxAnEponOnuDbaQueueThresholds7,'zxAnEponOnuDbaQueueThresholds8':zxAnEponOnuDbaQueueThresholds8,'zxAnEponOnuDbaQueueSetActiveTable':zxAnEponOnuDbaQueueSetActiveTable,'zxAnEponOnuDbaQueueSetActiveEntry':zxAnEponOnuDbaQueueSetActiveEntry,'zxAnEponOnuDbaQueueSetList':zxAnEponOnuDbaQueueSetList,'zxAnEponOnuProfileMgmt':zxAnEponOnuProfileMgmt,'zxAnEponOnuProfileIndexNextTable':zxAnEponOnuProfileIndexNextTable,'zxAnEponOnuProfileIndexNextEntry':zxAnEponOnuProfileIndexNextEntry,'zxAnEponOnuClassMarkingConditionIdNext':zxAnEponOnuClassMarkingConditionIdNext,'zxAnEponOnuClassMarkingRuleIdNext':zxAnEponOnuClassMarkingRuleIdNext,'zxAnEponOnuPfmncStatis':zxAnEponOnuPfmncStatis,'zxAnEponOnuPfmncStatisTable':zxAnEponOnuPfmncStatisTable,'zxAnEponOnuPfmncStatisEntry':zxAnEponOnuPfmncStatisEntry,'portType':portType,'parameter1':parameter1,'parameter2':parameter2,'parameter3':parameter3,'parameter4':parameter4,'parameter5':parameter5,'parameter6':parameter6,'parameter7':parameter7,'parameter8':parameter8,'parameter9':parameter9,'parameter10':parameter10,'parameter11':parameter11,'parameter12':parameter12,'parameter13':parameter13,'zxAnEponRmPerfConfTable':zxAnEponRmPerfConfTable,'zxAnEponRmPerfConfEntry':zxAnEponRmPerfConfEntry,_a:zxAnEponRmPerfOnuPortType,'zxAnEponRmPerfOnuHisStatInterval':zxAnEponRmPerfOnuHisStatInterval,'zxAnEponRmPerfConfRowStatus':zxAnEponRmPerfConfRowStatus,'zxAnEponRmEthCurPerfTable':zxAnEponRmEthCurPerfTable,'zxAnEponRmEthCurPerfEntry':zxAnEponRmEthCurPerfEntry,'zxAnEponRmCurDsDropEvents':zxAnEponRmCurDsDropEvents,'zxAnEponRmCurDsOctets':zxAnEponRmCurDsOctets,'zxAnEponRmCurDsPkts':zxAnEponRmCurDsPkts,'zxAnEponRmCurDsBcastPkts':zxAnEponRmCurDsBcastPkts,'zxAnEponRmCurDsMcastPkts':zxAnEponRmCurDsMcastPkts,'zxAnEponRmCurDsCrcErrPkts':zxAnEponRmCurDsCrcErrPkts,'zxAnEponRmCurDsUndersizePkts':zxAnEponRmCurDsUndersizePkts,'zxAnEponRmCurDsOversizePkts':zxAnEponRmCurDsOversizePkts,'zxAnEponRmCurDsFragments':zxAnEponRmCurDsFragments,'zxAnEponRmCurDsJabbers':zxAnEponRmCurDsJabbers,'zxAnEponRmCurDsPkts64Octets':zxAnEponRmCurDsPkts64Octets,'zxAnEponRmCurDs65To127Octets':zxAnEponRmCurDs65To127Octets,'zxAnEponRmCurDs128To255Octets':zxAnEponRmCurDs128To255Octets,'zxAnEponRmCurDs256To511Octets':zxAnEponRmCurDs256To511Octets,'zxAnEponRmCurDs512To1023Octets':zxAnEponRmCurDs512To1023Octets,'zxAnEponRmCurDs1024To1518Octets':zxAnEponRmCurDs1024To1518Octets,'zxAnEponRmCurDsDiscards':zxAnEponRmCurDsDiscards,'zxAnEponRmCurDsErrors':zxAnEponRmCurDsErrors,'zxAnEponRmCurUsDropEvents':zxAnEponRmCurUsDropEvents,'zxAnEponRmCurUsOctets':zxAnEponRmCurUsOctets,'zxAnEponRmCurUsPkts':zxAnEponRmCurUsPkts,'zxAnEponRmCurUsBcastPkts':zxAnEponRmCurUsBcastPkts,'zxAnEponRmCurUsMcastPkts':zxAnEponRmCurUsMcastPkts,'zxAnEponRmCurUsCrcErrPkts':zxAnEponRmCurUsCrcErrPkts,'zxAnEponRmCurUsUndersizePkts':zxAnEponRmCurUsUndersizePkts,'zxAnEponRmCurUsOversizePkts':zxAnEponRmCurUsOversizePkts,'zxAnEponRmCurUsFragments':zxAnEponRmCurUsFragments,'zxAnEponRmCurUsJabbers':zxAnEponRmCurUsJabbers,'zxAnEponRmCurUsPkts64Octets':zxAnEponRmCurUsPkts64Octets,'zxAnEponRmCurUs65To127Octets':zxAnEponRmCurUs65To127Octets,'zxAnEponRmCurUs128To255Octets':zxAnEponRmCurUs128To255Octets,'zxAnEponRmCurUs256To511Octets':zxAnEponRmCurUs256To511Octets,'zxAnEponRmCurUs512To1023Octets':zxAnEponRmCurUs512To1023Octets,'zxAnEponRmCurUs1024To1518Octets':zxAnEponRmCurUs1024To1518Octets,'zxAnEponRmCurUsDiscards':zxAnEponRmCurUsDiscards,'zxAnEponRmCurUsErrors':zxAnEponRmCurUsErrors,'zxAnEponRmCurPortStatusChanges':zxAnEponRmCurPortStatusChanges,'zxAnEponRmEthHisPerfTable':zxAnEponRmEthHisPerfTable,'zxAnEponRmEthHisPerfEntry':zxAnEponRmEthHisPerfEntry,_Ay:zxAnEponRmEthHisIntervalNo,'zxAnEponRmHisDsDropEvents':zxAnEponRmHisDsDropEvents,'zxAnEponRmHisDsOctets':zxAnEponRmHisDsOctets,'zxAnEponRmHisDsPkts':zxAnEponRmHisDsPkts,'zxAnEponRmHisDsBcastPkts':zxAnEponRmHisDsBcastPkts,'zxAnEponRmHisDsMcastPkts':zxAnEponRmHisDsMcastPkts,'zxAnEponRmHisDsCrcErrPkts':zxAnEponRmHisDsCrcErrPkts,'zxAnEponRmHisDsUndersizePkts':zxAnEponRmHisDsUndersizePkts,'zxAnEponRmHisDsOversizePkts':zxAnEponRmHisDsOversizePkts,'zxAnEponRmHisDsFragments':zxAnEponRmHisDsFragments,'zxAnEponRmHisDsJabbers':zxAnEponRmHisDsJabbers,'zxAnEponRmHisDsPkts64Octets':zxAnEponRmHisDsPkts64Octets,'zxAnEponRmHisDs65To127Octets':zxAnEponRmHisDs65To127Octets,'zxAnEponRmHisDs128To255Octets':zxAnEponRmHisDs128To255Octets,'zxAnEponRmHisDs256To511Octets':zxAnEponRmHisDs256To511Octets,'zxAnEponRmHisDs512To1023Octets':zxAnEponRmHisDs512To1023Octets,'zxAnEponRmHisDs1024To1518Octets':zxAnEponRmHisDs1024To1518Octets,'zxAnEponRmHisDsDiscards':zxAnEponRmHisDsDiscards,'zxAnEponRmHisDsErrors':zxAnEponRmHisDsErrors,'zxAnEponRmHisUsDropEvents':zxAnEponRmHisUsDropEvents,'zxAnEponRmHisUsOctets':zxAnEponRmHisUsOctets,'zxAnEponRmHisUsPkts':zxAnEponRmHisUsPkts,'zxAnEponRmHisUsBcastPkts':zxAnEponRmHisUsBcastPkts,'zxAnEponRmHisUsMcastPkts':zxAnEponRmHisUsMcastPkts,'zxAnEponRmHisUsCrcErrPkts':zxAnEponRmHisUsCrcErrPkts,'zxAnEponRmHisUsUndersizePkts':zxAnEponRmHisUsUndersizePkts,'zxAnEponRmHisUsOversizePkts':zxAnEponRmHisUsOversizePkts,'zxAnEponRmHisUsFragments':zxAnEponRmHisUsFragments,'zxAnEponRmHisUsJabbers':zxAnEponRmHisUsJabbers,'zxAnEponRmHisUsPkts64Octets':zxAnEponRmHisUsPkts64Octets,'zxAnEponRmHisUs65To127Octets':zxAnEponRmHisUs65To127Octets,'zxAnEponRmHisUs128To255Octets':zxAnEponRmHisUs128To255Octets,'zxAnEponRmHisUs256To511Octets':zxAnEponRmHisUs256To511Octets,'zxAnEponRmHisUs512To1023Octets':zxAnEponRmHisUs512To1023Octets,'zxAnEponRmHisUs1024To1518Octets':zxAnEponRmHisUs1024To1518Octets,'zxAnEponRmHisUsDiscards':zxAnEponRmHisUsDiscards,'zxAnEponRmHisUsErrors':zxAnEponRmHisUsErrors,'zxAnEponRmHisPortStatusChanges':zxAnEponRmHisPortStatusChanges,'zxAnPtpExtOamMgmt':zxAnPtpExtOamMgmt,'zxAnPtpExtOamTable':zxAnPtpExtOamTable,'zxAnPtpExtOamEntry':zxAnPtpExtOamEntry,_Az:zxAnPtpIfIndex,'zxAnPtpExtOamAdminStatus':zxAnPtpExtOamAdminStatus,'zxAnEponOnuCustomMgmt':zxAnEponOnuCustomMgmt,'zxAnEponOnuTkMgmt':zxAnEponOnuTkMgmt,'zxAnEponOnuTkAttrMgmt':zxAnEponOnuTkAttrMgmt,'zxAnEponOnuTkGlobalTable':zxAnEponOnuTkGlobalTable,'zxAnEponOnuTkGlobalEntry':zxAnEponOnuTkGlobalEntry,'zxAnEponOnuTkFirmwareVer':zxAnEponOnuTkFirmwareVer,'zxAnEponOnuTkModeName':zxAnEponOnuTkModeName,'zxAnEponOnuTkPortTable':zxAnEponOnuTkPortTable,'zxAnEponOnuTkPortEntry':zxAnEponOnuTkPortEntry,'zxAnEponOnuTkPortOperStatus':zxAnEponOnuTkPortOperStatus,'zxAnEponOnuTkPortAutoNegStatus':zxAnEponOnuTkPortAutoNegStatus,'zxAnEponOnuTkPortFlowCtrlStatus':zxAnEponOnuTkPortFlowCtrlStatus,'zxAnEponOnuTkPortDuplexMode':zxAnEponOnuTkPortDuplexMode,'zxAnEponOnuTkPortAdminStatus':zxAnEponOnuTkPortAdminStatus,'zxAnEponOnuTkLoopbackTable':zxAnEponOnuTkLoopbackTable,'zxAnEponOnuTkLoopbackEntry':zxAnEponOnuTkLoopbackEntry,'zxAnEponOnuTkLoopbackAdminStatus':zxAnEponOnuTkLoopbackAdminStatus,'zxAnEponOnuTkLinkBlockTable':zxAnEponOnuTkLinkBlockTable,'zxAnEponOnuTkLinkBlockEntry':zxAnEponOnuTkLinkBlockEntry,'zxAnEponOnuTkLinkBlockAdminStatus':zxAnEponOnuTkLinkBlockAdminStatus,'zxAnEponOnuTkLinkBlockOamType':zxAnEponOnuTkLinkBlockOamType,'zxAnEponOnuTkOpticalCtrlTable':zxAnEponOnuTkOpticalCtrlTable,'zxAnEponOnuTkOpticalCtrlEntry':zxAnEponOnuTkOpticalCtrlEntry,'zxAnEponOnuTkOpticalBlockStatus':zxAnEponOnuTkOpticalBlockStatus,'zxAnEponOnuTkOpticalBlockDurationTime':zxAnEponOnuTkOpticalBlockDurationTime,'zxAnEponOnuTkOpticalBlockOamType':zxAnEponOnuTkOpticalBlockOamType,'zxAnEponOnuTkRstpCtrlTable':zxAnEponOnuTkRstpCtrlTable,'zxAnEponOnuTkRstpCtrlEntry':zxAnEponOnuTkRstpCtrlEntry,'zxAnEponOnuTkRstpAdminStatus':zxAnEponOnuTkRstpAdminStatus,'zxAnEponOnuTkMacLearningTable':zxAnEponOnuTkMacLearningTable,'zxAnEponOnuTkMacLearningEntry':zxAnEponOnuTkMacLearningEntry,'zxAnEponOnuTkMacLearningMaxNum':zxAnEponOnuTkMacLearningMaxNum,'zxAnEponOnuTkMacLearningOamType':zxAnEponOnuTkMacLearningOamType,'zxAnEponOnuTkSnoopingTable':zxAnEponOnuTkSnoopingTable,'zxAnEponOnuTkSnoopingEntry':zxAnEponOnuTkSnoopingEntry,'zxAnEponOnuTkSnoopingCtrl':zxAnEponOnuTkSnoopingCtrl,'zxAnEponOnuTkSnoopingRobustCnt':zxAnEponOnuTkSnoopingRobustCnt,'zxAnEponOnuTkSnoopingLsmq':zxAnEponOnuTkSnoopingLsmq,'zxAnEponOnuTkSnoopingMaxGroupNum':zxAnEponOnuTkSnoopingMaxGroupNum,'zxAnEponOnuTkIgmpTable':zxAnEponOnuTkIgmpTable,'zxAnEponOnuTkIgmpEntry':zxAnEponOnuTkIgmpEntry,_A_:zxAnEponOnuTkIgmpVlanId,_B0:zxAnEponOnuTkIgmpIpAddr,'zxAnEponOnuTkIgmpPortList':zxAnEponOnuTkIgmpPortList,'zxAnEponOnuTkLoopDetectTable':zxAnEponOnuTkLoopDetectTable,'zxAnEponOnuTkLoopDetectEntry':zxAnEponOnuTkLoopDetectEntry,'zxAnEponOnuTkLoopDetectAdminStatus':zxAnEponOnuTkLoopDetectAdminStatus,'zxAnEponOnuTkLoopDetectInterval':zxAnEponOnuTkLoopDetectInterval,'zxAnEponOnuTkLoopDetectOamType':zxAnEponOnuTkLoopDetectOamType,'zxAnEponOnuTkPortShapingTable':zxAnEponOnuTkPortShapingTable,'zxAnEponOnuTkPortShapingEntry':zxAnEponOnuTkPortShapingEntry,'zxAnEponOnuTkPortDsShapingAdminStatus':zxAnEponOnuTkPortDsShapingAdminStatus,'zxAnEponOnuTkPortDsShapingRate':zxAnEponOnuTkPortDsShapingRate,'zxAnEponOnuTkPortDsShapingOamType':zxAnEponOnuTkPortDsShapingOamType,'zxAnEponOnuTkActionMgmt':zxAnEponOnuTkActionMgmt,'zxAnEponOnuTkRestoreActionTable':zxAnEponOnuTkRestoreActionTable,'zxAnEponOnuTkRestoreActionEntry':zxAnEponOnuTkRestoreActionEntry,'zxAnEponOnuTkRestoreFactorySettings':zxAnEponOnuTkRestoreFactorySettings,'zxAnEponOnuTkRestoreOamType':zxAnEponOnuTkRestoreOamType,'zxAnEponOnuTkUpdateVerTable':zxAnEponOnuTkUpdateVerTable,'zxAnEponOnuTkUpdateVerEntry':zxAnEponOnuTkUpdateVerEntry,'zxAnEponOnuTkVerType':zxAnEponOnuTkVerType,'zxAnEponOnuTkVerName':zxAnEponOnuTkVerName,'zxAnEponOnuTkUpdateStatus':zxAnEponOnuTkUpdateStatus,'zxAnEponOnuTkUpdateProgress':zxAnEponOnuTkUpdateProgress,'zxAnEponOnuTkOnuAckCode':zxAnEponOnuTkOnuAckCode,'zxAnEponOnuTkErrorCode':zxAnEponOnuTkErrorCode,'zxAnEponOnuTkUpdattingVerName':zxAnEponOnuTkUpdattingVerName,'zxAnEponOnuTkAutoUpdateVerTable':zxAnEponOnuTkAutoUpdateVerTable,'zxAnEponOnuTkAutoUpdateVerEntry':zxAnEponOnuTkAutoUpdateVerEntry,_B1:zxAnEponOltIfIndex,'zxAnEponOnuTkAutoUpdateAdminStatus':zxAnEponOnuTkAutoUpdateAdminStatus,'zxAnEponOnuTkVerActiveMode':zxAnEponOnuTkVerActiveMode,'zxAnEponOnuTkStatisticMgmt':zxAnEponOnuTkStatisticMgmt,'zxAnEponOnuTkGlobalStatTable':zxAnEponOnuTkGlobalStatTable,'zxAnEponOnuTkGlobalStatEntry':zxAnEponOnuTkGlobalStatEntry,'zxAnEponOnuTkGlobalStatResetCounter':zxAnEponOnuTkGlobalStatResetCounter,'zxAnEponOnuTkGlobalStatOamType':zxAnEponOnuTkGlobalStatOamType,'zxAnEponOnuTkGlobalStatTxRegReq':zxAnEponOnuTkGlobalStatTxRegReq,'zxAnEponOnuTkGlobalStatRxReg':zxAnEponOnuTkGlobalStatRxReg,'zxAnEponOnuTkGlobalStatTxRegAck':zxAnEponOnuTkGlobalStatTxRegAck,'zxAnEponOnuTkGlobalStatRxGateFrames':zxAnEponOnuTkGlobalStatRxGateFrames,'zxAnEponOnuTkGlobalStatTxReportFrames':zxAnEponOnuTkGlobalStatTxReportFrames,'zxAnEponOnuTkPortStatTable':zxAnEponOnuTkPortStatTable,'zxAnEponOnuTkPortStatEntry':zxAnEponOnuTkPortStatEntry,'zxAnEponOnuTkPortStatResetCounter':zxAnEponOnuTkPortStatResetCounter,'zxAnEponOnuTkPortStatOamType':zxAnEponOnuTkPortStatOamType,'zxAnEponOnuTkPortStatTxFrames':zxAnEponOnuTkPortStatTxFrames,'zxAnEponOnuTkPortStatTxBytes':zxAnEponOnuTkPortStatTxBytes,'zxAnEponOnuTkPortStatTxMulticast':zxAnEponOnuTkPortStatTxMulticast,'zxAnEponOnuTkPortStatTxBroadcast':zxAnEponOnuTkPortStatTxBroadcast,'zxAnEponOnuTkPortStatTxDropedFrames':zxAnEponOnuTkPortStatTxDropedFrames,'zxAnEponOnuTkPortStatRxFrames':zxAnEponOnuTkPortStatRxFrames,'zxAnEponOnuTkPortStatRxBytes':zxAnEponOnuTkPortStatRxBytes,'zxAnEponOnuTkPortStatRxMulticast':zxAnEponOnuTkPortStatRxMulticast,'zxAnEponOnuTkPortStatRxBroadcast':zxAnEponOnuTkPortStatRxBroadcast,'zxAnEponOnuTkPortStatRxOversizeFrames':zxAnEponOnuTkPortStatRxOversizeFrames,'zxAnEponOnuTkPortStatRxUnderSizeFrames':zxAnEponOnuTkPortStatRxUnderSizeFrames,'zxAnEponOnuTkPortStatRxCrcFrames':zxAnEponOnuTkPortStatRxCrcFrames})