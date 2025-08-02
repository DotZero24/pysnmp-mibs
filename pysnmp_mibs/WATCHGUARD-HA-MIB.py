_V='wgHAPeerIfIndex'
_U='WATCHGUARD-HA-MIB'
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
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
watchguard,=mibBuilder.importSymbols('WATCHGUARD-MIB','watchguard')
wgInfoModule=ModuleIdentity((1,3,6,1,4,1,3097,6))
if mibBuilder.loadTexts:wgInfoModule.setRevisions(('2007-01-25 12:00',))
_WgHAMIB_ObjectIdentity=ObjectIdentity
wgHAMIB=_WgHAMIB_ObjectIdentity((1,3,6,1,4,1,3097,6,6))
if mibBuilder.loadTexts:wgHAMIB.setStatus(_A)
_WgHALocal_ObjectIdentity=ObjectIdentity
wgHALocal=_WgHALocal_ObjectIdentity((1,3,6,1,4,1,3097,6,6,1))
if mibBuilder.loadTexts:wgHALocal.setStatus(_A)
class _WgHAStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('disabled',0),('unknown',1),('as-primary-active',2),('as-secondary-active',3),('aa-primary-ative',4),('aa-secondary-active',5),('aa-primary-takeover',6),('aa-secondary-takeover',7),(_E,8),('admin',9),(_F,10),(_D,11)))
_WgHAStatus_Type.__name__=_C
_WgHAStatus_Object=MibScalar
wgHAStatus=_WgHAStatus_Object((1,3,6,1,4,1,3097,6,6,1,1),_WgHAStatus_Type())
wgHAStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAStatus.setStatus(_A)
class _WgHAPeerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),('active',1),(_E,2),('admin',3),(_F,4)))
_WgHAPeerStatus_Type.__name__=_C
_WgHAPeerStatus_Object=MibScalar
wgHAPeerStatus=_WgHAPeerStatus_Object((1,3,6,1,4,1,3097,6,6,1,2),_WgHAPeerStatus_Type())
wgHAPeerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerStatus.setStatus(_A)
_WgHALastDBSyncTime_Type=DateAndTime
_WgHALastDBSyncTime_Object=MibScalar
wgHALastDBSyncTime=_WgHALastDBSyncTime_Object((1,3,6,1,4,1,3097,6,6,1,3),_WgHALastDBSyncTime_Type())
wgHALastDBSyncTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHALastDBSyncTime.setStatus(_A)
class _WgHAError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_P,9),(_Q,10),(_R,11),(_D,12),(_S,13),(_T,14)))
_WgHAError_Type.__name__=_C
_WgHAError_Object=MibScalar
wgHAError=_WgHAError_Object((1,3,6,1,4,1,3097,6,6,1,4),_WgHAError_Type())
wgHAError.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAError.setStatus(_A)
class _WgHAPeerError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_P,9),(_Q,10),(_R,11),(_D,12),(_S,13),(_T,14)))
_WgHAPeerError_Type.__name__=_C
_WgHAPeerError_Object=MibScalar
wgHAPeerError=_WgHAPeerError_Object((1,3,6,1,4,1,3097,6,6,1,5),_WgHAPeerError_Type())
wgHAPeerError.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerError.setStatus(_A)
_WgHAPeer_ObjectIdentity=ObjectIdentity
wgHAPeer=_WgHAPeer_ObjectIdentity((1,3,6,1,4,1,3097,6,6,2))
if mibBuilder.loadTexts:wgHAPeer.setStatus(_A)
_WgHAPeerSerialNumber_Type=OctetString
_WgHAPeerSerialNumber_Object=MibScalar
wgHAPeerSerialNumber=_WgHAPeerSerialNumber_Object((1,3,6,1,4,1,3097,6,6,2,1),_WgHAPeerSerialNumber_Type())
wgHAPeerSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerSerialNumber.setStatus(_A)
_WgHAPeerLastDBSyncTime_Type=DateAndTime
_WgHAPeerLastDBSyncTime_Object=MibScalar
wgHAPeerLastDBSyncTime=_WgHAPeerLastDBSyncTime_Object((1,3,6,1,4,1,3097,6,6,2,2),_WgHAPeerLastDBSyncTime_Type())
wgHAPeerLastDBSyncTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerLastDBSyncTime.setStatus(_A)
_WgHAPeerDevice_ObjectIdentity=ObjectIdentity
wgHAPeerDevice=_WgHAPeerDevice_ObjectIdentity((1,3,6,1,4,1,3097,6,6,2,3))
if mibBuilder.loadTexts:wgHAPeerDevice.setStatus(_A)
_WgHAPeerIfNumber_Type=Unsigned32
_WgHAPeerIfNumber_Object=MibScalar
wgHAPeerIfNumber=_WgHAPeerIfNumber_Object((1,3,6,1,4,1,3097,6,6,2,3,1),_WgHAPeerIfNumber_Type())
wgHAPeerIfNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerIfNumber.setStatus(_A)
_WgHAPeerIfTable_Object=MibTable
wgHAPeerIfTable=_WgHAPeerIfTable_Object((1,3,6,1,4,1,3097,6,6,2,3,2))
if mibBuilder.loadTexts:wgHAPeerIfTable.setStatus(_A)
_WgHAPeerIfEntry_Object=MibTableRow
wgHAPeerIfEntry=_WgHAPeerIfEntry_Object((1,3,6,1,4,1,3097,6,6,2,3,2,1))
wgHAPeerIfEntry.setIndexNames((0,_U,_V))
if mibBuilder.loadTexts:wgHAPeerIfEntry.setStatus(_A)
_WgHAPeerIfIndex_Type=Unsigned32
_WgHAPeerIfIndex_Object=MibTableColumn
wgHAPeerIfIndex=_WgHAPeerIfIndex_Object((1,3,6,1,4,1,3097,6,6,2,3,2,1,1),_WgHAPeerIfIndex_Type())
wgHAPeerIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerIfIndex.setStatus(_A)
_WgHAPeerIfIpAddr_Type=IpAddress
_WgHAPeerIfIpAddr_Object=MibTableColumn
wgHAPeerIfIpAddr=_WgHAPeerIfIpAddr_Object((1,3,6,1,4,1,3097,6,6,2,3,2,1,4),_WgHAPeerIfIpAddr_Type())
wgHAPeerIfIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerIfIpAddr.setStatus(_A)
class _WgHAPeerIfLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('down',0),('up',1),('other',2)))
_WgHAPeerIfLinkStatus_Type.__name__=_C
_WgHAPeerIfLinkStatus_Object=MibTableColumn
wgHAPeerIfLinkStatus=_WgHAPeerIfLinkStatus_Object((1,3,6,1,4,1,3097,6,6,2,3,2,1,9),_WgHAPeerIfLinkStatus_Type())
wgHAPeerIfLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerIfLinkStatus.setStatus(_A)
_WgHAPeerCounters_ObjectIdentity=ObjectIdentity
wgHAPeerCounters=_WgHAPeerCounters_ObjectIdentity((1,3,6,1,4,1,3097,6,6,2,4))
if mibBuilder.loadTexts:wgHAPeerCounters.setStatus(_A)
_WgHAPeerSystemCpuUtil_Type=Gauge32
_WgHAPeerSystemCpuUtil_Object=MibScalar
wgHAPeerSystemCpuUtil=_WgHAPeerSystemCpuUtil_Object((1,3,6,1,4,1,3097,6,6,2,4,1),_WgHAPeerSystemCpuUtil_Type())
wgHAPeerSystemCpuUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerSystemCpuUtil.setStatus(_A)
_WgHAPeerSystemTotalSendBytes_Type=Counter64
_WgHAPeerSystemTotalSendBytes_Object=MibScalar
wgHAPeerSystemTotalSendBytes=_WgHAPeerSystemTotalSendBytes_Object((1,3,6,1,4,1,3097,6,6,2,4,2),_WgHAPeerSystemTotalSendBytes_Type())
wgHAPeerSystemTotalSendBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerSystemTotalSendBytes.setStatus(_A)
_WgHAPeerSystemTotalRecvBytes_Type=Counter64
_WgHAPeerSystemTotalRecvBytes_Object=MibScalar
wgHAPeerSystemTotalRecvBytes=_WgHAPeerSystemTotalRecvBytes_Object((1,3,6,1,4,1,3097,6,6,2,4,3),_WgHAPeerSystemTotalRecvBytes_Type())
wgHAPeerSystemTotalRecvBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerSystemTotalRecvBytes.setStatus(_A)
_WgHAPeerSystemTotalSendPackets_Type=Counter64
_WgHAPeerSystemTotalSendPackets_Object=MibScalar
wgHAPeerSystemTotalSendPackets=_WgHAPeerSystemTotalSendPackets_Object((1,3,6,1,4,1,3097,6,6,2,4,4),_WgHAPeerSystemTotalSendPackets_Type())
wgHAPeerSystemTotalSendPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerSystemTotalSendPackets.setStatus(_A)
_WgHAPeerSystemTotalRecvPackets_Type=Counter64
_WgHAPeerSystemTotalRecvPackets_Object=MibScalar
wgHAPeerSystemTotalRecvPackets=_WgHAPeerSystemTotalRecvPackets_Object((1,3,6,1,4,1,3097,6,6,2,4,5),_WgHAPeerSystemTotalRecvPackets_Type())
wgHAPeerSystemTotalRecvPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerSystemTotalRecvPackets.setStatus(_A)
_WgHAPeerSystemStreamReqTotal_Type=Counter64
_WgHAPeerSystemStreamReqTotal_Object=MibScalar
wgHAPeerSystemStreamReqTotal=_WgHAPeerSystemStreamReqTotal_Object((1,3,6,1,4,1,3097,6,6,2,4,6),_WgHAPeerSystemStreamReqTotal_Type())
wgHAPeerSystemStreamReqTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerSystemStreamReqTotal.setStatus(_A)
_WgHAPeerSystemStreamReqDrop_Type=Counter64
_WgHAPeerSystemStreamReqDrop_Object=MibScalar
wgHAPeerSystemStreamReqDrop=_WgHAPeerSystemStreamReqDrop_Object((1,3,6,1,4,1,3097,6,6,2,4,7),_WgHAPeerSystemStreamReqDrop_Type())
wgHAPeerSystemStreamReqDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerSystemStreamReqDrop.setStatus(_A)
_WgHAPeerSystemCurrIpsecTunnels_Type=Counter64
_WgHAPeerSystemCurrIpsecTunnels_Object=MibScalar
wgHAPeerSystemCurrIpsecTunnels=_WgHAPeerSystemCurrIpsecTunnels_Object((1,3,6,1,4,1,3097,6,6,2,4,8),_WgHAPeerSystemCurrIpsecTunnels_Type())
wgHAPeerSystemCurrIpsecTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerSystemCurrIpsecTunnels.setStatus(_A)
_WgHAPeerSystemCpuUtil1_Type=Gauge32
_WgHAPeerSystemCpuUtil1_Object=MibScalar
wgHAPeerSystemCpuUtil1=_WgHAPeerSystemCpuUtil1_Object((1,3,6,1,4,1,3097,6,6,2,4,9),_WgHAPeerSystemCpuUtil1_Type())
wgHAPeerSystemCpuUtil1.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerSystemCpuUtil1.setStatus(_A)
_WgHAPeerSystemCpuUtil5_Type=Gauge32
_WgHAPeerSystemCpuUtil5_Object=MibScalar
wgHAPeerSystemCpuUtil5=_WgHAPeerSystemCpuUtil5_Object((1,3,6,1,4,1,3097,6,6,2,4,10),_WgHAPeerSystemCpuUtil5_Type())
wgHAPeerSystemCpuUtil5.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerSystemCpuUtil5.setStatus(_A)
_WgHAPeerSystemCpuUtil15_Type=Gauge32
_WgHAPeerSystemCpuUtil15_Object=MibScalar
wgHAPeerSystemCpuUtil15=_WgHAPeerSystemCpuUtil15_Object((1,3,6,1,4,1,3097,6,6,2,4,11),_WgHAPeerSystemCpuUtil15_Type())
wgHAPeerSystemCpuUtil15.setMaxAccess(_B)
if mibBuilder.loadTexts:wgHAPeerSystemCpuUtil15.setStatus(_A)
mibBuilder.exportSymbols(_U,**{'wgInfoModule':wgInfoModule,'wgHAMIB':wgHAMIB,'wgHALocal':wgHALocal,'wgHAStatus':wgHAStatus,'wgHAPeerStatus':wgHAPeerStatus,'wgHALastDBSyncTime':wgHALastDBSyncTime,'wgHAError':wgHAError,'wgHAPeerError':wgHAPeerError,'wgHAPeer':wgHAPeer,'wgHAPeerSerialNumber':wgHAPeerSerialNumber,'wgHAPeerLastDBSyncTime':wgHAPeerLastDBSyncTime,'wgHAPeerDevice':wgHAPeerDevice,'wgHAPeerIfNumber':wgHAPeerIfNumber,'wgHAPeerIfTable':wgHAPeerIfTable,'wgHAPeerIfEntry':wgHAPeerIfEntry,_V:wgHAPeerIfIndex,'wgHAPeerIfIpAddr':wgHAPeerIfIpAddr,'wgHAPeerIfLinkStatus':wgHAPeerIfLinkStatus,'wgHAPeerCounters':wgHAPeerCounters,'wgHAPeerSystemCpuUtil':wgHAPeerSystemCpuUtil,'wgHAPeerSystemTotalSendBytes':wgHAPeerSystemTotalSendBytes,'wgHAPeerSystemTotalRecvBytes':wgHAPeerSystemTotalRecvBytes,'wgHAPeerSystemTotalSendPackets':wgHAPeerSystemTotalSendPackets,'wgHAPeerSystemTotalRecvPackets':wgHAPeerSystemTotalRecvPackets,'wgHAPeerSystemStreamReqTotal':wgHAPeerSystemStreamReqTotal,'wgHAPeerSystemStreamReqDrop':wgHAPeerSystemStreamReqDrop,'wgHAPeerSystemCurrIpsecTunnels':wgHAPeerSystemCurrIpsecTunnels,'wgHAPeerSystemCpuUtil1':wgHAPeerSystemCpuUtil1,'wgHAPeerSystemCpuUtil5':wgHAPeerSystemCpuUtil5,'wgHAPeerSystemCpuUtil15':wgHAPeerSystemCpuUtil15})