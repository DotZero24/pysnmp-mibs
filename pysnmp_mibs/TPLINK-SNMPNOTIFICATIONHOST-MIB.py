_G='tpSnmpNotificationHostIndex'
_F='TPLINK-SNMPNOTIFICATIONHOST-MIB'
_E='TPRowStatus'
_D='OctetString'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkSnmpMIBObjects,=mibBuilder.importSymbols('TPLINK-SNMP-MIB','tplinkSnmpMIBObjects')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB',_E)
_TpSnmpNotificationHost_ObjectIdentity=ObjectIdentity
tpSnmpNotificationHost=_TpSnmpNotificationHost_ObjectIdentity((1,3,6,1,4,1,11863,6,32,1,1))
_TpSnmpNotificationHostTable_Object=MibTable
tpSnmpNotificationHostTable=_TpSnmpNotificationHostTable_Object((1,3,6,1,4,1,11863,6,32,1,1,1))
if mibBuilder.loadTexts:tpSnmpNotificationHostTable.setStatus(_A)
_TpSnmpNotificationHostEntry_Object=MibTableRow
tpSnmpNotificationHostEntry=_TpSnmpNotificationHostEntry_Object((1,3,6,1,4,1,11863,6,32,1,1,1,1))
tpSnmpNotificationHostEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:tpSnmpNotificationHostEntry.setStatus(_A)
class _TpSnmpNotificationHostIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_TpSnmpNotificationHostIndex_Type.__name__=_C
_TpSnmpNotificationHostIndex_Object=MibTableColumn
tpSnmpNotificationHostIndex=_TpSnmpNotificationHostIndex_Object((1,3,6,1,4,1,11863,6,32,1,1,1,1,1),_TpSnmpNotificationHostIndex_Type())
tpSnmpNotificationHostIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tpSnmpNotificationHostIndex.setStatus(_A)
_TpSnmpNotificationHostIpMode_Type=InetAddressType
_TpSnmpNotificationHostIpMode_Object=MibTableColumn
tpSnmpNotificationHostIpMode=_TpSnmpNotificationHostIpMode_Object((1,3,6,1,4,1,11863,6,32,1,1,1,1,2),_TpSnmpNotificationHostIpMode_Type())
tpSnmpNotificationHostIpMode.setMaxAccess('read-only')
if mibBuilder.loadTexts:tpSnmpNotificationHostIpMode.setStatus(_A)
_TpSnmpNotificationHostIpAddr_Type=InetAddress
_TpSnmpNotificationHostIpAddr_Object=MibTableColumn
tpSnmpNotificationHostIpAddr=_TpSnmpNotificationHostIpAddr_Object((1,3,6,1,4,1,11863,6,32,1,1,1,1,3),_TpSnmpNotificationHostIpAddr_Type())
tpSnmpNotificationHostIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpNotificationHostIpAddr.setStatus(_A)
class _TpSnmpNotificationHostUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TpSnmpNotificationHostUserName_Type.__name__=_D
_TpSnmpNotificationHostUserName_Object=MibTableColumn
tpSnmpNotificationHostUserName=_TpSnmpNotificationHostUserName_Object((1,3,6,1,4,1,11863,6,32,1,1,1,1,4),_TpSnmpNotificationHostUserName_Type())
tpSnmpNotificationHostUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpNotificationHostUserName.setStatus(_A)
class _TpSnmpNotificationHostUDPPort_Type(Integer32):defaultValue=162
_TpSnmpNotificationHostUDPPort_Type.__name__=_C
_TpSnmpNotificationHostUDPPort_Object=MibTableColumn
tpSnmpNotificationHostUDPPort=_TpSnmpNotificationHostUDPPort_Object((1,3,6,1,4,1,11863,6,32,1,1,1,1,5),_TpSnmpNotificationHostUDPPort_Type())
tpSnmpNotificationHostUDPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpNotificationHostUDPPort.setStatus(_A)
class _TpSnmpNotificationHostSecMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('v1',1),('v2c',2),('v3',3)))
_TpSnmpNotificationHostSecMode_Type.__name__=_C
_TpSnmpNotificationHostSecMode_Object=MibTableColumn
tpSnmpNotificationHostSecMode=_TpSnmpNotificationHostSecMode_Object((1,3,6,1,4,1,11863,6,32,1,1,1,1,6),_TpSnmpNotificationHostSecMode_Type())
tpSnmpNotificationHostSecMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpNotificationHostSecMode.setStatus(_A)
class _TpSnmpNotificationHostSecLev_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAuthNoPriv',1),('authNoPriv',2),('authPriv',3)))
_TpSnmpNotificationHostSecLev_Type.__name__=_C
_TpSnmpNotificationHostSecLev_Object=MibTableColumn
tpSnmpNotificationHostSecLev=_TpSnmpNotificationHostSecLev_Object((1,3,6,1,4,1,11863,6,32,1,1,1,1,7),_TpSnmpNotificationHostSecLev_Type())
tpSnmpNotificationHostSecLev.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpNotificationHostSecLev.setStatus(_A)
class _TpSnmpNotificationHostNtfyType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trap',1),('inform',2)))
_TpSnmpNotificationHostNtfyType_Type.__name__=_C
_TpSnmpNotificationHostNtfyType_Object=MibTableColumn
tpSnmpNotificationHostNtfyType=_TpSnmpNotificationHostNtfyType_Object((1,3,6,1,4,1,11863,6,32,1,1,1,1,8),_TpSnmpNotificationHostNtfyType_Type())
tpSnmpNotificationHostNtfyType.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpNotificationHostNtfyType.setStatus(_A)
_TpSnmpNotificationHostRetry_Type=Integer32
_TpSnmpNotificationHostRetry_Object=MibTableColumn
tpSnmpNotificationHostRetry=_TpSnmpNotificationHostRetry_Object((1,3,6,1,4,1,11863,6,32,1,1,1,1,9),_TpSnmpNotificationHostRetry_Type())
tpSnmpNotificationHostRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpNotificationHostRetry.setStatus(_A)
_TpSnmpNotificationHostTimeout_Type=Integer32
_TpSnmpNotificationHostTimeout_Object=MibTableColumn
tpSnmpNotificationHostTimeout=_TpSnmpNotificationHostTimeout_Object((1,3,6,1,4,1,11863,6,32,1,1,1,1,10),_TpSnmpNotificationHostTimeout_Type())
tpSnmpNotificationHostTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpNotificationHostTimeout.setStatus(_A)
class _TpSnmpNotificationHostRowStatus_Type(TPRowStatus):defaultValue=4
_TpSnmpNotificationHostRowStatus_Type.__name__=_E
_TpSnmpNotificationHostRowStatus_Object=MibTableColumn
tpSnmpNotificationHostRowStatus=_TpSnmpNotificationHostRowStatus_Object((1,3,6,1,4,1,11863,6,32,1,1,1,1,11),_TpSnmpNotificationHostRowStatus_Type())
tpSnmpNotificationHostRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpNotificationHostRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'tpSnmpNotificationHost':tpSnmpNotificationHost,'tpSnmpNotificationHostTable':tpSnmpNotificationHostTable,'tpSnmpNotificationHostEntry':tpSnmpNotificationHostEntry,_G:tpSnmpNotificationHostIndex,'tpSnmpNotificationHostIpMode':tpSnmpNotificationHostIpMode,'tpSnmpNotificationHostIpAddr':tpSnmpNotificationHostIpAddr,'tpSnmpNotificationHostUserName':tpSnmpNotificationHostUserName,'tpSnmpNotificationHostUDPPort':tpSnmpNotificationHostUDPPort,'tpSnmpNotificationHostSecMode':tpSnmpNotificationHostSecMode,'tpSnmpNotificationHostSecLev':tpSnmpNotificationHostSecLev,'tpSnmpNotificationHostNtfyType':tpSnmpNotificationHostNtfyType,'tpSnmpNotificationHostRetry':tpSnmpNotificationHostRetry,'tpSnmpNotificationHostTimeout':tpSnmpNotificationHostTimeout,'tpSnmpNotificationHostRowStatus':tpSnmpNotificationHostRowStatus})