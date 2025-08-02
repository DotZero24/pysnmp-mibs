_A4='ciscoVPNSharedLicOptUsageGroup'
_A3='ciscoVPNSharedLicUsageMandatoryGroup'
_A2='cvpnLicClntInfoTransferReqError'
_A1='cvpnLicClntInfoTransferReqRx'
_A0='cvpnLicClntInfoTransferReqTx'
_z='cvpnLicClntInfoRelReqError'
_y='cvpnLicClntInfoRelReqRx'
_x='cvpnLicClntInfoRelReqTx'
_w='cvpnLicClntInfoGetReqError'
_v='cvpnLicClntInfoGetReqRx'
_u='cvpnLicClntInfoGetReqTx'
_t='cvpnLicClntInfoRegReqError'
_s='cvpnLicClntInfoRegReqRx'
_r='cvpnLicClntInfoRegReqTx'
_q='cvpnLicServerUpdateError'
_p='cvpnLicServerUpdateRx'
_o='cvpnLicServerUpdateTx'
_n='cvpnLicServerSyncError'
_m='cvpnLicServerSyncRx'
_l='cvpnLicServerSyncTx'
_k='cvpnLicServerHelloError'
_j='cvpnLicServerHelloRx'
_i='cvpnLicServerHelloTx'
_h='cvpnLicBkpServerStatus'
_g='cvpnLicBkpServerHAPeerRegd'
_f='cvpnLicBkpServerHAPeerDevID'
_e='cvpnLicBkpServerRegd'
_d='cvpnLicBkpServerVer'
_c='cvpnLicBkpServerDevID'
_b='cvpnLicBkpServerAddr'
_a='cvpnLicBkpServerAddrType'
_Z='cvpnLicClntInfoHigh'
_Y='cvpnLicClntInfoCurUsage'
_X='cvpnLicClntInfoPlatLmt'
_W='cvpnLicClntInfoHostName'
_V='cvpnLicServerUtilized'
_U='cvpnLicServerNumLicAvail'
_T='cvpnLicServerNumLicCapacity'
_S='cvpnLicServerStatus'
_R='cvpnLicServerVer'
_Q='cvpnLicBkpSerAddr'
_P='cvpnLicBkpSerAddrType'
_O='cvpnLicServerAddr'
_N='cvpnLicServerAddrType'
_M='cvpnLicDeviceRole'
_L='cvpnLicClntInfoDeviceID'
_K='cvpnLicClntVPNLicType'
_J='cvpnLicServerVPNLicType'
_I='Integer32'
_H='not-accessible'
_G='Unsigned32'
_F='SnmpAdminString'
_E='license'
_D='packets'
_C='read-only'
_B='CISCO-VPN-LIC-USAGE-MONITOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoVpnLicUsageMonitorMIB=ModuleIdentity((1,3,6,1,4,1,9,9,816))
if mibBuilder.loadTexts:ciscoVpnLicUsageMonitorMIB.setRevisions(('2013-09-13 00:00',))
class VPNLicType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('anyconnectpremium',2)))
class VPNLicDeviceRole(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('server',1),('bkpserver',2),('client',3)))
class LicServerStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('inactive',2),('expired',3)))
class LicServerRegistered(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('no',1),('yes',2),('invalid',3)))
_CiscoVpnLicUsageMonitorMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVpnLicUsageMonitorMIBObjects=_CiscoVpnLicUsageMonitorMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,816,0))
_CvpnLicDeviceRole_Type=VPNLicDeviceRole
_CvpnLicDeviceRole_Object=MibScalar
cvpnLicDeviceRole=_CvpnLicDeviceRole_Object((1,3,6,1,4,1,9,9,816,0,1),_CvpnLicDeviceRole_Type())
cvpnLicDeviceRole.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicDeviceRole.setStatus(_A)
_CvpnLicServer_ObjectIdentity=ObjectIdentity
cvpnLicServer=_CvpnLicServer_ObjectIdentity((1,3,6,1,4,1,9,9,816,0,2))
_CvpnLicServerAddrType_Type=InetAddressType
_CvpnLicServerAddrType_Object=MibScalar
cvpnLicServerAddrType=_CvpnLicServerAddrType_Object((1,3,6,1,4,1,9,9,816,0,2,1),_CvpnLicServerAddrType_Type())
cvpnLicServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicServerAddrType.setStatus(_A)
_CvpnLicServerAddr_Type=InetAddress
_CvpnLicServerAddr_Object=MibScalar
cvpnLicServerAddr=_CvpnLicServerAddr_Object((1,3,6,1,4,1,9,9,816,0,2,2),_CvpnLicServerAddr_Type())
cvpnLicServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicServerAddr.setStatus(_A)
_CvpnLicBkpSerAddrType_Type=InetAddressType
_CvpnLicBkpSerAddrType_Object=MibScalar
cvpnLicBkpSerAddrType=_CvpnLicBkpSerAddrType_Object((1,3,6,1,4,1,9,9,816,0,2,3),_CvpnLicBkpSerAddrType_Type())
cvpnLicBkpSerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicBkpSerAddrType.setStatus(_A)
_CvpnLicBkpSerAddr_Type=InetAddress
_CvpnLicBkpSerAddr_Object=MibScalar
cvpnLicBkpSerAddr=_CvpnLicBkpSerAddr_Object((1,3,6,1,4,1,9,9,816,0,2,4),_CvpnLicBkpSerAddr_Type())
cvpnLicBkpSerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicBkpSerAddr.setStatus(_A)
class _CvpnLicServerVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvpnLicServerVer_Type.__name__=_I
_CvpnLicServerVer_Object=MibScalar
cvpnLicServerVer=_CvpnLicServerVer_Object((1,3,6,1,4,1,9,9,816,0,2,5),_CvpnLicServerVer_Type())
cvpnLicServerVer.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicServerVer.setStatus(_A)
_CvpnLicServerStatus_Type=LicServerStatus
_CvpnLicServerStatus_Object=MibScalar
cvpnLicServerStatus=_CvpnLicServerStatus_Object((1,3,6,1,4,1,9,9,816,0,2,6),_CvpnLicServerStatus_Type())
cvpnLicServerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicServerStatus.setStatus(_A)
_CvpnLicServerTable_Object=MibTable
cvpnLicServerTable=_CvpnLicServerTable_Object((1,3,6,1,4,1,9,9,816,0,2,7))
if mibBuilder.loadTexts:cvpnLicServerTable.setStatus(_A)
_CvpnLicServerEntry_Object=MibTableRow
cvpnLicServerEntry=_CvpnLicServerEntry_Object((1,3,6,1,4,1,9,9,816,0,2,7,1))
cvpnLicServerEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cvpnLicServerEntry.setStatus(_A)
_CvpnLicServerVPNLicType_Type=VPNLicType
_CvpnLicServerVPNLicType_Object=MibTableColumn
cvpnLicServerVPNLicType=_CvpnLicServerVPNLicType_Object((1,3,6,1,4,1,9,9,816,0,2,7,1,1),_CvpnLicServerVPNLicType_Type())
cvpnLicServerVPNLicType.setMaxAccess(_H)
if mibBuilder.loadTexts:cvpnLicServerVPNLicType.setStatus(_A)
class _CvpnLicServerNumLicCapacity_Type(Unsigned32):defaultValue=0
_CvpnLicServerNumLicCapacity_Type.__name__=_G
_CvpnLicServerNumLicCapacity_Object=MibTableColumn
cvpnLicServerNumLicCapacity=_CvpnLicServerNumLicCapacity_Object((1,3,6,1,4,1,9,9,816,0,2,7,1,2),_CvpnLicServerNumLicCapacity_Type())
cvpnLicServerNumLicCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicServerNumLicCapacity.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicServerNumLicCapacity.setUnits(_E)
class _CvpnLicServerNumLicAvail_Type(Unsigned32):defaultValue=0
_CvpnLicServerNumLicAvail_Type.__name__=_G
_CvpnLicServerNumLicAvail_Object=MibTableColumn
cvpnLicServerNumLicAvail=_CvpnLicServerNumLicAvail_Object((1,3,6,1,4,1,9,9,816,0,2,7,1,3),_CvpnLicServerNumLicAvail_Type())
cvpnLicServerNumLicAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicServerNumLicAvail.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicServerNumLicAvail.setUnits(_E)
class _CvpnLicServerUtilized_Type(Unsigned32):defaultValue=0
_CvpnLicServerUtilized_Type.__name__=_G
_CvpnLicServerUtilized_Object=MibTableColumn
cvpnLicServerUtilized=_CvpnLicServerUtilized_Object((1,3,6,1,4,1,9,9,816,0,2,7,1,4),_CvpnLicServerUtilized_Type())
cvpnLicServerUtilized.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicServerUtilized.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicServerUtilized.setUnits(_E)
_CvpnLicBkpServer_ObjectIdentity=ObjectIdentity
cvpnLicBkpServer=_CvpnLicBkpServer_ObjectIdentity((1,3,6,1,4,1,9,9,816,0,3))
_CvpnLicBkpServerAddrType_Type=InetAddressType
_CvpnLicBkpServerAddrType_Object=MibScalar
cvpnLicBkpServerAddrType=_CvpnLicBkpServerAddrType_Object((1,3,6,1,4,1,9,9,816,0,3,1),_CvpnLicBkpServerAddrType_Type())
cvpnLicBkpServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicBkpServerAddrType.setStatus(_A)
_CvpnLicBkpServerAddr_Type=InetAddress
_CvpnLicBkpServerAddr_Object=MibScalar
cvpnLicBkpServerAddr=_CvpnLicBkpServerAddr_Object((1,3,6,1,4,1,9,9,816,0,3,2),_CvpnLicBkpServerAddr_Type())
cvpnLicBkpServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicBkpServerAddr.setStatus(_A)
class _CvpnLicBkpServerDevID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CvpnLicBkpServerDevID_Type.__name__=_F
_CvpnLicBkpServerDevID_Object=MibScalar
cvpnLicBkpServerDevID=_CvpnLicBkpServerDevID_Object((1,3,6,1,4,1,9,9,816,0,3,3),_CvpnLicBkpServerDevID_Type())
cvpnLicBkpServerDevID.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicBkpServerDevID.setStatus(_A)
_CvpnLicBkpServerVer_Type=Unsigned32
_CvpnLicBkpServerVer_Object=MibScalar
cvpnLicBkpServerVer=_CvpnLicBkpServerVer_Object((1,3,6,1,4,1,9,9,816,0,3,4),_CvpnLicBkpServerVer_Type())
cvpnLicBkpServerVer.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicBkpServerVer.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicBkpServerVer.setUnits(_E)
_CvpnLicBkpServerRegd_Type=LicServerRegistered
_CvpnLicBkpServerRegd_Object=MibScalar
cvpnLicBkpServerRegd=_CvpnLicBkpServerRegd_Object((1,3,6,1,4,1,9,9,816,0,3,5),_CvpnLicBkpServerRegd_Type())
cvpnLicBkpServerRegd.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicBkpServerRegd.setStatus(_A)
class _CvpnLicBkpServerHAPeerDevID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CvpnLicBkpServerHAPeerDevID_Type.__name__=_F
_CvpnLicBkpServerHAPeerDevID_Object=MibScalar
cvpnLicBkpServerHAPeerDevID=_CvpnLicBkpServerHAPeerDevID_Object((1,3,6,1,4,1,9,9,816,0,3,6),_CvpnLicBkpServerHAPeerDevID_Type())
cvpnLicBkpServerHAPeerDevID.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicBkpServerHAPeerDevID.setStatus(_A)
_CvpnLicBkpServerHAPeerRegd_Type=LicServerRegistered
_CvpnLicBkpServerHAPeerRegd_Object=MibScalar
cvpnLicBkpServerHAPeerRegd=_CvpnLicBkpServerHAPeerRegd_Object((1,3,6,1,4,1,9,9,816,0,3,7),_CvpnLicBkpServerHAPeerRegd_Type())
cvpnLicBkpServerHAPeerRegd.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicBkpServerHAPeerRegd.setStatus(_A)
_CvpnLicBkpServerStatus_Type=LicServerStatus
_CvpnLicBkpServerStatus_Object=MibScalar
cvpnLicBkpServerStatus=_CvpnLicBkpServerStatus_Object((1,3,6,1,4,1,9,9,816,0,3,8),_CvpnLicBkpServerStatus_Type())
cvpnLicBkpServerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicBkpServerStatus.setStatus(_A)
_CvpnLicServerHelloTx_Type=Counter32
_CvpnLicServerHelloTx_Object=MibScalar
cvpnLicServerHelloTx=_CvpnLicServerHelloTx_Object((1,3,6,1,4,1,9,9,816,0,3,9),_CvpnLicServerHelloTx_Type())
cvpnLicServerHelloTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicServerHelloTx.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicServerHelloTx.setUnits(_D)
_CvpnLicServerHelloRx_Type=Counter32
_CvpnLicServerHelloRx_Object=MibScalar
cvpnLicServerHelloRx=_CvpnLicServerHelloRx_Object((1,3,6,1,4,1,9,9,816,0,3,10),_CvpnLicServerHelloRx_Type())
cvpnLicServerHelloRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicServerHelloRx.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicServerHelloRx.setUnits(_D)
_CvpnLicServerHelloError_Type=Counter32
_CvpnLicServerHelloError_Object=MibScalar
cvpnLicServerHelloError=_CvpnLicServerHelloError_Object((1,3,6,1,4,1,9,9,816,0,3,11),_CvpnLicServerHelloError_Type())
cvpnLicServerHelloError.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicServerHelloError.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicServerHelloError.setUnits(_D)
_CvpnLicServerSyncTx_Type=Counter32
_CvpnLicServerSyncTx_Object=MibScalar
cvpnLicServerSyncTx=_CvpnLicServerSyncTx_Object((1,3,6,1,4,1,9,9,816,0,3,12),_CvpnLicServerSyncTx_Type())
cvpnLicServerSyncTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicServerSyncTx.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicServerSyncTx.setUnits(_D)
_CvpnLicServerSyncRx_Type=Counter32
_CvpnLicServerSyncRx_Object=MibScalar
cvpnLicServerSyncRx=_CvpnLicServerSyncRx_Object((1,3,6,1,4,1,9,9,816,0,3,13),_CvpnLicServerSyncRx_Type())
cvpnLicServerSyncRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicServerSyncRx.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicServerSyncRx.setUnits(_D)
_CvpnLicServerSyncError_Type=Counter32
_CvpnLicServerSyncError_Object=MibScalar
cvpnLicServerSyncError=_CvpnLicServerSyncError_Object((1,3,6,1,4,1,9,9,816,0,3,14),_CvpnLicServerSyncError_Type())
cvpnLicServerSyncError.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicServerSyncError.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicServerSyncError.setUnits(_D)
_CvpnLicServerUpdateTx_Type=Counter32
_CvpnLicServerUpdateTx_Object=MibScalar
cvpnLicServerUpdateTx=_CvpnLicServerUpdateTx_Object((1,3,6,1,4,1,9,9,816,0,3,15),_CvpnLicServerUpdateTx_Type())
cvpnLicServerUpdateTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicServerUpdateTx.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicServerUpdateTx.setUnits(_D)
_CvpnLicServerUpdateRx_Type=Counter32
_CvpnLicServerUpdateRx_Object=MibScalar
cvpnLicServerUpdateRx=_CvpnLicServerUpdateRx_Object((1,3,6,1,4,1,9,9,816,0,3,16),_CvpnLicServerUpdateRx_Type())
cvpnLicServerUpdateRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicServerUpdateRx.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicServerUpdateRx.setUnits(_D)
_CvpnLicServerUpdateError_Type=Counter32
_CvpnLicServerUpdateError_Object=MibScalar
cvpnLicServerUpdateError=_CvpnLicServerUpdateError_Object((1,3,6,1,4,1,9,9,816,0,3,17),_CvpnLicServerUpdateError_Type())
cvpnLicServerUpdateError.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicServerUpdateError.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicServerUpdateError.setUnits(_D)
_CvpnLicClient_ObjectIdentity=ObjectIdentity
cvpnLicClient=_CvpnLicClient_ObjectIdentity((1,3,6,1,4,1,9,9,816,0,4))
_CvpnLicClntInfoTable_Object=MibTable
cvpnLicClntInfoTable=_CvpnLicClntInfoTable_Object((1,3,6,1,4,1,9,9,816,0,4,1))
if mibBuilder.loadTexts:cvpnLicClntInfoTable.setStatus(_A)
_CvpnLicClntInfoEntry_Object=MibTableRow
cvpnLicClntInfoEntry=_CvpnLicClntInfoEntry_Object((1,3,6,1,4,1,9,9,816,0,4,1,1))
cvpnLicClntInfoEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:cvpnLicClntInfoEntry.setStatus(_A)
_CvpnLicClntVPNLicType_Type=VPNLicType
_CvpnLicClntVPNLicType_Object=MibTableColumn
cvpnLicClntVPNLicType=_CvpnLicClntVPNLicType_Object((1,3,6,1,4,1,9,9,816,0,4,1,1,1),_CvpnLicClntVPNLicType_Type())
cvpnLicClntVPNLicType.setMaxAccess(_H)
if mibBuilder.loadTexts:cvpnLicClntVPNLicType.setStatus(_A)
class _CvpnLicClntInfoDeviceID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CvpnLicClntInfoDeviceID_Type.__name__=_F
_CvpnLicClntInfoDeviceID_Object=MibTableColumn
cvpnLicClntInfoDeviceID=_CvpnLicClntInfoDeviceID_Object((1,3,6,1,4,1,9,9,816,0,4,1,1,2),_CvpnLicClntInfoDeviceID_Type())
cvpnLicClntInfoDeviceID.setMaxAccess(_H)
if mibBuilder.loadTexts:cvpnLicClntInfoDeviceID.setStatus(_A)
class _CvpnLicClntInfoHostName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CvpnLicClntInfoHostName_Type.__name__=_F
_CvpnLicClntInfoHostName_Object=MibTableColumn
cvpnLicClntInfoHostName=_CvpnLicClntInfoHostName_Object((1,3,6,1,4,1,9,9,816,0,4,1,1,3),_CvpnLicClntInfoHostName_Type())
cvpnLicClntInfoHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicClntInfoHostName.setStatus(_A)
_CvpnLicClntInfoPlatLmt_Type=Unsigned32
_CvpnLicClntInfoPlatLmt_Object=MibTableColumn
cvpnLicClntInfoPlatLmt=_CvpnLicClntInfoPlatLmt_Object((1,3,6,1,4,1,9,9,816,0,4,1,1,4),_CvpnLicClntInfoPlatLmt_Type())
cvpnLicClntInfoPlatLmt.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicClntInfoPlatLmt.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicClntInfoPlatLmt.setUnits(_E)
_CvpnLicClntInfoCurUsage_Type=Unsigned32
_CvpnLicClntInfoCurUsage_Object=MibTableColumn
cvpnLicClntInfoCurUsage=_CvpnLicClntInfoCurUsage_Object((1,3,6,1,4,1,9,9,816,0,4,1,1,5),_CvpnLicClntInfoCurUsage_Type())
cvpnLicClntInfoCurUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicClntInfoCurUsage.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicClntInfoCurUsage.setUnits(_E)
_CvpnLicClntInfoHigh_Type=Unsigned32
_CvpnLicClntInfoHigh_Object=MibTableColumn
cvpnLicClntInfoHigh=_CvpnLicClntInfoHigh_Object((1,3,6,1,4,1,9,9,816,0,4,1,1,6),_CvpnLicClntInfoHigh_Type())
cvpnLicClntInfoHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicClntInfoHigh.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicClntInfoHigh.setUnits(_E)
_CvpnLicClntInfoRegReqTx_Type=Counter32
_CvpnLicClntInfoRegReqTx_Object=MibTableColumn
cvpnLicClntInfoRegReqTx=_CvpnLicClntInfoRegReqTx_Object((1,3,6,1,4,1,9,9,816,0,4,1,1,7),_CvpnLicClntInfoRegReqTx_Type())
cvpnLicClntInfoRegReqTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicClntInfoRegReqTx.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicClntInfoRegReqTx.setUnits(_D)
_CvpnLicClntInfoRegReqRx_Type=Counter32
_CvpnLicClntInfoRegReqRx_Object=MibTableColumn
cvpnLicClntInfoRegReqRx=_CvpnLicClntInfoRegReqRx_Object((1,3,6,1,4,1,9,9,816,0,4,1,1,8),_CvpnLicClntInfoRegReqRx_Type())
cvpnLicClntInfoRegReqRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicClntInfoRegReqRx.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicClntInfoRegReqRx.setUnits(_D)
_CvpnLicClntInfoRegReqError_Type=Counter32
_CvpnLicClntInfoRegReqError_Object=MibTableColumn
cvpnLicClntInfoRegReqError=_CvpnLicClntInfoRegReqError_Object((1,3,6,1,4,1,9,9,816,0,4,1,1,9),_CvpnLicClntInfoRegReqError_Type())
cvpnLicClntInfoRegReqError.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicClntInfoRegReqError.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicClntInfoRegReqError.setUnits(_D)
_CvpnLicClntInfoGetReqTx_Type=Counter32
_CvpnLicClntInfoGetReqTx_Object=MibTableColumn
cvpnLicClntInfoGetReqTx=_CvpnLicClntInfoGetReqTx_Object((1,3,6,1,4,1,9,9,816,0,4,1,1,10),_CvpnLicClntInfoGetReqTx_Type())
cvpnLicClntInfoGetReqTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicClntInfoGetReqTx.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicClntInfoGetReqTx.setUnits(_D)
_CvpnLicClntInfoGetReqRx_Type=Counter32
_CvpnLicClntInfoGetReqRx_Object=MibTableColumn
cvpnLicClntInfoGetReqRx=_CvpnLicClntInfoGetReqRx_Object((1,3,6,1,4,1,9,9,816,0,4,1,1,11),_CvpnLicClntInfoGetReqRx_Type())
cvpnLicClntInfoGetReqRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicClntInfoGetReqRx.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicClntInfoGetReqRx.setUnits(_D)
_CvpnLicClntInfoGetReqError_Type=Counter32
_CvpnLicClntInfoGetReqError_Object=MibTableColumn
cvpnLicClntInfoGetReqError=_CvpnLicClntInfoGetReqError_Object((1,3,6,1,4,1,9,9,816,0,4,1,1,12),_CvpnLicClntInfoGetReqError_Type())
cvpnLicClntInfoGetReqError.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicClntInfoGetReqError.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicClntInfoGetReqError.setUnits(_D)
_CvpnLicClntInfoRelReqTx_Type=Counter32
_CvpnLicClntInfoRelReqTx_Object=MibTableColumn
cvpnLicClntInfoRelReqTx=_CvpnLicClntInfoRelReqTx_Object((1,3,6,1,4,1,9,9,816,0,4,1,1,13),_CvpnLicClntInfoRelReqTx_Type())
cvpnLicClntInfoRelReqTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicClntInfoRelReqTx.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicClntInfoRelReqTx.setUnits(_D)
_CvpnLicClntInfoRelReqRx_Type=Counter32
_CvpnLicClntInfoRelReqRx_Object=MibTableColumn
cvpnLicClntInfoRelReqRx=_CvpnLicClntInfoRelReqRx_Object((1,3,6,1,4,1,9,9,816,0,4,1,1,14),_CvpnLicClntInfoRelReqRx_Type())
cvpnLicClntInfoRelReqRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicClntInfoRelReqRx.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicClntInfoRelReqRx.setUnits(_D)
_CvpnLicClntInfoRelReqError_Type=Counter32
_CvpnLicClntInfoRelReqError_Object=MibTableColumn
cvpnLicClntInfoRelReqError=_CvpnLicClntInfoRelReqError_Object((1,3,6,1,4,1,9,9,816,0,4,1,1,15),_CvpnLicClntInfoRelReqError_Type())
cvpnLicClntInfoRelReqError.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicClntInfoRelReqError.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicClntInfoRelReqError.setUnits(_D)
_CvpnLicClntInfoTransferReqTx_Type=Counter32
_CvpnLicClntInfoTransferReqTx_Object=MibTableColumn
cvpnLicClntInfoTransferReqTx=_CvpnLicClntInfoTransferReqTx_Object((1,3,6,1,4,1,9,9,816,0,4,1,1,16),_CvpnLicClntInfoTransferReqTx_Type())
cvpnLicClntInfoTransferReqTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicClntInfoTransferReqTx.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicClntInfoTransferReqTx.setUnits(_D)
_CvpnLicClntInfoTransferReqRx_Type=Counter32
_CvpnLicClntInfoTransferReqRx_Object=MibTableColumn
cvpnLicClntInfoTransferReqRx=_CvpnLicClntInfoTransferReqRx_Object((1,3,6,1,4,1,9,9,816,0,4,1,1,17),_CvpnLicClntInfoTransferReqRx_Type())
cvpnLicClntInfoTransferReqRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicClntInfoTransferReqRx.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicClntInfoTransferReqRx.setUnits(_D)
_CvpnLicClntInfoTransferReqError_Type=Counter32
_CvpnLicClntInfoTransferReqError_Object=MibTableColumn
cvpnLicClntInfoTransferReqError=_CvpnLicClntInfoTransferReqError_Object((1,3,6,1,4,1,9,9,816,0,4,1,1,18),_CvpnLicClntInfoTransferReqError_Type())
cvpnLicClntInfoTransferReqError.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpnLicClntInfoTransferReqError.setStatus(_A)
if mibBuilder.loadTexts:cvpnLicClntInfoTransferReqError.setUnits(_D)
_CiscoVpnLicUsageMonitorMIBConform_ObjectIdentity=ObjectIdentity
ciscoVpnLicUsageMonitorMIBConform=_CiscoVpnLicUsageMonitorMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,816,1))
_CiscoVpnLicUsageMonitorMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVpnLicUsageMonitorMIBCompliances=_CiscoVpnLicUsageMonitorMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,816,1,1))
_CiscoVpnLicUsageMonitorMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVpnLicUsageMonitorMIBGroups=_CiscoVpnLicUsageMonitorMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,816,1,2))
ciscoVPNSharedLicUsageMandatoryGroup=ObjectGroup((1,3,6,1,4,1,9,9,816,1,2,1))
ciscoVPNSharedLicUsageMandatoryGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:ciscoVPNSharedLicUsageMandatoryGroup.setStatus(_A)
ciscoVPNSharedLicOptUsageGroup=ObjectGroup((1,3,6,1,4,1,9,9,816,1,2,2))
ciscoVPNSharedLicOptUsageGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:ciscoVPNSharedLicOptUsageGroup.setStatus(_A)
ciscoVpnLicUsageMonitorMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,816,1,1,1))
ciscoVpnLicUsageMonitorMIBCompliance.setObjects(*((_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:ciscoVpnLicUsageMonitorMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VPNLicType':VPNLicType,'VPNLicDeviceRole':VPNLicDeviceRole,'LicServerStatus':LicServerStatus,'LicServerRegistered':LicServerRegistered,'ciscoVpnLicUsageMonitorMIB':ciscoVpnLicUsageMonitorMIB,'ciscoVpnLicUsageMonitorMIBObjects':ciscoVpnLicUsageMonitorMIBObjects,_M:cvpnLicDeviceRole,'cvpnLicServer':cvpnLicServer,_N:cvpnLicServerAddrType,_O:cvpnLicServerAddr,_P:cvpnLicBkpSerAddrType,_Q:cvpnLicBkpSerAddr,_R:cvpnLicServerVer,_S:cvpnLicServerStatus,'cvpnLicServerTable':cvpnLicServerTable,'cvpnLicServerEntry':cvpnLicServerEntry,_J:cvpnLicServerVPNLicType,_T:cvpnLicServerNumLicCapacity,_U:cvpnLicServerNumLicAvail,_V:cvpnLicServerUtilized,'cvpnLicBkpServer':cvpnLicBkpServer,_a:cvpnLicBkpServerAddrType,_b:cvpnLicBkpServerAddr,_c:cvpnLicBkpServerDevID,_d:cvpnLicBkpServerVer,_e:cvpnLicBkpServerRegd,_f:cvpnLicBkpServerHAPeerDevID,_g:cvpnLicBkpServerHAPeerRegd,_h:cvpnLicBkpServerStatus,_i:cvpnLicServerHelloTx,_j:cvpnLicServerHelloRx,_k:cvpnLicServerHelloError,_l:cvpnLicServerSyncTx,_m:cvpnLicServerSyncRx,_n:cvpnLicServerSyncError,_o:cvpnLicServerUpdateTx,_p:cvpnLicServerUpdateRx,_q:cvpnLicServerUpdateError,'cvpnLicClient':cvpnLicClient,'cvpnLicClntInfoTable':cvpnLicClntInfoTable,'cvpnLicClntInfoEntry':cvpnLicClntInfoEntry,_K:cvpnLicClntVPNLicType,_L:cvpnLicClntInfoDeviceID,_W:cvpnLicClntInfoHostName,_X:cvpnLicClntInfoPlatLmt,_Y:cvpnLicClntInfoCurUsage,_Z:cvpnLicClntInfoHigh,_r:cvpnLicClntInfoRegReqTx,_s:cvpnLicClntInfoRegReqRx,_t:cvpnLicClntInfoRegReqError,_u:cvpnLicClntInfoGetReqTx,_v:cvpnLicClntInfoGetReqRx,_w:cvpnLicClntInfoGetReqError,_x:cvpnLicClntInfoRelReqTx,_y:cvpnLicClntInfoRelReqRx,_z:cvpnLicClntInfoRelReqError,_A0:cvpnLicClntInfoTransferReqTx,_A1:cvpnLicClntInfoTransferReqRx,_A2:cvpnLicClntInfoTransferReqError,'ciscoVpnLicUsageMonitorMIBConform':ciscoVpnLicUsageMonitorMIBConform,'ciscoVpnLicUsageMonitorMIBCompliances':ciscoVpnLicUsageMonitorMIBCompliances,'ciscoVpnLicUsageMonitorMIBCompliance':ciscoVpnLicUsageMonitorMIBCompliance,'ciscoVpnLicUsageMonitorMIBGroups':ciscoVpnLicUsageMonitorMIBGroups,_A3:ciscoVPNSharedLicUsageMandatoryGroup,_A4:ciscoVPNSharedLicOptUsageGroup})