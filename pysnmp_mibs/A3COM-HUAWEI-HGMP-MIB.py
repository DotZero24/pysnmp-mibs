_m='hwNDPPortNbPortName'
_l='hwNDPPortNbDeviceId'
_k='enable'
_j='disable'
_i='hgmpNTDPTopEdgeIndex'
_h='hgmpNTDPTopEdgeStartDevID'
_g='hgmpNTDPTopHashIndex'
_f='hgmpNTDPCacheDeviceID'
_e='hgmpNTDPCacheHashIndex'
_d='hgmpNTDPInterfaceIfIndex'
_c='hgmpMemberPriPortProto'
_b='hgmpMemberDevId'
_a='hgmpBlacklistDeviceId'
_Z='hgmpWhitelistNbIndex'
_Y='read-create'
_X='roleBAKSW'
_W='roleMEMBERSW'
_V='roleCMDSW'
_U='hgmpMemberResetMAC'
_T='normal'
_S='MacAddress'
_R='IpAddress'
_Q='Counter32'
_P='hgmpNTDPCacheClusterRole'
_O='hwNDPIfIndex'
_N='hgmpWhitelistDeviceId'
_M='roleUNISW'
_L='roleCASW'
_K='not-accessible'
_J='hgmpStackMemberDeviceId'
_I='hgmpGrpMemberDeviceId'
_H='true'
_G='false'
_F='OctetString'
_E='A3COM-HUAWEI-HGMP-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
huaweiUtility,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','huaweiUtility')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_Q,'Counter64','Gauge32',_C,_R,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_S,'PhysAddress','RowStatus','TextualConvention')
hwCluster=ModuleIdentity((1,3,6,1,4,1,43,45,1,6,7))
_HwClusterObject_ObjectIdentity=ObjectIdentity
hwClusterObject=_HwClusterObject_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,7,1))
if mibBuilder.loadTexts:hwClusterObject.setStatus(_A)
_HgmpEventsV2_ObjectIdentity=ObjectIdentity
hgmpEventsV2=_HgmpEventsV2_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,7,1,0))
if mibBuilder.loadTexts:hgmpEventsV2.setStatus(_A)
class _HgmpSetVLANSecurity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noSecurity',0),('security',1)))
_HgmpSetVLANSecurity_Type.__name__=_C
_HgmpSetVLANSecurity_Object=MibScalar
hgmpSetVLANSecurity=_HgmpSetVLANSecurity_Object((1,3,6,1,4,1,43,45,1,6,7,1,1),_HgmpSetVLANSecurity_Type())
hgmpSetVLANSecurity.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpSetVLANSecurity.setStatus(_A)
class _HgmpHandShakeInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HgmpHandShakeInterval_Type.__name__=_C
_HgmpHandShakeInterval_Object=MibScalar
hgmpHandShakeInterval=_HgmpHandShakeInterval_Object((1,3,6,1,4,1,43,45,1,6,7,1,2),_HgmpHandShakeInterval_Type())
hgmpHandShakeInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpHandShakeInterval.setStatus(_A)
class _HgmpHandShakeHoldtime_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HgmpHandShakeHoldtime_Type.__name__=_C
_HgmpHandShakeHoldtime_Object=MibScalar
hgmpHandShakeHoldtime=_HgmpHandShakeHoldtime_Object((1,3,6,1,4,1,43,45,1,6,7,1,3),_HgmpHandShakeHoldtime_Type())
hgmpHandShakeHoldtime.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpHandShakeHoldtime.setStatus(_A)
class _HgmpGrpMemberTableChange_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HgmpGrpMemberTableChange_Type.__name__=_C
_HgmpGrpMemberTableChange_Object=MibScalar
hgmpGrpMemberTableChange=_HgmpGrpMemberTableChange_Object((1,3,6,1,4,1,43,45,1,6,7,1,4),_HgmpGrpMemberTableChange_Type())
hgmpGrpMemberTableChange.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpGrpMemberTableChange.setStatus(_A)
class _HgmpMemberDisconRate_Type(Integer32):defaultValue=0
_HgmpMemberDisconRate_Type.__name__=_C
_HgmpMemberDisconRate_Object=MibScalar
hgmpMemberDisconRate=_HgmpMemberDisconRate_Object((1,3,6,1,4,1,43,45,1,6,7,1,5),_HgmpMemberDisconRate_Type())
hgmpMemberDisconRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpMemberDisconRate.setStatus(_A)
class _HgmpCmdLanswitchFlag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_HgmpCmdLanswitchFlag_Type.__name__=_C
_HgmpCmdLanswitchFlag_Object=MibScalar
hgmpCmdLanswitchFlag=_HgmpCmdLanswitchFlag_Object((1,3,6,1,4,1,43,45,1,6,7,1,6),_HgmpCmdLanswitchFlag_Type())
hgmpCmdLanswitchFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpCmdLanswitchFlag.setStatus(_A)
class _HgmpCmdClusterName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_HgmpCmdClusterName_Type.__name__=_F
_HgmpCmdClusterName_Object=MibScalar
hgmpCmdClusterName=_HgmpCmdClusterName_Object((1,3,6,1,4,1,43,45,1,6,7,1,7),_HgmpCmdClusterName_Type())
hgmpCmdClusterName.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpCmdClusterName.setStatus(_A)
_HgmpMngPriIpSegCMIP_Type=IpAddress
_HgmpMngPriIpSegCMIP_Object=MibScalar
hgmpMngPriIpSegCMIP=_HgmpMngPriIpSegCMIP_Object((1,3,6,1,4,1,43,45,1,6,7,1,8),_HgmpMngPriIpSegCMIP_Type())
hgmpMngPriIpSegCMIP.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpMngPriIpSegCMIP.setStatus(_A)
_HgmpMngPriIpMask_Type=IpAddress
_HgmpMngPriIpMask_Object=MibScalar
hgmpMngPriIpMask=_HgmpMngPriIpMask_Object((1,3,6,1,4,1,43,45,1,6,7,1,9),_HgmpMngPriIpMask_Type())
hgmpMngPriIpMask.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpMngPriIpMask.setStatus(_A)
_HgmpFtpServer_Type=IpAddress
_HgmpFtpServer_Object=MibScalar
hgmpFtpServer=_HgmpFtpServer_Object((1,3,6,1,4,1,43,45,1,6,7,1,10),_HgmpFtpServer_Type())
hgmpFtpServer.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpFtpServer.setStatus(_A)
_HgmpTftpServer_Type=IpAddress
_HgmpTftpServer_Object=MibScalar
hgmpTftpServer=_HgmpTftpServer_Object((1,3,6,1,4,1,43,45,1,6,7,1,11),_HgmpTftpServer_Type())
hgmpTftpServer.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpTftpServer.setStatus(_A)
_HgmpSnmpHost_Type=IpAddress
_HgmpSnmpHost_Object=MibScalar
hgmpSnmpHost=_HgmpSnmpHost_Object((1,3,6,1,4,1,43,45,1,6,7,1,12),_HgmpSnmpHost_Type())
hgmpSnmpHost.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpSnmpHost.setStatus(_A)
_HgmpLogHost_Type=IpAddress
_HgmpLogHost_Object=MibScalar
hgmpLogHost=_HgmpLogHost_Object((1,3,6,1,4,1,43,45,1,6,7,1,13),_HgmpLogHost_Type())
hgmpLogHost.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpLogHost.setStatus(_A)
_HgmpGrpMemberTable_Object=MibTable
hgmpGrpMemberTable=_HgmpGrpMemberTable_Object((1,3,6,1,4,1,43,45,1,6,7,1,14))
if mibBuilder.loadTexts:hgmpGrpMemberTable.setStatus(_A)
_HgmpGrpMemberEntry_Object=MibTableRow
hgmpGrpMemberEntry=_HgmpGrpMemberEntry_Object((1,3,6,1,4,1,43,45,1,6,7,1,14,1))
hgmpGrpMemberEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:hgmpGrpMemberEntry.setStatus(_A)
class _HgmpGrpMemberDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HgmpGrpMemberDeviceId_Type.__name__=_F
_HgmpGrpMemberDeviceId_Object=MibTableColumn
hgmpGrpMemberDeviceId=_HgmpGrpMemberDeviceId_Object((1,3,6,1,4,1,43,45,1,6,7,1,14,1,1),_HgmpGrpMemberDeviceId_Type())
hgmpGrpMemberDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpGrpMemberDeviceId.setStatus(_A)
class _HgmpGrpMemberSerial_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2047))
_HgmpGrpMemberSerial_Type.__name__=_C
_HgmpGrpMemberSerial_Object=MibTableColumn
hgmpGrpMemberSerial=_HgmpGrpMemberSerial_Object((1,3,6,1,4,1,43,45,1,6,7,1,14,1,2),_HgmpGrpMemberSerial_Type())
hgmpGrpMemberSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpGrpMemberSerial.setStatus(_A)
_HgmpGrpMemberIpAddr_Type=IpAddress
_HgmpGrpMemberIpAddr_Object=MibTableColumn
hgmpGrpMemberIpAddr=_HgmpGrpMemberIpAddr_Object((1,3,6,1,4,1,43,45,1,6,7,1,14,1,3),_HgmpGrpMemberIpAddr_Type())
hgmpGrpMemberIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpGrpMemberIpAddr.setStatus(_A)
class _HgmpGrpMemberName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HgmpGrpMemberName_Type.__name__=_F
_HgmpGrpMemberName_Object=MibTableColumn
hgmpGrpMemberName=_HgmpGrpMemberName_Object((1,3,6,1,4,1,43,45,1,6,7,1,14,1,4),_HgmpGrpMemberName_Type())
hgmpGrpMemberName.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpGrpMemberName.setStatus(_A)
_HgmpGrpMemberPassword_Type=OctetString
_HgmpGrpMemberPassword_Object=MibTableColumn
hgmpGrpMemberPassword=_HgmpGrpMemberPassword_Object((1,3,6,1,4,1,43,45,1,6,7,1,14,1,5),_HgmpGrpMemberPassword_Type())
hgmpGrpMemberPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpGrpMemberPassword.setStatus(_A)
_HgmpGrpMemberPlatform_Type=OctetString
_HgmpGrpMemberPlatform_Object=MibTableColumn
hgmpGrpMemberPlatform=_HgmpGrpMemberPlatform_Object((1,3,6,1,4,1,43,45,1,6,7,1,14,1,6),_HgmpGrpMemberPlatform_Type())
hgmpGrpMemberPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpGrpMemberPlatform.setStatus(_A)
class _HgmpGrpMemberStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),('fault',1)))
_HgmpGrpMemberStatus_Type.__name__=_C
_HgmpGrpMemberStatus_Object=MibTableColumn
hgmpGrpMemberStatus=_HgmpGrpMemberStatus_Object((1,3,6,1,4,1,43,45,1,6,7,1,14,1,7),_HgmpGrpMemberStatus_Type())
hgmpGrpMemberStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpGrpMemberStatus.setStatus(_A)
_HgmpGrpMemberDisconCount_Type=Integer32
_HgmpGrpMemberDisconCount_Object=MibTableColumn
hgmpGrpMemberDisconCount=_HgmpGrpMemberDisconCount_Object((1,3,6,1,4,1,43,45,1,6,7,1,14,1,8),_HgmpGrpMemberDisconCount_Type())
hgmpGrpMemberDisconCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpGrpMemberDisconCount.setStatus(_A)
_HgmpGrpMemberEnrollTime_Type=Integer32
_HgmpGrpMemberEnrollTime_Object=MibTableColumn
hgmpGrpMemberEnrollTime=_HgmpGrpMemberEnrollTime_Object((1,3,6,1,4,1,43,45,1,6,7,1,14,1,9),_HgmpGrpMemberEnrollTime_Type())
hgmpGrpMemberEnrollTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpGrpMemberEnrollTime.setStatus(_A)
_HgmpGrpMemberOperate_Type=RowStatus
_HgmpGrpMemberOperate_Object=MibTableColumn
hgmpGrpMemberOperate=_HgmpGrpMemberOperate_Object((1,3,6,1,4,1,43,45,1,6,7,1,14,1,10),_HgmpGrpMemberOperate_Type())
hgmpGrpMemberOperate.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpGrpMemberOperate.setStatus(_A)
_HgmpMemberResetTable_Object=MibTable
hgmpMemberResetTable=_HgmpMemberResetTable_Object((1,3,6,1,4,1,43,45,1,6,7,1,15))
if mibBuilder.loadTexts:hgmpMemberResetTable.setStatus(_A)
_HgmpMemberResetEntry_Object=MibTableRow
hgmpMemberResetEntry=_HgmpMemberResetEntry_Object((1,3,6,1,4,1,43,45,1,6,7,1,15,1))
hgmpMemberResetEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:hgmpMemberResetEntry.setStatus(_A)
class _HgmpMemberResetMAC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_HgmpMemberResetMAC_Type.__name__=_F
_HgmpMemberResetMAC_Object=MibTableColumn
hgmpMemberResetMAC=_HgmpMemberResetMAC_Object((1,3,6,1,4,1,43,45,1,6,7,1,15,1,1),_HgmpMemberResetMAC_Type())
hgmpMemberResetMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpMemberResetMAC.setStatus(_A)
class _HgmpMemberEraseflash_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,65535)));namedValues=NamedValues(*(('noErase',0),('erase',1),('cannotget',65535)))
_HgmpMemberEraseflash_Type.__name__=_C
_HgmpMemberEraseflash_Object=MibTableColumn
hgmpMemberEraseflash=_HgmpMemberEraseflash_Object((1,3,6,1,4,1,43,45,1,6,7,1,15,1,2),_HgmpMemberEraseflash_Type())
hgmpMemberEraseflash.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpMemberEraseflash.setStatus(_A)
class _HgmpClusterRole_Type(Integer32):defaultValue=17;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,16,17)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_L,16),(_M,17)))
_HgmpClusterRole_Type.__name__=_C
_HgmpClusterRole_Object=MibScalar
hgmpClusterRole=_HgmpClusterRole_Object((1,3,6,1,4,1,43,45,1,6,7,1,16),_HgmpClusterRole_Type())
hgmpClusterRole.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpClusterRole.setStatus(_A)
_HgmpClusterMaxPoolNum_Type=Integer32
_HgmpClusterMaxPoolNum_Object=MibScalar
hgmpClusterMaxPoolNum=_HgmpClusterMaxPoolNum_Object((1,3,6,1,4,1,43,45,1,6,7,1,17),_HgmpClusterMaxPoolNum_Type())
hgmpClusterMaxPoolNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpClusterMaxPoolNum.setStatus(_A)
class _HgmpClusterCmdSwMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_HgmpClusterCmdSwMac_Type.__name__=_F
_HgmpClusterCmdSwMac_Object=MibScalar
hgmpClusterCmdSwMac=_HgmpClusterCmdSwMac_Object((1,3,6,1,4,1,43,45,1,6,7,1,18),_HgmpClusterCmdSwMac_Type())
hgmpClusterCmdSwMac.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpClusterCmdSwMac.setStatus(_A)
class _HgmpRun_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_HgmpRun_Type.__name__=_C
_HgmpRun_Object=MibScalar
hgmpRun=_HgmpRun_Object((1,3,6,1,4,1,43,45,1,6,7,1,19),_HgmpRun_Type())
hgmpRun.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpRun.setStatus(_A)
_HgmpProtocolMac_ObjectIdentity=ObjectIdentity
hgmpProtocolMac=_HgmpProtocolMac_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,7,1,22))
class _HgmpClusterProtocolMac_Type(MacAddress):defaultHexValue='0180C200000A'
_HgmpClusterProtocolMac_Type.__name__=_S
_HgmpClusterProtocolMac_Object=MibScalar
hgmpClusterProtocolMac=_HgmpClusterProtocolMac_Object((1,3,6,1,4,1,43,45,1,6,7,1,22,1),_HgmpClusterProtocolMac_Type())
hgmpClusterProtocolMac.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpClusterProtocolMac.setStatus(_A)
_HgmpTopologyManagement_ObjectIdentity=ObjectIdentity
hgmpTopologyManagement=_HgmpTopologyManagement_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,7,1,23))
_HgmpWhitelistTable_Object=MibTable
hgmpWhitelistTable=_HgmpWhitelistTable_Object((1,3,6,1,4,1,43,45,1,6,7,1,23,1))
if mibBuilder.loadTexts:hgmpWhitelistTable.setStatus(_A)
_HgmpWhitelistEntry_Object=MibTableRow
hgmpWhitelistEntry=_HgmpWhitelistEntry_Object((1,3,6,1,4,1,43,45,1,6,7,1,23,1,1))
hgmpWhitelistEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:hgmpWhitelistEntry.setStatus(_A)
class _HgmpWhitelistDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_HgmpWhitelistDeviceId_Type.__name__=_F
_HgmpWhitelistDeviceId_Object=MibTableColumn
hgmpWhitelistDeviceId=_HgmpWhitelistDeviceId_Object((1,3,6,1,4,1,43,45,1,6,7,1,23,1,1,1),_HgmpWhitelistDeviceId_Type())
hgmpWhitelistDeviceId.setMaxAccess(_K)
if mibBuilder.loadTexts:hgmpWhitelistDeviceId.setStatus(_A)
class _HgmpWhitelistSerial_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2047),ValueRangeConstraint(65535,65535))
_HgmpWhitelistSerial_Type.__name__=_C
_HgmpWhitelistSerial_Object=MibTableColumn
hgmpWhitelistSerial=_HgmpWhitelistSerial_Object((1,3,6,1,4,1,43,45,1,6,7,1,23,1,1,2),_HgmpWhitelistSerial_Type())
hgmpWhitelistSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpWhitelistSerial.setStatus(_A)
_HgmpWhitelistRowStatus_Type=RowStatus
_HgmpWhitelistRowStatus_Object=MibTableColumn
hgmpWhitelistRowStatus=_HgmpWhitelistRowStatus_Object((1,3,6,1,4,1,43,45,1,6,7,1,23,1,1,3),_HgmpWhitelistRowStatus_Type())
hgmpWhitelistRowStatus.setMaxAccess(_Y)
if mibBuilder.loadTexts:hgmpWhitelistRowStatus.setStatus(_A)
_HgmpWhitelistNbTable_Object=MibTable
hgmpWhitelistNbTable=_HgmpWhitelistNbTable_Object((1,3,6,1,4,1,43,45,1,6,7,1,23,2))
if mibBuilder.loadTexts:hgmpWhitelistNbTable.setStatus(_A)
_HgmpWhitelistNbEntry_Object=MibTableRow
hgmpWhitelistNbEntry=_HgmpWhitelistNbEntry_Object((1,3,6,1,4,1,43,45,1,6,7,1,23,2,1))
hgmpWhitelistNbEntry.setIndexNames((0,_E,_N),(0,_E,_Z))
if mibBuilder.loadTexts:hgmpWhitelistNbEntry.setStatus(_A)
class _HgmpWhitelistNbIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HgmpWhitelistNbIndex_Type.__name__=_C
_HgmpWhitelistNbIndex_Object=MibTableColumn
hgmpWhitelistNbIndex=_HgmpWhitelistNbIndex_Object((1,3,6,1,4,1,43,45,1,6,7,1,23,2,1,1),_HgmpWhitelistNbIndex_Type())
hgmpWhitelistNbIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hgmpWhitelistNbIndex.setStatus(_A)
class _HgmpWhitelistNbDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_HgmpWhitelistNbDeviceId_Type.__name__=_F
_HgmpWhitelistNbDeviceId_Object=MibTableColumn
hgmpWhitelistNbDeviceId=_HgmpWhitelistNbDeviceId_Object((1,3,6,1,4,1,43,45,1,6,7,1,23,2,1,2),_HgmpWhitelistNbDeviceId_Type())
hgmpWhitelistNbDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpWhitelistNbDeviceId.setStatus(_A)
class _HgmpWhitelistPortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_HgmpWhitelistPortName_Type.__name__=_F
_HgmpWhitelistPortName_Object=MibTableColumn
hgmpWhitelistPortName=_HgmpWhitelistPortName_Object((1,3,6,1,4,1,43,45,1,6,7,1,23,2,1,3),_HgmpWhitelistPortName_Type())
hgmpWhitelistPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpWhitelistPortName.setStatus(_A)
class _HgmpWhitelistNbPortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_HgmpWhitelistNbPortName_Type.__name__=_F
_HgmpWhitelistNbPortName_Object=MibTableColumn
hgmpWhitelistNbPortName=_HgmpWhitelistNbPortName_Object((1,3,6,1,4,1,43,45,1,6,7,1,23,2,1,4),_HgmpWhitelistNbPortName_Type())
hgmpWhitelistNbPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpWhitelistNbPortName.setStatus(_A)
_HgmpBlacklistTable_Object=MibTable
hgmpBlacklistTable=_HgmpBlacklistTable_Object((1,3,6,1,4,1,43,45,1,6,7,1,23,3))
if mibBuilder.loadTexts:hgmpBlacklistTable.setStatus(_A)
_HgmpBlacklistEntry_Object=MibTableRow
hgmpBlacklistEntry=_HgmpBlacklistEntry_Object((1,3,6,1,4,1,43,45,1,6,7,1,23,3,1))
hgmpBlacklistEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:hgmpBlacklistEntry.setStatus(_A)
class _HgmpBlacklistDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_HgmpBlacklistDeviceId_Type.__name__=_F
_HgmpBlacklistDeviceId_Object=MibTableColumn
hgmpBlacklistDeviceId=_HgmpBlacklistDeviceId_Object((1,3,6,1,4,1,43,45,1,6,7,1,23,3,1,1),_HgmpBlacklistDeviceId_Type())
hgmpBlacklistDeviceId.setMaxAccess(_K)
if mibBuilder.loadTexts:hgmpBlacklistDeviceId.setStatus(_A)
class _HgmpBlacklistAccessDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_HgmpBlacklistAccessDeviceId_Type.__name__=_F
_HgmpBlacklistAccessDeviceId_Object=MibTableColumn
hgmpBlacklistAccessDeviceId=_HgmpBlacklistAccessDeviceId_Object((1,3,6,1,4,1,43,45,1,6,7,1,23,3,1,2),_HgmpBlacklistAccessDeviceId_Type())
hgmpBlacklistAccessDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpBlacklistAccessDeviceId.setStatus(_A)
class _HgmpBlacklistAccessPortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_HgmpBlacklistAccessPortName_Type.__name__=_F
_HgmpBlacklistAccessPortName_Object=MibTableColumn
hgmpBlacklistAccessPortName=_HgmpBlacklistAccessPortName_Object((1,3,6,1,4,1,43,45,1,6,7,1,23,3,1,3),_HgmpBlacklistAccessPortName_Type())
hgmpBlacklistAccessPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpBlacklistAccessPortName.setStatus(_A)
_HgmpBlacklistRowStatus_Type=RowStatus
_HgmpBlacklistRowStatus_Object=MibTableColumn
hgmpBlacklistRowStatus=_HgmpBlacklistRowStatus_Object((1,3,6,1,4,1,43,45,1,6,7,1,23,3,1,4),_HgmpBlacklistRowStatus_Type())
hgmpBlacklistRowStatus.setMaxAccess(_Y)
if mibBuilder.loadTexts:hgmpBlacklistRowStatus.setStatus(_A)
_HgmpMemberPriPortTable_Object=MibTable
hgmpMemberPriPortTable=_HgmpMemberPriPortTable_Object((1,3,6,1,4,1,43,45,1,6,7,1,24))
if mibBuilder.loadTexts:hgmpMemberPriPortTable.setStatus(_A)
_HgmpMemberPriPortEntry_Object=MibTableRow
hgmpMemberPriPortEntry=_HgmpMemberPriPortEntry_Object((1,3,6,1,4,1,43,45,1,6,7,1,24,1))
hgmpMemberPriPortEntry.setIndexNames((0,_E,_b),(0,_E,_c))
if mibBuilder.loadTexts:hgmpMemberPriPortEntry.setStatus(_A)
class _HgmpMemberDevId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HgmpMemberDevId_Type.__name__=_F
_HgmpMemberDevId_Object=MibTableColumn
hgmpMemberDevId=_HgmpMemberDevId_Object((1,3,6,1,4,1,43,45,1,6,7,1,24,1,1),_HgmpMemberDevId_Type())
hgmpMemberDevId.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpMemberDevId.setStatus(_A)
_HgmpMemberPriPortProto_Type=Unsigned32
_HgmpMemberPriPortProto_Object=MibTableColumn
hgmpMemberPriPortProto=_HgmpMemberPriPortProto_Object((1,3,6,1,4,1,43,45,1,6,7,1,24,1,2),_HgmpMemberPriPortProto_Type())
hgmpMemberPriPortProto.setMaxAccess(_K)
if mibBuilder.loadTexts:hgmpMemberPriPortProto.setStatus(_A)
_HgmpMemberPriPortProtoDescr_Type=DisplayString
_HgmpMemberPriPortProtoDescr_Object=MibTableColumn
hgmpMemberPriPortProtoDescr=_HgmpMemberPriPortProtoDescr_Object((1,3,6,1,4,1,43,45,1,6,7,1,24,1,3),_HgmpMemberPriPortProtoDescr_Type())
hgmpMemberPriPortProtoDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpMemberPriPortProtoDescr.setStatus(_A)
_HgmpMemberPriPortNum_Type=Unsigned32
_HgmpMemberPriPortNum_Object=MibTableColumn
hgmpMemberPriPortNum=_HgmpMemberPriPortNum_Object((1,3,6,1,4,1,43,45,1,6,7,1,24,1,4),_HgmpMemberPriPortNum_Type())
hgmpMemberPriPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpMemberPriPortNum.setStatus(_A)
_HwStackObject_ObjectIdentity=ObjectIdentity
hwStackObject=_HwStackObject_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,7,2))
if mibBuilder.loadTexts:hwStackObject.setStatus(_A)
_HgmpStackEventsV2_ObjectIdentity=ObjectIdentity
hgmpStackEventsV2=_HgmpStackEventsV2_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,7,2,0))
if mibBuilder.loadTexts:hgmpStackEventsV2.setStatus(_A)
class _HgmpStackMemberTableChange_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HgmpStackMemberTableChange_Type.__name__=_C
_HgmpStackMemberTableChange_Object=MibScalar
hgmpStackMemberTableChange=_HgmpStackMemberTableChange_Object((1,3,6,1,4,1,43,45,1,6,7,2,1),_HgmpStackMemberTableChange_Type())
hgmpStackMemberTableChange.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpStackMemberTableChange.setStatus(_A)
class _HgmpStackMemberDisconRate_Type(Integer32):defaultValue=0
_HgmpStackMemberDisconRate_Type.__name__=_C
_HgmpStackMemberDisconRate_Object=MibScalar
hgmpStackMemberDisconRate=_HgmpStackMemberDisconRate_Object((1,3,6,1,4,1,43,45,1,6,7,2,2),_HgmpStackMemberDisconRate_Type())
hgmpStackMemberDisconRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpStackMemberDisconRate.setStatus(_A)
class _HgmpMainLanswitchFlag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_HgmpMainLanswitchFlag_Type.__name__=_C
_HgmpMainLanswitchFlag_Object=MibScalar
hgmpMainLanswitchFlag=_HgmpMainLanswitchFlag_Object((1,3,6,1,4,1,43,45,1,6,7,2,3),_HgmpMainLanswitchFlag_Type())
hgmpMainLanswitchFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpMainLanswitchFlag.setStatus(_A)
_HgmpStackIpPoolStartIP_Type=IpAddress
_HgmpStackIpPoolStartIP_Object=MibScalar
hgmpStackIpPoolStartIP=_HgmpStackIpPoolStartIP_Object((1,3,6,1,4,1,43,45,1,6,7,2,4),_HgmpStackIpPoolStartIP_Type())
hgmpStackIpPoolStartIP.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpStackIpPoolStartIP.setStatus(_A)
class _HgmpStackIpPoolLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_HgmpStackIpPoolLength_Type.__name__=_C
_HgmpStackIpPoolLength_Object=MibScalar
hgmpStackIpPoolLength=_HgmpStackIpPoolLength_Object((1,3,6,1,4,1,43,45,1,6,7,2,5),_HgmpStackIpPoolLength_Type())
hgmpStackIpPoolLength.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpStackIpPoolLength.setStatus(_A)
_HgmpStackMemberTable_Object=MibTable
hgmpStackMemberTable=_HgmpStackMemberTable_Object((1,3,6,1,4,1,43,45,1,6,7,2,6))
if mibBuilder.loadTexts:hgmpStackMemberTable.setStatus(_A)
_HgmpStackMemberEntry_Object=MibTableRow
hgmpStackMemberEntry=_HgmpStackMemberEntry_Object((1,3,6,1,4,1,43,45,1,6,7,2,6,1))
hgmpStackMemberEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:hgmpStackMemberEntry.setStatus(_A)
class _HgmpStackMemberDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HgmpStackMemberDeviceId_Type.__name__=_F
_HgmpStackMemberDeviceId_Object=MibTableColumn
hgmpStackMemberDeviceId=_HgmpStackMemberDeviceId_Object((1,3,6,1,4,1,43,45,1,6,7,2,6,1,1),_HgmpStackMemberDeviceId_Type())
hgmpStackMemberDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpStackMemberDeviceId.setStatus(_A)
class _HgmpStackMemberSerial_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2047))
_HgmpStackMemberSerial_Type.__name__=_C
_HgmpStackMemberSerial_Object=MibTableColumn
hgmpStackMemberSerial=_HgmpStackMemberSerial_Object((1,3,6,1,4,1,43,45,1,6,7,2,6,1,2),_HgmpStackMemberSerial_Type())
hgmpStackMemberSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpStackMemberSerial.setStatus(_A)
_HgmpStackMemberIpAddr_Type=IpAddress
_HgmpStackMemberIpAddr_Object=MibTableColumn
hgmpStackMemberIpAddr=_HgmpStackMemberIpAddr_Object((1,3,6,1,4,1,43,45,1,6,7,2,6,1,3),_HgmpStackMemberIpAddr_Type())
hgmpStackMemberIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpStackMemberIpAddr.setStatus(_A)
_HgmpStackMemberName_Type=OctetString
_HgmpStackMemberName_Object=MibTableColumn
hgmpStackMemberName=_HgmpStackMemberName_Object((1,3,6,1,4,1,43,45,1,6,7,2,6,1,4),_HgmpStackMemberName_Type())
hgmpStackMemberName.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpStackMemberName.setStatus(_A)
_HgmpStackMemberPassword_Type=OctetString
_HgmpStackMemberPassword_Object=MibTableColumn
hgmpStackMemberPassword=_HgmpStackMemberPassword_Object((1,3,6,1,4,1,43,45,1,6,7,2,6,1,5),_HgmpStackMemberPassword_Type())
hgmpStackMemberPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpStackMemberPassword.setStatus(_A)
_HgmpStackMemberPlatform_Type=OctetString
_HgmpStackMemberPlatform_Object=MibTableColumn
hgmpStackMemberPlatform=_HgmpStackMemberPlatform_Object((1,3,6,1,4,1,43,45,1,6,7,2,6,1,6),_HgmpStackMemberPlatform_Type())
hgmpStackMemberPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpStackMemberPlatform.setStatus(_A)
class _HgmpStackMemberStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),('fault',1)))
_HgmpStackMemberStatus_Type.__name__=_C
_HgmpStackMemberStatus_Object=MibTableColumn
hgmpStackMemberStatus=_HgmpStackMemberStatus_Object((1,3,6,1,4,1,43,45,1,6,7,2,6,1,7),_HgmpStackMemberStatus_Type())
hgmpStackMemberStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpStackMemberStatus.setStatus(_A)
_HgmpStackMemberDisconCount_Type=Integer32
_HgmpStackMemberDisconCount_Object=MibTableColumn
hgmpStackMemberDisconCount=_HgmpStackMemberDisconCount_Object((1,3,6,1,4,1,43,45,1,6,7,2,6,1,8),_HgmpStackMemberDisconCount_Type())
hgmpStackMemberDisconCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpStackMemberDisconCount.setStatus(_A)
_HgmpStackMemberEnrollTime_Type=Integer32
_HgmpStackMemberEnrollTime_Object=MibTableColumn
hgmpStackMemberEnrollTime=_HgmpStackMemberEnrollTime_Object((1,3,6,1,4,1,43,45,1,6,7,2,6,1,9),_HgmpStackMemberEnrollTime_Type())
hgmpStackMemberEnrollTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpStackMemberEnrollTime.setStatus(_A)
class _HgmpStackRole_Type(Integer32):defaultValue=17;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,16,17)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_L,16),(_M,17)))
_HgmpStackRole_Type.__name__=_C
_HgmpStackRole_Object=MibScalar
hgmpStackRole=_HgmpStackRole_Object((1,3,6,1,4,1,43,45,1,6,7,2,7),_HgmpStackRole_Type())
hgmpStackRole.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpStackRole.setStatus(_A)
_HgmpStackMaxPoolNum_Type=Integer32
_HgmpStackMaxPoolNum_Object=MibScalar
hgmpStackMaxPoolNum=_HgmpStackMaxPoolNum_Object((1,3,6,1,4,1,43,45,1,6,7,2,8),_HgmpStackMaxPoolNum_Type())
hgmpStackMaxPoolNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpStackMaxPoolNum.setStatus(_A)
class _HgmpStackMainSwMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_HgmpStackMainSwMac_Type.__name__=_F
_HgmpStackMainSwMac_Object=MibScalar
hgmpStackMainSwMac=_HgmpStackMainSwMac_Object((1,3,6,1,4,1,43,45,1,6,7,2,9),_HgmpStackMainSwMac_Type())
hgmpStackMainSwMac.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpStackMainSwMac.setStatus(_A)
class _HgmpStackIpPoolMask_Type(IpAddress):defaultHexValue='FFFF0000'
_HgmpStackIpPoolMask_Type.__name__=_R
_HgmpStackIpPoolMask_Object=MibScalar
hgmpStackIpPoolMask=_HgmpStackIpPoolMask_Object((1,3,6,1,4,1,43,45,1,6,7,2,10),_HgmpStackIpPoolMask_Type())
hgmpStackIpPoolMask.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpStackIpPoolMask.setStatus(_A)
_HwNTDPObject_ObjectIdentity=ObjectIdentity
hwNTDPObject=_HwNTDPObject_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,7,4))
if mibBuilder.loadTexts:hwNTDPObject.setStatus(_A)
class _HgmpNTDPCollectTopTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HgmpNTDPCollectTopTime_Type.__name__=_C
_HgmpNTDPCollectTopTime_Object=MibScalar
hgmpNTDPCollectTopTime=_HgmpNTDPCollectTopTime_Object((1,3,6,1,4,1,43,45,1,6,7,4,1),_HgmpNTDPCollectTopTime_Type())
hgmpNTDPCollectTopTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpNTDPCollectTopTime.setStatus(_A)
class _HgmpNTDPHopRange_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HgmpNTDPHopRange_Type.__name__=_C
_HgmpNTDPHopRange_Object=MibScalar
hgmpNTDPHopRange=_HgmpNTDPHopRange_Object((1,3,6,1,4,1,43,45,1,6,7,4,2),_HgmpNTDPHopRange_Type())
hgmpNTDPHopRange.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpNTDPHopRange.setStatus(_A)
class _HgmpNTDPRun_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_HgmpNTDPRun_Type.__name__=_C
_HgmpNTDPRun_Object=MibScalar
hgmpNTDPRun=_HgmpNTDPRun_Object((1,3,6,1,4,1,43,45,1,6,7,4,3),_HgmpNTDPRun_Type())
hgmpNTDPRun.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpNTDPRun.setStatus(_A)
class _HgmpNTDPPortDelay_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HgmpNTDPPortDelay_Type.__name__=_C
_HgmpNTDPPortDelay_Object=MibScalar
hgmpNTDPPortDelay=_HgmpNTDPPortDelay_Object((1,3,6,1,4,1,43,45,1,6,7,4,4),_HgmpNTDPPortDelay_Type())
hgmpNTDPPortDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpNTDPPortDelay.setStatus(_A)
class _HgmpNTDPHopDelay_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_HgmpNTDPHopDelay_Type.__name__=_C
_HgmpNTDPHopDelay_Object=MibScalar
hgmpNTDPHopDelay=_HgmpNTDPHopDelay_Object((1,3,6,1,4,1,43,45,1,6,7,4,5),_HgmpNTDPHopDelay_Type())
hgmpNTDPHopDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpNTDPHopDelay.setStatus(_A)
class _HgmpNTDPLastTopCollectDuration_Type(Integer32):defaultValue=0
_HgmpNTDPLastTopCollectDuration_Type.__name__=_C
_HgmpNTDPLastTopCollectDuration_Object=MibScalar
hgmpNTDPLastTopCollectDuration=_HgmpNTDPLastTopCollectDuration_Object((1,3,6,1,4,1,43,45,1,6,7,4,6),_HgmpNTDPLastTopCollectDuration_Type())
hgmpNTDPLastTopCollectDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPLastTopCollectDuration.setStatus(_A)
class _HgmpNTDPCacheChange_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HgmpNTDPCacheChange_Type.__name__=_C
_HgmpNTDPCacheChange_Object=MibScalar
hgmpNTDPCacheChange=_HgmpNTDPCacheChange_Object((1,3,6,1,4,1,43,45,1,6,7,4,7),_HgmpNTDPCacheChange_Type())
hgmpNTDPCacheChange.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPCacheChange.setStatus(_A)
class _HgmpNTDPTOPTableChange_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HgmpNTDPTOPTableChange_Type.__name__=_C
_HgmpNTDPTOPTableChange_Object=MibScalar
hgmpNTDPTOPTableChange=_HgmpNTDPTOPTableChange_Object((1,3,6,1,4,1,43,45,1,6,7,4,8),_HgmpNTDPTOPTableChange_Type())
hgmpNTDPTOPTableChange.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPTOPTableChange.setStatus(_A)
_HgmpNTDPInterfaceTable_Object=MibTable
hgmpNTDPInterfaceTable=_HgmpNTDPInterfaceTable_Object((1,3,6,1,4,1,43,45,1,6,7,4,9))
if mibBuilder.loadTexts:hgmpNTDPInterfaceTable.setStatus(_A)
_HgmpNTDPInterfaceEntry_Object=MibTableRow
hgmpNTDPInterfaceEntry=_HgmpNTDPInterfaceEntry_Object((1,3,6,1,4,1,43,45,1,6,7,4,9,1))
hgmpNTDPInterfaceEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:hgmpNTDPInterfaceEntry.setStatus(_A)
_HgmpNTDPInterfaceIfIndex_Type=Integer32
_HgmpNTDPInterfaceIfIndex_Object=MibTableColumn
hgmpNTDPInterfaceIfIndex=_HgmpNTDPInterfaceIfIndex_Object((1,3,6,1,4,1,43,45,1,6,7,4,9,1,1),_HgmpNTDPInterfaceIfIndex_Type())
hgmpNTDPInterfaceIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPInterfaceIfIndex.setStatus(_A)
class _HgmpNTDPInterfaceEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_HgmpNTDPInterfaceEnable_Type.__name__=_C
_HgmpNTDPInterfaceEnable_Object=MibTableColumn
hgmpNTDPInterfaceEnable=_HgmpNTDPInterfaceEnable_Object((1,3,6,1,4,1,43,45,1,6,7,4,9,1,2),_HgmpNTDPInterfaceEnable_Type())
hgmpNTDPInterfaceEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hgmpNTDPInterfaceEnable.setStatus(_A)
_HgmpNTDPCacheTable_Object=MibTable
hgmpNTDPCacheTable=_HgmpNTDPCacheTable_Object((1,3,6,1,4,1,43,45,1,6,7,4,10))
if mibBuilder.loadTexts:hgmpNTDPCacheTable.setStatus(_A)
_HgmpNTDPCacheEntry_Object=MibTableRow
hgmpNTDPCacheEntry=_HgmpNTDPCacheEntry_Object((1,3,6,1,4,1,43,45,1,6,7,4,10,1))
hgmpNTDPCacheEntry.setIndexNames((0,_E,_e),(0,_E,_f))
if mibBuilder.loadTexts:hgmpNTDPCacheEntry.setStatus(_A)
class _HgmpNTDPCacheHashIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HgmpNTDPCacheHashIndex_Type.__name__=_C
_HgmpNTDPCacheHashIndex_Object=MibTableColumn
hgmpNTDPCacheHashIndex=_HgmpNTDPCacheHashIndex_Object((1,3,6,1,4,1,43,45,1,6,7,4,10,1,1),_HgmpNTDPCacheHashIndex_Type())
hgmpNTDPCacheHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPCacheHashIndex.setStatus(_A)
class _HgmpNTDPCacheDeviceID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HgmpNTDPCacheDeviceID_Type.__name__=_F
_HgmpNTDPCacheDeviceID_Object=MibTableColumn
hgmpNTDPCacheDeviceID=_HgmpNTDPCacheDeviceID_Object((1,3,6,1,4,1,43,45,1,6,7,4,10,1,2),_HgmpNTDPCacheDeviceID_Type())
hgmpNTDPCacheDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPCacheDeviceID.setStatus(_A)
_HgmpNTDPCacheClusterName_Type=OctetString
_HgmpNTDPCacheClusterName_Object=MibTableColumn
hgmpNTDPCacheClusterName=_HgmpNTDPCacheClusterName_Object((1,3,6,1,4,1,43,45,1,6,7,4,10,1,3),_HgmpNTDPCacheClusterName_Type())
hgmpNTDPCacheClusterName.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPCacheClusterName.setStatus(_A)
class _HgmpNTDPCacheClusterRole_Type(Integer32):defaultValue=17;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,16,17)));namedValues=NamedValues(*(('roleCOSW',1),('roleMSW',2),('roleBKSW',3),(_L,16),(_M,17)))
_HgmpNTDPCacheClusterRole_Type.__name__=_C
_HgmpNTDPCacheClusterRole_Object=MibTableColumn
hgmpNTDPCacheClusterRole=_HgmpNTDPCacheClusterRole_Object((1,3,6,1,4,1,43,45,1,6,7,4,10,1,4),_HgmpNTDPCacheClusterRole_Type())
hgmpNTDPCacheClusterRole.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPCacheClusterRole.setStatus(_A)
class _HgmpNTDPCacheCapabilities_Type(Integer32):defaultValue=255
_HgmpNTDPCacheCapabilities_Type.__name__=_C
_HgmpNTDPCacheCapabilities_Object=MibTableColumn
hgmpNTDPCacheCapabilities=_HgmpNTDPCacheCapabilities_Object((1,3,6,1,4,1,43,45,1,6,7,4,10,1,5),_HgmpNTDPCacheCapabilities_Type())
hgmpNTDPCacheCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPCacheCapabilities.setStatus(_A)
_HgmpNTDPCacheVersion_Type=OctetString
_HgmpNTDPCacheVersion_Object=MibTableColumn
hgmpNTDPCacheVersion=_HgmpNTDPCacheVersion_Object((1,3,6,1,4,1,43,45,1,6,7,4,10,1,6),_HgmpNTDPCacheVersion_Type())
hgmpNTDPCacheVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPCacheVersion.setStatus(_A)
_HgmpNTDPCachePlatform_Type=OctetString
_HgmpNTDPCachePlatform_Object=MibTableColumn
hgmpNTDPCachePlatform=_HgmpNTDPCachePlatform_Object((1,3,6,1,4,1,43,45,1,6,7,4,10,1,7),_HgmpNTDPCachePlatform_Type())
hgmpNTDPCachePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPCachePlatform.setStatus(_A)
class _HgmpNTDPCacheMngVLAN_Type(Integer32):defaultValue=1
_HgmpNTDPCacheMngVLAN_Type.__name__=_C
_HgmpNTDPCacheMngVLAN_Object=MibTableColumn
hgmpNTDPCacheMngVLAN=_HgmpNTDPCacheMngVLAN_Object((1,3,6,1,4,1,43,45,1,6,7,4,10,1,8),_HgmpNTDPCacheMngVLAN_Type())
hgmpNTDPCacheMngVLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPCacheMngVLAN.setStatus(_A)
_HgmpNTDPCacheHop_Type=Integer32
_HgmpNTDPCacheHop_Object=MibTableColumn
hgmpNTDPCacheHop=_HgmpNTDPCacheHop_Object((1,3,6,1,4,1,43,45,1,6,7,4,10,1,9),_HgmpNTDPCacheHop_Type())
hgmpNTDPCacheHop.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPCacheHop.setStatus(_A)
_HgmpNTDPTopTable_Object=MibTable
hgmpNTDPTopTable=_HgmpNTDPTopTable_Object((1,3,6,1,4,1,43,45,1,6,7,4,11))
if mibBuilder.loadTexts:hgmpNTDPTopTable.setStatus(_A)
_HgmpNTDPTopEntry_Object=MibTableRow
hgmpNTDPTopEntry=_HgmpNTDPTopEntry_Object((1,3,6,1,4,1,43,45,1,6,7,4,11,1))
hgmpNTDPTopEntry.setIndexNames((0,_E,_g),(0,_E,_h),(0,_E,_i))
if mibBuilder.loadTexts:hgmpNTDPTopEntry.setStatus(_A)
class _HgmpNTDPTopHashIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HgmpNTDPTopHashIndex_Type.__name__=_C
_HgmpNTDPTopHashIndex_Object=MibTableColumn
hgmpNTDPTopHashIndex=_HgmpNTDPTopHashIndex_Object((1,3,6,1,4,1,43,45,1,6,7,4,11,1,1),_HgmpNTDPTopHashIndex_Type())
hgmpNTDPTopHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPTopHashIndex.setStatus(_A)
class _HgmpNTDPTopEdgeStartDevID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HgmpNTDPTopEdgeStartDevID_Type.__name__=_F
_HgmpNTDPTopEdgeStartDevID_Object=MibTableColumn
hgmpNTDPTopEdgeStartDevID=_HgmpNTDPTopEdgeStartDevID_Object((1,3,6,1,4,1,43,45,1,6,7,4,11,1,2),_HgmpNTDPTopEdgeStartDevID_Type())
hgmpNTDPTopEdgeStartDevID.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPTopEdgeStartDevID.setStatus(_A)
class _HgmpNTDPTopEdgeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HgmpNTDPTopEdgeIndex_Type.__name__=_C
_HgmpNTDPTopEdgeIndex_Object=MibTableColumn
hgmpNTDPTopEdgeIndex=_HgmpNTDPTopEdgeIndex_Object((1,3,6,1,4,1,43,45,1,6,7,4,11,1,3),_HgmpNTDPTopEdgeIndex_Type())
hgmpNTDPTopEdgeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPTopEdgeIndex.setStatus(_A)
class _HgmpNTDPTopEdgeEndDevID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HgmpNTDPTopEdgeEndDevID_Type.__name__=_F
_HgmpNTDPTopEdgeEndDevID_Object=MibTableColumn
hgmpNTDPTopEdgeEndDevID=_HgmpNTDPTopEdgeEndDevID_Object((1,3,6,1,4,1,43,45,1,6,7,4,11,1,4),_HgmpNTDPTopEdgeEndDevID_Type())
hgmpNTDPTopEdgeEndDevID.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPTopEdgeEndDevID.setStatus(_A)
class _HgmpNTDPTopEdgeStartPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_HgmpNTDPTopEdgeStartPort_Type.__name__=_F
_HgmpNTDPTopEdgeStartPort_Object=MibTableColumn
hgmpNTDPTopEdgeStartPort=_HgmpNTDPTopEdgeStartPort_Object((1,3,6,1,4,1,43,45,1,6,7,4,11,1,5),_HgmpNTDPTopEdgeStartPort_Type())
hgmpNTDPTopEdgeStartPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPTopEdgeStartPort.setStatus(_A)
class _HgmpNTDPTopEdgeStartPortFullDuplex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('half',0),('full',1)))
_HgmpNTDPTopEdgeStartPortFullDuplex_Type.__name__=_C
_HgmpNTDPTopEdgeStartPortFullDuplex_Object=MibTableColumn
hgmpNTDPTopEdgeStartPortFullDuplex=_HgmpNTDPTopEdgeStartPortFullDuplex_Object((1,3,6,1,4,1,43,45,1,6,7,4,11,1,6),_HgmpNTDPTopEdgeStartPortFullDuplex_Type())
hgmpNTDPTopEdgeStartPortFullDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPTopEdgeStartPortFullDuplex.setStatus(_A)
class _HgmpNTDPTopEdgeStartPortSpeed_Type(Integer32):defaultValue=0
_HgmpNTDPTopEdgeStartPortSpeed_Type.__name__=_C
_HgmpNTDPTopEdgeStartPortSpeed_Object=MibTableColumn
hgmpNTDPTopEdgeStartPortSpeed=_HgmpNTDPTopEdgeStartPortSpeed_Object((1,3,6,1,4,1,43,45,1,6,7,4,11,1,7),_HgmpNTDPTopEdgeStartPortSpeed_Type())
hgmpNTDPTopEdgeStartPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPTopEdgeStartPortSpeed.setStatus(_A)
class _HgmpNTDPTopEdgeEndPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_HgmpNTDPTopEdgeEndPort_Type.__name__=_F
_HgmpNTDPTopEdgeEndPort_Object=MibTableColumn
hgmpNTDPTopEdgeEndPort=_HgmpNTDPTopEdgeEndPort_Object((1,3,6,1,4,1,43,45,1,6,7,4,11,1,8),_HgmpNTDPTopEdgeEndPort_Type())
hgmpNTDPTopEdgeEndPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPTopEdgeEndPort.setStatus(_A)
class _HgmpNTDPTopLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forwarding',1),('blocking',2)))
_HgmpNTDPTopLinkStatus_Type.__name__=_C
_HgmpNTDPTopLinkStatus_Object=MibTableColumn
hgmpNTDPTopLinkStatus=_HgmpNTDPTopLinkStatus_Object((1,3,6,1,4,1,43,45,1,6,7,4,11,1,11),_HgmpNTDPTopLinkStatus_Type())
hgmpNTDPTopLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hgmpNTDPTopLinkStatus.setStatus(_A)
_HwNDPObject_ObjectIdentity=ObjectIdentity
hwNDPObject=_HwNDPObject_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,7,5))
if mibBuilder.loadTexts:hwNDPObject.setStatus(_A)
class _HwNDPStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_j,0),(_k,1)))
_HwNDPStatus_Type.__name__=_C
_HwNDPStatus_Object=MibScalar
hwNDPStatus=_HwNDPStatus_Object((1,3,6,1,4,1,43,45,1,6,7,5,1),_HwNDPStatus_Type())
hwNDPStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwNDPStatus.setStatus(_A)
class _HwNDPHelloTimer_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,254))
_HwNDPHelloTimer_Type.__name__=_C
_HwNDPHelloTimer_Object=MibScalar
hwNDPHelloTimer=_HwNDPHelloTimer_Object((1,3,6,1,4,1,43,45,1,6,7,5,2),_HwNDPHelloTimer_Type())
hwNDPHelloTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:hwNDPHelloTimer.setStatus(_A)
class _HwNDPAgingTime_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,255))
_HwNDPAgingTime_Type.__name__=_C
_HwNDPAgingTime_Object=MibScalar
hwNDPAgingTime=_HwNDPAgingTime_Object((1,3,6,1,4,1,43,45,1,6,7,5,3),_HwNDPAgingTime_Type())
hwNDPAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hwNDPAgingTime.setStatus(_A)
class _HwNDPChange_Type(Counter32):defaultValue=0
_HwNDPChange_Type.__name__=_Q
_HwNDPChange_Object=MibScalar
hwNDPChange=_HwNDPChange_Object((1,3,6,1,4,1,43,45,1,6,7,5,4),_HwNDPChange_Type())
hwNDPChange.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNDPChange.setStatus(_A)
_HwNDPPortTable_Object=MibTable
hwNDPPortTable=_HwNDPPortTable_Object((1,3,6,1,4,1,43,45,1,6,7,5,5))
if mibBuilder.loadTexts:hwNDPPortTable.setStatus(_A)
_HwNDPPortEntry_Object=MibTableRow
hwNDPPortEntry=_HwNDPPortEntry_Object((1,3,6,1,4,1,43,45,1,6,7,5,5,1))
hwNDPPortEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:hwNDPPortEntry.setStatus(_A)
_HwNDPIfIndex_Type=Integer32
_HwNDPIfIndex_Object=MibTableColumn
hwNDPIfIndex=_HwNDPIfIndex_Object((1,3,6,1,4,1,43,45,1,6,7,5,5,1,1),_HwNDPIfIndex_Type())
hwNDPIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNDPIfIndex.setStatus(_A)
class _HwNDPPortStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_j,0),(_k,1)))
_HwNDPPortStatus_Type.__name__=_C
_HwNDPPortStatus_Object=MibTableColumn
hwNDPPortStatus=_HwNDPPortStatus_Object((1,3,6,1,4,1,43,45,1,6,7,5,5,1,2),_HwNDPPortStatus_Type())
hwNDPPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwNDPPortStatus.setStatus(_A)
_HwNDPPortNbTable_Object=MibTable
hwNDPPortNbTable=_HwNDPPortNbTable_Object((1,3,6,1,4,1,43,45,1,6,7,5,6))
if mibBuilder.loadTexts:hwNDPPortNbTable.setStatus(_A)
_HwNDPPortNbEntry_Object=MibTableRow
hwNDPPortNbEntry=_HwNDPPortNbEntry_Object((1,3,6,1,4,1,43,45,1,6,7,5,6,1))
hwNDPPortNbEntry.setIndexNames((0,_E,_O),(0,_E,_l),(0,_E,_m))
if mibBuilder.loadTexts:hwNDPPortNbEntry.setStatus(_A)
class _HwNDPPortNbDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HwNDPPortNbDeviceId_Type.__name__=_F
_HwNDPPortNbDeviceId_Object=MibTableColumn
hwNDPPortNbDeviceId=_HwNDPPortNbDeviceId_Object((1,3,6,1,4,1,43,45,1,6,7,5,6,1,1),_HwNDPPortNbDeviceId_Type())
hwNDPPortNbDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNDPPortNbDeviceId.setStatus(_A)
class _HwNDPPortNbPortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_HwNDPPortNbPortName_Type.__name__=_F
_HwNDPPortNbPortName_Object=MibTableColumn
hwNDPPortNbPortName=_HwNDPPortNbPortName_Object((1,3,6,1,4,1,43,45,1,6,7,5,6,1,2),_HwNDPPortNbPortName_Type())
hwNDPPortNbPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNDPPortNbPortName.setStatus(_A)
_HwNDPPortNbDeviceName_Type=OctetString
_HwNDPPortNbDeviceName_Object=MibTableColumn
hwNDPPortNbDeviceName=_HwNDPPortNbDeviceName_Object((1,3,6,1,4,1,43,45,1,6,7,5,6,1,3),_HwNDPPortNbDeviceName_Type())
hwNDPPortNbDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNDPPortNbDeviceName.setStatus(_A)
class _HwNDPPortNbPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('full',1),('half',2),('auto',3)))
_HwNDPPortNbPortMode_Type.__name__=_C
_HwNDPPortNbPortMode_Object=MibTableColumn
hwNDPPortNbPortMode=_HwNDPPortNbPortMode_Object((1,3,6,1,4,1,43,45,1,6,7,5,6,1,4),_HwNDPPortNbPortMode_Type())
hwNDPPortNbPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNDPPortNbPortMode.setStatus(_A)
_HwNDPPortNbProductVer_Type=OctetString
_HwNDPPortNbProductVer_Object=MibTableColumn
hwNDPPortNbProductVer=_HwNDPPortNbProductVer_Object((1,3,6,1,4,1,43,45,1,6,7,5,6,1,5),_HwNDPPortNbProductVer_Type())
hwNDPPortNbProductVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNDPPortNbProductVer.setStatus(_A)
_HwNDPPortNbHardVer_Type=OctetString
_HwNDPPortNbHardVer_Object=MibTableColumn
hwNDPPortNbHardVer=_HwNDPPortNbHardVer_Object((1,3,6,1,4,1,43,45,1,6,7,5,6,1,6),_HwNDPPortNbHardVer_Type())
hwNDPPortNbHardVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNDPPortNbHardVer.setStatus(_A)
_HwNDPPortNbBootromVer_Type=OctetString
_HwNDPPortNbBootromVer_Object=MibTableColumn
hwNDPPortNbBootromVer=_HwNDPPortNbBootromVer_Object((1,3,6,1,4,1,43,45,1,6,7,5,6,1,7),_HwNDPPortNbBootromVer_Type())
hwNDPPortNbBootromVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNDPPortNbBootromVer.setStatus(_A)
_HwNDPPortNbSoftVer_Type=OctetString
_HwNDPPortNbSoftVer_Object=MibTableColumn
hwNDPPortNbSoftVer=_HwNDPPortNbSoftVer_Object((1,3,6,1,4,1,43,45,1,6,7,5,6,1,8),_HwNDPPortNbSoftVer_Type())
hwNDPPortNbSoftVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNDPPortNbSoftVer.setStatus(_A)
class _HwNDPPortNbAgingtime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,255))
_HwNDPPortNbAgingtime_Type.__name__=_C
_HwNDPPortNbAgingtime_Object=MibTableColumn
hwNDPPortNbAgingtime=_HwNDPPortNbAgingtime_Object((1,3,6,1,4,1,43,45,1,6,7,5,6,1,9),_HwNDPPortNbAgingtime_Type())
hwNDPPortNbAgingtime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNDPPortNbAgingtime.setStatus(_A)
hgmpMemberfailure=NotificationType((1,3,6,1,4,1,43,45,1,6,7,1,0,1))
hgmpMemberfailure.setObjects((_E,_I))
if mibBuilder.loadTexts:hgmpMemberfailure.setStatus(_A)
hgmpMemberRecover=NotificationType((1,3,6,1,4,1,43,45,1,6,7,1,0,2))
hgmpMemberRecover.setObjects((_E,_I))
if mibBuilder.loadTexts:hgmpMemberRecover.setStatus(_A)
hgmpMemberStatusChange=NotificationType((1,3,6,1,4,1,43,45,1,6,7,1,0,3))
hgmpMemberStatusChange.setObjects(*((_E,_I),(_E,_P)))
if mibBuilder.loadTexts:hgmpMemberStatusChange.setStatus(_A)
hgmpNetTopChange=NotificationType((1,3,6,1,4,1,43,45,1,6,7,1,0,4))
if mibBuilder.loadTexts:hgmpNetTopChange.setStatus(_A)
hgmpStackMemberfailure=NotificationType((1,3,6,1,4,1,43,45,1,6,7,2,0,1))
hgmpStackMemberfailure.setObjects((_E,_J))
if mibBuilder.loadTexts:hgmpStackMemberfailure.setStatus(_A)
hgmpStackMemberRecover=NotificationType((1,3,6,1,4,1,43,45,1,6,7,2,0,2))
hgmpStackMemberRecover.setObjects((_E,_J))
if mibBuilder.loadTexts:hgmpStackMemberRecover.setStatus(_A)
hgmpStackMemberStatusChange=NotificationType((1,3,6,1,4,1,43,45,1,6,7,2,0,3))
hgmpStackMemberStatusChange.setObjects(*((_E,_J),(_E,_P)))
if mibBuilder.loadTexts:hgmpStackMemberStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hwCluster':hwCluster,'hwClusterObject':hwClusterObject,'hgmpEventsV2':hgmpEventsV2,'hgmpMemberfailure':hgmpMemberfailure,'hgmpMemberRecover':hgmpMemberRecover,'hgmpMemberStatusChange':hgmpMemberStatusChange,'hgmpNetTopChange':hgmpNetTopChange,'hgmpSetVLANSecurity':hgmpSetVLANSecurity,'hgmpHandShakeInterval':hgmpHandShakeInterval,'hgmpHandShakeHoldtime':hgmpHandShakeHoldtime,'hgmpGrpMemberTableChange':hgmpGrpMemberTableChange,'hgmpMemberDisconRate':hgmpMemberDisconRate,'hgmpCmdLanswitchFlag':hgmpCmdLanswitchFlag,'hgmpCmdClusterName':hgmpCmdClusterName,'hgmpMngPriIpSegCMIP':hgmpMngPriIpSegCMIP,'hgmpMngPriIpMask':hgmpMngPriIpMask,'hgmpFtpServer':hgmpFtpServer,'hgmpTftpServer':hgmpTftpServer,'hgmpSnmpHost':hgmpSnmpHost,'hgmpLogHost':hgmpLogHost,'hgmpGrpMemberTable':hgmpGrpMemberTable,'hgmpGrpMemberEntry':hgmpGrpMemberEntry,_I:hgmpGrpMemberDeviceId,'hgmpGrpMemberSerial':hgmpGrpMemberSerial,'hgmpGrpMemberIpAddr':hgmpGrpMemberIpAddr,'hgmpGrpMemberName':hgmpGrpMemberName,'hgmpGrpMemberPassword':hgmpGrpMemberPassword,'hgmpGrpMemberPlatform':hgmpGrpMemberPlatform,'hgmpGrpMemberStatus':hgmpGrpMemberStatus,'hgmpGrpMemberDisconCount':hgmpGrpMemberDisconCount,'hgmpGrpMemberEnrollTime':hgmpGrpMemberEnrollTime,'hgmpGrpMemberOperate':hgmpGrpMemberOperate,'hgmpMemberResetTable':hgmpMemberResetTable,'hgmpMemberResetEntry':hgmpMemberResetEntry,_U:hgmpMemberResetMAC,'hgmpMemberEraseflash':hgmpMemberEraseflash,'hgmpClusterRole':hgmpClusterRole,'hgmpClusterMaxPoolNum':hgmpClusterMaxPoolNum,'hgmpClusterCmdSwMac':hgmpClusterCmdSwMac,'hgmpRun':hgmpRun,'hgmpProtocolMac':hgmpProtocolMac,'hgmpClusterProtocolMac':hgmpClusterProtocolMac,'hgmpTopologyManagement':hgmpTopologyManagement,'hgmpWhitelistTable':hgmpWhitelistTable,'hgmpWhitelistEntry':hgmpWhitelistEntry,_N:hgmpWhitelistDeviceId,'hgmpWhitelistSerial':hgmpWhitelistSerial,'hgmpWhitelistRowStatus':hgmpWhitelistRowStatus,'hgmpWhitelistNbTable':hgmpWhitelistNbTable,'hgmpWhitelistNbEntry':hgmpWhitelistNbEntry,_Z:hgmpWhitelistNbIndex,'hgmpWhitelistNbDeviceId':hgmpWhitelistNbDeviceId,'hgmpWhitelistPortName':hgmpWhitelistPortName,'hgmpWhitelistNbPortName':hgmpWhitelistNbPortName,'hgmpBlacklistTable':hgmpBlacklistTable,'hgmpBlacklistEntry':hgmpBlacklistEntry,_a:hgmpBlacklistDeviceId,'hgmpBlacklistAccessDeviceId':hgmpBlacklistAccessDeviceId,'hgmpBlacklistAccessPortName':hgmpBlacklistAccessPortName,'hgmpBlacklistRowStatus':hgmpBlacklistRowStatus,'hgmpMemberPriPortTable':hgmpMemberPriPortTable,'hgmpMemberPriPortEntry':hgmpMemberPriPortEntry,_b:hgmpMemberDevId,_c:hgmpMemberPriPortProto,'hgmpMemberPriPortProtoDescr':hgmpMemberPriPortProtoDescr,'hgmpMemberPriPortNum':hgmpMemberPriPortNum,'hwStackObject':hwStackObject,'hgmpStackEventsV2':hgmpStackEventsV2,'hgmpStackMemberfailure':hgmpStackMemberfailure,'hgmpStackMemberRecover':hgmpStackMemberRecover,'hgmpStackMemberStatusChange':hgmpStackMemberStatusChange,'hgmpStackMemberTableChange':hgmpStackMemberTableChange,'hgmpStackMemberDisconRate':hgmpStackMemberDisconRate,'hgmpMainLanswitchFlag':hgmpMainLanswitchFlag,'hgmpStackIpPoolStartIP':hgmpStackIpPoolStartIP,'hgmpStackIpPoolLength':hgmpStackIpPoolLength,'hgmpStackMemberTable':hgmpStackMemberTable,'hgmpStackMemberEntry':hgmpStackMemberEntry,_J:hgmpStackMemberDeviceId,'hgmpStackMemberSerial':hgmpStackMemberSerial,'hgmpStackMemberIpAddr':hgmpStackMemberIpAddr,'hgmpStackMemberName':hgmpStackMemberName,'hgmpStackMemberPassword':hgmpStackMemberPassword,'hgmpStackMemberPlatform':hgmpStackMemberPlatform,'hgmpStackMemberStatus':hgmpStackMemberStatus,'hgmpStackMemberDisconCount':hgmpStackMemberDisconCount,'hgmpStackMemberEnrollTime':hgmpStackMemberEnrollTime,'hgmpStackRole':hgmpStackRole,'hgmpStackMaxPoolNum':hgmpStackMaxPoolNum,'hgmpStackMainSwMac':hgmpStackMainSwMac,'hgmpStackIpPoolMask':hgmpStackIpPoolMask,'hwNTDPObject':hwNTDPObject,'hgmpNTDPCollectTopTime':hgmpNTDPCollectTopTime,'hgmpNTDPHopRange':hgmpNTDPHopRange,'hgmpNTDPRun':hgmpNTDPRun,'hgmpNTDPPortDelay':hgmpNTDPPortDelay,'hgmpNTDPHopDelay':hgmpNTDPHopDelay,'hgmpNTDPLastTopCollectDuration':hgmpNTDPLastTopCollectDuration,'hgmpNTDPCacheChange':hgmpNTDPCacheChange,'hgmpNTDPTOPTableChange':hgmpNTDPTOPTableChange,'hgmpNTDPInterfaceTable':hgmpNTDPInterfaceTable,'hgmpNTDPInterfaceEntry':hgmpNTDPInterfaceEntry,_d:hgmpNTDPInterfaceIfIndex,'hgmpNTDPInterfaceEnable':hgmpNTDPInterfaceEnable,'hgmpNTDPCacheTable':hgmpNTDPCacheTable,'hgmpNTDPCacheEntry':hgmpNTDPCacheEntry,_e:hgmpNTDPCacheHashIndex,_f:hgmpNTDPCacheDeviceID,'hgmpNTDPCacheClusterName':hgmpNTDPCacheClusterName,_P:hgmpNTDPCacheClusterRole,'hgmpNTDPCacheCapabilities':hgmpNTDPCacheCapabilities,'hgmpNTDPCacheVersion':hgmpNTDPCacheVersion,'hgmpNTDPCachePlatform':hgmpNTDPCachePlatform,'hgmpNTDPCacheMngVLAN':hgmpNTDPCacheMngVLAN,'hgmpNTDPCacheHop':hgmpNTDPCacheHop,'hgmpNTDPTopTable':hgmpNTDPTopTable,'hgmpNTDPTopEntry':hgmpNTDPTopEntry,_g:hgmpNTDPTopHashIndex,_h:hgmpNTDPTopEdgeStartDevID,_i:hgmpNTDPTopEdgeIndex,'hgmpNTDPTopEdgeEndDevID':hgmpNTDPTopEdgeEndDevID,'hgmpNTDPTopEdgeStartPort':hgmpNTDPTopEdgeStartPort,'hgmpNTDPTopEdgeStartPortFullDuplex':hgmpNTDPTopEdgeStartPortFullDuplex,'hgmpNTDPTopEdgeStartPortSpeed':hgmpNTDPTopEdgeStartPortSpeed,'hgmpNTDPTopEdgeEndPort':hgmpNTDPTopEdgeEndPort,'hgmpNTDPTopLinkStatus':hgmpNTDPTopLinkStatus,'hwNDPObject':hwNDPObject,'hwNDPStatus':hwNDPStatus,'hwNDPHelloTimer':hwNDPHelloTimer,'hwNDPAgingTime':hwNDPAgingTime,'hwNDPChange':hwNDPChange,'hwNDPPortTable':hwNDPPortTable,'hwNDPPortEntry':hwNDPPortEntry,_O:hwNDPIfIndex,'hwNDPPortStatus':hwNDPPortStatus,'hwNDPPortNbTable':hwNDPPortNbTable,'hwNDPPortNbEntry':hwNDPPortNbEntry,_l:hwNDPPortNbDeviceId,_m:hwNDPPortNbPortName,'hwNDPPortNbDeviceName':hwNDPPortNbDeviceName,'hwNDPPortNbPortMode':hwNDPPortNbPortMode,'hwNDPPortNbProductVer':hwNDPPortNbProductVer,'hwNDPPortNbHardVer':hwNDPPortNbHardVer,'hwNDPPortNbBootromVer':hwNDPPortNbBootromVer,'hwNDPPortNbSoftVer':hwNDPPortNbSoftVer,'hwNDPPortNbAgingtime':hwNDPPortNbAgingtime})