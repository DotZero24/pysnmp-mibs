_V='rsHAPeerIfIndex'
_U='RAPID-HA-MIB'
_T='config-sync-failed'
_S='hotsync-failed'
_R='detect-ha-error'
_Q='admin-command-failed'
_P='mia-not-responding'
_O='lost-mia-heartbeat'
_N='link-down'
_M='invalid-ha-role'
_L='forced-fail'
_K='mismatched-hardware'
_J='mismatched-database'
_I='mismatched-software'
_H='mismatched-ha-id'
_G='no-error'
_F='failed'
_E='standby'
_D='unavailable'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rapidstream,=mibBuilder.importSymbols('RAPID-MIB','rapidstream')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
rsInfoModule=ModuleIdentity((1,3,6,1,4,1,4355,6))
if mibBuilder.loadTexts:rsInfoModule.setRevisions(('2002-11-01 12:00',))
_RsHAMIB_ObjectIdentity=ObjectIdentity
rsHAMIB=_RsHAMIB_ObjectIdentity((1,3,6,1,4,1,4355,6,6))
if mibBuilder.loadTexts:rsHAMIB.setStatus(_A)
_RsHALocal_ObjectIdentity=ObjectIdentity
rsHALocal=_RsHALocal_ObjectIdentity((1,3,6,1,4,1,4355,6,6,1))
if mibBuilder.loadTexts:rsHALocal.setStatus(_A)
class _RsHAStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('disabled',0),('unknown',1),('as-primary-active',2),('as-secondary-active',3),('aa-primary-ative',4),('aa-secondary-active',5),('aa-primary-takeover',6),('aa-secondary-takeover',7),(_E,8),('admin',9),(_F,10),(_D,11)))
_RsHAStatus_Type.__name__=_C
_RsHAStatus_Object=MibScalar
rsHAStatus=_RsHAStatus_Object((1,3,6,1,4,1,4355,6,6,1,1),_RsHAStatus_Type())
rsHAStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAStatus.setStatus(_A)
class _RsHAPeerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),('active',1),(_E,2),('admin',3),(_F,4)))
_RsHAPeerStatus_Type.__name__=_C
_RsHAPeerStatus_Object=MibScalar
rsHAPeerStatus=_RsHAPeerStatus_Object((1,3,6,1,4,1,4355,6,6,1,2),_RsHAPeerStatus_Type())
rsHAPeerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerStatus.setStatus(_A)
_RsHALastDBSyncTime_Type=DateAndTime
_RsHALastDBSyncTime_Object=MibScalar
rsHALastDBSyncTime=_RsHALastDBSyncTime_Object((1,3,6,1,4,1,4355,6,6,1,3),_RsHALastDBSyncTime_Type())
rsHALastDBSyncTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHALastDBSyncTime.setStatus(_A)
class _RsHAError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_P,9),(_Q,10),(_R,11),(_D,12),(_S,13),(_T,14)))
_RsHAError_Type.__name__=_C
_RsHAError_Object=MibScalar
rsHAError=_RsHAError_Object((1,3,6,1,4,1,4355,6,6,1,4),_RsHAError_Type())
rsHAError.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAError.setStatus(_A)
class _RsHAPeerError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_P,9),(_Q,10),(_R,11),(_D,12),(_S,13),(_T,14)))
_RsHAPeerError_Type.__name__=_C
_RsHAPeerError_Object=MibScalar
rsHAPeerError=_RsHAPeerError_Object((1,3,6,1,4,1,4355,6,6,1,5),_RsHAPeerError_Type())
rsHAPeerError.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerError.setStatus(_A)
_RsHAPeer_ObjectIdentity=ObjectIdentity
rsHAPeer=_RsHAPeer_ObjectIdentity((1,3,6,1,4,1,4355,6,6,2))
if mibBuilder.loadTexts:rsHAPeer.setStatus(_A)
_RsHAPeerSerialNumber_Type=OctetString
_RsHAPeerSerialNumber_Object=MibScalar
rsHAPeerSerialNumber=_RsHAPeerSerialNumber_Object((1,3,6,1,4,1,4355,6,6,2,1),_RsHAPeerSerialNumber_Type())
rsHAPeerSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerSerialNumber.setStatus(_A)
_RsHAPeerLastDBSyncTime_Type=DateAndTime
_RsHAPeerLastDBSyncTime_Object=MibScalar
rsHAPeerLastDBSyncTime=_RsHAPeerLastDBSyncTime_Object((1,3,6,1,4,1,4355,6,6,2,2),_RsHAPeerLastDBSyncTime_Type())
rsHAPeerLastDBSyncTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerLastDBSyncTime.setStatus(_A)
_RsHAPeerDevice_ObjectIdentity=ObjectIdentity
rsHAPeerDevice=_RsHAPeerDevice_ObjectIdentity((1,3,6,1,4,1,4355,6,6,2,3))
if mibBuilder.loadTexts:rsHAPeerDevice.setStatus(_A)
_RsHAPeerIfNumber_Type=Unsigned32
_RsHAPeerIfNumber_Object=MibScalar
rsHAPeerIfNumber=_RsHAPeerIfNumber_Object((1,3,6,1,4,1,4355,6,6,2,3,1),_RsHAPeerIfNumber_Type())
rsHAPeerIfNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerIfNumber.setStatus(_A)
_RsHAPeerIfTable_Object=MibTable
rsHAPeerIfTable=_RsHAPeerIfTable_Object((1,3,6,1,4,1,4355,6,6,2,3,2))
if mibBuilder.loadTexts:rsHAPeerIfTable.setStatus(_A)
_RsHAPeerIfEntry_Object=MibTableRow
rsHAPeerIfEntry=_RsHAPeerIfEntry_Object((1,3,6,1,4,1,4355,6,6,2,3,2,1))
rsHAPeerIfEntry.setIndexNames((0,_U,_V))
if mibBuilder.loadTexts:rsHAPeerIfEntry.setStatus(_A)
_RsHAPeerIfIndex_Type=Unsigned32
_RsHAPeerIfIndex_Object=MibTableColumn
rsHAPeerIfIndex=_RsHAPeerIfIndex_Object((1,3,6,1,4,1,4355,6,6,2,3,2,1,1),_RsHAPeerIfIndex_Type())
rsHAPeerIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerIfIndex.setStatus(_A)
_RsHAPeerIfIpAddr_Type=IpAddress
_RsHAPeerIfIpAddr_Object=MibTableColumn
rsHAPeerIfIpAddr=_RsHAPeerIfIpAddr_Object((1,3,6,1,4,1,4355,6,6,2,3,2,1,4),_RsHAPeerIfIpAddr_Type())
rsHAPeerIfIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerIfIpAddr.setStatus(_A)
class _RsHAPeerIfLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('down',0),('up',1),('other',2)))
_RsHAPeerIfLinkStatus_Type.__name__=_C
_RsHAPeerIfLinkStatus_Object=MibTableColumn
rsHAPeerIfLinkStatus=_RsHAPeerIfLinkStatus_Object((1,3,6,1,4,1,4355,6,6,2,3,2,1,9),_RsHAPeerIfLinkStatus_Type())
rsHAPeerIfLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerIfLinkStatus.setStatus(_A)
_RsHAPeerCounters_ObjectIdentity=ObjectIdentity
rsHAPeerCounters=_RsHAPeerCounters_ObjectIdentity((1,3,6,1,4,1,4355,6,6,2,4))
if mibBuilder.loadTexts:rsHAPeerCounters.setStatus(_A)
_RsHAPeerSystemCpuUtil_Type=Gauge32
_RsHAPeerSystemCpuUtil_Object=MibScalar
rsHAPeerSystemCpuUtil=_RsHAPeerSystemCpuUtil_Object((1,3,6,1,4,1,4355,6,6,2,4,1),_RsHAPeerSystemCpuUtil_Type())
rsHAPeerSystemCpuUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerSystemCpuUtil.setStatus(_A)
_RsHAPeerSystemTotalSendBytes_Type=Counter64
_RsHAPeerSystemTotalSendBytes_Object=MibScalar
rsHAPeerSystemTotalSendBytes=_RsHAPeerSystemTotalSendBytes_Object((1,3,6,1,4,1,4355,6,6,2,4,2),_RsHAPeerSystemTotalSendBytes_Type())
rsHAPeerSystemTotalSendBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerSystemTotalSendBytes.setStatus(_A)
_RsHAPeerSystemTotalRecvBytes_Type=Counter64
_RsHAPeerSystemTotalRecvBytes_Object=MibScalar
rsHAPeerSystemTotalRecvBytes=_RsHAPeerSystemTotalRecvBytes_Object((1,3,6,1,4,1,4355,6,6,2,4,3),_RsHAPeerSystemTotalRecvBytes_Type())
rsHAPeerSystemTotalRecvBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerSystemTotalRecvBytes.setStatus(_A)
_RsHAPeerSystemTotalSendPackets_Type=Counter64
_RsHAPeerSystemTotalSendPackets_Object=MibScalar
rsHAPeerSystemTotalSendPackets=_RsHAPeerSystemTotalSendPackets_Object((1,3,6,1,4,1,4355,6,6,2,4,4),_RsHAPeerSystemTotalSendPackets_Type())
rsHAPeerSystemTotalSendPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerSystemTotalSendPackets.setStatus(_A)
_RsHAPeerSystemTotalRecvPackets_Type=Counter64
_RsHAPeerSystemTotalRecvPackets_Object=MibScalar
rsHAPeerSystemTotalRecvPackets=_RsHAPeerSystemTotalRecvPackets_Object((1,3,6,1,4,1,4355,6,6,2,4,5),_RsHAPeerSystemTotalRecvPackets_Type())
rsHAPeerSystemTotalRecvPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerSystemTotalRecvPackets.setStatus(_A)
_RsHAPeerSystemStreamReqTotal_Type=Counter64
_RsHAPeerSystemStreamReqTotal_Object=MibScalar
rsHAPeerSystemStreamReqTotal=_RsHAPeerSystemStreamReqTotal_Object((1,3,6,1,4,1,4355,6,6,2,4,6),_RsHAPeerSystemStreamReqTotal_Type())
rsHAPeerSystemStreamReqTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerSystemStreamReqTotal.setStatus(_A)
_RsHAPeerSystemStreamReqDrop_Type=Counter64
_RsHAPeerSystemStreamReqDrop_Object=MibScalar
rsHAPeerSystemStreamReqDrop=_RsHAPeerSystemStreamReqDrop_Object((1,3,6,1,4,1,4355,6,6,2,4,7),_RsHAPeerSystemStreamReqDrop_Type())
rsHAPeerSystemStreamReqDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerSystemStreamReqDrop.setStatus(_A)
_RsHAPeerSystemCurrIpsecTunnels_Type=Counter64
_RsHAPeerSystemCurrIpsecTunnels_Object=MibScalar
rsHAPeerSystemCurrIpsecTunnels=_RsHAPeerSystemCurrIpsecTunnels_Object((1,3,6,1,4,1,4355,6,6,2,4,8),_RsHAPeerSystemCurrIpsecTunnels_Type())
rsHAPeerSystemCurrIpsecTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerSystemCurrIpsecTunnels.setStatus(_A)
_RsHAPeerSystemCpuUtil1_Type=Gauge32
_RsHAPeerSystemCpuUtil1_Object=MibScalar
rsHAPeerSystemCpuUtil1=_RsHAPeerSystemCpuUtil1_Object((1,3,6,1,4,1,4355,6,6,2,4,9),_RsHAPeerSystemCpuUtil1_Type())
rsHAPeerSystemCpuUtil1.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerSystemCpuUtil1.setStatus(_A)
_RsHAPeerSystemCpuUtil5_Type=Gauge32
_RsHAPeerSystemCpuUtil5_Object=MibScalar
rsHAPeerSystemCpuUtil5=_RsHAPeerSystemCpuUtil5_Object((1,3,6,1,4,1,4355,6,6,2,4,10),_RsHAPeerSystemCpuUtil5_Type())
rsHAPeerSystemCpuUtil5.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerSystemCpuUtil5.setStatus(_A)
_RsHAPeerSystemCpuUtil15_Type=Gauge32
_RsHAPeerSystemCpuUtil15_Object=MibScalar
rsHAPeerSystemCpuUtil15=_RsHAPeerSystemCpuUtil15_Object((1,3,6,1,4,1,4355,6,6,2,4,11),_RsHAPeerSystemCpuUtil15_Type())
rsHAPeerSystemCpuUtil15.setMaxAccess(_B)
if mibBuilder.loadTexts:rsHAPeerSystemCpuUtil15.setStatus(_A)
mibBuilder.exportSymbols(_U,**{'rsInfoModule':rsInfoModule,'rsHAMIB':rsHAMIB,'rsHALocal':rsHALocal,'rsHAStatus':rsHAStatus,'rsHAPeerStatus':rsHAPeerStatus,'rsHALastDBSyncTime':rsHALastDBSyncTime,'rsHAError':rsHAError,'rsHAPeerError':rsHAPeerError,'rsHAPeer':rsHAPeer,'rsHAPeerSerialNumber':rsHAPeerSerialNumber,'rsHAPeerLastDBSyncTime':rsHAPeerLastDBSyncTime,'rsHAPeerDevice':rsHAPeerDevice,'rsHAPeerIfNumber':rsHAPeerIfNumber,'rsHAPeerIfTable':rsHAPeerIfTable,'rsHAPeerIfEntry':rsHAPeerIfEntry,_V:rsHAPeerIfIndex,'rsHAPeerIfIpAddr':rsHAPeerIfIpAddr,'rsHAPeerIfLinkStatus':rsHAPeerIfLinkStatus,'rsHAPeerCounters':rsHAPeerCounters,'rsHAPeerSystemCpuUtil':rsHAPeerSystemCpuUtil,'rsHAPeerSystemTotalSendBytes':rsHAPeerSystemTotalSendBytes,'rsHAPeerSystemTotalRecvBytes':rsHAPeerSystemTotalRecvBytes,'rsHAPeerSystemTotalSendPackets':rsHAPeerSystemTotalSendPackets,'rsHAPeerSystemTotalRecvPackets':rsHAPeerSystemTotalRecvPackets,'rsHAPeerSystemStreamReqTotal':rsHAPeerSystemStreamReqTotal,'rsHAPeerSystemStreamReqDrop':rsHAPeerSystemStreamReqDrop,'rsHAPeerSystemCurrIpsecTunnels':rsHAPeerSystemCurrIpsecTunnels,'rsHAPeerSystemCpuUtil1':rsHAPeerSystemCpuUtil1,'rsHAPeerSystemCpuUtil5':rsHAPeerSystemCpuUtil5,'rsHAPeerSystemCpuUtil15':rsHAPeerSystemCpuUtil15})