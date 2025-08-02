_K='colubrisTCPSerialConfigMIBGroup'
_J='coTCPSerialRxBytes'
_I='coTCPSerialTxBytes'
_H='coTCPSerialConnectTime'
_G='coTCPSerialRemoteTCPPort'
_F='coTCPSerialRemoteIPAddress'
_E='coTCPSerialConnectionStatus'
_D='Integer32'
_C='read-only'
_B='COLUBRIS-TCP-SERIAL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
colubrisTCPSerialMIB=ModuleIdentity((1,3,6,1,4,1,8744,5,37))
_ColubrisTCPSerialMIBObjects_ObjectIdentity=ObjectIdentity
colubrisTCPSerialMIBObjects=_ColubrisTCPSerialMIBObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,37,1))
_CoTCPSerialStatusGroup_ObjectIdentity=ObjectIdentity
coTCPSerialStatusGroup=_CoTCPSerialStatusGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,37,1,1))
class _CoTCPSerialConnectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('closed',1),('listen',2),('active',3),('idle',4),('connect',5)))
_CoTCPSerialConnectionStatus_Type.__name__=_D
_CoTCPSerialConnectionStatus_Object=MibScalar
coTCPSerialConnectionStatus=_CoTCPSerialConnectionStatus_Object((1,3,6,1,4,1,8744,5,37,1,1,1),_CoTCPSerialConnectionStatus_Type())
coTCPSerialConnectionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:coTCPSerialConnectionStatus.setStatus(_A)
_CoTCPSerialRemoteIPAddress_Type=IpAddress
_CoTCPSerialRemoteIPAddress_Object=MibScalar
coTCPSerialRemoteIPAddress=_CoTCPSerialRemoteIPAddress_Object((1,3,6,1,4,1,8744,5,37,1,1,2),_CoTCPSerialRemoteIPAddress_Type())
coTCPSerialRemoteIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coTCPSerialRemoteIPAddress.setStatus(_A)
_CoTCPSerialRemoteTCPPort_Type=Unsigned32
_CoTCPSerialRemoteTCPPort_Object=MibScalar
coTCPSerialRemoteTCPPort=_CoTCPSerialRemoteTCPPort_Object((1,3,6,1,4,1,8744,5,37,1,1,3),_CoTCPSerialRemoteTCPPort_Type())
coTCPSerialRemoteTCPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:coTCPSerialRemoteTCPPort.setStatus(_A)
_CoTCPSerialConnectTime_Type=Counter32
_CoTCPSerialConnectTime_Object=MibScalar
coTCPSerialConnectTime=_CoTCPSerialConnectTime_Object((1,3,6,1,4,1,8744,5,37,1,1,4),_CoTCPSerialConnectTime_Type())
coTCPSerialConnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:coTCPSerialConnectTime.setStatus(_A)
if mibBuilder.loadTexts:coTCPSerialConnectTime.setUnits('seconds')
_CoTCPSerialTxBytes_Type=Counter32
_CoTCPSerialTxBytes_Object=MibScalar
coTCPSerialTxBytes=_CoTCPSerialTxBytes_Object((1,3,6,1,4,1,8744,5,37,1,1,5),_CoTCPSerialTxBytes_Type())
coTCPSerialTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:coTCPSerialTxBytes.setStatus(_A)
if mibBuilder.loadTexts:coTCPSerialTxBytes.setUnits('bytes')
_CoTCPSerialRxBytes_Type=Counter32
_CoTCPSerialRxBytes_Object=MibScalar
coTCPSerialRxBytes=_CoTCPSerialRxBytes_Object((1,3,6,1,4,1,8744,5,37,1,1,6),_CoTCPSerialRxBytes_Type())
coTCPSerialRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:coTCPSerialRxBytes.setStatus(_A)
if mibBuilder.loadTexts:coTCPSerialRxBytes.setUnits('bytes')
_ColubrisTCPSerialMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
colubrisTCPSerialMIBNotificationPrefix=_ColubrisTCPSerialMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,8744,5,37,2))
_ColubrisTCPSerialMIBNotifications_ObjectIdentity=ObjectIdentity
colubrisTCPSerialMIBNotifications=_ColubrisTCPSerialMIBNotifications_ObjectIdentity((1,3,6,1,4,1,8744,5,37,2,0))
_ColubrisTCPSerialMIBConformance_ObjectIdentity=ObjectIdentity
colubrisTCPSerialMIBConformance=_ColubrisTCPSerialMIBConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,37,3))
_ColubrisTCPSerialMIBCompliances_ObjectIdentity=ObjectIdentity
colubrisTCPSerialMIBCompliances=_ColubrisTCPSerialMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,37,3,1))
_ColubrisTCPSerialMIBGroups_ObjectIdentity=ObjectIdentity
colubrisTCPSerialMIBGroups=_ColubrisTCPSerialMIBGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,37,3,2))
colubrisTCPSerialConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,37,3,2,1))
colubrisTCPSerialConfigMIBGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:colubrisTCPSerialConfigMIBGroup.setStatus(_A)
colubrisTCPSerialMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,37,3,1,1))
colubrisTCPSerialMIBCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:colubrisTCPSerialMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'colubrisTCPSerialMIB':colubrisTCPSerialMIB,'colubrisTCPSerialMIBObjects':colubrisTCPSerialMIBObjects,'coTCPSerialStatusGroup':coTCPSerialStatusGroup,_E:coTCPSerialConnectionStatus,_F:coTCPSerialRemoteIPAddress,_G:coTCPSerialRemoteTCPPort,_H:coTCPSerialConnectTime,_I:coTCPSerialTxBytes,_J:coTCPSerialRxBytes,'colubrisTCPSerialMIBNotificationPrefix':colubrisTCPSerialMIBNotificationPrefix,'colubrisTCPSerialMIBNotifications':colubrisTCPSerialMIBNotifications,'colubrisTCPSerialMIBConformance':colubrisTCPSerialMIBConformance,'colubrisTCPSerialMIBCompliances':colubrisTCPSerialMIBCompliances,'colubrisTCPSerialMIBCompliance':colubrisTCPSerialMIBCompliance,'colubrisTCPSerialMIBGroups':colubrisTCPSerialMIBGroups,_K:colubrisTCPSerialConfigMIBGroup})