_m='hpnicfNDPPortNbPortName'
_l='hpnicfNDPPortNbDeviceId'
_k='enable'
_j='disable'
_i='hpnicfhgmpNTDPTopEdgeIndex'
_h='hpnicfhgmpNTDPTopEdgeStartDevID'
_g='hpnicfhgmpNTDPTopHashIndex'
_f='hpnicfhgmpNTDPCacheDeviceID'
_e='hpnicfhgmpNTDPCacheHashIndex'
_d='hpnicfhgmpNTDPInterfaceIfIndex'
_c='hpnicfhgmpMemberPriPortProto'
_b='hpnicfhgmpMemberDevId'
_a='hpnicfhgmpBlacklistDeviceId'
_Z='hpnicfhgmpWhitelistNbIndex'
_Y='read-create'
_X='roleBAKSW'
_W='roleMEMBERSW'
_V='roleCMDSW'
_U='hpnicfhgmpMemberResetMAC'
_T='normal'
_S='MacAddress'
_R='IpAddress'
_Q='Counter32'
_P='hpnicfhgmpNTDPCacheClusterRole'
_O='hpnicfNDPIfIndex'
_N='hpnicfhgmpWhitelistDeviceId'
_M='roleUNISW'
_L='roleCASW'
_K='not-accessible'
_J='hpnicfhgmpStackMemberDeviceId'
_I='hpnicfhgmpGrpMemberDeviceId'
_H='true'
_G='false'
_F='OctetString'
_E='HPN-ICF-HGMP-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfRhw,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfRhw')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_Q,'Counter64','Gauge32',_C,_R,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_S,'PhysAddress','RowStatus','TextualConvention')
hpnicfHgmp=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,7))
_HpnicfClusterObject_ObjectIdentity=ObjectIdentity
hpnicfClusterObject=_HpnicfClusterObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,7,1))
if mibBuilder.loadTexts:hpnicfClusterObject.setStatus(_A)
_HpnicfhgmpEventsV2_ObjectIdentity=ObjectIdentity
hpnicfhgmpEventsV2=_HpnicfhgmpEventsV2_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,7,1,0))
if mibBuilder.loadTexts:hpnicfhgmpEventsV2.setStatus(_A)
class _HpnicfhgmpSetVLANSecurity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noSecurity',0),('security',1)))
_HpnicfhgmpSetVLANSecurity_Type.__name__=_C
_HpnicfhgmpSetVLANSecurity_Object=MibScalar
hpnicfhgmpSetVLANSecurity=_HpnicfhgmpSetVLANSecurity_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,1),_HpnicfhgmpSetVLANSecurity_Type())
hpnicfhgmpSetVLANSecurity.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpSetVLANSecurity.setStatus(_A)
class _HpnicfhgmpHandShakeInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfhgmpHandShakeInterval_Type.__name__=_C
_HpnicfhgmpHandShakeInterval_Object=MibScalar
hpnicfhgmpHandShakeInterval=_HpnicfhgmpHandShakeInterval_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,2),_HpnicfhgmpHandShakeInterval_Type())
hpnicfhgmpHandShakeInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpHandShakeInterval.setStatus(_A)
class _HpnicfhgmpHandShakeHoldtime_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfhgmpHandShakeHoldtime_Type.__name__=_C
_HpnicfhgmpHandShakeHoldtime_Object=MibScalar
hpnicfhgmpHandShakeHoldtime=_HpnicfhgmpHandShakeHoldtime_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,3),_HpnicfhgmpHandShakeHoldtime_Type())
hpnicfhgmpHandShakeHoldtime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpHandShakeHoldtime.setStatus(_A)
class _HpnicfhgmpGrpMemberTableChange_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfhgmpGrpMemberTableChange_Type.__name__=_C
_HpnicfhgmpGrpMemberTableChange_Object=MibScalar
hpnicfhgmpGrpMemberTableChange=_HpnicfhgmpGrpMemberTableChange_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,4),_HpnicfhgmpGrpMemberTableChange_Type())
hpnicfhgmpGrpMemberTableChange.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpGrpMemberTableChange.setStatus(_A)
class _HpnicfhgmpMemberDisconRate_Type(Integer32):defaultValue=0
_HpnicfhgmpMemberDisconRate_Type.__name__=_C
_HpnicfhgmpMemberDisconRate_Object=MibScalar
hpnicfhgmpMemberDisconRate=_HpnicfhgmpMemberDisconRate_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,5),_HpnicfhgmpMemberDisconRate_Type())
hpnicfhgmpMemberDisconRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpMemberDisconRate.setStatus(_A)
class _HpnicfhgmpCmdLanswitchFlag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_HpnicfhgmpCmdLanswitchFlag_Type.__name__=_C
_HpnicfhgmpCmdLanswitchFlag_Object=MibScalar
hpnicfhgmpCmdLanswitchFlag=_HpnicfhgmpCmdLanswitchFlag_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,6),_HpnicfhgmpCmdLanswitchFlag_Type())
hpnicfhgmpCmdLanswitchFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpCmdLanswitchFlag.setStatus(_A)
class _HpnicfhgmpCmdClusterName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_HpnicfhgmpCmdClusterName_Type.__name__=_F
_HpnicfhgmpCmdClusterName_Object=MibScalar
hpnicfhgmpCmdClusterName=_HpnicfhgmpCmdClusterName_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,7),_HpnicfhgmpCmdClusterName_Type())
hpnicfhgmpCmdClusterName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpCmdClusterName.setStatus(_A)
_HpnicfhgmpMngPriIpSegCMIP_Type=IpAddress
_HpnicfhgmpMngPriIpSegCMIP_Object=MibScalar
hpnicfhgmpMngPriIpSegCMIP=_HpnicfhgmpMngPriIpSegCMIP_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,8),_HpnicfhgmpMngPriIpSegCMIP_Type())
hpnicfhgmpMngPriIpSegCMIP.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpMngPriIpSegCMIP.setStatus(_A)
_HpnicfhgmpMngPriIpMask_Type=IpAddress
_HpnicfhgmpMngPriIpMask_Object=MibScalar
hpnicfhgmpMngPriIpMask=_HpnicfhgmpMngPriIpMask_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,9),_HpnicfhgmpMngPriIpMask_Type())
hpnicfhgmpMngPriIpMask.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpMngPriIpMask.setStatus(_A)
_HpnicfhgmpFtpServer_Type=IpAddress
_HpnicfhgmpFtpServer_Object=MibScalar
hpnicfhgmpFtpServer=_HpnicfhgmpFtpServer_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,10),_HpnicfhgmpFtpServer_Type())
hpnicfhgmpFtpServer.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpFtpServer.setStatus(_A)
_HpnicfhgmpTftpServer_Type=IpAddress
_HpnicfhgmpTftpServer_Object=MibScalar
hpnicfhgmpTftpServer=_HpnicfhgmpTftpServer_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,11),_HpnicfhgmpTftpServer_Type())
hpnicfhgmpTftpServer.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpTftpServer.setStatus(_A)
_HpnicfhgmpSnmpHost_Type=IpAddress
_HpnicfhgmpSnmpHost_Object=MibScalar
hpnicfhgmpSnmpHost=_HpnicfhgmpSnmpHost_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,12),_HpnicfhgmpSnmpHost_Type())
hpnicfhgmpSnmpHost.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpSnmpHost.setStatus(_A)
_HpnicfhgmpLogHost_Type=IpAddress
_HpnicfhgmpLogHost_Object=MibScalar
hpnicfhgmpLogHost=_HpnicfhgmpLogHost_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,13),_HpnicfhgmpLogHost_Type())
hpnicfhgmpLogHost.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpLogHost.setStatus(_A)
_HpnicfhgmpGrpMemberTable_Object=MibTable
hpnicfhgmpGrpMemberTable=_HpnicfhgmpGrpMemberTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,14))
if mibBuilder.loadTexts:hpnicfhgmpGrpMemberTable.setStatus(_A)
_HpnicfhgmpGrpMemberEntry_Object=MibTableRow
hpnicfhgmpGrpMemberEntry=_HpnicfhgmpGrpMemberEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,14,1))
hpnicfhgmpGrpMemberEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:hpnicfhgmpGrpMemberEntry.setStatus(_A)
class _HpnicfhgmpGrpMemberDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HpnicfhgmpGrpMemberDeviceId_Type.__name__=_F
_HpnicfhgmpGrpMemberDeviceId_Object=MibTableColumn
hpnicfhgmpGrpMemberDeviceId=_HpnicfhgmpGrpMemberDeviceId_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,14,1,1),_HpnicfhgmpGrpMemberDeviceId_Type())
hpnicfhgmpGrpMemberDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpGrpMemberDeviceId.setStatus(_A)
class _HpnicfhgmpGrpMemberSerial_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2047))
_HpnicfhgmpGrpMemberSerial_Type.__name__=_C
_HpnicfhgmpGrpMemberSerial_Object=MibTableColumn
hpnicfhgmpGrpMemberSerial=_HpnicfhgmpGrpMemberSerial_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,14,1,2),_HpnicfhgmpGrpMemberSerial_Type())
hpnicfhgmpGrpMemberSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpGrpMemberSerial.setStatus(_A)
_HpnicfhgmpGrpMemberIpAddr_Type=IpAddress
_HpnicfhgmpGrpMemberIpAddr_Object=MibTableColumn
hpnicfhgmpGrpMemberIpAddr=_HpnicfhgmpGrpMemberIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,14,1,3),_HpnicfhgmpGrpMemberIpAddr_Type())
hpnicfhgmpGrpMemberIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpGrpMemberIpAddr.setStatus(_A)
class _HpnicfhgmpGrpMemberName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfhgmpGrpMemberName_Type.__name__=_F
_HpnicfhgmpGrpMemberName_Object=MibTableColumn
hpnicfhgmpGrpMemberName=_HpnicfhgmpGrpMemberName_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,14,1,4),_HpnicfhgmpGrpMemberName_Type())
hpnicfhgmpGrpMemberName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpGrpMemberName.setStatus(_A)
_HpnicfhgmpGrpMemberPassword_Type=OctetString
_HpnicfhgmpGrpMemberPassword_Object=MibTableColumn
hpnicfhgmpGrpMemberPassword=_HpnicfhgmpGrpMemberPassword_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,14,1,5),_HpnicfhgmpGrpMemberPassword_Type())
hpnicfhgmpGrpMemberPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpGrpMemberPassword.setStatus(_A)
_HpnicfhgmpGrpMemberPlatform_Type=OctetString
_HpnicfhgmpGrpMemberPlatform_Object=MibTableColumn
hpnicfhgmpGrpMemberPlatform=_HpnicfhgmpGrpMemberPlatform_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,14,1,6),_HpnicfhgmpGrpMemberPlatform_Type())
hpnicfhgmpGrpMemberPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpGrpMemberPlatform.setStatus(_A)
class _HpnicfhgmpGrpMemberStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),('fault',1)))
_HpnicfhgmpGrpMemberStatus_Type.__name__=_C
_HpnicfhgmpGrpMemberStatus_Object=MibTableColumn
hpnicfhgmpGrpMemberStatus=_HpnicfhgmpGrpMemberStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,14,1,7),_HpnicfhgmpGrpMemberStatus_Type())
hpnicfhgmpGrpMemberStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpGrpMemberStatus.setStatus(_A)
_HpnicfhgmpGrpMemberDisconCount_Type=Integer32
_HpnicfhgmpGrpMemberDisconCount_Object=MibTableColumn
hpnicfhgmpGrpMemberDisconCount=_HpnicfhgmpGrpMemberDisconCount_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,14,1,8),_HpnicfhgmpGrpMemberDisconCount_Type())
hpnicfhgmpGrpMemberDisconCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpGrpMemberDisconCount.setStatus(_A)
_HpnicfhgmpGrpMemberEnrollTime_Type=Integer32
_HpnicfhgmpGrpMemberEnrollTime_Object=MibTableColumn
hpnicfhgmpGrpMemberEnrollTime=_HpnicfhgmpGrpMemberEnrollTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,14,1,9),_HpnicfhgmpGrpMemberEnrollTime_Type())
hpnicfhgmpGrpMemberEnrollTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpGrpMemberEnrollTime.setStatus(_A)
_HpnicfhgmpGrpMemberOperate_Type=RowStatus
_HpnicfhgmpGrpMemberOperate_Object=MibTableColumn
hpnicfhgmpGrpMemberOperate=_HpnicfhgmpGrpMemberOperate_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,14,1,10),_HpnicfhgmpGrpMemberOperate_Type())
hpnicfhgmpGrpMemberOperate.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpGrpMemberOperate.setStatus(_A)
_HpnicfhgmpMemberResetTable_Object=MibTable
hpnicfhgmpMemberResetTable=_HpnicfhgmpMemberResetTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,15))
if mibBuilder.loadTexts:hpnicfhgmpMemberResetTable.setStatus(_A)
_HpnicfhgmpMemberResetEntry_Object=MibTableRow
hpnicfhgmpMemberResetEntry=_HpnicfhgmpMemberResetEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,15,1))
hpnicfhgmpMemberResetEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:hpnicfhgmpMemberResetEntry.setStatus(_A)
class _HpnicfhgmpMemberResetMAC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_HpnicfhgmpMemberResetMAC_Type.__name__=_F
_HpnicfhgmpMemberResetMAC_Object=MibTableColumn
hpnicfhgmpMemberResetMAC=_HpnicfhgmpMemberResetMAC_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,15,1,1),_HpnicfhgmpMemberResetMAC_Type())
hpnicfhgmpMemberResetMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpMemberResetMAC.setStatus(_A)
class _HpnicfhgmpMemberEraseflash_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,65535)));namedValues=NamedValues(*(('noErase',0),('erase',1),('cannotget',65535)))
_HpnicfhgmpMemberEraseflash_Type.__name__=_C
_HpnicfhgmpMemberEraseflash_Object=MibTableColumn
hpnicfhgmpMemberEraseflash=_HpnicfhgmpMemberEraseflash_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,15,1,2),_HpnicfhgmpMemberEraseflash_Type())
hpnicfhgmpMemberEraseflash.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpMemberEraseflash.setStatus(_A)
class _HpnicfhgmpClusterRole_Type(Integer32):defaultValue=17;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,16,17)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_L,16),(_M,17)))
_HpnicfhgmpClusterRole_Type.__name__=_C
_HpnicfhgmpClusterRole_Object=MibScalar
hpnicfhgmpClusterRole=_HpnicfhgmpClusterRole_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,16),_HpnicfhgmpClusterRole_Type())
hpnicfhgmpClusterRole.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpClusterRole.setStatus(_A)
_HpnicfhgmpClusterMaxPoolNum_Type=Integer32
_HpnicfhgmpClusterMaxPoolNum_Object=MibScalar
hpnicfhgmpClusterMaxPoolNum=_HpnicfhgmpClusterMaxPoolNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,17),_HpnicfhgmpClusterMaxPoolNum_Type())
hpnicfhgmpClusterMaxPoolNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpClusterMaxPoolNum.setStatus(_A)
class _HpnicfhgmpClusterCmdSwMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_HpnicfhgmpClusterCmdSwMac_Type.__name__=_F
_HpnicfhgmpClusterCmdSwMac_Object=MibScalar
hpnicfhgmpClusterCmdSwMac=_HpnicfhgmpClusterCmdSwMac_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,18),_HpnicfhgmpClusterCmdSwMac_Type())
hpnicfhgmpClusterCmdSwMac.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpClusterCmdSwMac.setStatus(_A)
class _HpnicfhgmpRun_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_HpnicfhgmpRun_Type.__name__=_C
_HpnicfhgmpRun_Object=MibScalar
hpnicfhgmpRun=_HpnicfhgmpRun_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,19),_HpnicfhgmpRun_Type())
hpnicfhgmpRun.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpRun.setStatus(_A)
_HpnicfhgmpProtocolMac_ObjectIdentity=ObjectIdentity
hpnicfhgmpProtocolMac=_HpnicfhgmpProtocolMac_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,7,1,22))
class _HpnicfhgmpClusterProtocolMac_Type(MacAddress):defaultHexValue='0180C200000A'
_HpnicfhgmpClusterProtocolMac_Type.__name__=_S
_HpnicfhgmpClusterProtocolMac_Object=MibScalar
hpnicfhgmpClusterProtocolMac=_HpnicfhgmpClusterProtocolMac_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,22,1),_HpnicfhgmpClusterProtocolMac_Type())
hpnicfhgmpClusterProtocolMac.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpClusterProtocolMac.setStatus(_A)
_HpnicfhgmpTopologyManagement_ObjectIdentity=ObjectIdentity
hpnicfhgmpTopologyManagement=_HpnicfhgmpTopologyManagement_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,7,1,23))
_HpnicfhgmpWhitelistTable_Object=MibTable
hpnicfhgmpWhitelistTable=_HpnicfhgmpWhitelistTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,23,1))
if mibBuilder.loadTexts:hpnicfhgmpWhitelistTable.setStatus(_A)
_HpnicfhgmpWhitelistEntry_Object=MibTableRow
hpnicfhgmpWhitelistEntry=_HpnicfhgmpWhitelistEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,23,1,1))
hpnicfhgmpWhitelistEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:hpnicfhgmpWhitelistEntry.setStatus(_A)
class _HpnicfhgmpWhitelistDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_HpnicfhgmpWhitelistDeviceId_Type.__name__=_F
_HpnicfhgmpWhitelistDeviceId_Object=MibTableColumn
hpnicfhgmpWhitelistDeviceId=_HpnicfhgmpWhitelistDeviceId_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,23,1,1,1),_HpnicfhgmpWhitelistDeviceId_Type())
hpnicfhgmpWhitelistDeviceId.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfhgmpWhitelistDeviceId.setStatus(_A)
class _HpnicfhgmpWhitelistSerial_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2047),ValueRangeConstraint(65535,65535))
_HpnicfhgmpWhitelistSerial_Type.__name__=_C
_HpnicfhgmpWhitelistSerial_Object=MibTableColumn
hpnicfhgmpWhitelistSerial=_HpnicfhgmpWhitelistSerial_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,23,1,1,2),_HpnicfhgmpWhitelistSerial_Type())
hpnicfhgmpWhitelistSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpWhitelistSerial.setStatus(_A)
_HpnicfhgmpWhitelistRowStatus_Type=RowStatus
_HpnicfhgmpWhitelistRowStatus_Object=MibTableColumn
hpnicfhgmpWhitelistRowStatus=_HpnicfhgmpWhitelistRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,23,1,1,3),_HpnicfhgmpWhitelistRowStatus_Type())
hpnicfhgmpWhitelistRowStatus.setMaxAccess(_Y)
if mibBuilder.loadTexts:hpnicfhgmpWhitelistRowStatus.setStatus(_A)
_HpnicfhgmpWhitelistNbTable_Object=MibTable
hpnicfhgmpWhitelistNbTable=_HpnicfhgmpWhitelistNbTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,23,2))
if mibBuilder.loadTexts:hpnicfhgmpWhitelistNbTable.setStatus(_A)
_HpnicfhgmpWhitelistNbEntry_Object=MibTableRow
hpnicfhgmpWhitelistNbEntry=_HpnicfhgmpWhitelistNbEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,23,2,1))
hpnicfhgmpWhitelistNbEntry.setIndexNames((0,_E,_N),(0,_E,_Z))
if mibBuilder.loadTexts:hpnicfhgmpWhitelistNbEntry.setStatus(_A)
class _HpnicfhgmpWhitelistNbIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfhgmpWhitelistNbIndex_Type.__name__=_C
_HpnicfhgmpWhitelistNbIndex_Object=MibTableColumn
hpnicfhgmpWhitelistNbIndex=_HpnicfhgmpWhitelistNbIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,23,2,1,1),_HpnicfhgmpWhitelistNbIndex_Type())
hpnicfhgmpWhitelistNbIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfhgmpWhitelistNbIndex.setStatus(_A)
class _HpnicfhgmpWhitelistNbDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_HpnicfhgmpWhitelistNbDeviceId_Type.__name__=_F
_HpnicfhgmpWhitelistNbDeviceId_Object=MibTableColumn
hpnicfhgmpWhitelistNbDeviceId=_HpnicfhgmpWhitelistNbDeviceId_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,23,2,1,2),_HpnicfhgmpWhitelistNbDeviceId_Type())
hpnicfhgmpWhitelistNbDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpWhitelistNbDeviceId.setStatus(_A)
class _HpnicfhgmpWhitelistPortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_HpnicfhgmpWhitelistPortName_Type.__name__=_F
_HpnicfhgmpWhitelistPortName_Object=MibTableColumn
hpnicfhgmpWhitelistPortName=_HpnicfhgmpWhitelistPortName_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,23,2,1,3),_HpnicfhgmpWhitelistPortName_Type())
hpnicfhgmpWhitelistPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpWhitelistPortName.setStatus(_A)
class _HpnicfhgmpWhitelistNbPortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_HpnicfhgmpWhitelistNbPortName_Type.__name__=_F
_HpnicfhgmpWhitelistNbPortName_Object=MibTableColumn
hpnicfhgmpWhitelistNbPortName=_HpnicfhgmpWhitelistNbPortName_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,23,2,1,4),_HpnicfhgmpWhitelistNbPortName_Type())
hpnicfhgmpWhitelistNbPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpWhitelistNbPortName.setStatus(_A)
_HpnicfhgmpBlacklistTable_Object=MibTable
hpnicfhgmpBlacklistTable=_HpnicfhgmpBlacklistTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,23,3))
if mibBuilder.loadTexts:hpnicfhgmpBlacklistTable.setStatus(_A)
_HpnicfhgmpBlacklistEntry_Object=MibTableRow
hpnicfhgmpBlacklistEntry=_HpnicfhgmpBlacklistEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,23,3,1))
hpnicfhgmpBlacklistEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:hpnicfhgmpBlacklistEntry.setStatus(_A)
class _HpnicfhgmpBlacklistDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_HpnicfhgmpBlacklistDeviceId_Type.__name__=_F
_HpnicfhgmpBlacklistDeviceId_Object=MibTableColumn
hpnicfhgmpBlacklistDeviceId=_HpnicfhgmpBlacklistDeviceId_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,23,3,1,1),_HpnicfhgmpBlacklistDeviceId_Type())
hpnicfhgmpBlacklistDeviceId.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfhgmpBlacklistDeviceId.setStatus(_A)
class _HpnicfhgmpBlacklistAccessDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_HpnicfhgmpBlacklistAccessDeviceId_Type.__name__=_F
_HpnicfhgmpBlacklistAccessDeviceId_Object=MibTableColumn
hpnicfhgmpBlacklistAccessDeviceId=_HpnicfhgmpBlacklistAccessDeviceId_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,23,3,1,2),_HpnicfhgmpBlacklistAccessDeviceId_Type())
hpnicfhgmpBlacklistAccessDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpBlacklistAccessDeviceId.setStatus(_A)
class _HpnicfhgmpBlacklistAccessPortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_HpnicfhgmpBlacklistAccessPortName_Type.__name__=_F
_HpnicfhgmpBlacklistAccessPortName_Object=MibTableColumn
hpnicfhgmpBlacklistAccessPortName=_HpnicfhgmpBlacklistAccessPortName_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,23,3,1,3),_HpnicfhgmpBlacklistAccessPortName_Type())
hpnicfhgmpBlacklistAccessPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpBlacklistAccessPortName.setStatus(_A)
_HpnicfhgmpBlacklistRowStatus_Type=RowStatus
_HpnicfhgmpBlacklistRowStatus_Object=MibTableColumn
hpnicfhgmpBlacklistRowStatus=_HpnicfhgmpBlacklistRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,23,3,1,4),_HpnicfhgmpBlacklistRowStatus_Type())
hpnicfhgmpBlacklistRowStatus.setMaxAccess(_Y)
if mibBuilder.loadTexts:hpnicfhgmpBlacklistRowStatus.setStatus(_A)
_HpnicfhgmpMemberPriPortTable_Object=MibTable
hpnicfhgmpMemberPriPortTable=_HpnicfhgmpMemberPriPortTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,24))
if mibBuilder.loadTexts:hpnicfhgmpMemberPriPortTable.setStatus(_A)
_HpnicfhgmpMemberPriPortEntry_Object=MibTableRow
hpnicfhgmpMemberPriPortEntry=_HpnicfhgmpMemberPriPortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,24,1))
hpnicfhgmpMemberPriPortEntry.setIndexNames((0,_E,_b),(0,_E,_c))
if mibBuilder.loadTexts:hpnicfhgmpMemberPriPortEntry.setStatus(_A)
class _HpnicfhgmpMemberDevId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HpnicfhgmpMemberDevId_Type.__name__=_F
_HpnicfhgmpMemberDevId_Object=MibTableColumn
hpnicfhgmpMemberDevId=_HpnicfhgmpMemberDevId_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,24,1,1),_HpnicfhgmpMemberDevId_Type())
hpnicfhgmpMemberDevId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpMemberDevId.setStatus(_A)
_HpnicfhgmpMemberPriPortProto_Type=Unsigned32
_HpnicfhgmpMemberPriPortProto_Object=MibTableColumn
hpnicfhgmpMemberPriPortProto=_HpnicfhgmpMemberPriPortProto_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,24,1,2),_HpnicfhgmpMemberPriPortProto_Type())
hpnicfhgmpMemberPriPortProto.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfhgmpMemberPriPortProto.setStatus(_A)
_HpnicfhgmpMemberPriPortProtoDescr_Type=DisplayString
_HpnicfhgmpMemberPriPortProtoDescr_Object=MibTableColumn
hpnicfhgmpMemberPriPortProtoDescr=_HpnicfhgmpMemberPriPortProtoDescr_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,24,1,3),_HpnicfhgmpMemberPriPortProtoDescr_Type())
hpnicfhgmpMemberPriPortProtoDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpMemberPriPortProtoDescr.setStatus(_A)
_HpnicfhgmpMemberPriPortNum_Type=Unsigned32
_HpnicfhgmpMemberPriPortNum_Object=MibTableColumn
hpnicfhgmpMemberPriPortNum=_HpnicfhgmpMemberPriPortNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,1,24,1,4),_HpnicfhgmpMemberPriPortNum_Type())
hpnicfhgmpMemberPriPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpMemberPriPortNum.setStatus(_A)
_HpnicfStackObject_ObjectIdentity=ObjectIdentity
hpnicfStackObject=_HpnicfStackObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,7,2))
if mibBuilder.loadTexts:hpnicfStackObject.setStatus(_A)
_HpnicfhgmpStackEventsV2_ObjectIdentity=ObjectIdentity
hpnicfhgmpStackEventsV2=_HpnicfhgmpStackEventsV2_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,7,2,0))
if mibBuilder.loadTexts:hpnicfhgmpStackEventsV2.setStatus(_A)
class _HpnicfhgmpStackMemberTableChange_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfhgmpStackMemberTableChange_Type.__name__=_C
_HpnicfhgmpStackMemberTableChange_Object=MibScalar
hpnicfhgmpStackMemberTableChange=_HpnicfhgmpStackMemberTableChange_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,1),_HpnicfhgmpStackMemberTableChange_Type())
hpnicfhgmpStackMemberTableChange.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpStackMemberTableChange.setStatus(_A)
class _HpnicfhgmpStackMemberDisconRate_Type(Integer32):defaultValue=0
_HpnicfhgmpStackMemberDisconRate_Type.__name__=_C
_HpnicfhgmpStackMemberDisconRate_Object=MibScalar
hpnicfhgmpStackMemberDisconRate=_HpnicfhgmpStackMemberDisconRate_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,2),_HpnicfhgmpStackMemberDisconRate_Type())
hpnicfhgmpStackMemberDisconRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpStackMemberDisconRate.setStatus(_A)
class _HpnicfhgmpMainLanswitchFlag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_HpnicfhgmpMainLanswitchFlag_Type.__name__=_C
_HpnicfhgmpMainLanswitchFlag_Object=MibScalar
hpnicfhgmpMainLanswitchFlag=_HpnicfhgmpMainLanswitchFlag_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,3),_HpnicfhgmpMainLanswitchFlag_Type())
hpnicfhgmpMainLanswitchFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpMainLanswitchFlag.setStatus(_A)
_HpnicfhgmpStackIpPoolStartIP_Type=IpAddress
_HpnicfhgmpStackIpPoolStartIP_Object=MibScalar
hpnicfhgmpStackIpPoolStartIP=_HpnicfhgmpStackIpPoolStartIP_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,4),_HpnicfhgmpStackIpPoolStartIP_Type())
hpnicfhgmpStackIpPoolStartIP.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpStackIpPoolStartIP.setStatus(_A)
class _HpnicfhgmpStackIpPoolLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_HpnicfhgmpStackIpPoolLength_Type.__name__=_C
_HpnicfhgmpStackIpPoolLength_Object=MibScalar
hpnicfhgmpStackIpPoolLength=_HpnicfhgmpStackIpPoolLength_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,5),_HpnicfhgmpStackIpPoolLength_Type())
hpnicfhgmpStackIpPoolLength.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpStackIpPoolLength.setStatus(_A)
_HpnicfhgmpStackMemberTable_Object=MibTable
hpnicfhgmpStackMemberTable=_HpnicfhgmpStackMemberTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,6))
if mibBuilder.loadTexts:hpnicfhgmpStackMemberTable.setStatus(_A)
_HpnicfhgmpStackMemberEntry_Object=MibTableRow
hpnicfhgmpStackMemberEntry=_HpnicfhgmpStackMemberEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,6,1))
hpnicfhgmpStackMemberEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:hpnicfhgmpStackMemberEntry.setStatus(_A)
class _HpnicfhgmpStackMemberDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HpnicfhgmpStackMemberDeviceId_Type.__name__=_F
_HpnicfhgmpStackMemberDeviceId_Object=MibTableColumn
hpnicfhgmpStackMemberDeviceId=_HpnicfhgmpStackMemberDeviceId_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,6,1,1),_HpnicfhgmpStackMemberDeviceId_Type())
hpnicfhgmpStackMemberDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpStackMemberDeviceId.setStatus(_A)
class _HpnicfhgmpStackMemberSerial_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2047))
_HpnicfhgmpStackMemberSerial_Type.__name__=_C
_HpnicfhgmpStackMemberSerial_Object=MibTableColumn
hpnicfhgmpStackMemberSerial=_HpnicfhgmpStackMemberSerial_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,6,1,2),_HpnicfhgmpStackMemberSerial_Type())
hpnicfhgmpStackMemberSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpStackMemberSerial.setStatus(_A)
_HpnicfhgmpStackMemberIpAddr_Type=IpAddress
_HpnicfhgmpStackMemberIpAddr_Object=MibTableColumn
hpnicfhgmpStackMemberIpAddr=_HpnicfhgmpStackMemberIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,6,1,3),_HpnicfhgmpStackMemberIpAddr_Type())
hpnicfhgmpStackMemberIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpStackMemberIpAddr.setStatus(_A)
_HpnicfhgmpStackMemberName_Type=OctetString
_HpnicfhgmpStackMemberName_Object=MibTableColumn
hpnicfhgmpStackMemberName=_HpnicfhgmpStackMemberName_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,6,1,4),_HpnicfhgmpStackMemberName_Type())
hpnicfhgmpStackMemberName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpStackMemberName.setStatus(_A)
_HpnicfhgmpStackMemberPassword_Type=OctetString
_HpnicfhgmpStackMemberPassword_Object=MibTableColumn
hpnicfhgmpStackMemberPassword=_HpnicfhgmpStackMemberPassword_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,6,1,5),_HpnicfhgmpStackMemberPassword_Type())
hpnicfhgmpStackMemberPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpStackMemberPassword.setStatus(_A)
_HpnicfhgmpStackMemberPlatform_Type=OctetString
_HpnicfhgmpStackMemberPlatform_Object=MibTableColumn
hpnicfhgmpStackMemberPlatform=_HpnicfhgmpStackMemberPlatform_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,6,1,6),_HpnicfhgmpStackMemberPlatform_Type())
hpnicfhgmpStackMemberPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpStackMemberPlatform.setStatus(_A)
class _HpnicfhgmpStackMemberStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),('fault',1)))
_HpnicfhgmpStackMemberStatus_Type.__name__=_C
_HpnicfhgmpStackMemberStatus_Object=MibTableColumn
hpnicfhgmpStackMemberStatus=_HpnicfhgmpStackMemberStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,6,1,7),_HpnicfhgmpStackMemberStatus_Type())
hpnicfhgmpStackMemberStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpStackMemberStatus.setStatus(_A)
_HpnicfhgmpStackMemberDisconCount_Type=Integer32
_HpnicfhgmpStackMemberDisconCount_Object=MibTableColumn
hpnicfhgmpStackMemberDisconCount=_HpnicfhgmpStackMemberDisconCount_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,6,1,8),_HpnicfhgmpStackMemberDisconCount_Type())
hpnicfhgmpStackMemberDisconCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpStackMemberDisconCount.setStatus(_A)
_HpnicfhgmpStackMemberEnrollTime_Type=Integer32
_HpnicfhgmpStackMemberEnrollTime_Object=MibTableColumn
hpnicfhgmpStackMemberEnrollTime=_HpnicfhgmpStackMemberEnrollTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,6,1,9),_HpnicfhgmpStackMemberEnrollTime_Type())
hpnicfhgmpStackMemberEnrollTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpStackMemberEnrollTime.setStatus(_A)
class _HpnicfhgmpStackRole_Type(Integer32):defaultValue=17;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,16,17)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_L,16),(_M,17)))
_HpnicfhgmpStackRole_Type.__name__=_C
_HpnicfhgmpStackRole_Object=MibScalar
hpnicfhgmpStackRole=_HpnicfhgmpStackRole_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,7),_HpnicfhgmpStackRole_Type())
hpnicfhgmpStackRole.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpStackRole.setStatus(_A)
_HpnicfhgmpStackMaxPoolNum_Type=Integer32
_HpnicfhgmpStackMaxPoolNum_Object=MibScalar
hpnicfhgmpStackMaxPoolNum=_HpnicfhgmpStackMaxPoolNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,8),_HpnicfhgmpStackMaxPoolNum_Type())
hpnicfhgmpStackMaxPoolNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpStackMaxPoolNum.setStatus(_A)
class _HpnicfhgmpStackMainSwMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_HpnicfhgmpStackMainSwMac_Type.__name__=_F
_HpnicfhgmpStackMainSwMac_Object=MibScalar
hpnicfhgmpStackMainSwMac=_HpnicfhgmpStackMainSwMac_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,9),_HpnicfhgmpStackMainSwMac_Type())
hpnicfhgmpStackMainSwMac.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpStackMainSwMac.setStatus(_A)
class _HpnicfhgmpStackIpPoolMask_Type(IpAddress):defaultHexValue='FFFF0000'
_HpnicfhgmpStackIpPoolMask_Type.__name__=_R
_HpnicfhgmpStackIpPoolMask_Object=MibScalar
hpnicfhgmpStackIpPoolMask=_HpnicfhgmpStackIpPoolMask_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,2,10),_HpnicfhgmpStackIpPoolMask_Type())
hpnicfhgmpStackIpPoolMask.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpStackIpPoolMask.setStatus(_A)
_HpnicfNTDPObject_ObjectIdentity=ObjectIdentity
hpnicfNTDPObject=_HpnicfNTDPObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,7,4))
if mibBuilder.loadTexts:hpnicfNTDPObject.setStatus(_A)
class _HpnicfhgmpNTDPCollectTopTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfhgmpNTDPCollectTopTime_Type.__name__=_C
_HpnicfhgmpNTDPCollectTopTime_Object=MibScalar
hpnicfhgmpNTDPCollectTopTime=_HpnicfhgmpNTDPCollectTopTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,1),_HpnicfhgmpNTDPCollectTopTime_Type())
hpnicfhgmpNTDPCollectTopTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpNTDPCollectTopTime.setStatus(_A)
class _HpnicfhgmpNTDPHopRange_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpnicfhgmpNTDPHopRange_Type.__name__=_C
_HpnicfhgmpNTDPHopRange_Object=MibScalar
hpnicfhgmpNTDPHopRange=_HpnicfhgmpNTDPHopRange_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,2),_HpnicfhgmpNTDPHopRange_Type())
hpnicfhgmpNTDPHopRange.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpNTDPHopRange.setStatus(_A)
class _HpnicfhgmpNTDPRun_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_HpnicfhgmpNTDPRun_Type.__name__=_C
_HpnicfhgmpNTDPRun_Object=MibScalar
hpnicfhgmpNTDPRun=_HpnicfhgmpNTDPRun_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,3),_HpnicfhgmpNTDPRun_Type())
hpnicfhgmpNTDPRun.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpNTDPRun.setStatus(_A)
class _HpnicfhgmpNTDPPortDelay_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpnicfhgmpNTDPPortDelay_Type.__name__=_C
_HpnicfhgmpNTDPPortDelay_Object=MibScalar
hpnicfhgmpNTDPPortDelay=_HpnicfhgmpNTDPPortDelay_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,4),_HpnicfhgmpNTDPPortDelay_Type())
hpnicfhgmpNTDPPortDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpNTDPPortDelay.setStatus(_A)
class _HpnicfhgmpNTDPHopDelay_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_HpnicfhgmpNTDPHopDelay_Type.__name__=_C
_HpnicfhgmpNTDPHopDelay_Object=MibScalar
hpnicfhgmpNTDPHopDelay=_HpnicfhgmpNTDPHopDelay_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,5),_HpnicfhgmpNTDPHopDelay_Type())
hpnicfhgmpNTDPHopDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpNTDPHopDelay.setStatus(_A)
class _HpnicfhgmpNTDPLastTopCollectDuration_Type(Integer32):defaultValue=0
_HpnicfhgmpNTDPLastTopCollectDuration_Type.__name__=_C
_HpnicfhgmpNTDPLastTopCollectDuration_Object=MibScalar
hpnicfhgmpNTDPLastTopCollectDuration=_HpnicfhgmpNTDPLastTopCollectDuration_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,6),_HpnicfhgmpNTDPLastTopCollectDuration_Type())
hpnicfhgmpNTDPLastTopCollectDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPLastTopCollectDuration.setStatus(_A)
class _HpnicfhgmpNTDPCacheChange_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfhgmpNTDPCacheChange_Type.__name__=_C
_HpnicfhgmpNTDPCacheChange_Object=MibScalar
hpnicfhgmpNTDPCacheChange=_HpnicfhgmpNTDPCacheChange_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,7),_HpnicfhgmpNTDPCacheChange_Type())
hpnicfhgmpNTDPCacheChange.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPCacheChange.setStatus(_A)
class _HpnicfhgmpNTDPTOPTableChange_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfhgmpNTDPTOPTableChange_Type.__name__=_C
_HpnicfhgmpNTDPTOPTableChange_Object=MibScalar
hpnicfhgmpNTDPTOPTableChange=_HpnicfhgmpNTDPTOPTableChange_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,8),_HpnicfhgmpNTDPTOPTableChange_Type())
hpnicfhgmpNTDPTOPTableChange.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPTOPTableChange.setStatus(_A)
_HpnicfhgmpNTDPInterfaceTable_Object=MibTable
hpnicfhgmpNTDPInterfaceTable=_HpnicfhgmpNTDPInterfaceTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,9))
if mibBuilder.loadTexts:hpnicfhgmpNTDPInterfaceTable.setStatus(_A)
_HpnicfhgmpNTDPInterfaceEntry_Object=MibTableRow
hpnicfhgmpNTDPInterfaceEntry=_HpnicfhgmpNTDPInterfaceEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,9,1))
hpnicfhgmpNTDPInterfaceEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:hpnicfhgmpNTDPInterfaceEntry.setStatus(_A)
_HpnicfhgmpNTDPInterfaceIfIndex_Type=Integer32
_HpnicfhgmpNTDPInterfaceIfIndex_Object=MibTableColumn
hpnicfhgmpNTDPInterfaceIfIndex=_HpnicfhgmpNTDPInterfaceIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,9,1,1),_HpnicfhgmpNTDPInterfaceIfIndex_Type())
hpnicfhgmpNTDPInterfaceIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPInterfaceIfIndex.setStatus(_A)
class _HpnicfhgmpNTDPInterfaceEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_HpnicfhgmpNTDPInterfaceEnable_Type.__name__=_C
_HpnicfhgmpNTDPInterfaceEnable_Object=MibTableColumn
hpnicfhgmpNTDPInterfaceEnable=_HpnicfhgmpNTDPInterfaceEnable_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,9,1,2),_HpnicfhgmpNTDPInterfaceEnable_Type())
hpnicfhgmpNTDPInterfaceEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfhgmpNTDPInterfaceEnable.setStatus(_A)
_HpnicfhgmpNTDPCacheTable_Object=MibTable
hpnicfhgmpNTDPCacheTable=_HpnicfhgmpNTDPCacheTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,10))
if mibBuilder.loadTexts:hpnicfhgmpNTDPCacheTable.setStatus(_A)
_HpnicfhgmpNTDPCacheEntry_Object=MibTableRow
hpnicfhgmpNTDPCacheEntry=_HpnicfhgmpNTDPCacheEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,10,1))
hpnicfhgmpNTDPCacheEntry.setIndexNames((0,_E,_e),(0,_E,_f))
if mibBuilder.loadTexts:hpnicfhgmpNTDPCacheEntry.setStatus(_A)
class _HpnicfhgmpNTDPCacheHashIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfhgmpNTDPCacheHashIndex_Type.__name__=_C
_HpnicfhgmpNTDPCacheHashIndex_Object=MibTableColumn
hpnicfhgmpNTDPCacheHashIndex=_HpnicfhgmpNTDPCacheHashIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,10,1,1),_HpnicfhgmpNTDPCacheHashIndex_Type())
hpnicfhgmpNTDPCacheHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPCacheHashIndex.setStatus(_A)
class _HpnicfhgmpNTDPCacheDeviceID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HpnicfhgmpNTDPCacheDeviceID_Type.__name__=_F
_HpnicfhgmpNTDPCacheDeviceID_Object=MibTableColumn
hpnicfhgmpNTDPCacheDeviceID=_HpnicfhgmpNTDPCacheDeviceID_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,10,1,2),_HpnicfhgmpNTDPCacheDeviceID_Type())
hpnicfhgmpNTDPCacheDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPCacheDeviceID.setStatus(_A)
_HpnicfhgmpNTDPCacheClusterName_Type=OctetString
_HpnicfhgmpNTDPCacheClusterName_Object=MibTableColumn
hpnicfhgmpNTDPCacheClusterName=_HpnicfhgmpNTDPCacheClusterName_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,10,1,3),_HpnicfhgmpNTDPCacheClusterName_Type())
hpnicfhgmpNTDPCacheClusterName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPCacheClusterName.setStatus(_A)
class _HpnicfhgmpNTDPCacheClusterRole_Type(Integer32):defaultValue=17;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,16,17)));namedValues=NamedValues(*(('roleCOSW',1),('roleMSW',2),('roleBKSW',3),(_L,16),(_M,17)))
_HpnicfhgmpNTDPCacheClusterRole_Type.__name__=_C
_HpnicfhgmpNTDPCacheClusterRole_Object=MibTableColumn
hpnicfhgmpNTDPCacheClusterRole=_HpnicfhgmpNTDPCacheClusterRole_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,10,1,4),_HpnicfhgmpNTDPCacheClusterRole_Type())
hpnicfhgmpNTDPCacheClusterRole.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPCacheClusterRole.setStatus(_A)
class _HpnicfhgmpNTDPCacheCapabilities_Type(Integer32):defaultValue=255
_HpnicfhgmpNTDPCacheCapabilities_Type.__name__=_C
_HpnicfhgmpNTDPCacheCapabilities_Object=MibTableColumn
hpnicfhgmpNTDPCacheCapabilities=_HpnicfhgmpNTDPCacheCapabilities_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,10,1,5),_HpnicfhgmpNTDPCacheCapabilities_Type())
hpnicfhgmpNTDPCacheCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPCacheCapabilities.setStatus(_A)
_HpnicfhgmpNTDPCacheVersion_Type=OctetString
_HpnicfhgmpNTDPCacheVersion_Object=MibTableColumn
hpnicfhgmpNTDPCacheVersion=_HpnicfhgmpNTDPCacheVersion_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,10,1,6),_HpnicfhgmpNTDPCacheVersion_Type())
hpnicfhgmpNTDPCacheVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPCacheVersion.setStatus(_A)
_HpnicfhgmpNTDPCachePlatform_Type=OctetString
_HpnicfhgmpNTDPCachePlatform_Object=MibTableColumn
hpnicfhgmpNTDPCachePlatform=_HpnicfhgmpNTDPCachePlatform_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,10,1,7),_HpnicfhgmpNTDPCachePlatform_Type())
hpnicfhgmpNTDPCachePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPCachePlatform.setStatus(_A)
class _HpnicfhgmpNTDPCacheMngVLAN_Type(Integer32):defaultValue=1
_HpnicfhgmpNTDPCacheMngVLAN_Type.__name__=_C
_HpnicfhgmpNTDPCacheMngVLAN_Object=MibTableColumn
hpnicfhgmpNTDPCacheMngVLAN=_HpnicfhgmpNTDPCacheMngVLAN_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,10,1,8),_HpnicfhgmpNTDPCacheMngVLAN_Type())
hpnicfhgmpNTDPCacheMngVLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPCacheMngVLAN.setStatus(_A)
_HpnicfhgmpNTDPCacheHop_Type=Integer32
_HpnicfhgmpNTDPCacheHop_Object=MibTableColumn
hpnicfhgmpNTDPCacheHop=_HpnicfhgmpNTDPCacheHop_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,10,1,9),_HpnicfhgmpNTDPCacheHop_Type())
hpnicfhgmpNTDPCacheHop.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPCacheHop.setStatus(_A)
_HpnicfhgmpNTDPTopTable_Object=MibTable
hpnicfhgmpNTDPTopTable=_HpnicfhgmpNTDPTopTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,11))
if mibBuilder.loadTexts:hpnicfhgmpNTDPTopTable.setStatus(_A)
_HpnicfhgmpNTDPTopEntry_Object=MibTableRow
hpnicfhgmpNTDPTopEntry=_HpnicfhgmpNTDPTopEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,11,1))
hpnicfhgmpNTDPTopEntry.setIndexNames((0,_E,_g),(0,_E,_h),(0,_E,_i))
if mibBuilder.loadTexts:hpnicfhgmpNTDPTopEntry.setStatus(_A)
class _HpnicfhgmpNTDPTopHashIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfhgmpNTDPTopHashIndex_Type.__name__=_C
_HpnicfhgmpNTDPTopHashIndex_Object=MibTableColumn
hpnicfhgmpNTDPTopHashIndex=_HpnicfhgmpNTDPTopHashIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,11,1,1),_HpnicfhgmpNTDPTopHashIndex_Type())
hpnicfhgmpNTDPTopHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPTopHashIndex.setStatus(_A)
class _HpnicfhgmpNTDPTopEdgeStartDevID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HpnicfhgmpNTDPTopEdgeStartDevID_Type.__name__=_F
_HpnicfhgmpNTDPTopEdgeStartDevID_Object=MibTableColumn
hpnicfhgmpNTDPTopEdgeStartDevID=_HpnicfhgmpNTDPTopEdgeStartDevID_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,11,1,2),_HpnicfhgmpNTDPTopEdgeStartDevID_Type())
hpnicfhgmpNTDPTopEdgeStartDevID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPTopEdgeStartDevID.setStatus(_A)
class _HpnicfhgmpNTDPTopEdgeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfhgmpNTDPTopEdgeIndex_Type.__name__=_C
_HpnicfhgmpNTDPTopEdgeIndex_Object=MibTableColumn
hpnicfhgmpNTDPTopEdgeIndex=_HpnicfhgmpNTDPTopEdgeIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,11,1,3),_HpnicfhgmpNTDPTopEdgeIndex_Type())
hpnicfhgmpNTDPTopEdgeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPTopEdgeIndex.setStatus(_A)
class _HpnicfhgmpNTDPTopEdgeEndDevID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HpnicfhgmpNTDPTopEdgeEndDevID_Type.__name__=_F
_HpnicfhgmpNTDPTopEdgeEndDevID_Object=MibTableColumn
hpnicfhgmpNTDPTopEdgeEndDevID=_HpnicfhgmpNTDPTopEdgeEndDevID_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,11,1,4),_HpnicfhgmpNTDPTopEdgeEndDevID_Type())
hpnicfhgmpNTDPTopEdgeEndDevID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPTopEdgeEndDevID.setStatus(_A)
class _HpnicfhgmpNTDPTopEdgeStartPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_HpnicfhgmpNTDPTopEdgeStartPort_Type.__name__=_F
_HpnicfhgmpNTDPTopEdgeStartPort_Object=MibTableColumn
hpnicfhgmpNTDPTopEdgeStartPort=_HpnicfhgmpNTDPTopEdgeStartPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,11,1,5),_HpnicfhgmpNTDPTopEdgeStartPort_Type())
hpnicfhgmpNTDPTopEdgeStartPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPTopEdgeStartPort.setStatus(_A)
class _HpnicfhgmpNTDPTopEdgeStartPortFullDuplex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('half',0),('full',1)))
_HpnicfhgmpNTDPTopEdgeStartPortFullDuplex_Type.__name__=_C
_HpnicfhgmpNTDPTopEdgeStartPortFullDuplex_Object=MibTableColumn
hpnicfhgmpNTDPTopEdgeStartPortFullDuplex=_HpnicfhgmpNTDPTopEdgeStartPortFullDuplex_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,11,1,6),_HpnicfhgmpNTDPTopEdgeStartPortFullDuplex_Type())
hpnicfhgmpNTDPTopEdgeStartPortFullDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPTopEdgeStartPortFullDuplex.setStatus(_A)
class _HpnicfhgmpNTDPTopEdgeStartPortSpeed_Type(Integer32):defaultValue=0
_HpnicfhgmpNTDPTopEdgeStartPortSpeed_Type.__name__=_C
_HpnicfhgmpNTDPTopEdgeStartPortSpeed_Object=MibTableColumn
hpnicfhgmpNTDPTopEdgeStartPortSpeed=_HpnicfhgmpNTDPTopEdgeStartPortSpeed_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,11,1,7),_HpnicfhgmpNTDPTopEdgeStartPortSpeed_Type())
hpnicfhgmpNTDPTopEdgeStartPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPTopEdgeStartPortSpeed.setStatus(_A)
class _HpnicfhgmpNTDPTopEdgeEndPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_HpnicfhgmpNTDPTopEdgeEndPort_Type.__name__=_F
_HpnicfhgmpNTDPTopEdgeEndPort_Object=MibTableColumn
hpnicfhgmpNTDPTopEdgeEndPort=_HpnicfhgmpNTDPTopEdgeEndPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,11,1,8),_HpnicfhgmpNTDPTopEdgeEndPort_Type())
hpnicfhgmpNTDPTopEdgeEndPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPTopEdgeEndPort.setStatus(_A)
class _HpnicfhgmpNTDPTopLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forwarding',1),('blocking',2)))
_HpnicfhgmpNTDPTopLinkStatus_Type.__name__=_C
_HpnicfhgmpNTDPTopLinkStatus_Object=MibTableColumn
hpnicfhgmpNTDPTopLinkStatus=_HpnicfhgmpNTDPTopLinkStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,4,11,1,11),_HpnicfhgmpNTDPTopLinkStatus_Type())
hpnicfhgmpNTDPTopLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfhgmpNTDPTopLinkStatus.setStatus(_A)
_HpnicfNDPObject_ObjectIdentity=ObjectIdentity
hpnicfNDPObject=_HpnicfNDPObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,7,5))
if mibBuilder.loadTexts:hpnicfNDPObject.setStatus(_A)
class _HpnicfNDPStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_j,0),(_k,1)))
_HpnicfNDPStatus_Type.__name__=_C
_HpnicfNDPStatus_Object=MibScalar
hpnicfNDPStatus=_HpnicfNDPStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,1),_HpnicfNDPStatus_Type())
hpnicfNDPStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNDPStatus.setStatus(_A)
class _HpnicfNDPHelloTimer_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,254))
_HpnicfNDPHelloTimer_Type.__name__=_C
_HpnicfNDPHelloTimer_Object=MibScalar
hpnicfNDPHelloTimer=_HpnicfNDPHelloTimer_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,2),_HpnicfNDPHelloTimer_Type())
hpnicfNDPHelloTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNDPHelloTimer.setStatus(_A)
class _HpnicfNDPAgingTime_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,255))
_HpnicfNDPAgingTime_Type.__name__=_C
_HpnicfNDPAgingTime_Object=MibScalar
hpnicfNDPAgingTime=_HpnicfNDPAgingTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,3),_HpnicfNDPAgingTime_Type())
hpnicfNDPAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNDPAgingTime.setStatus(_A)
class _HpnicfNDPChange_Type(Counter32):defaultValue=0
_HpnicfNDPChange_Type.__name__=_Q
_HpnicfNDPChange_Object=MibScalar
hpnicfNDPChange=_HpnicfNDPChange_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,4),_HpnicfNDPChange_Type())
hpnicfNDPChange.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNDPChange.setStatus(_A)
_HpnicfNDPPortTable_Object=MibTable
hpnicfNDPPortTable=_HpnicfNDPPortTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,5))
if mibBuilder.loadTexts:hpnicfNDPPortTable.setStatus(_A)
_HpnicfNDPPortEntry_Object=MibTableRow
hpnicfNDPPortEntry=_HpnicfNDPPortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,5,1))
hpnicfNDPPortEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:hpnicfNDPPortEntry.setStatus(_A)
_HpnicfNDPIfIndex_Type=Integer32
_HpnicfNDPIfIndex_Object=MibTableColumn
hpnicfNDPIfIndex=_HpnicfNDPIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,5,1,1),_HpnicfNDPIfIndex_Type())
hpnicfNDPIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNDPIfIndex.setStatus(_A)
class _HpnicfNDPPortStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_j,0),(_k,1)))
_HpnicfNDPPortStatus_Type.__name__=_C
_HpnicfNDPPortStatus_Object=MibTableColumn
hpnicfNDPPortStatus=_HpnicfNDPPortStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,5,1,2),_HpnicfNDPPortStatus_Type())
hpnicfNDPPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNDPPortStatus.setStatus(_A)
_HpnicfNDPPortNbTable_Object=MibTable
hpnicfNDPPortNbTable=_HpnicfNDPPortNbTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,6))
if mibBuilder.loadTexts:hpnicfNDPPortNbTable.setStatus(_A)
_HpnicfNDPPortNbEntry_Object=MibTableRow
hpnicfNDPPortNbEntry=_HpnicfNDPPortNbEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,6,1))
hpnicfNDPPortNbEntry.setIndexNames((0,_E,_O),(0,_E,_l),(0,_E,_m))
if mibBuilder.loadTexts:hpnicfNDPPortNbEntry.setStatus(_A)
class _HpnicfNDPPortNbDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HpnicfNDPPortNbDeviceId_Type.__name__=_F
_HpnicfNDPPortNbDeviceId_Object=MibTableColumn
hpnicfNDPPortNbDeviceId=_HpnicfNDPPortNbDeviceId_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,6,1,1),_HpnicfNDPPortNbDeviceId_Type())
hpnicfNDPPortNbDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNDPPortNbDeviceId.setStatus(_A)
class _HpnicfNDPPortNbPortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_HpnicfNDPPortNbPortName_Type.__name__=_F
_HpnicfNDPPortNbPortName_Object=MibTableColumn
hpnicfNDPPortNbPortName=_HpnicfNDPPortNbPortName_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,6,1,2),_HpnicfNDPPortNbPortName_Type())
hpnicfNDPPortNbPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNDPPortNbPortName.setStatus(_A)
_HpnicfNDPPortNbDeviceName_Type=OctetString
_HpnicfNDPPortNbDeviceName_Object=MibTableColumn
hpnicfNDPPortNbDeviceName=_HpnicfNDPPortNbDeviceName_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,6,1,3),_HpnicfNDPPortNbDeviceName_Type())
hpnicfNDPPortNbDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNDPPortNbDeviceName.setStatus(_A)
class _HpnicfNDPPortNbPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('full',1),('half',2),('auto',3)))
_HpnicfNDPPortNbPortMode_Type.__name__=_C
_HpnicfNDPPortNbPortMode_Object=MibTableColumn
hpnicfNDPPortNbPortMode=_HpnicfNDPPortNbPortMode_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,6,1,4),_HpnicfNDPPortNbPortMode_Type())
hpnicfNDPPortNbPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNDPPortNbPortMode.setStatus(_A)
_HpnicfNDPPortNbProductVer_Type=OctetString
_HpnicfNDPPortNbProductVer_Object=MibTableColumn
hpnicfNDPPortNbProductVer=_HpnicfNDPPortNbProductVer_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,6,1,5),_HpnicfNDPPortNbProductVer_Type())
hpnicfNDPPortNbProductVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNDPPortNbProductVer.setStatus(_A)
_HpnicfNDPPortNbHardVer_Type=OctetString
_HpnicfNDPPortNbHardVer_Object=MibTableColumn
hpnicfNDPPortNbHardVer=_HpnicfNDPPortNbHardVer_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,6,1,6),_HpnicfNDPPortNbHardVer_Type())
hpnicfNDPPortNbHardVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNDPPortNbHardVer.setStatus(_A)
_HpnicfNDPPortNbBootromVer_Type=OctetString
_HpnicfNDPPortNbBootromVer_Object=MibTableColumn
hpnicfNDPPortNbBootromVer=_HpnicfNDPPortNbBootromVer_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,6,1,7),_HpnicfNDPPortNbBootromVer_Type())
hpnicfNDPPortNbBootromVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNDPPortNbBootromVer.setStatus(_A)
_HpnicfNDPPortNbSoftVer_Type=OctetString
_HpnicfNDPPortNbSoftVer_Object=MibTableColumn
hpnicfNDPPortNbSoftVer=_HpnicfNDPPortNbSoftVer_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,6,1,8),_HpnicfNDPPortNbSoftVer_Type())
hpnicfNDPPortNbSoftVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNDPPortNbSoftVer.setStatus(_A)
class _HpnicfNDPPortNbAgingtime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,255))
_HpnicfNDPPortNbAgingtime_Type.__name__=_C
_HpnicfNDPPortNbAgingtime_Object=MibTableColumn
hpnicfNDPPortNbAgingtime=_HpnicfNDPPortNbAgingtime_Object((1,3,6,1,4,1,11,2,14,11,15,8,7,5,6,1,9),_HpnicfNDPPortNbAgingtime_Type())
hpnicfNDPPortNbAgingtime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNDPPortNbAgingtime.setStatus(_A)
hpnicfhgmpMemberfailure=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,7,1,0,1))
hpnicfhgmpMemberfailure.setObjects((_E,_I))
if mibBuilder.loadTexts:hpnicfhgmpMemberfailure.setStatus(_A)
hpnicfhgmpMemberRecover=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,7,1,0,2))
hpnicfhgmpMemberRecover.setObjects((_E,_I))
if mibBuilder.loadTexts:hpnicfhgmpMemberRecover.setStatus(_A)
hpnicfhgmpMemberStatusChange=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,7,1,0,3))
hpnicfhgmpMemberStatusChange.setObjects(*((_E,_I),(_E,_P)))
if mibBuilder.loadTexts:hpnicfhgmpMemberStatusChange.setStatus(_A)
hpnicfhgmpNetTopChange=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,7,1,0,4))
if mibBuilder.loadTexts:hpnicfhgmpNetTopChange.setStatus(_A)
hpnicfhgmpStackMemberfailure=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,7,2,0,1))
hpnicfhgmpStackMemberfailure.setObjects((_E,_J))
if mibBuilder.loadTexts:hpnicfhgmpStackMemberfailure.setStatus(_A)
hpnicfhgmpStackMemberRecover=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,7,2,0,2))
hpnicfhgmpStackMemberRecover.setObjects((_E,_J))
if mibBuilder.loadTexts:hpnicfhgmpStackMemberRecover.setStatus(_A)
hpnicfhgmpStackMemberStatusChange=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,7,2,0,3))
hpnicfhgmpStackMemberStatusChange.setObjects(*((_E,_J),(_E,_P)))
if mibBuilder.loadTexts:hpnicfhgmpStackMemberStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hpnicfHgmp':hpnicfHgmp,'hpnicfClusterObject':hpnicfClusterObject,'hpnicfhgmpEventsV2':hpnicfhgmpEventsV2,'hpnicfhgmpMemberfailure':hpnicfhgmpMemberfailure,'hpnicfhgmpMemberRecover':hpnicfhgmpMemberRecover,'hpnicfhgmpMemberStatusChange':hpnicfhgmpMemberStatusChange,'hpnicfhgmpNetTopChange':hpnicfhgmpNetTopChange,'hpnicfhgmpSetVLANSecurity':hpnicfhgmpSetVLANSecurity,'hpnicfhgmpHandShakeInterval':hpnicfhgmpHandShakeInterval,'hpnicfhgmpHandShakeHoldtime':hpnicfhgmpHandShakeHoldtime,'hpnicfhgmpGrpMemberTableChange':hpnicfhgmpGrpMemberTableChange,'hpnicfhgmpMemberDisconRate':hpnicfhgmpMemberDisconRate,'hpnicfhgmpCmdLanswitchFlag':hpnicfhgmpCmdLanswitchFlag,'hpnicfhgmpCmdClusterName':hpnicfhgmpCmdClusterName,'hpnicfhgmpMngPriIpSegCMIP':hpnicfhgmpMngPriIpSegCMIP,'hpnicfhgmpMngPriIpMask':hpnicfhgmpMngPriIpMask,'hpnicfhgmpFtpServer':hpnicfhgmpFtpServer,'hpnicfhgmpTftpServer':hpnicfhgmpTftpServer,'hpnicfhgmpSnmpHost':hpnicfhgmpSnmpHost,'hpnicfhgmpLogHost':hpnicfhgmpLogHost,'hpnicfhgmpGrpMemberTable':hpnicfhgmpGrpMemberTable,'hpnicfhgmpGrpMemberEntry':hpnicfhgmpGrpMemberEntry,_I:hpnicfhgmpGrpMemberDeviceId,'hpnicfhgmpGrpMemberSerial':hpnicfhgmpGrpMemberSerial,'hpnicfhgmpGrpMemberIpAddr':hpnicfhgmpGrpMemberIpAddr,'hpnicfhgmpGrpMemberName':hpnicfhgmpGrpMemberName,'hpnicfhgmpGrpMemberPassword':hpnicfhgmpGrpMemberPassword,'hpnicfhgmpGrpMemberPlatform':hpnicfhgmpGrpMemberPlatform,'hpnicfhgmpGrpMemberStatus':hpnicfhgmpGrpMemberStatus,'hpnicfhgmpGrpMemberDisconCount':hpnicfhgmpGrpMemberDisconCount,'hpnicfhgmpGrpMemberEnrollTime':hpnicfhgmpGrpMemberEnrollTime,'hpnicfhgmpGrpMemberOperate':hpnicfhgmpGrpMemberOperate,'hpnicfhgmpMemberResetTable':hpnicfhgmpMemberResetTable,'hpnicfhgmpMemberResetEntry':hpnicfhgmpMemberResetEntry,_U:hpnicfhgmpMemberResetMAC,'hpnicfhgmpMemberEraseflash':hpnicfhgmpMemberEraseflash,'hpnicfhgmpClusterRole':hpnicfhgmpClusterRole,'hpnicfhgmpClusterMaxPoolNum':hpnicfhgmpClusterMaxPoolNum,'hpnicfhgmpClusterCmdSwMac':hpnicfhgmpClusterCmdSwMac,'hpnicfhgmpRun':hpnicfhgmpRun,'hpnicfhgmpProtocolMac':hpnicfhgmpProtocolMac,'hpnicfhgmpClusterProtocolMac':hpnicfhgmpClusterProtocolMac,'hpnicfhgmpTopologyManagement':hpnicfhgmpTopologyManagement,'hpnicfhgmpWhitelistTable':hpnicfhgmpWhitelistTable,'hpnicfhgmpWhitelistEntry':hpnicfhgmpWhitelistEntry,_N:hpnicfhgmpWhitelistDeviceId,'hpnicfhgmpWhitelistSerial':hpnicfhgmpWhitelistSerial,'hpnicfhgmpWhitelistRowStatus':hpnicfhgmpWhitelistRowStatus,'hpnicfhgmpWhitelistNbTable':hpnicfhgmpWhitelistNbTable,'hpnicfhgmpWhitelistNbEntry':hpnicfhgmpWhitelistNbEntry,_Z:hpnicfhgmpWhitelistNbIndex,'hpnicfhgmpWhitelistNbDeviceId':hpnicfhgmpWhitelistNbDeviceId,'hpnicfhgmpWhitelistPortName':hpnicfhgmpWhitelistPortName,'hpnicfhgmpWhitelistNbPortName':hpnicfhgmpWhitelistNbPortName,'hpnicfhgmpBlacklistTable':hpnicfhgmpBlacklistTable,'hpnicfhgmpBlacklistEntry':hpnicfhgmpBlacklistEntry,_a:hpnicfhgmpBlacklistDeviceId,'hpnicfhgmpBlacklistAccessDeviceId':hpnicfhgmpBlacklistAccessDeviceId,'hpnicfhgmpBlacklistAccessPortName':hpnicfhgmpBlacklistAccessPortName,'hpnicfhgmpBlacklistRowStatus':hpnicfhgmpBlacklistRowStatus,'hpnicfhgmpMemberPriPortTable':hpnicfhgmpMemberPriPortTable,'hpnicfhgmpMemberPriPortEntry':hpnicfhgmpMemberPriPortEntry,_b:hpnicfhgmpMemberDevId,_c:hpnicfhgmpMemberPriPortProto,'hpnicfhgmpMemberPriPortProtoDescr':hpnicfhgmpMemberPriPortProtoDescr,'hpnicfhgmpMemberPriPortNum':hpnicfhgmpMemberPriPortNum,'hpnicfStackObject':hpnicfStackObject,'hpnicfhgmpStackEventsV2':hpnicfhgmpStackEventsV2,'hpnicfhgmpStackMemberfailure':hpnicfhgmpStackMemberfailure,'hpnicfhgmpStackMemberRecover':hpnicfhgmpStackMemberRecover,'hpnicfhgmpStackMemberStatusChange':hpnicfhgmpStackMemberStatusChange,'hpnicfhgmpStackMemberTableChange':hpnicfhgmpStackMemberTableChange,'hpnicfhgmpStackMemberDisconRate':hpnicfhgmpStackMemberDisconRate,'hpnicfhgmpMainLanswitchFlag':hpnicfhgmpMainLanswitchFlag,'hpnicfhgmpStackIpPoolStartIP':hpnicfhgmpStackIpPoolStartIP,'hpnicfhgmpStackIpPoolLength':hpnicfhgmpStackIpPoolLength,'hpnicfhgmpStackMemberTable':hpnicfhgmpStackMemberTable,'hpnicfhgmpStackMemberEntry':hpnicfhgmpStackMemberEntry,_J:hpnicfhgmpStackMemberDeviceId,'hpnicfhgmpStackMemberSerial':hpnicfhgmpStackMemberSerial,'hpnicfhgmpStackMemberIpAddr':hpnicfhgmpStackMemberIpAddr,'hpnicfhgmpStackMemberName':hpnicfhgmpStackMemberName,'hpnicfhgmpStackMemberPassword':hpnicfhgmpStackMemberPassword,'hpnicfhgmpStackMemberPlatform':hpnicfhgmpStackMemberPlatform,'hpnicfhgmpStackMemberStatus':hpnicfhgmpStackMemberStatus,'hpnicfhgmpStackMemberDisconCount':hpnicfhgmpStackMemberDisconCount,'hpnicfhgmpStackMemberEnrollTime':hpnicfhgmpStackMemberEnrollTime,'hpnicfhgmpStackRole':hpnicfhgmpStackRole,'hpnicfhgmpStackMaxPoolNum':hpnicfhgmpStackMaxPoolNum,'hpnicfhgmpStackMainSwMac':hpnicfhgmpStackMainSwMac,'hpnicfhgmpStackIpPoolMask':hpnicfhgmpStackIpPoolMask,'hpnicfNTDPObject':hpnicfNTDPObject,'hpnicfhgmpNTDPCollectTopTime':hpnicfhgmpNTDPCollectTopTime,'hpnicfhgmpNTDPHopRange':hpnicfhgmpNTDPHopRange,'hpnicfhgmpNTDPRun':hpnicfhgmpNTDPRun,'hpnicfhgmpNTDPPortDelay':hpnicfhgmpNTDPPortDelay,'hpnicfhgmpNTDPHopDelay':hpnicfhgmpNTDPHopDelay,'hpnicfhgmpNTDPLastTopCollectDuration':hpnicfhgmpNTDPLastTopCollectDuration,'hpnicfhgmpNTDPCacheChange':hpnicfhgmpNTDPCacheChange,'hpnicfhgmpNTDPTOPTableChange':hpnicfhgmpNTDPTOPTableChange,'hpnicfhgmpNTDPInterfaceTable':hpnicfhgmpNTDPInterfaceTable,'hpnicfhgmpNTDPInterfaceEntry':hpnicfhgmpNTDPInterfaceEntry,_d:hpnicfhgmpNTDPInterfaceIfIndex,'hpnicfhgmpNTDPInterfaceEnable':hpnicfhgmpNTDPInterfaceEnable,'hpnicfhgmpNTDPCacheTable':hpnicfhgmpNTDPCacheTable,'hpnicfhgmpNTDPCacheEntry':hpnicfhgmpNTDPCacheEntry,_e:hpnicfhgmpNTDPCacheHashIndex,_f:hpnicfhgmpNTDPCacheDeviceID,'hpnicfhgmpNTDPCacheClusterName':hpnicfhgmpNTDPCacheClusterName,_P:hpnicfhgmpNTDPCacheClusterRole,'hpnicfhgmpNTDPCacheCapabilities':hpnicfhgmpNTDPCacheCapabilities,'hpnicfhgmpNTDPCacheVersion':hpnicfhgmpNTDPCacheVersion,'hpnicfhgmpNTDPCachePlatform':hpnicfhgmpNTDPCachePlatform,'hpnicfhgmpNTDPCacheMngVLAN':hpnicfhgmpNTDPCacheMngVLAN,'hpnicfhgmpNTDPCacheHop':hpnicfhgmpNTDPCacheHop,'hpnicfhgmpNTDPTopTable':hpnicfhgmpNTDPTopTable,'hpnicfhgmpNTDPTopEntry':hpnicfhgmpNTDPTopEntry,_g:hpnicfhgmpNTDPTopHashIndex,_h:hpnicfhgmpNTDPTopEdgeStartDevID,_i:hpnicfhgmpNTDPTopEdgeIndex,'hpnicfhgmpNTDPTopEdgeEndDevID':hpnicfhgmpNTDPTopEdgeEndDevID,'hpnicfhgmpNTDPTopEdgeStartPort':hpnicfhgmpNTDPTopEdgeStartPort,'hpnicfhgmpNTDPTopEdgeStartPortFullDuplex':hpnicfhgmpNTDPTopEdgeStartPortFullDuplex,'hpnicfhgmpNTDPTopEdgeStartPortSpeed':hpnicfhgmpNTDPTopEdgeStartPortSpeed,'hpnicfhgmpNTDPTopEdgeEndPort':hpnicfhgmpNTDPTopEdgeEndPort,'hpnicfhgmpNTDPTopLinkStatus':hpnicfhgmpNTDPTopLinkStatus,'hpnicfNDPObject':hpnicfNDPObject,'hpnicfNDPStatus':hpnicfNDPStatus,'hpnicfNDPHelloTimer':hpnicfNDPHelloTimer,'hpnicfNDPAgingTime':hpnicfNDPAgingTime,'hpnicfNDPChange':hpnicfNDPChange,'hpnicfNDPPortTable':hpnicfNDPPortTable,'hpnicfNDPPortEntry':hpnicfNDPPortEntry,_O:hpnicfNDPIfIndex,'hpnicfNDPPortStatus':hpnicfNDPPortStatus,'hpnicfNDPPortNbTable':hpnicfNDPPortNbTable,'hpnicfNDPPortNbEntry':hpnicfNDPPortNbEntry,_l:hpnicfNDPPortNbDeviceId,_m:hpnicfNDPPortNbPortName,'hpnicfNDPPortNbDeviceName':hpnicfNDPPortNbDeviceName,'hpnicfNDPPortNbPortMode':hpnicfNDPPortNbPortMode,'hpnicfNDPPortNbProductVer':hpnicfNDPPortNbProductVer,'hpnicfNDPPortNbHardVer':hpnicfNDPPortNbHardVer,'hpnicfNDPPortNbBootromVer':hpnicfNDPPortNbBootromVer,'hpnicfNDPPortNbSoftVer':hpnicfNDPPortNbSoftVer,'hpnicfNDPPortNbAgingtime':hpnicfNDPPortNbAgingtime})